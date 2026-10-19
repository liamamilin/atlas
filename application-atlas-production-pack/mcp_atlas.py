#!/usr/bin/env python3
"""Application Atlas MCP server.

Exposes the atlas corpus (software application types, bilingual, with relation
graph + vector search + classifier) as MCP tools. When launched with
``--atlas-read-only``, classification is disabled at the service layer.

The read-only queries delegate to ``atlas_tools``, which the Ask harness also
uses, so the corpus semantics stay identical across both entry points.
"""
import json
import sys

from mcp.server.fastmcp import FastMCP

import atlas_tools
from atlas_runtime import PACK as DATA_PACK

PACK = str(DATA_PACK)
READ_ONLY = "--atlas-read-only" in sys.argv[1:]

mcp = FastMCP("application-atlas")


def _dump(value) -> str:
    return json.dumps(value, ensure_ascii=False, indent=1)


@mcp.tool()
def search_atlas(query: str, k: int = 5) -> str:
    """Semantic search over the application type corpus (bilingual zh/en).
    Returns top-k types with similarity, Chinese name, defining core, and related types."""
    return _dump(atlas_tools.run_tool("search_atlas", {"query": query, "k": k}))


@mcp.tool()
def get_leaf(slug: str) -> str:
    """Get full detail of one application type: overview, defining core, how it
    works, important rules, variants, representative products, sources, and all
    typed relations to other types."""
    return _dump(atlas_tools.run_tool("get_leaf", {"slug": slug}))


@mcp.tool()
def read_atlas_source(slug: str, kind: str = "application", section: str = "",
                      offset: int = 0, limit: int = 12000) -> str:
    """Read canonical Atlas Markdown with fingerprint, line numbers, and
    explicit pagination. Use an outline id to read one heading subtree. If
    complete is false, continue from next_offset."""
    return _dump(atlas_tools.run_tool("read_atlas_source", {
        "slug": slug, "kind": kind, "section": section,
        "offset": offset, "limit": limit}))


@mcp.tool()
def get_atlas_source_manifest(slug: str) -> str:
    """List canonical application/research documents and outlines for a type."""
    return _dump(atlas_tools.run_tool(
        "get_atlas_source_manifest", {"slug": slug}))


@mcp.tool()
def classify_product(description: str) -> str:
    """Classify a software product (given a 1-3 sentence description, zh or en) into
    one of the atlas types. Returns the best-matching type slug with confidence
    scores for top candidates. Use when you need to know 'what kind of software is this'."""
    if READ_ONLY:
        return _dump({
            "error": "classification is disabled in Atlas read-only MCP mode"})
    import sys
    sys.path.insert(0, PACK)
    from classify import classify
    result = classify(description)
    top = sorted(result["scores"].items(), key=lambda pair: -pair[1])[:5]
    names = {item["slug"]: item["name_zh"] for item in result.get("detail") or []}
    return _dump({
        "choice": result["choice"],
        "candidates": [{"slug": slug, "name_zh": names.get(slug, "?"), "score": score}
                       for slug, score in top],
    })


@mcp.tool()
def get_section_tree() -> str:
    """Get the atlas directory tree: top-level domains and sub-domains with their
    id, name, parent, and type count. Use to browse the taxonomy."""
    return _dump(atlas_tools.run_tool("get_section_tree", {"depth": 3}))


@mcp.tool()
def get_neighbors(slug: str) -> str:
    """Get all typed relations of one application type to its neighbors
    (adjacent/sibling/upstream/downstream/overlaps etc.), each with the corpus's
    own boundary-distinction text. Use to understand how one type differs from its neighbors."""
    return _dump(atlas_tools.run_tool("get_neighbors", {"slug": slug}))


if __name__ == "__main__":
    mcp.run()
