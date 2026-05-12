# Frameworks Catalog — Software Architecture: The Hard Parts

Canonical pattern definitions, matrices, and decision aids from the book. **Skills deep-link to anchors in this file rather than duplicating definitions.** When a framework changes, update it here and the linked skills will read the new version.

Each section has a stable anchor (the heading slug) so external links survive.

---

## Coupling Vocabulary {#coupling-vocabulary}

The master concept of the book. Everything else is a special case.

### Static vs Dynamic Coupling

| Dimension | Definition | Visible in | Lifecycle stage |
|---|---|---|---|
| **Static coupling** | The wiring required for a service to bootstrap. OS, container, library, framework, DB, message broker, integration points. | Static-coupling diagram | Build / deploy time |
| **Dynamic coupling** | Communication between services at runtime. Synchronous / asynchronous calls, message passing, event subscription. | Runtime call graph | Request time |

Most teams conflate them. They are fundamentally different problems with different solutions.

### Dynamic Coupling — Three Dimensions

Dynamic coupling decomposes into three orthogonal axes. Every distributed transaction picks one value on each axis.

| Axis | Values | What it controls |
|---|---|---|
| **Communication** | synchronous / asynchronous | Does the caller wait? |
| **Consistency** | atomic / eventual | Does the system commit all-or-nothing? |
| **Coordination** | orchestrated / choreographed | Is there a central conductor? |

2³ = 8 combinations → the 8 transactional sagas (see [§the-8-transactional-sagas](#the-8-transactional-sagas)).

### Semantic Coupling

The inherent coupling in the problem domain itself. Implementation can't reduce semantic coupling; it can only express it well or badly. If the business requires 5 services to coordinate a workflow, no architecture removes the requirement. (Ch 11.)

### Stamp Coupling

Passing more data than needed across a contract boundary. Common in:
- Workflow management (passing entire workflow state through each step)
- API responses that return full entities when the caller needed two fields
- Event payloads that include unrelated context

Cost: data-volume coupling, hidden dependency on fields the consumer didn't appear to need, change blast radius. (Ch 11, Ch 13.)

### Connascence (carried in from *Fundamentals*)

The book uses connascence vocabulary throughout but doesn't redefine it. See `references/fundamentals-of-software-architecture/frameworks.md` for the full taxonomy. Stronger forms (Value, Identity) live inside services; weaker forms (Name, Type) cross service boundaries.

---

## Architectural Quantum {#architectural-quantum}

The unit of independent deployment, and the unit of trade-off analysis.

### Definition

An architectural quantum has three properties:

1. **Independently deployable artifact** — can be deployed alone without coordination
2. **High functional cohesion** — internal elements serve a single domain purpose
3. **Synchronous dynamic coupling** at runtime forms a quantum boundary — services that *must* be synchronously coupled at runtime belong to the same quantum

### Consequences

- A microservice with its own database is typically one quantum.
- Ten microservices sharing one database are **one quantum**, not ten.
- A user-facing service synchronously calling an auth service is one quantum (or auth is in the quantum).
- An async event-driven system can have many quanta because async coupling doesn't force a quantum boundary.

### Why the quantum matters

It's the unit of:
- **Scale** — quanta scale together
- **Failure** — quanta fail together (under sync coupling)
- **Deployment** — quanta deploy together (under shared state)
- **Decision** — when the book says "trade-off analysis", the unit being analyzed is the quantum

If you can't identify your quanta, your "microservices" are probably a distributed monolith (one quantum, distributed deployment, worst of both worlds).

---

## Modularity Drivers {#modularity-drivers}

Why decompose at all? Six named drivers. If none apply, **don't decompose**. (Ch 3.)

| Driver | What's broken if absent | Decomposition justifies cost when… |
|---|---|---|
| **Maintainability** | Changes ripple unpredictably | Domains change at very different rates |
| **Testability** | Test suite is slow or flaky | Test isolation impossible at current scope |
| **Deployability** | Releases are infrequent / risky | Teams need independent release cadences |
| **Scalability** | One bottleneck drags everything | Components have different load profiles |
| **Availability** | One failure stops everything | Components have different SLOs |
| **Fault Tolerance** | Errors propagate freely | Components have different blast-radius tolerance |

The book is explicit: "we want microservices" is **not** a driver. "Our deployment cadence is blocked by a 2-hour test suite that flakes once a week" is.

---

## Decomposition Patterns {#decomposition-patterns}

Two top-level approaches. The choice depends on whether the codebase is analyzable. (Ch 4.)

### Decision rule

| Codebase state | Approach | Why |
|---|---|---|
| Identifiable logical components (namespaces / packages / modules) | **Component-Based Decomposition** (Ch 5) | Iterative, structured, low-risk, evidence-driven |
| Too tangled to identify components | **Tactical Forking** | Crude but fast — fork the codebase per team, delete what doesn't belong |

### Elephant Migration Anti-Pattern

Extracting service by service from a tangled monolith *without* structure. Produces a distributed big ball of mud — the worst of both worlds. The fix: pick one of the two patterns above and follow it.

---

## Component-Based Decomposition {#component-based-decomposition}

A sequenced 6-pattern procedure. Each pattern produces an ADR. (Ch 5.)

| # | Pattern | Goal | Output |
|---|---|---|---|
| 1 | **Identify and Size Components** | Inventory components, measure them | List with statement-of-code per component |
| 2 | **Gather Common Domain Components** | Find shared logic | Decision: replicate or lift to shared |
| 3 | **Flatten Components** | Eliminate orphan namespaces | Flat component tree |
| 4 | **Determine Component Dependencies** | Map afferent (in) and efferent (out) coupling | Dependency graph |
| 5 | **Create Component Domains** | Group components into logical domains | Domain assignments |
| 6 | **Create Domain Services** | Promote domains to services when ready | Service catalog |

Apply in order. Don't skip steps. Each step's output justifies the next.

### Coupling metrics (Ch 5)

- **Afferent coupling (Ca)** — incoming dependencies
- **Efferent coupling (Ce)** — outgoing dependencies
- **Instability (I)** — Ce / (Ca + Ce). 0 = stable, 1 = unstable.
- **Abstractness (A)** — abstract types / total types

Used to identify components that are too tightly coupled to extract.

---

## Data Decomposition {#data-decomposition}

Decomposing the data model is harder than decomposing the code. (Ch 6.)

### Data Disintegrators — forces toward separation

| Disintegrator | When it pushes for separation |
|---|---|
| Change control | Different tables change at very different cadences |
| Connection management | Connection pool exhaustion |
| Scalability differential | One table dwarfs the others |
| Fault tolerance | One table's outage shouldn't affect others |
| Archival | Different retention requirements |
| Multi-region distribution | Latency requires geographic distribution |

### Data Integrators — forces toward staying together

| Integrator | When it pushes against separation |
|---|---|
| Referential integrity (FKs) | DB-level enforced foreign keys |
| ACID transactions | Atomic multi-table updates required |
| Joined queries | Frequent multi-table joins |
| Materialized views | Pre-computed cross-table aggregations |

### Data Domain

A **data domain** = a coupled set of tables, views, FKs, and stored procedures that *move together*. The unit of data decomposition.

### 5-Step Database Decomposition Process

1. **Analyze and create data domains** — group artifacts into proposed domains
2. **Assign tables to data domains** — explicit table → domain map
3. **Separate database connections** — one connection per domain
4. **Move schemas to separate schemas** — physical schema separation
5. **Move schemas to separate database servers** — full physical separation (last step)

Crucial: get the DBA team into the decomposition decisions early. (The Sysops Squad case study makes this point explicitly in Ch 6.)

---

## Granularity Forces {#granularity-forces}

"How big should a service be?" The book refuses to give a size. It gives the forces. (Ch 7.)

### Granularity Disintegrators — push toward smaller services

| Force | When it applies |
|---|---|
| Service scope and function | Service does multiple unrelated things |
| Code volatility | Parts of the service change at very different rates |
| Scalability and throughput | Parts need very different scaling |
| Fault tolerance | Failures in one part shouldn't kill others |
| Security | Different parts have different access requirements |
| Extensibility | Frequent additions of new capabilities |

### Granularity Integrators — push toward larger services

| Force | When it applies |
|---|---|
| Database transactions | Atomic multi-step updates required |
| Data dependency | One service can't function without another's data |
| Workflow coupling | Chatty service-to-service calls degrade performance |
| Shared code | Significant logic duplicated across services |

### Decision procedure

1. List all disintegrators present
2. List all integrators present
3. Weigh against the system's architectural characteristics
4. Land on granularity
5. Write the ADR

Granularity is *derived*, not chosen.

---

## Reuse Patterns {#reuse-patterns}

Four named patterns for code reuse in distributed systems. (Ch 8.)

### Pattern catalog

| Pattern | What it is | Coupling | Best for |
|---|---|---|---|
| **Replicated Code** | Copy the code into each service | None at runtime; drift over time | Small, stable, low-security utility code |
| **Shared Library** | Versioned dependency, statically linked or imported | Low runtime; version-skew at build | Utility code, well-defined functions |
| **Shared Service** | Runtime call to a separate service | High runtime | Data-heavy operations that *must* be consistent (rare) |
| **Sidecar / Service Mesh** | Operational cross-cutting concerns deployed alongside | High operational, zero domain | Monitoring, logging, security, mTLS |

### Defaults the book endorses

- **Sidecar / Service Mesh** for operational concerns — almost always
- **Shared Library** for utility code — common, well-trodden
- **Replicated Code** for small/stable code — under-used, often better than people think
- **Shared Service** for domain reuse — almost never

### Trade-offs (Sidecar)

| Pro | Con |
|---|---|
| Consistent operational tooling across services | Sidecar can grow in scope and become its own coupling |
| Decouples domain code from operational code | Adds deployment complexity |
| Enables service mesh patterns | Requires orchestration platform (Kubernetes typical) |

---

## Data Ownership Patterns {#data-ownership-patterns}

Who *writes* what data. (Ch 9.)

### The three ownership models

| Model | Definition | When to use | Anti-pattern? |
|---|---|---|---|
| **Single Ownership** | One service writes a table | Always preferred when possible | No — this is the goal |
| **Joint Ownership** | Limited writers (2–3 services) share write access | When write access is genuinely shared | Acceptable with resolution |
| **Common Ownership** | Many services write the same data | Reconsider decomposition first | Yes — almost always |

### Joint-ownership resolution patterns

When joint ownership is unavoidable, the book offers four resolution patterns:

| Resolution | Mechanism | Trade-off |
|---|---|---|
| **Table Split** | Split the shared table by columns | Increases data domain count |
| **Data Domain** | Two services share a data domain explicitly | Acknowledges the joint ownership; doesn't fix it |
| **Delegate** | One service is the writer; others request via API | Routes back to single ownership at the cost of latency |
| **Service Consolidation** | Merge the joint owners into one service | Last resort; loses decomposition benefit |

### Decision tree

```
Who writes this data?
├── One service              → Single Ownership
├── 2-3 services             → Joint Ownership → pick a resolution pattern
└── Many services            → Common Ownership → reconsider decomposition
```

---

## Data Access Patterns {#data-access-patterns}

Once ownership is decided, how do *non-owners* read the data? (Ch 10.)

### Four named patterns

| Pattern | Mechanism | Read latency | Freshness | Coupling |
|---|---|---|---|---|
| **Inter-Service Communication** | Sync call to owning service | Network RTT | Always fresh | Highest runtime |
| **Column Schema Replication** | Owner replicates columns into consumer's DB on change | Local | Eventual | Moderate (data) |
| **Replicated Cache** | In-memory replicated cache (Apache Ignite, Hazelcast) | Local | Eventual (cache lag) | Moderate (infra) |
| **Data Domain** | Two services share a data domain | Local (cross-service query) | Always fresh | Couples the two services |

### Selection matrix

| If you need… | Choose |
|---|---|
| Always-fresh data, low read volume | Inter-Service Communication |
| High read volume, stale-read tolerance | Column Schema Replication |
| Reference data read by many services | Replicated Cache |
| Two services that genuinely co-evolve | Data Domain |

The book explicitly notes: **Data Domain is a last resort.** Use it when joint ownership is real and stable.

---

## Workflow Coordination {#workflow-coordination}

Transactions that span multiple services. (Ch 11.)

### Orchestration

| Property | Detail |
|---|---|
| State location | Centralized in orchestrator |
| Reasoning | Easy — one place to look |
| Failure handling | Easy — orchestrator implements compensation |
| Coupling | High — orchestrator must know all services |
| Scale | Bottleneck through orchestrator |
| Best for | Workflows >4 participants, complex compensation logic |

### Choreography

| Property | Detail |
|---|---|
| State location | Decentralized — each service holds its part |
| Reasoning | Hard above 4 participants |
| Failure handling | Hard — distributed compensation |
| Coupling | Low — services know only their immediate events |
| Scale | Linear; no central bottleneck |
| Best for | Workflows ≤4 participants, simple flows |

### Combined with consistency

Orchestration × Atomic = strong consistency at cost of coupling
Orchestration × Eventual = weaker consistency, same coupling, slightly easier ops
Choreography × Atomic = rarely viable
Choreography × Eventual = the "modern microservices default" the book recommends

### Stamp coupling for workflow management

Passing the entire workflow state through each step. Trade-off:
- Pro: low semantic coupling between services
- Con: data-volume coupling, hidden field dependencies, debugging difficulty

---

## The 8 Transactional Sagas {#the-8-transactional-sagas}

The full taxonomy. Communication × Consistency × Coordination = 8 named patterns. The single biggest contribution of this book. (Ch 12.)

### The matrix

| Pattern | Communication | Consistency | Coordination | Coupling |
|---|---|---|---|---|
| **Epic Saga (sao)** | synchronous | atomic | orchestrated | very high |
| **Phone Tag Saga (sac)** | synchronous | atomic | choreographed | high |
| **Fairy Tale Saga (seo)** | synchronous | eventual | orchestrated | high |
| **Time Travel Saga (sec)** | synchronous | eventual | choreographed | medium |
| **Fantasy Fiction Saga (aao)** | asynchronous | atomic | orchestrated | high |
| **Horror Story (aac)** | asynchronous | atomic | choreographed | medium |
| **Parallel Saga (aeo)** | asynchronous | eventual | orchestrated | low |
| **Anthology Saga (aec)** | asynchronous | eventual | choreographed | very low |

Three-letter codes: (s|a) communication, (a|e) consistency, (o|c) coordination.

### One-line shape of each

- **Epic Saga (sao)** — orchestrator calls services sync, holds atomic transaction across all; if any fail, orchestrator commands rollback. This is the "Saga pattern" most other books describe. Highest coupling. Use only when the domain demands it.
- **Phone Tag Saga (sac)** — services call each other in a chain synchronously; atomic state managed via two-phase or explicit compensation. Very brittle.
- **Fairy Tale Saga (seo)** — orchestrator calls sync but consistency is eventual; orchestrator coordinates eventual reconciliation. Useful when sync calls are needed but atomic isn't.
- **Time Travel Saga (sec)** — services call each other sync, consistency is eventual, no orchestrator. Hardest to reason about given the constraint mix.
- **Fantasy Fiction Saga (aao)** — async messages, atomic outcomes, orchestrator. Rare; requires distributed transaction across async messaging.
- **Horror Story (aac)** — async messages, atomic, choreographed. The name says it: rarely the right answer.
- **Parallel Saga (aeo)** — async messages, eventual consistency, orchestrator. Modern default for complex workflows.
- **Anthology Saga (aec)** — async messages, eventual consistency, choreographed. Lowest coupling. Modern default for simple workflows.

### What teams reach for vs what they should

- **Reflex:** Epic Saga (because it's just called "Saga" in most other materials)
- **Recommendation:** start at Anthology or Parallel; only escalate to higher-coupling patterns when a domain requirement forces it

---

## Saga Selection Matrix {#saga-selection-matrix}

Use this when picking a saga pattern.

### Step 1 — Pin the axes from domain requirements

| Question | If Yes | If No |
|---|---|---|
| Does the caller need an immediate response? | sync | async |
| Must the entire transaction commit or fail atomically? | atomic | eventual |
| Will the workflow exceed 4 participants? | orchestrated | choreographed-OK |

### Step 2 — Land on the cell

Use the three answers as a 3-bit address into the 8-saga matrix above.

### Step 3 — Evaluate the chosen pattern

Score the selected saga against:
- Operational complexity (can the team run it?)
- Failure modes (what compensation logic is needed?)
- Coupling strength (does it create a quantum boundary you don't want?)
- Performance (does sync introduce latency you can't afford?)

### Step 4 — Reconsider

If any score is poor, walk back to Step 1 and ask whether the axis answer is *actually* forced by the domain, or whether the team is over-constraining. Most teams pick "atomic" when "eventual" would work; most pick "sync" when "async" would be fine.

### Step 5 — Write the ADR

Decision: chose <pattern> because <axis answers + domain reason>.
Consequences: <operational + coupling + performance trade-offs>.

---

## Contracts {#contracts}

The deepest coupling decision. (Ch 13.)

### Strict vs Loose Spectrum

| Property | Strict (Protobuf, Avro, GraphQL, OpenAPI-validated) | Loose (raw JSON, name-value pairs) |
|---|---|---|
| Error detection | Compile-time / call-time | Runtime |
| Change tolerance | Low — breaking changes break consumers | High — consumers ignore unknown fields |
| Versioning | Schema-versioning required | Field-additive often sufficient |
| Tooling | Mature (code gen, validators) | Manual |
| Best for | Internal cross-team APIs | Public APIs, evolving contracts |

### Stamp Coupling (the most common anti-pattern)

Passing more data than needed in a contract. Examples:
- API returns full entity when caller needs two fields
- Event payload includes upstream context the consumer doesn't process
- Workflow state passed through every step

Cost: change blast radius, hidden dependencies, larger surface area.

Mitigation: design contracts to fit the consumer, not to dump the producer's state.

### Semantic Coupling

Coupling on the *meaning* of fields, not their names. Renaming a field doesn't break the consumer; redefining its meaning does. Hardest coupling to detect; hardest to fix.

### Consumer-Driven Contracts (CDC)

Consumer specifies what they need; producer tests against it. Tools: Pact, Spring Cloud Contract.

The book endorses CDC for cross-team integrations because it forces semantic agreement to the surface — the consumer's expectations become testable artifacts the producer can run in CI.

---

## Analytical Data {#analytical-data}

Dehghani's chapter — operational-vs-analytical data divide, and **Data Mesh** as the analytical-data complement to microservices. (Ch 14.)

### Operational vs Analytical Data

| Operational | Analytical |
|---|---|
| Powers transactions | Powers reporting / ML / decisions |
| Latency-sensitive | Throughput-sensitive |
| Owned by service team | Often owned by central data team (legacy) |
| Hard Parts says: keep here | Hard Parts says: bring this back to service team |

### Data Mesh principles

1. **Domain ownership of data** — analytical data stays with the team that owns the operational data
2. **Data as a product** — analytical data treated with product discipline (quality, SLAs, discoverability)
3. **Self-serve data platform** — central platform team provides tooling, not ownership
4. **Federated computational governance** — global policies, local implementation

### Data Product Quantum (DPQ)

The analytical-data analog of the architectural quantum. A DPQ:
- Owns its analytical data
- Exposes the data via well-defined contracts (often async, often event-streamed)
- Is independently deployable
- Has product-level SLAs

The DPQ lives next to the service quantum and is owned by the same team. (Reference: full Data Mesh treatment in Dehghani's separate book *Data Mesh: Delivering Data-Driven Value at Scale*; this chapter is a primer.)

---

## Trade-Off Analysis (3-Step Method) {#trade-off-analysis-3-step}

The meta-skill. Introduced in Ch 2; operationalized in Ch 15. The book's signature contribution. (Ch 1, 2, 15.)

### The 3 steps

1. **Find what parts are entangled together.** What dimensions are interacting in this decision? Static coupling? Dynamic coupling? Semantic? Data? Use a static-coupling diagram with: OS/container deps, transitive deps, persistence deps, integration points, messaging infra.
2. **Analyze how they are coupled to one another.** Name the type (static / dynamic / semantic / stamp / contract). Rate the strength.
3. **Assess trade-offs by determining the impact of change to interdependent systems.** For each candidate solution, what changes? What downstream impact? Score against the system's chosen architectural characteristics.

### Output: a trade-off table + ADR

```
ADR-NNN: <decision title>

Context: <forces, constraints, assumptions>

Decision: <chosen option>

Trade-off table:
| Option | <char 1> | <char 2> | <char 3> | … |
|---|---|---|---|---|
| A | high | medium | low | … |
| B | medium | high | high | … |

Consequences:
- Positive: <…>
- Negative: <…>
- Mitigations: <…>
```

### Discipline as the practice

Ch 15's closing scene has Logan defending the method to a skeptical exec:

> "But isn't that just adding a lot of extra process and procedures to the mix?"
> "No. That's architecture. And as you can see, it works."

The method is the practice. Skip it on one decision and the next architect can't tell intentional from incidental.

### When to invoke

| Trigger | Why use the method |
|---|---|
| Choosing a saga pattern | The 3 axes need explicit scoring |
| Choosing a data access pattern | Read latency / freshness / coupling trade-off needs surfacing |
| Choosing a contract style | Strict/loose trade-off is non-obvious without the table |
| Choosing service granularity | Disintegrators vs integrators need explicit weighing |
| Any architectural decision someone will second-guess later | The ADR is the only defense |

---

## Cross-Reference: Concept → Skill → Anchor

This table is the inverse of `INDEX.md`'s "If you need X, load Y." Use it to find the framework anchor when you already know what concept you want.

| Concept | Primary skill | Anchor here |
|---|---|---|
| Architectural quantum | `architectural-quanta-and-modularity` | [§architectural-quantum](#architectural-quantum) |
| Static vs dynamic coupling | `architectural-quanta-and-modularity` | [§coupling-vocabulary](#coupling-vocabulary) |
| Modularity drivers | `architectural-quanta-and-modularity` | [§modularity-drivers](#modularity-drivers) |
| Component-Based Decomposition | `service-and-data-decomposition` | [§component-based-decomposition](#component-based-decomposition) |
| Tactical Forking | `service-and-data-decomposition` | [§decomposition-patterns](#decomposition-patterns) |
| Data domain | `data-ownership-and-distributed-data` | [§data-decomposition](#data-decomposition) |
| Data ownership models | `data-ownership-and-distributed-data` | [§data-ownership-patterns](#data-ownership-patterns) |
| Column Schema Replication | `data-ownership-and-distributed-data` | [§data-access-patterns](#data-access-patterns) |
| Replicated Cache | `data-ownership-and-distributed-data` | [§data-access-patterns](#data-access-patterns) |
| Granularity disintegrators / integrators | `service-granularity-forces` | [§granularity-forces](#granularity-forces) |
| Replicated Code / Shared Library / Shared Service / Sidecar | `code-reuse-in-distributed-systems` | [§reuse-patterns](#reuse-patterns) |
| The 8 sagas | `distributed-workflows-and-sagas` | [§the-8-transactional-sagas](#the-8-transactional-sagas) |
| Saga selection | `distributed-workflows-and-sagas` | [§saga-selection-matrix](#saga-selection-matrix) |
| Orchestration vs Choreography | `distributed-workflows-and-sagas` | [§workflow-coordination](#workflow-coordination) |
| Stamp coupling | `service-contracts-and-coupling` | [§coupling-vocabulary](#coupling-vocabulary), [§contracts](#contracts) |
| Semantic coupling | `service-contracts-and-coupling` | [§coupling-vocabulary](#coupling-vocabulary) |
| Strict vs loose contracts | `service-contracts-and-coupling` | [§contracts](#contracts) |
| Consumer-Driven Contracts | `service-contracts-and-coupling` | [§contracts](#contracts) |
| Trade-off analysis method | `trade-off-analysis-method` | [§trade-off-analysis-3-step](#trade-off-analysis-3-step) |
| Data mesh / DPQ | (deferred — Data Engineering folder) | [§analytical-data](#analytical-data) |
