---
name: icp-outbound-campaign
description: |
  Build an outbound campaign from your ideal customer profile: interview you for the ICP (who
  the buyer is, which companies, where, how many), turn it into a Clay people search you confirm
  in plain words, widen in declared tiers only if the strict ICP cannot reach your target, strip
  titles that match but never buy, keep a set number of leads per company, find verified work
  emails, optionally enrich any extra data point you want to personalize on (recent posts,
  company news, a funding round, anything Clay can find) using the best enrichment for it, save
  the kept leads to Clay Audiences as their own segment, and draft a two-email (optionally three) Clay Sequencer
  campaign around your offer. Use whenever someone asks: find leads in my ICP, build an outbound
  campaign, get me 200 VPs of Sales with emails, find CISOs to email, build a prospect list and a
  sequence, personalize outbound on recent funding or posts, or turn my ICP into a lead list. Do
  NOT use it to score or tier a list you already have, to enrich an existing CRM export, to find
  companies rather than people, to send or launch a campaign, or to write replies to people who
  answered.
category: build-lists
personas: [sales-development, revops]
mechanism: functions
touches: writes-records
keywords: [cold-email, sequencer]
---

# ICP outbound campaign (ask for the ICP, tier the search, then fill in order)

The insight: **the strict ICP on the source run found 141 people for a target of 200, so this
skill widens in declared tiers and fills them in order rather than loosening the definition.** The
source run targeted CISOs and heads of security at fast-growing software companies in the US and
Canada on 2026-09-28:

| Tier | Definition | People found |
|---|---|---:|
| 1 | persona titles, core industry, 51–5,000 employees, 20%+ 12-month headcount growth | **141** |
| 2 | same titles and growth, adjacent industries | 52 more (193) |
| 3 | same titles, industries and growth, 11–50 and 5,001–10,000 employees | 99 more (292) |

The strict definition alone could not reach 200 — and it lost more on the way: 12 titles that
matched the search but do not buy (vendor "Field" titles, deputies, program managers), 2 whose
company resolved to a junk domain, 24 with no verified email, and 24 who were a second leader at a
company already on the list. The run kept 200 of 230 eligible, filled tier 1 first (116), then
tier 2 (38), then tier 3 (46). How big any other ICP's pool is was not measured; that is why the
skill counts tier 1 before promising a number.

Four more things follow, and the first three bit the run that produced this skill.

**The ICP is the installer's, and the workspace may hold the wrong one.** The source workspace's
saved business context described a different company than the seller. An ICP read from context and
used silently would have targeted someone else's buyers. So this skill asks for the ICP every time,
and shows any saved ICP only as a starting point to confirm.

**Title similarity matching over-reaches in a predictable direction.** A title search expands into
related titles, and some of them never own a budget — on the source run, asking for "CISO" also
returned Field CISOs at vendors, deputies, fractional CISOs and advisors. Every persona has its own
version, so the skill shows the titles that came back and asks which to drop before anything paid
runs.

**A Sequencer follow-up is not a reply.** The sequence stops for a lead the moment they reply, so the
second step only ever reaches people who did not answer. Anything meant for people who said yes is
a message a human sends from the thread, not a sequence step.

**A personalization data point is only worth paying for if it reaches the email.** The source run
personalized on nothing beyond the fact the search filtered on, so it needed no extra enrichment. An
extra data point — a recent post, a funding round, a news story — costs a lookup per lead, returns
nothing for some of them, and can be wrong about the company. So the skill asks whether the
installer wants one, picks the enrichment by testing it on real rows, and writes copy that still
reads naturally for the leads where it came back empty.

## Declared inputs

**Nothing here ships with a value.** Each one is the installer's, not the author's: ask for it,
never substitute a plausible default, and if an answer does not exist say which step becomes
unavailable rather than guessing. Where a default IS defensible it is named below, and using it
means saying so in the output.

| Input | What the installer supplies | If it is missing |
|---|---|---|
| **Buyer persona** | the job titles that count as the buyer, and the seniority levels | no default — Step 3 has nothing to search for |
| **Company profile** | industries, employee size range, and any company signal that defines fit (headcount growth, hiring for a role, technology used, headquarters location) | no default — ask. A search with titles and no company profile is too broad to send to |
| **Geography** | where the people must be based | no default — ask |
| **Target count** | how many leads they want in the finished segment | the author recommends 250–300 for a first test campaign; recommend it, let the installer decide, and never pick a number for them |
| **Exclusions** | companies or segments never to contact (customers, competitors, an existing Audiences segment) | everyone already in the workspace's Audiences is excluded regardless; ask for anything beyond that |
| **Title exclusions** | titles that match the search but never buy | built from the search results in Step 4 and confirmed by the installer; never assumed |
| **Widening order** | which ICP criterion to relax first if tier 1 falls short | asked in Step 3 only if tier 1 falls short; never widen silently |
| **Leads per company** | how many people one company may contribute | the source run used 1, a run-time default rather than a stated rule; say it is borrowed |
| **Personalization data points** | any extra fact per lead or per company they want the emails to use, and how recent it must be | none is a complete answer — the campaign personalizes only on name, company and the ICP fact the search filtered on |
| **Audiences fields for data points** | the contact fields that will hold each extra data point | read the Audiences field list and propose a match; if none fits, ask whether to create one (a write, approved in Step 6) |
| **Seller and offer** | who is sending, what is offered, and what the recipient has to give to accept it (a call, a form, access) | no default — Step 9 cannot write copy |
| **Product facts and proof** | one or two sentences on what the product does, and any customer result the installer is cleared to cite | copy runs with no proof line. Never invent a customer or a number |
| **Lead-source tag** | the value written to the lead-source field so this batch forms its own segment | no default — without it Step 8 cannot build a segment that holds only this run |
| **Lead-source field** | the Audiences contact field that holds the tag | read the Audiences field list, show the match, ask them to confirm; if none exists, stop and ask them to create one in the Clay app |
| **Save-to-Audiences workflow** | an existing workflow that takes a CSV and upserts contacts, or permission to build one | Step 8 builds one after the Step 6 approval |
| **Follow-up delay** | days between the first email and the follow-up | the author recommends 3–4 days; if they have no view use 3 and say it is the author's |
| **Third email** | whether to add a third email, and its delay | two emails is the default. The author's experience is that anything after email 2 has a very low chance of a response; if they want a third, it goes 7 or more days after email 2, and say so |

**If an answer sheet is present beside this skill, load it and ask only for what it does not
cover.** A partial sheet is normal; a value it is missing gets asked for on its own rather than
restarting the interview. Say which values came from the sheet before using them. If there is no
sheet, say nothing about sheets.

## What this skill touches

- **Reads** — Clay's people search, the workspace's Audiences segments and fields, existing campaigns, saved business context, the routine list and action catalogue, and the declared costs of the enrichments it chooses.
- **Writes** — contact records in Audiences (name, title, company, location, work email, profile URL, lead-source tag, and any approved personalization fields), any new Audiences field the installer approved for a data point, one new Audiences segment, one new draft campaign with its audience and two sequence steps (three if the installer asks), and — only if none exists — one two-node save-to-Audiences workflow with a traceability line in its description.
- **Never** — launches, sends, pauses or deletes a campaign; sends a test email; deletes or clears any record or field; overwrites a populated field with a blank; emails anyone already in the workspace's Audiences; sends lead data to a service outside Clay.
- **Halts** — Step 1 other, Step 3 sample-review, Step 5 sample-review, Step 6 spend-approval, Step 6 write-approval.

## Step 0 — Check the platform works, and say what this run touches

Run `clay whoami`. It must return a user and a workspace; name the workspace out loud. If it fails,
say which component is wrong and the one command that fixes it (`clay login`), and stop. Do not
install, upgrade or fetch anything to repair the platform.

Then say, before anything else: *"I'll ask you about your ICP first, then search Clay for people who
match, find their work emails, add any extra details you want to personalize on, save the kept leads
into your Audiences as a new segment, and create a draft campaign. Nothing is sent or launched — you
do that in the Campaigns UI."*

Do not start a step before the steps above it have their answers. If a declared input is missing,
ask for it — never assume a default and continue.

## Step 1 — Interview for the ICP (do not guess)

**The ICP is the installer's judgment about their own market. Ask for it; never infer it from the
workspace, the seller's website, or an earlier campaign.** One question per message, in this order,
each with a one-line example so the installer knows the level of detail wanted:

1. **Who is the buyer?** *"Which job titles, and how senior — e.g. VP or Head of Sales, Director and
   above."*
2. **Which companies?** *"Industry, employee size range, and anything that makes a company a fit now
   — growing headcount, hiring for a role, using a technology, headquartered somewhere."*
3. **Where are the people based?** *"Countries or regions."*
4. **How many leads do you want?** *"For a first test campaign, 250–300 leads is a good size — big
   enough to read a reply rate, small enough to fix the copy before scaling."*
5. **Who must never be contacted?** *"Customers, competitors, an existing list."*

Before question 1, run `clay campaigns options business-context`. If it holds an ideal customer
profile or buyer personas, **show it and ask whether it applies to this campaign** — it may describe
a different company or an old ICP. Use it only on a yes, and only as the starting point for the
questions above.

If an answer is vague ("fast-growing", "mid-market", "tech"), ask once for the number or list behind
it. If they have no view, offer the closest searchable default from the live query reference, name
it, and record it as borrowed — for example, the reference maps vague growth wording to more than 20%
headcount growth over 12 months.

Then **play the ICP back in one short paragraph** — the titles, seniority, company profile, geography,
exclusions and target — and ask *"is that your ICP?"*. Stop until they say yes. This is the Step 1
halt.

## Step 2 — Look at what the workspace already has (free)

1. `clay audiences list --entity-type people`, following `cursor` to the end. Name any segment that
   looks like an earlier run for the same ICP.
2. `clay campaigns list --search` with the seller's name. Name any empty draft that looks like an
   earlier attempt.
3. If either exists, ask once whether to build fresh (excluding everyone already in Audiences) or to
   top up the earlier segment. Recommend fresh, excluding everyone.

## Step 3 — Turn the ICP into a search, confirm it, count tier 1

Fetch the live query reference first and write it to a file; never restate it from memory:

```
clay searches query-mode reference | jq -r '.reference' > ./clay-search-reference.md
```

Read its grammar, operators, people guardrails, the people and experience field catalogues, and any
topic section the ICP needs (location, company size, dates and growth, products and services). Map
each ICP criterion to a field. **Every enum value must come from the reference's own list** — an
industry or size band that is not listed fails validation.

The shape, with every value from the confirmed ICP:

```
select from people
where experiences.any(is_current = true
    and job_title is_similar_to (<persona titles>)
    and seniority in (<seniority levels>)
    and company.industry in (<industries>)
    and company.company_size in (<size bands>)
    and <company signal, e.g. company.employee_growth_12mo > 1.2>)
  and location_country in (<geography>)
  and clay.exclude_people_identifiers(@audience_segment("ALL"))
```

Keep every company condition inside one `experiences.any(...)`. `ALL` excludes every contact already
in the workspace's Audiences; add one `clay.exclude_people_identifiers(@audience_segment("<id>"))`
per extra exclusion segment the installer named, resolved from `clay audiences list`.

**If an ICP criterion has no search field, say so plainly** — name it, say what the search will use
instead (the closest field, or nothing), and offer to check it per lead as a data point in Step 5.
Never drop it silently.

**Before creating anything, read the search back in plain words** — *"people titled VP or Head of
Sales, Director and above, at software companies with 201–1,000 employees that grew headcount more
than 20% in the last year, based in the UK, not already in your Audiences"* — and ask them to
confirm. Then create with `clay searches query-mode create --query` and page with
`clay searches query-mode run <searchId> --limit 100` while `hasMore` is true. Keep each tier's rows
in its own file — **never merge with a shell glob that can pick up unrelated JSON files**; that
happened on the source run and polluted the merge.

After each `run` that returns `periodQuota`, check that the planned pull leaves at least 15% of
`limit`; if not, stop and ask.

**Show the first page as a sample** — the 10 most common titles and a handful of companies — and ask
whether these look like their buyers. This is the Step 3 halt, and it is where a wrong industry or an
over-broad title shows up before anything is spent.

**Widen only if tier 1 cannot reach the target.** Aim for roughly 1.4× the target in candidates,
because the source run lost about 30% between search and final list. If tier 1 falls short, say how
many it found and ask which criterion to relax first — an adjacent industry, a wider size band, a
looser signal, a neighbouring geography. Each widening is its own tier and its own search; label
every row with its tier. Dedupe across tiers on `clay_profile_id`.

Rows carry `clay_profile_id`, `name`, `first_name`, `last_name`, `linkedin_url`, `location.name` and
`matched_experiences[0]` with `title` and `company`. On the source run query mode returned
`linkedin_url`; if a row lacks it, the email step still runs on name, domain and company.

## Step 4 — Free cleanup before anything paid

1. **Build the title exclusions with the installer.** List the distinct titles across all tiers,
   grouped, and propose the ones that look like non-buyers — vendor-facing "Field" titles, deputies,
   interim or fractional roles, advisors, consultants, interns, analysts, board seats, assistants,
   and roles from a different function that share a keyword. Ask them to confirm or edit the list.
2. Drop rows whose `matched_experiences[0].title` is empty or matches the confirmed exclusions
   (case-insensitive, whole-phrase).
3. Rank what remains: tier ascending, then seniority — the most senior title first.
4. List unique company names. This is the domain step's input count.

Say the counts: found, removed by title, remaining, unique companies.

## Step 5 — Ask for personalization data points, and choose the enrichment for each

**Ask one question, with examples, and accept "none" as a complete answer:**

> *"Beyond their name, company and the ICP fact we searched on, is there anything else you'd like the
> emails to reference? Clay can find things like a person's recent LinkedIn posts, a company's recent
> news, or its latest funding round — or something else specific to your pitch. Name as many as you
> like, or say none."*

If they say none, skip to Step 6. For each data point they name, do the following. Do not name a
provider or function to the installer until you have checked it exists in their workspace.

1. **Pin the definition before looking for a source.** Ask only what the data point leaves open and
   the copy needs: is it about the **person** or the **company**, and **how recent** must it be
   (e.g. posts from the last 30 days, a round announced in the last 12 months)? A time-bound fact with
   no window is not usable — an undated or out-of-window result counts as not found.
2. **Find the candidates, managed routines first.** Run `clay routines list` and follow `cursor` to the
   end. Match on each routine's **input schema** (`clay routines get <id>`), not its name — a routine
   whose inputs the kept rows can supply (profile URL, full name, company domain, company name).
   Prefer `source: managed`, then custom routines. Only if none fits, search the action catalogue with
   `clay workflows actions --help` to find the listing and schema commands, and read the action's real
   input schema. Never carry a function name or price in from memory; read them from this workspace.
3. **Compare the candidates on four things, then pick one:**
   - **Inputs** — can every kept row supply them? A candidate needing a profile URL when half the rows
     lack one covers only half.
   - **Cost** — `estimatedCreditCost` from `clay routines get` (the list call omits it), or the
     action's own cost and `paymentType`. Read parameter descriptions for per-result pricing: a step
     that bills per item returned cannot be totalled before it runs, so give its per-item price and set
     a cap on items per lead.
   - **Output** — does it return the field the copy needs, with a date where the definition needs one?
   - **Scope** — a person-level fact runs once per lead; a company-level fact runs once per **unique
     company**, which is cheaper and must be joined back to each lead.
   Prefer the candidate that covers the most rows with the needed field at the lowest cost. If none
   can find the data point, say so plainly and drop it — never approximate it with an AI guess.
4. **Test the chosen enrichment on the first 10 ranked leads** and show, per lead: the value found, its
   date, and whether it is about the right person or company. **Check the entity**: news and posts can
   name a similarly named company or a different person — a result that is not clearly about this
   lead's company counts as not found. If fewer than half return a usable value, or the entity check
   fails often, say so and offer the next candidate or dropping the data point.
5. **Choose where it lands.** Read the Audiences field list (`clay audiences fields --help` for the
   commands) and propose an existing contact field for each data point, or a new one to create. For a
   long raw result (a post body, an article), keep a short extract — one or two sentences plus the
   date and source link — so the field stays readable and the copy step is grounded.

Then play back each data point in one line: *what it is, which enrichment, per-lead or per-company,
test hit rate, cost, and the field it lands in.* This is the Step 5 halt; wait for a yes before the
gate.

## Step 6 — Small batch, then ONE gate: the batch, the cost, the writes, the ask

Read declared costs by id — the list call omits them:

```
clay routines list                   # find the managed company-domain and work-email functions by input schema
clay routines get <routine id>       # estimatedCreditCost.perRun
```

On the source run the managed **Company Domain** function declared 1 credit per run and **Work
Email** declared 3 per run. Read them again; the installer's plan may differ.

Run the domain and email lookups on **10 rows** first (the inline form, `--input` with up to 100
items), and show the 10 results: company, domain found, email found or not. The Step 5 tests already
cover any personalization enrichment.

Then one message, and stop:

- the batch result, including any domain that is obviously wrong (hosting previews such as
  `vercel.app`, `netlify`, `github.io`, `herokuapp`, `wixsite`, `notion.site`, or a social-network domain);
- the full cost, computed and itemized: unique companies × domain cost + remaining people × email
  cost + each personalization enrichment × its row count (per lead or per unique company). State it as
  an upper bound, because the email function says it charges only when it finds one and that was not
  verified; for a per-item-priced enrichment, give the per-item price and the cap instead of a total;
- **the writes, in the word:** *"this writes N contact records into your Audiences, including the
  fields …, creates the new fields … (if any), creates a segment named …, creates a draft campaign
  named …, and — if you have no save-to-Audiences workflow — builds one. Those are mutations, not
  reads."*;
- the ask.

This single gate is both the spend approval and the write approval.

## Step 7 — Find domains, work emails, and personalization data

1. **Company domain.** Bulk-run the company-domain function, one row per unique company, input
   `Company Name`. The bulk result is a JSONL file at `resultUrl` from
   `clay routines runs get <runId> --bulk`; each line is `{"id", "status", "result": {"Domain": ...}}`.
   Drop the junk domains listed in Step 6 — the person is skipped, not guessed.
2. **Work email.** Bulk-run the work-email function per person: `Full Name`, `Company Domain`,
   `Company Name`, and `Social Profile URL` from `linkedin_url` when present. Read
   `result["Work Email"]`. An empty `result: {}` means no verified email — skip the person, never guess
   a pattern.
3. **Personalization data.** Run each approved enrichment only on leads that have a verified email —
   per lead or per unique company, as chosen in Step 5. Apply the same window and entity checks as the
   test. A lead with no usable value keeps an empty field; that is not a reason to drop them.
4. Wait with `clay routines runs get <runId> --bulk --wait 600`. Report found and not found for each.

## Step 8 — Select, save to Audiences, build the segment

1. From people with an email, walk the ranked list and keep up to the declared leads-per-company,
   deduping on email, until the target count.
2. Write a CSV with `full_name, first_name, last_name, title, company, location, work_email,
   linkedin_url, lead_source`, plus one column per approved data point.
3. **Create any approved new Audiences fields** for the data points, confirming the command on the
   installed CLI with `clay audiences fields --help`.
4. **Find the save-to-Audiences workflow** — `clay workflows list`, then `clay workflows graph get <id>`
   for a CSV-upload trigger feeding an `upsert-audiences-record` tool node on `CONTACT`. If one exists,
   read the node with `clay workflows nodes get` and confirm its trigger fields match the CSV headers,
   including the data-point columns. If it does not map them, say so; updating an existing workflow's
   mapping is a write the installer approves here, never a silent edit.
5. **If none exists, build one** (approved in Step 6). Confirm the command forms on the installed CLI
   first — `clay workflows --help`, `clay workflows nodes --help`, `clay workflows triggers --help`,
   `clay workflows actions --help` — never trust a form written here. Two nodes, one edge:
   - a `csv_upload` trigger whose fields are the CSV headers;
   - a tool node running `upsert-audiences-record`: entity type `CONTACT`; lookup on email and
     profile URL; record fields name, first name, last name, title, job title, company, email, profile
     URL, location, the installer's lead-source field, and each data-point field; remove-null-values
     on, so a blank never overwrites a populated field.

   Tool-node outputs are read at `$.result`, and a tool node does not echo its inputs. Say out loud:
   *"I'm writing a line into the workflow's description so this can be traced back to the listing."*
   Apply the marker only when this installed copy carries `marketplace_slug` and
   `marketplace_revision`; the line is `Sourced from marketplace skill: <slug>@<revision>`. Read the
   description first: null → write a description then the marker; a description with no marker →
   append; this same marker → write nothing; any other marker → stop and report a conflict. If the
   identity fields are absent, skip the marker and say attribution is unavailable. Read it back.
6. Upload and run: `clay workflows triggers csv upload <triggerId> --file <csv>`, then
   `clay workflows triggers csv run <triggerId>`.
7. Create the segment with `clay audiences create --entity-type people`, filtering on the lead-source
   field equal to the tag AND email not empty. Copy the filter's `key` and `dataPath` from an existing
   segment's `clay audiences get` output rather than guessing them. Name the segment after the ICP and
   the count.
8. Verify: `clay audiences records search-count --entity-type people --audience-id <id>` equals the
   CSV row count. If it does not, say how many landed and stop.

## Step 9 — Draft the campaign, never launch it

1. `clay campaigns create --name "<seller> — <offer> — <ICP label> (<date>)"`.
2. `clay campaigns update <id> --input '{"leadBaseSegmentId":"<segment id>"}'`.
3. `clay campaigns audience <id>` — use only fields by their exact ids. A data-point field will not be
   `reliablyPopulated` when some leads lack it; that is expected and is why it gets a fallback.
4. `clay campaigns context resolve <id>`. **If the attached business context describes a different
   company than the seller, say so** and do not let AI snippets draw on it.
5. Ask the copy inputs now: seller, offer and what accepting it requires, product facts, proof, and
   whether they want a third email.
6. **Two habits carry most of the weight, and every email follows both** (the author's practice):
   - **Keep the offer specific to the person receiving it.** Tie it to their role, their company, and
     the fact the search or a data point established — never an offer that would read the same to
     anyone.
   - **Be straightforward about who you are and what you want.** Name the sender and company early,
     say plainly what is being offered and what you are asking for, and do not disguise a sales email
     as something else.
7. Write the steps with `clay campaigns sequence edit` (read `--help` for the op schema):
   - **Initial email**, new thread. The reason to write is the ICP criterion the search actually
     filtered on (their growth, their hiring, their stack) — never a claim the data does not support.
     Then the offer, what it gives them, what it asks of them, and a yes/no ask. Keep "free" out of the
     subject.
   - **First follow-up**, reply in thread 3–4 days later (the declared delay). It reaches only
     non-responders: more on what the offer delivers, where the product fits, the proof line if
     cleared, a one-word reply ask.
   - **Second follow-up — only if the installer asked for one**, 7 or more days after the first
     follow-up. Tell them once that response odds this late are very low. Keep it short, give one
     new reason to reply, and make it easy to say no.
   Add spintax to several sentences, and avoid spam-trigger phrases such as "no cost".
8. **Use each data point through one short AI snippet**, placed where it replaces the generic reason
   to write — usually the opening line of the initial email. The brief names the data-point field as a
   nested lead token **with a fallback**, so a lead with no value is still enrolled:
   `{{ai:|Opener|Write one sentence referencing this recent item: {{lead:<fieldId>|<label>|fallback=none}}. If it is none, write a one-sentence opener from the ICP fact instead, without implying research.}}`
   The snippet may only restate what the field says; it must not infer opinions, results or intent
   the field does not contain.
9. Review every email as the recipient — a busy member of the ICP triaging the inbox — and fix only
   material objections. Check both habits first: would this offer read the same to anyone, and is it
   clear within two sentences who is writing and what they want?
10. `clay campaigns sequence spam-check`, then `clay campaigns variants preview-sequence` on one lead
   that has each data point and one that does not. If a preview lead's company does not look like the
   ICP, say so.

No sender accounts are set, nothing is launched, and no test email is sent.

## Step 10 — Deliver

Report the confirmed ICP in one line, the segment name and count, each data point with its hit rate,
the campaign name, the final copy with readable placeholders, the coverage line, any ICP criterion
the search could not express, and three things the installer does next: add sender accounts and
launch in the Campaigns UI; confirm any proof line is cleared to cite; and reply by hand to anyone who
says yes, because the sequence stops at their reply.

At delivery, offer: *"Want me to save your ICP and settings to a file alongside this? It isn't part of
the skill — it's a note of what you told me: your titles, company profile, geography, exclusions,
data points and offer. Next time you won't re-answer these, and a teammate who has it can run this
without knowing your setup. It stays with you, is never submitted or published, and holds no
passwords or keys."*

## Representative output

### Confirmed ICP

People titled VP or Head of Sales, Director and above, at software companies with 201–1,000
employees that grew headcount more than 20% in the last year, based in the UK and Ireland, excluding
current customers and everyone already in Audiences. Target: 150 leads, one per company.

### Personalization data points

| Data point | About | Window | Enrichment chosen | Test hit rate | Final hit rate | Field |
|---|---|---|---|---|---|---|
| Latest funding round | company | last 12 months | managed company funding routine, once per company | 4 of 10 | 61 of 150 | Latest funding |
| Recent LinkedIn post | person | last 30 days | profile-posts action, capped at 3 posts per lead | 3 of 10 — below half | dropped by the installer | — |

### Lead segment summary

| Group | Leads | Share | Definition |
|---|---:|---:|---|
| Tier 1 — confirmed ICP | 98 | 65% | the ICP exactly as confirmed |
| Tier 2 — size band widened | 52 | 35% | same, 1,001–5,000 employees, widened on the installer's say-so |
| Not kept — no verified email | 19 | — | skipped, never guessed |

Titles kept: 61 VP of Sales · 47 Head of Sales · 42 Director of Sales.

### Initial email, as one lead would receive it

Subject: Pipeline review for Northwind

> Hi Dana,
>
> Congrats on Northwind's Series B in March — a round like that usually means the sales team grows
> faster than the pipeline data behind it.
>
> I'm with Contoso. I'd like to offer a pipeline review for Northwind, on us: a 30-minute call where
> we look at your last two quarters of opportunities and show where deals stalled and why.
>
> There's nothing to buy, and you keep the findings either way.
>
> Want me to set one up?
>
> Sam

### Coverage line

212 found across two tiers · 9 removed by title · 169 with a verified email · 150 kept after one
per company, filled tier 1 first · funding found for 61 of 150 · 0 already in Audiences · draft
campaign, not launched.

## What this skill does not claim

- The widening pattern was measured on one ICP (security leaders); how often a strict ICP falls short of its target for other personas was not measured.
- The 1.4× over-sourcing ratio comes from one run's losses and will differ by persona and market.
- The personalization step was never run end to end; no hit rate, cost or accuracy for any data point was measured, and the figures in the representative output are invented.
- Choosing an enrichment on a 10-row test is a small sample; the full-run hit rate can differ.
- News and post results can be about a different company or person with a similar name; the entity check reduces this and does not eliminate it.
- No reply rate, meeting rate or deliverability outcome was ever measured — the source campaign had not launched when this skill was written.
- The credit costs are the functions' declared estimates on one workspace; actual spend was not reconciled against them.
- Whether the work-email function bills a miss was not verified, so the cost at the gate is an upper bound.
- Some ICP criteria have no search field; the skill names them and approximates or skips them rather than claiming to have filtered on them.
- The proposed title exclusions are a starting list from one run; the installer confirms them every time.
- Company-name-to-domain lookup can return a wrong company for a common name; only obvious junk is filtered.
- One lead per company and the source run's tier definitions were run-time defaults, not argued for.
- The 250–300 test size, the 3–4 day and 7-day spacing, the low response odds after email 2, and the two copy habits are the creator's practice; this skill did not measure them.
- The broader reading — that for senior personas the list, not the copy, is generally the constraint — was not confirmed by the creator; one run found it true once.
- The logic comes from the creator's stated intent and one live run, not from a table or workflow that already encoded it.

## What good looks like

A good run starts with an ICP the installer confirmed in their own words and a search they approved
in plain words, and ends with a segment whose count equals the CSV exactly, a coverage line that
accounts for every person found — removed by title, no email, over the per-company limit, or kept —
and a draft campaign whose preview reads naturally for a real lead who looks like the ICP. Tier 1
fills first, and any widening was asked for and appears as its own row. Every personalization data
point shows the enrichment chosen, why, its test and final hit rates, and a preview for a lead
without it that still reads well. A thin run says so: *"your ICP found 60; you asked for 200; I
stopped before widening"*, or *"posts came back for 3 of 10, so I dropped them."* A bad run looks
finished and hides one of these — an ICP the agent inferred, a criterion silently dropped from the
search, a segment count that does not match, a tier widened without asking, a non-buyer title in the
list, a guessed email, an opener about the wrong company, a data point with no fallback that drops
leads from enrollment, or a follow-up written as if the person had replied.

## Rules

- **NEVER** infer the ICP. Ask for it, play it back, and wait for a yes.
- **NEVER** use saved business context as the ICP without showing it and getting a yes.
- **NEVER** drop an ICP criterion silently; name any the search cannot express.
- **NEVER** pick a personalization enrichment from memory. Read what the workspace has, compare on inputs, cost, output and scope, and test on 10 leads.
- **NEVER** let AI generate a data point the enrichment did not return; a missing value uses the fallback.
- **NEVER** launch, send, pause or delete a campaign, or send a test email. The installer launches in the Campaigns UI.
- **NEVER** guess an email address or a domain. No verified result means the person is skipped.
- **NEVER** widen past tier 1 without asking, and never mix tiers without labelling them.
- **NEVER** email anyone already in the workspace's Audiences; the search excludes them.
- **NEVER** cite a customer result the installer has not confirmed they can use.
- **NEVER** send an offer that would read the same to anyone, or hide who is writing and what they want.
- **NEVER** schedule the first follow-up outside 3–4 days, or a third email sooner than 7 days after the second, without the installer choosing that.
- **NEVER** clear or blank a populated field; the upsert removes null values.
- **MUST** run the free title cleanup and per-company pass before any paid step.
- **MUST** hold one gate before the paid and write steps, carrying the batch, every cost and every write.
- **MUST** verify the segment count against the CSV before creating the campaign.

## Worked example

A GTM ops lead at a compliance-automation vendor asked for 200 leads in their ICP: CISOs and heads of
security at rapidly growing software companies, then a two-email campaign offering a free security
assessment. The saved business context in the workspace described a different company, so it was
not used. Asked where the leads should be based, they chose the US and Canada; "rapidly growing"
had no number behind it, so the reference's default of more than 20% 12-month headcount growth was
applied and recorded as borrowed. The workspace already held two earlier lists and two empty drafts
from the same vendor; they chose a fresh build excluding everyone already in Audiences. Tier 1
returned 141, so tiers 2 and 3 were added (292 total). Title cleanup removed 12 — Field CISOs,
deputies, program managers — leaving 280 across 252 companies. No extra personalization data point
was used on this run; the copy personalized on first name, company and the growth the search
filtered on. The domain lookup returned 250 usable domains (two junk hosting domains dropped); the
email lookup found 254 of 278. One per company left 230, and the first 200 in tier order were saved
to Audiences through a CSV-to-upsert workflow and gathered into a new segment of exactly 200. A draft
campaign was created on that segment with a three-day follow-up. The first spam check scored 56
("fair": no spintax, "no cost" flagged); after adding spintax and changing "no cost" to "on us" it
scored 100. The preview lead worked at a security vendor, which was flagged. Nothing was launched.
