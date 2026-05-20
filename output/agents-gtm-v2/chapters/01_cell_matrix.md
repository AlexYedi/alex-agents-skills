# Chapter 1 — The Cell Matrix

V1 mapped the AI stack into 18 strata, top to bottom, electrons to end-user. V3 zoomed Stratum XIII (agents) into 14 agent sub-strata, because the agent layer was the one band where the analytical resolution of V1 stopped being useful. V4 cuts further. The agent layer is what GTM functions actually consume; the consumption surface is the **function × capability cell**. Twelve GTM functions on the rows, thirteen agent capabilities on the columns, **156 cells in total**. Each cell carries a status (Mature, Forming, Gap, Saturated, Underserved, Convergence, or N/A), a top-vendor lineup, an OCQ score on a /20 scale (V4 widens the scale from V1's /15 — see Ch 6 §6.3.1 for the four-dimension rationale), and a JTBD anchor.

The reason for cell resolution is operational. At the stratum level, "vertical agent products" looks like one band (Stratum XIII in V1, sub-stratum IX in V3). Inside that band, Sierra at (10, D) — tier-1/tier-2 CS conversation handling at $175M+ ARR and outcome pricing — is a completely different competitive position from Hebbia at (6, A) — AE pre-call brief with vertical-data depth in finance. Every conversation Alex has with a buyer, a counterparty, or a portfolio company lands at a specific cell. The matrix is the conversation surface, not the field map.

Cell-coordinate notation is binding throughout the rest of this workbook. `(9, G)` means Function 9 (deal-desk / pricing / procurement) × Capability G (multi-step task execution). The seven counterparties of Bet #1 anchor at `(9, G)`; the buying-committee gap of Bet-C1 anchors at `(5, F)`; the deal-diagnosis gap surfaced by the Wave 1 synthesis anchors at `(6, E)`. Plate 1 (Cell Matrix Heatmap) is the visual key — cells shaded by OCQ score, top-15 outlined, the cell of record `(9, G)` distinct. Read top to bottom for a full pass; jump to a cell to refresh one node.

![Plate 1 — Cell Matrix Heatmap](plates/01_cell_matrix.svg)

## §1.1 The 12 GTM functions

### Function 1 — Demand-generation / brand

**Demand-gen / brand** owns top-of-funnel pipeline manufacture. Owner in a typical F1000 GTM org is the CMO with a Demand-gen VP underneath; binding metric is MQL volume at a defensible cost-per-MQL. The row at the matrix is **the most crowded and least defensible bucket in marketing**. Six cells are Mature — `(1, A)` TAL firmographic+intent (6sense, Demandbase, ZoomInfo Copilot [IX]), `(1, B)` personalization+content (Mutiny, Jasper, Movable Ink [IX]), `(1, D)` visitor-to-MQL conversation (Drift/Salesloft, Intercom Fin, Qualified [IX]) — and two are Gap. The two gaps that matter: `(1, K)` creative GUI ops at OCQ 13 (Adobe Firefly Services, Canva Magic Studio, Runway [IX]) — OSWorld 65% is the gating crux; and `(1, M)` marketing-agent observability at OCQ 14 — FTC AI-washing + EU Article 50 pull but no GTM-shape vendor exists at May 2026. Strategic read: not an Alex-claim row beyond Bet #1's marketing chapter at `(1, M)`. The CAC-drag warning at `(1, B)` is the credibility problem that the Procurement Playbook surfaces.

### Function 2 — Content / SEO

**Content / SEO** owns organic traffic and editorial supply. Owner is the Head of Content (CMO direct-report); binding metric is organic-traffic ROI net of Google E-E-A-T suppression. **`(2, B)` is the most commoditized cell in the matrix** — Jasper, Writer, Copy.ai [IX] saturate; Google's 2024–2025 Helpful Content + Core Updates demonstrably suppressed thin AI content in SERPs through 2025, so OCQ caps at 8. The interesting cell is `(2, L)` — brand-voice persistent memory. **Writer's Knowledge Graph [IX] is the only credible enterprise-shape implementation**, and that is Writer's $1.9B Series C narrative. Outside Writer, content vendors ship stateless RAG-over-store; that is the open vs absorbed crux. `(2, K)` creative GUI ops bundles with `(1, K)` — same OSWorld-gated cluster — at OCQ 13. `(2, M)` marketing-agent observability at OCQ 12 carries FTC + EU Art. 50 regulatory pull. Strategic read: not an Alex-claim row; the Playbook's content chapter is the only vector.

### Function 3 — Inbound / PLG

**Inbound / PLG** owns product-led pipeline — converting free-tier users and anonymous in-product visitors into qualified pipeline. Owner is the Head of Growth (often reports to CMO; sometimes to CRO in PLG-native orgs); binding metric is free-to-paid conversion and PQL-to-pipeline lift. The signature cell is **`(3, A+L+F)`** — the PLG signal-memory-hygiene compound — at **OCQ 14**, anchored by Common Room [IX] at $30M ARR May 2026, with Pocus and Endgame (Salesloft) as peers. This is a Bet #2 candidate cell (Bet-C5 promoted) — NYC-shipping, Series C $250M valuation, Alex-claimable via senior PMM/GTM operator role. `(3, D)` inbound conversation handling is mature (Intercom Fin's $100M+ ARR is the strongest single-cell datapoint in the bucket); `(3, G)` PLG-to-pipeline multi-step orchestration is forming. `(3, M)` PLG-funnel agent observability is empty — the audit posture lags as PLG agents drive in-product flows for SaaS expansion.

### Function 4 — Outbound SDR

**Outbound SDR** owns cold-pipeline manufacture against named-account lists. Owner is a Director-SDR reporting to the CRO or VP Sales; binding metric is meetings-booked per SDR per quarter and conversion to SQL. The row is **the densest, most-funded, most-exposed in the matrix**. Four cells score OCQ 14+. `(4, A)` SDR research/enrichment at OCQ 16 is winner-eats-most with Clay [IX] ($100M at $1.5B Jan 2026) and Apollo, ZoomInfo, Common Room [IX] orbiting. `(4, K)` computer-use in outbound at OCQ 15 is the post-OSWorld-65% watershed cell — Anthropic Computer Use, OpenAI Operator, Mariner, Browserbase, Nooks [II/VI] are the contenders, and LinkedIn TOS is the structural moat-killer. `(4, M)` SDR trajectory observability at OCQ 14 is regulatorily mandatory in ≤18 months (TCPA, CAN-SPAM, GDPR, CASL, EU Art. 14) but no SDR-shape vendor exists at May 2026 — direct Bet #1 module. `(4, F)` hygiene-as-code at OCQ 14 belongs to Clay's deeper play. The `(4, B)` content cell at OCQ 10 is the "synthetic SDR" ceiling — 11x flat $20M ARR Q1 2026 is the cautionary datapoint; reply rates on AI-generated cold are *worse* than human-templated at volume.

### Function 5 — Account-based marketing (ABM)

**ABM** owns named-account orchestration — coordinated marketing + sales activity against a list of target accounts. Owner is a Director-ABM reporting to CMO (sometimes co-owned with CRO); binding metric is target-account pipeline and target-account win rate. The row's signature is **`(5, F)` at OCQ 18 — the buying-committee mapping gap**, the second-most-claimable cell in the entire matrix. **No incumbent owner.** Common Room ships community-only signal; ZoomInfo and Sales Navigator ship static org charts; Clay ships waterfall enrichment. None ships the **dynamic 9-person buying-committee map updated weekly with intent + relationship + life-event signal in one signed artifact** (see §1.4 for the build sketch). JTBD Job 1 gap = 7. The rest of the row is either incumbent-locked (`(5, C)` Demandbase One, 6sense Revenue AI) or attribution-vapor (`(5, B)` Mutiny's 30–60% lift claims unverified). `(5, I)` and `(5, J)` are N/A — marketing doesn't negotiate or coach. `(5, K)` ABM platform UI driving is nascent; `(5, M)` is empty.

### Function 6 — New-business AE

**New-business AE** owns deal execution from qualified opportunity to signed contract. Owner is the CRO via VP Sales / Director New-Business; binding metric is win rate × ACV × cycle-time. **The row has three OCQ ≥14 cells, two of them deep in gap territory.** `(6, E)` deal-diagnosis causation at **OCQ 17** is the row's signature — Gong [IX/VII] sees activity, Salesforce Einstein pattern-matches deals that lost, Aircover scores deal momentum; **no vendor ships causation at confidence interval ("this deal stalled because X with 73% confidence")**. `(6, L)` persistent memory across the 6–9-month AE deal cycle at **OCQ 16** is the critical-gap cell — Mem0, Letta, Zep [IV] are dev-side only; no AE-shape product exists. `(6, A)` AE pre-call brief at OCQ 14 is where Microsoft Sales Copilot, Agentforce, Gong Engage, **Hebbia, Rogo, Glean [IX]** anchor — Hebbia and Rogo are NYC anchors for Bet #2. `(6, K)` AE motion GUI driving at OCQ 14 is the post-OSWorld-65% watershed for AE-side; Microsoft Sales Copilot has the structural advantage. `(6, I)` real-time discount/concession negotiation at OCQ 13 (Pricefx, DealHub, Vendavo, Ironclad, SF CPQ Agentforce) is under-served on the AE side.

### Function 7 — Enablement / training

**Enablement / training** owns rep-readiness — content libraries, certifications, coaching, and ramp curves. Owner is a VP Enablement (sometimes reports to CRO, sometimes to People); binding metric is time-to-ramp and quota-attainment lift. The row is **saturated** — Highspot AI, Seismic Aura, MindTickle Copilot, Showpad Coach [IX] all relaunched 2025 around AE coaching agents that watch Gong/Chorus. Cells `(7, A)` through `(7, E)` score OCQ 7–9 — commodity. The signature cell is **`(7, J+M)` at OCQ 13** — trajectory-grade coaching of procurement-seam work. Despite four years of "AI enablement," median F1000 AE ramp held at ~7 months in 2026. The diagnosis: coaching agents grade **surface activity** (talk-time ratio, filler-word frequency, discovery-question count) and not the **underlying buyer-counterparty work** that decides 6-figure deals — InfoSec questionnaires, MSA redlines, Article 14 oversight questions. `(7, J+M)` is the accident-of-light cell from Wave 1; it sharpens Bet #1's distribution (Bet-C2, absorbed).

### Function 8 — RevOps / Sales Ops

**RevOps** owns the data, tooling, and process spine of the GTM org — territory design, comp plan administration, forecast roll-up, CRM hygiene, pipeline scrub. Owner is a VP RevOps reporting to CRO or CFO; binding metric is forecast accuracy and pipeline-quality MAPE. The row's signature is **`(8, G)` RevOps multi-step trajectory agent at OCQ 15** — Clari, BoostUp, Aviso, Mosaic, Default, Tomo (NYC) [IX] ship the *pieces* (pipeline scrub, forecast prep, territory rebalance) but **nobody closes the loop end-to-end** (flag → ping AE → response → stage update → forecast retrigger). `(8, F)` CRM hygiene multi-tenant write governance at OCQ 11 (Syft, Default, Truva, Clari Copilot, SF Einstein 1) is the agentified RevOps job; the hard part is multi-tenant write-action governance for an agent that can mass-mutate CRM. `(8, M)` RevOps automation audit at OCQ 12 is the convergence cell — same problem as `(9, G)` action-rollback documentation; OpenTelemetry GenAI conventions (stabilized Jan 2026) are the substrate but no GTM-specific product wraps them. Strategic read: `(8, G)` is a builder cell (Bet-C7 candidate, watch-list); Alex-operator claim is weak.

### Function 9 — Deal-desk / pricing / procurement

**Deal-desk / pricing / procurement** is the cell of record row. It owns the seller-internal cost-to-close meeting the buyer-internal cost-to-buy. Owner on the seller side is a Director-Deal-Desk reporting to CRO or CFO; on the buyer side it is Procurement, Legal, InfoSec, AI Governance, Privacy, the business sponsor, and Enterprise Architecture / IT Ops — **seven counterparties at F1000 scale**. Binding metric is calendar-time-to-signature (16–24 weeks for ready F500 vendors; 32–52 weeks unprepared; 12–24 months in regulated verticals). **`(9, G)` scores OCQ 19/20 — the matrix peak**. The cell is the agent procurement gauntlet bilateral evidence pack: Loopio, Responsive, Arphie [IX] cover the RFP content surface; Ironclad AI, LinkSquares, SpotDraft, Lexion, Evisort, Pactum, Icertis [IX] cover contract redlines; Vanta, Drata, Secureframe [IX/VIII] cover SOC 2 / ISO 27001; Vendr, Tropic, Sastrify [IX] cover buyer-side procurement; **zero of seven sources ship a unified turnkey bilateral evidence pack** for agent-specific risk. The row carries three more OCQ ≥13 cells: `(9, I)` AI-specific contract addendum library at OCQ 16 — 12–15 clauses still unbuilt across Ironclad/LinkSquares/SpotDraft; Q2 2026 Ironclad roadmap is the falsifiability test. `(9, M)` deal-desk agent-trajectory evidence pack at OCQ 14 — Galileo, Arize, Langfuse [VII] serve eng-shape; no GTM-shape vendor. `(9, K)` agents driving Coupa/Ariba/Workday Procurement at OCQ 13 — OSWorld 65% gates. The row is the densest concentration of OCQ ≥13 cells in the matrix — four in one row — and the only cell that intersects all seven counterparties simultaneously is `(9, G)`. EU AI Act Article 14 enforcement (late 2026 / Q1 2027) is the punctuation that re-rates the entire row. The Playbook anchors here; the cell of record sits here; everything else in the matrix is read through this row's gravity.

### Function 10 — Customer success / onboarding

**Customer success / onboarding** owns post-sale activation, support, and tier-1/tier-2 conversation handling. Owner is the CCO via VP CS / VP Support; binding metric is gross retention, NPS, and ticket deflection rate. **`(10, D)` is the densest cell in agent-GTM by dollars** — Sierra ($175M+ ARR Q1 2026, $10B val), Decagon ($80M+ ARR at $4.5B), Intercom Fin ($100M+ ARR claimed 65% resolution rate), Ada, Forethought, Kustomer, SF Agentforce, ServiceNow, HubSpot, Hippocratic [IX] all saturate. OCQ caps at 14 despite the density because the cell is at saturation and the **Klarna reversal (Feb 2025)** reset budgets toward outcome-priced winners (Sierra, Decagon) and away from legacy CCaaS bundles. `(10, G)` multi-step refund/order-change with rollback at OCQ 13 — Sierra Agent OS, Decagon, SF Agentforce, Replit Agent [IX/X] — gates on OSWorld 65%. `(10, L)` per-customer durable memory at OCQ 11 is claimed-everywhere, real-nowhere — Sierra "Memory," Decagon "Knowledge," Hippocratic; RAG-over-store ≠ durable memory; GDPR right-to-be-forgotten in agent memory (ICO July 2025 guidance) is the live wire. `(10, M)` audit trail at OCQ 12 (Lakera, LangSmith, Galileo, Arize, Helicone, Braintrust [VII/VIII]) is the **#2 CIO procurement question after escalation-handoff**.

### Function 11 — AM / renewals / expansion

**AM / renewals / expansion** owns post-sale revenue — renewal cycles, expansion plays, NRR defense. Owner is the VP Customer Success / VP Account Management reporting to CCO or CRO; binding metric is net revenue retention. The row's signature is **`(11, L)` at OCQ 14 — the best cell in the L-column (memory) band** — multi-quarter durable agent memory across a 4-quarter renewal cycle. Sierra ships flat memory; Gainsight ships structured data not agentic memory; Hippocratic ships HIPAA-scoped healthcare-specific. The cross-quarter, cross-team, semantically-rich persistent memory needed for an 18-month renewal cycle **does not exist in any production CS agent today** — Mem0/Letta/Zep [IV] are dev-side only. Bet #5 anchors here. `(11, I)` outcome-based pricing operator playbook at OCQ 13 — Sierra ($1–4/resolution), Decagon (hybrid), Intercom Fin ($0.99 list), Hippocratic ($9/hour), SF Agentforce ($2/conv retreated Feb 2026) [IX] — has unsolved SOX rev-rec dispute mechanics. `(11, G)` pull usage → draft → route → procurement single trajectory at OCQ 13 is gap territory (Salesforce Agentforce demo, Gainsight Renewal Center). `(11, H)` Gainsight's home turf is weak — health-score → renewal-probability link is correlative not causal.

### Function 12 — Forecasting / strategy

**Forecasting / strategy** owns the CRO's instrument panel — quarter-by-quarter pipeline analytics, territory and quota planning, board prep, GTM-motion design. Owner is the CRO with RevOps and Strategic Finance below; binding metric is forecast MAPE and quota attainment. The row is **the most data-rich GTM function and the least agentic** — incumbents (Clari, BoostUp, Aviso, Gong Forecast, SF Einstein, InsightSquared, Outreach Commit) have spent five years bolting "AI" onto roll-up workflows as **prediction surfaces, not agents**. `(12, F)` cross-system narrative retrieval at OCQ 15 (Gong "Deal Stories" widely adopted at ~$300M Gong revenue 2025) and `(12, H)` decision support at OCQ 15 ($1.5B saturated category; honest 5–15% MAPE lift) are the natural cells. `(12, L)` 8-quarter pipeline-decay memory at OCQ 13 is the richest unclaimed cell in the column — BoostUp Forecasting Health partial, Mem0/Letta/Zep unadopted, Bet #5 anchor. `(12, D)` NL→SQL→chart for analysts at OCQ 14 is where Hex (NYC), Definite, Mosaic ship. The largest gap in the entire matrix at the row level is **the (12, "Strategy") slot for GTM motion design** — no agent meaningfully helps a CRO design a motion. The accountability cap is structural: **a CRO cannot put an agent's signature on a board-deck forecast or a wrong territory cut**, so autonomy is capped at recommendation level.

## §1.2 The 13 agent capabilities

### Capability A — Research / enrichment

**A** is the capability of pulling external data into agent context — firmographic, technographic, intent, news, person-level moves — and grounding it. It draws from V3's data sub-stratum (`9b`) and RAG sub-stratum (`9c`). Binding constraint: data freshness and source provenance. The Mature cells cluster at `(4, A)`, `(5, A)`, `(6, A)` — SDR/ABM/AE pre-call research is dense, commoditizing fast on the back of Clay (`(4, A)` $100M at $1.5B), Apollo, ZoomInfo Copilot, Common Room, Hebbia, Rogo, Glean. Almost every row carries a workable A cell; A is the column most likely to be a feature inside an incumbent suite rather than a standalone wedge. The two A cells where Alex-shaped claim survives are `(3, A+L+F)` (Common Room PLG signal) and `(6, A)` (Hebbia/Rogo vertical-data depth at finance).

### Capability B — Personalization + content

**B** is the capability of producing tailored content at scale — first-line copy, body content, account-specific landing pages, follow-up emails, MAPs, exec summaries. It draws on V3's model sub-strata and post-training fine-tunes for brand voice. Binding constraint: reply-rate / engagement-rate impact net of inbox-reputation decay. `(2, B)` is **the most commoditized cell in the matrix**; `(4, B)` is the synthetic-SDR ceiling (11x flat $20M ARR). The B column carries the matrix's clearest CAC-drag warning — at volume, AI cold reply rates are 0.6–1.2% vs 1.8–2.4% human-templated per 2025 Smartlead / Instantly meta-studies. The defensible position in the B column is brand-voice persistent memory (Writer at `(2, L)`), not raw generation.

### Capability C — Multi-channel orchestration

**C** is the capability of stitching email + LinkedIn + phone + SMS + ads + in-app into a single state-aware sequence on prospect signal. It draws on V3's orchestration sub-stratum. Binding constraint: cross-channel session continuity (shared state across modalities). The C column is **incumbent-owned across SDR/ABM/AE** — Outreach AI, Salesloft AI Cadences, Apollo, HubSpot Sales Hub AI, Agentforce, Reply.io absorb agentic features into seats. Standalone C plays have no space; the cell is forming only at `(1, C)` cross-channel brand-handoff (Optimove, Marketo Velocity orchestrate but don't reason).

### Capability D — Conversation handling

**D** is the capability of running a live, multi-turn dialogue — text, voice, multimodal — with tool-calling into systems of record. It draws on V3's runtime sub-stratum and voice-substrate sub-strata. Binding constraint: escalation-handoff governance (when does the agent ask for a human?) — the #1 CIO procurement question post-Klarna. **`(10, D)` is the densest cell in agent-GTM by dollars** — Sierra, Decagon, Intercom Fin, Ada, Forethought, Kustomer saturate. The D column also picks up `(3, D)` inbound conversational qualification (Intercom Fin $100M+ ARR) and `(6, D)` live AE-call assist (Cresta, Aircover, Gong Assist). Outside CX and inbound, D is shallow.

### Capability E — Meeting prep / listen / follow-up

**E** is the capability of pre-meeting brief assembly + in-meeting listen + post-meeting follow-up draft. It draws on V3's transcription sub-stratum and retrieval sub-stratum. Binding constraint: cross-tool handoff (SDR→AE, AE→CSM, CSM→AM) without context loss. The signature E cell is **`(6, E)` at OCQ 17 — deal-diagnosis causation** — Gong sees activity, no one ships causation. `(4, E)` is the under-served SDR→AE handoff seam (Granola, the only purpose-built handoff product, at ~$40M ARR Q1 2026 inferred). `(1, E)` is structurally N/A — brand has no meetings.

### Capability F — CRM hygiene / graph

**F** is the capability of keeping the system-of-record correct, complete, deduplicated, and current — accounts, contacts, opportunities, relationships, the buying-committee graph. It draws on V3's data sub-stratum and knowledge-graph sub-stratum. Binding constraint: multi-tenant write-action governance (an agent that can mass-mutate CRM needs audit + rollback). The signature F cell is **`(5, F)` at OCQ 18 — the buying-committee mapping gap** — no incumbent owner. `(4, F)` hygiene-as-code at OCQ 14 is Clay's deeper play; `(8, F)` RevOps CRM hygiene is agentified but governance-thin; `(12, F)` cross-system narrative retrieval at OCQ 15 is where Gong "Deal Stories" lives.

### Capability G — Multi-step task execution

**G** is the capability of running an end-to-end trajectory — multiple tool calls, multiple turns, multiple systems — with audit trail and reversibility. It draws on V3's planner, runtime, and tool-use sub-strata. Binding constraint: action-rollback documentation and sub-agent privilege separation — the procurement-side checks. **The G column concentrates value at the procurement seam**: `(9, G)` at 19, `(8, G)` at 15, `(11, G)` at 13, `(10, G)` at 13. G is also where vapor concentrates outside the procurement seam — most claimed in marketing/SDR (`(4, G)`, `(5, G)` both score under 10), real only where anchored to a constrained tool surface (deal desk) or a compliance gate (CS refund with rollback).

### Capability H — Forecasting / decision support

**H** is the capability of producing predictions and decisions — quota attainment, ARR landing, deal probability, churn risk — with rationale. It draws on V3's reasoning sub-stratum and time-series sub-strata. Binding constraint: the accountability cap — a CRO cannot blame an agent for a missed forecast, so autonomy is capped at recommendation level. **`(12, H)` at OCQ 15 is the column anchor** — Clari, BoostUp, Aviso, Gong Forecast, SF Einstein saturate; the honest read is AI augments (5–15% MAPE lift) but does not replace. The H column has no Genesis-stage cell — it is Product-stage across the matrix.

### Capability I — Negotiation / pricing

**I** is the capability of running real-time discount/concession negotiation, contract redlining, outcome-pricing disputes. It draws on V3's RLHF / preference-tuning sub-stratum and contract-templates sub-stratum. Binding constraint: bilateral evidence — outcome pricing requires dual telemetry, 30/60/90 dispute mechanics, third-party arbitration. The signature I cells are `(6, I)` AE-side real-time at OCQ 13, `(9, I)` AI-specific contract addendum library at OCQ 16, and **`(11, I)` outcome-based pricing operator playbook at OCQ 13** — Sierra's per-resolution thesis tested; SOX rev-rec dispute mechanics unsolved. `(4, I)`, `(5, I)`, `(10, I)` are structurally N/A — SDRs/marketing/CS don't negotiate price.

### Capability J — Coaching / performance

**J** is the capability of grading rep performance — call quality, talk-track adherence, objection handling, deal anti-patterns — and surfacing reflective feedback. It draws on V3's evaluation and observability sub-strata. Binding constraint: what you grade (surface activity vs procurement-seam work). The J column is the most-claimed/least-differentiated column in the matrix — Gong, Chorus, Aircover, Cresta, MindTickle, Hyperbound, Second Nature [IX/VII] all ship. The signature J cell is **`(7, J+M) at OCQ 13`** — coach the procurement-seam work the Playbook teaches, not the call surface.

### Capability K — Computer-use

**K** is the capability of driving GUIs the agent does not have an API for — LinkedIn, Sales Navigator, Coupa, Ariba, Salesforce, Outreach UIs. It draws on V3's computer-use sub-stratum (`9d`). **K is the single capability whose evolution stage moves the most over the next 12 months** — gated entirely on the OSWorld 65% crux (Q3 2026 expected; today ~50% on frontier, Mariner 35–40%). Crossing 65% flips `(4, K)`, `(6, K)`, `(8, K)`, `(9, K)`, `(10, K)`, `(11, K)`, `(12, K)` from demo-ware to deployable for narrow lanes. **Microsoft Sales Copilot wins by default** if OSWorld closes — owns LinkedIn graph + M365 + Dynamics + Outlook first-party. Standalone CU plays survive only on non-LinkedIn signal layers or non-MS-shop AE stacks.

### Capability L — Persistent memory

**L** is the capability of carrying durable agent state across sessions, quarters, and motion stages — commitments made, objections raised, exec changes, usage anomalies. It draws on V3's memory sub-stratum (`9e`) — Mem0, Letta, Zep [IV]. **L is the matrix's most consistent gap.** Critical at `(6, L)` AE deal cycle (OCQ 16), `(11, L)` renewal motion (OCQ 14), `(12, L)` forecasting decay (OCQ 13), `(10, L)` per-customer CX (OCQ 11), `(9, L)` counterparty negotiation (OCQ 10), `(5, L)` multi-year ABM (OCQ 13), `(2, L)` brand voice (Writer-locked). Dev-side memory players have not been picked up by any GTM vendor as of May 2026. Crux C5 (consumer/prosumer memory absorbed vs niche-standalone) is the single most load-bearing crux for the matrix outside `(9, G)`.

### Capability M — Trajectory observability

**M** is the capability of replaying what an agent did — which tools it called, what it retrieved, where it hallucinated — with signed, evidence-grade audit logs. It draws on V3's eval/observability sub-stratum (`9f`) — LangSmith, Braintrust, Galileo, Arize, Helicone serve eng-shape. **M is regulatorily mandatory and commercially unfunded across GTM.** Mandatory in ≤18 months at `(4, M)` SDR (TCPA/CAN-SPAM), `(1, M)`/`(2, M)` marketing (FTC AI-washing + EU Art. 50), `(9, M)` deal-desk (SOX/audit), `(10, M)`/`(11, M)` CS/AM (GDPR right-to-be-forgotten in agent memory). No GTM-shape vendor exists. **M is a horizontal opportunity disguised as 12 vertical ones** — the rubric is half-published in the Playbook §III.5 (Signed Reproducible Eval Reports), §III.3 (Action-Rollback), §III.4 (Sub-Agent Privilege).

## §1.3 The 156-Cell View — How to Read the Matrix

Plate 1 shows the matrix as a 12 × 13 heatmap. **Cell coloring** is OCQ aggregate score on the /20 scale — pale for under 8, mid for 9–12, dark for 13+, accent (`#1d4ed8`) outline for top-15, and a distinct outline at the cell of record `(9, G)`. **Cell labels** show the named lead vendor where one exists, or "no incumbent owner" or "gap" where the cell is unclaimed. Capability columns A–M run left to right; function rows 1–12 run top to bottom. Cluster reads (the row at Function 9, the L-column, the M-column, the K-column) are visible as adjacent shaded bands.

Cell-state vocabulary (binding throughout the workbook):

- **Mature** — multiple incumbent vendors ship credible production; OCQ caps under 12 because claimability is low. Example: `(1, A)`, `(2, B)`, `(4, A)`, `(10, D)`.
- **Forming** — credible vendors ship MVPs; product-market fit forming; claimability moderate. Example: `(1, C)`, `(3, G)`, `(6, B)`.
- **Gap** — no vendor ships production; demand visible; claimability high. Example: `(5, F)`, `(6, E)`, `(6, L)`, `(9, G)`, `(11, L)`.
- **Saturated** — many vendors at parity; differentiation collapsed; OCQ caps under 10 because density × claimability is hostile. Example: `(7, A)`, `(7, B)`, `(7, D)`, `(8, H)`.
- **Underserved** — buyer demand visible; vendor supply thin; OCQ rises with claimability. Example: `(4, F)`, `(4, M)`, `(8, K)`, `(9, A)`.
- **Convergence cell** — multiple capabilities converge into one offering surface. Example: `(3, A+L+F)`, `(7, J+M)`, `(8, M)`, `(9, G)`.
- **N/A** — structurally inapplicable. Example: `(1, E)` brand has no meetings; `(4, I)` SDRs don't negotiate; `(5, I)`/`(5, J)` marketing doesn't negotiate or coach; `(10, I)` lives at `(11, I)`.

Not all 156 cells are populated. Roughly 18 cells are structurally **N/A** — they appear as gray cells in Plate 1, with no OCQ score. Another ~30 cells score below OCQ 8 and are de-facto inactive; the workbook treats them as background context for the cells that matter.

**One reading discipline.** Every cell-coordinate appearance in this workbook is load-bearing — when Ch 2 lifts `(9, G)` into the OCQ × Cell Matrix framework, when Ch 3 anchors Bet #1 at `(9, G)`, when Ch 4 tracks weekly status changes by cell, the coordinate is the same coordinate the matrix here defines. Glossary entries for cell, cell of record, cell-state vocabulary, capability column, function row, and OCQ /20 are in Ch 6 §6.2.

## §1.4 Top-15 Cells by OCQ — The Highest-Leverage Intersections

### 1. (9, G) — 19/20 — Agent procurement gauntlet bilateral evidence pack — **cell of record**

**Status: Gap.** Top vendors: Loopio, Responsive, Arphie, Ironclad, Vanta, Drata, Vendr, Tropic [IX/VIII]. **JTBD:** pass the agent-specific procurement gauntlet in one calendar quarter without bespoke evidence regeneration per counterparty. **The bet:** Bet #1 anchors here. **What's missing:** zero of seven sources ships a unified turnkey bilateral evidence pack — Loopio/Responsive cover content surface, Ironclad covers redlines, Vanta covers SOC 2, Vendr covers buyer-side, no one bundles. The only cell intersecting all seven counterparties simultaneously. Article 14 enforcement (late 2026 / Q1 2027) is the punctuation that re-rates this cell upward; the Playbook (Bet #1 deliverable) sets the procurement default for the next five years if Alex publishes in 90 days.

### 2. (5, F) — 18/20 — Buying-committee mapping

**Status: Gap.** Top vendors: Common Room, Sales Navigator, Clay, ZoomInfo, Apollo, Demandbase [IX]. **JTBD:** know the current dynamic 9-person buying committee at every named target account, refreshed weekly without RevOps labor. **The bet:** Bet-C5 promoted (operator path inside Common Room); Bet-C1 absorbed (build path). **What's missing:** Common Room ships community-only; ZoomInfo/Sales Nav ship static org charts; Clay ships waterfall enrichment. **No vendor ships the multi-source-fusion product** — community signal + intent + relationship graph + life-event signal in one signed weekly artifact. JTBD Job 1 gap = 7 (the largest in Function 1–5). Defensible on signal-fusion engine + signed-artifact format, not the underlying data.

### 3. (6, E) — 17/20 — Deal-diagnosis causation

**Status: Gap at causation; saturated at activity.** Top vendors: Gong [IX/VII], Chorus (ZoomInfo), Clari Copilot, SF Einstein Deal Insights, BoostUp, Aircover, Granola. **JTBD:** when a deal stalls, *why?* — not "no contact in 14 days" (Gong sees this) but "champion went dark because procurement raised AI-vendor risk in week-4 InfoSec review." **The bet:** Bet-C8 promoted (operator-target if credible startup emerges; watch). **What's missing:** Gong sees activity, Einstein pattern-matches deals that lost, Aircover scores deal momentum; no vendor ships causation @ 73% confidence interval tracing causal chains across CRM + email + Slack + transcripts + committee-state + competitor mentions. Builder cell, not Alex's operator cell.

### 4. (4, A) — 16/20 — SDR research/enrichment

**Status: Dense, commoditizing, winner-eats-most.** Top vendors: Clay [IX], Apollo, ZoomInfo Copilot, Cognism AI, Common Room, LeadIQ. **JTBD:** collapse 30-minute pre-call research to <30 seconds at <$0.10/lead. **The bet:** no active bet; relevant as substrate for Bet #2 capability framing. **What's missing:** Clay closed $100M at $1.5B Jan 2026 on waterfall-enrichment-as-code; winner-eats-most-shares-with-Apollo. No new entry below $200M valuation has closed. High OCQ but low Alex claimability — the cell is bundled.

### 5. (6, L) — 16/20 — Persistent memory across 6–9-month AE deal cycle

**Status: Critical gap.** Top vendors: Mem0, Letta, Zep [IV] dev-side only; Salesforce Einstein "opportunity narrative" (shallow); Gong Engage thread memory (shallow). **JTBD:** agent remembers — at week 24, when AE rebuilds context after a 4-week pause — week-4 procurement-side AI Governance pushback on indirect-prompt-injection eval coverage, week-8 champion's boss change, week-11 competitor demo and pricing reset. **The bet:** Bet #5 re-anchored at AE-shape. **What's missing:** enterprise deal cycles are 6–9 months; tooling forgets 2 weeks back. Mem0/Letta target devs, not AE workflow. Whoever ships persistent deal-memory in AE-shape wins disproportionately.

### 6. (9, I) — 16/20 — AI-specific contract addendum library

**Status: Bet #1 + Bet #3 convergence.** Top vendors: Ironclad AI [IX], LinkSquares, SpotDraft, Lexion (Docusign), Evisort (Workday), Pactum AI, Icertis. **JTBD:** negotiate vendor terms — including AI-specific terms (training rights, output ownership, model-update notice, hallucination indemnity, agent-action liability) — semi-autonomously. **The bet:** Bet #1 module + Bet-C10 absorbed (Article 14 Tie-Out Standard). **What's missing:** 12–15 clauses for AI vendor MSAs unbuilt across Ironclad/LinkSquares/SpotDraft. Ironclad's April 2026 product roadmap commits to "AI vendor playbook templates" — direct competitor to Bet #1's clause library. Falsifiability test: if any one ships before Q4 2026, Bet #1's clause-library module loses its window.

### 7. (8, G) — 15/20 — RevOps multi-step trajectory agent

**Status: High-density underserved.** Top vendors: Clari, BoostUp, Aviso, Mosaic, Default, Tomo (NYC) [IX]. **JTBD:** flag stuck deal → ping AE → response → stage update → forecast retrigger as one trajectory. **The bet:** Bet-C7 candidate (parked / watch-list). **What's missing:** Clari/BoostUp/Aviso ship the *pieces*; nobody closes the loop end-to-end. 12–18-month build window; Alex's bet adjacency moderate. Builder cell, not operator cell.

### 8. (4, K) — 15/20 — Computer-use in outbound

**Status: Post-OSWorld watershed.** Top vendors: Anthropic Computer Use [II], OpenAI Operator [II/IX], Mariner, Browserbase, Nooks (parallel-dialer). **JTBD:** agent drives Sales Nav search → connection → LinkedIn message → Outreach update through GUI, no API. **The bet:** Bet #3a (gateway-partner advisory) touches here. **What's missing:** Mariner ~35–40% OSWorld May 2026. **LinkedIn TOS is the structural moat-killer** — Microsoft litigated hiQ Labs 2017–2022, ramped account-suspensions 4× through 2025. Microsoft Sales Copilot wins by default if OSWorld closes.

### 9. (12, F) — 15/20 — Forecasting retrieval

**Status: Mature; best-in-class.** Top vendors: Clari, BoostUp, Gong Forecast, Glean [IX]. **JTBD:** find every email, call, doc, and CRM event for this deal; assemble narrative. **The bet:** no active bet; relevant as substrate for Bet #1's forecasting chapter. **What's missing:** Gong "Deal Stories" (Q3 2025) widely adopted at ~$300M Gong revenue 2025. The cell is mature; the playbook value is *evaluating* AI forecasting vendors (the Aviso/Clari accuracy dispute is a chapter waiting to happen), not building a competing tool.

### 10. (12, H) — 15/20 — Decision support / forecasting

**Status: $1.5B saturated category.** Top vendors: Clari, BoostUp, Aviso, SF Einstein Forecasting, Gong Forecast. **JTBD:** predict end-of-quarter ARR landing within ±5%; rank deals by close probability. **The bet:** Bet #1 procurement overlay specifically targeting forecasting-vendor evaluation. **What's missing:** honest 5–15% MAPE lift; Aviso's 2025 98%-accuracy claim disputed by Gong; CRO commit accuracy 70–85% industry-wide per RevenueCollective Q1 2026. AI augments, doesn't replace — the accountability cap binds. Bet #1 module: "Evaluating AI Forecasting Vendors" Playbook chapter.

### 11. (4, M) — 14/20 — SDR trajectory observability

**Status: Near-empty, regulatorily mandatory.** Top vendors: LangSmith, Braintrust, Galileo, Arize, Helicone [VII] — all eng-shape; no SDR-shape vendor. **JTBD:** when an autonomous SDR sends 10K emails and 6 get TCPA complaints, audit trail (prompt, template, list, model version) is signed, replayable, evidence-grade. **The bet:** Bet #1 module wedge (the SDR side of the M-column overlay). **What's missing:** TCPA, CAN-SPAM, GDPR, CASL, WhatsApp consent (Jan 2026), EU AI Act Art. 14 all imply mandatory ≤18 months. Galileo's $60M Series C rumor April 2026 funds general agent observability — no SDR-shape product.

### 12. (9, M) — 14/20 — Deal-desk agent-trajectory evidence pack

**Status: High-density underserved.** Top vendors: Galileo, Arize, Langfuse [VII]. **JTBD:** observe the agent's trajectory through the deal-desk workflow — what tools it invoked on the MSA, what redlines it generated, what evidence it cited — with signed audit logs the buyer-side AI Governance counterparty will accept. **The bet:** Bet #1 buyer-side advisory + Bet-C10 absorbed (Article 14 Tie-Out Standard). **What's missing:** the agent-trajectory evidence pack referenced in the Addendum Part XIII §3 — "signed reproducible eval reports for this agent against my use case." Nobody ships this turnkey. The unclaimed flag at the procurement seam's M-column intersection.

### 13. (11, L) — 14/20 — Persistent memory for renewal motion

**Status: Best cell in the L-column band.** Top vendors: Sierra (flat memory), Gainsight (structured data), Hippocratic (HIPAA-scoped) [IX]; Mem0/Letta/Zep [IV] dev-side. **JTBD:** remember every commitment, objection, exec change, product-usage anomaly across an 18-month renewal cycle. **The bet:** Bet #5 anchor + Bet-C9 promoted (Persistent Memory as Service Line). **What's missing:** the cross-quarter, cross-team, semantically-rich persistent memory needed for a 4-quarter renewal cycle does not exist in any production CS agent today. Defensibility = data integrations (the moat) + GDPR deletion semantics (regulated capability) + CSM/AE curation UI (Switching Costs).

### 14. (3, A+L+F) — 14/20 — PLG signal + memory + CRM hygiene

**Status: Mature → Forming; convergence cell.** Top vendors: Common Room [IX] ($30M ARR May 2026, Series C $50M @ $250M Sept 2024), Pocus, Endgame (Salesloft Q4 2024), Mutiny, HockeyStack, Toplyne. **JTBD:** identify which free-tier user/anon visitor is in-market (the PQL); route + draft outbound on signal. **The bet:** Bet-C5 promoted (Bet #2 sub-target — operator role inside Common Room). **What's missing:** Common Room ships community-only signal; multi-source fusion (community + product behavior + intent + relationship) sits one product step away. NYC-shipping, Series C-stage; Alex's PLG-adjacent (Cohley) and creative-ops (Bazaarvoice/Curalate) background is a fit. Window: 6–9 months before next-round repricing.

### 15. (6, K) — 14/20 — Computer-use in AE motion

**Status: Emerging.** Top vendors: Anthropic Computer Use [II], OpenAI Operator, Microsoft Sales Copilot (first-party) [IX], Agentforce (API-side, not GUI). **JTBD:** AE says "update Acme opp, log the call, send MAP, schedule with procurement" — agent drives GUIs across Salesforce + LinkedIn + Outreach + Slack. **The bet:** Bet #2 NYC-target capability framing for non-MS-shop AE stacks. **What's missing:** Microsoft Sales Copilot has the structural advantage (LinkedIn + M365 + Dynamics + Outlook first-party). For non-MS-shop AEs (Salesforce + Gmail + Outreach + Slack), cell is open. High asymmetry post-OSWorld-65%.

## §1.5 The Cell-Coverage Map — Pattern Read

The 156 cells do not distribute opportunity uniformly. Three patterns dominate the heat-map.

### Where opportunity clusters

The highest OCQ aggregates land in **three regions**:

**Cluster 1 — the procurement seam at Function 9.** `(9, G)` at 19, `(9, I)` at 16, `(9, M)` at 14, `(9, K)` at 13. Four cells in one row at OCQ ≥ 13, with a single anchor at 19. No other row in the matrix produces this density. This is the through-line for Bet #1.

**Cluster 2 — the L-column (persistent memory) across functions 5, 6, 10, 11, 12.** `(6, L)` at 16, `(11, L)` at 14, `(12, L)` at 13, `(5, L)` at 13, `(10, L)` at 11, `(2, L)` Writer-locked, `(9, L)` at 10. Seven cells across five GTM functions at OCQ ≥ 10, three at OCQ ≥ 13. This is the through-line for Bet #5.

**Cluster 3 — the M-column (trajectory observability) across functions 1, 2, 4, 6, 8, 9, 10, 11, 12.** `(4, M)` at 14, `(9, M)` at 14, `(1, M)` at 14, `(6, M)` at 13, `(10, M)` at 12, `(8, M)` at 12, `(2, M)` at 12, `(11, M)` at 11, `(12, M)` at 10. Nine cells across eight functions at OCQ ≥ 10. This is the M-column overlay on Bet #1.

The **K-column (computer-use)** is a sleeper cluster — every K-cell waits on OSWorld 65% (expected Q3 2026). If/when the crux closes, seven cells `(4, K)`, `(6, K)`, `(8, K)`, `(9, K)`, `(10, K)`, `(11, K)`, `(12, K)` reprice in unison and Microsoft Sales Copilot wins by default on LinkedIn graph + M365 + Dynamics + Outlook first-party.

The single non-clustered high-OCQ cell is **`(5, F)` at 18** — the buying-committee graph. No incumbent, no row-cluster, JTBD Job 1 gap = 7. Bet-C5 territory standalone.

### Where the gaps are

**The M-column is the widest gap.** Regulatorily mandatory in ≤18 months across nine of twelve function rows; LangSmith/Braintrust/Galileo/Arize/Helicone [VII] serve eng-shape; no GTM-shape vendor exists at May 2026. The rubric is half-published in the Playbook §III.5 (Signed Reproducible Eval Reports), §III.3 (Action-Rollback), §III.4 (Sub-Agent Privilege). **M is a horizontal opportunity disguised as 12 vertical ones**, and Bet #1's Procurement Playbook overlays the entire column.

**The L-column is half-built across multiple functions.** Dev-side memory players (Mem0, Letta, Zep [IV]) have not been picked up by any GTM vendor as of May 2026. The L-column is the matrix's most consistent gap, and **Crux C5 (consumer/prosumer memory absorbed vs niche-standalone) is the single most load-bearing crux for the matrix outside `(9, G)`**.

**The procurement-seam — the `(9, *)` row — has the highest concentration of 13+ scores.** This is not a coincidence. Every conversation about an agent vendor inside an F1000 organization eventually routes through the same seven counterparties (InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, Enterprise Architecture); the seam is the place where every gap becomes a procurement-blocking gap.

### The cross-bucket convergence findings

Three patterns recur across the matrix that the per-function chapters do not visibly surface.

**`(9, G)` is the cell of record because procurement is the seam where every counterparty needs the same artifact.** The seven counterparties don't each need a different artifact — they need shared evidence interchanged in a format all seven accept. That is the bilateral evidence pack. Every other high-OCQ cell either feeds `(9, G)` (M-column overlays, I-column addenda) or is operator-only-claimable through `(9, G)` adjacency (Bet #2 NYC targets selling to F500 procurement gauntlets daily).

**Common Room shows up at multiple cells.** `(3, A+L+F)` at OCQ 14 (PLG signal-memory-hygiene), `(4, A)` at OCQ 16 (SDR enrichment substrate), `(4, F)` at OCQ 14 (hygiene-as-code), `(5, F)` at OCQ 18 (buying-committee mapping candidate). The reason: PLG signal + ABM committee mapping share the same underlying community + signal graph. Whoever builds that graph once monetizes it four times. This is the structural argument for Bet-C5 promoted (operator path inside Common Room) vs Bet-C1 absorbed (building a separate BCG product against Common Room).

**Microsoft's cell-coverage breadth is the matrix's deepest moat.** Microsoft 365 Copilot for Sales is the highest-OCQ cross-function vendor at ~18/20 — every cell where M365 + Dynamics + Graph + Purview attaches. 30M+ paid seats Q1 2026, $5B+ ARR. Microsoft owns the K-column post-OSWorld by default; owns the L-column inside the Microsoft Graph; owns the M-column inside Microsoft 365 Compliance Center. **The horizontal-vs-vertical battle in 2026 GTM is decided in favor of "suite floor + vertical wedge + gateway underneath."** Bet #2 NYC targets (Hebbia, Rogo, Sierra, Decagon) survive on vertical-domain depth and non-Microsoft graph wedges.

### The Hebbia phenomenon

Hebbia ranked #1 NYC operator target for Bet #2 even though it is **NOT** a top-5 most-durable company by 7 Powers screen at company resolution. Why: Hebbia is operationally Alex's cell of record for Bet #2 as a composite of four signals.

**F4 composite (career-asymmetry math)** ranks Hebbia first: under-funded ratio 2.5–5% (high equity-asymmetry zone), 0.20–0.40% equity expected, MBB feed-stock (Berger BCG → Hebbia Feb 2026) activated as the third career-feed-stock channel after Stripe and foundation-lab AE departures, 2-quarter window before next Series C close. **F2 (Alex's career asymmetry)** anchors at vertical-data depth in finance — Hebbia's customer base is consulting/banking/PE, where Alex's enterprise B2B + procurement scar-tissue is a stronger ICP fit than MBB candidates on execution depth. **F3 (JTBD coverage)** at `(6, A)` AE pre-call brief in finance — Hebbia, Rogo, Glean are the named anchors; Hebbia and Rogo are NYC-HQ. **F6 (sequencing)** — PE-5 (Anthropic ARR Q3 2026 resolution) is the single load-bearing valuation variable; if conviction high, sign Hebbia *before* the resolution.

Hebbia OCQ at 14/20 (cell-coverage authority) sits below Microsoft 365 Copilot for Sales (18) and Glean (17) at the company-screen level. But **at Alex's specific career-asymmetry math, the equity-asymmetry × MBB-feed-stock × NYC-HQ × `(6, A)` cell-fit combination dominates the cell-coverage authority comparison**. The reconciliation: cell-coverage authority is the bet for Microsoft / Salesforce / Glean career paths (Setting #2 quadrant per Wardley §8.5); equity asymmetry is the bet for Hebbia / Rogo / Augment career paths. Alex's profile compounds harder on the second.

## Apply

**Pick your three highest-leverage cells.** The first should be `(9, G)` by default — the cell of record. The other two should be one you're currently selling against (an AE / CS cell — `(6, A)`, `(6, L)`, `(10, D)`, or `(11, L)`) and one you want to be selling against (a procurement-seam adjacent cell — `(9, I)`, `(9, M)`, `(11, I)`, `(4, M)`).

**Write a 2-sentence pitch for each cell that uses cell-coordinate notation explicitly.** First sentence names the cell, the JTBD, and the gap. Second sentence names the bet, the artifact, and the falsifiability test. *Example for `(9, G)`:* "I operate at `(9, G)` — the agent procurement gauntlet, where zero of seven vendor surfaces ship a turnkey bilateral evidence pack and the Article 14 enforcement window closes for incumbents in 9 months. The artifact is the open Procurement Playbook, published in 90 days; falsifiability is 500 downloads / 50 inbounds in 60 days post-publish."

If you can write three of these — `(9, G)` plus two adjacencies — you operate the matrix. If you can only read it, you have not yet earned the right to lift it into Ch 2's framework chain. The matrix is not the map. It is the conversation surface.
