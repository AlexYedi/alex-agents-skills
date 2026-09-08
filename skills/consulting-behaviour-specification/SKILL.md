---
name: consulting-behaviour-specification
description: >
  Given-When-Then scenario writing (Dan North, "Introducing BDD", 2006) combined
  with the requirement quality bar from ISO/IEC/IEEE 29148:2018, Systems and
  software engineering — Life cycle processes — Requirements engineering. Converts
  a fuzzy automation ask into a set of singular, verifiable "shall" requirements,
  each backed by concrete happy-path, edge, and negative Given-When-Then scenarios.
  Triggers - "write acceptance criteria", "given when then", "GWT scenarios",
  "behaviour driven development", "BDD scenarios", "what exactly should this agent do",
  "spec out the required behaviour", "make this requirement testable", "is this
  requirement unambiguous", "define happy path and edge cases", "29148", "shall
  statements", "requirements aren't verifiable", "before we build let's spec the
  behaviour". Produces a requirements table (id, shall-statement, verifiable?, source)
  with fenced Given-When-Then scenario blocks per requirement covering happy, edge,
  and negative paths.
---

# Behaviour Specification (Given-When-Then, Dan North, 2006 + ISO/IEC/IEEE 29148:2018)

Given-When-Then is the scenario notation Dan North introduced in "Introducing BDD"
(2006) as the grammar of Behaviour-Driven Development: GIVEN an initial context,
WHEN an event occurs, THEN an observable outcome follows, with AND/BUT clauses
extending any step. Written in ubiquitous, business-readable language, a GWT
scenario is a concrete example that doubles as an executable acceptance test — a
feature or story is described by the set of scenarios that specify it.

ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes
— Requirements engineering*, supplies the quality bar those scenarios must satisfy
upstream: what makes one requirement statement good, and what makes a set of
requirements good, in a standard "The <system> shall <capability> <condition>
<constraint>" syntax.

This skill runs them together: 29148 disciplines the requirement ("necessary,
unambiguous, singular, verifiable…"), GWT gives it a testable, concrete form. The
combination turns "it should handle refunds" into scenarios an agent contract, an
eval harness, and an acceptance bar can all consume without reinterpretation.

---

## Where this sits in the engagement

This is Step 11 of 14, opening Phase D (Specify & build safely) — the delivery-contract
phase. It takes the chosen automation and human/AI function split from
`consulting-automation-design` (Step 7) and turns it into precise, verifiable required
behaviour. It feeds `consulting-agent-contract` (Step 12, which derives pre/postconditions
and invariants from these scenarios) and `consulting-acceptance-bar` (Step 14, which sets
go-live thresholds against the same scenario set).

---

## When to use this skill

- The team has agreed *what* to automate but not precisely *what it must do* in each situation.
- A stakeholder says "it should handle X" and nobody can say what "handle" means operationally.
- You're about to write an agent contract, an eval suite, or acceptance tests and need a scenario spec to build them from.
- A requirement reads as a paragraph, not a testable statement — signs of ambiguity or compound requirements hiding inside it.
- You need happy-path, edge-case, and failure-case coverage agreed before build starts, not discovered after.
- A PRD exists but its acceptance criteria are vague, untestable, or missing negative cases entirely.

---

## The method

### 1. Given-When-Then (Dan North, 2006)

Each scenario is written in ubiquitous language, one scenario per concrete example:

```
GIVEN <initial context / preconditions>
WHEN <an event or action occurs>
THEN <the expected, observable outcome>
[AND <extends the preceding step>]
[BUT <extends the preceding step, usually a negative case>]
```

A feature or story is described by its full *set* of scenarios, not any single one.
Name scenarios behaviourally ("should refund an order paid by card within 24
hours"), not implementation-first ("test refund function"). A scenario is only
usable as an acceptance test if its THEN is externally observable — something a
user, a log, an API response, or a downstream system state can confirm.

### 2. ISO/IEC/IEEE 29148:2018 — the requirement quality bar

**Characteristics of an individual requirement** — a good requirement is:

| Characteristic | Meaning |
|---|---|
| Necessary | Defines a capability actually needed; removing it would create a gap |
| Appropriate | Right level of detail for its level in the spec hierarchy |
| Unambiguous | One and only one interpretation |
| Complete | No missing units, conditions, or "TBD" |
| Singular | States exactly one capability — no "and/or" compounding |
| Feasible | Achievable within known constraints (technical, cost, schedule) |
| Verifiable | Can be proven satisfied by inspection, test, analysis, or demonstration |
| Correct | Accurately reflects what's actually needed |
| Conforming | Follows the standard statement syntax and house style |

**Characteristics of a requirement set** — the set as a whole must be: complete
(nothing needed is missing), consistent (no requirement contradicts another),
feasible (buildable together), comprehensible (readable by all stakeholders), and
able to be validated (traceable to a source and confirmable against it).

**Standard statement syntax:**

```
The <system> shall <capability> <condition> <constraint>.
```

Example: "The refund agent shall issue a full refund when a cancellation request
is received within 24 hours of the original charge." 29148 also defines the
document hierarchy this feeds — StRS (Stakeholder Requirements Spec), SyRS
(System Requirements Spec), SRS (Software Requirements Spec) — use whichever
tier matches the artifact you're producing this spec for.

### 3. How they combine

29148 tells you when a requirement is *ready*: singular, unambiguous, verifiable.
GWT tells you how to *prove* it: at least one scenario per requirement, and for
any requirement carrying real risk, three scenarios — happy path (the capability
works as intended), boundary/edge (a legitimate but extreme input — empty,
maximum, exactly-at-threshold), and negative/failure (an invalid input or
disallowed action that must be rejected or escalated, not silently mishandled).
A requirement that can't be turned into an observable GWT scenario has failed
the verifiable test and needs rewriting or splitting before it goes further.

---

## Workflow (what you do when invoked)

1. **List the behaviours.** From the automation scope (Step 7 output) and any
   existing PRD, enumerate every distinct behaviour the system must exhibit —
   don't merge related-but-different behaviours yet.
2. **Draft "shall" statements.** Write each behaviour as "The <system> shall
   <capability> <condition> <constraint>," then check it against the nine 29148
   characteristics. Flag and split any statement that fails singular (contains
   "and"/"or" joining two capabilities) or unambiguous.
3. **Assign an id and source.** Give each surviving requirement a stable id
   (e.g. `BR-01`) and cite where it came from (PRD section, stakeholder quote,
   policy doc) — this is the traceability 29148 requires for a validated set.
4. **Write GWT scenarios per requirement.** For each requirement, write at
   minimum a happy-path scenario; for anything risk-bearing, add a
   boundary/edge and a negative/failure scenario. Keep each scenario concrete —
   real example values, not placeholders.
5. **Check observability.** For every THEN, confirm it names something
   externally checkable (a state, a response, a log line) — reject any THEN
   that only describes internal implementation.
6. **Resolve ambiguity and re-split.** Where a scenario reveals a requirement
   was actually two requirements in disguise, split it, re-id, and re-derive
   its scenarios.
7. **Hand off.** Pass the finished requirements table + scenario blocks to
   `consulting-agent-contract` (Step 12) for pre/postconditions and to
   `consulting-acceptance-bar` (Step 14) for go-live thresholds.

---

## Deliverable & templates

**Requirements table:**

```markdown
| ID    | Shall statement                                                                 | Verifiable? | Source                  |
|-------|----------------------------------------------------------------------------------|-------------|--------------------------|
| BR-01 | The refund agent shall issue a full refund when cancellation is requested within 24 hours of charge. | Yes | PRD §4.2, support policy v3 |
| BR-02 | The refund agent shall escalate to a human agent when the refund amount exceeds $500. | Yes | Stakeholder interview, 2026-08-14 |
```

**GWT scenario block, per requirement:**

```gherkin
# BR-01 — happy path
GIVEN a customer's order was charged 3 hours ago
WHEN the customer submits a cancellation request
THEN the agent issues a full refund
AND the customer receives a refund confirmation within 5 minutes

# BR-01 — edge
GIVEN a customer's order was charged exactly 24 hours and 0 minutes ago
WHEN the customer submits a cancellation request
THEN the agent issues a full refund
BUT logs the request as a boundary case for audit

# BR-01 — negative
GIVEN a customer's order was charged 30 hours ago
WHEN the customer submits a cancellation request
THEN the agent declines the automatic refund
AND routes the request to a human agent with the reason recorded
```

Repeat the scenario block for every requirement in the table.

---

## Pitfalls

- **Compound requirements.** "The system shall validate and refund the order" is
  two requirements wearing one id — split before writing scenarios, or the
  scenarios will be untestable as a unit.
- **Unobservable THENs.** "THEN the system correctly processes the refund" isn't
  verifiable — say what "correctly" produces: a state change, a value, a message.
- **Happy-path-only coverage.** Shipping only the happy-path scenario hides the
  actual risk; boundary and negative scenarios are where automation usually fails.
- **Vague preconditions.** A GIVEN that omits the state that actually matters
  (account status, time elapsed, prior actions) produces a scenario nobody can
  reproduce or test against.
- **Skipping the 29148 check.** Writing GWT scenarios straight from a vague ask
  without first forcing a "shall" statement lets ambiguity survive into the
  scenarios themselves.
- **Treating this as documentation, not a contract.** These scenarios are inputs
  to Steps 12 and 14 — if they're not precise enough to code an eval against,
  they're not done.

---

## Related

- **In-suite** — `consulting-automation-design` (Step 7, feeds this with the
  chosen automation level and function allocation); `consulting-agent-contract`
  (Step 12, derives pre/postconditions and invariants from these scenarios);
  `consulting-acceptance-bar` (Step 14, sets go-live thresholds against this
  same scenario set).
- **Elsewhere in the library** — `tdd-workflow`, `workflow-testing`,
  `writing-prds`, `ai-evals`.
- **References** — North, D., "Introducing BDD" (2006); ISO/IEC/IEEE
  29148:2018, *Systems and software engineering — Life cycle processes —
  Requirements engineering*.
