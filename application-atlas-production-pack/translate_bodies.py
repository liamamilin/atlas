#!/usr/bin/env python3
"""Batch-translate leaf body fields to Chinese. Two engines: local (Ollama 27B, think off)
and api (mimo-v2.5). Same output format, shared dedupe state, resumable.
Usage:
  python3 translate_bodies.py --engine local --start 1 --end 902
  python3 translate_bodies.py --engine api   --start 903 --end 1804
  python3 translate_bodies.py --engine api --sample 5
"""
import argparse
import json
import os
import queue
import re
import sqlite3
import sys
import threading
import time
import urllib.request

from atlas_runtime import PACK as DATA_PACK, api_key, corpus_lock
PACK = str(DATA_PACK)
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(PACK, "atlas", "body-zh.jsonl")
STATE = os.path.join(PACK, "atlas", "bodyzh-state.json")
LOG = os.path.join(PACK, "logs", "translate-bodies.log")
PROMPT_V = "v2"
OLLAMA = "http://localhost:11434/api/chat"
API = "https://opencode.ai/zen/go/v1/chat/completions"

PROMPT = """把下列软件类型档案翻译成中文，只输出一个JSON对象（键与输入完全相同），不要输出思考过程。
规则：
- 逐段完整翻译，禁止概括、缩写或省略任何段落、句子或列表项；每个字段译完后核对一遍无遗漏
- 译文长度须与原文大致相当（中文字符数不低于原文的60%）
- 保留产品名、公司名、专有名词、英文缩写（CRM/SaaS/API/EDR 等）不译
- 保留 markdown 结构（代码块围栏、表格、列表符号、标题层级），只翻译其中的自然语言文字
- "Type"译为"类型"；核心结构术语翻译保持全文一致

{json}"""


def load_state():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE))
        except Exception:
            pass
    return {"done": {}}


def save_state(st):
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(st, f)
    os.replace(tmp, STATE)


def parse_out(txt):
    t = txt.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"\s*```\s*$", "", t)
    a, b = t.find("{"), t.rfind("}")
    if a == -1 or b == -1:
        raise ValueError("no braces")
    obj = json.loads(t[a:b + 1])
    if not obj.get("overview") or len(str(obj["overview"])) < 20:
        raise ValueError("missing overview")
    return {k: str(obj[k]).strip() for k in ("overview", "how", "rules", "variants", "products")}


def call_local(prompt):
    body = {"model": "qwen3.8:27b-mlx", "messages": [{"role": "user", "content": prompt}],
            "stream": False, "think": False, "options": {"temperature": 0.1, "num_ctx": 16384}}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        OLLAMA, json.dumps(body).encode(), {"Content-Type": "application/json"}), timeout=1800))
    return r["message"]["content"]


def call_api(prompt):
    body = {"model": "mimo-v2.5", "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1, "max_tokens": 6000}
    headers = {"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json",
               "x-opencode-session": "atlas-translate-body",
               "User-Agent": "atlas-translate/1.0 (curl-compatible)"}
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        API, json.dumps(body).encode(), headers), timeout=600))
    return (r["choices"][0]["message"].get("content") or "").strip()


def translate_one(slug, fields, engine, tries):
    payload = json.dumps({
        "overview": fields["overview"][:4000], "how": (fields["how"] or "")[:2500],
        "rules": (fields["rules"] or "")[:1800], "variants": (fields["variants"] or "")[:2500],
        "products": (fields["products"] or "")[:1800],
    }, ensure_ascii=False)
    prompt = PROMPT.format(json=payload)
    for attempt in range(tries):
        try:
            txt = call_local(prompt) if engine == "local" else call_api(prompt)
            zh = parse_out(txt)
            zh["slug"] = slug
            zh["engine"] = engine
            return zh
        except Exception as e:
            if attempt == tries - 1:
                return {"slug": slug, "error": str(e)[:120], "engine": engine}
            time.sleep(3 * (attempt + 1))
    return None


def _main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["local", "api"], required=True)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=999999)
    ap.add_argument("--sample", type=int, default=0, help="only first N of range")
    ap.add_argument("--workers", type=int, default=0)
    args = ap.parse_args()

    con = sqlite3.connect(DB)
    rows = con.execute(
        "SELECT slug, overview, how_it_works, rules, variants, products_md FROM leaf ORDER BY order_idx").fetchall()
    con.close()
    rows = [(r[0], {"overview": r[1], "how": r[2], "rules": r[3], "variants": r[4], "products": r[5]})
            for r in rows]
    rows = rows[args.start - 1:args.end]
    if args.sample:
        rows = rows[:args.sample]

    st = load_state()
    todo = [(s, f) for s, f in rows if st["done"].get(s) != PROMPT_V]
    log = open(os.path.join(PACK, "logs", "translate-bodies.log"), "a", encoding="utf-8")
    log.write(f"\n=== {args.engine} start {time.strftime('%F %T')} todo={len(todo)} prompt={PROMPT_V} ===\n")
    log.flush()

    q = queue.Queue()
    for r in todo:
        q.put(r)
    lock = threading.Lock()
    out = open(OUT, "a", encoding="utf-8")
    t0 = time.time()
    n = [0]

    def worker():
        while True:
            try:
                slug, fields = q.get_nowait()
            except queue.Empty:
                return
            r = translate_one(slug, fields, args.engine, tries=3)
            with lock:
                out.write(json.dumps(r, ensure_ascii=False) + "\n")
                out.flush()
                st["done"][slug] = PROMPT_V if "error" not in r else "FAIL-" + PROMPT_V
                n[0] += 1
                if n[0] % 10 == 0:
                    save_state(st)
                    rate = n[0] / (time.time() - t0)
                    eta = (len(todo) - n[0]) / max(rate, 0.001) / 3600
                    errs = sum(1 for v in st["done"].values() if str(v).startswith("FAIL"))
                    log.write(f"[{n[0]}/{len(todo)}] {rate*3600:.0f}/h ETA {eta:.1f}h fails={errs}\n")
                    log.flush()
            q.task_done()

    wnum = args.workers or (3 if args.engine == "local" else 12)
    ts = [threading.Thread(target=worker, daemon=True) for _ in range(wnum)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    save_state(st)
    out.close()
    log.write(f"=== {args.engine} DONE {n[0]} in {(time.time()-t0)/60:.1f}min ===\n")
    log.close()
    print("DONE", n[0])


def main():
    with corpus_lock(PACK):
        _main()


if __name__ == "__main__":
    main()
