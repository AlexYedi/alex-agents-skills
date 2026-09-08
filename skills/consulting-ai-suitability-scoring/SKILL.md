---
name: consulting-ai-suitability-scoring
description: >
  Applies the Suitability for Machine Learning (SML) rubric from Brynjolfsson & Mitchell
  ("What can machine learning do? Workforce implications," Science, 2017) and Brynjolfsson,
  Mitchell & Rock (AEA Papers & Proceedings, 2018) to score each task in a classified task
  inventory for fit with supervised ML. Separates high-SML automation candidates from
  low-SML tasks that stay human, at the task level rather than the job level.
  Triggers - "is this task automatable", "SML rubric", "score for machine learning", "AI
  suitability scoring", "can AI do this task", "which tasks should we automate", "Brynjolfsson
  Mitchell rubric", "how do we know if this is automatable", "machine learning suitability",
  "task automation candidates", "rate tasks for AI fit". Produces an SML scorecard ranking
  each task with a re-bundling recommendation per role.
---

# AI Suitability Scoring (SML Rubric, Brynjolfsson & Mitchell, Science, 2017; Brynjolfsson, Mitchell & Rock, 2018)

Brynjolfsson and Mitchell built the Suitability for Machine Learning (SML) rubric — a
21-question instrument applied to O*NET Detailed Work Activities to judge how well a task fits
supervised machine learning. Their finding, extended in the 2018 AEA Papers & Proceedings piece
with Rock, was that very few whole occupations are fully automatable end to end; most occupations
are a mix of high-SML and low-SML tasks bundled into one job description. This skill applies that
rubric to score each task in your inventory, so you target automation at the task level and
recommend re-bundling roles rather than replacing them.

---

## Where this sits in the engagement

This is step 6 of 14, the second step of Phase B (Diagnosis). It takes the classified task
inventory from `consulting-task-decomposition` (step 5) and rates each task's fit for machine
learning. The scored, ranked list of automation candidates it produces feeds directly into
`consulting-automation-design` (step 7), which chooses how much autonomy to grant each
high-SML task.

---

## When to use this skill

- You have a task inventory (from task decomposition) and need to decide which tasks are worth
  automating versus which stay human.
- A stakeholder asks "can AI actually do this?" about a specific task or role and wants more
  than a gut-check answer.
- You're pressure-testing a vendor or internal team's claim that a process is "AI-ready."
- You need to justify why an engagement is targeting specific tasks rather than replacing a job
  or department wholesale.
- Leadership is anxious about job displacement and needs the re-bundling framing (augment here,
  automate there) rather than a binary automate/don't-automate story.
- You're triaging a long backlog of candidate tasks and need a defensible, comparable score to
  rank them before committing engineering time.

---

## The method

**Source.** Brynjolfsson & Mitchell, "What can machine learning do? Workforce implications,"
*Science*, 358(6370), 2017; Brynjolfsson, Mitchell & Rock, "What Can Machines Learn, and What
Does It Mean for Occupations and the Economy?", *AEA Papers & Proceedings*, 108, 2018. The
original instrument is 21 questions rubric-scored against O*NET Detailed Work Activities. This
skill compresses those questions into the eight criteria below, scored 1–5 each, without
dropping any of the underlying judgment the 21 questions were probing.

A task is a **good ML fit** when it satisfies these key criteria:

1. **Well-defined inputs and outputs** — the task has a clear input and a clear output; the
   mapping between them can be stated precisely.
2. **Large digital datasets exist or can be created** that map those inputs to outputs — i.e.
   labels are available or obtainable at reasonable cost.
3. **Clear feedback with a quantifiable objective** — the task has a measurable goal, so a
   model (and its trainers) can tell success from failure.
4. **Does not require long chains of logic or reasoning** that depend on diverse background
   knowledge or common sense.
5. **Does not require detailed explanation** of how the decision was reached.
6. **Tolerant of error** — the task does not require a provably correct or optimal solution
   every time.
7. **The phenomenon being learned is stable** — it does not change rapidly over time.
8. **Does not require specialized dexterity**, physical skill, or mobility.

**Headline finding you must carry into the readout.** Very few whole occupations are fully
automatable. Most occupations are a mix of high-SML and low-SML tasks. The economic value comes
from **re-bundling** tasks — automating the high-SML ones, keeping humans on the rest, and often
creating new hybrid roles — not from replacing jobs wholesale. This is exactly why the engagement
scores at the **task level** (the inventory from step 5), not the job or role level.

**Scoring.** Score each task 1–5 on each of the eight criteria (5 = strongly favors ML fit, 1 =
strongly disfavors it). Aggregate to a normalized SML score (e.g. mean or sum, 0–100 scale).
Sort the task inventory by SML score. Tasks above your chosen threshold become automation
candidates and proceed to `consulting-automation-design`; tasks below it stay human or become
augmentation candidates (human does the task, AI assists).

---

## Workflow (what you do when invoked)

1. **Pull the task inventory** from `consulting-task-decomposition` — every task should already
   be classified routine/non-routine × manual/cognitive. If no inventory exists yet, send the
   user back to step 5 first.
2. **Score each task against the eight SML criteria**, 1–5 each. Interview the task owner or SME
   for criteria that aren't obvious from documentation alone — especially #2 (data availability)
   and #5 (explanation requirements), which are usually the ones people get wrong from a desk
   review.
3. **Aggregate to a normalized SML score per task** and rank the full inventory from highest to
   lowest.
4. **Set and apply a threshold** to split the ranked list into high-SML automation candidates
   and low-SML keep-human (or augment-human) tasks. Make the threshold and its rationale
   explicit — don't let it default silently.
5. **Flag data availability gaps** (low scores on criterion 2) as prerequisites, not
   disqualifiers — note what dataset or labeling effort would need to exist before the task can
   move forward.
6. **Write the one-line re-bundling recommendation per role** — which tasks in this role get
   automated, which stay human, and what the resulting hybrid role looks like.
7. **Hand the scored, ranked candidate list to `consulting-automation-design`** (step 7) for
   automation-level and function-allocation decisions on the high-SML tasks.

---

## Deliverable & templates

**SML scorecard** — one row per task from the inventory:

```markdown
| Task | Inputs/outputs defined (1-5) | Data available (1-5) | Clear feedback (1-5) | Reasoning depth (1-5, inverse-scored*) | Explanation needed (1-5, inverse-scored*) | Error tolerance (1-5) | Stability (1-5) | Dexterity required (1-5, inverse-scored*) | SML score | Candidate? |
|---|---|---|---|---|---|---|---|---|---|---|
| e.g. Classify inbound support ticket by category | 5 | 4 | 5 | 4 | 4 | 4 | 4 | 5 | 87 | Yes |
| e.g. Negotiate contract terms with enterprise client | 2 | 2 | 2 | 1 | 1 | 2 | 2 | 4 | 32 | No |

*Inverse-scored columns: 5 = task does NOT require long reasoning chains / detailed
explanation / dexterity (i.e. 5 is still the ML-favorable end of the scale).
```

**Re-bundling recommendation** — one line per role:

```markdown
**[Role name]:** Automate [task A, task B] (SML 80+); augment [task C] with AI-assisted
drafting; keep [task D, task E] fully human (SML <40, low data availability / high
explanation requirement). Resulting role shifts toward [judgment / exception-handling /
relationship work].
```

Hand both artifacts to `consulting-automation-design`.

---

## Pitfalls

- **Scoring the job, not the task.** If you score "customer service rep" as one unit you'll get
  a mushy, useless number. Score at the task grain the decomposition step already gave you.
- **Ignoring criterion 2 (data availability) until build time.** A task can score high on
  everything else and still stall for months because no labeled dataset exists — surface this
  as a prerequisite during scoring, not after a sprint is already planned.
- **Letting a high SML score imply full automation.** SML measures machine-learnability, not
  a mandate to remove humans — pair every high-SML flag with an automation-design decision
  (step 7) about the right level of human oversight.
- **Skipping the re-bundling narrative.** Presenting a flat list of automatable tasks reads as
  "we're automating your job" to stakeholders. Always close with the per-role re-bundling line —
  it's the headline finding, not an afterthought.
- **Treating "tolerant of error" as "doesn't matter."** Error tolerance is about whether the
  task needs a provably optimal answer every time, not about whether mistakes are cost-free.
  Don't let this criterion excuse sloppy scoring on high-stakes tasks.
- **Scoring from a desk review alone.** Several criteria (explanation requirements, reasoning
  depth, data availability) are invisible from a process doc — get the task owner or SME in the
  room.

---

## Related

- **In-suite** — `consulting-task-decomposition` (step 5) feeds this skill its task inventory,
  classified routine/non-routine × manual/cognitive. `consulting-automation-design` (step 7)
  takes this skill's high-SML candidates and decides the automation level and human–AI function
  allocation. `consulting-constraint-analysis` (step 8) later checks that automation-design's
  picks actually target the process bottleneck, not just the highest-scoring tasks.
- **Elsewhere in the library** — `ai-product-strategy`, `ai-build-vs-buy-and-model-adaptation`,
  `evaluating-new-technology`.
- **References** — *What can machine learning do? Workforce implications* (Brynjolfsson &
  Mitchell, 2017), Science, 358(6370); *What Can Machines Learn, and What Does It Mean for
  Occupations and the Economy?* (Brynjolfsson, Mitchell & Rock, 2018), AEA Papers &
  Proceedings, 108.
