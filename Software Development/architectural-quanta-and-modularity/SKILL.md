---
name: architectural-quanta-and-modularity
description: >
  Defines and applies the architectural quantum vocabulary from
  Ford/Richards/Sadalage/Dehghani Software Architecture: The Hard Parts
  Ch 1-3. Use to determine whether a proposed system is actually multiple
  services or a distributed monolith, to identify quantum boundaries, to
  reason about static vs dynamic coupling, to assess modularity drivers
  (maintainability/testability/deployability/scalability/availability/
  fault tolerance), and to apply the quantum test before any
  decomposition decision. This is foundational vocabulary; load it
  before downstream Hard Parts skills if the team is new to the
  taxonomy. Triggers - "architectural quantum", "is this a real
  microservice", "distributed monolith test", "shared database problem",
  "static coupling", "dynamic coupling", "quantum boundary", "high
  functional cohesion", "modularity drivers", "should we decompose",
  "why decompose", "Conway's Law shaped my services", "is this one
  service or many". Produces a quantum inventory + modularity-driver
  assessment + ADR if decomposition is being considered. Step-by-step
  workflow.
---

# Architectural Quanta and Modularity Drivers

You walk architects through the **foundational vocabulary** of *Software Architecture: The Hard Parts* (Ford/Richards/Sadalage/Dehghani 2021, Ch 1–3): architectural quanta, static vs dynamic coupling, and the six modularity drivers. This skill is the on-ramp to every other Hard Parts skill — load it first if the team is new to the taxonomy.

This is a **workflow** skill. When loaded, you march the user through a quantum inventory and a modularity-driver assessment. Output: a quantum map of the current system + a decision on whether decomposition is justified.

Pattern definitions live at:
- `references/software-architecture-the-hard-parts/frameworks.md#architectural-quantum`
- `references/software-architecture-the-hard-parts/frameworks.md#coupling-vocabulary`
- `references/software-architecture-the-hard-parts/frameworks.md#modularity-drivers`

---

## Related

- **Related skills**
  - `service-and-data-decomposition` — the downstream "now how do we split?" skill once decomposition is justified
  - `data-ownership-and-distributed-data` — the data-layer companion to quantum identification
  - `architecture-styles-monolithic-and-distributed` — augmented to use this skill's quantum vocabulary
  - `software-modularity-principles` — augmented to use this skill's modularity-driver framework
- **Related references**
  - `references/software-architecture-the-hard-parts/frameworks.md#architectural-quantum`
  - `references/software-architecture-the-hard-parts/frameworks.md#modularity-drivers`
  - `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md#ch-2-sysops-squad-saga-understanding-quanta`

---

## Contract for this skill

Two phases, ~20–30 minutes total:

- **Phase 1** — inventory the quanta in the current (or proposed) system
- **Phase 2** — assess modularity drivers to decide whether decomposition is justified

If both phases pass cleanly, the next skill to load is `service-and-data-decomposition` (for how to decompose). If Phase 2 fails (no modularity drivers broken), **don't decompose** — the cost isn't justified.

---

# Phase 1 — Identify the Quanta

## Step 1.1 — Define architectural quantum

A quantum has three properties (all required):

1. **Independently deployable artifact** — can be deployed alone without coordination with other artifacts
2. **High functional cohesion** — internal elements serve a single domain purpose
3. **Synchronous dynamic coupling** at runtime forms a quantum boundary — services that *must* be synchronously coupled at runtime belong to the same quantum

State this to the user. The vocabulary is non-negotiable; later steps assume it.

## Step 1.2 — Inventory candidates

List each candidate service / module / deployable in the system. For each, score the three properties.

```
Candidate                | Indep. deployable? | High cohesion? | Sync dynamic coupling?
-------------------------|--------------------|--------------- |----------------------
UserAuthService          | yes                | yes            | (none on critical path)  → 1 quantum
TicketService            | yes                | yes            | calls AssignmentService sync   → 1 quantum with…
AssignmentService        | yes                | yes            | called sync by TicketService    →  …TicketService
NotificationService      | yes                | yes            | async-only                     → independent quantum
ReportingService         | shared DB w/ Ticket | n/a            | shared DB                     → same quantum as TicketService (!)
```

The last row is the **distributed monolith reveal** — ReportingService looks like a separate service but shares a database with TicketService, so they're one quantum together.

## Step 1.3 — Apply the quantum test

For each pair of candidates, ask: **can you deploy A without coordinating with B?**

| Answer | Implication |
|---|---|
| Yes | Different quanta |
| No (sync critical path) | Same quantum |
| No (shared DB / schema) | Same quantum |
| No (shared deploy pipeline) | Same quantum |
| Async only between them | Different quanta |

The pairwise test produces a **quantum partition** of the candidates.

## Step 1.4 — Static vs dynamic coupling diagrams

For each quantum, build (or describe) a **static-coupling diagram** with:

- OS / container dependencies
- Transitive library/framework dependencies
- Persistence dependencies (DBs, search engines, cloud services)
- Architecture integration points
- Messaging infrastructure required to bootstrap

And a **dynamic-coupling map** showing:

- Sync calls (heavy lines — these create quantum boundaries)
- Async calls (light lines — these do not)
- Event subscriptions

The two diagrams are the artifacts of Phase 1. Many systems have surprising results when these are drawn for the first time.

### Output of Phase 1

```
Quantum 1: <services>
  Static coupling diagram: <description>
  Dynamic coupling: <sync internal calls, async external calls>

Quantum 2: <services>
  ...

Distributed-monolith reveals:
  - <services that appeared independent but are actually one quantum>
```

### Checkpoint

If the quantum count is much smaller than the service count, the system is more monolithic than the team realized. **Surface this finding** — most teams won't have heard it framed this way before.

---

# Phase 2 — Modularity Driver Assessment

If the team is *considering decomposition*, run this phase. If they're just trying to understand the current architecture, skip to ADR.

## Step 2.1 — Score the six drivers

For the current system, score each driver:

| Driver | Score: working / broken / critically broken | Evidence |
|---|---|---|
| **Maintainability** | | (e.g., "changes ripple unpredictably across 6 teams") |
| **Testability** | | (e.g., "test suite is 2 hours; flakes once a week") |
| **Deployability** | | (e.g., "monthly deploys; 30% rollback rate") |
| **Scalability / Elasticity** | | (e.g., "single bottleneck drags entire system at peak") |
| **Availability** | | (e.g., "one bad release brings down everything") |
| **Fault Tolerance** | | (e.g., "errors propagate; circuit breakers absent") |

**Evidence is required.** Vague "we want better X" is not a driver — name a specific failure with a number or example.

## Step 2.2 — Test for false drivers

The book is explicit: *"we want microservices"* is **not** a driver. Watch for false drivers the team may surface:

| Stated reason | Real driver? |
|---|---|
| "Industry best practice" | No |
| "Our competitors do it" | No |
| "Cloud-native" / "modern architecture" | No |
| "We hired engineers who want microservices" | No (Conway's-law warning) |
| "Deploys take 2 hours and block release" | Yes — Deployability |
| "Black Friday load spikes drag our whole stack" | Yes — Scalability differential |
| "Reporting workload kills the OLTP path" | Yes — Fault Tolerance |

If after evidence-testing **no driver is critically broken**, the answer is: **don't decompose**. Modularity inside the monolith is the cheaper path.

## Step 2.3 — Connect drivers to decomposition strategy

If at least one driver is critically broken, the broken driver(s) determine the decomposition emphasis:

| Critically broken driver | Decomposition emphasis |
|---|---|
| Maintainability | Bounded-context separation, domain alignment |
| Testability | Test isolation per service |
| Deployability | Independent release cadences per team |
| Scalability | Separate quanta for different load profiles |
| Availability | Separate quanta with separate SLOs |
| Fault Tolerance | Bulkhead-style isolation, separate failure domains |

The emphasis informs *how* to decompose, not just *whether*. Hand off to `service-and-data-decomposition` skill with the emphasis noted.

---

## Step 3 — Write the ADR

Whether you decompose or not, write an ADR. The ADR is valuable in either direction.

### If keeping the monolith:

```
ADR-NNN: Retain monolithic architecture

Context:
  Quantum inventory: <result of Phase 1>
  Modularity driver assessment: <result of Phase 2>

Decision:
  Retain current monolithic architecture. Invest in modularity within the
  monolith (Software Modularity Principles skill) rather than decomposition.

Rationale:
  No modularity drivers are critically broken. The cost of decomposition
  is not justified by current evidence.

Consequences:
  Positive: Operational simplicity preserved. Engineering velocity unchanged.
  Negative: If future drivers break, decomposition cost will be higher.
  Mitigations: Revisit annually. Track driver health in retros.
```

### If decomposing:

```
ADR-NNN: Decompose <system> based on <broken drivers>

Context:
  Quantum inventory: <result of Phase 1>
  Critically broken drivers: <list with evidence>

Decision:
  Decompose into N quanta following <Component-Based / Tactical Forking>.
  Emphasis: <broken-driver-aligned emphasis from Step 2.3>.

Hand-off:
  service-and-data-decomposition skill walks the decomposition itself.

Consequences:
  Positive: <broken drivers addressed>
  Negative: Operational complexity increases (N quanta to deploy, monitor, secure)
  Mitigations: <…>
```

---

## Common failure modes (call these out when you see them)

### "We have 12 microservices"

Apply the quantum test. The team often discovers they have 2–4 quanta, not 12 services. The remaining "services" are coupled by shared DB / sync calls / shared deploy and aren't independent quanta.

### "We want to decompose because the monolith is hard to work with"

Force the broken-driver question. "Hard to work with" is too vague. Which driver is broken? With what evidence? If they can't answer, the problem may be elsewhere (team structure, tooling, documentation) and decomposition won't fix it.

### "We share the database but it's fine because we only read"

If multiple services *write* the same tables, they're one quantum (and probably a Common Ownership problem — load `data-ownership-and-distributed-data` skill). If they only read, the read pattern is a separate decision (Inter-Service Communication / Replicated Cache / etc.) — same skill.

### "Async makes us independent quanta"

Mostly true. Async between two services breaks the synchronous-coupling test. But check: do they share a deployment pipeline? Do they share a database? Async between them doesn't help if they're coupled through other paths.

### "Our team boundaries don't match the quanta"

Conway's Law is at work. The book mostly leaves this to other texts (Team Topologies). Flag the misalignment; recommend the team read Skelton/Pais. The mismatch will produce constant friction regardless of how clean the technical decomposition is.

### "We can decompose later if we need to"

Sometimes true; often not. Decomposition cost grows superlinearly with the size and entanglement of the monolith. If you can credibly defer to "later," that's evidence drivers aren't critically broken yet — don't decompose now. But monitor the drivers.

---

## When NOT to invoke this skill

- **Single-team, single-service systems** — quantum vocabulary adds no value
- **Greenfield architecture** — easier to design quanta correctly from the start than to retrofit; this skill is more useful for analysis than greenfield design
- **Frontend-heavy systems** — quantum framing is server-side; use frontend-specific vocabulary for those

---

## Worked example

The Sysops Squad team (Ch 2) discovers they have **one quantum** at the start: the ticketing monolith. By Ch 3, they assess modularity drivers and find **all six are critically broken**. By Ch 4, they begin decomposition. By Ch 15, they have ~10 quanta with healthy modularity-driver scores.

The whole arc is a worked example of this skill. See `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md#ch-2-sysops-squad-saga-understanding-quanta` and `#ch-3-sysops-squad-saga-creating-a-business-case`.
