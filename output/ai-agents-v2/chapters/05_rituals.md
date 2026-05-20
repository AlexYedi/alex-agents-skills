# Chapter 5 — Operating Rituals (Volume III Add-Ons)

Volume I Chapter 5 owns the master ritual cadence. Five cadences carry the practice — weekly reflection (~10 min), bi-weekly tracker sync (~5 min), monthly conviction ritual (~15 min), quarterly deep review (~60 min), twice-yearly major refresh (~half-day). Volume III inherits all five without modification. If you are reading this chapter without V1 Ch 5 open in another tab, close this file and open that one first — the master cadence is load-bearing and is not restated here.

This chapter is a small overlay. It adds three things V1 Ch 5 does not cover, because they are agent-layer-specific and would dilute the master rituals if they lived there:

1. **A V3 quarterly delta-audit** — five minutes appended to the V1 quarterly deep review (V1 Ch 5 §5.3). Checks whether the V3 bet deltas, the 10-sub-stratum framing, or the 7-job JTBD set has solidified enough to fold back into V1.
2. **Three V3 trigger-based events** — same-day log entries that fire on OSWorld benchmark crossings, ASL-4 announcements, and major MCP governance events. Not new cadences; triggers added to the existing trigger-based path V1 already names.
3. **A V3 twice-yearly composability check with Volume IV** — five minutes appended to the V1 twice-yearly refresh (V1 Ch 5 §5.4). Confirms V3 still composes with the GTM volume once it lands.

None of these are new cadences. They are short additions to the cadences V1 already runs. Total V3 overhead, when alerts are wired correctly, is roughly twenty minutes per year on top of the V1 baseline. The trigger-based events are the most-used path — they are also the easiest to miss if the watch lists are not set up. Spend the five minutes at the end of this chapter wiring the alerts.

## §5.1 V3 quarterly delta-audit (~5 min added to V1 Ch 5 §5.3)

### When
First Sunday of January, April, July, October — during the V1 quarterly deep review. Append to the end of the V1 §5.3 checklist; do not run separately.

### What you do
Three short checks, each one minute, specific to V3:

1. **Re-check the V3 bet deltas.** Has any V3 framing solidified enough that it should be folded back into V1 as the parent framing? Three candidates to watch: Bet #3's reframe to advisory + gateway-adjacent (Ch 3 §3.1); Bet #4's split into per-token + per-trajectory FinOps; Bet #5's fold-in of memory architecture per Crux 5. If any has held through two consecutive quarters with reinforcing evidence, flag it for the next V1 twice-yearly major refresh.

2. **Confirm sub-stratum stability.** Does the 10-sub-stratum framing (Ch 1) still hold, or have any agent-layer events suggested a renumbering? The most-likely trigger is Crux 5 resolving "standalone" for memory — which would promote Stratum IV from "loop of cognition" to its own top-level position. If it has, flag for refresh.

3. **JTBD job map check.** V3 has 7 jobs; V1 has 6 (spec §3.4). Has any agent-layer event suggested the job set should change? The most-likely emergence is a Job 8 around multi-agent orchestration once sub-agent privilege separation becomes a procurement default rather than an overlay. If it has, flag.

### Where it lands
Ch 4 §4.10 update log gets a row dated today with the result. One line per check; three lines total. If nothing moved, write "no V3 deltas this quarter" — the noticing is the artifact.

### What you don't do
Do not rewrite chapters here. Do not re-rate bet conviction (that is the monthly ritual at V1 Ch 5 §5.2). The delta-audit flags candidates for the twice-yearly refresh; it does not perform the refresh.

## §5.2 V3 trigger-based events (~5 min each, when fired)

Three V3-specific triggers worth a same-day log entry. None requires a chapter rewrite at the moment of the trigger — the rewrite, if needed, happens at the next scheduled monthly or quarterly per V1 Ch 5.

### Trigger A — OSWorld benchmark crossing
**Fires when** any frontier system publicly reports an OSWorld score at or above 65% (the production-deployable threshold named in spec §3.7 and Ch 3 §3.3 as the sub-crux feeding Cruxes 2 and 5).

**What you do:**
- Log in Ch 4 §4.8 under the OSWorld sub-crux with date, source, and reported score.
- Update Crux 2 (inference compute growth) status — a 65%+ score is partial confirmation that test-time compute is still doing work at the agent layer.
- Re-rate Bet #2 conviction. The default delta: +★ if the crossing happens before Q3 2026 (ahead of schedule, vertical-agent valuations pull forward); hold if on schedule; -★ only if the crossing comes paired with evidence of a vertical-agent moat collapse, which is a different event.

### Trigger B — ASL-4 announcement or RSP threshold crossing
**Fires when** Anthropic or any frontier lab declares an ASL-4 capability or invokes a deployment freeze under its Responsible Scaling Policy.

**What you do:**
- Log in Ch 4 §4.9 under Risk #3 (OpenAI Preparedness adjustment-clause activation, generalized to "any frontier lab safety-driven freeze").
- Re-rate Bet #2. Vertical-agent companies face downstream constraints if their model providers freeze; the conviction delta is contingent on which lab and which capability — Anthropic freezing Opus 4.5 is more material to the NYC vertical-agent list than Meta freezing Llama 4.
- Re-check Meta-A in Ch 1 for a binding-constraint update. ASL-4 is the event that makes Meta-A the dominant constraint on the agent stack; before it fires, Meta-A is dormant.

### Trigger C — Major MCP governance event
**Fires when** the Linux Foundation Agentic AI Foundation publishes a major spec change, OR any major vendor (OpenAI, Google, Microsoft, AWS) ships a tool-use schema that diverges from the MCP spec.

**What you do:**
- Log in Ch 4 §4.8 under Crux 3 (MCP commons vs fork).
- If the event reads "fork" — Bet #3 in its productized form dies. Mark it in Ch 4 §4.2 immediately with conviction down to ★★ pending the next monthly. The advisory + gateway-adjacent reframe is partially insulated, but only partially.
- If the event reads "commons accelerates" — Bet #3 conviction +★. The reframe is reinforced; the gateway control-plane position becomes more valuable, not less.

## §5.3 V3 twice-yearly composability check with Volume IV (~5 min)

### When
First Sunday of January and July, during V1 Ch 5 §5.4 twice-yearly refresh. Append; do not run separately.

### What you do
Read the latest Volume IV (the GTM volume — `output/agents-gtm/chapters/03_*.md` for the GTM bets, if that volume exists yet at the time of the refresh) and confirm V3 still composes cleanly with V4. Three checks:

- **Are V3 Bets #1 and #2 still the platform for V4's GTM motion?** Bet #1 (procurement standard) and Bet #2 (vertical-agent GTM role) are the load-bearing platform for whatever GTM bets V4 names. If V4 has drifted such that V3's first two bets no longer carry it, one of the two volumes has moved without the other.
- **Has V4 surfaced any GTM-level insight that re-rates a V3 bet?** Example: a GTM channel finding that makes Bet #6 (newsletter) look weaker as a distribution vehicle than V3 currently rates it. If yes, flag for refresh.
- **Update V3 with any V4 deltas; or open an issue for the next major refresh.** Same posture as the V1 quarterly delta-audit — flag, don't refactor.

### What you don't do
Do not refactor V3 to match V4 mid-cycle. The composability check is a noticing ritual, not a refactor trigger. If V4 has shifted enough to demand a V3 rewrite, that rewrite happens in the next twice-yearly major refresh, not now.

## Apply

Confirm the three V3 triggers are wired into your watch lists. If you do not have a saved search or alert for OSWorld scoreboard events, ASL-4 announcements, and MCP spec changes — set them now. Five minutes today: an OSWorld GitHub watch, a Google Alert for "ASL-4" and "Responsible Scaling Policy", and a Linux Foundation Agentic AI Foundation mailing-list subscription. The V3 rituals cost five minutes a month when the alerts work. They cost zero minutes a month when you forget to set them — but then the bets drift, and the next time you notice is the next quarterly, which is too late.
