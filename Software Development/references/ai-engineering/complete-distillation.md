# Complete Distillation: AI Engineering

**Source:** *AI Engineering: Building Applications with Foundation Models* by Chip Huyen (O'Reilly)
**Distilled:** 2026-04-28
**Domain:** AI/ML Engineering, Production LLM Systems
**Pages processed:** ~340 (full book)

This is the all-encompassing single-document view of this book. Use it when
you want everything in one place rather than navigating skills + references.

---

## Executive Summary

Chip Huyen's book is the most rigorous and current textbook on AI engineering
in the foundation model era. It captures the fundamental shift from
*pre-LLM ML engineering* (where teams trained models from scratch) to
*foundation model engineering* (where teams adapt pretrained models via
prompting, RAG, or fine-tuning).

The book's central thesis: AI engineering is a distinct discipline with its
own canonical workflow, evaluation rigor, and optimization profile. The cost
center has shifted from training to inference. The bottleneck has shifted from
algorithms to evaluation. The dominant question has shifted from "what model
should we train?" to "what's the cheapest path to value?"

It is written for engineers building production AI applications — not
researchers, not pure ML scientists, not pure backend engineers. The voice is
opinionated, hedged where uncertainty exists, and grounded in production
reality.

---

## The Big Takeaways

1. **Foundation models change the engineering shape, not just the technology.** Less ML training expertise required, more application/integration expertise. Iteration speed is faster than traditional ML.

2. **Eval-driven development is the new TDD.** Define eval criteria *before* building features. Without evals, you can't tell if a change helps or hurts — flying blind.

3. **The cost is in inference, not training.** Most teams using foundation models don't train. Costs are per-token API + GPU + eval. Inference optimization (caching, batching, quantization) has higher ROI than for traditional ML.

4. **Reach for the cheapest tool first.** Order of escalation: prompt engineering → RAG → fine-tuning. Most teams reach for fine-tuning too early.

5. **Retrieval quality dominates RAG output quality.** A 20% improvement in retrieval is worth more than a 20% LLM upgrade.

6. **Slice-based evaluation is non-optional.** Aggregate metrics hide segment failures. Simpson's Paradox is real — a model can improve overall while degrading on every slice.

7. **Match agent type to task shape.** Don't reach for general-purpose LLM agents when simpler types suffice. Cost ladder: Simple Reflex < Goal-Based < Utility-Based < General-Purpose.

8. **Distinguish read vs write actions categorically.** Read = low risk; expose broadly. Write = high risk; require validation, approval gates, or human-in-loop.

9. **Prompt caching is the highest-leverage inference optimization.** 10x cost reduction with no quality impact when prompts share static prefixes. 5-min TTL on Anthropic; 90% discount on cached input.

10. **Self-host vs API: calculate break-even at expected scale.** Self-hosting hidden costs (monitoring infra, on-call, security review, model versioning) are often 2-3x the GPU cost. Stay on API until you cross break-even.

---

## Skills Derived From This Book

Located in `Software Development/`. Each is a self-contained action-focused skill.

| Skill | When to invoke | Source coverage |
|---|---|---|
| `ai-engineering-foundations` | Choosing prompt vs RAG vs fine-tune; deciding model class (LLM vs MLM vs multimodal); planning AI engineering workflow | Ch 1-2 |
| `ai-evaluation-methodology` | Setting up eval-driven development; choosing eval methods (exact match, semantic similarity, AI judge, comparative); slice-based evaluation; NIAH for long context | Ch 3-4 |
| `rag-and-agent-architecture` | RAG pipeline design (chunking, hybrid search, reranking, contextual retrieval); agent design (ReAct, Reflexion, Plan-and-Execute); tool inventory design | Ch 6-7 |
| `llm-inference-optimization` | Prompt caching, continuous batching, KV cache management, quantization, speculative decoding; self-host vs API economics | Ch 9 |

---

## Frameworks Index (See `frameworks.md` for Detail)

Quick reference. Detailed catalog in `frameworks.md`.

**Architecture:**
- Foundation Models (concept and subtypes)
- Transformer Architecture (encoder-only, decoder-only, encoder-decoder)
- Mixture-of-Experts (MoE)
- Chinchilla Scaling Law

**Adaptation:**
- Prompt Engineering (with sub-techniques)
- RAG (Retrieval-Augmented Generation)
- Fine-tuning (full and partial)
- PEFT (Parameter-Efficient Fine-Tuning)
- LoRA, QLoRA, Adapters
- Model Merging, Task Vectors

**Prompting techniques:**
- Few-Shot Prompting
- Chain-of-Thought (CoT) — Zero-Shot, Few-Shot, Auto-CoT
- Self-Consistency
- Tree-of-Thoughts (ToT)
- Constrained Sampling / Structured Outputs
- Prompt Caching
- Prompt Decomposition
- Roleplaying

**Alignment:**
- SFT (Supervised Fine-Tuning)
- RLHF (Reinforcement Learning from Human Feedback)
- DPO (Direct Preference Optimization)
- ORPO

**Retrieval:**
- Hybrid Search
- Reranking (cross-encoder)
- Contextual Retrieval
- Multimodal RAG
- Contrastive Learning

**Agents:**
- ReAct (Reason + Act)
- Reflexion
- Plan-and-Execute
- Tool inventory design
- Read vs Write action categorization

**Evaluation:**
- Eval-Driven Development
- Reference-Based Evaluation
- AI as Judge / LLM as Judge
- Comparative Evaluation
- Slice-Based Evaluation
- NIAH (Needle in a Haystack)
- Functional Correctness

**Inference Optimization:**
- Prompt Caching
- Continuous Batching, Static Batching, Dynamic Batching
- Quantization (PTQ, QAT — INT8, INT4)
- KV Cache Optimization (PagedAttention, Flash Attention)
- Speculative Decoding
- Decoupled Prefill/Decode
- Model Distillation
- Test Time Compute

**Hallucination mitigation:**
- Self-Verification (SelfCheckGPT)
- Knowledge-Augmented Verification (SAFE)
- Textual Entailment
- Grounded Generation

**Process:**
- AI Engineering Workflow (8 stages)

---

## Best Practices Index (See `additional-experts.md` for Detail)

Quick reference. Detailed expert voice in `additional-experts.md`.

**Mindset:**
- Foundation models change the engineering shape, not just the technology
- Eval-driven development is the new TDD
- Most cost is in inference, not training

**Adaptation choice:**
- Reach for the cheapest tool first (prompt → RAG → fine-tune)
- Few-shot prompting often matches fine-tuning quality on classification tasks
- CoT prompting often beats fine-tuning on reasoning tasks

**RAG:**
- Chunking is domain-specific; default 512 tokens with 10-15% overlap, but test
- Hybrid search is the production default
- Reranking improves precision@5 dramatically; latency cost worth it
- Augment chunks with context (title, summary)
- NIAH-aware ordering: critical info at start or end

**Agents:**
- Match agent type to task shape
- Tool inventory: fewer is better (5 well-designed > 30 narrow)
- Distinguish read vs write actions categorically
- Plan validation before execution
- Cap iterations and require progress signal

**Evaluation:**
- Match eval method to output shape
- AI Judge: fix the model and prompt; use stronger model than generator; validate against humans
- Slice-based eval avoids Simpson's Paradox
- Comparative evaluation as the saturation antidote

**Inference Optimization:**
- Optimize the right phase (prefill = compute-bound, decode = memory-bandwidth-bound)
- Prompt caching is the highest-leverage optimization
- Continuous batching > static batching for production
- Quantization is cheap; validate before relying on it
- Self-host vs API: calculate break-even at expected scale

---

## Decision Rules Consolidated

Every named "if X, do Y" rule across the four skills:

### From ai-engineering-foundations

| Condition | Action |
|---|---|
| Generation, dialog | Use LLM |
| Classification, extraction at high volume | Use MLM (faster, cheaper) |
| Multimodal task | Use multimodal foundation model |
| First adaptation choice | Prompt engineering |
| Knowledge changes faster than retraining cycle | Use RAG |
| Knowledge volume exceeds context window | Use RAG |
| Need source citation in responses | Use RAG |
| Narrow stable task with high precision needs | Fine-tune |
| Need a smaller deployable model for cost | Fine-tune (distillation pattern) |

### From ai-evaluation-methodology

| Condition | Action |
|---|---|
| Reference answer exists | Exact match (F1, accuracy) |
| Reference exists but paraphrasing OK | Semantic similarity (BERTScore) |
| Subjective criteria (tone, helpfulness) | AI as Judge with strong model |
| Tracking improvement over time | Comparative evaluation |
| Output is code | Functional correctness via tests |
| Long-context model evaluation | NIAH |

### From rag-and-agent-architecture

| Condition | Action |
|---|---|
| Production search system | Hybrid search (BM25 + vector) + reranker |
| Need to handle dynamic info | RAG over fine-tuning |
| Task-specific with clear logic | Simple Reflex agent |
| Multi-step planning toward objective | Goal-Based agent (ReAct) |
| Errors compound and need correction | Reflexion |
| Wrong moves are costly | Plan-and-Execute |
| Tool that modifies state | Categorize as Write; require validation |
| Tool that reads state | Categorize as Read; expose broadly |

### From llm-inference-optimization

| Condition | Action |
|---|---|
| Many requests share system prompt prefix | Prompt caching |
| Mixed-latency production workload | Continuous batching (vLLM, TGI) |
| Memory-constrained deployment | INT8 quantization with re-eval gate |
| Sub-second latency requirement | Speculative decoding with small draft model |
| Predictable batch workload | Static batching |
| Self-host vs API decision | Calculate break-even at expected scale |

---

## Anti-Patterns Consolidated

Every named anti-pattern across the four skills:

### Adaptation / Workflow Anti-Patterns

- **Finetuning before eval setup** — Train for two weeks; realize there's no eval; can't tell if it helped
- **Reaching for fine-tuning too early** — When prompt + RAG would have worked
- **Premature self-hosting** — High fixed costs at low volume; API would be cheaper

### Evaluation Anti-Patterns

- **Trusting offline evaluation as truth** — Online metrics are truth; offline is leading indicator
- **Single-metric evaluation** — Misses orthogonal failure modes
- **AI Judge biases ignored** — Length bias, model-family bias, position bias
- **Aggregate-only metrics** — Hide segment failures (Simpson's Paradox)

### RAG Anti-Patterns

- **Pure vector search without lexical** — Misses exact term matches
- **Pure lexical without semantic** — Misses paraphrases
- **No reranker in production** — Precision@5 suffers
- **Raw chunks without context augmentation** — Retrieval quality suffers

### Agent Anti-Patterns

- **30 tools because the API has 30 endpoints** — Agent overwhelmed; selection unreliable
- **No plan validation** — Runaway agent costs
- **No iteration cap** — Infinite loops
- **Mixing read and write tools without categorization** — High-risk actions get same treatment as low-risk

### Inference Optimization Anti-Patterns

- **Quantizing without re-eval** — Quality degrades silently
- **Optimizing prefill and decode together** — Different bottlenecks need different strategies

---

## Worked Examples Consolidated

### From ai-engineering-foundations
- **Customer Support Quality Triage System** — RAG over LLM (severity rubric stable but org-specific); MLM model for classification at scale; F1 per severity level + slice-based by product line; cheapest-path workflow

### From ai-evaluation-methodology
- **Comparative evaluation across model versions** — Generate two outputs per input, judge picks preferred, Elo ranking captures saturation-resistant preference
- **Slice-based eval catching Simpson's Paradox** — overall metric improving while every segment degrades

### From rag-and-agent-architecture
- **Production RAG pipeline for technical documentation** — hybrid search + cross-encoder reranking + augmented chunks
- **Plan-and-Execute agent for cost-sensitive tasks** — generate plan upfront, validate before execution, execute step-by-step with reflection

### From llm-inference-optimization
- **Inference optimization pass** — baseline 4.5s p99 → 1.2s after stacking prompt cache, continuous batching, INT8, speculative decoding. Each technique compounds.

---

## Notable Content NOT in Skill Files

These are insights from the book's content that didn't make it into action-focused
skills but are worth preserving.

### Hallucination mitigation techniques (referenced in skills, detailed only in references)

The book covers four techniques in depth:

1. **Self-Verification (SelfCheckGPT pattern):** Generate multiple outputs for same query; if they disagree, original is suspect
2. **Knowledge-Augmented Verification (SAFE — Search-Augmented Factuality Evaluator):** Use external search to verify individual facts in generated responses
3. **Textual Entailment classification:** Frame factual consistency as Entailment / Contradiction / Neutral
4. **Grounded Generation with explicit citations:** RAG with source-anchoring; require model to cite where claims come from

These compose. A production system might use Grounded Generation as primary,
Self-Verification on suspicious outputs, and SAFE for high-stakes claims.

### Modular Prompt Optimization (research methodology, not productized as skill)

The book describes a research framework where prompt-enhancement strategies
(Chain-of-Thought, Chain-of-Verification, Expert Persona, Uncertainty prompts)
are treated as composable modules tested factorially. The goal: hallucination-first
evaluation with metrics like hallucination rate, abstention rate, precision, F1.

Not productized as a standalone skill because most teams don't run hallucination
benchmarks at this rigor. But the *idea* — treat prompt enhancements as
independent modules and test them combinatorially — is valuable for any
production prompt iteration.

### Inference with Reference / Lookahead Decoding / Medusa

Beyond speculative decoding, the book mentions:
- **Inference with Reference:** Copy spans directly from input rather than regenerating (best for editing tasks, summaries)
- **Lookahead Decoding:** Generate multiple future tokens simultaneously
- **Medusa:** Parallel decoding head architecture

These are advanced optimizations rarely needed unless you're hitting hard
latency walls. Captured in `frameworks.md`.

### Model Merging and Task Vectors

Beyond fine-tuning, you can compose models:
- **Summing:** Average parameters or task vectors across multiple finetuned models
- **Layer Stacking (Frankenmerging):** Stack layers from different models
- **SLERP (Spherical Linear Interpolation):** Calculate shortest path on sphere between two model parameter spaces
- **Task Vectors:** Subtract base model from finetuned model to get "task adjustment"; arithmetic ops can remove biases or combine specialties

Useful when you have multiple specialized fine-tunes and want to combine them
without retraining. Niche but powerful.

### The "AI Engineering Workflow" canonical order

The book's recommended ordering (worth memorizing):

1. Product framing — what value, for whom, what success metric?
2. Adaptation choice — prompt, RAG, or finetune?
3. Eval setup — define eval before building features
4. MVP product surface — build user interface; ship fast
5. Real-world signals — collect usage data, user feedback
6. Data curation — based on real usage, not offline assumptions
7. Model adaptation — fine-tune or improve RAG based on data
8. Inference optimization — latency, cost, scale

Why this order matters:
- Step 1 first because no engineering work matters if framing is wrong
- Step 3 before step 4 — without evals, you can't tell if changes help
- Step 4 before 5-7 — real signals are 10x more valuable than synthetic
- Step 8 last — premature optimization on wrong-shape system wastes effort

---

## Redundant Content with Existing Repo

Items the book covers that are already well-handled by existing skills in
alex-agents-skills.

| Topic from book | Already covered by | Notes |
|---|---|---|
| General architecture decisions | `Software Development/cto-architect/` | Existing skill covers stack-aware architecture; book covers AI-specific architecture. Use `cto-architect` for general; book's skills for AI-specific. |
| TDD principles | `Software Development/iterative-engineering-practices/` (from Modern Software Engineering distillation) | Both apply TDD discipline; book applies it to AI as eval-driven development specifically. |
| Code review practices | Existing engineering skills | No direct overlap; book is AI-focused. |
| Frontend / UI work | `Software Development/frontend-dev/`, `karpathy-coder/` | No overlap; book is backend-focused. |
| Testing strategy | `engineering:testing-strategy` (system skill) | Book extends with eval-driven dev for AI; existing skill covers traditional testing. |
| Debugging | `engineering:debug` (system skill) | No direct overlap; book doesn't cover debugging. |

The book's content is complementary to — not redundant with — most of the
existing alex-agents-skills repo. The four new skills derived from it cover
AI-specific gaps that weren't addressed before.

---

## Recommended Reading Order

If you're new to this book's distilled content:

### Foundation
1. Read this `complete-distillation.md` for the overview
2. Skim `frameworks.md` (alphabetical index reveals scope)
3. Skim `additional-experts.md` for Chip Huyen's voice and best practices

### Core skills (build → eval → ship)
4. Invoke `ai-engineering-foundations` when scoping a new AI feature (adaptation choice)
5. Invoke `ai-evaluation-methodology` when setting up evals (do this BEFORE building features)
6. Invoke `rag-and-agent-architecture` when designing the runtime architecture

### Optimization (when you have a working system)
7. Invoke `llm-inference-optimization` when latency, cost, or scale becomes the bottleneck

### Deep dives (when you need them)
- `additional-experts.md` for best practices and worked examples
- `frameworks.md` for specific framework lookups
- The book's chapters for the deepest coverage of any specific topic

---

## When to Invoke Which Skill

A routing guide for choosing the right skill from this book.

| Situation | Skill |
|---|---|
| "Should we use an LLM, MLM, or multimodal model?" | `ai-engineering-foundations` |
| "Prompt vs RAG vs fine-tune for this?" | `ai-engineering-foundations` |
| "What's the AI engineering workflow for this project?" | `ai-engineering-foundations` |
| "How do we set up evals for this AI feature?" | `ai-evaluation-methodology` |
| "Which eval method for this output?" | `ai-evaluation-methodology` |
| "Should we use AI as Judge?" | `ai-evaluation-methodology` |
| "Why is the model good in offline but bad in production?" | `ai-evaluation-methodology` (slice-based eval) |
| "Design the RAG pipeline" | `rag-and-agent-architecture` |
| "Hybrid search vs pure vector?" | `rag-and-agent-architecture` |
| "Design an agent for X" | `rag-and-agent-architecture` |
| "ReAct vs Reflexion vs Plan-and-Execute?" | `rag-and-agent-architecture` |
| "How should we expose tools to the agent?" | `rag-and-agent-architecture` |
| "Latency is too high — how to optimize?" | `llm-inference-optimization` |
| "Cost is too high — how to optimize?" | `llm-inference-optimization` |
| "Should we self-host or use API?" | `llm-inference-optimization` |
| "Should we quantize?" | `llm-inference-optimization` |
| "Is prompt caching applicable here?" | `llm-inference-optimization` |

---

## Open Questions / Future Work

- **Pace of change:** AI engineering moves fast. Specific techniques (e.g.,
  best fine-tuning method) will look different in 12-18 months. Plan annual
  review.
- **Cross-book synthesis with Hands-On LLMs:** Both books cover similar
  technical ground from different angles. Huyen is rigorous and engineering-focused;
  Alammar/Grootendorst is hands-on and tooling-focused. A combined synthesis
  skill could be valuable.
- **Cross-book synthesis with Building AI-Powered Products:** The product PM
  side (Nika) and the engineering side (Huyen) are complementary lenses. Many
  AI initiatives need both perspectives applied.
- **Regulatory / governance:** Book stays mostly tactical; for AI products in
  regulated industries (healthcare, finance, legal), augment with industry-specific
  governance skills.

---

## Source

*AI Engineering: Building Applications with Foundation Models*
By Chip Huyen (O'Reilly Media)

For citations, see `frameworks.md` (each framework includes its originator).
