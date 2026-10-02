# Clay workflow build: Company Social Link Finding

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This is a good workflow candidate: the chain is a **precedence ladder**, and a code node expresses a
ladder far better than six columns and a pile of run conditions.

Relevant actions:

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | "\(.packageId)\t\(.actionKey)"' \
  | grep -iE 'scrape-website|enrich-company|find-company-linkedin|social'
```

## Graph

```
[1 trigger: domain]
   -> [2 tool: enrich-company]              candidates, weak evidence
   -> [3 tool: scrape-website]              SELF-ATTESTED, strongest evidence
   -> [4 code: blocked check + extract profile links]
   -> [5 tool: rendering proxy]             only when 4 says blocked
   -> [6 tool: SERP, per still-empty platform]
   -> [7 agent: ownership verifier]         ONLY on weak candidates
   -> [8 code: precedence ladder + X exception + contract]
```

## Node 3 — the site fetch

⚠️ **`scrape-website`, not `http-api-v2`.** The latter parses responses as JSON and returns
`body: {}` on HTML.

Walk the ladder: `https://<d>`, `https://www.<d>`, `http://<d>`, then `/contact`, `/about`,
`/contact-us` on whichever origin answered. Browser User-Agent, follow redirects.

**This is the strongest evidence in the whole chain** — a link in the company's own footer is
self-attested ownership — and it is the **only** source that finds TikTok.

## Node 4 — blocked check and link extraction

```python
import re

CHALLENGE = ("just a moment", "checking your browser", "enable javascript and cookies",
             "attention required", "verifying you are human")

PATTERNS = {
  "linkedin":  r"linkedin\.com/company/([A-Za-z0-9._-]+)",
  "x":         r"(?:twitter|x)\.com/([A-Za-z0-9_]{1,15})(?![A-Za-z0-9_])",
  "facebook":  r"facebook\.com/([A-Za-z0-9.]+)",
  "instagram": r"instagram\.com/([A-Za-z0-9._]+)",
  "youtube":   r"youtube\.com/(?:c/|@|channel/|user/)([A-Za-z0-9._-]+)",
  "tiktok":    r"tiktok\.com/@([A-Za-z0-9._]+)",
}
# Slugs that are never a company profile.
JUNK = {"sharer","plugins","tr","profile.php","groups","photo.php","posts","videos",
        "p","reel","explore","discover","popular","playlist","hashtag","search",
        "intent","share","home","login"}

def run(html, status, domain):
    body = (html or "")
    low  = body.lower()
    # A bot interstitial is commonly served with HTTP 200, yields zero matches, and
    # otherwise looks exactly like a clean legitimate miss. Checking the STATUS alone
    # records a whole segment of blocked sites as "no social accounts".
    blocked = (status in (403, 429)) or len(body) < 2000 or any(c in low for c in CHALLENGE)
    if blocked:
        return {"blocked": True, "links": {}}

    body = body.replace("\\/", "/")     # frameworks embed footer links inside JSON
    root = (domain or "").split(".")[0].lower()
    links = {}
    for platform, pat in PATTERNS.items():
        cands = [m for m in re.findall(pat, body, re.I) if m.lower() not in JUNK]
        if not cands:
            continue
        # PICK THE BEST MATCH ON THE PAGE, NEVER THE FIRST ONE. Sites link the parent
        # group, partners and staff profiles in the same footer as their own account.
        cands.sort(key=lambda s: (root not in s.lower(), len(s)))
        links[platform] = cands[0]
    return {"blocked": False, "links": links}
```

## Node 7 — the ownership verifier

The §6 prompt byte-identical. `max_completion_tokens=2500` (a measured floor — below it a reasoning
model truncates), JSON mode, no `temperature`.

**Route it only over weak candidates**: values from the company record and from search. **Site-derived
values skip it entirely** — they are self-attested, and paying to verify them is pure waste.

## Node 8 — the precedence ladder

```python
PLATFORMS = ["linkedin", "x", "facebook", "instagram", "youtube", "tiktok"]
BASE = {"linkedin": "https://www.linkedin.com/company/%s",
        "x":         "https://x.com/%s",
        "facebook":  "https://www.facebook.com/%s",
        "instagram": "https://www.instagram.com/%s",
        "youtube":   "https://www.youtube.com/@%s",
        "tiktok":    "https://www.tiktok.com/@%s"}

def run(site, record, search, verdicts):
    out = {}
    for p in PLATFORMS:
        # 1. Company-site evidence wins outright and needs no verification.
        slug = (site.get("links") or {}).get(p)
        if slug:
            out["company_%s_url" % p] = BASE[p] % slug
            out["company_%s_evidence" % p] = "company_site"
            continue

        # 2. X STOPS HERE. X handles are short, recycled and squatted: a search for
        #    one brand returned a handle that matched the brand BETTER than the real
        #    account did, and was titled "Bug Poc". No verifier catches that, because
        #    the handle genuinely does look right.
        if p == "x":
            out["company_x_url"] = ""
            out["company_x_evidence"] = ""
            continue

        # 3. Everything else may come from a weak source, but only through the verifier.
        for src, url in (("company_record", (record or {}).get(p)),
                         ("search",        (search or {}).get(p))):
            v = (verdicts or {}).get(url or "")
            if url and v and v.get("owned") is True:
                out["company_%s_url" % p] = v.get("canonical_url") or url
                out["company_%s_evidence" % p] = src
                break
        else:
            out["company_%s_url" % p] = ""
            out["company_%s_evidence" % p] = ""
    return out
```

**Always return the evidence field beside the URL.** Six months later it is the only way to tell a
self-attested link from a scraped search result — and that difference decides whether it is safe to
scrape behind.

## If you backfill the company-record step in bulk

⚠️ A company-search endpoint that accepts an array of domains may still be **hard-paginated at 25
results per page with no page-size parameter.** Posting 35 domains returned **25 results** and
`"total_page": 2`.

**A 500-domain body returns 25 matches and silently drops ~475.** Chunk to the page size **and** loop
pages. Read the pagination block on your first call.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: social link finding" | jq -r '.id')
# create the 8 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "social-links" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{"domain":"clay.com"}]}'
```

## Smoke test

| What you see | What it means |
|---|---|
| Node 3 returns `body: {}` | you used `http-api-v2` on HTML |
| A bot-protected site reports no accounts | node 4's challenge-page check is missing |
| Footer links missing on obviously social brands | the `\/` un-escape is missing |
| An X handle you cannot find on the company's own site | the X exception in node 8 is not wired |
| A parent brand's profile instead of the company's | node 4 is taking the first match instead of the best |
| The verifier truncates | raise the cap to 2500 |
| The verifier runs on every candidate | it should skip site-derived values entirely |
