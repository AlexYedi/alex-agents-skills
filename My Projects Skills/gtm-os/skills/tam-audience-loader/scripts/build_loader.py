"""Create the audience fields, then build the two loader workflows.

    python3 build_loader.py fields --map <mapping.json>
    python3 build_loader.py build  --map <mapping.json> --out build-state.json

`fields` creates only what is missing and writes the id Clay actually returned back into the
mapping. `build` resolves the upsert action from the live catalogue, then creates one workflow per
entity: a webhook trigger, a rules router, one writer per Clay match key — doubled on the contacts
side for linked and unlinked — and a default route that rejects loudly.

Neither workflow is published. The driver fires the draft through the manual trigger, so publishing
would only activate triggers nobody asked for.

The node shape and the five things that fail silently are in `references/graph-shape.md`.
"""
import argparse
import json
import os
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import loader_lib as L                                               # noqa: E402

ENTITY_TYPE = {"companies": "ACCOUNT", "contacts": "CONTACT"}
SINGULAR = {"companies": "company", "contacts": "contact"}   # not entity[:-1]: that gives "companie"
DSL_ENTITY = {"companies": "companies", "contacts": "people"}  # the query root, not the CLI flag
CLI_ENTITY = {"companies": "companies", "contacts": "people"}
UPSERT_KEY = "upsert-audiences-record"


def clay(*args, timeout=120):
    r = subprocess.run(["clay"] + list(args), capture_output=True, text=True, timeout=timeout)
    out = (r.stdout or "").strip()
    # `"" in "{["` is True, so an empty stdout would reach json.loads and crash with a
    # decode error instead of the CLI's actual message. Test for a first character first.
    if out[:1] and out[:1] in "{[":
        return json.loads(out)
    raise RuntimeError("clay %s: %s" % (" ".join(args[:3]), (r.stderr or out)[:300]))


# --------------------------------------------------------------------------- fields

def existing_fields(entity):
    data = clay("audiences", "fields", "list", "--entity-type", CLI_ENTITY[entity])
    rows = data.get("data") or []
    return {r["name"]: r["id"] for r in rows}, rows


def ensure_fields(mapping, entity, dry_run=False):
    """Create what is missing; take the id Clay RETURNS, never the name that was asked for.

    `fields create` silently suffixes a name already in use — "Tier" becomes "Tier (2)" — so a
    build wired to the name it requested is wired to nothing.
    """
    by_name, rows = existing_fields(entity)
    made, reused, failed = [], [], []
    for col, spec in mapping.get("fields", {}).get(entity, {}).items():
        spec = spec if isinstance(spec, dict) else {"type": spec}
        name = spec.get("field_name") or col
        if spec.get("field_id"):
            # An id the mapping already carries still gets its type checked, because reusing a
            # field whose stored type disagrees is the silent-write failure through the back door.
            live = next((r for r in rows if r.get("id") == spec["field_id"]), None)
            if live and live.get("dataType") and live["dataType"] != spec["type"]:
                failed.append((col, "maps to %s, which stores %s, but this column is typed %s — "
                                    "every value would report success and match no filter"
                               % (spec["field_id"], live["dataType"], spec["type"])))
                continue
            reused.append((col, spec["field_id"]))
            continue
        if name in by_name:
            spec["field_id"] = by_name[name]
            reused.append((col, by_name[name]))
        elif dry_run:
            made.append((col, "<would create: %s / %s>" % (name, spec["type"])))
        else:
            try:
                created = clay("audiences", "fields", "create",
                               "--entity-type", CLI_ENTITY[entity],
                               "--name", name, "--data-type", spec["type"])
            except RuntimeError as exc:
                # A workspace has a per-data-type field budget and its size is not readable.
                # Report which columns got no field; never drop one quietly.
                failed.append((col, str(exc)[:160]))
                continue
            spec["field_id"] = created["id"]
            spec["field_name"] = created["name"]          # may differ from what was requested
            made.append((col, created["id"]))
        mapping["fields"][entity][col] = spec
    return {"created": made, "reused": reused, "failed": failed}


# --------------------------------------------------------------------------- the graph

def resolve_action():
    """Resolve the upsert from the live catalogue, and stop if it is absent.

    Never fall back to a remembered package id: a guessed id builds a graph against the wrong
    action in any workspace that does not match the one it was written in, and the graph
    validates perfectly either way.
    """
    for a in clay("workflows", "actions", "list").get("data") or []:
        if a.get("actionKey") == UPSERT_KEY and a.get("packageId"):
            return a["packageId"]
    raise SystemExit("%s is not in this workspace's action catalogue. Stopping rather than "
                     "guessing a package id." % UPSERT_KEY)


def trigger_schema(mapping, entity):
    props = {"row_key": {"type": "string"}, "match_key": {"type": "string"}}
    for key in L.MATCH_KEYS[entity]:
        props[key] = {"type": "string"}
    for col, spec in mapping.get("fields", {}).get(entity, {}).items():
        fid = spec.get("field_id", col) if isinstance(spec, dict) else col
        props[fid] = {"type": "string"}
    if entity == "contacts":
        props["company_record_id"] = {"type": "string"}
    return {"type": "object", "properties": props}


def writer_node(mapping, entity, key, linked, cond_id, package_id):
    """One writer. Its lookup key is fixed, and on an unlinked contact the association key is
    ABSENT — not blank. A blank `associations|accountId` writes no contact at all."""
    fields = mapping.get("fields", {}).get(entity, {})
    field_ids = [spec.get("field_id", c) if isinstance(spec, dict) else c
                 for c, spec in fields.items()]
    selected = sorted(set(field_ids) | {key})

    imc = {
        "entityType": {"type": "static", "value": ENTITY_TYPE[entity]},
        "lookupFields|selectedLookupFields": {"type": "static", "value": [key]},
        "lookupFields|%s" % key: {"type": "reference", "expression": "{{%s}}" % key},
        "recordFields|selectedRecordFields": {"type": "static", "value": selected},
        "recordFields|removeNullValues": {"type": "static", "value": True},
    }
    for fid in selected:
        imc["recordFields|%s" % fid] = {"type": "reference", "expression": "{{%s}}" % fid}
    if linked:
        imc["associations|accountId"] = {"type": "reference",
                                         "expression": "{{company_record_id}}"}

    rule_id = route_id(key, linked)
    return {
        "nodeType": "tool",
        "name": "Write %s by %s%s" % (SINGULAR[entity], key, " (linked)" if linked else ""),
        "incomingEdges": [{"sourceNode": cond_id, "ruleId": rule_id}],
        "tools": [{"toolType": "clay_action", "actionKey": UPSERT_KEY,
                   "actionPackageId": package_id, "inputMappingConfig": imc}],
    }


def route_id(key, linked):
    return "%s__%s" % (key, "linked" if linked else "plain")


def routes(entity):
    """Linked routes first: rules run top to bottom and the first match wins."""
    out = []
    for key in L.MATCH_KEYS[entity]:
        if entity == "contacts":
            out.append((key, True))
        out.append((key, False))
    return out


def router_node(entity, trigger_node_id):
    props = {"match_key": {"type": "string", "sourceNodeId": trigger_node_id,
                           "sourcePath": "$.match_key"}}
    if entity == "contacts":
        props["company_record_id"] = {"type": "string", "sourceNodeId": trigger_node_id,
                                      "sourcePath": "$.company_record_id"}
    rules = []
    for key, linked in routes(entity):
        items = [{"type": "BinOp", "dataPath": ["match_key"], "operator": "Equal", "value": key}]
        if entity == "contacts":
            items.append({"type": "BinOp", "dataPath": ["company_record_id"],
                          "operator": "NotEmpty" if linked else "Empty"})
        rules.append({"id": route_id(key, linked),
                      "name": "%s%s" % (key, " + company" if linked else ""),
                      "condition": {"type": "GroupOp", "combinationMode": "And", "items": items}})
    return {"nodeType": "conditional", "name": "Route by match key",
            "incomingEdges": [{"sourceNode": trigger_node_id}],
            "inputSchema": {"type": "object", "properties": props},
            "conditionalMode": "rules", "rulesConditionalConfig": {"rules": rules}}


def reject_node(cond_id):
    """The default route. A conditional without one saves, validates, and fails the first run
    that matches nothing — so it exists even though the driver screens these rows locally."""
    return {"nodeType": "code", "name": "Reject - no match key",
            "incomingEdges": [{"sourceNode": cond_id, "isDefaultRoute": True}],
            "code": ("def handler(context):\n"
                     "    raise Exception('row carries no Clay match key; it should have been "
                     "screened before firing')\n")}


def node_ids(workflow_id):
    g = clay("workflows", "graph", "get", workflow_id, "--mode", "summary")
    return {n["name"]: n["id"] for n in g.get("summary", {}).get("nodes") or []}


def build_entity(mapping, entity, package_id, name_prefix):
    wf = clay("workflows", "create", "--name", "%s — %s loader" % (name_prefix, entity))
    wf_id = wf["id"]

    trig = clay("workflows", "triggers", "create", wf_id,
                "--input", json.dumps({"triggerType": "webhook",
                                       "inputSchema": trigger_schema(mapping, entity)}))
    trig_node = clay("workflows", "triggers", "get", trig["resourceId"])["workflowNodeId"]

    clay("workflows", "nodes", "create", wf_id,
         "--input", json.dumps(router_node(entity, trig_node)))
    cond_id = node_ids(wf_id)["Route by match key"]

    for key, linked in routes(entity):
        clay("workflows", "nodes", "create", wf_id,
             "--input", json.dumps(writer_node(mapping, entity, key, linked, cond_id, package_id)))
    clay("workflows", "nodes", "create", wf_id, "--input", json.dumps(reject_node(cond_id)))

    ids = node_ids(wf_id)
    validation = clay("workflows", "graph", "validate", wf_id)
    if not validation.get("valid"):
        raise SystemExit("graph did not validate for %s: %s" % (entity, validation.get("errors")))

    return {"workflow_id": wf_id, "url": wf.get("url"), "trigger_node": trig_node,
            "nodes": ids, "entity_type": ENTITY_TYPE[entity],
            "routes": [route_id(k, l) for k, l in routes(entity)], "published": False}


def field_usage(entity, fid, sample_ids=3):
    """How many records already carry this field, and one value it holds.

    A field that exists and a field that is IN USE are different facts, and only the second tells
    you whether reusing it would sit beside real data or overwrite it.
    """
    try:
        q = "count from %s where %s is_not_null" % (DSL_ENTITY[entity], fid)
        n = clay("audiences", "records", "search-count", "--query", q).get("count")
    except (RuntimeError, subprocess.TimeoutExpired):
        return None, ""
    if not n:
        return 0, ""
    try:
        q = "select from %s where %s is_not_null" % (DSL_ENTITY[entity], fid)
        ids = (clay("audiences", "records", "search-ids", "--query", q,
                    "--limit", str(sample_ids)).get("data") or [])[:1]
        if not ids:
            return n, ""
        recs = clay("audiences", "records", "get", "--entity-type", CLI_ENTITY[entity],
                    "--ids", str(ids[0])).get("data") or []
        val = ((recs[0] if recs else {}).get("fields") or {}).get(fid)
        return n, "" if val is None else str(val)
    except (RuntimeError, subprocess.TimeoutExpired):
        return n, ""


def match_command(a):
    """Lay the two lists side by side. The MATCHING is the agent's, not this script's.

    Everything here is fact: the columns with what they read as and two real values, and the
    fields this workspace already holds with their ids and stored types. The only matches it
    asserts are same-label ones, which need no judgment.

    It deliberately does not guess the rest. An earlier version carried a table of known
    spellings, which is judgment encoded as a lookup: it could not see `staff_count`,
    `# of employees` or a header in another language, and a miss printed "no field yet" -- which
    reads as an answer rather than as nobody having looked. The agent running the skill can read a
    column name, two sample values and a field list and do better, and can say why, which is what
    makes the proposal correctable.
    """
    shown = False
    for entity, spec in (("companies", a.companies), ("contacts", a.contacts)):
        if not spec:
            continue
        shown = True
        rows = L.read_table(spec)
        _by_name, existing = existing_fields(entity)

        # SHOW WHAT EACH FIELD ALREADY HOLDS, not just that it exists. Measured on a cold run:
        # the agent passed over `TAM Test Icp Tier` and `TAM Test Fit Score` because the names read
        # like test artifacts, created two new fields instead, and only afterwards found those
        # fields populated with real values on live records. The reasoning was sound on the
        # evidence available; the evidence was missing. Asking someone to make the one decision
        # the skill warns is expensive while withholding the data that settles it is not a fair
        # ask, so the populated count and a sample value ship with the catalogue.
        print("\n=== %s: fields this workspace already has ===" % entity)
        print("  %-26s %-9s %-9s %-22s %s"
              % ("field id", "stores", "populated", "a value it holds", "name"))
        for f in sorted(existing, key=lambda x: x.get("id") or ""):
            fid = f.get("id")
            n, sample = field_usage(entity, fid)
            print("  %-26s %-9s %-9s %-22s %s"
                  % (fid, f.get("dataType"),
                     "-" if n is None else n, (sample or "")[:22], f.get("name")))

        print("\n=== %s: columns in the file ===" % entity)
        print("  %-26s %-9s %-34s %s" % ("column", "reads as", "two values", "same-label match"))
        for col in (rows[0].keys() if rows else []):
            vals = [r.get(col) for r in rows]
            t = L.infer_type(vals)
            sample = " | ".join(str(v).strip() for v in vals if not L.blank(v))[:34]
            hit = L.certain_field_match(col, existing)
            if hit and L.type_conflict(hit["stored_type"], t):
                note = "%s -- TYPE CONFLICT, stores %s" % (hit["field_id"], hit["stored_type"])
            elif hit:
                note = hit["field_id"]
            else:
                note = ""
            print("  %-26s %-9s %-34s %s" % (col[:26], t, sample, note))

    if not shown:
        raise SystemExit("match needs --companies and/or --contacts")
    print("""
Now do the matching yourself, against the two lists above. For each column decide one of:
  - it belongs in a field that already exists  -> put that `field_id` in the mapping
  - it is genuinely new                        -> give it a `field_name` and a type
  - it does not belong in Clay                 -> leave it out

Say WHY for every match that is not a same-label one, and show the whole thing for correction
before anything is created. Where a column would reuse a field that stores a different type, that
is not a match -- retype the column or give it its own field. The build refuses that reuse anyway.""")
    return 0


def adopt_command(a):
    """Rebuild `build-state.json` from loaders already in the workspace.

    Without this the only way to reuse a loader was the state file the build wrote, so losing it —
    a different machine, a cleaned folder, next quarter — stranded working workflows: the guard
    refused to build, and the refusal advised reusing them via the very file that was missing.
    Step 9 tells people to KEEP these for next time, which that made untrue.

    It does not just record ids. An adopted graph is only usable if it still has the shape this
    version builds, so every expected node is checked and a mismatch refuses rather than loading
    thousands of rows through a graph that is missing a writer.
    """
    found = {}
    for w in clay("workflows", "list").get("data") or []:
        name = w.get("name") or ""
        if not name.startswith(a.name_prefix):
            continue
        for entity in ("companies", "contacts"):
            if entity in name.lower():
                found[entity] = w
    if not found:
        raise SystemExit("No workflow in this workspace has a name starting with %r. Nothing to "
                         "adopt — run `build` instead." % a.name_prefix)

    state = {"package_id": resolve_action(), "map": os.path.abspath(a.map) if a.map else None,
             "entities": {}, "adopted": True}
    problems = []
    for entity, w in sorted(found.items()):
        g = clay("workflows", "graph", "get", w["id"], "--mode", "summary").get("summary", {})
        nodes = {n["name"]: n["id"] for n in g.get("nodes") or []}
        trig = next((n["id"] for n in g.get("nodes") or [] if n.get("nodeType") == "trigger"), None)

        # Check the SHAPE, not the node names. Names are not load-bearing — the driver settles on
        # `isTerminal`, never on a name — and Clay lets anyone rename a node on the canvas, so
        # matching them refuses a perfectly good graph over a typo. Counting by node type is what
        # actually decides whether a row has somewhere to go: one entry, one router, one writer
        # per route, and a default that rejects.
        kinds = {}
        for n in g.get("nodes") or []:
            kinds[n.get("nodeType")] = kinds.get(n.get("nodeType"), 0) + 1
        need = {"trigger": 1, "conditional": 1, "tool": len(routes(entity)), "code": 1}
        short = {k: (need[k], kinds.get(k, 0)) for k in need if kinds.get(k, 0) < need[k]}
        if short or not trig:
            problems.append("  %s (%s): %s"
                            % (w.get("name"), entity,
                               "no trigger node" if not trig else
                               ", ".join("expected %d %s node(s), found %d" % (w_, k, g_)
                                         for k, (w_, g_) in sorted(short.items()))))
            continue
        state["entities"][entity] = {
            "workflow_id": w["id"], "url": w.get("url"), "trigger_node": trig,
            "nodes": nodes, "entity_type": ENTITY_TYPE[entity],
            "routes": [route_id(k, l) for k, l in routes(entity)], "published": None}
        print("adopted %-9s %s" % (entity, w.get("name")))
        print("          writers: %s"
              % ", ".join(sorted(n for n in nodes if n.lower().startswith("write"))))

    if problems:
        raise SystemExit(
            "These do not have the shape this version builds, so adopting them would load rows "
            "through a graph that is missing a writer:\n%s\n"
            "Delete them and run `build`, or use a different --name-prefix."
            % "\n".join(problems))
    if os.path.exists(a.out):
        raise SystemExit("%s already exists — adopting would overwrite it. Move it aside first."
                         % a.out)
    json.dump(state, open(a.out, "w", encoding="utf-8"), indent=2, sort_keys=True)
    print("wrote %s — the fields these expect must already exist; run `fields` to confirm" % a.out)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("command", choices=("fields", "build", "match", "adopt"))
    ap.add_argument("--map")
    ap.add_argument("--companies", metavar="FILE[#TAB]")
    ap.add_argument("--contacts", metavar="FILE[#TAB]")
    ap.add_argument("--out", default="build-state.json")
    ap.add_argument("--name-prefix", default="TAM load")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)

    if a.command == "match":
        return match_command(a)
    if a.command == "adopt":
        return adopt_command(a)
    if not a.map:
        ap.error("%s needs --map" % a.command)
    mapping = json.load(open(a.map, encoding="utf-8"))
    entities = [e for e in ("companies", "contacts") if mapping.get("fields", {}).get(e)]

    if a.command == "fields":
        for entity in entities:
            rep = ensure_fields(mapping, entity, a.dry_run)
            # "created" on a dry run would be a claim about the workspace that is not true of it.
            print("%s: %d %s, %d already there, %d refused"
                  % (entity, len(rep["created"]),
                     "would be created" if a.dry_run else "created",
                     len(rep["reused"]), len(rep["failed"])))
            if a.dry_run:
                for col, what in rep["created"]:
                    print("  %-24s %s" % (col, what))
            for col, err in rep["failed"]:
                print("  NO FIELD  %-24s %s" % (col, err))
            if rep["failed"]:
                print("  ^ these columns have no field and will not load. Cut them from the "
                      "mapping or free budget, then run `fields` again.")
        if not a.dry_run:
            json.dump(mapping, open(a.map, "w", encoding="utf-8"), indent=2, sort_keys=True)
            print("mapping updated with the field ids Clay returned")
        return 0

    if os.path.exists(a.out):
        raise SystemExit("%s already exists. That build's fields and workflows are already in the "
                         "workspace; re-running would create a second set. Delete it deliberately "
                         "if you mean to rebuild." % a.out)

    # AND CHECK THE WORKSPACE, not just this directory. Keying the guard on a local filename
    # protects nothing against the normal way a second attempt happens — someone runs it again
    # from a fresh folder, or with a different --out, and gets a duplicate pair of loaders with
    # no warning. The workspace is the thing that actually holds them.
    existing = [w for w in (clay("workflows", "list").get("data") or [])
                if (w.get("name") or "").startswith(a.name_prefix)]
    if existing:
        raise SystemExit(
            "This workspace already has %d workflow(s) whose name starts with %r:\n%s\n"
            "Building again makes a second set that does the same thing.\n"
            "  To use them:      build_loader.py adopt --name-prefix %r --out %s\n"
            "  A separate loader: pass a different --name-prefix\n"
            "  Start over:        delete them in Clay first"
            % (len(existing), a.name_prefix,
               "\n".join("  %s" % w.get("name") for w in existing),
               a.name_prefix, a.out))

    package_id = resolve_action()
    state = {"package_id": package_id, "map": os.path.abspath(a.map), "entities": {}}
    for entity in entities:
        state["entities"][entity] = build_entity(mapping, entity, package_id, a.name_prefix)
        print("%s: %s (draft, unpublished)" % (entity, state["entities"][entity]["url"]))
    json.dump(state, open(a.out, "w", encoding="utf-8"), indent=2, sort_keys=True)
    print("wrote %s — a second run reads this instead of rebuilding" % a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
