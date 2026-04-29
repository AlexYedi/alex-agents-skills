# Decision Intelligence — Additional Expert Notes

> Best practices from Lorien Pratt's *The Decision Intelligence Handbook* / *Link*.

## About the Author

**Lorien Pratt** — Co-founder of Quantellia. Coined "Decision Intelligence" in the 2010s; has been driving the discipline ever since. Background in machine learning (early 1990s neural networks contributor) — DI is her synthesis of ML, decision analysis, systems thinking, and operations research.

**Voice:** Clear, methodical, framework-oriented. Comfortable with both technical precision and business communication. Strong opinions about Type III error (the wrong-question trap).

## Foundational Mindset Shifts

1. **Start with the decision, not the data.** Type III error is the worst error.
2. **Action-to-outcome thinking.** Connect what you can do to what you want to happen.
3. **CDD is the blueprint.** Engineering discipline applied to decisions.
4. **Hybrid by default.** Humans + AI/models, not either alone.
5. **Decisions are projects.** Plan, design, execute, monitor, retrospect.
6. **Simulate over relevant horizon.** Lobster Claw appears at long horizons.
7. **Sensitivity analysis prioritizes attention.** Not all data deserves equal accuracy.
8. **Capture artifacts immediately.** Memory degrades; context erodes.

## Best Practices by Topic

### Decision Requirements (Phase A)
- Articulate the trigger / objective in 1-2 sentences
- Frame: constraints, boundaries, requirements
- Identify decision-maker (authority)
- Identify stakeholders (input, but not authority)
- Distinguish from related decisions (in scope vs out)

### Decision Modeling (Phase B)
- Build CDD with measurable elements
- Distinguish levers / externals / intermediates / outcomes religiously
- Annotate with available decision assets (data, models, expertise)
- Use divergent then convergent thinking (separated)
- Capture stakeholder disagreement as ranges
- Iterate from low-fidelity

### Decision Reasoning (Phase C)
- Simulate over relevant time horizon (avoid Lobster Claw)
- Sensitivity analysis on every lever and external
- Concentrate accuracy on high-sensitivity elements
- Surface known unknowns; brainstorm unknown knowns; humility for unknown unknowns
- Outcome envelope + cost envelope visualization
- Run cross-department simulations to detect Whack-a-Mole

### Decision Action + Monitoring (Phase D)
- Track levers (actuals), intermediates (leading), outcomes (lagging)
- Define safe / warning / unsafe ranges based on simulation envelope
- Pre-commit to re-decide triggers
- Monitor only sensitivity-justified elements (avoid alarm fatigue)
- Use intermediates as early warning system

### Decision Review (Phase E)
- E1 (Artifact Retention) immediately after decision
- E2 (Retrospective) after outcomes observable
- Compare predicted vs actual
- Update CDD for next cycle
- Document process improvements
- Separate sensitive data repositories from reusable templates

## Specific Advice

### "Make elements measurable"
**Why:** Causality requires measurement. Unmeasurable elements break simulations.
**Apply:** Every node needs a metric and unit. "Customer happiness" → "NPS (0-100)."

### "Remove directionality from outcomes"
**Why:** Direction is what the lever does to the outcome — it's a property of the decision, not the variable.
**Apply:** Outcome = "Revenue ($/quarter)"; Objective = "Maximize Revenue → $5M target."

### "Simulate over relevant horizon"
**Why:** Lobster Claw effects emerge at long horizons. Short simulations miss them.
**Apply:** For actions affecting customer behavior, simulate 12+ months minimum.

### "Decision is not the outcome"
**Why:** Outcomes can be lucky or unlucky. Decision quality is the process given information at decision time.
**Apply:** In retrospective, separate decision quality from outcome quality.

### "Tailor template processes"
**Why:** The 9 DI processes are templates. Organizations have different cultures.
**Apply:** Adapt cadence, formality, tooling. The frame remains; the form varies.

### "Capture disagreement; don't force resolution"
**Why:** Forcing premature consensus kills CDDs. Let simulation surface what matters.
**Apply:** Capture as ranges or variant CDDs.

### "Concentrate accuracy on sensitive elements"
**Why:** Volume without sensitivity is wasted effort.
**Apply:** Sensitivity analysis first. Then invest data quality in high-sensitivity elements.

## Worked Examples

### "AI investment not driving decisions" diagnostic
See `decision-intelligence-fundamentals`.

### Building a CDD for a pricing decision
See `causal-decision-modeling`.

### Diagnosing a Lobster Claw in marketing
See `decision-simulation-and-monitoring`.

## Anti-Patterns Deeper Than Skill Files

- **Skipping Phase A** — Type III error
- **Tool-First DI** — methodology before tooling
- **CDD as documentation theater** — not living
- **Pure automation decisions** — no human authority
- **Pure intuition decisions on $10M+** — no model articulation
- **One-and-done decisions** — no monitoring or retrospective
- **Forcing consensus before modeling**
- **Mixing element types** (lever vs outcome confusion)
- **Outcomes with direction** ("improve X")
- **Vague levers** ("better marketing")
- **Ignoring system boundaries**
- **Mixing divergent and convergent thinking**
- **Outcome bias** in retrospectives
- **One-iteration simulation**
- **Monitoring everything**
- **KPIs without causal chain analysis** → Whack-a-Mole
- **Late artifact capture**
- **Re-decide trigger never pulled**
- **Static CDDs across cycles**

## Process Wisdom

- Phase A workshop is 1-2 hours; Phase B is multi-session over 1-2 weeks
- CDD review before any simulation
- Cross-functional CDD construction (not just analysts)
- Specialized DI tools help but aren't required
- Living CDD in version control + animated dashboard
- Decision Quality Reports as quarterly review artifacts
- "Decision as a project" mindset — same rigor as engineering projects

## Career / Context Wisdom

- DI is an emerging discipline; consultants and tools are still maturing
- Quantellia is one canonical vendor; others (Causality.ai, etc.) growing
- Overlap with operations research, decision analysis, systems thinking — DI synthesizes
- LLM era boosting DI: causal reasoning + LLMs in CDD construction
- "Chief Decision Officer" is the emerging C-suite role
- Adjacent: Behavioral Economics, Cognitive Load, Calibration (Tetlock)

Source: *The Decision Intelligence Handbook* / *Link* by Lorien Pratt.
