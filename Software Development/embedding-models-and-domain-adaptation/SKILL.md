---
name: embedding-models-and-domain-adaptation
description: >
  Choose, train, and adapt text embedding models for production. Covers SBERT
  vs cross-encoder tradeoffs, contrastive learning, domain adaptation via
  continued pretraining, few-shot classification with SetFit, and hard-negative
  mining. Use when building semantic search, RAG retrieval, classification
  with limited labels, when generic embeddings underperform on your domain,
  or when picking between cross-encoder and bi-encoder architectures. Triggers:
  "choose an embedding model", "domain-adapt our embeddings", "few-shot
  classification", "SetFit for X", "cross-encoder vs bi-encoder", "embedding
  fine-tuning", "hard negatives". Produces concrete embedding strategy.
---

# Embedding Models and Domain Adaptation

You design and adapt embedding models for production retrieval, classification,
and similarity tasks. Off-the-shelf embeddings work for general tasks but
underperform on specialized domains. This skill covers when and how to adapt.

---

## When to Use This Skill

- Building semantic search or RAG and choosing the embedding model
- Off-the-shelf embeddings underperform on your domain (legal, medical, internal docs)
- Few-shot classification with limited labeled data
- Choosing between cross-encoder and bi-encoder architectures
- Setting up contrastive training for custom embeddings

---

## Bi-encoder vs Cross-encoder: Architectural Choice

The fundamental tradeoff in retrieval / similarity systems.

| Architecture | How it works | Pros | Cons |
|---|---|---|---|
| **Bi-encoder (SBERT)** | Two identical BERT models; produces independent embeddings; compare via dot product | Fast at scale; embeddings can be precomputed; supports vector search | Less accurate than cross-encoder for complex similarity |
| **Cross-encoder** | Pair of sentences fed jointly to one Transformer; outputs single similarity score | Highest accuracy; captures interactions between sentences | Slow; can't precompute; doesn't scale to large corpora |

### When to Use Which

```
Need to search/retrieve over a corpus of N documents?
├── N < 1000 and latency is not critical → Cross-encoder works
├── N > 1000, need fast retrieval → Bi-encoder (SBERT)
└── Want best of both → Bi-encoder for first-pass retrieval + Cross-encoder for reranking top-k
```

**Production default:** Hybrid. Bi-encoder retrieves top-50; cross-encoder
reranks to top-5. This pattern dominates in production search.

---

## Sentence-Transformers (SBERT): The Production Standard

SBERT solves the cross-encoder cost problem by using mean pooling over the
final BERT layer. This produces fixed-size embeddings that scale.

- **Mean pooling** averages the token embeddings to get a single vector
- **Siamese network structure** trains both encoders with shared weights
- **Contrastive learning** is the typical training objective

The `sentence-transformers` library is the production-grade implementation.

---

## Contrastive Learning: How Embeddings Get Trained

Train the model on pairs of similar and dissimilar examples. The model learns
to map similar pairs close together in embedding space, dissimilar pairs far apart.

### Components

| Component | What it is | Why it matters |
|---|---|---|
| **Positive pair** | Two semantically similar texts | Anchors what "similar" means in your domain |
| **Negative pair** | Two semantically different texts | Anchors what "different" means |
| **Hard negatives** | Negatives that *look* similar but are semantically different | Forces the model to learn fine-grained distinctions |
| **Easy negatives** | Negatives that are obviously different | Cheap to mine but limit ceiling |

### Hard Negatives Are the Lever

Easy negatives produce mediocre models. Hard negatives produce strong models.

**Hard negative mining strategies:**
- BM25 top-K (textually similar but wrong answer)
- Same topic, different intent
- Adversarial generation via LLM
- Existing retrieval system's top wrong results

**Rule:** If your retrieval is mediocre, the issue is usually negatives, not architecture.

---

## Domain Adaptation: When Generic Embeddings Fail

Generic embedding models (OpenAI ada, Cohere, Voyage) work for general text but
underperform on domain-specific corpora (legal, medical, internal documentation,
non-English).

### Two-Step Adaptation

```
Step 1: Continued Pretraining (MLM)
  - Take pretrained BERT
  - Continue training on YOUR domain text using masked language modeling
  - Updates subword representations to your vocabulary
  - Output: domain-aware base model

Step 2: Fine-tuning with Contrastive Objective
  - Use Step 1 model as starting point
  - Train on (positive, negative) pairs from your domain
  - Output: domain-adapted embedding model
```

### Lighter-Weight Alternatives

| Method | Best when | Limitation |
|---|---|---|
| **TSDAE** (Transformer-based Sequential Denoising Auto-Encoder) | Unlabeled domain text only; no pairs available | Quality below contrastive but better than generic |
| **SimCSE** | Similar to TSDAE but uses different augmentation | Comparable quality |
| **Synthetic pair generation** | Use LLM to generate positive/negative pairs from your corpus | Quality depends on LLM and prompts |

---

## SetFit: Few-Shot Classification

When you have limited labeled data (e.g., 32 examples per class) but need a
classifier, SetFit is the right tool.

### How SetFit Works

1. Take a pretrained sentence-transformer
2. Generate positive/negative pairs from your few labeled examples (e.g., same-class = positive)
3. Fine-tune the embedding model with contrastive learning on those pairs
4. Train a simple classifier head (logistic regression) on the resulting embeddings
5. Result: high-accuracy classifier from <50 labels

**When to use SetFit:** Few-shot classification (32-100 examples per class).
Outperforms full fine-tuning of a classifier in this regime.

**When NOT to use SetFit:** You have plenty of labels (>1000 per class). Full
fine-tuning of a smaller model wins on cost and speed.

---

## Principles

- **Hybrid retrieval is the default.** Bi-encoder for scale + cross-encoder for precision.
- **Hard negatives matter more than architecture choice.** Spending time on negative mining beats picking a fancier model.
- **Domain adaptation is high-leverage.** Generic embeddings underperform on specialized text. Continued pretraining + fine-tuning closes the gap.
- **Contrastive learning is the workhorse.** Most modern embedding training uses some form of it.
- **Few-shot wins with the right framework.** SetFit can match thousand-label classifiers using <100 labels.
- **Mean pooling > pooling alternatives in most cases.** Stick with sentence-transformers conventions.

---

## Anti-Patterns to Avoid

### Cross-encoder for Large-Scale Search

**Looks like:** Using cross-encoder to score every (query, doc) pair in a 10K corpus.

**Why it fails:** O(N) at query time. Latency unbearable.

**The fix:** Bi-encoder for first-pass retrieval, cross-encoder for reranking top-K.

### Easy Negatives Only

**Looks like:** Sampling negatives randomly from the corpus.

**Why it fails:** Random negatives are usually obvious; model doesn't learn fine distinctions.

**The fix:** Mine hard negatives via BM25, existing retrieval mistakes, or adversarial generation.

### Skipping Domain Adaptation on Specialized Corpora

**Looks like:** Using OpenAI ada embeddings for medical document retrieval.

**Why it fails:** Generic model misses domain terminology; retrieval recall is poor.

**The fix:** Continued pretraining + contrastive fine-tuning on your corpus.

### Full Fine-tuning When Few-Shot Works

**Looks like:** Labeling 5,000 examples to fine-tune a classifier when SetFit could work with 50.

**Why it fails:** Wasted labeling cost; longer iteration cycle.

**The fix:** Try SetFit first with <100 labels per class. Scale up only if quality is insufficient.

---

## Decision Rules

| Condition | Action |
|---|---|
| Need fast retrieval over large corpus | Bi-encoder (SBERT) |
| Need highest similarity precision, scale is small | Cross-encoder |
| Want both | Bi-encoder retrieval + cross-encoder reranking |
| Generic embeddings underperform on your domain | Continued pretraining + contrastive fine-tuning |
| Have unlabeled domain text only | TSDAE or SimCSE |
| Need classifier with <100 labels per class | SetFit |
| Have abundant labels | Full fine-tuning of smaller classifier |
| Retrieval quality is mediocre | Improve negatives before changing architecture |

---

## Worked Example: Internal Documentation Search

**Goal:** Build search over 50,000 internal engineering docs (RFCs, postmortems, runbooks).

| Decision | Choice | Rationale |
|---|---|---|
| **Architecture** | Hybrid: BM25 + bi-encoder for retrieval, cross-encoder for reranking | Internal jargon needs BM25; semantic match needs embeddings; reranker improves precision@5 |
| **Embedding model** | Off-the-shelf SBERT, then domain-adapt via continued pretraining + contrastive fine-tuning | Generic underperforms; domain has specific terminology |
| **Continued pretraining** | All 50K docs via MLM, 1 epoch | Updates subword reps to engineering vocabulary |
| **Contrastive training pairs** | Mined from search logs (clicked = positive, top-K not-clicked = hard negative) | Free signal from real users |
| **Cross-encoder for reranking** | ms-marco-MiniLM-L-12-v2 base, fine-tune on same pair distribution | Reranker captures fine-grained intent matching |

**Lesson:** No single model is optimal. The architecture is a hybrid; domain
adaptation is a multi-step process; negative mining matters more than model choice.

---

## Gotchas

- **Embedding dimensionality vs latency.** Higher dim (1536+) = better quality, more storage cost, slower search. Test dim reduction (e.g., 768→256 with PCA) for cost-quality tradeoff.
- **Batch size in contrastive training.** Larger batches → better hard negatives within batch → better model. GPU memory is the constraint.
- **MLM masking rate.** 15% is the BERT default; some domains benefit from higher rates.
- **Reranker latency.** Cross-encoders add 100-500ms. Budget for it.
- **Cosine vs dot product similarity.** Convention matters; mismatched normalization breaks downstream tools.

Source: *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst, embedding chapters.
