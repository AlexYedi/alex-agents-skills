# Playbook 01 — Greenfield Platform Architecture

End-to-end chain for designing a new data platform from a blank slate. Use when scoping the architecture before any implementation begins.

## When to Use

- "Design a data platform for [company / use case]"
- "What data stack should we adopt?"
- "We're greenfielding our analytics infrastructure"
- A new domain/product needs its own data architecture

## When to Skip

- You already know the architecture and need a specific skill (jump straight to it)
- The scope is one piece (just a schema, just a pipeline) — use playbook 02 or 03 instead
- You're optimizing an existing platform — playbook 04 (audit) is a better entry

## Sequence

| Step | Skill / reference | Output |
|---|---|---|
| 1 | `architecture/lifecycle-and-principles` | Frame: lifecycle stages, undercurrents, 9 architecture principles applied to your context |
| 2 | `architecture/architecture-frameworks` | Chosen framework (TOGAF / DAMA / AWS WA / Lambda vs Kappa / MDS vs Live Stack) with rationale |
| 3 | **Branch on org structure:** | |
|   | → `architecture/data-mesh-topologies` | If org is federated / domain-oriented |
|   | → `architecture/storage-and-modeling-patterns` | If centralized — pick warehouse vs lake vs lakehouse, model (Kimball / Inmon / Vault) |
| 4 | `architecture/integration-patterns` | Cross-domain flow: APIs, events, CDC, batch, choreography vs orchestration |
| 5 | `architecture/dataops-and-platforms` | Operating model: SLOs, semantic layer, FinOps, dbt-style analytics-as-code |
| 6 | `governance-and-quality/mdm-and-federated-governance` | MDM style + governance model + access control (ABAC) |
| 7 | Handoff to `databases/database-designer` | Implementation begins — schema, indexes, RLS, migrations |

## Decision Points

- **Mesh vs centralized** (step 3): driven by org structure, not technology. If domains can't own their own data products yet, start centralized and evolve.
- **MDS vs Live Stack vs Mesh** (step 2 / 5): batch tolerances + team maturity gate this. Don't pick Live Stack unless you have Kafka ops capacity.
- **Warehouse vs lakehouse** (step 3): if SQL is the dominant query interface and ML is secondary, warehouse. If both are first-class, lakehouse.

## Cross-folder pointers (optional)

For OLTP-side decisions encountered along the way:
- `Software Development/scalable-database-design-and-sharding`
- `Software Development/eventual-consistency-mechanics`
- `Software Development/event-streaming-with-kafka` (if Live Stack)
- `Software Development/cto-architect` (if you want a CTO-level review of the stack)

## References

- `references/Data_Engineering_Basics/complete-distillation.md` — Reis & Housley book digest
- `references/Data_Management_At_Scale/complete-distillation.md` — Strengholt book digest

## Bypass Phrases

To deviate mid-chain: *"Skip to step N"* / *"Use the [framework] approach directly"* / *"Just need [specific skill]"*.
