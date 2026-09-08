---
name: consulting-task-decomposition
description: >
  The task-based framework from Autor, Levy & Murnane, "The Skill Content of
  Recent Technological Change: An Empirical Investigation" (Quarterly Journal
  of Economics, 118(4), 2003) — the "ALM" framework. Breaks the elicited work
  of a role or process into discrete tasks (not jobs) and classifies each on
  two axes — routine vs. non-routine, manual vs. cognitive — to isolate which
  tasks are structurally exposed to automation before anyone scores AI fit.
  Triggers - "decompose this job into tasks", "ALM framework", "Autor Levy Murnane",
  "routine vs non-routine tasks", "is this task routine or cognitive", "what are we
  actually automating, the job or the task", "task inventory", "break the role down
  into tasks", "list the discrete tasks in this process", "manual vs cognitive work",
  "job polarization", "which tasks are rules-based". Produces a task inventory table
  (task, inputs, outputs, volume, owner, routine flag, manual/cognitive flag, ALM
  category, first-look automation candidate).
---

# Task Decomposition (Task-Based Framework, Autor, Levy & Murnane, QJE, 2003)

David Autor, Frank Levy, and Richard Murnane's "The Skill Content of Recent
Technological Change: An Empirical Investigation" (*Quarterly Journal of
Economics*, 118(4), 2003) made one move that reorganizes how you scope an
automation engagement: the unit of analysis is the **task**, not the job. A
job is a bundle of tasks. You cannot automate "a job" — you automate or
augment specific tasks inside it, and different tasks in the same job behave
completely differently under computerization.

ALM classify tasks on two independent dimensions — routine vs. non-routine,
and manual vs. cognitive — and argue computerization substitutes for routine
tasks (rules-based, fully specifiable by explicit procedures) while
complementing workers on non-routine cognitive tasks (abstract reasoning,
complex communication, problem solving). Non-routine manual tasks — flexible
physical work — historically resisted codification entirely. This thesis
later underpins the job-polarization literature. This skill does the
classification; it does not score AI suitability — that judgment, an
explicit widening of ALM's "routine/codifiable" to "learnable from data," is
the next step's job.

---

## Where this sits in the engagement

This is Step 5 of 14, opening Phase B (Diagnosis) of the AI/automation
transformation engagement. It takes the real, tacit-inclusive work surfaced
by `consulting-tacit-work-elicitation` (Step 4) and converts it into a
structured task inventory. It hands that inventory to
`consulting-ai-suitability-scoring` (Step 6), which applies the SML
(Brynjolfsson & Mitchell) rubric to score each task's machine-learnability —
scoring only works once the tasks are correctly decomposed and classified
here.

---

## When to use this skill

- The engagement has been talking about "automating the role" instead of
  naming specific tasks inside it — a sign the unit of analysis is wrong.
- You have elicited work (documented and tacit) from Step 4 and need to turn
  it into something scoreable.
- Stakeholders conflate "this job will be automated" with "this job will
  disappear," and you need the task-level vocabulary to correct that.
- You need to separate what's structurally rules-based from what genuinely
  requires judgment, before anyone proposes a solution.
- A prior automation attempt targeted a whole workflow and stalled because it
  tried to force non-routine cognitive work through a rules engine.
- You need a defensible, first-look shortlist of automation candidates to
  hand to the suitability-scoring step.

---

## The method

**Central move: the job is a bundle of tasks.** Stop describing the unit of
work as a role, position, or process step. Every one of those is a bundle.
List the discrete tasks inside it — each one a single verb + object, one
action, one output.

### The two classification dimensions

Every task gets tagged on both axes, independently:

1. **Routine vs. non-routine** — can the task be fully specified by explicit,
   codifiable rules? Routine means a programmer could, in principle, write
   down the complete procedure in advance and it would work every time.
   Non-routine means the task requires responding to circumstances that
   cannot be fully anticipated or exhaustively enumerated in advance.
2. **Manual vs. cognitive** — is the task physical (manipulating objects,
   the physical world) or mental (analytic reasoning, interactive
   communication, judgment)?

### The four ALM categories

| Category | Routine? | Manual/Cognitive | Character | ALM's prediction under computerization |
|---|---|---|---|---|
| Routine cognitive | Routine | Cognitive | Rule-based mental work — bookkeeping, calculating, record-keeping, form processing | **Substituted.** Computers do this directly and cheaply. |
| Routine manual | Routine | Manual | Repetitive physical work — repetitive assembly, repetitive picking/sorting | **Substituted.** Historically automated first (machinery, then robotics). |
| Non-routine cognitive (analytic) | Non-routine | Cognitive | Abstract reasoning, pattern recognition under novel circumstances, forming and testing hypotheses | **Complemented.** Computerization raises productivity here rather than replacing the worker. |
| Non-routine cognitive (interactive) | Non-routine | Cognitive | Complex communication — persuading, negotiating, motivating, informing, caregiving | **Complemented.** Same logic — computers extend but do not replace this. |
| Non-routine manual | Non-routine | Manual | Flexible physical work requiring visual/spatial adaptation — e.g. janitorial work, truck driving (as of ALM's 2003 evidence base) | **Resistant to codification.** ALM found this the hardest category for computerization to touch. |

### Modern extension (bridge to Step 6)

ALM wrote in 2003, before modern machine learning. What they called
"routine/codifiable" — fully specifiable by explicit rules — is only one way
a task becomes tractable for a machine. Modern ML also handles tasks that are
**not** rule-specifiable but **are** statistically learnable from sufficient
labeled data (pattern recognition in non-routine cognitive-analytic tasks
being the clearest case — this is exactly why the "complements" side of
ALM's thesis is being renegotiated by AI). This skill's job is to classify
tasks correctly on ALM's original two axes. Whether a non-routine task is
nonetheless learnable from data is a distinct question, answered precisely
by the SML rubric in `consulting-ai-suitability-scoring` (Step 6). Do not
pre-judge suitability here — classify, then hand off.

### Recording each task

For every discrete task, capture:

- **Task** — verb + object, one action (e.g. "Reconcile invoice against
  purchase order," not "Handle accounts payable").
- **Inputs** — what triggers or feeds the task.
- **Outputs** — what the task produces.
- **Volume / frequency** — how often it happens (per day/week/transaction).
- **Current owner** — who does it today (role, not name).
- **Routine?** — Y/N, with a one-line justification.
- **Manual / Cognitive** — which, with sub-tag (analytic / interactive) if
  cognitive.
- **ALM category** — the resulting cell from the table above.
- **First-look candidate?** — Y/N flag: routine tasks (either manual or
  cognitive) are first-look automation candidates by ALM's own thesis; flag
  them, but do not score them yet.

---

## Workflow (what you do when invoked)

1. **Confirm scope.** Gather the role(s) or process step(s) in scope — pull
   directly from the Step 4 elicitation output (documented process plus
   tacit work). Do not start from a job title; start from the work.
2. **List discrete tasks.** For every piece of elicited work, write it as a
   single verb + object task. Split any item that bundles more than one
   action. This step alone often doubles or triples the apparent task count
   versus the original process map.
3. **Tag routine vs. non-routine.** For each task, ask: could this be fully
   specified by explicit rules, written down once, and followed every time
   without judgment calls? Justify the answer in one line.
4. **Tag manual vs. cognitive.** For each task, ask: is this physical work or
   mental work? If cognitive, note analytic (reasoning/pattern-finding) or
   interactive (communication/persuasion) where it matters.
5. **Assign the ALM category** from the four-cell table and record inputs,
   outputs, volume/frequency, and current owner for each task.
6. **Flag first-look candidates.** Mark every routine task (cognitive or
   manual) as a first-look automation candidate per ALM's substitution
   thesis — this is a flag, not a suitability score.
7. **Hand off the task inventory.** Package the full table for
   `consulting-ai-suitability-scoring` (Step 6), which will score every
   task — not just the flagged ones — for machine-learnability under the
   SML rubric.

---

## Deliverable & templates

**Task inventory**

| Task | Inputs | Outputs | Volume/Frequency | Owner | Routine? | Manual/Cognitive | ALM category | First-look candidate? |
|---|---|---|---|---|---|---|---|---|
| | | | | | Y/N | | | Y/N |
| | | | | | Y/N | | | Y/N |
| | | | | | Y/N | | | Y/N |

**ALM category tally** (roll-up for a quick read on the shape of the work)

| ALM category | Count | % of total task volume |
|---|---|---|
| Routine cognitive | | |
| Routine manual | | |
| Non-routine cognitive (analytic) | | |
| Non-routine cognitive (interactive) | | |
| Non-routine manual | | |

---

## Pitfalls

- **Decomposing at the job level, not the task level.** "Automate customer
  service" is not a task list. If any row in your inventory is a role name
  rather than a verb + object, you haven't decomposed yet.
- **Scoring suitability here instead of classifying.** This step answers
  "what kind of task is this," not "can AI do it." That question belongs to
  Step 6 — resist the urge to short-circuit straight to a suitability
  verdict.
- **Confusing "routine" with "simple" or "low-skill."** Some routine
  cognitive tasks (complex tax calculations, structured underwriting
  checklists) are highly skilled; some non-routine tasks (basic
  troubleshooting) are low-skill. Routine means codifiable, not easy.
- **Missing the interactive/analytic split inside non-routine cognitive.**
  Lumping "judgment" and "persuasion" into one bucket obscures that they
  fail or succeed differently under automation — keep the sub-tag.
- **Treating ALM's "resistant" verdict on non-routine manual as permanent.**
  ALM's evidence base is 2003-era; note it as the historical finding it is,
  not an assumption to import unexamined into a 2020s robotics or physical-
  AI context.
- **Skipping volume/frequency.** A task inventory without volume data can't
  be prioritized later — the roadmap-sequencing step downstream needs it.

---

## Related

- **In-suite** — `consulting-tacit-work-elicitation` (Step 4): the upstream
  source — its Critical Incident Technique and Contextual Inquiry outputs
  are the raw material this step decomposes into discrete tasks.
  `consulting-ai-suitability-scoring` (Step 6): the downstream consumer —
  takes every task in this inventory and scores it against the SML
  (Brynjolfsson & Mitchell) rubric for machine-learnability, independent of
  whether ALM would call it routine.
- **Elsewhere in the library** — `jtbd-strategy-and-organization`,
  `outcome-driven-innovation-and-job-mapping`.
- **References** — *The Skill Content of Recent Technological Change: An
  Empirical Investigation* (Autor, Levy & Murnane, 2003), Quarterly Journal
  of Economics, 118(4).
