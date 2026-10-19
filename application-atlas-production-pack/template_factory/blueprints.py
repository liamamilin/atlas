"""Cognitive packages: validate data, freeze and export. Never execute package code."""

from __future__ import annotations

import base64
import binascii
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import stat
import tempfile
from urllib.parse import urlsplit
import zipfile

from atlas_runtime import atomic_json
from .artifacts import archive_tree, copy_tree, relative, tree_manifest
from .handoff import write_handoff
from .store import FactoryError, canonical, digest, now, text, uid

KIND = "product-blueprint"
SCHEMA = "atlas.product-blueprint.v0"
# Fits the shared 2 MiB JSON request boundary after base64 encoding.
MAX_ARCHIVE = 1024 * 1024
MAX_EXPANDED = 8 * 1024 * 1024
MAX_ENTRIES = 512
DOCUMENTS = (
    "README.md",
    "CATEGORY.md",
    "PRODUCT.md",
    "ARCHITECTURE.md",
    "DECISIONS.md",
    "ROADMAP.md",
    "AGENT.md",
    "VALIDATION.md",
)
REQUIRED = {
    *DOCUMENTS,
    "template.json",
    "integrity.json",
    "inputs/scenario.json",
    "acceptance/plan.json",
    "acceptance/README.md",
}


def is_blueprint(value):
    return value.get("artifact_type", "runnable-starter") == KIND


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _invalid_constant(value):
    raise ValueError("non-finite JSON number")


def read_json(path):
    try:
        return json.loads(
            Path(path).read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_invalid_constant,
        )
    except (ValueError, UnicodeError, OSError, RecursionError) as error:
        raise FactoryError("invalid blueprint JSON: " + Path(path).name) from error


def _items(value, key):
    rows = value.get(key)
    if (
        not isinstance(rows, list)
        or not rows
        or not all(isinstance(r, dict) for r in rows)
    ):
        raise FactoryError("blueprint needs non-empty " + key)
    result = {}
    for row in rows:
        identifier = text(row.get("id"), key + " id", 200)
        if identifier in result:
            raise FactoryError("duplicate blueprint " + key + " id")
        result[identifier] = row
    return result


def _refs(value, allowed, label):
    if (
        not isinstance(value, list)
        or not all(isinstance(x, str) for x in value)
        or len(set(value)) != len(value)
        or not set(value) <= set(allowed)
    ):
        raise FactoryError("invalid blueprint references: " + label)
    return set(value)


def _source_url(value, source):
    value = text(value, "source URL", 4000)
    try:
        parsed = urlsplit(value)
    except ValueError as error:
        raise FactoryError("invalid source URL") from error
    if parsed.scheme or parsed.netloc:
        if (
            parsed.scheme not in {"http", "https"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
        ):
            raise FactoryError("source URL must be HTTP(S) without credentials")
    elif not (source / relative(value)).is_file():
        raise FactoryError("local source reference is missing")


def validate_acceptance_manifest(source):
    path = Path(source) / "acceptance/package.json"
    if not path.is_file():
        return
    value = read_json(path)
    if not isinstance(value, dict):
        raise FactoryError("acceptance/package.json must be an object")
    for field in ("scripts", "dependencies", "devDependencies"):
        rows = value.get(field, {})
        if not isinstance(rows, dict) or not all(
            isinstance(k, str) and isinstance(v, str) and v.strip()
            for k, v in rows.items()
        ):
            raise FactoryError("invalid acceptance/package.json " + field)


def validate_blueprint(source):
    source = Path(source)
    files = tree_manifest(source)
    if not REQUIRED <= files.keys():
        raise FactoryError("blueprint is missing required documents or metadata")
    validate_acceptance_manifest(source)
    spec = read_json(source / "template.json")
    if isinstance(spec, dict) and spec.get("factory_policy") == "atlas.factory-v1.1":
        basis = spec.get("case_basis")
        if not isinstance(basis, dict) or digest({k: v for k, v in basis.items() if k != "basis_digest"}) != basis.get("basis_digest"):
            raise FactoryError("fixed case basis digest differs", "evidence_basis_invalid", 409)
        if basis.get("scenario_id") != spec.get("scenario", {}).get("id") or basis.get("scenario_revision") != spec.get("scenario", {}).get("revision"):
            raise FactoryError("case basis is bound to another scenario", "evidence_basis_invalid", 409)
        if read_json(source / "inputs/case-basis.json") != basis:
            raise FactoryError("case basis and normative input differ", "evidence_basis_invalid", 409)
        facts_view = spec.get("case_facts_view")
        if facts_view is not None:
            if (
                not isinstance(facts_view, dict)
                or facts_view.get("schema") != "atlas.accepted-case-facts.v1"
                or facts_view.get("basis_digest") != basis.get("basis_digest")
                or digest({key: value for key, value in facts_view.items() if key != "view_digest"}) != facts_view.get("view_digest")
                or read_json(source / "inputs/accepted-case-facts.json") != facts_view
            ):
                raise FactoryError("accepted case facts view digest or mirror differs", "case_facts_view_invalid", 409)
            if facts_view.get("status") == "accepted":
                facts = facts_view.get("facts")
                if not isinstance(facts, list) or not facts or any(
                    not isinstance(item, dict) or not isinstance(item.get("evidence_id"), str)
                    for item in facts
                ):
                    raise FactoryError("accepted case facts must contain observation objects", "case_facts_view_invalid", 409)
                ids = [item["evidence_id"] for item in facts]
                if sorted(ids) != facts_view.get("accepted_evidence_ids") or not isinstance(facts_view.get("source_research_digest"), str):
                    raise FactoryError("accepted case facts view contents are invalid", "case_facts_view_invalid", 409)
            elif facts_view.get("status") != "legacy_all_accepted":
                raise FactoryError("accepted case facts view status is invalid", "case_facts_view_invalid", 409)
        for choice in spec.get("case_design", []):
            if not set(choice.get("evidence_ids", [])) <= set(basis.get("evidence_ids", [])):
                raise FactoryError("case design references unknown evidence", "evidence_basis_invalid", 409)
    if (
        not isinstance(spec, dict)
        or spec.get("schema") != SCHEMA
        or spec.get("kind") != KIND
    ):
        raise FactoryError("unsupported cognitive blueprint schema")
    for field in ("id", "version", "title", "architecture_markdown"):
        text(
            spec.get(field),
            "blueprint " + field,
            100_000 if field == "architecture_markdown" else 1000,
        )
    inventory = read_json(source / "integrity.json")
    actual = {key: value for key, value in files.items() if key != "integrity.json"}
    if (
        not isinstance(inventory, dict)
        or inventory.get("template_version") != spec["version"]
        or inventory.get("sha256") != actual
    ):
        raise FactoryError(
            "blueprint file inventory differs from its declared hashes",
            "artifact_changed",
            409,
        )
    scenario = spec.get("scenario")
    if (
        not isinstance(scenario, dict)
        or (scenario.get("status") != "ready" and not (
            scenario.get("status") == "draft" and spec.get("factory_policy") == "atlas.factory-v1.1"
            and spec.get("admission", {}).get("kind") == "batch_policy"
            and spec.get("admission", {}).get("revision") == scenario.get("revision")
            and spec.get("admission", {}).get("review_id")
        ))
        or type(scenario.get("revision")) is not int
        or scenario["revision"] < 1
        or read_json(source / "inputs/scenario.json") != scenario
    ):
        raise FactoryError("blueprint needs the pinned confirmed scenario input")
    for field in ("id", "leaf", "name", "audience", "objective"):
        text(scenario.get(field), "scenario " + field)
    for field in ("workflow", "acceptance"):
        if not isinstance(scenario.get(field), list) or not scenario[field]:
            raise FactoryError("scenario needs " + field)
        for item in scenario[field]:
            text(item, "scenario " + field)
    groups = {
        key: _items(spec, key)
        for key in ("sources", "roles", "features", "decisions", "phases", "acceptance")
    }
    phase_order = {
        identifier: index for index, identifier in enumerate(groups["phases"])
    }
    for row in groups["sources"].values():
        for field in ("name", "version", "facts", "license", "reuse"):
            text(row.get(field), "source " + field, 20_000)
        _source_url(row.get("url"), source)
        if row.get("license_url"):
            _source_url(row["license_url"], source)
    for row in groups["roles"].values():
        for field in ("name", "responsibility"):
            text(row.get(field), "role " + field)
    for row in groups["decisions"].values():
        for field in ("question", "default", "when_to_ask", "impact", "status"):
            text(row.get(field), "decision " + field, 20_000)
    for row in groups["acceptance"].values():
        _refs(row.get("features"), groups["features"], "acceptance features")
    for row in groups["features"].values():
        for field in ("name", "applicability", "reason"):
            text(row.get(field), "feature " + field, 20_000)
        _refs(row.get("sources"), groups["sources"], "feature sources")
        cases = _refs(row.get("acceptance"), groups["acceptance"], "feature acceptance")
        phase = row.get("phase")
        if phase is not None and not isinstance(phase, str):
            raise FactoryError("invalid feature phase")
        if (phase and (phase not in groups["phases"] or not cases)) or (
            not phase and cases
        ):
            raise FactoryError("feature phase and acceptance must agree")
        for case in cases:
            if row["id"] not in groups["acceptance"][case].get("features", []):
                raise FactoryError("feature/case mapping must be bidirectional")
        if phase and not any(
            groups["acceptance"][case].get("phase") == phase for case in cases
        ):
            raise FactoryError("feature needs acceptance in its introduction phase")
    for row in groups["acceptance"].values():
        text(row.get("goal"), "acceptance goal", 20_000)
        features = _refs(row.get("features"), groups["features"], "acceptance features")
        if (
            not features
            or not isinstance(row.get("phase"), str)
            or row["phase"] not in groups["phases"]
        ):
            raise FactoryError("acceptance needs a phase and features")
        if not isinstance(row.get("type"), str) or row["type"] not in {
            "positive",
            "negative",
        }:
            raise FactoryError("acceptance type must be positive or negative")
        implementation = relative(row.get("implementation"))
        if (
            implementation not in files
            or Path(implementation).suffix
            not in {".py", ".js", ".cjs", ".mjs", ".ts", ".sh"}
            or not (source / implementation).stat().st_size
        ):
            raise FactoryError("acceptance implementation is missing")
        for feature in features:
            match = groups["features"][feature]
            if row["id"] not in match["acceptance"]:
                raise FactoryError("acceptance phase/feature mapping differs")
            if (
                match.get("phase") not in phase_order
                or phase_order[row["phase"]] < phase_order[match["phase"]]
            ):
                raise FactoryError(
                    "acceptance cannot depend on a future or unphased feature"
                )
    for row in groups["phases"].values():
        for field in ("title", "goal"):
            text(row.get(field), "phase " + field, 20_000)
        for key in ("features", "acceptance"):
            refs = _refs(row.get(key), groups[key], "phase " + key)
            if not refs or refs != {
                r["id"] for r in groups[key].values() if r.get("phase") == row["id"]
            }:
                raise FactoryError("phase mapping is incomplete")
    plan = read_json(source / "acceptance/plan.json")
    if (
        not isinstance(plan, dict)
        or plan.get("template_id") != spec["id"]
        or plan.get("cases") != spec["acceptance"]
        or plan.get("phases") != spec["phases"]
    ):
        raise FactoryError("acceptance plan and normative blueprint differ")
    evidence = spec.get("evidence", [])
    if not isinstance(evidence, list):
        raise FactoryError("invalid blueprint evidence")
    for record in evidence:
        if not isinstance(record, dict) or relative(record.get("path")) not in files:
            raise FactoryError("blueprint evidence file is missing")
    for name in DOCUMENTS:
        try:
            text((source / name).read_text(), "blueprint document", 1_000_000)
        except UnicodeError as error:
            raise FactoryError("blueprint documents must be UTF-8 text") from error
    manifest = {
        "artifact_type": KIND,
        "schema": SCHEMA,
        "name": spec["title"],
        "version": spec["version"],
        "description": scenario["objective"],
        "feature_count": len(groups["features"]),
        "decision_count": len(groups["decisions"]),
        "phase_count": len(groups["phases"]),
        "phases": [{"id": row["id"], "title": row["title"]} for row in spec["phases"]],
        "acceptance_count": len(groups["acceptance"]),
    }
    if (source / "acceptance/runner.json").exists():
        from .blueprint_runtime import validate_runner_manifest

        validate_runner_manifest(source, spec)
    return spec, manifest


def unpack_archive(data, destination):
    if not isinstance(data, bytes) or not 0 < len(data) <= MAX_ARCHIVE:
        raise FactoryError(
            "blueprint ZIP must be at most 1 MiB", "invalid_blueprint_archive"
        )
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            entries = archive.infolist()
            if len(entries) > MAX_ENTRIES:
                raise FactoryError("too many blueprint archive entries")
            names, total = set(), 0
            for entry in entries:
                name = relative(
                    entry.filename.rstrip("/") if entry.is_dir() else entry.filename
                )
                mode = entry.external_attr >> 16
                if (
                    name in names
                    or (stat.S_IFMT(mode) not in {0, stat.S_IFREG, stat.S_IFDIR})
                    or entry.flag_bits & 1
                ):
                    raise FactoryError("duplicate, encrypted or special archive entry")
                names.add(name)
                total += entry.file_size
                if total > MAX_EXPANDED or entry.file_size < 0:
                    raise FactoryError("expanded blueprint exceeds 8 MiB")
            # All names/sizes checked before any extraction; never use extractall.
            for entry in entries:
                if entry.is_dir():
                    continue
                content = archive.read(entry)
                if len(content) != entry.file_size:
                    raise FactoryError("invalid blueprint entry size")
                target = Path(destination) / entry.filename
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    except (zipfile.BadZipFile, RuntimeError, NotImplementedError, OSError) as error:
        raise FactoryError(
            "invalid blueprint ZIP", "invalid_blueprint_archive"
        ) from error


def freeze_blueprint(source, target, provenance, *, existing_target=False):
    """Host-owned freeze, shared by imported and generated cognition packages."""
    spec, manifest = validate_blueprint(source)
    target = Path(target)
    if not existing_target:
        target.mkdir(parents=True, exist_ok=False)
    copy_tree(source, target / "source")
    frozen = {
        "source": tree_manifest(target / "source"),
        "manifest": manifest,
        "plan": {"profile": KIND, "phases": spec["phases"]},
        "provenance": provenance,
    }
    for name in ("manifest", "plan", "provenance"):
        atomic_json(target / (name + ".json"), frozen[name])
    fingerprint = digest(frozen)
    atomic_json(target / "inventory.json", {"digest": fingerprint})
    return {
        "digest": fingerprint,
        **{key: frozen[key] for key in ("manifest", "plan", "provenance")},
    }


def import_blueprint(store, data, origin="imported-blueprint"):
    with tempfile.TemporaryDirectory(dir=store.root) as temporary:
        source = Path(temporary) / "input"
        source.mkdir()
        unpack_archive(data, source)
        spec, manifest = validate_blueprint(source)
        leaf = store.leaf(spec["scenario"]["leaf"])
        package_digest = digest(tree_manifest(source))
        target = None
        try:
            with store.connect(True) as con:
                previous = con.execute(
                    "SELECT id FROM artifact WHERE json_extract(body,'$.artifact_type')=? AND json_extract(body,'$.package_digest')=?",
                    (KIND, package_digest),
                ).fetchone()
                if previous:
                    return next(a for a in store.artifacts() if a["id"] == previous[0])
                artifact_id, job_id, batch_id, at = (
                    uid("tpl"),
                    uid("job"),
                    uid("bat"),
                    now(),
                )
                target = store.root / "artifacts" / artifact_id
                target.parent.mkdir(exist_ok=True)
                target.mkdir()
                provenance = {
                    "origin": origin,
                    "scenario": spec["scenario"],
                    "package_digest": package_digest,
                    "note": "Imported declarations and evidence are not factory acceptance; no code or model executed.",
                }
                if spec.get("factory_policy") == "atlas.factory-v1.1":
                    provenance["case_basis"] = spec.get("case_basis")
                    if spec.get("case_facts_view") is not None:
                        provenance["case_facts_view"] = spec["case_facts_view"]
                frozen_result = freeze_blueprint(
                    source, target, provenance, existing_target=True
                )
                plan, fingerprint = frozen_result["plan"], frozen_result["digest"]
                archive = target.parent / (artifact_id + ".zip")
                archive_tree(target / "source", archive)
                body = {
                    "artifact_type": KIND,
                    "package_digest": package_digest,
                    "job_id": job_id,
                    "leaf": leaf["slug"],
                    "scenario_name": spec["scenario"]["name"],
                    "scenario_revision": spec["scenario"]["revision"],
                    "created_at": at,
                    "digest": fingerprint,
                    "manifest": manifest,
                    "plan": plan,
                    "provenance": provenance,
                    "bundle_path": target.relative_to(store.root).as_posix(),
                    "archive_path": archive.relative_to(store.root).as_posix(),
                    "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                    "formal_checks": [
                        {
                            "passed": True,
                            "scope": "Structure, references, stage/case mapping and declared hashes only; no code executed.",
                        }
                    ],
                    "reports": [],
                }
                config = {
                    "kind": "blueprint-import",
                    "name": spec["title"],
                    "model": "",
                    "concurrency": 1,
                    "timeout": 0,
                    "repair_attempts": 0,
                }
                snapshot = {
                    "leaf": leaf,
                    "scenario": spec["scenario"],
                    "config": config,
                }
                con.execute(
                    "INSERT INTO batch VALUES(?,?,?,?)",
                    (batch_id, "completed", canonical(config), at),
                )
                con.execute(
                    "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        job_id,
                        batch_id,
                        "blueprint-import",
                        "completed",
                        "freeze",
                        1,
                        None,
                        None,
                        canonical(snapshot),
                        None,
                        at,
                        at,
                    ),
                )
                con.execute(
                    "INSERT INTO artifact VALUES(?,?,?,?,?,?,?)",
                    (
                        artifact_id,
                        job_id,
                        fingerprint,
                        "L0",
                        "draft",
                        canonical(body),
                        at,
                    ),
                )
                con.execute(
                    "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                    (
                        job_id,
                        1,
                        at,
                        "freeze",
                        "Imported cognition candidate; structural checks only, no execution or publication.",
                    ),
                )
        except BaseException:
            if target:
                shutil.rmtree(target, ignore_errors=True)
                target.with_suffix(".zip").unlink(missing_ok=True)
            raise
    return next(a for a in store.artifacts() if a["id"] == artifact_id)


def decode_archive(value):
    if not isinstance(value, str) or len(value) > ((MAX_ARCHIVE + 2) // 3) * 4:
        raise FactoryError("blueprint ZIP must be at most 1 MiB")
    try:
        return base64.b64decode(value, validate=True)
    except (ValueError, binascii.Error) as error:
        raise FactoryError("blueprint archive is not valid base64") from error


def verify_frozen(bundle, expected_digest):
    bundle = Path(bundle)
    spec, manifest = validate_blueprint(bundle / "source")
    frozen = {
        "source": tree_manifest(bundle / "source"),
        **{
            name: read_json(bundle / (name + ".json"))
            for name in ("manifest", "plan", "provenance")
        },
    }
    if (
        digest(frozen) != expected_digest
        or read_json(bundle / "inventory.json") != {"digest": expected_digest}
        or frozen["manifest"] != manifest
    ):
        raise FactoryError("blueprint changed after freezing", "artifact_changed", 409)
    view = spec.get("case_facts_view")
    if view is not None and frozen["provenance"].get("case_facts_view") != view:
        raise FactoryError("accepted case facts provenance differs from frozen specification", "case_facts_view_invalid", 409)
    return spec


def export_development(bundle, expected_digest, destination, project_name, phase=None):
    if not isinstance(project_name, str) or not re.fullmatch(
        r"[a-z][a-z0-9-]{0,62}", project_name
    ):
        raise FactoryError(
            "project_name must be a lowercase name using letters, digits and hyphens"
        )
    spec = verify_frozen(bundle, expected_digest)
    phase = spec["phases"][0]["id"] if phase is None else phase
    if not isinstance(phase, str) or phase not in {
        item["id"] for item in spec["phases"]
    }:
        raise FactoryError("choose a phase declared in the blueprint")
    destination = Path(destination)
    destination.mkdir(exist_ok=False)
    copy_tree(Path(bundle) / "source", destination / "blueprint")
    atomic_json(
        destination / "PROJECT_DECISIONS.json",
        {
            "project_name": project_name,
            "phase": phase,
            "template_digest": expected_digest,
            "choices": [
                {"id": d["id"], "default": d["default"], "choice": None}
                for d in spec["decisions"]
            ],
        },
    )
    write_handoff(destination, spec, phase, project_name, expected_digest)
    atomic_json(
        destination / ".atlas-blueprint.json",
        {
            "schema": 1,
            "artifact_type": KIND,
            "template_digest": expected_digest,
            "phase": phase,
            "project_name": project_name,
        },
    )
    return {
        "phase": phase,
        "project_name": project_name,
        "template_digest": expected_digest,
        "views": {
            "knowledge": "KNOWLEDGE.md",
            "execution": "HANDOFF.md",
            "acceptance": "ACCEPTANCE_CONTRACT.json",
        },
        "acceptance_contract_path": "ACCEPTANCE_CONTRACT.json",
        "acceptance_contract_schema": "atlas.acceptance-contract.v1",
    }
