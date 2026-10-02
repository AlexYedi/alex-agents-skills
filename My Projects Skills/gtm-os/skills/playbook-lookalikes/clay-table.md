# Clay table build: Case-Study Lookalikes

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.**

## What Clay does and does not do here

This playbook has two halves, and only one of them belongs in a table.

- **The mining half** — prompt A, the industry-enum bake-off, the filter search, the snowball — is a
  **once-per-case-study** job done outside Clay. It produces an attribute card and a list of domains.
  Putting a once-per-campaign step in a per-row table is how you pay for it thousands of times.
- **The labelling half** — prompt B judging each pulled company and attaching the right case-study
  reference — is per row, and belongs here.

So: mine outside, import the domains, label inside.

## Where the columns go

Your company-level work table, before contacts are pulled. **Judging companies is much cheaper than
judging people**, because one judgment covers every contact at that company.

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free |
| 2 | Company Description | action / imported | `{{Domain}}` | `!!{{f_Domain}}` | prefer a **free** company-data source. See the note below |
| 3 | Case Study Judge | AI | `SKILL.md` §6 prompt B, JSON out | `!!{{f_Description}}` | the only paid column |
| 4 | qualified | Formula | `{{f_Judge}}?.qualified === true` | none | the gate |
| 5 | case_study_ref | Formula | `{{f_Qualified}} ? ({{f_Judge}}?.case_study_ref \|\| "") : ""` | none | **always agrees with column 4** |
| 6 | case_study_match_reason | Formula | `{{f_Judge}}?.case_study_match_reason \|\| ""` | none | **QA only. Never pushed** |
| 7 | Site Liveness | HTTP / `scrape-website` | `{{f_Domain}}` | `{{f_Qualified}} === true` | **the verifier that actually matters here** |
| 8 | lookalike_case_study_line | Formula | look up the descriptor for `{{case_study_ref}}` from the attribute card | `!!{{f_CaseStudyRef}} && {{f_SiteLive}}` | **the pushed field** |

### Column 2: use a free company description

A **free** company-enrichment source is fine for a description. **Do not reach for a high-credit
company enrichment for this** — you are feeding a text judge, not building a profile, and an 8-credit
lookup per row on a widening pass is how this playbook stops being cheap.

### Column 7: the liveness check

The one verification this playbook genuinely needs. **Company databases happily describe companies
that no longer trade**, and a description-only judge will qualify them confidently.

Classify **dead / parked / live**, and on live sites prefer the site's own current copy over the
database description when the two disagree.

## The abstain convention here

If your workspace uses a literal sentinel string for "cannot answer" in AI columns, **this table does
not use it** — the AI column returns JSON that a formula parses, and the pushed value comes from a
formula lookup, not from the model.

The abstain path is `qualified: false` plus an empty `case_study_ref`, end to end. **Nothing gates on
a sentinel string here, so do not wire one — it would build a gate that never fires.**

If you later add a plain-text AI column to this table, that column should follow your normal sentinel
convention.

## Credit gate

Column 3 is the only paid column. Gate it on a description existing — **a thin description is
`qualified: false` anyway, so paying to judge one is pure waste.**

## Push to your sequencer

`{{lookalike_case_study_line}}` and `{{case_study_ref}}`.

⛔ **Never push `case_study_match_reason`.** It is internal QA text and it is populated on rejected
rows.

⚠️ **Never name the field `case_study_line`.** `playbook-case-study-page` owns that name for a
different sentence, and a collision renders **"We did this for your work with Intercom."**

## Smoke test

Run 20 rows and read the reasons in column 6 — including on rejected rows. That column exists so you
can see **why** the judge decided, and it is the fastest way to spot an attribute card that is too
loose.

- Nearly everything qualifies → your resonance reasons are not testable. "is innovative" is not a
  filter.
- Nearly nothing qualifies → the attribute card is over-specified, or you are judging against the
  wrong industry enum.
- Agencies and publishers qualify → add them to the exclude keywords and re-run the bake-off.
