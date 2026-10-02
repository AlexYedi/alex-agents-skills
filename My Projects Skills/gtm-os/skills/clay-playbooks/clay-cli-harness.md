# Clay CLI harness (workflow-driven)

The generic procedure for building **any** playbook's signal as a Clay **workflow**, entirely from
a terminal. Read this once. Then read the playbook's own `clay-workflow.md` for its node graph,
its action keys, and its prompt.

## What the CLI can and cannot build

| Object | Buildable from the CLI? |
|---|---|
| **Workflows** | **Yes.** `create`, `nodes create/update/delete`, `publish`, `runs` |
| Tables and columns | No. Read-only (`list`, `get`, `columns`, `rows`, `query`). Build them in the UI — see `clay-table-harness.md` |
| Functions | No. `list` and `get` only. Existing functions can be *invoked*, never created |

So: if you want a playbook under version control and buildable by a script, build it as a
**workflow**. If you want it visible as columns next to the leads, build it as a **table**.

## Command surface

```bash
clay whoami                                    # confirm workspace before you write anything
clay credits                                   # balance

clay workflows create --name "<name>"          # -> {id, name, url}
clay workflows nodes create <wfId> --input <json|file|->
clay workflows nodes get    <wfId> <nodeId>
clay workflows nodes update <wfId> <nodeId> --input <json|file|->
clay workflows nodes delete <wfId> <nodeId>
clay workflows nodes test   <wfId> <nodeId> --source-run <runId>
clay workflows publish <wfId>
clay workflows diagram <wfId>                  # mermaid, good for a sanity read
clay workflows actions list                    # the full action catalog, greppable JSON
clay workflows actions schema <packageId> <actionKey>
```

Node specs are **dynamic per node type and resolved per workspace**. Before creating a node type
you have not built before, read an existing one to see the real shape:

```bash
clay workflows nodes get <wfId> <nodeId> | jq '.node'
```

Use `nodeType` and `name` in the spec. **Not** `type` and `title` — those are silently wrong.

## Finding the right action

Every tool node wraps an action identified by a `packageId` + `actionKey` pair. Dump the catalog
once and grep it:

```bash
clay workflows actions list > catalog.json
jq -r '.. | objects | select(.actionKey) | "\(.packageId)\t\(.actionKey)"' catalog.json | sort -u
```

The generic building blocks live in one core package (`4299091f-3cd3-4d68-b198-0143575f471d`) and
are what most playbooks use:

| actionKey | What it does | Credits |
|---|---|---|
| `http-api-v2` | arbitrary HTTP request | **0** |
| `scrape-website` | fetch and parse a web page | metered |
| `check-url` | does this URL resolve | cheap |
| `get-sitemap` | list a site's URLs | cheap |
| `extract-field-from-object` | pull one field out of a blob | free |
| `categorize-by-keywords-v2` | keyword classification | free |
| `clay-normalize-first-and-last-names` | name cleanup | free |
| `score-your-data` | weighted scoring | free |

Others the playbooks reach for, by package:

| actionKey | Package prefix | Used by |
|---|---|---|
| `enrich-company` | `e5f3b09f` | most company-level playbooks |
| `find-people-lookalikes` | `e251a70e` | lookalikes |
| `cpj-find-lists-of-jobs`, `enrich-job` | `e251a70e` | hiring-surge, job-posting-language |
| `find-google-news-results` | `28d4ca01` | fundraising |
| `social-posts-get-post-activity-*` | `b210a16b` | linkedin-engagement, social-posts |
| `apify-run-actor` | `ea91b0b8` | ad-library, any LinkedIn-live source |
| `prospeo-find-people-at-company` | `48a31bbb` | name-to-other-prospects |

Then read its exact input schema before you write the mapping:

```bash
clay workflows actions schema 4299091f-3cd3-4d68-b198-0143575f471d http-api-v2 | jq '.inputParameters'
```

## The build, step by step

### 1. Create the workflow

```bash
WF=$(clay workflows create --name "Playbook: new in role" | jq -r '.id')
echo "$WF"
```

### 2. Add nodes in graph order

Each playbook's `clay-workflow.md` gives the node list. Create them top to bottom; positioning and
edges are handled server-side.

```bash
clay workflows nodes create "$WF" --input '{"nodeType":"tool","name":"Fetch source"}' | jq -r '.nodeId'
```

### 3. Wire the inputs — this is where builds actually fail

**Tool nodes cannot read trigger variables directly.** A `{{var}}` in a tool's mapping config
resolves to undefined unless the variable is *pinned* on the consuming node's `inputSchema` with
`sourceNodeId` + `sourcePath`. Multi-hop back through the graph is fine. The symptom when you get
this wrong is `missing required inputs: <name>`, which reads like a schema problem and is actually
a wiring problem.

The pattern, in two parts:

1. Pin the value onto the node's `inputSchema`, naming its `sourceNodeId` and `sourcePath`.
2. Reference it by name in `tools[].inputMappingConfig`:
   ```json
   {"type": "reference", "expression": "{{name}}"}
   ```

**Object-valued parameters** — `headers`, `body`, anything nested — need a map, never a JSON
string:

```json
{"type": "map", "entries": {"Content-Type": {"type": "literal", "value": "application/json"}}}
```

**Always set `automapInputs: false` on tool nodes.** The default is `true`, which lets the model
auto-fill inputs from run context. With a large input such as a multi-kilobyte prompt it stuffs
that into headers and the call dies with `HTTP 431 Request Header Fields Too Large`. That error
always means "automap injected your whole context", never what it appears to mean.

### 4. Send `inputSchema` and `outputSchema` in separate calls

⛔ Sending both in one `nodes update` call **silently drops `inputSchema`**. It reports success for
both, then persists `inputSchema: null`. The node runs with empty inputs and every lookup returns
nothing, which looks like a logic bug and is a wiring bug.

Send them in two calls, then read the node back and confirm both persisted.

### 5. Know the code-node sandbox limits

Playbooks use code nodes for deterministic fields: date math, enums, counts, string cleanup.

- **No `datetime`.** `import datetime` fails at module level. Use
  `time.strftime("%Y-%m-%d", time.gmtime())`.
- `time`, `re`, `unicodedata`, `json`, `math`, `os` are available.
- **No `urllib`, no outbound HTTP, no pip.** Hand-roll percent-encoding if you need it.
- ⚠️ **`run_code` is not a faithful preview** — its sandbox *does* have `datetime`, so code that
  passes `run_code` can still fail inside the node. Only a real run proves a code node.
- `outputSchema` is enforced: every declared key must be returned, or the node fails with
  `Structured output validation failed`.

### 6. Understand the graph rules

- **Fan-in works.** A node with many incoming edges fires on **first arrival** and does not wait
  for the others. Pins from branches that never ran resolve as *absent*, not null, and do not
  block. So "collect the winner in one node with pins from every branch" is a valid pattern and
  saves duplicating terminal nodes.
- **Tool instances are not shared across nodes.** Reusing an `actionKey` creates a fresh tool per
  node, so N nodes can map the same action to different inputs with no cross-contamination.
- **Deleting a node NULLs the `inputSchema` of downstream nodes.** The cascade wipes pinned
  inputs; the node then runs and returns all-empty fields **with no error**. After any deletion,
  re-read and re-apply `inputSchema` and `automapInputs` on everything downstream.
- **A routine returns the LAST executed node's output.** If your success path ends on an HTTP
  node, callers get the raw HTTP response instead of your data. Give **every** terminal path its
  own node with a matching `outputSchema`, so all branches return one contract.

### 7. Output paths

Tool node outputs are at `$.result.<field>`, with the success flag at `$.success`. An HTTP node
with `returnResponseMetadata: true` gives `$.result.body.<field>` and `$.result.statusCode`.
Confirm the real paths from `recentOutputPaths` after one run rather than assuming.

### 8. Publish and run

```bash
clay workflows publish "$WF"
```

⚠️ **`clay workflows runs test` is currently broken** (it errors with
`userId: expected number, received string`). Run through a routine instead — which is also how you
call the playbook from anything else:

```bash
RT=$(clay routines create workflow "$WF" --name "new-in-role" | jq -r '.id')

# 1 to 100 rows inline
clay routines runs start "$RT" --input '{"items":[{"domain":"example.com"}]}'

# bulk, one JSON object per line
clay routines runs start "$RT" --bulk rows.jsonl
```

A published workflow routine is callable exactly like a function routine, which makes it the only
agent-buildable, scriptable route into Clay.

### 9. Smoke test on 5 rows

Same rule as the table harness: run 5, read the output, then scale. The specific failures to look
for are in step 3 (unbound inputs), step 4 (dropped `inputSchema`), and step 5 (`datetime`).

## Cost and safety notes

- **`http-api-v2` costs 0 Clay credits** and parses responses as JSON. An **HTML** response comes
  back as `body: {}`, so it cannot be used to scrape web pages. Use `scrape-website` for HTML.
- **Set `removeNull: true` on any HTTP node that writes to a database.** Otherwise empty inputs
  are sent as `""` and overwrite good rows with blanks.
- When you write back to a cache or a CRM, write the **original** string casing, not values you
  normalized internally. A normalize-then-upsert pipeline will happily lowercase every name it
  touches.
- Clay may auto-bind an existing HTTP app account to a new `http-api-v2` tool. It does not inject
  headers into the request, but check the auth behavior before you trust a call.
- **Never put a credential in a node body.** Build secret-bearing URLs and bodies inside a code
  node reading from workspace secrets, and pin the single resulting string onto the HTTP node.

## Gotcha table

| Symptom | Cause | Fix |
|---|---|---|
| `missing required inputs: x` | tool node reading a trigger var directly | pin it on `inputSchema` with `sourceNodeId` + `sourcePath`, step 3 |
| `HTTP 431 Request Header Fields Too Large` | `automapInputs` left at `true` | set it `false`, step 3 |
| Node returns all-empty fields, no error | `inputSchema` was dropped, or a delete cascade nulled it | steps 4 and 6 |
| `Structured output validation failed` | a declared `outputSchema` key was not returned | return every declared key, step 5 |
| `ModuleNotFoundError: datetime` | code sandbox has no `datetime` | use `time.strftime`, step 5 |
| Code works in `run_code`, fails in the node | `run_code` sandbox is richer than the node's | trust only real runs, step 5 |
| HTTP node returns `body: {}` | response was HTML, `http-api-v2` parses JSON only | use `scrape-website` |
| Caller gets a raw HTTP response | terminal path ended on the HTTP node | give every terminal path its own output node, step 6 |
| Good rows overwritten with blanks | `removeNull` not set on a DB write | set `removeNull: true` |
| `runs test` errors on `userId` | known CLI break | publish, create a routine, `routines runs start` |
