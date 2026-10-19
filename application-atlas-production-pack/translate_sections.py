#!/usr/bin/env python3
"""Translate 113 section names to Chinese via mimo-v2.5 -> atlas/section-zh.json"""
import json
import os
import re
import sqlite3
import urllib.request

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_model

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(PACK, "atlas", "section-zh.json")

if os.path.exists(OUT):
    print("exists, skip")
else:
    con = sqlite3.connect(DB)
    secs = con.execute("SELECT id, name, path FROM section ORDER BY id").fetchall()
    con.close()
    payload = [{"id": s[0], "name": s[1], "path": s[2]} for s in secs]
    prompt = ("把下列分类树节点的 name 翻译成中文（path 仅作参考，不要输出）。"
              "输出JSON数组 [{\"id\":..., \"name_zh\":...}]，覆盖全部节点，不要遗漏。"
              "命名用软件行业通用中文叫法。保留缩写（CRM/ERP/HR）。\n" + json.dumps(payload, ensure_ascii=False))
    txt = atlas_model.complete_text(
        [{"role": "user", "content": prompt}],
        role="translate", temperature=0.1, max_tokens=4000, timeout=600)
    if txt.startswith("```"):
        txt = re.sub(r"^```[a-zA-Z]*\s*", "", txt)
        txt = re.sub(r"\s*```\s*$", "", txt)
    obj = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
    assert len(obj) >= 113, f"only {len(obj)} sections"
    json.dump(obj, open(OUT, "w"), ensure_ascii=False)
    print("sections translated:", len(obj))
