# Clay table build: First Name Cleaning

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.** The 96/100 verdict covers the script path. Neither the AI column nor
the JavaScript version of the guards below has ever been executed. **Port them, then smoke-test on
10 messy rows before trusting either.**

## Where the columns go

Main work table, **after email validation**. Cleaning names for rows that fail the email gate is
wasted work.

Unlike its company-name twin, this one is a **standing column on every campaign**, not a per-client
toggle. A mangled first name breaks the greeting on every campaign that opens with one.

## Columns

| Order | Column | Type | Action | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | First Name Raw | imported | n/a | your import | none | **Do not overwrite it** — the guards read it |
| 2 | Last Name Raw | imported | n/a | your import | none | free context, materially improves the person-versus-company call |
| 3 | First Name Clean JSON | AI | `gpt-4o-mini`, `SKILL.md` §6 prompt verbatim, JSON response format, `max_completion_tokens` 200 | `first="{{FirstNameRaw}}" last="{{LastNameRaw}}" company="{{CompanyNameRaw}}"` | `!!{{f_FirstNameRaw}} && !!{{f_ValidEmail}}` | pass the **raw** company string, not a cleaned one |
| 4 | Name Guards | Formula | the JavaScript below | 1, 2, 3, raw company | none | returns `{abstain, review}`. **Required, not optional** |
| 5 | first_name_clean | Formula | `{{f_NameGuards}}?.abstain ? "" : ({{f_FirstNameCleanJson}}?.first_name_clean \|\| "")` | 3, 4 | none | **this is what ships** |
| 6 | Name Needs Review | Formula | `!{{f_first_name_clean}} \|\| {{f_FirstNameCleanJson}}?.confidence === "low" \|\| {{f_NameGuards}}?.review` | 3, 4, 5 | none | drives the review filter and the §2 downstream gate |

## Column 4: the six guards

The JavaScript twin of G1 to G6. **This has not been executed.**

```javascript
(() => {
  const raw   = {{f_FirstNameRaw}} || "";
  const last  = {{f_LastNameRaw}} || "";
  const co    = {{f_CompanyNameRaw}} || "";
  const out   = ({{f_FirstNameCleanJson}} || {}).first_name_clean || "";

  // accent-insensitive, alphanumerics only. NOTE: this is EMPTY for a name written
  // only in Chinese, Cyrillic, Arabic or Hangul, which is exactly why hasLetters exists.
  const norm = s => (s || "").normalize("NFKD").replace(/\p{M}/gu, "")
                     .toLowerCase().replace(/[^0-9a-z]/g, "");
  const hasLetters = s => /[\p{L}\p{N}]/u.test(s || "");

  const BLOCK = new Set(["na","n","none","null","nil","nan","unknown","tbd","tba","test",
    "testing","xxx","asdf","noname","notprovided","notapplicable","nofirstname","firstname",
    "admin","administrator","info","information","sales","support","team","owner","manager",
    "management","hr","office","contact","contactus","help","helpdesk","service",
    "customerservice","billing","accounts","accounting","marketing","webmaster","postmaster",
    "noreply","donotreply","hello","hi","enquiries","inquiries","reception","frontdesk",
    "general","mail","email","user","guest","staff","employee","recruiting","careers","jobs",
    "press","media","legal"]);

  // G1 placeholder: WHOLE normalized string only. Never a substring:
  // "Adminson" and "Teamer" are real surnames.
  const g1 = !hasLetters(raw) || BLOCK.has(norm(raw)) || !hasLetters(out) || BLOCK.has(norm(out));

  // G2 company overlap: FLAG ONLY, never an auto-abstain. A solo consultant's company
  // is often literally their own name.
  const fl = norm(raw) + norm(last), cn = norm(co);
  const g2 = fl.length >= 4 && cn.length >= 3 && (fl === cn || cn.includes(fl) || fl.includes(cn));

  // G3 caps acronym: short ALL-CAPS with no vowel (TVK, KSM).
  // The vowel test is what keeps PAUL and PHAM out of the flag.
  const t = raw.trim();
  const g3 = /^[A-Z0-9]{2,4}$/.test(t) && !/[AEIOUY]/.test(t);

  // G4 run-together shout (KIRKDELANEY)
  const g4 = /^[A-Z]{9,}$/.test(t);

  // G5 non-Latin script in the OUTPUT. Keep the name as written and FLAG it; the
  // downstream gate excludes the row from an English campaign.
  // Never transliterate, never blank, never a generic greeting.
  const g5 = !!out && !/^[ -ɏḀ-ỿ‘’ʼ'\-\.]*$/.test(out);

  // G6 invented letters: every letter of the output must already be in the raw field.
  const g6 = !!out && !norm(raw).includes(norm(out));

  return { abstain: g1 || g6, review: g1 || g2 || g3 || g4 || g5 || g6 };
})()
```

Note which guards abstain and which only flag: **only G1 and G6 blank the value.** G2 through G5
route the row to review with its name intact. Turning G2 into an auto-abstain is a real bug someone
will be tempted to introduce — it drops every solo consultant whose company is named after them.

## Credit gate

Column 3 is gated so you never clean a name for a row that failed email validation. **No column
here spends an enrichment credit;** the only cost is the AI column.

⚠️ **Smoke-test the gate before you run the table.** A gate bound to a column that does not exist
fails silently and produces **exactly the same table state as "no rows qualified"** — and the
downstream gate then excludes your whole list.

## Sentinel note

If your workspace uses a literal sentinel string for "not found", this column deviates: it returns
JSON, so the abstain value is an **empty `first_name_clean` key**, tested with
`!{{first_name_clean}}`. Wiring a sentinel idiom here builds a gate that never fires, because this
column never emits that string.

## Push to your sequencer

Lead-level custom variable `{{first_name_clean}}`.

⚠️ **Do NOT map it onto the sequencer's built-in `first_name` field.** Keep the raw value there so
a human can always see what the source said. The single most common way this playbook fails in
production is copy that still references the built-in field.

## QA before launch, non-negotiable

**Read 20 sampled greetings out loud, in the actual sentence from the copy** (`Hi <value>,`). Any
value you would edit is a failure, and the fix is a prompt correction round, not a manual edit of
the row.
