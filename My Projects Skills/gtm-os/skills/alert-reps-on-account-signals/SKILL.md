---
name: alert-reps-on-account-signals
description: |
  Turn a rep's target-account list into Slack alerts — load the accounts into a Clay Audiences
  segment, watch that segment with three Clay Signals (news and fundraising, new leadership hires
  at C-suite, VP, director and head level, and job postings), and post one Slack message per event
  into a channel the rep names, mentioning the account owner. Built once per list as an ingest
  workflow, three signals and one alert workflow, then it runs unattended on the cadence you set.
  Use whenever someone asks: alert me when my accounts hire a VP, ping Slack when a target account
  raises money, watch my account list for news, tell me when these companies post jobs, set up
  account signals for my territory, or build a Slack alert on my named accounts. Do NOT use it to
  research one account right now (that is a lookback summary, not a watch), to track a named
  person's job change, to enrich or score the list, to write the outreach, or to alert on web or
  topic intent — it ends at a Slack message per event that a person acts on.
category: signals
personas: [account-executive, sales-leader]
mechanism: workflow
touches: writes-records
keywords: [job-change]
---

# Alert reps on account signals (watch the list, post the event, name the owner)

The insight, in the author's words: **a rep should not have to go looking — when something happens
at an account they own, the event should find them where they already are, with the account and
the owner named in the first line.** So the list is loaded once, the watches run on their own, and
every event becomes one Slack line shaped like *"@owner — a key new hire has been filled at Acme:
Jane Doe, VP Sales."* Nothing here scores, enriches or writes outreach; the rep decides what to do.

## Declared inputs

**Nothing here ships with a value.** Each one is the installer's, not the author's: ask for it, never
substitute a plausible default, and where an answer does not exist say which step becomes unavailable
rather than guessing. Where a default IS defensible it is named below, and using it means saying so in
the output.

| Input | What the installer supplies | If it is missing |
|---|---|---|
| **The account list** | a CSV with one row per target account and a column holding the company domain or company LinkedIn URL | no default — nothing to watch |
| **List name** | a short label for this list, e.g. the rep's name or territory; it tags the accounts in Audiences and names the segment, signals and workflows | no default — ask; two lists with the same label would merge |
| **Slack channel** | the rep's own **public** channel for these alerts, by name — one channel per rep, by the author's design; always ask for it, never assume one. Slack must be connected in Clay (Settings → Connections, in this workspace) **and** the Clay app added to the channel; only then does the channel appear in the action's list | no default — the alert step cannot be built; the signals still run and their events stay readable in Clay Audiences |
| **Mention** | the rep's own Slack member ID (the `U…` value from their profile) to put at the front of every alert, if they want the ping | none — alerts carry no mention |
| **Leadership seniority** | which new hires count as leadership, from Clay's seniority levels | **the author's default is c-suite, vp, director, head** — confirm it and say it was used |
| **Job posting titles** | comma-separated title words a posting must contain to alert, e.g. the roles the rep's product serves | none — **every** posting at every watched account alerts, which at a large account is many per week; say so before accepting it |
| **News topics** | which of Clay's news topics alert, from its fixed vocabulary | **the author's default is Fundraising, Investment, Initial Public Offering, Merger & Acquisition, Executive Appointment, New Product Launch, Business Expansion** — confirm it and say it was used |
| **Check cadence** | how often the watches run: daily, weekly, biweekly or monthly | **weekly is defensible** — new hires and postings are billed per account checked on every run, so daily costs about seven times weekly; say which was used |

**If an answer sheet is present beside this skill, load it and ask only for what it does not cover.**
A partial sheet is normal; a value it is missing gets asked for on its own rather than restarting the
interview. **Say which values came from the sheet** before using them — a sheet applied silently is a
wrong field nobody catches. **If there is no sheet, say nothing about sheets** — the check is a file
lookup, not a question, so run the interview as though the feature did not exist rather than reporting
an absence. At delivery, offer to save the answers back (identifiers only — never a token or a
password), private and never published — and phrase the offer so it explains itself: *"want me to save
your answers to a file, so the next person on your team doesn't have to answer these again?"*

## What this skill touches

- **Reads** — the CSV you supply, your Audiences account fields, the Slack channels the Clay app can see, and each signal event as it arrives.
- **Writes** — **Audiences account records** (creates or updates one per row, setting one list-tag field), one Audiences field for the tag if none fits, one Audiences segment, **three Clay Signals** on that segment, two Clay workflows of its own (ingest and alert) with a provenance line in each description, and **one Slack message per event** to the channel you name, through your own connected Slack account.
- **Never** — deletes or blanks any Audiences value, edits a signal, segment, workflow or record it did not create, writes to a CRM, or messages anyone outside the named channel.
- **Vendor-specific** — Slack is load-bearing for the alert step. Without a connected Slack account the signals still run and events remain readable with `clay audiences signals get`, but no alert is sent.
- **Halts** — Step 2 write-approval, Step 3 write-approval, Step 3 spend-approval, Step 4 sample-review

## Step 0 — Verify Clay is working, and say what this does

Say this first, as three sentences: *this loads your account list into Clay Audiences with a tag,
creates three signals that watch those accounts on the cadence you choose, and builds one workflow
that posts a Slack message per event to your channel; it writes to Audiences and Slack and nowhere
else, and it never deletes anything.*

Run `clay whoami; echo "exit_code=$?"`. If it fails, name what is wrong — the CLI missing, below the
version the Clay plugin requires, or signed out — give the one fix (`clay login`, or install the Clay
plugin and run its `setup` skill), and **stop**. Do not install, upgrade or fetch anything to repair
it. Tell the user which workspace you are in.

Then two free checks, before any interview:

- **Slack.** Resolve the channel by name with one free call:
  `clay workflows actions test <slackPackageId> slack-get-channel-id-from-name --inputs '{"channelName":"<channel>"}'`
  (the package is the one whose `packageDisplayName` is Slack in `clay workflows actions list`). A
  `channel_id` back means Slack is connected for this user and the channel is public and reachable;
  keep the id — the send action takes the **channel id**, not the name. **Do not judge the connection
  by `actions dynamic-fields`**: on the author's test it reported `MISSING_ACCOUNT` while the same
  actions ran fine, because the probe binds no default account. A `MISSING_ACCOUNT` on the *test*
  call is the real signal: say so, give the fix (connect Slack in Clay's Settings → Connections, add
  the Clay app to the channel), and offer to continue with the watches only.
- **Signals.** Run `clay signals list`. If it returns `auth_forbidden`, signals are not available on
  this workspace and the skill cannot do its job; say so and stop.

This skill builds through the Clay plugin's `workflows`, `signals` and `audiences` skills — read
them before Step 2 and follow them for every CLI shape (CSV triggers, Audiences upserts, signal
creation, trigger binding). If they are not installed, say the Clay plugin is required and stop.

## Step 1 — Collect the inputs (interview; do not guess)

1. **The CSV** and which column holds the domain or LinkedIn URL. Normalize identifiers (lowercase, strip `www.`, query strings, trailing
   slashes) and dedupe. A row with neither identifier is listed as skipped, never guessed from a name.
2. **List name**, the **Slack channel** (ask for it by name, every time — the channel-name lookup in
   Step 0 returns public channels only, so a private channel has to be given as its id), and
   whether to **mention** the rep.
3. **Leadership seniority**, **job posting titles**, **news topics**, **check cadence** — show each
   default and ask for a yes or an edit. For news topics, accept only words from Clay's fixed
   vocabulary (`clay signals create --help` lists it); a word outside it validates and then matches
   nothing.

## Step 2 — Load the list into Audiences (one gate first)

**Look before building.** `clay audiences fields list --entity-type companies` — find a field suitable
for the list tag. Prefer a **boolean field named for the list** (`Target list: <list name>`), created
with `clay audiences fields create --data-type boolean`: a workspace can hit Clay's **200-field limit
on text, email and URL account fields** (the author's did, 2026-09-28) and boolean fields are still
allowed. A shared text tag field is fine where one already exists.
`clay audiences list --entity-type companies` — an existing segment named for this list means the
list was loaded before; say so and ask whether to add to it. `clay workflows list` — look for
**Load target accounts — <list name>** and reuse it if the graph matches.

**Before creating anything, one message:** the two workflows and their names, the Audiences field(s)
to create, the segment, that N account records will be created or updated with the tag, and that
nothing is deleted. **Wait for an explicit yes.**

Then build the ingest workflow: a `csv_upload` trigger → one tool node, action
`upsert-audiences-record` (package *Audiences*): `entityType` ← `ACCOUNT`; lookup on `domain` when
the column is a domain or `linkedin_url` when it is a LinkedIn URL; record fields ← the list's boolean field set to `true`;
`removeNullValues` ← `true`. Link the CSV with `triggers csv upload`, run **`csv run --limit 3`**
first, read the three runs, then run the rest. Read the runs, not the batch: a run can complete
around an `ERROR_BAD_REQUEST` when a selected field has no binding.

Create the segment with `clay audiences create --entity-type companies --name "<list name>"` and a
filter selecting the list's boolean field equal to `true` (`key` is the field id and `dataPath` is
`["account_entity_field_values","field","<field id>"]`). Confirm the count with
`clay audiences records search-count --audience-id <id>` and compare it to the CSV's row count.
**A count above the row count means the workspace holds duplicate account records for one domain** —
the author's test tagged 20 records for a single `nvidia.com` row, because the upsert's domain lookup
updates every match. Signals bill per record checked and would alert once per duplicate, so narrow the
segment (for example the tag AND a headcount floor, or the record's own LinkedIn URL) until the count
matches, and say what you added.

## Step 3 — Create the three signals, paused, then one gate to start them

**Look before building.** `clay signals list` — a signal of the same type already watching this
segment answers the job, and a second one doubles the spend; reuse it. Otherwise create each with
`clay signals create` **without `--activate`**, watching the segment
(`"entityType": "ACCOUNT", "segmentIds": ["<segment id>"]`), named `<list name> — <type>`:

| Signal | `--type` | Per-type settings | Billed |
|---|---|---|---|
| Leadership hires | `NewHire` | `filters.start_from_method` ← `query`; `filters.job_title_seniority_levels_v2` ← the confirmed seniority list; `filters.job_title_exclude_keywords` ← `Office of, Assistant`; `lookBackTimeWindowInMonths` ← 1 (the author's test used 3, to see events on the first run) | per account checked, per run |
| Job postings | `JobPost` | `filters.startFrom` ← `ClayTableOfCompanies`; `filters.job_title_keywords` ← the confirmed titles (omit the key only if the installer accepted "every posting"); `filters.max_num_days_since_posted` ← the cadence in days | per account checked, per run |
| News and fundraising | `News` | `filters.topics` ← the confirmed topics; `filters.autoAdvanceEarliestPublishDate` ← `true`; `filters.earliestPublishDate` ← today; `filters.maxNewsPerDomain` ← 5 | **per event**, so the topic list is the cost lever |

`--schedule` ← the confirmed cadence on all three. Read each back with `clay signals get` and
confirm type, segment, filters and schedule. **Then one message:** the three signals as created, the
segment and account count, that starting them begins spending on every run — per account for hires
and postings, per event for news — and the ask. Give the per-record and per-event prices only as the
platform reports them; the author did not measure them. **Wait for an explicit yes**, then
`clay signals resume` each one. **Signals detect changes after monitoring starts**: say plainly that
the first alerts arrive after the first scheduled run, and that hires and postings that predate the
signal do not fire.

## Step 4 — Build the alert workflow, test one message, then leave it running

`clay workflows list` — look for **Account signal alerts — <list name>**; reuse if the graph
matches. Otherwise create it with three `audience_signal` triggers, one per signal, each bound to
that signal's **`signal.id`** (the `sig_…` value from `clay signals list`, not the entry id) with
`entityType` `ACCOUNT`, all wired to one tool node:

- **Post to Slack** — action `send-message-to-channel-botname` (package *Slack*), on the installer's
  connected Slack account: `targetSlackChannel` ← the **channel id** from Step 0 (static), `botName` ← `Account signals`, `summary` ← the message below, built by
  `reference` from the trigger payload. Slack bills nothing to Clay; it runs on the installer's own
  connected account.

The message, one line per event type, in Slack markdown, with the mention first when the rep asked
for one (`<@U…>`), else nothing:

- new hire — `<@owner> A key new hire has been filled at *<account>*: <person name>, <title>. <profile link>`
- job posting — `<@owner> *<account>* is hiring: <job title> (<location>). <posting link>`
- news — `<@owner> News at *<account>* — <topic>: <headline>. <article link>`

**The trigger's payload has two halves**, both confirmed on the author's test (2026-09-28): the
account's Audiences fields under `$.fields` by display name (`$.fields["Company name"]`,
`$.fields.Domain`, `$.fields["LinkedIn URL"]`), and the event under `$.signal` (`signalType`,
`emittedAt`, `activityTime`, and `data`, whose shape is per type). For a **NewHire** event the
author read a real payload: `$.signal.data.fullProfile.name`, `.latest_experience_title`,
`.latest_experience_start_date`, `.latest_experience_company`, `.location_name` and `.url` (the
person's profile). **JobPost and News payloads were not observed** — before wiring those two
messages, read one event of each with `clay audiences signals get --segment-id <id> --since <date>
--signal-types JobPost,News` and take the paths from its `data`; until one exists, wire the account
name and `signalType` only and finish the fields after the first run posts. Record the paths you used
in the workflow's description.

**Test one message** with `clay workflows nodes test <wf> <slackNode> --inputs` carrying **the
node's own pinned inputs by name** (`company`, `person`, `title`, `started`, `profile`), not the
trigger payload — a node test resolves no upstream pins, and the author's first attempt posted a
message with every field blank. Confirm in the channel that it arrived and reads as above. The author did this on 2026-09-28: a direct send and
a node test both posted to the test channel, and the send action reported `wasSent: true` with a
`message_ts`; Slack billed nothing to Clay and used one action execution. **Show the installer the
message** and wait for a yes before publishing. Then `clay workflows publish` so the triggers run on
the live graph, write the provenance line into both workflows' descriptions (see below), and stop —
from here the signals and the alert workflow run unattended.

**Provenance line:** read each workflow's description with `clay workflows get`; if it is `null`
write the skill's one-line description, a newline, then `Sourced from marketplace skill:
<slug>@<revision>` using the `marketplace_slug` and `marketplace_revision` this file's frontmatter
carries when installed from the Marketplace; if those fields are absent, say *"Marketplace
attribution is unavailable for this skill"* and write no marker. If a marker is already there, write
nothing and say so; if a different marker is there, stop and report the conflict.

## Step 5 — Deliver

One summary: the list name, accounts loaded (created vs updated vs skipped), the segment and its
count, the three signals with their cadence and filters, the channel, the mention rule, the test
message as posted, and where to look — `clay signals list` for run status and errors,
`clay audiences signals get` for events, `clay workflows runs list` for alert runs. Then the
answer-sheet offer from *Declared inputs*.

## Representative output

### Setup summary

| List | Accounts loaded | Segment count | Signals | Cadence | Channel | Mention |
|---|---|---|---|---|---|---|
| Northwind territory | 48 created · 2 updated · 1 skipped (no domain) | 50 (matches CSV) | Leadership hires · Job postings (titles: *Data, Analytics*) · News (7 topics) | weekly | #northwind-dana | @Dana |

### Slack alert

```
@Dana Whitfield  A key new hire has been filled at *Contoso*: Priya Raman, VP Data Platform. linkedin.com/in/…
```

### Where to look

- Signal health: `clay signals list` — `runStatus` and any `error.userFriendlyMessage`
- Events so far: `clay audiences signals get --segment-id <id> --since <date> --signal-types NewHire,JobPost,News`
- Alerts sent: `clay workflows runs list <alert workflow id>`

## What this skill does not claim

- The logic comes from the author's interview, not from a table or workflow that already ran; nothing has checked it against a system in production.
- Only the NewHire event payload was observed by the author; JobPost and News payloads are read from a real event at install time, and the skill says when those fields are still unwired.
- The author's test built the ingest workflow, the segment and the three signals, ran the hire signal once, and posted two test messages to Slack (one direct, one through the alert node with a real hire payload). No alert has yet been produced end to end by a live signal event; that path is the same trigger and node, unobserved.
- Per-account and per-event signal prices were not measured; the platform's reported figures are what the installer sees.
- How many alerts a list produces per week was never measured; a large account with no posting-title filter can produce many.
- Whether a new hire the signal reports is truly leadership depends on Clay's seniority classification of the title.
- Slack delivery is only confirmed by the test message; a channel the Clay app is later removed from fails silently until someone checks `runs list`.
- The default news topic list is the author's reading of "news and fundraising"; it was never tuned against alert volume.

## What good looks like

- Every alert names the account and, when the rep asked, mentions them.
- A rep can read the channel for a week and see only hires at the chosen seniority, postings for the chosen titles, and news on the chosen topics.
- Nothing in Audiences was deleted or blanked; the only new values are the tag and the owner ID.
- The signals were created paused and started only after the spend was stated and agreed.
- The common mistake: activating signals before the segment count is confirmed, and paying to watch an empty or wrong list.

## Rules

- MUST create every signal paused and start it only after the installer sees the spend model and says yes.
- MUST confirm the segment's account count against the CSV before creating any signal.
- MUST take the alert message's field paths from a real event payload, and say when they are still unwired.
- MUST use `removeNullValues: true` on the upsert; NEVER blank or delete an Audiences value.
- MUST look for an existing segment, signals and workflows for this list name before building, and NEVER edit any it did not create.
- MUST post only to the named channel, through the installer's connected Slack account.
- NEVER write to a CRM, enrich, score or draft outreach — this ends at the alert.

## Worked example

Ask: "Set up Slack alerts on my 50 target accounts — new execs, jobs, funding." Step 0: signed in;
Slack connected; signals available. Step 1: CSV with a `domain` column; list
name *Northwind territory*; channel `#northwind-dana`, mention @Dana; seniority default confirmed; posting titles
*Data, Analytics*; news topics default confirmed; weekly. Step 2: boolean field *Target list:
Northwind territory* created; ingest workflow built; 3 rows tested, then 47; segment created, count
50, matching the CSV.
Step 3: three signals created paused, read back, spend model shown, yes, resumed. Step 4: alert
workflow with three signal triggers → Slack; a sample payload tests one message into the channel;
paths for each type wired after the first weekly run; published. Step 5: summary as above, and the
answer-sheet offer.
