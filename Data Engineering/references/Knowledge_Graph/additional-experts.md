# Knowledge Graphs — Additional Expert Notes

> From *Knowledge Graphs* by Jesús Barrasa & Jim Webber (Neo4j; O'Reilly, 2023).

## About the Authors

**Jesús Barrasa** — Neo4j practitioner; semantic web background.
**Jim Webber** — Chief Scientist at Neo4j; co-author of *Graph Databases*. Distributed-systems heritage.

**Voice:** Practitioner-grounded; Neo4j-leaning but principles are model-agnostic. Strong skeptic of over-engineering ("just-enough-semantics").

## Foundational Mindset Shifts

1. **Graphs need an organizing principle.** Plain Old Graphs are application logic in disguise.
2. **Just-Enough-Semantics.** Don't build the comprehensive ontology before validating use cases.
3. **Adopt standards if they fit.** SNOMED CT, Schema.org, FIBO. Custom only when needed.
4. **Federate; don't merge.** Composite databases over wholesale rewrites.
5. **Graph algorithms run on projections, not live graphs.**
6. **Entity resolution is graph-native.** WCC + similarity + blocking = the canonical workflow.
7. **Knowledge Lake is mature-stage.** Most companies don't reach that scale.

## Best Practices by Topic

### Modeling
- Property graph (Neo4j) is the practitioner default
- Labels are tags, not classes
- Add organizing principle (taxonomy / ontology) early
- Schema.org for common concepts; domain-specific (SNOMED CT, FIBO) for specialized
- Bidirectional annotations on relationships (forward + inverse text)

### Loading
- `neo4j-admin import` for initial bulk (millions+)
- LOAD CSV for incremental updates
- Kafka Connect for streaming sync
- Spark connector for distributed preprocessing
- APOC for utility (JSON/XML/virtual nodes)

### Application patterns
- WCC + Node Similarity for identity resolution
- Multi-attribute clustering with negative controls for fraud
- Org chart + Expertise + Skills graphs together
- SPOF queries for dependency risk
- Common-ancestor traversal for root cause
- Entity-based search with disambiguation
- Materialized similarities for fast queries

### Performance
- Working set in RAM (non-negotiable)
- SSD for the graph store
- Index entry points only
- Traverse structure first; retrieve properties last
- LIMIT early in queries
- Memory locality > distributed scale-out for graph algorithms

### Integration
- GraphQL API for application-facing
- UDFs for domain-specialized logic; tested independently
- GDS algorithms on projected subgraphs
- Composite databases for federation
- DataHub + Neo4j for metadata knowledge graph

## Specific Advice

### "Organizing principle is the contract"
**Why:** Without it, the graph is application-specific. Tools, visualization, reuse all break.
**Apply:** Even a basic taxonomy is better than nothing.

### "Just-Enough-Semantics"
**Why:** Comprehensive ontologies built upfront are theoretical. Real use cases reveal flaws.
**Apply:** Build minimal organizing principle. Iterate.

### "Federate, don't merge"
**Why:** Wholesale merges of multiple graphs are expensive, slow, and politically fraught.
**Apply:** Composite Database (Neo4j Enterprise). Multiple physical graphs; one virtual access point.

### "Aggregate weak identifiers into strong"
**Why:** Real-world data has many weak identifiers (cookies, IPs). Combining them via graph algorithms reveals true identities.
**Apply:** WCC over weak-identifier edges; Node Similarity for fuzzy matches.

### "Negative controls in fraud detection"
**Why:** Aggressive aggregation produces false positives (legitimate households, public WiFi).
**Apply:** Filter known-legitimate patterns. Threshold on cluster size + temporal pattern.

### "GDS on projections"
**Why:** Algorithms are heavy; running on production graphs blocks queries.
**Apply:** Project subgraph in memory; run; write back.

### "Entity resolution: 3 stages"
**Why:** ER is a process, not an algorithm. Prep + match + curation each have distinct concerns.
**Apply:** Normalize → Block → Match (strong + weak) → WCC → Master records.

## Worked Examples

### Modeling a product knowledge graph for e-commerce
See `knowledge-graph-modeling`.

### Synthetic identity fraud detection
See `knowledge-graph-applications`.

### Entity resolution for B2B SaaS contacts
See `knowledge-graph-platform-integration`.

## Anti-Patterns Deeper Than Skill Files

- **Plain Old Graph in production** — interpretation in app logic only
- **Ontology-first without use case** — months on theoretical model
- **Custom ontology where standard exists** (e.g., custom medical instead of SNOMED CT)
- **One giant graph** for unrelated domains
- **Property-heavy traversals** — slow even on small graphs
- **Index-everything** — write performance crater
- **Identity resolution without negative controls** — over-merge
- **Fraud detection on single attribute** — massive false positives
- **Dependency graph without versioning** — can't reason about specific versions
- **SPOF analysis as one-off** — architecture changes; SPOFs change
- **Entity-based search without disambiguation** — Apple Inc. + apple fruit collide
- **NL-to-Cypher LLM hallucinations** — schema-unaware generation
- **Document similarity by raw term overlap** — synonyms missed
- **LOAD CSV for bulk bootstrap** — locks queries; slow
- **Streaming + sync confusion** — two sources of truth
- **GraphQL with expensive resolver Cypher** — N+1 problem
- **GDS on live production graph** — blocks queries
- **UDFs without tests**
- **ER without blocking keys** — O(n²) explosion

## Process Wisdom

- Schema-first — define organizing principle before loading
- Document Cypher conventions in repo (CONTRIBUTING.md for graph queries)
- Version control GraphQL schemas, ontologies, organizing principles
- Index review quarterly — most are unused
- GDS workflows in code (not Cypher Browser scratchpad)
- Entity resolution metrics: precision, recall, F1 — track over time

## Career / Context Wisdom

- Graph engineering is a niche but rising specialty
- Neo4j is the dominant property graph; competitors include TigerGraph, Memgraph, JanusGraph
- RDF/SPARQL world is academic-leaning; Stardog and GraphDB are common
- LLMs + KGs is a hot 2025-2026 topic (RAG with structured knowledge)
- Knowledge engineering as a discipline overlaps data engineering + librarianship + ML

Source: *Knowledge Graphs* (Barrasa & Webber, O'Reilly, 2023).
