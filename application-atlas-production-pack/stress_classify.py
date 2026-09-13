#!/usr/bin/env python3
"""Classify all 1804 synthetic instances back into the atlas (qwen3.8-flash, 12 concurrent).
Output: atlas/stress_results.jsonl (slug, predicted, correct). Resumable."""
import json
import os
import queue
import sys
import threading
import time

PACK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PACK)
from classify import classify

INST = os.path.join(PACK, "atlas", "stress_instances.jsonl")
OUT = os.path.join(PACK, "atlas", "stress_results.jsonl")
LOG = os.path.join(PACK, "logs", "stress-classify.log")
WORKERS = 6

have = set()
if os.path.exists(OUT):
    for line in open(OUT, encoding="utf-8"):
        try:
            have.add(json.loads(line)["slug"])
        except Exception:
            pass

items = []
for line in open(INST, encoding="utf-8"):
    r = json.loads(line)
    if r["slug"] not in have:
        items.append(r)

log = open(LOG, "a", encoding="utf-8")
log.write(f"\n=== classify start {time.strftime('%F %T')}, todo={len(items)} ===\n")
q = queue.Queue()
for it in items:
    q.put(it)
out_lock = threading.Lock()
out = open(OUT, "a", encoding="utf-8")
t0 = time.time()
done = [0]
correct = [0]


def worker():
    while True:
        try:
            it = q.get_nowait()
        except queue.Empty:
            return
        pred, ok = None, 0
        for attempt in range(5):
            try:
                r = classify(it["desc"])
                pred = r["choice"]
                if pred and pred != "none":
                    break
            except Exception:
                pass
            pred = "none"
            time.sleep(15 * (attempt + 1))
        ok = int(pred == it["slug"])
        with out_lock:
            out.write(json.dumps({"slug": it["slug"], "name_zh": it["name_zh"],
                                  "predicted": pred, "correct": ok}, ensure_ascii=False) + "\n")
            out.flush()
            done[0] += 1
            correct[0] += ok
            if done[0] % 50 == 0:
                rate = done[0] / (time.time() - t0)
                log.write(f"[{done[0]}/{len(items)}] acc={correct[0]/done[0]:.1%} "
                          f"{rate*60:.0f}/min ETA {(len(items)-done[0])/max(rate,0.01)/60:.0f}min\n")
                log.flush()
        q.task_done()


threads = [threading.Thread(target=worker, daemon=True) for _ in range(WORKERS)]
for t in threads:
    t.start()
for t in threads:
    t.join()
out.close()
log.write(f"CLASSIFY DONE {done[0]} acc={correct[0]/max(done[0],1):.1%}\n")
log.close()
print("DONE", done[0], "acc", correct[0] / max(done[0], 1))
