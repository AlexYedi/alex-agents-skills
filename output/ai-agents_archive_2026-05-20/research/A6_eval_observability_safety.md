# A6 — Agent Evaluation, Observability, and Runtime Safety / Guardrails

> Brief in the AI-Agents Series. Companion to A1 (models / runtimes / MCP) and the AI-Stack regulatory work (`AI_STACK_SUBSTRATE_VOL2.pdf`, `OCQ_TRACKER.md`). Capability-level safety (ASL, Preparedness Framework, model cards, deployment freezes) is Meta-A in Phase 3 — **this brief stays operational**: what runs in the pipeline at inference time and what the procurement counterparty actually asks.
> **Date:** 2026-05-12 • **Word target:** ≤2,200 • **Voice:** OCQ_TRACKER register.

---

## Zone 1 — Agent-specific evaluation and observability

### Why the category broke from "LLM observability"

Through 2024, eval/obs meant: log prompt, log completion, score for hallucination / toxicity. Agents broke that on four axes:

1. **Trajectories, not turns.** One request fans out into 20–80 tool calls across sub-agents. Final-output eval catches ~30% of real failures; trajectory eval catches the rest — wrong tool, right tool with wrong args, infinite loops, sub-agent that summarized away the load-bearing fact.
2. **Replay is the debug primitive.** "Re-run from step 7 with a different model / prompt / tool stub." Logfire, LangSmith, Braintrust, Langfuse, Arize Phoenix all converged on replay UIs in 2025; those without it are losing deals.
3. **Online eval, not just offline.** Agents drift inside a session (context degradation past 32k, see A1). The pattern is **LLM-as-judge over live traces** + **regression sets auto-curated from production failures**.
4. **Cost and latency are first-class.** A 47-tool-call trace at Opus pricing is a P&L event. Token / dollar / wall-clock per node is non-negotiable.

### The vendor map — as of May 2026

**Tier 1, real enterprise traction:**

- **LangSmith / LangChain** — bundled with LangGraph 1.0 GA (Oct 22 2025). Series C $25M Feb 2024 at ~$1B; recruiters peg $40–60M ARR by Q1 2026. Tightest LangGraph integration; ecosystem-locked, not the choice for Claude-shop or OpenAI-shop greenfield.
- **Braintrust** — Series A $36M (a16z, June 2024); Series B reportedly closed Q1 2026 (~$60M, Information leak, unconfirmed). Strongest "evals-as-CI" workflow; Notion, Airtable, Brex publicly named (Q4 2025 / Q1 2026 case studies). Most likely pure-play winner.
- **Langfuse** — OSS core (MIT), YC W23, $4M seed + $4M extension (Lightspeed, July 2024). 8k+ GitHub stars; self-host genuinely usable. Reference choice in EU/regulated deploys.
- **Arize Phoenix / Arize AX** — Phoenix is the OSS sibling (Apache 2.0). Series C $70M (Salesforce Ventures, Dec 2024). MLOps-mature accounts migrating from SageMaker/Vertex.
- **Galileo** — Series B $45M (Scale Venture, June 2024); Series C reported April 2026 (~$60M, unconfirmed). Hallucination metrics ("ChainPoll", "Context Adherence") + agent-trace eval. Hubspot, ServiceNow named (Q3 2025).

**Tier 2, narrower but credible:**

- **Comet Opik** (OSS, Sept 2024) — Langfuse competitor from the experiment-tracking world.
- **Confident AI / DeepEval** — DeepEval OSS (15k+ stars), pytest-style eval-as-code; engineering teams that hate UIs.
- **HumanLoop** — UK, prompt management + agent eval. Strong in UK/EU financial services.
- **Patronus AI** — Series A $17M (Notable, March 2024). Lynx + Glider open eval models — when buyer wants a *defensible* judge, not a vendor black box.
- **AgentOps** — agent traces specifically; OSS-first; CrewAI/AutoGen ecosystem.
- **Helicone** — observability-as-proxy. YC S23. Time-to-value wins; proxy model loses as runtime native tracing matures.
- **Promptfoo** — OSS red-team + eval CLI. **Acquired by OpenAI Sept 2025**; OSS continues but strategic neutrality gone.
- **Inspect AI** — UK AISI, OSS (MIT). Framework not vendor. The standard for capability evals in safety-conscious shops; cited in EU AI Act conformity-assessment drafts (Feb 2026).
- **METR** — research org. RE-Bench + the "task length doubles every 7 months" paper (March 2025) set the agenda. Cite, don't procure.

### Benchmark landscape — useful vs. theater

- **TAU-bench / τ²-bench** (Sierra, Aug 2024 / Q1 2025): multi-turn tool use against a simulated user. Best CX-agent proxy. Sierra-co-authored; read accordingly.
- **SWE-Bench Verified** (Princeton + OpenAI, Aug 2024): 500 human-validated GitHub issues. Inflated by harness tricks; **SWE-Bench Live** (rolling) is cleaner.
- **GAIA** (Meta, Nov 2023): humans 92%, frontier ~70%. Saturating.
- **BrowseComp** (OpenAI, April 2025): hard web research. Deep Research products 50–55%.
- **OSWorld** (HKU+CMU, April 2024), **WebArena** (CMU, July 2023): computer/browser use. Frontier 35–42%; production reliability worse (A1 error-compounding).
- **AgentBench** (Tsinghua, Aug 2023): mostly research artifact now.
- **SWE-Lancer** (OpenAI, Feb 2025): freelance software priced in $. Best "would I pay for this" framing public. Frontier earns ~$200K of $1M — under 25%.

**The honest read.** No public benchmark predicts enterprise agent ROI; they predict ceiling-of-the-possible. Every serious enterprise builds **internal eval sets from production traffic** — typically 200–1,000 curated trajectories. Winners make curating that set cheap (Braintrust, Langfuse, LangSmith converging here). Losers still pitch "use our benchmark."

### Open-source vs. proprietary — where lock-in bites

Not in trace ingest — OpenTelemetry GenAI semantic conventions stabilized Jan 2026; LangSmith, Braintrust, Arize, Langfuse all support OTel. Lock-in is in **eval logic and judge models**: regression sets as Braintrust YAML or Galileo metric definitions take a quarter to port. Langfuse + DeepEval + Inspect AI is the OSS triad that survives a vendor switch.

### Will eval consolidate?

**Partially, by 2027.** Too many pure-plays for a ~$300M ARR category. Likely:
- LangSmith stays because LangGraph stays.
- Braintrust wins OpenAI-shop, eval-as-CI; the rumored Series B makes them the consolidator candidate.
- Langfuse wins EU + self-host. Arize keeps MLOps-mature accounts.
- 2–3 of {Galileo, HumanLoop, Patronus, Comet, Helicone, AgentOps, Confident AI} acquired by hyperscalers or runtime vendors (LangChain, Vercel, Databricks) by EOY 2026.
- Native model-provider tooling (OpenAI Traces, Anthropic eval dashboards, Vertex AI Eval) eats the bottom.

### What eval/obs vendors do NOT solve (procurement-readiness gap)

The live-fire question for Bet #1. NO eval/obs vendor today fully covers:

- **Auditable, signed eval reports** (model + harness + dataset + score, chain-of-custody) that survive a regulator's subpoena. Inspect AI is closest; nobody is fully there.
- **Multi-party eval** — vendor + customer + auditor on the same trace with redaction. Single-tenant infra exists; cross-counterparty is bespoke.
- **Reproducibility across silent model upgrades.** Without fixed model pins, eval isn't a control.
- **Tie-out to EU AI Act conformity / NIST AI RMF GenAI Profile / ISO 42001.** Vendors *claim* alignment; nobody ships a turnkey bundle.
- **Agent-specific harms** — cascading sub-agent failure, injection-induced tool misuse, exfiltration via tool returns. Most vendors evaluate the model, not the system.

**That is the gap.** It is the gap a Procurement Playbook can name and price.

---

## Zone 2 — Runtime safety / guardrails at the tool boundary

### Threat model — what's real

1. **Direct prompt injection / jailbreak** — user types "ignore your instructions." Largely solved at the frontier model layer; residual risk low and falling.
2. **Indirect prompt injection via tool returns** — agent fetches a webpage, email, Jira ticket, Slack message, PDF containing adversarial instructions. **Unsolved.** Anthropic constitutional-classifier research, Simon Willison's continuing reporting, and EchoLeak / "AgentSmith"-class PoCs (multiple through 2025) all confirm: any agent that reads attacker-controlled data and has write/action tools is exploitable. Defense is layered (sandbox, action confirmation, output validation), never complete.
3. **Multi-turn / multi-agent injection** — compromised sub-agent influencing parent; tool returns shaping later-turn decisions. Emerging; mostly research-stage.

### The vendor map

**Pure-play guardrail vendors:**

- **Lakera** — Swiss, Series A $20M (Atomico, Oct 2023); Series B reported Q4 2025 (~$50M, trade press). Lakera Guard (real-time PI defense) + Lakera Red (red-team-as-a-service). Strongest brand. **Atlassian, Dropbox, Citi publicly named (Q3 2025).**
- **Protect AI** — Series B $60M (Evolution Equity, Aug 2024). **Acquired by Palo Alto Networks announced April 2025; closed Q3 2025 for ~$700M.** First big consolidation signal in the category.
- **Robust Intelligence** — **Acquired by Cisco Aug 2024**, now Cisco AI Defense.
- **HiddenLayer** — Series B $50M (M12, March 2024). Model-supply-chain security (model scanning, MLSecOps). Earlier in the lifecycle than Lakera.
- **Cranium** — KPMG spin-out (2023). More GRC than runtime.
- **CalypsoAI** — Series B $23M (Paladin, Sept 2023); enterprise GenAI gateway, federal/defense angle.
- **Apex Security** — seed (Sequoia, March 2024); NYC Lakera competitor, early but credible.

**Hyperscaler bundles (the real competitor):**

- **AWS Bedrock Guardrails** (Apr 2024 → GA; expanded 2025–2026): policy filters, PII redaction, denied topics, **Automated Reasoning** for hallucination (GA Dec 2024). Friction-free if you're on Bedrock.
- **Microsoft Purview AI Hub + Defender for AI** (Ignite Nov 2024 → GA 2025): prompt DLP, AI inventory, posture. The procurement-friendly answer in M365 shops.
- **Google Vertex AI Safety Filters + Model Armor** (Cloud Next 2024 → 2025): similar surface; weak brand outside GCP.
- **Anthropic constitutional classifiers**: not a sold product, baked into Claude.

**Open-source — actually used:**

- **NVIDIA NeMo Guardrails** (Apache 2.0, GTC 2023): Colang DSL for conversational rails. Reference OSS choice in regulated shops.
- **Meta Llama Guard 3 / Llama Prompt Guard 2** (open weights, Llama 3/4 cycle): purpose-built classifier models. Genuinely good; OSS baseline.
- **Promptfoo red-team** (now under OpenAI): automated jailbreak/injection probing.
- **Garak** (NVIDIA, OSS): LLM vulnerability scanner.

### Honest assessment on prompt-injection defense

**Nobody is solving indirect prompt injection.** Vendors quoting "99.X% PI detection" report on **known-pattern** rates against public attack corpora. Adaptive-adversary numbers — attacker knows the defense — fall to 60–80% (Lakera and Anthropic both publicly admit this).

The honest defense-in-depth stack:

1. **Treat tool returns as untrusted.** Tag bytes from outside user instructions; degrade/refuse high-privilege actions when planning context is tainted.
2. **Action confirmation gates.** Any tool that writes, pays, sends, escalates requires explicit approval — or runs in a reversible sandbox (Vercel Sandbox, E2B, Modal; see A4).
3. **Output validation / schema enforcement.** Constrain decoding; refuse free-form action when a tool call is expected.
4. **Privilege separation across sub-agents.** A web-reading sub-agent does NOT carry write tokens. The Claude Agent SDK sub-agents pattern is the cleanest expression.
5. **Continuous red-team.** Promptfoo / Garak / Lakera Red on every major prompt or model change.

A vendor selling item 1 only is selling vapor for production touching money. The procurement-grade answer is the whole stack.

### Will runtime-safety survive standalone?

**Mostly absorbed into hyperscaler bundles within 18 months.** Protect AI → Palo Alto (Q3 2025) was the bell. AWS/Azure/GCP guardrails ship "good enough" for 80% of use cases at zero procurement friction. Lakera survives as cross-cloud / model-neutral and the red-team specialist — last independent at scale or next acquisition. Apex, Calypso, Cranium likely roll up. **Llama Guard + NeMo Guardrails + Promptfoo eat the floor.**

One durable niche: **regulated, model-neutral, audit-grade** — Lakera-shaped, with the procurement-readiness gap (signed reports, EU AI Act tie-out) explicitly closed. That niche is where Bet #1's Playbook would partner or compete.

---

## The production-readiness threshold

The "would I deploy this in production touching customer money?" question, May 2026:

**Crosses the bar:** internal-employee agents, read-only tools, supervised execution, full trace logging, human approval for writes, ≥200-trajectory regression set, action-confirmation on anything irreversible.

**Does not cross the bar:** customer-facing autonomous agents with write access to systems-of-record, unsupervised multi-hour horizons, reading attacker-controllable input (email, web, public docs), without action confirmation. This is *most* "AI Agent" pitch decks of 2025–2026. Decagon, Sierra, Glean, Harvey, Hippocratic all built **substantial custom guardrail stacks on top of their model providers** because off-the-shelf doesn't clear the bar. That custom stack is part of the moat (see Bet #2).

---

## Handoff to Bet #1 (Procurement Playbook)

Five questions a F1000 risk officer asks that NO vendor turnkey-answers as of May 2026:

1. Show me a **signed, reproducible eval report** for this agent against my use case, with model pin, dataset hash, harness version.
2. Show me your **prompt-injection adversarial test suite** and your adaptive-adversary results — not just the public-corpus numbers.
3. Show me **tool-boundary policy**: which tools can the agent invoke un-supervised, which require approval, which are blocked when context is tainted by external content.
4. Show me **the action-rollback story** for every write tool.
5. Show me **EU AI Act / NIST AI RMF / ISO 42001 conformity-assessment tie-out** with traceable controls.

Vendors today answer #1 and #2 partially; #3, #4, #5 are bespoke. **That is the playbook's job to systematize.**

---

## What changed in the last 90 days (Feb → May 2026)

- **Braintrust Series B (~$60M) reported closed Q1 2026** (trade press leak, not yet confirmed publicly) — repositions Braintrust as likely consolidator in eval/obs.
- **OpenTelemetry GenAI semantic conventions stabilized Jan 2026** — the trace-format war is effectively over; vendor switching cost on ingest drops; eval logic becomes the only lock-in.
- **EU AI Act GPAI obligations (Article 55) became enforceable Aug 2025; first conformity-assessment guidance drafts circulated Feb 2026** — eval/obs vendors now have something concrete to map to; Inspect AI cited explicitly.
- **EchoLeak / Microsoft 365 Copilot indirect-injection PoC disclosed March 2026** — pushed indirect prompt injection from "research curiosity" to "named CVE class" in enterprise security conversations.
- **Galileo Series C reportedly closed April 2026 (~$60M, unconfirmed)** — signal that LPs still believe in pure-play eval/obs despite the bundling threat.
- **Promptfoo (post-OpenAI) shipped agent-specific red-team modules (Feb 2026)** — raises the OSS floor; pressures Lakera Red on pricing.
- **Anthropic published Claude Agent SDK eval harness templates (March 2026)** — model-provider-native eval eats the bottom of third-party.
- **NeMo Guardrails 1.0 GA (April 2026, Apache 2.0)** — OSS guardrails now production-credible; floor under paid vendors rises.

---

*End A6.*
