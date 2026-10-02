# The workflow, node by node

```
trigger (manual)
  │
  └─ 0a Intake ........................ code. One fan-in point. Turns "" into null.
       │
       └─ 1 Company gate .............. does this attendee have a company DOMAIN?
            │
            ├─ yes ─ 2 Company record .. upsert ACCOUNT, matched on domain
            │          │
            │          └─ 3 Linked router
            │               ├─ 4a Attendee by LinkedIn (linked)
            │               ├─ 4b Attendee by email (linked)
            │               └─ 4z Nothing to write        (default lane)
            │
            └─ no ── 5 Unlinked router
                         ├─ 6a Attendee by LinkedIn
                         ├─ 6b Attendee by email
                         └─ 6z Nothing to write           (default lane)
```

Eleven nodes plus the trigger. Every one of them is forced by something the platform does,
and each is a bug somebody already paid for.

## Why intake exists at all

Two reasons, and neither is tidiness.

**A trigger node can have only one outgoing edge**, so the fan-out has to start somewhere
else. And a trigger create mints its node **unconnected** — every run then dies with
"Workflow has no initial node", which names the wrong cause.

**The trigger's input schema must be COMPLETE, and re-sent on every build.** A key absent
from it is stripped at intake, so every pin downstream resolves to null. The version of this
build that created the trigger once and never touched it again had a specific, silent failure:
adding one column to the field plan wired it correctly through every node and it still
arrived null, because the trigger from the first build still carried the old key list. No
error, no warning — one empty column, for ever. Measured on five records. The build now
re-sends the schema every run and reads it back to confirm every key survived. Intake is wired from *every*
trigger node the graph has, not only the one the build created: binding a table adds its own
trigger node, and an edge list that omits it severs that binding on the next rebuild.

**It nulls every blank.** `removeNullValues` drops nulls but not empty strings, and a field
sent as `""` clears whatever the record already held. Doing it here means a caller who sends
an empty string is safe too.

The generated source imports nothing. The code runtime has no `datetime`, no `urllib`, no
`hashlib`, no `base64` — and the sandbox that tests code nodes has modules the runtime does
not, so a green test-run of a code node proves nothing about the runtime. The safe move is to
import nothing at all and do every piece of judgment in the driver, where it can be tested
offline.

## Why the company write is a separate node upstream

The association is a **record id**, not a domain — so the company record has to exist and
report its id before the person can be linked to it. The upsert returns `entityId` on the
write itself, so this costs no second lookup.

The linked writers read it at `$.result.entityId`. **A tool node's output is read at
`$.result.…`; an intake or trigger pin is read at `$.…`.** Mixing the two resolves to null,
and a null association writes no record at all — so a mis-wire here does not look like a
mis-wire, it looks like every linked attendee silently vanishing.

## Why four attendee writers

- Every selected lookup field is **required and rejects an empty string**, so one writer
  cannot choose a key at run time. One writer per key.
- A **blank association writes no record at all**, so linked and unlinked cannot be one
  writer with an optional field. That doubles it.

## Why every lane is conditional and nothing joins

A plain edge into a join **hangs the run** whenever a sibling lane is pending. So no lane ever
converges: each writer is the end of its own branch. The two `Nothing to write` nodes are
default lanes, not error handlers — **a conditional with no matching rule hard-fails the
run**, so every router needs a lane for the case its rules do not cover.

## What the build must send on every write

**Every pin, every time.** A schema write rebuilds the binding map from exactly what the call
contains: it reports success and destroys whatever the call omitted. And the reverse — a pin
that no `inputMappingConfig` reference uses is deleted on write, which the read-back then
reports as a lost pin. So each node pins exactly what it references and nothing "for
consistency", and every write is read back and verified.

An action parameter fed from an upstream node needs **both** an `inputSchema` pin **and** an
`inputMappingConfig` reference naming it. A pin alone is silently dropped, and the action runs
with that parameter empty — which, for a lookup, is indistinguishable from a genuine miss.

Other shapes with no documentation and no useful error:

- `toolType` goes **inside** each entry of `tools`, and the package key is
  **`actionPackageId`** — not `packageId`, which is what the action catalogue calls the same
  thing.
- `inputMappingConfig` lives **inside `tools[0]`**, never at the node's top level.
- **Every `recordFields|…` pin is `"type": "string"`**, including the pins for number and date
  fields.
- `upsert-audiences-record` additionally requires `recordFields|selectedRecordFields` (an
  array) and `recordFields|removeNullValues` (a boolean). Nothing reveals this until a run
  fails, and only the per-step read shows the error — the run-level read reports `failed` with
  an empty node list.
- `toolType` cannot be changed in place. Swapping a node's type means delete and recreate, and
  a live node cannot be trusted to report its own type — so the build records what it created
  and prefers that over a live read.

## Publishing

**A test run fires the draft; a routine run fires the published version.** An unpublished
graph therefore builds clean, validates clean, and writes nothing. The build says so rather
than publishing on its own.

## Driving it

A **manual** trigger, wrapped in a routine, driven one batch at a time — a routine refuses a
workflow with no manual trigger, and pins bind to one specific source node, so two triggers
would leave half the pins resolving to null.

Batches are capped at 100 items per inline run by the platform. Every verdict is appended to
the ledger the moment it settles, and only a **written** record settles: a failure stays in
the work set so the next run retries it untouched. Do not "fix" a transient failure before
retrying it.

Because every write is an upsert keyed on the attendee's own identifier, a lost ledger costs
redundant writes and never duplicates. The ledger is an optimisation, not a correctness
requirement — which is what makes the whole thing safe to interrupt.
