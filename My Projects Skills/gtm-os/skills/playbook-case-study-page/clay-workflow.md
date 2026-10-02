# Clay workflow build: Case-Study Page Name-Drop

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This ports well to a workflow: the ten-path sweep is a loop, the five gates are code, and the clause
assembly is code. The table version needs ten HTTP columns to express what one node does here.

## Graph

```
[1 trigger: domain + company_name]
   -> [2 code: normalize + build the ten candidate URLs]
   -> [3 tool: probe them, keep the first that resolves]   <- soft-404 guard
   -> [4 tool: scrape-website]
   -> [5 agent: pick ONE customer]
   -> [6 code: five verbatim gates + line assembly + ship gate]
```

## Node 2 — normalize and build candidates

```python
PATHS = ["/customers", "/case-studies", "/customer-stories", "/success-stories",
         "/case-study", "/clients", "/our-work", "/portfolio", "/testimonials", "/stories"]

def run(domain):
    d = (domain or "").strip().lower()
    for p in ("https://", "http://"):
        if d.startswith(p):
            d = d[len(p):]
    d = d.replace("www.", "").split("/")[0].rstrip("/")
    if not d:
        return {"candidates": [], "domain": ""}
    # TEN paths, not four. One live-test hit came from /testimonials, the NINTH
    # path. A four-path build loses every row of that class to a paid fallback,
    # which is both worse and more expensive.
    return {"candidates": ["https://%s%s" % (d, p) for p in PATHS], "domain": d}
```

## Node 3 — probe, with the soft-404 guard

Send a **browser User-Agent** on every request, or CDN-fronted prospect sites read as *missing*
rather than as *blocked*. Fall back to `GET` with `Range: bytes=0-4095` when HEAD is refused, and
accept any **2xx** (a compliant origin answers **206**).

Accept a candidate only when:

1. the final status is 2xx, **and**
2. the final resolved path is **not `/`**, **and**
3. the final resolved path still matches a case-study-shaped pattern.

Rule 2 is the soft-404 guard: many origins 302 unknown paths to `/` and return 200, so **"it
resolved" is not the same as "the page exists".**

**Politeness: concurrency 2 per origin, never above about 4.** These are the web servers of companies
you want to sell to. A global cap is a blast-radius control on your own egress and can be higher —
and note **throughput is fetch-bound**, so raising model concurrency alone does nothing.

## Node 4 — fetch and flatten

⚠️ **`scrape-website`, not `http-api-v2`.** `http-api-v2` parses responses as JSON and returns
`body: {}` on HTML.

Flatten with one non-obvious rule: **keep `<img alt>` text as `[logo: X]`.** On logo-wall pages the
alt text is the only place the customer name exists. Cap at ~18,000 characters, which is what the
tested prompt uses.

If the flattened text is under 200 characters, the page is JS-rendered — escalate **that row only** to
a rendering proxy.

## Node 5 — the picker

The §6 prompt byte-identical as the system message. **Minimal reasoning effort** — without it this
exact prompt returned `finish_reason=length` with **empty content on 6 of 6 rows.** JSON mode, cap
1200, no `temperature`. Retry on `length`; **never record it as an abstain.**

**The model picks and quotes. It never writes the sentence.** Node 6 assembles it.

## Node 6 — gates, assembly, ship decision

```python
import re

PLACEHOLDER = {"startup","university","company","partner","client","customer","logo",
               "brand","enterprise","business","organization","team"}
BAD_CTX  = ("investor","backed by","our investors","press","featured in","as seen in",
            "partner","integrations","works with","media")
GOOD_CTX = ("customer","client","case stud","success stor","testimonial","story")
DANGLING = {"back","up","out","on","of","to","in","with","for"}
VERBS    = {"is","are","was","were","has","have","helps","helped","cut","cuts",
            "saved","saves","unified","unifies","centralizes","centralises"}

def run(ai, page_text, url):
    a = ai or {}
    name  = (a.get("client_name") or "").strip()
    quote = (a.get("evidence_quote") or "").strip()
    conf  = a.get("confidence", "low")
    text  = (page_text or "").lower()

    def out(line, reason, verified=False, ship=False):
        return {"case_study_line": line, "client_name": name if verified else "",
                "case_study_url": url if verified else "", "evidence_quote": quote if verified else "",
                "confidence": conf, "verified": verified, "ship_ready": ship,
                "reject_reason": reason}

    if not name or not quote:
        return out("", "empty")

    # 1-3: the string is really on the page and the quote really contains the name.
    if name.lower()  not in text: return out("", "name-not-on-page")
    if quote.lower() not in text: return out("", "quote-not-on-page")
    if name.lower() not in quote.lower(): return out("", "quote-missing-name")

    # 4: CMS placeholders. A real captured page served [logo: University] beside
    # real customers, and "Saw your work with University." passed checks 1-3.
    if name.lower() in PLACEHOLDER:
        return out("", "placeholder-name")

    # 5: non-customer context. Investor walls, press strips and integration grids
    # sit on the SAME page and all pass a substring check. Checks 1-3 prove the
    # string is ON the page; they do NOT prove the entity is a CUSTOMER.
    i   = text.find(name.lower())
    win = text[max(0, i - 600):i]
    if any(b in win for b in BAD_CTX) and not any(g in win for g in GOOD_CTX):
        return out("", "non-customer-context")

    # Assemble in CODE. Asking the model to write the sentence produced lowercased
    # proper nouns, ungrammatical clauses, and a percentage copied out of a
    # few-shot example onto an unrelated company.
    d = (a.get("detail_phrase") or "").strip()
    w = [x for x in d.lower().split() if x]
    grounded = (d and all(x in quote.lower() for x in w)
                and d.lower() != name.lower()
                and w and w[-1] not in DANGLING
                and not any(x in VERBS for x in w)
                and conf == "high")          # a low row NEVER carries a topic

    line = "your work with " + name + ((" on " + d) if grounded else "")
    if len(line.split()) > 16:
        line = "your work with " + name

    # A low-confidence row is a BARE LOGO with no story -- the exact shape an
    # investor, press, partner and placeholder logo all take. It is verified but
    # HELD for a human, not shipped.
    return out(line, "", verified=True, ship=(conf == "high"))
```

Give every terminal path a node with this same `outputSchema`.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: case study page" | jq -r '.id')
# create the 6 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "case-study" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"ramp.com","company_name":"Ramp"},
  {"domain":"chipotle.com","company_name":"Chipotle"}
]}'
```

The second should abstain. **That is a correct answer, not a failure.**

## Smoke test

| What you see | What it means |
|---|---|
| 100% "no page found" from a workflow that works by hand | the browser User-Agent is missing on node 3 |
| Pages "found" on companies that obviously have none | the soft-404 guard is missing — the origin 302s to `/` and returns 200 |
| Node 4 returns `body: {}` | you used `http-api-v2` on HTML |
| Logo-wall pages yield nothing | node 4 is dropping `<img alt>` text |
| All lines empty | node 5's reasoning effort is not minimal |
| A generic word ships as a customer | the placeholder gate is missing |
| Two runs name different customers | **expected.** Any named customer is valid. Cache the first accepted value if you need determinism |
