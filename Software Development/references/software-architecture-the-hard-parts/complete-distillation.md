# Complete Distillation: Software Architecture — The Hard Parts

**Source:** *Software Architecture: The Hard Parts — Modern Trade-Off Analyses for Distributed Architectures* by Neal Ford, Mark Richards, Pramod Sadalage & Zhamak Dehghani (O'Reilly, 2021)
**Distilled:** 2026-05-12
**Domain:** Distributed Architecture, Trade-Off Analysis, Service & Data Decomposition
**Pages processed:** 334 (full book)

This file is the all-in-one view. Use it when you want the whole picture rather than navigating skills + framework anchors. Use `frameworks.md` when you need a specific pattern catalog. Use `sysops-squad-worked-example.md` when you need a worked example.

---

## Executive Summary

Ford, Richards, Sadalage & Dehghani's *The Hard Parts* is the sequel to *Fundamentals of Software Architecture* — same Richards & Ford voice, joined by Sadalage (database/agile thought leader) and Dehghani (data mesh originator). Where *Fundamentals* teaches the architect's mindset, *The Hard Parts* teaches what to do when that mindset meets a real distributed system mid-decomposition: services that share data, transactions that span boundaries, contracts that bind services together, granularity that nobody can defend.

The book's central thesis is in its subtitle: **modern trade-off analyses for distributed architectures**. Not patterns to copy. Not best practices to apply. A replicable method for analyzing trade-offs in the specific situation in front of you, because the authors are explicit that **no best practices exist** for the problems this book covers (Chapter 1's opening line). The "hard parts" are problems where every solution has costs, and the architect's job is to make those costs visible.

The book is built around a running case study — the **Sysops Squad** — a fictional tech support team trying to decompose a monolithic ticketing application. Every chapter ends with a "Sysops Squad Saga" segment where the team applies that chapter's frameworks to a concrete decision and ratifies an ADR. The case study is not garnish; it's the pedagogy. Anyone trying to extract value from the book without engaging the case study is reading a recipe book instead of cooking.

---

## The Big Takeaways

1. **There are no best practices for the hard parts.** If a solution were universal, conferences wouldn't talk about it. The book trains the analysis method, not the answer.

2. **Coupling is the master concept.** Architectural quanta, static coupling, dynamic coupling, semantic coupling, stamp coupling, contract coupling — every "hard part" reduces to coupling reasoning.

3. **The architectural quantum is the unit of measurement.** An independently deployable artifact with high functional cohesion + high static coupling internally + synchronous dynamic coupling at runtime. The quantum is what you decompose, scale, and reason about — not "the service."

4. **Static coupling vs dynamic coupling are different problems.** Static = wiring (what does this service depend on to bootstrap?). Dynamic = communication (what does it talk to at runtime?). Most teams conflate them, then make decisions based on the wrong one.

5. **The 8 transactional sagas form a complete taxonomy.** Communication × consistency × coordination = 8 patterns, from Epic Saga (sync/atomic/orchestrated, very high coupling) to Anthology Saga (async/eventual/choreographed, very low coupling). Pick by trade-offs, name by the catalog.

6. **Data ownership precedes data access.** Decide who *owns* the data (single / joint / common) before deciding how others *read* it (inter-service communication / column schema replication / replicated cache / data domain).

7. **Granularity has named forces.** Disintegrators push toward smaller services (independent deployment, fault isolation, scalability differential). Integrators push toward larger (database transactions, data dependency, workflow coupling). The architect's job is to name the forces and weigh them, not to pick a target size up front.

8. **Reuse in distributed systems is harder than reuse in monoliths.** Four named patterns — code replication, shared library, shared service, sidecar/service mesh — each with different deployment / change cadence / coupling implications. Almost never use shared service for domain code; almost always use sidecar for cross-cutting operational concerns.

9. **Contracts are the deepest coupling decision.** Strict contracts (Protobuf, GraphQL schemas, OpenAPI-bound) catch errors early but bind tightly. Loose contracts (JSON without schema, name-value pairs) survive change but defer error detection. Stamp coupling — passing more data than needed — is the most common contract anti-pattern.

10. **Build your own trade-off analysis.** Chapter 15 is the meta-skill: surface entangled dimensions, analyze how they're coupled, assess impact of change, write the ADR. Repeat for every decision worth defending. *Discipline* is the word the book uses; it's what separates "architecture" from "luck."

---

## Skills Derived From This Book

Located in `Software Development/`. Each is a self-contained action-focused skill that links back to specific sections of `frameworks.md`.

| Skill | When to invoke | Source coverage |
|---|---|---|
| `distributed-workflows-and-sagas` | Choosing between Epic / Phone Tag / Fairy Tale / Time Travel / Fantasy Fiction / Horror / Parallel / Anthology Saga; designing distributed transactions | Ch 11–12 |
| `trade-off-analysis-method` | Making a defensible architecture decision; structuring an ADR with explicit trade-off scoring | Ch 1, Ch 2, Ch 15 |
| `data-ownership-and-distributed-data` | Deciding ownership across services; choosing a data access pattern for cross-service queries | Ch 6, Ch 9, Ch 10 |
| `service-contracts-and-coupling` | Choosing strict vs loose contracts; reasoning about stamp coupling and semantic coupling | Ch 13 |
| `architectural-quanta-and-modularity` | Defining the unit of independent deployment; assessing modularity drivers | Ch 1–3 |
| `service-and-data-decomposition` | Breaking a monolith apart; choosing between Component-Based and Tactical Forking | Ch 4–5 |
| `service-granularity-forces` | Sizing a service; weighing disintegrators against integrators | Ch 7 |
| `code-reuse-in-distributed-systems` | Choosing replicated code / shared lib / shared service / sidecar | Ch 8 |

Existing skills augmented with Hard Parts content:
- `architecture-characteristics-and-tradeoffs` — Build-Your-Own method appendix
- `architecture-styles-monolithic-and-distributed` — quantum vocabulary, distributed monolith trap
- `distributed-system-patterns` — replaced generic Saga blurb with the 8-saga catalog
- `scalable-database-design-and-sharding` — Ch 6 operational-data decomposition specifics
- `api-design-and-evolution` — strict/loose contract trade-off, stamp coupling
- `software-modularity-principles` — modularity drivers (Ch 3)
- `eventual-consistency-mechanics` — cross-link to sagas (business-level EC vs storage-level EC)

---

## Part I — Pulling Things Apart

Part I deals with static structure: how the system is wired before runtime begins. The four-chapter arc is *coupling vocabulary → modularity drivers → decomposition method → component patterns → data decomposition → granularity*. The Sysops Squad team finishes Part I with a decomposed service catalog and a decomposed data model, but the services don't talk to each other yet.

### Chapter 1 — What Happens When There Are No "Best Practices"?

The book's thesis chapter. Best practices exist for solved problems. The hard parts are not solved. Therefore the book teaches a *method* (trade-off analysis), not answers. Introduces:

- **The Sysops Squad case study** — a tech support ticketing monolith owned by Penultimate Electronics. Customer support tickets are routed to experts who travel to customer sites. The team: Addison & Austen (architects), Logan (senior architect mentor), Skyler & Taylen (developers), Dana (DBA), Parker (PM), Bailey (business sponsor).
- **Architecture decision records (ADRs)** as the documentation discipline. Every significant decision in the book ends with an ADR template: Context · Decision · Consequences.
- **Architectural fitness functions** as the governance discipline. Automated tests that protect the architectural characteristics you care about, run continuously.

### Chapter 2 — Discerning Coupling in Software Architecture

Introduces the master concept of the book.

- **Architectural quantum** = an independently deployable artifact with high functional cohesion + high static coupling internally + synchronous dynamic coupling at runtime. A microservice that doesn't share a database is typically a quantum. A microservices system where all services share a DB is *one* quantum, not many.
- **Static coupling** = the wiring required to bootstrap. OS, container, library, framework, DB, message broker, integration point. Visible in a static-coupling diagram.
- **Dynamic coupling** = communication at runtime. Has three dimensions:
  - **Communication**: synchronous or asynchronous
  - **Consistency**: atomic or eventual
  - **Coordination**: orchestrated or choreographed
- **Table 2-1 — the 8-saga matrix.** The combinations of (sync/async) × (atomic/eventual) × (orchestrated/choreographed) produce 8 named patterns, ranked by coupling strength (Epic Saga = very high → Anthology Saga = very low). This is the spine of the entire book.
- **3-step trade-off analysis method** (introduced here, refined in Ch 15):
  1. Find what parts are entangled together
  2. Analyze how they are coupled to one another
  3. Assess trade-offs by determining the impact of change to interdependent systems

### Chapter 3 — Architectural Modularity

Why decompose at all? The book names six **modularity drivers** that justify the cost:

- Maintainability
- Testability
- Deployability
- Scalability / Elasticity
- Availability / Fault Tolerance

You don't decompose because microservices are fashionable. You decompose because at least one of these drivers is broken in your current architecture badly enough to pay the cost. If none are broken, the answer is: don't decompose.

### Chapter 4 — Architectural Decomposition

Two top-level approaches based on the codebase's analyzability:

- **Component-Based Decomposition (Ch 5)** — when the codebase has identifiable logical components (namespaces, packages, modules). Iterative, structured, low-risk, preserves what already works.
- **Tactical Forking** — when the codebase is too tangled to analyze. Replicate the entire codebase per team, then *delete* what doesn't belong. Crude, fast, suited to "big ball of mud."

Warns of the **Elephant Migration Anti-Pattern** — extracting service by service from a tangled monolith without structure produces a *distributed* big ball of mud.

### Chapter 5 — Component-Based Decomposition Patterns

A sequence of patterns to apply in order, each producing an ADR:

1. **Identify and Size Components** — find components, measure them (statements of code), prune the outliers
2. **Gather Common Domain Components** — find shared logic, decide replicate vs lift-to-shared
3. **Flatten Components** — move toward a flat component tree, eliminating orphan namespaces
4. **Determine Component Dependencies** — afferent / efferent coupling, draw the dep graph
5. **Create Component Domains** — group components into logical domains
6. **Create Domain Services** — promote domains to services when ready

The decomposition is gradual, evidence-based, and ADR-backed at each step.

### Chapter 6 — Pulling Apart Operational Data

Decomposing the data model is harder than decomposing the code. Introduces:

- **Data Disintegrators** — change control, scalability differential, fault tolerance, archival, multi-region distribution
- **Data Integrators** — referential integrity, ACID transactions, joined queries, materialized views
- **Data Domain** — a coupled set of tables/views/FKs/stored procs that move together. The unit of data decomposition.
- **5-step database decomposition process** — analyze, create data domains, assign tables to domains, refactor cross-domain dependencies, separate schemas/databases

The DBA character (Dana) finally joins the decomposition decisions here. The book is explicit: decomposing data without the database team is a route to disaster.

### Chapter 7 — Service Granularity

The "how big should a service be?" question. The book refuses to give a size. Instead it names:

- **Granularity Disintegrators** — service scope (multiple unrelated responsibilities), code volatility (different change cadences), scalability differential, fault tolerance, security, extensibility
- **Granularity Integrators** — database transactions, data dependency, workflow coupling (chatty service-to-service calls)

The architect's job is to name which forces are present in this situation and weigh them. Granularity is *derived*, not chosen.

---

## Part II — Putting Things Back Together

Part I dismantled the monolith. Part II is about what happens when the services need to cooperate again, which is most of the time. The arc: *reuse → data ownership → data access → workflows → sagas → contracts → analytical data → build your own*.

### Chapter 8 — Reuse Patterns

Four named patterns with explicit trade-offs:

- **Replicated Code** — copy the code into each service. Simple, no runtime coupling. Drift becomes the cost. Best for: code that's small + stable + low security risk.
- **Shared Library** — versioned dependency. Common, low coupling at runtime, version skew at build time. Best for: utility code, well-defined functions.
- **Shared Service** — runtime call to a separate service. High runtime coupling, single source of truth. Best for: data-heavy operations that *must* be consistent (rare).
- **Sidecar / Service Mesh** — operational cross-cutting concerns deployed alongside each service. Sidecar holds the operational coupling so the service can hold the domain coupling.

The book's bias: *almost never use shared service for domain reuse*; *almost always use sidecar for operational concerns*.

### Chapter 9 — Data Ownership and Distributed Transactions

Decomposed data must be owned. Three ownership models:

- **Single Ownership** — one service writes a table. Cleanest case. Always preferred.
- **Common Ownership** — many services write the same data. Almost always an anti-pattern. Routes to single ownership or to "data domain" pattern.
- **Joint Ownership** — limited writers (2–3 services) share write access. Sometimes unavoidable. Handle via: table split, data domain, delegate model, or service consolidation.

The chapter is a decision tree. Single ownership first. If joint, name the resolution pattern. If common, reconsider the decomposition.

### Chapter 10 — Distributed Data Access

How services that *don't* own data still read it. Four patterns:

- **Inter-Service Communication** — call the owning service synchronously. Highest runtime coupling. Simplest data freshness.
- **Column Schema Replication** — replicate the columns into the consuming service's DB on change. Reads are local; writes need replication. Stale-read tolerance required.
- **Replicated Cache** — in-memory replicated cache (Apache Ignite, Hazelcast). Fast reads, replication overhead, eventual freshness.
- **Data Domain** — sharing services own a *shared* data domain. Two services, one DB schema, careful joint-ownership rules. Use sparingly.

Pick by: read volume, freshness tolerance, data size, fault tolerance need.

### Chapter 11 — Managing Distributed Workflows

When a transaction spans multiple services, who runs it? Two top-level styles:

- **Orchestration** — a single orchestrator service knows the workflow, calls each step. State centralized. Easier to reason about. Single point of failure / coupling.
- **Choreography** — services emit events, others react. No orchestrator. State decentralized. Hard to reason about above ~4 participants.

Key concept introduced here: **semantic coupling** — the inherent coupling in the problem domain itself. Implementation can't reduce it; implementation can only express it well or badly. If the problem requires 5 services to coordinate, no architecture removes that requirement.

Also introduced: **stamp coupling for workflow management** — passing the entire workflow state through each step. Common in choreography. Trade-off: low semantic coupling but high data-volume coupling.

### Chapter 12 — Transactional Sagas

The heart of Part II. Re-introduces the 8-saga matrix from Chapter 2 and walks each in detail:

| Pattern | Communication | Consistency | Coordination | Coupling |
|---|---|---|---|---|
| **Epic Saga (sao)** | sync | atomic | orchestrated | very high |
| **Phone Tag Saga (sac)** | sync | atomic | choreographed | high |
| **Fairy Tale Saga (seo)** | sync | eventual | orchestrated | high |
| **Time Travel Saga (sec)** | sync | eventual | choreographed | medium |
| **Fantasy Fiction Saga (aao)** | async | atomic | orchestrated | high |
| **Horror Story (aac)** | async | atomic | choreographed | medium |
| **Parallel Saga (aeo)** | async | eventual | orchestrated | low |
| **Anthology Saga (aec)** | async | eventual | choreographed | very low |

The book's recommendation: most teams should default to Parallel Saga or Anthology Saga (lower coupling) and only escalate when a domain requirement forces atomicity or synchronicity. Epic Saga (the "Saga pattern" most other books describe) is the *worst* default in this taxonomy — highest coupling, hardest to operate, and what teams reach for by reflex.

### Chapter 13 — Contracts

The deepest coupling decision. Two ends of the spectrum:

- **Strict contracts** — Protobuf, Avro schemas, GraphQL types, OpenAPI with schema validation. Compile-time / call-time enforcement. Catches errors early. Brittle to change.
- **Loose contracts** — JSON over HTTP without schema, name-value pairs. Survives change. Defers error detection to runtime.

Plus:

- **Stamp coupling** — passing more data than needed in a contract. Common, usually accidental. Increases dependency surface area.
- **Semantic coupling** — coupling on the *meaning* of fields. Worst kind. Renaming a field can break consumers who depended on the old name's meaning.
- **Consumer-driven contracts (CDC)** — consumers specify the contract; producer tests against it. Spring Cloud Contract, Pact. The book endorses these for cross-team integrations.

### Chapter 14 — Managing Analytical Data

Dehghani's chapter — covers the operational-vs-analytical data divide. Introduces **Data Mesh** as the analytical-data complement to microservices:

- **Data product** — analytical data treated as a product, owned by the domain team
- **Data product quantum (DPQ)** — the analytical-data analog of the architectural quantum
- **Domain ownership of data** — analytical data lives close to the operational data, owned by the same team
- **Federated computational governance** — global policies, local implementation

Marked optional in the INDEX — this chapter is the seed for the `Data Engineering/analytical-data-mesh` skill (deferred to T5).

### Chapter 15 — Build Your Own Trade-Off Analysis

The meta-chapter. Restates and operationalizes the 3-step method from Ch 2:

1. **Find entangled dimensions** — what's coupled to what in this specific decision? Use the static-coupling diagram template the book provides (OS/container deps, transitive deps, persistence deps, integration points, messaging infra).
2. **Analyze coupling** — name the type (static / dynamic / semantic / stamp / contract). Score the strength.
3. **Assess trade-offs** — for each candidate solution, what changes? What downstream impact? Score against the system's chosen architectural characteristics.

Ends with the book's closing line, delivered by Logan to a skeptical exec: *"That's architecture. And as you can see, it works."*

The closing meeting (the retrospective at the start of Ch 15) is the case study's payoff. Read it directly when you need to remind yourself what "good architecture work" looks like in a business context.

---

## Voice & Authority

- **Mark Richards** — 30+ years independent consultant, author of *Fundamentals of Software Architecture* (also distilled in this repo).
- **Neal Ford** — Director / Software Architect at Thoughtworks; co-author of *Building Evolutionary Architectures*. Provides the fitness-function / governance lens.
- **Pramod Sadalage** — Thoughtworks; co-author of *NoSQL Distilled* and *Refactoring Databases*. Provides the data-decomposition rigor in Ch 6, Ch 9, Ch 10.
- **Zhamak Dehghani** — Thoughtworks; originator of **Data Mesh**. Provides Ch 14 (analytical data) and the data-product-quantum vocabulary.

The voice is firm on principles (every decision needs an ADR, every saga has a name, every reuse pattern has explicit trade-offs), hedged on specifics (the book repeatedly refuses to recommend a "default" service size, default contract style, or default saga — every answer is "depends, here's how to decide").

Tone: practitioner-confident, dialogue-heavy via the Sysops Squad case study. The Sysops Squad conversations are the book's best feature — they show *how* an architecture team argues, not just what they conclude.

---

## What This Book Is NOT

- Not a microservices tutorial. Assumes you've already chosen microservices and are dealing with the consequences.
- Not a runtime-resilience book. Circuit breakers, timeouts, bulkheads barely appear. See `microservices-resilience-patterns` skill.
- Not a Kubernetes/operations book. Operational concerns appear only via the Sidecar pattern.
- Not a distributed-systems-theory book. CAP, consensus, gossip do not appear. See `distributed-systems-essentials` and `consensus-and-strong-consistency` skills.
- Not an introductory book. Assumes *Fundamentals of Software Architecture* (or equivalent) as background.

---

## How to Use This Folder

1. **First decision: do I want the whole book, or a specific framework?**
   - Whole book → keep reading this file.
   - Specific framework → open `frameworks.md` and jump to the anchor in INDEX.md.
   - Worked example → `sysops-squad-worked-example.md`.

2. **Second decision: am I making a real decision right now, or just learning?**
   - Real decision → load the relevant skill from `Software Development/` (the SKILL.md will walk you through a workflow).
   - Learning → stay in references.

3. **Third decision: do I need to update something?**
   - If a framework changes → update `frameworks.md` and the relevant skill in the same commit.
   - If a new pattern is added → add an anchor to `frameworks.md`, add a row to INDEX.md, add a row to `HARD_PARTS_MAP.md` at the Software Development root.
