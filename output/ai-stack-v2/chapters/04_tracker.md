# Chapter 4 — Operating Tracker

This chapter is the touch-surface. Chapters 1 through 3 describe the field and the bets placed on it; this chapter is where evidence accumulates against those bets. Three operating sections update on three different cadences (see §4.1): talent and capital flow refresh bi-weekly, bet conviction re-rates monthly, cruxes and risks log when triggered. The point is not completeness — it is disciplined attention to leading indicators in a format that survives 18 months of churn.

If you only have 15 minutes for a session, update §4.2 (bets status) and §4.3 (talent moves). If you only have 5 minutes, log one signal anywhere — a single new row in any table beats a polished refresh that never happens. If you have 60 minutes, do the monthly conviction ritual (Ch 5 §5.2) end-to-end and write the update-log entry. The tables in this chapter are intentionally lean. Add columns sparingly; the schema is designed to be re-readable a year from now without parsing legend text.

## §4.1 How to use & update cadences

Three cadences govern this chapter. They are deliberately desynchronized so no single session has to update everything.

| Cadence | What updates | Where (in this chapter) | Owner |
|---|---|---|---|
| Bi-weekly | Talent moves, capital events | §4.3, §4.4 | Alex |
| Monthly | Bet status, conviction, leading indicators | §4.2 | Alex |
| Trigger-based | Cruxes resolved, risks fired | §4.8, §4.9 | Alex |
| Quarterly | Risk re-check, score-discipline audit | §4.9 | Alex |

The bi-weekly cadence is the metronome. Talent and capital are the easiest to surface (Pallet newsletters, LinkedIn alerts, The Information funding section, Apollo activity) and the most immediately predictive of which bets re-rate. The monthly conviction pass on §4.2 is where the talent and capital evidence is interpreted; do it on the same day of the month each time so the comparison interval is constant.

Update discipline: if you skip a cadence twice in a row, do not try to backfill bi-weekly logs from memory. Schedule a quarterly deep review (Ch 5 §5.3) to catch up, and treat the gap as an honest signal that the operating tempo slipped. Every row written from memory more than two weeks late is contaminated by hindsight; the point of this tracker is to preserve the prior, not to launder a narrative.

When a crux moves (§4.8), log the date and the answer-event in the row, then re-rate any affected bet in §4.2 in the same session. Crux resolution is the most expensive event in the operating model — every other bet gets re-ranked off it.

## §4.2 Bets status board

Compact view of the seven bets. Full hypothesis, falsifiability, and leading indicators live in Ch 3. This board is the monthly conviction-rating surface.

| # | Bet (compact) | Conviction | Status | Last change | Note |
|---|---|---|---|---|---|
| 1 | Enterprise AI Procurement Standard | ★★★★★ | Unstarted | 2026-05-08 | No change; ready to begin Q2 |
| 2 | Vertical Agent GTM Role (NYC) | ★★★★★ | Active | 2026-05-08 | Search ramp; NYC list expanding |
| 3 | MCP-Native Enterprise Integration | ★★★★ | Unstarted | 2026-05-08 | Sequenced after Bet #1 |
| 4 | FinOps for Tokens | ★★★★ | Unstarted | 2026-05-08 | Decay window: 12–18 mo |
| 5 | Enterprise RAG Architecture | ★★★★ | Unstarted | 2026-05-08 | Bundles with Bet #1 + #4 |
| 6 | Operator's Translation Newsletter | ★★★ | Unstarted | 2026-05-08 | Lowest cost-to-start |
| 7 | VC Operating Partner / Platform | ★★★ | Background | 2026-05-08 | Promotes to ★★★★ if #1/#2/#3 stall |

Conviction scale: ★★★★★ "convergent across all 5 frameworks, near-term cash or career-defining"; ★★★★ "strong but with one explicit failure mode"; ★★★ "real but secondary or execution-dependent"; ★★ "watch only"; ★ "killed". Re-rate monthly with explicit reasoning in the update log (§4.10), not by feel. Grade-inflation drift is the most common failure mode on a board like this; resist the urge to bump everything up after a good week of inbound.

## §4.3 Senior frontier talent moves (rolling 12 months)

Bi-weekly. Add rows above the read-through paragraph; do not delete rows older than 12 months without first archiving them in Ch 6 §6.5.

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
| Nov 2025 | Jan Leike | Anthropic (retention) | — | Anthropic alignment moat held |
| Dec 2025 | Mohan / Chen (Windsurf) | Windsurf → Google DeepMind (acqui-hire) | $2.4B licensing | New 3-party M&A template |
| Mar 2026 | Multiple Stripe/Ramp/Datadog/Snowflake AEs | → Sierra / Decagon / Glean / Hippocratic | mid-six base + meaningful equity | The dominant pattern for Alex's profile |
| May 2026 | Stripe/Ramp enterprise reps continued | → Decagon, Sierra, Glean (NYC + SF) | mid-six + equity | NYC vertical-agent hiring at peak |

**Read-through (May 2026).** Meta is the top talent destination, paying capability-cluster prices for whole teams rather than individuals. OpenAI is the top source of departures; Anthropic retained its alignment core. The most actionable signal for Alex's profile is the Stripe/Ramp/Datadog/Snowflake → Sierra/Decagon/Glean/Hippocratic migration, now visible in NYC at peak intensity. That migration is Bet #2's leading indicator (Ch 3 §3.2).

## §4.4 Capital events ($100M+ rounds, M&A, infra commits)

Bi-weekly. Threshold: $100M+ rounds, any M&A involving AI capability, infra commitments above $1B.

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

The capital table is read in three passes. First, by stage — concentration at Series C–E indicates which vertical-agent categories are committing to enterprise GTM scaling. Second, by buyer — incumbent M&A (MongoDB-Voyage, NVIDIA-Run:ai, NVIDIA-SchedMD) maps which adjacent layers are absorbing the AI stack. Third, by infra commit — Stargate, CoreWeave-Meta, Humain track the deploy-to-commit ratio that resolves Crux #2 (Ch 3 §3.3, Crux 2).

## §4.5 ARR Watchlist

Quarterly snapshot of named-vendor ARR trajectories. Disputed figures get flagged inline.

| Company | Trajectory | Implication |
|---|---|---|
| Anthropic | $1B Dec'24 → $30B disputed Apr'26 | Claude Code = inflection driver; enterprise non-OpenAI demand real |
| OpenAI | $5.5B Q1'24 → $24–30B Apr'26 disputed | Consumer-heavy; enterprise via Microsoft channel |
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

Note on disputed figures. The Anthropic and OpenAI rows carry "$24B vs $30B" disputes because both companies' Q1 2026 disclosures conflict with The Information's leaks and Stripe processing data. The dispute is itself the signal — it is Crux #1 (Ch 3 §3.3, Crux 1) and resolves on Q2–Q3 2026 audited reporting. Do not pick a number; log both bounds and update when the audit lands.

## §4.6 Public statements decoded

Quarterly. The "decoded" column is the signal. The verbatim quote without operator-translation is noise.

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

## §4.7 NYC snapshot

Quarterly. The NYC view is over-weighted in this tracker because Bet #2 (Ch 3 §3.2) is NYC-anchored.

**NYC AI companies hiring aggressively (Q2 2026).** Sierra (NYC + SF dual-HQ; Bret Taylor in NYC monthly), Hippocratic AI (NYC HQ; healthcare voice), Hugging Face (Brooklyn), Runway (Chelsea), Hex (NYC), Cohere (NYC office expanding), Anthropic NYC (small but growing — finance vertical), OpenAI NYC (sales hub), Decagon NYC presence (small), Ramp (NYC fintech, AI-product-aggressive), Scale AI Defense (residual after Wang exit).

**Events of consequence.** RAAIS NYC (Nathan Benaich), NYC AI Hub (Mayor + Cornell Tech), AI Founders NYC, AI Tinkerers NYC, Cornell Tech AI demo days, Betaworks AI Camps, Lux/USV/FirstMark portfolio events. Attendance ROI is highest at RAAIS (founder-density per hour) and Betaworks (NYC operator-density per hour).

**People to meet.** Bret Taylor (Sierra), Munjal Shah (Hippocratic), Aman Sanger (Cursor — SF/NYC frequent), Eric Glyman (Ramp), Daniel Gross (Meta MSL — but NYC-network active), Nathan Benaich (Air Street / RAAIS), Nabeel Hyatt (Spark), Lee Edwards (Root), Matt Turck (FirstMark, MAD Landscape).

**Verdict.** NYC is growing in vertical-agent GTM and shedding in foundation R&D. The hiring gradient favors Alex's profile (12y enterprise B2B + AI-builder fluency + NYC residency). The risk is that the dual-HQ vertical-agent companies (Sierra, Decagon) anchor product and engineering in SF and route NYC headcount toward field roles only — confirm titles, not just locations, when triaging postings.

## §4.8 Cruxes status

Trigger-based. When a crux resolves, log the date, the answer-event, and re-rate any affected bet in §4.2 in the same session.

| # | Crux | Horizon | Answer-event | Re-rank consequence | Status |
|---|---|---|---|---|---|
| 1 | Anthropic ARR — $24B or $30B? | Q2–Q3 2026 | Audited disclosure; The Information leak; Stripe data | Lower bound = vertical-agent valuations compress 20–30%; upper = Bet #2 timing accelerates | Open (2026-05-20) |
| 2 | Inference compute — 10× growth or flat? | 2026 Q4 hyperscaler earnings | NVIDIA quarterly; Crusoe / CoreWeave; MSFT/GOOG capex | Flat = NVDA reprices, GPU brokerage adjacent to Bet #4 opens; 10× = neocloud GTM (Stratum II) goes hot | Open (2026-05-20) |
| 3 | MCP — commons or fork? | H2 2026 | Major-vendor proprietary tool-use schema; LF governance | Fork = Bet #3 dies; commons = Bet #3 accelerates; decide by Q3 2026 | Open (2026-05-20) |
| 4 | EU AI Act — teeth or paper tiger? | Late 2026 enforcement | Commission guidance + first GPAI fines | Teeth = Bet #1 advisory becomes $10B+ category; paper = Bet #1 stays niche but defensible | Open (2026-05-20) |
| 5 | Long-term memory — standalone or absorbed? | 12–18 months | Anthropic / OpenAI / Google native memory feature launches | Absorbed = Mem0/Letta/Zep compress; Bet #5 RAG practice gains share. Standalone = $1B+ category; consider folding into Bet #5 | Open (2026-05-20) |

Status values are "Open", "Resolved YYYY-MM-DD", or "Partially answered" (use sparingly — partial answers usually mean the crux was framed too coarsely; rewrite it). As of 2026-05-20 all five are Open. That is the expected state for the first six months of this tracker; cruxes resolve on annual horizons, not weekly.

## §4.9 Structural risks status

Quarterly re-check. If a risk fires, move it to a "fired" archive section below the live table (none yet).

| # | Risk | What it threatens | Watch | Last re-checked |
|---|---|---|---|---|
| 1 | HBM4 / CoWoS-L slip | Every 2026 capacity plan; GPU pricing | SK Hynix / Micron HBM4 ramp; TSMC capex commentary | 2026-05-20 |
| 2 | Hyperscaler FCF reckoning | AI infra trade reprices; sales cycles harden 2–4 quarters | Amazon/Alphabet/Meta/Microsoft FCF Q3–Q4 2026 | 2026-05-20 |
| 3 | OpenAI Preparedness adjustment-clause activation | Voluntary safety regimes destabilize | Public adjustment notice; Anthropic counter-statement | 2026-05-20 |
| 4 | Federal preemption volatility on AI rules | Compliance practice repricing | Trump Dec 2025 EO court rulings; CA SB 53 lawsuits | 2026-05-20 |
| 5 | Foundation labs walking up-stack into vertical apps | Vertical agent companies (Bet #2 targets) compressed | ChatGPT Business connectors; Claude for Work; Gemini Workspace agent expansion | 2026-05-20 |

Risks differ from cruxes in that a fired risk reprices bets immediately; a resolved crux merely tells you which bets to re-rate. Treat the watch-column triggers as alerts, not as background reading.

## §4.10 Update log

| Date | Change |
|---|---|
| 2026-05-08 | Initial creation. Big Bets ranked; talent + capital tables seeded; cruxes and risks logged. |
| 2026-05-20 | Migrated tracker into AI_STACK_MASTER Ch 4; restructured with how-to-use preface; cross-refs updated to new chapter numbering. |
| _next update_ | _Bi-weekly: refresh §4.3 + §4.4. Monthly: re-rate §4.2. Trigger-based: §4.8, §4.9._ |

## Apply

Add one new talent move or capital event from the last 14 days. If you don't have one, you haven't been paying attention — go scan Pallet, your LinkedIn alerts, The Information's funding section, and your Apollo activity for five minutes, then come back. Log it with date, source, and one-line "why this is signal, not noise" — meaning, name the bet it informs (Ch 3 §3.1–§3.7) and which leading indicator it satisfies or contradicts. If the move informs no bet, do not log it; recreational news consumption is not what this chapter is for. This drill takes eight minutes end to end and is the keystone habit for keeping this chapter alive.
