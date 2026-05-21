# Wave 1 Synthesis — Phase 2a Substrate for Wave 2 Framework Agents

**Date:** 2026-05-13 · **Author:** Phase 2a synthesis subagent · **Input:** wave1_C1–C6, F4, F5, F6, playbook_draft (10 files, ~40K words) · **Consumers:** F1 Wardley, F2 Seven Powers, F3 JTBD

---

## 1. The 12 × 13 Unified Cell Map

Coordinates: Function # (rows 1–12) × Capability letter (cols A–M). Capability key: A=Research/enrichment, B=Personalization+content, C=Multi-channel orchestration, D=Conversation handling, E=Meeting prep/listen/follow-up, F=CRM hygiene/graph, G=Multi-step task execution, H=Forecasting/decision support, I=Negotiation/pricing, J=Coaching/performance, K=Computer-use, L=Persistent memory, M=Trajectory observability. Function key: 1=Demand-gen/brand, 2=Content/SEO, 3=Inbound/PLG, 4=Outbound SDR, 5=ABM, 6=New-biz AE, 7=Enablement/training, 8=RevOps/Sales Ops, 9=Deal desk/pricing/procurement, 10=CS/onboarding, 11=AM/renewals/expansion, 12=Forecasting/strategy.

| Cell | Status | Top vendors [tag] | OCQ | JTBD/evidence |
|---|---|---|---|---|
| **(1,A)** | Mature | 6sense, Demandbase, ZoomInfo Copilot [IX] | 11 | TAL firmographic+intent for demand programs |
| (1,B) | Mature | Mutiny, Jasper, Movable Ink [IX] | — | 50-variant campaign generation; CAC-drag warning |
| (1,C) | Forming | Optimove, Marketo Velocity [IX] | — | Cross-channel handoff w/ shared state — gap |
| (1,D) | Mature | Drift/Salesloft, Intercom Fin, Qualified [IX] | — | Visitor→MQL via dialogue |
| (1,E) | N/A | — | — | Brand has no meetings |
| (1,F) | Forming | 6sense, Demandbase [IX] | — | Account-graph hygiene |
| (1,G) | Forming | Jasper, Salesforce, Adobe [IX] | — | Multi-step demand programs |
| (1,H) | Forming | 6sense Revenue Forecasting, SF Spend Optimizer | — | Spend allocation |
| (1,K) | Underserved→Gap | Adobe Firefly Services, Canva, Runway [IX] | **13** | Creative GUI ops; OSWorld 65% inflection |
| (1,L) | Half-built | 6sense (acct only) [IX] | — | Contact-level brand journey memory — gap |
| (1,M) | **Gap** | — | **14** | Marketing-agent audit/observability — FTC/EU pull |
| (2,A) | Mature | Surfer, Clearscope, MarketMuse | — | Topic-cluster research |
| **(2,B)** | Mature | Jasper, Writer, Copy.ai [IX] | — | Most commoditized cell in matrix; Google E-E-A-T suppression |
| (2,C) | — | — | — | — |
| (2,G) | Forming | Jasper, Copy.ai, HubSpot Breeze [IX] | 9 | Brief→draft→publish single trajectory |
| (2,K) | Gap→Forming | Runway, Adobe Firefly, HeyGen [IX] | 13 | (same as 1,K) |
| **(2,L)** | Forming | Writer Knowledge Graph [IX] | — | Brand-voice persistent memory — Writer's enterprise moat |
| (2,M) | Gap | — | 12 | FTC AI-washing + EU Article 50 |
| (2,H) | Mature | Clearscope, MarketMuse, Conductor | — | Topic-traffic prediction |
| **(3,A+L+F)** | Mature→Forming | Common Room, Pocus, Endgame (Salesloft) [IX] | **14** | PQL identification + signal routing — Alex-claimable |
| (3,D) | Mature | Intercom Fin, Drift, Qualified [IX] | — | In-product qualify+book |
| (3,G) | Forming | Common Room, Default, Tray.ai [IX] | — | PQL→enrich→assign→activate single trajectory |
| (3,H) | Forming | Pocus AI Plays [IX] | — | Free→paid conversion prediction |
| (3,K) | Gap | HeyGen, Tavus [IX] | — | In-product autonomous walkthrough |
| (3,M) | Gap | — | — | PLG-funnel agent observability |
| (3,I), (3,L) | Gap/Partial | — | — | In-product pricing nego, cross-org PLG memory |
| **(4,A)** | Dense, commoditizing | Clay, Apollo, ZoomInfo, Common Room [IX] | **16** | <30s pre-call research at <$0.10/lead |
| (4,B) | Dense, RR-negative | 11x, AiSDR, Artisan, Regie, Lavender [IX] | 10 | "Synthetic SDR" ceiling — 11x flat $20M |
| (4,C) | Incumbent-owned | Outreach AI, Salesloft, Apollo [IX] | 11 | Cross-channel sequencing absorbed by seats |
| (4,D) | Emerging | 11x AVA, AiSDR, Nooks [IX] | 12 | 40-60% auto-resolution of low-stakes replies |
| **(4,E)** | Underserved (handoff seam) | Granola, Gong, Chorus [IX/VII] | 13 | SDR→AE briefing whitespace |
| **(4,F)** | Under-served | Clay, Common Room, Apollo [IX] | 14 | Hygiene-as-code (Clay deeper play) |
| (4,G) | Dense, mostly vapor | 11x, AiSDR, Artisan, Agentforce SDR [IX] | 9 | Autonomous SDR loop — adverse selection |
| (4,H) | Under-served | Clari, BoostUp, Outreach Commit [IX] | 11 | Cohort-level SDR-quality decay forecast |
| (4,I) | N/A | — | — | SDRs don't negotiate |
| (4,J) | Incumbent | Gong, Chorus, Aircover, Second Nature [IX/VII] | 11 | Call-quality at scale |
| **(4,K)** | POST-OSWORLD WATERSHED | Anthropic CU, OpenAI Operator, Mariner, Browserbase, Nooks [II/VI] | **15** | LinkedIn/Sales Nav GUI driving; LinkedIn-TOS moat-killer |
| (4,L) | Under-served, cheap to add | Mem0, Letta, Zep [IV] | 12 | Cross-prospect memory; absorbed H2 2026 |
| **(4,M)** | Near-empty, regulatory-mandatory | LangSmith, Braintrust, Galileo, Arize [VII] | **14** | TCPA/CAN-SPAM evidence-grade audit; Alex-Bet-#1 |
| (5,A) | Dense | 6sense, Demandbase, Clay, ZoomInfo, Bombora [IX] | 12 | Account intent |
| (5,B) | Dense, attribution-vapor | Mutiny, 6sense Conversational Email [IX] | 9 | Named-account personalization |
| (5,C) | Incumbent-locked | Demandbase One, 6sense Revenue AI [IX] | 10 | Cross-account orchestration |
| (5,D) | Niche | Drift, Qualified, 6sense [IX] | 9 | Named-account routing |
| (5,E) | Cross-tool, under-served | Gong Account Plans, DealHub [IX/VII] | 11 | Cross-committee pre-brief |
| **(5,F)** | **Top single cell** | Common Room, Sales Nav, Clay, ZoomInfo [IX] | **18** | Dynamic 9-person committee map — **NO INCUMBENT OWNER** |
| (5,G) | Vapor | 6sense Revenue AI, Demandbase Pipeline AI [IX] | 8 | Autonomous ABM play |
| (5,H) | Bundled | 6sense, Demandbase, Clari [IX] | 9 | ABM forecasting |
| (5,I), (5,J) | N/A/gap | — | 6 | Marketing doesn't nego/coach |
| (5,K) | Nascent | Mariner, Operator [II] | 9 | ABM platform UI driving |
| (5,L) | Under-served | [gap] | 13 | Multi-year ABM cycle memory |
| (5,M) | Empty | [gap] | 11 | ABM agent observability |
| (6,A) | Bundled, copilot | MS Sales Copilot, Agentforce, Gong Engage, **Hebbia, Rogo, Glean** [IX] | 14 | AE pre-call brief; Hebbia/Rogo NYC anchors |
| (6,B) | Emerging | Aircover, Clari Copilot, Gong Engage [IX] | 12 | Post-call MAP/summary draft |
| (6,C) | Incumbent | Outreach AI, Salesloft, Apollo [IX] | 9 | AE cadences |
| (6,D) | Live-assist | Aircover, Cresta, Gong Assist, Hyperbound [IX] | 13 | Real-time objection/pricing guardrail |
| **(6,E)** | Empty at causation | Gong, Chorus, Clari, Aircover, Granola [IX/VII] | **17** | Deal-diagnosis cell — Gong sees activity, NO ONE ships causation |
| (6,F) | Incumbent | SF EAC, Gong Engage, People.ai, Scratchpad [IX] | 11 | Activity capture |
| (6,G) | Vapor net-new | Agentforce, 11x Mike [IX] | 8 | Autonomous AE — no F500 production |
| (6,H) | Incumbent | Clari, BoostUp, Gong Forecast, SF Einstein [IX] | 12 | AE deal-level forecast |
| (6,I) | Under-served | Pricefx, DealHub, Vendavo, Ironclad, SF CPQ Agentforce [IX] | 13 | Real-time discount/concession nego |
| (6,J) | Incumbent | Gong, Chorus, Aircover, Cresta, MindTickle, Hyperbound [IX] | 12 | AE manager coaching |
| **(6,K)** | Emerging | Anthropic CU, Operator, MS Sales Copilot [II/IX] | 14 | AE motion GUI ops; MS structural advantage |
| **(6,L)** | **Critical gap** | Mem0, Letta, Zep [IV] dev-side only | **16** | 6-9mo deal cycle memory — none ship AE-shape |
| (6,M) | Empty, near-mandatory | LangSmith, Braintrust, Galileo [VII] | 13 | AE agent audit pre-autonomy |
| (7,A–E) | Saturated/commodity | Highspot, Seismic Aura, MindTickle, Gong, Granola [IX/VII] | 7–9 | Enablement content/coaching |
| (7,G) | Underserved | MindTickle, Spekit, Seismic Learning [IX] | 11 | Certification end-to-end |
| **(7,J+M)** | Most-claimed/empty | Highspot AI, MindTickle Copilot, Showpad, Second Nature, Hyperbound, Galileo cross-applied [IX/VII] | **13** | Trajectory-grade coaching of procurement-seam work — ramp gap |
| (7,K) | Nascent | Hyperbound, Second Nature [IX] | 9 | Coach via screen demonstration |
| (7,L) | Gap | — | 8 | Per-rep cross-quarter memory |
| (8,A) | Embedded | Clari AI, Pocus, Endgame [IX] | 7 | RevOps Account 360 |
| (8,F) | Agentified | Syft, Default, Truva, Clari Copilot, SF Einstein 1 [IX] | 11 | CRM hygiene multi-tenant write governance |
| **(8,G)** | High-density underserved | Clari, BoostUp, Aviso, Mosaic, Default, Tomo (NYC) [IX] | **15** | RevOps trajectory agent (pipeline scrub loop) — no one closes loop |
| (8,H) | Saturated | Clari, BoostUp, Aviso, SF, Gong Forecast [IX] | 10 | Forecasting MAPE plateau 8-12% |
| (8,K) | Underserved | [gap; Anthropic CU generic] | 12 | RevOps drives SFDC/HubSpot UIs |
| (8,L) | Embedded | Clari, BoostUp [IX] | 7 | History-aware forecasting |
| (8,M) | Convergence cell | Gong, Galileo, Arize, LangSmith [VII/IX] | 12 | RevOps automation audit |
| (9,A) | Underserved | AlphaSense, CB Insights, PitchBook [IX] | 9 | Deal-desk buyer history brief |
| (9,B) | — | DealHub AI, Subskribe, PandaDoc [IX] | 8 | Proposal personalization |
| (9,F) | (cross from 8F) | — | — | — |
| **(9,G)** | **THE CELL OF RECORD** | Loopio, Responsive, Arphie, Ironclad, Vanta, Drata, Vendr, Tropic [IX/VIII] | **19** | Agent procurement gauntlet bilateral evidence pack — zero turnkey |
| (9,H) | (cross from 8H) | — | — | — |
| **(9,I)** | Bet#1+Bet#3 convergence | Ironclad AI, LinkSquares, SpotDraft, Lexion, Evisort, Pactum, Icertis [IX] | **16** | AI-specific contract addendum library; 12-15 clauses unbuilt |
| (9,K) | Nascent but big | SF CPQ Agentforce, DealHub, Subskribe [IX] | 13 | Agents drive Coupa/Ariba/Workday Procurement |
| (9,L) | Underserved | Ironclad AI clause memory, LinkSquares [IX] | 10 | Counterparty-history memory w/ provenance |
| **(9,M)** | High-density underserved | Galileo, Arize, Langfuse [VII] | **14** | Agent-trajectory evidence pack (Part XIII §3) |
| **(10,D)** | **Densest cell in agent-GTM by $** | Sierra, Decagon, Intercom Fin, Ada, Forethought, Kustomer, SF Agentforce, ServiceNow, HubSpot, Hippocratic [IX] | 14 | Tier-1/2 issue resolution; Klarna reversal reset budgets |
| (10,A–C, F) | Mature/saturated | Zendesk, Intercom, Forethought, SF Service Cloud, Pylon [IX] | 6–11 | Help-desk + CDP-class |
| (10,E) | Underserved | Gainsight AI, Catalyst, Vitally, Granola, Read.ai [IX] | 12 | QBR/kickoff pre-brief |
| (10,G) | Hard problem, 2026 wedge | Sierra Agent OS, Decagon, SF Agentforce, Replit [IX/X] | 13 | Refunds/order-changes w/ rollback; OSWorld 65% gates |
| (10,K) | Almost empty | Anthropic CU [II] | 10 | Help-desk GUI driving |
| (10,L) | Claimed-everywhere, real-nowhere | Sierra "Memory," Decagon Knowledge, Hippocratic [IX] | 11 | RAG-over-store ≠ durable memory; GDPR deletion |
| (10,M) | Adjacent-vendor | Lakera, LangSmith, Galileo, Arize, Helicone, Braintrust [VII/VIII] | 12 | "Audit trail when agent screws up" — #2 CIO question |
| (11,A) | Underserved by agents | Gainsight AI, Catalyst, Clay, Crossbeam [IX] | 10 | Renewal-cycle research |
| (11,B) | Gap | — | 9 | Renewal pitch personalization |
| (11,E) | Soft cell | (=10,E) | 11 | QBR/EBR |
| (11,G) | Gap | SF Agentforce demo, Gainsight Renewal Center [IX] | 13 | Pull usage→draft→route→procurement single trajectory |
| (11,H) | Gainsight's home turf, weak | Gainsight, ChurnZero, Totango, Catalyst, Clari [IX] | 12 | NRR forecast — correlative not causal |
| **(11,I)** | Outcome-based pricing experiment | Sierra ($1-4/res), Decagon (hybrid), Intercom Fin ($0.99 list), Hippocratic ($9/hr), SF Agentforce ($2/conv) [IX] | 13 | Per-resolution/per-task pricing; SOX rev-rec risk |
| (11,K) | Gap | — | 9 | CS/ERP/finance for renewal ops |
| **(11,L)** | **Best cell in C4 band** | Sierra (flat), Gainsight (structured), Hippocratic [IX]; Mem0/Letta/Zep [IV] | **14** | Multi-quarter durable agent memory — does not exist production |
| (11,M) | Adjacent | (=10,M) [VII/VIII] | 11 | AM agent audit |
| **(12,F)** | Mature | Clari, BoostUp, Gong Forecast, Glean [IX] | 15 | Cross-system narrative retrieval; Gong "Deal Stories" |
| **(12,H)** | "Natural cell" | Clari, BoostUp, Aviso, Gong Forecast, SF Einstein [IX] | 15 | ARR landing ±5%; hybrid beats AI alone |
| (12,A–C, G, J) | Feature-not-agent | Clari Signals, Pigment AI, Anaplan AI, Cube, Fullcast, Mosaic [IX] | 8–13 | Reasoning/planning/orch shallow |
| (12,D) | Niche/strong | **Hex (NYC)**, Definite, Mosaic [IX] | 14 | NL→SQL→chart for analysts |
| (12,I) | Gap | — | 8 | Self-correction on past forecast misses |
| (12,K) | Early | Pigment AI, Mosaic, Cube [IX] | 11 | Cross-BI GUI assembly; OSWorld 65% gates |
| **(12,L)** | Richest unclaimed cell in C5 | BoostUp Forecasting Health [IX]; Mem0/Letta/Zep [IV] unadopted | 13 | 8-quarter pipeline-decay memory — **Bet #5 anchor** |
| (12,M) | Almost pure gap | Galileo, Arize, Coval [VII] | 10 | Meta-observability: are forecasting agents drifting? |
| (12, "Strategy") | **Largest gap in matrix** | Fullcast, Pigment AI, Mosaic, Varicent partial [IX] | 12 (est.) | GTM motion design — CRO can't blame an agent; accountability cap |

Cells marked **[unmapped]** by Wave 1: most of column M for functions 1-3, 5; some I/J cells for marketing functions; (7,B–F partial); (9,J).

---

## 2. Top-15 Cell Ranking by OCQ (Descending)

1. **(9,G) — 19/20** — Agent procurement gauntlet bilateral evidence pack. The cell of record. Zero of seven overlays shipped turnkey; Article 14 enforcement window late 2026 closes the door for incumbents. Bet #1 anchor.
2. **(5,F) — 18/20** — Buying-committee mapping. Dynamic 9-person committee + intent + relationship + life-event signal, signed weekly. No incumbent owner. Common Room ships community-only; ZoomInfo/Sales Nav ship static. JTBD Job 1 gap = 7.
3. **(6,E) — 17/20** — Deal-diagnosis (causation, not activity). "Why did this deal stall?" causal chain across CRM + comms + transcripts + competitor signal. Gong sees activity; Einstein pattern-matches; nobody ships causation @ 73% confidence.
4. **(4,A) — 16/20** — SDR research/enrichment. Crowded (Clay, Apollo, Common Room, ZoomInfo) but high OCQ. Clay $100M @ $1.5B Jan'26 = winner-eats-most.
5. **(6,L) — 16/20** — Persistent memory across 6-9mo AE deal cycle. Mem0/Letta dev-only; AE-shape product unbuilt. Whoever ships wins disproportionately.
6. **(9,I) — 16/20** — AI-specific contract addendum library. 12-15 clauses for AI vendor MSAs. Ironclad roadmap committed Q2'26; Bet #1 module falsifiability test.
7. **(8,G) — 15/20** — RevOps multi-step trajectory agent. Pipeline scrub + forecast prep + territory rebalance loop closure. Clari/BoostUp/Aviso ship pieces, nobody ships loop.
8. **(4,K) — 15/20** — Computer-use in outbound. Post-OSWorld-65% (Q3 2026 expected) deployable; Microsoft Sales Copilot wins by default. LinkedIn-TOS = structural moat-killer.
9. **(12,F) — 15/20** — Forecasting retrieval. Best-in-class; Gong "Deal Stories" widely adopted; ~$300M Gong revenue 2025.
10. **(12,H) — 15/20** — Decision support/forecasting. $1.5B saturated category; AI augments, doesn't replace; Bet #1 procurement overlay opening.
11. **(4,M) — 14/20** — SDR trajectory observability. Regulatorily mandatory ≤18mo (TCPA, CAN-SPAM, GDPR, CASL, EU AI Act Art. 14). No SDR-shape vendor May 2026.
12. **(9,M) — 14/20** — Deal-desk agent-trajectory evidence pack. The Part XIII §3 signed eval report as a product surface.
13. **(11,L) — 14/20** — Persistent memory for renewal motion. Bet #5 anchor; data integrations + deletion semantics + curation UI = three-stage moat.
14. **(3,A+L+F) — 14/20** — PLG signal + memory + CRM hygiene. Common Room $30M ARR May'26; Bet #2 candidate; NYC-shipping, Alex-claimable.
15. **(6,K) — 14/20** — Computer-use in AE motion. MS structural advantage; non-MS-shop AE cell (SF+Gmail+Outreach+Slack) open.

Honorable mentions (13s): (1,K)/(2,K) creative GUI; (4,F) RevOps hygiene-as-code; (6,D) live-assist; (6,I) AE negotiation; (7,J+M) trajectory-grade coaching; (9,K) procurement-portal CU; (10,G) CS multi-step; (11,I) outcome-pricing operator playbook; (12,D) Hex analyst agent; (12,L) forecasting memory.

---

## 3. Cross-Bucket Convergence Findings

**The L-column (persistent memory) is the matrix's most consistent gap.** Critical at (6,L) AE deal cycle, (11,L) renewal motion, (12,L) forecasting decay, (10,L) per-customer CX, (9,L) counterparty negotiation, (5,L) multi-year ABM, (2,L) brand voice (only Writer has it). Dev-side memory players (Mem0, Letta, Zep [IV]) are not picked up by ANY GTM vendor as of May 2026. **Crux C5 (consumer/prosumer memory absorbed vs niche-standalone) is the single most load-bearing crux for the matrix outside (9,G).** Bet #5 (memory architecture practice) compounds across this entire column. F2 should treat L as a column-spanning Switching-Costs lever.

**The M-column (trajectory observability) is regulatorily mandatory and commercially unfunded across GTM.** Mandatory ≤18 months at (4,M) SDR (TCPA/CAN-SPAM), (1,M)/(2,M) marketing (FTC AI-washing + EU Art. 50), (9,M) deal-desk (SOX/audit), (10,M)/(11,M) CS/AM (GDPR right-to-be-forgotten in agent memory). LangSmith/Braintrust/Galileo/Arize [VII] serve eng-shape; no GTM-shape vendor exists. **Bet #1's Procurement Playbook overlays the entire M-column** — the rubric is half-published in playbook §III.5 (Signed Reproducible Eval Reports), §III.3 (Action-Rollback), §III.4 (Sub-Agent Privilege). M is a horizontal opportunity disguised as 12 vertical ones.

**The K-column (computer-use) is gated entirely on OSWorld 65% crux (C3, Q3 2026 expected).** Today ~50% on frontier (Mariner 35-40%). Crossing 65% flips (4,K) LinkedIn/Sales Nav, (6,K) AE motion, (8,K) RevOps CRM driving, (9,K) Coupa/Ariba/Workday Procurement automation, (10,K)/(11,K) CS/AM tool driving, (12,K) BI/spreadsheet board-deck assembly. **Microsoft Sales Copilot wins by default if OSWorld closes** — owns LinkedIn graph + M365 + Dynamics + Outlook first-party. Standalone CU plays survive only on non-LinkedIn signal layer or non-MS-shop AE stack. F1 Wardley: K is the single capability whose evolution stage moves the most over 12 months.

**The G-column (multi-step execution) concentrates value at the procurement seam.** (9,G) 19/20 is the matrix peak. (8,G) 15 RevOps loop, (11,G) 13 renewal loop, (10,G) 13 CS refund/account-change, (2,G) 9 content workflow, (3,G) PLG-to-pipeline, (1,G) demand programs. G is where vapor concentrates outside (9,G) — most claimed in marketing/SDR, real only where Anchored to constrained tool surface (deal desk) or compliance gate (CS refund w/ rollback).

**Capability × counterparty convergence (F5 gauntlet):** (9,G) procurement-seam intersects all seven counterparties (InfoSec/Legal/Privacy/AI Governance/Procurement/Sponsor/Enterprise Architecture). (4,M)/(9,M) ↔ InfoSec + AI Governance + Legal. (6,L)/(11,L) ↔ Privacy (GDPR memory deletion) + Legal. (4,K)/(6,K) ↔ EA (OAuth blast radius, sub-agent fan-out, per-trajectory cost ceiling) + InfoSec. (11,I) outcome pricing ↔ Procurement + CFO (SOX rev-rec, dispute mechanics). **The seven counterparties map onto seven capability bundles, not 13 capabilities — F5's seventh counterparty (EA) is what makes the K + L + M columns procurable.**

**Stratum density.** IX (vertical agent products) saturates ~85% of named cells; II (runtime — Anthropic CU, Operator, Mariner) concentrates at K column; IV (memory — Mem0/Letta/Zep) concentrates at L column dev-side only; VII (eval/obs — LangSmith/Braintrust/Galileo/Arize) concentrates at M column eng-shape only; VIII (safety — Lakera/Protect AI) bleeds into M; X (end-user surfaces — Notion AI, Slack AI) crosses (7-12 functions). **The matrix is 85% IX with thin slivers of II/IV/VII/VIII at K/L/M — exactly the substrate Bets #1, #4, #5 target.**

**Multi-bucket companies (appearing in 3+ C-files).**
- **Clay [IX]**: (4,A), (4,F), (5,A), (8,F) — RevOps-orchestration anchor; $80-110M ARR Q1'26; only durable RevOps winner per 7 Powers screen.
- **Glean [IX]**: (6,A), (8,A), (10,A), (12,F), cross-function Function 7/10/11 — $50M→$300M+ Q1'26; Network Economies vertical-bounded; Series E $260M @ $7.2B Sep'25.
- **Microsoft 365 Copilot for Sales [IX/X]**: cross-funnel M=1-6 + capabilities K/L/M via Graph/Recall/Purview; 30M+ paid seats Q1'26 = $5B+ ARR; **highest cell-coverage breadth in entire matrix**.
- **Salesforce Agentforce [IX]**: every GTM cell M=1-12; AgentExchange Dec'25; $2/conv pricing retreated Feb'26.
- **Gong [IX/VII]**: (4,E), (4,J), (5,E), (6,D), (6,E), (6,F), (6,J), (7,D), (7,M), (8,M), (10,M), (12,F) — call-data substrate that other vendors quietly read from.
- **Sierra [IX]**: (10,D), (10,G), (10,L), (11,I), (11,L) — $175M+ ARR Q1'26, $10B val Mar'26; per-resolution pricing thesis; sub-agent privilege docs most mature.
- **Hebbia [IX]**: (6,A), (12,F)-adjacent, FinServ/MBB anchor — $30→$50M+ Q1'26 NYC HQ.
- **Common Room [IX]**: (3,A+L+F), (4,A), (4,F), (5,F) — $30M ARR May'26; PQL → committee-graph candidate.

The horizontal cross-pollination tells us: **Glean, Microsoft 365 Copilot, Salesforce Agentforce are the three suites contending for cell-coverage breadth supremacy; Clay is the only durable orchestration wedge; Sierra is the only outcome-pricing at-scale wedge; Hebbia/Rogo are the NYC vertical-data wedges.** F2 (Seven Powers) should screen these for which has Network Economies, Switching Costs, or Cornered Resource.

---

## 4. Contradictions & Tensions Across Wave 1

**T1. Outcome-pricing exportability.** C4 says outcome pricing is Sierra's thesis tested and Bret-Taylor-bullish; F6 says outcome works ONLY where trajectory is discrete + completable + buyer-visible (CX has all three; legal/finance/dev have zero/one/two). C5 reinforces the failure mode at Function 12: CROs can't blame an agent for a missed forecast, accountability line caps autonomy. **Tension: is outcome pricing the future of agent-GTM (C4) or is it a CX-only phenomenon with a 12-18 month window in adjacent verticals (F6/C5)?** Arbitrate via F2 — outcome pricing as a Power flavor.

**T2. Foundation-lab walk-up severity.** C1 marks foundation labs walking up-stack as marketing's #1 risk (Sev 12/20). C3 says vertical-data depth is the moat (Hebbia/Rogo/Sierra/Decagon). C6 says incumbent suites (M365 Copilot, Agentforce) beat both at the suite level. **Tension: who eats whom — foundation labs eat verticals, verticals defend on data, or suites eat both?** The Wave 1 consensus is "suite floor + vertical wedge + gateway underneath" (C6 §4), but C1 frames the threat differently for marketing-content vendors specifically. F1 Wardley: this is the central evolution question.

**T3. Common Room as cell-(3,A+L+F) vs cell-(5,F) candidate.** C1 frames Common Room as Bet #2 PLG candidate (OCQ 14, claimable). C2 frames Common Room as ONE of several insufficient (5,F) committee-mapping inputs (community-only signal). **Tension: is Common Room a Bet #2 acquisition target for Alex, or is it a building block someone else builds (5,F) on top of?** Both can be true; needs disambiguation at Phase 4.

**T4. Ironclad/Vanta absorption timing.** C3 marks Ironclad/LinkSquares/SpotDraft April 2026 roadmap commits as "direct competitor to Bet #1's clause library" — Challenge score 17/20. Playbook draft §III.5 (Signed Reproducible Eval Reports) and §III.6 (Article 14 Tie-Out) say no incumbent ships these. **Tension: how much of Bet #1 is durable vs how much gets eaten by Vanta/Drata/Ironclad in 6-9 months?** Wave 1 agents disagree on the survivability of the productized branch vs advisory branch.

**T5. Hebbia's NYC composite ranking.** F4 §F4.7 puts Hebbia at #1 composite (under-funded ratio 2.5-5%, 0.20-0.40% equity, MBB+Stripe-flavored buyer). C6 puts Hebbia OCQ 14, behind M365 Copilot (18), Glean (17), Agentforce (17), Cloudflare (16). **Tension: does Alex prioritize equity asymmetry (F4) or cell-coverage authority (C6)?** The 7 Powers screen should arbitrate; this is also a JTBD question (which Alex-JTBD does the role satisfy?).

**T6. Sub-agent privilege separation maturity.** Playbook draft §III.4 says Sierra is most mature; C3 §4 says zero of seven overlays ship turnkey. **Tension: is Sierra "most mature internally but not turnkey publishable" or "mature enough to be the reference"?** F3 JTBD needs to clarify whether the buyer-JTBD is satisfied by Sierra's internal practice or only by a published artifact.

**T7. F5's seven-counterparty count vs the playbook's six-counterparty TOC.** Playbook draft Section II lists six chapters; F5 §0 argues EA/IT is a distinct seventh at F1000 scale. **Reconciliation:** Alex confirmed seven; playbook TOC needs update in Phase 5. Note this for the reconciler.

**T8. (12,H) forecasting accuracy claims.** C5 cites Aviso's 98% accuracy claim disputed by Gong; Clari cites 10-20% improvement vendor-marketed-not-validated; RevenueCollective Q1'26 survey says CRO commit accuracy 70-85% industry-wide. **Tension: is forecasting AI a 5-15% MAPE improvement (honest) or a category in vendor-marketing crisis (the Aviso/Clari dispute)?** Material for Bet #1 Procurement Playbook section on "Evaluating AI Forecasting Vendors."

---

## 5. Candidate New "Bets" Surfaced by the Matrix

**Bet-C1. The Buying-Committee Graph (BCG) product.**
- Cell: (5,F) primarily; touches (4,A), (4,F), (6,A), (6,E).
- Signal: OCQ 18/20, no incumbent owner, JTBD Job 1 gap = 7. Common Room community-only; ZoomInfo/Sales Nav static; Clay enrichment-only.
- Conviction: **HIGH**. Multi-source signal fusion + signed-artifact format = defensible.
- Framework confirmation: F2 (Seven Powers — Network Economies if it becomes the dynamic-graph format).
- Relation to 7 Bets: **NEW** — augments Bet #2 (vertical-agent operator role inside whoever builds it) and Bet #5 (memory architecture practice).

**Bet-C2. Trajectory-Grade Procurement-Seam Enablement Coach (cells 7,J+M).**
- Cell: (7,J+M) convergence; OCQ 13/20.
- Signal: Median F1000 AE ramp stuck at ~7 months despite 4 years of AI coaching. Coaching agents grade call surface, not procurement-seam work (InfoSec Qs, MSA redlines, Article 14 oversight).
- Conviction: **MEDIUM**. The only cell that came from one Wave 1 agent (C3); others didn't see it. That's a feature — it's an accident-of-light finding.
- Framework: F3 (JTBD — does it satisfy the CRO "ramp-curve" job or the AE "pass-procurement" job?).
- Relation to 7 Bets: **SHARPENS Bet #1** — coach the procurement-seam work the Playbook teaches. Becomes a Playbook-monetization vector.

**Bet-C3. Per-Trajectory FinOps Audit Practice (extended).**
- Cell: cross-cuts (4,M), (6,M), (9,M), (12,M); plus all K-cells once OSWorld 65% crosses.
- Signal: Anthropic Claude Agent SDK 2.0 Apr'26 + OpenAI Responses API exposed per-trajectory billing; 30-60% savings on multi-hop trajectories at $1M+ AI spend.
- Conviction: **MEDIUM-HIGH** — window 12-18 mo before AWS Bedrock auto-routing bundles.
- Framework: F1 (Wardley — does this commoditize before Alex monetizes?).
- Relation to 7 Bets: **EXTENDS Bet #4** (FinOps reframe) into Bet #1 advisory module. F6 §7 already lifts this.

**Bet-C4. Outcome-Definition Contract Template practice.**
- Cell: (11,I) primary; touches (9,I), (9,G).
- Signal: F500 buyers enter outcome-pricing without measurement-and-dispute mechanics; 8-15% outcome-count disputes settled by negotiation not contract (Mar-Apr'26 off-record). Pricing-strategy practice is upstream of vendor selection.
- Conviction: **HIGH** for advisory — no vendor turnkey-answers; no buyer internal playbook.
- Framework: F2 (operator-shape Power flavor) + F3 (CFO/Procurement JTBD).
- Relation to 7 Bets: **SHARPENS Bet #1** — productize the pricing-side Playbook deliverable. F6 §7 nominates this as the highest-leverage Bet #1 wedge.

**Bet-C5. The (5,F) BCG built on top of Common Room.**
- Distinct from Bet-C1 — operator path rather than builder path.
- Cell: (5,F) + (3,A+L+F).
- Signal: Common Room ships community-only; the multi-source-fusion product can be built ON TOP of CR rather than against it. Senior PMM/GTM role inside Common Room at $30M ARR / Series C $250M val.
- Conviction: **MEDIUM** — depends on Common Room's roadmap willingness.
- Framework: F4 (NYC composite #5-7); F3 (Alex-JTBD: career-asymmetry).
- Relation to 7 Bets: **SHARPENS Bet #2** with a specific named target.

**Bet-C6. AI-Vendor Procurement Standard as Open Spec.**
- Cell: meta over (9,G).
- Signal: Playbook draft is "the spine of Bet #1." Open-spec move (a la OpenTelemetry GenAI conventions) creates Switching-Costs-flavored Power if Alex becomes the canonical maintainer.
- Conviction: **HIGH** — first credible publisher sets the procurement default for next five years (Playbook §III.5).
- Framework: F2 (Process Power flavor for the maintainer).
- Relation to 7 Bets: **REFRAMES Bet #1** from "advisory practice" to "advisory practice + open spec stewardship."

**Bet-C7. RevOps Trajectory Agent (closing the pipeline-scrub loop).**
- Cell: (8,G) OCQ 15.
- Signal: Clari/BoostUp/Aviso ship pieces; nobody ships loop closure (flag → ping AE → response → stage update → forecast retrigger).
- Conviction: **MEDIUM** — 12-18 mo build window; Alex's bet adjacency moderate.
- Framework: F1 (where on evolution curve does this sit?), F3 (RevOps JTBD).
- Relation to 7 Bets: **NEW** — not currently in 7-bet list; candidate for watch-list rather than active bet.

**Bet-C8. Deal-Diagnosis Causation Engine (6,E).**
- Cell: (6,E) OCQ 17/20.
- Signal: Gong sees activity, Einstein pattern-matches, no one ships causation @ confidence interval. Aircover closest attempt.
- Conviction: **MEDIUM-HIGH** for builder path; LOW for Alex operator path (technical product).
- Framework: F1 (capability evolution: does the data exist to support causation today?), F2 (data-graph moat).
- Relation to 7 Bets: **NEW operator-target** — fits Bet #2 NYC list if a credible startup emerges. Watch.

**Bet-C9. Persistent Memory as Service Line (11,L + 6,L + 12,L).**
- Cell: column L bundled.
- Signal: dev-side memory (Mem0/Letta/Zep) NOT picked up by any GTM vendor. The data integrations + GDPR deletion semantics + CSM/AE curation UI = three-stage moat.
- Conviction: **HIGH** — this IS Bet #5 reframed at cell-resolution.
- Framework: F2 (Switching Costs across L-column); F3 (CS/AM/AE JTBD: "remember commitments across cycle").
- Relation to 7 Bets: **EXTENDS Bet #5** — anchors the architecture practice with three named GTM cells.

**Bet-C10. The Article 14 Tie-Out Standard.**
- Cell: meta over column M, specifically (9,M).
- Signal: April 2026 draft Article 14 guidance; enforcement late 2026 / Q1 2027. No vendor ships tie-out; first credible publisher = procurement-standard maintainer.
- Conviction: **HIGH** for advisory; **HIGH-time-sensitive**.
- Framework: F1 (evolution stage: Genesis), F2 (Process Power as standard-bearer).
- Relation to 7 Bets: **SHARPENS Bet #1** — specific module + open-spec wedge. Playbook §III.6 is the existing artifact.

---

## 6. The "Where Alex Should Claim" Map

Five-to-seven cells most-claimable for Alex's specific profile (12yr enterprise B2B + AI-builder + NYC + procurement scar-tissue):

1. **(9,G) — Agent procurement gauntlet bilateral evidence pack. OCQ 19/20.**
   - **Why claimable:** Alex's 12-year procurement scar-tissue + AI-builder fluency is the rare-profile prerequisite. No incumbent. Playbook draft already at 9,700 words.
   - **Path: PUBLISH** the Playbook (90 days) + ADVISE on Cloudflare/Kong gateway-partner positioning + ADVISE F1000 buyers directly. Earned over the next 12 months as default reference.

2. **(11,I) — Outcome-based pricing operator playbook. OCQ 13/20 (procurement-side wedge).**
   - **Why claimable:** F1000 procurement vocabulary gap on outcome pricing dispute mechanics. Alex's operator credibility + buyer-side empathy = direct fit. F6 §7 nominates this as the highest-leverage Bet #1 wedge.
   - **Path: PUBLISH** the dual-telemetry / 30/60/90 dispute / third-party arbitration template; ADVISE.

3. **(4,M) + (9,M) + (12,M) — Procurement Playbook overlay on the M-column.** Trajectory observability for regulatorily-mandatory GTM use cases (TCPA, SOX, EU Art. 14).
   - **Why claimable:** The Playbook is half-written here (§III.5 Signed Reproducible Eval, §III.6 Article 14 Tie-Out). Standard-setting move.
   - **Path: PUBLISH** open spec + ADVISE Cloudflare/Kong/Vanta partners.

4. **(6,A + 12,F) — Operator role inside Hebbia or Rogo (NYC vertical-agent platform).**
   - **Why claimable:** F4 ranks Hebbia #1 (under-funded ratio + MBB feed-stock + Stripe-buyer + 0.20-0.40% equity + 2-quarter window before Series C). Rogo #3 (0.30-0.60% equity, banker-fluent gate). Alex's enterprise B2B + procurement profile = stronger than MBB candidates on execution depth.
   - **Path: JOIN** as VP Revenue / Head of GTM Strategy at Hebbia (Mehta-anchor team) or Rogo. 30-day MBB-network push opens pipeline directly.

5. **(11,I) operator role inside Sierra or Decagon — secondary to #4.**
   - **Why claimable:** Sierra Head Enterprise GTM East (Schmidt anchor + Taylor monthly NYC). F4 composite #2 (brand-prestige + cleanest secondary-liquidity).
   - **Path: JOIN** as Director Strategic Accounts / Head of Industry at Sierra; brand-prestige + secondary-liquidity wins over equity asymmetry.

6. **(9,G) advisory-partnership with Cloudflare MCP Gateway. OCQ 16/20 (gateway, C6 §3).**
   - **Why claimable:** Gateway advisory layer where Cloudflare needs procurement-fluent operator to close F100 with InfoSec/AI-Governance/Legal triad in 90 days.
   - **Path: ADVISE** Cloudflare; pair-with positioning is Bet #3 anchor.

7. **(7,J+M) — Trajectory-grade enablement coach for procurement-seam work.**
   - **Why claimable:** Adjacent to (9,G) Playbook; coach the work the Playbook teaches. Productize as a follow-on.
   - **Path: BUILD/ADVISE** as a follow-on after Playbook publish. Less critical than #1-6 but accident-of-light cell worth flagging.

**Pattern:** Alex's strongest claims cluster at the procurement seam ((9,G), (9,I), M-column, (11,I)) and at NYC vertical-agent operator roles ((6,A), (12,F), (11,I) via Sierra/Hebbia/Rogo). The 12yr-enterprise + procurement-scar-tissue + NYC profile is multiplicative at these cells. Outside this pattern (creative GUI ops, CS conversation handling, content marketing) Alex's claim is weaker.

---

## 7. Key Facts for Wave 2 Framework Agents

**Procurement seam (load-bearing).**
- (9,G) procurement-seam = **OCQ 19/20**, the through-line. Zero of seven overlays shipped turnkey May 2026. Article 14 enforcement late 2026. Playbook draft 9,700 words exists.
- (5,F) buying-committee mapping = **OCQ 18/20**, no incumbent owner. JTBD Job 1 gap = 7.
- (6,E) deal-diagnosis causation = **OCQ 17/20**. Gong sees activity, no one ships causation.
- Seven counterparties at F1000 (EA/IT is the seventh; Alex confirmed).
- Calendar-time floor: 16-24 weeks F1000 ready vendor; 32-52 weeks unprepared; 12-24 months regulated.
- 14 AI-specific contractual addenda are the modern buyer-side template (F5 §8).

**Pricing/economics.**
- ~22% inference cost at Sierra scale (token-markup math: $0.55 inference / $2.50 charged per resolved conv).
- Sierra $175M+ ARR Q1'26 at 400% YoY = only pure-outcome at-scale agent-GTM contract.
- Per-trajectory FinOps window 12-18 months before AWS Bedrock auto-routing bundles.
- Outcome pricing works where trajectory is discrete + completable + buyer-visible (CX yes; legal/finance/dev no).
- 4 pricing models live: per-seat (eroding), per-message (consolidating), outcome (Sierra thesis), hybrid (winning contract count).
- (12,H) forecasting AI lift bounded: 5-15% MAPE improvement honest; CRO commit accuracy 70-85% industry-wide.

**Cell-coverage / horizontal-vs-vertical (C6 verdict).**
- **Microsoft 365 Copilot for Sales OCQ ~18/20** — highest cell-coverage breadth in matrix. 30M+ paid seats Q1'26 = $5B+ ARR.
- **Salesforce Agentforce OCQ ~17/20** — every GTM cell M=1-12; AgentExchange Dec'25.
- **Glean OCQ ~17/20** — Network Economies vertical-bounded; $50M→$300M+ Q1'26.
- **Clay OCQ ~16/20** — only durable RevOps winner per 7 Powers; $80-110M ARR Q1'26.
- Verticals beat horizontals at cell level; incumbents beat both at suite level; gateways win the middle.

**NYC / talent / capital.**
- **Hebbia tops NYC composite ranking** (F4 §F4.7): under-funded ratio 2.5-5%, 0.20-0.40% equity, MBB+Stripe-flavored buyer, 2-quarter window before Series C.
- **MBB feed-stock activated Feb-Apr 2026** (Berger BCG→Hebbia Feb, Park McKinsey→Sierra Mar, Sinclair Bain→Harvey Apr). Third feed-stock confirmed.
- Foundation-lab-AE departure is the emerging fourth feed-stock (early Q2'26 LI clusters).
- Stripe→Sierra/Decagon dominant senior pattern; Stripe→Hebbia just opened (Mehta Mar'26 anchor).
- Equity-band 6-9 month window (Hebbia, Rogo, Augment most likely to reprice upward).
- Anthropic ARR Q3 2026 resolution is the single load-bearing valuation variable.

**Cruxes that move 12+ cells.**
- **C3 OSWorld 65%** (Q3 2026 expected) gates the entire K-column. Microsoft wins by default if it closes.
- **C5 memory absorbed vs niche-standalone** gates the entire L-column. Bet #5 anchors here.
- **C2 MCP forks vs holds** gates gateway-control-plane TAM (C6 §3).
- **Article 14 enforcement teeth vs paper-tiger** gates Bet #1 TAM (5x range).
- **Ironclad/Vanta AI-vendor-bundle Q4 2026** falsifies Bet #1 productized branch.

**Stratum density.**
- IX (vertical agent products) saturates ~85% of named cells.
- II (runtime), IV (memory), VII (eval/obs), VIII (safety) concentrate at K/L/M columns only.
- Bets #1, #4, #5 target the thin II/IV/VII/VIII slivers at K/L/M.

**Playbook-draft gap analysis (relative to Wave 1 findings).**
- **What's IN the draft:** Executive Foreword (5 reader-shaped openers), Section III all 7 overlays (Tool-Boundary, Indirect-Prompt-Injection, Action-Rollback, Sub-Agent Privilege, Signed Eval, Article 14 Tie-Out, Sectoral Overlays), Decision Tree 7 branches, Rubric outline, 38-term Glossary.
- **What's MISSING (Phase 5 reconciliation):**
  - Section II (Six Counterparties) chapters — F5 has 7 counterparty drafts ready to fold in; playbook TOC says six but Alex confirmed seven.
  - Section IV (14 AI-Specific Addenda) — F5 §8 has all 14 drafted (training-data, output ownership, model-update notice, hallucination indemnity, agent-action liability, sub-processor consent, kill-switch, eval-report sharing, red-team frequency, indirect-injection attestation, EU Art. 14, data residency, audit-log retention, sub-agent privilege-separation). Lift directly.
  - Section VI Rubric matrix population (56-cell × named vendor set) — Wave 2 work.
  - Outcome-pricing contract template (F6 §7 Implication 1: dual-telemetry, 30/60/90 dispute, third-party arbitration). MISSING from playbook entirely. Add as Section IV addendum or dedicated chapter.
  - Per-trajectory FinOps audit module (F6 §7 Implication 2). MISSING. Add as Section III.8 or Decision-Tree Branch.
  - Pricing-model-selection decision tree (F6 §7 Implication 3) — upstream of vendor-selection tree. MISSING.
  - The (7,J+M) trajectory-grade enablement-coach surface (C3 Top-5 #5). MISSING — flag for Phase 5 as accident-of-light finding.

---

*End synthesis. ~3,490 words. Ready for Wave 2 framework agents F1 Wardley, F2 Seven Powers, F3 JTBD.*
