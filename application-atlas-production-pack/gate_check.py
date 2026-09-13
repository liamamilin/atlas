#!/usr/bin/env python3
"""Classify the fixed pilot set; exit nonzero on failures or accuracy below 90%.
Use --score-only FILE to rescore saved predictions without model calls.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time
from atlas_runtime import PACK, atomic_json

# Explicit owner adjudications documented in USAGE_ROADMAP.md, 2026-09-10.
ACCEPTED_ALTERNATIVES = {
    "钉钉": {"team-workspace-platform"},
    "简道云": {"no-code-application-builder"},
    "synthetic-20": {"kanban-task-board"},
}
BASELINE_GATE = 0.90


def score_rows(rows, items):
    expected = {item["name"]: item for item in items}
    if len(rows) != len(items) or len({r["name"] for r in rows}) != len(rows):
        raise ValueError("回归结果数量不完整或包含重复样本")
    if {r["name"] for r in rows} != set(expected):
        raise ValueError("回归结果与固定样本集不一致")
    scored = []
    for row in rows:
        item = expected[row["name"]]
        raw = row.get("got") == item["expect"]
        accepted = row.get("got") in ACCEPTED_ALTERNATIVES.get(row["name"], set())
        scored.append({**row, "expect": item["expect"], "raw_hit": raw,
                       "hit": (raw or accepted) and not row.get("error"), "accepted_alternative": accepted})
    total = len(scored)
    errors = sum(bool(r.get("error")) for r in scored)
    accuracy = sum(bool(r["hit"]) for r in scored) / total if total else 0
    summary = {"total": total, "raw_accuracy": sum(r["raw_hit"] for r in scored) / total if total else 0,
               "accuracy": accuracy, "threshold": BASELINE_GATE, "errors": errors,
               "passed": bool(total) and not errors and accuracy >= BASELINE_GATE,
               "generated": datetime.now(timezone.utc).isoformat()}
    return scored, summary


def run_items(items, classify_fn, sleep=time.sleep):
    rows = []
    for item in items:
        result, error = None, None
        for attempt in range(3):
            try:
                result = classify_fn(item["desc"])
                error = None
                break
            except Exception as exc:
                error = str(exc)
                if attempt < 2:
                    sleep(5 * (attempt + 1))
        pool = result.get("pool", []) if result else []
        row = {"name": item["name"], "expect": item["expect"],
               "got": result["choice"] if result else "none",
               "ret1": bool(pool) and pool[0] == item["expect"],
               "ret5": item["expect"] in pool[:5], "ret_pool": item["expect"] in pool}
        if error:
            row["error"] = error
        rows.append(row)
        print(f"[{len(rows)}/{len(items)}] {item['name']}: {row['got']}", flush=True)
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--score-only", type=Path)
    args = parser.parse_args()
    items = json.loads((PACK / "pilot_clean.json").read_text()) + json.loads((PACK / "pilot_synthetic.json").read_text())
    if args.score_only:
        rows = json.loads(args.score_only.read_text())
    else:
        from classify import classify
        rows = run_items(items, classify)
    rows, summary = score_rows(rows, items)
    if not args.score_only:
        atomic_json(PACK / "atlas/gate_regression.json", rows)
        atomic_json(PACK / "atlas/gate_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
