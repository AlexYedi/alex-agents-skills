# Chapter 4 — Operating Tracker (Agent Layer)

This is the agent-layer sub-tracker. It runs at higher resolution than the parent (V1 Ch 4) and feeds it: when a conviction, ARR figure, or crux status moves here, the delta propagates back to V1 Ch 4 on the next monthly ritual. The same touch-surface discipline carries over from V1 — bi-weekly talent and capital, monthly bet refresh, trigger-based crux and risk events — applied to the agent slice specifically.

Three things make this tracker different from the parent. First, the agent-layer cycle time is faster: vertical-agent ARR multiples, MCP governance moves, and OSWorld scores reprice on 4–8 week intervals, not the 6–9 month intervals that matter at full-stack. Second, the NYC concentration is over-weighted here because Bet #2 is NYC-anchored and the May 2026 hiring market is at a historic peak. Third, the OSWorld sub-crux (§4.8) is V3-specific — it does not appear in V1 because it sits inside the agent-layer Crux #2 + #5 envelope but resolves on its own answer-event.

If a session opens with 15 minutes, update §4.2 (bet deltas) and §4.3 (talent). If 5 minutes, log a single row anywhere. If 60 minutes, run the monthly ritual end-to-end and write the §4.10 update-log entry. Add columns to the tables sparingly; the schema is designed to be re-readable a year out.

## §4.1 How to use & update cadences

Cadences defer to V1 Ch 5 §5.1–§5.4 for the underlying rituals. V3 updates ride alongside V1 updates — when a monthly conviction pass fires in V1, it fires here if any agent-layer delta has moved. V3-specific trigger-based events (OSWorld benchmark crossings, ASL-4 announcement, MCP governance decisions) live in §4.8.

| Cadence | What updates | Where (in this chapter) | Defers to |
|---|---|---|---|
| Bi-weekly | Talent moves, capital events | §4.3, §4.4 | V1 Ch 5 §5.1 |
| Monthly | V3-delta bet status, conviction | §4.2 | V1 Ch 5 §5.2 |
| Quarterly | ARR watchlist, public statements, NYC snapshot, risk re-check | §4.5, §4.6, §4.7, §4.9 | V1 Ch 5 §5.3 |
| Trigger-based | Cruxes resolved, OSWorld crossings, ASL-4 events | §4.8 | V1 Ch 5 §5.4 |

The bi-weekly cadence is the metronome at this resolution; senior moves into Sierra, Decagon, Glean, Hebbia, Rogo, Hippocratic, and Clay are the most predictive leading indicator for Bet #2 timing. When a senior move logs, ask the same monthly question one week early: does this re-rate the bet, or just confirm the prior? If it only confirms, keep the conviction unchanged.

When V3 logs a bet conviction change, write the parallel V1 Ch 4 update in the same session. The two tracker files diverging in conviction without an explicit delta note is the single highest-cost failure mode — it forces re-reconciliation later, and re-reconciliation laundered through memory is contaminated.

## §4.2 Bets status board (V3 deltas)

Compact view of the seven bets at agent-layer resolution. Full hypotheses and falsifiability live in Ch 3. This board is the monthly conviction-rating surface and shows where V3 deltas from V1.

| # | Bet (compact) | V3 Conviction | V3 Status | Delta from V1 |
|---|---|---|---|---|
| 1 | Enterprise AI Procurement Standard (agent overlays) | ★★★★★ | Unstarted; ready Q2 2026 | **Sequenced first** in V3 (was implicit third in V1); +7 agent-specific overlays named (tool-boundary, indirect-injection red-team, action-rollback, sub-agent privilege, signed evals, EU Art 14 tie-out, sectoral) |
| 2 | Vertical Agent GTM Role (NYC) | ★★★★★ | Active; search ramping | NYC target list expanded — Hebbia, Rogo, Clay, Runway, Ramp AI added; MBB consulting feed-stock surfaced as third path |
| 3 | MCP-Native Enterprise Integration | ★★★★ | Unstarted | **Reframed** — from "build MCP servers" to advisory + gateway-adjacent (Cloudflare / Kong / Pomerium); productized form drops in conviction |
| 4 | Inference Cost Optimization (FinOps) | ★★★★ | Unstarted | **Split** into per-token + per-trajectory; per-trajectory window narrowed to ~12 months ahead of hyperscaler auto-routing H2 2027 |
| 5 | Enterprise RAG + Memory Architecture | ★★★★ | Unstarted | Memory folded in as service line (no separate memory practice bet) per Crux #5 directional answer |
| 6 | Operator's Translation Newsletter | ★★★ | Unstarted | Confirmed as distribution layer for Bets #1–#3; angle sharpens to Conclude-phase translation |
| 7 | VC Operating Partner / Platform | ★★★ | Background; ★★★★ contingent | Carey Lai (Insight → Sierra Apr 2026) + 3–5 similar moves confirm platform/operator convergence at senior level |

Conviction scale matches V1: ★★★★★ "convergent across all 5 frameworks, near-term cash or career-defining"; ★★★★ "strong with one explicit failure mode"; ★★★ "real but secondary or execution-dependent". The largest single V3 delta is Bet #1 sequencing — the five-framework convergence at agent-layer resolution flips it to first.

## §4.3 Senior moves into agent-specific companies (rolling 12 months)

Bi-weekly. The vertical-agent flow is the dominant Bet #2 leading indicator. Add rows above the read-through paragraph.

### Vertical agent companies

| Date | Person | From → To | Role | Signal |
|---|---|---|---|---|
| Jun 2025 | Brittany Bohnet | DeepMind PM lead → Sierra | VP Product | Founder-team |
| Jul 2025 | Joe Schmidt IV | Stripe Enterprise (NYC) → Sierra | Head Enterprise GTM East | **GTM — Alex match-fit** |
| Sep 2025 | Ashutosh Sinha | Datadog VP CE → Decagon | Field CTO | GTM/SE leadership |
| Sep 2025 | 4+ Stripe NYC enterprise AEs | → Decagon NYC | Enterprise AE | $220–280k base + ~0.05% (inf); Alex cohort |
| Oct 2025 | Tamar Yehoshua (ex-Slack CPO) | board → Glean | CPO | Founder-team; ~1% (inf) |
| Nov 2025 | Mike Yu | Snowflake Field Eng dir → Glean | Director Field Eng East | GTM/SE |
| Nov 2025 | Cravath/A&O associates (multiple) | BigLaw → Harvey | Solutions / FDE | Legal-SE adjacent |
| Jan 2026 | Yash Tekriwal | Goldman MBD VP → Rogo | Head Enterprise Sales | **GTM — NYC match-fit** |
| Feb 2026 | Vivek Raghunathan | Meta AI Infra → Sierra | Head Platform Eng | Founder-team; 9-figure (rumor) |
| Mar 2026 | Multiple Ramp+Brex enterprise reps | → Sierra / Decagon / Glean | AE / CSM | **Peak cohort month — 8+ named LI moves into top three** |
| Mar 2026 | Divya Mehta | Stripe Enterprise → Hebbia | VP Revenue (NYC) | **Alex match-fit, NYC** |
| Mar 2026 | Adobe/Frame.io alumni | → Runway Enterprise | GTM | NYC creative wedge |
| Apr 2026 | Carey Lai | Insight Partners principal → Sierra | VP Strategy | VC→operator pattern (Bet #7) |
| Apr 2026 | Lukas Petersson | ex-Spotify product → Lovable | Head of US | Lovable US push |

### Departures (signal — who is leaving)

| Date | Event | Read |
|---|---|---|
| Jun 2025 | Mid-2025 GTM exits from 11x → recruiting-AI stealth | First public crack in 11x team |
| Sep 2025 | Cresta enterprise AEs → Sierra / Decagon | Cresta becoming feed-stock |
| Oct 2025 | Hayden Sukkar public from 11x | Tacit "synthetic SDR quality ceiling" admission |
| Dec 2025 | Adept research residual → Anthropic / Sierra | Adept fully dispersed |
| Jan 2026 | Inflection Enterprise residual GTM → Glean / Sierra | Post-MSFT-licensing diaspora placed |
| Mar 2026 | Mem (K. Moody) → Letta (advisor) | Memory consolidation; Mem stalled |
| Apr 2026 | 3+ Magic.dev senior eng → Anthropic / Cursor | $1.6B / <$10M ARR mismatch breaking |

### Runtime / protocol layer

| Date | Event | Read |
|---|---|---|
| Jun 2025 | Logan Kilpatrick → Google AI Studio + ADK devrel lead | Google centralizing agent devrel |
| Sep 2025 | Anthropic NYC HQ enterprise doubled by Q1'26 (rumor) | NYC enterprise org real |
| Sep 2025 | Romain Huet — OpenAI Head DevEx, Agents SDK + Responses | OAI agent narrative owner |
| Oct 2025 | AWS AgentCore PMs hired pre-launch | Hyperscaler agent stack staffing |
| Dec 2025 | MCP TSC seats: Anthropic, MSFT, Google, OpenAI, HF, Cloudflare | Governance distributed |
| Apr 2026 | Mahesh Murag — OpenAI Agents → Cloudflare MCP/AI | Gateway category staffing up — **Bet #3 reframe validation** |
| Apr 2026 | Harrison Chase posture: "LangSmith is the margin layer" | Runtime-is-thin admission against interest |

**Read-through (May 2026).** The Stripe / Ramp / Datadog / Snowflake → Sierra / Decagon / Glean / Hippocratic migration is accelerating, with March 2026 the heaviest single month yet (8+ named LinkedIn moves into the top three alone). NYC concentration sits at historic peak Q2 2026. Over-funded under-performers (11x, Mem, Magic.dev, Adept residual) are shedding senior talent into segment winners, lifting supply while top equity rooms tighten.

**MBB → vertical agent feed-stock (V3-discovered pattern V1 missed).** BCG / McKinsey / Bain AI-practice partners are rotating into Sierra, Hebbia, and Harvey GTM. Hebbia sources MBB heavily (Sivulka public, Bloomberg Mar 2026). This is a third feed-stock alongside Stripe / Ramp / Datadog / Snowflake and BigLaw — less competed in Alex's lane because consultants don't bring SaaS-operator commercial scar tissue. A 30-day push to NYC MBB AI-practice alumni could open the Hebbia / Sivulka pipeline directly.

## §4.4 Capital events ($50M+ agent-platform rounds, M&A)

Bi-weekly. Threshold lower than V1 ($50M vs $100M) because agent-layer rounds index lower in absolute size. Includes M&A and infrastructure commits where agent-relevant.

### Agent platform rounds

| Date | Company | Round | Amount | Val | Signal |
|---|---|---|---|---|---|
| Jul 2025 | Cursor (Anysphere) | C | $900M | $9.9B | First IDE > $9B; Anthropic-dependent |
| Aug 2025 | Sierra | C | $300M | $4.5B | Vertical-agent thesis validated |
| Sep 2025 | Decagon | C | $250M | $4.5B | Two-winner CX crystallizes |
| Sep 2025 | Glean | E | $260M | $7.2B | Search-agents cap tightens |
| Sep 2025 | Replit | C | $250M | $3B | Agent ARR inflection |
| Oct 2025 | Bolt (StackBlitz) | B | $105M | $700M | Prosumer code wedge |
| Nov 2025 | Augment Code | B | $252M | $977M | Under-funded ratio |
| Jan 2026 | Lovable | A | $200M | $1.8B | Fastest EU SaaS curve; M&A bait |
| Jan 2026 | Clay | growth | $100M | $1.5B | NYC RevOps survivor |
| Jan 2026 | Rogo | B | $50M | $400M | NYC banker-copilot |
| Jan 2026 | Perplexity | E | $500M | $18B | Comet pivot funded |
| Feb 2026 | Harvey | E | $300M | $5B | Legal durability; NYC office |
| Feb 2026 | Hippocratic AI | C | $150M | $2B | NYC healthcare anchor |
| Feb 2026 | Factory | B (inf) | $100M | $750M | SF code-agent infra |
| Mar 2026 | Sierra add'l (rumor) | — | $350M | **$10B** (The Information) | Highest agent-platform mark |
| Mar 2026 | Mistral | C | €600M | €11B | First credible non-US enterprise-agent platform |
| Mar 2026 | Cognition acquires Codeium | M&A | ~$3B | — | After OpenAI–Windsurf collapsed Jul 2025 |
| Apr 2026 | ElevenLabs (rumor) | D | unknown | $5B+ | Voice infra dual-motion |
| Apr 2026 | Galileo (rumor) | C | ~$60M | — | Pure-play eval still LP-backable |
| Q2 2026 | Ramp (rumor) | growth | unknown | $20B+ | NYC AI-org expansion funded |
| Q2 2026 | Hebbia (rumor) | C | unknown | $1.5–2B | NYC knowledge-agent overdue |

### Picks-and-shovels + M&A — agent-relevant

| Date | Event | Signal |
|---|---|---|
| Apr 2025 | PANW → Protect AI ~$700M (closed Q3'25) | Safety into security stack |
| Sep 2025 | OpenAI → Promptfoo | Eval/red-team internalized at frontier |
| Q4 2025 | Lakera Series B ~$50M | Last independent runtime-safety at scale |
| Q4 2025 | AWS AgentCore launch (re:Invent) | Hyperscaler agent runtime arrives |
| Dec 2025 | MCP → Linux Foundation | Spec authority distributed |
| Q1 2026 | Braintrust B ~$60M (rumor) | Eval-as-CI consolidator candidate |
| Q1 2026 | Cloudflare MCP auth expansion | Gateway category compounding — **Bet #3 reframe** |
| Apr 2026 | Kong MCP Gateway GA pricing | "MCP gateway = API gateway 2.0" |
| Apr 2026 | Vercel Sandbox + AI Gateway prod pricing | Vercel-staked agent infra |
| Apr 2026 | NeMo Guardrails 1.0 GA (Apache 2.0) | OSS guardrails production-credible |

Read the capital table by stage, buyer, and infra commit, same as V1 §4.4. The agent-specific addition: a fourth pass by **gateway-vs-productized** — Cloudflare, Kong, Vercel, and Pomerium activity validates the Bet #3 reframe (Ch 3 §3.1). Productized MCP server M&A has stayed quiet; gateway category investment has not.

## §4.5 Agent-layer ARR Watchlist

Quarterly snapshot of named agent-vendor ARR trajectories. Disputed figures show range. Trailing-12 ARR and annualized run-rate are kept separate when sources allow.

| Company | T12 → RR May'26 | Disputed? | Note |
|---|---|---|---|
| Anthropic (parent) | $1B Dec'24 → **$24–30B** Apr'26 | **YES** | Claude Code = inflection; **Bet #2 valuation crux (C1)** |
| Sierra | $0 → $175M+ Q1'26 | low | Taylor public 4× YoY |
| Decagon | $1M 2024 → $80M+ Q1'26 | low | Sierra peer |
| Glean | $50M → $300M+ Q1'26 | low | Search-agent leader |
| Harvey | $25M → $100M+ Q1'26 | low | Legal NYC tripling Q3'26 |
| Hippocratic | $5M → $50M+ Q1'26 | low | "1,000 agents deployed" |
| Abridge | $50M → $120M+ Q1'26 | low | Fastest healthcare-AI |
| Cursor | <$1M → $500M+ RR | low | Anthropic-dependent |
| Lovable | $0 → $80M Q1'26 | confirmed | Fastest EU SaaS ever (Osika public) |
| Hebbia | $30M → $50M+ Q1'26 | **inf — disputed** | NYC HQ; raise overdue |
| Rogo | <$5M → $30M+ Q1'26 | **inf — rumor** | NYC; should clear $1B Q3'26 |
| Clay | $20M → $80M+ Q1'26 | low | Only durable RevOps winner |
| Augment | $5M → $40M Q1'26 | low | Under-funded ratio |
| Mistral Le Chat Ent. | €30M → €100M+ Q1'26 | inf | EU sovereign |
| Replit Agent | $50M → $150M+ Q1'26 | inf | Prosumer/SMB |
| ElevenLabs | $25M → $200M+ Q1'26 | low | Voice infra |
| Perplexity | $20M Q1'24 → $200M+ Q1'26 | low | Comet rationale |
| 11x | $20M → **$20M flat** Q1'26 | **YES — retention** | Sukkar quality-ceiling admission; cautionary tale |
| Braintrust | $25M (inf) → $60M+ Q1'26 | inf | Eval-as-CI |
| LangSmith | $15M (inf) → $40–60M Q1'26 | **inf — disputed** | LangChain Inc. margin layer |

**Load-bearing flag — Anthropic ARR.** The Anthropic figure re-prices Bet #2 directly. The $24B lower bound compresses vertical-agent valuations 20–30% (Sierra $10B → $6–8B); the $30B upper bound strengthens equity and accelerates Alex's offer timing. Both ends remain defensible May 2026. Resolution Q3 2026 — see Crux C1 (§4.8). Treat the dispute itself as the signal until then; do not pick a number.

## §4.6 Public statements from agent founders (decoded)

Quarterly. The "decoded" column is the signal. The verbatim quote without operator translation is noise.

| Speaker | Statement | Decoded |
|---|---|---|
| Bret Taylor (Sierra) | "Outcome pricing is how AI eats SaaS"; "$175M+ ARR, 4× YoY" (AIE Feb'26, SaaStr May'26) | Per-resolution exports beyond CX; owning the *narrative* is the moat; pre-IPO posture |
| Munjal Shah (Hippocratic) | "$9/hr RN equivalent; 1,000 agents deployed" (HLTH'25) | Per-call as labor-sub; outcome-adjacent without malpractice exposure |
| Aman Sanger (Cursor) | "The IDE is the agent" | Form-factor wins prosumer; enterprise contested = Anthropic-channel anxiety |
| Sam Altman | "Agents are the most important 2026 category"; "Compute-constrained not idea-constrained" | OAI re-anchors post-GPT-5 disappointment; Stargate deploy ratio = bear case |
| Dario Amodei | "Most code at frontier labs is AI-written; 90% in 12mo" (Mar'26); Mar'26 op-ed on agentic compute | Recruiting tool + ARR proof point; primes disputed $24–30B and next-round infra story |
| Maor Shlomo (Decagon) | "Per-resolution is now standard" (AIE Feb'26) | Validates Taylor; CX pricing wars over |
| Aravind Srinivas (Perplexity) | "Browsers are the new OS" → Comet pivot | Search ARR can't sustain $18B; new pitch — believe at your peril |
| Harrison Chase (LangChain) | "LangSmith is the margin layer" (Sept'25+) | Runtime thin; observability is where dollars sit |
| Sundar / Demis | Mariner GA in Gemini Enterprise (Apr'26) | Google walks into browser-use; OSWorld ~35% = execution lag |

## §4.7 NYC agent-company snapshot

Quarterly. NYC is over-weighted because Bet #2 is NYC-anchored, and Q2 2026 is the historic peak window.

**Companies hiring Alex's profile (12+ yrs B2B + AI fluency, NYC).** Sierra (NYC + SF dual-HQ; Taylor in NYC monthly per AIE Feb'26); Hippocratic AI (NYC HQ; healthcare voice); Hugging Face (Brooklyn); Runway (Chelsea); Hex (NYC); Cohere (NYC office expanding); Anthropic NYC (enterprise org doubled Q1 2026, rumor CB Insights); OpenAI NYC (sales hub); Decagon NYC (expanded Q1 2026); Ramp (NYC fintech, AI-product-aggressive; $20B+ raise rumored Q2 2026); Hebbia (NYC HQ; Mehta hire Mar 2026); Harvey (NYC tripling by Q3 2026); Rogo (NYC HQ; banker-copilot); Clay (NYC HQ; Amin's 40-headcount push H1 2026); Regal.io (NYC; smaller bands). Comp bands $250–400k base + 0.05–0.40% equity (inf).

**Events of consequence (next 90 days).** RAAIS NYC June (Nathan Benaich; founder-density per hour highest); NYC AI Hub demos rolling (Mayor + Cornell Tech); Anthropic NYC enterprise meetup rumored June; Betaworks AI Camp quarterly (operator-density per hour highest); Cornell Tech AI demo days; Lux / FirstMark portfolio events.

**People to meet.** Bret Taylor (Sierra); Munjal Shah (Hippocratic); Aman Sanger (Cursor — SF/NYC frequent); Eric Glyman (Ramp); Divya Mehta (Hebbia, post-Stripe); Nathan Benaich (Air Street / RAAIS); Matt Turck (FirstMark, MAD Landscape).

**Verdict.** NYC vertical-agent hiring is at historic peak Q2 2026 — 10+ companies hiring Alex's exact profile simultaneously. Window approximately 6–9 months before Anthropic ARR resolution (C1) and the first vertical-agent IPO posture reprice equity bands. Confirm titles, not just locations, when triaging dual-HQ postings — Sierra and Decagon anchor product and engineering in SF.

## §4.8 Cruxes status (with OSWorld sub-crux)

Trigger-based. The five parent cruxes plus the OSWorld sub-crux. When a crux moves, log the date and answer-event, then re-rate any affected bet in §4.2 in the same session.

| # | Crux | Horizon | Answer-event | Re-rank consequence | Status |
|---|---|---|---|---|---|
| C1 | Anthropic ARR — $24B or $30B? | Q3 2026 | Audited disclosure / The Information leak / Stripe data | Lower bound = vertical-agent vals compress 20–30%; upper = Bet #2 timing accelerates | Open (2026-05-20) |
| C2 | Inference compute — 10× growth or flat? (V1 framing) | 2026 Q4 hyperscaler earnings | NVIDIA quarterly; Crusoe / CoreWeave; MSFT/GOOG capex | Flat = NVDA reprices, Bet #4 GPU-brokerage adjacency opens; 10× = neocloud GTM goes hot | Open (2026-05-20) |
| C3 | MCP — commons or silent fork? | EOY 2026 | Major-vendor proprietary tool-use schema announcements; A2A adoption outside Google | Fork = Bet #3 productized form dies; commons = advisory practice accelerates | Open (2026-05-20) |
| C4 | EU AI Act Article 14 — teeth or paper tiger? | Late 2026 | First GPAI fine; Commission Art. 14 enforcement actions | Teeth = Bet #1 becomes $10B+ category; paper = stays niche but defensible | Open (2026-05-20) |
| C5 | Standalone memory — absorbed or niche? | H2 2026 | Mem0 / Letta acquisition vs independent Series B at higher val | Directional: consumer/prosumer absorbed; compliance-enterprise niche-standalone (already folded into Bet #5) | Open (2026-05-20) |
| **C3a** | **OSWorld 65% on a frontier system (sub-crux)** | Q3 2026 | Public scoreboard event | Crossed = computer use moves from supervised to deployable for narrow back-office a quarter earlier than this volume assumes; feeds C2 and C5 | Open (2026-05-20) |

Status values: "Open", "Resolved YYYY-MM-DD", or "Partially answered" (use sparingly — partial answers usually mean the crux was framed too coarsely; rewrite it). As of 2026-05-20 all six are Open, which is the expected state for the first six months. The OSWorld sub-crux is V3-specific — it sits inside the C2 + C5 envelope but resolves on its own benchmark event (frontier system crossing 65%) and gets watched on the trigger-based path independently. Mariner GA in Gemini Enterprise (Apr 2026) hit roughly 35% OSWorld; the 65% threshold is the deployment marker that re-rates Bets #2 and #5.

## §4.9 Structural risks status

Quarterly re-check. If a risk fires, move it to a "fired" archive below the live table (none yet).

| # | Risk | What it threatens | Watch | Last re-checked |
|---|---|---|---|---|
| R1 | Foundation labs walking up-stack into verticals | Bet #2 — ChatGPT Business connectors, Claude for Work, Gemini Workspace agents compress vertical-agent vendor moats | Connectors / Skills / Apps store launches; named-customer deflection from Glean / Cursor | 2026-05-20 |
| R2 | MCP silent fork via Responses-API proprietary path | Bet #3 productized form — production OpenAI agents bypassing MCP for latency | OpenAI Responses-API extensions outpacing MCP-spec evolution; A2A adoption outside Google | 2026-05-20 |
| R3 | Anthropic ARR resolution downside | Bet #2 valuation + timing — $24B lower bound compresses Sierra $10B → $6–8B | Q3 2026 disclosure or leak | 2026-05-20 |
| R4 | Hyperscaler bundling of runtime safety / eval / sandbox / routing | Bet #4 window + standalone eval/obs category — Bedrock auto-optim, Vertex routing, Azure routing default-on plausible H2 2027 | AWS Bedrock auto-optimization launches; Vertex / Azure routing default-on announcements | 2026-05-20 |
| R5 | EU AI Act paper-tiger outcome | Bet #1 advisory TAM — small / procedural enforcement late 2026 | Commission guidance; first GPAI fine size | 2026-05-20 |

Risks differ from cruxes (§4.8) in that a fired risk reprices bets immediately; a resolved crux merely tells you which bets to re-rate. Treat watch-column triggers as alerts, not background reading.

## §4.10 Update log

| Date | Change |
|---|---|
| 2026-05-12 | Initial V3 creation. Seven Bets refreshed at agent-layer resolution. Bet #1 sequenced first (delta from V1). Bet #3 reframed to advisory + gateway-adjacent. NYC target list expanded for Bet #2 (+ Hebbia, Rogo, Clay, Runway, Ramp AI). MBB consulting feed-stock surfaced as Bet #2 secondary path. Five Cruxes and five Risks refreshed for agent layer; OSWorld added as sub-crux C3a. |
| 2026-05-20 | Consolidated into AI_AGENTS_MASTER Ch 4. Restructured with how-to-use preface, defer-cadences to V1 Ch 5, registered §4.5 ARR table to spec, added §4.6 public-statements decoded table, lifted §4.7 NYC snapshot from B8.5. V1 Ch 4 §4.2, §4.3 noted to absorb the Bet #1 sequencing change and Hebbia/Rogo/Clay/Runway/Ramp NYC additions on next monthly ritual. |
| _next update_ | _Bi-weekly: refresh §4.3 + §4.4. Monthly: re-rate §4.2 (with parallel V1 Ch 4 §4.2 update). Trigger-based: §4.8, §4.9._ |

## Apply

Add one new agent-layer talent move OR capital event from the last 14 days. The agent-layer cadence is higher than the full-stack cadence — if a week passes without anything to log here, you've drifted off the field. Scan: LinkedIn alerts for Sierra / Decagon / Glean / Hebbia / Rogo / Hippocratic / Clay; Pallet newsletters; The Information funding section; Apollo activity on NYC vertical-agent companies; MCP TSC announcements; Cloudflare / Kong / Vercel MCP-related releases. Log the row with date and a one-line "why this is signal, not noise" — name the bet it informs (Ch 3 §3.1) and the leading indicator it satisfies or contradicts. If the move informs no V3 bet, do not log it here; route it to V1 Ch 4 instead. This drill takes eight minutes end to end and is the keystone habit for keeping the agent-layer tracker alive.
