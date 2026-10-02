# Clay table build: Company Social Link Finding

Read [`../clay-playbooks/clay-table-harness.md`](../clay-playbooks/clay-table-harness.md) first.

⚠️ **Status: specification.**

## Where the columns go

A **company-level** table, not a person-level one. Six URLs per company, reused across every contact
there. Running this per person multiplies the cost by your contacts-per-company ratio for zero extra
information.

## Integration check

| Provider | Native? | Use |
|---|---|---|
| Company data / enrichment | often yes | the **native action** |
| The website fetch | — | **`scrape-website`**, never `http-api-v2` (it parses JSON and returns `body: {}` on HTML) |
| SERP | no | `http-api-v2` |
| The model | yes | native AI column |

## Columns

| # | Column | Type | Input | Run condition | Notes |
|---|---|---|---|---|---|
| 1 | Normalize a Domain | action | Website | none | free |
| 2 | Company Record | action | `{{Domain}}` | `!!{{f_Domain}}` | ⚠️ **bind results by PRIMARY domain only** |
| 3 | Site HTML | `scrape-website` | `https://{{Domain}}/` | `!!{{f_Domain}}` | **the strongest evidence in the chain** |
| 4 | Site Blocked | Formula | see below | `!!{{f_Domain}}` | catches the HTTP-200 challenge page |
| 5 | Site HTML (rendered) | HTTP API | rendering proxy | `{{f_SiteBlocked}} === true` | METERED. One call, never a retry loop |
| 6 | Links From Site | Formula | profile regexes over 3 and 5 | `!!{{f_SiteHTML}} \|\| !!{{f_SiteRendered}}` | **self-attested. Needs no model check** |
| 7 | Links From Record | Formula | pull the platform URLs out of column 2 | `!!{{f_CompanyRecord}}` | candidates only |
| 8 | Search *(per empty platform)* | HTTP API | `site:<platform> <company name>` | that platform still empty | one **simple** query. Never an OR chain |
| 9 | Ownership Verifier | AI | `SKILL.md` §6 prompt | **only on candidates from 7 and 8** | the paid column |
| 10 | company_*_url *(six columns)* | Formula | see the precedence rule below | none | the pushed fields |
| 11 | *_evidence *(six columns)* | Formula | which source won | none | **keep these** |

## Column 4: the challenge-page check

```js
(() => {
  const s = String({{f_SiteHTML}} || "");
  const status = {{f_SiteStatus}} || 0;
  if (status === 403 || status === 429) return true;
  // A bot interstitial is commonly served with HTTP 200. It yields zero matches
  // and otherwise looks exactly like a clean legitimate miss, which is how a
  // whole segment of blocked sites gets recorded as "no social accounts".
  if (s.length < 2000) return true;
  const CHALLENGE = ["just a moment", "checking your browser", "enable javascript and cookies",
                     "attention required", "verifying you are human"];
  const low = s.toLowerCase();
  return CHALLENGE.some(c => low.includes(c));
})()
```

## Column 10: precedence, and the X exception

```js
(() => {
  const site = {{f_LinksFromSite}}?.linkedin || "";      // self-attested, strongest
  const rec  = {{f_LinksFromRecord}}?.linkedin || "";
  const srch = {{f_SearchLinkedin}}?.url || "";
  const ok   = u => u && ({{f_Verifier}}?.[u]?.owned === true);
  // Site evidence wins outright and needs no verification.
  // Everything else must clear the ownership check.
  return site || (ok(rec) ? {{f_Verifier}}[rec].canonical_url
       : ok(srch) ? {{f_Verifier}}[srch].canonical_url : "");
})()
```

⚠️ **For X, drop the last two branches entirely:**

```js
{{f_LinksFromSite}}?.x || ""     // company-site evidence ONLY
```

X handles are short, recycled and squatted. A search for a brand returned a handle that **matched the
brand better than the real account does** and was titled "Bug Poc". **No verifier catches that,
because the handle really does look right.**

## The batching trap, if you backfill outside Clay

If you pre-fill column 2 from a batch script rather than a per-row action: a company-search endpoint
that accepts an array of domains may still be **hard-paginated at 25 results per page with no
page-size parameter.**

Posting 35 domains returned 25 results and `"total_page": 2`. **A 500-domain body returns 25 matches
and drops ~475 silently, with no error.**

Chunk to the page size **and** loop pages. **Read the pagination block on your very first call.**

## Credit gate

Column 5 (the proxy) fires only on genuinely blocked rows. Column 9 (the verifier) fires **only on
candidates that did not come from the company's own site** — which on a normal list is a minority of
values, because the site fetch wins most rows outright.

## Push

These are usually **not** pushed to a sequencer. They feed other playbooks. Store them on the company
record, **with the evidence column beside each one.**

Without the evidence column you cannot tell six months later whether a URL was self-attested or
scraped off a search page — and that difference decides whether it is safe to scrape behind.

## Smoke test

Run 10 domains including one you know is bot-protected.

- The blocked domain reports "no accounts" → column 4's challenge-page check is missing.
- An X handle appears that you cannot find on the company's own site → the X exception is not wired.
- The wrong company's LinkedIn appears → column 2 is binding on a secondary website field.
- Post URLs stored as profiles → the verifier's not-a-profile rules were trimmed.
