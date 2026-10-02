# Clay table build: Company Name Cleaning

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: the default build (columns 1 and 2) is standard Clay and works. The toggle build
(columns 3 to 6) is a specification that has never been run as a Clay AI column.** The 98/100
verdict covers the script path.

## Where the columns go

Main work table, **after email validation**. Cleaning names for rows that fail the email gate is
wasted work.

## The default build is two free native actions

For most clients **you build nothing at all here.**

| Order | Column | Type | Action | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Normalize a Domain | Clay action | `Normalize a Domain`, `type: "bare"` | Website | none | **DEFAULT.** Free, always first |
| 2 | Normalize Company Name | Clay action | `Normalize Company Name`, `titleCase: true` | the raw company string | none | **DEFAULT, and on most clients the last column in this playbook.** Free. Its output is what your sequencer push sends as `company_name` |

**Do not remove column 2, do not replace it, and do not re-point the push away from it** unless you
are deliberately switching the toggle on.

## The toggle build adds four more

Add these **only** when the §0 test in `SKILL.md` says to.

| Order | Column | Type | Action | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 3 | Company Clean JSON | AI | `gpt-4o-mini`, `SKILL.md` §6 prompt verbatim, JSON response format | `name="{{RawCompanyName}}" domain="{{BareDomain}}"` | `!!{{f_RawCompanyName}} && !!{{f_ValidEmail}}` | **Pass the RAWEST company string you have**, not the normalized one, so the model still sees the dba and tagline structure |
| 4 | Placeholder Guard | Formula | see below | column 3 and the raw name | none | **Required whenever column 3 exists.** Mini scored 7/10 on the abstain probe on its own |
| 5 | company_clean | Formula | `{{f_PlaceholderGuard}} ? "" : ({{f_CompanyCleanJson}}?.company_clean \|\| "")` | 3, 4 | none | When it exists, **this** is what ships, and the push's `company_name` binding moves here. Moving that binding is the switch — remember to move it back if you turn the toggle off |
| 6 | Name Needs Review | Formula | `!{{f_company_clean}} \|\| {{f_CompanyCleanJson}}?.confidence === "low"` | 3, 5 | none | drives the review filter and the downstream gate |

## Column 4: the placeholder guard

Matches on the **whole normalized string** plus a `selfemployed` prefix. Substring matching would
delete real companies — `Unknown Arts` is a real brand, and so is the bank in `Retired - BTH Bank`.

```javascript
(() => {
  const norm = s => (s || "").toLowerCase().replace(/[^a-z0-9]/g, "");
  const BLOCK = new Set(["na","n","none","null","nil","unknown","unknowncompany","tbd","tba",
    "test","testing","xxx","asdf","retired","unemployed","student","freelance","freelancer",
    "selfemployed","self","soleproprietor","soleproprietorship","privatepractice","private",
    "confidential","confidentialjobs","confidentialcompany","homemaker","various","other",
    "myself","me","personal","notapplicable","stealth","stealthmode","stealthstartup"]);
  const hit = v => { const n = norm(v); return !n || BLOCK.has(n) || n.startsWith("selfemployed"); };
  return hit({{f_RawCompanyName}}) || hit({{f_CompanyCleanJson}}?.company_clean);
})()
```

Optionally add the invented-word guard from `SKILL.md` §6 as a seventh column: normalize both
strings to lowercase alphanumerics and confirm the output is a substring of the input.

## Credit gate

On the default build there is nothing to gate — both columns are free native actions.

With the toggle on, column 3 is gated so you never clean a name for a row that failed email
validation. **No column in this recipe spends an enrichment credit.**

⚠️ **Smoke-test the gate before you run the table.** Set the gate, run 10 rows, and confirm the AI
column actually executed on rows you *know* have a valid email. A gate bound to a column name that
does not exist fails silently and produces **exactly the same table state as "no rows qualified"** —
and the downstream gate then excludes your entire list from the campaign. It looks like a data
problem and it is a config typo.

## Sentinel note

If your workspace uses a literal sentinel string for "not found", this column deviates: it returns
JSON, so the abstain value is an **empty `company_clean` key**, tested directly with
`!{{company_clean}}`.

## Push to your sequencer

Lead-level custom variable `{{company_clean}}`. Name it exactly that in the lead payload so copy
and QA both refer to one string.

## QA before launch, non-negotiable

**Read 20 sampled values inside the actual sentence from the copy, out loud.** The normalizer's
output on the default build; `company_clean` when the toggle is on. **Any value you would edit is a
failure.**

On the default build, that read **is** the toggle test: if more than about 2 of the 20 fail, and
they fail in the tagline / dba / parenthetical / second-language way, switch the toggle on.

When the toggle is already on, the fix is a **prompt correction round, not a manual edit of the
row**.
