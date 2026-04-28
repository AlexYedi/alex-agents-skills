# Additional Experts: Hands-On Large Language Models

**Source:** *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst

This reference captures the best practices, advice, and worked examples from
two practitioners deep in the LLM tooling ecosystem. Use this alongside:
- `advanced-prompting-techniques/SKILL.md`
- `embedding-models-and-domain-adaptation/SKILL.md`
- `llm-conversation-memory-and-multimodal/SKILL.md`

---

## About the Experts

**Jay Alammar** is widely known for "The Illustrated Transformer" — the
canonical visual explanation of how transformers work. His teaching philosophy:
build mental models through visualizations, then ground them in working code.

**Maarten Grootendorst** is the creator of BERTopic and several open-source
NLP libraries. Practitioner first, theorist second. His instinct: get something
working, then optimize and understand.

The book's voice combines visual intuition with hands-on code. When they
recommend something, you'll typically see a diagram, an explanation of why
it works, and runnable code. They're skeptical of hype and grounded in
production tooling.

---

## Foundational Mental Models

### Embeddings as the unifying abstraction

Throughout the book, embeddings are treated as the core abstraction underlying
nearly all LLM applications:
- **Token embeddings:** the foundation of how models process text
- **Sentence embeddings:** how we measure similarity between sentences
- **Document embeddings:** how RAG retrieves relevant content
- **Image embeddings (CLIP):** how multimodal applications connect modalities

**Mental model:** "If two things should be considered similar, they should be
near each other in some embedding space." Many design decisions come down to
choosing the right embedding space and similarity measure.

### The pretrain-then-finetune two-step

A central pattern in modern NLP. Pretrain on massive unsupervised data
(billions of tokens) → finetune on a specific task with much smaller labeled data.

**Implication:** Most teams should not train from scratch. The cost-benefit
heavily favors picking a pretrained model and adapting it.

### Self-attention as the architectural pivot

The conceptual shift from RNNs (sequential processing) to Transformers
(parallel processing via attention) is what unlocked modern LLM scale.

**Best practice:** Understand self-attention well enough to know when models
will struggle (long context recency biases, attention dilution at scale, etc.).

---

## Best Practices for Prompt Engineering

### The Modular Prompt Framework

Treat every prompt as composed of these components. Tune each independently.

| Component | What it does |
|---|---|
| Persona | Role the model should adopt |
| Instruction | The specific task |
| Context | Background needed for the task |
| Format | Structure of the output |
| Audience | Who reads the output |
| Tone | Voice characteristics |
| Data | Inputs the task operates on |
| Examples (few-shot) | Concrete demonstrations |

**Practical wisdom:** When a prompt fails, fix the broken component without
rewriting the whole thing. Reuse strong components across prompts.

### Few-Shot Prompting Best Practices

- **Use 3-5 examples** unless task is complex (then more)
- **Examples should reflect the distribution** of expected inputs
- **Consistency matters:** all examples should have the same format
- **Order matters:** put most representative example last (recency bias)
- **Diversity within examples:** cover edge cases, not just happy paths

### Constrained Sampling for Reliable Output

When you need structured output reliably:
- **Don't trust prompt instructions alone** — models occasionally violate format
- **Use JSON mode** (OpenAI/Anthropic API) when available
- **Use grammar-based libraries** (Outlines, Guidance) for complex constraints
- **Always validate** at the consuming layer; treat constrained sampling as a hint, not a guarantee

---

## Best Practices for Embeddings and Retrieval

### Choosing an Embedding Model

The book emphasizes that embedding model choice is consequential and use-case-specific:
- **For general semantic search:** `all-mpnet-base-v2` is a strong default (sentence-transformers)
- **For multilingual:** `paraphrase-multilingual-mpnet-base-v2`
- **For longer context:** `bge-large-en` or similar
- **For cost-sensitive at scale:** smaller models like `MiniLM` variants

**Practical advice:** Start with the off-the-shelf default; switch to
domain-adapted only if generic underperforms.

### The Bi-Encoder vs Cross-Encoder Tradeoff

| Architecture | Speed | Accuracy | Use case |
|---|---|---|---|
| Bi-encoder (SBERT) | Fast — embeddings precomputed | Good | Large-scale search/retrieval |
| Cross-encoder | Slow — must run on every pair | Best | Reranking top-K candidates |

**Production pattern (the book's strong recommendation):** Hybrid approach.
Use bi-encoder to retrieve top-50, then cross-encoder to rerank to top-5.

### Hard Negatives Matter More Than Architecture

A persistent theme: spending time on hard negative mining beats picking a
fancier model architecture.

**Why:** Easy negatives produce mediocre models. Hard negatives produce strong
models. The model learns "what's similar AND what's similar-looking but different."

**Hard negative mining strategies:**
- BM25 top-K (textually similar but wrong answer)
- Same topic, different intent
- Adversarial generation via LLM
- Existing retrieval system's top wrong results

### Domain Adaptation Two-Step

When generic embeddings underperform on your domain:

1. **Continued pretraining (MLM):** Take a pretrained BERT; continue training
   on YOUR domain text with masked language modeling. Updates subword
   representations to your vocabulary.
2. **Fine-tuning with contrastive objective:** Use the result as starting point;
   train on (positive, negative) pairs from your domain.

**Lighter alternatives** when labeled pairs aren't available:
- **TSDAE** (Transformer-based Sequential Denoising Auto-Encoder): Random word removal + reconstruction
- **SimCSE:** Similar idea, different augmentation
- **Synthetic pair generation via LLM:** Use an LLM to generate positive/negative pairs from your corpus

---

## Best Practices for Topic Modeling and Clustering

### BERTopic as a Modular Framework

The authors created BERTopic. Their philosophy:
- **Modular design:** Each step (embedding, dimensionality reduction, clustering, representation) is swappable
- **Stack representation models:** Apply multiple representation methods (KeyBERTInspired → MMR → TextGeneration) for richer topic descriptions
- **Class-based TF-IDF:** Calculate frequencies at the cluster level rather than the document level

### Pipeline Best Practices

```
Documents → Embed → Reduce Dimensionality (UMAP) → Cluster (HDBSCAN) → Topic Representation
```

**Why each step matters:**
- **Embed:** captures semantic meaning
- **UMAP:** preserves global structure when reducing high-dim to low-dim
- **HDBSCAN:** density-based; auto-detects number of clusters; identifies outliers
- **Topic representation:** gives clusters human-readable names

### Avoiding Common Topic Modeling Pitfalls

- **Don't use centroid-based clustering** (k-means) without a strong prior on cluster count
- **Stop words matter:** c-TF-IDF penalizes words common across clusters; preserves cluster-distinguishing terms
- **Iterative refinement:** Run topic modeling multiple times with different settings; converge on what's interpretable

---

## Best Practices for Conversation Memory

### Match Memory Pattern to Conversation Length

| Pattern | Best for | Failure mode |
|---|---|---|
| ConversationBufferMemory | Short conversations (<10 turns) | Token limit exceeded |
| ConversationBufferWindowMemory | Bounded conversations | Loses old context |
| ConversationSummaryMemory | Long conversations | Specific details lost |

**Production reality:** Pure patterns rarely fit. Use hybrid:
- Window for recent verbatim context
- Summary for older context
- External memory for specific facts (user identity, preferences, in-flight task state)

### Use a Cheap Model for Summarization

Don't burn your strong generation model on summarization. Use Haiku/GPT-3.5
for summary; reserve the strong model for actual user-facing generation.

### Persist Critical Facts Explicitly

User identity, stated preferences, and in-flight task state should live in
structured storage (DB, key-value store) — not be inferred from conversation
summary.

---

## Best Practices for Agents (ReAct)

### The ReAct Loop Done Right

```
Thought → Action → Observation → repeat
```

**Practical advice:**
- **Limit tool inventory:** few high-leverage tools beat many narrow tools
- **Use tools with clear names and signatures:** the agent reads tool docs every turn
- **Log every Thought/Action/Observation:** without traces, debugging is impossible
- **Cap iterations:** typically 5-10 turns; beyond that, escalate

### Human-in-the-Loop Pattern

Fully autonomous ReAct agents have higher error rates. The book recommends
intermediate verification steps:
- Show the user the agent's plan before execution
- Allow user to override individual tool calls
- Present "best guess" responses with confidence; let user redirect

### When to Switch to Reflexion or Plan-and-Execute

- **ReAct:** Default for general tasks
- **Reflexion:** When errors compound and need correction (Shinn et al. 2023)
- **Plan-and-Execute:** When wrong moves are costly; benefit from upfront verification

---

## Best Practices for Multimodal Applications

### CLIP for Cross-Modal Retrieval

CLIP embeds images and text in the same vector space. Practical applications:
- **Zero-shot image classification:** Compare image embedding to text embeddings of candidate labels
- **Image search by text query:** Embed query text, find images with closest embeddings
- **Image-image similarity:** Direct cosine similarity between image embeddings

**Production tip:** Pre-compute image embeddings; compute text embeddings on-demand.

### BLIP-2 for Multimodal Generation

When you need to generate text from images (captioning, visual Q&A):
- **CLIP alone is insufficient** — it can't generate
- **BLIP-2** composes frozen ViT + frozen LLM via a small trainable Q-Former
- **Hosted multimodal APIs** (GPT-4V, Claude vision, Gemini) are usually the right starting point unless you have specific reasons to self-host

### Vision Transformer (ViT) Pattern

ViT adapts the Transformer architecture for images by converting them into
patches of pixels (rather than text tokens).

**Mental model:** Same architecture, different "tokens." A 224×224 image becomes
196 16×16 patches, each treated like a token.

---

## Best Practices for Fine-Tuning

### When to Fine-Tune

The book is conservative on this — fine-tune only when:
- Prompt + RAG hits a quality ceiling
- Task is narrow and stable
- You need a smaller deployable model (cost optimization)
- Domain-specific behavior can't be elicited via prompts

### PEFT (Parameter-Efficient Fine-Tuning) as Default

Don't full-finetune unless you have a specific reason. PEFT methods:

- **LoRA (Low-Rank Adaptation):** approximates large weight updates with smaller low-rank matrices
- **QLoRA:** quantized LoRA — enables fine-tuning of large models on single consumer GPU
- **Adapters:** insert small trainable modules into Transformer blocks

**LoRA rank guidance:**
- Higher rank = better representative power, less compression
- Typical: 8-64
- Start with 16; tune based on quality

### Alignment Techniques (DPO/ORPO over RLHF)

- **RLHF:** Classical approach. Powerful but complex (SFT → reward model → RL).
- **DPO (Direct Preference Optimization):** Eliminates the reward model. Simpler training.
- **ORPO (Odds Ratio Preference Optimization):** Combines SFT and DPO into one training loop.

**Practical advice:** For new alignment work, start with DPO. ORPO if you also
want SFT in the same pass.

### Goodhart's Law in Fine-Tuning

"When a measure becomes a target, it ceases to be a good measure."

Optimizing purely for a specific benchmark (e.g., grammatical correctness) can
degrade other useful capabilities. Always evaluate against multiple metrics
post-finetune.

---

## Worked Examples

### Example 1: Few-Shot Classification with SetFit

**Goal:** Classifier with only 32 labeled examples per class.

| Step | Action |
|---|---|
| 1 | Take pretrained sentence-transformer |
| 2 | Generate positive/negative pairs from your 32 examples (same-class = positive) |
| 3 | Fine-tune embedding model with contrastive learning on those pairs |
| 4 | Train simple classifier head (logistic regression) on resulting embeddings |
| 5 | Result: high-accuracy classifier from <50 labels |

**Lesson:** Few-shot wins when you have <100 labels per class. Beyond that,
full fine-tuning of a smaller model wins on cost and speed.

### Example 2: Production Search Pipeline

**Goal:** Search 50,000 internal engineering docs.

| Component | Choice |
|---|---|
| Architecture | Hybrid: BM25 + bi-encoder retrieval, cross-encoder reranking |
| Embedding model | SBERT, then domain-adapt via continued pretraining + contrastive fine-tuning |
| Continued pretraining | All 50K docs via MLM, 1 epoch |
| Contrastive training pairs | Mined from search logs (clicked = positive, top-K not-clicked = hard negative) |
| Cross-encoder | ms-marco-MiniLM-L-12-v2 base, fine-tuned on same pair distribution |

### Example 3: Image Search by Photo Upload + Text Query

**Goal:** Let users find products by photo or text.

| Step | Action |
|---|---|
| 1 | Embed all product images via CLIP image encoder, store in vector DB |
| 2 | User uploads photo → embed via CLIP image encoder |
| 3 | Find K nearest neighbors in product image embedding space |
| 4 | User searches text "blue running shoes" → embed via CLIP text encoder |
| 5 | Search same vector space (text and image embeddings co-exist) |

**No labeled training needed.** CLIP's pretrained shared space handles zero-shot
classification on whatever products you have.

---

## Anti-Patterns

### Cross-Encoder for Large-Scale Search

Using cross-encoder to score every (query, doc) pair in a 10K corpus.
**Why it fails:** O(N) at query time. Latency unbearable.
**The fix:** Bi-encoder for first-pass retrieval, cross-encoder for reranking.

### Using CLIP for Tasks Requiring Generation

CLIP is an embedding model, not a generative one. It has no decoder.
**The fix:** Use BLIP-2 or hosted multimodal APIs (GPT-4V, Claude vision, Gemini).

### Easy Negatives Only

Sampling negatives randomly from the corpus.
**Why it fails:** Random negatives are obvious; model doesn't learn fine distinctions.
**The fix:** Mine hard negatives.

### Skipping Domain Adaptation on Specialized Corpora

Using OpenAI ada embeddings for medical document retrieval.
**Why it fails:** Generic model misses domain terminology; recall is poor.
**The fix:** Continued pretraining + contrastive fine-tuning on your corpus.

### Full Fine-Tuning When Few-Shot Works

Labeling 5,000 examples to fine-tune a classifier when SetFit could work with 50.
**Why it fails:** Wasted labeling cost; longer iteration cycle.
**The fix:** Try SetFit first with <100 labels per class.

### Static Window That Loses Critical Facts

ConversationBufferWindowMemory with K=5 in long-running customer support chat.
**Why it fails:** User said their account ID 10 turns ago; window discarded it.
**The fix:** Selective memory — extract critical entities; persist explicitly.

---

## Process Wisdom

### The "build something working, then understand" approach

The authors push readers toward immediate hands-on experimentation. Read
just enough theory to start; build something; iterate.

**Practical habit:** When learning a new technique, prototype it on a
realistic-but-small dataset before committing to production.

### Prefer modular composition over monolithic frameworks

BERTopic and sentence-transformers are designed as modular libraries because
real applications need to swap components.

**Implication for your tooling:** When evaluating an LLM library, prefer ones
that let you replace any component (embedding model, retriever, reranker, generator).

### Treat embeddings as a separate engineering concern

Embedding pipelines have their own lifecycle:
- Embedding model selection
- Continued pretraining (if domain-adapted)
- Vector store choice and indexing strategy
- Refresh cadence (re-embed when source data changes)
- Migration strategy (when you upgrade the embedding model)

This deserves explicit ownership and engineering investment, not "we'll figure it out."

---

## When to Apply These Practices

This expert reference complements:

- For prompting techniques → also see `advanced-prompting-techniques/SKILL.md`
- For embeddings → also see `embedding-models-and-domain-adaptation/SKILL.md`
- For memory + multimodal → also see `llm-conversation-memory-and-multimodal/SKILL.md`
- For frameworks catalog → see `frameworks.md` in this folder
