# B1 — OCQ Matrix: Models · Runtimes · Protocol · Geopolitics

> Framework analysis for the AI-agents stratum. Companion to `A1_models_runtimes_protocol.md` and `A5_vertical_products.md`. Feeds AI_AGENTS_ADDENDUM.
> **Date:** 2026-05-12. **Scores 1–5.** Opp = Conf/TTM/Claim · Chal = Sev/Prob/Exp · OQ = Dec/Asym/Bet.

---

## Layer 1 — Foundation Models (agentic capability only)

**Framing.** Single-turn IQ saturated; frontier is trajectory length and tool reliability. Claude Opus 4.5 (82.8% SWE-Bench Verified, Mar 2026) leads agentic tool use; GPT-5 leads single-shot codegen; Gemini Deep Think leads long-context. Computer-use is demoware — OSWorld 35–42%, prod 20–30% end-to-end. Test-time compute (Opus 4.5 64k thinking) is the real lever; bifurcates market into interactive (Sonnet/4o) vs. autonomous (Opus/GPT-5-Thinking). Stage: **late-Custom chat, early-Custom agency**.

### Opportunities

**1.1 Trajectory-quality evaluation as sellable artifact.** Vendor SWE-Bench numbers are harness-dependent; F500 buyers can't reproduce them. No neutral "agentic capability audit" exists. A GTM operator running Claude Opus 4.5 + GPT-5 + Gemini through TAU-bench / SWE-Bench / OSWorld on the buyer's tool surface = procurement-side SOC-2 auditor analog. Anthropic Sept 2025 notes admit context-degradation past 32k; no buyer tests this.
*Conf 4 · TTM 4 · Claim 4.* **Falsifiability:** ArtificialAnalysis or Vellum ships a productized buyer-side agentic eval by Q4 2026 → lane closes.

**1.2 "Thinking-budget" cost-arbitrage advisory.** Opus 4.5 thinking runs $0.50–$5/task; most enterprises max-think by default. Routing 80% Sonnet/Haiku, 20% Opus-thinking cuts agent spend 4–8× at flat TAU-bench quality. Stacks onto Bet #4. Sonnet/Opus price delta 5×; Claude Code telemetry (Dario, Mar 2026) shows ~70% of calls don't need Opus.
*Conf 4 · TTM 5 · Claim 4.* **Falsifiability:** AWS Bedrock or Vercel AI Gateway ship auto-routing-by-task-complexity by Q3 2026 → window slams.

**1.3 Computer-use deployment-readiness (supervised-not-autonomous niche).** OSWorld at 40% means computer-use works *only with a human reviewer*. Buyers either ignore the category or expect autonomy and get burned. Productizable: HITL workflow design — bounding scope, defining checkpoints, picking 5 tasks where 70% reliability is acceptable. Claude for Chrome preview Dec 2025, Mariner GA Apr 2026 — shipped without buyer playbooks.
*Conf 3 · TTM 3 · Claim 4.* **Falsifiability:** OSWorld crosses 60% before Q2 2027 → supervised niche evaporates.

### Challenges

**1.A Foundation labs walking into vertical apps faster than expected.** Claude for Chrome, ChatGPT Agent (Jul 2025 Operator+Deep Research merge), Gemini Enterprise absorbing the horizontal-agent surface Sierra/Decagon/Glean treat as moat. If labs ship multi-system orchestration with outcome SLAs natively, Bet #2 valuations reprice.
*Sev 4 · Prob 3 · Exp 5.* **Watch:** ChatGPT Business or Claude for Work announce per-resolution pricing on CX workloads.

**1.B Context-degradation ceiling persists.** Sub-agents is workaround, not fix. If long-context + sub-agent orchestration stays brittle past 50-step trajectories through 2026, multi-step ARR curves at Sierra/Decagon flatten; Bet #4 pivots to "FinOps for re-runs."
*Sev 3 · Prob 4 · Exp 3.* **Watch:** Anthropic / OpenAI release notes Q3 2026 quantifying multi-turn reliability gains.

### Open Questions

**1.i Does Opus 4.5's lead survive GPT-5.5 / Gemini 3?** Anthropic's ~8pt SWE-Bench gap is real but narrow. If GPT-5.5 or Gemini 3 lands within 2 pts in H2 2026, "Claude as default agent model" weakens; the $200B valuation reprices.
*Dec 4 · Asym 4 · Bet 5.* **Answer-event:** GPT-5.5 or Gemini 3 SWE-Bench Verified independently reproduced.

**1.ii Does DeepSeek R2 close the agentic gap?** R2 leaks (May 2026) suggest mid-60s SWE-Bench. If real, open-weight agentic capability hits closed-frontier-minus-15pts; sovereign procurement reprices; F500s in regulated geos get a credible in-VPC option.
*Dec 4 · Asym 4 · Bet 4.* **Answer-event:** R2 official release with independent SWE-Bench Verified > 60%.

---

## Layer 2 — Agent Runtimes / Harnesses

**Framing.** Today the runtime layer splits along the model spine. Claude Agent SDK (Sept 2025, sub-agents/skills/hooks/MCP-native), OpenAI Agents SDK (Mar 11 2025, Responses API), Google ADK (Apr 9 2025, A2A), LangGraph 1.0 (Oct 22 2025); plus Mastra, Pydantic AI, CrewAI. Neutral-runtime pitch losing to vendor SDKs in greenfield — providers ship faster than wrappers wrap. Value accrues to model below, app above. Stage: **early-Product, commoditizing 12–18 months**.

### Opportunities

**2.1 Claude Agent SDK + Skills as F500 builder's standard kit.** Sub-agents/skills/hooks primitives ~6 months ahead; buyer-side Skill catalog (procurement-readiness, vendor-DDQ, RevOps-handoff) empty. GTM operator publishing 10–20 enterprise-vertical Skills as open repo = canonical reference. Cursor/Vercel/Replit name-check the SDK in 2026 notes; no curated enterprise Skills library exists.
*Conf 4 · TTM 5 · Claim 5.* **Falsifiability:** Anthropic ships a first-party Skills Marketplace with curated enterprise content by Q4 2026 → wedge closes (authorship credit endures).

**2.2 LangGraph-rip-out / vendor-SDK migration practice.** F500s standardized on LangChain in 2024; LangGraph 1.0 (Oct 2025) is API-churn fatigue at scale; greenfield 2026 chooses vendor SDKs. Migration audit ("which workloads stay on LangGraph, which move to Claude/OpenAI SDK") = $50–250K engagement. LangChain Inc. repositioning on LangSmith because runtime margin collapses — confirms thesis from source.
*Conf 4 · TTM 4 · Claim 4.* **Falsifiability:** LangGraph posts >2× ARR growth in Aug 2026 update → rip-out narrative wrong.

**2.3 Observability/eval consulting (LangSmith / Inspect AI / Pydantic Logfire).** Once runtimes commoditize, eval+observability is where margin sits. F500s have no playbook for picking between LangSmith, Inspect AI (UK AISI, safety-conscious), Pydantic Logfire, Anthropic-native traces. Bet #5 extension. OpenAI acquired Promptfoo Sept 2025; eval being internalized.
*Conf 3 · TTM 4 · Claim 3.* **Falsifiability:** A single observability vendor (Datadog LLM, New Relic AI) captures >40% F500 mindshare by EOY 2026.

### Challenges

**2.A Runtime commoditization compresses Alex's claim window.** If runtimes become "thin wrapper around model SDK" by H1 2027, Skills-catalog and migration-audit positioning last ~12 months. Career capital must convert into something durable (Bets #1, #2, #5) inside the window.
*Sev 3 · Prob 4 · Exp 4.* **Watch:** Mastra / Pydantic AI / CrewAI consolidation (acquihires by Vercel, Anthropic, MSFT) — once 2 of 3 happen the window is closing.

**2.B Vendor lock-in becomes the procurement objection reviving neutral runtime.** Claude Agent SDK locks to Claude; OpenAI Agents SDK to OpenAI. F500 procurement (Bet #1 territory) will increasingly demand multi-model abstraction — swinging back toward LangGraph. If hard enough, "vendor SDK is dominant" is too clean.
*Sev 3 · Prob 3 · Exp 3.* **Watch:** F500 RFP language standardizing on "model-portable agent runtime" in late 2026.

### Open Questions

**2.i Does Google A2A win agent-to-agent communication?** A2A (Apr 2025) is the second protocol-fragmentation venue. If it wins, multi-agent systems route through Google primitives even with Anthropic/OpenAI models. May 2026: non-Google adoption thin — bearish.
*Dec 3 · Asym 3 · Bet 4.* **Answer-event:** A non-Google hyperscaler or Sierra/Decagon-tier vertical agent commits to A2A publicly.

**2.ii Does any independent runtime survive as a $1B+ business?** LangChain Apr 2026 funding update is the bellwether. If LangGraph + LangSmith can't sustain $200M+ ARR by EOY 2027 → "runtimes are SDK features, not companies."
*Dec 3 · Asym 4 · Bet 4.* **Answer-event:** LangChain Inc. financial disclosure or acquisition.

---

## Layer 3 — Tool-Use Protocol (MCP)

**Framing.** MCP launched Nov 25 2024; OpenAI Mar 26 2025, Google Apr 9 2025, MSFT May 2025; LF donation Dec 8 2025. Registry: 50 → 11.4k (Apr'26). Crux: **commons vs. silent fork**. Spec held; experience fragmenting — OpenAI Responses-API native tool-calls bypass MCP for latency; Anthropic's `tool_use` blocks remain proprietary native; quality bimodal. Gateway category (Cloudflare Dec 2024, Kong GA Jul 2025, Pomerium May 2025) = most durable middleware tier here. Stage: **late-Custom crossing to Product**.

### Opportunities

**3.1 Enterprise MCP server productization for un-served SaaS.** Salesforce, HubSpot, Outreach, Gong, Highspot ship zero or one MCP server; F500 GTM stacks need 10–15. Direct Bet #3 mapping. A constellation of first-party-parity servers (auth, audit, rate-limit-aware) via LF registry + marketplace = inbound flywheel. Registry 11.4k Apr 2026; first-party from Snowflake/Databricks/ServiceNow accelerated; GTM-SaaS coverage still thin.
*Conf 4 · TTM 3 · Claim 4.* **Falsifiability:** Salesforce + HubSpot ship enterprise-grade MCP servers in 2026 → 3rd-party wedge for those systems closes (8+ others remain).

**3.2 MCP-gateway buyer-side advisory (Kong / Cloudflare / Pomerium).** Gateway = enterprise-control-plane scale ($1B+ ARR by 2028, inferred from API-gateway analog). F500s have zero picking frameworks. Vendor-neutral audit = $50–150K engagement; natural Bet #1 extension. Kong GA Jul 2025 with F500 design partners; Cloudflare auth primitives expanded Apr 2026.
*Conf 4 · TTM 4 · Claim 4.* **Falsifiability:** Kong captures >50% F500 reference customers by Q2 2027 → choice trivializes.

**3.3 Private MCP registry curation as enterprise practice.** Quality bimodal in public registry; F500 InfoSec won't whitelist 11k servers. Pattern: curated private registry (analog: internal npm/PyPI mirrors). Sellable artifact = curation framework + 100-server vetted list + governance template. Light-tech, GTM-claimable.
*Conf 3 · TTM 3 · Claim 4.* **Falsifiability:** Anthropic or LF launches a "verified" tier in the public registry by Q4 2026 → private-curation value compresses.

### Challenges

**3.A Silent fork (Responses-API-native vs. MCP-native) hardens in production traffic.** Already happening: many production OpenAI agents bypass MCP for latency. If this hardens, MCP becomes the "OpenAPI of agents" (baseline, not interop). Bet #3 thesis halves.
*Sev 4 · Prob 3 · Exp 5.* **Watch:** OpenAI introduces a Responses-API-only tool primitive (e.g., streaming-tool-calls) with no MCP equivalent.

**3.B LF governance turbulence.** Tracker Crux #3. TSC has Anthropic, MSFT, Google, OpenAI, HF, Cloudflare. If any major vendor walks (IP, schema, telemetry disputes), the commons cracks fast.
*Sev 5 · Prob 2 · Exp 5.* **Watch:** Public TSC dispute, Anthropic re-asserting unilateral authority, or OpenAI announcing a non-MCP "AgentSpec v2."

### Open Questions

**3.i Does MCP cross the OpenAPI threshold (universal baseline)?** OpenAPI took ~6 years post-2010. MCP is 18 months in with 11k servers + 4 hyperscaler commits — running 3–4× faster.
*Dec 4 · Asym 5 · Bet 5.* **Answer-event:** Registry crosses 25k AND >50 SaaS incumbents ship first-party servers by EOY 2026.

**3.ii Do MCP gateways consolidate or stay fragmented?** Highest-margin durable layer in this brief. 1–2 winners or 10+ undifferentiated vendors?
*Dec 3 · Asym 4 · Bet 4.* **Answer-event:** Kong, Cloudflare, or new entrant posts >$50M ARR on gateway-specific SKUs by EOY 2026.

---

## Layer 4 — Meta-D · Geopolitics & Sovereign Agents

**Framing.** Most under-discussed layer in US-anchored agent press. Stargate UAE (May 2025, G42), Humain KSA ($10B AMD), Mistral Series C (€600M @ €11B Mar 2026) selling BNP/Orange/Schneider plus US F500 EU-subs on data-residency. Sarvam ($41M Dec 2024, agent platform Q1 2026); Manus AI viral Mar 2025, Coze (ByteDance) — non-investable US-LP but real. US Commerce auth for G42/Humain chips (Nov 2025) made export controls a diplomatic bargaining chip. EU AI Act enforcement late 2026 = binary event. Stage: **Genesis crossing to Custom**.

### Opportunities

**4.1 EU AI Act procurement-readiness for US vendors selling into EU.** Enforcement begins late 2026; GPAI rules already binding. US vendors with EU F500 customers need an audit-ready stance — agent classification, transparency obligations, conformity for high-risk uses. Bet #1 extension into regulated geo. Mistral's €11B is half-priced on EU-sovereign positioning; EU-subs actively ask.
*Conf 4 · TTM 3 · Claim 4.* **Falsifiability:** EU AI Act enforcement is paper-tiger through 2027 → demand stays niche, advisory price compresses.

**4.2 Sovereign-agent vendor evaluation for US F500.** F500s with G42-region ops (Emirati banks, Saudi Aramco, Indian conglomerates) procure local-sovereign platforms (Falcon-derived, Sarvam, Humain-aligned) alongside Claude/GPT-5/Gemini. No neutral framework for "when do we use Mistral vs. Claude in the EU sub" — operator who writes it owns it.
*Conf 3 · TTM 3 · Claim 3.* **Falsifiability:** Hyperscalers ship region-pinned versions of frontier models with auditable data-residency by Q4 2026 → sovereign selection collapses into region selection.

**4.3 Sovereign procurement playbook as Bet #1 export.** Bet #1 ports laterally to sovereign procurement offices (UAE PIF, KSA Humain, India MeitY, Singapore IMDA). Inference, not citation: sovereign offices procure via Big-4 (Deloitte/EY/Accenture); claimability real but contested for a NYC operator.
*Conf 2 · TTM 2 · Claim 2.* **Falsifiability:** Deloitte / Accenture publish their "sovereign AI procurement framework" by Q3 2026 → window closed before it opens.

### Challenges

**4.A Export-control volatility reprices vendor selection mid-deal.** Nov 2025 Commerce auth for G42/Humain signaled "negotiated, not blanket." A single EO or court ruling re-locks the door, stranding F500 customers mid-procurement. Bet #1's playbook needs a geopolitical risk register — adds value, also shelf-life decay.
*Sev 4 · Prob 4 · Exp 4.* **Watch:** Court ruling on Trump Dec 2025 EO; new BIS entity-list update touching agent infra.

**4.B EU AI Act enforcement is paper-tiger.** Tracker Crux #4. If first late-2026 actions are token (€1–10M fines, no operational injunctions), "EU procurement readiness" caps at niche. Bet #1's EU lateral compresses.
*Sev 3 · Prob 3 · Exp 4.* **Watch:** First GPAI fine size and whether Commission issues operational injunctions.

### Open Questions

**4.i Does Mistral consolidate as Europe's defensible enterprise-agent platform?** €600M Mar 2026 funded the bet. Le Chat Enterprise ARR (€100M+ inferred) real but small. Do EU F500s standardize on Mistral by 2027, or treat it as a "data-residency sidecar" to Claude/GPT?
*Dec 3 · Asym 4 · Bet 4.* **Answer-event:** Mistral discloses (or leaks) >€250M ARR with named F500 EU-sub anchors by EOY 2026.

**4.ii Do sovereign agent platforms (Falcon/Humain, Sarvam, Manus) procure US-style?** Sovereign procurement timelines 9–24 months; first major awards 2026–2027. Open: does Bet #1's framework port, or is sovereign procurement relationship-driven (Big-4 + government) and structurally closed to a NYC operator?
*Dec 2 · Asym 4 · Bet 4.* **Answer-event:** UAE PIF / KSA Humain / India MeitY publish a public agent-procurement framework or first major contract award.

---

## Score discipline check

Opp sums (Conf+TTM+Claim, max 15): 2.1 = 14 (Anthropic-curious bias check passed — score earned by ahead-of-peers SDK primitives); 1.2 = 13; 1.1, 2.2, 3.1, 3.2, 4.1 = 12; 1.3, 2.3, 3.3 = 10; 4.2 = 9; 4.3 = 6 (honest floor — Alex is NYC enterprise, not sovereign-Big-4). Two at 13+; bulk in 10–12; floor at 6. Lens held. Inference flagged inline (3.2 ARR projection; 4.3 sovereign port).

*End B1. Feeds AI_AGENTS_ADDENDUM; surfaces candidate bets adjacent to #1 / #3 / #4.*
