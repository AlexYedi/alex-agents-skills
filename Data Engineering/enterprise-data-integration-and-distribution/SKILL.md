---
name: enterprise-data-integration-and-distribution
description: >
  Pick the right enterprise integration pattern: APIs (REST, SOA, ROA),
  event-driven (message queues, event brokers, event streams, CEP), CQRS,
  Backend-for-Frontend, composite services, choreography vs orchestration,
  point-to-point exceptions, queue-based load leveling. Apply to data
  distribution: batch vs API vs event-based ingestion. Use when designing
  cross-domain data flow, choosing sync vs async, deciding between message
  queue and event stream, or selecting between orchestration and
  choreography. Triggers: "REST or events", "queue vs stream", "CQRS for
  data", "BFF pattern", "service orchestration vs choreography",
  "composite service", "data distribution patterns", "event-driven for
  data". Produces a chosen integration approach with rationale.
---

# Enterprise Data Integration and Distribution

You apply Strengholt's catalog of enterprise integration patterns specifically
for data: APIs, events, queues, streams, plus the patterns that combine them
(CQRS, BFF, queue-based load leveling). You pick the right tool for each
data flow's actual constraints — sync vs async, near-real-time vs batch,
strongly consistent vs eventually consistent.

---

## When to Use This Skill

- Designing cross-domain data flow in a Mesh / Federated architecture
- Choosing between APIs, events, and batch for a specific integration
- Deciding sync (request/response) vs async (event-driven)
- Selecting message queue vs event broker vs event stream
- Resolving "should we orchestrate centrally or choreograph?"
- Implementing CQRS to separate read and write models
- Spec'ing a Backend-for-Frontend layer

---

## The Integration Pattern Spectrum

```
SYNC                                                                    ASYNC
────                                                                    ─────

REST API     SOA          Composite      Message       Event Broker      Event
(direct)     (interface-  Service        Queue         (lightweight      Stream
             encapsulated) (aggregator)  (point-to-    middleware)       (append-
                                          point)                          only log)
                                                                              │
                                          │              │                    │
                                  Once-delivered    Multi-consumer       Replayable
                                  Ordered           Validation/storage   Distributed
                                                    Routing
```

| Pattern | Communication | When |
|---|---|---|
| **REST API** | Sync request/response | Strongly consistent reads; direct command invocation; thin mediation |
| **SOA** | Sync; interface-encapsulated | Connecting operational + analytical systems with formal contracts |
| **Resource-Oriented API (ROA)** | Sync; resource-noun-oriented | RESTful APIs at higher rigor; resources self-discoverable |
| **Composite Service** | Sync; aggregating | Avoid "chattiness" between client + N backends |
| **Message Queue** | Async; once-delivered | Point-to-point; ordering matters; one consumer per message |
| **Event Broker** | Async; multi-consumer | Multiple subscribers; light validation/routing |
| **Event Stream** | Async; replayable log | Multi-consumer with replay (Kafka, Pulsar); historical analytics |
| **CEP (Complex Event Processing)** | Async; correlating | Time-window correlation; fraud detection; alerting |

---

## The Six Distribution Patterns (Strengholt's Catalog)

When data flows from one domain to another, you choose one of these:

### 1. Batch-Oriented Data Processing

```
Source domain ──► Snapshot/file ──► Consumer domain
                  (scheduled)
```

**When:** Periodic reconciliation, auditing, large historical processing.
**Pros:** Cheap, simple, well-understood.
**Cons:** Latency in hours/days. Late-arriving data complications.

### 2. API-Based Ingestion

```
Source domain ──► REST API ──► Consumer domain
                  (consumer
                   pulls)
```

**When:** Provider or consumer wants to initiate; strongly consistent reads.
**Pros:** Direct, simple. Strong consistency.
**Cons:** Coupling on availability; consumer pulls regardless of new data.

### 3. Event-Based Ingestion

```
Source domain ──► CDC / events ──► Stream / queue ──► Consumer domain
                  (reactive)        (decoupled)
```

**When:** State transfer is reactive; CDC; async OK.
**Pros:** Loose coupling; near-real-time; multi-consumer.
**Cons:** Eventual consistency; ordering / exactly-once complexity.

### 4. CQRS (Command Query Responsibility Segregation)

```
Commands ──► Command Store     Queries ──► Read Store
              (operational                  (analytical /
               OLTP)                         data product)
                  │                              ▲
                  └─────── replicate ────────────┘
                           (events / CDC)
```

**When:** Heavy read load that would crush operational systems; separate scaling needs.
**Pros:** Optimized for each side; queries don't impact writes.
**Cons:** Replication lag; operational complexity.

### 5. Queue-Based Load Leveling

```
Consumer requests ──► Queue ──► API gateway ──► Source domain
                      (buffers)
```

**When:** API has rate-limit / capacity constraints; spiky consumer load.
**Pros:** Source domain protected from spikes.
**Cons:** Latency added by queue; complexity.

### 6. Point-to-Point (the exception)

```
Source ───direct───► Consumer
        (no broker)
```

**When:** Latency-critical (e.g., payment authorization < 100ms). Strict time budget rules out intermediation.
**Pros:** Lowest latency.
**Cons:** Tight coupling. Use sparingly. Document the exception.

---

## Application Integration Patterns (Beyond Data)

### Service-Oriented Architecture (SOA)

**Strengths:** Formalized interfaces; reusable services; cross-system integration.
**Caveat:** ESB-driven SOA fell out of favor — too much in the bus, too little in the services.

### Resource-Oriented Architecture (ROA)

A specific RESTful guideline: data modeled as collections of homogeneous resources; nouns over verbs; self-discoverable.

```
GET    /customers
GET    /customers/{id}
POST   /customers
PATCH  /customers/{id}
DELETE /customers/{id}
GET    /customers/{id}/orders
```

**When:** APIs serving multiple clients; long-lived contracts; discoverability matters.

### Composite Service

```
Client ──► Composite Service ──► [Service A]
                              ├─► [Service B]
                              └─► [Service C]
            (aggregates response)
```

**When:** Client would otherwise make N round trips; latency budget; integration logic should not live in client.

**Anti-pattern variant:** Composite service that grows into a "god service" with all the logic. Keep them thin and aggregation-focused.

### Backend-for-Frontend (BFF)

```
[Mobile App] ──► [Mobile BFF] ──► [Service A] [Service B] [Service C]
[Web App]    ──► [Web BFF]    ──► (same backends, different aggregation)
```

**When:** Multiple frontends with different data shapes / latency needs. Each BFF optimizes for its frontend.

**Caveat:** BFFs proliferate; treat them as part of the frontend, not a separate tier.

### Service Orchestration vs Choreography

```
ORCHESTRATION (centralized)             CHOREOGRAPHY (distributed)
─────────────────────                    ─────────────────────────

         [Orchestrator]                   Service A ──event──► Service B
        ╱      │      ╲                                            │
       ▼       ▼       ▼                                          event
  Service  Service  Service                                         │
     A        B        C                                            ▼
                                                              Service C
   (each step                                                       │
    explicitly                                              event   │
    coordinated)                                                    ▼
                                                              Service D
```

**Orchestration:** Central component (often ESB or workflow engine) explicitly coordinates the sequence.
- **Pros:** Clear control flow; easier to reason about.
- **Cons:** Bottleneck; central component becomes complex.

**Choreography:** Services emit and react to events. No central coordinator.
- **Pros:** Loose coupling; each service is autonomous.
- **Cons:** Hard to trace end-to-end flow; emergent behavior.

**Modern guidance:** Choreography for the happy path; orchestration for cross-cutting workflows (sagas, compensation logic).

### Federated Responsibility Model

The opposite of a fat ESB. Business logic and data persistence return to the domains. The integration layer does only what's truly cross-cutting (security, observability, routing).

---

## CQRS in Detail

**Why separate read and write?**
- Writes need ACID transactions; reads need scale and low latency
- Optimal storage / indexing for each is different
- Queries don't need to wait for write-side locks

```
─── Command Path ───                      ─── Query Path ───
                                          
[Client] ──► [Command API] ──► [Aggregate] ──events──► [Read Store(s)]
                                    │                        │
                                    └──persists──► [Event Store]
                                                                ▲
                                                                │
                                          [Client] ──► [Query API] ─┘
```

**Event Sourcing:** Often paired with CQRS. State is reconstructed from event log; current state is derived, not stored canonically. Powerful but adds complexity.

**Practical take:** Most teams shouldn't adopt full CQRS / Event Sourcing. The simpler pattern — separate read replicas, eventual consistency — gives 80% of the benefit at 10% of the complexity.

---

## Principles

- **Async by default; sync when truly required.** Async unlocks resilience, elasticity, multi-consumer.
- **Eventually consistent reads are usually fine.** Demand for strong consistency is often unexamined.
- **Standardize endpoints, not implementations.** Common Driveway pattern. Every domain registers via the same metadata format; underlying tech can vary.
- **Decouple via abstraction, not just queuing.** A queue with a tight schema contract is still tight coupling.
- **Compose services thoughtfully.** A composite service is fine; ten composite services with overlapping responsibilities is a mess.
- **Choreography for autonomy; orchestration for sagas.** Match the pattern to the workflow type.
- **Federated responsibility.** Push logic to domains. The integration layer stays thin.

---

## Anti-Patterns

### Sync Everything

**Looks like:** Every cross-domain call is a REST request. Failures cascade. SLA = product of every dependency's SLA.

**Why it fails:** Coupling on availability. One slow service drags everything down.

**The fix:** Async (events / queues) for non-critical paths. Reserve sync for genuinely synchronous needs (commands, strongly consistent reads).

### Async Everything

**Looks like:** Adopting events / queues universally. Even simple read paths go through a queue. Latency proliferates.

**Why it fails:** Async has overhead and complexity. For a synchronous read, a REST call is simpler.

**The fix:** Pick the simplest pattern that satisfies the constraint. Don't async-cult.

### Fat ESB

**Looks like:** Enterprise Service Bus accumulates business logic over years. Becomes the largest "service" in the org.

**Why it fails:** Single point of complexity. Changes to any flow require ESB changes. Team structure follows.

**The fix:** Federated Responsibility Model. Push logic to domains. ESB does only routing/security/observability.

### Composite Service Sprawl

**Looks like:** 50 composite services. Each aggregates 5 backends in a slightly different way. Maintenance nightmare.

**Why it fails:** Composite services were a tactical fix; treating them as architecture creates a tier of N services with unclear ownership.

**The fix:** Audit. Consolidate where possible. For client-specific aggregation, use BFFs (owned by frontend teams).

### Point-to-Point Everywhere

**Looks like:** "Just call the API directly" between every pair of services. N² connections.

**Why it fails:** Coupling explodes. Moving any service breaks N consumers. Discovery is impossible.

**The fix:** Standardized integration via the Common Driveway pattern. Point-to-point only as documented exception.

### Orchestration Without Sagas

**Looks like:** Every workflow goes through an orchestrator. Even read paths. Even single-service flows.

**Why it fails:** Orchestrator becomes bottleneck and a god service.

**The fix:** Orchestration only for distributed transactions (sagas) and cross-cutting workflows. Choreography for the rest.

### CQRS as Default

**Looks like:** Adopting CQRS for everything. Doubling the codebase. Replication lag bugs everywhere.

**Why it fails:** CQRS is heavy. Most use cases don't need it.

**The fix:** Read replica + eventual consistency for most cases. Full CQRS only when read/write characteristics genuinely diverge.

### Event Stream as Database

**Looks like:** Querying Kafka directly for current state. Slow. Brittle.

**Why it fails:** Streams are append-only logs, not databases. Reading current state requires scanning history.

**The fix:** Stream → projection → read store. Or use a streaming-native KV store (RocksDB-backed) for state.

---

## Decision Rules

| Situation | Pattern |
|---|---|
| Strongly consistent read across domains | REST API (sync) |
| Cross-domain command (state change) | REST API or message queue |
| Multi-consumer change feed | Event broker / event stream |
| Periodic reconciliation / large batch | Batch processing |
| Source DB → analytics warehouse | CDC (event-based) |
| Client makes many backend calls | Composite service or BFF |
| Different frontends need different aggregations | Backend-for-Frontend per frontend |
| Read load crushes write DB | Read replica first; CQRS only if replica isn't enough |
| Distributed transaction across services | Saga via orchestration (or choreography for simple cases) |
| Latency budget < 100ms | Point-to-point sync (document exception) |
| Spiky API traffic threatening source | Queue-based load leveling |
| Time-window event correlation (fraud, alerting) | Complex Event Processing (CEP) |
| New cross-domain integration | Common Driveway via catalog |
| Tight coupling complaint | Likely sync where async would do; or shared mutation schema |

---

## Worked Example: Cross-Domain Customer Profile

**Context:** Multi-domain SaaS. Customer profile owned by Customer domain. Consumed by Marketing (segmentation), Support (CRM tickets), Billing (invoicing), Analytics (reporting).

**Per-consumer choice:**

| Consumer | Pattern | Why |
|---|---|---|
| Marketing | Event stream (Kafka) | Many segments; segments built on profile changes; multi-consumer fits |
| Support (CRM) | REST API (sync) | Agent needs current profile in <500ms; UI calls API directly |
| Billing | Event-based (CDC from Customer DB) | Profile change triggers billing recalc; eventual consistency OK |
| Analytics | Batch (nightly snapshot) | Daily reporting; cost optimization; latency tolerant |

**Common Driveway:** All four expose via DataHub catalog. Marketing's stream registered as a data product with schema + SLA. Support's API registered with OpenAPI spec. Billing's CDC topic registered. Analytics' nightly snapshot registered as a table contract.

**Result:** Customer domain is the Golden Source. Each consumer takes the appropriate pattern. No point-to-point spaghetti.

**Lesson:** "Which pattern" is wrong. The right question is "which pattern per consumer relationship." Different consumers have different constraints.

---

## Gotchas

- **Strong consistency in distributed systems is expensive.** Pursue it only where genuinely required (financial transactions, etc.).
- **Async patterns require idempotency at consumers.** Otherwise duplicates corrupt state.
- **Event ordering is not free.** Kafka offers per-partition ordering; getting global ordering is hard.
- **Replication lag in CQRS is real.** Plan for "this read might be slightly stale" in UX and tests.
- **Choreography is hard to debug.** Without distributed tracing, root-causing an event-driven flow is archaeology.
- **Composite services can become a hidden tier.** Document them; assign owners; review periodically.
- **CDC requires source cooperation.** Old/legacy DBs may not expose binlog or logical replication.
- **Saga compensation logic is non-trivial.** "Cancel the payment if shipping fails" is several edge cases.
- **Event schemas evolve.** Adopt schema registry (Confluent, Apicurio) and versioning discipline early.

---

## Further Reading

- *Data Management at Scale* (Strengholt), Chapter 4
- *Enterprise Integration Patterns* by Hohpe & Woolf — the canonical catalog
- *Building Microservices* by Sam Newman — sync vs async, BFF, etc.
- *Microservices Patterns* by Chris Richardson — Saga, CQRS, Event Sourcing in depth
- See `data-mesh-domain-topologies` for the Mesh context where these patterns operate
- See `mdm-and-federated-data-governance` for catalog and contract approaches

Source: *Data Management at Scale* (Strengholt), Chapter 4 (Application Integration & Data Distribution).
