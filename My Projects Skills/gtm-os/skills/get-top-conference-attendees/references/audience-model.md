# What lands in Audiences, and why each column has the type it has

## The shape

One **person** record per attendee, and — when their company has a domain — one **company**
record with the person linked to it. Not a table. Records, with real fields, so the list can
be filtered, segmented and re-used after the conference is over.

## People

Written into the fields every workspace already has: `name`, `first_name`, `last_name`,
`title`, `email`, `linkedin_url`, `phone`. Plus these, adopted by display name or created:

| Column | Type | Holds |
|---|---|---|
| Conference | text | the event's name, as the lookup verified it |
| Conference start | date | first day, ISO |
| Conference location | text | city as given |
| Conference campaign id | text | which run produced this record |
| Attendee record id | text | the service's own id for this person |
| Attendee tier | text | S / A / B / C / F — **read from the flat response format, not the dossier** |
| Attendee score | number | the rubric score |
| Attendee rank | number | position in the ranked list |
| Attendance confidence | text | confirmed, or likely |
| Attendance evidence | text | why they are believed to be going |
| Attendance source | text | the page that evidence came from |
| Dossier state | text | enriched / ranked_only / queued / failed / unranked |
| Dossier headline | text | the one-line read on them |
| Dossier summary | text | the paragraph on the person |
| Their company | text | the paragraph on the company |
| Why they score | text | the rubric's own rationale |
| Buying signals | text | the list, joined |
| Conversation openers | text | the list, joined |
| Value prop | text | what to lead with |
| Dossier written at | date | when this skill wrote the record |

**Tier is the one column that cannot be read from the same response as the rest.** Measured
against a live campaign: no contact in the rich format carries a tier under any key, while the
flat projection has one for every contact (S 17, A 15, B 18, C 73, F 21 across 144 people —
reconciling exactly with the campaign's own locked block). So both formats are read and merged
on identity. A client that reads only the documented one writes a permanently empty tier
column and reports success.

## Companies

`org_name` and `domain`, plus **Conference**, **Conference campaign id**, **Attending this
conference** (text, `yes`) and **Dossier written at**.

## Why the types are what they are

**`Attendee score` is the only number, and it is validated before it is sent.** A value the
field's declared type cannot parse is *accepted*: the write returns success, the value is
counted as updated, and it reads back verbatim on the record — and it matches no filter, ever.
Three of the four places you would look agree the value is there; only a filter disagrees. So
a score that arrives as a range or as prose is **dropped and named as dropped**, not written
invisibly.

**Nothing is a boolean, and "Attending this conference" is text holding `yes`.** A boolean
cannot be coverage-checked: `is_not_null` is the same query as `= true`, and `= false` returns
everything else *including every record the field was never set on*. No query separates
"explicitly false" from "never touched", so a fill rate read off a boolean is meaningless.
Text with explicit values keeps the difference.

**`Dossier state` is text with five values rather than a flag.** `enriched`, `ranked_only`,
`queued`, `failed`, `unranked` are five different facts, and only one of them means "we have
their dossier". Collapsing them into "has a dossier: no" makes every rate you would want —
what the free allowance actually covered, what failed, what is still running — impossible to
compute after the fact.

**Both date fields are real `date` columns.** An ISO string round-trips verbatim and the
relative-time operators work on it, so "everyone we researched in the last 30 days" is a saved
audience rather than a spreadsheet. The same string in a text field makes those operators
return a server error, and a stamp in the future falls outside `WithinLast` entirely.

**Every one of those columns is filled from a key the service actually returns, which is not
the key its documentation names.** Measured: the real dossier shares exactly ONE key
(`buying_signals`) with the published shape. `summary` is `contact_summary`, `openers` is
`conversation_openers`, `value_prop` is `value_prop_framing`, `company_history` is
`company_summary`, and `headline`, `fit_rationale`, `fit_score` and `attending_status` are in
no documentation at all. Every read here scans the real name first and the documented name
second, so a deployment using either shape works — but a client built from the documentation
alone writes a row of empty columns and reports success.

**Columns are adopted by display name, never created blindly.** Creating a field whose name is
already in use does not fail — it appends a suffix. A build that always creates leaves a
workspace holding "Attendee tier", "Attendee tier (2)", "Attendee tier (3)", each stamped by a
different run and none of them complete. When an adopted column turns out to have the wrong
type, the build says so and the driver drops values that would not survive it.

## The company domain has to be derived

Measured: this provider returns **no company domain on any contact**. The enrichment block
carries an email, a phone, a profile URL and an avatar — nothing else. Taken literally that
means no company record can ever be created and every attendee is written unlinked, which
makes half the graph decorative.

The work email is the evidence available, and for a work address it is strong: the domain on
a work address identifies the employer as well as any field would. So when nothing supplies a domain, one is
derived from the email — **except at a mailbox provider**, where it is refused outright. An
upsert keyed on `gmail.com` would merge every unrelated attendee into one fictional company,
which is worse than leaving them unlinked.

Live result: 5 of 5 attendees linked to the right company, verified by querying people whose
company's domain matches — one person at each of five distinct employer domains, and zero at a
control domain nothing wrote.

## An association is ADDED, never moved

Measured on a live workspace, and confirmed after a 45-second pause to rule out the query
index lagging: **writing a contact with a different `associations|accountId` does not move
them — it adds a second link.** The same person then satisfies a company traversal for *both*
companies, and a filter on the old one still returns them.

It happened here for a real reason worth keeping. A contact was first written with a company
domain derived from their work email, and later rewritten once the service returned the real
one — the employer had been acquired and the person's address still carried the old domain.
Both company records now exist under the same name, and the person is attached to each.

There is **no CLI path to remove an association** — audience records are read-only from the
CLI — so this cannot be cleaned up by the skill that caused it. Only the app can detach one.

What follows:

- A rewrite that changes an attendee's company **says so before it writes**. It is the one
  case where re-running is not free, and a silent second link is worse than a refusal.
- The first write is the one that sets the company cleanly. Loading a campaign before the
  company data is good, then correcting it, costs a duplicate link per corrected contact.
- "Which company does this person work at" has no single answer for a corrected contact, so
  do not build a segment that assumes it does.

## Matching, and the four writers it forces

Upsert match keys are fixed by the platform and cannot be extended — a custom field is never a
match key.

- **people**: `email`, `linkedin_url`, `phone`
- **companies**: `domain`, `linkedin_url`

This skill matches people on **LinkedIn URL first, email second**. For a conference attendee
the profile is the more stable identity, and two people at one company can share an inbox
alias while never sharing a profile.

Three constraints compound into the graph's shape, and none of them is optional:

1. **Every selected lookup field is required and rejects an empty string.** One writer cannot
   "use whichever key is present" — that is one writer per match key.
2. **A match key is checked for being that kind of thing, not merely for being non-empty.** A
   `linkedin_url` must be a linkedin.com URL; an email must parse. A near-miss fails with
   wording that reads as though the field were blank, so both are normalised before the write
   and a profile URL pointing at a company website is discarded rather than sent.
3. **A blank association writes no record at all** — not an unlinked one. So "has a company"
   and "has no company" cannot be one writer with an optional field. That doubles it again.

Two keys × linked and unlinked = four writers, plus one for the company. An attendee whose
company has no domain is written **unlinked**, never dropped. An attendee with neither a
LinkedIn URL nor an email cannot be matched on anything and is reported as unwritable — with
their name, so the person running it can decide.

## The blank that overwrites

`removeNullValues` drops nulls. It does **not** drop empty strings. A field sent as `""` is
counted as an update and **clears whatever the audience already held** — measured on a record
that lost an email address it already had.

Every writer here sends a fixed field list, so this is not a hypothetical: without a
correction, a second campaign touching a person the audience already knows would strip them
down to whatever that one campaign happened to know. So every blank is turned into a null
before any write sees it, in the graph's own intake step — belt and braces, so a caller who
sends an empty string is safe too.
