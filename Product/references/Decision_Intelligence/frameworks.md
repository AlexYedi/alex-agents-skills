# Decision Intelligence — Frameworks Catalog

## Index

| Name | Phase / Domain |
|---|---|
| Action-to-Outcome Decisions | Foundations |
| Causal Decision Diagram (CDD) | Phase B |
| Causal Decision Design Document | Phase B |
| Decision Asset Register | Phase B |
| Decision Assessment | Phase C2 |
| Decision Design | Phase B1 |
| Decision Framing | Phase A2 |
| Decision Intelligence (DI) | Foundations |
| Decision Monitoring | Phase D1 |
| Decision Objective Statement | Phase A1 |
| Decision Quality Drift | Phase D/E |
| Decision Quality Report | Phase E |
| Decision Retrospective | Phase E2 |
| Decision Review | Phase E |
| Decision Simulation | Phase C1 |
| Digital Twin | Phase C |
| Divergent vs Convergent Thinking | Phase B (process) |
| Five Phases (A-E) | Methodology |
| Ground Truth | Phase D/E |
| Hybrid Decision-Making | Foundations |
| Human-in-the-Loop | Foundations |
| Known Unknowns / Unknown Knowns / Unknown Unknowns | Phase C |
| Lobster Claw Pattern | Anti-pattern |
| Nine DI Processes | Methodology |
| OODA Loop | Foundations |
| Opportunity vs Cost Envelope | Phase C |
| Outcome Bias | Anti-pattern |
| Sensitivity Analysis | Phase C2 |
| Silos / Whack-a-Mole / Measurement Effect | Anti-pattern |
| Type III Error | Foundations |

## Catalog

### Decision Intelligence (DI)
**Origin:** Lorien Pratt, ~2010s.
**Definition:** Methodology + processes + technologies for evidence-based decisions linking actions to outcomes.
**Distinct from:** Decision analysis (statistical), decision support (passive), decision automation (no human).

### The Five Phases
- **A:** Decision Requirements (A1 Objective, A2 Framing)
- **B:** Decision Modeling (B1 Design, B2 Asset Investigation)
- **C:** Decision Reasoning (C1 Simulation, C2 Assessment)
- **D:** Decision Action (D1 Monitoring)
- **E:** Decision Review (E1 Artifacts Retention, E2 Retrospective)

### Action-to-Outcome Decisions
**Definition:** Choices to take irrevocable resource allocations to achieve specific outcomes.
**Distinct from:** Classification decisions (categorize), Regression decisions (predict).

### Hybrid Decision-Making (Human-in-the-Loop)
**Structure:** Humans (authority, judgment) + AI/models (scale, recall) in loop.
**Anti-pattern:** Pure automation OR pure intuition.

### Type III Error
**Definition:** "Using all the right math to answer the wrong question."
**Cause:** Skipping Phase A.
**Cure:** Decision-first, not data-first.

### OODA Loop
**Origin:** John Boyd, military strategist.
**Stages:** Observe → Orient → Decide → Act.
**DI mapping:** Observe = Phase D Monitoring; Orient = Phase B Modeling + Phase E Retrospective; Decide = Phase C Reasoning; Act = Phase D Action.

### Causal Decision Diagram (CDD) / Causal Decision Design Document
**Components:** Levers / Externals / Intermediates / Outcomes / Causal chains.
**Purpose:** Blueprint aligning stakeholders.

### CDD Components
| Element | Definition |
|---|---|
| Lever | Action / decision the decision-maker controls |
| External | Factor outside decision-maker's control |
| Intermediate | Measurable interim state |
| Outcome | Goal the decision aims to influence |
| Causal Chain | Directional link cause → effect |

### Decision Asset Register
**Purpose:** Track data, models, expertise that populate causal chains.
**Asset types:** Mathematical models, ML models, sketch graphs, human expertise, empirical data, surveys.

### Digital Twin
**Definition:** Computerized version of CDD for simulation.

### Divergent vs Convergent Thinking
**Divergent:** Brainstorm; generate without judgment.
**Convergent:** Filter, refine, validate.
**Rule:** Don't mix in same session.

### Decision Simulation
**Purpose:** Understand system behavior + risks before action.
**Outputs:** Outcome envelope, sensitivity table, risk surface.

### Sensitivity Analysis
**Purpose:** Identify which elements most affect outcomes.
**Use:** Concentrate accuracy on high-sensitivity elements.

### Opportunity vs Cost Envelope
**Visualization:** Heavy boundary = profit potential; lighter = loss scenarios.

### Known / Unknown Knowns / Unknowns
**Known unknowns:** Need value, uncertain.
**Unknown knowns:** Known to group, not top-of-mind.
**Unknown unknowns:** Entirely unrecognized (e.g., pandemic).

### Lobster Claw Pattern
**Anti-pattern:** Short-term gain → long-term loss.
**Cause:** Missed feedback loops; short simulation horizon.
**Mitigation:** Long-horizon simulation.

### Silos / Whack-a-Mole / Measurement Effect
**Anti-pattern:** Local KPIs without causal-chain analysis → global conflicts.
**Mitigation:** Cross-department CDDs; align before setting KPIs.

### Decision Monitoring
**Track:** Levers (actuals), intermediates (leading), outcomes (lagging).
**Define:** Safe / warning / unsafe ranges.

### Ground Truth
**Definition:** Actual outcome to validate model.
**Use:** Compare predicted vs actual; compute decision quality.

### Decision Quality Drift
**Definition:** Increasing prediction-vs-actual gap.
**Mitigation:** Periodic re-decision triggered when drift exceeds threshold.

### One-Time vs Repeated Decisions
**Repeated:** Cumulative learning; CDD as asset.
**One-time:** Capture artifacts for context-transfer.

### Decision Retrospective
**Purpose:** Compare predicted vs actual; update CDD; capture process improvements.
**Output:** Decision Quality Report.

### Outcome Bias
**Anti-pattern:** Conflating decision quality with outcome quality.
**Mitigation:** Decision quality = process given information at decision time.

## Cross-Reference Map

```
                        DECISION INTELLIGENCE
                                │
                    ┌───────────┴────────────────────────────┐
                    ▼                                          ▼
             FIVE PHASES (A-E)                          KEY CONCEPTS
                    │                                          │
                    │                                  - Action-to-Outcome
       ┌────────────┼─────────────────┐                - Type III Error
       ▼            ▼                  ▼                - Hybrid (HITL)
   PHASE A     PHASE B            PHASE C/D/E         - OODA Loop
   Requirements Modeling          Reasoning
                                  /Action/Review
       │            │                  │
       ▼            ▼                  ▼
   A1 Objective  B1 Design        C1 Simulation
   A2 Framing    B2 Asset Inv     C2 Assessment
                                  D1 Monitoring
                                  E1 Artifact
                                  E2 Retrospective

                                          │
                              ┌───────────┼───────────┐
                              ▼           ▼            ▼
                      CDD Components  Anti-Patterns  Visualization
                      - Levers        - Lobster Claw - Opportunity
                      - Externals     - Silos /        Envelope
                      - Intermediates   Whack-a-Mole - Cost Envelope
                      - Outcomes      - Outcome Bias
                      - Causal chains - Type III Error
```

Source: *Link* / *The Decision Intelligence Handbook* (Pratt).
