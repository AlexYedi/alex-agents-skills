"""Build helpers for the conference-attendee writer workflow.

Credential rule, and it is absolute: this module never reads, holds or writes an API key of
any kind. The conference service's key is handled only by the driver, only from the
environment, and is never passed on a command line — a key in an argument is visible in
`ps` to every process on the machine. Everything this module drives is a Clay-native action
authenticated by the installer's own Clay session.

Resumability contract: every created node id and every field id is written to
`build-state.json` the moment the create succeeds, so an interrupted build re-runs as a
no-op over what already exists and creates only the gap. Nothing that would be lost is held
in memory.
"""

import json
import os
import time
import subprocess

# Resolved from the LIVE action catalogue at build time and deliberately not pinned here:
# a package id written into source is an environment assumption nobody can see.
UPSERT_ACTION_KEY = "upsert-audiences-record"

MIN_CLI = (0, 17, 0)

# **The writer is generic, and its name says so.** Nothing in the graph is specific to a
# conference or a company: the event, the goals, the company domain and the campaign id all
# arrive as per-record trigger inputs. So one writer serves every conference this workspace
# will ever run, and naming it after the first one produces a workspace full of near-identical
# graphs — measured, two runs made two workflows.
#
# The name is a constant rather than a config field on purpose. A field invites personalising,
# personalising defeats `guard_orphan` (which matches by name), and by the time anybody
# notices there are five of them.
WRITER_NAME = "Conference attendees to Audiences (shared writer)"

# Where the writer's identity lives. Keyed on the WORKSPACE, never on the campaign, because
# the campaign config is per-run and the writer is not. A per-run state file means a per-run
# workflow, which is the bug this exists to prevent.
DEFAULT_WRITER_HOME = "~/.clay-conference-writer"


def writer_dir(cfg):
    """The durable, workspace-keyed directory holding `build-state.json`."""
    base = cfg.get("writer_dir") or os.path.join(DEFAULT_WRITER_HOME,
                                                 str(cfg.get("workspace_id", "unknown")))
    return os.path.expanduser(base)


def run_dir(cfg, date=None):
    """Where a run's own files belong: config, campaign result, breadcrumbs.

    `~/.clay-conference-writer/<workspace>/runs/<date>/`. Durable, next to the writer state
    and the ledgers, and — the part that matters — **outside every git repository**. Three
    separate cold runs each invented a folder inside whatever repo the session started in, and
    that output carries real email addresses, the path the key was written to, and live share
    tokens. One `git add -A` publishes all of it.
    """
    date = date or time.strftime("%Y-%m-%d")
    return os.path.join(writer_dir(cfg), "runs", date)


def writer_state_path(cfg):
    return os.path.join(writer_dir(cfg), "build-state.json")


def writer_config_path(cfg):
    """The workspace-level config a LATER session can run a top-up from.

    A top-up needs none of the campaign's own inputs — no domain, no goals, no conference. It
    needs the workspace, whether companies are linked, and where the key is. Those are writer
    facts, so they are written beside the writer and a cold session weeks later can find them
    from `clay whoami` alone, with nothing kept from the original run."""
    return os.path.join(writer_dir(cfg), "writer-config.json")


WRITER_CONFIG_KEYS = ("workspace_id", "link_companies", "key_file", "clay_config_home",
                      "writer_dir")


def save_writer_config(cfg):
    """Record just the writer-level keys, so a later session needs nothing else."""
    out = {k: cfg[k] for k in WRITER_CONFIG_KEYS if k in cfg and cfg[k] is not None}
    out["_what"] = ("Workspace-level config for the conference-attendee writer. A top-up "
                    "needs only this file — point drive_load.py at it and ask for the "
                    "campaign by name.")
    path = writer_config_path(cfg)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    os.replace(tmp, path)
    return path


class Build:
    def __init__(self, config_path):
        self.cfg = json.load(open(config_path))
        self.dir = os.path.dirname(os.path.abspath(config_path))
        # NOT beside the config: the config is per-campaign, the writer is per-workspace.
        self.state_path = writer_state_path(self.cfg)
        os.makedirs(os.path.dirname(self.state_path), exist_ok=True)
        self.writer_name = self.cfg.get("writer_name") or WRITER_NAME
        self.env = dict(os.environ)
        if self.cfg.get("clay_config_home"):
            self.env["XDG_CONFIG_HOME"] = self.cfg["clay_config_home"]
        self._action_pkg = {}
        self._field_cache = {}

    # ------------------------------------------------------------------ the CLI

    def clay(self, *args, inp=None):
        cmd = ["clay", *args]
        if inp is not None:
            cmd += ["--input", json.dumps(inp) if not isinstance(inp, str) else inp]
        r = subprocess.run(cmd, capture_output=True, text=True, env=self.env)
        if r.returncode != 0:
            raise SystemExit("clay %s failed (%s):\n%s"
                             % (" ".join(args), r.returncode, r.stderr or r.stdout))
        try:
            return json.loads(r.stdout or "{}")
        except json.JSONDecodeError:
            return {"raw": r.stdout}

    def paged(self, *args, limit=100):
        """Walk every page of a list command.

        A single page is the wrong default for anything a name resolves against: list
        commands return a page, not everything, and an unpaginated lookup fails to find a
        thing that is right there while reporting the wrong cause."""
        rows, cursor, seen = [], None, 0
        while True:
            call = list(args) + ["--limit", str(limit)]
            if cursor:
                call += ["--cursor", cursor]
            d = self.clay(*call)
            rows.extend(d.get("data") or [])
            cursor = d.get("cursor")
            seen += 1
            if not cursor or seen > 50:
                return rows

    def check_cli(self):
        """Report the platform and stop. Never install, upgrade or fetch anything to repair
        it — a script that starts rebuilding its own prerequisites reads as a hang."""
        r = subprocess.run(["clay", "--version"], capture_output=True, text=True, env=self.env)
        if r.returncode != 0:
            raise SystemExit(
                "The `clay` CLI is not on PATH.\n"
                "Install the Clay plugin and run its setup skill, then re-run this build.")
        raw = (r.stdout or "").strip()
        try:
            got = tuple(int(x) for x in raw.split("+")[0].split(".")[:3])
        except ValueError:
            print("clay %s (could not parse a version; continuing)" % raw)
            return
        if got < MIN_CLI:
            raise SystemExit("clay %s is below the minimum this build needs (%s). Run "
                             "`clay update`." % (raw, ".".join(str(x) for x in MIN_CLI)))
        print("clay %s" % raw)

    def check_workspace(self):
        who = self.clay("whoami")
        got = str((who.get("workspace") or {}).get("id"))
        want = str(self.cfg["workspace_id"])
        if got != want:
            raise SystemExit(
                "WORKSPACE MISMATCH: the clay login resolves to workspace %s, the config "
                "expects %s.\nRefusing to build. Sign in to the right workspace and re-run."
                % (got, want))
        print("workspace %s verified" % got)

    def check_audiences(self):
        """Audiences must be enabled, or there is nothing to write into.

        A command, not a question: it either answers or it does not."""
        try:
            self.clay("audiences", "fields", "list", "--entity-type", "people")
        except SystemExit as e:
            raise SystemExit(
                "Audiences does not appear to be enabled on this workspace.\n"
                "`clay audiences fields list --entity-type people` failed:\n%s" % e)
        print("audiences reachable")

    # ---------------------------------------------------------------- build state

    def state(self):
        if os.path.exists(self.state_path):
            return json.load(open(self.state_path))
        return {"nodes": {}, "fields": {}, "tooltypes": {}, "meta": {}}

    def save(self, st):
        tmp = self.state_path + ".tmp"
        json.dump(st, open(tmp, "w"), indent=1, sort_keys=True)
        os.replace(tmp, self.state_path)

    def set_meta(self, **kv):
        st = self.state()
        st.setdefault("meta", {}).update(kv)
        self.save(st)

    @property
    def wf(self):
        return self.state()["meta"]["workflow_id"]

    def guard_orphan(self):
        """If state has no workflow but one already carries this config's name, STOP.

        `build-state.json` is the only record of which node is which. Without it the build
        cannot tell an existing graph apart, so creating a second workflow would silently
        orphan the first — still live, still writing to the same audience."""
        if "workflow_id" in self.state()["meta"]:
            return
        name = str(self.writer_name).strip().lower()
        for w in self.paged("workflows", "list", limit=200):
            if str(w.get("name", "")).strip().lower() == name:
                raise SystemExit(
                    "A workflow named %r already exists (%s) but build-state.json is "
                    "missing,\nso this build cannot tell which node is which.\n"
                    "Restore build-state.json beside this config, or rename that workflow "
                    "in Clay and re-run. Refusing to create a second one."
                    % (self.writer_name, w.get("id")))

    def reconcile(self):
        """Drop state entries whose node no longer exists. A node deleted in the app leaves
        a stale id; without this the next run updates an id that resolves to nothing."""
        st = self.state()
        if "workflow_id" not in st["meta"] or not st["nodes"]:
            return
        g = self.clay("workflows", "graph", "get", self.wf)
        live = {n["id"] for n in (g.get("summary") or {}).get("nodes") or []}
        gone = [k for k, nid in st["nodes"].items() if nid not in live]
        for k in gone:
            st["nodes"].pop(k, None)
            st.get("tooltypes", {}).pop(k, None)
            print("  ! %-28s missing in Clay; will be recreated" % k)
        if gone:
            self.save(st)

    # -------------------------------------------------------------------- fields

    def audience_fields(self, entity_type):
        if entity_type not in self._field_cache:
            self._field_cache[entity_type] = self.clay(
                "audiences", "fields", "list", "--entity-type", entity_type).get("data") or []
        return self._field_cache[entity_type]

    def ensure_field(self, key, name, data_type, entity_type, dry_run=False):
        """Create the column, or ADOPT the one already carrying that display name.

        Adoption is not a nicety. `audiences fields create` does not fail on a name already
        in use — it suffixes it — so a build that always creates leaves a workspace holding
        "Attendee tier", "Attendee tier (2)", "Attendee tier (3)", each stamped by a
        different run and none of them complete."""
        st = self.state()
        have = (st.get("fields") or {}).get(key)
        if have:
            print("  = %-28s %s  %r (already built)" % (key, have["id"], have["name"]))
            return have
        for f in self.audience_fields(entity_type):
            if str(f.get("name", "")).strip().lower() == str(name).strip().lower():
                rec = {"id": f["id"], "name": f["name"], "dataType": f.get("dataType"),
                       "entityType": entity_type, "adopted": True,
                       "wantedType": data_type}
                if f.get("dataType") != data_type:
                    # Writing a value the adopted field's type cannot parse is the silent
                    # failure this whole skill is built around: accepted, echoed back, and
                    # invisible to every filter. Report it; the driver drops such values.
                    print("  ! %-28s exists as %r (%s), wanted %s — values that do not fit "
                          "%s will be DROPPED rather than written invisibly"
                          % (key, f["name"], f.get("dataType"), data_type, f.get("dataType")))
                st = self.state()
                st.setdefault("fields", {})[key] = rec
                self.save(st)
                print("  = %-28s %s  %r (adopted)" % (key, rec["id"], rec["name"]))
                return rec
        if dry_run:
            print("  + %-28s would be created: %r (%s)" % (key, name, data_type))
            return {"id": "<not created — dry run>", "name": name, "dataType": data_type,
                    "entityType": entity_type, "adopted": False, "wantedType": data_type}
        out = self.clay("audiences", "fields", "create", "--entity-type", entity_type,
                        "--name", name, "--data-type", data_type)
        rec = {"id": out["id"], "name": out["name"], "dataType": out.get("dataType"),
               "entityType": entity_type, "adopted": False, "wantedType": data_type}
        if out.get("name") != name:
            print("  ! asked for %r, the workspace named it %r — recording the name it "
                  "returned" % (name, out.get("name")))
        st = self.state()
        st.setdefault("fields", {})[key] = rec
        self.save(st)
        print("  + %-28s %s  %r" % (key, rec["id"], rec["name"]))
        return rec

    # --------------------------------------------------------------------- nodes

    def action_package(self, action_key):
        if action_key in self._action_pkg:
            return self._action_pkg[action_key]
        for a in self.clay("workflows", "actions", "list").get("data") or []:
            if a.get("actionKey") == action_key:
                pkg = a.get("packageId") or a.get("actionPackageId")
                if pkg:
                    self._action_pkg[action_key] = pkg
                    return pkg
        raise SystemExit(
            "Could not resolve the %r action in this workspace's catalogue.\n"
            "Audiences may not be enabled here. Refusing to guess at a package id."
            % action_key)

    def ensure_node(self, key, spec):
        """Create the node if this key has no id yet; persist the id immediately."""
        st = self.state()
        if key in st["nodes"]:
            return st["nodes"][key]
        out = self.clay("workflows", "nodes", "create", self.wf, inp=spec)
        nid = out.get("nodeId")
        if not nid:
            raise SystemExit("create %s returned no nodeId: %s" % (key, out))
        st = self.state()
        st["nodes"][key] = nid
        self.save(st)
        print("  + %-28s %s  %s" % (key, nid, spec.get("name", "")))
        return nid

    def ensure_tool_node(self, key, spec):
        """Like ensure_node, but recreates when the toolType changed — it cannot be altered
        in place. The live node cannot be trusted to report its own type, so the type each
        node was created with is recorded in build-state and preferred over a live read."""
        st = self.state()
        want = (spec.get("tools") or [{}])[0].get("toolType")
        if key in st["nodes"]:
            have = (st.get("tooltypes") or {}).get(key)
            if have == want:
                return st["nodes"][key]
            if have is not None:
                self.clay("workflows", "nodes", "delete", self.wf, st["nodes"][key])
                st = self.state()
                st["nodes"].pop(key, None)
                st.get("tooltypes", {}).pop(key, None)
                self.save(st)
                print("  ! %-28s recreated (%s -> %s)" % (key, have, want))
        nid = self.ensure_node(key, spec)
        st = self.state()
        st.setdefault("tooltypes", {})[key] = want
        self.save(st)
        return nid

    def pin(self, source_key, path, typ="string"):
        """One pinned inputSchema property.

        Every pin must be sent on EVERY schema write: a schema write rebuilds the binding
        map from exactly what the call contains, reports success, and destroys whatever the
        call omitted."""
        st = self.state()
        src = st["nodes"][source_key] if source_key in st["nodes"] else source_key
        return {"type": typ, "sourceNodeId": src, "sourcePath": path}

    def wire(self, key, input_schema=None, edges=None, **fields):
        """Apply pins and parents to an existing node, then READ IT BACK.

        Reads back because the success echo is not proof: an omitted pin is silently
        dropped, and a pin nothing references is deleted on write."""
        st = self.state()
        nid = st["nodes"][key]
        payload = dict(fields)
        if input_schema is not None:
            payload["inputSchema"] = input_schema
        if edges is not None:
            out = []
            for e in edges:
                if isinstance(e, str):
                    out.append({"sourceNode": st["nodes"][e]})
                    continue
                if "sourceNode" in e:
                    out.append(dict(e))
                    continue
                ed = {"sourceNode": st["nodes"][e["from"]] if e["from"] in st["nodes"] else e["from"]}
                if e.get("default"):
                    ed["isDefaultRoute"] = True
                else:
                    ed["ruleId"] = e["rule"]
                    if e.get("name"):
                        ed["ruleName"] = e["name"]
                out.append(ed)
            payload["incomingEdges"] = out
        self.clay("workflows", "nodes", "update", self.wf, nid, inp=payload)
        back = self.clay("workflows", "nodes", "get", self.wf, nid)["node"]
        if input_schema is not None:
            want = {k for k, v in input_schema.get("properties", {}).items()
                    if "sourceNodeId" in v}
            got = {k for k, v in ((back.get("inputSchema") or {}).get("properties") or {}).items()
                   if v.get("sourceNodeId")}
            lost = want - got
            if lost:
                raise SystemExit("PINS LOST on %s: %s — re-send every pin on every write"
                                 % (key, sorted(lost)))
        print("  ~ %-28s wired" % key)
        return back

    def publish(self):
        self.clay("workflows", "publish", self.wf)
        print("published %s" % self.wf)


# ------------------------------------------------------------------- node specs


def rules_router(name, field, routes):
    """One rule per lane, testing one field for one value, so exactly one lane is ever
    reached and none is left pending.

    There is no join afterwards, on purpose: a plain edge from a writer into a shared
    terminal node hangs the run whenever a sibling lane was not taken."""
    return {
        "nodeType": "conditional", "name": name, "conditionalMode": "rules",
        "rulesConditionalConfig": {"rules": [
            {"id": "rule_" + r, "name": r.replace("_", " "),
             "condition": {"type": "GroupOp", "combinationMode": "And", "items": [
                 {"type": "BinOp", "dataPath": [field], "operator": "Equal", "value": r}]}}
            for r in routes
        ]},
    }


# The runtime's entry point is `handler`, not `run`. It fails with "No 'handler' function
# defined" and nothing but a live run reveals it.
TERMINAL_CODE = '''def handler(context):
    """Route taken when nothing is written. Exists so every lane of a conditional is
    covered — a conditional with no matching rule hard-fails the run."""
    return {"written": False}
'''


def terminal_node(name):
    return {"nodeType": "code", "name": name, "codeTimeoutMs": 30000, "code": TERMINAL_CODE}
