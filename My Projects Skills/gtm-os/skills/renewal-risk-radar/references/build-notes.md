# Build notes — CRM intake, the weekly workflow, and per-signal routing

Mechanics only. The decisions live in `SKILL.md`; this file is what to type and what has bitten
builds before. Everything here is a starting point to **re-verify** against the installed CLI version,
never a substitute for the live pull.

## Asking which CRM without demanding a recital

A skill authenticated to a CRM can usually **read** that CRM's shape, so do not ask the installer to
type field names from memory. The flow:

1. **Name the shape** — the four fields in `SKILL.md` Step 1 (account id+name, renewal date, owner,
   champion contact), each with what it is for.
2. **Read their system.** Ask which CRM they run (a trigger phrase, not a dependency — this skill is
   CRM-agnostic), then read the account object's schema through the connected account.
3. **Show the mapping you found** — which of their fields you matched to each row, and which you could
   not.
4. **Ask only about the unmatched rows**, and gate the judgment calls (windows, rules, model) that no
   schema can answer.

Where the CRM cannot be introspected, ask for a pasted field list or one sample record and map from
that — still far better than a vague "tell me your fields". Never let the input degrade into a
loosely-worded request; that just moves the guess somewhere nobody can see it.

The champion is the field most often *not* a field: it may be a contact **role** on the account, a
tag, or a named person. Read how they record it; if nothing records it, the champion-change signal is
`unmeasured` for those accounts and the digest says so.

## The weekly workflow — node graph and the traps

Confirm the node commands on the installed version before wiring anything:

```
clay workflows nodes --help
clay workflows nodes ...        # create/update/test as the installed version exposes them
```

A skill that routes only to plugin tools is a dead end on a machine with no plugin; build real nodes.

Graph, left to right:

```
schedule trigger (weekly)
  → code node: scope the book to the renewal window (read CRM, drop out-of-window/renewed)   [free]
  → per account, fan out to three enrichment tool nodes (the three signals)                  [paid]
  → merge the three results per account
  → code node: combine signals + rank (all judgment lives HERE, never an LLM node)           [free]
  → write node: digest table you own  (+ optional Slack/email delivery)                       [no CRM write]
```

Four node behaviours that have cost real debugging — design around them, do not discover them:

- **An asymmetric merge node stays pending forever.** If one arm can produce no row (e.g. an account
  with no champion), a merge that waits for all arms never completes. Make every arm emit a row —
  including an explicit `unmeasured` row — so the merge is symmetric.
- **A tool node does not echo its own inputs.** Fields from the trigger (account id, renewal date) do
  **not** ride through a tool node to later nodes. Carry them forward explicitly in a code node, or
  re-join on the account id after the tool node.
- **A pin two hops back resolves to null.** Reference the immediately-preceding node's output; if you
  need something older, thread it through each hop rather than reaching back.
- **Tool-node pins need `$.result`; code-node pins need `$`.** Mixing them is a silent null.

Idempotency: on the stateless (recent-window) model a re-run recomputes and overwrites the week's rows
— safe. On the stateful (compare-to-last-week) model you must persist last run's per-account snapshot
and read it back; handle a skipped run (a two-week gap must not read as "no change") and a duplicated
run (do not double-count). Diff on the **provider's signal date**, not the run date.

## Per-signal routing — resolve names and costs live

For each signal, resolve the function by the pair `(packageId, actionKey)`, read the input schema, and
record: what runs, what goes in, what to verify, what it costs. `paymentType` before `creditCost`;
watch for per-unit rates whose basis is in a parameter description; budget for billed misses
(`success: true, result: {}` can still cost a credit; `SUCCESS_NO_DATA` with `isRefunded: true` is
free).

| Signal | Job to route | Input (declared) | Verify in response | Cost note |
|---|---|---|---|---|
| Champion changed employer | detect a contact job change | champion identity | new employer ≠ account; carry the provider's signal date; if no champion → `unmeasured` | per-contact; a change-detection arm may bill per result |
| Headcount fell | current headcount + trailing-90d figure | account domain | both figures present (null horizon ≠ 0); numeric compare; prefer exact count over band string | per-company |
| Company went quiet | recent public activity (news / hiring / exec posts) | account domain | "no activity found" ≠ "arm returned nothing"; date the last activity | waterfall the boolean + evidence only; never the count you rank on |

Route by the input the installer holds (a domain vs a contact), not by what a lookup returns — that
keeps the build deterministic. Fail loudly when a named function is absent; never silently substitute
the nearest arm — a substituted liveness probe fills every row and asserts dead companies are alive.
