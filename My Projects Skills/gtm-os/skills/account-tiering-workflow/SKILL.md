---
name: account-tiering-workflow
description: |
  Stand up an always-on account-tiering workflow in Clay — a signal-triggered pipeline that fires per
  account as it enters an audience, enriches it, scores its fit for your product, tiers it, and writes
  the result back onto the record with no one in the loop. Use whenever someone asks: build me an
  account-tiering workflow, score accounts for fit as they enter a segment, tier my book automatically
  and write it back to the CRM, run fit scoring on a schedule, or set up an unattended account-scoring
  pipeline. It scores prospects and existing customers on DIFFERENT rubrics (net-new fit vs upgrade
  potential), and it separates fit from timing: a strong-fit account with no live signal is Tier 2, not
  Tier 1. It reads the account record and public enrichment, and it WRITES six scoring fields back onto
  the account. Do NOT use it to tier a static list you paste in once with nobody triggering it (that is
  a function-calling scorer, not a workflow), to route inbound leads or people, to audit whether a CRM's
  existing fields are accurate, or to monitor a single company for one signal. It never contacts anyone
  and never deletes a field.
category: score-and-qualify
personas: [revops, gtm-engineer]
mechanism: workflow
touches: writes-records
keywords: [lead-scoring, tech-stack, plg]
marketplace_identity_schema: 1
marketplace_slug: account-tiering-workflow
marketplace_revision: 2
---

Whenever you create or copy a workflow, append `Sourced from marketplace skill: account-tiering-workflow@2` to its description. Preserve the existing description and do not add the same line twice.

# Account tiering workflow

The insight: **fit and timing are two axes, not one, and a single score cannot serve both a prospect
and a customer.** A book ranked by fit alone points reps at accounts with no reason to be called this
week; a book ranked by activity alone points them at noise. So the tier is a fit score *gated on a live
signal* — Tier 1 is strong fit **and** a reason to act now, and a strong-fit account with nothing
happening is Tier 2 "nurture," not a missed Tier 1. And because a prospect and an existing customer are
different questions — *would they buy* versus *would they upgrade* — the plan the account is on picks
which rubric it is scored against, deterministically, before any judgment runs.

Two more things follow from "unattended." Because a signal starts each run and no one is present, the
tier CUT lives in a **code** step, not the scoring model — the model produces the dimension scores and
the rationale, arithmetic and thresholds are deterministic and auditable. And because it writes to the
record, the whole thing is gated: nothing is built or run against real accounts without an explicit yes,
with the cost and the write named in the same breath.

## Declared inputs

**Nothing here ships with a value.** Each one is the installer's, not the author's: ask for it at build
time, never substitute a plausible default, and where an answer does not exist say which step becomes
unavailable rather than guessing. Where a default is defensible it is named, and using it means saying
so in the output.

| Input | What the installer supplies | If it is missing |
|---|---|---|
| **The trigger audience** | the Clay audience/segment whose accounts should be scored as they enter it | no default — there is nothing to trigger the workflow |
| **Your product & ICP** | one paragraph on what you sell and to whom, and what signals fit: the tooling, hiring, firmographics and usage that mean a good account for *you* | ask — this is the whole scoring rubric; without it the score is generic and wrong |
| **Account-record fields** | which fields on the record hold: domain, company LinkedIn URL, company name, current plan/tier, acquisition type (prospect/customer/churned), a usage metric, open pipeline, open-opp count, engagement status & summary, last-signal date, employee count | each unmapped field drops out of scoring and is listed as unobserved; domain is required (it is the write key) |
| **In-scope rule** | which accounts should run at all — the default is *prospects, plus existing customers on the plan you want to expand from*; everything else ends the run before any credit is spent | ask — an empty rule scores your whole audience and spends on accounts you would never work |
| **Expansion-from plan** | the plan name that means "existing customer worth an upgrade motion" (the source workflow used `Pro`) | if absent, every in-scope account is scored on the New-Business rubric only |
| **Usage-pressure thresholds** | the usage-metric cut-offs that mean an account has outgrown its plan (source defaults: ≥5 moderate, ≥10 high, ≥20 severe) | default to the source values and say so; only meaningful on the Expansion track |
| **Tier cut-offs** | the score cuts for the tiers (source defaults: ≥75 Tier 1/2 line, ≥60 Tier 2/3 line) | default to the source values and say so — they are editable, and a distribution with most accounts in Tier 1 means re-tune, not celebrate |
| **Tech-stack connected account** | the connected account for the tech-stack lookup (the source used a BuiltWith key, billed to that account, not in Clay credits) | if absent, either connect one or swap in a Clay-credit tech action — say which, and that the tech dimension is otherwise unobserved |
| **Write-target fields** | the six account fields to write: fit score, tier, priority, rationale, why-now, track — created in the audience if they do not exist | if the installer does not want a write, this is not this skill (see the boundary) |

**If an answer sheet is present beside this skill, load it and ask only for what it does not cover.** A
partial sheet is normal; a value it is missing gets asked for on its own rather than restarting the
interview. **Say which values came from the sheet** before using them — a sheet applied silently is a
wrong field nobody catches. **If there is no sheet, say nothing about sheets** — the check is a file
lookup, not a question, so run the interview as though the feature did not exist. At delivery, offer to
save the answers back (identifiers and settings only — never a token or a password), private and never
published, phrased so it explains itself: *"want me to save your answers to a file, so the next person
on your team doesn't have to answer these again?"*

## What this skill touches

- **Reads** — the account record on the trigger audience (the fields you map), plus four per-account public enrichments: tech stack, open GTM roles, headcount growth, and company profile.
- **Writes** — six scoring fields onto each in-scope account record: fit score, account tier, priority flag, fit rationale, why-now, and tiering track. It creates those fields in the audience if they are absent; it does not touch any other field, and `removeNullValues` is on so a blank result never overwrites existing data.
- **Never** — contacts anyone, deletes or blanks a field, moves account data to a third party, or scores an account it never enriched.
- **Halts** — Step 3 write-approval, Step 5 spend-approval, Step 5 write-approval.

## Representative output

### Scored & tiered account record

Six fields written per in-scope account — one deliverable, six fields. This is their shape (placeholder
accounts, invented values); `fabrikam.example` is the insight on one row: a 77 clears the fit bar and
still lands Tier 2, because Tier 1 requires a live signal.

| Account | Track | Fit score | Tier | Priority | Why now | Rationale |
|---|---|---|---|---|---|---|
| northwind.example | New Business | 82 | Tier 1 | Yes | 3 RevOps roles posted in the last 60 days | Full outbound stack (CRM + sequencer + data provider), RevOps + GTM-engineering hiring, 22% headcount growth; engagement thin, scored conservatively there. |
| contoso.example | Expansion | 88 | Tier 1 | Yes | severe usage pressure on the current plan (24 workspaces) | On the expansion plan with 24 workspaces — structurally past it; large, still-hiring GTM org; open opportunity already in flight. |
| fabrikam.example | New Business | 77 | Tier 2 | No | No timing signal | Strong stack and healthy growth, but no GTM roles posted, no recent funding, and last signal is stale — good fit, nothing making it live this week. |

The ranking key the workflow computes (fit + a Tier-1 bonus + a Priority bonus) is what makes a
downstream digest sortable; it is computed but not written to the record.

## Step 0 — State the posture, then confirm the platform

Say it before anything runs: **this reads the account record and public enrichment, and it WRITES six
scoring fields back onto each in-scope account.** It contacts no one, deletes nothing, and moves nothing
off-platform. Where it runs decides what it costs — the enrichment and the write bill in the installer's
own workspace, per account, and the numbers are read there at build time, never quoted from anywhere
else.

Then confirm Clay is working: run `clay whoami; echo "exit_code=$?"`. If it fails or the Clay tools are
missing, run the Clay plugin's `setup` skill, restart if it says to, and re-run this skill. Name the
workspace out loud. **If the installed CLI is below the workflow surface's minimum, that is the
installer's to fix** — name the component, the version, and the one command that updates it, then stop.
Do not clone, fetch, or rebuild the platform to repair it.

## Step 1 — Collect the definition (interview at build; do not guess)

Ask for the declared inputs above, in this order, and stop as soon as the picture is complete:

1. **The trigger audience and the account fields.** Which audience fires the workflow, and which field
   on the record holds each input the scoring needs (domain, company LinkedIn URL, plan, acquisition
   type, usage metric, pipeline, engagement, employee count, last-signal date). Domain is required — it
   is the key the write upserts on. Every field they cannot map drops out of the score and is reported
   as unobserved, never scored as zero.
2. **Your product and ICP, in their words.** What they sell, to whom, and what makes an account good for
   *them* — the tooling a fit account runs, the roles it hires, the firmographics and the usage that
   signal budget and urgency. This becomes the scoring prompt. *(As a shape, not a default: the source
   workflow sold a GTM data-and-automation platform, so its fit signals were an outbound stack —
   CRM + sequencer + data provider — plus RevOps / GTM-engineering hiring and headcount growth. Use
   their signals, not these.)*
3. **The in-scope rule and the two tracks.** Who runs at all (default: prospects + customers on the
   expansion-from plan), which plan name means "expansion candidate," and confirm the two-rubric design:
   prospects scored on net-new fit, expansion candidates scored on upgrade potential. If they only sell
   net-new, drop the Expansion track and say so.
4. **The thresholds.** Tier cuts (default ≥75 / ≥60) and usage-pressure cut-offs (default 5 / 10 / 20).
   These are the installer's and editable — carry the source defaults, say they are defaults, and note
   that a distribution with most accounts in Tier 1 means the weights or cuts need re-tuning.

## Step 2 — Confirm node syntax on the installed version

**Never hardcode the build commands.** Read them off the CLI that is actually installed before writing a
node:

```
clay workflows nodes --help
clay workflows actions list                 # the action catalogue, greppable
clay workflows actions schema <packageId> <actionKey>   # the real input parameters
```

Resolve every action by the **`(packageId, actionKey)` pair, never the key alone** — keys collide across
packages (one `enrich-company` is a different vendor and price from another). The pairs the source
workflow used, as a starting point to confirm against the installed catalogue, not to trust blind:

| Step | packageId | actionKey | Reads → writes |
|---|---|---|---|
| Tech stack | `0a9cacbc-efd8-406d-a5f8-11b2f22b44a5` | `lookup-technology-stack-new` | domain → `$.result.technologiesFound` |
| GTM hiring | `e251a70e-46d7-4f3a-b3ef-a211ad3d8bd2` | `cpj-find-lists-of-jobs` | company LinkedIn URL → `$.result.jobs`, `$.result.jobCount` |
| Headcount growth | `e251a70e-46d7-4f3a-b3ef-a211ad3d8bd2` | `cpj-get-company-employee-growth` | company LinkedIn URL → `$.result.percent_employee_growth_over_last_6_months` / `_12_months`, `$.result.employee_count` |
| Company profile | `e251a70e-46d7-4f3a-b3ef-a211ad3d8bd2` | `cpj-enrich-company` | company LinkedIn URL → `$.result.{founded,industry,type,annual_revenue,description}` |
| Write | `b1ab3d5d-b0db-4b30-9251-3f32d8b103c1` | `upsert-audiences-record` | domain (lookup) → the six fields |

## Step 3 — Build the workflow  *(write-approval: creating nodes in the workspace)*

Say what is about to be created — a trigger and nine nodes in this audience — and get a yes before
creating anything. Then build in dependency order. **Tool-node pins read `$.result.<path>`; code-node
and trigger pins read `$.<path>`** — mixing them resolves to null. This pipeline is linear (no merge
node), so map every downstream input straight from the trigger or from the specific upstream node that
produced it, never "through" an enrichment node — a tool node does not echo its own inputs.

1. **Trigger** — `audience_segment` on the installer's audience. Exposes the account record at
   `$.fields.<Field>`.

2. **In-Scope Gate** — a conditional (rules mode). The default rule, OR-combined:
   acquisition type = prospect, **or** plan = the expansion-from plan, **or** the record's type = prospect.
   Set **`endRunOnNoMatch: true`** — an unmatched account ends the run here, before any enrichment
   credit is spent. State this fallthrough explicitly; it is the credit-protection move.

3. **Resolve Track** — a **code** node. Deterministically picks the rubric and grades usage pressure:

   ```python
   def handler(context):
       def s(key):
           v = context.get_input(key)
           return str(v).strip() if v is not None else ""

       product_tier = s("product_tier")          # the account's current plan
       acquisition_type = s("acquisition_type")
       csv_type = s("csv_type")
       try:
           usage = int(float(context.get_input("usage_metric") or 0))
       except (TypeError, ValueError):
           usage = 0

       # DECLARED INPUTS — read from the workflow's inputs; the defaults are fallbacks, not literals.
       expansion_plan = s("expansion_plan")                                 # the plan you expand FROM
       moderate = int(float(context.get_input("pressure_moderate") or 5))   # defaults shown; editable
       high     = int(float(context.get_input("pressure_high")     or 10))
       severe   = int(float(context.get_input("pressure_severe")   or 20))

       if expansion_plan and product_tier.lower() == expansion_plan.lower():
           track, rubric = "Expansion", "upgrade potential from your {} plan".format(expansion_plan)
       else:
           track, rubric = "New Business", "net-new fit for your product"

       pressure = "none"
       if track == "Expansion":
           if usage >= severe:   pressure = "severe"
           elif usage >= high:   pressure = "high"
           elif usage >= moderate: pressure = "moderate"

       return {
           "track": track, "rubric": rubric,
           "product_tier": product_tier or "none",
           "acquisition_type": acquisition_type or csv_type or "unknown",
           "usage": usage, "usage_pressure": pressure,
       }
   ```

4–7. **Four enrichment tool nodes**, wired as a **serial chain** exactly as the source builds them —
   Resolve Track → Tech Stack → Hiring → Headcount → Company Profile → Score Account Fit. Each is fed
   from the account record (domain or company LinkedIn URL), not from the node before it. **All four
   always run — this is not a waterfall**, so ordering them buys no saving; the per-account cost is
   simply the sum of the four. **Parallel is possible** — every dependency is on the trigger record, not
   on the prior enrichment — **but it needs a merge node before the scoring step, and that shape has not
   been run** (the serial chain needs no merge, and an asymmetric merge stays pending forever). Since this
   fires per account on an unattended trigger, nobody is waiting
   on the latency, so the serial chain is the shape that ships. For every paid step name the four
   things — what runs (the pair from Step 2), what goes in (which mapped field), what to verify, and what
   it costs in *this* workspace — and read the real cost with `clay routines get <id>` / the action
   schema before promising a number:
   - **Tech stack** — verify `$.result.technologiesFound` is non-empty. Empty is the common case (in the
     source, populated on ~1% of accounts), so treat empty as *no detectable stack, scored
     conservatively*, never as an error. Billing usually runs on the installer's own connected account
     (no Clay credits) — say so rather than quoting a credit price that does not exist.
   - **GTM hiring** — cap `limit` (source used 10) and filter to GTM titles and the last 60 days.
     **Cost trap, verified on this action family: some arms bill PER RESULT FOUND, not per call** — the
     basis lives in the parameter description, not the cost field, so a call can cost up to `limit`×
     the unit. Read the schema, keep the cap, and price it at the cap.
   - **Headcount growth** — verify the growth fields; **a null horizon is not 0%** — read it as
     unobserved, not as shrinkage.
   - **Company profile** — verify `founded / industry / type / annual_revenue / description`.

8. **Score Account Fit** — an **agent** (Claygent) node, `agentType: account`. It applies exactly one
   rubric, chosen by `track`, and returns dimension scores plus prose — never the tier. Output schema
   (product-neutral keys, none named after this workflow): `fit_score` (0–100), the four dimension scores
   `motion_or_usage` / `hiring` / `growth` / `engagement`, `fit_rationale`, `why_now`,
   `recommended_play`, and `has_timing_signal` (Yes/No). The tier code recomputes the total from the four
   dimensions, so the model's own total is informational. The prompt, generalised — fill the ICP from
   Step 1:

   > You are scoring one account for **{your company}**'s sales team. {your company} is {one-paragraph
   > product description}. The best-fit accounts are {ICP in their words}.
   >
   > Score this account on the rubric its **Track** selected.
   >
   > **New Business** — net-new fit, out of 100: motion & stack (0–35), GTM hiring (0–25), growth &
   > funding (0–20), engagement & intent (0–20).
   > **Expansion** — upgrade potential, out of 100: usage pressure against the current plan (0–35, the
   > dominant signal — severe/high usage means the account has structurally outgrown its plan), GTM team
   > scale & hiring (0–25), growth & funding (0–20), engagement & champion strength (0–20).
   >
   > Rules: use only the evidence provided; where a signal is missing, score that dimension
   > conservatively and say so in the rationale; **the four dimension scores must sum to the total**; set
   > `has_timing_signal` to Yes only if at least one holds — a GTM role posted in the last 60 days, a
   > funding event in the last 6 months, engagement status highly/moderately engaged, or usage pressure
   > high/severe — otherwise No; `fit_rationale` is 2–3 sentences naming the specific evidence used;
   > `why_now` is one sentence on the timing hook or exactly "No timing signal."

9. **Tier & Priority** — a **code** node. This is where fit becomes a tier, and it is deterministic on
   purpose. **Recompute the total from the four dimension scores here** rather than trusting the model's
   addition — the model judges, the code adds:

   ```python
   def handler(context):
       def n(key):
           try: return float(context.get_input(key) or 0)
           except (TypeError, ValueError): return 0.0
       def s(key):
           v = context.get_input(key); return str(v).strip() if v is not None else ""

       # deterministic total: sum the dimensions the model scored, don't trust its arithmetic
       score = round(n("motion_or_usage") + n("hiring") + n("growth") + n("engagement"), 1)
       timing = s("has_timing_signal").lower() == "yes"
       track = s("track") or "New Business"
       pressure = s("usage_pressure").lower()
       engagement = s("engagement_status")
       pipeline = n("open_pipeline")

       # DECLARED INPUTS — tier cut-offs read from inputs; the defaults are fallbacks, not literals.
       tier1_cut = float(context.get_input("tier1_cut") or 75)
       tier2_cut = float(context.get_input("tier2_cut") or 60)
       if score >= tier1_cut and timing:
           tier, reason = "Tier 1", "Strong fit with a live timing signal"
       elif score >= tier1_cut:
           tier, reason = "Tier 2", "Strong fit but no timing signal — nurture until one appears"
       elif score >= tier2_cut:
           tier, reason = "Tier 2", "Moderate fit"
       else:
           tier, reason = "Tier 3", "Weak fit on the evidence available"

       reasons = []
       if engagement.lower().startswith("highly"): reasons.append("highly engaged in the last 90 days")
       if pipeline > 0: reasons.append("open pipeline of {:,.0f}".format(pipeline))
       if pressure in ("high", "severe"): reasons.append("{} usage pressure on the current plan".format(pressure))
       is_priority = tier == "Tier 1" and len(reasons) > 0

       # Internal output keys — the WRITE node maps these to the installer's OWN field names,
       # never to fields named after this workflow.
       return {
           "account_tier": tier, "tier_reason": reason,
           "priority_account": "Yes" if is_priority else "No",
           "priority_reason": "; ".join(reasons) if reasons else "none",
           "fit_score": score, "track": track,
           "sort_key": score + (1000 if is_priority else 0) + (500 if tier == "Tier 1" else 0),
       }
   ```

10. **Write Scores to Audiences** — the `upsert-audiences-record` tool node. `entityType: ACCOUNT`, look
    up by domain, `removeNullValues: true`. **Map the internal outputs to the installer's OWN field
    names, never to fields named after this workflow:** `fit_score`, `account_tier`, `priority_account`,
    and `track` come from the code node; `fit_rationale` and `why_now` come from the scoring node — each
    is written into the field the installer named in Declared inputs. Confirm those fields exist in the
    target audience and create them with the installer's chosen labels if not; do not reuse another
    audience's field ids, and do not invent field names of your own.

## Step 4 — Validate and dry-run a small sample

Validate the graph (`clay workflows graph validate <id>`), then run it against a **small sample of
in-scope accounts** and read the payloads before the write goes wide: confirm each enrichment returns at
the path named (completion status is never data — gate on non-empty values), confirm the track resolves
correctly for a known prospect and a known customer, and confirm the tier cut behaves at the boundary (a
≥75 with no timing lands Tier 2, not Tier 1). Fix mappings here, where it is cheap.

## Step 5 — First live batch, then go live  *(spend-approval + write-approval, one gate)*

Everything free has run. Now, in **one** message and then stop: the sample result, the **actual cost per
account** read from this workspace (four enrichments + one scoring call + one write, with the per-result
hiring caveat priced at the cap), the count of in-scope accounts currently in the audience so the total
is a real number and not a guess, exactly what will be written and where, and the ask. On yes, run the
first live batch (e.g. the sample's accounts, written for real), report actual spend against the
estimate, then enable the standing trigger so new accounts are scored as they enter. **Re-read the
balance after the batch and report the real figure** — an estimate never reconciled is how an overrun
goes unnoticed. From then on it bills per account entering the audience; say that plainly, because a
standing trigger is a standing cost.

## What this skill does not claim

- It does not measure whether an account is a good fit — it scores the *evidence available*, and the
  most fit-predictive signal (the tech stack) is empty on most accounts, so a low score often means thin
  data, not a bad account. The rationale says which dimensions were unobserved; read it before acting.
- The tier cut-offs, usage-pressure thresholds and dimension weights are the source workflow's values
  carried as editable defaults; none of them is validated against an outcome, and nothing re-checks a
  cut-off the installer re-tunes.
- Per-account credit and token cost are not quoted here — they are the installer's own workspace prices,
  read at build time. The one structural cost fact carried is that the hiring action can bill per result.
- `has_timing_signal` is produced by the scoring model from the evidence it was given; if an enrichment
  silently returned empty, a real timing signal can be missed and the account under-tiered.

## What good looks like

- A rep can answer "why is this account Tier 1?" from the record alone — score, the four dimension
  scores in the rationale, the tier reason, and the why-now — with no black box.
- Re-tuning a cut-off is a one-line change to a code node, not a rebuild.
- A ≥75 account with nothing happening reads as Tier 2 with "nurture until a signal appears," not as a
  missed Tier 1 — and the installer can see it was fit, not the pipeline, that held it back.
- The common mistake this avoids: letting the scoring model also do the tiering and the arithmetic, so
  the cut drifts run to run and the total does not equal its parts.

## Rules

- MUST keep the tier cut and the total in a code node; the model produces dimension scores and prose,
  never the tier and never the sum.
- MUST set `endRunOnNoMatch: true` on the in-scope gate so out-of-scope accounts end before any spend.
- MUST resolve every action by its `(packageId, actionKey)` pair against the installed catalogue, and
  price the hiring action at its per-result cap.
- MUST gate the build behind write-approval and the first live run behind one spend-and-write approval
  that names the cost and the write together; reconcile actual spend afterwards.
- MUST score prospects and expansion candidates on their own rubric, chosen deterministically by plan
  before any judgment runs.
- NEVER contact anyone, delete or blank a field, or move account data off-platform.
- NEVER score a dimension whose input was unobserved as zero — leave it out and say so in the rationale.

## Worked example

A team selling a GTM data platform points the workflow at their "Target Accounts" audience and maps
domain, company LinkedIn URL, plan, acquisition type, and a workspace-count usage field. In-scope rule:
prospects, plus customers on the "Pro" plan. The build creates ten nodes; the dry run on eight accounts
shows the tech-stack lookup empty on seven of them (expected) and the tracks resolving correctly. The go-
live gate reports per-account cost at the hiring cap and 412 in-scope accounts in the audience; the team
approves. First batch: a prospect running a full outbound stack with three RevOps roles posted lands
**New Business · 82 · Tier 1 · Priority** (live hiring signal); a Pro customer on 24 workspaces lands
**Expansion · 88 · Tier 1 · Priority** (severe usage pressure); a strong-fit prospect with a stale last-
signal lands **New Business · 77 · Tier 2** — fit without timing. The standing trigger is enabled;
new accounts entering the audience are scored automatically from then on.
