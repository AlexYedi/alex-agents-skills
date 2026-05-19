---
name: llm-conversation-memory-and-multimodal
description: >
  Design conversation memory for LLM applications and integrate multimodal
  models (vision + language). Covers ConversationBufferMemory variants, the
  token-limit/recall tradeoff, ViT, CLIP, and BLIP-2. Use when building a
  chatbot or agent that needs to remember context across turns, when token
  limits are forcing memory tradeoffs, or when adding image/video understanding
  to an LLM application. Triggers: "conversation memory for our chatbot",
  "agent forgets earlier turns", "buffer vs summary memory", "add vision to
  our LLM", "CLIP for image search", "BLIP-2 for image captioning",
  "multimodal LLM patterns". Produces structured memory strategy and
  multimodal integration design.
---

# LLM Conversation Memory and Multimodality

You design two things LLM applications get wrong often: how to maintain context
across multi-turn conversations within token limits, and how to integrate
visual understanding into text-based LLM workflows.

---

## When to Use This Skill

- Building a chatbot or agent that needs context across multiple turns
- Token limits are forcing tradeoffs between memory completeness and cost
- Adding image or video understanding to an existing LLM application
- Choosing between CLIP-style embeddings and BLIP-2 visual prompting

---

## Part 1: Conversation Memory Patterns

LLMs have no memory between calls. Every interaction is stateless. To create
the *appearance* of conversation, you must explicitly pass prior context.
The challenge: token limits.

### Three Memory Patterns

| Pattern | Mechanism | Best for | Failure mode |
|---|---|---|---|
| **ConversationBufferMemory** | Append the entire history to every prompt | Short conversations; perfect recall is critical | Token limit exceeded; cost grows with conversation length |
| **ConversationBufferWindowMemory** | Keep only the last K turns | Bounded latency + cost; older context not needed | Loses information older than the window (e.g., user said their age 20 turns ago) |
| **ConversationSummaryMemory** | Summarize history with a separate LLM, pass the summary | Long conversations; semantic recall matters more than verbatim | Specific details lost in summarization; adds latency for the summary call |

### The Three-Way Tradeoff

```
                Cost / Latency
                      │
                      │
       Buffer ●       │
                      │
          ●  Window   │
                      │
                      │       ● Summary
                      │
                      └────────────────── Recall fidelity
```

- **Buffer:** Highest fidelity, highest cost
- **Window:** Bounded cost, fidelity capped by window size
- **Summary:** Lower cost than buffer for long convos, but specific facts can be lost

### Hybrid Patterns (the production reality)

Pure patterns rarely fit production needs. Common hybrids:

- **Window + Summary:** Keep last K turns verbatim, summarize older context
- **Selective Memory:** Keep specific entities (user name, preferences) explicitly; summarize the rest
- **External Memory Store:** Persist key facts to a DB/vector store; retrieve relevant ones per turn

### Implementation Decisions

| Question | Default |
|---|---|
| What's the max conversation length you'll support? | Plan for at least 50 turns |
| What must NEVER be forgotten? | User identity, explicit preferences, in-flight task state |
| What can be summarized? | Casual context, exploratory chat |
| Do you need turn-by-turn replay later? | If yes, store full history externally + use compressed memory in prompt |

---

## Part 2: Multimodal Models

Adding vision (or audio, video) to an LLM workflow. Three core models drive
modern multimodal applications.

### ViT (Vision Transformer)

Adapts the Transformer architecture for images by converting them into
**patches of pixels** rather than text tokens.

```
Image (224×224 pixels)
       ↓
Split into 16×16 pixel patches → 196 patches
       ↓
Flatten + project each patch into an embedding (like a token)
       ↓
Standard Transformer encoder
       ↓
Image representation
```

**Use case:** Image classification, image embeddings, building blocks for
larger multimodal systems.

### CLIP (Contrastive Language-Image Pre-training)

Computes embeddings for **both images and text in the same vector space**.
Trained with contrastive learning on image-caption pairs.

| Capability | How it works |
|---|---|
| **Zero-shot image classification** | Compare image embedding to text embeddings of candidate labels; pick closest |
| **Image search by text query** | Embed the query text, find images with closest embeddings |
| **Text search by image query** | Embed the image, find captions with closest embeddings |
| **Image-text similarity scoring** | Direct cosine similarity in shared space |

**Game-changer:** No labeled training data needed for new categories. The
shared vector space handles open-ended classification.

### BLIP-2 (Bootstrapping Language-Image Pre-training)

Connects a frozen ViT to a frozen LLM via a small trainable component (Q-Former).

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Frozen    │     │   Trainable  │     │    Frozen   │
│   Vision    │ ──→ │   Q-Former   │ ──→ │     LLM     │
│ Transformer │     │              │     │             │
│   (ViT)     │     │ (32 queries  │     │  (e.g.GPT)  │
│             │     │  → soft      │     │             │
│             │     │   prompts)   │     │             │
└─────────────┘     └──────────────┘     └─────────────┘
```

**Why this matters:** Training a multimodal model from scratch costs millions.
BLIP-2 lets you compose existing vision and language models with a small
trainable bridge. Result: image captioning, visual Q&A, multimodal chat with
~100x less training cost.

### Multimodal Choice Matrix

| Use case | Use this | Don't use this |
|---|---|---|
| Image classification with custom labels | CLIP (zero-shot) | Train a new vision classifier (expensive) |
| Search images by text or vice versa | CLIP embeddings + vector store | Manual tagging |
| Image captioning, visual Q&A | BLIP-2 or GPT-4V/Claude vision | CLIP alone (it can't generate text) |
| Just embedding images for similarity | ViT or CLIP image encoder | Full BLIP-2 (overkill) |
| Production multimodal chat | Hosted multimodal API (GPT-4V, Claude vision, Gemini) | Self-host BLIP-2 unless you have specific reasons |

---

## Principles

- **Choose memory pattern based on what must persist.** Identity and preferences should never be summarized; casual context can be.
- **Plan memory architecture for the long-term conversation, not the demo.** A pattern that works for 5 turns can fail at 50.
- **Hybrid memory beats pure patterns in production.** Pure buffer hits token limits; pure summary loses specifics. Mix them.
- **Multimodal embeddings unlock zero-shot.** CLIP-style shared spaces eliminate the need for labeled training data on new categories.
- **Compose frozen models for cost efficiency.** BLIP-2's pattern (frozen ViT + frozen LLM + small trainable bridge) is a template — apply it elsewhere where end-to-end training is too expensive.

---

## Anti-Patterns to Avoid

### Full History Retention Without Limits

**Looks like:** ConversationBufferMemory in production with no fallback strategy.

**Why it fails:** Token limit exceeded after enough turns. Costs balloon. Latency grows.

**The fix:** Always pair buffer memory with a fallback (window or summary) that activates near the token limit.

### Static Window That Loses Critical Facts

**Looks like:** ConversationBufferWindowMemory with K=5 in a long-running customer support chat.

**Why it fails:** User said their account ID 10 turns ago; window has discarded it; agent now has to re-ask, frustrating the user.

**The fix:** Selective memory — extract critical entities (account ID, preferences) and persist them explicitly; window only the conversational context.

### Implicit Information Loss in Summarization

**Looks like:** Relying solely on summarized history; specific details (user said "I prefer X over Y") get smoothed away.

**Why it fails:** Agent loses ability to reference specifics. Recall feels vague.

**The fix:** Don't summarize away facts the user might reference later. Use structured memory for specifics + summary for context.

### Single-LLM Constraint for Memory + Generation

**Looks like:** Same LLM does the conversation generation AND the summarization.

**Why it fails:** You're paying generation-tier latency and cost for what could be a much cheaper summarization call.

**The fix:** Use a fast/cheap model (Haiku, GPT-3.5) for summarization; reserve the strong model for actual user-facing generation.

### CLIP for Tasks Requiring Generation

**Looks like:** Trying to use CLIP to caption images.

**Why it fails:** CLIP is an embedding model, not a generative one. It has no decoder.

**The fix:** Use BLIP-2, GPT-4V, or Claude vision for any task that requires generating text from images.

---

## Decision Rules

| Condition | Action |
|---|---|
| Short conversations (<10 turns), perfect recall needed | ConversationBufferMemory |
| Bounded conversations, recent context dominates | ConversationBufferWindowMemory |
| Long conversations, semantic recall over verbatim | ConversationSummaryMemory |
| Production chatbot, mixed needs | Hybrid: window + summary + selective entity extraction |
| Image classification with new/changing labels | CLIP zero-shot |
| Image-text similarity / search | CLIP embeddings + vector store |
| Image captioning, visual Q&A | BLIP-2 or hosted multimodal API |
| Just need image embeddings | ViT or CLIP image encoder |
| Memory-related summarization happening on every turn | Use cheap model for summary, strong model for generation |

---

## Worked Example: Customer Support Chatbot Memory Architecture

**Goal:** Multi-turn support chat that remembers user identity, account state, and recent context across a 30-minute session.

**Memory layers:**

| Layer | Pattern | Contents |
|---|---|---|
| **Persistent identity** | Selective extraction → DB | Name, email, account ID, plan tier |
| **Stated preferences** | Selective extraction → DB | "I prefer email over phone", language preference |
| **Recent context (last 10 turns)** | Buffer (verbatim) | Full Q&A flow |
| **Older context (turns 11+)** | Summary (cheap LLM) | Compressed gist of earlier discussion |
| **In-flight task state** | Structured memory | Active ticket ID, current step in workflow |

**Per-turn prompt construction:**

```
[System]: You are a support agent.

[Selective memory]:
  User: <name> (<account_id>, plan: <plan>)
  Preferences: <stated preferences>
  Active task: <task_state>

[Summary of older context]:
  <auto-generated summary of turns 11+>

[Recent context]:
  <last 10 turns verbatim>

[User]: <new message>
```

**Lesson:** No single memory pattern solves production needs. Layered hybrid
memory is the production reality.

---

## Worked Example: Adding Image Search to a Product Catalog

**Goal:** Let users find products by uploading a photo or by searching with text.

| Step | Action | Tool |
|---|---|---|
| 1 | Embed all product images | CLIP image encoder, store vectors in pgvector / Pinecone |
| 2 | User uploads a photo | Embed via CLIP image encoder |
| 3 | Find K nearest neighbors in product image embedding space | Vector similarity search |
| 4 | User searches with text "blue running shoes" | Embed text via CLIP text encoder |
| 5 | Search same vector space (text and image embeddings co-exist) | Same similarity search |
| 6 | Display top results | Standard product UI |

**No labeled training needed.** CLIP's pretrained shared space handles zero-shot
classification on whatever products you have.

---

## Gotchas

- **ConversationSummaryMemory adds latency on every turn.** The summarization call is sequential to the generation call. Budget for it.
- **CLIP doesn't generalize well to specialized domains.** Out-of-the-box CLIP is great for general images; medical imaging or industrial inspection often needs domain-adapted CLIP variants (e.g., MedCLIP).
- **Q-Former training cost is non-trivial for BLIP-2 customization.** "Small bridge" is relative — still meaningful compute. Use pretrained BLIP-2 unless you have specific domain reasons to retrain.
- **Memory token cost compounds.** A 50-turn conversation with 200-token avg responses + buffer memory = 10,000+ tokens per turn by the end. Active monitoring needed.
- **Multimodal hosted APIs (GPT-4V, Claude vision, Gemini) are usually the right starting point.** Self-hosting BLIP-2 makes sense at scale or for privacy; not for prototyping.

Source: *Hands-On Large Language Models* by Jay Alammar and Maarten Grootendorst, conversational memory and multimodal chapters.
