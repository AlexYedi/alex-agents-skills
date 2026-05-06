# Playbook 05 — Governance / MDM Setup

Chain for setting up Master Data Management, data contracts, federated governance, or fine-grained access control. No slash command — invoked by reading this file or following from another playbook.

## When to Use

- "Set up MDM for [domain]"
- "We need data contracts"
- "GDPR / CCPA compliance for our data"
- "Fine-grained access control on [data product]"
- "Define data ownership across teams"

## When to Skip

- You're just adding column-level permissions on one table — `databases/database-designer` covers RLS directly
- You only need to define one data contract for one consumer — read `architecture/integration-patterns` and write the contract
- The org is too early for governance investment — note the debt and revisit at scale

## Sequence

| Step | Skill | Output |
|---|---|---|
| 1 | **`governance-and-quality/mdm-and-federated-governance`** | MDM style chosen (Consolidation / Registry / Centralized / Coexistence), governance model, data catalog architecture, access control model (ABAC + PEP/PDP/PIP/PAP) |
| 2 | `architecture/data-mesh-topologies` | Domain ownership context — who owns which data product? Federated governance only works if domains have clear ownership |
| 3 | `architecture/integration-patterns` | Data contracts at the boundaries — what each consumer agrees to consume, with versioning |
| 4 | `governance-and-quality/data-quality-auditor` | Verify contracts are met — audit the actual data against the declared contract |

## Decision Points

- **MDM style** (step 1):
  - **Registry** — keep operational systems as sources of truth; just point to them. Cheapest. Right when systems can't be replaced.
  - **Consolidation** — read-only golden record built from sources. Right for analytics use cases.
  - **Coexistence** — golden record + bidirectional sync. Right when downstream systems must use the same record.
  - **Centralized** — single system of record for everything. Most expensive. Right when starting fresh or consolidating after M&A.
- **ABAC vs RBAC** (step 1): start RBAC for simplicity; move to ABAC when role explosion happens (>20 roles) or when access depends on data attributes (region, classification, ownership).
- **Data contracts in YAML vs in code** (step 3): YAML for declarative + tool-readable; in-code (Pydantic / dbt schema tests) for runtime enforcement. Most teams need both.

## Pitfalls (from the skill itself)

- **YAML files alone don't change behavior.** Contracts work only with cultural buy-in.
- **MDM is a multi-year journey.** Plan for ongoing investment, not a project.
- **OPA performance** — per-query policy evaluation adds latency. Cache decisions.
- **Catalog adoption is the hardest part.** Tooling is easy; owner enrollment is hard.

## References

- `references/Data_Management_At_Scale/complete-distillation.md` — Strengholt distillation, chapters 5–7
- `governance-and-quality/data-quality-auditor/SKILL.md` — for the audit step

## Bypass Phrases

*"Just need the access control model"* / *"Skip the catalog step"* / *"Single contract for one consumer — go straight to integration-patterns"*.
