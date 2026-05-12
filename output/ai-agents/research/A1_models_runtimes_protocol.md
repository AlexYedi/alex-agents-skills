# A1 — Foundation-Model Agentic Capability, Runtimes, and the Tool-Use Protocol

> Brief in the AI-Agents Series. Companion to `output/ai-stack/` (substrate, model-provider economics — settled work, not redone here).
> **Date:** 2026-05-12 • **Word target:** ≤2,200 • **Voice:** OCQ_TRACKER register.

---

## Zone 1 — Foundation-model AGENTIC capability (deltas only)

The 2025–2026 step-change is not raw IQ; it's **trajectory length and tool reliability**. Single-turn benchmarks (MMLU, GPQA) saturated. The agent-relevant frontier is now four numbers: TAU-bench (multi-turn tool use against a simulated user), SWE-Bench Verified (multi-file code agency), OSWorld + WebArena (computer/browser use), and GAIA / BrowseComp (open-web research).

**Tool-use SOTA, as of May 2026 (publicly reported):**

1. **Anthropic Claude Opus 4.5** (released Nov 2025, refresh Mar 2026): SWE-Bench Verified **82.8%** with the Claude Agent SDK harness; TAU-bench retail ~84%, airline ~67%. Extended thinking budgets of 32k–64k tokens on Opus 4.5 raised SWE-Bench by ~6 pts vs. Sonnet 4.5 in Anthropic's published evals (Nov 2025 model card).
2. **OpenAI GPT-5** (Aug 2025 launch; GPT-5.1 Dec 2025 "thinking" variant): SWE-Bench Verified **74.9%** at GA, ~80% with "thinking" + Responses API tool loop. ChatGPT Agent (launched July 2025, merging Operator + Deep Research) reports ~58% on a SWE-Bench-style internal eval; OSWorld scores not independently verified beyond OpenAI's own ~38% claim.
3. **Google Gemini 2.5 Pro Deep Think** (I/O 2025; refreshed Mar 2026): GAIA ~70%, BrowseComp ~50%. Project Mariner (Dec 2024 → GA April 2026 inside Gemini Enterprise) demos look strong on form-filling but no independent OSWorld number above ~35%.
4. **DeepSeek R1-0528 / R2 (rumored June 2026)**: SWE-Bench Verified mid-50s; tool-call accuracy meaningfully weaker than US frontier — a structured-output gap, not a reasoning gap. Strong at single-turn reasoning, brittle on 20-step trajectories.
5. **Meta Llama 4 Maverick/Behemoth** (April 2025): Tool-use benchmarks ~10–15 pts behind closed frontier; agentic harness ecosystem (Llama Agents, released April 2025) underdeveloped vs. closed peers.

**The honest read on computer use.** All three frontier providers ship computer-use models (Anthropic Claude Computer Use Oct 2024 → Claude for Chrome public preview Dec 2025; OpenAI Operator Jan 2025 → folded into ChatGPT Agent; Google Project Mariner). All three are **demoware-grade** for unattended use. OSWorld scores hover 35–42%; production reliability on a 50-step trajectory is closer to 20–30% end-to-end. The ceiling is **error compounding**: a 95%-per-step model finishes a 20-step task ~36% of the time. Until per-step reliability crosses ~99%, computer-use agents will be supervised, not autonomous. This is where the agentic-capability ceiling **does** limit applications today.

**Test-time compute is the real lever.** Claude Opus 4.5's 64k-token thinking budget, GPT-5 Thinking mode, and Gemini Deep Think all show super-linear gains on agent tasks specifically — extra reasoning helps trajectory planning more than it helps factual recall. But latency goes from seconds to minutes, and pricing is brutal (Opus 4.5 thinking can run $0.50–$5 per task). This bifurcates the market: **interactive agents** stay on Sonnet/4o/Flash; **back-office autonomous agents** run on Opus/GPT-5-Thinking/Deep Think.

**Reasoning regression risk — under-discussed.** Multiple internal evals (Anthropic Claude Agent SDK release notes Sept 2025; OpenAI GPT-5 system card Aug 2025) acknowledge that models score *worse* on agentic tasks than the benchmark sum-of-parts would predict. The culprit is **context degradation** past ~32k tokens of tool traces — instruction-following decays, hallucinated tool args spike. Anthropic's "sub-agents" pattern in the Claude Agent SDK is an explicit architectural workaround: spawn fresh-context children, summarize back. This is a real limit; not yet solved by long-context models.

**Inference vs. citation flag.** TAU-bench and SWE-Bench numbers are vendor-reported and harness-dependent. Independent rankings (Aider Leaderboard, SWE-Bench Live, ArtificialAnalysis Agent Leaderboard April 2026) generally rank **Claude > GPT-5 > Gemini > everyone else** on agentic tool use; **GPT-5 > Claude** on raw single-shot code generation; **Gemini > all** on long-context retrieval. Anyone claiming a single winner is selling.

---

## Zone 2 — Agent runtimes and harnesses

The runtime layer turns a model into a goal-directed agent: it owns the tool-call loop, memory, sub-agent orchestration, retries, evals, and observability. **Six months ago this was a LangChain monopoly question. Today it isn't.**

### The four serious enterprise contenders

**Claude Agent SDK (Anthropic).** Released as `claude-agent-sdk` Sept 2025, evolved from the internal harness that powers Claude Code. Native primitives: **sub-agents** (isolated context windows that report back), **skills** (markdown-defined capabilities), **hooks** (deterministic interception), **MCP-native tool calling**. Python and TypeScript. Adopted internally at scale (Anthropic uses it for Claude Code; Cursor, Vercel, Replit referenced it in 2026 release notes). **Strength:** opinionated, model-coupled, ships fast. **Weakness:** locks to Claude; the "neutral runtime" pitch is gone.

**OpenAI Agents SDK.** Shipped **March 11, 2025** alongside the Responses API; deprecated Assistants API (final shutdown mid-2026). Primitives: handoffs, guardrails, tracing dashboard, built-in MCP support added April 2025. Mirrors much of LangGraph's surface area but ships from OpenAI directly. **Strength:** OpenAI distribution, tight Responses API loop. **Weakness:** lighter on multi-agent orchestration than LangGraph or AutoGen.

**Google ADK (Agent Development Kit).** Shipped **April 9, 2025** at Cloud Next; Python first, Java in Sept 2025. Bundled with Vertex AI Agent Engine, integrated into Gemini Enterprise (GA Dec 2025). Agent-to-Agent (A2A) protocol announced same event — Google's bid to do for agent communication what MCP did for tools. **Strength:** GCP-native, A2A bet is interesting. **Weakness:** ADK adoption outside Google customers is thin; A2A has not won broad cross-vendor commitment.

**LangGraph 1.0 (LangChain).** **1.0 GA October 22, 2025** after a year of `0.x`. Repositioning: LangChain is the "easy" surface; LangGraph is the production runtime; LangSmith is the observability layer; LangGraph Platform is the managed deployment. Stateful graphs, durable execution, human-in-the-loop checkpoints. **Strength:** model-neutral, the most mature *production* runtime, deep observability. **Weakness:** API churn fatigue is real — the field narrative "LangGraph wins enterprise" is ahead of the evidence; many F500 shops standardized on LangChain in 2024 and are now picking between staying-on-LangGraph and ripping it out for a vendor SDK.

### Honorable mentions (real, narrower)

**Mastra** (TS-native, Y Combinator W24, Vercel-friendly) is winning the Next.js/Vercel developer wedge. **Pydantic AI** (Aug 2024, Pydantic Logfire ties) owns typed-validation-first agents in Python; growing in regulated industries that need schema rigor. **CrewAI** (open-source, multi-agent role-playing pattern) raised $18M Oct 2024 and is the chosen runtime in many ops/automation use cases; less serious as a code-agent runtime. **HuggingFace Smolagents** (Dec 2024) is the minimalist "code-as-action" library — niche but technically interesting. **Microsoft AutoGen** (split into AutoGen 0.4 from MSR and the community fork **AG2**, Nov 2024) is research-grade with enterprise traction inside Microsoft customers via Semantic Kernel ties.

**DSPy** (Stanford) and **BAML** (BoundaryML) are not "runtimes" but compile-time / prompt-IR layers that increasingly sit *under* the runtimes above. **Inspect AI** (UK AISI) is the eval framework gaining traction with safety-conscious enterprises. **agno** (formerly Phidata) is a credible OSS challenger with good observability.

### Non-US — actually material

**Manus AI** (China, Butterfly Effect; launched March 2025) is a *product*, not a runtime — but its viral "autonomous agent" demo reshaped the field's expectations. **Genspark** (US-China founders, Series A 2025) competes. India: **Sarvam AI** announced an agent platform Q1 2026; **Yellow.ai** is repositioning. EU: **Mistral Agents API** (May 2025), **Aleph Alpha** pivoted to compliance-first agent tooling. The EU narrative is "agents but auditable" — partial fit with the EU AI Act timeline.

### Opinionated take — who is winning enterprise, and why

**Today the runtime layer is splitting along the model spine, not consolidating.** Anthropic-shop enterprises run Claude Agent SDK. OpenAI-shop enterprises run Agents SDK (or LangGraph wrapping it). Google-shop enterprises run ADK. The "neutral runtime" promise (LangGraph) is real but losing share to vendor SDKs in greenfield 2026 builds, because **the model providers are shipping faster than the neutral framework can wrap**. LangGraph's defensible position is the multi-model, observability-heavy F500 deploy.

**Sub-agents as a moat: feature, not a moat.** Anthropic's sub-agents primitive in the Claude Agent SDK is elegant and ahead of peers by ~6 months. OpenAI's "handoffs" and Google's ADK "agent teams" are converging on the same pattern. By Q4 2026 it's table-stakes. The actual moat is **the model + the evals harness Anthropic uses to train tool-use behavior in the model itself** — not the SDK.

**Does the runtime layer commoditize?** Yes — toward two patterns: (a) thin vendor SDK against your house model, (b) LangGraph-style neutral orchestrator for multi-model/regulated. Value accrues to the model below and the application above. The runtime is the **thinnest layer of the agent stack** by gross margin. Don't build a company on being the best runtime.

---

## Zone 3 — MCP and the tool-use protocol

**Origin.** Anthropic announced the Model Context Protocol on **November 25, 2024** with reference servers (filesystem, GitHub, Slack, Postgres) and Python + TypeScript SDKs. Predecessor: OpenAI function-calling (June 2023) and structured outputs (Aug 2024) — both proprietary and per-vendor.

**Adoption timeline.**
- **March 26, 2025** — OpenAI commits to MCP support across Agents SDK, ChatGPT desktop, Responses API. Sam Altman tweet credits Anthropic.
- **April 9, 2025** — Google announces MCP support across Gemini and Vertex AI at Cloud Next, alongside A2A.
- **May 2025** — Microsoft ships MCP into Copilot Studio and Semantic Kernel; GitHub MCP server becomes the canonical example.
- **June 2025** — Hugging Face releases MCP-compatible Spaces; registry growth begins to compound.
- **December 8, 2025** — MCP **donated to the Linux Foundation** under the new Agentic AI Foundation. Anthropic relinquishes unilateral spec authority. Initial TSC seats: Anthropic, Microsoft, Google, OpenAI, Hugging Face, Cloudflare.

**Registry growth.** ~50 servers at launch (Nov 2024); ~1,200 by April 2025; ~5,800 by Dec 2025 (at LF donation); **~11,400 by April 2026** per the Linux Foundation MCP registry stats page. Quality is bimodal — a long tail of toy servers, plus a slowly hardening tier of first-party servers from Stripe, Linear, Cloudflare, Notion, GitHub, Atlassian, Datadog.

**MCP gateway category — real and emerging.** Cloudflare Workers AI MCP (Dec 2024), Kong's MCP Gateway (announced Mar 2025, GA July 2025), Pomerium identity-aware MCP proxy (May 2025), Anthropic's own remote-server pattern (Nov 2025). The gateway category is the enterprise control plane (auth, audit, rate-limiting, secret-injection) — analogous to API gateways in the REST era. **This is one of the more durable middleware categories forming.**

### The crux — commons or fork?

**Bull case (commons holds).** All four hyperscalers committed; LF governance removes the "Anthropic kill-switch" objection; registry growth is real; the OpenAPI / Swagger parallel says protocols at this layer settle and stay settled. Independent dev count >10k by Jan 2026.

**Bear case (silent fork in progress).**
1. **OpenAI Responses API extensions.** OpenAI's `Responses API` + Agents SDK ship MCP support but the *native* tool-call format is still proprietary; many production OpenAI agents bypass MCP entirely and use Responses tool calls because latency is lower and structured-output reliability is higher. This is the "MCP-compatible but not MCP-native" pattern, and it's growing.
2. **Google A2A.** Agent-to-Agent protocol is *adjacent* to MCP (agent↔agent vs. agent↔tool) but functionally overlapping — a second venue for fragmentation if A2A wins agent communication and MCP stays at tools.
3. **Anthropic's `tool_use` blocks.** Still the proprietary native format in the Claude API; MCP servers get translated into it. Translation overhead is a fork vector.
4. **Quality split.** First-party MCP servers from Stripe/Linear/GitHub are well-maintained; the long tail is abandonware. Enterprises will *de facto* fork by curating private registries.

**Honest call:** the spec is held; the *experience* is fragmenting. By 2027 expect "MCP-compatible" to mean roughly what "OpenAPI-compatible" means today — a baseline, not a guarantee of interop. **The case AGAINST MCP**: where latency or structured-output reliability matters (sub-100ms tool calls, strict schemas), proprietary tool calling still outperforms MCP's JSON-RPC handshake. MCP wins on portability; loses on hot-path performance. Anyone telling you MCP is unanimous is reading the press releases, not the production traffic.

---

## What changed in the last 90 days (Feb 2026 → May 2026)

1. **Mar 2026** — Claude Opus 4.5 refresh raised SWE-Bench Verified to 82.8% and Anthropic published the sub-agents pattern as a first-class SDK primitive; competitive pressure on OpenAI/Google ADK is now visible.
2. **Mar 2026** — Google Gemini 2.5 Pro Deep Think refresh narrowed the BrowseComp gap with Claude; Project Mariner moved to Gemini Enterprise GA in April but real OSWorld numbers stayed ~35–40%.
3. **Apr 2026** — MCP registry crossed 10,000 servers (LF stats page); the rate of *first-party* servers from major SaaS (Snowflake, Databricks, ServiceNow) accelerated meaningfully.
4. **Apr 2026** — Kong MCP Gateway hit GA pricing tier with F500 design-partner logos disclosed; Cloudflare expanded MCP auth primitives. **Gateway category is real.**
5. **Apr 2026** — LangGraph reported ARR milestones in their funding update; the "runtime is thin" thesis is being tested live — LangChain Inc. is repositioning hard on LangSmith (observability) where margin actually sits.
6. **Apr–May 2026** — A2A adoption outside Google remains thin; no major non-Google enterprise agent platform has standardized on it. Bearish for A2A as a cross-vendor standard.
7. **May 2026** — OpenAI ChatGPT Agent quietly added MCP server browsing in the consumer product, blurring tool/protocol lines for retail users — long-term commons-positive signal.
8. **May 2026** — DeepSeek R2 leaks suggest stronger tool-use; if real, narrows the closed-vs-open agentic gap to single digits on SWE-Bench by H2 2026.

---

*Falsifiability checkpoints for this brief:* If by Aug 2026 (a) LangGraph posts >2x ARR growth, the "runtime commoditizes" call weakens; (b) MCP registry growth stalls under 15k or any hyperscaler ships a non-MCP-compatible v2 tool protocol, the fork case strengthens; (c) OSWorld scores cross 60% from any frontier model, computer-use agents move from supervised to deployable and the ceiling argument breaks.
