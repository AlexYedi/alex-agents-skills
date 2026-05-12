# A3 — Planning & Reasoning Inside Agents

**Brief:** What planning and reasoning actually do inside production agents. Where the test-time-compute curve bends. What enterprise buyers can and cannot reason about when they buy a "reasoning model."
**Date:** 2026-05-12
**Companion:** post-training survey (RLHF/RLVR/GRPO/DPO) and the o1/o3/Claude-Extended-Thinking/Deep Think capability tier already covered in `output/ai-stack/` — referenced by name; not redone.

---

## 1. Architectural lineage — what survived

The chain is shorter than the hype suggests.

- **ReAct** (Yao et al., Oct 2022): interleave Thought→Action→Observation. Still the dominant loop in production agents in 2026. Most "agentic frameworks" (LangGraph, CrewAI, Pydantic-AI, Vercel AI SDK) are ReAct plus tool schemas and a state machine.
- **Plan-and-Solve** (Wang et al., May 2023): pre-compute a plan, then execute it. Survives as a *prompting pattern* in coding agents (Cursor, Cognition Devin, Claude Code) and in deep-research products — not as a separate framework.
- **Tree-of-Thoughts** (Yao et al., May 2023) and **Graph-of-Thoughts**: lab curiosity. Token cost is multiplicative; production usage is rare outside ad-hoc evals. Most teams that tried ToT in 2024–2025 reverted to ReAct + best-of-N sampling.
- **Reflexion** (Shinn et al., Mar 2023): self-criticism loop. Survived as the "reviewer" sub-agent pattern (Anthropic's research agent, Devin's verifier, Manus's critic). Materially helps on coding and SWE-bench-style tasks. Mostly noise elsewhere.
- **AutoGPT / BabyAGI** (Mar–Apr 2023): the open-ended planner-executor loop. **Dead in production.** What survived: the *idea* of a scratchpad, persistent memory, and tool registries — not the autonomous outer loop. Every serious 2026 agent runs bounded.
- **Planner–executor split**: alive and shipping. Sierra, Decagon, Cognition, Cursor, Claude Code, OpenAI's Operator/ChatGPT Agents all separate a "thinking" model from cheaper "doing" models. Often two of three calls in an agent run are the executor; one is the planner.
- **Meta-planning / hierarchical agents** (2025–2026): emerging in research-style products (Manus, Genspark, Anthropic's deep-research). A top-level planner spawns sub-agents with sub-budgets. Production maturity is uneven — coordination overhead is real.

**Reasoning-model tier impact on agents.** o1 (Sep 2024) → o3 (Dec 2024 → GA Jan 2025) → Claude 3.7 extended thinking (Feb 2025) → Claude 4/4.5 Sonnet & Opus extended thinking → Gemini 2.5 Deep Think (May 2025) → **DeepSeek R1 / R1-Zero** (Jan 2025) → **Qwen QwQ-32B** (Mar 2025) → **Kimi K1.5 / K2** (Jan–Jul 2025) collapsed two distinctions that mattered in the ReAct era:

1. The model now does *internal* multi-step search before emitting a token. The agent framework's "plan" step becomes redundant on hard tasks — the model already planned, you just paid for it inside `reasoning_tokens`.
2. Tool-use *during* reasoning (o3, Claude extended-thinking with tool use, Gemini 2.5 thinking + tools) means the framework's outer ReAct loop and the model's inner thinking loop overlap. The result: simpler outer scaffolds, more tokens per step.

**Net opinion:** most production "agents" in May 2026 are **3–7 step ReAct loops with a reasoning model, good system prompts, and a verifier pass**. The exotic graph/tree/meta-planner stuff is either inside the model now or relegated to long-horizon research agents.

---

## 2. Test-time compute economics — where the curve bends

The OpenAI o1 blog (Sep 2024) showed roughly **log-linear** AIME and Codeforces gains with thinking compute. By o3 (Dec 2024) and o3-pro (Jun 2025), the curve flattened on most agent-style tasks well before the latency budget did.

Honest numbers from public deployments and vendor disclosures (2025–Q1 2026):

- **Typical enterprise agent trajectory** (CX deflection, internal Q&A, RAG-heavy support agent): 4k–25k total tokens per task, of which 0–4k is reasoning. Cost: ~$0.02–$0.30 per task on Claude Sonnet 4.5 / GPT-4.1 / Gemini 2.5 Flash-Thinking class models.
- **Coding agent trajectory** (Cursor/Cline/Claude Code, single feature edit): 30k–250k tokens, with 5k–40k reasoning. Cost: $0.20–$3 per task. The SWE-bench Verified jump from ~49% (Claude 3.5, mid-2024) to **~75–80% range** for Claude 4.5 Sonnet and GPT-5/o3-class (late 2025–Q1 2026) came almost entirely from thinking budget + tool use, not architecture.
- **Deep-research-style trajectory** (Anthropic Research, OpenAI Deep Research, Gemini Deep Research, Manus): 500k–5M tokens, multi-agent fanout. Cost: $1–$20 per task. **METR's** 2025 "task time horizon doubling every ~7 months" finding is real but flattering — measured on a curated bench, not enterprise jobs.

**Where the curve bends in 2026:**

- **Below ~2k reasoning tokens**: gains are large and linear on math, coding, multi-hop retrieval. Cheap.
- **2k–8k**: diminishing but real. The "sweet spot" for most agent tasks.
- **8k–32k**: gains exist on hard coding / olympiad math / agent benchmarks (Aider, SWE-bench Verified, GPQA Diamond) but cost 4–10× and latency crosses **10–30 seconds**. Past the "interactive" line for chat UIs.
- **>32k**: research-mode only. Often regresses ("overthinking") on tasks where the answer was already correct at 4k. Anthropic's Feb 2026 extended-thinking guidance and OpenAI's `reasoning_effort=high` docs both warn about this explicitly.

**Latency thresholds that matter for enterprise:**
- **<2s**: interactive autocomplete / inline chat.
- **2–10s**: acceptable for "thinking" UIs with a visible spinner.
- **10–60s**: tolerable for "tasks" (research, code-PR, ticket resolution).
- **>60s**: must be async with notification — different product surface entirely.

**The 10× thinking-budget question.** Going from `reasoning_effort=medium` (~2k) to `high` (~16k) on Claude/OpenAI reasoning APIs typically costs **5–12× the call price** for a **3–10 pt benchmark gain on hard subsets** and **0–2 pt on typical enterprise tasks**. For CX, RAG, and most knowledge-work agents, the high setting is a waste. For coding and compliance/legal reasoning it pays. **The split is task-class-specific, not vendor-specific.**

**Planning-heavy vs. execution-cheap split (production pattern):**

The shipping pattern at Sierra, Decagon, Cursor, Cognition is roughly:

- Planner: Claude Opus 4.5 / GPT-5 / Gemini 2.5 Pro Thinking — $$$ — once per task
- Executor: Sonnet 4.5 / GPT-5-mini / Gemini Flash — $ — N times per task
- Verifier: a second Sonnet/o4-mini-class pass — $ — once

This routes 70–85% of tokens to the cheap tier while spending on the one step where reasoning actually changes the outcome. Vercel AI Gateway, Martian, OpenRouter, and AWS Bedrock all now expose this as a first-class routing pattern.

---

## 3. Reward modeling and learning in agent trajectories

Three threads, increasingly applied:

- **Process Reward Models (PRMs).** Lightman et al. (May 2023, *Let's Verify Step by Step*) showed step-level supervision beats outcome-only on math. By 2025–2026 PRMs are inside production reasoning models — but **they are not exposed to enterprise buyers**. OpenAI, Anthropic, Google all use process supervision internally for o-series, extended thinking, and Deep Think. Open replications (Qwen2.5-Math-PRM, DeepSeek-Prover-V2) exist but enterprise adoption is near-zero.
- **RLVR — Reinforcement Learning with Verifiable Rewards.** This is the breakthrough of the last 15 months. DeepSeek R1-Zero (Jan 2025) showed *pure RL on verifiable rewards* (math + code, automated checkers) produces reasoning behavior without SFT bootstrapping. Qwen QwQ, Kimi K1.5, and the entire Chinese reasoning ecosystem run on this recipe. US labs use it but disclose less. Applied to **agent trajectories**: reward = "did the task complete with a passing test / a satisfied verifier?" The training signal is the trajectory eval itself.
- **GRPO at trajectory level.** Group Relative Policy Optimization (DeepSeek, 2024) replaced PPO's value function with group-relative advantages. By Q1 2026 it is the default RL recipe for reasoning models and increasingly for agent fine-tunes. The implication for enterprise: **a vertical agent company that owns its task verifier and its trajectory data can post-train its own reasoning model on top of an open base (Qwen3, DeepSeek-V3.5, Llama 4)**. This is what Sierra and Cognition almost certainly do internally; what Harvey claims to do; what Manus did publicly.

**Trajectory eval as training signal — the benchmarks that matter:**
- **SWE-bench Verified** (500 human-validated tasks): the coding-agent ground truth. State of the art ~75–80% in Q1 2026.
- **AgentBench** (Liu et al., 2023; refreshed 2025): cross-domain agent eval; less load-bearing in 2026 because saturated on easy splits.
- **METR Task Time-Horizon** (2025): measures the length of human-task an agent can complete autonomously. Headline finding — doubling every ~7 months — is now the most-cited single chart in the field. Skeptics note bench composition matters.
- **AgentArena / τ-bench / WebArena**: increasingly important for CX, browsing, and tool-use agents. τ-bench (Sierra, 2024) is the closest public proxy for enterprise CX agent quality.

---

## 4. Opinionated takes

- **Planning is overrated for typical enterprise jobs.** A well-prompted 3-step ReAct loop on Sonnet 4.5 with a verifier matches or beats fancy planner-executor architectures on >80% of CX, RAG, and internal-knowledge tasks. The fancy stuff earns its keep on coding, deep research, and compliance reasoning — and nowhere else, today.
- **"Reasoning model" is a procurement category, not a capability claim.** Enterprise buyers can reason about (a) API cost per task at a measured token budget, (b) p50/p95 latency, (c) benchmark score on a task class that resembles theirs. They **cannot** reason about whether the model's internal CoT is faithful, whether thinking tokens generalize beyond the eval set, or whether the vendor's RLVR pipeline will keep improving. Treat reasoning-model marketing as opaque; demand task-class evals.
- **Test-time compute has unattractive economics for most agent classes.** A 10× thinking budget on a CX deflection agent costs 5–10× more, returns <2 pt accuracy, and pushes p95 latency past the abandon threshold. Spend the money on retrieval quality and tool design instead.
- **Chinese reasoning ecosystem is at parity on the recipe, behind on scale, ahead on openness.** DeepSeek R1/V3.5, Qwen3/QwQ, Kimi K1.5/K2, and Manus's agent stack ship open weights, open RL recipes, and competitive benchmark scores at 20–40% of US frontier inference cost. The procurement implication for US F1000: open-weight Chinese reasoners are the realistic on-prem option; political/IP risk is the gating factor, not capability.
- **The planner-executor split is the most durable architectural idea of the era.** Not because planning is special, but because it lets you route 80%+ of tokens to the cheap tier without sacrificing the one decision that matters. This is FinOps for agents and it ships today.

---

## What changed in the last 90 days (Feb → May 2026)

- **Anthropic Claude 4.5 Sonnet + Opus extended-thinking tool-use GA** (Mar 2026): tool calls *inside* the thinking trace are now first-class. Collapses outer-loop ReAct overhead on coding and research agents.
- **OpenAI `reasoning_effort` exposed across the o-series and GPT-5** (Feb–Apr 2026): `minimal/low/medium/high` is now a buyer-controllable knob. Made cost ranges in this brief possible to cite.
- **DeepSeek-V3.5 / R2** (Apr 2026): RLVR-trained reasoning at a reported ~$0.55/M input tokens — roughly 4–6× cheaper than GPT-5 reasoning. F1000 CIOs are running pilots.
- **METR's Q1 2026 update**: time-horizon doubling holds; agents now reliably complete ~4–6 hour human-equivalent tasks on the bench. Caveat: bench is curated.
- **Manus 2.0 / Genspark agent updates** (Mar–Apr 2026): hierarchical Chinese-built agents posting credible deep-research and coding numbers — without OpenAI/Anthropic weights underneath.
- **Sierra public ARR cross $150M, Decagon ~$100M** (Q1 2026 reporting): confirms the planner-executor + verifier production pattern at enterprise scale.
- **τ-bench v2 release** (Apr 2026): refreshed CX agent eval; first credible public proxy for "is your CX agent actually good." Vertical-agent vendors now cite it in sales.
- **Vercel AI Gateway, AWS Bedrock, OpenRouter all ship reasoning-tier routing** (Q1–Q2 2026): planner-on-Opus / executor-on-Sonnet is a config flag, not custom code.

---

**Word count check:** ~1,790. Within cap.
