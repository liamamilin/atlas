#!/usr/bin/env python3
"""Stress test generation via mimo-v2.5 direct API (12 concurrent, resumable).
Appends to atlas/stress_instances.jsonl, skipping slugs already present."""
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
OUT = os.path.join(PACK, "atlas", "stress_instances.jsonl")
STATE = os.path.join(PACK, "atlas", "stress-state-api.json")
LOG = os.path.join(PACK, "logs", "stress-gen.log")
API = "https://opencode.ai/zen/go/v1/chat/completions"
MODEL = "mimo-v2.5"
WORKERS = 12

KEY = json.load(open(os.path.expanduser("~/.local/share/opencode/auth.json")))["opencode-go"]["key"]

PROMPT = """基于下面这个软件应用类型的定义，虚构一个真实感的产品使用场景描述（2-3句中文）。
硬性要求：
1. 场景必须以该类型定义中的核心对象和工作结构为中心（定义说管什么，场景就写用户在怎么管它）
2. 虚构产品名，不要用真实产品名
3. 不要照抄定义原文，不要出现"类型""平台""系统"这类抽象词描述产品自身
4. 场景中的用户行为要能明显对应定义里的每个核心结构

类型: {name}
定义: {dc}

只输出场景文本，不要输出思考过程。"""


def api_gen(name, dc, retries=2):
    body = {"model": MODEL,
            "messages": [{"role": "user", "content": PROMPT.format(name=name, dc=dc[:900])}],
            "temperature": 0.8, "max_tokens": 1200}
    headers = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json",
               "x-opencode-session": "atlas-stress",
               "User-Agent": "atlas-stress/1.0 (curl-compatible)"}
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(API, json.dumps(body).encode(), headers)
            r = json.load(urllib.request.urlopen(req, timeout=240))
            txt = (r["choices"][0]["message"].get("content") or "").strip()
            m = re.search(r"(?:</think>\s*)?(.+)", txt, re.S)
            txt = (m.group(1) if m else txt).strip()
            if len(txt) >= 40:
                return txt
        except Exception:
            time.sleep(2)
    return None


def main():
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT slug, name_zh, COALESCE(NULLIF(l0_zh,''), defining_core) FROM leaf ORDER BY order_idx").fetchall()
    con.close()
    have = set()
    if os.path.exists(OUT):
        for line in open(OUT, encoding="utf-8"):
            try:
                have.add(json.loads(line)["slug"])
            except Exception:
                pass
    todo = [(s, n, d) for s, n, d in rows if s not in have and d]
    log = open(LOG, "a", encoding="utf-8")
    log.write(f"\n=== API gen start {time.strftime('%F %T')}, todo={len(todo)} ===\n")
    q = queue.Queue()
    for t in todo:
        q.put(t)
    out_lock = threading.Lock()
    out = open(OUT, "a", encoding="utf-8")
    t0 = time.time()
    done = [0]

    def worker():
        while True:
            try:
                slug, name_zh, dc = q.get_nowait()
            except queue.Empty:
                return
            txt = api_gen(name_zh or slug, dc)
            if txt:
                with out_lock:
                    out.write(json.dumps({"slug": slug, "name_zh": name_zh, "desc": txt}, ensure_ascii=False) + "\n")
                    out.flush()
                    done[0] += 1
                    if done[0] % 50 == 0:
                        rate = done[0] / (time.time() - t0)
                        log.write(f"[{done[0]}/{len(todo)}] {rate*60:.0f}/min ETA {len(todo)-done[0]:.0f} left\n")
                        log.flush()
            else:
                with out_lock:
                    log.write(f"FAIL {slug}\n")
                    log.flush()
            q.task_done()

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(WORKERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    out.close()
    log.write(f"GEN DONE {done[0]}/{len(todo)} in {(time.time()-t0)/60:.1f}min\n")
    log.close()


if __name__ == "__main__":
    main()
