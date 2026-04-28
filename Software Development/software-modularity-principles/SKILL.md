---
name: software-modularity-principles
description: >
  Apply modularity, cohesion, separation of concerns, and information hiding
  to software design. Use when designing a new system, refactoring code with
  growing complexity, deciding service/module boundaries, evaluating whether
  to extract or merge modules, or applying YAGNI to feature requests. Triggers:
  "design a service for X", "should we extract this into a module?",
  "refactor for better modularity", "cohesion vs coupling", "where should this
  code live?", "ports and adapters pattern", "YAGNI on feature X". Produces
  structured architectural guidance grounded in modularity principles.
---

# Software Modularity Principles

You design software systems applying modularity, cohesion, and separation of
concerns. These aren't aesthetic preferences — they're the engineering
properties that determine whether software stays changeable as it grows.

---

## When to Use This Skill

- Designing a new service or system from requirements
- Refactoring code where complexity is hurting iteration speed
- Deciding service/module boundaries (extract or merge?)
- Applying YAGNI to a feature that "might be useful later"
- Diagnosing why a codebase is hard to change

---

## The Core Concepts

| Concept | Definition | Why it matters |
|---|---|---|
| **Modularity** | Degree to which a system's components can be separated and recombined | High modularity = parts can be replaced/changed independently |
| **Cohesion** | How much the elements inside a module belong together | High cohesion = each module has one clear purpose |
| **Coupling** | Dependencies between modules | Loose coupling = changes don't ripple |
| **Separation of Concerns** | Each section addresses one issue | Reduces interdependencies; isolates change impact |
| **Information Hiding** | Hide internal workings; expose stable interfaces | Internal changes don't break callers |

### The Two Levers

```
                 LOW COUPLING
                      ↑
                      │
   weak ←─────────────┼─────────────→ strong
                      │
                      ↓
                LOOSE COUPLING

       LOW COHESION ←──────→ HIGH COHESION
```

**Goal:** High cohesion AND loose coupling. Both, simultaneously, at every
level of the system.

---

## Essential vs Accidental Complexity

| Type | Source | What to do |
|---|---|---|
| **Essential** | The problem itself (business logic, domain rules) | Express as cleanly as possible |
| **Accidental** | Our chosen solution (database, framework, infrastructure) | Minimize aggressively; isolate from essential |

**The rule:** Essential complexity is unavoidable. Accidental complexity is
your choice. Software gets bad when accidental complexity bleeds into the
essential domain logic.

### Where to Draw the Boundary

```
┌────────────────────────────────────────────┐
│            ESSENTIAL COMPLEXITY            │
│     (domain models, business rules)        │
└────────────────────────────────────────────┘
                      ↕  via Ports
┌────────────────────────────────────────────┐
│            ACCIDENTAL COMPLEXITY           │
│  (DB, HTTP, queues, third-party APIs)      │
└────────────────────────────────────────────┘
```

The translation layer (ports + adapters) is where accidental → essential
conversions happen. Domain code never imports framework or DB libraries directly.

---

## Ports & Adapters Pattern

The architectural realization of separation of concerns.

| Component | Role |
|---|---|
| **Domain core** | Business logic; depends on nothing external |
| **Ports (interfaces)** | Domain's view of what it needs (abstract) |
| **Adapters** | Implementations that translate to/from external systems |

```
                    ┌──────────────┐
                    │  Domain Core │
                    │   (Pure)     │
                    └──────┬───────┘
                           │
                           ▼ defines
                    ┌──────────────┐
                    │     Ports    │
                    │ (interfaces) │
                    └──────┬───────┘
                           │
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
        ┌────────┐   ┌─────────┐    ┌────────┐
        │  HTTP  │   │   DB    │    │ Queue  │
        │adapter │   │ adapter │    │adapter │
        └────────┘   └─────────┘    └────────┘
```

**Benefits:**
- Domain testable without infrastructure
- Infrastructure swappable (Postgres → DynamoDB) without domain changes
- Domain language clean of framework concepts

---

## Domain-Driven Design (DDD): Identifying Boundaries

Use DDD techniques to find the *natural* lines of separation in a problem domain.

| Concept | What it is |
|---|---|
| **Bounded Context** | A region where one model is consistent; outside it, the model differs |
| **Ubiquitous Language** | Within a bounded context, one shared vocabulary between business and code |
| **Anti-Corruption Layer** | Boundary that prevents one bounded context from infecting another with its model |
| **Event Storming** | Collaborative technique to identify domain events and bounded contexts |

**Why this matters:** Bounded contexts are *better* boundaries for services
than technical divisions. They're naturally decoupled because they reflect
real-world domain boundaries.

---

## Principles

- **Fractal Modularity.** Apply modularity recursively at every level: enterprise → service → module → class → function.
- **High Cohesion.** Each unit does one thing. If you can't describe its purpose in one sentence, it's not cohesive enough.
- **Loose Coupling.** Components change independently. Dependencies flow through stable interfaces, not concrete implementations.
- **Separate Essential from Accidental.** Domain code never depends on framework code. The essential is pure; the accidental is isolated at boundaries.
- **Information Hiding.** Expose what callers need; hide everything else. Today's "internal detail" is tomorrow's API breaking change if exposed.
- **Testability as Design Driver.** If something is hard to test, the design is wrong. Use testing pain as feedback on design.
- **YAGNI (You Ain't Gonna Need It).** Write only what current problems require. Speculative generality is a debt magnet.
- **Consistent Abstraction Levels.** Within a unit of code, all operations should be at the same level of abstraction. Mixing levels hides intent.
- **Low Tolerance for Complexity.** When complexity grows, refactor immediately. Cleanup deferred = cleanup never done.

---

## Anti-Patterns to Avoid

### God Object / God Module

**Looks like:** One class or module that does everything; thousands of lines; many responsibilities.

**Why it fails:** Low cohesion (mixed responsibilities), high coupling (everything depends on it), impossible to test.

**The fix:** Extract responsibilities into focused modules. The Single Responsibility Principle is a guide here.

### Speculative Generality

**Looks like:** "We might need to support multiple databases someday" → premature abstraction layer with one implementation.

**Why it fails:** Adds complexity for hypothetical future. Often the imagined future never arrives, or arrives differently.

**The fix:** YAGNI. Build for current needs. Refactor to abstraction *when* the second use case appears.

### Leaking Abstractions

**Looks like:** Domain code that says `userRepo.queryByEmailLowerCase()` — abstraction includes implementation detail (SQL-style query syntax).

**Why it fails:** Couples domain to implementation. Changing the underlying store breaks domain code.

**The fix:** Domain expresses intent, not implementation. `userRepo.findByEmail(email)` lets the adapter handle case sensitivity internally.

### Inconsistent Abstraction Levels

**Looks like:** A function that mixes high-level orchestration with low-level byte manipulation.

**Why it fails:** Reader has to context-switch constantly. Hides the actual algorithm.

**The fix:** Each function operates at one level. Lower levels live in their own functions.

### Premature Microservices

**Looks like:** Splitting a small project into 10 microservices "for scalability."

**Why it fails:** Adds operational complexity (deployment, networking, observability) without solving real problems. Distributed monolith.

**The fix:** Start with a well-modularized monolith. Extract services only when you have evidence (organizational scaling, divergent deploy cadences, distinct scaling needs).

---

## Decision Rules

| Condition | Action |
|---|---|
| Module is "doing too much" | Extract. Each unit, one purpose. |
| Two modules constantly change together | They might belong together. Consider merging. |
| Function harder to test than expected | Design is wrong. Refactor for testability. |
| Adding hypothetical-future flexibility | YAGNI. Build for now. |
| Domain code imports framework code | Wrong direction. Move domain to pure layer; access framework via port + adapter. |
| Function has > 50 lines or > 3 levels of indentation | Likely violating SRP or mixing abstraction levels. Decompose. |
| Choosing service boundary | Match bounded contexts, not technical layers. |

---

## Worked Example: Refactoring a Tightly-Coupled Order Service

**Starting state:** `OrderService` 2000 lines. Imports SQLAlchemy, Stripe SDK, Twilio SDK, internal pricing engine. Tests require live DB and mocked external services.

| Step | Action | Why |
|---|---|---|
| 1 | Identify the essential: order lifecycle, pricing calculation, stock reservation | Domain logic |
| 2 | Identify the accidental: persistence, payment, SMS notification | Infrastructure |
| 3 | Define ports: `OrderRepository`, `PaymentGateway`, `Notifier` | Domain's view of what it needs |
| 4 | Move essential logic to pure domain module; ports are abstract | Domain becomes testable in isolation |
| 5 | Implement adapters for SQLAlchemy, Stripe, Twilio | Infrastructure is now interchangeable |
| 6 | Tests for domain become fast unit tests with fake adapters | 1000x speed improvement |
| 7 | Tests for adapters are integration tests against real systems | Smaller, focused, less frequent |

**Lesson:** Most of "monolithic service is unmaintainable" complaints are
really "domain and infrastructure are tangled." Untangle them before considering
microservices.

---

## Gotchas

- **Modularity has overhead.** Indirection costs cognitive load. Don't apply maximum modularity to a 50-line script.
- **Premature ports + adapters.** Adding ports for a single use case is YAGNI violation. Wait for the second use case.
- **DDD is not free.** Event Storming, ubiquitous language work require domain expert time. Worth it for complex domains, overkill for simple CRUD.
- **Coupling is inevitable, not eliminated.** Manage it; don't pretend it doesn't exist.
- **Refactoring tests is part of refactoring.** Tests that depend on internals create as much coupling as production code. Refactor both.

Source: *Modern Software Engineering* by Dave Farley, Chapters 7-9.
