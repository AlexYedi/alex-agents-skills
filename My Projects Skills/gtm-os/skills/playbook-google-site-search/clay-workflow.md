# Clay workflow build: Google `site:` Keyword Filter

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

**This ports better to a workflow than to a table**, for one specific reason: the table version has a
formula dependency cycle that forces an extra column, and code nodes have no such constraint. You can
sanitize, guard and gate in one node.

⚠️ **Do step 0 in `SKILL.md` §5 first.** Run the query by hand for 3 to 5 real domains and read the
results.

## Graph

```
[1 trigger: domain + keyword]
   -> [2 code: build the query]
   -> [3 tool: http-api-v2, the SERP call]
   -> [4 code: literal filter + host exclusions]   <- THE CREDIT GATE
   -> [5 agent: the judge]
   -> [6 code: sanitize + guards + gate + pre-render]
```

## Node 2 — build the query

```python
def run(domain, keyword):
    d = (domain or "").strip().lower().replace("https://", "").replace("http://", "")
    d = d.replace("www.", "").split("/")[0]
    k = (keyword or "").strip()
    if not d or not k:
        return {"query": "", "domain": d, "keyword": k}
    # ONE keyword, ONE query. An OR chain drops precision from 100% to 40% and
    # destroys attribution: one response for seven keywords cannot tell you which
    # one matched.
    return {"query": 'site:%s "%s"' % (d, k), "domain": d, "keyword": k}
```

## Node 3 — the SERP call

`http-api-v2` is correct here: a SERP API returns **JSON**, not HTML.

⚠️ **Percent-encode the query.** Raw quotes and colons in a URL get rejected, and the failure often
surfaces as a 400 or a 431 rather than anything that names the real cause. The sandbox has no
`urllib`, so hand-roll it in node 2 if your action does not encode for you.

`automapInputs: false`. Headers as `{"type":"map",...}`, never a JSON string. Pin `query` from node 2.

Also check your provider's response shape: a "light" endpoint often returns a flat array while the
full endpoint nests results a level deeper, and **parsing one like the other silently returns zero
rows** rather than erroring.

## Node 4 — the literal filter (this is the credit gate)

```python
import re

BAD_HOSTS = ("community.", "forum.", "forums.", "discuss.", "answers.",
             "feedback.", "ideas.", "status.", "help.")

def _norm(s):
    return re.sub(r"[\s\-]+", " ", (s or "").lower()).strip()

def run(search, keyword, domain):
    results = (search or {}).get("data") or []
    k_norm  = _norm(keyword)
    k_tight = k_norm.replace(" ", "")

    kept = []
    for r in results:
        url = (r.get("url") or "")
        host = url.split("//")[-1].split("/")[0].lower()

        # Subdomain exclusions: site: includes subdomains, and community/forum
        # subdomains are USERS talking, not the company. A stale forum answer
        # outranked one company's own current security page.
        if host.startswith(BAD_HOSTS):
            continue

        text = _norm((r.get("title") or "") + " " + (r.get("snippet") or ""))
        # Accept the normalized form OR the space-free form, so "SOC 2" also
        # matches "soc-2" and "SOC2". A plain contains silently drops SOC2.
        if k_norm in text or k_tight in text.replace(" ", ""):
            kept.append({"title": r.get("title",""), "url": url,
                         "snippet": r.get("snippet","")})

    # Search engines do NOT strictly honor quoted phrases on site: queries.
    # One query returned 10 results, zero containing the phrase, all matching an
    # unrelated company that shared the letters. This filter is what stops that
    # reaching the model, and it short-circuited 3 of 10 rows in the live test.
    return {"results": kept[:5], "has_literal": bool(kept)}
```

Route node 5 on `has_literal`.

## Node 5 — the judge

- **System prompt:** the block from `SKILL.md` §6, byte-identical — it measures ~1,030 tokens, just
  over the caching floor, so **do not interpolate row data into it.**
- **User message:** `domain=... keyword=... results=[...]`.
- **`reasoning_effort: minimal`** — load-bearing. Without it, `finish_reason=length` with empty
  content on **2 of 10 rows**, and latency of 17.6s instead of 1.1s.
- JSON mode on. Token cap 1200.

## Node 6 — sanitize, guard, gate, pre-render

One node does what the table needs four columns for.

```python
import re

LEAD = re.compile(r"^\s*(i\s+noticed|noticed|that)\b[:,]?\s*", re.I)

def sanitize(line, domain):
    v = LEAD.sub("", line or "").strip()          # the model prepends the frame on
                                                  # ~3 of 10 rows despite an explicit
                                                  # prompt rule. A regex, not a rule.
    v = v.rstrip(". ").replace("—", ",").replace("–", ",").replace('"', "").strip()
    if not v:
        return ""
    first = v.split()[0]
    root  = (domain or "").split(".")[0]
    # Lowercase the first letter ONLY for ordinary words. Skip acronyms (SOC),
    # internal capitals (HubSpot) and the company's own name.
    ordinary = not (first.isupper() or any(c.isupper() for c in first[1:])
                    or first.lower() == root)
    if ordinary:
        v = v[0].lower() + v[1:]
    return v

def run(judge, filtered, domain, error=None):
    # An ERROR is never an abstain. A rate limit, a 5xx, an empty judge cell or an
    # exhausted truncation retry must be re-run -- silently converting it to
    # "no signal" produced a wrong abstain on a company that DOES mention the keyword.
    if error or (filtered.get("has_literal") and not judge):
        return {"site_keyword_status": "error", "campaign_usable": False,
                "site_keyword_line": "", "site_keyword_sentence": "",
                "site_keyword_hit": "", "site_keyword_url": "", "confidence": "low"}

    j = judge or {}
    line = sanitize(j.get("line", ""), domain)

    # A hit needs all three. One live row returned mentions:true with status:"none"
    # and an empty line, which without the third clause renders "Noticed ." into a
    # live email.
    hit = bool(j.get("mentions")) and j.get("status") != "none" and bool(line)

    # THE GATE, computed BEFORE the copy fields. Stricter than "hit" on purpose:
    # a judge once wrote "you passed your SOC 2 audit on the first try" from a
    # sentence inside an EXAMPLE COLD EMAIL printed on the company's own marketing
    # page. mentions was true. The company had passed no such audit.
    usable = hit and j.get("status") == "has" and j.get("confidence") == "high"

    return {
        "site_keyword_hit":      "yes" if hit else "",
        "site_keyword_status":   j.get("status", "none"),
        "site_keyword_url":      j.get("evidence_url", "") if hit else "",
        "confidence":            j.get("confidence", "low"),
        "campaign_usable":       usable,
        "site_keyword_line":     line if usable else "",
        # The WHOLE sentence, period and one trailing space, or "". Spintax cannot
        # branch on emptiness, so the emptiness has to be baked into the value.
        "site_keyword_sentence": ("Noticed " + line + ". ") if usable else "",
        "judge_line_raw":        j.get("line", ""),   # audit only. NEVER pushed.
    }
```

`judge_line_raw` is returned deliberately — it is how you audit a suppressed row later. **It is
populated on rows that failed the gate, so it must never reach a sequencer.**

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: site keyword filter" | jq -r '.id')
# create the 6 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "site-keyword" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"linear.app","keyword":"SOC 2"},
  {"domain":"patagonia.com","keyword":"SOC 2"}
]}'
```

The second row should come back with `campaign_usable: false`. If it comes back usable, your literal
filter is not running — that domain is the one that returned 10 results matching an unrelated
company.

## Before you wire the output into an email

Use `site_keyword_sentence` **alone on its own line, with no frame text around it.** Do not wrap it
in spintax, and do not build the frame yourself around `site_keyword_line`.

## Smoke test

| What you see | What it means |
|---|---|
| Node 5 runs on every row | node 4's `has_literal` is not gating |
| `Noticed Noticed ...` | node 6's leading-frame regex is missing |
| `Noticed .` | the three-clause hit guard lost its line-is-not-empty term |
| Everything usable | the keyword is too generic to filter on |
| Empty judge, counted as no-signal | the error branch in node 6 is missing. **Re-run those rows** |
| `finish_reason=length` | reasoning effort is not minimal |
| Node 3 returns 400/431 | the query was not percent-encoded |
