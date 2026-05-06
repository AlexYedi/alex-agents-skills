# Playbook 06 — Retrieval Architecture

Chain for designing retrieval over your data — RAG, knowledge graph, semantic search, or text-to-SQL. Triggered automatically by phrases like "build RAG", "knowledge graph", "semantic search", "vector search" (UserPromptSubmit hook).

## When to Use

- "Build a RAG system over [our docs]"
- "Set up a knowledge graph for [domain]"
- "Semantic search across [content]"
- "Chat over our [data / wiki / Slack / code]"
- "Text-to-SQL on [warehouse]"

## When to Skip

- You're tweaking one chunk-size parameter — go direct to `retrieval/rag-architect`
- You only need to learn how RAG works conceptually — read the tutorials in `retrieval/tutorials/`
- The use case is structured-data Q&A and you've already chosen text-to-SQL — go to `retrieval/text-to-sql`

## Sequence

| Step | Skill / reference | Output |
|---|---|---|
| 1 | **Always start here:** `references/structured-vs-unstructured-retrieval.md` | KG vs RAG vs text-to-SQL decision with explicit reasoning. Most production systems use a combination — this aid helps pick the *primary* paradigm |
| 2 | **Branch on chosen paradigm:** | |
|   | → KG path | step 3a |
|   | → RAG path | step 3b |
|   | → Structured-data path | step 3c |
|   | → Hybrid (most production systems) | KG for metadata + governance, RAG for content; do both branches with handoffs |
| 3a | `retrieval/knowledge-graph-modeling` → `retrieval/knowledge-graph-applications` → `retrieval/knowledge-graph-platform-integration` | Property graph vs RDF, applications (identity res / fraud / dependency), platform integration (ETL, Spark, Kafka, GDS) |
| 3b | `retrieval/rag-architect` | Pipeline design, chunking, embedding model, retrieval strategy, evaluation |
| 3c | `retrieval/text-to-sql` | NL → SQL with prompting + RAG over schema |
| 4 | Optional learning: `retrieval/tutorials/retrieval_augmented_generation/`, `retrieval/tutorials/contextual-embeddings/` | Hands-on technique tutorials before scaling to prod |

## Cross-folder pointers (typically needed)

- `Software Development/rag-and-agent-architecture` — agent-level retrieval patterns (multi-step, tool use, planner-executor)
- `Software Development/embedding-models-and-domain-adaptation` — choosing/fine-tuning embedding models for your domain
- `Software Development/llm-conversation-memory-and-multimodal` — when retrieval feeds a conversational agent
- `Software Development/ai-evaluation-methodology` — how to evaluate retrieval quality

## Decision Points

- **KG vs RAG** (step 1): graph-shaped queries (multi-hop, identity res, dependencies) → KG. Document-shaped queries (semantic Q&A) → RAG. Read the decision aid for the full matrix.
- **Hybrid?** (step 2): if you have both governance/lineage requirements AND open-ended Q&A, you'll end up hybrid. Don't fight it — design for it.
- **Open-source embeddings vs API** (step 3b): API for speed-of-iteration (OpenAI, Cohere); self-host once volume + privacy demands it.
- **Re-ranking?** (step 3b): adds significant precision at moderate cost. Worth it for production but skip for prototypes.

## References

- `references/structured-vs-unstructured-retrieval.md` — the decision aid (always step 1)
- `references/Knowledge_Graph/complete-distillation.md` — Barrasa & Webber book digest
- `retrieval/rag-architect/references/` — RAG-specific deep references

## Bypass Phrases

To skip the playbook when the hook fires: *"Just need a chunking heuristic"* / *"Already chose RAG — go straight to rag-architect"* / *"Skip the decision aid"*.
