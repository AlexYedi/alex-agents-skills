# Knowledge Graphs — Complete Distillation

## 1. Source Identification
- **Title:** Knowledge Graphs: Data in Context for Responsive Businesses
- **Authors:** Jesús Barrasa & Jim Webber
- **Publisher:** O'Reilly Media, 2023
- **Pages:** ~215 OCR'd
- **Distilled in this repo:** 2026-04-29
- **Skills produced:** 3

## 2. Executive Summary

Barrasa & Webber's contribution: **knowledge graphs need an organizing principle** (taxonomy or ontology) to be useful, and they're best applied to a recognizable set of patterns (identity resolution, fraud detection, dependency analysis, semantic search). The book is Neo4j-leaning but principles are model-agnostic. "Just-Enough-Semantics" is a recurring discipline — don't over-model.

## 3. The Big Takeaways

1. **Organizing principle is the contract.** Plain Old Graphs aren't useful at scale.
2. **Property Graph for practitioners; RDF for standards-mandated.**
3. **Just-Enough-Semantics.** Iterate; don't pre-build comprehensive ontologies.
4. **Adopt standards if they fit** (SNOMED CT, Schema.org, FIBO).
5. **Federate; don't merge** when multiple graphs exist.
6. **Working set in RAM** is non-negotiable for performance.
7. **Identity resolution = WCC + Node Similarity + blocking keys.**
8. **Fraud detection needs negative controls** (legitimate households).
9. **Org chart + expertise graph together** beats either alone.
10. **SPOF analysis surfaces hidden risks** invisible to flat dependency lists.
11. **Root cause = common-ancestor traversal** over failed-node clusters.
12. **Entity-based search > keyword search.**
13. **GDS algorithms run on projections, not live graphs.**
14. **GraphQL via Neo4j library** for type-safe application APIs.
15. **Knowledge Lake is a multi-year journey** — most companies don't reach it.

## 4. Skills Derived

| Skill | When |
|---|---|
| [`knowledge-graph-modeling`](../../knowledge-graph-modeling/SKILL.md) | Data model + organizing principle + loading |
| [`knowledge-graph-applications`](../../knowledge-graph-applications/SKILL.md) | Use cases: identity, fraud, dependencies, search, NL |
| [`knowledge-graph-platform-integration`](../../knowledge-graph-platform-integration/SKILL.md) | ETL, Kafka, Spark, GraphQL, GDS, ER, metadata KG |

## 5. Frameworks Index
See `frameworks.md`. 50+ items covering data models, organizing principles, loading, integration, algorithms, applications, NL/search.

## 6. Best Practices Index
See `additional-experts.md`. Topics: modeling discipline, loading strategies, application patterns, performance, integration, mindset shifts.

## 7. Decision Rules Consolidated

| Condition | Action |
|---|---|
| New graph project | Property graph (Neo4j default) |
| RDF/OWL required | Triple store |
| Need classification only | Taxonomy (SKOS) |
| Rich relationships | Ontology (OWL, Schema.org, FIBO, SNOMED CT) |
| Standard exists | Adopt; extend if needed |
| Initial bulk load (10M+) | `neo4j-admin import` |
| Incremental load | LOAD CSV |
| Streaming sync | Kafka Connect |
| Distributed preprocessing | Spark connector |
| Application-facing API | GraphQL (Neo4j GraphQL library) |
| Need custom logic | UDF (Java/Scala, JVM); test independently |
| Run graph algorithm | GDS on projected subgraph |
| Need embeddings | GDS (FastRP / Node2Vec) |
| Multiple graphs | Composite Database (federation) |
| External data shouldn't be copied | Data virtualization (APOC virtual nodes) |
| Slow queries | Traverse structure first; properties last; index entry points |
| Identity fragmentation | WCC + Node Similarity + blocking keys |
| Fraud detection | Multi-attribute clustering + negative controls |
| "Who knows about X" | Expertise graph from collaboration data |
| SPOF analysis | Recursive dependency traversal + count threshold |
| Root cause | Common-ancestor traversal over failed-node clusters |
| Search over docs | Entity-based + disambiguation via Wikipedia/Wikidata |
| NL → Cypher | Rule-based for predictable; LLM-to-Cypher with schema for general |
| Knowledge Lake | Mature stage only; defer until multi-graph + multi-source pain |
| Metadata catalog | DataHub + Neo4j integration; OpenLineage from pipelines |

## 8. Anti-Patterns Consolidated

- Plain Old Graph in production
- Ontology-first without use case
- Custom ontology where standard exists
- Massive ingestion via LOAD CSV (use neo4j-admin import)
- One giant graph for unrelated domains
- Property-heavy traversals
- Index everything
- Identity resolution without negative controls
- Fraud detection on single attribute
- Dependency graph without versioning
- SPOF analysis as one-off
- Entity-based search without disambiguation
- NL-to-Cypher without schema awareness
- Document similarity by raw term overlap
- LOAD CSV for bulk bootstrap
- Streaming + sync confusion
- GraphQL with expensive resolver Cypher (N+1)
- GDS on live production graph
- UDFs without tests
- Entity resolution without blocking
- Metadata graph without update process

## 9. Worked Examples Pointer

| Example | Skill |
|---|---|
| E-commerce product knowledge graph | `knowledge-graph-modeling` |
| Synthetic identity fraud detection | `knowledge-graph-applications` |
| Entity resolution for B2B SaaS contacts | `knowledge-graph-platform-integration` |

## 10. Notable Content NOT in Skill Files

- **Cypher tutorial-level examples** — book has many; assumed prior Cypher familiarity in skills.
- **Specific Neo4j Browser usage** — visualization tooling, not skill-worthy.
- **Detailed APOC procedure listing** — refer to APOC docs.
- **Performance benchmarking comparing graph DBs** — vendor matrix.
- **History of graph databases** — context only.

## 11. Redundancy with Existing Repo Coverage

| Topic | Existing | Relationship |
|---|---|---|
| Knowledge graphs for metadata | `mdm-and-federated-data-governance` (Strengholt) | **Adjacent.** Strengholt covers KG as metalake; this book covers building KGs in general. |
| Semantic search | Possible overlap with AI engineering | **Different angle.** This book is graph-native; AI engineering is embedding-native. They compose. |
| Entity resolution | `mdm-and-federated-data-governance` mentions | **This book elaborates.** ER as graph-native workflow. |
| Data Fabric | `mdm-and-federated-data-governance` | **Adjacent.** Both treat fabric; this book emphasizes KG as semantic layer. |

**Net assessment:** No direct overlap. KG skills add a graph-native modeling and application layer.

## 12. Recommended Reading Order

For a developer starting with knowledge graphs:
1. `knowledge-graph-modeling` — data model and organizing principle
2. `additional-experts.md` — mindset and best practices
3. `knowledge-graph-applications` — recognizable use cases
4. `knowledge-graph-platform-integration` — wire it into the stack

For an architect designing graph-based systems:
1. `knowledge-graph-modeling`
2. `knowledge-graph-platform-integration`
3. Strengholt's `mdm-and-federated-data-governance` for metadata-graph context

For a data scientist using graph features in ML:
1. `knowledge-graph-platform-integration` (GDS section, embeddings)
2. `knowledge-graph-applications` (use cases)
3. `knowledge-graph-modeling` (referenceif modeling)

## 13. When to Invoke Which Skill

| User intent | Skill |
|---|---|
| "Model a knowledge graph" | `knowledge-graph-modeling` |
| "Property graph vs RDF" | `knowledge-graph-modeling` |
| "Taxonomy vs ontology" | `knowledge-graph-modeling` |
| "Load data into Neo4j" | `knowledge-graph-modeling` |
| "Federate multiple graphs" | `knowledge-graph-modeling` |
| "Fraud detection with graphs" | `knowledge-graph-applications` |
| "SPOF analysis" / "root cause" | `knowledge-graph-applications` |
| "Identity resolution" | `knowledge-graph-applications` (algorithm) + `knowledge-graph-platform-integration` (workflow) |
| "Semantic search" | `knowledge-graph-applications` |
| "NL → Cypher" / "NL generation" | `knowledge-graph-applications` |
| "GraphQL on Neo4j" | `knowledge-graph-platform-integration` |
| "GDS algorithm" | `knowledge-graph-platform-integration` |
| "Spark + Neo4j" | `knowledge-graph-platform-integration` |
| "Kafka + Neo4j" | `knowledge-graph-platform-integration` |
| "Metadata knowledge graph" | `knowledge-graph-platform-integration` |

Source: *Knowledge Graphs* (Barrasa & Webber, O'Reilly, 2023), distilled 2026-04-29.
