---
name: "building-mcp-servers"
description: "Use when building or consuming a Model Context Protocol (MCP) server — exposing your own tools/data as an MCP server (FastMCP), choosing STDIO vs Streamable-HTTP transport, validating with MCP Inspector, and consuming local + remote MCP tools inside a LangGraph/LangChain agent. Reach for this when you want an agent to reach a tool or data source through the MCP standard instead of bespoke glue."
---

# Building & Consuming MCP Servers

Decision-oriented reference for the **Model Context Protocol**. Paraphrased from Roberto Infante, *AI Agents and Applications* (Manning), Ch. 13 — use the book's official repo for runnable code. Especially relevant here because the Empire State stack already *consumes* MCP everywhere (Notion, HubSpot, Linear, Gamma); this skill is about *building* your own and wiring remote ones into custom agents.

## What MCP is for

MCP solves **"context integration at scale."** Without it, every agent↔tool integration is bespoke glue. With it, a service exposes tools via an **MCP server**, and any agent consumes them via an **MCP client** as if they were local functions. The integration burden shifts to the service, once, for everyone. It became a de-facto standard fast — treat it as the default interface for exposing capabilities to agents.

## When to build a server vs. just consume one

- **Consume an existing MCP server** when a vendor/tool already ships one (the common case).
- **Build your own MCP server** when: you have data/tools *you* want multiple agents (or other people's agents) to reach through one stable interface; you're re-wrapping the same tool across projects; or you want to decouple a capability from any single agent's codebase. For you, the prime candidate is exposing the **Events/Notion spine** as read tools.

## Building a server (FastMCP)

1. `from fastmcp import FastMCP`; `mcp = FastMCP("name")`.
2. Decorate each capability: `@mcp.tool(description=...)` on a (usually async) function. **The description is what the consuming LLM reads to decide when to call it** — write it like a prompt, not a code comment.
3. Run it on a transport (below): `mcp.run(transport=..., host=..., port=..., path=...)`.

### Transport choice

| Transport | Use when |
|---|---|
| **STDIO** | The server runs **locally**, co-located with the client (dev, a local tool, a CLI-launched server). |
| **Streamable HTTP** | The server is **remote** / networked / shared across clients (a hosted tool, a vendor API wrapper, anything another machine calls). |

## Validate standalone *before* wiring into an agent

Use the **MCP Inspector** (`npx @modelcontextprotocol/inspector`) to call the server's tools directly and confirm inputs/outputs. Debugging a broken tool is far easier here than inside an agent's reasoning loop. Tool results come back wrapped in a `CallToolResult`.

## Consuming MCP tools in an agent

1. `client = MultiServerMCPClient({ "myserver": {"url": "...", "transport": "streamable_http"} })`.
2. `remote_tools = await client.get_tools()`.
3. Combine with local tools: `tools = [local_tool, *remote_tools]`.
4. Feed into `create_react_agent(model=..., tools=tools, ...)` (see [[building-agents-with-langgraph]]).

**Consuming remote tools makes the loop async** — your chat loop and `main()` become `await agent.ainvoke(...)` / `asyncio.run(main())`. Local and remote tools coexist in the same agent; you can swap a local mock tool for a real remote MCP tool without changing the agent's structure.

## Gotchas

- The **tool `description`** is load-bearing — a vague description means the model won't call the tool at the right time.
- Mixing local (STDIO) and remote (HTTP) tools is fine, but remote consumption forces **async** through the whole call path.
- Validate in **Inspector first**; don't debug transport/schema issues through the agent.
- Don't confuse *building* an MCP server (this skill) with the harness's *connected* MCP servers — those are consumed, not built here.

## Map to the Empire State pipeline

Stand up a FastMCP server exposing read tools over the Notion/Supabase spine — `get_event(name)`, `list_recent_events(days)`, `find_person(name)` — validate each in MCP Inspector, then register the server into the event-content agent so drafting pulls **live** event context through one standard interface instead of ad-hoc Notion calls. This is the cleanest way to make your data agent-consumable.

## Key APIs (verify against current FastMCP/langchain-mcp docs)

`from fastmcp import FastMCP` · `FastMCP("name")` · `@mcp.tool(description=...)` · `mcp.run(transport="streamable-http"|"stdio", host, port, path)` · `MultiServerMCPClient({name: {url, transport}})` · `await client.get_tools()` · MCP Inspector: `npx @modelcontextprotocol/inspector` · `CallToolResult`.

_Source: Infante, *AI Agents and Applications* (Manning), Ch. 13._
