---
name: api-design-and-evolution
description: >
  Apply API-First design with ADRs, C4 diagrams, Consumer-Driven Contracts,
  the Test Pyramid + Test Quadrant, evolutionary architecture, fitness
  functions, and migration patterns (Strangler Fig, Facade, Adapter, Modules,
  Seams). Use when designing a new API, evolving an existing one, migrating a
  legacy system to APIs, deciding what to ADR, or setting up consumer
  contract testing. Triggers: "design an API", "API-First", "consumer-driven
  contracts", "Strangler Fig migration", "fitness function", "ADR template",
  "C4 diagram for API", "evolve API without breaking consumers". Produces a
  designed API + evolution strategy with rationale documented.
---

# API Design and Evolution

You apply Bernardez & Olejár's *Mastering API Architecture* methodology:
APIs are first-class artifacts, designed with consumers, evolved without
breaking them, and migrated incrementally via Strangler Fig + Facade/Adapter.

---

## When to Use This Skill

- Designing a new API from scratch
- Evolving an API that has consumers
- Migrating a monolith to APIs (Strangler-Fig style)
- Setting up consumer contract testing
- Documenting architecture decisions (ADR)
- Establishing fitness functions for API quality

---

## API-First Design

**The principle:** Design the API before implementation. Treat it as the most public, durable artifact.

```
API as a contract  ──►  Implementation can change
                        Consumers don't notice
                        New providers can swap in
```

### Workflow
1. Identify consumers and their actual needs (not assumed needs)
2. Design endpoints in OpenAPI / AsyncAPI spec
3. Review with at least one prospective consumer
4. Generate stub server + client code from spec
5. Implement against the stub
6. Validate consumer contracts via CDC (see below)

### Spec-driven artifacts
- **Mock server** from spec for early consumer integration
- **Client SDKs** generated for languages consumers use
- **Documentation** auto-generated from spec
- **Contract tests** validating provider matches spec

---

## C4 Model Diagrams

```
LEVEL 1: Context  ──► The system + its actors at the highest level
LEVEL 2: Container  ──► Major technical pieces (API gateway, services, DBs)
LEVEL 3: Component  ──► Internal modules within a service
LEVEL 4: Code  ──► Class-level (rarely used; often skipped)
```

For APIs, **Container and Component diagrams matter most.** They show the API's place in the architecture and how request flow works internally.

**Use when:** Architecture documentation. ADR illustrations. New-team onboarding. Stakeholder communication.

---

## Architecture Decision Records (ADRs)

Lightweight markdown documents capturing decisions:

```
# ADR-005: Use REST over gRPC for public API

## Status: Accepted (2024-03-15)

## Context
Public API consumers include diverse clients (web, mobile, partners).
gRPC offers performance benefits but limits browser/JS clients.

## Decision
Use REST/JSON for the public API. Reserve gRPC for internal services.

## Consequences
- Wider consumer compatibility
- Slightly higher latency vs gRPC
- Manual schema management (vs gRPC's protobuf compiler)
- Internal services can still use gRPC for east-west traffic
```

**Why ADRs:**
- Future engineers see *why*, not just *what*
- Decisions are deliberately made, not accidentally inherited
- "What were they thinking?" becomes answerable

**ADR discipline:**
- One ADR per decision
- Status: Proposed → Accepted → Deprecated → Superseded (link forward)
- Stored in version control alongside code
- Reviewed in PRs

---

## Consumer-Driven Contracts (CDC)

```
Consumer ──submits contract──► Producer
                                │
                                ▼
                       Producer runs CDC tests
                       in CI; failure blocks deploy
```

**The pattern:** Consumer specifies expected interactions. Producer's CI verifies it can satisfy them. Both parties confirm before integration.

**Tools:** Pact, Spring Cloud Contract, Postman API Network.

**Why it matters:** Producer changes that would break consumers are caught at producer's CI, not after deployment.

**When to use:** Multiple consumers; producer doesn't know all consumers; want to evolve API safely.

---

## Test Pyramid (for APIs)

```
         /\         END-TO-END / UI
        /  \        (few; expensive; brittle)
       /────\
      /      \      SERVICE / INTEGRATION
     /        \     (medium; API-level tests)
    /──────────\
   /            \   UNIT / COMPONENT
  /              \  (many; fast; isolated)
 /________________\
```

**Apply to APIs:**
- Unit tests for handler logic
- Service tests calling the API in-process or via local container
- E2E tests for critical user journeys only

**Anti-pattern:** Inverted pyramid (mostly E2E, few unit) — slow, brittle, hard to debug.

---

## Test Quadrant

```
              BUSINESS                 TECHNOLOGY
              ─────────                 ──────────
SUPPORTING   │ Q2: Functional         Q1: Unit + 
TEAM         │ acceptance, story       Component
             │ tests, examples         tests
             │
CRITIQUE     │ Q3: Exploratory,       Q4: Performance,
PRODUCT      │ user journey, UAT       resilience, security
```

Use to ensure your test portfolio covers all four quadrants — not just unit + integration.

---

## Evolutionary Architecture

**The principle:** Architecture is a journey, not a destination. Design for change.

### Fitness Functions

Quantifiable metrics gate architecture quality, integrated into CI:

| Dimension | Example fitness function |
|---|---|
| Performance | "p99 latency < 200ms on /search endpoint" |
| Resiliency | "Service recovers within 30s of dependency failure" |
| Code quality | "Cyclomatic complexity per function < 15" |
| Security | "No high-severity CVEs in dependencies" |
| Operability | "Logs include correlation ID on every request" |
| Coupling | "No service depends on more than 5 others" |

**CI pipeline runs fitness functions** alongside tests. Failure blocks merge.

### Modules and Seams

**Module:** A well-defined boundary that hides implementation. For APIs:
- **Controller** — HTTP / serialization
- **Service** — business logic
- **Data Access Object (DAO)** — persistence

**Seam:** Where you can substitute one implementation for another (testing, refactoring).

```
Controller ──seam──► Service ──seam──► DAO ──seam──► Database
            (DI for                  (Repository
             test fakes)              pattern)
```

Seams enable:
- Unit tests with fakes
- Refactoring (swap DAO from Postgres to DynamoDB without touching Service)
- Contract testing (test Controller against Service contract, not real DB)

---

## Migration Patterns

### Strangler Fig

```
t=0                  t=1                          t=2
─────                ─────                        ─────

[Legacy           [Legacy ◄── shrinking]         [Legacy retired]
  Monolith]            │
                       │  ┌── New endpoint A
                       └─►│
                         └── New endpoint B
                          (via Facade)
```

Wrap legacy with a facade. Route portions of traffic to new components. Shrink legacy.

### Facade Pattern

```
Consumer ──► [Facade API] ──► Legacy backend
                          OR
                       New backend
```

Facade hides whether the request is served by legacy or new. Migration is invisible to consumers.

### Adapter Pattern

```
Modern API ──► [Adapter] ──► Legacy SOAP / RPC / proprietary protocol
```

Adapter converts between modern (REST/JSON) and legacy (SOAP/XML) representations. Legacy clients can be modernized incrementally.

### Layered APIs ("API Layer Cake")

```
Presentation API
      │
Application API
      │
Domain API
      │
Datastore API
```

**Pro:** Separation of concerns.
**Con:** Often produces high coupling between adjacent layers; performance penalty from N hops.

**Practical guidance:** Use for genuinely complex domains. Avoid as a default — it's often over-engineered.

---

## Cloud Migration Strategies (the 6+ R's)

| Strategy | Mechanics | Use when |
|---|---|---|
| **Rehost (Lift-and-shift)** | Move VMs to cloud unchanged | Quickest path; minimal value |
| **Replatform** | Lift-and-shift + swap to managed services (e.g., RDS instead of self-hosted MySQL) | Reasonable middle ground |
| **Refactor / Re-architect** | Reimagine using cloud-native features | Genuine cloud benefits required |
| **Repurchase** | Replace with SaaS | Commodity domain |
| **Retire** | Decommission | Service no longer needed |
| **Retain (or Revisit)** | Do nothing; revisit later | Cost of migration > benefit |

---

## Principles

- **Design APIs before implementing them.** Spec-driven.
- **Document decisions in ADRs.** Status: Proposed → Accepted → Deprecated → Superseded.
- **Consumer-Driven Contracts** to evolve safely.
- **Fitness functions** to keep architecture from rotting.
- **Strangler Fig for migrations.** Never big-bang.
- **High cohesion, loose coupling** as the dominant design property.
- **Information hiding** via stable APIs that wrap changeable internals.
- **Modules and seams** so testing and refactoring stay tractable.
- **Statelessness** at API boundaries — consumer carries state when needed.

---

## Anti-Patterns

### API Designed by Implementers Without Consumer Input

**Looks like:** Backend team designs endpoints based on database schema. Consumers struggle to use it.

**Why it fails:** API mirrors implementation, not consumer needs. Becomes hard to evolve as implementation changes.

**The fix:** Consumer interviews. API-First. Mock server for early feedback.

### "We'll Document Decisions Later"

**Looks like:** Six months in, "why did we do it this way?" — nobody knows.

**Why it fails:** Decisions become tribal knowledge that walks out the door.

**The fix:** ADR per decision. Lightweight. PR-reviewed.

### No CDC; Producer "Tries Not to Break Consumers"

**Looks like:** Producer changes behavior. Hopes nothing breaks. Sometimes finds out at customer escalation.

**Why it fails:** No automated detection of breaking changes.

**The fix:** Consumer-Driven Contracts in CI. Producer's CI runs each consumer's contract.

### Inverted Test Pyramid

**Looks like:** Most tests are E2E. Slow CI. Flaky failures. Hard to debug.

**Why it fails:** E2E tests are expensive and brittle. The pyramid balances cost.

**The fix:** Restructure. Most tests are unit; medium service-level; few E2E.

### Layered APIs Across Network Boundaries

**Looks like:** Controller calls Service-via-network calls Domain-via-network calls DAO-via-network. 4 hops per request.

**Why it fails:** Latency multiplies. Failure modes proliferate. Operational burden.

**The fix:** Layers within a service (in-process). Across services, use clear boundaries (microservices) — not arbitrary tier slicing.

### Strangler Without Routing Investment

**Looks like:** "Let's strangle the monolith" without an API gateway / facade. Each migrated piece requires app-level changes.

**Why it fails:** Strangler Fig requires a routing layer to direct traffic. Without it, every migration is invasive.

**The fix:** Invest in routing first (gateway, load balancer with route rules, or proxy). Then strangle.

### Big-Bang Cloud Migration

**Looks like:** Lift the entire monolith to AWS in one weekend.

**Why it fails:** Surprise pitfalls in production. No rollback path. High risk concentrated.

**The fix:** Strategy per service (6+ R's). Migrate incrementally. Replatform first, refactor later if warranted.

### Fitness Functions as One-Off Documents

**Looks like:** "Architecture quality KPIs" in a Confluence doc nobody reads.

**Why it fails:** Goals without enforcement drift.

**The fix:** Fitness functions in CI. Failures block merge. They're code, not docs.

### ADRs Without Status Hygiene

**Looks like:** ADR-005 says "Use REST"; ADR-015 says "Use gRPC". Both Accepted. Confusion.

**Why it fails:** ADRs accumulate without supersession discipline.

**The fix:** When superseding, mark old ADR as Superseded and link forward.

---

## Decision Rules

| Situation | Action |
|---|---|
| New API, multiple consumers expected | API-First; design before implementing |
| Need to communicate architecture | C4 Container + Component diagrams |
| About to make a sticky decision | Write an ADR. Even if "obvious" now. |
| Multiple consumers, want to evolve safely | Consumer-Driven Contracts in CI |
| Test suite slow + flaky | Audit pyramid shape; usually E2E-heavy |
| Architecture rotting over time | Adopt fitness functions; CI-enforce |
| Migrating a legacy system | Strangler Fig + Facade. Never big-bang. |
| Need new API for legacy backend | Adapter pattern; modern API → legacy |
| Cloud migration | Pick strategy per workload; 6+ R's |
| Refactoring a service | Identify seams (DI / Repository); test through seams |
| Statefulness creeping into API | Push state to consumer (token, header) — keep API stateless |
| API design feels DB-coupled | Step back; design from consumer perspective |
| Want to switch DB without breaking API | Information hiding via DAO seam |
| Architecture decision affects future | Write ADR; PR-review |
| ADRs proliferating | Quarterly cleanup; supersede stale ones |

---

## Worked Example: Migrating a Monolith to API-First Microservices

**Context:** 8-year-old Java monolith. 50 engineers. New mobile app drove API needs. Decided to extract APIs incrementally.

**Approach:**

| Step | Action |
|---|---|
| 1 | Set up API gateway in front of monolith. All traffic routed through it. |
| 2 | Identify first extraction target: User Profile (well-bounded, high read traffic) |
| 3 | API-First: design new `/v1/users/{id}` endpoint in OpenAPI. Mock server. Mobile team integrates against mock. |
| 4 | New User service implementation. Adapter to read from monolith DB until cutover. |
| 5 | Gateway routes `/v1/users/*` to new service. Monolith's user code can be deleted. |
| 6 | CDC tests: mobile + web teams have Pact contracts. Producer CI runs both. |
| 7 | ADRs documented for: gateway choice, OpenAPI standardization, Pact for contracts. |
| 8 | Repeat 2-7 for next bounded context. |

**Fitness functions adopted:**
- p99 latency on extracted services < 150ms
- Test coverage > 80%
- No service depends on more than 4 other services
- All public endpoints have OpenAPI specs in repo
- All ADRs reviewed within 7 days

**Result:** 18 months in, 12 services extracted. Monolith is 30% of original size. Mobile team unblocked.

**Lesson:** The investment in API gateway + CDC up front made each subsequent extraction routine. Without it, every extraction would be bespoke.

---

## Gotchas

- **OpenAPI ≠ REST best practice.** OpenAPI describes any HTTP API; you can describe a non-RESTful API in OpenAPI. Verify the API itself follows REST principles separately.
- **Pact requires consumer cooperation.** If consumers won't write contracts, CDC degrades to producer-side schema tests.
- **Mock servers drift from real implementation.** Integration tests against the mock should be supplemented by tests against a real instance periodically.
- **Strangler routing layer is non-trivial.** Path-based routing is easy; header / weight-based routing requires more sophisticated gateways.
- **Fitness functions can become bureaucratic.** Start with 3-5; expand. 30 fitness functions = 30 ways to block merges.
- **ADR template debates** are a productivity sink. Pick one (Michael Nygard's classic, MADR, or your own). Don't litigate format.
- **C4 Level 4 (Code) is rarely useful.** UML class diagrams. Skip unless you have a specific need.
- **Layered APIs ≠ N-tier architecture.** Layered APIs is a specific anti-pattern; N-tier is general (and fine).

---

## Further Reading

- *Mastering API Architecture* by Bernardez & Olejár (O'Reilly)
- *Building Evolutionary Architectures* by Ford, Parsons & Kua — fitness functions
- C4 model documentation (Simon Brown) — c4model.com
- Pact documentation — for CDC
- See `api-gateway-and-service-mesh` for gateway and mesh patterns
- See `api-security-and-lifecycle` for security, OAuth, observability

Source: *Mastering API Architecture* (Bernardez & Olejár, O'Reilly).
