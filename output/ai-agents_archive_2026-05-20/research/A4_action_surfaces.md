# A4 — Action Surfaces: Where Agents Reach Into the World

**Date:** 2026-05-12 · **Author:** Alex Yedi · **Scope:** sandboxed code execution, browser automation, full computer use, agent-outbound voice. Excludes inbound user-instruction surfaces (covered in A7) and excludes compute/fabric/inference (covered in A1–A3 of the prior brief).

The action-surface layer is where agentic systems stop being chatbots and start being labor. Each of the four families below has a different reliability curve, a different incumbent set, and a very different procurement story. The honest read in May 2026: sandboxed code execution is production-ready and commoditizing; browser automation is production-ready in narrow lanes; computer use is still demo-grade despite the marketing; voice agents are production-ready for short, scripted calls and collapse on the long tail.

---

## 1. Sandboxed Code Execution — the most under-discussed procurement requirement

The category exists because frontier-model code output is non-deterministic and frequently unsafe to run on first-party infra. Sandboxes give you (a) a clean filesystem, (b) network egress controls, (c) per-execution isolation, (d) sub-second cold-start.

**The vendor set in May 2026:**

- **E2B** — open-core, dominant developer mindshare. Series A extended in late 2025. Public ARR not disclosed; community signal suggests $15–25M ARR range, doubling YoY. Most-cited by AI eng teams I've talked to.
- **Modal** — emerged from Modal Labs' serverless GPU origin; agent-workload pivot in 2025. Reported ARR north of $50M in early 2026 (inference + agent compute combined; sandboxing is a fraction). Strongest infra credibility.
- **Daytona** — newer; positions on dev-environment heritage. Smaller install base, aggressive on price.
- **Vercel Sandbox** — GA January 2026, Firecracker microVMs, tight integration with AI Gateway and Workflow DevKit. The "if you're already on Vercel" default.
- **Hugging Face Spaces** — used as ad-hoc sandbox by research teams; not production-grade for paying enterprise.
- **Replit Agent sandbox** — bundled, consumer-leaning, the workhorse for prosumer "build me an app" flows.
- **GitHub Codespaces / Actions** — repurposed; works, but cold-starts and quota make it a poor fit for high-volume agent loops.

**The non-obvious question:** when does an agent actually need a sandbox vs. a direct Python tool call?

The honest answer: **anytime the code is model-authored AND the execution touches anything beyond pure-function math.** A `tool_call: calculator` doesn't need E2B. An agent installing `pandas`, fetching a CSV, and writing output files absolutely does. Anthropic's own `code_execution` tool defaults to this pattern. Once a buyer's security review starts, "where does AI-generated code run" becomes the #2 question (right after "where does data go"). Anything other than "ephemeral isolated VM, no persistent state, no egress to internal networks" gets red-flagged.

**Procurement implication for F1000:** sandboxing is a SOC2/ISO27001 control surface, not a feature. Vanta-style frameworks will start mapping `AI-001: AI-generated code MUST execute in isolated tenancy with default-deny egress` by end of 2026. Vendors that ship "agents that run code" without a named sandbox layer (E2B / Modal / Vercel Sandbox / equivalent) will fail enterprise security review.

**Commoditization timeline:** fast. 18–24 months before this looks like S3 — boring, multi-vendor, priced on egress.

---

## 2. Browser Automation — Playwright's quiet dominance, Browserbase's loud growth

Distinct from computer use. Browser automation is **DOM-level**: agent reads accessibility tree, dispatches clicks via CDP, parses structured responses. Pixel-perfect rendering doesn't matter.

**Vendor map:**

- **Playwright + AI patterns** — the boring baseline. Microsoft-maintained. Free. Combined with a Sonnet/Opus loop that emits selectors, it solves 70%+ of "scrape this site / log into this portal / fill this form" tasks. The honest baseline anyone benchmarking agent browsers should beat.
- **Browserbase** — fastest-growing in category. Series B in late 2025, reported $50M+ ARR by Q1 2026 (per multiple operator newsletters; not officially confirmed). Sells managed Chromium-at-scale + session recording + stealth. The default "buy" choice.
- **Stagehand** (Browserbase OSS) — natural-language wrapper over Playwright. The DX win that pulled developers off raw Playwright.
- **Browserless** — incumbent (2018). Lost the AI-era narrative to Browserbase. Still strong on price for batch scraping.
- **Skyvern** — open-source, agent-native browser. Smaller team. Differentiates on vision+DOM hybrid.
- **Anchor Browser, Hyperbrowser** — 2025 entrants, both aimed at the long tail of "I need an MCP-compatible browser tool." Too early to call.

**The honest comparison:** an agent-native browser outperforms plain Playwright when (a) the target site has heavy anti-bot, (b) the workflow spans many sessions and needs replay/audit, or (c) the dev team doesn't want to maintain Playwright themselves. Otherwise — and this is the under-told story — a well-prompted Playwright loop with a strong model still wins on cost and latency. Plenty of Series B AI companies I've talked to internally use Playwright + Sonnet 4.5/4.7; they bought Browserbase only after Playwright maintenance became someone's full-time job.

**Reliability inflection:** crossed in mid-2025. Browser automation is production-ready today *for sites the agent has seen at training time or has a stable DOM*. It still collapses on novel SPAs with shadow DOM tricks, captcha walls, and any auth flow involving SMS/2FA without a human-in-loop.

---

## 3. Full Computer Use — loud, hyped, still demo-grade in May 2026

The OS-clicks-and-keystrokes tier. Vision-based. The agent watches pixels, moves a virtual mouse, types.

**Vendor map:**

- **Anthropic Computer Use** (Oct 2024 launch) → **Claude for Chrome** (2025) → **Claude for OS-level use** continues to evolve via Claude 4.7. The most-cited baseline.
- **OpenAI Operator** (Jan 2025) → rebranded **ChatGPT Agent** in mid-2025 after consumer confusion. Lives in ChatGPT Pro.
- **Google Project Mariner** — Chrome-embedded; tied to Gemini 2.5/3.
- **Microsoft Copilot Vision / Copilot Studio agents** — Windows-native; the enterprise default for Microsoft shops.
- **Adept** — acqui-hired by Amazon in mid-2024; ACT-2 lineage now inside AWS Q.
- **Multi-On, Twin AI** — early consumer plays; both shrunk after Operator launched.
- **Manus** (Chinese, 2025) — agent that combines computer use + browser + voice; gained genuine traction outside US press. Worth tracking.

**The reliability honest answer (cite, don't infer):**

| Benchmark | What it measures | Best public score (May 2026) |
|---|---|---|
| **OSWorld** | Real OS tasks across Ubuntu/Win | ~50–55% (Claude 4.7 + Anthropic Computer Use, late-Q1 2026 report); humans ~72%. Crossed 50% in early 2026, up from ~22% at Oct 2024 launch. |
| **WebArena** | Web tasks in sandboxed sites | ~70%+ for top systems (GPT/Claude tied range); humans ~78%. |
| **ScreenSpot / ScreenSpot-Pro** | GUI element grounding | 80%+ on ScreenSpot v1; ScreenSpot-Pro (harder, professional apps) ~45–55%. |
| **AndroidWorld** | Mobile OS tasks | ~50% top systems; substantial headroom. |

**The 70% threshold question:** is computer use production-ready? **No, not for unattended autonomous work.** WebArena ~70% means roughly 1 in 3 multi-step tasks fails. OSWorld ~50% means coin-flip. For human-in-loop "drive this for me while I watch," it's useful and improving fast. For "run overnight, file the expense reports unsupervised," it's still a 2027 question.

**Where it does work in May 2026:** scripted, narrow, repeated workflows where the failure cost is low and a retry is cheap. Filling forms on a known SaaS. Doing visual QA. Light data entry. Anything that's a high-frequency, low-stakes, reversible click sequence.

**Where it collapses:** anything involving payment, anything where a wrong click is destructive, anything with novel UI, anything across more than ~15 steps without checkpoint.

---

## 4. Voice (Agent-Outbound Only) — production-ready for short calls, collapses on the long tail

Scope: the agent makes or receives phone calls, replaces an IVR, does sales/support/scheduling outbound.

**Vendor map (orchestration layer):**

- **Vapi** — fastest-mover; YC W23 origin. Reported $20M+ ARR by Q4 2025, growing fast. Developer-first.
- **Retell AI** — close competitor; differentiates on enterprise compliance and latency. Mid-teens ARR estimate.
- **Bland AI** — third in the trio; aggressive marketing, mid-market focus, similar ARR band.
- **LiveKit Agents** — infrastructure layer (WebRTC); powers a meaningful slice of the above + OpenAI Realtime. Series B 2025.
- **ElevenLabs Conversational AI** — ElevenLabs' move up-stack from TTS into full agent. Strong on voice quality, weaker on telephony depth.
- **PolyAI, Parloa, Regal** — enterprise CX. PolyAI is the most-cited in F1000 contact-center RFPs. Parloa raised $66M Series B in 2024 and grew through 2025. Regal targets revenue calls (sales/collections).

**Foundation models for voice:**

- **OpenAI Realtime API** — gpt-realtime / gpt-4o-realtime line. Sub-500ms voice-to-voice.
- **Cartesia Sonic-2** — fastest TTS in market on most independent latency tests through 2025; ~40ms first-byte.
- **Deepgram Nova-3** — speech-to-text leader on accent robustness and code-switching.
- **Telephony substrate:** Twilio (incumbent, premium), Telnyx (price/perf challenger), LiveKit Cloud (WebRTC-native, the AI-native pick).

**The latency floor and uncanny line:**

End-to-end voice-to-voice in May 2026 sits at **~500–800ms** for the best stacks (Cartesia + GPT-realtime + LiveKit). Human conversational turn-taking is ~200–300ms; below ~600ms the experience feels human, above ~1s it feels robotic. The field has *crossed the natural-cadence line* for short turns. The "uncanny" remaining gap is in interruption handling, backchanneling ("uh-huh," "right"), and prosody on emotionally-loaded statements.

**Where voice agents hold up:** outbound qualification calls, appointment scheduling, "press 1 for sales" IVR replacement, simple Tier-1 support deflection. Vapi/Retell are running these at scale today.

**Where they collapse, predictably:**
- **Numeric input over phone** — credit card digits, long account numbers; ASR error rates jump sharply.
- **Long proper nouns** — multi-syllable last names, foreign street names; transcription degrades.
- **Heavy accents and code-switching** — Nova-3 helps but doesn't close it.
- **Interruption mid-utterance** — most systems still over-talk or freeze for 600ms.
- **Calls >5 minutes** — context drift, repetition, looping.

**Procurement implication:** voice is the surface where AI-vendor risk shows up fastest in regulated industries — TCPA, GDPR, state consent laws. The serious enterprise buyers (financial services, healthcare) want consent capture, full-call audit recording, named voice cloning policy. Most of the Vapi/Retell/Bland trio is still maturing this.

---

## Cross-cutting Argument: does the action-surface layer commoditize?

**The bull case for commoditization:** sandboxes are converging on Firecracker + Linux + Python. Browsers are converging on managed Chromium + CDP. Voice is converging on LiveKit + OpenAI Realtime + best-of-breed TTS. All of these are infrastructure plays where the winning move is "cheap, reliable, ubiquitous." In 24 months these look like Twilio circa 2018 — boring, multi-vendor, sub-10% gross margin attractive.

**The counter-argument:** the moat is *operational tooling around the surface*, not the surface itself. Browserbase isn't winning because their Chromium is better; they're winning because they ship session recording, replay, anti-bot evasion, and a Stagehand DX layer. Vapi isn't winning on telephony — they're winning on the dashboard that lets a non-engineer ship a phone agent in 30 minutes. The surface commoditizes; the workflow layer on top does not.

My read: **both are true**. Pure surface — sandbox, headless browser, TTS — commoditizes inside 24 months. The operational layer on top (recording, replay, evals, compliance, observability) is where durable value lands.

---

## What changed in the last 90 days (Feb → May 2026)

- **Vercel Sandbox went GA (Jan 2026)** and by April had visible adoption inside the Next.js + AI SDK developer cohort. Firecracker + Fluid Compute pricing reframed the category cost curve.
- **OSWorld crossed 50%** on the leading scoreboard in late Q1 2026 — meaningful symbolic threshold, still well short of 70%+ human level. Confirms steady, not breakout, progress on full computer use.
- **Browserbase reportedly closed >$50M ARR** by Q1 2026 (operator newsletter reporting; not officially confirmed by company). Confirms it has separated from the rest of the browser-automation pack.
- **Cartesia Sonic-2 generally available** with sub-50ms first-byte TTS, pushing the realistic voice-to-voice floor below 600ms for the first time in production stacks.
- **Anthropic Claude 4.7 + Computer Use** quietly improved long-horizon trajectory length on OSWorld in the Q1 release — partial credit, still a 1-in-2 failure rate at 15+ steps.
- **Manus (China)** gained meaningful traction in APAC; first credible non-US cross-modal agent. Worth a tracker entry.
- **MCP-native browser tools (Hyperbrowser, Anchor)** moved from launch to GA — sign that the surface is being absorbed into the MCP-server distribution model rather than staying proprietary SDKs.
- **Voice TCPA enforcement** uptick in Q1 2026 (US) forced Vapi/Retell to ship consent-capture and recording-policy features. Compliance is becoming the procurement gate.
