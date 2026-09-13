#!/usr/bin/env python3
"""Analyze stress-test round-trip results -> boundary-weak leaf report."""
import json
import os
import sqlite3
from collections import Counter, defaultdict

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
RES = os.path.join(PACK, "atlas", "stress_results.jsonl")
REPORT = os.path.join(PACK, "logs", "stress-report.md")

con = sqlite3.connect(DB)
sections = dict(con.execute("SELECT slug, section_name FROM leaf").fetchall())
l0s = dict(con.execute("SELECT slug, l0_zh FROM leaf").fetchall())
names = dict(con.execute("SELECT slug, name_zh FROM leaf").fetchall())
neighbors = defaultdict(set)
for a, b in con.execute("SELECT from_slug, to_slug FROM relation"):
    neighbors[a].add(b)
    neighbors[b].add(a)
con.close()

errors = []
total = 0
for line in open(RES, encoding="utf-8"):
    r = json.loads(line)
    total += 1
    if not r["correct"]:
        errors.append(r)

# 1. confusion pairs
pairs = Counter((e["slug"], e["predicted"].split()[0]) for e in errors if not e["predicted"].startswith("__ERROR__"))
# 2. error type: boundary confusion vs way-off
boundary, wayoff, err = [], [], []
for e in errors:
    pred = e["predicted"].split()[0]
    if pred.startswith("__ERROR__"):
        err.append(e)
    elif pred in neighbors[e["slug"]]:
        boundary.append(e)
    else:
        wayoff.append(e)
# 3. per-section accuracy
sec_tot = Counter(sections.get(r["slug"], "?") for r in map(json.loads, open(RES, encoding="utf-8")))
sec_err = Counter(sections.get(e["slug"], "?") for e in errors)
# 4. worst leaves (leaf-level failure rate)
leaf_err = Counter(e["slug"] for e in errors)

rep = ["# 合成压力测试报告 (U3b)", "",
       f"- 样本: {total} (每叶 1 个合成场景, mimo-v2.5 生成 → qwen3.8-flash 回分类)",
       f"- 整体往返准确率: **{1-len(errors)/total:.1%}** (闸门时盲测为 94.2%, 差距=全谱系难度 vs 简单盲测)",
       f"- 错误 {len(errors)}: 边界混淆 {len(boundary)} | 完全偏移 {len(wayoff)} | 调用异常 {len(err)}", ""]

rep.append("## 边界混淆 TOP 25 (真类型 → 被误判为邻居类型, 语料需强化分界)")
rep.append("| 真类型 | 误判为 | 次数 | 已有区分文本? |")
rep.append("|---|---|---|---|")
for (a, b), n in pairs.most_common(25):
    rel = con_q = ""
    con = sqlite3.connect(DB)
    row = con.execute("SELECT distinction FROM relation WHERE from_slug=? AND to_slug=?", (a, b)).fetchone()
    con.close()
    rep.append(f"| {a} | {b} | {n} | {'有' if row and row[0] else '**缺**'} |")

rep.append("")
rep.append("## 完全偏移 TOP 20 (误判为非邻居, 检索池召回问题或定义误导)")
rep.append("| 真类型 | 误判为 | 次数 |")
rep.append("|---|---|---|")
for (a, b), n in [p for p in pairs.most_common(60) if p[0][1] not in neighbors[p[0][0]]][:20]:
    rep.append(f"| {a} | {b} | {n} |")

rep.append("")
rep.append("## 各域准确率 (低于 55% 的域)")
rows = [(s, 1 - sec_err.get(s, 0) / t, t) for s, t in sec_tot.items() if t >= 5]
rows.sort()
for s, acc, t in rows:
    if acc < 0.55:
        rep.append(f"- {s}: **{acc:.0%}** ({t} 叶)")

rep.append("")
rep.append("## 高频失败叶子 TOP 20 (语料质量改进优先级)")
for s, n in leaf_err.most_common(20):
    pred_top = Counter(e["predicted"].split()[0] for e in errors if e["slug"] == s).most_common(1)[0][0]
    rep.append(f"- **{s}** ({names.get(s,'')}) 失败 {n} 次 → 常被吸到 `{pred_top}`")

open(REPORT, "w").write("\n".join(rep))
print("\n".join(rep[:40]))
print(f"\n... full report: {REPORT}")
