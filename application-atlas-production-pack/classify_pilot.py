#!/usr/bin/env python3
"""Classification pilot: embed product desc -> top-3 leaves -> LLM adjudication -> accuracy."""
import json
import os
import re
import sqlite3
import urllib.request
import numpy as np

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
API = "https://opencode.ai/zen/go/v1/chat/completions"
KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]


def embed(texts):
    body = json.dumps({"model": "bge-m3", "input": texts}).encode()
    req = urllib.request.Request("http://localhost:11434/api/embed", body, {"Content-Type": "application/json"})
    return [np.array(e, dtype=np.float32) for e in json.load(urllib.request.urlopen(req, timeout=600))["embeddings"]]


def pairwise_distinctions(con, cands):
    """Pull the atlas's own boundary text between candidate pairs."""
    slugs = [c["slug"] for c in cands]
    lines = []
    for i, a in enumerate(slugs):
        for b in slugs[i+1:]:
            r = con.execute("""SELECT from_slug, to_name, distinction FROM relation
                               WHERE (from_slug=? AND to_slug=?) OR (from_slug=? AND to_slug=?)""",
                            (a, b, b, a)).fetchone()
            if r and r[2]:
                lines.append(f"{r[1]} vs 相邻类型的分界: {r[2][:200]}")
    return "\n".join(lines[:6])


def adjudicate(desc, cands, bounds=""):
    cand_txt = "\n\n".join(
        f"候选{i+1}: {c['name_zh']} ({c['slug']})\n定义: {c['l0_zh'] or c['overview'][:200]}"
        for i, c in enumerate(cands))
    btxt = f"\n候选类型之间的分界记录（来自语料库）:\n{bounds}\n" if bounds else ""
    prompt = f"""你是软件类型分类裁决器。给定一个产品的描述和 5 个候选类型，选出最匹配的一个；如果都不匹配选 "none"。
注意：利用候选类型之间的分界记录区分近义类型。

产品描述: {desc}

{cand_txt}
{btxt}
只输出 JSON: {{"choice": "<slug 或 none>", "reason": "一句话理由"}}"""
    body = {"model": "qwen3.7-max", "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1, "max_tokens": 2000}
    req = urllib.request.Request(API, json.dumps(body).encode(),
                                 {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
                                  "x-opencode-session": "atlas-pilot", "User-Agent": "atlas-pilot/1.0"})
    r = json.load(urllib.request.urlopen(req, timeout=240))
    txt = (r["choices"][0]["message"].get("content") or "").strip()
    m = re.search(r"\{.*\}", txt, re.S)
    if m:
        return json.loads(m.group(0))
    return {"choice": "parse-error", "reason": txt[:100]}


def main():
    con = sqlite3.connect(DB)
    slugs = [r[0] for r in con.execute("SELECT slug FROM embedding")]
    rows = con.execute("SELECT slug, vec FROM embedding").fetchall()
    mat = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    mat = mat / (norms + 1e-9)
    slug_arr = [r[0] for r in rows]

    items = json.load(open(os.path.join(PACK, "pilot_clean.json")))
    items += json.load(open(os.path.join(PACK, "pilot_synthetic.json")))

    vecs = embed([it["desc"] for it in items])
    out = []
    for it, v in zip(items, vecs):
        v = v / (np.linalg.norm(v) + 1e-9)
        sims = mat @ v
        top = np.argsort(-sims)[:10]
        cands = []
        for i in top:
            slug = slug_arr[i]
            leaf = con.execute("SELECT name_zh, overview, defining_core, l0_zh FROM leaf WHERE slug=?",
                               (slug,)).fetchone()
            cands.append({"slug": slug, "score": round(float(sims[i]), 3), "name_zh": leaf[0],
                          "overview": leaf[1], "l0_zh": leaf[3]})
        bounds = pairwise_distinctions(con, cands)
        adj = adjudicate(it["desc"], cands, bounds)
        choice = adj.get("choice", "").strip()
        hit = choice == it["expect"]
        ret_top1 = cands[0]["slug"] == it["expect"]
        out.append({"name": it["name"], "expect": it["expect"], "choice": choice,
                    "reason": adj.get("reason", "")[:80], "hit": hit, "ret_top1": ret_top1,
                    "top5": [(c["slug"], c["score"]) for c in cands]})
        print(f"{'OK ' if hit else 'MISS'} {it['name']}: expect={it['expect']} got={choice} | ret1={ret_top1} | {adj.get('reason','')[:60]}", flush=True)

    n = len(out)
    adj_acc = sum(o["hit"] for o in out) / n
    ret_acc = sum(o["ret_top1"] for o in out) / n
    ret3 = sum(any(t[0] == o["expect"] for t in o["top5"]) for o in out) / n
    real = [o for o in out if not o["name"].startswith("synthetic")]
    syn = [o for o in out if o["name"].startswith("synthetic")]
    print(f"\n=== GATE REPORT (n={n}) ===")
    print(f"adj top-1: {adj_acc:.1%}  (gate >= 90%)")
    print(f"retrieval top-1: {ret_acc:.1%}  top-3 recall: {ret3:.1%}")
    print(f"real (n={len(real)}): adj {sum(o['hit'] for o in real)/max(len(real),1):.1%} | synthetic (n={len(syn)}): adj {sum(o['hit'] for o in syn)/max(len(syn),1):.1%}")
    json.dump(out, open(os.path.join(PACK, "pilot_results.json"), "w"), ensure_ascii=False, indent=1)
    print("saved pilot_results.json")


if __name__ == "__main__":
    main()
