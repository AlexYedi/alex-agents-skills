# F1 — Wardley Map of the Agent × GTM Matrix

**Date:** 2026-05-13 · **Principal:** Alex Yedi · **Scope:** Extends Session A's `B5_wardley.md` from the agent stack writ-large to the 12×13 agent-GTM matrix at cell resolution. Anchors four GTM-buyer needs; traces them through Function → Capability → Sub-stratum → Meta; places named tools on the evolution axis; calls 6 punctuated equilibria; positions Alex.

---

## 1. What Wardley says about agent-GTM specifically now

Agent-GTM is not consolidating; it is **stratifying along the capability columns, not the function rows.** The substrate (functions 1–12) is largely Product/Commodity already — every GTM motion has incumbent SaaS that an agent capability *attaches to*. Where evolution is fast is in the capability columns: G (multi-step execution), K (computer-use), L (persistent memory), M (trajectory observability). These four columns are where stage-jumps happen in 2026–2027. The conventional "vertical AI eats SaaS" framing misreads the map — verticals are reskinning Product-stage SaaS with Custom-stage agent capabilities and pricing the *capability lift*, not the substrate. **The interesting positions are where a Custom-stage column attaches to a Product-stage function and the seam is procurable.** That seam — capability-attached-to-function-via-procurement-evidence — is the whole map's gravitational center, and it sits at (9,G). Everything else orbits.

A second hard truth Wardley forces: **roughly 85% of the named matrix lives at sub-stratum IX (vertical agent products).** That means cell-by-cell evolution is *gated* by IX vendor roadmaps. The thin slivers of II (runtime — Anthropic CU, Operator, Mariner), IV (memory — Mem0/Letta/Zep), VII (eval — LangSmith/Braintrust/Galileo/Arize), VIII (safety — Lakera/Protect AI) are where Genesis still lives. Those slivers are exactly what Bets #1, #4, #5 target.

---

## 2. The four anchored user needs and their dependency chains

**Need 1 — "Fill the top of the sales funnel reliably without scaling headcount linearly."**
- GTM Function: **4 (Outbound SDR)** primarily; touches **3 (Inbound/PLG)** and **5 (ABM)**.
- Agent Capability: **A (research)** → **C (orchestration)** → **G (multi-step execution)** with **K (computer-use)** unlocking next-stage gains.
- Sub-stratum dependencies: **IX** (Clay, Apollo, 11x, Outreach, Common Room) over **II** (Anthropic CU / Operator for LinkedIn-Sales-Nav GUI driving once OSWorld 65% crosses) and **IV** (memory across prospects, currently absorbed as feature).
- Meta-layer dependencies: **TCPA / CAN-SPAM / GDPR / EU Article 14** force (4,M) trajectory observability into the chain by late 2026; LinkedIn ToS / data-graph control sits one layer above as a regulatory-adjacent constraint that *kills the dependency chain wholesale* if Microsoft pulls API access from non-MS-shop CU agents.
- **Wardley read:** chain is Product-heavy at the substrate, with two Genesis components (CU + cross-prospect memory) and one Custom component (M-column SDR-shape eval). The bottleneck is (4,M), not (4,A).

**Need 2 — "Compress enterprise sales cycle by clearing the procurement gauntlet faster."**
- GTM Function: **9 (Deal desk / pricing / procurement)** primarily; touches **6 (AE)** for upstream prep and **8 (RevOps)** for evidence assembly.
- Agent Capability: **G (multi-step execution at the procurement seam)** is the load-bearing one; **M (trajectory observability)** is the procurement-evidence currency; **I (negotiation / contractual)** is the contract-addendum overlay; **L (counterparty memory)** is the residual deal-desk asset.
- Sub-stratum dependencies: **IX** (Loopio, Responsive, Arphie, Ironclad, Vanta, Drata, Vendr, Tropic) over **VII** (Galileo, Arize, Langfuse for trajectory evidence) over **VIII** (Lakera / Protect AI safety attestations).
- Meta-layer dependencies: **EU AI Act Article 14 enforcement (late 2026 / Q1 2027)** is the single regulatory variable that turns this from advisory niche into a $10B+ category. **SOX rev-rec** sits underneath (11,I) outcome-pricing dispute mechanics.
- **Wardley read:** **(9,G) is in Genesis-to-early-Custom; the bundle does not exist turnkey.** This is the map's most-claimable cell and matches the parent tracker's Bet #1 anchor.

**Need 3 — "Increase NRR through proactive customer-success interventions."**
- GTM Function: **10 (CS/onboarding)**, **11 (AM/renewals/expansion)**.
- Agent Capability: **D (conversation handling)** at scale, **G (multi-step execution)** for refund/account-change loops, **L (persistent memory across renewal cycle)**, **I (outcome-priced) negotiation** at the renewal seam.
- Sub-stratum dependencies: **IX** (Sierra, Decagon, Intercom Fin, Gainsight, Ada, Hippocratic) over **IV** (Mem0/Letta/Zep dev-side only — not picked up by IX as of May 2026), over **VII / VIII** (audit / safety).
- Meta-layer dependencies: **GDPR right-to-be-forgotten in agent memory** + **outcome-pricing SOX rev-rec** + Bret-Taylor outcome-pricing thesis as the economic precedent.
- **Wardley read:** (10,D) is **the densest Product-stage cell in the matrix by dollars**. The Custom layer that matters is (11,L) durable cross-quarter memory — and **no IX vendor ships it production-shape**. That is the soft spot.

**Need 4 — "Produce accurate quarterly forecasts the board will trust."**
- GTM Function: **12 (Forecasting/strategy)**; touches **8 (RevOps)** for inputs.
- Agent Capability: **H (forecasting/decision support)** primary, **F (cross-system retrieval)** for narrative, **L (8-quarter pipeline-decay memory)**, **M (forecasting-agent drift observability)**.
- Sub-stratum dependencies: **IX** (Clari, BoostUp, Aviso, Gong Forecast, SF Einstein) over **IV** (memory) over **VII** (drift detection).
- Meta-layer dependencies: **Accountability cap** — CRO cannot blame an agent for a missed forecast (C5 finding); **SOX-adjacent CFO-controls** on AI-touched financial outputs.
- **Wardley read:** (12,H) is Product-stage saturated; honest lift is 5–15% MAPE. The Custom layer is (12,L) memory + (12,M) drift, both Genesis. The accountability cap is a *meta-layer ceiling* that prevents this column from ever fully commoditizing into autonomous-agent territory.

---

## 3. Component placement on the evolution axis

Stage scale: **Genesis → Custom-Built → Product/Rental → Commodity-Utility.** All placements are at May 2026.

**Late Genesis (write/observe; do not productize yet):**
- (9,G) **Agent procurement gauntlet bilateral evidence pack** — Loopio/Responsive/Arphie at content-only; Ironclad/Vanta/Drata at controls-only; zero of seven overlays ship turnkey. **OCQ 19/20.** [IX/VII/VIII]
- (4,M) **SDR-shape trajectory observability for TCPA/CAN-SPAM** — LangSmith/Braintrust/Galileo eng-shape only; no GTM-shape vendor. [VII]
- (9,M) **Deal-desk agent-trajectory signed evidence pack** — Galileo/Arize/Langfuse eng-shape only. [VII]
- (11,L) **Multi-quarter durable agent memory for renewal motion** — Sierra "Memory" is RAG-with-writes, not memory; Mem0/Letta/Zep dev-side only. [IV/IX]
- (6,L) **6–9 month AE deal-cycle memory** — same gap, AE-shape. [IV]
- (5,F) **Dynamic 9-person buying-committee graph** — Common Room community-only; ZoomInfo/Sales Nav static. [IX]
- (6,E) **Deal-diagnosis causation** — Gong sees activity, Einstein pattern-matches; no one ships causation @ confidence interval. [IX/VII]
- (1,M) (2,M) (3,M) **Marketing-shape trajectory observability** — FTC AI-washing + EU Art. 50. [VII]

**Early Custom (bespoke deployments; replicable pattern emerging):**
- (4,K) **LinkedIn / Sales Nav GUI driving via CU** — Anthropic CU, Operator, Mariner all under OSWorld 65%; Nooks closest in-segment. [II/VI]
- (6,K) **AE motion GUI driving** — MS Sales Copilot has structural advantage (LinkedIn graph + M365 + Dynamics + Outlook first-party). [II/IX]
- (8,G) **RevOps pipeline-scrub loop closure** — Clari/BoostUp/Aviso ship pieces; no one closes the loop. [IX]
- (11,I) **Outcome-based pricing operator playbook** — Sierra ($1–4/res), Decagon hybrid, Intercom Fin ($0.99 list), Hippocratic ($9/hr), SF Agentforce ($2/conv-retreated). [IX]
- (9,I) **AI-specific contract addendum library** — Ironclad/LinkSquares/SpotDraft/Lexion/Evisort roadmap-committed Q2'26; 12–15 clauses still unbuilt. [IX]
- (7,J+M) **Trajectory-grade procurement-seam enablement coach** — Highspot AI / MindTickle Copilot / Hyperbound coach call surface, not procurement seam. [IX/VII]
- (12,L) **8-quarter pipeline-decay memory** — BoostUp Forecasting Health structural; Mem0/Letta/Zep unadopted. [IX/IV]

**Late Custom → early Product:**
- (3,A+L+F) **PLG signal + memory + CRM hygiene** — Common Room $30M ARR May'26; Pocus, Endgame (Salesloft). [IX]
- (4,A) **SDR research/enrichment** — Clay $100M @ $1.5B Jan'26 = winner-eats-most. [IX]
- (8,F) **CRM hygiene multi-tenant write governance** — Syft/Default/Truva/Clari Copilot/Einstein 1. [IX]
- (6,A) **AE pre-call brief** — MS Sales Copilot, Agentforce, Gong Engage, **Hebbia, Rogo, Glean**. [IX]
- (10,G) **CS multi-step refund/account-change** — Sierra/Decagon ship; OSWorld-gated for cross-tool. [IX/X]
- (12,F) **Forecasting narrative retrieval** — Gong "Deal Stories" widely adopted. [IX]
- **MCP gateways** — Cloudflare/Kong/Pomerium, F500 design partners. [II]

**Product/Rental:**
- (10,D) **Tier-1/2 customer-service issue resolution** — Sierra ($175M+ ARR), Decagon ($80M+), Intercom Fin, Ada, Forethought, Hippocratic, SF Agentforce, HubSpot Service. **Densest cell in the matrix by dollars.** [IX]
- (4,B) (4,C) **SDR content + cadences** — 11x flat $20M signals ceiling; Outreach/Salesloft/Apollo cadence-as-feature. [IX]
- (2,B) **Content/SEO generation** — Jasper/Writer/Copy.ai; Google E-E-A-T suppression risk. [IX]
- (12,H) **Forecasting decision support** — Clari/BoostUp/Aviso/Gong Forecast/Einstein; honest 5–15% MAPE lift. [IX]
- (7,A–E) **Enablement content & coaching** — Highspot/Seismic/MindTickle/Gong/Granola. [IX]
- (6,J) **AE coaching** — Gong/Chorus/Aircover/Cresta/MindTickle/Hyperbound. [IX]
- **Microsoft 365 Copilot for Sales** — 30M+ paid seats, $5B+ ARR Q1'26; cross-funnel cell coverage breadth. [IX/X]
- **Salesforce Agentforce** — every M=1–12 GTM cell; AgentExchange Dec'25. [IX]
- **Glean** — $50M → $300M+ Q1'26; Series E $260M @ $7.2B. [IX]

**Late Product → Commodity:**
- LangSmith / Braintrust / Galileo / Arize tracing (eng-shape) — OTel GenAI stabilized Jan'26. [VII]
- Voice substrate (LiveKit / Cartesia / Deepgram / Twilio) for (10,D) telephony. [II/VI]
- Sandboxes (E2B, Modal, Vercel) under (10,G) / (8,G) tool execution. [II]
- Foundation-model API calls under every cell. [I]

**Pattern:** Vertical-agent IX vendors at Product; the matrix's *interesting* cells are where Genesis II/IV/VII/VIII slivers must attach to those Product-stage substrates. **The bottleneck is always the Genesis component, never the Product substrate.** This is the single most useful lens for picking where to claim.

---

## 4. The six punctuated equilibria 2026–2027

**PE-1. OSWorld 65% crossed on a frontier system. (Q3 2026 expected, Crux C3.)**
- Trigger: Anthropic CU 4.5 / GPT-Operator-2 / Mariner 1.5 public scoreboard event.
- Cells repriced: **(4,K), (6,K), (8,K), (9,K), (10,K), (11,K), (12,K)** — the entire K-column moves from Genesis to Custom-deployable for *narrow lanes*. Computer-use unlocks Coupa/Ariba/Workday Procurement automation (9,K), LinkedIn/Sales Nav driving (4,K), AE motion driving (6,K), BI/spreadsheet board-deck assembly (12,K).
- Winner-by-default: **Microsoft Sales Copilot** owns LinkedIn graph + M365 + Dynamics + Outlook first-party. Standalone CU plays survive only on non-LinkedIn signal layer or non-MS-shop AE stack. **Bet #2 NYC targets that aren't MS-shop ride this.**
- Adjacent-possible: BPO-shape services billed per-completed-trajectory at 1/5 cost; reprices UiPath/Automation Anywhere; AI-augmented click-bot shapes the (8,G) RevOps loop closure.

**PE-2. EU AI Act Article 14 first enforcement action. (Late 2026 / Q1 2027, Crux C4.)**
- Trigger: Commission Art. 14 enforcement; first GPAI fine. Draft conformity Feb 2026 names Inspect AI explicitly.
- Cells repriced: **(9,G), (9,M), (4,M), (6,M), (10,M), (11,M), (12,M)** — the entire M-column flips from "would-be-nice procurement evidence" to "regulatorily mandatory." Bet #1 TAM expands 5x.
- Adjacent-possible: Open-spec stewardship of the Article 14 Tie-Out Standard (Bet-C10 from the synthesis); first credible publisher = procurement default for next five years. **This is Bet #1's most asymmetric outcome.**

**PE-3. Sierra ARR crosses $500M. (Mid-2027 expected; $175M+ Q1'26 at 400% YoY.)**
- Trigger: Sierra disclosure / The Information leak.
- Cells repriced: **(10,D), (10,G), (10,L), (11,I), (11,L)** — vertical-agent Product → late-Product / early-Commodity at the *top* of the stack. Sets reference pricing for outcome-priced agent contracts F500-wide. Reprices Bet #2 NYC target equity bands upward (Hebbia, Rogo, Decagon ride the comp).
- Adjacent-possible: SOX rev-rec dispute mechanics for outcome pricing (Bet-C4); outcome-pricing contract template becomes the procurement-side counterpart Alex can plant a flag on.

**PE-4. MCP gateway sub-category solidifies as Product. (H2 2026, Crux C2.)**
- Trigger: Cloudflare MCP Gateway GA, Kong v2, Pomerium identity-aware proxy at named F500.
- Cells repriced: **(9,G), (4,K), (6,K), (8,F), (8,K), (10,K), (11,K)** — auth/audit/rate-limit/secret-injection control plane hardens; gateway-control-plane TAM forms a distinct line. Sub-stratum III (tool-use protocol) crosses Custom → Product.
- Adjacent-possible: MCP-native iPaaS (Zapier-replacement); F500-private MCP registries; **Bet #3 reframed-target** — advisory + gateway-adjacent positioning at Cloudflare/Kong is the canonical Settle move.

**PE-5. Anthropic ARR Q3 2026 resolution. (Q3 2026, Crux C1.)**
- Trigger: Anthropic audited disclosure / leak; resolves $24B vs $30B.
- Cells repriced: **all IX cells across the matrix** via comp-set vibration. Lower bound = Sierra $10B → $6–8B compression, Hebbia/Rogo C-round equity bands tighten 20–30%, vertical-agent operator-equity window compresses. Upper bound = Bet #2 timing accelerates; Hebbia/Rogo up-round before EOY 2026 likely.
- **First-mover-window-closing event:** if Alex wants Bet #2 equity asymmetry at Hebbia/Rogo/Augment, he signs *before* this resolution if conviction is high; *after* if wobbly. The window is ~6 months wide.

**PE-6. Microsoft 365 Copilot crosses $10B ARR run-rate. (H1 2027 expected; $5B+ Q1'26.)**
- Trigger: Microsoft disclosure (FY27 earnings).
- Cells repriced: **horizontal suite floor solidifies across (1–12, A–F) cells** — every cell where M365 + Dynamics + Graph + Purview attaches. Reprices (4,A) Clay-class wedges as MS-encroached at the low end; reprices Glean (10,A)/(6,A) competing M365 directly; locks in MS-shop AE cells (6,K). **The horizontal-vs-vertical battle is decided in favor of "suite floor + vertical wedge + gateway underneath" (C6 §4 prediction confirmed).**
- Adjacent-possible: non-MS-shop GTM stacks (Salesforce + Gmail + Outreach + Slack + Notion) become the durable Bet #2 / Bet #3 target geography.

**Watchlist (probable but not yet sufficient):** Ironclad / Vanta / Drata Q4 2026 AI-vendor-bundle launch (falsifies Bet #1 productized branch — Tension T4 in the synthesis); AWS Bedrock auto-routing default-on H2 2027 (closes Bet #4 per-token + per-trajectory window).

---

## 5. Strategic quadrants for Alex

**PIONEER (Genesis cells; Alex's first-mover wins; write+publish, do not productize-as-SaaS yet):**
- **(9,G) Agent procurement gauntlet bilateral evidence pack.** OCQ 19. The Playbook draft (9,700 words) is already half the artifact. No incumbent. Article 14 enforcement closes the door on incumbents late 2026.
- **(9,M) Deal-desk trajectory evidence pack as open-spec.** Sister cell to (9,G); Part XIII §3 of the addendum.
- **(11,I) Outcome-based pricing operator playbook.** Dual-telemetry / 30/60/90 dispute / third-party arbitration template; CFO/Procurement-shape. F6 §7 nominates this as the highest-leverage Bet #1 wedge.
- **(4,M) SDR trajectory observability for regulatory mandates.** TCPA/CAN-SPAM/GDPR/CASL/EU Art. 14. No SDR-shape vendor exists May 2026.
- **(7,J+M) Trajectory-grade enablement coach for procurement-seam work.** Accident-of-light cell from the synthesis; sharpens Bet #1's distribution.

**SETTLE (Custom → Product cells; established practice compounds; productize what works):**
- **(4,A) RevOps adjacency** — operator role at Clay, Common Room, or Pocus. Clay $100M @ $1.5B = winner-eats-most. Alex's commercial fluency adds at the orchestration-pattern layer.
- **(6,A) + (12,F) Hebbia / Rogo operator role.** F4 ranks Hebbia #1 NYC composite (under-funded ratio 2.5–5%, 0.20–0.40% equity, MBB+Stripe-flavored buyer, 2-quarter window before Series C). Rogo #3.
- **(11,I) + (10,D) Sierra / Decagon operator role.** Sierra Head Enterprise GTM East (Schmidt anchor + Taylor monthly NYC). Brand-prestige + cleanest secondary-liquidity.
- **(12,H) forecasting overlay** — Bet #1 procurement module specifically targeting forecasting-vendor evaluation (T8 in the synthesis: the Aviso/Clari dispute is a Playbook chapter waiting to happen).
- **(3,A+L+F) Common Room operator role** as the (5,F) BCG candidate-from-the-inside (Bet-C5).

**TOWN-PLAN / CONSUME (Product → Commodity cells; rent, don't build, mostly avoid as a claim target):**
- (4,B) SDR content generation, (2,B) content/SEO generation — most-commoditized cells; CAC-drag warning.
- (10,D) help-desk volume — Sierra/Decagon/Intercom Fin/Ada saturate; Klarna reversal already reset budgets.
- (7,A–E) enablement content — Highspot/Seismic/MindTickle/Gong saturate.
- (4,C) (6,C) cadences — Outreach/Salesloft/Apollo absorb cadences-as-feature.
- Sandboxes (E2B/Modal/Vercel), voice substrate (LiveKit/Cartesia/Deepgram), browser automation (Browserbase/Playwright), OTel GenAI tracing — rent silently; differentiation zero.

**PARTNER (cells where someone else builds; Alex's commercial fluency adds leverage):**
- **Cloudflare MCP Gateway / Kong / Pomerium** — gateway-control-plane advisory layer; F100 InfoSec/AI-Governance/Legal triad in 90 days. Bet #3 reframed-target.
- **Common Room** ↔ (5,F) committee graph; operator-from-inside or advisor-from-outside.
- **Hebbia / Rogo** ↔ (6,A) + (12,F) enterprise vertical-data wedge.
- **Galileo / Arize / Langfuse** ↔ (4,M) (9,M) trajectory observability productization (eng-shape vendor needs GTM-shape go-to-market — Alex is the bridge).
- **Vanta / Drata / Ironclad** ↔ (9,I) AI-specific contract addendum library — partner before they compete; the T4 tension in the synthesis says they will ship Q4 2026.

---

## 6. Implications for the 7 Bets

**Most-validated by the Wardley map: Bet #1.** Procurement-grade controls sit clearly in late Genesis at (9,G), (9,M), (4,M), (11,I). No incumbent ships turnkey. Article 14 enforcement is the punctuation (PE-2). First credible publisher = procurement-default-setter. The map *forces* Bet #1 first. **The single most asymmetric position on the map.**

**Most-threatened by the map: Bet #3 productized form.** Even the synthesis's reframed Bet #3 (advisory + gateway-adjacent) is threatened by PE-4 (MCP gateways Product H2 2026) compressing the advisory window. If Cloudflare / Kong harden the control plane before Alex publishes a positioning piece, the partnership-leverage layer eats the advisory layer. **Bet #3 must run on the same clock as Bet #1, not behind it.** This is the biggest sequencing change Wardley demands.

**Bet #2 — held with Wardley sharpening.** PE-5 (Anthropic ARR resolution) is the *single load-bearing valuation variable*. If conviction is high, sign Hebbia/Rogo *before* Q3 2026 resolution; if wobbly, *after*. PE-6 (M365 Copilot $10B) confirms non-MS-shop vertical-agent geography as durable. Sierra remains brand-prestige + secondary-liquidity play; Hebbia/Rogo remain equity-asymmetry play. **F4's composite ranking stands; the Wardley view confirms timing not target.**

**Bet #4 — held, sequencing demoted.** Per-trajectory FinOps (the agent-specific reframe) sits in the AWS Bedrock auto-routing shadow (H2 2027). Window is ≤18 months. **Fold into Bet #1 as a Playbook module rather than scale as standalone bet.** F6 §7 already lifts this; Wardley confirms.

**Bet #5 — held with cell-attachment.** Memory architecture-as-service-line anchors at (11,L) + (6,L) + (12,L). The L-column is the matrix's most consistent gap (synthesis §3). PE-5 / PE-1 don't move it; Crux C5 directly resolves it H2 2026. **Bundle with Bet #1 + Bet #4 as the "Enterprise AI Architecture Audit" three-product practice.**

**Bet #6 — held.** Newsletter as distribution layer for Bets #1/#3.

**Bet #7 — VC platform — held, deferred until 12 months.**

**Sequencing recommendation:**
1. **Bet #1 published — Weeks 1–12.** The map says first; the synthesis says first; agreement is rare.
2. **Bet #2 NYC operator role — Weeks 4–26.** Parallel-track with Bet #1; sign before Q3 2026 Anthropic ARR resolution if conviction high.
3. **Bet #3 reframed — Weeks 4–16.** Cloudflare/Kong advisory positioning piece on the same clock as Bet #1; PE-4 closes faster than expected.
4. **Bet #4 + #5 folded — Weeks 12–26.** Three-product practice with Bet #1 anchor.
5. **Bet #6 newsletter — Weeks 2–4 launch.** Distribution layer.
6. **Bet #7 VC platform — deferred Q4 2026.**

**First-mover windows closing in next 12 months:**
- **Article 14 procurement-default standard** — Q4 2026 / Q1 2027. Closes when the first F100 vendor RFP cites Vanta/Drata's AI module as the standard. **6–9 month window.**
- **Hebbia / Rogo / Augment up-round equity asymmetry** — 2-quarter window pre-Series C. Closes when Hebbia announces (rumored Q3 2026).
- **MCP gateway advisory positioning** — H2 2026. Closes when Cloudflare publishes its named-customer F100 procurement template.
- **Per-trajectory FinOps advisory** — 12–18 months. Closes when AWS Bedrock auto-routing default-on (rumored H2 2027).

---

## 7. Three open questions Wardley alone cannot answer

**Q1. Where is the *power* — at the procurement seam, at the gateway, or in the vertical-agent operator role?** Wardley places (9,G) in late Genesis and the gateway in early Product. It does not tell us which position confers durable *power* (Switching Costs, Process Power, Network Economies, Cornered Resource). **Hand off to F2 (Seven Powers):** which of Bet #1 (open-spec stewardship), Bet #2 (vertical-agent inside seat), Bet #3 (gateway-adjacent advisory) generates the most-defensible Power, and which Power flavor at each?

**Q2. Whose JTBD does the (9,G) Playbook actually satisfy — the InfoSec officer's, the CIO's, the CRO's, or the AI vendor's GTM lead's?** The map confirms the artifact is the through-line; it doesn't tell us which buyer JTBD generates the highest willingness-to-pay or the most-durable pull. **Hand off to F3 (JTBD):** rank the six (or seven, per F5) procurement counterparties by Playbook-as-product fit and forced-rank the Pioneer/Settle/Partner cells by buyer-JTBD priority.

**Q3. Can outcome pricing (11,I) — which the map places in early Custom — *export* from CX into deal-desk, AE-cycle, or renewal motions before the SOX rev-rec accountability cap binds?** Wardley sees the *evolution stage* clearly; it cannot adjudicate Tension T1 from the synthesis (Sierra-thesis exportability vs CX-only-phenomenon). **Hand off to F2 + F3:** F2 to test whether outcome pricing is a Power flavor or a pricing experiment; F3 to test whether the CFO/Procurement JTBD on dispute mechanics is large enough to underwrite Bet-C4 (Outcome-Definition Contract Template practice).

---

*End F1. ~2,420 words. Hand-off to F2 (Seven Powers) and F3 (JTBD). Cross-refs: synthesis §1 (12×13 cell map), synthesis §2 (top-15 OCQ), synthesis §3 (column convergences), synthesis §5 (Bets C1–C10), synthesis §6 (where Alex claims), OCQ_TRACKER §A Bets #1–#7, AI_AGENTS_TRACKER §A agent-layer deltas, B5_wardley (Session A; this brief extends it).*
