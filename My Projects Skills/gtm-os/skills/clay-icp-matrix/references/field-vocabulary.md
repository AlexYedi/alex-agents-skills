# Field vocabulary — what the two axes actually accept

Read from `clay search filters-mode fields --source-type {companies,people}` on **2026-08-13**.
Free metadata; no credits and no search rows. **Re-pull at the start of every build** — allowed-value
sets are the whole point of this skill and they are not stable enough to recite.

## The vocabulary gap, measured

The industry taxonomy has **457 closed values** and is used by both axes (`industries` on the
account axis, `company_industries_include` on the persona axis).

**6 of 25 common GTM industry terms exist as values — a 24% hit rate:**

| Present | Absent |
|---|---|
| `Manufacturing`, `Insurance`, `Retail`, `Real Estate`, `Education`, `Hospitality` | `SaaS`, `B2B`, `B2C`, `Fintech`, `Healthcare`, `Cybersecurity`, `Software`, `MarTech`, `HR Tech`, `E-commerce`, `Logistics`, `Legal`, `Media`, `Gaming`, `Biotech`, `Telecom`, `Energy`, `Nonprofit`, `Government` |

The shape of the mismatch explains it: **only 11% of the taxonomy (52 of 457) is a single word.**
The taxonomy is compound-phrase shaped — `Embedded Software Products`,
`Transportation, Logistics, Supply Chain and Storage`, `Abrasives and Nonmetallic Minerals
Manufacturing` — while GTM vocabulary is single-word shaped. Two distinct failures follow:

- **Concept absent.** `SaaS`, `B2B`, `Fintech` have no representation at all — not as a value, not
  as a substring of any value.
- **Word-form mismatch.** `Biotech` misses while `Biotechnology` is a value; `Software` misses while
  six `… Software Products` compounds exist. The concept is there and the user's spelling is not.

**Short terms are actively dangerous with substring matching.** `AI` substring-matches 53 values
including `Air, Water, and Waste Program Management`, `Airlines and Aviation` and
`Blockchain Services`. Anything under roughly five characters must be matched exactly or not at all.

## Why a translation failure is silent — in both directions

From `guidance.behavior`, verbatim on both axes:

```
Each top-level filter narrows the result set (AND).
Multiple values in one string[] filter broaden matches (OR).
Omit fields instead of passing empty arrays; empty arrays do not restrict results.
```

So an unmatched value **narrows to nothing** (reads as a tiny market) and an empty array
**restricts nothing** (reads as a huge one). Neither errors. This is the mechanism that turns a
vocabulary problem into a false fact about the market.

## Explicitly NOT filters — the platform's own words

Account axis: *"Lookalike company search, funding stage, Fortune 500, unicorn status, and
technographics are not native public API filters."*

Persona axis: *"Email addresses, phone numbers, Fortune 500, unicorn status, and employer lookalikes
are not native public API filters."*

Every one of these is something teams routinely write into an ICP. Each becomes a **paid per-row
verify** after the population exists, or nothing. Note `funding stage` is absent while
`funding_amounts` is present — the *amount* filters, the *stage* (Series A/B) does not.

## Account axis — 30 fields

**Enum fields (closed sets):**

| Field | Values |
|---|---|
| `industries` | 457 |
| `annual_revenues` | 12 — `0-500K, 500K-1M, 1M-5M, 5M-10M, 10M-25M, 25M-75M, 75M-200M, 200M-500M, 500M-1B, 1B-10B, 10B-100B, 100B-1T` |
| `sizes` | 9 — **`1, 2, 10, 50, 200, 500, 1000, 5000, 10000`** (band FLOORS) |
| `funding_amounts` | 9 — `under_1m, 1m_5m, 5m_10m, 10m_25m, 25m_50m, 50m_100m, 100m_250m, over_250m, **unknown**` |
| `types` | 8 — `Privately Held, Public Company, Partnership, Self Employed, Non Profit, Educational, Self Owned, Government Agency` |

`funding_amounts` carrying an explicit **`unknown`** is the enum equivalent of an `is_null`
fallback: omit it and every company whose funding was never recorded is excluded by a funding
filter, so a sparse attribute becomes a smaller market.

**The rest:** `country_names` (+`_exclude`), `locations` (+`_exclude`),
`location_cities/states/regions/postal_codes_include|exclude`, `location_headquarters_only`,
`industries_exclude`, `derived_business_types`, `derived_industries`, `derived_subindustries`
(+`_exclude`), `derived_revenue_streams`, `description_keywords` (+`_exclude`),
`include_company_identifiers`, `minimum_member_count`, `maximum_member_count`,
`minimum_follower_count`.

The `derived_*` family is where an untranslatable concept sometimes lands — but note the grammar's
low-coverage warning about AI-derived fields: filtering one without a null fallback silently
excludes every unpopulated record.

## Persona axis — 41 fields

**Enum fields:**

| Field | Values |
|---|---|
| `company_industries_include` | 457 — the same taxonomy, so the vocabulary gap applies here too |
| `company_annual_revenues` | 12 — identical spellings to the account axis |
| `company_sizes` | 9 — **`1, 2-10, 11-50, 51-200, 201-500, 501-1,000, 1,001-5,000, 5,001-10,000, 10,001+`** (band LABELS) |
| `job_title_seniority_levels_v2` | 14 — `founder, owner, board-member, partner, c-suite, vp, director, head, manager, senior, mid-level, entry, intern, unknown` |
| `job_title_seniority_floor_level` | same 14 |
| `job_title_seniority_match_mode` | 2 — `exact, floor` |

**Seniority is the one axis with a clean closed vocabulary**, and `match_mode: floor` with
`floor_level: 'vp'` expresses "VP or above" directly — no keyword gymnastics needed.

**Useful others:** `job_title_keywords` (+`_exclude`), `job_description_keywords`,
`headline_keywords`, `about_keywords`, `profile_keywords`, `certification_keywords`,
`include_past_experiences`, `current_role_min|max_months_since_start_date` (tenure),
`role_range_start|end_month`, `experience_count` / `max_experience_count`, `connection_count` /
`max_connection_count`, `follower_count` / `max_follower_count`, `languages`, `school_names`,
`names`, `company_identifier`, `company_description_keywords` (+`_exclude`),
`company_industries_exclude`, and the same location include/exclude family.

## ⚠ The two axes spell the same bands differently

| Band | Account axis (`sizes`) | Persona axis (`company_sizes`) |
|---|---|---|
| 51–200 | `'50'` | `'51-200'` |
| 1,001–5,000 | `'1000'` | `'1,001-5,000'` |
| 10,001+ | `'10000'` | `'10,001+'` |

**Nine identical bands, two vocabularies.** A matrix that states a headcount range once must
translate it twice, differently, and a value carried from one axis to the other is not in the
other's closed set — so it narrows to nothing, silently.

Revenue is the exception: `annual_revenues` and `company_annual_revenues` share spellings exactly.
So the dialect split is specific to headcount, which makes it easy to miss.

## Band alignment

Because both size and revenue are banded, **an arbitrary numeric threshold cannot be expressed**:

- `50–2,000 employees` → account axis `['50','200','500','1000']` covers **50–4,999**. The stated
  ceiling does not exist as a boundary.
- `$10M ARR floor` → `10M-25M` upward. A `$12M` floor has no boundary at all.

The rounding is always outward on the selected bands, so a band-aligned filter is **wider** than
the stated ICP, never narrower. Say by how much; the difference changes the market size before
anyone enumerates it.


## `derived_*` — where the untranslatable terms actually live (measured 2026-08-13)

The gap this file opened — `SaaS`, `B2B`, `Fintech` matching **0** of 457 industry values — has a
partial answer that was not visible from the filter metadata. Two live enrichment payloads carry a
`derived_datapoints` object, and its values are exactly the vocabulary the industry taxonomy lacks:

```
business_type      ["B2B"]   /   ["B2C"]          <- B2B EXISTS here, and nowhere in `industries`
industry           ["Professional, Business and Legal Services"] / ["Finance and Insurance"]
subindustry        ["Architecture, Urban Planning and Green Building"] / ["Banking and Lending"]
business_stage     "Established"
pattern_tags       "Architecture, B2B, Full-Service"
revenue_streams    ["Project/Contract Work", "Professional Services"]
scale_scope        "international; Location Detail: 11 offices worldwide"
primary_offerings  [...]
```

So for an untranslatable dimension, `derived_business_types` / `derived_industries` /
`derived_subindustries` / `derived_revenue_streams` are the **first** place to look, and `B2B` is
translatable after all — just not on the field a user would guess.

Two cautions before relying on it:

- **These were observed in an enrichment payload, not as filter values.** The filter fields of the
  same name exist on the account axis, but their allowed-value sets were not enumerable from
  `filters-mode fields` (no `allowedValues` returned). Whether the filter accepts these exact
  strings is **unverified** — resolve it before promising it.
- **The grammar flags AI-derived fields as low coverage**, so filtering one without a null fallback
  silently excludes every unpopulated record. A derived field is a recall filter as well as a
  criteria filter.

Also observed, and relevant to any band handling: `total_funding_amount_range_usd` returns the
string **`"Funding unknown"`** rather than null — unknown encoded as a value, twice out of two. A
band comparison that does not special-case it will treat "unknown" as a band label.
