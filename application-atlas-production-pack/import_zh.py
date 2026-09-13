#!/usr/bin/env python3
"""Import zh translations (body-zh.jsonl, rels-zh.jsonl, section-zh.json) into atlas.sqlite.
Idempotent: drops & recreates tables. Rerun after batches complete."""
import json
import os
import sqlite3

PACK = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
con = sqlite3.connect(DB)
cols = [r[1] for r in con.execute("PRAGMA table_info(section)")]
if "name_zh" not in cols:
    con.execute("ALTER TABLE section ADD COLUMN name_zh TEXT")
con.execute("DROP TABLE IF EXISTS leaf_zh_body")
con.execute("DROP TABLE IF EXISTS rel_zh")
con.execute("""CREATE TABLE leaf_zh_body (slug TEXT PRIMARY KEY, overview_zh TEXT, how_zh TEXT,
               rules_zh TEXT, variants_zh TEXT, products_zh TEXT, engine TEXT)""")
con.execute("""CREATE TABLE rel_zh (from_slug TEXT, to_name TEXT, distinction_zh TEXT, PRIMARY KEY(from_slug, to_name))""")

n_ok = n_err = 0
for line in open(os.path.join(PACK, "atlas", "body-zh.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    if "error" in r:
        n_err += 1
        continue
    con.execute("INSERT OR REPLACE INTO leaf_zh_body VALUES (?,?,?,?,?,?,?)",
                (r["slug"], r["overview"], r["how"], r["rules"], r["variants"], r["products"], r["engine"]))
    n_ok += 1

n_rel = 0
rels_path = os.path.join(PACK, "atlas", "rels-zh.jsonl")
if os.path.exists(rels_path):
    for line in open(rels_path, encoding="utf-8"):
        r = json.loads(line)
        if "error" in r:
            n_err += 1
            continue
        for it in r["items"]:
            con.execute("INSERT OR REPLACE INTO rel_zh VALUES (?,?,?)", (r["slug"], it["to"], it["zh"]))
            n_rel += 1

sec_n = 0
sec_path = os.path.join(PACK, "atlas", "section-zh.json")
if os.path.exists(sec_path):
    for s in json.load(open(sec_path)):
        con.execute("UPDATE section SET name_zh=? WHERE id=?", (s.get("name_zh"), s["id"]))
        sec_n += 1
con.commit()
print(f"leaf_zh_body={n_ok} (err {n_err}), rel_zh={n_rel}, sections={sec_n}")
