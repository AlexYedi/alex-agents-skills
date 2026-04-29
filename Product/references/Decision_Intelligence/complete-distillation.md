# Decision Intelligence — Complete Distillation

## 1. Source Identification
- **Title:** *The Decision Intelligence Handbook* (also draws on *Link*)
- **Author:** Lorien Pratt
- **Publisher:** O'Reilly Media
- **Pages:** ~225 OCR'd
- **Distilled in this repo:** 2026-04-29
- **Skills produced:** 3

## 2. Executive Summary

Lorien Pratt's contribution: **Decision Intelligence** as a discipline. The book's most durable insights are (1) the **Type III error** — using all the right math to answer the wrong question — and (2) the **9 DI processes across 5 phases** that prevent it. The methodology centers on **Causal Decision Diagrams (CDDs)** as engineering blueprints for decisions, with simulation, monitoring, and retrospective forming a learning loop.

## 3. The Big Takeaways

1. **Start with the decision, not the data.** Type III error is the worst error.
2. **Action-to-Outcome thinking.** Connect levers to outcomes via causal chains.
3. **CDD is the blueprint.** Engineering discipline applied to decisions.
4. **9 processes / 5 phases:** A (Requirements) → B (Modeling) → C (Reasoning) → D (Action) → E (Review).
5. **Hybrid by default.** Humans + AI/models, never either alone.
6. **Make every element measurable.**
7. **Direction lives in the objective**, not the outcome.
8. **Simulate over relevant horizon.** Lobster Claw appears at long horizons.
9. **Sensitivity analysis prioritizes attention.** Concentrate accuracy where it matters.
10. **Three categories of unknowns** — known/unknown × knowns/unknowns.
11. **Silos / Whack-a-Mole** is the failure mode of KPIs without causal analysis.
12. **Monitor intermediates as leading indicators.**
13. **Decision quality drift** demands re-decision triggers.
14. **Outcome bias** is a universal trap; separate decision quality from outcome quality.
15. **Capture artifacts immediately** after decision.

## 4. Skills Derived

| Skill | When |
|---|---|
| [`decision-intelligence-fundamentals`](../../decision-intelligence-fundamentals/SKILL.md) | The 9 processes; Type III; OODA; hybrid decisions |
| [`causal-decision-modeling`](../../causal-decision-modeling/SKILL.md) | CDD construction; measurability; system boundaries; asset register |
| [`decision-simulation-and-monitoring`](../../decision-simulation-and-monitoring/SKILL.md) | Simulation; sensitivity; monitoring; retrospective; failure modes |

## 5. Frameworks Index
See `frameworks.md`. Catalog covers: 5 Phases / 9 Processes, CDD Components, Action-to-Outcome, Type III Error, OODA Loop, Hybrid HITL, Decision Asset Register, Digital Twin, Sensitivity Analysis, Opportunity/Cost Envelopes, Known/Unknown Unknowns, Lobster Claw, Silos/Whack-a-Mole, Decision Monitoring, Ground Truth, Decision Quality Drift, One-Time vs Repeated, Decision Retrospective, Outcome Bias.

## 6. Best Practices Index
See `additional-experts.md`. Topics: per-phase practices, CDD construction discipline, simulation tactics, monitoring discipline, retrospective rigor.

## 7. Decision Rules Consolidated

| Condition | Action |
|---|---|
| High-stakes decision | Full DI 9-process treatment |
| Repeated decision | Build reusable CDD; refine over cycles |
| AI/ML investment not driving decisions | Type III diagnostic — Phase A first |
| Stakeholder conflict | Capture as ranges; simulate; let dynamics surface |
| Pure automation proposal | Reject; insist on hybrid HITL |
| New CDD | Outcome → Levers → Externals → Intermediates |
| Vague element | Refine to measurable |
| Outcome with direction ("improve X") | Move direction to objective statement |
| Workshop stalling | Probably mixed divergent/convergent; reset |
| 50+ elements | Likely over-modeled |
| Static CDD getting ignored | Animate; sliders + real-time outcome |
| About to act | Simulate first; understand envelope |
| Long-horizon effects expected | Simulate over years |
| Setting KPIs | Cross-department CDD first; check for Whack-a-Mole |
| What to monitor | Sensitivity-justified intermediates |
| Outcome in unsafe range | Re-decide |
| Retrospective | Predicted vs actual; update CDD |
| Outcome bias temptation | Decision quality ≠ outcome quality |

## 8. Anti-Patterns Consolidated

- Skipping Phase A (Type III Error)
- Tool-First DI
- CDD as documentation theater
- Pure automation decisions
- Pure intuition on $10M+ decisions
- One-and-done decisions
- Forcing consensus before modeling
- Mixing element types (lever vs outcome confusion)
- Outcomes with direction
- Vague levers
- Ignoring system boundaries
- Mixing divergent/convergent thinking
- Outcome bias
- One-iteration simulation
- Monitoring everything (alarm fatigue)
- KPIs without causal chain analysis (Silos/Whack-a-Mole)
- Late artifact capture
- Re-decide trigger never pulled
- Static CDDs across cycles
- Lobster Claw (short-horizon simulation missing long-term effects)

## 9. Worked Examples Pointer

| Example | Skill |
|---|---|
| AI investment not driving decisions diagnostic | `decision-intelligence-fundamentals` |
| CDD for a pricing decision | `causal-decision-modeling` |
| Lobster Claw in marketing | `decision-simulation-and-monitoring` |

## 10. Notable Content NOT in Skill Files

- **Specific case studies** from the book (~10 industries) — illustrative; not generalizable enough for skills.
- **Tooling-specific examples** (Quantellia DEXi, particular Excel patterns) — vendor-specific.
- **Detailed brainstorming techniques** (Six Hats, Lateral Thinking, etc.) — covered in many other facilitation books.
- **Project management adjacencies** — DI overlaps with PM but isn't synonymous.

## 11. Redundancy with Existing Repo Coverage

| Topic | Existing | Relationship |
|---|---|---|
| Product brainstorming | `product-management:brainstorm` | **Adjacent.** Brainstorming is a tool used in CDD construction. |
| Strategic planning | `product-management:roadmap-update` | **Different.** Roadmap is what; DI is how to decide. |
| Metrics review | `product-management:metrics-review` | **Adjacent.** Metrics review is monitoring; DI elaborates the design phase. |
| Forecast | `sales:forecast` | **Different.** Forecast = regression decision; DI = action-to-outcome. |
| Architecture decisions | `engineering:architecture` (ADRs) | **Adjacent methodology.** ADRs = engineering decisions; CDDs = business decisions. |

**Net assessment:** No direct overlap. DI adds a strategic decision-making framework underneath product/sales/engineering practices.

## 12. Recommended Reading Order

For a leader scoping a major decision:
1. `decision-intelligence-fundamentals` — methodology overview
2. `causal-decision-modeling` — build the CDD
3. `decision-simulation-and-monitoring` — simulate, monitor, retrospect
4. `additional-experts.md` for best practices

For a practitioner facilitating decision workshops:
1. `causal-decision-modeling` (the workshop discipline)
2. `decision-simulation-and-monitoring` (post-workshop)
3. `decision-intelligence-fundamentals` (vocabulary)

For a CTO / data leader bridging analytics to decisions:
1. `decision-intelligence-fundamentals` (Type III diagnostic)
2. Run through the AI investment example
3. `causal-decision-modeling` for the CDD construction
4. `decision-simulation-and-monitoring` for monitoring discipline

## 13. When to Invoke Which Skill

| User intent | Skill |
|---|---|
| "Decision Intelligence" / "structured decision-making" | `decision-intelligence-fundamentals` |
| "Type III error" / "answering the wrong question" | `decision-intelligence-fundamentals` |
| "OODA loop" | `decision-intelligence-fundamentals` |
| "Build a CDD" / "Causal Decision Diagram" | `causal-decision-modeling` |
| "Decision modeling workshop" | `causal-decision-modeling` |
| "Levers vs externals vs outcomes" | `causal-decision-modeling` |
| "Decision simulation" | `decision-simulation-and-monitoring` |
| "Sensitivity analysis" | `decision-simulation-and-monitoring` |
| "Lobster claw" / "unintended consequences" | `decision-simulation-and-monitoring` |
| "Silos and KPIs" | `decision-simulation-and-monitoring` |
| "Decision monitoring" / "leading indicators" | `decision-simulation-and-monitoring` |
| "Ground truth" / "decision quality drift" | `decision-simulation-and-monitoring` |
| "Decision retrospective" | `decision-simulation-and-monitoring` |
| "Outcome bias" | `decision-simulation-and-monitoring` |

Source: *The Decision Intelligence Handbook* / *Link* (Lorien Pratt), distilled 2026-04-29.
