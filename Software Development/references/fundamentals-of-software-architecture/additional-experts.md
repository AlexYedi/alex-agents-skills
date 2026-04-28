# Additional Experts: Fundamentals of Software Architecture

**Source:** *Fundamentals of Software Architecture* by Mark Richards and Neal Ford

This reference captures the accumulated wisdom of two of the most experienced
software architects working today. Use alongside:
- `architecture-characteristics-and-tradeoffs/SKILL.md`
- `architecture-styles-monolithic-and-distributed/SKILL.md`
- `distributed-system-patterns/SKILL.md`

---

## About the Experts

**Mark Richards** is an independent software architect with 30+ years of experience.
Author of *Software Architecture Patterns*, popular trainer, and frequent
conference speaker.

**Neal Ford** is a Director and Software Architect at Thoughtworks. Author of
multiple books including *Building Evolutionary Architectures* and *Software
Architecture: The Hard Parts* (with Richards).

The book is an academic-feeling textbook applied to real practice. Richards
brings decades of war stories from corporate consulting; Ford brings the
modern thoughtworks-style perspective on evolvable architecture.

The voice is firm on principles, hedged on specifics, and emphasizes that
architecture is fundamentally about trade-offs.

---

## The Architectural Mindset

### Architecture is fundamentally about trade-offs

Richards and Ford state this as their First Law of Software Architecture:
**"Everything is a trade-off."** No architecture is "right"; all are trade-off
resolutions for a specific context.

**Practical implications:**
- "Best practice" is context-dependent
- An architecture great for Netflix might be wrong for your startup
- Your job is not to find the "right" answer but to make trade-offs explicit and defensible

### Why is more important than how

The Second Law: **"Why is more important than how."**

Architecture decisions outlive their implementations. The reasoning behind a
choice is what matters when teams need to decide whether to keep, change, or
abandon the architecture.

**Practical advice:**
- Document the *rationale* for every significant decision
- ADRs (Architecture Decision Records) are the discipline
- Future-you will thank past-you

### Most decisions exist on a spectrum, not as binaries

The Third Law: forced binary thinking ("monolith vs microservices") misses
the spectrum. Service-Based Architecture sits between monolith and microservices.
Eventual consistency sits between strict and weak consistency.

**Practical implication:** Resist binary framings. Ask "where on the spectrum
should this be?"

### Technical breadth > technical depth for architects

Engineers go deep; architects go wide.

The Knowledge Pyramid:
- **Stuff you know:** What you can do today
- **Stuff you know you don't know:** What you need to learn
- **Stuff you don't know you don't know:** The dangerous zone

Architects must shrink the third layer by knowing a little about a lot of things.

**Practical advice:**
- Use the Thoughtworks Technology Radar pattern: Hold / Assess / Trial / Adopt
- Continually re-evaluate the technology landscape
- The "Frozen Caveman" architect (sticks with patterns from 10 years ago) is the failure mode

---

## Best Practices for Architectural Characteristics

### Surface implicit characteristics

Most architectural characteristics ("ilities") are explicit in requirements:
"system must handle 10K req/sec" → performance is explicit.

**The dangerous ones are implicit:**
- Security (always required, rarely stated)
- Availability (always required, rarely stated)
- Basic usability (always required, rarely stated)

**Architect's job:** Surface these. They're often what bites if missed.

### Decompose composite characteristics

Some characteristics are not directly measurable. They decompose into measurable parts:

**"Agility" decomposes to:**
- Deployability (how quickly can you ship?)
- Modularity (how isolated are changes?)
- Testability (how cheaply can you verify?)

Always decompose composite characteristics before treating them as requirements.
"We need agility" is unmeasurable. "We need deployability < 1 hour, modularity that
keeps blast radius < 1 service, testability with < 10 min CI" is.

### The Least Worst Architecture Principle

You can't maximize every characteristic — they conflict.

**Common conflicts:**
- Performance vs Security (encryption costs latency)
- Availability vs Consistency (CAP theorem)
- Simplicity vs Flexibility (more plug points = more complexity)
- Modularity vs Performance (module boundaries can prevent cache-friendly layouts)

**The rule:** Choose the **fewest** characteristics critical to success. 3-7
characteristics is typical. Aim for "least worst" rather than "best."

### Translating Business Goals to Characteristics

| Business goal | Architectural characteristic |
|---|---|
| Mergers and acquisitions | Interoperability |
| Time to market | Agility |
| User satisfaction | Performance + availability + usability |
| Competitive advantage | Time to market + scalability |
| Time and budget | Simplicity + feasibility |

This mapping is the architect's most important translation skill.

### Connascence: A Vocabulary for Coupling

Connascence measures coupling strength. Static (visible in source code) ranges from
weakest to strongest:

- **Connascence of Name:** Components agree on identifier names
- **Connascence of Type:** Components agree on types
- **Connascence of Meaning:** Components agree on values (magic numbers)
- **Connascence of Position:** Components agree on order (argument position)
- **Connascence of Algorithm:** Components agree on algorithm

Dynamic (only at runtime):
- **Connascence of Execution:** Order matters
- **Connascence of Timing:** Timing constraints
- **Connascence of Values:** Multiple values must agree
- **Connascence of Identity:** Must reference same instance

**Three properties:**
- **Strength:** Easier to refactor at lower strength (Name = easy; Identity = hard)
- **Locality:** Closer = better tolerated (within module > across services)
- **Degree:** Lower degree = better (fewer entangled components)

**Rules:**
- Stronger connascence = worse coupling. Reduce strength.
- Closer locality = stronger connascence is acceptable.
- Lower degree = better.

---

## Best Practices for Architectural Styles

### Layered Architecture: the right default for many

Layered (N-tier) is the default for most teams. Components grouped by technical
capability (presentation, business, persistence).

**When it works:**
- Small/medium apps
- Teams new to architecture
- Domains that decompose cleanly into layers

**When it fails:**
- Domain-heavy applications (architecture sinkhole appears)
- High-scale apps requiring independent service scaling
- Diverse team needs (frontend ≠ backend ≠ data)

**Closed vs Open layers:**
- Closed: requests must traverse every layer (better isolation)
- Open: some layers can be bypassed (more flexibility)
- **Default:** Closed layers. Open them only with deliberate justification.

### Microkernel: for product lines and extension marketplaces

Core system + plug-ins. Used by IDEs, browsers, products with extension marketplaces.

**Key principle:** Core contains only the **minimal happy path**. Complex domain
logic lives in plug-ins.

**When to use:** Apps with extension points; product line engineering; apps with
extension marketplaces.

### Service-Based: the pragmatic distributed

Coarse-grained services (4-12 typical), often with shared monolithic database,
usually REST communication.

**Why it matters:** Gets 80% of microservices benefits with 20% of operational pain.
A pragmatic middle ground.

**When to use:** Want some distributed properties (independent deployability,
separation of concerns) but don't want full microservices commitment.

### Microservices: when they earn their cost

Fine-grained services aligned to bounded contexts; database-per-service;
independent deployment.

**When microservices earn their cost:**
- Different services have genuinely different scaling needs
- Different services have different deployment cadences
- Multiple teams need independent ownership
- Bounded contexts in the domain are clearly identifiable
- Operational maturity is already strong

**When microservices are wrong:**
- Small team (< 8 engineers) — overhead exceeds benefits
- Tightly coupled domain — services constantly change together
- Operational immaturity — distributed systems amplify ops gaps
- Premature optimization — start with monolith

### Space-Based: for extreme scale

Replicated processing units + in-memory data grid. No central database in the hot path.

**When to use:** Extreme elastic scaling, high-throughput unpredictable load
(ticketing, flash sales, real-time auctions).

**Cost:** Very high operational complexity. Eventual consistency. Hard to debug.

### Choosing a Style: Use the Characteristics Comparison

The book provides a characteristics-rating matrix. Apply it:

1. List your top 3-5 critical characteristics
2. Rate each style on those characteristics
3. Pick the style with highest combined score

**Example for B2B SaaS, ~20 engineers, 5 product teams:**
- Critical: Modularity, Deployability, Operational Simplicity
- Result: Service-Based wins (microservices score higher on Modularity + Deployability but lose on Operational Simplicity)

---

## Best Practices for Distributed Systems

### Network is unreliable

Any distributed style must assume network failures. Built-in:
- Timeouts on all calls
- Circuit breakers to prevent cascading failure
- Retries with exponential backoff
- Graceful degradation when dependencies fail

**Practical implication:** Distributed code is fundamentally different from in-process code.
Don't pretend remote calls are local.

### Data minimization in distributed

Send only what's needed. Network and serialization costs add up at scale.

### Contract Governance

When services share contracts, change discipline matters:
- Versioning strategy (URL versioning, header versioning)
- Backward compatibility expectations
- Deprecation timelines
- Consumer-driven contracts (Pact)

### "Duplication is preferable to coupling"

Counterintuitive but central to microservices. Don't share data structures or
schemas across services. Duplicate the data via events.

**Why:** Shared schemas couple services at the data layer — the worst kind of coupling.

### Saga Pattern for Distributed Transactions

ACID transactions don't span services. Saga is the standard alternative.

**Variants:**
- **Orchestrated Saga:** Central orchestrator coordinates the sequence
- **Choreographed Saga:** Each service listens for events and acts

**Key insight:** Compensating actions are not "undo" — they're forward-acting
business operations that semantically reverse the original.

### Sidecar Pattern for Cross-Cutting Concerns

Co-deploy a companion that handles operational concerns (logging, monitoring,
auth, mTLS, service discovery).

**Why it works:**
- Domain code stays focused on business logic
- Operational concerns update independently across the fleet
- Sidecar updates don't require app team involvement

### Service Mesh: When You Have Many Services

Service Mesh = sidecars + control plane.

**When to adopt:**
- > 10 services
- Complex inter-service traffic
- Need consistent observability across services

**When NOT:** 3-service systems. Operational complexity exceeds benefits.

### BFF (Backends for Frontends)

Thin API adapter layer per frontend device.

**When to adopt:** Multiple distinct client types with different needs (iOS,
Android, web, third-party).

**Caveat:** Watch for one BFF doing too much. One BFF per *client class*, not
one BFF for all.

### Choreography vs Orchestration

| Pattern | When |
|---|---|
| Choreography | Loosely coupled flows; bounded contexts respected |
| Orchestration | Complex multi-step flows that need coordination |

**Rule of thumb:** Start with choreography. Adopt orchestration when complex flows need explicit coordination.

---

## Worked Examples

### Example 1: Architectural Characteristics for a Notification Service

**Business context:** Internal company notification service; sends emails, Slack messages, mobile push. Used by all internal product teams.

| Characteristic | Selected? | Rationale |
|---|---|---|
| Reliability | Yes (top 3) | Notifications downstream of user-impacting events; can't drop them |
| Scalability | Yes (top 3) | Internal use grows with company headcount + feature surface |
| Modularity | Yes (top 3) | Many integration points (email/Slack/push); modular plug-ins enable independent change |
| Performance | No (medium) | Notification latency tolerated up to seconds; not a hot path |
| Availability | Implicit | Always required; not unique to this system |
| Security | Implicit | Always required; not unique |
| Portability | No | Internal infra; no need to port |
| Usability | No | Backend service; consumed via API |

**Decomposition:** "Modularity" measured as: "Add new channel without modifying core orchestration code."

**Trade-off:** Selected reliability over performance. If a notification fails, retry. Latency acceptable; loss is not.

### Example 2: Choosing Style for B2B SaaS Backend

**Context:** B2B SaaS, ~20 engineers, 5 product teams, single-tenant deployments.

**Critical characteristics:** Modularity, Deployability, Operational Simplicity.

| Style | Modularity | Deployability | Op Simplicity | Total |
|---|---|---|---|---|
| Layered | 2 | 1 | 5 | 8 |
| Service-Based | 4 | 4 | 4 | **12** |
| Microservices | 5 | 5 | 1 | 11 |

**Decision:** Service-Based wins. Coarse-grained services enable team ownership
and independent deploys without microservices ops overhead.

**Lesson:** Microservices score highest on modularity + deployability but ops
simplicity is decisive given small ops team.

### Example 3: E-Commerce Order Flow with Saga

**Goal:** Place an order across Inventory, Pricing, Payment, Shipping, Notification services.

| Step | Service | Action | Compensation |
|---|---|---|---|
| 1 | Inventory | Reserve stock | Release reservation |
| 2 | Pricing | Calculate final price + tax | (no compensation; idempotent) |
| 3 | Payment | Charge card | Refund |
| 4 | Shipping | Schedule shipment | Cancel shipment |
| 5 | Notification | Send confirmation | Send cancellation notice |

**Pattern choice:** Orchestrated Saga (clarity over decoupling for this flow).

**Sidecars:** Each service has Envoy sidecar for mTLS, observability, retries.
**BFF:** Mobile app has its own BFF combining order + tracking calls.
**Service Mesh:** Istio manages cross-service auth and traffic shaping.

---

## Anti-Patterns (deeper than skill files)

### Frozen Caveman

Architect insists on patterns that worked 10 years ago, ignoring modern alternatives.
**Why:** Tools and patterns evolve. Yesterday's best practice = today's anti-pattern.
**The fix:** Use Thoughtworks Technology Radar (Hold / Assess / Trial / Adopt).

### Ivory Tower Architecture

Architect makes decisions in isolation; hands them down to implementation team.
**Why:** Misses on-the-ground reality; team has no buy-in; decisions don't survive contact with code.
**The fix:** Collaborate with implementers. Code reviews. Validate decisions in code, not just diagrams.

### Bottleneck Architect

Architect on critical path for all coding; team blocked.
**Why:** Architect becomes throughput limit.
**The fix:** Code on minor business functionality. Stay technical without becoming the bottleneck.

### Maximum Characteristic Optimization

Trying to make the system maximally fast AND scalable AND secure AND simple AND portable.
**Why:** Characteristics conflict.
**The fix:** Pick 3-7 critical to business success. Accept "good enough" on the rest.

### Big Ball of Mud

No discernible structure. Components instantiate each other freely.
**Why:** Every change is risky; impact analysis impossible.
**The fix:** Adopt one of the named styles. Enforce its boundaries.

### Architecture Sinkhole

Most requests pass through all layers performing trivial work.
**Why:** Style mismatch — domain doesn't decompose into layers naturally.
**The fix:** Switch to domain partitioning, microkernel, or service-based.

### Distributed Monolith

Multiple services that must deploy together; tight coupling via shared DB or schema.
**Why:** All operational cost of distribution, none of the independence benefits.
**The fix:** Either consolidate to monolith with good modularity, OR truly decouple.

### Saga Without Compensation Planning

Implementing happy path of multi-service transactions; hoping nothing fails.
**Why:** Failures will happen; without compensating actions, system enters inconsistent states.
**The fix:** Design compensating actions for every step *before* implementing.

### Premature Service Mesh

Adopting Istio for a 3-service system "for the future."
**Why:** Operational complexity exceeds benefits.
**The fix:** Use simple sidecars first. Adopt service mesh when service count justifies.

### God Orchestrator

Central orchestrator that knows about every service and every workflow.
**Why:** Becomes a god-service; single point of complexity.
**The fix:** Multiple smaller orchestrators per business workflow. Or shift to choreography.

### Sharing a Database Across Services

Two microservices accessing the same database. "It's fine, they query different tables."
**Why:** Schema changes break both. Coupling at data layer is the worst kind.
**The fix:** Database-per-service. Duplicate related data via events.

---

## Process Wisdom

### Architecture Decision Records (ADRs)

Every significant decision deserves an ADR. Format:
- **Title:** Short noun phrase
- **Status:** Proposed / Accepted / Superseded
- **Context:** What problem are we solving?
- **Decision:** What did we decide?
- **Rationale:** Why?
- **Consequences:** What are the trade-offs?

**Why ADRs matter:** They're the historical record of how the architecture became
what it is. Without them, future engineers can't tell "intentional" from "incidental."

**Storage:** Wiki, not emails. Single source of truth.

### Last Responsible Moment

Defer decisions until you have enough information to validate, but not so long
that development is held up.

**Practical use:** When pressured to make an architectural decision early,
ask: "Do we have evidence to validate this decision now? If not, what would we
need to know?"

### Iterative Component Identification

Use feedback loop:
1. Identify candidate components from user stories
2. Refine against architectural characteristics
3. Restructure as evidence comes in

Don't try to design the perfect component decomposition upfront.

### Domain Partitioning > Technical Partitioning

The industry trend. Organize services by domain (orders, inventory, payment),
not by technical layer (frontend, backend, DB).

**Why:**
- Bounded contexts are naturally decoupled
- Cross-functional teams own end-to-end flows
- Changes localize within domain boundaries

### Guard Against Overspecification

Avoid building unnecessary brittleness or fragility into designs by being wary
of overspecifying architectural characteristics.

**Example:** Specifying "must support 100K concurrent users" when current load
is 100. The over-spec drives over-engineering.

### Measure Outliers

When measuring operational characteristics like performance, capture maximum
response times to catch outliers — not just averages.

**Why:** Average latency hides p99 spikes that ruin user experience.

---

## When to Apply These Practices

This expert reference complements:

- For ilities and trade-offs → also see `architecture-characteristics-and-tradeoffs/SKILL.md`
- For style selection → also see `architecture-styles-monolithic-and-distributed/SKILL.md`
- For distributed patterns → also see `distributed-system-patterns/SKILL.md`
- For frameworks catalog → see `frameworks.md` in this folder
