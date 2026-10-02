# Clay table build: Hiring Surge

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.
This file carries only what is specific to this signal.

⚠️ **Status: specification. This exact column set has never been built from scratch and graded.**
The 17/20 verdict covers the gate logic, not a from-scratch build.

**This playbook genuinely needs the browser path.** `Find Employee Headcount by Criteria` is a Clay
**table action** with no API surface anywhere — it does not appear in the workflow action catalog,
the CLI is read-only for tables, and the Public API is query-only. Building this table through the
Clay UI is the supported route, not a workaround for a missing API.

## Where the columns go

Main work table, **after email validation**. Never spend enrichment work on rows that will not
survive the email gate, even when the enrichment is free — free actions still consume table run
time, and run time is the binding constraint on this playbook.

## Integration check

| Provider | Native integration? | Use |
|---|---|---|
| Clay headcount | native **table action** | `Find Employee Headcount by Criteria`, FREE. This is the engine |
| The model | native AI column | `gpt-4o-mini` (see `SKILL.md` §6 — Clay cannot set reasoning effort) |
| Your sequencer | native `Add Lead to Campaign` | the native action with the connected account |
| Company enrichment | — | ⛔ **not used anywhere here.** ~8 credits for a URL you can approximate free |

## Columns

| Order | Column name | Type | Action | Input binding | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Clay `Normalize a Domain` | intake domain, `type: "bare"` | none | canonical first column |
| 1b | Company Linkedin Url | basic | formula | `({{Webhook}}?.company_linkedin_url) \|\| {{Webhook}}?.company_linkedin` | none | **FREE.** Populated on ~16.35% of rows |
| 2 | ~~Enrich Company~~ | — | — | — | — | ⛔ **Do not build this column.** 8 credits per company for a LinkedIn URL |
| 3 | Company Identifier | basic | formula | `{{Company Linkedin Url}} \|\| {{Normalize a Domain}}?.domain` | none | what every headcount column binds to. Free URL first, free bare domain for the rest |
| 4 | Sales Headcount Total | action | `Find Employee Headcount by Criteria` | `company_identifier = {{Company Identifier}}`, `job_functions = ["Sales"]`, `job_title_exact_keyword_match = true` | `!!{{Company Identifier}}` | FREE |
| 5 | Sales Hires 6mo | action | same | column 4's inputs **plus** `current_role_max_months_since_start_date = "6"` | `!!{{Company Identifier}}` | FREE. Counts ROLE STARTS, not hires |
| 6 | Sales Growth Pct | basic | formula | below | none | deterministic |
| 7 | Sales Surge Check | basic | formula | below | none | deterministic YES / NO |
| 8 | Marketing Headcount Total | action | same as 4 but `job_functions = ["Marketing and Public Relations"]` | | `!!{{Company Identifier}}` | FREE |
| 9 | Marketing Hires 6mo | action | column 8 plus the recency filter | | `!!{{Company Identifier}}` | FREE |
| 10 | Marketing Growth Pct | basic | formula | below | none | deterministic |
| 11 | Marketing Surge Check | basic | formula | below | none | deterministic YES / NO |
| 12 | Hiring Surge Dept | basic | formula | below | none | picks the winning department, applies the floors |
| 13 | Hiring Surge Hires | basic | formula | below | none | the number the copy uses |
| 14 | Hiring Surge Line | action | AI column, **`gpt-4o-mini`** | `{{Hiring Surge Dept}}`, `{{Hiring Surge Hires}}` | `{{Hiring Surge Dept}} !== ""` | **the only paid column** |
| 15 | Add Lead to Campaign | action | native sequencer action | see below | see the gate below | campaign stays in DRAFT |

⚠️ Only `"Sales"` and `"Marketing and Public Relations"` are confirmed values for `job_functions`.
**A wrong enum value does not error — it silently returns zero.** Test any new value on 10
known-good companies first, or use free-text `job_title_keywords`.

## Formulas

Columns 6, 7, 10 and 11 are known-good production formulas, not invented ones:

```
Sales Growth Pct        {{Sales Hires 6mo}}?.roleCount && {{Sales Headcount Total}}?.roleCount ? {{Sales Hires 6mo}}?.roleCount / ({{Sales Headcount Total}}?.roleCount - {{Sales Hires 6mo}}?.roleCount) * 100 : ""
Sales Surge Check       parseFloat({{Sales Growth Pct}}) > 15 || {{Sales Growth Pct}} === "Infinity" || {{Sales Hires 6mo}}?.roleCount > 6 ? "YES" : "NO"
Marketing Growth Pct    {{Marketing Hires 6mo}}?.roleCount && {{Marketing Headcount Total}}?.roleCount ? {{Marketing Hires 6mo}}?.roleCount / ({{Marketing Headcount Total}}?.roleCount - {{Marketing Hires 6mo}}?.roleCount) * 100 : ""
Marketing Surge Check   parseFloat({{Marketing Growth Pct}}) > 15 || {{Marketing Growth Pct}} === "Infinity" || {{Marketing Hires 6mo}}?.roleCount > 6 ? "YES" : "NO"
```

The percentage is deliberately `recent / (total - recent)` — new starts as a share of the
**pre-existing** team, not of the current team. A team that went from 4 to 8 reads as 100% growth,
which is what a human would say. When `total == recent` the division yields `Infinity`, which the
check treats as YES **on purpose**. Do not "fix" it.

Columns 12 and 13 add the floors:

```
Hiring Surge Dept    ({{Sales Hires 6mo}}?.roleCount >= 2 && {{Sales Headcount Total}}?.roleCount >= 4 && {{Sales Surge Check}} === "YES") ? "sales" : ({{Marketing Hires 6mo}}?.roleCount >= 2 && {{Marketing Headcount Total}}?.roleCount >= 4 && {{Marketing Surge Check}} === "YES") ? "marketing" : ""
Hiring Surge Hires   {{Hiring Surge Dept}} === "sales" ? {{Sales Hires 6mo}}?.roleCount : {{Hiring Surge Dept}} === "marketing" ? {{Marketing Hires 6mo}}?.roleCount : 0
```

The `>= 2` and `>= 4` floors are the fix for the false positives in `SKILL.md` §7. Without them the
raw percentage check fires on a 4-person marketing team that added 1 person, which is not a surge
and reads badly in an email. **These numbers are validated**: benched on 20 companies drawn blind
from a batch created *after* they were written — **17/20 (85%) with them, 10/20 (50%) without**.
They cut the gated segment from 14.6% to 5.2%, costing about two thirds of your list volume. That
trade is worth taking. **Do not loosen them to hit a volume target; source more rows.**

Note that `Hiring Surge Dept` also performs department de-duplication: a company that qualifies on
both departments gets `sales`, never both.

## One campaign or several

**Default: a single campaign with one `{{hiring_surge_line}}` variable.** One campaign to build,
one sequence to QA, one variable to lint.

The split shape — a campaign per department per region — stays fully supported. Reach for it when
the departments need genuinely different offers or different senders, not merely a different noun
in one sentence. If you split, you need mutual-exclusion formulas so a lead never lands in both
(`{{Marketing Surge Check}} === "YES" && {{Sales Surge Check}} !== "YES"` on the marketing side).

## Credit gate

There is exactly **one** paid column, and it is the model call.

```js
{{Hiring Surge Dept}} !== ""
```

At the 5.2% floors-gate rate, **948 of every 1,000 rows never touch the model**. Do not remove this
gate: without it the model runs on every row, spends about 19x more, and (as the v1 test proved)
hallucinates a surge onto companies that do not have one.

Everything upstream is free. The four headcount columns carry only a sanity gate
(`!!{{Company Identifier}}`), not a credit gate. **If you find yourself writing a credit gate here
for anything other than column 14, stop — you have added a metered action that does not belong.**

## Column 15: the push gate

Every clause is load-bearing. Copy it, do not simplify it.

```js
!!{{First Name}}
  && !!{{Company Name Clean}}
  && !!{{Master Email Column}}
  && {{Country Classification}}?.includes("US")
  && !{{Person Started Recently}}?.includes("true")
  && !{{Suppression Lookup}}
  && {{Sales Surge Check}} === "YES"
```

| Clause | Why | What breaks without it |
|---|---|---|
| `!!{{First Name}}` | no first name, no greeting | broken merge tag in the send |
| `!!{{Company Name Clean}}` | the cleaned name, not the raw intake name | you bind "ACME, Inc." into copy |
| `!!{{Master Email Column}}` | only fully valid emails reach a campaign | you send to an unvalidated address |
| `{{Country Classification}}?.includes("US")` | region split | US and EMEA leads share a sending window and the wrong copy |
| `!{{Person Started Recently}}?.includes("true")` | **mutual exclusion with `playbook-new-in-role`.** A person who personally just started is routed to that sequence instead | the same lead gets two different sequences from you — the worst deliverability and credibility outcome on the list |
| `!{{Suppression Lookup}}` | the client's suppression list | you email someone the client told you never to email |
| `{{Sales Surge Check}} === "YES"` | the signal itself | the campaign premise is false for the row |

Action bindings: `campaign_id` (string literal), `email = {{Master Email Column}}`, `first_name`,
`last_name`, `website`, `linkedin_profile`, `location`, `company_name = {{Company Name Clean}}`,
and `custom_fields` — add `hiring_surge_line` there.

## Push to your sequencer

Lead-level custom variable `{{hiring_surge_line}}`, rendered as `Noticed {{hiring_surge_line}}.`
Also push `{{hiring_surge_dept}}` if the sequence branches on department.

## Smoke test

Run column 14 on 5 gated rows.

- Column 12 empty on every row → check the floors against your actual counts, and check that
  `job_functions` used a real enum value (a wrong one returns zero silently).
- Counts wildly larger than the company → name collision on the bare-domain path. Apply the
  §7 guard.
- Line says "hired" or "added" → the prompt was edited. Restore it.
