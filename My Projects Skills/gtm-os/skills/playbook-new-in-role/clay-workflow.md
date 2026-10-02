# Clay workflow build: New in Role

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first — it
carries the command surface, the input-pinning rules, and the sandbox limits. This file only
carries what is specific to this signal.

⚠️ **Status: specification. This workflow has never been built and published.** The graded path is
the script path in `SKILL.md` §4. Build it, run 5 rows, read the output, then fix this file.

## What the workflow does

Takes a search spec in, returns one `new_in_role_line` per person out. Linear graph, six nodes.

```
[1 trigger]
   -> [2 code: build search filters]
   -> [3 tool: http-api-v2  POST /search-person]
   -> [4 code: title gate + deterministic fields]
   -> [5 agent: write the line]
   -> [6 code: QC + shape the output]
```

Everything deterministic happens in code nodes. The agent node does exactly one thing: turn a fact
list into one sentence.

## Node 1 — trigger

Inputs the caller supplies:

| Field | Type | Example |
|---|---|---|
| `titles` | string[] | `["Chief Operating Officer","COO","VP of Operations"]` |
| `gate_titles` | string[] | the same list **plus abbreviations and variants** |
| `location` | string | `"United States #US"` |
| `headcount_min` / `headcount_max` | int | `50` / `2000` |
| `months_max` | int | `3` (the 90-day default; ceiling 9) |
| `page` | int | `1` |

`gate_titles` defaults to `titles`, which is usually **wrong** — see node 4.

## Node 2 — code: build search filters

Emits one object that node 3 pins as its request body. Building the body here (rather than mapping
it field by field on the HTTP node) is the pattern that keeps secrets and structure out of the tool
config.

```python
def run(titles, location, headcount_min, headcount_max, months_max, page):
    return {"body": {
        "page": page,
        "filters": {
            "person_location_search": {"include": [location]},
            "person_job_title": {"include": titles},
            "company_headcount_custom": {"min": headcount_min, "max": headcount_max},
            "person_time_in_current_role": {"min": 0, "max": months_max},
        },
    }}
```

`outputSchema` must declare `body`. Every declared key has to be returned or the node fails with
`Structured output validation failed`.

## Node 3 — tool: the search call

| Setting | Value |
|---|---|
| package | `4299091f-3cd3-4d68-b198-0143575f471d` |
| actionKey | `http-api-v2` |
| method | `POST` |
| url | `https://api.prospeo.io/search-person` |
| headers | `{"X-KEY": "<from workspace auth, never inline>", "Content-Type": "application/json", "User-Agent": "<a browser UA>"}` |
| body | pinned from node 2's `body` |
| `automapInputs` | **`false`** |
| `returnResponseMetadata` | `true`, so you can branch on `statusCode` |

Three things that will bite you here:

1. **`http-api-v2` costs 0 Clay credits** and parses responses as JSON. That is fine for this API.
   It would **not** work for scraping HTML — an HTML response comes back as `body: {}`.
2. **`headers` and `body` are object-valued**, so they need a `{"type":"map","entries":{...}}`
   mapping, never a JSON string.
3. **Send a browser User-Agent.** Many data vendors sit behind Cloudflare and 403 a default runtime
   user agent while allowing `curl`, so a manual test passes and the batch silently fails.

Output path: `$.result.body`, with the status at `$.result.statusCode`.

## Node 4 — code: title gate and deterministic fields

The load-bearing node. It does four things the model must never do.

```python
import time

MONTHS = ["January","February","March","April","May","June","July","August","September",
          "October","November","December"]

def run(response, gate_titles):
    # An empty result set arrives as HTTP 400 with error_code NO_RESULTS.
    # Branch on it BEFORE any generic error handling or normal empty pulls kill the run.
    if (response or {}).get("error_code") == "NO_RESULTS":
        return {"people": []}

    now = time.gmtime()
    keys = [t.lower() for t in (gate_titles or [])]
    out = []

    for r in (response or {}).get("results", []):
        p = r.get("person", {}) or {}
        hist = p.get("job_history", []) or []
        cur = next((h for h in hist if h.get("is_current")), None)
        if not cur:
            continue

        # 1. TITLE GATE. person_job_title is a loose contains match that can hit a PAST
        #    role, so the pull returns people whose current title is unrelated. Gate on
        #    job_history's current title, never on person.current_job_title.
        title = (cur.get("title") or "")
        if not any(k in title.lower() for k in keys):
            continue

        # 2. Deterministic date fields.
        y, m = cur.get("start_year"), cur.get("start_month")
        if not (y and m):
            continue
        months_in_role = (now.tm_year - int(y)) * 12 + (now.tm_mon - int(m))
        start_label = "%s %s" % (MONTHS[int(m) - 1], y)

        # 3. Deterministic enum. > 1 position at the same company means an internal move.
        #    It proves the move, never its DIRECTION, which is why the prompt says
        #    "stepped into" and never "moved up".
        cid = cur.get("company_id")
        positions = sum(1 for h in hist if h.get("company_id") == cid)
        change_type = "promotion" if positions > 1 else "new_hire"

        prior = next((h for h in hist if h is not cur), {}) or {}

        out.append({
            "first_name": p.get("first_name", ""),
            "current_title": title,
            "company_name": (r.get("company", {}) or {}).get("name", ""),
            "company_domain": (r.get("company", {}) or {}).get("domain", ""),
            "role_start_month": start_label,
            "months_in_role": months_in_role,
            "role_change_type": change_type,
            "prior_title": prior.get("title", ""),
            "prior_company": prior.get("company_name", ""),
        })

    return {"people": out}
```

Sandbox reminders: **no `datetime`** (that is why this uses `time`), no `urllib`, no outbound
HTTP, no pip. And `run_code` is *not* a faithful preview of this sandbox — it has `datetime`, so
code that passes there can still fail in the node.

⚠️ **`gate_titles` must include abbreviations.** Gate on the search list alone and you silently
drop every person whose `job_history` title is literally "COO", which is very common. Silent row
loss on a free mandatory step is the worst kind.

## Node 5 — agent: write the line

- **System prompt:** everything **above** the `PER-ROW DATA` marker in `SKILL.md` §6,
  byte-identical.
- **User message:** the `Facts: ...` line only, bound from node 4's fields.
- **Model:** the small reasoning model named in §6.
- **Reasoning effort: minimal.** At default effort this exact prompt returned `finish_reason=length`
  with empty content on **10 of 10 rows**. This is not optional.
- **JSON mode on**, schema `{new_in_role_line: string, confidence: string}`.

**Do not add `role_change_type` to the output schema.** It is computed in node 4. If the model's
value were allowed through, a flipped enum would make the copy claim someone "joined" a company
they have worked at for years.

## Node 6 — code: QC and output contract

```python
def run(line, person):
    v = (line or {}).get("new_in_role_line", "") or ""
    if "—" in v or "–" in v:      qc = "fail: dash"
    elif v.endswith("."):          qc = "fail: trailing period"
    elif v and v[0].isupper():     qc = "fail: uppercase start"
    elif len(v) > 90:              qc = "fail: too long"
    elif not v:                    qc = "empty"
    else:                          qc = "pass"
    return {
        "new_in_role_line": v if qc == "pass" else "",
        "role_change_type": person.get("role_change_type", ""),
        "months_in_role":   person.get("months_in_role", 0),
        "company_domain":   person.get("company_domain", ""),
        "qc": qc,
    }
```

**Every terminal path needs its own node with this same `outputSchema`.** A routine returns the
last executed node's output, so if a branch ends on the HTTP node, the caller gets a raw HTTP
response instead of your data.

## Build it

```bash
WF=$(clay workflows create --name "Playbook: new in role" | jq -r '.id')

# create nodes 1..6, then for each: pin inputSchema, then set outputSchema
# SEPARATELY -- sending both in one update call silently drops inputSchema
clay workflows nodes create "$WF" --input node2.json | jq -r '.nodeId'
clay workflows nodes update "$WF" <nodeId> --input inputschema.json
clay workflows nodes update "$WF" <nodeId> --input outputschema.json
clay workflows nodes get    "$WF" <nodeId> | jq '.node.inputSchema'   # confirm it persisted

clay workflows diagram "$WF"        # eyeball the graph
clay workflows publish "$WF"
```

## Run it

`clay workflows runs test` is currently broken (`userId: expected number, received string`). Go
through a routine, which is also how anything else calls this playbook:

```bash
RT=$(clay routines create workflow "$WF" --name "new-in-role" | jq -r '.id')

clay routines runs start "$RT" --input '{"items":[{
  "titles": ["Chief Operating Officer","VP of Operations"],
  "gate_titles": ["chief operating officer","coo","vp of operations","vp ops"],
  "location": "United States #US",
  "headcount_min": 50, "headcount_max": 2000,
  "months_max": 3, "page": 1
}]}'
```

## Smoke test

Run 5 and read the sentences.

| What you see | What it means |
|---|---|
| `missing required inputs` | a tool node is reading a trigger var directly. Pin it with `sourceNodeId` + `sourcePath` |
| `HTTP 431` | `automapInputs` left at `true` on node 3 |
| Node 4 returns empty, no error | node 3's `inputSchema` was dropped by a combined update, or a delete cascade nulled it |
| All lines empty | node 5's reasoning effort is not minimal |
| Zero people survive node 4 | `gate_titles` has no abbreviations |
| `ModuleNotFoundError: datetime` | use `time.strftime`, not `datetime` |
