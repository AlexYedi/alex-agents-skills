---
name: "multi-agent-orchestration"
description: "Use when deciding how to split work across multiple agents — single agent vs router vs supervisor — and how to wire them in LangGraph. Covers the router (one-way dispatch) and supervisor (agent-of-agents, return-ticket) patterns, routing logic, structured-output dispatch, and folding a scope guardrail into the router. Reach for this when one agent with a few tools is no longer enough."
---

# Multi-Agent Orchestration

Decision-oriented reference for coordinating multiple agents. Paraphrased from Roberto Infante, *AI Agents and Applications* (Manning), Ch. 12 — use the book's repo for runnable code. Complements [[building-agents-with-langgraph]] (the graph mechanics) and [[ai-agent-design-patterns]].

## The core decision: single vs. router vs. supervisor

Pick the **least** structure that covers the task:

| Topology | Shape | Choose when |
|---|---|---|
| **Single ReAct agent** | one LLM + a handful of tools | One domain; no need to isolate scope or specialize sub-behaviors. |
| **Router** | top agent classifies → hands to exactly one specialist → specialist answers and **terminates** (one-way ticket) | Requests split into **distinct, non-overlapping** capabilities, and each request belongs to exactly one specialist that can answer alone. Cheapest multi-agent shape. |
| **Supervisor** ("agent of agents") | specialists are treated **as tools**; a specialist hands control **back** to the supervisor, which can call another, loop, or synthesize (**return-ticket**) | A request needs **coordination, iteration, or synthesis across** multiple specialists — a single hand-off can't complete it. |

The one-line test: **one-way vs. return-ticket.** If a specialist can finish the job and stop, use a router. If the hub must get control back to combine or continue, use a supervisor.

## Building a router (LangGraph)

- `StateGraph(AgentState)` with a `router_agent` node plus one node per specialist.
- The router node runs an LLM with **structured output** to pick a destination: define an `Enum` of agent types and a Pydantic model (`AgentTypeOutput{agent: AgentType}`), `llm.with_structured_output(AgentTypeOutput)`, then the node returns `Command(update=state, goto=response.agent.value)`.
- Each specialist edges to `END`; the router is the entry point; compile with a checkpointer for memory.

### Fold the guardrail into the router (fail-fast)

Before routing, run a cheap classifier LLM. If the request is out of scope, emit a refusal `AIMessage` and route to a **no-op `guardrail_refusal` node wired straight to `END`** — so off-topic requests never reach (or cost) a specialist. This is the canonical "reject before you spend" shape. Two reasons it matters: **accuracy** (off-domain questions hallucinate) and **cost** (stops abuse of your agent as a free gateway to an expensive model). See [[agent-memory-and-guardrails]].

## Building a supervisor

Build it like a ReAct agent, but pass it a **list of agents as tools** and a **high-grade model** (the coordination decisions are the hard part). The supervisor invokes agents, receives their returns, decides whether to call another or re-query, and synthesizes the final answer. In current LangChain (1.0), build the agent with `from langchain.agents import create_agent`; there's also a dedicated `langgraph-supervisor` package (`pip install langgraph-supervisor`, `create_supervisor`) if you want the pattern prebuilt — though the maintainers now recommend the direct agents-as-tools approach above for most cases (more control over context engineering).

## Gotchas

- **Router misclassification is silent** — it routes to the wrong specialist and you only notice in the output. Add few-shot examples to the routing prompt, define a **default/fallback route**, and trace routing decisions.
- **Don't reach for a supervisor when a router suffices** — the return-ticket loop adds cost and failure surface. Overlapping specialties or multi-part requests are the only real justification.
- Keep **each specialist's own guardrail** even behind a router (belt-and-suspenders): a specialist may be reused in a context where the router isn't in front of it.

## Map to the Empire State pipeline

The four research specialists (`company-researcher`, `person-researcher`, `topic-landscape-analyst`, `competitive-signal-scanner`) are today a **parallel fan-out** — a supervisor's fan-out *without* the return-ticket loop. Two upgrade paths: (a) formalize as a **router** if each request cleanly belongs to one specialist, with a scope guardrail rejecting non-event asks before any specialist spend; (b) go **supervisor** if you want the hub to receive each return, decide whether to re-query, then call the synthesizer. Note the SDK constraint recorded in the project: subagents can't spawn subagents, so any fan-out runs from the parent thread — a router/supervisor graph is the clean way to express that from one place. Full constraint set + the authoring skeleton: `references/claude-code-sdk-constraints.md` and `references/orchestration-authoring-skeleton.md`.

## Key APIs (verified against current LangGraph/LangChain docs, 2026 — v1.x)

`StateGraph(AgentState)` · `class AgentType(str, Enum)` · `llm.with_structured_output(AgentTypeOutput)` · router node returns `Command(update=state, goto=agent_name)` (`from langgraph.types import Command`) · `add_edge(agent, END)` · entry via `add_edge(START, "router_agent")` (idiomatic) or `set_entry_point("router_agent")` (still works) · supervisor agent = **`from langchain.agents import create_agent`** (v1 canonical; legacy `langgraph.prebuilt.create_react_agent` still runs) given agents-as-tools + a strong model, or the prebuilt `create_supervisor` from the `langgraph-supervisor` package (verified 2026-07-16 vs PyPI + the LangChain reference docs; maintainers now favor the direct agents-as-tools path above).

_Source: Infante, *AI Agents and Applications* (Manning), Ch. 12; identifiers verified against current LangGraph/LangChain docs (2026)._
