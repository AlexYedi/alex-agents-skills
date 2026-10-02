# Clay workflow build: Company Name Cleaning

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

This is the **simplest workflow in the library** — no external API, no paid enrichment, three
nodes. It is a good first workflow to build if you are learning the CLI.

A caveat worth stating up front: if all you want is the **default** (free suffix and casing
normalization), you do not need a workflow at all. Clay's `Normalize Company Name` action does it
on a table for free. Build this workflow when you want the **toggle** behavior available as a
callable routine — from a script, a scheduler, or another workflow.

## Graph

```
[1 trigger: name + domain]
   -> [2 code: placeholder guard on the INPUT]
   -> [3 agent: the locked prompt]
   -> [4 code: placeholder guard on the OUTPUT + invented-word guard + contract]
```

Fully linear. No fan-out, no conditionals, so none of the graph gotchas apply.

## Node 1 — trigger

| Field | Type | Example |
|---|---|---|
| `company_name_raw` | string | `"318, Inc dba Hamiltons Bud and Bloom"` |
| `domain` | string, optional | `"hamiltonsbudandbloom.com"` |

## Node 2 — placeholder guard on the input

Cheapest possible abstain. Junk strings never reach the model.

```python
import re

BLOCK = {"na","n","none","null","nil","unknown","unknowncompany","tbd","tba","test","testing",
         "xxx","asdf","retired","unemployed","student","freelance","freelancer","selfemployed",
         "self","soleproprietor","soleproprietorship","privatepractice","private","confidential",
         "confidentialjobs","confidentialcompany","homemaker","various","other","myself","me",
         "personal","notapplicable","stealth","stealthmode","stealthstartup"}

def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def is_placeholder(v):
    n = norm(v)
    # WHOLE-string match plus a selfemployed prefix. NEVER substring:
    # "Unknown Arts" and "Retired - BTH Bank" are real companies and a
    # substring rule silently deletes them.
    return (not n) or (n in BLOCK) or n.startswith("selfemployed")

def run(company_name_raw, domain):
    return {
        "skip": is_placeholder(company_name_raw),
        "name": company_name_raw or "",
        "domain": (domain or "").lower().replace("www.", ""),
    }
```

## Node 3 — agent: the locked prompt

- **System prompt:** the entire block from `SKILL.md` §6, byte-identical. All 22 examples.
- **User message:** `name="<name>" domain="<domain>"`.
- **JSON mode on**, schema `{company_clean: string, changed: boolean, confidence: string}`.
- **Token cap:** 200 for a mini-class model, **2000 for a nano-class reasoning model** — its
  reasoning tokens count against the same cap, and at 200 it returns `finish_reason=length` with
  empty content on essentially every row.
- **No `temperature`.**

⚠️ **Do not shorten the example block to "save tokens".** It is what pushes the static prefix past
the 1,024-token caching floor. A ~950-token prefix cached **zero** tokens; the 1,716-token prefix
caches ~1,300. Trimming it makes the workflow **more** expensive, not less.

Route so this node is skipped when node 2 set `skip`.

## Node 4 — output guards and contract

Two guards, both deterministic, both free.

```python
import re

def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def run(ai, guard):
    if guard.get("skip"):
        return {"company_clean": "", "changed": True, "confidence": "high", "needs_review": True}

    out = (ai or {}).get("company_clean", "") or ""

    # GUARD 1: the placeholder list again, on the OUTPUT.
    # A mini-class model scored only 7/10 on the abstain probe and will hand back
    # "Confidential Jobs" as if it were a brand. The regex path independently turns
    # "Retired - BTH Bank" into "Retired". Both are caught here.
    from_input = guard.get("name", "")
    if norm(out) in {"","na","none","unknown","retired","confidential","privatepractice"}:
        out = ""

    # GUARD 2: nothing may be invented. The answer is always a substring of the input.
    # Character-level, not word-level: word-level would falsely flag "3M Company" -> "3M".
    if out and norm(out) not in norm(from_input):
        out = ""

    conf = (ai or {}).get("confidence", "low")
    return {
        "company_clean": out,
        "changed": out != from_input,
        "confidence": conf,
        "needs_review": (not out) or conf == "low",
    }
```

Guard 2 is the thing this playbook has that the others do not: because the answer is always a
substring of the input, **you get a perfect verifier for free** and never need a second model call.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: company name cleaning" | jq -r '.id')
# create the 4 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "company-name-clean" | jq -r '.id')

clay routines runs start "$RT" --input '{"items":[
  {"company_name_raw":"318, Inc dba Hamiltons Bud and Bloom","domain":"hamiltonsbudandbloom.com"},
  {"company_name_raw":"AMTC TECH GROUP LLC","domain":"amtctech.com"},
  {"company_name_raw":"Private Practice","domain":""}
]}'
```

Expected: `Hamiltons Bud and Bloom`, `AMTC Tech Group`, `""`.

For a real list, use the bulk path — one JSON object per line:

```bash
clay routines runs start "$RT" --bulk names.jsonl
```

## Smoke test

Run the three rows above. Then read 20 real values **inside the sentence from your copy, out loud.**
Any value you would edit is a failure, and the fix is a prompt correction round, not a manual edit.

| What you see | What it means |
|---|---|
| `finish_reason=length`, empty on every row | token cap is the mini value on a reasoning model. Use 2000 |
| Cost ~3x expected | the example block was trimmed below the 1,024-token caching floor |
| `Private Practice` comes back as a brand | node 4's output guard is not running |
| Casing flattened (`AdGreetz` → `adGreetz`) | reasoning effort set to minimal. Do not use minimal for this job |
| Prose instead of JSON | JSON mode not set on node 3 |
| Different answer on a rerun | no `temperature` passed and the default is not 0. Cache the output; do not re-run a locked campaign's names |
