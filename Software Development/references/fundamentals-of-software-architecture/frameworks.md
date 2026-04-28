# Frameworks: Fundamentals of Software Architecture

**Source:** *Fundamentals of Software Architecture* by Mark Richards and Neal Ford

A catalog of every framework, pattern, principle, and concept this book introduces
or applies. Use alongside `additional-experts.md` for application guidance.

---

## Framework Index (Alphabetical)

| Framework | Domain | When to apply |
|---|---|---|
| ADR (Architecture Decision Record) | Decision documentation | Significant architecture decisions |
| Anti-Corruption Layer | Architecture | Isolating legacy systems |
| Application Services (SOA) | SOA | Single-implementation, single-team services |
| Architectural Characteristics ("ilities") | Design | Defining what matters |
| Architectural Quantum | Distributed systems | Defining unit of independent deployment |
| Architecture Sinkhole (anti) | Anti-pattern | Layered architecture mismatch |
| BFF (Backends for Frontends) | Distributed | Multiple frontend client types |
| Big Ball of Mud (anti) | Anti-pattern | No discernible structure |
| Bottleneck Architect (anti) | Anti-pattern | Architect on critical path |
| Bounded Context | Domain modeling | Service boundary identification |
| Broker-Domain Pattern | Distributed | Multiple message brokers per domain |
| Business Services (SOA) | SOA | Top-level entry points |
| Chaos Engineering | Reliability | Production resilience testing |
| Choreography vs Orchestration | Distributed | Service coordination pattern |
| Closed vs Open Layers | Architecture | Layered architecture isolation |
| Cohesion | Design | Internal module quality |
| Component-Based Thinking | Design | Logical structure modeling |
| Composite Architectural Characteristics | Design | Decomposition of "ilities" |
| Connascence Framework | Coupling | Coupling strength analysis |
| Coupling | Design | Inter-module relationships |
| Data Pumps (Space-Based) | Distributed | Async data persistence |
| Data Readers (Space-Based) | Distributed | Async data retrieval |
| Data Writers (Space-Based) | Distributed | Async DB updates |
| Database-per-Service | Microservices | Service data ownership |
| Database Topologies (Dedicated/Domain/Monolithic) | Distributed | Data architecture choice |
| Decoupling Patterns | Design | Reducing inter-service dependencies |
| Dedicated Database Topology | Distributed | Microservices data pattern |
| Deployment Pipeline | CD | Releasability mechanism |
| Distributed Monolith (anti) | Anti-pattern | Coupled services |
| Domain Database Topology | Distributed | Domain-clustered databases |
| Domain Partitioning | Architecture | Service organization |
| Enterprise Services (SOA) | SOA | Reusable building blocks |
| Event-Driven Architecture | Architecture style | High-decoupling reactive systems |
| Event Storming | Discovery | Bounded context identification |
| Extreme Decoupling | Microservices | Duplication > coupling |
| Fast-Lane Reader (anti) | Anti-pattern | Layer bypassing |
| First Law of Software Architecture | Foundational | Everything is a trade-off |
| Fitness Functions | Architecture governance | Automated architecture verification |
| Frozen Caveman (anti) | Anti-pattern | Outdated patterns |
| God Orchestrator (anti) | Anti-pattern | Centralized complexity |
| Hidden Connascence | Connascence | Implicit coupling |
| Implicit vs Explicit Characteristics | Design | Surfacing required ilities |
| Infrastructure Services (SOA) | SOA | Operational cross-cutting |
| Iterative Component Identification | Design process | Component decomposition |
| Ivory Tower Architecture (anti) | Anti-pattern | Decisions in isolation |
| ISO Quality Attributes | Standards | Standardized characteristics |
| Knowledge Pyramid | Mindset | Architect's epistemology |
| Last Responsible Moment | Process | Decision deferral discipline |
| Law of Demeter | Design | Loose coupling principle |
| Layered Architecture | Style | Default monolithic style |
| Layers of Isolation | Architecture | Layered isolation property |
| Least Worst Architecture | Mindset | Trade-off acceptance |
| Logical Components | Design | Component-level building blocks |
| Logical vs Physical Architecture | Design | Modeling separation |
| Message Bus | SOA/EDA | Integration intermediary |
| Microkernel Architecture | Style | Plug-in architecture |
| Microservices | Style | Bounded-context-aligned services |
| Monolithic Database Topology | Distributed | Single shared database |
| Orchestration Engine (SOA) | SOA | Workflow coordination |
| Orthogonal Coupling | Design | Cross-cutting concern isolation |
| Pipeline Architecture | Style | Workflow processing |
| Premature Microservices (anti) | Anti-pattern | Distribution before justified |
| Premature Service Mesh (anti) | Anti-pattern | Mesh before scale justifies |
| Saga Pattern | Distributed | Multi-service atomicity |
| Second Law of Software Architecture | Foundational | Why > how |
| Service Mesh | Distributed | Multi-service operational fabric |
| Service-Based Architecture | Style | Pragmatic distributed |
| Service-Oriented Architecture (SOA) | Style | Enterprise integration |
| Shared Database (anti) | Anti-pattern | Data-layer coupling |
| Sidecar Pattern | Distributed | Cross-cutting concern isolation |
| Single Source of Truth | Decision | ADRs in wiki |
| Single System of Record | Decision | Centralized decision storage |
| Space-Based Architecture | Style | Extreme elastic scale |
| Static vs Dynamic Connascence | Coupling | Coupling visibility |
| Strength/Locality/Degree | Connascence | Connascence properties |
| Technical Breadth vs Depth | Architect mindset | Skill development |
| Technology Radar (Thoughtworks) | Mindset | Continuous tech evaluation |
| Third Law of Software Architecture | Foundational | Spectrum, not binary |
| Trade-Off Analysis | Process | Architectural decisions |
| Translation from Domain Concerns | Process | Business → "ilities" mapping |
| Virtualized Middleware | Distributed | Space-Based infra |

---

## Framework Catalog (Detailed)

### The Three Laws of Software Architecture

**First Law:** Everything is a trade-off.
**Second Law:** Why is more important than how.
**Third Law:** Most architecture decisions exist on a spectrum, not as binaries.

These foundational laws inform every other framework in the book.

---

### Architectural Characteristics ("Ilities")

**Definition:** Non-domain design considerations that influence structural aspects
of the design. Critical or important to the application's success.

**Categories (ISO Quality Model):**
- Performance efficiency
- Compatibility
- Usability
- Reliability
- Security
- Maintainability
- Portability
- Functional suitability

**Implicit vs Explicit:**
- Explicit: Stated in requirements
- Implicit: Necessary but not stated (security, availability, basic usability)

---

### Composite Architectural Characteristics

**Definition:** Characteristics with no single objective definition; composed
of measurable parts.

**Example:** "Agility" decomposes to deployability + modularity + testability.

**Rule:** Always decompose composite characteristics before treating them as requirements.

---

### Translation from Domain Concerns

**Definition:** Architects must translate business goals into corresponding "-ilities."

**Mapping:**

| Business goal | Architectural characteristic |
|---|---|
| Mergers and acquisitions | Interoperability |
| Time to market | Agility |
| User satisfaction | Performance + availability + usability |
| Competitive advantage | Time to market + scalability |
| Time and budget | Simplicity + feasibility |

---

### Least Worst Architecture

**Principle:** It is rare to maximize every architectural characteristic; architects
must choose the fewest possible characteristics that are critical to success.

**Implication:** 3-7 characteristics is typical. Aim for "least worst" rather than "best."

---

### Knowledge Pyramid

**Structure:** Three levels of technical knowledge:
1. **Stuff you know:** What you can do today
2. **Stuff you know you don't know:** What you need to learn
3. **Stuff you don't know you don't know:** The dangerous zone

**Architect's job:** Shrink the third layer by knowing a little about a lot.

---

### Thoughtworks Technology Radar

**Originator:** Thoughtworks (free public publication)

**Structure:** Four rings for tech assessment:
- **Hold:** Don't use
- **Assess:** Watch and learn
- **Trial:** Use in non-critical areas
- **Adopt:** Use in production

---

### Connascence Framework

**Originator:** Meilir Page-Jones (1992); revived for modern use

**Definition:** A quality of relationship between components measuring coupling strength.

**Static Connascence (visible in source code), weakest to strongest:**

| Type | Example |
|---|---|
| Connascence of Name | Method name, variable name |
| Connascence of Type | Function expects an `int` |
| Connascence of Meaning | "0 means inactive, 1 means active" — magic numbers |
| Connascence of Position | Argument order in function calls |
| Connascence of Algorithm | Both sides hash the same way |

**Dynamic Connascence (only at runtime):**

| Type | Meaning |
|---|---|
| Connascence of Execution | Components must execute in specific order |
| Connascence of Timing | Timing constraints |
| Connascence of Values | Multiple values must agree (distributed transaction) |
| Connascence of Identity | Must reference same instance |

**Three Properties:**
- **Strength:** How easy to refactor (Name = easy; Identity = hard)
- **Locality:** Closer = better tolerated (within module > across services)
- **Degree:** How many components share the connascence

**Rules:**
- Stronger connascence = worse coupling. Reduce strength.
- Closer locality = stronger connascence is acceptable.
- Lower degree = better.

---

### Architectural Quantum

**Definition:** The smallest part of the system that runs independently.

**Properties:**
- Independent deployment
- High functional cohesion
- Low external static coupling
- Synchronous communication

**Practical implication:** A microservices system with shared DB has architectural
quantum = the whole system, not individual services.

---

### Logical Components

**Definition:** Building blocks of a system identified at the level of major
functions or workflows rather than classes.

**Manifestation:** Often via namespace or directory structures.

---

### Component-Based Thinking

**Definition:** The practice of viewing system structure as a set of interacting
logical components performing specific business functions.

---

### Logical vs Physical Architecture

**Logical Architecture:** What the system does and how functionality is demarcated.
Independent of physical deployment.

**Physical Architecture:** How the system is deployed (services, databases,
networks, regions).

**Best practice:** Define logical architecture first; physical can change without changing logical.

---

### Iterative Component Identification

**Process:**
1. Identify candidate components from user stories
2. Refine against architectural characteristics
3. Restructure as evidence comes in

**Anti-pattern:** Trying to design the perfect component decomposition upfront.

---

### Domain Partitioning vs Technical Partitioning

**Technical Partitioning:** Organize by capability (presentation, persistence, business)
**Domain Partitioning:** Organize by workflows and domains

**Industry trend:** Domain partitioning. Better aligns with business changes
and cross-functional teams.

---

### Fitness Functions

**Originator:** Building Evolutionary Architectures (Ford, Parsons, Kua)

**Definition:** Automated governance mechanisms used to verify architectural
principles and constraints within continuous integration pipelines.

**Examples:**
- "No service exceeds 200ms p99 latency" — automated test
- "No domain code imports framework code" — static analysis
- "Inter-service coupling stays below threshold" — measured automatically

---

### Chaos Engineering

**Originator:** Netflix (Chaos Monkey)

**Definition:** Discipline involving the simulation of general chaos in production
environments to test system robustness and anticipate breakages.

**Why it matters:** Production failures will happen. Better to discover failure
modes when you control the timing.

---

### Layered Architecture

**Style:** Components organized by technical capability (presentation, business, persistence).

**Layers (typical):**
1. Presentation
2. Business Rules
3. Persistence
4. Database

**Closed vs Open Layers:**
- Closed: requests must traverse every layer (better isolation)
- Open: some layers can be bypassed (more flexibility)

**Default:** Closed layers.

**Anti-patterns:**
- **Fast-Lane Reader:** Presentation accesses Database directly
- **Architecture Sinkhole:** Most requests pass through layers performing trivial work

---

### Pipeline Architecture

**Style:** Technically partitioned style using unidirectional pipes and filters.

**Components:**
- Producer
- Transformer
- Tester
- Consumer

**Best for:** Workflow-based data processing, ETL, compilers.

---

### Microkernel Architecture

**Style:** Core system + plug-ins.

**Principle:** Core contains only minimal happy path. Complex domain logic in plug-ins.

**Examples:** IDEs, browsers, products with extension marketplaces.

---

### Service-Based Architecture

**Style:** Coarse-grained domain services accessed remotely (e.g., REST), often
with optional monolithic database.

**Key property:** Pragmatic middle ground between monolith and microservices.

---

### Service-Oriented Architecture (SOA)

**Service hierarchy:**
- **Business Services:** Top-level entry points; coarse-grained business processes
- **Enterprise Services:** Reusable building blocks; isolated business functionality (CreateCustomer, CalculateQuote)
- **Application Services:** One-off, single-implementation, single-team
- **Infrastructure Services:** Operational concerns (monitoring, logging, auth)

**Components:**
- **Orchestration Engine:** Stitches together business service implementations
- **Message Bus:** Integration hub; intermediary for all calls

---

### Microservices Architecture

**Style:** Distributed architecture; each service runs in its own process,
includes everything to operate independently, driven by bounded contexts.

**Properties:**
- Fine granularity
- Aligned to bounded contexts
- Database-per-service
- Independent deployment
- Sidecars for cross-cutting concerns

---

### Space-Based Architecture

**Style:** Multiple parallel processors communicating through shared memory
(tuple space). High scalability, elasticity, performance.

**Components:**
- **Processing Units:** Replicated, in-memory data
- **Virtualized Middleware:** Messaging grid, data grid, deployment manager
- **Data Pumps:** Async messages from processing units to data writers
- **Data Writers:** Update database with payload information
- **Data Readers:** Read DB → send to processing units (for cold start)

**When to use:** Extreme elastic scaling, unpredictable high load.

---

### Database Topologies (in distributed systems)

**Dedicated Database Topology:**
- Each event processor owns its own dedicated database within a tightly formed bounded context
- Like microservices

**Domain Database Topology:**
- Combines domains into a single one
- Shares a database across multiple event processors

**Monolithic Database Topology:**
- Moves all domains and event processors to a single shared database instance

---

### Bounded Context

**Originator:** Eric Evans (DDD)

**Definition:** Decoupling style where each service models a particular function,
subdomain, or workflow, including everything necessary to operate within it
(code, database schemas, corresponding database).

---

### Saga Pattern

**Originator:** Garcia-Molina and Salem (1987); modernized for microservices

**Definition:** Distributed transaction pattern handling atomicity issues across
microservice boundaries by breaking transactions into a sequence of local actions
with compensating transactions for error conditions.

**Variants:**
- **Orchestrated Saga:** Central orchestrator coordinates the sequence
- **Choreographed Saga:** Each service listens for events and acts

**Key insight:** Compensating actions are forward-acting business operations,
not "undos." Refund ≠ deleting charge record.

---

### Sidecar Pattern

**Definition:** Co-deploy a companion container/process that handles cross-cutting
operational concerns.

**What goes in sidecar:** Logging, monitoring, auth/authz, mTLS, service discovery, rate limiting.

**Real-world examples:** Istio's Envoy, Datadog agent.

---

### Service Mesh

**Definition:** Sidecars + control plane. Control plane manages all sidecars to
provide consistent operational fabric.

**Components:**
- **Data plane (sidecars):** Handle traffic per-service
- **Control plane:** Configure sidecars centrally

**Examples:** Istio, Linkerd, Consul Connect.

---

### Backends for Frontends (BFF)

**Definition:** Thin API adapter layer per frontend device, translating generic
backend output into client-specific formats.

**When to adopt:** Multiple distinct client types with significantly different needs.

---

### Database-per-Service

**Definition:** Standard database topology for microservices where each service
owns its own data in a separate database or schema, preserving bounded contexts.

**Cross-service queries:** Solved via data duplication (controlled), CQRS read
models, or async event projection. Don't JOIN across services.

---

### Choreography vs Orchestration

**Choreography:**
- Services emit events; others subscribe and react
- Best for loosely coupled flows; bounded contexts respected
- Tradeoff: hard to trace; emergent behavior

**Orchestration:**
- Central orchestrator sends commands to services
- Best for complex multi-step flows that need coordination
- Tradeoff: single point of complexity; orchestrator can become god-service

**Default:** Start with choreography. Adopt orchestration for complex flows.

---

### Broker-Domain Pattern

**Definition:** Multiple message brokers, each serving a domain cluster, vs
single shared broker.

**Comparison:**

| Pattern | Pros | Cons |
|---|---|---|
| Single Broker | Simple ops | SPOF; ownership coupling |
| Broker-Domain | Fault isolation; domain ownership | More ops surface |

**When to adopt Broker-Domain:** Large enough that domain teams want to own
their messaging infra independently.

---

### Extreme Decoupling

**Principle:** "Duplication is preferable to coupling," especially regarding
internal representations within bounded contexts.

**Implication:** Don't share databases or schemas across services.

---

### Orthogonal Coupling

**Definition:** Distinct purposes (e.g., domain behavior vs operational monitoring)
must intersect; use patterns like Sidecars to isolate these concerns rather than
entangling them hierarchically.

---

### Last Responsible Moment

**Principle:** Architects should wait until there is enough information to justify
and validate a decision, but not so long that development is held up.

**Practical use:** When pressured to make decisions early, ask: "Do we have
evidence to validate this decision now?"

---

### Single System of Record / Single Source of Truth

**Definition:** Avoid storing architectural decisions in emails. Communicate only
the context and provide a link to a single location (e.g., ADR wiki page) containing
the full decision and justification.

---

### ADR (Architecture Decision Record)

**Format:**
- **Title:** Short noun phrase
- **Status:** Proposed / Accepted / Superseded
- **Context:** What problem are we solving?
- **Decision:** What did we decide?
- **Rationale:** Why?
- **Consequences:** What are the trade-offs?

**Storage:** Wiki, not emails.

---

### Event Storming

**Originator:** Alberto Brandolini

**Definition:** Collaborative analysis technique used to model interactions
within a problem domain, identify clusters of behavior, and highlight natural
lines of abstraction.

**Process:**
1. Domain experts + developers gather
2. Map domain events on timeline (sticky notes)
3. Identify clusters
4. Bounded contexts emerge

---

### Anti-Corruption Layer

**Definition:** Boundary or translation layer placed around a legacy system to
prevent new systems from adopting bad practices or patterns inherent in the old code.

---

### Cohesion / Coupling / Modularity

**Cohesion:** How much elements inside a module belong together
**Coupling:** Dependencies between modules
**Modularity:** Degree to which components can be separated and recombined

**Goal:** High cohesion AND loose coupling at every level.

---

### Law of Demeter (Principle of Least Knowledge)

**Originator:** Ian Holland (1987)

**Definition:** A component should have limited knowledge of other components
or services. Specifically, an object should only call methods on:
- Itself
- Its parameters
- Objects it creates
- Its direct fields

**Why:** Loose coupling; easier refactoring.

---

### Layers of Isolation

**Definition:** Property of layered architecture where changes in one layer
should not impact others if contracts remain unchanged.

**Caveat:** Major request flows require closed layers to prevent tight coupling.

---

### Implicit vs Explicit Characteristics

**Explicit:** Stated in requirements
**Implicit:** Necessary but not stated (security, availability, basic usability)

**Architect's job:** Surface implicit characteristics. They're often what bites if missed.

---

## Cross-Reference Map

```
                ┌────────────────────────────────────┐
                │  Three Laws of Software Architecture│
                │  1. Everything is a trade-off       │
                │  2. Why > How                       │
                │  3. Spectrum, not binary            │
                └────────────────┬───────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │  Architectural Characteristics     │
                │  (ilities)                         │
                ├────────────────────────────────────┤
                │  Composite + Implicit/Explicit     │
                │  Translation from Domain Concerns  │
                │  Least Worst Architecture          │
                │  Connascence (coupling vocab)      │
                └────────────────┬───────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │  Architectural Style Choice        │
                ├────────────────────────────────────┤
                │  Monolithic styles:                │
                │   • Layered                        │
                │   • Microkernel                    │
                │   • Pipeline                       │
                │  Distributed styles:               │
                │   • Service-Based                  │
                │   • Event-Driven                   │
                │   • Microservices                  │
                │   • SOA                            │
                │   • Space-Based                    │
                └────────────────┬───────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │  Distributed Patterns              │
                ├────────────────────────────────────┤
                │  Saga                              │
                │  Sidecar                           │
                │  Service Mesh                      │
                │  BFF                               │
                │  Database-per-Service              │
                │  Choreography vs Orchestration     │
                │  Broker-Domain                     │
                └────────────────┬───────────────────┘
                                 │
                                 ▼
                ┌────────────────────────────────────┐
                │  Process & Discipline              │
                ├────────────────────────────────────┤
                │  ADRs (decision documentation)     │
                │  Last Responsible Moment           │
                │  Iterative Component Identification│
                │  Event Storming (discovery)        │
                │  Fitness Functions (governance)    │
                │  Trade-Off Analysis                │
                └────────────────────────────────────┘

  Architect mindset:
  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────┐
  │ Knowledge       │  │ Tech Breadth     │  │ Technology Radar │
  │ Pyramid         │  │ vs Depth         │  │ (Hold/Assess/    │
  │                 │  │                  │  │  Trial/Adopt)    │
  └─────────────────┘  └──────────────────┘  └──────────────────┘

  Anti-patterns:
  Frozen Caveman │ Ivory Tower │ Bottleneck Architect │ Big Ball of Mud │
  Architecture Sinkhole │ Distributed Monolith │ Premature Microservices │
  God Orchestrator │ Shared Database │ Premature Service Mesh
```

---

## How to use this catalog

- **Vaguely remember a name?** → Browse the alphabetical index
- **Choosing an architecture style?** → See the comparison table in `additional-experts.md`
- **Analyzing coupling?** → See Connascence Framework
- **Designing distributed systems?** → See distributed patterns subsection
- **Need expert advice?** → See `additional-experts.md`
