---
name: concurrent-systems-foundations
description: >
  Apply per-node concurrency primitives correctly - threads, race conditions,
  critical sections, monitor locks, deadlocks, producer-consumer with
  blocking queues, thread pools (ExecutorService), barrier synchronization
  (CountDownLatch), and the difference between Java's threading model, Go's
  CSP / goroutines, Erlang's actors, and Node.js's event loop. Use when
  designing concurrent code, diagnosing race conditions or deadlocks,
  choosing a concurrency model, or sizing thread pools. Triggers - "race
  condition", "deadlock", "dining philosophers", "thread pool sizing",
  "synchronized vs lock", "Goroutines / channels", "actor model",
  "CountDownLatch / barrier", "BlockingQueue", "Amdahl's law in concurrent
  code". Produces correct, predictable concurrent designs.
---

# Concurrent Systems Foundations

You design and review concurrent code at the per-node level. Distributed
scalability is bounded by how well your nodes use their cores — Amdahl's law
caps the system at the serialized fraction of work. Per-node concurrency
mistakes are race conditions and deadlocks; they're intermittent, hard to
reproduce, and easy to ship.

This skill captures the per-node concurrency material from Gorton's
*Foundations of Scalable Systems* (Ch 4): the Java threading primitives, the
canonical pitfalls (race conditions, deadlocks via dining philosophers), the
high-level abstractions in `java.util.concurrent`, and the alternative
concurrency models (Go, Erlang, Node.js).

---

## When to Use This Skill

- Designing or reviewing concurrent code on the JVM (or analogous platforms)
- Diagnosing intermittent test failures, race conditions, or deadlocks
- Sizing thread pools for an application server or a worker
- Choosing between concurrency models (threads vs CSP vs actors vs event loop)
- Diagnosing why "more cores" didn't make code faster (Amdahl)

---

## The Mental Model

```
A concurrent program has N threads sharing memory.

The OS scheduler interleaves threads NONDETERMINISTICALLY.

Anything that touches shared mutable state without
explicit coordination CAN AND WILL race.
```

| Term | Meaning |
|---|---|
| **Thread** | An OS-scheduled execution context within a process |
| **Race condition** | Interleaved access to shared state produces wrong, intermittent results |
| **Critical section** | Code that mutates shared state and must execute atomically |
| **Monitor lock / synchronized / intrinsic lock** | Java's per-object lock — only one thread at a time inside a synchronized block on that object |
| **Deadlock / deadly embrace** | Circular wait on locks acquired in inconsistent order |
| **Thread state** | Created → Runnable → Blocked → Terminated, with preemption + time-slicing |

**Critical sections are the serialized fraction Amdahl's law penalizes.**
A small critical section is a small Amdahl penalty; a large one caps your
scalability. Keep them small.

---

## Java Threading Primitives

```
class Worker implements Runnable {
    public void run() { /* work */ }
}

Worker w = new Worker();
new Thread(w).start();    // ← creates a new execution context
new Thread(w).run();      // ← STAYS IN THE CURRENT THREAD! Common bug.
```

**The `start()` vs `run()` trap:** `start()` creates a thread; `run()`
calls the method directly in the current thread. Calling `run()` silently
turns multi-threaded code into single-threaded code. The bug is invisible
until load is high.

**Thread coordination:**

| Primitive | Use |
|---|---|
| `synchronized` block / method | Critical section guarded by an object's monitor lock |
| `wait()` / `notify()` / `notifyAll()` | Low-level signaling. Almost always replaced by higher-level abstractions today. |
| `Thread.join()` | Wait for another thread to complete. The right way to coordinate "wait until done." |
| `Thread.sleep()` | **Never** for coordination. Use latches and barriers. |

> "If you are using absolute times for thread coordination, you are doing it
> wrong. Almost always."

---

## The Race Condition Anatomy

```
Thread A          Shared counter = 0          Thread B
─────────                                     ─────────
read 0 ───────►   ┌──────┐
                  │  0   │   ◄─────────────── read 0
+1                └──────┘                    +1
                  ┌──────┐
write 1 ────────► │  1   │   ◄─────────────── write 1
                  └──────┘
                                              Result: 1
                                              Expected: 2
                                              **Lost update**
```

**The fix — atomic critical section:**

```java
synchronized (counterLock) {
    counter++;       // read-modify-write, now atomic
}
```

Or use `AtomicInteger.incrementAndGet()` — same effect, lock-free, faster.

**Race conditions are insidious because they pass small tests and fail in
production.** Stress-test concurrent code with many more threads than cores.

---

## Deadlocks: Dining Philosophers

```
            Philosopher 1
               (left fork: A, right fork: B)
            ┌─────────────┐
       A → │              │ ← B
            └─────────────┘
                   │
        ┌──────────┼──────────┐
        │                     │
  Philosopher 4         Philosopher 2
   (left: D,             (left: B,
    right: A)             right: C)
        │                     │
        └──────────┬──────────┘
                   │
            Philosopher 3
            (left: C, right: D)

   Each tries to pick up left fork, then right fork.
   All pick up left → all wait for right → DEADLOCK.
```

**The fix — global lock-acquisition order:**

```java
// Always acquire the LOWER-NUMBERED fork first.
Fork first  = (leftFork.id < rightFork.id) ? leftFork  : rightFork;
Fork second = (leftFork.id < rightFork.id) ? rightFork : leftFork;
synchronized (first) {
    synchronized (second) {
        eat();
    }
}
```

By imposing a total order on lock acquisition, no philosopher can hold a
higher-numbered fork while waiting for a lower-numbered one — the cycle is
broken.

**Conditions for deadlock (Coffman):** mutual exclusion + hold-and-wait +
no preemption + circular wait. Break any one. Lock ordering breaks circular
wait; this is the easiest fix.

---

## Producer-Consumer with `BlockingQueue`

The single most useful pattern for in-process concurrent work.

```
Producer threads             Consumer threads
─────────────────            ──────────────────
                  ┌───────┐
   put(task) ────►│ FIFO  │────► take() (blocks if empty)
                  │ queue │
   put(task) ────►│       │────► take()
                  └───────┘
            (blocks if full)
```

```java
BlockingQueue<Task> q = new LinkedBlockingQueue<>(1000);

// Producer
q.put(task);     // blocks if full (backpressure)

// Consumer
Task t = q.take();   // blocks if empty
```

**Why this beats hand-rolled `wait()/notify()`:**

- Thread-safe by construction.
- Backpressure built-in: when full, producers block.
- No race conditions — the buffer is the synchronization point.

---

## Thread Pools (ExecutorService)

```
┌────────────┐    ┌────────────┐
│  Caller    │    │  Caller    │
│  thread    │    │  thread    │
└──────┬─────┘    └──────┬─────┘
       │ submit(task)    │
       ▼                 ▼
   ┌──────────────────────────┐
   │   Task queue (bounded)   │
   └──────────┬───────────────┘
              │
   ┌──────────┴───────────┐
   ▼          ▼           ▼
 ┌────┐    ┌────┐      ┌────┐
 │W1  │    │W2  │ ...  │Wn  │     ← pre-allocated worker threads
 └────┘    └────┘      └────┘
```

```java
ExecutorService pool = Executors.newFixedThreadPool(16);
Future<Result> f = pool.submit(() -> compute(...));
Result r = f.get();   // blocks until done
```

**Sizing rules of thumb:**

| Workload | Pool size |
|---|---|
| CPU-bound | ≈ number of physical cores |
| I/O-bound (mostly waiting) | Much larger (10×–100× cores). Tune empirically. |
| Mixed | `cores × (1 + wait_time / cpu_time)` |

**Tomcat default:** 25 minimum, configurable max. Most app servers expose
this as a config knob.

**Why pools beat per-task threads:** Thread creation costs ~milliseconds and
hundreds of KB of stack memory. A pool amortizes both.

---

## Barrier Synchronization (CountDownLatch)

When N threads must all reach a point before any continues.

```java
int N = 10;
CountDownLatch latch = new CountDownLatch(N);

// Each worker
for (int i = 0; i < N; i++) {
    pool.submit(() -> {
        doPhaseOne();
        latch.countDown();    // mark this worker done with phase 1
        latch.await();        // wait for all to finish phase 1
        doPhaseTwo();
    });
}
```

Use cases: parallel reduce, multi-phase init, "warm-up complete" barriers
in benchmark code.

**Don't use `Thread.sleep()` to wait for "everyone to be ready."** That's the
absolute-time anti-pattern. Use a latch or barrier.

---

## Concurrency Models: Beyond Java Threads

| Model | Example languages | How it works | Strength |
|---|---|---|---|
| **Threads + shared memory + locks** | Java, C++, C#, Python (with GIL), Rust | OS threads share heap; locks coordinate | Direct mapping to hardware; familiar; race-prone |
| **CSP (Communicating Sequential Processes)** | Go (goroutines + channels), Clojure (core.async) | Lightweight threads communicate by sending values over channels; "share memory by communicating, don't communicate by sharing memory" | Race-resistant; structured concurrency; cheap goroutines |
| **Actor model** | Erlang/Elixir, Akka (Scala/Java) | Independent actors with mailboxes; only message passing, no shared state | Fault tolerance; supervision trees; distribution-friendly |
| **Single-threaded event loop** | Node.js, Python asyncio, browser JS | One thread, async I/O, callbacks/promises/await | No race conditions on shared state; great for I/O-bound; bad for CPU-bound |

**When to pick which:**

- **CPU-bound Java/JVM service:** threads + ExecutorService.
- **Highly concurrent I/O-bound service in Go/Elixir:** use the platform's
  native model (goroutines, actors). Don't fight it.
- **Web server handling many idle connections:** event loop (Node, Python
  asyncio) or coroutines.
- **Distributed fault-tolerant system:** actor model maps cleanly across nodes
  (Akka, Erlang OTP).

**The Java trap:** It's tempting to bolt async-style code onto a Java thread
pool. CompletableFuture, reactive streams, virtual threads (JDK 21+) — all
useful, but each has its own model. Pick one and stick with it per service.

---

## Principles

- **Critical sections must stay small.** They're the Amdahl bottleneck.
- **Prefer high-level abstractions.** `BlockingQueue`, `ExecutorService`,
  `CountDownLatch`, `AtomicInteger`, `ConcurrentHashMap` over hand-rolled
  `wait()`/`notify()` and explicit locks.
- **Never coordinate threads with absolute sleep times.** Use latches,
  barriers, or `join()`.
- **Impose a global lock-acquisition order** to prevent deadlocks.
- **Stress-test concurrent code** with many more threads than cores. Bugs
  hide at low concurrency.
- **Keep shared mutable state to a minimum.** Immutability + message passing
  scale better than locks.
- **Match the concurrency model to the language.** Don't write Java like Go.

---

## Anti-Patterns

### Calling `run()` Instead of `start()`

**Looks like:** `new Thread(worker).run();`

**Why it fails:** Stays in the calling thread. Code is silently single-threaded.
Bug invisible until profiled.

**The fix:** `start()`. Always.

### Locking Too Much

**Looks like:** `synchronized` on the whole method, even though only two lines
mutate shared state.

**Why it fails:** Critical section is huge. Throughput collapses under
contention. Amdahl ceiling drops.

**The fix:** Synchronize the smallest possible region. Use `ConcurrentHashMap`
and atomic types instead of broad locks.

### Inconsistent Lock Order

**Looks like:** Method A locks X then Y; method B locks Y then X.

**Why it fails:** Under load, A holds X, B holds Y, both wait forever. Classic
dining philosophers.

**The fix:** Document a total order on locks. Always acquire in that order.
Lint or code-review for violations.

### `Thread.sleep()` for Coordination

**Looks like:** "Wait, the worker should be ready by now... sleep(1000)..."

**Why it fails:** Brittle. Slow on healthy machines, race-prone on slow ones.

**The fix:** `CountDownLatch`, `CyclicBarrier`, or `Future.get()`.

### Unbounded Thread Pool

**Looks like:** `Executors.newCachedThreadPool()` for a public-facing service.
Under traffic spike, pool grows to 10,000 threads. OOM.

**Why it fails:** No backpressure. Each thread costs hundreds of KB. Server
dies.

**The fix:** Bounded pool with bounded queue. Reject or backpressure on
overflow.

### Calling Blocking Code in an Event Loop

**Looks like:** `await fs.readFileSync(...)` inside a Node.js handler. Or a
synchronous DB call in a Tornado coroutine.

**Why it fails:** Blocks the single event-loop thread. Whole server stalls.

**The fix:** Use the async API. If unavoidable, run blocking code in a
worker thread pool.

---

## Decision Rules

| Situation | Action |
|---|---|
| Java service, mostly CPU-bound | `ExecutorService` with pool size ≈ cores |
| Java service, mostly I/O-bound | Larger pool, or virtual threads (JDK 21+), or async API |
| Need atomic counter / map | `AtomicInteger`, `ConcurrentHashMap` (lock-free) |
| Multi-stage parallel computation | `CountDownLatch` or `CyclicBarrier` for phase boundaries |
| Producer / consumer in process | `LinkedBlockingQueue` |
| Greenfield highly concurrent service | Pick the language model: Go (CSP), Elixir (actors), Java (threads + pools), Node (event loop) |
| Diagnosing intermittent failure under load | Suspect race condition. Add stress test with 10× the production thread count. |
| Diagnosing hang under load | Suspect deadlock. Take a thread dump. Look for two threads each holding a lock the other wants. |

---

## Worked Example: Web Crawler with Bounded Concurrency

**Goal:** Crawl up to 10,000 URLs in parallel with at most 50 concurrent HTTP
requests.

**Design:**

```java
ExecutorService pool = Executors.newFixedThreadPool(50);
BlockingQueue<URL> toVisit = new LinkedBlockingQueue<>();
Set<URL> visited = ConcurrentHashMap.newKeySet();
CountDownLatch done = new CountDownLatch(targetCount);

while (!toVisit.isEmpty() && visited.size() < targetCount) {
    URL u = toVisit.take();
    if (!visited.add(u)) continue;        // skip if already visited
    pool.submit(() -> {
        try {
            String html = fetch(u);
            for (URL link : extractLinks(html)) toVisit.put(link);
        } catch (Exception e) {
            log.warn("fetch failed", e);
        } finally {
            done.countDown();
        }
    });
}

done.await();
pool.shutdown();
```

**What this gets right:**
- Bounded pool → bounded resource use.
- `ConcurrentHashMap.newKeySet()` for thread-safe dedup without explicit lock.
- `LinkedBlockingQueue` for backpressure.
- `CountDownLatch` for clean termination.

**What we avoided:**
- Unbounded thread pool (OOM).
- Synchronized blocks around the visited set (would serialize the fast path).
- `Thread.sleep()` to "give time for things to start."

---

## Gotchas

- **`HashMap` is not thread-safe.** `ConcurrentHashMap` is. `Vector` and
  `Hashtable` are technically thread-safe but coarsely locked and slow.
- **Java `synchronized` is reentrant.** A thread already holding a lock can
  re-acquire it. Don't rely on this; design without recursion across locked
  methods.
- **`volatile` is not a substitute for synchronization.** It guarantees
  visibility of writes, not atomicity of read-modify-write.
- **Java memory model surprises:** without proper synchronization, threads
  can see stale values indefinitely. Use `synchronized`, `volatile`, or
  `AtomicXxx`.
- **Garbage collection pauses can mimic deadlock.** A 5-second GC stop-the-world
  looks like a hang. Check GC logs before chasing locks.
- **Thread dumps in production** are the diagnostic tool for hangs. Take one
  with `jstack <pid>`.

---

## Related Skills

- `scalability-foundations` — Amdahl's law and the per-node ceiling
- `distributed-systems-essentials` — coordination across nodes
- `load-balancing-and-app-services` — application-server thread pools
- `asynchronous-messaging-patterns` — channel pools, thread-per-channel
  semantics

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 4. Brian
Goetz's *Java Concurrency in Practice* is the canonical deeper reference.
