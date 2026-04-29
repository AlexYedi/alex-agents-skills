---
name: decision-simulation-and-monitoring
description: >
  Run decision simulation, sensitivity analysis, and monitoring: detect the
  Lobster Claw pattern (short-term win, long-term loss), the Silos / Whack-a-
  Mole / Measurement Effect failure modes, opportunity vs cost envelopes,
  known unknowns vs unknown unknowns, decision-quality drift, and ground
  truth measurement. Use when running a decision simulation, designing
  monitoring KPIs/intermediates as leading indicators, defining safe ranges,
  or running a Decision Retrospective. Triggers: "decision simulation",
  "sensitivity analysis", "leading indicators", "decision monitoring",
  "decision drift", "ground truth", "lobster claw effect", "silos and KPIs",
  "outcome bias", "decision retrospective". Produces a simulation +
  monitoring plan + retrospective template.
---

# Decision Simulation and Monitoring

You apply Pratt's Phase C (Reasoning), Phase D (Monitoring), and Phase E
(Review) of Decision Intelligence: simulate before acting, monitor after
acting, retrospect to learn. Avoid the Lobster Claw, Whack-a-Mole, and
outcome bias traps that defeat well-modeled decisions.

---

## When to Use This Skill

- Running a simulation on a CDD before action
- Designing what to monitor (Phase D)
- Defining safe ranges and warning thresholds
- Running a Decision Retrospective (Phase E)
- Diagnosing a decision-quality drift
- Avoiding common simulation/monitoring pitfalls

---

## Decision Simulation (Phase C1)

```
[CDD] ──animate──► [Sliders on levers] ──compute──► [Outcome envelope]
                                                       │
                                                       ▼
                                                 [Risk profile]
                                                 - Best case
                                                 - Likely
                                                 - Worst case
```

**Mechanics:** With CDD + asset annotations, build interactive simulation. User adjusts levers and externals; outcomes recalculated.

**Tools:**
- Custom (Excel, Streamlit, Jupyter, Tableau)
- Specialized DI platforms (Quantellia DEXi, similar)
- Causal inference libraries (DoWhy, EconML for academic-leaning teams)

**Outputs:**
- **Outcome envelope:** Distribution of likely outcomes given lever choices
- **Sensitivity table:** Which levers/externals most affect outcomes
- **Risk surface:** Where outcomes are vulnerable

---

## Decision Assessment (Phase C2) — Risk, Sensitivity, Uncertainty

### Sensitivity Analysis

For each lever / external, vary independently. Measure outcome change. **Most-sensitive elements deserve the most attention.**

| Element | Outcome change | Conclusion |
|---|---|---|
| Lever A | ±5% | Low-impact; precision unnecessary |
| External B | ±25% | High-impact; track closely; build mitigations |
| Lever C | ±15% | Medium; reasonable focus |

**Principle:** Concentrate accuracy where it matters. Irrelevant data needs minimal accuracy regardless of volume.

### Three Categories of Unknowns

| Type | Definition | Mitigation |
|---|---|---|
| **Known unknowns** | We know we need X but uncertain of value | Range modeling; sensitivity analysis |
| **Unknown knowns** | Known to the larger group but not top-of-mind | Brainstorming, expert elicitation |
| **Unknown unknowns** | Entirely unrecognized | Scenarios, war games, historical analogies |

**The pandemic was an unknown unknown for most supply chain decisions in 2019.** No model captured it. Mitigation is humility — outcomes can fall outside the envelope.

### Opportunity vs Cost Envelopes

```
              Outcome
                 ▲
  Opportunity    │
  envelope       │   ╭─────╮
  (heavy)        │   │     │
                 │   │  ●  │   ← Optimal point
  Cost envelope  │   │     │      with risk interval
  (lighter)      │  ╱       ╲
                 │ ╱         ╲
                 │╱           ╲
                 └─────────────►
                        Lever value
```

- **Opportunity envelope** — maximum potential profit peaks
- **Cost envelope** — maximum loss scenarios; risk intervals

The narrower the gap between them at the optimal lever, the more confident the recommendation.

---

## The Failure Modes

### Lobster Claw

```
Outcome
   ▲
   │     ╲
   │      ╲       ← Short-term gain
   │       ╲
   │        ╲___
   │            ╲
   │             ╲
   │              ╲___    ← Long-term loss
   │                  ╲
   └────────────────────►
        Time
```

**Pattern:** Action produces positive short-term effects; long-term unintended consequences dominate.

**Cause:** Missed feedback loops or dynamic behaviors in the CDD.

**Examples:** Aggressive discount campaign → spike sales → conditioning customers to wait for discounts → long-term revenue decline.

**Detection:** Simulate over relevant time horizon. Don't stop at quarter 1 if effects unfold over years.

### Silos / Whack-a-Mole / Measurement Effect

```
Department A: KPI X (local)
Department B: KPI Y (local)
Department C: KPI Z (local)
                         ↓
            Each optimizes locally → conflicts globally
                         ↓
       Whack-a-Mole: fixing A breaks B; fixing B breaks C
                         ↓
       Measurement effect: people optimize for the metric, not the goal
```

**Cause:** KPIs reflect local departmental goals, not organizational causal chains.

**Detection:** Build CDDs across departments. Simulate. Look for situations where no possible combination satisfies all local KPIs.

**Mitigation:**
- Align objectives and incentives via shared CDDs
- Assess causal chains *before* setting KPIs
- Identify critical leading indicators based on CDD sensitivity

---

## Decision Monitoring (Phase D)

Once action is taken, monitor decision elements over time.

### Track Three Things

1. **Levers (actuals)** — what we actually did
2. **Intermediates** — leading indicators
3. **Outcomes** — final results vs prediction

### Intermediates as Leading Indicators

Outcomes are lagging. Intermediates lead.

**Example:** Pricing decision impacts:
- Lever: list price changed
- Intermediate (leading): trial-to-paid conversion rate (week 1)
- Intermediate (leading): churn rate of new cohort (month 1-3)
- Outcome (lagging): annual ARR delta

Watch intermediates to detect drift early.

### Define Safe Ranges

For each monitored element:
- **Safe value range** — outcomes/intermediates within this window indicate decision is on track
- **Warning range** — outside safe; review trigger
- **Unsafe range** — re-decide

**Example:** Conversion rate predicted at 12%. Safe = 10-14%; warning = 8-10% or 14-16%; unsafe = below 8% or above 16%.

### Reduce Monitoring to Essentials

Don't monitor everything. **Monitor only elements that matter most**, based on sensitivity analysis from Phase C.

Why: Monitoring has cost. Alarm fatigue. Focus on signal.

---

## Ground Truth and Decision Quality Drift

### Ground Truth

The actual outcome / state used to validate the model.

**When available:** Compare predicted vs actual. Decision quality is computable.

**When not available:** Use proxies; acknowledge uncertainty in retrospective.

### Decision Quality Drift

Increasing discrepancy between model predictions and ground truth over time.

**Causes:**
- World changes (model trained on old data)
- Lever effects shift (saturation, cannibalization)
- New externals (pandemic, regulation, competitor move)

**Detection:** Track prediction vs actual delta. When delta exceeds threshold → re-decide.

### One-Time vs Repeated Decisions

| Type | Approach |
|---|---|
| **Repeated** (e.g., quarterly pricing) | Pattern detection across cycles; refine CDD; build cumulative learning |
| **One-time** (e.g., M&A deal) | Capture artifacts for context-transfer to similar future decisions |

For repeated decisions, the **CDD becomes a learning asset** that improves over time.

---

## Decision Review (Phase E)

### Decision Artifacts Retention (E1)

**Right after the decision is made**, capture:
- Final CDD
- Asset register
- Simulation results
- Ranges of opinion (where stakeholders disagreed)
- Rationale for the chosen lever values
- Predicted outcomes with confidence intervals

**Don't wait until "after results come in."** Memory and context erode during the rollout.

**Storage:** Separate sensitive (PII, financial) from general knowledge. Reusable templates ↔ specific decisions.

### Decision Retrospective (E2)

After outcomes are observed:
1. Compare predicted vs actual outcomes
2. Identify which assumptions held; which broke
3. Update CDD for next cycle
4. Capture process improvements
5. Document what surprised stakeholders

**Format:** Decision Quality Report. Lives in version control alongside CDD.

---

## Anti-Patterns

### Outcome Bias

**Looks like:** "The decision was good because the outcome was good." Or vice versa.

**Why it fails:** Outcomes can be lucky. Decisions can be sound but unlucky. Conflating them produces bad lessons.

**The fix:** Decision quality = quality of the process, given information available at decision time. Outcome ≠ decision quality.

### One-Iteration Simulation

**Looks like:** Simulate once at decision time. Done.

**Why it fails:** CDDs improve with iteration. First simulation reveals gaps.

**The fix:** Multiple simulation rounds. Each one updates the CDD.

### Monitoring Everything

**Looks like:** Dashboard with 50 metrics. Nobody reads it.

**Why it fails:** Alarm fatigue. Real signals lost.

**The fix:** Monitor only sensitivity-justified elements. Reduce until each metric matters.

### KPIs Without Causal Chain Analysis

**Looks like:** Each department gets its KPI. Conflicts surface only in production.

**Why it fails:** Silos / Whack-a-Mole / Measurement Effect.

**The fix:** Run CDD across departments before setting KPIs. Test for conflicts via simulation.

### Late Artifact Capture

**Looks like:** "We'll document the decision after we see results."

**Why it fails:** Context evaporates. Stakeholders move on. Memory degrades.

**The fix:** E1 happens *immediately* after decision. Outcomes go into E2 later.

### "Re-Decide" Trigger Never Pulled

**Looks like:** Outcomes drift to unsafe range. Nobody acts. Original decision still in effect.

**Why it fails:** Monitoring without action is theater.

**The fix:** Pre-commit to triggers. "If conversion drops below 8%, we revisit." Document and follow.

### Static CDDs Across Cycles

**Looks like:** Same CDD reused for 2 years. World changed. CDD didn't.

**Why it fails:** Decision quality drift. Latest CDD is wrong.

**The fix:** CDD updates after each retrospective. Living document.

---

## Decision Rules

| Situation | Action |
|---|---|
| About to take action on CDD | Simulate first; understand outcome envelope |
| High-stakes decision | Sensitivity analysis; run scenarios on key externals |
| Department conflict on KPIs | Build cross-department CDD; simulate; surface conflicts |
| Action effects expected over years | Simulate over years, not just quarter 1 |
| New action being considered | Check for Lobster Claw — run long horizon |
| Setting up monitoring | Pick intermediates as leading indicators |
| What to monitor | Sensitivity-justified elements only |
| Define safe ranges | Use simulation outcome envelope ± confidence interval |
| Outcome in warning range | Review trigger; verify causes |
| Outcome in unsafe range | Re-decide |
| Decision Retrospective | Compare predicted vs actual; update CDD |
| One-time decision | Capture for context-transfer; don't expect repeat learning |
| Repeated decision | Build cumulative learning; CDD as asset |
| New stakeholder claims "we knew this would happen" | Check artifact retention from decision time; outcome bias |
| Sensitive data in artifacts | Separate repository for PII / financial |

---

## Worked Example: Diagnosing a Lobster Claw in Marketing

**Context:** B2C company. Q1 2024: aggressive discount campaign. Sales spiked +30%. Q3 2024: full-price sales down 25%. Customers conditioned to wait for discounts.

**Diagnosis (DI lens):**

| Phase | Finding |
|---|---|
| Phase B (CDD) | Original CDD modeled discount → sales lift. Did not include feedback loop: discounts → customer expectations → reduced full-price tolerance. |
| Phase C (Simulation) | Original simulation ran 1 quarter. Lobster claw appears at 6+ months. |
| Phase D (Monitoring) | Monitored quarterly sales. Did not monitor "% sales at full price" or "customer wait-for-sale signal." |
| Phase E (Retrospective) | Now updating CDD with feedback loop. Future simulations run 12-month horizon. Will monitor full-price-sales-share as leading indicator. |

**Action items:**
1. Update CDD: add intermediate "customer expectations of discount frequency"
2. Future simulations: 12-month horizon minimum
3. New monitoring: full-price-sales-share weekly
4. Define safe range: full-price-sales-share > 70%

**Lesson:** Lobster claw is invisible in short-horizon simulation. Always check long horizon for actions that affect customer behavior or expectations.

---

## Gotchas

- **Sensitivity is not always linear.** Some levers are step-functioned; small changes do nothing until a threshold.
- **Unknown unknowns can't be eliminated.** Plan for surprise. Maintain optionality.
- **Ground truth lags.** For decisions with long outcomes (M&A, hires), full evaluation may be 1-3 years.
- **Outcome bias is universal.** Even sophisticated stakeholders fall into it. Use process metrics alongside outcomes.
- **Simulation tools matter.** Excel works for small CDDs; specialized tools for animation; Python (DoWhy, EconML) for causal inference rigor.
- **Monitoring fatigue is real.** Reduce ruthlessly. Each alarm should mean action.
- **Re-decide triggers must be pre-committed.** Otherwise inertia wins.
- **Drift detection requires baseline.** Capture artifacts at decision time; retrospective compares against this baseline.
- **Some decisions are unmeasurable.** Brand reputation, culture changes. Acknowledge limits.

---

## Further Reading

- *The Decision Intelligence Handbook* by Lorien Pratt
- *Thinking in Systems* by Donella Meadows — systems dynamics for unintended consequences
- *Superforecasting* by Tetlock — calibration and prediction discipline
- See `decision-intelligence-fundamentals` for 9-process overview
- See `causal-decision-modeling` for CDD construction

Source: *Link* / *The Decision Intelligence Handbook* (Pratt), Phases C, D, E.
