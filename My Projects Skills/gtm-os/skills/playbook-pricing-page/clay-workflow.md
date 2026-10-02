# Clay workflow build: Pricing Page

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This ports to a workflow **much better than to a table**, because the two hard parts — walking 7
candidate URLs and inspecting the **final resolved path** after redirects — are code, and a table has
nowhere to put them.

## Graph

```
[1 trigger: domain]
   -> [2 tool: candidate existence sweep]     <- the soft-404 guard lives here
   -> [3 tool: scrape-website]
   -> [4 code: price-dense window + richness gate]
   -> [5 tool: rendering proxy]               only when 4 says the fetch was thin
   -> [6 agent: extract the record]
   -> [7 code: verbatim price assertion + contract]
```

## Node 2 — the existence sweep

**The most important node, and the one most likely to be built wrong.**

Seven candidates, in order: `/pricing`, `/pricing/`, `/plans`, `/pricing-plans`, `/price`, then the
same on `www.`. 15 of 16 pages resolve on the first — **but the walk is not optional**: one company
only resolves via `/pricing → /plans/`, and two needed all seven.

Accept a candidate **only** when both hold:

1. the final status is **any 2xx** — a compliant origin answers a `Range` fallback with **206**, and
   a script that accepts only 200 silently records those domains as having no pricing page;
2. the **final resolved path**, after redirects, still matches `/pricing|plans|price/`.

```python
import re

CANDIDATES = ["/pricing", "/pricing/", "/plans", "/pricing-plans", "/price"]
PRICING_PATH = re.compile(r"/(pricing|plans|price)", re.I)

def accept(final_url, status):
    # HTTP 200 alone proves NOTHING. A real enterprise domain returns 200 on
    # /pricing and redirects straight to /404. A guard that fails in the wrong
    # direction records every quote-only company as having public pricing, which
    # is a false claim on every one of them.
    if not (200 <= status < 300):
        return False
    path = "/" + "/".join(final_url.split("//")[-1].split("/")[1:])
    return bool(PRICING_PATH.search(path))
```

The sandbox has no outbound HTTP, so the fetching itself is a **tool** node (or your own endpoint);
this code node holds the acceptance logic and picks the winner.

⚠️ **Send a browser User-Agent on every request.** A default runtime UA gets 403'd by common CDNs
while `curl` passes — so **never validate this path with `curl`, because `curl` is not the production
path.**

## Node 3 — fetch the page

⚠️ **`scrape-website`, not `http-api-v2`.** `http-api-v2` parses responses as JSON, so an HTML
pricing page comes back as `body: {}`.

## Node 4 — the price-dense window and the richness gate

```python
import re

CURRENCY = re.compile(r"[$€£]\s?\d")

def run(html_text):
    # Strip to visible text upstream if your fetch does not.
    t = html_text or ""

    # DO NOT use t[:14000]. One real pricing page extracts to 354,059 characters
    # and the first 14,000 contain ZERO prices -- which reports a company with a
    # full public price list as quote_only, with high confidence.
    # Slide a window and keep the densest one.
    WIN, STEP = 14000, 3500
    best, best_hits = t[:WIN], len(CURRENCY.findall(t[:WIN]))
    for i in range(0, max(len(t) - WIN, 0), STEP):
        chunk = t[i:i + WIN]
        hits = len(CURRENCY.findall(chunk))
        if hits > best_hits:
            best, best_hits = chunk, hits

    # The richness gate. This is the ONLY condition that justifies paying for a render.
    rich = len(t) >= 800 and best_hits >= 2
    return {"text": best, "currency_hits": best_hits, "rich": rich}
```

## Node 5 — the rendering proxy

Route it on `rich == false` only. **Never otherwise.**

Keep a render wait as the default but **treat it as unproven**: an A/B on one real page gave
**43 currency tokens either way**, with the wait costing 23.5s instead of 3.4s and adding only a
cookie banner. If you are burning credits with nothing to show, A/B it on your own pages.

Retry transient connection resets with backoff. **A network failure is never a verdict** — and a
fetch step with no retries is worse than it looks: an empty body fails the richness gate and
**spends a metered render credit on what was only a blip.**

## Node 6 — the extractor

The §6 prompt byte-identical as the system message, page text last. `reasoning_effort: "low"`,
`max_completion_tokens: 6000`, JSON mode, no `temperature`. Retry on `finish_reason=length` —
measured **empty content on 3 of 8 rows** at a 3,000-token cap.

**Do not edit the prompt to stop it returning the copy line.** Drop that field in node 7. Editing the
static prefix cools the cache and invalidates the grading.

## Node 7 — the verbatim assertion and the contract

```python
import re

def _norm(s):
    return re.sub(r"\s+", "", str(s or "")).lower()

def run(record, page, want_line=False):
    rec = record or {}
    hay = _norm(page.get("text", ""))

    # THE VERIFIER. Every price and every plan name the model reports must appear
    # VERBATIM in the text we fetched seconds ago. Free, local, and impossible to
    # fool -- strictly better than a second model call here.
    # Writing "Base" where the page says "Basic" is the same failure as inventing
    # a number. That was scored as a pass once already.
    claims = []
    for p in (rec.get("plans") or []):
        if p.get("name"):  claims.append(p["name"])
        if p.get("price"): claims.append(p["price"])
    if rec.get("lowest_paid_price"):
        claims.append(rec["lowest_paid_price"])
    bad = [c for c in claims if _norm(c) not in hay]

    out = {
        "pricing_public":        bool(rec.get("pricing_public")) and not bad,
        # quote_only is a FINDING you can filter on.
        # unknown is a FAILED FETCH and must never remove a row.
        "pricing_model":         rec.get("pricing_model", "unknown"),
        "pricing_url":           page.get("url", ""),
        "plans":                 rec.get("plans", []),
        "lowest_paid_price":     rec.get("lowest_paid_price", ""),
        "has_free_tier":         bool(rec.get("has_free_tier")),
        "enterprise_quote_only": bool(rec.get("enterprise_quote_only")),
        "feature_diff_axis":     rec.get("feature_diff_axis", ""),
        "confidence":            rec.get("confidence", "low"),
        "price_assertion":       "pass" if not bad else ("fail: " + ", ".join(bad)),
        "needs_review":          bool(bad) or rec.get("confidence") == "low",
    }
    # Bones only by default. The copy clause is opt-in and gets dropped HERE,
    # at the boundary, rather than by editing the graded prompt.
    if want_line:
        out["pricing_line"] = rec.get("pricing_line", "")
    return out
```

Give every terminal path a node with this same `outputSchema`.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: pricing page" | jq -r '.id')
# create the 7 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "pricing-page" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"notion.com"},
  {"domain":"palantir.com"}
]}'
```

Expected: the first `pricing_public: true` with real tiers; the second `quote_only` — **not**
`pricing_public: true`. If the second comes back public, your soft-404 guard is missing, because
that domain's `/pricing` returns 200 and lands on a 404 page.

## Politeness

**Concurrency 2 per origin.** These are the websites of companies you want to sell to.

## Smoke test

| What you see | What it means |
|---|---|
| An enterprise quote-only domain reports public pricing | node 2's final-path check is missing |
| A big pricing page reports `quote_only` confidently | node 4 is slicing from the front instead of sliding a window |
| Everything empty | `finish_reason=length`. Raise the cap, lower reasoning effort, retry |
| Node 3 returns `body: {}` | you used `http-api-v2` on HTML |
| Renders firing on most rows | the richness gate is inverted |
| The assertion fails often | the model is shifting prices between plan cards, or picking up a footnote number for a "Contact us" tier |
