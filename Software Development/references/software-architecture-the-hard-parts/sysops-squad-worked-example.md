# The Sysops Squad — Worked Example

The book's running case study. This file distills the cast, setting, per-chapter decisions, and ADRs the team ratifies. Use it when you need a concrete example to ground a method in practice — or to remember what "doing architecture work" actually looks like inside a real-feeling organization.

The full Sysops Squad narrative runs across all 15 chapters. This file gives you 90% of the value at <5% of the page count.

---

## Setting

**Penultimate Electronics** — a large electronics retailer with stores across the country. Customers buy products in store. Some products come with a support contract: an on-site expert ("Sysops Squad expert") will travel to the customer and fix issues.

**Sysops Squad ticketing application** — the system that runs all of this. A monolith built years ago. It's failing.

**The Bad Scenario** (Ch 1):
- Customers complain experts never show up — tickets are lost
- Wrong experts show up — skills/location matching is broken
- The system is frequently unavailable to enter new tickets
- Changes are slow and risky — every deploy breaks something
- The monolith "freezes up" 5 minutes to 2 hours at a time, regularly

If nothing changes, Penultimate Electronics will **abandon the support contract business line** and lay off every Sysops Squad employee — administrators, experts, managers, IT staff, and the architects. The book opens with the architects' jobs literally on the line.

---

## The Four Users (the domain)

| User | Role |
|---|---|
| **Administrator** | Maintains internal users, expert profiles (skills, location, availability), billing processing, reference data |
| **Customer** | Registers, maintains profile, files tickets, fills out post-repair surveys |
| **Sysops Squad expert** | Assigned tickets via mobile app, fixes problems on-site, updates knowledge base |
| **Manager** | Receives operational and analytical reports — financial, performance, ticketing |

---

## The Cast

| Name | Role | First appears |
|---|---|---|
| **Addison** | Architect on the Sysops Squad team | Ch 1 |
| **Austen** | Co-architect on the team | Ch 1 |
| **Logan** | Lead architect for Penultimate Electronics (mentor figure) | Ch 1 |
| **Skyler** | Developer on the team | Ch 5 |
| **Taylen** | Developer on the team | Ch 5 |
| **Dana** | Database team lead — joins decomposition decisions in Ch 6 | Ch 6 |
| **Parker** | Product owner | Ch 1 |
| **Bailey** | Business sponsor — head of the Sysops Squad ticketing application | Ch 1, Ch 15 |
| **Sydney** | Developer on the integration / contracts work | Ch 13 |
| **Sam** | Penultimate Electronics security lead | Ch 7 |
| **Morgan** | Head of marketing — represents skeptical-exec audience in Ch 15 retrospective | Ch 15 |

The case study is told largely through dialogue between these characters. The arguments are the lesson; the conclusions are secondary.

---

## The Per-Chapter Arc

Each chapter ends with a "Sysops Squad Saga" segment where the team applies that chapter's frameworks to a concrete decision. The flow:

### Ch 1 — Introducing the Sysops Squad Saga

Logan is reluctantly pulled in by Addison and Austen. The business is about to kill the product. Logan agrees to help but on one condition: every decision goes through trade-off analysis and gets an ADR. *That's* the contract for the rest of the book.

> "ADR: A short noun phrase containing the architecture decision"
> Context. Decision. Consequences.

This is the only governance discipline the book asks for. Everything else is method.

### Ch 2 — Sysops Squad Saga: Understanding Quanta

Addison and Austen learn to see the monolith as **one architectural quantum**. They had been calling pieces "services" but everything ran in one deploy, shared one DB, and failed together. Quantum vocabulary lets them name the problem without arguing about labels.

### Ch 3 — Sysops Squad Saga: Creating a Business Case

The architects translate their technical problems into the **six modularity drivers**:
- Maintainability: changes ripple unpredictably → broken
- Testability: test suite takes too long → broken
- Deployability: monthly deploys, frequent rollbacks → broken
- Scalability: ticket-entry load spikes drag the system → broken
- Availability: 5min–2hr outages → broken
- Fault Tolerance: one bug stops everything → broken

All six drivers are broken. The business case writes itself: decompose or lose the product line.

### Ch 4 — Sysops Squad Saga: Choosing a Decomposition Approach

The team debates Tactical Forking vs Component-Based Decomposition. Logan argues against the Elephant Migration Anti-Pattern. They inspect the codebase — it *has* identifiable namespaces. Decision: **Component-Based Decomposition**.

> **ADR: Migration Using the Component-Based Decomposition Approach**
> Context: Codebase has identifiable namespaces; team needs iterative, evidence-based migration.
> Decision: Component-Based Decomposition (Ch 5 patterns) over Tactical Forking.
> Consequences: Slower than tactical forking; preserves what works; produces evidence for each step.

### Ch 5 — Sysops Squad Saga (multiple segments — one per pattern)

The team walks the 6 Component-Based Decomposition patterns:
1. **Sizing Components** — inventory by statements of code; prune outliers
2. **Gathering Common Components** — find shared domain logic across components
3. **Flattening Components** — eliminate orphan namespaces
4. **Determining Component Dependencies** — afferent / efferent coupling graph
5. **Creating Component Domains** — Customer, Ticket, Expert, Billing, Reporting, Survey
6. **Creating Domain Services** — promote domains to services when their dependencies are clean

By end of Ch 5, the team has a flat component tree, a dependency graph, and 6 named domains.

### Ch 6 — Sysops Squad Saga: Justifying Database Decomposition

Dana (DBA) joins. The architects realize they should have invited her earlier. Dana is initially skeptical of breaking apart the database. The team walks Dana through **Data Disintegrators vs Data Integrators**: change control wins over referential integrity, scalability differential wins over join queries. Dana proposes the **data domain** concept and the **5-step database decomposition** process.

By end of Ch 6, the team has 6 data domains corresponding to the 6 service domains:
- Customer, Ticket, Expert, Billing, Reporting, Survey

### Ch 7 — Sysops Squad Saga: Ticket Assignment Granularity

Sam (security) joins because expert location data has privacy implications.

The team debates Ticket Assignment granularity. Disintegrators: scalability differential (assignment runs 10× more than other ticket ops), security (sensitive expert location data), code volatility (assignment algorithm changes frequently). Integrators: data dependency (assignment needs ticket + expert + customer data).

> **ADR: Consolidated Service for Ticket Assignment and Routing**
> The disintegrators win; assignment becomes its own service.

### Ch 7 — Sysops Squad Saga: Customer Registration Granularity

Different decision, different forces. Customer registration is low-volume, security-sensitive, but not volatile. Integrators win. Registration stays consolidated.

The lesson: same framework, different forces → different answer. The framework doesn't produce a recipe; it produces a defensible decision.

### Ch 8 — Sysops Squad Saga: Common Infrastructure Logic

Taylen argues authorization should be a **Shared Service**. Skyler argues for **Shared Library**.

Trade-off table:
- Shared Service: high runtime coupling, single source of truth, single point of failure
- Shared Library: low runtime coupling, version skew across services, faster

Decision: **Shared Library** for ticketing DB logic; **Sidecar / Service Mesh** for operational cross-cutting concerns (logging, mTLS, metrics).

> **ADR: Use of a Shared Library for Common Ticketing Database Logic**

### Ch 8 — Sysops Squad Saga: Shared Domain Functionality

Different decision: ticket notification logic. Decided by the same framework but lands on **Shared Library** for a different reason — the notification code is small, stable, and the consistency requirements are low.

### Ch 9 — Sysops Squad Saga: Data Ownership

For each table → which service owns it?

> **ADR: Single Table Ownership for Bounded Contexts**
> Every table has exactly one writer.
> Exceptions documented separately as joint-ownership decisions.

> **ADR: Survey Service Owns the Survey Table**
> Customer Service reads survey data via inter-service call.

The decision tree is mechanical: walk every table, identify the writer(s), default to single ownership. Where multiple writers exist, name the resolution pattern.

### Ch 10 — Sysops Squad Saga: Expert Profile Data Access

Multiple services need expert profile data (Ticket Assignment, Notification, Mobile API). Reads are high-volume. Expert Service owns the data.

Trade-off:
- **Inter-Service Communication** — every read = network call. Latency too high at scale.
- **Column Schema Replication** — replicate profile columns into each consumer. Operational complexity for replication.
- **Replicated Cache** — in-memory cache (Apache Ignite). Fast reads, eventual freshness.
- **Data Domain** — sharing two services on one DB. Couples the services.

> **ADR: Use of In-Memory Replicated Caching for Expert Profile Data**
> Apache Ignite. Reads are high-volume; staleness of seconds is tolerable; no coupling between services.

### Ch 11 — Workflow: Ticket Management

The team designs ticket workflow coordination. Choreography becomes hard above 4 participants — and ticket flow involves 6 services (Ticket, Assignment, Expert, Notification, Survey, Audit). Decision: **orchestration** via a Ticket Orchestrator service.

Then a separate question: what consistency? Atomic across all 6 → too coupled, too brittle. Eventual is fine — the business tolerates "the survey email goes out 3 seconds after the ticket closes."

### Ch 12 — Transactional Sagas: The Big Pick

Combined: synchronous? async? The team picks **asynchronous** to avoid coupling assignment latency to notification latency. Combined with **eventual** consistency and **orchestrated** coordination →

> **Parallel Saga (aeo)** — async, eventual, orchestrated, **low coupling**.

This is the modern microservices default the book recommends. The Sysops Squad team lands there *via the trade-off analysis*, not because someone said "use sagas."

### Ch 13 — Sysops Squad Saga: Expert Mobile App Contract

Addison meets Sydney to design the contract between the Ticket Orchestrator and the expert mobile app.

Sydney proposes gRPC. Addison: "That's implementation, not architecture. First decide strict vs loose."

Trade-off:
- Strict: catches errors early, mobile app must update with every contract change, app store delays make this painful
- Loose: app survives field additions; some errors deferred to runtime

> **ADR: Loose Contract for Sysops Squad Expert Mobile Application**
> Reason: mobile deployment cadence is much slower than backend; loose contract protects the mobile app from server-side evolution.

For *internal* service-to-service contracts: strict (Protobuf). For *mobile boundary*: loose (JSON, name-value-pairs).

### Ch 14 — Analytical Data

Manager reporting (financial, ticketing, performance) becomes a **Data Product Quantum** owned by the same team that owns the operational data. No central data team intermediary.

### Ch 15 — Build Your Own Trade-Off Analysis (the Retrospective)

**Monday, June 10, 10:01 AM.** Nine months after the book opens. The same conference room. Bailey, the business sponsor who almost killed the product, opens the meeting.

The Sysops Squad business line is healthy. Tickets aren't lost. Experts arrive on time. Deploys are frequent and routine. Outages have moved from "hourly" to "rare." Bailey wants to know what changed.

The architects answer in turns:

- **Addison**: We learned to analyze trade-offs. Logan's discipline.
- **Dana**: We started collaborating across teams. Database team and application team finally talked.
- **Austen**: We looked at business drivers, not just technical aspects.

Morgan, the head of marketing, asks the question that closes the book:

> "But isn't that just adding a lot of extra process and procedures to the mix?"

Logan answers:

> "No. That's architecture. And as you can see, it works."

That is the book's thesis in one exchange. *Architecture is the discipline of explicit trade-off analysis.* Skip it on one decision and the next architect can't tell intentional from incidental.

---

## ADR Index (the team's actual decisions)

The book contains these named ADRs by chapter. Each is a worked example of the trade-off analysis method applied to a real-feeling decision.

| Ch | ADR | Skill that teaches the underlying method |
|---|---|---|
| 4 | Migration Using the Component-Based Decomposition Approach | `service-and-data-decomposition` |
| 7 | Use of Document Database for Customer Survey | `scalable-database-design-and-sharding` |
| 7 | Consolidated Service for Ticket Assignment and Routing | `service-granularity-forces` |
| 8 | Use of a Shared Library for Common Ticketing Database Logic | `code-reuse-in-distributed-systems` |
| 9 | Single Table Ownership for Bounded Contexts | `data-ownership-and-distributed-data` |
| 9 | Survey Service Owns the Survey Table | `data-ownership-and-distributed-data` |
| 10 | Use of In-Memory Replicated Caching for Expert Profile Data | `data-ownership-and-distributed-data` |
| 12 | (Implicit) Parallel Saga (aeo) for Ticket Workflow | `distributed-workflows-and-sagas` |
| 13 | Loose Contract for Sysops Squad Expert Mobile Application | `service-contracts-and-coupling` |

Reading the ADRs in order is a mini-course in applying the book's method. Each is short, defensible, and shows the trade-off table behind it.

---

## Translating Sysops Squad to Your System

A template for using this case study to ground a real decision in your own architecture.

1. **Find the analog.** Which of your services maps to Ticket? Customer? Expert? Survey? You probably have all four shapes (transactional entity, profile entity, assignment-routing entity, post-event survey entity).
2. **Find the analog forces.** Where in your system are the same disintegrators / integrators present?
3. **Lift the ADR.** Which Sysops Squad ADR has the same forces as your decision? Read its trade-off table.
4. **Re-derive, don't copy.** Don't copy the Sysops Squad decision. Re-run the method with *your* forces. You'll often land elsewhere, and that's the point — the method, not the answer, transfers.
5. **Write your ADR in the same shape.** Context · Decision · Consequences. With a trade-off table.

The Sysops Squad team didn't pick Parallel Saga because "the book said so." They derived it from a specific axis assignment driven by their specific business requirements. Your axes will differ. Your saga will differ. The method is the constant.

---

## Why this case study is the book's best feature

Most architecture books leave you with patterns. *The Hard Parts* leaves you with the experience of *arguing* about patterns. The Sysops Squad dialogues show:

- How architects push back on each other (Skyler vs Taylen on shared service vs shared library)
- How teams bring in late stakeholders (Dana the DBA in Ch 6, Sam the security lead in Ch 7)
- How business sponsors react to architecture discipline (Bailey almost killed the product in Ch 1, defends it in Ch 15)
- How "discipline" feels from the outside (Morgan's question: *"isn't that just process?"*)

If you only read one chapter's case study, read **Ch 15's retrospective**. It's 4 pages, and it's the only place in the architecture-book literature where the *business* tells the architects, in their own words, what trade-off analysis did for the business.
