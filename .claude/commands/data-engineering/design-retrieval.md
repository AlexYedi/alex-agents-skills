---
description: Walk the retrieval architecture chain — KG vs RAG vs text-to-SQL decision aid first, then branch into the chosen paradigm.
---

You are guiding a retrieval architecture decision using the chain documented at `Data Engineering/playbooks/06-retrieval-architecture.md`.

**Step 1 (always first):** Read and apply `Data Engineering/references/structured-vs-unstructured-retrieval.md` to choose between knowledge graph, RAG, and text-to-SQL based on:
- Whether queries are graph-shaped (multi-hop, identity res, dependency) → KG
- Whether queries are document-shaped (semantic Q&A) → RAG
- Whether queries are SQL-shaped over relational data → text-to-SQL
- Whether the system needs both (most production systems) → hybrid

**Step 2: Branch on chosen paradigm.**

If KG path:
- `Data Engineering/retrieval/knowledge-graph-modeling` — property graph vs RDF, ontology vs taxonomy
- `Data Engineering/retrieval/knowledge-graph-applications` — fraud, identity res, dependency analysis
- `Data Engineering/retrieval/knowledge-graph-platform-integration` — ETL, Spark, Kafka Connect, GDS

If RAG path:
- `Data Engineering/retrieval/rag-architect` — pipeline design, chunking, embedding, retrieval, evaluation
- Reference tutorials at `Data Engineering/retrieval/tutorials/retrieval_augmented_generation/` and `contextual-embeddings/`

If structured-data path:
- `Data Engineering/retrieval/text-to-sql`

If hybrid:
- Walk both KG and RAG branches, with KG handling metadata + governance and RAG handling content retrieval.

**Step 3 (cross-folder, often needed):**
- `Software Development/rag-and-agent-architecture` — agent-level retrieval patterns
- `Software Development/embedding-models-and-domain-adaptation` — model selection / fine-tuning
- `Software Development/ai-evaluation-methodology` — evaluating retrieval quality

For each step:
- State the decision and trade-offs from the named skill
- Capture the user's choice before advancing

Bypass: *"Already chose [KG / RAG / text-to-SQL] — skip the decision aid"* or *"Just need a chunking heuristic"*.

Reference the full playbook for the decision matrix and trade-offs:
**`Data Engineering/playbooks/06-retrieval-architecture.md`**
