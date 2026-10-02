"""Drive the load: one workflow run per row, one ledger line the moment it settles.

    python3 load_drive.py --entity companies --state build-state.json \
            --csv <path> --map <mapping.json> --ledger ledger/companies.jsonl [--limit 10]

    python3 load_drive.py --entity contacts  --state build-state.json \
            --csv <path> --map <mapping.json> --ledger ledger/contacts.jsonl \
            --company-ledger ledger/companies.jsonl

    python3 load_drive.py verify --state build-state.json --map <mapping.json> \
            --ledger ledger/companies.jsonl [--contacts-ledger ledger/contacts.jsonl]

Nothing is held in memory: the remaining work is recomputed from the ledger on every start, so a
run that dies resumes and a settled row is never fired twice. Shard with `--shard i --of n` over
disjoint strided slices, which is why no lock is needed on the ledger.

`references/ledger-and-resume.md` carries the record shape, the settled-versus-retryable rule and
the resume breadcrumb this writes.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys
import time

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import loader_lib as L                                               # noqa: E402

CLI_ENTITY = {"companies": "companies", "contacts": "people"}


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def clay(*args, timeout=180):
    r = subprocess.run(["clay"] + list(args), capture_output=True, text=True, timeout=timeout)
    out = (r.stdout or "").strip()
    # `"" in "{["` is True, so an empty stdout would reach json.loads and crash with a
    # decode error instead of the CLI's actual message. Test for a first character first.
    if out[:1] and out[:1] in "{[":
        return json.loads(out)
    raise RuntimeError("clay %s: %s" % (" ".join(args[:3]), (r.stderr or out)[:300]))


# --------------------------------------------------------------------------- one row

def fire(workflow_id, payload):
    return clay("workflows", "runs", "test", workflow_id, "--inputs", json.dumps(payload))["runId"]


def settle(workflow_id, run_id, budget=120, interval=3):
    """Poll until a TERMINAL step reports completed, or the budget runs out.

    Settle on `stepOutputs.isTerminal`, never on the node's name. Matching terminal writers by
    name prefix is how every successful update in a load gets reported as a timeout, and a
    structural flag cannot drift when somebody renames a node.
    """
    waited = 0
    while waited < budget:
        time.sleep(interval)
        waited += interval
        try:
            steps = clay("workflows", "runs", "steps", workflow_id, run_id).get("data") or []
        except RuntimeError:
            continue                        # a read that failed is not a verdict
        for s in steps:
            out = s.get("stepOutputs") or {}
            if out.get("isTerminal") and s.get("status") == "completed":
                return "completed", (out.get("result") or {})
        if any(s.get("status") == "failed" for s in steps):
            errs = [e for s in steps if s.get("status") == "failed" for e in (s.get("errors") or [])]
            return "failed", {"error": (errs[0] if errs else "")[:300]}
    return "timeout", {}


def load_row(item, mapping, entity, state, ledger, company_ids, company_verdicts,
             hold_unlinked, budget):
    """Screen locally first. A row Clay would reject permanently must never be fired: it comes
    back as an ordinary `failed` step, identical to a network blip, and a driver that retries
    everything non-terminal retries it forever."""
    key = item["row_key"]

    if item["duplicate"]:
        return L.ledger_line(key, "rejected_duplicate_row_key", at=now(),
                             reason="a row with this key was already seen in this file")

    match_key, _ = L.choose_match_key(item["row"], mapping, entity)
    if not match_key:
        return L.ledger_line(key, "rejected_no_match_key", at=now(),
                             reason="carries none of %s" % ", ".join(L.MATCH_KEYS[entity]))

    company_id, unlinked_reason, link_source = None, None, None
    if entity == "contacts":
        ref = L.contact_join_key(item["row"], mapping)
        company_id = company_ids.get(ref) if ref else None
        if company_id is not None:
            # Where the company came from, read off its own ledger line rather than tracked
            # separately. `created_from` is written by the pre-pass; its absence means the
            # company came from the companies table.
            link_source = {"audience": "already_in_audience",
                           "contact": "created_from_contact"}.get(
                               (company_verdicts.get(ref) or {}).get("created_from"),
                               "company_table")
        if company_id is None:
            # Distinguish WHY, so "not every contact got a company" is answerable from the ledger
            # rather than from a debugging session. Three different causes, three different fixes.
            if not ref:
                unlinked_reason = "no_company_reference"
            elif ref in company_verdicts:
                unlinked_reason = "company_%s" % company_verdicts[ref].get("status", "unsettled")
            else:
                unlinked_reason = "company_not_in_company_ledger"
            if hold_unlinked:
                return L.ledger_line(key, "skipped_no_company", at=now(),
                                     reason=unlinked_reason)

    built = L.build_payload(item, mapping, entity, company_id)
    wf = state["entities"][entity]["workflow_id"]

    try:
        run_id = fire(wf, built["payload"])
    except (RuntimeError, subprocess.TimeoutExpired) as exc:
        return L.ledger_line(key, "failed", at=now(), reason=str(exc)[:200])

    status, result = settle(wf, run_id, budget)
    return L.ledger_line(
        key, status, at=now(), run_id=run_id,
        entity_id=result.get("entityId"),
        fields_written=result.get("fieldsUpdatedCount"),
        match_key=built["match_key"], match_value=built["match_value"],
        associated=(built["linked"] if entity == "contacts" else None),
        link_source=link_source,
        unlinked_reason=unlinked_reason,
        dropped_fields=built["dropped_fields"],
        reason=result.get("error", ""))


# --------------------------------------------------------------------------- the pre-pass

def lookup_company(key_type, value):
    """Find a company already in the audience by one of Clay's match keys. Free, read-only.

    Called once per DISTINCT company, never per contact — which is the whole reason this is a
    pre-pass rather than a node in the contacts graph. `clay audiences` shares a 60-calls-per-minute
    budget across the workspace, and a per-contact lookup at eight shards would spend it in
    seconds.
    """
    q = 'select from companies where %s = "%s"' % (key_type, str(value).replace('"', ""))
    try:
        data = clay("audiences", "records", "search-ids", "--query", q).get("data") or []
    except (RuntimeError, subprocess.TimeoutExpired):
        return None                          # a failed read is not evidence the company is absent
    return data[0] if data else None


def prepass(a):
    """Resolve the companies the contacts reference but the companies table does not contain.

    Three outcomes per distinct company, and the pre-pass exists so all three are known before a
    single contact is written: already in the audience, created here, or unresolvable.

    Anything it resolves is appended to the COMPANY ledger under the key the contacts load will
    look up, so the contacts phase needs no new logic and a re-run never repeats the work.
    """
    mapping = json.load(open(a.map, encoding="utf-8"))
    state = json.load(open(a.state, encoding="utf-8"))
    rows = L.keyed_rows(L.read_table(a.contacts_csv), mapping, "contacts")
    known = L.company_id_map(a.ledger)

    needed, no_key = {}, []
    for item in rows:
        if item["duplicate"] or not L.choose_match_key(item["row"], mapping, "contacts")[0]:
            continue
        join = L.contact_join_key(item["row"], mapping)
        if join and join in known:
            continue                         # the companies table already covered it
        ktype, kval, src = L.company_key_for_contact(item["row"], mapping)
        if not kval:
            no_key.append(item["row_key"])
            continue
        entry = needed.setdefault(join or kval, {"type": ktype, "value": kval, "source": src,
                                                 "name": "", "contacts": 0})
        entry["contacts"] += 1
        entry["name"] = entry["name"] or L.company_name_for_contact(item["row"], mapping)

    distinct = {(e["type"], e["value"]) for e in needed.values()}
    print("contacts referencing a company not in the companies table: %d, across %d distinct "
          "companies" % (sum(e["contacts"] for e in needed.values()), len(distinct)))
    print("contacts with nothing to identify a company by: %d" % len(no_key))
    if not needed:
        return 0

    resolved, created_keys, found, made, failed = {}, set(), 0, 0, 0
    for (ktype, kval) in sorted(distinct):
        eid = lookup_company(ktype, kval)
        if eid:
            found += 1
        elif a.create:
            name = next((e["name"] for e in needed.values()
                         if (e["type"], e["value"]) == (ktype, kval) and e["name"]), "")
            eid = create_company(state, mapping, ktype, kval, name, a.budget, a.dry_run)
            if eid:
                made += 1
                created_keys.add((ktype, kval))
            elif not a.dry_run:
                failed += 1
        if eid:
            resolved[(ktype, kval)] = eid
        print("  %-14s %-44s %s" % (ktype, kval[:44],
                                    eid or ("would create" if a.dry_run and a.create else "absent")))

    if not a.dry_run:
        for join, e in needed.items():
            eid = resolved.get((e["type"], e["value"]))
            if eid:
                # Ledgered under the key the CONTACTS load looks up, so that phase is unchanged.
                L.append_settled(a.ledger, L.ledger_line(
                    join, "completed", at=now(), entity_id=eid, match_key=e["type"],
                    match_value=e["value"],
                    created_from=("contact" if (e["type"], e["value"]) in created_keys
                                  else "audience")))

    if a.dry_run:
        # EVERY key in `distinct` is by definition identified — a contact with nothing to go on
        # never got here, it was counted in `no_key` above. An earlier version derived
        # "cannot be identified" as a remainder that only balanced when --create had run, so a
        # plain dry run reported identified companies as unidentifiable. A dry run's whole job is
        # to be trustworthy before you commit, and that number was wrong in the direction nobody
        # chases: it under-promised.
        print("\nalready in the audience: %d   would be created: %d"
              % (found, len(distinct) - found))
        print("(contacts with nothing to identify a company by are the %d counted above, and no "
              "flag changes that number)" % len(no_key))
        return 0
    print("\nalready in the audience: %d   created here: %d   could not create: %d   "
          "still unresolved: %d" % (found, made, failed, len(distinct) - len(resolved)))
    if made:
        print("NOTE: the %d created here carry only their match key and a name where one was "
              "available. They have none of the attributes a companies table would have given "
              "them — say so, and hand back the list so they can be loaded properly later." % made)
    return 0


def create_company(state, mapping, key_type, value, name, budget, dry=False):
    """Create one company, through the same companies loader every other company goes through."""
    if dry:
        return None
    wf = state["entities"]["companies"]["workflow_id"]
    payload = {"row_key": value, "match_key": key_type, key_type: value}
    # ALWAYS give it a name, falling back to the key itself. Two reasons, and the second is a bug
    # this fixes: the Step 4 script promises the installer "a domain and a name", and the Step 8
    # association check traverses `company.org_name`, so a nameless company makes every contact
    # attached to it read as unlinked.
    for col, spec in (mapping.get("fields", {}).get("companies", {}) or {}).items():
        fid = spec.get("field_id", col) if isinstance(spec, dict) else col
        if fid == "org_name":
            payload[fid] = name or value
        elif fid in ("domain", "linkedin_url") and fid == key_type:
            payload[fid] = value
    payload.setdefault("org_name", name or value)
    try:
        status, result = settle(wf, fire(wf, payload), budget)
    except (RuntimeError, subprocess.TimeoutExpired):
        return None
    return result.get("entityId") if status == "completed" else None


# --------------------------------------------------------------------------- the pass

def run(a):
    mapping = json.load(open(a.map, encoding="utf-8"))
    state = json.load(open(a.state, encoding="utf-8"))
    if a.entity not in state.get("entities", {}):
        raise SystemExit("%s was not built. Run build_loader.py build first." % a.entity)

    rows = L.keyed_rows(L.read_table(a.csv), mapping, a.entity)
    todo = L.remaining(rows, a.ledger)
    if a.of > 1:
        todo = todo[a.shard - 1::a.of]
    if a.limit:
        todo = todo[:a.limit]

    company_ids, company_verdicts = {}, {}
    if a.entity == "contacts":
        company_ids = L.company_id_map(a.company_ledger)
        company_verdicts = L.fold_ledger(a.company_ledger)
        print("company ids folded from the ledger: %d of %d settled company rows"
              % (len(company_ids), len(company_verdicts)))

        # THE ONE FAILURE THAT IS COMPLETELY SILENT. A wrong or missing `company_ref_column`
        # unlinks every contact, every row still loads, and the run reports success end to end —
        # so it is caught HERE, before anything is fired, rather than discovered afterwards by
        # someone noticing that no contact has a company. Loading the whole file unlinked is not
        # a recoverable mistake worth making quietly.
        ref_col = mapping.get("company_ref_column")
        resolvable = sum(1 for i in todo
                         if L.contact_join_key(i["row"], mapping) in company_ids)
        print("contacts in this pass that resolve to a company: %d of %d, via %r"
              % (resolvable, len(todo), ref_col))
        if todo and not resolvable and not a.allow_all_unlinked:
            raise SystemExit(
                "\nSTOPPING: not one contact in this pass resolves to a company, so every row "
                "would load with no company attached.\n"
                "  the company reference column is %r\n"
                "  the company ledger holds %d ids, keyed like: %s\n"
                "  contacts carry values like: %s\n"
                "Those two have to be the SAME key. Fix `company_ref_column` in the mapping, or "
                "the row key on the companies side, then run this again. If the contacts really "
                "have no companies, pass --allow-all-unlinked and say so in the output."
                % (ref_col, len(company_ids),
                   ", ".join(list(company_ids)[:3]) or "(none)",
                   ", ".join(str(i["row"].get(ref_col)) for i in todo[:3]) if ref_col
                   else "(no column configured)"))
    print("shard %d/%d — %d rows to do" % (a.shard, a.of, len(todo)))

    write_resume(a, mapping)
    for n, item in enumerate(todo, 1):
        line = load_row(item, mapping, a.entity, state, a.ledger, company_ids,
                        company_verdicts, a.hold_unlinked, a.budget)
        L.append_settled(a.ledger, line)      # the moment it settles, never a batch
        rec = json.loads(line)
        print("%5d/%d  %-28s %-26s %s"
              % (n, len(todo), (item["row_key"] or "?")[:28], rec["status"],
                 rec.get("entity_id") or rec.get("reason", "")[:40]))
        time.sleep(a.pace)

    tally = L.counts_by_status(a.ledger)
    print("\nledger now: %s" % tally)
    if a.entity == "contacts":
        why = {}
        for rec in L.fold_ledger(a.ledger).values():
            if rec.get("status") == "completed" and not rec.get("associated"):
                why[rec.get("unlinked_reason") or "unknown"] = \
                    why.get(rec.get("unlinked_reason") or "unknown", 0) + 1
        how = {}
        for rec in L.fold_ledger(a.ledger).values():
            if rec.get("status") == "completed" and rec.get("associated"):
                k = rec.get("link_source") or "unknown"
                how[k] = how.get(k, 0) + 1
        print("company attached, by where it came from: %s" % (how or "none"))
        print("loaded with no company attached: %s" % (why or "none"))
    write_resume(a, mapping, tally)
    return 0


# --------------------------------------------------------------------------- verify

# The DSL root is not the CLI's `--entity-type` vocabulary: people are `people` in a query and
# `contacts` nowhere. Getting this wrong fails the query rather than returning a wrong number,
# which is the better of the two outcomes and still worth not doing.
DSL_ROOT = {"companies": "companies", "contacts": "people"}

# How many populated records this will page through before giving up and saying so. A field is
# reported as NOT CHECKED rather than passed when the workspace holds more than this.
SCOPE_CAP = 50000


def populated_ids(entity, fid, cap=SCOPE_CAP):
    """The ids Clay considers to have this field populated. Returns None when there are too many.

    **It has to be the ids, not a count, and it has to come from a FILTER.** A count is
    workspace-wide, which is how the previous version of this step passed every field on a
    workspace that already held records: `count ... is_not_null` returned 17 while the load had
    written 5, and `got >= want` waved it through. The check was structurally incapable of
    detecting the failure the whole skill exists to catch, and it looked rigorous doing it.

    A filter rather than `records get`, because that is the entire point: a value the field's type
    could not parse is PRESENT on the record and invisible to filters. Reading the record back
    would show it and prove nothing.
    """
    q = "select from %s where %s is_not_null" % (DSL_ROOT[entity], fid)
    found, cursor = set(), None
    while True:
        args = ["audiences", "records", "search-ids", "--query", q, "--limit", "10000"]
        if cursor:
            args += ["--cursor", cursor]
        try:
            r = clay(*args)
        except (RuntimeError, subprocess.TimeoutExpired):
            return None
        found.update(r.get("data") or [])
        cursor = r.get("cursor")
        if not cursor or len(found) > cap:
            return None if len(found) > cap else found

# A boolean cannot be coverage-checked, and the reason is not a bug in this script. Measured:
# on a boolean field, `is_not_null` returns exactly what `= true` returns, and `= false` returns
# EVERYTHING ELSE — including every record the field was never set on. Counted on one workspace:
# 15 true + 21 false = 36 = every person in it, against 28 the loader had written to.
# So no query distinguishes "explicitly false" from "never set", and any expected-versus-actual
# comparison on a boolean is arithmetic on a number that does not mean what it says. Report it
# as unmeasurable rather than raising a discrepancy that is really a property of the store.
UNCHECKABLE_TYPES = ("boolean",)


def expected_populated(rows, ledger_path, col, ftype):
    """How many DISTINCT Clay records should carry this field.

    Not "how many CSV rows had a value" — that number is wrong twice over, and both corrections
    matter. Rows that never loaded do not count. And rows that share a Clay match key landed on
    ONE record, so counting them separately invents a shortfall that is really a collision doing
    exactly what the pre-load report said it would.
    """
    settled = L.fold_ledger(ledger_path)
    ids = set()
    for item in rows:
        rec = settled.get(item["row_key"])
        if not rec or rec.get("status") != "completed" or not rec.get("entity_id"):
            continue
        if col in (rec.get("dropped_fields") or []):
            continue
        v = item["row"].get(col)
        if not L.blank(v) and L.parses_as(v, ftype):
            ids.add(rec["entity_id"])
    return len(ids)


def verify(a):
    """Ask Clay what it holds, and hold that against what should have landed.

    The ledger says what was SENT, and a value the field's type could not parse was sent,
    accepted, and is invisible to every filter. So the load's own report cannot tell a finished
    load from a load that finished and lost two columns. Only this comparison can.
    """
    mapping = json.load(open(a.map, encoding="utf-8"))
    sources = {"companies": (a.csv, a.ledger), "contacts": (a.contacts_csv, a.contacts_ledger)}

    # A VERIFICATION THAT CHECKED NOTHING MUST NOT REPORT SUCCESS. Measured on a real run: called
    # with `--ledger` and no `--csv`, this skipped every entity, checked zero fields, and printed
    # "every field matches what should have landed" — which is the exact failure the whole step
    # exists to catch, committed by the step itself. Refuse before the loop rather than after.
    usable = [e for e, (path, led) in sources.items()
              if path and led and mapping.get("fields", {}).get(e)]
    if not usable:
        raise SystemExit(
            "NOTHING TO VERIFY, so nothing is being claimed.\n"
            "  companies needs --csv AND --ledger; contacts needs --contacts-csv AND "
            "--contacts-ledger.\n"
            "  got: --csv %r --ledger %r --contacts-csv %r --contacts-ledger %r\n"
            "Re-run with the file each ledger belongs to."
            % (a.csv, a.ledger, a.contacts_csv, a.contacts_ledger))
    for entity, (path, led) in sources.items():
        if led and not path:
            print("!! %s: a ledger was given but not its file, so %s IS NOT BEING CHECKED"
                  % (entity, entity))
        elif path and not led:
            print("!! %s: a file was given but not its ledger, so %s IS NOT BEING CHECKED"
                  % (entity, entity))

    # The records THIS LOAD wrote. Everything below is counted against these ids and nothing else.
    mine = {}
    for entity, (_p, led) in sources.items():
        mine[entity] = {r["entity_id"] for r in L.fold_ledger(led or "").values()
                        if r.get("status") == "completed" and r.get("entity_id")} if led else set()
    print("scoped to this load: %d companies, %d contacts"
          % (len(mine["companies"]), len(mine["contacts"])))

    print("%-26s %-9s %-8s %9s %9s  %s"
          % ("field", "entity", "type", "expected", "in your load", ""))
    ok, checked = True, 0
    for entity, (path, ledger) in sources.items():
        if not path or not ledger or not mapping.get("fields", {}).get(entity):
            continue
        rows = L.keyed_rows(L.read_table(path), mapping, entity)
        for col, spec in mapping["fields"][entity].items():
            fid = spec.get("field_id", col) if isinstance(spec, dict) else col
            ftype = spec["type"] if isinstance(spec, dict) else spec
            want = expected_populated(rows, ledger, col, ftype)
            if ftype in UNCHECKABLE_TYPES:
                # Scoped like everything else — a workspace-wide "23 true" beside an expected 7
                # reads as a number about this load and is not one.
                q = "select from %s where %s = true" % (DSL_ROOT[entity], fid)
                try:
                    hits = set(clay("audiences", "records", "search-ids", "--query", q,
                                    "--limit", "10000").get("data") or [])
                    shown = "%d true" % len(hits & mine[entity])
                except (RuntimeError, subprocess.TimeoutExpired):
                    shown = "-"
                print("%-26s %-9s %-8s %9d %9s  %s"
                      % (col[:26], entity, ftype, want, shown,
                         "not checkable — false and never-set are the same query"))
                continue
            hits = populated_ids(entity, fid)
            if hits is None:
                print("%-26s %-9s %-8s %9d %9s  %s"
                      % (col[:26], entity, ftype, want, "-",
                         "NOT CHECKED — too many records to scope this to your load"))
                continue
            got = len(hits & mine[entity])
            flag = "ok" if got >= want else "SHORT BY %d" % (want - got)
            ok = ok and got >= want
            checked += 1
            print("%-26s %-9s %-8s %9d %9d  %s" % (col[:26], entity, ftype, want, got, flag))

    if a.contacts_ledger:
        # Traversed through the association, so it is the link Clay holds rather than the one the
        # loader believes it sent. A matching domain establishes nothing.
        #
        # The field has to be one EVERY company carries. `company.domain is_not_null` was tried
        # and under-counted by exactly the companies matched on `linkedin_url`, which have no
        # domain: their contacts are linked and the query cannot see them. `org_name` is written
        # on every company this loader creates, so it tests the association and nothing else.
        hits = populated_ids("contacts", "company.org_name")
        got = len(hits & mine["contacts"]) if hits is not None else -1
        want = len({r["entity_id"] for r in L.fold_ledger(a.contacts_ledger).values()
                    if r.get("associated") and r.get("entity_id")})
        if got < 0:
            print("%-26s %-9s %-8s %9d %9s  %s"
                  % ("linked to a company", "contacts", "-", want, "-", "NOT CHECKED"))
            want = got = 0
        ok = ok and got >= want
        print("%-26s %-9s %-8s %9d %9d  %s"
              % ("linked to a company", "contacts", "-", want, got,
                 "ok" if got >= want else "SHORT BY %d" % (want - got)))

    if not checked:
        raise SystemExit("\nNo field was actually compared, so there is nothing to report. That is "
                         "a failure, not a pass — check the mapping has fields for the entities "
                         "whose ledgers you passed.")
    print("\n%d fields compared. %s" % (checked,
          "Every one matches what should have landed." if ok else
                    "AT LEAST ONE FIELD IS SHORT — those values wrote, reported success, and "
          "cannot be filtered on."))
    return 0 if ok else 1


# --------------------------------------------------------------------------- resume breadcrumb

RESUME = """# Resume this load

State on disk (this is the only state that matters):

- ledger:        {ledger}
- mapping:       {map}
- build state:   {state}
- source CSV:    {csv}

Ledger counts at {when}: {tally}

## Next command

```
{cmd}
```

## Do not repeat

- The audience fields already exist. `build_loader.py fields` is safe to re-run; it creates only
  what is missing.
- The workflows already exist and are **unpublished on purpose**. Re-running
  `build_loader.py build` would create a second set — it refuses while the build state file is
  present, and if that file is gone this is a new build rather than a continuation.
- Settled rows are never re-fired. `failed` and `timeout` are not settled and the next pass picks
  them up; do not change anything before retrying one.
"""


def write_resume(a, mapping, tally=None):
    cmd = ("python3 scripts/load_drive.py --entity %s --state %s --csv %s --map %s --ledger %s"
           % (a.entity, a.state, a.csv, a.map, a.ledger))
    if a.entity == "contacts":
        cmd += " --company-ledger %s" % a.company_ledger
    body = RESUME.format(ledger=a.ledger, map=a.map, state=a.state, csv=a.csv, when=now(),
                         tally=tally if tally is not None else L.counts_by_status(a.ledger),
                         cmd=cmd)
    path = os.path.join(os.path.dirname(a.ledger) or ".", "RESUME.md")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w", encoding="utf-8").write(body)


# --------------------------------------------------------------------------- cli

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("command", nargs="?", default="load",
                    choices=("load", "verify", "prepass"))
    ap.add_argument("--entity", choices=("companies", "contacts"))
    ap.add_argument("--state", required=True)
    ap.add_argument("--map", required=True)
    ap.add_argument("--csv")
    ap.add_argument("--contacts-csv")
    ap.add_argument("--ledger")
    ap.add_argument("--company-ledger")
    ap.add_argument("--contacts-ledger")
    ap.add_argument("--shard", type=int, default=1)
    ap.add_argument("--of", type=int, default=1)
    ap.add_argument("--pace", type=float, default=1.0)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--budget", type=int, default=120, help="seconds to wait for one run")
    ap.add_argument("--allow-all-unlinked", action="store_true",
                    help="proceed even when NO contact resolves to a company. Only for a TAM "
                         "that genuinely has no company links")
    ap.add_argument("--create", action="store_true",
                    help="prepass only: create the companies that are in neither the companies "
                         "table nor the audience. Opt-in — it writes company records nobody listed, "
                         "carrying only a match key and a name")
    ap.add_argument("--dry-run", action="store_true",
                    help="prepass only: resolve and report, create nothing")
    ap.add_argument("--hold-unlinked", action="store_true",
                    help="hold a contact whose company has not loaded instead of loading it "
                         "without a company link")
    a = ap.parse_args(argv)

    if a.command == "verify":
        return verify(a)
    if a.command == "prepass":
        for need in ("contacts_csv", "ledger"):
            if not getattr(a, need):
                ap.error("prepass needs --%s" % need.replace("_", "-"))
        return prepass(a)
    for need in ("entity", "csv", "ledger"):
        if not getattr(a, need):
            ap.error("load needs --%s" % need)
    if a.entity == "contacts" and not a.company_ledger:
        ap.error("contacts need --company-ledger: the company record ids come from it")
    return run(a)


if __name__ == "__main__":
    sys.exit(main())
