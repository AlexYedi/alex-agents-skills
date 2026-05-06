# Data Engineering Playbooks

Documented chains across the Data Engineering skills, agents, and references. Each playbook walks an end-to-end workflow with handoffs between skills — they don't duplicate skill content, they sequence it.

**Important framing:** Playbooks are *defaults to deviate from*, not workflows to march through. Real work zigzags. Use a playbook to find the right entry point, then deviate when the work demands it.

## Playbook Index

| # | Playbook | When to use | Has slash command? |
|---|---|---|---|
| 1 | [Greenfield platform](01-greenfield-platform.md) | Designing a new data platform from scratch | `/data-engineering:design-platform` |
| 2 | [Schema design](02-schema-design.md) | Designing a database schema, ERD, or migration | (hook auto-suggests) |
| 3 | [Pipeline build](03-pipeline-build.md) | Building or operating a production pipeline | `/data-engineering:build-pipeline` |
| 4 | [Quality audit](04-quality-audit.md) | Auditing data quality and remediating issues | (hook auto-suggests) |
| 5 | [Governance setup](05-governance-setup.md) | Setting up MDM, contracts, governance, access control | (no command) |
| 6 | [Retrieval architecture](06-retrieval-architecture.md) | Building RAG, knowledge graph, or text-to-SQL | `/data-engineering:design-retrieval` (hook also auto-suggests) |
| 7 | [Data enrichment](07-data-enrichment.md) | Enriching contacts, accounts, or building intelligence | `/data-engineering:enrich` |

## How Invocation Works

- **Slash commands** (chains 1, 3, 6, 7): explicit invocation — type `/data-engineering:<chain>` to walk a chain step-by-step.
- **Hook auto-suggestions** (chains 2, 4, 6): when you describe a task matching a chain's trigger pattern, a system reminder injects a pointer to the playbook. You can bypass by naming a specific skill ("just use database-designer") or saying "skip the playbook."
- **Manual reading**: open any playbook and follow the sequence yourself.

## Bypass

Every playbook has a "When to skip" section. The general rule: if you already know which single skill answers your question, just invoke it directly. Playbooks earn their cost when work spans multiple skills.

## Future Migration

Hooks and slash commands are currently project-level (`<repo>/.claude/settings.json` and `<repo>/.claude/commands/data-engineering/`). When this folder migrates to a standalone repo as a Claude Code plugin, both move into `Data Engineering/.claude-plugin/` to travel with the folder. See the v2 TODO in the bundle READMEs.
