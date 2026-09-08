---
name: consulting-constraint-analysis
description: >
  Theory of Constraints (Eliyahu Goldratt, *The Goal*, North River Press, 1984). Finds the one
  system constraint — the bottleneck that caps the whole process's throughput — and applies the
  Five Focusing Steps (Identify, Exploit, Subordinate, Elevate, repeat) so that automation
  investment targets the actual bottleneck instead of a non-constraint that only produces a
  local, cosmetic gain. Use after the process is mined and cost/time-baselined and candidate
  automations are designed, to prove the roadmap will move systemwide throughput, not just make
  a busy-looking step faster.
  Triggers - "where's the bottleneck", "theory of constraints", "TOC", "find the constraint",
  "are we automating the right step", "will this actually speed up the process", "Goldratt",
  "five focusing steps", "drum buffer rope", "local efficiency trap", "what's slowing this down",
  "is this a real bottleneck or a symptom", "throughput vs local optimization". Produces a
  constraint diagnosis one-pager: goal & throughput measure, identified constraint & evidence,
  exploit actions, subordination rules, elevate options mapped to candidate automations, and a
  next-constraint watch.
---

# Constraint Analysis (Theory of Constraints, Goldratt, 1984)

Every system — a factory floor or an office process — has exactly one, or very few, genuine
constraints: the weakest link that caps how fast the whole system can deliver its goal.
Eliyahu Goldratt laid this out as the Theory of Constraints (TOC) in his 1984 business novel
*The Goal* (North River Press) and formalized it in *Theory of Constraints* (North River Press,
1990). The counterintuitive, load-bearing claim is that improving anything that is *not* the
constraint produces no system-level gain at all — it just makes a non-bottleneck step pile up
more work-in-process in front of the next queue. Local efficiency is a trap. Only throughput at
the constraint moves the needle.

This matters directly to an automation roadmap: teams instinctively automate the step that
*feels* slow, is easiest to touch, or generates the most complaints — and often that step is not
the constraint. This skill forces the discipline of proving, with evidence from the mined
process and the cost/time baseline, which step is actually the constraint, before any candidate
automation is greenlit against it.

---

## Where this sits in the engagement

This is step 8 of 14, the last step of Phase B (Diagnosis). It draws on the mined as-is process
from `consulting-process-recovery` (step 2) — which shows where queues and waits actually build
— the economic baseline from `consulting-cost-time-baseline` (step 3) — which shows where time
and money concentrate — and the candidate automations and human/AI function allocations from
`consulting-automation-design` (step 7). Together these locate the system's constraint and test
whether the proposed automations actually relieve it. The output — the constraint plus its
exploit/subordinate/elevate plan — is the single most important input to
`consulting-roadmap-sequencing` (step 9): a candidate automation that doesn't touch the
constraint should be sequenced *after*, or dropped from, anything that does.

---

## When to use this skill

- You have mined process data and a cost/time baseline and need to know where the process's real ceiling is, not just where it feels slow.
- Automation-design (step 7) produced several candidate automations and you need to know which ones actually move systemwide throughput.
- A stakeholder wants to automate their own team's step because it's visible or painful, and you need evidence before agreeing.
- You suspect a proposed automation will just move the queue downstream rather than shrink the process's total cycle time.
- You need to sequence a roadmap (step 9) and want the highest-leverage initiative identified before you weight and rank anything.
- You're revisiting a process after a prior automation shipped, to check whether the constraint moved (the "go back to step 1" check).

---

## The method

**Three system measures.** TOC evaluates every decision against these, not local cost or
utilization:

| Measure | Definition |
|---|---|
| **Throughput (T)** | The rate at which the system generates goal units (money, cases closed, orders fulfilled) — not units produced, units *sold/delivered*. |
| **Inventory / Investment (I)** | Money tied up in the system: work-in-process, backlog, capital invested to produce throughput. |
| **Operating Expense (OE)** | Money spent turning inventory into throughput: labor, overhead, running cost. |

The governing rule: **local efficiency is a trap.** A non-constraint resource running at 100%
utilization does not raise throughput — it raises inventory and OE while the constraint still
caps what ships. Only throughput measured *at the constraint* is real progress.

**The Five Focusing Steps.**

1. **IDENTIFY** the system's constraint — the one resource, step, or policy that limits
   throughput for the whole system.
2. **EXPLOIT** the constraint — get the maximum output from it with no new investment (fix its
   scheduling, remove idle time, stop it working on low-value units, never let it starve or
   wait).
3. **SUBORDINATE** everything else to the decision in step 2 — every non-constraint step runs at
   the constraint's pace, not faster. Building inventory ahead of the constraint faster than it
   can consume is waste, not progress.
4. **ELEVATE** the constraint — invest, add capacity, or otherwise break the constraint once it
   is fully exploited and still limiting.
5. If the constraint breaks in step 4, **GO BACK TO STEP 1** — the constraint has moved.
   **Do not let inertia become the new constraint**: old rules, policies, and habits built around
   the *former* constraint often outlive it and quietly become the new limiting factor.

**Governing aphorism:** *"An hour lost at the bottleneck is an hour lost for the entire system;
an hour saved at a non-bottleneck is a mirage."*

**Drum-Buffer-Rope (DBR) scheduling.** The constraint is the **drum** — it sets the pace for the
whole system. A **buffer** of protective time or inventory sits just ahead of it so it never
starves. A **rope** ties the release of new work at the front of the process to the drum's pace,
so work-in-process doesn't pile up faster than the constraint can absorb it. For an office/
knowledge-work process, the drum is the constraint step, the buffer is a queue sized to protect
it from upstream variability, and the rope is a WIP limit or intake gate tied to the
constraint's actual throughput.

**Locating the constraint with steps 2 and 3.** The mined process (step 2) shows where queues and
wait times actually accumulate across cases — a step with a persistent backlog in front of it and
starvation behind it is a strong constraint signal. The cost/time baseline (step 3) shows where
time and cost concentrate and where capacity is fully consumed (little or no unused capacity).
The constraint is usually the step where both signals agree: high wait-time-before, high
utilization/no idle capacity, and material cost or time concentration.

---

## Workflow (what you do when invoked)

1. **Define the goal and throughput measure.** State, in one sentence, what "goal units" this
   process produces (cases closed, invoices paid, applications processed) and how throughput is
   measured (units/day, $/period). Confirm inventory (WIP/backlog) and operating expense are
   also defined for this process.
2. **Identify the constraint.** Cross-reference the mined process's queue/wait data (step 2)
   against the cost/time baseline's utilization and cost concentration (step 3). Name the single
   step (or very few steps) that caps throughput; state the evidence for each — do not accept a
   step as "the bottleneck" on reputation or complaint volume alone.
3. **Exploit.** List concrete, no-new-investment actions to squeeze maximum output from the
   constraint right now: eliminate idle time at that step, stop it processing low-priority work,
   fix scheduling/handoff delays immediately before or after it, remove non-constraint-caused
   interruptions.
4. **Subordinate.** Define the rules by which every other step runs at the constraint's pace:
   where to place a protective buffer (DBR), what WIP limit or intake gate ("rope") throttles new
   work releases, and which non-constraint local-efficiency metrics to stop optimizing for.
5. **Elevate — map to automation-design's candidates.** Take the candidate automations and
   human/AI function allocations from `consulting-automation-design` (step 7) and check each one
   against the constraint: does it add capacity or remove work *at the constraint itself*? Flag
   which candidates elevate the constraint, which merely speed up a non-constraint (a mirage),
   and which change the subordination rules needed elsewhere.
6. **Set the next-constraint watch.** Note what the constraint is expected to become once
   elevated, and name the inertia risk — which existing policy, SLA, or approval rule was built
   around the old constraint and needs to be revisited so it doesn't become the new limiting
   factor.
7. **Hand off.** Package the constraint diagnosis one-pager for `consulting-roadmap-sequencing`
   (step 9): the constraint, its evidence, and which candidate automations actually elevate it
   should dominate that step's sequencing weight.

---

## Deliverable & templates

**Constraint diagnosis one-pager**

```
GOAL & THROUGHPUT MEASURE
  Goal unit:           <e.g. loan applications funded>
  Throughput measure:  <e.g. applications funded / week>
  Inventory measure:   <e.g. applications in WIP>
  Operating expense:   <e.g. fully loaded team cost / period>

IDENTIFIED CONSTRAINT
  Step:                <name of step from the mined process / VSM>
  Evidence — queueing:  <wait time before this step, from process mining (step 2)>
  Evidence — capacity:  <utilization / unused capacity at this step, from TDABC (step 3)>
  Evidence — cost/time: <cost & time concentration at this step, from TDABC (step 3)>

EXPLOIT (no new investment)
  - <action>
  - <action>

SUBORDINATE
  Buffer placement (drum-buffer-rope): <where, and how sized>
  Rope / WIP limit / intake gate:      <rule>
  Local metrics to stop chasing:       <metric(s) at non-constraint steps>

ELEVATE — mapped to candidate automations (step 7)
| Candidate automation | Targets the constraint? | Effect |
|---|---|---|
| e.g. Auto-triage intake | No — targets intake, not underwriting | Mirage: shifts WIP into underwriting queue faster |
| e.g. AI-assisted underwriting review | Yes | Elevates constraint — adds effective capacity at the drum |

NEXT-CONSTRAINT WATCH
  Expected new constraint once elevated: <step>
  Inertia risk:                          <policy/SLA/rule built around old constraint to revisit>
```

---

## Pitfalls

- **Automating the loudest complaint, not the constraint.** The step people complain about most
  is often downstream of the real bottleneck, which is starving it — fix the evidence trail, not
  the noise.
- **Chasing local efficiency at non-constraints.** Speeding up or "utilizing" a non-bottleneck
  step produces no systemwide throughput gain and can even hurt it by flooding the constraint
  with more WIP than it can absorb.
- **Skipping Exploit before Elevate.** Jumping straight to "we need to automate/invest" without
  first squeezing free capacity from the constraint (fixing scheduling, removing starvation)
  wastes budget on a problem partly solvable for free.
- **Forgetting to subordinate.** Elevating the constraint while non-constraint steps keep running
  at their own pace just relocates the queue instead of shortening the process.
- **Letting inertia become the new constraint.** Once the original bottleneck is broken, old
  policies, approval rules, or SLAs built around it can silently become the new limiting factor —
  always run the "go back to step 1" check.
- **Treating "busy" as "constraint."** A step at 100% utilization is a candidate, not proof — cross
  -check against the mined queueing data (step 2) before naming it.

---

## Related

- **In-suite** — `consulting-process-recovery` (step 2, upstream): supplies the mined queue/wait
  evidence used to identify the constraint. `consulting-cost-time-baseline` (step 3, upstream):
  supplies the utilization and cost/time concentration evidence. `consulting-automation-design`
  (step 7, upstream): supplies the candidate automations mapped against the constraint in the
  Elevate step. `consulting-roadmap-sequencing` (step 9, downstream): sequences initiatives using
  the constraint diagnosis as its primary economic-value signal.
- **Elsewhere in the library** — `systems-thinking`, `capacity-modeling`, `performance-analysis`.
- **References** — Goldratt, E. M. & Cox, J., *The Goal*, North River Press, 1984; Goldratt, E. M.,
  *Theory of Constraints*, North River Press, 1990.
