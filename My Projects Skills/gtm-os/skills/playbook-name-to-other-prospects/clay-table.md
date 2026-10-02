# Clay table build: Name 2 Other Prospects

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.**

⚠️ **This variable puts a named human being into a stranger's inbox.** Build the exclusions before
you build anything else, and smoke-test them on a row where you *know* the recipient is also a
qualifying colleague.

## Where the columns go

Your **person-level** table, after email validation. Note the shape: the lookup is **per domain**,
but the exclusion is **per person** — so the same company's candidate list is reused across its
contacts while each contact gets a different exclusion applied.

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free |
| 2 | Colleague Candidates | action / HTTP | `{{Domain}}` | `!!{{f_Domain}} && !!{{f_RecipientFullName}}` | ⚠️ **the run condition requires the recipient name.** No name means no exclusion is possible, and the row must not run |
| 3 | Candidates Filtered | Formula | see below | `!!{{f_Candidates}}` | **TIER 1 exclusion, in code, before the model** |
| 4 | Colleague Judge | AI | `SKILL.md` §6 prompt | `!!{{f_CandidatesFiltered}}` | the only paid column |
| 5 | Kept People | Formula | `{{f_Judge}}?.keep \|\| []` | none | |
| 6 | Still There Check | HTTP / search | the kept names + domain | `{{f_KeptPeople}}?.length > 0` | free-ish. **Not optional** |
| 7 | other_prospects | Formula | see below | none | **the pushed field** |
| 8 | other_prospects_count | Formula | the number of names in column 7 | none | |
| 9 | Judge Dropped Reasons | Formula | `{{f_Judge}}?.dropped \|\| []` | none | **QA only. Never pushed** — but read it |

## Column 3: the exclusions, in code, before the model

Doing this **before** the model matters twice: you never pay to judge the recipient, and you never
give the model the chance to return them.

```js
(() => {
  const norm = s => String(s || "")
        .normalize("NFKD").replace(/\p{M}/gu, "")
        .toLowerCase().replace(/[^a-z ]/g, " ")
        .split(/\s+/).filter(Boolean);

  // Compare FIRST + LAST only. Middle names, initials, credentials and
  // "Priya (Pri) Ramanathan, MBA" must all still match the recipient.
  const key = s => { const p = norm(s); return p.length ? p[0] + " " + p[p.length - 1] : ""; };

  const meName = key({{f_RecipientFullName}});
  const meUrl  = String({{f_RecipientLinkedinUrl}} || "").toLowerCase().replace(/\/$/, "");

  // TIER 2 (optional): everyone else from this domain who is ALSO in this campaign,
  // so two colleagues never receive emails naming each other.
  const alsoInCampaign = ({{f_CampaignRecipientsAtDomain}} || []).map(key).filter(Boolean);

  return ({{f_Candidates}} || []).filter(c => {
    const n = key(c.name);
    const u = String(c.linkedin_url || "").toLowerCase().replace(/\/$/, "");
    if (!n) return false;
    if (meName && n === meName) return false;                 // TIER 1, name
    if (meUrl && u && u === meUrl) return false;              // TIER 1, url
    if (alsoInCampaign.includes(n)) return false;             // TIER 2
    return true;
  });
})()
```

⛔ **If `{{f_RecipientFullName}}` is empty this formula excludes nothing.** That is why column 2's run
condition requires it. A row that reaches the judge with no recipient name is one nickname away from
`Hey John, should I reach out to John?`

## Column 7: assemble the phrase in code

```js
(() => {
  const kept = ({{f_KeptPeople}} || []).filter(p => p && p.name);
  const live = kept.filter(p => !({{f_StillThereCheck}}?.gone || []).includes(p.name));
  const names = live.slice(0, 2).map(p => p.name);
  if (!names.length) return "";
  // ONE name is a fine answer. Build the join in code so the copy never renders
  // a dangling "or".
  return names.length === 1 ? names[0] : names[0] + " or " + names[1];
})()
```

## Credit gate

Column 4 is the only model spend, and column 2 is the only data spend. Both are gated on the
recipient name existing — **which is a safety gate that happens to also be a cost gate.**

## Push to your sequencer

`{{other_prospects}}` and `{{other_prospects_count}}`.

⛔ **Never push the dropped-reasons column.** It names people you deliberately rejected.

**The referral CTA must be its own sentence**, and it must disappear entirely when the variable is
empty. Use a pre-rendered whole-sentence field or split the list at upload — **spintax cannot branch
on emptiness.**

## Smoke test, and make it the adversarial one

Do not smoke-test this on random rows. **Find a row where the recipient themselves would qualify as
a senior colleague** — a founder at a small company, someone whose title matches the persona
cascade — and confirm they do not appear in their own variable.

Then check:

- Two contacts at the same domain, both in the campaign → do they name each other?
- A recipient with a nickname or a middle initial in one source and not the other → still excluded?
- A row with a blank recipient name → **did it run at all?** It should not have.

Finally, read 20 rows of column 9. The dropped reasons are the cheapest audit you will get on a
variable that names real people.
