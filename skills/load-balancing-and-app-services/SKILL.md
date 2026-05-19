---
name: load-balancing-and-app-services
description: >
  Design and operate the HTTP request-handling tier - REST/CRUD APIs over
  application servers (Tomcat / Express / Spring), L4 vs L7 load balancers,
  load distribution policies (round robin, least connections, fastest
  response, weighted), auto-scaling groups (scheduled vs metric-driven),
  health checks, sticky sessions, and the stateless-services pattern. Use
  when designing the front of a service, choosing/configuring a load
  balancer, sizing thread/connection pools, planning auto-scaling, or
  deciding between stateful and stateless service designs. Triggers -
  "load balancer choice", "L4 vs L7", "auto-scaling group", "sticky
  sessions", "stateless services", "Tomcat thread pool", "Express
  scaling", "session affinity", "health check", "blue-green / canary".
  Produces a concrete request-tier design with sizing and scaling rules.
---

# Load Balancing and Application Services

You design the request-handling tier — the HTTP services and the load balancer
in front of them. This is the bedrock of horizontal scaling: stateless
services + load balancer + external state store. Get this layer right and
most other tiers can scale predictably; get it wrong and nothing else helps.

This skill captures Gorton's *Foundations of Scalable Systems* (Ch 5): the
application-server anatomy, the LB type/policy choice, auto-scaling, and the
stateful-vs-stateless trade-off.

---

## When to Use This Skill

- Designing the API layer for a new service or refactoring an existing one
- Choosing or configuring a load balancer (NLB / ALB / HAProxy / NGINX)
- Sizing application thread pools and DB connection pools
- Planning auto-scaling policies (scheduled vs metric-driven)
- Deciding stateful vs stateless service design and session handling
- Diagnosing capacity / latency issues at the request tier

---

## The Baseline Pattern

```
                ┌──────────────────────────┐
                │      Internet / Users    │
                └────────────┬─────────────┘
                             │
                ┌────────────▼─────────────┐
                │      Load Balancer       │
                │   (ALB / NLB / HAProxy)  │
                │      Health checks       │
                └────┬────────┬────────┬───┘
                     │        │        │
              ┌──────▼──┐ ┌───▼───┐ ┌──▼─────┐
              │ App     │ │ App   │ │ App    │     ← Stateless replicas
              │ server  │ │ server│ │ server │       (Tomcat / Express /
              │  #1     │ │  #2   │ │  #3    │        Spring / FastAPI)
              └────┬────┘ └───┬───┘ └────┬───┘
                   │          │          │
                   └──────────┼──────────┘
                              │
                  ┌───────────▼───────────┐
                  │  External state store │     ← Sessions, cache,
                  │   (Redis / DynamoDB)  │       feature flags
                  └───────────┬───────────┘
                              │
                  ┌───────────▼───────────┐
                  │       Database        │
                  └───────────────────────┘
```

**The rule:** Any scalable service needs stateless APIs. Session state lives
in an external store. Replicas are interchangeable. The LB distributes load
to whichever replica is least busy and pulls failed instances out of rotation.

---

## REST / CRUD APIs

| HTTP verb | Purpose | Idempotent? |
|---|---|---|
| `GET` | Retrieve | Yes |
| `POST` | Create / non-idempotent action | No |
| `PUT` | Replace (full update) | Yes |
| `PATCH` | Partial update | Sometimes |
| `DELETE` | Remove | Yes |

**REST treats URIs as resources** (`/customers/42/orders/17`), HTTP verbs as
operations on them. The strict Roy-Fielding-thesis interpretation includes
HATEOAS; almost no production API does this. The mainstream pattern is
"RESTful-ish" — verb + URI + JSON body.

For deeper API design see `api-design-and-evolution`. This skill focuses on
the *runtime* tier.

---

## Application Server Anatomy

```
   ┌──────────────────────────────────────────────────────────┐
   │                  Application Server (e.g., Tomcat)       │
   │                                                          │
   │   Listener thread                                        │
   │       │                                                  │
   │       ▼                                                  │
   │   ┌─────────────────┐                                   │
   │   │  Sockets backlog│    OS-level pending-connection    │
   │   │  (Linux: 100)   │    queue                          │
   │   └────────┬────────┘                                   │
   │            │                                             │
   │            ▼                                             │
   │   ┌─────────────────┐                                   │
   │   │ HTTP connector  │                                   │
   │   └────────┬────────┘                                   │
   │            │ accepts                                     │
   │            ▼                                             │
   │   ┌─────────────────────────┐                           │
   │   │  Application thread     │     Tomcat default:       │
   │   │  pool                   │     25 min, configurable  │
   │   │  (worker threads)       │     max                   │
   │   └────────┬────────────────┘                           │
   │            │                                             │
   │            ▼                                             │
   │   ┌─────────────────────────┐                           │
   │   │  DB connection pool     │     Bound to DB capacity, │
   │   │                         │     not app load          │
   │   └─────────────────────────┘                           │
   └──────────────────────────────────────────────────────────┘
```

**The four numbers to size:**

| Knob | Bounded by |
|---|---|
| Sockets backlog (OS) | Burst arrival rate the OS should buffer |
| Listener accept rate | Effectively unbounded for most servers |
| **App thread pool** | Cores × (1 + waitTime/cpuTime), or empirical |
| **DB connection pool** | Database's `max_connections` ÷ (replica count × concurrency factor) |

**Sizing trap:** If app pool > DB pool × 5–10, threads constantly wait for DB
connections. Saturated wait-queue inside the app server. Diagnosed via thread
dump showing many threads in `WAITING (parking)` on the connection pool.

**Observability:** JMX / MBeans / JConsole / JavaMelody for JVM-based servers.
Watch active threads, queue depth, GC pauses, connection pool wait time.

---

## L4 vs L7 Load Balancers

| | L4 (Network) | L7 (Application) |
|---|---|---|
| OSI layer | Transport (TCP/UDP) | Application (HTTP) |
| What it sees | Source/dest IP, port | Method, path, headers, cookies |
| Routing | By IP/port hash | By URL path, host, header value |
| Latency | Lowest (kernel-level) | Higher (parses HTTP) |
| Use cases | Pure throughput, non-HTTP, end-to-end TLS | Path-based routing, A/B, canary, WebSocket termination |
| AWS | NLB | ALB |
| Other | HAProxy (in TCP mode) | NGINX, HAProxy (HTTP mode), Traefik, Envoy |

**Gorton's benchmark:** AWS NLB is ~20% faster than ALB on light loads. The
difference disappears once the backend is saturated — at that point the LB
isn't the bottleneck.

**Default in 2026:** ALB (or NGINX) for HTTP services. Drop to NLB only when:

1. You need end-to-end TLS without termination at the LB.
2. The protocol isn't HTTP (raw TCP, custom protocol).
3. You've measured LB latency as the bottleneck.

---

## Load Distribution Policies

HAProxy offers ~10 of these. The ones that matter:

| Policy | When to use |
|---|---|
| **Round robin** | Default. Replicas are equally capable. |
| **Least connections** | Long-lived connections (WebSocket, gRPC) — keeps load even. |
| **Fastest response** | Heterogeneous backends (different sizes / regions). |
| **Weighted** | Gradual rollout / canary — send 5% to new version. |
| **Source IP hash (sticky)** | Stateful services that need session affinity. **Avoid when possible.** |
| **URL hash** | Cache-friendly — route same URL to same backend. |

**Default:** Round robin. Switch only when there's a measured reason.

---

## Health Checks

```
LB                              Replica
  │                                │
  ├── GET /health  ──────────────→ │
  │ ←──────────────  200 OK ─────  │
  │                                │  (every 5–30 s)
  │                                │
  │                                │  (replica process dies)
  │                                │
  ├── GET /health  ──────────────→ │
  │   <timeout / 5xx>              │
  │                                │
  ├── (mark unhealthy, remove from rotation)
  │
  ├── GET /health  ──────────────→ │  (recovers)
  │ ←──────────────  200 OK ─────  │
  ├── (return to rotation after N consecutive successes)
```

**Health endpoint design:**

- **Cheap.** Don't query the DB on every check (the LB will hammer it).
- **Truthful.** Reflect real readiness — DB connection pool initialized,
  warm-up complete, downstream dependencies reachable enough to serve.
- **Distinguish liveness from readiness.** Liveness = "process alive"; readiness
  = "ready to take traffic." Kubernetes formalizes this; LBs benefit from the
  same distinction.

**Tuning:**
- Check interval: 5–30 s typical.
- Unhealthy threshold: 2–3 consecutive failures.
- Healthy threshold: 2–3 consecutive successes (avoid flapping).

---

## Auto-Scaling Groups

```
┌──────────────────────────────────────────────────────────┐
│                 Auto-Scaling Group                       │
│                                                          │
│  Min: 3      Desired: 6      Max: 20                     │
│                                                          │
│  Scaling policy:                                         │
│    Scale up:   if CPU > 70% for 2 consecutive minutes    │
│                add 2 instances                           │
│    Scale down: if CPU < 30% for 10 consecutive minutes   │
│                remove 1 instance                         │
│                                                          │
│  Warm-up: 90 s (no LB traffic until container ready)     │
└──────────────────────────────────────────────────────────┘
```

| Strategy | When to use |
|---|---|
| **Scheduled** | Predictable load patterns (business hours, batch windows) |
| **Metric-driven** | Unpredictable spikes |
| **Combined** | The realistic answer: schedule a baseline, autoscale the spikes |

**Common metrics:**

- CPU utilization (default; coarse but reliable).
- Request rate per instance.
- Response time P95/P99 (better than CPU for latency-sensitive services).
- Custom (queue depth, active connections).

**Cooldown / warm-up periods are critical.** New instances need time to
initialize (JVM warm-up, JIT, connection pool) before taking traffic. Without
warm-up, new replicas serve slow first requests and the LB sees them as "the
fastest" and routes more traffic to them — a thundering herd.

**Scaling-down signals:**
- Drain connections gracefully (LB stops sending new; existing finish).
- Shut down only after the connection drain timeout (~30 s typical).

---

## Stateless vs Stateful Services

| | Stateless | Stateful |
|---|---|---|
| Where state lives | External (Redis, DB) | In-process memory |
| LB requirements | None special | Sticky sessions / session affinity |
| Replica failure impact | None (state is elsewhere) | All client sessions on that replica are lost |
| Auto-scaling | Free — any replica can serve any request | Hot replicas resist scale-down; new replicas can't take existing sessions |
| Deploy complexity | Trivial — drain and replace | Drain takes longer; in-flight sessions must finish or migrate |
| Memory footprint | Predictable (no per-user growth) | Grows with active sessions |

**The Gorton conclusion:** any scalable service needs stateless APIs. Use
sticky sessions only when you truly can't externalize state — and accept
that they create persistent hot replicas as long-lived sessions accumulate.

---

## Principles

- **Stateless or it doesn't scale.** Move session state to Redis / DynamoDB /
  the database.
- **App pool size and DB pool size are coupled.** Don't tune one without the
  other.
- **L7 LB by default; drop to L4 only when measured.**
- **Health endpoints must be cheap and truthful.** Don't query the DB; do
  reflect real readiness.
- **Use scheduled scaling for predictable load, metric-driven for spikes.**
  Combine both for realistic systems.
- **Warm up new replicas before taking traffic.** JVM JIT and connection
  pools take seconds.
- **Drain gracefully on scale-down.** No abrupt kills of in-flight requests.
- **Add replicas first, LB sophistication second.** Most LB choices are
  fine; capacity is usually the gap.

---

## Anti-Patterns

### Stateful Services Without Sticky Sessions

**Looks like:** Sessions in app-server memory, round-robin LB. Random clients
get logged out.

**Why it fails:** Round robin sends requests to different replicas; the
session isn't there.

**The fix:** Either externalize session state (preferred) or enable sticky
sessions on the LB.

### App Pool Far Larger Than DB Pool

**Looks like:** 200 app threads, 20 DB connections. Under load, 180 threads
are blocked waiting for a DB connection.

**Why it fails:** App server appears overloaded but the bottleneck is
elsewhere. Diagnosed by thread dump showing waits on the connection pool.

**The fix:** Match app pool size to DB pool × concurrency factor (typically
5–10 simultaneous app calls per DB connection). Or expand the DB pool. Or
fix slow queries.

### Aggressive Health Checks

**Looks like:** `/health` endpoint queries 3 tables and a downstream service.
LB hits it every 2 seconds across 8 replicas. The DB sees 12 health-check
queries per second.

**Why it fails:** Health-check queries become the dominant DB load. When DB
is slow, health checks fail, replicas get pulled, the surviving replicas get
hammered.

**The fix:** Cheap `/health` for the LB; richer `/ready` or `/diagnostic`
for human use.

### Unbounded Auto-Scaling Max

**Looks like:** Auto-scaling group with `max=1000`. A traffic anomaly
(or DDoS) scales to 1,000 instances. Bill spike. Downstream DB collapses.

**Why it fails:** Auto-scaling without a circuit somewhere just relays
overload to a downstream tier — at high cost.

**The fix:** Realistic max. Rate limiting at the LB. Backpressure / circuit
breakers downstream.

### Too-Short / Too-Long Session Timeouts

**Looks like:** Either users get logged out mid-session, or app servers run
out of memory holding zombie sessions for hours.

**Why it fails:** Wrong end of the trade-off.

**The fix:** Externalize state with TTL. Then session timeout doesn't pressure
app-server memory.

### Cold-Start Thundering Herd

**Looks like:** New replicas start, immediately receive full LB share, serve
slow requests, latency spikes.

**Why it fails:** No warm-up period. The LB doesn't distinguish "warm and
fast" from "cold and slow."

**The fix:** Warm-up window in the auto-scaling config. Health endpoint
returns "not ready" until JIT is hot and connections are pooled.

---

## Decision Rules

| Situation | Action |
|---|---|
| New service, HTTP-based | ALB + stateless replicas + external state store |
| Need TLS termination at the LB | ALB (or NGINX). NLB only for end-to-end. |
| Long-lived connections (WebSocket, gRPC) | Least-connections policy on L7 LB |
| Replicas of differing capacity | Weighted or fastest-response policy |
| Predictable diurnal load | Scheduled scaling + metric-driven scaling on top |
| Bursty unpredictable load | Aggressive metric-driven scaling; consider serverless |
| Stateful service that can't be made stateless | Sticky sessions; accept hot-replica tax |
| App tier saturating, DB underutilized | Increase app pool or replica count |
| App threads waiting on DB pool | Fix slow queries or expand DB pool — don't grow app pool |
| Health checks loading the DB | Make them cheap; separate `/health` from `/ready` |

---

## Worked Example: Sizing a Spring Boot API

**Context:** Spring Boot service, Postgres backend, ~200 req/s steady, P99
latency target 300 ms.

**Sizing:**

| Component | Value | Rationale |
|---|---|---|
| Replicas | 4 | 200 req/s ÷ 50 req/s per replica with headroom |
| Tomcat thread pool | 50 max | I/O-heavy: cores × (1 + 70/30) ≈ 8 × ~2.3 ≈ 20 baseline; 50 for headroom |
| HikariCP DB pool | 20 per replica | Postgres `max_connections=200`, with 4 replicas = 50 each available, 20 leaves room for migrations / admin |
| LB | ALB, round-robin | HTTP service, no special routing needs |
| Health check | `/health` returning 200 if DB ping last <2 s ago (cached) | Cheap |
| Auto-scaling | min=3, max=10, target CPU 70%, warm-up 60 s | Headroom + safety against runaway |

**Total DB connections:** 4 replicas × 20 = 80, well under Postgres's 200.

**What we deliberately don't do:**
- Sticky sessions (state is in Redis).
- L4 LB (HTTP routing wanted at the LB).
- Per-replica caching (Redis is shared).

**Failure mode to monitor:** Thread pool saturation. Metric:
`tomcat.threads.busy / tomcat.threads.config-max-threads > 0.8` for 2 min →
scale up.

---

## Gotchas

- **Tomcat default 25 threads** is small for I/O-heavy services. Tune up.
- **Spring Boot's default HikariCP pool is 10** — fine for small services,
  too small for production-scale APIs.
- **Health-check loops between LBs and replicas** can dominate small-service
  load. Watch traffic mix.
- **Sticky sessions don't survive replica restarts.** When the replica is
  pulled, all sessions on it are gone. External state is the only durable answer.
- **Scaling up before warm-up completes** sends slow new replicas into the
  rotation. P99 spikes.
- **"Drain" semantics differ between LBs.** ALB drains for connection
  duration; NLB drains for "deregistration delay." Know your platform.
- **Auto-scaling reaction time is minutes**, not seconds. For sub-minute
  spikes, you need over-provisioning (or serverless).

---

## Related Skills

- `scalability-foundations` — when to add a load balancer at all
- `distributed-systems-essentials` — connection reuse, partial failure
- `concurrent-systems-foundations` — thread-pool sizing
- `distributed-caching-patterns` — what fronts the DB
- `microservices-resilience-patterns` — circuit breakers, bulkheads at this tier
- `serverless-processing-systems` — alternative to fixed replicas for spiky load
- `api-design-and-evolution` — REST API design at the contract level
- `api-gateway-and-service-mesh` — when service count grows beyond simple LB

Source: *Foundations of Scalable Systems* by Ian Gorton, Chapter 5.
