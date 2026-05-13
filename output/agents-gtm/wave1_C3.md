# Wave-1 / C3 — Enablement × RevOps × Deal Desk × all 13 capabilities

**Agent codename:** C3
**Scope:** Functions 7 (Sales enablement & training), 8 (RevOps / Sales Ops / data & tooling), 9 (Deal desk / pricing / procurement) × Capabilities A–M
**Date:** 2026-05-12
**Cell of record:** (9, G) — Deal desk × Multi-step task execution (RFPs / security questionnaires / MSAs). The through-line of Alex's three-session arc. Dedicated 600-word section at the end.

---

## 0. Framing — State of play, May 2026

These three functions are where the seller's internal cost-to-close meets the buyer's internal cost-to-buy, and they are the functions where agents have moved fastest from copilot to operator. Three structural facts dominate May 2026:

1. **Enablement-AI is a coaching-feedback business now, not a content-library business.** Highspot AI, Seismic Aura, Showpad Coach, MindTickle Copilot all relaunched 2025 around AE coaching agents that watch Gong/Chorus trajectories. The ramp-curve problem is not solved — median enterprise AE ramp held at ~7 months (SiriusDecisions/Forrester 2026 benchmark) despite four years of "AI enablement" — because agents coach surface activity (calls/emails) and not the underlying buyer-side counterparty work that decides 6-figure deals.
2. **RevOps is being eaten from two sides.** Clari AI ($2.6B 2024 round; reportedly approaching $300M ARR Q1'26) and Boostup/Aviso compete on forecasting AI; Pocus/Endgame/UserGems compete on PLG signal-to-pipeline AI; DealHub/Subskribe compete on agentic CPQ; Mosaic on strategic finance. Every layer is being agentified, but the **integration seam between them remains an open RevOps job that no incumbent has unified.** Capability G (multi-step task execution) in RevOps is the most underserved combination on this map after (9, G).
3. **Deal desk is the single highest-density agent procurement seam in the enterprise.** Ironclad AI (Series E rumor $200M+ at $3B+, April 2026), LinkSquares (Series D 2024), SpotDraft (Series B $54M Aug 2024, NYC-adjacent), Lexion (Docusign 2024 acquisition), Evisort (Workday 2024 acquisition) all ship contract-side automation. Vendr ($150M Series B 2022; reportedly flat in 2025), Tropic ($100M Series C 2023; "Spend Intelligence" 2025 launch), Sastrify (Series B €32M 2023) ship buyer-side. **Neither side has shipped the bilateral artifact** — the signed, reproducible, agent-trajectory evidence pack the F1000 InfoSec/Legal/Privacy/AI Governance/Procurement gauntlet now demands for agent vendors specifically. That is the (9, G) gap.

The single most-actionable near-term regulatory lever in this whole region is **EU AI Act Article 14 (human-oversight) enforcement guidance — draft April 2026, enforceable late 2026** — because Article 14 is *agentic-trigger-specific* and bites every deal desk that closes an agent vendor without a documented oversight tie-out. Bet #1 anchors here.

---

## 1. Function 7 — Sales Enablement & Training (cells 7A–7M)

### 7A — Research
**Status:** Saturated; commoditized. **Companies:** Highspot AI [IX], Seismic Aura [IX], MindTickle Copilot [IX].
**JTBD:** Pull account/competitor/persona briefs into enablement assets at draft time so reps see context-tailored content. **OCQ:** 8/20 (low claimability; everyone ships it).
Highspot's "AI-Generated Plays" (relaunched May 2025) and Seismic Aura's "Account Briefs" (GA Sep 2025) both stitch ZoomInfo + Crunchbase + internal CRM into the asset surface. Functional, not differentiated. Alex has no claim here.

### 7B — Personalization
**Status:** Active; AE-side personalization arms race. **Companies:** Seismic Aura [IX], Highspot AI [IX], Regie.ai [IX].
**JTBD:** Re-cut a master pitch deck or one-pager for a specific account/persona/stage without rep effort. **OCQ:** 9/20.
The 2025 launches (Aura "Living Decks" April 2025; Highspot "AI Slides" Aug 2025) generate decks at 60-90s latency. Adoption is real (Aura cited 40% rep-side usage at Dreamforce 2025) but **measurement of revenue impact is still anecdotal** — no incumbent has published a controlled study.

### 7C — Multi-channel orchestration
**Status:** [gap as a distinct enablement capability]. Belongs to outbound/ABM (C2's lane). [no public datapoint May 2026 for enablement-specific orchestration].

### 7D — Conversation handling
**Status:** Crowded; Gong/Chorus dominate. **Companies:** Gong [IX], Chorus (ZoomInfo) [IX], Avoma [IX], Fireflies [IX].
**JTBD:** Watch every rep call, flag risk moments, surface coachable patterns. **OCQ:** 8/20.
Gong's "Engage" agent (2024) and "Forecast" (2025) have moved Gong from observability to action. The 2026 pattern: every enablement agent quietly reads from Gong; the surface companies are reluctant to admit Gong is the substrate.

### 7E — Meeting prep
**Status:** Active; commoditizing. **Companies:** Granola [IX], Read.AI [IX], Highspot AI [IX], MindTickle.
**JTBD:** Brief the AE 30 min before the call with attendees, account history, last-call action items. **OCQ:** 7/20 — table stakes.
Granola's enterprise tier (Mar 2026 launch) is the cleanest implementation; Read.AI ships similar; Highspot/MindTickle bundle this into platform.

### 7F — CRM hygiene
**Status:** [partially gap from enablement angle]. Enablement tools don't write to CRM cleanly; RevOps owns this (see 8F). [no public datapoint May 2026 for enablement-specific CRM hygiene].

### 7G — Multi-step task execution
**Status:** Underserved. **Companies:** MindTickle [IX] (certifications), Spekit [IX], Lessonly/Seismic Learning [IX].
**JTBD:** Run a multi-week rep certification workflow end-to-end — schedule, deliver, grade, escalate, sign off. **OCQ:** 11/20.
Certification flows are the rare "agent" use case in enablement, but **none of the incumbents has shipped a tool-use agent that can actually fail a rep, escalate to the manager, and reschedule the recertification.** This is a near-term opportunity; not Alex's bet.

### 7H — Forecasting
**Status:** [gap from enablement angle; lives in RevOps]. See 8H.

### 7I — Negotiation / pricing
**Status:** [partial gap]. Enablement tools coach on negotiation; pricing logic lives in deal desk. The only company straddling: **Gong** ("deal-risk negotiation flags," 2025). **OCQ:** 9/20.

### 7J — Coaching
**Status:** **Most-claimed cell in enablement; ramp-curve problem unsolved.** **Companies:** Highspot AI Coach [IX], MindTickle Copilot [IX], Showpad Coach [IX], Second Nature [IX], Hyperbound [IX] (synthetic-buyer role-play; Series A $15M Mar 2026).
**JTBD:** Watch rep calls/emails, give real-time + reflective coaching to ramp to quota faster. **OCQ:** 14/20 — high cell density, opportunity = "why does ramp still take 7 months?"
**The enablement-AI gap surfaced.** Despite four years of AI coaching, the median F1000 AE ramp held at ~7 months in 2026. The diagnosis: coaching agents grade **surface activity** (talk-time ratio, filler-word frequency, discovery-question count) and not the **underlying buyer-counterparty work** that decides 6-figure deals — handling InfoSec questionnaires, MSA redlines, EU AI Act Article 14 questions from AI Governance. **The actionable opportunity:** coach the procurement-seam work, not the call. This connects directly to Bet #1.

### 7K — Computer-use
**Status:** Nascent. **Companies:** Hyperbound (browser-driven role-play sims, 2025), Second Nature.
**JTBD:** Drive the rep's Salesforce/Outreach/Slack from a coaching shadow to demonstrate "what good looks like." **OCQ:** 9/20.
OSWorld 65% (Crux C3) would change this materially — a coaching agent that can show the rep exactly the click sequence to log a deal correctly in CPQ. [no public datapoint May 2026 of this shipping.]

### 7L — Persistent memory
**Status:** [gap]. Coaching agents do not yet carry rep-specific memory across quarters; each call is graded fresh. **OCQ:** 8/20. The vendor that ships "Persistent AE Memory" (the rep's running profile of strengths, gaps, blockers across deals) wins the next coaching cycle. [no public datapoint May 2026].

### 7M — Trajectory observability
**Status:** **The interesting convergence cell.** **Companies:** Gong [IX], MindTickle Copilot [IX], Galileo [IX/VIII] (cross-applied from agent-eval).
**JTBD:** Watch the AE's full trajectory across systems (calls, CRM updates, emails, Slack DMs, screen actions) and grade it as an end-to-end task, not a series of activities. **OCQ:** 13/20.
**The J + M convergence Alex flagged.** Coaching (J) + trajectory observability (M) is the architectural future of enablement AI: agents grade the work, not the activity. No incumbent ships this turnkey today; it requires Gong-style call data + Highspot-style content engagement + RevOps-style CRM telemetry + actual screen-trajectory ingest. **The under-claimed enablement frontier.**

---

## 2. Function 8 — RevOps / Sales Ops (cells 8A–8M)

### 8A — Research
**Status:** Embedded in forecasting/territory tooling. **Companies:** Clari AI [IX], Pocus [IX], Endgame [IX]. **OCQ:** 7/20. Account 360 briefs surfaced inside Clari Copilot/Pocus dashboards. Functional, undifferentiated.

### 8B — Personalization
**Status:** [gap as RevOps capability — belongs to outbound/ABM]. [no public datapoint May 2026].

### 8C — Multi-channel orchestration
**Status:** Lives in marketing/outbound stack. [gap as RevOps function.]

### 8D — Conversation handling
**Status:** RevOps consumes Gong/Chorus; doesn't own conversation. [partial gap.]

### 8E — Meeting prep
**Status:** Lives in AE function. [gap.]

### 8F — CRM hygiene
**Status:** **The classic RevOps job; agentified.** **Companies:** Syft (Y Combinator W24), Default [IX], Truva [IX], Clari Copilot [IX], Salesforce Einstein 1 [IX].
**JTBD:** Keep contact/account/opportunity records correct, complete, deduplicated, current — without rep effort. **OCQ:** 11/20.
Salesforce Einstein 1 "Agentforce 2.0" (Dreamforce 2025) and Clari Copilot (May 2025) both ship hygiene agents. The hard part: **multi-tenant write-action governance** for an agent that can mass-mutate CRM. Audit logs are weak; rollback is weak. **Cross-references to (9, G) procurement seam — the agent-action-liability question is identical.**

### 8G — Multi-step task execution
**Status:** **High-density underserved cell. The RevOps equivalent of (9, G).** **Companies:** Clari AI [IX], Boostup [IX], Aviso [IX], Mosaic [IX]; emerging: Default [IX], Tomo (NYC).
**JTBD:** Run forecast prep, pipeline scrub, territory rebalancing, comp-plan adjustment as multi-step automated workflows — not as a series of dashboards the RevOps human must orchestrate. **OCQ:** 15/20.
2026 state: Clari ships "Forecast Copilot" that drafts the forecast narrative; **none of Clari, Boostup, or Aviso ships a multi-step agent that closes the pipeline scrub loop — flag a stuck deal, ping the AE, get a response, update the stage, retrigger the forecast.** The pipeline-scrub-as-agent is unbuilt at scale. Mosaic ($175M Series C 2022) ships finance-side but not GTM-side. The opportunity name: **"RevOps trajectory agent."** A 2026-2027 cell to watch.

### 8H — Forecasting
**Status:** **The original RevOps AI cell. Saturated.** **Companies:** Clari AI [IX], Boostup [IX], Aviso [IX], Salesforce Forecasting [IX], Gong Forecast [IX].
**JTBD:** Predict next-quarter bookings, identify gap, surface risk. **OCQ:** 10/20.
Clari's $2.6B 2024 round priced this category. Forecast accuracy MAPE benchmarks have plateaued ~8-12% across vendors; **the moat is now usability and integration, not algorithmic.** Bet adjacency: forecasting accuracy is the load-bearing variable in (9, G) deal-desk decisions.

### 8I — Negotiation / pricing
**Status:** RevOps consumes pricing decisions from deal desk. [partial gap; see 9I.]

### 8J — Coaching
**Status:** RevOps coaches managers (not AEs); thin. [gap.]

### 8K — Computer-use
**Status:** **Underserved. Real opportunity.** **Companies:** [gap; Anthropic Claude Computer Use generic; no GTM-specific incumbent.]
**JTBD:** Drive Salesforce/Outreach/Gong/HubSpot via screen to do the RevOps grunt work (territory reassignments, comp-plan reissue, list rebuild) at scale. **OCQ:** 12/20.
OSWorld 65% (Crux C3) would unlock this. No GTM-specific company has shipped credible CRM-driving computer-use agents; Salesforce Agentforce uses tool-use, not computer-use. **Watch:** if OSWorld crosses 65% Q3 2026 as Vol III predicts, RevOps tooling fragments — the bottleneck shifts from "build an integration" to "drive the UI." [no public datapoint of GTM-specific CU agent May 2026.]

### 8L — Persistent memory
**Status:** Embedded; not standalone. Clari/Boostup ship history-aware forecasting that uses persistent state. **OCQ:** 7/20.

### 8M — Trajectory observability
**Status:** **The convergence cell for RevOps.** **Companies:** Gong [IX] (rep trajectory), Galileo [IX/VIII], Arize [IX/VIII], LangSmith [IX].
**JTBD:** Watch the RevOps automation trajectory — which agent did what to which CRM record at what time — and surface anomalies. **OCQ:** 12/20.
The audit problem for agentic CRM mutation. **This is the same problem as (9, G) action-rollback documentation.** Cross-reference. No incumbent ships RevOps-specific trajectory observability; OpenTelemetry GenAI conventions (stabilized Jan 2026) are the substrate but no GTM-specific product wraps them.

---

## 3. Function 9 — Deal Desk / Pricing / Procurement (cells 9A–9M)

### 9A — Research
**Status:** Underserved as a deal-desk-specific capability. **Companies:** AlphaSense [IX] (deal intelligence for the seller-side; Series F $650M Jun 2024 at $4B), CB Insights, PitchBook.
**JTBD:** Brief the deal desk on the buyer's procurement history, past AI-vendor approvals, known objections. **OCQ:** 9/20.
The buyer-side research deal desks need is "has this customer signed a similar agent vendor; what redlines did they push." Nothing turnkey ships this — it's bespoke per deal.

### 9B — Personalization
**Status:** Pricing pages / proposal templates personalized by segment. **Companies:** DealHub AI [IX], Subskribe [IX], PandaDoc [IX].
**JTBD:** Customize the proposal to the buyer's industry/size/use case. **OCQ:** 8/20.
DealHub's "AI Quote Generator" (2024) and Subskribe's "Smart Proposals" (2025) are functional; the deal-desk operator still rewrites the AI draft 60-80% of the time on enterprise deals.

### 9C — Multi-channel orchestration
**Status:** [gap]. Belongs to buyer enablement / CS.

### 9D — Conversation handling
**Status:** [gap]. Deal desk doesn't run conversations.

### 9E — Meeting prep
**Status:** Light. Deal desk gets briefed for QBR/pricing committee meetings; nothing AI-specific ships. [no public datapoint May 2026.]

### 9F — CRM hygiene
**Status:** Cross-applied from 8F.

### 9G — Multi-step task execution — **THE CELL OF RECORD. See dedicated section §4.**

### 9H — Forecasting
**Status:** Deal desk consumes 8H. [partial overlap.]

### 9I — Negotiation / pricing
**Status:** **The "AI-specific contract addendum" cell Alex flagged.** **Companies:** Ironclad AI [IX], LinkSquares [IX], SpotDraft [IX], Lexion (Docusign), Evisort (Workday), Pactum AI (Series B $20M 2024; autonomous negotiation), Icertis [IX].
**JTBD:** Negotiate vendor terms — including AI-specific terms (training rights, output ownership, model-update notice, hallucination indemnity, agent-action liability) — semi-autonomously. **OCQ:** 16/20.
**This is the convergence of Bet #1 + Bet #3.** State of play May 2026:
- **Ironclad AI Assist (2024) + Repaper (2025)** generate redlines on standard terms; **no shipped AI-clause library** specific to agent procurement. Ironclad's April 2026 product roadmap (per public blog) commits to "AI vendor playbook templates" — *direct competitor to Bet #1's clause library.*
- **Pactum** runs autonomous supplier negotiation but on logistics/commodities, not AI vendor terms. The technology is the closest fit; the vertical is wrong.
- **The unmet job:** A 12-15 clause library for AI vendor MSAs (training-data warranty, output IP, model-pin notice, hallucination indemnity carve-outs, agent-action liability with rollback evidence, EU AI Act Article 14 oversight clause, sub-agent privilege separation, eval-reproducibility right-of-audit) — none of Ironclad/LinkSquares/SpotDraft/Lexion/Evisort ships this turnkey today (May 2026). **Falsifiability test:** if any one ships before Q4 2026, Bet #1's clause-library module loses its window.
This is also where the **vendor-IP-indemnity addendum library** opportunity (B3 OCQ Stratum III O9) lives. $25-60K artifact per engagement; high velocity.

### 9J — Coaching
**Status:** [gap]. Deal desk reps don't get coached in any structured way.

### 9K — Computer-use
**Status:** **The "agents driving CPQ" cell. Nascent but big.** **Companies:** [no incumbent]; adjacent — Salesforce CPQ Agentforce (tool-use, not screen), DealHub AI, Subskribe.
**JTBD:** Drive CPQ + DocuSign + procurement portals via screen to push a quote through the buyer's Coupa/Ariba/Workday Procurement instance. **OCQ:** 13/20.
**OSWorld 65% implications:** if a frontier system crosses 65% on OSWorld Q3 2026 (Vol III Crux C3), the bottleneck on deal-desk computer-use lifts. The job today: deal-desk humans spend hours each week clicking through Coupa/Ariba to chase a vendor through procurement. An agent that drives those portals on behalf of the seller is **direct Bet #1 buyer-side advisory product** — the playbook would name the failure modes (action-rollback gaps, sub-agent privilege violations in the buyer's environment) before adoption.

### 9L — Persistent memory
**Status:** **Underserved.** **Companies:** Ironclad AI [IX] (clause memory), LinkSquares [IX] (contract repository memory). **OCQ:** 10/20.
The job: "what did we negotiate with this exact counterparty 18 months ago?" Ironclad's Repaper edges into this; nothing ships agent-memory grade durability with audit/provenance. The vector-DB + memory architecture practice (Bet #5) compounds here.

### 9M — Trajectory observability
**Status:** **High-density underserved cell. Cross-references (9, G) heavily.** **Companies:** [no incumbent]; Galileo [IX/VIII], Arize [IX/VIII], Langfuse adjacent.
**JTBD:** Observe the agent's trajectory through the deal-desk workflow — what tools it invoked on the MSA, what redlines it generated, what evidence it cited — with signed audit logs the buyer-side AI Governance counterparty will accept. **OCQ:** 14/20.
This is the **agent-trajectory evidence pack** referenced in the addendum Part XIII Section 3 — "signed reproducible eval reports for this agent against my use case." **Nobody ships this turnkey today.** The unclaimed flag.

### Deal-diagnosis cell (seller-side post-mortem on lost deals)
**Status:** [partial gap]. **Companies:** Gong "Deal Insights," Clari "Win-Loss," Aviso. **OCQ:** 11/20.
Deal-loss post-mortems today are activity-based ("rep didn't follow up") and not procurement-seam-based ("buyer's AI Governance counterparty blocked at the autonomy-scope question"). **The opportunity:** post-mortem the procurement-seam failure modes, not the AE behavior. Direct Bet #1 module: "here are the six counterparties that kill agent deals and the questions they ask." This belongs in the Playbook.

---

## 4. The (9, G) Procurement-Seam Cell — Dedicated 600-word section

**Cell:** Function 9 (Deal desk / pricing / procurement) × Capability G (Multi-step task execution — RFPs / security questionnaires / MSA negotiation / agent-procurement gauntlet).

**OCQ score: 19/20.** Confidence 5 (every dimension of the Vol III addendum converges here). TTM 5 (Article 14 enforcement late 2026; Playbook publishable in 90 days). Claimability 5 for Alex (12-year procurement scar tissue + AI-builder fluency is a rare-profile prerequisite; no incumbent currently fills). Cell-density 4 (Vanta/Drata/Ironclad each ship adjacent slivers but no one bundles).

### a. Seller-side: what exists today, what they miss

**RFP/security-questionnaire automation** — Loopio (Series C $200M 2021, slowed 2025), Responsive (formerly RFPIO; PE-owned since 2023; "Responsive AI" launched Q4 2024), Ombud, ProcureDesk. AI-native challengers: **Arphie** (Series A $14M Sep 2024; YC W23), **AutogenAI** (Series B £39M 2023, UK), **Spot AI** (different company; not relevant). These tools answer the questionnaire. **What they miss:** the *agent-specific* questions don't yet have canonical answers — tool-boundary policy, action-rollback documentation, indirect prompt injection adaptive red-team results, signed reproducible eval reports against the buyer's use case, EU AI Act Article 14 human-oversight tie-out, sub-agent privilege separation diagrams, sectoral overlay (FINRA/HIPAA/TCPA). When the buyer's AI Governance counterparty asks "show me the adaptive-adversary prompt-injection test result for this agent against our use case," Loopio/Responsive return nothing useful.

**Contract / MSA automation** — Ironclad AI [IX], LinkSquares [IX], SpotDraft [IX], Lexion (Docusign), Evisort (Workday). All ship clause libraries; **none ships an agent-vendor clause library** (training-data warranty, output IP, model-pin notice, hallucination indemnity, agent-action liability, sub-agent privilege, eval-reproducibility right-of-audit). Ironclad's April 2026 roadmap mention is the closest competitive signal.

**Trust-center / SOC2 evidence** — Vanta [IX/VIII], Drata [IX/VIII], Secureframe [IX/VIII], TrustCloud. SOC2/ISO27001 fully automated. **AI-specific evidence (model cards, evals, DPAs, agent-trajectory replays, autonomy-scope docs, Article 14 oversight artifact)** — none ship a turnkey bundle. Vanta's "AI Trust Center" (announced Q4 2025) is the closest; it ships model cards and a policy library but no eval-reproducibility or trajectory artifact.

### b. Buyer-side: what exists, what they miss

**SaaS procurement** — Vendr [IX], Tropic [IX], Sastrify [IX], ProcurementIQ. They negotiate price and shortlist vendors. **None has shipped an "AI-vendor specific gauntlet" workflow** — the six-counterparty (InfoSec/Legal/Privacy/AI Governance/Procurement/business sponsor) sequenced approval workflow with agent-specific checks. Tropic's "Spend Intelligence" (2025) edges toward this but is generic SaaS spend.

**AI governance tooling** — Credo AI (Series A $12.8M 2022; quiet 2025), Holistic AI, Trustible. They ship governance frameworks for the buyer's AI council. None has shipped the *procurement workflow* yet.

### c. The unserved JTBD inside this cell — named

**"Pass the agent-specific procurement gauntlet in one calendar quarter without bespoke evidence regeneration per counterparty."** The job is bilateral: seller assembles evidence; buyer's six counterparties consume it; gaps escalate per sectoral overlay (FINRA, HIPAA, TCPA). The unserved core: **the evidence-pack interchange format that both sides accept.**

### d. Seven agent-specific procurement overlays — who's shipping toward each (May 2026)

| Overlay | Anyone shipping? | Closest incumbent |
|---|---|---|
| Tool-boundary policy | No turnkey | Lakera Red, Promptfoo (partial — testing only, not policy artifact) |
| Indirect prompt injection adaptive red-team | Partial | Lakera Red, Garak, Protect AI (PA acq Q3 2025) — none signed/audit-grade |
| Action-rollback documentation | No | [gap]; LangSmith trace replays adjacent |
| Sub-agent privilege separation | No | [gap]; MCP 0.3 auth substrate exists but no product wraps it |
| Signed reproducible eval reports | No turnkey | Inspect AI compatibility emerging; Galileo, Braintrust, Arize partial — none signed |
| EU AI Act Article 14 human-oversight tie-out | No | Credo AI, Holistic AI partial; **April 2026 draft just landed** |
| Sectoral overlays (FINRA / HIPAA / TCPA) | Partial | Hippocratic AI (HIPAA-internal); no procurement product cross-vendor |

**Verdict:** zero of seven shipped as turnkey bundles. **This is the unclaimed flag.**

### e. OCQ score: 19/20 (computed above)

### f. 100-word tactical note — what Alex's Procurement Playbook should anchor on

Anchor the Playbook on the **bilateral evidence-pack interchange format** — what the seller assembles, what each of the six counterparties consumes, what gaps escalate per sectoral overlay. Lead Chapter 1 with the **autonomy-scope document template** (the question every Article 14 reviewer asks first). Make the **signed reproducible eval report template** (Section 3 of the existing Part XIII Rubric) the downloadable artifact that anchors inbound. Cross-reference Ironclad/Loopio/Responsive/Vanta gaps explicitly; name them as adjacencies, not competitors. Falsifiability: 500 downloads / 50 inbounds in 60 days post-Week-12 publish. If Vanta ships an AI-Trust-Center 2.0 with eval-reproducibility before Q4 2026, the SaaS-productization branch is dead but the advisory branch survives.

---

## 5. Top 5 opportunities ranked by OCQ

1. **(9, G) — Agent procurement gauntlet bilateral evidence pack — OCQ 19/20.** The cell of record. Bet #1 lives here. See §4. Single highest opportunity in the entire C3 region.
2. **(9, I) — AI-specific contract addendum library — OCQ 16/20.** 12-15 clause library for agent vendor MSAs. Direct Bet #1 module. Falsified if Ironclad/LinkSquares/SpotDraft ships before Q4 2026.
3. **(8, G) — RevOps multi-step trajectory agent (pipeline scrub + forecast prep + territory rebalance loop closure) — OCQ 15/20.** Clari/Boostup/Aviso ship pieces; nobody ships the loop. 12-18 month build window. Not Alex's bet but a watched cell.
4. **(9, M) — Agent-trajectory evidence pack for deal desk — OCQ 14/20.** The Part XIII Section 3 signed eval report turned into a product surface. Bet #1 buyer-side advisory.
5. **(7, J + M convergence) — Trajectory-grade enablement coaching — OCQ 13/20.** Watch the AE's procurement-seam work, not the call surface. Solves the 7-month ramp-curve problem. Adjacent to Bet #1 (coach on procurement-gauntlet handling).

---

## 6. Top 3 challenges

1. **Ironclad / LinkSquares / SpotDraft April 2026 roadmap commits to "AI vendor playbook templates"** — direct competitor to Bet #1's clause-library module. **Severity 4 / Probability 4 / Alex exposure 4 / Bet-coverage 5 = Challenge score 17/20.** Mitigation: publish the open Playbook in 90 days, before any vendor ships the bundle. The Playbook's advisory wedge is harder for an incumbent to copy than the clause library is.
2. **Vanta / Drata / Secureframe shipping "AI Trust Center 2.0" with eval-reproducibility before Q4 2026** would close the SaaS-productization branch of Bet #1. **Severity 5 / Probability 3 / Alex exposure 4 / Bet-coverage 5 = 17/20.** Vanta's Q4 2025 AI Trust Center announcement is the leading indicator; watch for Q3 2026 product releases.
3. **The enablement-AI category (cells 7A–7M) is saturated with Highspot/Seismic/MindTickle/Showpad incumbents.** **Severity 3 / Probability 5 / Alex exposure 2 / Bet-coverage 2 = 12/20.** Low Alex exposure because Alex isn't betting in enablement, but worth monitoring if the J+M trajectory-coaching convergence creates a defensible new entrant that erodes deal-desk training adjacencies.

---

## 7. Top 3 open questions

1. **Does EU AI Act Article 14 human-oversight enforcement guidance (April 2026 draft) become teeth or paper tiger by late 2026?** Decidability: first Commission enforcement actions late 2026. Asymmetry: huge — teeth makes Bet #1 a $10B+ advisory category; paper keeps it niche but defensible. Bet-size implication: 5x range on Bet #1 TAM. Time-window narrowing rate: high (decidable within 6 months). **OQ score 18/20.**
2. **Does OSWorld 65% cross on a frontier system in Q3 2026 (Crux C3)?** If yes, deal-desk computer-use agents (9, K) become deployable for narrow procurement-portal driving — Coupa/Ariba/Workday Procurement automation. Asymmetry: opens an entire new product category 1-2 quarters earlier than this volume assumes. Bet implication: accelerates Bet #1 advisory modules around CU-readiness; opens a new Bet #3 advisory line on procurement-portal automation. **OQ score 16/20.**
3. **Does any of Ironclad / LinkSquares / SpotDraft / Vanta / Drata ship a credible agent-vendor procurement bundle (clause library + evidence pack + Article 14 tie-out) before Q4 2026?** Decidability: ~6 months via product roadmap public commitments + GA dates. Asymmetry: closes the productization branch of Bet #1; advisory branch survives but is repriced. Time-window narrowing: high (the next 1-2 quarters of product roadmap statements decide it). **OQ score 17/20.**

---

*End C3. Word count approximately 3,000 incl. dedicated §4. The (9, G) cell is Alex's procurement-seam through-line; the Playbook anchors here.*
