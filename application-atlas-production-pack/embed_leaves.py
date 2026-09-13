#!/usr/bin/env python3
"""Embed all leaves with bge-m3 (local ollama) into atlas.sqlite (embedding table)."""
import json
import os
import sqlite3
import time
import urllib.request
import numpy as np

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OLLAMA = "http://localhost:11434/api/embed"
BATCH = 32


def embed(texts):
    body = json.dumps({"model": "bge-m3", "input": texts}).encode()
    req = urllib.request.Request(OLLAMA, body, {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=600))
    return [np.array(e, dtype=np.float32) for e in r["embeddings"]]


def compose(name, name_zh, ov, dc, l0):
    parts = []
    if name:
        parts.append(name)
    if name_zh:
        parts.append(f"({name_zh})")
    head = " ".join(parts)
    body = []
    for t in (l0, ov, dc):
        if t:
            body.append(t[:2600])
    text = f"{head}\n\n" + "\n\n".join(body)
    return text[:6000]


def main():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS embedding (
      slug TEXT PRIMARY KEY, model TEXT, dim INTEGER, vec BLOB)""")
    done = {r[0] for r in cur.execute("SELECT slug FROM embedding")}
    rows = cur.execute("SELECT slug, name, name_zh, overview, defining_core, l0_zh FROM leaf ORDER BY order_idx").fetchall()
    todo = [(s, n, nz, ov, dc, l0) for s, n, nz, ov, dc, l0 in rows if s not in done]
    print(f"total {len(rows)}, done {len(done)}, todo {len(todo)}", flush=True)
    t0 = time.time()
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        texts = [compose(n, nz, ov, dc, l0) for _, n, nz, ov, dc, l0 in chunk]
        vecs = embed(texts)
        for (slug, *_), v in zip(chunk, vecs):
            cur.execute("INSERT OR REPLACE INTO embedding VALUES (?,?,?,?)",
                        (slug, "bge-m3", len(v), v.tobytes()))
        con.commit()
        if (i // BATCH) % 5 == 0:
            rate = (i + len(chunk)) / max(time.time() - t0, 1)
            eta = (len(todo) - i) / max(rate, 0.01) / 60
            print(f"[{i+len(chunk)}/{len(todo)}] rate {rate*60:.0f}/min ETA {eta:.1f}min", flush=True)
    con.close()
    print(f"EMBED DONE in {(time.time()-t0)/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
