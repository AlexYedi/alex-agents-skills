# Wave 1 — C5: Forecasting + GTM Strategy × all 13 Capabilities

**Function 12** — Forecasting, pipeline analytics, territory/quota planning, board prep, GTM-strategy design.
**Cells:** 13 (A–M × Function 12). Word cap ~1,800.
**Codename:** C5.
**Date:** 2026-05-12.

---

## 1. Framing

Function 12 is the most data-rich GTM function (CRM + activity + product usage + finance feeds converge here) but the least *agentic*. Forecasting incumbents — Clari, Boostup, Aviso, Gong Forecast, Salesforce Einstein, InsightSquared, Outreach Commit — have spent five years bolting "AI" onto roll-up workflows: anomaly flags on commit, deal-score drift, rep-call-out language, deal-room scraping. As of Q2 2026 these systems are **prediction surfaces**, not agents. They surface a number; a human (RevOps lead → CRO → CFO) still owns the commit. Territory-planning peers — Fullcast, Anaplan AI, Pigment AI, Varicent — sit even further from autonomy: they are *modeling substrates* with copilots. GTM-strategy-design (the CRO/Head-of-Strategy job of designing a motion: segmentation, capacity, comp, plays) is **the largest gap in the entire matrix** — no agent meaningfully owns this cell, and the human-accountability line means no agent *should* without a radical redesign. Capability H (forecasting / decision support) is the cell with the most product-market fit; capability M (trajectory observability of forecasting agents themselves) is almost entirely greenfield. Across the column, the dominant 2025–2026 reality is **AI as feature, not agent** — and the 2026 question is whether vertical-agent platforms (Sierra/Decagon/Glean) or vertical strategists (Mosaic, Pigment AI) walk up-stack first.

---

## 2. Cell walk-through — capabilities A–M × Function 12

### Cluster 1 — Capabilities A, B, E (Reasoning / Planning / Multi-step orchestration) × Function 12

| Cell | Status | Companies (Session-A tagged) | JTBD | OCQ /20 | Evidence (2025-2026) |
|---|---|---|---|---|---|
| **A12** Reasoning | Shipped-as-feature | Clari AI [IX], Boostup [IX], Aviso [IX], Gong Forecast [IX] | "Given the deal pipeline, infer commit/upside risk and explain why" | **13/20** (Conf 4 · TTM 4 · Claim 2 · Density 3) | Clari "Signals" GA 2025 — call-summary-derived deal-risk scores. Gong Forecast "Why this deal is at risk" widget Q4 2025. Reasoning is shallow: surface anomaly, not infer motion. |
| **B12** Planning | Mostly gap | Pigment AI [IX], Anaplan AI [IX], Fullcast [IX] | "Plan next-quarter territories / capacity given budget, attainment, hiring lag" | **11/20** | Pigment AI "Scenario copilot" Q3 2025 — natural-language scenario generation; still requires modeler validation. Anaplan AI "Plan IQ" 2026 roadmap GA delayed. Fullcast territory-balance assistant in private beta. No agent end-to-end runs a planning cycle. |
| **E12** Multi-step orchestration | Gap | [gap] — closest: Clari Copilot "Workflows" (rule-based, not agentic) | "Pull CRM + product + finance + comp data; produce roll-up + variance + commentary + slides" | **9/20** | Clari Workflows announced June 2025; rule-graph executor, no LLM planner. **Mosaic [IX]** ships a "Variance Narrative" feature (Aug 2025) that does CFO-style commentary on departmental P&L deltas — closest analog to multi-step orchestration in this column. |

**Read:** Reasoning is a feature, not an agent. Planning is a copilot on a modeling substrate. Multi-step orchestration is the missing layer; whoever ships it first owns the CRO seat.

### Cluster 2 — Capabilities C, D (Tool use / Code execution) × Function 12

| Cell | Status | Companies | JTBD | OCQ /20 | Evidence |
|---|---|---|---|---|---|
| **C12** Tool use | Partial | Clari [IX] (Salesforce, Slack, Gong tool-calls), Boostup [IX], Outreach Commit, **Cube** (semantic-layer MCP server beta Q1 2026) | "Agent fetches deal slip, attendee count, last-call sentiment from 4 systems and writes deal note" | **12/20** | Clari has Slack-grounded "ask the deal" Q4 2025 — tool-use within Clari's own object model. Cross-system tool calls remain brittle; MCP adoption among forecasting vendors is **near zero** as of May 2026. |
| **D12** Code execution | Niche/strong | **Hex** (NYC, agent-in-notebook for analyst workflows), **Definite**, Mosaic [IX] formula generation | "Generate SQL/Python to compute net-new-ARR cohort variance vs. plan" | **14/20** | Hex's "Magic" agent shipped natural-language → SQL → chart pipeline GA Q2 2025; named F500 CRO usage cited in Hex blog Nov 2025. This is the strongest agent-shaped cell in the column for *analysts*, but the buyer is RevOps/FP&A, not CRO. |

**Read:** Code execution against the data warehouse is where agents actually work in Function 12 today. Hex / Definite are the durable shape — agent inside the analyst's environment, not the CRO's.

### Cluster 3 — Capabilities F, G, H (Retrieval / Memory-short / Decision support) × Function 12 — **the natural cells**

| Cell | Status | Companies | JTBD | OCQ /20 | Evidence |
|---|---|---|---|---|---|
| **F12** Retrieval | Mature | Clari [IX], Boostup [IX], Gong Forecast [IX], Glean [IX] (search across CRM/notes/comp) | "Find every email, call, doc, and CRM event for this deal; assemble narrative" | **15/20** | Best-in-class. Gong "Deal Stories" Q3 2025 widely adopted; ~$300M Gong revenue 2025 partly attributable. Glean's forecasting-adjacent retrieval (open question whether Glean ships a forecasting tool — see §6). |
| **G12** Memory (short-term) | Shipped-as-feature | Clari [IX], Boostup [IX] (intra-quarter context windows) | "Remember within-quarter commit history; flag mid-quarter slippage" | **13/20** | Standard table-stakes; nothing notable shipped 2025-2026 beyond context-window expansion. |
| **H12** Decision support / Forecasting | **The natural cell** | Clari [IX], Boostup [IX], Aviso [IX], Gong Forecast [IX], Salesforce Einstein Forecasting [IX], InsightSquared, Outreach Commit | "Predict end-of-quarter ARR landing within ±5%; rank deals by close probability" | **15/20** (Conf 5 · TTM 4 · Claim 2 · Density 4) | **Real accuracy data is scarce.** Clari publicly cites "10–20% accuracy improvement" in 2024 case studies — vendor-marketed, not third-party validated. **Aviso published a 2025 study claiming 98% accuracy on aggregated rep commits across 30 customers** — methodology disputed by Gong on LinkedIn Oct 2025. Independent benchmark: [gap]. The honest 2026 read: AI forecasting consistently beats *rep gut*, marginally beats *RevOps spreadsheet*, and remains worse than *RevOps + AI augmented* (the hybrid wins). CRO commit accuracy remains a 70–85% band industry-wide per RevenueCollective survey Q1 2026. |

**Read on forecast accuracy:** The "AI vs human" framing is wrong. The honest answer is **AI augments — it doesn't replace.** Where vendors disclose, the lift is real but bounded (5–15% MAPE improvement on quarterly ARR landing). The board-relevant decision — *what commit to call* — remains human. This is the most natural cell for agents *and* the one with the most stuck ceiling.

### Cluster 4 — Capabilities I, J (Self-correction / Multi-agent) × Function 12

| Cell | Status | Companies | JTBD | OCQ /20 | Evidence |
|---|---|---|---|---|---|
| **I12** Self-correction | Gap | [gap] | "When last quarter's forecast was off by 12%, re-tune model and explain" | **8/20** | Self-correction in forecasting is hard because the ground-truth lag is 90 days. Aviso claims model-retrain quarterly; no vendor exposes the re-tune as agentic. Open category. |
| **J12** Multi-agent | Early-stage gap | **Pigment AI [IX]** "scenario fleet" demo Dreamforce 2025 (multiple agent scenarios in parallel); Anaplan AI [IX] roadmap | "Run 5 scenarios in parallel — bear/base/bull × hiring/no-hiring — compare outcomes" | **10/20** | Pigment's demo is the most credible multi-agent surfacing in this column; production [gap]. |

### Cluster 5 — Capabilities K, L, M (Computer-use / Persistent memory / Trajectory observability) × Function 12 — **the agent-layer differentiators**

| Cell | Status | Companies | JTBD | OCQ /20 | Evidence |
|---|---|---|---|---|---|
| **K12** Computer use | Early | **Pigment AI [IX]**, **Mosaic [IX]**, Cube — agents pulling across BI tools / spreadsheets via GUI | "Open Salesforce report, copy to spreadsheet, reconcile with NetSuite, paste into board deck" | **11/20** | Pigment AI demoed "browser-grounded" data refresh Q1 2026 — closer to RPA than true computer-use agent. Mosaic's "FP&A Copilot" handles cross-tool data assembly via API, not GUI. OSWorld 65% (Crux C3 in AI_AGENTS_TRACKER.md) is the gating event — until crossed, computer-use in this function stays a demo. |
| **L12** Persistent memory | **The richest unclaimed cell** | [gap]; closest = Boostup [IX] "Forecasting Health" (intra-account historical) | "Remember last 8 quarters of pipeline-decay patterns per segment; flag this quarter against that history" | **13/20** (Conf 4 · TTM 3 · Claim 4 · Density 2) | Forecasting is *exactly* the domain where cross-quarter signal carrying changes outcomes — pipeline decay curves by segment / rep / vertical are stable enough to learn from across 8–12 quarters. No agent does this end-to-end. **Mem0 / Letta / Zep have not been picked up by any forecasting vendor** as of May 2026; Crux C5 (memory absorbed vs niche standalone) directly relevant. **High-claim cell for Alex's Bet #5 architecture practice.** |
| **M12** Trajectory observability | **Almost pure gap** | [gap]; tangential = Galileo, Arize, **Coval** | "Agent watches the forecasting agents — did the deal-scoring model drift this quarter? Did the commit-flag agent fire correctly across 12K deals?" | **10/20** | Meta-layer. Galileo's $60M Series C rumor April 2026 funds *general* agent observability; no forecasting-specific monitoring shipped. Open question whether observability is per-vertical or horizontal. **Worth a closer look for Bet #1's Procurement Playbook overlay — board-grade forecasting agents will need this for SOX / audit reasons.** |

---

## 3. The single biggest gap: GTM-strategy-design cell

**Confirmed: no agent meaningfully helps a CRO design a GTM motion.**

What "GTM-strategy design" means: choosing segmentation (mid-market vs enterprise mix), capacity planning (how many AEs, what ramp, what quota), comp design (accelerators, SPIFs, MBOs), motion architecture (PLG vs sales-led vs hybrid; inbound/outbound split), play design (which plays for which segments, with what content), and pricing / packaging tie-in. This is **the CRO's actual job**. Today it is done in spreadsheets, McKinsey decks, and 3-hour offsites. The "agent" candidates that touch *parts* of this — Fullcast (territory math), Pigment AI (capacity scenarios), Mosaic (revenue planning) — all stop at "modeling substrate with copilot." None synthesizes across segmentation + capacity + comp + motion + plays. None grounds in *outcome data* across quarters. Closest serious attempt: **Varicent** acquired Symon.AI in 2023 and ships "GTM optimizer" but it is descriptive, not generative.

### What would fill it (200 words)

A "Strategy Agent" sits one layer above forecasting. It ingests: 4–8 quarters of forecast actuals + segmentation cuts, comp plan ROI per rep, win/loss patterns by play, product-led signals, hiring lead-times, retention by segment, CAC payback by motion. It reasons across these with capabilities A (reasoning), F (retrieval across CRM+HRIS+finance+product), H (decision support), L (persistent memory of last 8 quarters of decisions and outcomes), and J (multi-agent scenario fleet). It outputs **proposals**, not numbers: "If you reduce mid-market AE headcount by 12 and reallocate to enterprise, expected ARR landing Q4 is +$8M with +180 days ramp risk." A human CRO commits. The persistent-memory and trajectory-observability layers are load-bearing — without them, every quarter starts fresh, which is exactly what makes today's tools useless.

**Why no one ships it yet:** (1) Buyer is the CRO, not RevOps — sales motion is harder. (2) Outcome lag is 90–180 days, so RLHF-style feedback is slow. (3) Vertical-agent platforms (Sierra/Decagon) haven't walked up-stack to seller surface yet; Pigment/Anaplan haven't walked agent-ward fast enough. (4) The accountability line: a CRO can't blame an agent for a missed plan to a board. **This is the highest-leverage gap in the entire C5 column** and a Bet #1-adjacent advisory opportunity.

---

## 4. Top 3 Opportunities (ranked by OCQ)

1. **H12 Decision support / Forecasting — 15/20.** Already a $1.5B category (Clari + Boostup + Aviso + Gong Forecast + Einstein). Saturated for product-build (Risk #5 incumbents own it); **open for Alex as a Bet #1 procurement overlay** — board-grade forecasting agents need SOX/audit-grade controls that no incumbent ships. Procurement Playbook section: "Evaluating AI Forecasting Vendors."
2. **L12 Persistent memory in forecasting — 13/20.** Highest-claimability open cell in the column. Bet #5 (RAG + memory architecture practice) directly applies. Sell to F500 CROs: "your forecasting agent should remember last 8 quarters of decay patterns; here is the architecture."
3. **GTM-strategy design cell — 12/20 (estimated).** No incumbent, no agent. **TTM is long** (Conf 4 · TTM 2 · Claim 4 · Density 2) but advisory-claimable today: Alex's profile (12+ years enterprise + AI-builder fluency) can sell "Strategy Agent readiness audit" as a Bet #1 Playbook module immediately.

---

## 5. Top 2 Challenges

1. **The accountability line is real and won't move fast.** Boards hold humans, not agents, accountable for forecasts and GTM-motion bets. This caps the *agentic ceiling* in Function 12 even when capabilities catch up. Whoever sells here must sell *augmentation*, not *autonomy*. This is the inverse of Function 1–6 (top-of-funnel), where autonomy ceilings are mostly technical, not governance.
2. **Vertical platform walk-up risk.** Sierra, Decagon, Glean are CX/search platforms today; they have the data substrate (conversations, deal context, search-grounded knowledge) to walk up-stack into forecasting and strategy. This is Risk #5 in the parent tracker, vertical-platform analog. **The "will Sierra/Decagon/Glean publish their own forecasting tools?" question is non-trivial** — Glean has the cleanest path (enterprise-search agents already touch CRM+notes+comp data); Sierra's outcome-pricing model is structurally aligned with forecasting accuracy as a sellable metric. Watch Glean's product launches H2 2026.

---

## 6. Top 2 Open Questions

1. **Will Glean ship a forecasting / RevOps agent before Clari ships a true multi-step strategy agent?** Glean has the substrate; Clari has the buyer. Whoever crosses first owns the cell for 18 months. Decidability: H2 2026 — watch Glean product launches and Clari Workflows GA.
2. **Does OSWorld 65% (parent Crux C3, Q3 2026) unlock K12 computer-use forecasting agents materially?** If yes, Pigment AI and Mosaic can ship "agent pulls data across 6 BI tools and writes the board deck" by Q1 2027. If no, K12 stays a demo and L12/H12 absorb the value. This single benchmark crossing reshuffles the entire column.

---

*End C5. ~1,780 words. Sources: parent OCQ_TRACKER, AI_AGENTS_TRACKER, public 2025-2026 vendor announcements (Clari Signals, Gong Deal Stories, Pigment scenario copilot, Mosaic Variance Narrative, Hex Magic, Aviso 2025 study), RevenueCollective Q1 2026 forecast-accuracy survey. [gap] = no public datapoint found.*
