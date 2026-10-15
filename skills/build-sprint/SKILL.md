---
name: build-sprint
description: Use when preparing for or running a hackathon or build sprint — the night-before prep (organizer brief, concept primer, sponsor tech, idea diverge, architecture, safeguards, repo scaffold, pitch skeleton, time-boxed build plan) and the build day itself (re-plan on day-of info, parallel scoped builds, debugging, review, demo and submission, post-event content). Maps every step to an agent, model, skills and the decision Alex owns. Teaching-first: Alex decides at every fork and comes out able to explain what was built.
---

# Build Sprint

A hackathon is a fixed-deadline product launch with a 3-minute sales call at the end. The judges score a small number of things (typically impact, technical execution, creativity, presentation, plus a sponsor-tool bonus) and they see the product only through the demo and the pitch. This skill is the path from "I'm going tomorrow" to "submitted, pitched, and I can defend every choice."

It is a map, not a script: each step names the agent to dispatch, the model, the skills it should load, what it returns, and **what Alex decides**. The parent thread orchestrates; agents cannot spawn agents.

## Three rules that hold the whole way

1. **Teaching rule.** Alex is learning to build, not offloading the build. At every fork the parent presents at most 3 options with a recommendation, and Alex picks. Every agent handback ends with the teaching contract (what / why, ≤3 key concepts with prior art, what changed, one interview-framing sentence). At the end of each phase, `alex:learning-coach-mentor` recaps what was decided and why, in language Alex could use in the pitch Q&A.
2. **Time-box and cut-line rule.** Every block has an end time and a pre-agreed cut line: the thing that gets dropped (or stubbed with canned data) if the block overruns. Overrun by 15 minutes → take the cut, do not negotiate with the clock. Feature work stops at **deadline minus 90 minutes**; the last 90 belong to the demo, the video, the Devpost fields and rehearsal. A working narrow demo beats a broken broad one.
3. **Never commit coupon codes or keys.** Sponsor credits, coupon codes, API keys, tokens and organizer-only links live in `.env` (gitignored) or a private note outside any public repo. The sprint repo is public by requirement, so treat every commit as published the moment it lands. Secret scan before every push.

## Model guide

| Work | Model |
|---|---|
| Reasoning-heavy: idea scoring, architecture, safeguards, re-plan | Fable |
| Execution and prose: builds, diagnosis, pitch drafting, primers | Opus |
| Specialist and bulk: sponsor research, code review, demo walk-through | Sonnet |

Budgets (from the agent-routing budgets): ≤12 live agents, ≤2 Fable or Opus agents in the background at once, and on build day **≤3 builders at once**. A spend-limit kill or cap bounce ends the wave: stop, report what landed, re-plan.

---

## Phase 1 — PREP (the night before)

### Step 0 · Capture the organizer brief privately
- **Who:** parent thread (no agent).
- **Do:** save the organizer's brief verbatim — schedule, deadline, judging rubric and weights, required submission fields, sponsor list and prize criteria, rules on pre-built code — to a private file outside the public sprint repo (or a gitignored `private/` folder). **Strip coupon codes, credit links and credentials** into `.env` or a password manager; the note keeps only "credits: see .env".
- **Alex decides:** nothing yet; confirms the brief is complete and which parts are unknown until day-of.

### Step 1 · Concept primer
- **Agent:** `alex:learning-coach-mentor` · **Model:** Opus.
- **Skills:** `ai-engineering-foundations`, `ai-agent-design-patterns`, `book-distiller`.
- **Do:** a 15-minute primer on the concepts the brief assumes (e.g. sandboxed code execution, agent tracing and evals, tool calling), each tied to something Alex already knows from enterprise SaaS. Ends with 3 questions Alex should be able to answer before picking an idea.
- **Alex decides:** which concepts he wants deeper before Step 3.

### Step 2 · Sponsor tech for a one-day build
- **Agent:** `alex:research-analyst` · **Model:** Sonnet.
- **Skills:** `evaluating-new-technology`, `research-brief-blueprint`, `competitive-analysis`.
- **Do:** per sponsor: what the product does, the SDK and quickstart, auth and free-tier or credit limits, **what can be wired in one hour** (with the doc link), known gotchas, and the sponsor's stated prize criteria. Plus: what past winners of this sponsor's prizes built, if public.
- **Returns:** one table, sponsor × (wire-in-an-hour path · limits · prize criteria · confidence).
- **Alex decides:** which sponsor tools are in play (more sponsors ≠ more points if the integration is shallow).

### Step 3 · Diverge 8–12 ideas and score them
- **Agent:** `alex:head-of-product` · **Model:** Fable.
- **Skills:** `problem-definition`, `ai-product-strategy`, `product-taste-intuition`, `consulting-ai-suitability-scoring`.
- **Do:** 8–12 ideas, each scored against the published rubric weights, the sponsor bonus, **one-day feasibility for a non-engineer with agent help**, and fit with Alex's GTM point of view (a problem he has lived as a seller or operator, so the impact story is first-hand). Kill reasons stated for the bottom half.
- **Returns:** a ranked table and a top 3 with a recommendation.
- **ALEX PICKS.** This is the biggest fork of the sprint; the parent does not proceed until Alex chooses (or merges two).

### Step 4 · Architecture of the pick
- **Agent:** `alex:cto-principal-architect` · **Model:** Fable.
- **Skills:** `cto-architect`, `ai-agent-design-patterns`, `trade-off-analysis-method`, `agent-memory-and-guardrails`.
- **Do:** components and data flow (one diagram), **what to stub vs build live** (canned data is legitimate for anything off the demo path), the sponsor integration points, and **where each safeguard layer lives**:
  - **Containment** — where the agent's code runs and what it can reach (sandbox, network, filesystem, credentials).
  - **Policy** — rules enforced outside the model (tool allowlists, approval gates, deny lists), not only asked for in a prompt.
  - **Evidence** — the traces, evals or logs that let a judge *see* the agent behaving safely in the demo.
- **Alex decides:** stub-vs-build lines and any stack choice the architect flags as a fork.

### Step 5 · Adversarial safeguards and failure check
- **Agent:** `alex:systems-analyst` · **Model:** Fable.
- **Skills:** `consulting-failure-design`, `systems-thinking`, `agent-memory-and-guardrails`.
- **Do:** pre-mortem ("it's 3:30 and the demo failed — why?") plus attack the architecture: prompt injection paths, the lethal trifecta (private data + untrusted input + an outbound channel in one component), credential exposure, runaway loops or spend. Rank by severity × likelihood; name the one safeguard that most strengthens the pitch.
- **Alex decides:** which risks to mitigate in the build, which to state honestly in the pitch, which to accept.

### Step 6 · Repo scaffold decision
- **Agent:** `alex:builder` · **Model:** Opus.
- **Skills:** `git-fundamentals-and-workflow`, `karpathy-coder`.
- **Do:** propose (and, once Alex agrees, create locally) a **new public repo per sprint**: README skeleton (problem, architecture, sponsor tools, safeguards, how to run), `.env.example` with key names only, `.gitignore` covering `.env`, `private/`, credentials and local data, and a **secret scan from minute one** (e.g. a pre-commit hook running `gitleaks` if installed, else a grep for key patterns; plus GitHub push protection turned on in repo settings). Builder does not push; Alex creates the GitHub repo and pushes himself the first time, so he knows where it lives. Check the event rules on pre-built code: scaffolding is usually fine, feature code before the start usually is not.
- **Alex decides:** repo name, licence, and that the first push contains no secret (he runs the scan and reads its output).

### Step 7 · Pitch skeleton
- **Agent:** `alex:content-correspondent` · **Model:** Opus.
- **Skills:** `brand-storytelling`, `value-story-framework`, `message-architecture`.
- **Do:** **3 slides max** (problem with a real number or story · how it works incl. the safeguards argument · impact and what's next), a demo script beat by beat (what is clicked, what the judge should notice, where the safeguard visibly fires), and 5 likely Q&A questions with one-line answers. Fit the time limit (e.g. 3-minute pitch + 2-minute Q&A).
- **Alex writes** the words. The agent supplies the structure, options for the opening line and critique; the voice is his. He also decides which beat the demo hinges on.

### Step 8 · Build plan in 30-minute blocks
- **Agent:** parent thread, with `Plan` (built-in) if the build is large · **Model:** Fable.
- **Skills:** `consulting-roadmap-sequencing`, `shipping-products`.
- **Do:** work **back from the deadline**: deadline − 90 min = feature freeze; before that, 30-minute blocks, each with an owner (Alex or a named builder dispatch), a path allowlist, a done-check and a **cut line**. The demo path's thinnest end-to-end slice is built first; everything else is layered on after it runs.
- **Alex decides:** the block order and every cut line, before sleeping.

**Phase close:** `alex:learning-coach-mentor` recap — the pick, why it beat the others, the architecture in one sentence, the three safeguard layers, and the cut lines.

---

## Phase 2 — BUILD DAY

### 1 · Absorb day-of info and re-plan (15 minutes, hard stop)
- **Agent:** `alex:cto-principal-architect` · **Model:** Fable.
- **Do:** fold in anything announced on the day (new rules, sponsor prompts, API changes, extra prizes) and diff it against the Step 4 architecture and the Step 8 plan. Output: what changes, what doesn't, the revised blocks.
- **Alex decides:** whether the idea survives the new info unchanged, bends, or swaps for the runner-up.

### 2 · Parallel builder pieces
- **Agent:** `alex:builder` · **Model:** Opus · **Skills:** `karpathy-coder`, `tdd-workflow`, plus `fullstack-dev` / `frontend-dev` / `building-mcp-servers` / `building-with-llms` as the piece needs.
- **Do:** one dispatch per block-sized piece, **each with a path allowlist, a done-check, and the commit rule**. **≤3 builders at once**, on non-overlapping paths (worktrees or separate directories) so they cannot collide. Builders never push.
- **Alex decides:** every fork a builder returns; he reads each diff summary before the next wave.

### 3 · Diagnostician on any failure
- **Agent:** `alex:diagnostician` · **Model:** Opus · **Skills:** `post-mortems-retrospectives` (optional, for the write-up).
- **Do:** reproduce, **inspect the actual data at the failure point before theorising**, bisect, one root cause with evidence, smallest-fix proposal. It does not edit; the proposal goes to a builder. Two failed hypotheses → it stops and escalates, and the parent checks the cut line before spending more time.
- **Alex decides:** apply the fix, or take the cut.

### 4 · Review gates
- **Agent:** `alex:reviewer` · **Model:** Sonnet.
- **Before each merge:** mode `code` (correctness, scope, secrets).
- **Before submission:** mode `safeguards` (containment / policy / evidence, tested layer by layer) and mode `demo` (run the demo path exactly as it will be shown, time it, list what could fail live and the fallback).
- **Alex decides:** on any `blocker`, fix or cut; he never ships past a reviewer `blocker` without saying so out loud.

### 5 · Submission (from deadline − 90 minutes)
- **Who:** Alex, with the parent thread.
- **Devpost fields checklist:** project name and tagline · problem and what it does · how it's built (architecture image) · **sponsor tools used, each with what it does in the project** · safeguards · challenges and what's next · public GitHub repo link (README complete, secret scan clean, repo visibility checked as public) · demo video link.
- **Demo video < 2 minutes:** record the rehearsed demo path; this is also the fallback if the live demo fails.
- **Pitch rehearsal:** at least twice against a timer at the stated length (e.g. 3 minutes), once with someone asking the Step 7 Q&A questions.

### 6 · Post-event
- Hand the event to the content workflow (`/post-event-content` where the events pipeline is installed; otherwise `alex:content-correspondent`): what was built, what the judges and other teams surfaced, and the build-in-public post. Repo, video and pitch become portfolio artifacts.
- **Phase close:** `alex:learning-coach-mentor` recap — what Alex can now explain that he couldn't yesterday, and one sentence per concept for interviews.
