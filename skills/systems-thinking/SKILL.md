---
name: systems-thinking
description: Help users think in systems and understand complex dynamics. Use when someone is dealing with multi-stakeholder problems, trying to understand second-order effects, managing platform ecosystems, analyzing complex organizational dynamics, diagnosing chronic issues, or making decisions where leverage matters.
---

# Systems Thinking

Help the user apply systems thinking to complex problems using the canonical frameworks distilled from Donella Meadows' *Thinking in Systems: A Primer* (2008), the upstream guest insights from a product-leader podcast set, and applied lessons from real diagnostic runs.

## When to use this skill

- Multi-stakeholder problems where each actor's incentives matter.
- Chronic issues where the obvious fix keeps not working.
- Decisions where leverage matters — picking *where* to push, not just *what* to push.
- Roadmap or prioritization choices that need second-order-effects analysis.
- Organizational dynamics, team velocity, content systems, GTM motions.
- Architecture and system-design decisions with long-lived consequences.
- Any "why does this keep happening?" or "we've tried everything" situation.

## How to help — the eight-phase analysis

Don't jump to interventions. Walk through the diagnosis.

1. **Bound the system** — what's in, what's out, who decided.
2. **Map stocks and flows** — what's accumulating, what's moving.
3. **Identify feedback loops** — R loops, B loops, where the delays are.
4. **Test for archetype shape** — match against the 8 named patterns; *and* explicitly state which archetypes you considered and ruled out, with evidence.
5. **Locate players and their incentives** — bounded rationality applies to all of them. For single-actor systems, treat each functional sub-role (researcher / reviewer / publisher) as a separate row.
6. **Find the highest workable leverage point** — on the 12-point hierarchy.
7. **Test second-order effects** — what breaks if we push?
8. **Check posture** — am I dancing with this system, or trying to control it?

Each phase has a working question bank in `references/diagnostic-questions.md`. When time is short, run phases 1, 2, 3, and 4 — that's usually enough to reframe the problem.

## Core principles (the foundation)

### See the system, not just the elements
Meadows: a system has elements (visible), interconnections (often informational), and a function or purpose (least obvious, most determinative). Most decisions get made at the elements layer where leverage is lowest. Watch for the rules and the goal underneath the rules.

### Stocks and flows
A stock is what accumulates. A flow is what changes it. The bathtub equation: stock(t) = stock(t-dt) + (inflow − outflow) × dt. **A stock can be raised by increasing inflows OR decreasing outflows.** Most "growth" plans focus only on inflow.

**Watch for perverse balancing loops** — outflows of decay/expiration/abandonment look identical to outflows of delivery at the stock level, but the system is failing. Always split the outflow metric.

### Feedback loops
Two kinds, only two:
- **Balancing (B):** goal-seeking, stability-restoring. The system's self-correction.
- **Reinforcing (R):** self-amplifying. Exponential growth or collapse.
Most chronic system pain is a reinforcing loop running unchecked, or a balancing loop that's been stripped of redundancy.

### Bounded rationality
Each actor in a system makes "rational" decisions inside their limited view. The decisions aggregate to outcomes nobody wanted. Don't assume malice when bounded rationality explains it. **For single-actor systems, multiple sub-roles within one person count as separate actors** for this analysis.

### Second-order effects
After the first-order impact comes the system's response, then the actors' adaptation. Pre-mortem: imagine the intervention failed spectacularly; what went wrong? The answer is usually a second-order effect.

### Find leverage points; check direction
Some places to push are 100x more effective than others. People often locate them correctly and push them in the wrong direction. The full hierarchy lives in `references/leverage-points.md`.

### Beware the eight system traps
Most chronic systemic problems are one of eight named patterns: Policy Resistance, Tragedy of the Commons, Drift to Low Performance, Escalation, Success to the Successful, Shifting the Burden, Rule Beating, Seeking the Wrong Goal. Each has a known way out. Catalog in `references/system-archetypes.md`.

**Rule-out discipline:** when matching an archetype, also state which archetypes you considered and rejected, and on what evidence. Two archetypes can produce similar surface symptoms but their escapes are different.

### Manage for resilience, self-organization, and hierarchy
Healthy systems have all three. Productivity-only optimization erodes them by default. See `references/system-properties.md`.

### Dance, don't control
Self-organizing nonlinear feedback systems are inherently unpredictable. The discipline is to dance with them: get the beat, expose mental models, honor information, design for feedback, listen for system wisdom, stay humble. See `references/dancing-with-systems.md`.

### Upstream guest principles

Six insights from product-leader interviews that are useful as concrete handles on Meadows' abstractions:

- **Seth Godin:** "What does it mean to be a strategic thinker? It means to see the system." The invisible rules, culture, and interoperability that govern how products and organizations succeed or fail.
- **Sriram:** "Think of all the players in the system, think of all of their incentives and how they interact with each other." Strong handle on Meadows' bounded rationality.
- **Will Larson:** "Stocks are things that accumulate and flows are the movement from a stock to another thing." Hands-on application to hiring pipelines and user funnels.
- **Hari Srinivasan:** Managing complex ecosystems requires understanding effects that cascade beyond immediate impact.
- **Nickey Skarstad:** "Second order thinking is you being able to think beyond the decisions that you're making today."
- **Melissa Perri + Denise Tilles:** Identify recurring manual pains and build systems around them.

Full versions in `references/guest-insights.md`.

## Reference files

| File | When to use |
|---|---|
| [meadows-thinking-in-systems.md](references/meadows-thinking-in-systems.md) | Source distillation; how Meadows defines a system; bibliography |
| [feedback-loops-stocks-flows.md](references/feedback-loops-stocks-flows.md) | Foundational vocabulary; CLD notation; perverse balancing loops; single-actor sub-roles |
| [leverage-points.md](references/leverage-points.md) | The 12 leverage points with descriptions, examples, and software/product analogs |
| [system-archetypes.md](references/system-archetypes.md) | The 8 traps with trap/escape patterns |
| [system-properties.md](references/system-properties.md) | Resilience, self-organization, hierarchy as design qualities |
| [dancing-with-systems.md](references/dancing-with-systems.md) | The 15 practitioner-conduct guidelines |
| [diagnostic-questions.md](references/diagnostic-questions.md) | Question bank organized by analysis phase |
| [applications-to-product-and-engineering.md](references/applications-to-product-and-engineering.md) | Translation to software architecture, product, GTM, AI products, content systems |
| [guest-insights.md](references/guest-insights.md) | Original 6-guest podcast insights |

## Common mistakes to flag

- **Jumping to intervention before diagnosis.** Run the eight phases first.
- **Pushing on the right leverage point in the wrong direction.** Always ask: am I sure this push moves the system the way I think it does?
- **Treating elements as the leverage point** when rules, goals, or paradigms are the actual lever.
- **Stripping out balancing loops because they "look like overhead."** Most resilience erosion is a sequence of these.
- **Mistaking stability for resilience.** A system that has never been disturbed isn't necessarily resilient; it might just be untested brittleness.
- **Optimizing parts at the expense of the whole.** Local optima are the most common cause of system-level failure.
- **Setting goals that drift with performance.** "Drift to Low Performance" is the silent killer of cultures and codebases.
- **Defining metrics that can be gamed.** Rule Beating + Seeking the Wrong Goal compound; check every KPI for "what would a malicious actor do to win this number?"
- **Politely affirming the user's prior archetype hypothesis.** Run the rule-out discipline. Two similar-looking archetypes have different escapes.
- **Treating decay-drained stocks as healthy.** A flat stock can mean equilibrium *or* loss-via-waste. Always split the outflow.

## Project-specific extensions

This skill is the canonical foundation. Project repos that depend on it (e.g., personal pipelines, specific product builds) often add project-specific layers on top:

- A *horizon framework* (e.g., MVP / Scaling / Enterprise-Prod) that ties polish decisions to system-property design choices.
- An *applications-to-<project>.md* reference file with stocks, flows, and loops sketched for that specific project.
- A *systems-analyst* sub-agent definition that performs the eight-phase analysis as a delegated task.

Look in the project's own `.claude/skills/systems-thinking/` for these extensions; they should reference (not duplicate) the canonical content here.

## Related skills

- `defining-product-vision` — vision is a paradigm-level intervention (leverage point #2)
- `prioritizing-roadmap` — roadmap items distributed across leverage points
- `risk-playbooks` — system traps as risk taxonomy
- `shipping-products` — info flows + feedback policies (`dancing-with-systems` guidelines 3, 6)
- `launch-tiering` — second-order effects per launch tier
- `head-of-product-engineering` — end-to-end orchestration uses the full systems lens
- `writing-north-star-metrics` — Goodhart's Law / Seeking the Wrong Goal trap
- `ai-product-strategy` — bounded rationality of LLMs; feedback loops in AI systems
- `conducting-user-interviews` — listening for system structure, not just symptoms
