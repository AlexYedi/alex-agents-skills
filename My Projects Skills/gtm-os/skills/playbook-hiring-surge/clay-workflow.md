# Clay workflow build: Hiring Surge

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Read this before you build anything.**

**The free engine of this playbook is not available in a workflow.**
`Find Employee Headcount by Criteria` is a Clay **table action**. It does not appear in the
workflow action catalog, so a workflow cannot call it. Confirm for yourself:

```bash
clay workflows actions list | grep -i "headcount\|employee-count"
```

That means the workflow build is **not** a like-for-like port. It is the same gate logic and the
same locked prompt over a **different, metered** counting source. Concretely:

| | Table build | Workflow build |
|---|---|---|
| Counting source | `Find Employee Headcount by Criteria` | a metered employee-count action, or your own HTTP call |
| Cost per 1,000 rows | ~$0.005 (model only) | **materially more**, and charged per row |
| Gate logic | identical | identical |
| Locked prompt | identical | identical |

**If cost matters, build the table, not the workflow.** The workflow is the right choice when you
need this callable from a script or a scheduler and you accept paying per row for the counts.

⚠️ **Status: specification. Never built or published.**

## Graph

```
[1 trigger: domains]
   -> [2 code: normalize identifier]
   -> [3 tool: department count, total]
   -> [4 tool: department count, last 6 months]
   -> [5 code: ratio + floors gate]
   -> [6 agent: write the line]      (only fires when the gate passed)
   -> [7 code: QC + output contract]
```

Nodes 3 and 4 repeat per department. Two departments means four count nodes. **Tool instances are
not shared across nodes**, so the same action key can be mapped four different ways with no
cross-contamination.

## Node 1 — trigger

| Field | Type | Example |
|---|---|---|
| `domain` | string | `"acme.com"` |
| `company_linkedin_url` | string, optional | `"https://www.linkedin.com/company/acme"` |
| `departments` | string[] | `["Sales","Marketing and Public Relations"]` |
| `window_months` | int | `6` |

## Node 2 — code: normalize the identifier

Free LinkedIn URL first, bare domain second. Never buy a URL.

```python
def run(domain, company_linkedin_url):
    d = (domain or "").strip().lower()
    for p in ("https://", "http://", "www."):
        if d.startswith(p):
            d = d[len(p):]
    d = d.split("/")[0]
    return {"identifier": (company_linkedin_url or "").strip() or d, "bare_domain": d}
```

## Nodes 3 and 4 — the count calls

Pick your counting source. Two options:

**Option A: a metered employee-count action from the catalog.**

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | .actionKey' | grep -i employee
clay workflows actions schema <packageId> <actionKey> | jq '.inputParameters'
```

⚠️ Several of these **charge even when they find nothing**. Read the action's own description
before you wire it, and put a per-row cost ceiling on the node.

**Option B: `http-api-v2` against a people API you already pay for.** Costs 0 Clay credits, but
you pay the vendor. Node 3 asks for the department total; node 4 adds the recency filter.

Either way:

- `automapInputs: false` on both nodes.
- `headers` and `body` are object-valued, so they need `{"type":"map","entries":{...}}`, never a
  JSON string.
- Pin `identifier` from node 2 with `sourceNodeId` + `sourcePath`. A raw `{{identifier}}` in the
  mapping resolves to undefined and you get `missing required inputs`.
- Send a browser User-Agent if the vendor sits behind Cloudflare.

## Node 5 — code: the gate

The heart of the playbook. Ratio **plus** absolute floors.

```python
def run(sales_total, sales_recent, mkt_total, mkt_recent):
    def pct(total, recent):
        # New starts as a share of the PRE-EXISTING team, not the current team.
        # A team that went 4 -> 8 reads as 100% growth, which is what a human would say.
        base = (total or 0) - (recent or 0)
        if base <= 0:
            # The whole department started inside the window. A real surge, not an error.
            return float("inf") if (recent or 0) > 0 else 0.0
        return (recent or 0) / base * 100.0

    def surge(total, recent):
        p = pct(total, recent)
        return p > 15 or p == float("inf") or (recent or 0) > 6

    def qualifies(total, recent):
        # The floors. Benched, not fitted: 17/20 with them, 10/20 without.
        return (recent or 0) >= 2 and (total or 0) >= 4 and surge(total, recent)

    if qualifies(sales_total, sales_recent):
        dept, hires = "sales", sales_recent
    elif qualifies(mkt_total, mkt_recent):
        dept, hires = "marketing", mkt_recent
    else:
        dept, hires = "", 0

    return {"hiring_surge_dept": dept, "hiring_surge_hires": hires}
```

`dept` is `""` on ~95% of rows. That is the design, and it is what keeps node 6 from running.

⚠️ **Do not loosen the floors to hit a volume target.** They cut the gated segment from 14.6% to
5.2%, which is roughly 96,000 source rows for a 5,000-lead campaign. Source more rows instead.

**Sanity guard, mandatory on the bare-domain path.** Two companies can share a short name, and a
bare domain invites the collision. Abstain when a department count exceeds the company's known
total headcount, and abstain on any company whose name is a short generic token.

## Node 6 — agent: write the line

- **System prompt:** everything above the `PER-ROW DATA` marker in `SKILL.md` §6, byte-identical.
- **User message:** `{"department":"<dept>","role_starts_last_6_months":<hires>}`.
- **Reasoning effort: minimal.** At default effort this prompt returned empty content on **10 of
  10 rows** with `finish_reason=length`.
- **JSON mode on**, schema `{hiring_surge_line: string, confidence: string}`.
- Route so this node only runs when `hiring_surge_dept != ""`. Without that, the model runs on
  every row, spends ~19x more, and hallucinates a surge onto companies that do not have one.

Fan-in is safe here: a node with several incoming edges fires on **first arrival** and pins from
branches that never ran resolve as absent, not null.

## Node 7 — code: QC and output contract

```python
def run(line, gate):
    v = (line or {}).get("hiring_surge_line", "") or ""
    banned = ("hired", "added", "brought on", "recruited")
    low = v.lower()
    if any(b in low for b in banned):  qc = "fail: hire claim"
    elif "—" in v or "–" in v:         qc = "fail: dash"
    elif v.endswith("."):              qc = "fail: trailing period"
    elif v and v[0].isupper():         qc = "fail: uppercase start"
    elif len(v) > 90:                  qc = "fail: too long"
    elif not v:                        qc = "empty"
    else:                              qc = "pass"
    return {
        "hiring_surge_line":  v if qc == "pass" else "",
        "hiring_surge_dept":  gate.get("hiring_surge_dept", ""),
        "hiring_surge_hires": gate.get("hiring_surge_hires", 0),
        "qc": qc,
    }
```

The `hire claim` check is specific to this playbook and it is not optional — the whole scope
limitation in `SKILL.md` §1 lives or dies on it.

**Every terminal path needs its own node with this same `outputSchema`**, or a caller gets the raw
output of whatever node happened to run last.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: hiring surge" | jq -r '.id')
# create nodes, then pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows diagram "$WF"
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "hiring-surge" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{"domain":"acme.com","window_months":6}]}'
```

## Smoke test

| What you see | What it means |
|---|---|
| Every row gates to `""` | Expected on ~95% of rows. Confirm on a company you know is scaling before assuming a bug |
| Counts are zero everywhere | your counting source got a department value outside its enum — many return zero silently rather than erroring |
| Counts larger than the company | name collision on the bare-domain path |
| `missing required inputs: identifier` | node 2's output is not pinned on nodes 3/4 |
| All lines empty | node 6's reasoning effort is not minimal |
| QC says `fail: hire claim` | the prompt was edited. Restore it |
