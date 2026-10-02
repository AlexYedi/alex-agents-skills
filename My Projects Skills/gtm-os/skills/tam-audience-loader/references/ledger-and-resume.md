# The ledger, the shards, and picking up where it died

A TAM load is long, interruptible, and duplicating ten thousand companies is not something anyone
gets to take back. So the design constraint is not throughput — it is that **the only state that
matters is on disk, and "what is left" is recomputed from it rather than remembered.**

## One line per row, written the moment it settles

The ledger is JSONL, append-only, never rewritten in place. A line goes down as soon as a row
reaches a verdict — not at the end of a batch, not when a shard finishes. A batch held in memory is
a batch lost when the process dies, and the process dying is the case this is designed for.

```
{"row_key":"northwind","status":"completed","run_id":"<run id>","entity_id":900100200,
 "match_key":"domain","match_value":"northwind.example","associated":null,
 "dropped_fields":["employee_count"],"fields_written":4,"reason":"","at":"2026-05-04T11:02:19Z"}
```

| Field | |
|---|---|
| `row_key` | the row's key in the file. The ledger is indexed on this |
| `status` | one of the six below |
| `run_id` | the Clay run, so a verdict can be opened later with `clay workflows runs steps` |
| `entity_id` | the Clay record id the upsert returned. **On companies this is the read-back** |
| `match_key` / `match_value` | which of Clay's fixed keys this row was matched on, and with what |
| `associated` | contacts only — `true`, `false`, or `null` on a company line |
| `dropped_fields` | values omitted because they would not parse as their field's type |
| `fields_written` | what the action reported it updated. Informational: see the caveat below |
| `reason` | why, on a `rejected_*`; empty otherwise |

**`fields_written` is not evidence the values landed.** It counts what was sent and accepted. The
count that matters comes from Clay at Step 8.

## Six verdicts, four of them settled

| Status | Settled | Meaning |
|---|---|---|
| `completed` | yes | a terminal writer step reported `completed` |
| `rejected_no_match_key` | yes | the row carries none of Clay's fixed keys. **Never fired** — screened in the driver |
| `rejected_duplicate_row_key` | yes | a second row with a row key already seen in this file |
| `skipped_no_company` | yes | a contact whose company never loaded, under the flag that holds rather than loads such contacts |
| `failed` | **no** | a step errored. Stays in the work set |
| `timeout` | **no** | no terminal step inside the poll budget. Stays in the work set |

Two rules follow, and the second is the expensive one:

- **Only settled verdicts remove a row from the work set.** A re-run refires everything else.
- **Do not "fix" a transient failure before retrying it.** Failures arrive in bursts and clear on
  their own. Diagnosing one before re-running it is how a day goes.

**Screen the permanent failures in the driver rather than learning them from Clay.** A row with no
match key, and a contact whose company id is blank, both come back as `failed` steps — the same
shape as a network blip, and a driver that retries everything non-terminal retries them forever.
Neither should ever be fired.

## Recomputing what is left

```python
settled = {}
for line in open(ledger):
    try:
        r = json.loads(line)
    except ValueError:
        continue                     # a torn last line is normal after a kill
    if r.get("status") in SETTLED:
        settled[r["row_key"]] = r    # later lines supersede earlier ones
todo = [row for row in rows if row["row_key"] not in settled]
```

Three properties this relies on and one it tolerates:

- **Last line wins.** A row can legitimately settle twice — a forced re-run, a corrected export —
  and the later line is the current truth.
- **A torn final line is survivable.** A process killed mid-write leaves partial JSON; skipping an
  unparseable line costs one row, which the next pass refires.
- **The work set is derived, never stored.** There is no "remaining" file to fall out of sync.
- **A re-run over an untouched file writes nothing**, because every row is already settled. That is
  the test that the row key is stable — if a re-run creates records, the row key is not doing its
  job and the load should stop until that is understood.

## Shards

Concurrency is **process-based, over disjoint inputs**. Split the remaining work with a strided
slice — `todo[i::n]` — write one file per shard, and run one process per file. Each shard owns rows
no other shard will touch, so appends to a shared ledger never collide on content, and no lock is
needed.

**Eight shards, one row per second per shard.** That number is carried over from a load of about
nine thousand records driven by different code against a different workflow: four was slow, and
sixteen was watched turning a failure rate of about 1% into 15% on contention. **It is borrowed, not
measured here** — say so when you use it, and treat a rising failure rate as the signal to come
down rather than as something to retry through.

Detach so that the shards outlive the session that started them:

```
nohup python3 scripts/load_drive.py --entity companies --shard 3 --of 8 … > logs/co-3.log 2>&1 < /dev/null & disown
```

A shard is a child of the shell, not of the conversation. `nohup … & disown` is what keeps a load
running when the session ends; without it, closing the session kills the load mid-row. Nothing is
lost either way — the ledger has every settled row — but restarting eight shards is avoidable.

## The resume breadcrumb

The driver writes `RESUME.md` beside the ledger on start and rewrites it on exit. It holds four
things and no narrative:

1. **Where the state is** — the ledger paths, the mapping file, the build state.
2. **What is settled and what is left**, as counts by status, recomputed from the ledger at the
   moment it was written.
3. **The exact next command**, copy-pasteable, with every path filled in.
4. **What must not be repeated** — that the fields exist, that the workflows exist and are
   already built, and that re-running the build would create a second set.

The bar it has to clear: someone opening a cold session, reading one file, and continuing without
asking anything. A breadcrumb that says "resume the load" and not which command has not cleared it.

## Two things a re-run must not do

- **It must not rebuild.** `build-state.json` is how a second run knows the fields and the workflows
  already exist. If it is gone, treat it as a new build and say so — do not infer a graph you
  cannot see, and do not create a second one beside the first. **This is also why the workflows are
  worth keeping**: with that file and those graphs, a later load of a different file is a driver
  invocation rather than a build.
- **It must not widen the mapping without saying so.** A re-run with more columns than the first is
  a new set of fields and a different load. That is allowed; it is not allowed to be quiet.
