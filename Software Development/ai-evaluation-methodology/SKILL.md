---
name: ai-evaluation-methodology
description: >
  Evaluate AI systems rigorously: pick the right method, design eval datasets,
  use AI-as-judge correctly, run comparative evaluations, and avoid common eval
  pitfalls. Use when setting up evals for an AI feature, debugging why your
  model evals look good but production users complain, building benchmarks for
  an internal application, or deciding when to use exact vs subjective metrics.
  Triggers: "set up evals for X", "AI as judge", "comparative evaluation",
  "model leaderboard for our app", "why do our evals look good but users hate
  it?", "slice-based evaluation", "design a benchmark". Produces structured
  evaluation plan with method selection, dataset design, and pitfall checklist.
---

# AI Evaluation Methodology

You design and run evaluation systems for AI applications. Most production
issues trace to weak evaluation — eval-driven development is to AI what
test-driven development is to software, but harder because outputs are
open-ended.

---

## When to Use This Skill

- Setting up evals for a new AI feature before building it
- Debugging "the model evals well but users complain" gap
- Building an internal benchmark for your application
- Choosing between exact metrics, AI-as-judge, and human eval
- Designing slice-based eval to catch segment-specific failures
- Setting up comparative evaluation when absolute scoring is unstable

---

## The Five Evaluation Methods

| Method | When to use | Pros | Cons |
|---|---|---|---|
| **Exact match / lexical similarity** (BLEU, ROUGE, F1) | Reference answer exists; output is constrained | Cheap, deterministic, repeatable | Fails on equivalent paraphrases |
| **Semantic similarity** (BERTScore, cosine) | Reference exists; output is flexible | Captures meaning beyond exact words | Less interpretable than exact |
| **AI as Judge** (LLM judges another LLM) | Subjective criteria (tone, helpfulness, safety) | Scales, captures nuance | Subjective; depends on judge model + prompt |
| **Comparative evaluation** (pairwise preference) | Absolute scoring is unstable across versions | Captures human preference; saturation-resistant | Slower; needs Elo/Bradley-Terry math |
| **Functional correctness** (unit tests, execution) | Code generation, structured outputs | Deterministic; closes the loop | Only works for executable outputs |

### Choose Your Method Tree

```
Is there a reference answer?
├── Yes, exact match works → Exact metrics (F1, accuracy)
└── No, or output is flexible
    ├── Output is code or executable → Functional correctness
    ├── Criterion is subjective (tone, safety, helpfulness) → AI as Judge
    └── Need to rank models stably over time → Comparative evaluation
```

---

## Eval-Driven Development

Set up eval criteria *before* building features. The order:

```
1. Define eval criteria — what does "good" mean for this feature?
2. Curate eval dataset — representative of production input
3. Establish baseline — current model's score on eval set
4. Build feature
5. Re-eval against the same criteria
6. Ship only if eval improves and no guardrails breach
```

**Key principle:** Eval criteria must be specific and concrete. "Helpful" is too
vague. "Provides at least one actionable next step in the response" is testable.

---

## AI as Judge: Use Carefully

LLM-as-judge scales evaluation of subjective criteria. But it has hard limits.

### Rules for AI-as-Judge

- **Fix the judge model and prompt.** Changing them changes the metric. If you upgrade GPT-4-turbo → GPT-4o, recalibrate.
- **Use a stronger model than your generator.** Judging is harder than generating; weaker judges miss subtle failures.
- **Validate the judge against humans first.** Run 100 examples, compare judge scores to human scores, measure agreement. <80% agreement = bad judge.
- **Use clear scoring rubrics with examples.** "Score 1-5 on factual accuracy" is too vague. Provide concrete examples for each score level.
- **Watch for judge biases.** LLM judges have systematic biases: prefer longer responses, favor their own model family, weight first-mentioned options.

### When to Use AI as Judge

- Tone, style, helpfulness (subjective qualities)
- Safety / toxicity classification
- Format adherence (does output match required structure?)
- Factual consistency vs a reference

### When NOT to Use AI as Judge

- Tracking model improvements over time (use comparative eval instead)
- High-stakes deployments without human spot-checks
- Domains where the judge lacks expertise (medical, legal — needs domain experts)

---

## Comparative Evaluation: Avoid Benchmark Saturation

Traditional benchmarks saturate as models improve (everyone hits 95% on MMLU).
Comparative evaluation captures preference and doesn't saturate.

### How It Works

1. Generate two outputs (Model A, Model B) for the same input
2. Have judge (human or LLM) pick the preferred one
3. Apply Elo, Bradley-Terry, or TrueSkill to convert pairwise wins to rankings
4. Track ranking changes across model versions

### Caveat: Transitivity Doesn't Always Hold

If A > B and B > C in pairwise preference, A > C is *not guaranteed*. Human
preferences for AI models can be intransitive. Use rankings as signal, not as
strict ordering.

---

## Slice-Based Evaluation

Aggregate metrics hide segment failures. Always slice.

### What to Slice By

| Slice | Why |
|---|---|
| User tier (free / paid / enterprise) | Usage patterns differ; quality expectations differ |
| Traffic source (organic / referral / search) | Input distribution differs |
| Topic / domain | Model strengths vary by domain |
| Error-prone topics | Concentrate eval where failures cluster |
| Language / region | Multilingual performance varies wildly |
| Demographics (when ethical) | Catch fairness/bias issues |

### Avoiding Simpson's Paradox

A model can improve overall while degrading on every slice (Simpson's paradox)
if traffic mix shifts. Always look at per-slice metrics, not just aggregate.

---

## Principles

- **Distinguish exact vs subjective metrics.** Use exact when you can; reserve subjective for what truly requires judgment.
- **Context matters: evaluate on production-like data.** Training data ≠ production data. Eval must use the latter.
- **Avoid benchmark saturation.** When everyone scores 95%, the metric stopped discriminating. Switch to comparative.
- **Beware transitivity assumptions.** Pairwise preference doesn't always chain.
- **Standardize over time.** Eval setup must be reproducible across runs. Changing the judge changes the metric.
- **Cost-benefit awareness.** Use weak models for generation; reserve strong models for judging only when necessary.
- **Multi-criteria scoring.** Single metric = single failure mode missed. Score on capability, generation, instruction-following, cost, and latency.

---

## Anti-Patterns to Avoid

### Vague Eval Criteria

**Looks like:** "We'll evaluate it for helpfulness."

**Why it fails:** Helpfulness can't be measured. Different evaluators score the same response differently.

**The fix:** Concrete, testable criteria with score-level examples. "Helpful = response addresses the user's specific question with at least one actionable next step."

### Single Aggregate Metric

**Looks like:** "Our F1 is 0.87, ship it."

**Why it fails:** F1 of 0.87 with class imbalance can mean 60% on the minority class. Production users on the minority class will complain.

**The fix:** Slice-based eval. F1 per class, per segment, per language.

### Changing Judges Without Recalibration

**Looks like:** Upgrading the judge model or prompt mid-quarter without flagging it.

**Why it fails:** All metric trends become noise. You can't tell if the model improved or the judge changed.

**The fix:** Treat the judge as part of the metric. Version it. Recalibrate when it changes.

### Skipping Human Validation of AI Judge

**Looks like:** Trusting GPT-4 as judge without checking it agrees with humans.

**Why it fails:** AI judges can be systematically wrong on your domain. You're optimizing for the wrong target.

**The fix:** 100-example human-vs-judge agreement check before relying on AI as judge.

---

## Decision Rules

| Condition | Action |
|---|---|
| Reference answer exists, output is constrained | Use exact match (F1, accuracy) |
| Reference exists but paraphrasing is OK | Semantic similarity (BERTScore) |
| Subjective criteria (tone, helpfulness) | AI as Judge with strong model |
| Tracking improvement over time | Comparative evaluation, not absolute |
| Output is code | Functional correctness via tests |
| Aggregate metric looks good but users complain | Slice-based eval to find segment failures |
| Multiple criteria matter | Score each separately; report Pareto frontier |

---

## Worked Example: Eval Setup for a Customer Support Agent

**Application:** Agent that auto-responds to tier-1 support tickets.

| Layer | Method | What it measures |
|---|---|---|
| **Functional correctness** | Exact match | Does response include the policy reference number? |
| **Factual consistency** | AI as Judge (GPT-4 with rubric) | Does response contradict the knowledge base? |
| **Tone** | AI as Judge with examples | Empathetic, not robotic, not over-apologetic? |
| **Usefulness** | Comparative eval | Vs human-written responses on the same tickets — which does the user prefer? |
| **Safety guardrails** | Exact regex match | No PII leaked, no harmful instructions, no escalation skipped |
| **Slices** | Per-tier (free/paid), per-product-line, per-language | Catch segment failures |

This stack catches different failure modes. Skipping any layer creates a blind spot.

---

## Gotchas

- **Benchmark contamination.** If your eval set leaked into training data, scores are inflated. Curate fresh.
- **Eval freshness.** Eval data ages. As your product evolves, eval set must too.
- **Judge prompt fragility.** Minor prompt changes shift judge scores 5-10%. Lock the judge prompt and version it.
- **Cost of comparative eval.** Pairwise scales O(n²). Use sampling or Elo to make it tractable.
- **Subjective metrics drift.** Two annotators differ; one annotator differs from themselves over time. Run inter-rater reliability checks.

Source: *AI Engineering: Building Applications with Foundation Models* by Chip Huyen, Chapters 3-4.
