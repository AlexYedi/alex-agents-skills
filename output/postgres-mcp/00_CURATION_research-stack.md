# Research Stack Curation — PostgreSQL × MCP Deep Dive

**Date:** 2026-05-28 · **Owner:** Alex Yedi · **Companion to:** `POSTGRES_MCP_DEEP_DIVE.md`

This file is the first deliverable: a reviewed, opinionated selection of the **most
valuable research plugins, skills, and agents** in this repository (plus the live MCP
servers in session) for producing an investment-grade deep dive on PostgreSQL in the
AI/agentic era. Selection criterion: *does the asset materially raise the accuracy,
structure, or judgment of the deep dive?* Everything below earned its place; the
hundreds of GTM/product/finance skills in the library did not, and are excluded.

---

## Tier 1 — Load-bearing (used directly to structure and argue the deep dive)

| Asset | Type | Why it's selected | What it contributes |
|---|---|---|---|
| `research-analyst` | Agent (`alex:research-analyst`) | Investment-grade research posture: lead with the insight, distinguish signal from noise, flag confidence, recommend next action. | The deep dive's **output discipline** — conclusion → evidence → caveats, confidence flags (High/Med/Low), tables over prose. |
| `rag-and-agent-architecture` | Skill | Chip Huyen's RAG-vs-Agents-vs-Full-Context decision frame + the 4-stage RAG pipeline. | The spine of "**why agents touch databases at all**" — and where Postgres sits in retrieval vs action. |
| `structured-vs-unstructured-retrieval` + `data-engineering:design-retrieval` | Reference + slash-command (plugin) | One-page decision aid: KG vs RAG vs **text-to-SQL** over relational data. | Frames Postgres as the **text-to-SQL + hybrid-retrieval substrate**, not just an OLTP store. |
| `scalable-database-design-and-sharding` | Skill | Gorton's scaling lineage (scale-up → replicas → shard), SQL-vs-NoSQL, CAP as a tunable knob. | Positions Postgres against the **"specialized datastore" alternatives** the everything-database thesis displaces. |
| `database-designer` | Skill | Schema/index/RLS/multi-tenancy patterns (POWERFUL tier). | The concrete **agent-facing schema discipline**: RLS isolation, surrogate keys, audit trails, index strategy. |
| **Supabase MCP server** | Live MCP (in session) | First-party, Postgres-backed MCP: `list_tables`, `execute_sql`, `apply_migration`, `get_advisors`, branching, `read_only`/`project_ref`/`features`. | The **primary worked example** of Postgres × MCP, including its threat model (prompt injection, read-only, scoping). |
| **Azure Database for PostgreSQL MCP** | Live MCP (Microsoft Learn docs) | Enterprise pattern: Foundry agent → Container Apps MCP server → Postgres via Entra ID + managed identity; per-tool Destructive/Read-Only annotations. | The **enterprise-governed** counterpoint to Supabase's developer-tool posture. |

## Tier 2 — Supporting (consulted for depth on specific sections)

| Asset | Type | Role in the deep dive |
|---|---|---|
| `cto-principal-architect` | Agent | Architectural judgment on build-vs-buy, "Supabase (Postgres) as default stack," MCP architecture. Explicitly names MCP + Supabase in Alex's reference stack. |
| `systems-analyst` | Agent | Second-order/ecosystem reasoning for the "everything database" and lethal-trifecta security dynamics. |
| `data-storage-and-modeling-patterns` | Skill | Storage-tier and consistency vocabulary (cache hierarchy, strong vs eventual) used to frame Postgres' OLTP role and agent memory. |
| `rag-architect` | Skill | Chunking/embedding/eval detail behind pgvector-based RAG. |
| `knowledge-graph-applications` / `-platform-integration` | Skills | The KG/hybrid angle (Postgres + Apache AGE, metadata graphs) and when to reach past relational. |
| `Data Engineering/retrieval/text-to-sql` | Reference + eval harness | Working text-to-SQL pipeline with a promptfoo eval suite — the agentic "write SQL" pattern grounded in runnable code. |
| `research-brief-blueprint` | Skill | Scoped the brief: business question → methods/sources → deliverable shape. |

## Tier 3 — Domain agents available but not load-bearing here

`market-research/*` (insights-research-director, quant-insights-architect),
`competitive-intelligence/*` (market-insights-director, win-loss-analyst),
`business-intelligence/*` (data-architecture-lead). Useful if this deep dive were
extended into a vendor bake-off or market-sizing study; out of scope for a technical
deep dive.

---

## The plugin itself

The repository is published as a Claude Code plugin — **`alex` v0.3.0** (see
`.claude-plugin/plugin.json` / `marketplace.json`). Skills invoke as `alex:<skill>`,
agents as `subagent_type: alex:<agent>`, and the Data Engineering chain ships as slash
commands (`/data-engineering:design-retrieval`, `:build-pipeline`, `:enrich`). The deep
dive treats the Data Engineering **retrieval chain** as the canonical lens for "where a
database meets an LLM."

## Live MCP servers in session (the "plugins" that make this topic concrete)

- **Supabase** (`mcp.supabase.com/mcp`) — managed Postgres + the reference developer-facing Postgres MCP.
- **Microsoft Learn / Azure MCP** — first-party Azure Database for PostgreSQL MCP docs.
- **Notion** (`mcp.notion.com/mcp`) — out of scope; not Postgres-related.

> **Method note (from `research-analyst`):** Every non-obvious claim in the deep dive
> carries a confidence flag. First-party docs (Supabase, Microsoft Learn) and the MCP
> specification are treated as tier-1 sources; vendor blogs and survey aggregations as
> tier-2; my own synthesis as flagged judgment.
