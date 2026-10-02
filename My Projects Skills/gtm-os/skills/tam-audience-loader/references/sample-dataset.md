# The shipped sample, end to end

Three files ship beside this one so the skill can be exercised before anyone points it at real
data: `references/sample-companies.csv` (18 rows), `references/sample-contacts.csv` (32 rows) and
`references/sample-mapping.json`.

They are shaped like a TAM a model actually produces: a handful of columns Clay already has a field
for, a pile of research columns it does not, and values that are *nearly* well-formed. **Every
defect in them is deliberate**, and the point of the walkthrough below is that each one is caught
at a different step, by a different check, with a different remedy.

Nothing here resolves to a real company. Every domain is under `.example`. The LinkedIn URLs use
the real `linkedin.com` host because Clay will not accept anything else as a match key — see below,
it is one of the findings.

## What is in the files

**Companies — 27 columns.** Six map onto fields Clay already has (`company_name`, `website`,
`linkedin_company_url`, `hq_city`, `hq_country`, `employee_count`). Ten are research columns that
have to be created (`icp_tier`, `fit_score`, `why_now`, `buying_trigger`, `tech_stack_detected`,
`last_funding_stage`, `last_funding_date`, `funding_raised_usd`, `net_new_arr_potential`,
`expansion_signal`). **Eleven are left out of the mapping entirely** — `compliance_regime`,
`procurement_model`, `pricing_page_url`, `renewal_month`, `owner_email`, `confidence`,
`sourced_from`, `research_notes`, `analyst_coverage`, `founded`, `hq_*` duplicates — because a TAM
export carries far more than belongs in an audience and the default is to leave a column out.

**Contacts — 21 columns.** Eight map onto existing fields, six are created, seven are left out.

## The nine planted defects, and where each one is caught

| # | Where | What | Caught by |
|---|---|---|---|
| 1 | `CT-002`, `VC-013` | `1,001-5,000` and `~2,500` in a headcount column | Step 1 infers `text`; Step 3 counts them if you override to `number` |
| 2 | `TS-004` | `Q3 2024` where every other funding date is ISO | same |
| 3 | `FB-003` | `03/15/2024` — one US-format date in an ISO column | Step 1 infers `text` |
| 4 | `FB-003`, `PS-009` | `$8,500,000` and `€8.5M` in a funding amount | Step 3 coercion count |
| 5 | `TS-004` | `unknown` in an otherwise true/false column | Step 3 coercion count |
| 6 | `LW-006` | no website and no LinkedIn URL | Step 3 `no Clay match key` — cannot be loaded at all |
| 7 | `FC-010` | a LinkedIn URL whose host is not `linkedin.com` | Step 3 `values Clay will not accept as that key`; falls through to its domain and still loads |
| 8 | `NW-001` / `NW-007` | two rows, one domain in different case with a trailing slash | Step 3 collision count — two rows, one record |
| 9 | `NW-001` twice, `P-0001` twice | the same row key exported twice | Step 3 `duplicate row key` |

On the contacts side: `P-0005` carries no email, LinkedIn or phone; `P-0010` carries a LinkedIn URL
on the wrong host and nothing else, so he is unloadable **for a different reason**; `P-0004` points
at a company id that is not in the companies file; `P-0023` and `P-0032` are distinct people the
research pass gave the same email, so they collapse onto one record; `~3` sits in a years-in-role
column and `Q1 2025` in a job-change column; `mobile_phone` is blank on every row, so the phone
match key never claims anything.

`tech_stack_detected` and `conferences_attended` hold several values per cell. **There is no list
type**, so they land as one text field each — matchable with `contains`, never countable.

## Step 1 — what `inspect` says

```
python3 scripts/loader_lib.py inspect --companies references/sample-companies.csv \
                                      --contacts references/sample-contacts.csv
```

The interesting rows, and every one of them is the inference refusing to be clever:

```
column                       type      blank   two values
website                      url       2       https://northwind.example | https://contoso.example
employee_count               text      0       512 | 1,001-5,000
fit_score                    number    0       92 | 88
last_funding_date            text      6       2024-03-01 | 03/15/2024
funding_raised_usd           text      6       48000000 | $8,500,000
expansion_signal             text      0       true | true
analyst_coverage             boolean   0       yes | yes
  proposed, correct any of these:
    row_key_column       company_id
    domain_column        website
    name_column          company_name
```

**`employee_count` comes back as `text` and that is the whole lesson.** The first value is `512`
and the fifty-first is a band; reading the column rather than its first rows is what keeps it out
of a number field. Same for `last_funding_date` and `funding_raised_usd`. Note `expansion_signal`
reads as `text` — because one row says `unknown` — while `analyst_coverage` beside it is a clean
`boolean`.

The three proposals are worth reading closely, because each had to be taught not to guess
confidently: `pricing_page_url` beat `website` for "the domain" on the token `url`; `company_id`
beat `company_name` for "the name" on `company`; and on the contacts side `contact_id` beat
`company_key` for "the company this contact belongs to" on `id`. All three were wrong and all three
read as if the file had been understood.

## Step 3 — what `check` says, on the shipped mapping

**`sample-mapping.json` is deliberately the installer's FIRST attempt, not the corrected one.**
Four columns in it are typed the way a reasonable person types them on sight — a headcount is a
number, a funding date is a date — rather than the way the data actually reads. So the report has
something to say:

```
python3 scripts/loader_lib.py check --companies references/sample-companies.csv \
        --contacts references/sample-contacts.csv --map references/sample-mapping.json
```

```
companies — 18 rows, 16 loadable
  no Clay match key ........ 1
  duplicate row key ........ 1
  sharing a match key ...... 2 rows into 1 records
  matched by ............... {'domain': 15, 'linkedin_url': 1}
  values Clay will not accept as that key — present, and refused like a blank:
    linkedin_url             1   e.g. https://www.linkedin.example/company/fourth-coffee
  values their type cannot parse — these WRITE and never match a filter:
    employee_count           number  2 of 16 carried   e.g. 1,001-5,000, ~2,500
    last_funding_date        date  1 of 10 carried   e.g. Q3 2024
    funding_raised_usd       number  2 of 10 carried   e.g. $8,500,000, €8.5M
    expansion_signal         boolean  1 of 16 carried   e.g. unknown
```

Four counts, four different remedies, and the last block is the one to act on: move those columns
to `text` and the values stay visible. Leave them and they will write, report success, and never
match a filter.

## Step 5 — creating the audience fields

**Dry run first.** It changes nothing and names every field it would add:

```
python3 scripts/build_loader.py fields --map <your copy of sample-mapping.json> --dry-run
```

```
companies: 10 would be created, 6 already there, 0 refused
  icp_tier                 <would create: TAM ICP tier / text>
  fit_score                <would create: TAM fit score / number>
  why_now                  <would create: TAM why now / text>
  buying_trigger           <would create: TAM buying trigger / text>
  tech_stack_detected      <would create: TAM tech stack / text>
  last_funding_stage       <would create: TAM last funding stage / text>
  last_funding_date        <would create: TAM last funding date / date>
  funding_raised_usd       <would create: TAM funding raised / number>
  net_new_arr_potential    <would create: TAM net new ARR potential / number>
  expansion_signal         <would create: TAM expansion signal / boolean>
contacts: 6 would be created, 8 already there, 0 refused
  persona                  <would create: TAM persona / text>
  persona_confidence       <would create: TAM persona confidence / number>
  outreach_angle           <would create: TAM outreach angle / text>
  years_in_role            <would create: TAM years in role / number>
  is_decision_maker        <would create: TAM is decision maker / boolean>
  last_job_change          <would create: TAM last job change / date>
```

**"6 already there" is the interesting half.** `company_name` maps to `org_name`, `website` to
`domain`, `hq_city` to `location_city` — fields every workspace has. Nothing is created for those,
and mapping a research column onto an existing field is usually better than minting a near-duplicate
beside it.

Then, for real:

```
python3 scripts/build_loader.py fields --map <your copy>
```

```
companies: 10 created, 6 already there, 0 refused
contacts: 6 created, 8 already there, 0 refused
mapping updated with the field ids Clay returned
```

**Work on a COPY of `sample-mapping.json`.** That last line is literal: the command writes the field
ids Clay returned back into the mapping file, and those ids exist only in the workspace that made
them. The shipped copy carries none, and it must stay that way.

**The ids are read back rather than assumed** because `fields create` silently uniquifies a name
already in use — ask for `TAM persona` twice and the second one is `TAM persona (2)`, under an id
you would never have guessed. Confirm what landed:

```
clay audiences fields list --entity-type companies
clay audiences fields list --entity-type people
```

## What a full load of this sample does

18 companies: **16 load**, 1 is refused for carrying no match key, 1 for a duplicate row key. Two of
the 16 — `NW-001` and `NW-007` — come back with **the same record id**, which is the domain
collision the report predicted, visible in the ledger rather than inferred.

32 contacts: **29 load**, 2 refused for no usable match key, 1 for a duplicate row key. `P-0032`
comes back with `P-0023`'s record id. 15 company ids are folded out of the company ledger, and the
contacts whose company never loaded — `P-0007`, whose employer is `LW-006` — load with no company
attached and are stamped `associated: false`.

## Three things this sample taught that nothing else did

**A match key is validated for shape, not just for being non-empty.** `WG-005` has no website, so
it must match on its LinkedIn URL — and with a `.example` host it failed with *"None of the selected
lookup fields contained a valid value to match on"*, which reads exactly like the field was blank.
Confirmed on all three key types: a malformed email and a phone with no digits fail identically,
while a `.example` **domain** and a `.example` **email address** are both accepted. So it is not a
check on whether the thing is real — it is a check on whether it is that *kind* of thing, and
`linkedin_url` means `linkedin.com`. The loader screens for it and falls through to the next key,
which is why `FC-010` still loads on its domain.

**A boolean cannot be coverage-checked.** On a boolean field, `is_not_null` returns exactly what
`= true` returns, and `= false` returns everything else — **including every record the field was
never set on**. Counted here: 15 true plus 21 false equals 36, which is every person in the
workspace, against 28 the loader had written to. So no query distinguishes "explicitly false" from
"never set", and the verification step reports booleans as unmeasurable rather than raising a
discrepancy that is really a property of the store. **If you need to tell false from unset, a
boolean field cannot do it** — use text with explicit values, which is what `expansion_signal`
being three-valued was trying to say all along.

**The query index lags the write.** A verification run fired immediately after a load under-reported
one field and reported it correctly a minute later. A single "SHORT BY" on a fresh load is worth
re-reading before acting on.

## Cleaning up after a trial run

The fields and both workflows are removable; the records are not.

```
clay audiences fields delete <fieldId> --entity-type companies
clay workflows delete <workflowId>
```

**There is no CLI path that deletes an audience record** — `clay audiences records` is read-only. A
trial load leaves its records behind, and they have to be archived in the app. Run the sample in a
workspace where that is acceptable, and prefer `--limit 10` on the first pass.
