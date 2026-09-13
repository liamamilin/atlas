#!/usr/bin/env python3
"""Application Atlas MCP server.

Exposes the atlas corpus (1804 software application types, bilingual,
with relation graph + vector search + classifier) as MCP tools.
"""
import json
import os
import re
import sqlite3
import urllib.request

import numpy as np
from mcp.server.fastmcp import FastMCP

from atlas_runtime import PACK as DATA_PACK
PACK = str(DATA_PACK)
DB = os.path.join(PACK, "atlas", "atlas.sqlite")

mcp = FastMCP("application-atlas")


def db():
    return sqlite3.connect(DB)


def embed_texts(texts):
    b = json.dumps({"model": "bge-m3", "input": texts}).encode()
    r = json.load(urllib.request.urlopen(urllib.request.Request(
        "http://localhost:11434/api/embed", b, {"Content-Type": "application/json"}), timeout=300))
    return [np.array(e, dtype=np.float32) for e in r["embeddings"]]


@mcp.tool()
def search_atlas(query: str, k: int = 5) -> str:
    """Semantic search over 1804 software application types (bilingual zh/en).
    Returns top-k leaf types with similarity, Chinese name, defining core, and graph neighbors."""
    con = db()
    rows = con.execute("SELECT slug, vec FROM embedding").fetchall()
    M = np.stack([np.frombuffer(r[1], dtype=np.float32) for r in rows])
    M /= (np.linalg.norm(M, axis=1, keepdims=True) + 1e-9)
    slugs = [r[0] for r in rows]
    q = embed_texts([query])[0]
    q /= (np.linalg.norm(q) + 1e-9)
    sims = M @ q
    out = []
    for i in np.argsort(-sims)[:max(1, min(k, 15))]:
        s = slugs[i]
        leaf = con.execute("SELECT name, name_zh, l0_zh, defining_core FROM leaf WHERE slug=?", (s,)).fetchone()
        nbs = con.execute("""SELECT to_name, rel_kind FROM relation WHERE from_slug=? LIMIT 4""", (s,)).fetchall()
        out.append({"slug": s, "score": round(float(sims[i]), 3), "name": leaf[0], "name_zh": leaf[1],
                    "defining_core": (leaf[2] or leaf[3] or "")[:300],
                    "related": [f"{n[0]}({n[1]})" for n in nbs]})
    con.close()
    return json.dumps(out, ensure_ascii=False, indent=1)


@mcp.tool()
def get_leaf(slug: str) -> str:
    """Get full detail of one application type: overview, defining core, variants,
    representative products, sources, and all typed relations to other types."""
    con = db()
    r = con.execute("""SELECT slug, name, name_zh, aliases_zh, section_id, section_name,
                       overview, defining_core, how_it_works, rules, variants, products_md, sources_md
                       FROM leaf WHERE slug=?""", (slug,)).fetchone()
    if not r:
        alt = con.execute("SELECT slug FROM leaf WHERE name_zh LIKE ? OR name LIKE ?",
                          (f"%{slug}%", f"%{slug}%")).fetchall()
        return json.dumps({"error": "slug not found", "candidates": [a[0] for a in alt[:10]]}, ensure_ascii=False)
    try:
        aliases = json.loads(r[3]) if r[3] else []
        if not isinstance(aliases, list):
            aliases = [a for a in re.split(r"[\n,]", str(r[3])) if a.strip()]
    except Exception:
        aliases = [a for a in re.split(r"[\n,]", str(r[3] or "")) if a.strip()]
    rels = con.execute("""SELECT to_name, to_slug, rel_kind, distinction FROM relation
                          WHERE from_slug=?""", (slug,)).fetchall()
    con.close()
    return json.dumps({
        "slug": r[0], "name": r[1], "name_zh": r[2], "aliases_zh": aliases,
        "section": f"{r[4]} {r[5]}", "overview": (r[6] or "")[:1200],
        "defining_core": (r[7] or "")[:2000], "how_it_works": (r[8] or "")[:1500],
        "important_rules": (r[9] or "")[:1200], "variants": (r[10] or "")[:1500],
        "products": (r[11] or "")[:1500], "sources": (r[12] or "")[:800],
        "relations": [{"to": x[0], "slug": x[1], "kind": x[2], "distinction": x[3][:200]} for x in rels],
    }, ensure_ascii=False, indent=1)


@mcp.tool()
def classify_product(description: str) -> str:
    """Classify a software product (given a 1-3 sentence description, zh or en) into
    one of the 1804 atlas types. Returns the best-matching type slug with confidence
    scores for top candidates. Use when you need to know 'what kind of software is this'."""
    import sys
    sys.path.insert(0, PACK)
    from classify import classify
    r = classify(description)
    top = sorted(r["scores"].items(), key=lambda kv: -kv[1])[:5]
    con = db()
    named = [{"slug": s, "name_zh": (con.execute("SELECT name_zh FROM leaf WHERE slug=?", (s,)).fetchone() or ["?"])[0],
              "score": sc} for s, sc in top]
    con.close()
    return json.dumps({"choice": r["choice"], "candidates": named}, ensure_ascii=False, indent=1)


@mcp.tool()
def get_section_tree() -> str:
    """Get the atlas directory tree: 113 sections (top-level domains and sub-domains)
    with their id, name, parent, and leaf count. Use to browse the taxonomy."""
    con = db()
    secs = con.execute("""SELECT s.id, s.name, s.parent, s.path,
                          (SELECT COUNT(*) FROM leaf l WHERE l.section_id = s.id)
                          FROM section s ORDER BY s.id""").fetchall()
    con.close()
    return json.dumps([{"id": x[0], "name": x[1], "parent": x[2], "path": x[3], "leaves": x[4]}
                       for x in secs], ensure_ascii=False, indent=1)


@mcp.tool()
def get_neighbors(slug: str) -> str:
    """Get all typed relations of one application type to its neighbors
    (adjacent/sibling/upstream/downstream/overlaps etc.), each with the corpus's
    own boundary-distinction text. Use to understand how one type differs from its neighbors."""
    con = db()
    rels = con.execute("""SELECT to_name, to_slug, rel_kind, distinction FROM relation
                          WHERE from_slug=? ORDER BY rel_kind""", (slug,)).fetchall()
    rev = con.execute("""SELECT from_slug, rel_kind, distinction FROM relation
                         WHERE to_slug=?""", (slug,)).fetchall()
    name = con.execute("SELECT name, name_zh FROM leaf WHERE slug=?", (slug,)).fetchone()
    con.close()
    if not name:
        return json.dumps({"error": "slug not found"}, ensure_ascii=False)
    return json.dumps({"slug": slug, "name": name[0], "name_zh": name[1],
                       "outbound": [{"to": r[0], "slug": r[1], "kind": r[2], "distinction": r[3][:250]} for r in rels],
                       "inbound": [{"from": r[0], "kind": r[1], "distinction": r[2][:250]} for r in rev]},
                      ensure_ascii=False, indent=1)


if __name__ == "__main__":
    mcp.run()
