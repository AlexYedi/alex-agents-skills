# Clay workflow build: perfect company list

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md)
first. It covers the command surface, input wiring and the `runs test` workaround.

⚠️ **Status: specification. Never built or published end to end.** The method in `SKILL.md` was run
with our own scripts; this file is how to run the same method inside Clay.

## Three workflows, not one

| Workflow | Runs | Input | Output |
|---|---|---|---|
| **A: learn** | once per customer list | customer domains | industry and keyword tally |
| **B: judge** | once per pulled company | ICP question + one company | `p_fit`, `fit` |
| **C: loop** | once per seed batch | a few judged fits | new fits, or nothing |

Keep them separate. A runs once, B runs hundreds of thousands of times, and C calls B. Folding them
together makes every judgment pay for the learning step and lets the ICP question drift row to row.

## Workflow A: learn from your customers

```
[1 trigger: CSV upload of customer domains]
   -> [2 tool: enrich-company]                 LinkedIn industry, headcount, HQ, description
   -> [3 code: tally industries + keywords]
   -> [4 tool: write to Audiences]             optional, keeps the customer profile
```

```bash
clay workflows actions list | jq -r '.. | objects | select(.actionKey) | "\(.packageId)\t\(.actionKey)"' \
  | grep -iE 'enrich-company|http-api-v2|claygent|use-ai'
```

Node 3 returns the pull plan directly:

```python
from collections import Counter

def run(rows):
    inds = Counter((r.get("industry") or "(blank)") for r in rows)
    return {
        "industries_to_pull": [i for i in inds if i != "(blank)"],
        "industry_counts": dict(inds.most_common()),
        "blank_count": inds.get("(blank)", 0),
        "note": "Pull every industry here, even the ones with a count of 1. "
                "Cover blank-industry companies with keyword searches.",
    }
```

Then pull the companies with `clay search` (companies, every industry from node 3, your size and
geography band) plus keyword searches, and export the rows for workflow B.

## Workflow B: judge every company

```
[1 trigger: domain, name, industry, description, question, yes, no]
   -> [2 tool: enrich-company]      only when no description came in
   -> [3 tool: http-api-v2]         POST https://api.typesafe.ai/v1/systemone (Jev)
   -> [4 code: threshold + contract]
```

Node 3 body. Jev returns a probability, not text, so node 4 is a single comparison:

```json
{
  "model": "jev-latest",
  "state": {"name": "{{name}}", "domain": "{{domain}}",
            "linkedin_industry": "{{industry}}", "description": "{{description}}"},
  "questions": {
    "fit": {"type": "noul", "instructions": "{{question}}",
            "criteria": {"true": "{{yes}}", "false": "{{no}}"}}
  }
}
```

Header: `Authorization: Bearer <TYPESAFE_API_KEY>`. `http-api-v2` costs 0 Clay credits; you pay Jev
directly ($0.042 per million input tokens, output free).

```python
def run(resp, threshold=0.5):
    p = resp["answers"]["fit"]["noul"]
    return {"p_fit": round(p, 3), "fit": p >= threshold}
```

For very large pulls, batch outside Clay with `scripts/jev_judge.py` (20 companies per request).

## Workflow C: the Claygent loop

```
[1 trigger: seed_domains (5 to 10 judged fits), icp_summary]
   -> [2 agent: Claygent]           "These companies fit our ICP: {{seed_domains}}.
                                      Find 10 more companies like these that we might have missed.
                                      Return domain and one-line description for each."
   -> [3 code: dedupe]               drop any domain already judged (keep the set in a table or file)
   -> [4 call workflow B]            same question, same criteria
   -> [5 code: emit new fits]        they become the next seeds
```

Run it on a schedule or a driver loop. Stop rule: **stop when 20 runs in a row add one company or
fewer**, and set a run budget as well, because a big market can keep adding one company per run for a
long time.

## Checks before you publish

- Canary 50 to 100 rows through workflow B and read every "yes" on companies you did not expect.
- Read `clay workflows diagram <wfId>` once to confirm the graph.
- `runs test` is currently broken; publish, create a routine, then `routines runs start`
  (see the harness).
