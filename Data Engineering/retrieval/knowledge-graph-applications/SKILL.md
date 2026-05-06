---
name: knowledge-graph-applications
description: >
  Apply knowledge graph patterns for real applications: identity resolution
  (strong vs weak identifiers, Connected Components, SIMILAR), fraud
  detection (fraud rings, legitimate households), organizational graphs
  (org charts, expertise/skills graphs), dependency analysis (chains,
  multidependencies, redundant, SPOF, root cause), entity-based search,
  document similarity, and natural-language query/generation. Use when
  solving fraud detection, organizational analytics, dependency analysis,
  semantic search, or natural-language interfaces over a knowledge graph.
  Triggers: "fraud ring detection", "expertise graph", "single point of
  failure analysis", "root cause analysis with graphs", "entity-based
  search", "semantic search", "natural language to Cypher". Produces a
  pattern + query approach.
---

# Knowledge Graph Applications

You apply Barrasa & Webber's catalog of knowledge graph use cases: identity
resolution, fraud detection, organizational analytics, dependency analysis,
semantic search, and natural-language interfaces. Each is a recognizable
pattern; you fit your use case to the closest match.

---

## When to Use This Skill

- Detecting fraud (especially synthetic identity fraud)
- Resolving fragmented user identities into consolidated profiles
- Analyzing organizational structure + expertise networks
- Tracing dependencies for impact analysis or root cause
- Building semantic search over documents
- Exposing a natural-language interface to a graph

---

## Identity Resolution

### Strong vs Weak Identifiers

- **Strong identifier:** Stable, globally unique. Email, SSN, government ID, master ID.
- **Weak identifier:** Volatile or shared. Cookie, session ID, IP, device fingerprint, name.

**Pattern:** Aggregate weak identifiers into strong identifiers using graph algorithms.

### Connected Components (WCC)

```
[Cookie A] ──belongs_to──► [User Profile]
[Cookie B] ──belongs_to──► [User Profile]   ← all three cookies + email
[Cookie C] ──belongs_to──► [User Profile]    converge to one strong identity
[Email]    ──belongs_to──► [User Profile]
```

Run WCC over the weak-identifier graph. Each connected component is a unified profile.

### Node Similarity / SIMILAR

When string identifiers are weak, compute token-based similarity (Jaccard, cosine on n-grams). Above a threshold, link nodes with a `SIMILAR` relationship. Then run WCC over `SIMILAR` + other relationships.

**Use case:** Meredith Corporation example — fragmented user profiles consolidated by combining cookies + emails + name-similarity.

---

## Fraud Detection

### Fraud Rings

Synthetic identities sharing attributes (phone, address, SSN suffix) in a chain or ring.

```
[Person 1] ──shares phone──► [Phone X] ◄──shares phone── [Person 2]
[Person 2] ──shares addr──► [Address Y] ◄──shares addr── [Person 3]
[Person 3] ──shares phone──► [Phone Z] ◄──shares phone── [Person 4]
```

**Detection:** Find clusters of `Person` nodes connected through shared `Phone` / `Address` / etc. above a threshold.

### Negative Control: Legitimate Households

Two-Person + one-Address + one-Phone is normal (couple living together). Don't flag.

```
Differentiate:
  [Husband] ──► [Address] ◄── [Wife]
  [Husband] ──► [Phone]   ◄── [Wife]

   vs

  [Person 1] ──► [Address] ◄── [Person 2] ◄── [Phone] ◄── [Person 3] ──► [Address 2]
                                                                        ◄── [Person 4]
```

**Approach:** Use heuristic rules + ML on graph features (cluster size, shared-attribute count, application timing).

---

## Organizational Knowledge Graphs

### Org Charts

Hierarchical tree:

```
(:Person {name})-[:REPORTS_TO]->(:Person {name})
(:Person)-[:BELONGS_TO]->(:Department)
```

**Use cases:**
- Span of control analysis
- Reporting chain queries
- Department crossover

### Expertise Knowledge Graphs

Derived from collaboration platforms (Slack, Teams). Maps users to skills via message threads, replies, topic mentions.

```
(:User)-[:DISCUSSED]->(:Topic)-[:REQUIRES_SKILL]->(:Skill)
(:User)-[:HAS_EXPERTISE_IN {confidence}]->(:Skill)
```

**Use cases:**
- "Who knows about X?" — find users with high expertise in X
- "Knowledge power" — distinct from formal authority; identifies de facto experts

### Skills Knowledge Graphs

Models project dependencies and participation:

```
(:Project)-[:REQUIRES]->(:Skill)
(:User)-[:PARTICIPATED_IN {role, duration}]->(:Project)
```

**Use cases:**
- Tenure / recency / proficiency calculations
- Project staffing — match required skills to available people
- Career path analysis

---

## Dependency Analysis

### Dependency Chains

```
(:Service A)-[:DEPENDS_ON]->(:Service B)-[:DEPENDS_ON]->(:Service C)
```

**Traverse recursively:**
- Direct dependencies: 1 hop
- Transitive: variable-length traversal `(*)`

**Cypher:**
```cypher
MATCH (a:Service {name: 'A'})-[:DEPENDS_ON*]->(d:Service)
RETURN DISTINCT d
```

### Aggregate Multidependencies

Element depends on multiple others; weighted contributions sum to a threshold (e.g., 100% portfolio).

```
(:Portfolio) -[:CONTAINS {weight: 0.4}]-> (:Asset A)
(:Portfolio) -[:CONTAINS {weight: 0.35}]-> (:Asset B)
(:Portfolio) -[:CONTAINS {weight: 0.25}]-> (:Asset C)
```

### Redundant Dependencies

Multiple alternative paths; failure absorbed if at least one survives.

```
(:Network)-[:HAS_BACKUP]->(:Primary Router)
(:Network)-[:HAS_BACKUP]->(:Secondary Router)
```

### Single Point of Failure (SPOF)

Topological vulnerability where multiple chains converge on one node.

```
(:Service A)──┐
(:Service B)──┼──►(:Critical Database)──►(:Many Services)
(:Service C)──┘
```

**Detection:**
```cypher
MATCH (n)<-[:DEPENDS_ON*]-(s:Service)
WITH n, count(DISTINCT s) AS dependent_count
WHERE dependent_count > 10  // Adjust threshold
RETURN n, dependent_count
ORDER BY dependent_count DESC
```

### Root Cause Analysis

Inverse of impact propagation. Cluster failed nodes; find common ancestors.

```
   Failed nodes: A, B, C, D
   
   A ──┐
   B ──┼──► [Common Root: X]
   C ──┤
   D ──┘
```

**Approach:** For each failed node, walk up dependencies. Find common ancestors. Highest-frequency common ancestor is the likely root cause.

---

## Entity-Based Search

Beyond keyword search: annotate documents with extracted entities (Named Entity Recognition).

```
(:Document) -[:MENTIONS {salience}]-> (:Entity)
(:Entity) -[:IS_A]-> (:Concept)
```

**Search:** "Find documents about Apple Inc." matches entity `Apple_Inc`, not the keyword "apple."

**Salience:** how prominent the entity is in the document. Use as weight.

### Document Similarity

```
(d1:Document)-[:MENTIONS]->(e:Entity)<-[:MENTIONS]-(d2:Document)
```

**Similarity score:** Weighted overlap of shared entities × salience scores.

**Two strategies:**
- **On-the-fly:** Compute at query time. Always fresh; slower.
- **Materialized:** Precompute and store as `:SIMILAR_TO` relationships. Fast queries; needs refresh.

---

## Semantic Search via Organizing Principles

Disambiguate entities by linking to ontology entries:

```
"Apple" mention →
   - If preceded by "$", links to (:Company {name: "Apple Inc."})
   - If followed by "pie", links to (:Food {name: "Apple"})
```

**External links:** Wikipedia URLs, DBpedia, Wikidata IDs help disambiguate via NLP API output.

---

## Natural-Language Interfaces

### Natural Language Query → Cypher

Rule-based matchers (e.g., spaCy patterns) map linguistic tokens to schema elements.

```
"Find people who know Alice" →
  MATCH (p:Person)-[:KNOWS]->(:Person {name: 'Alice'})
  RETURN p
```

**Caveats:** Rule-based works for predictable patterns. For arbitrary NL, use LLM-to-Cypher (newer pattern, post-book).

### Natural Language Generation from Graphs

Generate sentences from subject-predicate-object triples.

```
(:Alice)-[:KNOWS]->(:Bob)  →  "Alice knows Bob."
```

**Annotate relationships** with bidirectional natural language:
- `KNOWS`: forward = "knows"; inverse = "is known by"

**Schema independence:** Use named properties for human-friendly text — don't expose internal names like `sub_109`.

### Lexical Database Integration

Store WordNet (or similar) as a graph for semantic similarity calculations.

**Algorithms:**
- **Leacock-Chodorow:** Depth-aware similarity using taxonomy depth
- **Least Common Subsumer:** Most specific shared ancestor

---

## Knowledge Lake Architecture

Evolution: Departmental KG → Inter-departmental KG → **Knowledge Lake** (foundational, general-purpose, subsuming other KGs and non-graph data).

**When valuable:** Mature data org with multiple graphs and data sources. Want a unified contextualized layer.

**Caveat:** Heavy. Most companies don't reach this stage.

---

## Principles

- **Aggregate weak identifiers into strong via graph algorithms.** WCC + similarity.
- **Fraud detection needs negative controls.** Avoid flagging legitimate households.
- **Org chart + expertise graph together** reveal more than either alone.
- **SPOF analysis surfaces hidden risks** that flat dependency lists miss.
- **Root cause analysis is graph traversal, not statistical inference.** Common ancestors reveal causes.
- **Entity-based search > keyword search** for ambiguous terms.
- **Salience weighting** is the difference between useful and noisy entity matches.
- **Materialize similarities** when query latency matters; compute on-the-fly when freshness matters.
- **Bidirectional annotations** make NL generation work in both directions.

---

## Anti-Patterns

### Identity Resolution Without Negative Control

**Looks like:** Aggressive WCC over shared attributes. Two strangers sharing a public WiFi IP merge into one identity.

**Why it fails:** Over-merge creates false consolidations.

**The fix:** Negative controls (legitimate households for fraud, public-IP filters for identity).

### Fraud Detection on Single Attribute

**Looks like:** Flagging anyone who shares a phone with another person.

**Why it fails:** Couples, families, roommates legitimately share. Massive false positive rate.

**The fix:** Multi-attribute clustering. Threshold on cluster size + sharing pattern.

### Dependency Graph Without Versioning

**Looks like:** "Service A depends on Service B" — but B has 5 versions, each different. Graph collapses them.

**Why it fails:** Impact analysis is inaccurate.

**The fix:** Model versions as nodes. Dependencies point at specific versions.

### SPOF Analysis as One-Off Audit

**Looks like:** Annual SPOF audit, results filed away.

**Why it fails:** Architecture changes; SPOFs change.

**The fix:** SPOF queries in CI. Alert on threshold violations.

### Entity-Based Search Without Disambiguation

**Looks like:** "Apple" entity match returns Apple Inc. + apple fruit + Apple Records.

**Why it fails:** Search results are mixed.

**The fix:** Disambiguate via context (Wikipedia URL, Wikidata ID, surrounding entities).

### NL-to-Cypher Without Schema Awareness

**Looks like:** Generic LLM generates Cypher. Hallucinates labels and relationships that don't exist.

**Why it fails:** Schema is constraint; LLM ignores.

**The fix:** Provide schema in the LLM prompt; constrained generation; validate against schema before execution.

### Document Similarity by Raw Term Overlap

**Looks like:** TF-IDF over raw text.

**Why it fails:** Synonyms missed; entity ambiguity persists.

**The fix:** Entity-based similarity. Salience-weighted shared entities.

---

## Decision Rules

| Use case | Pattern |
|---|---|
| Fragmented user profiles | Weak → Strong identifiers via WCC + Node Similarity |
| Synthetic-identity fraud | Multi-attribute clustering; legitimate households as control |
| "Who knows about X" | Expertise graph from collaboration data |
| Project staffing | Skills graph: REQUIRES + PARTICIPATED_IN + recency weight |
| Service dependency analysis | Recursive traversal; SPOF query for risk |
| Production incident root cause | Failed-node clustering; common ancestor traversal |
| Search over documents | Entity-based; disambiguate via Wikipedia / Wikidata |
| Document recommendation | Materialized SIMILAR_TO with salience weights |
| Natural-language query interface | Rule-based for predictable patterns; LLM-to-Cypher with schema for general |
| Generate text from graph | Subject-predicate-object with bidirectional annotations |
| Semantic similarity between concepts | WordNet integration; Leacock-Chodorow or Least Common Subsumer |
| Cross-domain unified knowledge | Knowledge Lake (heavy; only at scale) |

---

## Worked Example: Synthetic Identity Fraud Detection

**Context:** Bank. Need to detect synthetic identities (fake people created from real partial data).

**Approach:**

```
Application data → Knowledge Graph

Node types: Person, Phone, Address, Email, SSN_Last4, BankAccount, Device

Suspicious patterns:
  - Cluster of Person nodes sharing 3+ attributes
  - Application time within 24h
  - No long-term banking history
  - Aggregate credit limit > suspicious threshold

Negative controls:
  - Legitimate household: 2 Person + 1 Address + 1 Phone, application time spread out
  - Family: shared Address; different Phones; SSN_Last4 from same family
```

**Detection query:**
```cypher
MATCH (p:Person)-[:HAS_PHONE|HAS_ADDR|HAS_SSN_PREFIX]->(attr)<-[:HAS_PHONE|HAS_ADDR|HAS_SSN_PREFIX]-(other:Person)
WHERE p <> other
WITH p, COUNT(DISTINCT attr) AS shared_count, COLLECT(DISTINCT other) AS connections
WHERE shared_count >= 3 AND size(connections) >= 5
WITH p, connections, shared_count
MATCH (p)-[:APPLIED_FOR]->(app:Application)
WHERE app.created_at > date() - duration('P7D')
RETURN p, connections, shared_count, app
```

**Combine with:** ML model on graph features (cluster size, attribute overlap, temporal pattern).

**Result:** Detection rate up; false-positive rate manageable due to negative controls.

**Lesson:** Pure graph queries identify candidates. ML refines. Together they're stronger than either alone.

---

## Gotchas

- **WCC over noisy edges** produces giant components. Threshold or filter edges before running.
- **Salience weights vary by NLP API.** Calibrate; don't trust raw scores.
- **Wikipedia URL disambiguation has gaps.** Some entities aren't on Wikipedia.
- **Materialized similarities decay.** New documents arrive; old similarities miss them.
- **NL-to-Cypher LLM hallucinations.** Always validate against schema.
- **WordNet is English-centric.** Other languages need different lexical databases.
- **Knowledge Lake is a multi-year journey.** Don't promise it as a quarter-1 deliverable.
- **SPOF threshold is judgmental.** Tune to your environment.
- **Org charts go stale fast.** Refresh from HRIS at least weekly.
- **Expertise graphs depend on data privacy compliance.** Don't mine collaboration platforms without policy review.

---

## Further Reading

- *Knowledge Graphs* (Barrasa & Webber), Chapters on use cases
- Neo4j Graph Data Science library documentation
- See `knowledge-graph-modeling` for data models and organizing principles
- See `knowledge-graph-platform-integration` for ETL, GDS, ML pipelines

Source: *Knowledge Graphs* (Barrasa & Webber), use case chapters.
