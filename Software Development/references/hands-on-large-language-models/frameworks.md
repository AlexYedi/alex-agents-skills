# Frameworks: Hands-On Large Language Models

**Source:** *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst

A catalog of every framework, pattern, and named technique introduced or
applied in this book. Use alongside `additional-experts.md` for application
guidance.

---

## Framework Index (Alphabetical)

| Framework | Domain | When to apply |
|---|---|---|
| Adapters | Fine-tuning | Modular task specialization |
| Attention | Architecture | Foundation of Transformers |
| Autoregressive Generation | Inference | Token-by-token text generation |
| BERT (Encoder-Only) | Architecture | Classification, embeddings |
| BERTopic | Topic modeling | Modular semantic topic modeling |
| Bi-encoder (SBERT) | Embeddings | Scalable similarity search |
| BLIP-2 | Multimodal | Frozen-model multimodal generation |
| Byte Pair Encoding (BPE) | Tokenization | General-purpose tokenization |
| Chain-of-Thought (CoT) | Prompting | Reasoning tasks |
| ConversationBufferMemory | Conversation | Short conversations, perfect recall |
| ConversationBufferWindowMemory | Conversation | Bounded recent context |
| ConversationSummaryMemory | Conversation | Long conversations, semantic recall |
| Constrained Sampling | Prompting | Reliable structured output |
| Context Window | Architecture | Token limit constraint |
| Continued Pretraining | Fine-tuning | Domain adaptation step 1 |
| Contrastive Learning | Embeddings | Training embedding models |
| Cross-encoder | Embeddings | Reranking precision |
| Decoder-Only Models (GPT family) | Architecture | Generative tasks |
| Dense Retrieval | RAG | Semantic search via embeddings |
| Direct Preference Optimization (DPO) | Alignment | Simpler RLHF alternative |
| Domain Adaptation | Embeddings | Improving on specialized corpora |
| Embeddings (concept) | Foundation | Underlying abstraction |
| Encoder-Only Models | Architecture | Representation tasks |
| Encoder-Decoder Models (T5) | Architecture | Sequence-to-sequence tasks |
| Few-Shot Classification | NLP | Classification with limited labels |
| Few-Shot Prompting | Prompting | Reducing prompt ambiguity |
| Fine-Tuning | Adaptation | Behavior alignment via examples |
| Foundation Models | Architecture | General-purpose pretrained models |
| GPT (1, 2, 3, 3.5, 4) | Architecture | Generative LLMs |
| Goodhart's Law | Eval discipline | Single-metric warning |
| Grounded Generation | RAG | Reduce hallucination |
| Hard Negatives | Embeddings | Contrastive training quality |
| HDBSCAN | Clustering | Density-based topic clustering |
| Instruction Tuning | Fine-tuning | Aligning models with instructions |
| Key-Value Caching | Inference | Decoder speedup |
| KeyBERTInspired | Topic modeling | Topic representation refinement |
| LangChain (chain extensions) | Application | Composing LLM workflows |
| Large Language Models (LLMs) | Architecture | Generative models with billions of params |
| LoRA (Low-Rank Adaptation) | Fine-tuning | PEFT default |
| Masked Language Modeling (MLM) | Pretraining | Bidirectional pretraining |
| Masked Self-attention | Architecture | Decoder attention pattern |
| Maximal Marginal Relevance (MMR) | Topic modeling | Diverse topic keywords |
| Mean Pooling | Embeddings | SBERT default |
| Modular Prompt Framework | Prompting | Composable prompt design |
| Multi-Modal Models | Architecture | Cross-modality applications |
| Odds Ratio Preference Optimization (ORPO) | Alignment | Combined SFT + DPO |
| Parameter-Efficient Fine-Tuning (PEFT) | Fine-tuning | Memory-efficient adaptation |
| Pre-training | Training | Foundation step before fine-tuning |
| Preference Tuning | Alignment | Output quality refinement |
| Pretraining and Fine-Tuning | Training pattern | Two-step adaptation |
| QLoRA | Fine-tuning | Quantized LoRA |
| RAG (Retrieval-Augmented Generation) | Application | Knowledge-heavy tasks |
| Recurrent Neural Networks (RNNs) | Architecture | Pre-Transformer era; sequential |
| ReAct (Reason + Act) | Agents | Foundational agent loop |
| Reranking | RAG | Precision improvement |
| Reward Models | Alignment | RLHF component |
| Self-attention | Architecture | Parallel sequence processing |
| Self-Consistency | Prompting | Variance reduction via majority vote |
| Sentence-Transformers | Embeddings | Production embedding library |
| SetFit | Few-shot classification | Classifier with <100 labels |
| Siamese Network (Bi-encoder structure) | Embeddings | Contrastive training topology |
| SimCSE | Embeddings | Unsupervised sentence embedding |
| Soft Visual Prompts | Multimodal | Vision-to-LLM bridge |
| Sentence-BERT (SBERT) | Embeddings | Production sentence embeddings |
| Supervised Fine-Tuning (SFT) | Fine-tuning | Behavior alignment via examples |
| TextGeneration (BERTopic representation) | Topic modeling | Human-readable topic labels |
| Tokenization Methods | Pre-processing | Text → tokens conversion |
| Topic Modeling Framework | NLP | Document clustering + naming |
| Transformer Architecture | Architecture | Foundation of all modern LLMs |
| Tree-of-Thoughts (ToT) | Prompting | Multi-path reasoning |
| TSDAE | Embeddings | Unsupervised domain adaptation |
| Vision Transformer (ViT) | Multimodal | Image as patches/tokens |
| Word2vec | Embeddings | Static word embeddings |
| Zero-Shot Tree-of-Thoughts | Prompting | Cheaper ToT variant |

---

## Framework Catalog (Detailed)

### Transformer Architecture

**Originator:** Vaswani et al., "Attention Is All You Need" (2017)

**Components:**
- **Tokenizer:** Converts text into tokens
- **Stack of Transformer blocks:** Each contains self-attention + feedforward
- **Language Modeling Head (LM head):** Outputs probability distribution over vocabulary

**Variants by composition:**
- **Encoder-only (BERT):** representation models
- **Decoder-only (GPT):** generative models
- **Encoder-decoder (T5):** sequence-to-sequence

---

### Attention Mechanisms

**Attention** — Bahdanau et al. (2014) original; revolutionized by Transformers
- Allows model to focus on relevant parts of input sequence
- Improves over fixed-length embeddings for long sentences

**Self-attention** — Vaswani et al. (2017)
- Attention applied within a single sequence
- Enables parallel training; captures long-range dependencies

**Masked self-attention** — Decoder-specific
- Masks future positions
- Prevents information leakage during autoregressive generation

---

### Foundation Models

**Definition (this book):** Open-source base models (Llama 2, Mistral, Phi, Falcon)
that undergo pretraining on massive datasets (e.g., 2 trillion tokens) and can
be fine-tuned for specific tasks.

**Distinction from earlier ML:** Pretrained once; adapted many times. Eliminates
need to train from scratch for each task.

---

### Encoder-Only Models (BERT)

**Originator:** Devlin et al. (2018)

**Pretraining:** Masked Language Modeling (MLM) — randomly mask tokens; predict them.

**Use cases:**
- Classification
- Embedding generation
- NER (Named Entity Recognition)

**Variants:** BERT, RoBERTa, ALBERT, DeBERTa, DistilBERT

---

### Decoder-Only Models (GPT family)

**Architecture:** Stacked decoder blocks; autoregressive generation.

**GPT family progression:** GPT-1 → GPT-2 → GPT-3 (175B params) → GPT-3.5 → GPT-4

**Used as:** Generative models; foundation for instruction-tuned and chat models.

---

### Encoder-Decoder Models (T5)

**Originator:** Raffel et al. (2020), Google

**Used for:** Sequence-to-sequence tasks where input → output transformation is required.

**Examples:** Translation, summarization, structured generation.

---

### Tokenization Methods

**Byte Pair Encoding (BPE):**
- Iteratively merges frequent character pairs
- Default for GPT family
- Balance between vocabulary size and sequence length

**WordPiece:**
- Used in BERT family
- Similar to BPE but uses likelihood-based merging

**Character-level tokens:**
- One token per character
- Robust to typos but creates very long sequences

**Byte tokens:**
- One token per byte
- Universal across languages and modalities

---

### Pretraining and Fine-Tuning Pattern

**Step 1 — Pretraining:**
- Train on massive unlabeled dataset
- Self-supervised (masked language modeling, next-token prediction)

**Step 2 — Fine-tuning:**
- Adapt to specific task with smaller labeled dataset
- Updates pretrained weights

**Why this dominates:** Saves resources; pretraining is one-time; many tasks
share the same pretrained foundation.

---

### Embeddings

**Definition:** Numeric representations created for tokens (static or contextual)
or entire documents/sentences to capture semantic meaning.

**Types:**
- **Static embeddings (Word2vec):** Fixed per token
- **Contextual embeddings (BERT, GPT):** Vary by surrounding context
- **Sentence embeddings (SBERT):** Single vector per sentence

---

### Word2vec Algorithm

**Originator:** Mikolov et al. (2013), Google

**Methods:**
- **Skip-gram:** Predict surrounding words from a target word
- **CBOW (Continuous Bag of Words):** Predict target from surroundings
- **Negative sampling:** Train against contrastive negatives

**Use cases:** Recommendation systems, static word embeddings.

---

### Sentence-BERT (SBERT)

**Originator:** Reimers and Gurevych (2019)

**Structure:** Siamese network (bi-encoder) topology with mean pooling on
final BERT layer to produce fixed-size sentence embeddings.

**Why it solved the problem:** Cross-encoders had high accuracy but poor
scalability. SBERT enables fast similarity search via vector store.

---

### Bi-encoder vs Cross-encoder

**Bi-encoder:** Two identical networks; produces independent embeddings; compare via dot product.
- Pros: Fast at scale; embeddings precomputable
- Cons: Less accurate than cross-encoder for nuanced similarity

**Cross-encoder:** Pair of sentences passed jointly to one network; outputs single similarity score.
- Pros: Highest accuracy
- Cons: Slow; can't precompute; doesn't scale

**Production pattern:** Bi-encoder for retrieval; cross-encoder for reranking.

---

### Contrastive Learning

**Definition:** Train models on pairs of similar and dissimilar examples.

**Components:**
- **Positive pair:** Two semantically similar texts (or text+image, etc.)
- **Negative pair:** Two semantically different examples
- **Hard negatives:** Negatives that look similar but are different
- **Easy negatives:** Obviously different negatives

**Why hard negatives matter:** Force the model to learn fine-grained distinctions.

---

### Modular Prompt Framework

**Originator:** This book

**Components:**

| Component | Role |
|---|---|
| Persona | Role the model adopts |
| Instruction | The specific task |
| Context | Background information |
| Format | Output structure |
| Audience | Who reads the output |
| Tone | Voice characteristics |
| Data | Inputs to operate on |
| Examples (few-shot) | Concrete demonstrations |

**Practice:** Tune each component independently; reuse strong components.

---

### Chain-of-Thought (CoT)

**Originator:** Wei et al. (2022)

**Structure:** Force the model to reason explicitly before answering.

**Variants:**
- **Zero-Shot CoT:** Append "Let's think step by step"
- **Few-Shot CoT:** Provide reasoning examples
- **Auto-CoT:** Generate reasoning examples programmatically

---

### Self-Consistency

**Originator:** Wang et al. (2022)

**Structure:** Sample the same prompt N times with temperature > 0; majority-vote.

**When to use:** Discrete-answer tasks where stakes justify N× cost. Sweet spot: 3-5 samples.

---

### Tree-of-Thoughts (ToT)

**Originator:** Yao et al. (2023)

**Structure:** Explore multiple reasoning paths; evaluate; prune low-probability branches.

**Variants:**
- **Full ToT:** Iterative model calls; expansion + evaluation + pruning
- **Zero-Shot ToT:** Single prompt simulating multi-expert conversation

---

### Constrained Sampling

**Methods:**
- **Logit filtering:** Mask invalid tokens at generation
- **Grammar constraints:** BNF, regex
- **JSON mode:** API-level (OpenAI/Anthropic)
- **Outlines / Guidance libraries:** Wrap constrained sampling

---

### Conversation Memory Patterns

**ConversationBufferMemory:**
- Append entire history to every prompt
- Best for short conversations; perfect recall

**ConversationBufferWindowMemory:**
- Keep only the last K turns
- Best for bounded latency + cost

**ConversationSummaryMemory:**
- Summarize history with separate LLM, pass summary
- Best for long conversations; semantic recall over verbatim

**Hybrid patterns (production reality):**
- Window + Summary
- Selective Memory (extract specific entities)
- External Memory Store (DB / vector store)

---

### Topic Modeling Framework (BERTopic)

**Originator:** Maarten Grootendorst (this book's author)

**Pipeline:**
1. Convert documents to embeddings
2. Reduce dimensionality (UMAP)
3. Cluster (HDBSCAN)
4. Topic representation (c-TF-IDF, KeyBERTInspired, MMR, TextGeneration)

**Why modular:** Each step is swappable; users can stack representation methods.

---

### Class-based TF-IDF (c-TF-IDF)

**Definition:** Calculate word frequencies within entire clusters rather than
per document. Weight by inverse class frequency to penalize words common across all clusters.

**Why it matters:** Document-level bag-of-words misses cluster-distinguishing terms.
c-TF-IDF surfaces them.

---

### KeyBERTInspired

**Definition:** Representation model that updates topic keywords by averaging
embeddings of representative documents in each cluster.

**When to use:** As a stage in BERTopic pipeline to refine c-TF-IDF output.

---

### Maximal Marginal Relevance (MMR)

**Definition:** Algorithm to diversify topic representations by iteratively
selecting keywords that are diverse from one another but still relevant.

**When to use:** When topic representations are too similar; need to differentiate.

---

### TextGeneration (Topic Representation)

**Definition:** Use pretrained generative LLMs (Flan-T5, GPT-3.5) via prompt
engineering to generate human-readable labels for topics.

**Pattern:** Prompt the LLM with: "Given these representative documents and
keywords, generate a 5-word topic name."

---

### ReAct (Reason + Act)

**Originator:** Yao et al. (2022)

**Loop:**
```
Thought → Action → Observation → repeat until done
```

**When to apply:** General agent tasks; foundational pattern.

---

### Dense Retrieval

**Definition:** Relies on embeddings to convert queries and documents into
numeric representations where similar meanings result in close proximity.

**Compare to:** Lexical retrieval (BM25) which matches on exact terms.

---

### Reranking (in RAG)

**Definition:** Second stage in search pipeline where an LLM acts as a
cross-encoder to re-order shortlisted results based on relevance scores.

**When to use:** When retrieval recall is high but precision is low.

---

### RAG (Retrieval-Augmented Generation)

**Definition:** A system incorporating search capabilities followed by grounded
generation, where retrieved context is provided to an LLM to answer questions
and reduce hallucinations.

**Components:** Retriever (dense or hybrid) + Reranker (optional) + Generator (LLM)

---

### Vision Transformer (ViT)

**Originator:** Dosovitskiy et al. (2020)

**Structure:** Adapts the Transformer architecture for computer vision by
converting images into patches of pixels rather than text tokens.

**Mental model:** A 224×224 image becomes 196 16×16 patches, each treated as a token.

---

### CLIP (Contrastive Language-Image Pre-training)

**Originator:** Radford et al. (2021), OpenAI

**Structure:** Embedding model that computes embeddings for both images and texts
in the same vector space.

**Capabilities:**
- Zero-shot image classification
- Cross-modal retrieval (text → image, image → text)
- Image-text similarity scoring

---

### BLIP-2

**Originator:** Li et al. (2023)

**Structure:** Connects frozen ViT to frozen LLM via small trainable Q-Former (32 query embeddings → soft prompts).

**Why it matters:** Composes existing vision and language models with small
trainable bridge. ~100x less training cost than end-to-end multimodal.

---

### Soft Visual Prompts

**Definition:** Convert extracted visual features from encoders (like ViT) into
learnable embeddings that act as contextual inputs to condition a textual LLM.

**Use case:** Bridging modalities without training the LLM from scratch.

---

### Fine-Tuning Hierarchy

**Supervised Fine-Tuning (SFT):**
- Train on (prompt, response) pairs
- Teaches conversational behavior

**Preference Tuning:**
- Generate multiple outputs; humans rank them
- Use preference data to refine quality

**RLHF (Reinforcement Learning from Human Feedback):**
- SFT → reward model → RL optimization
- Classical alignment approach

**Direct Preference Optimization (DPO):**
- Eliminates reward model
- Compares log probabilities of accepted vs rejected directly

**ORPO (Odds Ratio Preference Optimization):**
- Combines SFT and DPO into one training loop
- Works with QLoRA

---

### Parameter-Efficient Fine-Tuning (PEFT)

**Definition:** Techniques avoiding updating all model weights to improve
computational efficiency.

**Categories:**
- **Adapter-based:** Insert small modules (LoRA, BitFit, IA3)
- **Soft prompt-based:** Trainable input embeddings (prefix-tuning, P-Tuning)

---

### LoRA (Low-Rank Adaptation)

**Originator:** Hu et al. (2021)

**Structure:** Approximate large weight matrices with smaller low-rank matrices
(A and B). Only A and B are updated.

**Rank guidance:** 8-64 typical. Higher rank = better representation, less compression.

---

### QLoRA

**Originator:** Dettmers et al. (2023)

**Structure:** Quantized LoRA — stores model weights in 4-bit NF4 format during
finetuning, dequantizes back to BF16 during computation.

**Why it matters:** Enables fine-tuning of large models on single consumer GPU.

---

### SetFit (Few-Shot Classification)

**Definition:** Efficient framework built on sentence-transformers for few-shot
text classification.

**Pipeline:**
1. Take pretrained sentence-transformer
2. Generate positive/negative pairs from few labeled examples (same-class = positive)
3. Fine-tune embedding model with contrastive learning
4. Train classifier head (logistic regression) on resulting embeddings

**When to use:** <100 labels per class.

---

### TSDAE (Transformer-based Sequential Denoising Auto-Encoder)

**Definition:** Unsupervised technique that randomly removes words from input,
passes through encoder, reconstructs original sentence.

**When to use:** Domain adaptation when labeled pairs aren't available.

---

### Continued Pretraining

**Definition:** Process of continuing pretraining of an already-pretrained
BERT model using masked language modeling (MLM) with domain-specific data.

**When to use:** Domain adaptation step 1 (before contrastive fine-tuning).

---

### Goodhart's Law (in Fine-Tuning)

**Statement:** "When a measure becomes a target, it ceases to be a good measure."

**Application:** Optimizing purely for a specific benchmark can degrade other
useful capabilities. Always evaluate against multiple metrics.

---

### Key-Value Caching

**Definition:** To speed up autoregressive generation, results of previous
calculation steps (specifically keys and values matrices in the attention
mechanism) are cached rather than recomputed.

**Why it matters:** Without KV caching, generation is O(n²); with it, O(n).

---

### Context Window

**Definition:** Maximum number of tokens an LLM can process. Increases dynamically
as architectures evolve.

**Practical implication:** Longer context = more capability but higher cost
and risk of attention dilution (NIAH effect).

---

## Cross-Reference Map

```
                  ┌────────────────────┐
                  │ Transformer Arch.  │
                  └────────┬───────────┘
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
          ┌──────────┐┌──────────┐┌──────────┐
          │ Encoder- ││ Decoder- ││ Encoder- │
          │ Only     ││ Only     ││ Decoder  │
          │ (BERT)   ││ (GPT)    ││ (T5)     │
          └─────┬────┘└─────┬────┘└──────────┘
                │           │
                ▼           ▼
          ┌──────────┐┌──────────┐
          │Embedding ││Generation│
          │ tasks    ││ tasks    │
          └──────────┘└──────────┘

  Pretraining → Fine-tuning two-step:
  ┌─────────────────────────────┐
  │ Pretraining (MLM/causal LM) │
  └────────┬────────────────────┘
           │
           ▼
  ┌─────────────────┐
  │ SFT             │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────────────┐
  │ Preference Tuning       │
  │ (RLHF / DPO / ORPO)     │
  └─────────────────────────┘
           │
           ▼ (memory-efficient via)
  ┌─────────────────┐
  │ PEFT            │ ─→ LoRA, QLoRA, Adapters, Soft Prompts
  └─────────────────┘

  Embeddings:
  ┌─────────────┐  ┌──────────────┐
  │ Word2vec    │  │ Sentence-BERT│
  │ (static)    │  │ (contextual) │
  └─────────────┘  └──────────────┘
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
      ┌──────────┐ ┌──────────────┐ ┌──────────┐
      │Bi-encoder│ │Cross-encoder │ │SetFit    │
      │ (search) │ │(rerank)      │ │(few-shot)│
      └──────────┘ └──────────────┘ └──────────┘

  Domain adaptation:
  ┌────────────────────────┐
  │ Continued Pretraining  │ → MLM on your domain
  └──────────┬─────────────┘
             ▼
  ┌────────────────────────┐
  │ Contrastive Fine-tuning│ → with hard negatives
  └────────────────────────┘
  Alternatives: TSDAE, SimCSE (unsupervised)

  Prompting:
  ┌────────────────────┐
  │ Modular Prompt     │ → Persona + Instruction + Context + Format + Audience + Tone + Data + Examples
  │ Framework          │
  └─────┬──────────────┘
        │
        ├──→ CoT (zero/few-shot)
        ├──→ Self-Consistency
        ├──→ Tree-of-Thoughts
        └──→ Constrained Sampling

  Memory + Agents (LLM applications):
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │ Buffer       │  │ Window       │  │ Summary      │
  │ Memory       │  │ Memory       │  │ Memory       │
  └──────────────┘  └──────────────┘  └──────────────┘
                          ↓
                   Hybrid in production
                          ↓
  ┌──────────────────────────────────────────────────┐
  │ ReAct Agent (Thought → Action → Observation)     │
  └──────────────────────────────────────────────────┘

  Topic Modeling (BERTopic):
  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────────┐
  │ Embed   │→│ UMAP     │→│ HDBSCAN  │→│ Representation   │
  │         │ │ (reduce) │ │ (cluster)│ │ (c-TF-IDF, MMR,  │
  │         │ │          │ │          │ │  KeyBERT, GenLLM)│
  └─────────┘ └──────────┘ └──────────┘ └──────────────────┘

  Multimodal:
  ┌──────┐    ┌──────┐    ┌────────┐
  │ ViT  │ ──→│ CLIP │ ──→│ BLIP-2 │ → multimodal generation
  └──────┘    └──────┘    └────────┘
   (image)    (cross-     (vision-to-LLM bridge via
              modal       Q-Former + soft prompts)
              search)

  RAG:
  ┌────────┐  ┌──────────┐  ┌────────────┐  ┌─────────────┐
  │ Dense  │→ │ Hybrid   │→ │ Reranking  │→ │ Grounded    │
  │ Retr.  │  │ Search   │  │            │  │ Generation  │
  └────────┘  └──────────┘  └────────────┘  └─────────────┘
```

---

## How to use this catalog

- **Vaguely remember a name?** → Browse the alphabetical index
- **Picking a fine-tuning approach?** → See PEFT and alignment subsections
- **Designing a search pipeline?** → See bi-encoder vs cross-encoder + reranking
- **Building multimodal?** → See CLIP, BLIP-2, ViT
- **Need expert advice?** → See `additional-experts.md`
