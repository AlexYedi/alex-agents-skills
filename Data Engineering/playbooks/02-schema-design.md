# Playbook 02 — Schema Design

Focused chain for designing a database schema, ERD, or migration. Triggered automatically when editing `*.sql`, `migrations/*`, `schema.prisma`, or `schema.ts` files (PreToolUse hook).

## When to Use

- "Design a schema for [feature]"
- "Create an ERD for [system]"
- "Plan a migration for [change]"
- "Add multi-tenancy / soft deletes / audit trail to existing schema"
- File edits in any schema or migration directory

## When to Skip

- You're writing a single ad-hoc query (not modifying schema) — use sql-database-assistant
- You only need to look up a normalization rule — read `architecture/storage-and-modeling-patterns` directly
- The change is a one-line column addition with no downstream impact

## Sequence

| Step | Skill | Output |
|---|---|---|
| 1 | `architecture/storage-and-modeling-patterns` | Chosen model (Kimball star / Inmon 3NF / Data Vault / SCD type) with rationale — *theory* |
| 2 | `databases/database-designer` | Schema (tables, columns, types, constraints), indexes, RLS policies, migration plan, seed data — *implementation* |
| 3 | `governance-and-quality/data-quality-auditor` | Post-build profile: confirm distributions, nulls, and constraints behave as expected on real data |

## Cross-cutting checks built into step 2

The `database-designer` SKILL.md already covers:
- Multi-tenancy (`organization_id` on every tenant-scoped table)
- Soft deletes (`deleted_at` with partial index)
- Audit trail (`created_by`, `updated_by`, timestamps)
- Optimistic locking (`version` column for concurrent writers)
- Row-Level Security (RLS) policies for app-role access control
- Index every foreign key

If you're skipping step 2 and going direct, at least skim that skill's "Cross-cutting Schema Concerns" section.

## Decision Points

- **SCD type** (step 1): type 1 if no history needed, type 2 for full history (most common for dim tables), type 3 only when history is bounded to current+previous.
- **UUID vs CUID vs sequential ID**: never sequential for client-exposed IDs (leakage). UUIDv7 or CUID2 are the safe defaults.
- **RLS at app-layer or DB-layer**: DB-layer (RLS policies) is the right answer for multi-tenant — app-layer filtering is one bug away from a tenancy breach.

## References

- `databases/database-designer/references/full-schema-examples.md` — worked example for a multi-tenant SaaS
- `databases/database-designer/references/normalization_guide.md`
- `databases/database-designer/references/index_strategy_patterns.md`
- `databases/database-designer/references/database_selection_decision_tree.md`

## Bypass Phrases

To skip the chain when the hook fires: *"Just write the migration — no playbook"* / *"Skip the audit step"* / *"Just use database-designer directly"*.
