# Clay workflow build: Name 2 Other Prospects

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

Relevant catalog actions:

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | "\(.packageId)\t\(.actionKey)"' \
  | grep -iE 'find-people|people-at-company'
# 48a31bbb...  prospeo-find-people-at-company
# 303cd8bc...  icypeas-find-people-at-company
```

## Graph

```
[1 trigger: domain + recipient_full_name + recipient_linkedin_url + persona_titles]
   -> [2 code: HARD PRECONDITION -- refuse the row without a recipient name]
   -> [3 tool: find people at company]
   -> [4 code: the exclusions]
   -> [5 agent: the judge]
   -> [6 tool: still-there check]
   -> [7 code: assemble the phrase + contract]
```

## Node 2 — refuse the row, loudly

```python
def run(domain, recipient_full_name):
    # A row with no recipient name CANNOT be excluded, and this variable puts a
    # named human into a stranger's inbox. "Hey John, should I reach out to John?"
    # is the failure this whole playbook exists to prevent, so a missing name is a
    # hard stop, not a soft skip.
    if not (recipient_full_name or "").strip():
        raise ValueError("recipient_full_name is required; refusing to run this row")
    if not (domain or "").strip():
        raise ValueError("domain is required")
    return {"ok": True}
```

Raising is deliberate. A silent skip looks identical to "no colleagues found", and you would never
notice a whole segment running unprotected.

## Node 4 — the exclusions, before the model

```python
import re, unicodedata

def _key(s):
    d = unicodedata.normalize("NFKD", s or "")
    d = "".join(c for c in d if not unicodedata.combining(c))
    parts = [p for p in re.sub(r"[^a-z ]", " ", d.lower()).split() if p]
    # First + last only. Middle names, initials, credentials, "(Pri)" nicknames
    # and ", MBA" must all still collapse to the same key as the recipient.
    return (parts[0] + " " + parts[-1]) if parts else ""

def _url(u):
    return (u or "").strip().lower().rstrip("/")

def run(candidates, recipient_full_name, recipient_linkedin_url, campaign_peers=None):
    me_name = _key(recipient_full_name)
    me_url  = _url(recipient_linkedin_url)
    peers   = {_key(p) for p in (campaign_peers or []) if p}

    kept = []
    for c in (candidates or []):
        k = _key(c.get("name"))
        if not k:
            continue
        if me_name and k == me_name:                 # TIER 1: never name the recipient
            continue
        if me_url and _url(c.get("linkedin_url")) == me_url:
            continue
        if k in peers:                               # TIER 2: never name a campaign peer
            continue
        kept.append(c)

    # Excluding BEFORE the model means you never pay to judge the recipient and
    # the model never gets the chance to return them.
    return {"candidates": kept, "has_candidates": bool(kept)}
```

## Node 5 — the judge

The §6 prompt byte-identical. `reasoning_effort: "low"`, `max_completion_tokens: 3000`, JSON mode, no
`temperature`. Route on `has_candidates`.

**Keep the `dropped` array in the output schema.** It costs a handful of tokens and it is the only
cheap audit you get on a variable that names real people.

## Node 6 — the still-there check

Provider job titles go stale. Search each kept name plus the domain and confirm the person is still
presented as being there. Route it on the judge having kept anyone, so you only check the few names
that could actually ship.

**This is not optional.** A wrong name here is not a soft miss — it is a stranger being told their
colleague works somewhere they left a year ago.

## Node 7 — assemble and contract

```python
def run(judge, still_there, exclusions):
    kept = [p for p in ((judge or {}).get("keep") or []) if p.get("name")]
    gone = set((still_there or {}).get("gone") or [])
    live = [p for p in kept if p["name"] not in gone][:2]

    names = [p["name"] for p in live]
    # ONE name is a fine answer. Join in CODE so the copy can never render a
    # dangling "or".
    phrase = "" if not names else (names[0] if len(names) == 1
                                   else names[0] + " or " + names[1])

    return {
        "other_prospects":        phrase,
        "other_prospects_count":  len(names),
        "other_prospect_1_title": live[0]["title"] if len(live) > 0 else "",
        "other_prospect_2_title": live[1]["title"] if len(live) > 1 else "",
        # QA only. Names people you deliberately rejected -- never push it.
        "dropped_reasons":        (judge or {}).get("dropped", []),
    }
```

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: name 2 other prospects" | jq -r '.id')
# create the 7 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "other-prospects" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{
  "domain":"acme.com",
  "recipient_full_name":"Priya Ramanathan",
  "recipient_linkedin_url":"https://www.linkedin.com/in/priya-ramanathan",
  "persona_titles":["Chief Operating Officer","VP Operations","Head of Operations"]
}]}'
```

## The smoke test that matters

Do not test on random rows. **Pick a row where the recipient themselves would qualify** — a founder
at a small company, or someone whose title matches the persona cascade exactly — and confirm they do
not appear in their own variable.

Then vary the name: add a middle initial, a nickname in parentheses, a credential suffix. **The
exclusion must survive all of them**, because your two sources will not spell the name the same way.

| What you see | What it means |
|---|---|
| The recipient appears in their own variable | node 4's key normalization is too strict. Compare first+last only |
| Two campaign peers name each other | tier 2 exclusion is off, or `campaign_peers` is not being passed |
| A row ran with no recipient name | node 2 is not raising |
| Named people who left last year | node 6 is not running |
| A dangling "or" in the copy | the phrase is being built in the email template instead of in node 7 |
| Executive assistants named | the support-staff list in the prompt was trimmed |
