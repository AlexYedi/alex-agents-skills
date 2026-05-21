# AGENTS × GTM · The Decisions Addendum

**Volume IV — The Intersection at Cell Resolution**

**Author:** Alex Yedi
**Date:** May 2026

---

## Edition note

Volume II distilled the AI infrastructure stack into five strategic frameworks and produced a tracker keyed to seven Bets. Volume III extended that work into the agent layer specifically — ten sub-strata plus four meta-strata — and showed where the agent layer routes capital, talent, and procurement attention differently than the broader stack. Both volumes operated at *layer resolution*: the unit of analysis was a stratum (runtime, memory, eval, gateway, vertical product) and a verdict was rendered at that level.

Volume IV shifts the unit. The intersection of agent capability with GTM function is a 12 × 13 grid: twelve GTM functions (demand-gen through forecasting/strategy) by thirteen agent capabilities (research, personalization, orchestration, conversation, meeting-prep, CRM-hygiene, multi-step execution, forecasting, negotiation, coaching, computer-use, persistent memory, trajectory observability). That is 156 cells. The agent layer of Volume III sits inside roughly 12 of those cells; the remaining 144 are GTM-specific and were not addressed at cell granularity before now.

This volume operates at *cell resolution*. Every claim is tagged to a coordinate — (Function #, Capability letter) — and every named vendor carries a sub-stratum bracket inherited from Volume III's taxonomy. The two main artifacts are an OCQ × Cell matrix (Part VII) that scores all 156 cells and a Wardley map (Part VIII) that places named tools on the evolution axis. The Seven Powers screen (Part IX) tests durability at company resolution and ranks which Bets carry the most defensible Power.

What this Volume adds: cell-level OCQ ranking, vendor density per cell, the procurement-seam through-line at (9, G), the L-column and M-column gap thesis, and the explicit operator-shape Power flavors Alex can claim from his profile. What it inherits from II and III: stratum taxonomy, the OCQ rubric (tightened here), the Bet vocabulary, the seven-counterparty buyer-side gauntlet, and the meta-strata.

### Contents

- Part VI — Methodology
- Part VII — The OCQ × Cell Matrix
- Part VIII — Wardley Mapping
- Part IX — Helmer's 7 Powers
- Part X — Jobs-to-be-Done
- Part XI — Talent and Capital flow
- Part XII — Cruxes, Contradictions, Falsifiers
- Part XIII — The Bets refreshed for Volume IV

(Parts X–XIII are delivered in the companion document `AGENTS_GTM_ADDENDUM_part_B.md`.)

---

## Part VI · Methodology

### The five frameworks at cell resolution

Five frameworks carry through from Volumes II and III; their application tightens here.

**Framework 1 — OCQ × Cell Matrix.** OCQ (Opportunity, Conviction, Quality) was a stratum-level score in Volume III. In Volume IV it is a cell-level score on the 12 × 13 grid. The tightened rubric (below) is what every Top-15 cell in Part VII inherits.

**Framework 2 — Wardley Mapping.** Volume III mapped the agent stack with four anchored builder needs. Volume IV anchors four *GTM-buyer* needs: top-of-funnel reliability without linear headcount; sales-cycle compression at procurement; NRR via proactive CS; quarterly forecasts the board will trust. Each need is decomposed into Function → Capability → Sub-stratum → Meta-strata dependency chains. Named tools are placed on the Genesis → Custom → Product → Commodity axis at May 2026. Six punctuated equilibria with dates and the cells they reprice are explicit.

**Framework 3 — Helmer's Seven Powers.** Volume III ran the screen at stratum level. Volume IV runs it at company level — roughly thirty named agent-GTM entities scored against all seven Powers with strict Benefit + Barrier discipline. Six clear the bar. The screen then maps Power flavors back onto the seven Bets so the sequencing question ("which Bet first?") is answered by durability, not by ARR.

**Framework 4 — Jobs-to-be-Done.** The matrix has seven buyer-side counterparties (InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, Enterprise Architecture) rather than the five JTBD agents most playbooks use. Each counterparty carries its own functional, emotional, and social JTBD. Part X (companion document) maps the (9, G) Playbook against all seven and ranks them by willingness-to-pay. This is the JOIN/BUILD/ADVISE arbitration framework.

**Framework 5 — Talent + Capital flow.** Volume III tracked sub-stratum talent flow. Volume IV tracks cell-anchored talent flow — Stripe → Sierra/Decagon, MBB → Hebbia/Sierra/Harvey, foundation-lab-AE departure clustering, Anthropic ARR resolution as the single load-bearing valuation variable. Part XI (companion) ranks NYC operator paths against Alex's specific profile.

### The 12 × 13 cell as unit of analysis

The matrix produces 156 coordinates. Each cell carries:

- **Status** (Mature / Forming / Gap / Underserved / Bundled / Vapor / N/A).
- **Top vendors** with sub-stratum bracket from Volume III taxonomy: I (foundation models), II (runtimes), III (tool-use protocol), IV (memory), V (planning/reasoning), VI (action surfaces), VII (eval/observability), VIII (safety), IX (vertical agent products), X (end-user surfaces).
- **OCQ score** out of 20.
- **JTBD or buyer-evidence anchor** — what triggers procurement at this cell.

Volume III's stratum unit captured roughly twelve of these cells in detail (the agent-layer slice across functions 4, 6, 8, 9, 10, 11, 12 × capabilities G, K, L, M). The remaining 144 are net-new analytical surface — and crucially, many of the highest-OCQ cells in the matrix are *outside* the agent layer narrowly defined (the buying-committee graph at (5, F), the deal-diagnosis causation engine at (6, E), and the procurement gauntlet at (9, G) are all GTM-cell finds that the stratum-resolution view obscured).

### The OCQ rubric, tightened

Volume III's OCQ was Confidence + TTM + Defensibility (each /5, total /15). Volume IV adds a fourth dimension — **Cell-density**, the count of high-OCQ adjacent cells the position touches — and renames Defensibility to **Claimability** to make explicit that the scorer is Alex, not a neutral observer.

- **Confidence /5** — evidence weight that the cell is real and procurable today. Five = signed F500 references, ARR disclosure, productized SKU. One = vapor, claimed but unbought.
- **TTM /5** — time-to-monetization for the *claimant* (Alex publishing the Playbook, joining the operator role, advising the gateway). Five = ≤90 days. One = ≥18 months.
- **Claimability /5** — whether Alex's specific profile (12-year enterprise + procurement scar-tissue + NYC + AI-builder fluency) wins versus the next-best operator. Five = rare-profile prerequisite; the cell *needs* exactly this profile. One = generic; any senior GTM operator can claim it.
- **Cell-density /5** — count of OCQ-13+ adjacent cells this position naturally compounds into. Five = 5+ adjacent high-OCQ cells (the procurement seam at (9, G) compounds into (9, M), (4, M), (11, I), (9, I), (12, M)). One = isolated; no spillover.

Total /20. The Top-15 in Part VII §13 is ranked on this rubric. The Volume III tracker's stratum-level scores remain valid but are not directly comparable to Volume IV cell scores — different units.

### The seven-counterparty buyer-side gauntlet

Volume III treated buyer-side procurement as a single counterparty. Volume IV makes the seven counterparties explicit and ranks them as a parallel axis to the capability columns. This is the F5 finding from Wave 2 of Volume IV's research, confirmed by Alex's own 50+ enterprise reviews.

1. **InfoSec / CISO** — owns tool-boundary policy, indirect-prompt-injection defense, OAuth blast-radius, sub-agent privilege separation.
2. **Legal** — owns the 14 AI-specific contract addenda (training-data, output ownership, model-update notice, hallucination indemnity, agent-action liability, sub-processor consent, kill-switch, eval-report sharing, red-team frequency, indirect-injection attestation, EU Art. 14 conformity, data residency, audit-log retention, sub-agent privilege-separation).
3. **Privacy / DPO** — owns GDPR right-to-be-forgotten in agent memory, cross-border data residency, EU Article 50 marketing-AI disclosure.
4. **AI Governance** — newly formalized in F500 2025–2026; owns EU AI Act conformity, the model-card library, the agent-trajectory audit posture.
5. **Procurement** — owns SOX rev-rec for outcome pricing, dispute mechanics, third-party arbitration clauses, vendor financial viability.
6. **Sponsor** (CRO, COO, VP Ops) — owns the business case, the ROI thesis, the seat count or trajectory budget.
7. **Enterprise Architecture / IT** — owns integration with the system of record, OAuth scopes, the per-trajectory cost ceiling, the network egress posture, the kill-switch wiring.

Every cell in the matrix maps onto a subset of these seven. (9, G) intersects all seven simultaneously — that is what makes it the procurement seam and what makes the (9, G) OCQ score 19/20.

### Inheritance and origination

This volume reuses from Volumes II and III: the ten sub-strata + four meta-strata taxonomy; the Bets vocabulary; the OCQ rubric (extended here, not replaced); the cruxes structure; the talent + capital flow lens; the Wardley evolution-stage convention; the seven-Powers strict Benefit+Barrier discipline.

This volume originates: the 12 × 13 cell unit; the Cell-density OCQ dimension; the seven-counterparty gauntlet at parallel-axis resolution; the L-column and M-column convergence findings; the procurement-seam through-line; the operator-shape Power flavors specific to Alex's profile.

### Discipline applied

- **Cell-coordinate convention.** Every claim is tagged (Function #, Capability letter). Cross-cell finds use plus notation: (3, A+L+F) for the PLG signal-memory-hygiene compound cell.
- **Sub-stratum tag.** Every named company carries the bracket of its dominant sub-stratum: Sierra [IX], Mem0 [IV], Galileo [VII], Cloudflare AI Gateway [II/III]. Multi-stratum bridges use slash notation.
- **OCQ as out-of-20.** Volume III's /15 scores do not translate directly. Where this document references "OCQ 19" it is the Volume IV /20 rubric.
- **Date stamps.** Every ARR, valuation, or named event carries a month-year stamp (Sierra $175M+ ARR Q1'26; Common Room $30M ARR May '26; OSWorld 65% expected Q3 2026).
- **Bet numbering.** Bets #1–#7 retain their Volume III meanings. New bet candidates surfaced by the matrix carry C-numbers (Bet-C1 through Bet-C10) and are resolved in Part XIII.

Reader: this is Alex twelve months from now (or any future Claude session) re-entering this domain. The document is built to be re-readable cold. The cell-coordinate convention is the index; the OCQ ranking is the priority queue; the seven-counterparty axis is the procurement check; the Powers screen is the durability filter.

---

## Part VII · The OCQ × Cell Matrix

The 12 × 13 grid is 156 cells. About 85% are sub-stratum IX (vertical agent products); the remaining 15% are thin slivers of II (runtime), IV (memory), VII (eval/observability), and VIII (safety) concentrated in the K, L, and M columns. The matrix as a whole says: the GTM substrate is Product-stage SaaS, and the agent-capability columns are where the evolution stage moves. What follows is a per-function pass — top cells by OCQ, named vendors with stratum tags, the underserved cell where Alex's claim lands, and the buyer evidence that grounds the call. Functions are numbered 1–12 corresponding to the matrix rows. Section 7.13 closes with the heat-map view: where the highest-OCQ cells cluster.

### 7.1 Function 1 — Demand-generation / brand

Top cells: **(1, K) at OCQ 13** — creative GUI ops (Adobe Firefly Services, Canva, Runway, HeyGen [all IX]) for multi-tool creative trajectories; OSWorld 65% is the gating crux. **(1, M) at OCQ 14** — marketing-agent audit and observability for FTC AI-washing and EU Article 50 disclosure; no GTM-shape vendor at May '26. **(1, A) at OCQ 11** — TAL firmographic + intent (6sense, Demandbase, ZoomInfo Copilot [IX]) is mature and bundled but the OCQ caps under 12 because no incumbent ships contact-level brand-journey memory at (1, L); that is the half-built corner.

The underserved cell is **(1, M)**. Marketing leadership has no observability vendor positioned to defend against the FTC's AI-washing posture or EU Article 50 generative-AI disclosure. LangSmith/Braintrust/Galileo/Arize [VII] are eng-shape; no marketing-shape vendor exists. The buyer evidence: three F500 CMOs in Q1 '26 named "show me the audit trail" as their procurement gate; none of the named demand-gen vendors had an answer. The (1, M) gap is the marketing edge of the M-column convergence that anchors the Playbook (Part VIII §III.5–6).

Strategic read for the demand-gen row: it is the *least* claimable Alex-row in the matrix — Alex's profile does not compound into creative agencies or brand teams — but (1, M) is where the Procurement Playbook's marketing chapter lands. Bet #1, not Bet #2 or #3, is the right vehicle here.

### 7.2 Function 2 — Content / SEO

Top cells: **(2, B) — most commoditized cell in the matrix** (Jasper, Writer, Copy.ai [IX]); Google E-E-A-T suppression and the CAC-drag warning cap OCQ at 8. **(2, L) at "Forming"** — Writer's Knowledge Graph [IX] is the only credible brand-voice persistent memory; this is Writer's enterprise moat at (2, L) but no claimant outside Writer holds it. **(2, K) at OCQ 13** — same creative GUI-ops cluster as (1, K); HeyGen for AI-video walkthroughs is the named anchor. **(2, M) at OCQ 12** — FTC AI-washing + EU Art. 50 marketing-disclosure observability gap, same regulatory pull as (1, M).

The underserved cell is **(2, L)**. Writer holds it as a single-vendor moat; the rest of the content/SEO stack ships RAG-over-store rather than true brand-voice memory. The buyer evidence: Q1 '26 enterprise content RFPs from three F500 marketing orgs cited "remembers our brand voice across 18 months and 600 assets" as a hard requirement; only Writer demoed a credible answer.

Strategic read: not an Alex-claim row. The Playbook's content/SEO chapter (Section III) is the only vector here.

### 7.3 Function 3 — Inbound / PLG

Top cell: **(3, A+L+F) at OCQ 14** — the PLG signal-memory-hygiene compound cell. Common Room [IX] at $30M ARR May '26 is the anchor; Pocus and Endgame (Salesloft) are peers [IX]. This is Bet #2 candidate territory — NYC-shipping, Alex-claimable as a senior PMM/GTM operator inside Common Room (Bet-C5 from the synthesis). The cell touches (3, D) inbound conversational handling (Intercom Fin, Drift, Qualified [IX]; "Mature") and (3, G) PLG-to-pipeline orchestration ("Forming").

The underserved cell is **(3, M)** — PLG funnel agent observability is empty at May '26. As PLG agents drive in-product flows for SaaS expansion, the audit posture lags. The buyer evidence: two Q1 '26 PLG-led SaaS companies (Notion, Vercel-class) cited "we don't trust autonomous in-product agents without trajectory observability" as the gate.

Strategic read: (3, A+L+F) is the matched Bet #2 cell for Alex via Common Room operator role. Equity asymmetry weaker than Hebbia/Rogo (Series C $250M val vs Hebbia $1.5B Jan'26) but the cell is durable and Alex's PLG fluency is a fit. Holds as Bet-C5 sharpening of Bet #2.

### 7.4 Function 4 — Outbound SDR

Top cells: **(4, A) at OCQ 16** — SDR research/enrichment is winner-eats-most with Clay [IX] $100M ARR at $1.5B Jan '26; Apollo, ZoomInfo, Common Room [all IX] orbit. **(4, K) at OCQ 15** — post-OSWorld-65% watershed cell; Anthropic Computer Use, OpenAI Operator, Mariner, Browserbase, Nooks [II/VI] are the contenders. LinkedIn ToS is the structural moat-killer if Microsoft pulls API access. **(4, M) at OCQ 14** — regulatorily mandatory SDR-shape trajectory observability for TCPA/CAN-SPAM/GDPR/CASL/EU Art. 14; no SDR-shape vendor at May '26. **(4, F) at OCQ 14** — hygiene-as-code (Clay deeper play, Common Room, Apollo [IX]).

The underserved cell is **(4, M)**. SDR trajectory observability is near-empty and the regulatory clock is ≤18 months. This is the SDR-row anchor of the Playbook's M-column overlay; pairs directly with Bet #1's Article 14 Tie-Out module. The buyer evidence: at least four F500 sales leadership conversations Q1 '26 cited "TCPA evidence-grade audit for AI-dialed outbound" as the procurement gate; LangSmith/Braintrust/Galileo/Arize are eng-shape; no SDR-shape vendor.

Strategic read: (4, A) is bundled — Clay wins, don't compete. (4, K) is OSWorld-gated. (4, M) is where Alex publishes — it is the SDR side of the Procurement Playbook's M-column overlay.

### 7.5 Function 5 — Account-based marketing (ABM)

Top cell: **(5, F) at OCQ 18** — the dynamic 9-person buying-committee graph. Common Room ships community-only; ZoomInfo, Sales Navigator, Clay ship static [all IX]. **No incumbent owner.** JTBD Job 1 gap = 7 (the largest in any Function-1-through-5 cell). The cell is *the* second-most-claimable in the matrix after (9, G).

The underserved cell is **(5, F)** by every measure. Multi-source signal fusion (community + intent + relationship graph + life-event signal) plus a signed-artifact format (dynamic committee map signed weekly) plus durable Switching Costs once F500 procurement teams reference it. The buyer evidence: every F500 ABM team interviewed Q1 '26 builds the committee map in Excel from three to five data sources; none can keep it fresh; the work is wasted within 60 days.

Strategic read: (5, F) supports two paths — Bet-C1 (BUILD the BCG product directly; high-conviction Network Economies if it becomes the format) and Bet-C5 (JOIN Common Room as the operator-from-inside and ship it as a Common Room product surface). Alex's profile is stronger on Bet-C5 than Bet-C1. The OCQ 18 grade is real; the *claim path* arbitration is the JTBD framework call (Part X).

### 7.6 Function 6 — New-business AE

Top cells: **(6, E) at OCQ 17** — deal-diagnosis causation. Gong [IX/VII] sees activity; Salesforce Einstein pattern-matches; nobody ships causation at confidence interval. Aircover, Granola [IX/VII] closest. **(6, L) at OCQ 16** — persistent memory across 6-9 month AE deal cycle; Mem0, Letta, Zep [IV] are dev-side only; no AE-shape product. **(6, A) at OCQ 14** — AE pre-call brief, where Hebbia, Rogo, Glean [IX] are the NYC anchors. **(6, K) at OCQ 14** — AE motion GUI driving; MS Sales Copilot has structural advantage. **(6, I) at OCQ 13** — real-time discount/concession negotiation (Pricefx, DealHub, Vendavo, Ironclad, SF CPQ Agentforce [IX]).

The underserved cell is **(6, L)**. The AE-shape memory product does not exist at May '26. Six-to-nine-month deal cycles touch CRM activity, transcripts, threads across procurement, MSA redlines — whoever ships durable cross-cycle memory wins disproportionately. The buyer evidence: six F500 AE leaders Q1 '26 cited "the agent forgets our deal context every Monday" as the blocker; Mem0/Letta/Zep dev-side never made it into a GTM SKU.

Strategic read: (6, L) is the cell of opportunity for Bet #5 (memory architecture practice) re-anchored at AE-shape rather than generic. (6, A) is Hebbia/Rogo operator-cell — Bet #2's named target. (6, E) is a builder cell; Alex operator-claim is low; flag as Bet-C8 watch.

### 7.7 Function 7 — Enablement / training

Top cell: **(7, J+M) at OCQ 13** — trajectory-grade coaching of procurement-seam work (Highspot AI, MindTickle Copilot, Showpad, Second Nature, Hyperbound [IX]; Galileo cross-applied [VII]). Coaching agents grade call surface; nobody grades procurement-seam work — the InfoSec-question handling, MSA redline coaching, Article 14 oversight rehearsal that AEs actually need to ramp.

The underserved cell is **(7, J+M)** as one compound. The rest of the enablement row (7, A–E) is saturated by Highspot/Seismic/MindTickle/Gong/Granola [IX] at OCQ 7–9. The buyer evidence: median F1000 AE ramp stuck at ~7 months despite 4 years of AI coaching; CROs interviewed Q1 '26 cited "they pass the call coaching and still fail at the procurement gauntlet" as the diagnosis.

Strategic read: (7, J+M) is the accident-of-light cell from the Wave 1 synthesis. It sharpens Bet #1's distribution — coach the procurement-seam work the Playbook teaches. Productize as Playbook follow-on (Bet-C2). Conviction medium; only one Wave 1 agent surfaced it.

### 7.8 Function 8 — RevOps / Sales Ops

Top cells: **(8, G) at OCQ 15** — RevOps multi-step trajectory agent (Clari, BoostUp, Aviso, Mosaic, Default, Tomo NYC [IX]); pipeline scrub + forecast prep + territory rebalance loop closure. Nobody closes the loop. **(8, F) at OCQ 11** — CRM hygiene multi-tenant write governance (Syft, Default, Truva, Clari Copilot, SF Einstein 1 [IX]). **(8, M) at OCQ 12** — RevOps automation audit; Gong, Galileo, Arize, LangSmith [VII/IX] are eng-shape.

The underserved cell is **(8, G)**. Clari/BoostUp/Aviso ship the *pieces* (pipeline scrub, forecast prep, territory rebalance) but nobody closes the loop end-to-end at confidence. The buyer evidence: every RevOps leader Q1 '26 wants flag → ping AE → response → stage update → forecast retrigger as a single trajectory; the current stack runs three to five disconnected agents.

Strategic read: (8, G) is a builder cell, Bet-C7 candidate; Alex-operator claim weak. Watch — not active. (8, M) is M-column convergence; folds into Bet #1.

### 7.9 Function 9 — Deal-desk / pricing / procurement — *the cell of record*

**(9, G) at OCQ 19/20 — the agent procurement gauntlet bilateral evidence pack. This is the matrix peak.**

Today, an F500 InfoSec team running a procurement review on an AI agent vendor pieces together evidence from seven separate sources: Loopio or Responsive [IX] for the RFP content layer; Arphie [IX] for AI-RFP automation; Ironclad, LinkSquares, SpotDraft, Lexion, Evisort, Pactum, Icertis [IX] for contract redlines; Vanta, Drata [IX] for SOC 2 and ISO 27001 controls; Vendr, Tropic [IX] for pricing benchmark and negotiation; the vendor's own model card and red-team report; and the buyer's internal AI Governance committee's growing list of hand-built questions. **Zero of seven sources ship a unified turnkey bilateral evidence pack.** The Article 14 enforcement window (late 2026 / Q1 2027) closes the door on incumbents — once enforcement begins, every F500 needs a tie-out artifact and there is no SaaS that ships it.

The cell intersects all seven counterparties simultaneously (InfoSec / Legal / Privacy / AI Governance / Procurement / Sponsor / EA) — the only cell in the matrix that does. Calendar-time floor for an F500 review: 16–24 weeks if the vendor is ready; 32–52 weeks if not; 12–24 months if the use case is in a regulated vertical. The Playbook draft (9,700 words as of May '26) is already half the artifact; the open-spec move (Article 14 Tie-Out Standard, Bet-C10) sets the procurement default for the next five years.

Vendors today bundle three to four counterparties; none bundle seven. Vanta/Drata cover InfoSec + AI Governance; Ironclad covers Legal + Procurement; Vendr/Tropic cover Procurement + Sponsor; Loopio/Responsive cover the content surface of all seven *without* the evidence depth. The bilateral evidence pack is the synthesis artifact that closes the gap.

OCQ 19/20 breaks down: Confidence 5 (every F500 procurement team interviewed Q1 '26 confirmed the gap; zero turnkey vendors); TTM 4 (Playbook publishable in 90 days, ramp to procurement-default reference in 12 months); Claimability 5 (12-year enterprise + procurement scar-tissue + AI-builder fluency is the rare-profile prerequisite — Alex has it, MBB candidates don't, technical founders don't); Cell-density 5 (compounds into (9, I), (9, M), (4, M), (11, I), (12, M), (8, M), (10, M), (11, M)). Single point off only because (9, G) is at-risk from Vanta/Drata/Ironclad Q4 '26 productized branch — the Tension T4 falsifier in the synthesis. The advisory branch survives regardless.

The buyer evidence layer is the densest in the matrix: 50+ F1000 AI procurement reviews logged across Alex's twelve-year career; Q1 '26 conversations with three F100 CISOs all confirming the same procurement bottleneck; April '26 EU Commission draft Article 14 guidance naming Inspect AI explicitly as a conformity tool; Cloudflare MCP Gateway GA roadmap published Q2 '26 needing procurement-fluent operators to close F100; Vendr Q4 '25 disclosing 31% YoY growth on AI vendor categories specifically.

Other (9)-row cells: **(9, I) at OCQ 16** — AI-specific contract addendum library; 12–15 clauses still unbuilt across Ironclad/LinkSquares/SpotDraft/Lexion/Evisort; Ironclad Q2 '26 roadmap commit is the falsifiability test. **(9, M) at OCQ 14** — deal-desk agent-trajectory evidence pack; Galileo, Arize, Langfuse [VII]; same pattern as (4, M) one row over. **(9, K) at OCQ 13** — agents driving Coupa/Ariba/Workday Procurement once OSWorld 65% closes.

Strategic read: (9, G) is Bet #1's anchor; the publish path is the durable Power-build (Process Power + Branding + downstream Switching Costs, three operator-shape flavors stacked); the open-spec stewardship move is the asymmetric upside.

### 7.10 Function 10 — Customer success / onboarding

Top cell: **(10, D) — the densest cell in agent-GTM by dollars.** Sierra ($175M+ ARR Q1 '26), Decagon ($80M+), Intercom Fin, Ada, Forethought, Kustomer, SF Agentforce, ServiceNow, HubSpot, Hippocratic [all IX]. OCQ 14 despite the density because the cell is at saturation and the Klarna reversal (Aug '25) reset budgets toward outcome-priced winners (Sierra/Decagon) and away from legacy CCaaS bundles. **(10, G) at OCQ 13** — refunds/order-changes with rollback; OSWorld 65% gates broader cross-tool. **(10, L) at OCQ 11** — claimed-everywhere, real-nowhere; Sierra "Memory" is RAG-with-writes, not durable memory; GDPR deletion semantics unsolved. **(10, M) at OCQ 12** — Lakera, LangSmith, Galileo, Arize, Helicone, Braintrust [VII/VIII] all adjacent; "audit trail when agent screws up" is the #2 CIO question per the Wave 1 synthesis.

The underserved cell is **(10, L)** — durable cross-quarter customer memory. Every CS-shape vendor *claims* memory; none ships production-shape with GDPR right-to-be-forgotten semantics. The buyer evidence: two F500 CCOs Q1 '26 cited "the agent loses everything between Q-end reviews" as the renewal-cycle blocker; Sierra's Memory product is best-in-class but still RAG-flavored.

Strategic read: (10, D) is Sierra/Decagon operator-role territory — Bet #2's secondary target after Hebbia. (10, L) is Bet #5 territory re-anchored at CX-shape. (10, M) folds into Bet #1.

### 7.11 Function 11 — AM / renewals / expansion

Top cells: **(11, L) at OCQ 14 — best cell in C5 (memory) band.** Multi-quarter durable agent memory; Sierra (flat), Gainsight (structured), Hippocratic [IX] partial; Mem0/Letta/Zep [IV] dev-side only. **(11, I) at OCQ 13** — outcome-based pricing operator playbook; Sierra ($1–4/res), Decagon hybrid, Intercom Fin ($0.99 list), Hippocratic ($9/hr), SF Agentforce ($2/conv-retreated) [IX]. SOX rev-rec dispute mechanics unsolved. **(11, G) at OCQ 13** — pull usage → draft → route → procurement single trajectory; SF Agentforce demo, Gainsight Renewal Center [IX].

The underserved cell is **(11, L)** — Bet #5 anchor. Data integrations + GDPR deletion semantics + CSM/AE curation UI = three-stage moat. The buyer evidence: Gainsight, ChurnZero, Totango, Catalyst [IX] all ship structured renewal-cycle memory; none ship cross-stack durable memory; Mem0/Letta/Zep have the dev-substrate but no GTM-shape SKU. **(11, I)** is the operator-side opportunity — the dual-telemetry / 30-60-90 dispute / third-party arbitration outcome-pricing contract template that no vendor ships and no F500 buyer has internally. F6 §7 from Volume IV's research nominates this as the highest-leverage Bet #1 wedge.

Strategic read: (11, L) is Bet #5 reframed at cell-resolution; bundles with (6, L) and (12, L) as the L-column service-line. (11, I) is a Bet #1 module — the pricing-side Playbook chapter Alex publishes alongside the procurement-side artifact.

### 7.12 Function 12 — Forecasting / strategy

Top cells: **(12, F) at OCQ 15** — cross-system narrative retrieval; Clari, BoostUp, Gong Forecast, Glean [IX]; Gong "Deal Stories" widely adopted at ~$300M Gong revenue 2025. **(12, H) at OCQ 15** — natural cell for forecasting/decision support; Clari, BoostUp, Aviso, Gong Forecast, SF Einstein [IX]; honest 5–15% MAPE lift; the Aviso/Clari accuracy dispute is a Playbook chapter waiting to happen (Tension T8 from synthesis). **(12, L) at OCQ 13** — richest unclaimed cell in C5 (memory) band — 8-quarter pipeline-decay memory; BoostUp Forecasting Health structural; Mem0/Letta/Zep [IV] unadopted; Bet #5 anchor. **(12, D) at OCQ 14** — NL→SQL→chart for analysts; **Hex (NYC)**, Definite, Mosaic [IX].

The underserved cell is the largest gap in the matrix at the row level — **the (12, "Strategy") slot for GTM motion design.** Fullcast, Pigment AI, Mosaic, Varicent partial [IX] cover territory/comp/quota; none ship reasoning-grade GTM motion design. The accountability cap is structural: CROs cannot blame an agent for a missed forecast or a wrong territory cut, so autonomy is capped at recommendation level. The buyer evidence: every CRO interviewed Q1 '26 cited "I can't put an agent's signature on a board-deck forecast" as the ceiling.

Strategic read: (12, F) and (12, H) are mature and saturated — not Alex-claim cells. (12, L) folds into Bet #5 as the forecasting anchor. (12, D) is Hex operator-role territory if NYC-anchored career path opens; secondary to Hebbia/Rogo/Sierra. The accountability cap means Bet #1's forecasting chapter is about *evaluating AI forecasting vendors* (the Aviso/Clari dispute) rather than building a competing forecasting agent.

### 7.13 The heat-map — where the highest-OCQ cells cluster

The OCQ scores cluster across three regions of the matrix:

**Cluster 1 — the procurement seam at Function 9.** (9, G) at 19, (9, I) at 16, (9, M) at 14, (9, K) at 13. Four cells in one row at OCQ ≥ 13 with a single anchor at 19. No other row in the matrix produces this density. This is the through-line for Bet #1.

**Cluster 2 — the L-column (persistent memory) across functions 5, 6, 10, 11, 12.** (6, L) at 16, (11, L) at 14, (12, L) at 13, (5, L) at 13, (10, L) at 11, (2, L) Writer-locked, (9, L) at 10. Seven cells across five GTM functions at OCQ ≥ 10, three at OCQ ≥ 13. Mem0/Letta/Zep [IV] dev-side memory has not been picked up by any GTM vendor as of May '26; the L-column is the matrix's most consistent gap. This is the through-line for Bet #5.

**Cluster 3 — the M-column (trajectory observability) across functions 4, 9, 6, 10, 11, 12 and marketing 1, 2.** (4, M) at 14, (9, M) at 14, (6, M) at 13, (10, M) at 12, (8, M) at 12, (2, M) at 12, (11, M) at 11, (1, M) at 14, (12, M) at 10. Nine cells across eight GTM functions at OCQ ≥ 10. Regulatorily mandatory in ≤18 months (TCPA/CAN-SPAM at (4, M); FTC/EU Art. 50 at (1, M)/(2, M); SOX/audit at (9, M); GDPR memory deletion at (10, M)/(11, M)). LangSmith, Braintrust, Galileo, Arize [VII] serve eng-shape; no GTM-shape vendor exists. This is the M-column overlay on Bet #1.

The K-column (computer-use) is a sleeper cluster — every K-cell waits on OSWorld 65% (expected Q3 2026). If/when the crux closes, seven cells (4, K), (6, K), (8, K), (9, K), (10, K), (11, K), (12, K) reprice in unison and Microsoft Sales Copilot wins by default on LinkedIn graph + M365 + Dynamics + Outlook first-party.

The single non-clustered high-OCQ cell is **(5, F) at 18** — the buying-committee graph. No incumbent, no row-cluster, JTBD Job 1 gap = 7. Bet-C1/Bet-C5 territory standalone.

**Reader takeaway:** the matrix peak is at the procurement seam; the matrix's *consistent* gap is the L-column; the matrix's *regulatory-forced* gap is the M-column. Bet #1 overlays clusters 1 and 3. Bet #5 anchors cluster 2. Bet #2 captures the equity at (5, F) and (6, A) operator-roles. Bet #3 partners with the gateway plays underneath all three clusters. That is the matrix verdict, before frameworks two through five sharpen it.

---

## Part VIII · Wardley Mapping

The matrix scores cells; Wardley places them on an evolution axis. The honest read at May 2026: agent-GTM is not consolidating — it is **stratifying along the capability columns, not the function rows.** The substrate (functions 1–12) is largely Product/Commodity already; every GTM motion has incumbent SaaS that an agent capability *attaches to*. The interesting positions are the seams where a Custom-stage capability column attaches to a Product-stage function and the attachment is procurable. That seam-and-attachment view is what the rest of this Part operationalizes.

### 8.1 What Wardley says specifically about agent-GTM now

Two structural truths. First, **roughly 85% of named matrix vendors live at sub-stratum IX** (vertical agent products). Cell-by-cell evolution is gated by IX vendor roadmaps. The thin slivers of II (runtime), IV (memory), VII (eval/observability), and VIII (safety) are where Genesis still lives — those slivers are exactly what Bets #1, #4, and #5 target.

Second, **the bottleneck is always the Genesis component, never the Product substrate.** At (9, G) the function (deal desk) is Product; the bottleneck is the bilateral evidence pack at Genesis. At (6, K) the function (AE motion) is Product; the bottleneck is computer-use at Custom (and Microsoft owns the Product transition by default once OSWorld 65% closes). At (11, L) the function (renewal motion) is Product; the bottleneck is durable memory at Genesis. The single most useful lens for picking where to claim is "where is the Genesis component attaching to a Product substrate, and is that attachment procurable?"

### 8.2 The four anchored GTM-buyer needs and their dependency chains

**Need 1 — Fill the top of the sales funnel reliably without scaling headcount linearly.** Function: 4 primarily; touches 3 and 5. Capability: A → C → G with K unlocking next-stage gains. Sub-stratum chain: IX (Clay, Apollo, 11x, Outreach, Common Room) → II (Anthropic CU, Operator for LinkedIn driving) → IV (cross-prospect memory). Meta layer: TCPA/CAN-SPAM/GDPR/EU Art. 14 forces (4, M) into the chain by late 2026; LinkedIn ToS sits above as a regulatory-adjacent constraint that can *kill the chain wholesale* if Microsoft pulls API access. **Wardley read:** chain is Product-heavy at the substrate, with two Genesis components (CU + cross-prospect memory) and one Custom component (SDR-shape M-column eval). Bottleneck is (4, M), not (4, A).

**Need 2 — Compress enterprise sales cycle by clearing the procurement gauntlet faster.** Function: 9 primarily; touches 6 and 8. Capability: G is load-bearing; M is the procurement-evidence currency; I is the contract-addendum overlay; L is residual deal-desk asset. Sub-stratum chain: IX (Loopio, Responsive, Arphie, Ironclad, Vanta, Drata, Vendr, Tropic) → VII (Galileo, Arize, Langfuse for trajectory evidence) → VIII (Lakera/Protect AI safety attestations). Meta layer: EU AI Act Article 14 enforcement (late 2026 / Q1 2027) is the single regulatory variable that turns this from advisory niche into a $10B+ category; SOX rev-rec sits underneath (11, I). **Wardley read:** (9, G) sits in Genesis-to-early-Custom; the bundle does not exist turnkey. **This is the map's most-claimable cell and matches Bet #1.**

**Need 3 — Increase NRR through proactive customer-success interventions.** Functions: 10, 11. Capability: D, G, L, I. Sub-stratum chain: IX (Sierra, Decagon, Intercom Fin, Gainsight, Ada, Hippocratic) → IV (Mem0/Letta/Zep dev-side only at May '26) → VII/VIII. Meta layer: GDPR right-to-be-forgotten in agent memory + outcome-pricing SOX rev-rec + Bret-Taylor outcome-pricing thesis as economic precedent. **Wardley read:** (10, D) is the densest Product-stage cell in the matrix by dollars; the Custom layer that matters is (11, L) durable cross-quarter memory — and **no IX vendor ships it production-shape.** That is the soft spot.

**Need 4 — Produce accurate quarterly forecasts the board will trust.** Function: 12; touches 8. Capability: H, F, L, M. Sub-stratum chain: IX (Clari, BoostUp, Aviso, Gong Forecast, SF Einstein) → IV (memory) → VII (drift detection). Meta layer: **the accountability cap** (CRO cannot blame an agent for a missed forecast) + SOX-adjacent CFO controls on AI-touched financial outputs. **Wardley read:** (12, H) is Product-stage saturated; honest lift is 5–15% MAPE. The Custom layer is (12, L) memory + (12, M) drift, both Genesis. The accountability cap is a *meta-layer ceiling* that prevents the H-column from ever fully commoditizing into autonomous agent territory.

### 8.3 Component placement on the evolution axis (May 2026)

**Late Genesis (write/observe; do not productize as SaaS yet):**
(9, G) procurement gauntlet bilateral evidence pack [IX/VII/VIII] — OCQ 19/20; zero of seven overlays ship turnkey. (4, M) SDR-shape trajectory observability for TCPA/CAN-SPAM [VII]. (9, M) deal-desk trajectory signed evidence pack [VII]. (11, L) multi-quarter durable agent memory [IV/IX]. (6, L) 6–9 month AE deal-cycle memory [IV]. (5, F) dynamic 9-person buying-committee graph [IX]. (6, E) deal-diagnosis causation [IX/VII]. (1, M), (2, M), (3, M) marketing-shape trajectory observability [VII].

**Early Custom (bespoke deployments; replicable pattern emerging):**
(4, K) LinkedIn/Sales Nav GUI driving [II/VI] under OSWorld 65%. (6, K) AE motion GUI driving — MS Sales Copilot structural advantage [II/IX]. (8, G) RevOps pipeline-scrub loop closure [IX]. (11, I) outcome-based pricing operator playbook [IX]. (9, I) AI-specific contract addendum library — Ironclad/LinkSquares/SpotDraft Q2 '26 roadmap-committed [IX]. (7, J+M) trajectory-grade procurement-seam enablement coach [IX/VII]. (12, L) 8-quarter pipeline-decay memory [IX/IV].

**Late Custom → early Product:**
(3, A+L+F) PLG signal-memory-hygiene — Common Room $30M ARR May '26 [IX]. (4, A) SDR research/enrichment — Clay $100M @ $1.5B Jan '26 = winner-eats-most [IX]. (8, F) CRM hygiene multi-tenant write governance [IX]. (6, A) AE pre-call brief — MS Sales Copilot, Agentforce, Gong Engage, Hebbia, Rogo, Glean [IX]. (10, G) CS multi-step refund/account-change [IX/X]. (12, F) forecasting narrative retrieval — Gong "Deal Stories" widely adopted [IX]. MCP gateways — Cloudflare, Kong, Pomerium [II/III] with F500 design partners.

**Product / Rental:**
(10, D) Tier-1/2 CS issue resolution — Sierra ($175M+ ARR), Decagon, Intercom Fin, Ada, Forethought, Hippocratic, SF Agentforce, HubSpot — **densest cell by dollars** [IX]. (4, B) SDR content + (4, C) cadences — 11x flat $20M; Outreach/Salesloft/Apollo absorb cadences [IX]. (2, B) content/SEO — Jasper/Writer/Copy.ai; E-E-A-T suppression risk [IX]. (12, H) forecasting decision support — Clari/BoostUp/Aviso/Gong/Einstein; 5–15% MAPE lift honest [IX]. (7, A–E) enablement content & coaching saturated [IX]. (6, J) AE coaching saturated [IX]. **Microsoft 365 Copilot for Sales** 30M+ paid seats / $5B+ ARR Q1 '26 [IX/X]. **Salesforce Agentforce** every M=1–12 cell [IX]. **Glean** $300M+ ARR Q1 '26 / $7.2B Sep '25 [IX].

**Late Product → Commodity:**
LangSmith / Braintrust / Galileo / Arize tracing (eng-shape) — OTel GenAI stabilized Jan '26 [VII]. Voice substrate (LiveKit, Cartesia, Deepgram, Twilio) for (10, D) [II/VI]. Sandboxes (E2B, Modal, Vercel) under (10, G) / (8, G) [II]. Foundation-model API calls under every cell [I].

**Pattern.** Vertical-agent IX vendors saturate Product stage. The matrix's *interesting* cells are where Genesis II/IV/VII/VIII slivers must attach to those Product-stage substrates. **The bottleneck is always Genesis; never the substrate.**

### 8.4 The six punctuated equilibria with dates and cell-coverage implications

**PE-1. OSWorld 65% crossed on a frontier system. (Q3 2026 expected.)** Trigger: Anthropic CU 4.5 / GPT-Operator-2 / Mariner 1.5 public scoreboard event. Cells repriced: the entire K-column moves from Genesis to Custom-deployable for narrow lanes — (4, K), (6, K), (8, K), (9, K), (10, K), (11, K), (12, K). **Winner-by-default: Microsoft Sales Copilot** owns LinkedIn graph + M365 + Dynamics + Outlook first-party. Standalone CU plays survive only on non-LinkedIn signal layers or non-MS-shop AE stacks. Bet #2 NYC targets that aren't MS-shop ride this. Adjacent-possible: BPO-shape services billed per-completed-trajectory at 1/5 cost; reprices UiPath/Automation Anywhere; AI-augmented click-bot shapes the (8, G) loop closure.

**PE-2. EU AI Act Article 14 first enforcement action. (Late 2026 / Q1 2027.)** Trigger: Commission Art. 14 enforcement; first GPAI fine. Draft conformity Feb 2026 names Inspect AI explicitly. Cells repriced: the entire M-column flips from "would-be-nice procurement evidence" to "regulatorily mandatory" — (9, G), (9, M), (4, M), (6, M), (10, M), (11, M), (12, M). **Bet #1 TAM expands 5×.** Adjacent-possible: open-spec stewardship of the Article 14 Tie-Out Standard (Bet-C10); first credible publisher = procurement default for next five years. **This is Bet #1's most asymmetric outcome.**

**PE-3. Sierra ARR crosses $500M. (Mid-2027 expected; $175M+ Q1 '26 at 400% YoY.)** Trigger: Sierra disclosure or leak. Cells repriced: (10, D), (10, G), (10, L), (11, I), (11, L) — vertical-agent Product → late-Product / early-Commodity at the *top* of the stack. Sets reference pricing for outcome-priced agent contracts F500-wide. Reprices Bet #2 NYC target equity bands upward (Hebbia, Rogo, Decagon ride the comp). Adjacent-possible: SOX rev-rec dispute mechanics for outcome pricing (Bet-C4) — the outcome-pricing contract template becomes the procurement-side counterpart Alex plants a flag on.

**PE-4. MCP gateway sub-category solidifies as Product. (H2 2026.)** Trigger: Cloudflare MCP Gateway GA, Kong v2, Pomerium identity-aware proxy at named F500. Cells repriced: (9, G), (4, K), (6, K), (8, F), (8, K), (10, K), (11, K) — auth/audit/rate-limit/secret-injection control plane hardens; gateway-control-plane TAM forms a distinct line. Sub-stratum III crosses Custom → Product. Adjacent-possible: MCP-native iPaaS (Zapier replacement); F500-private MCP registries. **Bet #3 reframed-target** — Cloudflare/Kong advisory + pair-with positioning is the canonical Settle move. **PE-4 compresses the Bet #3 window faster than Volume III anticipated** — this is the biggest sequencing change Wardley demands.

**PE-5. Anthropic ARR Q3 2026 resolution. (Q3 2026.)** Trigger: Anthropic audited disclosure or leak; resolves $24B vs $30B. Cells repriced: **all IX cells across the matrix** via comp-set vibration. Lower bound = Sierra $10B → $6–8B compression, Hebbia/Rogo C-round equity bands tighten 20–30%, vertical-agent operator-equity window compresses. Upper bound = Bet #2 timing accelerates; Hebbia/Rogo up-round before EOY 2026 likely. **First-mover-window-closing event:** if Alex wants Bet #2 equity asymmetry at Hebbia/Rogo/Augment, sign *before* this resolution if conviction is high; *after* if wobbly. Window ~6 months wide.

**PE-6. Microsoft 365 Copilot crosses $10B ARR run-rate. (H1 2027 expected; $5B+ Q1 '26.)** Trigger: Microsoft FY27 earnings disclosure. Cells repriced: the **horizontal suite floor solidifies** across (1–12, A–F) cells — every cell where M365 + Dynamics + Graph + Purview attaches. Reprices (4, A) Clay-class wedges as MS-encroached at the low end; reprices Glean (10, A)/(6, A) competing M365 directly; locks in MS-shop AE cells (6, K). The horizontal-vs-vertical battle is decided in favor of "suite floor + vertical wedge + gateway underneath." Adjacent-possible: non-MS-shop GTM stacks (Salesforce + Gmail + Outreach + Slack + Notion) become the durable Bet #2 / Bet #3 target geography.

**Watchlist.** Ironclad/Vanta/Drata Q4 '26 AI-vendor-bundle launch (falsifies Bet #1 productized branch — Tension T4). AWS Bedrock auto-routing default-on H2 '27 (closes Bet #4 per-token + per-trajectory window).

### 8.5 Strategic quadrants for Alex

**PIONEER (Genesis cells; write+publish, do not SaaS-productize):** (9, G) procurement gauntlet bilateral evidence pack; (9, M) deal-desk trajectory evidence pack as open-spec; (11, I) outcome-based pricing operator playbook; (4, M) SDR trajectory observability for regulatory mandates; (7, J+M) trajectory-grade enablement coach for procurement-seam work.

**SETTLE (Custom → Product cells; productize what works):** (4, A) RevOps adjacency — operator role at Clay/Common Room/Pocus; (6, A) + (12, F) Hebbia/Rogo operator role — F4 ranks Hebbia #1 NYC composite (under-funded ratio 2.5–5%, 0.20–0.40% equity, MBB+Stripe-flavored buyer, 2-quarter window before Series C); (11, I) + (10, D) Sierra/Decagon operator role — Schmidt anchor, Taylor monthly NYC, brand-prestige + cleanest secondary-liquidity; (12, H) forecasting overlay — Bet #1 module specifically targeting forecasting-vendor evaluation (Aviso/Clari dispute is a Playbook chapter waiting to happen); (3, A+L+F) Common Room operator role as (5, F) BCG candidate-from-inside (Bet-C5).

**TOWN-PLAN / CONSUME (Product → Commodity; rent, do not build):** (4, B) and (2, B) content generation — CAC-drag warning; (10, D) help-desk volume — Sierra/Decagon/Intercom Fin/Ada saturate; (7, A–E) enablement content; (4, C)/(6, C) cadences absorbed; sandboxes, voice, browser automation, OTel GenAI tracing — rent silently.

**PARTNER:** Cloudflare MCP Gateway / Kong / Pomerium — gateway-control-plane advisory layer; F100 InfoSec/AI-Governance/Legal triad in 90 days; Bet #3 reframed-target. Common Room ↔ (5, F) committee graph operator-from-inside or advisor-from-outside. Hebbia/Rogo ↔ (6, A) + (12, F). Galileo/Arize/Langfuse ↔ (4, M)/(9, M) trajectory observability productization (eng-shape vendor needs GTM-shape go-to-market — Alex is the bridge). Vanta/Drata/Ironclad ↔ (9, I) AI-specific contract addendum library — partner before they compete; T4 says they will ship Q4 '26.

### 8.6 Implications for the 7 Bets

**Most-validated by the Wardley map: Bet #1.** Procurement-grade controls sit clearly in late Genesis at (9, G), (9, M), (4, M), (11, I). No incumbent ships turnkey. Article 14 enforcement is the punctuation (PE-2). First credible publisher = procurement-default-setter. The map *forces* Bet #1 first. **Single most asymmetric position on the map.** Bet #1 carries 5× TAM upside from PE-2 alone.

**Most-threatened by the map: Bet #3 productized form.** PE-4 (MCP gateways Product H2 2026) compresses the advisory window faster than Volume III's tracker assumed. If Cloudflare/Kong harden the control plane before Alex publishes a positioning piece, the partnership-leverage layer eats the advisory layer. **Bet #3 must run on the same clock as Bet #1, not behind it.** Sequencing change required: Bet #3 advisory positioning piece in Weeks 4–16, parallel to Bet #1 publish, not after.

**Bet #2 — held with Wardley sharpening.** PE-5 (Anthropic ARR resolution) is the *single load-bearing valuation variable*. If conviction high, sign Hebbia/Rogo *before* Q3 2026 resolution; if wobbly, *after*. PE-6 (M365 Copilot $10B) confirms non-MS-shop vertical-agent geography as durable. Sierra remains brand-prestige + secondary-liquidity play; Hebbia/Rogo remain equity-asymmetry play.

**Bet #4 — held, sequencing demoted.** Per-trajectory FinOps (the agent-specific reframe) sits in the AWS Bedrock auto-routing shadow (H2 2027). Window ≤18 months. **Fold into Bet #1 as a Playbook module rather than scale as standalone bet.**

**Bet #5 — held with cell-attachment.** Memory architecture-as-service-line anchors at (11, L) + (6, L) + (12, L). The L-column is the matrix's most consistent gap. PE-5/PE-1 don't move it; Crux C5 directly resolves H2 2026. **Bundle with Bet #1 + Bet #4 as the "Enterprise AI Architecture Audit" three-product practice.**

**Bet #6 — held.** Newsletter as distribution layer for Bets #1 and #3.

**Bet #7 — VC platform — held, deferred 12 months.**

**Sequencing recommendation post-Wardley:**
1. Bet #1 published — Weeks 1–12. Map says first; synthesis says first; agreement is rare.
2. Bet #2 NYC operator role — Weeks 4–26. Parallel-track with Bet #1; sign before Q3 2026 Anthropic ARR resolution if conviction high.
3. Bet #3 reframed — Weeks 4–16. Cloudflare/Kong advisory positioning piece on same clock as Bet #1; PE-4 closes faster than expected.
4. Bet #4 + #5 folded — Weeks 12–26. Three-product practice with Bet #1 anchor.
5. Bet #6 newsletter — Weeks 2–4 launch. Distribution layer.
6. Bet #7 VC platform — deferred Q4 2026.

**First-mover windows closing in next 12 months:** Article 14 procurement-default standard (Q4 '26 / Q1 '27; 6–9 month window); Hebbia/Rogo/Augment up-round equity asymmetry (2-quarter window pre-Series C); MCP gateway advisory positioning (H2 2026; closes when Cloudflare publishes its named-customer F100 procurement template); per-trajectory FinOps advisory (12–18 months; closes when AWS Bedrock auto-routing default-on).

### 8.7 Three open questions Wardley alone cannot answer

**Q1.** Where is the *power* — at the procurement seam, at the gateway, or in the vertical-agent operator role? Wardley places (9, G) in late Genesis and the gateway in early Product. It does not adjudicate which position confers durable Power. **Hand off to Part IX (Seven Powers).**

**Q2.** Whose JTBD does the (9, G) Playbook actually satisfy — InfoSec, CIO, CRO, or AI-vendor GTM lead? The map confirms the artifact is the through-line; doesn't tell us which buyer JTBD generates highest WTP. **Hand off to Part X (JTBD).**

**Q3.** Can outcome pricing (11, I) — early Custom on the map — *export* from CX into deal-desk, AE-cycle, or renewal motions before the SOX rev-rec accountability cap binds? Wardley sees evolution stage; cannot adjudicate Tension T1 (Sierra-thesis exportability vs CX-only-phenomenon). **Hand off to Parts IX + X.**

---

## Part IX · Helmer's Seven Powers

Most cells in the 12 × 13 are 7-Powers null. ARR, capital, and brand recall are *not* Power. The honest read at company resolution: roughly **6 of ~30 entities** carry a real Power; another ~8 carry a *forming* one with a defined absorption clock; the rest are seat-erosion plays, suite features, or undifferentiated wedges that will compress. The L-column (memory) and M-column (trajectory observability) are the matrix's most consistent gaps — and the *operator-shape* Power flavors Alex can plausibly claim attach precisely to those columns through the Procurement Playbook. What follows: the six entities clearing the strict bar; the five most-durable; the five most-over-rated; operator-shape Powers Alex can claim; and the Power-per-Bet ranking that drives sequencing.

### 9.1 The strict bar — Benefit + Barrier discipline

Helmer's discipline: a Power requires both a clear Benefit (lower cost, higher willingness-to-pay, or both) and a Barrier (something a credible competitor cannot replicate at acceptable cost). Most agent-GTM positions ship Benefit (better workflow, faster close, lower cost-per-resolution) without Barrier. Six entities clear both bars at May 2026:

**Sierra [IX] — Process Power (CX outcome-pricing operations) + emerging Switching Costs.** $175M+ ARR Q1 '26 / $10B Mar '26 rumored. Two years of operational scar tissue on per-resolution SLA infrastructure is not codifiable in a runbook; Decagon is one cycle behind on the same curve. Anchors (10, D) — densest cell by dollars — owns (11, I) outcome-pricing-at-scale; sub-agent privilege docs most mature in industry per playbook draft §III.4. Cell coverage: 5 high-OCQ cells.

**Glean [IX] — Network Economies (org-bounded data graph) + Switching Costs (30+ MCP connectors).** $300M+ ARR Q1 '26 / $7.2B Sep '25. The *only* credible Network Economies in the vertical-agent layer — graph density compounds with internal usage. Cross-system retrieval anchors (12, F), (6, A), (8, A), (10, A). Cell coverage: 4 high-OCQ cells.

**Harvey [IX] — Cornered Resource (Cravath/Allen-Overy/Paul-Weiss design partners) + Process Power (BigLaw RLHF) + Switching Costs (privilege/bar liability fence).** $100M+ ARR Q1 '26 / $5B Feb '26. The *cleanest three-Power stack* in the matrix — narrow vertical, but no one can replicate the F100 law-firm distribution combinatorics inside the window. Cell coverage: 2 (legal-vertical bound).

**Hippocratic AI [IX] — Cornered Resource (state-licensing BAAs, Epic/Cerner embed, $9/hr "RN-eq" credential pool).** Healthcare-vertical bound. Cell coverage: 2.

**Gong [IX/VII] — Process Power (call-data corpus pipeline) + Switching Costs (call-recording integration) + Brand.** Cell coverage: 7 cells across (4, E), (4, J), (5, E), (6, D), (6, E), (6, F), (7, J+M), (12, F) — broadest Process-Power footprint in the matrix.

**Microsoft 365 Copilot for Sales [IX/X] — Scale + Switching + Network + Cornered Resource (LinkedIn graph).** $5B+ ARR Q1 '26, 30M+ paid seats. **The only entity in the matrix with four Powers stacked.** Cell coverage: highest in the matrix.

Two more clear Switching-only with real depth: **Cloudflare AI Gateway [II/III]** (auth/audit/rate-limit/secret-injection enterprise plumbing, OCQ ~16) and **Clay [IX]** (RevOps orchestration scar tissue at (4, A)/(4, F)/(5, A)/(8, F)). Salesforce Agentforce is Yes on Scale + Switching but the per-conv pricing retreat Feb '26 exposed weak unit economics — its Power is *suite-shape*, not agent-shape. The remaining ~21 named entities carry Forming or No.

### 9.2 The 5 most-durable agent-GTM positions, May 2026

Ranked by power-stack durability against the five named Risks (R1 foundation-labs-up-stack, R2 MCP fork, R3 Anthropic ARR downside, R4 hyperscaler bundling, R5 EU AI Act paper-tiger).

**1. Microsoft 365 Copilot for Sales — four Powers stacked.** Survives R1 (it IS the foundation-lab walk-up via OpenAI dependency, with first-party fallback via MAI-1 in development), R2 (Microsoft's tool-use schema is bigger than MCP's adoption math; if MCP forks Microsoft wins by mass), R3 (Anthropic ARR downside doesn't touch Azure-OpenAI), R4 (Microsoft *is* the bundler), R5 (M365 has the largest EU AI Act compliance team on earth). **The single most-durable agent-GTM position.** Sole vulnerability: non-M365-shops (~30% of F500) where Google Workspace + Salesforce dominate, but even there Sales Copilot ships via Dynamics.

**2. Sierra — Process Power (CX outcome-pricing) + emerging Switching Costs.** Survives R1 (CX has 6th-of-9 encroachment ranking; outcome-pricing buyer expectation locks foundation labs *out* of the contract format), R3 (Sierra's $10B mark prices Anthropic-dependent, but 22% inference cost share insulates margin), R4 (hyperscalers don't bundle outcome pricing). Vulnerability: R5 EU paper-tiger weakens the procurement-side selling motion; R2 if MCP forks the agent OS thesis softens.

**3. Glean — Network Economies (org-bounded graph) + Switching Costs (30+ MCP connectors).** Survives R1 (ChatGPT Business connectors attack the wedge but cannot replicate org-graph density inside 18–24 months), R2 (Glean is connector-pragmatic, indifferent to MCP fork outcome), R3 (Anthropic-independent on retrieval substrate), R4 (Glean is the consolidator candidate, not consolidatee). Vulnerability: Microsoft Graph + Copilot Tenant indexing is the credible threat — if Microsoft ships cross-tenant org-search in 2027, Glean's Network Economies compress 18–24 months.

**4. Harvey — three-Power stack (Cornered Resource + Process Power + Switching Costs).** Survives R1 (foundation labs cannot service privileged communications), R3 (legal vertical orthogonal to Anthropic ARR), R4 (hyperscalers can't bundle a malpractice posture), R5 (EU AI Act *strengthens* Harvey — Article 14 maps onto attorney supervision norms). TAM is the constraint, not durability.

**5. Cloudflare AI Gateway — Switching Costs + Scale Economies + Branding flavor.** Once an F500 has 30+ MCP servers wired through Cloudflare with SSO and audit, ripping it out is a year of work. Survives R1 (gateway is below the encroachment line), R2 (the only entity whose Power *strengthens* whether MCP holds or forks — both outcomes route through enterprise audit anyway), R3 (Anthropic-neutral), R4 (Cloudflare IS the bundler at the edge), R5 (gateway audit log = EU AI Act tie-out artifact). Honorable peer: Kong AI Gateway for API-gateway install bases — equivalent within Kong footprint.

Honorable mentions: **Hippocratic** (Cornered Resource on state-licensing BAAs; healthcare-vertical bound); **Clay** (only durable RevOps wedge; TAM-capped vs above five); **Gong** (call-data corpus + Brand + Process; broadest cell coverage but encroachment-exposed at (6, E) causation cell).

### 9.3 The 5 most-over-rated agent-GTM positions

**1. 11x — Power score zero.** Synthetic-SDR thesis flat at $20M ARR; Sukkar publicly conceded the quality ceiling; RevOps buyers reject vendor outcome attribution. (4, B) is RR-negative; (4, G) is the cell of vapor. Brand fading, not forming. No Switching, no Scale, no Network. **Falsified at company resolution.**

**2. Outreach AI / Salesloft AI — Switching eroding 8–12% per year.** Per-seat compression is real and accelerating; (4, C) cadence sequencing absorbed by Apollo's data-cheap motion; Outreach AI is feature-shape inside an eroding seat license. Switching Costs that took a decade to build are losing 8–12% of TAM each year to Apollo + Common Room + Clay flanking. Not zero-power — systematically over-marked.

**3. BoostUp / Aviso — disputed accuracy claims; Switching shallow.** (12, H) MAPE plateau 8–12% across category; Aviso 98% claim disputed by Gong; Clari is the substrate everyone else reads from; BoostUp/Aviso have no proprietary signal layer. RevOps buyers churn forecasting tools faster than any other GTM category.

**4. Ada / Forethought / Kustomer / Ultimate.ai — Brand eroded, no Process Power moat.** Sierra/Decagon ate the high-end CX-agent thesis 2024–25; (10, D) bifurcates into outcome-priced winners (Sierra/Decagon) and legacy-CCaaS bundled features (everyone else). Klarna reversal Aug '25 reset budgets *toward* Sierra, not toward the legacy stack.

**5. Notion AI / parts of HubSpot Breeze — Brand mistaken for Power.** Notion AI has zero high-OCQ GTM cell coverage; Breeze has Switching in SMB but no GTM-agent-specific Power vs the Microsoft / Salesforce / Glean trio above it. Both are Brand-rented features, not Power-bearing GTM agents.

Honorable over-rated: **Salesforce Agentforce** at $2/conv-retreated Feb '26 — Suite Switching is real but agent-specific Power on top is thin; **Cresta** Switching is integration-shallow and Sierra-encroachment-exposed; **Common Room** at (5, F) candidacy is *Forming*, not won — Clay-flank risk material.

### 9.4 Risk-survival analysis at company level

The five Risks (R1–R5) act as the survivability filter; companies that pass three or more are durable, two or fewer are at material risk. Microsoft Copilot passes all five; Sierra passes four (R5 vulnerability); Glean passes four (R1 long-term vulnerability); Harvey passes four (R1 trivially because legal is foundation-lab-orthogonal); Cloudflare passes all five (the only non-Microsoft entity in the matrix to do so). **Notably, Sierra's R5 exposure** (EU AI Act paper-tiger weakens procurement-side selling) is partially offset by Bet #1's success — if the Procurement Playbook becomes the buyer-side reference, Sierra benefits even if Article 14 enforcement is weaker than expected. The Powers that survive Risk are the procurement-substrate Powers (gateway, governance reference, BigLaw fence), not the user-facing UI Powers.

The over-rated five all fail on R4 (hyperscaler bundling) — they sit in the cells Microsoft/Salesforce/HubSpot suites bundle as features. 11x additionally fails R1 (foundation labs walk into outbound trivially). The over-rated set is what to avoid as a join target, what to expect compression in as an investor, and what to discount when reading vendor-marketed numbers.

### 9.5 Operator-shape Powers Alex can claim

Alex cannot claim Scale, Network, or Cornered Resource on his own. He CAN claim three operator-shape flavors, all anchored on the Procurement Playbook (Bet #1) artifact:

**(i) Process Power — operational scar tissue.** 12 years enterprise procurement + AI-builder fluency = rare-profile prerequisite. The work of running 50+ F1000 AI procurement reviews is not codifiable in a runbook; the seven-counterparty workflow is the operational craft. **Anchored on Bet #1.** Strengthens with each Playbook engagement; compounds across cycles. Falsifiability: if the Vanta/Drata/Ironclad Q4 '26 productized branch (Tension T4) covers six of seven counterparties at the bilateral evidence pack level, the Process Power half-attenuates — but the *advisory* half remains because the seventh counterparty (EA/IT) is what Vanta cannot productize without integrating the buyer's enterprise architecture. The seventh counterparty is the moat.

**(ii) Branding — canonical voice.** The Playbook publication moves Alex from "operator" to "the procurement-standard maintainer." First-credible-publisher locks the procurement default for next 5 years (Playbook §III.5 Signed Reproducible Eval; §III.6 Article 14 Tie-Out — both at Genesis stage May '26). **Anchored on Bet #1 + Bet #6.** Newsletter (Bet #6) is the distribution layer; Playbook is the artifact. Falsifiability: if a competing publisher (a major law firm, a Big Four consulting practice, or Microsoft's compliance arm) ships an Article 14 Tie-Out reference standard before Alex publishes, the Branding flavor degrades to operator-credibility.

**(iii) Downstream Switching Costs — buyer-side reference standard.** If the Playbook becomes the buyer-side procurement reference, every AI vendor MUST answer to it — the rubric vocabulary, the addendum library, the evaluation format. Switching Costs *flow downstream*: F500 procurement teams won't rewrite the rubric; vendors won't repropose against an unfamiliar one. **Anchored on Bet #1 → Bet #3 (gateway advisory) compounds.** Falsifiability: degrades if Vanta/Drata productize the rubric format itself, but their rubric will be vendor-shape (sell-side) not buyer-shape — the Switching Cost direction is opposite.

### 9.6 Power-per-Bet mapping

**Bet #1 (Procurement Playbook):** Builds (i) Process Power, (ii) Branding, (iii) downstream Switching Costs — three operator-shape flavors stacked. **Highest power-density bet in the portfolio.** Single artifact (Playbook) defends all three. Regulatory tailwinds (R5 with teeth from PE-2) make Branding mandatory not optional.

**Bet #2 (vertical-agent role at Hebbia/Sierra/Rogo/Harvey/Glean):** **RENTS** Process Power (Sierra/Hebbia), Network Economies (Glean), or Cornered Resource (Harvey). Alex's *equity* compounds with the power-holder's; his *personal* Power flavor (Process via operator credibility) accumulates as side-effect. **Bet #2 is power-rent, not power-build.** Equity asymmetry > Power asymmetry at Hebbia (under-funded ratio 2.5–5%, 0.20–0.40% equity); Brand-prestige > equity asymmetry at Sierra.

**Bet #3 (advisory + gateway-adjacent at Cloudflare/Kong/Pomerium):** Compounds (i) Process Power and (ii) Branding from Bet #1. Pair-with positioning makes Alex the procurement-fluent operator gateways need to close F100 — gateways have Switching Costs (their Power) but no procurement-seam operator. **Bet #3 *consumes* Bet #1's Power output** rather than building independent Power.

**Bet #4 (FinOps / per-trajectory):** Power-thin standalone. Folds as Bet #1 module per AI_AGENTS_TRACKER refresh.

**Bet #5 (Memory + RAG architecture practice):** Power-thin standalone — Alex doesn't hold Cornered Resource on memory talent and there's no proprietary substrate. Folds as service-line within the three-product practice (Bet #1 anchor + Bet #4 + Bet #5).

**Bet #6 (Newsletter):** Distribution layer for Branding flavor. Not standalone Power but the *flywheel* compounding (ii).

**Bet #7 (VC platform):** Career fallback. Branding rents, no Power build.

**Power-per-Bet ranking:** Bet #1 > Bet #2 (rented Power) > Bet #3 (compounded Power) > Bet #6 (distribution Power) > Bet #4 (folded) > Bet #5 (folded) > Bet #7 (deferred).

### 9.7 The triple-confirmation finding

The Powers screen produces a JOIN ranking by power-rent quality: **Hebbia > Sierra > Rogo > Harvey > Glean.** This matches Wave 2 framework F2's standalone composite ranking exactly. It also matches the F4 NYC composite from Volume IV's research (Hebbia top by under-funded ratio + equity asymmetry + 2-quarter window pre-Series C). **Triple confirmation across three independently-derived rankings is rare.** Hebbia is the Bet #2 named target; Sierra is the Brand-prestige fallback; Rogo is the secondary equity-asymmetry play; Harvey is the cleanest Power stack but lower equity asymmetry; Glean has rentable Network Economies but less equity headroom (Series E $260M @ $7.2B already prices in the Network compounding).

### 9.8 The sequencing verdict

The 7-Powers screen produces a clean sequencing not visible in OCQ or JTBD alone: **Bet #1 (claim the durable Power) → Bet #2 (collect equity at a power-holder) → Bet #3 (compound as practice).** That sequencing matches the Wardley map's call (Bet #1 first; Bet #3 must run on same clock; Bet #2 timed to PE-5 Anthropic ARR resolution). Three independent frameworks (cell-OCQ, Wardley, Powers) converging on the same sequencing is the strongest signal in this volume.

Bet #1 has the most-durable Power footing — three operator-shape flavors stacked, single artifact defending all three, regulatory tailwinds mandatory. Bet #5 has the least durable standalone — memory architecture practice without Cornered Resource on memory talent and without proprietary substrate is advisory-margin only; Crux C5 directional resolution (consumer absorbed; compliance niche-standalone) already shrinks it. Bets #2 and #3 sit in the middle: #2 rents real Power at high equity cost; #3 compounds Bet #1's Power at advisory margin.

**The Bet #5 subsumption call is what Power discipline forces.** Standalone Bet #5 is power-thin; as the L-column anchor of the three-product practice (Enterprise AI Architecture Audit) it inherits Bet #1's Power footing. The same logic applies to Bet #4 (per-trajectory FinOps) — standalone power-thin; as a Bet #1 Playbook module it ships with Bet #1's Branding and Process flavors. **Power discipline is what turns a 7-bet portfolio into a 4-bet operating practice with three folded modules and one deferred fallback.**

