# The AI Vendor Procurement Playbook

**A Field Manual for F1000 Buyers of Agentic AI**
*Edition 1.0 · Spring 2026*
*Author: Alex Yedi · Companion to the Volume III Agent Layer Substrate*

---

## Part 1 — Structural Outline (Table of Contents)

### I. Executive Foreword
The moment we are in. Why this Playbook exists. Who it is for. How to read it. [Drafted in this document, Section I.]

### II. The Six Counterparties
One chapter each, written to the buyer-side approver who runs that lane and to the seller-side counterparty who has to satisfy them.

1. Chapter II.1 — InfoSec (CISO and team) → *see F5 draft*
2. Chapter II.2 — Legal (GC and Commercial Counsel) → *see F5 draft*
3. Chapter II.3 — Privacy (DPO / Privacy Counsel) → *see F5 draft*
4. Chapter II.4 — AI Governance (AI Council Chair / Chief AI Officer) → *see F5 draft*
5. Chapter II.5 — Procurement (CPO / Strategic Sourcing) → *see F5 draft*
6. Chapter II.6 — Business Sponsor (the line manager who actually wants the tool) → *see F5 draft*

### III. The Seven Agent-Specific Overlays
The seven controls that distinguish *agent* procurement from generic AI vendor procurement. One chapter each. [All seven drafted in Section III of this document.]

1. Chapter III.1 — Tool-Boundary Policy
2. Chapter III.2 — Indirect-Prompt-Injection Adaptive Red-Team
3. Chapter III.3 — Action-Rollback Documentation
4. Chapter III.4 — Sub-Agent Privilege Separation
5. Chapter III.5 — Signed Reproducible Eval Reports
6. Chapter III.6 — EU AI Act Article 14 Human-Oversight Tie-Out
7. Chapter III.7 — Sectoral Overlays (Healthcare, Financial Services, Defense)

### IV. The 14 AI-Specific Addenda — Sample Contract Language
Drop-in MSA addenda for the agent era. Training rights, output ownership, hallucination indemnity, agent-action liability, model-update notice, kill-switch, persistent-memory residency, sub-processor changes, eval-evidence freshness, EU AI Act tie-out warranty, indirect-injection red-team disclosure, action-rollback SLA, computer-use restrictions, deprecation notice. → *see F5 draft*

### V. The Decision Tree — Buy, Build, or Wait
A real branching decision tree. Specific to agent procurement. [Drafted in Section V of this document.]

### VI. The Vendor Scoring Rubric — Procurement Operating Standard 1.0
The named matrix. Uses the (Function, Capability) coordinate system from the Volume III substrate. [Outline + intro drafted in Section VI of this document. Full matrix populated in Wave 2.]

### VII. Glossary of Agent-Specific Terms
Thirty-eight terms a F1000 buyer needs to read a vendor SOC 2-plus-AI-addendum the same way they read a SOC 2. [Drafted in Section VII of this document.]

### VIII. Appendix — Reference Contract Clauses (MSA + DPA + AI Addendum)
Long-form sample language. → *see F5 draft*

---

## Part 2 — Section I · Executive Foreword

If you are a CIO, you are reading this because the AI agents your business sponsors are buying do not pass any of the procurement controls you built between 2014 and 2023. The SOC 2 your vendor proudly references covers their cloud posture. It does not cover the agent's tool-boundary policy. The DPA you signed in 2022 contemplates a vendor processing your data. It does not contemplate a vendor's agent writing into your system of record, taking an irreversible action, and being unable to roll it back. You are reading this because between the AI council you set up in 2024 and the vertical-agent vendor your CFO wants to sign next quarter, there is a gap that nobody in your organization is currently equipped to close. This Playbook closes it.

If you are a CISO, you are reading this because every red-team result a vendor has shown you is run against a public corpus and you cannot tell whether the 99% indirect-prompt-injection detection rate they cite is meaningful or marketing. It is marketing. The adaptive-adversary numbers, when vendors are willing to disclose them, sit between 60% and 80% — and even those are unstable across model versions. You are reading this because Bartz v. Anthropic (the May 2024 fair-use dismissal, the September 2024 reversal, the $1.5B class-settlement framework that crystallized through 2025) and the NYT v. OpenAI proceedings have already re-priced what training-rights and output-ownership clauses cost in dollar terms, and your peers are missing the analogous re-pricing happening on agent-action liability. This Playbook is how you stop missing it.

If you are an AI Council Chair, you are reading this because the EU AI Act Article 14 human-oversight implementation guidance went to draft in April 2026 and your General Counsel is asking you what it means for the sixty-two AI tools in flight across the business. The honest answer is that for most of those tools — the embedded copilots, the document QA assistants, the retrieval layers — Article 14 changes almost nothing. For the agents that take actions on your behalf, it changes the shape of every contract you have not yet signed. You are reading this because you need a way to separate the two and to write the second into your AI policy without having to re-read the Act twice a week.

If you are a Chief Procurement Officer, you are reading this because the cycle time from security questionnaire to AI Governance sign-off is now the single longest variable in your AI vendor close-time, your business sponsors are bypassing you when they can, and Vanta's AI Trust Center is good for compliance posture but does not substitute for the seven overlays. You need a standard that compresses cycle time without compressing rigor. The Playbook is that standard.

If you are a General Counsel, you are reading this because Air Canada (February 2024) established that a chatbot's output binds the company contractually. Colorado's AI Act (May 2024) established personal-injury exposure for high-risk AI decisions. The Bartz settlement framework established that training-data exposure is measured in billions. None of these reshape your existing vendor template. All three reshape the one you are about to sign with Sierra, Decagon, Glean, Harvey, Hippocratic, Augment, Hebbia, or Rogo. You are reading this because the fourteen addenda in Part IV are what you should be inserting into your MSA template before the next vertical-agent renewal.

This Playbook exists because no incumbent — not Vanta, not Drata, not Secureframe, not OneTrust, not the Big Four — currently ships a canonical, buyer-side, agent-specific procurement standard. There is a Wardley map of the AI agent stack on my desk that places every layer beneath the runtime (sandboxes, browsers, gateways, telephony, TTS) on a clean 24-month commoditization path and every layer above the runtime (eval, observability, guardrails, vertical workflow, procurement controls) at Custom-to-Genesis. Buyer-side procurement controls are the only piece of the picture sitting at Genesis with no flag planted in it. The window to plant the flag is the window before EU AI Act Article 14 enforcement starts in late 2026 and before Anthropic's ARR resolves at $24B or $30B in Q3 2026 and re-prices the entire vertical-agent valuation stack.

Read it in this order. If you are a CIO or AI Council Chair, start with Section V (Decision Tree). If you are a CISO, start with Section III (Seven Overlays). If you are a CPO, start with Section VI (Scoring Rubric) and Section II (Six Counterparties). If you are a GC, start with Section IV (Fourteen Addenda) and Section III.6 (Article 14 Tie-Out). The Glossary in Section VII is short because it has to be — you should be able to read every term twice and use them in a vendor call the same week.

The position this Playbook takes throughout is that agent procurement is not a more permissive SaaS procurement; it is a stricter one with new questions. Vendors will tell you the old questions still work with minor additions. They do not. The seven overlays are not nice-to-haves. They are the questions that separate agent vendors who can survive a regulator subpoena and a class action from agent vendors who will fold the first time a write action runs against the wrong row and a customer sues. Treat them that way.

---

## Part 3 — Section III · The Seven Agent-Specific Overlays

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

**Why it matters now.** Indirect prompt injection became the unsolved problem of the agent layer through 2024 and 2025. Public-corpus defenses (Lakera Guard, NeMo Guardrails, Promptfoo) cleared 95%+ on their own benchmarks; adaptive-adversary methodology — where the red team updates faster than the defense — clears 60–80% honestly. The gap is the dollar-exposure gap. Adam Raine's case against OpenAI in California court, the Air Canada chatbot ruling (February 2024) that held the airline liable for its bot's hallucinated refund policy, and the NYT v. OpenAI proceedings all crystallize the legal argument that the vendor is responsible for what the agent does in the presence of adversarial inputs. By 2026 the procurement question is not *whether* the agent has indirect-injection defense. It is whether the defense is adaptive, whether it is honestly disclosed, and whether the test methodology survives review.

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

## Part 4 — Section V · The Decision Tree (Buy, Build, or Wait)

This section is the procurement officer's decision aid. It is intentionally agent-specific. Generic SaaS decision trees do not produce the right answers because agent procurement asks questions SaaS procurement does not (autonomy scope, action reversibility, model deprecation, sub-agent privilege, EU AI Act Article 14 tie-out). Use this tree at the start of every agent-procurement cycle. Do not use it as a substitute for the seven overlays; use it as the framing that determines which overlays bite hardest.

### Branch 1 — Is the workload regulated?

If the workload is regulated under HIPAA, GLBA, FERPA, FINRA, NYDFS 500, SR 11-7, FedRAMP, CMMC, ITAR, GDPR's special-category data, or California CCPA/CPRA sensitive data, the answer is not "buy faster" or "build instead." The answer is: only consider vendors who ship the sectoral overlay packet from Chapter III.7 *before* you start the pilot. Roughly four out of five horizontal vendors will not pass this screen. That is correct behavior. The screen exists to keep them out.

If the workload is unregulated, proceed.

### Branch 2 — Is the data shareable with a foundation-model provider?

If the data flowing through the agent — prompts, context windows, persistent memory, tool returns — contains material non-public information (MNPI), pre-IPO financials, attorney-client-privileged material, customer PII, employee compensation data, or anything else that would create exposure if it reached a foundation-model provider's training set, then the procurement question collapses to: which deployment posture does the vendor support? You need one of: a no-training-rights commitment with audit, a private deployment (VPC, dedicated tenancy, customer-managed keys), or a sovereign-cloud option (AWS GovCloud, Azure Government, GCP Sovereign, or a regional EU option such as OVHcloud or Scaleway). Do not accept "we don't train on your data" without the contract language and the audit hook. The Bartz settlement framework is the reason — training-rights ambiguity is not a small contract issue any more.

If the data is shareable (public information, synthetic test data, or data the buyer is comfortable having ingested), proceed.

### Branch 3 — Is the agent taking irreversible actions?

If the agent's action surface includes any of: sending external email, posting to a customer-facing channel, charging a card, executing a financial transaction, modifying a system of record without versioning, deleting data, granting access, generating regulatory filings, or interacting with any third party on the buyer's behalf — then the procurement defaults change. You need: a written action-rollback document per write tool (Chapter III.3); a human-in-the-loop gate on every irreversible action; a kill-switch the buyer holds; and contractual language that makes the vendor co-liable when an irreversible action goes wrong outside the human gate. Pilot scope must not include irreversible actions in the first 30 days. Production deployment must not include irreversible actions in the first 90 days. This is conservative on paper. It is the right posture given current vendor-side maturity.

If the agent's action surface is read-only or reversible-only, proceed.

### Branch 4 — What is your fallback if the model is deprecated?

The single most-undertaught lesson of 2024–2026 is that frontier-model deprecation is now a procurement event. GPT-3.5 was deprecated mid-2024. Claude 1 and 2 deprecated by end of 2024. Multiple Claude 3 family endpoints were retired through 2025. Gemini 1.5 family rotated through 2025. The model your vendor pinned in their last eval report may not exist in twelve months. Ask: what is the model-pin-change notice? What is the re-eval procedure? What is the buyer's right to refuse a model swap that materially changes agent behavior? What is the deprecation indemnity?

If the vendor's answer is "we automatically upgrade you to the latest model," reject. That is not a fallback. That is a vendor's optimization at the buyer's risk. The right answer is a 90-day model-pin-change notice, a re-eval requirement before swap, and a contractual right to refuse with prorated refund.

### Branch 5 — Build or buy?

This is the branch where most procurement teams get the wrong answer.

You should *buy* when: (a) the workflow is generic enough that a vertical-agent vendor has solved it for the median buyer at a scale you cannot match; (b) the vendor's eval evidence is at parity with or better than what your internal team can produce; (c) the integration surface is bounded by a small number of MCP servers or first-party connectors; (d) the regulatory posture is a vendor contractual commitment, not your problem to construct.

You should *build* when: (a) the workflow is core to your differentiation and the agent's behavior encodes your proprietary judgment (the underwriting policy, the pricing model, the customer-segmentation logic); (b) the data flow is too sensitive to share with a third party even under no-training-rights commitments; (c) the orchestration touches more than five proprietary internal systems; (d) you have the engineering capacity to maintain it.

You should *partner* — the underestimated third option — when: (a) a vertical-agent vendor has 80% of what you need and you can co-build the 20% on their platform with shared IP terms; (b) you can negotiate operator-shaped terms (per-trajectory pricing, customer-owned eval data, exit clause for the proprietary 20%); (c) the partnership is structured as a 12-month pilot with explicit exit rights, not a five-year platform commitment. Most F1000 buyers should be partnering more and building less.

### Branch 6 — Buy now or wait six months?

This is the branch that the 2026 calendar makes urgent and that most procurement teams answer wrong by default.

Buy now if: (a) the EU AI Act Article 14 implementation timeline aligns with your enforcement calendar (Q4 2026 onward for EU operations); (b) the vendor's pricing reflects Q2 2026 market and you expect a Q3 2026 ARR-resolution-driven re-price upward; (c) the integration window in your IT roadmap is open now and not in twelve months; (d) the workflow's dollar-impact justifies non-optimized deployment.

Wait six months if: (a) AWS Bedrock auto-routing of planner-executor splits is expected by H2 2027 and you can fold per-trajectory cost optimization into the buy decision later; (b) Anthropic ARR resolves in Q3 2026 with a downside print ($24B rather than $30B) and you expect vertical-agent valuations to compress 20–30%, which will produce better contract terms; (c) the vendor's eval evidence is below the threshold from Chapter III.5 and you would be buying on a roadmap commitment rather than a signed report; (d) the regulatory posture is genuinely unsettled and the vendor's tie-out is conceptual rather than control-by-control. The asymmetry here is heavy: waiting costs you six months of value; buying wrong costs you a vendor-replacement project that will run twelve to eighteen months.

### Branch 7 — Pilot scope and exit-cost analysis

If you have answered the prior six branches and the answer is "pilot," structure the pilot so it does not trap you. Three rules.

*Rule one.* The 90-day pilot must touch fewer than three systems, must include zero irreversible actions in the first 30 days, must produce a signed reproducible eval report by day 60, and must conclude with a binary go/no-go gate by day 90 against criteria you wrote on day zero. Vendors will press for longer pilots and broader scope. Resist.

*Rule two.* The pilot contract must include exit terms with explicit data-portability obligations: any persistent memory the agent has accumulated about your business is yours, must be exportable in a documented format within 30 days of pilot termination, and must be deletable from vendor systems with a deletion confirmation log. Without these terms, you have not run a pilot. You have made an undisclosed long-term commitment.

*Rule three.* The pilot pricing must not anchor production pricing. Vendors price pilots aggressively (free, $25–50K) and then anchor production pricing against a fully-loaded base that includes counterfactuals the pilot never tested. Insist that production pricing be quoted at the start of the pilot, with a defensible per-trajectory or per-resolution unit-economics breakdown, and with a written right-to-renegotiate at the production-transition gate.

The 90-day pilot, the seven overlays, the four agent-specific MSA addenda from Section IV that bind on day one, and the production-pricing pre-quote together are the procurement equivalent of a forward-deployable arming switch. They let you commit conditionally while keeping the option to walk. Anything looser is a long-term commitment the vendor will eventually exercise against you.

---

## Part 5 — Section VI · The Vendor Scoring Rubric (Procurement Operating Standard 1.0) — Outline

The rubric is the named matrix this Playbook publishes. It scores each candidate vendor against eight axes (the Job 6 phase map: Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude) and seven overlays (Section III), producing a 56-cell coordinate system mappable onto the (Function, Capability) framework Alex's Volume III substrate uses. Each cell is scored 1–5 (vapor → signed evidence). A vendor below 3 average on the eight axes should not pass an F1000 AI Governance review as of May 2026; a vendor below 3 average on the seven overlays should not pass an InfoSec / AI Council joint review at all. The rubric is the input to the buyer-side leaderboard the Playbook maintains publicly and refreshes quarterly. The full matrix (rows × columns × scoring guidance × evidence catalog) is in the appendix; this Wave 1 draft delivers the intro and the structure. Wave 2 populates the cells across the named vendor set (Sierra, Decagon, Glean, Harvey, Hippocratic, Hebbia, Rogo, Augment, Clay, Mistral, Anthropic, OpenAI, and the regulated-vertical specialists) with the May 2026 read.

---

## Part 6 — Section VII · Glossary of Agent-Specific Terms

**Trajectory.** The complete sequence of an agent's reasoning steps, tool calls, sub-agent invocations, and final output for a single task. The trajectory — not the response — is the unit of evaluation and of cost.

**Planner-executor split.** An architectural pattern where a higher-capability model produces a plan and a lower-capability model executes the plan's individual steps. Dominant cost-optimization pattern of 2025–2026 and the architectural lever behind per-trajectory FinOps.

**MCP (Model Context Protocol).** Anthropic-originated open protocol for connecting LLMs to tools, data sources, and third-party services. Graduated to Linux Foundation governance December 2025. As of Q2 2026 the de facto interoperability spec, with experience-layer fragmentation across implementations.

**MCP server.** A process exposing tools to an MCP-compatible client. May be first-party (vendor-supplied) or third-party. Quality varies widely; first-party servers from Stripe, Linear, GitHub, Snowflake, and Databricks are the current quality benchmark.

**MCP gateway.** Control plane sitting between the agent and the MCP servers, handling auth, audit, rate-limiting, secret-injection, and policy enforcement. Cloudflare, Kong, and Pomerium are the durable incumbents.

**Sub-agent.** A specialized agent invoked by an orchestrator agent for a bounded role (planning, executing, verifying, escalating). Privilege separation between sub-agents is the agent-era equivalent of role-based access control.

**Tool-boundary policy.** The written, vendor-supplied document enumerating every tool an agent can invoke, the actions allowed, the privilege scopes, and the human-in-the-loop conditions. See Chapter III.1.

**Signed eval report.** An evaluation artifact tied to a specific model identifier, dataset hash, and harness version, signed by a named vendor representative, reproducible by the buyer within a stated tolerance. See Chapter III.5. As of May 2026 no vendor ships turnkey signed eval reports.

**Kill-switch.** Buyer-side mechanism to disable a tool, a sub-agent, or the entire agent without engineering intervention. Must be in the buyer's hands, not behind a support ticket. Should be tested quarterly.

**Indirect prompt injection.** A class of attack where content the agent reads from a tool, document, or external source contains instructions the agent treats as if they came from the operator. The unsolved problem of the agent layer; adaptive-adversary defense rates sit at 60–80% honestly disclosed.

**Action rollback.** Per-write-tool procedure for restoring a system of record after the agent has written the wrong value. See Chapter III.3. Distinct from "logging," which is necessary but insufficient.

**Model pin.** The specific model identifier (e.g., `claude-opus-4-7-20260301`) the vendor has tested the agent against. Every eval report and every contract clause should reference a model pin. Model swaps without re-eval are a procurement event.

**Model-update notice.** The contractual SLA — typically 30 to 90 days — for a vendor to notify the buyer before swapping the underlying model. Must include re-eval rights and right-to-refuse.

**Training rights.** The contractual scope of what the vendor may do with the buyer's prompts, completions, and persistent memory for model training, fine-tuning, or eval-set augmentation. Bartz v. Anthropic and NYT v. OpenAI re-priced this language in 2024–2025; assume any ambiguity now reads against the vendor in 2026.

**Output ownership.** The contractual statement of who owns the agent's outputs (the buyer, the vendor, joint, public domain). Default vendor templates assume buyer ownership of inputs and joint or vendor ownership of outputs, which is wrong for most enterprise use cases.

**Hallucination indemnity.** Contractual provision allocating liability for harms caused by the agent's incorrect or fabricated output. Air Canada (February 2024) crystallized the rule that the deploying party holds the bag absent specific contract language. Insert the indemnity.

**Agent-action liability.** Distinct from hallucination indemnity. Allocates liability when the agent's *action* — not its *output* — causes harm (a wrong payment, an unauthorized scope grant, a deleted record). New as a category; treat it as a board-level concern.

**Persistent memory.** Long-term storage of conversation history, derived facts, and user preferences the agent carries across sessions. Residency, deletion, and subpoena posture of persistent memory are first-class procurement questions, not afterthoughts.

**Computer-use.** Class of agent capability in which the agent operates a SaaS application by reading the screen and emulating keyboard / mouse input rather than calling an API. OSWorld benchmark scores sit in the mid-50s as of Q2 2026, well below the human 72%. Not yet production-grade for unattended SaaS-UI tasks; do not buy on the demo.

**Conversation-resolution metric.** Outcome-based metric, popularized by Sierra, that prices CX-agent value by resolved conversations rather than per-seat. Not yet a procurement standard outside CX; Bret Taylor's bet is that it will become one. Watch in 2026.

**Escalation handoff.** The Conclude-phase artifact when an agent hands a task to a human. Quality of handoff (full context, no re-asking, ticket linked, decision-record attached) is the single most-correlated variable with CSAT in CX-agent deployments and with controller acceptance in back-office deployments.

**Outcome-based pricing.** Vendor pricing tied to a business outcome rather than seats or tokens. Common in CX (Sierra). Rare elsewhere. Procurement should price the unit-economics floor and the gaming risk before agreeing.

**Per-trajectory billing.** Vendor pricing per completed agent trajectory rather than per token or per seat. Aligns vendor and buyer incentives on efficiency; gameable on trajectory boundary definition. Negotiate the definition before the rate.

**Reasoning effort.** Buyer-controllable parameter (low / medium / high) on reasoning-enabled models (OpenAI o-series, Claude 4.5+, Gemini 2.5+) that trades latency and cost for trajectory quality. A procurement input now, not a developer-only knob.

**Sandboxing.** Containment of the agent's execution environment such that tool calls, file writes, and external requests are confined to a controlled scope. Becoming a SOC 2 / ISO 27001-adjacent control ("AI-001: AI-generated code MUST execute in isolated tenancy with default-deny egress").

**Sub-processor change.** Vendor's introduction of a new downstream service provider (e.g., a new model provider, a new vector database, a new observability platform). Triggers a procurement event under GDPR, DPA terms, and increasingly EU AI Act tie-out refresh.

**Eval freshness.** The age of the vendor's signed eval report relative to the current model pin and system prompt. Anything older than 180 days is stale; anything older than the most recent model swap is invalid.

**Adaptive adversary.** A red-team methodology in which the test set is regenerated against the live defense, producing honest success rates as the defense improves. The honest counterpart to static red-team scores. Critical for indirect-injection defense disclosure.

**Conformity assessment.** EU AI Act process by which high-risk AI systems demonstrate compliance with the Act's requirements before being placed on the EU market. The vendor-side tie-out (Chapter III.6) is the input; the buyer-side conformity assessment is the output. Both required.

**Schrems-II posture.** The vendor's data-transfer regime for personal data moving between the EU and the US, post the 2020 Schrems-II decision and the EU-US Data Privacy Framework (2023). Required disclosure for any agent processing EU data; the agent's memory residency and tool-call destinations both count.

**HITRUST CSF.** Common Security Framework adopted by US healthcare; CSF v11.x is the current major version. The de facto procurement bar for healthcare AI agents; level r2 with HITRUST certification is the strongest posture.

**SR 11-7.** US Federal Reserve guidance on model risk management. The de facto framework for financial-services AI model governance; covers validation, monitoring, and governance. Increasingly applied to LLM-driven credit, suitability, and underwriting decisions through 2025–2026.

**ISO 42001.** The 2023 international standard for AI management systems. Adopted by Drata, Vanta, and Secureframe as a readiness mapping; not yet a regulator-mandated bar in most jurisdictions but the cleanest single-attestation vendor posture as of 2026.

**NIST AI RMF GenAI Profile.** The 2024 NIST AI Risk Management Framework Generative AI Profile. The closest US-side analog to EU AI Act Article 14 framing. Voluntary today; mentioned in federal acquisition guidance and procurement-template-shaping in late 2025 and 2026.

**Sovereign deployment.** Agent deployment posture in which model inference, agent runtime, persistent memory, and audit logs all reside within a single jurisdictional boundary, typically a sovereign-cloud region. Required for some EU buyers; advisable for any buyer whose data-residency regime is non-trivial.

**Trajectory cost audit.** A FinOps-for-agents exercise that measures the dollar cost per trajectory and identifies optimization (planner-executor split, prompt caching, FP4 quantization, aggregator routing) opportunities. Folds into Bet #4 as a Bet #1 module. Plausibly absorbed by AWS Bedrock auto-routing by H2 2027.

**Form-factor.** The user-facing surface the agent inhabits (Slack thread, browser extension, voice channel, computer-use overlay, dedicated SaaS UI). Procurement-relevant because form factor determines DLP inheritance, threat surface, and approval pattern. Slack agents inherit DLP; computer-use agents do not; the procurement story diverges per form.

**ASL-3 / Responsible Scaling Policy.** Anthropic's classification of model risk levels and the corresponding deployment commitments. Adjacent to OpenAI's Preparedness Framework. Procurement question: what does the vendor's deployment posture commit to when the underlying model crosses a safety threshold mid-contract?

---

*End of Wave 1 Playbook draft. F5 chapters (Six Counterparties, Fourteen Addenda, Appendix Contract Clauses) reconcile in Phase 5. Wave 2 populates the Section VI rubric across the named vendor set. The Executive Foreword, Seven Overlays, Decision Tree, Rubric outline, and Glossary stand as the Wave 1 backbone.*
