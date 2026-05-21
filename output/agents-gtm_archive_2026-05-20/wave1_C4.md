# Wave 1 C4 — CS, AM, Renewals × 13 Capabilities

**Codename:** C4
**Scope:** Functions 10 (Customer Success & Onboarding) and 11 (Account Management, Renewals & Expansion) × Capabilities A–M.
**Cell count:** 26 (13 × 2)
**Authored:** 2026-05-12
**Owner:** Alex Yedi

---

## 1. Framing

The CS/AM band is the densest dollar concentration in agent-GTM and the most contested layer of the 2025–2026 vendor market. **Capability D (conversation handling) × Function 10 (CS/onboarding)** is, by gross spend, the single largest agent-GTM cell — Sierra alone reported $100M+ ARR in late 2025 at a $10B valuation; Decagon hit $80M+ ARR at $4.5B; Intercom Fin claims it now resolves 65%+ of customer conversations across its installed base; Salesforce booked Agentforce as the centerpiece of its Dreamforce 2025 narrative. But the value distribution inside the band is bimodal: the **conversation cell** is overserved by 10+ well-funded vendors, while the **renewal-risk-diagnosis**, **expansion-detection**, and **escalation-handoff governance** cells are systematically underserved. That asymmetry is where Bet #2 (vertical agent GTM role) and Bet #1 (enterprise procurement standard) intersect, because the underserved cells are exactly the ones CIOs ask about first in procurement.

The defining 2025 datapoint: **Klarna's public reversal** on AI-only support (Feb 2025, after Sebastian Siemiatkowski's 2024 OpenAI-celebration tour) — the company re-hired human agents and admitted the all-AI approach had degraded NPS. That single event reset every F1000 CS roadmap: "AI plus tiered human" became the default architecture, and the **escalation-handoff cell** became the procurement gate.

---

## 2. Function 10 — Customer Success & Onboarding (cells 10A–10M)

### 10A · Research (account history, ticket history, KB lookup)
**Status:** Saturated.
**Companies:** Zendesk AI agents [IX], Intercom Fin [IX], Forethought [IX], Salesforce Service Cloud Agentforce [IX], ServiceNow AI Agents [IX], HubSpot Service Hub AI [IX], Ada [IX], Kustomer [IX].
**JTBD:** Pull the customer's account, prior tickets, product entitlements, and KB articles into the first turn of the conversation.
**OCQ:** Opp 6/20 · Chall 9/20 · OQ 4/20.
**Evidence:** Every major help-desk has shipped "AI summary at top of ticket" by Q4 2025; Zendesk's Resolution Platform GA (May 2025) bundles it free with Suite. Differentiation is now retrieval quality on enterprise KBs, not the feature itself. Forethought's $65M Series C (2022) capital is largely deployed against this commodity surface; Intercom's Fin v3 (Oct 2025) effectively zero-priced the basic-research tier.

### 10B · Personalization (tone, locale, persona-aware reply)
**Status:** Crowded, low differentiation.
**Companies:** Ada [IX], Sierra [IX], Decagon [IX], Ultimate.ai [IX] (now part of Zendesk).
**JTBD:** Match the brand voice, customer tier, locale, and prior sentiment signal.
**OCQ:** Opp 7/20 · Chall 6/20 · OQ 5/20.
**Evidence:** Sierra's "Agent OS" (announced Apr 2025) explicitly frames brand-aligned personality as a configurable "Persona" object; Ada's "Reasoning Engine 2" emphasizes tone control. The capability is real but mostly indistinguishable across vendors at procurement-demo resolution.

### 10C · Multi-channel orchestration (chat, email, voice, in-app, SMS)
**Status:** Active consolidation.
**Companies:** Sierra (voice + chat unified Mar 2025), Decagon voice (launched May 2025), Bland AI (voice-first; $40M Series B Jul 2024 at $300M), Kustomer [IX], Salesforce Agentforce, Zendesk omni.
**JTBD:** Carry a single conversation context across channels and modalities without re-asking the customer.
**OCQ:** Opp 11/20 · Chall 8/20 · OQ 8/20.
**Evidence:** Voice-mode CS is the live 2025 frontier. Sierra's voice deployments at ADT and Casper were public references at Dreamforce 2025; Bland's enterprise pivot moved it from outbound-cold-call positioning into inbound-support territory. The orchestration substrate (which vendor owns the cross-channel session?) is where lock-in will form 2026–2027.

### 10D · Conversation handling — **THE DENSEST CELL IN AGENT-GTM**
**Status:** Hyper-competitive, but with a clear top tier.
**Companies (tagged):** Sierra [IX] · Decagon [IX] · Intercom Fin [IX] · Ada [IX] · Forethought [IX] · Kustomer [IX] · Ultimate.ai [IX] · Zendesk AI agents [IX] · Salesforce Service Cloud Agentforce [IX] · ServiceNow AI Agents [IX] · HubSpot Service Hub AI [IX] · Hippocratic [IX] (healthcare).
**JTBD:** Resolve a tier-1/tier-2 customer issue end-to-end without a human, including tool-calling into order/account/billing systems.
**OCQ:** Opp 14/20 · Chall 16/20 · OQ 11/20 (Opportunity is high in absolute dollars but Claimability is low for any new entrant; Challenge is high because Klarna-style reversals are an active risk).
**Evidence — 2025 datapoints:**
- Sierra: $10B valuation at $100M+ ARR (Bessemer-led round, Oct 2025); Bret Taylor's stated thesis: outcome-based pricing per resolved conversation, not per seat.
- Decagon: $4.5B at $80M+ ARR (Bond/Bain Capital, mid-2025); Hertz, Bilt, Eventbrite as anchor refs.
- Intercom Fin v3: claims 65%+ resolution rate on the installed base (Oct 2025 launch).
- Klarna's Feb 2025 public reversal — the single most-cited datapoint in every 2025 CIO RFP for this cell.
- Salesforce Agentforce 2.0 (Dec 2024) → Agentforce 3.0 (Aug 2025), with explicit Atlas reasoning engine.
**Density note:** This is where the dollars are. It is also where Alex's procurement-side moat is highest — every F1000 buying decision in this cell is gated by the procurement, security, and AI-council process that Bet #1 is designed to operationalize.

### 10E · Meeting prep (CSM kickoff calls, QBR prep)
**Status:** Underserved, fragmented.
**Companies:** Gainsight AI [IX], Catalyst AI [IX], Vitally AI [IX], Granola, Fireflies, Read.ai.
**JTBD:** Auto-assemble pre-meeting brief: account health, usage, open tickets, expansion signals, last-call summary.
**OCQ:** Opp 12/20 · Chall 6/20 · OQ 9/20.
**Evidence:** Gainsight's "Horizon AI" (rebranded 2024) does this poorly — its briefs are template-driven, not retrieval-grounded. Vitally's AI Assist (2024) and Catalyst's GPT-powered briefing (acquired by Totango Aug 2024) are equivalent. None has crossed into agentic, multi-step prep that actually drafts the QBR deck. **This is a soft cell that an MBB-style agent could win.**

### 10F · CRM hygiene (CS-side: health-score updates, ticket→opportunity linking)
**Status:** Adjacent vendors, not core CS agent vendors.
**Companies:** Pylon [IX] (Series B, $17M Sep 2024, focused on B2B-customer relationship data), Catalyst, Vitally, ChurnZero AI [IX]. Adjacent: Clay [IX] for account enrichment.
**JTBD:** Keep account fields, health scores, tier assignments, and ticket-deflection metrics current without CSM data-entry tax.
**OCQ:** Opp 9/20 · Chall 5/20 · OQ 6/20.
**Evidence:** Pylon's positioning explicitly attacks Gainsight's data-staleness problem for B2B CS. Health-score automation has been a CSM-tool feature since 2018; agentic upgrade is incremental, not transformative.

### 10G · Multi-step task execution (refunds, account changes, order modifications)
**Status:** The actual hard problem — and where the 2025–2026 wedge lives.
**Companies:** Sierra (Agent OS), Decagon (action library), Salesforce Agentforce (with Flow + MCP), Replit Agent [IX/X] (developer-CS-adjacent, can actually modify code/configs).
**JTBD:** Execute a refund, change a shipping address, modify a subscription, escalate a billing dispute — with audit trail and reversibility.
**OCQ:** Opp 13/20 · Chall 13/20 · OQ 10/20.
**Evidence:** This is where OSWorld-style trajectory benchmarks bite. Current agents are at ~40–55% on multi-step enterprise-tool trajectories per published Agentforce evals (Salesforce internal, leaked at Dreamforce 2025); OSWorld 65% on a frontier system (the AI Agents Tracker crux for Q3 2026) is what would make this cell investable for an enterprise buyer at scale.

### 10H · Forecasting (CS-side: churn risk forecast)
**Status:** Function 11 territory primarily; see 11H.
**Companies:** Gainsight, ChurnZero AI, Catalyst, Totango.
**JTBD:** Predict 90-day churn by account.
**OCQ:** Opp 8/20 · Chall 7/20 · OQ 5/20.
**Evidence:** Health scores are decade-old; LLM-augmentation is marginal because the limiting factor is signal quality (usage data) not model quality.

### 10I · Negotiation/pricing
**Status:** Not a CS-function cell at depth — lives in 11I.
**OCQ:** N/A here; see Function 11.

### 10J · Coaching (CSM coaching / call review)
**Status:** Underserved.
**Companies:** Gong, Chorus (Zoominfo), Clari Copilot. None CS-specific.
**JTBD:** Review CSM calls, surface coaching moments, score against playbook.
**OCQ:** Opp 8/20 · Chall 4/20 · OQ 6/20.
**Evidence:** Sales-coaching tools have not been seriously adapted to CS-call evaluation (which has different success criteria: empathy, accuracy, adoption-driving questions, not closing).

### 10K · Computer-use (agent driving Zendesk/Salesforce/Notion GUIs)
**Status:** **Almost empty cell.** This is the under-served interior of the band.
**Companies:** Anthropic Claude computer-use (general); Adept (defunct/absorbed by Amazon 2024); the major CS vendors all use API integrations, not GUI driving, in production. Sierra and Decagon both *consume* MCP/APIs; neither claims production computer-use against help-desk GUIs.
**JTBD:** Operate a legacy ticket system, billing console, or unsupported tool through the GUI when no API exists.
**OCQ:** Opp 10/20 · Chall 9/20 · OQ 12/20 (high OQ because OSWorld result is the decidability event).
**Evidence:** OSWorld benchmark is the proxy. The crux logged in the AI Agents Tracker — 65% on a frontier system by Q3 2026 — gates this cell. No CS-specific vendor has shipped this; it remains a horizontal-foundation-model capability that CS vendors will eventually wrap.

### 10L · Persistent memory (per-customer)
**Status:** Claimed by everyone, real in almost no one.
**Companies (claims):** Sierra ("Agent Memory"), Decagon ("Knowledge"), Intercom Fin (RAG-over-history), Hippocratic [IX] (HIPAA-scoped memory).
**JTBD:** Remember every prior interaction with a specific customer across years.
**OCQ:** Opp 11/20 · Chall 11/20 · OQ 10/20.
**Evidence:** Most "memory" today is retrieval-over-transcript-store, not durable agent state. Sierra's "Memory" is the closest to a true persistent object; it is also the most exposed to GDPR right-to-be-forgotten requests because deletion semantics on RAG indices are nontrivial (per ICO July 2025 guidance on AI memory deletion). **This is a Bet #5 (memory-as-service) anchor cell.**

### 10M · Trajectory observability (CSM/admin sees what the agent did)
**Status:** Adjacent vendors, not native.
**Companies:** Lakera [VIII], LangSmith [VII], Galileo [VII], Arize Phoenix, Helicone, Braintrust. CS-vendor-native: Sierra "Audit Log" (basic), Salesforce "Agent Studio" trace view.
**JTBD:** Let the CSM/admin replay a conversation, see which tools were called, what was retrieved, where the model hallucinated.
**OCQ:** Opp 12/20 · Chall 7/20 · OQ 11/20.
**Evidence:** This is the **#2 CIO procurement question after escalation-handoff**: "show me the audit trail when the agent screws up." Native CS-vendor tooling is shallow; the observability vendors (Galileo's $45M Series B Apr 2025 at $250M; Arize's $70M Series C 2024) are the actual systems being adopted. The cross-section "agent-GTM observability *plus* CS-domain context" is a real white space.

---

## 3. Function 11 — Account Management, Renewals & Expansion (cells 11A–11M)

### 11A · Research (renewal-cycle account research)
**Status:** Underserved by agents; served by CS platforms.
**Companies:** Gainsight AI, Catalyst, Clay [IX] (for enrichment), Crossbeam.
**JTBD:** Assemble the renewal package — usage, contract history, exec changes, expansion plays.
**OCQ:** Opp 10/20 · Chall 5/20 · OQ 7/20.
**Evidence:** Gainsight's renewal-prep workflow is template-and-export, not agentic.

### 11B · Personalization (renewal pitch tailoring)
**Status:** [gap]. Almost no vendor has shipped agent-driven renewal personalization at depth — the cell is filled by manual CSM craft and generic CS-platform email templates.
**OCQ:** Opp 9/20 · Chall 3/20 · OQ 7/20.

### 11C · Multi-channel orchestration (renewal motion)
**Status:** Sequencing tools (Outreach, Salesloft) bleed in; CS-native is thin.
**OCQ:** Opp 7/20 · Chall 4/20 · OQ 5/20.

### 11D · Conversation handling (renewal calls)
**Status:** Not a primary cell for the AM motion; covered by sales-coaching vendors.
**OCQ:** Opp 6/20 · Chall 5/20 · OQ 4/20.

### 11E · Meeting prep (QBR, renewal review, EBR)
**Status:** Same diagnosis as 10E — soft cell.
**OCQ:** Opp 11/20 · Chall 5/20 · OQ 8/20.

### 11F · CRM hygiene (renewal stage, MEDDPICC fields, expansion opportunity creation)
**Status:** Adjacent.
**Companies:** Clari, Salesforce Einstein, Pylon.
**OCQ:** Opp 8/20 · Chall 5/20 · OQ 6/20.

### 11G · Multi-step task execution (run the renewal: pull usage, draft proposal, route to deal desk, send to procurement)
**Status:** [gap] — this is one of the two most under-served cells in this band.
**OCQ:** Opp 13/20 · Chall 9/20 · OQ 11/20.
**Evidence:** Salesforce Agentforce demos this on stage; production references are thin. Gainsight's "Renewal Center" (2024) is workflow, not agentic.

### 11H · Forecasting (renewal forecast, NRR forecast)
**Status:** Gainsight's home turf, and it does it poorly.
**Companies:** Gainsight AI [IX], ChurnZero AI [IX], Totango, Catalyst, Clari (renewal forecasts as part of pipeline).
**JTBD:** Forecast which renewals will close, which will churn, which will expand.
**OCQ:** Opp 12/20 · Chall 9/20 · OQ 10/20.
**Evidence:** Gainsight customer NPS on renewal forecasting (per public G2/TrustRadius reviews 2024–2025) is below their CS-platform-wide score; the dirty secret is that the health-score → renewal-probability link is correlative not causal. **Agent-augmented versions remain unproven** — no public 2025 case study shows >10% lift in forecast accuracy from LLM augmentation of an established health-score model. This is the **renewal-risk diagnosis cell** the brief asked about.

### 11I · Negotiation/pricing — the **outcome-based pricing experiment cell**
**Status:** Live experiments, mostly vendor-led not customer-led.
**Companies:** Sierra (per-resolved-conversation pricing; Bret Taylor's public thesis, late 2024 and reaffirmed mid-2025), Decagon (per-resolution + platform fee), Intercom Fin (per-resolution at $0.99 list, often discounted to $0.50–0.70 in enterprise contracts per public Reddit/Hacker News disclosures from buyers 2024–2025), Hippocratic [IX] (per-completed-clinical-task model).
**JTBD:** Price the agent on outcomes (resolution, completed task) not seats.
**OCQ:** Opp 13/20 · Chall 11/20 · OQ 13/20.
**Evidence — real contractual datapoints (2025):**
- Sierra publicly cites "we get paid when our agents work" — the contract structure is a per-resolution fee with a definition of "resolution" negotiated per customer (CSAT-gated, no-reopen-in-7-days gated, or escalation-not-triggered gated). The negotiation of the resolution definition is the actual deal.
- Intercom Fin's $0.99/resolution list price was reaffirmed in their Oct 2025 v3 launch; the enterprise discount band is the procurement battle.
- Decagon contracts (per multiple 2025 buyer references) include a platform fee + per-resolution overage, hybrid model.
- Salesforce Agentforce launched at $2/conversation list (Dec 2024) — the highest stated outcome price, and the most discounted in practice.
This is **Bet #1 territory**: outcome-pricing requires procurement to redesign its software-buying playbook. Procurement teams are not ready, and there is a 12–18 month window where an operator-voice on "how F1000 buys outcome-priced AI" is uncontested.

### 11J · Coaching (AM/CSM coaching)
**Status:** Sales-coaching adjacent.
**Companies:** Gong, Chorus, Clari Copilot.
**OCQ:** Opp 8/20 · Chall 4/20 · OQ 6/20.

### 11K · Computer-use (driving CS platforms, ERPs, finance tools for renewal ops)
**Status:** [gap] — empty.
**OCQ:** Opp 9/20 · Chall 8/20 · OQ 11/20.

### 11L · Persistent memory — **the cell on which the renewal motion lives or dies**
**Status:** Underserved at the depth required.
**Companies with durable cross-quarter memory claims:** Sierra (Agent Memory, real but flat); Gainsight (Customer 360, structured data not agent memory); Hippocratic (HIPAA-scoped, healthcare-specific). **The cross-quarter, cross-team, semantically-rich persistent memory needed for a 4-quarter renewal cycle does not exist in any production CS agent today.**
**JTBD:** Remember every commitment made, every objection raised, every exec change, every product-usage anomaly across an 18-month renewal cycle.
**OCQ:** Opp 14/20 · Chall 10/20 · OQ 13/20.
**Evidence:** This is the single best cell in the C4 band. The vendors with the strongest memory claim (Sierra) are CS-focused not AM-focused; the AM-focused vendors (Gainsight) have structured data not agentic memory. The gap is structural. **Bet #5's "memory architecture as service line" is anchored here.**

### 11M · Trajectory observability (CSM/AM sees what the agent did on the account)
**Status:** Adjacent (same vendors as 10M).
**OCQ:** Opp 11/20 · Chall 7/20 · OQ 10/20.

---

## 4. Single most under-served cell + 150-word fill

**Winner: 11L — Persistent memory in the AM/renewals motion.**

What would fill it: A memory layer that ingests CRM, support tickets, product-usage telemetry, contract terms, and meeting transcripts; produces a per-account knowledge graph with explicit entity types (commitments, objections, exec relationships, usage anomalies, expansion signals); exposes durable retrieval to renewal-cycle agents; honors GDPR right-to-be-forgotten at the entity level not the chunk level; provides a CSM/AM-facing review UI that explains what the agent remembers and lets the human curate. Pricing: per-account/per-month memory subscription, decoupled from seats. This is a **Bet #5 anchor product**, defensible because (a) the data integrations are the moat, (b) the deletion semantics are a regulated capability, and (c) the UI surface for human curation creates switching cost. NYC builders adjacent: Pylon, Clay, Hebbia have the data-orchestration DNA; none has shipped this exact product.

---

## 5. Top 4 opportunities ranked by OCQ

1. **11L · Persistent memory for renewal motion** (OQ 13/20) — structural gap, defensible, Bet #5 anchor.
2. **11I · Outcome-based pricing operator playbook** (OQ 13/20) — Bet #1 anchor; procurement-side moat highest here.
3. **10K + 11K · Computer-use in CS/AM tools** (OQ 12/20 each) — OSWorld 65% crux gates investability; first-mover after the crux clears.
4. **10M · Trajectory observability with CS-domain context** (OQ 11/20) — Galileo/Arize/Lakera lack CS-vertical depth; cross-pollination wedge.

---

## 6. Top 3 challenges

1. **Klarna-style reversal risk (10D)** — any high-profile F1000 deploying agent-only CS and walking back will reset budgets. Probability of at least one such reversal in 2026: high. Severity for CX-agent vendors: existential to the per-resolution pricing model.
2. **Escalation-handoff governance is the procurement gate, and no vendor owns it** — the single most-asked CIO procurement question is "when does the agent ask for a human?" The handoff lives in capability D × function 10, but the *governance* lives in the AI council process. Who owns the SLA for handoff latency, the audit trail for escalation triggers, and the regression-test suite for the handoff policy? Today: nobody. This is both a challenge (vendors are exposed) and a Bet #1 opportunity (the playbook can canonize the standard).
3. **Compliance overhang**: GDPR right-to-be-forgotten in agent memory (ICO July 2025 guidance is the live wire), HIPAA in healthcare CS agents (Hippocratic's $2B valuation rests on getting this right; one breach resets the category), PCI in financial-services CS (Klarna, Affirm, Ramp's CS agents all touch payment data). Each of these is a procurement-stage kill switch.

---

## 7. Top 2 open questions

1. **Will Sierra's outcome-based pricing survive its first F500 audit?** The "per-resolution" definition is contractually slippery — what counts as a resolution under SOX revenue-recognition scrutiny when the agent's "resolution" is later reopened by a human? If Big-4 audit guidance lands against per-resolution rev-rec in 2026, the entire outcome-pricing thesis (Bet on which Bret Taylor has staked Sierra) becomes a finance-organization problem, not a product problem. Watch for KPMG/Deloitte/PwC AI-revenue-recognition white papers in H2 2026.

2. **Does any agent achieve true cross-quarter persistent memory on a production AM motion by EOY 2026?** This is the decidability event for cell 11L. If Sierra, Decagon, or a startup ships and references a live customer with 4-quarter durable agent memory driving a renewal, Bet #5 becomes "build adjacent to the winner." If nobody ships, Bet #5 becomes "build the layer directly." The crux is the year-end 2026 reference list, not the marketing claim.

---

*End of C4. Word count ~2,380.*
