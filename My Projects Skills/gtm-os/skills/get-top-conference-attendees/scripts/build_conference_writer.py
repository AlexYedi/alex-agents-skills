#!/usr/bin/env python3
"""Build the writer workflow that puts conference attendees and their dossiers into Audiences.

    python3 build_conference_writer.py conference-config.json [--dry-run] [--publish]

What it builds, and why it is shaped this way:

    trigger (manual)
      -> 0a Intake .................. one fan-in point; turns "" into null
      -> 1  Company gate ............ does this attendee have a company DOMAIN?
           yes -> 2  Company record .......... upsert ACCOUNT on domain
                  -> 3  Linked router
                       -> 4a Attendee by LinkedIn (linked)
                       -> 4b Attendee by email    (linked)
                       -> 4z nothing to write
           no  -> 5  Unlinked router
                       -> 6a Attendee by LinkedIn
                       -> 6b Attendee by email
                       -> 6z nothing to write

Four attendee writers is not over-engineering; it is the smallest graph the platform allows:

  * Every selected lookup field is REQUIRED and rejects an empty string, so one writer
    cannot "use whichever key is present" — that is one writer per match key.
  * A BLANK association writes no record AT ALL, not an unlinked one, so "has a company" and
    "has no company" cannot be one writer with an optional field — that doubles it again.

There is no join node. A plain edge into a shared terminal hangs the run whenever a sibling
lane is pending, so every lane ends where it ends.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import audience_lib as A                                  # noqa: E402
from conference_lib import (Build, UPSERT_ACTION_KEY,     # noqa: E402
                            rules_router, save_writer_config, terminal_node)

# Trigger keys. Derived from the field plan so the payload a person sees in a run reads as
# English rather than as positions in an array.
KEY_ROUTE = "route"
KEY_HAS_ACCOUNT = "has_account"
KEY_ACCT_DOMAIN = "acct_domain"
KEY_ACCT_NAME = "acct_org_name"
KEY_MATCH_EMAIL = "key_email"
KEY_MATCH_LINKEDIN = "key_linkedin"

PEOPLE_BUILTIN_KEYS = {f: "c_" + f for f in A.PEOPLE_BUILTINS}
COMPANY_BUILTIN_KEYS = {"org_name": KEY_ACCT_NAME, "domain": KEY_ACCT_DOMAIN}
assert sorted(COMPANY_BUILTIN_KEYS) == sorted(A.COMPANY_BUILTINS)


def people_plan_keys():
    return {display: "pf_" + src for display, _t, src in A.PEOPLE_FIELDS}


def company_plan_keys():
    return {display: "af_" + src for display, _t, src in A.COMPANY_FIELDS}


def all_trigger_keys():
    keys = [KEY_ROUTE, KEY_HAS_ACCOUNT, KEY_ACCT_DOMAIN, KEY_ACCT_NAME,
            KEY_MATCH_EMAIL, KEY_MATCH_LINKEDIN]
    keys += sorted(PEOPLE_BUILTIN_KEYS.values())
    keys += sorted(set(people_plan_keys().values()))
    keys += sorted(set(company_plan_keys().values()))
    # People and company plans share DISPLAY NAMES ("Conference", "Dossier written at") but
    # not keys: the prefixes keep them distinct, so "Conference" becomes both
    # `pf_conference_name` and `af_conference_name` — two keys carrying the same value to two
    # different records. The set() here dedupes within a plan, never across them.
    return sorted(set(keys))


def intake_code(keys):
    """The one place a blank is turned into a null, before any write sees it.

    This is not tidiness. `removeNullValues` drops nulls but NOT empty strings: a field sent
    as "" is counted as updated and CLEARS whatever the audience already held. Measured, on
    a record that lost an email address it had. Every writer here sends a fixed field list,
    so without this step a re-run would strip an existing record down to whatever this one
    campaign happened to know."""
    return (
        'KEYS = %r\n\n'
        # The entry point MUST be named `handler`. The runtime looks for exactly that and
        # fails with "No \'handler\' function defined" — measured, on every row of the first
        # real load. Nothing in the node spec or the build reveals it; only a run does.
        'def handler(context):\n'
        '    """Normalise the trigger payload. Empty string -> None, so a blank never\n'
        '    overwrites a populated field."""\n'
        '    out = {}\n'
        '    for k in KEYS:\n'
        '        v = context.get_input(k)\n'
        '        if isinstance(v, str):\n'
        '            v = v.strip()\n'
        '        out[k] = v if v not in ("", None) else None\n'
        '    return out\n'
    ) % (sorted(keys),)


def record_fields_imc(field_ids, key_map, builtin_ids, builtin_keys):
    """`recordFields|<id>` -> a reference to the intake key carrying its value.

    An action parameter fed from an upstream node needs BOTH an inputSchema pin AND an
    inputMappingConfig reference. A pin alone is silently dropped; a pin nothing references
    is deleted on write."""
    imc = {}
    for fid in builtin_ids:
        imc["recordFields|" + fid] = {"type": "reference",
                                      "expression": "{{%s}}" % builtin_keys[fid]}
    for display, fid in field_ids.items():
        imc["recordFields|" + fid] = {"type": "reference",
                                      "expression": "{{%s}}" % key_map[display]}
    return imc


def record_pins(b, field_ids, key_map, builtin_ids, builtin_keys):
    pins = {}
    for fid in builtin_ids:
        k = builtin_keys[fid]
        pins[k] = b.pin("intake", "$." + k)
    for display, _fid in field_ids.items():
        k = key_map[display]
        pins[k] = b.pin("intake", "$." + k)
    return pins


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        raise SystemExit(__doc__.strip().splitlines()[2].strip())
    dry = "--dry-run" in flags
    b = Build(args[0])

    print("== platform ==")
    b.check_cli()
    b.check_workspace()
    b.check_audiences()
    link_companies = bool(b.cfg.get("link_companies", True))
    print("company records: %s" % ("on — attendees linked to their company"
                                   if link_companies else "off — attendees written unlinked"))

    # ---- workflow ----------------------------------------------------------
    b.guard_orphan()
    b.reconcile()
    st = b.state()
    if "workflow_id" not in st["meta"]:
        if dry:
            # Do NOT stop here. The columns are what a dry run exists to show — they are the
            # part that lands in the installer's workspace and the part they might object to
            # — and they can be planned without a workflow existing. Returning early made the
            # first dry run of a new build the one that showed the least.
            print("would create the shared writer %r" % b.writer_name)
        else:
            # `workflows create` takes --name as a FLAG and accepts no --input body and no
            # description. Hardcoding the wrong form is the trap this skill warns about, and
            # it failed here first: the error named the missing option, not the wrong shape.
            out = b.clay("workflows", "create", "--name", b.writer_name)
            b.set_meta(workflow_id=out.get("id") or out.get("resourceId"))
            print("+ workflow %s" % b.wf)
    else:
        print("= writer already built in this workspace: %s" % b.wf)
        print("  (one writer serves every conference — nothing new is created for this one)")

    # ---- fields ------------------------------------------------------------
    print("\n== audience fields ==")
    people_ids, company_ids = {}, {}
    for display, dtype, _src in A.PEOPLE_FIELDS:
        rec = b.ensure_field("people:" + display, display, dtype, "people", dry_run=dry)
        people_ids[display] = rec["id"]
    if link_companies:
        for display, dtype, _src in A.COMPANY_FIELDS:
            rec = b.ensure_field("companies:" + display, display, dtype, "companies", dry_run=dry)
            company_ids[display] = rec["id"]

    if dry:
        print("\n-- dry run: no nodes built. Fields above are what would be created or adopted.")
        return

    pkg = b.action_package(UPSERT_ACTION_KEY)
    keys = all_trigger_keys()
    pkeys, akeys = people_plan_keys(), company_plan_keys()

    # ---- trigger -----------------------------------------------------------
    print("\n== trigger ==")
    st = b.state()
    if "trigger_id" not in st["meta"]:
        # A MANUAL trigger: a routine refuses a workflow that has none, and the routine is
        # what the driver starts. The schema must be COMPLETE — fields absent from it are
        # stripped at intake, which surfaces later as "Workflow has no initial node".
        t = b.clay("workflows", "triggers", "create", b.wf, inp={
            "triggerType": "manual",
            "inputSchema": {"type": "object",
                            "properties": {k: {"type": "string"} for k in keys},
                            "required": [KEY_ROUTE]},
        })
        tid = t["resourceId"]
        got = b.clay("workflows", "triggers", "get", tid)
        b.set_meta(trigger_id=tid, trigger_node=got["workflowNodeId"])
        print("  + trigger %s" % tid)
    else:
        # **UPDATE the schema every build, never only on create.** A key absent from the
        # trigger's inputSchema is STRIPPED at intake, so a column added to the field plan
        # after the first build would be wired all the way through the graph and still arrive
        # null — the write succeeds, the column stays empty for ever, and nothing reports it.
        # Measured: adding one column and rebuilding left it empty on all five records,
        # because the trigger created on the first build still carried the old key list.
        tid = st["meta"]["trigger_id"]
        b.clay("workflows", "triggers", "update", tid, inp={
            "inputSchema": {"type": "object",
                            "properties": {k: {"type": "string"} for k in keys},
                            "required": [KEY_ROUTE]},
        })
        back = b.clay("workflows", "triggers", "get", tid)
        have = set(((back.get("inputSchema") or {}).get("properties") or {}))
        missing = [k for k in keys if k not in have]
        if missing:
            raise SystemExit(
                "The trigger schema is missing %d key(s) after an update: %s\n"
                "Anything absent here is stripped at intake and its column stays empty."
                % (len(missing), sorted(missing)))
        print("  = trigger %s (schema re-sent, %d keys verified)" % (tid, len(have)))

    # ---- intake ------------------------------------------------------------
    print("\n== nodes ==")
    code = intake_code(keys)
    b.ensure_node("intake", {"nodeType": "code", "name": "0a Intake",
                             "codeTimeoutMs": 30000, "code": code})
    # A trigger create mints the node but leaves it UNCONNECTED, and every run then dies
    # with "Workflow has no initial node". Wire intake from EVERY trigger node, not only
    # the one built here: binding a table adds its own, and an edge list that omits it
    # severs that binding on the next rebuild.
    tnode = b.state()["meta"]["trigger_node"]
    tnodes = [tnode]
    g = b.clay("workflows", "graph", "get", b.wf)
    for t in (g.get("summary") or {}).get("triggers") or []:
        nid = b.clay("workflows", "triggers", "get", t["id"]).get("workflowNodeId")
        if nid and nid not in tnodes:
            tnodes.append(nid)
    b.wire("intake", code=code, name="0a Intake",
           input_schema={"type": "object", "properties": {
               k: {"type": "string", "sourceNodeId": tnode, "sourcePath": "$." + k}
               for k in keys}},
           edges=[{"sourceNode": n} for n in tnodes])

    # ---- company gate ------------------------------------------------------
    gate = rules_router("1 Company gate", KEY_HAS_ACCOUNT, ["yes", "no"])
    b.ensure_node("gate_account", gate)
    b.wire("gate_account", **gate,
           input_schema={"type": "object", "properties": {
               KEY_HAS_ACCOUNT: b.pin("intake", "$." + KEY_HAS_ACCOUNT)}},
           edges=["intake"])

    # ---- company record ----------------------------------------------------
    acct_builtins = list(A.COMPANY_BUILTINS) if link_companies else []
    acct_selected = acct_builtins + sorted(company_ids.values())
    acct_imc = {
        "entityType": {"type": "static", "value": "ACCOUNT"},
        # ACCOUNT can only be matched on domain or a LinkedIn URL. A company with neither
        # cannot be upserted at all, which is exactly why its people go down the unlinked
        # lane rather than being dropped.
        "lookupFields|selectedLookupFields": {"type": "static",
                                             "value": [A.ACCOUNT_MATCH_KEY]},
        "lookupFields|" + A.ACCOUNT_MATCH_KEY: {"type": "reference",
                                                "expression": "{{%s}}" % KEY_ACCT_DOMAIN},
        "recordFields|selectedRecordFields": {"type": "static", "value": acct_selected},
        "recordFields|removeNullValues": {"type": "static", "value": True},
    }
    acct_imc.update(record_fields_imc(company_ids, akeys, acct_builtins, COMPANY_BUILTIN_KEYS))
    acct_tools = [{"toolType": "clay_action", "actionKey": UPSERT_ACTION_KEY,
                   "actionPackageId": pkg, "inputMappingConfig": acct_imc}]
    if link_companies:
        b.ensure_tool_node("acct_writer", {"nodeType": "tool", "name": "2 Company record",
                                           "tools": acct_tools})
        apins = record_pins(b, company_ids, akeys, acct_builtins, COMPANY_BUILTIN_KEYS)
        b.wire("acct_writer", tools=acct_tools, name="2 Company record",
               input_schema={"type": "object", "properties": apins},
               edges=[{"from": "gate_account", "rule": "rule_yes", "name": "has a domain"}])

    # ---- attendee writers --------------------------------------------------
    people_builtins = list(A.PEOPLE_BUILTINS)
    selected = people_builtins + sorted(people_ids.values())
    base_imc = {
        "entityType": {"type": "static", "value": "CONTACT"},
        "recordFields|selectedRecordFields": {"type": "static", "value": selected},
        # Nulls are dropped; empty strings are not, which is why intake nulls every blank.
        "recordFields|removeNullValues": {"type": "static", "value": True},
    }
    base_imc.update(record_fields_imc(people_ids, pkeys, people_builtins, PEOPLE_BUILTIN_KEYS))

    LANES = [
        ("linked", A.ROUTE_LINKED_LINKEDIN, A.ROUTE_LINKED_EMAIL, "3 Linked router",
         "acct_writer", "4a Attendee by LinkedIn (linked)", "4b Attendee by email (linked)",
         "4z Nothing to write"),
        ("unlinked", A.ROUTE_UNLINKED_LINKEDIN, A.ROUTE_UNLINKED_EMAIL, "5 Unlinked router",
         "gate_account", "6a Attendee by LinkedIn", "6b Attendee by email",
         "6z Nothing to write"),
    ]

    for tag, li_route, em_route, router_name, parent, li_name, em_name, term_name in LANES:
        if tag == "linked" and not link_companies:
            continue
        rkey = "router_" + tag
        router = rules_router(router_name, KEY_ROUTE, [li_route, em_route])
        b.ensure_node(rkey, router)
        parent_edge = ([parent] if tag == "linked"
                       else [{"from": "gate_account", "rule": "rule_no", "name": "no domain"}])
        b.wire(rkey, **router,
               input_schema={"type": "object",
                             "properties": {KEY_ROUTE: b.pin("intake", "$." + KEY_ROUTE)}},
               edges=parent_edge)

        for route, match_key, node_name in ((li_route, KEY_MATCH_LINKEDIN, li_name),
                                           (em_route, KEY_MATCH_EMAIL, em_name)):
            # The lane's match field comes from the same function the driver routes with, so
            # the graph and the payload can never disagree about which key identifies a person.
            match_field = A.route_match_key(route)
            imc = dict(base_imc)
            imc["lookupFields|selectedLookupFields"] = {"type": "static", "value": [match_field]}
            imc["lookupFields|" + match_field] = {"type": "reference",
                                                  "expression": "{{%s}}" % match_key}
            if tag == "linked":
                # The company's record id, straight off the writer above. A tool node's
                # output is read at $.result.…; an intake or trigger pin is read at $.… —
                # mixing the two resolves to null and reads as "no company".
                imc["associations|accountId"] = {"type": "reference",
                                                 "expression": "{{acct_record_id}}"}
            tools = [{"toolType": "clay_action", "actionKey": UPSERT_ACTION_KEY,
                      "actionPackageId": pkg, "inputMappingConfig": imc}]
            nkey = "w_" + route
            b.ensure_tool_node(nkey, {"nodeType": "tool", "name": node_name, "tools": tools})
            pins = record_pins(b, people_ids, pkeys, people_builtins, PEOPLE_BUILTIN_KEYS)
            pins[match_key] = b.pin("intake", "$." + match_key)
            if tag == "linked":
                pins["acct_record_id"] = b.pin("acct_writer", "$.result.entityId")
            b.wire(nkey, tools=tools, name=node_name,
                   input_schema={"type": "object", "properties": pins},
                   edges=[{"from": rkey, "rule": "rule_" + route, "name": route}])

        tkey = "term_" + tag
        term = terminal_node(term_name)
        b.ensure_node(tkey, term)
        b.wire(tkey, **term,
               input_schema={"type": "object",
                             "properties": {"prev": b.pin("intake", "$", "object")}},
               edges=[{"from": rkey, "default": True, "name": "no writable key"}])

    # ---- routine -----------------------------------------------------------
    print("\n== routine ==")
    st = b.state()
    if "routine_id" not in st["meta"]:
        # The id is documented as `<type>:<objectId>`, but READ IT BACK rather than
        # constructing it: a synthesised identifier that the platform happens to agree with
        # today is an assumption with no error when it stops being true. The construction is
        # kept only as the fallback for a routine that already exists, where the create
        # returns a conflict instead of a body.
        rid = None
        try:
            # --name is REQUIRED here (6-100 chars) despite reading as optional in the
            # help, and it is a flag rather than part of an --input body.
            rname = str(b.writer_name)[:100]
            if len(rname) < 6:
                rname = "Conference attendee writer"
            out = b.clay("routines", "create", "workflow", b.wf, "--name", rname)
            rid = out.get("id")
        except SystemExit as e:
            # `conflict` means this workflow already has a routine, which is the expected
            # state on every re-run. Match the error CODE, not English in the message.
            if '"conflict"' not in str(e) and "already exists" not in str(e).lower():
                raise
            print("  = routine already exists for this workflow")
        if not rid:
            rid = "workflow:" + b.wf
        b.set_meta(routine_id=rid)
        print("  + routine %s" % rid)
    else:
        print("  = routine %s" % st["meta"]["routine_id"])

    # ---- the interface the driver reads -------------------------------------
    b.set_meta(
        trigger_keys=keys,
        people_field_ids=people_ids,
        company_field_ids=company_ids,
        people_plan_keys=pkeys,
        company_plan_keys=akeys,
        people_builtin_keys=PEOPLE_BUILTIN_KEYS,
        company_builtin_keys=COMPANY_BUILTIN_KEYS,
        link_companies=link_companies,
    )

    # Leave behind everything a LATER session needs to top this up, so nothing depends on
    # the campaign folder still existing months from now.
    wc = save_writer_config(b.cfg)
    print("\nA top-up from any future session needs only this file:\n  %s" % wc)

    if "--publish" in flags:
        # A test run fires the DRAFT; a routine run fires the PUBLISHED version. An
        # unpublished graph therefore builds, validates, and writes nothing.
        b.publish()
    else:
        print("\nNOT PUBLISHED. A routine run fires the published version, so this graph "
              "will not write until you re-run with --publish.")

    print("\nBuilt. Workflow %s, routine %s" % (b.wf, b.state()["meta"]["routine_id"]))
    print("State: %s" % b.state_path)


if __name__ == "__main__":
    main()
