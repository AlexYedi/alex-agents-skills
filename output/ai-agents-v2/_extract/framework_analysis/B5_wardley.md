# B5 — Wardley Map of the Agent Stack

**Date:** 2026-05-12 · **Principal:** Alex Yedi · **Scope:** agent layer specifically (above foundation models, below end-user surfaces). Companion to the prior Wardley register in `build_addendum.js` Part VII — this brief refreshes placement at the **agent** stratum; silicon, fabric, and training layers not re-mapped.

---

## What Wardley says about agents right now

Most of the agent stack is not where its press releases place it. The narrative is "MCP won, computer use is here, agents are deploying"; the map shows MCP is a stable spec with a fragmenting experience, computer use is Genesis-bordering-Custom, and most "production agents" are 3–7 step ReAct loops with a verifier. Evolution is **bifurcated**: infrastructure under agents (sandboxes, browsers, gateways, TTS, telephony) is on a 24-month commodity trajectory; the operational layer above (evals, observability, guardrails, procurement controls, vertical workflow integration) is Custom-to-early-Product and is where durable margin lives. **The field is not consolidating, it is stratifying** — surfaces below the runtime commoditize fast; vertical and compliance layers harden into moats. That is the strategic terrain.

---

## Anchored user needs (top of map)

1. **Complete a multi-step research-and-reporting task autonomously** — the deep-research / GAIA / BrowseComp use case (Anthropic Research, OpenAI Deep Research, Gemini Deep Research, Manus, Genspark).
2. **Operate a browser or computer to complete a back-office workflow** — claims, expense, vendor onboarding; the CFO-credible "AI BPO" pitch.
3. **Handle a customer query end-to-end with voice + tools + escalation** — Sierra/Decagon/Hippocratic/Vapi pattern; the only domain where outcome pricing has landed.
4. **Write, test, and merge a production code change** — Claude Code / Cursor / Codex / Devin / Augment; the only category where AI labor is priced like FTE displacement at scale.

Function-different, not vertical variants. Each anchors a distinct dependency chain.

---

## Layer-by-layer placement

| Component | Stage | Rationale | Travel |
|---|---|---|---|
| **End-user surfaces** | | | |
| Chat web/desktop | Product | ChatGPT ~800M WAU; UI commodity. | → Commodity casual; Custom high-stakes |
| Chat mobile | Product | Apple Intelligence default; ChatGPT 250M MAU. | → Commodity bundled with OS |
| CLI (Claude Code, Codex CLI) | Product | Claude Code ~$500M ARR-run-rate. | → Product, slow commoditization |
| IDE inline (Cursor, Copilot) | Product | Cursor ~$500M; Copilot ~22M seats. | → Stratified; Cursor/Copilot durable |
| Browser sidebar (Comet, Claude for Chrome) | Custom → Product | Comet 5M downloads; enterprise blocked >60%. | → Product consumer; stalls regulated |
| Embedded SaaS (M365 Copilot, Agentforce) | Product | Copilot $5B ARR, ~30M seats. | → Commodity bundled |
| Computer use (Operator, Mariner, Claude CU) | **Genesis → Custom** | OSWorld 50–55%; 50-step ~20–30%. | → Custom late 2026 if OSWorld 65%+ |
| Voice (Advanced Voice, Gemini Live) | Custom → Product | <800ms voice-to-voice crossed Q1'26. | → Product mid-2026 short calls |
| Wearable/AR | Genesis | Ray-Ban Display 2M; pendants dead. | → Custom 2027 for glasses |
| **Vertical agents** | | | |
| CX (Sierra, Decagon) | Custom → Product | Sierra $175M; per-resolution pricing exported. | → Product 2026; 2-winner |
| Knowledge (Glean, Hebbia) | Custom → Product | Glean $300M ARR. | → Product 2026; ChatGPT Business encroaches |
| Legal (Harvey) | Custom | $100M ARR, AmLaw100 lock-in. | → Product 2027; most defensible |
| Healthcare (Abridge, Hippocratic) | Custom | HIPAA/FDA fence. | → Product 2027; lowest encroachment |
| RevOps (Clay, 11x) | Custom (struggling) | 11x flat $20M; Clay only durable winner. | → 1–2 winners |
| Coding (Cursor, Claude Code) | Product | Multi-winner prosumer; winner-take-most enterprise. | → Lab bundling threat |
| Finance (Rogo, Ramp AI) | Custom | NYC-anchored; per-seat $1–5K/banker. | → Custom through 2027 |
| Creative (ElevenLabs, Runway) | Product | ElevenLabs $200M, Runway $100M. | → Product; Suno RIAA risk |
| Sovereign (Mistral, Sarvam, Manus) | Custom | Residency wedge. | → EU Act enforcement = catalyst |
| **Action surfaces** | | | |
| Sandboxes (E2B, Modal, Vercel) | Product | Firecracker+Linux convergence. | → Commodity by 2027 |
| Browser automation (Browserbase, Playwright) | Product | Browserbase ~$50M; Playwright the floor. | → Commodity surface; ops layer durable |
| Voice substrate (LiveKit, Cartesia, Twilio) | Product → Commodity | Sonic-2 sub-50ms. | → Commodity 2026–27 |
| Voice orchestration (Vapi, Retell, Bland) | Custom → Product | Compliance gating Q1'26. | → Product 2026, consolidation |
| **Runtimes & SDKs** | | | |
| Claude Agent SDK | Custom → Product | Sub-agents primitive ahead ~6mo. | → Product, model-locked |
| OpenAI Agents SDK | Custom → Product | Assistants deprecation mid-2026. | → Product 2026 |
| Google ADK + A2A | Custom | Thin outside GCP. | → Custom; A2A uncertain |
| LangGraph 1.0 | Product | Oct'25 GA; LangSmith is the margin. | → Margin moves to obs |
| Mastra, Pydantic AI, CrewAI | Custom | Real but narrow. | → Niche Product 2026 |
| **Protocol** | | | |
| MCP spec | Product (held) | LF Dec'25; 11.4K servers Apr'26. | → Spec held; experience fragments |
| MCP gateways (Cloudflare, Kong, Pomerium) | Custom → Product | Kong GA Jul'25; F500 design-partners. | → Product H2 2026 |
| First-party MCP servers (Stripe, GitHub, Linear) | Product | Well-maintained. | → Product; long-tail abandonware |
| A2A | Genesis | No cross-vendor commitment. | → Stays Genesis or dies |
| **Memory & state** | | | |
| Lab-native memory (ChatGPT, Claude Projects) | Custom → Product | Claude Projects GA Apr'26. | → Product 2026; absorbs consumer |
| Standalone (Mem0, Letta, Zep) | **Genesis → Custom** | <50K dev accts vs. 800M lab MAU. | → Niche-compliance or absorbed |
| GraphRAG / LightRAG | Custom | Two with production traction. | → Selective Product H2'26 |
| **Planning & reasoning** | | | |
| Reasoning models (o3, Opus thinking, Deep Think) | Product | Buyer-controllable `reasoning_effort`. | → Product; cost curve steep |
| Planner-executor split | Product | Gateway config flag. | → Commodity routing pattern |
| RLVR / GRPO trajectory fine-tune | Genesis → Custom | DeepSeek recipe public. | → Custom 2026 vertical agents |
| **Eval, obs, safety** | | | |
| LLM tracing (OTel GenAI) | Product | Stabilized Jan'26. | → Commodity ingest |
| Eval platforms (Braintrust, LangSmith, Galileo) | Custom → Product | Eval logic = lock-in; ~$300M ceiling. | → Product 2026; 2–3 winners |
| Inspect AI / OSS eval | Custom | Cited in EU Act drafts. | → Audit-grade Custom |
| Runtime guardrails (Lakera, NeMo) | Custom → Product (bundled) | Protect AI → PANW $700M was the bell. | → Mostly absorbed by 2027 |
| **Procurement-grade controls** | | | |
| Signed eval reports, multi-party audit, EU Act tie-out | **Genesis** | No vendor turnkey today. | → Stays Genesis through 2026 |
| Action-confirm / tool-boundary policy | Custom | Bespoke; sub-agents pattern closest. | → Product 2027 |

The honest pattern: **bottom of the stack commoditizes on a 24-month timer**, **runtimes split along model spines rather than consolidate**, **vertical layer hardens into 1–2-winner segments**, and **procurement-grade controls do not yet exist as products**. Two zones the field thinks are Product but honestly aren't: standalone memory and full computer use.

---

## The 5–7 punctuated equilibria for 2026–2027

**1. MCP gateways: Custom → Product (H2 2026).** Kong GA, Cloudflare expansion, Pomerium identity-aware proxy. The enterprise control plane (auth, audit, rate-limit, secret-injection) hardens. Reprices custom-MCP builds; adjacent-possible = MCP-native iPaaS, policy-firewall products, F500-private registries. **Sharpens Bet #3: the gateway sub-category, not the spec itself, is the punctuation.**

**2. Computer use: Genesis → Custom (mid-to-late 2026).** OSWorld 50–55% crosses ~65% on a frontier system; end-to-end reliability ~30% at 50 steps. Stage jump, not commoditization — *piloted-in-narrow-lanes*, not deployable. Reprices RPA (UiPath, Automation Anywhere); adjacent-possible = AI-augmented BPO at 1/5 cost for reversible/auditable click sequences. **Unattended autonomous computer use stays a 2027–2028 question.**

**3. Voice telephony substrate: Product → Commodity (mid-to-late 2026).** LiveKit + Cartesia + OpenAI Realtime + Twilio/Telnyx is a stack default; sub-600ms for short calls. Substrate commoditizes; **voice-orchestration (Vapi, Retell, Bland) consolidates to 1–2 winners** with compliance as the moat. Reprices Genesys/NICE/Five9; adjacent-possible = vertical voice (healthcare intake, debt collection, dental, field-service).

**4. Standalone memory: forced binary, resolves H2 2026.** Either Mem0/Letta/Zep harden the compliance wedge (Zep most likely; ~$50M ARR by 2027), or absorbed — lab-native at consumer end, runtime primitives at developer end. **My read: absorbed for consumer/prosumer, niche-standalone for compliance enterprise.** Memory's access pattern is RAG-with-writes, not a distinct primitive. Refreshes CRUX #5; rolls memory architecture into Bet #5.

**5. Procurement-grade agent controls: Genesis → Custom (Q4 2026).** No vendor today ships signed eval reports + multi-party audit + EU Act conformity + action-rollback + adaptive-adversary red-team turnkey. EU AI Act GPAI enforcement starts Aug 2026; first conformity draft (Feb 2026) names Inspect AI explicitly. First Custom solutions emerge from Big-4 consulting + a Lakera-shaped partner. **The unclaimed flag for Bet #1.**

**6. Eval/observability consolidation: Product (Q4 2026 – H1 2027).** OTel stabilization killed ingest lock-in; eval logic remains. ~$300M ARR ceiling. LangSmith stays (LangGraph-bundled); Braintrust likeliest consolidator; Langfuse wins EU/self-host; 2–3 of {Galileo, Patronus, HumanLoop, Comet, Helicone, AgentOps} acquired by EOY 2026. **Reprices the pure-play eval thesis from defensible to acquisition-target.**

**7. Foundation labs walking up-stack (continuous 2026).** ChatGPT Business connectors, Claude for Work, Gemini Enterprise. Reprices Glean, Notion AI, Copilot 365's monopoly. **Adjacent-possible:** vertical-agent companies with deep workflow integration + outcome SLAs + custom guardrails (Sierra, Decagon, Harvey, Hippocratic) are *least* vulnerable — moat is integration + change-management, not the model. Confirms Bet #2.

---

## Strategic quadrants

### Pioneer (Genesis — build/explore, expect failures)
- **Procurement-grade signed eval bundles** (no vendor turnkey; Inspect AI closest).
- **Computer use for unattended back-office** (30% reliability at 50 steps).
- **Multi-party agent audit** (vendor + customer + auditor on one trace with redaction).
- **Contextual-integrity primitives for memory** (no vendor ships "written in B2B sales, refuse to surface in HR").
- **Sovereign agent stacks for EU AI Act–exposed F500 EU-subs** (Mistral-equivalent partner play).
- **MCP-native iPaaS replacing Zapier** (technically possible; no winner).

### Settle (Custom → Product — productize what works)
- **MCP server constellations for enterprise GTM SaaS** (Salesforce, Outreach, Gong, Highspot, Zoominfo, Linear) — Bet #3's buildable target.
- **Vertical voice agents** (debt collection, healthcare intake, NPS-detractor recovery) — substrate commodity, vertical packaging + compliance the moat.
- **Vertical AI workers with deep workflow integration** — Sierra/Decagon/Harvey/Hippocratic pattern; **Bet #2 = take a GTM role inside one rather than build one.**
- **Enterprise-acceptance eval/obs** (SOC2, model-risk, signed reports, red-team artifacts) — "Drata for AI agents."
- **AI procurement / deal desk SaaS** — Bet #1's downstream product.
- **Memory architecture as a service line** (folded into Bet #5).

### Consume (Product → Commodity — rent, don't build)
Foundation models via API or AI Gateway. Sandboxes (E2B, Modal, Vercel Sandbox). Headless browsers (Browserbase + Playwright). Voice substrate (LiveKit, Cartesia, Deepgram, Twilio/Telnyx). Agent runtimes — use the SDK of your dominant model provider. MCP transport + first-party servers. AI gateways (Vercel, Cloudflare, OpenRouter). Vector DB / embeddings / rerankers (pgvector or Turbopuffer + Voyage / Cohere). OTel GenAI tracing.

### Utility / Build-around (ubiquitous)
Linux, Postgres, Chromium, WebRTC, Firecracker, Python/TypeScript, PyTorch, public internet, Kubernetes, OTel, Markdown, JSON-RPC.

---

## Implications for Alex

Alex's compounding advantage is enterprise GTM judgment (12 years, F1000-buyer-side scar tissue) plus AI-builder fluency. That fits **Settle**, with a Pioneer flag on procurement-grade controls and disciplined Consume on everything below the runtime. The agent-layer map sharpens the prior bet stack in three specific ways.

**PIONEER (write, observe, do not build yet).** The unclaimed flag is **procurement-grade agent controls** — signed eval reports, multi-party audit, EU Act tie-out, action-rollback, adaptive-adversary red-team — sold first as a buyer-side audit framework, not a vendor product. This is **Bet #1's Wardley-defensible position**: not "Drata for AI" (Settle-quadrant SaaS, harder cold-start) but the **buyer-side Playbook that names the gap** between what vendors ship (A6's #1, #2) and what regulators will require (#3, #4, #5). Plant the flag with the open Playbook; SaaS is a downstream option, not the first move. Conviction up.

**SETTLE (highest-conviction zone — productize a known pattern).** Two positions:
1. **Bet #2 (vertical agent GTM role).** Wardley confirms vertical-workflow integration is the durable moat against lab encroachment. The Talent Flow target list is correctly placed; this refresh adds **Rogo, Hebbia, Clay, Runway** as NYC-native targets the prior register missed. Sierra remains most-aligned (NYC dual-HQ, Stripe/Ramp/Salesforce alumni pipeline, per-resolution pricing = the only validated outcome-pricing wedge).
2. **Bet #3 (MCP-native enterprise integration practice).** Timing sharpens: the **gateway sub-category** is the punctuation. Window for MCP servers for enterprise GTM SaaS is Q2–Q4 2026; window for gateway-adjacent policy/audit tooling is H2 2026 on. Falsifiability unchanged: any major vendor unilaterally extending MCP without spec coordination kills it.

**CONSUME (do not reinvent).** Silent leverage. Anything below the agent runtime — sandboxes, browsers, voice, telephony, vector DBs, embeddings, gateways, OTel, first-party MCP servers — rent it. 24-month commoditization timer is favorable; build cost is unfavorable; differentiation is zero.

**Where the map disagrees with the field.**
- "MCP won" is half-true — spec held, experience fragmenting (Anthropic `tool_use`, OpenAI Responses, Google A2A overlap). Bet #3 plans for "MCP-compatible baseline," not "MCP-native interop guarantee."
- "Computer use is here" is wrong for unattended autonomous work through 2026. Error-compounding (95%/step × 20 steps ≈ 36%) is the hard ceiling. Bet on watched/narrow products; do not bet on autonomous back-office agents to clear F500 procurement before mid-2027.

**Non-US placement.** Sovereign agents sit one stage earlier than US peers: **Mistral Le Chat Enterprise Custom→Product**, gaining where EU residency is procurement-required (BNP, Orange, Schneider, US F500 EU-subs); **Sarvam, Manus, Coze Custom**, politically-funded, US-LP-non-investable in the Chinese cases. EU AI Act enforcement (late 2026) is the catalyst that could move Mistral-equivalents from Custom to Product inside Europe — direct overlap with Bet #1.

**Bet inheritance, refreshed.** Bet #1 holds (★★★★★) with Pioneer-flag sharpening. Bet #2 holds (★★★★★) with expanded NYC target list. Bet #3 holds (★★★★) with timing shifted to the gateway sub-category. Bets #4–#7 unchanged by the agent-layer map.

Strong opinions weakly held. The single call most likely to move within 90 days: **computer use Genesis→Custom**. If OSWorld crosses 65% on one frontier system before September 2026, back-office automation becomes viable a quarter earlier than this brief assumes, and Bet #3 should add an "MCP servers for the systems back-office computer-use agents will need to drive" sub-line. Watch the leaderboard.

---

*End B5. Cross-refs: OCQ_TRACKER Bets #1, #2, #3, #5; CRUX #3, #5. A1 §Zone 3 (MCP fork), A2 §6 (memory compression), A4 §3 (computer-use reliability), A5 §cross-cutting (vertical winners), A6 §Zone 1 close (procurement gap), A7 §thesis (form factor as constraint).*
