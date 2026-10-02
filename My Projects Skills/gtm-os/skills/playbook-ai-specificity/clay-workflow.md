# Clay workflow build: AI Specificity Line

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

⚠️ **Lock the client offer block first.** It is the model's only whitelist and it is per client, not
per row.

The workflow advantage here is the same as elsewhere: an agent node lets you set reasoning effort, so
the cheaper nano-class model runs correctly instead of returning blanks at 19x the cost.

## Graph

```
[1 trigger: domain + company_name + client_offer_block]
   -> [2 tool: company description]
   -> [3 code: richness gate]
   -> [4 tool: rendering proxy]     only when 3 says thin, and only with a cap
   -> [5 agent: fit check -> anchor -> offer item -> line]
   -> [6 code: deterministic guard + reading-level gate + contract]
```

## Node 3 — the richness gate, and why it exists

```python
def run(description):
    t = (description or "").strip()
    # Measured on four real ecommerce brands, a PLAIN homepage fetch returned:
    # 0 bytes, 16 bytes, 1 byte, and a refused connection. If your evidence source
    # is "just fetch the homepage", you will silently write from nothing on exactly
    # the list types this playbook is best at.
    return {"rich": len(t) >= 400, "evidence": t}
```

Node 4 is metered. **Give it an explicit cap and refuse to start without one** — an uncapped rescue
step on a list full of thin sites is the whole budget.

## Node 5 — the writer

The three-part prompt from `SKILL.md` §6: static prefix, client offer block, client-specific few-shot
pairs as faux turns. **Minimal reasoning effort**, `max_completion_tokens: 400`, JSON mode, no
`temperature`.

**Include at least two abstain examples** in the few-shot block — one obvious non-fit and one
fluff-only description. **Without them the model learns that every row deserves a line.**

## Node 6 — guard, grade, contract

```python
import re

BANNED = ("product margins","gross margin","your business","your products","boost margins",
          "improve efficiency","grow faster","grow sales","more sales","drive demand",
          "increase sales","channel","platform","across")

def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def _fk_grade(text):
    # Flesch-Kincaid on the TAIL only. Rough syllable count is fine here.
    words = re.findall(r"[A-Za-z]+", text or "")
    if not words:
        return 0.0
    def syl(w):
        w = w.lower()
        groups = re.findall(r"[aeiouy]+", w)
        n = len(groups) - (1 if w.endswith("e") and len(groups) > 1 else 0)
        return max(1, n)
    sylls = sum(syl(w) for w in words)
    sents = max(1, len(re.findall(r"[.!?]", text)) or 1)
    return 0.39 * (len(words) / sents) + 11.8 * (sylls / len(words)) - 15.59

def run(ai, evidence, client_offer_block, company_name):
    r = ai or {}
    blank = {"specificity_line": "", "specificity_anchor": "", "specificity_offer_item": "",
             "grade_line": None, "guard": ""}

    if str(r.get("fits", "")) != "yes":
        return dict(blank, guard="abstain: no fit")

    line   = (r.get("line") or "").strip()
    anchor = (r.get("anchor") or "").strip()
    item   = (r.get("offer_item") or "").strip()
    if not line or not anchor:
        return dict(blank, guard="abstain: empty")

    ev, offer = _norm(evidence), _norm(client_offer_block)

    # THE VERIFIER, and it is free. The model quotes its anchor from the company
    # data and its offer item from the client list; we assert both quotes are real.
    # A line built on an invented anchor, or promising something off the list,
    # cannot pass.
    if _norm(anchor) not in ev:      return dict(blank, guard="fail: anchor not in evidence")
    if _norm(item) not in offer:     return dict(blank, guard="fail: offer item not on the list")
    if _norm(anchor) not in _norm(line): return dict(blank, guard="fail: line missing anchor")

    w = len(line.split())
    low = line.lower()
    if not (6 <= w <= 14):                   return dict(blank, guard="fail: length")
    if "—" in line or "–" in line:           return dict(blank, guard="fail: dash")
    if line.endswith("."):                   return dict(blank, guard="fail: trailing period")
    if line[:1].isupper():                   return dict(blank, guard="fail: leading capital")
    if "help you" in low or "specifically" in low:
        return dict(blank, guard="fail: repeats the frame")
    if _norm(company_name) and _norm(company_name) in _norm(line):
        return dict(blank, guard="fail: names the company")
    if any(b in low for b in BANNED):        return dict(blank, guard="fail: generic phrase")

    # Grade the TAIL, never the rendered sentence. The frame alone scores 5.7, so
    # any 6-to-14-word tail renders at 7.0-9.8 regardless of how plain it is --
    # gating the render blanks every row for a property of house copy.
    g = _fk_grade(line)
    if g > 7:
        return dict(blank, guard="blanked: line grade %.1f" % g, grade_line=round(g, 1))

    return {"specificity_line": line, "specificity_anchor": anchor,
            "specificity_offer_item": item, "grade_line": round(g, 1), "guard": "pass"}
```

Note the guard returns a **reason** on every failure path. On a playbook with real run-to-run
variance, the reason column is how you tell "the prompt drifted" from "this row was always going to
abstain".

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: ai specificity line" | jq -r '.id')
# create the 6 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "specificity-line" | jq -r '.id')
clay routines runs start "$RT" --input '{"items":[{
  "domain":"example-poolsupply.com",
  "company_name":"Example Pool Supply",
  "client_offer_block":"CLIENT OFFER ... (locked block)"
}]}'
```

## How to read the output

**Read the anchors before you read the lines.** The anchor is where this playbook succeeds or fails:
a real product noun produces a good sentence almost automatically, and a business word
("product", "margin", "SKU") produces a generic one no amount of prompt tuning fixes.

**And judge a batch, never a row.** Two runs on the same company genuinely produce different lines —
measured — so a single awkward output is not evidence of anything.

## Smoke test

| What you see | What it means |
|---|---|
| Anchors are business words | the evidence is too generic, or the anchor rule was softened |
| Every row fills | the abstain examples are missing from the few-shot block |
| Lines promise growth the client cannot deliver | the offer block has no "do NOT do" line |
| Every row blanks on grade | you graded the rendered sentence instead of the tail |
| The render step fires on most rows | your description source is failing. Check node 2 before paying for node 4 |
| Cost 19x the estimate | reasoning effort is not set |
| Over 30% blanks in a segment | **the list is wrong for this campaign, not the prompt** |
