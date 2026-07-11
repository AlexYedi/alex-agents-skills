---
name: "advanced-rag-retrieval"
description: "Use when a RAG system retrieves the wrong or incomplete context and you need to pick the right fix — advanced indexing (parent/child, multi-vector, splitting strategy), query transformations (rewrite, multi-query, step-back, HyDE, decomposition), routing across vector/SQL/graph backends, hybrid search with RRF, and retrieval post-processing. Reach for this to diagnose a specific retrieval failure and choose the matching technique."
---

# Advanced RAG Retrieval

Diagnostic reference for fixing RAG accuracy. Paraphrased from Roberto Infante, *AI Agents and Applications* (Manning), Ch. 8–10 — use the book's repo for runnable code. Complements [[rag-architect]] (pipeline design, chunking, embeddings, eval) and [[rag-and-agent-architecture]]; this skill is the **failure → technique** decision layer.

## Mental model

Naive RAG fails for three *separable* reasons: **vague questions, weak indexing, unfiltered retrieval.** The fix is an **ensemble**, not one trick. Every technique intervenes at one of two stages:

- **Ingestion / indexing** — splitting and embedding (fix *what can be found later*).
- **Q&A / retrieval** — query transformation, routing, post-filtering (fix *what actually reaches the LLM*).

Diagnose which stage owns the failure first, then pick from that column.

## The master decision table (start here)

| Symptom you observe | Technique to apply | Stage |
|---|---|---|
| Answer lives in a different backend than you searched (facts vs. records vs. relationships) | **Routing** (vector / SQL / graph) | Q&A |
| Question implies a filter ("under 20%", "in Brighton", a date range) | **Self-query** / **text-to-SQL** | Q&A |
| Retrieval misses because phrasing differs from the docs | **Rewrite-Retrieve-Read** / **multi-query** | Q&A |
| One phrasing under-covers; recall is spotty | **RAG fusion / RRF** | Q&A |
| Exact terms/codes/names not matching under embeddings | **Hybrid search** (dense + BM25) | Q&A |
| Too many weak chunks reach the LLM | **Similarity-score threshold** | Q&A |
| Must guarantee or forbid specific terms | **Keyword include/exclude** | Q&A |
| Stale content outranks fresh content | **Time-weighted retriever** | Q&A |
| Detailed hits are too narrow for a complete answer | **Step-back prompting** | Q&A |
| Question wording ≠ ideal-answer wording; dense retrieval underperforms | **HyDE** | Q&A |
| Context lost across chunk boundaries | **↑ overlap** or **parent/child indexing** | Ingestion |
| Corpus must serve both narrow and broad questions | **ParentDocumentRetriever** | Ingestion |
| Coarse-chunk embeddings are noisy/diluted | **MultiVectorRetriever** (summary / hypothetical-question embeddings) | Ingestion |
| Question is genuinely multi-part | **Decomposition** (single- or multi-step) | Q&A |

## Indexing-side techniques (Ch. 8)

**The two-layer chunk pattern** is the backbone: *synthesis chunks* (large, context-rich, fed to the LLM) + *retrieval chunks* (small/derived, whose embeddings only point back to a synthesis chunk).

- **ParentDocumentRetriever** — embed small child chunks, return the parent. Serves narrow + broad from the same docs. Cost: ~2× storage.
- **MultiVectorRetriever** — attach extra embeddings to a chunk: a generated **summary** (denser, cleaner match) or **hypothetical questions the chunk could answer** (aligns stored vectors to real user phrasing). Cost: one LLM call per chunk at index time.
- **Granular chunk expansion** — retrieve small, return a version stitched with neighboring chunks. Needs positional bookkeeping.
- **Splitting strategy** — structure-aware (`HTMLHeaderTextSplitter`, `MarkdownHeaderTextSplitter`) for well-structured docs; fixed-size (`RecursiveCharacterTextSplitter`, `TokenTextSplitter`) for prose; `SemanticChunker` for embedding-based breakpoints. Hierarchy → uneven sizes; fixed → mid-sentence cuts; semantic → extra cost. **Test sizes/overlaps empirically — no universal answer.**
- **Semi-structured & multimodal** — summarize tables/images with a (multimodal) LLM, embed the *summary*, keep the raw asset in a doc store, return the raw on a hit.

## Query-side techniques (Ch. 9)

All share one shape: **transform the question, keep the original for synthesis** (`RunnablePassthrough()` forwards the original).

- **Rewrite-Retrieve-Read** — clean a casually-worded question before retrieval.
- **Multi-query** — 3–5 phrasings → retrieve each → merge with RRF/dedup. Cost: N× retrieval.
- **Step-back** — generate a *more abstract* question for broader context; synthesize on detailed + abstract context. Needs a capable model.
- **HyDE** — LLM writes a *fake answer*; retrieve using its embedding (closer to real answer-chunks than the question). Retrieval-only, never shown to the user; can hallucinate off-target.
- **Decomposition** — single-step (independent sub-questions, parallel) or multi-step (dependent chain; LangChain has no built-in multi-step class — see LlamaIndex's `MultiStepQueryEngine`).

## Routing & post-processing (Ch. 10)

- **Routing** — an LLM classifies the question and dispatches to vector store (semantic), **text-to-SQL** (structured facts/aggregations), or **knowledge-graph / Cypher-SPARQL** (relationships). Give it few-shot examples + a fallback; **misrouting is silent** — trace it.
- **Self-querying** — infer a metadata filter from the NL question ("festivals in Newquay" → `venue=Newquay` + semantic search). Options: explicit `search_kwargs` filter, `SelfQueryRetriever.from_llm` (+ `AttributeInfo`, needs `lark`), or a typed function-call (`StructuredQuery` → `ChromaTranslator`).
- **Hybrid search** — dense (embeddings) + sparse (BM25), merged by **Reciprocal Rank Fusion (RRF)**: `Σ 1/(rank + k)` across ranked lists, then rerank. Caveat: LangChain's `BM25Retriever` is in-memory and doesn't scale to millions of docs.
- **Post-processing** — **similarity-score threshold** (`search_type="similarity_score_threshold"`, `score_threshold`), **keyword include/exclude** (filter in Python — no built-in), **time-weighting** (`TimeWeightedVectorStoreRetriever(decay_rate=...)`; `adjusted = similarity + (1 - decay_rate)**hours_passed`; store `last_accessed_at`).

## Text-to-SQL & KG-RAG gotchas

- Text-to-SQL: `create_sql_query_chain(llm, db)` + `QuerySQLDataBaseTool`; reduce hallucinated tables/columns with few-shot prompts embedding the `CREATE TABLE` schema + sample rows; **add a "clean-SQL" pass** to strip the markdown fences models wrap SQL in (they break execution).
- KG-RAG: NL → Cypher/SPARQL → graph DB → prose. Same skeleton, generator swapped for the retriever. Needs a high-accuracy model + curated few-shot examples.

## Map to the Empire State pipeline

Concrete builds over your Notion/Supabase corpus: (1) **parent/child indexing** — 500-char child chunks for precise recall ("exact quote on RAG cost at Ray Dev Day"), large parents returned for context; (2) **self-query over event metadata** (`event_name`, `date`, `venue`, `speaker`, `company`, `topic`) so "what did Anthropic folks say in June?" auto-infers filters; (3) **router** between a vector branch (transcripts/briefs) and a text-to-SQL branch (Content Drafts + outcomes / CRM export); (4) **time-weighted retrieval** so a funding round from last week outranks a similar note from six months ago. Always ground generation with the "answer only from context, else say you don't know" fence to kill fabricated quotes.

## Key APIs (verify against current LangChain docs)

`ParentDocumentRetriever(vectorstore, docstore, child_splitter, parent_splitter)` · `MultiVectorRetriever(vectorstore, byte_store)` · splitters from `langchain_text_splitters` · `SemanticChunker` (`langchain_experimental`) · `ChatOpenAI(...).with_structured_output(Model)` · `SelfQueryRetriever.from_llm(...)` (+ `lark`) · `create_sql_query_chain` + `QuerySQLDataBaseTool` · `as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.6})` · `TimeWeightedVectorStoreRetriever(decay_rate=...)`.

_Source: Infante, *AI Agents and Applications* (Manning), Ch. 8–10._
