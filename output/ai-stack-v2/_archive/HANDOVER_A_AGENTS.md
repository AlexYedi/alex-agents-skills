# HANDOVER A · AI Agents and Agentic Systems — Deep-Dive Spin-Up

> **Read this in full before doing anything.** It is both a long-form executive summary of what has already been built and a complete operating brief for a new session focused specifically on AI agents and agentic systems.

**Prepared for:** Alex Yedi · Lead Enterprise Account Director / AI Builder · NYC
**Prepared by:** the prior session, the one that built the SUBSTRATE atlas and Decisions Playbook
**Date prepared:** 2026-05-12
**Working directory for this new session:** `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents/` (create it)
**Inheriting from:** `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-stack/` (read-only)

---

## 1. The long-form executive summary

### What this is, in plain prose

The prior session produced a foundation-grade analysis of the entire AI stack from the power grid to the end user. Three volumes of work: a visual atlas (eleven plates plus a master synthesis plate), a foundation report and a decisions-playbook addendum totalling roughly twenty-seven thousand words of structured prose, and a living tracker that the field updates monthly. The full inventory and references are in §3 below.

That body of work treated the AI stack as eighteen strata: fourteen layers from power up through user, plus four meta-strata of safety, regulation, economics, and geopolitics. Five analytical frameworks were applied in sequence — the OCQ × Layer Matrix, Wardley Mapping, Helmer's 7 Powers, Ecosystem-level JTBD, and the empirical Talent and Capital Flow tracker. The convergence across those five frameworks identified seven cross-layer bets, five structural risks, and five unresolved cruxes that re-rank everything. The conclusion, in one sentence that ended up on the master plate, was that the highest-leverage opportunity for someone with Alex's exact profile — twelve years of enterprise B2B fluency, growing AI-builder practice, NYC location, active job search for AI-native GTM roles — is to plant a flag at the intersection of enterprise AI procurement, vertical agent go-to-market, and operator translation, three positions that compound and that fewer than fifty people on Earth are structurally able to occupy.

That conclusion has a tell. Three of the seven Big Bets named in the prior work touch the agent layer directly. Bet #2 is "Vertical Agent GTM Leadership Role" — taking a Director or Field-CTO seat at Sierra, Decagon, Glean, Harvey, Hippocratic, or Augment. Bet #3 is "MCP-Native Enterprise Integration Practice" — building MCP servers for systems enterprise GTM teams live in. Bet #4 (Inference Cost Optimization) has its largest cost surface inside agent workloads, because agents consume hundreds to thousands of tokens per task versus single-shot calls. Even Bet #1 (the Enterprise AI Procurement Playbook) lives or dies based on how enterprises buy *agents* — not LLMs, not RAG systems, agents. The agent layer is where the prior analysis was most reductive. Eighteen strata gave the agent layer one band — Stratum XIII. That single band hides a stack of its own.

This session's job is to unfold that band. To take the agent layer and treat it the way the original analysis treated the whole stack: as a multi-stratum field with its own physics, its own constraints, its own evolution stages, its own JTBD landscape, and its own competitive dynamics. Then to surface the per-layer opportunities, challenges, and open questions that a person with Alex's profile can actually act on — separately from and on top of the prior recommendations. Anything that re-derives what the prior work already concluded is wasted effort; this session should compose with the prior work, not duplicate it.

The narrowing also flips a particular lever. At the full-stack level, Alex's career options sit mostly in Strata XII-XIII (Orchestration, Application) because that is where his enterprise-GTM skill compounds. At the agent-specific level, the field is still in genesis-to-custom evolution stage across most sub-layers, which means there are positions that are wide open right now that will close within twelve to eighteen months. Examples to anchor calibration: Anthropic's Claude Agent SDK is approximately fourteen months old at this writing. OpenAI Agents SDK shipped March 2025. Google ADK April 2025. MCP went from Anthropic-only to a Linux Foundation Agentic AI Foundation directed-fund in fourteen months. The number of named, well-funded "computer-use agent" enterprise companies in 2024 was effectively zero; in May 2026 it is eight or nine. The cycle time inside the agent layer is materially shorter than the cycle time at the full-stack level, and the windows for planting flags are correspondingly shorter.

This handover defines a structured deep-dive that mirrors the prior session's discipline at higher resolution. The aim is to produce a parallel set of seven artifacts that sit alongside the originals — same aesthetic, same framework discipline, same end-state actionability, but with the unit of analysis being the agent stack, not the full AI stack.

### What the new session should NOT do

Three failure modes are pre-empted here so the new session does not waste cycles.

**First**, do not re-survey the broader field. The seven inherited deliverables already contain a thorough mapping of power, compute, fabric, data, pretraining, model providers, inference, retrieval, regulation, economics, geopolitics. Citations exist; numbers exist; positions exist. The agent layer's parent context is settled work — reference it, do not redo it.

**Second**, do not score everything 15/15. A frequent failure mode of OCQ matrices is to grade-inflate when applied to a hot field. If every agent-sub-layer Opportunity is scored Confidence-5, Time-to-Monetize-5, Claimability-5, the precise definitions are not being enforced. The discipline of the lens is what produces the signal; if everything is interesting, nothing is.

**Third**, do not produce a "list of agent products and companies." There are good aggregators and newsletters that do this — Latent Space, Air Street Capital's State of AI Report, the MCP registry, Hugging Face Agents leaderboard, Artificial Analysis. The prior session did NOT produce a survey artifact; it produced a decision artifact. This session needs to do the same.

### What "AI agents and agentic systems" means here, precisely

The field uses the term loosely. For this analysis, the working definition is: a software system that takes a goal expressed in natural language, plans multiple steps to achieve it, executes those steps using tools or actions on external systems, observes results, and updates its plan iteratively until completion or escalation. The minimum bar is three properties: (a) multi-step execution, (b) tool or action use, (c) observe-and-adapt loop. Anything that is a single-turn prompt-response chain is not an agent in this sense, even if it is sometimes marketed as one. Anything that is a fixed workflow with LLM steps inside it is closer to "AI-augmented automation" than "an agent." The line is fuzzy; the new session should err on the inclusive side but flag where the distinction matters for a specific opportunity assessment.

This implies a stratification within the agent layer that mirrors the original SUBSTRATE column. Read this as the candidate "agent strata" for the new atlas:

1. **Foundation models with agentic capability** — Claude Opus 4.5, GPT-5, Gemini 2.5 Deep Think, Llama 4, DeepSeek R1 / V4-Pro. The capability ceiling.
2. **Agent runtimes / harnesses** — Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph 1.0, Mastra, Pydantic AI, CrewAI, Smolagents, AutoGen.
3. **Tool integration / protocol** — MCP and its 10,000+ servers; the Linux Foundation governance; OpenAI Structured Outputs / function calling; Google Tool Use.
4. **Memory and state** — short-term context, working memory (Mem0, Letta, Zep), long-term episodic, knowledge-graph hybrids (GraphRAG, HippoRAG).
5. **Planning and reasoning** — single-turn → ReAct → tree-of-thoughts → planner-executor → meta-planning. Test-time compute and adaptive thinking budgets.
6. **Action surface** — text output, code execution, sandboxed compute (E2B, Modal, Daytona, Vercel Sandbox), browser automation (Playwright + AI, Browserbase, Browserless, Stagehand, Skyvern), full computer use (Operator, Mariner, Claude for Chrome, Anthropic Computer Use), voice (Vapi, Retell, Bland, LiveKit Agents), multi-agent orchestration.
7. **Evaluation and observability** — agent-specific evals (HumanLoop, Braintrust, Langfuse, LangSmith, Arize Phoenix, Inspect, METR, Patronus, Galileo). Replay-driven debug. Trajectory eval, not just final-output eval.
8. **Safety / guardrails specific to agents** — prompt-injection defense at the tool boundary, jailbreak detection in multi-turn, action-confirmation gates, sandboxing, output validation, Lakera, Robust Intelligence, NeMo Guardrails, Llama Guard.
9. **Vertical agent products** — coding (Claude Code, Cursor, Cognition Devin, Augment, Replit Agent, Lovable, Factory, Bolt, v0); customer experience (Sierra, Decagon, Cresta, Ada, Intercom Fin); knowledge worker (Glean, Hebbia, Sana, Mem); legal (Harvey, Hebbia, Spellbook); healthcare (Hippocratic, Abridge, Ambience, Suki); revenue ops (Clay, 11x, Regie, Artisan, AiSDR); engineering (Reflection, Cognition, Magic, Magic Patterns); creative (ElevenLabs, Suno, Sora 2).
10. **End-user surfaces** — chat, voice, computer use, IDE, terminal CLI, browser extension, mobile, on-device.

Plus the same meta-strata wrap: safety, regulation, economics, geopolitics — but each meta has its agent-specific dynamics. Agent-specific safety is more about action consequences than text outputs. Agent-specific regulation is the EU AI Act's "high-risk" classification triggers and US sectoral overlays. Agent-specific economics is the inference-cost-per-task curve, which is meaningfully different from per-token economics because of multi-step execution. Agent-specific geopolitics is sovereign-AI agent products in the Gulf, India, and Europe.

This gives roughly ten "agent strata" plus four meta-strata — fourteen total — close in shape to the original eighteen but with very different content per layer.

### Why the timing matters now

Three reasons the agent-specific deep-dive is high-leverage in May 2026 specifically.

First, the agent-builder layer just consolidated. Within fourteen months — November 2024 (Anthropic publishes MCP) through January 2026 (Linux Foundation directed-fund) — the protocol layer for tool use settled. OpenAI, Anthropic, Google, Hugging Face, and Microsoft all adopted MCP at the protocol level. This is the rarest condition in software: a standard that won. The fourteen-to-twenty-four-month window after a protocol wins is when the largest application companies get built on top of it. The window opened in early 2026 and will close around mid-2027. We are inside it now.

Second, the agent-app revenue layer just validated. Sierra grew from zero to $175M+ ARR in 24 months; Cursor went from sub-$1M to $500M+ in similar time; Lovable hit $20M ARR in two months; Decagon reached $80M Q1 2026; Harvey reached $100M+ Q1 2026; Augment reached $40M Q1 2026; Glean $300M+. Every one of these is an agent or agent-adjacent company. The pattern is not anomalous; it is the new dominant pattern of enterprise SaaS adoption. The Stripe-Ramp-Datadog-Snowflake → Sierra-Decagon-Glean-Hippocratic talent migration that the prior session's Talent and Capital Flow tracker identified is the same observation seen from the labor-market side.

Third, the agent-procurement gauntlet just hardened. In the same fourteen months, enterprise AI councils stood up at most Fortune 1000 buyers, EU AI Act GPAI obligations took effect (August 2025), and California SB 53 went live (January 2026). The buying motion for an agent is now categorically different from the buying motion for an API: governance, action-consequence review, model-risk assessment, kill-switch documentation, and operational SLAs around action outcomes are all required. This is exactly the seam where Alex's twelve years of enterprise procurement scar tissue plus AI-builder fluency creates uncommon leverage.

The agent-specific deep-dive will, if executed well, produce three things the prior session could not: per-agent-sub-layer opportunity rankings (instead of one-band lumping); a tactical map of which specific companies in each sub-layer match Alex's profile (instead of a horizontal target list); and an agent-specific procurement playbook outline that becomes an immediate input to Bet #1 from the prior session (instead of remaining a generic ambition).

### What success looks like

At the end of this session, Alex should be able to:

- Open a single visual plate and immediately see all ten agent sub-layers with their evolution stage, dominant players, and binding constraints.
- Read a forty-to-sixty-minute deep-dive document that explains the agent stack with the same depth the foundation report gives to the broader stack.
- Open a decisions playbook for the agent layer specifically that names seven (or however many converge) agent-specific bets, ranks them, and gives him falsifiability criteria and conviction marks.
- Maintain a living tracker that follows agent-specific talent flow, capital flow, and ARR signals — a sub-tracker that feeds into the broader OCQ_TRACKER.md.
- Walk into any conversation with a vertical-agent company (Sierra, Decagon, Harvey, Hippocratic, Augment, Cresta, Cognition) and demonstrate field-level mastery of the layer they sit in — not just their company.

If the artifacts produced enable all five of those, the session succeeded.

---

## 2. The methodology that was used (so this session can replicate it)

### The skills inventory that mattered

Skills loaded and applied (these are anthropic-skills and repo-skills the prior session deployed):

- **anthropic-skills:canvas-design** — for the visual aesthetic. Produced "Substrate" design philosophy: ink-on-cream, hairline rules, vermilion/verdigris/ochre accents, condensed display caps, monospace marginalia. The full philosophy is at `design_philosophy.md`. Reuse the same aesthetic for continuity.
- **anthropic-skills:docx** — for Word document generation. Uses docx-js. The build pattern is `npm install docx --save` in the output directory, then a single self-contained build script using helper functions (h1, h2, h3, p, bullet, rich). The original scripts are at `build_report.js` and `build_addendum.js` — copy their helper-function patterns.
- **Repo skills referenced for analytical discipline:**
  - `Product/decision-intelligence-fundamentals` — Lorien Pratt's DI methodology; Type III error trap.
  - `Product/causal-decision-modeling` — Causal Decision Diagrams (levers/externals/intermediates/outcomes).
  - `Product/decision-simulation-and-monitoring` — Lobster Claw and Whack-a-Mole patterns; leading indicators.
  - `Product/systems-thinking` — Meadows' 12 leverage points; feedback-loop archetypes.
  - `Product/ai-product-strategy` — "build for the slope, not the snapshot"; human-AI boundary; society of models.
  - `Product/outcome-driven-innovation-and-job-mapping` — 8-phase Job Map; desired outcome statements; importance-satisfaction gap.
  - `Product/jtbd-strategy-and-organization` — JTBD applied at organizational scale.
  - `Product/platform-strategy` — multi-sided platforms; cross-side network effects.
  - `Product/ai-build-vs-buy-and-model-adaptation` — build-and-buy framing, abstraction-layer bets.
  - `Evals, Harness, & Observability/evaluating-new-technology` — Aparna's "update your priors"; Asha's abstraction-layer bet.
  - `Evals, Harness, & Observability/evaluating-trade-offs` — weighted criteria matrices; "would I start this today?" test; Lochhead's "spend more time on the problem."
  - `Organizational Leadership/problem-definition` — Moesta's struggling moments; Lochhead's spend-time-on-problem.
  - `Organizational Leadership/setting-okrs-goals` — leading indicators per bet.
  - `Research, Financial Modeling, and Market Analysis/competitive-intelligence` — competitor maps, intelligence gathering.
  - `Research, Financial Modeling, and Market Analysis/market-research` — sizing, segmentation.
  - `Software Development/cto-architect` — technical-constraint reading, the PROJECT_BRIEF protocol, the stack-context awareness.

### The order of operations that worked

The prior session executed roughly this sequence, and the new session should mirror it:

**Phase 0 — Calibration (15–30 min)**
- Read this handover document in full.
- Read `Me/claude.md` if it has not changed (Alex's identity and communication preferences).
- Read `STACK_README.md` (Alex's current tool stack and MCP connections).
- Sample 3–5 sentences from the prior outputs (the executive summary in `AI_STACK_REPORT.docx`, Part X in `AI_STACK_ADDENDUM.docx`, and `OCQ_TRACKER.md`) to absorb the register and aesthetic.
- Confirm or adjust the candidate sub-strata list in §1 above before dispatching parallel agents.

**Phase 1 — Parallel research dispatch (60–90 min wall-clock)**
- Dispatch six parallel `general-purpose` sub-agents covering the candidate sub-strata. Use the briefs in §4 below.
- Each brief is written in the prior session's voice and contains: precise scope, register, output format, length cap (1,500–2,500 words each), citations expected.

**Phase 2 — Atlas build (30–45 min)**
- Synthesize the research outputs into a foundation report following the structure of `AI_STACK_REPORT.docx`. Target ~10,000 words, structured as: Executive Summary, ten sub-strata sections, two meta sections, closing synthesis, sources.
- Build the parallel visual atlas as Plates I–VI for the agent layer, mirroring the SUBSTRATE aesthetic. Use the `build_infographic.py` script from `output/ai-stack/` as the template; copy/adapt its helper functions (`new_page`, `page_frame`, `stratum`, `node`, `metric_bar`).

**Phase 3 — Framework analysis dispatch (60–90 min wall-clock)**
- Dispatch eight parallel framework-specific agents using the briefs in §5 below:
  - Four OCQ-chunk agents covering ten sub-strata + four meta in four buckets.
  - One Wardley Mapping agent for the agent stack.
  - One 7 Powers agent for the agent stack.
  - One Ecosystem JTBD agent for agent-specific jobs.
  - One Talent and Capital Flow agent specifically for the agent labor and funding market.

**Phase 4 — Decisions playbook build (45–60 min)**
- Synthesize framework outputs into a decisions addendum following the structure of `AI_STACK_ADDENDUM.docx`. Parts: OCQ Matrix, Wardley analysis, 7 Powers analysis, Ecosystem JTBD, Synthesis (Big Bets / Risks / Cruxes), Action Map (6/12/18-month), Best-Use-Case Reflections.
- Build Plates VII–XI matching the SUBSTRATE Vol II aesthetic.

**Phase 5 — Master Plate (30 min)**
- One synthesis plate showing entanglements, flows, constraints, and feedback loops for the agent stack — mirroring `AI_STACK_MASTER_PLATE.pdf`.

**Phase 6 — Living tracker (15–30 min)**
- An agent-specific subset of the OCQ_TRACKER.md format: agent bets, agent talent flow, agent capital flow, agent ARR watchlist, agent-specific cruxes and risks.

### What the prior session learned about pitfalls

- Build scripts: docx-js loses node_modules when the directory is cleaned; always re-run `npm install docx --save` before invoking the build.
- Font handling: Big Shoulders does not contain Ω, ★, or some Unicode symbols. Use letters or filled-circle shapes instead.
- Letterspacing: matplotlib has no `letterspacing=` kwarg. Use the `sp(text, n)` helper that inserts space characters between each character.
- Stratigraphic plates: keep the numeral column at least 16 units wide if numerals can be three Roman characters (XIII, VIII).
- Densely-labeled rails: if labels are right-anchored, anchor them OUTSIDE the column boundary. Mis-placement is the #1 visual bug.
- Word-count discipline: 8,500 words is a good target for the foundation report; 18,000 for the decisions addendum; >20,000 starts producing returns below cost.
- Score discipline: enforce the precise lens definitions. The prior session caught itself scoring 15/15 on too many opportunities; the second pass tightened them to a distribution.

---

## 3. The inheritance — what exists in `output/ai-stack/`

The new session should treat these as read-only references, not as inputs to re-derive.

**Visual artifacts:**
- `AI_STACK_SUBSTRATE.pdf` — Volume I. Six plates (I–VI) covering the full stratigraphic column.
- `AI_STACK_SUBSTRATE_VOL2.pdf` — Volume II. Five plates (VII–XI): OCQ heat map, Wardley map, 7 Powers grid, Ecosystem JTBD canvas, Action Portfolio.
- `AI_STACK_MASTER_PLATE.pdf` — Master Plate. The whole stack on a single page with cross-layer flows, binding constraints, feedback loops, and meta-strata as wrapping forces.

**Narrative artifacts:**
- `AI_STACK_REPORT.docx` — Foundation report. ~8,500 words. The descriptive prose layer.
- `AI_STACK_ADDENDUM.docx` — Decisions Playbook. ~18,700 words. Parts VI–XII: OCQ Matrix per stratum, Wardley analysis, 7 Powers grid, Ecosystem JTBD (six jobs), Synthesis (7 Bets / 5 Risks / 5 Cruxes), 6/12/18-month Action Map, Best-Use-Case Reflections.

**Living artifact:**
- `OCQ_TRACKER.md` — The 7 Big Bets with falsifiability, conviction, leading indicators; talent + capital flow tracker; ARR watchlist; cruxes and structural risks. Maintained bi-weekly/monthly.

**Reproducible build scripts:**
- `design_philosophy.md` — the "Substrate" aesthetic philosophy.
- `build_infographic.py` — Vol I plate generator (matplotlib).
- `build_substrate_vol2.py` — Vol II plate generator.
- `build_master_plate.py` — Master Plate generator.
- `build_report.js` — Foundation report generator (docx-js).
- `build_addendum.js` — Decisions Playbook generator (docx-js).

### Key conclusions inherited (so this session can build on them rather than re-derive)

- **The seven Big Bets** are in `AI_STACK_ADDENDUM.docx` Part X and on Plate XI. Bets #2, #3, and #4 directly involve the agent layer.
- **The five Structural Risks**: HBM4/CoWoS-L slip; Hyperscaler FCF reckoning; OpenAI Preparedness adjustment-clause; Federal preemption volatility; Foundation labs walking up-stack.
- **The five Cruxes**: Anthropic ARR ($24B vs $30B); inference compute growth (10× vs flat); MCP commons vs fork; EU AI Act enforcement teeth; long-term memory as standalone category or absorbed.
- **The Talent and Capital Flow signal** that the Stripe/Ramp/Datadog/Snowflake → Sierra/Decagon/Glean/Hippocratic migration is the most actionable signal for Alex's profile.
- **The conclusion** that NYC is winning in vertical-agent GTM specifically (Sierra dual-HQ, Hippocratic NYC, Anthropic NYC enterprise ramp, Decagon NYC presence).

The new session should reference these by name when relevant and not redo them.

---

## 4. Phase 1 — Parallel research agent briefs (6 agents, ready to dispatch)

Each brief is self-contained. Dispatch as parallel sub-agents (general-purpose). Word counts are firm caps.

### Agent A1 — Agent runtimes, harnesses, and protocol

**Scope:** Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph 1.0, Mastra, Pydantic AI, CrewAI, Smolagents, AutoGen, AG2. Plus MCP (the Model Context Protocol) — its 2024 origin at Anthropic, the November 2025 spec, the December 2025 donation to the Linux Foundation Agentic AI Foundation, the registry growth (5,800 → 10,000+ servers), the major hyperscaler MCP gateways (Cloudflare, Kong, Pomerium). Plus function calling and structured outputs as the proto-MCP era.

**What to surface:** maturity of each runtime, market position, opinionated takes on which wins enterprise (with the why), MCP fork risk indicators, the Custom-to-Product evolution-stage assessment.

**Output:** ~2,000 words, structured markdown. Include 3–5 specific data points with dates. Flag where you're uncertain. End with a "what changed in the last 90 days" summary.

### Agent A2 — Memory and state for agents

**Scope:** Mem0, Letta (formerly MemGPT), Zep, Cognee — the long-term memory category. Context-engineering patterns inside agent runtimes. Working memory vs episodic vs semantic. Knowledge-graph hybrids (Microsoft GraphRAG, HippoRAG/HippoRAG2, PathRAG, OG-RAG). The "is memory a standalone category or absorbed by labs?" crux. Native memory features in Claude / ChatGPT / Gemini.

**What to surface:** which memory architectures hold up under multi-turn, multi-session, multi-user load. The procurement and compliance implications of agent memory (HIPAA, GDPR right-to-be-forgotten, EU AI Act transparency). Real production deployments at named customers.

**Output:** ~1,800 words. Same format as A1.

### Agent A3 — Planning, reasoning, and test-time compute in agents

**Scope:** how planning evolved from single-turn → ReAct → tree-of-thoughts → planner-executor → meta-planning. Test-time compute scaling: o1, o3, Claude extended thinking 64k budgets, Gemini Deep Think, DeepSeek R1. The agent-specific implications: per-task compute spend, latency budgets, planning vs execution split. Process Reward Models. RLVR and GRPO when applied to agent trajectories.

**What to surface:** which planning architectures show up in production agents (not research). The economic implications of a 10× thinking budget per agent task. Adaptive thinking-budget product features.

**Output:** ~1,800 words. Same format.

### Agent A4 — Action surfaces: code, browser, computer, voice, sandbox

**Scope:** the action layer of agents. Code execution sandboxes (E2B, Modal, Daytona, Vercel Sandbox, Hugging Face Spaces); browser automation for agents (Playwright + AI, Browserbase, Browserless, Stagehand, Skyvern); computer use (Anthropic Computer Use, OpenAI Operator → ChatGPT Agent, Google Project Mariner, Claude for Chrome); voice agent platforms (Vapi, Retell, Bland, LiveKit Agents, ElevenLabs Conversational AI, OpenAI Realtime, Cartesia Sonic-2, Deepgram Nova-3); telephony for agents (Twilio, Telnyx, LiveKit Cloud).

**What to surface:** the reliability inflection point per action type. The 70%+ on WebArena/OSWorld threshold for computer use. Voice latency floor and what crosses the "uncanny" line. Sandboxing for AI-generated code as a procurement requirement.

**Output:** ~2,200 words. Same format.

### Agent A5 — Vertical agent products (the application layer)

**Scope:** the vertical agent companies organized by domain. Coding (Claude Code, Cursor, Cognition Devin, Augment, Replit Agent, Lovable, Factory, Bolt, v0). CX (Sierra, Decagon, Cresta, Ada, Intercom Fin, Parloa, PolyAI, Regal). Knowledge worker (Glean, Hebbia, Sana, Mem). Legal (Harvey, Hebbia, Spellbook, EvenUp, Eve). Healthcare (Hippocratic AI, Abridge, Ambience, Suki, Nabla). RevOps (Clay, 11x, Regie, Artisan, AiSDR, Nooks). Engineering productivity beyond coding (Reflection, Magic). Finance (Rogo, Hebbia, Cognition-adjacent). For each: ARR if known, valuation, NYC presence Y/N, hiring pattern Y/N, top-3 talent inflow source if known.

**What to surface:** which segments support multiple winners vs winner-take-most. Which companies are over-funded vs under-funded relative to ARR velocity. Which are hiring exactly Alex's profile right now.

**Output:** ~2,500 words. Same format.

### Agent A6 — Agent evaluation, observability, and safety

**Scope:** agent-specific eval frameworks (HumanLoop, Braintrust, Langfuse, LangSmith, Arize Phoenix, Inspect, METR, Patronus, Galileo, Promptfoo-acquired-by-OpenAI). Trajectory evals vs final-output evals. Replay-driven debug. Agent-specific guardrails (Lakera, Robust Intelligence Cisco, NeMo Guardrails, Llama Guard, Prompt Guard). Prompt injection at the tool boundary. Action-confirmation gates. Sandboxing as guardrail. EU AI Act high-risk classification triggers for agents.

**What to surface:** the procurement-readiness gap — what enterprise risk and compliance officers ask about agents that no eval/obs vendor fully addresses. The "would I deploy this in production touching customer money?" threshold. Open-source vs proprietary tradeoffs.

**Output:** ~2,000 words. Same format.

**Total Phase 1 output:** roughly 12,300 words of research, ready to synthesize.

---

## 5. Phase 3 — Framework analysis agent briefs (8 agents, ready to dispatch)

The four OCQ-chunk agents apply the precise lens definitions from `AI_STACK_ADDENDUM.docx` Part VI (Methodology section). Repeat the discipline here. The other four agents follow the same patterns as the prior session — copy briefs from `build_addendum.js` (the Part X/XI/XII passages) for register.

### Agents B1–B4 — OCQ Matrix (four chunks across ten agent sub-strata + four meta)

**Bucket distribution suggestion:**
- B1: Sub-strata 1–3 (Foundation models with agentic capability; Agent runtimes; Tool integration / MCP) + Meta-D (geopolitics: sovereign agents).
- B2: Sub-strata 4–5 (Memory; Planning/reasoning) + Meta-A (safety specific to agents).
- B3: Sub-strata 6–7 (Action surface; Evaluation/observability) + Meta-B (regulation: agent autonomy classification).
- B4: Sub-strata 8–10 (Safety/guardrails; Vertical agent products; End-user surfaces) + Meta-C (economics: per-task agent inference cost).

**Per-bucket brief:** apply OCQ lens precisely (top 3 opportunities, top 2 challenges, top 2 open questions per sub-stratum, scored 1–5 on each of three dimensions). Tie every entry to a specific 2025–2026 datapoint. Word cap: ~2,000 words per bucket.

### Agent B5 — Wardley Map of the agent stack

**Brief:** anchor 3–4 user-need top-of-map items specific to agentic workflows (e.g., "complete a 5-step research and reporting task autonomously," "operate a browser to complete a back-office workflow," "answer customer queries with voice + escalation handoff," "write, test, and merge a production code change"). Trace dependency chains down through every sub-stratum. Place each component at its current evolution stage with reasoning. Identify 5–7 punctuated equilibria expected in 2026–2027 for the agent layer specifically. Then list the strategic quadrants — Pioneer (genesis), Settle (custom→product), Consume (product→commodity), Utility — with named components in each. Close with implications for Alex.

**Output:** ~2,500 words.

### Agent B6 — 7 Powers analysis for the agent stack

**Brief:** for each of the ten agent sub-strata, identify which of Helmer's seven powers (Scale, Network, Counter-Positioning, Switching Costs, Brand, Cornered Resource, Process Power) are present, who holds them, whether they are strengthening or eroding. Conclude with the five most durable agent-layer positions, the five most over-rated, and what this means for career-bet selection inside the agent stack.

**Output:** ~2,200 words.

### Agent B7 — Ecosystem JTBD for agent-augmented workflows

**Brief:** identify 5–7 ecosystem-level jobs that the agent stack is hired to do (e.g., "fully complete a discrete back-office task without human babysitting"; "run a customer-facing conversation to resolution with appropriate escalation"; "execute a multi-step coding change including PR review and merge"; "operate a SaaS application on the user's behalf"). For each, build an 8-phase Job Map and identify the top 3 underserved outcomes. End with a cross-job synthesis: the three most-underserved patterns and the three most over-served. Connect each to a specific buyer persona and willingness-to-pay.

**Output:** ~2,500 words.

### Agent B8 — Talent and Capital Flow specifically in agents

**Brief:** track senior talent moves into and out of agent-specific companies in the last 12 months. Cover Sierra, Decagon, Glean, Hebbia, Harvey, Hippocratic, Abridge, Cresta, Cognition, Augment, Cursor, Lovable, Replit Agent team, Clay, 11x, Anthropic agent team, OpenAI agent team. Track capital events ($50M+ rounds, M&A, infra commits) in the same window. Maintain an ARR watchlist (with disputed-figure ranges where applicable). Identify public statements from agent-company founders that decode interesting signal. Include NYC-specific cuts. End with a synthesis of what the empirical signal says that the analytical frameworks miss.

**Output:** ~3,500 words. Format for living-tracker maintenance.

**Total Phase 3 output:** roughly 17,000 words. Synthesizable.

---

## 6. Expected deliverables (mirror the prior session structure)

Final output folder: `output/ai-agents/`

| File | Mirrors | Target |
|---|---|---|
| `AI_AGENTS_SUBSTRATE.pdf` | `AI_STACK_SUBSTRATE.pdf` | 6 plates — index, 2–3 sub-strata pages, 1 meta page |
| `AI_AGENTS_SUBSTRATE_VOL2.pdf` | `AI_STACK_SUBSTRATE_VOL2.pdf` | 5 plates — OCQ heat, Wardley, 7 Powers grid, JTBD canvas, Action Portfolio |
| `AI_AGENTS_MASTER_PLATE.pdf` | `AI_STACK_MASTER_PLATE.pdf` | 1 plate — synthesis of agent-layer flows |
| `AI_AGENTS_REPORT.docx` | `AI_STACK_REPORT.docx` | ~10,000 words foundation report |
| `AI_AGENTS_ADDENDUM.docx` | `AI_STACK_ADDENDUM.docx` | ~18,000 words decisions playbook |
| `AI_AGENTS_TRACKER.md` | `OCQ_TRACKER.md` | Living tracker, agent-specific |
| `design_philosophy_agents.md` | `design_philosophy.md` | Aesthetic continuity statement (one paragraph) |

The aesthetic is the same — "Substrate" — but the badge should read "VOL III" or similar to distinguish the agent atlas from the original.

---

## 7. The tailored framework — agent-specific lens definitions

The prior session's OCQ lens definitions are at `AI_STACK_ADDENDUM.docx` Part VI Methodology. Use the same lenses but tighten them for the agent context.

**OPPORTUNITY (agent layer):** where in the agent stack is value being created faster than the field's prevailing narrative reflects, AND where can someone with enterprise B2B GTM and growing AI-builder skill claim it inside a 12-18 month window before the layer commoditizes or consolidates? Score: Confidence × Time-to-Monetize × Claimability for Alex.

**CHALLENGE (agent layer):** what is the binding constraint or latent feedback loop in the agent stack that, if it tightens or fires, materially reprices everything above it? Specifically: protocol fragmentation, model-vendor reasoning regression, inference-cost spikes, action-consequence liability, eval-trust collapse. Score: Severity × Probability × Alex's exposure.

**OPEN QUESTION (agent layer):** what is the agent-specific crux the field is betting on without admitting? Examples to anchor: does memory become a permanent category or absorbed; does MCP fork; does computer-use cross 80% reliability in 2026 or 2027; does test-time compute scaling hit diminishing returns; does ASL-4 capability emerge in 2026 and force a deployment freeze. Score: Decidability × Asymmetry × Bet-size.

---

## 8. Final notes for the new session

- **Tone discipline.** Match the register in `AI_STACK_REPORT.docx` and `AI_STACK_ADDENDUM.docx`. Direct, commercially fluent, technically aware. Headers and structure for complex outputs. No filler.
- **Update prior bets.** Where this session's analysis materially changes the conviction or sequencing of one of the prior session's seven Big Bets, say so explicitly. The new tracker should annotate any deltas.
- **Show the compose, not the duplicate.** The new deliverables should READ AS a higher-resolution zoom that uses the prior work as scaffold, not as standalone work that ignores the prior synthesis.
- **The procurement playbook lives.** Bet #1 from the prior session (Enterprise AI Procurement Playbook) will be built in Session B. This session should produce, as a byproduct, the agent-specific section of that future Playbook — i.e., the rubric for evaluating an agent vendor in a Fortune 1000 procurement gauntlet. Drop this into `AI_AGENTS_ADDENDUM.docx` as a Part XIII or appendix.
- **Tag deltas to the prior cruxes.** If a research finding decisively resolves one of the five inherited cruxes, mark it in the new tracker and propose a re-rank of bets.
- **Cycle time.** This session should complete in roughly half a day of wall-clock work if parallel-agent dispatch is used properly. Three to four hours of agent run-time plus two to three hours of synthesis.

When ready, the new session opens with: "I have read HANDOVER_A_AGENTS.md and the seven inherited artifacts. I am beginning Phase 0 calibration."
