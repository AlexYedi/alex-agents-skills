# F5 — The F1000 Agent Procurement Gauntlet: Counterparties, Cycle, and the Fourteen AI Addenda

**Scope.** Map the F1000 buyer-side procurement gauntlet as it actually runs in 2026 for AI-agent vendors specifically — who sits in each chair, what they evaluate, what they reject for, what they need, what they will ask, and what the seller can do to make their job easier. Then build the canonical list of fourteen AI-specific contractual addenda that hardened into the buyer-side template between 2024 and May 2026. Close with three sectoral overlays (FSI, healthcare, defense/gov).

**Inheritance.** Buyer-side complement to the Part XIII rubric in the Volume III Addendum and to the Job 6 phase map. The rubric is *what the buyer asks at each phase*; this chapter is *who in the org chart asks it, when, and why*. Together they are chapters 1–2 of the Procurement Playbook.

**Audience.** Senior buyer-side reader at F1000 — CIO, CISO, AI Council Chair, CPO, GC — and the vendor sales leader walking into that room. Written from inside the buyer's chair.

---

## 0. Six or Seven Counterparties at F1000?

Alex's working hypothesis is that the standard "six approver" model under-counts at F1000 specifically. The seventh is **Enterprise Architecture / IT Ops** (CIO / Chief Architect / Head of Platform). At sub-$10B it folds into InfoSec or Procurement; at F1000 scale it is a distinct sign-off with its own queue and veto. Evidence for EA as distinct: it owns the cloud bill (unbounded trajectory cost is an EA problem, not an InfoSec one); it owns the reference architecture (vendors that demand non-conformant identity, observability, or runtime get blocked here); it owns the identity fabric and the OAuth blast radius (agents asking for "read all mail, all calendar, all files" trigger EA review for blast radius, not InfoSec review for credential security); it owns on-call and operability (no runbook, no RTO/RPO = EA blocks); it owns capacity (F1000 runs agents at 10⁴–10⁶ concurrency and EA stress-tests vendor claims because Procurement and InfoSec lack the vocabulary).

**Recommendation: Seven at F1000.** EA is treated below as the seventh counterparty.

---

## 1. InfoSec (CISO / Security Architecture / GRC)

**Who.** CISO reports to CIO at ~55% of F1000, to CEO at ~25%, to CRO/CFO/GC at ~20% (the post-Yahoo/Uber/SolarWinds independent-CISO pattern). For agent vendors, **Security Architecture** is load-bearing — they decide whether the proposed architecture is acceptable in principle before GRC processes the paperwork.

**What they actually evaluate.** Not "is the vendor SOC 2" (SOC 2 is floor). For agents: (a) trust boundary between vendor runtime and our data plane, (b) what tools/MCP servers/APIs can the agent invoke, on whose authority, with what credentials, (c) blast radius if prompt injection succeeds, (d) rollback story for wrong actions, (e) tamper-evident trajectory log exportable to our SIEM, (f) ability to run in our VPC/tenancy/keys, (g) foundation-model dependency chain.

**What they will reject for.** (1) Unbounded tool scope with no documented tool-boundary policy. (2) No tamper-evident audit log meeting buyer's 1–7 year retention floor. (3) Shared-tenancy inference for regulated data. (4) No documented indirect-prompt-injection defense — post-Microsoft Copilot Studio prompt-injection demos (Black Hat 2024) and EchoLeak (2025), this is a hard line. (5) Vendor can't answer "what happens if your foundation-model provider has an outage / update / vulnerability" — CISOs live in the shadow of CrowdStrike (July 2024).

**Review cycle.** Questionnaire turnaround 4–8 weeks; architecture review 2–6 weeks; pen-test review 4–12 weeks. **Total time-in-queue: 10–20 weeks**, FSI/healthcare upper bound.

**Artifacts.** SOC 2 Type II (current, unqualified), ISO 27001 if EU-exposed, completed SIG/CAIQ/HECVAT, third-party pen-test within 12 months, plus the AI-specific addenda: model card, signed eval report, red-team report, indirect-prompt-injection attestation, tool-boundary policy, sub-agent privilege model, kill-switch documentation, sub-processor list with foundation-model providers named, foundation-model fallback plan.

**New AI-specific concerns since 2022.** Indirect prompt injection from data ingested; tool-boundary enforcement at runtime not just config; sub-agent privilege escalation; foundation-model supply chain (deprecation, drift, outage, vulnerability); trajectory log integrity.

**Escalation/blockers.** CISO escalates to CIO, CRO, or board risk committee. Overridden when business sponsor has CEO air-cover for strategic gaps (Sierra into CX, Harvey into law firm) or when GC accepts contractual risk transfer. Rarely overridden on FedRAMP, HIPAA, FFIEC floors.

**Three questions they will ask in 2026.**
1. *"Walk me through your tool-boundary policy. What can your agent call, on whose authority, enforced at runtime — not config time."*
2. *"Show me your indirect-prompt-injection defense — adaptive-adversary red-team report, not a benchmark — and the refresh cadence."*
3. *"If your foundation-model provider issues a model update tomorrow, what happens to our deployment, what notice do we get, and what is our right to pin and to test."*

**Vendor tactical guide.** Ship a Trust Center with CAIQ, SIG, model card, signed eval, red-team summary, prompt-injection attestation, sub-processor list, and a one-page architecture diagram with trust boundary explicit — all dated. Volunteer buyer's-VPC deployment early. Bring a security engineer to the second meeting, not GRC.

---

## 2. Legal (GC / Commercial Counsel / IP)

**Who.** GC reports to CEO and to the board audit/governance committee. Below: Commercial Counsel (MSA/DPA/order form), IP Counsel (training data, output ownership), Litigation Counsel (indemnity, liability), and an **AI-dedicated counsel** seat that did not exist in 2022 — often a senior Commercial Counsel cross-trained, or a hire from the AI practice groups at Cooley, Wilson Sonsini, Latham, Morrison Foerster.

**What they evaluate.** Liability allocation for agent actions/outputs; ownership of inputs, outputs, derived data; indemnity scope (hallucination, IP, third-party content); audit/pause/terminate rights; exit and data portability; sub-processor visibility; insurance floors; agent-specific carve-outs.

**What they will reject for.** (1) Hallucination liability disclaimed entirely — post-*Moffatt v. Air Canada* (BC CRT, Feb 2024), the "chatbot is a separate legal entity" theory is the bad-case study; GCs want the vendor on the hook. (2) Output-ownership ambiguity or refusal to disclaim training rights — post-Bartz v. Anthropic (Aug 2024) and the NYT v. OpenAI/Microsoft consolidated litigation. (3) Indemnity caps below the AI-specific floor (a $1M aggregate cap on $250K ARR was acceptable in 2022; today AI indemnity needs at least 2x ARR with separate carve-outs). (4) No model-change notification — post-GPT-4 to Turbo behavior drift and Claude 3.5→3.6→3.7 sequence. (5) Foundation-model sub-processor not disclosed (DPA fails Privacy review, contract fails Legal).

**Review cycle.** First redline 2–4 weeks; negotiation rounds 2–5 (vs. 1–2 for traditional SaaS). **Total time-in-queue: 8–16 weeks**.

**Artifacts.** MSA, DPA, AI Addendum, BAA if PHI in scope, sub-processor list with foundation-model providers, insurance certificates (E&O, cyber, AI-specific tower if >$1M ARR), indemnity-backing evidence, order form, SLA exhibit, third-party content licenses (post-NYT v. OpenAI).

**New AI-specific concerns.** Agent-action liability (autonomous email, ticket, refund, return); training-data provenance; output ownership and derivative-work risk (Getty v. Stability AI 2023–2025; music-industry cases); model-update notice and pinning rights; termination and exit data rights (persistent memory, trajectory logs, fine-tuned adapters).

**Escalation/blockers.** GC escalates to CEO or board audit. Overridden when sponsor has board air-cover, when deal is below GC escalation floor ($250K–$1M ARR), or when Procurement and InfoSec have cleared and Legal is the last gate at quarter-end. Rarely overridden on indemnity floors or sub-processor disclosure.

**Three questions in 2026.**
1. *"Walk me through your indemnity stack. Cap on IP infringement, cap on hallucination, cap on agent action, and the insurance tower backing it."*
2. *"Show me the AI Addendum. Training-data carve-out, model-update notice, output ownership, kill-switch rights, termination-data rights."*
3. *"Who is your foundation-model sub-processor, and your contingency if their terms change against you mid-contract."*

**Vendor tactical guide.** Publish a public AI Addendum with buyer-favorable defaults pre-baked (no training on customer data, output ownership to customer, model-update notice with pinning, foundation-model providers named, indemnity stack disclosed). Pre-clear BAA if healthcare. Volunteer insurance-tower disclosure. Do not redline standard EU SCCs out of customer DPAs — signals you are not EU-ready.

---

## 3. Privacy (CPO / DPO / Privacy Counsel)

**Who.** CPO reports to GC at ~60%, CISO at ~20%, CEO/CRO at ~20%. DPO is statutorily required in the EU under GDPR Article 37. Below: Privacy Counsel (DPIA, cross-border), Privacy Engineering (controls, consent, data-subject-rights tooling), AI Ethics seats embedded in privacy or the AI Council.

**What they evaluate.** What personal data the agent ingests; lawful basis; retention; processing location; controller/processor split; data-subject rights (access, deletion, portability, Article 22 objection); cross-border transfer mechanism (SCCs, adequacy, DPF); whether the agent makes automated decisions about EU subjects under Article 22; special-category data; DPIA. For agents specifically, the new lens is **contextual integrity** (Nissenbaum) — does data collected in sales get used in HR.

**What they will reject for.** (1) No DPIA, or one that does not name agent-specific risks. (2) Cross-border transfer with no clean Schrems II-compliant mechanism. (3) Training on EU personal data without lawful basis (Italian Garante's ChatGPT order, March 2023, is the precedent). (4) No surgical-deletion mechanism for data-subject erasure across the agent's persistent memory, trajectory logs, and any fine-tuned weights — within GDPR's 30 days. (5) Special-category data (GDPR Article 9) routed without documented basis.

**Review cycle.** DPIA review 3–6 weeks; cross-border review 2–4 weeks. **Total: 6–12 weeks**, longer for healthcare, public sector, EU-HQ buyers.

**Artifacts.** DPA with preferred SCCs, DPIA template completed for buyer's use-case, sub-processor list, data-flow diagram across borders, retention schedule, DSR process, TOMs annex.

**New AI-specific concerns.** Persistent agent memory and right to be forgotten; inference-time data leakage (foundation-model provider sees prompts; prompts leave region; prompts retained); contextual integrity across the agent's tool surface; Article 22 ADM and CCPA's November 2025 ADMT rule (effective); EU AI Act Article 14 human-oversight tie-out (Privacy increasingly owns half of this with AI Council).

**Escalation/blockers.** CPO escalates to GC, board audit, or — in EU — to the DPO with independent statutory protection. Overridden only when residual risk is documented and DPO records objection. Rarely overridden on Article 22, DSR, or special-category data.

**Three questions in 2026.**
1. *"Show me your data-flow diagram. Where does the prompt go, the output go, the memory persist, what borders does any of it cross."*
2. *"If a data subject asks us to delete their data, what is the surgical-deletion mechanism in your agent's memory and trajectory logs, and what is your SLA."*
3. *"For automated decisions about EU subjects, show me the human-in-the-loop and the Article 22 conformance documentation."*

**Vendor tactical guide.** Ship pre-completed DPIA templates per use-case (sales, support, HR, finance). Offer EU-only inference routing as a tier. Document surgical-deletion explicitly. Pre-publish sub-processor list with 30-day notice rights. Volunteer Schrems II supplementary-measures analysis.

---

## 4. AI Governance Council

**Who.** The newest counterparty, stood up at virtually every F1000 between 2023 and 2025 in response to the EU AI Act passage (March 2024), NIST AI RMF and GenAI Profile (Jan 2023 / July 2024), the Biden Executive Order (Oct 2023) and Trump's EO (Jan 2025), NYC Local Law 144 (effective July 2023), Colorado AI Act (passed May 2024, effective Feb 2026), and consolidating state-level AI legislation. Chairs to a CTO, CDO, Chief AI Officer (a 2024–2025 role explosion), COO, or CRO. Membership: CISO, CPO, GC, business-line reps, often an external advisor or ethics seat. Issues internal AI Use Policy, maintains approved-vendor list, gates any new AI deployment above a risk threshold.

**What they evaluate.** Whether the vendor risk profile fits the AI Use Policy; control mapping to NIST AI RMF and ISO 42001; whether the deployment is "high-risk" under EU AI Act Annex III (HR, credit, education, law enforcement, critical infrastructure, biometrics); human-oversight effectiveness (Article 14); FRIA support if required; bias testing; model card and evaluation credibility; misuse and dual-use pressure tests.

**What they will reject for.** (1) No evidence of NIST AI RMF or ISO 42001 conformity (the new floor). (2) Bias testing absent or stale — post-NYC LL 144 and Colorado AI Act, hiring and credit agents need annual disparate-impact analysis. (3) Theatrical human oversight — a "human in the loop" reviewing 1000 decisions per hour is not effective oversight under Article 14. (4) No FRIA for high-risk EU AI Act deployments — April 2026 draft enforcement guidance makes this explicit; August 2026 window enforces. (5) Vendor refuses to share evaluation methodology, dataset, results in a re-runnable form — signed reproducible eval reports are the 2026 standard.

**Review cycle.** Council meets monthly or biweekly. **Intake-to-decision: 6–14 weeks routine, 12–24 weeks high-risk with FRIA.** Cross-functional design makes it inherently slow.

**Artifacts.** Model card (substance, not marketing); evaluation report (signed and reproducible preferred); red-team report with named methodology; NIST AI RMF GenAI Profile control mapping; ISO 42001 mapping; FRIA template; bias audit (NYC LL 144, Colorado AI Act); prompt-injection attestation; Article 14 human-oversight design; sub-agent privilege-separation design; trajectory observability surface.

**New AI-specific concerns.** Foundation-model risk inherited from the lab (Anthropic RSP, OpenAI Preparedness, Google Frontier Safety) and how the vendor passes that through; high-risk classification under Annex III; evaluation reproducibility and tamper-resistance (model pin, dataset hash, harness version, signed); human-oversight effectiveness; cumulative portfolio risk across the buyer's agent fleet.

**Escalation/blockers.** Escalates to executive committee or board risk. Rarely overridden — it exists precisely to be the slow-but-decisive gate. Blocked downward when sponsor brings CEO in early. Rarely overridden on FRIA, bias findings, or Article 14.

**Three questions in 2026.**
1. *"Show me your evaluation report — signed, reproducible, with model pin, dataset hash, harness version, and methodology. Walk me through your red-team for indirect prompt injection."*
2. *"Map your controls to NIST AI RMF GenAI Profile and ISO 42001. If you have an EU AI Act conformity assessment, show it. If not, tell me when."*
3. *"Show me the human-oversight design for our use-case. Article 14 in practice. Not the marketing version."*

**Vendor tactical guide.** Publish a signed reproducible eval. Publish a real model card. Publish NIST AI RMF and ISO 42001 mappings with control IDs and reproducible evidence. Volunteer the FRIA template. Bring an AI Safety/Trust engineer, not the AE. Do not pretend a benchmark is an evaluation or a marketing summary is a red-team.

---

## 5. Procurement (CPO / Strategic Sourcing / Vendor Management)

**Who.** CPO reports to CFO at ~70%, COO at ~20%. Below: Strategic Sourcing (the category manager who runs the RFP), Vendor Management (post-signature performance), Procurement Ops (P2P plumbing), and an **AI Category Manager** seat (a 2024–2025 role explosion driven by AI-spend visibility on the cloud bill and the apples-to-oranges comparison problem).

**What they evaluate.** Commercial terms (pricing model, term, ramp, true-up); vendor viability (financials, concentration, investor profile); reference checks; competitive bake-off; total cost (foundation-model passthrough, infra footprint, integration); negotiation history with industry peers; exit story.

**What they will reject for.** (1) Pricing not benchmarkable — per-trajectory, per-token, per-resolved-case, per-seat; each vendor uses a different unit. (2) Vendor viability concerns — sub-$10M ARR selling to F1000 with no path to capitalization, no enterprise references, no auditable financials. (3) No exit story — what happens to memory, trajectory logs, fine-tuned adapters, integrations on termination. (4) MFN refusal at scale when buyer is top-10% of vendor ACV. (5) Pricing volatility from unbounded foundation-model passthrough.

**Review cycle.** RFP/bake-off 6–16 weeks; commercial negotiation 4–10 weeks; references 1–3 weeks. **Total: 10–24 weeks**, often parallel with Legal and InfoSec.

**Artifacts.** Pricing with multi-year ramp; 3–5 named at-scale in-industry references; financial viability (audited financials, capitalization, runway); order form; SLA exhibit; competitive benchmarking data; exit-and-portability section; minimum-commit and true-up structure.

**New AI-specific concerns.** Foundation-model passthrough margin and exposure to model-price increases; trajectory cost variance (per-trajectory pricing is unmodellable if trajectories vary 10x in tokens — buyers want per-trajectory ceilings or per-tenant budgets); outcome-based pricing legitimacy (Sierra-style "pay on resolved case" — attractive but attribution is contested; Bret Taylor's thesis pressure-tested across CX, migrating to legal, finance, CS); AI vendor viability through shakeout (11x's quality-ceiling concession and Hayden Sukkar's public ARR-and-churn disclosures taught Procurement that AI-agent revenue does not predict survival); total cost including buyer's own compute, observability, and trajectory storage — often 30–60% on top of vendor invoice.

**Escalation/blockers.** Escalates to CFO. Overridden when sponsor has CFO/CEO air-cover for strategic spend. Rarely overridden on viability or on pricing-unbenchmarkable concerns.

**Three questions in 2026.**
1. *"Model your pricing three years out at our projected usage, stress-tested for foundation-model price increases of 20% and a usage spike of 3x. What is the cap, what is the renegotiation trigger."*
2. *"Three at-scale references in our industry. I will call them. I will ask what they would change about the contract."*
3. *"What does my exit look like on day 1, 30, 90, 365? Where is my data, my agent state, what is the migration cost."*

**Vendor tactical guide.** Publish transparent benchmarkable pricing (resolved cases or completed trajectories with SLA, not raw tokens). Offer usage caps. Offer foundation-model pass-through transparency. Bring three references willing to take a call. Document the exit story in the MSA up front.

---

## 6. Business Sponsor (CRO / CMO / VP CS / business-line owner)

**Who.** The executive who actually wants the tool — CRO for sales agents, CMO for marketing, VP CS for support, CFO for finance ops, CHRO for HR, Chief Legal Ops for legal-tech. The vendor's internal champion and the seller's true customer. Reports to CEO or board on deployment outcomes.

**What they evaluate.** Will it hit my number; how fast to value; change-management cost; team adoption; operator-translation cost (line manager translating between agent and human team); vendor-roadmap alignment.

**What they will reject for.** (1) TTM over 90 days (sponsors have quarterly P&L pressure). (2) Operator-translation gap unaddressed — vendor pitches the line manager but ships the cockpit UI for the engineer. (3) Outcome attribution that feels dishonest — "we resolved X cases" with vendor-defined resolution criteria, post-11x. (4) No co-marketing or case-study leverage. (5) Roadmap divergence from sponsor strategy.

**Review cycle.** Sponsor engagement is fast — **2–6 weeks** intro to internal champion. The sponsor then carries the deal across the other six counterparties (where time-in-queue lives).

**Artifacts.** Product demo (with sponsor data if possible); in-vertical/in-function case studies; implementation timeline; success-metrics framework; reference calls.

**New AI-specific concerns.** Reputational risk from agent error (sales agent mis-sending to the CEO of a top-10 customer is a career risk for the CRO); internal political optics of replacing seats with agents (CHROs, CMOs, CROs sensitive to "AI replaces humans" framing — want augment-not-replace talk-tracks); outcome attribution under board scrutiny; operator-translation cost; quarterly model-quality drift (deployed in Q1, performance shifted in Q3).

**Escalation/blockers.** Escalates to CEO. Rarely blocked except on hard regulatory or security floors. When blocked, sponsor either drops, escalates for CEO override, or negotiates smaller scope.

**Three questions in 2026.**
1. *"What did the last three customers at my scale do in their first 90 days, measurable outcome at day 90."*
2. *"My line manager runs this day-to-day. Show me their week."*
3. *"When the model drifts or the agent acts wrong, who calls me, when, what is the playbook."*

**Vendor tactical guide.** Run a 30-day paid pilot with a defined success metric. Bring two reference sponsors on a peer call. Map the operator-translation surface — line manager UI, workflow, escalation path. Co-author the case study before signing.

---

## 7. Enterprise Architecture / IT Ops (CIO / Chief Architect / Head of Platform)

**Who.** CIO reports to CEO at ~70% of F1000, COO at ~20%, CFO at ~10%. Below: Chief Architect (reference architecture, technology radar), Head of Platform Engineering / IT Ops (run-the-business, on-call, capacity), Head of Integration (SaaS-to-SaaS plumbing), and an **AI Platform Engineering** team (LLM gateway, eval/obs, vector store, agent runtime — the Volume III stack).

**What they evaluate.** Reference-architecture fit; integration with identity, observability, secrets, deployment, change management; operability footprint (runbook, dashboards, alerts, cost telemetry); capacity (concurrency, throughput, sub-agent fan-out); failure modes (graceful degradation, circuit breakers); multi-region/multi-cloud/multi-tenancy.

**What they will reject for.** (1) Non-conformant to reference architecture — vendor demands a private VPC peer when SAML/OIDC suffices; can't ship logs to buyer's observability pipeline; bespoke identity. (2) Unbounded sub-agent fan-out without circuit breaker — an agent spawning 100 sub-agents on one trigger is a DoS risk against downstream systems. (3) No per-trajectory cost telemetry (EA cannot govern what it cannot see). (4) OAuth blast radius unbounded — "read all email, all calendar, all files" when the agent's purpose justifies narrow scope. (5) No runbook, no RTO/RPO, no failure-mode design.

**Review cycle.** **4–10 weeks**, often parallel with InfoSec. Longer if integration design requires new reference-architecture exceptions.

**Artifacts.** Architecture diagram with trust boundaries; integration design (identity, obs, secrets, deployment); operability runbook; capacity-and-concurrency benchmarks; cost-telemetry data model; multi-region design; failure-mode catalog with circuit breakers; OAuth scope inventory with least-privilege justification.

**New AI-specific concerns.** Foundation-model dependency in reference architecture (where model runs, who pays, what contingency); per-trajectory cost variance vs. predictable per-API-call SaaS; OAuth-blast-radius governance; trajectory observability through buyer's OpenTelemetry pipeline (OpenTelemetry GenAI conventions matured 2024–2025 and are table-stakes at F1000); sub-agent privilege separation (when an agent spawns a sub-agent, what tools and credentials does it inherit, what does the identity fabric see).

**Escalation/blockers.** Escalates to CEO or COO. Rarely overridden on reference-architecture conformance or operability.

**Three questions in 2026.**
1. *"Reference-architecture fit. Identity, observability, secrets, deployment, multi-region. Here is our published architecture — tell me where you don't fit."*
2. *"Sub-agent fan-out behavior under failure. What is the circuit breaker, the cost ceiling per trajectory, what does my SIEM see."*
3. *"Per-trajectory cost telemetry. Show me the data model and the export."*

**Vendor tactical guide.** Ship OpenTelemetry GenAI conventions native. Expose per-trajectory cost metering. Document OAuth scopes per tool with least-privilege justification. Publish a reference architecture with buyer's-VPC as a first-class tier. Bring the Solutions Architect to the EA meeting.

---

## 8. The Fourteen AI-Specific Contractual Addenda (May 2026)

The post-2024 hardening of the F1000 buyer-side AI template. Each has a precedent, an owner, vendor response patterns, and risk-if-refused.

**1. Training-data rights — no training on customer data.** *"Vendor shall not use Customer Data, including prompts, completions, embeddings, or any derivative thereof, to train, fine-tune, or improve any Vendor or third-party model, without Customer's prior written consent on a per-use-case basis."* **Drove it:** Bartz v. Anthropic (Aug 2024); Tremblay v. OpenAI (June 2024); consolidated authors' suits. **Owner:** Legal + Privacy. **Patterns:** Compliant at OpenAI Enterprise, Anthropic, AWS Bedrock; negotiated at smaller vendors; refused at data-monetizing vendors. **Risk if refused:** Deal-killer at F1000.

**2. Output ownership clarity.** *"As between the parties, Customer owns all Outputs generated by the Service in response to Customer prompts and Customer Data, subject to Vendor's underlying IP in the Service itself."* **Drove it:** Getty v. Stability AI (2023–2025); music-industry suits. **Owner:** Legal (IP). **Patterns:** Compliant at every credible enterprise vendor. **Risk if refused:** Deal-killer.

**3. Model-update notification and pinning rights.** *"Vendor shall provide no less than thirty (30) days advance notice of any material change to the underlying foundation model. Customer shall have the right to pin to the prior model version for not less than ninety (90) days."* **Drove it:** GPT-4 to GPT-4-Turbo behavior drift (2023–2024); Claude 3.5→3.6→3.7 sequence (2024–2025); Anthropic April 2025 RSP-driven Sonnet update. **Owner:** Legal + AI Council. **Patterns:** Increasingly compliant; resistance from vendors fully dependent on a single lab. **Risk if refused:** Hard reject from AI Council in regulated industries.

**4. Hallucination indemnity caps and carve-outs.** *"Vendor shall indemnify Customer for damages from materially inaccurate Outputs reasonably relied upon in production, capped at [2x ARR]. This indemnity shall not be subject to the general liability cap."* **Drove it:** *Moffatt v. Air Canada* (Feb 2024). **Owner:** Legal. **Patterns:** Negotiated — landing zone 1–2x ARR carve-out separate from general cap, with exclusions for misuse. **Risk if refused:** GC blocks; deal renegotiated at smaller scope.

**5. Agent-action liability allocation.** *"For Outputs that constitute autonomous actions taken by the Service on systems or data outside the Service's tenancy (including email, transactions, system modifications, external API calls), Vendor's indemnity shall extend to [N]x ARR, separately capped."* **Drove it:** Sierra and Decagon production deployments (2024–2026); autonomous-agent incidents (mass-mailer over-sends, refund cascades reported 2025). **Owner:** Legal + InfoSec. **Patterns:** Negotiated; vendors push back on "autonomous" definition. **Risk if refused:** Deal-killer for high-autonomy use-cases.

**6. Sub-processor consent for foundation-model providers.** *"Vendor shall maintain a current list of all sub-processors, including foundation-model providers, identifying data flows. Vendor shall provide thirty (30) days' notice of material changes, and Customer shall have the right to object."* **Drove it:** Schrems II (2020) and ongoing US-EU data-flow contestation; Italian Garante's ChatGPT order (March 2023). **Owner:** Privacy + Legal. **Patterns:** Compliant by default; contested element is right-to-object. **Risk if refused:** Deal-killer.

**7. Kill-switch and immediate-shutdown rights.** *"Customer shall have the right to immediately disable the Service, or any specific agent, tool, or capability thereof, via a defined interface available 24/7, with no remediation period or vendor consent required."* **Drove it:** Microsoft Tay (2016, the original); Bing chatbot (Feb 2023); Air Canada (2024). **Owner:** InfoSec + EA. **Patterns:** Compliant — "defined interface" detail varies. **Risk if refused:** Deal-killer.

**8. Eval-report sharing on a defined cadence.** *"Vendor shall deliver, on a quarterly basis, an Evaluation Report covering performance on a defined set of agent tasks, including methodology, dataset hash, model pin, harness version, and signed attestation."* **Drove it:** AI Council formalization (2024–2025); NIST AI RMF GenAI Profile (July 2024); the procurement-readiness gap. **Owner:** AI Council. **Patterns:** Few vendors ship turnkey today; emerging at Anthropic and partial at OpenAI Enterprise. **Risk if refused:** Council blocks for high-risk use-cases. **(The Bet #1 wedge.)**

**9. Red-team frequency and reporting.** *"Vendor shall conduct adaptive-adversary red-teaming no less than annually, and following any material model update, and shall share methodology, scope, findings, and remediation."* **Drove it:** EU AI Act (2024); NIST AI RMF GenAI Profile; Microsoft Copilot Studio prompt-injection demos (Black Hat 2024). **Owner:** AI Council + InfoSec. **Patterns:** Anthropic and OpenAI ship summaries; most vertical agents do not. **Risk if refused:** Council blocks for regulated use-cases.

**10. Indirect-prompt-injection defense attestation.** *"Vendor shall maintain an annual attestation of defenses against indirect prompt injection, including threat model, mitigation design, and test results against a published adversarial test suite."* **Drove it:** Copilot Studio demos (2024); EchoLeak class disclosures (2025). **Owner:** InfoSec. **Patterns:** Few ship turnkey; emerging. **Risk if refused:** InfoSec blocks for any agent ingesting external content.

**11. EU AI Act Article 14 human-oversight conformance.** *"For any deployment that constitutes a 'high-risk AI system' under EU AI Act Annex III as applied to Customer's use-case, Vendor shall provide documentation supporting human-oversight conformance under Article 14, including oversight-design specification, operator-training materials, and a Fundamental Rights Impact Assessment template."* **Drove it:** EU AI Act passage (March 2024); enforcement window August 2026; April 2026 draft enforcement guidance. **Owner:** AI Council + Legal + Privacy. **Patterns:** Rare compliant — **the Bet #1 wedge**. **Risk if refused:** Deal-killer in EU-exposed F1000 from August 2026.

**12. Data residency for inference (region-pinning).** *"Vendor shall provide an option for inference to be processed exclusively within [EU / US / specified region], including all foundation-model calls, prompt retention, and output retention, with annual attestation."* **Drove it:** Schrems II; DPF contestation; Italian Garante; sovereign-cloud demands from EU governments and financial regulators. **Owner:** Privacy + EA. **Patterns:** Compliant at AWS Bedrock, Azure OpenAI; rare at vertical-agent vendors. **Risk if refused:** Deal-killer in EU and regulated US.

**13. Audit-log retention and customer access.** *"Vendor shall maintain tamper-evident audit logs of all agent trajectories, tool invocations, and Outputs for [seven (7) years], and shall provide Customer continuous read-access via a defined interface, in a format suitable for Customer's SIEM."* **Drove it:** SR 11-7 (Fed Reserve model risk management, 2011, applied by analogy to AI agents); SOX; HIPAA Security Rule; FINRA Rule 4511; post-CrowdStrike (July 2024) elevation of observability as a board-level concern. **Owner:** InfoSec + GRC + Legal. **Patterns:** Compliant for log generation; contested on retention and tamper-evidence. **Risk if refused:** Deal-killer in regulated industries.

**14. Sub-agent privilege-separation attestation.** *"For deployments involving sub-agents, Vendor shall attest to the privilege-separation design, including least privilege applied to sub-agent tool access, credential inheritance, and cross-tenant isolation, with annual review."* **Drove it:** 2024–2025 pattern of agent fan-out incidents in production; Anthropic/OpenAI/Google sub-agent risk publications. **Owner:** InfoSec + EA + AI Council. **Patterns:** Rare turnkey; emerging at Anthropic. **Risk if refused:** AI Council and InfoSec block.

---

## 9. Sectoral Overlays

**Financial Services (NYDFS Part 500, SR 11-7, OCC model-risk guidance, FINRA, EU DORA).** Adds: SR 11-7-style model validation evidence; independent model-validation report; NYDFS 23 NYCRR 500 attestation; FINRA Rule 4511 audit-log retention floors; DORA-aligned operational resilience for EU FSI; AML/sanctions-screening attestation if the agent touches onboarding. The **model-risk function** (reports to Chief Risk Officer, distinct from CISO) is a de facto eighth counterparty in FSI. **Add 8–16 weeks.**

**Healthcare (HIPAA, HITECH, ONC HTI-2 predictive-decision rules, OCR enforcement, FDA SaMD).** Adds: BAA at signature; HIPAA Security Rule attestation; OCR-aligned breach-notification procedures; if the agent makes clinical decisions, FDA Software-as-Medical-Device pathway (typically 510(k) or De Novo); for predictive decision support, ONC HTI-2 transparency rules effective 2026; bias audit specific to clinical disparities. **Add 6–14 weeks.**

**Defense / Government (FedRAMP Moderate/High, DoD IL4/IL5/IL6, CMMC, ITAR/EAR).** Adds: FedRAMP authorization in the relevant boundary; ATO from the sponsor agency; CMMC Level 2 or 3 for defense contractors; ITAR/EAR export controls applied to the model itself (relevant for any agent crossing dual-use thresholds under the October 2023 EO and January 2025 EO); sponsor-agency risk acceptance for emerging-tech use-cases. **Total cycle 6–18 months end-to-end**; FedRAMP authorization alone is 12–18 months from start.

---

## 10. The Honest Bottom Line

Six counterparties, seven at F1000. Sequential and parallel review. **Calendar-time floor: 16–24 weeks** at F1000 for an agent vendor that has its act together; 32–52 weeks for one that does not; 12–24 months for regulated sectors. The fourteen AI-specific addenda are not margin negotiating positions — they are the modern buyer-side template, and the vendor that ships compliant by default closes faster and at higher ACV than the vendor that fights every clause.

The procurement-readiness gap is not that buyers do not know what to ask. It is that no canonical source compiles the questions in agent-specific form. The seven counterparty chapters and the fourteen addenda above are the most-actionable artifact a CIO or CISO can lift directly into their next AI vendor review. That is the load-bearing claim, and the spine of Bet #1.
