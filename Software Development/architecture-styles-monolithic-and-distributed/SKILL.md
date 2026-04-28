---
name: architecture-styles-monolithic-and-distributed
description: >
  Choose the right architectural style for a system: Layered, Pipeline,
  Microkernel, Service-Based, Event-Driven, Microservices, Space-Based.
  Use when architecting a new system and deciding the top-level structure,
  evaluating whether to evolve from monolith to distributed, or comparing
  trade-offs between architectural styles. Triggers: "what architecture for
  X?", "monolith vs microservices", "Layered vs Microkernel", "should we
  use microservices?", "Space-Based architecture for high scale". Produces
  structured architecture style recommendation with characteristics rating.
---

# Architecture Styles: Monolithic and Distributed

You guide the top-level architectural style decision — the foundational shape
of a system. The choice constrains everything downstream. Wrong style
selection costs months of rework.

---

## When to Use This Skill

- Architecting a new system and choosing the top-level style
- Evaluating evolution from monolith to distributed
- Comparing architectural styles for a specific use case
- Diagnosing whether current architecture matches problem characteristics

---

## The Major Architecture Styles

### Monolithic Styles

| Style | Structure | Best for |
|---|---|---|
| **Layered (N-tier)** | Components organized by technical capability (presentation, business, persistence) | Small/medium apps; teams new to architecture; clear technical separation |
| **Pipeline** | Pipes & filters; unidirectional data flow (Producer → Transformer → Tester → Consumer) | Workflow-based processing, ETL pipelines, compilers |
| **Microkernel** | Core system + plug-ins | Apps with extension points; product lines (IDEs, browsers) |

### Distributed Styles

| Style | Structure | Best for |
|---|---|---|
| **Service-Based** | Coarse-grained services; often shared monolithic database | Pragmatic distributed; less ops complexity than microservices |
| **Event-Driven** | Services communicate via events through a broker | High decoupling; reactive systems; complex event flows |
| **Microservices** | Fine-grained services aligned to bounded contexts; database-per-service | Independent team ownership; differing scale needs; high deploy cadence |
| **Space-Based** | Replicated processing units + in-memory data grid | Extreme elastic scaling; high-throughput unpredictable load |

---

## Layered Architecture

The default for most teams. Components grouped by technical capability.

```
┌───────────────────────────────┐
│       Presentation Layer      │
└──────────────┬────────────────┘
               ↓
┌───────────────────────────────┐
│     Business Rules Layer      │
└──────────────┬────────────────┘
               ↓
┌───────────────────────────────┐
│      Persistence Layer        │
└──────────────┬────────────────┘
               ↓
┌───────────────────────────────┐
│        Database Layer         │
└───────────────────────────────┘
```

### Closed vs Open Layers

- **Closed layers:** Requests must traverse every layer. Stricter; better isolation.
- **Open layers:** Some layers can be bypassed. More flexible; weaker isolation.

**Default:** Closed layers. Open them only with deliberate justification.

### Anti-Patterns

- **Fast-Lane Reader:** Presentation accesses Database directly, bypassing layers. Quick fix, long-term coupling disaster.
- **Architecture Sinkhole:** Most requests pass through all layers performing trivial work. Symptom of wrong style — domain doesn't decompose into layers cleanly.

---

## Microkernel Architecture

Core system + plug-ins.

```
                ┌──────────┐
                │   Core   │
                │  System  │
                └─────┬────┘
                      │
        ┌─────────┬───┴────┬─────────┐
        ▼         ▼        ▼         ▼
   ┌────────┐┌────────┐┌────────┐┌────────┐
   │Plug-in ││Plug-in ││Plug-in ││Plug-in │
   │   1    ││   2    ││   3    ││   4    │
   └────────┘└────────┘└────────┘└────────┘
```

**Key principle:** Core contains only the **minimal happy path**. Complex domain
logic lives in plug-ins.

**Best for:** IDE/editor architectures, product line engineering, apps with
extension marketplaces.

---

## Service-Based Architecture (Pragmatic Distributed)

| Property | Value |
|---|---|
| Service granularity | Coarse (4-12 services typical) |
| Database | Often shared monolithic |
| Communication | Usually REST |
| Operational complexity | Medium (much less than microservices) |

**Why it matters:** Service-based gets you 80% of the benefits of microservices
with 20% of the operational pain. A pragmatic middle ground.

**When to choose:** When you want some distributed properties (independent
deployability for some services, separation of concerns) but don't want full
microservices commitment.

---

## Microservices Architecture

| Property | Value |
|---|---|
| Service granularity | Fine (aligned to bounded contexts) |
| Database | Database-per-service |
| Communication | Mix of sync REST and async events |
| Operational complexity | High |
| Architecture quantum | Each service is independent |

### When Microservices Earn Their Cost

✅ Different services have **genuinely different scaling needs**
✅ Different services have **different deployment cadences** (some daily, some monthly)
✅ Multiple teams need to own services **independently**
✅ Bounded contexts in the domain are **clearly identifiable**
✅ Operational maturity (monitoring, observability, on-call) is **already strong**

### When Microservices Are Wrong

❌ Small team (< 8 engineers) — overhead exceeds benefits
❌ Tightly coupled domain — services constantly change together
❌ Operational immaturity — distributed systems amplify ops gaps
❌ Premature optimization — start with monolith, extract services when justified

---

## Space-Based Architecture

For extreme scale. Replicated processing units + in-memory data grid; no central database in the hot path.

```
┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
│ Processing Unit 1  │  │ Processing Unit 2  │  │ Processing Unit N  │
│  - In-memory data  │  │  - In-memory data  │  │  - In-memory data  │
└─────────┬──────────┘  └─────────┬──────────┘  └─────────┬──────────┘
          ↕                       ↕                       ↕
          ────────── replicated tuple space ──────────────
                              ↕
┌─────────────────────────────────────────────────────────┐
│              Data Pumps + Data Writers                  │
│         (asynchronously persist to database)            │
└─────────────────────────────────────────────────────────┘
```

**Use case:** High-volume, unpredictable load (ticketing, flash sales, real-time
auctions).

**Cost:** High operational complexity. Eventual consistency. Hard to debug.

---

## Choosing a Style: Characteristics Comparison

Rate each architecture on key characteristics (1=poor, 5=excellent):

| Characteristic | Layered | Microkernel | Service-Based | Microservices | Space-Based |
|---|---|---|---|---|---|
| **Simplicity** | 4 | 3 | 3 | 1 | 1 |
| **Deployability** | 1 | 2 | 4 | 5 | 4 |
| **Elasticity** | 1 | 1 | 3 | 4 | 5 |
| **Performance** | 2 | 3 | 3 | 2 | 5 |
| **Scalability** | 1 | 1 | 3 | 5 | 5 |
| **Modularity** | 2 | 4 | 4 | 5 | 3 |
| **Testability** | 3 | 4 | 4 | 4 | 2 |
| **Reliability** | 3 | 3 | 3 | 4 | 4 |
| **Operational simplicity** | 5 | 5 | 4 | 1 | 1 |

**Use this:** Rate your top 3-5 critical characteristics. Pick the style with the highest combined score on those characteristics.

---

## Principles

- **Distinguish logical from physical architecture.** Logical = what the system does. Physical = how it's deployed. Don't conflate them.
- **Iterative component identification.** Start with user stories → identify candidate components → refine against architectural characteristics.
- **Domain partitioning > technical partitioning.** Industry trend favors organizing by domain, not by layer. Better aligns with team boundaries and business changes.
- **Network is unreliable.** Any distributed style must assume network failures. Timeouts, circuit breakers, retries built in.
- **Data minimization in distributed.** Send only what's needed. Network and serialization costs add up.
- **Contract governance is critical.** When services share contracts, change discipline matters.

---

## Anti-Patterns to Avoid

### Premature Microservices

**Looks like:** Splitting a small project into 8 microservices "for scalability."

**Why it fails:** Operational complexity exceeds benefits. Distributed monolith.

**The fix:** Start monolithic with good modularity. Extract services when you have evidence (organizational scaling, divergent deploys, distinct scaling).

### Big Ball of Mud

**Looks like:** No discernible structure. Components instantiate each other freely. Layers leak.

**Why it fails:** Every change is risky. No predictable impact analysis.

**The fix:** Adopt one of the named styles. Enforce its boundaries.

### Architecture Sinkhole

**Looks like:** Most requests pass through all layers performing trivial work.

**Why it fails:** Style mismatch — domain doesn't decompose into layers naturally. Wasted indirection.

**The fix:** Switch to domain partitioning, microkernel, or service-based.

### Distributed Monolith

**Looks like:** Multiple services that must deploy together; tight coupling via shared DB or shared schema.

**Why it fails:** All the operational cost of microservices, none of the benefits.

**The fix:** Either consolidate to one monolith, or properly decouple (database per service, async communication, no shared schema).

---

## Decision Rules

| Condition | Style |
|---|---|
| Small team, simple domain | Layered (default) |
| Workflow / ETL / data pipeline | Pipeline |
| Plugin architecture, extensibility | Microkernel |
| Some distributed benefits without ops burden | Service-Based |
| High-decoupling reactive system | Event-Driven |
| Independent team ownership + bounded contexts + ops maturity | Microservices |
| Extreme elastic scale, unpredictable load | Space-Based |
| Existing monolith painful to scale, but team < 8 | Improve modularity, don't decompose yet |

---

## Worked Example: Choosing for a B2B SaaS Backend

**Context:** B2B SaaS, ~20 engineers, 5 product teams, single-tenant deployments.

**Critical characteristics:**
1. Modularity (teams own different parts independently)
2. Deployability (each team ships on own cadence)
3. Operational simplicity (small ops team)

**Comparison:**

| Style | Modularity | Deployability | Op Simplicity | Total |
|---|---|---|---|---|
| Layered | 2 | 1 | 5 | 8 |
| Service-Based | 4 | 4 | 4 | 12 |
| Microservices | 5 | 5 | 1 | 11 |

**Decision:** Service-Based wins. Coarse-grained services enable team ownership
and independent deploys without microservices ops overhead.

**Lesson:** Microservices score highest on modularity + deployability but the
ops simplicity score is decisive given the small ops team.

---

## Gotchas

- **Architectural Quantum is the unit of independent deployment.** A microservices system with shared DB has architectural quantum = the whole system, not individual services.
- **Choosing a style isn't permanent but is expensive to change.** Treat the choice with the weight of "we'll live with this for 2-3 years."
- **Communication between services dominates costs in distributed.** Network calls = 100-1000x slower than in-process. Plan accordingly.
- **Eventual consistency is harder than it looks.** Sounds simple in slides; produces production incidents in practice.

Source: *Fundamentals of Software Architecture* by Mark Richards and Neal Ford, architecture styles chapters.
