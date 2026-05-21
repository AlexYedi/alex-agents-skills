# Wave 2 · F3 — Ecosystem-level Jobs-to-be-Done (GTM-org as customer)

**Date:** 2026-05-13 · **Method:** Ulwick ODI + Moesta struggling-moments, applied at the GTM-org scale (50–200 person revenue org, not the individual end-buyer). Input: wave1_synthesis.md + B7_ecosystem_jtbd.md (end-user-shape, do not duplicate). Coordinates use (Function #, Capability letter) per the 12×13 matrix.

---

## 1 · Framing — what makes the GTM org a non-standard JTBD customer

Classic ODI customers are individuals. The GTM org isn't one. It's a federation: a CRO who needs the number, a CFO who underwrites the unit economics, a CCO who owns the renewal book, a CMO who feeds the pipeline, a RevOps lead who instruments the whole apparatus, and a CRO–CFO–Board triangle that decides what gets funded. **Each of the five jobs below has a different counterparty inside the GTM org as the primary buyer, a different secondary blocker, and a different finance-line that pays for the agent.** That federation is the *real* customer. When an agent vendor wins, they win across at least two of those counterparties; when they lose, it is almost always one of those counterparties veto'ing on a job they didn't believe was theirs to fund.

Three structural consequences:

- **The "struggling moment" is calendar-bound.** GTM orgs don't shop continuously — they shop quarterly (Job 1), annually (Job 2), at planning (Job 3), at QBR (Job 4), at board prep (Job 5). Vendor pull is concentrated in 4–8 forcing-function weeks per year. Outside those windows the org is non-buying. Synthesis §7 calendar-time floor (16–24 weeks F1000-ready, 32–52 unprepared) interacts with this: a vendor not closed in the procurement window slips a full quarter, the equivalent of a 25% probability discount per slip.
- **The buyer is the counterparty who can blame the agent.** Synthesis flagged (12, "Strategy") as the largest matrix gap *because* a CRO can't blame an agent for a missed forecast — the accountability line caps agent autonomy at exactly the cell where the strategic JTBD lives. **Every job below has an accountability-line constraint that shapes which agent capability is purchasable vs theatrical.**
- **The GTM org consumes the matrix as bundles, not cells.** The 13 capabilities don't sell one-at-a-time at this scale; they sell as job-shaped bundles — Job 1 buys (4,A) + (5,F) + (6,A) + (6,E) + (9,G) as one motion-budget. F2's Seven Powers analysis should be read with this: cell-level cornered resource matters less than bundle-level switching costs.

---

## 2 · The five top-down jobs, restated

| # | Job | Owner | Co-buyer | Struggling moment (Moesta) | Annual budget line |
|---|---|---|---|---|---|
| **1** | "Hit the number this quarter." | CRO | VP Sales / VP Mktg | Mid-Q2 forecast call shows -$3M gap, 7 weeks to close. CRO triggers "buy something that compresses cycle by 20%". | Variable; comes out of next-Q hiring or contractor budget. |
| **2** | "Hit next year's number without doubling headcount." | CRO + CFO | VP Ops | November planning: target +40% ARR, hiring plan +15% heads. Math doesn't close. CFO refuses to fund the gap; CRO must find productivity. | FY plan capacity line. |
| **3** | "Reduce CAC payback period below 18 months." | CFO + CRO | Board | Series C diligence or annual board review: CAC payback at 22mo flagged as gating. Board demands a quarter-over-quarter improvement plan. | Sales & Marketing efficiency line. |
| **4** | "Increase NRR above 120%." | CCO + CRO | CFO | Customer-base revenue model shows churn-offset breaking new logo gains. NRR drift from 118 → 112 over 3 quarters; CCO's tenure depends on reversal. | CS budget + expansion-quota incentive line. |
| **5** | "Get the forecast right (±5%)." | CRO + Board | CFO | Two consecutive quarters of >10% miss vs commit. CFO loses board credibility; CRO under threat. Forecasting tooling reviewed, MAPE plateau at 8–12% (synth §7). | RevOps + analytics opex. |

These are the five jobs that survive the "is this really at GTM-org scale" test. B7's six jobs (back-office task, customer-facing conversation, code change, SaaS operation, stay current, procurement) are *end-user* JTBD — they describe what the *agent does*, not what the *GTM org buys the agent for*. F3 layers above B7 — the GTM org buys B7-Job-2 agents to satisfy F3-Job-4 (NRR). That hierarchy is the key reframe.

---

## 3 · 8-phase job maps with high-gap phases pulled out

For each job I name only the 2–3 highest-gap phases plus a one-line summary of the others. Gap-of-N is a 1–10 ODI proxy: 10 = critical unsolved at the GTM-org scale (not at the agent-tech scale).

### Job 1 · "Hit the number this quarter."

| Phase | Outcome (Ulwick-shape) | Cell(s) | Vendors today | Gap | Buyer |
|---|---|---|---|---|---|
| Define | Minimize time to convert quota gap → list of nameable, deal-stage-shifted actions. | (12,F) | Clari, Gong Deal Stories | 5 | VP Sales |
| **Locate** | **Minimize time to identify the right 9-person buying committee when prospect is F500 w/ 12+ months incumbent vendor history.** | **(5,F)** | Common Room, Sales Nav, ZoomInfo (static) | **8** | VP Sales + ABM lead |
| Prepare | Minimize time for AE to walk into Mtg #1 with research/MAP/causation context. | (6,A), (4,A) | Hebbia, Rogo, Glean, MS Sales Copilot, Clay | 6 | AE manager |
| **Confirm** | **Minimize time to diagnose *why* a $200K+ deal stalled @ stage 3, with causation not activity.** | **(6,E)** | Gong (activity only), Einstein (pattern), Aircover | **9** | AE + Sales Mgr |
| **Execute** | **Minimize calendar-time AE spends on the procurement-seam gauntlet for an in-quarter AI/agent vendor close.** | **(9,G)** | Loopio, Responsive, Arphie, Ironclad, Vanta | **10** | AE + Deal Desk |
| Monitor | Minimize MTTR when an at-risk deal slips committed-stage during the last 14 days of Q. | (6,H), (8,H) | Clari, BoostUp, Gong Forecast | 6 | RevOps + Sales Mgr |
| Modify | Minimize time to authorize discount/concession on a slipping deal w/ guardrails. | (6,I) | DealHub, SF CPQ Agentforce, Vendavo | 6 | Deal Desk |
| Conclude | Minimize re-key time when deal closes — signed evidence pack + CRM hygiene + commission-attribution. | (4,F), (8,F), (9,M) | Clay, Default, Galileo (eng-shape only) | 7 | RevOps |

**Top-3 highest-gap underserved outcomes for Job 1:**

1. **(9,G) — gap 10.** "Minimize calendar time the AE loses to InfoSec/Legal/AI-Governance/Procurement/Sponsor/EA/Privacy questionnaires when selling an agent into an F500 with no prior agent precedent." OCQ 19. Zero of seven overlays ship turnkey. This is the in-quarter cycle-compression lever. **Bet #1 anchor.**
2. **(6,E) — gap 9.** "Minimize time to causally diagnose why this specific $200K+ deal stalled at stage 3 (vs the org's stage-3 base rate)." Gong/Einstein give pattern-matching, not causation @ confidence. **Bet #1-adjacent operator-target** (Bet-C8 in synthesis §5).
3. **(5,F) — gap 8.** "Minimize time to identify the right 9-person buying committee when the prospect is an F500 with 12+ months of incumbent vendor history." No incumbent owner. **Bet-C1 anchor.** *Synthesis claimed gap=7; I am refining UP to 8 — the F500-with-incumbent qualifier doubles the gap vs the generic "build a committee map" framing.*

### Job 2 · "Hit next year's number without doubling headcount."

| Phase | Outcome | Cell(s) | Vendors | Gap | Buyer |
|---|---|---|---|---|---|
| Define | Minimize time to translate FY ARR target into rep-capacity model w/ AI lift assumption. | (12, Strategy), (8,H) | Pigment, Anaplan, Fullcast | 7 | CFO + RevOps |
| Locate | Minimize time to find which workflows are the productivity bottlenecks (per-AE, per-week). | (8,A), (6,L) | Clari, Gong, Glean | 6 | RevOps |
| **Prepare** | **Minimize calendar-time from "approve AI vendor" → "AE is operating it" inside the org.** | **(9,G), (7,J+M)** | Loopio + Highspot + MindTickle (not bundled) | **9** | RevOps + Enablement |
| Confirm | Minimize uncertainty that the AI-lift assumption in plan is empirically defensible. | (4,M), (6,M), (8,M) | Galileo, Braintrust (eng-shape) | 8 | CFO |
| **Execute** | **Maximize productive AE hours saved per quarter without degrading deal quality (no synthetic-SDR-style RR-negative trap).** | **(6,L), (4,B)** | Mem0/Letta/Zep (dev only), Outreach, Salesloft, Lavender | **9** | VP Sales |
| Monitor | Minimize MTTR when AI-augmented rep cohort underperforms vs non-augmented control. | (4,H), (7,J+M) | Clari rep insights, MindTickle Copilot | 7 | Sales Ops |
| Modify | Minimize time to re-tune which AI capabilities ship to which rep cohort. | (7,J+M), (8,K) | (gap) | 8 | Enablement |
| Conclude | Maximize % of productivity-gain hours converted into incremental pipeline (not idle slack). | (8,G) | Clari, BoostUp, Tomo | 7 | RevOps + VP Sales |

**Top-3 underserved outcomes for Job 2:**

1. **(6,L) — gap 9.** "Minimize the time an AE re-learns context on a 6–9 month deal cycle they touched 14 weeks ago." Mem0/Letta/Zep dev-only; nobody ships AE-shape. OCQ 16. **Bet #5 anchor; Bet-C9 the productized form.**
2. **(9,G) — gap 9 (for Job 2 specifically).** "Minimize the org's calendar-time from AI-vendor signature → first AE-productive use." Productivity job's procurement-seam variant: not cycle-compression for the *vendor's* in-quarter, but deployment-compression for the *buyer's* productivity-FY. **Same cell, different JTBD framing — see arbitration §6.**
3. **(7,J+M) — gap 8.** "Minimize time to certify a new AE on the procurement-seam work the Playbook describes (InfoSec answers, MSA redlines, Article 14 oversight)." OCQ 13. The single Wave 1 accident-of-light cell (only C3 surfaced it). **Bet-C2 anchor.**

### Job 3 · "Reduce CAC payback period below 18 months."

| Phase | Outcome | Cell(s) | Vendors | Gap | Buyer |
|---|---|---|---|---|---|
| Define | Minimize time to decompose CAC into segment × stage × channel contributions. | (12,F), (1,H) | Mosaic, Pigment, Clari spend optimizer | 5 | CFO |
| Locate | Minimize time to identify highest-CAC channels w/ AI-substitution candidates. | (1,A), (4,A) | 6sense, Demandbase, Clay | 6 | CMO + RevOps |
| **Prepare** | **Minimize blast-radius of pricing change when shifting from per-seat to outcome/hybrid w/ existing book.** | **(11,I), (9,I)** | Sierra (CX-only), Decagon, Intercom Fin | **9** | CFO + Pricing |
| Confirm | Minimize uncertainty in the post-substitution unit-economics model. | (8,M), (12,M) | Galileo, Arize (eng-shape) | 7 | FP&A |
| **Execute** | **Minimize the cost-per-acquired-account when swapping SDR FTE for synthetic-SDR + AE compression.** | **(4,B), (4,G), (4,M)** | 11x, AiSDR, Artisan (RR-negative trap) | **9** | VP Sales + CFO |
| Monitor | Minimize MTTR when CAC drifts vs forecast by channel. | (1,H), (12,F) | Mosaic, Anaplan, Clari | 6 | FP&A |
| Modify | Minimize time to reallocate spend across paid + agent + content. | (1,G), (1,H) | Marketo, HubSpot, 6sense Revenue AI | 6 | CMO |
| Conclude | Maximize % of CAC-payback improvement that holds 4+ quarters (not optical). | (11,L), (12,L) | (gap) | 8 | CFO + Board |

**Top-3 underserved outcomes for Job 3:**

1. **(11,I) — gap 9.** "Minimize the dispute risk of moving from per-seat to outcome/hybrid pricing without dual-telemetry and a 30/60/90 dispute mechanic." Sierra+Decagon+Intercom Fin all live, but procurement-side template not productized. **Bet-C4 anchor.**
2. **(4,B)/(4,G)/(4,M) trio — gap 9.** "Minimize the CAC-per-acquired-account when synthetic-SDR replaces FTE — without triggering the 11x reply-rate-negative ceiling." OCQ 14 at (4,M). Adverse-selection risk is the under-told story. **Bet #1 module + Bet #4 advisory.**
3. **(11,L)/(12,L) memory — gap 8.** "Maximize the % of CAC-payback improvement that survives 4 quarters of channel-mix churn." The L-column convergence: without persistent memory across the renewal/expansion motion, CAC improvements decay into ARR they could have captured. **Bet #5 / Bet-C9.**

### Job 4 · "Increase NRR above 120%."

| Phase | Outcome | Cell(s) | Vendors | Gap | Buyer |
|---|---|---|---|---|---|
| Define | Minimize time to convert "increase NRR" → cohort-shaped action list (logo retention vs expansion vs price). | (11,H) | Gainsight, ChurnZero, Catalyst | 6 | CCO |
| **Locate** | **Minimize time to find the renewal motion's slipping-customer signal before the AE notices.** | **(11,A), (10,E)** | Gainsight AI, Catalyst, Gong Account Plans | **8** | CSM Mgr |
| Prepare | Minimize time for CSM to enter QBR with full-cycle context + commitments-tracked. | (10,E), (11,E) | Granola, Read.ai, Gainsight | 7 | CSM |
| **Confirm** | **Minimize the % of expansion conversations where the CSM doesn't know what the customer was promised 9 months ago.** | **(11,L), (6,L)** | Sierra "Memory," Decagon Knowledge (RAG-over-store, not durable) | **10** | CCO + CSM |
| Execute | Maximize % of expansion plays that convert without slowing renewal. | (11,G) | SF Agentforce, Gainsight Renewal Center | 7 | CSM + AE |
| Monitor | Minimize MTTR on at-risk renewal — usage drop → CSM action. | (10,G), (11,H) | Sierra, Decagon, Gainsight | 7 | CSM Mgr |
| **Modify** | **Minimize the dispute cost when an outcome-priced agent under-delivers vs SLA, without losing the account.** | **(11,I)** | Sierra ($1-4/res), Hippocratic ($9/hr) | **8** | CCO + Procurement |
| Conclude | Maximize % of renewals that close with multi-year + auto-renew clauses. | (9,I), (11,I) | Ironclad, LinkSquares | 6 | Deal Desk |

**Top-3 underserved outcomes for Job 4:**

1. **(11,L) — gap 10.** "Minimize the % of expansion conversations where the CSM doesn't know what the customer was promised 9 months ago." Synthesis OCQ 14; arguably under-rated. The renewal-motion memory gap is the load-bearing NRR lever. **Bet #5 / Bet-C9 anchor.**
2. **(11,A) + (10,E) — gap 8.** "Minimize time from churn-signal to CSM-intervention with cohort-relative risk-ranking." Catalyst/Gainsight cover signal; nobody integrates with QBR pre-brief at CSM-shape resolution.
3. **(11,I) — gap 8.** "Minimize the dispute cost when an outcome-priced agent under-delivers vs SLA without losing the account." Different framing than Job 3 (which is *adoption* dispute risk; this is *operational SLA* dispute risk). **Bet-C4 doubles as a Job 4 lever.**

### Job 5 · "Get the forecast right (±5%)."

| Phase | Outcome | Cell(s) | Vendors | Gap | Buyer |
|---|---|---|---|---|---|
| Define | Minimize time to convert pipeline-coverage rule into commit-vs-upside-vs-best methodology. | (12,H), (8,H) | Clari, BoostUp, Aviso, SF Einstein | 6 | RevOps + CRO |
| Locate | Minimize time to surface every deal's signal-set across CRM + email + transcripts + product usage. | (12,F), (8,A) | Clari, Gong Deal Stories, Glean | 6 | RevOps |
| **Prepare** | **Minimize time for CRO to walk into board with explainable forecast deltas across 6+ quarters of decay.** | **(12,L), (12,F)** | BoostUp Forecasting Health, Mem0/Letta unadopted | **9** | CRO + Board |
| **Confirm** | **Minimize % of "committed" deals that miss based on a signal already in CRM 14+ days prior.** | **(6,E), (12,F), (12,M)** | Aircover, Gong, Galileo (eng-shape) | **9** | RevOps + Sales Mgr |
| Execute | Maximize MAPE improvement w/o introducing a "the AI missed it" accountability vacuum. | (12,H), (12, Strategy) | Clari, BoostUp, Aviso (5–15% MAPE plateau) | 7 | CRO + RevOps |
| Monitor | Minimize time-to-detect forecasting-agent drift (are the forecasts themselves degrading?). | (12,M) | Galileo, Arize, Coval | 7 | RevOps |
| Modify | Minimize re-tune time when a quarter's miss is post-mortemed into the model. | (12,I), (12,L) | (gap) | 8 | RevOps |
| **Conclude** | **Maximize CRO defensibility: produce an evidence pack the board accepts for any quarter outcome.** | **(12,M), (9,M)** | (gap) | **9** | CRO + Board |

**Top-3 underserved outcomes for Job 5:**

1. **(12,L) — gap 9.** "Minimize the time it takes the CRO to walk the board through 6+ quarters of forecast-miss decay attribution." Synthesis OCQ 13; Bet #5 anchor (Bet-C9 memory-as-service). **The forecast-miss-attribution memory is the load-bearing accountability artifact.**
2. **(6,E) read-through (12,F)/(12,M) — gap 9.** "Minimize the % of committed deals that miss based on a signal already in CRM 14+ days prior." Deal-diagnosis cell crosses into forecast accuracy because the same causation engine that diagnoses a stalled deal is what makes the forecast explainable post-hoc. **Bet-C8.**
3. **(12,M) Conclude — gap 9.** "Minimize the bespoke effort for the CRO to produce an evidence pack the board accepts for any quarter outcome." The Conclude phase across all 5 jobs is the matrix's softest tissue (B7 §Cross-job §1); at Job 5 it directly threats the CRO's tenure. **Bet #1's M-column overlay sells here.**

---

## 4 · The 15 highest-gap underserved outcomes (compiled)

| Job | Cell | Outcome (compressed) | Gap | Bet |
|---|---|---|---|---|
| 1 | (9,G) | F500 procurement-seam closes in-quarter | 10 | #1 |
| 1 | (6,E) | Deal-stall causal diagnosis | 9 | C8 |
| 1 | (5,F) | F500-w/-incumbent committee map | 8 | C1 |
| 2 | (6,L) | AE 6–9mo deal memory | 9 | #5 / C9 |
| 2 | (9,G) | Sig → AE-productive compression | 9 | #1 |
| 2 | (7,J+M) | Procurement-seam coach-grading | 8 | C2 |
| 3 | (11,I) | Outcome-pricing dispute template | 9 | C4 |
| 3 | (4,B)+(4,G)+(4,M) | Synthetic-SDR adverse-selection guardrail | 9 | #1 + #4 |
| 3 | (11,L)+(12,L) | CAC-improvement durability across renewals | 8 | #5 / C9 |
| 4 | (11,L) | CSM remembers 9-mo-old commitments | 10 | #5 / C9 |
| 4 | (11,A)+(10,E) | Churn-signal → cohort-ranked CSM action | 8 | C8 adj |
| 4 | (11,I) | Outcome-SLA dispute (operational) | 8 | C4 |
| 5 | (12,L) | 6Q forecast-decay board-explainability | 9 | #5 / C9 |
| 5 | (6,E)↔(12,F)/(12,M) | "CRM had the signal 14d prior" diagnosis | 9 | C8 + #1 |
| 5 | (12,M) | CRO board evidence-pack | 9 | #1 |

**Patterns visible in the 15:**

- **The L-column lights up at 3 of 5 jobs** (2, 4, 5) and is the *load-bearing* cell at Jobs 4 and 5. This validates synthesis §3's verdict: L is the matrix's most consistent gap. **Bet #5 is the single most JTBD-validated bet.**
- **(9,G) appears at both Jobs 1 and 2** — same cell, different JTBD framing. Job 1 = vendor-side cycle compression; Job 2 = buyer-side deployment compression. *Bet #1's playbook serves both — write the playbook with both framings.*
- **The M-column appears at Jobs 3, 4, 5 Conclude phases.** B7's "Conclude is universally underserved" applies sharply at GTM-org scale. Bet #1's M-column overlay is what makes the Playbook 5x.
- **(11,I) outcome-pricing dispute appears at Jobs 3 AND 4** (adoption vs SLA-operational). Bet-C4 is a two-job lever, increasing its TAM substantially.

---

## 5 · Three jobs where Alex's profile fits most directly

### Job 1 — "Hit the number this quarter."

**Why Alex.** 12 years carrying enterprise B2B SaaS quotas at Meltwater → Bazaarvoice/Curalate → Cohley → GKY meant he *lived* the in-quarter procurement-seam compression. At Cohley/Curalate the cycle-stretch from InfoSec/Legal/Privacy review on creator-content + first-party data was the actual quota-killer — not the demo, not the price. He has the operator scar tissue on every counterparty Wave 1 names. The Meltwater years gave him EU-data-residency exposure (Article 28 GDPR predecessor to Article 14); the Bazaarvoice years gave him retailer-procurement exposure (SOX-flavored cycles); Curalate/Cohley gave him creator-platform privacy exposure; GKY industrials gave him SOC2 + ISO27001 fluency at the manufacturing-IT seam.

**Bet served.** **Bet #1 (Procurement Playbook) primarily; Bet #6 (newsletter) as distribution.**

**Path.** **Publish.** The (9,G) Playbook is 9,700 words drafted; complete it + ship the open-spec Agent Procurement Rubric.

**90-day action.** Weeks 1–2: outline Playbook v1 against the Job-1 Locate/Confirm/Execute phase-row above (use F500-w/-incumbent qualifier as the framing prompt). Weeks 3–8: 30 expert interviews (RevOps + InfoSec + AI Governance leads at 10 F1000 buyers; 10 vendor-side leaders; 10 procurement/legal counterparties). Weeks 9–10: ship Playbook v1.0 + Agent Procurement Rubric (open spec). Weeks 11–12: drive 500 downloads, 50 inbound conversations via Bet #6 newsletter cross-pollination — falsifiability threshold for productized SaaS branch.

### Job 4 — "Increase NRR above 120%."

**Why Alex.** Bazaarvoice/Curalate was a renewal-motion business — UGC/influencer programs are renewal-renewal-renewal until the next platform-RFP cycle. Alex knows the CSM↔AE↔CCO triangle from inside. Cohley's contract structure (managed-service + platform) is the prototype hybrid-pricing motion Sierra is now exporting. The (11,L) "CSM doesn't remember 9-mo-old commitments" is something Alex has experienced as the AE on the *other side* of the table — promising what CS later forgot. That experiential authority is rare among the AI-builder cohort competing for these roles.

**Bet served.** **Bet #2 (vertical agent GTM role inside Sierra / Decagon / Gainsight-AI / Hippocratic) — specifically Sierra or Decagon where (11,L) + (11,I) live together.**

**Path.** **Join.** Sierra Head of Enterprise GTM East / Decagon Director Strategic Accounts. F4 ranks Sierra #2 NYC composite for prestige + secondary-liquidity; (11,L) + (11,I) are both the underserved outcomes Sierra is closest to publishing on internally.

**90-day action.** Weeks 1–4: complete Bet #1 Playbook v0.5 as a credibility artifact (signals procurement-seam fluency that beats MBB candidates on depth). Weeks 5–6: warm intros to Sierra (Schmidt anchor + Taylor monthly NYC) + Decagon (Mehta/Stripe-pipeline) via 5–8 second-degree connections from Stripe / Ramp / Datadog alumni network. Weeks 7–10: 4–6 conversations; lead each with a written "Here is how I would close the (11,L) memory-gap inside your existing roadmap by Q1 2027" memo. Weeks 11–12: close offer signature *before* Anthropic ARR resolution (Crux C1, Q3 2026) to lock pre-up-round equity band.

### Job 2 — "Hit next year's number without doubling headcount."

**Why Alex.** This is the job his GKY Industries chapter most directly addresses — industrials/manufacturing GTM teams running 6-quarter forecast horizons with hiring-budget compression. Alex has run the CFO-side of "we need 40% growth on 15% heads" — that's literally the operating math at GKY. The Bet #4 per-trajectory FinOps + Bet #1 procurement playbook bundle becomes a *one buyer, three products* practice — same CFO buys all three.

**Bet served.** **Bet #1 + Bet #4 + Bet #5 as a bundled advisory practice** ("Enterprise AI Architecture + Procurement + FinOps Audit").

**Path.** **Advise.** Independent operator-shape advisory, monetized via the Playbook + 4-week FinOps audits + RAG/memory architecture audits.

**90-day action.** Weeks 1–2: scope the 3-product bundle pricing ($25K Playbook engagement, $40K FinOps audit, $40K RAG/memory audit — anchor on the Vanta SOC2 readiness pattern, F500 line-item-comfortable). Weeks 3–6: 5 free-first-audit offers via the Bet #6 newsletter + LinkedIn outbound to F1000 RevOps + CFO leads at $50M+ AI-spend companies. Weeks 7–10: convert 2 to paid Phase 1; document as 1 anonymized case-study + 1 named. Weeks 11–12: re-decide — if 2 conversions land at >$50K combined ACV, scale; if not, fold Bet #4 module into Bet #1 advisory and de-prioritize standalone.

---

## 6 · Arbitration of the seven cross-Wave-1 JTBD questions

**Q1 — Is (5,F) buying-committee mapping Job 1's biggest gap (gap=7 per synthesis)?** **Refine UP, but not to #1.** Job 1's biggest gap is **(9,G) procurement-seam at gap 10.** (5,F) is real and unsolved (gap 8 with the F500-w/-incumbent qualifier), but the cycle-time cost of bad committee-mapping is 2–4 weeks; the cycle-time cost of unprepared procurement-seam navigation is 6–24 weeks (synth §7). The latter is the bigger gap-of-N at GTM-org scale.

**Q2 — Is (9,G) Job 2's biggest gap or Job 1's?** **Both, in different framings.** Job 1 frames (9,G) as *vendor-side cycle compression* — close the deal in-quarter. Job 2 frames (9,G) as *buyer-side deployment compression* — signature-to-productive-use compression. The cell is the same; the JTBD is different. **Bet #1's playbook should be written with both framings explicit.** Sequence-wise the *Job 1 framing pulls harder* — vendors have variable quarterly budget for cycle compression; buyers' deployment-compression budget is fixed planning-cycle and slower to release. Sell Job 1 first, expand to Job 2 in chapter 2.

**Q3 — Does (6,L) persistent AE memory serve Job 2 (productivity) or Job 5 (forecast)?** **Job 2 primarily; Job 5 secondarily through the (12,L) read-through.** The AE-memory product satisfies the productivity job because AE re-context cost is the biggest per-rep productivity tax. Forecasting benefits *downstream* — better-remembered deals are better-forecasted deals — but that's a second-order benefit not a primary JTBD. **The buyer for (6,L) is VP Sales (Job 2 owner), not RevOps (Job 5 owner).** Build the product for the AE; sell to the VP Sales; *bonus-sell* to RevOps as forecast accuracy improvement.

**Q4 — Does (11,I) outcome-pricing playbook serve Job 4 (NRR) or Job 3 (CAC payback)?** **Both, with different counterparties.** Job 3 framing: outcome-pricing reduces CAC payback because per-outcome billing scales linearly w/ value delivered → CFO buys the *adoption-risk* template. Job 4 framing: outcome-pricing introduces NRR risk if SLAs disputes erode renewal trust → CCO buys the *operational-SLA-dispute* template. **Two distinct buyers, two distinct chapter framings, one shared productized template.** Bet-C4's productization fork: dual-telemetry + 30/60/90 dispute mechanic + third-party arbitration applies to both; the *narratives* differ.

**Q5 — Does (7,J+M) trajectory-grade procurement-seam coaching serve Job 2 (ramp curve) or Job 1 (close rate)?** **Job 2 — the ramp curve.** Job 1 close-rate is about the AE who is already procurement-fluent; coaching doesn't compress *this quarter's* deal. Job 2 ramp-curve compression *is* the JTBD: get a new AE certified on procurement-seam work in 12 weeks not 28. The forcing-function is FY hiring-budget compression — Job 2's struggling-moment is "you're hiring 8 AEs, they ramp at 7 months, you need them at 3.5." Bet-C2 is the productized form. Buyer: VP Enablement → reports to VP Sales → Job 2 owner.

**Q6 — Common Room: Bet #2 join target (Alex inside) or (5,F) building block (someone else builds on top)?** **Both can be true; resolved by sequencing.** Common Room at $30M ARR + Series C $250M val + community-signal-only is *too narrow* a single-product moat to be the durable (5,F) winner standalone. Either (a) Common Room expands into multi-source fusion themselves and becomes a credible (5,F) winner, in which case Bet #2 join makes sense for Alex (12–18 month window); OR (b) someone else builds (5,F) on top, and Common Room becomes input — in which case Alex's better play is the builder-side Bet-C1 (probably operator-advisor inside a (5,F)-shape startup not yet named). **The Common Room roadmap reveal in next 2 quarters is the decidability event.** Default position: prefer Common Room join (lower-risk) over speculative (5,F) builder bet.

**Q7 — Hebbia (#1 F4 composite) vs MS 365 Copilot (#1 C6 cell-coverage) — which serves Alex's career JTBD better?** **Hebbia, for Alex.** This is a JTBD question about Alex's own career — what's the struggling moment he's solving? It's *equity-asymmetry-with-operator-credibility* on a 5-7 year horizon, not *cell-coverage authority* on a 12-month horizon. Microsoft 365 Copilot wins the matrix at suite level; Alex inside Microsoft is a senior IC seat with no equity asymmetry. Hebbia at 2.5–5% under-funded ratio + 0.20–0.40% equity + Mehta/Stripe-anchored team + MBB-feedstock + NYC = 5x asymmetric upside relative to MS. The cell-coverage authority of Microsoft is the *market truth*; Hebbia is the *Alex truth*. They don't contradict — different JTBDs at different scales.

---

## 7 · Implications — which bet does JTBD validate, threaten, surface?

**JTBD most-validates: Bet #5 (memory architecture as service line).** L-column lights up at 3 of 5 jobs and is the load-bearing cell at Jobs 4 and 5. (11,L) NRR memory is gap 10; (12,L) forecast-decay memory is gap 9; (6,L) AE memory is gap 9. Bet-C9 (memory-as-service) is the productized form. **No other bet draws the same density of JTBD pull across the five-job map.** Sequence: Bet #1 ships first as planned (90-day publish), but Bet #5 should be the *next* productization wedge — Q3 2026 priority — not a folded sub-line.

**JTBD most-threatens: Bet #6 (newsletter as standalone).** B7 §Cross-job §1 named "Conclude phase universally unserved." At GTM-org scale, Conclude is the CRO/CFO/Board-readiness phase across all 5 jobs. The newsletter doesn't *close* a Conclude gap — it sits at Job 5 (stay current in B7 framing, not the F3 Job 5 forecast job). **Bet #6 has lower JTBD-pull than implied in the tracker.** Recommendation: explicit reframe of Bet #6 as Bet #1 distribution layer — not standalone justifiable on its own merits.

**JTBD-surfaces new bet: Bet-C8 (Deal-Diagnosis Causation Engine, cell 6,E).** Appears at Job 1 (gap 9) AND Job 5 (gap 9, via the (6,E)↔(12,F) read-through). Two-job cell at gap 9 = high JTBD compounding. Synthesis §5 listed Bet-C8 as a watch-target with "LOW for Alex operator path (technical product)." JTBD says: **the operator path inside a (6,E) startup is more attractive than synthesis implied** — if a credible (6,E) startup emerges in NYC over the next 2 quarters, it joins Hebbia/Rogo/Sierra on the Bet #2 target list at a similar tier. Watchlist add: Aircover (closest attempt — synth (6,D)), or any AI-Gong-spinout in NYC.

**Cross-bet through-line.** Bet #1 *publishes* the Playbook → Bet #5 *productizes* the memory-architecture-as-service practice → Bet-C4 *templates* the outcome-pricing dispute mechanic → Bet-C8 *operator-watches* the causation-engine startup. Each compounds JTBD validation for the next. **The structural finding of F3:** the GTM org is not buying agents; it's buying procurement-fluent + memory-durable + outcome-defensible + causation-explainable substrate that lets the CRO/CFO/CCO/Board defend the number. Alex's commercial fluency lands directly on three of the five jobs (1, 4, 2), and the procurement-seam he carries from 12 years of enterprise B2B is the single multiplier that turns his profile from one-of-many enterprise AE to rare-on-the-market.

---

*End F3 JTBD. ~2,790 words. Strong opinions weakly held; the 30-expert-interview Bet #1 plan is the falsification mechanism for every gap-of-N score above.*
