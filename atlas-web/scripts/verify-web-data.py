#!/usr/bin/env python3
"""Verify that generated web data exactly matches the current Atlas SQLite source."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sqlite3

CODE_PACK = Path(__file__).resolve().parents[2] / "application-atlas-production-pack"
PACK = Path(os.environ.get("ATLAS_PACK", CODE_PACK)).resolve()
DB = PACK / "atlas" / "atlas.sqlite"
OUT = Path(os.environ.get(
    "ATLAS_WEB_OUT", Path(__file__).resolve().parents[1] / "public" / "data")).resolve()
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
MARKDOWN_FIELDS = (
    "full_md", "overview", "overview_zh", "dc", "dc_zh", "how", "how_zh",
    "rules", "rules_zh", "variants", "variants_zh", "products", "products_zh",
    "sources",
)


def relative_markdown_target(value: str) -> str | None:
    target = value.strip()
    if not target or target.startswith(("#", "/")) or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    path = target.split("#", 1)[0].split("?", 1)[0]
    filename = path.rsplit("/", 1)[-1]
    if not filename.lower().endswith(".md"):
        return None
    return filename[:-3]


def read_json(path: Path):
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> None:
    errors: list[str] = []
    if not DB.is_file():
        raise SystemExit(f"missing source database: {DB}")
    if not OUT.is_dir():
        raise SystemExit(f"missing generated data directory: {OUT}")

    uri = DB.as_uri() + "?mode=ro"
    with sqlite3.connect(uri, uri=True) as con:
        leaf_count = con.execute("SELECT count(*) FROM leaf").fetchone()[0]
        section_count = con.execute("SELECT count(*) FROM section").fetchone()[0]
        leaf_slugs = {row[0] for row in con.execute("SELECT slug FROM leaf")}
        leaf_names = {
            row[0]: {"name": row[1], "name_zh": row[2] or ""}
            for row in con.execute("SELECT slug, name, name_zh FROM leaf")
        }
        section_slugs = {
            row[0] for row in con.execute(
                "SELECT DISTINCT section_id FROM leaf WHERE section_id != ''")
        }
    app_sources = read_json(PACK / "mvp_apps.json")
    classified = {
        item["slug"]: item for item in read_json(PACK / "mvp_apps_classified.json")
    }
    app_count = len(app_sources)

    try:
        meta = read_json(OUT / "meta.json")
        apps = read_json(OUT / "apps.json")
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(f"invalid generated root data: {error}") from error

    for key, expected in {
        "leafCount": leaf_count,
        "sectionCount": section_count,
        "appCount": app_count,
    }.items():
        if meta.get(key) != expected:
            errors.append(f"meta.{key}={meta.get(key)!r}, expected {expected}")
    if len(apps) != app_count:
        errors.append(f"apps.json has {len(apps)} entries, expected {app_count}")
    app_slugs = [app.get("slug") for app in apps]
    if len(app_slugs) != len(set(app_slugs)):
        errors.append("apps.json contains duplicate slugs")
    for app in apps:
        slug = app.get("slug")
        leaf = app.get("leaf")
        source = classified.get(slug, {})
        if leaf and leaf not in leaf_slugs:
            errors.append(f"app {slug!r} points to missing leaf {leaf!r}")
        if leaf != source.get("leaf", ""):
            errors.append(f"app {slug!r} classification leaf does not match source record")
        if not isinstance(app.get("aliases", []), list):
            errors.append(f"app {slug!r} aliases must be a list")
        tasks = app.get("tasks", [])
        tasks_valid = isinstance(tasks, list) and all(isinstance(task, str) for task in tasks)
        task_count = len(tasks) if isinstance(tasks, list) else 0
        if not tasks_valid:
            errors.append(f"app {slug!r} tasks must be a string list")
        task_labels = app.get("taskLabels")
        if not isinstance(task_labels, dict) or set(task_labels) != {"zh", "en"}:
            errors.append(f"app {slug!r} taskLabels must contain zh and en")
        elif any(not isinstance(task_labels[lang], list) or len(task_labels[lang]) != task_count for lang in ("zh", "en")):
            errors.append(f"app {slug!r} taskLabels must align with tasks")
        for field in ("nameEn", "nameZh", "taglineEn", "leafNameEn", "leafNameZh"):
            if not isinstance(app.get(field), str) or not app[field].strip():
                errors.append(f"app {slug!r} missing bilingual field {field}")
        if leaf:
            expected = leaf_names.get(leaf, {})
            if app.get("leafNameEn") != (expected.get("name") or expected.get("name_zh", "")):
                errors.append(f"app {slug!r} leafNameEn does not match SQLite")
            if app.get("leafNameZh") != (expected.get("name_zh") or expected.get("name", "")):
                errors.append(f"app {slug!r} leafNameZh does not match SQLite")
        evidence = app.get("classificationEvidence")
        if not isinstance(evidence, dict):
            errors.append(f"app {slug!r} missing classificationEvidence")
        else:
            if evidence.get("source") != "mvp_apps_classified.json" or evidence.get("method") != "atlas-classification":
                errors.append(f"app {slug!r} classification provenance is incomplete")
            if evidence.get("sourceRef") != f"mvp_apps_classified.json#{slug}":
                errors.append(f"app {slug!r} classification sourceRef is invalid")
            if evidence.get("selectedLeaf") != leaf:
                errors.append(f"app {slug!r} classification evidence selects a different leaf")
            if not isinstance(evidence.get("scores"), list) or not evidence["scores"]:
                errors.append(f"app {slug!r} classification evidence has no scores")
            else:
                for score in evidence["scores"]:
                    if not isinstance(score, dict) or not isinstance(score.get("leaf"), str) or not isinstance(score.get("score"), (int, float)):
                        errors.append(f"app {slug!r} has malformed classification score")
                        break

    index_slugs = [item.get("slug") for item in meta.get("leafIndex", [])]
    if len(index_slugs) != len(set(index_slugs)):
        errors.append("meta.leafIndex contains duplicate slugs")
    if set(index_slugs) != leaf_slugs:
        missing = sorted(leaf_slugs - set(index_slugs))[:5]
        stale = sorted(set(index_slugs) - leaf_slugs)[:5]
        errors.append(f"leaf index mismatch; missing={missing}, stale={stale}")
    for item in meta.get("leafIndex", []):
        if not isinstance(item.get("aliases_zh", []), list):
            errors.append(f"leaf index {item.get('slug')!r} aliases_zh must be a list")

    leaf_dir = OUT / "leaves"
    section_dir = OUT / "sections"
    generated_leaf_slugs = {
        path.stem for path in leaf_dir.glob("*.json") if path.is_file()
    }
    generated_section_slugs = {
        path.stem for path in section_dir.glob("*.json") if path.is_file()
    }
    if generated_leaf_slugs != leaf_slugs:
        errors.append(
            "generated leaf files do not match SQLite; "
            f"missing={sorted(leaf_slugs - generated_leaf_slugs)[:5]}, "
            f"stale={sorted(generated_leaf_slugs - leaf_slugs)[:5]}")
    if generated_section_slugs != section_slugs:
        errors.append(
            "generated section files do not match SQLite; "
            f"missing={sorted(section_slugs - generated_section_slugs)[:5]}, "
            f"stale={sorted(generated_section_slugs - section_slugs)[:5]}")

    for slug in sorted(leaf_slugs):
        path = leaf_dir / f"{slug}.json"
        try:
            value = read_json(path)
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"invalid leaf file {path.name}: {error}")
            continue
        if value.get("slug") != slug:
            errors.append(f"leaf file {path.name} contains slug {value.get('slug')!r}")
        for field in MARKDOWN_FIELDS:
            for match in MARKDOWN_LINK_RE.finditer(str(value.get(field) or "")):
                target = relative_markdown_target(match.group(1))
                if target and target not in leaf_slugs:
                    errors.append(
                        f"leaf {slug} contains dead canonical Markdown link {match.group(1)!r}"
                    )
        relation_ids: set[str] = set()
        for relation in value.get("relations", []):
            target = relation.get("to")
            if target not in leaf_slugs:
                errors.append(f"leaf {slug} points to missing relation target {target!r}")
            if not isinstance(relation.get("toNameZh"), str) or not relation.get("toNameZh") or not isinstance(relation.get("toNameEn"), str) or not relation.get("toNameEn"):
                errors.append(f"leaf {slug} relation {relation.get('id')!r} lacks bilingual target labels")
            if not relation.get("kindLabelZh") or not relation.get("kindLabelEn"):
                errors.append(f"leaf {slug} relation {relation.get('id')!r} lacks bilingual kind labels")
            relation_id = relation.get("id")
            if not relation_id:
                errors.append(f"leaf {slug} has relation without stable id")
            elif relation_id in relation_ids:
                errors.append(f"leaf {slug} has duplicate relation id {relation_id!r}")
            relation_ids.add(relation_id or "")
    for slug in sorted(section_slugs):
        path = section_dir / f"{slug}.json"
        try:
            value = read_json(path)
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"invalid section file {path.name}: {error}")
            continue
        if value.get("id") != slug:
            errors.append(f"section file {path.name} contains id {value.get('id')!r}")

    if errors:
        raise SystemExit("web data verification failed:\n- " + "\n- ".join(errors))
    print(
        f"verified: {leaf_count} leaves, {section_count} sections, {app_count} apps; "
        "no missing or stale generated files")


if __name__ == "__main__":
    main()
