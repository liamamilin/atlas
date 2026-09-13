#!/usr/bin/env python3
"""Atlas classification pipeline (Phase-2 pilot, final config).

  query (product description, zh/en) -> bge-m3 body embedding
    -> top-10 candidates
    -> +1-hop graph neighbors of top-5 (ranked by sim, +6)
    -> capped 16-candidate pool
    -> cheap LLM scoring adjudicator (qwen3.8-flash), each candidate scored 0-10
       with corpus pairwise-boundary records injected
    -> argmax (or none)

Usage: python3 classify.py "产品描述..."
"""
import json, os, re, sqlite3, sys, urllib.request
import numpy as np

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]
ADJUDICATOR = os.environ.get("ATLAS_ADJUDICATOR", "qwen3.8-flash")
POOL_MAX = 16

_con = sqlite3.connect(DB)
_rows = _con.execute("SELECT slug, vec FROM embedding").fetchall()
_M = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in _rows])
_Mn = _M / (np.linalg.norm(_M, axis=1, keepdims=True) + 1e-9)
_slugs = [r[0] for r in _rows]
_s2i = {s: i for i, s in enumerate(_slugs)}
_leaf_info = {r[0]: (r[1], (r[2] or r[3] or "")[:170]) for r in
              _con.execute("SELECT slug, name_zh, l0_zh, overview FROM leaf")}
_nb = {}
for a, b in _con.execute("SELECT from_slug, to_slug FROM relation WHERE to_slug IS NOT NULL"):
    _nb.setdefault(a, set()).add(b)
    _nb.setdefault(b, set()).add(a)
_rels = {}
for a, b, tn, d in _con.execute("SELECT from_slug, to_slug, to_name, distinction FROM relation WHERE to_slug IS NOT NULL AND distinction != ''"):
    _rels.setdefault((a, b), (tn, d))

PROMPT = """你是软件类型分类器。对下列每个候选类型，独立打 0-10 分表示与产品描述的匹配度（互不比较，仅看各自定义）。
产品描述: {desc}
候选:
{cands}
{bounds}
输出 JSON 数组: [{{"slug":"...","score":0-10,"brief":"≤12字"}}] 然后输出 {{"choice":"最高分slug或none"}}。"""


def _embed(texts):
    b = json.dumps({"model": "bge-m3", "input": texts}).encode()
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://localhost:11434/api/embed", b, {"Content-Type": "application/json"}), timeout=600))
    return [np.array(e, dtype=np.float32) for e in r["embeddings"]]


def _pairwise(sl):
    lines = []
    for i, a in enumerate(sl):
        for b in sl[i + 1:]:
            r = _rels.get((a, b)) or _rels.get((b, a))
            if r:
                lines.append(f"{r[0]} vs 相邻: {r[1][:140]}")
    return "\n".join(lines[:8])


def candidates(qtext, k=10):
    v = _embed([qtext])[0]
    v /= (np.linalg.norm(v) + 1e-9)
    sims = _Mn @ v
    order = np.argsort(-sims)
    top10 = [_slugs[i] for i in order[:k]]
    pool, seen = list(top10), set(top10)
    nbs = []
    for s in top10[:5]:
        for n in _nb.get(s, set()):
            if n not in seen:
                nbs.append((sims[_s2i[n]], n))
    nbs.sort(reverse=True)
    for _, n in nbs[:POOL_MAX - k]:
        pool.append(n)
        seen.add(n)
    return pool[:POOL_MAX], sims


def classify(desc, model=None):
    pool, _ = candidates(desc)
    cands = [f"- {s}（{_leaf_info[s][0]}）: {_leaf_info[s][1]}" for s in pool]
    bd = _pairwise(pool)
    body = {"model": model or ADJUDICATOR,
            "messages": [{"role": "user", "content": PROMPT.format(
                desc=desc, cands="\n".join(cands), bounds=("\n分界记录:\n" + bd if bd else ""))}],
            "temperature": 0.1, "max_tokens": 3000}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "https://opencode.ai/zen/go/v1/chat/completions", json.dumps(body).encode(),
        {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
         "x-opencode-session": "atlas-classify", "User-Agent": "atlas-classify/1.0"}), timeout=300))
    txt = (r["choices"][0]["message"].get("content") or "").strip()
    scores = {}
    m = re.search(r"\[.*?\]", txt, re.S)
    if m:
        try:
            scores = {x["slug"]: x["score"] for x in json.loads(m.group(0))}
        except Exception:
            pass
    m2 = re.search(r"\{[^{]*\"choice\"[^}]*\}", txt, re.S)
    choice = json.loads(m2.group(0))["choice"].strip() if m2 else None
    return {"choice": choice, "scores": scores,
            "detail": [{"slug": s, "name_zh": _leaf_info[s][0]} for s in pool]}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    res = classify(" ".join(sys.argv[1:]))
    print(f"判定: {res['choice']}")
    for s, sc in sorted(res["scores"].items(), key=lambda kv: -kv[1])[:5]:
        name = _leaf_info.get(s, ("?",))[0]
        print(f"  {sc:>4} {s}（{name}）")
