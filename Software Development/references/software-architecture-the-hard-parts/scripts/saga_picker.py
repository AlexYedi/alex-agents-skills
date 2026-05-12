#!/usr/bin/env python3
"""
saga_picker.py — interactive lookup over the 8 transactional sagas from
Software Architecture: The Hard Parts (Ford/Richards/Sadalage/Dehghani 2021,
Ch 11-12).

This is the *non-conversational* complement to the
`distributed-workflows-and-sagas` SKILL.md. The skill is for making a
defensible decision with full trade-off analysis and ADR. This tool is for
fast lookup: "I know my three axis answers, which saga is this?"

Usage:
    python saga_picker.py                # interactive
    python saga_picker.py --adr          # interactive + ADR scaffold to stdout
    python saga_picker.py --matrix       # print the full 8-saga matrix and exit
    python saga_picker.py -c sync -k atomic -d orchestrated   # non-interactive

Exit codes:
    0  success
    2  invalid arguments

Run with no arguments to enter interactive mode. The tool will NOT push you
toward better axis answers — that's the SKILL's job. This is a reference
lookup, not a deliberation tool.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# The 8-saga matrix (Table 2-1 in the book)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Saga:
    name: str
    code: str
    communication: str  # "synchronous" | "asynchronous"
    consistency: str    # "atomic" | "eventual"
    coordination: str   # "orchestrated" | "choreographed"
    coupling: str       # "very low" | "low" | "medium" | "high" | "very high"
    one_liner: str

    @property
    def address(self) -> str:
        """3-bit address: e.g., 's-a-o' for sync/atomic/orchestrated."""
        return "-".join((
            "s" if self.communication == "synchronous" else "a",
            "a" if self.consistency == "atomic" else "e",
            "o" if self.coordination == "orchestrated" else "c",
        ))


SAGAS: tuple[Saga, ...] = (
    Saga(
        name="Epic Saga",
        code="sao",
        communication="synchronous",
        consistency="atomic",
        coordination="orchestrated",
        coupling="very high",
        one_liner=(
            "Orchestrator runs synchronous atomic flow. The 'Saga pattern' most "
            "other materials describe. Highest coupling. Only when domain demands it."
        ),
    ),
    Saga(
        name="Phone Tag Saga",
        code="sac",
        communication="synchronous",
        consistency="atomic",
        coordination="choreographed",
        coupling="high",
        one_liner=(
            "Services call each other sync in a chain, atomic via compensation. "
            "Very brittle."
        ),
    ),
    Saga(
        name="Fairy Tale Saga",
        code="seo",
        communication="synchronous",
        consistency="eventual",
        coordination="orchestrated",
        coupling="high",
        one_liner=(
            "Sync orchestrated, eventual consistency. Useful when calls must be "
            "sync but atomic isn't required."
        ),
    ),
    Saga(
        name="Time Travel Saga",
        code="sec",
        communication="synchronous",
        consistency="eventual",
        coordination="choreographed",
        coupling="medium",
        one_liner=(
            "Sync chain, eventual consistency, no orchestrator. Hardest to reason "
            "about given the constraint mix."
        ),
    ),
    Saga(
        name="Fantasy Fiction Saga",
        code="aao",
        communication="asynchronous",
        consistency="atomic",
        coordination="orchestrated",
        coupling="high",
        one_liner=(
            "Async messages, atomic outcome, orchestrator. Rare; needs distributed "
            "transaction across async messaging."
        ),
    ),
    Saga(
        name="Horror Story",
        code="aac",
        communication="asynchronous",
        consistency="atomic",
        coordination="choreographed",
        coupling="medium",
        one_liner="Async, atomic, choreographed. The name says it.",
    ),
    Saga(
        name="Parallel Saga",
        code="aeo",
        communication="asynchronous",
        consistency="eventual",
        coordination="orchestrated",
        coupling="low",
        one_liner=(
            "Async, eventual, orchestrator. Modern default for complex workflows."
        ),
    ),
    Saga(
        name="Anthology Saga",
        code="aec",
        communication="asynchronous",
        consistency="eventual",
        coordination="choreographed",
        coupling="very low",
        one_liner="Async, eventual, choreographed. Lowest coupling. Modern default for simple flows.",
    ),
)


def find_saga(communication: str, consistency: str, coordination: str) -> Saga:
    for s in SAGAS:
        if (
            s.communication == communication
            and s.consistency == consistency
            and s.coordination == coordination
        ):
            return s
    raise AssertionError(
        f"no saga for ({communication}, {consistency}, {coordination}) — "
        "this is a bug in the matrix"
    )


# ---------------------------------------------------------------------------
# Interactive prompting
# ---------------------------------------------------------------------------

def ask_choice(prompt: str, options: tuple[tuple[str, str], ...]) -> str:
    """Prompt user; accept letter, number, or full word. Returns canonical value."""
    print()
    print(prompt)
    for i, (letter, value) in enumerate(options, start=1):
        print(f"  {i}) {value}  [{letter}]")
    valid_letters = {letter: value for letter, value in options}
    valid_values = {value for _letter, value in options}
    while True:
        raw = input("> ").strip().lower()
        if not raw:
            print("(please enter a value)", file=sys.stderr)
            continue
        # Try number
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1][1]
        # Try letter
        if raw in valid_letters:
            return valid_letters[raw]
        # Try full word
        if raw in valid_values:
            return raw
        print(f"(invalid; expected one of {sorted(valid_values)} or a letter)", file=sys.stderr)


def interactive() -> tuple[str, str, str]:
    print()
    print("  saga_picker — fast lookup over the 8-saga matrix")
    print("  (for a full decision with trade-off table, load")
    print("   `distributed-workflows-and-sagas` SKILL instead)")
    print()

    comm = ask_choice(
        "Communication: does the caller need to wait for a response?",
        (("s", "synchronous"), ("a", "asynchronous")),
    )
    cons = ask_choice(
        "Consistency: must the transaction commit atomically across all services?",
        (("a", "atomic"), ("e", "eventual")),
    )
    coord = ask_choice(
        "Coordination: is there a central orchestrator, or do services react via events?",
        (("o", "orchestrated"), ("c", "choreographed")),
    )
    return comm, cons, coord


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_saga(s: Saga) -> None:
    print()
    print("━" * 72)
    print(f"  {s.name} ({s.code})")
    print("━" * 72)
    print(f"  Communication : {s.communication}")
    print(f"  Consistency   : {s.consistency}")
    print(f"  Coordination  : {s.coordination}")
    print(f"  Coupling      : {s.coupling}")
    print()
    print(f"  {s.one_liner}")
    print()
    print(f"  Reference: references/software-architecture-the-hard-parts/")
    print(f"             frameworks.md#the-8-transactional-sagas")
    print("━" * 72)
    print()


ADR_TEMPLATE = """\
ADR-NNN: {name} for <workflow-name>

Context:
  Workflow:           <one-sentence business workflow>
  Participants:       <list of services>
  Trigger:            <sync/async user-facing trigger>
  Success criterion:  <what success means at the data layer>
  Failure criterion:  <what failure means at the data layer>

Decision:
  We will use {name} ({code}) for this workflow.

Axis answers:
  Communication: {communication} — because <reason>
  Consistency:   {consistency} — because <reason>
  Coordination:  {coordination} — because <reason>

Trade-off table:
  | Property                 | Score                          | Notes |
  |--------------------------|--------------------------------|-------|
  | Operational complexity   | low / med / high               |       |
  | Failure-handling effort  | low / med / high               |       |
  | Coupling strength        | {coupling:<28} |       |
  | Performance              | adequate / concerning          |       |

Consequences:
  Positive:
    - <…>
  Negative:
    - <…>
  Mitigations:
    - <…>

Notes:
  Generated by saga_picker.py — this is a scaffold for fast capture.
  For a full deliberation (with walk-back checkpoints and trade-off
  scoring), load `distributed-workflows-and-sagas` SKILL.
"""


def print_adr_scaffold(s: Saga) -> None:
    print(ADR_TEMPLATE.format(
        name=s.name,
        code=s.code,
        communication=s.communication,
        consistency=s.consistency,
        coordination=s.coordination,
        coupling=s.coupling,
    ))


def print_matrix() -> None:
    print()
    print("  The 8 Transactional Sagas (Hard Parts Ch 12, Table 2-1)")
    print()
    fmt = "  {:<22} {:<5} {:<14} {:<10} {:<14} {:<10}"
    print(fmt.format("Pattern", "Code", "Communication", "Consistency", "Coordination", "Coupling"))
    print("  " + "─" * 78)
    for s in SAGAS:
        print(fmt.format(
            s.name, s.code, s.communication, s.consistency, s.coordination, s.coupling,
        ))
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pick a saga pattern from the 8-saga matrix.",
        epilog=(
            "Run with no flags for interactive prompts. For a real decision, "
            "load the `distributed-workflows-and-sagas` SKILL instead."
        ),
    )
    p.add_argument(
        "-c", "--communication",
        choices=("sync", "synchronous", "async", "asynchronous"),
        help="Communication axis",
    )
    p.add_argument(
        "-k", "--consistency",
        choices=("atomic", "eventual"),
        help="Consistency axis",
    )
    p.add_argument(
        "-d", "--coordination",
        choices=("orchestrated", "choreographed"),
        help="Coordination axis",
    )
    p.add_argument(
        "--adr",
        action="store_true",
        help="After picking, print an ADR scaffold to stdout",
    )
    p.add_argument(
        "--matrix",
        action="store_true",
        help="Print the full 8-saga matrix and exit",
    )
    return p.parse_args(argv)


def normalize(comm: Optional[str]) -> Optional[str]:
    if comm is None:
        return None
    return {"sync": "synchronous", "async": "asynchronous"}.get(comm, comm)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)

    if args.matrix:
        print_matrix()
        return 0

    comm = normalize(args.communication)
    cons = args.consistency
    coord = args.coordination

    # Mix of CLI flags and interactive prompts is intentionally not supported:
    # either all 3 flags, or none.
    flags_count = sum(x is not None for x in (comm, cons, coord))
    if flags_count not in (0, 3):
        print(
            "error: provide all of --communication / --consistency / --coordination, "
            "or none (for interactive mode).",
            file=sys.stderr,
        )
        return 2

    if flags_count == 0:
        comm, cons, coord = interactive()

    assert comm is not None and cons is not None and coord is not None
    saga = find_saga(comm, cons, coord)
    print_saga(saga)

    if args.adr:
        print_adr_scaffold(saga)

    return 0


if __name__ == "__main__":
    sys.exit(main())
