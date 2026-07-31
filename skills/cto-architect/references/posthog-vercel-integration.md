# PostHog + Vercel integration — key model & gotchas

Hard-won reference for wiring **PostHog telemetry** (capture + read) and deploying a **Next.js app on
Vercel** that reads it. Distilled from a real debugging session — every item below cost time to learn.
Read this before wiring PostHog into a project or debugging "why are my dashboard panels empty / why did
the preview build fail."

---

## 1. PostHog has three key types — use the right one for each job

| Key | Prefix | Level | Use it for | Do NOT use it for |
|---|---|---|---|---|
| **Personal API key** | `phx_` | account (the user) | **Reading data out** via the query API (HogQL) | capture |
| **Project API key / token** | `phc_` | project (public) | **Capturing/ingesting** events (`/capture/`) — write-only | reading |
| **Project secret key** | `phs_` | project (secret) | feature-flag local eval / secure server SDK | **the query API rejects it** |

**The load-bearing fact:** the query/read API accepts **only a personal `phx_` key**. There is no
project-level key that can read via the query API. A `phs_` project-secret key returns
`"Personal API key ... is invalid"` from the query endpoint. So the read path is *always* a personal key;
achieve least-privilege by making that personal key **read-only + scoped to one project**, not by reaching
for a project key.

## 2. The read-path 403 is usually project-**access**, not a missing scope

A scoped personal key can be valid, in the right org, and still 403 with
`"API key does not have access to the requested project: ID <n>"`. That is the key's **project-access list**
excluding the project — a different setting from its permission **scopes**. To read, the `phx_` key needs
**both**: project `<n>` in its org/project access **and** the `query:read` scope. (Symptom of a scoped key:
`GET /api/projects/` returns `"API keys with scoped projects are only supported on project-based endpoints"`
— proof it's scoped, not that it's broken; `GET /api/users/@me/` still succeeds.)

## 3. Canonical env-var set (for a capture-in-one-repo, read-in-another setup)

Both repos of a "pipeline captures telemetry → dashboard reads it" loop must point at the **same** project
(they're two ends of one stream; different projects → the dashboard reads an empty project):

```
POSTHOG_PROJECT_TOKEN      # phc_  — capture (the pipeline's hooks POST to /capture/)
POSTHOG_PERSONAL_API_KEY   # phx_  — read   (the dashboard's query API; scoped to the project + query:read)
POSTHOG_PROJECT_ID         # numeric project id, goes in the query URL
POSTHOG_HOST               # e.g. https://us.posthog.com
```

## 4. Verify capture and read independently before building UI

```bash
# CAPTURE (phc_ token) — 200 {"status":"Ok"} proves the token + project accept ingestion
curl -sS -X POST "$POSTHOG_HOST/capture/" -H "Content-Type: application/json" \
  -d "{\"api_key\":\"$POSTHOG_PROJECT_TOKEN\",\"event\":\"wiring_test\",\"distinct_id\":\"check\"}"

# READ (phx_ personal key) — 200 with results proves scope + access; 403 = fix key project-access/scope
curl -sS -X POST "$POSTHOG_HOST/api/projects/$POSTHOG_PROJECT_ID/query/" \
  -H "Authorization: Bearer $POSTHOG_PERSONAL_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":{"kind":"HogQLQuery","query":"select count() from events"}}'
```
Note: `/capture/` returns 200 even for a bad token (ingestion is async) — so a 200 there proves the pipe
is reachable, not that the token is valid. A brand-new project's query engine can also time out for a few
minutes while ClickHouse materializes — that's warm-up, not a wiring bug.

---

## 5. Vercel: data env vars set only for Production break EVERY PR preview build

If a page reads a required env var at module-eval/build time (e.g. a Notion/DB client that throws
`Missing required env var: X` when unset), and that var is set **only** for the Production environment, then
**every Preview (PR) deployment fails to build** — even though Production is fine. The fix is to **replicate
the data vars to the Preview environment** too. (The failure looks like it's caused by the PR, but it's a
pre-existing Preview-env gap — confirm by noting Production builds/serves fine.)

## 6. The Vercel CLI can't set "all Preview branches" non-interactively — use the REST API

`vercel env add NAME preview` (and even `... --yes`) returns `git_branch_required` — it wants a specific git
branch and won't apply to "all Preview branches" in a script. Per-branch is useless (future PRs have new
names). Use the **REST API**, which takes `target: ["preview"]` directly:

```bash
# token = the CLI's own stored auth (macOS): ~/Library/Application Support/com.vercel.cli/auth.json -> .token
# projectId + teamId (orgId) are in the repo's .vercel/project.json
curl -sS -X POST "https://api.vercel.com/v10/projects/$PROJ/env?teamId=$TEAM" \
  -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"key":"NOTION_TOKEN","value":"...","type":"encrypted","target":["preview"]}'
```
The same API reads (`GET /v9/projects/{id}/env`), scopes (`PATCH .../env/{id}` with `{"target":["preview"]}`),
and deletes. Note: Vercel will **not** return a decrypted secret value even to you (`?decrypt=true` comes
back empty) — so you can't silently migrate a value you don't already hold.

## 7. Same key, different value per environment — the UI can block it; use a suffix + code fallback

Vercel's UI sometimes won't let you add a second entry for a key (e.g. `OPS_PASSWORD`) scoped to Preview
alongside the Production one. Workaround: store the preview value under a suffixed key (`OPS_PASSWORD_PREVIEW`,
scoped preview-only) and have the code fall back:

```ts
const password = process.env.OPS_PASSWORD ?? process.env.OPS_PASSWORD_PREVIEW;
```
Production is unaffected (`OPS_PASSWORD` wins there); Preview uses the suffixed value.

---

**Security posture:** capture tokens (`phc_`) are public/write-only by design. Personal read keys (`phx_`)
should be read-only + single-project scoped. Replicating data vars to Preview widens the blast radius
slightly (preview URLs are more numerous) but the exposure is the same server-only exposure as Production —
never shipped to the browser. Keep `/ops`-style surfaces gated regardless.
