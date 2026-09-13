#!/usr/bin/env python3
"""Propose subsection layers for DIRECTORY.md domains 06-29.
Pipeline: bge-m3 embeddings (sqlite embedding table) -> KMeans per domain
-> LLM names & re-assigns subsections (en+zh) -> MECE validation.
Output: atlas/subsections-proposal.json
"""
import json, os, re, sqlite3, struct, time, urllib.request
import numpy as np
from sklearn.cluster import KMeans

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(PACK, "atlas", "subsections-proposal.json")
API = "https://opencode.ai/zen/go/v1/chat/completions"
KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]

con = sqlite3.connect(DB)
leaves = {}
for slug, name, name_zh, sec in con.execute("SELECT slug, name, name_zh, section_id FROM leaf"):
    leaves[slug] = {"name": name, "name_zh": name_zh, "sec": sec}
vecs = {s: np.frombuffer(v, dtype=np.float32) for s, v in
        con.execute("SELECT slug, vec FROM embedding")}

domains = {}
for slug, lf in leaves.items():
    domains.setdefault(lf["sec"].split(".")[0], []).append(slug)

PROMPT = """你是应用软件分类专家。下面是"{domain}"领域下的叶子类型清单，已按语义相似度预分组（组号仅为参考）。
任务：为该领域设计 {klo}-{khi} 个子节（subsection），把全部叶子归入子节。
要求：
- 子节名先给英文、再给中文（如 "SEO & Search" / "SEO 与搜索"），命名风格与示例一致：简短、行业通用、互斥
- 每个叶子必须且只能归入一个子节，叶子英文名必须逐字复制清单中的写法
- 参考分组可以合并或重划，但不要凭空发明清单外的叶子
- 只输出 JSON 对象：{{"subsections":[{{"name":"英文名","name_zh":"中文名","leaves":["叶子英文名",...]}}]}}
- 输出前自查：所有叶子恰好出现一次、无遗漏无重复

{groups}
"""

def call_api(prompt, tries=3):
    body = {"model": "mimo-v2.5", "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2, "max_tokens": 8000}
    headers = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
               "x-opencode-session": "atlas-sections", "User-Agent": "atlas-sections/1.0"}
    for i in range(tries):
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(
                API, json.dumps(body).encode(), headers), timeout=600))
            return (r["choices"][0]["message"].get("content") or "").strip()
        except Exception as e:
            print(f"    api retry {i+1}: {e}")
            time.sleep(5)
    raise RuntimeError("api failed")

def parse_json(txt):
    t = re.sub(r"^```[a-zA-Z]*\s*|\s*```\s*$", "", txt.strip())
    a, b = t.find("{"), t.rfind("}")
    return json.loads(t[a:b+1])

proposal = {}
for top in sorted(domains):
    if top <= "05":
        continue
    slugs = domains[top]
    dom_name = con.execute("SELECT name FROM section WHERE id=?", (top,)).fetchone()[0]
    k = max(4, min(8, round(len(slugs) ** 0.5)))
    X = np.stack([vecs[s] for s in slugs])
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)
    names = [leaves[s]["name"] for s in slugs]
    groups = {}
    for s, c in zip(slugs, km.labels_):
        groups.setdefault(int(c), []).append(leaves[s])
    gtxt = "\n".join(f"组{i+1}: " + " | ".join(
        f"{g['name']}({g['name_zh']})" for g in gs) for i, gs in sorted(groups.items()))
    print(f"{top} {dom_name}: {len(slugs)} 叶, 预聚类 {k} 组")
    ok = None
    for attempt in range(3):
        try:
            out = call_api(PROMPT.format(domain=dom_name, klo=3, khi=k, groups=gtxt))
            obj = parse_json(out)
            subs = obj["subsections"]
            covered = [l for s in subs for l in s["leaves"]]
            if sorted(covered) != sorted(names):
                missing = set(names) - set(covered)
                extra = set(covered) - set(names)
                raise ValueError(f"MECE fail: missing={list(missing)[:3]} extra={list(extra)[:3]}")
            if not (3 <= len(subs) <= 10):
                raise ValueError(f"bad sub count {len(subs)}")
            ok = subs
            break
        except Exception as e:
            print(f"    attempt {attempt+1} fail: {e}")
    if ok:
        proposal[top] = {"domain": dom_name, "subsections": ok}
        print(f"    -> {len(ok)} 子节: " + ", ".join(s["name_zh"] for s in ok))
    else:
        print(f"    !! {top} 三次尝试均失败, 跳过")

json.dump(proposal, open(OUT, "w"), ensure_ascii=False, indent=1)
print(f"\nsaved {OUT}: {len(proposal)} domains")
