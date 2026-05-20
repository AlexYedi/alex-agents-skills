---
name: service-and-data-decomposition
description: >
  Walks through decomposing a monolithic codebase into services using
  the two top-level approaches from Ford/Richards/Sadalage/Dehghani
  Software Architecture: The Hard Parts Ch 4-5 - Component-Based
  Decomposition (when the codebase has identifiable namespaces/packages)
  and Tactical Forking (when the codebase is too tangled to analyze).
  Covers the 6 sequenced Component-Based Decomposition patterns
  (Identify and Size Components, Gather Common Domain Components,
  Flatten Components, Determine Component Dependencies, Create Component
  Domains, Create Domain Services) plus the Elephant Migration
  Anti-Pattern warning. Use when starting a monolith-to-services
  migration, picking a decomposition approach, sequencing decomposition
  steps, or recovering from a stuck decomposition. Triggers - "how do
  we break up the monolith", "monolith to microservices", "Component-Based
  Decomposition", "Tactical Forking", "Elephant Migration", "strangler
  fig vs", "where do we start", "decomposition order", "namespace
  analysis", "extract first service", "Mikado method". Produces a
  decomposition plan with ADRs per pattern step. Step-by-step workflow.
---

# Service and Data Decomposition

You walk architects through choosing and executing a **decomposition approach** from *Software Architecture: The Hard Parts* (Ch 4–5). The book offers two top-level approaches and a sequenced 6-pattern procedure for one of them. Most teams that fail at monolith-to-microservices fail by skipping this method.

This is a **workflow** skill. Phase 1 picks the approach; Phase 2 (Component-Based) or 2' (Tactical Forking) executes it. Each pattern application produces an ADR.

Pattern definitions are in *Software Architecture: The Hard Parts* (Ford et al., O'Reilly 2021): "Decomposition Patterns" and "Component-Based Decomposition" frameworks.

---

## Related

- **Related skills**
  - `architectural-quanta-and-modularity` — **load first** if it's not yet clear that decomposition is justified
  - `data-ownership-and-distributed-data` — runs in parallel; data decomposition happens alongside service decomposition (Ch 6 sequences with Ch 5)
  - `service-granularity-forces` — the "how big" question, applied per emerging service
  - `software-modularity-principles` — internal-to-service organization once services exist
- **Related references**
  - *The Hard Parts*, "Decomposition Patterns" framework
  - *The Hard Parts*, "Component-Based Decomposition" framework
  - *The Hard Parts*, Sysops Squad worked example, Ch. 4 (Choosing a Decomposition Approach)

---

## Contract for this skill

Two phases:
- **Phase 1** (~10 min) — pick Component-Based or Tactical Forking
- **Phase 2** (weeks to months — apply iteratively) — execute the chosen approach

Don't try to run Phase 2 in one session. The book is explicit that decomposition is a sustained effort. This skill marches the user through the *first iteration* and produces the first ADR; subsequent iterations re-invoke the skill.

---

# Phase 1 — Pick the Decomposition Approach

## Step 1.1 — Codebase analyzability test

The choice depends on whether the codebase is analyzable for components. Test:

| Question | Answer |
|---|---|
| Does the codebase have identifiable namespaces / packages / modules? | yes / no |
| Can you trace dependency boundaries (afferent / efferent coupling)? | yes / no |
| Does the codebase compile and pass tests? | yes / no |
| Can a static analysis tool produce a meaningful dependency graph? | yes / no |

3–4 yes → **Component-Based Decomposition**
0–2 yes → **Tactical Forking**

The book is explicit: most teams reflexively pick Component-Based even when their codebase is too tangled. **Force the test.** If the codebase is genuinely a big ball of mud, Tactical Forking is the right call.

## Step 1.2 — Avoid the Elephant Migration Anti-Pattern

The most common decomposition failure: extracting one service at a time from a tangled monolith *without* a structured approach. Produces a distributed big ball of mud.

If the team is already attempting ad-hoc service extraction, **stop them**. Apply Step 1.1, pick an approach, execute it.

## Step 1.3 — Write the approach ADR

```
ADR-NNN: Decomposition approach for <system>

Context:
  Codebase analyzability test: <result>
  Modularity drivers broken (from architectural-quanta skill): <list>

Decision:
  Use <Component-Based Decomposition | Tactical Forking>.

Consequences:
  Positive: <…>
  Negative: <…>
  Mitigations: <…>
```

The Sysops Squad team writes this ADR in Ch 4 (ADR: Migration Using the Component-Based Decomposition Approach) and uses it as the spine of the entire migration.

---

# Phase 2 — Component-Based Decomposition (when applicable)

Six sequenced patterns. Each produces an ADR. **Apply in order.** Don't skip steps.

## Pattern 1 — Identify and Size Components

Inventory the components in the codebase. For each, measure:

- **Statements of code** (preferred over line count — robust to formatting)
- **Number of classes / files**
- **Domain concept** the component represents

```
Component                    SoC    Files   Domain
---------------------------- -----  ------  -------------------
ticket.entry                 1450   38      ticket creation
ticket.assignment            2200   54      expert matching
ticket.notification          800    21      customer + expert notify
billing.processing           3100   72      billing logic
billing.history              900    24      billing display
…
```

### Prune the outliers

- Components >2× average size → candidates to split
- Components <0.2× average size → candidates to merge

Output: a sized component inventory. Write an ADR with the sizing decisions (which to split, which to merge).

## Pattern 2 — Gather Common Domain Components

Find code that's shared across components. For each shared piece, decide:

| Option | When |
|---|---|
| Replicate per component | Small, stable, low security risk |
| Lift to a shared library | Utility code, mature, low coupling |
| Lift to a shared service | (Rare) data-heavy operations needing consistency |
| Promote to a sidecar | Operational cross-cutting concerns |

The book maps this to the four **reuse patterns** (Ch 8). See `code-reuse-in-distributed-systems` skill.

Output: an explicit shared-code disposition. ADR per non-trivial decision.

## Pattern 3 — Flatten Components

Eliminate orphan namespaces — namespaces with only sub-namespaces and no concrete components.

```
Before:                     After:
com.app.ticket              com.app.ticket
  .entry                      .entry
    .impl                     .assignment
  .assignment                 .notification
    .impl
  .notification
    .impl
```

The flat tree is easier to reason about and easier to extract from. Output: a flat component tree.

## Pattern 4 — Determine Component Dependencies

Build the dependency graph. Use static analysis tools (jdepend for JVM, dependency-cruiser for JS, pylint for Python, etc.) — don't do this by hand.

For each component, compute:

- **Afferent coupling (Ca)** — incoming dependencies
- **Efferent coupling (Ce)** — outgoing dependencies
- **Instability (I)** — Ce / (Ca + Ce). 0 = stable, 1 = unstable.

### Identify extraction blockers

- Components with high afferent coupling (many things depend on them) — extract last
- Components with high efferent coupling and low afferent — extract first
- Cyclic dependencies — must be broken before extraction

Output: a directed dependency graph + extraction order.

## Pattern 5 — Create Component Domains

Group components into logical domains. Each domain becomes a candidate service.

```
Domain          Components
--------------  --------------------------------------------
Customer        customer.profile, customer.preferences
Ticket          ticket.entry, ticket.assignment, ticket.lifecycle
Expert          expert.profile, expert.availability
Billing         billing.processing, billing.history
Reporting       reporting.financial, reporting.operational
Survey          survey.delivery, survey.collection
```

Domain grouping is informed by:
- Bounded contexts (DDD)
- Modularity drivers (which driver is broken for which domains)
- Team structure (Conway's Law — *not* the driver, but the constraint)

Output: domain → components map. ADR per domain.

## Pattern 6 — Create Domain Services

Promote each domain to a service when its dependencies are clean (no cycles, low cross-domain coupling).

**Order matters.** Promote leaf domains (few dependencies on other domains) first. Promote highly-depended-on domains last.

Per-domain service creation includes:
1. Extract the code into its own deployable
2. Extract the data into its own schema (load `data-ownership-and-distributed-data` skill)
3. Replace internal calls with API calls / events
4. Add operational concerns (load `code-reuse-in-distributed-systems` skill for sidecar)
5. Define the contract (load `service-contracts-and-coupling` skill)

Each domain service promotion is a multi-week activity. **Don't promote in parallel** — finish one, validate it, start the next.

Output: a sequenced service rollout plan.

---

# Phase 2' — Tactical Forking (when the codebase is too tangled)

If the codebase fails the analyzability test, use Tactical Forking instead.

## Step T.1 — Set up team forks

For each team that owns a piece of the eventual decomposed system, **fork the entire codebase**. Yes, the whole thing.

```
monolith-main/             ← original, frozen
├── monolith-team-ticket/  ← fork 1
├── monolith-team-billing/ ← fork 2
└── monolith-team-expert/  ← fork 3
```

## Step T.2 — Delete what doesn't belong

Each team **deletes** code from their fork that isn't their concern. They don't refactor. They don't reorganize. They delete.

After deletion, each fork is the team's service (still bigger than needed, but bounded).

## Step T.3 — Stabilize each fork

Each team gets their fork compiling and passing tests independently. Stub out cross-fork calls.

## Step T.4 — Replace stubs with real cross-service calls

Build the inter-service contracts (load `service-contracts-and-coupling` skill). Replace stubs with real calls.

## Step T.5 — Continue refactoring inside forks

Each fork now has structured technical debt instead of unstructured. Apply Component-Based Decomposition patterns *inside each fork* over time.

### Tactical Forking trade-offs

| Pro | Con |
|---|---|
| Fast: weeks instead of months | Crude: produces oversized services |
| Survives genuinely-tangled codebases | Lots of deletion work |
| Each team's fork is independently workable | Cross-fork integration is hard |
| Forces immediate ownership boundaries | Code duplication during transition |

Use when Component-Based fails the analyzability test. Otherwise prefer Component-Based.

---

## Common failure modes (call these out when you see them)

### "We'll extract the first service and learn"

Without an approach, this is the Elephant Migration Anti-Pattern. Pick Component-Based or Tactical Forking *first*.

### "We tried Component-Based but got stuck on Pattern 4"

Stuck on Pattern 4 (dependency mapping) usually means the codebase fails the analyzability test more than the team realized. Reconsider Tactical Forking.

### "We tried Tactical Forking but ended up with three monoliths"

That's actually a partial success — three monoliths is better than one. Now apply Component-Based *inside each fork* over time.

### "The strangler-fig pattern is enough"

Strangler-fig (Fowler) is an *extraction tactic*, not a decomposition approach. It tells you how to route traffic away from the monolith as you extract. It doesn't tell you *what to extract* or *in what order*. Use this skill's patterns to drive the decomposition; use strangler-fig (or Branch-by-Abstraction) as the runtime mechanic.

### "We're decomposing without the database team"

The book's strongest warning (Ch 6): bring the database team in at Pattern 5–6. Without them, you'll re-decompose later when the data layer doesn't fit your service boundaries. Load `data-ownership-and-distributed-data` skill in parallel.

### "We're extracting services by team boundary"

Conway's Law. Often the right answer; sometimes the wrong one. Check whether the bounded contexts match the team boundaries. If not, you're either reorganizing teams or accepting suboptimal services. Surface the choice.

---

## When to deviate from this skill

- **Pure rewrite (not migration)** — different problem. You're not decomposing an existing system; you're designing a new one. Use greenfield architecture skills.
- **Modular monolith target** — if the team wants modularity within the monolith (not microservices), apply Patterns 1–5 but stop before Pattern 6 (don't promote to services). The internal structure is the win.
- **Library / framework decomposition** — different vocabulary (semver, public API surface) applies more than this skill's service-centric vocabulary.

---

## Worked example

The Sysops Squad case study walks the full 6-pattern Component-Based Decomposition across Chapters 4–5. Each pattern produces an ADR. By end of Ch 5, the team has:

- 6 named component domains (Customer, Ticket, Expert, Billing, Reporting, Survey)
- A flat component tree
- A dependency graph with extraction order
- ADRs for sizing decisions, shared-code dispositions, domain assignments

See *The Hard Parts*, Sysops Squad worked example, Ch. 5 (Multiple Segments — One Per Pattern), for the full walkthrough.
