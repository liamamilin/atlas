#!/usr/bin/env python3
"""Export the Application Atlas corpus to SQLite (primary store) + atlas.json (portable).

Parses:
  DIRECTORY.md          -> tree: sections + leaf order (parent relations)
  applications/*.md     -> leaf sections, Related table (relations), products, sources
  research/*.md         -> research metadata (boundary findings section, uncertainties)
  STATUS.md             -> processed dates, boundary issues, taxonomy decisions
  logs/<slug>.log       -> writing-model attribution

Outputs:
  atlas/atlas.sqlite    -- primary store (FTS5 search index included)
  atlas/atlas.json      -- portable graph export
  logs/relation-words.txt -- raw histogram of Relationship column values
"""
import json
import os
import re
import sqlite3
import sys
from collections import Counter, defaultdict

PACK = os.path.dirname(os.path.abspath(__file__))
APPS = os.path.join(PACK, "applications")
RESEARCH = os.path.join(PACK, "research")
LOGS = os.path.join(PACK, "logs")
OUT = os.path.join(PACK, "atlas")
os.makedirs(OUT, exist_ok=True)

SECTION_RE = re.compile(r"^##\s+(.+)$", re.M)
SUB_RE = re.compile(r"^###\s+(.+)$", re.M)
REL_TABLE_ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)
REL_TABLE_ROW2_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)


def read(p):
    with open(p, encoding="utf-8", errors="replace") as f:
        return f.read()


# ---------------------------------------------------------------- DIRECTORY
def parse_directory():
    text = read(os.path.join(PACK, "DIRECTORY.md"))
    lines = text.splitlines()
    top = None
    sub = None
    tree = []          # list of {"id","name","parent","path"}
    leaves = []        # ordered [{"name","section_id","section_name","order"}]
    order = 0
    top_re = re.compile(r"^##\s+(\d[\d.]*\.?)\s+(.+)$")
    sub_re = re.compile(r"^###\s+(\d[\d.]*\.?)\s+(.+)$")
    seen_names = Counter()
    for ln in lines:
        m = top_re.match(ln)
        if m:
            top = {"id": m.group(1).rstrip("."), "name": m.group(2).strip(), "parent": None}
            tree.append(top)
            sub = None
            continue
        m = sub_re.match(ln)
        if m:
            sub = {"id": m.group(1), "name": m.group(2).strip(), "parent": top["id"] if top else None}
            tree.append(sub)
            continue
        if ln.startswith("- ") and not ln.startswith("- ["):
            name = ln[2:].strip()
            seen_names[name] += 1
            sec_id = sub["id"] if sub else (top["id"] if top else "")
            sec_name = sub["name"] if sub else (top["name"] if top else "")
            leaves.append({"name": name, "section_id": sec_id, "section_name": sec_name,
                           "order": order})
            order += 1
    dups = {n: c for n, c in seen_names.items() if c > 1}
    return tree, leaves, dups


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


# ------------------------------------------------- relation canonicalization
# Closed enumeration of relation kinds (Phase 0 convergence, STATUS decisions).
# Order matters: first match wins; check overlaps before adjacent.
CANON_RULES = [
    ("overlaps",      [r"overlap", r"straddl", r"shared", r"shares", r"blurs", r"same population", r"alias"]),
    ("contrasts",     [r"collision", r"polysem", r"namesake", r"name[- ]?only", r"word[- ]?collision", r"false friend"]),
    ("capability_of", [r"component", r"capability (slice|of|layer)", r"capability", r"slice", r"layer of", r"module of", r"embedded", r"bundled capability", r"feature of"]),
    ("upstream",      [r"upstream", r"feeds", r"input to", r"source of"]),
    ("downstream",    [r"downstream", r"consumer", r"consumes", r"uses", r"builds on"]),
    ("sibling",       [r"sibling", r"same family", r"same genus", r"same spine", r"same core"]),
    ("broader",       [r"broader", r"umbrella", r"parent", r"superset", r"generic", r"general form"]),
    ("narrower",      [r"narrower", r"variant", r"specialization", r"specialisation", r"subset", r"specific form", r"industry (form|variant)"]),
    ("counterpart",   [r"counterpart", r"opposite", r"other side", r"mirror", r"inverse"]),
    ("authority",     [r"authority", r"regulator", r"agency counterpart", r"external authority"]),
    ("substrate",     [r"substrate", r"foundation", r"infrastructure (for|layer)", r"underlies"]),
    ("complementary", [r"complement", r"pairs with", r"integrates with", r"adjacent, often bundled", r"commonly bundled"]),
    ("alternative",   [r"alternative", r"competitor", r"rival", r"instead of"]),
    ("adjacent",      [r"adjacent", r"neighbor", r"neighbour", r"nearby", r"different domain", r"different object", r"different record"]),
]


def canon_rel(raw):
    if not raw:
        return "related"
    r = raw.lower()
    for canon, pats in CANON_RULES:
        for p in pats:
            if re.search(p, r):
                return canon
    return "other"


def zh_str(v):
    if isinstance(v, list):
        return "\n".join(str(x) for x in v)
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False)


def build_alias_index(dir_leaves, docs):
    """name / alt-spelling / acronym -> slug"""
    alias = defaultdict(set)
    for e in dir_leaves:
        slug = e.get("slug") or slugify(e["name"])
        name = e["name"]
        alias[slugify(name)].add(slug)
        # split alt spellings: "Foo / Bar / Baz", "Foo (BAR)"
        parts = [p.strip() for p in re.split(r"[/(,]", name) if p.strip()]
        for p in parts:
            alias[slugify(p)].add(slug)
            # acronyms: "Customer Relationship Management / CRM" -> crm
            words = re.findall(r"\b[A-Za-z0-9]+\b", p)
            if len(words) >= 2:
                acr = "".join(w[0] for w in words if w[0].isupper())
                if len(acr) >= 2:
                    alias[acr.lower()].add(slug)
        # explicit parenthetical acronyms
        for acr in re.findall(r"\(([A-Z][A-Za-z0-9/\- ]{1,20})\)", name):
            alias[slugify(acr)].add(slug)
    for s in docs:
        alias[s].add(s)
    return alias


def resolve_target(to_name, alias, docs):
    """Try progressively looser resolution; returns slug or None."""
    base = to_name.split("(")[0]
    cands = []
    cands.append(re.sub(r"\s*/\s*.*$", "", base))            # strip "/ alt"
    cands.append(base)                                        # full incl. alt
    for p in re.split(r"\s*/\s*", base):                      # each alt alone
        cands.append(p.strip())
    for c in cands:
        sl = slugify(c)
        hits = alias.get(sl)
        if hits:
            in_docs = sorted(h for h in hits if h in docs)
            if in_docs:
                return in_docs[0]
    # token-subset match against directory names
    q = set(re.findall(r"[a-z0-9]+", slugify(base)))
    if q:
        best, best_score = None, 0.0
        for s in docs:
            n = set(re.findall(r"[a-z0-9]+", s))
            if not n:
                continue
            score = len(q & n) / max(len(q | n), 1)
            if score > best_score:
                best, best_score = s, score
        if best_score >= 0.75:
            return best
    return None


# ---------------------------------------------------------------- leaf docs
def parse_leaf(slug, text):
    doc = {"slug": slug, "text": text}
    # split into top-level sections
    parts = SECTION_RE.split(text)
    # parts[0] = preamble (title line), then alternating name, body
    sections = {}
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i].strip()] = parts[i + 1].strip()
    doc["sections"] = sections

    def grab(*names):
        for n in names:
            for k, v in sections.items():
                if k.lower().startswith(n.lower()):
                    return v
        return ""

    doc["overview"] = grab("Overview")
    doc["users"] = grab("Users")
    doc["core_model"] = grab("Core Model")
    doc["how_it_works"] = grab("How It Works")
    doc["interfaces"] = grab("Interfaces")
    doc["rules"] = grab("Important Rules", "Rules")
    doc["variants"] = grab("Variants", "One Structure")
    doc["related"] = grab("Related Application Types", "Related")
    doc["products"] = grab("Representative Products", "Products")
    doc["sources"] = grab("Sources", "Source Notes")
    doc["title"] = parts[0].lstrip("# ").strip() if parts else slug

    # defining core: first "The Defining Core" subsection body, else first paragraph of core model
    dc = ""
    m = re.search(r"###\s+.*[Dd]efining[^\n]*\n+(.*?)(?=\n###|\Z)", doc["core_model"], re.S)
    if m:
        dc = m.group(1).strip()
    else:
        paras = [p for p in doc["core_model"].split("\n\n") if len(p.strip()) > 80]
        dc = paras[0].strip() if paras else ""
    doc["defining_core"] = dc

    # related table rows
    rels = []
    matched_spans = set()
    for m2 in REL_TABLE_ROW_RE.finditer(doc["related"]):
        matched_spans.add(m2.span())
        rels.append({"to_name": m2.group(1).strip(),
                     "rel_raw": m2.group(2).strip(),
                     "distinction": m2.group(3).strip()})
    # 2-column variant (Type | Distinction) — no explicit Relationship word
    for m2 in REL_TABLE_ROW2_RE.finditer(doc["related"]):
        if m2.span() in matched_spans:
            continue
        to_name, distinction = m2.group(1).strip(), m2.group(2).strip()
        if to_name in ("Application Type", "Type", "---", "Distinction") or distinction == "---":
            continue
        rels.append({"to_name": to_name, "rel_raw": "", "distinction": distinction})
    doc["relations"] = rels

    # representative product names: bold list items or "- **Name**" patterns
    prods = re.findall(r"^\s*[-*]\s+\*{0,1}([^*\n]{2,60}?)\*{0,1}\s*(?:[—–-]|$)", doc["products"], re.M)
    doc["product_names"] = [p.strip() for p in prods if p.strip()][:12]

    # uncertainties/boundary from research side
    doc["research"] = ""
    rp = os.path.join(RESEARCH, slug + ".md")
    if os.path.exists(rp):
        rt = read(rp)
        doc["research"] = rt
        doc["boundary_findings"] = grab_from(rt, "Boundary Findings")
        doc["uncertainties"] = grab_from(rt, "Uncertainties")

    # model attribution from log first lines
    doc["model"] = ""
    lp = os.path.join(LOGS, slug + ".log")
    if os.path.exists(lp):
        try:
            head = read(lp)[:2000]
            m3 = re.search(r"atlas-writer\s*·\s*([a-z0-9.\-]+)", head)
            if m3:
                doc["model"] = m3.group(1)
        except Exception:
            pass
    doc["size"] = len(text)
    return doc


def grab_from(text, header):
    m = re.search(r"^#+\s*.*" + re.escape(header) + r".*$", text, re.M | re.I)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^#+\s+", rest, re.M)
    return rest[: nxt.start()].strip() if nxt else rest.strip()


# ---------------------------------------------------------------- STATUS
def parse_status():
    text = read(os.path.join(PACK, "STATUS.md"))
    out = {}
    # processed dates: lines like "slug — 2026-09-06 — ..."
    dates = {}
    for m in re.finditer(r"^- ([a-z0-9\-]+) — (\d{4}-\d{2}-\d{2}) —", text, re.M):
        dates[m.group(1)] = m.group(2)
    out["processed_dates"] = dates
    return out


# ---------------------------------------------------------------- build
def main():
    tree, dir_leaves, dups = parse_directory()
    print(f"directory: {len(tree)} sections, {len(dir_leaves)} leaf entries, {len(dups)} duplicate names")

    status = parse_status()

    docs = {}
    files = sorted(f for f in os.listdir(APPS) if f.endswith(".md"))
    for f in files:
        slug = f[:-3]
        docs[slug] = parse_leaf(slug, read(os.path.join(APPS, f)))
    print(f"parsed {len(docs)} leaf documents")

    # match directory entries to slugs
    unresolved = []
    dir_index = {}
    for e in dir_leaves:
        slug = slugify(e["name"])
        if slug in docs:
            e["slug"] = slug
            dir_index[slug] = e
        else:
            unresolved.append(e["name"])
    print(f"directory slugs matched: {len(dir_index)}, unresolved: {len(unresolved)}")
    for u in unresolved:
        print("  UNRESOLVED:", u)

    # orphan docs (in applications/ but not matched from directory)
    orphans = [s for s in docs if s not in dir_index]
    if orphans:
        print(f"orphan docs (no directory node): {len(orphans)}")
        for o in orphans[:20]:
            print("  ORPHAN:", o)

    # relation histogram (raw + canonical closed enumeration)
    rel_counter = Counter()
    canon_counter = Counter()
    for d in docs.values():
        for r in d["relations"]:
            if r["to_name"] in ("Application Type", "Type", "---") or r["rel_raw"] == "---":
                continue
            rel_counter[r["rel_raw"]] += 1
            canon_counter[canon_rel(r["rel_raw"])] += 1
    with open(os.path.join(LOGS, "relation-words.txt"), "w") as f:
        f.write("# canonical closed enumeration\n")
        for w, c in canon_counter.most_common():
            f.write(f"{c:6d}  {w}\n")
        f.write("\n# raw values (top 200)\n")
        for w, c in rel_counter.most_common(200):
            f.write(f"{c:6d}  {w}\n")
    print(f"distinct Relationship values: {len(rel_counter)} (top 25: {[w for w,_ in rel_counter.most_common(25)]})")
    print(f"canonical enumeration: {dict(canon_counter.most_common())}")

    # relation target resolution
    alias = build_alias_index(dir_leaves, docs)
    unmapped = Counter()
    total_rel = 0
    resolved_rel = 0
    for d in docs.values():
        for r in d["relations"]:
            if r["to_name"] in ("Application Type", "Type", "---") or r["rel_raw"] == "---":
                continue
            total_rel += 1
            tgt = resolve_target(r["to_name"], alias, docs)
            if tgt:
                resolved_rel += 1
                r["to_slug"] = tgt
            else:
                unmapped[r["to_name"]] += 1
    print(f"relations total {total_rel}, resolved {resolved_rel}, unmapped {total_rel - resolved_rel}")

    # ---------------------------------------------------------------- sqlite
    db_path = os.path.join(OUT, "atlas.sqlite")
    if os.path.exists(db_path):
        os.remove(db_path)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
    CREATE TABLE section (id TEXT PRIMARY KEY, name TEXT, parent TEXT, path TEXT, kind TEXT);
    CREATE TABLE leaf (
      slug TEXT PRIMARY KEY,
      name TEXT, section_id TEXT, section_name TEXT, order_idx INTEGER,
      title TEXT, overview TEXT, users TEXT, core_model TEXT, defining_core TEXT,
      how_it_works TEXT, interfaces TEXT, rules TEXT, variants TEXT,
      related_md TEXT, products_md TEXT, sources_md TEXT,
      full_md TEXT, size INTEGER, model TEXT, processed_date TEXT,
      research_md TEXT, boundary_findings TEXT, uncertainties TEXT,
      name_zh TEXT, aliases_zh TEXT, l0_zh TEXT
    );
    CREATE TABLE relation (
      from_slug TEXT, to_name TEXT, to_slug TEXT, rel_raw TEXT, rel_kind TEXT, distinction TEXT
    );
    CREATE TABLE boundary_issue (
      slug TEXT, date TEXT, text TEXT
    );
    CREATE INDEX idx_rel_from ON relation(from_slug);
    CREATE INDEX idx_rel_to ON relation(to_slug);
    CREATE INDEX idx_leaf_section ON leaf(section_id);
    """)
    # FTS5
    cur.execute("""    CREATE VIRTUAL TABLE leaf_fts USING fts5(
      slug, name, name_zh, overview, defining_core, l0_zh, body,
      tokenize='trigram'
    )
    """)
    cur.execute("""CREATE VIRTUAL TABLE leaf_fts_lat USING fts5(
      slug, name, overview, defining_core, body,
      tokenize='porter unicode61'
    )""")

    # sections
    path_map = {}
    for sec in tree:
        pid = sec["parent"]
        path = (path_map.get(pid, "") + " > " if pid else "") + sec["name"]
        path_map[sec["id"]] = path
        cur.execute("INSERT INTO section VALUES (?,?,?,?,?)",
                    (sec["id"], sec["name"], pid, path, "top" if not sec["parent"] else "sub"))

    # translations (if translations.jsonl exists, load zh columns)
    zh = {}
    zh_path = os.path.join(OUT, "translations.jsonl")
    if os.path.exists(zh_path):
        for line in open(zh_path, encoding="utf-8"):
            try:
                r = json.loads(line)
                zh[r["slug"]] = r
            except Exception:
                pass
        print(f"translations loaded: {len(zh)}")

    # leaves
    unresolved_slugs = set()
    for e in dir_leaves:
        slug = e.get("slug")
        if not slug:
            unresolved_slugs.add(slugify(e["name"]))
            continue
        d = docs[slug]
        z = zh.get(slug, {})
        cur.execute("""INSERT INTO leaf VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (slug, e["name"], e["section_id"], e["section_name"], e["order"],
                     d["title"], d["overview"], d["users"], d["core_model"], d["defining_core"],
                     d["how_it_works"], d["interfaces"], d["rules"], d["variants"],
                     d["related"], d["products"], d["sources"],
                     d["text"], d["size"], d["model"], status["processed_dates"].get(slug, ""),
                     d["research"], d.get("boundary_findings", ""), d.get("uncertainties", ""),
                     zh_str(z.get("name_zh", "")), zh_str(z.get("aliases_zh", [])), zh_str(z.get("l0_zh", ""))))
        body = "\n\n".join([d["overview"], d["defining_core"], d["how_it_works"], d["variants"], d["text"]])
        cur.execute("INSERT INTO leaf_fts VALUES (?,?,?,?,?,?,?)",
                    (slug, e["name"], zh_str(z.get("name_zh", "")), (d["overview"] or "")[:8000],
                     (d["defining_core"] or "")[:8000], zh_str(z.get("l0_zh", "")), body[:200000]))
        cur.execute("INSERT INTO leaf_fts_lat VALUES (?,?,?,?,?)",
                    (slug, e["name"], d["overview"][:8000], d["defining_core"][:8000], body[:200000]))

    # relations with resolution + canonical kind
    for slug, d in docs.items():
        for r in d["relations"]:
            if r["to_name"] in ("Application Type", "Type", "---") or r["rel_raw"] == "---":
                continue
            cur.execute("INSERT INTO relation VALUES (?,?,?,?,?,?)",
                        (slug, r["to_name"], r.get("to_slug"), r["rel_raw"],
                         canon_rel(r["rel_raw"]), r["distinction"]))
    con.commit()

    # meta
    cur.executemany("INSERT INTO meta VALUES (?,?)", [
        ("leaves_directory", len(dir_leaves)),
        ("leaves_documents", len(docs)),
        ("leaves_unresolved", len(unresolved)),
        ("relations_total", total_rel),
        ("relations_unmapped", sum(unmapped.values())),
        ("duplicate_directory_names", json.dumps(dups)),
        ("model_counts", json.dumps(Counter(d["model"] or "unknown" for d in docs.values()))),
        ("generated", "2026-09-10"),
    ])
    con.commit()
    con.close()

    # ---------------------------------------------------------------- json
    j = {"leaves": {}, "sections": tree, "relations": [], "meta": {}}
    for slug, d in docs.items():
        e = dir_index.get(slug, {})
        j["leaves"][slug] = {
            "name": e.get("name", d["title"]),
            "section": e.get("section_id"), "order": e.get("order"),
            "overview": d["overview"], "defining_core": d["defining_core"],
            "variants": d["variants"], "sources": d["sources"],
            "relations": d["relations"], "products": d["product_names"],
            "model": d["model"], "processed": status["processed_dates"].get(slug),
            "size": d["size"],
        }
    for slug, d in docs.items():
        for r in d["relations"]:
            if r["to_name"] in ("Application Type", "Type", "---") or r["rel_raw"] == "---":
                continue
            j["relations"].append({"from": slug, "to_name": r["to_name"],
                                   "to": r.get("to_slug"), "rel": r["rel_raw"],
                                   "kind": canon_rel(r["rel_raw"]), "distinction": r["distinction"]})
    j["meta"] = {"leaves": len(docs), "relations": len(j["relations"]),
                 "unmapped_directory_names": unresolved,
                 "model_counts": Counter(d["model"] or "unknown" for d in docs.values())}
    with open(os.path.join(OUT, "atlas.json"), "w") as f:
        json.dump(j, f, ensure_ascii=False)

    # unmapped targets for the dangling-reference register
    with open(os.path.join(LOGS, "unmapped-rel-targets.txt"), "w") as f:
        for name, c in unmapped.most_common():
            f.write(f"{c:6d}  {name}\n")

    print(f"sqlite -> {db_path}")
    print(f"json   -> {os.path.join(OUT, 'atlas.json')}")


if __name__ == "__main__":
    main()
