# Additional Experts: Modern Software Engineering

**Source:** *Modern Software Engineering* by Dave Farley

This reference captures Dave Farley's accumulated wisdom on engineering as an
empirical, scientific discipline. Use alongside:
- `iterative-engineering-practices/SKILL.md`
- `software-modularity-principles/SKILL.md`

---

## About the Expert

**Dave Farley** is co-author of *Continuous Delivery* (the canonical book on
the practice) and runs the popular YouTube channel *Continuous Delivery*. He
worked on the LMAX trading platform — one of the highest-throughput, lowest-latency
financial systems ever built — using the practices he advocates.

The book's central thesis: software engineering is an empirical, scientific
discipline. Most teams treat it as craft or art; this leaves performance gains
on the table.

The voice is direct, often contrarian, and grounded in measurement. Farley
challenges sacred cows (defensive coding, big upfront design, "we'll write
tests later") with both reasoning and personal experience.

---

## The Engineering Mindset Shift

### Software engineering is not the code

This is Farley's First Law. Many teams optimize for "code" — number of lines,
elegance of abstractions, framework choices. Software engineering is the
**process, culture, and philosophy** required to build and evolve software.

**Practical implications:**
- Code reviews focus on whether the change advances learning, not on style
- Quality is a property of the engineering process, not just the artifact
- Bad processes produce bad code regardless of developer skill

### Treat development as scientific method applied to software

Hypothesis → Prediction → Experiment → Falsification.

**The mapping:**
- Hypothesis: "This change will improve metric X"
- Prediction: "After deploy, X will move from A to B"
- Experiment: Deploy and measure
- Falsification: If X doesn't move, the hypothesis was wrong

**Key insight:** Most teams skip falsification. Changes ship; outcomes don't get measured; teams keep doing what feels right rather than what works.

### Mistakes are inevitable; the goal is to discover them at minimum cost

This reframes everything. Instead of trying to prevent mistakes (impossible),
optimize for **fast cheap detection**.

This is why Farley evangelizes:
- Continuous Integration (catch integration bugs at merge, not at release)
- TDD (catch design bugs at write-time, not at runtime)
- Continuous Delivery (catch production bugs at staging, not at customer)
- Fail Fast (let errors propagate to where they can be handled, don't bury them)

---

## Best Practices for Iterative Development

### Continuous Integration as discipline, not tooling

CI is not "we have Jenkins set up." It's a discipline:
- **Multiple merges per day per developer**
- **Time from commit to feedback < 10 minutes**
- **Broken main = stop everything until fixed**
- **No long-lived feature branches**

If any of these is missing, you don't have CI in the meaningful sense, regardless of tooling.

### The cost of slow feedback compounds

Farley repeatedly emphasizes the cost of slow feedback loops:
- 10-minute CI: developer stays in flow, fixes immediately
- 1-hour CI: developer context-switches, returns later, costs ~5x more time
- 1-day CI: changes pile up; integration becomes archaeology
- 1-week CI: practice is dead; teams revert to "test in prod"

**Practical advice:** Treat CI speed as a P0 feature. If CI is slow, stop adding features and fix CI.

### TDD is design discipline, not testing discipline

The most misunderstood point in TDD adoption.

**The Red-Green-Refactor loop:**
- **Red:** Write a failing test (forces you to think about the contract)
- **Green:** Write just enough code to make it pass
- **Refactor:** Clean up while tests still pass

**Why it works for design:**
- If a test is hard to write, the design is wrong (testability = good design proxy)
- Tests force decoupling (can't test tightly coupled code)
- Tests force interface clarity (the test specifies the contract)

**Anti-pattern:** "Test-after-development" — writing tests after the code.
Misses TDD's design benefit. Tests rubber-stamp existing design rather than driving it.

### Continuous Delivery is the goal; CI is the prerequisite

Continuous Delivery: software is **always in a releasable state**. Deployment
becomes a non-event.

**Required infrastructure:**
- **Deployment pipeline:** Automated mechanism that determines releasability
- **Environment as code:** Same configuration in dev/staging/prod
- **Feature flags:** Decouple deployment from release
- **Automated rollback:** Bad deploys self-recover

**Why it matters:** Big-bang deployments concentrate risk. Continuous Delivery
distributes risk across many small ships.

### Shift-Left: catch defects earlier

Cost of fixing a defect:
- Compile time: $1
- Unit tests: $10
- Integration tests: $100
- Production: $1,000

**Practical implications:**
- Static type systems pay for themselves
- Lint catches a lot of cheap mistakes
- Fast unit tests beat slow integration tests for the bugs they can catch
- The earlier in the pipeline a defect is caught, the cheaper it is

---

## Best Practices for Managing Complexity

### Modularity as the dominant lever

Farley's strongest claim: managing complexity is the single most important
engineering skill.

**Why modularity is the lever:**
- Modularity = separation of concerns
- Separation of concerns = local reasoning
- Local reasoning = testable, changeable code

### High Cohesion, Loose Coupling — at every level

Apply recursively:
- System level: services should have one purpose
- Service level: modules should have one purpose
- Module level: classes/functions should have one purpose
- Function level: each function does one thing

**Farley's term:** "Fractal modularity." Same principle applies at every scale.

### Separate Essential from Accidental Complexity

| Type | Source | What to do |
|---|---|---|
| **Essential** | The problem itself (business logic, domain rules) | Express as cleanly as possible |
| **Accidental** | Our chosen solution (database, framework, infrastructure) | Minimize aggressively; isolate from essential |

**Practical implication:** Domain code should never import framework code,
database libraries, or HTTP libraries. The translation lives in adapter layers.

### Information Hiding as a design discipline

Hide internal workings; expose stable interfaces.

**Specific advice:**
- Use general representations (`List` instead of `ArrayList`)
- Use dependency injection to create measurement points
- Avoid overly generic abstractions (`Object`, `Any`) — they hide nothing
- Today's "internal detail" is tomorrow's API breaking change if exposed

### YAGNI (You Ain't Gonna Need It)

Write only the code necessary to solve the current problem. Avoid future-proofing
and over-engineering.

**Why this matters:**
- Speculative generality adds complexity for hypothetical futures
- Most imagined futures don't arrive (or arrive differently)
- Build for current needs; refactor to abstraction *when* the second use case appears

**Practical guidance:** If you're tempted to add a "configurable" or
"extensible" or "pluggable" feature with one current use case, don't. Add
the feature when the second use case appears.

---

## Best Practices for Distributed Systems

### Domain partitioning > technical partitioning

The industry trend (Farley supports it strongly): organize services by domain,
not by technical layer.

**Why:**
- Bounded contexts are naturally decoupled (real domain boundaries)
- Cross-functional teams own end-to-end user journeys
- Changes localize within domain boundaries

### Decouple Teams and Systems

Conway's Law: organizations design systems that mirror their communication
structure. Inverse Conway: design teams to match the system structure you want.

**Practical advice:**
- Cross-functional teams own services (not "frontend team," "backend team")
- Each team can deploy independently
- Inter-team dependencies should be at API contracts, not at code level

### Microservices as the destination, not the start

Farley's nuanced view: microservices are appropriate when you have:
- Domain teams that need independent ownership
- Services with genuinely different scaling needs
- Operational maturity (monitoring, observability, on-call)
- Clear bounded contexts

**Anti-pattern:** Premature microservices. Distributed monolith is worse than
a well-modularized monolith.

**Path forward:** Start with monolith + good modularity. Extract services when
you have evidence that distribution is justified.

### Event Storming for Domain Identification

Collaborative analysis technique to identify natural lines of abstraction:
- Gather domain experts and developers
- Map domain events on a timeline
- Identify clusters of related behavior
- Bounded contexts emerge from the clusters

**Why it works:** Surfaces the domain's natural structure before you bake it into code.

---

## Best Practices for Empirical Process Control

### Base decisions on evidence, not fashion

Farley is consistently skeptical of "we should adopt X because everyone is
using X." Adopt X when you have evidence that X solves a problem you have.

**Specific antidotes:**
- "Our team is too small for microservices" — based on volume of evidence
- "We need a Kubernetes cluster" — actually do you? What problem does it solve?
- "We need a service mesh" — only at scale where benefits exceed operational cost

### Control Variables

Software engineering's "experiments" require controlling variables:
- Version control (changes are tracked)
- Automated testing (consistent verification)
- Infrastructure as code (consistent environments)
- Feature flags (controlled rollouts)

**Without control of variables:** Cannot tell what causes what. Debugging is
guessing.

### Fail Fast

When something is wrong, surface it immediately. Don't:
- Swallow exceptions silently
- Return null and hope the caller handles it
- Add defensive null checks everywhere

Do:
- Validate at boundaries (user input, external APIs)
- Trust internal contracts
- Let errors propagate to where they can be handled meaningfully

**Why this works:** Errors caught early are cheap. Errors caught late are
catastrophic. Defensive coding hides errors; doesn't prevent them.

---

## Worked Examples

### Example 1: Refactoring a Legacy Service to Iterative Practices

**Starting point:** Monolithic Java service, no tests, quarterly releases, hour-long manual QA.

| Step | Action | Why |
|---|---|---|
| 1 | Add CI with build only (no tests yet) | Establish "broken build = stop" culture |
| 2 | Add tests at the seams (HTTP boundary, DB boundary) | Don't backfill 100% — start with high-leverage |
| 3 | Add deployment pipeline: build → seam tests → manual gate | First step toward CD |
| 4 | Identify highest-coupling module; extract via ports & adapters | Reduce coupling, enable independent change |
| 5 | Replace manual QA with automated acceptance tests at API boundary | Compounding feedback gain |
| 6 | Promote to fully automated CD on a single subsystem first | Build confidence before expanding |
| 7 | Repeat 4-6 across other subsystems | Fractal modularity |

**Lesson:** You don't go from "no tests, quarterly releases" to "TDD + CD"
overnight. Iterative practices include adopting iterative practices iteratively.

### Example 2: Refactoring a Tightly-Coupled Order Service

**Starting state:** `OrderService` 2000 lines. Imports SQLAlchemy, Stripe SDK,
Twilio SDK, internal pricing engine. Tests require live DB and mocked external services.

| Step | Action | Why |
|---|---|---|
| 1 | Identify essential: order lifecycle, pricing calculation, stock reservation | Domain logic |
| 2 | Identify accidental: persistence, payment, SMS notification | Infrastructure |
| 3 | Define ports: `OrderRepository`, `PaymentGateway`, `Notifier` | Domain's view of what it needs |
| 4 | Move essential logic to pure domain module; ports are abstract | Domain becomes testable |
| 5 | Implement adapters for SQLAlchemy, Stripe, Twilio | Infrastructure now interchangeable |
| 6 | Tests for domain become fast unit tests with fake adapters | 1000x speed improvement |
| 7 | Tests for adapters are integration tests against real systems | Smaller, focused, less frequent |

**Lesson:** Most "monolithic service is unmaintainable" complaints are really
"domain and infrastructure are tangled." Untangle them before considering microservices.

---

## Anti-Patterns (deeper than skill files)

### Long-Lived Feature Branches

Branches living for weeks, merged as massive PRs.
**Why it fails:** Integration pain compounds. Conflicts proliferate. Feedback delayed.
**The fix:** Merge to main multiple times per day. Use feature flags to hide incomplete work.

### Defensive Coding Everywhere

Every function checks every input; null checks proliferate; exception handling at every layer.
**Why it fails:** Hides real failures. Errors get swallowed. Bugs harder to diagnose.
**The fix:** Fail fast. Validate at boundaries. Trust internal contracts.

### Big-Bang Deployment

Months of work shipped in one deploy. Deploy day is high-anxiety.
**Why it fails:** All risk concentrated. Rollback painful. Defects hard to attribute.
**The fix:** Continuous Delivery. Ship small increments often.

### God Object / God Module

One class or module that does everything; thousands of lines; many responsibilities.
**Why it fails:** Low cohesion, high coupling, impossible to test.
**The fix:** Extract responsibilities into focused modules.

### Speculative Generality

Premature abstraction layer for hypothetical future needs.
**Why it fails:** Adds complexity. Often the imagined future never arrives.
**The fix:** YAGNI. Build for current needs. Refactor when second use case appears.

### Leaking Abstractions

Domain code that says `userRepo.queryByEmailLowerCase()` — abstraction includes implementation detail.
**Why it fails:** Couples domain to implementation. Changing the underlying store breaks domain.
**The fix:** Domain expresses intent (`userRepo.findByEmail(email)`); adapter handles details.

### Inconsistent Abstraction Levels

A function that mixes high-level orchestration with low-level byte manipulation.
**Why it fails:** Reader has to context-switch constantly.
**The fix:** Each function operates at one level. Lower levels live in their own functions.

### Premature Microservices

Splitting a small project into 10 microservices "for scalability."
**Why it fails:** Adds operational complexity without solving real problems.
**The fix:** Start with well-modularized monolith. Extract when justified by evidence.

---

## Process Wisdom

### Code reviews

- Focus on whether the change advances learning, not on style
- Style should be enforced by formatters, not reviewers
- Reviews should ask "is this the right shape of solution?" not "is this code idiomatic?"

### Refactoring

- Refactor in small steps; tests pass after each step
- Don't combine refactoring with feature work
- Refactor to enable a feature; ship the feature; then move on

### Postmortems

- Blameless: focus on systemic causes, not individual mistakes
- Output should change the system, not just the people
- Track action items; verify they're done

### Hiring

- Hire for engineering judgment, not for knowledge of specific frameworks
- Frameworks change; engineering principles don't
- Test for testability mindset, modularity instincts, willingness to delete code

---

## When to Apply These Practices

This expert reference complements:

- For TDD/CI/CD/Shift-Left → also see `iterative-engineering-practices/SKILL.md`
- For modularity, cohesion, ports & adapters → also see `software-modularity-principles/SKILL.md`
- For frameworks catalog → see `frameworks.md` in this folder
