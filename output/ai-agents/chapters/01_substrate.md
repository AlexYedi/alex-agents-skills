# Chapter 1 — The Agent Sub-Strata

Volume I treated the entire AI stack as fourteen strata plus four meta. The agent layer — Stratum XIII in that taxonomy — was a single band. The repricing pressure since late 2024 has been disproportionate to that single-band treatment. Three of the seven Big Bets sit directly on this layer; the fastest enterprise-software adoption curves on record (Sierra to $175M ARR in roughly thirty-six months, Anthropic Claude Code clearing a $500M run-rate inside the parent, Microsoft 365 Copilot crossing $5B ARR) are all agent-shaped products. The single-band view is no longer enough resolution to decide where to plant a flag.

This chapter zooms the agent layer into ten numbered sub-strata wrapped by four meta-strata. The stratification is analytical, not natural — agents are one coupled system from foundation model to end-user surface. Cutting it into bands makes the binding constraints, the pricing logic, and the competitive position legible at each layer. Strata I–III are the capability substrate (foundation models, runtimes, tool-use and MCP) — the geological basement on which every agent runs. Strata IV–V are the loops of cognition (memory, planning and test-time compute) — the inner system that determines what an agent can do. Strata VI–VIII are the action and defense surfaces (action surfaces, evaluation and observability, runtime safety) — the outer surfaces by which the agent reaches into the world, is measured, and is defended. Strata IX–X are the productized layer (vertical agent products, end-user surfaces and form factor) — where dollars actually accrue. Meta-A through Meta-D wrap the column: capability-level safety regimes, regulation, economics, geopolitics — agent-specific where Volume I's were field-wide.

Each entry uses the same four-part structure as V1 Ch 1: Position, What lives there, Binding constraints, Evolution stage, What changed in the last 12 months. Treat May 2026 as "now." Plate 1 (Agent Substrate Column) is the visual key.

![Plate 1 — Agent Substrate Column](plates/01_agent_substrate_column.svg)

## Part I — The Capability Substrate

Three sub-strata form the substrate on which every agent runs: the foundation model and its agentic capability, the runtime that turns the model into a goal-directed system, and the protocol by which the system reaches out to external tools. These three are the basement of the agent layer.

### Stratum I — Foundation models as agentic engines

**Position.** The model treated strictly as an agentic engine — the multi-turn, tool-using, long-horizon capability surface, not the provider-economics layer (V1 Ch 1 Stratum IX). Depends on pretraining and post-training (V1 Ch 1 Strata VII–VIII) and on inference economics (V1 Ch 1 Stratum X). Gates the runtime above it (Stratum II) and every action surface (Stratum VI) that depends on per-step reliability.

**What lives there.**
- Claude Opus 4.5 (Nov 2025, refreshed Mar 2026): 82.8% on SWE-Bench Verified inside the Claude Agent SDK harness; ~84% TAU-bench retail; ~67% TAU-bench airline; 64K-token extended-thinking budget.
- GPT-5 (Aug 2025) and GPT-5.1 thinking (Dec 2025): 74.9% on SWE-Bench at GA, ~80% with thinking + Responses-API tool loop.
- Gemini 2.5 Pro Deep Think (Mar 2026 refresh): GAIA ~70%, BrowseComp ~50%, OSWorld ~38%; powers Project Mariner (Gemini Enterprise GA Apr 2026).
- DeepSeek R1-0528 and rumored R2: mid-fifties SWE-Bench; structured-output gap, not a reasoning gap.
- Llama 4 Maverick / Behemoth (Apr 2025): tool-use ten-to-fifteen points behind closed frontier.
- Computer-use ceiling: OSWorld at 50–55% (May 2026) against a human baseline of ~72%; WebArena high sixties to low seventies versus human ~78%.

**Binding constraints.** Error compounding on multi-step trajectories: 95% per-step reliability completes a 20-step task ~36% of the time. Until per-step reliability crosses ~99% — a 2027 question — computer-use agents stay supervised. Reasoning regression past ~32K tokens of tool traces degrades instruction-following and spikes argument hallucination. Test-time compute beyond ~8K reasoning tokens has unattractive economics on most enterprise tasks.

**Evolution stage.** Product racing toward Commodity-Utility on single-turn benchmarks (MMLU, GPQA saturated). Custom-Built at the agentic frontier — sub-agents, extended thinking, computer use are still differentiated. Genesis for any per-step reliability above ~95% on long horizons.

**What changed in the last 12 months.**
- Claude Opus 4.5 with sub-agents pattern shipped November 2025 — explicit architectural workaround for context degradation.
- GPT-5 thinking and Responses-API tool loop went GA August 2025; thinking variant December 2025.
- OSWorld crossed 50% for the first time in early 2026; human baseline 72% remains uncrossed.

### Stratum II — Agent runtimes and harnesses

**Position.** The software framework that turns a foundation model into a goal-directed system. Owns the tool-call loop, memory paging, sub-agent orchestration, retries, evals, and observability hooks. Depends on the model below (Stratum I) and on MCP (Stratum III); gates every higher sub-stratum that ships an agent loop.

**What lives there.**
- Claude Agent SDK (released Sep 2025 as `claude-agent-sdk`): sub-agents, skills, hooks, MCP-native tool calling; Python and TypeScript surfaces. Anthropic uses internally at scale; referenced in Cursor, Vercel, Replit 2026 release notes. Locks to Claude.
- OpenAI Agents SDK (shipped Mar 11, 2025 alongside the Responses API; Assistants API deprecated, final shutdown mid-2026): handoffs, guardrails, tracing dashboards; MCP support added April 2025.
- Google ADK (Apr 9, 2025 at Cloud Next, Python-first with Java added Sep 2025): bundled with Vertex AI Agent Engine and Gemini Enterprise (GA Dec 2025). A2A protocol announced same event — not yet won broad cross-vendor commitment.
- LangGraph 1.0 (GA Oct 22, 2025): model-neutral, deepest production maturity. LangChain Inc. now four products — LangChain, LangGraph, LangSmith (where margin sits), LangGraph Platform.
- Honorable mentions: Mastra (TypeScript, YC W24, the Vercel/Next.js wedge); Pydantic AI (typed-validation-first, regulated industries); CrewAI ($18M Oct 2024, multi-agent role-play); Smolagents (Hugging Face, Dec 2024); AutoGen 0.4 + AG2 fork (Nov 2024). Non-US: Manus AI (Mar 2025), Mistral Agents API (May 2025), Sarvam (Q1 2026), Aleph Alpha compliance pivot.

**Binding constraints.** The runtime is the thinnest layer of the agent stack by gross margin. Switching costs are shallow (LangGraph-to-Claude-SDK migration is a quarter). Value accrues to the model below and the application above. Sub-agents pattern is a feature, not a moat — peers converging by Q4 2026.

**Evolution stage.** Product. Lab-aligned SDKs (Claude, OpenAI, Google) are Custom-to-Product racing to Product. LangGraph is Product with margin moving to LangSmith. Splitting along the model spine, not consolidating.

**What changed in the last 12 months.**
- OpenAI Agents SDK shipped March 11, 2025; Claude Agent SDK shipped September 2025.
- LangGraph 1.0 went GA October 22, 2025.
- AutoGen split into MSR fork and community AG2 in November 2024.

### Stratum III — Tool use and the Model Context Protocol (MCP)

**Position.** The joint at which an agent reaches out of its context window into the world. Sits between the runtime (Stratum II) and every action surface and SaaS integration above (Stratum VI, Stratum IX). Before MCP, tool use was the OpenAI function-calling spec (June 2023) — proprietary, per-vendor, non-interoperable.

**What lives there.**
- MCP spec: published by Anthropic Nov 25, 2024 as JSON-RPC with Python and TypeScript SDKs and four reference servers (filesystem, GitHub, Slack, Postgres). OpenAI adopted Mar 26, 2025; Google Apr 9, 2025 at Cloud Next; Microsoft May 2025 (Copilot Studio, Semantic Kernel).
- Registry growth: ~50 servers at launch Nov 2024 → ~1,200 by Apr 2025 → 5,800 at the Linux Foundation donation Dec 2025 → ~11,400 by April 2026 per the LF MCP registry statistics.
- Quality is bimodal: long tail of toy servers plus a hardening tier of first-party from Stripe, Linear, Cloudflare, Notion, GitHub, Atlassian, Datadog, Snowflake, Databricks, ServiceNow.
- MCP gateway category — the enterprise control plane: Cloudflare Workers AI MCP (Dec 2024); Kong MCP Gateway (announced Mar 2025, GA Jul 2025); Pomerium identity-aware MCP proxy (May 2025); Anthropic remote-server pattern (Nov 2025). Analogous to the API gateway category in the REST era.
- A2A (Google) is adjacent to MCP and could fragment agent-to-agent communication along a second axis.

**Binding constraints.** The spec is held; the experience is fragmenting silently. Four fork vectors: OpenAI Responses-API native tool calls remain proprietary and many production OpenAI agents bypass MCP for latency; A2A as a parallel protocol; Anthropic `tool_use` blocks remain proprietary with translation overhead at the runtime edge; quality split between first-party servers and abandonware. By 2027, "MCP-compatible" will mean roughly what "OpenAPI-compatible" means today — a baseline, not a guarantee.

**Evolution stage.** Product for the spec (held). Custom-to-Product for MCP gateways, crossing in H2 2026. Product for first-party servers; the long tail is Custom verging on abandonware. A2A is Genesis.

**What changed in the last 12 months.**
- MCP donated to the Linux Foundation's Agentic AI Foundation on Dec 8, 2025; initial TSC seats Anthropic, Microsoft, Google, OpenAI, Hugging Face, Cloudflare.
- Kong MCP Gateway shipped GA July 2025.
- Registry crossed 11,000 servers by April 2026.

## Part II — The Loops of Cognition

Two sub-strata constitute the inner loops of a working agent: memory, by which the agent retains state across turns, sessions, users, and time; and planning-and-reasoning, by which the agent decomposes a goal into steps and decides which to take. These two layers determine whether the agent feels like a stateless function or a persistent coworker.

### Stratum IV — Memory and state

**Position.** What turns a stateless completion into a persistent assistant. Depends on the model's context window (Stratum I) and the runtime's state hooks (Stratum II); gates Stratum IX vertical products where cross-session entity reconciliation is the unit of work (CX, longitudinal health, longitudinal sales). Vendors blur five distinct concepts: context window (lab-controlled, not memory); working memory (orchestrator state); episodic memory (recall of past sessions — the actual category); semantic memory (extracted entity facts); procedural memory (learned playbooks, mostly research-stage).

**What lives there.**
- Mem0 (YC W24): $24M Series A Dec 2025 led by Basis Set with YC and Kindred; vector-plus-graph hybrid, pgvector default and Neo4j optional. Self-reported 26% lift on LoCoMo (Apr 2025).
- Letta (formerly MemGPT, Berkeley spin-out): $10M seed from Felicis and Essence Sep 2024; Series A reportedly closing ~$70M valuation. Stateful-agent-as-the-unit positioning.
- Zep with Graphiti graph engine: $15M Series A from Curiosity Lane Feb 2025; sharpest enterprise compliance positioning (SOC 2 Type II, HIPAA-ready); Athelas plus late-stage fintech logos.
- Cognee: $2.5M seed; likely consolidation outcome.
- Lab-native memory at scale: ChatGPT memory (GA paid Apr 2024, free Sep 2024); Claude Projects memory (GA Apr 2026); Gemini Workspace personalization (GA Mar 2026).
- Knowledge-graph hybrids: Microsoft GraphRAG (research Apr 2024, OSS Jul 2024, partial production at Hitachi and KPMG); LightRAG (HKU, the only graph alternative with non-trivial production beyond GraphRAG). HippoRAG, PathRAG, OG-RAG remain papers.

**Binding constraints.** The compliance and procurement wedge — where memory lives physically, who can subpoena it, GDPR Article 17 forget with auditable confirmation, EU AI Act Article 13 GPAI transparency tie-out, HIPAA, contextual integrity. Lab-native memory is opaque on deletion auditability. Most production "memory" is summarization plus a database — RAG with a write path, not a distinct primitive.

**Evolution stage.** Genesis-to-Custom for standalone vendors. Custom-to-Product for lab-native (Claude Projects, ChatGPT memory). Product for GraphRAG-class research patterns selectively used in production.

**What changed in the last 12 months.**
- Mem0 closed $24M Series A in December 2025 and added forget APIs February 2026 plus BAA enterprise tier March 2026.
- Claude Projects memory hit GA April 2026.
- HippoRAG 2 paper landed August 2025; remains research-only.

### Stratum V — Planning, reasoning, test-time compute

**Position.** How the agent decides what to do next. Depends on the foundation model's reasoning capability (Stratum I), the runtime's loop primitives (Stratum II), and the planning context loaded from memory (Stratum IV). Architectural chain is shorter than the hype suggests: ReAct (Yao et al., Oct 2022) is still the dominant production loop; most "agentic frameworks" are ReAct plus a tool schema and a state machine.

**What lives there.**
- ReAct (interleaved thought-action-observation): still the production default in LangGraph, CrewAI, Pydantic AI, Vercel AI SDK.
- Plan-and-Solve (Wang et al., May 2023): survives in coding agents and deep-research products.
- Reflexion (Shinn et al., Mar 2023): survives as the "reviewer" sub-agent in Anthropic research, Cognition Devin, Manus.
- Planner-executor split — the durable architectural idea: route 70–85% of tokens through cheap executors (Sonnet 4.5, GPT-5-mini, Gemini Flash) and reserve expensive planners (Opus, GPT-5 thinking, Deep Think) for outcome-changing calls. Shipping in Sierra, Decagon, Cognition, Cursor, Claude Code, ChatGPT Agent.
- Reasoning-model tier since Sep 2024: o1 → o3 (Dec 2024, GA Jan 2025) → Claude 3.7 extended thinking (Feb 2025) → Claude 4 / 4.5 thinking → Gemini 2.5 Deep Think (May 2025) → DeepSeek R1 (Jan 2025) → Qwen QwQ-32B (Mar 2025) → Kimi K1.5 and K2 (Jan–Jul 2025).
- Test-time compute brackets: <2K reasoning tokens large linear gains; 2–8K sweet spot for most agent tasks; 8–32K hard-task gains at 4–10× cost and 10–30s latency; >32K regresses on tasks already correct at 4K ("overthinking").
- Latency thresholds: <2s autocomplete; 2–10s "thinking" UIs; 10–60s "task" UIs; >60s requires async + notification.

**Binding constraints.** Test-time compute economics — a 10× thinking budget from `reasoning_effort=medium` to `high` typically costs 5–12× per call for a 3–10-point gain on hard subsets and 0–2 points on typical enterprise tasks. Task-class-specific, not vendor-specific. AutoGPT-style open-ended outer loops are dead in production; every serious 2026 agent runs bounded (3–7 step ReAct loop plus a reasoning model plus a verifier).

**Evolution stage.** Product for ReAct loops and reasoning models. Custom-to-Product for planner-executor split (a gateway config flag). Genesis-to-Custom for RLVR/GRPO trajectory fine-tunes inside frontier labs (Process Power inside labs, no outside-vendor expression).

**What changed in the last 12 months.**
- Claude extended thinking budget raised to 64K tokens (Sonnet 4.5 Sep 2025, Opus 4.5 Nov 2025).
- Anthropic published February 2026 extended-thinking guidance and OpenAI documented `reasoning_effort=high` "overthinking" — both publicly admit diminishing returns above ~8K.
- DeepSeek R1 (Jan 2025) demonstrated pure-RL reasoning emergence; reproduced and Apache-licensed by Qwen QwQ-32B in March 2025.

## Part III — Action and Defense Surfaces

Three sub-strata cover the surfaces by which the agent reaches into the world, the layer by which we measure whether it is doing the right thing, and the layer that defends against the consequences when it does not. These are three views of the same system seen from outside, from above, and from the threat actor's seat.

### Stratum VI — Action surfaces

**Position.** Where the agent stops being a chatbot and starts being labor. Depends on the runtime (Stratum II) and on tool-use plumbing (Stratum III); gates Stratum IX vertical products that promise outcomes rather than answers. Four families: sandboxed code execution, browser automation, full computer use, agent-outbound voice.

**What lives there.**
- Sandboxes: E2B (open-core, ~$15–25M ARR doubling YoY); Modal Labs ($50M+ combined ARR after agent-workload pivot); Daytona; Vercel Sandbox (Firecracker microVMs, GA Jan 2026); Replit Agent sandbox; Hugging Face Spaces and GitHub Codespaces re-purposed. Pattern: Firecracker + Linux + Python.
- Browser automation (DOM-level): Playwright with AI patterns as baseline; Browserbase ($50M+ ARR by Q1 2026; Stagehand wrapper; session recording, stealth); Browserless (price-led); Skyvern (vision + DOM); Anchor Browser, Hyperbrowser (2025 MCP-compatible entrants).
- Full computer use (pixel-level): Anthropic Computer Use (Oct 2024, OSWorld low 20s at launch); Claude for Chrome (preview Dec 2025, wider rollout Apr 2026); ChatGPT Agent (rebrand of Operator Jan 2025); Google Project Mariner (Gemini Enterprise GA Apr 2026); Microsoft Copilot Vision / Copilot Studio. OSWorld 50–55%, WebArena high 60s to low 70s, ScreenSpot-Pro 45–55%, AndroidWorld ~50%.
- Voice agents: Vapi ($20M+ ARR Q4 2025), Retell AI, Bland AI; LiveKit Agents (WebRTC); ElevenLabs Conversational; PolyAI, Parloa ($66M Series B 2024), Regal. Substrate: OpenAI Realtime, Cartesia Sonic-2 (~40ms first-byte), Deepgram Nova-3; telephony across Twilio, Telnyx, LiveKit Cloud. End-to-end voice-to-voice 500–800ms for best stacks.

**Binding constraints.** Computer use is demo-grade for unattended autonomous work — OSWorld 50–55% is a coin flip. Voice collapses on numeric input over phone, heavy accents, mid-utterance interruption, calls beyond five minutes. Browser automation collapses on novel SPAs, shadow DOM tricks, captcha walls, and SMS/2FA flows. Sandboxes converge on Firecracker + Linux + Python; eighteen-to-twenty-four-month commodity timer running.

**Evolution stage.** Product converging to Commodity-Utility within 24 months for sandboxes (Firecracker + Linux + Python). Product with durable operational layer on top for browsers (Browserbase + Stagehand + session recording). Custom-to-Product for voice orchestration (Vapi, Retell, Bland) with compliance as moat. Genesis-to-Custom for computer use; will not cross to Product without OSWorld at ~65%.

**What changed in the last 12 months.**
- Vercel Sandbox shipped GA January 2026 (Firecracker microVMs, AI Gateway integration).
- Claude for Chrome moved from preview to wider rollout April 2026 (paying tier).
- WhatsApp Business API opened to agentic vendors January 2026 — reshapes the voice / messaging substrate for the global majority.

### Stratum VII — Evaluation and observability

**Position.** How we know whether the agent did the right thing. Wraps every sub-stratum below; consumes traces from the runtime (Stratum II), tool calls (Stratum III), memory writes (Stratum IV), reasoning tokens (Stratum V), action calls (Stratum VI). Through 2024 this layer meant logging prompt and completion; agents broke that on four axes: trajectories not turns; replay as the debug primitive; online evaluation not just offline; cost and latency as first-class.

**What lives there.**
- Tier one (enterprise-traction): LangSmith (bundled with LangGraph 1.0 GA Oct 2025; Series C $25M Feb 2024 at ~$1B; ~$40–60M ARR Q1 2026); Braintrust (Series A $36M from a16z Jun 2024, Series B reported Q1 2026 ~$60M; evals-as-CI with Notion, Airtable, Brex); Langfuse (OSS MIT, YC W23, $4M seed + extension from Lightspeed Jul 2024; EU and regulated default); Arize Phoenix and Arize AX ($70M Series C from Salesforce Ventures Dec 2024); Galileo ($45M Series B Jun 2024, Series C reported Apr 2026 ~$60M; Hubspot, ServiceNow named Q3 2025).
- Tier two: Comet Opik (OSS Sep 2024); Confident AI / DeepEval (pytest-style); HumanLoop (UK, financial services); Patronus ($17M Series A Mar 2024, Lynx and Glider open eval models); AgentOps (OSS, CrewAI/AutoGen ecosystem); Helicone; Promptfoo (acquired by OpenAI Sep 2025); Inspect AI (UK AISI, cited explicitly in EU AI Act conformity-assessment drafts Feb 2026); METR (research, cite don't procure).
- Benchmark landscape: TAU-bench and τ²-bench (Sierra-co-authored — read accordingly); SWE-Bench Verified (Princeton + OpenAI, inflated by harness tricks); SWE-Bench Live cleaner; GAIA saturating at ~70% versus human ~92%; BrowseComp 50–55%; OSWorld and WebArena as above; SWE-Lancer earns ~$200K of $1M envelope at frontier.

**Binding constraints.** No public benchmark predicts enterprise agent ROI; they predict the ceiling of the possible. Every serious enterprise builds internal sets from production traffic (typically 200–1,000 curated trajectories). OpenTelemetry GenAI semantic conventions stabilized January 2026, killing trace-ingest lock-in; lock-in lives in evaluation logic and judge models (Braintrust YAML, Galileo metric definitions take a quarter to port).

**Evolution stage.** Product for trace ingest (OpenTelemetry GenAI). Custom-to-Product for eval platforms with eval logic as the lock-in. Custom and audit-grade for Inspect AI. Two-to-three of {Galileo, HumanLoop, Patronus, Comet, Helicone, AgentOps, Confident AI} acquired by hyperscalers or runtime vendors by end of 2026.

**What changed in the last 12 months.**
- OpenTelemetry GenAI semantic conventions stabilized January 2026.
- Promptfoo acquired by OpenAI September 2025; OSS continues but strategic neutrality is gone.
- EU AI Act conformity-assessment draft (Feb 2026) named Inspect AI explicitly — first regulatory citation of an open eval framework.

### Stratum VIII — Runtime safety and guardrails

**Position.** Defends the tool-boundary at runtime. Distinct from capability-level safety regimes (Meta-A). Sits beside evaluation (Stratum VII) and depends on tool-use plumbing (Stratum III); blocks bad outputs at action surfaces (Stratum VI) before they reach systems of record at Stratum IX. Three threat classes: direct prompt injection (largely solved at the model layer); indirect prompt injection via tool returns (unsolved); multi-turn and multi-agent injection (emerging, mostly research-stage).

**What lives there.**
- Pure-play: Lakera (Swiss, Series A $20M from Atomico Oct 2023, Series B reported Q4 2025 ~$50M; Guard + Red; Atlassian, Dropbox, Citi named Q3 2025); Protect AI (acquired by Palo Alto Apr 2025, closed Q3 2025 for ~$700M — the first big consolidation); Robust Intelligence (acquired by Cisco Aug 2024, now Cisco AI Defense); HiddenLayer ($50M Series B Mar 2024); Cranium (KPMG spin-out 2023); CalypsoAI ($23M Series B Sep 2023, federal angle); Apex Security (Sequoia seed Mar 2024, NYC).
- Hyperscaler bundles: AWS Bedrock Guardrails (PII, denied topics, Automated Reasoning for hallucination, GA Dec 2024); Microsoft Purview AI Hub and Defender for AI (Ignite Nov 2024, GA 2025); Google Vertex Safety Filters and Model Armor; Anthropic constitutional classifiers (baked in, not sold).
- Open source: NVIDIA NeMo Guardrails (Apache 2.0, 1.0 GA Apr 2026); Meta Llama Guard 3 + Llama Prompt Guard 2; Promptfoo red-team (under OpenAI); Garak (NVIDIA OSS scanner).

**Binding constraints.** Nobody is solving indirect prompt injection. Vendor "99.X% PI detection" claims are known-pattern rates; adaptive-adversary numbers fall to 60–80% (Lakera and Anthropic publicly admit this). Defense-in-depth is the only working stack: treat tool returns as untrusted; action confirmation gates for write/pay/send; output validation and schema enforcement; sub-agent privilege separation; continuous red-team.

**Evolution stage.** Custom-to-Product for the pure-plays. Most absorbed into hyperscaler bundles within 18 months — Protect AI to Palo Alto was the bell. Lakera survives as cross-cloud audit-grade specialist; Apex, Calypso, Cranium likely roll up. NeMo + Llama Guard + Promptfoo OSS floor rising and eating the bottom of paid.

**What changed in the last 12 months.**
- Protect AI acquired by Palo Alto Networks (announced April 2025, closed Q3 2025 ~$700M).
- NVIDIA NeMo Guardrails 1.0 GA April 2026.
- EchoLeak and AgentSmith-class indirect-injection proofs of concept published through 2025–2026, confirming the unsolved threat class.

## Part IV — The Productized Layer

Two sub-strata productize everything below. Vertical agent products are the domain-specific applications where enterprise dollars actually land. End-user surfaces are the form factors through which buyer, user, and regulator meet the agent. This is where Bet #2 (vertical agent GTM role) and Bet #1 (procurement playbook) most directly apply.

### Stratum IX — Vertical agent products

**Position.** Where domain workflow knowledge becomes the moat and revenue accrues to people, not chips. Depends on every sub-stratum below — model capability (I), runtime (II), MCP (III), memory (IV), planning (V), action surfaces (VI), eval (VII), runtime safety (VIII). Organized by buying motion, not technology. Nine domains define the contour.

**What lives there.**
- **Coding.** Claude Code (Anthropic, ~$500M run-rate Q1 2026, inside the $200B parent); Cursor (Anysphere, $500M+ run-rate, $9.9B valuation Jul 2025); Cognition Devin ($80–100M ARR Q1 2026, after absorbing Codeium's Windsurf residual in the $2.4B three-party deal Dec 2025); Augment ($40M ARR, $977M valuation); Replit Agent ($150M+ run-rate); Lovable (Stockholm, $80M in 12 months, $1.8B valuation); Factory; Bolt and v0; Magic.dev; Reflection.AI; GitHub Copilot Workspace. Multi-winner at prosumer, winner-take-most at enterprise (Claude Code). Outcome-pricing fails (commits/PRs resist attribution). Foundation-lab encroachment is the highest of any vertical.
- **Customer experience.** Sierra ($175M+ ARR at 4× YoY Q1 2026, $10B rumored Mar 2026); Decagon ($80M+, $4.5B Sep 2025); Cresta and Ada (stalling); Intercom Fin; Parloa (Berlin, €30M+ ARR); PolyAI; Regal (NYC, ~$40M); Forethought; Lorikeet. Two-winner segment confirmed. Per-resolution pricing standard at $1–$4 — Bret Taylor's outcome thesis most validated here. Sierra is the most aligned Bet #2 target (NYC + SF dual HQ, Stripe-Ramp-Salesforce alumni pipeline).
- **Knowledge worker / enterprise search.** Glean ($300M+ ARR Q1 2026, $7.2B Sep 2025); Hebbia (NYC HQ, $50M+ Q1 2026, $700M Jul 2024 — overdue for a raise); Sana; Mem (struggling); Notion AI; Coda AI (merged into Grammarly Dec 2024); Microsoft Copilot 365 agents. Single dominant winner (Glean) with niche players. Hebbia is the NYC-native pure-play target. Per-seat $50–$150/user/month + workflow credits. Encroachment is highest in this volume — ChatGPT Business connectors attack Glean's wedge.
- **Legal.** Harvey ($100M+ ARR Q1 2026, $5B Feb 2026, SF + NYC office); Hebbia cross-segment; Spellbook; EvenUp ($80M in PI law); Eve; Robin AI; Ironclad agent products. Winner-take-most at AmLaw 100 (Harvey owns it; Cravath, A&O Shearman, PwC Legal). Per-seat $250–$500/lawyer/month. Encroachment low — privilege, bar liability, contract-data RLHF fence the segment. Most defensible vertical in the volume.
- **Healthcare.** Hippocratic AI (NYC + Palo Alto, $50M+ Q1 2026, $2B Feb 2026); Abridge (Pittsburgh + SF, $120M+ Q1 2026, fastest healthcare-AI ramp on record, $2.75B); Ambience; Suki (stalled); Nabla (Paris); DeepScribe (slowed); Iodine Software (mature CDI); Talkdesk Healthcare. Functional split: Abridge owns hospital ambient scribing; Hippocratic owns voice-agent patient-facing workflows. Encroachment very low — HIPAA, FDA SaMD, EHR tax fence generalists.
- **RevOps and sales.** Clay (NYC HQ, $80M+ Q1 2026, $1.5B Jan 2026); 11x ($20M flat with churn — cautionary tale); Regie.ai (NYC); Artisan; AiSDR; Nooks; Common Room (Seattle); Default; Lavender; Apollo agent products. Most over-funded under-performing segment. Clay survives because moat is data orchestration, not the agent. RevOps buyers reject vendor outcome attribution.
- **Finance.** Rogo (NYC HQ, $30M+ Q1 2026, $400M Jan 2026); Hebbia cross-application; Brex AI; Ramp AI agents (NYC HQ, $13B Mar 2025 with a $20B+ raise rumored Q2 2026); FactSet AI; Bloomberg GPT-derived products. Most NYC-native segment in the volume. Per-seat heavy at $1,000–$5,000/banker/month at Rogo; per-transaction emerging at Ramp and Brex. Encroachment low at the regulated tier (FINRA, OCC, broker-dealer rules).
- **Creative and media.** ElevenLabs ($200M+ ARR Q1 2026, $3.3B Jan 2025 with $5B+ rumored); Suno ($60M+ with RIAA litigation as a structural risk); Sora-2-derived products inside OpenAI; Runway (NYC HQ Chelsea, $100M+ Q1 2026); Pika; Higgsfield; Krea. Multi-winner with sharp lane separations. Runway is the NYC creative Bet #2 target.
- **Sovereign / non-US.** Mistral Le Chat Enterprise (€600M Series C at €11B Mar 2026 — only credible non-US enterprise-agent platform, BNP, Orange, Schneider plus US F500 EU-subs on data residency); Falcon-derived sovereign in UAE via Humain; Sarvam AI and Krutrim in India; Manus AI and Coze on Feishu plus WeChat Mini-Programs in China. EU AI Act enforcement late 2026 reshapes the segment.

**Binding constraints.** Three constraints stack. First, foundation-lab encroachment (Knowledge > Coding > RevOps > Creative > CX > Healthcare > Legal > Finance) compresses moats continuously. Second, the Bret Taylor outcome-pricing thesis is segment-specific — confirmed CX, partial healthcare, failed elsewhere — and the verticals where it fails are stuck on per-seat compression. Third, enterprise procurement (Job 6 in the ecosystem JTBD set, Ch 2 §2.4) is the longest cycle in B2B AI sales — the agent-specific overlays (tool-boundary, action-rollback, sub-agent privilege, indirect-injection adversarial testing, EU AI Act Article 14 tie-out) are unowned by Vanta or Drata.

**Evolution stage.** Custom-to-Product for the leaders in each domain. Product for prosumer coding. Custom for legal, healthcare, finance — the regulatory-fenced verticals. Genesis for sovereign vertical products outside Mistral.

**What changed in the last 12 months.**
- Sierra disclosed $175M+ ARR at 4× YoY Q1 2026 (per Bret Taylor); valuation rumored at $10B (March 2026) versus confirmed $4.5B (August 2025).
- Cognition acquired Codeium's Windsurf residual in a $2.4B three-party deal December 2025 after the OpenAI deal collapsed July 2025.
- Mistral Le Chat Enterprise closed €600M Series C at €11B in March 2026 — first credible non-US enterprise-agent platform at scale.

### Stratum X — End-user surfaces and form factor

**Position.** The form factor through which the buyer, the user, and the regulator meet the agent. Wraps Stratum IX. Capability is increasingly form-factor-indifferent; humans are not. Form factor governs four things at once: adoption velocity, buyer persona, threat model, regulatory surface.

**What lives there.**
- Chat web/desktop: ChatGPT ~800M WAU (Oct 2025); Claude.ai ~30M MAU Q1 2026; Gemini web; Perplexity ~22M MAU Mar 2026.
- Mobile and on-device: ChatGPT iOS/Android ~250M MAU Q4 2025; Apple Intelligence with ChatGPT and Gemini hand-off (iOS 18.4 Mar 2026); Samsung Galaxy AI. Claude mobile feature-thin — no advanced voice, no Apple Intelligence slot.
- CLI and terminal: Claude Code (GA Feb 2025, ~$500M run-rate per Anthropic Mar 2026); OpenAI Codex CLI; Aider; Cursor CLI (Apr 2026).
- In-IDE inline: Cursor (~$500M ARR Mar 2026, $9.9B); Windsurf (under Cognition after $2.4B three-party deal Mar 2026); GitHub Copilot ($1.5B+ ARR per Microsoft FY25, ~22M paid seats Mar 2026); Cline (OSS); Augment Code.
- Agentic triggers (cron/webhook/event): n8n (€55M Mar 2025, 300K+ self-hosted); Zapier AI Actions (2.2M+ paid users, Agents GA Apr 2025); Make.com; Vercel Cron + AI Gateway; Temporal; Pipedream. EU AI Act Article 14 bites here.
- In-browser sidebar / overlay: Claude for Chrome (preview Dec 2025, wider Apr 2026); ChatGPT extension; Perplexity Comet (GA Oct 2025, 5M downloads by Mar 2026); Arc Browser AI.
- Embedded SaaS: Microsoft 365 Copilot ($5B+ ARR, ~30M paid seats Q3 FY26); Google Workspace Gemini; Salesforce Agentforce ($300M+ ARR, ~10,000 customers Mar 2026); HubSpot Breeze; Zendesk AI; Slack AI (1M+ paid seats Mar 2026).
- Remote messaging (Slack, Teams, Discord, WhatsApp, SMS, email): Glean (Slack-first $300M+); WhatsApp-native agents (Meta opened Business API to agentic vendors Jan 2026); Ramp SMS card-control agent (Feb 2026).
- Voice inbound, wearable / AR / ambient, computer-use as form factor, API/SDK: covered in detail above (Stratum VI) and in V1 Ch 1 Stratum XIV.

**Binding constraints.** Form factor outranks capability as the binding constraint for enterprise adoption. Microsoft 365 Copilot wins because it ships inside a renewal; Glean wins inside Slack because Slack DLP and audit log inherit; WhatsApp dominates the global majority. The US-coastal sequence "chat web → IDE inline → computer use" is a US-coastal narrative. Real path includes WhatsApp-native, Feishu and WeChat-native, voice-first in Hindi, Portuguese, Bahasa.

**Evolution stage.** Product for chat, IDE, CLI. Product trending Commodity-bundled for embedded SaaS surfaces. Custom-to-Product for browser sidebar (consumer) and stalled at Custom for regulated. Genesis-to-Custom for computer-use UX and ambient/wearable surfaces.

**What changed in the last 12 months.**
- Microsoft 365 Copilot crossed $5B ARR with ~30M paid seats by Q3 FY26.
- Apple Intelligence added Gemini hand-off March 2026; Anthropic talks confirmed by Bloomberg April 2026 with no ship.
- WhatsApp Business API opened to agentic vendors January 2026 — the single most under-weighted surface in US discourse.

## Part V — The Meta-Strata

Four meta-strata wrap the agent layer the way they wrap the parent stack: capability-level safety regimes, regulation, economics, geopolitics. Content is agent-specific rather than the field-wide treatment from V1 Ch 1.

### Meta-A — Capability-level safety regimes

**Position.** The lab-side regime that determines whether an agent capability tier is released, restricted, or held back. Distinct from Stratum VIII runtime defenses. Wraps Strata I, V, VI.

**What lives there.**
- Anthropic Responsible Scaling Policy and ASL framework: ASL-3 invoked for Claude Opus 4 May 2025; November 2024 RSP update binding through deployment; v3.0 effective Feb 24, 2026; v3.1 effective Apr 2, 2026.
- OpenAI Preparedness Framework v2 (Apr 15, 2025): categories of cybersecurity, CBRN, persuasion, model autonomy; adjustment clause permitting OpenAI to relax safeguards "if competitors deploy" — Volume II Risk #3.
- Google DeepMind Frontier Safety Framework (May 2024 onward): Critical Capability Levels for autonomy, biosecurity, cybersecurity, ML R&D; "pragmatic interpretability" shift.
- Pre-deployment evals: UK AISI (founded Nov 2023, renamed AI Security Institute Feb 14, 2025); US AISI (restructured early 2026 under Trump-era reorganization); METR (time-horizon doubling result the most-cited agent capability finding); European AI Office.

**Binding constraints.** Capability-level safety is the bottleneck on highest-autonomy agent products — long-horizon coding agents, computer-use systems, broad action authority. Two field-betting questions: when does ASL-4 capability emerge (Anthropic points at 2026–2027), and what happens when one lab's framework triggers a freeze while another's does not.

**Evolution stage.** Custom-Built. Standards are converging but not commodified. Anthropic holds the most defensible single-vendor position in the entire agent stack — Branding plus Process Power plus Cornered Resource (alignment researchers, ~200 globally; Jan Leike retained).

### Meta-B — Regulation

**Position.** Jurisdictional rules that bind every agent sub-stratum. Touches data (V1 Ch 1 Stratum VI), models (Stratum I), application (Stratum IX), surface (Stratum X). Where Bet #1 sits.

**What lives there.**
- EU AI Act GPAI obligations under Article 55 (effective Aug 2, 2025); first conformity-assessment guidance drafts (Feb 2026); first Article 14 human-oversight enforcement guidance (Apr 2026).
- California SB 53 (Transparency in Frontier AI Act) live January 1, 2026 — frontier-model disclosure for >10^26 FLOPs at >$500M revenue. New York S5641 and adjacent state proposals advance through 2026.
- Federal preemption volatility: Trump December 2025 EO on "Eliminating State Law Obstruction"; court rulings ongoing. Re-prices compliance practice every quarter (V1 Ch 1 Risk #4).
- Sectoral overlays: FINRA and broker-dealer rules for finance agents; HIPAA and FDA SaMD for health agents; TCPA and state consent for voice. Bartz v. Anthropic ($1.5B training-data provenance) and NYT v. OpenAI dynamic re-price vendor terms.

**Binding constraints.** Article 14 human-oversight is the most actionable near-term lever — unattended agentic systems (cron, webhook, event-driven) in regulated sectors face direct exposure. First GPAI fine expected late 2026 (Crux #4 — EU AI Act teeth or paper tiger). Either way, agent-specific procurement becomes the wedge: with teeth, a $10B+ advisory category; without teeth, niche but defensible.

**Evolution stage.** Custom-Built. Rules written, enforcement not mature. Counter-Positioning for Mistral and EU-resident challengers ("data never leaves the EU"). Procurement-grade controls sit at Genesis — no vendor ships turnkey signed eval reports plus multi-party audit plus EU AI Act conformity plus action-rollback plus adaptive-adversary red-team. Bet #1's unclaimed flag.

### Meta-C — Economics

**Position.** Capital flows and unit economics specific to agent workloads. Inverts token economics from V1 Ch 1 Meta-C — per-token pricing fell 4–10× from Q1 2024 through Q1 2026, but trajectory length grew faster.

**What lives there.**
- Per-trajectory cost curves: CX deflection 4K–25K tokens at a few cents; coding edits 30K–250K tokens at $0.20–$3; deep-research 500K–5M tokens at $1–$20.
- Planner-executor split: routes 70–85% through cheap executors (Sonnet 4.5, GPT-5-mini, Gemini Flash) and reserves the expensive planner (Opus, GPT-5 thinking, Deep Think) for outcome-changing calls. Vercel AI Gateway, AWS Bedrock, Martian, OpenRouter expose this as a first-class product.
- Outcome-based pricing: per-resolved-ticket in CX, per-encounter in healthcare scribing, per-call in voice. Bret Taylor's "outcome-based pricing is how AI eats SaaS" framing — confirmed in CX, partial in healthcare, not yet validated elsewhere. Per-seat survives where outcomes resist attribution (coding, knowledge work, finance).
- Thinking-budget economics: `reasoning_effort=medium` (~2K tokens) versus `high` (~16K) is 5–12× the call price for 3–10 points of benchmark gain on hard subsets.

**Binding constraints.** Volume I Bet #4 (Inference Cost Optimization) finds its largest cost surface inside agent workloads. Twelve-to-eighteen-month window before hyperscaler bundling (Bedrock auto-optimization, Azure routing) absorbs the layer. Hyperscaler FCF reckoning (V1 Ch 1 Risk #2) re-prices vertical-agent valuations downstream.

**Evolution stage.** Custom-Built. Per-trajectory FinOps as a procurable category is Custom; per-token FinOps is Product. Outcome-pricing infrastructure (per-resolution SLA enforcement) is Custom and a Process Power moat at Sierra.

### Meta-D — Geopolitics

**Position.** International layer over agent products, capability exports, sovereign capital. Wraps Strata I, II, IX, X. Distinct from V1 Ch 1 Meta-D in the agent-specific angle.

**What lives there.**
- Sovereign agents: Mistral Le Chat Enterprise (€600M Series C at €11B Mar 2026) selling against US incumbents on EU residency and AI Act-aligned posture; G42 (UAE, Mubadala) and Humain (KSA) extending sovereign AI thesis into the agent layer with Falcon-derived deployments and AMD MI300/350 commits.
- Sub-scale platforms: Sarvam AI ($41M at $300M Dec 2024, raise rumored Q2 2026) and Krutrim (Ola, $50M at $1B Jan 2024) in India; Manus AI (Butterfly Effect, viral Mar 2025, $500M rumored Q1 2026) and Coze (ByteDance) in China — non-investable from a US-LP perspective but real.
- Export-controls extension: US Commerce authorizations for advanced-chip exports to G42 and Humain November 2025 set the precedent. Restrictions on agent capabilities themselves (full computer use, autonomous decision-making) are a 2026–2027 regulatory front.
- Jurisdictional siting of agent workloads: where trajectories run, where memory persists, where action logs accrue — becomes a procurement lever for EU and Asian buyers comparable to data residency for SaaS today.

**Binding constraints.** Taiwan-strait stability inherits from V1 Ch 1. US-LP non-investability of Chinese verticals constrains capital flow. Counter-Positioning for Mistral (EU sovereignty), Sarvam (India), Manus (Cornered Resource on Mandarin trajectory data) is real and US-discourse-underweighted.

**Evolution stage.** Custom-Built. "Sovereign agent stack" as a procurement category is Genesis-to-Custom; EU AI Act enforcement is the catalyst that could move Mistral-equivalents to Product inside Europe.

## Apply

Pick three sub-strata you couldn't explain to a buyer in 60 seconds. Write a 2-sentence explanation of each — what it does, what depends on it. Then write the binding constraint with a 2026 number for each (e.g., "OSWorld 50–55% versus human baseline 72%"; "MCP registry ~11,400 servers April 2026 with quality bimodal"; "per-trajectory cost 4K–25K tokens for CX, 30K–250K for coding"). Re-check next month: did the constraint move? If it did, which sub-stratum above just got repriced? Rotate sub-strata next month so weak spots cycle through. This drill takes ten minutes and surfaces the layers a senior buyer or procurement committee will probe hardest — almost always the ones you handwaved through on the first pass.
