# HANDOVER B · AI Agents × the Go-to-Market Organization — Deep-Dive Spin-Up

> **Read this in full before doing anything.** This is the long-form executive summary of two prior bodies of work AND a complete operating brief for a third session focused on the intersection of agentic systems and the GTM organization. This is the most actionable layer of the entire analysis chain — the one where Alex's twelve years of enterprise B2B fluency stop being context and start being the leverage.

**Prepared for:** Alex Yedi · Lead Enterprise Account Director / AI Builder · NYC
**Prepared by:** the session that built the SUBSTRATE atlas and Decisions Playbook
**Date prepared:** 2026-05-12
**Working directory for this new session:** `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/agents-gtm/` (create it)
**Inheriting from (read-only):**
- `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-stack/` — the original full-stack analysis (7 artifacts)
- `/Users/sameoldexpressions/Documents/GitHub/alex-agents-skills/output/ai-agents/` — the agent-specific deep-dive (Session A's 7 artifacts), if Session A has been completed before this one runs

If Session A has not yet been run when this session starts, this session can still execute — it will reference the agent layer more abstractly using the prior `AI_STACK_*` artifacts as the agent-layer source. Both modes are supported; the agent briefs below note where they reach for Session A outputs vs the original full-stack ones.

---

## 1. The long-form executive summary

### What this is, in plain prose

Two prior bodies of work sit upstream of this session.

The first — call it Foundation — produced a full-stack analysis of the AI ecosystem from the power grid to the end user. Three volumes of work: eleven plates plus a master synthesis plate; a foundation report and a decisions playbook totalling roughly twenty-seven thousand words; and a living tracker that the field updates monthly. Five analytical frameworks were applied in sequence over eighteen strata, producing seven cross-cutting bets, five structural risks, and five unresolved cruxes. The big conclusion was that for someone with Alex's exact profile — twelve years of enterprise B2B fluency, growing AI-builder practice, NYC, active job search for AI-native GTM roles — the highest-leverage position to claim is at the intersection of enterprise AI procurement, vertical agent GTM, and operator translation.

The second — call it Agent Zoom — drills the agent layer of the original stack at higher resolution. Where the original analysis treated agents as one band (Stratum XIII), the Agent Zoom treats it as a stack of its own: ten sub-strata from foundation models with agentic capability through end-user surfaces, with the same five frameworks applied. The Agent Zoom's session brief, `HANDOVER_A_AGENTS.md`, is in the same folder as this document and will produce a parallel set of seven artifacts in `output/ai-agents/`.

This third session — call it GTM Intersection — takes the agent stack and crosses it with the structure of the enterprise GTM organization. The unit of analysis is a matrix: agent capabilities along one axis, GTM functions along the other. Each cell answers four questions. What agents exist for this function today? How mature, durable, and adopted are they? Where is the underserved JTBD inside this cell? And where is the buyer (the GTM operator, the RevOps lead, the CRO) actually willing to pay?

The strategic premise of this session: every prior session has produced analysis. This one is meant to produce a *playbook*. Specifically, the operating playbook for Alex to (a) take a Director or Field-CTO seat at a vertical agent company selling INTO GTM teams, and/or (b) productize the Enterprise AI Procurement Playbook (Bet #1) starting with the agent-vendor procurement category — which is the largest single category of AI procurement spend in 2026.

A reader skeptical of this layering might ask: why not just go straight to the agents-times-GTM question? Why three sessions? The answer is that the prior two sessions establish the field-level constraints (what the entire AI stack is doing) and the agent-layer dynamics (what the agent stack inside it is doing). Without those, the GTM-intersection analysis would produce surface-level recommendations: "Sierra is hiring, go talk to them." With those, the same analysis produces structural recommendations: "Sierra's durable power is process power plus switching costs, which are strengthening; Stripe-to-Sierra is the dominant talent migration; the unserved JTBD inside CX is the buying-committee mapping piece that no one is selling; and the procurement gauntlet is the layer where Alex's tacit muscle compounds. Go." The difference is the difference between job-search advice and a career thesis.

### Why this intersection, why now

Three forces converge to make the agent × GTM intersection the highest-leverage zoom level of all three sessions.

**First**, GTM is the function that 2024–2026 enterprise AI spend disproportionately targets. Of the ~$30 billion in enterprise generative-AI spend in 2025, conservative estimates put GTM-adjacent workloads at 35–45%: SDR / outbound sequencing, AE / sales enablement, customer success / churn-prevention, marketing content generation, RevOps data hygiene, deal desk and procurement, forecasting. The companies validating fastest in the agent-app layer are predominantly GTM-adjacent. Sierra and Decagon sit in CX. Glean spans enterprise search but is bought by RevOps and CS leaders. Clay sits in RevOps. 11x, AiSDR, Artisan, Regie, Nooks all sit in outbound. Cresta sits in conversational coaching for support and sales. Harvey sits in legal, which is procurement-adjacent. The agent-economy revenue is GTM-economy revenue at the buyer.

**Second**, GTM organizations are uniquely well-positioned to absorb agentic capability because their work decomposes into the multi-step, tool-using, observe-and-adapt patterns agents are good at. An SDR's day is fifty discrete tasks: research a list, find emails, validate, sequence, follow up, requalify, log to CRM, schedule, prep meeting, write recap, update opportunity. An AE's day is similar but with relational scaffolding underneath. A CSM's day is the same with longer feedback loops. Each task is agent-shaped: bounded, tool-using, observable, with a clear success criterion. The capability fit is unusually good — better than for marketing creative, better than for product strategy, better than for engineering. The expected adoption curve in GTM is steeper than in most enterprise functions.

**Third**, GTM is the function Alex has personally executed at three companies for twelve years. Meltwater, Bazaarvoice / Curalate, Cohley — all enterprise B2B SaaS, all with a procurement gauntlet on the buyer side, all with the same kinds of stakeholder maps and deal cycles and pricing fights. The tacit knowledge of how a Fortune 500 actually buys is the rarest input to the prior session's recommendations. Most analysts can describe the stack; very few have personally negotiated through it. That asymmetric knowledge is the operating advantage in agent × GTM positioning specifically.

The convergence is: the layer is hot, the capability fit is unusually good, and Alex's personal background is uniquely well-matched. Three conditions you rarely see line up.

### What the matrix actually looks like

The unit of analysis is an N × M cell matrix. The candidate dimensions:

**M — GTM functions (twelve)**

1. Demand generation and brand marketing
2. Content marketing and SEO
3. Inbound / PLG funnel optimization
4. Outbound prospecting (SDR / BDR)
5. Account-based marketing (ABM)
6. New-business sales (AE)
7. Sales enablement and training
8. RevOps / Sales Ops / data and tooling
9. Deal desk / pricing / procurement (the buyer-facing seam)
10. Customer success and onboarding
11. Account management, renewals, and expansion
12. Forecasting, GTM strategy, and planning

**N — Agent capabilities (ten)**

A. Research and enrichment (account, contact, intent)
B. Personalization and content generation (email, LinkedIn, ad, video, voice)
C. Multi-channel orchestration (email + LinkedIn + voice + SMS + meeting)
D. Conversation handling (chat, voice, multi-turn, escalation)
E. Meeting prep, listening, and follow-up
F. CRM and data hygiene, account/contact graph maintenance
G. Multi-step task execution (RFP responses, security questionnaires, MSA drafting)
H. Forecasting and decision support
I. Negotiation and pricing support
J. Coaching and performance management

That's 12 × 10 = 120 cells. Realistically, only 40–60 of those cells have meaningful current activity in May 2026, and only 15–25 are high-leverage opportunities for someone in Alex's position. The session's job is to identify those, rank them, and tie each one to a specific action.

This matrix is the central artifact of this session. Most other deliverables hang off it.

### The procurement seam — why it's the through-line

One particular cell in the matrix deserves special call-out because the prior session's Bet #1 lives inside it: cell (Function 9: Deal desk / pricing / procurement) × (Capability G: Multi-step task execution).

The buyer-side of enterprise AI procurement in 2026 is a six-counterparty workflow: InfoSec, Legal, Privacy, AI Governance Council, Procurement, and the business sponsor. Every Fortune 1000 AI vendor cycle moves through this gauntlet, and most vendors handle it badly because the InfoSec questionnaire flow was designed for SaaS-circa-2018 and now has 100+ AI-specific addenda layered on top. The seller-side equivalent of this gauntlet is the AE / Sales Engineer / Deal Desk team doing one-off responses to each buyer's questionnaire with no cross-deal learning.

This is the exact cell where the prior session's Bet #1 (the Enterprise AI Procurement Playbook) lives, and it is the exact cell where Alex's prior career — selling INTO enterprise procurement at three companies — is the rarest experience. The Procurement Playbook will be drafted in this session as a real artifact, not just a future ambition. Specifically: a 25–35 page reference document, the agent-vendor version of the Vanta trust-center concept, openly published as the canonical reference for the F1000 AI buying gauntlet. It will become the inbound flywheel for everything downstream.

That document is one of the named expected outputs of this session.

### What this session inherits vs originates

**Inherited (do not re-derive):**

- The seven Big Bets, five Structural Risks, five Cruxes from Foundation.
- The agent-layer sub-strata definitions from Agent Zoom (or, if Agent Zoom hasn't run, the candidate list in `HANDOVER_A_AGENTS.md` §1).
- The talent + capital flow signals — especially the Stripe / Ramp / Datadog / Snowflake → Sierra / Decagon / Glean / Hippocratic migration, which IS the GTM × agents story seen from the labor side.
- The NYC market positioning conclusion.
- The OCQ × Wardley × 7 Powers × JTBD × Talent-flow framework discipline.
- The aesthetic ("Substrate" — ink on cream, hairline rules, vermilion/verdigris/ochre, condensed display caps).

**Originated here:**

- The 12 × 10 matrix of GTM functions × agent capabilities, populated and ranked.
- A vertical-by-vertical map of the agent-GTM company landscape with explicit "where is hiring happening for Alex's profile" tags.
- An updated Action Map that supersedes the original 6/12/18-month plan — same shape, much higher resolution.
- The Enterprise AI Vendor Procurement Playbook as a real published document.
- A "buyer's map" of how a F1000 actually purchases an agent product, end-to-end, with the role and concern of each counterparty named.
- An updated tracker focused on agent-GTM company signals specifically.

The composition rule: Foundation establishes field constraints, Agent Zoom establishes layer dynamics, GTM Intersection produces the operating playbook.

### What success looks like

At the end of this session, Alex should be able to:

- Walk into any vertical agent company selling INTO GTM teams (Sierra, Decagon, Cresta, 11x, Clay, Cognism-AI, Outreach AI, Apollo AI, Gong AI, Salesloft AI, Aircover, etc.) and demonstrate buyer-side mastery of the very function their product targets.
- Hand a Fortune 1000 CIO/CISO/AI Council the Enterprise AI Vendor Procurement Playbook and have it read as authoritative.
- Hold a CRO conversation about the right way to staff a GTM org against agent-augmented workflows.
- Diagnose any agent-GTM product within ten minutes against a structured rubric — which cells of the matrix it covers, which durable powers it has, which JTBD outcomes it solves, which open questions it dodges.
- Decide, with data, whether to (a) take a senior GTM role at a named vertical agent company, (b) productize the Procurement Playbook into a SaaS, or (c) consult / advise across multiple agent-GTM vendors. The matrix tells him which path the cells reward best.

That's the bar.

---

## 2. The methodology inheritance (so this session can replicate the discipline)

### Skills loaded in the prior sessions

(Same as `HANDOVER_A_AGENTS.md` §2 — refer to that document for the full list.)

The most-load-bearing for this session:

- **anthropic-skills:canvas-design** — for the new "GTM Cell Matrix" plate and the Procurement Playbook's visual elements.
- **anthropic-skills:docx** — for the Procurement Playbook document AND the GTM Decisions playbook AND the foundation report.
- **`Product/jtbd-strategy-and-organization`** and **`Product/outcome-driven-innovation-and-job-mapping`** — JTBD at the organizational scale, not the product scale. This skill is the most useful for analyzing the GTM org as a system of jobs.
- **`GTM/*`** subskills (Sales, Growth, Marketing, RevOps, CS_Post_Sale, partnership-bd) — these have not been loaded in prior sessions because the focus was field-level. They are critical here.
- **`Product/decision-intelligence-fundamentals`** + **`Product/causal-decision-modeling`** — for the buyer's-map artifact.
- **`Organizational Leadership/problem-definition`** — for the Procurement Playbook (Lochhead "spend time on the problem"; Moesta struggling moments at each counterparty).

### Repo skills NOT YET LOADED that this session should use

These were not used by Foundation or Agent Zoom and should be specifically pulled in here:

- `GTM/Sales/*` — for the AE / new-business motion.
- `GTM/Growth/*` — for the PLG / inbound motion.
- `GTM/Marketing/*` — for the demand-gen and content side.
- `GTM/RevOps/*` — for the data / tooling / forecasting side.
- `GTM/CS_Post_Sale/*` — for the customer success / renewal / expansion side.
- `GTM/partnership-bd/*` — for the channel / partnership angle.
- `Product/product-led-sales` — for the PLG-meets-enterprise motion.
- `Product/product-led-growth` — for the PLG funnel side.
- `Product/measuring-product-market-fit` — applied to the agent-GTM segment.

Read the SKILL.md for each of these in Phase 0 of this session. They will reshape the framework definitions in non-trivial ways.

### The order of operations

**Phase 0 — Calibration (30–60 min)**
- Read this handover document in full.
- Read `Me/claude.md` and `STACK_README.md`.
- Read the seven Foundation artifacts and, if available, the seven Agent Zoom artifacts.
- Read the GTM skills listed above (load the SKILL.md headers; deeper read for any that look critical).
- Confirm the 12 × 10 matrix axes with Alex before dispatching agents (the candidate definitions are above; he may want to adjust, e.g., to split outbound from ABM, or merge renewals into expansion, or add "GTM enablement tooling" as its own function).

**Phase 1 — Cell population (parallel agents, 90–120 min wall-clock)**
- Dispatch six parallel `general-purpose` sub-agents covering buckets of the matrix:
  - C1: Marketing (functions 1–3) × all capabilities. Includes content gen, demand gen, ABM.
  - C2: Outbound + AE (functions 4–6) × all capabilities. The largest cell-count bucket.
  - C3: Enablement, RevOps, Deal desk (functions 7–9) × all capabilities. Includes the procurement-seam cell explicitly.
  - C4: CS, AM, Renewals (functions 10–11) × all capabilities.
  - C5: Forecasting and GTM strategy (function 12) × all capabilities. Smaller cell-count.
  - C6: Cross-function agent platforms (Clay, Glean, Notion AI, Mosaic, etc.) — these are tools that span multiple functions and need a cross-cut treatment.
- Briefs are in §4 below.

**Phase 2 — Matrix synthesis and visual atlas (45–60 min)**
- Assemble the cell map. Mark every cell with: maturity (0–5), opportunity score (0–15 using OCQ definition), claimability for Alex (1–5), and 1–3 named companies.
- Build `AGENTS_GTM_MATRIX.pdf` — a single large plate showing the 12 × 10 matrix with cell intensity coding. Mirrors the OCQ heat map from `AI_STACK_SUBSTRATE_VOL2.pdf` Plate VII.
- Build `AGENTS_GTM_SUBSTRATE.pdf` — 4–5 plates: the matrix index, by-function deep-dives, the buyer's map, the talent flow plate.

**Phase 3 — Framework analysis dispatch (parallel agents, 90–120 min)**
- Dispatch six parallel framework agents using briefs in §5 below:
  - F1 — Wardley Mapping for agent-GTM tools.
  - F2 — 7 Powers for the named agent-GTM companies.
  - F3 — Ecosystem JTBD applied to the GTM org as the customer.
  - F4 — Talent + Capital Flow specifically in agent-GTM companies.
  - F5 — Buyer-side procurement workflow analysis (the six-counterparty gauntlet).
  - F6 — Pricing and packaging analysis of agent-GTM products (outcome-based vs seat vs usage).

**Phase 4 — Decisions playbook (60–90 min)**
- Build `AGENTS_GTM_ADDENDUM.docx` — the decisions playbook for the intersection. ~16,000 words. Same structure as the Foundation addendum: OCQ Matrix, Wardley, 7 Powers, JTBD, Synthesis, Action Map, Best-Use-Case Reflections.
- The Synthesis here is critical: it should produce the **updated 7 Big Bets** that supersede the Foundation bets. Some Foundation bets will be unchanged; some will be re-ranked; some will be subdivided into agent-GTM-specific sub-bets.

**Phase 5 — The Procurement Playbook (90–120 min)**
- This is the headline deliverable of this session. Build `AI_VENDOR_PROCUREMENT_PLAYBOOK.docx` — a 25–35 page reference document targeted at Fortune 1000 AI buyers (CIO, CISO, AI Council Chair, Chief Procurement Officer, GC).
- Structure: Executive Foreword; The Six Counterparties (1 chapter each); The 14 AI-Specific Addenda Every Vendor Should Pass; The Decision Tree (when to buy, when to build, when to wait); Vendor Scoring Rubric (the named matrix); Glossary of Agent-Specific Terms; Appendix of Reference Contract Clauses.
- Target audience tone: senior buyer-side reader, not technical, decision-relevant. Voice: Alex's voice — direct, commercial, no theatrics.

**Phase 6 — Master Plate and Tracker (45 min)**
- `AGENTS_GTM_MASTER_PLATE.pdf` — one plate, same aesthetic, synthesizing the matrix + the buyer's map + the named bets + the cruxes. Mirrors `AI_STACK_MASTER_PLATE.pdf`.
- `AGENTS_GTM_TRACKER.md` — living tracker focused on agent-GTM signals: per-cell maturity changes, hiring patterns at named companies, new product launches, ARR updates, regulatory changes affecting GTM tooling (e.g., CCPA email-personalization rulings, CAN-SPAM AI-content rulings).

**Phase 7 — Cross-session synthesis (30 min)**
- One short addendum to `OCQ_TRACKER.md` in `output/ai-stack/` noting the deltas to the original 7 Big Bets — which were reinforced, which were re-ranked, which were superseded. This keeps the three-session chain coherent rather than producing three islands.

---

## 3. The inheritance — full reference

**From Foundation (`output/ai-stack/`):**

- `AI_STACK_SUBSTRATE.pdf` (Vol I) · `AI_STACK_SUBSTRATE_VOL2.pdf` (Vol II) · `AI_STACK_MASTER_PLATE.pdf`
- `AI_STACK_REPORT.docx` · `AI_STACK_ADDENDUM.docx`
- `OCQ_TRACKER.md`
- `design_philosophy.md`
- All build scripts (`build_*.py`, `build_*.js`)

**From Agent Zoom (`output/ai-agents/`, if completed):**

- `AI_AGENTS_SUBSTRATE.pdf` · `AI_AGENTS_SUBSTRATE_VOL2.pdf` · `AI_AGENTS_MASTER_PLATE.pdf`
- `AI_AGENTS_REPORT.docx` · `AI_AGENTS_ADDENDUM.docx`
- `AI_AGENTS_TRACKER.md`
- `design_philosophy_agents.md`

**Critical conclusions to anchor on:**

- **Bet #1** from Foundation: Enterprise AI Procurement Playbook + Practice. Conviction ★★★★★. This session converts the ambition into a real document.
- **Bet #2** from Foundation: Vertical Agent GTM Leadership Role at Sierra/Decagon/Glean/Harvey/Hippocratic/Augment. Conviction ★★★★★. This session refines the target list and the pitch.
- **The talent migration finding**: Stripe/Ramp/Datadog/Snowflake enterprise sellers → vertical agent companies, mid-six base + meaningful equity. This is the exact path for Alex's profile.
- **Crux #3**: MCP commons vs fork. Decidable H2 2026. If commons holds, the agent-GTM ecosystem standardizes; if it forks, every agent-GTM company gets repriced.
- **Risk #5**: Foundation labs walking up-stack into vertical apps. Watch ChatGPT Business Connectors, Claude for Work, Gemini Workspace agent features. This is the structural overhang on every vertical agent company.

---

## 4. Phase 1 — Cell-population agent briefs (6 agents, ready to dispatch)

Each agent populates a slice of the 12 × 10 matrix. Briefs are tight; word caps firm.

### Agent C1 — Marketing functions (functions 1–3) × all agent capabilities

**Scope:** Demand generation, content marketing/SEO, inbound/PLG funnel optimization. For each cell where activity exists, name 1–3 leading companies/products, name the underserved JTBD, and score the Opportunity / Challenge / Open Question per the OCQ lens. Cover both incumbents adding agent features (HubSpot Breeze, Marketo Velocity, 6sense, Drift, Intercom Fin) and AI-native entrants (Jasper, Copy.ai, Writer, Mutiny, Devin's-marketing-counterparts, Common Room, Gong "predict marketing").

**What to surface specifically:**
- The content gen × demand gen overlap (where MQL-to-SQL automation actually works).
- The PLG funnel optimization cell (Mutiny, Common Room, Endgame, Pocus) — and where agent-augmented PQL identification crosses the line into RevOps.
- ABM × research-and-enrichment (6sense, Demandbase, ZoomInfo Copilot).
- Compliance posture: CAN-SPAM, CASL, GDPR for AI-generated content.

**Output:** ~2,000 words structured markdown. Each cell with 2–4 sentences: status, named players, gap, score.

### Agent C2 — Outbound + AE (functions 4–6) × all agent capabilities

**Scope:** Outbound prospecting (SDR/BDR), account-based marketing, new-business AE motion. This is the densest cell-count bucket and the most-funded. Cover Apollo, ZoomInfo, Cognism, Clay (which dominates this), 11x, AiSDR, Artisan, Regie, Outreach AI, Salesloft AI Cadences, Aircover, Nooks (parallel dialer), Salesforce AI Sales Cloud, HubSpot Sales Hub AI, Gong AI sales coaching, Chorus, Cresta, Microsoft Sales Copilot.

**What to surface specifically:**
- The buying-committee mapping gap — JTBD Job #1 from Foundation's Ecosystem JTBD (gap of 7). No one owns this.
- The deal-diagnosis cell — when a deal stalls, why? Gong sees activity, not causation.
- The handoff seam — SDR → AE → CSM. Agent-augmented handoffs are wide open.
- ABM agents that actually drive pipeline (rare). The "we'll personalize at scale" promise vs reality.
- Pricing model patterns: per-seat for AEs, per-message for SDR tools, outcome-based experiments at Sierra/Cresta level.

**Output:** ~2,800 words. Same structure.

### Agent C3 — Enablement, RevOps, Deal Desk (functions 7–9) × all agent capabilities

**Scope:** Sales enablement and training, RevOps / Sales Ops / data and tooling, deal desk / pricing / procurement. This bucket contains the procurement-seam cell that the entire session is built around.

Cover sales-enablement AI (Highspot AI, Seismic Aura, Showpad Coach, MindTickle); RevOps (Clari AI, Boostup, Aviso, RevOps.io, Pocus, Endgame); deal desk tooling (Salesforce CPQ AI, DealHub AI, Subskribe, Chargebee); procurement-side tooling for buyers (Vendr, Tropic, Sastrify, ProcurementIQ, Drata for vendor-side trust); MSA / contract automation (Ironclad AI, LinkSquares, SpotDraft).

**What to surface specifically:**
- The procurement-seam cell — what exists on both buyer and seller side; what does NOT exist that needs to.
- The RFP / security-questionnaire automation cell — Loopio, Responsive, Vanta, Drata AI, plus AI-native entrants.
- The deal-diagnosis cell from the seller side (different from C2's deal diagnosis).
- Enablement-AI gaps: rep ramp curves are still terrible despite AI augmentation.
- The "AI-specific contract addendum" cell — who, if anyone, has automated the negotiation of AI vendor terms.

**This is the most important agent of all six. Allocate the most depth here.**

**Output:** ~3,000 words. Same structure plus a dedicated 600-word section on the procurement-seam cell specifically.

### Agent C4 — CS, AM, Renewals (functions 10–11) × all agent capabilities

**Scope:** Customer success, account management, renewals and expansion. Sierra and Decagon dominate the CX-agent side. Cover Sierra, Decagon, Cresta, Ada, Intercom Fin, Forethought, Kustomer, Ultimate.ai, Zendesk AI agents, Salesforce Service Cloud Agentforce, ServiceNow AI Agents, Gainsight AI, Catalyst AI, Vitally AI, ChurnZero AI, Pylon, Asana / Notion CS workflows. Plus the named NYC-anchored: Hippocratic (healthcare CX), Replit Agent (developer CS-like).

**What to surface specifically:**
- The escalation-handoff cell — when does the agent ask for human help? This is the #1 question CIOs ask in procurement.
- The renewal-risk diagnosis cell — Gainsight does this poorly; agent-augmented versions are unproven.
- The expansion-detection cell — where in usage data does an upsell signal live, and which agents surface it.
- Outcome-based pricing experiments (Bret Taylor's thesis from Sierra) — what they actually look like contractually.
- Compliance: GDPR right-to-be-forgotten in agent memory; HIPAA in healthcare CS agents.

**Output:** ~2,400 words.

### Agent C5 — Forecasting and GTM strategy (function 12) × all agent capabilities

**Scope:** Sales forecasting, pipeline analytics, GTM strategy and planning. Cover Clari (incumbent), Boostup, Aviso, Gong Forecast, Salesforce Einstein Forecasting; territory planning (Fullcast, Anaplan AI, Pigment AI); GTM strategy support agents (rare — most planning is still spreadsheet + judgment).

**What to surface specifically:**
- Forecast accuracy gains from AI vs human: real data only, not vendor claims.
- The GTM-strategy gap: there is no agent that meaningfully helps a CRO design a GTM motion. Underserved cell.
- The board-prep cell: what gets automated, what doesn't, what shouldn't.

**Output:** ~1,800 words. Smaller bucket.

### Agent C6 — Cross-function agent platforms (the platforms that span)

**Scope:** Clay (data enrichment that spans marketing + outbound + RevOps); Glean (enterprise search that spans CS + marketing + sales enablement); Notion AI / Mosaic-style cross-function tools; Microsoft 365 Copilot for sales; Google Workspace Gemini for sales; Salesforce Agentforce as a horizontal platform; ServiceNow / Workday agent stories. These need a cross-cut treatment because they don't sit in any one cell.

**What to surface specifically:**
- The "horizontal platform" thesis — is it real or do verticals always beat horizontals in GTM?
- The buyer-counter to horizontal-platform sales: existing platform lock-in (Salesforce, Microsoft) creates structural advantage for incumbents shipping AI features.
- The "AI-native horizontal" challenger pattern (Glean, Clay) vs the "incumbent-with-AI" pattern (Salesforce, HubSpot).
- Where Alex's enterprise selling experience is most valuable: at horizontal platforms or at vertical agents.

**Output:** ~2,200 words.

**Total Phase 1 output:** ~14,200 words. Synthesizable into a populated matrix.

---

## 5. Phase 3 — Framework analysis agent briefs (6 agents)

### Agent F1 — Wardley Mapping for agent-GTM tools

**Brief:** anchor four user-need top-of-map items specific to GTM-leader buyers: "fill the top of the sales funnel reliably without scaling headcount linearly"; "compress sales cycle for enterprise deals through automated procurement workflow"; "increase NRR through proactive customer-success interventions"; "produce accurate quarterly forecasts the board will trust." Trace dependency chains down through each GTM function and the agent capability it relies on. Place each named agent-GTM tool at its current evolution stage. Identify 5–7 punctuated equilibria specific to agent-GTM in 2026–2027 (e.g., outcome-based pricing crossing into Product stage; Sierra ARR crossing $500M; Salesforce Agentforce gaining vs vertical CX startups; MCP-native sales-tool standardization). Strategic quadrants for someone in Alex's position.

**Output:** ~2,400 words.

### Agent F2 — 7 Powers analysis for named agent-GTM companies

**Brief:** apply Helmer's 7 Powers to ~30 specific agent-GTM companies. Score each on Scale, Network, Counter-Positioning, Switching Costs, Brand, Cornered Resource, Process Power. Identify the five most durable agent-GTM positions (likely Sierra, Glean, Clay, Decagon, possibly Cresta or Harvey-adjacent legal-ops). Identify the five most over-rated (where brand or buzz outpaces structural moat). Conclude with implications for Alex's "join vs build" decision per company.

**Output:** ~2,400 words.

### Agent F3 — Ecosystem JTBD applied to the GTM org as customer

**Brief:** the customer here is not the end-buyer of the agent — it is the GTM org buying the agent on behalf of its motion. Five top-down jobs of a GTM org: "Hit the number this quarter"; "Hit the number next year without doubling headcount"; "Reduce CAC payback period"; "Increase NRR above 120%"; "Get the forecast right." For each, build an 8-phase Job Map showing where agent-augmented capability could land. Identify the three highest-gap underserved outcomes per job. End with the three jobs where Alex's commercial fluency is most directly applicable.

**Output:** ~2,800 words.

### Agent F4 — Talent + Capital Flow specifically in agent-GTM companies

**Brief:** extend the Foundation Talent + Capital tracker focused on agent-GTM hires and funding events. Track senior GTM hires (VP Sales, CRO, VP CS, VP RevOps) at named agent-GTM companies over the past 12 months. Track which companies are hiring Director / Field-CTO / Head of GTM Strategy roles — Alex's exact target. Capital events specifically affecting agent-GTM companies; M&A patterns; the NYC angle. Include Stripe / Ramp / Datadog / Snowflake → agent-GTM company migration tracking by name and date. End with a target list: the 10 highest-velocity hiring agent-GTM companies in Alex's target band, NYC-friendly or NYC-anchored.

**Output:** ~3,000 words. Format as living-tracker maintainable.

### Agent F5 — The six-counterparty buyer-side procurement workflow

**Brief:** map the F1000 AI vendor procurement gauntlet in detail. Six counterparties: InfoSec, Legal, Privacy, AI Governance Council, Procurement, Business Sponsor. For each: who they report to, what they actually evaluate, what they will reject for, what their typical review-cycle duration is, what artifacts they need from the vendor (SOC 2, BAA, DPA, AI addendum, model card, eval results, kill-switch documentation, etc.). Identify the 14 AI-specific addenda that have emerged as common buyer demands in 2025–2026. This is direct input to the Procurement Playbook in Phase 5.

**Output:** ~3,500 words. Detailed enough that it can be lifted into the Playbook directly.

### Agent F6 — Pricing and packaging analysis

**Brief:** how do agent-GTM products price? Compare per-seat (Salesforce, HubSpot, Outreach traditional); per-message / per-usage (Sierra, Decagon for inbound CX volume); outcome-based (Sierra emerging, Bret Taylor's thesis); hybrid (Cresta, Gong AI add-ons). Identify the 3–4 buyer objections that recur across pricing models. Cover the contract negotiation reality: what AI-specific terms get negotiated (training rights, output ownership, model-update notice, hallucination indemnity, agent-action liability). Pricing power forecast: where does compression happen, where does premium hold.

**Output:** ~2,200 words.

**Total Phase 3 output:** ~16,300 words.

---

## 6. Expected deliverables

Final output folder: `output/agents-gtm/`

| File | Mirrors / Originates | Target |
|---|---|---|
| `AGENTS_GTM_MATRIX.pdf` | New artifact (the 12 × 10 cell matrix) | 1 large plate |
| `AGENTS_GTM_SUBSTRATE.pdf` | Mirrors `AI_STACK_SUBSTRATE.pdf` | 5 plates: matrix index, by-function deep-dives, buyer's map, talent flow |
| `AGENTS_GTM_DECISIONS.pdf` | Mirrors `AI_STACK_SUBSTRATE_VOL2.pdf` | 5 plates: OCQ heat (cell-level), Wardley, 7 Powers, JTBD, Action Portfolio |
| `AGENTS_GTM_MASTER_PLATE.pdf` | Mirrors `AI_STACK_MASTER_PLATE.pdf` | 1 plate: synthesis |
| `AGENTS_GTM_REPORT.docx` | Mirrors `AI_STACK_REPORT.docx` | ~10,000 words foundation report at agent-GTM resolution |
| `AGENTS_GTM_ADDENDUM.docx` | Mirrors `AI_STACK_ADDENDUM.docx` | ~16,000 words decisions playbook for the intersection |
| **`AI_VENDOR_PROCUREMENT_PLAYBOOK.docx`** | **New flagship artifact** | **25–35 page reference document, the canonical buyer-side reference** |
| `AGENTS_GTM_TRACKER.md` | Mirrors `OCQ_TRACKER.md` | Agent-GTM living tracker |
| `BETS_DELTA_NOTE.md` | New small artifact | Appended to `output/ai-stack/OCQ_TRACKER.md` noting changes to the original 7 Big Bets |

The Procurement Playbook is the headline. It is the artifact that converts Bet #1 from ambition into reality. It should be written for a Fortune 1000 senior buyer — CIO, CISO, Chief Procurement Officer, GC, AI Council Chair — with Alex's name on the cover.

---

## 7. The tailored framework — agent-GTM-specific lens definitions

Tighten the standard OCQ definitions one more time for this intersection.

**OPPORTUNITY (agent × GTM):** where in the matrix is value being created faster than the GTM-leader narrative reflects, AND where can someone with twelve years of enterprise B2B GTM experience plus working AI-builder skills claim a position — either by joining (Bet #2 from Foundation), by building (Bet #3 / #4 / #5 from Foundation), or by advising-and-publishing (Bet #1 / #6 from Foundation)? Score: Confidence × Time-to-Monetize × Claimability for Alex specifically — and now also Cell-density (how many cells of the matrix the opportunity touches). Total out of 20.

**CHALLENGE (agent × GTM):** what binds the intersection? Specifically: foundation labs walking into vertical agent territory (Risk #5 from Foundation, sharpened here); CRM/CDP/marketing-cloud incumbents shipping native AI faster than expected (Salesforce Agentforce, HubSpot Breeze, Microsoft Sales Copilot); enterprise procurement-cycle elongation as governance maturity outpaces vendor readiness; outcome-based pricing not converting at scale; talent-comp inflation pricing out small entrants. Score: Severity × Probability × Alex exposure × Bet-coverage (how many of his bets it threatens). Total out of 20.

**OPEN QUESTION (agent × GTM):** what cruxes remain? Specifically: does outcome-based pricing actually scale beyond Sierra-class deals; does the buying committee consolidate or fragment further; does the CRM incumbents' AI-feature shipping pace catch the vertical agents before they reach platform-scale; does the procurement gauntlet relax with familiarity or harden with regulation; does ChatGPT Business / Claude for Work absorb the SDR-AI category. Score: Decidability × Asymmetry × Bet-size implication × Time-window-narrowing-rate. Total out of 20.

---

## 8. Final notes for the new session

- **The Procurement Playbook is the prize.** All other deliverables are reference; this one is the artifact Alex carries into every conversation for the next 12 months. Treat it accordingly. Voice should be his — direct, commercially fluent, not afraid to take a position. Length 25–35 pages of dense reference material.
- **Update the 7 Big Bets.** The original Foundation bets were field-level. After this session, four to five of them get sharpened and one or two may get superseded by new agent-GTM-specific bets that the cell matrix surfaces. Make this delta explicit in `BETS_DELTA_NOTE.md` and append to the original tracker.
- **Name the cells.** Throughout the deliverables, refer to specific matrix cells by their (Function, Capability) coordinate. This is the unit of analysis; treating it consistently makes the whole document easier to reference.
- **Show your work on convergence.** Where the cell matrix, Wardley map, 7 Powers analysis, JTBD, and talent flow all converge on the same opportunity — say so explicitly. Where they diverge, say that too.
- **NYC focus stays.** The Foundation conclusion that NYC is winning in vertical-agent GTM holds; this session should reinforce it with specific named NYC roles, NYC events, NYC operators worth meeting, and NYC-anchored buyer accounts to target.
- **Cycle time.** This session is heavier than the prior two. Plan for 6–8 hours of wall-clock work — 4 hours of agent dispatch and run-time, 2–4 hours of synthesis and document build. The Procurement Playbook alone is a 90–120 minute deliverable.

When ready, the new session opens with: "I have read HANDOVER_B_AGENTS_GTM.md and the inherited artifacts from `output/ai-stack/` (and `output/ai-agents/` if present). I am beginning Phase 0 calibration."
