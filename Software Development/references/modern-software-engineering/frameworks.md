# Frameworks: Modern Software Engineering

**Source:** *Modern Software Engineering* by Dave Farley

A catalog of every framework, principle, and pattern Farley introduces or
applies. Use alongside `additional-experts.md` for application guidance.

---

## Framework Index (Alphabetical)

| Framework | Domain | When to apply |
|---|---|---|
| Anti-Corruption Layer | Architecture | Isolating legacy systems |
| BAPO (Business Architecture Process Organization) | Org design | Top-down org design |
| BDD (Behavior-Driven Development) | Practice | Cross-functional collaboration via shared language |
| Bounded Contexts | Architecture | Service boundary identification |
| Cohesion | Design | Module quality measurement |
| Continuous Delivery | Practice | Releasable software at all times |
| Continuous Integration | Practice | Frequent merges with feedback |
| Coupling (loose vs tight) | Design | Module relationship measurement |
| Decoupling Teams and Systems | Org design | Conway's Law application |
| Deployment Pipeline | CD infrastructure | Automated releasability gate |
| Design Engineering | Mindset | Treating code as executable model |
| Domain-Driven Design (DDD) | Architecture | Domain modeling and bounded contexts |
| Domain-Specific Languages (DSL) | Abstraction | Hide detail; raise abstraction level |
| Empirical Process Control | Process | Evidence-based decisions |
| Event Storming | Discovery | Identifying bounded contexts collaboratively |
| Fail Fast | Discipline | Surface errors immediately |
| Fail Safely | Design | Graceful degradation |
| Fractal Modularity | Design principle | Recursive modularity |
| High Cohesion, Loose Coupling | Design principle | Module design lever |
| Incrementalism | Practice | Small experiments to manage risk |
| Information Hiding | Design principle | Stable interfaces |
| Iteration | Practice | Repetition toward goal |
| Layers of Isolation | Architecture | Layered architecture isolation property |
| Levels of Indirection | Design | Decoupling via dependency injection |
| Mechanical Sympathy | Design | Hardware-aware design |
| Microservices | Architecture | Independent ownership and scaling |
| Modularity | Design principle | Compartmentalization |
| Optimize for Learning | Mindset | Feedback as primary product |
| Ports & Adapters | Architecture | Domain/infrastructure separation |
| Production Is Not Our Problem | Mindset | Confidence in deployment |
| Scientific Rationality in Software | Mindset | Software as experimental system |
| Separation of Concerns | Design principle | Single-responsibility focus |
| Shift-Left | Practice | Early defect detection |
| Stakeholder Alignment | Process | Synthesizing conflicting goals |
| Strict Modularity | Design discipline | Low tolerance for complexity |
| Test-Driven Development (TDD) | Practice | Test-first design |
| Testability as a Design Driver | Design principle | Use testing pain as feedback |
| Working Iteratively | Practice | Repetition toward goal |
| YAGNI (You Ain't Gonna Need It) | Discipline | Avoid speculative generality |

---

## Framework Catalog (Detailed)

### The Three Laws of Software Engineering (this book)

While not formally numbered, Farley's foundational claims:

1. **Engineering ≠ Code:** Software engineering is the entire process, culture,
   and philosophy required to build software, not just the code.

2. **Mistakes are inevitable; optimize for cheap detection:** Don't try to prevent
   mistakes (impossible); optimize for fast cheap detection.

3. **Empirical, not theoretical:** Software engineering is closer to medicine
   or experimental science than to pure mathematics. Base decisions on evidence.

---

### Continuous Integration (CI)

**Originator:** Practice popularized by Kent Beck and the XP community

**Definition:** Merge all developers' working copies to a shared mainline several
times a day. Every merge triggers automated build + test.

**Healthy CI indicators:**
- Time from commit to feedback: < 10 min
- Frequency of merges to main: multiple per day per developer
- Cost of broken build: stop, fix, ship within minutes

**Anti-pattern indicators:**
- Time to feedback: > 1 hour
- Days/weeks between merges
- Investigation lasts days when CI breaks

---

### Continuous Delivery (CD)

**Originator:** Dave Farley + Jez Humble (the original *Continuous Delivery* book, 2010)

**Definition:** Software is always in a releasable state; deployment becomes a non-event.

**Required infrastructure:**
- **Deployment pipeline:** Automated mechanism determining releasability
- **Environment as code:** Same configuration in dev/staging/prod
- **Feature flags:** Decouple deployment from release
- **Automated rollback:** Bad deploys self-recover

---

### Test-Driven Development (TDD)

**Originator:** Kent Beck (modern formulation), 1990s

**Loop:**
- **Red:** Write a failing test
- **Green:** Write *just enough* code to make it pass
- **Refactor:** Clean up code and tests while keeping them passing

**Deeper purpose:** Drives better design. If a test is hard to write, the
design is wrong.

---

### Behavior-Driven Development (BDD)

**Originator:** Dan North (2006)

**Definition:** Methodology emphasizing collaboration between business stakeholders
and developers to define behavior through shared language, often supported by
automated acceptance testing.

**Key practice:** Given/When/Then specifications that double as both documentation and tests.

---

### Domain-Driven Design (DDD)

**Originator:** Eric Evans (book of the same name, 2003)

**Definition:** Software development approach that focuses on modeling complex
domain problems in terms of their own vocabulary and concepts.

**Key concepts:**
- **Bounded Context:** A region where one model is consistent
- **Ubiquitous Language:** Within a bounded context, one shared vocabulary
- **Anti-Corruption Layer:** Boundary preventing one bounded context from infecting another
- **Domain Events:** Things that happened in the domain; foundation for event-driven systems

**When to apply:** Complex domains where business logic is non-trivial. Overkill for simple CRUD.

---

### Bounded Contexts

**Originator:** Eric Evans (DDD)

**Definition:** Natural lines of abstraction in the problem domain. More
decoupled than technical divisions; identified through techniques like event storming.

**Why they matter for architecture:** Bounded contexts make better service
boundaries than technical divisions because they reflect real-world domain boundaries.

---

### Event Storming

**Originator:** Alberto Brandolini

**Definition:** Collaborative analysis technique used to model interactions
within a problem domain.

**Process:**
1. Gather domain experts and developers
2. Map domain events on a timeline using sticky notes
3. Identify clusters of related behavior
4. Bounded contexts emerge from the clusters

---

### Modularity

**Definition:** Degree to which a system's components can be separated and
recombined with flexibility.

**Properties:**
- Small, understandable pieces
- Internal workings hidden (information hiding)
- Stable interfaces

---

### High Cohesion, Loose Coupling

**Definition:**
- **Cohesion:** How much elements inside a module belong together
- **Coupling:** Dependencies between modules

**Goal:** High cohesion AND loose coupling, simultaneously, at every level.

---

### Separation of Concerns

**Originator:** Edsger Dijkstra (term origin)

**Definition:** Each module addresses one issue. Reduces interdependencies;
isolates change impact.

**Practical implementation:**
- "One class, one thing"
- Minimize coupling between essential complexity (core logic) and accidental complexity (persistence, security)

---

### Information Hiding

**Originator:** David Parnas (1972)

**Definition:** Hide internal workings; expose stable interfaces. Today's
"internal detail" is tomorrow's API breaking change if exposed.

**Practical advice:**
- Use general representations (`List` instead of `ArrayList`)
- Use dependency injection to create measurement points
- Avoid overly generic abstractions like `Object`

---

### Ports & Adapters (Hexagonal Architecture)

**Originator:** Alistair Cockburn (early 2000s)

**Definition:** Mechanism connecting different parts of a system. Domain core
depends on nothing external; ports are interfaces; adapters translate to/from
external systems.

**Visualization:**
```
                    ┌──────────────┐
                    │  Domain Core │
                    │   (Pure)     │
                    └──────┬───────┘
                           │ defines
                           ▼
                    ┌──────────────┐
                    │     Ports    │
                    │ (interfaces) │
                    └──────┬───────┘
                           │ implemented by
            ┌──────────────┼──────────────┐
            ▼              ▼              ▼
        ┌────────┐   ┌─────────┐    ┌────────┐
        │  HTTP  │   │   DB    │    │ Queue  │
        │adapter │   │ adapter │    │adapter │
        └────────┘   └─────────┘    └────────┘
```

---

### Anti-Corruption Layer

**Originator:** Eric Evans (DDD)

**Definition:** A boundary or translation layer placed around a legacy system
to prevent new systems from adopting bad practices or patterns inherent in
the old code.

**When to apply:** Integrating with legacy systems whose model differs from yours.

---

### Mechanical Sympathy

**Originator:** Term from racing (Jackie Stewart); applied to software by Martin Thompson

**Definition:** Concept describing the alignment of technical tools and processes
with human cognitive capabilities — and with the underlying hardware.

**In practice:** Cache-friendly data structures, awareness of memory hierarchy,
designs validated through measurement rather than assumption.

---

### Levels of Indirection

**Definition:** Strategies used to decouple components, often achieved through
dependency injection, to increase flexibility and testability.

**Caveat:** Each level adds cognitive load. Don't apply more indirection than necessary.

---

### Working Iteratively

**Definition:** A procedure where repetition of operations yields results
successively closer to a desired goal, driven by the assumption that mistakes
are inevitable and must be mitigated rather than avoided at the start.

**Implementation:** Small experiments → measure → adjust → repeat.

---

### Incrementalism

**Definition:** The strategy of breaking work into small, manageable experiments
or changes to limit risk and manage complexity without requiring full system
understanding upfront.

---

### Empirical Process Control

**Definition:** Base decisions on evidence and data gathered from experiments
and observations rather than fashion, guesswork, or rigid defined-process models.

**Contrast with:** Waterfall (fully specified upfront) and pure agile (no specification).

---

### Fail Fast

**Definition:** Identify defects and validate ideas with minimum cost so that if
an idea is bad, it can be identified quickly with low investment.

**Goal:** Reduce the "blast radius" of failure.

---

### Fail Safely

**Definition:** Systems should be designed to recover gracefully from unexpected
errors or failures rather than attempting to predict every possible scenario perfectly.

**Implementation:** Bulkheads, circuit breakers, retries with backoff, graceful degradation.

---

### Shift-Left

**Definition:** Process of preferring early failures by identifying defects first
in compile-time checks, then unit tests, and finally higher-level tests.

**Cost ladder:**
- Compile time: $1 to fix
- Unit tests: $10
- Integration tests: $100
- Production: $1,000

**Implication:** Invest in earlier-stage gates. Static type checks, lint, fast unit tests catch the same bugs cheaper than production incidents.

---

### Mechanical Sympathy

**Definition:** Code structured based on a deep understanding of underlying
hardware mechanics (such as cache behavior) to maximize performance, validated
through experimentation.

**Example:** Cache-friendly data structures (arrays of structs vs structs of arrays)
can be 10-100x faster than algorithmically-equivalent designs.

---

### Fractal Modularity

**Definition:** Apply modularity principles recursively across all levels of
granularity, from entire enterprise systems down to individual methods and functions.

**Why this matters:** Same principles work at every scale. The skills transfer.

---

### Decouple Teams and Systems

**Definition:** Organize teams and architectures to minimize dependencies,
allowing independent creation, testing, and deployment.

**Conway's Law:** Organizations design systems that mirror their communication structure.

**Inverse Conway:** Design teams to match the system structure you want.

---

### YAGNI (You Ain't Gonna Need It)

**Originator:** XP community (Kent Beck, Ron Jeffries)

**Definition:** Write only the code necessary to solve the current problem.
Avoid future-proofing and over-engineering.

**Practical guidance:** If tempted to add a "configurable" or "extensible"
feature with one current use case, don't. Add it when the second use case appears.

---

### Testability as a Design Driver

**Definition:** Use the requirement for easy testing to force better design
decisions, including modularity, loose coupling, and clear interfaces.

**Practical use:** When something is hard to test, the design is wrong. Refactor for testability.

---

### Microservices

**Definition (this book):** Architectural style featuring services that are:
- Small, focused on one task
- Aligned with a bounded context
- Autonomous
- Independently deployable
- Loosely coupled

**When to apply:** Independent team ownership + clear bounded contexts + operational maturity.

**When NOT to apply:** Small teams, tightly coupled domains, low operational maturity.

---

### Domain-Specific Languages (DSL)

**Definition:** Narrowly focused languages or graphical representations used to
hide detail and raise the level of abstraction for solving specific problems.

**Examples:** SQL for data queries, regex for pattern matching, build files (Makefile, Bazel BUILD).

---

### Deployment Pipeline

**Definition:** An automated mechanism intended to determine the releasability
of an independently deployable unit of software.

**Stages:**
- Build
- Unit tests
- Integration tests
- Acceptance tests
- Performance tests
- Deploy to staging
- Deploy to production

If passes pipeline, can ship.

---

### BAPO (Business Architecture Process Organization)

**Originator:** Industry term (Software Engineering Institute)

**Definition:** Organizational structure approach where business vision and goals
are identified first, followed by architecture, process, and finally organization.

**Contrast with OBAP:** Organization first → Business → Architecture → Process.
Common but problematic — organizes around current org chart instead of needed structure.

---

### Layers of Isolation

**Definition:** Property of layered architecture where changes in one layer
should not impact others if contracts remain unchanged.

**Caveat:** Major request flows require closed layers to prevent tight coupling.
Open layers (where some can be bypassed) reduce isolation.

---

### Optimize for Learning

**Definition:** Prioritize building better software faster by ensuring feedback
is fast, efficient, and actionable to guide decision-making.

**Practical implication:** When choosing between options, prefer the one that
gives faster, clearer feedback even if it's slightly less elegant.

---

### Strict Modularity / Low Tolerance for Complexity

**Definition:** Maintain a strict standard where code must remain simple and
readable; pause and refactor immediately when complexity increases.

**Anti-pattern:** "We'll clean this up later" — later never comes.

---

### Production Is Not Our Problem

**Mindset:** Triggering a build is considered "production" in the engineering
sense. The deployment is a result of practices, not a separate event to fear.

**Implication:** Confident deployment requires confident engineering practices upstream.

---

### Design Engineering

**Definition (this book):** An approach focusing on the exploration and design
of systems rather than the mass production of artifacts, treating code as an
executable model that can be rapidly iterated upon.

**Implication:** Code is for thinking with, not just for execution. Refactoring
is part of design, not a tax.

---

### Stakeholder Alignment

**Definition:** Synthesizing conflicting stakeholder goals (e.g., quality vs speed)
through PM vision and strategic thinking to paint a full picture of trade-offs.

**Practical advice:** Make trade-offs explicit. Document them. Revisit periodically.

---

## Cross-Reference Map

```
   ┌─────────────────────────────────────┐
   │  Engineering ≠ Code (1st Law)       │
   │  Empirical Process Control          │
   │  Mistakes are inevitable            │
   └────────────┬────────────────────────┘
                │
                ▼
   ┌─────────────────────────────────────┐
   │  Iterative Practices (the daily)    │
   ├─────────────────────────────────────┤
   │  • CI                               │
   │  • CD                               │
   │  • TDD                              │
   │  • Shift-Left                       │
   │  • Mechanical Sympathy              │
   │  • Fail Fast                        │
   │  • Working Iteratively              │
   └────────────┬────────────────────────┘
                │
                ▼
   ┌─────────────────────────────────────┐
   │  Modularity Principles (the design) │
   ├─────────────────────────────────────┤
   │  • Modularity                       │
   │  • High Cohesion, Loose Coupling    │
   │  • Separation of Concerns           │
   │  • Information Hiding               │
   │  • Fractal Modularity               │
   │  • YAGNI                            │
   │  • Testability as Design Driver     │
   │  • Levels of Indirection            │
   │  • Strict Modularity                │
   └────────────┬────────────────────────┘
                │
                ▼
   ┌─────────────────────────────────────┐
   │  Architectural Patterns             │
   ├─────────────────────────────────────┤
   │  • Ports & Adapters                 │
   │  • DDD + Bounded Contexts           │
   │  • Anti-Corruption Layer            │
   │  • Microservices                    │
   │  • Layers of Isolation              │
   │  • DSL                              │
   │  • Event Storming (discovery)       │
   └────────────┬────────────────────────┘
                │
                ▼
   ┌─────────────────────────────────────┐
   │  Org Design                         │
   ├─────────────────────────────────────┤
   │  • Decouple Teams and Systems       │
   │  • BAPO (vs OBAP)                   │
   │  • Conway's Law / Inverse Conway    │
   └─────────────────────────────────────┘
```

---

## How to use this catalog

- **Vaguely remember a name?** → Browse the alphabetical index
- **Setting up engineering practices?** → See the Iterative Practices subsection
- **Designing module boundaries?** → See Modularity Principles
- **Choosing architectural style?** → See Architectural Patterns
- **Need expert advice?** → See `additional-experts.md`
