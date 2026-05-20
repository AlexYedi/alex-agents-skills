# B3 — OCQ Matrix: Action Surfaces, Eval/Observability, Regulation

**Date:** 2026-05-12 · **Author:** Alex Yedi · **Voice:** OCQ_TRACKER register
**Companions:** A4, A6, OCQ_TRACKER. Capability safety lives in B2; this brief is operational and procurement-facing. Scoring 1–5; **5/5/5** = lens failed. Axis 1 = Confidence/Severity/Decidability; Axis 2 = Time-to-Monetize/Probability/Asymmetry; Axis 3 = Claimability/Exposure/Bet-size.

---

## Sub-stratum 6 — Action Surfaces (sandboxes, browser, computer use, voice)

**Framing.** Four sub-categories, four reliability curves, one procurement story. Sandboxed execution is production-ready and commoditizing (Vercel Sandbox GA Jan 2026; Modal $50M+ ARR; E2B doubling). Browser automation crossed inflection mid-2025 — Browserbase >$50M ARR Q1 2026. Computer use hit OSWorld 50% Q1 2026 but stays coin-flip at 15+ steps. Voice crossed the natural-cadence line (~500–800ms via Cartesia Sonic-2 + GPT-Realtime + LiveKit) for short calls; collapses on numerics, accents, >5min, TCPA-regulated outbound. **The surface commoditizes; the operational layer on top — replay, recording, evals, consent capture, audit — is where margin lives.**

### Opportunities

**O1 — "Operational layer" advisory for action-surface deployments.** Browserbase, Vapi, Modal, E2B sell the surface; F1000 procurement needs the surrounding stack — session recording, replay, action confirmation, consent capture, sandbox-tenancy policy. No vendor turnkey-bundles all four. Bet #1's Playbook packages "action-surface readiness" as a SOC2/ISO27001 control set (`AI-001: AI-generated code MUST execute in isolated tenancy`) that vendors and buyers both adopt. Falsifiable if Vanta/Drata ships an AI-action-surface module before Q4 2026.
**Score: Confidence 4 / Time-to-Monetize 4 / Claimability 5.**

**O2 — Voice-agent compliance wrapper for regulated outbound (TCPA/HIPAA/FINRA).** Q1 2026 TCPA enforcement forced Vapi/Retell to ship consent capture; coverage is uneven and none have FINRA-grade recording with disclosure scripting. NYC fintech (Ramp, Brex), legal (Harvey), healthcare (Hippocratic) need this yesterday. A "Voice Compliance Pack" — disclosure scripts, consent flows, recording-policy spec, RFP checklist — sells to GTM ops at $15–40K. Falsifiable if PolyAI or Parloa ships a regulated-vertical SKU before Q4 2026.
**Score: Confidence 4 / Time-to-Monetize 5 / Claimability 4.**

**O3 — Sandbox tenancy as a procurement gate-question.** Most 2026 agent pitches still answer "where does AI-generated code run?" with hand-waving. Vercel Sandbox GA, E2B Firecracker, and EchoLeak (March 2026) opened the narrative window to make "named, isolated, default-deny-egress sandbox" the *second* question on every AI procurement form. Distributed via Bet #6's newsletter, this compounds. Falsifiable if AWS Bedrock ships first-party agent-sandbox bundling before Q3 2026 and collapses the discussion to a checkbox.
**Score: Confidence 4 / Time-to-Monetize 3 / Claimability 5.**

### Challenges

**C1 — Hyperscaler bundling absorbs the operational layer.** AWS, Azure, GCP are 12–18 months from shipping integrated "AI action runtime" bundles (sandbox + browser + voice + traces + guardrails). Bedrock AgentCore (re:Invent 2025) is the leading indicator. If the bundle ships before Alex plants flag, operational-layer thesis collapses to a checkbox. Watch: Bedrock AgentCore GA and pricing Q3 2026.
**Score: Severity 4 / Probability 4 / Alex's exposure 3.**

**C2 — Computer use stays demo-grade through 2026.** OSWorld 50% Q1 2026 is symbolic, not operational. If the field plateaus at 55–65%, "computer-use procurement" advisory is theoretical — buyers won't pay to evaluate what they aren't deploying. O1 leans on browser + voice + sandbox where production is real; computer use is the asterisk. Watch: OSWorld delta Q2→Q4 2026 and any unattended 30-step trajectory demo with <10% failure.
**Score: Severity 3 / Probability 3 / Alex's exposure 2.**

### Open Questions

**OQ1 — Does Browserbase consolidate or get acquired before Q2 2027?** $50M+ ARR Q1 2026, growing, with operational moat (recording + replay + Stagehand). Acquired by Cloudflare/Vercel/hyperscaler = browser-automation stack consolidates, advisory window shortens 6 months. Independent Series C = window holds. Answer-event: Browserbase funding or M&A press in next 6 months.
**Score: Decidability 4 / Asymmetry 3 / Bet-size 3.**

**OQ2 — Does voice outbound get re-zoned by FCC or state TCPA expansion in 2026?** Q1 2026 enforcement is the leading edge; NY/CA/IL drafting AI-voice disclosure laws (chatter). If enforcement reaches a named Vapi/Retell customer with a six-figure fine, O2 goes advisory→mandatory and TAM 3–5x's. If paper, O2 stays a sideline. Answer-event: first named TCPA enforcement against an AI-voice vendor, or first state AI-voice consent bill clearing committee.
**Score: Decidability 3 / Asymmetry 4 / Bet-size 3.**

---

## Sub-stratum 7 — Evaluation and Observability

**Framing.** Category broke from "LLM observability" on four axes — trajectories not turns, replay as debug primitive, online eval over live traces, cost/latency as first-class. Tier-1 (LangSmith, Braintrust, Langfuse, Arize, Galileo) converging; OTel GenAI conventions stabilized Jan 2026 — trace-ingest war over. Lock-in lives in eval logic and judge models. Braintrust Series B (~$60M, Q1 2026 leak) is the likely consolidator. **The named procurement gap from A6** — signed reproducible eval reports, multi-party eval with redaction, model-pin stability, EU AI Act / NIST RMF / ISO 42001 tie-out, agent-specific harms — is unclosed by every vendor. Bet #1's live wedge.

### Opportunities

**O4 — Systematize the "signed reproducible eval report" as a procurement artifact (Bet #1's load-bearing wedge).** A6 named the gap: no vendor ships model-pin + dataset-hash + harness-version + signed chain-of-custody that survives a regulator subpoena. Inspect AI (UK AISI, cited in EU AI Act Feb 2026 drafts) is closest but is framework, not procurement artifact. The Playbook publishes the *report template itself* — open, vendor-neutral, regulator-presentable — and becomes canonical. Falsifiable if Braintrust/Galileo ships a "compliance eval report" SKU before Q4 2026 with named regulator endorsement.
**Score: Confidence 5 / Time-to-Monetize 4 / Claimability 5.**

**O5 — Eval vendor-selection advisory for F1000 procurement teams.** Five Tier-1, ~7 Tier-2 vendors; no buyer has neutral guidance. Pitches rhyme: trajectories, replay, LLM-as-judge, OTel. Real differentiation is buried — LangSmith for LangGraph, Braintrust for OpenAI + eval-as-CI, Langfuse for EU/self-host, Arize for MLOps-mature, Galileo for hallucination-heavy. A 12-page memo refreshed quarterly is a sales asset across Bets #1/#4/#5. Falsifiable if Gartner/Forrester ships a Magic Quadrant equivalent before Q3 2026.
**Score: Confidence 4 / Time-to-Monetize 4 / Claimability 4.**

**O6 — "Adaptive-adversary" prompt-injection test suite as a compliance artifact.** Vendors quote "99.X% PI detection" against public corpora; adaptive-adversary falls to 60–80% (A6). EchoLeak (Microsoft 365 Copilot, March 2026) made indirect injection a named CVE class. Promptfoo (post-OpenAI) shipped agent red-team modules Feb 2026. A productized "adversarial eval bundle" — Promptfoo + Garak + Llama Prompt Guard 2 + curated trajectories — sold to mid-market vendors as "ready for enterprise security review," $25–75K. Falsifiable if Lakera Red drops prices >50% or AWS bundles equivalent into Bedrock Guardrails by Q4 2026.
**Score: Confidence 4 / Time-to-Monetize 4 / Claimability 4.**

### Challenges

**C3 — Native model-provider eval eats the bottom.** Anthropic published Claude Agent SDK eval harness templates March 2026. OpenAI Traces, Vertex AI Eval, Bedrock Evaluations all live. For 60–70% of agent teams: use provider tooling. Pure-play advisory loses oxygen unless buyer is multi-model or regulated. Alex's exposure mediated by Bet #1 framing (procurement, not implementation). Watch: Anthropic + OpenAI eval-product roadmaps at Q3 2026 dev days.
**Score: Severity 4 / Probability 5 / Alex's exposure 2.**

**C4 — Playbook's eval section requires technical depth Alex must still build.** Signed report mechanics, harness reproducibility, model-pin policies, OTel GenAI conventions — technical artifacts, not commercial talking points. Alex's AI-builder fluency must be visibly current. Watch: gap between Alex's eval-vendor map (this brief) and what a Braintrust/Langfuse founder would say to a regulator. Close monthly.
**Score: Severity 3 / Probability 4 / Alex's exposure 4.**

### Open Questions

**OQ3 — Does Braintrust become the consolidator or get acquired?** Series B (~$60M, Q1 2026 leak) repositions them. Series C at $1B+ rolling up 2–3 Tier-2 vendors (Galileo, Patronus, AgentOps candidates) = they become the eval-platform layer and advisory reorganizes around them. Acquired by Databricks/hyperscaler = category consolidates into infra. Answer-event: Braintrust Series C or M&A press in 6–9 months.
**Score: Decidability 4 / Asymmetry 4 / Bet-size 3.**

**OQ4 — Does EU AI Act Article 55 conformity-assessment guidance name specific eval frameworks?** Feb 2026 drafts cited Inspect AI explicitly. Final guidance naming 1–2 frameworks = procurement default in EU + US-regulated spillover. Vendor-neutral = category stays fragmented and Bet #1 has room to *define* the standard rather than reference one. Either outcome moves O4. Answer-event: Commission final Article 55 conformity-assessment guidance (Q3–Q4 2026).
**Score: Decidability 4 / Asymmetry 4 / Bet-size 4.**

---

## Meta-B — Regulation (EU AI Act, US state laws, sectoral)

**Framing.** Three regulatory surfaces, three teeth-vs-paper profiles. **EU AI Act:** GPAI (Art. 55) enforceable Aug 2025; first conformity drafts Feb 2026; high-risk agent classification unresolved; Article 14 human-oversight guidance (April 2026 draft) is the most actionable near-term lever. **US state:** CA SB 53 (signed Sep 2025, enforceable Jan 2026) live; NY S5641 (employment AI audit) tracking Q3 2026; Trump Dec 2025 preemption EO in court. **Sectoral:** FINRA AI rules (drafted 2025), HIPAA AI (HHS Dec 2025), FDA SaMD (Q1 2026). Bartz v. Anthropic and NYT v. OpenAI re-priced vendor IP indemnity through 2025–2026. EU enforcement is paper today; teeth question = Crux #4.

### Opportunities

**O7 — Article 14 human-oversight implementation playbook for agentic systems.** April 2026 Commission draft is the most actionable regulatory artifact for agent deployments. It requires "effective human oversight" for high-risk AI but leaves *operationalization* (when does a human review, what tools, what audit trail, what training) wide open. F1000 deploying CX/hiring/financial-advisor agents need this concretely. A 20-page playbook — control mapping, RACI, audit-log spec, training curriculum — sells to compliance + AI governance for $40–100K, recurs annually. Falsifiable if Big-4 ships an Article 14 playbook before Q4 2026 under $150K.
**Score: Confidence 5 / Time-to-Monetize 4 / Claimability 4.**

**O8 — CA SB 53 + NY S5641 transparency-report templates.** SB 53 (Jan 2026 effective) requires frontier developers to publish safety frameworks; downstream buyers are now asking their AI vendors for equivalent artifacts even when not legally required. NY S5641 (employment AI audit, AEDT successor) tracking Q3 2026 enforcement. A vendor-RFP transparency template pre-empting both — published open, brand-positioning value — feeds Bet #1's flywheel. Falsifiable if CalAI or NY AG publishes a model template before Q4 2026 that buyers reference instead.
**Score: Confidence 4 / Time-to-Monetize 3 / Claimability 5.**

**O9 — Vendor-IP-indemnity addendum library for AI procurement (post-Bartz, post-NYT).** Bartz v. Anthropic settled 2025 (training data); NYT v. OpenAI ongoing. Every F1000 procurement legal team is rewriting AI vendor terms — IP indemnity scope, training-data warranty, output-ownership clarity — mostly from scratch. A curated 10–15-clause library, vendor-side and buyer-side variants with negotiation notes, is a $25–60K artifact for procurement/legal-ops. Lower margin than O4/O7, high velocity. Falsifiable if Ironclad, Lexion, or a Big-Law firm ships a public clause library before Q4 2026.
**Score: Confidence 4 / Time-to-Monetize 5 / Claimability 4.**

### Challenges

**C5 — EU AI Act stays paper, US federal preemption succeeds.** Crux #4. No named 2026 GPAI fines AND Trump Dec 2025 EO preemption surviving court = regulatory advisory shrinks from "$10B+ category" to "niche but defensible." Playbook still works on F1000 self-policing but urgency collapses. Watch: first GPAI enforcement action AND Ninth/Second Circuit ruling on Dec 2025 EO (both likely Q4 2026).
**Score: Severity 4 / Probability 3 / Alex's exposure 4.**

**C6 — Sectoral regulators (FINRA, HIPAA, FDA) move faster than horizontal, fragmenting advisory.** FINRA shipping AI rules for sell-side in Q3 2026 (drafts circulating) splits the Playbook into 4–6 vertical SKUs (finserv, healthcare, life sciences, employment, education). Each smaller, more defensible, harder to scale one Playbook across. Watch: FINRA Notice to Members Q3 2026; HHS HIPAA AI Final Rule timing.
**Score: Severity 3 / Probability 4 / Alex's exposure 3.**

### Open Questions

**OQ5 — Does the EU classify autonomous agents as "high-risk" under Annex III in 2026?** Currently ambiguous. Commission guidance (expected H2 2026) placing agents that "take consequential actions in employment, credit, essential services" in Annex III = every vertical-agent vendor (Sierra, Decagon, Harvey, Hippocratic) faces conformity assessment and Bet #1's TAM 3x's. Punt and treat as GPAI-with-tools = status quo. Answer-event: Annex III agent guidance or formal Article 6 amendment proposal.
**Score: Decidability 4 / Asymmetry 5 / Bet-size 5.**

**OQ6 — Does a US state pass an AI-agent-specific consumer protection law before federal action?** CA SB 53 covers frontier developers, not downstream deployments. NY S5641 covers employment narrowly. A broader state agent law (consumer protection, agent dark-patterns) is most likely from CA, NY, or IL. Passed before Q4 2026 = sets template. Federal preemption succeeds first = no states pass. Answer-event: any state AI-agent consumer-protection bill clearing committee.
**Score: Decidability 3 / Asymmetry 4 / Bet-size 3.**

---

## Score-distribution check

15 rows × 3 axes = 45 scores. Distribution: 5s (8), 4s (24), 3s (12), 2s (1). Skewed high but not flat — Claimability favors 4–5 (procurement profile well-fit); Exposure pulled to 2–4. O4 (5/4/5) and O7 (5/4/4) were 5/5/5 candidates; neither hit. **Lens held.**

## Inference vs. citation flag

- **Cited (A4/A6/prompt):** Vercel Sandbox Jan 2026 GA; Browserbase >$50M ARR Q1 2026 (operator newsletters, unconfirmed); OSWorld 50% Q1 2026; Cartesia Sonic-2 sub-50ms; Braintrust Series B ~$60M Q1 2026 (trade leak, unconfirmed); OTel GenAI Jan 2026; EchoLeak March 2026; Article 14 April 2026 draft; CA SB 53 Sep 2025 / Jan 2026; Bartz v. Anthropic, NYT v. OpenAI.
- **Inferred:** sizing for O2/O6/O7/O9 ($15–100K) — operator judgment from procurement scar tissue, not benchmarked. Planning estimates, not forecasts.

*End B3.*
