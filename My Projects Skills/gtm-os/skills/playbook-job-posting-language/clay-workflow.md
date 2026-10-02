# Clay workflow build: Job Posting Language

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

A workflow has one real advantage over the table here: **an agent node lets you set reasoning effort
and a completion-token cap**, which a native AI column does not. That means you can run the cheaper
nano-class model correctly instead of being forced onto a mini-class model.

Relevant catalog actions:

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | .actionKey' | grep -iE 'job'
# cpj-find-lists-of-jobs, enrich-job, leadmagic-find-jobs, apollo-oauth-find-company-jobs ...
clay workflows actions schema <packageId> <actionKey> | jq '.inputParameters'
```

## Graph

```
[1 trigger: domain + company_name + keywords]
   -> [2 tool: domain -> company profile]
   -> [3 code: NAME-MATCH GATE]
   -> [4 tool: jobs query, keywords filtered SERVER-SIDE]
   -> [5 code: dedupe + shape the postings]
   -> [6 agent: write the clause]
   -> [7 code: freshness gate + output contract]
```

## Node 3 — the name-match gate

```python
import re

def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def run(profile, company_name):
    want = _norm(company_name)
    got  = _norm((profile or {}).get("company_name"))
    # A domain -> company-profile resolution can land on a DIFFERENT company, and
    # every posting after that point is about the wrong business. This gate is
    # mandatory, not a nicety.
    ok = bool(want and got and (want in got or got in want))
    return {"name_match": "pass" if ok else "fail",
            "profile_url": (profile or {}).get("url", "") if ok else ""}
```

## Node 4 — the jobs query

⚠️ **Put the keywords in the request, not in your own post-filter.**

Most jobs APIs return `title`, `date_posted`, `url` and a summary — **but never the full description.**
The description is reachable **only through the filter.** Measured on the same 8 companies with the
same 8 keywords: scanning returned fields matched **1 of 8**; the identical keywords passed to the
description filter matched **5 of 8**.

```jsonc
{
  "company_linkedin_url": "<from node 3>",
  "job": {
    "date_posted": { "last_days": 60 },
    "description": { "include": ["cold call", "cold calls", "cold calling",
                                 "cold outreach", "cold email", "cold emails",
                                 "outbound prospecting", "outbound calls"] }
  },
  "max_results": 25
}
```

Two traps:

- **Unknown keys are silently stripped** and you get an unfiltered result set that looks successful.
  If a filter appears to do nothing, you spelled it wrong. Compare counts with and without it.
- **Matching is on whole phrase tokens, not substrings.** `cold call` returned **996** matches while
  `cold calling` returned **2,065** — under substring matching the shorter phrase would be the larger
  set. And `coldcall` returns **0**. **Enumerate plural and gerund forms yourself.**

`automapInputs: false`. Object-valued params as `{"type":"map",...}`. Browser User-Agent.

## Node 5 — dedupe and shape

```python
def run(response, max_keep=5):
    seen, out = set(), []
    for j in ((response or {}).get("jobs") or []):
        key = (j.get("title", ""), j.get("url", ""))
        if key in seen:
            continue
        seen.add(key)
        out.append({"title": j.get("title", ""), "url": j.get("url", ""),
                    "date_posted": j.get("date_posted", "")})
        if len(out) >= max_keep:
            break
    return {"postings": out, "has_postings": bool(out)}
```

Route node 6 on `has_postings`.

## Node 6 — the line writer

- **System prompt:** the block from `SKILL.md` §6, byte-identical.
- **User message:** `Company: <domain> | Postings: <postings JSON>`.
- **`reasoning_effort: "low"`, `max_completion_tokens: 2500`**, no `temperature`, JSON mode.

⚠️ At a 900-token cap with **default** effort, **all 8 generating rows returned
`finish_reason=length` with empty content**, and both retries failed identically. Note how that hides:
**rows with nothing to say still succeeded, so the abstains looked healthy and only the rows worth
having died.**

Retry on `length`. Retry transport errors **separately, with backoff** — they are not verdicts either.

## Node 7 — freshness gate and contract

```python
import time

def _days_since(iso):
    if not iso:
        return 9999
    t = time.strptime(iso[:10], "%Y-%m-%d")     # no datetime in this sandbox
    return (time.mktime(time.gmtime()) - time.mktime(t)) / 86400.0

def run(ai, postings):
    a    = ai or {}
    line = (a.get("job_posting_line") or "").strip()
    url  = a.get("evidence_url", "")
    date = next((p.get("date_posted", "") for p in (postings or []) if p.get("url") == url), "")

    # Detect on 60 days, CLAIM on 30. A date_posted is when the provider OBSERVED
    # the posting, not proof the job is live. One live-test row quoted a 53-day-old
    # posting already gone from the company's own board.
    # This is a formula, not a model call, and it is the field copy binds to.
    fresh = bool(line) and _days_since(date) <= 30

    return {
        "job_posting_line_safe": line if fresh else "",   # <- push THIS
        "job_posting_line":      line,                    # audit only
        "job_role_named":        a.get("role_named", ""),
        "job_evidence_url":      url,
        "job_posted_date":       date,
        "job_confidence":        a.get("confidence", "low"),
    }
```

Give every terminal path a node with this same `outputSchema`.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: job posting language" | jq -r '.id')
# create the 7 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "job-posting-line" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"gong.io","company_name":"Gong",
   "keywords":["cold call","cold calling","outbound prospecting"]}
]}'
```

## Before you add an AI classifier

Run the recall measurement in `SKILL.md` note C first — three API calls plus a 25-row sample, well
under a cent.

| Measured recall | Do this |
|---|---|
| ≥90% | **keywords only.** No AI column |
| 60-90% | add the classifier **behind a gate on the missed rows** |
| <60% | **your keyword set is wrong. AI will not save it** |

## Smoke test

| What you see | What it means |
|---|---|
| Postings returned but never matching your keywords | you are filtering client-side. **1 of 8 vs 5 of 8** |
| A filter appears to do nothing | an unknown key was silently stripped |
| Postings for a different company | node 3's name-match gate is missing |
| Empty lines on exactly the rows with postings | node 6's reasoning effort is not low |
| Copy references a dead role | you pushed the ungated line instead of the `_safe` one |
| `ModuleNotFoundError: datetime` | use `time.strptime` |
