# Frameworks: AI Engineering

**Source:** *AI Engineering: Building Applications with Foundation Models* by Chip Huyen

A catalog of every framework, pattern, and named technique introduced or
applied in this book. Use this when:
- You vaguely remember a name (e.g., "PEFT", "ReAct") and need its structure
- You're deciding between technique variants (e.g., LoRA vs QLoRA)
- You need cross-references to combine techniques

---

## Framework Index (Alphabetical)

| Framework | Domain | When to apply |
|---|---|---|
| AI as a Judge (LLM as a Judge) | Evaluation | Subjective criteria evaluation |
| AI Engineering Workflow | Process | Ordering work across an AI project |
| Adapter-Based Methods (PEFT) | Finetuning | Parameter-efficient finetuning |
| Agent Loop Patterns (ReAct, Reflexion) | Agent design | Multi-step agent reasoning |
| Beam Search | Inference | Generating multiple candidate outputs |
| Best-of-N Sampling | Inference | Quality-critical outputs |
| Chain-of-Thought (CoT) | Prompt engineering | Reasoning-heavy tasks |
| Chinchilla Scaling Law | Model selection | Compute-budget reasoning |
| Comparative Evaluation | Evaluation | Saturation-resistant ranking |
| Constrained Sampling | Prompt engineering | Structured output enforcement |
| Continuous Batching | Inference | Production serving |
| Contextual Retrieval | RAG | Improving retrieval quality |
| Contrastive Learning | Embeddings | Training embedding models |
| DPO (Direct Preference Optimization) | Alignment | Post-training without reward model |
| Decoupled Prefill/Decode | Inference | Large-scale optimization |
| Dynamic Batching | Inference | Mixed-latency workloads |
| Eval-Driven Development | Process | Standard for AI engineering |
| Few-Shot Prompting | Prompt engineering | Reducing ambiguity |
| Finetuning (full and partial) | Adaptation | Stable narrow tasks |
| Flash Attention | Inference | Memory-bandwidth optimization |
| Foundation Models (concept) | Architecture | Choosing model class |
| Functional Correctness | Evaluation | Code generation eval |
| Hybrid Search | RAG | Production retrieval default |
| KV Cache Optimization | Inference | Decode phase optimization |
| LoRA (Low-Rank Adaptation) | Finetuning | PEFT default |
| LLM as a Judge | Evaluation | (see AI as a Judge) |
| MLM (Masked Language Models) | Architecture | Classification, embedding |
| Mixture-of-Experts (MoE) | Architecture | Scaling capacity efficiently |
| Model Distillation | Inference | Smaller deployable model |
| Model Merging | Finetuning | Combining specialized models |
| Multimodal RAG | RAG | Image/video/audio retrieval |
| NIAH (Needle in a Haystack) | Evaluation | Long-context evaluation |
| ORPO | Alignment | Combined SFT + DPO |
| PEFT (Parameter-Efficient Finetuning) | Finetuning | Memory-efficient finetuning |
| PTQ (Post-Training Quantization) | Inference | Reduce inference cost |
| PagedAttention | Inference | KV cache management (vLLM) |
| Plan-and-Execute | Agent design | Costly-error tasks |
| Prompt Caching | Inference | Shared prompt prefixes |
| Prompt Decomposition | Prompt engineering | Complex tasks |
| Prompt Engineering | Adaptation | Cheap experimentation |
| QAT (Quantization-Aware Training) | Inference | Higher-quality quantization |
| QLoRA | Finetuning | Memory-constrained finetuning |
| Quantization | Inference | Memory + cost optimization |
| RAG (Retrieval-Augmented Generation) | Adaptation | Knowledge-heavy tasks |
| RLHF (Reinforcement Learning from Human Feedback) | Alignment | Standard alignment technique |
| ReAct (Reason + Act) | Agent design | Foundational agent loop |
| Reference-Based Evaluation | Evaluation | When ground truth exists |
| Reflexion | Agent design | Error-correcting agent |
| Reranking | RAG | Precision improvement |
| Roleplaying | Prompt engineering | Persona-based prompting |
| SFT (Supervised Finetuning) | Finetuning | Behavior alignment via examples |
| Self-Consistency | Prompt engineering | Variance reduction |
| Self-Supervision | Training | Label-cost reduction |
| Self-Verification | Hallucination mitigation | Reduce factual errors |
| Slice-Based Evaluation | Evaluation | Avoid Simpson's paradox |
| Speculative Decoding | Inference | Latency reduction |
| Static Batching | Inference | Predictable workloads |
| Structured Outputs Frameworks | Prompt engineering | JSON/regex enforcement |
| Task Vectors | Finetuning | Model arithmetic |
| Test Time Compute | Inference | Quality vs compute tradeoff |
| Textual Entailment | Hallucination mitigation | Factual consistency |
| Top-k / Top-p Sampling | Inference | Sampling strategies |
| Transformer Architecture | Architecture | Foundation of all LLMs |
| Tree-of-Thoughts (ToT) | Prompt engineering | Multi-path reasoning |

---

## Framework Catalog (Detailed)

### Foundation Models (Concept)

**Originator:** Industry term, popularized by Stanford CRFM 2021

**Structure:** Large-scale models capable of handling multiple data modalities
(text, image, video) and performing a wide range of general-purpose tasks
without specific task-specific training.

**Subtypes:**
- **LLMs (Autoregressive):** Predict next token; trained on text. Best for generation, completion, agentic tasks.
- **MLMs (Masked Language Models):** Predict missing tokens bidirectionally. Best for classification, extraction.
- **Multimodal:** Generate or understand text + image + audio + video.

**Decision rules:**
- Generation, dialog → LLM
- Classification, extraction at high volume → MLM (faster, cheaper)
- Multimodal tasks → multimodal foundation model

---

### Transformer Architecture

**Originator:** Vaswani et al., "Attention Is All You Need" (2017)

**Structure:** Replaces RNNs with attention mechanisms. Allows parallel input
processing. Dynamic weighting via query, key, value vectors.

**Variants:**
- **Encoder-only:** BERT, RoBERTa — for representation
- **Decoder-only:** GPT family — for generation
- **Encoder-decoder:** T5, BART — for sequence-to-sequence

**Cross-references:** Foundation of all subsequent frameworks in this book.

---

### Mixture-of-Experts (MoE)

**Originator:** Shazeer et al. (2017), popularized in modern LLMs

**Structure:** Sparse architecture; model divided into groups of parameters
(experts). Only a subset is active for each token. Balances capacity with
efficiency.

**Examples:** Mixtral 8x7B (8 experts, 7B params each, 2 active per token)

**When to apply:** When parameter scaling is desired but compute budget is tight.

---

### Chinchilla Scaling Law

**Originator:** Hoffmann et al. (2022), DeepMind

**Statement:** For compute-optimal training, the number of training tokens
should be approximately 20× the model size.

**Implication:** Equal scaling of parameters and data. Earlier models (GPT-3,
PaLM) were undertrained relative to their size.

**When to apply:** Model selection planning. Start with a fixed FLOP budget
rather than arbitrary parameter counts.

---

### Prompt Engineering

**Originator:** Emerged with GPT-3; became formal discipline ~2022

**Structure:** Adapts foundation models by providing instructions and context
without updating model weights.

**Sub-techniques:**
- **Few-Shot Prompting:** Provide 3-5 examples in the prompt
- **Chain-of-Thought (CoT):** Force step-by-step reasoning
- **Self-Consistency:** Sample N times, majority vote
- **Tree-of-Thoughts (ToT):** Explore multiple reasoning paths
- **Constrained Sampling:** Force structured output formats
- **Prompt Decomposition:** Break complex prompts into subtasks
- **Roleplaying:** Assign persona for tone/expertise alignment

**When to apply:** First adaptation choice for any new use case. Cheapest, fastest iteration.

---

### Chain-of-Thought (CoT)

**Originator:** Wei et al. (2022)

**Structure:** Force the model to reason explicitly before answering. Variants:
- **Zero-Shot CoT:** Append "Let's think step by step"
- **Few-Shot CoT:** Provide reasoning examples in prompt
- **Auto-CoT:** Generate reasoning examples programmatically

**When to apply:** Any reasoning-heavy task. Cost is low; quality gain is large.

---

### Self-Consistency

**Originator:** Wang et al. (2022)

**Structure:** Sample the same prompt N times with temperature > 0; majority-vote the final answer.

**When to apply:** Tasks with discrete answers (math, classification, code generation)
where stakes justify N× cost. Sweet spot: 3-5 samples.

---

### Tree-of-Thoughts (ToT)

**Originator:** Yao et al. (2023)

**Structure:** Explore multiple reasoning paths; evaluate them; prune low-probability branches.

**Variants:**
- **Full ToT:** Iterative model calls; tree expansion + evaluation + pruning
- **Zero-Shot ToT:** Single prompt simulating multi-expert conversation

**When to apply:** Complex multi-step problems where wrong moves are costly.
Reserve for hard problems where CoT + Self-Consistency are insufficient.

---

### Constrained Sampling / Structured Outputs

**Originator:** Industry development; libraries like Outlines, Guidance

**Structure:** Force output adherence to specific format by restricting valid
tokens at generation time.

**Methods:**
- Logit filtering (mask invalid tokens)
- Grammar constraints (BNF, regex)
- JSON mode (OpenAI/Anthropic API-level)
- Outlines / Guidance libraries

**When to apply:** Structured outputs that must validate (JSON, regex, enums).
Don't rely on prompt instructions alone for structured outputs at scale.

---

### Prompt Caching

**Originator:** Industry pattern; productized by Anthropic, OpenAI, others

**Structure:** Cache the static prefix of prompts (system prompts, persona
prompts). Subsequent requests with the same prefix get cached input pricing.

**Anthropic specifics:** 5-min TTL; 90% discount on cached input.

**When to apply:** When many requests share a system prompt prefix. Cost reduction
of 10x is typical.

---

### RAG (Retrieval-Augmented Generation)

**Originator:** Lewis et al. (2020)

**Structure:** A two-step process:
1. Retrieve relevant info from external sources at query time
2. Generate response using retrieved context

**Components:**
- Ingest: Chunk + embed
- Retrieve: Term-based, vector, or hybrid
- Rerank: Cross-encoder refinement
- Generate: LLM with context

**When to apply:** Information-heavy tasks where knowledge is dynamic or exceeds context window.

---

### Hybrid Search

**Originator:** Industry pattern; combines lexical and semantic search

**Structure:** First-pass term-based (BM25) candidate retrieval + vector embedding-based reranking.

**Why it dominates production:** Pure vector misses exact term matches; pure
term-based misses paraphrases. Hybrid gets both.

---

### Reranking

**Originator:** Information retrieval foundational; cross-encoder approach modern

**Structure:** Second stage in search pipeline; uses an LLM as a cross-encoder
to re-order shortlisted results based on relevance.

**Why it matters:** Retrieval recall@100 might be high, but the LLM only sees
top-k=5. Reranker improves precision@5 dramatically.

**Latency cost:** 100-500ms typical.

---

### Contextual Retrieval

**Originator:** Anthropic (2024)

**Structure:** Augment each chunk with relevant context (document title, summary,
or AI-generated situational context) to make it easier for the retriever to
understand and locate the correct chunks.

**Implementation:** Each chunk gets prepended with: section title + AI-generated 50-token context.

---

### NIAH (Needle in a Haystack)

**Originator:** Greg Kamradt (2023)

**Structure:** Insert a piece of information at different positions within a long
prompt; evaluate how effectively the model retrieves it.

**Finding:** Models perform better when information is near the beginning or
end rather than the middle.

**Implication:** Order matters in long context. Put critical info at start or end.

---

### Multimodal RAG

**Originator:** Extension of standard RAG

**Structure:** External data sources include non-text modalities (images, video, audio).
Augmented by multimodal embedding models like CLIP for content-based retrieval.

---

### Agent Loop Patterns

**ReAct (Reason + Act)** — Yao et al. (2022)
- Loop: Think → Act → Observe → Repeat
- Foundational pattern; the default agent loop

**Reflexion** — Shinn et al. (2023)
- ReAct + explicit Evaluator + Self-Reflection module
- Best for complex tasks where errors need correction

**Plan-and-Execute** — Industry pattern
- Generate plan upfront → Validate plan → Execute step-by-step
- Best for tasks where wrong moves are costly

---

### Finetuning Hierarchy

**SFT (Supervised Finetuning):**
- Process: Train on (prompt, response) pairs
- When: Teaching model conversational behavior beyond completion

**Preference Finetuning:**
- Techniques: RLHF, DPO, ORPO
- Process: Rank outputs; optimize for maximal reward
- When: Aligning model with human preferences

**RLHF (Reinforcement Learning from Human Feedback):**
- Process: SFT → train reward model → RL optimization
- The classical alignment technique

**DPO (Direct Preference Optimization):**
- Process: Compare log probabilities of accepted vs rejected generations against reference model
- Why: Eliminates need for separate reward model. Simpler than RLHF.

**ORPO (Odds Ratio Preference Optimization):**
- Process: Combines SFT and DPO into single training loop
- Why: Simpler training pipeline; works with QLoRA

---

### PEFT (Parameter-Efficient Finetuning)

**Originator:** Multiple papers; popularized for LLM finetuning ~2022

**Structure:** Techniques that achieve strong finetuning performance with
significantly fewer trainable parameters than full finetuning.

**Categories:**
- **Adapter-based methods:** LoRA, BitFit, IA3, LongLoRA
- **Soft prompt-based methods:** prefix-tuning, P-Tuning, prompt tuning

**When to apply:** Memory-efficient finetuning. Default choice for most teams
without massive GPU budgets.

---

### LoRA (Low-Rank Adaptation)

**Originator:** Hu et al. (2021)

**Structure:** Approximates large weight matrices with smaller low-rank matrices
(matrices A and B). Only A and B are updated during finetuning.

**Tradeoffs:**
- Higher rank = better representation, less compression
- Typical ranks: 8-64

---

### QLoRA

**Originator:** Dettmers et al. (2023)

**Structure:** Quantized LoRA — stores model weights in 4-bit NF4 format during
finetuning, dequantizes back to BF16 during computation.

**When to apply:** Memory-constrained finetuning. Enables finetuning of large
models on single consumer GPU.

---

### Model Merging

**Originator:** Industry techniques; multiple papers ~2023-2024

**Structure:** Combining multiple models (often finetuned models) into one custom model.

**Methods:**
- **Summing:** Average parameters or task vectors
- **Layer stacking (Frankenmerging):** Stack layers from different models
- **Concatenation:** Combine adapters by summing ranks
- **SLERP (Spherical Linear Interpolation):** Calculate shortest path on sphere

---

### Task Vectors

**Originator:** Ilharco et al. (2022)

**Structure:** Parameters representing task-specific adjustments derived by
subtracting a base model from a finetuned model. Allows arithmetic operations
like subtraction to remove biases.

---

### Eval-Driven Development

**Originator:** Chip Huyen (this book)

**Structure:** Define eval criteria *before* building features. The order:
1. Define eval criteria
2. Curate eval dataset (representative of production input)
3. Establish baseline
4. Build feature
5. Re-eval
6. Ship only if eval improves and no guardrails breach

**When to apply:** Standard discipline for any AI engineering project.

---

### Evaluation Methods (5-way)

| Method | When to use |
|---|---|
| **Exact match / lexical similarity** (BLEU, ROUGE, F1) | Reference exists; output constrained |
| **Semantic similarity** (BERTScore, cosine) | Reference exists; output flexible |
| **AI as Judge** | Subjective criteria (tone, helpfulness, safety) |
| **Comparative evaluation** | Tracking ranking over time, saturation-resistant |
| **Functional correctness** | Code generation, structured outputs |

---

### AI as a Judge (LLM as a Judge)

**Originator:** Industry pattern; formalized in Zheng et al. (2023)

**Structure:** Use one LLM to evaluate another LLM's outputs.

**Rules:**
- Fix the judge model and prompt
- Use a stronger model than your generator
- Validate the judge against humans first
- Use clear scoring rubrics with examples
- Watch for biases (length, model-family, position)

---

### Comparative Evaluation

**Originator:** Industry pattern; ranking via Elo / Bradley-Terry / TrueSkill

**Structure:**
1. Generate two outputs (Model A, Model B) for the same input
2. Judge picks preferred
3. Apply Elo / Bradley-Terry / TrueSkill to convert pairwise wins to rankings
4. Track ranking changes across model versions

**Caveat:** Transitivity doesn't always hold.

---

### Slice-Based Evaluation

**Originator:** Industry pattern; from production ML

**Structure:** Break evaluation datasets into subsets (by user tier, traffic
source, error-prone topics, language, demographics) to detect biases and
debug performance.

**Why it matters:** Avoids Simpson's paradox. A model can improve overall while
degrading on every slice if traffic mix shifts.

---

### Inference Optimization Techniques

**Quantization (PTQ, QAT):**
- PTQ: post-training quantization (cheap to apply)
- QAT: quantization-aware training (better quality preservation)
- Levels: INT8 default, INT4 for memory-constrained

**Batching strategies:**
- **Static Batching:** Fixed batch size; predictable workloads
- **Dynamic Batching:** Process when window expires or threshold met
- **Continuous Batching:** Returns completed requests immediately, fills slots; production default

**KV Cache Optimization:**
- **PagedAttention** (vLLM): Manages cache like virtual memory
- **Flash Attention:** Tile-based attention for memory bandwidth
- **KV cache compression:** Quantize the cache itself

**Speculative Decoding:**
- Use small "draft" model to propose tokens; verify with target in parallel
- Speedup: 2-3x typical

**Inference with Reference:**
- Copy spans directly from input rather than regenerating
- Best for editing tasks, summaries

**Parallel Decoding:**
- Lookahead, Medusa: generate multiple future tokens simultaneously

**Decoupling Prefill/Decode:**
- Run prefill on compute-optimized hardware
- Run decode on memory-bandwidth-optimized hardware

**Model Parallelism:**
- Tensor parallelism: split weight matrices across GPUs
- Pipeline parallelism: split layers across GPUs
- Expert parallelism (MoE): distribute experts

---

### Hallucination Mitigation Techniques

**Self-Verification (SelfCheckGPT):**
- Generate multiple outputs for same query
- If they disagree, original is likely hallucinated

**Knowledge-Augmented Verification (SAFE):**
- Use external search engines to verify individual facts
- Search-Augmented Factuality Evaluator

**Textual Entailment:**
- Frame factual consistency as classification: Entailment / Contradiction / Neutral

**Grounded Generation:**
- Provide LLM with retrieved relevant info alongside question
- Constrain generation to facts in source material

---

## Cross-Reference Map

```
   ┌─────────────────────────────────────────────┐
   │       AI Engineering Workflow (8 stages)    │
   └────┬────────────────────────────────────────┘
        │
        ▼
┌──────────────────┐
│ Adaptation Choice│
└──────┬───────────┘
       │
       ├── Prompt Engineering ─→ CoT, Self-Consistency, ToT, Constrained Sampling, Few-Shot
       │
       ├── RAG ─→ Chunking, Hybrid Search, Reranking, Contextual Retrieval, Multimodal RAG
       │
       └── Finetuning ─→ SFT → Preference Finetuning (RLHF / DPO / ORPO)
                              ↓
                         PEFT (LoRA, QLoRA, Adapters, Soft Prompts)

   Eval-Driven Development (parallel to all):
   ┌─────────────────────────────────────────────┐
   │ Eval Methods: Exact / Semantic / AI Judge / │
   │ Comparative / Functional Correctness        │
   │ + Slice-Based + NIAH                         │
   └─────────────────────────────────────────────┘

   Agents (compose loops + tools):
   ┌────────────┐    ┌──────────┐    ┌────────────────┐
   │ ReAct      │ ←→ │Reflexion │ ←→ │ Plan-and-Execute│
   └────────────┘    └──────────┘    └────────────────┘

   Inference Optimization (apply selectively):
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │ Quantization │  │ Batching     │  │ KV Cache     │
   │ (PTQ, QAT)   │  │(continuous)  │  │ (PagedAttn,  │
   └──────────────┘  └──────────────┘  │  Flash, etc.)│
                                       └──────────────┘
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │ Prompt Cache │  │ Speculative  │  │ Decoupled    │
   │              │  │ Decoding     │  │ Prefill/Decode│
   └──────────────┘  └──────────────┘  └──────────────┘

   Hallucination Mitigation (parallel):
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │Self-Verify  │  │ Knowledge-   │  │ Textual      │
   │(SelfCheckGPT│  │ Augmented    │  │ Entailment   │
   │             │  │ (SAFE)       │  │              │
   └──────────────┘  └──────────────┘  └──────────────┘
```

---

## How to use this catalog

- **Vaguely remember a name?** → Browse the alphabetical index
- **Picking a technique for a specific stage?** → Use the cross-reference map
- **Choosing between variants (LoRA vs QLoRA, PTQ vs QAT)?** → See detailed catalog
- **Need expert advice on application?** → See `additional-experts.md`
