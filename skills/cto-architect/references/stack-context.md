# Alex's Stack Context — Full Reference

**Last synced from STACK_README.md**: 2026-04-08
**Updates applied**: Added HubSpot (CRM), Buffer (social media), Notion (knowledge
base/database/content management). Removed ChatGPT as a model option.

Read this file when you need specifics about Alex's tools, conventions, or integration
patterns. The SKILL.md has a quick reference — this file has the details.

---

## Table of Contents

1. [Tool Inventory](#tool-inventory)
2. [MCP Connections](#mcp-connections)
3. [Tool Selection Rules](#tool-selection-rules)
4. [Infrastructure Conventions](#infrastructure-conventions)
5. [Integration Harness Patterns](#integration-harness-patterns)
6. [n8n Workflow Conventions](#n8n-workflow-conventions)
7. [Known Gaps & Planned Additions](#known-gaps--planned-additions)

---

## Tool Inventory

### AI & Reasoning

| Tool | Role | When to Use |
|------|------|-------------|
| **Claude** (Sonnet/Opus) | Primary AI brain | All reasoning, writing, code, strategy |
| **Gemini / Google AI Studio** | Secondary AI | >200k token context, Google Workspace integration, multimodal. Gemini 2.0 Flash for speed, Pro for reasoning depth |
| **Perplexity** | Research & search | Real-time web research with citations |
| **NotebookLM** | Document intelligence | Deep Q&A on large document sets |
| **ElevenLabs** | Voice & audio | TTS for demos, voiceovers, audio content |

**Model rule**: Claude is default. Use Gemini only when context exceeds Claude's window
or task requires native Google ecosystem integration. Use Perplexity for anything
requiring live web data with citations.

### Build & Development

| Tool | Role | When to Use |
|------|------|-------------|
| **Cursor** | Primary IDE | All production code. Set up `.cursorrules` per project |
| **Bolt** | Full-stack scaffolding | Rapid v0 scaffold → migrate to Cursor |
| **Lovable** | Frontend scaffolding | UI-first projects, stronger on visual polish |
| **Replit** | Sandboxed prototyping | Quick experiments only, not production |
| **Devin** | Autonomous agent | Long-horizon ambiguous tasks needing judgment |
| **Codex** | Autonomous agent | Well-scoped parallel tasks (effectively free on Pro) |
| **Factory** | Code automation | PR automation, code review workflows, CI/CD |
| **Warp** | AI terminal | Interactive real-time debugging ONLY. All other terminal work → Cursor terminal or Claude bash_tool |

### Infrastructure & Data

| Tool | Role | When to Use |
|------|------|-------------|
| **Supabase** | Primary DB + backend | Postgres, auth, storage, edge functions, pgvector |
| **Vercel** | Frontend deployment | All Next.js/React deployments (auto-deploy from GitHub) |
| **Railway** | Backend deployment | Node/Python services, workers, cron (when Vercel serverless limits hit) |
| **GitHub** | Source control | All code versioning, CI/CD |
| **n8n** | Workflow automation | All automation, agent pipelines, scheduled jobs (self-hosted on n8n.cloud) |
| **Google Antigravity** | Compute scheduling | AI/ML workload optimization on Google Cloud — infrastructure layer, not user-facing |

### CRM, Knowledge & Content Management

| Tool | Role | When to Use |
|------|------|-------------|
| **HubSpot** | CRM | Pipeline management, contact/deal tracking, sales workflow. MCP connected |
| **Notion** | Knowledge base & content | Wiki, project documentation, databases, content management. MCP connected |
| **Buffer** | Social media management | Content scheduling, cross-platform distribution |

### Analytics & Monitoring

| Tool | Role | When to Use |
|------|------|-------------|
| **PostHog** | Product analytics | Event tracking, funnels, retention, session recording, feature flags |
| **Google Sheets** | Data analysis | Metrics dashboards, financial models |

### Design & Content

| Tool | Role | When to Use |
|------|------|-------------|
| **Canva** | Visual design | Marketing assets, social graphics, brand materials |
| **Magic Patterns** | UI component design | React component generation, design system exploration |
| **Gamma** | Decks & documents | Investor decks, proposals, research briefs |
| **Framer** | Interactive prototypes | Marketing sites with animation/polish |
| **Miro** | Visual collaboration | Strategy, architecture diagrams, journey mapping |
| **Mobbin** | UI research | iOS/Android/web pattern reference |

### Product & Project Management

| Tool | Role | When to Use |
|------|------|-------------|
| **Linear** | Issue tracking (primary) | Sprints, bugs, backlog, roadmap |
| **ClickUp** | Task management (secondary) | When Linear isn't the right fit |
| **Monday.com** | Board management (secondary) | When board-style tracking is needed |
| **ChatPRD** | Product docs | PRD generation, feature specs |
| **Granola** | Meeting intelligence | Auto meeting notes, action items, transcripts |

### Input & Capture

| Tool | Role | When to Use |
|------|------|-------------|
| **Wispr Flow** | Voice-to-text | Dictation for prompts, notes, messages |
| **Google Workspace** | Docs & collab | Docs, Sheets, Slides, Gmail, Calendar |

---

## MCP Connections

These are live connections Claude can interact with directly. Always prefer MCP over
manual when a connected service is involved.

**Active connections**: Linear, Supabase, Vercel, n8n, PostHog, Google Calendar, Gmail,
Canva, Magic Patterns, Gamma, Granola, ChatPRD, Clay, ClickUp, Monday.com, Hugging Face,
Microsoft Learn, Dice, Google BigQuery, Similarweb, ElevenLabs, HubSpot, Notion.

**MCP rules**:
- Always prefer MCP over manual when connected service is involved
- Never store credentials in prompts — auth at connector level
- Flag MCP failures immediately — don't silently fall back
- n8n and Clay have the tightest rate limits — batch where possible

---

## Tool Selection Rules

### Build Decisions

| Scenario | Use | Don't Use |
|----------|-----|-----------|
| New app from scratch, fast | Bolt/Lovable → migrate to Cursor | Starting in Cursor cold |
| Production code | Cursor | Replit, Bolt |
| Quick throwaway experiment | Replit | Cursor (overkill) |
| Parallel well-scoped autonomous tasks | Codex | Devin (sequential, costs per task) |
| Long-horizon ambiguous task | Devin | Codex (less suited to ambiguity) |
| PR automation / CI/CD | Factory | Codex or Devin |
| Backend API service | Railway + Supabase edge functions | Vercel serverless (for long-running) |
| Frontend deployment | Vercel | Railway |
| Interactive terminal debugging | Warp | Cursor terminal |
| All other terminal/scripting | Cursor terminal or Claude bash_tool | Warp |

### Content & Design Decisions

| Scenario | Use | Don't Use |
|----------|-----|-----------|
| Investor deck / proposal | Gamma | Canva, Google Slides |
| Social graphics / marketing | Canva | Gamma |
| Social scheduling / distribution | Buffer | Manual posting |
| Interactive marketing site | Framer | Webflow (not in stack) |
| UI component generation | Magic Patterns | Building from scratch |
| UI research / patterns | Mobbin | Googling screenshots |
| Strategy visualization | Miro | Default for spatial thinking |
| Project wiki / documentation | Notion | GitHub markdown (for anything beyond READMEs) |

### Research Decisions

| Scenario | Use | Don't Use |
|----------|-----|-----------|
| Real-time market research | Perplexity | Claude alone |
| Deep doc analysis | NotebookLM | Uploading raw PDFs to Claude |
| Competitive traffic data | Similarweb MCP | Manual web lookups |
| Contact/company enrichment | Clay MCP | Manual LinkedIn research |
| CRM lookups / pipeline data | HubSpot MCP | Spreadsheets |

### AI Model Decisions

| Scenario | Use | Don't Use |
|----------|-----|-----------|
| Reasoning, writing, strategy, code | Claude (Sonnet or Opus) | Defaulting to Gemini |
| 200k+ token doc processing | Gemini (Google AI Studio) | Claude (context limit) |
| Voice output | ElevenLabs | Built-in TTS |
| Research with citations | Perplexity | Claude without web search |

---

## Infrastructure Conventions

### Supabase

- All tables use `snake_case`
- Every table: `id uuid`, `created_at timestamptz`, `updated_at timestamptz`
- Row Level Security (RLS) enabled by default on ALL tables
- Edge functions in TypeScript
- pgvector extension installed (embedding pipeline not yet built)

### Environment Variables

```
NEXT_PUBLIC_*           = client-safe (OK to expose)
*_SECRET_*              = server-only (NEVER expose to client)
SUPABASE_URL            = project URL
SUPABASE_ANON_KEY       = public key (safe)
SUPABASE_SERVICE_ROLE_KEY = server-only (NEVER expose)
```

Store in: Vercel UI, Railway UI, `.env.local` (gitignored). Never commit `.env` files.

### Deployment Architecture

```
GitHub (source)
  → Vercel (auto-deploy: Next.js frontends)
  → Railway (backend services, workers, cron)
  → Supabase (DB migrations via Supabase CLI)
```

---

## Integration Harness Patterns

Reusable cross-tool workflow patterns. Reference these when designing new systems.

### Research → Structure → Store → Output
```
Perplexity → Claude (synthesize) → Supabase (store) → Gamma (present)
```
Use for: competitive analysis, market research, ICP research

### Meeting → Actions → Tasks → Notify
```
Granola → n8n webhook → Claude (extract) → Linear (issues) → Gmail (summary)
```
Use for: all important meetings

### Idea → Spec → Build → Ship → Measure
```
Claude (define) → ChatPRD (formalize) → Linear (issues) → Cursor/Bolt (build)
  → Vercel/Railway (deploy) → PostHog (instrument)
```
Use for: all product feature development

### Lead → Enrich → Qualify → Outreach
```
Source → Clay (enrich) → HubSpot (store + manage pipeline) → n8n (trigger sequence)
  → Gmail (send)
```
Use for: outbound prospecting, pipeline management

### Build → Ship → Measure → Close
```
GitHub PR → Vercel (deploy) → PostHog (events) → n8n (alert on errors)
  → Linear (auto-close issue)
```
Use for: all production deployments

---

## n8n Workflow Conventions

**Instance**: `yedimaing.app.n8n.cloud`

**Naming convention**:
```
[DOMAIN]_[ACTION]_[FREQUENCY/TRIGGER]
Examples:
  GTM_ICP_enrichment_onNewLead
  Research_competitorMonitoring_weekly
  Engineering_deployNotification_onVercelDeploy
```

**The rule**: n8n is the automation hub. If a task is recurring, cross-tool, or
trigger-based, it belongs in n8n — not in a one-off script.

---

## Known Gaps & Planned Additions

### Current Gaps
- Vector search pipeline not yet built (pgvector installed, no embedding flow)
- No unified observability (logging scattered across Vercel, Railway, Supabase)
- n8n workflow library in progress (first brief ready, awaiting build)

### Under Evaluation
| Tool | Why | Priority |
|------|-----|----------|
| LangSmith | LLM call tracing and evaluation | Medium |
| Pinecone | Vector DB if pgvector insufficient at scale | Low |
| Composio | Broader agent tool connectivity | Medium |

When recommending tools in these gap areas, note the gap and whether an existing
tool can cover it temporarily vs. needing a new addition.
