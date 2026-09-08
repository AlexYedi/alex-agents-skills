---
name: consulting-boundary-setting
description: >
  SIPOC scoping (Six Sigma DMAIC Define) combined with Value Stream Mapping
  (Rother & Shook, "Learning to See", Lean Enterprise Institute, 1999). Fixes
  the process start/end trigger events, builds the one-page SIPOC scope
  agreement, then maps the current-state flow of material and information to
  expose lead time, value-added time, and waste.
  Triggers - "scope this engagement", "SIPOC", "where does this process start and end",
  "value stream map", "current state map", "what's in scope and out of scope",
  "map the process end to end", "who are the suppliers and customers of this process",
  "before we dig in let's bound the problem", "draw the as-is flow", "process boundary",
  "kick off the discovery phase", "define the process family". Produces a signed-off
  SIPOC table plus a current-state VSM summary with lead time, VA time, and process
  cycle efficiency.
---

# Boundary Setting (SIPOC + Value Stream Mapping, Rother & Shook, 1999)

SIPOC is the Six Sigma DMAIC Define-phase scoping tool: five columns — Suppliers,
Inputs, Process, Outputs, Customers — built to fix the boundary of a process before
anyone tries to improve it. Value Stream Mapping, from Mike Rother and John Shook's
*Learning to See: Value Stream Mapping to Add Value and Eliminate Muda* (Lean
Enterprise Institute, 1999), is the pencil-and-paper discipline of mapping the material
and information flow for one product or service family, current-state first, to see
where time and waste actually accumulate.

This skill runs them in sequence, on the same process, in the same session: SIPOC
draws the box, VSM fills in what happens inside it.

---

## Where this sits in the engagement

This is Step 1 of 14, opening Phase A (Discovery) of the AI/automation transformation
engagement. It is the entry point — nothing upstream feeds it. It hands a bounded
process and a current-state map to `consulting-process-recovery` (Step 2, recovers the
actual as-is process from event logs), `consulting-cost-time-baseline` (Step 3, prices
each step in cost and time), and `consulting-tacit-work-elicitation` (Step 4, captures
the undocumented work inside those steps).

---

## When to use this skill

- Kicking off a new engagement and nobody has agreed, in writing, where the process starts and ends.
- Stakeholders disagree about what's in scope ("is onboarding part of this or not?").
- You need a one-page artifact everyone — sponsor, process owner, frontline staff — signs off on before deeper analysis begins.
- The client wants to "map the process" but has no current-state diagram, or has one that shows only the happy path.
- You need a defensible baseline (lead time, VA time, waste) to compare a future-state redesign against.
- A prior improvement effort stalled because it optimized a sub-step nobody had agreed was in scope.

---

## The method

### 1. SIPOC — fix the boundary

Five columns, built **right-to-left**: start from the Customer and the Outputs they
require, then work back through Process, Inputs, and Suppliers.

| Suppliers | Inputs | Process (5–7 steps) | Outputs | Customers |
|---|---|---|---|---|
| Who provides what the process consumes | What they provide (materials, data, requests) | High-level steps only — no more than 5–7 | What the process produces | Who receives the output |

Rules:
- **Process column is high-level only** — 5 to 7 steps, verb-noun phrases (e.g. "Validate
  application"), never a detailed procedure. If you're writing more than 7 steps you're
  scoping a VSM, not a SIPOC.
- The first and last Process steps **define the trigger events** — the specific event
  that starts the process (an order lands, a ticket is opened) and the event that ends
  it (payment posted, ticket closed). This is the actual deliverable of SIPOC: a fixed
  start and end everyone agrees to.
- Everything before the start trigger or after the end trigger is explicitly **out of
  scope** — name it, don't just omit it, so nobody assumes it's included.
- SIPOC output is a **one-page scope agreement** the sponsor and process owner sign off
  on before deeper work starts.

### 2. Value Stream Mapping — map the flow inside the boundary

Draw the flow for **one product or service family** (not every variant) between the
start and end triggers SIPOC just fixed.

**Current-state map first, always** — a future-state map or action plan without a
validated current-state map is fiction. Standard symbols:

- **Process boxes** — one per processing step, with a **data box** underneath carrying:
  - C/T — cycle time
  - C/O — changeover time
  - Uptime %
  - Number of operators
- **Inventory / queue triangles** — where work waits between steps.
- **Push arrows vs. pull/supermarket** — how work moves from step to step: pushed
  regardless of downstream readiness, or pulled only when downstream signals capacity.
- **Information flows** — manual (paper, phone, email) vs. electronic, drawn separately
  from the material/work flow because they often move on different cadences.
- **Timeline at the bottom**, split into two rails:
  - **Value-added time** — time actually transforming the work product (the process
    boxes' cycle times).
  - **Non-value-added time** — everything else: queues, waiting, rework, approvals
    sitting in an inbox.

### 3. Compute the headline metrics

- **Lead Time** = total elapsed time from trigger start to trigger end (VA + NVA, all
  queue time included).
- **Value-Added Time** = sum of cycle times across process steps that actually transform
  the work product for the customer.
- **Process Cycle Efficiency** = Value-Added Time / Lead Time. Low PCE (frequently
  single digits or low double digits in white-collar processes) is where the opportunity
  lives — the gap between lead time and VA time.
- **Takt Time** = available work time / customer demand. Sets the pace the process
  needs to run at to match demand; compare each step's cycle time against it to spot
  the pacing bottleneck.
- Hunt the **7 wastes (muda)** at each queue and handoff: overproduction, waiting,
  transport, over-processing, inventory, motion, defects.

---

## Workflow (what you do when invoked)

1. **Agree the process family and its trigger events.** Ask: what single product/service
   family are we mapping, and what event starts it, what event ends it? Do not proceed
   until you have both in one sentence each.
2. **Build the SIPOC right-to-left.** Start with Customers and Outputs, work back through
   the 5–7 Process steps, then Inputs and Suppliers. Fill the template below live with
   the user.
3. **Validate in/out of scope with the room.** Read the SIPOC back, name explicitly what
   sits just before the start trigger and just after the end trigger, and confirm it's
   excluded. Get sign-off before moving on.
4. **Draw the current-state VSM.** Walk each Process step from the SIPOC, add the data
   box (C/T, C/O, uptime, operators), mark the queue/inventory before each step, note
   push vs. pull, and layer in the information flow.
5. **Compute the three headline metrics** — Lead Time, Value-Added Time, Process Cycle
   Efficiency — plus Takt Time if demand data is available.
6. **Mark the biggest waste and the biggest queue.** Flag which gap between VA time and
   wait time is largest — that's the first place downstream steps should look.
7. **Hand off the bounded map.** Package the SIPOC table, the VSM summary table, and the
   headline metrics as the shared as-is baseline for Steps 2–4.

---

## Deliverable & templates

**SIPOC one-pager**

| Suppliers | Inputs | Process | Outputs | Customers |
|---|---|---|---|---|
| | | 1. [START TRIGGER] | | |
| | | 2. | | |
| | | 3. | | |
| | | 4. | | |
| | | 5. [END TRIGGER] | | |

**Out of scope (explicit):** — list what sits immediately before the start trigger and
after the end trigger.

**Current-state VSM summary**

| Step | Cycle time | Wait before | VA? | Notes |
|---|---|---|---|---|
| 1. | | | Y/N | |
| 2. | | | Y/N | |
| 3. | | | Y/N | |
| 4. | | | Y/N | |
| 5. | | | Y/N | |

**Headline metrics**

| Metric | Value |
|---|---|
| Lead Time | |
| Value-Added Time | |
| Process Cycle Efficiency (VA/Lead) | |
| Takt Time (if demand known) | |

---

## Pitfalls

- **Writing a detailed procedure instead of 5–7 SIPOC steps.** If the Process column has
  15 rows, you've started the VSM early and skipped the scoping conversation.
  Boundary-setting and flow-mapping are sequential, not the same exercise.
- **Skipping the current-state map and jumping to future-state.** Rother & Shook are
  explicit: you cannot design a credible future state without a validated current-state
  map. Teams that skip it design against assumptions, not evidence.
- **Leaving the start/end trigger events vague** ("when the request comes in" — from
  where, in what form?). A fuzzy trigger means every downstream step's data is
  unreproducible.
- **Building the SIPOC left-to-right from Suppliers.** This tends to scope the process
  around what's convenient to measure rather than what the customer actually needs;
  right-to-left from the Customer keeps scope honest.
- **Mapping every product variant at once.** VSM is for one product/service family. A map
  that tries to show all variants collapses into a flowchart of exceptions and loses the
  timeline discipline that makes VSM useful.
- **Not getting sign-off on out-of-scope items.** Undocumented exclusions resurface later
  as scope disputes; naming them explicitly on the one-pager prevents that.

---

## Related

- **In-suite** — `consulting-process-recovery` (Step 2): takes the SIPOC's bounded
  process and the VSM's steps and recovers what actually happens from event-log data,
  checking the map against reality. `consulting-cost-time-baseline` (Step 3): prices
  each VSM step in cost and time using Time-Driven ABC. `consulting-tacit-work-elicitation`
  (Step 4): digs into the undocumented work happening inside the steps this map only
  sketches at a high level.
- **Elsewhere in the library** — `problem-definition`, `journey-mapping`,
  `systems-thinking`, `capacity-modeling`.
- **References** — SIPOC: Six Sigma / DMAIC Define phase, popularized via GE, rooted in
  Rummler & Brache process mapping. *Learning to See: Value Stream Mapping to Add Value
  and Eliminate Muda* (Rother & Shook, 1999), Lean Enterprise Institute.
