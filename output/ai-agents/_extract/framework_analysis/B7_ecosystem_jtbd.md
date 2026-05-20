# B7 — Ecosystem JTBD for the Agent Stack

**Date:** 2026-05-12 · **Principal:** Alex Yedi · **Target:** AI_AGENTS_ADDENDUM.docx
**Companions:** `OCQ_TRACKER.md`; `build_addendum.js` Part IX (prior register — calibrated against, not duplicated).
**Method:** Christensen/Ulwick/Moesta. 8-phase job map. Top-down jobs the *agent stack* is hired for. I/S 1–10; opportunity = I + max(I−S, 0).

> The prior addendum's six AI-stack jobs framed the whole stack. This brief drops one stratum into the agent layer specifically. Where it inherits — Job 6 here = Job 4 there, narrowed — flagged.

---

## Job 1 · Complete a discrete back-office task without babysitting

**Framing.** An ops or finance leader has a multi-step rules-governed workflow (invoice triage, payroll exception, contract abstraction, refund, KYC) and wants the agent to take it inbox-to-archive over hours-to-days, fail safely, and report. **Buyer:** VP Ops / Controller / Shared-Services. **WTP:** $25–150K/yr per workflow mid-market; $500K–$2M F500 (per resolution / per document / per FTE-replaced).

| Phase | Most-overlooked outcome |
|---|---|
| Define | Time to translate an SOP into an agent spec (n8n/Zapier partial; no "SOP→agent" owner) |
| Locate | % source data reachable — legacy ERP, scanned PDFs (Glean/Hebbia for search; ETL bespoke) |
| Prepare | Confidence tools have correct write-scope + rollback (sandboxes for code; no SaaS-write equivalent) |
| Confirm | Pre-run probability the run won't stall at step 12 (PRMs internal at labs — A3; not exposed) |
| Execute | Trajectories that succeed-as-judged but write wrong — silent-failure, unserved |
| Monitor | Time-to-detect a looping run before token blow-out |
| Modify | Mid-flight intervention by a non-engineer (replay UIs are engineer-only) |
| Conclude | Audit-grade run summary a controller will sign — universally unserved (A6) |

**Top 3 underserved outcomes:**

1. Minimize time to diagnose *why* a partial-failure run stopped. **I 9 / S 3 / gap 9.**
2. Increase % of unattended runs producing a tamper-evident, signed evidence pack auditors accept without re-running. **I 8 / S 2 / gap 8.**
3. Minimize trajectories that complete-as-judged but write the wrong value to a system-of-record. **I 10 / S 4 / gap 10** — the silent-failure problem.

---

## Job 2 · Run a customer-facing conversation to resolution

**Framing.** A CX/growth leader needs every contact (chat / voice / WhatsApp / SMS / email) to either resolve to a stated outcome or hand off warm with full context. **Buyer:** VP CX (incumbent); CRO when retention-coupled; Director of Member Services in regulated. **WTP:** $1–4 per resolved ticket (Sierra, Decagon — A5); $9/hr "RN equivalent" (Hippocratic); $0.05–0.15/min outbound voice (Vapi/Retell — A4).

| Phase | Most-overlooked outcome |
|---|---|
| Define | Time to agree what counts as "resolved" with the business (Sierra Outcomes leads) |
| Locate | % identity + history found across CRM/billing/help-desk |
| Prepare | Channel-compliance (TCPA/GDPR/state-consent/HIPAA) pre-call — unserved (A4) |
| Confirm | Cold-start hallucination on policies told but not tested |
| Execute | First-contact resolution without misrepresenting policy (Sierra/Decagon optimize) |
| Monitor | Time to detect a class of failure (e.g., policy misquote) |
| Modify | Non-engineer CX lead ships a fix same-day — universally unserved |
| Conclude | Handoff with no re-asking, ticket linked, full context (Sierra leads; rest lose CSAT) |

**Top 3 underserved outcomes:**

1. Minimize % of escalations where the human re-asks something the agent already asked. **I 10 / S 3 / gap 10.**
2. Increase confidence a WhatsApp/SMS agent is consent-compliant across jurisdictions pre-launch. **I 9 / S 2 / gap 9** (WhatsApp Business API opened Jan 2026 — A7; almost no compliance tooling).
3. Minimize time for a non-engineer CX lead to ship a policy correction. **I 9 / S 3 / gap 9.**

**Non-US note.** WhatsApp-native (Yellow.ai, Haptik, Gupshup, Meta first-party) is the dominant global shape; same phase map, materially worse threat model (no end-to-end encryption guarantees, no audit-log inheritance). US-coastal vendors miss this; Bet #2 should not.

---

## Job 3 · Execute a multi-step coding change including PR review and merge

**Framing.** Eng lead has a spec'd change; wants the agent to branch, code, test, open the PR, satisfy CI, respond to review, and merge — without senior babysitting. **Buyer:** Eng Director / VP Eng / CTO. **WTP:** $200–500/seat/mo enterprise (Cursor Teams, Copilot Enterprise, Claude Code); success-priced not stable.

| Phase | Most-overlooked outcome |
|---|---|
| Define | Time from ticket to fully-scoped agent task (spec quality is bottleneck) |
| Locate | % of repo/doc/PR/test context surfaced (incumbents racing here) |
| Prepare | Secrets/keys exposed during execution (sandbox vendors serve; not standardized) |
| Confirm | Pre-PR confidence the change won't break unknown downstream (PRMs internal, not exposed — A3) |
| Execute | Trajectories that pass tests but regress in prod (SWE-Bench Verified gameable) |
| Monitor | Wall-clock to know if CI failure is flaky vs. real |
| Modify | Reviewer redirects mid-PR without restart (Cursor Composer closest) |
| Conclude | Residue — dead branches, abandoned WIPs post-merge — unserved |

**Top 3 underserved outcomes:**

1. Minimize % of agent PRs that pass review/CI but need senior rewrite within 30 days. **I 9 / S 4 / gap 9.**
2. Reduce time to disambiguate flaky CI vs. agent regression vs. environment. **I 8 / S 3 / gap 8.**
3. Increase % of code-agent runs producing audit-grade authorship/provenance metadata (model pin, prompt, dataset hash) for compliance and IP defense. **I 7 / S 2 / gap 7** — becomes I 10 in regulated industries post-Bartz / NYT v. OpenAI.

**Over-served caution.** "Make any code change from a prompt" is over-served (14+ funded players). The gaps are at the *end* of the job map.

---

## Job 4 · Operate a SaaS application on the user's behalf

**Framing.** A line-of-business user knows the tool (Salesforce, Workday, SAP, NetSuite, ServiceNow, Notion, Linear) but doesn't want to drive it. **Buyer:** the line manager who owns the workflow (RevOps Director, FP&A lead, Service Desk lead) — *not IT*. IT is compliance veto. **WTP:** embedded in seat (Agentforce $30–125, Copilot $30); standalone $50–200/seat for cross-tool orchestrators (Glean, Hebbia).

| Phase | Most-overlooked outcome |
|---|---|
| Define | Natural-language intent → executable plan (embedded copilots lead) |
| Locate | % of user's actual app state correctly perceived (computer-use fails prod — A4; embedded cheats via API) |
| Prepare | OAuth blast radius for a transient task — universally unserved |
| Confirm | User trust the agent won't touch out-of-scope |
| Execute | First-try success on multi-screen workflows (Mariner ~35–40% OSWorld) |
| Monitor | Cognitive load of watching a SaaS-UI agent in real time — A7 form-factor problem |
| Modify | Pause, edit goal, resume mid-task (ChatGPT Agent leads) |
| Conclude | Unambiguous record of what changed (embedded ship change-logs; cross-tool does not) |

**Top 3 underserved outcomes:**

1. Reduce OAuth blast radius — increase % of tasks running with least-privilege, time-boxed, scope-bounded credentials. **I 9 / S 2 / gap 9.** MCP 0.3 auth closes this *eventually*; today: unserved. **Bet #3 wedge.**
2. Increase % of cross-tool tasks (Salesforce → Outreach → Gong → Slack) that complete without a human reconnecting the chain. **I 8 / S 3 / gap 8.**
3. Minimize the calendar time a non-IT line manager waits to deploy a new agent into a sanctioned tool. **I 8 / S 3 / gap 8** — procurement gauntlet hits hardest here since the buyer is not the seat-owner.

**Persona honesty.** Vendor marketing targets the CIO; the *true buyer* is the line manager. IT is procurement, not customer. Vendors who pitch line-up and bring IT along sell faster (Glean's Slack-first wedge — A7).

---

## Job 5 · Stay current on a domain and act on what changes

**Framing.** Operator (PM, AE, RevOps, compliance, architect, investor) needs a fast-moving domain monitored, summarized, prioritized, and surfaced only for decisions they would make. **Buyer:** operator themselves ($20–200/mo); employer for team-tier ($500–5K/seat/yr — AlphaSense, Hebbia, Perplexity Enterprise, Glean). **Inheritance:** narrower than prior Job 3; same shape, any domain.

| Phase | Most-overlooked outcome |
|---|---|
| Define | Encoding "what matters to me about X" actionably |
| Locate | High-signal source coverage vs. SEO sludge |
| Prepare | De-duplicate ingestion across sources |
| Confirm | Trust that "nothing important" was filtered (unserved at consumer tier) |
| Execute | Reduce daily attention to extract today's decisions |
| Monitor | Signal that source quality is degrading (AI-slop) — unserved |
| Modify | Re-tune the agent when role shifts (manual today) |
| Conclude | "What changed" → calendar / ticket / message; cross-tool unserved |

**Top 3 underserved outcomes:**

1. Minimize time from event to operator-*deciding* (not just notified). **I 9 / S 2 / gap 9** — Bet #6's target.
2. Increase confidence the filter isn't silently dropping contrarian sources. **I 8 / S 3 / gap 8.**
3. Minimize duplicate processing across email/Slack/RSS/podcast/newsletter/X for the same event. **I 7 / S 3 / gap 7.**

---

## Job 6 · Pass agent-specific enterprise procurement and risk review

**Framing.** An AI-agent vendor enters a F1000 cycle and must satisfy InfoSec, Legal, Privacy, AI Governance, Procurement, and the business sponsor on agent-specific risks — autonomy scope, tool-boundary policy, indirect prompt injection, action rollback, sub-agent privilege, Art. 14 oversight, eval reproducibility — to close within the buyer's planning cycle. **Inheritance:** agent-narrowing of Bet #1 / prior Job 4. **Buyer:** the AI vendor's sales leader; real customer is the F1000 committee. **WTP:** the deal slips a quarter if this fails ($500K–$10M ACV); a tool closing the gap is worth $50–250K/yr (Vanta-shape).

| Phase | Most-overlooked outcome |
|---|---|
| Define | Map buyer's six counterparty checklists to vendor evidence (Vanta/Drata for SOC2; nothing AI-specific) |
| Locate | Artifacts (model cards, evals, DPAs, AI policy) in one place (TrustCenter partial) |
| Prepare | Agent-trajectory eval evidence buyer accepts (no turnkey signed report — A6) |
| Confirm | Pre-call confidence AI Governance will sign — unserved |
| Execute | Time-in-queue at each of six counterparties (Vanta-style workflow needed) |
| Monitor | Visibility into which counterparty is blocking — unserved |
| Modify | Counterparty-specific evidence packs on demand |
| Conclude | Evidence freshness through annual review |

**Top 3 underserved outcomes:**

1. Minimize calendar-time from security questionnaire to signed AI Governance sign-off. **I 10 / S 2 / gap 10.** Bet #1's target.
2. Increase % of agent-specific risk questions (indirect injection, tool-boundary, action rollback, sub-agent privilege) the vendor answers in standardized form. **I 9 / S 2 / gap 9.**
3. Reduce bespoke effort for an EU AI Act / NIST AI RMF / ISO 42001 conformity tie-out. **I 8 / S 2 / gap 8** — rising fast.

**Honest demand check.** Buyer-side demand real and growing (A6 lists the five questions). Vendor-side demand partly marketing-induced. Buyer-pull is sufficient — OCQ_TRACKER's 500-downloads / 50-inbound test in 60 days is the actual measurement.

---

## Job 7 · Onboard or ramp a new role using an agent-augmented training stack

**Framing.** Manager hires into an AI-native role (AE, FDE, Applied AI engineer, CS, ops analyst); wants the hire to reach productive output in weeks-not-quarters by pairing them with an agent that scaffolds workflow, coaches tool-by-tool, and produces observable trace for ramp assessment. **Buyer:** hiring manager (primary), L&D / People Ops (channel). **WTP:** L&D budget $1,200/employee/yr US median (ATD 2024); compressing 6-month ramp to 3 is worth $20–80K per hire.

| Phase | Most-overlooked outcome |
|---|---|
| Define | Capture senior's tacit practice (Sana/Docebo not agent-shaped) |
| Locate | Senior's prior traces/SOPs/recordings synthesized for ramp |
| Prepare | New-hire OAuth on day one (same blast-radius as Job 4) |
| Confirm | Coaching matches company's actual practice — unserved |
| Execute | Gap between "explainer" and "co-doer" (Cursor leads in coding; nothing for CS/AE/Ops) |
| Monitor | Ramp velocity vs. peers without surveillance — unserved |
| Modify | Correct coaching when practice diverges (manual) |
| Conclude | Agent tapers as hire ramps — agents don't taper |

**Top 3 underserved outcomes:**

1. Minimize time-to-productive-output for a new hire in an AI-native role. **I 9 / S 3 / gap 9.**
2. Increase manager visibility into ramp velocity without intrusive monitoring. **I 7 / S 3 / gap 7.**
3. Increase % of senior tacit knowledge captured into agent-usable form. **I 8 / S 2 / gap 8.**

**Anchor caution.** Most "AI for onboarding" is repackaged LMS. This job is different: an agent that *does the work alongside* the new hire and tapers. Nobody ships it cleanly in May 2026.

---

## Cross-job synthesis

### The 3 most-underserved patterns

1. **Conclude is universally unserved.** Across all seven jobs the Conclude phase — signed evidence pack (Job 1), warm handoff (Job 2), provenance metadata (Job 3), change-log (Job 4), decision-routing (Job 5), counterparty evidence (Job 6), taper (Job 7) — is the worst-served phase. Vendors compete on Execute. Buyers feel pain at Conclude. **Single highest-leverage pattern in the brief.**
2. **Modify by a non-engineer is the second.** Replay UIs exist for engineers (LangSmith, Braintrust); cockpit UIs for the line manager / CX lead / FP&A director do not. Every map shows a Modify gap of 7+. This is the *operator translation* gap inside the runtime — Bet #6 adjacent, productizable.
3. **Confirm (pre-flight: will this run actually work?) is the third.** Process-reward models exist inside frontier labs (A3) but aren't exposed to buyers. Pre-flight checks are technically feasible and commercially absent. Closing this turns Job 1 from "agent attempts, sometimes succeeds" into "agent commits, reliably succeeds" — the difference between $25K and $250K ACV.

### The 3 most over-served patterns

1. **Execute on coding tasks.** Cursor, Claude Code, Codex, Augment, Cognition, Lovable, Replit, Bolt, v0, Magic, Reflection, Factory, Plandex, Aider, Cline, Continue — 14+ funded players. Marginal demand at Execute exhausted (A5 §1: winner-take-most via Claude Code).
2. **Locate / enterprise search-agents.** Glean has the moat; Hebbia is the NYC specialist; Notion AI, Copilot, ChatGPT Business connectors, Slack AI, Box AI all attack. Twelve vendors for a Locate problem consolidating to 2–3 winners (A5 §3, highest encroachment).
3. **Execute on inbound chat.** Web/mobile chat-as-form-factor is over-served (A7 §1–2); the next 100 chat UIs will not move enterprise demand. The win is Conclude (escalation handoff) and Confirm (pre-deployment trust), not more chat.

### Recommendations for Alex — tied to Bets #1, #2, #3

**Bet #1 (Procurement Playbook) maps precisely to Job 6.** The Job 6 phase map is the Playbook's table of contents. The five risk-officer questions in A6 are the five chapter prompts. The opportunity-10 on "calendar-time to AI Governance sign-off" is the falsifiable hypothesis. **Action:** use the Job 6 phase map verbatim as the Playbook skeleton; position eventual SaaS as "Vanta for the agent-specific gauntlet" with the Conclude-phase evidence pack as the demo.

**Bet #2 (Vertical Agent GTM seat) maps to Jobs 2, 4, 7.** Sierra/Decagon win Job 2; Glean/Hebbia win Job 4 in knowledge; Hippocratic wins Job 2 + Job 7 in clinical; Harvey wins Job 4 in legal; Rogo / Ramp-AI win Job 4 in finance. The Field-CTO / Director-of-GTM role is **paid to close the Confirm + Modify + Conclude gaps for one job in one vertical** — that's the actual work. Frame interviews: "Your sales team is selling Execute; the buyer is signing on Confirm and Conclude. Here's how I close that." Sierra (NYC dual-HQ) is the cleanest fit; Hebbia and Rogo are NYC-native sleepers worth equal weight.

**Bet #3 (MCP-native integration) maps to Job 4's OAuth blast radius and Job 1's missing write-action sandbox.** Job 4's "least-privilege, time-boxed credentials" is what MCP 0.3 auth enables but no incumbent SaaS has shipped. Job 1's "Prepare: write-scope + rollback" is the parallel gap on the back-office side. **Action:** filter the Bet #3 audit (10 SaaS systems most lacking MCP servers) by *which Job 4 / Job 1 outcomes* each unlocks. Don't ship for completeness; ship for the Confirm/Conclude gap. This is what makes Bet #3 defensible against Cloudflare/Kong gateway commoditization.

**Cross-Bet through-line.** Conclude is the connective tissue: Bet #1 *sells* the Conclude gap; Bet #2 *closes* it inside a vertical; Bet #3 *ships the substrate*. **Bet #6 is the distribution layer** — the Job 5 "translate capability to operator action" gap is what makes the rest reach.

**What Alex should not pursue.** Job 3 (coding-PR-merge) is over-served at Execute and the buyer is engineering, not Alex's network. Job 5 standalone is right for Bet #6 distribution but not a defensible vendor opportunity at Alex's stage.

---

*End B7. Strong opinions weakly held. Confirm and Modify gaps require buyer-interview validation in the first 30 expert calls (OCQ_TRACKER Bet #1 plan).*
