#!/usr/bin/env python3
"""Gate regression: run promoted classify() over 52 pilot items with retry/backoff."""
import json
import os
import sys
import time

PACK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PACK)
from classify import candidates

items = json.load(open(os.path.join(PACK, "pilot_clean.json"))) + \
    json.load(open(os.path.join(PACK, "pilot_synthetic.json")))

out = []
for i, it in enumerate(items):
    pred = None
    for attempt in range(5):
        try:
            pool, sims = candidates(it["desc"])
            ret1 = pool[0] == it["expect"]
            from classify import classify
            r = classify(it["desc"])
            pred = r["choice"]
            if pred and pred != "none":
                break
        except Exception as e:
            print(f"[{i}] retry {attempt}: {e}", file=sys.stderr)
            time.sleep(15 * (attempt + 1))
    pred = pred or "none"
    hit = pred == it["expect"]
    out.append({"name": it["name"], "expect": it["expect"], "got": pred, "hit": hit,
                "ret1": ret1, "ret5": it["expect"] in candidates(it["desc"])[0]})
    print(f"{'OK ' if hit else 'MISS'} {it['name']}: {pred}", flush=True)

real = [o for o in out if not o["name"].startswith("synthetic")]
n = len(out)
acc = sum(o["hit"] for o in out) / n
print(f"\n=== GATE (n={n}) adj={acc:.1%} real={sum(o['hit'] for o in real)}/{len(real)} "
      f"ret1={sum(o['ret1'] for o in out)/n:.1%} ret5={sum(o['ret5'] for o in out)/n:.1%} ===")
json.dump(out, open(os.path.join(PACK, "atlas", "gate_regression.json"), "w"), ensure_ascii=False, indent=1)
