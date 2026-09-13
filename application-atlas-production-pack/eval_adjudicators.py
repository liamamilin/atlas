#!/usr/bin/env python3
"""Evaluate cheap adjudicator models on the classification pilot (graph-expanded pool)."""
import json, re, sqlite3, urllib.request, numpy as np, concurrent.futures as cf, time, sys

KEY = json.load(open("/Users/milin/.local/share/opencode/auth.json"))["opencode-go"]["key"]
con = sqlite3.connect("atlas/atlas.sqlite")
rows = con.execute("SELECT slug, vec FROM embedding").fetchall()
M = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
Mn = M / (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)
slugs = [r[0] for r in rows]
s2i = {s: i for i, s in enumerate(slugs)}
leaf_info = {r[0]: (r[1], (r[2] or r[3] or "")[:170]) for r in
             con.execute("SELECT slug, name_zh, l0_zh, overview FROM leaf")}
nb = {}
for a, b in con.execute("SELECT from_slug, to_slug FROM relation WHERE to_slug IS NOT NULL"):
    nb.setdefault(a, set()).add(b)
    nb.setdefault(b, set()).add(a)
rels = {}
for a, b, tn, d in con.execute("SELECT from_slug, to_slug, to_name, distinction FROM relation WHERE to_slug IS NOT NULL AND distinction != ''"):
    rels.setdefault((a, b), (tn, d))
con.close()


def emb(texts):
    b = json.dumps({"model": "bge-m3", "input": texts}).encode()
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://localhost:11434/api/embed", b, {"Content-Type": "application/json"}), timeout=600))
    return [np.array(e, dtype=np.float32) for e in r["embeddings"]]


def pairwise(sl):
    lines = []
    for i, a in enumerate(sl):
        for b in sl[i + 1:]:
            r = rels.get((a, b)) or rels.get((b, a))
            if r:
                lines.append(f"{r[0]} vs 相邻: {r[1][:140]}")
    return "\n".join(lines[:8])


PROMPT = """你是软件类型分类器。对下列每个候选类型，独立打 0-10 分表示与产品描述的匹配度（互不比较，仅看各自定义）。
产品描述: {desc}
候选:
{cands}
{bounds}
输出 JSON 数组: [{{"slug":"...","score":0-10,"brief":"≤12字"}}] 然后输出 {{"choice":"最高分slug或none"}}。"""


def pool_for(q):
    sims = Mn @ q
    order = np.argsort(-sims)
    top10 = [slugs[i] for i in order[:10]]
    pool, seen = list(top10), set(top10)
    nbs = []
    for s in top10[:5]:
        for n in nb.get(s, set()):
            if n not in seen:
                nbs.append((sims[s2i[n]], n))
    nbs.sort(reverse=True)
    for _, n in nbs[:6]:
        pool.append(n)
        seen.add(n)
    return pool[:16]


def run(model, items, Q):
    def one(args):
        it, q = args
        pool = pool_for(q)
        cands = [f"- {s}（{leaf_info[s][0]}）: {leaf_info[s][1]}" for s in pool]
        bd = pairwise(pool)
        body = {"model": model, "messages": [{"role": "user", "content": PROMPT.format(
            desc=it["desc"], cands="\n".join(cands), bounds=("\n分界记录:\n" + bd if bd else ""))}],
            "temperature": 0.1, "max_tokens": 3000}
        for attempt in range(2):
            try:
                r = json.load(urllib.request.urlopen(urllib.request.Request(
                    "https://opencode.ai/zen/go/v1/chat/completions", json.dumps(body).encode(),
                    {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
                     "x-opencode-session": "atlas-eval", "User-Agent": "atlas-pilot/1.0"}), timeout=300))
                txt = (r["choices"][0]["message"].get("content") or "").strip()
                m = re.search(r"\{[^{]*\"choice\"[^}]*\}", txt, re.S)
                if m:
                    return {"name": it["name"], "expect": it["expect"], "choice": json.loads(m.group(0))["choice"].strip()}
            except Exception:
                time.sleep(2)
        return {"name": it["name"], "expect": it["expect"], "choice": "err"}

    t0 = time.time()
    with cf.ThreadPoolExecutor(8) as ex:
        out = list(ex.map(one, list(zip(items, Q))))
    hits = sum(o["choice"] == o["expect"] for o in out)
    real = [o for o in out if not o["name"].startswith("synthetic")]
    syn = [o for o in out if o["name"].startswith("synthetic")]
    print(f"{model:24s}: {hits}/{len(out)} = {hits/len(out):.1%} | real {sum(o['choice']==o['expect'] for o in real)}/21 | syn {sum(o['choice']==o['expect'] for o in syn)}/31 | {time.time()-t0:.0f}s")
    return out


if __name__ == "__main__":
    items = json.load(open("pilot_clean.json")) + json.load(open("pilot_synthetic.json"))
    Q = np.stack(emb([it["desc"] for it in items]))
    Q /= (np.linalg.norm(Q, axis=1, keepdims=True) + 1e-9)
    results = {}
    for model in sys.argv[1:] or ["glm-5.3-flash", "qwen3.8-flash", "deepseek-v4-flash"]:
        results[model] = run(model, items, Q)
    json.dump(results, open("pilot_results_cheap.json", "w"), ensure_ascii=False, indent=1)
    print("saved pilot_results_cheap.json")
