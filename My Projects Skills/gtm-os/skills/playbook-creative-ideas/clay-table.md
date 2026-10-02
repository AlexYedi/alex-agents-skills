# Clay table build: 3-Bullet Creative Ideas

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 83% verdict covers the script path. **Run the acceptance check at
the bottom of this file before trusting a Clay build.**

⚠️ **Do not build anything until the operator has named the three slots and hand-written three
complete bullet sets for three real companies.** See `SKILL.md` §1.

## Where the columns go

The table behind your email gate.

## Columns

Fourteen, in dependency order.

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free |
| 2-6 | Evidence Source 1-5 | action / HTTP | `{{Domain}}` | **`length({{previous evidence}}) < 200`** | five sources in a locked order. ⚠️ **gated on SHORT, not on empty** |
| 7 | Company Evidence | Formula | coalesce 2-6, first with `length >= 200` | none | the model's only input about the company |
| 8 | Creative Ideas Raw | AI | `gpt-4o-mini`, the §6 prompt, JSON out | `length({{f_Evidence}}) >= 200` | **ONE AI column for all three bullets**, not three |
| 9-11 | creative_idea_1/2/3 | Formula | extract from 8 | `!!{{f_IdeasRaw}}` | free |
| 12 | Ideas QC | Formula | see below | `!!{{f_IdeasRaw}}` | **the verifier plus the lint** |
| 13 | creative_ideas_block | Formula | join the three bullets | `{{f_IdeasQC}} === "pass"` | the rendered block |
| 14 | Ideas Campaign Route | Formula | `{{f_IdeasQC}} === "pass" ? "ideas" : "non-ideas"` | none | **any empty bullet routes away** |

### Why the evidence rungs gate on length, not emptiness

A two-sentence boilerplate description is **technically non-empty**, and it produces three generic
bullets that read like a mail merge. Gating on emptiness stops the waterfall at the first rung that
returned *anything*, which is usually the thinnest one.

### Why one AI column, not three

Three separate columns triple the cost, and worse, they let the model repeat itself across slots
because no call can see what the others wrote.

## Column 12: the verifier and the lint

```js
(() => {
  const raw = {{f_IdeasRaw}} || {};
  const ev  = String({{f_Evidence}} || "");
  const norm = s => String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "");
  const hay = norm(ev);

  const BUZZ = ["leverage","synergy","best-in-class","cutting-edge","seamless","robust",
                "world-class","game-changing","revolutionize"];

  for (let i = 1; i <= 3; i++) {
    const b = String(raw["creative_idea_" + i] || "").trim();
    const e = String(raw["evidence_" + i] || "").trim();
    if (!b) return "fail: bullet " + i + " empty";

    // THE VERIFIER, and it is free: the model quotes what it used, and we assert
    // the quote is real. A bullet whose evidence is not in the input was invented.
    if (!e || !hay.includes(norm(e))) return "fail: bullet " + i + " evidence not in input";

    const w = b.split(/\s+/).length;
    if (w < 8 || w > 22)              return "fail: bullet " + i + " length";
    if (b.includes("—") || b.includes("–")) return "fail: bullet " + i + " dash";
    if (b.endsWith("."))              return "fail: bullet " + i + " trailing period";
    if (b[0] !== b[0].toLowerCase())  return "fail: bullet " + i + " leading capital";
    if (/\ba [aeiou]/i.test(b))       return "fail: bullet " + i + " article";
    if (BUZZ.some(x => b.toLowerCase().includes(x))) return "fail: bullet " + i + " buzzword";
  }
  return "pass";
})()
```

**Note that an empty bullet is a `fail`, not a partial pass.** A 3-bullet email with 2 bullets is not
a degraded version of this campaign — it is a different email, and column 14 routes it to one.

## Push to your sequencer

Push `creative_ideas_block`, or the three fields individually.

⚠️ **Namespace the custom field names per client** (`creative_idea_1_<client>`). Custom-field names
are case sensitive and **near-duplicates coexist silently on the same lead record** — which is a very
quiet way to send last client's bullets.

Route on column 14. **Get the non-ideas campaign's name and client right before you create it** —
many sequencers have no campaign-delete API.

## The 8-point Clay acceptance check

The script verdict does not transfer. Run this on **10 real rows from the client's own list**, never
on invented companies, and record the date and the numbers.

1. **Model and reasoning.** The column is a mini-class model, **or** a reasoning model with its
   reasoning level explicitly set to the lowest value. **A reasoning column with the level unset
   fails outright, no sample needed.**
2. **Prompt byte match.** Diff the Clay column's prompt against your reference — **including the
   few-shot turns**, which are the part most likely to drift. Any diff and the tuning you did stops
   describing production.
3. **JSON parses on all 10.** Prose or a fenced code block means JSON mode is off.
4. **Blank rate between 5% and 30%.** Above 30% the evidence source is wrong for this client. **Under
   5%, read the thinnest 3 rows by hand** — models fill thin rows rather than abstaining when the
   prompt is even slightly loosened.
5. **Evidence substring assertion passes** on every non-empty bullet. **If column 12 is not asserting
   it, the column is not built to spec.**
6. **Lint clean.** No dashes, no trailing period, no leading capital, 8 to 22 words, no buzzword, no
   article error.
7. **Cost per row read from the run log, not estimated.** A number several times the budget means
   reasoning is on.
8. **Round-trip one lead through your sequencer.** Push one row to a DRAFT campaign, pull the lead
   back from the API, and confirm the field name matches **exactly** and the value is populated.

**Eight for eight is a pass. Anything less and the Clay path is untested, whatever the script's
verdict says.**
