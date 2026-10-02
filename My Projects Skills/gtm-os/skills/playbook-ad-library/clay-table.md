# Clay table build: Meta Ad Library

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification, never built in Clay.** The 75% verdict covers the script chain only.
Every Clay claim here is an inference from that run plus house conventions. Verify on 10 to 50 rows
before you trust any of it.

## Where the columns go

The table that already sits **behind your email gate**. Never enrich a row that has not passed
email validation, or you are paying a metered scraper for people you cannot email.

## Integration check

| Provider | Native integration? | Use |
|---|---|---|
| The model (cols 14, 15b) | **yes** | native AI column on `gpt-4o-mini`. Do **not** build an HTTP column to the model API here |
| Cache store, site fetch, SERP, rendering proxy, Apify | **no native** | `http-api-v2`, correctly. None of these is a Clay integration, so HTTP is the only route and no house pattern is being ignored |

## How to write the gates (do not skip this)

A run condition is a **JavaScript expression over field ids**, not English. It must evaluate truthy
for the column to run.

| Intent | Correct | Wrong (silently broken) |
|---|---|---|
| run if empty | `!{{f_x}}` | `{{f_x}} is empty` |
| run if present | `!!{{f_x}}` | `{{f_x}} is not empty` |
| equality | `{{f_x}} === "valid"` | `{{f_x}} = "valid"` |
| substring | `{{f_x}}?.toLowerCase()?.includes("403")` | `{{f_x}} contains "403"` |
| both | `!{{f_a}} && !{{f_b}}` | `... AND ...` |

`contains` is not a JavaScript method and `=` is assignment, not comparison. **A gate written in
prose does not throw a helpful error: it either blocks every row or fails open and runs the metered
column on 100% of the table.** Always use optional chaining — a column that has not run yet is
`null`, and `null.toLowerCase()` throws.

## Columns

`{{f_...}}` are placeholders. Get the real ids with `clay tables columns get <tableId>` and
substitute before saving.

| # | Column | Type | Integration | Input | Run condition | Notes |
|---|---|---|---|---|---|---|
| 1 | Ad Cache Lookup | Lookup Object | your cache store | `{{f_domain}}` | email-valid gate | FREE |
| 2 | Cache Fresh | Formula | `{{f_cache}}?.last_checked && (Date.now() - Date.parse({{f_cache}}.last_checked)) / 86400000 < 45` | `{{f_cache}}` | none | 45-day fast path |
| 3 | FB Page From Site | HTTP API | `GET https://{{f_domain}}/` with a browser User-Agent | `{{f_domain}}` | `!{{f_cache_fresh}}` + email gate | FREE. ⚠️ Unverified: whether Clay's HTTP column follows redirects and exposes the status separately from the body. **Check both on 10 rows** before relying on column 8's gate |
| 4 | FB Page Slug | Formula | see below | `{{f_site_html}}` | `!!{{f_site_html}}` | FREE. The `\/` un-escape is load-bearing |
| 5 | FB Search Q | Formula | `encodeURIComponent('site:facebook.com "' + ({{f_company_clean}} \|\| "") + '"')` | `{{f_company_clean}}` | `!{{f_slug}}` | **Percent-encode here, never inline the raw name.** A name with spaces or an `&` truncates the query |
| 6 | FB Page From Google | HTTP API | your SERP provider, limit 10 | `{{f_search_q}}` | `!{{f_slug}} && !!{{f_search_q}}` | CHEAP. Fires only when 3 and 4 found nothing |
| 7 | FB Page Verified | Formula | **all three gates**, see below | `{{f_google}}`, `{{f_company_clean}}`, `{{f_domain}}` | `!!{{f_google}}` | FREE. **A plain formula, not an AI column** — deterministic string work does not need a model |
| 8 | FB Page Proxy | HTTP API | rendering proxy, `js_render`, premium proxy | `{{f_domain}}` | `!{{f_slug}} && !{{f_verified}} && ({{f_site_status}} === 403 \|\| {{f_site_status}} === 429)` | METERED. **Bot-protected sites only.** If the HTTP column exposes no status, fall back to a body substring check and verify the body actually carries it |
| 9 | FB Page URL | Formula | `{{f_slug}} ? "https://www.facebook.com/" + {{f_slug}} : ({{f_verified}} \|\| {{f_proxy_slug}} \|\| "")` | 4, 7, 8 | none | the single field the rest of the chain reads |
| 10 | Ad Library Raw | HTTP API | `POST https://api.apify.com/v2/acts/apify~facebook-ads-scraper/run-sync-get-dataset-items` body `{"startUrls":[{"url":"{{f_fb_page_url}}"}],"onlyTotal":true,"activeStatus":"active"}` | `{{f_fb_page_url}}` | `!!{{f_fb_page_url}} && !{{f_cache_fresh}}` | METERED. **This gate is the whole credit story.** `onlyTotal:true` is mandatory or billing switches to per-ad |
| 11 | Active Ad Count | Formula | `{{f_adraw}}?.[0]?.totalCount ?? 0` | `{{f_adraw}}` | `!!{{f_adraw}}` | output field |
| 12 | Volume Phrase | Formula | `({{f_count}} ?? 0) >= 50 ? "allowed" : "banned"` | `{{f_count}}` | `!!{{f_adraw}}` | **Required by the prompt.** Without it the model writes "a lot of ads" for a page with 20 |
| 13 | Ad Samples | Formula | dedupe on title+body, **drop any ad whose body AND title are both template tokens**, keep 4, format as `[id … \| title "…" \| body "…"]` | `{{f_adraw}}` | `({{f_count}} ?? 0) > 0` | the template filter is mandatory |
| 14 | Ad Line Raw | AI | `gpt-4o-mini`, prompt from `SKILL.md` §6, JSON out | 5, 11, 12, 13 | `!!{{f_samples}}` | **Volume Phrase must be bound here** or the prompt's VOLUME_PHRASE line has no input |
| 15 | Ad Line Linted | Formula | the full lint + ungrounded-words stack | 14, 12, 13, `{{f_company_clean}}`, `{{f_domain}}` | `!!{{f_ai}}` | **An empty variable is always better than a bad one** |
| 15b | Truth Judge | AI | `gpt-4o-mini`, judge prompt, out `{"supported": bool, "why": "..."}` | `{{f_samples}}`, `{{f_line_linted}}` | `!!{{f_line_linted}}` | **Mandatory, 100% of rows that produced a line, never a sample.** ~$0.02 per 10,000 rows |
| 15c | ad_library_line | Formula | `{{f_judge}}?.supported === false ? "" : ({{f_line_linted}} \|\| "")` | 15, 15b | `!!{{f_ai}}` | **Push THIS column to your sequencer**, never the raw AI column |
| 16 | ad_theme | Formula | `{{f_ai}}?.ad_theme \|\| ""` | 14 | `!!{{f_ai}}` | output field |
| 17 | evidence_ad_id | Formula | `{{f_ai}}?.evidence_ad_id \|\| ""` | 14 | `!!{{f_ai}}` | output field |
| 18 | ad_confidence | Formula | `{{f_line}} ? ({{f_ai}}?.confidence \|\| "low") : "low"` | 14, 15c | `!!{{f_ai}}` | **The model key is `confidence`; the rename happens here.** A blanked line is always `low` |
| 19 | Cache Write | Post/Patch Object | upsert cols 9-18 plus `last_checked: now()`, merge-duplicates | 9-18 | `!!{{f_fb_page_url}} \|\| !!{{f_count}}` | **Write abstains too** |

### Column 4 formula

```js
({{f_site_html}} || "")
  .replace(/\\\//g, "/")
  .match(/https?:\/\/(?:www\.)?facebook\.com\/([a-zA-Z0-9._-]+)/)?.[1] || ""
```

Then blank the slug if it is in the junk list: `sharer`, `plugins`, `tr`, `profile.php`, `groups`,
`photo.php`, `posts`, `videos`, `people`, `pg`.

### Column 7: the three gates

Over the SERP results, keep the first result where **all three** hold:

1. the facebook.com URL has **exactly one path segment**;
2. the title, lowercased and stripped to alphanumerics, contains the same normalization of the
   company name;
3. the **slug** starts with the second-level label of the domain, or is a prefix of it.

**Dropping the third gate is how a pottery studio got billed.** Never re-add a title escape hatch.

## Best-of-3 has no clean Clay equivalent

Options, in order of preference, none measured:

1. **Run the chain outside Clay and import the CSV.** This is what the shipped recipe does.
2. Three parallel AI columns plus a formula that picks the first passing one. Triples the AI cost.
3. One AI column, accepting the per-draft rate (roughly 2 in 3 usable), with the lint formula
   blanking the bad ones.

Whichever you pick, **the truth-judge column is not optional.**

## Push to your sequencer

Lead-level custom variable `{{ad_library_line}}`, from **column 15c**. Rendered as
`Noticed {{ad_library_line}}.`

## Smoke test

Run 10 rows and read the run counts before importing a list.

- Metered column ran on 100% of rows → your gate was written in prose. See the idiom table.
- SERP column returns junk for multi-word companies → the name was interpolated raw into a
  pre-encoded query string. Build it with `encodeURIComponent` in column 5.
- Charged events far exceed page count → `onlyTotal` was omitted.
