---
name: microservices-resilience-patterns
description: >
  Apply microservices runtime resilience patterns - fail fast (read timeouts
  at P99), circuit breakers (CLOSED / OPEN / HALF_OPEN), bulkheads
  (partitioned thread pools per API), exponential backoff, default /
  fallback responses, API gateway throttling, and how to combine them as
  defense-in-depth against cascading failures triggered by slow
  dependencies. Use when designing or hardening service-to-service calls,
  diagnosing cascading failures, choosing an API gateway, or auditing a
  microservices system for runtime resilience. Triggers - "circuit breaker",
  "bulkhead pattern", "fail fast", "cascading failure", "long-tail
  latency", "API gateway", "exponential backoff", "fallback response",
  "Hystrix", "resilience4j", "polly". Produces a concrete defense-in-depth
  plan for a microservices call path.
---

# Microservices Resilience Patterns

You design and audit the runtime defenses that keep microservices systems
from cascading into outage. Microservices are coupled distributed systems —
a slow database doesn't just slow down one service, it propagates back
through the call chain and exhausts thread pools at every tier. This skill
captures the runtime patterns that prevent that.

This is the operationally critical content from Gorton's *Foundations of
Scalable Systems* (Ch 9): cascading failures triggered by *slow* responses
(not outright failures), long-tail latency profiles, and the layered defense
of fail-fast / circuit breaker / bulkhead / exponential backoff.

This skill complements `distributed-system-patterns` (Saga, Sidecar, BFF,
Service Mesh) — that one is about *architectural* patterns, this one is
about *runtime fault tolerance* between services.

---

## When to Use This Skill

- Designing or hardening any service-to-service call path
- Diagnosing cascading failures (one slow service taking down the rest)
- Auditing an existing microservices system for resilience
- Choosing or configuring an API gateway
- Setting timeouts, retry policies, and fallback behaviors

---

## The Cascading Failure: Why Slow Is Worse Than Failed

```
Time:  0 ─────────────────────────────────────────────────────────────►
                                                                      
       ┌─────────────────────────────────┐
       │  Backend DB: 5 s slowdown       │
       └─────────────────────────────────┘
                  │
                  ▼ (every Service C call hangs)
       ┌─────────────────────────────────┐
       │  Service C: thread pool fills   │
       │  with hung requests             │
       └─────────────────────────────────┘
                  │
                  ▼ (Service B's calls to C also hang)
       ┌─────────────────────────────────┐
       │  Service B: thread pool fills   │
       │  with hung requests             │
       └─────────────────────────────────┘
                  │
                  ▼ (Service A's calls to B also hang)
       ┌─────────────────────────────────┐
       │  Service A: thread pool fills   │
       │  with hung requests             │
       └─────────────────────────────────┘
                  │
                  ▼
       ┌─────────────────────────────────┐
       │  Whole system: 5xx errors       │
       └─────────────────────────────────┘
```

> "The insidious nature of cascading failures is that they are triggered by
> *slow* response times of dependent services."

**Why slow is worse than failed:**

| | Failed (connection refused / 500) | Slow (no response in 30 s) |
|---|---|---|
| Caller's response time | Fast (immediate error) | 30 seconds |
| Caller's thread cost | Returns immediately | Held for the full duration |
| Thread pool pressure | None | Climbs linearly with request rate |
| Failure mode | Easy to detect | Looks like normal operation until pool exhausts |
| Mitigation | Easy — return error fast | Hard — depends on caller's timeout |

**Implication:** Default timeouts (often 60 s, 5 min, or unlimited) are the
silent killer. The first defense is fail-fast.

---

## Long-Tail Response Times

```
Frequency
  │
  │ ████
  │ ████
  │ ████
  │ ████ ██
  │ ████ ██
  │ ████ ██ █
  │ ████ ██ █  █                              █
  │ ████ ██ █  █  █  █                              █
  └──────────────────────────────────────────────────────►
   1ms  10ms  100ms 1s  10s  60s    Latency

      P50           P95     P99   P99.9
```

**Real workloads exhibit long-tail latency.** A small percentage of requests
take 20–100× the average, due to:

- GC pauses
- Thread / lock contention
- Page faults
- Dropped TCP packets requiring retransmission
- Network microbursts
- Backend warmup / JIT compilation

**Implication:** Set timeouts based on P99 (or P99.9 for critical paths) +
headroom. Don't size for averages — outliers cluster and cascade.

---

## The Defense-in-Depth Stack

```
┌─────────────────────────────────────────────────────────────────────┐
│                  Defense-in-Depth Stack                              │
│                                                                      │
│  1. Tight read timeouts (P99 + headroom)                             │
│         ↓ fail fast                                                  │
│                                                                      │
│  2. Circuit breaker around dependency                                │
│         ↓ stop calling broken thing                                  │
│                                                                      │
│  3. Bulkhead per API endpoint                                        │
│         ↓ contain blast radius                                       │
│                                                                      │
│  4. Default / fallback response                                      │
│         ↓ degrade gracefully                                         │
│                                                                      │
│  5. Exponential backoff on retries                                   │
│         ↓ avoid retry storms                                         │
│                                                                      │
│  6. API gateway throttling                                           │
│         ↓ cap total upstream pressure                                │
└─────────────────────────────────────────────────────────────────────┘
```

Each layer covers a failure mode the next can't.

---

## 1. Fail Fast — Read Timeouts

Set client-side read timeouts for every remote call.

```python
import requests

resp = requests.get(
    "https://order-service/orders/42",
    timeout=(0.5, 2.0)   # 500ms connect, 2s read
)
```

**Setting the timeout:**

| Step | Action |
|---|---|
| 1 | Measure the dependency's P99 (or P99.9 for critical paths) |
| 2 | Add headroom (1.5×–2× P99) |
| 3 | Make sure callers' timeouts are *smaller* than their callers' (cascading timeout budget) |

**The cascading timeout budget:** if Service A has a 2 s timeout to Service B,
B's calls to C should have ≤1.5 s timeout (so B can return an error to A
before A times out). Otherwise the timeouts pile up and A times out before B
returns its error.

```
A → B (timeout 2 s)
        B → C (timeout 1.5 s)        ← must be < A's timeout
                C → DB (timeout 1 s) ← must be < B's timeout
```

---

## 2. Circuit Breaker

Wraps a dependency call. After repeated failures, the breaker **opens** —
all further calls fail fast without trying the dependency. After a cool-down
period, it goes **half-open**, lets one trial through; if it succeeds, the
breaker **closes** and normal operation resumes.

```
                ┌────────────────────────────┐
                │         CLOSED             │
                │  (normal operation)        │
                │                            │
                │  Track recent failures     │
                └─────────┬──────────────────┘
                          │ failure rate exceeds threshold
                          ▼
                ┌────────────────────────────┐
                │          OPEN              │
                │  (fail fast immediately)   │
                │                            │
                │  Don't even try the call   │
                └─────────┬──────────────────┘
                          │ recovery timeout elapses
                          ▼
                ┌────────────────────────────┐
                │      HALF_OPEN             │
                │  (probe the dependency)    │
                │                            │
                │  Let one call through;     │
                │  measure result            │
                └─────────┬──────────────────┘
                  success │ │ failure
                  ↓       │ │ ↓
              CLOSED      └─┴── OPEN
```

**Python example with `circuitbreaker`:**

```python
from circuitbreaker import circuit

@circuit(failure_threshold=5, recovery_timeout=30)
def call_inventory_service(item_id):
    return requests.get(f"https://inventory/items/{item_id}", timeout=2.0)
```

**Common parameters:**

| Param | Typical |
|---|---|
| Failure threshold | 5–20 errors in window |
| Window | 10–60 seconds |
| Recovery timeout (open → half-open) | 30 s – 2 min |
| Half-open trial count | 1–5 |

**Libraries:** Resilience4j (Java), Polly (.NET), `circuitbreaker` (Python),
go-resiliency (Go), Hystrix (Java, retired).

**Hook circuit breakers into monitoring.** OPEN state should fire alerts —
something is broken upstream. Don't just silently degrade forever.

---

## 3. Bulkhead Pattern

Partition resources (typically thread pools) per API endpoint or per
dependency, so a flood on one doesn't starve the others.

```
Without bulkheads                    With bulkheads
─────────────────                    ──────────────

┌──────────────┐                     ┌──────────────────────┐
│ One pool     │                     │  /api/orders pool    │
│ All APIs     │                     ├──────────────────────┤
│ share        │                     │  /api/products pool  │
│              │                     ├──────────────────────┤
│ Slow API X   │ ┄┄┄┄┄┄┄┄┄┄►        │  /api/users pool     │
│ exhausts     │                     ├──────────────────────┤
│ pool, all    │                     │  /api/admin pool     │
│ APIs fail    │                     └──────────────────────┘
└──────────────┘                     Slow API stays
                                      contained
```

**Java example with Resilience4j:**

```java
ThreadPoolBulkhead orders = ThreadPoolBulkhead.of("orders",
    ThreadPoolBulkheadConfig.custom()
        .maxThreadPoolSize(20)
        .coreThreadPoolSize(10)
        .queueCapacity(50)
        .build());

ThreadPoolBulkhead products = ThreadPoolBulkhead.of("products", ...);
```

**Sizing:** each bulkhead pool's size + queue should equal that API's
expected concurrent demand. Total across bulkheads should fit the host's
capacity.

**When NOT to bulkhead:** small services with one or two APIs, or where the
APIs share most dependencies anyway. Bulkheads add complexity; use them when
APIs really do isolate work.

---

## 4. Default / Fallback Responses

When a dependency is broken (circuit open, timeout, error), return a
*degraded but available* response rather than failing.

```python
@circuit(failure_threshold=5)
def get_recommendations(user_id):
    return rec_service.recommend(user_id)

def get_recommendations_with_fallback(user_id):
    try:
        return get_recommendations(user_id)
    except CircuitBreakerError:
        # Fall back to popular items if rec service is down
        return get_popular_items(default_count=10)
```

**Examples:**

| API | Fallback |
|---|---|
| Personalized recommendations | Generic popular items |
| Real-time inventory check | "In stock" with order-time confirmation |
| User-specific pricing | Default pricing tier |
| Map / address validation | Skip validation; flag for async review |

**Not always safe.** Fallbacks must be ones the business can tolerate. A
fallback that ships the wrong product is worse than an outright failure.

---

## 5. Exponential Backoff on Retries

Naive retry loops amplify outages — a struggling backend gets hit harder
exactly when it's struggling. Exponential backoff with jitter spreads retries
over time.

```
Attempt   Delay
───────   ─────
   1      0       (immediate)
   2      1 s     (+ jitter ±100ms)
   3      2 s
   4      4 s
   5      8 s
   6      16 s    (cap)
```

**Pseudocode:**

```python
delay = base
for attempt in range(max_retries):
    try:
        return call()
    except RetryableError:
        time.sleep(min(delay + jitter(), cap))
        delay *= 2
raise
```

**Jitter is essential.** Without it, all clients retry simultaneously,
producing synchronized spikes. ±10–25% randomization prevents this.

**Don't retry idempotency violations.** If the call is non-idempotent and
you don't have an idempotency key, retrying may double-charge / double-
deliver. See `distributed-systems-essentials`.

**Don't retry forever.** Cap attempts (3–5 typical). Surface the error to
the caller eventually.

---

## 6. API Gateway

The single entry point that wraps the microservices system from the outside.

```
                 ┌──────────────────────────┐
                 │     API Gateway          │
                 │                          │
                 │  • Auth                  │
                 │  • Throttling            │
                 │  • Caching               │
                 │  • Request routing       │
                 │  • Monitoring            │
                 │  • Aggregation           │
                 └─────────┬────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   ┌─────────┐        ┌─────────┐        ┌─────────┐
   │ Service │        │ Service │        │ Service │
   │   A     │        │   B     │        │   C     │
   └─────────┘        └─────────┘        └─────────┘
```

**Common gateways:**
- NGINX Plus
- Kong
- AWS API Gateway (10K req/s soft limit, 5K/s burst)
- Apigee
- Tyk
- Envoy (often as Ambassador / Contour)

**Throttling** at the gateway is the outermost layer — protects the whole
system from upstream pressure.

**Watch the gateway as a bottleneck.** Know its req/s limit; provision
accordingly.

---

## Putting It Together: A Service-to-Service Call

```
┌──────────────────────────────────────────────────────────────────────┐
│                     Service A calling Service B                       │
│                                                                       │
│  caller_thread = bulkhead.get_thread("call_to_b")                    │
│                                                                       │
│  if circuit_breaker_b.is_open:                                       │
│      return fallback_response()                                      │
│                                                                       │
│  try:                                                                 │
│      with timeout(2.0):                       ← fail fast            │
│          response = b.call(args)                                     │
│      circuit_breaker_b.on_success()           ← circuit breaker      │
│      return response                                                 │
│  except TimeoutError, ConnectionError:                               │
│      circuit_breaker_b.on_failure()                                  │
│      return fallback_response()               ← graceful degradation │
│  finally:                                                             │
│      bulkhead.release(caller_thread)          ← bulkhead             │
│                                                                       │
│  retry policy: 3 attempts, exponential backoff, idempotent only      │
└──────────────────────────────────────────────────────────────────────┘
```

Every external call should look something like this. The patterns compose
into a runtime model that resists cascading failure.

---

## Principles

- **Cascading failures are triggered by slow responses, not outright
  failures.** Default timeouts of "until the connection drops" are the
  silent killer.
- **Fail fast.** Set tight read timeouts at P99 + headroom.
- **Use a circuit breaker around every external dependency.** Hook to
  monitoring; alert on OPEN state.
- **Use bulkheads to cap thread-pool occupation per API.**
- **Prefer fallbacks over propagating errors** when degraded service is
  acceptable.
- **Avoid immediate retries.** Use exponential backoff with jitter.
- **Cap total retries** (3–5). Surface the error to the caller eventually.
- **Don't retry non-idempotent calls** without an idempotency key.
- **Build cascading timeout budgets** — caller timeouts > callee timeouts.
- **Hook all of this into monitoring** — silent degradation is its own
  failure mode.
- **API gateway is the outermost defense** — throttle there.

---

## Anti-Patterns

### No Read Timeout

**Looks like:** Default HTTP client timeout (often "until OS gives up" — 5+
minutes). One slow downstream takes the whole thread pool with it.

**Why it fails:** Resource exhaustion → cascading failure.

**The fix:** Set explicit read timeout on every external call. P99 + headroom.

### Naive Retry Loop

**Looks like:** `for attempt in range(10): try call() except: pass`. Retries
hammer the struggling service.

**Why it fails:** Synchronizes load, amplifies outage.

**The fix:** Exponential backoff + jitter + cap.

### Retrying Non-Idempotent Calls

**Looks like:** `POST /charge` with retry-on-error. Network flakes during
response. Customer gets two charges.

**Why it fails:** Retries assume idempotence.

**The fix:** Idempotency keys (see `distributed-systems-essentials`). Or
don't retry — fail to the caller.

### Circuit Breaker Without Monitoring

**Looks like:** Service silently returns fallback for two days because
breaker is open and nobody noticed.

**Why it fails:** Resilience without visibility just hides problems.

**The fix:** Alert on OPEN state. Dashboards show breaker state per
dependency.

### Premature Fallback

**Looks like:** Single 5xx → fall back. Service is fine; one transient blip
gets papered over.

**Why it fails:** Loses signal. Real failures look like noise.

**The fix:** Threshold + window. Only fall back when there's a *pattern*
of failure.

### Cascading Timeout Inversion

**Looks like:** A → B has 2 s timeout; B → C has 5 s timeout. C is slow;
A times out at 2 s; B keeps trying for another 3 s; orphan resources.

**Why it fails:** Caller timeouts must exceed callee timeouts so the callee
can return its error before the caller gives up.

**The fix:** Cascading timeout budget. A's timeout > B's > C's.

### One Pool for Everything

**Looks like:** All APIs share a single Tomcat thread pool. A load spike on
`/admin` fills the pool; `/checkout` requests can't get a thread.

**Why it fails:** No isolation between APIs.

**The fix:** Bulkhead — thread pools (or queues) per API or per dependency.

### Premature Microservices

**Looks like:** A 3-engineer team architects 8 microservices. None of them
have circuit breakers, bulkheads, or fail-fast configured.

**Why it fails:** Distributed-system complexity without operational maturity.
First load spike turns into cascading outage.

**The fix:** Modularize the monolith. Adopt microservices when team size and
ops maturity justify the tax.

---

## Decision Rules

| Situation | Action |
|---|---|
| Designing any service-to-service call | Read timeout (P99 + headroom), circuit breaker, retry with backoff |
| Service has multiple APIs with different SLAs | Bulkhead — thread pool per API |
| Critical user-facing path with optional dependency | Fallback to default response on circuit OPEN |
| Diagnosing cascading failure | Look for absent / wrong timeouts first; bulkhead second |
| Retrying mutating call | Only with idempotency key + exponential backoff |
| Choosing API gateway | Kong / NGINX / Apigee on-prem; AWS API Gateway managed |
| Public API exposure | Throttle at the gateway level |
| Multi-tenant service | Per-tenant bulkheads + rate limits |

---

## Worked Example: Hardening a Checkout Service

**Context:** Checkout service depends on Payment, Inventory, Pricing, and
Notification services. Recent incident: slow Payment caused checkout pool
exhaustion.

**Defenses to install:**

| Layer | Defense |
|---|---|
| 1. Timeouts | Payment 5 s; Inventory 1 s; Pricing 500 ms; Notification 200 ms (fire-and-forget). All client-side. |
| 2. Circuit breakers | Per-dependency. 10 failures in 60 s → OPEN; 60 s recovery. |
| 3. Bulkheads | Thread pool per dependency: Payment 50, Inventory 30, Pricing 20, Notification 10. |
| 4. Fallbacks | Notification: drop on OPEN (best-effort). Pricing: use cached default tier on OPEN. Inventory and Payment: must succeed; on OPEN, return 503 with retry-after. |
| 5. Retries | Payment & Inventory: 3 attempts, exponential backoff (1s, 2s, 4s) + jitter; idempotency keys required. |
| 6. Gateway | API Gateway throttles per-customer at 10 req/s, total at 1000 req/s. |
| Monitoring | Dashboard: per-dependency P99 latency, circuit breaker state, bulkhead utilization, retry rate, fallback rate. Alerts on OPEN state. |

**Cascading timeout budget:**
- Gateway → Checkout: 8 s
- Checkout → Payment: 5 s ✓
- Payment → Stripe: 4 s ✓

**Outcome:** Next time Payment slows down, Checkout's circuit breaker opens
quickly, calls fail fast, the bulkhead caps the impact to the Payment pool
only, and other endpoints continue to function. Alerting fires; engineers
investigate Payment.

---

## Gotchas

- **Async / reactive code may not respect synchronous timeouts.** Verify the
  HTTP client honors timeout in the runtime you're using (Node `fetch` until
  recently didn't; Python `requests` does; Java HttpClient since 11).
- **Circuit breaker tuning is workload-specific.** Default thresholds rarely
  match production traffic. Tune empirically.
- **Bulkhead pool sizing affects max throughput.** Size pools for expected
  concurrent demand, not theoretical max.
- **Fallback responses can themselves fail.** Plan for it — fallback caches
  expire; default values become wrong.
- **Retry storms can be self-inflicted DDoS.** Always include jitter and
  total retry caps.
- **API gateway is a critical dependency itself.** Know its limits; have
  fallback paths if it fails (or run it active-active).
- **Hystrix is retired** but the conceptual model lives on in Resilience4j
  (Java), Polly (.NET), and others.
- **Service mesh** (Istio, Linkerd) can apply many of these patterns at the
  sidecar level — see `distributed-system-patterns`. Useful at large scale,
  overkill at small scale.

---

## Related Skills

- `distributed-system-patterns` — Saga, Sidecar, BFF, Service Mesh
  (architectural patterns)
- `distributed-systems-essentials` — idempotency keys (required for
  safe retries)
- `load-balancing-and-app-services` — thread pools at the request tier
- `architecture-styles-monolithic-and-distributed` — when microservices
  are the right architectural choice
- `api-gateway-and-service-mesh` — deeper coverage of the gateway layer

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 9. Sam
Newman's *Building Microservices* is the reference for the broader
microservices design space.
