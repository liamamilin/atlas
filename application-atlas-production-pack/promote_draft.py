#!/usr/bin/env python3
"""Promote a draft leaf into the corpus, or merge it into an existing leaf.

Actions:
  new    slug -> DIRECTORY.md subsection (NN.MM) + applications/<slug>.md +
         research/<slug>.md, then rebuild pipeline with embedding/zh snapshot
         (export -> restore aux -> embed new -> translate new -> import_zh ->
         gen-data -> gate regression).
  merge  append draft name as alias on an existing DIRECTORY.md leaf.

Usage:
  python3 promote_draft.py <slug> new   --section 20.01 [--yes]
  python3 promote_draft.py <slug> merge --into accounting-software [--yes]
"""
import json
import os
import re
import sqlite3
import subprocess
import sys

PACK = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PACK)
from draft_new import DRAFTS, slugify
from drafts_api import draft_path, load_review, save_review
from leaf_lint import parse_front

DIR_MD = os.path.join(PACK, "DIRECTORY.md")
APPS = os.path.join(PACK, "applications")
RESEARCH = os.path.join(PACK, "research")
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
WEB_SCRIPTS = os.path.join(os.path.dirname(PACK), "atlas-web", "scripts")
BASELINE_GATE = 0.90   # alarm threshold (production baseline 0.942; allow small drift)


def run(cmd, **kw):
    print("$", " ".join(map(str, cmd)), flush=True)
    r = subprocess.run(cmd, cwd=PACK, **kw)
    if r.returncode != 0:
        raise RuntimeError(f"exit {r.returncode}: {cmd[0]}")


def snapshot_aux():
    """Copy embedding rows out (export rebuild wipes them; zh tables are rebuilt
    from jsonl by import_zh)."""
    if not os.path.exists(DB):
        return []
    con = sqlite3.connect(DB)
    try:
        rows = con.execute("SELECT slug, model, dim, vec FROM embedding").fetchall()
    except sqlite3.OperationalError:
        rows = []
    con.close()
    return rows


def insert_bullet(section_id, name):
    """Insert `- Name` alphabetically into the `### NN.MM ...` block of DIRECTORY.md."""
    text = open(DIR_MD, encoding="utf-8").read()
    lines = text.split("\n")
    start = None
    for i, l in enumerate(lines):
        if re.match(rf"^###\s+{re.escape(section_id)}\b", l):
            start = i
            break
    if start is None:
        raise RuntimeError(f"DIRECTORY.md 中找不到子域 {section_id}")
    end = start + 1
    while end < len(lines) and not re.match(r"^#{1,3}\s|^---$", lines[end]):
        end += 1
    bullets = [l for l in lines[start + 1 : end] if l.startswith("- ")]
    new = f"- {name}"
    if any(l[2:].lower() == name.lower() for l in bullets):
        return new  # idempotent: bullet already inserted by an earlier attempt
    bullets.append(new)
    bullets.sort(key=lambda s: re.sub(r"^- ", "", s).lower())
    lines[start + 1 : end] = bullets
    open(DIR_MD, "w", encoding="utf-8").write("\n".join(lines))
    return new


def append_alias(into_slug, alias_name):
    """Add ` / alias_name` to the DIRECTORY bullet of into_slug (if not present)."""
    text = open(DIR_MD, encoding="utf-8").read()
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if l.startswith("- "):
            name = l[2:].strip()
            if slugify(name.split(" / ")[0]) == into_slug:
                if alias_name.lower() in name.lower():
                    return name
                lines[i] = f"- {name} / {alias_name}"
                open(DIR_MD, "w", encoding="utf-8").write("\n".join(lines))
                return lines[i][2:]
    raise RuntimeError(f"DIRECTORY.md 中找不到叶子 {into_slug}")


def promote_new(slug, section_id):
    front, body = parse_front(open(draft_path(slug), encoding="utf-8").read())
    name = front.get("name") or slug
    if slugify(name) != slug:
        raise RuntimeError(f"叶子名与 slug 不一致: name={name!r} slug={slug}")

    snap = snapshot_aux()
    open(os.path.join(APPS, slug + ".md"), "w", encoding="utf-8").write(body.rstrip() + "\n")
    rp = os.path.join(DRAFTS, slug + ".research.md")
    if os.path.exists(rp):
        os.replace(rp, os.path.join(RESEARCH, slug + ".md"))
    insert_bullet(section_id, name)

    # 2. rebuild pipeline
    run([sys.executable, "export_atlas.py"])
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS embedding (slug TEXT PRIMARY KEY, model TEXT, dim INTEGER, vec BLOB)")
    if snap:
        cur.executemany("INSERT OR REPLACE INTO embedding VALUES (?,?,?,?)", snap)
    con.commit()
    con.close()
    run([sys.executable, "embed_leaves.py"])
    run([sys.executable, "translate_bodies.py", "--engine", "api"])
    run([sys.executable, "translate_rels.py", "--engine", "api"])
    run([sys.executable, "import_zh.py"])
    run([sys.executable, os.path.join(WEB_SCRIPTS, "gen-data.py")])

    # 3. gate regression
    out = os.popen(f"{sys.executable} gate_check.py 2>/dev/null | tail -2").read()
    m = re.search(r"adj=([\d.]+%)", out)
    gate = m.group(1) if m else "n/a"
    ok_gate = m and float(m.group(1).rstrip("%")) / 100 >= BASELINE_GATE
    print(f"gate regression: {gate} ({'OK' if ok_gate else 'ALARM: below baseline'})")

    # 4. record + cleanup
    rv = load_review()
    rv[slug] = {"promoted": True, "action": "new", "section": section_id,
                "gate": gate, "gate_ok": bool(ok_gate)}
    save_review(rv)
    for suffix in (".md", ".opencode.log"):
        p = os.path.join(DRAFTS, slug + suffix)
        if os.path.exists(p):
            os.remove(p)
    print(f"promoted {slug} -> {section_id} (gate {gate})")


def promote_merge(slug, into_slug):
    front, _ = parse_front(open(draft_path(slug), encoding="utf-8").read())
    name = front.get("name") or slug
    newdir = append_alias(into_slug, name)
    rv = load_review()
    rv[slug] = {"promoted": True, "action": "merge", "into": into_slug, "directory": newdir}
    save_review(rv)
    for suffix in (".md", ".research.md", ".opencode.log"):
        p = os.path.join(DRAFTS, slug + suffix)
        if os.path.exists(p):
            os.remove(p)
    print(f"merged {slug} -> alias of {into_slug} (需重跑 export+gen 使别名生效)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    slug, action = sys.argv[1], sys.argv[2]
    if action == "new":
        sect = sys.argv[sys.argv.index("--section") + 1]
        promote_new(slug, sect)
    elif action == "merge":
        into = sys.argv[sys.argv.index("--into") + 1]
        promote_merge(slug, into)
    else:
        print("action 必须是 new|merge")
        sys.exit(2)
