---
name: knowledge-graph-platform-integration
description: >
  Integrate knowledge graphs with the data platform: ETL workflows, Kafka
  Connect (Neo4j Streams), Apache Spark connectors, GraphQL APIs,
  user-defined procedures (UDFs), Graph Data Science (GDS) algorithms,
  in-graph ML pipelines, entity resolution workflows (data prep + matching
  + curation via WCC), metadata knowledge graph hubs, and data fabric
  with virtualization platforms (Dremio, Denodo). Use when wiring a KG into
  the broader data platform, designing entity resolution, exposing the KG
  via GraphQL, building ML on graph features. Triggers: "Neo4j Spark
  connector", "Kafka Connect for Neo4j", "GraphQL API on Neo4j", "Graph
  Data Science", "entity resolution with WCC", "metadata knowledge graph",
  "data fabric for graphs". Produces an integration architecture.
---

# Knowledge Graph Platform Integration

You apply Barrasa & Webber's integration toolkit: how a knowledge graph
fits into the broader data platform via ETL, streaming, GraphQL, ML, and
entity resolution workflows.

---

## When to Use This Skill

- Integrating a KG with an existing data platform (DW, lake, streams)
- Designing entity resolution for master data
- Exposing the KG via GraphQL to applications
- Building ML pipelines that read/write graph data
- Adopting Graph Data Science (GDS) algorithms
- Building a metadata knowledge graph for the organization

---

## Integration Surface Area

```
                    [Knowledge Graph]
                          ▲
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        │                 │                 │
   [Ingestion]        [Compute]        [Serving]
        │                 │                 │
   - LOAD CSV         - GDS algorithms   - GraphQL API
   - neo4j-admin      - UDFs             - Cypher endpoints
     import           - In-graph ML      - Driver libraries
   - Kafka Connect      pipelines        - Bolt protocol
   - Spark connector  - Entity Resolution
   - ETL (Hop, NiFi,                    - Application embedding
     Airflow)
   - APOC virtualization
```

---

## ETL Workflow Orchestration

### Apache Hop (low-code/no-code)

Visual data integration. Map source fields → graph nodes/relationships. Handles availability, cleansing, indexing, schema validation.

**When:** Non-developer users; visual modeling preferred; graph-first integration.

### Airflow / Dagster / Prefect

Code-first orchestrators. Trigger Cypher queries / `apoc.periodic.iterate` calls; coordinate with other data platform jobs.

**When:** Complex pipelines; engineering team comfortable with Python/code.

### NiFi / Ab Initio (enterprise ETL)

Heavyweight enterprise tools with graph connectors. Common in regulated industries.

---

## Streaming Integration: Neo4j Streams (Kafka Connect)

```
[Source DB] ──CDC──► [Kafka Topic] ──[Neo4j Streams]──► [Knowledge Graph]
                                            │
                                            └──► [Kafka Topic] ◄── change feed from KG
```

### Sink (Kafka → Neo4j)

Periodically execute Cypher against incoming Kafka messages. Bulk insert / merge.

```cypher
// Configured per topic; Cypher executes per message batch
MERGE (c:Customer {id: event.id})
SET c.name = event.name, c.email = event.email
```

### Source (Neo4j → Kafka)

Periodically execute Cypher; emit results as Kafka events. Power downstream systems.

**When:** Near-real-time graph synchronization; integration with event-driven architecture.

---

## Apache Spark Connector

Treats KG as source or sink for distributed pipelines:

```python
# Read from Neo4j as DataFrame
df = spark.read.format("org.neo4j.spark.DataSource") \
    .option("query", "MATCH (p:Person) RETURN p.name AS name") \
    .load()

# Write to Neo4j
df.write.format("org.neo4j.spark.DataSource") \
    .option("labels", ":Person") \
    .save()
```

**When:** Large-scale data preprocessing; bulk node/relationship loading; integration with existing Spark jobs.

---

## GraphQL API Construction

Define schema with `@relationship` directive to expose KG topology:

```graphql
type Person {
  name: String
  knows: [Person!]! @relationship(type: "KNOWS", direction: OUT)
}
```

GraphQL queries automatically translate to Cypher. Strict schema guidance — clients see types, not raw graph.

**Tools:** Neo4j GraphQL Library (Node.js), Hasura, custom resolvers.

**When:** Application-facing API. Multiple clients with different shapes. Want type safety.

---

## User-Defined Procedures (UDFs)

Extensible Neo4j components in JVM languages (Java, Scala). Annotated with `@Procedure`, `@Description`. Access database via `@Context`.

```java
@Procedure(name = "myorg.calculateRiskScore")
@Description("Calculates risk score for a customer subgraph")
public Stream<RiskScore> calculateRiskScore(
    @Name("customerId") String customerId
) {
    // Custom logic with full DB access
}
```

**When:** Domain-specialized operations needing native performance. Reusable across multiple Cypher queries.

**Discipline:** Test independently of database. Standard version control. Build pipeline.

---

## Graph Data Science (GDS)

A library of graph algorithms running on **projected subgraphs** in memory.

### Four-Phase Lifecycle

```
1. PROJECT  ──►  Read subgraph into in-memory native graph
2. EXECUTE  ──►  Run algorithm in parallel
3. INSPECT  ──►  Stream results back to client (or to disk)
4. WRITE    ──►  Mutate or write properties back to underlying graph
```

### Algorithm Categories

| Category | Examples | Use |
|---|---|---|
| **Centrality** | PageRank, Betweenness, Closeness | Influence, importance, brokerage |
| **Community Detection** | Louvain, Label Propagation, Leiden | Cluster identification |
| **Similarity** | Node Similarity, K-NN | Find similar nodes |
| **Path Finding** | Shortest Path, A*, Yen's K-shortest | Routing |
| **Connectivity** | Weakly Connected Components, Strongly Connected | Identity resolution; structural analysis |
| **Embeddings** | FastRP, Node2Vec, GraphSAGE | Vector representations for ML |

### In-Graph ML Pipelines

```
1. EXTRACT FEATURES  ──►  Generate node/graph embeddings (FastRP, Node2Vec)
2. TRAIN              ──►  Train predictive model on embeddings + properties
3. PREDICT            ──►  Apply model; mutate relationships above confidence threshold
4. ITERATE            ──►  Periodically retrain; refresh predictions
```

**When:** Recommendation, link prediction, node classification on graph data.

---

## Entity Resolution — Three-Stage Workflow

```
1. DATA PREPARATION
   - Normalize / standardize
   - Harmonize formats
   - Tokenize names; remove noise
   
2. ENTITY MATCHING
   - Blocking keys (group candidates by similarity bucket)
   - Strong identifier rules (exact match)
   - Weak identifier rules (similarity > threshold)
   - Build SIMILAR / MATCHES relationships
   
3. CURATION
   - Run Weakly Connected Components (WCC) on match graph
   - Each component = one master entity
   - Persist as Master records
   - Maintain mapping: source entity → master entity
```

**Key tactics:**
- **Blocking keys** prevent O(n²) comparisons. Common: prefix-of-name, hashed-zip, etc.
- **Strong identifier rules** catch high-precision matches.
- **Weak identifier rules** catch the long tail (similarity-based).
- **WCC at the end** consolidates: same entity across all match types.

**Tools:** Neo4j GDS for WCC; custom procedures for matching logic; ER frameworks (Zingg, Splink).

---

## Metadata Knowledge Graph Hubs

Enterprise-wide mapping of:
- Datasets ↔ Tables ↔ Columns
- Pipelines ↔ Tasks ↔ Sinks
- Domains ↔ Catalogs ↔ Owners
- Lineage edges across all of the above

```
(:Dataset)-[:STORED_IN]->(:Table)-[:HAS_COLUMN]->(:Column)
(:Pipeline)-[:READS]->(:Dataset)
(:Pipeline)-[:WRITES]->(:Dataset)
(:Dataset)-[:OWNED_BY]->(:Domain)
```

**Use cases:**
- Lineage tracing for compliance / audit
- Impact analysis ("if I change column X, what breaks?")
- Catalog search across the entire data estate

**Tools:** DataHub (open-source) integrates with Neo4j; OpenMetadata; custom builds.

---

## Data Fabric with Virtualization Platforms

Knowledge graph as the **master source** for golden record creation, dedup, logical view design across multiple data sources.

```
[Multiple sources: SQL, NoSQL, files, APIs]
                  │
                  ▼
        [Data Virtualization: Dremio / Denodo]
        (single SQL/REST surface)
                  │
                  ▼
        [Knowledge Graph]
        (golden records, relationships, semantics)
                  │
                  ▼
        [Applications, BI, ML]
```

**When:** Heterogeneous source systems; need unified semantic layer; enterprise scale.

---

## Principles

- **Bulk load offline; sync online.** `neo4j-admin import` for bootstrap; LOAD CSV / Kafka / Spark for ongoing.
- **Test UDFs independently.** Don't tie test logic to a running database.
- **Graph algorithms run on projections, not the live graph.** Project, compute, write back.
- **GraphQL provides strict schema for clients.** Don't expose raw Cypher to applications.
- **Entity resolution needs blocking keys.** Otherwise O(n²) comparison kills performance.
- **WCC at the end of ER.** Consolidates across all match types.
- **Memory locality matters for graph algorithms.** Distributed scale-out is rarely worth the latency cost.

---

## Anti-Patterns

### LOAD CSV for Bulk Bootstrap

**Looks like:** Loading 50M nodes via LOAD CSV. Hours. Locks queries.

**Why it fails:** LOAD CSV is online; not optimized for bulk.

**The fix:** `neo4j-admin import` for initial load. LOAD CSV for incremental.

### Streaming + Sync Confusion

**Looks like:** Both Kafka Connect ingest + nightly full sync running. Conflicts. Stale data wins sometimes.

**Why it fails:** Two sources of truth for "what's in the graph."

**The fix:** One pattern per dataset. Streaming OR batch. Document.

### GraphQL With Resolvers Doing Expensive Cypher

**Looks like:** Each GraphQL resolver runs an unbounded Cypher query. N+1 patterns. Slow.

**Why it fails:** Per-resolver Cypher is the GraphQL N+1 problem.

**The fix:** Use Neo4j GraphQL library's `@cypher` directive (single query for nested fields). DataLoader patterns for batched fetches.

### GDS on Live Production Graph

**Looks like:** PageRank running directly on the production graph. Production queries blocked.

**Why it fails:** Algorithms are heavy. Live graph traffic suffers.

**The fix:** Project a subgraph; run; write back. Or run on a read replica.

### UDFs Without Tests

**Looks like:** Custom Java procedures developed against a live database. No unit tests.

**Why it fails:** Refactoring breaks silently. Production bugs.

**The fix:** Test UDFs independently with mocked transactions or test containers.

### Entity Resolution Without Blocking

**Looks like:** Comparing every Person to every other Person.

**Why it fails:** O(n²) — 1M people = 10^12 comparisons.

**The fix:** Blocking keys (e.g., first-3-letters-of-last-name + zip). Then compare within blocks.

### Metadata Graph Without Update Process

**Looks like:** DataHub + Neo4j integration set up once. Lineage drifts as pipelines change.

**Why it fails:** Stale lineage misleads.

**The fix:** Automated lineage emission from pipelines (OpenLineage). DataHub ingests automatically.

---

## Decision Rules

| Situation | Action |
|---|---|
| Initial bootstrap (10M+ nodes) | `neo4j-admin import` |
| Ongoing CDC | Kafka Connect with Neo4j Streams |
| Bulk preprocessing in Spark | Neo4j Spark Connector |
| Visual ETL workflow | Apache Hop |
| Code-first orchestration | Airflow / Dagster + Cypher / `apoc.periodic.iterate` |
| Application-facing API | GraphQL (Neo4j GraphQL library) |
| Need custom domain logic | UDF / procedure (Java/Scala, JVM) |
| Run graph algorithm | GDS, on a projected subgraph |
| Need embeddings for ML | GDS embeddings (FastRP / Node2Vec) |
| Train predictive model on graph | In-graph ML pipeline |
| Entity resolution | 3-stage: prep → match → WCC curation |
| Lineage / metadata | Metadata KG hub (DataHub + Neo4j) |
| Heterogeneous sources | Data fabric (Dremio / Denodo) + KG as master |
| Fed-up with Cypher complexity | Build domain-specific UDFs |
| GraphQL N+1 | Use `@cypher` directive; DataLoader |
| GDS overload | Run on projection or replica, not production |

---

## Worked Example: Entity Resolution for a B2B SaaS

**Context:** B2B SaaS. 10M+ contacts ingested from CRM, Marketing, Support, Billing. Need master Contact record per real person.

**Pipeline:**

| Step | Action |
|---|---|
| 1 | Ingest source contacts into staging graph: `(:RawContact:Source)` |
| 2 | Normalize: lowercase emails; strip phone formatting; standardize names |
| 3 | Blocking: `(:RawContact)-[:IN_BLOCK]->(:Block {key: <hash of first-3-of-name + email-domain>})` |
| 4 | Within blocks, run match rules: |
|    - Strong: exact email match → `:MATCHES` (high confidence) |
|    - Weak: name similarity > 0.85 + same domain → `:SIMILAR` (medium confidence) |
| 5 | Run WCC over the union of `:MATCHES` and `:SIMILAR` |
| 6 | Each component → one `(:MasterContact)` |
| 7 | Persist mapping: `(:RawContact)-[:RESOLVES_TO]->(:MasterContact)` |
| 8 | Schedule incremental ER for new ingests |

**Throughput:** ~1M new contacts/day; ER runs hourly.

**Result:** Marketing campaigns now hit master contacts (no duplicates). Support tickets across systems link to the right person. Sales sees full activity history per master.

**Lesson:** Entity resolution is graph-native. Combining strong + weak identifiers + WCC gives both precision and recall.

---

## Gotchas

- **Spark connector schema inference is imperfect.** Define schema explicitly when possible.
- **Kafka Connect with high-volume topics requires tuning** (batch size, parallel tasks).
- **GraphQL nested queries can multiply Cypher calls** if not configured carefully.
- **GDS license is Enterprise-only** for production use; Community has limits.
- **Embeddings drift with graph changes.** Plan retraining cadence.
- **WCC over noisy edges** produces giant components. Filter aggressively.
- **Metadata KG can lag** if lineage emission is unreliable. Validate periodically.
- **Data fabric introduces latency.** Cache or pre-materialize for performance-sensitive queries.
- **APOC procedures vary across Neo4j versions.** Pin versions; test on upgrade.
- **Bolt connection pooling matters.** Misconfigured drivers exhaust connections under load.

---

## Further Reading

- *Knowledge Graphs* (Barrasa & Webber), platform integration chapters
- Neo4j Graph Data Science documentation
- Neo4j GraphQL Library
- DataHub + Neo4j integration patterns
- See `knowledge-graph-modeling` for data models
- See `knowledge-graph-applications` for use case patterns

Source: *Knowledge Graphs* (Barrasa & Webber), platform integration chapters.
