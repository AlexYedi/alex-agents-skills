# Clay workflow build: First Name Cleaning

Read [`../clay-playbooks/clay-cli-harness.md`](../clay-playbooks/clay-cli-harness.md) first.

⚠️ **Status: specification. Never built or published.**

Like its company-name twin, this is one of the simplest workflows in the library: no external API,
no paid enrichment, four nodes. The difference is the **guard node**, which is doing real work here
and is the reason this playbook has zero silent failures.

## Graph

```
[1 trigger: first + last + company]
   -> [2 agent: the locked prompt]
   -> [3 code: the six guards]
   -> [4 code: output contract]
```

Nodes 3 and 4 can be one node. They are split here because the guards are the part you will edit.

## Node 1 — trigger

| Field | Type | Example |
|---|---|---|
| `first_name_raw` | string | `"Dr Ruba"` |
| `last_name_raw` | string | `"Maatouk"` |
| `company_name_raw` | string | `"Metropolitan Dental Care"` |

Pass the **raw** strings, including the mess. The model needs to see it, and the guards need the
raw first name to check for invented letters.

## Node 2 — agent: the locked prompt

- **System prompt:** the entire block from `SKILL.md` §6, byte-identical, all 30 examples.
- **User message:** `first="<first>" last="<last>" company="<company>"`.
- **JSON mode on**, schema `{first_name_clean: string, changed: boolean, confidence: string}`.
- **Token cap:** 200 for a mini-class model, **2000 for a nano-class reasoning model.**
- **No `temperature`.**

⚠️ **Do not shorten the prompt to save tokens.** This was measured head to head: a 435-token
candidate saved **$0.0145 per 1,000 rows** and produced **3 broken greetings in 30 rows**, none of
which the guards below caught. Cutting 82% of the tokens cut only 31% of the cost, because the long
prompt gets 79% of its input at the cached rate and the short one drops under the 1,024-token cache
floor and gets none of it.

## Node 3 — the six guards

The reason this playbook has zero silent failures. **The guards catch invention and known junk —
they do not catch a weak prompt's plausible-but-wrong output.**

```python
import re
import unicodedata

BLOCK = {"na","n","none","null","nil","nan","unknown","tbd","tba","test","testing","xxx","asdf",
         "noname","notprovided","notapplicable","nofirstname","firstname","admin","administrator",
         "info","information","sales","support","team","owner","manager","management","hr","office",
         "contact","contactus","help","helpdesk","service","customerservice","billing","accounts",
         "accounting","marketing","webmaster","postmaster","noreply","donotreply","hello","hi",
         "enquiries","inquiries","reception","frontdesk","general","mail","email","user","guest",
         "staff","employee","recruiting","careers","jobs","press","media","legal"}

LATIN = re.compile(r"^[ -ɏḀ-ỿ‘’ʼ'\-\.]*$")

def norm(s):
    # Accent-insensitive, alphanumerics only.
    # NOTE: this is EMPTY for a name written only in Chinese, Cyrillic, Arabic or
    # Hangul. That is exactly why has_letters exists -- an emptiness test built on
    # norm() alone silently abstained on every non-Latin name in the benchmark and
    # reported them as ordinary placeholder abstains, so the score never moved.
    d = unicodedata.normalize("NFKD", s or "")
    d = "".join(c for c in d if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]", "", d.lower())

def has_letters(s):
    return any(c.isalpha() or c.isdigit() for c in (s or ""))

def run(raw, last, company, ai):
    out = (ai or {}).get("first_name_clean", "") or ""
    t = (raw or "").strip()

    g1 = (not has_letters(raw)) or norm(raw) in BLOCK \
         or (not has_letters(out)) or norm(out) in BLOCK

    fl, cn = norm(raw) + norm(last), norm(company)
    g2 = len(fl) >= 4 and len(cn) >= 3 and (fl == cn or cn in fl or fl in cn)

    g3 = bool(re.fullmatch(r"[A-Z0-9]{2,4}", t)) and not re.search(r"[AEIOUY]", t)
    g4 = bool(re.fullmatch(r"[A-Z]{9,}", t))
    g5 = bool(out) and not LATIN.match(out)
    g6 = bool(out) and norm(out) not in norm(raw)

    return {
        # Only G1 and G6 blank the value. G2-G5 flag with the name INTACT.
        # Turning G2 into an abstain drops every solo consultant whose company
        # is named after them.
        "abstain": g1 or g6,
        "review":  g1 or g2 or g3 or g4 or g5 or g6,
        "fired":   [n for n, v in
                    [("g1",g1),("g2",g2),("g3",g3),("g4",g4),("g5",g5),("g6",g6)] if v],
    }
```

## Node 4 — output contract

```python
def run(ai, guards):
    val = "" if guards.get("abstain") else ((ai or {}).get("first_name_clean", "") or "")
    conf = (ai or {}).get("confidence", "low")
    return {
        "first_name_clean": val,
        "changed":      (ai or {}).get("changed", False),
        "confidence":   conf,
        "needs_review": (not val) or conf == "low" or guards.get("review", False),
        "guards_fired": guards.get("fired", []),
    }
```

`guards_fired` is worth returning even though nothing consumes it: when a batch looks wrong, it
tells you **which** guard is misfiring without a re-run.

## Build and run

```bash
WF=$(clay workflows create --name "Playbook: first name cleaning" | jq -r '.id')
# create the 4 nodes; pin inputSchema and set outputSchema in SEPARATE update calls
clay workflows publish "$WF"

RT=$(clay routines create workflow "$WF" --name "first-name-clean" | jq -r '.id')

clay routines runs start "$RT" --input '{"items":[
  {"first_name_raw":"Dr Ruba","last_name_raw":"Maatouk","company_name_raw":"Metropolitan Dental Care"},
  {"first_name_raw":"PAUL","last_name_raw":"Harlin","company_name_raw":""},
  {"first_name_raw":"Kathryn (Katie)","last_name_raw":"Connors","company_name_raw":"BrightFarms"},
  {"first_name_raw":"AAA","last_name_raw":"Upholstery","company_name_raw":"AAA Upholstery"},
  {"first_name_raw":"珊","last_name_raw":"苏","company_name_raw":"Axine Water Technologies"}
]}'
```

Expected: `Ruba` · `Paul` · `Katie` · `""` (G1/G2) · `珊` with `needs_review: true` (G5, name
intact).

**That fifth row is the one to check.** If it comes back blank, your `norm()` is being used as an
emptiness test without `has_letters()`, and you are silently destroying every non-Latin name in the
list.

## Smoke test

| What you see | What it means |
|---|---|
| Every non-Latin name blank | `has_letters()` missing from G1. **4 of 100 rows, invisible in any accuracy score** |
| `finish_reason=length`, empty on every row | nano-class model at mini's 200-token cap |
| Cost ~2x expected | the example block was trimmed below the 1,024-token cache floor |
| `PAUL` flagged for review | G3 missing its vowel test |
| A solo consultant dropped entirely | G2 was made an abstain instead of a flag |
| Greetings still read `Hi Dr Matthew,` downstream | your copy is bound to the sequencer's built-in `first_name`, not to `first_name_clean` |
