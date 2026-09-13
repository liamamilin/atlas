#!/usr/bin/env python3
"""Generate synthetic blind-test product pitches from randomly sampled leaves."""
import json
import os
import random
import re
import sqlite3
import urllib.request

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
API = "https://opencode.ai/zen/go/v1/chat/completions"
KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]
N = 40

PROMPT = """基于下面这个软件应用类型的定义，虚构一个真实感的产品使用场景描述（2-3句中文）。
要求：
- 虚构一个产品名（不要用真实存在的产品名）
- 描述这个产品的目标用户和他们要做的事、关键工作方式
- 体现类型的核心结构，但不要照抄定义原文，不要使用定义中的分类学术语（如"记录单元""类型"等）
- 不要列举产品名

类型定义: {dc}

只输出场景描述文本本身，不要 JSON，不要解释。"""


def main():
    random.seed(42)
    con = sqlite3.connect(DB)
    rows = con.execute("""SELECT slug, name_zh, defining_core, l0_zh FROM leaf
                          WHERE defining_core != '' ORDER BY RANDOM() LIMIT {n}""".format(n=N * 2)).fetchall()
    # stratify: max 1 per section
    seen_sec, picked = set(), []
    for slug, name_zh, dc, l0 in rows:
        sec = con.execute("SELECT section_id FROM leaf WHERE slug=?", (slug,)).fetchone()[0]
        if sec in seen_sec:
            continue
        seen_sec.add(sec)
        picked.append((slug, name_zh, dc, l0))
        if len(picked) >= N:
            break
    print(f"sampled {len(picked)} leaves across {len(seen_sec)} sections")

    results = []
    for i, (slug, name_zh, dc, l0) in enumerate(picked):
        body = {"model": "mimo-v2.5",
                "messages": [{"role": "user", "content": PROMPT.format(dc=(l0 or dc)[:900])}],
                "temperature": 0.8, "max_tokens": 800}
        req = urllib.request.Request(API, json.dumps(body).encode(),
                                     {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
                                      "x-opencode-session": "atlas-pilot", "User-Agent": "atlas-pilot/1.0"})
        r = json.load(urllib.request.urlopen(req, timeout=240))
        txt = (r["choices"][0]["message"].get("content") or "").strip()
        txt = re.sub(r"^```.*?\n|```$", "", txt, flags=re.S).strip()
        results.append({"name": f"synthetic-{i+1:02d}", "expect": slug, "leaf_zh": name_zh, "desc": txt})
        print(f"[{i+1}/{N}] {slug} ({name_zh}): {txt[:60]}...", flush=True)
    con.close()
    with open(os.path.join(PACK, "pilot_synthetic.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    print("saved pilot_synthetic.json")


if __name__ == "__main__":
    main()
