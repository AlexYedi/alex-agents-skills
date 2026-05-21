# Chapter 6 — Appendix

This appendix extends V1 Ch 6 and V3 Ch 6 rather than duplicating either. The field-wide glossary lives in V1 §6.1 (Wardley stages, OCQ discipline, HBM, JTBD, RSP, conviction calibration, falsifiability protocol). The agent-specific glossary lives in V3 §6.1 (MCP, agent runtime, computer use, trajectory, planner-executor, procurement gauntlet at six counterparties, OSWorld sub-crux). V4 layers cell-resolution and outcome-pricing terminology on top of both. The methodology notes lock V4-specific analytical choices — why /20 not /15, why 5 GTM-org jobs not 7 agent-workflow jobs, why cells not strata, why the Playbook is a separate EPUB, why three Bet-Cs promoted and seven absorbed, why a new outcome-pricing crux earned a slot. Reference, not narrative. Delta-pack against V1 Ch 6 and V3 Ch 6.

## §6.1 V4-Specific Glossary

Alphabetized. V4-specific terms only — every entry either does not exist in V1 / V3 glossaries or carries a materially different meaning at cell-resolution. Cross-reference V1 Ch 6 §6.1 and V3 Ch 6 §6.1 for base vocabulary.

| Term | Definition |
|---|---|
| AI Council | F1000 cross-functional standing committee chartered to approve AI vendor purchases. Stood up across F1000 between 2024 and 2025. Reads the Playbook as the canonical procedure. Bet #1's primary published reader. |
| Article 14 tie-out | Documented mapping from the EU AI Act Article 14 human-oversight requirement to specific agent-product affordances (action-confirmation, rollback, sub-agent privilege separation). Bet-C10 absorbed as Playbook §III.6 overlay. |
| Bet-C / candidate bet | Bet candidate surfaced by Wave 2 synthesis. Ten candidates surfaced; three promoted (C5 Common Room, C8 Deal-Diagnosis, C9 Memory-as-Service); seven absorbed or parked (C1, C2, C3, C4, C6, C7, C10). |
| Bilateral evidence pack | Signed reproducible eval report format that becomes the canonical downloadable Playbook artifact. Buyer requests; vendor returns. Includes model pin, dataset hash, harness version, chain-of-custody. Distinguishes Bet #1 from generic AI procurement guidance. |
| Buyer-side procurement scar-tissue | Alex's 12-year accumulated knowledge of how F1000 procurement actually runs at the seam between InfoSec, Legal, and the business sponsor. The Process Power flavor of Bet #1. Most NYC GTM talent does not carry this. |
| Cell | A function × capability intersection in the 12 × 13 matrix. 156 total. Each cell is a specific GTM-function-buys-this-capability conversation surface. |
| Cell of record | The (9, G) cell — deal-desk × multi-step task execution — scoring OCQ 19/20. The matrix peak. The published Playbook's surface area maps directly to this cell. |
| Cell coordinate notation | `(function#, capability_letter)` — e.g. `(9, G)` for deal-desk × multi-step execution; `(6, L)` for AE × persistent memory; `(11, H)` for renewals × forecasting decision support. |
| Cell-coverage | The number of cells a framework finding or bet re-rates. The fourth dimension added to OCQ scoring at V4 resolution. |
| Counterparty history memory | Persistent agent memory of a single buyer-counterparty across multiple deal cycles. Anchors cell (9, L). Bet-C9 productization vector. |
| Cross-counterparty workflow | The procurement-gauntlet workflow that moves a vendor evaluation across the seven counterparties. No incumbent owns this workflow at agent-specific resolution. The (9, G) opportunity. |
| Density | The fourth OCQ-Opportunity sub-dimension added at V4. How dense the vendor landscape is at this cell — Forming (no incumbent), Mature (contested), Saturated (incumbent locked in). |
| Forming / Mature / Saturated / Gap cell states | The four cell-density states. Forming = no incumbent; Mature = multiple contenders, no winner; Saturated = incumbent locked in; Gap = no vendor at all. Pattern-read across the matrix in Ch 1 §1.5. |
| Function vs Capability terminology | Row vs column of the cell matrix. Functions = 12 GTM-organization roles (demand-gen / content / inbound-PLG / outbound-SDR / ABM / new-business AE / enablement / RevOps / deal-desk / CS / AM-renewals / forecasting-strategy). Capabilities = 13 agent-product affordances (A–M). |
| Gateway control plane | Cloudflare AI Gateway / Kong / Pomerium — where Bet #3a's Switching Costs power lives. The MCP-adjacent layer that survives a fork because the gateway-control-plane advisory works on either schema. |
| Heat-map clustering | The Cell Matrix Heatmap (Plate 1) reveals clusters where OCQ scores concentrate — the deal-desk row (function 9), the L-column (persistent memory across multiple functions), the G-column (multi-step execution at deal-desk + RevOps). Visual evidence for the cell-coverage pattern read. |
| MBB feed-stock | The third career-feed-stock for Bet #2 (after Stripe/Ramp/Datadog and foundation-lab AE departures). Berger BCG → Hebbia Feb 2026, Park McKinsey → Sierra Mar 2026, Sinclair Bain → Harvey Apr 2026. Activated; trigger D fires on any new analog hire. |
| OCQ /20 (vs V1's /15) | V4's four-dimensional OCQ scoring. Each lens (Opportunity / Challenge / Open Question) scored 1–5 on four sub-dimensions. Total /20. V4-specific because the cell-matrix resolution surfaces the Density / Time-Sensitivity / Cell-Coverage fourth dimensions. |
| Open-spec stewardship | The maintainer role Bet #1 absorbs via Bet-C6 reframe. Process Power flavor — the first credible publisher of the open-spec AI Vendor Procurement Standard sets the procurement default for the next 5 years. |
| Outcome-pricing | Pricing model where vendor revenue depends on a measurable outcome — per-resolution (Sierra $1–4 / resolution), per-task, per-conversation ($2 / conversation Agentforce list), hybrid floor-plus-outcome. Triggered Crux #6 at V4 (sustainable or vapor?). Decidability Q4 2026. |
| Per-resolution / per-task pricing | The two dominant outcome-pricing units in the vertical-agent CX category. Klarna's 2024 reversal precedent is the load-bearing falsifiability event for the sustainability question. |
| Procurement gauntlet | The F1000 AI procurement cycle. V1 framing: generic. V3 framing: six counterparties + seven agent-specific overlays. V4 framing: seven counterparties (V3's six plus Enterprise Architecture / IT Ops) anchored around the (9, G) cell. |
| Procurement seam | The handoff joints between the seven counterparties — InfoSec → Legal, Legal → Privacy, AI Governance → Business Sponsor — where Alex's Process Power scar-tissue is most claimable. The conversational substrate of the Playbook. |
| Saturated vs Mature vs Forming vs Gap | See Forming / Mature / Saturated / Gap cell states above. The four states are the V4 cell-density classification used in the quarterly cell-coverage audit (Ch 5 §5.1 check 2). |
| Seven counterparties | The F1000 AI procurement gauntlet at V4 framing: InfoSec, Legal, Privacy, AI Governance, Procurement, Business Sponsor, Enterprise Architecture / IT Ops. The seventh (EA/IT Ops) is V4's addition over V3's six. Each gets a chapter in Playbook Section II. |

## §6.2 V4-Specific Sources

V1 Ch 6 §6.2 covers the field-wide rotation (IEA Electricity, EPRI, PJM, NVIDIA earnings, SemiAnalysis, Air Street State of AI, Pallet, Stratechery, Latent Space, framework lineage books). V3 Ch 6 §6.2 covers the agent-specific rotation (OSWorld leaderboards, MCP governance, agent-specific company watch, Anthropic RSP, EU AI Act Article 55). Both carry forward unchanged. V4 adds the cell-coverage and outcome-pricing layer below.

### Cell-coverage company watch URLs

Grouped by anchor cell. Add to the existing V1/V3 rotation.

- **(3, A+L+F), (5, F) buying-committee graph / PLG fusion**: Common Room, Pocus, Endgame. Common Room roadmap reveal = Bet-C5 decidability.
- **(4, A) outbound SDR research / enrichment**: Clay (NYC), Apollo, ZoomInfo. Clay is the only durable RevOps winner per F4.
- **(1, B), (2, B), (2, L) demand-gen / content personalization**: Mutiny, Jasper, Writer.
- **(4, B) outbound SDR personalization + content**: 11x (F2 most-over-rated), AiSDR, Artisan.
- **(4, K), (6, K) computer use across SDR + AE**: Anthropic Computer Use, OpenAI Operator, Browser Use. OSWorld 65% is the K-column trigger.
- **M-column observability — (4, M), (6, M), (9, M), (12, M)**: LangSmith, Braintrust, Galileo, Arize, Langfuse.
- **(10, D) CX conversation handling — the outcome-pricing front line**: Sierra, Decagon, Intercom Fin, Ada, Forethought. Trigger A fires here first.
- **(9, G) the cell of record**: Loopio, Responsive, Arphie, Ironclad, Vanta, Drata, Secureframe. Trigger B fires here.
- **(6, A) new-business AE research**: Hebbia (NYC Bet #2 #1), Rogo (NYC #3), Glean, Crayon.
- **(6, E) new-business AE meeting prep / follow-up**: Gong, Chorus, Outreach. Bet-C8 watches for a credible startup here.

### Outcome-pricing observability sources

Crux #6 watch sources:

- **Klarna 2024 reversal precedent** — historical analog; falsifiability anchor.
- **Sierra** — $1–4 / resolution; Bret Taylor commentary, The Information.
- **Decagon** — hybrid floor-plus-outcome; quarterly investor updates.
- **Intercom Fin** — $0.99 / resolution list; McCabe commentary.
- **Hippocratic AI** — $9 / hour (per-time, not outcome); Munjal Shah interviews.
- **Salesforce Agentforce** — $2 / conversation list; Dreamforce announcements.
- **SOX revenue-recognition guidance** — Big-4 whitepapers. Non-vendor source most-likely to fire Crux #6.

### Procurement-specific sources

- **Vanta / Drata / Secureframe AI-vendor roadmaps** — Risk GR3 watch.
- **Ironclad / LinkSquares / SpotDraft AI-vendor-clause-library** — Trigger B. Watch product-release blogs.
- **Cloudflare AI Gateway / Workers MCP** — Bet #3a gateway-partner source.
- **Kong / Pomerium MCP gateway launches** — Bet #3a comparison points.

### Regulatory primary sources (cell-relevant)

V3 §6.2 covers EU AI Act / SB 53 / Colorado / Texas. V4 adds:

- **FTC Operation AI Comply** — re-prices M-column and (9, G) cells.
- **CCPA Nov 2025 ADMT rulemaking** — hits L-column and M-column cells.
- **EU AI Act Article 14 enforcement window late 2026** — Crux GC3 + Trigger E.
- **TCPA / CAN-SPAM** — M-column compliance for SDR.

## §6.3 V4 Methodology Notes

V1 §6.3 covers field-wide methodology (meta-strata wrap not stack, /15 OCQ, conviction-star calibration, falsifiability, time-discipline). V3 §6.3 covers agent-layer methodology (14 sub-strata, 7 JTBD jobs vs V1's 6, Bet #3 reframe, memory fold-in to Bet #5, Procurement Rubric as new artifact, OSWorld sub-crux). Both carry forward. V4 adds six V4-specific decisions below.

### §6.3.1 Why OCQ /20 not /15 at V4

V1 scored OCQ /15 across three sub-dimensions per lens (V1 §6.3). V3 carried that forward. V4 adds a fourth dimension per lens because cell-resolution surfaces a question stratum-resolution hid — how dense the vendor landscape is at this specific cell. **Density** for Opportunity (Forming / Mature / Saturated / Gap distinguishes Bet-claimable from already-lost), **Time-Sensitivity** for Challenge (some cells degrade in months, others in years), **Cell-Coverage** for Open Question (how many other cells the answer re-rates). Each lens scored 1–5 on four dimensions; total /20. The (9, G) cell at 19/20 is one point off the ceiling — Time-Sensitivity is the missing point because the Vanta / Drata / Ironclad ship event compresses the window.

### §6.3.2 Why 5 GTM-org jobs not 7 agent-workflow jobs

Different unit of analysis. V3 jobs are agent-augmented-workflow-level (conceive demand → generate opportunity → progress and close → procure → onboard → retain → expand). V4 jobs are GTM-organization-shape-level (hit the number / hit next year without doubling heads / make the motion legible / defend NRR / stay current). Cross-walk in Addendum X.5: V4 Job 1 ≅ V3 Jobs 1–3 collapsed; V4 Job 2 ≅ V3 Job 5 capital-efficiency framed; V4 Job 4 ≅ V3 Jobs 6–7; V4 Job 5 is V4-specific. Five at GTM-org shape matches cells to organizational buyers; seven at agent-workflow scale matches agents to workflow steps. Both retained.

### §6.3.3 Why cell-coordinates instead of strata

The function × capability intersection is what Alex's buyer experiences. A CFO does not buy "the agent layer"; she buys "the renewal-forecasting agent reads our last four quarters of CRM hygiene, predicts decay, and surfaces accounts at risk before QBR" — cells (11, A), (11, F), (11, H), (11, L) bundled. V1/V3's stratum framing is the field map; V4's cell framing is the conversation surface. V4 cell-coordinates do not replace V3 sub-strata or V1 strata; they are an orthogonal cut for a different operating purpose (selling to a buyer, not mapping the field).

### §6.3.4 Why the Playbook is a separate EPUB

Different audience, different cadence, different governance. The workbook (`AGENTS_GTM_MASTER.epub`) has an audience of one (Alex), updates monthly, governed alone. The Playbook (`AI_VENDOR_PROCUREMENT_PLAYBOOK.epub`) has an F1000-counterparty audience at scale, updates event-driven (new EU enforcement, new clause library), and once published commits to open-spec stewardship — version-bumps follow a published changelog. Mixing artifacts would degrade both: workbook candor would constrain Playbook publication; Playbook framing would attenuate workbook utility.

### §6.3.5 Why 3 Bet-Cs promoted and 7 absorbed

Three independent screens had to clear before promotion: (a) Helmer 7 Powers — does the candidate accumulate durable Power independent of the parent bet? (b) JTBD coverage — does it serve a job no parent bet serves? (c) Wardley evolution stage — is it Settle-quadrant rather than Pioneer? C5 (Common Room operator path) cleared all three. C8 (Deal-Diagnosis Causation Engine) cleared (b) but is Watch-only until a credible startup emerges. C9 (Memory-as-Service) cleared (a) and (b) with a three-stage moat (data-integrations + GDPR-deletion + curation UI). The other seven absorbed into Bet #1 (C2/C3/C4/C6/C10) or parked (C1/C7). Absorption discipline avoids fragmenting Bet #1 — the Playbook's authority depends on it being the canonical surface, not one of several competing spec surfaces.

### §6.3.6 The new V4 outcome-pricing crux

Crux #6 (outcome-pricing sustainable or vapor) earned a slot beyond V3's five because it is load-bearing for two bets simultaneously. Bet #2 timing accelerates if outcome-pricing holds; sign-window narrows if it collapses to seat-based floors. Bet-C9 productization gates on the same question — Memory-as-Service economics depend on outcome-pricing viability. V3 had no analogous pricing question because V3's bets do not depend on vendor revenue mechanics. Klarna 2024 reversal is the historical anchor; Sierra-Decagon-Intercom-Fin earnings cadence is the decidability path; Q4 2026 SOX rev-rec guidance is the horizon. Decidability + asymmetry + bet-size + cell-coverage all clear the threshold; pricing as a Crux is V4's most original analytical contribution.

## §6.4 Update Protocol

Defers to V1 Ch 5 §5.1–§5.4 for master cadences, V3 Ch 5 for agent-layer overlays, and V4 Ch 5 for V4-specific add-ons. V4 ride-alongs: V1 monthly fires the V4 monthly if any cell-status changed; V1 quarterly fires the V3 delta-audit and the V4 cell-resolution add-on in sequence. V4 triggers fire on cell-resolution and outcome-pricing watches (Ch 5 §5.2 A–E). Playbook publication ritual (Ch 5 §5.3) is one-time Q3 2026 Week 12.

Version-bump rule (inherits V1 §6.4): minor for content additions / single re-rates; major for taxonomy change (renumbering functions/capabilities, retiring a Bet-C, adding a crux, changing OCQ /20 dimensions). Divergence rule (inherits V3 §6.4): if V4 logs a change without parallel V3 §4.2 and V1 §4.2 updates in the same session, trackers have diverged — fix before next monthly. Most likely V4 major-version trigger: Crux GC3 resolving "teeth" and re-rating Bet #1 TAM 5×; second: Crux #6 resolving and re-rating Bet #2 + Bet-C9 simultaneously.

## §6.5 Change Log

V1 changes log in V1 §6.5; V3 changes log in V3 §6.5; do not duplicate either.

| Date | Version | Change | Driver |
|---|---|---|---|
| 2026-05-20 | 1.0 | Initial V4 consolidation: produces TWO EPUBs (workbook + Procurement Playbook). Cell-resolution refresh of the 7 Bets — Bet #1 absorbs Bets #4 + #5 + Bet-Cs (C2/C3/C4/C6/C10) as modules; Bet #3 splits into 3a (concurrent advisory + gateway-partner) and 3b (parked productized); Bet #6 reframed as distribution layer. Three Bet-Cs promoted (C5 Common Room, C8 Deal-Diagnosis, C9 Memory-as-Service); seven absorbed or parked. New crux #6 (outcome-pricing economics sustainable or vapor) added beyond V3's five. OCQ scoring moved to /20 (four dimensions per lens; Density / Time-Sensitivity / Cell-Coverage added). 5 GTM-org jobs replace V3's 7 agent-workflow jobs at the GTM-organization unit of analysis. | The cell matrix surfaced the operating plan V3 implied. |
| _next_ | _next_ | _Bi-weekly: tracker syncs do not log here. Monthly: only if a cell status changed or a bet conviction moved. Quarterly: cell-coverage audit yes per Ch 5 §5.1. Twice-yearly: re-extract from wave files + plate regeneration + spec version bump._ | — |

Most likely first row to land after 1.0: Crux GC1 (OSWorld 65%) resolving Q3 2026 and propagating to K-column cells (cells with capability K computer-use) across functions 4, 6, 10. Second-most-likely: Crux GC2 (Anthropic ARR $24B vs $30B) resolving Q3 2026 and re-pricing Bet #2 timing. Third: the Playbook publish at Q3 2026 Week 12 itself, which fires Bet #1's falsifiability evaluation 60 days later.

## Apply

Open V1 §6.1 (foundation glossary), V3 §6.1 (agent-specific glossary), and V4 §6.1 (cell-resolution glossary). Pick one term from each layer that you stumble on when speaking to it — V1 might be MFU, NCCL, or LPO; V3 might be sub-agent privilege separation, indirect prompt injection, or per-trajectory cost; V4 might be bilateral evidence pack, open-spec stewardship, or cell-coverage. Write a two-sentence cleaner explanation for each. The glossary is for your future self; the explanations are for the next buyer you talk to. If you cannot write the two-sentence explanation, the term has not yet earned a place in your operating vocabulary — and the cell, the bet, or the ritual that depends on it is correspondingly under-grounded.
