---
name: mdm-and-federated-data-governance
description: >
  Apply Master Data Management (MDM) styles (Consolidation, Registry,
  Centralized, Coexistence), federated governance via data contracts and
  policy automation, data catalog + metalake architecture, knowledge graphs
  for metadata, semantic layers, and access control models (ACL, RBAC,
  ABAC + PEP/PDP/PIP/PAP). Use when scoping MDM, choosing an MDM style,
  designing a data catalog, building governance automation, defining data
  contracts, or implementing fine-grained access control on data products.
  Triggers: "MDM strategy", "consolidation vs registry vs centralized vs
  coexistence", "data contract", "data catalog", "knowledge graph for
  metadata", "ABAC for data", "semantic layer for governance", "metalake".
  Produces a chosen MDM style + governance architecture with policy
  automation.
---

# MDM and Federated Data Governance

You apply Strengholt's catalog of Master Data Management styles, federated
governance patterns, and metadata architectures. The discipline: maintain
authoritative master records, automate policy enforcement at the data product
level, and surface data through a catalog + semantic layer that consumers
can trust.

---

## When to Use This Skill

- Scoping Master Data Management (MDM) for a multi-domain enterprise
- Choosing among the four MDM styles
- Designing a data catalog (or evaluating one)
- Building automated, federated governance for a Data Mesh
- Defining data contracts between providers and consumers
- Implementing fine-grained access control on data products
- Considering a knowledge graph for metadata (metalake)

---

## The Four MDM Styles

```
LIGHT TOUCH                                                     HEAVY TOUCH
───────────                                                     ───────────

Registry        Consolidation       Coexistence         Centralized
Style           Style                Style               Style

Cross-          Hub aggregates       Improvements        Transactional
reference       for analytics;       flow back to        hub; cleansed +
table only      no modification      sources             republished
                of sources           bidirectionally     two-way sync

Lowest impact;  Easy analytics;      Authoritative       Most control;
Lowest control  Lowest source        across systems;     Highest impact
                impact               Some source impact  on sources
```

### 1. Registry Style

**Mechanics:** A master ID table maps records across systems. Sources unchanged.

**When:** Quick visibility into duplicates / inconsistencies. Discovery phase. No appetite for system changes.

**Pros:** Lowest impact. Fastest to deploy.
**Cons:** Doesn't fix data quality at source. Cross-system consistency stays manual.

### 2. Consolidation Style

**Mechanics:** MDM hub consolidates master data from sources for analytics / reporting. **Read-only relative to sources** — no propagation back.

**When:** Single source of truth for downstream analytics. Sources too critical / fragile to modify.

**Pros:** Low source impact. Clean analytics.
**Cons:** Operational systems still inconsistent. Drift between sources accumulates.

### 3. Coexistence Style

**Mechanics:** Improvements found in MDM hub flow back to sources via complex integration. Sources become consistent over time.

**When:** Authoritative records needed across operational systems. Willing to invest in bidirectional integration.

**Pros:** Operational consistency.
**Cons:** Complex; sources must accept updates from MDM.

### 4. Centralized Style

**Mechanics:** Transactional hub. Master data is *created and modified* in MDM, then **published** to source systems via two-way sync.

**When:** Strict regulatory requirement for single source. Greenfield rebuild possible.

**Pros:** Highest control. Single point of truth.
**Cons:** Highest impact. Often impractical to retrofit.

---

## Choosing an MDM Style — Pragmatic Path

Most enterprises follow this maturation:

```
Start ──► Registry ──► Consolidation ──► (sometimes) Coexistence ──► Centralized
         (visibility)  (analytics-       (operational    (only if
                        clean)            consistency)    greenfield or
                                                          regulatory)
```

**Strengholt's heuristic:** Don't try to unify all enterprise data. Select only the **stable, critical, broadly-shared** data elements for MDM scope. Customer, Product, Account — these are typical. Transaction-level data is usually not MDM scope.

### Practical Tactics

- **Master identifier centrally.** Issue unique, immutable IDs. Map to source-system local IDs.
- **Bake data quality in.** MDM hub validates on ingest. Reject or flag bad records.
- **Define ownership early.** Every master record has a domain owner. Modifications go through them.
- **Start narrow.** 5 critical master entities. Expand as you learn.

---

## The Data Catalog and Metalake Architecture

### Data Catalog

An inventory of data products with metadata:
- Business terms (glossary)
- Owners
- Origins / lineage
- Classifications (PII, SOX, GDPR-restricted)
- SLAs (freshness, quality, availability)
- Schema + sample
- Access requests

**Tools:** DataHub (open-source), Atlan, Collibra, Alation, Apache Atlas.

### Metalake Architecture

```
                      [Marketplace Layer]
                       (visualization +
                        consumption UI)
                              ▲
                              │
                       [Knowledge Graph]
                       (semantic relationships
                        across all metadata)
                              ▲
                              │
                      [Processed Zone]
                      (cleansed, integrated metadata)
                              ▲
                              │
                      [Landing Zone]
                      (raw metadata from
                       all sources)
```

**The idea:** Treat metadata itself as data. Apply lakehouse architecture (Bronze / Silver / Gold) to metadata. Use a knowledge graph as the unified semantic layer.

**When valuable:** Large enterprise with hundreds of data products and complex relationships. Heavy compliance load.

**Caveat:** Heavy. Most companies don't need it. A single catalog tool with manual relationships is enough until it isn't.

---

## Knowledge Graphs for Metadata

A knowledge graph models data products and their relationships as nodes + edges in a semantic graph (RDF, OWL, SPARQL — or a property-graph DB).

```
[Customer Data Product]
    │
    ├─owned_by──► [Customer Domain]
    ├─complies_with──► [GDPR]
    ├─derived_from──► [CRM Source System]
    ├─produces──► [Customer 360 View]
    └─used_by──► [Marketing Campaign Service]
```

**Why use it:**
- Cross-cuts traditional table/document silos
- Powers "show me everything that depends on this" queries
- Enables federated semantic search

**Implementation options:**
- **RDF/SPARQL:** GraphDB, Stardog. Pure semantic web; standards-aligned.
- **Property graph:** Neo4j, Amazon Neptune. Easier to operate.
- **Both via gateway:** Some platforms support both queries.

**When to bother:** Heavy metadata complexity (regulatory, multi-source). Otherwise, a relational catalog is sufficient.

---

## Semantic Layer (Beyond BI Metrics)

Earlier covered as a metric-definition layer for BI. Extends to:

- **Business glossary:** "Customer" defined once; consistent across all surfaces
- **Data products:** Logical entity in metamodel; multiple physical implementations OK
- **Lineage:** Semantic, not just column-level
- **Access policies:** Bound to semantic roles, not physical tables

**Strengholt's framing:** Define data products as **logical entities** in a metamodel, linked to glossary terms and technical attributes. Provides flexibility — physical implementation can change without metadata churn.

---

## Federated Computational Governance

Three components, working together:

### 1. Data Contracts

Provider commits to:
- Schema (versioned)
- SLA (freshness, quality, availability)
- Classifications (PII, sensitivity)

Consumer commits to:
- Acceptable usage
- Notification of breaking-change needs
- Compliance with classifications

**Tooling:** Bitol Project's Open Data Contract Standard (ODCS), Data Contract CLI, custom YAML in dbt, etc.

**Practical:** Treat data contract YAML files like API contracts. Version control. PRs. Breaking changes follow deprecation cycle.

### 2. Policy Automation (ABAC / OPA)

```
ACCESS CONTROL EVOLUTION:

ACL (Access Control Lists)
   ↓
RBAC (Role-Based Access Control)
   ↓
ABAC (Attribute-Based Access Control)
```

**ABAC architecture:**

```
[Subject] ──request──► [Policy Enforcement Point (PEP)]
                              │
                              ▼
                       [Policy Decision Point (PDP)]
                              │
                              ├──queries──► [Policy Information Point (PIP)]
                              │
                              ├──reads──► [Policy Administration Point (PAP)]
                              │
                              ▼
                       [Allow / Deny]
```

**Components:**
- **PEP:** Where access is enforced. Often the data plane (warehouse, API gateway).
- **PDP:** Evaluates policies. Open Policy Agent (OPA) is the canonical OSS implementation.
- **PIP:** Provides data for decision (e.g., user attributes, data classifications).
- **PAP:** Where policies are authored and registered. Often a UI or Git repo.

**Practical:** OPA + Rego policies. Domain-team-authorable. Version-controlled. Auto-applied at every data touch.

### 3. Data Contract Application (DCA)

A standalone application that acts as the **PAP + PIP** for data contracts:
- Domains register their products + contracts
- Consumers register usage agreements
- DCA exposes them to PEPs (warehouses, gateways) for enforcement

**Benefit:** Self-serve governance. Domains don't ask a central committee; they register a contract.

---

## Domain Data Stores (DDS)

Distinct from data products: **DDS is a consumer-side store** that ingests, transforms, and stores data **for a specific use case** (a department's reporting model, a feature store for an ML team).

**Key distinction:**
- **Data Product:** Stable, owned by source domain, contract-bound
- **Domain Data Store:** Specific to a consumer, may be transient, owned by consumer

Both are valid. The mistake is treating one as the other.

---

## Principles

- **Define ownership before the workflow.** A new dataset without an owner is a future fire.
- **Master data is narrow by design.** Don't try to MDM everything. 5-10 entities.
- **Bake data quality in at the producer.** Pushing it downstream multiplies effort.
- **Data contracts are API contracts.** Version, deprecate, communicate.
- **Federated governance via automation.** Manual approvals don't scale.
- **Glossary first; tooling second.** A shared business glossary is the foundation of every other catalog feature.
- **Semantic > syntactic.** Metadata should describe meaning, not just structure.
- **Logical data product > physical table.** Allows underlying technology to change.

---

## Anti-Patterns

### MDM as Big Bang

**Looks like:** "Let's MDM everything." 18-month project. Scope creep. Eventually canceled.

**Why it fails:** MDM scope explodes when undisciplined.

**The fix:** Start with Registry style. 5 entities. 90 days to first value. Expand from there.

### Catalog Without Owners

**Looks like:** Adopting DataHub/Atlan/Collibra. Loading metadata. Nobody owns the entries. They go stale.

**Why it fails:** A catalog is a maintenance commitment. Without owners, it's a graveyard.

**The fix:** Every entry has an owner. Owners review quarterly. Stale entries archived.

### RBAC When ABAC is Needed

**Looks like:** "Marketing role can read all marketing data" — but compliance requires PII to be tokenized for non-EU teams.

**Why it fails:** Role-based can't express attribute-based constraints.

**The fix:** ABAC for fine-grained policies. PEP at data plane. OPA for policy logic.

### Data Contracts as Documentation Only

**Looks like:** YAML data contract files. Nobody enforces. Contracts drift from reality.

**Why it fails:** Contracts must be enforced or they're theater.

**The fix:** CI checks. Schema validation at ingestion. Breaking changes blocked at PR.

### Semantic Layer Without Business Buy-in

**Looks like:** Engineering builds a semantic layer. Business teams keep their own metric definitions in spreadsheets.

**Why it fails:** Two sources of truth. Engineering's semantic layer is rejected.

**The fix:** Co-author semantic definitions with business. Migrate spreadsheet metrics through co-design, not over-the-wall.

### Knowledge Graph as First Move

**Looks like:** Adopt RDF + SPARQL + GraphDB before having a working catalog.

**Why it fails:** Heavy stack with steep learning curve. Premature optimization.

**The fix:** Start with relational catalog. Adopt knowledge graph when complexity genuinely warrants.

### Treating Domain Data Stores as Products

**Looks like:** Marketing builds a "marketing data store" for its reporting. Other teams query it as if it's a stable data product.

**Why it fails:** DDS isn't a contract-bound product. Schema changes silently. Consumers break.

**The fix:** Distinguish DDS from data products explicitly. Products have contracts; DDS doesn't.

---

## Decision Rules

| Situation | Action |
|---|---|
| First MDM effort | Registry style. 5 entities. 90-day target. |
| MDM goal: clean analytics | Consolidation style. |
| MDM goal: cross-system operational consistency | Coexistence (if sources accept) or Centralized (greenfield). |
| Greenfield with strict regulatory | Centralized MDM possible if app-layer cooperation exists. |
| Scoping MDM | Pick stable, broadly-shared, critical entities. Reject transactional. |
| Data catalog adoption | Pick one tool (DataHub if OSS-leaning). Establish ownership process before loading metadata. |
| Multi-team metric drift | Adopt semantic layer (LookML / dbt Semantic Layer / Cube). Migrate spreadsheet metrics via co-design. |
| Fine-grained access requirement | ABAC. OPA + Rego. PEP at data plane. |
| Cross-system metadata complexity | Knowledge graph; otherwise stick with relational catalog. |
| Provider/consumer drift complaints | Adopt formal data contracts. Enforce in CI. |
| New cross-domain data product | Define owner first. Then schema. Then contract. Then implement. |
| Existing PII spread | Tokenize at ingest. ABAC policy: only specific roles see raw. |
| Compliance audit incoming | Catalog must show: data inventory, owners, classifications, lineage, access logs. |
| Domain wants its own store | DDS — but explicit it's not a data product (no cross-domain contract). |

---

## Worked Example: Federated Governance for a Pharma's Data Mesh

**Context:** Global pharma, regulatory-heavy. Multiple business units (Research, Clinical Trials, Commercial, Supply Chain). 30 data products envisioned.

**Architecture:**

| Component | Choice |
|---|---|
| MDM style for "Customer" / "Product" / "Site" | Coexistence — research and commercial both modify; both must converge |
| MDM style for transactional data | Not in MDM scope |
| Catalog | DataHub OSS — extensible, REST API for integration |
| Knowledge graph for metadata | Yes — pharma's regulatory complexity warrants. Stardog over Neptune (RDF/SPARQL native). |
| Data Contract format | Open Data Contract Standard (ODCS). Stored in Git. |
| Policy enforcement | OPA at the warehouse boundary (Snowflake row + column policies driven by OPA). |
| PEP locations | Warehouse, API gateway, BI tool query layer. |
| PAP | DataHub (catalog) + GitOps repo (Rego policies). |
| PIP | Identity provider (Okta) for user attributes; DataHub for data classifications. |
| Semantic layer | dbt Semantic Layer for metrics; pharma-specific glossary in DataHub. |
| Lineage | OpenLineage emitted from Airflow/dbt; ingested into DataHub + knowledge graph. |
| Access flow | User requests access → DataHub portal → policy auto-evaluates → JIT grant or human review → audit. |

**First quarter scope:** 5 master entities. 8 highest-value data products. Full ABAC-enforced.

**Why it works:** Heavy regulatory load justifies the metalake + knowledge graph investment. Without that load, this would be over-engineering.

**Lesson:** Metalake / knowledge graph approach matches regulated industries where metadata complexity dominates. Lighter approach for less-regulated contexts.

---

## Gotchas

- **MDM is a multi-year journey, not a project.** Plan for ongoing investment.
- **Data contracts only work with cultural buy-in.** YAML files alone won't change behavior.
- **OPA performance matters.** Per-query policy evaluation can add latency. Cache decisions; batch policies.
- **Knowledge graphs require ongoing curation.** Outdated nodes / relationships become misleading.
- **Catalog adoption is the hardest part.** Tooling is the easy part. Owner enrollment is the hard part.
- **Semantic layer + LookML lock-in:** moving off Looker is non-trivial if all metrics are LookML.
- **DCA + ABAC can become governance bottlenecks** if approval workflows are heavy. Default to auto-grant for compliant requests.
- **MDM "single source of truth" is nuanced.** "Single source of definition" is the goal; physical implementations may vary by use case.
- **Consolidation MDM still leaves operational drift.** Decide if that's acceptable; if not, you need Coexistence or Centralized.

---

## Further Reading

- *Data Management at Scale* (Strengholt), Chapters 5-7
- *Building the Data Lakehouse* by Inmon, Levins, Srivastava — for metalake / catalog approaches
- *Open Policy Agent (OPA)* documentation — Rego language and integration patterns
- *Data Contracts* by Andrew Jones (O'Reilly, 2024) — the canonical contracts reference
- *Building Knowledge Graphs* by Hofer & Bonatti — semantic web foundations
- See `data-mesh-domain-topologies` for the topology context where this governance operates
- See `enterprise-data-integration-and-distribution` for the integration patterns governance constrains

Source: *Data Management at Scale* (Strengholt), Chapters 5-7 (MDM, Governance, Metadata).
