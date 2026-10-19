#!/usr/bin/env python3
"""Read-only Atlas corpus queries, shared by the MCP server and the Ask harness.

Every function here is a pure query against the canonical corpus: it reads the
derived SQLite index, the canonical Markdown, or the relation graph, and
returns plain data. Nothing here writes to the corpus, calls a shell, touches
the network beyond the configured embedding endpoint, or spawns an agent.

`mcp_atlas.py` wraps these for MCP; `atlas_ask.py` publishes the same
functions to the model as callable tools. Keeping one implementation means the
tool surface cannot drift between the two entry points.

`TOOL_SCHEMAS` is the OpenAI-style function-calling description of the safe
subset. Only tools listed there are reachable from the Ask harness, so the
read-only guarantee is structural rather than a prompt instruction.
"""
from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

import numpy as np

import atlas_model
from atlas_runtime import PACK as DATA_PACK
from atlas_sources import SourceError, read_source, source_manifest

PACK = str(DATA_PACK)
DB = os.path.join(PACK, "atlas", "atlas.sqlite")

# Bound every result so a single tool call cannot flood the model context or
# the UI. These are per-call limits, not global budgets.
MAX_SEARCH_K = 15
DEFAULT_SEARCH_K = 5
MAX_EXCERPT = 1200
MAX_RELATIONS = 40


class ToolError(RuntimeError):
    """A tool could not answer: missing corpus, bad argument, or provider down."""

    def __init__(self, message: str, code: str = "tool_error"):
        super().__init__(message)
        self.code = code


def _connect() -> sqlite3.Connection:
    if not os.path.isfile(DB):
        raise ToolError(
            "the corpus index is missing; run export_atlas.py and embed_leaves.py first",
            code="corpus_missing")
    # Read-only: the corpus is a build artifact and must never be mutated by a
    # query path.
    return sqlite3.connect(Path(DB).resolve().as_uri() + "?mode=ro", uri=True)


def _slug(value) -> str:
    text = str(value or "").strip()
    if not text or len(text) > 200:
        raise ToolError("slug must be a non-empty short string", code="bad_argument")
    return text


def _limit(value, default: int, maximum: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return max(1, min(number, maximum))


def search_atlas(query: str, k: int = DEFAULT_SEARCH_K) -> dict:
    """Semantic search over the corpus.

    Returns ranked types with similarity, the defining core, and a few graph
    neighbors. This is the entry point for "what kind of software is X".
    """
    text = str(query or "").strip()
    if not text:
        raise ToolError("query must be non-empty text", code="bad_argument")
    count = _limit(k, DEFAULT_SEARCH_K, MAX_SEARCH_K)

    # Reuse the classifier's cached snapshot so search and classification read
    # the same index revision within a request.
    import classify
    try:
        state = classify.snapshot()
    except FileNotFoundError as error:
        raise ToolError(
            "the corpus index is missing; run export_atlas.py and embed_leaves.py first",
            code="corpus_missing") from error
    except RuntimeError as error:
        raise ToolError(str(error), code="corpus_unavailable") from error
    except atlas_model.ModelConfigError as error:
        raise ToolError(str(error), code="embedding_unavailable") from error
    except OSError as error:
        raise ToolError(
            f"the embedding endpoint is unreachable: {error}",
            code="embedding_unavailable") from error

    try:
        pool, scores = classify.candidates(text, k=count, state=state)
    except atlas_model.ModelConfigError as error:
        raise ToolError(str(error), code="embedding_unavailable") from error
    except OSError as error:
        raise ToolError(
            f"the embedding endpoint is unreachable: {error}",
            code="embedding_unavailable") from error

    # candidates() expands the pool with graph neighbors for classification.
    # Search promises exactly `k` ranked types, so take the top slice by score.
    ranked = sorted(pool, key=lambda slug: (-scores.get(slug, 0.0), slug))[:count]

    results = []
    for slug in ranked:
        name_zh, core = state.leaf_info.get(slug) or ("", "")
        neighbors = sorted(state.neighbors.get(slug, set()))[:4]
        results.append({
            "slug": slug,
            "score": round(float(scores.get(slug, 0.0)), 4),
            "name_zh": name_zh,
            "defining_core": str(core or "")[:MAX_EXCERPT],
            "related": neighbors,
        })
    return {"query": text, "count": len(results), "results": results}


def get_leaf(slug: str) -> dict:
    """Full detail for one type: core, variants, products, sources, relations."""
    slug = _slug(slug)
    connection = _connect()
    try:
        row = connection.execute(
            """SELECT slug, name, name_zh, aliases_zh, section_id, section_name,
                      overview, defining_core, how_it_works, rules, variants,
                      products_md, sources_md
               FROM leaf WHERE slug=?""", (slug,)).fetchone()
        if not row:
            candidates = [item[0] for item in connection.execute(
                "SELECT slug FROM leaf WHERE slug LIKE ? OR name LIKE ? "
                "OR name_zh LIKE ? LIMIT 10",
                (f"%{slug}%", f"%{slug}%", f"%{slug}%")).fetchall()]
            return {"error": "slug not found", "requested": slug,
                    "candidates": candidates}
        relations = connection.execute(
            """SELECT to_name, to_slug, rel_kind, distinction FROM relation
               WHERE from_slug=? LIMIT ?""", (slug, MAX_RELATIONS)).fetchall()
    finally:
        connection.close()

    try:
        aliases = json.loads(row[3]) if row[3] else []
        if not isinstance(aliases, list):
            aliases = []
    except (TypeError, ValueError):
        aliases = []

    return {
        "slug": row[0], "name": row[1], "name_zh": row[2], "aliases_zh": aliases,
        "section": f"{row[4]} {row[5]}",
        "overview": str(row[6] or "")[:MAX_EXCERPT],
        "defining_core": str(row[7] or "")[:2000],
        "how_it_works": str(row[8] or "")[:1500],
        "important_rules": str(row[9] or "")[:MAX_EXCERPT],
        "variants": str(row[10] or "")[:1500],
        "products": str(row[11] or "")[:1500],
        "sources": str(row[12] or "")[:800],
        "relations": [
            {"to": item[0], "slug": item[1], "kind": item[2],
             "distinction": str(item[3] or "")[:200]}
            for item in relations],
    }


def get_neighbors(slug: str) -> dict:
    """All typed relations of one type, in and out, with boundary text."""
    slug = _slug(slug)
    connection = _connect()
    try:
        name = connection.execute(
            "SELECT name, name_zh FROM leaf WHERE slug=?", (slug,)).fetchone()
        if not name:
            return {"error": "slug not found", "requested": slug}
        outbound = connection.execute(
            """SELECT to_name, to_slug, rel_kind, distinction FROM relation
               WHERE from_slug=? ORDER BY rel_kind LIMIT ?""",
            (slug, MAX_RELATIONS)).fetchall()
        inbound = connection.execute(
            """SELECT from_slug, rel_kind, distinction FROM relation
               WHERE to_slug=? ORDER BY rel_kind LIMIT ?""",
            (slug, MAX_RELATIONS)).fetchall()
    finally:
        connection.close()
    return {
        "slug": slug, "name": name[0], "name_zh": name[1],
        "outbound": [
            {"to": item[0], "slug": item[1], "kind": item[2],
             "distinction": str(item[3] or "")[:250]}
            for item in outbound],
        "inbound": [
            {"from": item[0], "kind": item[1],
             "distinction": str(item[2] or "")[:250]}
            for item in inbound],
    }


def get_section_tree(depth: int = 2) -> dict:
    """The taxonomy: domains and sub-domains with their type counts."""
    connection = _connect()
    try:
        rows = connection.execute(
            """SELECT s.id, s.name, s.parent, s.path,
                      (SELECT COUNT(*) FROM leaf l WHERE l.section_id = s.id)
               FROM section s ORDER BY s.id""").fetchall()
    finally:
        connection.close()
    sections = [
        {"id": row[0], "name": row[1], "parent": row[2], "path": row[3],
         "leaves": row[4]}
        for row in rows]
    # `depth=1` returns only top-level domains, which keeps the payload small
    # when the model just needs the shape of the taxonomy.
    if _limit(depth, 2, 3) == 1:
        top = {item["id"] for item in sections if not item["parent"]}
        sections = [item for item in sections if item["id"] in top]
    return {"count": len(sections), "sections": sections}


def read_atlas_source(slug: str, kind: str = "application", section: str = "",
                      offset: int = 0, limit: int = 12000) -> dict:
    """Canonical Markdown for one type, with pagination and a fingerprint."""
    slug = _slug(slug)
    kind = str(kind or "application").strip().lower()
    if kind not in {"application", "research"}:
        raise ToolError("kind must be application or research",
                        code="bad_argument")
    try:
        return read_source(slug, kind, str(section or "").strip() or None,
                           max(0, int(offset or 0)),
                           _limit(limit, 12000, 40000), PACK)
    except (SourceError, FileNotFoundError) as error:
        raise ToolError(str(error), code="source_not_found") from error


def get_atlas_source_manifest(slug: str) -> dict:
    """Which canonical documents exist for a type, with outline and sizes."""
    slug = _slug(slug)
    try:
        return source_manifest(slug, PACK)
    except (SourceError, FileNotFoundError) as error:
        raise ToolError(str(error), code="source_not_found") from error


# The read-only tool surface exposed to the Ask harness. Adding a write tool
# here would break the guarantee that this page cannot mutate the corpus, so
# the registry is deliberately explicit rather than discovered.
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "search_atlas",
            "description": (
                "Semantic search over the Atlas corpus of software application "
                "types (bilingual zh/en). Returns ranked types with similarity, "
                "the defining core, and related types. Call this first for any "
                "'what kind of software is X' or 'which types relate to Y' "
                "question."),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string",
                              "description": "Natural-language query, zh or en."},
                    "k": {"type": "integer", "minimum": 1, "maximum": MAX_SEARCH_K,
                          "description": "How many types to return (default 5)."},
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_leaf",
            "description": (
                "Full detail for one type given its slug: defining core, how it "
                "works, important rules, variants, representative products, "
                "sources, and typed relations to other types."),
            "parameters": {
                "type": "object",
                "properties": {"slug": {"type": "string"}},
                "required": ["slug"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_neighbors",
            "description": (
                "All typed relations of one type (sibling, overlaps, upstream, "
                "downstream, variant_of, ...) with the corpus's own boundary "
                "distinction text. Use to explain how two similar types differ."),
            "parameters": {
                "type": "object",
                "properties": {"slug": {"type": "string"}},
                "required": ["slug"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_section_tree",
            "description": (
                "The taxonomy of domains and sub-domains with type counts. Use "
                "when you need to locate where a topic sits or list a domain."),
            "parameters": {
                "type": "object",
                "properties": {
                    "depth": {"type": "integer", "minimum": 1, "maximum": 3,
                              "description": "1 = top-level domains only."},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_atlas_source",
            "description": (
                "Read the canonical Markdown of a type. Use for exact wording, "
                "full sections, or research notes. Paginated: if the result "
                "reports complete=false, continue from next_offset."),
            "parameters": {
                "type": "object",
                "properties": {
                    "slug": {"type": "string"},
                    "kind": {"type": "string", "enum": ["application", "research"],
                             "description": "Default application."},
                    "section": {"type": "string",
                                "description": "Optional outline id to read one subtree."},
                    "offset": {"type": "integer", "minimum": 0},
                    "limit": {"type": "integer", "minimum": 1, "maximum": 40000},
                },
                "required": ["slug"],
            },
        },
    },
]

# Dispatch table. A name not present here cannot be called, even if a model
# invents it.
TOOL_FUNCTIONS = {
    "search_atlas": search_atlas,
    "get_leaf": get_leaf,
    "get_neighbors": get_neighbors,
    "get_section_tree": get_section_tree,
    "read_atlas_source": read_atlas_source,
    "get_atlas_source_manifest": get_atlas_source_manifest,
}


def run_tool(name: str, arguments: dict) -> dict:
    """Execute one tool by name, never raising: failures become data.

    A tool error is information the model can act on (retry with a better
    slug, or say the corpus lacks the answer), so it is returned rather than
    propagated and allowed to abort the turn.
    """
    function = TOOL_FUNCTIONS.get(name)
    if function is None:
        return {"error": f"unknown tool {name!r}", "code": "unknown_tool"}
    if not isinstance(arguments, dict):
        return {"error": "arguments must be an object", "code": "bad_argument"}
    try:
        return function(**arguments)
    except ToolError as error:
        return {"error": str(error), "code": error.code}
    except TypeError as error:
        return {"error": f"invalid arguments: {error}", "code": "bad_argument"}
    except Exception as error:  # pragma: no cover - defensive
        return {"error": f"tool failed: {error}", "code": "tool_error"}
