---
name: consulting-roadmap-sequencing
description: >
  Applies Donald Reinertsen's Weighted Shortest Job First (WSJF) from *The Principles of
  Product Development Flow* (Celeritas Publishing, 2009) to sequence a set of candidate
  automation initiatives for maximum economic value under a capacity constraint. Scores
  Cost of Delay (business value + time criticality + risk reduction/opportunity enablement)
  against job size to compute WSJF, then sorts descending into a delivery sequence.
  Triggers - "WSJF", "weighted shortest job first", "which one do we build first", "sequence
  the roadmap", "cost of delay", "Reinertsen prioritization", "how do we order these
  initiatives", "prioritize the backlog by economics", "what should we build first",
  "roadmap sequencing", "job size vs value", "economic sequencing", "delivery order".
  Produces a WSJF sequencing table and the ranked delivery sequence.
---

# Roadmap Sequencing (Weighted Shortest Job First, Reinertsen, 2009)

Donald Reinertsen, in *The Principles of Product Development Flow: Second Generation Lean
Product Development* (Celeritas Publishing, 2009), argues that under a capacity constraint the
economically optimal policy is to sequence jobs by Cost of Delay per unit of job duration —
Weighted Shortest Job First. Reinertsen's central point is that most organizations never
quantify cost of delay, and that omission is the single biggest gap in their economics: without
it, teams default to sequencing by gut feel, political weight, or raw business value, and
routinely under-prioritize short, high-value jobs while over-prioritizing large ones whose size
was never weighed against their value. This skill applies WSJF to the candidate automations
surfaced earlier in the engagement, turning a prioritized list into an actual delivery sequence.

---

## Where this sits in the engagement

This is step 9 of 14, the first step of Phase C (Plan & justify). It takes the
constraint-relieving automation candidates identified in `consulting-constraint-analysis`
(step 8) — already scored for suitability back in `consulting-ai-suitability-scoring`, step 6 —
and sequences them for maximum economic value under the team's delivery capacity. It pairs with
`consulting-benefits-case` (step 10), which turns the sequenced roadmap into a quantified
benefits plan.

---

## When to use this skill

- You have a validated list of constraint-relieving automation candidates and a capacity limit
  (one team, one delivery quarter, one budget) and need to decide the build order.
- Stakeholders are prioritizing by opinion, seniority, or "whoever asks loudest" and you need a
  defensible, economics-based ordering instead.
- A backlog contains a mix of small quick wins and large strategic bets, and naive
  value-ranking keeps pushing the large bets to the top even though they tie up capacity for
  months.
- Leadership asks "why isn't the biggest, most valuable thing first?" and you need to show the
  duration-adjusted math.
- You suspect the team is quietly deprioritizing time-sensitive work because nobody has put a
  number on what waiting costs.
- The constraint-relieving candidates from step 8 need a sanity check: do they actually come out
  on top once sequenced, or does the roadmap need re-examining?

---

## The method

**Source.** Donald G. Reinertsen, *The Principles of Product Development Flow: Second
Generation Lean Product Development*, Celeritas Publishing, 2009.

**The formula.** Under a capacity constraint, sequence jobs to maximize economic value using
Weighted Shortest Job First:

```
WSJF = Cost of Delay / Job Duration (job size)
```

Do the job with the highest Cost-of-Delay per unit time **first**. This is the economically
optimal sequencing policy when cost of delay is roughly homogeneous across jobs and capacity is
limited — it is the scheduling-theory result known as "weighted shortest processing time." The
skill is to **sequence**, not merely prioritize: WSJF produces an order, not just a ranked list
of what matters.

**Cost of Delay.** Cost of Delay (CoD) is the money you lose for every unit of time a job is
*not* done. Reinertsen's central point is that most organizations never quantify cost of delay,
and that this is the single biggest gap in their economics — everything downstream (sequencing,
batch size, WIP limits) depends on knowing it. The widely used operational form (popularized by
SAFe, built directly on Reinertsen's economic framework) decomposes CoD into three components,
each scored on a relative scale — typically modified Fibonacci (1, 2, 3, 5, 8, 13, 20):

```
Cost of Delay = User/Business Value + Time Criticality + Risk Reduction & Opportunity Enablement
```

- **User/Business Value** — how much value this delivers to the user or the business, relative
  to the other candidates on the list.
- **Time Criticality** — how much the value decays the longer the job waits (a fixed deadline,
  a closing competitive window, a compliance date).
- **Risk Reduction & Opportunity Enablement** — value from reducing risk or unlocking future
  opportunities that isn't captured in the raw business-value score (e.g. de-risking a platform
  dependency other initiatives need).

**Job size.** Job size (duration) is likewise estimated on a relative scale — the same Fibonacci
sequence works — as a proxy for how long the job will occupy the constrained capacity.

**Counter-intuitive lessons to carry into the readout:**

- Quantify Cost of Delay above all else — an un-quantified CoD is the default failure mode, not
  an edge case.
- Short, high-CoD jobs dominate the sequence — they clear the queue fast and stop bleeding value
  quickly.
- Large, long-duration jobs are usually mis-prioritized in naive value-only rankings because
  their size is never weighed against their value.
- The highest-*value* item is not always first — the highest value **per unit time** is. A
  10-value job that takes 10 units nets the same WSJF as a 2-value job that takes 2 units; the
  smaller job clears sooner and frees capacity sooner.

**Sanity-check.** The constraint-relieving jobs identified in step 8 should rank near the top
once sequenced. If they don't, re-examine the Cost of Delay estimates before accepting the
sequence — a low WSJF on a constraint-relieving job usually means time criticality or risk
reduction was under-scored, not that the constraint analysis was wrong.

---

## Workflow (what you do when invoked)

1. **List the candidate initiatives.** Pull the constraint-relieving automation candidates from
   `consulting-constraint-analysis` (step 8). Confirm each was already scored for suitability in
   `consulting-ai-suitability-scoring` (step 6) — don't sequence unvetted candidates.
2. **Score the three Cost of Delay components** for each initiative — user/business value, time
   criticality, risk reduction/opportunity enablement — on a relative Fibonacci scale (1, 2, 3,
   5, 8, 13, 20). Score them with the people who own the value and the deadline, not from a desk
   review alone.
3. **Sum the three components to get Cost of Delay** per initiative.
4. **Estimate job size/duration** for each initiative on the same relative scale, as a proxy for
   how long it will occupy the team's constrained capacity.
5. **Compute WSJF = Cost of Delay / Job Size** for every initiative.
6. **Sort descending by WSJF** to produce the delivery sequence — highest WSJF first.
7. **Sanity-check against the constraint** identified in step 8: do the constraint-relieving
   initiatives rank near the top? If not, revisit the CoD estimates before finalizing. Hand the
   sequenced roadmap to `consulting-benefits-case` (step 10).

---

## Deliverable & templates

**WSJF sequencing table** — one row per candidate initiative:

```markdown
| Initiative | User/Business Value (1-20) | Time Criticality (1-20) | Risk Reduction/Opportunity (1-20) | Cost of Delay | Job Size (1-20) | WSJF | Rank |
|---|---|---|---|---|---|---|---|
| e.g. Automate invoice matching (relieves bottleneck) | 13 | 8 | 8 | 29 | 5 | 5.8 | 1 |
| e.g. Auto-triage support tickets | 8 | 13 | 5 | 26 | 8 | 3.25 | 2 |
| e.g. Consolidate reporting dashboard | 13 | 3 | 3 | 19 | 13 | 1.46 | 3 |
```

**Ordered delivery sequence:**

```markdown
1. [Initiative] — WSJF [x.x] — constraint-relieving: [yes/no]
2. [Initiative] — WSJF [x.x] — constraint-relieving: [yes/no]
3. [Initiative] — WSJF [x.x] — constraint-relieving: [yes/no]
...
```

Hand both artifacts to `consulting-benefits-case`.

---

## Pitfalls

- **Skipping Cost of Delay entirely and prioritizing by raw value.** This is Reinertsen's
  headline warning — an un-quantified CoD is the default failure mode. If you can't score all
  three CoD components, at minimum force a relative comparison; don't fall back to "gut sense of
  importance."
- **Ranking by value alone and ignoring job size.** A large, valuable initiative will look like
  the obvious first pick until you divide by its duration — always compute the full WSJF ratio,
  never truncate to CoD.
- **Letting job size estimates come from optimism rather than the people who'll do the work.**
  An under-estimated job size inflates WSJF and jumps the queue; get sizing from the delivery
  team, not the sponsor.
- **Treating WSJF as a one-time exercise.** Cost of Delay and job size both change as the
  engagement progresses — re-sequence when new candidates surface or estimates prove wrong,
  don't treat the first sequencing table as permanent.
- **Ignoring a failed sanity-check.** If the constraint-relieving initiatives from step 8 don't
  rank near the top, that's a signal the CoD scoring under-weighted risk reduction or time
  criticality — fix the scores, don't override the sequence by hand.
- **Confusing prioritization with sequencing.** A ranked list of "what matters" is not a
  delivery plan. WSJF's output is an order jobs get built in under a real capacity constraint —
  present it as a sequence, not a priority list.

---

## Related

- **In-suite** — `consulting-constraint-analysis` (step 8) supplies the constraint-relieving
  candidates this skill sequences. `consulting-benefits-case` (step 10) is this skill's pair:
  it takes the sequenced roadmap and builds the quantified benefits plan, bounded by Amdahl's
  Law, on top of it.
- **Elsewhere in the library** — `prioritizing-roadmap`, `technical-roadmaps`,
  `evaluating-trade-offs`.
- **References** — *The Principles of Product Development Flow: Second Generation Lean Product
  Development* (Reinertsen, 2009), Celeritas Publishing.
