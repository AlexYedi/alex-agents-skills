# Clay table build: Warm Intros

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification, and this playbook is less proven than the others.** Sources were probed;
**no line has been graded.** Build member 2, run 10 rows, read them, and fix this file before you
build anything else.

## Where the columns go

A **person-level** table. The discovery half — a people search with a past-company filter — happens
outside Clay and produces the rows; Clay does the exclusions, the evidence extraction and the line.

That split matters here because the search is **one-to-many** (one customer company yields hundreds
of alumni) and a column cannot produce rows.

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Matched Past Employer | imported | from the search | none | **must arrive dated** |
| 2 | Current Employer Domain | Formula / action | imported | none | resolve to a bare domain |
| 3 | **Still At Source** | Formula | 2 + the source list | none | **exclusion. Build this first** |
| 4 | Client Domain Check | Formula | the source list | none | **a config check, not a row filter** |
| 5 | Suppression Lookup | Lookup Object | domain, email | `{{f_StillAtSource}} === false` | client DNC, existing TAM, live campaigns |
| 6 | Qualifies | Formula | `!{{f_StillAtSource}} && !{{f_Suppressed}}` | none | |
| 7 | warm_intro_member | Formula | which member produced this row | none | **keep it. This is how you learn which angle works** |
| 8 | Warm Intro Evidence | Formula | employer + title + dates from 1 | `{{f_Qualifies}}` | **QA only, never pushed** |
| 9 | warm_intro_line | Formula or AI | 1, 7 | `{{f_Qualifies}}` | see the naming rule below |

## Column 3: the exclusion that defines the list

```js
(() => {
  const SOURCE_DOMAINS = ["customer-one.com", "customer-two.com"];   // the client's customers
  const cur  = String({{f_CurrentEmployerDomain}} || "").toLowerCase();
  const mail = String({{f_Email}} || "").split("@")[1] || "";
  // Someone still AT the client's customer is not a warm intro -- they ARE the
  // customer. The probe found ~15 of 20 had moved on, so this exclusion removes
  // roughly a quarter of the raw pull and it is the difference between a prospect
  // list and a list of your client's own account contacts.
  return SOURCE_DOMAINS.includes(cur) || SOURCE_DOMAINS.includes(mail);
})()
```

## Column 4: a config check, not a filter

```js
(() => {
  const SOURCE_DOMAINS = ["customer-one.com", "customer-two.com"];
  const CLIENT_DOMAIN  = "our-client.com";
  // If the CLIENT's own domain is in the source set, the source list is wrong.
  // Do not filter around it -- surface it and stop.
  return SOURCE_DOMAINS.includes(CLIENT_DOMAIN) ? "CONFIG ERROR" : "ok";
})()
```

Filter the view on this column once, before you run anything. It should be empty.

## Column 9: the line, and the naming rule

The line is short enough to be a **formula**, and a formula is the safer choice here because the risk
in this playbook is **what gets named**, not how it is phrased.

```js
(() => {
  const emp = String({{f_MatchedPastEmployer}}?.company || "").trim();
  if (!emp || !{{f_Qualifies}}) return "";
  // The UNNAMED form is the default. "who we work with now" says the relationship
  // without disclosing which of the client's customers this is. Naming a client's
  // customer in cold email is the CLIENT's decision, not ours.
  // Never state a date: profile date ranges are imprecise, and "in 2018 you were
  // at X" is both creepy and frequently wrong.
  return "you came up through " + emp + ", who we work with now";
})()
```

If the client has explicitly approved naming the customer, that is a copy change to this one formula
— **and it should be recorded per client, not applied globally.**

## Push to your sequencer

`{{warm_intro_line}}` and `{{warm_intro_member}}`.

⛔ **Never push the evidence column.** It contains employment dates.

**Keep the member field on every row.** Seven members share one copy shape, and without the member
name you cannot tell which angle produced replies — which is the only way this family ever gets
narrowed to the two or three members worth keeping.

## Do not forget the DNC push

Push the source companies onto the client's do-not-contact list, once per build. **Row exclusions fix
this run; the block list is what persists.**

## Smoke test

Run 20 rows, and grade the lines by hand — **this playbook has no graded verdict, so your first run
is the verdict.**

- Column 4 shows a config error → **stop.** The source list contains the client.
- Most rows still work at the source company → the search returned current employees, not alumni.
- Lines name a customer → check that naming was actually approved.
- Lines state dates → the formula was changed. Dates do not go in copy.
- You cannot tell which member a row came from → column 7 is missing.
