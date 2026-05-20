# Chapter 6 — Appendix

This appendix extends V1 Ch 6 rather than duplicating it. The V1 glossary, V1 source list, and V1 methodology notes all carry forward by reference — terms like Wardley evolution stage, OCQ scoring discipline, HBM, CoWoS, RSP, JTBD, MTEB, NCCL, MEP, PUE, conviction-star calibration, and the falsifiability protocol live in V1 §6.1–§6.3 and are not restated here. This chapter only documents the V3-specific additions: agent terminology that did not matter at full-stack resolution, agent-specific sources that augment the V1 rotation, the methodological choices unique to V3 (7 JTBD jobs not 6, memory folded into Bet #5, Bet #3 reframed, the procurement rubric as new artifact, the OSWorld sub-crux), the update protocol pointer back to V1 Ch 5, and the change log for this volume specifically. Treat it as a delta-pack against V1 Ch 6.

## §6.1 Agent-Specific Glossary

Alphabetized. Agent-specific terms only — every entry either does not exist in V1 Ch 6 or carries a materially different meaning at agent-layer resolution. Cross-reference V1 Ch 6 §6.1 for the base glossary.

| Term | Definition |
|---|---|
| A2A | Agent-to-Agent protocol; Google-announced Apr 2025 at Cloud Next. Fork-vector candidate for Crux 2. |
| Action-confirmation gate | Procurement requirement: agent surfaces a confirmation step before write/pay/send actions. §3.5 rubric item 1 and 3. |
| Agent runtime / harness | Software framework hosting the agent loop (Claude Agent SDK, OpenAI Agents SDK, LangGraph, Mastra, Pydantic AI). Ch 1 Stratum II. |
| AI Gateway | Provider-routing layer (Vercel AI Gateway, OpenRouter, AWS Bedrock, Cloudflare) exposing planner-executor splits and tier routing as config. Ch 1 Meta-C. |
| ASL-4 | Anthropic RSP capability tier four. Deployment-freeze threshold. Ch 5 §5.2 Trigger B. |
| Browser automation | DOM-level agent action surface (Playwright, Browserbase, Skyvern). Distinct from full computer use. Ch 1 Stratum VI. |
| Computer use | Pixel-level agent action surface — desktop OS via screenshots plus mouse/keyboard. Tracked on OSWorld. Ch 1 Stratum VI. |
| Episodic memory | Recall of past agent sessions — the actual memory category most enterprise buyers mean. Ch 1 Stratum IV. |
| GraphRAG | Knowledge-graph-augmented retrieval; Microsoft GraphRAG uses Leiden clustering plus community summaries. |
| HippoRAG | Hippocampal-inspired retrieval architecture. Research-stage (HippoRAG 2 paper Aug 2025). |
| Indirect prompt injection | Adversarial input arriving via tool output rather than direct user input. Unsolved threat class. §3.5 rubric item 2. |
| Knowledge-worker agent | Vertical sub-category — Glean, Hebbia, Sana, Notion AI, M365 Copilot agents. Highest hyperscaler-encroachment ranking. |
| Long-term memory | Cross-session persistent state. Folded into Bet #5 per Crux 5. |
| MCP | Model Context Protocol — Anthropic-originated, donated to Linux Foundation Agentic AI Foundation Dec 8, 2025. Ch 1 Stratum III. |
| MCP fork | Risk that a major vendor unilaterally extends MCP with proprietary schemas. Crux 2; Risk 2. |
| MCP gateway | Enterprise control plane in front of MCP servers — Cloudflare Workers AI MCP, Kong, Pomerium. Bet #3 reframe target. |
| MCP registry | Aggregated index of MCP servers. ~11,400 servers April 2026 per LF MCP registry statistics. |
| Meta-planning | Outer-loop reasoning about which planning strategy to invoke. Genesis-stage. |
| Operator translation | Translating frontier capability into specific implications for a named operator persona. Bet #6 thesis. |
| OSWorld | Computer-use benchmark. 65% on a frontier system = production-deployment threshold (V3 sub-crux). May 2026 frontier ~50–55%; human baseline ~72%. |
| Per-trajectory cost | Total inference cost across an entire agent execution. Bet #4 per-trajectory FinOps unit. Ch 1 Meta-C. |
| Planner-executor split | Route 70–85% of tokens through cheap executors; reserve expensive planners for outcome-changing calls. Ch 1 Stratum V. |
| Procurement gauntlet | The six-counterparty F1000 procurement cycle (InfoSec, Legal, Privacy, AI Governance, Procurement, business sponsor) plus the seven agent-specific overlays. Bet #1 target. |
| Procurement rubric | Agent-specific seven-overlay checklist appended to Bet #1 Playbook. New V3 artifact (Ch 3 §3.5). |
| ReAct | Reasoning-and-Acting interleaved prompting (Yao et al., Oct 2022). Still the dominant production loop. |
| Realtime API | Low-latency speech-to-speech surface (OpenAI Realtime, Gemini Live, ElevenLabs Conversational). Voice-agent substrate. |
| Reproducible eval report | Signed eval report with model pin, dataset hash, harness version, chain-of-custody. §3.5 rubric item 5. |
| RevOps agent | Vertical sub-category — Clay, 11x, Regie, Artisan. Most over-funded under-performing segment. |
| Sandbox | Ephemeral compute environment for agent code execution (E2B, Modal, Vercel Sandbox, Daytona, Replit). |
| Sub-agent privilege separation | Multi-agent architecture where downstream sub-agents run with reduced permissions at the runtime layer. §3.5 rubric item 4. |
| Telephony integration | Voice-agent connection to phone networks via Twilio, Telnyx, LiveKit Cloud. |
| Test-time compute | Inference-time reasoning budget. Brackets: <2K linear; 2–8K sweet spot; 8–32K diminishing; >32K overthinking. |
| Tool boundary | Written tool-by-tool authority list — unsupervised / approval-required / blocked-when-tainted. §3.5 rubric item 1. |
| Trajectory | Full sequence of agent actions from goal to completion. Agent-layer unit of analysis. |
| Trajectory eval | Evaluation against the full action sequence rather than final-output alone. |
| Tree-of-thoughts (ToT) | Planning architecture exploring reasoning branches in parallel. Mostly displaced by planner-executor splits in production. |
| Vertical agent | Domain-specific agent product — coding, CX, knowledge, legal, healthcare, RevOps, finance, creative. Ch 1 Stratum IX. |
| Voice agent | Speech-to-speech agent over phone or in-app voice (Vapi, Retell, Bland, ElevenLabs Conversational). Sub-800ms is the 2026 quality threshold. |
| WebArena | Browser-agent benchmark. Frontier ceiling high 60s to low 70s May 2026; human ~78%. |
| Working memory | Orchestrator state during a single agent run. Distinct from episodic / semantic / procedural memory. |

## §6.2 Agent-Specific Sources & Further Reading

V1 Ch 6 §6.2 covers the field-wide rotation (IEA Electricity, EPRI, PJM, NVIDIA earnings, SemiAnalysis, Air Street State of AI, Pallet, Stratechery, Latent Space, the framework lineage books). Carry that rotation forward unchanged. V3 adds the agent-specific layer below; aim for a combined rotation of six to eight sources well.

### Agent benchmark and capability sources

- **OSWorld and WebArena leaderboards** — computer-use and browser-agent reliability. 65% on OSWorld is the V3 sub-crux watch.
- **GAIA, BrowseComp, AndroidWorld, ScreenSpot-Pro** — companion deep-research, browser, mobile, and screen-grounding benchmarks.
- **TAU-bench / τ²-bench** — Sierra-co-authored, vendor-aligned.
- **SWE-Bench Verified and SWE-Bench Live** — coding-agent capability; Live is the cleaner number.
- **Hugging Face Agents leaderboard** — aggregated agent reliability.
- **METR** — agent capability and time-horizon doubling research. Cite, do not procure.
- **Artificial Analysis** — independent model benchmarks; agent-relevant latency and cost trade-offs.
- **Anthropic RSP updates** — v3.0 effective Feb 24, 2026; v3.1 effective Apr 2, 2026. ASL-4 watch.
- **OpenAI Preparedness Framework v2** — Apr 15, 2025; adjustment-clause language is Risk 3 trigger.
- **Google DeepMind Frontier Safety Framework** — Critical Capability Levels.

### MCP ecosystem sources

- **Linux Foundation Agentic AI Foundation** — MCP governance home since Dec 8, 2025. TSC seats: Anthropic, Microsoft, Google, OpenAI, Hugging Face, Cloudflare.
- **MCP Registry** — server count and quality bimodal signal.
- **Anthropic MCP docs** — primary spec reference.
- **OpenAI Responses API docs** — for tracking proprietary tool-use divergence (Crux 2 leading indicator).
- **Google A2A docs** — adjacent protocol; fork-vector candidate.

### Regulatory primary sources (agent-specific)

- **EU AI Act Article 14** — human-oversight requirements; April 2026 Commission draft.
- **EU AI Act Article 55** — GPAI obligations binding Aug 2, 2025; conformity drafts Feb 2026.
- **California SB 53** — Transparency in Frontier AI Act; effective Jan 1, 2026.
- **US state-level agent disclosure** — Colorado SB 24-205 (effective Feb 1, 2026); Texas (TODO per V1 §6.2); NY S5641.
- **Trump December 2025 EO** on state-law preemption.
- **Sectoral overlays** — HIPAA, GLBA, TCPA, FDA SaMD.

### Agent-specific company watchlist

One-line "watch via" per row. Use alongside the V1 watchlist.

- **Anthropic, OpenAI, Google DeepMind** — company blogs plus founder X feeds; Stratum I + Meta-A.
- **Sierra, Decagon, Glean, Harvey, Hippocratic, Abridge** — vertical-agent ARR cadence; Bet #2 leading indicators.
- **Hebbia, Rogo, Clay, Runway, Ramp AI org** — NYC vertical-agent cluster for Bet #2.
- **Cursor (Anysphere), Cognition (Devin/Windsurf), Augment, Lovable** — coding agents.
- **Mistral** — EU sovereign agent watch (Meta-D).
- **ElevenLabs** — voice-infra dual-motion.
- **Cloudflare MCP / AI, Kong, Pomerium** — gateway control-plane; Bet #3 reframe validation.
- **Vercel** — Sandbox, AI Gateway, Workflow DevKit.
- **LangChain Inc.** — LangSmith margin-layer signal.
- **Mem0, Letta, Zep** — Crux 4 directional signal via funding.
- **Lakera** — runtime safety; adaptive-adversary numbers honesty.
- **Braintrust, LangSmith, Langfuse, Galileo** — eval consolidation watch.
- **Inspect AI (UK AISI)** — cited in EU AI Act conformity drafts.
- **METR, Apollo Research, Pattern Labs** — third-party eval.
- **Frontier Model Forum** — joint publications.

### Agent-specific newsletters and press

- **Latent Space (swyx)** — agent-specific deep dives.
- **Air Street Press (Nathan Benaich)** — agent-layer coverage; RAAIS NYC June.
- **Sam Bhagwat (Mastra)** — TypeScript-side agent ecosystem.
- **Pallet's agent-specific role aggregations** — talent-flow primary surface.
- **AI Hub Live (NYC events)** — Mayor + Cornell Tech demos.
- **The Information (Stephanie Palazzolo)** — vertical-agent ARR leaks.
- **Lexicate** — legal-tech agent watch.

Discipline (V1 §6.2 carries over): six to eight sources well, not thirty poorly. Retire two and add two each twice-yearly refresh.

## §6.3 Methodology Notes (V3-Specific)

V1 Ch 6 §6.3 covers field-wide methodology (meta-strata wrap not stack, /15 OCQ, conviction-star calibration, falsifiability, time-discipline on numbers). Those carry forward unchanged. Below: V3-specific decisions only.

### §6.3.1 Why 14 agent sub-strata (10 + 4 meta) and not V1's 18

The agent layer at higher resolution has 10 distinguishable bands plus 4 meta. Some V1 strata have no agent-layer equivalent — V1 Stratum I (Power) affects agent economics via Meta-C (per-trajectory cost) rather than its own band; V1 Networking and Storage collapse into Meta-C because the buyer interacts with them as a cost line. 10+4 is the minimum stratification that keeps Bets #1–#5 legible without forcing one band to carry three bets.

### §6.3.2 Why 7 JTBD jobs in V3 versus 6 in V1

Different unit of analysis. V1 jobs are AI-field-ecosystem-level; V3 jobs are agent-augmented-workflow-level. Cross-walk: V3 Job 6 (procurement) is the agent-narrowing of V1 Job 4; the other six V3 jobs are agent-specific and not present in V1 because V1's monolithic ecosystem framing hides them. Seven jobs is the right granularity for surfacing Job 6 as PRIORITY loading Bet #1 — a six-job framing would collapse Job 6 into a broader procurement job and lose the agent-specific procurement scar tissue that makes it claimable.

### §6.3.3 Why Bet #3 was reframed (deepest delta in V3)

At V1 framing Bet #3 was "productized MCP servers for enterprise SaaS." That scored well on OCQ Opportunity but failed the 7 Powers screen at agent-layer resolution. The B6 analysis (Ch 2 §2.3) shows the durable power at the MCP layer sits at the gateway control plane (Cloudflare, Kong, Pomerium) — Switching Costs via auth, audit, rate-limit, secret-injection — not in productized servers. Productized MCP servers face commoditization the moment Salesforce or HubSpot ships first-party. The reframe — advisory plus gateway-adjacent — trades upside for substantially higher durability across both Crux 2 outcomes.

### §6.3.4 Why memory was folded into Bet #5 (not standalone)

Crux 5 (long-term memory: standalone or absorbed) has a directional answer at V3 resolution. Consumer / prosumer memory is being absorbed by labs (Claude Projects GA April 2026; ChatGPT memory; Gemini Workspace personalization March 2026). Compliance / enterprise memory remains niche-standalone (Zep cleanest read; Mem0 and Letta likely consolidation). The niche-standalone tier is too thin for a standalone Bet. Folded into Bet #5 as a service line — same buyer, same engagement, no separate distribution build.

### §6.3.5 The Procurement Rubric as new V3 artifact

Ch 3 §3.5 is the agent-specific section of Bet #1's Playbook. It exists because V1's procurement playbook is for AI vendors generally; the agent context adds seven overlays — tool-boundary policy, indirect-injection adaptive red-team, action-rollback documentation, sub-agent privilege separation, signed reproducible eval reports, EU AI Act Article 14 tie-out, sectoral overlays. The rubric is the demo the Playbook ships with; F1000 AI Governance is the primary reader; the Job 6 phase map is the structure. By design it is the most-robust artifact in the portfolio across all five cruxes (Ch 3 §3.6).

### §6.3.6 The OSWorld sub-crux

Added in Ch 3 §3.3 as a sub-crux feeding Cruxes 2 (inference compute) and 5 (memory). 65% reliability is the production-deployment threshold for computer-use agents — below means hard to sell to enterprise back-office, above means vertical-agent product timing accelerates by ~2 quarters. The answer-event is a single public scoreboard crossing — high decidability, high asymmetry, modest bet-size impact. That profile makes it worth its own trigger-based ritual (Ch 5 §5.2 Trigger A) rather than a buried leading indicator.

### §6.3.7 Why V3 defers most rituals to V1 Ch 5

Avoid ritual fragmentation. The cadences are the same (weekly / bi-weekly / monthly / quarterly / twice-yearly); V3 adds three trigger-based items (OSWorld, ASL-4, MCP governance) plus a quarterly delta-audit plus a twice-yearly composability check with Volume IV. New rituals would create maintenance burden without operational benefit. V3 Ch 5 footprint is roughly twenty minutes per year on top of V1 — by design.

## §6.4 Update Protocol

Defers to V1 Ch 5 §5.1–§5.4 for cadences and to V1 Ch 6 §6.4 for the version-bump rule. V3 rides alongside V1 — when a monthly conviction ritual fires in V1, it fires in V3 if any V3 bet conviction or status moved. Bi-weekly tracker syncs touch V3 §4.3 and §4.4 on the same cadence as V1 §4.3 / §4.4; the monthly conviction ritual re-rates V3 §4.2 with a parallel V1 §4.2 update written in the same session. The quarterly deep review appends the V3 delta-audit (Ch 5 §5.1); the twice-yearly major refresh appends the V3 composability check with Volume IV (Ch 5 §5.3). Trigger-based events live in V3 Ch 4 §4.8 and §4.9.

Divergence rule: if V3 logs a bet conviction change without the parallel V1 §4.2 update in the same session, the two trackers have diverged — fix the gap before the next monthly. Most likely V3 major-version trigger: Crux 5 resolving "standalone" for memory (re-elevates Bet #5's memory service line into a standalone bet) or Crux 3 resolving "MCP fork" (kills Bet #3 in its productized form).

## §6.5 Change Log (V3-Specific)

V1 changes log in V1 Ch 6 §6.5; do not duplicate.

| Date | Version | Change | Driver |
|---|---|---|---|
| 2026-05-20 | 1.0 | Initial V3 consolidation: merged AI_AGENTS_REPORT, AI_AGENTS_ADDENDUM (Parts VI–XIII), AI_AGENTS_TRACKER, AI_AGENTS_MASTER_READTHROUGH, and 11 plates into 7 chapters + 5 SVG plates + EPUB. Built on V1 Ch 5 rituals; added V3 trigger-based layer (OSWorld, ASL-4, MCP governance) plus quarterly delta-audit and twice-yearly V4 composability check. New artifact: agent-specific procurement rubric (Ch 3 §3.5). Bet #1 sequenced first; Bet #3 reframed to advisory + gateway-adjacent; Bet #4 split per-token + per-trajectory; Bet #5 absorbs memory; OSWorld added as sub-crux feeding Cruxes 2 and 5. | Reduce friction; make the agent-layer view actionable on top of V1. |
| _next_ | _next_ | _Bi-weekly: tracker syncs do not log here. Monthly: only if conviction changed. Quarterly: yes, delta-audit per Ch 5 §5.1. Twice-yearly: composability check with V4 once `output/agents-gtm/` lands._ | — |

Most likely first row to land after 1.0: Crux 1 (Anthropic ARR) resolving Q3 2026 and propagating to Bet #2 conviction. Second-most-likely: Crux 3 (MCP commons vs. fork) resolving by EOY 2026 and re-rating Bet #3.

## Apply

Open V1 Ch 6 §6.2 sources first, then V3 §6.2. Pick one V3-specific source you do not currently follow — add it to your rotation this week. The V3 list is intentionally shorter than V1's; the agent layer moves fast enough that following five sources well beats following thirty poorly. Candidates if starting fresh: the OSWorld leaderboard (V3 sub-crux), the Linux Foundation Agentic AI Foundation announcements (Crux 2), Pallet's agent-specific role aggregations (Bet #2 leading indicator), the Cloudflare AI / MCP blog (Bet #3 reframe validation), or The Information's funding section (ARR signal). One added source this week — not five.
