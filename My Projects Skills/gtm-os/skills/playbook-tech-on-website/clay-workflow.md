# Clay workflow build: Technology On Website

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

**This playbook ports to a workflow better than it ports to a table**, because a workflow has code
nodes — and the fingerprint grading is code. The one thing a workflow still cannot do is read
**response headers**, which is where the strongest evidence lives. Read the "header problem" section
before you build.

## Graph

```
[1 trigger: domain + target_tech]
   -> [2 tool: scrape-website]
   -> [3 code: blocked detection]
   -> [4 code: fingerprint match + platform grading]
   -> [5 code: verdict + confidence]
   -> [6 agent: write the clause]     OPT-IN, skip by default
   -> [7 code: post-guards + contract]
```

Nodes 1 to 5 are the whole default deliverable. **Build those, ship, and only add 6 and 7 if a
sentence was actually requested.**

## The header problem

The confirmed-grade evidence for a platform is a **response header** (`x-shopid`, `powered-by`).
Neither of Clay's fetch actions gives you headers cleanly:

- `http-api-v2` parses responses as JSON, so an HTML homepage returns `body: {}`.
- `scrape-website` returns content, not headers.

Three ways to live with that, in order of preference:

1. **Point node 2 at your own verification endpoint** that does the fetch, exposes headers, and
   returns JSON. Then `http-api-v2` works, because the response really is JSON.
2. **Use the technology oracles**, which are ordinary JSON endpoints and therefore fine for
   `http-api-v2`: `/products.json` for Shopify, `/wp-json/` for WordPress. An oracle answer grades
   as **confirmed**, exactly like a header.
3. **Accept HTML-only matching**, and treat every platform hit as `unconfirmed`. Honest, and much
   less useful.

Option 2 is the one that makes a pure-Clay workflow actually work for the two technologies that have
oracles.

## Node 2 — fetch

⚠️ Use `scrape-website`, **not** `http-api-v2`, for the homepage. `http-api-v2` returns `body: {}`
on HTML. If you are calling an oracle or your own endpoint, `http-api-v2` is correct.

`automapInputs: false`. Pin `domain` from the trigger.

## Node 3 — blocked detection

```python
BLOCKED_STATUSES = {401, 403, 405, 429, 503}

def run(fetch):
    status = (fetch or {}).get("status") or 0
    body   = (fetch or {}).get("content") or ""
    err    = (fetch or {}).get("error")

    reason = ""
    if err:                              reason = "transport_error"
    elif status in BLOCKED_STATUSES:     reason = "http_%d" % status
    elif status >= 400:                  reason = "http_%d" % status
    elif len(body) < 2000:               reason = "body_too_small"

    # A bot wall is NOT an answer. Without this, a CDN 403 comes back as a
    # successful fetch whose only "detected" technology is the CDN itself, which
    # reads downstream as "we looked and found nothing" -- a silent false abstain
    # that quietly drops real customers off the list.
    return {"blocked": bool(reason), "blocked_reason": reason, "body": body}
```

The `body_too_small` check catches challenge pages that return HTTP 200. It is not optional.

## Node 4 — fingerprints and platform grading

```python
import re

# kind: platform  -> needs header or oracle evidence to be CONFIRMED
# kind: embed     -> dropped before the model entirely
# kind: infra/analytics -> noise, never a verdict
FINGERPRINTS = {
    "Shopify":   {"kind": "platform",
                  "html": [r"cdn\.shopify\.com", r"[a-z0-9-]+\.myshopify\.com"],
                  "oracle": "/products.json"},
    "WordPress": {"kind": "platform",
                  "html": [r"/wp-content/", r"/wp-includes/"],
                  "oracle": "/wp-json/"},
    "Klaviyo":   {"kind": "app",
                  "html": [r"static\.klaviyo\.com", r"klaviyo\.js"]},
    "Gorgias":   {"kind": "app",
                  "html": [r"config\.gorgias\.chat"]},
    # NEVER add a bare vendor domain like /klaviyo\.com/ -- it matches every page
    # that merely LINKS to the vendor, including every "top 10 tools" blog post.
}

def run(page, oracle_results):
    if page.get("blocked"):
        return {"detected": [], "html_only": [], "evidence": ""}

    body = page.get("body") or ""
    detected, html_only, evidence = [], [], ""

    for name, fp in FINGERPRINTS.items():
        if not any(re.search(p, body, re.I) for p in fp["html"]):
            continue
        if fp["kind"] == "embed":
            continue                       # a Buy Button is not a storefront
        if fp["kind"] == "platform":
            # HTML strings for a platform appear on every agency portfolio, every
            # app-review roundup and every B2B site with an embedded widget.
            # Require an oracle (or a header, if your fetch exposes them).
            if (oracle_results or {}).get(name) is True:
                detected.append(name)
                evidence = evidence or fp.get("oracle", "")
            else:
                html_only.append(name)     # -> "unconfirmed", NOT a negative
        else:
            detected.append(name)

    return {"detected": detected, "html_only": html_only, "evidence": evidence}
```

## Node 5 — verdict

```python
def run(page, match, target_tech):
    t = (target_tech or "").strip().lower()
    if not t:
        # Erroring is correct. Silently grading every row against a default
        # technology produces a plausible, entirely wrong list.
        raise ValueError("target_tech is required per row")

    if page.get("blocked"):
        return {"tech_confirmed": False, "tech_confidence": "blocked",
                "blocked_reason": page.get("blocked_reason", ""),
                "tech_stack_verified": [], "tech_evidence": ""}

    # EXACT element match. "Shopify Buy Button".includes("Shopify") is true, and
    # that is exactly how a B2B software company gets a storefront clause.
    confirmed = any(str(x).strip().lower() == t for x in match["detected"])
    unconf    = any(str(x).strip().lower() == t for x in match["html_only"])

    return {
        "tech_confirmed":      confirmed,
        "tech_confidence":     "high" if confirmed else ("unconfirmed" if unconf else "negative"),
        "tech_stack_verified": match["detected"],
        "tech_evidence":       match["evidence"],
        "blocked_reason":      "",
    }
```

**`blocked`, `unconfirmed` and `negative` are three different answers.** Collapse them to a boolean
and you lose the ability to tell "we could not look" from "we looked and it is not there".

## Nodes 6 and 7 — the clause, OPT-IN

Skip by default. If requested: the §4 prompt byte-identical as the system message, JSON mode,
`reasoning_effort` low, routed on `tech_confirmed == true`. Then a code node running the post-guards
— **a prompt rule is a request, a regex is a guarantee.**

**No verifier model call.** The claim is grounded in a live fetch of the company's own site seconds
earlier, which is a stronger guarantee than an LLM judge.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: tech on website" | jq -r '.id')
# create nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "tech-on-website" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"bombas.com","target_tech":"Shopify"},
  {"domain":"basecamp.com","target_tech":"Shopify"}
]}'
```

Expected: the first confirmed, the second `negative`. If the second comes back confirmed, your
fingerprint is matching a link rather than an installation.

## Smoke test

| What you see | What it means |
|---|---|
| Node 2 returns `body: {}` | you used `http-api-v2` on an HTML page. Use `scrape-website` |
| A bot-walled domain reports `negative` | node 3 is not running, or `body_too_small` is missing |
| Agency portfolios come back confirmed | node 4 is not requiring oracle evidence for platform hits |
| Everything confirmed | the fingerprint is matching a bare vendor domain |
| ~90% of a provider list survives | the gate is not running. Expect ~60% |
