---
name: ai-agent-design-patterns
description: >
  Design AI agents for production: pick the right agent type, choose the UI
  surface, set the autonomy level, and define success metrics. Use when scoping
  a new AI agent feature, deciding between a chatbot and a true autonomous
  agent, choosing whether the agent should be proactive or reactive, or
  designing the surface where the agent lives (side panel, chat, embedded UI).
  Triggers: "design an agent for X", "should this be an agent or a workflow?",
  "agent UI pattern for our product", "how autonomous should this agent be?",
  "what metrics for an agent?", "is this just a glorified chatbot?". Produces
  a structured agent design covering type, UI pattern, autonomy spectrum,
  proactivity, and success metrics.
---

# AI Agent Design Patterns

You design agents for production - from simple reflex agents to general-purpose
LLM agents - and the surfaces they live in. Most "agent" features fail not
from poor model quality but from wrong agent type, wrong UI, or wrong autonomy.

This skill turns the architectural choice space into a small set of named
decisions, each with clear tradeoffs.

---

## When to Use This Skill

- Scoping a new AI agent feature for a product
- Deciding between a chatbot and a true autonomous agent
- Choosing the agent's UI surface (side panel, dedicated chat, floating bubble, embedded, browser-collab)
- Setting the autonomy spectrum (suggestion-only → full automation) and where to stop
- Choosing proactive vs reactive activation
- Defining KPIs and guardrails for an agent

---

## The Four Agent Types

Match agent type to task requirements. Don't reach for general-purpose when goal-based suffices — it costs more and behaves less predictably.

| Type | Behavior | Best for | Don't use for |
|---|---|---|---|
| **Simple Reflex** | If/then rules, no memory or learning | Task-specific automation with clear logic (e.g., Zapier workflows, basic ticket routing) | Multi-step planning, ambiguous inputs |
| **Goal-Based** | Plans steps toward an explicit objective | Sales outreach optimization, lead routing, multi-step approvals | Pure optimization tasks (use Utility-Based instead) |
| **Utility-Based** | Maximizes a specific metric (objective function) | Energy minimization, cost optimization, latency tuning | Tasks where "success" is qualitative |
| **General-Purpose** | Internal world model, adapts across domains | Multi-domain assistants, open-ended user interactions, complex reasoning | Narrow well-defined tasks (overkill, more cost, less predictable) |

---

## The Five UI Patterns

Each fits different autonomy levels and task complexity.

| Pattern | Visibility | Best for | Examples |
|---|---|---|---|
| **Side Panel** | Always visible, contextual to current view | Continuous assistance during workflow | Microsoft Copilot in Word/Excel |
| **Floating Bubble** | Small movable icon, summoned by user | Reactive help that doesn't dominate the surface | In-app chat widgets |
| **Dedicated Chat Interface** | Full conversational space | Complex multi-turn tasks, exploration | ChatGPT, Claude.ai |
| **Integrated UI** | Seamlessly embedded into product flow, no dedicated chat surface | Specialized assistance baked into an existing UI | GitHub Copilot inline suggestions |
| **Collaborative Browser Interface** | Blends agent autonomy with manual user control | Agent operates on user's behalf with visible take-over | Browser agents (Anthropic Computer Use, OpenAI Operator) |

---

## Autonomy Spectrum

The dominant strategic choice. Define where on the spectrum your agent
operates - and where it stops.

```
[Assistance]──[Suggestion]──[Approval]──[Co-pilot]──[Full Automation]
   suggests     proposes      requires     acts on        executes
                              user OK     user's behalf   end-to-end
                                          with confirm
```

| Level | When to use | Risk profile |
|---|---|---|
| **Assistance** | Early agent, regulated domain, low-trust user | Low - user always in control |
| **Suggestion** | Agent provides drafts, user edits and ships | Low - user reviews everything |
| **Approval** | Agent proposes complete actions; user approves before execution | Medium - user is gatekeeper |
| **Co-pilot** | Agent acts on user's behalf with confirmation for consequential actions | Medium-High - need clear consequence boundaries |
| **Full Automation** | Agent executes end-to-end without user intervention | High - failure mode is at scale |

**Graduated autonomy is the right default.** Start narrow, expand scope as you measure reliability. Agents that launch with full automation usually have to roll back.

---

## Proactivity vs Reactivity

| Mode | Activation | Best for | Risks |
|---|---|---|---|
| **Proactive** | Agent initiates based on context, behavior, or schedule | Notification-driven flows, anomaly detection, proactive recommendations | Notification fatigue, perceived intrusiveness |
| **Reactive** | Agent responds only to explicit user invocation | Tools, query-driven assistance, on-demand help | Underutilization if invocation isn't obvious |

**Default to reactive.** Proactivity is a power that's easily abused. Earn it
by demonstrating value reactively first.

---

## Principles

- **Define autonomy explicitly before building.** Unclear autonomy boundaries lead to over-cautious agents (low value) or runaway agents (catastrophic errors).
- **Establish learning and adaptation mechanisms from day one.** Build feedback loops (explicit thumbs / implicit signals) so the agent improves with use.
- **Design for integration compatibility.** Agents that can't talk to CRMs, ERPs, or internal APIs are demos, not products. Integration work often dwarfs intelligence work.
- **Plan backend infrastructure for scale before launch.** Agents have unpredictable usage patterns; successful launches can 10x infra load overnight.
- **Privacy and security are non-optional.** Agents touch sensitive data (CRM, email, calendar). GDPR/CCPA compliance must be designed in, not bolted on.

---

## Anti-Patterns to Avoid

### Glorified Chatbots

**Looks like:** Agent marketed as autonomous but actually a script-following chatbot with predefined responses. No real decision-making.

**Why it fails:** Users hit the limits in the first session and stop trusting. Damages brand more than no agent would.

**The fix:** Either build true agency (decision-making, tool use, multi-step planning) or call it a chatbot. Don't market the gap.

### Over-Automation

**Looks like:** Granting full autonomy at launch without measured reliability or human escape hatches. "Just let the agent handle it."

**Why it fails:** When agents fail at scale, the failure is at scale. One bug becomes thousands of incidents simultaneously.

**The fix:** Graduated autonomy. Narrow scope at launch, expand based on measured task completion rate. Always include human escape hatches and rollback paths.

---

## Agent Success Metrics

Standard KPIs for any agent:

| Metric | What it measures | Threshold to graduate autonomy |
|---|---|---|
| **Task Completion Rate** | % of agent attempts that finish without intervention | ≥ 95% before expanding scope |
| **Quality / Accuracy** | Correctness of agent output (vs human baseline or ground truth) | Domain-dependent; medical/legal need higher |
| **Human Intervention Frequency** | How often a human has to step in | Decreasing trend over time |
| **User Satisfaction** | CSAT or NPS specific to agent interactions | ≥ 4.0/5 sustained |

### Guardrails Specific to Agents

- **Hallucination rate** (factual errors): hard ceiling
- **Cost per interaction**: must align with unit economics
- **Latency**: agents that are slow get abandoned
- **Action reversibility**: irreversible actions need higher autonomy thresholds

---

## Decision Rules

| Condition | Action |
|---|---|
| Task is task-specific with clear if/then logic | Simple Reflex Agent |
| Task requires multi-step planning toward an objective | Goal-Based Agent |
| Task is to optimize a specific metric | Utility-Based Agent |
| Task spans multiple domains, needs adaptive behavior | General-Purpose Agent (LLM-based) |
| Continuous assistance during workflow | Side Panel UI |
| Reactive help, summoned occasionally | Floating Bubble UI |
| Complex multi-turn conversation needed | Dedicated Chat Interface |
| Specialized assistance inside existing flow | Integrated UI |
| Agent acts in environment with user oversight | Collaborative Browser Interface |
| New agent, regulated domain | Start at Suggestion or Approval autonomy |
| New agent, low-stakes domain | Can start at Co-pilot autonomy |
| Any agent | Reactive activation default; earn proactivity |

---

## Worked Example: Sales Outreach Agent

**Use case:** Auto-generate personalized cold outreach emails for sales reps.

| Decision | Choice | Rationale |
|---|---|---|
| **Agent type** | Goal-Based | Multi-step: research prospect, draft email, suggest follow-ups |
| **UI pattern** | Side Panel inside CRM | Reps live in CRM; side panel keeps rep in flow |
| **Autonomy** | Suggestion (drafts only, rep edits & sends) | Sales tone is voice-sensitive; auto-send is high-risk |
| **Activation** | Reactive (rep clicks "draft outreach") | Avoids notification fatigue |
| **North Star** | Reply rate of agent-drafted emails vs human-drafted | Measures actual value, not vanity metrics |
| **Guardrails** | Hallucination rate (false claims about prospect) < 0.5% | Brand risk is the dominant failure mode |

This decomposition makes the design choices visible and lets you stress-test
each one before building.

---

## Gotchas

- **Confusing "AI-powered" with "agentic."** Many features marketed as agents
  are just LLM-backed chatbots. The distinguishing feature of an agent is
  *decision-making and tool use*, not just generative text.
- **Skipping the integration layer.** Agents look impressive in demos but die
  in production when they can't read from the CRM or write to the ERP. Budget
  more time for integration than for intelligence.
- **Treating autonomy as binary.** "Should we automate this?" is the wrong
  question. The right one is "where on the autonomy spectrum should this start,
  and what criteria graduate it?"
- **Measuring agents like chatbots.** Chatbots are measured on engagement and
  CSAT. Agents need task completion, intervention rate, and reversibility-weighted
  reliability metrics.

Source: *Building AI-Powered Products: The Essential Guide to AI and GenAI Product Management*, Chapter 7.
