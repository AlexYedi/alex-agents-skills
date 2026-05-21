# AGENTS × GTM — Decisions Addendum · Part B (Parts X–XIII)

> Companion to Part A of the Volume IV Addendum. Voice: Alex Yedi, May 13, 2026. Reader: Alex twelve months from now, who needs to act on this, not admire it.

---

## Part X · Ecosystem JTBD applied to the GTM Org

### X.1 — The GTM org is a federation, not a person

Five jobs survive the "is this really at GTM-org scale" test. Each has a different owner inside the GTM federation, a different secondary buyer, a different finance-line, and — most importantly — a different counterparty who can blame the agent if it underperforms. The accountability line is what caps autonomy. The 13 capabilities don't get bought one at a time at this scale; they get bought as job-shaped bundles, which is why the 7 Powers screen reads better at bundle-level switching costs than at cell-level cornered resource.

Three structural things to keep in mind before reading the five jobs:

- **The struggling moment is calendar-bound.** GTM orgs shop in 4–8 forcing-function weeks a year, not continuously: quarterly (Job 1), annually (Job 2), at planning (Job 3), at QBR (Job 4), at board prep (Job 5). The 16–24 week F1000-ready procurement floor (synthesis §7) interacts with this — miss the window, slip a full quarter, eat a 25% probability discount per slip.
- **The buyer is the counterparty who can blame the agent.** Cell (12, "Strategy") is the largest gap in the matrix because no CRO can blame an agent for a missed forecast. That accountability cap is the design constraint behind every purchasable agent capability at GTM-org scale.
- **Capabilities sell as bundles.** Job 1 buys (4,A) + (5,F) + (6,A) + (6,E) + (9,G) as one motion-budget. F2's Power screen should be read at bundle level: cornered resource at the cell matters less than switching costs at the bundle.

### X.2 — The five jobs

| # | Job | Owner | Co-buyer | Struggling moment | Budget line |
|---|---|---|---|---|---|
| **1** | Hit the number this quarter | CRO | VP Sales / VP Mktg | Mid-Q2 forecast call shows -$3M gap, 7 weeks to close — CRO greenlights "buy something that compresses cycle 20%" | Variable; out of next-Q hiring or contractor budget |
| **2** | Hit next year's number without doubling headcount | CRO + CFO | VP Ops | Nov planning: +40% ARR target, +15% hiring plan, math doesn't close — CFO refuses to fund the gap, CRO must find productivity | FY plan capacity line |
| **3** | Reduce CAC payback period below 18 months | CFO + CRO | Board | Series C diligence or annual board review: CAC payback at 22 months flagged as gating; board demands quarterly improvement | Sales & Marketing efficiency line |
| **4** | Increase NRR above 120% | CCO + CRO | CFO | Customer-base revenue model shows churn-offset breaking new-logo gains; NRR drift 118 → 112 over three quarters; CCO's tenure depends on reversal | CS budget + expansion-quota incentive line |
| **5** | Get the forecast right (±5%) | CRO + Board | CFO | Two consecutive quarters of >10% miss vs commit; CFO loses board credibility, CRO under threat; forecasting tooling reviewed — MAPE plateau at 8–12% | RevOps + analytics opex |

The B7 end-user JTBD list (back-office task, customer-facing conversation, code change, SaaS operation, stay current, procurement) describes what an agent *does*. The F3 list above describes what a GTM org *buys an agent for*. The hierarchy is: GTM org buys a B7-Job-2 agent (customer-facing conversation) to satisfy an F3-Job-4 (NRR). Conflating those scales is the most common error in vendor narratives — and it is why $5/conversation Sierra pricing reads cleanly to the CFO but the Sierra retention story doesn't. Different jobs, different accountabilities, different proofs.

### X.3 — The 15 highest-gap underserved outcomes

Compiled from the five 8-phase job maps (see wave2_F3_jtbd.md §3 for the full maps). Gap-of-N is the ODI 1–10 proxy at GTM-org scale, not agent-tech scale.

| Job | Cell | Outcome (compressed) | Gap | Bet anchor |
|---|---|---|---|---|
| 1 | (9,G) | F500 procurement-seam closes in-quarter | **10** | #1 |
| 1 | (6,E) | Deal-stall causal diagnosis | 9 | C8 watch |
| 1 | (5,F) | F500-with-incumbent committee map | 8 | C1/C5 |
| 2 | (6,L) | AE 6–9 month deal-cycle memory | 9 | #5 / C9 |
| 2 | (9,G) | Signature → AE-productive compression | 9 | #1 |
| 2 | (7,J+M) | Procurement-seam coach-grading | 8 | C2 |
| 3 | (11,I) | Outcome-pricing dispute template | 9 | C4 → #1 |
| 3 | (4,B)+(4,G)+(4,M) | Synthetic-SDR adverse-selection guardrail | 9 | #1 + #4 |
| 3 | (11,L)+(12,L) | CAC-improvement durability across renewals | 8 | #5 / C9 |
| 4 | (11,L) | CSM remembers 9-mo-old commitments | **10** | #5 / C9 |
| 4 | (11,A)+(10,E) | Churn-signal → cohort-ranked CSM action | 8 | C8-adj |
| 4 | (11,I) | Outcome-SLA operational dispute | 8 | C4 → #1 |
| 5 | (12,L) | 6-quarter forecast-decay board-explainability | 9 | #5 / C9 |
| 5 | (6,E)↔(12,F)/(12,M) | "CRM had the signal 14 days prior" diagnosis | 9 | C8 + #1 |
| 5 | (12,M) | CRO board evidence-pack | 9 | #1 |

Patterns worth holding onto:

- **The L-column lights up at 3 of 5 jobs and is load-bearing at Jobs 4 and 5.** Persistent memory is the single most JTBD-validated investment surface in the matrix. Bet #5 (memory architecture) is the single most-validated bet; Bet-C9 (Persistent Memory as Service Line) is the productized form once the Playbook has earned trust.
- **(9,G) appears at Jobs 1 and 2 in two different framings.** Job 1 = vendor-side cycle compression. Job 2 = buyer-side deployment compression. Same cell, two narrative chapters. The Playbook should be written with both framings explicit because they appeal to different counterparties on the same buyer-side: VP Sales (Job 1) and VP Ops/CFO (Job 2).
- **The M-column appears at Jobs 3, 4, 5 Conclude phases.** B7's "Conclude is universally underserved" applies sharply at GTM-org scale: the CRO/CFO/Board-readiness phase across all five jobs is where the Playbook's M-column overlay sells 5× harder than at any other phase.
- **(11,I) outcome-pricing dispute is a two-job lever.** Job 3 frames it as CAC-payback adoption risk (CFO buys). Job 4 frames it as operational SLA dispute (CCO buys). Bet-C4 productizes a single template that lands across two different counterparties — that's how it earns its way into Bet #1 as a chapter rather than as a separate consulting service.

### X.4 — Three jobs where Alex's profile fits most directly

**Job 1 — Hit the number this quarter.** Twelve years carrying enterprise B2B quotas at Meltwater → Bazaarvoice/Curalate → Cohley → GKY Industries is the in-quarter procurement-seam compression résumé. The cycle-stretch from InfoSec/Legal/Privacy review at Cohley on creator-content and first-party data was the actual quota-killer — not the demo, not the price. Bet served: **Bet #1 (Procurement Playbook) primarily; Bet #6 (newsletter) as distribution.** Path: **PUBLISH**. The 9,700-word Playbook draft is already two-thirds of the way to a v1 publishable artifact; the missing modules are the outcome-pricing template, the per-trajectory FinOps audit, and the memory-architecture overlay — all absorbed from Bets #4, #5, and Bet-C4 per the reconciliation.

**Job 4 — Increase NRR above 120%.** Bazaarvoice/Curalate was a renewal-motion business; Cohley's contract structure (managed-service plus platform) is the prototype hybrid-pricing motion Sierra is exporting now. Alex has been the AE on the other side of the (11,L) "CSM forgot what we promised nine months ago" moment more times than he can count. That experiential authority is rare in the AI-builder cohort competing for these roles. Bet served: **Bet #2 (vertical-agent operator role inside Sierra or Decagon).** Path: **JOIN.** Sierra's Head of Enterprise GTM East / Decagon's Director Strategic Accounts — both companies live at (11,L) + (11,I) — are where the renewal-motion memory gap is closest to internal productization.

**Job 2 — Hit next year's number without doubling headcount.** GKY Industries was a 6-quarter forecast horizon with hiring-budget compression at exactly the CFO-side math F3's Job 2 describes: "40% growth on 15% heads." Bet served: **Bet #1 + Bet #4 + Bet #5 as a bundled advisory practice.** Path: **ADVISE.** One CFO buyer, three modules: $25K Playbook engagement → $40K FinOps audit → $40K RAG/memory audit. Anchor the line-item pricing on Vanta's SOC2-readiness pattern, which is the F500 procurement comfort zone.

### X.5 — Arbitration of seven cross-Wave-1 JTBD questions

1. **Is (5,F) buying-committee mapping Job 1's biggest gap?** Refine up but not to #1. (9,G) procurement-seam at gap 10 is bigger than (5,F) at gap 8 because cycle-time cost of bad committee mapping is 2–4 weeks; cycle-time cost of unprepared procurement-seam navigation is 6–24 weeks. The latter is the bigger gap-of-N at GTM-org scale.

2. **Is (9,G) Job 2's biggest gap or Job 1's?** Both, in different framings. Job 1 = vendor-side cycle compression (sell in-quarter). Job 2 = buyer-side deployment compression (signature → productive use). The Playbook should carry both framings explicitly. Sequence-wise: Job 1 framing pulls harder because vendors hold variable quarterly budget; buyers' deployment-compression budget is fixed planning-cycle and slower to release. Open the Playbook on Job 1, expand to Job 2 in Chapter 2.

3. **Does (6,L) persistent AE memory serve Job 2 or Job 5?** Job 2 primarily; Job 5 secondarily through the (12,L) read-through. Build the product for the AE, sell to the VP Sales (Job 2 owner), bonus-sell to RevOps (Job 5 owner) as forecast-accuracy improvement. The buyer is VP Sales — not RevOps.

4. **Does (11,I) outcome-pricing playbook serve Job 4 or Job 3?** Both, with different counterparties. Job 3 framing: CAC payback adoption-risk template (CFO). Job 4 framing: operational SLA dispute template (CCO). Two distinct buyers, two distinct chapter framings, one shared productized template (dual-telemetry + 30/60/90 dispute mechanic + third-party arbitration).

5. **Does (7,J+M) procurement-seam coach-grading serve Job 2 or Job 1?** Job 2 — the ramp curve. Job 1's close-rate is about the AE who is *already* procurement-fluent; coaching does not compress this-quarter's deal. Job 2's ramp-curve compression IS the JTBD: get a new AE certified on procurement-seam work in 12 weeks not 28. Buyer: VP Enablement → reports to VP Sales → Job 2 owner.

6. **Common Room: Bet #2 join target or (5,F) building block?** Both possible; resolved by sequencing. Common Room at $30M ARR + Series C $250M val + community-signal-only is too narrow a single-product moat to be the durable (5,F) winner standalone. Either Common Room expands into multi-source fusion themselves (Bet-C5 JOIN makes sense, 12–18 month window) OR someone else builds (5,F) on top and Common Room becomes input (Bet-C1 BUILD makes more sense, but Alex's operator path is weaker there). **Decidability event: the next two-quarter Common Room roadmap reveal (GC6).** Default position per Alex's lock: **Bet-C5 JOIN wins over Bet-C1 BUILD.**

7. **Hebbia (#1 F4 composite) vs Microsoft 365 Copilot (#1 C6 cell-coverage) — which serves Alex's career JTBD?** Hebbia, unambiguously. Microsoft wins the matrix at suite level; Alex inside Microsoft is a senior IC seat with no equity asymmetry. Hebbia at 2.5–5% under-funded ratio + 0.20–0.40% equity + Mehta/Stripe-anchored team + MBB-feedstock + NYC = 5× asymmetric upside relative to MS. Cell-coverage authority is the *market* truth; equity asymmetry is the *Alex* truth. Different JTBDs at different scales — they do not contradict.

### X.6 — What JTBD tells us about which bets to fund

- **JTBD most-validates Bet #5 (memory architecture).** L-column lights up at 3 of 5 jobs; (11,L) NRR memory at gap 10; (12,L) forecast-decay at gap 9; (6,L) AE memory at gap 9. No other bet draws the same JTBD density. Bet-C9 is the productized form. Sequence: Bet #1 ships first (90-day publish), Bet-C9 productization at the Q3 2026 trust-earned gate.
- **JTBD most-threatens Bet #6 (newsletter standalone).** The newsletter doesn't *close* a Conclude gap — it sits at "stay current," which is a B7 job, not an F3 job. Bet #6's JTBD pull is weaker than the tracker implied. Reframe as Bet #1 distribution layer only; do not justify it standalone.
- **JTBD surfaces Bet-C8 above the synthesis read.** (6,E) deal-diagnosis appears at Job 1 (gap 9) AND Job 5 (gap 9). Two-job cell at gap 9 = high JTBD compounding. The operator path inside a credible (6,E) NYC startup belongs on the Bet #2 watchlist alongside Hebbia/Rogo/Sierra. Watch Aircover and any AI-Gong spinout.

The cross-bet through-line: **Bet #1 publishes → Bet #5 productizes → Bet-C4 templates → Bet-C8 operator-watches.** Each compounds JTBD validation for the next. The structural finding of F3: the GTM org is not buying agents. It's buying procurement-fluent + memory-durable + outcome-defensible + causation-explainable substrate that lets the CRO/CFO/CCO/Board defend the number. Alex's commercial fluency lands on three of the five jobs (1, 4, 2); the procurement-seam he carries from twelve years of enterprise B2B is the multiplier that turns the profile from one-of-many enterprise AE into rare-on-the-market.

---

## Part XI · Synthesis · The Updated 7 Bets + 5 Risks + 6 Cruxes

The cell-matrix work converted the seven bets from a portfolio of options into a sequenced operating plan. Three independent frameworks (Wardley, 7 Powers, Ecosystem JTBD) all confirmed Bet #1 as the highest-leverage, most-Power-footed position. Bet #5 was repositioned. Bet #3 was re-sequenced. The ten candidate new bets surfaced in Phase 2a synthesis were winnowed to three promotions and seven absorptions / parks. The new short form: **publish (Bet #1), then rent equity (Bet #2), with advisory + gateway-pair (Bet #3a) running concurrent from H2 2026, distributed via newsletter (Bet #6), with Bets #4 and #5 as modules of #1, and Bet-C9 promoted as Q3 2026 productization vector.**

### XI.1 — The seven bets, refreshed

#### Bet #1 · Enterprise AI Procurement Operating Standard
**Verdict: REINFORCED + EXPANDED. Conviction ★★★★★.** No change in rank. Three independent frameworks converged on this — Wardley says it sits at the single most asymmetric position in the matrix (Genesis-stage flag claimable, Article 14 first-enforcement as a 5× TAM expansion event); 7 Powers identifies the highest Power footing of all seven bets (Process Power from twelve years of procurement scar-tissue stacked on Branding stacked on downstream Switching Costs as the Playbook becomes the buyer-side reference); JTBD validates two-job direct service (Job 1 in-quarter close compression AND Job 2 buyer-side deployment compression).

The cells this bet now anchors at: **(9,G) at OCQ 19/20** as the matrix peak; (9,I) AI-specific contract addenda; (9,M) trajectory-evidence pack; (4,M) SDR observability; (6,M) AE observability; (12,M) forecasting observability; (11,I) outcome-pricing dispute as a module; (4,B)+(4,G)+(4,M) synthetic-SDR adverse-selection guardrail; the entire seven-counterparty gauntlet (InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, Enterprise Architecture — the seventh confirmed).

The Playbook now absorbs four new modules from Wave 1 and the C-candidates:

- Outcome-pricing contract template (from F6, productizes Bet-C4 dual-telemetry + 30/60/90 dispute + third-party arbitration)
- Per-trajectory FinOps audit module (from F6, productizes Bet #4 / Bet-C3 — Anthropic Agent SDK 2.0 + OpenAI Responses API per-trajectory billing exposes 30–60% savings on multi-hop trajectories at $1M+ AI spend)
- Pricing-model selection decision tree (from F6 — upstream of vendor-selection tree, since pricing-strategy practice is upstream of vendor selection)
- Memory-architecture overlay (from F3, productizes Bet #5 / Bet-C9 as a vendor-evaluation rubric)

Sequencing change: unchanged from Volume III — first. Falsifiability event: **<500 downloads / <50 inbound conversations in 60 days OR Vanta/Drata/Ironclad ships AI-vendor bundle Q4 2026.** Next action: outline locked Week 1 of Q3 2026; 30 expert interviews Weeks 2–6; publish Week 12 with the bilateral evidence-pack interchange format as the canonical artifact and the Agent Procurement Rubric shipped as an open spec (Bet-C6 reframe).

#### Bet #2 · Vertical Agent GTM Leadership Role
**Verdict: REINFORCED + SHARPENED. Conviction ★★★★★.** No rank change. F4 ranked Hebbia #1 NYC composite (under-funded ratio 2.5–5%, 0.20–0.40% equity, MBB+Stripe-flavored buyer fit, 2-quarter window before Series C). F2 ranked Hebbia #1 for JOIN despite Hebbia not being a top-5 most-durable company — different question (Alex's career asymmetry vs the company's structural moat). F3 confirmed: Hebbia for Alex's career JTBD; Microsoft 365 Copilot for matrix-market truth; not contradictory, different scales.

Cells anchored: (6,A) AE pre-call brief / vertical-data anchor; (12,F) cross-system narrative retrieval — Hebbia's FinServ/MBB cell of strength; (10,D) + (10,G) + (11,L) at Sierra; (10,D) + (11,I) at Decagon; (11,L) renewal memory at any vertical-CX winner.

Ranked target list (triple-confirmed): **Hebbia > Sierra > Rogo > Harvey > Glean.** MBB feed-stock activated Feb–Apr 2026 — Mateo Berger (BCG NYC Principal AI practice → Hebbia, Feb 2026), Sarah Park (McKinsey QuantumBlack → Sierra, Mar 2026), Andrew Sinclair (Bain Boston AI practice → Harvey, Apr 2026). Divya Mehta (Stripe Enterprise → Hebbia VP Revenue NYC, Mar 2026) is the anchor for the Hebbia conversation. Foundation-lab AE departures (OpenAI / Anthropic enterprise) are the emerging 4th feed-stock — early-May 2026 LI clusters; this signals comp-band reset to come.

Bet-C5 sub-target: operator path inside Common Room ($30M ARR, Series C $250M val, NYC). Per Alex's lock, Bet-C5 (JOIN) wins over Bet-C1 (BUILD). Decidability event: 2-quarter Common Room roadmap reveal (GC6).

Sequencing change: unchanged from Volume III — second, concurrent with Bet #1. Falsifiability: 6 months focused NYC search yields no offers in the band. Next action: time the offer **before** the up-round at Hebbia / Rogo / Augment (the under-funded-relative-to-ARR-velocity plays). 30-day MBB-network push opens parallel pipeline. Sign **before** Anthropic ARR Q3 2026 resolution (GC2) if conviction high; **after** if wobbly.

#### Bet #3 · MCP-Native Enterprise Integration Practice
**Verdict: SPLIT. Conviction ★★★★ held but shape changed materially.** Wardley: PE-4 (MCP gateways crossing to Product, H2 2026) compresses the advisory window faster than Volume III modeled — if Bet #1 publishes Q3 2026 and Bet #3 advisory waits, the gateway-control-plane window may already be closing.

**Resolution: Bet #3 has two legs:**

- **3a · Advisory + gateway-partner positioning (Cloudflare / Kong / Pomerium pair).** Runs **CONCURRENT** with Bet #1 from H2 2026 — it IS Bet #1's gateway-partner module. Process Power flavor compounds with Bet #1's Branding flavor. Cells anchored: (9,G) gateway-side, (4,M) + (6,M) + (9,M) M-column overlay through the gateway audit log.
- **3b · Productized MCP server practice.** Already reframed away in Volume III. Remains parked. F2 confirmed minimal Power footing here.

Sequencing change: YES — 3a moves to concurrent with Bet #1, not deferred. Falsifiability: MCP forks (GC4 / Crux C2). 3a survives a fork better than 3b. Next action: Q2 2026 audit of ten SaaS systems most lacking MCP servers (filter by Job 4 and Job 1 outcomes); open Cloudflare gateway-partner conversation in Q3 2026 in parallel with Playbook publish.

#### Bet #4 · Inference Cost Optimization / FinOps for Tokens
**Verdict: SUBSUMED into Bet #1 as a module. Conviction ★★★★ standalone is moot.** Per-trajectory FinOps window is 12–18 months before AWS Bedrock auto-routing default-on (H2 2027 expected) bundles the layer. Anthropic Claude Agent SDK 2.0 (Apr 2026) + OpenAI Responses API expose per-trajectory billing today — 30–60% savings on multi-hop trajectories at $1M+ AI spend, real numbers, real audit-able. The standalone "FinOps services practice" play is no longer the right shape; the high-leverage move is to fold per-token + per-trajectory FinOps as one of the seven Procurement Playbook overlays (Playbook §III.8). Sells through the Playbook's distribution + earns CFO/CIO trust without standing up a separate practice.

Cells anchored as module: (4,M) + (6,M) + (9,M) + (12,M) via per-trajectory cost ceilings; all K-column cells once OSWorld 65% crosses (GC1) because sub-agent fan-out and per-trajectory blast-radius become a procurement constraint.

Sequencing change: absorbed into Bet #1 timeline. Falsifiability: AWS Bedrock auto-optimization announces Q3 2026, window collapses fast — the audit module survives the bundle better than a standalone services practice would. Next action: free first audit for 1–2 mid-market AI-spending companies in Q3 2026; case study lifts into Playbook §III.8 as new module. Decide by Q3 2026 whether to scale or absorb fully.

#### Bet #5 · Enterprise RAG / Memory Architecture Practice
**Verdict: SUBSUMED + RE-EMERGES as Bet-C9 productization vector. Conviction ★★★★ standalone repositioned.** This is where F2 and F3 split most sharply. F2 (7 Powers) said: least Power-footed of all seven bets standalone — RAG architecture as advisory does not accumulate durable Power because buyers consume the audit and the practice doesn't compound. F3 (JTBD) said: most-validated job-fit — L-column lights up at 3 of 5 jobs, load-bearing at Jobs 4 and 5, and the underlying buyer pain is real and growing.

Reconciliation per Alex's lock: **subsume Bet #5 into Bet #1's modules; promote Bet-C9 (Persistent Memory as Service Line) as the Q3 2026 productization vector AFTER the Playbook earns trust.** The data-integrations + GDPR-deletion-semantics + CSM/AE curation UI = three-stage moat.

Cells anchored: (6,L) AE deal-cycle memory · (11,L) renewal cross-quarter memory · (12,L) forecasting decay memory · (10,L) per-customer CX memory · (9,L) counterparty memory.

Sequencing change: standalone deferred; module within Bet #1 immediate; Bet-C9 productization vector at Q3 2026 trust-earned decision gate. Falsifiability: long-context model improvements (Gemini 3.0, Claude prompt caching) eat the low end faster than enterprise grows the high end. Next action: Bet #5 modules ride inside the Bet #1 Playbook publish; revisit standalone Bet-C9 productization at the Q3 2026 trust-earned gate, with the (11,L) NRR-memory cell as the demo target.

#### Bet #6 · Operator's Translation Newsletter / Public Voice
**Verdict: REFRAMED as distribution layer for Bets #1–#3. Conviction ★★★ standalone not viable.** F3 explicit: the standalone weekly translation newsletter most-threatens itself — the JTBD it serves (Job 5: stay current + act on it) does not by itself drive action conversion at scale. Reframe: newsletter = the distribution layer for the Playbook + the gateway-partner positioning + the operator-translation public voice. Cross-pollinate Bet #1 Playbook downloads with newsletter subscribers (correlation = right-audience proof).

Sequencing change: reframe to publish-cadence supporting Bets #1–#3, not standalone. Falsifiability: <2K subscribers in 6 months AND no inbound role/advisory from it = positioning theater. Kill at month 6 OR commit harder. Next action: Kit v1 Week 4 of Q3 2026 (after Playbook outline locked), distribution-pair with Playbook publish at Week 12.

#### Bet #7 · VC Operating Partner / Platform Path
**Verdict: HELD as fallback. Conviction ★★★ unchanged. ★★★★ if becomes primary.** F4 confirmed: principal-to-operator pattern (Carey Lai Insight → Sierra Apr 2026 + 3–5 similar moves) — the platform and operator paths converge at the senior level. This bet runs as background networking only; not actively pursued. Sequencing change: none. Falsifiability: if Bets #1, #2, #3a all land by month 12, this drops further; if none do, it becomes primary. Next action: build relationships at three NYC funds via RAAIS / Betaworks AI Camps / FirstMark MAD events. No active applications until Q4 2026.

### XI.2 — Five Risks, refreshed for the intersection

The five risks from `AI_AGENTS_TRACKER.md` (R1–R5) survive Volume IV with one sharpening. Restating:

- **R1 — Foundation labs walk up-stack faster than verticals can entrench.** Sharpened by Volume IV: the threat is *concentrated at the horizontal-suite incumbent expansion vector* (Microsoft 365 Copilot for Sales, Salesforce Agentforce, Glean Network Economies) rather than at direct foundation-lab application plays. F2 named Microsoft 365 Copilot for Sales as the matrix-wide top-Power-footed entity (4-Power stack). The Microsoft + Anthropic + OpenAI sales-app posture is the actual concentration risk. Mitigation: the Playbook ships open-spec; Bet #1 is structurally hedge-able against MS expansion because it sits at the procurement seam where MS lacks operator credibility.

- **R2 — Article 14 / EU AI Act enforcement is paper-tiger.** Decidability event: late 2026 / Q1 2027 first enforcement. If paper-tiger, Bet #1 TAM compresses ~5×. Mitigation: the Playbook ships in Q3 2026 anyway; the bilateral evidence-pack format and the seven counterparty gauntlet hold value independent of Article 14 enforcement — they map to SOX, SOC2, HIPAA, TCPA, CAN-SPAM all-of-the-above.

- **R3 — MCP forks before becoming the standard.** GC4 watch. If MCP forks (Anthropic vs OpenAI vs Microsoft Graph), Bet #3a still survives because Cloudflare gateway-partner positioning is fork-agnostic — gateways arbitrate forks rather than betting on one. Bet #3b (productized servers) does not survive; remains parked.

- **R4 — Anthropic ARR Q3 2026 resolves below $24B lower-bound.** GC2 watch. Vertical-agent valuations compress 20–30%; Sierra $10B → $6–8B; Hebbia / Rogo round timing slows. Counterintuitive read: this *strengthens* equity bands for Alex's Bet #2 entry (companies need more total comp to hire). Mitigation: time the offer signature relative to the ARR resolution — sign before if conviction high, after if wobbly.

- **R5 — Synthetic-SDR adverse selection collapses Bet #1 ICP credibility.** Sharpened by F2 finding: the synthetic-SDR ceiling (11x flat at $20M ARR) is now public; the (4,B)/(4,G)/(4,M) trio in Job 3 frames the synthetic-SDR adverse-selection guardrail as a Bet #1 module rather than a market risk. Mitigation: the Playbook *names* the 11x ceiling, the RR-negative trap, and the Lavender/Regie commoditization — this earns credibility with CFO/RevOps buyers rather than losing it.

### XI.3 — Six Cruxes (one new from Volume III, sharpened for the intersection)

The five cruxes from Session A survive; Volume III added GC1 OSWorld 65%. All six restated with Volume IV refinements:

| # | Crux | Decidability horizon | Answer-event to watch | Re-rank consequence |
|---|---|---|---|---|
| **GC1** | OSWorld 65% on a frontier system | **Q3 2026** | Public scoreboard event (Anthropic / OpenAI / Google) | Crossed = K-column reprices; Microsoft Sales Copilot wins by default; procurement-overlay needs computer-use sub-section published within 30 days; Bet #1 Playbook chapter prepped on per-trajectory cost ceilings + OAuth blast-radius for CU agents |
| **GC2** | Anthropic ARR Q3 2026 resolution | **Q3 2026** | The Information / WSJ confirmation of annualized run rate | Below $24B = vertical-agent comp reprice (Sierra $10B → $6–8B); strengthens Alex's Bet #2 equity-band timing window. Above $30B = Sierra/Decagon push toward IPO posture 2027; bands tighten further; equity asymmetry weakens |
| **GC3** | Article 14 enforcement teeth vs paper-tiger | **Late 2026 / Q1 2027** | First enforcement action by an EU member-state DPA | Teeth = Bet #1 TAM 5× expansion; paper-tiger = Bet #1 still survives on SOX/SOC2/HIPAA cousins, but advisory-economy compresses to 2× rather than 5× |
| **GC4** | MCP commons-or-fork | **Q4 2026 / Q1 2027** | OpenAI / Microsoft public posture on MCP compliance + Anthropic Sept'25 spec acceptance | Commons = Bet #3a gateway-pair compounds at scale; fork = gateways still win (arbitrage role), but standardized clauses in Bet #1 need fork-aware language |
| **GC5** | Ironclad / Vanta / Drata AI-vendor bundle launch | **Q4 2026** | Public product launch or RFP/AI-vendor module from any one of the three | Launch = Bet #1 productized branch falsified; advisory branch survives; Playbook becomes the open-spec input to the bundle (Process Power for the maintainer holds). No launch by Q1 2027 = Bet #1 productized branch reopens |
| **GC6** | Common Room roadmap reveal (BUILD vs JOIN decidability) | **Q3 / Q4 2026** | Common Room product event or Series C public messaging | Multi-source fusion expansion = Bet-C5 JOIN strengthens; community-signal-only-permanent = Bet-C1 BUILD reopens (but Alex's operator path remains weaker there) |

The six cruxes carry asymmetric weight. **GC1 (OSWorld) and GC2 (Anthropic ARR) both resolve in Q3 2026**, which is the same quarter as the Playbook publish — that quarter is the single largest information-density event in the 18-month horizon. GC3 + GC5 resolve in Q4 2026 / Q1 2027 and bracket the Bet #1 productization-vs-advisory fork. GC4 + GC6 resolve later and bracket the Bet #3a sequencing and the Bet #2 sub-target choice.

### XI.4 — The ten candidate new bets · verdict table

| ID | Candidate | Verdict | Anchor cell | Bet absorption / promotion |
|---|---|---|---|---|
| Bet-C1 | The Buying-Committee Graph product (BUILD) | **PARK** — Alex-locked: Bet-C5 (JOIN) wins. Revisit if Common Room roadmap doesn't move (GC6) | (5,F) OCQ 18 | — |
| Bet-C2 | Trajectory-grade procurement-seam coach | **ABSORB into Bet #1 as follow-on.** Coach the work the Playbook teaches; productize after Playbook publish. Accident-of-light cell — flag in Action Map | (7,J+M) OCQ 13 | Module into Bet #1 chapter 2 |
| Bet-C3 | Per-trajectory FinOps audit practice | **ABSORB into Bet #1 / Bet #4 fold.** Module §III.8 of Playbook | (4/6/9/12, M) | Module into Bet #1 §III.8 |
| Bet-C4 | Outcome-definition contract template | **ABSORB into Bet #1.** Highest-leverage Bet #1 wedge per F6 | (11,I) → (9,I) | Module — new Playbook section |
| Bet-C5 | Operator path inside Common Room | **PROMOTE as Bet #2 sub-target.** F3 verdict explicit — JOIN beats BUILD until GC6 forces re-decide | (3, A+L+F), (5,F) | Promoted within Bet #2 |
| Bet-C6 | AI-Vendor Procurement Standard as open spec | **PROMOTE as Bet #1 reframe.** First credible publisher sets procurement default for next 5 years; Process Power for the maintainer | meta over (9,G) | Reframes Bet #1 itself |
| Bet-C7 | RevOps trajectory agent (closing pipeline-scrub loop) | **WATCH only.** 12–18 month build window; Alex's bet adjacency moderate; not a primary bet | (8,G) OCQ 15 | Watchlist |
| Bet-C8 | Deal-Diagnosis Causation Engine | **WATCH as Bet #2 operator-target.** F3 elevated above synthesis read — two-job cell at gap 9. Watch Aircover + any NYC AI-Gong spinout | (6,E) OCQ 17 | Watchlist within Bet #2 |
| Bet-C9 | Persistent Memory as Service Line | **PROMOTE as Q3 2026 productization vector inside Bet #5 fold.** Decide at trust-earned gate | L-column | Promoted as Q3 2026 productization vector |
| Bet-C10 | Article 14 Tie-Out Standard | **ABSORB into Bet #1.** Already drafted as Playbook §III.6 Overlay. Open-spec wedge | (9,M) | Module — Playbook §III.6 |

**Net result: three promotions (Bet-C5, Bet-C6, Bet-C9), four absorptions (Bet-C2, Bet-C3, Bet-C4, Bet-C10), three watch-list / parks (Bet-C1, Bet-C7, Bet-C8).**

### XI.5 — The Updated 7 Bets · one-line shape

Still seven, with two nested sub-bets (3a / 3b) and one promotion gate (Bet-C9).

| # | Bet | Status | Sequence | Conviction |
|---|---|---|---|---|
| **1** | **Enterprise AI Procurement Operating Standard** — open-spec stewardship via Bet-C6 reframe; absorbs Bets #4, #5, modules from C2/C3/C4/C10 | reinforced + expanded | **NOW** | ★★★★★ |
| **2** | **Vertical Agent GTM Role** — Hebbia > Sierra > Rogo > Harvey > Glean; Bet-C5 Common Room as sub-target | reinforced + sharpened | **Concurrent with Bet #1** | ★★★★★ |
| **3a** | **Advisory + gateway-partner positioning** — Cloudflare / Kong / Pomerium pair | held + re-sequenced concurrent | **Concurrent with Bet #1 from H2 2026** | ★★★★ |
| 3b | Productized MCP server practice | parked | — | parked |
| 4 | **FinOps for Tokens** — module of Bet #1 §III.8 | subsumed | inside Bet #1 | ★★★★ (as module) |
| 5 | **RAG / Memory architecture** — module of Bet #1; Bet-C9 productization at Q3 2026 gate | subsumed standalone; Bet-C9 promoted | inside Bet #1, then Bet-C9 Q3 2026 | ★★★★ (as Bet-C9) |
| 6 | **Operator Translation Newsletter** — distribution layer for #1–#3 | reframed | from Q3 2026 ongoing | ★★★ |
| 7 | **VC Operating Partner** — fallback only | held | background | ★★★ |

The clean read across the seven: Alex is building one practice (Bet #1) with two distribution layers (Bet #6 newsletter, Bet #3a gateway-partner) and one operator-role parallel (Bet #2 at Hebbia / Sierra / Rogo). Bets #4 + #5 are no longer standalone but the modules that make Bet #1 valuable. Bet-C9 is the post-trust productization vector. Bet #7 is the fallback if the first six don't land.

---

## Part XII · 6 / 12 / 18-Month Action Map for Alex

This is a calendar Alex can act on tomorrow, not a strategy deck. Q3 2026 is the most-detailed because that's where the highest-density information events cluster (GC1 OSWorld and GC2 Anthropic ARR both resolve in that quarter). Q4 2026 is the productization / gateway / Article-14 watch quarter. H1 2027 is the offer-or-pivot quarter. Months 12–18 is the anchor-decision quarter.

### XII.1 — Q3 2026 (next 90 days) — most detailed

#### Week 1 · Outline lock + MBB-network 30-day push opens

- **Playbook outline locked.** Use the F3 Job 1 phase-row as the framing prompt: Locate (5,F) → Confirm (6,E) → Execute (9,G) → Conclude (9,M) becomes the spine of the seven counterparty chapters. Lock the seven counterparties (InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, Enterprise Architecture) as the chapter structure, with Section IV reserved for the 14 AI-specific contractual addenda already drafted in F5 §8.
- **MBB-network 30-day push opens.** Three named warm intros to start:
  - **Mateo Berger** (BCG NYC Principal AI practice → Hebbia Head of GTM Strategy, Feb 2026). Berger is the foothold for the Hebbia conversation; one intro = three more by week 3.
  - **Sarah Park** (McKinsey QuantumBlack → Sierra Head of Industry FinServ, Mar 2026). Park is the FinServ-vertical intro at Sierra; pairs with Joe Schmidt IV (Stripe NYC → Sierra Head Enterprise GTM East, Jul 2025) as the second touch.
  - **Andrew Sinclair** (Bain Boston AI practice → Harvey Director GTM Strategy, Apr 2026). Sinclair is the legal-vertical comparison data point; informs the Job 4 (NRR) framing for Bet #2 conversation.
- **NYC events to lock for Weeks 1–4:** RAAIS NYC (advance attendance list pull), Cornell Tech AI demo days (calendar block), Betaworks AI Camps (May/June cohort demo nights), FirstMark MAD events (Matt Turck monthly). These are the four standing events that index founders + capital + operator-tier in one room.

#### Weeks 2–6 · 30 expert procurement-side interviews

Counterparty-mix: ~5 per role across the seven counterparties — InfoSec (5), Legal (5), Privacy (5), AI Council/Governance (5), Procurement (4), Sponsor (3), Enterprise Architecture (3). Target 30 total, ~5 per week, three buckets:

- **F1000 buyer-side (15):** JPMorgan (InfoSec + Privacy + AI Governance triad), Goldman Sachs (Legal + AI Council, where the Yash Tekriwal → Rogo Jan 2026 hire opens the door), Walmart (Procurement + EA), Pfizer (Privacy + AI Council, EU/HIPAA-adjacent), Anthropic enterprise side (Sponsor + AI Governance, where the foundation-lab AE departure pattern gives a reciprocal door). Anchor list. Five F1000 = anchor; ten more across the second-tier list (Citi, Capital One, CVS, Lowe's, Cigna, etc.).
- **Vendor-side (10):** Hebbia (Mehta), Sierra (Schmidt), Rogo (Tekriwal), Decagon (Sinha — Field CTO), Glean, Clay (Kareem Amin's 40-headcount NYC push gives a public-facing intro), Ironclad (the Bet-C10 Article 14 reference partner), Vanta (the Bet-C10 / GC5 falsifiability watch), Cloudflare (Bet #3a gateway-pair primer conversation), Galileo or Arize (the M-column observability cousin).
- **Procurement / Legal counterparties (5):** vendor-side procurement leads + buyer-side Deal Desk leads with named AI-vendor closing scar tissue.

Output of the 30 interviews: the 56-cell × named vendor matrix in Playbook §VI Rubric gets populated; the 14 AI-specific addenda get red-teamed against real F1000 redlines; the seven counterparty chapters each get 3–5 anonymized quotes that ground the prose; the bilateral evidence-pack interchange format gets stress-tested against five real procurement gauntlets.

#### Weeks 6–9 · Hebbia / Sierra / Rogo / Decagon outreach via warm intros

This is the Bet #2 sequencing window. The Bet #1 Playbook v0.5 is now a credibility artifact — signals procurement-seam fluency that beats MBB candidates on operator depth. Lead each conversation with a written one-page memo: "Here is how I would close the (11,L) memory-gap inside your existing roadmap by Q1 2027" (Sierra / Decagon framing) or "Here is how I would close the (12,F) FinServ vertical-data narrative gap inside your existing roadmap" (Hebbia / Rogo framing).

Named-people sequence:

- **Bret Taylor (Sierra co-CEO, NYC monthly).** The Sierra anchor conversation. Taylor's calendar opens through Schmidt + the a16z Anjney Midha referral lattice. Frame: Bet #1 Playbook earns the room; the (11,L) NRR memory chapter is the conversation prompt. Target outcome: introduction to the Head of Industry / Director Strategic Accounts hiring panel.
- **Munjal Shah (Hippocratic AI CEO).** Healthcare GTM bench needs Sara Mauskopf-tier operator addition; Hippocratic at Series C $2B + $50M+ ARR is the one healthcare vertical with senior-tier comp band ($250–350K + 0.10–0.25% equity). Frame: the Bet #1 HIPAA-overlay chapter as the entry conversation.
- **Aman Sanger (Cursor SF/NYC).** Adjacent target — Cursor has growing NYC presence and the AI-coding cell pulls onto the Bet #1 Playbook surface (developer-tool procurement gauntlet is increasingly enterprise-priced). Lower-fit than Hebbia/Sierra but worth one conversation.
- **Eric Glyman (Ramp CEO / AI org).** Ramp's AI-org Director role opens at $300–400K + 0.01–0.05% equity (broader product = lower equity asymmetry, which is why Ramp ranks behind Hebbia / Rogo in the F4 composite). Frame: the Bet #4 per-trajectory FinOps audit as the natural Ramp wedge — this is the company most likely to *buy* the audit even before they hire the operator.
- **Vinay Sivulka (Hebbia, leadership team).** Beyond Mehta, Sivulka is the second Hebbia anchor in the founder-team-extended ring. Frame: the Bet #1 Playbook + the (12,F) FinServ vertical-data narrative as combined entry.

The Rogo angle: NYC FinServ vertical-data + banker-fluent gate. Rogo's Tekriwal hire (Goldman MBD VP → Head of Enterprise Sales, Jan 2026) is the door; the equity asymmetry (0.30–0.60% per F4 §F4.2) is the largest in the named set. The conversation is "I have walked into 200+ banker procurement seams; here is how I would compress the Rogo enterprise sales cycle by 30%." Target outcome: Director Enterprise Sales offer in the band, signed before the Q2 2026 Series C up-round closes.

#### Weeks 9–12 · Playbook v1 publication

- **Playbook v1.0 publishes Week 12.** Format: open-spec markdown + PDF + an HTML Agent Procurement Rubric tool (the bilateral evidence-pack interchange format as a fillable artifact). Distribution: LinkedIn announcement post, three-post launch sequence, four-podcast tour (Latent Space, Practical AI, Lenny's Podcast, AI in Business).
- **Cloudflare gateway-partner conversation opened in parallel (Bet #3a).** The Playbook publish is the credibility unlock for the Cloudflare conversation — frame: "Here is the open-spec procurement rubric. Here is the gateway-side audit log requirement that maps onto it. Cloudflare One is the natural reference architecture." Target: Cloudflare gateway-partner positioning agreement signed by end of Q3.
- **Newsletter Kit v1 (Bet #6) launches.** Format: weekly translation, ~700–1200 words, open with the week's most consequential agent-GTM news interpreted through the Playbook lens. Subscribe list seeded with the 30 interview targets + 200 LinkedIn second-degree connections + 50 NYC operator network.
- **500-download / 50-inbound falsifiability test starts.** Clock starts at Week 12 publication. 60-day window. <500 downloads OR <50 inbound conversations = falsification of the productized branch (advisory still survives). >500 + >50 = scale Bet #1 productization branch and accelerate Bet-C9 productization decision into Q4 instead of Q3 2026 of next year.

### XII.2 — Q4 2026 (months 4–6)

- **Article 14 first enforcement watch (GC3).** Late-2026 / Q1-2027 first DPA enforcement action is the trigger. If teeth, Bet #1 Playbook §III.6 Article 14 Tie-Out Overlay becomes the procurement default and Bet #1 TAM expands ~5×. If paper-tiger, the Playbook still serves SOX / SOC2 / HIPAA / TCPA / CAN-SPAM cousins — TAM compresses to 2× rather than 5×. **Playbook Q1 2027 update locked into the publishing cadence regardless.**
- **Common Room roadmap reveal (Bet-C5 decidability — GC6).** Multi-source fusion expansion = Bet-C5 JOIN strengthens; community-signal-only-permanent = Bet-C1 BUILD reopens. **Default per Alex's lock: Bet-C5 wins.** If the reveal lands ambiguous, the Bet-C5 conversation moves into Q1 2027 alongside the Hebbia / Sierra offer windows.
- **Anthropic ARR Q3 resolution → vertical-agent comp reprice (GC2).** Q3 2026 Anthropic ARR resolves; reprice cascades into Sierra / Decagon / Hebbia / Rogo offer bands within 30–60 days. **This is the Bet #2 offer-signature timing window** — sign before the reprice if conviction high; after if wobbly.
- **Per-trajectory FinOps audit pilot (Bet-C3 module of Bet #1).** Two free-first audits delivered in Q3 promote into one paid Phase-1 engagement in Q4 ($40K). Audit becomes case study for Playbook §III.8 module update. Decision gate: if paid conversion lands at >$50K combined ACV across two clients, scale; if not, fold module fully into Bet #1 advisory and de-prioritize standalone services line.
- **Ironclad / Vanta AI-vendor-bundle launch watch (Bet #1 productization branch falsifiability — GC5).** If any of Ironclad / Vanta / Drata launches an AI-vendor-bundle module in Q4, Bet #1's productized branch is falsified — but the *advisory* branch survives + the Playbook becomes the open-spec input to the bundle (Process Power for the maintainer holds). If no launch by Q1 2027, the productized branch reopens in H1 2027.
- **Bet #2 offer-signature target.** End of Q4 2026. Hebbia VP Revenue or Sierra Head Enterprise GTM East or Rogo Director Enterprise Sales. The 30-day MBB-network push from Q3 has by now produced 4–6 advanced conversations; close one in this window.

### XII.3 — H1 2027 (months 6–12)

- **Bet #5 productization decision.** Based on Q3 2026 trust earned (>500 downloads + >50 inbound + 2 Phase-1 paid engagements). Promote Bet-C9 (Persistent Memory as Service Line) as productization vector with (11,L) NRR-memory cell as the demo target. If trust not earned, park Bet-C9 for H2 2027 reconsideration and double-down on Bet #1 advisory as the standalone practice.
- **OSWorld 65% potential crossing → K-column reprice → procurement-overlay update (GC1).** If GC1 didn't resolve in Q3 2026, the H1 2027 window is the next likely trigger. Crossed = the K-column (computer-use) becomes deployable for back-office, Microsoft Sales Copilot wins by default, and the Playbook needs a new chapter on per-trajectory cost ceilings + OAuth blast-radius for CU agents within 30 days of the scoreboard event.
- **Bet #2 decision: offer signed at Hebbia / Sierra / Rogo OR pivot to Bet #1 standalone advisory practice.** The 6-month NYC search falsification window from Volume III is now the H1 2027 date. If no offer in band by month 12, the Bet #1 standalone advisory practice becomes the primary, Bet-C9 productization becomes the ceiling on it, and Bet #7 (VC operating partner) re-emerges as the secondary fallback.
- **MCP commons-or-fork resolution (GC4).** Q4 2026 / Q1 2027 horizon — likely lands inside H1 2027. Commons = Bet #3a gateway-pair compounds at scale and the Cloudflare partnership becomes the Bet #3a flagship reference. Fork = gateways still win the arbitrage role, but Playbook Section IV (14 AI-specific addenda) needs fork-aware language inserted in the Q1 2027 update.
- **Bet #1 v2.0 publish.** Playbook publishes its second edition in H1 2027 — incorporates Article 14 enforcement evidence (or paper-tiger update), OSWorld 65% K-column chapter (or update saying it didn't resolve), MCP commons-or-fork update, and the 6-month productization-vs-advisory branching evidence from Q3 2026 publication.

### XII.4 — Months 12–18

- **Bet #6 newsletter as Bet #1 distribution layer (ongoing).** By month 12 the newsletter has either passed the 2K-subscriber + non-trivial-inbound threshold (commit harder) or it has not (kill or fold to monthly cadence as Playbook companion).
- **Bet #7 VC platform path remains fallback.** If Bets #1, #2, #3a all landed by month 12, Bet #7 stays background. If two of three did not land, Bet #7 surfaces from background to active applications (3 NYC funds: Insight, Lightspeed, FirstMark or Two Sigma Ventures — relationships built via RAAIS / Betaworks / FirstMark MAD events from Q3–Q4 2026).
- **Anchor decision: stay-the-course on advisory + open-spec stewardship vs pivot to operator role at scale.** Months 12–18 is the natural decision-anchor — by then either the Bet #2 operator role is producing equity and Alex is inside Hebbia / Sierra / Rogo, OR Bet #1 advisory practice + Bet-C9 productization is producing $300K–$500K/year run rate and Alex is the open-spec maintainer of the Agent Procurement Rubric. Both are good outcomes; both close out Volume IV's central thesis as resolved.
- **Volume V session candidate?** Compute the next zoom level. Three candidate angles: (a) cell-coverage drill on the top-3 promoted candidate bets (Bet-C5 Common Room, Bet-C6 open-spec stewardship, Bet-C9 memory-as-service) at deeper resolution — sub-cell granularity, named-counterparty mapping, contract-template specifics; (b) post-OSWorld K-column deep-dive across the seven functions where computer-use newly deploys; (c) the Bet-C8 deal-diagnosis causation engine NYC startup-watch as a standalone Wave 1 substrate. Default: option (a) if Bet #1 + Bet #2 land cleanly; option (b) if GC1 resolves and the K-column repriced is the bigger story; option (c) only if a credible NYC (6,E) startup emerges to make it material.

---

## Part XIII · Best-Use-Case Reflections per Framework

A short post-mortem on what each framework was best at, what it missed, and where to use it again. Written for Alex twelve months from now who will run the next zoom-level analysis.

### XIII.1 — OCQ × Cell Matrix (12 functions × 13 capabilities)

**Best for:** surfacing under-served cells nobody else sees. The 156-cell grid forced visibility into combinations that vendor narratives never name — (9,G) procurement-seam at OCQ 19 became the matrix peak only because a 12 × 13 grid required us to score it. The (5,F) buying-committee mapping cell jumping to OCQ 18 is invisible at any coarser resolution; same for (6,E) deal-diagnosis causation at 17. Without the matrix you read about "AI for sales" as a category. With it you see seven specific cells where the category is empty and seventeen where it is saturated. **Missed:** cross-cell dependencies. The matrix scores cells in isolation; it does not capture that (9,G) sells *because* (4,M) + (6,M) + (12,M) are mandatory ≤18 months. The L-column convergence finding only emerged once we read across columns rather than down them — which is a step the matrix doesn't do natively. **Use again for:** any horizontal-vs-vertical decision with discrete, scoreable cells. Particularly any decision where vendor narratives are saturated and the question is "where is the matrix actually empty?"

### XIII.2 — Wardley Mapping

**Best for:** punctuated-equilibrium dating. Wardley's evolution stages (Genesis → Custom-Built → Product → Commodity) gave us PE-2 (Article 14 first enforcement, late 2026), PE-4 (MCP gateways crossing to Product, H2 2026), PE-5 (per-trajectory FinOps audit window, 12–18 months before AWS Bedrock auto-routing default-on H2 2027), and PE-1 (OSWorld 65%, Q3 2026). Wardley's framing of *when* a capability moves from Custom-Built to Product is the only thing that gave Bet #1 its sequencing-first verdict — without it the Playbook would have published in H1 2027 and missed the Article 14 first-enforcement procurement-default window. **Missed:** operator-personality fit at the cell. Wardley says "the K-column is at Genesis-stage transitioning to Custom-Built in H2 2026"; it does not say "Alex is uniquely positioned to operate inside Hebbia or Sierra rather than to build a CU startup." That JTBD-and-fit layer is invisible to Wardley. **Use again for:** any Build-vs-Buy timing decision where the question is "how long is the advisory window before commoditization?" Particularly load-bearing in compressed-window calls like Bet #3a (gateway-pair) where missing the window kills the bet entirely.

### XIII.3 — Seven Powers (Helmer)

**Best for:** filtering vendor narratives ruthlessly. The 7 Powers screen rejected most of the matrix's loud names and identified Microsoft 365 Copilot for Sales as the matrix-wide top-Power-footed entity (4-Power stack: Counter-Positioning + Switching Costs + Network Economies via M365 Graph + Cornered Resource via LinkedIn ToS). It downgraded Bet #5 standalone (no Power footing) while validating Bet #1 as the highest-Power-footed of the seven (operator-shape Process Power + Branding + downstream Switching Costs). Without 7 Powers you fund Bet #5 standalone and lose the next 18 months on consulting-shape work that doesn't compound. **Missed:** Power flavors that *operators* (vs companies) can claim. Helmer's framework was built for company-scale Power; the operator-shape Process Power flavor that Bet #1 anchors at had to be invented for this analysis. The R5 sharpening on synthetic-SDR adverse-selection guardrail is also operator-shape and doesn't fit cleanly into any of the seven canonical Powers. **Use again for:** any join-vs-build call across multiple companies where the question is "which of these has actual durable Power vs venture-marketed Power?" Particularly load-bearing for Bet #2 target ranking.

### XIII.4 — Ecosystem JTBD (org-scale)

**Best for:** surfacing the buyer-side struggling moments. The five jobs (hit number this Q, hit number next year without doubling heads, reduce CAC payback, increase NRR, get forecast right) at GTM-org scale are the only framing that made Bet-C4 (outcome-pricing dispute template) a two-job lever — Job 3 (CFO) and Job 4 (CCO) — rather than a one-vendor-wedge. The 15 highest-gap underserved outcomes table is the single most useful artifact in the whole Volume IV cycle for prioritizing the next 90 days; the L-column pattern (3 of 5 jobs, load-bearing at Jobs 4 + 5) is the JTBD validation that converted Bet-C9 from speculative to promoted. **Missed:** the inside-the-org political dynamics that F5's seven-counterparty gauntlet caught. JTBD says "the CRO buys to satisfy Job 1"; F5 says "the CRO can't buy without InfoSec, Legal, Privacy, AI Governance, Procurement, Sponsor, and Enterprise Architecture all closing first." The political-gauntlet layer is what makes the procurement-seam cell (9,G) the matrix peak — JTBD told us *which* job; F5 told us *which* counterparties. Both needed. **Use again for:** any new-product positioning question at organizational scale, particularly when the buyer is a federation (CRO + CFO + CCO + Board) rather than a single role. Conflating end-user JTBD (B7) with org-scale JTBD (F3) is the most common error in vendor narratives — the layered B7 → F3 hierarchy is itself a transferable analysis tool.

### XIII.5 — Talent + Capital Flow (F4)

**Best for:** timing windows and equity arbitrage. F4's NYC composite ranking of Hebbia #1 (under-funded ratio 2.5–5%, 0.20–0.40% equity, MBB+Stripe-flavored buyer fit, 2-quarter window before Series C) is the single most actionable Wave 1 finding. The MBB feed-stock activation pattern (Berger Feb / Park Mar / Sinclair Apr 2026) is what makes the 30-day MBB-network push viable — the warm-intro lattice is now real, not hypothetical. The Anthropic ARR Q3 2026 single-load-bearing-variable framing is what gives Bet #2 its offer-signature sequencing. **Missed:** cultural-fit beyond resume signals. F4 ranks Hebbia + Sierra + Rogo + Harvey + Glean on equity asymmetry + brand-prestige + secondary-liquidity — but does not rank them on whether Alex's 12-year procurement-scar-tissue + AI-builder fluency + NYC operator profile actually *clicks* with Mehta's vs Schmidt's vs Tekriwal's leadership style. That's the dimension that decides which one converts to offer-signature; the framework can't see it. **Use again for:** any operator-role decision with a finite signing window. Particularly load-bearing for the H2 2026 / H1 2027 Bet #2 offer window where Anthropic ARR resolution + Hebbia/Rogo Series C round timing compress the equity asymmetry inside a 6–9 month band that won't reopen.

### XIII.6 — Closing note on the framework stack

The five frameworks compounded. OCQ × Cell Matrix surfaced the cells; Wardley dated the windows; 7 Powers filtered the bets; JTBD validated the buyer pain; Talent + Capital Flow timed the offers. None of them alone would have produced the seven-bet sequencing — the 156-cell grid without Wardley dating would have under-prioritized Bet #3a; Wardley without 7 Powers would have over-funded Bet #5 standalone; 7 Powers without JTBD would have missed the L-column validation that promotes Bet-C9; JTBD without Talent + Capital Flow would have left Bet #2 unanchored to Hebbia. The five-framework stack is itself the transferable artifact — apply it as a template at the next zoom level.

---

*End AGENTS_GTM_ADDENDUM Part B (Parts X–XIII). ~7,800 words. Companion to Part A. Both feed into the next refresh of `output/ai-stack/OCQ_TRACKER.md` per the BETS_DELTA_NOTE annotations.*



