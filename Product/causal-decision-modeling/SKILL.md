---
name: causal-decision-modeling
description: >
  Build a Causal Decision Diagram (CDD): identify levers, externals,
  intermediates, and outcomes; remove directionality; make elements
  measurable; manage system boundaries; annotate with decision assets
  (data, models, expertise); separate divergent and convergent thinking;
  handle stakeholder disagreement via ranges. Use when constructing or
  evaluating a CDD, facilitating a decision-modeling workshop, or
  translating an unstructured business problem into a decision blueprint.
  Triggers: "Causal Decision Diagram", "build a CDD", "decision modeling
  workshop", "lever vs external vs outcome", "make outcomes measurable",
  "decision asset register", "divergent and convergent thinking". Produces
  a workshop-ready CDD with annotations.
---

# Causal Decision Modeling

You apply Lorien Pratt's CDD construction methodology: a Causal Decision
Diagram is a **blueprint** that aligns stakeholders, exposes assumptions,
and structures the problem before any data work. You facilitate its
creation rigorously.

---

## When to Use This Skill

- Building a CDD for a real decision (Phase B of DI)
- Facilitating a decision-modeling workshop
- Translating an unstructured business question into a structured model
- Diagnosing why a decision conversation keeps stalling
- Annotating a CDD with available decision assets (data, models, expertise)

---

## CDD Components

```
[Lever] ──action──► [Intermediate] ──effect──► [Outcome]
                            ▲
                            │
                       [External]
```

| Element | Definition | Example |
|---|---|---|
| **Lever** | An action / decision the decision-maker controls | "Ad spend on channel X" |
| **External** | Factor outside the decision-maker's control that affects outcomes | "Competitor enters market" |
| **Intermediate** | A measurable interim state between lever and outcome | "Brand awareness in segment Y" |
| **Outcome** | The goal the decision aims to influence | "Gross revenue from new customers" |
| **Causal chain** | The directional link from cause to effect | An arrow with rationale |

**Crucial:** Distinguish elements you **control** (levers) from those you **don't** (externals) from **measurable interim states** (intermediates) from **goals** (outcomes). Mixing them is the most common modeling error.

---

## Making Elements Measurable

### Outcomes Must Be Measurable

❌ "Increase revenue"
✓ "Gross revenue (USD/quarter)"

The verb "increase" is direction, not outcome. Direction lives in the **objective statement**, separately.

### Levers Must Be Measurable

❌ "Marketing"
✓ "Marketing spend (USD/month) on channel X"

### Externals Must Be Measurable

❌ "The economy"
✓ "Consumer Confidence Index"

### Intermediates Must Be Measurable

❌ "Customer happiness"
✓ "NPS in segment X (0-100)"

If you can't measure it, you can't model causality through it.

---

## Remove Directionality from Outcomes

Direction (increase / decrease / improve / reduce) belongs in the **objective statement**, not the outcome.

**Why:** A CDD shows causality. Direction is what the lever does *to* the outcome — it's a property of the decision, not the variable.

```
Outcome:                          Objective:
──────────                        ─────────
Gross revenue (USD/quarter)       Maximize Gross revenue → $5M target
                                                            ↑
                                                        Direction lives here
```

This separation lets you simulate "what if we want to *minimize* revenue (maybe to defer recognition)?" — same outcome variable, different objective.

---

## Manage System Boundaries

Where does decision-maker control end? This determines lever-vs-external-vs-intermediate.

```
┌─────── System Boundary ───────────────┐
│                                        │
│   [Lever 1]   [Lever 2]   [Lever 3]   │   ← Inside: things you control
│       │           │           │        │
│       ▼           ▼           ▼        │
│   [Intermediate]  [Intermediate]       │   ← Inside: causal consequences
│       │                                │
│       ▼                                │
│   [Outcome 1]   [Outcome 2]            │   ← Inside: what you're optimizing
│                                        │
└──────────────┬─────────────────────────┘
               │
               ▼
        [External 1]   [External 2]         ← Outside: factors you don't control
        (these affect intermediates / outcomes
         but you can't change them)
```

**Move the boundary** when scope changes. A CMO has different levers than a CEO.

---

## The Decision Asset Register

After CDD is drafted, identify what assets populate each causal chain:

| Asset type | Examples |
|---|---|
| Mathematical models | Marketing mix model; price-elasticity model |
| ML models | Churn predictor; demand forecast |
| Sketch graphs | Hand-drawn relationships from a domain expert |
| Human expertise | "VP Sales says lead-time-to-close is X" |
| Empirical data | Historical CRM records, web analytics |
| Surveys / qualitative | Customer interviews; competitor war games |

Annotate each causal chain in the CDD with **icons** for the asset types that inform it.

```
[Lever: ad spend] ──[$ML demand model]──► [Intermediate: leads] ──[Sketch]──► [Outcome]
```

This makes data needs explicit. Gaps stand out: chains with no annotations need investigation.

---

## Divergent vs Convergent Thinking

CDD construction alternates between two modes. **Mixing them in the same conversation kills creativity.**

### Divergent (brainstorm phase)

- Generate many candidate elements without judgment
- "What could be a lever here?" — list 30
- "What could affect outcome X?" — list 50
- No criticism; no filtering; no causal arrows yet

### Convergent (analysis phase)

- Filter to relevant elements
- Cluster duplicates
- Draw causal arrows
- Make elements measurable
- Validate with stakeholders

**Facilitator's job:** Clearly announce which mode the room is in. "We're brainstorming — no objections yet" vs "We're refining — objections welcome."

---

## Iterative Refinement

CDDs evolve. **Low-fidelity first; refine.**

```
v0.1: Hand-drawn on whiteboard. 5 elements. Causality unclear.
       ↓
v0.5: Digital diagram. 15 elements. Causal arrows. Measurability rough.
       ↓
v1.0: Stakeholders aligned. Asset annotations. Ranges where disagreement exists.
       ↓
v2.0: After simulation feedback. Refined chains. Some elements removed.
       ↓
v3.0: Post-action retrospective updates.
```

Don't aim for v1.0 in the first workshop. Iterate.

---

## Handle Disagreement Respectfully

Stakeholders will disagree on:
- Whether something is a lever or external (control disputes)
- Causal direction (does A cause B or B cause A?)
- Magnitude of effect

**Don't force resolution. Capture the disagreement:**
- Causal arrow with annotation: "Sales VP: strong; Marketing VP: moderate"
- Element with range of opinions: "Lead conversion 5%-15% (depending on assumption set)"
- Multiple variants of the CDD: "Variant A assumes X; Variant B assumes Y"

Simulations later test which assumptions matter most. The disagreement that doesn't affect outcomes can be left unresolved.

---

## Balance Fidelity and Usefulness

Every additional element costs facilitation time. Documenting every nuance is rarely justified.

**Heuristic:** If removing the element wouldn't change the decision recommendation, remove it.

**Symptom of over-modeling:**
- 50+ elements
- Diagram unreadable
- Stakeholders disengage
- Months in workshops

**Symptom of under-modeling:**
- Key levers missing
- Externals ignored
- Simulations don't reveal trade-offs

The CDD should be just complex enough to support the decision.

---

## Animate the CDD with Low-Fidelity Software

Static CDDs lose attention. Animate them:
- Sliders on levers
- Real-time outcome update
- Highlight which causal chains are active

Even a low-fidelity simulation (Excel / Streamlit / Tableau) is dramatically more engaging than a static diagram.

This also defers the consensus burden — instead of demanding agreement on the CDD before proceeding, let stakeholders see dynamics and respond to results.

---

## Principles

- **Levers, externals, intermediates, outcomes** — distinguish religiously.
- **Make every element measurable.**
- **Direction lives in the objective, not the outcome.**
- **Manage system boundaries deliberately.**
- **Annotate with decision assets.**
- **Separate divergent and convergent thinking.**
- **Iterate. Low-fidelity first.**
- **Capture disagreement; don't force resolution.**
- **Balance fidelity and usefulness.**
- **Animate to engage stakeholders.**

---

## Anti-Patterns

### Mixing Element Types

**Looks like:** "Customer Satisfaction" listed as both lever and outcome.

**Why it fails:** Causality breaks; simulation results meaningless.

**The fix:** Strict typology. Customer satisfaction is an intermediate (you don't pull a lever on it directly).

### Outcomes With Direction

**Looks like:** Outcome = "Improve customer satisfaction."

**Why it fails:** "Improve" is direction. Causality is about what affects satisfaction, not the verb.

**The fix:** Outcome = "Customer satisfaction (NPS, 0-100)." Objective separately = "Maximize NPS."

### Vague Levers

**Looks like:** Lever = "Better marketing."

**Why it fails:** Not actionable. Can't measure. Can't simulate.

**The fix:** Lever = "Increase ad spend on Channel X by $Y/month."

### Ignoring System Boundaries

**Looks like:** "Competitor pricing" listed as a lever.

**Why it fails:** Competitor isn't your lever. Treating it as one produces nonsensical recommendations.

**The fix:** Competitor pricing is an external. Your levers respond to it.

### Elements With No Asset Annotations

**Looks like:** CDD has 30 causal chains; none annotated. No idea where data will come from.

**Why it fails:** Phase B isn't complete. Simulation will hit gaps.

**The fix:** Annotate every chain. Gaps become work items.

### Mixing Divergent and Convergent in One Session

**Looks like:** "Let's brainstorm levers... no, that one won't work because..."

**Why it fails:** Creativity stops. Useful candidates discarded.

**The fix:** Strict mode separation. Brainstorm first; critique later.

### Forcing Consensus Before Simulation

**Looks like:** "We can't proceed until everyone agrees the lever-to-outcome chain is right."

**Why it fails:** Stalemate. Months pass.

**The fix:** Capture as ranges or variant CDDs. Let simulation surface what matters.

### CDD as Document Theater

**Looks like:** CDD created in week 1. Filed in Confluence. Never updated.

**Why it fails:** Static; misses retrospective learning.

**The fix:** CDDs are living. Updated during monitoring (Phase D) and retrospective (Phase E).

---

## Decision Rules

| Situation | Action |
|---|---|
| Building a new CDD | Start with outcome (1 hour); levers (1 hour); externals (1 hour); intermediates last |
| Stakeholders can't agree on element type | Treat as a typology workshop; reach shared definition |
| Element seems both lever and outcome | Probably intermediate; or you have two CDDs |
| Direction in outcome statement | Move to objective statement |
| Vague lever like "improve marketing" | Refine to specific actions: "Increase Channel X spend by $Y/mo" |
| Workshop stalling | Probably mixed divergent/convergent; reset mode |
| Stakeholder disagreement | Capture as range or variant; don't force resolution |
| 50+ elements in CDD | Likely over-modeled; ask which to remove |
| 5 elements in CDD | Likely under-modeled; check for missing externals |
| Static CDD getting ignored | Animate; sliders on levers; real-time outcome update |
| Asset annotation missing | Phase B not complete; do Decision Asset Investigation |
| New stakeholder joins | Walk them through the CDD; don't restart |

---

## Worked Example: CDD for a Pricing Decision

**Context:** B2B SaaS. Considering a 15% price increase on the flagship plan. CMO and CFO disagree on whether it'll drive churn.

**CDD construction:**

```
LEVERS (controlled):
  - List price ($/seat/month)
  - Discount levels (% off list)
  - Grandfather policy for existing customers (yes/no)

EXTERNALS (not controlled):
  - Competitor pricing (current + 12-month projection)
  - Macroeconomic indicators (Consumer Confidence, B2B IT spend index)
  - Customer-base composition (SMB / Mid / Enterprise mix)

INTERMEDIATES:
  - Lead conversion rate (%)
  - Existing customer churn rate (%/quarter)
  - Average contract value (ACV, $)
  - Sales cycle length (days)

OUTCOMES:
  - Quarterly revenue (ARR delta, $/quarter)
  - Customer count (count, end of quarter)
  - Customer LTV (years × $/year)

OBJECTIVE:
  - Maximize Quarterly Revenue while keeping Churn ≤ 5%/quarter
```

**Asset annotations:**
- Lead conversion → ML model from Marketing Ops (1 year of data)
- Churn rate → Statistical model from CS team (3 years of data)
- Competitor pricing → Manual research (CRM + web scraping)
- ACV → Historical Salesforce data
- Sales cycle → Salesforce reports

**Disagreement captured:**
- CMO: "Price increase will drop conversion 5%"; CFO: "Drop conversion 15%"
- Captured as range: conversion impact = -5% to -15%

**Result:** Simulation explores both ends of the range. CMO's vs CFO's assumptions reveal which actions are robust across both scenarios.

**Lesson:** The disagreement was about magnitude, not direction. Capturing the range let both stakeholders watch the simulation; they converged on a recommendation neither would have predicted.

---

## Gotchas

- **CDDs aren't flowcharts.** Causal direction (A causes B) is different from process direction (A happens before B).
- **Tool support is rough.** Lucidchart / Miro for drawing; specialized DI tools (Quantellia DEXi) for animation. Spreadsheets work for small CDDs.
- **Workshops can run long.** A real CDD might take 3-5 sessions over 2 weeks for stakeholders to align.
- **Don't make every element a node.** Some are properties of nodes. Distinguishing is judgment.
- **Externals can become levers** when boundaries shift. A CMO's "competitor pricing" is a CEO's "M&A acquisition" lever sometimes.
- **Asset gaps are valuable** — they reveal where investment is needed.
- **Stakeholders use everyday language**, not technical. Resist jargon when capturing element names.
- **Animation tools matter.** Static CDDs in Confluence rot. Animated demos drive engagement.

---

## Further Reading

- *The Decision Intelligence Handbook* by Lorien Pratt
- *Link* by Lorien Pratt
- *The Fifth Discipline* by Peter Senge — systems thinking foundations
- See `decision-intelligence-fundamentals` for the 9-process methodology
- See `decision-simulation-and-monitoring` for what comes after CDD

Source: *Link* / *The Decision Intelligence Handbook* (Pratt), Phase B (Modeling).
