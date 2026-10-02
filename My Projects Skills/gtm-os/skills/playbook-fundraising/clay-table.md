# Clay table build: Fundraising

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 8/10 verdict covers the script path.

## Where the columns go

The table that already sits **behind your email gate**.

## Integration check

| Provider | Native integration? | Use |
|---|---|---|
| The company-data provider (column 1) | often **yes** | the **native action** bound to `{{Domain}}`, reading the same funding block. A raw HTTP column is the fallback, used only when no native exists or it is unconnected |
| The model (column 4) | yes | native AI column |

If the native action appears in the picker but asks you to connect an account, **the native exists
and is merely unconnected — connect it, do not fall back to HTTP.**

⛔ **Never a paid company-enrichment action anywhere in this recipe.**

## Columns

| # | Column | Type | Action | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Funding Raw | native action (HTTP as fallback) | company lookup on the domain, reading the funding block | `{{Domain}}` | `!!{{Domain}}` | free. If you fall back to HTTP, **copy the key from an existing column, do not paste a new one** |
| 2 | Funding Eligible | Run function | the JS below | `{{Funding Raw}}`, `{{Domain}}` | `!!{{Funding Raw}}` | does the domain guard, the stage filter, the 12-month window, and the amount formatting. **All facts are decided here, never by the AI column** |
| 3 | Funding Eligible Flag | Formula | `JSON.parse({{Funding Eligible}}).eligible_flag`, with a fallback returning `"no"` | 2 | none | **a plain scalar so the gate cannot be broken by JSON spacing** |
| 4 | Funding Clause | AI | the §6 prompt verbatim | `{{Funding Eligible}}` | `{{Funding Eligible Flag}} === "yes"` | the gate is both the credit gate and the hallucination gate |
| 5 | funding_clause | Formula | extract the clause, trim, return `""` on anything unparseable | 4 | none | the model's raw clause. **QA reads this column** |
| 6 | funding_line | Formula | `{{funding_clause}} ? "Saw " + {{funding_clause}} + "." : ""` | 5 | none | **this is the column that gets pushed.** The wrap happens in code so an abstaining row pushes a truly empty variable |
| 7 | funding_evidence_url | Formula | extract the evidence URL | 4 | none | QA only, never pushed into copy |

## Column 2: the eligibility function

```js
// Decides EVERY fact. The model downstream only chooses words.
(function () {
  const EQUITY = new Set(["Pre seed","Seed","Series unknown","Series A","Series B","Series C",
    "Series D","Series E-J","Angel","Corporate round","Convertible note","Equity crowdfunding"]);
  // Stage labels that are database buckets, not round names anyone says out loud.
  const UNSPEAKABLE = new Set(["Series E-J", "Series unknown"]);

  const out = { company:"", amount:"", stage:"", eligible:false,
                evidence_url:"", confidence:"low", eligible_flag:"no" };

  const raw = {{Funding Raw}};
  const want = String({{Domain}} || "").toLowerCase();
  const hit  = (raw && raw.results && raw.results[0] && raw.results[0].company) || null;
  if (!hit || !want) return JSON.stringify(out);

  // GUARD 1: domain equality. A website filter also matches OTHER listed websites, so a
  // vendor that lists your target as a customer can win the match with no warning.
  if (String(hit.domain || "").toLowerCase() !== want) return JSON.stringify(out);

  out.company = hit.name || "";

  // GUARD 2: equity stages only. Secondary sales and PE stake purchases are not money
  // the company raised, and a founder will notice if you call them a raise.
  const events = (hit.funding && hit.funding.events) || [];
  const eligible = events.filter(e => EQUITY.has(e.stage));
  if (!eligible.length) return JSON.stringify(out);

  eligible.sort((a, b) => String(b.raised_at || "").localeCompare(String(a.raised_at || "")));
  const latest = eligible[0];

  // GUARD 3: 12-month window, computed here so the model never does arithmetic.
  const months = (Date.now() - Date.parse(latest.raised_at)) / (1000 * 60 * 60 * 24 * 30.44);
  if (!(months >= 0 && months <= 12)) return JSON.stringify(out);

  const amt = Number(latest.amount || 0);
  out.amount = amt >= 1e9 ? "$" + (amt / 1e9).toFixed(1).replace(/\.0$/, "") + "B"
             : amt >= 1e6 ? "$" + Math.round(amt / 1e6) + "M"
             : "";
  out.stage        = UNSPEAKABLE.has(latest.stage) ? "" : (latest.stage || "");
  out.evidence_url = latest.url || "";
  out.confidence   = "high";
  out.eligible     = true;
  out.eligible_flag = "yes";
  return JSON.stringify(out);
})()
```

Note the amount is **rounded here, in code**. The prompt then says "use amount exactly as written",
so the model cannot round differently on different rows.

## Credit gate, and a trap that costs you a whole table

Column 4 is the only column that costs anything, gated on `{{Funding Eligible Flag}} === "yes"`.

⛔ **Do not gate on a substring of the serialized JSON**, e.g.
`{{Funding Eligible}}?.includes('"eligible": true')`.

That substring carries a space after the colon, which only exists because Python's `json.dumps`
defaults to `": "` separators. **A Clay Run-function column is JavaScript, and `JSON.stringify`
emits `"eligible":true` with no space.** The gate would evaluate false on **every row**, the AI
column would never run, the output would be empty for the entire table, and **nothing anywhere would
raise an error.**

That is exactly why column 3 exists: **gate on a scalar, never on the whitespace of a serialized
blob.** If you ever must match inside JSON text, strip whitespace first:

```js
String({{Funding Eligible}}).replace(/\s/g, "").includes('"eligible":true')
```

## Model choice inside Clay

Use the model that was **graded**. A cheaper non-reasoning model may look better on paper — but the
abstain rule, the 80-character cap, the lowercase-first rule and the no-date rule were never
verified on it, and instruction-following differs.

To switch: run the 10 test domains through the candidate, grade with the same rubric, and only if it
scores ≥8/10 **and** measures cheaper do you change the model, the frontmatter, and the verdict
**together**.

## Push to your sequencer

Lead-level custom variable `{{funding_line}}` — **the wrapped whole sentence from column 6, never
the raw clause.** Gate the push action on a valid email.

Then read the §2 downstream gate again. The body line is `{{funding_line}}` alone on its own line.
**Do not wrap it in spintax.**

## Measuring the non-empty rate

`SKILL.md` §2 defers this to your first real campaign. Do it by counting, not by eye: take 200
domains sampled from the lane-A-filtered list, run them through, and count non-empty values. That
percentage decides mechanism 1 versus mechanism 2 in the downstream gate.

## Smoke test

Run 10 rows, including one company you know is bootstrapped.

- Everything empty → almost certainly the JSON-substring gate trap above.
- A wrong company's round appears → the domain-equality guard in column 2 is not firing.
- Copy names a month → the prompt was edited.
