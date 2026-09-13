#!/usr/bin/env python3
"""Generate atlas-web public/data/*.json from atlas.sqlite + classified apps.
Source of truth = markdown corpus; rerun after corpus updates."""
import json
import os
import re
import sqlite3

PACK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "application-atlas-production-pack")
DB = os.path.join(PACK, "atlas", "atlas.sqlite")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public", "data")

con = sqlite3.connect(DB)
sec_cols = [r[1] for r in con.execute("PRAGMA table_info(section)")]
has_sec_zh = "name_zh" in sec_cols
sections = {}
for sid, name, parent, path, kind in con.execute("SELECT id, name, parent, path, kind FROM section"):
    sections[sid] = {"id": sid, "name": name, "parent": parent, "path": path}
if has_sec_zh:
    for sid, name_zh in con.execute("SELECT id, name_zh FROM section WHERE name_zh != ''"):
        sections[sid]["name_zh"] = name_zh
leaves = {}
for row in con.execute("SELECT slug, name, name_zh, aliases_zh, section_id, section_name, overview, defining_core, how_it_works, rules, variants, products_md, l0_zh FROM leaf"):
    leaves[row[0]] = {
        "slug": row[0], "name": row[1], "name_zh": row[2] or "",
        "aliases_zh": [a for a in (row[3] or "").split("\n") if a.strip()],
        "section_id": row[4], "section_name": row[5],
        "overview": (row[6] or "")[:2600], "dc": (row[7] or "")[:2600],
        "how": (row[8] or "")[:1800], "rules": (row[9] or "")[:1400],
        "variants": (row[10] or "")[:1800], "products": (row[11] or "")[:1800],
        "dc_zh": (row[12] or "")[:2600],
    }
# body zh from translation table
try:
    for row in con.execute("SELECT slug, overview_zh, how_zh, rules_zh, variants_zh, products_zh FROM leaf_zh_body"):
        if row[0] in leaves:
            leaves[row[0]].update({
                "overview_zh": (row[1] or "")[:2600], "how_zh": (row[2] or "")[:1800],
                "rules_zh": (row[3] or "")[:1400], "variants_zh": (row[4] or "")[:1800],
                "products_zh": (row[5] or "")[:1800],
            })
except sqlite3.OperationalError:
    pass
relations = {}
rel_zh = {}
try:
    rel_zh = {(a, tn): d for a, tn, d in con.execute("SELECT from_slug, to_name, distinction_zh FROM rel_zh")}
except sqlite3.OperationalError:
    pass
for a, b, tn, k, d in con.execute("SELECT from_slug, to_slug, to_name, rel_kind, distinction FROM relation WHERE to_slug IS NOT NULL"):
    item = {"to": b, "toName": tn, "kind": k, "distinction": (d or "")[:300]}
    z = rel_zh.get((a, tn))
    if z:
        item["distinction_zh"] = z[:300]
    relations.setdefault(a, []).append(item)

apps = json.load(open(os.path.join(PACK, "mvp_apps.json")))
classified = {c["slug"]: c for c in json.load(open(os.path.join(PACK, "mvp_apps_classified.json")))}
app_entries = []
app_by_leaf = {}
for a in apps:
    c = classified.get(a["slug"], {})
    leaf = c.get("leaf") or ""
    e = {"slug": a["slug"], "name": a["name"], "vendor": a.get("vendor", ""),
         "tagline": a.get("tagline", ""), "tasks": a.get("tasks", []),
         "leaf": leaf, "leafName": leaves.get(leaf, {}).get("name_zh", "") or leaves.get(leaf, {}).get("name", "")}
    app_entries.append(e)
    if leaf:
        app_by_leaf.setdefault(leaf, []).append({"slug": e["slug"], "name": e["name"]})

os.makedirs(os.path.join(OUT, "sections"), exist_ok=True)
os.makedirs(os.path.join(OUT, "leaves"), exist_ok=True)

# meta + search index
def summ(md, n):
    md = re.sub(r"```[\s\S]*?```", " ", md)
    prose = []
    for ln in md.splitlines():
        s = ln.strip()
        if not s or s[0] in "│├└┌#" :
            continue
        s = re.sub(r"^[-*+]\s+", "", s)
        s = re.sub(r"(\*\*|__)(.*?)\1", r"\2", s)
        s = re.sub(r"`([^`]*)`", r"\1", s)
        prose.append(s)
    if len(prose) > 1 and prose[1].startswith(prose[0]):
        prose = prose[1:]
    txt = re.sub(r"\s+", " ", " ".join(prose)).strip()
    return txt[:n]

def summ_zh(lf, n):
    c1 = summ(lf.get("dc_zh", ""), 400)
    c2 = summ(lf.get("overview_zh", ""), 400)
    return (c1 if len(c1) >= 40 or len(c1) >= len(c2) else c2)[:n]

leaf_index = []
for slug, lf in sorted(leaves.items(), key=lambda kv: (kv[1]["section_id"], kv[1]["name"])):
    leaf_index.append({"slug": slug, "name": lf["name"], "name_zh": lf["name_zh"],
                       "sec": lf["section_id"], "dc": summ(lf["dc"], 160), "dc_zh": summ_zh(lf, 160)})
l0s = []
for sid, s in sorted(sections.items(), key=lambda kv: kv[0]):
    if s["parent"]:
        continue
    subs = []
    for sid2, s2 in sorted(sections.items(), key=lambda kv: kv[0]):
        if s2["parent"] == sid:
            subs.append({"id": sid2, "name": s2["name"], "name_zh": s2.get("name_zh", ""), "path": s2["path"]})
    if not subs and any(lf["section_id"] == sid for lf in leaves.values()):
        n_leaves = sum(1 for lf in leaves.values() if lf["section_id"] == sid)
        subs.append({"id": sid, "name": f"All Types ({n_leaves})", "name_zh": f"全部类型 ({n_leaves})",
                     "path": s["path"]})
    l0s.append({"id": sid, "name": s["name"], "name_zh": s.get("name_zh", ""), "subs": subs})
meta = {"leafCount": len(leaves), "sectionCount": len(sections), "l0Count": len(l0s),
        "appCount": len(app_entries), "generated": "gen-data.py", "l0s": l0s, "leafIndex": leaf_index}
json.dump(meta, open(os.path.join(OUT, "meta.json"), "w"), ensure_ascii=False)

# per-section leaf cards
sec_leaves = {}
for slug, lf in leaves.items():
    sec_leaves.setdefault(lf["section_id"], []).append(
        {"slug": slug, "name": lf["name"], "name_zh": lf["name_zh"], "l0": summ(lf["dc"], 260), "l0_zh": summ_zh(lf, 260)})
for sid, lst in sec_leaves.items():
    json.dump({"id": sid, "name": sections[sid]["name"], "name_zh": sections[sid].get("name_zh", ""),
               "path": sections[sid]["path"],
               "leaves": sorted(lst, key=lambda x: x["name"])},
              open(os.path.join(OUT, "sections", f"{sid}.json"), "w"), ensure_ascii=False)
stale = set(os.listdir(os.path.join(OUT, "sections"))) - {f"{sid}.json" for sid in sec_leaves}
for f in stale:
    os.remove(os.path.join(OUT, "sections", f))

# per-leaf full detail
for slug, lf in leaves.items():
    detail = dict(lf)
    detail["section_name_zh"] = sections.get(lf["section_id"], {}).get("name_zh", "")
    detail["relations"] = sorted(relations.get(slug, []), key=lambda r: (r["kind"], r["toName"]))
    detail["apps"] = app_by_leaf.get(slug, [])
    json.dump(detail, open(os.path.join(OUT, "leaves", f"{slug}.json"), "w"), ensure_ascii=False)

json.dump(app_entries, open(os.path.join(OUT, "apps.json"), "w"), ensure_ascii=False)
print(f"generated: {len(leaves)} leaves, {len(sections)} sections, {len(app_entries)} apps")
