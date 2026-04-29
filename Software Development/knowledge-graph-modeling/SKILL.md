---
name: knowledge-graph-modeling
description: >
  Model knowledge graphs with the right data model — Plain Old Graph,
  Property Graph, Labeled Property Graph — plus organizing principles
  (Taxonomies, Ontologies), Just-Enough-Semantics, federation, and
  virtualization (LOAD CSV, neo4j-admin import, APOC virtual nodes,
  Composite Databases). Use when scoping a knowledge graph, choosing
  property graph vs RDF, deciding when to use ontology vs taxonomy,
  loading initial data, or federating multiple graphs. Triggers: "model a
  knowledge graph", "property graph vs RDF", "taxonomy vs ontology",
  "load data into Neo4j", "graph federation", "data virtualization for
  graphs", "Schema.org vs custom ontology". Produces a graph model + import
  strategy + organizing principle.
---

# Knowledge Graph Modeling

You apply Barrasa & Webber's *Knowledge Graphs* methodology: graphs aren't
useful unless they have an **organizing principle**. You pick the graph
model (Plain Old → Property → Labeled Property), layer the right
organizing principle (Taxonomy → Ontology), and load data efficiently.

---

## When to Use This Skill

- Scoping a knowledge graph for a use case
- Choosing the graph data model
- Deciding between taxonomy and ontology
- Adopting standards (SNOMED CT, Schema.org, OWL) vs building custom
- Loading initial data (LOAD CSV, neo4j-admin import, Data Importer)
- Federating multiple knowledge graphs

---

## Three Data Models

### 1. Plain Old Graph

Just nodes and edges. Interpretation lives entirely in application logic.

**When:** Pre-prototype. Quick exploration. Throwaway analysis.
**Caveat:** Doesn't scale beyond one application. Other tools can't reuse.

### 2. Property Graph Model

Nodes + typed/directed relationships + key-value properties on both.

```
(Alice {name: "Alice", age: 30}) -[:KNOWS {since: 2020}]-> (Bob {name: "Bob"})
```

**When:** Most knowledge graphs. Default choice.
**Tools:** Neo4j, JanusGraph, TigerGraph, Memgraph.

### 3. Labeled Property Graph Model (LPGM)

Adds **labels** (tags) to nodes describing their role.

```
(:Person:Employee {name: "Alice"}) -[:WORKS_FOR]-> (:Company {name: "Acme"})
```

**When:** Practically the same as property graph; LPGM is what Neo4j and similar tools implement.
**Important:** Labels are **tags**, not classes. No inheritance. No associativity. They mark roles.

### RDF / Triple Store (alternative paradigm)

Subject-Predicate-Object triples. Standards: RDF, OWL, SPARQL.

```
:Alice :knows :Bob .
:Alice :age 30 .
```

**When:** Semantic web standards required (academic, government, healthcare). OWL reasoning needed. Federation across SPARQL endpoints.

**Property Graph vs RDF:** Property graphs are practitioner-friendly; RDF is standards-aligned. Most enterprises use property graphs unless RDF is mandated.

---

## Organizing Principles

A graph without organization is noise. The **organizing principle** is the contract between the graph and its consumers.

### Taxonomy

Hierarchical classification. Broader/narrower. Generalization/specialization.

```
Vehicle
  ├── Car
  │    ├── Sedan
  │    └── SUV
  └── Truck
       ├── Pickup
       └── Heavy
```

**When:** Categorization is the primary need. Domains with established hierarchies (product catalogs, biological taxonomy).

**Standards:** SKOS (Simple Knowledge Organization System), Dewey Decimal, MeSH.

### Ontology

Beyond hierarchy. Defines complex non-hierarchical relationships:
- `IS_A`, `PART_OF`, `COMPATIBLE_WITH`, `CAUSES`, `INHIBITS`, `UPSELL`, etc.

**When:** Domain has rich relationship structure beyond hierarchy. Healthcare (SNOMED CT), pharma, finance.

**Standards:** OWL (Web Ontology Language), RDFS, Schema.org, FIBO (financial), SNOMED CT (medical).

**Custom vs standard:**
- **Adopt standards** for interoperability if they exist (Schema.org, SNOMED CT)
- **Build custom** if you need fine-grained control or specific business logic
- **Hybrid** is common: use Schema.org for common concepts; extend with custom for domain-specific

### Just-Enough-Semantics

Don't over-engineer. Add semantic metadata only when the current use case requires it. Build complexity as business demands evolve.

**Anti-pattern:** Adopting OWL + reasoner + full ontology before validating the graph helps the use case.

---

## Loading Data

### LOAD CSV

Cypher command for online bulk loading from filesystems, web URLs, or compressed streams.

```cypher
LOAD CSV WITH HEADERS FROM 'file:///customers.csv' AS row
MERGE (c:Customer {id: row.id})
SET c.name = row.name, c.email = row.email
```

**When:** Iterative loading; smaller datasets (millions); production-running database.
**Caveats:** Slower than offline; locks affect online queries.

### neo4j-admin import

Offline command-line tool. High-throughput bootstrap. Database must be empty.

**When:** Initial bulk load of large datasets (10M+ nodes). Production-grade bootstrapping.
**Caveats:** Database offline during import. CSV format requirements are strict.

### Neo4j Data Importer

Visual tool. Define domain model graphically; map CSV columns; generate Cypher. Good for prototyping.

**When:** Early modeling; non-developer users.

### APOC

Apache Commons-style extension library. Provides:
- `apoc.load.json`, `apoc.load.xml` — load other formats
- `apoc.periodic.iterate` — batch processing for large transformations
- Virtual nodes/relationships — represent external data without persisting

---

## Graph Federation

When multiple knowledge graphs exist (different teams, different systems), federate rather than merge.

### Composite Databases (Neo4j 5+)

Virtual database integrating multiple physical graph sources. Single point of access; underlying graphs unchanged.

```
Application
    │
    ▼
[Composite DB: enterprise]
    │
    ├──► [Physical: hr-graph]
    ├──► [Physical: products-graph]
    └──► [Physical: customer-graph]
```

**When:** Multiple graphs with cross-domain query needs. Avoid wholesale merge.

### Data Virtualization

External data sources (CSV, SQL DBs, JSON APIs) presented as virtual nodes/relationships. Useful when data shouldn't be copied into the graph.

**Caveats:** Performance depends on the underlying source. Caching helps.

---

## Performance Optimization

### Hardware Synergy

- **Working set in RAM:** Graph traversals are random-access; disk I/O kills performance.
- **SSD over HDD:** Random reads on HDD are ~100x slower than sequential.
- **Sufficient memory:** Operating system page cache + Neo4j page cache + heap.

### Query Optimization

- **Traverse structure first; retrieve properties last.** Graph traversal is constant-time per hop; property lookup is linear in the property store.
- **Use indexes for entry-point lookups** (label + property). Don't index everything.
- **Limit early.** `LIMIT 10` after a small `MATCH` is much faster than after a massive one.

---

## Principles

- **Organizing principle is the contract.** Graph without organization is noise.
- **Just-Enough-Semantics.** Don't over-model.
- **Adopt standards if they fit.** SNOMED CT, Schema.org, OWL — interoperability matters.
- **Property graph for practitioners; RDF for standards-mandated contexts.**
- **Labels are tags**, not classes. No inheritance.
- **Federate; don't merge.** Composite databases over wholesale rewrites.
- **Hardware synergy:** working set in RAM is non-negotiable.
- **Query traverses structure first, properties last.** Performance follows.

---

## Anti-Patterns

### Plain Old Graph in Production

**Looks like:** Nodes and edges with no labels, no relationship types, no organizing principle. Application encodes everything.

**Why it fails:** Tools can't reason about it. Visualization breaks. Other apps can't reuse.

**The fix:** Add an organizing principle. Even a basic taxonomy.

### Ontology-First Without a Use Case

**Looks like:** Spending months building a comprehensive ontology before loading any data.

**Why it fails:** The ontology is theoretical. The first real use case will reveal it's wrong.

**The fix:** Just-Enough-Semantics. Build minimal organizing principle. Iterate.

### Custom Ontology When Standard Exists

**Looks like:** Building a custom medical ontology when SNOMED CT exists.

**Why it fails:** Reinventing the wheel. Lose interoperability.

**The fix:** Adopt the standard. Extend if needed, but don't replace.

### Massive Ingestion via LOAD CSV

**Looks like:** Loading 100M nodes via LOAD CSV. Hours per chunk. Locks slow queries.

**Why it fails:** LOAD CSV is online; not optimized for bulk bootstrap.

**The fix:** `neo4j-admin import` for initial load. LOAD CSV for incremental.

### One Giant Graph for Everything

**Looks like:** Merging HR, products, customers, finance, ops all into one Neo4j database.

**Why it fails:** Operations conflict. Performance suffers. Ownership is unclear.

**The fix:** Multiple graphs by domain. Composite Database for cross-domain queries.

### Property-Heavy Traversals

**Looks like:** Cypher query that retrieves properties on every traversed node, then filters.

**Why it fails:** Property lookup is the slow operation. Doing it on every traversed node is O(n) per traversal.

**The fix:** Traverse structure first. Filter on labels and relationships. Retrieve properties only on the surviving set.

### Index Everything

**Looks like:** Index on every property of every node.

**Why it fails:** Indexes slow writes; consume RAM. Most aren't queried.

**The fix:** Index entry points only (e.g., `:Person(email)` for lookups).

---

## Decision Rules

| Situation | Action |
|---|---|
| New graph project | Start with property graph (Neo4j default) unless RDF mandated |
| RDF / OWL / SPARQL required | Triple store (Stardog, GraphDB, Allegrograph) |
| Need just classification | Taxonomy (SKOS or simple parent-child) |
| Need rich relationships | Ontology (OWL, Schema.org, FIBO, SNOMED CT) |
| Standard exists for domain | Adopt; extend if needed |
| No standard | Custom ontology; document carefully |
| Initial bulk load (millions+) | `neo4j-admin import` |
| Incremental load | LOAD CSV |
| Visual modeling | Neo4j Data Importer |
| Multiple existing graphs | Composite Database (federation) |
| External data shouldn't be copied | Data virtualization (APOC virtual nodes) |
| Slow queries | Traverse structure first; retrieve properties last; index entry points |
| Working set > RAM | Add memory; the working-set-in-RAM rule is non-negotiable |
| Want OWL reasoning | Use a triple store; property graphs don't have native reasoners |
| Mostly a documentation graph | Schema.org probably suffices |
| Healthcare | SNOMED CT for medical concepts |
| Finance | FIBO for financial concepts |

---

## Worked Example: Modeling a Product Knowledge Graph for E-Commerce

**Context:** B2C retailer. 100K products. Want recommendations, search, and product comparison.

**Modeling decisions:**

| Decision | Choice |
|---|---|
| Data model | Property graph (Neo4j) |
| Organizing principle | Schema.org Product + custom extensions |
| Taxonomy | Product categories (Schema.org `ProductCategory`) |
| Ontology | Custom relationships: `COMPATIBLE_WITH`, `UPSELL_TO`, `BUNDLED_WITH`, `REPLACES` |
| Initial load | `neo4j-admin import` from product DB extract |
| Ongoing sync | CDC from product DB → Kafka → LOAD CSV (incremental) |
| Federation | None — single domain |

**Schema:**

```
(:Product {sku, name, price, ...}) -[:IN_CATEGORY]-> (:Category)
(:Product) -[:COMPATIBLE_WITH]-> (:Product)
(:Product) -[:UPSELL_TO]-> (:Product)
(:Product) -[:HAS_FEATURE]-> (:Feature)
(:Customer) -[:VIEWED|PURCHASED]-> (:Product)
```

**Use cases:**
- Recommendation: traverse `(:Customer)-[:PURCHASED]->(:Product)-[:UPSELL_TO]->(:Recommendation)`
- Search: index `:Product(name)` for full-text; combine with category traversal
- Comparison: traverse `:HAS_FEATURE` for two products; intersect

**Result:** Schema.org gives interoperability; custom relationships give business specifics. `neo4j-admin import` bootstrapped 100K products in 30 seconds.

**Lesson:** Schema.org first. Custom relationships only where needed. Don't over-model.

---

## Gotchas

- **Labels are not classes.** Multiple labels are tags. `:Person:Employee` means the node is both, not "Employee inherits from Person."
- **`neo4j-admin import` requires database to be empty.** Plan accordingly.
- **LOAD CSV memory footprint** can blow up on huge files. Use `:auto USING PERIODIC COMMIT` (older Neo4j) or `CALL { ... } IN TRANSACTIONS` (Neo4j 5+).
- **APOC isn't bundled by default in Neo4j 5+.** Install separately.
- **Property graphs don't reason like RDF/OWL.** No automatic inference. Reasoning is explicit Cypher logic.
- **Composite Databases require Enterprise license** (Neo4j 5+).
- **Data virtualization performance depends on source.** Caching is essential for any latency-sensitive use case.
- **Schema.org has limits.** It's broad and shallow. Domain-specific ontologies (FIBO, SNOMED CT) are deeper.
- **OWL reasoning is computationally expensive.** Most queries don't need it; reach for it only when necessary.

---

## Further Reading

- *Knowledge Graphs: Data in Context for Responsive Businesses* by Barrasa & Webber (O'Reilly, 2023)
- *Building Knowledge Graphs* by Hofer & Bonatti — semantic-web-leaning reference
- Neo4j documentation — neo4j.com/docs
- Schema.org — for common concept ontologies
- See `knowledge-graph-applications` for fraud detection, RCA, semantic search use cases
- See `knowledge-graph-platform-integration` for ETL, Spark, Kafka, GDS

Source: *Knowledge Graphs* (Barrasa & Webber, O'Reilly, 2023).
