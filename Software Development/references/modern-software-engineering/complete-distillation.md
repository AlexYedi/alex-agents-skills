# Complete Distillation: Modern Software Engineering

**Source:** *Modern Software Engineering* by Dave Farley
**Distilled:** 2026-04-28
**Domain:** Software Engineering Discipline, Continuous Delivery, Modularity
**Pages processed:** ~190 (full book)

This is the all-encompassing single-document view of this book. Use it when
you want everything in one place rather than navigating skills + references.

---

## Executive Summary

Dave Farley's book is a manifesto for treating software engineering as an
empirical, scientific discipline. The author co-wrote *Continuous Delivery*
(2010) and built the LMAX trading platform — one of the highest-throughput,
lowest-latency systems ever produced — using the practices he advocates.

The book's central thesis: most teams treat software engineering as craft or
art; this leaves performance gains on the table. Engineering means measurement,
hypothesis testing, mistake-detection-at-minimum-cost, and disciplined process
control.

It is structured around two sets of practices:
1. **Iterative practices:** how you work day-to-day (CI, CD, TDD, fail fast, shift-left)
2. **Modularity principles:** how you design (cohesion, coupling, ports & adapters, YAGNI)

Both sets compose. Bad practices produce bad code regardless of design skill;
good practices on bad design hit ceilings. You need both.

The voice is direct, often contrarian, and grounded in measurement. Farley
challenges sacred cows (defensive coding, big upfront design, "we'll write
tests later") with both reasoning and personal experience.

---

## The Big Takeaways

1. **Software engineering is the process, culture, and philosophy — not just the code.** Code reviews, deployment cadence, team structure, and feedback loops shape outcomes more than any framework choice.

2. **Mistakes are inevitable; optimize for cheap detection.** Don't try to prevent mistakes — that's impossible. Optimize for fast feedback that catches them at minimum cost.

3. **Eval (test) BEFORE feature.** TDD applied to AI = eval-driven development. The pattern is universal: define how you'll know if it works *before* building it.

4. **CI is a discipline, not tooling.** Multiple merges per day per developer; sub-10-minute feedback; broken main = stop everything. If you don't have these, you don't have CI.

5. **CD is the destination; CI is the prerequisite.** "Always in a releasable state" is the goal. Big-bang deployments concentrate risk.

6. **Modularity is the dominant complexity lever.** Apply recursively (fractal modularity). High cohesion + loose coupling at every scale.

7. **Separate essential from accidental complexity.** Domain logic ≠ database/framework/HTTP code. The latter must never infect the former. Ports & Adapters is the canonical pattern.

8. **YAGNI ruthlessly.** Speculative generality adds complexity for hypothetical futures that often don't arrive.

9. **Microservices are a destination, not a start.** Distributed monolith is worse than well-modularized monolith. Earn the right to distribute.

10. **Empirical, not theoretical.** Base decisions on evidence, not fashion. "Adopt X because everyone does" is a failure mode.

---

## Skills Derived From This Book

Located in `Software Development/`. Each is a self-contained action-focused skill.

| Skill | When to invoke | Source coverage |
|---|---|---|
| `iterative-engineering-practices` | Setting up CI/CD/TDD; deciding feedback loop investments; shift-left strategy; fail-fast vs defensive coding | Iterative practices chapters |
| `software-modularity-principles` | Designing module boundaries; ports & adapters refactoring; choosing abstraction level; YAGNI judgment calls; identifying essential vs accidental complexity | Modularity principles chapters |

---

## Frameworks Index (See `frameworks.md` for Detail)

Quick reference. Detailed catalog in `frameworks.md`.

**Foundations:**
- The Three Laws of Software Engineering (Farley's framing)
- Empirical Process Control
- Scientific Rationality in Software
- Engineering ≠ Code mindset

**Iterative Practices:**
- Continuous Integration (CI)
- Continuous Delivery (CD)
- Test-Driven Development (TDD)
- Behavior-Driven Development (BDD)
- Shift-Left
- Fail Fast / Fail Safely
- Mechanical Sympathy
- Working Iteratively
- Incrementalism
- Optimize for Learning
- Production Is Not Our Problem (mindset)

**Modularity Principles:**
- Modularity (concept)
- High Cohesion, Loose Coupling
- Cohesion / Coupling
- Separation of Concerns
- Information Hiding
- Fractal Modularity
- YAGNI (You Ain't Gonna Need It)
- Testability as a Design Driver
- Levels of Indirection
- Strict Modularity / Low Tolerance for Complexity
- Law of Demeter

**Architectural Patterns:**
- Ports & Adapters (Hexagonal Architecture)
- Domain-Driven Design (DDD)
- Bounded Contexts
- Anti-Corruption Layer
- Microservices
- Domain-Specific Languages (DSL)
- Layers of Isolation
- Domain Partitioning vs Technical Partitioning

**Discovery / Process:**
- Event Storming
- Iteration (concept)
- Stakeholder Alignment
- Last Responsible Moment
- Single Source of Truth

**Org Design:**
- Decouple Teams and Systems
- BAPO (Business Architecture Process Organization)
- Conway's Law / Inverse Conway

**CD Infrastructure:**
- Deployment Pipeline

**Mindset:**
- Design Engineering

---

## Best Practices Index (See `additional-experts.md` for Detail)

Quick reference. Detailed expert voice in `additional-experts.md`.

**Mindset shifts:**
- Software engineering is not the code
- Treat development as scientific method (hypothesis → prediction → experiment → falsification)
- Mistakes are inevitable; optimize for fast cheap detection

**CI / CD / TDD:**
- CI is discipline, not tooling — multiple merges per day; sub-10-min feedback
- Cost of slow feedback compounds nonlinearly
- TDD is design discipline, not testing discipline (Red-Green-Refactor)
- CD is the destination; deployment becomes a non-event
- Shift-left: catch defects earlier; cost ladder $1 → $10 → $100 → $1000

**Modularity:**
- Apply recursively (fractal)
- High Cohesion + Loose Coupling at every scale
- Separate essential from accidental complexity
- Information hiding as design discipline
- YAGNI: build for current needs, refactor when 2nd use case appears

**Distributed systems:**
- Domain partitioning > technical partitioning
- Decouple teams and systems (Inverse Conway)
- Microservices as destination, not start
- Event Storming for domain identification

**Empirical:**
- Base decisions on evidence, not fashion
- Control variables (version control, testing, IaC, feature flags)
- Fail Fast — don't swallow errors

**Code review:**
- Focus on whether the change advances learning, not on style
- Style enforced by formatters, not reviewers
- Ask "is this the right shape?" not "is this idiomatic?"

**Refactoring:**
- Small steps; tests pass after each
- Don't combine refactoring with feature work
- Refactor to enable a feature; ship the feature; then move on

**Postmortems:**
- Blameless: focus on systemic causes
- Output should change the system, not just the people
- Track action items; verify done

---

## Decision Rules Consolidated

Every named "if X, do Y" rule across the two skills:

### From iterative-engineering-practices

| Condition | Action |
|---|---|
| CI feedback time > 10 min | P0: stop adding features; fix CI |
| Broken main build | Stop everything until fixed |
| Adding new feature | Define test first (TDD Red) |
| Test is hard to write | The design is wrong; refactor for testability |
| Defect found | Fix it where it was caught; trace upstream to prevent recurrence |
| Production failure | Fail fast; surface to handler; don't swallow |
| Environment difference | Make environment as code; same config dev/staging/prod |
| Deployment | Continuous Delivery; ship small increments often |

### From software-modularity-principles

| Condition | Action |
|---|---|
| Designing new module | High cohesion + loose coupling |
| Identifying complexity source | Separate essential (domain) from accidental (infra) |
| Tempted to add abstraction layer for hypothetical future | Apply YAGNI; don't add until 2nd use case appears |
| Module's domain code imports framework code | Refactor to ports & adapters; isolate via interfaces |
| Test requires live DB / network | Decouple via dependency injection; use fake adapter |
| Multi-domain monolith struggling | Apply Bounded Contexts via Event Storming |
| Considering microservices | Verify: domain teams, scaling needs, ops maturity, clear contexts. Otherwise → modularize monolith first. |
| Function spans multiple abstraction levels | Refactor; each function operates at one level |
| Shared dependency between modules causing change ripples | Apply Anti-Corruption Layer or extract interface |

---

## Anti-Patterns Consolidated

Every named anti-pattern across the two skills:

### Iterative Practices Anti-Patterns

- **Long-Lived Feature Branches** — branches living for weeks, merged as massive PRs
- **Defensive Coding Everywhere** — every function checks every input; null checks proliferate
- **Big-Bang Deployment** — months of work shipped in one deploy; high anxiety
- **Skipping CI Discipline** — having Jenkins/CircleCI/GitHub Actions but breaking the discipline (slow feedback, broken main not stopping work)

### Modularity Anti-Patterns

- **God Object / God Module** — one class doing everything; thousands of lines
- **Speculative Generality** — premature abstraction for hypothetical future needs
- **Leaking Abstractions** — domain code expressing implementation details
- **Inconsistent Abstraction Levels** — function mixing high-level orchestration with low-level details
- **Premature Microservices** — splitting before justified

---

## Worked Examples Consolidated

### From iterative-engineering-practices
- **Refactoring Legacy Service to Iterative Practices** — 7-step incremental adoption: CI build → seam tests → deploy pipeline → port-and-adapter extraction → automated acceptance → CD on subsystem → expand. Lesson: iterative practices include adopting iterative practices iteratively.

### From software-modularity-principles
- **Refactoring Tightly-Coupled Order Service** — 7-step: identify essential vs accidental → define ports → move logic to pure domain → implement adapters → fast unit tests with fakes → integration tests for adapters. Lesson: most "monolithic service is unmaintainable" complaints are really "domain and infrastructure are tangled."

---

## Notable Content NOT in Skill Files

These are insights from the book's content that didn't make it into action-focused
skills but are worth preserving.

### Mechanical Sympathy

Farley borrows this term from racing (Jackie Stewart) via Martin Thompson's
software work. The principle: align technical tools, processes, and design
with the underlying hardware and human cognitive capabilities.

In practice:
- Cache-friendly data structures (arrays of structs vs structs of arrays) can be 10-100x faster than algorithmically-equivalent designs
- Awareness of memory hierarchy (L1 cache, L2, RAM, disk, network)
- Designs validated through measurement, not assumption

Particularly important for high-performance systems (the LMAX context where
Farley developed many of these ideas). Less critical for typical web apps,
but the mindset transfers.

### Domain-Specific Languages (DSL)

Briefly covered in the book. DSLs are narrowly-focused languages or graphical
representations that hide detail and raise abstraction level. Examples:
- SQL for data queries
- Regex for pattern matching
- Build files (Makefile, Bazel BUILD)
- Internal DSLs in code (e.g., RSpec's matchers)

Useful when:
- Domain has clear vocabulary
- Many similar operations need to be expressed
- Operators differ from general-purpose code maintainers

Captured in `frameworks.md` for completeness.

### BAPO vs OBAP (Org Design)

BAPO = Business → Architecture → Process → Organization
OBAP = Organization → Business → Architecture → Process

BAPO is the *correct* order for setting up a software org:
1. Define business vision and goals
2. Define architecture that serves the business
3. Define processes that enable the architecture
4. Organize teams to fit processes

OBAP is the *common* (problematic) approach:
1. Start with current org chart
2. Bend business vision to fit the org
3. Force architecture to match the org
4. Force processes to bridge the mismatch

Most companies are stuck in OBAP. Recognizing this is the first step toward
correcting it.

### Layers of Isolation (Layered Architecture detail)

Property of layered architecture where changes in one layer should not impact
others if contracts remain unchanged.

Caveat from book: major request flows often violate strict layer isolation in
practice. Open layers (where some can be bypassed) reduce isolation but
increase flexibility. Trade-off requires deliberate decision per system.

### Production Is Not Our Problem (mindset)

Triggering a build = "production" in the engineering sense. The deployment is
a result of practices, not a separate event to fear.

This is a counterintuitive framing. Most teams think "production = scary." The
mindset shift: if your engineering practices are right, production is just
another step in your pipeline. If you fear production, your practices need work.

### Optimize for Learning

The book frames feedback as the primary product of engineering. Build practices
that maximize feedback speed and quality. Better software emerges as a side
effect.

This reframes prioritization: between two options, prefer the one that gives
faster, clearer feedback even if slightly less elegant.

### Hiring Wisdom

From the additional-experts.md, worth surfacing:
- Hire for engineering judgment, not knowledge of specific frameworks
- Frameworks change; engineering principles don't
- Test for testability mindset, modularity instincts, willingness to delete code

The "willingness to delete code" criterion is unusual but important. Engineers
who can't delete struggle with modularity (because deletion is a key tool for
reducing coupling).

---

## Redundant Content with Existing Repo

Items the book covers that overlap with existing skills.

| Topic from book | Already covered by | Notes |
|---|---|---|
| General architecture decisions | `Software Development/cto-architect/` | Existing skill is broader; book is more focused on engineering practices. Use `cto-architect` for tech strategy; book for engineering discipline. |
| Engineering testing strategy | `engineering:testing-strategy` (system skill) | Book extends testing into TDD discipline; existing covers testing strategy generally. |
| Code review | `engineering:code-review` (system skill) | Book has philosophical takes; existing skill is mechanical (security, performance, correctness). Complementary. |
| Architecture decisions | `engineering:architecture` (system skill) | Existing skill is ADR template; book is the "why ADRs matter" thinking behind it. |
| System design | `engineering:system-design` (system skill) | Existing skill is for designing new systems; book is broader (modularity at all scales). |
| Tech debt | `engineering:tech-debt` (system skill) | Both relate; book frames as "how to never accumulate debt"; existing skill is "how to manage existing debt." |
| Debug | `engineering:debug` (system skill) | No direct overlap; book doesn't cover debugging tactics. |
| Standup | `engineering:standup` (system skill) | No overlap. |
| Documentation | `engineering:documentation` (system skill) | No overlap. |
| Incident response | `engineering:incident-response` (system skill) | Tangentially: book covers fail-fast and postmortem mindset; system skill is operational. |
| Deploy checklist | `engineering:deploy-checklist` (system skill) | Both relate to CD; existing is checklist; book is the discipline behind it. |

---

## Recommended Reading Order

If you're new to this book's distilled content:

### Foundation
1. Read this `complete-distillation.md` for the overview
2. Skim `frameworks.md` (alphabetical index)
3. Skim `additional-experts.md` for Farley's voice — it's distinctive and worth absorbing

### Core skills
4. Invoke `iterative-engineering-practices` when setting up dev workflow
5. Invoke `software-modularity-principles` when designing or refactoring

### Companion reading
- For specific architecture decisions, also see `cto-architect` (existing) and `architecture-styles-monolithic-and-distributed` (from Software Architecture Fundamentals distillation)
- For test strategy, see `engineering:testing-strategy`
- For ADR mechanics, see `engineering:architecture`

The book pairs naturally with *Fundamentals of Software Architecture* — Farley
for engineering discipline, Richards/Ford for architectural decision-making.

---

## When to Invoke Which Skill

A routing guide for choosing the right skill from this book.

| Situation | Skill |
|---|---|
| "Set up CI/CD for our team" | `iterative-engineering-practices` |
| "Why is our CI so slow?" | `iterative-engineering-practices` |
| "Should we adopt TDD?" | `iterative-engineering-practices` |
| "Why are deploys scary?" | `iterative-engineering-practices` |
| "What's our test strategy?" | `iterative-engineering-practices` |
| "Defects keep slipping to prod" | `iterative-engineering-practices` (shift-left) |
| "Refactor this monolithic service" | `software-modularity-principles` |
| "How should we structure this module?" | `software-modularity-principles` |
| "Should we add this abstraction?" | `software-modularity-principles` (YAGNI) |
| "Should we go to microservices?" | `software-modularity-principles` |
| "Why is this code hard to test?" | `software-modularity-principles` |
| "Domain code is tangled with infra" | `software-modularity-principles` (ports & adapters) |

---

## Open Questions / Future Work

- **Mechanical Sympathy skill:** If Alex starts working on performance-critical
  systems, a dedicated skill on cache-friendly design + measurement-driven
  optimization could be valuable.
- **DDD deep dive:** The book covers DDD lightly. *Domain-Driven Design* (Evans)
  and *Implementing DDD* (Vernon) are the canonical sources. A dedicated
  DDD distillation could augment.
- **Cross-book synthesis:** This book + Software Architecture Fundamentals
  cover engineering discipline + architectural decision-making. A combined
  synthesis on "engineering excellence" would tie them together.

---

## Source

*Modern Software Engineering*
By Dave Farley

For citations, see `frameworks.md` (each framework includes its originator).
