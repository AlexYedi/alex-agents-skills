# C6 — Cross-Function Platforms

**Wave 1 · Matrix cell: Cross-cut (spans M = 1..12, N = A..M)**
**Author:** Alex Yedi · **Date:** 2026-05-12 · **Voice:** OCQ_TRACKER register
**Companions:** `OCQ_TRACKER.md`, `AI_AGENTS_TRACKER.md`, `framework_analysis/B6_seven_powers.md`
**Word target:** ≤2,200

---

## 1. Framing — The Horizontal-vs-Vertical Bet, Named

The cross-function platform category is where 2026 enterprise AI spend actually *lands* on the P&L — and where Helmer's 7 Powers screen is most punishing. Two structural patterns compete:

- **The AI-native horizontal challenger** (Glean, Clay, Hebbia, Rogo, Notion AI) — built greenfield on LLM substrate, sells horizontally across functions, claims "one assistant for the whole company" or "data layer for the whole GTM stack."
- **The incumbent-with-AI** (Salesforce Agentforce, HubSpot Breeze, Microsoft 365 Copilot, Google Workspace Gemini, ServiceNow AI Agents, Workday, Oracle) — bolts agentic features onto an installed graph of data, identity, and workflow that already owns Switching Costs flavor.

**Named bet:** *Verticals beat horizontals on capability-per-cell, but incumbents beat both on cell-coverage breadth where the data graph is already owned.* The AI-native horizontal challenger pattern only survives where (a) the incumbent's data graph is fragmented (Glean's wedge: cross-SaaS search where Microsoft's Graph stops at the M365 boundary), or (b) the workflow is structurally outside the incumbent's surface (Clay: enrichment-as-pipeline that doesn't fit inside Salesforce's per-record edit model). Everywhere else, **the incumbent's cell-coverage breadth wins the F1000 procurement even when the AI-native challenger's per-cell capability is superior** — because the buyer has already paid the Switching Costs and the AI feature is bundle-priced.

This is the cell-coverage version of the classic "best-of-breed vs. suite" debate, and the answer in 2026 GTM specifically is: **suite wins where the suite already owns the system of record; best-of-breed wins where the data lives outside it.** The corollary for Bet #2 is that vertical-agent equity is still the most durable career play, but the second-most durable is to be inside the incumbent's AI org (Salesforce Agentforce, Microsoft Copilot for Sales) at the moment cross-function bundling closes the window on horizontals.

---

## 2. Platform-by-Platform — Cell Coverage Map

### 2.1 AI-Native Horizontal Challengers

**Glean** [IX] — Cell coverage: (M=7 marketing-content-retrieval, 8 RevOps-data-retrieval, 10 enablement, 11 ops). Stratum IX. *Series E $260M @ $7.2B Sep 2025.* ARR $50M→$300M+ Q1'26. **Powers:** Network Economies (vertical-bounded org-data graph compounding with internal usage), Switching Costs (cross-system identity + permission inheritance). **OCQ ~17/20.** Glean App Marketplace launched late 2025 — *the closest thing to network economies forming at the enterprise-search layer*. Encroachment risk: ChatGPT Business connectors (Mar 2026), Microsoft Copilot Studio cross-tenant. Glean's durability question is whether org-graph density compounds faster than Microsoft can ship cross-tenant Copilot.

**Clay** [IX] — Cell coverage: (M=1 prospecting, 4 enrichment, 5 outbound, 8 RevOps). Stratum IX. *Growth $100M @ $1.5B Jan 2026.* ARR $20M→$80M+. **Powers:** Switching Costs (waterfall logic, custom enrichment recipes that took quarters to author) + emerging Process Power on the enrichment-orchestration layer. **OCQ ~16/20.** The only durable RevOps winner per 7 Powers screen. Clay's defensibility is the data-orchestration recipe layer, not the underlying enrichment vendors (which are commoditizing).

**Hebbia** [IX] — Cell coverage: (M=7 research synthesis, 8 analyst workflows). Stratum IX. *Series C rumored Q2 2026.* NYC HQ; financial-services and consulting customer base (Sivulka public on MBB sourcing). ARR $30M→$50M+. **Powers:** Switching Costs (analyst-workflow muscle memory; matrix-style report templates). **OCQ ~14/20.**

**Rogo** [IX] — Cell coverage: (M=7 IB/PE research, 8 financial analysis). Stratum IX. *Series B $50M @ $400M Jan 2026.* NYC HQ; financial-services-specific. ARR <$5M→$30M+. Closest "verticalized horizontal" to Hebbia. **OCQ ~13/20** (lower than Hebbia on cell-density but higher on TTM given the under-funded ratio).

**ZoomInfo Copilot** [IX] — Cell coverage: (M=1 prospecting, 4 enrichment). Stratum IX. Incumbent-with-AI pattern but losing share to Clay on the orchestration layer. **OCQ ~10/20** — power eroding; the data asset is the moat but Clay routes around it.

**Notion AI** [IX/X] — Cell coverage: (M=9 marketing-content drafting, 10 enablement-doc generation, 11 ops/PMM). Stratum IX bleeding into X. *Notion has 100M+ users; AI add-on ~$10/seat.* **Powers:** Switching Costs on the doc graph itself; AI is feature, not power. **OCQ ~11/20.**

### 2.2 Incumbents-with-AI

**Salesforce Agentforce** [IX] — Cell coverage: (M=1 lead-routing, 2 SDR-augmentation, 3 AE-coaching, 4 enrichment, 5 sequencing, 6 forecasting, 7 marketing-cloud, 8 RevOps-data, 9 customer service, 10 enablement, 11 ops, 12 finance-handoff). *Effectively every GTM cell.* Stratum IX. **Powers:** Switching Costs (CRM lock-in), Scale Economies (channel), early Network Economies via AgentExchange. **OCQ ~17/20.** AgentExchange launched Dec 2025 — the most credible suite-incumbent agent marketplace. The Agentforce 2.0 push (Q1 2026) pricing at $2/conversation reframes outcome-pricing as a suite feature.

**HubSpot Breeze** [IX] — Cell coverage: (M=1–6 SMB/mid-market full GTM funnel). Stratum IX. **Powers:** Switching Costs in SMB segment; weaker enterprise position than Salesforce. **OCQ ~14/20.** Breeze Copilot, Breeze Agents (Content, Social, Prospecting, Customer), Breeze Intelligence (enrichment, formerly Clearbit) — *the most coherent SMB cross-funnel AI suite.* Breeze Intelligence's Clearbit acquisition (Nov 2023, productized 2025) is the only Clay-substitute inside a CRM.

**Microsoft 365 Copilot for Sales** [IX/X] — Cell coverage: (M=1–6 cross-funnel) + (Capability K computer-use via Recall + Copilot in Windows, L persistent memory via Microsoft Graph, M trajectory observability via Microsoft 365 Compliance Center). Stratum IX/X. *30M+ paid seats Q1 2026; $5B+ ARR.* **Powers:** Switching Costs (M365 + Graph + Entra ID + Purview), Scale Economies (channel + bundle), Cornered Resource on enterprise-identity-as-substrate. **OCQ ~18/20 — the highest cell-coverage breadth in the matrix.** Copilot Studio (Nov 2024 GA, expanded 2025) is the agent-builder layer; Copilot in Dynamics 365 Sales is the GTM-specific surface. **The incumbent with the most defensible cross-function play, full stop.**

**Google Workspace Gemini for Sales** [IX/X] — Cell coverage: similar to M365 Copilot but weaker in CRM-adjacent functions; stronger in cross-app reasoning via Gemini 3.0 long-context. Stratum IX/X. **OCQ ~14/20.** Gemini in Sheets/Docs/Gmail for sellers; partnership with Salesforce on bidirectional data (announced 2025). Trajectory observability via Workspace audit + Vertex Model Armor.

**ServiceNow AI Agents** [IX] — Cell coverage: (M=9 customer service, 10 IT-service enablement, 11 ops). Stratum IX. NowAssist + Agentic AI offerings (re-launched late 2025) targeting cross-function service workflows. **Powers:** Switching Costs (workflow-platform lock-in in IT/HR/CS). **OCQ ~14/20.**

**Workday Agents** [IX] — Cell coverage: (M=11 ops, 12 finance, HR cross-function). Stratum IX. Workday Illuminate (2024) + Agent System of Record positioning (2025). Less GTM-specific; finance-meets-GTM bleed only. **OCQ ~10/20** for GTM scope.

**Oracle AI Agents** [IX] — Cell coverage: (M=11 ops, 12 finance) via Fusion Apps. Stratum IX. **OCQ ~8/20** for GTM scope.

### 2.3 Document & Communication Platforms

**Box AI** [IX] — Cell coverage: (M=7 content, 10 enablement). Stratum IX. Box Hubs + Box AI Agents; Aaron Levie's positioning as "content-as-agent-substrate." **OCQ ~10/20.**

**Dropbox Dash** [IX/X] — Cell coverage: (M=7 search, 10 enablement). Stratum IX/X. *Dropbox acquired Command E 2023 → Dash 2024 GA → enterprise tier 2025.* Glean-lite for SMB/mid-market. **OCQ ~9/20.**

**Slack AI** [IX] — Cell coverage: (M=8 RevOps-conversational, 9 customer-service-internal). Stratum IX. Slack AI summaries + Agentforce-in-Slack (Salesforce ownership). **OCQ ~12/20** — power inherited from Salesforce.

**Microsoft Teams AI** [IX] — Cell coverage: (M=2 SDR-conversational, 3 AE-meetings, 9 service). Stratum IX. Copilot-in-Teams + Intelligent Recap + Sales Copilot in Teams. **OCQ ~14/20** — power inherited from M365.

---

## 3. The Gateway-Control-Plane Cell (Bet #3 Anchor)

This is the durable power location at the MCP layer and the anchor cell for Bet #3's reframe per Session A's deltas.

**The setup.** MCP crossed Genesis→late-Custom Dec 2025 (Linux Foundation governance). Registry hit 11,400 servers Apr 2026, on track to 20K+ by EOY. **By 7 Powers strict reading, MCP itself is not a moat — it's a non-exclusion protocol by design.** But the *gateway/control plane wrapping MCP* accumulates real Switching Costs: once an F500 has 30+ MCP servers wired through Kong's AI Gateway with SSO, audit, rate-limits, and secret-injection, ripping it out is a year of work. This is the cell where Bet #3 advisory practice anchors.

**Cloudflare AI Gateway / MCP Gateway** — *Launched as full MCP Gateway H2 2025; Workers AI + AI Gateway + Vectorize + Durable Objects stacked underneath.* Cloudflare's edge-distribution + Workers integration is the cleanest path to "every enterprise MCP server runs through a Cloudflare-managed control plane." **Powers:** Scale Economies (edge POPs), emerging Switching Costs (one-click MCP-server deploy + observability). **OCQ ~16/20.** The single highest-OCQ name in this cell.

**Kong AI Gateway** — *AI Gateway GA Q2 2024; agentic extensions 2025.* Kong's enterprise-API-gateway installed base is the substrate; AI Gateway extends prompt-guard, semantic-routing, token-cost-accounting, MCP-proxy. **Powers:** Switching Costs (enterprise gateway lock-in already exists; AI is a feature extension that compounds it). **OCQ ~14/20.**

**Pomerium** — *Zero-trust identity-aware gateway; AI-policy enforcement extensions 2025.* Narrower wedge than Cloudflare or Kong but credible on the identity-as-policy axis. **OCQ ~11/20.**

**Identity-for-agents (gateway-adjacent):** Auth0 Agent Identity, Okta Agent Identity, Clerk. Stratum IX. *Okta Agent Identity announced Oktane 2025; Auth0 — now an Okta unit — extended FAPI 2.0 + DPoP for agent flows.* Clerk added agent-token APIs Q1 2026. **Powers:** Switching Costs via SSO + audit lock-in. **OCQ:** Okta ~13/20, Auth0 ~12/20, Clerk ~10/20.

**Eval-gateway adjacencies:** Lakera Guardrails (runtime safety injection at gateway layer), Galileo (eval gateway, Series C rumored ~$60M Apr 2026), Arize Phoenix (open-source observability at the gateway hop). Stratum VII bleeding into the gateway cell. **OCQ:** Lakera ~12/20, Galileo ~11/20, Arize ~10/20.

**Advisory practice anchor.** The Bet #3 reframe per `AI_AGENTS_TRACKER.md §A` is: *advisory + gateway-adjacent, not productized MCP servers.* The claim: a procurement-fluent operator who has done the gateway-selection conversation 10+ times — *which gateway for which auth model, which audit posture, which rate-limit policy, which secret-injection pattern, how to grade third-party MCP server quality, how to map gateway controls to EU AI Act Article 14 oversight requirements* — earns Process Power flavor that no software vendor can ship as a SKU. Pair-with-Cloudflare positioning is the highest-leverage entry (largest distribution, cleanest documentation, most credible enterprise-edge story). Cloudflare doesn't need an advisory partner to win mid-market; it does need one to land F100 procurement with the InfoSec / AI-Governance / Legal triad signed off in 90 days. That gap is exactly where the Bet #1 Playbook + Bet #3 advisory bundle converts.

**The hidden adjacency:** Salesforce AgentExchange and Glean App Marketplace are *also* gateway-control-plane plays, just inside a vendor walled garden. If MCP forks (Crux C2), these marketplaces eat the standalone-gateway TAM. If MCP holds as commons, the standalone gateways (Cloudflare, Kong) compound. Watch Crux C2 with this cell in mind.

---

## 4. Horizontal vs Vertical Thesis — Verdict

**Verticals beat horizontals at the cell level; incumbents beat both at the suite level; gateways win the middle.** The cleanest F1000 procurement pattern Q2 2026 is: (a) Microsoft 365 Copilot or Salesforce Agentforce as the suite floor, (b) Glean or Clay as the cross-SaaS challenger where the suite's graph stops, (c) Sierra / Harvey / Glean / Abridge / Hippocratic / Rogo as the vertical winners-take-most, (d) Cloudflare or Kong as the MCP gateway underneath. Pure horizontals without a data-graph wedge (Notion AI, generic Copilots) get bundled into the suite. **The AI-native horizontal challenger pattern is real but bounded by where the incumbent's graph doesn't already exist.** Microsoft via M365 Graph is the most defensible cross-function play; Salesforce via the AgentExchange + Data Cloud combo is the closest second.

---

## 5. Top 4 Opportunities Ranked by OCQ

1. **Microsoft 365 Copilot for Sales / Copilot Studio role (OCQ ~18/20).** The largest installed-base + highest cell-coverage breadth in the matrix; NYC enterprise-AI org hiring through 2026. *Highest-leverage incumbent-with-AI seat for Alex's profile.*
2. **Salesforce Agentforce GTM / AgentExchange ecosystem role (OCQ ~17/20).** Cross-function bundle authority; outcome-pricing reframe in market; NYC presence growing. *Direct competitor seat to Microsoft Copilot for Sales path.*
3. **Cloudflare MCP Gateway advisory partnership (OCQ ~16/20, Bet #3 anchor).** The highest-OCQ gateway-control-plane vendor; pair-with positioning is the cleanest Bet #3 entry. *Most credible advisory practice anchor.*
4. **Glean enterprise GTM role (OCQ ~17/20, Bet #2 holdover).** Highest Network Economies in the upper stack; org-graph density compounding. *Highest-power AI-native horizontal challenger seat.*

---

## 6. Top 2 Challenges

1. **Incumbent absorption inevitability.** Microsoft 365 Copilot at 30M paid seats Q1 2026 + Salesforce Agentforce at suite-bundle pricing means horizontal-challenger TAM is structurally capped to the wedges where the incumbent graph doesn't exist. Glean's question is whether it crosses $1B ARR before Microsoft ships credible cross-tenant Copilot. Clay's question is whether RevOps procurement frames it as "enrichment-orchestration" (durable) or "Salesforce add-on" (bundled).
2. **Gateway commoditization via vendor walled gardens.** Salesforce AgentExchange and Glean App Marketplace each replicate the gateway-control-plane locally; if MCP forks (Crux C2), the standalone-gateway TAM collapses into vendor marketplaces and Bet #3 advisory window narrows to 12 months instead of 24+.

---

## 7. Top 2 Open Questions

1. **Does the Microsoft Graph become the AI substrate for GTM specifically?** If Copilot in Dynamics 365 Sales + Copilot Studio + Microsoft Graph + Purview compliance ships as a unified procurement bundle by EOY 2026, the AI-native horizontal challenger TAM compresses 30%+ and Bet #2 valuations at Glean / Clay reprice. Watch Microsoft Ignite Nov 2026 announcements.
2. **Does Cloudflare or Kong consolidate the MCP gateway category, or does it stay three-way (plus Pomerium plus hyperscaler-native)?** Three-way persistence means the advisory window stays open for Bet #3; consolidation to one winner shrinks it to a single pair-with relationship. Watch H2 2026 funding and partnership announcements.

---

*End C6. Word count ~2,180.*
