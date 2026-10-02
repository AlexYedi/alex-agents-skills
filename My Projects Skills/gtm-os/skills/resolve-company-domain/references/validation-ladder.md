# The validation ladder — probes, gates, entity rules, arms

Live-verified mechanics 2026-08-11; re-verify per workspace (costs and contracts
drift).

## Arms + costs (live)

| Arm | Cost | Role |
|---|---|---|
| Managed **Company Domain** (`Company Name` → `Domain`) | ~1 credit | candidate generator, name-only rows. Commodity by itself — this skill IS its verification lever |
| `http-api-v2` GET | free | the liveness probe — contract pinned live: 2xx → success with BODY ONLY (no statusCode/finalUrl fields); non-2xx → the action ERRORS with the status named ("Clay received a 404 error") + the error body. Status-honesty lives in the error channel; the final URL after redirects is recovered from the 2xx body's canonical/og:url tags. Set a User-Agent |
| DNS resolution (any tool) | free | NXDOMAIN / no-resolve pre-gate; dead domains grind scrapers for 60s+ while DNS answers instantly |
| `scrape-website` bodyText | ~1 credit | site-content check on survivors only (real enum: `bodyText`, `title`; invalid outputFields values silently no-op AND bill) |
| Managed **Enrich Company** | ~1 credit | entity corroboration ONLY — never liveness: it returns last-known firmographics for dead AND acquired companies (matches the entity, not the live site); read `website` (the `domain` field can echo a link-shortener) |
| Company search (identifier filter) | quota | secondary candidates only; recall-not-exact — can miss the canonical entity entirely and rank unrelated orgs above it; gate on match confidence, never position |

## The ladder, in order (cheap kills first)

1. **Normalize** (code): lowercase, strip scheme/`www.`/paths/query; registrable
   label via public-suffix-aware extraction (a naive `split(".")[-2]` kills
   co.uk-family domains).
2. **DNS / liveness probe** (free): NXDOMAIN → dead candidate. The HTTP probe's
   verdict channel: a non-2xx root ERRORS with the code named → dead/broken; a 2xx
   returns the (redirect-followed) body — read its canonical/og:url tags for the
   destination domain and validate THAT (brand→corporate redirects are normal; note
   the hop). A destination on social media or a registrar/parking body → inactive
   candidate, not an operating site.
3. **Site-content check** (paid, survivors only): homepage bodyText must plausibly
   BE the company — brand/name present (allowing rebrand/acquisition with
   reasoning), coherent business content, not a parking/for-sale/soft-404 body.
   Quote the line that convinced you into provenance.
4. **Semantic name↔domain match**: does the site represent the NAMED company —
   subsidiary and REBRAND acceptable with the reasoning stated; **acquisition is
   NOT a pass** — "X is now part of Y" / acquirer branding / redirect-to-acquirer
   means the X domain is stale: verdict `acquired`, acquirer domain as candidate.
   A similarly-named different business is the fail case. Name-boundary
   discipline: `<Name> Partners|Group|Capital|Holdings` and vessel/product
   designations are DIFFERENT entities.
5. **Operating-entity check** (judgment + optional corroboration): holding parent
   vs operating company vs franchise brand — say which the domain hosts; when the
   user's intent is unclear, resolve to the operating entity and flag the
   hierarchy. Corroborate with Enrich Company (`website` field) when the site is
   thin.

## The override bar and the zombie-site trap (iteration-3 rules)

- **An acquisition-language signal on the candidate's own page is overridden only by
  positive counter-evidence** — the language provably refers to a different entity,
  or to THIS company acquiring others. "Looks like boilerplate" is not
  counter-evidence: unresolved acquisition signals degrade the row to a flag
  (`acquired` if the acquirer is identifiable, `ambiguous` otherwise), never to a
  clean assertion.
- **A live site with a matching name is necessary, not sufficient, when any signal
  conflicts.** Zombie sites are real: acquired or defunct companies leave their
  marketing site running with no banner. When an acquisition flag, a liveness
  conflict, or staleness indicators (old copyright year, dead blog, stale news)
  exist on an otherwise-passing candidate, corroborate independently before
  asserting — the ~1-credit news screen ("<name> acquired OR shut down", past-year
  window) and/or Enrich Company's `website`. Corroboration clean → assert;
  corroboration reveals absorption/shutdown → the matching verdict; corroboration
  silent but the conflict stands → flag, don't assert.
- **Bot-blocked roots (403/429/challenge) are UNVERIFIED, not alive.** Without
  content evidence the confidence vocabulary cannot reach `validated`: corroborate
  independently (enrichment + hints) to assert at `corroborated`, else degrade to
  `ambiguous` with the block noted.
- **Probe surface unavailable = same discipline, different cause.** When the
  environment can't reach sites at all (egress-blocked agent; the HTTP probe
  behind a spent ad-hoc quota — the ladder's "free" column silently assumes an
  un-exhausted quota), rungs 2-3 are NOT skippable-as-passed: corroborate via
  enrichment to assert at `corroborated`, never `validated`, and say why. A DNS
  answer through a proxy can be synthetic — a half-signal, not liveness. Bonus
  while corroborating: the Enrich Company payload often carries the company's
  LinkedIn URL — harvest it into the row; downstream skills' high-accuracy arms
  (headcount, people finds) key off it for free.

## Ambiguity policy (the refusal gate)

- A common-word or multi-entity name (the lookup will still answer confidently) →
  `ambiguous` + candidate list (one evidence line each). Signals: the name is a
  dictionary word; hints (geo/industry) don't discriminate; two living candidates
  both pass content checks.
- Hints narrow BEFORE refusing: country/region, industry, a known person there, a
  LinkedIn company URL — each can pin the entity. Refuse only when hints are
  exhausted.
- The confidence vocabulary: `validated` (ladder passed on the site's own
  evidence) · `corroborated` (ladder + independent enrichment agree) — nothing
  weaker ships as resolved.

## Batch mechanics

Dedupe names first (case/suffix-insensitive: "Acme", "Acme Inc.", "ACME" are one
lookup). Free gates run across the whole batch before any paid step; paid
validation only on candidates that survived. Per-call cost from usage metadata
where the surface exposes it (the routines surface exposes none — declared
estimate, say so). CLI envelope for the managed function:
`{"items":[{"id":"<key>","inputs":{"Company Name":"..."}}]}` via `--input -`;
gate on an actual domain value in the payload, never run status (complete + empty
is the routine miss shape).
