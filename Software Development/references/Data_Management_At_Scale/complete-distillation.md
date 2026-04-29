# Data Management at Scale — Complete Distillation

## 1. Source Identification
- **Title:** Data Management at Scale: Best Practices for Enterprise Architecture (2nd ed.)
- **Author:** Piethein Strengholt
- **Publisher:** O'Reilly Media, 2nd edition
- **Pages:** ~333 OCR'd
- **Distilled in this repo:** 2026-04-29
- **Skills produced:** 3

## 2. Executive Summary

Strengholt's contribution is the **topology taxonomy for Data Mesh** — Mesh isn't one architecture, it's nine. He pairs that with a federated governance toolkit (data contracts + ABAC/OPA + catalog + knowledge graph), MDM style selection (Registry → Consolidation → Coexistence → Centralized), and detailed integration patterns. His framing is regulatory-aware and pragmatic — comfortable saying "Mesh isn't right for you."

## 3. The Big Takeaways

1. **Data Mesh is a spectrum.** 9 topology variants. Pick by capability, not aspiration.
2. **Platform investment is the lever** for Mesh success. Without self-serve infrastructure, decentralization is chaos.
3. **Data product = data + metadata + infrastructure + code.** Contract-bound. Domain-owned.
4. **Three rules:** Capture/modify only at Golden Source. New facts → new ownership. Don't distribute what you don't own.
5. **MDM is narrow.** 5-10 entities. Don't unify everything.
6. **Federated governance via automation** (OPA + Rego), not committees.
7. **Data contracts are API contracts.** Versioned in Git; CI-enforced.
8. **Common Driveway pattern:** standardize endpoints, not implementations.
9. **Async by default; sync when truly required.**
10. **Metalake / knowledge graph for heavy regulatory contexts only.**

## 4. Skills Derived

| Skill | When |
|---|---|
| [`data-mesh-domain-topologies`](../../data-mesh-domain-topologies/SKILL.md) | Topology selection, landing zones, data product definition |
| [`enterprise-data-integration-and-distribution`](../../enterprise-data-integration-and-distribution/SKILL.md) | Cross-domain integration; sync vs async; CQRS; event-driven |
| [`mdm-and-federated-data-governance`](../../mdm-and-federated-data-governance/SKILL.md) | MDM style selection, catalog, ABAC, knowledge graphs |

## 5. Frameworks Index
See `frameworks.md`. 50+ frameworks covering: 9 topologies, 4 MDM styles, 6 distribution patterns, 12+ application integration patterns, ABAC/PEP/PDP/PIP/PAP, knowledge graphs, semantic layers.

## 6. Best Practices Index
See `additional-experts.md`. Topics: topology selection, data product design, MDM scoping, catalog operations, governance automation, integration pattern selection, mindset shifts, worked examples.

## 7. Decision Rules Consolidated

| Condition | Action |
|---|---|
| Greenfield, < 50 engineers | Centralized Domain Topology |
| 50-100 engineers, multiple BU | Governed Domain Topology |
| 100+ engineers, mature platform | Plan toward Fully Federated |
| Strict audit requirement | Hub-and-Spoke |
| Heterogeneous legacy sources | Source-Aligned |
| Many consumer joined views | Consumer-Aligned |
| Stream-aligned teams | Value Chain-Aligned |
| Single regulatory regime | Single Landing Zone |
| Multi-geo / multi-regulation | Multiple Landing Zones |
| First MDM | Registry style, 5 entities, 90 days |
| MDM for clean analytics | Consolidation |
| MDM for operational consistency | Coexistence (or Centralized greenfield) |
| Sync required (strong consistency) | REST API |
| Multi-consumer change feed | Event stream |
| Periodic large batch | Batch processing |
| Heavy read load | Read replica; CQRS only if replica insufficient |
| Latency < 100ms | Point-to-point (document exception) |
| Spiky traffic | Queue-based load leveling |
| Time-window correlation | CEP |
| Fine-grained access | ABAC + OPA + Rego |
| Cross-team metric drift | Adopt semantic layer |
| Metadata complexity (regulatory) | Knowledge graph + metalake |
| Provider/consumer drift | Formal data contracts in Git, CI-enforced |
| New data product | Owner first, schema, contract, then implement |
| Existing PII spread | Tokenize at ingest; ABAC for raw access |

## 8. Anti-Patterns Consolidated

- Mesh without platform (rebranding centralized DW)
- Premature Full Federation
- Domain boundaries from org chart
- Distribution layer as de facto centralized DW
- Cross-domain modifications (Golden Source rule violated)
- Federated governance with manual approval workflows
- Sync everything (cascading availability failures)
- Async cult (overhead where sync would be simpler)
- Fat ESB (logic accumulating in integration layer)
- Composite service sprawl (50 thin god-services)
- Point-to-point everywhere (N² coupling)
- Orchestration without sagas (orchestrator becomes god)
- CQRS as default (premature complexity)
- Event stream as database (slow current-state queries)
- MDM big bang (18-month projects that get canceled)
- Catalog without owners (graveyard)
- RBAC where ABAC is needed
- Data contracts as documentation only
- Semantic layer without business buy-in
- Knowledge graph as first move (premature)
- Treating DDS as data products
- Coarse-grained as compromise (rather than deliberate choice)

## 9. Worked Examples Pointer

| Example | Skill |
|---|---|
| Adopting Governed Mesh at 200-engineer fintech | `data-mesh-domain-topologies` |
| Cross-domain customer profile (per-consumer pattern selection) | `enterprise-data-integration-and-distribution` |
| Federated governance for pharma's Data Mesh | `mdm-and-federated-data-governance` |

## 10. Notable Content NOT in Skill Files

- **Service Mesh** — Strengholt covers as integration pattern; not promoted to a skill because not data-specific (general microservices concern).
- **Specific Microsoft Azure tooling** — book has chapters on Azure-specific implementations. Skipped because vendor-specific.
- **Detailed BI tool comparisons** — vendor matrix; ages fast.
- **Lakehouse architecture** — already covered in `data-storage-and-modeling-patterns` from Reis & Housley book.
- **MLOps lifecycle** — covered briefly; deeper coverage exists in the AI Engineering book skills.

## 11. Redundancy with Existing Repo Coverage

| Topic | Existing | Relationship |
|---|---|---|
| Data Mesh fundamentals | `dataops-and-modern-data-platforms` (Reis & Housley) | **Strengholt extends.** R&H introduce Mesh; Strengholt provides the topology taxonomy. Read both. |
| MDS / lakehouse | `data-architecture-frameworks`, `data-storage-and-modeling-patterns` | **Adjacent.** Strengholt's contribution is governance + topology. |
| DataOps practices | `dataops-and-modern-data-platforms` | **Strengholt complements.** Adds federated governance + ABAC layer. |
| Distributed system patterns (general) | `distributed-system-patterns` | **Adjacent.** Strengholt focuses on data-specific patterns. |

**Net assessment:** No direct overlap. Strengholt deepens Mesh + governance content from R&H.

## 12. Recommended Reading Order

For someone scoping Data Mesh adoption:
1. `data-mesh-domain-topologies` — pick a topology
2. `additional-experts.md` mindset shifts + topology selection guidance
3. `mdm-and-federated-data-governance` — governance and MDM
4. `enterprise-data-integration-and-distribution` — cross-domain wiring
5. `dataops-and-modern-data-platforms` (DE Basics book) for ops + DataOps

For an architect designing federated governance:
1. `mdm-and-federated-data-governance` first
2. `data-mesh-domain-topologies` for topology context
3. `frameworks.md` as reference

For an engineer implementing cross-domain integration:
1. `enterprise-data-integration-and-distribution`
2. Then governance + topology context as needed

## 13. When to Invoke Which Skill

| User intent | Skill |
|---|---|
| "Which Data Mesh topology fits us" | `data-mesh-domain-topologies` |
| "Define a data product" | `data-mesh-domain-topologies` |
| "Hub-and-spoke vs Mesh" | `data-mesh-domain-topologies` |
| "Should this be REST or events" | `enterprise-data-integration-and-distribution` |
| "CQRS for our system" | `enterprise-data-integration-and-distribution` |
| "Composite service vs BFF" | `enterprise-data-integration-and-distribution` |
| "MDM strategy" | `mdm-and-federated-data-governance` |
| "ABAC for data" | `mdm-and-federated-data-governance` |
| "Data contracts" | `mdm-and-federated-data-governance` |
| "Semantic layer" | `mdm-and-federated-data-governance` |
| "Knowledge graph for metadata" | `mdm-and-federated-data-governance` |

Source: *Data Management at Scale* (Strengholt, 2nd ed., O'Reilly), distilled 2026-04-29.
