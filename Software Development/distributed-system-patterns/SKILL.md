---
name: distributed-system-patterns
description: >
  Apply patterns for distributed systems and microservices: Saga, Sidecar,
  Backend-for-Frontend (BFF), Choreography vs Orchestration, Service Mesh,
  Database-per-Service, Broker-Domain. Use when building or evolving a
  microservices system, designing distributed transactions, isolating
  cross-cutting concerns, choosing between event choreography and orchestration,
  or designing API layers for multiple frontend devices. Triggers: "Saga
  pattern for X", "should we use choreography or orchestration?", "Sidecar
  for cross-cutting concerns", "BFF pattern", "service mesh", "distributed
  transaction across services". Produces structured pattern recommendation.
---

# Distributed System Patterns

You apply the named patterns that make distributed systems work in production.
Microservices and distributed architectures introduce specific failure modes;
these patterns are the well-validated solutions.

---

## When to Use This Skill

- Designing a distributed transaction across services (atomicity issues)
- Choosing between event choreography and orchestration
- Isolating cross-cutting concerns (logging, monitoring, auth) from domain code
- Designing API layers for multiple frontend devices
- Setting up service-to-service communication infrastructure

---

## The Patterns

### Saga: Distributed Transactions Done Right

The standard pattern for atomicity across microservice boundaries. ACID
transactions don't span services — Saga makes a sequence of local actions
that compensate on failure.

```
Service A                   Service B                Service C
┌─────────┐                 ┌─────────┐              ┌─────────┐
│ Step 1  │ ──── success ──→ │ Step 2  │ ── success ─→│ Step 3  │
│ Reserve │                 │ Charge  │              │ Ship    │
│ Stock   │                 │ Card    │              │ Order   │
└────┬────┘                 └────┬────┘              └────┬────┘
     │                           │                         │
     │←──── compensate ←─────────┤                        │
     │   (release stock)         │←──── compensate ←──────┤
     │                           │   (refund charge)       │
     │                           │                         │
                          ↑ if Ship fails ↑
```

| Pattern variant | Use when |
|---|---|
| **Orchestrated Saga** | Central orchestrator coordinates the sequence; clearer flow, single point of complexity |
| **Choreographed Saga** | Each service listens for events and acts; more decoupled, harder to trace |

**Key insight:** Compensating actions are not "undo" — they're forward-acting
business operations that semantically reverse the original. Refund ≠ deleting
charge record; release ≠ deleting reservation.

### Sidecar Pattern

Isolate cross-cutting operational concerns into a co-deployed companion.

```
┌─────────────────────────────────┐
│        Pod / Host               │
│  ┌──────────────┐ ┌──────────┐  │
│  │ Application  │ │ Sidecar  │  │
│  │  (domain)    │ │          │  │
│  │              │ │ - logs   │  │
│  │              │ │ - metrics│  │
│  │              │ │ - auth   │  │
│  │              │ │ - mTLS   │  │
│  └──────────────┘ └──────────┘  │
└─────────────────────────────────┘
```

**What goes in sidecar:** Logging, monitoring, auth/authz, mTLS termination,
service discovery, rate limiting.

**Why:** Domain code stays focused on business logic. Operational concerns
update independently across the fleet without app-team involvement.

**Real-world:** Istio's Envoy proxy is a sidecar; Datadog agent is a sidecar.

### Service Mesh

Service Mesh = sidecars + control plane. The control plane manages all sidecars
to provide a consistent operational fabric.

| Layer | What it does |
|---|---|
| **Data plane** (sidecars) | Handle traffic per-service |
| **Control plane** | Configure sidecars centrally; observability, policy, security |

**When to adopt:** > 10 services, complex inter-service traffic, need consistent
observability across services.

**Cost:** Significant operational complexity. Don't adopt for 3-service systems.

### Backends for Frontends (BFF)

A thin API adapter layer per frontend device, translating generic backend output
into client-specific formats.

```
                    ┌─────────────────────────┐
                    │  Generic Backend        │
                    │  (microservices, APIs)  │
                    └─────────┬───────────────┘
                              ↓
        ┌───────────┬─────────┴─────────┬──────────┐
        ↓           ↓                   ↓          ↓
   ┌────────┐  ┌────────┐          ┌────────┐ ┌────────┐
   │  iOS   │  │Android │          │  Web   │ │  3rd   │
   │  BFF   │  │  BFF   │          │  BFF   │ │ Party  │
   └────────┘  └────────┘          └────────┘ │  BFF   │
                                              └────────┘
```

**Why:** Different clients have different needs. iOS app wants compact JSON;
web wants HTML chunks; third-party wants standard REST. One backend that tries
to serve all becomes a god-API.

**When to adopt:** Multiple distinct client types with significantly different needs.

### Database-per-Service

Each microservice owns its data in a separate database (or schema). Other
services access via API only.

| Property | Why it matters |
|---|---|
| Bounded context preservation | Service owns its model |
| Independent evolution | Schema changes don't break other services |
| Independent scaling | DB scaled per service |
| Independent technology | Service can pick its DB type |

**The hard part:** Cross-service queries. You can't JOIN across databases.
Solutions: data duplication (controlled), CQRS read models, async event projection.

**Rule:** "Duplication is preferable to coupling." Storing related data in two
services is OK if it preserves bounded contexts.

### Choreography vs Orchestration

Two ways services coordinate.

| Pattern | How it works | Best for | Tradeoff |
|---|---|---|---|
| **Choreography** | Services emit events; others subscribe and react | Loosely coupled flows; bounded contexts respected | Hard to trace; emergent behavior |
| **Orchestration** | A central orchestrator sends commands to services | Complex multi-step flows that need coordination | Single point of complexity; orchestrator can become god-service |

**Rule of thumb:** Start with choreography. Adopt orchestration when complex
flows need explicit coordination.

### Broker-Domain Pattern

Multiple message brokers, each serving a domain cluster, vs single shared broker.

| Pattern | Setup | Pros | Cons |
|---|---|---|---|
| **Single Broker** | One broker for all services | Simple ops | Single point of failure; ownership coupling |
| **Broker-Domain** | Each domain cluster has its own broker | Fault isolation; domain ownership | More ops surface |

**When to adopt Broker-Domain:** Large enough that domain teams want to own
their messaging infra independently.

---

## Principles

- **Extreme decoupling.** "Duplication is preferable to coupling." Don't share databases or schemas across services.
- **Bounded contexts as service boundaries.** Domain-driven service partitioning beats technical partitioning.
- **Network is unreliable.** All distributed patterns must assume failures. Timeouts, retries, circuit breakers always.
- **Eventual consistency is the rule, not the exception.** Strong consistency across services is rarely worth its cost.
- **Sidecars for cross-cutting concerns.** Don't bake auth/logging/monitoring into every service. Let sidecars handle it.
- **Start simple, evolve toward complexity.** Choreography before orchestration. Single broker before broker-domain. Add operational complexity only when justified by scale.

---

## Anti-Patterns to Avoid

### Distributed Monolith

**Looks like:** Multiple services that must deploy together; shared schema; tight coupling.

**Why it fails:** All the operational cost of distribution, none of the independence benefits.

**The fix:** Either consolidate to monolith with good modularity, OR truly decouple (per-service DB, async communication, no shared schema).

### Saga Without Compensation Planning

**Looks like:** Implementing the happy path of multi-service transactions, hoping nothing fails.

**Why it fails:** Failures will happen; without compensating actions, system enters inconsistent states.

**The fix:** Design compensating actions for every step before implementing the saga. They're business logic, not afterthoughts.

### Premature Service Mesh

**Looks like:** Adopting Istio for a 3-service system "for the future."

**Why it fails:** Operational complexity exceeds benefits. Service mesh is for 10+ service systems.

**The fix:** Use simple sidecars or library-based approaches first. Adopt service mesh when service count justifies it.

### God Orchestrator

**Looks like:** Central orchestrator that knows about every service and every workflow.

**Why it fails:** Becomes a god-service that everyone touches. Single point of complexity. Deploys risky.

**The fix:** Multiple smaller orchestrators per business workflow. Or shift to choreography for simpler flows.

### Sharing a Database Across Services

**Looks like:** Two microservices accessing the same database. "It's fine, they query different tables."

**Why it fails:** Schema changes break both services. Coupling at the data layer is the worst kind.

**The fix:** Database-per-service. If services need related data, duplicate it via events.

---

## Decision Rules

| Condition | Action |
|---|---|
| Multi-service workflow with atomicity needs | Saga (orchestrated for clarity, choreographed for decoupling) |
| Cross-cutting concerns clutter every service | Sidecar pattern |
| > 10 services with complex inter-service traffic | Service mesh |
| Multiple distinct client types (iOS, web, partners) | BFF per client |
| Service-to-service queries needed | Duplicate data via events; don't share DB |
| Simple service coordination | Choreography |
| Complex multi-step coordination | Orchestration with workflow service |
| Domain teams own their messaging | Broker-domain pattern |

---

## Worked Example: E-Commerce Order Flow

**Goal:** Place an order across Inventory, Pricing, Payment, Shipping, Notification services.

| Step | Service | Action | Compensation |
|---|---|---|---|
| 1 | Inventory | Reserve stock | Release reservation |
| 2 | Pricing | Calculate final price + tax | (no compensation needed; idempotent) |
| 3 | Payment | Charge card | Refund |
| 4 | Shipping | Schedule shipment | Cancel shipment |
| 5 | Notification | Send confirmation | Send cancellation notice |

**Choice:** Orchestrated Saga. The flow is complex enough that explicit
coordination beats implicit choreography for clarity and debuggability.

**Sidecars:** Each service has Envoy sidecar for mTLS, observability, retries.
**BFF:** Mobile app has its own BFF that combines order + tracking calls.
**Service Mesh:** Istio manages cross-service auth and traffic shaping.

**Lesson:** Distributed patterns compose. A real production system uses 5-10
of them simultaneously. Each addresses a specific failure mode.

---

## Gotchas

- **Saga orchestrator state must be durable.** If orchestrator crashes mid-saga, recovery requires durable state. Use a workflow engine (Temporal, AWS Step Functions).
- **Compensations aren't always possible.** Some actions are irreversible (sending an email, calling a webhook). Plan for this.
- **Sidecar resource cost is real.** Each sidecar consumes CPU + memory. At fleet scale, this adds up.
- **BFF can become its own monolith.** Watch for one BFF doing too much. One BFF per *client class*, not one BFF for all clients.
- **Choreography is trace-hostile.** Event-driven flows are hard to debug. Invest in distributed tracing (OpenTelemetry) before adopting.

Source: *Fundamentals of Software Architecture* by Mark Richards and Neal Ford, distributed systems chapters.
