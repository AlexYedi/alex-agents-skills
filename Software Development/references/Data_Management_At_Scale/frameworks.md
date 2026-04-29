# Data Management at Scale — Frameworks Catalog

## Index

| Name | Domain |
|---|---|
| ABAC (Attribute-Based Access Control) | Governance |
| ACL / RBAC / ABAC progression | Governance |
| Backend for Frontend (BFF) | Integration |
| Bounded Contexts (DDD) | Domain Modeling |
| Centralized Domain Topology | Topology |
| Centralized MDM Style | MDM |
| Coarse-Grained Domain Topology | Topology |
| Coexistence MDM Style | MDM |
| Common Driveway Pattern | Topology |
| Complex Event Processing (CEP) | Integration |
| Composite Services | Integration |
| Consolidation MDM Style | MDM |
| CQRS | Integration |
| Data Catalog | Governance |
| Data Contract / DCA | Governance |
| Data Fabric | Architecture |
| Data Mesh | Architecture |
| Data Product | Architecture |
| Domain Data Stores (DDS) | Architecture |
| Event Brokers | Integration |
| Event Sourcing | Integration |
| Event Stream Engines | Integration |
| Event Stores | Integration |
| Federated Computational Governance | Governance |
| Federated Responsibility Model | Integration |
| Fully Federated Domain Topology | Topology |
| Golden Source | Architecture |
| Governed Domain Topology | Topology |
| Hub-and-Spoke Topology | Topology |
| Knowledge Graph | Governance |
| Landing Zones (Single, Multi, Source/Consumer-aligned) | Topology |
| MDM Styles (4) | MDM |
| Medallion Architecture (Bronze/Silver/Gold) | Storage |
| Message Queues | Integration |
| Metalake Architecture | Governance |
| MLOps / DataOps | Discipline |
| Partially Federated Domain Topology | Topology |
| PEP / PDP / PIP / PAP | Governance |
| Point-to-Point (exception pattern) | Integration |
| Queue-Based Load Leveling | Integration |
| Registry MDM Style | MDM |
| Republishing Through Aggregates | Topology |
| Resource-Oriented Architecture (ROA) | Integration |
| REST | Integration |
| Semantic Layer | Governance |
| Service Choreography | Integration |
| Service Mesh | Integration |
| Service Orchestration | Integration |
| Service-Oriented Architecture (SOA) | Integration |
| Shared Kernel Integration | Topology |
| Source-Aligned Topology | Topology |
| Strangler Pattern | Migration |
| Stream Processing Engines | Integration |
| Value Chain-Aligned Domain Topology | Topology |

## Catalog (Detailed)

### Data Mesh
**Origin:** Zhamak Dehghani, 2019.
**Structure:** Domain-oriented decentralized data ownership; data as product; self-serve platform; federated computational governance.
**When:** Large org with strong domain capability and platform investment.

### Data Fabric
**Origin:** Gartner-popularized; Strengholt extends.
**Structure:** Intelligent metadata layer over data products; automatic transformations on consumption.
**When:** Heavy metadata complexity; semantic-driven integration. Composes with Mesh.

### Domain Topologies (9 variants)
- **Fully Federated** — no central orchestrator
- **Governed** — central distribution layer
- **Partially Federated** — central engineering for some domains
- **Hub-and-Spoke** — strict mediation
- **Centralized Domain** — domain-oriented org, centralized infra
- **Source-Aligned** — central source layer, federated consumers
- **Consumer-Aligned** — federated sources, central consumer layer
- **Coarse-Grained** — large business-unit-aligned domains
- **Value Chain-Aligned** — stream-aligned end-to-end domain

### Data Product
**Origin:** Dehghani; Strengholt elaboration.
**Structure:** Smallest independently deployable unit. Bundles data + metadata + infrastructure + code.
**Three rules:** Capture/modify only at Golden Source; new data → new ownership; don't distribute what you don't own.

### Golden Source
**Structure:** Authoritative dataset for a concept; unique within a domain.
**Rule:** Modifications happen only here, with owner approval.

### Common Driveway Pattern
**Structure:** Standardized catalog registration; domains implement integration however they like.
**When:** Heterogeneous integration styles across domains.

### Landing Zone Patterns
- Single — one zone
- Source/Consumer-aligned — two zones
- Multiple Data — by geography/risk/cost
- Multiple Management — for conflicting governance regimes

### MDM Styles (4)
- **Registry** — cross-reference table only
- **Consolidation** — analytics hub; sources unchanged
- **Coexistence** — improvements flow back to sources
- **Centralized** — transactional hub; two-way sync

### MDM Practical Tactics
- Master IDs centrally
- Bake data quality at producer
- Define ownership early
- Start narrow (5-10 entities)

### Data Catalog
**Components:** Glossary, owners, lineage, classifications, SLAs, schema, access workflow.
**Tools:** DataHub, Atlan, Collibra, Alation, Apache Atlas.

### Metalake Architecture
**Layers:** Landing → Processed → Marketplace + Knowledge Graph as semantic spine.
**When:** Heavy regulatory metadata complexity. Most don't need.

### Knowledge Graph
**Structure:** RDF/OWL or property graph for metadata semantic relationships.
**Tools:** Stardog, GraphDB, Neo4j, Neptune.
**When:** Cross-cutting metadata complexity dominates.

### Semantic Layer
**Structure:** Logical metric / entity definitions consumed by all tools.
**Implementations:** LookML, dbt Semantic Layer, Cube, AtScale.

### Federated Computational Governance
Three components: Data Contracts + Policy Automation (ABAC/OPA) + Data Contract Application (DCA).

### Data Contract
**Structure:** Schema + SLA + classifications + usage agreements.
**Standards:** Open Data Contract Standard (ODCS).
**Practice:** Versioned in Git; CI-enforced.

### ABAC (Attribute-Based Access Control)
**Components:** PEP (enforcement), PDP (decision), PIP (information), PAP (administration).
**Tools:** OPA + Rego for PDP.

### Domain Data Stores (DDS)
**Distinction:** Consumer-side store for specific use case. Not a contract-bound product.

### Integration Patterns
- REST (sync, resource-oriented)
- SOA (interface-encapsulated)
- ROA (REST + resource discipline)
- Composite Service (aggregator)
- BFF (per-frontend aggregation)
- Service Mesh (microservice infrastructure)
- Message Queue (once-delivered async)
- Event Broker (multi-consumer, lightweight)
- Event Stream (replayable log; Kafka)
- CEP (time-window correlation)
- CQRS (separate read/write)
- Service Orchestration (central)
- Service Choreography (event-driven, distributed)
- Federated Responsibility Model (logic to domains; thin integration layer)

### Distribution Patterns (6)
- Batch
- API-based
- Event-based
- CQRS
- Queue-based load leveling
- Point-to-point (exception)

### Strangler Pattern
**Origin:** Martin Fowler, 2004.
**Use:** Incremental legacy migration; route portions to new components; shrink legacy.

### Medallion Architecture
**Layers:** Bronze (raw) → Silver (cleaned) → Gold (curated/consumable).
**Implementation:** Lakehouse on Iceberg/Delta/Hudi.

### MLOps / DataOps
**MLOps:** End-to-end ML lifecycle with experimentation, deployment, monitoring.
**DataOps:** Iterative engineering practices applied to data; team autonomy.

## Cross-Reference Map

```
                       DATA MESH (architecture)
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
        TOPOLOGIES      DATA PRODUCTS    GOVERNANCE
        (9 variants)        │               │
              │             │               │
              │     LANDING ZONES    FEDERATED COMP.
              │     (single, multi)  GOVERNANCE
              │                      ┌───┬─────┬────┐
              ▼                      │   │     │    │
         INTEGRATION              CATALOG │  ABAC  CONTRACTS
         PATTERNS                          │  │     │
         (6 distribution +            METALAKE  PEP/PDP  ODCS
          12+ application)            (knowl.   /PIP/PAP
                                       graph,
                                       data fabric)

                       MDM
                       │
                  4 STYLES
                  (Registry → Consolidation
                  → Coexistence → Centralized)
```

Source: *Data Management at Scale* (Strengholt, 2nd ed.).
