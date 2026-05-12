# Hard Parts Map — User-Facing Routing

This file is the **user-facing** navigation for everything derived from *Software Architecture: The Hard Parts* (Ford/Richards/Sadalage/Dehghani, O'Reilly 2021). Look up your situation here; jump to the canonical asset.

For agent-facing routing, skill `description:` triggers handle it automatically. For reference-internal navigation, see `references/software-architecture-the-hard-parts/INDEX.md`.

---

## Symptom → asset

| Your situation / question | Canonical asset | Type |
|---|---|---|
| "Should we use a saga?" | `distributed-workflows-and-sagas` SKILL | Workflow |
| "Which saga pattern fits — Epic / Phone Tag / Fairy Tale / Time Travel / Fantasy Fiction / Horror / Parallel / Anthology?" | `distributed-workflows-and-sagas` SKILL | Workflow |
| "Choreography vs orchestration?" | `distributed-workflows-and-sagas` SKILL | Workflow |
| "Should we use atomic or eventual consistency across services?" | `distributed-workflows-and-sagas` SKILL | Workflow |
| "Who owns this table?" | `data-ownership-and-distributed-data` SKILL | Workflow |
| "Two services write the same data — what do we do?" | `data-ownership-and-distributed-data` SKILL | Workflow |
| "How does a non-owner service read this data?" | `data-ownership-and-distributed-data` SKILL | Workflow |
| "Replicated Cache or Column Schema Replication?" | `data-ownership-and-distributed-data` SKILL | Workflow |
| "Strict vs loose contract?" | `service-contracts-and-coupling` SKILL | Workflow |
| "Should we use Protobuf / gRPC / OpenAPI / GraphQL?" | `service-contracts-and-coupling` SKILL | Workflow |
| "What's stamp coupling and how do we avoid it?" | `service-contracts-and-coupling` SKILL | Workflow |
| "Should we adopt Consumer-Driven Contracts (Pact)?" | `service-contracts-and-coupling` SKILL | Workflow |
| "Should we decompose this monolith?" | `architectural-quanta-and-modularity` SKILL | Workflow |
| "Is this a real microservice or a distributed monolith?" | `architectural-quanta-and-modularity` SKILL | Workflow |
| "How do we break apart this monolith?" | `service-and-data-decomposition` SKILL | Workflow |
| "Component-Based Decomposition or Tactical Forking?" | `service-and-data-decomposition` SKILL | Workflow |
| "Shared library or shared service?" | `code-reuse-in-distributed-systems` SKILL | Workflow |
| "Should we use a sidecar / service mesh?" | `code-reuse-in-distributed-systems` SKILL | Workflow |
| "How big should this service be?" | `service-granularity-forces` SKILL | Workflow |
| "Should we split this service?" | `service-granularity-forces` SKILL | Workflow |
| "How do we make a defensible architecture decision?" | `trade-off-analysis-method` SKILL | Workflow |
| "I need to write an ADR with a trade-off table" | `trade-off-analysis-method` SKILL | Workflow |
| "Read the whole book in distilled form" | `references/software-architecture-the-hard-parts/complete-distillation.md` | Reference |
| "Look up a specific named pattern" | `references/software-architecture-the-hard-parts/frameworks.md` | Reference |
| "Show me a worked example" | `references/software-architecture-the-hard-parts/sysops-squad-worked-example.md` | Reference |
| "What else should I read?" | `references/software-architecture-the-hard-parts/additional-experts.md` | Reference |
| "Re-extract the source text" | `references/software-architecture-the-hard-parts/scripts/ocr_pipeline.sh` | Script |
| "Quick saga lookup from the terminal" | `references/software-architecture-the-hard-parts/scripts/saga_picker.py` | Script |
| "Data Mesh + Data Product Quantum architecture" | `Data Engineering/architecture/data-mesh-topologies` SKILL (with Hard Parts Deepening) | Workflow |

---

## New skills derived from the book

All under `Software Development/<skill-folder>/SKILL.md`.

| Skill | Type | Steps | Source chapters |
|---|---|---|---|
| `distributed-workflows-and-sagas` | Workflow | 5 | Ch 11–12 |
| `trade-off-analysis-method` | Workflow | 5 | Ch 1, 2, 15 |
| `data-ownership-and-distributed-data` | Workflow | 2 phases × ~5 steps | Ch 6, 9, 10 |
| `service-contracts-and-coupling` | Workflow | 6 | Ch 13 |
| `architectural-quanta-and-modularity` | Workflow | 2 phases | Ch 1–3 |
| `service-and-data-decomposition` | Workflow | 2 phases | Ch 4–5 |
| `code-reuse-in-distributed-systems` | Workflow | 4 | Ch 8 |
| `service-granularity-forces` | Workflow | 5 | Ch 7 |

All 8 are workflow-structured: load the skill, get marched through numbered steps, produce an ADR at the end. Each cites the corresponding Sysops Squad ADR in the worked-example reference.

---

## Existing skills augmented (Hard Parts deepening sections)

| Skill | What was added |
|---|---|
| `distributed-system-patterns` | Replaced generic Saga blurb with the 8-saga taxonomy + pointer to sagas skill |
| `scalable-database-design-and-sharding` | Cross-service decomposition vocabulary (Ch 6) + pointer to ownership skill |
| `api-design-and-evolution` | Strict/loose, stamp coupling, semantic coupling (Ch 13) + pointer to contracts skill |
| `architecture-characteristics-and-tradeoffs` | Build-Your-Own 3-step method + pointer to trade-off-analysis-method skill |
| `architecture-styles-monolithic-and-distributed` | Quantum vocabulary + distributed monolith trap + Elephant Migration |
| `software-modularity-principles` | The six modularity drivers (Ch 3) |
| `eventual-consistency-mechanics` | Distinction between storage-level EC and business-level EC (sagas) |

Augmentations are *additive only* — no rewrites. Each appends a "Hard Parts Deepening" section at the bottom of the skill.

---

## Reference folder structure

```
Software Development/references/software-architecture-the-hard-parts/
├── INDEX.md                            ← agent-facing routing
├── complete-distillation.md            ← full book summary
├── frameworks.md                       ← every named pattern, anchored
├── sysops-squad-worked-example.md      ← running case study
├── additional-experts.md               ← adjacent reading
└── scripts/
    └── ocr_pipeline.sh                 ← reproducible OCR
```

---

## How to use this map

**Three navigation paths:**

1. **You know what you need** — look up the symptom in the table above; load the asset directly.
2. **You're an agent** — the harness loads skills automatically via `description:` triggers. You usually don't need this file.
3. **You're exploring** — start at `references/software-architecture-the-hard-parts/INDEX.md` and follow links.

**One rule:** skills are workflow-structured (they march you through a decision). References are knowledge-structured (you look things up). If you want a decision made, load a skill. If you want to learn, read a reference.

---

## What this map does NOT cover

- **Runtime resilience** (circuit breakers, bulkheads, timeouts) — use `microservices-resilience-patterns` skill
- **Storage-level eventual consistency** (N/W/R quorums, CRDTs) — use `eventual-consistency-mechanics` skill (separate problem from saga-level EC)
- **General distributed systems theory** (CAP, consensus, gossip) — use `distributed-systems-essentials` and `consensus-and-strong-consistency` skills
- **Analytical data / Data Mesh** — landed as a Hard Parts Deepening section on `Data Engineering/architecture/data-mesh-topologies` SKILL (Strengholt's taxonomy + the Hard Parts Data Product Quantum vocabulary together)

---

*Maintained as part of the Hard Parts reference distillation. Update this file when a new skill or reference is added, or when an existing one is augmented.*
