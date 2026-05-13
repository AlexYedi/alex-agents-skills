# The AI Vendor Procurement Playbook

**How the Fortune 1000 Should Buy AI Agents in 2026**

*Author: Alex Yedi*
*Date: May 2026*
*Edition: v1.0*

*Part C — Decision Tree, Rubric, Glossary, Appendix, Closing*

---

## Section V · The Decision Tree (Buy, Build, Wait, or Walk)

This section is the procurement officer's decision aid. It is intentionally agent-specific. Generic SaaS decision trees do not produce the right answers because agent procurement asks questions SaaS procurement does not — autonomy scope, action reversibility, model deprecation, sub-agent privilege, EU AI Act Article 14 tie-out, per-trajectory cost variance, and outcome-pricing dispute mechanics. Use this tree at the start of every agent-procurement cycle. Do not use it as a substitute for the seven overlays in Section III; use it as the framing that determines which overlays bite hardest, which counterparties from Section II hold the load-bearing veto, and which addenda from Section IV must be in the redline before pen touches paper.

The tree has eight branches. The first seven establish whether you should buy at all and on what terms. The eighth — Pricing-Model Selection — is the branch most procurement teams skip and most regret skipping. Run them in order. If a branch closes the deal, stop; do not advance to the next branch hoping a later question will rescue an answer the earlier one already gave you.

### Branch 1 — Is the workload regulated?

If the workload is regulated under HIPAA, GLBA, FERPA, FINRA, NYDFS Part 500, SR 11-7, FedRAMP, CMMC, ITAR, GDPR's special-category data, California CCPA/CPRA sensitive-data provisions, or the sectoral overlays in Chapter III.7, the answer is not "buy faster" or "build instead." The answer is: only consider vendors who ship the sectoral overlay packet from Chapter III.7 *before* you start the pilot. Roughly four out of five horizontal vendors will not pass this screen. That is correct behavior. The screen exists to keep them out.

For financial services, add the eighth counterparty — the model-risk function reporting to the Chief Risk Officer — to your gauntlet. SR 11-7 model validation is not a CISO sign-off and not an AI Council sign-off; it is its own queue with its own evidence requirements and an additional eight-to-sixteen weeks of cycle time. Vendors who do not arrive with an SR 11-7 mapping have not done the work and will not finish the work inside your fiscal quarter.

If the workload is unregulated, proceed to Branch 2.

### Branch 2 — Is the data shareable with a foundation-model provider?

If the data flowing through the agent — prompts, context windows, persistent memory, tool returns — contains material non-public information (MNPI), pre-IPO financials, attorney-client-privileged material, customer PII, employee compensation data, or anything else that would create exposure if it reached a foundation-model provider's training set, then the procurement question collapses to: which deployment posture does the vendor support? You need one of: a no-training-rights commitment with audit, a private deployment (VPC, dedicated tenancy, customer-managed keys), or a sovereign-cloud option (AWS GovCloud, Azure Government, GCP Sovereign, or a regional EU option such as OVHcloud or Scaleway). Do not accept "we don't train on your data" without the contract language and the audit hook. The Bartz settlement framework is the reason — training-rights ambiguity is not a small contract issue any more.

The sub-processor question is downstream of the deployment question. Ask which foundation-model provider sits behind the agent today, which one will sit behind it in twelve months, and what the change-notice mechanism is when the vendor swaps providers. The answer "we abstract the model away from you" is a vendor's optimization at your DPA's expense — it converts a sub-processor change you have a contractual right to object to into a routine engineering decision you never see.

If the data is shareable (public information, synthetic test data, or data the buyer is comfortable having ingested), proceed to Branch 3.

### Branch 3 — Is the agent taking irreversible actions?

If the agent's action surface includes any of: sending external email, posting to a customer-facing channel, charging a card, executing a financial transaction, modifying a system of record without versioning, deleting data, granting access, generating regulatory filings, or interacting with any third party on the buyer's behalf — then the procurement defaults change. You need: a written action-rollback document per write tool (Chapter III.3); a human-in-the-loop gate on every irreversible action; a kill-switch the buyer holds; and contractual language that makes the vendor co-liable when an irreversible action goes wrong outside the human gate. Pilot scope must not include irreversible actions in the first 30 days. Production deployment must not include irreversible actions in the first 90 days. This is conservative on paper. It is the right posture given current vendor-side maturity.

The per-action authorization tier (read-only / write-with-confirmation / autonomous) belongs in the order form, not in a kickoff email. Vendor liability should attach only to autonomous-tier failures violating documented behavior — and the documented behavior is the tool-boundary policy from Chapter III.1, not a marketing slide.

If the agent's action surface is read-only or reversible-only, proceed to Branch 4.

### Branch 4 — What is your fallback if the model is deprecated?

The single most-undertaught lesson of 2024–2026 is that frontier-model deprecation is now a procurement event. GPT-3.5 was deprecated mid-2024. Claude 1 and 2 deprecated by end of 2024. Multiple Claude 3 family endpoints retired through 2025. Gemini 1.5 family rotated through 2025. The OpenAI March 2025 GPT-4-to-GPT-4-Turbo silent swap caused a quiet wave of downstream prompt-tuning regressions for a subset of customers who had no notice and no pinning right. The model your vendor pinned in their last eval report may not exist in twelve months. Ask: what is the model-pin-change notice? What is the re-eval procedure? What is the buyer's right to refuse a model swap that materially changes agent behavior? What is the deprecation indemnity?

If the vendor's answer is "we automatically upgrade you to the latest model," reject. That is not a fallback. That is a vendor's optimization at the buyer's risk. The right answer is a 60-to-90-day model-pin-change notice, a re-eval requirement before swap, a contractual right to refuse with prorated refund, and a pin-to-prior-version right of at least twelve months for any deployment that has cleared an AI Council gate against a specific model identifier.

If the vendor passes Branch 4, proceed to Branch 5.

### Branch 5 — Build, buy, or partner?

This is the branch where most procurement teams get the wrong answer.

You should *buy* when: (a) the workflow is generic enough that a vertical-agent vendor has solved it for the median buyer at a scale you cannot match; (b) the vendor's eval evidence is at parity with or better than what your internal team can produce; (c) the integration surface is bounded by a small number of MCP servers or first-party connectors; (d) the regulatory posture is a vendor contractual commitment, not your problem to construct.

You should *build* when: (a) the workflow is core to your differentiation and the agent's behavior encodes your proprietary judgment (the underwriting policy, the pricing model, the customer-segmentation logic); (b) the data flow is too sensitive to share with a third party even under no-training-rights commitments; (c) the orchestration touches more than five proprietary internal systems; (d) you have the engineering capacity to maintain it through at least two foundation-model rotations.

You should *partner* — the underestimated third option — when: (a) a vertical-agent vendor has 80% of what you need and you can co-build the 20% on their platform with shared IP terms; (b) you can negotiate operator-shaped terms (per-trajectory pricing, customer-owned eval data, exit clause for the proprietary 20%); (c) the partnership is structured as a 12-month pilot with explicit exit rights, not a five-year platform commitment. Most F1000 buyers should be partnering more and building less. The partner path is where vendors most willingly grant the AI-specific addenda from Section IV — they need the logo, you need the leverage, and the leverage closes the moment money has fully moved.

If the answer is buy or partner, proceed to Branch 6. If the answer is build, this Playbook still applies to the model-provider, eval-platform, and gateway vendors you will procure into the build — read Sections III.1, III.2, III.5 with that lens.

### Branch 6 — Buy now or wait six months?

This is the branch that the 2026 calendar makes urgent and that most procurement teams answer wrong by default.

Buy now if: (a) the EU AI Act Article 14 implementation timeline aligns with your enforcement calendar (Q4 2026 onward for EU operations); (b) the vendor's pricing reflects Q2 2026 market and you expect a Q3 2026 ARR-resolution-driven re-price upward; (c) the integration window in your IT roadmap is open now and not in twelve months; (d) the workflow's dollar impact justifies non-optimized deployment.

Wait six months if: (a) AWS Bedrock auto-routing of planner-executor splits is expected by H2 2027 and you can fold per-trajectory cost optimization into the buy decision later; (b) Anthropic ARR resolves in Q3 2026 with a downside print ($24B rather than $30B) and you expect vertical-agent valuations to compress 20–30%, which will produce better contract terms; (c) the vendor's eval evidence is below the threshold from Chapter III.5 and you would be buying on a roadmap commitment rather than a signed report; (d) the regulatory posture is genuinely unsettled and the vendor's tie-out is conceptual rather than control-by-control.

The asymmetry here is heavy. Waiting costs you six months of value; buying wrong costs you a vendor-replacement project that will run twelve to eighteen months and a sunk-cost fight with the sponsor who championed the wrong vendor. The right default in May 2026 is: buy now if and only if the vendor passes Branches 1–5 with documented evidence; otherwise pilot under the Branch 7 rules and reserve the production decision for the post-Q3-2026 market.

### Branch 7 — Pilot scope and exit-cost analysis

If you have answered the prior six branches and the answer is "pilot," structure the pilot so it does not trap you. Three rules.

*Rule one — pilot scope.* The 90-day pilot must touch fewer than three systems, must include zero irreversible actions in the first 30 days, must produce a signed reproducible eval report by day 60, and must conclude with a binary go/no-go gate by day 90 against criteria you wrote on day zero. Vendors will press for longer pilots and broader scope. Resist. A pilot that does not have an exit gate is not a pilot; it is a soft commitment the vendor will harden over your CFO's signature at renewal.

*Rule two — data portability and deletion exit terms.* The pilot contract must include exit terms with explicit data-portability obligations: any persistent memory the agent has accumulated about your business is yours, must be exportable in a documented format within 30 days of pilot termination, and must be deletable from vendor systems with a deletion confirmation log. Without these terms, you have not run a pilot. You have made an undisclosed long-term commitment, and the persistent memory the agent has accumulated about your customers, your accounts, and your internal processes is now hostage to a renewal negotiation.

*Rule three — production pricing pre-quoted.* The pilot pricing must not anchor production pricing. Vendors price pilots aggressively (free, $25–50K) and then anchor production pricing against a fully-loaded base that includes counterfactuals the pilot never tested. Insist that production pricing be quoted at the start of the pilot, with a defensible per-trajectory or per-resolution unit-economics breakdown, and with a written right-to-renegotiate at the production-transition gate. The pricing-model selection question (Branch 8) is the input to this rule, not the output.

The 90-day pilot, the seven overlays, the AI-specific MSA addenda from Section IV that bind on day one, and the production-pricing pre-quote together are the procurement equivalent of a forward-deployable arming switch. They let you commit conditionally while keeping the option to walk. Anything looser is a long-term commitment the vendor will eventually exercise against you.

### Branch 8 — Pricing-Model Selection

Most procurement teams negotiate price-per-unit but not unit-of-pricing. That is the wrong order. The unit determines the dispute mechanics, the forecast volatility, the gross-margin behavior under usage spikes, and whether your CFO can defend the line item to the audit committee. Pick the unit before you negotiate the rate.

Four pricing models are live in May 2026: per-seat, per-message (or per-API-call), outcome-based (per-resolution, per-encounter, per-hour-of-care), and hybrid (fixed platform fee plus variable). Each fits a specific workload shape. Mismatched fit is the single most common reason a buyer ends a year inside an agent contract that looked good at signing and is now a fight at renewal.

*Per-seat is right when:* the agent augments a named human whose work product is the audit trail (AE, CSM, analyst, attorney, line manager). Glean per-seat at $40–50/user holds because the buyer is IT and the seat count is the procurement vocabulary. Harvey at $200–500/seat holds because the privilege-and-accuracy buyer is the law-firm partner. Cursor at $40 enterprise holds because the user is the buyer. Per-seat fails the moment the agent does end-to-end work without a human cosignatory — 11x's flat ARR through 2024–Q1 2026 is the canonical SDR-AI saturation signal that per-seat AI SDR at $4–8K/seat hits a wall when buyers benchmark against per-meeting outsourced pods at $80–150/meeting.

*Per-message or per-API-call is right when:* the agent is a developer or platform surface where the trajectory boundary is technical and the buyer is an engineering team that already thinks in API units. Cursor's $0.04 premium-model overage is acceptable because the developer absorbs the forecasting cognitive load. Per-message becomes hostile to F1000 procurement the moment the buyer is a CFO who needs to defend a line item — pure variable pricing without a floor cannot be modeled in an annual budget.

*Outcome-based is right when:* the trajectory is *discrete, completable in one session, and produces a buyer-visible success signal*. This is the test. Sierra's per-resolved-conversation pricing at $1–4 works because CX has all three properties: a conversation is bounded, it closes in one session, and the CSAT signal is observable. Hippocratic's $9/hour RN-equivalent voice agent works because the work-time unit has measurement clarity. Abridge's $3–8 per encounter works because the encounter is the natural clinical unit. Outcome pricing fails outside this triad — Harvey, Rogo, and Hebbia explicitly refuse it because legal and finance outcomes are case-specific, multi-session, and confounded by attribution. Cursor refuses it because developer productivity is per-seat-stable. The rule of thumb: **outcome pricing exports cleanly to workloads where the trajectory is discrete + completable + buyer-visible. CX has all three. Legal, finance, and developer tools have zero, one, or two. Do not let a vendor sell you outcome pricing for a workload that fails the triad — you will spend the contract year arguing definitions.**

*Hybrid is right when:* the workload sits in the middle (variable usage with a stable platform component) and your CFO requires a fixed forecast anchor. Cresta at $150–250/agent platform plus $0.50–1.50 per AI-handled call is the dominant CX hybrid. Decagon's $250–500K platform minimum plus per-conversation overage is the dominant mid-market hybrid. Hybrid wins the 2026 contract count even as outcome wins the headline narrative, because procurement infrastructure (annual budgets, SAP/Coupa workflows) is built for fixed-plus-variable, not pure variable.

The buyer's reality check on per-resolution pricing is the **token-markup math**. At Sierra scale, a 47-call trace at roughly $0.012 average Claude Sonnet blend per call is approximately $0.55 of inference cost per resolved conversation against $2.50 charged — about 22%. The other 78% covers telephony, integration, training, ops, and gross margin. That is not unreasonable, but it is the number you should hold in your head when a vendor tells you per-resolution pricing reflects their cost structure. The Anthropic Claude Agent SDK 2.0 (April 2026) and OpenAI Responses API trace-cost views let you estimate inference fraction independently. Use them. The per-trajectory cost transparency clause from Section IV is how you make this estimation a contractual right rather than a back-of-envelope.

The discipline in Branch 8 is that the unit-of-pricing decision is upstream of the per-unit-rate decision. A buyer who walks into a Sierra negotiation having already decided the unit is "per-resolved-conversation" has already lost the conversation about whether outcome pricing fits their workload. A buyer who walks in with the discrete-completable-buyer-visible test in hand can negotiate the unit first, and the rate second, and arrive at a contract that survives the audit committee, the CFO's quarterly forecast review, and the renewal cycle. That is the position this Playbook takes, and the position your procurement team should take into every agent vendor conversation in 2026.

---

## Section VI · The Vendor Scoring Rubric (Procurement Operating Standard 1.0)

The Rubric is the named matrix this Playbook publishes. It does one thing and does it deliberately: it translates the seven counterparties of Section II and the seven overlays of Section III (plus the per-trajectory FinOps overlay implied by Section V Branch 8) into a single 7 × 8 scoring grid that any two readers can apply to the same vendor and arrive at the same buy / conditional / no-buy decision. That replicability is the test. If two competent procurement teams score the same vendor differently using this Rubric, the Rubric has failed and I want to know about it.

Use it three times in the lifecycle of every agent vendor relationship. **During evaluation** — score the vendor before you sign the pilot, with whatever evidence the vendor will provide under NDA, and use the gaps to write the pilot evidence-acceptance criteria. **During procurement** — score the vendor again at the production-transition gate, with the pilot evidence pack in hand, and use the score to inform Branch 6 (buy now vs. wait). **During renewal** — score the vendor a third time before each renewal, against the most recent eval, red-team, and Article 14 tie-out artifacts the vendor has supplied, and use the score to anchor the renegotiation. A vendor whose Rubric score has degraded materially across two cycles is a vendor whose architecture has drifted away from your requirements; renew on shorter terms or exit.

### The Rubric Matrix

Each cell is scored **Pass / Conditional / Fail** with a one-line evidence requirement. The seven counterparties are rows; the eight overlay categories are columns. The eighth column is Per-Trajectory FinOps — the cost-telemetry and trajectory-cost-transparency overlay surfaced by Section V Branch 8 and by the Enterprise Architecture chapter in Section II.

| Counterparty ↓ / Overlay → | Tool-Boundary Policy | Indirect-Injection Red-Team | Action-Rollback | Sub-Agent Privilege | Signed Eval Reports | Article 14 Tie-Out | Sectoral Overlays | Per-Trajectory FinOps |
|---|---|---|---|---|---|---|---|---|
| **InfoSec** | Document supplied; ≥4 privilege tiers | Adaptive-adversary report <90 days, named methodology | Per-write-tool RTO + irreversible-action list | Diagram + runtime enforcement + escalation tests | Model pin + harness + reproducible by buyer ±5pts | N/A (cross-ref AI Council) | Pen-test current + sectoral attestations | Per-trajectory log to buyer SIEM |
| **Legal** | Tool-boundary breach defined as material breach in MSA | Red-team disclosure clause + 48-hr injection-class notification | Action-rollback SLA + irreversible-action indemnity | Sub-agent privilege change = 30-day notice in MSA | Eval-evidence warranty + 5-pt reproduction = breach trigger | Article 14 tie-out warranted in MSA | BAA / SR 11-7 / FedRAMP exhibit | Per-trajectory cost transparency clause |
| **Privacy** | Tool inventory mapped to data categories | N/A (cross-ref InfoSec) | Persistent-memory deletion path on rollback | Sub-agent memory-write scope documented | Eval datasets do not contain customer PII | Article 14 + GDPR Art. 22 dual map | DPA + sectoral data-flow diagram | Trajectory logs Schrems-II posture documented |
| **AI Governance** | Policy reviewed by AI Council; matches Use Policy | Adaptive red-team in NIST AI RMF mapping | Rollback in AI incident-response runbook | Privilege matrix mapped to ISO 42001 controls | Signed report + dataset hash + reproducibility = required artifact | Article 14 tie-out is the load-bearing artifact | Sectoral risk-tier classification | Trajectory cost as governance metric (drift signal) |
| **Procurement** | Policy enables vendor benchmarking | Red-team partner named + cost in TCO | Rollback SLA + service credits priced | Sub-agent count + cost-fan-out modeled in TCO | Eval-report cadence in order form | Tie-out refresh cadence in order form | Sectoral overlay packet included pre-pilot | Per-trajectory ceiling + per-tenant budget caps |
| **Sponsor** | Operator can read it without legal translation | Demonstrable in vendor's customer war-stories | Rollback never requires sponsor sign-off in business-hours | Sub-agent fan-out invisible to operator UX | Eval results align with sponsor's business KPIs | Tie-out includes operator-training materials | Sectoral artifacts do not slow time-to-value | Cost dashboard available to operator |
| **Enterprise Architecture** | Tools listed match identity-fabric scopes (OAuth blast radius bounded) | Defense integrates with EA's gateway and SIEM | Rollback hooks integrate with buyer's incident automation | Sub-agent enforcement uses EA's identity primitives | Reproducibility runs in buyer's eval environment | Tie-out evidence flows through buyer's audit pipeline | Sectoral isolation conformant to reference architecture | OpenTelemetry GenAI-conventions-native trajectory metering |

A cell scores **Pass** when the vendor supplies the named artifact and a named representative will defend it. **Conditional** when the artifact exists but is incomplete, stale (>180 days for eval / >12 months for tie-out), or available only under post-signature NDA. **Fail** when the artifact does not exist or the vendor refuses to disclose. The sub-rule that prevents creative grading: any cell scored Pass must reference an artifact you can attach to the procurement file. If you cannot attach it, the cell is at best Conditional.



### The (Function, Capability) Vendor-Coverage Map

The Rubric scores the vendor's posture. The Coverage Map scores the vendor's product. Use the (Function, Capability) cell coordinate system from the Volume III substrate to ask: which cells does this vendor credibly serve? For an F1000 buyer, five coordinates carry disproportionate weight in any agent-procurement decision, and each maps to a load-bearing question this Playbook takes a position on:

- **(9, G) — Procurement seam compliance.** Does the vendor pass the gauntlet — all seven counterparties, all seven overlays, the fourteen addenda? This is the cell of record. As of May 2026, no incumbent ships a turnkey bilateral evidence pack for this cell. The vendor that earns a Pass in column G against (9, G) is a vendor you can deploy without a six-month controls retrofit.
- **(4, M) / (6, M) / (9, M) / (10, M) — Trajectory observability.** Does the vendor ship audit-grade trajectory artifacts to the buyer's SIEM and observability pipeline? The M-column is regulatorily mandatory inside eighteen months under TCPA, CAN-SPAM, GDPR, SOX-applied-to-agent-actions, and EU AI Act Article 14 evidence requirements. A vendor weak on M will be replaceable by Q4 2027 — do not sign multi-year on M-failures.
- **(6, L) / (11, L) — Persistent memory durable across cycles.** Does the vendor's memory layer survive multi-quarter deal cycles, multi-year renewal motions, and GDPR right-to-be-forgotten requests with surgical-deletion semantics? The L-column is the matrix's most consistent gap. A Conditional here is acceptable in May 2026; a Fail is a procurement risk.
- **(11, I) — Outcome-pricing maturity.** If the vendor offers outcome pricing, does the contract include the dual-telemetry, the dispute window, the third-party-arbitration clause, and the per-trajectory cost transparency rider? A Sierra-style outcome contract without these is a contract you will renegotiate inside two quarters.
- **(5, F) — Buying-committee mapping.** If the vendor ships toward this cell (Common Room, Sales Nav, Clay, ZoomInfo, 6sense), does its committee-graph artifact have signed provenance, weekly refresh, and exportable-on-exit semantics? This is an OCQ 18/20 cell with no incumbent owner; vendors are claiming it without earning it.

### Rolling the Score Up to a Decision

The Rubric is a 56-cell matrix. Aggregate as follows. **Buy** when no Fail anywhere in the InfoSec / Legal / AI Governance / Enterprise Architecture rows, no more than two Conditionals across those four rows, and Pass on every overlay column for whichever sectoral and pricing-model branches were triggered in Section V. **Conditional buy** (proceed to pilot under Branch 7 rules; production-transition gate becomes a hard gate) when the failure surface is bounded — fewer than four Fails total, none in InfoSec or Legal, and a vendor commitment to remediate the named Conditionals inside the pilot window with Procurement holding the timeline. **No buy** when there is any Fail in InfoSec or Legal, when the Article 14 tie-out is missing for an EU-exposed deployment, or when the sectoral overlay packet is missing for a regulated workload. The aggregation rule is intentionally conservative because the cost of a wrong-buy in this category is a twelve-to-eighteen-month replacement project, and the cost of a wrong-walk is six months of waiting for the vendor to ship the artifacts you need. Asymmetric downside justifies asymmetric defaults.

---

## Section VII · Glossary of Agent-Specific Terms

The terms a F1000 buyer needs in order to read a vendor's SOC 2-plus-AI-addendum the same way they read a SOC 2 today. Operational definitions, not academic ones. Sorted alphabetically.

**Action rollback.** Per-write-tool procedure for restoring a system of record after the agent has written the wrong value. Distinct from "logging," which is necessary but insufficient. See Chapter III.3.

**Adaptive adversary.** A red-team methodology in which the test set is regenerated against the live defense, producing honest success rates as the defense improves. The honest counterpart to static red-team scores. Critical for indirect-injection defense disclosure.

**Adverse selection in per-message pricing.** The buyer's risk that vendors absorb easy conversations under per-message pricing (where margin is high) and ration the hard ones (where margin is low or negative). The mirror-image of the vendor's risk that buyers route only the hardest conversations to the agent. Both produce contract disputes inside two quarters absent a dual-telemetry mechanism.

**Agent-action liability.** Distinct from hallucination indemnity. Allocates liability when the agent's *action* — not its *output* — causes harm (a wrong payment, an unauthorized scope grant, a deleted record). New as a category; treat it as a board-level concern.

**ASL-3 / Responsible Scaling Policy.** Anthropic's classification of model risk levels and the corresponding deployment commitments. Adjacent to OpenAI's Preparedness Framework. Procurement question: what does the vendor's deployment posture commit to when the underlying model crosses a safety threshold mid-contract?

**Bilateral evidence-pack interchange format.** The shared schema by which a vendor's eval, red-team, tool-boundary, sub-agent privilege, and Article 14 tie-out artifacts are exchanged with the buyer's procurement file in a form portable across vendors. Does not yet exist as a standard. The first credible publisher sets the procurement default for the next five years. The Bet #1 wedge.

**Computer-use.** Class of agent capability in which the agent operates a SaaS application by reading the screen and emulating keyboard / mouse input rather than calling an API. OSWorld benchmark scores sit in the mid-50s as of Q2 2026, well below the human 72%. Not yet production-grade for unattended SaaS-UI tasks; do not buy on the demo.

**Conformity assessment.** EU AI Act process by which high-risk AI systems demonstrate compliance with the Act's requirements before being placed on the EU market. The vendor-side tie-out (Chapter III.6) is the input; the buyer-side conformity assessment is the output. Both required.

**Conversation-resolution metric.** Outcome-based metric, popularized by Sierra, that prices CX-agent value by resolved conversations rather than per-seat. Not yet a procurement standard outside CX. Watch the legal-and-finance-vertical refusal pattern in 2026 as the test of exportability.

**Dual-telemetry.** The contract mechanism in outcome-pricing deployments where the vendor's telemetry is the billing source of truth and the buyer's parallel telemetry is the audit override, with disputes resolved via third-party arbitration. The unsolved measurement-and-dispute problem of outcome-based pricing absent this mechanism.

**Escalation handoff.** The Conclude-phase artifact when an agent hands a task to a human. Quality of handoff (full context, no re-asking, ticket linked, decision-record attached) is the single most-correlated variable with CSAT in CX-agent deployments and with controller acceptance in back-office deployments.

**Eval freshness.** The age of the vendor's signed eval report relative to the current model pin and system prompt. Anything older than 180 days is stale; anything older than the most recent model swap is invalid.

**Form-factor.** The user-facing surface the agent inhabits (Slack thread, browser extension, voice channel, computer-use overlay, dedicated SaaS UI). Procurement-relevant because form factor determines DLP inheritance, threat surface, and approval pattern.

**Hallucination indemnity.** Contractual provision allocating liability for harms caused by the agent's incorrect or fabricated output. Air Canada (February 2024) crystallized the rule that the deploying party holds the bag absent specific contract language. Insert the indemnity.

**HITRUST CSF.** Common Security Framework adopted by US healthcare; CSF v11.x is the current major version. The de facto procurement bar for healthcare AI agents; level r2 with HITRUST certification is the strongest posture.

**Indirect prompt injection.** A class of attack where content the agent reads from a tool, document, or external source contains instructions the agent treats as if they came from the operator. The unsolved problem of the agent layer; adaptive-adversary defense rates sit at 60–80% honestly disclosed.

**ISO 42001.** The 2023 international standard for AI management systems. Adopted by Drata, Vanta, and Secureframe as a readiness mapping; not yet a regulator-mandated bar in most jurisdictions but the cleanest single-attestation vendor posture as of 2026.

**Kill-switch.** Buyer-side mechanism to disable a tool, a sub-agent, or the entire agent without engineering intervention. Must be in the buyer's hands, not behind a support ticket. Should be tested quarterly.

**MCP (Model Context Protocol).** Anthropic-originated open protocol for connecting LLMs to tools, data sources, and third-party services. Graduated to Linux Foundation governance December 2025. As of Q2 2026 the de facto interoperability spec, with experience-layer fragmentation across implementations.

**MCP gateway.** Control plane sitting between the agent and the MCP servers, handling auth, audit, rate-limiting, secret-injection, and policy enforcement. Cloudflare, Kong, and Pomerium are the durable incumbents.

**MCP server.** A process exposing tools to an MCP-compatible client. May be first-party (vendor-supplied) or third-party. Quality varies widely; first-party servers from Stripe, Linear, GitHub, Snowflake, and Databricks are the current quality benchmark.

**Model pin.** The specific model identifier (e.g., `claude-opus-4-7-20260301`) the vendor has tested the agent against. Every eval report and every contract clause should reference a model pin. Model swaps without re-eval are a procurement event.

**Model-risk function (FSI 8th counterparty).** In financial services, the model-risk-management group reporting to the Chief Risk Officer, distinct from CISO and from AI Council, with its own SR 11-7-driven evidence requirements and an additional 8–16 weeks of cycle time. The eighth counterparty in any FSI agent procurement.

**Model-update notice.** The contractual SLA — typically 60 to 90 days — for a vendor to notify the buyer before swapping the underlying model. Must include re-eval rights, right-to-refuse, and pin-to-prior-version of at least 12 months.

**NIST AI RMF GenAI Profile.** The 2024 NIST AI Risk Management Framework Generative AI Profile. The closest US-side analog to EU AI Act Article 14 framing. Voluntary today; mentioned in federal acquisition guidance and procurement-template-shaping in late 2025 and 2026.

**OAuth blast radius.** The total scope of access an agent acquires when granted OAuth tokens against the buyer's identity fabric. An agent asking for "read all mail, all calendar, all files" has unbounded blast radius and should be rejected at Enterprise Architecture review on principle, not on use-case necessity. Least-privilege scope inventory per tool is the artifact.

**Outcome-based pricing.** Vendor pricing tied to a business outcome rather than seats or tokens. Common in CX (Sierra). Rare elsewhere. Procurement should price the unit-economics floor and the gaming risk before agreeing.

**Outcome-definition arbitrage.** The vendor's structural advantage in outcome-based pricing where the vendor controls the definition of "resolved" or "completed" and the buyer controls only post-hoc dispute. Resolved by dual-telemetry plus contractual dispute window plus third-party arbitration.

**Output ownership.** The contractual statement of who owns the agent's outputs (the buyer, the vendor, joint, public domain). Default vendor templates assume buyer ownership of inputs and joint or vendor ownership of outputs, which is wrong for most enterprise use cases.

**Per-action authorization tier.** The buyer-defined granularity of agent permissions — read-only, write-with-confirmation, autonomous — applied per action verb per tool. Vendor liability attaches only to autonomous-tier failures violating documented behavior. The order-form artifact, not the kickoff-email artifact.

**Per-trajectory billing.** Vendor pricing per completed agent trajectory rather than per token or per seat. Aligns vendor and buyer incentives on efficiency; gameable on trajectory boundary definition. Negotiate the definition before the rate. Anthropic Claude Agent SDK 2.0 (April 2026) and OpenAI Responses API expose per-trajectory cost views that make this billing unit independently auditable.

**Persistent memory.** Long-term storage of conversation history, derived facts, and user preferences the agent carries across sessions. Residency, deletion, and subpoena posture of persistent memory are first-class procurement questions, not afterthoughts.

**Planner-executor split.** An architectural pattern where a higher-capability model produces a plan and a lower-capability model executes the plan's individual steps. Dominant cost-optimization pattern of 2025–2026 and the architectural lever behind per-trajectory FinOps.

**Reasoning effort.** Buyer-controllable parameter (low / medium / high) on reasoning-enabled models (OpenAI o-series, Claude 4.5+, Gemini 2.5+) that trades latency and cost for trajectory quality. A procurement input now, not a developer-only knob.

**Sandboxing.** Containment of the agent's execution environment such that tool calls, file writes, and external requests are confined to a controlled scope. Becoming a SOC 2 / ISO 27001-adjacent control.

**Schrems-II posture.** The vendor's data-transfer regime for personal data moving between the EU and the US, post the 2020 Schrems-II decision and the EU-US Data Privacy Framework (2023). Required disclosure for any agent processing EU data; the agent's memory residency and tool-call destinations both count.

**Seventh counterparty (Enterprise Architecture).** At F1000 scale, the Chief Architect / Head of Platform / IT Ops chair is a distinct sign-off with its own queue and veto, owning OAuth blast radius, per-trajectory cost telemetry, sub-agent fan-out circuit-breakers, and reference-architecture conformance. Below F1000, EA folds into InfoSec or Procurement; at F1000 it does not.

**Signed eval report.** An evaluation artifact tied to a specific model identifier, dataset hash, and harness version, signed by a named vendor representative, reproducible by the buyer within a stated tolerance (±5 points). See Chapter III.5. As of May 2026 no vendor ships turnkey signed eval reports.

**Sovereign deployment.** Agent deployment posture in which model inference, agent runtime, persistent memory, and audit logs all reside within a single jurisdictional boundary, typically a sovereign-cloud region.

**SR 11-7.** US Federal Reserve guidance on model risk management. The de facto framework for financial-services AI model governance; covers validation, monitoring, and governance. Increasingly applied to LLM-driven credit, suitability, and underwriting decisions through 2025–2026.

**Sub-agent.** A specialized agent invoked by an orchestrator agent for a bounded role (planning, executing, verifying, escalating). Privilege separation between sub-agents is the agent-era equivalent of role-based access control.

**Sub-processor change.** Vendor's introduction of a new downstream service provider (e.g., a new model provider, a new vector database, a new observability platform). Triggers a procurement event under GDPR, DPA terms, and increasingly EU AI Act tie-out refresh.

**Tool-boundary policy.** The written, vendor-supplied document enumerating every tool an agent can invoke, the actions allowed, the privilege scopes, and the human-in-the-loop conditions. See Chapter III.1.

**Trajectory.** The complete sequence of an agent's reasoning steps, tool calls, sub-agent invocations, and final output for a single task. The trajectory — not the response — is the unit of evaluation and of cost.

**Trajectory cost audit.** A FinOps-for-agents exercise that measures the dollar cost per trajectory and identifies optimization (planner-executor split, prompt caching, FP4 quantization, aggregator routing) opportunities. Plausibly absorbed by AWS Bedrock auto-routing by H2 2027 — a 12-to-18-month advisory window.

**Training rights.** The contractual scope of what the vendor may do with the buyer's prompts, completions, and persistent memory for model training, fine-tuning, or eval-set augmentation. Bartz v. Anthropic and NYT v. OpenAI re-priced this language in 2024–2025; assume any ambiguity now reads against the vendor in 2026.

---

## Section VIII · Appendix — Reference Contract Clauses

The clauses below are sample MSA / DPA / AI-Addendum language. Lift them directly into your template. They are organized by the counterparty whose review the clause is for; a single clause may travel through two or three counterparties' redlines in sequence. The clauses pair with the fourteen addenda in Section IV — this Appendix is the operational form.

### For InfoSec

**Tool-boundary disclosure.** *"Vendor shall maintain and provide to Customer, upon request and at least annually, a Tool-Boundary Policy Document covering every tool the Agent is configured to invoke against any Customer System. Material changes to the Document shall be communicated to Customer no less than thirty (30) days before deployment to production. Vendor's failure to maintain or disclose this Document is a material breach permitting Customer to terminate this Agreement without penalty."*

**Indirect-injection red-team and kill-switch.** *"Vendor shall conduct an adaptive-adversary indirect-prompt-injection red-team assessment against the Agent no less frequently than quarterly. Discovery of an injection class against which the Agent's defense rate falls below sixty percent (60%) shall constitute a Security Incident requiring notification to Customer within forty-eight (48) hours, and Vendor shall make available a kill-switch procedure permitting Customer to disable the affected tool or agent pending remediation."*

**Sub-agent privilege separation.** *"Vendor shall enforce sub-agent privilege boundaries at runtime via capability tokens, signed delegation, or equivalent mechanism, and shall maintain test cases against cross-sub-agent privilege escalation. Architectural changes that alter the sub-agent privilege matrix shall be communicated to Customer no less than thirty (30) days before production deployment."*

**Audit-log retention.** *"Vendor shall maintain tamper-evident audit logs of all agent trajectories, tool invocations, and Outputs for seven (7) years, and shall provide Customer continuous read-access via a defined interface, in a format suitable for Customer's SIEM."*

### For Legal

**Training-data rights.** *"Vendor shall not use Customer Data, including prompts, completions, embeddings, or any derivative thereof, to train, fine-tune, or improve any Vendor or third-party model, without Customer's prior written consent on a per-use-case basis."*

**Output ownership.** *"As between the parties, Customer owns all Outputs generated by the Service in response to Customer prompts and Customer Data, subject to Vendor's underlying IP in the Service itself."*

**Hallucination indemnity.** *"Vendor shall indemnify Customer for damages from materially inaccurate Outputs reasonably relied upon in production, capped at two times (2x) ARR. This indemnity shall not be subject to the general liability cap."*

**Agent-action liability.** *"For Outputs that constitute autonomous actions taken by the Service on systems or data outside the Service's tenancy (including email, transactions, system modifications, external API calls), Vendor's indemnity shall extend to [N]x ARR, separately capped."*

**Model-update notification and pinning.** *"Vendor shall provide no less than sixty (60) days advance notice of any material change to the underlying foundation model. Customer shall have the right to pin to the prior model version for not less than twelve (12) months."*

**Action-rollback SLA.** *"Vendor shall maintain a written Action-Rollback Procedure for every Write Tool the Agent is configured to invoke against any Customer System of Record. Failure of a rollback within the SLA window shall constitute a Service Failure and entitle Customer to service credits as specified in the Service Level Schedule."*

### For Privacy

**Sub-processor consent.** *"Vendor shall maintain a current list of all sub-processors, including foundation-model providers, identifying data flows. Vendor shall provide thirty (30) days' notice of material changes, and Customer shall have the right to object."*

**Data residency for inference.** *"Vendor shall provide an option for inference to be processed exclusively within [EU / US / specified region], including all foundation-model calls, prompt retention, and output retention, with annual attestation."*

**Surgical deletion across memory.** *"Upon a data-subject erasure request, Vendor shall delete the affected data from the Agent's persistent memory, trajectory logs, and any fine-tuned weights within thirty (30) days, and shall provide a deletion confirmation log."*

### For AI Governance

**Signed reproducible eval reports.** *"Vendor shall provide to Customer, no less frequently than quarterly and within thirty (30) days of any model-version change affecting the Agent, a Signed Reproducible Eval Report specifying the model identifier, dataset identifier and hash, harness version, metrics, methodology, confidence intervals, and reproduction instructions. Reproduction by Customer's team within a reasonable window shall yield a score within five (5) points of the Report's stated score. A reproduction failure outside this tolerance shall constitute a material breach of the eval-evidence warranty."*

**EU AI Act Article 14 tie-out.** *"Vendor shall maintain and provide to Customer, upon request and at least annually, a Human Oversight Tie-Out Document mapping the Agent's design and operational features to the requirements of Article 14 of Regulation (EU) 2024/1689. Vendor warrants that the Document, taken together with the supporting evidence referenced therein, is sufficient to support Customer's good-faith demonstration of Article 14 compliance. Material misrepresentation of Article 14 conformity in the Document shall constitute a material breach."*

### For Procurement and Enterprise Architecture

**Per-trajectory cost transparency.** *"Vendor shall expose, via the Service's billing or observability interface, the per-trajectory cost decomposition for any Customer-initiated Agent task, including inference cost, telephony cost, human-review cost, and any other COGS component representing more than five percent (5%) of the per-trajectory total."*

**Outcome-definition and dispute mechanics.** *"For outcome-priced services, the Agreement shall specify (a) the precise definition of the chargeable outcome unit, (b) Vendor-side telemetry as the billing source of truth, (c) Customer-side telemetry as the audit override, (d) a thirty/sixty/ninety (30/60/90) day dispute window, and (e) third-party arbitration via [named arbitrator] for disputes unresolved within ninety (90) days."*

**Exit and data portability.** *"On termination, Vendor shall make Customer's persistent agent memory, trajectory logs, and configuration exportable in a documented format within thirty (30) days, and shall delete the same from Vendor systems within sixty (60) days following Customer's confirmation of export."*

---

## Closing

This Playbook is a position. It is not a neutral white paper, it is not a Gartner subscription, and it is not a substitute for the operational judgment of the seven counterparties whose chairs it tries to fit inside the same procurement gauntlet. It is the artifact I wish I had read three procurement cycles ago, and the artifact I would hand any F1000 CIO walking into an agent vendor evaluation in 2026 as the thing to read on the plane.

If you are a buyer using this Playbook to evaluate an agent vendor, the questions in Section II are yours. The overlays in Section III are yours. The decision tree in Section V is yours. Use them. Score the vendor against the Rubric in Section VI before you sign, and again before every renewal. If you are a vendor reading this Playbook to pre-empt the questions, every clause in Section IV is your homework, and every Pass cell in Section VI is the work you need to do before your next F1000 conversation.

This is Edition 1.0. It is falsifiable on purpose. The Rubric, the decision tree, and the addenda are written so that two competent procurement teams scoring the same vendor should arrive at the same answer; if they do not, the Playbook has failed and I want to know about it. The next edition will be informed by the gauntlets you run vendors through and by the artifacts vendors begin shipping in response. Send what worked, send what did not, send the clauses you redlined into your MSA and the cells where the Rubric was too generous or too strict. The standard improves by use.

The flag is planted. Reach me at alex@yedi.io.

*— Alex Yedi, May 2026*

