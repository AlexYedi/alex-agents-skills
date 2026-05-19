---
name: rag-and-agent-architecture
description: >
  Architect production RAG systems and AI agents. Use when building a RAG
  pipeline (retrieval strategy, chunking, hybrid search, reranking), designing
  an agent (tool selection, planning, reflection, error correction), choosing
  between RAG and agents and full-context for a use case, or debugging a RAG
  system that retrieves wrong context. Triggers: "design a RAG pipeline",
  "build an agent that does X", "ReAct vs Reflexion", "hybrid search vs vector
  search", "agent planning strategy", "why does my RAG retrieve wrong context?",
  "tool inventory for an agent". Produces concrete architecture covering
  retrieval mechanism, agent loop pattern, tool design, and validation gates.
---

# RAG and Agent Architecture

You design production-grade retrieval-augmented and agentic systems. Both
patterns address the same root problem (model needs information or capability
beyond its weights) but with different tradeoffs.

This skill operationalizes Chip Huyen's RAG and Agent design patterns into
concrete architectural decisions.

---

## When to Use This Skill

- Building a RAG pipeline and choosing retrieval mechanism, chunking, reranking
- Designing an AI agent and picking the loop pattern (ReAct, Reflexion, plan-and-execute)
- Choosing between RAG, agents, and full-context approaches for a use case
- Debugging a RAG system retrieving wrong context
- Designing a tool inventory for an agent (read vs write, scope, validation)

---

## RAG vs Agents vs Full Context: The Architectural Choice

| Pattern | Mechanism | Best for | When to avoid |
|---|---|---|---|
| **Full Context** | Stuff all relevant info into the prompt | Small knowledge sets, simple queries | Knowledge exceeds context window or is dynamic |
| **RAG** | Retrieve relevant info from external store at query time | Large/dynamic knowledge bases, knowledge-intensive Q&A | Tasks needing iterative reasoning or external action |
| **Agents** | Use tools (search, APIs, code execution) to gather info and act | Multi-step reasoning, tasks requiring external action | Simple lookup tasks (overkill, more failure modes) |

### Decision Flow

```
Does the model need external information OR external action?
├── Information only, fixed knowledge fits in context → Full Context
├── Information only, large/dynamic knowledge → RAG
└── Information + actions in the world → Agents
```

---

## RAG Architecture

A production RAG pipeline has 4 components. Get any of them wrong and the
output quality collapses.

```
┌─────────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   1. INGEST     │→│ 2. RETRIEVE  │→│ 3. RERANK    │→│ 4. GENERATE  │
│   chunk + embed │  │ candidates   │  │ refine top-k │  │ with context │
└─────────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

### 1. Ingest: Chunking + Embedding

| Decision | Options | Default |
|---|---|---|
| **Chunk size** | 256-2048 tokens | Start at 512; tune based on retrieval quality |
| **Chunk overlap** | 0-20% | Use 10-15% overlap to preserve context across boundaries |
| **Embedding model** | OpenAI ada-002, voyage, cohere, custom | Match embedding model to retrieval task; multilingual matters if your data is |
| **Contextual augmentation** | Plain chunk vs chunk-with-context | Augment each chunk with doc title/summary for better retrieval |

### 2. Retrieve: The Mechanism Choice

| Mechanism | Strength | Weakness |
|---|---|---|
| **Term-based (BM25, keyword)** | Exact term matching, fast, cheap | Misses semantic meaning |
| **Vector (embedding similarity)** | Semantic understanding, paraphrase tolerance | Misses exact term matches; expensive |
| **Hybrid Search** | Combines both | More complex; need to tune weights |

**Recommendation:** Hybrid search by default. Use term-based for the cheap first-pass
candidate retrieval, vector for reranking the top candidates. Get the best of both.

### 3. Rerank: The Quality Gate

A reranker (typically a cross-encoder) refines the top-k candidates from the
retriever. It's slower but more accurate than the first-pass retrieval.

**Why it matters:** Retrieval recall@100 might be high, but the LLM only sees top-k=5.
A good reranker improves precision@5 dramatically.

**When to skip:** If retrieval precision@5 is already strong (rare), reranking adds latency without benefit.

### 4. Generate: Context Construction

- Order matters: NIAH studies show models attend better to start and end of context. Put critical info there.
- De-duplicate retrieved chunks; redundancy wastes context budget
- Cite sources in the response — improves trust and enables verification

### Multimodal RAG

For non-text data (images, video, audio), use multimodal embeddings (CLIP,
ImageBind). Retrieval works the same way; generation pipeline must accept
multimodal context.

---

## Agent Architecture

An agent has two parts: an environment it operates in, and a set of actions
(tools) it can perform.

### Agent Loop Patterns

| Pattern | Loop | Best for |
|---|---|---|
| **ReAct** (Reason + Act) | Think → Act → Observe → Repeat | General agent tasks; foundational pattern (Yao et al. 2022) |
| **Reflexion** | ReAct + explicit Evaluator + Self-Reflection module | Complex tasks where errors need correction (Shinn et al. 2023) |
| **Plan-and-Execute** | Generate plan upfront → Validate plan → Execute step-by-step | Tasks where wrong moves are costly; benefit from upfront verification |

### Tool Inventory Design

The most important agent design decision after the loop pattern.

| Principle | Why |
|---|---|
| **Few high-leverage tools beat many narrow tools** | More tools = harder selection, more context bloat, more failure modes |
| **Distinguish read (perception) vs write (action)** | Read tools are safe to expose broadly; write tools need validation gates |
| **Group related operations into one tool with parameters** | Better than 5 separate tools (e.g., `query_crm(operation, params)` vs 5 CRM tools) |
| **Document tool contracts strictly** | Agents fail when tool docs are ambiguous; treat tool docs as part of the prompt |

### Read vs Write Action Categorization

```
Read actions (perception): web search, retrieve, query DB, get user data
  → low risk; expose broadly

Write actions (modification): send email, update CRM, deploy code, charge card
  → high risk; require validation, approval gates, or human-in-loop
```

### Planning + Validation

For complex tasks:

1. **Decompose** the user task into subtasks (intent classification)
2. **Plan**: generate a plan as structured output (JSON list of steps with dependencies)
3. **Validate** the plan before execution: does it use only available tools? Are inputs reasonable? Does sequence make sense?
4. **Execute** validated steps one at a time
5. **Reflect** after each step: did it succeed? Update plan if needed.

---

## Principles

- **Evaluate retrieval solutions on multiple axes.** Hybrid search vs vector, scalability, indexing speed, query latency, and pricing structure all matter.
- **Augment context with all available signals.** Internal docs, user history, time/date, source documents, search results — combine for better generation.
- **Manage tool inventory ruthlessly.** Capability vs context-bloat is a real tradeoff. More tools = more failures.
- **Distinguish read vs write actions.** Categorize on creation; security depends on it.
- **Implement planning and validation for complex tasks.** Decompose → generate plan → validate → execute. Don't let agents free-range on multi-step tasks.
- **Apply reflection at multiple stages.** Initial plan, after each step, post-execution. Errors caught early are cheap; errors caught late are catastrophic.
- **Watch for runaway loops.** Agents can loop indefinitely. Cap iterations; require progress signal between iterations.

---

## Anti-Patterns to Avoid

### Tool Bloat

**Looks like:** Exposing 30 tools to the agent because the underlying API has 30 endpoints.

**Why it fails:** Agent has to read all tool docs every turn; selection becomes unreliable; context bloats.

**The fix:** Aggregate. Five well-designed tools beat thirty narrow ones.

### Skipping Plan Validation

**Looks like:** Agent generates a plan and immediately executes step 1.

**Why it fails:** Bad plans waste tokens, time, and money. Plan validation is cheap; execution is expensive.

**The fix:** Always validate plans before execution. Reject plans referencing nonexistent tools, missing inputs, or implausible sequences.

### Treating Retrieval as a Solved Problem

**Looks like:** "We use vector search, RAG works."

**Why it fails:** Retrieval quality is the dominant lever in RAG output quality. A 20% retrieval improvement beats a 20% LLM upgrade.

**The fix:** Eval retrieval separately from generation. Track precision@5 and recall@100 over time.

### Letting Agents Loop Indefinitely

**Looks like:** Agent retries the same failing tool call ad nauseam.

**Why it fails:** Token costs compound; user waits forever; underlying issue not surfaced.

**The fix:** Cap iterations (e.g., 10). Require evidence of progress between iterations. Escalate after cap to a different strategy or human.

### Mixing Read and Write Tools Without Categorization

**Looks like:** Agent has equal access to "search prospect" and "send email" without different validation.

**Why it fails:** First wrong move sends a bad email. No undo.

**The fix:** Classify every tool. Read = expose broadly. Write = validation gate or human-in-loop.

---

## Decision Rules

| Condition | Action |
|---|---|
| Knowledge fits in context window, mostly stable | Full context (no RAG needed) |
| Large or dynamic knowledge, no actions needed | RAG |
| Multi-step task with external actions | Agent (start with ReAct) |
| Complex agent task where errors compound | Reflexion or Plan-and-Execute |
| Building first agent | ReAct + tight tool inventory |
| Retrieval misses obvious matches | Switch to hybrid search |
| Top-k retrieval looks fine but generation hallucinates | Add reranker |
| Many narrow tools | Consolidate to fewer parameterized tools |
| Agent has write tools | Add validation + approval gates |

---

## Worked Example: Customer Support RAG + Agent Hybrid

**Goal:** Auto-resolve tier-1 support tickets using product docs + customer history.

| Component | Choice | Rationale |
|---|---|---|
| **RAG over docs** | Hybrid search (BM25 + embeddings) + reranker | Product docs have technical terms (BM25 wins) AND need semantic match (embeddings win); reranker improves precision@5 |
| **Chunking** | 512 tokens, 15% overlap, augmented with section title | Standard sweet spot |
| **Customer context** | Direct retrieval from CRM, full context (no embeddings) | Customer profile fits in context; freshness > similarity |
| **Agent loop** | ReAct with 3 tools: `search_docs`, `get_customer_history`, `escalate_to_human` | Limited tool surface; clear escape hatch |
| **Iteration cap** | 5 turns | Beyond 5, escalate (something is wrong) |
| **Write actions** | Only `escalate_to_human` is a write; reading is unrestricted | Read/write categorization |
| **Validation** | Before responding to user, check response against guardrails (no PII, no policy violations) | Cheap final gate |

**Lesson:** RAG and agents compose. RAG retrieves; agent decides what to do
with what it retrieved. Categorizing read vs write keeps the agent safe.

---

## Gotchas

- **Chunking decisions are domain-specific.** Code chunks differently from prose; tables chunk differently from narrative. No universal default.
- **Embedding model choice ages.** Today's best embedding model is not tomorrow's. Plan for migrations.
- **Reranker latency is real.** Cross-encoder reranking adds 100-500ms. Budget for it.
- **NIAH performance varies wildly.** Test long-context retrieval explicitly; don't assume.
- **PEFT confusion.** PEFT (LoRA, adapters) is finetuning territory, not RAG. Don't mix the patterns.

Source: *AI Engineering: Building Applications with Foundation Models* by Chip Huyen, Chapters 6 (RAG and Agents) and 7 (Finetuning).
