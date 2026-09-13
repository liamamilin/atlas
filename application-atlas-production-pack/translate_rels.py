#!/usr/bin/env python3
"""Batch-translate relation distinction texts per leaf (same engine split as bodies).
Usage: python3 translate_rels.py --engine local --start 1 --end 902
"""
import argparse
import json
import os
import queue
import re
import sqlite3
import threading
import time
import urllib.request

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(PACK, "atlas", "rels-zh.jsonl")
STATE = os.path.join(PACK, "atlas", "relszh-state.json")
OLLAMA = "http://localhost:11434/api/chat"
API = "https://opencode.ai/zen/go/v1/chat/completions"
KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]
PROMPT_V = "v2"

PROMPT = """把下列关系分界说明翻译成中文，只输出一个JSON对象 {{"items":[...]}}，不要输出思考过程。
规则：
- 逐条完整翻译，禁止概括或省略
- 保留产品名、公司名、英文缩写不译
- 类型英文名（如 Kanban Task Board）保留英文原样，不译

{json}"""


def call_local(prompt):
    body = {"model": "qwen3.8:27b-mlx", "messages": [{"role": "user", "content": prompt}],
            "stream": False, "think": False, "options": {"temperature": 0.1, "num_ctx": 16384}}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        OLLAMA, json.dumps(body).encode(), {"Content-Type": "application/json"}), timeout=1800))
    return r["message"]["content"]


def call_api(prompt):
    body = {"model": "mimo-v2.5", "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1, "max_tokens": 4000}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        API, json.dumps(body).encode(),
        {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
         "x-opencode-session": "atlas-rels", "User-Agent": "atlas/1.0"}), timeout=600))
    return (r["choices"][0]["message"].get("content") or "").strip()


def parse_out(txt):
    t = txt.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"\s*```\s*$", "", t)
    a, b = t.find("{"), t.rfind("}")
    if a == -1 or b == -1:
        raise ValueError("no braces")
    obj = json.loads(t[a:b + 1])
    items = obj["items"]
    if not isinstance(items, list) or not items:
        raise ValueError("bad items")
    for it in items:
        zh = it.get("zh") or it.get("distinction")
        if not it.get("to") or not zh or len(zh) < 5:
            raise ValueError("bad item")
        it["zh"] = str(zh).strip()
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["local", "api"], required=True)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=999999)
    args = ap.parse_args()

    con = sqlite3.connect(DB)
    leaves = [r[0] for r in con.execute("SELECT slug FROM leaf ORDER BY order_idx")][args.start - 1:args.end]
    rels = {}
    for s, tn, d in con.execute("SELECT from_slug, to_name, distinction FROM relation WHERE to_slug IS NOT NULL AND distinction != ''"):
        rels.setdefault(s, []).append({"to": tn, "distinction": d})
    con.close()
    todo = [(s, rels[s]) for s in leaves if s in rels]
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"done": {}}
    todo = [(s, r) for s, r in todo if st["done"].get(s) != PROMPT_V]
    log = open(os.path.join(PACK, "logs", "translate-rels.log"), "a", encoding="utf-8")
    log.write(f"\n=== {args.engine} start {time.strftime('%F %T')} todo={len(todo)} ===\n")
    log.flush()

    q = queue.Queue()
    for t in todo:
        q.put(t)
    lock = threading.Lock()
    out = open(OUT, "a", encoding="utf-8")
    t0 = time.time()
    n = [0]

    def worker():
        while True:
            try:
                slug, items = q.get_nowait()
            except queue.Empty:
                return
            r = None
            for attempt in range(3):
                try:
                    txt = call_local(PROMPT.format(json=json.dumps(items, ensure_ascii=False))) \
                        if args.engine == "local" else \
                        call_api(PROMPT.format(json=json.dumps(items, ensure_ascii=False)))
                    parsed = parse_out(txt)
                    r = {"slug": slug, "items": parsed, "engine": args.engine}
                    break
                except Exception:
                    time.sleep(3 * (attempt + 1))
            with lock:
                out.write(json.dumps(r or {"slug": slug, "error": True}, ensure_ascii=False) + "\n")
                out.flush()
                st["done"][slug] = PROMPT_V if r else "FAIL-" + PROMPT_V
                n[0] += 1
                if n[0] % 20 == 0:
                    json.dump(st, open(STATE, "w"))
                    rate = n[0] / (time.time() - t0)
                    log.write(f"[{n[0]}/{len(todo)}] {rate*60:.0f}/min ETA {(len(todo)-n[0])/max(rate,0.001)/60:.0f}min\n")
                    log.flush()
            q.task_done()

    wnum = 3 if args.engine == "local" else 12
    ts = [threading.Thread(target=worker, daemon=True) for _ in range(wnum)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    json.dump(st, open(STATE, "w"))
    out.close()
    log.write(f"=== {args.engine} DONE {n[0]} in {(time.time()-t0)/60:.1f}min ===\n")
    log.close()
    print("DONE", n[0])


if __name__ == "__main__":
    main()
