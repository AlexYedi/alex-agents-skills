---
name: ai-engineering-foundations
description: >
  Foundational decisions for engineering AI applications on top of foundation
  models. Use when starting a new LLM-powered project and deciding between
  prompt engineering, RAG, and finetuning; when mapping business metrics to ML
  metrics; when evaluating whether to adapt a model or train from scratch; or
  when establishing the AI engineering workflow for a new product. Triggers:
  "should I prompt, RAG, or finetune?", "set up an AI engineering workflow",
  "map business metrics to ML metrics", "evaluate vs adapt vs train",
  "AI engineering best practices for a new project". Produces structured
  guidance covering the adaptation decision, evaluation gates, and workflow
  ordering.
---

# AI Engineering Foundations

You guide foundational decisions for building applications on top of foundation
models. The wrong choice early — wrong adaptation method, wrong eval setup,
wrong workflow ordering — costs months. This skill operationalizes Chip Huyen's
AI Engineering framework into actionable decisions.

---

## When to Use This Skill

- Starting a new LLM-powered application and deciding between prompt engineering, RAG, and finetuning
- Mapping business goals to ML metrics that actually predict business outcomes
- Deciding whether to adapt an existing foundation model or train from scratch
- Setting up the AI engineering workflow for a new project
- Choosing an evaluation strategy before deployment

---

## The Adaptation Decision: Prompt vs RAG vs Finetune

Three ways to make a foundation model fit your application. Choose based on
information dynamics, accuracy needs, and iteration speed.

| Method | Mechanism | Best for | Cost | Iteration speed |
|---|---|---|---|---|
| **Prompt Engineering** | Provide instructions and context without updating weights | Rapid experimentation, narrow tasks, when behavior is achievable via instruction | Low | Fast (minutes) |
| **RAG** (Retrieval-Augmented Generation) | Connect model to external knowledge base; retrieve at inference | Information-heavy tasks where knowledge changes (news, internal docs, product catalogs) | Medium | Medium (update knowledge base, not model) |
| **Finetuning** | Further train pretrained model on specific dataset; update weights | Stable narrow tasks needing high precision (content moderation, classification, code completion in a specific style) | High | Slow (full retraining) |

### Decision Flow

```
1. Can prompt engineering get you to acceptable quality?
   YES → Stop. Use prompts.
   NO  → continue
2. Is the bottleneck "the model lacks information" rather than "the model lacks behavior"?
   YES → Use RAG.
   NO  → continue
3. Is the task narrow, stable, and high-precision?
   YES → Finetune.
   NO  → Reconsider if AI is the right tool.
```

**Key insight:** Most teams reach for finetuning too early. Prompt engineering
combined with RAG covers 80%+ of production use cases. Finetune only when
prompt+RAG hits a quality ceiling that the use case demands you cross.

---

## Foundation Model Types

Match model class to task shape:

| Type | Description | Use for | Don't use for |
|---|---|---|---|
| **LLMs** (Autoregressive) | Predict next token; trained on text | Generation, completion, agentic tasks | Classification at scale (overkill, slow) |
| **MLMs** (Masked Language Models) | Predict missing tokens bidirectionally | Classification, extraction, debugging | Open-ended generation (not their strength) |
| **Multimodal** | Generate or understand text + image + audio + video | Multimodal tasks (image+text reasoning, video understanding) | Pure text tasks (cost without benefit) |
| **Foundation Models (general)** | Large-scale, general-purpose, multi-modality capable | Task variety, exploration, when scope is unclear | Narrow stable tasks (use specialized model) |

---

## Principles

- **Map business metrics to ML metrics systematically.** If user retention is the goal, your ML metric should predict retention — not just accuracy. If profit is the goal, latency and cost per inference matter as much as quality.
- **Evaluate before deployment.** Open-ended outputs make evaluation harder than closed-ended tasks. Set up evals before you start building features. Eval-driven development beats test-driven development for AI.
- **Start with product development, then invest in data + model adaptation.** Build the product interface first to validate value. Real usage signals are more valuable than offline data quality assumptions.
- **Curate data quality over quantity.** High-quality datasets beat large noisy datasets, especially when source is unstructured (Common Crawl, scraped data).
- **Optimize for latency and cost continuously.** Users have low tolerance for delays. Continuously apply inference optimization (quantization, batching, prompt caching).
- **Align with human preferences.** Use post-training (RLHF, DPO) to adjust model behavior to match safety, tone, and instruction-following expectations.

---

## The AI Engineering Workflow

Order matters. Inverting these steps creates rework.

```
1. Product framing       — what value, for whom, what success metric?
2. Adaptation choice     — prompt, RAG, or finetune?
3. Eval setup            — define eval before building features
4. MVP product surface   — build the user interface; ship fast
5. Real-world signals    — collect usage data, user feedback
6. Data curation         — based on real usage, not offline assumptions
7. Model adaptation      — fine-tune or improve RAG based on data
8. Inference optimization — latency, cost, scale
```

### Why This Order

- **Step 1 first:** No engineering work matters if the product framing is wrong.
- **Step 2 next:** The adaptation choice determines all subsequent infra. Don't build before deciding.
- **Step 3 BEFORE step 4:** If you build features without evals, you can't tell if changes help or hurt.
- **Step 4 before 5-7:** Real signals are 10x more valuable than synthetic. Ship a thin MVP to start collecting them.
- **Step 6 before 7:** Adapt based on data, not assumptions.
- **Step 8 last:** Premature optimization on a wrong-shape system wastes effort.

---

## Anti-Patterns to Avoid

### Finetuning Too Early

**Looks like:** Reaching for finetuning before exhausting prompt engineering and RAG.

**Why it fails:** Finetuning costs 10-100x more than prompt iteration. If prompt+RAG works, finetuning adds cost without value.

**The fix:** Force the question — what specifically does prompt+RAG fail on that finetuning would fix? If you can't articulate it, don't finetune yet.

### Optimizing Inference Before Validating Product

**Looks like:** Quantizing models, optimizing serving, building inference pipelines before you have users.

**Why it fails:** You optimize for the wrong shape. Real production load has different characteristics than your assumptions.

**The fix:** Ship a slow MVP first. Optimize inference only after you understand actual usage patterns.

### Treating ML Metrics as Sufficient

**Looks like:** "Our model has 90% accuracy" with no business context.

**Why it fails:** 90% accuracy on the wrong metric, or on the right metric with wrong distribution, doesn't translate to business outcomes.

**The fix:** Every ML metric must have a stated business metric it predicts. If you can't draw that line, the ML metric is wrong.

### Build-First, Eval-Later

**Looks like:** Building features then trying to figure out how to evaluate them.

**Why it fails:** You can't tell if changes help or hurt. Engineering time gets spent on the wrong problems.

**The fix:** Eval-driven development. Define eval criteria before building features. Treat eval setup as P0 infra.

---

## Decision Rules

| Condition | Action |
|---|---|
| Prompt engineering hits quality ceiling, but task is narrow + stable | Finetune |
| Information needed by model changes frequently | RAG (don't finetune on stale data) |
| Information is stable but model lacks domain knowledge | Finetune OR RAG (try RAG first - cheaper) |
| Task is broad, exploratory, pre-MVQ | Prompt engineering only |
| Multiple modalities needed | Multimodal foundation model |
| Classification or extraction at high volume | MLM (faster, cheaper than LLM) |
| Generation, completion, multi-turn dialog | LLM |
| Latency-sensitive (sub-second) | Optimize inference, not model size |

---

## Worked Example: Customer Support Quality Triage

**Goal:** Classify incoming support tickets by severity to route appropriately.

| Decision | Choice | Rationale |
|---|---|---|
| Adaptation method | RAG over LLM | Severity rubric is stable but org-specific; RAG against rubric docs avoids fine-tuning |
| Model type | MLM (e.g. DeBERTa) | Classification at scale; LLM would be overkill |
| Eval setup | F1 per severity level + slice-based eval by product line | Single F1 hides class imbalance; slicing catches segment failures |
| Workflow | Prompt baseline → RAG → eval gating → ship → collect mistakes → finetune later if RAG ceiling hit | Cheapest path first |
| Inference budget | <200ms p99 | Triage is upstream of human routing; can't be the bottleneck |

**Lesson:** Even a "simple" classification task involves all 4 architectural axes
(adaptation, model type, eval, latency). Working through them in order prevents
costly rework.

---

## Gotchas

- **Open-ended evaluation is harder than closed-ended.** Plan extra time for eval setup on generation tasks.
- **Prompt engineering improvements don't compound monotonically.** Two improvements can interact negatively. Always re-eval after combining changes.
- **RAG retrieval quality dominates final output quality.** A 20% improvement in retrieval is worth more than a 20% improvement in the LLM.
- **Self-supervision unlocks scale.** When labeled data is the bottleneck, framing the task as self-supervised (predict missing words, match image-text pairs) often beats manual labeling.

Source: *AI Engineering: Building Applications with Foundation Models* by Chip Huyen, Chapters 1-3.
