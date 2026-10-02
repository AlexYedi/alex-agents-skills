# Detector mechanics — the net-new arm, noise profiles, harvest rules, surfaces

Live-verified 2026-08-12 (isolated eval workspace); re-verify per workspace —
catalogs, costs, and payload shapes drift on an alpha platform.

## What this surface has (and doesn't)

| Arm | Verdict (live-checked) |
|---|---|
| `find-google-news-results` (catalog action, ~1 credit) | **The net-new detector.** Free-text `query` (required), `date_filter` (relative buckets `qdr:h/d/w/m/y`), `hl`. Event-anchored queries (no company in the query) return articles about companies you don't know yet. |
| RSS / trigger-source / webhook fan-in actions | **Absent from the action catalog** (all ~650 actions checked). The KB's detector-mesh architecture is in-app-only. |
| Company search (`clay search filters-mode`) | **No event or date filters** (only static firmographic fields + a funding-amount band) — search cannot source by signal; it is the ICP-first arm (build-prospect-list's turf). |
| Structured event lookups (fundraising-data, latest-funding, job-openings actions; ~6 credits) | All take a **domain as input** — corroboration arms for candidates you already resolved, never sourcing arms. |
| `audience_signal` workflow trigger | Subscribes a workflow to ONE pre-configured in-app signal, firing a run per event. The signal definition itself cannot be created or listed from this surface — graduation path, verify per workspace. |

## The query contract

- Compose queries as **event vocabulary × ICP qualifier** (round/incident/expansion
  vocabulary × vertical/industry term). Two to three variants per signal type beats
  one broad query — vocabulary drives the noise profile (below).
- Quoted phrases are RECALL, not precision (live: a quoted round name returned
  adjacent-round raises and a preferred-stock conversion notice). Never treat the
  query as the qualifier; the gates qualify.
- Windowing is relative buckets only (`qdr:*`) — precise windows need bucket +
  post-filter on derived dates.
- **Quiet shape**: the `news_results` field is ABSENT entirely (not an empty
  list). Gate on absence-of-events; the credit is billed either way.
- **The date stamps are crawl dates.** Live-verified: a years-old roundup surfaced
  inside a one-week bucket stamped "3 days ago" — the bucket bounds when the index
  saw the page, not when the event happened. Also, dates arrive as relative
  strings ("6 days ago"); parse to absolute at sweep time, then treat as a claim.

## Noise profiles by vocabulary (live-observed; expect both mixes)

| Vocabulary family | Dominant noise | Countermeasure |
|---|---|---|
| Funding/round terms | Roundup + listicle pages; false vocabulary matches (finance-instrument notices, adjacent rounds); social posts with garbled figures; stale archives with fresh crawl stamps | Harvest roundups per below; per-candidate event verification; drop social; derive dates from content |
| Incident/breach terms | High article precision but heavy CROSS-OUTLET DUPLICATION (one event in 3–4 outlets per sweep); law-firm "investigation" PRs derivative of the true event; tracker/listicle pages | Dedupe on (entity, event); demote law-firm PRs to entity-only leads; corroborate to the primary notice |

## Harvest rules (article → candidate)

The unit of work is a CANDIDATE = (company, claimed event), never an article.
**Order matters**: classify the source (rules 1–4) → dedupe into event clusters
(rule 6) → derive the merged candidate's event date from its best-basis source
(rule 5) → window-check the merged candidate. Dating before dedupe kills cluster
members one by one on their weakest source; the EVENT is the unit that lives or
dies.

1. **Direct event article** → one candidate: name, event type, claimed date
   (from text/URL), amount/scale if stated, source URL.
2. **Event roundup/digest page** (weekly deals roundup, breach tracker — pages
   aggregating DATED events) → harvest every named company as a candidate marked
   `corroboration-required`. Sourcing posture inverts the monitoring rule: when
   WATCHING a named account, aggregator pages are dropped (a page about history
   is not an event); when SOURCING, an event roundup is a candidate-rich feed —
   but the roundup is a pointer, not evidence. Each harvested candidate must be
   corroborated per-company (primary article or structured lookup) before
   delivery. Harvest ONLY entries matching the sweep's signal menu (a deals
   roundup mentions acquisitions, milestones, hires — take what was asked for),
   and only entries whose own claimed timing can sit inside the window; a
   roundup aggregating a longer period than the sweep ("this summer", "this
   year") contributes only its in-window entries. **Profile listicles are not
   event pages** ("top X to watch", "best Y of 2026" — companies aggregated by
   PROFILE, not by something that happened): drop them; harvesting them
   manufactures undated candidates that waste corroboration spend.
3. **Social posts / forums** → drop the article (garbled figures observed live);
   an entity may be re-harvested if another source carries it.
4. **Law-firm / class-action PRs and other derivative coverage** → the
   underlying event is usually real but the page is derivative; keep the entity,
   mark `corroboration-required`, cite the primary notice in delivery. A
   derivative source's dates never DATE the event and never KILL the candidate —
   they simply don't count; the date comes from corroboration or a primary
   cluster-mate.
5. **Date derivation** — the date of the UNDERLYING EVENT, not the article:
   in-text event date > URL-path date > publication dateline (weakest — derivative
   coverage is fresh about old events: a new lawsuit story dates the lawsuit, not
   the breach it's about). For incident/disclosure signals the actionable event
   date is the DISCLOSURE/notification date, not the incident's start (breaches
   are often months old when disclosed — a prior-report or filing date in the
   text dates the disclosure and counts). Applied to the merged candidate using
   its best-basis source: outside the window kills it (recorded); no derivable
   date → `undated`, deliverable only if corroboration supplies the date.
6. **Dedupe into event clusters** across the whole sweep — key on (entity,
   event-type, approximate date), and merge on EVENT FINGERPRINT (matching scale
   figure, geography, timing) even when names differ or are missing: one outlet
   names the parent, another the subsidiary, a third no company at all — one
   incident, one candidate, all names carried forward for Step 5 to resolve to
   the entity the user would actually sell to. Lead-source primacy: the
   disclosing party's own notice > regulator/registry filing > trade press
   (peers — pick any, say so). An unnamed-entity article matching no cluster is
   an `unresolved-entity` candidate. Same entity with two DIFFERENT events = two
   candidates.
7. **Name-boundary discipline** (monitoring kin, applies here too): a candidate
   name must not be a prefix of a longer org name (suffix tokens:
   Partners/Group/Capital/Holdings) or a vessel/product designation. Resolution
   (SKILL.md Step 5) is where near-name traps are finally settled.

## Build-once query workflow (bypasses the ad-hoc daily quota)

Ad-hoc action execution is capped per workspace per day (25) and other work
shares it — route sweeps through a workflow. One-time build (CLI + the plugin's
workflow tools):

1. `clay workflows create --name "<yours>"` — created workflows are trigger-less.
2. Add a manual trigger via the plugin's trigger-edit tool: `triggerType:
   manual`, inputSchema requiring `{query, date_filter}` — this call creates AND
   binds the canvas trigger node.
3. Read the workflow back (plugin's read tool, summary mode) for the trigger's
   `wfn_…` node id — the create response returns only a UUID resourceId.
4. Add a tool node wired from that node id: the news action, both inputs mapped
   as references (`{{query}}`, `{{date_filter}}`). Pinned-input discipline: every
   run must supply both (undefined AND `""` fail the run).
5. Per query: `echo '{"query":"...","date_filter":"qdr:w"}' | clay workflows runs
   test <wf> --inputs -` → `clay workflows runs get <wf> <runId> --wait 60
   --verbose` → the tool node's `outputs.result.news_results` is the payload;
   run-level `dataCreditsUsed` is the measured cost.

If the plugin's workflow tools are unavailable in the session, the CLI's `clay
mcp` stdio server exposes the same tools (initialize → tools/call) — same
contract.

## Degraded-mode corroboration (no general web egress)

Sandboxed sessions may be unable to fetch arbitrary article URLs (the proxy denies
general egress), and incident-type signals have NO structured corroboration action
in the catalog (structured lookups are funding/jobs only) — so "fetch the primary
source" can be unexecutable. The substitute ladder: (1) cross-outlet agreement —
≥2 independent outlets carrying the same event fingerprint corroborates the event;
(2) the enrichment/search echo corroborates the ENTITY (never the event); (3) a
candidate left with one derivative source drops as `uncorroborated — source
unreachable`. State which mode the sweep ran in; never claim primary-source
verification that didn't happen.

## Cost model (state before the sweep)

- Query: ~1 credit each, quiet or not. Fan-out = signal types × variants.
- Resolution/qualification: ~1 credit per surviving candidate (company
  enrichment; band-string outputs — compare as bands, never parse to ints).
- Premium corroboration: structured funding/jobs lookups ~6 credits per company —
  shortlist only, named and approved.
- Read measured cost from the workflow run's `dataCreditsUsed`; ad-hoc/routine
  surfaces that expose no usage metadata get "declared estimate" wording.

## Graduation (standing watches)

A repeated ask ("every week, same definition") should not become a re-scraping
loop. Hand off to the in-app signal engine: native signal subscriptions on
tables (one listener side-table per signal type; cost scales with events, not
sweeps) and — where configured — `audience_signal` triggers that fire a workflow
run per event. Offer the arithmetic (cadence × fan-out vs per-event cost); the
sweep remains right for one-shot and exploratory definitions.
