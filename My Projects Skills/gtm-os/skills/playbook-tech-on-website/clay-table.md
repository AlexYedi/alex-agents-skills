# Clay table build: Technology On Website

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.**

## The structural problem, and how to solve it

This playbook's gate is **a live HTTP fetch of the prospect's homepage, matched against fingerprints
over both HTML and response headers.** Clay cannot do that in a column, for a concrete reason:

- `http-api-v2` **parses responses as JSON**, so an HTML page comes back as `body: {}`. It cannot
  read a homepage.
- `scrape-website` returns page **content**, but does not give you the **response headers** — and
  the headers are where the confirmed-grade evidence lives (`x-shopid`, `powered-by`).

Two workable options:

**Option A (recommended): verify outside Clay, import the verdict.** Run the gate as a script, then
import `verdicts.jsonl` as a CSV. Clay holds the verdict and the clause; it does not do the fetching.

**Option B: stand up a small verification endpoint** that does the fetch, the header match and the
grading, and returns **JSON**. Then `http-api-v2` can call it, because now the response really is
JSON. This is the right choice if the table needs to self-serve on new rows.

Option B is what makes this a live Clay table rather than an import. Its whole job is to turn "read
a webpage" into "call a JSON API", which is the one shape Clay columns handle well.

## Where the columns go

The table behind your email gate.

## Columns

| # | Column | Type | Action | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | `Normalize a Domain`, `type: "bare"` | Website | none | free |
| 2 | Tech Verify Raw | HTTP API | your verification endpoint (option B), or **imported** (option A) | `{{Domain}}` | `!!{{Domain}}` | returns `{ok, blocked, blocked_reason, detected_names, confidence, evidence, checked_at}` |
| 3 | Tech Blocked | Formula | `{{f_TechVerifyRaw}}?.blocked === true` | 2 | none | **route on this flag** |
| 4 | Tech Stack Verified | Formula | `{{f_TechVerifyRaw}}?.detected_names \|\| []` | 2 | none | output field |
| 5 | Tech Confirmed | Formula | see below | 3, 4 | none | **exact array-element match, never a substring** |
| 6 | Tech Evidence | Formula | `{{f_TechVerifyRaw}}?.evidence \|\| ""` | 2 | none | output field |
| 7 | Tech Checked At | Formula | `{{f_TechVerifyRaw}}?.checked_at \|\| ""` | 2 | none | ⚠️ the verifier's own key is often `checked_at`; **the output field is `tech_checked_at`. Map it on write** |
| 8 | Tech Confidence | Formula | see below | 2, 3, 5 | none | must be able to say `blocked` and `unconfirmed`, not just true/false |
| 9 | Tech Line Raw | AI | **OPT-IN ONLY.** `gpt-4o-mini`, `SKILL.md` §4 prompt | 4, 5, 6, Company Name Clean | `{{f_TechConfirmed}} === true` | **do not build this column unless a sentence was requested** |
| 10 | tech_on_website_line | Formula | the post-guards | 9 | `!!{{f_TechLineRaw}}` | OPT-IN ONLY |

## Column 5: the exact-match formula

```js
// EXACT array-element match. A substring test is how a B2B software company
// with a "Shopify Buy Button" embed gets a storefront clause written about it.
(() => {
  const target = String({{f_TargetTech}} || "").trim().toLowerCase();
  const stack  = {{f_TechStackVerified}} || [];
  if (!target || {{f_TechBlocked}}) return false;
  return stack.some(t => String(t).trim().toLowerCase() === target);
})()
```

## Column 8: confidence, with the three non-negatives

```js
(() => {
  if ({{f_TechBlocked}}) return "blocked";                 // we could not look. NOT a no.
  if ({{f_TechConfirmed}}) return {{f_TechVerifyRaw}}?.confidence || "high";
  const stack = {{f_TechVerifyRaw}}?.html_only_names || [];
  const target = String({{f_TargetTech}} || "").trim().toLowerCase();
  // HTML matched but no header and no oracle: the agency / Buy-Button shape.
  if (stack.some(t => String(t).trim().toLowerCase() === target)) return "unconfirmed";
  return "negative";                                       // a real, earned no.
})()
```

⚠️ **`blocked` and `unconfirmed` must survive into whatever you persist, beside the verdict.** If you
collapse them to `false`, a bot-wall 403 reads downstream as a confident "no technology found" and
you silently drop real customers from the list.

## Credit gate

The verdict path costs nothing. **The only paid column is the opt-in AI column**, gated on
`{{f_TechConfirmed}} === true`.

If you find yourself writing a credit gate for anything else here, you have added a metered action
that does not belong.

## Filtering the table after a run

```
Tech Confidence == "blocked"      -> re-verify through the rendering proxy
Tech Confidence == "unconfirmed"  -> human check, or a tech-specific endpoint
Tech Confidence == "negative"     -> a genuine no. Safe to exclude
Tech Confirmed  == true           -> the list
```

Expect roughly **60% of a provider-sourced list to survive.** If you are seeing 90%+, check that the
gate is actually running rather than defaulting to true.

## Push to your sequencer

The verdict is usually the deliverable and never reaches copy — you use it to **build the list**,
not to personalize it.

If a clause was requested, push `{{tech_on_website_line}}`, rendered as
`Noticed {{tech_on_website_line}}.`

## Smoke test

Run 10 domains, including one you know is behind a bot wall.

- The blocked domain comes back `false` instead of `blocked` → your verifier is treating a 403 body
  as a successful fetch. This is the single most damaging bug in this playbook.
- An agency portfolio site comes back confirmed → the platform grading is not requiring header or
  oracle evidence.
- Everything confirmed → the gate is not running.
