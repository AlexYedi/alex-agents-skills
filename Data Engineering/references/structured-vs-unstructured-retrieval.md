# Structured (Knowledge Graph) vs Unstructured (RAG) Retrieval

A one-page decision aid for choosing between knowledge-graph and RAG-based retrieval for a given problem. Read this *before* committing to one of the `retrieval/` skills.

## The Question in One Sentence

**Are you retrieving facts about explicit relationships between entities (KG), or passages that semantically answer a question (RAG)?**

Most real systems eventually use both. This guide is for picking the right *primary* paradigm and knowing when to add the other.

## Quick Decision Matrix

| Your data is mostly... | Your queries are mostly... | Start with |
|---|---|---|
| Structured rows + relationships | "Who is connected to X via Y?" / multi-hop joins | **Knowledge Graph** |
| Documents, articles, chats, code | "What does the system say about X?" / semantic Q&A | **RAG** |
| Mixed, but governance/lineage matters | "Which records came from which source under which contract?" | **Knowledge Graph** (metadata graph) |
| Mixed, but freshness and recall matter | "Find anything relevant to X across all our docs" | **RAG** |
| Highly typed entities with hard rules | Compliance, fraud, identity resolution | **Knowledge Graph** |
| Highly variable text, no fixed schema | Customer support, internal Q&A, code search | **RAG** |

## When KG Wins

- **Multi-hop reasoning** — "find people connected to a sanctioned entity through ≤ 3 ownership steps." RAG can't traverse; KG can.
- **Identity resolution** — merging records across systems where strong/weak identifiers and confidence rules matter.
- **Dependency analysis** — service graphs, supply chains, org charts, root-cause traversal.
- **Fraud detection** — fraud rings, legitimate-vs-suspicious household structures.
- **Hard governance** — every fact must trace to a typed source with a contract; metadata-as-a-graph.
- **Symbolic constraints** — type checking, ontology validation, "this can't happen by definition" rules.

When the answer requires *graph traversal logic*, KG wins. When the answer requires *finding relevant text*, KG is the wrong tool.

## When RAG Wins

- **Open-ended question answering** over a corpus of documents.
- **Semantic search** — "find passages that talk about X-like things," even when X never appears verbatim.
- **Long-tail facts** — content that's expensive to extract into a schema and rarely queried in the same shape.
- **Fast iteration** — adding a new document is one ingestion step; adding a new entity type to a KG is a schema change.
- **Cross-domain corpora** — internal wiki + Slack + code + tickets; getting these into one ontology is months of work, embeddings work in days.

When the answer is "the sentence in the doc that says it," RAG wins. When the answer requires reasoning *about* what those sentences imply, you need more than RAG.

## When You Need Both

Most production systems converge here:

- **KG-backed RAG** — use the KG to filter or rerank retrieved chunks ("only show me chunks from documents authored by people in this org subgraph"). Improves precision.
- **RAG-extracted KG** — extract entities + relationships from documents via an LLM, populate a graph, query it. Cheaper than hand-building an ontology, less precise than a curated graph.
- **Hybrid query routing** — classify the query: graph-shaped → KG; semantic → RAG; both → fan out and merge.
- **Metadata graph + vector index** — KG holds lineage, ACLs, contracts; vector index holds the content. Retrieval consults both.

## Common Anti-Patterns

- **Building a KG to do semantic search.** If the query is "find docs about X," vectors are 10× cheaper and faster.
- **RAG-ing structured data.** If your data is in a relational schema and queries are joins, write SQL or use a KG. Text-to-SQL (`retrieval/text-to-sql`) sits here.
- **One giant KG ontology before any retrieval works.** Start narrow — one entity type, one relationship type, one query — and grow.
- **One giant embedding index over everything.** Without metadata filtering, recall stays high but precision collapses at scale.

## Skill Pointers

| If you chose... | Go to |
|---|---|
| Knowledge Graph (modeling) | `retrieval/knowledge-graph-modeling/` |
| Knowledge Graph (applications: identity, fraud, dependency) | `retrieval/knowledge-graph-applications/` |
| Knowledge Graph (wiring into the platform: ETL, Spark, Kafka, GDS) | `retrieval/knowledge-graph-platform-integration/` |
| RAG (architecture, chunking, retrieval evaluation) | `retrieval/rag-architect/` |
| RAG (foundational tutorials) | `retrieval/tutorials/retrieval_augmented_generation/`, `retrieval/tutorials/contextual-embeddings/` |
| Natural language → SQL over a relational warehouse | `retrieval/text-to-sql/` |
| Both — metadata graph + vector index | Start with `retrieval/knowledge-graph-modeling` (governance frame), then layer `retrieval/rag-architect` on top |

## Heuristic Summary

- Graph-shaped queries → KG
- Document-shaped queries → RAG
- Structured tables + natural language → text-to-SQL
- Mixed at scale → both, with the KG as the metadata/governance layer and RAG as the content layer
