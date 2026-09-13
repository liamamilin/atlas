#!/usr/bin/env python3
"""Stress test: generate 1 synthetic instance per leaf (local Ollama, free).
Output: stress_instances.jsonl (resumable via translate-style state).
"""
import json, os, re, sqlite3, time, urllib.request

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(PACK, "atlas", "stress_instances.jsonl")
STATE = os.path.join(PACK, "atlas", "stress-state.json")
OLLAMA = "http://localhost:11434/api/generate"
MODEL = "qwen3.8:27b-mlx"

PROMPT = """基于下面这个软件应用类型的定义，虚构一个真实感的产品使用场景描述（2-3句中文）。
硬性要求：
1. 场景必须以该类型定义中的核心对象和工作结构为中心（定义说管什么，场景就写用户在怎么管它）
2. 虚构产品名，不要用真实产品名
3. 不要照抄定义原文，不要出现"类型""平台""系统"这类抽象词描述产品自身
4. 场景中的用户行为要能明显对应定义里的每个核心结构

类型: {name}
定义: {dc}

只输出场景文本。"""


def load_state():
    if os.path.exists(STATE):
        return json.load(open(STATE))
    return {"done": []}


def main():
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT slug, name_zh, COALESCE(NULLIF(l0_zh,''), defining_core) FROM leaf ORDER BY order_idx").fetchall()
    con.close()
    st = load_state()
    done = set(st["done"])
    out = open(OUT, "a", encoding="utf-8")
    t0 = time.time()
    n = 0
    for i, (slug, name_zh, dc) in enumerate(rows):
        if slug in done or not dc:
            continue
        body = {"model": MODEL, "prompt": PROMPT.format(name=name_zh or slug, dc=dc[:900]),
                "stream": False, "options": {"temperature": 0.8}}
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(OLLAMA, json.dumps(body).encode(), {"Content-Type": "application/json"}), timeout=600))
            txt = r["response"].strip()
            if len(txt) < 40:
                raise ValueError("too short")
        except Exception as e:
            print(f"[{i}] {slug} GEN-FAIL: {e}", flush=True)
            continue
        out.write(json.dumps({"slug": slug, "name_zh": name_zh, "desc": txt}, ensure_ascii=False) + "\n")
        out.flush()
        st["done"].append(slug)
        n += 1
        if n % 10 == 0:
            json.dump(st, open(STATE, "w"))
            rate = n / (time.time() - t0)
            todo = len(rows) - len(done) - n
            print(f"[{len(done)+n}/{len(rows)}] {rate*3600:.0f}/h ETA {todo/max(rate,0.01)/3600:.1f}h | {slug}: {txt[:50]}", flush=True)
    json.dump(st, open(STATE, "w"))
    out.close()
    print("GEN DONE", flush=True)


if __name__ == "__main__":
    main()
