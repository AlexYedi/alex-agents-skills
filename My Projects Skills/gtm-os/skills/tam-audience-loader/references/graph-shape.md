# The two loader graphs, and the six things that fail silently

Everything here was confirmed against a live workspace by building it and running rows through it.
Where a claim came from documentation rather than a run, it says so.

## Why there is a matrix at all

Clay's audience upsert matches an existing record on a **fixed** set of keys, and every key you
select becomes a **required** input that rejects an empty string. Both halves were measured:

- Selecting `["email","linkedin_url"]` and sending a blank `linkedin_url` failed with
  `missing required inputs: lookupFields|linkedin_url`. The node never ran.
- Sending a blank `domain` on a company failed the same way.

So you **cannot** select several keys and let whichever is present win. One writer node per match
key. Doubled on the contacts side, because the company association is a separate required-when-present
value, giving the matrix below.

| | Match keys | Association | Writers |
|---|---|---|---|
| Companies | `domain`, `linkedin_url` | none — companies do not associate to anything | 2 |
| Contacts | `email`, `linkedin_url`, `phone` | linked / unlinked | 6 |

`associations` resolves to exactly one field, `associations|accountId`, and only for contacts. That
is not documented; it comes off the action itself:

```
clay workflows actions dynamic-fields <packageId> upsert-audiences-record associations \
     --type input --inputs '{"entityType":"CONTACT"}'
```

which returns `associations|accountId` — *"Audiences company ID · Associate this person with an
existing Clay company"*. The same call with `ACCOUNT` returns nothing.

## Resolve the action; never pin it

```
clay workflows actions list      # dump once, then grep it
```

Take `packageId` and `actionKey` for `upsert-audiences-record` from that dump. **If it is not there,
stop and say so.** A remembered package id builds a graph against the wrong action in any workspace
that does not match the one it was written in, and the graph validates perfectly either way.

The action declares one output, `entityId`. Read it at `$.result.entityId` — and in a run's steps,
at `stepOutputs.result.entityId`. That value is the whole company read-back: it comes back from the
company's own write, free and synchronously, so nothing needs to look a company up again later.

## Shape

Both graphs are the same three layers.

```
Webhook trigger  ──▶  Router (conditional, rules)  ──▶  one writer per route
                                                   └─▶  Reject (code node, raises)
```

**Companies**

| Node | Route condition | What it writes |
|---|---|---|
| `Route by match key` | rules on `match_key` | — |
| `Write company by domain` | `match_key` Equal `domain` | lookup `domain`; the confirmed record fields |
| `Write company by LinkedIn URL` | `match_key` Equal `linkedin_url` | lookup `linkedin_url`; the same record fields |
| `Reject — no match key` | default route | raises with the row key in the message |

**Contacts** — the same, with six writers keyed on `match_key` **and** whether `company_record_id`
is non-empty. The linked writers carry `associations|accountId`; **the unlinked writers do not carry
the key at all.** Not blank. Absent.

The driver decides the route and sends `match_key` as a field, so the **order the keys are tried is
a run flag, not a property of the graph**. Changing the order never rebuilds anything.

## The exact mapping for one writer

Everything goes in the tool's `inputMappingConfig`. References resolve straight off the trigger
fields by name — this was tried and works; no `inputSchema` entry is needed on the tool node.

```json
{
  "entityType":                          { "type": "static",    "value": "ACCOUNT" },
  "lookupFields|selectedLookupFields":   { "type": "static",    "value": ["domain"] },
  "lookupFields|domain":                 { "type": "reference", "expression": "{{domain}}" },
  "recordFields|selectedRecordFields":   { "type": "static",    "value": ["org_name", "domain"] },
  "recordFields|org_name":               { "type": "reference", "expression": "{{org_name}}" },
  "recordFields|domain":                 { "type": "reference", "expression": "{{domain}}" },
  "recordFields|removeNullValues":       { "type": "static",    "value": true }
}
```

Three invariants:

- **Every id in a `selected*` array needs a matching `<group>|<id>` binding**, or the action returns
  `ERROR_BAD_REQUEST`.
- **`selectedRecordFields` and `selectedLookupFields` must be `static`.** Passed as a reference they
  resolve to nothing, and the action writes only the lookup field while still reporting success.
- **`removeNullValues: true`.** This is what makes blank *record* fields safe: they are dropped and
  the write succeeds with a lower `fieldsUpdatedCount`. It does nothing for lookup fields, which are
  required regardless.

A contact writer is identical with `"CONTACT"`, its own lookup key, and — on the linked variants
only — `"associations|accountId": { "type": "reference", "expression": "{{company_record_id}}" }`.

## Discovering the field ids to put in `selectedRecordFields`

```
clay audiences fields list --entity-type companies
clay audiences fields list --entity-type people
```

**Names are not ids.** Company "company name" is `org_name`. Read the catalogue; never guess an id
from a display name, and never assume the name you asked `fields create` for is the name you got —
a name already in use is silently suffixed.

Which fields a selection reveals can be confirmed the same way the association was:

```
clay workflows actions dynamic-fields <packageId> upsert-audiences-record recordFields \
     --type input --inputs '{"entityType":"ACCOUNT","recordFields|selectedRecordFields":["org_name"]}'
```

`recordFields|removeNullValues` only appears once record fields are selected.

## The six that fail silently

1. **A blank `associations|accountId` writes nothing.** Not an unlinked contact — no contact.
   `ERROR_BAD_REQUEST … expected number to be >0`, the step reports `failed`, the record count does
   not move. This is why unlinked contacts need their own writer with the key absent.
2. **A blank lookup value fails before the node runs.** `missing required inputs: lookupFields|<key>`.
   Also a `failed` step. Both of these are **permanent** failures wearing the costume of a transient
   one, so a driver that retries everything non-terminal will retry them forever. Screen for a usable
   match key in the driver and never fire a row without one.
3. **A lookup value that is present but is not that KIND of thing fails too, and the wording hides
   it.** `None of the selected lookup fields contained a valid value to match on` — which reads as
   though the field were empty. Measured on all three key types: a malformed email, a phone with no
   digits, and a LinkedIn URL whose host is anything but `linkedin.com`. The surprise is the last
   one, because a `.example` **domain** and a `.example` **email** are both accepted, so this is not
   a check on whether the thing exists — only on whether it is the right shape. Screen for it
   locally and fall through to the next key in the order.
4. **A value the field's declared type cannot parse is accepted and then invisible.** Covered in
   `column-mapping.md`; it is the reason this skill exists in the shape it does.
5. **A schema write rebuilds the binding map from exactly what the call contained.** Send every
   mapping on every write, then read the node back. A partial write reports success and destroys
   what was omitted.
6. **Deleting a node can sever the trigger edge and orphan a sibling.** Watched: removing one writer
   left the graph answering `trigger_not_connected` and `Workflow has no initial node`, with the
   remaining writer still present and unwired. A trigger takes **one** outgoing edge, so the router
   is the only thing that should ever hang off it. After any node delete, re-validate and rewire.

## `Record was not upserted` — transient, and it has been misdiagnosed once already

A create can come back with `Tool execution failed with status: ERROR — Record was not upserted`
even though the row is sound. **It is transient and it self-heals.** Measured: a contact failed
this way twice in a row, two minutes apart; the identical payload succeeded later with no change to
anything.

**A repeated identical failure is not proof of a rule.** The run that hit it concluded that Clay
requires an email to create a person, because the failing contact had none and every contact that
succeeded had one. That conclusion was wrong, and it was disproved four ways in a few minutes:

| Test | Result |
|---|---|
| Create keyed on `linkedin_url`, no email at all | **works** |
| Same, plus a company association | **works** |
| The failing contact's exact payload, matched on `email` instead | works |
| The failing contact's exact payload, unchanged, re-fired later | **works** |

Two samples of one failure and a plausible story is how a load ends up fabricating email addresses
to satisfy a rule that does not exist. **Before concluding anything about the platform from a
failure, bisect it**: change one thing at a time — the match key, the association, the field set —
each with a fresh match value so every attempt is a real create rather than an update of what the
last attempt made.

So the handling is: leave it in the retry set, because it clears on its own. Count it separately at
delivery so a run of them is visible, and **do not describe it as a rule about emails, LinkedIn-only
contacts, or anything else the payload happened to contain.**

## Running a row, and knowing when it settled

```
clay workflows runs test <workflowId> --inputs '<one row as JSON>'   # returns runId
clay workflows runs steps <workflowId> <runId>
```

`runs test` without `--audience-segment` fires the **draft** through the manual trigger. That is why
neither workflow needs publishing.

A step carries `stepOutputs.isTerminal`. **Settle on that flag, not on the node's name.** Matching
terminal writers by name prefix is how a load ends up reporting every successful update as a
timeout — a name sliced to two characters never equals the one-character constant it is compared
against. `isTerminal` is structural and cannot drift when a node is renamed.

A row is settled when a step reports `isTerminal` with `status: completed`; read `entityId` from the
same step's `stepOutputs.result`. Anything else is retryable and stays in the work set.
