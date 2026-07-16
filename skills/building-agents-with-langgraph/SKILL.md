---
name: "building-agents-with-langgraph"
description: "Use when designing or building an agent or stateful workflow with LangGraph — StateGraph design, typed state, nodes/edges, conditional branching and loops, the ReAct tool loop, prebuilt create_react_agent, and converting a linear LangChain/LCEL chain into an adaptive graph. Reach for this when a linear chain can't loop, branch, or self-correct."
---

# Building Agents with LangGraph

Decision-oriented reference for building agents and stateful workflows in **LangGraph**. Distilled and paraphrased from Roberto Infante, *AI Agents and Applications: With LangChain, LangGraph and MCP* (Manning) — buy the book and use its official GitHub repo for runnable code. This skill is the *how-to-decide* layer, not a code dump.

## First decision: do you even need a graph?

Escalate only as far as the task forces you:

1. **Single LLM call** — one bounded transform, no tools, no memory.
2. **LCEL chain** (`prompt | llm | parser`) — a fixed, linear pipeline. Predictable and cheap. **Stay here if the flow never needs to loop or branch.**
3. **LangGraph** — the moment you need **loops, conditional branches, self-correction, or persistent state across turns.** A chain that "barrels to the end even when its intermediate output is bad" is the signal to graduate to a graph.

The tell: if you catch yourself wanting the pipeline to *look at its own intermediate result and decide to try again*, you need a graph.

## The LangGraph mental model

A **typed state object flows through nodes (Python functions) connected by edges (some conditional).** That's the whole thing. It's a state machine, not a pipeline.

- **State** — a `TypedDict` whose fields thread through the graph. Node functions receive state and return a **partial update** (`return {"queries": qs}`), never a full replacement. For fields that *accumulate* (a message list), annotate with a reducer: `messages: Annotated[list, add_messages]` (`from langgraph.graph.message import add_messages` — handles append + update-by-id/de-dupe; prefer it over a bare `operator.add`). The prebuilt `MessagesState` gives you this field for free.
- **Nodes** — `graph.add_node("name", fn)`. A node is just `def fn(state) -> dict`.
- **Edges** — `add_edge("a", "b")` for a fixed hop; `add_conditional_edges("node", router_fn, {"opt": "nodeX"})` where `router_fn` reads state and returns a branch key.
- **Entry / end** — `set_entry_point("first")` and the built-in `END`.
- **Compile / run** — `app = graph.compile()`, `app.invoke(initial_state)`. Add memory with `graph.compile(checkpointer=...)` (see [[agent-memory-and-guardrails]]).

## The ReAct tool loop

An agent = an LLM that can call **tools**. Define a tool by decorating a function with `@tool`; its **name, docstring, and type hints become the schema the model reads** to decide when to call it. Bind with `llm.bind_tools(TOOLS)`. The loop is **reason → act (call tool) → observe (feed result back) → repeat** until the model can answer.

As a graph: `START → llm_node → (conditional: tool calls?) → ToolNode → llm_node → … → END`. Use the built-in **`ToolNode(TOOLS)`** to execute tools and the **`tools_condition`** edge to decide call-a-tool-vs-finish.

**Steer tool discipline through the system prompt, not just schemas** — e.g. "only call tools to find information you're missing; if the user didn't specify X, check both options." This is where most agent quality comes from.

### Hand-built vs. prebuilt

- **Hand-build the graph** when you need custom nodes, guardrail hooks, or non-standard control flow.
- **Prebuilt** — collapses the standard loop into one call. **As of LangChain 1.0 (Oct 2025) the canonical form is `from langchain.agents import create_agent`** (`model`, `tools`, `state_schema`, `system_prompt=`, and guardrail logic via `middleware`). The older `from langgraph.prebuilt import create_react_agent(model, tools, state_schema, prompt, pre_model_hook=...)` still runs but is deprecated (note `prompt` → `system_prompt`, and `pre_model_hook` → middleware). Start here; drop to a hand-built graph only when you hit its limits.

## Playbook: convert a linear chain into an adaptive agent

1. Identify each stage of the chain → make it a **node**.
2. Define a **`TypedDict` state** carrying every value that flows between stages (plus control fields like `iteration_count`).
3. Wire the happy path with `add_edge`.
4. Add an **evaluator node** that scores intermediate quality (e.g., "% of results relevant").
5. Add a **conditional edge** off the evaluator: loop back to an earlier node if quality is low **and** you're under an iteration cap; otherwise proceed.
6. **Always cap loops** (the book uses 3) so a bad run can't spin forever; on cap-hit, proceed with what you have.

That evaluator + conditional-edge + iteration-cap trio is the difference between a script and an agent.

## Gotchas

- Node functions return **partial** state updates; forgetting that clobbers other fields.
- Accumulating fields need a **reducer annotation** or each node overwrites the list.
- **Uncapped conditional loops** are the classic footgun — always bound them.
- The **agent registry is session-frozen** in this harness: adding/editing an agent file requires a fresh conversation to test (relevant when you graduate a graph into a reusable subagent).

## Map to the Empire State pipeline

`event-deep-research` is today an *engine with fan-out* — reliable precisely because it's mostly linear. The upgrade this skill unlocks: rebuild it as a LangGraph with a **Relevance Evaluator** node and a conditional edge that regenerates queries when a thin-signal event returns mostly-irrelevant results (cap 3), so it self-corrects instead of shipping a weak brief. Pairs with [[multi-agent-orchestration]] (router/supervisor shape) and [[agent-memory-and-guardrails]] (checkpoints + scope guardrail).

## Key APIs (verified against current LangGraph/LangChain docs, 2026 — v1.x)

`from langgraph.graph import StateGraph, START, END` · `StateGraph(MyState)` · `add_node` / `add_edge` / `add_conditional_edges(node, router_fn, {key: dest})` · entry point via `add_edge(START, "first")` (idiomatic) or `set_entry_point("first")` (still works) · `compile(checkpointer=...)` · `invoke(state)` · `@tool` (`langchain_core.tools`) · `llm.bind_tools(TOOLS)` · `ToolNode(TOOLS)` / `tools_condition` (`langgraph.prebuilt`) · `Command(update=…, goto="node")` (`langgraph.types`) · agent constructor: **`from langchain.agents import create_agent`** (canonical, v1) — legacy `from langgraph.prebuilt import create_react_agent` still runs (deprecated). Message-state reducer: prefer `Annotated[list, add_messages]` (`langgraph.graph.message`) over `operator.add`.

_Source: Infante, *AI Agents and Applications* (Manning), Ch. 5, 11; identifiers verified against current LangGraph/LangChain docs (2026)._
