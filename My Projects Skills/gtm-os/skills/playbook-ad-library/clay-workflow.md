# Clay workflow build: Meta Ad Library

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This playbook ports to a workflow **better than most**, because its whole chain is HTTP calls and
deterministic string work — exactly what workflow nodes are good at. The one thing that gets harder
is best-of-3 drafting, which needs three agent nodes fanning into one picker.

The relevant action is `apify-run-actor` (package prefix `ea91b0b8`), or plain `http-api-v2`
against the Apify REST API. Check the schema before wiring:

```bash
clay workflows actions schema ea91b0b8-6c78-4d32-a978-345e923bdc93 apify-run-actor | jq '.inputParameters'
```

## Graph

```
[1 trigger: domain + company_name]
   -> [2 tool: cache lookup]            -> short-circuit on a fresh hit
   -> [3 tool: scrape-website]
   -> [4 code: extract + junk-filter the slug]
   -> [5 tool: SERP site:facebook.com]   (only when 4 found nothing)
   -> [6 code: THE THREE GATES]
   -> [7 code: assemble fb_page_url]
   -> [8 tool: apify-run-actor, onlyTotal]
   -> [9 code: count, volume phrase, ad samples]
   -> [10a/10b/10c agents: three drafts]
   -> [11 code: lint + ungrounded words, pick first passing]
   -> [12 agent: truth judge]
   -> [13 code: final output contract]
   -> [14 tool: cache write]
```

## Node 3 — fetch the site

⚠️ **Use `scrape-website`, not `http-api-v2`.** `http-api-v2` parses responses as JSON, so an HTML
response comes back as `body: {}` and you get nothing. This is the single most common way this
node is built wrong.

## Node 4 — extract the slug

```python
import re

JUNK = {"sharer","plugins","tr","profile.php","groups","photo.php","posts","videos","people","pg"}

def run(html):
    # Load-bearing: modern frameworks embed footer links inside JSON as
    # https:\/\/facebook.com\/ridge  -- un-escape BEFORE the regex or you lose 38% of free hits.
    body = (html or "").replace("\\/", "/")
    m = re.search(r"https?://(?:www\.)?facebook\.com/([A-Za-z0-9._-]+)", body)
    slug = m.group(1) if m else ""
    return {"slug": "" if slug in JUNK else slug}
```

## Node 6 — the three gates

The most important node in the workflow. All three gates are load-bearing.

```python
import re

def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def run(serp_results, company_name, domain):
    label = norm((domain or "").split(".")[0])   # second-level label
    want  = norm(company_name)

    for r in (serp_results or []):
        url   = r.get("url", "") or ""
        title = r.get("title", "") or ""

        m = re.match(r"https?://(?:www\.)?facebook\.com/([^/?#]+)/?$", url)
        if not m:
            continue                      # GATE 1: exactly one path segment.
                                          # Rejects /JohnDaly/videos/... -- somebody else's
                                          # page talking about the brand.

        slug = norm(m.group(1))

        if want not in norm(title):
            continue                      # GATE 2: title contains the company name.

        if not (slug.startswith(label) or label.startswith(slug)):
            continue                      # GATE 3: THE SLUG, and only the slug.
                                          # The title is whatever the page owner typed;
                                          # the slug is the page identity. Dropping this
                                          # gate is how a pottery studio got billed for
                                          # a query about "Clay".

        return {"fb_page_url": "https://www.facebook.com/" + m.group(1)}

    return {"fb_page_url": ""}             # abstain. A wrong page costs the same as a right one.
```

**Never re-add a title escape hatch.** A patch that also accepted a title-first-segment match let
an unrelated creative agency through, because its title began with the target word.

## Node 8 — the paid call

| Setting | Value |
|---|---|
| action | `apify-run-actor` (or `http-api-v2` to the Apify REST API) |
| actor | `apify/facebook-ads-scraper` |
| input | `{"startUrls":[{"url":"<fb_page_url>"}],"onlyTotal":true,"activeStatus":"active"}` |
| `automapInputs` | **`false`** |
| run condition | verified page **and** cache miss |

⛔ **`"onlyTotal": true` is mandatory.** Omit it and billing switches from **1 item per page** to
**1 item per ad**, which is roughly an 8x bill on a page with 8 ads and far worse on a big
advertiser. Read the charged-event count back after every run and confirm it equals the page count.

Wrap this node's retries: one unhandled transient socket error after the paid call goes out means
**money spent and nothing returned**, which is the worst failure shape there is. Retry with
exponential backoff, and treat an errored row as a retry candidate, never an abstain.

## Node 9 — count, volume phrase, samples

```python
import re

TOKEN = re.compile(r"\{\{[^}]+\}\}")

def run(apify):
    items = apify or []
    first = items[0] if items else {}
    count = first.get("totalCount") or 0

    ads, seen = [], set()
    for a in (first.get("results") or []):
        title = (a.get("title") or "").strip()
        body  = (a.get("body")  or "").strip()
        # Dynamic catalog ads store the TEMPLATE, not the copy. Drop them before
        # the model ever sees them.
        if TOKEN.search(title) and TOKEN.search(body):
            continue
        key = (title, body)
        if key in seen:
            continue                      # totalCount collates near-duplicates
        seen.add(key)
        ads.append('[id %s | title "%s" | body "%s"]' % (a.get("adArchiveID",""), title, body))
        if len(ads) == 4:
            break

    return {
        "active_ad_count": count,
        # Any rule with a NUMBER in it lives in code, never in the model.
        "volume_phrase": "allowed" if count >= 50 else "banned",
        "ad_samples": " ".join(ads),
    }
```

## Nodes 10a-c — three drafts

Three agent nodes with the identical system prompt from `SKILL.md` §6, byte-identical, and the same
per-row message. Reasoning effort minimal, JSON mode on.

Fan-in to node 11 is safe: a node with several incoming edges fires on **first arrival**, and pins
from branches that did not run resolve as absent rather than blocking.

If you want to keep this cheap, run one draft and accept the ~2-in-3 per-draft usable rate, with
node 11 blanking the failures.

## Node 11 — lint and grounding

Port the whole guard stack from `SKILL.md` §6. The free ungrounded-words check runs **first**,
because on the "named a product the ads never mentioned" failure it is both cheaper *and* more
reliable than the judge.

```python
import re

def content_words(s):
    return {w[:4] for w in re.findall(r"[a-z]{4,}", (s or "").lower())}

def lint(line, ad_text, brand_tokens, volume_phrase):
    v = (line or "").strip()
    if not v:                                     return ""
    low = v.lower()
    if re.match(r"^(noticed|saw|seeing|and|,)", low):        return ""
    if any(c in v for c in '"’—–™®*'): return ""
    if "angle" in low:                                        return ""
    if len(v.split()) > 20:                                   return ""
    if v.endswith(".") or v[0].isupper():                     return ""
    if low.count(",") >= 2 or low.split().count("and") >= 2:  return ""
    if volume_phrase == "banned" and re.search(r"\ba lot of ads\b", low): return ""
    if any(t in low for t in brand_tokens):                   return ""
    words = re.findall(r"[a-z]{5,}", low)
    if len(words) != len(set(words)):                         return ""
    # Grounding: every content word must appear in the ad text.
    if content_words(v) - content_words(ad_text):             return ""
    return v
```

Add your own banned-word list on top — a generated merge field is prospect-visible copy and is
bound by the same spam list as hand-written copy.

## Node 12 — truth judge

**Mandatory, 100% of lines that survived node 11, never a sample.** ~$0.02 per 10,000 rows.
Input is the ad samples and the linted line; output is `{"supported": bool, "why": "..."}`.

An earlier version of this playbook argued a judge was unnecessary because every claim is copied
from ad text the same call is looking at. That was **wrong twice in one graded run**. Structural QC
cannot catch semantic error.

## Node 13 — output contract

```python
def run(line, judge, meta, page_url, ai):
    v = line if (judge or {}).get("supported") is not False else ""
    return {
        "ad_library_line": v,
        "ad_theme":        (ai or {}).get("ad_theme", ""),
        "evidence_ad_id":  (ai or {}).get("evidence_ad_id", "") if v else "",
        # The model key is `confidence`; the rename to ad_confidence happens HERE.
        "ad_confidence":   ((ai or {}).get("confidence") or "low") if v else "low",
        "active_ad_count": meta.get("active_ad_count", 0),
        "fb_page_url":     page_url or "",
    }
```

Every terminal path needs its own node with this same `outputSchema`.

## Node 14 — cache write

Upsert on bare domain, **including abstains**. Set `removeNull: true` so an empty field does not
overwrite a good cached row with a blank.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: meta ad library" | jq -r '.id')
# create nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows diagram "$WF"
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "ad-library" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{"domain":"smartlead.ai","company_name":"Smartlead"}]}'
```

## Smoke test

| What you see | What it means |
|---|---|
| Node 3 returns `body: {}` | you used `http-api-v2` on an HTML page. Use `scrape-website` |
| Slug empty on obviously social brands | the `\/` un-escape is missing in node 4 |
| Node 6 passes an unrelated page | a gate is missing, almost always gate 3 |
| Apify charged events >> page count | `onlyTotal` was omitted |
| Lines mention products the ads never named | the grounding check in node 11 is not running before the judge |
| Lines name the prospect's own brand | brand-token lint missing. This was 3 of 4 lines before the fix |
