# Finding mechanics — search arms, buyer mapping, employment fields

Live-verified mechanics 2026-08-11 (this workspace); re-verify per workspace.

## The search arm (quota, not credits)

`clay search filters-mode create --source-type people` with filters:
- `company_identifier`: [the domain] — LIST-shaped (a bare string is a validation
  error).
- `job_title_keywords`: [the title vocabulary] — the role scoping. Widen VOCABULARY
  before seniority: "CFO" misses "Head of Finance", "Finance Director", localized
  titles.
- Optionally `names` (also a list) when narrowing to a known person — but that's
  find-linkedin-profile territory.

Then `clay search filters-mode run <searchId>` pages results. Facts that bite:
- Filters are RECALL, not guarantees — post-validate every returned record against
  the role/company ask; never trust the filter to have enforced it.
- `total` is always null; `hasMore: false` is the only exhaustion signal — shortfall
  claims are honest only after paging to it.
- Filters-mode records carry `url` (LinkedIn), name, current title, and role start
  date; query-mode records carry NO LinkedIn URL — stay in filters-mode here.
- An empty result consumes nothing.

## Why not the obvious function (the measured reality)

Managed **Find People at Company** (~3.3 credits declared) returns the company's top
~10 profiles ranked by SENIORITY and ignores every name/role filter it accepts
(measured live in this factory: name-filter keys accepted-and-ignored; `total:
10000` on a big company; a famous-CEO ground-truth passes only because the CEO ranks
first). It is the result-based-dedupe BASELINE this skill must beat, and the measured
gap is the point: for any persona below "most senior person," the bare call returns
the wrong people at 3.3 credits while the role-scoped search returns the right ones
on quota. Use the managed function only when the ask genuinely IS "who's most senior
here."

## Buyer mapping (what-you-sell → department × seniority floor)

Canonical enums (use verbatim — they drive deterministic gates):

Seniority (7): `C-Level, Founders, Owners` · `Executives and Senior Leadership` ·
`Non-Executive Management` · `Individual Contributors and Non-Management` ·
`External partners and contractors` · `Non-corporate role` · `Other`.

Title-token override rules, applied in order (0 and 2b are live-eval folds):
0. **"Chief of Staff" → Non-Executive Management** — applied BEFORE the Chief token:
   a Chief of Staff (to the CFO/CEO/anyone) is a staff role, not a function owner;
   the bare Chief-token rule misclassifies it as C-level (caught live: a "CFO"
   keyword search returned "Chief of Staff to the CFO" as its top hit).
1. Chief / Founder / Owner → C-Level, Founders, Owners
2. Director / VP / Vice President → Executives and Senior Leadership
2b. **Controller / Treasurer → Executives and Senior Leadership** — finance
   leadership titles with no VP/Director token; without this rule they fall to
   "Other" and get dropped.
3. Senior / Lead / Group → Non-Executive Management
4. Product / project / program / relationship / renewal MANAGERS → Individual
   Contributors (the classic misread — "manager" in these titles is not management)

**Keyword containment ≠ role identity**: `job_title_keywords` matches SUBSTRINGS —
"CFO" surfaces "Chief of Staff to the CFO". Every hit must pass role-identity
post-validation (is this title THE role, or a title that mentions it?) before
classification. And index coverage has holes at the very top: a major public
company's sitting CFO can be absent under the exact title while their SVPs are
present — the honest output is "senior-most identifiable: SVP Finance", never a
promotion of the nearest hit.

Department (12): Engineering & Data & R&D · Design · Marketing & PR · Product ·
Finance & Accounting · IT & Security · People & HR & Recruiting · Operations ·
Legal · Sales · Customer Service · Other.

Common sell-into mappings: spend/finance tooling → Finance & Accounting, Director+;
security → IT & Security, Director+; devtools → Engineering, Director+ (plus
staff-level champions); HR tech → People & HR, Director+; martech → Marketing & PR,
Director+. At small companies (< ~200 headcount) the economic buyer floor rises to
C-level and the CEO is often genuinely the buyer.

Buying-committee framing: `Economic Buyer` (final budget authority — usually the
function's C/VP peak, or CEO at small cos) · `Champion` (senior operator who'd run
the tool) · `Influencer` (adjacent stakeholder). Emit the role per kept person; the
opener differs per role.

## Employment verification fields

- The search record's `domain` ECHOES the search anchor — never read it as
  employment. Employment lives in the person's `latest_experience_*` fields
  (company, domain, title, start date, is_current).
- Multiple concurrent `is_current` roles are real (board seats, advisors, portfolio
  execs) — `latest_experience` selects the primary; length>1 = `multi-role` flag,
  never "departed".
- Mismatch resolution ladder: person enrichment (LinkedIn URL → canonical record) →
  emit `multi-role` / `departed` / `employment unconfirmed`. A departed hit at the
  target company is a lead for track-champion territory, not a decision-maker row.
- Slug variance: the same person carries different LinkedIn slugs across sources —
  ship the canonical URL from enrichment, or mark the raw search URL as raw.

## Cost posture

Role-scoped search: search-result quota, 0 credits; empty results consume nothing.
Optional per-person enrichment (canonical URL / employment resolution): ~1 credit
per person — state before spending. The 3.3-credit managed lister is the baseline,
not a rung.
