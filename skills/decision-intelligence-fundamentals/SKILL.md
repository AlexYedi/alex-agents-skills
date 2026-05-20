---
name: decision-intelligence-fundamentals
description: >
  Apply Lorien Pratt's Decision Intelligence (DI) methodology: the nine
  DI processes across five phases (A: Decision Requirements; B: Modeling;
  C: Reasoning; D: Action; E: Review), Action-to-Outcome decisions,
  Human-in-the-Loop hybrid decision-making, the Type III error trap, and
  the OODA loop framing. Use when a high-stakes decision needs structured
  analysis, when leadership keeps "answering the wrong question with great
  data," when AI/ML investments aren't translating into decisions, or when
  setting up a decision-making practice. Triggers: "Decision Intelligence",
  "structured decision-making", "Type III error", "action-to-outcome",
  "OODA loop", "human-in-the-loop AI", "we keep answering the wrong
  question". Produces a structured decision plan + roles for each DI
  process.
---

# Decision Intelligence Fundamentals

You apply Lorien Pratt's *Link* / *The Decision Intelligence Handbook*
methodology: high-stakes decisions are engineered, not improvised. DI's
nine processes across five phases (A-E) provide a repeatable scaffold for
moving from objective to monitored outcome.

---

## When to Use This Skill

- Scoping a high-stakes decision (strategic pivot, major investment, regulatory response)
- Avoiding the **Type III error** — answering the wrong question precisely
- Translating AI/ML capabilities into decisions
- Aligning stakeholders before action
- Establishing a decision-making practice in an organization
- Diagnosing why "data-rich, decision-poor" persists

---

## Decision Intelligence — Definition

**DI:** A methodology and set of processes/technologies for making better,
evidence-based decisions by helping decision-makers understand how *actions*
affect *outcomes*.

**Distinct from:** Decision analysis (statistics-heavy), decision support
(passive dashboards), decision automation (no human judgment).

**Defining frame:** **Action-to-Outcome decisions** — choices to take
irrevocable resource allocations to achieve specific outcomes. Distinct from
classification (categorizing) or regression (predicting a number).

---

## The Nine DI Processes (Five Phases)

```
Phase A — Decision Requirements
   Process A1: Decision Objective Statement (the trigger / initiative)
   Process A2: Decision Framing (constraints, boundaries, requirements)

Phase B — Decision Modeling
   Process B1: Decision Design (creates the initial CDD)
   Process B2: Decision Asset Investigation (identifies data, models, expertise)

Phase C — Decision Reasoning
   Process C1: Decision Simulation (understand system behavior + risks)
   Process C2: Decision Assessment (manage risk, sensitivity, uncertainty)

Phase D — Decision Action
   Process D1: Decision Monitoring (track results via KPIs / intermediates / outcomes)

Phase E — Decision Review
   Process E1: Decision Artifacts Retention (preserve information for reuse)
   Process E2: Decision Retrospective (assess and improve processes)
```

The phases roughly map to: **What are we deciding? → How are we modeling it? → What do we expect? → What's actually happening? → What did we learn?**

---

## The Causal Decision Design Document (CDD)

The **CDD is the blueprint** for the decision. It represents human expert knowledge in everyday language and structures causal chains:

```
[Lever 1] ─── causal chain ──► [Intermediate] ──► [Outcome 1]
[Lever 2] ─── causal chain ──► [Intermediate] ──► [Outcome 2]
                                       ▲
                                       │
                                  [External factor]
```

**Components:**
- **Levers** — actions / decisions / resource allocations the decision-maker controls
- **Externals** — factors outside the decision-maker's control that affect outcomes
- **Intermediates** — measurable interim states between levers and outcomes
- **Outcomes** — the goals the decision aims to influence
- **Causal chains** — the directional links among them

The CDD is what you align stakeholders around. Build it before discussing tools or data.

---

## Action-to-Outcome Decisions vs Other Types

| Type | Example | DI applies? |
|---|---|---|
| Action-to-Outcome | "Should we enter market X?" | **Yes — DI is built for this** |
| Classification | "Is this transaction fraudulent?" | No — ML classification |
| Regression | "What will sales be next quarter?" | No — forecasting |
| Decision Analysis | "What's the expected value of option A vs B?" | Adjacent — DI extends DA with causal modeling + monitoring |

DI's distinctive contribution: **continuous loop** from decision → model → simulate → act → monitor → learn.

---

## Human-in-the-Loop (Hybrid Decision-Making)

DI is explicitly **hybrid**:
- Humans bring authority, responsibility, judgment, context
- AI / models / data bring scale, recall, statistics, consistency

The CDD bridges them: humans articulate causal chains; models populate them with data; humans evaluate trade-offs.

**Anti-pattern:** Pure automation ("the model decides") or pure human ("trust me, I've been here 20 years"). DI insists on the loop.

---

## Type III Error

> Using all the right math to answer the wrong question.

(Type I = false positive. Type II = false negative. Type III is structural — wrong question entirely.)

**Symptoms:**
- Beautiful dashboards nobody acts on
- Models that are statistically valid but business-irrelevant
- Endless data-quality projects with no outcome change
- "Why are we measuring this?" silences

**Cure:** Start with the **decision** (Phase A), not the data. The CDD forces you to articulate what action-to-outcome you're trying to make. Data and models follow.

---

## OODA Loop Connection

```
OBSERVE  →  ORIENT  →  DECIDE  →  ACT  ─┐
   ▲                                       │
   └───────────────────────────────────────┘
```

John Boyd's military strategist's loop. DI maps it to:
- **Observe** — Phase D Decision Monitoring
- **Orient** — Phase B Decision Modeling, Phase E Decision Retrospective
- **Decide** — Phase C Decision Reasoning
- **Act** — Phase D Decision Action (the actual lever pull)

DI is OODA scaled up with causal modeling and monitoring discipline.

---

## Principles

- **Start with the decision, not the evidence.** Phase A first. Always.
- **Action-to-Outcome thinking.** Data must show the path from action to outcome, not just sit there.
- **Design before execution.** Treat decisions like engineering projects with blueprints (CDDs).
- **Problem-first, not technology-first.** Decision objective → CDD → assets → tooling. In that order.
- **Hybrid by default.** Humans + AI / models, not either alone.
- **Type III is the worst error.** Avoid by spending the time on Phase A.
- **Iterative, not waterfall.** CDDs evolve; monitor and refine.
- **Tailor template processes.** The 9 processes are templates; adapt to organizational culture.

---

## Anti-Patterns

### Skipping Phase A

**Looks like:** Diving into data analysis. Building dashboards. Running models. No clear decision in scope.

**Why it fails:** You answer the wrong question. Type III error.

**The fix:** Phase A1 (Objective) and A2 (Framing) before any data work.

### Tool-First DI

**Looks like:** "We bought Decision Intelligence software. Now what?" Tool selected before decisions identified.

**Why it fails:** Tools don't make decisions. The methodology does.

**The fix:** Pick a real decision. Walk it through the 9 processes. Buy tools when you know what you need.

### CDD as Documentation Theater

**Looks like:** CDD created at decision-time. Filed away. Never referenced again.

**Why it fails:** Static CDDs don't capture decision quality drift.

**The fix:** CDDs are living. Update during monitoring. Reference in retrospective.

### Pure Automation Decisions

**Looks like:** "The model will decide." No human authority. Drift goes unnoticed.

**Why it fails:** Models are trained on history. Reality drifts. Human judgment catches what the model misses.

**The fix:** Hybrid. Model recommends; human decides. Or model auto-decides within bounds; human reviews exceptions.

### Pure Intuition Decisions on High-Stakes Topics

**Looks like:** "I've been doing this 20 years; trust me." No model. No data. No CDD.

**Why it fails:** Intuition fails on novel situations and at scale. Bias goes unchallenged.

**The fix:** DI's CDD process forces articulation. Intuition expressed as a model becomes inspectable.

### One-and-Done Decisions

**Looks like:** Decision made. Action taken. Move on.

**Why it fails:** No monitoring; no retrospective; no learning.

**The fix:** Phases D and E are non-optional. Monitor; retrospect; reuse.

### Forcing Consensus Before Modeling

**Looks like:** "We can't proceed until everyone agrees on the CDD."

**Why it fails:** Stalemates. Months of meetings.

**The fix:** Capture disagreement as ranges or assumptions in the CDD. Simulate alternatives. Let the model surface conflicts.

---

## Decision Rules

| Situation | Action |
|---|---|
| Strategic decision worth > $1M / quarter | Full DI process (all 9 steps) |
| Repeated decision (e.g., quarterly) | Build reusable CDD; refine over cycles |
| One-time decision | Capture artifacts for context-transfer to similar future decisions |
| AI/ML investment not driving decisions | Type III diagnostic — go back to Phase A |
| Decision feels political | CDD makes assumptions explicit; surfaces disagreement |
| Multiple stakeholders, conflicting goals | Simulate interacting CDDs; show conflicts; force conversation |
| Pure automation proposal | Reject; insist on human-in-the-loop |
| Pure intuition proposal on $10M+ decision | Insist on CDD articulation |
| "We need more data" complaint | Phase A first; data scope follows decision scope |
| Decision-making is slow | Time-box phases. Low-fidelity CDDs are valid early. |
| Stakeholder won't engage | Use CDD as facilitation tool — animate it; show dynamics |

---

## Worked Example: Diagnosing "AI Investment Not Driving Decisions"

**Context:** F500 company. $50M AI investment over 3 years. ML models proliferating. Executive: "We're not getting decisions out of this."

**Diagnosis (DI lens):**

| Question | Finding |
|---|---|
| What decisions does the org make repeatedly? | Pricing, M&A, market entry, capacity planning, hiring |
| For each, do we have a CDD? | None. |
| Where does ML fit in those decisions? | Unclear; models exist but aren't tied to specific decisions |
| Type III error? | Yes — answering "what will sales be" when the decision is "where to expand." Forecast ≠ decision. |
| Hybrid or pure-AI/pure-human? | Pure-human in practice; AI dashboards ignored |
| Phase D monitoring? | Inconsistent; decisions made; outcomes not tracked |
| Phase E retrospective? | None |

**Plan:**
1. Pick the highest-leverage decision (pricing for the top product line)
2. Phase A — articulate the decision: levers, externals, outcomes
3. Phase B — build CDD with cross-functional stakeholders; identify which existing models populate which causal chains
4. Phase C — simulate; surface where ML adds the most value
5. Phase D — pilot with monitoring; track ground truth vs prediction
6. Phase E — retrospective at 90 days; refine CDD; reuse template for next product line

**Result:** First pricing decision improved by ~8% margin via better lever selection. Replicate to other product lines.

**Lesson:** AI investment doesn't translate to decisions without DI scaffolding. The CDD is the bridge.

---

## Gotchas

- **DI vocabulary is dense.** "Lever," "intermediate," "external," "outcome" are precise terms. Misuse confuses stakeholders.
- **CDDs are not flowcharts.** Causal direction matters; flow charts often have arrows for "what happens next" rather than "what causes what."
- **The 9 processes are templates, not gospel.** Pratt explicitly says tailor them.
- **Phase A is hard.** Stakeholders want to skip to data. Resist.
- **Hybrid decision-making requires authority clarity.** Who decides when model and human disagree?
- **DI tooling is an emerging market.** Tools exist (Quantellia, others) but don't substitute for the methodology.
- **Don't confuse DI with Decision Analysis.** DA is statistical (utility, expected value); DI is causal modeling + monitoring + reuse.
- **CDDs can be over-engineered.** Pratt recommends low-fidelity versions early; refine as needed.

---

## Further Reading

- *The Decision Intelligence Handbook* by Lorien Pratt
- *Link* by Lorien Pratt — earlier, more accessible book
- See `causal-decision-modeling` for CDD construction details
- See `decision-simulation-and-monitoring` for simulation, sensitivity, monitoring

Source: *Link* / *The Decision Intelligence Handbook* (Pratt).
