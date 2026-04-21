# STACK_README.md
**Owner:** Alex — Lead Enterprise Account Director / AI Builder  
**Last Updated:** 2026-03-23  
**Version:** 1.0  
**Purpose:** Single source of truth for all tools, integrations, MCP connections, automation workflows, and architectural decisions. Upload this file into every Claude Project so all role modules have full stack awareness.

---

## Table of Contents

1. [Stack Overview Map](#1-stack-overview-map)
2. [Tool Inventory by Category](#2-tool-inventory-by-category)
3. [MCP Connections Index](#3-mcp-connections-index)
4. [n8n Workflow Registry](#4-n8n-workflow-registry)
5. [Data & Infrastructure Architecture](#5-data--infrastructure-architecture)
6. [Claude Projects Structure](#6-claude-projects-structure)
7. [Tool Selection Rules](#7-tool-selection-rules)
8. [Integration Harness Patterns](#8-integration-harness-patterns)
9. [Decision Log](#9-decision-log)
10. [Known Gaps & Planned Additions](#10-known-gaps--planned-additions)

---

## 1. Stack Overview Map

```
┌─────────────────────────────────────────────────────────────────┐
│                        INPUTS & CAPTURE                         │
│  Wispr Flow (voice) · Granola (meetings) · Perplexity (research)│
│  NotebookLM (doc analysis) · Google Workspace (docs/sheets)     │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      AI BRAIN LAYER                             │
│  Claude (primary) · Gemini / Google AI Studio (secondary)       │
│  ElevenLabs (voice/audio output)                                │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                   ORCHESTRATION & AUTOMATION                    │
│              n8n (central automation hub)                       │
│         triggers → workflows → tool calls → outputs            │
└──────┬──────────────────────┬────────────────────────┬──────────┘
       │                      │                        │
┌──────▼──────┐    ┌──────────▼────────┐    ┌─────────▼──────────┐
│   BUILD     │    │    MANAGE         │    │    DISTRIBUTE       │
│             │    │                   │    │                     │
│ Cursor      │    │ Linear (issues)   │    │ Vercel (deploy)     │
│ Replit      │    │ ChatPRD (docs)    │    │ Railway (backend)   │
│ Bolt        │    │ Miro (strategy)   │    │ GitHub (source)     │
│ Lovable     │    │ Notion (wiki)     │    │ Supabase (DB/auth)  │
│ Framer      │    │ PostHog (metrics) │    │                     │
│ Devin       │    │ Granola (notes)   │    │                     │
│ Factory     │    │                   │    │                     │
└─────────────┘    └───────────────────┘    └────────────────────┘
       │
┌──────▼──────────────────────────────────────────────────────────┐
│                    DESIGN & CONTENT                             │
│  Canva · Magic Patterns · Gamma · Mobbin · Miro · Warp          │
└─────────────────────────────────────────────────────────────────┘
```

**The rule:** n8n is the automation hub. Supabase is the data layer. Claude is the reasoning layer. Everything else is a specialized tool that feeds into or out of those three.

---

## 2. Tool Inventory by Category

### 🤖 AI & Reasoning

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Claude** | Primary AI brain | All reasoning, writing, code review, strategy, coaching | Claude.ai Projects + API via artifacts |
| **Gemini / Google AI Studio** | Secondary AI | Long-context document processing, Google Workspace integration, multimodal tasks | Use when >200k token context needed or deep Google integration required |
| **Perplexity** | Research & search | Real-time web research, competitive intel, market sizing, fact-checking | Preferred over web search for sourced, cited answers |
| **NotebookLM** | Document intelligence | Deep Q&A on uploaded PDFs/docs, research synthesis, podcast-style summaries | Best for processing large document sets |
| **ElevenLabs** | Voice & audio | TTS for demos, voiceovers, audio content generation | MCP connected |
| **Google AI Studio** | AI development environment & secondary reasoning | Gemini API access and prototyping, long-context document processing (1M+ token window), multimodal tasks (image/audio/video + text), model comparison and experimentation, Google Workspace deep integration | Use when context exceeds Claude's window, or when task requires native Google ecosystem integration. Gemini 2.0 Flash for speed; Gemini 2.0 Pro for reasoning depth. Not a replacement for Claude — a complement for specific constraints. |

### 🏗️ Build & Development

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Cursor** | Primary IDE | All serious development work; AI-assisted coding with full codebase context | Use for production code. Set up `.cursorrules` per project |
| **Replit** | Sandboxed prototyping | Quick experiments, testing concepts, sharing runnable demos | Not for production |
| **Bolt** | Full-stack scaffolding | Rapid full-stack app generation from prompts | Good for v0 scaffolds; migrate to Cursor for serious work |
| **Lovable** | Frontend scaffolding | React app generation; UI-first projects | Similar to Bolt; stronger on UI polish |
| **Devin** | Autonomous coding agent | Long-horizon coding tasks, background execution, multi-file changes | Use for well-defined tasks with clear acceptance criteria |
| **Factory** | Code automation | PR automation, code review workflows, CI/CD tasks | Integrate with GitHub |
| **Warp** | AI terminal | Terminal with AI assistance; command history and context | Replace standard terminal |

### 🗄️ Infrastructure & Data

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Supabase** | Primary database + backend | Postgres DB, auth, storage, edge functions, vector (pgvector) | MCP connected. Central data layer for all apps |
| **Vercel** | Frontend deployment | All Next.js / React app deployments | MCP connected. Auto-deploy from GitHub |
| **Railway** | Backend deployment | Node/Python backend services, background workers, cron jobs | Use when Vercel serverless limits are hit |
| **GitHub** | Source control | All code versioning, CI/CD pipelines, collaborative development | Source of truth for all code |
| **n8n** | Workflow automation | All automation, agent pipelines, tool integrations, scheduled jobs | MCP connected. Self-hosted on n8n.cloud |
| **Google Antigravity** | Compute resource scheduling & infrastructure optimization | Intelligent workload scheduling across compute resources, resource allocation optimization for AI/ML workloads, cost management for compute-intensive tasks, integration with Google Cloud infrastructure | Use when running compute-heavy AI workloads that need intelligent resource scheduling. Relevant at the infrastructure layer — not a user-facing tool. Complements Railway and Vercel for workloads that require Google Cloud's compute fabric. |

### 📊 Analytics & Monitoring

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **PostHog** | Product analytics | Event tracking, funnels, retention, session recording, feature flags | MCP connected. Instrument every shipped feature |
| **Google Sheets** | Data analysis & reporting | Metrics dashboards, financial models, data manipulation | Part of Google Workspace suite |

### 🎨 Design & Content

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Canva** | Visual design | Marketing assets, social graphics, presentations, brand materials | MCP connected |
| **Magic Patterns** | UI component design | React component generation, design system exploration | MCP connected. Use before building custom UI |
| **Gamma** | Decks & documents | Investor decks, research briefs, proposals, sales materials | MCP connected. Default for presentation-ready output |
| **Framer** | Interactive prototypes | Marketing sites, interactive demos, no-code web publishing | Use for sites that need animation and polish |
| **Miro** | Visual collaboration | Strategy workshops, journey mapping, architecture diagrams, ICP canvases | Good for async visual thinking |
| **Mobbin** | UI research | iOS/Android/web UI pattern research, design inspiration | Reference before designing flows |

### 📋 Product & Project Management

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Linear** | Issue tracking | Sprint planning, bug tracking, feature backlog, roadmap | MCP connected. Primary project management tool |
| **ChatPRD** | Product documentation | PRD generation, feature specs, product briefs | MCP connected |
| **Granola** | Meeting intelligence | Automatic meeting notes, action item extraction, summary generation | MCP connected. Run on all important calls |
| **Miro** | Strategic planning | OKRs, roadmap visualization, discovery workshops | (also listed under Design) |

### 📥 Input & Capture

| Tool | Role in Stack | Primary Use Cases | Notes |
|------|--------------|-------------------|-------|
| **Wispr Flow** | Voice-to-text | Dictation across all apps; faster than typing for longer inputs | Use for prompts, notes, messages |
| **Google Workspace** | Documents & collaboration | Docs (long-form writing), Sheets (data), Slides (presentations), Gmail, Calendar | Full suite; deep integration with Gemini |
| **NotebookLM** | Document Q&A | (also listed under AI) | |

---

## 3. MCP Connections Index

*MCP (Model Context Protocol) connections allow Claude to directly interact with these services mid-conversation.*

| Service | MCP URL | Status | What Claude Can Do | Auth Notes |
|---------|---------|--------|--------------------|------------|
| **Linear** | `https://mcp.linear.app/mcp` | ✅ Active | Create/update issues, manage sprints, query roadmap | OAuth |
| **Supabase** | `https://mcp.supabase.com/mcp` | ✅ Active | Query DB, run migrations, manage tables, deploy edge functions | API key |
| **Vercel** | `https://mcp.vercel.com` | ✅ Active | Deploy, check build logs, manage projects, get runtime logs | OAuth |
| **n8n** | `https://yedimaing.app.n8n.cloud/mcp-server/http` | ✅ Active | Trigger workflows, search workflows, get workflow details | API key |
| **PostHog** | `https://mcp.posthog.com/mcp` | ✅ Active | Query analytics, create dashboards, manage feature flags | API key |
| **Google Calendar** | `https://gcal.mcp.claude.com/mcp` | ✅ Active | Create/update/delete events, find free time, respond to invites | OAuth |
| **Gmail** | `https://gmail.mcp.claude.com/mcp` | ✅ Active | Search messages, read threads, create drafts | OAuth |
| **Canva** | `https://mcp.canva.com/mcp` | ✅ Active | Generate designs, create assets | OAuth |
| **Magic Patterns** | `https://mcp.magicpatterns.com/mcp` | ✅ Active | Create/iterate UI components, publish artifacts | API key |
| **Gamma** | `https://mcp.gamma.app/mcp` | ✅ Active | Create and update decks/docs | OAuth |
| **Granola** | `https://mcp.granola.ai/mcp` | ✅ Active | Retrieve meeting notes, search transcripts | OAuth |
| **ChatPRD** | `https://app.chatprd.ai/mcp` | ✅ Active | Create/update product documents | API key |
| **Clay** | `https://api.clay.com/v3/mcp` | ✅ Active | Enrich contacts/companies, search accounts, run subroutines | API key |
| **ClickUp** | `https://mcp.clickup.com/mcp` | ✅ Active | Task management (secondary to Linear) | OAuth |
| **Monday.com** | `https://mcp.monday.com/mcp` | ✅ Active | Board management, item tracking | OAuth |
| **Hugging Face** | `https://huggingface.co/mcp` | ✅ Active | Model search, space interaction, paper research | OAuth |
| **Microsoft Learn** | `https://learn.microsoft.com/api/mcp` | ✅ Active | Azure/Microsoft documentation search | Public |
| **Dice** | `https://mcp.dice.com/mcp` | ✅ Active | Job search | Public |
| **Google BigQuery** | `https://bigquery.googleapis.com/mcp` | ✅ Active | Data warehouse queries | OAuth |
| **Similarweb** | `https://mcp.similarweb.com` | ✅ Active | Website traffic & competitive intelligence | API key |
| **ElevenLabs** | Via Claude.ai | ✅ Active | Voice generation, music, sound effects | OAuth |

### MCP Usage Rules
- **Always prefer MCP over manual** when a connected service is involved — don't ask Alex to do things Claude can do directly
- **Never store credentials in prompts** — auth is handled at the connector level
- **Flag MCP failures immediately** — don't silently fall back to a manual workaround without telling Alex
- **Rate limits**: n8n and Clay have the tightest rate limits; batch calls where possible

---

## 4. n8n Workflow Registry

*n8n is the central automation hub. All recurring tasks, agent pipelines, and cross-tool integrations should be built here first.*

**Instance:** `yedimaing.app.n8n.cloud`

### Active Workflows
*(Update this section as workflows are built)*

| Workflow Name | Trigger | What It Does | Tools Used | Status |
|---------------|---------|--------------|------------|--------|
| *(Add as built)* | | | | |

### Workflow Naming Convention
```
[DOMAIN]_[ACTION]_[FREQUENCY/TRIGGER]
Examples:
  GTM_ICP_enrichment_onNewLead
  Research_competitorMonitoring_weekly
  JobSearch_applicationTracker_onNewRole
  Engineering_deployNotification_onVercelDeploy
```

---

## 5. Data & Infrastructure Architecture

### Primary Data Layer: Supabase

```
supabase_project/
├── auth/                    — User authentication (if applicable)
├── storage/                 — File storage (docs, assets, uploads)
├── database/
│   ├── public schema        — Application tables
│   └── extensions/
│       └── pgvector         — Vector embeddings for RAG
└── edge_functions/          — Serverless functions (TypeScript)
```

**Supabase conventions:**
- All tables use `snake_case`
- Every table has `id uuid`, `created_at timestamptz`, `updated_at timestamptz`
- Row Level Security (RLS) enabled by default on all tables
- Use edge functions for lightweight API endpoints before spinning up Railway

### Deployment Architecture

```
GitHub (source) 
    → Vercel (auto-deploy: Next.js frontends)
    → Railway (backend services, workers, cron)
    → Supabase (DB migrations via Supabase CLI)
```

### Environment Variables Convention
```
# Never commit .env files. Store in:
# - Vercel: environment variables UI
# - Railway: environment variables UI  
# - Local: .env.local (gitignored)

NEXT_PUBLIC_*     = client-safe variables
*_SECRET_*        = server-only, never exposed to client
SUPABASE_URL      = project URL
SUPABASE_ANON_KEY = public key (safe to expose)
SUPABASE_SERVICE_ROLE_KEY = server-only, never expose
```

---

## 6. Claude Projects Structure

*Each Project has a dedicated system prompt = Alex Core + Role Module. Project files = living documentation.*

### Project Map

| Project Name | System Prompt | Key Uploaded Files |
|--------------|--------------|-------------------|
| `⚙️ Build — AI Engineering & Product Dev` | Alex Core + CTO Module | `STACK_README.md`, active `schema.sql`, `architecture_decisions.md` |
| `📣 GTM — Marketing, ICP & Growth Strategy` | Alex Core + CMO Module | `STACK_README.md`, `ICP_profiles.md`, `channel_playbook.md`, `competitor_map.md` |
| `🧠 Product — Roadmap, PRDs & Feature Strategy` | Alex Core + Head of Product Module | `STACK_README.md`, `roadmap.md`, `PRD_library/`, `PostHog_event_taxonomy.md` |
| `💼 Sales — Deal Strategy & Enterprise Execution` | Alex Core + Enterprise Sales Module | `STACK_README.md`, `MEDDPICC_templates.md`, `active_accounts.md` |
| `🔬 Research — Market Intel & Competitive Analysis` | Alex Core + Research Analyst Module | `STACK_README.md`, `market_map.md`, `research_archive/` |
| `🧑‍🏫 Learn — AI Engineering & Skill Building` | Alex Core + Learning Coach Module | `STACK_README.md`, `learning_roadmap.md`, `project_log.md` |
| `💼 Career — Job Search & Positioning` | Alex Core + Career Module | `STACK_README.md`, `resume_master.md`, `target_companies.md`, `outreach_templates.md` |

### File Update Protocol
- Update `STACK_README.md` whenever a tool is added, removed, or significantly changed
- Re-upload to affected Projects after major updates
- Tag updates with date: `<!-- Updated: 2026-03-23 -->`

---

## 7. Tool Selection Rules

*When multiple tools could do a job, use these rules to pick one consistently.*

### Build decisions

| Scenario | Use This | Not That |
|----------|----------|----------|
| New app from scratch, fast | Bolt or Lovable → migrate to Cursor | Starting in Cursor cold |
| Production code, serious work | Cursor | Replit, Bolt |
| Quick throwaway experiment | Replit | Cursor (overkill) |
| Autonomous multi-file task | Devin or Factory | Manual in Cursor |
| Backend API service | Railway + Supabase edge functions | Vercel serverless (for long-running) |
| Frontend deployment | Vercel | Railway (not optimized for frontend) |

### Content & design decisions

| Scenario | Use This | Not That |
|----------|----------|----------|
| Investor deck / proposal | Gamma | Canva (not structured enough), Google Slides |
| Social graphics / marketing assets | Canva | Gamma |
| Interactive marketing site | Framer | Webflow (not in stack) |
| UI component generation | Magic Patterns | Building from scratch |
| UI research / pattern reference | Mobbin | Googling screenshots |
| Strategy visualization | Miro | Miro is the default for anything spatial |

### Research decisions

| Scenario | Use This | Not That |
|----------|----------|----------|
| Real-time market research | Perplexity | Claude alone (no live web access by default) |
| Deep doc analysis | NotebookLM | Uploading raw PDFs to Claude |
| Competitive traffic data | Similarweb MCP | Manual web lookups |
| Contact/company enrichment | Clay MCP | Manual LinkedIn research |

### AI model decisions

| Scenario | Use This | Not That |
|----------|----------|----------|
| Reasoning, writing, strategy, code | Claude (Sonnet or Opus) | Defaulting to Gemini |
| 200k+ token doc processing | Gemini (Google AI Studio) | Claude (context limit) |
| Voice output | ElevenLabs | Built-in TTS |
| Research with citations | Perplexity | Claude without web search |

---

## 8. Integration Harness Patterns

*Reusable connection patterns for common cross-tool workflows.*

### Pattern 1: Research → Structured Output → Storage
```
Perplexity (research) 
  → Claude (synthesize + structure) 
  → Supabase (store) 
  → Gamma (format for output)
```
*Use for: competitive analysis, market research, ICP research*

### Pattern 2: Meeting → Action Items → Task Management
```
Granola (meeting notes) 
  → n8n webhook trigger 
  → Claude (extract action items) 
  → Linear (create issues) 
  → Gmail (send summary)
```
*Use for: all important meetings and calls*

### Pattern 3: Idea → Spec → Build
```
Claude GTM/Product Project (define + spec) 
  → ChatPRD (formalize PRD) 
  → Linear (create issues) 
  → Cursor/Bolt (build) 
  → Vercel/Railway (deploy) 
  → PostHog (instrument)
```
*Use for: all product feature development*

### Pattern 4: Lead → Enrich → Qualify → Outreach
```
Source (LinkedIn / Dice / inbound) 
  → Clay (enrich: firmographic, contact) 
  → Supabase (store + score) 
  → n8n (trigger outreach sequence) 
  → Gmail (send personalized email)
```
*Use for: outbound prospecting, job search outreach*

### Pattern 5: Build → Ship → Measure
```
GitHub PR merge 
  → Vercel (auto-deploy) 
  → PostHog (event fires) 
  → n8n (alert if error rate spikes) 
  → Linear (auto-close related issue)
```
*Use for: all production deployments*

---

## 9. Decision Log

*Why key architectural and tool choices were made. Update when significant decisions are made.*

| Date | Decision | Rationale | What Would Change It |
|------|----------|-----------|---------------------|
| 2026-03-23 | n8n as central automation hub | Self-hosted, MCP-connected, visual, covers 80% of automation needs | If workflow complexity requires LangGraph-level agent orchestration |
| 2026-03-23 | Supabase as primary data layer | Postgres + auth + storage + vector + edge functions in one; MCP connected | If scale requires dedicated infrastructure |
| 2026-03-23 | Cursor as primary IDE | Best AI-assisted coding experience; project-wide context; `.cursorrules` support | If Devin/Factory mature enough for most coding tasks |
| 2026-03-23 | Claude as primary AI | Best reasoning, writing, and code quality; MCP ecosystem; Claude Projects | If a specific task category clearly requires another model |
| 2026-03-23 | Linear over ClickUp/Monday for issues | Faster, cleaner, better GitHub integration, engineer-preferred | If team collaboration requires more non-technical stakeholder tooling |
| *(Add as decisions are made)* | | | |

---

## 10. Known Gaps & Planned Additions

### Current Gaps
- [ ] **Vector search not yet configured** — Supabase pgvector installed but no embedding pipeline built yet
- [ ] **No unified observability** — logging scattered across Vercel, Railway, Supabase; needs consolidation
- [ ] **n8n workflow library empty** — automation patterns defined but not yet built
- [ ] **PostHog not yet instrumented** — connected but no event taxonomy finalized
- [ ] **No CRM** — Clay handles enrichment but there's no pipeline management tool for sales work

### Planned Additions (Under Evaluation)
| Tool | Category | Why | Priority |
|------|----------|-----|----------|
| LangSmith | LLM observability | Trace and evaluate LLM calls in production | Medium |
| Pinecone | Vector DB | If pgvector proves insufficient for RAG at scale | Low |
| Composio | Agent tool integrations | Broader tool connectivity for agents | Medium |
| Notion | Knowledge base | If project wikis outgrow GitHub markdown | Low |

### Tools Evaluated & Rejected
| Tool | Reason Not Adopted |
|------|--------------------|
| *(Add as evaluated)* | |

---

## Maintenance

**Update this file when:**
- A new tool is added to the stack
- An MCP connection is added, removed, or changes URL/auth
- A new n8n workflow is built and deployed
- A significant architectural decision is made
- A tool is deprecated or replaced

**Version format:** `MAJOR.MINOR` — increment MINOR for additions, MAJOR for architectural changes

**Storage locations:**
- Primary: GitHub repo root (`/STACK_README.md`)
- Uploaded to: All active Claude Projects (re-upload after major updates)
- Reference copy: Notion or Google Drive (optional)

---

*This document is a living system. The goal is that any version of Claude, in any Project, reading this file, knows exactly what you're working with and how it fits together — without you having to explain it again.*
