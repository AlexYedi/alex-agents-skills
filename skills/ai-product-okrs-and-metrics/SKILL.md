---
name: ai-product-okrs-and-metrics
description: >
  Set OKRs and define success metrics for AI/ML products using the AI Product
  Metric Blend (Product Health + System Health + AI Proxy + North Star + Guardrails).
  Use when defining quarterly or annual goals for an AI product team, choosing
  the right success metrics for an AI feature, debugging why an AI product looks
  successful in one metric but not in users' eyes, or when building a metric
  scorecard. Triggers: "OKRs for an AI product", "what metrics for this AI
  feature?", "AI product scorecard", "north star for our AI", "AI accuracy looks
  great but users aren't happy". Produces a structured OKR or scorecard with
  metrics from each bucket plus guardrails.
---

# AI Product OKRs & Metrics

You guide AI product teams to set goals that reflect *all* the ways an AI
product can succeed or fail. Single-metric OKRs miss orthogonal failure modes.
The AI Product Metric Blend ensures balanced measurement across user, system,
and model dimensions.

---

## When to Use This Skill

- Setting quarterly or annual OKRs for an AI/ML product team
- Choosing the right success metrics for a new AI feature
- Diagnosing why an AI product looks successful on one metric but underwhelms users
- Building a scorecard that gives leadership a complete picture of AI product health

---

## The AI Product Metric Blend

Every AI product OKR should include metrics from all three buckets, plus a single
North Star, plus 2-3 guardrails.

```
                    ┌────────────────────┐
                    │   NORTH STAR (1)   │
                    │  Core value KPI    │
                    └────────┬───────────┘
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
┌──────▼──────┐       ┌──────▼──────┐       ┌──────▼──────┐
│  PRODUCT    │       │   SYSTEM    │       │  AI PROXY   │
│   HEALTH    │       │   HEALTH    │       │             │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ DAU/MAU     │       │ Uptime      │       │ Accuracy    │
│ Engagement  │       │ Latency     │       │ Precision   │
│ Retention   │       │ Error rate  │       │ Recall      │
│ NPS         │       │ Scalability │       │ Drift       │
│ Conversion  │       │ Cost/req    │       │ Confidence  │
└─────────────┘       └─────────────┘       └─────────────┘

       └─────────────── GUARDRAILS (2-3) ──────────────┘
       Complaint rate · p99 latency · Bias detection signals
```

### How to Pick Metrics in Each Bucket

| Bucket | What to look for | Example for a Recommendation System |
|---|---|---|
| **North Star** | Single number representing core value delivered | Recommendations clicked per active user per week |
| **Product Health** | User-facing outcomes - engagement, retention, satisfaction | DAU, session length, retention curve, NPS |
| **System Health** | Technical performance - the table stakes | Uptime %, p50/p99 latency, error rate, infra cost per request |
| **AI Proxy** | Model behavior signals - leading indicators | Top-N accuracy, click-through-rate on top result, model drift score, confidence calibration |
| **Guardrails** | Adverse outcomes - hard thresholds you mustn't cross | Complaint rate < 0.1%, p99 latency < 500ms, bias delta across segments < 5% |

---

## Principles

- **No single metric captures AI product impact.** Optimizing one in isolation creates blind spots. Use a balanced blend.
- **Context beats templates.** The right metric set depends on product type, user expectations, and problem characteristics. There is no one-size-fits-all.
- **Track online + offline.** Offline metrics (validation set) are leading; online metrics (live users) are truth. Diverge at your peril.
- **Models must integrate, not be isolated.** Model performance is necessary but not sufficient. Measure end-to-end product impact, not just model metrics.
- **Guardrails get hard thresholds.** Performance metrics get pushed up; guardrails are lines you don't cross. Breach = P0.

---

## OKR Construction Template

Use this shape for any AI product OKR:

```markdown
## Objective: <user-focused goal>

### North Star Key Result
- KR1: <North Star metric> from X to Y by <date>

### Product Health Key Results
- KR2: <Product Health metric> from X to Y by <date>

### System Health Key Results
- KR3: <System Health metric> from X to Y by <date>

### AI Proxy Key Results
- KR4: <AI Proxy metric> from X to Y by <date>

### Guardrails (must not cross)
- G1: <Guardrail metric> ≤ <threshold>
- G2: <Guardrail metric> ≤ <threshold>
```

Every KR is SMART: Specific, Measurable, Achievable, Relevant, Time-bound.

---

## Anti-Patterns to Avoid

### Single Metric Reliance

**Looks like:** "Our OKR is just to hit 90% accuracy" or "DAU is our only number that matters."

**Why it fails:** Misses orthogonal failures. 99% accuracy with 5s latency = unusable. Growing DAU with falling NPS = unsustainable.

**The fix:** Balanced blend — minimum one metric per bucket.

### Ignoring Guardrails

**Looks like:** Tracking happy-path metrics without complaint rate, error rate, or latency spikes.

**Why it fails:** Bad outcomes accumulate invisibly until a public incident makes them visible all at once.

**The fix:** Define 2-3 guardrails with hard thresholds. Breaches escalate immediately.

### Neglecting System Health

**Looks like:** ML team optimizes accuracy; ignores latency, uptime, scalability.

**Why it fails:** Users abandon slow products regardless of model quality. System health is table stakes.

**The fix:** Always include at least one System Health KR in every AI OKR.

### Disconnected Models (vs Product)

**Looks like:** ML team owns model metrics; product team owns user metrics; they don't share a cadence.

**Why it fails:** Model improvements don't translate to user gains; user feedback doesn't loop back to the model.

**The fix:** Same OKR has both AI Proxy and Product Health KRs. Shared weekly review.

### Generic Templates Applied to Specific Products

**Looks like:** Using a "standard AI product OKR template" without tuning.

**Why it fails:** Wrong metrics → wrong optimizations. A diagnostic AI ≠ a recommender ≠ an agent.

**The fix:** Customize the metric blend per product. Review and revise quarterly.

---

## Worked Example: OKR for an AI-Powered Customer Support Agent

**Objective:** Reduce time-to-resolution for inbound support tickets while maintaining customer satisfaction.

**North Star KR:** % of tickets fully auto-resolved without human escalation: 25% → 50% by end of Q3.

**Product Health KR:** CSAT for AI-resolved tickets: 4.2 → 4.5 by end of Q3.

**System Health KR:** p99 response latency: 4.5s → 1.5s by end of Q3.

**AI Proxy KR:** Intent classification accuracy on production traffic: 78% → 90% by end of Q3.

**Guardrails:**
- Escalation-after-AI-attempt complaint rate: < 0.5%
- Hallucination flag rate (factual errors in agent response): < 1%
- p99 response latency: < 3s (hard ceiling, not just goal)

This blend captures: business value (auto-resolution rate), user happiness
(CSAT), technical health (latency), model quality (intent accuracy), and
risk floor (hallucinations + complaints).

---

## Gotchas

- **North Star inflation.** Teams pick a North Star that's easy to hit, not the
  one that reflects real value. Pressure-test: if this metric doubles, would
  the business meaningfully change?
- **Online-offline divergence.** Offline accuracy looks great, online users
  bounce. Cause: distribution shift, missing context features, or eval set
  bias. Trust online over offline when they disagree.
- **Guardrails treated as soft.** Teams set guardrails then ignore breaches as
  "edge cases." Either escalate breaches or remove the guardrail. No middle ground.
- **Vanity AI Proxy metrics.** "Accuracy" without specifying which subset can
  hide segment failures. Always slice AI Proxy metrics by user segment, language,
  edge case category.

Source: *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management*, Chapter 6.
