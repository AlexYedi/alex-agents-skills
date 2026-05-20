# B6 — Helmer's 7 Powers Applied to the Agent Stack

**Date:** 2026-05-12 · **Author:** Alex Yedi · **Voice:** OCQ_TRACKER register · **Frame:** Helmer's 7 Powers (Scale, Network, Counter-Positioning, Switching Costs, Branding, Cornered Resource, Process Power) — discipline: a power must combine *benefit* AND *barrier*; mindshare is not a power. **Word target:** ≤2,400.

## Opener

Most of the agent stack does not contain durable power. Read strictly, 7 Powers is brutal here: capability gaps close in months; the runtime is the thinnest gross-margin layer; MCP is by design a non-moat. The *real* power positions are narrow — concentrated in (a) frontier labs holding Process Power on RL-from-trajectory-data and Cornered Resource on alignment talent, (b) one or two vertical agent companies with outcome-pricing operational scar tissue, (c) the workflow-and-compliance layer wrapping commoditizing surfaces, (d) hyperscaler distribution. Almost everywhere else, "winning" is hype, mindshare, or capital, not power. The career-bet corollary: durable positions inside the agent stack are *fewer than the funding cycle suggests*, which sharpens targeting.

---

## Per-Stratum Analysis

### S-I · Foundation models (agentic capability)
**Powers.** Process Power (Anthropic, OpenAI, Google DeepMind): the moat is the *RL-from-trajectory-data pipeline* (RLVR + GRPO + PRMs + verifier harness), not the architecture. Claude SWE-Bench 82.8% and GPT-5 codegen leads are matched on benchmarks but not in production reliability past 32k tool traces. **Cornered Resource:** the ~200 senior researchers who have shipped >100B-param frontier models with reasoning loops. **Branding:** Anthropic owns "safety + coding"; OpenAI owns "consumer." Narrow.
**Direction.** Capability lead is rentable — DeepSeek R2 / Qwen3 close the gap at 4–6× lower cost. Process Power on trajectory training **strengthens** as labs accumulate proprietary RL data from their own products (Claude Code, ChatGPT Agent). The honest read: capability is rented; trajectory-data Process Power is owned.

### S-II · Agent runtimes & harnesses
**Powers.** Almost none. Switching Costs shallow (LangGraph→Claude-SDK migration is one quarter). LangChain Brand eroding to fatigue. Vendor SDKs (Anthropic, OpenAI, Google) have pull derived from the model, not the runtime. No Network Economies, no Cornered Resource, no Scale Economies.
**Direction.** Eroding. Commoditizes toward thin vendor SDK or neutral orchestrator. **Not a power layer. Don't build a company here.**

### S-III · MCP / tool-use protocol
**Powers present.** **Network Economies forming** at the registry level (11,400 servers Apr 2026; first-party Stripe/Linear/GitHub/Snowflake servers compounding). But — and this is the Helmer-strict point — *open protocols are designed to defeat moats*. MCP's value comes from non-exclusion. **Counter-Positioning** for Anthropic (incumbent OpenAI couldn't easily endorse a competitor's protocol; Anthropic shipped first, got it adopted, then donated to Linux Foundation Dec 2025 — locking in the standard while disclaiming control).
**Direction.** Network Economies on the *registry* strengthen; Network Economies on any specific *implementation* are zero. **The durable power-holders at this layer are MCP-gateway vendors (Cloudflare, Kong, Pomerium)** — Switching Costs via auth/audit/secret-injection enterprise control plane. **Anthropic's Counter-Positioning win is permanent and underweighted.** No US lab can re-claim spec authority.

### S-IV · Memory & state
**Powers.** Thin. Zep has nascent Switching Costs in compliance-sensitive accounts (HIPAA, SOC 2 Type II, EU residency). Mem0's "Pinecone-for-memory" framing is the wrong analogy — memory is RAG-with-writes, a feature.
**Direction.** Eroding fast. Claude Projects memory GA Apr 2026, ChatGPT 800M MAU, Gemini personalization Mar 2026 absorb consumer/prosumer. Only Zep holds a durable niche on compliance Process Power in healthcare/regulated. **Not a $1B category. Absorbed.**

### S-V · Planning & reasoning
**Powers.** Inside frontier labs only (Process Power via PRM/RLVR/GRPO pipelines buyers can't inspect). Outside the labs: none. Planner-executor-verifier is a config flag in Vercel AI Gateway / Bedrock / OpenRouter.
**Direction.** Lab-internal power strengthening; external-to-labs power non-existent. **No standalone "reasoning company" has 7-Powers durability.**

### S-VI · Action surfaces (sandbox / browser / computer-use / voice)
**Powers present.** Mixed. Browserbase has emerging **Switching Costs** via session-recording, replay, anti-bot ops state and Stagehand DX — but their Chromium isn't proprietary. E2B and Modal show **Scale Economies** flavor at the unit-cost level (Firecracker micro-VM utilization curves), but the floor is open-source. Vapi/Retell/Bland have neither. **LiveKit** at the WebRTC infra layer is the closest thing to a Cornered Resource (only credible AI-native real-time substrate).
**Direction.** Surface commoditizes inside 24 months (sandbox = S3-like; browser = managed Chromium + CDP; voice = LiveKit + Realtime API + Cartesia). **Operational layer on top — recording, replay, evals, compliance — holds Switching Costs.** That's where power locates, not in the surface. The Anthropic/OpenAI/Google computer-use products are demoware-grade and won't generate power until OSWorld crosses ~70%, a 2027+ question.

### S-VII · Eval / observability / runtime safety
**Powers present.** **Switching Costs** are real in eval logic (regression sets as Braintrust YAML or Galileo metric definitions take a quarter to port). OpenTelemetry GenAI conventions stabilized Jan 2026 killed lock-in on trace ingest. LangSmith has tight LangGraph **Switching Costs**; Braintrust has eval-as-CI workflow stickiness. **Branding** for Lakera in the runtime-safety vertical (Atlassian, Dropbox, Citi named).
**Direction.** Mostly eroding to hyperscaler bundling (AWS Bedrock Guardrails, Azure Purview AI Hub, Vertex Model Armor). Protect AI → Palo Alto (Q3 2025, ~$700M) was the bell. Lakera survives as cross-cloud / model-neutral. Braintrust is the consolidator candidate. **The durable niche: signed/auditable eval reports tied to EU AI Act + NIST AI RMF — and nobody ships this turnkey today.** That is Bet #1's opening.

### S-VIII · Runtime safety / guardrails
**Powers.** Thin. Lakera Branding + early Switching Costs in regulated accounts. No prompt-injection moat — adaptive-adversary numbers fall to 60–80%; vendors admit it.
**Direction.** Absorbed into hyperscaler bundles within 18 months. Llama Guard 3 + NeMo Guardrails 1.0 GA (Apr 2026) eat the OSS floor. **Not a power layer except Lakera's model-neutral red-team niche.**

### S-IX · Vertical agent products
**Powers present.** This is the upper-stack power concentration in 7 Powers analysis — and it is *vertical-specific*. **Process Power + Switching Costs** are real at: Sierra (CX outcome-pricing operational scar tissue + per-resolution SLA enforcement infra that took 2 years to build), Harvey (BigLaw RLHF on contract data + privilege/bar liability fence), Abridge (Epic embedding depth + clinician workflow integration), Hippocratic ($9/hr "RN equivalent" + state-licensing buy-in + Cerner/Epic), Glean (org-wide data graph that compounds with usage — closest thing to **Network Economies** in the vertical layer). **Cornered Resource** is rare here; Harvey's Cravath/A&O design-partner relationships are the closest. **Branding** matters less than usually claimed — F1000 buying is RFP-driven, not brand-driven. Sierra benefits from Bret Taylor's CEO brand on outbound, but the renewal is operational.
**Direction.** **Strengthening for the 2–3 winners per vertical; eroding for the long tail.** Multi-winner: Coding (Cursor/Claude Code/Augment), CX (Sierra/Decagon), Healthcare (Abridge/Hippocratic/Ambience), Finance (Rogo/Hebbia/Ramp-AI). Winner-take-most: Knowledge (Glean), Legal AmLaw100 (Harvey), RevOps (Clay). **The most durable upper-stack positions are vertical-specific Process Power, not category-wide.** Hyperscaler encroachment ranking: Knowledge > Coding > RevOps > Creative > CX > Healthcare > Legal > Finance.

### S-X · End-user surfaces
**Powers present.** Surface-by-surface differentiation. **Microsoft Copilot 365**: Switching Costs (enterprise seat lock-in, M365 graph integration) + Scale Economies (existing channel) — the largest agentic-revenue position in 2026 ($5B+ ARR, 30M paid seats). **Apple Intelligence**: Cornered Resource (Neural Engine + iOS distribution) + Switching Costs. **Anthropic**: Branding + Process Power on the model, but **first-party-surface deficit is real** (no Apple Intelligence slot; Claude mobile feature-thin vs. ChatGPT mobile; no native voice product; Claude for Chrome paying-tier only). **WhatsApp** (Meta): Cornered Resource — the dominant AI surface for the global majority once the agentic API opened Jan 2026.
**Direction.** Strengthening for the surface-and-distribution holders (Microsoft, Apple, Google, Meta-on-WhatsApp). **Anthropic's enterprise power is real but routes through API/IDE/CLI, not consumer surfaces** — a structural shape, not a temporary gap.

---

## Meta-Strata

### Meta-A · Capability-level safety / model alignment
**Powers.** Anthropic holds **Branding** (uniquely owns "safety" in enterprise mind) + **Process Power** (Constitutional AI, interpretability program) + **Cornered Resource** (alignment researchers — ~200 globally; Anthropic retains Leike post-Murati move). Strengthening with EU AI Act conformity-assessment drafts (Feb 2026) citing Inspect AI explicitly. **The most defensible single-vendor position in the entire stack.**

### Meta-B · Regulation / compliance
**Powers.** **Counter-Positioning** for Mistral and EU-resident challengers under EU AI Act enforcement (late 2026): a US frontier lab cannot match "data never leaves the EU" without re-architecting its training pipeline. Palantir holds **Process Power** (accreditation craft) + **Cornered Resource** (cleared personnel + government relationships) at the FedRAMP/IL5-IL6/HIPAA frontier — decades-deep. Strengthening with EU AI Act enforcement and US federal preemption volatility. **This is where Bet #1 sits.**

### Meta-C · Economics / token & inference
**Powers.** Eroding. Token prices compressing 4–10× per cycle; OpenRouter and Bedrock commoditize switching. **Hyperscalers** retain Scale Economies on inference infra (Microsoft via Azure-OpenAI; Google via Vertex; AWS via Bedrock). Pure-play inference (Groq, Together, Fireworks) has Process Power on kernels but not durable Switching Costs. **Anthropic's $200B valuation depends on capability-lead-pricing surviving the next two cycles.** It might not.

### Meta-D · Geopolitics / sovereignty
**Powers.** **Counter-Positioning** for Mistral (EU sovereignty), Sarvam (India), Manus (China-language-data Cornered Resource — Mandarin trajectory data US labs cannot legally train on). Falcon (UAE) is capital-backed, not power-backed. **Manus's cornered-resource on Chinese-language agent-trajectory data is real and US-discourse-underweighted.** Strengthening as US export controls and EU residency rules compound.

---

## The 5 Most Durable Agent-Layer Power Positions, May 2026

1. **NVIDIA at the substrate layer** (already covered in Part VIII) — Cornered Resource (CoWoS, HBM allocation) + Process Power (CUDA) + Scale Economies. Three powers stacked. Agent-stack-relevant via inference economics. Durable through 2030 on training; eroding faster at inference.
2. **Anthropic's alignment + trajectory-data Process Power** — Constitutional AI + Claude Code RL-from-production-trajectories + the ~200-person alignment talent pool. The *capability* lead is rentable; the *Process Power* on internal RL pipelines compounds with their own product usage. Endures past 2027 because the data flywheel is self-reinforcing.
3. **Sierra in CX (vertical Process Power + Switching Costs)** — outcome-pricing operational scar tissue, per-resolution SLA infrastructure, two-year head start on the operational moat. Helmer-strict: this is Process Power, not Brand. Endures because the operational practices took two years to build, are not codifiable in a runbook, and Decagon (the closest competitor) is one cycle behind on the same curve.
4. **Glean's organizational data graph (Network Economies, vertical-bounded)** — value increases with users *inside the same enterprise*; cross-system graph is hard to replicate; ChatGPT Business connectors attack the wedge but cannot replicate the org-graph density. Endures 18–24 months past 2027 if Microsoft doesn't ship a credible cross-tenant equivalent.
5. **MCP gateway control plane (Cloudflare, Kong, Pomerium)** — Switching Costs via auth/audit/rate-limit/secret-injection enterprise plumbing. Once an F500 has 30+ MCP servers wired through Kong's gateway with SSO and audit, ripping it out is a year of work. Strengthens as the registry grows. This is the *durable* MCP power — not "build at the MCP layer" but "own the enterprise control plane around it."

Honorable: Harvey at AmLaw100 (Process Power + privilege/bar fence; smaller TAM); Microsoft Copilot (Scale + Switching but inherits OpenAI dependency); Palantir; Browserbase's ops layer.

---

## The 5 Most Over-Rated Power Positions

1. **Cursor at $9.9B as a durable position.** Real ARR ($500M+), but the moat is mindshare + DX, not power. Anthropic owns the model underneath (Claude Code is the encroacher); IDE inline is the form factor most exposed to foundation-lab walk-up. Switching Costs are low — engineers move IDEs in a week. **Branding ≠ moat.**
2. **LangChain / LangGraph as the "neutral runtime moat."** API churn fatigue is real; vendor SDKs ship faster; the field narrative is ahead of evidence. Switching Costs exist but are shallow. The durable LangChain bet is LangSmith observability, not the runtime.
3. **Memory companies (Mem0, Letta) as standalone categories.** "Pinecone for memory" is the wrong analogy. Lab absorption + RAG-with-writes economics + opaque enterprise compliance story. Letta's pivot to "stateful agent runtime" is the implicit concession.
4. **11x and the "synthetic SDR" category.** $20M flat ARR, churn spike, Sukkar publicly conceding the quality ceiling. RevOps buyers reject vendor outcome attribution. **No power.** Clay survives by owning data, not by being an agent.
5. **Standalone runtime-safety vendors (excluding Lakera's red-team niche).** Indirect prompt injection isn't solved; hyperscaler bundles cover 80% at zero procurement friction; Protect AI → Palo Alto was the consolidation bell. Apex, Calypso, Cranium most likely roll up. Pure-play guardrails ≠ durable power.

---

## Implications for Alex (Bet #2 + Bet #3 Calibration)

**Bet #2 — Vertical Agent GTM Leadership.** The 7-Powers screen sharpens the target list. The most durable upper-stack positions are **Sierra, Harvey, Glean, Abridge, Hippocratic, Rogo** — each has named Process Power or Switching Costs or vertical-bounded Network Economies. **Sierra** has the strongest power-stack (Process Power on outcome-pricing operations + emerging vertical Switching Costs) AND the most-aligned NYC anchor. **Glean** is the closest thing to Network Economies in the upper stack. **Harvey** has the lowest-encroachment-risk vertical (privilege/bar liability fence). The over-rated list **eliminates 11x, Cresta, Lavender, and any RevOps target other than Clay** from serious consideration — they don't pass the power screen, even where the ARR is real. The Bet #2 target list (Sierra, Glean, Hippocratic, Harvey, Hebbia, Rogo, Clay, Ramp-AI, Decagon, Runway) holds. Sierra and Harvey are the highest-power targets; Glean is the highest-Network-Economies bet.

**Bet #3 — MCP-Native Enterprise Integration Practice.** The 7-Powers verdict cuts both ways. *Building MCP servers* per se is **not a power position** — by design (open protocol, non-exclusion). The durable power at the MCP layer is the **gateway/control-plane** (Cloudflare, Kong, Pomerium) and **first-party servers from SaaS incumbents** (Snowflake, Databricks, ServiceNow shipping their own). Alex's claimable position is the *advisory/practice* layer: helping F1000 architect MCP procurement, gateway selection, server quality grading, and audit posture. This is **Process Power flavor** (operational scar tissue from doing it 10+ times) + **Branding** (canonical voice via Bet #1's playbook), not a software moat. **Bet #3 should be framed as advisory/practice, not as productized MCP servers.** Productized servers are commoditizing the moment Salesforce and HubSpot ship first-party.

**Cross-bet implication.** The most durable position Alex can *claim* in the agent stack is the **compliance/procurement Process Power** at Meta-B — Counter-Positioning on EU AI Act enforcement + signed-eval-report gap + tool-boundary policy gap + action-rollback procurement frame. Bet #1 is the highest-power-density career bet in the portfolio. Bet #2 is the highest-equity bet but power-rents Anthropic/Sierra/Harvey. Bet #3 is advisory power, not platform power. **Sequence: Bet #1 (claim the durable position) → Bet #2 (collect equity at a power-holder) → Bet #3 (compound as practice).** That sequencing is what the 7-Powers screen produces that no other framework does.

---

*End B6. Word count ~2,380.*
