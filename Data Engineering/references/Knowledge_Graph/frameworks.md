# Knowledge Graphs — Frameworks Catalog

## Index (Alphabetical)

| Name | Domain |
|---|---|
| APOC | Tooling |
| Apache Hop | ETL |
| Apache Spark Connector | Integration |
| Bidirectional Annotation | NL Generation |
| Blocking Keys | Entity Resolution |
| Composite Databases (Federation) | Modeling |
| Connected Components (WCC) | Algorithms |
| Cypher | Query |
| Data Fabric (with Dremio/Denodo) | Integration |
| Data Virtualization | Integration |
| Dependency Chains | Applications |
| Document Similarity | Applications |
| Embeddings (FastRP, Node2Vec, GraphSAGE) | ML |
| Entity-Based Search | Applications |
| Entity Resolution (3-stage) | Applications |
| Expertise Knowledge Graph | Applications |
| Fraud Rings | Applications |
| Graph Data Science (GDS) | Algorithms |
| Graph Federation | Modeling |
| GraphQL with @relationship | API |
| In-graph ML Pipelines | ML |
| Just-Enough-Semantics | Modeling |
| Kafka Connect (Neo4j Streams) | Integration |
| Knowledge Lake | Architecture |
| Labeled Property Graph Model | Modeling |
| Leacock-Chodorow Similarity | NL |
| Least Common Subsumer | NL |
| Lexical Database (WordNet) | NL |
| LOAD CSV | Loading |
| Materialized Similarities | Applications |
| Metadata Knowledge Graph Hub | Architecture |
| Natural Language Generation | NL |
| Natural Language Query Interface | NL |
| neo4j-admin import | Loading |
| Node Similarity | Algorithms |
| Ontology | Modeling |
| Organizing Principle | Modeling |
| Plain Old Graph | Modeling |
| Property Graph Model | Modeling |
| Redundant Dependencies | Applications |
| Root Cause Analysis (graph) | Applications |
| Schema.org | Standards |
| SIMILAR Relationship | Algorithms |
| Single Point of Failure (SPOF) | Applications |
| Skills Knowledge Graph | Applications |
| SNOMED CT | Standards |
| Strong vs Weak Identifiers | Identity |
| Subject-Predicate-Object | NL |
| Taxonomy | Modeling |
| User-defined Procedures (UDFs) | Tooling |

## Detailed Catalog

### Plain Old Graph
**Structure:** Nodes + edges, no organizing principle.
**When:** Pre-prototype only; not for production.

### Property Graph Model
**Structure:** Nodes + typed/directed relationships + key-value properties.
**Tools:** Neo4j, JanusGraph, TigerGraph, Memgraph.
**When:** Default for most knowledge graphs.

### Labeled Property Graph Model (LPGM)
**Structure:** Property graph + labels (tags) on nodes.
**Caveat:** Labels are tags, not classes. No inheritance.

### Taxonomy
**Structure:** Hierarchical classification (broader/narrower).
**Standards:** SKOS.

### Ontology
**Structure:** Beyond hierarchy — `IS_A`, `PART_OF`, `COMPATIBLE_WITH`, etc.
**Standards:** OWL, RDFS, Schema.org, FIBO, SNOMED CT.

### Schema.org / SNOMED CT / FIBO
**Schema.org:** General web concepts.
**SNOMED CT:** Medical terminology.
**FIBO:** Financial terminology.

### Just-Enough-Semantics
**Principle:** Add semantic metadata only as use cases require.

### Composite Databases (Federation)
**Origin:** Neo4j 5+ Enterprise.
**Structure:** Virtual database integrating multiple physical graph sources.

### Data Virtualization
**Tooling:** APOC virtual nodes; Dremio / Denodo for broader fabric.

### LOAD CSV / neo4j-admin import / Data Importer
**LOAD CSV:** Online; incremental.
**neo4j-admin import:** Offline; bulk bootstrap.
**Data Importer:** Visual modeling tool.

### APOC
**Structure:** Apache Commons-style extensions for Neo4j.
**Examples:** `apoc.load.json`, `apoc.periodic.iterate`, virtual nodes.

### User-Defined Procedures (UDFs)
**Structure:** JVM (Java/Scala) procedures annotated with `@Procedure`.
**Discipline:** Test independently; standard build practices.

### Kafka Connect (Neo4j Streams)
**Source:** KG → Kafka events.
**Sink:** Kafka → KG via Cypher.

### Apache Spark Connector
**Read/write:** KG as DataFrame source/sink.
**When:** Distributed preprocessing.

### GraphQL with @relationship
**Tooling:** Neo4j GraphQL Library.
**Behavior:** Type-safe schema; auto-translates to Cypher.

### Apache Hop
**Type:** Low-code ETL with KG-native node/relationship mapping.

### Graph Data Science (GDS)
**Lifecycle:** Project → Execute → Inspect → Write.
**Categories:** Centrality, Community Detection, Similarity, Path Finding, Connectivity, Embeddings.

### Connected Components (WCC)
**Use:** Identity resolution; cluster detection.

### Node Similarity / SIMILAR Relationship
**Use:** Fuzzy matching of weak identifiers.

### Embeddings (FastRP, Node2Vec, GraphSAGE)
**Use:** Vector representations for ML on graphs.

### In-graph ML Pipelines
**Lifecycle:** Extract features → Train → Predict → Iterate.

### Entity Resolution (3-stage)
**Stages:** Data prep → Matching (strong/weak rules with blocking) → Curation (WCC).
**Tools:** Zingg, Splink, Neo4j GDS.

### Blocking Keys
**Purpose:** Avoid O(n²) comparisons in entity resolution.
**Examples:** prefix-of-name, hashed-zip, year-of-birth.

### Strong vs Weak Identifiers
**Strong:** Stable, globally unique (email, SSN, master ID).
**Weak:** Volatile / shared (cookie, IP, name).

### Fraud Rings
**Pattern:** Multiple synthetic identities sharing attributes.
**Detection:** Multi-attribute clustering with thresholds.

### Legitimate Households (Negative Control)
**Pattern:** 2 Person + 1 Address + 1 Phone — normal.
**Use:** Filter from fraud-ring detection.

### Org Charts / Expertise / Skills KGs
**Org:** REPORTS_TO hierarchy.
**Expertise:** Derived from collaboration platforms (Slack/Teams).
**Skills:** Project participation + dependencies.

### Dependency Chains / Multidependencies / Redundant / SPOF
**Chains:** Recursive traversal.
**Multi:** Weighted contributions to threshold.
**Redundant:** Backup paths; failure absorbed.
**SPOF:** Convergence on single node.

### Root Cause Analysis (graph-based)
**Approach:** Cluster failed nodes; find common ancestors.

### Entity-Based Search
**Pattern:** NER → entity nodes → ontology disambiguation.
**Vs keyword:** Search "Apple Inc." not text "apple".

### Document Similarity
**Approach:** Weighted shared entities × salience scores.
**Strategies:** On-the-fly query / Materialized SIMILAR_TO.

### Materialized Similarities
**Trade:** Speed vs freshness.

### Natural Language Query Interface
**Approaches:** Rule-based (spaCy patterns) / LLM-to-Cypher (with schema in prompt).

### Natural Language Generation
**Pattern:** Subject-Predicate-Object from graph triples.
**Annotation:** Bidirectional natural-language expressions.
**Schema independence:** Use named properties, not internal names.

### Subject-Predicate-Object
**Modeling:** Nouns in nodes, verbs in relationships, attributes in properties.

### Lexical Database Integration (WordNet)
**Use:** Semantic similarity, polysemy analysis.

### Leacock-Chodorow Similarity
**Approach:** Depth-aware similarity using taxonomy depth.

### Least Common Subsumer
**Approach:** Most specific shared ancestor as proximity measure.

### Knowledge Lake Architecture
**Stage:** Foundational, general-purpose KG subsuming other KGs and non-graph data.
**When:** Mature data org; multi-graph environment.

### Metadata Knowledge Graph Hub
**Use:** Enterprise lineage + impact analysis + catalog search.
**Tools:** DataHub + Neo4j integration.

### Data Fabric (Dremio/Denodo + KG)
**Pattern:** Virtualization platforms + KG as master semantic layer.

### Cypher
**The language:** Pattern-matching declarative graph query.

## Cross-Reference Map

```
                  PLAIN OLD GRAPH
                       │
                       ▼ (add organizing principle)
                  PROPERTY GRAPH ──► LABELED PROPERTY GRAPH
                       │
                       ▼
                  ORGANIZING PRINCIPLES
                  ┌─────────────┐
                  │             │
              TAXONOMY      ONTOLOGY
              (SKOS)        (OWL, Schema.org,
                             FIBO, SNOMED CT)
                       │
                       ▼ (federation)
              COMPOSITE DATABASES
              DATA VIRTUALIZATION
              KNOWLEDGE LAKE


              LOADING                 INTEGRATION                ALGORITHMS
              ───────                 ───────────                ───────────
              LOAD CSV                Kafka Connect              GDS Library
              neo4j-admin import      Spark Connector            - Centrality
              Data Importer           GraphQL                    - Community
              APOC                    UDFs                       - Similarity
                                      Apache Hop                 - Path Finding
                                                                 - WCC
                                                                 - Embeddings
              APPLICATIONS                              NL & SEARCH
              ────────────                              ───────────
              Identity Resolution (WCC + SIMILAR)       Entity-Based Search
              Fraud Detection (rings, controls)         Document Similarity
              Org Charts + Expertise + Skills           NL Query → Cypher
              Dependency Analysis (chains, SPOF, RCA)   NL Generation (S-P-O)
              Entity Resolution (3-stage)               WordNet integration
              Metadata KG Hub                           Leacock-Chodorow
              Data Fabric                               Least Common Subsumer
```

Source: *Knowledge Graphs* (Barrasa & Webber, O'Reilly, 2023).
