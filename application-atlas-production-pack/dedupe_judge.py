#!/usr/bin/env python3
"""LLM dedup adjudication for draft leaves: same / variant / new + evidence.

  python3 dedupe_judge.py <slug>          # uses draft desc + top-10 vector neighbors
Returns dict {verdict, best, reason, section_hint}.
"""
import json
import os
import re
import sys
import urllib.request

PACK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PACK)
import classify as C
from draft_new import DRAFTS
from leaf_lint import parse_front
from drafts_api import draft_path

KEY = C.KEY
MODEL = os.environ.get("ATLAS_DEDUP_MODEL", "mimo-v2.5")

PROMPT = """你是软件类型语料库的查重裁决者。判断「新提案」与已有类型的关系。

新提案:
- 名称: {name}（{name_zh}）
- 主张: {desc}
- 定义核心摘录: {dc}

候选已有类型（含类型 id 与定义核心）:
{cands}

相邻分界记录:
{bounds}

裁决规则:
- same: 提案描述的产品类别与某已有类型本质相同（同一物、换皮、改名）
- variant: 提案是该已有类型的一个真子变体/子形态，不足以独立成叶
- new: 提案有独立的定义核心，现有候选都不覆盖

只输出 JSON: {{"verdict":"same|variant|new","best":"slug或null","reason":"≤80字","section_hint":"NN.MM或null"}}
section_hint 用候选类型所在子域编号；仅在 verdict=new 时给出。"""


def dc_excerpt(body, n=900):
    m = re.search(r"###\s+.*defining.*?\n(.*?)(?=\n###|\Z)", body, re.S | re.I)
    t = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return t[:n] or re.sub(r"\s+", " ", body[:n])


def judge(slug):
    front, body = parse_front(open(os.path.join(DRAFTS, slug + ".md"), encoding="utf-8").read())
    desc = front.get("desc", "")
    pool, sims = C.candidates(desc + "\n" + body[:400], k=10)
    cands = []
    for s in pool:
        nz, txt = C._leaf_info.get(s) or ("", "")
        cands.append(f"- {s} [子域 {con_sec(s)}]（{nz}）: {txt[:160]}")
    bd = C._pairwise(pool)
    prompt = PROMPT.format(
        name=front.get("name", slug), name_zh=front.get("name_zh", ""), desc=desc,
        dc=dc_excerpt(body), cands="\n".join(cands), bounds=("\n" + bd if bd else "（无）"))
    body_msg = {"model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1, "max_tokens": 3000}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "https://opencode.ai/zen/go/v1/chat/completions", json.dumps(body_msg).encode(),
        {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
         "x-opencode-session": "atlas-dedupe", "User-Agent": "atlas-dedupe/1.0"}), timeout=300))
    msg = r["choices"][0]["message"]
    txt = (msg.get("content") or "").strip()
    if not txt and msg.get("reasoning"):
        txt = str(msg["reasoning"]).strip()
    m = re.search(r"\{[^{]*verdict[^}]*\}", txt, re.S)
    out = json.loads(m.group(0)) if m else {"verdict": "unknown", "best": None,
                                            "reason": txt[:200], "section_hint": None}
    out["pool"] = pool[:5]
    return out


_con = None
def con_sec(slug):
    global _con
    if _con is None:
        import sqlite3
        _con = sqlite3.connect(C.DB, check_same_thread=False)
    row = _con.execute("SELECT section_id FROM leaf WHERE slug=?", (slug,)).fetchone()
    return row[0] if row else ""


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    print(json.dumps(judge(sys.argv[1]), ensure_ascii=False, indent=2))
