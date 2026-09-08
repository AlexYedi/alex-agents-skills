---
name: consulting-automation-design
description: >
  Applies Sheridan & Verplank's 10 Levels of Automation (1978) and the Parasuraman,
  Sheridan & Wickens four-stage model (IEEE SMC-A, 2000) to decide how much to automate
  each high-SML task and how to split acquire/analyze/decide/act work between human and
  machine. Evaluates each design against workload, situation awareness, complacency, and
  skill-degradation costs before locking the function allocation.
  Triggers - "how much should we automate this", "levels of automation", "human in the loop
  design", "should this be fully autonomous", "Sheridan Verplank scale", "Parasuraman Sheridan
  Wickens", "where does the human stay in control", "function allocation", "automation vs
  augmentation", "how autonomous should the agent be", "keep a human in the loop", "escalation
  triggers for automation". Produces a per-task automation-design table (LOA per processing
  stage, reliability, consequence cost, human-in-loop points, escalation triggers).
---

# Automation Design (Levels of Automation, Sheridan & Verplank, 1978; Parasuraman, Sheridan & Wickens, IEEE, 2000)

Automation is not a binary switch. Sheridan & Verplank's 1978 MIT report on undersea
teleoperator control gave the field its founding scale: 10 discrete levels running from full
human control to full machine autonomy that ignores the human entirely. Parasuraman, Sheridan
& Wickens (2000) then showed the scale has to be applied separately to four distinct stages of
information processing — a system can acquire data autonomously while keeping decisions fully
human, or vice versa — and gave the human-factors criteria for choosing each level correctly.

This skill uses both together: for every task that scored high on AI suitability, it picks a
level per processing stage, stress-tests that choice against human-performance costs, and
locks a function allocation the delivery team can build to.

---

## Where this sits in the engagement

Step 7 of 14, Phase B (Diagnosis). It takes the high-SML candidate tasks scored by
`consulting-ai-suitability-scoring` (step 6) and decides how much to automate and how to split
work between human and machine. It feeds `consulting-constraint-analysis` (step 8), which
checks the design actually attacks the real bottleneck, and `consulting-agent-contract`
(step 12), which turns the function allocation into formal pre/postconditions.

---

## When to use this skill

- A task has cleared the AI-suitability bar and the next question is "how much do we hand over."
- Stakeholders are debating full autonomy vs. a human-approval step and need a structured answer.
- You need to decide where an agent should stop and escalate to a person.
- A prior automation rollout caused complacency, skill loss, or missed exceptions — you're
  redesigning the human's role, not just the machine's.
- Legal, safety, or reversibility concerns mean some tasks need conservative levels even though
  they are technically automatable.
- You're specifying inputs for a Design-by-Contract agent spec and need the human-in-the-loop
  points defined first.

---

## The method

### 1. Sheridan & Verplank's 10 Levels of Automation (LOA)

Reproduce exactly — this is the canonical decision/action-selection scale:

1. The computer offers no assistance; the human must take all decisions and actions.
2. The computer offers a complete set of decision/action alternatives, or
3. narrows the selection down to a few, or
4. suggests one alternative, and
5. executes that suggestion if the human approves, or
6. allows the human a restricted time to veto before automatic execution, or
7. executes automatically, then necessarily informs the human, and
8. informs the human only if asked, or
9. informs the human only if it, the computer, decides to.
10. The computer decides everything and acts autonomously, ignoring the human.

### 2. Parasuraman, Sheridan & Wickens — four stages, each with its own level

Automation is not one dial. It applies independently to four stages of information
processing, and each stage can sit at a different LOA (1–10):

1. **Information acquisition** — sensing, gathering.
2. **Information analysis** — inference, prediction, integration.
3. **Decision and action selection.**
4. **Action implementation.**

A system can run acquisition and analysis near level 10 while holding decision/selection at
level 4–6 — that asymmetry is the whole point of the model.

### 3. Evaluate the design

**Primary evaluative criteria — human-performance consequences:**
- Mental workload
- Situation awareness
- Complacency
- Skill degradation

**Secondary criteria:**
- Automation reliability
- Costs of decision/action consequences

Iterate the levels up or down per stage until human-performance costs are acceptable. High
autonomy on the decide/act stages is dangerous when reliability is imperfect and the cost of a
wrong action is high — keep a human in the loop there even if acquisition and analysis run
near-autonomous.

---

## Workflow (what you do when invoked)

1. Pull each high-SML candidate task from step 6 (`consulting-ai-suitability-scoring`).
2. For each task, walk the four processing stages — acquire, analyze, decide, act — and pick a
   target LOA (1–10) per stage.
3. Assess automation reliability for that stage and the consequence cost of a wrong output.
4. Apply the primary criteria — workload, situation awareness, complacency, skill decay — and
   push levels down (toward human involvement) wherever reliability is unproven or consequence
   cost is high; push up where the task is low-stakes and well-validated.
5. Define the concrete human-in-the-loop points (what the human sees, when, and what they can
   veto or approve) and the escalation triggers (what condition kicks the task back to a human).
6. Record the function-allocation design in the deliverable table below.
7. Hand the table to `consulting-constraint-analysis` (does this design attack the real
   bottleneck?) and `consulting-agent-contract` (turn the human-in-loop points and escalation
   triggers into formal pre/postconditions).

---

## Deliverable & templates

```
| Task | Acquire LOA | Analyze LOA | Decide LOA | Act LOA | Reliability | Consequence cost | Human-in-loop points | Escalation trigger |
|------|-------------|-------------|------------|---------|-------------|-------------------|-----------------------|---------------------|
|      |             |             |            |         |             |                   |                       |                     |
```

For each row, also capture in a short note:
- Which primary criterion (workload / situation awareness / complacency / skill degradation)
  drove the level down, if any.
- The rationale for any stage sitting above level 7 (autonomous-then-inform or higher).

---

## Pitfalls

- **Treating automation as one dial.** Setting a single "automation level" for a task instead
  of separate levels per stage hides where the real risk sits (usually decide/act, not acquire).
- **Automating the decide/act stages first.** These carry the highest consequence cost; raise
  levels there last, after acquisition and analysis automation has proven reliable.
- **No escalation trigger defined.** A level-6/7 design without a concrete condition for
  handing control back to a human silently drifts into unsupervised level 9/10 behavior.
- **Ignoring complacency and skill degradation.** High autonomy that "informs only if asked"
  (level 8) erodes human vigilance and ability to intervene when the system does fail.
- **Setting levels once and never revisiting.** Reliability changes as the system is used —
  the P-S-W evaluation is meant to be iterated, not a one-time sign-off.
- **Confusing high SML with high LOA.** A task being machine-learnable (step 6) does not by
  itself justify a high decision/action LOA; that call rests on reliability and consequence cost.

---

## Related

- **In-suite** — `consulting-ai-suitability-scoring` (step 6, upstream): supplies the high-SML
  candidate tasks this skill designs automation levels for. `consulting-constraint-analysis`
  (step 8, downstream): checks the resulting function allocation actually targets the process
  bottleneck. `consulting-agent-contract` (step 12, downstream): formalizes the human-in-loop
  points and escalation triggers as pre/postconditions and invariants.
- **Elsewhere in the library** — `ai-agent-design-patterns`, `multi-agent-orchestration`,
  `agent-memory-and-guardrails`.
- **References** — *Human and Computer Control of Undersea Teleoperators* (Sheridan &
  Verplank, MIT Man-Machine Systems Laboratory, 1978); "A Model for Types and Levels of Human
  Interaction with Automation" (Parasuraman, Sheridan & Wickens, IEEE Transactions on Systems,
  Man, and Cybernetics — Part A, 30(3), 2000).
