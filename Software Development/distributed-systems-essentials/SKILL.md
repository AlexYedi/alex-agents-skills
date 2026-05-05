---
name: distributed-systems-essentials
description: >
  Apply the substrate-level reality of distributed systems - LAN/WAN latency,
  TCP/UDP, RPC/RMI/gRPC, partial failures, idempotence and idempotency keys,
  delivery guarantees (at-most-once / at-least-once / exactly-once), the
  Two Generals' Problem and FLP Impossibility, and the time/clock pitfalls
  that break naive ordering across nodes. Use when designing remote-call APIs,
  retry / dedup logic, time-sensitive workflows, or reasoning about why a
  remote call hung. Triggers - "why did this remote call hang", "exactly-once
  delivery", "idempotency key design", "retry with timeout", "clock skew",
  "monotonic vs wall clock", "TCP vs UDP", "gRPC vs HTTP", "partial failure",
  "FLP", "Two Generals". Produces robust remote-call designs and clear failure
  reasoning.
---

# Distributed Systems Essentials

You apply the physical, protocol, and coordination realities every distributed
system sits on top of. Networks are unreliable. Components fail individually
while the system keeps running. There is no global clock. Most distributed-system
bugs come from one of these three things being misunderstood.

This skill captures the substrate-level material from Gorton's *Foundations of
Scalable Systems* (Ch 3): the network, RPC lineage, the asynchronous-network +
crash-fault failure model, exactly-once via idempotence, and time/clocks.

---

## When to Use This Skill

- Designing or reviewing any remote-call API
- Building retry logic, deduplication, or "exactly-once" workflows
- Reasoning about why a remote call hung, returned twice, or returned a
  stale result
- Choosing between TCP / UDP / HTTP / gRPC for a service contract
- Debating timestamps, clocks, or ordering across nodes

---

## The Network You're Actually On

| Hop type | Latency floor | Bandwidth | Notes |
|---|---|---|---|
| Same socket | sub-µs | n/a | In-process |
| Same host | µs | very high | localhost loopback |
| Same datacenter (LAN) | ~0.5–1 ms | 10–100 Gbps | Sub-ms typical |
| Same region (WAN) | 5–20 ms | 1–10 Gbps | Bounded by speed of light in fiber |
| Cross-region (transcontinental) | 60–200 ms | 100 Mbps–1 Gbps | The "around the world is ~140 ms" rule |
| Cellular last-mile | +20–100 ms | variable | Highly bimodal — great or terrible |

**The speed-of-light floor in fiber:** ~5 µs/km. NYC → London ≈ 28 ms one way
*minimum*. There is no engineering trick that beats physics.

**Implication:** Latency-sensitive paths must be co-located. Multi-region for
reads is fine; multi-region for synchronous transactions is expensive
(see `consensus-and-strong-consistency` for Spanner / TrueTime).

---

## TCP, UDP, and Sockets

| Protocol | Guarantees | Use when |
|---|---|---|
| **TCP** | Reliable, in-order, connection-oriented, congestion-controlled | Almost everything. The default. |
| **UDP** | Unreliable, datagram, no ordering, no congestion control | DNS, NTP, video/audio streaming, custom reliable protocols (QUIC) |
| **Sockets** | Bidirectional byte stream — the OS-level pipe | You should rarely write to this directly. Use a higher abstraction. |

**Reuse TLS connections.** Connection establishment is expensive; in-flight
encryption is cheap thanks to modern CPU AES instructions. Connection pools
(HTTP keep-alive, JDBC pools, gRPC channels) are not optional optimizations
— they are correctness for high-throughput systems.

---

## RPC / RMI: A Brief Lineage

```
1985–1990   DCE-RPC                  C/C++ on Unix; cross-host RPC
1991        CORBA                    Cross-language IDL; complex
mid-90s     Java RMI                 Java-to-Java; stub/skeleton; serialization
2000s       XML web services         WSDL contracts; SOAP envelopes; verbose
2010s       JSON over HTTP / REST    The de-facto modern simplification
2016+       gRPC                     HTTP/2 + Protobuf; bidirectional streaming
```

**The constants:**

- A **stub** marshals call arguments and sends bytes; a **skeleton**
  unmarshals on the other side.
- Marshalling = serializing. Unmarshalling = deserializing. Both fail subtly
  at type-system boundaries (e.g., Java Long → JS number losing precision).
- **Location transparency** is the goal — call as if local. The lie: it isn't.

**When to pick which:**

| Scenario | Pick |
|---|---|
| Public API for third parties | HTTP + JSON (REST or RPC-flavored) |
| High-throughput service-to-service inside one company | gRPC over HTTP/2 |
| Streaming bidirectional | gRPC, WebSockets |
| Java-to-Java legacy | Java RMI (probably maintenance-only) |
| Cross-language enterprise | gRPC; CORBA only if you must |

---

## Partial Failures: The Hardest Thing in Distributed Systems

```
Client                                            Server
  │                                                  │
  │── request ────────────────────────────────────→  │
  │                                                  │ ── starts work
  │                                                  │
  │     (no response yet — what happened?)           │
  │                                                  │
  │     • Server is slow                             │
  │     • Server crashed mid-work                    │
  │     • Network dropped the request                │
  │     • Network dropped the response               │
  │     • Server completed successfully and          │
  │       the response is on its way                 │
  │                                                  │
  │     The client cannot distinguish these.         │
```

**Crash faults + asynchronous network:** the canonical failure model.

| Outcome | What client knows |
|---|---|
| Response received | Success (assuming response says so) |
| Connection refused / reset | Server didn't accept the request — safe to retry |
| Read timeout | **Unknown.** Could be processed, could be dropped — retry only if idempotent |
| 5xx error | Operation may or may not have happened — retry only if idempotent |

**Implication:** Every mutating endpoint must be **idempotent**, or you must
build dedup at the application layer.

> "Failures that can be detected quickly are easy to deal with."

---

## Delivery Guarantees

```
At-most-once       At-least-once       Exactly-once
─────────────       ─────────────       ────────────
Fire-and-forget     TCP, ack/retry      Idempotency keys
                                        OR enable.idempotence

May lose            Won't lose          Application sees one
May duplicate? No   May duplicate? Yes  effect per logical event
```

**Exactly-once does not mean "no transmission failures."** It means the
*effect* is observed exactly once. Transmissions and retries still happen
underneath; the application layer dedups.

---

## Idempotency Keys: The Practical Pattern

**Every mutating endpoint** that can be retried — directly by clients, by
proxies, by message-broker redelivery — needs idempotency at the application
layer.

```
┌────────────┐    1. POST /charge                   ┌────────────┐
│  Client    │       Idempotency-Key: u8eY9k        │  Server    │
│            │       { amount: 100 }                │            │
│            │ ──────────────────────────────────→  │            │
│            │                                      │            │
│            │                                      │  Has key   │
│            │                                      │  been seen?│
│            │                                      │     │      │
│            │                                      │     ▼      │
│            │                                      │   ┌────┐   │
│            │                                      │   │ No │   │
│            │                                      │   └────┘   │
│            │                                      │     │      │
│            │                                      │  Process,  │
│            │                                      │  store     │
│            │                                      │  (key→     │
│            │                                      │   result)  │
│            │ ←──────────────────────────────────  │            │
│            │       2. 200 { id: charge_42 }       │            │
│            │                                      │            │
│ network drops response                            │            │
│            │                                      │            │
│            │ 3. POST /charge (retry)              │            │
│            │       Idempotency-Key: u8eY9k        │            │
│            │ ──────────────────────────────────→  │            │
│            │                                      │ Has key    │
│            │                                      │ been seen? │
│            │                                      │   YES →    │
│            │                                      │ return     │
│            │                                      │ stored     │
│            │                                      │ result     │
│            │ ←──────────────────────────────────  │            │
│            │       4. 200 { id: charge_42 }       │            │
└────────────┘                                      └────────────┘
```

**Key design:**

| Field | Why |
|---|---|
| User / session ID | Prevent cross-user collision |
| UUID or timestamp+sequence | Uniqueness within user |
| TTL (60 min – 24 h) | Bounded storage; long enough for client retries |

**Storage requirements:**

- Fast lookup (Redis, DynamoDB, Memcached).
- **Application update + key write must be transactional** — either both happen
  or neither. Otherwise dedup silently fails.

**Use cases that *demand* idempotency keys:**
- Payment / charge endpoints (Stripe, Square — they require this)
- Fulfillment ("place order")
- Account creation
- Anything where a duplicate is a real-world double-effect

---

## Time and Clocks

| Clock | Provided by | Properties | Use for |
|---|---|---|---|
| **Wall-clock / time-of-day** | NTP-disciplined OS clock | Can jump (forward or **backward**) when NTP corrects | Logging, displaying to users |
| **Monotonic** | Hardware tick counter | Only moves forward; never returns | Measuring elapsed time, timeouts |

**Java:**
- `System.currentTimeMillis()` → wall-clock (do **not** subtract for elapsed!)
- `System.nanoTime()` → monotonic (correct for elapsed)

**Cross-node ordering by timestamp is broken.**

```
Node A clock      Node B clock
─────────────     ─────────────
12:00:00.000      11:59:59.500   ← 500 ms behind A
                                   (NTP-disciplined within ~100 ms,
                                    but skew across geographically
                                    distant nodes is much worse)

A writes "X" at 12:00:00.000
B writes "Y" at 11:59:59.500
By timestamp, B < A.
By real (wall-clock-as-it-actually-happened) time, A may be earlier.
```

**Tools:**

| Service | Accuracy | Notes |
|---|---|---|
| NTP | ~10–100 ms typical | Internet-wide |
| Chrony | ~1–10 ms | Linux replacement for ntpd |
| Amazon Time Sync Service | ~1 ms | EC2-internal |
| Google TrueTime | ~7 ms bounded | Spanner only — GPS + atomic clocks |

**Rule:** Don't trust cross-node timestamps for ordering. Use logical clocks
(version vectors, Lamport timestamps), per-partition sequence numbers, or
TrueTime + commit-wait if you have it (see `consensus-and-strong-consistency`).

---

## Two Generals' Problem and FLP Impossibility

These are the theoretical limits.

**Two Generals' Problem:** Two armies on opposite hills must coordinate an
attack. Messengers can be captured. Each side wants confirmation that the
other will attack. There is no number of confirmations that produces certainty
on both sides.

**Implication:** Coordinating actions across two parties on a lossy channel
cannot guarantee mutual agreement in bounded time. Don't try.

**FLP Impossibility (Fischer–Lynch–Paterson, 1985):** In an asynchronous
network with even one crash-faulty process, no deterministic algorithm can
guarantee consensus in bounded time.

**Implication:** Practical consensus algorithms (Paxos, Raft) terminate in
*expected* bounded time but make assumptions (timeouts, fail-stop) to escape
FLP. Don't expect true consensus over the open internet without one of those
assumptions.

**Byzantine faults** — malicious failures — are out of scope here. Inside
trusted enterprise networks, assume crash faults only.

---

## Principles

- **Networks are unreliable.** Assume any call can fail, time out, or arrive
  twice. Design accordingly.
- **Partial failure is the normal case.** Don't write code that assumes binary
  success/failure.
- **Make every mutating endpoint idempotent.** Retries are not optional in
  distributed systems; idempotency is the cost of admission.
- **Implement exactly-once at the application layer.** TCP gives at-least-once;
  idempotency keys give exactly-once.
- **Don't trust cross-node timestamps.** Use logical clocks or per-partition
  sequence numbers for ordering.
- **Reuse connections.** Establishing them is expensive; in-flight encryption
  is cheap.
- **Don't write to raw sockets.** Use a higher abstraction unless you have
  a specific reason.
- **Co-locate latency-sensitive paths.** Speed of light is real.

---

## Anti-Patterns

### Naive Retry Without Idempotency

**Looks like:** Client gets a 500. Retries the POST. Server processes it twice.
Customer is double-charged.

**Why it fails:** The client cannot distinguish "request lost" from "response
lost." Naive retry assumes the former.

**The fix:** Idempotency key on every mutating endpoint. Retry only when key
is set.

### Subtracting Wall-Clock for Elapsed Time

**Looks like:** `long start = currentTimeMillis(); ...; long elapsed =
currentTimeMillis() - start;`

**Why it fails:** NTP can jump the clock backward mid-operation. `elapsed`
becomes negative and breaks downstream logic.

**The fix:** Use `nanoTime()` for elapsed time. Use `currentTimeMillis()` only
for absolute timestamps.

### Cross-Node Ordering by Timestamp

**Looks like:** Distributed log "ordered" by `logged_at`. Or "last write wins"
on objects with timestamps from multiple nodes.

**Why it fails:** Nodes can have 10–100 ms+ clock skew. Order is unreliable.
Concurrent writes silently overwrite each other.

**The fix:** Logical clocks (version vectors). Per-partition sequence numbers.
Or, if you really need linearizability, TrueTime + commit-wait.

### Long Read Timeouts

**Looks like:** HTTP client with a 30-second read timeout, calling a service
that should answer in <100 ms.

**Why it fails:** A slow downstream takes the whole thread for the entire
30-second window. Thread pool exhausts. Caller fails too.

**The fix:** Set read timeout near P99 + headroom. Fail fast. (See
`microservices-resilience-patterns`.)

### Trying to Coordinate on a Lossy Channel

**Looks like:** "We'll send a confirmation, then they'll send a confirmation
of the confirmation, and we're sure."

**Why it fails:** Two Generals' Problem. There is no finite number of
confirmations that gets you to certainty on both sides.

**The fix:** Accept that you can't have it. Use idempotent operations + at-
least-once delivery + reconciliation.

---

## Decision Rules

| Situation | Action |
|---|---|
| Calling a remote service | Set tight read timeout. Make caller idempotent if you'll retry. |
| Building a payment / fulfillment endpoint | Idempotency key required. Transactional dedup table + business write. |
| Choosing a service-to-service protocol | gRPC for internal; HTTP+JSON for public. |
| Logging timestamps for ordering across nodes | Don't. Use logical clocks or per-partition sequence numbers. |
| Measuring elapsed time | Monotonic clock (`nanoTime()`). |
| Cross-region latency-sensitive workload | Don't. Replicate close to users; eventual consistency. |
| Need exactly-once delivery | At-least-once + idempotency key. There is no protocol that gives exactly-once on its own. |

---

## Worked Example: Designing a Payment Endpoint

**Context:** External clients can call `POST /v1/charge` to charge a card.
Network can drop responses; clients retry on timeout.

**Design:**

1. **Required header:** `Idempotency-Key: <client-generated UUID>`. Reject
   requests without it (HTTP 400).
2. **Storage:** Postgres table `idempotency_keys (key, user_id, status,
   response_body, created_at)` with a unique index on `(user_id, key)`.
3. **Flow:**
   - Begin transaction.
   - `SELECT FOR UPDATE` from `idempotency_keys` where key matches.
   - If row exists with `status=COMPLETED`: return stored response.
   - If row exists with `status=IN_PROGRESS`: return 409 (concurrent).
   - If no row: insert with `status=IN_PROGRESS`, perform charge, update with
     `status=COMPLETED` and stored response, commit.
4. **TTL:** Cron deletes keys older than 24 hours.
5. **Read timeout:** Clients should set 5 s; we respond within 2 s P99.

**Result:** Network drop or client retry produces at most one charge. Stripe
and Square's `Idempotency-Key` headers are exactly this pattern.

---

## Gotchas

- **Idempotency only works if the dedup write and the business write are in
  the same transaction.** Otherwise a crash between them produces duplicate
  effects.
- **Idempotency keys must be scoped to the client/user.** Otherwise one user's
  retry can collide with another's.
- **Marshalling fails subtly across languages.** Java `Long` → JS `number`
  loses precision above 2^53. UUIDs are safer than 64-bit ints across
  language boundaries.
- **Out-of-order packet delivery is normal under packet switching.** TCP
  reassembles for you; UDP doesn't. Don't assume order if you're using UDP.
- **Cross-node clock drift breaks order-by-timestamp logic** even when
  drift is small (10s of ms). Logical clocks are the answer.
- **`exactly-once` is a marketing word.** Read carefully — usually it means
  "at-least-once with broker-side dedup," which is fine, but know what you're
  buying.

---

## Related Skills

- `concurrent-systems-foundations` — single-node concurrency below this layer
- `scalability-foundations` — when and why to add distributed pieces
- `consensus-and-strong-consistency` — Paxos/Raft and how they escape FLP
- `eventual-consistency-mechanics` — what you get when you avoid consensus
- `asynchronous-messaging-patterns` — at-least-once + idempotency in messaging
- `event-streaming-with-kafka` — Kafka's `enable.idempotence` model
- `microservices-resilience-patterns` — read timeouts, circuit breakers

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 3.
