# Clay table build: Case-Study Page Name-Drop

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification, never run end to end in Clay.** The 6/7 verdict covers the script path.

⚠️ **Above a few thousand rows, prefer the script path and import the results.** Ten free HTTP probes
per row inside Clay is slower and noisier than one script pass, and the script skips the
credit-consuming scrape and AI columns entirely.

## Column 0 is mandatory, and skipping it produces a 100% miss rate with no obvious cause

**Normalize the domain first, and bind every column below to the normalized value, never to the raw
one.**

A list column holding `https://www.gong.io/` concatenates into
`https://https://www.gong.io//customers`. Every probe 404s. Every row falls through to the paid
fallback. The operator sees a **100% miss rate with no error anywhere.**

Scripts usually normalize internally, so **this bites only in Clay.**

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 0 | Normalized Domain | action | `Normalize a Domain`, type `bare` | none | **MANDATORY.** See above |
| 1 | Case Study URL | HTTP API | `GET https://{{NormalizedDomain}}/customers` | email-valid gate | **Plus nine sibling columns**, one per remaining path, each gated on the previous returning non-200. Browser User-Agent on every one |
| 2 | Case Study URL (agent fallback) | web agent | `{{NormalizedDomain}}` | `!{{f_CaseStudyURL}}` | **Paid per row, the most expensive column here.** This is the credit gate: it only fires when all ten free probes missed |
| 3 | Case Study Page Text | `Scrape Website` | `{{f_CaseStudyURL}}` | `!!{{f_CaseStudyURL}}` | **consumes credits.** Cap at ~18,000 characters, which is what the tested prompt uses |
| 4 | Case Study Raw | AI | `gpt-4o-mini`, `SKILL.md` §6 prompt | `!!{{f_PageText}}` | **consumes credits.** Returns JSON |
| 5 | client_name | Formula | parse from 4 | same | free |
| 6 | evidence_quote | Formula | parse from 4 | same | free. Kept so an operator can audit any line in one click |
| 7 | detail_phrase | Formula | parse from 4 | same | free. Dropped later if ungrounded |
| 8 | confidence | Formula | parse from 4 | same | free. Drives the ship gate |
| 9 | Line Gates | Formula | the five checks, below | `!!{{f_ClientName}}` | free. **Port all five, not the three obvious ones** |
| 10 | case_study_line | Formula | assembly, below | `{{f_LineGates}} === "pass"` | free |
| 11 | ship_ready | Formula | `!!{{f_CaseStudyLine}} && {{f_Confidence}} === "high"` | none | **only `ship_ready` rows get pushed** |

⚠️ **All ten path columns, not four.** One live-test hit came from `/testimonials`, the ninth path.
A four-path build loses every row of that class to the paid fallback — which is both worse and more
expensive.

## Column 9: the five gates

```js
(() => {
  const text  = String({{f_PageText}} || "").toLowerCase();
  const name  = String({{f_ClientName}} || "").trim();
  const quote = String({{f_EvidenceQuote}} || "").trim();
  if (!name || !quote) return "fail: empty";

  // 1-3: the string really is on the page, and the quote really contains the name.
  if (!text.includes(name.toLowerCase()))  return "fail: name-not-on-page";
  if (!text.includes(quote.toLowerCase())) return "fail: quote-not-on-page";
  if (!quote.toLowerCase().includes(name.toLowerCase())) return "fail: quote-missing-name";

  // 4: CMS placeholders and generic nouns. A real captured page served
  // [logo: Startup] and [logo: University] next to real customer logos, and
  // "Saw your work with University." passed checks 1-3 and shipped.
  const PLACEHOLDER = ["startup","university","company","partner","client","customer",
                       "logo","brand","enterprise","business","organization","team"];
  if (PLACEHOLDER.includes(name.toLowerCase())) return "fail: placeholder-name";

  // 5: non-customer context. Investor walls, press strips, partner grids and
  // integration directories sit on the SAME page as the customer logos and all
  // pass a substring check. Reject-only heuristic: a false positive costs one
  // abstained row and never a bad line.
  const BAD  = ["investor","backed by","our investors","press","featured in","as seen in",
                "partner","integrations","works with","media"];
  const GOOD = ["customer","client","case stud","success stor","testimonial","story"];
  const idx  = text.indexOf(name.toLowerCase());
  const win  = text.slice(Math.max(0, idx - 600), idx);
  if (BAD.some(b => win.includes(b)) && !GOOD.some(g => win.includes(g)))
    return "fail: non-customer-context";

  return "pass";
})()
```

**Checks 4 and 5 are not a proof of customerhood.** They reject the shapes that were observed. The
class has never been live-tested against a real investor or press wall, which is why low-confidence
rows are held.

## Column 10: line assembly, in a formula, never by the model

```js
(() => {
  const name  = String({{f_ClientName}} || "").trim();
  const quote = String({{f_EvidenceQuote}} || "").toLowerCase();
  let   d     = String({{f_DetailPhrase}} || "").trim();
  if (!name) return "";

  const DANGLING = ["back","up","out","on","of","to","in","with","for"];
  const VERBS    = ["is","are","was","were","has","have","helps","helped","cut","cuts",
                    "saved","saves","centralises","centralizes","unified","unifies"];
  const words = d.toLowerCase().split(/\s+/).filter(Boolean);

  const grounded = d && words.every(w => quote.includes(w))
                 && d.toLowerCase() !== name.toLowerCase()
                 && !DANGLING.includes(words[words.length - 1])
                 && !words.some(w => VERBS.includes(w))
                 && {{f_Confidence}} === "high";   // a low row never carries a topic

  let line = "your work with " + name + (grounded ? " on " + d : "");
  if (line.split(/\s+/).length > 16) line = "your work with " + name;
  return line;
})()
```

**Every grounding rule here exists because of an observed failure:** a percentage copied from a
few-shot example onto an unrelated company; `your work with Air Tutors on Air Tutors`; `your work
with Google on time back`.

## Credit gates

The paid columns are **2, 3 and 4** — not just column 2, which is the easy mistake.

- **Column 2** (the agent fallback) is gated on all ten free probes missing.
- **Columns 3 and 4** consume credits **on every row that found a page.** A 50k-row import costs
  roughly 50k × (scrape + AI) plus the agent tail.

⚠️ **Add rows LAST.** Clay auto-runs columns on insert, and an ungated table burns credits the moment
you import.

## Push to your sequencer

`{{case_study_line}}`, plus `client_name` and `case_study_url` as lead-level fields — **so a reply can
be answered without re-researching the account.**

Filter to `ship_ready == true`.

## Smoke test

Run 10 rows including one company you know has no customer page.

- 100% miss with no error → column 0 is missing and your domains carry a scheme.
- The agent fallback fires on most rows → your path columns are not chained correctly, or the
  User-Agent header is missing.
- A generic word ships as a customer name → the placeholder gate is missing.
- Everything ships → check that `ship_ready` is actually requiring high confidence.
