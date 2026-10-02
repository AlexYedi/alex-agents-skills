# Clay workflow build: Fundraising

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This one ports cleanly: a lookup, a code node that decides every fact, an agent that only picks
words, and a code node that wraps the sentence. Five nodes, linear.

## Graph

```
[1 trigger: domain]
   -> [2 tool: company lookup by domain]
   -> [3 code: domain guard + stage filter + 12-month window]
   -> [4 agent: write the clause]      (only when eligible)
   -> [5 code: wrap into the sentence + contract]
```

The design principle worth copying into other playbooks: **node 3 decides truth, node 4 decides
wording.** The model is structurally incapable of inventing a round because it never sees anything
but a pre-validated record.

## Node 2 — company lookup

Either the native company-data action from the catalog, or `http-api-v2`:

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | .actionKey' | grep -i enrich-company
clay workflows actions schema e5f3b09f-1b8f-4806-a960-27abf163940f enrich-company | jq '.inputParameters'
```

If you use `http-api-v2`: `automapInputs: false`, `headers` and `body` as `{"type":"map",...}` never
a JSON string, a browser User-Agent, and pin `domain` from the trigger with
`sourceNodeId` + `sourcePath`.

⚠️ Some providers return **HTTP 400 with a `NO_RESULTS` code** instead of an empty list. Treat that
as zero matches, not an outage — a workflow that fails on any 400 will look broken on perfectly
normal empty pulls.

## Node 3 — the three guards

```python
import time

EQUITY = {"Pre seed","Seed","Series unknown","Series A","Series B","Series C","Series D",
          "Series E-J","Angel","Corporate round","Convertible note","Equity crowdfunding"}
# Database bucket labels, not round names anyone says out loud.
UNSPEAKABLE = {"Series E-J", "Series unknown"}

def _months_since(iso):
    if not iso:
        return 9999
    # No datetime in this sandbox. time.strptime + calendar arithmetic only.
    t = time.strptime(iso[:10], "%Y-%m-%d")
    now = time.gmtime()
    return (now.tm_year - t.tm_year) * 12 + (now.tm_mon - t.tm_mon)

def run(response, domain):
    out = {"company":"", "amount":"", "stage":"", "eligible":False,
           "evidence_url":"", "confidence":"low"}

    want = (domain or "").strip().lower()
    results = (response or {}).get("results") or []
    hit = (results[0] or {}).get("company") if results else None
    if not hit or not want:
        return {"record": out}

    # GUARD 1: domain equality. A website filter also matches OTHER listed websites,
    # so a vendor that lists your target as a customer can win the match, silently,
    # with a total_count of 1 and no warning. This removed 1 wrong company in 10.
    if (hit.get("domain") or "").lower() != want:
        return {"record": out}

    out["company"] = hit.get("name", "")

    # GUARD 2: equity stages only. Secondary-market sales and PE stake purchases are
    # money moving between SHAREHOLDERS, not into the company. Calling either a raise
    # is a false claim and a founder will notice. This removed 3 of 6.
    events = ((hit.get("funding") or {}).get("events")) or []
    eligible = [e for e in events if e.get("stage") in EQUITY]
    if not eligible:
        return {"record": out}

    latest = sorted(eligible, key=lambda e: e.get("raised_at") or "", reverse=True)[0]

    # GUARD 3: the 12-month window, computed HERE so the model never does arithmetic.
    m = _months_since(latest.get("raised_at"))
    if not (0 <= m <= 12):
        return {"record": out}

    amt = float(latest.get("amount") or 0)
    if   amt >= 1e9: out["amount"] = "$%s B" % round(amt / 1e9, 1)
    elif amt >= 1e6: out["amount"] = "$%dM" % round(amt / 1e6)

    stage = latest.get("stage") or ""
    out["stage"]        = "" if stage in UNSPEAKABLE else stage
    out["evidence_url"] = latest.get("url", "")
    out["confidence"]   = "high"
    out["eligible"]     = True
    return {"record": out, "eligible_flag": "yes"}
```

Return `eligible_flag` as a **plain string**, and route node 4 on that scalar. Do not route on a
substring of a serialized blob: `json.dumps` writes `"eligible": true` with a space and
`JSON.stringify` writes `"eligible":true` without one, so a substring gate silently matches nothing
and **the whole run comes back empty with no error.**

Sandbox reminder: **no `datetime`** — that is why this uses `time.strptime`. And `run_code` is not a
faithful preview of the node sandbox.

## Node 4 — agent: write the clause

- **System prompt:** the block from `SKILL.md` §6, byte-identical.
- **User message:** the record from node 3.
- **JSON mode on**, schema `{funding_line: string, evidence_url: string, confidence: string}`.
- **Token cap 3000**, no `temperature`, retry up to 3 times on `finish_reason=length`.
- **Route so it only runs when `eligible_flag == "yes"`.**

The prompt's key is `funding_line` but it holds the **clause**. Do not rename it — that is
byte-for-byte what was graded.

## Node 5 — wrap and contract

```python
def run(ai, record):
    clause = ((ai or {}).get("funding_line") or "").strip()
    if clause.endswith("."):
        clause = clause[:-1]
    # The wrap happens in CODE. The model never writes the finished sentence, so the
    # leading "Saw" and the trailing period cannot be forgotten or hallucinated, and an
    # abstaining row pushes a TRULY empty variable that renders as nothing at all.
    return {
        "funding_clause":       clause,
        "funding_line":         ("Saw " + clause + ".") if clause else "",
        "funding_evidence_url": (ai or {}).get("evidence_url", "") if clause else "",
        "funding_confidence":   (ai or {}).get("confidence", "low") if clause else "low",
        "company":              record.get("company", ""),
    }
```

Give every terminal path a node with this same `outputSchema`.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: fundraising" | jq -r '.id')
# create the 5 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "funding-line" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[
  {"domain":"attio.com"},
  {"domain":"basecamp.com"}
]}'
```

The second row should come back **empty**. That is a correct abstain, not a failure — bootstrapped
companies are supposed to produce nothing.

## Before you wire the output into an email

Read `SKILL.md` §2. The body line is `{{funding_line}}` **alone on its own line, never wrapped in
spintax.** Spintax is a random chooser with no knowledge of whether the variable is populated: it
will render `Saw .` on abstaining rows and throw the personalization away on populated ones.

## Smoke test

| What you see | What it means |
|---|---|
| Every row empty | node 4 is routed on a serialized-JSON substring instead of the scalar flag |
| A wrong company's round | node 3's domain-equality guard is not firing |
| A secondary sale reported as a raise | the equity-stage set was widened |
| Copy names a month or a year | the prompt was edited |
| `ModuleNotFoundError: datetime` | use `time.strptime`, not `datetime` |
| `finish_reason=length`, empty | retry. **Never record it as an abstain** |
