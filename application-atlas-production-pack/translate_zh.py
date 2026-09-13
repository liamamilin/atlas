#!/usr/bin/env python3
"""Batch-translate leaf names/aliases/defining-cores into Chinese via direct API.
Concurrent workers + checkpoint state. Results -> atlas/translations.jsonl
"""
import json
import os
import queue
import re
import sqlite3
import threading
import time
import urllib.request

from atlas_runtime import PACK as DATA_PACK, api_key, corpus_lock
PACK = str(DATA_PACK)
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
STATE = os.path.join(PACK, "atlas", "translate-state.json")
OUTL = os.path.join(PACK, "atlas", "translations.jsonl")
LOG = os.path.join(PACK, "logs", "translate.log")
API = "https://opencode.ai/zen/go/v1/chat/completions"
MODEL = "mimo-v2.5"
WORKERS = 12


PROMPT = """你是软件分类学翻译。将以下软件应用类型的信息翻译成中文，只输出JSON，不要输出思考过程：
{{"name_zh": "类型名的中文市场通用叫法，保留英文缩写如CRM", "aliases_zh": ["中文市场别名1", "别名2"], "l0_zh": "defining core 的忠实中文翻译，保留精确性与结构"}}

类型英文名: {name}
Defining core: {dc}"""


def load_state():
    if os.path.exists(STATE):
        with open(STATE) as f:
            return json.load(f)
    return {"done": {}, "failed": []}


def save_state(st):
    with open(STATE, "w") as f:
        json.dump(st, f, ensure_ascii=False)


def translate(name, dc, retries=2):
    body = {"model": MODEL,
            "messages": [{"role": "user", "content": PROMPT.format(name=name, dc=dc)}],
            "temperature": 0.1, "max_tokens": 2500}
    headers = {"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json",
               "x-opencode-session": "atlas-translate",
               "User-Agent": "atlas-translate/1.0 (curl-compatible)"}
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(API, json.dumps(body).encode(), headers)
            r = json.load(urllib.request.urlopen(req, timeout=240))
            txt = (r["choices"][0]["message"].get("content") or "").strip()
            m = re.search(r"\{.*\}", txt, re.S)
            if m:
                res = json.loads(m.group(0))
                if res.get("name_zh"):
                    return res
        except Exception as e:
            if attempt < retries:
                time.sleep(3 * (attempt + 1))
            else:
                raise
    return None


def _main():
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT slug, name, defining_core, overview FROM leaf ORDER BY order_idx").fetchall()
    con.close()
    st = load_state()
    todo = [(s, n, dc, ov) for s, n, dc, ov in rows if s not in st["done"]]
    print(f"total {len(rows)}, done {len(st['done'])}, todo {len(todo)}", flush=True)

    lock = threading.Lock()
    out_f = open(OUTL, "a", encoding="utf-8")
    q = queue.Queue()
    for t in todo:
        q.put(t)
    t_start = time.time()
    done_ct = [0]

    def worker():
        while True:
            try:
                slug, name, dc, ov = q.get_nowait()
            except queue.Empty:
                return
            src = (dc or "").strip()
            if len(src) < 60 or src.count("└") + src.count("├") + src.count("│") > len(src) / 4:
                paras = [p.strip() for p in (dc or ov or "").split("\n\n")
                         if len(p.strip()) > 100 and p.count("└") == 0]
                src = paras[0] if paras else (ov or "")[:600]
            try:
                res = translate(name, src[:1400])
                ok = bool(res)
            except Exception:
                res, ok = None, False
            with lock:
                if ok:
                    rec = {"slug": slug, "name_zh": res.get("name_zh", "")[:60],
                           "aliases_zh": (res.get("aliases_zh") or [])[:4],
                           "l0_zh": res.get("l0_zh", "")}
                    st["done"][slug] = rec
                    out_f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    out_f.flush()
                else:
                    st["failed"].append(slug)
                done_ct[0] += 1
                n = done_ct[0]
                if n % 5 == 0:
                    save_state(st)
                    rate = n / max(time.time() - t_start, 1)
                    eta = (len(todo) - n) / max(rate, 0.01) / 60
                    print(f"[{n}/{len(todo)}] {slug}: {res.get('name_zh','FAILED') if ok else 'FAILED'} | rate {rate*60:.0f}/min ETA {eta:.0f}min", flush=True)
                if n % 50 == 0:
                    save_state(st)

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(WORKERS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    save_state(st)
    out_f.close()
    print(f"ALL DONE. ok {len(st['done'])}, failed {len(st['failed'])}", flush=True)


def main():
    with corpus_lock(PACK):
        _main()


if __name__ == "__main__":
    main()
