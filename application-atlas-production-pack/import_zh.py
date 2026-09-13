#!/usr/bin/env python3
"""Import persisted translations. Safe to import as a module; no API calls."""
import json
import sqlite3
from pathlib import Path
from atlas_runtime import PACK, corpus_lock


def import_translations(con, pack=PACK):
    atlas = Path(pack) / "atlas"
    if "name_zh" not in {r[1] for r in con.execute("PRAGMA table_info(section)")}:
        con.execute("ALTER TABLE section ADD COLUMN name_zh TEXT")
    con.execute("""CREATE TABLE IF NOT EXISTS leaf_zh_body
        (slug TEXT PRIMARY KEY, overview_zh TEXT, how_zh TEXT, rules_zh TEXT,
         variants_zh TEXT, products_zh TEXT, engine TEXT)""")
    con.execute("""CREATE TABLE IF NOT EXISTS rel_zh
        (from_slug TEXT, to_name TEXT, distinction_zh TEXT, PRIMARY KEY(from_slug,to_name))""")
    slugs = {r[0] for r in con.execute("SELECT slug FROM leaf")}
    for path, kind in [(atlas / "body-zh.jsonl", "body"), (atlas / "rels-zh.jsonl", "relations")]:
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                r = json.loads(line)
                if "error" in r or r["slug"] not in slugs:
                    continue
                if kind == "body":
                    con.execute("INSERT OR REPLACE INTO leaf_zh_body VALUES (?,?,?,?,?,?,?)",
                        (r["slug"], r["overview"], r["how"], r["rules"], r["variants"], r["products"], r["engine"]))
                else:
                    con.executemany("INSERT OR REPLACE INTO rel_zh VALUES (?,?,?)",
                        [(r["slug"], it["to"], it["zh"]) for it in r["items"]])
    sections = atlas / "section-zh.json"
    if sections.exists():
        for section in json.loads(sections.read_text()):
            con.execute("UPDATE section SET name_zh=? WHERE id=?", (section.get("name_zh"), section["id"]))
    con.execute("DELETE FROM leaf_zh_body WHERE slug NOT IN (SELECT slug FROM leaf)")
    con.execute("DELETE FROM rel_zh WHERE from_slug NOT IN (SELECT slug FROM leaf)")


def main():
    with corpus_lock(PACK):
        with sqlite3.connect(PACK / "atlas/atlas.sqlite") as con:
            import_translations(con)
            print("Translations imported")


if __name__ == "__main__":
    main()
