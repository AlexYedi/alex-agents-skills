# Clay table build: AI Specificity Line

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 8/10 verdict covers the script path.

⚠️ **Lock the client offer block before you build anything.** It is the model's only whitelist, and
it is per client, not per row. Paste it into the column's system prompt and do not edit it mid-campaign.

## Where the columns go

The table behind your email gate.

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free |
| 2 | Company Description | action / imported | `{{Domain}}` | `!!{{f_Domain}}` | the **whole** input. A free source is fine |
| 3 | Description Rich | Formula | `String({{f_Description}} \|\| "").length >= 400` | none | the render gate |
| 4 | Rendered Fetch | HTTP API | rendering proxy | `{{f_DescriptionRich}} === false` | METERED, **capped** |
| 5 | Company Evidence | Formula | coalesce 2 and 4 | none | |
| 6 | Specificity Raw | AI | `gpt-4o-mini`, `SKILL.md` §6 parts 1-3, JSON out | `!!{{f_Evidence}}` | the only paid model column |
| 7 | Guard | Formula | see below | `!!{{f_SpecificityRaw}}` | **deterministic. This is the verifier** |
| 8 | Grade Line | Formula | Flesch-Kincaid on the **tail** | `{{f_Guard}} === "pass"` | ⚠️ **the tail, not the rendered sentence** |
| 9 | specificity_line | Formula | `{{f_Guard}} === "pass" && {{f_GradeLine}} <= 7 ? tail : ""` | none | **the pushed field** |
| 10 | specificity_anchor / _offer_item | Formula | extract from 6 | none | **QA only. Never pushed** |

## Column 7: the deterministic guard

```js
(() => {
  const r = {{f_SpecificityRaw}} || {};
  if (String(r.fits || "") !== "yes") return "abstain: no fit";

  const line   = String(r.line || "").trim();
  const anchor = String(r.anchor || "").trim();
  const item   = String(r.offer_item || "").trim();
  const ev     = String({{f_Evidence}} || "");
  const offer  = String({{f_ClientOfferBlock}} || "");
  if (!line || !anchor) return "abstain: empty";

  const norm = s => String(s || "").toLowerCase().replace(/[^a-z0-9]/g, "");

  // 1. The ANCHOR must be copied from the company data. This is what stops the
  //    model inventing a product the company does not sell.
  if (!norm(ev).includes(norm(anchor))) return "fail: anchor not in evidence";

  // 2. The OFFER ITEM must be copied from the client offer list. The capability
  //    lines double as the whitelist, which is why they are written as short
  //    quotable phrases.
  if (!norm(offer).includes(norm(item))) return "fail: offer item not on the list";

  // 3. The line must actually contain the anchor.
  if (!norm(line).includes(norm(anchor))) return "fail: line missing anchor";

  // 4. Mechanical copy rules.
  const w = line.split(/\s+/).length;
  if (w < 6 || w > 14)                  return "fail: length";
  if (line.includes("—") || line.includes("–")) return "fail: dash";
  if (line.endsWith("."))               return "fail: trailing period";
  if (line[0] !== line[0].toLowerCase()) return "fail: leading capital";

  const low = line.toLowerCase();
  if (low.includes("help you") || low.includes("specifically"))
    return "fail: repeats the frame";
  if (norm(line).includes(norm({{f_CompanyName}})))
    return "fail: names the company";

  const BANNED = ["product margins","gross margin","your business","your products",
                  "boost margins","improve efficiency","grow faster","grow sales",
                  "more sales","drive demand","increase sales","channel","platform","across"];
  if (BANNED.some(b => low.includes(b))) return "fail: generic phrase";

  return "pass";
})()
```

**Checks 1 and 2 are the verifier**, and they are free. The model is asked to quote its anchor from
the company data and its offer item from the client list, and you assert both quotes are real. **A
line built on an invented anchor or an off-list promise cannot pass.**

## Column 8: grade the TAIL only

⚠️ Do **not** grade the rendered sentence.

The frame `Specifically, I think we can help you.` **scores 5.7 on its own**, so any 6-to-14-word
tail pushes the full sentence to **7.0 to 9.8 regardless of how plain the tail is.** A tail of grade
2.5 still renders at 7.0.

**Gating the render blanks every row for a property of house copy, not of the data.**

If you want the rendered sentence under the bar too, that is a copy fix: **dropping "Specifically"
takes the worst sampled render from 9.1 to 6.3** with no change to the tail. Keep gating the tail
either way.

## Credit gates

- **Column 4** (the render) fires only on thin descriptions, **and needs an explicit row cap.**
- **Column 6** is the only model spend.

## Push to your sequencer

`{{specificity_line}}`.

⛔ **Never push the anchor or the offer item.** They are QA fields and they are populated on rows that
failed the guard.

**Route the abstains out of this campaign** rather than sending a frame with a hole in it. If you
must keep them, pre-render the whole sentence — frame plus value plus trailing period and space —
into one field, so it renders as nothing when empty.

**Spintax cannot do this job.**

## Smoke test

Run 20 rows and read the **anchors** first, before the lines.

- Anchors are business words ("product", "margin", "SKU") → your evidence source is too generic, or
  the anchor rule was softened.
- Every row fills → the abstain examples are missing from the few-shot block.
- Lines promise growth → the offer block has no "do NOT do" line.
- Every row blanks on grade → you graded the rendered sentence.
- Two runs give different lines for the same row → **expected. Judge a batch, never a row.**
