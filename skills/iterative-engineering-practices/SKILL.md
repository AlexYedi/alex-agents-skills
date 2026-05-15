---
name: iterative-engineering-practices
description: >
  Apply iterative software engineering practices: TDD, CI, Shift-Left,
  Continuous Delivery, Mechanical Sympathy, and incremental design. Use when
  setting up a new project's development practices, debugging slow feedback
  loops, deciding when to fail fast vs build defenses, or evaluating whether
  to adopt TDD on a particular project. Triggers: "set up TDD for our team",
  "improve our feedback loops", "fail fast vs defensive coding", "shift-left
  testing", "iterative vs upfront design", "continuous integration practices".
  Produces concrete recommendations on which iterative practices fit the
  context.
---

# Iterative Engineering Practices

You apply Dave Farley's modern software engineering practices: treating software
development as an empirical, scientific process where iterative experiments
beat upfront speculation. The core insight: mistakes are inevitable; the goal
is to discover them at minimum cost.

---

## When to Use This Skill

- Setting up development practices for a new team or project
- Diagnosing why feedback loops are slow and what to fix first
- Deciding when to fail fast vs build defensive guards
- Evaluating TDD adoption on an existing codebase
- Choosing the right level of iterativeness for a project context

---

## The Five Foundational Practices

### 1. Continuous Integration (CI)

Merge all developers' working copies to mainline several times a day. Every
merge triggers automated build + test. Issues surface at the merge point, not
weeks later in integration hell.

| Indicator | Healthy CI | Broken CI |
|---|---|---|
| Time from commit to feedback | < 10 min | > 1 hour |
| Frequency of merges to main | Multiple per day per dev | Days or weeks between merges |
| Cost of a "broken build" | Stop, fix, ship within minutes | Investigation lasts days |

### 2. Test-Driven Development (TDD)

Three steps, in order:
- **Red:** Write a test that fails
- **Green:** Write *just enough* code to make it pass
- **Refactor:** Clean up code and tests while keeping them passing

**The deeper purpose:** TDD isn't really about testing — it's about *driving
better design*. If a test is hard to write, the design is wrong. The test acts
as a forcing function for modularity and clear interfaces.

### 3. Shift-Left

Move defect detection earlier in the cycle. Cheaper to catch and fix.

```
Compile time   → Unit tests   → Integration tests   → Production
   $1                $10              $100                $1,000
   (cost to fix a defect found at this stage)
```

**Implication:** Invest in earlier-stage gates. Static type checks, lint, fast
unit tests catch the same bugs cheaper than production incidents.

### 4. Continuous Delivery (CD)

Software is always in a releasable state. Deployment becomes a non-event.

**Key practice: deployment pipeline.** An automated mechanism that determines
releasability of an independently deployable unit. If it passes the pipeline,
it can ship.

### 5. Mechanical Sympathy

Design code based on understanding underlying hardware mechanics (cache,
memory hierarchy, IO patterns). Validated through measurement, not assumption.

**Example:** Cache-friendly data structures (arrays of structs vs structs of
arrays) can be 10-100x faster than algorithmically-equivalent designs that
ignore cache behavior.

---

## Principles

- **Fail Fast.** Identify defects with minimum cost. Quick failure beats slow success because feedback drives learning.
- **Empirical Process Control.** Base decisions on evidence, not fashion. Run experiments, measure outcomes.
- **Manage Complexity.** Both technical (code architecture) and organizational (team coupling). They're the same problem at different scales.
- **Control Variables.** Use version control, automated tests, infrastructure-as-code to eliminate uncontrolled variation.
- **Separation of Essential from Accidental Complexity.** Essential = the problem itself. Accidental = our chosen solution's complexity. Minimize accidental aggressively.
- **High Cohesion, Loose Coupling.** Modules should be cohesive internally and loosely coupled externally. The dominant design principle.
- **Modularity, Recursively Applied.** Same principle from system level down to individual functions. Fractal modularity.

---

## Anti-Patterns to Avoid

### Long-Lived Branches

**Looks like:** Feature branches living for weeks, merged to main as massive PRs.

**Why it fails:** Integration pain compounds. Conflicts proliferate. Feedback delayed.

**The fix:** Merge to main multiple times per day. Use feature flags to hide incomplete work, not branches.

### TDD as Test-After

**Looks like:** Writing code, then writing tests to "achieve coverage."

**Why it fails:** Misses TDD's design benefit. Tests rubber-stamp existing design rather than driving it.

**The fix:** Tests first, even for prototype-y code. The discipline reveals design problems.

### Defensive Coding Everywhere

**Looks like:** Every function checks every input; null checks proliferate; exception handling at every layer.

**Why it fails:** Hides real failures. Errors get swallowed. Bugs become harder to diagnose.

**The fix:** Fail fast. Validate at boundaries (user input, external APIs); trust internal contracts. Let errors propagate to where they can be handled meaningfully.

### Big-Bang Deployment

**Looks like:** Months of work shipped in one deploy. Deploy day is high-anxiety.

**Why it fails:** All risk concentrated. Rollback is painful. Defects hard to attribute.

**The fix:** Continuous Delivery. Ship small increments often. Each deploy is low-risk because the change is small.

### Feedback Loops Slower Than 1 Hour

**Looks like:** Wait an hour for CI. Wait a day for QA. Wait a week for staging.

**Why it fails:** Context evaporates. Bug fixing becomes archaeology.

**The fix:** Optimize feedback ruthlessly. <10 min for unit tests, <30 min for full pipeline.

---

## Decision Rules

| Condition | Action |
|---|---|
| Setting up a new project | TDD + CI + automated deployment from day 1 |
| Inheriting legacy code with no tests | Add tests at the seams (boundaries); don't try to backfill 100% |
| Bug discovered in production | Add a test that reproduces it BEFORE fixing |
| Function is hard to test | Refactor for testability; the difficulty is signal |
| Feature deferred for "future-proofing" | YAGNI — write only what current problem requires |
| CI feedback > 30 min | Stop adding features; fix CI. Slow feedback is the dominant productivity killer |
| Deploy is high-anxiety | You're not doing CD. Restructure to ship smaller pieces more often |

---

## Worked Example: Refactoring a Legacy Service to Iterative Practices

**Starting point:** Monolithic Java service. No tests. Quarterly releases. Hour-long manual QA.

| Step | Action | Why |
|---|---|---|
| 1 | Add CI with build only (no tests yet) | Establish "broken build = stop" culture |
| 2 | Add tests at the seams (HTTP boundary, DB boundary) | Don't backfill 100% — start with high-leverage tests |
| 3 | Add deployment pipeline: build → seam tests → manual gate | First step toward CD; manual gate stays for now |
| 4 | Identify highest-coupling module; extract to a port-and-adapter pattern | Reduce coupling to enable independent change |
| 5 | Replace manual QA with automated acceptance tests at the API boundary | Compounding feedback gain |
| 6 | Promote to fully automated CD on a single subsystem first | Build confidence before expanding |
| 7 | Repeat 4-6 across other subsystems | Fractal modularity |

**Lesson:** You don't go from "no tests, quarterly releases" to "TDD + CD"
overnight. Iterative practices include adopting iterative practices iteratively.

---

## Gotchas

- **TDD doesn't slow you down for skilled practitioners.** For learners, yes initially. The crossover is 2-3 weeks of practice.
- **Coverage % is a vanity metric.** 100% coverage with no assertions tests nothing. Mutation testing is a better measure.
- **CI ≠ CD.** CI is integration; CD is delivery. Many teams have CI but not CD. The deployment pipeline is the bridge.
- **Mechanical sympathy can be premature optimization.** Measure first. Optimize cache behavior only when profiling shows it's the bottleneck.
- **Failing tests in main = stop everything.** This is a discipline. If you tolerate broken main, CI's value collapses.

Source: *Modern Software Engineering* by Dave Farley, Chapters 3-5.
