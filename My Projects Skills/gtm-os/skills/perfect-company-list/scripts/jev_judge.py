#!/usr/bin/env python3
"""Judge every company in a CSV against one ICP question with Jev (TypeSafe).

Batches 20 companies per request (one yes/no question per company over a shared state),
runs requests in parallel, and writes the input CSV back out with a p_fit column.

usage:
  TYPESAFE_API_KEY=... python jev_judge.py companies.csv out.csv \
      --question "Is this company a bank or savings institution that takes deposits?" \
      --yes "A deposit-taking bank or thrift" \
      --no  "Anything else: credit union, lender, fintech, vendor, association" \
      [--threshold 0.5] [--workers 16] [--batch 20]

The CSV needs a domain column. name/company_name, industry and description are used when present.
Standard library only.
"""
import argparse, csv, json, os, sys, time, urllib.request, urllib.error
import concurrent.futures as cf

URL = "https://api.typesafe.ai/v1/systemone"


def call(key, state, questions, retries=6):
    body = json.dumps({"state": state, "model": "jev-latest", "questions": questions}).encode()
    for a in range(retries):
        try:
            req = urllib.request.Request(URL, data=body, headers={"Authorization": "Bearer " + key,
                                                                  "Content-Type": "application/json"})
            return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504, 529):
                time.sleep(2 ** a)
                continue
            raise RuntimeError(f"Jev HTTP {e.code}: {e.read()[:300]!r}")
        except (urllib.error.URLError, TimeoutError):
            time.sleep(2 ** a)
    raise RuntimeError("Jev: retries exhausted")


def card(row):
    return {"name": row.get("name") or row.get("company_name") or "",
            "domain": row.get("domain", ""),
            "linkedin_industry": row.get("industry", ""),
            "description": (row.get("description") or "")[:300]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp"); ap.add_argument("out")
    ap.add_argument("--question", required=True)
    ap.add_argument("--yes", required=True)
    ap.add_argument("--no", required=True)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--batch", type=int, default=20)
    a = ap.parse_args()
    key = os.environ.get("TYPESAFE_API_KEY") or sys.exit("set TYPESAFE_API_KEY")

    rows = list(csv.DictReader(open(a.inp, newline="", encoding="utf-8")))
    chunks = [rows[i:i + a.batch] for i in range(0, len(rows), a.batch)]
    crit = {"true": a.yes, "false": a.no}

    def run(ch):
        qs = {f"q{i}": {"type": "noul", "criteria": crit,
                        "instructions": f"{a.question} Answer only about `companies[{i}]`."}
              for i in range(len(ch))}
        r = call(key, {"companies": [card(x) for x in ch]}, qs)
        return [r["answers"][f"q{i}"]["noul"] for i in range(len(ch))], r["usage"]["input_tokens"]

    tokens = 0
    with cf.ThreadPoolExecutor(a.workers) as ex:
        for ch, (ps, t) in zip(chunks, ex.map(run, chunks)):
            tokens += t
            for row, p in zip(ch, ps):
                row["p_fit"] = f"{p:.3f}"
                row["fit"] = "yes" if p >= a.threshold else "no"

    fields = list(rows[0].keys()) if rows else ["domain", "p_fit", "fit"]
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    fits = sum(r["fit"] == "yes" for r in rows)
    print(f"{len(rows)} in / {fits} fit, {tokens:,} input tokens (~${tokens * 0.042 / 1e6:.4f} at $0.042/M)")


if __name__ == "__main__":
    main()
