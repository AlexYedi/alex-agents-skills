#!/usr/bin/env python3
"""
ScaleDown HTTP client for the book-distiller pipeline.

Subcommands:
  screen    Run ScaleDown /summarize + /extract on a chunk for triage (Stage 0)
  index     Run ScaleDown /summarize + /extract for full indexing (Stage 1)
  extract   Run ScaleDown /extract only with the book-distillation entity schema
  summarize Run ScaleDown /summarize only with structured digest instructions

Reads SCALEDOWN_API_KEY from environment. Source /tmp/scaledown_key.env first.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib import request, error

API_BASE = "https://api.scaledown.xyz"
EXTRACT_URL = f"{API_BASE}/extract"
SUMMARIZE_URL = f"{API_BASE}/summarization/abstractive"
COMPRESS_URL = f"{API_BASE}/compress/raw/"
CLASSIFY_URL = f"{API_BASE}/classify"

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ENTITY_SCHEMA_PATH = SKILL_DIR / "references" / "entity-schema.json"

DIGEST_INSTRUCTIONS = (
    "Produce a structured digest with three sections: FRAMEWORKS (named patterns), "
    "PRINCIPLES (design rules), ANTI-PATTERNS (named failure modes). "
    "Use bullet points. No introduction. No conclusion. Quote names verbatim where used."
)

MAX_RETRIES = 3
BACKOFF_BASE = 2.0


def get_api_key() -> str:
    key = os.environ.get("SCALEDOWN_API_KEY")
    if not key:
        sys.exit(
            "ERROR: SCALEDOWN_API_KEY not set. Source /tmp/scaledown_key.env first.\n"
            "  source /tmp/scaledown_key.env && python3 scaledown_client.py ..."
        )
    return key


def _post(url: str, payload: dict, api_key: str) -> dict:
    """POST to a ScaleDown endpoint with retry-on-429/5xx."""
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
    }
    last_err = None
    for attempt in range(MAX_RETRIES):
        try:
            req = request.Request(url, data=body, headers=headers, method="POST")
            with request.urlopen(req, timeout=180) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES - 1:
                wait = BACKOFF_BASE ** attempt
                print(f"  retry in {wait:.1f}s (HTTP {e.code})", file=sys.stderr)
                time.sleep(wait)
                continue
            err_body = e.read().decode("utf-8", errors="replace")
            sys.exit(f"ERROR: HTTP {e.code} from {url}\n{err_body}")
        except error.URLError as e:
            last_err = e
            if attempt < MAX_RETRIES - 1:
                time.sleep(BACKOFF_BASE ** attempt)
                continue
            sys.exit(f"ERROR: network failure to {url}: {e}")
    sys.exit(f"ERROR: exhausted retries to {url}: {last_err}")


def load_entity_schema() -> dict:
    with open(ENTITY_SCHEMA_PATH) as f:
        schema = json.load(f)
    return {
        "threshold": schema.get("threshold", 0.4),
        "entities": {
            name: {"description": v["description"]}
            for name, v in schema["entities"].items()
        },
    }


def call_extract(text: str, api_key: str) -> dict:
    schema = load_entity_schema()
    payload = {"text": text, "threshold": schema["threshold"], "entities": schema["entities"]}
    return _post(EXTRACT_URL, payload, api_key)


def call_summarize(text: str, api_key: str, max_tokens: int = 1500) -> dict:
    payload = {"text": text, "instructions": DIGEST_INSTRUCTIONS, "max_tokens": max_tokens}
    return _post(SUMMARIZE_URL, payload, api_key)


def filter_entities(extract_response: dict, min_confidence: float = 0.6) -> dict:
    """Drop entities below confidence threshold."""
    entities = extract_response.get("entities", [])
    kept = [e for e in entities if e.get("confidence", 0) >= min_confidence]
    return {
        "entities": kept,
        "_filter_meta": {
            "raw_count": len(entities),
            "kept_count": len(kept),
            "min_confidence": min_confidence,
        },
    }


def cmd_screen(args):
    """Stage 0: cheap triage — summarize + extract, smaller cap."""
    api_key = get_api_key()
    text = Path(args.chunk).read_text()
    print(f"  /summarize ({len(text)} chars)...", file=sys.stderr)
    summary = call_summarize(text, api_key, max_tokens=600)
    print(f"  /extract ({len(text)} chars)...", file=sys.stderr)
    entities = call_extract(text, api_key)
    filtered = filter_entities(entities, min_confidence=0.6)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "screen_digest.md").write_text(summary.get("summary", ""))
    (out_dir / "screen_entities.json").write_text(json.dumps(filtered, indent=2))
    print(json.dumps({
        "stage": "screen",
        "summary_chars": summary.get("output_chars"),
        "entities_kept": filtered["_filter_meta"]["kept_count"],
        "entities_raw": filtered["_filter_meta"]["raw_count"],
        "out_dir": str(out_dir),
    }, indent=2))


def cmd_index(args):
    """Stage 1: full indexing — summarize + extract, full cap."""
    api_key = get_api_key()
    text = Path(args.chunk).read_text()
    print(f"  /summarize ({len(text)} chars)...", file=sys.stderr)
    summary = call_summarize(text, api_key, max_tokens=1500)
    print(f"  /extract ({len(text)} chars)...", file=sys.stderr)
    entities = call_extract(text, api_key)
    filtered = filter_entities(entities, min_confidence=0.6)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "digest.md").write_text(summary.get("summary", ""))
    (out_dir / "entities.json").write_text(json.dumps(filtered, indent=2))
    (out_dir / "entities_raw.json").write_text(json.dumps(entities, indent=2))
    print(json.dumps({
        "stage": "index",
        "summary_chars": summary.get("output_chars"),
        "entities_kept": filtered["_filter_meta"]["kept_count"],
        "entities_raw": filtered["_filter_meta"]["raw_count"],
        "out_dir": str(out_dir),
    }, indent=2))


def cmd_extract(args):
    api_key = get_api_key()
    text = Path(args.chunk).read_text()
    result = call_extract(text, api_key)
    if args.filter:
        result = filter_entities(result, min_confidence=args.filter)
    print(json.dumps(result, indent=2))


def cmd_summarize(args):
    api_key = get_api_key()
    text = Path(args.chunk).read_text()
    result = call_summarize(text, api_key, max_tokens=args.max_tokens)
    if args.summary_only:
        print(result.get("summary", ""))
    else:
        print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_screen = sub.add_parser("screen", help="Stage 0: triage chunk")
    p_screen.add_argument("chunk", help="Path to chapter chunk text file")
    p_screen.add_argument("out_dir", help="Output directory for digest + entities")
    p_screen.set_defaults(func=cmd_screen)

    p_index = sub.add_parser("index", help="Stage 1: full chunk indexing")
    p_index.add_argument("chunk", help="Path to chapter chunk text file")
    p_index.add_argument("out_dir", help="Output directory for digest + entities")
    p_index.set_defaults(func=cmd_index)

    p_extract = sub.add_parser("extract", help="Run /extract only")
    p_extract.add_argument("chunk", help="Path to chunk text file")
    p_extract.add_argument("--filter", type=float, default=None,
                           help="Min confidence (0-1) to keep entities")
    p_extract.set_defaults(func=cmd_extract)

    p_sum = sub.add_parser("summarize", help="Run /summarize only")
    p_sum.add_argument("chunk", help="Path to chunk text file")
    p_sum.add_argument("--max-tokens", type=int, default=1500)
    p_sum.add_argument("--summary-only", action="store_true",
                       help="Print only summary text, not full JSON")
    p_sum.set_defaults(func=cmd_summarize)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
