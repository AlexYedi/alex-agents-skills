# Chapter 2 — Framework Lenses (agent layer)

Chapter 1 sliced the agent layer into ten sub-strata plus four meta-strata. This chapter re-runs the same five analytical lenses Volume I applied to the eighteen-stratum stack — OCQ, Wardley, Helmer's 7 Powers, Ecosystem JTBD, Talent & Capital Flow — at the resolution where the V1 view went lossy. The convergence principle is unchanged: each lens on its own is mis-calibrated or fashion-driven, but when five independent frames agree at the agent layer they produce signal that survives doubt.

The honest delta from V1 Ch 2 is that the agent layer is hotter. Cycle time at this resolution is twelve to eighteen months rather than eighteen to twenty-four; the OCQ score distribution naturally tightens because more cells justify a 4 or 5 on Confidence and Time-to-Monetize than the full-stack average. That is the scoring distortion to anticipate; the discipline below is to keep the *Claimability* and *Severity* dimensions doing real work.

V1 Ch 2 still owns the full-stack synthesis — anyone reading this chapter should treat (V1 Ch 2 §2.1–§2.5) as the parent register. What V3 Ch 2 produces that V1 could not: per-sub-stratum scoring inside Stratum XIII, the agent-specific gateway/control-plane read on Wardley, the vertical-by-vertical Power inventory, the seven JTBD jobs (versus V1's six), and the agent-tuned Talent & Capital methodology that surfaces the MBB-to-agent feed-stock V1 missed. Bets, risks, cruxes, and action map live in Ch 3.

## §2.1 OCQ × Agent Sub-Stratum Matrix

### Lens definitions

Carried verbatim from the parent spec (V1 spec §3.3), tightened to agent context per the agent-layer methodology in `_extract/framework_analysis/B1`–`B4`. Same dimensions, same /15 totals.

**OPPORTUNITY (agent layer).** Where in the agent stack value is being created faster than the field's prevailing narrative, AND where can someone with enterprise B2B GTM plus AI-builder skill claim it inside a 12–18 month window before the layer commoditizes. Scored 1–5 on three dimensions:

- **Confidence (C)** — how sure we are the opportunity is real
- **Time-to-Monetize (T)** — 5 = soon
- **Claimability (Cl)** — can Alex's profile act on it

Total: /15.

**CHALLENGE (agent layer).** The binding constraint or latent feedback loop that, if it tightens or fires, materially reprices everything above it. Agent-specific: protocol fragmentation, model-vendor reasoning regression, inference-cost spikes, action-consequence liability, eval-trust collapse. Scored:

- **Severity (S)** — how much it reprices
- **Probability (P)** — likelihood it bites
- **Exposure (E)** — how much it affects Alex's bets

Total: /15.

**OPEN QUESTION (agent layer).** The agent-specific crux the field is betting on without admitting — does memory become permanent or absorbed; does MCP fork; does computer-use cross 80% reliability in 2026 or 2027; does test-time compute hit diminishing returns; does ASL-4 force a deployment freeze. Phrased as actual questions. Scored:

- **Decidability (D)** — 5 = decidable soon
- **Asymmetry (A)** — how much bets diverge based on the answer
- **Bet-size (B)** — how much the playbook would shift

Total: /15.

Resist 15/15 inflation. The lens produces a distribution, not validation.

### How to use this matrix

Read across to compare sub-strata: where does opportunity intensity cluster, where do challenges concentrate, which open questions are decidable in the next four quarters. Read down a single sub-stratum to balance the three lenses — a 14/15 opportunity with a 13/15 binding challenge in the same sub-stratum is the field of play, not a quiet pasture. The lens is a filter, not validation: if every cell scores 13+, the scoring is broken, not the field. The agent-layer score distribution is naturally tighter than V1's because the field is hot — anticipate Claimability and Severity to do most of the discriminating work. Cross-reference with Plate 2 (Agent OCQ Heatmap) for the visual read.

### Per-sub-stratum scoring

**Stratum I — Foundation models as agentic engines.**

- **Top Opportunity.** Thinking-budget cost-arbitrage advisory — Opus 4.5 thinking runs $0.50–$5/task, most enterprises max-think by default, routing 80% Sonnet/Haiku and 20% Opus-thinking cuts agent spend 4–8× at flat TAU-bench quality. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Foundation labs walking into vertical apps faster than expected — Claude for Chrome, ChatGPT Agent, Gemini Enterprise absorbing the horizontal-agent surface Sierra/Decagon/Glean treat as moat. (12/15 — S:4 / P:3 / E:5)
- **Top Open Question.** Does Opus 4.5's agentic lead survive GPT-5.5 / Gemini 3 within H2 2026? Answer-event: independent SWE-Bench Verified reproduction. (13/15 — D:4 / A:4 / B:5)

**Stratum II — Agent runtimes and harnesses.**

- **Top Opportunity.** Claude Agent SDK + Skills as F500 builder's standard kit — sub-agents, skills, hooks primitives ~6 months ahead of peers; buyer-side Skill catalog (procurement-readiness, vendor-DDQ, RevOps-handoff) empty; a curated open repo of 10–20 enterprise Skills becomes canonical reference. (14/15 — C:4 / T:5 / Cl:5)
- **Top Challenge.** Runtime commoditization compresses Alex's claim window — runtimes become "thin wrapper around model SDK" by H1 2027 if Mastra/Pydantic AI/CrewAI consolidate via acquihire. (11/15 — S:3 / P:4 / E:4)
- **Top Open Question.** Does any independent runtime survive as a $1B+ business? LangChain Inc.'s April 2026 funding update is the bellwether. (11/15 — D:3 / A:4 / B:4)

**Stratum III — Tool use and the Model Context Protocol (MCP).**

- **Top Opportunity.** MCP-gateway buyer-side advisory — Cloudflare/Kong/Pomerium gateway category is the highest-margin durable middleware tier; F500s have zero picking framework; vendor-neutral audit = $50–150K engagement. (12/15 — C:4 / T:4 / Cl:4)
- **Top Challenge.** Silent fork between Responses-API-native and MCP-native hardens in production traffic — already happening with OpenAI agents bypassing MCP for latency. (12/15 — S:4 / P:3 / E:5)
- **Top Open Question.** Does MCP cross the OpenAPI threshold as universal baseline? Answer-event: registry crosses 25k AND >50 SaaS incumbents ship first-party servers by EOY 2026. (14/15 — D:4 / A:5 / B:5)

**Stratum IV — Memory and state.**

- **Top Opportunity.** Memory Audit Lane in the Procurement Playbook (Bet #1 fold-in) — Mem0 shipped GDPR Art. 17 forget APIs only Feb 2026 after losing a deal on deletion-auditability; F1000 InfoSec has no canonical memory-audit checklist. (13/15 — C:4 / T:4 / Cl:5)
- **Top Challenge.** Lab absorption faster than productization window — Claude Projects + Gemini + ChatGPT memory compress the developer-API thesis inside 12 months. (10/15 — S:4 / P:4 / E:2)
- **Top Open Question.** Does a memory-portability standard emerge by 2027 (MCP-shaped memory schema), or do labs fight it for the same lock-in reason they hesitated on MCP? (10/15 — D:3 / A:4 / B:3)

**Stratum V — Planning, reasoning, test-time compute.**

- **Top Opportunity.** Trajectory Cost & Latency Audit (Bet #4 FinOps fold-in) — planner-executor-verifier routes 70–85% tokens cheap; median enterprise running `reasoning_effort=high` on every call for 0–2pt gains at 5–12× cost; audit-and-rewire sellable today. (15/15 — C:5 / T:5 / Cl:5)
- **Top Challenge.** Hyperscaler auto-routing absorbs the FinOps wedge inside 18 months — Bedrock + Vercel AI Gateway + OpenRouter shipping tier routing as config Q1–Q2 2026. (13/15 — S:4 / P:4 / E:5)
- **Top Open Question.** Does test-time compute keep paying past 32k reasoning tokens through 2026–2027? If >32k unlocks new task classes, Bet #4's "10× is waste" frame ages badly. (11/15 — D:4 / A:4 / B:3)

**Stratum VI — Action surfaces.**

- **Top Opportunity.** Form-factor-aware procurement audit chapter for Bet #1 Playbook v2 — buyers mis-price ACVs 3–5× when surface-buyer pair is wrong; F500 buying "an agent" without distinguishing chat/IDE/cron/Slack/embedded buys the wrong thing. (14/15 — C:5 / T:4 / Cl:5)
- **Top Challenge.** Hyperscaler bundling absorbs the operational layer — Bedrock AgentCore (re:Invent 2025) is the leading indicator; integrated "AI action runtime" bundles 12–18 months out. (11/15 — S:4 / P:4 / E:3)
- **Top Open Question.** Does voice outbound get re-zoned by FCC or state TCPA expansion in 2026 — first named TCPA enforcement against an AI-voice vendor moves the O2 wedge from advisory to mandatory. (10/15 — D:3 / A:4 / B:3)

**Stratum VII — Evaluation and observability.**

- **Top Opportunity.** Systematize the "signed reproducible eval report" as a procurement artifact — no vendor ships model-pin + dataset-hash + harness-version + signed chain-of-custody that survives a regulator subpoena; Inspect AI is framework, not procurement artifact. Bet #1's load-bearing wedge. (14/15 — C:5 / T:4 / Cl:5)
- **Top Challenge.** Native model-provider eval eats the bottom — Anthropic published Claude Agent SDK eval harness templates March 2026; OpenAI Traces, Vertex AI Eval, Bedrock Evaluations all live. (11/15 — S:4 / P:5 / E:2)
- **Top Open Question.** Does EU AI Act Article 55 conformity guidance name specific eval frameworks (Inspect AI cited in Feb 2026 drafts)? (12/15 — D:4 / A:4 / B:4)

**Stratum VIII — Runtime safety and guardrails.**

- **Top Opportunity.** Procurement-grade guardrail audit module bundled into Bet #1 Playbook — productize the 5-question diagnostic (tool-boundary policy, rollback, conformity tie-out) as buyer-side audit F1000 risk officers run against vendors. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Hyperscaler bundle absorption window shorter than productization curve — Bedrock Automated Reasoning + Defender for AI + NeMo Guardrails 1.0 cover 80% of cases at zero procurement friction. (11/15 — S:4 / P:4 / E:3)
- **Top Open Question.** Does EU AI Act Art. 55 enforcement give signed-eval-reports legal weight in late 2026? Answer-event: first GPAI Art. 55 fine OR formal conformity-assessment guidance Q4'26–Q1'27. (12/15 — D:4 / A:4 / B:4)

**Stratum IX — Vertical agent products.**

- **Top Opportunity.** Sierra NYC dual-HQ enterprise GTM role — $10B Mar'26 rumored / $4.5B confirmed; Taylor monthly in NYC; Stripe/Ramp/Salesforce alumni pipeline; per-resolution pricing is the segment standard Sierra exported; highest-fit Bet #2 target. (13/15 — C:5 / T:4 / Cl:4)
- **Top Challenge.** Outcome-pricing thesis is CX-only — confirmed at Sierra/Decagon, partial at Hippocratic, failed elsewhere; Sierra/Decagon valuations extrapolated to non-outcome verticals risk 20–30% repricing on Anthropic-ARR lower-bound. (11/15 — S:4 / P:3 / E:4)
- **Top Open Question.** Does Sierra NYC hiring cadence accelerate or stall Q3'26 — Taylor monthly in NYC but Sierra could centralize SF post-$10B round? Answer-event: monthly LinkedIn scrape of Sierra NYC postings. (14/15 — D:5 / A:4 / B:5)

**Stratum X — End-user surfaces and form factor.**

- **Top Opportunity.** "Embedded vs. standalone" advisory for F500 agentic procurement — Microsoft wins more agentic enterprise revenue than any pure-play in 2026; buyers default embedded, pure-plays win on multi-system stitching + custom guardrails; procurement question of 2026–2027 with no incumbent. (12/15 — C:4 / T:4 / Cl:4)
- **Top Challenge.** EU AI Act Art. 14 enforcement breaks cron/webhook surface for regulated enterprise — n8n €55M, Zapier 2.2M paid users; unattended-agent triggers are SMB default; Art. 14 makes cron-Claude auto-replying high-risk. (11/15 — S:4 / P:3 / E:4)
- **Top Open Question.** Does unattended-agent reliability cross ~99%/step in 18 months and flip the binding constraint back to capability from form factor? (13/15 — D:4 / A:5 / B:4)

**Meta-A — Capability-level safety regimes.**

- **Top Opportunity.** Capability-Safety Translation chapter for the Playbook — every frontier vendor's safety posture is a marketing artifact buyers can't evaluate; 8-question audit (which evaluator, pre/post-deployment, adjustment-clause invocation, rollback precedent, EU Code alignment). (12/15 — C:4 / T:3 / Cl:5)
- **Top Challenge.** Anthropic ASL framework's regulatory durability is contested — ASL-3/4 reputationally durable but not baked into EU AI Code of Practice (Aug 2026), NIST AI RMF, or ISO 42001; buyers cannot procure on "ASL-3" as a control. (10/15 — S:3 / P:4 / E:3)
- **Top Open Question.** Does OpenAI's Preparedness adjustment clause get invoked in 2026? Public invocation destabilizes voluntary-safety regimes and EU may shift voluntary to mandatory. (13/15 — D:4 / A:5 / B:4)

**Meta-B — Regulation.**

- **Top Opportunity.** Article 14 human-oversight implementation playbook for agentic systems — April 2026 Commission draft is the most actionable regulatory artifact; F1000 deploying CX/hiring/financial-advisor agents need control mapping, RACI, audit-log spec; sells to compliance + AI governance at $40–100K. (13/15 — C:5 / T:4 / Cl:4)
- **Top Challenge.** EU AI Act stays paper AND US federal preemption succeeds — Crux #4; no named 2026 GPAI fines AND Trump Dec 2025 EO preemption surviving court reduces regulatory advisory from $10B+ category to niche-but-defensible. (11/15 — S:4 / P:3 / E:4)
- **Top Open Question.** Does the EU classify autonomous agents as "high-risk" under Annex III in 2026? Commission guidance placing employment/credit/essential-services agents in Annex III triples Bet #1's TAM. (14/15 — D:4 / A:5 / B:5)

**Meta-C — Economics.**

- **Top Opportunity.** FinOps for Tokens productized advisory (Bet #4 direct) — free first audit × 5 mid-market cos, EAGLE-3 3–6.5×, FP4, prompt caching, planner-executor routing; tight Bet #1 CFO/CIO overlap; targets >$50K/month Claude/GPT burners. (13/15 — C:4 / T:5 / Cl:4)
- **Top Challenge.** Token-price decline makes "optimization" below the line of caring faster than expected — frontier API prices fell 4–10× 2024–2026; another 3–5× in 18 months removes CFO motivation. (14/15 — S:5 / P:4 / E:5)
- **Top Open Question.** Does trajectory-compute growth outpace per-token price decline through 2027 — 47-call traces become 200-call per METR doubling and FinOps stays relevant; or reasoning compresses trajectories and FinOps decays? (12/15 — D:3 / A:5 / B:4)

**Meta-D — Geopolitics.**

- **Top Opportunity.** EU AI Act procurement-readiness for US vendors selling into EU — enforcement begins late 2026; US vendors with EU F500 customers need audit-ready stance on agent classification, transparency, conformity. Bet #1 extension into regulated geo. (11/15 — C:4 / T:3 / Cl:4)
- **Top Challenge.** Export-control volatility reprices vendor selection mid-deal — Nov 2025 Commerce auth for G42/Humain signaled negotiated-not-blanket; one EO or court ruling re-locks the door. (12/15 — S:4 / P:4 / E:4)
- **Top Open Question.** Does Mistral consolidate as Europe's defensible enterprise-agent platform by 2027 — €600M Mar 2026 funded the bet; do EU F500s standardize on Mistral or treat it as data-residency sidecar? (11/15 — D:3 / A:4 / B:4)

### Pattern read

Opportunity intensity clusters at Strata V (Planning, 15/15), VI (Action Surfaces, 14/15), VII (Eval/Obs, 14/15), and II (Runtimes, 14/15) — the operational layer that wraps commoditizing surfaces is where margin lives, exactly as Wardley's "field stratifies" thesis predicts (§2.2). Meta-strata B and C score 13/15: regulation and economics fold cleanly into Bet #1's procurement frame. Sub-strata IV (Memory, 13/15 op / 10/15 challenge) and IX (Vertical agents, 13/15 op / 14/15 question) carry the highest *open-question* asymmetry — Sierra hiring cadence (14/15) and EU Annex III classification (14/15) are the cruxes that move Bets #2 and #1 the hardest.

Challenge intensity concentrates at Meta-C (token-price decline, 14/15) and Stratum V (hyperscaler auto-routing, 13/15) — both reprice Bet #4 on the same 18-month timer. Stratum I challenge (foundation-lab walk-up-stack, 12/15) and Stratum III challenge (MCP silent fork, 12/15) are the structural risks for Bets #2 and #3.

Open Questions decidable in 2026 (Decidability 4+): Sierra hiring cadence (Stratum IX), MCP universal-baseline threshold (III), EU AI Act conformity guidance (VII, VIII), OpenAI adjustment clause (Meta-A), EU Annex III agent classification (Meta-B), Opus 4.5 lead survival (I). Open Questions decidable in 2027 (Decidability 3): memory portability standard (IV), trajectory-compute vs. token-price (Meta-C), Mistral consolidation (Meta-D). Six of the nine top-asymmetry cruxes resolve in the same 12-month window — that window is the planning anchor for Ch 3's bet refresh.

![Plate 2 — Agent OCQ Heatmap](plates/02_agent_ocq_heatmap.svg)

## §2.2 Wardley Map of the Agent Stack

### Anchor needs

Four function-different user needs anchor the top of the agent-layer map. Each anchors a distinct dependency chain; together they cover every credible agent deployment shape in 2026.

- **Complete a multi-step research-and-reporting task autonomously** — the deep-research / GAIA / BrowseComp use case (Anthropic Research, OpenAI Deep Research, Gemini Deep Research, Manus, Genspark).
- **Operate a browser or computer to complete a back-office workflow** — claims, expense, vendor onboarding; the CFO-credible "AI BPO" pitch.
- **Handle a customer query end-to-end with voice plus tools plus escalation** — Sierra / Decagon / Hippocratic / Vapi pattern; the only domain where outcome pricing has landed.
- **Write, test, and merge a production code change** — Claude Code / Cursor / Codex / Devin / Augment; the only category where AI labor is priced like FTE displacement at scale.

### Stack placement

**Stratum I — Foundation models.** Product. Claude Opus 4.5 / GPT-5 / Gemini 2.5 Deep Think are productized and rentable; DeepSeek R2 (May 2026 leaks at mid-60s SWE-Bench) is the rightward open-weight pull. Direction: capability is rented; trajectory-data Process Power inside labs strengthens.

**Stratum II — Agent runtimes and harnesses.** Custom → Product. Claude Agent SDK and OpenAI Agents SDK lead with ~6-month primitive advantage; LangGraph 1.0 is Product but margin compresses to LangSmith. Direction: model-locked SDKs harden, neutral runtimes drift to acquihire or niche.

**Stratum III — Tool use / MCP.** Spec at Product (LF-governed, 11.4k servers Apr 2026); experience fragmenting — Anthropic `tool_use` proprietary, OpenAI Responses-API bypassing MCP for latency. Gateways (Cloudflare, Kong GA Jul 2025, Pomerium) Custom → Product. Direction: spec held; gateway sub-category is where margin locates.

**Stratum IV — Memory and state.** Lab-native memory Custom → Product (Claude Projects GA Apr 2026); standalone (Mem0, Letta, Zep) Genesis → Custom with <50k dev accounts versus 800M lab MAU. Direction: absorbed for consumer/prosumer, niche-standalone for compliance.

**Stratum V — Planning, reasoning, test-time compute.** Reasoning models at Product (buyer-controllable `reasoning_effort`); planner-executor split at Product (gateway config flag); RLVR/GRPO trajectory fine-tune Genesis → Custom. Direction: routing pattern commoditizes; cost curve steep through 2026.

**Stratum VI — Action surfaces.** Sandboxes Product (Vercel Sandbox GA Jan 2026; E2B, Modal); browser automation Product (Browserbase ~$50M ARR Q1 2026); voice substrate Product → Commodity (LiveKit + Cartesia Sonic-2 sub-50ms); computer use Genesis → Custom (OSWorld 50% Q1 2026; ~30% at 50 steps); voice orchestration Custom → Product (compliance gating Q1 2026). Direction: surfaces commoditize; operational layer on top — recording, replay, evals, compliance — holds Switching Costs.

**Stratum VII — Evaluation and observability.** LLM tracing at Product / OTel-stabilized Jan 2026; eval platforms Custom → Product (Braintrust, LangSmith, Galileo); Inspect AI at Custom (cited in EU AI Act conformity drafts Feb 2026); signed reproducible eval reports at Genesis (no vendor turnkey today). Direction: ingest commoditizes, eval logic = lock-in; signed-report layer stays Genesis through 2026.

**Stratum VIII — Runtime safety and guardrails.** Mostly absorbed: Llama Guard 3, NeMo Guardrails 1.0 GA (Apr 2026), Bedrock Guardrails. Lakera at Custom → Product (model-neutral red-team niche). Direction: hyperscaler bundle absorption through 2027; Lakera-shaped survivors hold compliance wedge.

**Stratum IX — Vertical agent products.** CX (Sierra, Decagon) Custom → Product, per-resolution pricing exported; Knowledge (Glean, Hebbia) Custom → Product, ChatGPT Business encroaches; Legal (Harvey) Custom, AmLaw100 lock-in, most defensible; Healthcare (Abridge, Hippocratic) Custom, HIPAA/FDA fence; RevOps (Clay) Custom-struggling, 1–2 winners; Coding (Cursor, Claude Code) Product, lab-bundling threat; Finance (Rogo, Ramp AI) Custom; Creative (ElevenLabs, Runway) Product; Sovereign (Mistral, Sarvam, Manus) Custom. Direction: 1–2-winner segments harden; long tail eroding.

**Stratum X — End-user surfaces.** Chat web/desktop Product; CLI (Claude Code ~$500M ARR-run-rate) Product; IDE inline (Cursor ~$500M, Copilot ~22M seats) Product; browser sidebar (Comet, Claude for Chrome) Custom → Product, enterprise blocked >60%; embedded SaaS (M365 Copilot $5B ARR / ~30M seats) Product; voice (Advanced Voice, Gemini Live) Custom → Product (sub-800ms crossed Q1 2026); wearable/AR Genesis. Direction: stratified — embedded bundles dominate revenue, pure-plays trail an order of magnitude.

**Meta-A — Capability-level safety regimes.** Custom — ASL/PF/FSF voluntary, evaluator capacity binding (METR, UK AISI, US AISI, Singapore AISI, EU AI Office). Inspect AI at Custom but cited in EU drafts. Direction: Anthropic ASL reputationally durable, regulatory durability contested.

**Meta-B — Regulation.** Custom. EU AI Act GPAI rules binding Aug 2025; Article 14 human-oversight draft Apr 2026; first conformity drafts Feb 2026. Direction: rightward pull from EU enforcement late 2026.

**Meta-C — Economics.** Custom-Built. Per-trajectory cost models still bespoke; outcome-based pricing confirmed CX, partial healthcare, failed elsewhere; trajectory-compute growth versus per-token decline is the live tension.

**Meta-D — Geopolitics.** Genesis → Custom. Stargate UAE / Humain KSA / Mistral €11B / Sarvam / Manus are real but pre-procurement-doctrine. Direction: EU AI Act enforcement late 2026 is the binary catalyst.

**Procurement-grade agent controls** sit at Genesis as a cross-cutting layer with no turnkey vendor — signed eval reports, multi-party audit with redaction, EU Act tie-out, action-rollback, adaptive-adversary red-team. This is the unclaimed flag for Bet #1.

### Punctuated equilibria expected 2026–2027

Seven specific transitions in the next eighteen months. Each one reprices everything that depends on it.

- **MCP gateways: Custom → Product (H2 2026).** Kong GA July 2025, Cloudflare auth expansion April 2026, Pomerium identity-aware proxy. Enterprise control plane (auth, audit, rate-limit, secret-injection) hardens. Reprices custom-MCP builds; adjacent-possible: MCP-native iPaaS, policy-firewall products, F500-private registries. Sharpens Bet #3 onto the gateway sub-category.
- **Computer use: Genesis → Custom (mid-to-late 2026).** OSWorld 50% Q1 2026 → ~65% on a frontier system mid-2026 (the OSWorld sub-crux, spec §3.7). Reprices RPA; adjacent-possible: AI-augmented BPO at 1/5 cost for reversible/auditable click sequences. Unattended autonomous computer use stays a 2027–2028 question.
- **Voice telephony substrate: Product → Commodity (mid-to-late 2026).** LiveKit + Cartesia + OpenAI Realtime + Twilio/Telnyx sub-600ms for short calls. Substrate commoditizes; voice-orchestration (Vapi, Retell, Bland) consolidates to 1–2 winners with compliance as the moat. Reprices Genesys / NICE / Five9.
- **Standalone memory: forced binary, resolves H2 2026.** Either Mem0/Letta/Zep harden the compliance wedge (Zep most likely, ~$50M ARR by 2027), or absorbed — lab-native at consumer, runtime primitives at developer. Read: absorbed for consumer/prosumer, niche-standalone for compliance. Memory folds into Bet #5.
- **Procurement-grade agent controls: Genesis → Custom (Q4 2026).** EU AI Act GPAI enforcement starts Aug 2026; first conformity draft (Feb 2026) names Inspect AI explicitly. First Custom solutions emerge from Big-4 + a Lakera-shaped partner. The unclaimed flag for Bet #1.
- **Eval/observability consolidation: Product (Q4 2026 – H1 2027).** OTel stabilization killed ingest lock-in; eval logic remains; ~$300M ARR ceiling. LangSmith stays (LangGraph-bundled); Braintrust likeliest consolidator (~$60M Series B Q1 2026 leak); Langfuse wins EU/self-host; 2–3 of {Galileo, Patronus, HumanLoop, Comet, Helicone, AgentOps} acquired by EOY 2026.
- **Foundation labs walking up-stack (continuous 2026).** ChatGPT Business connectors, Claude for Work, Gemini Enterprise. Reprices Glean, Notion AI, Copilot 365 monopoly. Adjacent-possible: vertical-agent companies with deep workflow integration and outcome SLAs (Sierra, Decagon, Harvey, Hippocratic) are least vulnerable — confirms Bet #2.

Three of the seven anchor to dated events: MCP gateway hardening to Kong GA (Jul 2025) + Cloudflare April 2026 expansion; procurement-grade controls to EU AI Act Aug 2026 GPAI enforcement; eval/obs consolidation to Braintrust Series B Q1 2026 leak.

### Strategic quadrants

**Pioneer (Genesis — build/explore).** Procurement-grade signed eval bundles (no vendor turnkey; Inspect AI closest); computer use for unattended back-office (30% reliability at 50 steps); multi-party agent audit (vendor + customer + auditor on one trace with redaction); contextual-integrity primitives for memory; sovereign agent stacks for EU AI Act–exposed F500 EU-subs; MCP-native iPaaS replacing Zapier.

**Settle (Custom → Product — productize what works).** MCP server constellations for enterprise GTM SaaS (Salesforce, Outreach, Gong, Highspot, Zoominfo, Linear) — Bet #3's buildable target; vertical voice agents (debt collection, healthcare intake, NPS-detractor recovery) — substrate commodity, vertical packaging + compliance the moat; vertical AI workers with deep workflow integration — Sierra/Decagon/Harvey/Hippocratic pattern (Bet #2 = take a GTM role inside one rather than build one); enterprise-acceptance eval/obs ("Drata for AI agents"); AI procurement / deal desk SaaS (Bet #1's downstream product); memory architecture as a service line (folded into Bet #5).

**Consume (Product → Commodity — rent, don't build).** Foundation models via API or AI Gateway. Sandboxes (E2B, Modal, Vercel Sandbox). Headless browsers (Browserbase + Playwright). Voice substrate (LiveKit, Cartesia, Deepgram, Twilio/Telnyx). Agent runtimes (use the SDK of your dominant model provider). MCP transport + first-party servers. AI gateways (Vercel, Cloudflare, OpenRouter). Vector DB / embeddings / rerankers (pgvector or Turbopuffer + Voyage / Cohere). OTel GenAI tracing.

**Utility / Build-around (ubiquitous).** Linux, Postgres, Chromium, WebRTC, Firecracker, Python/TypeScript, PyTorch, public internet, Kubernetes, OTel, Markdown, JSON-RPC.

### Pattern read

The strongest cluster is Custom-Built → Product across the operational layer — gateways, vertical agents, voice orchestration, eval logic, procurement controls. That zone is exactly where Alex's GTM judgment compounds. Two specific errors recur in the field. First, treating standalone memory (Mem0/Letta) as a Product-tier category when it is Genesis → Custom and absorbing fast; the addendum picks "absorbed for consumer, niche-standalone for compliance" — Wardley agrees. Second, treating computer use as Product when OSWorld 50% means it is Genesis bordering Custom; unattended autonomous back-office through F500 procurement remains a mid-2027 question. The map disagrees with the field's "MCP won" framing — spec held, experience fragmenting — and Bet #3 plans for "MCP-compatible baseline," not "MCP-native interop guarantee." See Plate 3 for the full map.

![Plate 3 — Agent Wardley Map](plates/03_agent_wardley_map.svg)

## §2.3 Helmer's 7 Powers

### The 7 powers (one-line each)

Carried from V1 Ch 2 §2.3. Same definitions:

- **Scale Economies.** Declining unit costs as production grows.
- **Network Economies.** Value increases with users or nodes connected.
- **Counter-Positioning.** Incumbents cannot copy without destroying their existing business.
- **Switching Costs.** High cost for the customer to leave.
- **Branding.** Durable affective association that commands a premium.
- **Cornered Resource.** Privileged access to a critical input.
- **Process Power.** Embedded organizational know-how that is hard to replicate.

Discipline: a power must combine *benefit* AND *barrier*. Mindshare is not a power.

### Per-sub-stratum power inventory

**Stratum I — Foundation models (agentic capability).** Process Power held by Anthropic, OpenAI, Google DeepMind — the moat is the RL-from-trajectory-data pipeline (RLVR + GRPO + PRMs + verifier harness), not the architecture. Cornered Resource on the ~200 senior researchers who have shipped >100B-param frontier models with reasoning loops. Branding: Anthropic owns "safety + coding"; OpenAI owns "consumer." Direction: capability lead is rentable (DeepSeek R2 / Qwen3 close the gap at 4–6× lower cost); Process Power on trajectory training strengthens as labs accumulate proprietary RL data from their own products (Claude Code, ChatGPT Agent).

**Stratum II — Agent runtimes and harnesses.** Almost none. Switching Costs shallow (LangGraph → Claude-SDK migration is one quarter). LangChain Brand eroding to fatigue. Vendor SDKs (Anthropic, OpenAI, Google) have pull derived from the model, not the runtime. No Network Economies, no Cornered Resource, no Scale Economies. Direction: eroding. Not a power layer.

**Stratum III — MCP / tool-use protocol.** Network Economies forming at the registry level (11,400 servers April 2026; first-party Stripe/Linear/GitHub/Snowflake servers compounding) — but open protocols are designed to defeat moats. Counter-Positioning for Anthropic: incumbent OpenAI couldn't easily endorse a competitor's protocol; Anthropic shipped first, got it adopted, then donated to Linux Foundation December 2025 — locking in the standard while disclaiming control. The durable power-holders at this layer are MCP-gateway vendors (Cloudflare, Kong, Pomerium) — Switching Costs via auth/audit/secret-injection enterprise control plane. Direction: Anthropic's Counter-Positioning win is permanent and underweighted; gateway Switching Costs strengthen with registry growth.

**Stratum IV — Memory and state.** Thin. Zep has nascent Switching Costs in compliance-sensitive accounts (HIPAA, SOC 2 Type II, EU residency Q3 2026 roadmap). Mem0's "Pinecone-for-memory" framing is the wrong analogy — memory is RAG-with-writes, a feature. Direction: eroding fast. Claude Projects memory GA April 2026, ChatGPT 800M MAU, Gemini personalization March 2026 absorb consumer/prosumer. Only Zep holds a durable niche on compliance Process Power.

**Stratum V — Planning, reasoning, test-time compute.** Inside frontier labs only (Process Power via PRM/RLVR/GRPO pipelines buyers can't inspect). Outside the labs: none. Planner-executor-verifier is a config flag in Vercel AI Gateway / Bedrock / OpenRouter. Direction: lab-internal power strengthens; external-to-labs power non-existent.

**Stratum VI — Action surfaces.** Mixed. Browserbase has emerging Switching Costs via session-recording, replay, anti-bot ops state and Stagehand DX — but their Chromium isn't proprietary. E2B and Modal show Scale Economies flavor at the unit-cost level (Firecracker micro-VM utilization curves), but the floor is open-source. Vapi/Retell/Bland have neither. LiveKit at the WebRTC infra layer is the closest thing to a Cornered Resource (only credible AI-native real-time substrate). Direction: surface commoditizes inside 24 months; operational layer on top — recording, replay, evals, compliance — holds Switching Costs.

**Stratum VII — Evaluation and observability.** Switching Costs real in eval logic (regression sets as Braintrust YAML or Galileo metric definitions take a quarter to port). OTel GenAI conventions stabilized January 2026 killed lock-in on trace ingest. LangSmith has tight LangGraph Switching Costs; Braintrust has eval-as-CI workflow stickiness. Branding for Lakera in runtime-safety vertical (Atlassian, Dropbox, Citi named). Direction: mostly eroding to hyperscaler bundling. Durable niche: signed/auditable eval reports tied to EU AI Act + NIST AI RMF — nobody ships turnkey today. Bet #1's opening.

**Stratum VIII — Runtime safety and guardrails.** Thin. Lakera Branding + early Switching Costs in regulated accounts. No prompt-injection moat — adaptive-adversary numbers fall to 60–80%. Direction: absorbed into hyperscaler bundles within 18 months. Llama Guard 3 + NeMo Guardrails 1.0 GA (April 2026) eat the OSS floor. Not a power layer except Lakera's model-neutral red-team niche.

**Stratum IX — Vertical agent products.** This is the upper-stack power concentration — vertical-specific. Process Power + Switching Costs are real at: Sierra (CX outcome-pricing operational scar tissue, per-resolution SLA enforcement infrastructure built over two years), Harvey (BigLaw RLHF on contract data + privilege/bar liability fence), Abridge (Epic embedding depth + clinician workflow integration), Hippocratic ($9/hr "RN equivalent" + state-licensing buy-in + Cerner/Epic), Glean (organizational data graph that compounds with usage — closest thing to Network Economies in the vertical layer). Cornered Resource is rare here; Harvey's Cravath/A&O design-partner relationships are the closest. Direction: strengthening for the 2–3 winners per vertical; eroding for the long tail. Hyperscaler encroachment ranking: Knowledge > Coding > RevOps > Creative > CX > Healthcare > Legal > Finance.

**Stratum X — End-user surfaces.** Surface-by-surface differentiation. Microsoft Copilot 365: Switching Costs (enterprise seat lock-in, M365 graph integration) + Scale Economies — the largest agentic-revenue position in 2026 ($5B+ ARR, 30M paid seats). Apple Intelligence: Cornered Resource (Neural Engine + iOS distribution) + Switching Costs. Anthropic: Branding + Process Power on the model, but first-party-surface deficit is real (no Apple Intelligence slot; Claude mobile feature-thin; no native voice). WhatsApp (Meta): Cornered Resource — dominant AI surface for global majority once agentic API opened January 2026. Direction: strengthening for surface-and-distribution holders.

**Meta-A — Capability-level safety regimes.** Anthropic holds Branding (uniquely owns "safety" in enterprise mind) + Process Power (Constitutional AI, interpretability program) + Cornered Resource (alignment researchers — ~200 globally; Anthropic retains Leike post-Murati move). The most defensible single-vendor position in the entire stack.

**Meta-B — Regulation.** Counter-Positioning for Mistral and EU-resident challengers under EU AI Act enforcement (late 2026): a US frontier lab cannot match "data never leaves the EU" without re-architecting its training pipeline. Palantir holds Process Power (accreditation craft) + Cornered Resource (cleared personnel + government relationships) at the FedRAMP/IL5-IL6/HIPAA frontier — decades-deep. Strengthening with EU AI Act enforcement and US federal preemption volatility. This is where Bet #1 sits.

**Meta-C — Economics.** Eroding. Token prices compressing 4–10× per cycle; OpenRouter and Bedrock commoditize switching. Hyperscalers retain Scale Economies on inference infra. Pure-play inference (Groq, Together, Fireworks) has Process Power on kernels but not durable Switching Costs.

**Meta-D — Geopolitics.** Counter-Positioning for Mistral (EU sovereignty), Sarvam (India), Manus (China-language-data Cornered Resource — Mandarin trajectory data US labs cannot legally train on). Falcon (UAE) is capital-backed, not power-backed. Strengthening as US export controls and EU residency rules compound.

### The five most durable agent-layer positions

1. **Anthropic's alignment + trajectory-data Process Power.** Constitutional AI + Claude Code RL-from-production-trajectories + the ~200-person alignment talent pool. The capability lead is rentable; Process Power on internal RL pipelines compounds with their own product usage. Endures past 2027 because the data flywheel is self-reinforcing.
2. **Sierra in CX (vertical Process Power + Switching Costs).** Outcome-pricing operational scar tissue, per-resolution SLA infrastructure, two-year head start on the operational moat. Helmer-strict: Process Power, not Brand. Endures because the operational practices took two years to build, are not codifiable in a runbook, and Decagon — the closest competitor — is one cycle behind on the same curve.
3. **Glean's organizational data graph (Network Economies, vertical-bounded).** Value increases with users *inside the same enterprise*; cross-system graph is hard to replicate; ChatGPT Business connectors attack the wedge but cannot replicate org-graph density. Endures 18–24 months past 2027 if Microsoft doesn't ship a credible cross-tenant equivalent.
4. **MCP gateway control plane (Cloudflare, Kong, Pomerium).** Switching Costs via auth/audit/rate-limit/secret-injection enterprise plumbing. Once an F500 has 30+ MCP servers wired through Kong's gateway with SSO and audit, ripping it out is a year of work. Strengthens as the registry grows.
5. **Harvey at AmLaw100 (Process Power + privilege/bar fence).** Cravath/A&O design-partner depth, BigLaw RLHF on contract data, legal-bar liability moat. Smaller TAM than Sierra/Glean but lowest encroachment risk in the entire vertical layer.

Honorable: Microsoft Copilot ($5B ARR + Scale + Switching, but inherits OpenAI dependency); Palantir (Meta-B accreditation craft); Browserbase ops layer (Switching Costs on session-recording + replay); Anthropic Branding on Meta-A.

### The five most over-rated

1. **Cursor at $9.9B as a durable position.** Real ARR ($500M+), but the moat is mindshare + DX, not power. Anthropic owns the model underneath (Claude Code is the encroacher); IDE inline is the form factor most exposed to foundation-lab walk-up. Switching Costs are low — engineers move IDEs in a week. Branding ≠ moat.
2. **LangChain / LangGraph as the "neutral runtime moat."** API churn fatigue is real; vendor SDKs ship faster; the field narrative is ahead of evidence. Switching Costs exist but are shallow. The durable LangChain bet is LangSmith observability, not the runtime.
3. **Memory companies (Mem0, Letta) as standalone categories.** "Pinecone for memory" is the wrong analogy. Lab absorption + RAG-with-writes economics + opaque enterprise compliance story. Letta's pivot to "stateful agent runtime" is the implicit concession.
4. **11x and the "synthetic SDR" category.** $20M flat ARR, churn spike, Sukkar publicly conceding the quality ceiling. RevOps buyers reject vendor outcome attribution. No power. Clay survives by owning data, not by being an agent.
5. **Standalone runtime-safety vendors (excluding Lakera's red-team niche).** Indirect prompt injection isn't solved; hyperscaler bundles cover 80% at zero procurement friction; Protect AI → Palo Alto (Q3 2025, ~$700M) was the consolidation bell. Apex, Calypso, Cranium most likely roll up. Pure-play guardrails ≠ durable power.

### Pattern read

Durable power at the agent layer concentrates in two zones: vertical-specific Process Power (Stratum IX) and the compliance/control-plane stack wrapping commoditizing surfaces (Meta-B, parts of III and VII). The middle — generic runtimes, generic memory, generic guardrails, generic reasoning wrappers — is where margin and durability both compress. The barrens are where the most VC dollars went in 2024–25: framework-as-company, pure-play memory, pure-play guardrails. Alex's claimable career zone hugs the vertical-top (Bet #2) and the compliance/control-plane (Bet #1) clusters. See Plate 4 for the powers × sub-stratum grid.

![Plate 4 — Agent Powers × Sub-Stratum Grid](plates/04_agent_powers_grid.svg)

## §2.4 Ecosystem JTBD

### Why ecosystem-level (note the 7-job framing)

V1 Ch 2 §2.4 ran six jobs at the AI-field level — "the entire AI stack hired to do X." V3 runs seven jobs at the agent-augmented-workflow level: the unit of analysis is not the field but the agent inside a customer workflow. The frames overlap but do not 1:1 remap. V3 Job 6 (procurement) ≅ V1 Job 4 (enterprise procurement), narrowed to agent-specific risks (autonomy scope, tool-boundary, indirect injection, action rollback, sub-agent privilege, Article 14 oversight). The other six V3 jobs are agent-specific and not present in V1: customer-facing conversation as a discrete job (Job 2), multi-step coding change including PR merge (Job 3), operating a SaaS application on behalf of a line manager (Job 4), domain-currency monitoring with action (Job 5), back-office completion without babysitting (Job 1), and onboarding with an agent-augmented training stack (Job 7). The cross-walk is one-to-many because the agent layer fragments what V1 treated as monolithic ecosystem work.

### The 7 jobs

**Job 1 — Complete a discrete back-office task without babysitting.**
An ops or finance leader has a multi-step rules-governed workflow (invoice triage, payroll exception, contract abstraction, refund, KYC) and wants the agent to take it inbox-to-archive, fail safely, and report. Buyer: VP Ops / Controller / Shared-Services. Top-3 underserved outcomes: (1) minimize time to diagnose *why* a partial-failure run stopped — I 9 / S 3 / gap 9; (2) increase % of unattended runs producing a tamper-evident, signed evidence pack auditors accept without re-running — I 8 / S 2 / gap 8; (3) minimize trajectories that complete-as-judged but write the wrong value to a system-of-record — I 10 / S 4 / gap 10 — the silent-failure problem.

**Job 2 — Run a customer-facing conversation to resolution.**
A CX/growth leader needs every contact (chat / voice / WhatsApp / SMS / email) to resolve to a stated outcome or hand off warm with full context. Buyer: VP CX (incumbent); CRO when retention-coupled; Director of Member Services in regulated. Top-3 underserved outcomes: (1) minimize % of escalations where the human re-asks something the agent already asked — I 10 / S 3 / gap 10; (2) increase confidence a WhatsApp/SMS agent is consent-compliant across jurisdictions pre-launch — I 9 / S 2 / gap 9 (WhatsApp Business API opened January 2026; almost no compliance tooling); (3) minimize time for a non-engineer CX lead to ship a policy correction — I 9 / S 3 / gap 9.

**Job 3 — Execute a multi-step coding change including PR review and merge.**
Engineering lead has a spec'd change; wants the agent to branch, code, test, open the PR, satisfy CI, respond to review, and merge — without senior babysitting. Buyer: Eng Director / VP Eng / CTO. Top-3 underserved outcomes: (1) minimize % of agent PRs that pass review/CI but need senior rewrite within 30 days — I 9 / S 4 / gap 9; (2) reduce time to disambiguate flaky CI versus agent regression versus environment — I 8 / S 3 / gap 8; (3) increase % of code-agent runs producing audit-grade authorship/provenance metadata (model pin, prompt, dataset hash) for compliance and IP defense — I 7 / S 2 / gap 7, rising to I 10 in regulated industries post-Bartz / NYT v. OpenAI.

**Job 4 — Operate a SaaS application on the user's behalf.**
A line-of-business user knows the tool (Salesforce, Workday, SAP, NetSuite, ServiceNow, Notion, Linear) but doesn't want to drive it. Buyer: the line manager who owns the workflow (RevOps Director, FP&A lead, Service Desk lead) — *not* IT (IT is compliance veto). Top-3 underserved outcomes: (1) reduce OAuth blast radius — increase % of tasks running with least-privilege, time-boxed, scope-bounded credentials — I 9 / S 2 / gap 9 (MCP 0.3 auth closes this eventually; today unserved — Bet #3 wedge); (2) increase % of cross-tool tasks completing without a human reconnecting the chain — I 8 / S 3 / gap 8; (3) minimize calendar time a non-IT line manager waits to deploy a new agent into a sanctioned tool — I 8 / S 3 / gap 8 (procurement gauntlet hits hardest here since the buyer is not the seat-owner).

**Job 5 — Stay current on a domain and act on what changes.**
Operator (PM, AE, RevOps, compliance, architect, investor) needs a fast-moving domain monitored, summarized, prioritized, and surfaced only for decisions they would make. Buyer: operator themselves ($20–200/mo); employer for team-tier ($500–5K/seat/yr). Top-3 underserved outcomes: (1) minimize time from event to operator-*deciding* (not just notified) — I 9 / S 2 / gap 9, Bet #6's target; (2) increase confidence the filter isn't silently dropping contrarian sources — I 8 / S 3 / gap 8; (3) minimize duplicate processing across email/Slack/RSS/podcast/newsletter/X for the same event — I 7 / S 3 / gap 7.

**Job 6 — Pass agent-specific enterprise procurement and risk review. [PRIORITY]**
An AI-agent vendor enters a F1000 cycle and must satisfy InfoSec, Legal, Privacy, AI Governance, Procurement, and the business sponsor on agent-specific risks — autonomy scope, tool-boundary policy, indirect prompt injection, action rollback, sub-agent privilege, Article 14 oversight, eval reproducibility — to close within the buyer's planning cycle. Inheritance: agent-narrowing of V1 Job 4. Top-3 underserved outcomes: (1) minimize calendar-time from security questionnaire to signed AI Governance sign-off — I 10 / S 2 / gap 10, Bet #1's target; (2) increase % of agent-specific risk questions (indirect injection, tool-boundary, action rollback, sub-agent privilege) the vendor answers in standardized form — I 9 / S 2 / gap 9; (3) reduce bespoke effort for an EU AI Act / NIST AI RMF / ISO 42001 conformity tie-out — I 8 / S 2 / gap 8, rising fast. Falsifiability: OCQ_TRACKER's 500-downloads / 50-inbound test in 60 days is the actual measurement.

**Job 7 — Onboard or ramp a new role using an agent-augmented training stack.**
Manager hires into an AI-native role (AE, FDE, Applied AI engineer, CS, ops analyst); wants the hire to reach productive output in weeks-not-quarters by pairing them with an agent that scaffolds workflow, coaches tool-by-tool, and produces observable trace for ramp assessment. Buyer: hiring manager (primary), L&D / People Ops (channel). Top-3 underserved outcomes: (1) minimize time-to-productive-output for a new hire in an AI-native role — I 9 / S 3 / gap 9; (2) increase manager visibility into ramp velocity without intrusive monitoring — I 7 / S 3 / gap 7; (3) increase % of senior tacit knowledge captured into agent-usable form — I 8 / S 2 / gap 8. Anchor caution: most "AI for onboarding" is repackaged LMS; this job is different — an agent that *does the work alongside* the new hire and tapers.

### Cross-job synthesis

Three underservice patterns repeat across all seven jobs. **Conclude is universally unserved** — signed evidence pack (Job 1), warm handoff (Job 2), provenance metadata (Job 3), change-log (Job 4), decision-routing (Job 5), counterparty evidence (Job 6), taper (Job 7). Vendors compete on Execute; buyers feel pain at Conclude. **Modify by a non-engineer** is the second — replay UIs exist for engineers (LangSmith, Braintrust); cockpit UIs for the line manager / CX lead / FP&A director do not. **Confirm (pre-flight: will this run actually work)** is the third — Process-reward models exist inside frontier labs but aren't exposed to buyers; closing this turns Job 1 from "agent attempts, sometimes succeeds" into "agent commits, reliably succeeds." Job 6 dominates the priority ranking because it composes Alex's three rarest assets (buyer-side procurement scar tissue, AI-builder fluency, current publishing incentive) with almost no qualified competition — and because its Conclude-phase artifact (signed evidence pack) is the deliverable that opens Jobs 1, 3, and 4 buy-cycles in regulated F1000.

## §2.5 Talent & Capital Flow methodology

### What we track at agent-layer resolution

The agent layer narrows the V1 tracking scope without changing its discipline. Specifically:

- **Senior moves into agent-specific companies** — director-level and above, comp packages above $250K base, into the named vertical-agent winners (Sierra, Decagon, Glean, Harvey, Hippocratic, Hebbia, Rogo, Clay, Ramp-AI, Runway) plus the runtime/protocol/eval layer (Anthropic NYC, Cloudflare MCP, Braintrust, Lakera, Mistral US). Capability-cluster moves (two or more researchers, or a senior IC plus team) are signal; single moves are noise.
- **Capital events at agent platforms** — $50M+ rounds (lower threshold than V1's $100M+, because the agent-layer round-size band is tighter), M&A above $50M, infrastructure commitments in the agent runtime/sandbox/voice substrate categories. We log the round, the named investors, the disclosed or rumored valuation, and the post-money equity room.
- **Agent-layer ARR signals** — trailing-12 versus annualized run-rate disputed-range tolerated. The load-bearing variable is Anthropic ARR ($24B versus $30B, resolution Q3 2026); a 20–30% vertical-agent valuation compression follows the lower bound. Sierra, Decagon, Glean, Harvey, Hippocratic ARR triangulated from three sources where possible.
- **NYC-specific cuts** — vertical-agent moves into Alex's exact profile band (12+ years enterprise B2B + AI fluency + NYC) are double-weighted. Q2 2026 is NYC vertical-agent hiring at historic peak; the window is ~6–9 months before Anthropic ARR resolution reprices equity bands.

### Cadence

Bi-weekly cadence for the rolling tables (talent moves, capital events). Monthly synthesis to feed bet re-rating. Trigger-based logging for one-off signals — Sierra Series D, Anthropic ARR resolution, EU AI Act first GPAI fine, OSWorld benchmark crossings, MCP TSC governance events. Quarterly refresh of public-statements decoded and NYC snapshot.

### Signal vs. noise rules specific to agent layer

V1's three signal rules carry over (capability-cluster moves; $100M+ packages; NYC double-weight). Two are agent-specific. **The MBB-to-agent migration is the third feed-stock alongside Stripe/Ramp/Datadog/Snowflake and BigLaw** — BCG / McKinsey / Bain AI-practice partners rotating into Sierra / Hebbia / Harvey GTM (Sivulka public on Hebbia sourcing MBB heavily). V1 missed this pattern because the unit of analysis was AI-field-wide; at agent-layer resolution it surfaces as a distinct path and is less competed in Alex's lane because consultants don't bring SaaS-operator commercial scar tissue. **Departures from over-funded under-performers (11x, Mem, Magic.dev, Adept residual) compound pressure on top-tier equity rooms** — supply rising while top targets tighten, which means the Alex window is Q2–Q3 2026 specifically.

### Pointer

Methodology only here. Full data tables (talent moves, capital events, ARR watchlist, public statements decoded, NYC snapshot) live in Ch 4 §4.3–§4.7.

## Apply

Pick one. Twelve minutes, with a date stamp, so the result is rotatable next month.

- Score one new agent-layer opportunity you heard about this week against the OCQ lens. What does it total /15 across Confidence/Time-to-Monetize/Claimability? Where does it sit on the agent Wardley map — Pioneer, Settle, Consume, or Utility? If it scores above 13/15 on opportunity AND sits in Settle, it earns a Ch 3 bet review.
- Pick one of the seven JTBD jobs and write one underserved outcome you observed this week that the B7 brief did not capture. Phrase it as a desired outcome with direction, unit, object, and context (Bettencourt structure). If the gap is above 6 in your own estimation, log it as a candidate addition to Ch 3's procurement rubric.
- Identify one of Helmer's powers that is eroding in a sub-stratum you operate in. What is the leading indicator — pricing compression, talent migration, a new entrant counter-positioning? If the indicator moved this month, the bet attached to that power needs a re-rate in Ch 3.

Log the result with date and the drill chosen. Rotate next month so all three drills get used quarterly.
