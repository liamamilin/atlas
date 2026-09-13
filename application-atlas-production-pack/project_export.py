"""Export an Atlas project as a self-contained Markdown development bundle."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
import uuid
import zipfile

from project_baseline import latest_project_baseline


DOCUMENT_ORDER = {
    "analysis": 10,
    "product-requirements": 20,
    "interaction": 30,
    "technical-plan": 40,
    "development-plan": 50,
    "acceptance-plan": 60,
    "current-state": 70,
}


def export_project(store, project_id: str) -> dict:
    project = store.get_project(project_id)
    references = store.list_references(project_id)
    requirements = store.list_requirements(project_id)
    decisions = store.list_decisions(project_id)
    documents = store.list_documents(project_id)
    baseline = latest_project_baseline(store, project_id)
    root = store.path.parent / "exports" / project_id
    root.mkdir(parents=True, exist_ok=True)
    name = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    temp = Path(tempfile.mkdtemp(prefix=".export-", dir=root))
    final = root / name
    archive = root / f"{name}.zip"
    temp_archive = root / f".{name}.zip.tmp"
    try:
        files = _build_files(
            project, references, requirements, decisions, documents, baseline)
        hashes = {}
        for relative, content in files.items():
            path = temp / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            hashes[relative] = hashlib.sha256(content.encode("utf-8")).hexdigest()
        manifest = {
            "schema": 2,
            "exported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "project_id": project_id,
            "project_updated_at": project["updated_at"],
            "counts": {
                "references": len(references), "requirements": len(requirements),
                "decisions": len(decisions), "documents": len(documents),
                "workspace_baselines": 1 if baseline else 0,
            },
            "workspace_baseline_id": baseline["id"] if baseline else None,
            "workspace_baseline_fingerprint": baseline["fingerprint"] if baseline else None,
            "unresolved_requirement_ids": [
                item["id"] for item in requirements if item["confirmed_scope"] is None],
            "documents_needing_review": [
                item["id"] for item in documents if item["review"]["status"] == "needs_review"],
            "files": hashes,
        }
        (temp / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        os.replace(temp, final)
        with zipfile.ZipFile(temp_archive, "w", zipfile.ZIP_DEFLATED) as bundle:
            for path in sorted(final.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(final))
        os.replace(temp_archive, archive)
    except BaseException:
        shutil.rmtree(temp, ignore_errors=True)
        shutil.rmtree(final, ignore_errors=True)
        temp_archive.unlink(missing_ok=True)
        archive.unlink(missing_ok=True)
        raise
    return {
        "project_id": project_id,
        "directory": str(final),
        "archive": str(archive),
        "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "manifest": manifest,
    }


def _build_files(project, references, requirements, decisions, documents, baseline=None):
    files = {}
    reference_links = []
    for index, reference in enumerate(references, 1):
        name = f"sources/{index:02d}-{_slug(reference['source_ref'])}-{reference['id'][-8:]}.md"
        files[name] = _reference_markdown(reference)
        reference_links.append((reference, name))
    document_links = []
    ordered_documents = sorted(
        documents, key=lambda item: (DOCUMENT_ORDER.get(item["kind"], 999), item["title"], item["id"]))
    for index, document in enumerate(ordered_documents, 1):
        name = f"documents/{index:02d}-{_slug(document['kind'])}-{document['id'][-8:]}.md"
        files[name] = _document_markdown(document)
        document_links.append((document, name))
    files["requirements.md"] = _requirements_markdown(requirements)
    files["decisions.md"] = _decisions_markdown(decisions)
    files["sources.md"] = _sources_index(reference_links)
    if baseline:
        files["workspace-baseline.md"] = _baseline_markdown(baseline)
        files["workspace-baseline.json"] = json.dumps(
            baseline, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    files["INDEX.md"] = _index_markdown(
        project, reference_links, document_links, requirements, decisions, baseline)
    return files


def _index_markdown(project, reference_links, document_links, requirements, decisions,
                    baseline=None):
    unresolved = [item for item in requirements if item["confirmed_scope"] is None]
    review = [item for item, _ in document_links if item["review"]["status"] == "needs_review"]
    lines = [
        f"# {project['name']}", "", project["objective"], "", "## Project", "",
        f"- ID: `{project['id']}`", f"- Mode: `{project['mode']}`",
        f"- Workspace: `{project['workspace']}`", f"- Updated: `{project['updated_at']}`",
        "", "## Documents", "",
    ]
    lines.extend(
        f"- [{item['title']}]({path}) — `{item['kind']}` v{item['current_version']} · "
        f"{item['author']} · {item['review']['status']}"
        for item, path in document_links)
    if not document_links:
        lines.append("- No documents")
    lines.extend(["", "## Project knowledge", "",
                  f"- [Requirements](requirements.md): {len(requirements)}",
                  f"- [Decisions](decisions.md): {len(decisions)}",
                  f"- [Sources](sources.md): {len(reference_links)}", "",
                  "## Open review", ""])
    if baseline:
        lines.insert(lines.index("## Open review") - 1,
                     f"- [Workspace baseline](workspace-baseline.md): `{baseline['id']}`")
    lines.extend(f"- Unconfirmed requirement `{item['id']}`: {item['content']}" for item in unresolved)
    lines.extend(f"- Document needs review `{item['id']}`: {item['title']}" for item in review)
    if not unresolved and not review:
        lines.append("- No unresolved requirements or stale document dependencies")
    return "\n".join(lines) + "\n"


def _document_markdown(item):
    basis = ", ".join(
        f"{entry.get('kind', 'external')}:{entry.get('id') or entry.get('source')}"
        for entry in item["basis"]) or "none"
    header = [
        f"<!-- atlas-document-id: {item['id']} -->",
        f"<!-- atlas-version-id: {item['version_id']} -->",
        f"<!-- version: {item['current_version']} -->",
        f"<!-- author: {item['author']} -->",
        f"<!-- review-status: {item['review']['status']} -->",
        f"<!-- basis: {basis} -->", "",
    ]
    return "\n".join(header) + item["content"].rstrip() + "\n"


def _reference_markdown(item):
    lines = [
        f"# Source: {item['source_ref']}", "",
        f"- Reference ID: `{item['id']}`", f"- Kind: `{item['source_kind']}`",
        f"- Source version: `{item['source_version']}`",
        f"- Locator: `{item['locator'] or 'full document'}`",
        f"- Read status: `{item['read_status']}`", "",
        "## Project note", "", item["note"] or "No project note.", "",
        "## Fixed excerpt", "", item["excerpt"].rstrip(), "",
    ]
    return "\n".join(lines)


def _baseline_markdown(item):
    manifest = item["manifest"]
    header = [
        "# Accepted workspace baseline", "",
        f"- Baseline ID: `{item['id']}`",
        f"- Record fingerprint: `{item['fingerprint']}`",
        f"- Captured: `{item['created_at']}`",
        f"- Full evidence manifest: [workspace-baseline.json](workspace-baseline.json)", "",
    ]
    return "\n".join(header) + manifest.get("report_markdown", "").rstrip() + "\n"


def _sources_index(links):
    lines = ["# Source index", ""]
    lines.extend(
        f"- [{item['source_ref']}]({path}) — `{item['source_kind']}` · "
        f"`{item['source_version'][:12]}` · {item['read_status']}"
        for item, path in links)
    if not links:
        lines.append("- No sources")
    return "\n".join(lines) + "\n"


def _requirements_markdown(items):
    lines = ["# Requirements", ""]
    for item in items:
        lines.extend([
            f"## {item['id']}", "", item["content"], "",
            f"- AI recommendation: `{item['recommended_scope'] or 'none'}` — "
            f"{item['recommendation_reason'] or 'No recommendation reason.'}",
            f"- User confirmation: `{item['confirmed_scope'] or 'pending'}` — "
            f"{item['confirmation_reason'] or 'Not confirmed.'}",
            f"- Source references: {', '.join(item['reference_ids']) or 'none'}", "",
            "### Acceptance conditions", "",
        ])
        lines.extend(f"- {condition}" for condition in item["acceptance_conditions"])
        if not item["acceptance_conditions"]:
            lines.append("- None recorded")
        lines.append("")
    if not items:
        lines.append("No requirements.\n")
    return "\n".join(lines)


def _decisions_markdown(items):
    lines = ["# Decisions", ""]
    for item in items:
        lines.extend([
            f"## {item['id']} · {item['statement']}", "", item["rationale"], "",
            f"Sources: {', '.join(item['reference_ids']) or 'none'}", "",
        ])
    if not items:
        lines.append("No decisions.\n")
    return "\n".join(lines)


def _slug(value):
    value = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return value[:48] or "item"
