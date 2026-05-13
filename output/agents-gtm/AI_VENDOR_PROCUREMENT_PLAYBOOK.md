# The AI Vendor Procurement Playbook

**How the Fortune 1000 Should Buy AI Agents in 2026**

*Author: Alex Yedi*
*Date: May 2026*
*Edition: v1.0*

---

## Section I · Executive Foreword

If you are a CIO, you are reading this because the AI agents your business sponsors are buying do not pass any of the procurement controls you built between 2014 and 2023. The SOC 2 your vendor proudly references covers their cloud posture. It does not cover the agent's tool-boundary policy. The DPA you signed in 2022 contemplates a vendor processing your data. It does not contemplate a vendor's agent writing into your system of record, taking an irreversible action, and being unable to roll it back. You are reading this because between the AI council you set up in 2024 and the vertical-agent vendor your CFO wants to sign next quarter, there is a gap that nobody in your organization is currently equipped to close. This Playbook closes it.

If you are a CISO, you are reading this because every red-team result a vendor has shown you is run against a public corpus and you cannot tell whether the 99% indirect-prompt-injection detection rate they cite is meaningful or marketing. It is marketing. The adaptive-adversary numbers, when vendors are willing to disclose them, sit between 60% and 80% — and even those are unstable across model versions. You are reading this because Bartz v. Anthropic (the May 2024 fair-use dismissal, the September 2024 reversal, the $1.5B class-settlement framework that crystallized through 2025) and the NYT v. OpenAI proceedings have already re-priced what training-rights and output-ownership clauses cost in dollar terms, and your peers are missing the analogous re-pricing happening on agent-action liability. This Playbook is how you stop missing it.

If you are an AI Council Chair, you are reading this because the EU AI Act Article 14 human-oversight implementation guidance went to draft in April 2026 and your General Counsel is asking you what it means for the sixty-two AI tools in flight across the business. The honest answer is that for most of those tools — the embedded copilots, the document QA assistants, the retrieval layers — Article 14 changes almost nothing. For the agents that take actions on your behalf, it changes the shape of every contract you have not yet signed. You are reading this because you need a way to separate the two and to write the second into your AI policy without having to re-read the Act twice a week.

If you are a Chief Procurement Officer, you are reading this because the cycle time from security questionnaire to AI Governance sign-off is now the single longest variable in your AI vendor close-time, your business sponsors are bypassing you when they can, and Vanta's AI Trust Center is good for compliance posture but does not substitute for the seven overlays. You need a standard that compresses cycle time without compressing rigor. The Playbook is that standard.

If you are a General Counsel, you are reading this because Air Canada (February 2024) established that a chatbot's output binds the company contractually. Colorado's AI Act (May 2024) established personal-injury exposure for high-risk AI decisions. The Bartz settlement framework established that training-data exposure is measured in billions. None of these reshape your existing vendor template. All three reshape the one you are about to sign with Sierra, Decagon, Glean, Harvey, Hippocratic, Augment, Hebbia, or Rogo. You are reading this because the fourteen addenda in Part IV are what you should be inserting into your MSA template before the next vertical-agent renewal.

If you are a Chief Architect or Head of Enterprise Architecture, you are reading this because the cloud bill from your AI portfolio went non-linear in Q4 2025, your reference architecture does not have an agent-runtime tier, and the OAuth scopes the new vertical-agent vendors are asking for would have been rejected on sight in any non-AI procurement review you have ever run. You are reading this because the agent layer broke the assumption your reference architecture was built on — that vendors call APIs and humans take actions — and the fan-out from a single agent invocation against a misconfigured sub-processor can cost more than your entire 2025 LLM gateway budget in a weekend. The Enterprise Architecture chair is the seventh counterparty in this Playbook, and at F1000 scale it is a distinct sign-off with its own queue and veto. The CIO who treats EA as a sub-function of InfoSec is the CIO who finds out in Q3 2026 that the agent fleet has no per-trajectory cost telemetry, no circuit breakers on sub-agent fan-out, and no published OpenTelemetry GenAI conformance — three problems that should have been caught in Branch 1 of the decision tree, not in the post-mortem.

This Playbook exists because no incumbent — not Vanta, not Drata, not Secureframe, not OneTrust, not the Big Four — currently ships a canonical, buyer-side, agent-specific procurement standard. There is a Wardley map of the AI agent stack on my desk that places every layer beneath the runtime (sandboxes, browsers, gateways, telephony, TTS) on a clean 24-month commoditization path and every layer above the runtime (eval, observability, guardrails, vertical workflow, procurement controls) at Custom-to-Genesis. Buyer-side procurement controls are the only piece of the picture sitting at Genesis with no flag planted in it. The window to plant the flag is the window before EU AI Act Article 14 enforcement starts in late 2026 and before Anthropic's ARR resolves at $24B or $30B in Q3 2026 and re-prices the entire vertical-agent valuation stack.

Read it in this order. If you are a CIO or AI Council Chair, start with Section V (Decision Tree). If you are a CISO, start with Section III (Seven Overlays). If you are a CPO, start with Section VI (Scoring Rubric) and Section II (Seven Counterparties). If you are a GC, start with Section IV (Fourteen Addenda) and Section III.6 (Article 14 Tie-Out). If you are a Chief Architect, start with Section II.7 (Enterprise Architecture) and Section III.4 (Sub-Agent Privilege Separation). The Glossary in Section VII is short because it has to be — you should be able to read every term twice and use them in a vendor call the same week.

The position this Playbook takes throughout is that agent procurement is not a more permissive SaaS procurement; it is a stricter one with new questions. Vendors will tell you the old questions still work with minor additions. They do not. The seven overlays are not nice-to-haves. They are the questions that separate agent vendors who can survive a regulator subpoena and a class action from agent vendors who will fold the first time a write action runs against the wrong row and a customer sues. Treat them that way.

A note on what this Playbook is not. It is not a neutral white paper. It takes positions. Vanta's AI Trust Center is good for posture, not for the seven overlays. Drata's ISO 42001 readiness mapping is useful for AI Council documentation, not for an Article 14 tie-out. The Big Four AI risk frameworks are competent on theory and weak on the named-vendor reads buyers actually need before signing a contract this quarter. The vertical-agent leaders — Sierra, Decagon, Glean, Harvey, Hippocratic, Hebbia, Rogo — are named and graded. The synthetic-SDR category is named as a cautionary pattern. The horizontal incumbents (OpenAI, Anthropic, Google) are graded on what their enterprise contracts actually contain in May 2026, not on what their marketing claims. If you wanted neutrality, you would buy a Gartner subscription. This is the artifact you read when you have already bought the Gartner subscription and it is not closing the gap.

---

## Section II · The Seven Counterparties

Every F1000 AI-agent procurement runs through seven chairs. The standard "six approver" model under-counts at F1000 specifically — the seventh, Enterprise Architecture / IT Ops, folds into InfoSec or Procurement at sub-$10B but at F1000 scale is a distinct sign-off with its own queue and its own veto. EA owns the cloud bill (unbounded trajectory cost is an EA problem, not an InfoSec one). It owns the reference architecture (vendors that demand non-conformant identity, observability, or runtime get blocked here). It owns the identity fabric and the OAuth blast radius. It owns on-call and operability. It owns capacity. Treat it as the seventh chair from day one or you will discover it as the eighth-week blocker.

The seven chairs sit in this order: InfoSec, Legal, Privacy, AI Governance Council, Procurement, Business Sponsor, Enterprise Architecture. Each chapter that follows carries the same nine attributes — who they are, what they evaluate, what they reject for, review-cycle duration, artifacts required, new AI-specific concerns, escalation and blocker dynamics, three verbatim 2026 questions, and a vendor tactical guide. Read the chapter that owns your chair first. Then read the chair sitting next to you in the deal — the one whose turn comes next, the one whose veto kills your timeline if you missed it.

A framing instruction for every chapter that follows. *If you are this counterparty, this chapter is for you. If you are the vendor selling to them, this is what they will not say but always think.*

---

### Chapter II.1 — InfoSec (CISO / Security Architecture / GRC)

If you are the CISO, this chapter is your seat at the table. If you are the vendor selling to them, this chapter is the silent question every Security Architect is grading you on while the AE is talking.

**Who they are.** The CISO reports to the CIO at roughly 55% of F1000, to the CEO at 25%, and to the CRO, CFO, or GC at the remaining 20% — the post-Yahoo, post-Uber, post-SolarWinds independent-CISO pattern that hardened through the late 2010s and never reversed. For agent procurement specifically, the load-bearing seat is not the CISO themselves but Security Architecture. They decide whether the proposed architecture is acceptable in principle before GRC ever processes the questionnaire paperwork. A vendor who wins the architecture review wins the InfoSec lane in fewer cycles than the vendor who wins the questionnaire.

**What they actually evaluate.** Not "is the vendor SOC 2." SOC 2 is the floor and every credible vendor clears it. The agent-era questions are: what is the trust boundary between vendor runtime and our data plane; what tools, MCP servers, and APIs can the agent invoke, on whose authority, with what credentials; what is the blast radius if a prompt injection succeeds; what is the rollback story for wrong actions; what does the tamper-evident trajectory log look like and can it be exported into our SIEM; can the vendor run in our VPC, our tenancy, with our customer-managed keys; and what is the foundation-model dependency chain underneath all of it. Every one of these questions is new since 2022. None of them are answered by a clean SOC 2.

**What they will reject for.** Five hard lines as of May 2026. First, unbounded tool scope with no documented tool-boundary policy. Second, no tamper-evident audit log meeting the buyer's 1-to-7-year retention floor. Third, shared-tenancy inference for regulated data. Fourth, no documented indirect-prompt-injection defense — post-Microsoft Copilot Studio prompt-injection demonstrations at Black Hat 2024 and the EchoLeak class disclosures of 2025, this is not a soft question any more. Fifth, the vendor cannot answer "what happens if your foundation-model provider has an outage, an update, or a vulnerability." Every CISO in the F1000 lives in the shadow of CrowdStrike (July 2024); none of them are signing for an agent vendor whose answer to a foundation-model supply-chain disruption is "we'll figure it out."

**Review cycle.** Questionnaire turnaround sits at 4–8 weeks. Architecture review at 2–6 weeks. Pen-test review at 4–12 weeks, and longer when the buyer's testing partner has not previously assessed an agent runtime of this shape. Total time-in-queue for InfoSec at F1000 in 2026: **10–20 weeks**, with the upper bound applying to FSI and healthcare buyers. Vendors who model their close cycles on a 6-week SOC 2 review are pricing in a fiction.

**Artifacts required.** The legacy stack — SOC 2 Type II current and unqualified, ISO 27001 if EU-exposed, completed SIG / CAIQ / HECVAT, third-party pen-test conducted within the last 12 months — is necessary but no longer sufficient. The AI-specific stack adds: model card, signed eval report, red-team report (with adaptive-adversary methodology named), indirect-prompt-injection attestation, tool-boundary policy document, sub-agent privilege model, kill-switch documentation, sub-processor list with foundation-model providers explicitly named, and a foundation-model fallback plan. The vendor that ships seven of these nine artifacts in the Trust Center on day one closes the InfoSec lane in 8 weeks. The vendor that ships three of nine closes in 18.

**New AI-specific concerns.** Indirect prompt injection from data ingested through tools, documents, retrieved context, or MCP server returns. Tool-boundary enforcement at runtime, not at config time — the difference between a vendor who has thought about this and a vendor who has not is whether the enforcement survives a redeploy. Sub-agent privilege escalation in multi-agent architectures. Foundation-model supply chain risk: deprecation, drift, outage, and the security-vulnerability disclosure pattern when the underlying lab issues a CVE. Trajectory log integrity — a log a determined adversary can rewrite is not an audit log.

**Escalation and blocker dynamics.** The CISO escalates to the CIO, the CRO, or the board risk committee. Override pathways exist when a business sponsor has explicit CEO air-cover for a strategic gap (Sierra into CX, Harvey into a top-tier law firm) or when the GC has accepted contractual risk transfer in writing. Override is rare and effectively unavailable on FedRAMP, HIPAA, and FFIEC floors — those are statutory, not negotiable.

**Three questions a CISO will ask in 2026, verbatim.**

1. *"Walk me through your tool-boundary policy. What can your agent call, on whose authority, enforced at runtime — not config time."*
2. *"Show me your indirect-prompt-injection defense — adaptive-adversary red-team report, not a benchmark — and the refresh cadence."*
3. *"If your foundation-model provider issues a model update tomorrow, what happens to our deployment, what notice do we get, and what is our right to pin and to test."*

**Vendor tactical guide.** Ship a Trust Center that contains: completed CAIQ, completed SIG, current model card, signed reproducible eval report, red-team summary with named methodology, prompt-injection attestation, sub-processor list with foundation-model providers named, and a one-page architecture diagram with the trust boundary explicit. Date everything. Volunteer buyer's-VPC deployment as a first-class tier in the first conversation, not the third. Bring a security engineer to the second meeting. Do not lead with the GRC team — Security Architecture wants to talk to an engineer who can answer "how does the executor sub-agent get its credentials" without consulting a slide.

---

### Chapter II.2 — Legal (GC / Commercial Counsel / IP)

If you are the GC, this chapter is your seat. If you are the vendor selling to them, this chapter is the redline you cannot bluff your way through and the indemnity stack the AE was hoping you would not ask about.

**Who they are.** The GC reports to the CEO and to the board's audit or governance committee. Below the GC sit Commercial Counsel (who run the MSA, DPA, and order form), IP Counsel (who run training-data and output-ownership posture), and Litigation Counsel (who run indemnity, liability, and the agent-action carve-outs). The seat that did not exist in 2022 and is now standard at F1000 is **AI-dedicated counsel** — often a senior Commercial Counsel cross-trained on the AI act stack, or a hire from the AI practice groups at Cooley, Wilson Sonsini, Latham, or Morrison Foerster. If you are a vendor and your buyer's GC has hired AI-dedicated counsel, the redlines you receive will be denser, the indemnity asks will be sharper, and the cycle will be longer. That is correct behavior on the buyer side.

**What they evaluate.** Liability allocation for both agent actions and agent outputs (these are different categories and the modern template treats them separately). Ownership of inputs, outputs, and any derived data. Indemnity scope across hallucination, IP infringement, and third-party-content exposure. Audit, pause, and terminate rights. Exit and data-portability obligations. Sub-processor visibility, with the foundation-model provider named explicitly. Insurance floors, including AI-specific tower coverage above a $1M ARR threshold. And the agent-specific carve-outs — the line items that did not appear in any 2022 vendor template and now appear in every credible 2026 one.

**What they will reject for.** Five hard lines, each with a precedent. First, hallucination liability disclaimed entirely — post-*Moffatt v. Air Canada* (BC CRT, February 2024), the "the chatbot is a separate legal entity" theory is the bad case study every GC cites; they want the vendor on the hook. Second, output-ownership ambiguity or vendor refusal to disclaim training rights — post-Bartz v. Anthropic (the August 2024 ruling and the $1.5B class-settlement framework that crystallized through 2025) and the consolidated NYT v. OpenAI / Microsoft litigation. Third, indemnity caps below the AI-specific floor: a $1M aggregate cap on $250K ARR was acceptable in 2022; in 2026 AI indemnity needs at least 2x ARR with separate carve-outs for hallucination, IP, and agent-action exposure. Fourth, no model-change notification — post the GPT-4 to GPT-4-Turbo behavior drift episode and the Claude 3.5 → 3.6 → 3.7 sequence, every credible GC wants 30-to-90-day notice and a pinning right. Fifth, the foundation-model sub-processor is not disclosed — the DPA fails Privacy review, and the contract fails Legal review for the same reason.

**Review cycle.** First redline at 2–4 weeks. Negotiation rounds at 2–5, against the 1–2 you would expect for traditional SaaS. Total time-in-queue for Legal at F1000 in 2026: **8–16 weeks**. The vendor whose AE promises the GC will sign in two weeks is the vendor who has not actually been through an F1000 AI legal review.

**Artifacts required.** Master Services Agreement, Data Processing Addendum, AI Addendum (the 2024–2026 hardening documented in Section IV), Business Associate Agreement if PHI is in scope, sub-processor list with foundation-model providers named, insurance certificates (E&O, cyber, and an AI-specific tower if ARR exceeds $1M), indemnity-backing evidence, the order form, the SLA exhibit, and third-party content licenses (post-NYT v. OpenAI). The vendor who arrives at the legal review with these artifacts pre-staged closes legal in 8 weeks. The vendor who treats each as a custom redline closes in 16, and signals to the GC that they have not done this before.

**New AI-specific concerns.** Agent-action liability — autonomous email send, autonomous ticket close, autonomous refund issued, autonomous return processed — distinct from hallucination liability and demanding its own indemnity carve-out. Training-data provenance, with documented chain-of-custody back to the underlying corpus. Output ownership and derivative-work risk in the wake of Getty v. Stability AI (2023–2025) and the music-industry suits. Model-update notice and pinning rights. Termination and exit-data rights covering persistent agent memory, trajectory logs, and any fine-tuned adapters trained on the buyer's data.

**Escalation and blocker dynamics.** The GC escalates to the CEO or to the board audit committee. Override pathways exist when the sponsor has explicit board air-cover, when the deal is below the GC escalation floor (typically $250K–$1M ARR), or when Procurement and InfoSec have already cleared and Legal is the last gate at quarter-end. Override is rare and effectively unavailable on indemnity floors or sub-processor disclosure — both are board-reported risk lines.

**Three questions a GC will ask in 2026, verbatim.**

1. *"Walk me through your indemnity stack. Cap on IP infringement, cap on hallucination, cap on agent action, and the insurance tower backing it."*
2. *"Show me the AI Addendum. Training-data carve-out, model-update notice, output ownership, kill-switch rights, termination-data rights."*
3. *"Who is your foundation-model sub-processor, and your contingency if their terms change against you mid-contract."*

**Vendor tactical guide.** Publish a public AI Addendum with buyer-favorable defaults pre-baked: no training on customer data, output ownership to customer, model-update notice with pinning rights, foundation-model providers named, indemnity stack disclosed in tabular form. Pre-clear a BAA if you sell into healthcare. Volunteer insurance-tower disclosure before the GC asks. Do not redline standard EU SCCs out of the customer's DPA — that signals you are not EU-ready and the GC will read it as exactly that. Do not negotiate hallucination indemnity to zero; the modern landing zone is 1–2x ARR carve-out separate from the general cap, and a vendor who fights this signals they intend to leave the buyer holding the Air Canada bag.

---

### Chapter II.3 — Privacy (CPO / DPO / Privacy Counsel)

If you are the CPO or the DPO, this chapter is your seat. If you are the vendor selling to them, this chapter is the contextual-integrity question your AE has never been asked and the surgical-deletion SLA your engineering team has never been asked to commit to.

**Who they are.** The CPO reports to the GC at roughly 60% of F1000, to the CISO at 20%, and to the CEO or CRO at 20%. The DPO is statutorily required for any organization processing EU personal data at scale (GDPR Article 37) and has independent statutory protection that no F1000 GC can override. Below the CPO sit Privacy Counsel (DPIA, cross-border transfers), Privacy Engineering (consent, data-subject-rights tooling, deletion mechanisms), and AI Ethics seats embedded either in privacy or on the AI Council.

**What they evaluate.** What personal data does the agent ingest, with what lawful basis, retained for how long, processed in which jurisdictions. What is the controller / processor split. What is the data-subject-rights story across access, deletion, portability, and Article 22 objection. What is the cross-border transfer mechanism — Standard Contractual Clauses, an adequacy decision, or the EU-US Data Privacy Framework. Does the agent make automated decisions about EU subjects under Article 22 (or about California subjects under the November 2025 ADMT rule). Is special-category data under GDPR Article 9 in scope, and on what documented basis. Is the DPIA done, and does it name agent-specific risks. For agents specifically, the new lens is **contextual integrity** in the Helen Nissenbaum sense — does data collected in the sales context end up routed through an HR or compliance workflow, and is the data subject's reasonable expectation honored across the agent's tool surface.

**What they will reject for.** Five hard lines. First, no DPIA or one that does not name agent-specific risks (persistent memory, indirect injection, sub-agent privilege, foundation-model training-set exposure). Second, cross-border transfer with no clean Schrems II-compliant mechanism. Third, training on EU personal data without lawful basis — the Italian Garante's ChatGPT order (March 2023) is the precedent and every European Privacy Counsel cites it. Fourth, no surgical-deletion mechanism for data-subject erasure across the agent's persistent memory, trajectory logs, and any fine-tuned weights, with completion within GDPR's 30-day clock. Fifth, special-category data routed through the agent without documented basis — health, biometric, sexual-orientation, political-opinion, religious data hitting the same agent runtime as ordinary customer-support data is a rejection signal, not a flag.

**Review cycle.** DPIA review at 3–6 weeks. Cross-border transfer review at 2–4 weeks. Total time-in-queue for Privacy at F1000 in 2026: **6–12 weeks**, with the upper bound applying to healthcare buyers, public-sector buyers, and EU-headquartered buyers who treat the DPO function with statutory weight.

**Artifacts required.** DPA with the buyer's preferred SCCs (do not negotiate the SCC text itself; negotiate the supplementary measures). A DPIA template completed for the buyer's specific use-case, not a generic vendor template. The sub-processor list with foundation-model providers named explicitly. A data-flow diagram showing what crosses which border. A retention schedule per data category. The data-subject-rights process documented, with a named SLA. Technical and Organizational Measures (TOMs) annex.

**New AI-specific concerns.** Persistent agent memory and the right to be forgotten — the question "where does the deletion request actually propagate, and within what window" did not exist in 2022 and is now load-bearing. Inference-time data leakage — the foundation-model provider sees the prompts; the prompts may leave the region; the prompts may be retained in vendor logs even if the foundation-model provider commits to no training. Contextual integrity across the agent's tool surface, with explicit attention to whether sales-channel data ends up in an HR-channel inference. Article 22 automated-decision-making conformance, and the parallel CCPA ADMT rule that became effective in November 2025. EU AI Act Article 14 human-oversight tie-out, which Privacy increasingly co-owns with the AI Council in F1000 organizations.

**Escalation and blocker dynamics.** The CPO escalates to the GC, to the board audit committee, or — for EU operations — to the DPO with independent statutory protection. Override is available only when residual risk is documented in writing and the DPO records objection. Override is effectively unavailable on Article 22 violations, on data-subject-rights gaps, or on special-category data routing.

**Three questions a CPO will ask in 2026, verbatim.**

1. *"Show me your data-flow diagram. Where does the prompt go, the output go, the memory persist, what borders does any of it cross."*
2. *"If a data subject asks us to delete their data, what is the surgical-deletion mechanism in your agent's memory and trajectory logs, and what is your SLA."*
3. *"For automated decisions about EU subjects, show me the human-in-the-loop and the Article 22 conformance documentation."*

**Vendor tactical guide.** Ship pre-completed DPIA templates per use-case (sales, support, HR, finance, legal) — do not make the buyer's Privacy Counsel write yours from scratch. Offer EU-only inference routing as a first-class deployment tier, with annual attestation. Document the surgical-deletion mechanism explicitly, with a per-component SLA: persistent memory in N hours, trajectory logs in N days, fine-tuned adapter weights on the next training cycle. Pre-publish the sub-processor list with 30-day notice rights and a documented objection procedure. Volunteer the Schrems II supplementary-measures analysis before the buyer asks for it. Do not pretend that "the foundation-model provider does not train on customer data" is the same answer as "the foundation-model provider does not retain prompts" — they are different commitments and Privacy Counsel will catch the substitution every time.

---

### Chapter II.4 — AI Governance Council (Chair / Chief AI Officer / cross-functional)

If you are the AI Council Chair, this chapter is your seat. If you are the vendor selling to them, this chapter is the slow-but-decisive gate that exists precisely to be slow and decisive, and the artifact set you will be asked for is longer than the one you are currently shipping.

**Who they are.** The newest counterparty, stood up at virtually every F1000 between 2023 and 2025 in response to a converging regulatory stack: the EU AI Act passage (March 2024), NIST AI RMF and the GenAI Profile (January 2023 and July 2024 respectively), the Biden Executive Order (October 2023) and Trump's superseding EO (January 2025), NYC Local Law 144 (effective July 2023), the Colorado AI Act (passed May 2024, effective February 2026), and the consolidating state-level AI legislation that accelerated through 2025. The Council chairs to a CTO, a CDO, a Chief AI Officer (a 2024–2025 role explosion), a COO, or a CRO depending on the organization. Membership: CISO, CPO, GC, the relevant business-line representative for the use-case under review, often an external advisor or an embedded ethics seat. The Council issues the internal AI Use Policy, maintains the approved-vendor list, and gates any new AI deployment above a defined risk threshold.

**What they evaluate.** Whether the vendor's risk profile fits the organization's AI Use Policy. Control mapping to NIST AI RMF and ISO 42001. Whether the deployment qualifies as "high-risk" under EU AI Act Annex III (HR, credit, education, law enforcement, critical infrastructure, biometrics, certain medical and product-safety contexts). Human-oversight effectiveness under Article 14 — not whether there is a human in the loop, but whether that human can effectively understand, monitor, interpret, intervene, and interrupt. FRIA (Fundamental Rights Impact Assessment) support if the deployment requires one. Bias testing methodology, freshness, and disclosed disparate-impact analysis. Model card and evaluation credibility. Misuse and dual-use pressure tests.

**What they will reject for.** Five hard lines. First, no evidence of NIST AI RMF or ISO 42001 conformity — these are the new floor and the AI Council will not pass a vendor who treats them as optional. Second, bias testing absent or stale; post NYC LL 144 and the Colorado AI Act, hiring and credit agents need annual disparate-impact analysis with the methodology disclosed. Third, theatrical human oversight — a "human in the loop" reviewing 1,000 decisions per hour at 200ms median dwell time is not effective oversight under any honest reading of Article 14, and the Council exists to call this out. Fourth, no FRIA for high-risk EU AI Act deployments — the April 2026 draft enforcement guidance makes this explicit and the August 2026 enforcement window forces compliance. Fifth, the vendor refuses to share evaluation methodology, dataset, and results in a re-runnable form — signed reproducible eval reports are the 2026 standard, no vendor ships them turnkey today, and the Council Chair who lets a vendor through without one is the Council Chair who will be explaining the gap to the board in Q1 2027.

**Review cycle.** The Council meets monthly or biweekly at most F1000 organizations. Intake-to-decision in routine cases: **6–14 weeks**. For high-risk EU AI Act deployments requiring a FRIA: **12–24 weeks**. The cross-functional design of the Council makes it inherently slow — every member has a separate calendar, a separate threshold for objection, and a separate set of artifacts they need to read before voting. This slowness is a feature. The vendor who pushes for accelerated Council review is the vendor who has not done one before.

**Artifacts required.** A real model card with substance — not marketing. An evaluation report, signed and reproducible preferred. A red-team report with methodology named (Lakera Red, Robust Intelligence, HiddenLayer, or a credible internal team with external attestation). NIST AI RMF GenAI Profile control mapping with control IDs and reproducible evidence. ISO 42001 mapping. A FRIA template the buyer can adapt for their specific use-case. Bias audit conformant to NYC LL 144 and Colorado AI Act methodology. Indirect-prompt-injection attestation. Article 14 human-oversight design document for the buyer's specific use-case. Sub-agent privilege-separation design. Trajectory observability surface — what the buyer can see, in what format, with what retention.

**New AI-specific concerns.** Foundation-model risk inherited from the underlying lab — Anthropic's Responsible Scaling Policy, OpenAI's Preparedness Framework, Google's Frontier Safety Framework — and how the vendor passes that through into their own deployment commitments. High-risk classification under EU AI Act Annex III for the buyer's specific use-case. Evaluation reproducibility and tamper-resistance: model pin, dataset hash, harness version, signed attestation, all of which must hold under the scrutiny a regulator subpoena will apply. Human-oversight effectiveness as a system property, not a UI feature. Cumulative portfolio risk across the buyer's full agent fleet — the Council looks at the marginal vendor against the existing portfolio, not in isolation.

**Escalation and blocker dynamics.** The Council escalates to the executive committee or board risk committee. Override is rare and effectively unavailable on FRIA gaps, on documented bias findings, or on Article 14 deficiencies. The Council exists to be the slow, decisive gate — it is overridden downward only when the sponsor brings the CEO in early and the CEO accepts written residual-risk acceptance.

**Three questions an AI Council Chair will ask in 2026, verbatim.**

1. *"Show me your evaluation report — signed, reproducible, with model pin, dataset hash, harness version, and methodology. Walk me through your red-team for indirect prompt injection."*
2. *"Map your controls to NIST AI RMF GenAI Profile and ISO 42001. If you have an EU AI Act conformity assessment, show it. If not, tell me when."*
3. *"Show me the human-oversight design for our use-case. Article 14 in practice. Not the marketing version."*

**Vendor tactical guide.** Publish a signed reproducible eval. Publish a real model card. Publish NIST AI RMF and ISO 42001 mappings with control IDs and reproducible evidence. Volunteer the FRIA template before the Council asks. Bring an AI Safety or AI Trust engineer to the Council meeting — not the AE, not the GRC analyst. Do not pretend a benchmark is an evaluation. Do not pretend a marketing summary is a red-team. Do not bring an Article 14 tie-out that consists of "the operator can see the agent's actions in the UI" — that is a UI feature, not a system property, and the Council will reject it. The vendor who closes Council fastest is the vendor who walks in with the artifact set already in place and lets the Council ask the third-order questions instead of forcing them to ask the first-order ones.

---

### Chapter II.5 — Procurement (CPO / Strategic Sourcing / Vendor Management)

If you are the Chief Procurement Officer, this chapter is your seat. If you are the vendor selling to them, this chapter is the unit-economics breakdown your competitive comparison failed and the exit story your roadmap deck did not contain.

**Who they are.** The CPO reports to the CFO at roughly 70% of F1000 and to the COO at 20%. Below the CPO sit Strategic Sourcing (the category manager who runs the RFP), Vendor Management (post-signature performance), Procurement Operations (the purchase-to-pay plumbing), and the seat that did not exist in 2022 and now does — the **AI Category Manager**. The AI Category Manager exists because the cloud bill went non-linear in 2024–2025, the apples-to-oranges pricing-comparison problem made traditional sourcing methodology break, and someone in the CPO's organization needed to own the pricing-model heterogeneity across per-seat, per-token, per-trajectory, per-resolved-case, and per-outcome vendor offers.

**What they evaluate.** Commercial terms — pricing model, term length, ramp, true-up structure, MFN, cap-and-collar mechanisms. Vendor viability — financials, customer concentration, investor profile, runway, the burn-to-ARR ratio for vendors below $100M. Reference checks — three to five named at-scale customers in the buyer's industry, willing to take a call. Competitive bake-off against the top alternatives in the category. Total cost — including foundation-model passthrough, infrastructure footprint on the buyer's side, integration cost, and the operator-translation overhead. Negotiation history with industry peers (Procurement organizations talk to each other). The exit story — what happens on day 1, day 30, day 90, day 365 of a termination.

**What they will reject for.** Five hard lines. First, pricing not benchmarkable — every vendor in the agent category uses a different unit (per-trajectory, per-token, per-resolved-case, per-seat, per-outcome) and Procurement cannot run a competitive comparison without a normalized basis. Second, vendor viability concerns: a sub-$10M ARR vendor selling to F1000 with no path to capitalization, no enterprise references, and no auditable financials does not pass viability review in 2026 regardless of how good the demo is. Third, no exit story — what happens to persistent memory, trajectory logs, fine-tuned adapters, and integrations on termination is a contract question, not a roadmap question. Fourth, MFN refusal at scale when the buyer is in the top-10% of the vendor's ACV. Fifth, pricing volatility from unbounded foundation-model passthrough — Procurement will not sign a contract whose total cost over three years is a function of OpenAI's or Anthropic's price decisions.

**Review cycle.** RFP and competitive bake-off at 6–16 weeks. Commercial negotiation at 4–10 weeks. Reference calls at 1–3 weeks. Total time-in-queue for Procurement at F1000 in 2026: **10–24 weeks**, often running in parallel with Legal and InfoSec. The vendor who shortens this lane shortens the deal more than any other compression.

**Artifacts required.** Pricing with multi-year ramp, with stress-tested scenarios at +20% and +50% usage. Three to five named at-scale in-industry references willing to take a call. Financial viability documentation — audited financials for vendors above $50M ARR, capitalization summary for everyone, runway and burn disclosure. Order form, SLA exhibit, competitive benchmarking data. An exit-and-portability section in the MSA itself, not a roadmap commitment. Minimum-commit and true-up structure with documented thresholds.

**New AI-specific concerns.** Foundation-model passthrough margin and the buyer's exposure to model-price increases — vendors who build their P&L assuming inference cost stays flat are vendors whose pricing terms will not survive a Bedrock or Azure OpenAI repricing event. Trajectory cost variance — per-trajectory pricing is unmodellable for the buyer if the trajectories vary 10x in token consumption, so buyers want per-trajectory ceilings or per-tenant budgets. Outcome-based pricing legitimacy — Sierra's "pay on resolved case" model is attractive but the attribution methodology is contested, Bret Taylor's thesis is being pressure-tested across CX in 2025–2026 and has begun migrating to legal, finance, and customer-success, and Procurement's job is to price the gaming risk. AI vendor viability through the shakeout — 11x's quality-ceiling concession and the ARR-and-churn disclosures from Hayden Sukkar in 2024–2025 taught Procurement that AI-agent revenue does not predict survival, and the lesson is now hard-coded into viability scorecards. Total cost including the buyer's own compute, observability stack, and trajectory storage — usually 30–60% on top of the vendor invoice and almost never disclosed by the vendor up front.

**Escalation and blocker dynamics.** Procurement escalates to the CFO. Override is available when the sponsor has CFO or CEO air-cover for strategic spend; override is effectively unavailable on viability concerns or on pricing-unbenchmarkable rejections. The CPO who lets a non-viable vendor through is the CPO who explains the migration cost to the CFO 18 months later.

**Three questions a CPO will ask in 2026, verbatim.**

1. *"Model your pricing three years out at our projected usage, stress-tested for foundation-model price increases of 20% and a usage spike of 3x. What is the cap, what is the renegotiation trigger."*
2. *"Three at-scale references in our industry. I will call them. I will ask what they would change about the contract."*
3. *"What does my exit look like on day 1, 30, 90, 365? Where is my data, my agent state, what is the migration cost."*

**Vendor tactical guide.** Publish transparent benchmarkable pricing — resolved cases or completed trajectories with an SLA, not raw tokens. Offer usage caps and per-tenant ceilings as a default contract term, not a negotiation concession. Offer foundation-model passthrough transparency with documented margin. Bring three references willing to take a call — and brief them honestly, because the CPO's reference call is going to ask "what would you change about the contract" and the reference is going to answer truthfully. Document the exit story in the MSA up front, with named SLAs per artifact (memory export in N days, trajectory-log export in N days, fine-tuned-adapter handover in N weeks, deletion confirmation log within N hours of completion). The vendor who treats Procurement as the last lane to clear is the vendor whose deal goes sideways at quarter-end. The vendor who treats Procurement as a co-architect of the commercial terms gets a second contract on the next renewal.

---

### Chapter II.6 — Business Sponsor (CRO / CMO / VP CS / business-line owner)

If you are the business sponsor, this chapter is your seat. If you are the vendor selling to them, this chapter is your true customer — and the operator-translation gap that quietly kills more agent deployments than any other failure mode.

**Who they are.** The executive who actually wants the tool. The CRO for sales agents. The CMO for marketing automation and content. The VP of Customer Success or VP of Support for service agents. The CFO for finance-ops automation. The CHRO for HR agents (with the heavy political layer that comes with it). The Chief Legal Operations Officer for legal-tech. The sponsor is the vendor's internal champion and the seller's true customer. The sponsor reports to the CEO or to the board on deployment outcomes. The sponsor has quarterly P&L pressure, and that quarterly pressure is the variable that determines pilot speed and willingness to absorb procurement friction.

**What they evaluate.** Will the agent hit the number — the specific quarterly metric the sponsor reports to the CEO. How fast does it get to value (the TTM curve). What is the change-management cost across the affected team. What is the team-adoption story (the agent that ships and is not used is the agent that gets renewed at zero). What is the operator-translation cost — the line manager who actually runs the deployment day-to-day, translating between the agent's outputs and the human team's workflow. What is the vendor-roadmap alignment with the sponsor's strategy, and where is the divergence risk.

**What they will reject for.** Five hard lines. First, time-to-meaningful-result over 90 days — sponsors operate on quarterly P&L cycles and cannot wait two quarters for a flat outcome. Second, operator-translation gap unaddressed — the vendor who pitches the line manager but ships the cockpit UI for the engineer is the vendor whose pilot stalls at week 4 because nobody on the team knows how to drive it. Third, outcome attribution that feels dishonest — "we resolved X cases" with vendor-defined resolution criteria, where the resolution criteria conveniently align to the vendor's per-resolved-case pricing model. Post-11x, every CRO reads outcome-attribution claims with appropriate skepticism. Fourth, no co-marketing or case-study leverage — sponsors get internal credit for being early on the case study, and a vendor who refuses to co-author is leaving the sponsor's career incentive on the table. Fifth, roadmap divergence from the sponsor's strategy — the agent that solves a Q2 2026 problem the sponsor has already stopped caring about is not the agent the sponsor signs.

**Review cycle.** Sponsor engagement is the fastest lane in the procurement gauntlet. Intro to internal champion at **2–6 weeks**. The sponsor then carries the deal across the other six counterparties — which is where the actual time-in-queue accumulates. A vendor who lands the sponsor and then loses two months in InfoSec, Privacy, Legal, AI Council, Procurement, and EA has not lost the sponsor; the sponsor has lost confidence in the vendor's ability to clear the gauntlet, and in the next deal the sponsor will quietly look elsewhere.

**Artifacts required.** Product demo with the sponsor's own data if possible (not a generic demo with sample data). In-vertical and in-function case studies — three to five, with named comparable customers. Implementation timeline mapped to the sponsor's fiscal calendar. A success-metrics framework the sponsor can defend to their CEO and their board. Reference calls with peer-level sponsors at comparable companies.

**New AI-specific concerns.** Reputational risk from agent error — a sales agent mis-sending an outbound to the CEO of a top-10 customer is a career risk for the CRO and the sponsor knows it. Internal political optics of replacing seats with agents — CHROs, CMOs, and CROs are sensitive to the "AI replaces humans" framing and want augment-not-replace talk-tracks they can deploy in town halls. Outcome attribution under board scrutiny — when the board asks "did this agent actually move the number," the sponsor needs to answer with attribution methodology that survives the audit committee. Operator-translation cost — the line manager running the deployment may be the binding constraint on time-to-value, not the agent itself. Quarterly model-quality drift — an agent deployed in Q1 whose performance shifted in Q3 because the underlying foundation model updated is the agent that produces a difficult earnings-call moment for the sponsor's executive.

**Escalation and blocker dynamics.** The sponsor escalates to the CEO. The sponsor is rarely blocked except on hard regulatory or security floors that trace back to InfoSec, Privacy, Legal, or AI Council. When blocked, the sponsor either drops the deal, escalates for CEO override, or negotiates a smaller-scope deployment that fits inside the existing compliance envelope. The honest pattern in 2026 is that sponsors who escalate too often lose internal credibility, and sponsors who escalate too rarely lose deals to faster-moving peers — the calibration is real and the vendor's job is to make the sponsor look good either way.

**Three questions a sponsor will ask in 2026, verbatim.**

1. *"What did the last three customers at my scale do in their first 90 days, measurable outcome at day 90."*
2. *"My line manager runs this day-to-day. Show me their week."*
3. *"When the model drifts or the agent acts wrong, who calls me, when, what is the playbook."*

**Vendor tactical guide.** Run a 30-day paid pilot with a defined success metric — paid pilots filter out tire-kickers and signal sponsor commitment to the rest of the buyer's organization. Bring two reference sponsors on a peer call within the first three weeks, before the sponsor has to defend the deal internally. Map the operator-translation surface explicitly — name the line manager's persona, walk through their week, identify the workflow integration points and the escalation paths. Co-author the case study before signing, not after — the sponsor wants the artifact in their file the day they make the decision, not the quarter after they have to defend it. Do not pitch the sponsor on token economics, model architecture, or sub-agent privilege design — those are the other six counterparties' questions. Pitch the sponsor on the number, the time-to-value, and the operator's week.

---

### Chapter II.7 — Enterprise Architecture / IT Ops (CIO / Chief Architect / Head of Platform)

If you are the Chief Architect or Head of Platform Engineering, this chapter is your seat — and the F1000 procurement model that under-counted you for two decades has finally caught up. If you are the vendor selling to them, this chapter is the reference-architecture conformance review your AE has been pretending was an InfoSec problem and the OpenTelemetry GenAI export your engineering team has been treating as a roadmap item.

**Who they are.** The CIO reports to the CEO at roughly 70% of F1000, to the COO at 20%, and to the CFO at 10%. Below the CIO sit the Chief Architect (who owns the reference architecture and the technology radar), the Head of Platform Engineering or IT Operations (who owns run-the-business, on-call rotation, and capacity planning), the Head of Integration (the SaaS-to-SaaS plumbing layer), and the seat that did not exist in 2022 and is now standard at F1000 — the **AI Platform Engineering** team. AI Platform Engineering owns the LLM gateway, the eval and observability stack, the vector store, the agent runtime, and the per-trajectory cost telemetry. They are the team who actually gets paged when the agent fan-out cascades into a downstream-system DoS.

**What they evaluate.** Reference-architecture fit — does the vendor work with the buyer's identity fabric, observability pipeline, secrets management, deployment toolchain, and change-management process. Operability footprint — runbook quality, dashboard depth, alert specification, cost-telemetry data model. Capacity — concurrency, throughput, sub-agent fan-out behavior under load. Failure modes — graceful degradation, circuit breakers, the behavior of the system when the foundation-model provider returns 429s for an hour. Multi-region, multi-cloud, and multi-tenancy posture.

**What they will reject for.** Five hard lines. First, non-conformance to reference architecture — the vendor demands a private VPC peer when SAML/OIDC suffices, cannot ship logs to the buyer's observability pipeline, or insists on bespoke identity. Second, unbounded sub-agent fan-out without circuit breaker — an agent spawning 100 sub-agents on a single trigger is a denial-of-service risk against downstream systems and the EA team will not let it through. Third, no per-trajectory cost telemetry — EA cannot govern what it cannot see, and per-trajectory metering is the agent-era equivalent of per-API-call billing transparency. Fourth, OAuth blast radius unbounded — "read all email, all calendar, all files" when the agent's purpose justifies a narrow scope is a rejection on principle, not a negotiation. Fifth, no runbook, no RTO, no RPO, and no documented failure-mode catalog — operability is a contract item, not a roadmap commitment.

**Review cycle.** **4–10 weeks**, often running in parallel with InfoSec. Longer when the integration design requires new reference-architecture exceptions, which it usually does for first-of-kind agent runtimes and for any vendor whose deployment posture has not been seen in the buyer's environment before.

**Artifacts required.** Architecture diagram with trust boundaries explicit. Integration design covering identity, observability, secrets, deployment, and change management. Operability runbook with named on-call contacts and RTO/RPO commitments. Capacity-and-concurrency benchmarks at the buyer's expected load. Cost-telemetry data model with a documented export interface. Multi-region design if the buyer operates in multiple jurisdictions. Failure-mode catalog with circuit breakers per failure class. OAuth scope inventory with least-privilege justification per scope.

**New AI-specific concerns.** Foundation-model dependency in the reference architecture — where does the model run, who pays for inference, what is the contingency when the lab issues a CVE or rate-limits the buyer mid-quarter. Per-trajectory cost variance versus the predictable per-API-call SaaS economics the EA team built their finance models around. OAuth-blast-radius governance — agents asking for "read everything" trigger EA review at F1000 even when InfoSec has cleared the credential-security question. Trajectory observability through the buyer's OpenTelemetry pipeline (OpenTelemetry GenAI conventions matured through 2024–2025 and stabilized through Q4 2025; they are table-stakes at F1000 in 2026 and a vendor without OTel GenAI conformance is signaling that they have not done F1000 work at scale). Sub-agent privilege separation as an identity-fabric question — when an agent spawns a sub-agent, what tools and credentials does it inherit, and what does the buyer's identity fabric actually see in the audit log.

**Escalation and blocker dynamics.** EA escalates to the CEO or COO. Override is rare and effectively unavailable on reference-architecture conformance or on operability gaps. The reference architecture exists because the F1000 has spent two decades cleaning up the consequences of every "exception" it ever granted, and the Chief Architect is the institutional memory of those consequences. Vendors who try to negotiate around the reference architecture instead of conforming to it are the vendors whose deals fall apart in week 8.

**Three questions a Chief Architect will ask in 2026, verbatim.**

1. *"Reference-architecture fit. Identity, observability, secrets, deployment, multi-region. Here is our published architecture — tell me where you don't fit."*
2. *"Sub-agent fan-out behavior under failure. What is the circuit breaker, the cost ceiling per trajectory, what does my SIEM see."*
3. *"Per-trajectory cost telemetry. Show me the data model and the export."*

**Vendor tactical guide.** Ship OpenTelemetry GenAI conventions native — not as a roadmap commitment, as a current capability. Expose per-trajectory cost metering with a documented export interface. Document OAuth scopes per tool with least-privilege justification, and offer narrower scopes as a default rather than asking the buyer to negotiate them down. Publish a reference architecture with buyer's-VPC as a first-class deployment tier — not a "we can do that on request" caveat. Bring the Solutions Architect to the EA meeting and let them answer the integration questions directly. Do not let the AE handle the EA review; the AE will fold on a question they do not understand and the Chief Architect will read the fold as a vendor-maturity signal.

The Chief Architect is the seventh chair, and they are the one who will tell you — in the post-mortem, not the pre-mortem — exactly why the agent vendor you bought in Q1 is the agent vendor you will be migrating off in Q4.

---

*End of Section II. Sections III and IV (Seven Overlays, Fourteen Addenda) are in PLAYBOOK_part_B.md. Sections V through VIII (Decision Tree, Scoring Rubric, Glossary, Appendix Contract Clauses, Closing) are in PLAYBOOK_part_C.md.*

# The AI Vendor Procurement Playbook — Part B

**Sections III + IV · The Seven Agent-Specific Overlays + The 15 AI-Specific Addenda**
*Edition 1.0 · Spring 2026 · Author: Alex Yedi*

---

## Section III · The Seven Agent-Specific Overlays (plus §III.8 · Per-Trajectory FinOps)

Section II walked the seven counterparties — InfoSec, Legal, Privacy, AI Governance, Procurement, Business Sponsor, and (at F1000 specifically) Enterprise Architecture. Those chapters answered the question: *who in the buyer org chart is asking this, and why*. This section answers a different question: *what are the seven controls that exist only because the vendor is shipping an agent and not a SaaS?*

The distinction matters. A 2014–2023 SaaS procurement asks the seven counterparties seven sets of questions, and the vendor passes or fails on a SOC 2, a DPA, an MSA, an SLA, and a reference call. None of those artifacts answer the question of what happens when the agent reads a tainted email and writes the wrong value to a system of record. None of them answer the question of which model version the eval was run against, or what the rollback path looks like when the action was already committed downstream. Those are agent-specific questions, and they map to seven specific overlays — controls that did not exist in 2022, that emerged through 2024 and 2025 in the seam between SaaS procurement and AI governance, and that hardened into a procurement floor through Q1 and Q2 2026.

Each overlay maps to one or more counterparties. Tool-Boundary Policy is owned by InfoSec and AI Governance jointly. Indirect Prompt-Injection Adaptive Red-Team is owned by InfoSec. Action-Rollback Documentation is owned by InfoSec, the controller (under Procurement-adjacent SOX exposure), and the Business Sponsor. Sub-Agent Privilege Separation is owned by InfoSec and Enterprise Architecture. Signed Reproducible Eval Reports are owned by AI Governance, with Legal and InfoSec as co-signers. EU AI Act Article 14 Tie-Out is owned by AI Governance, Legal, and Privacy. Sectoral Overlays attach to the regulated-vertical counterparty seat (model-risk in FSI, the BAA owner in healthcare, the program security officer in defense). And §III.8 — Per-Trajectory FinOps — is owned by Enterprise Architecture and the CFO's FP&A team jointly, and it is the overlay most likely to be missed in a 2026 procurement cycle.

Each overlay chapter follows the same seven-part structure: plain-English definition, why it matters now, the buyer-side question, the vendor-side artifact, sample contract language, the red flag to reject for, and the current vendor landscape as of May 2026. Use the sample language as drafting material; do not adopt it verbatim without your GC's review.

---

### Chapter III.1 — Tool-Boundary Policy

**Plain English.** A tool-boundary policy is the written, vendor-supplied map of every tool the agent can call, every action each tool can take, every condition under which the agent is allowed to call it unattended, every condition under which the agent must escalate to a human, and the exact privilege scope the agent holds against the tool. Without this document, the buyer is approving an agent on the basis of demos. With this document, the buyer is approving an agent on the basis of policy.

**Why it matters now.** Three things changed between Q1 2024 and Q2 2026. First, computer-use launched in October 2024 (Claude) and matured through 2025 with OSWorld scores climbing into the mid-50s — still well below the human 72% — which made unattended SaaS-UI agents commercially marketed but operationally fragile. Second, MCP graduated to Linux Foundation governance in December 2025, making tool inventories more legible across vendors but also exposing how few vendors had a written tool-boundary policy at all. Third, the Colorado AI Act (May 2024) and the EU AI Act (passed March 2024, GPAI obligations live August 2025, Article 14 implementation guidance to draft April 2026) made the lack of a written boundary a regulatory exposure, not just an operational one. A 2026 procurement review without a tool-boundary policy is a 2026 procurement review you cannot defend in a Q1 2027 audit.

**The buyer-side question.** The InfoSec lead and the AI Council Chair will ask, jointly: *"For each tool this agent can call, name the action verbs available, the scope of each action, the privilege the agent runs under, the conditions under which the agent invokes the tool unattended, the conditions under which the agent must request human approval, the conditions under which the tool is blocked entirely because the planning context is tainted by external content, and the audit log emitted per call."* A vendor that hands you a thirty-page document satisfies this question. A vendor that says *"the agent uses your existing approval flows"* does not.

**The vendor-side artifact.** A Tool-Boundary Policy Document. Twelve to forty pages depending on tool surface. Per tool: action verbs and scopes; default privilege grant; sub-agent privilege if any; conditions for unattended invocation; conditions for human-in-the-loop approval; conditions for tainted-context blocking; rollback story; audit log schema. Sierra, Decagon, Glean, and Harvey have these documents internally; not all of them will share without an NDA. Hebbia, Rogo, and Hippocratic, in my experience, will share once you ask in the right form. Demand it before you sign a pilot, not before you sign a production contract — the asymmetry in your favor closes the moment money has moved.

**Sample contract language.** *"Vendor shall maintain and provide to Customer, upon request and at least annually, a Tool-Boundary Policy Document covering every tool the Agent is configured to invoke against any Customer System. The Document shall enumerate, per tool: (a) available action verbs and their scopes; (b) the privilege under which the Agent invokes the tool; (c) the conditions under which the tool may be invoked without human approval; (d) the conditions under which human approval is required prior to invocation; (e) the conditions under which the tool is blocked when planning context contains untrusted external content; (f) the audit log schema emitted per invocation. Material changes to the Document shall be communicated to Customer no less than thirty (30) days before deployment to production. Vendor's failure to maintain or disclose this Document is a material breach permitting Customer to terminate this Agreement without penalty and recover prepaid fees on a prorated basis."*

**The red flag — what to reject for.** Reject any vendor who answers "the agent only does what you authorize it to do" without supplying the document. That sentence is a defense lawyer's nightmare and a procurement officer's escape clause. Also reject any vendor whose policy lists fewer than four privilege tiers across the tool surface — agents that operate at a single privilege level are agents that will eventually do something they should not have.

**Current landscape.** Sierra is the clearest leader; their AgentOS documentation is the closest thing to a public tool-boundary policy in the vertical-agent space. Harvey is competent here because the legal-vertical buyer demands it. Hippocratic publishes a partial version as part of HIPAA preparation. Glean publishes a thin version aimed at enterprise search rather than action. Decagon is improving but lagging Sierra by roughly a year. Hebbia and Rogo, both NYC-native, are documenting internally faster than they are publishing — a procurement opportunity in your favor if you push. 11x is a cautionary tale: synthetic-SDR vendors built without a tool-boundary policy in 2024 are the vendors whose ARR went flat in 2025 because RevOps buyers stopped trusting outcome attribution. The pattern repeats elsewhere.

---

### Chapter III.2 — Indirect-Prompt-Injection Adaptive Red-Team

**Plain English.** An indirect prompt injection happens when content the agent reads from a tool — a customer email, a CRM note, a PDF, a webpage, an MCP server response — contains instructions to the agent that override what the operator asked. An adaptive red-team is a continuously updated adversarial test suite that generates new injections against the live agent, against the current model version, against the current system prompt. A static red-team is a test suite that ran once against a public corpus. They are not the same thing, and 99% of the indirect-injection numbers vendors cite refer to the second.

**Why it matters now.** Indirect prompt injection became the unsolved problem of the agent layer through 2024 and 2025. Public-corpus defenses (Lakera Guard, NeMo Guardrails, Promptfoo) cleared 95%+ on their own benchmarks; adaptive-adversary methodology — where the red team updates faster than the defense — clears 60–80% honestly. The gap is the dollar-exposure gap. Adam Raine's case against OpenAI in California court, the Air Canada chatbot ruling (February 2024) that held the airline liable for its bot's hallucinated refund policy, and the NYT v. OpenAI proceedings all crystallize the legal argument that the vendor is responsible for what the agent does in the presence of adversarial inputs. The Microsoft Copilot Studio prompt-injection demos at Black Hat 2024 and the EchoLeak class disclosures through 2025 made the threat surface concrete enough that no F1000 InfoSec team treats it as theoretical anymore. By 2026 the procurement question is not *whether* the agent has indirect-injection defense. It is whether the defense is adaptive, whether it is honestly disclosed, and whether the test methodology survives review.

**The buyer-side question.** The CISO will ask: *"Show me the most recent adaptive-adversary red-team report against this specific agent, this specific model version, this specific system prompt, run within the last 90 days. Name the methodology. Name the team that ran it. Name the success rate against tool returns, against retrieved document context, against multi-turn injection sequences. Disclose the failure modes."* The InfoSec lead will follow with: *"What is your refresh cadence and your kill-switch procedure when a new injection class breaks the defense?"*

**The vendor-side artifact.** A signed adaptive-adversary red-team report. Quarterly minimum. Conducted by an external team (Lakera Red, Robust Intelligence, HiddenLayer, or a credible internal team with an external attestation). Tied to a model pin, a system prompt hash, and a tool inventory. Discloses adaptive-adversary success rates honestly — anything above 90% should be treated with skepticism, anything below 60% should be treated as a fail. Includes the kill-switch procedure: how the vendor disables the tool, the model, or the agent when a new injection class is discovered, and the buyer-notification SLA.

**Sample contract language.** *"Vendor shall conduct an adaptive-adversary indirect-prompt-injection red-team assessment against the Agent no less frequently than quarterly. Each assessment shall be tied to a specific model identifier, system prompt hash, and tool inventory, and shall report adaptive-adversary success rates against tool returns, retrieved document context, and multi-turn injection sequences. Vendor shall provide the report to Customer within thirty (30) days of completion. Discovery of an injection class against which the Agent's defense rate falls below sixty percent (60%) shall constitute a Security Incident requiring notification to Customer within forty-eight (48) hours, and Vendor shall make available a kill-switch procedure permitting Customer to disable the affected tool or agent pending remediation."*

**The red flag — what to reject for.** Any vendor citing >95% indirect-injection detection without naming the adaptive-adversary methodology. Any vendor citing public-corpus benchmarks only. Any vendor unable to commit to a 48-hour notification SLA on a defense-rate drop. Any vendor whose kill-switch procedure requires opening a support ticket — the kill-switch must be in the buyer's hands or in a documented automated path.

**Current landscape.** Lakera is the most honest disclosure in the category and the right red-team partner for most F1000 buyers; their adaptive numbers track between 60% and 80% depending on agent surface, and they say so. Robust Intelligence sells more broadly. HiddenLayer is improving on the model-supply-chain side. Anthropic and OpenAI both publish responsible-disclosure timelines and have improved through 2025; neither yet ships a turnkey adaptive-adversary report for the buyer's specific deployment. The vertical-agent vendors (Sierra, Decagon, Harvey) are partnering with the red-team specialists rather than building internally — which is fine, and on balance preferable, because conflict-of-interest is real when the vendor is the one grading their own homework. Reject vendors who refuse to name their red-team partner.

---

### Chapter III.3 — Action-Rollback Documentation

**Plain English.** An action-rollback story is the written, per-write-tool description of what happens when the agent executes the wrong action against a Customer system of record. It names the recovery path, the recovery time, the data residency of the rollback log, and the conditions under which rollback is impossible. Without this document, you are buying optimism. With this document, you are buying a recovery procedure.

**Why it matters now.** Air Canada (February 2024) is the cleanest precedent: the airline argued the chatbot was a separate legal entity; the British Columbia tribunal disagreed and held Air Canada liable for the chatbot's hallucinated bereavement-refund policy. That ruling is about output, not action. Replace "hallucinated policy" with "wrongly posted journal entry," "duplicate refund," "unauthorized scope grant," or "deleted customer record" and the legal exposure compounds. Through 2024 and 2025 the production-failure mode that recurs most often in F500 post-mortems is not the agent failing visibly; it is the agent succeeding-as-judged and writing the wrong value to a system of record. Silent failure is the dominant operational risk of the agent era. Action-rollback documentation is how procurement holds the vendor to a recovery contract.

**The buyer-side question.** The CIO and the controller will ask jointly: *"For every write tool this agent can call against our systems, show me: (a) the recovery procedure when the wrong value is written; (b) the maximum recovery time; (c) the audit log a controller will accept; (d) the conditions under which recovery is impossible, and the indemnity that attaches to those conditions."* The AI Council Chair will follow with: *"How does this procedure integrate with our existing incident-response runbook?"*

**The vendor-side artifact.** An Action-Rollback Document, per write tool, signed off by the vendor's engineering and security leads. Per tool: the underlying recovery mechanism (database row versioning, idempotency keys, soft-delete with restore window, dead-letter queues for irreversible side effects); the maximum recovery time SLA; the audit-log schema; the irreversible-action list (e.g., sending an email, charging a card, executing a trade, posting to a public channel) and the human-approval gate that must precede each; the rollback testing cadence.

**Sample contract language.** *"Vendor shall maintain a written Action-Rollback Procedure for every Write Tool the Agent is configured to invoke against any Customer System of Record. The Procedure shall specify, per tool: (a) the recovery mechanism (including row versioning, idempotency, soft-delete, or dead-letter queue) and the maximum time-to-restore SLA; (b) the audit log emitted per write, in a format Customer's controller will accept for SOX or equivalent financial-control review; (c) the list of irreversible actions, and for each, the human-approval gate that must precede invocation; (d) the rollback testing cadence, with results provided to Customer no less frequently than semi-annually. Failure of a rollback within the SLA window shall constitute a Service Failure and entitle Customer to service credits as specified in the Service Level Schedule, in addition to any remedies available for material breach."*

**The red flag — what to reject for.** Any vendor whose answer is "we have logging." Logging is not rollback. Any vendor whose irreversible-action list is shorter than three items — they have not thought about it. Any vendor unwilling to commit to a maximum time-to-restore SLA. Any vendor whose rollback testing has not been conducted in the last twelve months.

**Current landscape.** This is the single weakest overlay in the current vendor field. Sierra has the most mature internal practice but does not publish externally. Hippocratic, because of HIPAA, has the cleanest write-side discipline in the regulated-vertical space — their action-confirmation gates are real and audited. Harvey is acceptable for legal-research workflows because the write surface is narrow. Decagon is improving but uneven across customer instances. Glean has effectively no write story at scale because its product is read-dominant — which is fine for Glean, less fine for the buyer who is asking Glean to start writing back into the CRM. Hebbia and Rogo are documenting privately. The vendors with the worst action-rollback documentation as of May 2026 are the synthetic-SDR vendors (11x and its peers), the autonomous-coding-agent category (Cognition, Devin's earlier iterations) where rollback meant "revert the PR" rather than "restore the production deployment," and any vendor pitching unattended computer-use into a production SaaS without naming the rollback story. Reject these.

---

### Chapter III.4 — Sub-Agent Privilege Separation

**Plain English.** Most production agents are not one agent. They are an orchestrator that delegates to two-to-ten sub-agents (a planner, an executor, a verifier, a tool-specific worker, a memory-writer, an escalation handler). Sub-agent privilege separation is the architectural and contractual commitment that each sub-agent runs at the minimum privilege necessary for its role, that an executor sub-agent cannot escalate itself into a privilege a planner would hold, and that the privilege boundary is enforced at runtime — not just at design time.

**Why it matters now.** The transition from single-agent ReAct loops to multi-agent / planner-executor architectures accelerated through 2025 as `reasoning_effort` became a buyer-controllable knob (OpenAI o-series, Claude 4.5 / 4.6 / 4.7, Gemini 2.5+) and as the planner-executor split emerged as the dominant cost-optimization pattern at the trajectory level. The security consequence is that a single compromise — an indirect injection into the planner — can now propagate down a privilege chain that the buyer never mapped. Without sub-agent privilege separation, an injection that reaches the executor reaches everything the executor can reach. With it, the blast radius is bounded. Through 2025 and into 2026 the architectural reality outran the procurement framing; buyers were still asking "what does the agent do" while vendors were shipping six-sub-agent systems. The procurement question has to catch up.

**The buyer-side question.** The InfoSec lead and the AI Council Chair will ask: *"Diagram every sub-agent in this architecture. Per sub-agent, name the role, the privilege scope, the tool inventory, the memory it can read, the memory it can write, and the conditions under which it can invoke another sub-agent. Show me how the privilege boundary is enforced at runtime, not in code review. Show me your test cases for cross-sub-agent privilege escalation."*

**The vendor-side artifact.** A Sub-Agent Architecture Document. Diagram per role. Privilege matrix. Runtime enforcement mechanism (capabilities, signed delegation tokens, separate execution contexts). Test cases for privilege escalation, with results. The honest version of this document is uncomfortable for the vendor to share because it tends to show the seams in their architecture. That discomfort is your leverage during pilot procurement.

**Sample contract language.** *"Vendor shall maintain a Sub-Agent Architecture Document enumerating every sub-agent in the Agent system, the role and privilege scope of each, the tool inventory available to each, the read- and write-scopes against persistent memory, and the conditions under which one sub-agent may invoke another. Vendor shall enforce sub-agent privilege boundaries at runtime via capability tokens, signed delegation, or equivalent mechanism, and shall maintain test cases against cross-sub-agent privilege escalation. The Document and the most recent test results shall be provided to Customer upon request and at least annually. Architectural changes that alter the sub-agent privilege matrix shall be communicated to Customer no less than thirty (30) days before production deployment."*

**The red flag — what to reject for.** Any vendor whose architecture diagram is one box labeled "the agent." Any vendor whose privilege enforcement is "we check it in code review." Any vendor unable to produce test cases for cross-sub-agent privilege escalation. Any vendor where the planner and the executor run in the same execution context with the same tool inventory — that is a single-agent system pretending to be a multi-agent system, and the architectural complexity will surface as security debt within twelve months.

**Current landscape.** Anthropic and OpenAI both publish architectural patterns for sub-agent privilege separation in their developer documentation; Anthropic's sub-agent / tool-use patterns are the cleaner public reference as of Q2 2026. Sierra, Decagon, and Harvey all operate multi-agent architectures with named privilege boundaries internally; Sierra's is the most mature and the most willing to be documented for buyer review. Hippocratic uses sub-agent separation by clinical-task boundary, which maps cleanly to HIPAA minimum-necessary; the artifact is good. Glean is a read-dominant orchestrator and the sub-agent question is less load-bearing. The general-purpose autonomous-coding-agent category (Cognition / Devin and its peers) is the weakest here — single-context multi-tool agents with insufficient privilege separation between the planner and the executor, which is why their production-failure modes tend to be catastrophic rather than bounded. The agent-building frameworks (LangGraph, CrewAI, AutoGen, Letta) document sub-agent patterns but do not enforce them; the enforcement burden falls on the vendor or the buyer.

---

### Chapter III.5 — Signed Reproducible Eval Reports

**Plain English.** A signed reproducible eval report is a written artifact tied to a specific model identifier, a specific dataset hash, a specific harness version, and a specific evaluation methodology, that the buyer can independently reproduce within their own observability stack and that survives a regulator subpoena. It is the agent-era equivalent of a SOC 2 Type II report. It does not currently exist at turnkey grade from any major vendor. That gap is the highest-leverage wedge in this Playbook.

**Why it matters now.** Through 2024 and 2025 the eval-platform category (Braintrust, LangSmith, Galileo, Patronus, Arize) commoditized on the observability side. Inspect AI (UK AI Safety Institute) emerged as the audit-grade open-source harness through 2025. OpenTelemetry GenAI conventions stabilized through Q4 2025 and into Q1 2026. What did not emerge is the missing piece: a *signed* report that ties a model pin to a dataset hash to a harness version to a reproduction procedure, that is portable across buyers, and that an EU AI Act conformity assessor in late 2026 will accept as evidence. Every vendor produces internal benchmarks. None of those benchmarks are buyer-reproducible. None of them are signed. None of them survive a subpoena. The Bartz settlement framework and the NYT v. OpenAI proceedings make this exposure concrete: the question "what did you know and when did you know it about your model's behavior on this class of input" is now a litigated question, and the answer is the eval report. If your vendor cannot produce one in defensible form, your company is the one holding the bag.

**The buyer-side question.** The AI Council Chair, the CISO, and the GC will ask jointly: *"Provide a signed reproducible eval report for this agent against use cases representative of our deployment. The report must specify: (a) the exact model identifier (e.g., claude-opus-4-7-20260301); (b) the dataset identifier and hash; (c) the harness version; (d) the metrics, methodology, and confidence intervals; (e) reproduction instructions detailed enough for our team to independently re-run the eval and verify within five points of your reported score. The report must be signed by a named vendor representative and dated within the last 180 days."*

**The vendor-side artifact.** A Signed Reproducible Eval Report. Per release, per major use case. Format: written report plus reproduction artifacts (dataset, harness configuration, model identifier). Refresh: at least quarterly, immediately on model-version change. Signature: named vendor representative with attestation language. Reproduction: the buyer should be able to re-run within their observability stack and land within five points of the reported score; if they cannot, the report is untrusted by definition.

**Sample contract language.** *"Vendor shall provide to Customer, no less frequently than quarterly and within thirty (30) days of any model-version change affecting the Agent, a Signed Reproducible Eval Report covering use cases representative of Customer's deployment. The Report shall specify the model identifier, dataset identifier and hash, harness version, metrics, methodology, confidence intervals, and reproduction instructions. Reproduction by Customer's team within a reasonable window shall yield a score within five (5) points of the Report's stated score. A reproduction failure outside this tolerance shall constitute a material breach of the eval-evidence warranty, and Customer shall have the right to terminate this Agreement for cause and recover prepaid fees on a prorated basis."*

**The red flag — what to reject for.** Any vendor citing "our internal benchmark" without supplying the artifact. Any vendor unable or unwilling to share the dataset hash. Any vendor unwilling to commit to reproduction within five points. Any vendor whose report is dated more than 180 days ago. Any vendor whose eval is run against a public benchmark only — SWE-Bench Verified, GAIA, AgentBench — without a use-case-specific eval against your representative tasks. Public benchmarks are necessary; they are not sufficient.

**Current landscape.** Inspect AI is the closest open-source approximation of an audit-grade harness and is the right backbone to ask vendors to support. Braintrust, LangSmith, and Galileo are good observability-side platforms but do not solve the signing problem. Anthropic publishes responsible-disclosure-style model cards for each major release; OpenAI does the same; neither yet ships a turnkey signed report tied to a buyer's specific deployment. The vertical-agent vendors are uneven: Harvey publishes legal-benchmark performance with reproducibility hooks, Hippocratic publishes clinical-task evals with the right methodological discipline, Sierra reports outcome-based metrics that translate poorly to a regulator subpoena framing, Decagon and Glean lag. Hebbia and Rogo publish less but document internally with reasonable rigor. This is the load-bearing Bet #1 wedge: the canonical buyer-side standard for signed reproducible eval reports does not exist, and the first credible publisher of that standard will set the procurement default for the next five years.

---

### Chapter III.6 — EU AI Act Article 14 Human-Oversight Tie-Out

**Plain English.** Article 14 of the EU AI Act requires that high-risk AI systems be designed and developed so that natural persons can effectively oversee them. A human-oversight tie-out is the written, control-by-control mapping from the vendor's product to the specific Article 14 requirements (the operator's ability to understand the system, monitor operation, interpret output, decide not to use the output, intervene, and interrupt). The mapping must hold for the buyer's specific deployment, must be refreshed when the system changes, and must produce evidence a conformity assessor will accept.

**Why it matters now.** The EU AI Act passed March 2024. GPAI obligations entered force August 2025. Conformity-assessment guidance drafts landed February 2026. Article 14 implementation guidance went to draft in April 2026 — the most-actionable near-term lever in the entire regulatory stack, with first enforcement actions expected late 2026 or Q1 2027. Whether the Act becomes a $10B+ procurement category or stays a niche defensive posture depends on the size and pattern of the first fines. Either way, every F1000 with EU operations is buying agents into a regime that did not exist when the agent-vendor MSAs they currently sign were written. The tie-out is how the buyer demonstrates compliance and shifts a portion of the burden onto the vendor through contract.

**The buyer-side question.** The AI Council Chair, the GC, and the privacy counsel will ask jointly: *"Provide a control-by-control mapping of this agent's design and operational features to the Article 14 oversight requirements as drafted. Per requirement, name the product feature, the operator action enabled, the evidence emitted, the refresh procedure when the system changes, and the conformity-assessment artifact. Include the parallel mapping to NIST AI RMF GenAI Profile and ISO 42001 where applicable."*

**The vendor-side artifact.** An Article 14 Tie-Out Document. Tabular form: Article 14 sub-requirement on the left, product feature in the middle, evidence and refresh procedure on the right. Cross-referenced to NIST AI RMF GenAI Profile (2024 update) and ISO 42001 (2023) where the buyer's regime requires it. Refresh cadence: annually minimum, immediately on any change that affects the oversight surface. Signature: a named vendor representative with attestation. Buyer-side reusable for the EU operations regulatory file.

**Sample contract language.** *"Vendor shall maintain and provide to Customer, upon request and at least annually, a Human Oversight Tie-Out Document mapping the Agent's design and operational features to the requirements of Article 14 of Regulation (EU) 2024/1689 (the EU AI Act) and to the National Institute of Standards and Technology AI Risk Management Framework Generative AI Profile and to ISO/IEC 42001:2023 where applicable to Customer's regulatory regime. The Document shall be refreshed within sixty (60) days of any change to the Agent that materially affects its oversight surface. Vendor warrants that the Document, taken together with the supporting evidence referenced therein, is sufficient to support Customer's good-faith demonstration of Article 14 compliance for Customer's deployment of the Agent. Material misrepresentation of Article 14 conformity in the Document shall constitute a material breach."*

**The red flag — what to reject for.** Any vendor whose answer is "we have SOC 2." SOC 2 is necessary for cloud posture; it is not an Article 14 tie-out. Any vendor whose tie-out is conceptual rather than control-by-control. Any vendor unwilling to warrant the document. Any vendor whose interpretation of Article 14 treats oversight as a UI feature ("the operator can see the agent's actions") rather than a system property ("the operator can understand, monitor, interpret, override, intervene, and interrupt"). Any vendor whose timeline for producing a tie-out is longer than your timeline for signing a renewal.

**Current landscape.** The European AI Office's Article 14 guidance is in draft and changes weekly through Q2 2026; vendors who claim certainty before final guidance is a posture, not a fact, and you should price it accordingly. The vendors with the strongest EU posture as of May 2026 are Mistral (sovereign), Anthropic (early publication of Responsible Scaling Policy maps that translate adjacently), OpenAI (Preparedness Framework similarly), and the regulated-vertical leaders (Hippocratic for clinical, Harvey for legal). The vertical-agent CX leaders (Sierra, Decagon) are improving but historically US-centric. The synthetic-SDR category effectively does not have an EU posture and you should treat their EU sales accordingly. ISO 42001 certification is becoming a procurement asset — Drata and Vanta both ship readiness mappings — but it is not the same artifact as an Article 14 tie-out and you should not let your CPO conflate them.

---

### Chapter III.7 — Sectoral Overlays (Healthcare, Financial Services, Defense)

**Plain English.** Sectoral overlays are the regime-specific control sets that attach when the agent operates inside healthcare (HIPAA, FDA SaMD, HITRUST), financial services (FINRA, broker-dealer rules, NYDFS Part 500, model-risk management under SR 11-7), or defense (FedRAMP, IL5, CMMC, ITAR). They are not optional. They are additive on top of the six other overlays and they bite hardest where the regulatory posture pre-existed the agent and was never re-drafted to contemplate one.

**Why it matters now.** Healthcare AI vendors learned through 2024 and 2025 that ambient-scribe products (Abridge, Nuance DAX, Augmedix) cleared the HIPAA bar because the data flow was scoped; full clinical agents (Hippocratic AI, Glass Health, OpenEvidence) face a harder bar because the action surface is wider. Financial-services AI faced a 2025 wave of FINRA guidance on AI-generated communications, broker-dealer suitability with AI assistance, and the OCC's interpretation of SR 11-7 model-risk management as it applies to LLMs in credit-decision flows. Defense procurement through 2025 and into 2026 hardened the FedRAMP Moderate-to-High-to-IL5 ladder for AI workloads, and CMMC Level 2 (effective broadly through 2025) added a controlled-unclassified-information layer that affects every defense-adjacent agent procurement. None of these regimes assumed agents that take autonomous actions when they were drafted. All of them now must accommodate them, and the accommodation is happening through vendor contracts, not through statute.

**The buyer-side question.** Depends on the sector.

*Healthcare:* The Privacy Counsel and the AI Council Chair will ask: *"Provide the HIPAA Business Associate Agreement; the Minimum Necessary analysis per workflow; the FDA SaMD classification if applicable, with substantial-equivalence pathway or de novo justification; the HITRUST CSF v11.x certification or readiness; the patient-safety incident-response procedure; the audit log retention duration and accessibility."*

*Financial Services:* The Compliance Officer and the CRO will ask: *"Provide the model-risk-management documentation per SR 11-7 (validation, monitoring, governance); the FINRA Communications with the Public review for any customer-facing output; the broker-dealer suitability analysis if applicable; the NYDFS Part 500 cybersecurity tie-out; the books-and-records retention per Rule 17a-4 for any agent-generated content."*

*Defense:* The CISO and the program security officer will ask: *"Provide the FedRAMP authorization at the required impact level; the CMMC Level 2 assessment; the ITAR registration if any controlled technical data is in scope; the IL5 designation if applicable; the sovereign-cloud deployment story; the supply-chain risk management plan including the model-provider relationship."*

**The vendor-side artifact.** Sector-specific. In all cases: a sectoral overlay packet stapled to the six other overlays. Healthcare adds a BAA, a FDA pathway document if applicable, a HITRUST readiness or certification artifact, and a Minimum Necessary mapping. Financial services adds SR 11-7 model-risk documentation, a FINRA communications review process, a books-and-records retention attestation, and a NYDFS 500 cybersecurity tie-out. Defense adds the FedRAMP package, CMMC level, ITAR status, and the sovereign-cloud or air-gapped deployment story.

**Sample contract language.** *(Healthcare illustrative — finance and defense follow same pattern.)* *"Vendor shall execute a Business Associate Agreement substantially in the form attached as Exhibit B. Vendor shall provide a Minimum Necessary analysis covering each Tool the Agent is configured to invoke against Customer's protected-health-information systems. If the Agent qualifies as Software as a Medical Device under FDA regulation, Vendor shall provide its 510(k), De Novo, or PMA documentation; absent such qualification, Vendor shall provide its written analysis supporting the non-SaMD determination, refreshed annually. Vendor shall maintain HITRUST CSF certification at level v11.x or higher throughout the Term and shall provide annual attestation. Any Security Incident affecting Customer PHI shall be notified within twenty-four (24) hours of discovery."*

**The red flag — what to reject for.** Any healthcare AI vendor without a BAA. Any financial-services AI vendor without an SR 11-7 mapping. Any defense AI vendor without a FedRAMP authorization at the required impact level or a documented IL5 path. Any vendor in any of these sectors claiming "horizontal" capability without the sectoral artifact — horizontal vendors are not wrong, they are early, and you are not the customer who pays for them to get late.

**Current landscape.** Healthcare: Abridge, Suki, Nuance DAX, and Augmedix are clean on the ambient-scribe pattern. Hippocratic AI is the leader on full clinical-agent posture and ships the HITRUST, BAA, and Minimum Necessary artifacts in usable form. OpenEvidence, Glass Health, and Hyro vary. Financial services: Harvey is competent at the legal-services edge of finance (deal documents, regulatory research). Rogo is the NYC-native financial-vertical agent with the cleanest sell-side posture; their SR 11-7 narrative is developing and worth pushing on during pilot. Hebbia operates in financial services with knowledge-worker posture rather than action posture, which simplifies their regulatory burden. The horizontal vendors (Sierra, Decagon, Glean) operate in regulated sectors as tenants of customer compliance, which works for read-dominant workflows and breaks down for action-dominant ones. Defense: Anthropic ships through Palantir for defense-adjacent workloads; OpenAI through Microsoft Azure Government. Scale AI's evolution post-Meta-investment shifted the defense-AI vendor map through 2024 and 2025. There is no clean independent defense-AI vendor in the agent layer as of May 2026; the procurement question is which prime contractor's AI subsystem you are buying, and the BAA / FedRAMP / ITAR posture follows from the prime.

---

### Chapter III.8 — Per-Trajectory FinOps Module

**Plain English.** A per-trajectory FinOps module is the buyer-side discipline of measuring, attributing, and re-routing the dollar cost of every agent trajectory — every multi-step sequence of model calls, sub-agent invocations, and tool calls a single task triggers — at the line-item level. It is the AI-era equivalent of cloud FinOps, except that the unit of consumption is not a CPU-second or a GB-month but a trajectory, and the trajectory is composed of fan-out calls the buyer cannot see without instrumentation. A 2026 agent procurement that does not include per-trajectory cost telemetry is a 2026 agent procurement that will surprise the CFO mid-year. This overlay sits beside the other seven because it is the only one that bites against the cloud bill rather than the security or governance posture, and Enterprise Architecture and FP&A — not InfoSec — are the counterparties who own it.

**Why it matters now.** Two events through Q1 2026 made per-trajectory FinOps a procurement question rather than a developer-tooling concern. First, Anthropic shipped the Claude Agent SDK 2.0 in April 2026 with a per-trajectory billing console — the "trace cost" view — that lets a buyer see, for the first time, the dollar cost of a single 47-call agent trace as a line item. Second, OpenAI's Responses API exposed parallel per-trajectory billing at roughly the same time. Together, the two changes converted a category of cost that previously hid inside vendor COGS into a category the buyer can audit and the vendor can be asked to disclose. The economics underneath the disclosure are large: at $1M+ annual AI spend, a planner-executor split that routes 80% of trajectory steps to a cheaper-tier model (Sonnet, GPT-4-mini, Gemini Flash) instead of running the entire trajectory at Opus / GPT-4 / Gemini Pro produces savings of 30–60% on multi-hop workloads. The advisory window is bounded: AWS Bedrock auto-routing of planner-executor splits is expected to ship in production form by H2 2027, which will absorb most of the explicit-FinOps surface into runtime defaults. Through that 12–18 month window, per-trajectory FinOps is a live procurement lever and a live margin lever; after the window closes, it becomes a hyperscaler default.

**The buyer-side question.** The Enterprise Architect and the FP&A lead will ask, jointly: *"Show me per-trajectory cost telemetry for this agent across our top ten use cases, broken out by model tier, sub-agent, and tool call. For each trajectory class, name the dollar cost at p50, p90, and p99. Show me the planner-executor split if any. Show me the cost-per-resolved-outcome at our projected volume, stress-tested for a 3x usage spike and a 20% foundation-model price increase. Show me the budget cap and the renegotiation trigger when we hit it."*

**The vendor-side artifact.** A Per-Trajectory Cost Disclosure Document and a live cost-telemetry feed. Disclosure document: per use-case trajectory taxonomy, per-class cost distribution at p50/p90/p99, planner-executor split documentation, foundation-model passthrough margin if any, and the cost-attribution methodology. Live feed: per-trajectory cost as a metric exposed via OpenTelemetry GenAI conventions or an equivalent vendor API, integrated into the buyer's observability pipeline. Refresh: monthly minimum on the disclosure document; continuous on the live feed. Format: machine-readable for the buyer's FinOps tooling.

**Sample contract language.** *"Vendor shall expose per-trajectory cost telemetry to Customer via the OpenTelemetry GenAI conventions or an equivalent documented API, including, per Agent invocation: (a) the dollar cost of foundation-model inference, broken out by model tier and sub-agent role; (b) the dollar cost of any third-party tool, telephony, or infrastructure call attributable to the trajectory; (c) the trajectory identifier sufficient to trace the call chain in Vendor's system. Vendor shall maintain and provide to Customer, on a monthly basis, a Per-Trajectory Cost Disclosure Document covering Customer's top ten trajectory classes by volume, including p50, p90, and p99 cost distributions. Vendor's foundation-model passthrough shall be billed at no more than [110%] of Vendor's documented unit cost from the underlying model provider, with annual audit rights. Customer shall have the right to renegotiate the unit-economics floor at any quarter in which actual per-trajectory cost exceeds the disclosed p99 by more than [25%]."*

**The red flag — what to reject for.** Any vendor whose answer is "we charge per resolved conversation, the trajectory cost is our problem." That answer is fine until the vendor's gross margin compresses and the renegotiation lands at your door. Any vendor refusing to expose per-trajectory cost telemetry through any interface. Any vendor running every step of every trajectory at the highest model tier — that is the canonical 30–60% margin leak and it will surface as a cost surprise within two quarters. Any vendor whose pricing-model allows foundation-model price increases to pass through unbounded — the right structure is a cap, an audit hook, and a renegotiation trigger. Any vendor whose answer is "we do not disclose inference cost as a category." That answer is the 22% inference-fraction-vs-2.50-charged math from the Sierra back-of-envelope, and your CFO is going to find it eventually.

**Current landscape.** Anthropic's Claude Agent SDK 2.0 (April 2026) and OpenAI's Responses API are the upstream enabling primitives. Sierra has resisted per-trajectory cost transparency at the contract level because the per-resolution pricing model depends on the inference-fraction asymmetry; expect resistance, push anyway. Decagon has partially complied on Tier-1 deals through Q1 2026 — that is the precedent to cite when negotiating. Cresta and Gong AI Studio bolt cost telemetry onto per-seat platforms; the data is available but you have to ask. Glean exposes per-query cost with reasonable transparency, which is consistent with the read-dominant posture. Harvey, Rogo, and Hebbia run per-seat pricing where the trajectory question is less load-bearing — but the moment any of them adds an outcome-tied module, the disclosure question reactivates. The hyperscaler offers (AWS Bedrock, Azure OpenAI, Google Vertex) are the cleanest at-source disclosure; they are also the providers most likely to absorb the FinOps surface into runtime defaults by H2 2027 — buy the advisory window now while it exists. The agent-observability platforms (Braintrust, LangSmith, Galileo, Helicone, Langfuse) ship per-trajectory cost as a first-class metric and are the right buyer-side instrumentation tier for any F1000 spending more than $500K/year on agent vendors.

---

### Closing flag — the (7, J+M) accident-of-light surface

One observation worth flagging at the close of Section III, not as a chapter but as a follow-on consideration for the Playbook companion vector. The seven counterparties × eight Job-phase-map columns produce a 56-cell coordinate system. One cell that lights up under load is (7, J+M) — Enterprise Architecture across the *Modify* and *Monitor* phases of the procurement-seam workflow itself. Trajectory-grade enablement coaching for the procurement counterparties — the buyer-side InfoSec, AI Council, and EA staff who actually run the seven overlays in flight against named vendors — is the surface that emerges when you compose this Playbook with the operational reality of running it inside an F1000. It is not a chapter in this edition. It is the natural next-edition companion: a coaching curriculum for the procurement-seam operator, structured trajectory-by-trajectory against the seven overlays and the fourteen-plus-one addenda. Flagging it here so the next-edition scope is on the record.

---

## Section IV · The 15 AI-Specific Addenda (with sample contract language)

Section III defined the seven (now eight) procurement controls that exist because the vendor is shipping an agent and not a SaaS. Section IV is the contractual surface where those controls bind. The fourteen addenda below — plus a fifteenth on outcome-definition mechanics — hardened into the F1000 buyer-side AI template between Q4 2024 and Q2 2026 in response to a specific event chain: Bartz v. Anthropic, Tremblay v. OpenAI, the Air Canada chatbot ruling, the Italian Garante's ChatGPT order, the EU AI Act passage and August 2025 GPAI obligations, the Microsoft Copilot Studio prompt-injection demos, the EchoLeak class disclosures, the GPT-4-to-Turbo silent-update fallout, the Claude 3.5→3.6→3.7 sequence, the CrowdStrike outage of July 2024, NYC Local Law 144 effective July 2023, the Colorado AI Act effective February 2026, and the Anthropic Claude Agent SDK 2.0 / OpenAI Responses API per-trajectory billing exposure of April 2026. Each addendum names the precedent that drove it, the counterparty owner, the vendor response patterns observed in the field, and the risk if the vendor refuses. Use the sample language as a drafting starting point; do not adopt verbatim without your GC's review. Close with the three sectoral overlays (FSI, healthcare, defense/government) that attach on top.

---

### Addendum #1 — Training-data rights · No training on customer data

**Verbatim sample contract language.** *"Vendor shall not use Customer Data, including prompts, completions, embeddings, or any derivative thereof, to train, fine-tune, or improve any Vendor or third-party model, without Customer's prior written consent on a per-use-case basis. This restriction shall apply to all sub-processors of Vendor, including foundation-model providers, and Vendor shall flow this restriction down through all sub-processor agreements. Vendor shall provide annual written attestation of compliance and shall maintain audit rights permitting Customer to verify compliance no more than once per year and as reasonably necessary following a Security Incident."*

**Why it emerged.** Bartz v. Anthropic (filed 2024, settlement framework $1.5B aggregate through 2025) and Tremblay v. OpenAI (June 2024) crystallized the training-data exposure category at billion-dollar scale. The consolidated authors' suits and the NYT v. OpenAI proceedings made the training-rights ambiguity in 2022–2023 vendor templates into a litigated category by 2025. The April 2026 Bartz preliminary injunction (N.D. Cal.) cited output-ownership ambiguity in enterprise contracts as a contributing factor; OpenAI Enterprise and Anthropic Enterprise both updated MSAs in Q1 2026 in response.

**Owner.** Legal (commercial counsel) + Privacy.

**Vendor response patterns.** Compliant by default at OpenAI Enterprise, Anthropic Enterprise / Workspace, AWS Bedrock, Azure OpenAI, Google Vertex, Glean, Sierra, Harvey enterprise SKUs. Negotiated at smaller vendors who want fine-tuning rights in exchange for pricing concessions. Refused at data-monetizing vendors — refusal is the signal that the vendor's business model depends on customer-data ingestion, and the buyer should treat that as disqualifying for any deployment touching MNPI, PII, or proprietary corpora.

**Risk if vendor refuses.** Deal-killer at F1000. Also a Bartz-class litigation exposure if the buyer signs around the clause and the vendor's training pipeline is later subpoenaed.

---

### Addendum #2 — Output ownership clarity

**Verbatim sample contract language.** *"As between the parties, Customer owns all Outputs generated by the Service in response to Customer prompts and Customer Data, subject only to Vendor's underlying intellectual property in the Service itself. Vendor hereby assigns to Customer any rights it may otherwise have in such Outputs. Vendor shall indemnify Customer against any third-party claim that an Output, as generated and delivered by the Service, infringes a third-party copyright, trademark, or trade secret, subject to the indemnity stack set out in the Master Agreement."*

**Why it emerged.** Getty v. Stability AI (2023–2025), the consolidated music-industry suits against major model providers (2024–2026), and the NYT v. OpenAI proceedings made output-ownership ambiguity a litigated category. Default vendor templates pre-2024 assumed buyer ownership of inputs and joint or vendor ownership of outputs — wrong for almost every enterprise use case. The Bartz preliminary injunction (April 2026, N.D. Cal.) cited output-ownership ambiguity in enterprise contracts as a contributing factor in the underlying claim posture.

**Owner.** Legal (IP counsel).

**Vendor response patterns.** Compliant by default at every credible enterprise vendor as of Q2 2026 — OpenAI Enterprise, Anthropic Enterprise, AWS Bedrock, Sierra, Decagon, Harvey, Hippocratic. The negotiation friction has moved to the indemnity-stack question (Addendum #4), not to the ownership question. Resistance now is a signal of a small or pre-enterprise vendor that has not updated its template; push and they will fold.

**Risk if vendor refuses.** Deal-killer. Also a third-party-IP-claim exposure if the vendor's training-data provenance is contested and the buyer holds no indemnity.

---

### Addendum #3 — Model-update notification and pinning rights

**Verbatim sample contract language.** *"Vendor shall provide no less than thirty (30) days advance written notice of any material change to the underlying foundation model powering the Service, including a model version upgrade, a model provider change, or a system-prompt change materially affecting Output behavior. Customer shall have the right to pin the Service to the prior model version for not less than ninety (90) days following such notice, and shall have the right to refuse the model swap with prorated refund of prepaid fees if Customer's good-faith re-evaluation demonstrates a material regression in Service behavior against Customer's representative test cases."*

**Why it emerged.** OpenAI's March 2025 GPT-4 to GPT-4-Turbo silent swap produced downstream prompt-tuning regressions for a subset of customers; the Anthropic Claude 3.5 → 3.6 → 3.7 sequence through 2024–2025 produced parallel behavior drift; Anthropic's April 2025 Responsible Scaling Policy-driven Sonnet update made the pattern repeatable. Model deprecation became a procurement event through 2024–2026: GPT-3.5 deprecated mid-2024, Claude 1 and 2 by end of 2024, multiple Claude 3 family endpoints retired through 2025, Gemini 1.5 family rotated through 2025.

**Owner.** Legal + AI Governance Council.

**Vendor response patterns.** Increasingly compliant at OpenAI Enterprise (30–60 day notice), Anthropic Enterprise (90 day notice on major versions), AWS Bedrock, Azure OpenAI. Resistance from vendors fully dependent on a single foundation-model provider who cannot themselves pin upstream. Harvey, Hippocratic, and Sierra ship some version of model-pin disclosure but not all of them grant the right-to-refuse with prorated refund; that is the negotiating leverage.

**Risk if vendor refuses.** Hard reject from AI Council in regulated industries (FSI, healthcare, defense). Also material exposure if a model swap mid-deployment changes Article 14 oversight surface or invalidates a signed eval report.

---

### Addendum #4 — Hallucination indemnity caps and carve-outs

**Verbatim sample contract language.** *"Vendor shall indemnify Customer for damages from materially inaccurate Outputs reasonably relied upon by Customer in production, including damages arising from third-party reliance on such Outputs in the ordinary course of Customer's business. This indemnity shall be capped at two (2) times the trailing twelve-month fees paid under this Agreement and shall not be subject to the general liability cap. The indemnity shall exclude damages caused by Customer's misuse of the Service materially contrary to Vendor's documented use guidelines."*

**Why it emerged.** Moffatt v. Air Canada (BC CRT, February 2024) — the airline was held bound by its chatbot's hallucinated bereavement-refund policy, and the "chatbot is a separate legal entity" theory failed. The ruling crystallized hallucination as a category of liability the deploying party holds absent specific contract language. Through 2024 and 2025 the F1000 GC view consolidated: insert the indemnity, do not rely on disclaimer.

**Owner.** Legal (litigation counsel).

**Vendor response patterns.** Negotiated. Landing zone in Q2 2026 is 1–2x ARR carve-out separate from the general cap, with misuse exclusions and a cure-period for inaccuracies disclosed in vendor documentation. Sierra, Decagon, Cresta carry $5M+ aggregate liability terms in F500 master agreements; this is the precedent to cite.

**Risk if vendor refuses.** GC blocks. Deal renegotiated at smaller scope or moves to a per-use-case carve-out structure rather than aggregate.

---

### Addendum #5 — Agent-action liability allocation

**Verbatim sample contract language.** *"For Outputs that constitute autonomous Actions taken by the Service on systems or data outside the Service's tenancy — including without limitation sending external email, posting to a customer-facing channel, charging a payment instrument, executing a financial transaction, modifying a system of record, granting access, or making external API calls on Customer's behalf — Vendor's indemnity shall extend to three (3) times the trailing twelve-month fees paid under this Agreement, separately capped from the general liability cap and from the hallucination-indemnity cap. The indemnity shall apply where the Action is taken without prior human approval consistent with Vendor's documented Tool-Boundary Policy and Action-Rollback Procedure."*

**Why it emerged.** Sierra and Decagon production deployments through 2024–2026 produced the first wave of autonomous-agent incidents in the field — mass-mailer over-sends, refund cascades, unauthorized scope grants — that legal teams could trace to a specific contractual gap. The Air Canada precedent extended naturally: if the chatbot's *output* binds the company, the agent's *action* binds the company harder. Through 2025 the agent-action category became a board-level concern at F1000 with non-trivial autonomous deployments.

**Owner.** Legal + InfoSec.

**Vendor response patterns.** Negotiated. Vendors push back hard on the definition of "autonomous" — the negotiating wedge is to tie the definition to the vendor's own Tool-Boundary Policy (Overlay #1) and Action-Rollback Procedure (Overlay #3). Sierra and Decagon will carry the indemnity if the autonomous-tier action surface is documented; refusal correlates with vendors who have not done the documentation work.

**Risk if vendor refuses.** Deal-killer for any high-autonomy use case. EU AI Act Article 14 enforcement (late 2026 onward) hardens this position — autonomous-tier actions on high-risk categories require human-oversight clauses by regulation, and the indemnity is the contractual mirror.

---

### Addendum #6 — Sub-processor consent for foundation-model providers

**Verbatim sample contract language.** *"Vendor shall maintain a current and publicly accessible list of all sub-processors used in the provision of the Service, including all foundation-model providers, and shall identify the categories of Customer Data flowing to each. Vendor shall provide Customer no less than thirty (30) days advance notice of any addition, removal, or material change in scope of any sub-processor, including any change in foundation-model provider. Customer shall have the right to object to a proposed sub-processor change on reasonable grounds (including data-residency, regulatory, or competitive concerns) and, if the parties cannot resolve the objection within sixty (60) days, to terminate this Agreement without penalty and recover prepaid fees on a prorated basis."*

**Why it emerged.** Schrems II (2020) and the ongoing US-EU data-flow contestation through the EU-US Data Privacy Framework (2023). The Italian Garante's ChatGPT order (March 2023) made foundation-model data residency a regulatory event. Through 2024–2026 the foundation-model sub-processor question hardened into the standard DPA template question; vendor refusal to disclose the foundation-model provider became a Privacy review fail.

**Owner.** Privacy + Legal.

**Vendor response patterns.** Compliant by default on disclosure. The contested element is the right-to-object — vendors push for "notice only," buyers push for "object with termination right." Landing zone in Q2 2026 is notice plus a reasonable-grounds objection right with a defined cure period.

**Risk if vendor refuses.** Deal-killer. Privacy review fail. DPA cannot be executed.

---

### Addendum #7 — Kill-switch and immediate-shutdown rights

**Verbatim sample contract language.** *"Customer shall have the right to immediately disable the Service, or any specific Agent, sub-agent, tool, or capability thereof, via a defined interface available to Customer's authorized administrators twenty-four hours a day, seven days a week. The disable action shall require no remediation period, no Vendor consent, and no support-ticket process. Vendor shall test the disable interface no less frequently than quarterly and shall report test results to Customer. Vendor shall not charge Customer fees for the duration of any Customer-initiated disable period."*

**Why it emerged.** Microsoft Tay (2016, the original kill-switch lesson). Bing chatbot (February 2023). Air Canada (February 2024). Through 2024–2025 the F1000 InfoSec view consolidated: the kill-switch must be in the buyer's hands or in a documented automated path. A kill-switch that requires opening a support ticket is not a kill-switch.

**Owner.** InfoSec + Enterprise Architecture.

**Vendor response patterns.** Compliant in principle at every credible enterprise vendor. The variation is in the interface — some vendors expose a console toggle, some expose an API, some require a support call within an SLA. Push for a console toggle plus an API and quarterly testing.

**Risk if vendor refuses.** Deal-killer. Also a regulatory exposure under EU AI Act Article 14 and most sectoral regimes.

---

### Addendum #8 — Eval-report sharing on a defined cadence (the Bet #1 wedge)

**Verbatim sample contract language.** *"Vendor shall deliver to Customer, on a quarterly basis and within thirty (30) days of any model-version change affecting the Service, a Signed Reproducible Evaluation Report covering performance on a defined set of Agent tasks representative of Customer's deployment. The Report shall specify: (a) the model identifier; (b) the dataset identifier and cryptographic hash; (c) the harness version; (d) the metrics, methodology, and confidence intervals; (e) reproduction instructions sufficient for Customer's team to independently re-run the evaluation. The Report shall be signed by a named Vendor representative and dated. A reproduction by Customer's team yielding a score outside five (5) points of the Report's stated score shall constitute a material breach of the eval-evidence warranty."*

**Why it emerged.** AI Governance Council formalization across F1000 in 2024–2025. NIST AI RMF GenAI Profile (July 2024). The procurement-readiness gap: every vendor produced internal benchmarks, none were buyer-reproducible, none survived a regulator subpoena. The Bartz settlement framework and the NYT v. OpenAI proceedings made "what did you know and when did you know it about your model's behavior on this class of input" a litigated question.

**Owner.** AI Governance Council (with Legal and InfoSec as co-signers).

**Vendor response patterns.** Few vendors ship turnkey today. Anthropic publishes responsible-disclosure-style model cards; OpenAI does the same; neither yet ships a turnkey signed report tied to a buyer's specific deployment. Harvey publishes legal-benchmark performance with reproducibility hooks; Hippocratic publishes clinical-task evals with the right methodological discipline; Sierra reports outcome-based metrics that translate poorly to a regulator subpoena framing; Decagon and Glean lag.

**Risk if vendor refuses.** AI Council blocks for any high-risk use case. This is the load-bearing Bet #1 wedge — the canonical buyer-side standard for signed reproducible eval reports does not yet exist, and the first credible publisher will set the procurement default for the next five years.

---

### Addendum #9 — Red-team frequency and reporting

**Verbatim sample contract language.** *"Vendor shall conduct adaptive-adversary red-teaming of the Service no less frequently than annually, and shall conduct an additional red-team within sixty (60) days following any material model update or system-prompt change. Each red-team shall be conducted by a named external red-team partner or by a credible internal team with external attestation. Vendor shall share with Customer the methodology, scope, findings, and remediation status of each red-team within thirty (30) days of completion. Discovery of a critical vulnerability (defined as enabling unauthorized data exfiltration, unauthorized action, or privilege escalation) shall constitute a Security Incident requiring notification to Customer within forty-eight (48) hours."*

**Why it emerged.** EU AI Act passage (March 2024) made red-teaming a regulatory expectation. The Microsoft Copilot Studio prompt-injection demos at Black Hat 2024 and the EchoLeak class disclosures through 2025 made the threat surface concrete. NIST AI RMF GenAI Profile (July 2024) formalized red-team frequency expectations. The pattern through 2024–2026: vendors who could cite a named external red-team partner closed faster; vendors who self-assessed lost InfoSec battles.

**Owner.** AI Governance Council + InfoSec.

**Vendor response patterns.** Anthropic and OpenAI ship public summaries of frontier red-team work; vertical-agent vendors are uneven. Sierra, Decagon, and Harvey partner with red-team specialists (Lakera Red, Robust Intelligence, HiddenLayer); the partnership is preferable to internal-only because conflict-of-interest is real when the vendor grades its own homework. Refusal to name the red-team partner is the rejection signal.

**Risk if vendor refuses.** AI Council blocks for any regulated use case. Also material exposure under EU AI Act Article 15 (accuracy, robustness, cybersecurity).

---

### Addendum #10 — Indirect-prompt-injection defense attestation

**Verbatim sample contract language.** *"Vendor shall maintain an annual attestation of the Service's defenses against indirect prompt injection, including: (a) the documented threat model; (b) the mitigation design (input filtering, output validation, tool-level isolation, planning-context tainting); (c) test results against an adaptive-adversary test suite, with success rates disclosed honestly against tool returns, retrieved document context, and multi-turn injection sequences; (d) the kill-switch procedure and the buyer-notification SLA when a new injection class is discovered. Vendor shall provide the attestation to Customer no less frequently than annually, and shall update it within thirty (30) days following the discovery of any injection class against which the Service's defense rate falls below sixty percent (60%)."*

**Why it emerged.** Microsoft Copilot Studio prompt-injection demos at Black Hat 2024. EchoLeak class disclosures through 2025. The 2024–2026 recognition that public-corpus benchmarks (95%+ scores) and adaptive-adversary methodology (60–80% honest success rates) are different categories of evidence and should not be conflated.

**Owner.** InfoSec.

**Vendor response patterns.** Few vendors ship turnkey attestations. Lakera publishes the most honest disclosure in the category; Robust Intelligence sells more broadly; HiddenLayer is improving on the model-supply-chain side. Anthropic and OpenAI publish responsible-disclosure timelines but do not yet ship turnkey attestations tied to buyer deployments. Vertical-agent vendors are emerging.

**Risk if vendor refuses.** InfoSec blocks for any agent ingesting external content — which is most agents in production. Also a board-level exposure once the first F500 indirect-injection breach surfaces in the press.

---

### Addendum #11 — EU AI Act Article 14 human-oversight conformance

**Verbatim sample contract language.** *"For any deployment of the Service that constitutes a 'high-risk AI system' under EU AI Act Annex III as applied to Customer's use case, Vendor shall provide and maintain documentation supporting human-oversight conformance under Article 14 of Regulation (EU) 2024/1689, including: (a) an oversight-design specification mapping each Article 14 sub-requirement to a Service feature; (b) operator-training materials sufficient for Customer's authorized operators to exercise meaningful oversight; (c) a Fundamental Rights Impact Assessment (FRIA) template completed for Customer's deployment; (d) refresh procedures upon any material change to the Service. Vendor warrants that the documentation, taken together with the supporting evidence, is sufficient to support Customer's good-faith demonstration of Article 14 compliance for Customer's deployment."*

**Why it emerged.** EU AI Act passage (March 2024). GPAI obligations in force August 2025. Article 14 implementation guidance to draft April 2026. First enforcement actions expected late 2026 or Q1 2027. Through 2026 the Article 14 tie-out became the most-actionable near-term regulatory lever in the AI procurement stack.

**Owner.** AI Governance Council + Legal + Privacy.

**Vendor response patterns.** Rare compliant. The Article 14 tie-out is the second Bet #1 wedge alongside the signed eval report — both are categories where the buyer-side standard does not yet exist and the first credible publisher will set the default. Mistral, Anthropic, OpenAI publish adjacent material (Responsible Scaling Policy, Preparedness Framework) that translates with effort. Hippocratic and Harvey publish vertical-specific human-oversight design that maps to Article 14 in regulated workflows.

**Risk if vendor refuses.** Deal-killer in EU-exposed F1000 from August 2026 onward. Also material litigation exposure as the first enforcement actions land.

---

### Addendum #12 — Data residency for inference (region-pinning)

**Verbatim sample contract language.** *"Vendor shall provide an option, available to Customer at contract execution and continuing throughout the Term, for inference processing to occur exclusively within a specified jurisdictional region (including without limitation the European Union, the United States, the United Kingdom, or a sovereign-cloud region nominated by Customer). The region-pinned option shall encompass all foundation-model calls, prompt processing, output generation, persistent memory, and audit-log retention. Vendor shall provide annual written attestation that no Customer Data has crossed the specified region boundary during the attestation period."*

**Why it emerged.** Schrems II (2020). EU-US Data Privacy Framework contestation (2023 onward). Italian Garante's ChatGPT order (March 2023). Sovereign-cloud demands from EU governments and financial regulators through 2024–2026. The 2025 wave of EU FSI buyers requiring region-pinned inference as a condition of pilot contracts.

**Owner.** Privacy + Enterprise Architecture.

**Vendor response patterns.** Compliant at AWS Bedrock (EU regions), Azure OpenAI (EU, UK, regional sovereign), Google Vertex (EU). Mistral is sovereign by default. Rare at vertical-agent vendors who use single-region foundation-model providers without an EU passthrough. Sierra, Decagon, Harvey, and Hippocratic are improving but heterogeneous. Vertical vendors who use OpenAI-only or Anthropic-only inference need to demonstrate EU-region passthrough at the upstream provider; many do not.

**Risk if vendor refuses.** Deal-killer in EU and in regulated US sectors. Also material exposure under GDPR Articles 44–49 (international transfers).

---

### Addendum #13 — Audit-log retention and customer access

**Verbatim sample contract language.** *"Vendor shall maintain tamper-evident audit logs of all Agent trajectories, sub-agent invocations, tool invocations, and Outputs for a period of seven (7) years from the date of generation. Vendor shall provide Customer continuous read-access to such logs via a defined interface, in a format suitable for ingestion into Customer's Security Information and Event Management (SIEM) system, including the OpenTelemetry GenAI conventions or an equivalent documented schema. Vendor shall not modify, delete, or otherwise alter logs prior to the expiration of the retention period without Customer's prior written consent. Loss or corruption of logs prior to retention expiration shall constitute a material breach."*

**Why it emerged.** SR 11-7 (Federal Reserve model risk management, 2011, applied by analogy to AI agents through 2024–2026). SOX. HIPAA Security Rule. FINRA Rule 4511. The post-CrowdStrike (July 2024) elevation of observability as a board-level concern. Through 2025–2026 the seven-year retention floor became the F1000 default for any agent touching financial systems, PHI, or regulated communications.

**Owner.** InfoSec + GRC + Legal.

**Vendor response patterns.** Compliant for log generation at most enterprise vendors. The contested elements are retention duration (vendors push for shorter) and tamper-evidence (vendors push for "we won't change them" rather than cryptographic guarantees). Push for tamper-evident with cryptographic chaining or an immutable storage tier. Sierra, Decagon, and Glean have improved retention discipline through 2025; Hebbia and Rogo carry the cleanest log posture in financial services.

**Risk if vendor refuses.** Deal-killer in regulated industries. Also material exposure under SOX (financial reporting) and SR 11-7 (model governance).

---

### Addendum #14 — Sub-agent privilege-separation attestation

**Verbatim sample contract language.** *"For deployments involving sub-agents (defined as any specialized agent invoked by an orchestrator agent for a bounded role including planning, executing, verifying, escalating, or memory writing), Vendor shall maintain and provide to Customer an annual attestation of the privilege-separation design, including: (a) least-privilege scoping of each sub-agent's tool access; (b) credential inheritance and delegation mechanism (capability tokens, signed delegation, or equivalent); (c) cross-tenant isolation; (d) test cases for cross-sub-agent privilege escalation, with results. Material changes to the sub-agent privilege matrix shall be communicated to Customer no less than thirty (30) days before production deployment."*

**Why it emerged.** The 2024–2025 architectural transition from single-agent ReAct loops to planner-executor and multi-sub-agent architectures. The pattern of agent fan-out incidents in production through 2025. Anthropic, OpenAI, and Google sub-agent risk publications through 2024–2026. The recognition that an injection into a planner sub-agent propagates downstream into every executor sub-agent that shares context.

**Owner.** InfoSec + Enterprise Architecture + AI Governance Council.

**Vendor response patterns.** Rare turnkey. Anthropic's sub-agent / tool-use patterns are the cleanest public reference; OpenAI similar. Sierra and Decagon operate multi-agent architectures with named privilege boundaries internally; Sierra's is the most willing to be documented for buyer review. The general-purpose autonomous-coding-agent category (Cognition/Devin and peers) is the weakest. Agent-building frameworks (LangGraph, CrewAI, AutoGen, Letta) document patterns but do not enforce; the enforcement burden falls on the vendor or buyer.

**Risk if vendor refuses.** AI Council and InfoSec block. Also material blast-radius exposure when an indirect-injection event materializes against the planner sub-agent.

---

### Addendum #15 — Outcome-Definition Mechanics (new in 2026)

**Verbatim sample contract language.** *"For any pricing model in which Vendor's fee is calculated by reference to an Outcome (including without limitation a 'resolved conversation,' a 'completed task,' a 'successful escalation,' or any equivalent measurable result of Service operation), the parties shall maintain dual-telemetry of Outcome occurrence: (a) Vendor's telemetry shall be the source of truth for monthly billing; (b) Customer's independent telemetry shall serve as audit override, and material divergence (defined as exceeding [5%] of Outcome count in any month) shall trigger a mandatory reconciliation. Reconciliation disputes unresolved within thirty (30) days shall escalate to a sixty (60) day commercial discussion at Vendor's executive level. Disputes unresolved within ninety (90) days from initial divergence shall be submitted to a third-party arbitrator agreed in advance (the 'Outcome Arbitrator,' selected from a panel of Iron Mountain, KPMG, Deloitte, EY, or PwC AI advisory practices), whose determination shall be binding for the disputed billing period. Vendor shall expose per-trajectory cost and per-Outcome cost telemetry sufficient to support both parties' computation. Customer shall have the right to renegotiate the Outcome definition at the second annual renewal if cumulative dispute volume across the prior twelve months exceeds [10%] of total Outcomes billed."*

**Why it emerged.** Through 2025–2026 the F500 buyer entry into outcome-pricing — Sierra at $175M+ ARR (Q1 2026, trailing-12), Decagon $80M+, Hippocratic AI $9/hour RN-equivalent, Abridge $3–8 per encounter — outpaced the measurement-and-dispute mechanics. Two F500 buyers (a US bank and an EU airline, off-record at the Procurement Leaders AI Summit, April 2026) reported 8–15% outcome-count disputes in early-quarter resolution, settled by negotiation rather than contract mechanism. Sierra's master template defines "resolved" via CSAT threshold + 7-day no-return-contact window — contested by regulated buyers where a complaint at day 14 against a "resolved" conversation is not in fact resolved. The category of outcome-definition arbitrage was a $50M+ leakage problem in F500 outcome-pricing contracts through 2025; no vendor turnkey-answers it; no buyer ships internal playbooks. Anthropic's Claude Agent SDK 2.0 (April 2026) and OpenAI's Responses API exposing per-trajectory cost in billing consoles gave the dual-telemetry mechanism its empirical teeth — for the first time, both parties can compute the underlying unit economics from independent vantage points.

**Owner.** Procurement (CPO + AI Category Manager) + CFO (specifically the SOX revenue-recognition lead, because outcome-pricing on an executory contract is now a rev-rec event under ASC 606 with non-trivial estimation risk).

**Vendor response patterns.** Sierra has resisted dual-telemetry at the contract level — the per-resolution pricing model depends on the inference-fraction asymmetry and the audit-only-after-the-fact posture. Decagon has partially complied on Tier-1 deals through Q1 2026; that is the precedent to cite. Cresta and Gong AI Studio (which run hybrid per-seat plus per-conversation) are more amenable because the outcome-tied module is a smaller fraction of total fees. Hippocratic AI is amenable because the per-hour-of-care unit is independently verifiable through clinical scheduling. Abridge is amenable because per-encounter is independently verifiable through the EHR. Push for dual-telemetry plus 30/60/90 dispute windows plus Outcome Arbitrator at the start; landing zone in Q2 2026 is dual-telemetry plus 60-day reconciliation plus mediation rather than binding arbitration, with a renegotiation right at the second annual renewal.

**Risk if vendor refuses.** Procurement blocks at F500. Also a SOX rev-rec exposure if the buyer accounts for outcome-pricing payables on the basis of vendor-reported counts that the buyer cannot independently verify. Also a CFO-level exposure if the dispute volume materializes mid-contract and there is no pre-agreed resolution mechanism — the 8–15% dispute pattern in early F500 outcome-pricing contracts is the empirical case. The asymmetric leverage point is procurement timing: insist on Addendum #15 before the pilot signs, because once the pilot has run for 90 days on vendor-defined telemetry, the vendor has the data anchor and the buyer does not.

---

### Sectoral Overlays — FSI, Healthcare, Defense/Government

The fifteen addenda above apply across sectors. The three regimes below add control-set overlays that bind in addition. Each adds 6–18 weeks to the procurement cycle on top of the base F1000 floor. Each surfaces a counterparty seat (model-risk in FSI, the BAA owner in healthcare, the program security officer in defense) that does not appear in the seven-counterparty base structure of Section II.

**Financial Services (NYDFS Part 500, SR 11-7, OCC model-risk guidance, FINRA, EU DORA).** Adds: SR 11-7-style model validation evidence; an independent model-validation report distinct from the vendor's internal eval; NYDFS 23 NYCRR 500 cybersecurity attestation; FINRA Rule 4511 audit-log retention floors (which interact with Addendum #13's seven-year requirement); DORA-aligned operational resilience for EU FSI; AML/sanctions-screening attestation if the agent touches onboarding workflows; OCC interpretation of SR 11-7 as applied to LLM-driven credit, suitability, and underwriting decisions through 2025–2026. The **Model-Risk Function** (reports to the CRO, distinct from the CISO and from the AI Governance Council) is a de facto eighth counterparty in FSI. Sample contractual hook: *"For any deployment in which the Service informs a credit, underwriting, suitability, or trading decision subject to SR 11-7, Vendor shall provide independent model-validation evidence prepared by a qualified third-party validator, refreshed annually, sufficient to support Customer's model-risk function in its own validation activity under the Federal Reserve's Model Risk Management guidance."* Cycle impact: add 8–16 weeks for model-validation review, longer for any non-trivial credit or trading workflow. Vendor landscape: Rogo and Hebbia carry the cleanest sell-side and knowledge-worker postures respectively; Harvey covers the legal-services edge of finance; the horizontal vendors operate as tenants of customer model-risk compliance.

**Healthcare (HIPAA, HITECH, ONC HTI-2 predictive-decision rules, OCR enforcement, FDA SaMD, HITRUST CSF v11.x).** Adds: BAA executed at signature; HIPAA Security Rule attestation; OCR-aligned breach-notification procedures with twenty-four-hour notification SLA on PHI-affecting incidents; if the agent makes clinical decisions, FDA Software-as-Medical-Device pathway documentation (typically 510(k) substantial-equivalence or De Novo); for predictive decision support, ONC HTI-2 transparency rules effective 2026 (algorithm transparency, source attribute disclosure); clinical-disparities bias audit; HITRUST CSF v11.x certification or readiness as the de facto procurement bar. Sample contractual hook: *"Vendor shall execute a Business Associate Agreement substantially in the form attached as Exhibit B. If the Service qualifies as Software as a Medical Device under 21 CFR 820 or equivalent FDA regulation, Vendor shall provide its 510(k), De Novo, or PMA documentation and shall maintain its FDA submission throughout the Term. Vendor shall maintain HITRUST CSF certification at level v11.x or higher and shall provide annual attestation."* Cycle impact: add 6–14 weeks for BAA negotiation and FDA pathway review; substantially longer for SaMD-classified workflows. Vendor landscape: Hippocratic AI ships HITRUST, BAA, and Minimum Necessary artifacts in usable form; Abridge, Suki, Nuance DAX, and Augmedix are clean on the ambient-scribe pattern; OpenEvidence, Glass Health, and Hyro vary.

**Defense / Government (FedRAMP Moderate / High, DoD IL4 / IL5 / IL6, CMMC Level 2 or 3, ITAR / EAR).** Adds: FedRAMP authorization at the relevant impact-level boundary (Moderate for most civilian agencies, High for sensitive workloads, IL5/IL6 for DoD); ATO from the sponsor agency; CMMC Level 2 or 3 for defense contractors handling controlled unclassified information; ITAR/EAR export controls applied to the model itself (relevant for any agent crossing dual-use thresholds under the October 2023 EO and January 2025 EO); sponsor-agency risk acceptance for emerging-tech use cases; supply-chain risk management plan including the foundation-model provider relationship. Sample contractual hook: *"Vendor warrants that the Service holds and shall maintain throughout the Term a FedRAMP authorization at the [Moderate/High/IL5] impact level appropriate to Customer's deployment, and that any change in authorization status shall be notified to Customer within seventy-two (72) hours. Vendor shall provide its CMMC Level 2 assessment and shall comply with all applicable ITAR/EAR controls on the underlying foundation model."* Cycle impact: total cycle 6–18 months end-to-end; FedRAMP authorization alone is 12–18 months from start, which means a vendor without a pre-existing authorization is effectively not procurable for a defense workload on any reasonable timeline. Vendor landscape: Anthropic ships through Palantir for defense-adjacent workloads; OpenAI through Microsoft Azure Government; Scale AI's evolution post-Meta-investment shifted the defense-AI vendor map through 2024–2025. There is no clean independent defense-AI vendor in the agent layer as of May 2026 — the procurement question is which prime contractor's AI subsystem you are buying, and the BAA / FedRAMP / ITAR posture follows from the prime.

---

*End Part B. The seven overlays plus per-trajectory FinOps (Section III) and the fifteen addenda plus three sectoral overlays (Section IV) form the procurement-control surface a 2026 F1000 buyer should bring to every agent vendor review. Part A delivers the Executive Foreword and the Six (or Seven) Counterparties; Part C delivers the Decision Tree, the Vendor Scoring Rubric, the Glossary, and the Appendix Contract Clauses. Together the three parts are the Playbook spine.*



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

The flag is planted. Reach me at alex.e.yedi@gmail.com.

*— Alex Yedi, May 2026*

