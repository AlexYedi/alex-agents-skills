---
name: consulting-process-recovery
description: >
  Process mining (Wil van der Aalst; IEEE Task Force on Process Mining, "Process Mining
  Manifesto", 2011) reconstructs the de facto process from event logs and compares it to the
  de jure process people describe in interviews. This skill extracts and assesses an event log,
  runs discovery, conformance-checks it against the documented SOP, and enhances the model with
  timing and frequency to expose bottlenecks, rework, and hidden variants.
  Triggers - "what actually happens in this process", "process mining", "de facto vs de jure",
  "mine the event log", "discover the real process", "conformance checking", "why does the SOP
  not match reality", "spaghetti process", "find the rework loops", "event log readiness",
  "happy path vs exception path", "recover the as-is process", "variant analysis". Produces an
  event-log readiness checklist, a variant/hotspot table, and a de-facto-vs-de-jure findings note.
---

# Process Recovery (Process Mining, van der Aalst; IEEE Process Mining Manifesto, 2011)

Process mining (Wil van der Aalst; IEEE Task Force on Process Mining, *Process Mining
Manifesto*, 2011) sits between data mining and business process management: it reconstructs
what a process actually does from the digital trail it leaves behind, rather than from what
people say it does. The core move is distinguishing the **de facto** process — the one visible
in event logs — from the **de jure** process — the documented SOP or the idealized flow an
interview produces. Interviews give you intent; logs give you truth, including the long tail of
variants, rework loops, handoffs, and waiting that nobody mentions because it feels normal to
the people living inside it.

---

## Where this sits in the engagement

This is step 2 of 14, Phase A (Discovery). It takes the bounded process and value stream from
`consulting-boundary-setting` (1) — the SIPOC scope and swim lanes — and recovers the actual
as-is process from event data inside those boundaries. It feeds the economic baseline in
`consulting-cost-time-baseline` (3), which needs real step-by-step timing rather than the SOP's
idealized timing, and it feeds `consulting-constraint-analysis` (8), which needs to know where
the real bottlenecks and rework loops are, not where the org chart says they should be.

---

## When to use this skill

- The client has described a process in an interview or SOP and you need to verify it against
  what actually happens.
- Cycle times or defect rates are inconsistent with the documented flow and nobody can explain
  the gap.
- The client has a system of record (ticketing, ERP, CRM, workflow engine) that timestamps
  activity and no one has mined it yet.
- You suspect significant rework, looping, or informal escalation paths that don't appear on
  any process diagram.
- You need a quantified, evidence-based baseline before costing the process or hunting for its
  constraint — not another workshop-drawn flowchart.
- Stakeholders disagree about how the process runs, and the disagreement itself is diagnostic.

---

## The method

**Event log requirements.** Every event needs three fields at minimum:

| Field | Meaning |
|---|---|
| Case ID | The process instance the event belongs to (an order, a ticket, a claim) |
| Activity | The name of the step that occurred |
| Timestamp | When it occurred (start and/or complete) |
| Resource *(ideal)* | The actor or system that performed it |
| Other attributes *(ideal)* | Cost, priority, channel, outcome, etc. |

Events are ordered within a case by timestamp; a case's full ordered sequence of activities is
its **trace**. Getting a clean log — one Case ID scheme, consistent activity naming, reliable
timestamps — is the first practical hurdle in almost every engagement, and it is where most of
the elapsed time goes.

**Three types of process mining:**

1. **Discovery** — derive a process model directly from the log with no prior model to compare
   against. Standard algorithms: Alpha algorithm, Heuristic Miner, Inductive Miner. This is
   "play-in": log → model.
2. **Conformance checking** — replay the log against an existing (documented) model to find and
   quantify deviations. Produces a fitness score and a concrete list of where reality departs
   from the SOP. This is "replay": log on model → diagnostics.
3. **Enhancement / extension** — enrich an existing model with log-derived facts: bottleneck
   locations, activity/transition timing, frequencies, rework rates, resource handoff patterns.

A model can also be run forward — "play-out": model → generated behavior — to sanity-check that
a discovered or documented model actually produces traces consistent with the log.

Real logs from real systems almost always produce a **spaghetti model** on first discovery:
dozens or hundreds of variants tangled into an unreadable diagram. The job is not to present the
spaghetti — it's to separate the **happy path** (the small number of variants covering most
case volume) from the **exceptional tail** (the long list of rare, expensive, or rule-breaking
variants), and to name what's driving the tail.

**Manifesto principles (IEEE Task Force on Process Mining, 2011)**, summarized:

- Event data are first-class citizens — extract them with the same rigor as any other analytic
  dataset, not as an afterthought.
- Log extraction should be driven by concrete questions, not "extract everything and see."
- Models must support concurrency, choice, and other real control-flow constructs — real
  processes are not straight lines.
- Models are purposeful abstractions — a model built for bottleneck analysis need not be the
  model built for compliance checking.
- Process mining should be a continuous, living activity, not a one-off snapshot.

The Manifesto also names recurring challenges you should expect and budget for: finding,
merging, and cleaning event data from multiple systems; handling complex/spaghetti processes;
and concept drift — the process changing shape over the period the log covers, which can make a
single "as-is" model misleading if you don't segment by time window.

---

## Workflow (what you do when invoked)

1. **Confirm the questions the mining exercise must answer.** Anchor to the SIPOC/value stream
   from `consulting-boundary-setting`: which steps, which case type, which time window. Do not
   extract "everything" — extract to answer named questions (cycle time by step? rework rate?
   handoff delay? conformance to a specific SOP?).
2. **Locate and extract the event log.** Identify the system(s) of record, confirm you can get
   Case ID, Activity, and Timestamp (and ideally Resource) for the in-scope steps, and pull the
   data. Run the event-log readiness checklist (below) before trusting anything downstream.
3. **Run Discovery** to produce the de-facto model with no assumptions baked in. Expect spaghetti
   on the first pass — that's expected, not a failure.
4. **Conformance-check** the discovered log against the documented SOP or the process the client
   described in interviews. Quantify the fitness/deviation and list the specific divergence
   points (skipped steps, reordered steps, unauthorized loops).
5. **Enhance** the model with timing and frequency: attach average/median duration per step and
   transition, case volume per variant, rework counts, and resource handoff waits.
6. **Separate happy path from exception tail.** Rank variants by case volume; draw the line
   where the "happy path" ends and the long tail of exceptions begins; characterize what
   triggers the tail (channel, customer type, error condition, specific resource).
7. **Hand off.** Package the real process, the hotspot table, and the de-facto-vs-de-jure gap
   into the findings note for `consulting-cost-time-baseline` and `consulting-constraint-analysis`.

---

## Deliverable & templates

**1. Event-log readiness checklist**

```
[ ] Case ID field identified and consistent across source system(s)
[ ] Activity names identified and normalized (no duplicate labels for the same step)
[ ] Timestamps present, reliable, and at usable granularity (not date-only if step order matters)
[ ] Resource/actor field available (or explicitly noted as unavailable)
[ ] Time window covers a representative period (seasonality, drift checked)
[ ] Log extraction scoped to the SIPOC boundary agreed in step 1
[ ] Known data-quality issues logged (missing events, duplicate events, clock skew)
```

**2. Variant / hotspot table**

```
| Variant (activity sequence)     | % of cases | Avg duration | Rework? | Deviation from SOP        |
|----------------------------------|-----------|--------------|---------|----------------------------|
| A -> B -> C -> D                 | 62%       | 3.2 days     | No      | Matches SOP                |
| A -> B -> C -> B -> C -> D       | 18%       | 7.9 days     | Yes     | SOP has no loop back to B  |
| A -> B -> E -> C -> D            | 9%        | 5.1 days     | No      | Step E not in SOP          |
| (long tail, N variants)          | 11%       | varies       | mixed   | not individually mapped    |
```

**3. De-facto-vs-de-jure findings note (short, narrative)**

```
De jure (documented/assumed): <summary of the SOP or interview-described flow>
De facto (mined): <summary of what the log actually shows>
Fitness / conformance: <score or qualitative statement>
Top 3 deviations: <bulleted, with % of cases and cost/time impact where known>
Concept drift check: <did the process shape change materially within the log window?>
Handoff notes: <what steps 3 and 8 need to know>
```

---

## Pitfalls

- **Mining without a question.** Pulling the full log and hoping a model "tells you something"
  produces unreadable spaghetti and burns client trust. Anchor every extraction to a named
  question first.
- **Trusting timestamps blindly.** Batch-inserted records, clock skew across systems, and
  date-only granularity silently corrupt case ordering and duration math — check before you mine.
- **Presenting the spaghetti model to the client.** It's real, but it's not a deliverable — do the
  work of separating happy path from exception tail before it leaves your hands.
- **Treating the SOP as ground truth.** Conformance checking exists precisely because the
  documented process is often wrong or stale; report the deviation, don't assume the log is at
  fault.
- **Ignoring concept drift.** A log spanning a system migration, a policy change, or a seasonal
  peak can average together two genuinely different processes into one misleading model.
- **Stopping at Discovery.** Discovery alone tells you the shape of the process; without
  Enhancement (timing/frequency) you have no way to locate the bottlenecks or rework costs the
  downstream steps need.

---

## Related

- **In-suite** — `consulting-boundary-setting` (1): supplies the scoped process and value stream
  this mining exercise operates inside. `consulting-cost-time-baseline` (3): consumes the mined
  step-level timing and rework data to build the cost/time baseline. `consulting-constraint-analysis`
  (8): consumes the hotspot table to confirm the real bottleneck rather than the assumed one.
- **Elsewhere in the library** — `instrumentation`, `performance-analysis`, `observability-designer`.
- **References** — *Process Mining Manifesto* (IEEE Task Force on Process Mining, 2011); van der
  Aalst, *Process Mining: Data Science in Action* (Springer, 2016).
