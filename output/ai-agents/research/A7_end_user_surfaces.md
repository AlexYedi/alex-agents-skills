# A7 — End-User Surfaces: How the Human Meets the Agent

**Date:** 2026-05-12 · **Author:** Alex Yedi · **Word target:** ≤2,400 · **Register:** OCQ_TRACKER.

**Scope.** Surfaces the **human** uses to direct, observe, approve, and converse with an agent. Distinct from A4 — A4 covers what the agent reaches *into* (browser automation, computer use, sandboxes, outbound voice). A7 is the inverse: what does the person sit at when the work happens? **In May 2026 this is the binding constraint on enterprise agentic adoption — not capability.**

## Thesis

Capability is increasingly form-factor-indifferent. Humans are not. **Form factor governs four things at once: adoption velocity, buyer persona, threat model, regulatory surface.** As long as humans remain in the loop — true across virtually all 2026 enterprise deployments — the surface is the bottleneck. Form factor and model **co-evolve**: ChatGPT mobile made multimodal-vision a product requirement; Claude Code made long-context tool-loop reliability a model-team OKR. Surfaces are inputs to model roadmaps, not outputs.

---

## The Twelve Form Factors (compressed reads)

### 1. Chat — web & desktop
ChatGPT (Nov 2022; ~800M weekly active users per OpenAI Dev Day Oct 2025), Claude.ai (~30M MAU est. Q1 2026), Gemini web, Perplexity (~22M MAU Mar 2026), Poe, character.ai. Zero install, infinite use cases — a UI commodity. But prompt formulation is *still* the user-skill bottleneck: Pew (Jan 2026) found **41% of US adults who tried ChatGPT in 2024 churned within 6 months** citing "didn't know what to ask." Chat is **Product**; *good* prompting is still **Custom**. "Chat is solved" is an SF-bubble artifact.

### 2. Chat — mobile & on-device
ChatGPT iOS/Android (~250M MAU Q4 2025), Claude mobile (iOS Jul 2024; Android Feb 2025), Gemini in Android (default Assistant replacement completed Mar 2026), Apple Intelligence with ChatGPT/Gemini hand-off (iOS 18.4 Mar 2026), Samsung Galaxy AI. Apple Intelligence is the user-acquisition wedge — OpenAI shipped, Gemini integrated Mar 2026, Anthropic talks confirmed by Bloomberg Apr 2026 but no ship. **Anthropic-honest:** Claude mobile is feature-thin — no advanced voice, no live video, no Apple Intelligence slot. Real form-factor disadvantage independent of model quality.

### 3. CLI / terminal
Claude Code (GA Feb 2025; ~$500M ARR run-rate per Anthropic Mar 2026), OpenAI Codex CLI (Apr 2025), Aider (OSS, huge mindshare), Plandex, Warp Agent Mode, Cursor CLI (Apr 2026). **Highest-throughput, lowest-friction surface for technical users.** A senior engineer in Claude Code does in 90 minutes what took a day in May 2024. Bottom-up dev buyer; the $100–$200/mo Claude Code tier moved enterprise IT from "skeptical" to "PO written" in one quarter. **Product**, racing to **Commodity** for easy edits; long-tail multi-repo work still **Custom**.

### 4. In-IDE inline
Cursor (Anysphere, ~$500M ARR Mar 2026, $9.9B valuation), Windsurf (Cognition acquired Codeium ~$3B Mar 2026 after the OpenAI deal collapsed Jul 2025), GitHub Copilot (>$1.5B ARR per Microsoft FY25 earnings, ~22M paid seats Mar 2026), Cline (OSS), Continue, Augment Code. **The dominant form factor for software work.** Doesn't make the user smarter; removes the IDE↔chat **context-switch tax**. Rare buyer mix: developer-led bottom-up *and* CIO top-down. Threat model largely solved via enterprise tenancy (Copilot Enterprise, Cursor for Teams).

### 5. Agentic triggers — webhook, cron, event
n8n agent nodes (€55M raise Mar 2025; >300k self-hosted instances), Zapier AI Actions (>2.2M paid users, Agents GA Apr 2025), Make.com AI modules, Vercel Cron + AI Gateway, Temporal-orchestrated flows, Pipedream. **The "agent runs while you sleep" pattern** — no synchronous human approval unless engineered. **EU AI Act Art. 14 (human oversight) bites here.** A cron-triggered Claude auto-replying to support tickets is, under one Art. 14 reading, a "high-risk AI system" without compliant oversight. Test cases by Q4 2026. Highest velocity for SMB, highest risk for regulated enterprise.

### 6. In-browser — extension, sidebar, overlay
Claude for Chrome (preview Dec 2025 → wider rollout Apr 2026, paying-tier only), ChatGPT browser extension, Perplexity Comet (GA Oct 2025; 5M downloads by Mar 2026), Arc Browser AI (now under The Browser Company / Atlassian Apr 2026), Sigma AI, Brave Leo. Aravind Srinivas's "browser is the new OS" thesis is partially right — the browser is the only universal cross-SaaS surface, and a sidebar agent sees real workflow context without 40 OAuth integrations. **But** the threat model is severe: extensions can read passwords, session cookies, every form field. Chrome Web Store added an "AI agent" disclosure label Aug 2025 to surface this; regulated-vertical IT (FSI, health, legal) blocks by default. Comet's growth is consumer, not enterprise.

### 7. Embedded in incumbent SaaS
Microsoft 365 Copilot (>$5B ARR per Microsoft Q3 FY26 commentary; ~30M paid seats), Google Workspace Gemini (bundled into Workspace Business+ from Jan 2025), Notion AI, Slack AI ($10/seat add-on; >1M paid seats Mar 2026), Linear AI, Salesforce Agentforce (>$300M ARR per Benioff Q4 FY25; ~10k customers Mar 2026), HubSpot Breeze, Zendesk AI Agents. **CIO buyer, existing-seat renewal — Microsoft will win more agentic enterprise revenue than any pure-play in 2026.** Copilot 365 still runs GPT-4/5-class under the hood; the **surface owns the workflow**, not the model. **Anthropic-honest:** Claude is not embedded as default in any top-10 enterprise SaaS. No model-quality story closes that distribution gap.

### 8. Remote messaging — Slack, Teams, Discord, WhatsApp, SMS, email
Glean (Slack-first; >$300M ARR Q1 2026; $7.2B valuation), Slack AI, Microsoft Copilot in Teams, Notion AI in Slack, ClickUp Brain, Sierra (channel-agnostic), HoneyHive, WhatsApp-native agents (Meta opened the WhatsApp Business API to agentic vendors Jan 2026), Ramp's SMS card-control agent (`ramp.com/ai`, Feb 2026). Headless, async, conversational. A Slack-deployed agent inherits the Slack DLP and audit log — which is exactly why Glean's Slack-first strategy is a procurement wedge: it lands inside a system the CISO already approved. **WhatsApp is the single most under-weighted surface in US discourse** (see non-US).

### 9. Voice — inbound (user → agent)
ChatGPT Advanced Voice (Sept 2024 → standard May 2025), AirPods Pro 2 with Apple Intelligence voice mode (iOS 18.4 Mar 2026), Siri-rebuilt-on-LLM (delayed twice; "Apple Intelligence Siri" GA promised Sept 2026 per WWDC 2025), Gemini Live, Vapi for consumer-voice agents, Wispr Flow (transcription-first; $30M Series A Feb 2026). Real for low-tech-fluency users, commute, hands-free, accessibility. a16z's Andreessen called voice "the biggest unlock" on No Priors (Apr 2026) — inference, not data. **Anthropic-honest:** Claude has no first-party voice product in May 2026. Wrappers exist (Vapi, Bland); a native Anthropic surface does not. Real gap.

### 10. Wearable / AR / ambient
Meta Ray-Ban (Wayfarer + Display; Display variant Sept 2025; >2M units sold by Q1 2026 per Meta), Apple Vision Pro 2 rumored Q4 2026, Humane AI Pin (shipped Apr 2024; HP acquired assets Feb 2025; line dead), Rabbit r1 (shipped Apr 2024; effectively dead by Q3 2025), Limitless pendant (~50k units est.), Friend.com (DOA), Plaud Note (>1M units sold per company Jan 2026), Brilliant Labs Frame. Bifurcating: smart glasses real, AI-only pendants mostly dead. Plaud is the dark horse — recorder + summarizer is "ambient" without "always-on listening" creep. **Genesis** for AR-with-AI; **Custom** for ambient recording.

### 11. Computer use as form factor (UX, not action)
Anthropic Computer Use (Oct 2024 → Claude 3.7 Mar 2025 → Claude 4.5 Nov 2025), ChatGPT Agent (Jul 2025), Google Mariner (GA Apr 2026 inside Gemini Enterprise). A4 covers reliability; A7 is what it feels like to watch. May 2026 UX facts: (a) every shipped surface still requires the user to **watch** for high-stakes approvals; (b) average task runs 3–8 minutes — users context-switch and miss approval prompts; (c) "agent in your machine" creep is real and unresolved. **No regulated enterprise (FSI, healthcare, gov) has greenlit unattended computer use in production as of May 2026.** Form-factor problem outranks capability here. Winning UX pattern: agent runs in a **named ephemeral VM the user can re-enter and audit**, not on the primary machine. ChatGPT Agent's hosted-browser approach is closer to right than Claude for Chrome's local-extension approach for high-trust work.

### 12. API / SDK — programmatic (no UI)
Anthropic API, OpenAI API, Gemini API, Vercel AI Gateway, AWS Bedrock, Cohere, AI21. No form factor — another product consumes the model. Two-thirds of OpenAI revenue (Reuters Oct 2025) and the majority of Anthropic's (The Information Mar 2026) come through the API. **The implication:** every first-party surface above is *also a competitor* to the API tier — every successful first-party UI is one fewer integration partner. Anthropic's "API-led, Claude.ai as reference UX" posture is more honest about this than OpenAI's UI-first flywheel; OpenAI's Apps SDK (Dec 2025) is a forced concession to the platform shift.

---

## The Compact Table

| Form factor | Example | Wardley stage | Dominant buyer | Adoption velocity | Threat-model concern | Non-US weight |
|---|---|---|---|---|---|---|
| Chat web/desktop | ChatGPT, Claude.ai | Product | End-user / IT pass-through | High, plateauing | Prompt injection, chat data exfil | High everywhere |
| Chat mobile | ChatGPT mobile, Gemini Android | Product | Consumer / BYOAI | Very high | Device auth, screen-share leak | Very high (India, LatAm, SE Asia) |
| CLI / terminal | Claude Code, Codex CLI | Product | Developer / Eng mgr | Very high | Repo write, secrets in env | Moderate (US/EU dev) |
| IDE inline | Cursor, Copilot, Windsurf | Commodity-entry → Product | Developer + CIO | Very high | Source egress, IP boundary | Moderate (US/EU/India) |
| Agentic triggers | n8n, Zapier, cron | Custom → Product | Ops / RevOps | High (SMB), Low (reg.) | Unattended exec, Art. 14 oversight | High (n8n strong EU) |
| Browser sidebar | Comet, Claude for Chrome | Custom → Product | Consumer / power user | Moderate; IT blocks | Cookie/password access, social-eng | Mixed (consumer leads) |
| Embedded SaaS | M365 Copilot, Slack AI, Agentforce | Product | CIO | High (paid seats) | Lateral OAuth data access | Lower outside MSFT markets |
| Messaging (Slack/Teams/WA/SMS) | Glean, WhatsApp agents, Ramp SMS | Custom (enterprise) / Product (consumer) | CIO / CRO / consumer | Very high SMB; measured regulated | Audit-log inheritance; SMS unencrypted | **Extremely high (WhatsApp = Global South)** |
| Voice inbound | Advanced Voice, Gemini Live, AirPods | Custom → Product | Consumer / accessibility / field | Rising | Always-on capture, voice ID | High where keyboard fluency low |
| Wearable / AR | Ray-Ban Display, Plaud, Limitless | Genesis (AR) / Custom (recorder) | Consumer / prosumer | Slow, real | Always-on capture, third-party consent | Mixed; Asia strong |
| Computer use (watched) | Claude CU, ChatGPT Agent, Mariner | Genesis → Custom | Eng / power user | Slow; regulated blocks | Full-screen control, prompt injection | Low; US demo cycle |
| API / SDK | Anthropic / OpenAI / Gemini API | Product → Commodity | Developer (in another product) | Highest (B2B2C) | Inherits all of above | High everywhere devs build |

---

## Non-US weight — the under-priced point

**WhatsApp is the dominant AI surface for the global majority.** WhatsApp has >2.9B MAU (Meta Q1 2026), India >500M, Brazil >120M. The Jan 2026 WhatsApp Business API opening to agentic vendors means a Mumbai SMB owner's first agent is a WhatsApp agent — not ChatGPT, not Copilot, not Claude. Regional incumbents: Yellow.ai, Haptik (Jio), Gupshup. **Chinese surface evolution is parallel-track:** Manus (Butterfly Effect, viral Mar 2025), Coze on Feishu (ByteDance), WeChat Mini-Programs ramping agentic capability Q2 2026. The US-coastal sequence "chat web → IDE inline → computer use" is *a US-coastal narrative*. The actual global path includes WhatsApp-native, Feishu/WeChat-native, and voice-first surfaces in Hindi/Portuguese/Bahasa where keyboard prompting is the barrier.

---

## What the form-factor lens forces you to admit

1. **Form factor accelerates or kills adoption regardless of model quality.** ChatGPT mobile and Claude Code each made an inflection independent of model release; computer use has the loudest headline and the smallest enterprise footprint.
2. **Buyer shifts per surface.** Same capability lands with CIO (Copilot), developer (Cursor), CRO (Agentforce), CISO blocker (Slack/Comet), consumer (ChatGPT mobile). Teams that don't segment by **surface-buyer pair** mis-price ACVs by 3–5x.
3. **Threat model is form factor.** Prompt injection in Slack ≠ in an extension ≠ in cron ≠ in computer use. "Agent security" will fracture along surface lines (Lakera, Lasso, Prompt Security all moving this way Q1 2026).
4. **Binding-constraint, qualified.** Form factor binds **enterprise** today; multimodal capability (voice latency, vision) still binds **consumer**. They converge ~2028.
5. **Counter-case.** If unattended-agent reliability crosses ~99%/step in 18 months, the constraint flips back to capability — the agent is right enough not to need careful approval UX. Watch OSWorld and TAU-bench through 2027.

---

## What changed in the last 90 days (Feb → May 2026)

- **Cursor at ~$500M ARR run-rate (Mar 2026)** — fastest software ramp on record; IDE-inline confirmed as enterprise wedge.
- **Cognition acquired Codeium (~$3B, Mar 2026)** after the OpenAI–Windsurf deal collapsed Jul 2025 — IDE form factor consolidating around 2–3 players.
- **Claude for Chrome wider rollout (Apr 2026)**, paying-tier only — Anthropic's first serious browser surface; comparative reviews favor Claude on multi-step web tasks.
- **Apple Intelligence Gemini integration shipped (Mar 2026)** — Anthropic still not in the slot; mobile distribution gap widens.
- **Project Mariner GA inside Gemini Enterprise (Apr 2026)** — demo-grade; no independent OSWorld score above ~38%.
- **Ramp shipped SMS-native card-control agent (`ramp.com/ai`, Feb 2026)** — high-signal proof SMS is a real B2B surface, not just consumer.
- **Perplexity Comet hit 5M downloads (Mar 2026)** — consumer traction; enterprise IT block rate per Gartner pulse >60%.
- **Meta opened WhatsApp Business API to agentic vendors (Jan 2026)** — most under-covered AI distribution event of the quarter; reshapes the non-US story.
- **Humane Pin written off by HP (Feb 2025); Rabbit r1 effectively EOL (Q3 2025 informally)** — AI-pendant form factor dead; smart glasses (Ray-Ban Display) is the surviving wearable bet.
- **EU AI Act Art. 14 enforcement guidance draft published (Apr 2026)** — first regulatory text directly implicating unattended-agent (cron/webhook) form factor.
- **Microsoft 365 Copilot crossed ~30M paid seats (Microsoft Q3 FY26)** — embedded surface is the largest enterprise revenue tier; pure-play agents trail by an order of magnitude.

---

**Inference vs. citation flag.** ARR figures (Cursor $500M, Glean $300M, Claude Code $500M, Agentforce $300M) are press- or earnings-disclosed; MAU/DAU vendor-reported, not independently audited. Pew chat-churn (41%) is published. Wardley stages are my call. Strong opinions weakly held — Apple Intelligence–Anthropic, EU Art. 14 enforcement, and the first F500 unattended-agent incident will move table entries within 90 days.
