---
name: ai-product-development-lifecycle
description: >
  Plan, scope, and validate AI/ML products through the AI Product Development
  Lifecycle (AIPDL). Use when scoping a new AI feature or product, deciding
  between 0-to-1 vs 1-to-n product framing, prioritizing AI features with RICE,
  validating product-market fit for an AI initiative, or deciding monetization
  strategy. Triggers: "scope an AI product", "is this 0-to-1 or 1-to-n?",
  "prioritize these AI features", "should we build or buy this AI capability?",
  "what's the MVP for this AI feature?", "how do we monetize this AI feature?".
  Produces a structured product brief covering AIPDL stage, PMF assessment,
  prioritization, MVP scope, and monetization recommendation.
---

# AI Product Development Lifecycle

You are guiding the development of an AI/ML product through a specialized
lifecycle that differs from traditional software development. AI products are
not just code — they are code + data + algorithms + UX, and the lifecycle is
inherently iterative.

This skill translates Marily Nika's AIPDL framework into actionable product
decisions for AI PMs.

---

## When to Use This Skill

- Scoping a new AI/ML feature or product from concept to launch
- Deciding whether the work is 0-to-1 (novel) or 1-to-n (enhancement) and structuring the team accordingly
- Prioritizing a backlog of candidate AI features when resources are constrained
- Validating an AI product idea against the three PMF pillars before committing engineering resources
- Defining what "MVP" means for an AI feature (it's not the same as a software MVP)
- Choosing between direct and indirect monetization for a new AI feature

---

## Core Framework: AIPDL (AI Product Development Lifecycle)

Five iterative stages. Reiterate from any stage as needed. Only proceed past
Concept/Prototype after achieving Minimum Viable Quality (MVQ).

```
                    Reiterate as needed for PMF
            ┌──────────────────────────────────────┐
            │                                      │
   Ideation → Opportunity → Concept/Prototype → Testing & Analysis → Rollout
                                                           │
                              Proceed only after MVQ ──────┘
```

| Stage | Purpose | Output |
|---|---|---|
| **Ideation** | Identify AI features for a target user segment | Initial PRD draft, RICE-prioritized feature list |
| **Opportunity** | Validate the three PMF pillars | Go/no-go decision with evidence |
| **Concept/Prototype** | Build AI MVP that satisfies AI MVP requirements (below) | Functional prototype, MVQ assessment |
| **Testing & Analysis** | Gather feedback, validate ethics, measure |  Validated learnings, fairness audit |
| **Rollout** | Launch + post-deployment monitoring | Live product, monitoring stack, retraining schedule |

**Key distinction from traditional SDLC:** the data + model + evaluation loop
is part of the product, not just code. Stage transitions are gated by model
fitness (MVQ), not just feature completeness.

---

## 0-to-1 vs 1-to-n: Choose Your Mode First

Before applying any other framework, decide which mode you're in. The work
shape, team composition, and timeline expectations differ significantly.

| Dimension | 0-to-1 | 1-to-n |
|---|---|---|
| User known? | No | Yes |
| Market known? | No | Yes |
| Primary work | Hypothesis-and-test market discovery | Enhancement of known surfaces |
| Risk profile | Existential (might not have a market) | Optimization (improving on known baseline) |
| Common context | Early-stage startups, research-led teams (Adobe/Pinterest LLM PMs) | Established product orgs (Netflix recs, Amazon Prime Video) |
| Ideation focus | Untapped use cases, blank-canvas thinking | Existing pain points, feedback-driven |

**Confusion warning:** Some products feel like both. An existing app adding LLM
features has 0-to-1 model behavior on a 1-to-n user base. When in doubt, treat
the *new behavior* as 0-to-1 even if the surface is 1-to-n — the validation
work mirrors 0-to-1.

---

## Principles

- **Adopt an innovation-first mindset before solution-fitting.** AI's transformative
  potential is in problems users don't yet articulate. Don't constrain ideation
  to current-state thinking.
- **Validate willingness-to-pay through MVP behavior, not survey claims.** Stated
  WTP inflates 2-3x vs revealed WTP. A/B pricing experiments on an MVP reveal
  actual valuation.
- **Back hunches with data before pitching.** AI proposals are scrutinized harder
  than typical features due to cost. Pre-load every proposal with comparable
  implementations + ROI signals.
- **Add value from day one, even with an imperfect MVP.** AI products can't promise
  their way to adoption. Hardcode fallbacks for un-trained edge cases to keep
  the experience usable while the model matures.
- **Choose monetization based on willingness-to-pay signal, not analogy.** Direct
  vs indirect bundling shapes adoption. Bundling "because competitors bundle"
  loses signal; deliberate selection from observed behavior preserves it.

---

## Frameworks You'll Use Inside the AIPDL

### RICE Prioritization (for the Ideation stage)

Score each candidate feature on:

- **Reach**: How many users affected within a time window (e.g. 8,000/month)
- **Impact**: Effect on key metrics, scaled (3=high, 2=medium, 1=low, 0.5=minimal)
- **Confidence**: Certainty in your estimates (% backed by data, e.g. 80%)
- **Effort**: Total work in person-months (incl. data, model, integration, design)

```
RICE Score = (Reach × Impact × Confidence) / Effort
```

**Why Confidence matters more in AI:** data and algorithm feasibility are often
unknown at ideation. A high-Confidence feature is one where you've already seen
similar implementations work or have validated the data exists.

### Product-Market Fit: Three Pillars (for the Opportunity stage)

All three required. Missing any one means no PMF.

| Pillar | What to validate | How to assess |
|---|---|---|
| **Business Viability** | Sustainable revenue, capturable market, regulatory compliance | Market sizing, competitive analysis, ROI estimation, regulatory audit (GDPR/EU AI Act/HIPAA) |
| **Technical Feasibility** | Resources/data/compute available; team can build it | Technical feasibility review with engineering; data availability check; compute cost estimation |
| **User Desirability** | Solves real pain; users will pay (in money, attention, time, effort, or reputation) | Surveys + interviews + MVP A/B testing; Van Westendorp pricing model |

### AI MVP Requirements (for the Concept/Prototype stage)

An AI MVP must:

1. **Demonstrate low-effort integration** with existing systems via API or sample integration layer
2. **Showcase domain-specific expertise** via a small but high-quality dataset relevant to the target vertical
3. **Add value from day one** — operational efficiency, personalization, or actionable insights from the start (not just a promise of future improvement)
4. **Include a feedback loop** that demonstrates how the model learns and improves (e.g., capturing which recommendations users click)

**It's OK to hardcode** the un-essential paths in an AI MVP. A chatbot can have
predefined responses for common queries while the differentiating NLP capability
is still being refined. Hardcoding lets you focus on demonstrating core value
without burning time on the long tail.

### Direct vs Indirect Monetization (for the Rollout stage)

| Strategy | When to use | Example |
|---|---|---|
| **Direct** (charge separately, bundle with price increase, or sell standalone) | Customers recognize clear added value; AI features have high operational costs (compute, storage); willingness-to-pay signal is strong | OpenAI's $20/mo Plus tier |
| **Indirect** (integrate into existing packages without altering price) | Goal is adoption/retention; AI capability is still maturing; you want to refine before pricing | Spotify's AI DJ in standard Premium |

---

## Anti-Patterns to Avoid

### The Shiny AI Object Trap

**Looks like:** "We built it with GPT-4!" or "Our app now uses agentic AI!" without
articulating the user pain being solved.

**Why it fails:** Tech-first products fail PMF because no problem is being solved.
They demo well, ship, and die in the metrics.

**The fix:** Ground every AI feature in a stated user pain. Use RICE Confidence
column to force honest data on whether the pain is real.

### Hunch-Driven Pitching

**Looks like:** "We feel users will love this" in stakeholder review without
comparable implementations or ROI estimates.

**Why it fails:** AI investments cost 5-10x more than typical features. Stakeholders
need defensibility. Hunches lose to data-backed proposals every time.

**The fix:** Pre-load every proposal with: comparable past implementations,
ROI estimates, RICE scores, technical feasibility from engineering.

---

## Decision Rules

| Condition | Action | Alternative (don't do this) |
|---|---|---|
| Building an AI MVP, uncertain whether to fully train the model or hardcode | Hardcode un-essential paths; train only the differentiating capability | Full model training before MVP — too slow, blocks user feedback |
| Choosing general-purpose vs specialized AI model | If domain accuracy dominates success metric → specialized. If breadth is the differentiator → general-purpose | Defaulting to general-purpose because LLMs feel general — risks losing domain accuracy where it matters |
| Deciding direct vs indirect monetization | Strong WTP signal + high compute cost → direct. Adoption/retention goal or maturing feature → indirect | Defaulting to whatever competitors do — misses your audience's WTP signal |

---

## Worked Example: RICE on Three Netflix Features

You're an AI PM at Netflix evaluating three candidate features for binge-watchers.

| Feature | Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|---|
| Personalized binge-watching recommendations | 8,000 | 3 | 90% | 4 person-months | **5,400** |
| "Continue watching" smart notifications | 6,000 | 2 | 80% | 2 person-months | **4,800** |
| Enhanced watchlist management | 5,000 | 2 | 70% | 3 person-months | **2,333** |

**Decision:** Ship personalized recs first (highest score). Watchlist management
is the lowest priority despite reasonable Reach because Effort and lower
Confidence drag the score.

**What this teaches:** Confidence is the dominant lever in AI prioritization.
Two features with similar Reach and Impact can rank wildly differently based on
how confident you are in the underlying data and algorithm feasibility.

---

## Gotchas

- **Survey-only WTP validation lies.** Stated "I'd pay $20/mo" often becomes 50%+
  drop-off at $5/mo when tested in an MVP. Don't ship pricing decisions on survey
  data alone.
- **AI MVP timelines are not software MVP timelines.** AI MVPs need data pipelines,
  model training, and eval setup *before* the user-facing surface. A 4-week
  software MVP estimate often balloons to 12 weeks for AI. If your eng team's
  estimate includes "we still need to figure out the data," that's not an MVP
  timeline yet.
- **Confidence column gets gamed.** Teams inflate Confidence to push pet projects
  through prioritization. Force teams to *cite* what data backs each Confidence
  number — "80% because we saw similar pattern in Q3 retention experiment" beats
  "80% because we feel good about it."

---

## Further Reading

- **Marc Andreessen** (2007), *The Only Thing That Matters* — origin of the PMF
  framing this skill builds on
- **Eric Ries** (2009), *What Is an MVP?* — foundational MVP definition that
  this skill's AI MVP requirements extend
- **Eric Ries** (2011), *The Lean Startup* — broader framing of build-measure-learn
  loops that underpin AIPDL iteration

Source: *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management*, Chapter 2 (AIPDL).
