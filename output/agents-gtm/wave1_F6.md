# F6 — Pricing & Packaging Analysis of Agent-GTM Products

**Scope:** The four live pricing models in agent-GTM products (May 2026), named-company datapoints, recurring buyer objections, contract-term negotiation reality, compression-vs-premium forecast, ACV data table, hyperscaler-margin angle, and implications for Alex's Bet #1 procurement playbook.

---

## 0. Framing — Why Pricing Is the Real Battle in May 2026

Outcome-based is winning the headline narrative without yet winning the contract count. Bret Taylor's thesis ("Outcome-based pricing is how AI eats SaaS," Sierra; reaffirmed Feb 2026 AI Engineer Summit) is *confirmed in CX, partial in healthcare, failed elsewhere* (B4 finding). Sierra trailing-12 ARR $175M Q1'26 at 400% YoY — annualized run-rate likely $250–280M — is the proof point everyone cites, but Sierra is also the only at-scale pure-outcome agent-GTM contract. Decagon $80M+ ARR Q1'26 (The Information, Mar 2026) runs hybrid per-conversation + platform fee. Glean ($100M+ ARR, Sequoia May 2025; $250M+ Q1'26 rumored) and Harvey ($75M+ ARR Q1'26, $300M Mar 2026 raise) stayed per-seat. Cresta and Gong AI bolt outcome modules onto per-seat platforms. The market has four pricing models in active negotiation, not one — and the **per-trajectory FinOps reframe (Bet #4 split, AI_AGENTS_TRACKER §52)** is the technical mechanism that determines which model gross-margins out. F500 procurement has the *vocabulary* of outcome-based pricing but not the *measurement and dispute mechanics*. That gap is Bet #1's pricing-side surface area.

---

## 1. The Four Pricing Models — Examples and Trajectory

### 1.1 Per-Seat — The Legacy Default

Salesforce Sales Cloud ($165/user/month Enterprise; Agentforce add-on $2/conversation list, retreated to negotiated annual minimums Feb 2026), HubSpot Sales Hub Enterprise ($150/seat + Breeze Intelligence credit-pack Q1 2026), Outreach ($130–150/seat enterprise; AI Prospector GA Nov 2025 bundled in), Gong Forecast ($1,600/user/year list, ~$1,200 net) hold the per-seat baseline.

**Where it holds:** AE/CSM/manager headcount where the human is the audit trail and the CRO buyer prices off rep-count. Glean per-seat ($40–50/user enterprise; floor $35 at 5K+ seats per Reddit r/sales leak Q4 2025) holds because the buyer is IT and seat count is the procurement vocabulary.

**Where it's eroding:** When the agent does end-to-end work without a human cosignatory. 11x's flat-curve (~$20M ARR through 2024 → ~$21M Q1 2026, The Information Apr 2026) is the canonical SDR-AI saturation signal: per-seat AI SDR at $4–8K/seat hits a wall when buyers benchmark against per-meeting (Clay enrichment + outsourced SDR pods at $100–250/meeting). Salesforce's Agentforce $2/conversation pivot — then Feb 2026 retreat — tells the story: the seat is no longer the unit of work when the work is autonomous.

### 1.2 Per-Message / Per-Usage — The CX Default

Sierra, Decagon, Ada, Forethought price the CX trajectory by outcome unit. **Sierra: $1–4 per resolved conversation** (Sierra commercial deck, Twilio Customer AI roundtable Mar 2026; $1 floor high-volume retail, ~$4 regulated CX). **Decagon: $0.50–2 per conversation with $250K–500K platform minimums** (TechCrunch AT&T leak Feb 2026). **Ada and Forethought** quote $1.50–3 per resolution at $100K+ minimums.

Per-API-call exists at the developer layer: Cursor $20/seat + $0.04/request premium-model overage (GPT-5 routing GA Mar 2026); Cognition Devin $500/month for 250 ACU credits + overages (~1 ACU = 1 agent-minute). Anthropic and OpenAI exposed per-trajectory billing in Q1 2026 — Anthropic's "trace cost" view (Claude Agent SDK 2.0, Apr 2026) lets buyers see per-task fan-out cost, which restructures every per-message contract since vendors can no longer absorb a 47-call trace as opaque COGS.

**Trajectory:** Per-message consolidating around per-resolution as canonical CX unit; per-API-call fragmenting (developer surfaces tolerate it, business buyers reject as forecasting-hostile).

### 1.3 Outcome-Based — Sierra's Thesis, Tested

Sierra: deals priced exclusively on resolved-conversation outcomes, contract defining "resolved" via CSAT threshold + deflection-rate (typically 30-day post-conversation lookback). **Hippocratic AI: $9/hour RN-equivalent voice agent** (STAT News deck leak Jan 2026) — outcome-adjacent, pricing work-time not conversation, cleanest non-CX outcome contract. **Abridge: $3–8 per encounter** for ambient clinical documentation (Becker's Hospital Review Feb 2026, UPMC renewal).

**What "outcome" means contractually:** Sierra master template (per Procurement Leaders AI Summit Apr 2026 discussion) defines outcome as (a) conversation closed without human escalation, (b) CSAT ≥ pre-agreed threshold, (c) 7-day no-return-contact verification window, (d) measurement via Sierra's telemetry with quarterly buyer audit rights. The **measurement-and-dispute problem** is unsolved: vendor declares outcome, buyer has post-hoc audit rights but no real-time veto. Two F500 buyers (US bank, EU airline; off-record Mar–Apr 2026) reported 8–15% outcome-count disputes early-quarter, settled by negotiation not contract mechanism.

**Trajectory:** Outcome pricing is the dominant *narrative* but minority of *contracts*. Sierra at $175M+ ARR is the only pure-outcome at-scale agent-GTM company. Thesis cracks outside CX/healthcare: Harvey, Rogo, Hebbia explicitly refuse outcome pricing because (a) outcomes are case-specific and (b) regulated buyers won't expose outcome data to vendor telemetry.

### 1.4 Hybrid — The Pragmatic Majority

Cresta ($100M+ ARR Q1 2026, Greylock-confirmed Mar 2026) prices per-seat platform ($150–250/agent/month) + per-conversation module ($0.50–1.50 per AI-handled call) — the dominant agent-GTM CX hybrid. Gong AI Studio is $40–60/seat add-on to $1,600/user/year forecast base, with outcome-tied modules in pilot at retail (Best Buy, Macy's rumored). Decagon, while described as per-conversation, runs hybrid in practice: $250K–500K platform minimum + per-conversation overage.

**Trajectory:** Hybrid wins 2026 contract count even as outcome wins the headline. Procurement infrastructure (annual budgets, SAP/Coupa workflows) is built for fixed + variable, not pure-variable. "Predictable floor + outcome ceiling" is the path of least friction for F500 procurement.

---

## 2. Buyer Objections — The Four Recurring Patterns

**Pattern 1 — "Is this just a token markup?"** If Sierra pays Anthropic $0.10 inference per conversation and bills $2.50, am I paying 25× markup? Vendor answer: per-resolution covers full COGS (telephony, integration, training, ops); no vendor discloses the inference fraction. Anthropic and OpenAI exposing per-trajectory billing (Apr 2026) sharpens the objection — buyers can estimate inference independently. Back-of-envelope at Sierra scale: 47-call trace × $0.012 average Claude Sonnet blend ≈ $0.55 inference per resolved conversation vs. ~$2.50 charged (~22%).

**Pattern 2 — "What if the agent fails and you bill me anyway?"** Most acute in per-usage. Buyers want "no-charge for unresolved"; vendors resist (unresolved still burns inference). Sierra's resolution definition is the negotiated answer; hybrids add "<X% failure rate or refund overage" SLA. Cresta and Decagon contracts now include named-failure-mode credits (Cresta deck, RevOps Leaders forum Mar 2026: 3% credit-back if AI-handled rate falls below floor for two consecutive months).

**Pattern 3 — "How do we forecast spend?"** The objection that converts pure-outcome to hybrid. CFOs cannot defend a line item floating ±40% QoQ; FP&A builds budgets on T-12 and needs a fixed anchor. Sierra has lost (and Decagon won) at least two F500 retail logos late 2025 on this objection (Procurement Leaders AI Summit panel, Apr 2026, off-record). Hybrid survives because it gives the CFO a fixed forecast and the CRO an outcome story.

**Pattern 4 — "Outcome-definition arbitrage."** Vendor controls definition; buyer controls dispute. Sierra's 7-day no-return-contact window is contested by regulated buyers — a "resolved" conversation triggering a complaint at day 14 is not resolved. Q1 2026 emerging contract solution: **dual-telemetry** — vendor measurement is billing source of truth, buyer-side telemetry is audit override, disputes settled via third-party arbitration (Iron Mountain, Big Four advisory). Pure Bet #1 procurement-playbook gap.

---

## 3. Contract Term Negotiation Reality — May 2026

AI-specific terms now standard in F500 SaaS negotiations:

- **Training rights on customer data — near-universal.** No-training-by-default at OpenAI Enterprise, Anthropic Enterprise/Workspace, Glean/Sierra/Harvey enterprise SKUs. Buyers still negotiate explicit zero-retention windows (0–30 days) and audit logs.
- **Output ownership — Bartz-driven.** The Bartz v. Anthropic preliminary injunction (Apr 2026, N.D. Cal.) cited output-ownership ambiguity in enterprise contracts. Buyers now demand explicit output assignment to buyer entity + vendor indemnity against third-party IP claims. Anthropic and OpenAI Enterprise both updated MSAs Q1 2026.
- **Model-update notice — silent-update fallout.** OpenAI's Mar 2025 GPT-4 → GPT-4-turbo silent swap (downstream prompt-tuning regressions for a subset of customers) made version-pinning a procurement demand. Q1 2026 standard: 60–90 day notice for major updates; pin-to-prior-version for 12 months; vendor migration-testing support.
- **Hallucination indemnity — Air Canada precedent extended.** Moffatt v. Air Canada (2024, BC Civil Resolution Tribunal) — airline bound by chatbot statements — is the cited precedent. F500 buyers demand vendor indemnity for AI-misstatement damages, cap typically 12-month fees, exclusions for misuse. Sierra, Decagon, Cresta carry $5M+ aggregate liability terms in F500 master agreements.
- **Agent-action liability — the new frontier.** Who owns when the agent takes an irreversible action (refund, email, ticket, calendar invite)? Standard 2026 term: per-action authorization tier (read-only / write-with-confirmation / autonomous), vendor liability only for autonomous-tier failures violating documented behavior. EU AI Act Article 14 enforcement (late 2026) will harden this — autonomous-tier on high-risk categories requires human-oversight clauses.
- **Per-trajectory cost transparency — emerging.** Anthropic Claude Agent SDK 2.0 (Apr 2026) and OpenAI Responses API expose trajectory cost in billing consoles. Q1 2026 F500 buyers begin demanding vendor-side trajectory cost disclosure as a contract term — "show me what one resolved conversation cost in inference, telephony, and human-review tokens." Sierra has resisted; Decagon has partially complied on Tier-1 deals.

---

## 4. Forecast — Where Compression, Where Premium Holds

**Compression coming:**
- **SDR-AI:** 11x flat at ~$20M ARR through 2024–Q1 2026 is the saturation signal. Per-seat AI SDR at $4–8K/seat commodifies first — buyers can benchmark output against Clay enrichment + outsourced SDR pods at $80–150/meeting.
- **Generic copywriting:** Jasper (~$95M ARR), Writer ($100M+), Copy.ai pivoting to "marketing workflow agents" — pure-content pricing collapsed.
- **Low-stakes chat:** Tier-2 CX (FAQ deflection) absorbed by ChatGPT Business connectors + Claude for Work; pure-play floor at $0.50/conversation and falling.

**Premium holding:**
- **Healthcare CX:** Hippocratic $9/hr RN-equivalent — regulatory moat + nursing-cost replacement math.
- **Legal:** Harvey $200–500/seat enterprise (Goldman deal leak Apr 2025) — privilege + accuracy + UPL liability.
- **Financial services / regulated:** Rogo $250–500/seat (Goldman, JPM); Hebbia $150–300/seat; Glean Finance vertical — data-residency + audit-trail requirements deter foundation-lab encroachment.

**The per-trajectory FinOps advisory window (Bet #4 reframe).** Per-token compresses 3–5× through 2027; per-trajectory expands as agents fan out 20–80 tool calls. Net advisory window 12–18 months, possibly 24, before AWS Bedrock auto-optimization (Risk #4) bundles it into runtime. Arbitrage: enterprises pay full Opus-tier on every step of a 47-call trajectory when 80% of steps should run cheaper-tier. Planner-executor diagnostic saves $50–250K/year per $1M AI spend.

**The "outcome-based pricing for non-CX" question.** Sierra's model exports cleanly to Hippocratic (per-hour-of-care has measurement clarity), partially to Glean (per-query measurable but value-per-query buyer-specific). Fails at Harvey (legal outcomes case-specific, multi-year, unmeasurable per-event), Rogo/Hebbia (banker outcomes confound vendor attribution), Cursor (developer productivity is per-seat-stable, user is buyer). **Rule of thumb: outcome pricing works where the trajectory is discrete, completable in one session, with a buyer-visible success signal. CX has all three. Legal, finance, and developer tools have zero, one, or two.**

---

## 5. What Enterprise Buyers Actually Pay — May 2026 ACV / Contract-Size Data Table

| Company | Pricing Unit | Typical ACV | Source |
|---|---|---|---|
| **Sierra** | $1–4 / resolved conversation | $500K–5M F500; ~$2.5M median | Sierra deck, Twilio CX roundtable Mar 2026 |
| **Decagon** | Per-conversation + platform min | $250K–1M minimum + variable; ~$500K mid-market | The Information AT&T leak Feb 2026 |
| **Glean** | Per-seat | $40–50/user; floor $35 at 5K+ seats | Reddit r/sales leak Q4 2025 |
| **Harvey** | Per-seat | $200–500/user; Goldman/PwC $5–15M ACV | Bloomberg Apr 2025; $300M raise Mar 2026 |
| **Hippocratic AI** | $9/hour RN-equivalent | $1–5M ACV health-system pilots | STAT News deck leak Jan 2026 |
| **Cursor / Anysphere** | Per-seat | $20 individual / $40 enterprise; $100M+ ARR Q1'26 | TechCrunch enterprise launch Nov 2025 |
| **Cresta** | Per-seat + per-conversation hybrid | $150–250/agent + $0.50–1.50/call | Greylock $100M+ ARR Mar 2026 |
| **Abridge** | Per-encounter | $3–8/encounter; $10–30M ACV at IDN scale | Becker's Feb 2026 UPMC renewal |
| **Clay** | Per-credit usage-based | $50K–500K mid-market; $110M ARR Q1'26 | Clay blog Q1 2026 milestone |
| **Rogo** | Per-seat | $250–500/seat; $5–20M ACV bulge brackets | TechCrunch $400M raise Jan 2026 |
| **Hebbia** | Per-seat | $150–300/seat; $50M+ ARR | The Information raise-overdue Mar 2026 |
| **Salesforce Agentforce** | $2/conversation list + negotiated minimums | Bundled with Sales Cloud Enterprise | Salesforce Q4 FY26 call; Feb 2026 repricing |

---

## 6. The Hyperscaler Margin-Squeeze Angle

As AWS Bedrock auto-optimization ships (Bedrock Automated Reasoning GA Dec 2024; auto-routing across model tiers plausibly bundled Q4 2026 per OCQ C8), three margin layers reprice:

- **Inference compression hits pure-play gross margin.** Sierra, Decagon, Cresta absorb token cost as fixed-COGS in per-resolution pricing. Bedrock auto-optimization cutting inference 30–50% at scale expands Sierra gross margin — *unless* buyers demand pass-through (per-trajectory cost transparency clause, §3). The pricing-power test arrives 2026–2027: do vendors retain optimization gains, or does buyer-side audit force pass-through?
- **Hyperscaler bundle absorption attacks the audit middleman.** Bedrock Guardrails + Microsoft Purview + Bedrock auto-routing bundle FinOps / guardrail / routing audit into runtime free — the way AWS attacked Datadog's monitoring market. Bet #4's advisory window is bounded by this.
- **Where gross margins hold:** Regulated verticals (Hippocratic, Harvey, Rogo, Hebbia) where hyperscaler bundles cannot ship the compliance moat. Cursor / Anysphere where per-seat developer pricing is stable. Glean where moat is connectors + tenancy isolation.

**Net read:** Pure-play CX gross margin compresses 2026–2028 unless vendors hold pricing-power against pass-through demands. Vertical-regulated holds through 2028. Per-seat developer tools hold. SDR-AI compresses fast.

---

## 7. Top 3 Implications for Alex's Bet #1 Advisory Practice — Procurement Playbook (Pricing-Side)

**Implication 1 — Productize the "outcome-definition contract template" as the highest-leverage Bet #1 deliverable.** No vendor turnkey-answers the measurement-and-dispute problem; no buyer has internal playbooks. Deliverable: procurement-side outcome-pricing template with dual-telemetry, 30/60/90 dispute windows, third-party arbitration, per-trajectory cost transparency riders. Sits dead-center in Bet #1's CISO/CFO/CIO ICP; compounds with the form-factor procurement audit (O7, 100/125).

**Implication 2 — Bundle a per-trajectory FinOps audit into every Bet #1 engagement.** Anthropic and OpenAI exposing per-trajectory billing (Apr 2026) gives the audit empirical teeth. Math: at $1M+ AI spend, planner-executor reroutes save 30–60% on multi-hop trajectories. The audit is the wedge to broader playbook adoption. Window: 12–18 months before Bedrock auto-routing bundles. Score equivalent: O10 (80/125) extended into pricing.

**Implication 3 — Move the playbook upstream: pricing-model selection, not just vendor selection.** F500 buyers enter negotiations without a thesis on per-seat vs. hybrid vs. outcome — they negotiate price-per-unit but not unit-of-pricing. The decision tree (use-case → unit → contract template → measurement architecture) is upstream of every vendor deal and is unowned. This converts Bet #1 from vendor-due-diligence practice to pricing-strategy practice — a 3–5× ACV uplift in deliverable scope.

*End F6. Cross-link: feeds the procurement-playbook pricing module of Bet #1 in `OCQ_TRACKER.md` next monthly update; data table feeds Wave 2 ACV benchmarking.*
