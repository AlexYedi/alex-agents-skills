# Additional Experts: AI Engineering

**Source:** *AI Engineering: Building Applications with Foundation Models* by Chip Huyen

This reference captures the best practices, advice, and real-world examples
from the most rigorous and recent textbook on AI engineering. Use this
alongside the action-focused skills:
- `ai-engineering-foundations/SKILL.md`
- `ai-evaluation-methodology/SKILL.md`
- `rag-and-agent-architecture/SKILL.md`
- `llm-inference-optimization/SKILL.md`

---

## About the Expert

**Chip Huyen** is one of the most respected practitioners in ML/AI engineering.
Previously: ML at NVIDIA, Snorkel AI, Netflix, Stanford. Author of *Designing
Machine Learning Systems* (the canonical book on production ML systems before
the LLM era). She maintains a popular blog and discord community on AI engineering.

The book is opinionated, current (2024-2025), and grounded in production
reality. When she recommends a technique, it's because she's seen it work
at scale — and when she warns against one, she's seen it fail.

The voice throughout: precise, hedged where uncertainty exists, willing to
say "this is hard" rather than oversimplify.

---

## The AI Engineering Mindset

### Foundation models change the engineering shape, not just the technology

Pre-LLM ML engineering required teams to train models. Post-foundation-model
engineering shifts the work toward *adaptation* — picking the right model and
adapting it via prompting, RAG, or finetuning. This changes:
- **Team composition:** less ML training expertise, more application/integration expertise
- **Iteration speed:** faster than traditional ML; ship via prompt iteration
- **Evaluation rigor:** harder than traditional ML because outputs are open-ended

### Eval-driven development is the new TDD

Huyen pushes hard on this throughout the book. Just as TDD became the norm
for software, eval-driven development is becoming the norm for AI engineering.

**Practical advice:**
- Define eval criteria *before* building features
- Treat eval setup as P0 infrastructure, not a Phase 2 nice-to-have
- Eval cost grows; budget for it in initial planning
- Without evals, you can't tell if a change helps or hurts — you're flying blind

### The cost of AI engineering is concentrated in inference, not training

Most teams using foundation models don't train. Their costs are:
- Per-token API costs (if using hosted)
- GPU costs (if self-hosting)
- Eval costs (which compound with model iterations)

**Implication:** Inference optimization (prompt caching, batching, quantization)
has larger ROI than for traditional ML.

---

## Best Practices for the Adaptation Decision

### Reach for the cheapest tool first

Huyen's order of escalation:
1. **Prompt engineering** (cheapest, fastest iteration)
2. **RAG** (when knowledge is large or dynamic)
3. **Finetuning** (when narrow precision is required)

**Practical wisdom:** Most teams reach for finetuning too early. The cost is
10-100x; the iteration speed is 10-100x slower. If prompt + RAG covers your
need, don't finetune.

### When prompt engineering is enough

Often more capable than teams realize. Specifically:
- **Few-shot prompting** with 3-5 examples often matches finetuning quality on classification tasks
- **Chain-of-Thought** prompting often beats finetuning on reasoning tasks
- **Constrained sampling** (JSON mode) handles structured outputs reliably

### When RAG is the right tool

- Information changes faster than retraining cycle (news, internal docs, product catalogs)
- Knowledge volume exceeds context window
- Need source citation in responses

**Critical advice:** Retrieval quality dominates RAG output quality. A 20%
improvement in retrieval is worth more than a 20% LLM upgrade.

### When finetuning is the right tool

- Narrow stable task with high precision needs (content moderation, fraud detection)
- Domain-specific behavior that prompts can't elicit
- Cost optimization at scale (smaller fine-tuned model can replace larger generic model)

**Practical example from book:** Social media platforms fine-tune for hate
speech detection because precision needs are extreme and the task is stable.
Audio streaming services fine-tune for personalized recommendations.

---

## Best Practices for Evaluation

### Match eval method to output shape

| Output type | Best eval method |
|---|---|
| Reference answer exists | Exact match (F1, accuracy) |
| Reference exists but paraphrasing OK | Semantic similarity (BERTScore) |
| Subjective criteria (tone, helpfulness) | AI as Judge with strong model |
| Tracking improvement over time | Comparative evaluation |
| Output is code | Functional correctness via tests |

### Rules for AI as Judge

The most powerful but easily abused eval pattern. Rules from Huyen:

1. **Fix the judge model and prompt.** Changing them changes the metric.
   If you upgrade GPT-4-turbo → GPT-4o, recalibrate.

2. **Use a stronger model than your generator.** Judging is harder than generating.
   Weak judges miss subtle failures.

3. **Validate the judge against humans first.** Run 100 examples; compare
   judge scores to human scores. Below 80% agreement → bad judge.

4. **Use clear scoring rubrics with examples.** "Score 1-5 on factual accuracy"
   is too vague. Provide concrete examples for each score level.

5. **Watch for judge biases.** LLM judges have known biases:
   - Prefer longer responses
   - Favor their own model family
   - Weight first-mentioned options

### Slice-based evaluation is non-optional

Aggregate metrics hide segment failures. Always slice:
- User tier (free / paid / enterprise)
- Traffic source (organic / referral / search)
- Topic / domain
- Error-prone topics
- Language / region
- Demographics (where ethical)

**Simpson's Paradox warning:** A model can improve overall while degrading on
every slice if traffic mix shifts. Always look at per-slice metrics.

### Comparative evaluation as the saturation antidote

Traditional benchmarks saturate (everyone scores 95% on MMLU). Comparative
evaluation captures preference and doesn't saturate.

**Setup:** Generate two outputs (Model A, Model B) for the same input. Have
judge pick preferred. Apply Elo / Bradley-Terry / TrueSkill to convert pairwise
wins to rankings.

**Caveat:** Transitivity doesn't always hold. If A > B and B > C, A > C is
*not guaranteed*. Use rankings as signal, not strict ordering.

---

## Best Practices for RAG

### Chunking is domain-specific; default to 512 tokens with 10-15% overlap

But test for your data. Code chunks differently than prose. Tables chunk
differently than narrative.

### Hybrid search is the production default

**Term-based (BM25):** Catches exact term matches. Cheap and fast.
**Vector (embedding):** Captures semantic meaning. More expensive.
**Hybrid:** First-pass term-based candidate retrieval + vector reranking. Best of both.

Huyen's strong claim: production RAG should default to hybrid. Pure vector
search misses obvious term matches; pure term-based misses paraphrases.

### Reranking improves precision@5 dramatically

A reranker (cross-encoder) refines the top candidates. Slower than retrieval
but more accurate.

**When to use:** Always, in production. The latency cost (100-500ms) is
worth the precision gain.

### Augment chunks with context

Don't store raw chunks. Augment each chunk with:
- Document title or source
- Section header
- Brief AI-generated context summary

This dramatically improves retrieval quality for ambiguous chunks.

### Order matters in the final context

NIAH (Needle in a Haystack) studies show models attend better to the start and
end of context. Put critical info there.

**Implementation:**
- System prompt at the start
- User question at the end
- Retrieved context in the middle (less critical)
- Or: most-relevant retrieved chunk at the end (closest to question)

---

## Best Practices for Agents

### Match agent type to task shape

Don't reach for general-purpose LLM agents when simpler types suffice. The
cost ladder: Simple Reflex < Goal-Based < Utility-Based < General-Purpose.

| Task | Right agent type |
|---|---|
| Task-specific with clear logic | Simple Reflex |
| Multi-step planning toward objective | Goal-Based (e.g., ReAct) |
| Optimize specific metric | Utility-Based |
| Multi-domain adaptive behavior | General-Purpose |

### Tool inventory: fewer is better

The most common agent design mistake: exposing 30 tools because the underlying
API has 30 endpoints.

**Why it fails:**
- Agent has to read all tool docs every turn
- Selection becomes unreliable
- Context bloats
- Failure modes multiply

**The fix:** Aggregate to fewer parameterized tools. Five well-designed tools
beat thirty narrow ones.

### Distinguish read vs write actions categorically

```
Read actions (perception): web search, retrieve, query DB, get user data
  → low risk; expose broadly

Write actions (modification): send email, update CRM, deploy code, charge card
  → high risk; require validation, approval gates, or human-in-loop
```

**Why this matters:** A bad write action is a public incident. A bad read action
is an inefficiency. The risk profiles differ; the controls should differ.

### Plan validation before execution

For complex tasks, the loop is:
1. Decompose user task into subtasks (intent classification)
2. Generate plan (structured output with steps and dependencies)
3. **Validate plan before execution** — does it use only available tools? Are inputs reasonable? Does sequence make sense?
4. Execute validated steps one at a time
5. Reflect after each step

Skipping validation is the #1 cause of runaway agent costs.

### Cap iterations and require progress

Agents can loop indefinitely. Hard rules:
- **Iteration cap:** typically 5-10 turns. Beyond that, escalate.
- **Progress signal between iterations:** "did this step accomplish something?" If three iterations show no progress, escalate.

---

## Best Practices for Inference Optimization

### Optimize the right phase

LLM inference has two phases with different optimization profiles:

| Phase | Bottleneck | Optimization |
|---|---|---|
| Prefill | Compute-bound | Throughput |
| Decode | Memory-bandwidth-bound | Latency |

**Practical advice:** Don't optimize together. Different hardware and strategies
are optimal for each phase.

### Prompt caching is the highest-leverage optimization

If many requests share a system prompt prefix, caching gives 10x cost reduction
with no quality impact.

**Where it applies:**
- Caching the system prompt for a chatbot used by many users
- Caching the persona/skill prompt across many requests
- Caching long context that gets reused across queries

**Anthropic's prompt caching API:** 5-min TTL; 90% discount on cached input.

### Continuous batching > static batching for production

Mixed workloads benefit dramatically. Major frameworks (vLLM, TGI) implement
continuous batching by default.

**Why it matters:** Static batching wastes capacity. Continuous batching returns
completed requests immediately and fills slots with new ones.

### Quantization is cheap; validate before relying on it

INT8 PTQ usually fine. INT4 sometimes catastrophic. Always re-eval after
quantizing — quality can degrade silently.

### Self-host vs API: calculate break-even

API costs scale linearly with usage. Self-hosting has high fixed costs
(GPU rental, MLOps) but flat marginal costs.

**Break-even guidance:** Calculate at expected scale. Self-host when you cross
the break-even volume; not before.

**Hidden costs of self-hosting:**
- Monitoring infrastructure
- On-call rotation
- Security review
- Model versioning and migration
- Often 2-3x the GPU cost

---

## Worked Examples

### Example 1: Customer Support Quality Triage System

**Goal:** Classify incoming support tickets by severity to route appropriately.

| Decision | Choice | Rationale |
|---|---|---|
| Adaptation method | RAG over LLM | Severity rubric is stable but org-specific; RAG against rubric docs avoids fine-tuning |
| Model type | MLM (e.g., DeBERTa) | Classification at scale; LLM would be overkill |
| Eval setup | F1 per severity level + slice-based by product line | Single F1 hides class imbalance; slicing catches segment failures |
| Workflow | Prompt baseline → RAG → eval gating → ship → collect mistakes → finetune later if RAG ceiling hit | Cheapest path first |
| Inference budget | < 200ms p99 | Triage is upstream of human routing; can't be the bottleneck |

### Example 2: Inference Optimization Pass

**Baseline:** p99 latency 4.5s, $0.40/conversation, 50 conversations/sec capacity.

| Step | Optimization | Latency | Cost | Capacity |
|---|---|---|---|---|
| 0 | Baseline (vanilla serving, FP16) | 4.5s | $0.40 | 50/s |
| 1 | Prompt caching for system prompt | 3.2s | $0.18 | 50/s |
| 2 | Continuous batching (vLLM) | 2.5s | $0.15 | 200/s |
| 3 | INT8 quantization (validated quality) | 1.8s | $0.10 | 250/s |
| 4 | Speculative decoding with small draft model | 1.2s | $0.09 | 300/s |

**Lesson:** Each technique compounds. Biggest single wins were prompt caching
(cost) and continuous batching (capacity).

### Example 3: RAG Pipeline for Technical Documentation Search

**Goal:** Search 50,000 internal engineering docs.

| Component | Choice | Rationale |
|---|---|---|
| Architecture | Hybrid: BM25 + bi-encoder for retrieval, cross-encoder for reranking | Internal jargon needs BM25 + semantic match |
| Embedding model | Off-the-shelf SBERT, then domain-adapt via continued pretraining + contrastive fine-tuning | Generic underperforms; engineering vocabulary needs adaptation |
| Chunking | 512 tokens, 15% overlap, augmented with section title | Standard sweet spot |
| Generation | Top-3 retrieved chunks + system prompt + user query | Limit context bloat; force model to use the most relevant chunks |
| Eval | Click-through-rate on top-1 result + relevance scoring via AI judge | Real signal + scalable evaluation |

---

## Anti-Patterns (deeper than skill files)

### Finetuning before eval setup

The disaster sequence:
1. Team commits to finetuning
2. Trains model for two weeks
3. Realizes there's no eval set
4. Cobbles together eval at the end
5. Can't tell if finetune helped or hurt

**The fix:** Eval setup first. Always.

### Quantizing without re-eval

Quantization is "free" until quality degrades silently. Then it's not.

**The fix:** Every optimization step must include a re-eval gate.

### Trusting offline evaluation as truth

Offline metrics (validation set performance) diverge from online metrics
(live user behavior). Both must be tracked; offline is leading, online is truth.

**The fix:** When they disagree, trust online. Investigate the cause of divergence
(distribution shift, missing context features, eval set bias).

### Premature self-hosting

"We should self-host for control" at low volume → infra cost > API cost.

**The fix:** Calculate break-even. Stay on API until you cross it.

### Mixing read and write tools without categorization

Equal access to "search prospect" and "send email" without different validation.

**The fix:** Classify every tool. Read = expose broadly. Write = validation gate.

---

## Process Wisdom

### The AI engineering workflow (canonical order)

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

**Why this order:**
- Step 1 first because no engineering work matters if framing is wrong
- Step 2 next because adaptation choice determines all subsequent infra
- Step 3 BEFORE step 4 — without evals, you can't tell if changes help
- Step 4 before 5-7 — real signals are 10x more valuable than synthetic
- Step 6 before 7 — adapt based on data, not assumptions
- Step 8 last — premature optimization on wrong-shape system wastes effort

### Hallucination mitigation strategies

Throughout the book, Huyen returns to hallucination. Specific tactics:

1. **Self-verification:** Generate multiple outputs; if they disagree, the original is suspect (SelfCheckGPT pattern)
2. **Knowledge-augmented verification:** Use search to verify individual facts (SAFE — Search-Augmented Factuality Evaluator)
3. **Grounded generation:** RAG with explicit citations; require model to ground claims in retrieved context
4. **Textual entailment classification:** Frame factual consistency as classification (Entailment / Contradiction / Neutral)

---

## When to Apply These Practices

This expert reference complements the action-focused skills:

- For prompt vs RAG vs finetune decisions → also see `ai-engineering-foundations/SKILL.md`
- For evaluation setup → also see `ai-evaluation-methodology/SKILL.md`
- For RAG and agent architecture → also see `rag-and-agent-architecture/SKILL.md`
- For inference optimization → also see `llm-inference-optimization/SKILL.md`
- For frameworks catalog → see `frameworks.md` in this folder

When facing a novel AI engineering decision not directly covered by the skills,
browse this reference for adjacent practical wisdom.
