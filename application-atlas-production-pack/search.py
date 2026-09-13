#!/usr/bin/env python3
"""Atlas semantic search: query -> top-k leaves + one-hop neighbors + boundary notes.
Usage:
  python3 search.py "中文或英文查询" [k]
"""
import json
import os
import sqlite3
import sys
import urllib.request
import numpy as np

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OLLAMA = "http://localhost:11434/api/embed"


def embed_query(q):
    body = json.dumps({"model": "bge-m3", "input": [q]}).encode()
    req = urllib.request.Request(OLLAMA, body, {"Content-Type": "application/json"})
    return np.array(json.load(urllib.request.urlopen(req, timeout=120))["embeddings"][0], dtype=np.float32)


def search(q, k=3, with_neighbors=True):
    con = sqlite3.connect(DB)
    qv = embed_query(q)
    qv /= (np.linalg.norm(qv) + 1e-9)
    rows = con.execute("SELECT slug, vec FROM embedding").fetchall()
    slugs = np.array([r[0] for r in rows])
    mat = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
    mat /= (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
    sims = mat @ qv
    top_idx = np.argsort(-sims)[:k]
    results = []
    for i in top_idx:
        slug = slugs[i]
        leaf = con.execute("SELECT name, name_zh, overview, defining_core, l0_zh FROM leaf WHERE slug=?",
                           (slug,)).fetchone()
        rels = con.execute("""SELECT to_name, to_slug, rel_kind, distinction FROM relation
                              WHERE from_slug=? LIMIT 6""", (slug,)).fetchall()
        results.append({
            "slug": slug, "score": round(float(sims[i]), 3),
            "name": leaf[0], "name_zh": leaf[1],
            "overview": (leaf[2] or "")[:300],
            "l0_zh": (leaf[4] or leaf[3] or "")[:220],
            "neighbors": [{"name": r[0], "slug": r[1], "kind": r[2]} for r in rels],
        })
    con.close()
    return results


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else "expense reimbursement"
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    for r in search(q, k):
        print(f"\n[{r['score']}] {r['name']}  /  {r['name_zh']}  ({r['slug']})")
        print(f"  zh-L0: {r['l0_zh']}")
        nb = ", ".join(f"{n['name']}({n['kind']})" for n in r["neighbors"][:4])
        print(f"  neighbors: {nb}")


if __name__ == "__main__":
    main()
