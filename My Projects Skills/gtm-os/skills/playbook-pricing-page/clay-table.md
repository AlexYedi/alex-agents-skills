# Clay table build: Pricing Page

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 8/10 verdict covers the script path.

## The structural constraint

The chain is: a multi-candidate **HEAD** sweep, a plain **GET** of HTML, and a model extraction.
Clay columns handle the third well and the first two badly:

- `http-api-v2` **parses responses as JSON**, so an HTML pricing page returns `body: {}`.
- Clay's HTTP column does not give you a clean way to walk 7 candidate URLs and inspect the **final
  resolved path** after redirects — which is the load-bearing part of step 1.

So the honest options are:

**Option A (recommended): run steps 1 and 2 outside Clay, import `pricing_url` and the page text**,
and let Clay do the extraction, the assertion and the filtering. The existence check costs nothing at
any list size, so run it on the entire TAM, not a sample.

**Option B: a small endpoint** that takes a domain and returns `{pricing_url, text, exists}` as JSON.
Then Clay can self-serve on new rows.

Either way, **`scrape-website` is the right action for a page body, never `http-api-v2`.**

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free, `type: "bare"` |
| 2 | Pricing URL | text / HTTP | imported, or your endpoint | `!!{{f_Domain}}` | ⚠️ **must already encode the soft-404 guard** — see below |
| 3 | Pricing Page Text | text / `scrape-website` | `{{f_PricingURL}}` | `!!{{f_PricingURL}}` | the **price-dense window**, not the first N characters |
| 4 | Pricing Text Rich | Formula | see below | `!!{{f_PricingText}}` | the richness gate that decides whether a render is worth paying for |
| 5 | Pricing Render | HTTP API | rendering proxy | `!!{{f_PricingURL}} && {{f_PricingTextRich}} === false` | **METERED. Never runs otherwise** |
| 6 | Pricing Record | AI | the §6 prompt, page text last | `!!{{f_PricingText}} \|\| !!{{f_PricingRender}}` | `reasoning_effort` low, cap 6000, JSON mode |
| 7 | Price Assertion | Formula | see below | `!!{{f_PricingRecord}}` | **the free verifier. Do not skip it** |
| 8 | pricing_public | Formula | `{{f_PricingRecord}}?.pricing_public === true && {{f_PriceAssertion}} === "pass"` | none | the filter field |
| 9 | pricing_model | Formula | `{{f_PricingRecord}}?.pricing_model \|\| "unknown"` | none | ⚠️ **`unknown` never removes a row** |
| 10 | lowest_paid_price | Formula | `{{f_PricingRecord}}?.lowest_paid_price \|\| ""` | none | |
| 11 | Pricing Needs Review | Formula | `{{f_PricingRecord}}?.confidence === "low" \|\| {{f_PriceAssertion}} !== "pass"` | none | |
| 12 | pricing_line | Formula | `{{f_PricingRecord}}?.pricing_line \|\| ""` | `!!{{f_PricingRecord}}` | **OPT-IN. Do not build this column unless the brief asks for a pricing clause** |

## Column 2: the soft-404 guard

The single most damaging failure in this playbook: `{domain}/pricing` returns **HTTP 200** and
redirects to a 404 page. A real enterprise domain resolves 200 straight to `/404`.

Whatever produces column 2 must accept a candidate **only** when:

1. the final status is 2xx (**any** 2xx — a `Range` fallback answers **206**), **and**
2. the **final resolved path**, after redirects, still matches `/pricing|plans|price/`.

**Status 200 alone proves nothing**, and a guard that fails in the wrong direction records every
quote-only company as having public pricing — a false claim on every one of them.

Walk all 7 candidates: `/pricing`, `/pricing/`, `/plans`, `/pricing-plans`, `/price`, then the same
on `www.`. 15 of 16 pages resolve on the first candidate, **but the walk is not optional** — one
company only resolves via `/pricing → /plans/`.

## Column 4: the richness gate

```js
(() => {
  const t = String({{f_PricingText}} || "");
  const currency = (t.match(/[$€£]\s?\d/g) || []).length;
  // Under 800 visible chars or fewer than 2 currency amounts means we did not really
  // read the page. This is the ONLY condition that justifies paying for a render.
  return t.length >= 800 && currency >= 2;
})()
```

## Column 7: the price assertion

The free verifier. **Better than a second model call, because it cannot be fooled.**

```js
(() => {
  const rec = {{f_PricingRecord}};
  const text = String({{f_PricingText}} || "") + String({{f_PricingRender}} || "");
  if (!rec) return "no record";
  const norm = s => String(s || "").replace(/\s+/g, "").toLowerCase();
  const hay = norm(text);
  const claims = [];
  (rec.plans || []).forEach(p => { if (p.name) claims.push(p.name); if (p.price) claims.push(p.price); });
  if (rec.lowest_paid_price) claims.push(rec.lowest_paid_price);
  // EVERY price and EVERY plan name must appear verbatim in the fetched text.
  // Writing "Base" where the page says "Basic" is the same failure as inventing a
  // number, and it was scored as a pass once already.
  const bad = claims.filter(c => !hay.includes(norm(c)));
  return bad.length ? ("fail: " + bad.join(", ")) : "pass";
})()
```

Filter the view to `Price Assertion != "pass"` before you trust any batch. **Never grade by eye.**

## Credit gates

- **Column 5** (the render) is the only metered enrichment, and it runs **only** when column 4 says
  the free fetch failed.
- **Column 6** is the only model spend.

## Model choice

This prompt is **input-dominated** (~3,461 input tokens against ~702 output), so pick the model with
the cheapest **input** rate at standard pricing. That often inverts the usual in-Clay choice — read
the numbers rather than applying the habit.

## Push to your sequencer

**Nothing, by default.** `pricing_public` and `pricing_model` stay in the table as filter fields and
are **never pushed into copy.**

Only when a brief asked for a clause: push `{{pricing_line}}`, rendered as `Noticed {{pricing_line}}.`

## Smoke test

Run 10 domains, including one you know is enterprise quote-only.

- The quote-only domain reports `pricing_public: true` → your soft-404 guard is missing.
- A big known pricing page reports `quote_only` with high confidence → column 3 is slicing from the
  front instead of using a price-dense window.
- Everything empty → the model hit `finish_reason=length`. Raise the cap and lower reasoning effort.
- The assertion column fails often → the model is shifting prices between plan cards. Spot-check any
  price an order of magnitude above the rest.
