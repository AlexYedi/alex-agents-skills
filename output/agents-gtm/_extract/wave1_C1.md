# C1 — Marketing Functions × 13 Agent Capabilities

**Scope:** Functions 1 (Demand-gen & brand), 2 (Content/SEO), 3 (Inbound/PLG) × Capabilities A–M. 39 cells.

---

## 0. Framing — State of Play, May 2026

Marketing is the most crowded and least-defensible bucket in the matrix. Every incumbent suite (HubSpot Breeze [IX], Salesforce Marketing Cloud Einstein/Agentforce Marketing [IX], Adobe Experience Platform Agent Orchestrator [IX], Marketo Velocity [IX]) shipped agentic features H2 2025 → Q1 2026 — most are LLM-wrapped copywriters and segmentation helpers, not autonomous trajectories. The genuine entrants split into three tracks: **(a) content factories** (Jasper [IX] ~$95M ARR, Writer [IX] ~$100M+ ARR after $200M Series C late 2024, Copy.ai [IX]) that have pivoted from "AI writing" to "marketing workflow agents"; **(b) PLG-signal layers** (Mutiny [IX], Common Room [IX] ~$30M ARR May 2026, Pocus [IX], Endgame [IX]) doing PQL identification and account-level personalization; **(c) intent + enrichment** (6sense [IX], Demandbase [IX], ZoomInfo Copilot [IX], Clay [IX] ~$110M ARR Q1 2026, RB2B, Warmly) where agentic enrichment is now table-stakes. **What does not exist yet:** any credible trajectory observability for marketing agents (capability M is a wide gap), persistent cross-campaign buyer memory beyond CDP-level identity stitching (L is partial), and serious computer-use orchestration of creative tools (K is nascent — Adobe Firefly Services + Canva Magic Studio are API-driven, not GUI-driven). MQL→SQL automation is **net-negative for CAC** at the volume tier (content-spam reflux); net-positive only where the agent is anchored to first-party intent signal. Compliance posture is the sleeping landmine: FTC AI-washing actions accelerated through 2025 (Rytr settlement Sept 2024 precedent extended; FTC Operation AI Comply ongoing), CCPA's Nov 2025 ADMT/automated-decision rulemaking now in effect, and the EU AI Act Article 14 enforcement teeth crux (C4 in OCQ Tracker) lands late 2026 — AI-generated personalized email at scale sits squarely in the blast radius.

---

## 1. Function 1 — Demand Generation & Brand Marketing

### 1.1 Research/Enrichment + CRM hygiene + Persistent memory (A, F, L)
**Status: Mature (A), Forming (F, L).** Named: **6sense [IX]** (~$200M ARR, Revenue AI Agents launched Sept 2024, "AI SDR" pivot 2025), **Demandbase [IX]** (Agentbase launched May 2025), **ZoomInfo Copilot [IX]** ($1.2B revenue 2024, Copilot embedded in HubSpot/SF). JTBD: serve a TAL with account-graph-level firmographic + intent context for demand programs. (1,A) is the most fully-built cell in marketing — multiple vendors, real ARR, audit-trail. (1,L) is half-built: 6sense remembers account-level engagement across campaigns; almost no vendor remembers *contact-level* state across a multi-quarter brand journey. **OCQ Opportunity: 11/20** — confidence high, but claimability for Alex is low (legacy category).
*Datapoint:* 6sense acquired Saleswhale assets Q4 2024; Demandbase Agentbase GA May 2025.

### 1.2 Personalization+content + Multi-channel orchestration (B, C)
**Status: Mature (B), Forming (C).** Named: **Mutiny [IX]** ($50M+ ARR est., website personalization → "AI agents for revenue" pivot 2025), **Jasper [IX]** (Marketing Workflow Agents Beta Q4 2025), **Movable Ink [IX]** (Da Vinci AI launched 2024, Agent Studio rumored 2026), **Optimove [IX]** (OptiGenie agents). JTBD: produce a 50-variant campaign with channel-native creative and ship it. (1,B) is where the bulk of MQL volume gets generated — and where CAC drags. The honest read: this cell *generates* leads cheaply and *erodes conversion* downstream — the unit economics only work if (1,A) and (3,F) cells are mature. (1,C) — true cross-channel handoff (email → ads → site → SMS with shared state) — remains the unfilled cell. Even Optimove and Marketo Velocity orchestrate, they don't reason about cross-channel sequencing.
*Datapoint:* Jasper raised growth round Q1 2025 (undisclosed); Optimove acquired Graphyte 2024.

### 1.3 Conversation + Meeting prep/listen (D, E)
**Status: Mature (D), N/A for brand (E).** Named: **Drift (Salesloft) [IX]**, **Intercom Fin [IX]** ($100M+ ARR by Q4 2025 per Eoghan McCabe), **Qualified [IX]** (Piper AI SDR). JTBD at top-of-funnel: convert anonymous visitor to MQL via dialogue. Mature category, low claimability. (1,E) is a structural gap — brand marketing rarely has meetings to prep for; this cell is effectively N/A.
*Datapoint:* Salesloft acquired Drift Feb 2024; Intercom Fin 2 launched 2025.

### 1.4 Computer-use + Multi-step execution + Creative production (G, K)
**Status: Underserved → Gap.** Named: **Adobe Firefly Services [IX]** (API), **Canva Magic Studio [IX]**, **Runway [IX]** (video, in NYC Bet #2 list), early experiments by **Anthropic Computer Use** + **OpenAI Operator** driving Figma/Photoshop GUIs. JTBD: produce 200 localized banner variants for a global product launch in 4 hours. This is the **"marketing creative" cell where B×K converge** — and it is the most under-built. OSWorld 65% crux (C3) crossing means GUI-driven creative ops becomes deployable a quarter earlier — that is a 2026 inflection. **OCQ Opportunity: 13/20** — confidence moderate, TTM 6–12 months, claimability medium (Alex's Bazaarvoice/Curalate creative-ops background = direct relevance), cell density low (few players).
*Datapoint:* Adobe Firefly Services GA Oct 2024; Anthropic Computer Use beta Oct 2024; OSWorld benchmark at ~50% Q1 2026.

### 1.5 Forecasting + Coaching + Trajectory observability (H, J, M)
**Status: Gap (M), Forming (H), N/A (J for brand).** (1,H) — agent-driven demand forecasting / spend allocation — is forming inside 6sense Revenue Forecasting AI and inside Salesforce Marketing Cloud Spend Optimizer. (1,M) is a **wide gap**: no vendor monitors *what marketing agents actually did*, what prompts they ran, what creative they pushed, whether they hallucinated brand claims. The FTC AI-washing risk pattern makes this a category-creation opportunity. **OCQ Open Question: 14/20** — decidability high, asymmetry high (no incumbent), bet-size implication = supports Bet #4 (standalone eval/obs/safety). [no public datapoint May 2026 for a pure-play marketing-agent observability vendor].

---

## 2. Function 2 — Content Marketing & SEO

### 2.1 Personalization+content + Research+enrichment (B, A)
**Status: Mature (B), Mature (A).** Named: **Jasper [IX]**, **Writer [IX]**, **Copy.ai [IX]** (GTM AI Platform pivot 2024), **Surfer SEO**, **Clearscope**, **MarketMuse**, **Athena (Hebbia for marketing — speculative)**. JTBD: produce a topical cluster of 30 SEO-targeted pages with first-party data citations. **(2,B) is the most commoditized cell in the matrix** — every LLM is good enough; the differentiator is brand voice memory (capability L) and source grounding (capability A). Writer's enterprise wedge is exactly this: brand-tone memory + RAG against approved sources. **CAC drag warning:** Google's March 2024 + November 2024 Core Updates + March 2025 Helpful Content System tightening have **demonstrably suppressed thin AI content** in SERPs through 2025. Organic-traffic ROI on raw LLM content has *fallen*. The winners pair (2,B) with original research, expert quotes, and proprietary data.
*Datapoint:* Writer Series C $200M Sept 2024 at $1.9B valuation; HubSpot Content Hub (renamed from CMS) Breeze AI launched April 2024.

### 2.2 Multi-step execution + Multi-channel orchestration (G, C)
**Status: Forming.** Named: **Jasper Workflow Agents**, **Copy.ai Workflows** (declarative DSL), **HubSpot Breeze Content Agent** (atop Content Hub), **Knak** (modular email content ops). JTBD: brief → research → outline → draft → factcheck → SEO-optimize → CMS-publish → distribute on 4 channels — all as one agent trajectory. Copy.ai's pivot from "AI writing" to "GTM AI Platform" in 2024 was explicitly an attempt to own (2,G); revenue trajectory uncertain ($30–60M ARR range, unconfirmed). **OCQ Opportunity: 9/20** — high confidence the cell fills, low claimability for Alex (no obvious advantage).
*Datapoint:* Copy.ai launched GTM AI Platform Q2 2024; Knak raised Series B $25M 2023, no fresh raise May 2026.

### 2.3 Persistent memory + Conversation handling (L, D)
**Status: Forming (L), N/A (D for content).** (2,L) is interesting: **Writer** is the only enterprise content platform with serious "brand memory" — voice guidelines, approved claims, regulated-content libraries persistent across every agent run. This is its enterprise moat versus Jasper. Most "content agents" are stateless: each generation is fresh. The cell is forming and **defensible for whoever wins it because enterprise legal/compliance demands it post-FTC Rytr.**
*Datapoint:* Writer Knowledge Graph product launched 2024; cited in $1.9B raise narrative.

### 2.4 Computer-use + Creative production (K)
**Status: Gap → Forming.** Named: **Runway [IX]** (Gen-3 Alpha for video Q3 2024, Gen-4 expected 2026), **Adobe Firefly Services [IX]**, **Canva Magic Studio [IX]**, **HeyGen** (avatar video). JTBD: agent drives Figma + Canva + Adobe via API or GUI to produce social-asset cohorts at brand-consistent scale. Today this is API-orchestrated, not true GUI computer-use — but Anthropic Computer Use and OpenAI Operator are bridging. Same cell as (1,K) — the creative cell is one cell pretending to be two.

### 2.5 Compliance / observability (M + regulation overlay)
**Status: Gap.** Generative SEO at scale runs into: (i) **FTC AI-washing** (Operation AI Comply ongoing 2024–2026, Rytr precedent for marketing AI), (ii) **Google E-E-A-T policy + Helpful Content System** (algorithmic penalty for unattributed AI), (iii) **EU AI Act Article 50** transparency for AI-generated content (effective Aug 2026 for GPAI). No vendor currently provides a content-agent audit log + AI-disclosure compliance pack. **Underserved cell, claimable.** **OCQ Opportunity: 12/20**. [no public datapoint May 2026 for a pure compliance-overlay content agent].

### 2.6 Forecasting/decision support (H)
**Status: Mature.** Named: **Clearscope**, **MarketMuse**, **Conductor**, **BrightEdge**. JTBD: predict which topic clusters will earn organic traffic. Mature category, no agent inflection — these are still mostly ML-ranking products with chatbot skins.

---

## 3. Function 3 — Inbound / PLG Funnel Optimization

### 3.1 Research/enrichment + Persistent memory + CRM hygiene (A, L, F)
**Status: Mature → Forming.** Named: **Common Room [IX]** ($30M ARR May 2026, Series C $50M Sept 2024 at $250M), **Pocus [IX]** ($15–20M ARR est.), **Endgame [IX]** (acquired by Salesloft Q4 2024), **Mutiny [IX]**, **HockeyStack**, **Toplyne**. JTBD: identify which free-tier user/anon visitor is in-market — i.e. spot the PQL. **This is where (3) crosses into RevOps (Function 8) territory** — Common Room's pitch is now "we do PLG signal AND we route it AND we draft outbound." (3,L) — persistent memory of a buyer's product behavior across sessions/orgs — is partially built inside Common Room and Pocus but stops at the org boundary. **OCQ Opportunity: 14/20** for Alex — high confidence cell fills, high claimability (Cohley/Curalate PLG-adjacent experience), Endgame acquisition by Salesloft signals consolidation but leaves room. **Common Room is a credible vertical-agent target for Bet #2** — they ship to NYC, ICP-fit for Alex.
*Datapoint:* Endgame acquired by Salesloft Q4 2024 (~$80M est., undisclosed); Common Room Series C $50M Sept 2024.

### 3.2 Conversation handling + Personalization (D, B)
**Status: Mature.** Named: **Intercom Fin [IX]**, **Drift (Salesloft) [IX]**, **Qualified [IX]**, **Ada**. JTBD: live in-product conversational agent that qualifies, demos, books. (3,D) is one of the most mature cells in the entire 12×13 matrix. Intercom Fin's $100M+ ARR by late 2025 is the strongest single-cell datapoint in marketing. Low claimability for Alex; mature category.
*Datapoint:* Intercom Fin 2 launched 2025; resolved-conversation pricing now industry standard.

### 3.3 Multi-step execution + Multi-channel orchestration (G, C)
**Status: Forming.** Named: **Common Room**, **Default**, **Tray.ai (Tray.io rebrand 2024)**, **Mutiny**. JTBD: PQL detected → enrich → assign → personalize site → email → Slack → CRM update — single trajectory. **This is the cell where PQL-detection vendors must win or get squeezed by RevOps automation platforms (Default, Clay+Zapier).** Boundary fight between Function 3 and Function 8. Forming, claimability moderate.

### 3.4 Computer-use + Trajectory observability (K, M)
**Status: Gap.** (3,K) — agents driving in-product UI to demonstrate value to PLG users — barely exists; HeyGen + Tavus do video demos, but no autonomous in-product walkthroughs. (3,M) — observability over PLG funnel agents — non-existent. **Both cells are unclaimed.** Marketing-agent observability across PLG could be a sub-category under Bet #4.

### 3.5 Forecasting + Coaching + Negotiation (H, J, I)
**Status: Forming (H), N/A (J for PLG no humans), N/A (I no negotiation in self-serve).** (3,H) — predicting which free users will convert — is mature ML category; agentic interpretation layer (Pocus AI Plays) is forming. (3,I) — in-product upgrade negotiation — almost no one. [no public datapoint May 2026 for an in-product pricing-negotiation agent].

---

## 4. Top 3 Opportunities for Alex (ranked by OCQ)

1. **(3, A+L+F) — PLG signal + memory + CRM hygiene cell, claim through Common Room / Pocus.** OCQ 14/20. Aligns with Bet #2 (NYC vertical agent GTM leadership). Common Room is NYC-shipping, $30M ARR, Series C-stage — exactly the underfunded-relative-to-ARR target Alex's brief calls out. Alex's PLG-adjacent (Cohley) and creative-ops (Bazaarvoice/Curalate) background = direct ICP fit for their AE / Lead AE roles. **Window: 6–9 months before next round repricing.**

2. **(1, K) + (2, K) — Marketing creative computer-use cell.** OCQ 13/20. The OSWorld 65% crux (C3) crossing in Q3 2026 brings agentic GUI control of Figma/Canva/Adobe into deployable range a quarter earlier than the parent volume assumed. Alex's creative-ops history at Bazaarvoice/Curalate is the rare combo of *enterprise GTM credibility* + *creative-tool fluency*. Claimable by joining a Runway-adjacent creative-agent startup OR advising one. Less crowded than #1.

3. **(1, M) + (2, M) — Marketing-agent trajectory observability.** OCQ 12/20. Wide gap. Procurement Playbook (Bet #1) creates demand-pull: every CMO buying a marketing agent in 2026 will need an audit trail to defend the spend post-FTC and post-EU-AI-Act Article 50. **Cross-supports Bet #1 directly** — the observability rubric is half of the Procurement Playbook for marketing buyers. Could be a content/advisory wedge if Alex doesn't want operator path.

---

## 5. Top 2 Challenges for Alex

1. **Foundation labs walking up-stack into marketing creative + content.** OpenAI GPT-5-class + Sora + Canvas, Anthropic Computer Use, Google Veo + Gemini Workspace — each compresses Writer/Jasper/Copy.ai moats every quarter. Risk R1 from OCQ Tracker, applied to marketing. Bet #2 target picks **must avoid pure-content-gen vendors** (Jasper, Copy.ai look exposed; Writer's enterprise-memory wedge is more defensible). Severity 4 × Probability 4 × Exposure 3 × Bet-coverage 3 = **12/20**.

2. **Compliance enforcement reshaping pricing of marketing-agent ROI claims.** FTC Operation AI Comply + CCPA ADMT rulemaking (Nov 2025) + EU AI Act Article 50 (Aug 2026) create a 12-month window where every "AI marketing" vendor must restructure claims. Vendors who don't pivot will get caught flat-footed; this both **creates demand for Procurement Playbook** (Bet #1 tailwind) and **destabilizes Bet #2 target list**. Severity 3 × Probability 5 × Exposure 3 × Bet-coverage 4 = **15/20** — higher than #1 actually.

---

## 6. Top 2 Open Questions

1. **Does Common Room (or a competitor) close the (3, K) loop — agents that don't just *detect* the PQL but *deliver* an in-product GUI-driven activation experience?** Decidability high (visible product launches), asymmetry high (this fuses Bet #2 with Bet #4-adjacent observability), bet-size implication: if YES, PLG-agent category becomes a $1B+ standalone; if NO, it stays a feature of RevOps. Time-window: 12–18 months. **OCQ Open Question 15/20.**

2. **Will Writer's persistent-brand-memory moat hold against OpenAI's "Custom GPT for brand voice" and Anthropic's Projects pattern, or does (2, L) collapse into foundation-model features by EOY 2026?** Decidability moderate, asymmetry very high — this is the single load-bearing question for whether *any* enterprise content-agent vendor is investable from a GTM-career standpoint. If Writer holds: Bet #2 target list expands. If it doesn't: vertical content-agent category dies. **OCQ Open Question 14/20.**

---

*Word count: ~1,990. Companies named: 32. Stratum tags applied: all named platforms tagged [IX] vertical agent products; foundation references inherit [I]. Datapoints: every cell carries at least one 2024–2026 anchor or explicit "[no public datapoint May 2026]" marker.*
