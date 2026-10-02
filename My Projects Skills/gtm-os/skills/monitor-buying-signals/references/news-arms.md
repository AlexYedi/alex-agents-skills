# News arms — cost ladder, call mechanics, and the graduation path

Mechanics verified live 2026-08-11; re-verify per workspace (catalogs and costs
drift, and provider rosters differ between workspaces — the canonical structured-news
provider may simply not exist in yours; check before promising an arm).

## The cost ladder (verify per workspace before quoting)

| Arm | Surface | Declared cost | When |
|---|---|---|---|
| `find-google-news-results` | catalog action (workflow tool node, or ad-hoc where available) | ~1 credit | the default sweep arm |
| Managed **Company News** function | routine (`clay routines runs start`) | ~6.7 credits/run | premium: aggregated multi-source, for a NAMED priority shortlist only |
| `intellizence-get-news` | catalog action | ~6 credits | alternative structured arm if present |
| `lusha-*-signal` family | catalog action | ~8 credits | own-key territory; not a default |
| Native `trigger-source` News feed | in-app table subscription | subscription free; ~0.5-1 credit per landed EVENT | standing watches — see Graduation |

Read the actual charge from usage metadata per call where the surface exposes it
(workflow `runs steps` carries `creditUsageMetadata`); the routines surface exposes
no per-run cost — report its declared estimate AS an estimate.

## Call mechanics

**Managed Company News** (routine): inputs `Company Domain` (required),
`Earliest Publish Date YYYY MM DD`, `Latest Publish Date YYYY MM DD`,
`Max News Events`. The date-window inputs are the whole point — ALWAYS pin them to
the sweep window. Contract traps verified live (the field NAMES lie): the date
fields REQUIRE full ISO 8601 date-times (`2026-08-11T00:00:00Z`) despite being named
"YYYY MM DD", and `Max News Events` must be a STRING — and was IGNORED in live
testing (asked 5, got 100 events): never rely on it to bound cost or output. CLI
envelope: `{"items":[{"id":"<key>","inputs":{...}}]}` piped via `--input -`.
Payload shape: structured events under `Find Most Recent News` with pre-classified
`category`, `effective_date`, `article_sentence`, `confidence`, and a source URL per
event (100% in live testing) — but expect a large undated fraction (~1/3 live):
dated events respect the window; UNDATED events ride along and must be routed out by
the no-date rule. Gate on the payload's events, not run status: quiet domains return
a complete run with an empty/valueless result (completion is not data), and a
complete run can wrap a failed item — check both levels.

**Catalog arm quiet + date shapes** (verified live): a quiet result omits the
`news_results`/`result` field ENTIRELY (not an empty list) — gate on absence-of-
events, and note a quiet call still bills its ~1 credit (misses cost money). Event
dates arrive as RELATIVE strings ("2 days ago") — parse to absolute at sweep time.

**Catalog action in a workflow**: minimal manual-trigger workflow — create →
`surfaces_edit_trigger` (triggerType manual; this call creates AND binds the canvas
trigger — an empty workflow has none, and `edit_node` cannot add one) → tool node with
static inputs, `incomingEdges` from the returned trigger node id → `runs test` → read
per-step `creditUsageMetadata`. Downstream pins from a tool node use
`sourcePath: "$.result"` bound to a named input. Any merge node needs BOTH incoming
paths the same length from their common ancestor — an asymmetric join deadlocks
(stays pending forever); balance with a passthrough code node on the short edge.

**Window state**: the sweep's only state is the last sweep date. Store it in the
digest (and/or the table row); next window = [last sweep → today]. First sweep uses
the user's lookback. Never run unwindowed.

## Graduation: from sweeps to the native subscription

Windowed sweeps are for lists you look at occasionally. The moment the watch is
STANDING (weekly+ cadence, 100+ accounts, or the user says "always tell me"), the
right shape is Clay's native signal feed, not a re-scraping loop:

- In-app, on a table holding the account list: add the `trigger-source` action,
  signalType **News** — note it is the combined "News & fundraising" feed; there is
  no standalone Funding signal type. Funding events arrive on this feed.
- Clay auto-spawns one listener side-table per signal type ("News & fundraising
  Events from [table]") — one row per event as it happens. Keep one signal type per
  listener; keep the parent-trace in the table name.
- First action on the listener: hydrate the event row from its origin pointer
  (`origin.tableId` + `origin.recordId` → lookup) — free context you already paid
  for. Then this skill's Step 4-5 (classify → route → digest) applies to listener
  rows exactly as to sweep results.
- Economics: cost scales with EVENTS (~0.5-1 credit each), not accounts × sweeps —
  on 5K monitored accounts expect roughly 50-200 events/month per signal type.
- Don't subscribe the same entity to the same signal type twice across tables, and
  don't attach subscriptions to one-shot lists nobody will watch.

This skill can set up and run sweeps end-to-end; the in-app subscription is a
hand-off it should offer with the arithmetic ("your cadence × list size makes the
subscription cheaper from week N"), not silently build around.
