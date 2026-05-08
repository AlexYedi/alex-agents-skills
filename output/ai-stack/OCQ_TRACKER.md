# OCQ Living Tracker — Talent & Capital Flow + Bet Status

> Living document. Update monthly. Source of truth for the AI-stack thesis Alex is acting on.

**Last updated:** 2026-05-08
**Owner:** Alex
**Companion artifacts:** `AI_STACK_SUBSTRATE.pdf` (the map), `AI_STACK_REPORT.docx` (the prose), `AI_STACK_ADDENDUM.docx` (the framework analyses).

---

## How to use this tracker

This tracker has three operating sections you update on three different cadences:

| Section | Cadence | Owner action |
|---|---|---|
| **A. The 7 Big Bets** | Monthly | Update status, leading indicators, conviction. Mark dead bets. |
| **B. Talent & Capital Flow** | Bi-weekly | Add high-signal moves, funding rounds, ARR snapshots, public statements. |
| **C. Cruxes & Decision Triggers** | When triggered | Each crux has a measurable answer-event; log the date and re-rank bets. |

The point is **not** completeness — it's **disciplined attention** on the leading indicators that actually move bets, in a format that survives 18 months of churn.

---

## A. THE 7 BIG BETS

Each bet has: hypothesis, falsifiability, current status, leading indicators, conviction, next action.

---

### Bet #1 — The Enterprise AI Procurement Operating Standard
**The play:** Become the canonical operator-voice on how F1000 buys AI. Publish an open Procurement Playbook → use it as inbound flywheel for advisory, then productize as SaaS (procurement-readiness tool for AI vendors).

**Hypothesis:** Every F1000 stood up an "AI council" in 2024–2025 and is procuring AI vendors with 6 non-overlapping approvers (InfoSec, Legal, Privacy, AI Governance, Procurement, business sponsor). No incumbent owns the cross-counterparty workflow. A commercial operator with 12 years of buyer-side procurement scar tissue + AI-builder fluency can plant the canonical flag in 90 days.

**Falsifiability:** If the open playbook gets <500 downloads / <50 inbound conversations in 60 days, OR if Vanta/Drata/Secureframe ship a credible AI-procurement product in that window, the productized SaaS thesis is dead.

**Current status:** Unstarted. Ready to begin Q2 2026.

**Leading indicators to watch:**
- Vanta / Drata / Secureframe AI-vendor product launches (would close the window)
- F1000 AI council job postings (LinkedIn alerts; growth = market validation)
- EU AI Act enforcement actions in late 2026 (forces the issue)
- Bartz-style settlements or NYT v. OpenAI rulings (re-prices vendor terms)

**Conviction:** ★★★★★ — highest convergence across all 5 frameworks (OCQ Stratum IX/Meta-B/Meta-C, JTBD Job 4 priority, Wardley Settle quadrant, 7 Powers compliance-as-moat, Talent Flow NYC procurement migration).

**Next action:** Outline the Playbook (Week 1). 30 expert interviews (Weeks 2–6). Publish (Week 12). [See addendum Part X for the full 6/12/18-month playbook.]

---

### Bet #2 — Vertical Agent GTM Leadership Role
**The play:** Take a Director / Head of Enterprise GTM / Field CTO role at a Series B–C vertical agent company in NYC.

**Hypothesis:** Sierra ($10B/$100M+ ARR), Decagon ($4.5B/$80M+), Glean ($7.2B/$300M+), Harvey ($5B/$100M+), Hippocratic ($2B), Augment ($977M) are hiring exactly Alex's profile (12+ years enterprise B2B + AI fluency + NYC) at $300–400K base + 0.1–0.5% equity. Talent-flow data shows the dominant migration is Stripe/Ramp/Datadog/Snowflake → Sierra/Decagon/Glean.

**Falsifiability:** If 6 months of focused NYC search yields no offers in this band, either the bet on Alex's profile is wrong, or the market is more SF-anchored than the talent flow suggests.

**Current status:** Active job search. Networking ramp.

**Leading indicators to watch:**
- LinkedIn job alerts on Sierra, Decagon, Glean, Harvey, Hippocratic, Augment, Lovable
- Sierra NYC office hiring cadence (Bret Taylor's monthly NYC presence)
- Anthropic NYC enterprise headcount (proxy for whole market)
- Stripe/Ramp/Datadog → vertical-agent migrations (Pallet newsletters)

**Conviction:** ★★★★★ — Talent Flow + 7 Powers (vertical agents = most durable upper-stack power) + JTBD (CX implementation underserved) + Wardley (Settle quadrant) all converge.

**Next action:** Target 6 companies in NYC band, second-degree intros via Stripe/Ramp alumni, weekly Sierra/Decagon/Glean posting check.

---

### Bet #3 — MCP-Native Enterprise Integration Practice
**The play:** Build a small constellation of high-quality MCP servers for systems enterprise GTM teams live in (Salesforce, HubSpot, Outreach, Gong, Highspot). Distribute via marketplace + open-source; productize the build pattern as advisory.

**Hypothesis:** MCP crossed Genesis→late-Custom in Dec 2025 (Linux Foundation governance) and is crossing Custom→Product in H1 2026. Most SaaS incumbents ship zero or one MCP server. The window for "MCP server productization for enterprise SaaS" is roughly Q2–Q4 2026 — early enough to plant flags, late enough that the protocol is stable.

**Falsifiability:** If MCP forks (Anthropic vs. OpenAI proprietary tool-use schemas diverge), the entire "build at MCP layer" thesis dies. Watch for any major vendor unilaterally extending MCP without spec coordination.

**Current status:** Unstarted. Building expertise via the Procurement Playbook product first.

**Leading indicators to watch:**
- MCP registry growth (5,800 → 10K+ by EOY 2026 = ecosystem real)
- Anthropic / OpenAI / Google MCP statements (spec convergence vs. divergence)
- Cloudflare / Kong / Pomerium MCP gateway product launches (commoditization signal)
- Salesforce / HubSpot first-party MCP server announcements (incumbents arriving)

**Conviction:** ★★★★ — Wardley flagged as 2026 punctuated equilibrium; 7 Powers says network economies forming; JTBD Job 1 (sales motion) underserved. Risk = MCP fork.

**Next action:** Audit the 10 SaaS systems most lacking MCP servers in enterprise GTM (Q2 2026). Prototype one.

---

### Bet #4 — Inference Cost Optimization / FinOps for Tokens
**The play:** Productized "FinOps for Tokens" advisory: audit, recommend quantization (FP8/NVFP4/MXFP4, AWQ/GPTQ), implement speculative decoding, re-architect routing. Sell to CFO/CIO at companies burning >$50K/month on Claude/GPT.

**Hypothesis:** The median enterprise is running un-tuned vLLM on over-provisioned H100s. EAGLE-3 at 3–6.5×, FP4 quantization, prompt caching, and aggregator routing can deliver 3–10× cost reduction. The procurement-side audit is sellable today; the technical work is straightforward enough for a 2-person services team.

**Falsifiability:** AWS Bedrock auto-optimization features ship in 2026 → 12-month window slammed. OR: token prices fall fast enough that "optimization" is below the line of caring.

**Current status:** Unstarted. Highest-priority "near-term cash" play if vertical-agent role doesn't materialize fast.

**Leading indicators to watch:**
- AWS Bedrock / Azure auto-optimization product announcements
- Frontier API price changes (4–10× compression continuing or pausing)
- vLLM / SGLang adoption telemetry (Prometheus scrapes)
- NVFP4 / MXFP4 production deployment by hyperscalers

**Conviction:** ★★★★ — OCQ Stratum X 15/15. Highest-velocity-to-cash play but **explicit decay**: 12–18 month window before hyperscaler bundling absorbs the layer.

**Next action:** Free first audit for 5 mid-market AI-spending companies, build case studies, decide by Q3 2026 whether to scale or pivot.

---

### Bet #5 — Enterprise RAG Architecture Practice
**The play:** Architecture-and-procurement consulting for enterprise RAG: vector DB selection (pgvector / Pinecone / Turbopuffer / Qdrant), reranker choice, hybrid retrieval (ColBERT / SPLADE), GraphRAG implementation for vertical-knowledge workflows.

**Hypothesis:** F500 enterprises are paralyzed by 8+ vector DB options + 5 embedding choices + 3 reranker options + 4 retrieval-pattern paradigms. The decision is $50K–$500K per workload and they have no vendor-neutral guidance. Pure architecture sale; commercial fluency is the asset; technical depth required is "enough to read benchmarks," not "build a kernel."

**Falsifiability:** Long-context (Gemini 1–2M tokens, Claude prompt caching) eats RAG at the low end faster than enterprise-scale grows at the high end. Or: vector DB consolidation (1–2 winners) makes the choice trivial.

**Current status:** Unstarted. Synergistic with Bet #1 (procurement) and Bet #4 (FinOps).

**Leading indicators to watch:**
- Long-context model improvements (Gemini 3.0 context window, Claude context caching pricing)
- Vector DB M&A (MongoDB-Voyage was the first; expect 2–3 more by 2027)
- GraphRAG production deployments at named F500 (validates the high-end opportunity)
- Memory category resolution (Bet #6 below) — overlaps

**Conviction:** ★★★★ — OCQ Stratum XI 15/15; clean compounding play with #1 and #4.

**Next action:** Bundle as "Enterprise AI Architecture Audit" alongside Bet #1's Playbook → Bet #4's FinOps → this. Three-product practice, one buyer.

---

### Bet #6 — Operator's Translation Newsletter / Public Voice
**The play:** Weekly "operator's translation" newsletter — translate frontier capabilities into specific operator implications (enterprise AE / RevOps lead / GTM head). Compounds positioning for everything else.

**Hypothesis:** 200+ AI newsletters aggregate; near-zero translate. JTBD Job 3 (stay current and act on it) gap = 7 on "translating X shipped → I should change Y." A commercial operator with first-hand AI-builder practice is the rare profile that can translate authentically.

**Falsifiability:** If subscriber growth is <2K in 6 months and no inbound role/advisory comes from it, this is positioning theater. Kill at month 6 or commit harder.

**Current status:** Unstarted. Lowest cost-to-start of any bet.

**Leading indicators to watch:**
- Subscriber growth rate (target: 1K month 1 → 5K month 6)
- Inbound from VC platform teams (Lerer, FirstMark, Box Group, Primary, Insight)
- Cross-pollination with Bet #1 Playbook downloads (correlation = right audience)

**Conviction:** ★★★ — JTBD highest-leverage cross-job pattern, but execution-dependent.

**Next action:** Kit v1 published Week 2. Decide on cadence (weekly vs. biweekly) by Week 4.

---

### Bet #7 — VC Operating Partner / Platform Path
**The play:** Long-arc fallback: Operating Partner / Platform role at a Tier 1–2 NYC VC fund, focused on the AI-stack-translation work the platform team can't do themselves.

**Hypothesis:** VC platform teams need someone who can read technical updates and translate them to portfolio-company GTM teams. This is a rare combo. NYC funds (Lerer Hippeau, FirstMark, Box Group, Primary, Insight, Tiger, Forerunner, Lux, Costanoa) are visibly hiring for this profile.

**Falsifiability:** If Bets #1, #2, #3 land, this is downstream and lower-priority. If none of them do by month 12, this becomes the primary path.

**Current status:** Background networking. Not actively pursued.

**Leading indicators to watch:**
- VC platform-role postings (LinkedIn, Pallet)
- Cross-firm hires (when one fund hires this profile, others follow within 90 days)
- Bet #6 newsletter inbound from VC platform readers

**Conviction:** ★★★ — Real but secondary; ★★★★ if becomes primary.

**Next action:** Build relationships at 3 NYC funds via RAAIS / Betaworks / FirstMark MAD events. No active applications until Q4 2026.

---

## B. TALENT & CAPITAL FLOW

### B1. Senior Frontier Talent Moves (rolling 12 months)

| Date | Person | From → To | Comp | Signal |
|---|---|---|---|---|
| Jun 2025 | Alexandr Wang | Scale AI → Meta MSL (CAIO) | $14.3B Scale stake + multi-year | Meta paid for CEO-operator, not just researcher |
| Jul 2025 | Daniel Gross | SSI → Meta MSL | 9-figure | Money beat mission; SSI's perceived inviolability cracked |
| Jul 2025 | Beyer / Kolesnikov / Zhai | OpenAI Zurich → Meta MSL | ~$100M ea (rumored) | Capability clusters being acquired as units |
| Jul 2025 | Bill Peebles (Sora) | OpenAI → Meta MSL | 9-figure | Reels/Instagram pipeline use case |
| Jul 2025 | Trapit Bansal (o-series RL) | OpenAI → Meta MSL | 9-figure | Reasoning-RL leakage |
| Aug 2025 | Ruoming Pang | Apple Foundation Models → Meta MSL | ~$200M | Apple AI leadership hollowing |
| Sep 2025 | Andrew Tulloch | Thinking Machines → Meta MSL | ~$1.5B | Largest individual package on record |
| Sep 2025 | Shengjia Zhao (ChatGPT co-creator) | OpenAI → Meta MSL | 9-figure | OAI foundational cohort recruitable |
| Oct 2025 | Mira Murati | (already at TM) → continues | $2B raised at $10–12B | Largest seed in history; talent bet |
| Nov 2025 | Jan Leike | Anthropic | Retention | Anthropic alignment moat held |
| Dec 2025 | Mohan / Chen (Windsurf) | Windsurf → Google DeepMind (acqui-hire) | $2.4B licensing | New 3-party M&A template |
| Mar 2026 | Multiple Stripe/Ramp/Datadog/Snowflake AEs | → Sierra / Decagon / Glean / Hippocratic | mid-six base + meaningful equity | **The dominant pattern for Alex's profile** |
| May 2026 | Stripe/Ramp enterprise reps continued | → Decagon, Sierra, Glean (NYC + SF) | mid-six + equity | NYC vertical-agent hiring at peak |

**Read-through (May 2026):** Meta is the #1 talent destination, paying capability-cluster prices. OpenAI is #1 source of departures. Anthropic retained its core. **The Stripe/Ramp/Datadog/Snowflake → Sierra/Decagon/Glean/Hippocratic migration is the most actionable signal for Alex.**

### B2. Capital Events ($100M+ rounds, M&A, infra commits)

| Date | Event | Amount | Signal |
|---|---|---|---|
| Oct 2024 | MongoDB acquires Voyage AI | ~$220M | DBs absorbing retrieval layer |
| Jan 2025 | Stargate (OpenAI/Oracle/SoftBank/MGX) | $500B / 4yr | Watch deploy/commit ratio |
| Jan 2025 | NVIDIA closes Run:ai | ~$700M | Scheduling consolidation |
| Mar 2025 | OpenAI primary + tender | ~$40B at ~$300B | Largest private round ever |
| May 2025 | Stargate UAE 1 GW with G42 | Multi-billion | First sovereign Stargate node |
| May 2025 | Humain (KSA) AMD MI300/MI350 | $10B | KSA $40B AI PIF arm |
| Jun 2025 | CoreWeave / Meta deal | $14B | Meta de-risking from NVIDIA |
| Jul 2025 | Cursor Series C | $900M at $9.9B | First IDE company > $9B |
| Aug 2025 | Sierra Series C | $300M at $4.5B | Vertical agent thesis validated |
| Sep 2025 | OpenAI acquires Promptfoo | undisclosed | Eval/red-team internalized |
| Sep 2025 | Decagon Series C | $250M at $4.5B | CX agent layer; 2 winners viable |
| Sep 2025 | Glean Series E | $260M at $7.2B | Enterprise search-agents |
| Oct 2025 | SSI Series B | undisclosed at $32B | Pure talent bet |
| Oct 2025 | Thinking Machines seed | $2B at $10–12B | Mira's network priced |
| Oct 2025 | Anthropic Series G | $5B+ at ~$200B | ARR-driven |
| Nov 2025 | Augment Code Series B | $252M at $977M | Cursor competitor |
| Nov 2025 | US Commerce auths G42+Humain advanced chip exports | — | Diplomatic signal |
| Dec 2025 | NVIDIA acquires SchedMD | undisclosed | NVDA owns HPC scheduler |
| Dec 2025 | Cognition acquires Windsurf residual | $250M | New 3-party M&A template |
| Jan 2026 | Lovable Series A | $200M at $1.8B | Fastest EU startup to $20M ARR |
| Jan 2026 | Perplexity Series E | $500M at $18B | Comet browser pivot funded |
| Feb 2026 | Harvey Series E | $300M at $5B | Legal vertical durability |
| Feb 2026 | Hippocratic AI Series C | $150M at $2B | NYC anchor strengthening |
| Mar 2026 | Mistral Series C | €600M at €11B | EU sovereignty bet |

### B3. ARR Watchlist

| Company | Trajectory | Implication |
|---|---|---|
| Anthropic | $1B Dec'24 → $30B disputed Apr'26 | Claude Code = inflection driver; enterprise non-OpenAI demand real |
| OpenAI | $5.5B Q1'24 → $24-30B Apr'26 disputed | Consumer-heavy; enterprise via Microsoft channel |
| Cursor | <$1M → $500M+ in 24mo | IDE platform shift; Anthropic dependency |
| Lovable | $0 → $80M Q1'26 | AI app builder PMF; M&A interest H2 2026 likely |
| Sierra | $0 → $175M+ Q1'26 (400% YoY) | Vertical CX = enterprise SaaS pricing |
| Decagon | $1M 2024 → $80M Q1'26 | Sierra competitor; segment supports multiple |
| Glean | $50M 2024 → $300M+ Q1'26 | Enterprise search-agent layer |
| Harvey | $25M 2024 → $100M+ Q1'26 | Legal vertical agents |
| Perplexity | $20M Q1'24 → $200M+ Q1'26 | Margin-thin; Comet pivot tells |
| Hippocratic AI | $5M 2024 → $50M+ Q1'26 | NYC ecosystem anchor |
| Augment Code | $5M 2024 → $40M Q1'26 | Cursor competitor for enterprise |
| ElevenLabs | $25M 2024 → $200M+ Q1'26 | Voice infra dual-motion |

### B4. Public Statements as Signal (decoded)

| Speaker | Statement | Decoded |
|---|---|---|
| Dario Amodei (Anthropic) | "Most code at frontier labs is now AI-written" | Internal dogfooding = the proof point Anthropic sells |
| Sam Altman | "Compute-constrained, not idea-constrained" | GPT-5 capability-per-dollar below expectations; Stargate not deploying fast enough |
| Mark Zuckerberg | "Personal superintelligence for everyone" | MSL competing OAI on consumer, not enterprise |
| Jensen Huang | "AI factories are the new utility" | Defending $4T cap against custom-silicon erosion |
| Andrej Karpathy | "Software 3.0: English as the programming language" | Cursor/Lovable thesis validated by name |
| Bret Taylor (Sierra) | "Outcome-based pricing is how AI eats SaaS" | End of seat-based pricing in CX/agent categories |
| Aravind Srinivas (Perplexity) | "Browsers are the new OS" | Pure-search ARR can't sustain $18B; Comet rationale |
| Dario Amodei | "Within 12mo, models will write 90% of code at frontier labs" | Recruiting tool for Claude Code |

### B5. NYC Snapshot

**NYC AI companies hiring aggressively (Q2 2026):** Sierra (NYC + SF dual-HQ; Bret Taylor in NYC monthly), Hippocratic AI (NYC HQ; healthcare voice), Hugging Face (Brooklyn), Runway (Chelsea), Hex (NYC), Cohere (NYC office expanding), Anthropic NYC (small but growing — finance vertical), OpenAI NYC (sales hub), Decagon NYC presence (small), Ramp (NYC fintech, AI-product-aggressive), Scale AI Defense (residual after Wang exit).

**Events of consequence:** RAAIS NYC (Nathan Benaich), NYC AI Hub (Mayor + Cornell Tech), AI Founders NYC, AI Tinkerers NYC, Cornell Tech AI demo days, Betaworks AI Camps, Lux/USV/FirstMark portfolio events.

**People to meet:** Bret Taylor (Sierra), Munjal Shah (Hippocratic), Aman Sanger (Cursor — SF/NYC frequent), Eric Glyman (Ramp), Daniel Gross (Meta MSL — but NYC-network active), Nathan Benaich (Air Street / RAAIS), Nabeel Hyatt (Spark), Lee Edwards (Root), Matt Turck (FirstMark, MAD Landscape).

**Verdict:** NYC growing in vertical-agent GTM, shedding in foundation R&D. Favors Alex's profile.

---

## C. CRUXES & DECISION TRIGGERS

The 5 unresolved questions that, when answered, re-rank every bet.

| # | Crux | Decidability horizon | Answer-event to watch | Re-rank consequence |
|---|---|---|---|---|
| 1 | **Anthropic ARR — $24B or $30B?** | Q2–Q3 2026 (audited reports/leaks) | Anthropic financial disclosure; The Information leak; Stripe data leak | Lower bound = vertical-agent valuations compress 20–30%; upper bound = Bet #2 timing accelerates |
| 2 | **Inference compute — 10× growth or flat?** | 2026 Q4 hyperscaler earnings + Stargate deploy data | NVIDIA quarterly; Crusoe / CoreWeave disclosures; Microsoft/Google capex commentary | Flat = NVDA reprices, GPU brokerage opportunity (#4 adjacent) opens; 10× = neocloud GTM (Stratum II) goes hot |
| 3 | **MCP — commons or fork?** | H2 2026 | Major-vendor proprietary tool-use schema announcements; Linux Foundation governance turbulence | Fork = Bet #3 dies; commons = Bet #3 accelerates; either way, decide by Q3 2026 |
| 4 | **EU AI Act — teeth or paper tiger?** | First enforcement actions late 2026 | Commission guidance + first GPAI fines | Teeth = Bet #1 advisory becomes a $10B+ category; paper = Bet #1 stays niche but defensible |
| 5 | **Long-term memory — standalone or absorbed?** | 12–18 months | Anthropic / OpenAI / Google native memory feature launches | Absorbed = Mem0/Letta/Zep compress; Bet #5 RAG architecture practice gains share. Standalone = $1B+ category; consider including in Bet #5 service stack |

---

## D. STRUCTURAL RISKS (re-check quarterly)

| # | Risk | What it threatens | Watch |
|---|---|---|---|
| 1 | HBM4/CoWoS-L slip | Every 2026 capacity plan; GPU pricing | SK Hynix / Micron HBM4 ramp telemetry; TSMC capex commentary |
| 2 | Hyperscaler FCF reckoning | AI infra trade reprices; sales cycles harden 2–4 quarters | Amazon/Alphabet/Meta/Microsoft FCF Q3–Q4 2026 |
| 3 | OpenAI Preparedness adjustment-clause activation | Voluntary safety regimes destabilize | Public adjustment notice; Anthropic counter-statement |
| 4 | Federal preemption volatility on AI rules | Compliance practice repricing | Trump Dec 2025 EO court rulings; CA SB 53 lawsuits |
| 5 | Foundation labs walking up-stack into vertical apps | Vertical agent companies (Bet #2 targets) compressed | ChatGPT Business connectors; Claude for Work; Gemini Workspace agent expansion |

---

## E. UPDATE LOG

| Date | Change |
|---|---|
| 2026-05-08 | Initial creation. Big Bets ranked; talent + capital tables seeded; cruxes and risks logged. |
| _next update_ | _Bi-weekly: refresh talent + capital. Monthly: bet status + leading indicators. Trigger-based: cruxes + risks._ |

---

*This document is the working surface for the next 18 months. The infographic and the report describe the field. This tracker drives the bets.*
