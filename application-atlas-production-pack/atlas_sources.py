"""Read canonical Atlas Markdown without silently truncating the source.

The SQLite export is useful for search and summaries, but it is not the evidence
boundary for U17. This module returns source metadata, heading-scoped content,
and explicit pagination information from the canonical Markdown files.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
from pathlib import Path
import re

from atlas_runtime import PACK


SOURCE_DIRS = {"application": "applications", "research": "research"}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$", re.MULTILINE)
DEFAULT_LIMIT = 12_000
MAX_LIMIT = 50_000


class SourceError(ValueError):
    """Invalid source request."""


@dataclass(frozen=True)
class Heading:
    id: str
    title: str
    level: int
    line: int
    start: int
    end: int


def _heading_id(title: str) -> str:
    value = re.sub(r"[^\w\u4e00-\u9fff]+", "-", title.lower(), flags=re.UNICODE)
    return value.strip("-") or "section"


def _outline(text: str) -> list[Heading]:
    matches = list(HEADING_RE.finditer(text))
    counts: dict[str, int] = {}
    headings: list[Heading] = []
    for index, match in enumerate(matches):
        level = len(match.group(1))
        title = match.group(2).strip()
        base = _heading_id(title)
        counts[base] = counts.get(base, 0) + 1
        heading_id = base if counts[base] == 1 else f"{base}-{counts[base]}"
        end = len(text)
        for later in matches[index + 1:]:
            if len(later.group(1)) <= level:
                end = later.start()
                break
        headings.append(Heading(
            id=heading_id,
            title=title,
            level=level,
            line=text.count("\n", 0, match.start()) + 1,
            start=match.start(),
            end=end,
        ))
    return headings


def _heading_dict(heading: Heading | None) -> dict | None:
    if heading is None:
        return None
    return {"id": heading.id, "title": heading.title, "level": heading.level,
            "line": heading.line, "chars": heading.end - heading.start}


def _source_path(slug: str, kind: str, pack: str | Path) -> Path:
    if kind not in SOURCE_DIRS:
        raise SourceError(f"unknown source kind: {kind}")
    if not SLUG_RE.fullmatch(slug):
        raise SourceError("invalid slug")
    root = (Path(pack).resolve() / SOURCE_DIRS[kind]).resolve()
    path = (root / f"{slug}.md").resolve()
    if path.parent != root:
        raise SourceError("invalid source path")
    return path


def source_manifest(slug: str, pack: str | Path = PACK) -> dict:
    """Describe which canonical documents exist for a leaf."""
    if not SLUG_RE.fullmatch(slug):
        raise SourceError("invalid slug")
    sources = []
    for kind in SOURCE_DIRS:
        path = _source_path(slug, kind, pack)
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        sources.append({
            "kind": kind,
            "chars": len(text),
            "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
            "fingerprint": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "outline": [_heading_dict(item) for item in _outline(text)],
        })
    if not sources:
        raise FileNotFoundError(slug)
    return {"slug": slug, "sources": sources}


def read_source(slug: str, kind: str, section: str | None = None,
                offset: int = 0, limit: int = DEFAULT_LIMIT,
                pack: str | Path = PACK) -> dict:
    """Read a whole document or one heading subtree with explicit pagination."""
    if offset < 0:
        raise SourceError("offset must be non-negative")
    if limit < 1:
        raise SourceError("limit must be positive")
    limit = min(limit, MAX_LIMIT)
    path = _source_path(slug, kind, pack)
    if not path.is_file():
        raise FileNotFoundError(f"{kind}/{slug}")

    text = path.read_text(encoding="utf-8")
    headings = _outline(text)
    selected = None
    scope_start, scope_end = 0, len(text)
    if section:
        normalized = section.casefold().strip()
        selected = next((item for item in headings if item.id == section), None)
        if selected is None:
            candidates = [item for item in headings if item.title.casefold() == normalized]
            if len(candidates) != 1:
                raise SourceError("section not found or ambiguous; use an outline id")
            selected = candidates[0]
        scope_start, scope_end = selected.start, selected.end

    scope_length = scope_end - scope_start
    if offset > scope_length:
        raise SourceError("offset exceeds selected content")
    chunk_start = scope_start + offset
    chunk_end = min(scope_end, chunk_start + limit)
    content = text[chunk_start:chunk_end]
    line_start = text.count("\n", 0, chunk_start) + 1
    complete = chunk_end >= scope_end
    return {
        "slug": slug,
        "kind": kind,
        "fingerprint": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "document_chars": len(text),
        "document_lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "section": _heading_dict(selected),
        "offset": offset,
        "limit": limit,
        "returned_chars": len(content),
        "selected_chars": scope_length,
        "line_start": line_start,
        "line_end": line_start + content.count("\n"),
        "complete": complete,
        "next_offset": None if complete else offset + len(content),
        "content": content,
        "outline": [_heading_dict(item) for item in headings],
    }
