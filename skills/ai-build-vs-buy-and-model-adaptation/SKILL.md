---
name: ai-build-vs-buy-and-model-adaptation
description: >
  Make strategic AI decisions: build vs buy vs hybrid, fine-tuning vs RAG vs
  grounding, synthetic vs real-world data. Use when scoping a new AI capability
  and deciding whether to develop in-house or use a third-party model, when
  choosing how to adapt a foundation model to your domain, when planning a data
  strategy where labeled real-world data is scarce, or when evaluating whether
  AI is even the right tool for a given problem. Triggers: "should we build or
  buy this?", "fine-tune or use RAG?", "do we need fine-tuning here?", "should
  we use synthetic data?", "is AI actually the right tool here?", "is this an
  Innovator's Dilemma situation?". Produces a structured decision rationale
  covering core-competency assessment, resource check, model adaptation choice,
  and data strategy.
---

# AI Build vs Buy & Model Adaptation Strategy

You guide AI strategic decisions at the intersection of business strategy,
technical architecture, and resource reality. The wrong call here costs more
than any other AI decision — it shapes 12-24 months of work and either
preserves or surrenders the AI moat.

This skill operationalizes Clayton Christensen's Innovator's Dilemma applied
to AI plus the Build-vs-Buy Decision Matrix and Model Adaptation Methods.

---

## When to Use This Skill

- Deciding whether to build an AI capability in-house, buy off-the-shelf, or go hybrid
- Choosing the right model adaptation method (fine-tuning, RAG, or grounding) for a use case
- Planning a data strategy when labeled real-world data is scarce, sensitive, or expensive
- Evaluating whether AI is actually the right tool for a problem (vs rule-based / statistical)
- Spotting Innovator's Dilemma situations where weaker AI today might dominate tomorrow

---

## First Question: Is AI Even the Right Tool?

Before any other decision, force this gate:

| Check | If "no" | Implication |
|---|---|---|
| Is there a specific user pain that *requires* AI? | Don't build | Capability-led AI fails PMF |
| Can you get sufficient quality data (volume, diversity, cleanliness)? | Don't build | Bad data → bad model, period |
| Have you evaluated at least one non-AI alternative (rules, scripts, statistics)? | Re-evaluate | Often the simpler approach wins |
| Is your org ready for productionization (infra, monitoring, retraining cadence)? | Build deferred | Pre-production AI products fail in deploy |

If any check is "no," AI is not the right starting point. Document the
reasoning so the question doesn't keep getting re-asked.

---

## Build vs Buy: Decision Matrix

Score each factor for your specific situation. Build wins on capability+resources; Buy wins on speed+cost; Hybrid is often the right answer.

| Factor | Favors Build | Favors Buy |
|---|---|---|
| **Core competency** | AI is the differentiating value prop | AI is a supporting feature |
| **Resources/expertise** | Have ML talent + data + 2-year iteration budget | Limited ML expertise or short runway |
| **Time to market** | 6+ months acceptable | Need to ship in weeks |
| **Cost (upfront + ongoing)** | Long-horizon investment justified | Cost-constrained or uncertain ROI |
| **Risk (quality, regulatory, IP)** | Need full control over model behavior | Acceptable to delegate to vendor |
| **Data privacy** | Cannot send data to third party | Data can flow to vendor (HIPAA, GDPR signed) |
| **Competitive differentiation** | AI is your moat | Competitors can also buy the same model |

### When to Default to Hybrid

If your factors split — e.g. core competency = build but resources = buy — pick
hybrid:

- Build the *differentiating* capability in-house
- Use third-party APIs (OpenAI, Anthropic, etc.) for *supporting* capabilities

**Example:** A health-tech startup builds proprietary diagnostic models in-house
(core moat, regulated data) but uses OpenAI for patient-facing chat support
(non-differentiating, no PHI in chat).

---

## Model Adaptation Methods: Fine-tune vs RAG vs Grounding

Choose based on accuracy needs vs iteration speed.

| Method | Best for | Cost | Iteration speed |
|---|---|---|---|
| **Fine-tuning** | Stable, narrow tasks needing high precision (content moderation, fraud detection, medical diagnostics) | High (compute + labeled data) | Slow — full retraining cycle |
| **RAG (Retrieval-Augmented Generation)** | Dynamic info that changes frequently (news, market trends, internal docs, product catalogs) | Medium (vector DB + retrieval infra) | Medium — update knowledge base, not model |
| **Grounding (prompt engineering)** | Rapid experimentation during pre-MVQ exploration; lightweight customization | Low (just prompts) | Fast — minutes to test changes |

### Decision Flow

```
Does information in your domain change frequently?
├── Yes → RAG
└── No  → Is the task stable and narrow with high precision needed?
         ├── Yes → Fine-tune
         └── No  → Are you still in pre-MVQ exploration?
                  ├── Yes → Grounding (then graduate to Fine-tune or RAG later)
                  └── No  → Reconsider: should the task be narrowed?
```

---

## Data Strategy: Synthetic vs Real-World

| Use case | Strategy |
|---|---|
| Sensitive data (PHI, PII, financial) | Synthetic for development, real for production validation |
| Rare scenarios / edge cases | Synthetic to fill the long tail |
| Stakes-sensitive decisions (medical, autonomous driving) | Both — real for fidelity, synthetic for edge case coverage |
| Behavior nuance critical (recommendations, NLP) | Real-world primary; synthetic only as supplement |

### Tesla's Hybrid Approach (Worked Example)

- **Real-world driving data** captures common scenarios from user fleets
- **Synthetic scenarios** simulate rare conditions: unusual weather, animal crossings, atypical traffic
- **Validation gate:** synthetic data's statistical properties must match real distribution; no accidental bias patterns
- Result: model trained on combined dataset, validated against real-world hold-outs

**Lesson:** Synthetic *supplements* real; it doesn't *replace* it. Validate
synthetic data against minority-segment slices to catch hidden bias.

---

## Anti-Patterns to Avoid

### Adding AI Without a Clear Problem

**Looks like:** Team or board pushing for "an AI strategy" without a specific user pain.

**Why it fails:** Capability-led AI adds cost and complexity without proportional value.
Often demos well but dies in production metrics.

**The fix:** Force the question — what specific user pain, with what evidence,
requires AI specifically? If no answer, don't build.

### Default to Buy Without Considering Core Competency

**Looks like:** Always picking off-the-shelf AI to ship faster, even when AI is your core differentiator.

**Why it fails:** Surrenders the moat. If competitors can buy the same model, differentiation collapses.

**The fix:** If the AI capability *is* the core value prop, build in-house even if
slower. Buy only for non-differentiating capabilities.

### Default to Build Without Honest Resource Check

**Looks like:** Committing to in-house AI without ML talent, data infrastructure, or 2-year iteration budget.

**Why it fails:** Build projects stall, model never reaches MVQ, gets replaced by off-the-shelf anyway.

**The fix:** Pre-mortem on talent, data, infra, and 2-year iteration budget *before* committing.

---

## Innovator's Dilemma Applied to AI

Christensen's framework predicts when incumbents miss disruptive shifts. Applied to AI:

- **Sustaining innovation:** Improving existing products with AI for current customers (Netflix recs, Gmail Smart Compose). Incumbents do this well.
- **Disruptive innovation:** New AI capability that initially looks *worse* than existing solutions but redefines the market (early ChatGPT vs traditional search).

**The trap:** Today's weak AI model can become tomorrow's dominant standard.
Incumbents kill disruptive AI projects because they underperform on current
metrics — and lose the long game.

**Detection signal:** Internal critiques like "the AI is less accurate than our
current approach" or "users don't ask for this" — these are *exactly* the
patterns Christensen described in pre-disruption blind spots.

**Caveat:** Not every weak model is disruptive. Distinguish *promising-but-immature*
(real users find narrow value, capability improves rapidly) from *fundamentally-flawed*
(no users, no improvement curve).

---

## Decision Rules

| Condition | Action |
|---|---|
| Information changes frequently in your domain | Use RAG |
| Stable narrow task, high precision required | Fine-tune |
| Pre-MVQ exploration, need fast iteration | Use grounding (prompt engineering) |
| AI is core value prop AND you have resources | Build in-house |
| AI is supporting feature OR resources constrained | Buy / use API |
| Core build but adjacent capabilities buy | Hybrid approach |
| Sensitive data + edge case coverage needed | Synthetic + real combined |

---

## Gotchas

- **Acquisition tech-debt blindspot.** Acquiring an AI startup for the model often
  surfaces incompatible architecture post-close. Tech DD must include "how does
  this fit our stack" — not just "is the model good."
- **Synthetic data hidden bias.** Synthetic data passes aggregate validation but
  fails on minority slices. Always validate on segment cuts, not just headline metrics.
- **Buy decisions that look cheap aren't always.** Per-token API costs scale
  unpredictably. Estimate cost at 10x current usage before committing.
- **Build decisions that look expensive aren't always.** Off-the-shelf model
  vendors raise prices and change terms. Build cost is bounded; buy cost has tail risk.

---

## Further Reading

- **Clayton Christensen** (1997), *The Innovator's Dilemma* — the seminal disruption framework this skill applies to AI

Source: *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management*, Chapter 5.
