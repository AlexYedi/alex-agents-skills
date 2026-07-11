---
name: "agent-memory-and-guardrails"
description: "Use when productionizing an agent — adding short/long-term memory via LangGraph checkpointers, rewinding state, and layering guardrails (input/router, agent-level, post-model) plus human-in-the-loop. Also covers the evaluation and deployment posture for shipping agents. Reach for this when an agent works in a demo but isn't safe, stateful, or observable enough to ship."
---

# Agent Memory & Guardrails (Productionizing)

Decision-oriented reference for the gap between a working demo and a shippable agent. Paraphrased from Roberto Infante, *AI Agents and Applications* (Manning), Ch. 14 — use the book's repo for runnable code. Pairs with [[building-agents-with-langgraph]], [[multi-agent-orchestration]], and the measurement/eval work in [[ai-evals]] / [[eval-harness]].

## Memory = checkpointing

Short-term memory in LangGraph **is** checkpointing: the graph snapshots its entire state after each node, keyed by a **`thread_id`**. Pass the same `thread_id` next turn and the state rehydrates, so follow-ups resolve coreference ("the same town", "that hotel"). You don't hand-manage message lists — the checkpointer does it.

**Backend tiers** — match to environment:

| Backend | Use for |
|---|---|
| `InMemorySaver` | Dev / throwaway |
| `SqliteSaver` | Local persistence |
| `PostgresSaver` | **Production** — scale, reliability, concurrency |

**Rewinding** — restore any past checkpoint (`get_state_history` → pick a snapshot → build a config with its `thread_id` + `checkpoint_id` → `invoke(None, config)`) for resume-after-error or "what if I'd chosen B" branching.

**Load-bearing gotcha:** with OpenAI's Responses API you must set `use_previous_response_id=True` **alongside** `use_responses_api=True`. Without it, LangChain re-sends the whole history each turn, the API reads that as a duplicate submission, and it **errors.**

**Long-term memory** (across sessions) is a *separate, heavier* concern: per-user vector stores, summarization/pruning, and PII compliance. Don't reach for it before short-term memory is solid.

## Guardrails = application-level scope & policy

Three families — **rule-based** (regex/conditions), **retrieval-based** (check against approved sources), **model-based** (a small classifier/moderation model) — attached at **four points**:

1. **Input / router guardrail (fail-fast).** A cheap structured-output classifier — `GuardrailDecision(is_in_scope: bool, reason: str)` via `llm.with_structured_output(...)` — rejects off-topic requests **before** any specialist/tool spend, routing refusals to a no-op node wired to `END`. Two motivations: **accuracy** (off-domain → hallucination) and **cost** (stop your agent being abused as a free gateway to an expensive model). Make the refusal still-helpful (say what you *can* do).
2. **Agent-level guardrail.** A stricter `pre_model_hook` on an individual agent whose real data scope is narrower than the system's. Keep it even behind a router — **belt-and-suspenders**, because the agent may be reused without the router in front.
3. **Post-model guardrail.** Validate the **output** before it ships: redact PII, de-stale facts, enforce tone, verify structured-output format. A "reasonable-looking" answer can still be wrong.
4. **Tool-level guardrail.** Validate at the point a tool is invoked.

## Human-in-the-loop

Pause the workflow at the decision point, persist a checkpoint, notify a reviewer, and resume on approve/reject. **Log every decision as training data** so automated thresholds can rise over time. It's interim scaffolding: if escalation volume doesn't trend down, you've built a bottleneck, not a loop.

## Evaluation (a production discipline, not a checkbox)

Four test types over a labeled set of **100+ query/answer pairs including adversarial cases** (prompt injections, out-of-scope):

- **Functional** — correct/complete answers.
- **Behavioral** — policy, safety, tone.
- **Performance** — latency + API cost under realistic/peak load.
- **Regression** — stays stable against a fixed ground-truth set as prompts/tools/models change.

Score accuracy/precision/recall/F1 across runs (LangSmith automates the loop). The book flags eval as the "most overlooked but essential" step.

## Deployment posture

- **LangGraph Platform** — managed hosting, LangSmith-observed.
- **Open Agent Platform** — orchestration layer with prebuilt multi-tool/supervisor patterns that plug into MCP servers.

Production means **persistent storage**, **monitoring** (error rate, **P95 latency, tokens/query, tool success rate**, anomaly alerts), and **staged rollout with canary testing.** The deploy choice is driven by org constraints (on-prem vs cloud, data residency, compliance), not convenience.

## Map to the Empire State pipeline

Three concrete wins: (1) a **post-model guardrail** that flags any draft asserting a firm/person thesis without a cited source (the CLAUDE.md source-check rule) or echoing copy already in the visual brief — enforcing your anti-patterns *mechanically* before a draft lands in Notion; (2) a **checkpointed, rewindable steering session** (`PostgresSaver`) so a half-finished `steering-interview` survives interruption and can branch a draft from an earlier answer — directly targeting the "captured-and-deferred" friction; (3) the **100+ example eval set** is exactly the muscle your measurement-rigor layer and `judge-build` are building — this is the book's blueprint for it.

## Key APIs (verify against current LangGraph docs)

`InMemorySaver()` / `SqliteSaver` / `PostgresSaver` · `graph.compile(checkpointer=...)` · `config = {"configurable": {"thread_id": ...}}` · `get_state_history(config)` / `get_state(config)` / `invoke(None, config)` · `ChatOpenAI(use_responses_api=True, use_previous_response_id=True)` · `GuardrailDecision(BaseModel)` + `llm.with_structured_output(...)` · `create_react_agent(..., pre_model_hook=...)`.

_Source: Infante, *AI Agents and Applications* (Manning), Ch. 14._
