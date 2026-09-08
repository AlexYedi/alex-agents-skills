---
name: consulting-acceptance-bar
description: >
  Service Levels and Error Budgets, as codified by Beyer, Jones, Petoff & Murphy (eds.),
  *Site Reliability Engineering: How Google Runs Production Systems* (O'Reilly, 2016), the
  "Service Level Objectives" chapter. Chooses the SLIs that matter for the automation (accuracy,
  latency, escalation, cost, safety), sets SLOs as the go-live acceptance bar, derives the error
  budget (1 - SLO), and defines the burn-rate response and change-freeze policy that governs
  shipping versus hardening once live. Use it as the final gate before go-live, once the benefits
  case, behaviour spec, and failure modes are in hand.
  Triggers - "set the acceptance bar", "SLI SLO SLA", "what's the error budget", "service level
  objective", "are we ready to go live", "google SRE error budget", "burn rate alert", "when do
  we freeze releases", "define the go-live threshold", "how good does this have to be to ship",
  "SLO vs SLA", "acceptance criteria for launch", "run-time reliability target", "how much failure
  can we tolerate". Produces an SLI/SLO table (SLI, definition, SLO target, error budget,
  monitor/source, owner), a burn-rate & change-freeze policy, and a go-live acceptance checklist.
---

# The Acceptance Bar (Service Levels and Error Budgets, Beyer, Jones, Petoff & Murphy, 2016)

Site Reliability Engineering, the practice Google formalized and the book of the same name edited
by Betsy Beyer, Chris Jones, Jennifer Petoff & Niall Richard Murphy (O'Reilly, 2016) documents,
draws a strict line between three terms people routinely conflate. The Service Level Objectives
chapter is the canonical source, and this skill reproduces its vocabulary exactly because the
distinction is the whole point: an SLI is a *measurement*, an SLO is a *target*, an SLA is a
*contract with consequences*. The error budget — 1 minus the SLO — is what makes an SLO more than
a scoreboard: it is an explicit, spendable allowance for failure that aligns the people who want
to ship faster with the people who want the system to stay up, by giving both sides the same
number to argue from.

For an AI automation, this is the objective bar that decides whether it may go live and whether it
may keep running: not "does it feel good in review," but "does it clear a number we agreed on in
advance, and what happens the moment it doesn't."

---

## Where this sits in the engagement

This is Step 14 of 14, the last step of Phase D (Specify & build safely) and the close of the
whole engagement. It is the final gate: it takes the benefit measures from
`consulting-benefits-case` (Step 10), the verifiable requirements and Given-When-Then scenarios
from `consulting-behaviour-specification` (Step 11), and the failure modes and monitors from
`consulting-failure-design` (Step 13), and turns them into the numbers that decide go-live. What
counts as "success" comes from Step 10; what counts as "correct behaviour" comes from Step 11;
what counts as "an error" — the thing the error budget is a budget *of* — is defined by Step 13's
failure modes and the monitors built to catch them. Nothing further downstream consumes this
skill's output inside the engagement; it closes the loop back to the benefits case by handing the
client the objective, ongoing test of whether the promised value is actually being delivered.

---

## When to use this skill

- The automation has cleared build and is approaching a go-live decision, and nobody has written
  down the number it has to hit.
- A stakeholder wants to ship faster than the team is comfortable with, or the team wants to keep
  hardening past the point of diminishing return — and there's no shared budget to arbitrate it.
- An SLA is being negotiated with an external party and the internal bar needs to sit strictly
  above it, not equal to it.
- The failure modes and monitors from Step 13 exist but aren't yet wired to a target — you know
  what can go wrong and you're watching for it, but not yet what rate of it is acceptable.
- The system is already live and burning through its error budget faster than the period allows,
  and you need a pre-agreed policy for what happens next rather than an ad hoc argument.
- Leadership is asking "are we ready" and the honest answer requires a checklist, not a feeling.

---

## The method

### 1. Three terms, kept strictly separate

| Term | Definition | Role |
|---|---|---|
| **SLI** — Service Level Indicator | A carefully defined, quantitative *measure* of some aspect of the service (e.g. task-success/accuracy rate, escalation rate, p95 latency, cost per task, safety-violation rate) | What you observe |
| **SLO** — Service Level Objective | A *target* value or range for an SLI (e.g. 99.5% of tasks succeed; p95 latency < 5s) | The internal bar |
| **SLA** — Service Level Agreement | An explicit *contract* with users that includes **consequences** of missing the objective | The external promise, if one exists |

Keep the SLO strictly stricter than any SLA — the internal bar must be missed before the external
one is, giving room to react before a contractual consequence triggers. Not every service needs an
SLA; every service should have SLOs.

### 2. The error budget

```
Error budget = 1 - SLO
```

A 99.9% availability SLO yields a 0.1% error budget. The budget is *permission to fail that much*
— no more, no less — and it is what aligns incentives: development wants velocity, operations
wants stability, and the budget gives both a single number to spend against. You spend the budget
on releases, experiments, and calculated risk. When the budget is exhausted, you **freeze risky
changes** and redirect effort into reliability work until the system is back under budget.

### 3. Burn rate

Burn rate is how fast the error budget is being consumed relative to the period it's meant to
cover (e.g. a 30-day SLO window). A budget spent evenly across the period is burning at 1x; a
budget on pace to exhaust in a fraction of the period is burning fast. Alert on **fast burn**, not
just on threshold breach — a fast burn rate is the leading indicator that catches a problem while
budget still remains, before the SLO itself is missed.

### 4. Candidate SLIs for an agent/automation

Pick only the SLIs that actually matter for this automation — a short, defensible list beats a
comprehensive one nobody watches:

| SLI category | Example measure |
|---|---|
| Task success / accuracy | % of tasks completed correctly against the behaviour spec (Step 11) |
| Escalation rate | % of tasks routed to a human instead of resolved by the automation |
| Latency | p95 / p99 time to complete a task |
| Cost | Cost per task (compute, API, human-review time) |
| Safety | Rate of safety-violation or policy-violation events (Step 13's failure modes) |

---

## Workflow (what you do when invoked)

1. **Pick the SLIs that matter.** From the benefit measures (Step 10) and the behaviour spec
   (Step 11), select the small set of SLIs — success/accuracy, latency, escalation, cost, safety —
   that actually represent whether this automation is working. Reject candidates that don't map to
   a real decision anyone will make from them.
2. **Set SLOs as the go-live acceptance bar.** For each SLI, agree a target value or range that
   the automation must clear to ship. If an SLA exists or is being negotiated, set every SLO
   strictly stricter than it.
3. **Compute the error budget per SLI.** `Error budget = 1 - SLO` for each. State it in the same
   units stakeholders will actually track (failures per period, minutes, dollars, incidents).
4. **Define the burn-rate response and change-freeze policy.** Set the burn-rate threshold that
   triggers an alert, and the explicit policy for what happens at exhaustion: what gets frozen
   (releases, experiments, new automation targets), who declares the freeze, and what "back under
   budget" means before it lifts.
5. **Wire the monitors from Step 13 to each SLI.** For every SLI, name the monitor or data source
   (from the failure-design monitors) that measures it in production, and confirm every failure
   mode in Step 13 that should count as "an error" actually rolls up into an SLI's numerator.
6. **Ratify the go-live checklist and close the loop.** Walk the explicit acceptance checklist
   against current numbers, get sign-off, and route the finished SLO spec back to whoever owns the
   benefits case (Step 10) as the ongoing, objective test of realized value.

---

## Deliverable & templates

**SLI/SLO/error-budget table**

```markdown
| SLI | Definition | SLO target | Error budget | Monitor/source (Step 13) | Owner |
|---|---|---|---|---|---|
| Task success rate | % of tasks meeting the behaviour spec (Step 11) end-to-end | >= 99.0% over 30 days | 1.0% (≈ 1 in 100 tasks) | Eval harness + production outcome monitor | e.g. Automation Lead |
| Escalation rate | % of tasks routed to a human | <= 8.0% over 30 days | 8.0% budget for escalations | Routing/escalation monitor | e.g. Ops Lead |
| p95 latency | Time to task completion, 95th percentile | < 5s | 5% of tasks may exceed 5s | Latency monitor | e.g. Platform Eng |
| Cost per task | Fully loaded compute + review cost | <= $0.40 | n/a (cost ceiling, not a rate) | Cost/usage monitor | e.g. Finance/Eng |
| Safety-violation rate | Rate of policy/safety-violation events (Step 13 failure modes) | <= 0.05% | 0.05% (≈ 1 in 2,000 tasks) | Safety monitor / FMEA detection controls | e.g. Risk Owner |
```

**Burn-rate & change-freeze policy**

```
Error budget period: <e.g. rolling 30 days>
Fast-burn alert threshold: <e.g. burning >= 4x the sustainable rate over a 1-hour window>
On fast-burn alert: <e.g. page on-call, halt non-essential releases pending investigation>
On budget exhaustion: FREEZE <e.g. new automation targets, risky releases, expanded scope>
Freeze declared by: <named owner/role>
Freeze lifts when: <e.g. burn rate back under 1x and budget replenished to >= X% for N days>
```

**Go-live acceptance checklist**

```markdown
- [ ] Every SLI maps to a real decision and has an owner
- [ ] Every SLO is stricter than any external SLA covering the same measure
- [ ] Error budget computed and expressed in units stakeholders will track
- [ ] Burn-rate alert threshold and change-freeze policy agreed and owned
- [ ] Every SLI has a live monitor/source wired from Step 13's failure modes
- [ ] Current measured values meet or exceed every SLO target
- [ ] Realization review date set, tying back to the benefits case (Step 10)
```

---

## Pitfalls

- **Conflating SLI, SLO, and SLA.** Loosely saying "our SLA is 99.9%" when there's no contract or
  consequence attached is an SLO wearing the wrong name — keep the vocabulary exact.
- **Setting the SLO equal to (or looser than) the SLA.** This leaves no room to react before a
  contractual consequence fires; the internal bar must be stricter.
- **Measuring everything instead of what matters.** A long SLI list nobody reviews is worse than a
  short one that's actually watched — pick from the benefits case and behaviour spec, not from
  what's easy to instrument.
- **Treating the error budget as a target to spend to zero on principle.** The budget is
  permission to fail that much, not a quota to be exhausted for its own sake — spend it on real
  velocity and risk, not carelessness.
- **No burn-rate alerting, only threshold alerting.** Waiting until the SLO is actually missed
  means the budget is already gone; alert on fast burn while budget remains.
- **No change-freeze policy, or one with no named owner.** An error budget with no agreed
  consequence at exhaustion is a suggestion, not a bar — someone must be able to say "we freeze
  now" and have it stick.

---

## Related

- **In-suite** — `consulting-benefits-case` (Step 10, upstream): supplies the benefit measures
  that become candidate SLIs. `consulting-behaviour-specification` (Step 11, upstream): supplies
  the verifiable requirements and scenarios that "task success" is measured against.
  `consulting-failure-design` (Step 13, upstream): supplies the failure modes and monitors that
  define what counts as an error and where the data comes from.
- **Elsewhere in the library** — `observability-designer`, `quality-gates`,
  `ai-evaluation-methodology`, `ai-evals`.
- **References** — Beyer, B., Jones, C., Petoff, J. & Murphy, N. R. (eds.), *Site Reliability
  Engineering: How Google Runs Production Systems* (O'Reilly, 2016), "Service Level Objectives."
