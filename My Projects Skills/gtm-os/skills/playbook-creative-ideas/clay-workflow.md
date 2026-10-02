# Clay workflow build: 3-Bullet Creative Ideas

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

⚠️ **Do not build until the operator has named the three slots and hand-written three complete bullet
sets for three real companies.** The slots are the playbook; everything below is plumbing.

**The workflow has one real advantage here:** an agent node lets you set reasoning effort, so you can
run the cheaper nano-class model correctly (**$0.12/1k**) instead of being forced onto a mini-class
model in a native AI column (**$0.27/1k**).

## Graph

```
[1 trigger: domain + company_name + spec]
   -> [2..6 tools: evidence waterfall, each gated on the previous being SHORT]
   -> [7 code: coalesce evidence]
   -> [8 agent: all three bullets in ONE call]
   -> [9 code: evidence assertion + lint + route]
```

## Nodes 2-6 — the evidence waterfall

Five sources in a locked order: an internal company description, a **free** company-enrichment
action, client-owned tables, a company-search API, a rendering proxy.

⚠️ **Gate each rung on the previous evidence being SHORT, not on it being empty.**

```python
def run(evidence_so_far):
    text = (evidence_so_far or "").strip()
    # A two-sentence boilerplate description is technically NON-EMPTY, and it
    # produces three generic bullets that read like a mail merge. Gating on
    # emptiness stops the waterfall at the first rung that returned anything --
    # usually the thinnest one.
    return {"need_more": len(text) < 200, "evidence": text}
```

A row still thin after all five rungs **abstains**.

## Node 8 — one call, all three bullets

- **System block:** the seller's offer, the **three named slots**, the must-never-appear list, the
  output contract.
- **Few-shot:** the operator's hand-written sets as faux prior turns.
- **User message, last:** company name, domain, evidence.
- **Output:** `{creative_idea_1..3, evidence_1..3, confidence}`.
- **Reasoning effort minimal**, `max_completion_tokens: 1200`, JSON mode, no `temperature`.

**One call, not three.** Three calls triple the cost and let the model repeat itself across slots,
because no call can see what the others wrote.

⚠️ **The model never picks what a bullet is about.** If you find yourself writing "pick three
interesting angles" into this prompt, you have rebuilt the free-form version that scored **2/5** —
against **21/23** for slot-defined.

## Node 9 — assert, lint, route

```python
import re

BUZZ = ("leverage","synergy","best-in-class","cutting-edge","seamless","robust",
        "world-class","game-changing","revolutionize")

def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def run(ai, evidence, client_slug):
    raw = ai or {}
    hay = _norm(evidence)
    bullets, problems = [], []

    for i in (1, 2, 3):
        b = (raw.get("creative_idea_%d" % i) or "").strip()
        e = (raw.get("evidence_%d" % i) or "").strip()

        if not b:
            problems.append("bullet %d empty" % i); continue

        # THE VERIFIER, and it is free: the model quotes what it used, and we
        # assert the quote is real. No second model call -- a bullet whose
        # evidence is not in the input was invented, and it is blanked.
        if not e or _norm(e) not in hay:
            problems.append("bullet %d evidence not in input" % i); continue

        w = len(b.split())
        if not (8 <= w <= 22):                 problems.append("bullet %d length" % i)
        elif "—" in b or "–" in b:             problems.append("bullet %d dash" % i)
        elif b.endswith("."):                  problems.append("bullet %d period" % i)
        elif b[:1].isupper():                  problems.append("bullet %d capital" % i)
        elif re.search(r"\ba [aeiou]", b, re.I): problems.append("bullet %d article" % i)
        elif any(x in b.lower() for x in BUZZ): problems.append("bullet %d buzzword" % i)
        else:
            bullets.append(b); continue

    ok = len(bullets) == 3

    # ANY empty or failing bullet routes the row away. A 3-bullet email with 2
    # bullets is not a degraded version of this campaign, it is a different email,
    # and a sequencer cannot pin a lead to a specific variant.
    out = {
        "creative_ideas_block": "\n".join("- " + b for b in bullets) if ok else "",
        "route":                "ideas" if ok else "non-ideas",
        "qc":                   "pass" if ok else "; ".join(problems),
    }
    for i in (1, 2, 3):
        # Namespace per client. Custom-field names are case sensitive and
        # near-duplicates coexist SILENTLY on the same lead record, which is a
        # very quiet way to send last client's bullets.
        out["creative_idea_%d_%s" % (i, client_slug)] = bullets[i - 1] if ok else ""
    return out
```

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: creative ideas" | jq -r '.id')
# create the nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "creative-ideas" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{
  "domain":"example-manufacturing.com",
  "company_name":"Example Manufacturing",
  "client_slug":"acme"
}]}'
```

## Smoke test

Run 20 real rows from the client's own list — **never invented companies.**

| What you see | What it means |
|---|---|
| Bullets are generic and interchangeable | the slots are not fixed, or the prompt invites the model to pick angles |
| Bullets sound like the model, not the seller | the exemplars were AI-drafted. Hand-write them |
| Every row fills, even thin ones | the evidence gate is on emptiness, or the prompt was loosened. **Read the thinnest 3 by hand** |
| Blank rate above 30% | wrong evidence source for this client. Change the source, not the prompt |
| The assertion fails often | the model is paraphrasing its evidence rather than quoting it. Tighten that rule |
| Cost several times the estimate | reasoning effort is not minimal |
| Last client's bullets appear | field names were not namespaced |
