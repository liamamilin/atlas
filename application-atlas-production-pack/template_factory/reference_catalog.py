"""Immutable catalog for independently reviewed ProductReference packages.

Imports are host-only: callers provide a path to a generated freeze together
with its pilot/revision identity. This module verifies that identity against
the factory ledger before copying the package into the read-only catalog.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sqlite3
import sys
import tempfile
import zipfile
from contextlib import contextmanager

from .product_reference import render_reference, select_scope, validate_reference
from .store import FactoryError, canonical, digest, now

_HEX = re.compile(r"^[0-9a-f]{64}$")
_LEAF = re.compile(r"^[a-z0-9][a-z0-9-]{0,199}$")
_REVISION = re.compile(r"^r[2-9][0-9]*$")
_MAX_ARCHIVE = 4 * 1024 * 1024
_MAX_UNPACKED = 24 * 1024 * 1024
_MAX_FILES = 256


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _safe_rel(value, field):
    if (not isinstance(value, str) or "\\" in value or not value
            or PurePosixPath(value).is_absolute()
            or any(part in {"", ".", ".."} for part in PurePosixPath(value).parts)):
        raise FactoryError(f"{field} must be a safe relative POSIX path", "reference_import", 400)
    return PurePosixPath(value)


def _read_json_bytes(data, field):
    try:
        value = json.loads(data)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise FactoryError(f"{field} is not valid UTF-8 JSON", "reference_import", 400) from error
    if not isinstance(value, dict):
        raise FactoryError(f"{field} must be an object", "reference_import", 400)
    return value


def _require_file(root: Path, relative: str, field: str) -> Path:
    rel = _safe_rel(relative, field)
    root = root.resolve(strict=True)
    path = root.joinpath(*rel.parts)
    current = root
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            raise FactoryError(f"{field} path contains a symlink", "reference_import_provenance", 409)
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError) as error:
        raise FactoryError(f"{field} path is missing or escapes its root", "reference_import_provenance", 409) from error
    if not resolved.is_file():
        raise FactoryError(f"{field} must be a regular file", "reference_import_provenance", 409)
    return resolved


def _tree_digest(root: Path) -> str:
    if root.is_symlink() or not root.is_dir():
        raise FactoryError("official research checkpoint is unavailable", "reference_import_provenance", 409)
    values = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise FactoryError("official research checkpoint contains a symlink", "reference_import_provenance", 409)
        if path.is_file():
            values[path.relative_to(root).as_posix()] = _sha(path.read_bytes())
    return digest(values)


def _official_review_context(generation, review_request, review_result, session_id):
    checkpoint = generation.parent / "official-checkpoints/review"
    source_root = _require_directory(checkpoint, "source", "official review source")
    snapshot_path = _require_file(source_root, "snapshot.json", "official review snapshot")

    def source_files(directory):
        values = {}
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise FactoryError("official review source contains a symlink", "reference_import_provenance", 409)
            if path.is_file():
                values[path.relative_to(directory).as_posix()] = path.read_text(encoding="utf-8")
        return values

    snapshot = _read_json_bytes(snapshot_path.read_bytes(), "official review snapshot")
    upstream_root = source_root / "upstream"
    review_root = source_root / "review"
    if not upstream_root.is_dir() or not review_root.is_dir():
        raise FactoryError("official review source tree is incomplete", "reference_import_provenance", 409)
    return {"checkpoint_dir": checkpoint, "review_request": review_request,
            "result": review_result, "session_id": session_id,
            "source": {"snapshot": snapshot, "files": source_files(upstream_root),
                       "review_materials": source_files(review_root)}}


def _require_directory(root: Path, relative: str, field: str) -> Path:
    rel = _safe_rel(relative, field)
    root = root.resolve(strict=True)
    path = root.joinpath(*rel.parts)
    current = root
    for part in rel.parts:
        current = current / part
        if current.is_symlink():
            raise FactoryError(f"{field} path contains a symlink", "reference_import_provenance", 409)
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError) as error:
        raise FactoryError(f"{field} path is missing or escapes its root", "reference_import_provenance", 409) from error
    if not resolved.is_dir():
        raise FactoryError(f"{field} must be a directory", "reference_import_provenance", 409)
    return resolved


def _profile_module(pack):
    path = Path(pack).resolve().parent / "examples/assisted-trials/product_reference_profile.py"
    if not path.is_file() or path.is_symlink():
        raise FactoryError("official ProductReference validator unavailable", "reference_validator_unavailable", 503)
    key = "_atlas_product_reference_catalog_profile"
    module = sys.modules.get(key)
    if module is None:
        spec = importlib.util.spec_from_file_location(key, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[key] = module
        try:
            spec.loader.exec_module(module)
        except Exception:
            sys.modules.pop(key, None)
            raise
    return module


class ReferenceCatalog:
    """Separate immutable archive store, indexed by its complete SHA-256."""

    def __init__(self, store):
        self.store = store
        self.root = Path(store.root) / "product-references"
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        if self.root.is_symlink():
            raise FactoryError("reference catalog root must not be a symlink")
        self.db = self.root / "catalog.sqlite"
        if self.db.is_symlink():
            raise FactoryError("reference catalog database must not be a symlink")
        with self._connect() as con:
            con.execute("""CREATE TABLE IF NOT EXISTS product_reference (
              id TEXT PRIMARY KEY, package_sha256 TEXT NOT NULL UNIQUE,
              archive_name TEXT NOT NULL UNIQUE, body TEXT NOT NULL,
              imported_at TEXT NOT NULL)""")
        os.chmod(self.db, 0o600)

    @contextmanager
    def _connect(self, write=False):
        con = sqlite3.connect(self.db, timeout=30)
        con.row_factory = sqlite3.Row
        try:
            if write:
                con.execute("BEGIN IMMEDIATE")
            yield con
            con.commit()
        except BaseException:
            con.rollback()
            raise
        finally:
            con.close()

    def _registered_revision(self, pilot_id, leaf, revision_id):
        from .reference_pilot import ReferencePilotService
        revision_info = ReferencePilotService(self.store).get_revision(pilot_id, leaf, revision_id)
        with self.store.connect() as con:
            pilot = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id=?", (pilot_id,)).fetchone()
            if not pilot:
                raise FactoryError("reference pilot not found", "not_found", 404)
            events = con.execute("SELECT body FROM auxiliary_reference_pilot_event WHERE pilot_id=? AND kind='revision' ORDER BY id", (pilot_id,)).fetchall()
            selected = None
            for event_row in events:
                event = json.loads(event_row[0])
                request = event.get("request")
                if not isinstance(request, dict) or digest(request) != event.get("request_digest"):
                    raise FactoryError("registered revision record changed", "reference_pilot_integrity", 409)
                if request.get("leaf") == leaf and request.get("revision_id") == revision_id:
                    selected = (request, event)
                    break
            if not selected:
                raise FactoryError("revision is not registered for this pilot and leaf", "reference_pilot_binding", 409)
            request, event = selected
            if request.get("plan_id") != pilot["plan_id"]:
                raise FactoryError("revision plan differs from registered pilot", "reference_pilot_binding", 409)
            if (revision_info.get("request") != request
                    or revision_info.get("request_digest") != event.get("request_digest")):
                raise FactoryError("revision service receipt differs from durable request", "reference_pilot_integrity", 409)
            registered = json.loads(pilot["request_json"])
            binding = next((item for item in registered.get("leaves", []) if item.get("leaf") == leaf), None)
            if not binding:
                raise FactoryError("leaf is outside registered pilot scope", "reference_pilot_scope", 409)
            return pilot, registered, binding, request, event, revision_info

    def _generation_dir(self, generation_path, leaf, revision_id):
        rel = _safe_rel(generation_path, "generation_path")
        if len(rel.parts) < 4 or tuple(rel.parts[-3:]) != (leaf, revision_id, "generation"):
            raise FactoryError("generation_path must identify the registered leaf/revision generation", "reference_import", 400)
        root = Path(self.store.pack).resolve().parent
        target = root.joinpath(*rel.parts)
        current = root
        for part in rel.parts:
            current = current / part
            if current.is_symlink():
                raise FactoryError("generation path contains a symlink", "reference_import", 400)
        try:
            resolved = target.resolve(strict=True)
            resolved.relative_to(root)
        except (OSError, ValueError) as error:
            raise FactoryError("generation path is unavailable or escapes the repository", "reference_import", 400) from error
        if not resolved.is_dir():
            raise FactoryError("generation path must be a directory", "reference_import", 400)
        return resolved

    def _ledger_check(self, pilot, leaf, revision_id, checkpoint_summaries):
        stage_names = {
            "research": f"reference/research/{pilot['id']}",
            "author": f"reference/author/{pilot['id']}/{revision_id}",
            "review": f"reference/review/{pilot['id']}/{revision_id}",
        }
        with self.store.connect() as con:
            rows = con.execute(
                "SELECT id,identity,phase,kind,status,stage FROM tf_budget_reservation WHERE campaign_id=? AND phase=? AND identity=?",
                (pilot["campaign_id"], pilot["phase"], pilot["plan_id"] + ":" + leaf),
            ).fetchall()
        for stage, expected_stage in stage_names.items():
            summary = checkpoint_summaries[stage]
            reservation_id = summary.get("reservation_id")
            matches = [row for row in rows if row["id"] == reservation_id]
            if (not isinstance(reservation_id, str) or len(matches) != 1
                    or matches[0]["status"] != "completed"
                    or matches[0]["stage"] != expected_stage
                    or matches[0]["identity"] != pilot["plan_id"] + ":" + leaf):
                raise FactoryError(f"{stage} checkpoint lacks its completed matching ledger reservation", "reference_ledger_incomplete", 409)

    def _verify_archive(self, archive_path, expected_sha, generation, pilot, revision_request, input_binding):
        if not isinstance(expected_sha, str) or not _HEX.fullmatch(expected_sha):
            raise FactoryError("package_sha256 must be lowercase SHA-256", "reference_import", 400)
        package = archive_path.read_bytes()
        if len(package) > _MAX_ARCHIVE or _sha(package) != expected_sha:
            raise FactoryError("reference package size or SHA-256 differs", "reference_package_changed", 409)
        try:
            with zipfile.ZipFile(archive_path) as archive:
                infos = archive.infolist()
                names = [info.filename for info in infos]
                if (len(infos) > _MAX_FILES or len(names) != len(set(names))
                        or any(info.is_dir() or _safe_rel(info.filename, "ZIP member").as_posix() != info.filename for info in infos)
                        or any(((info.external_attr >> 16) & 0o170000) == 0o120000 for info in infos)
                        or sum(info.file_size for info in infos) > _MAX_UNPACKED
                        or any(info.file_size > _MAX_UNPACKED for info in infos)):
                    raise FactoryError("reference ZIP inventory is unsafe or exceeds limits", "reference_package_invalid", 400)
                files = {info.filename: archive.read(info) for info in infos}
        except (zipfile.BadZipFile, OSError, RuntimeError) as error:
            raise FactoryError("reference package is not a readable ZIP", "reference_package_invalid", 400) from error
        if ("manifest.json" not in files or "reference.json" not in files or "review.json" not in files
                or "review-result.json" not in files or "research.json" not in files or "revision.json" not in files):
            raise FactoryError("reference package is missing required files", "reference_package_invalid", 400)
        manifest = _read_json_bytes(files["manifest.json"], "manifest.json")
        profile = _profile_module(self.store.pack)
        if (manifest.get("artifact_kind") != "atlas.product-reference"
                or manifest.get("artifact_type") != "atlas.product-reference.v1"
                or manifest.get("profile_version") != revision_request.get("profile_version")
                or manifest.get("prompt_digest") != revision_request.get("prompt_digest")
                or manifest.get("upstream_status") != "not_run"
                or manifest.get("application_runtime_status") != "not_run"
                or manifest.get("publication_status") != "not_published"):
            raise FactoryError("package is not a non-runtime ProductReference freeze", "reference_package_invalid", 400)
        expected_inventory = manifest.get("file_sha256")
        if (not isinstance(expected_inventory, dict) or set(expected_inventory) != set(files) - {"manifest.json"}
                or any(not isinstance(value, str) or not _HEX.fullmatch(value)
                       or _sha(files[name]) != value for name, value in expected_inventory.items())):
            raise FactoryError("reference package inventory or file digest differs", "reference_package_integrity", 409)
        spec = _read_json_bytes(files["reference.json"], "reference.json")
        inputs_path = generation / "author/INPUT.json"
        author_result_path = generation / "author/RESULT.json"
        author_delivery_path = generation / "author/DELIVERED.json"
        review_result_path = generation / "review/RESULT.json"
        review_delivery_path = generation / "review/DELIVERED.json"
        review_input_path = generation / "REVIEW_INPUT.json"
        review_stage_input_path = generation / "review/INPUT.json"
        read_views_path = generation / "READ_VIEWS.json"
        for relative in ("author/INPUT.json", "author/RESULT.json", "author/DELIVERED.json", "author/BINDING.json",
                         "review/RESULT.json", "review/DELIVERED.json", "review/BINDING.json", "review/INPUT.json",
                         "REVIEW_INPUT.json", "READ_VIEWS.json", "REVIEW_RESULT.json", "research/RESULT.json",
                         "research/DELIVERED.json", "research/BINDING.json"):
            _require_file(generation, relative, relative)
        inputs = _read_json_bytes(inputs_path.read_bytes(), "author/INPUT.json")
        author_revision = inputs.get("revision")
        revision_record = _read_json_bytes(files["revision.json"], "revision.json")
        author_raw = _read_json_bytes(author_result_path.read_bytes(), "author/RESULT.json")
        author_delivery = _read_json_bytes(author_delivery_path.read_bytes(), "author/DELIVERED.json")
        author_binding = _read_json_bytes((generation / "author/BINDING.json").read_bytes(), "author/BINDING.json")
        review_raw = _read_json_bytes(review_result_path.read_bytes(), "review/RESULT.json")
        review_delivery = _read_json_bytes(review_delivery_path.read_bytes(), "review/DELIVERED.json")
        review_input = _read_json_bytes(review_input_path.read_bytes(), "REVIEW_INPUT.json")
        review_revision = review_input.get("revision")
        review_stage_input = _read_json_bytes(review_stage_input_path.read_bytes(), "review/INPUT.json")
        review_binding = _read_json_bytes((generation / "review/BINDING.json").read_bytes(), "review/BINDING.json")
        read_views = _read_json_bytes(read_views_path.read_bytes(), "READ_VIEWS.json")
        if not isinstance(read_views, dict):
            raise FactoryError("READ_VIEWS.json must be an object", "reference_import_provenance", 409)
        for name in read_views:
            _require_file(generation, name, "review read material")
        review_receipt = _read_json_bytes(files["review.json"], "review.json")
        reviewed = _read_json_bytes(files["review-result.json"], "review-result.json")
        coverage_path = _require_file(generation, "READ_COVERAGE_PROOF.json", "read coverage proof")
        coverage_proof = _read_json_bytes(coverage_path.read_bytes(), "READ_COVERAGE_PROOF.json")
        if (not isinstance(coverage_proof, dict)
                or coverage_proof.get("schema") != "atlas.product-reference-read-coverage.v1"
                or coverage_proof.get("mode") not in {"exact", "canonical_equivalent"}
                or coverage_proof.get("review_input_digest") != digest(review_input)
                or coverage_proof.get("material_manifest_digest") != digest(read_views)
                or coverage_proof.get("read_events_digest") != digest(review_delivery.get("read_events", []))):
            raise FactoryError("read coverage proof does not bind the delivered review evidence", "reference_import_review", 409)
        if coverage_proof.get("mode") == "canonical_equivalent":
            bundled_coverage = files.get("read-coverage-proof.json")
            if (bundled_coverage is None
                    or _read_json_bytes(bundled_coverage, "read-coverage-proof.json") != coverage_proof
                    or review_receipt.get("read_coverage_proof_sha256") != digest(coverage_proof)):
                raise FactoryError("canonical-equivalent read proof is not bound by the frozen package and review receipt", "reference_import_review", 409)
        elif "read-coverage-proof.json" in files and _read_json_bytes(files["read-coverage-proof.json"], "read-coverage-proof.json") != coverage_proof:
            raise FactoryError("bundled exact read proof differs from its generation receipt", "reference_import_review", 409)
        repo_root = Path(self.store.pack).resolve().parent
        input_rel = _safe_rel(input_binding.get("input_path"), "registered input path")
        input_path = _require_file(repo_root, input_rel.as_posix(), "registered input")
        if _sha(input_path.read_bytes()) != input_binding.get("input_sha256"):
            raise FactoryError("registered frozen inputs are unavailable or changed", "reference_pilot_integrity", 409)
        registered_inputs = _read_json_bytes(input_path.read_bytes(), "registered inputs")
        if inputs.get("inputs") != registered_inputs or manifest.get("input_sha256") != digest(registered_inputs):
            raise FactoryError("author and package inputs differ from registered pilot inputs", "reference_pilot_binding", 409)
        try:
            resolved_author_reference = profile.resolve_authored_reference(author_raw, inputs)
        except (AttributeError, KeyError, TypeError, ValueError) as error:
            raise FactoryError("delivered author result cannot be resolved against its bound revision input", "reference_import_provenance", 409) from error
        if (resolved_author_reference != spec
                or digest(author_raw) != author_delivery.get("result_digest")
                or author_binding.get("stage") != "author"
                or author_binding.get("payload_digest") != digest(inputs)
                or author_delivery.get("binding_digest") != digest(author_binding)):
            raise FactoryError("ZIP reference does not match the delivered author result", "reference_import_provenance", 409)
        if (not isinstance(author_revision, dict)
                or set(author_revision) != {"revision_id", "parent_author_result", "parent_reference",
                                            "parent_reference_digest", "parent_author_sha256", "diagnostics", "lineage"}
                or not isinstance(review_revision, dict)
                or revision_record != review_revision
                or revision_record != {"parent_reference": author_revision.get("parent_reference"),
                                       "author_result": author_raw,
                                       "diagnostics": author_revision.get("diagnostics"),
                                       "lineage": author_revision.get("lineage")}
                or manifest.get("revision_lineage") != author_revision.get("lineage")
                or author_revision.get("parent_reference_digest") != digest(author_revision.get("parent_reference"))
                or author_revision.get("revision_id") != revision_request.get("revision_id")
                or author_revision.get("parent_author_sha256") != revision_request.get("parents", {}).get("author", {}).get("sha256")):
            raise FactoryError("bundled revision record differs from the bound author and review inputs", "reference_import_provenance", 409)
        identity = digest(review_input)
        if (review_stage_input.get("input_digest") != identity
                or review_stage_input.get("review_input") != review_input
                or review_binding.get("stage") != "review"
                or review_binding.get("payload_digest") != digest(review_stage_input)
                or review_delivery.get("binding_digest") != digest(review_binding)):
            raise FactoryError("delivered reviewer input is not bound to the canonical review input", "reference_import_provenance", 409)
        if (review_input.get("reference") != spec or review_receipt.get("review_input_digest") != identity
                or manifest.get("review_input_digest") != identity
                or review_raw != reviewed or digest(review_raw) != review_delivery.get("result_digest")
                or review_receipt.get("review_result_digest") != digest(reviewed)):
            raise FactoryError("bundled independent review does not match delivered review input/result", "reference_import_provenance", 409)
        if (review_receipt.get("read_view_manifest_digest") != digest(read_views)
                or review_receipt.get("revision_lineage") != manifest.get("revision_lineage")):
            raise FactoryError("bundled review receipt differs from package read-view or revision lineage", "reference_import_provenance", 409)
        author_session, review_session = author_delivery.get("session_id"), review_delivery.get("session_id")
        if (not isinstance(author_session, str) or not author_session
                or not isinstance(review_session, str) or not review_session or author_session == review_session
                or review_receipt.get("sessions", {}).get("author") != author_session
                or review_receipt.get("sessions", {}).get("review") != review_session):
            raise FactoryError("independent review must bind distinct delivered author and reviewer sessions", "reference_import_provenance", 409)
        if (reviewed.get("verdict") != "pass" or not isinstance(reviewed.get("checks"), dict)
                or not all(value is True for value in reviewed["checks"].values())
                or reviewed.get("issues") != []):
            raise FactoryError("reference package does not contain a passing independent review", "reference_import_review", 409)
        try:
            trusted = inputs["inputs"]["trusted_source_ids"] if "inputs" in inputs else inputs["trusted_source_ids"]
            source_ids = set(trusted.get("requirements", [])) | set(trusted.get("upstream", []))
            if isinstance(trusted.get("requirements"), dict):
                source_ids |= set(trusted["requirements"])
            if isinstance(trusted.get("upstream"), dict):
                source_ids |= set(trusted["upstream"])
            validate_reference(spec, source_ids=source_ids)
            rendered = render_reference(spec, source_ids=source_ids)
            scopes = {row["id"]: select_scope(spec, row["id"], source_ids=source_ids) for row in spec["scope_options"]}
        except (ValueError, KeyError, TypeError) as error:
            raise FactoryError(f"strict ProductReference validation failed: {error}", "reference_package_invalid", 400) from error
        for name, content in rendered.items():
            if files.get(name) != content.encode("utf-8"):
                raise FactoryError(f"rendered ProductReference file differs: {name}", "reference_package_integrity", 409)
        for scope_id, value in scopes.items():
            name = f"scopes/{scope_id}.json"
            if files.get(name) != (canonical(value) + "\n").encode():
                raise FactoryError(f"scope file differs from strict scope selection: {name}", "reference_package_integrity", 409)
        if (manifest.get("spec_sha256") != digest(spec)
                or manifest.get("input_sha256") != digest(registered_inputs)
                or manifest.get("scope_slice_digests") != {key: digest(value) for key, value in scopes.items()}
                or review_receipt.get("status") != "passed"):
            raise FactoryError("reference package declared digests differ from verified content", "reference_package_integrity", 409)
        expected_cases = inputs.get("inputs", {}).get("case_refs", inputs.get("case_refs"))
        if manifest.get("case_refs") != expected_cases:
            raise FactoryError("package case references differ from frozen inputs", "reference_case_mismatch", 409)
        lineage = manifest.get("revision_lineage")
        parents = revision_request.get("parents", {})
        adapter_research_root = generation.parent / "official-checkpoints/research"
        if (not isinstance(lineage, dict) or lineage.get("revision_id") != revision_request.get("revision_id")
                or lineage.get("parent_author_sha256") != parents.get("author", {}).get("sha256")
                or lineage.get("research_result_sha256") != parents.get("research", {}).get("sha256")
                or lineage.get("inputs_digest") != registered_inputs.get("digest")
                or not isinstance(lineage.get("adapter_research_checkpoint_digest"), str)
                or lineage.get("adapter_research_checkpoint_digest") != _tree_digest(adapter_research_root)):
            raise FactoryError("package revision lineage differs from registered parent checkpoints", "reference_pilot_binding", 409)
        research_path = _require_file(generation, "research/RESULT.json", "research result")
        research_receipt_path = _require_file(generation, "research/DELIVERED.json", "research delivery")
        if files["research.json"] != research_path.read_bytes():
            raise FactoryError("bundled research result differs from the retained host checkpoint", "reference_import_provenance", 409)
        research_parent = revision_request.get("parents", {}).get("research", {})
        research_parent_receipt = revision_request.get("parents", {}).get("research_receipt", {})
        if (_sha(research_path.read_bytes()) != research_parent.get("sha256")
                or _sha(research_receipt_path.read_bytes()) != research_parent_receipt.get("sha256")):
            raise FactoryError("retained research checkpoints differ from the registered parent references", "reference_pilot_integrity", 409)
        research_result = _read_json_bytes(research_path.read_bytes(), "research/RESULT.json")
        research_delivery = _read_json_bytes(research_receipt_path.read_bytes(), "research/DELIVERED.json")
        research_binding_path = _require_file(generation, "research/BINDING.json", "research binding")
        if (research_delivery.get("binding_digest") != digest(_read_json_bytes(research_binding_path.read_bytes(), "research/BINDING.json"))
                or research_delivery.get("result_digest") != digest(research_result)
                or research_delivery.get("session_id") != review_receipt.get("sessions", {}).get("research")):
            raise FactoryError("retained research delivery receipt is not intact", "reference_import_provenance", 409)
        summary_paths = {stage: _require_file(generation.parent, f"official-checkpoints/{stage}/cli-summary.json", f"{stage} cli summary") for stage in ("author", "review", "research")}
        author_summary = _read_json_bytes(summary_paths["author"].read_bytes(), "author cli summary")
        review_summary = _read_json_bytes(summary_paths["review"].read_bytes(), "review cli summary")
        research_summary = _read_json_bytes(summary_paths["research"].read_bytes(), "research cli summary")
        summaries = {"author": author_summary, "review": review_summary, "research": research_summary}
        author_checkpoint = generation.parent / "official-checkpoints/author"
        review_checkpoint = generation.parent / "official-checkpoints/review"
        for stage, checkpoint, expected in (("author", author_checkpoint, author_raw), ("review", review_checkpoint, review_raw)):
            for name in ("RESULT.json", "DELIVERED.json"):
                _require_file(generation.parent, f"official-checkpoints/{stage}/{name}", f"official {stage} {name}")
            if _read_json_bytes((checkpoint / "RESULT.json").read_bytes(), f"official {stage} result") != expected:
                raise FactoryError(f"official {stage} result differs from generation result", "reference_import_provenance", 409)
            checkpoint_result = _read_json_bytes((checkpoint / "RESULT.json").read_bytes(), f"official {stage} result")
            checkpoint_delivery = _read_json_bytes((checkpoint / "DELIVERED.json").read_bytes(), f"official {stage} delivery")
            checkpoint_binding_path = _require_file(generation.parent, f"official-checkpoints/{stage}/BINDING.json", f"official {stage} binding")
            checkpoint_binding = _read_json_bytes(checkpoint_binding_path.read_bytes(), f"official {stage} binding")
            if (checkpoint_delivery.get("result_digest") != digest(checkpoint_result)
                    or checkpoint_delivery.get("binding_digest") != digest(checkpoint_binding)):
                raise FactoryError(f"official {stage} checkpoint receipt does not bind its result", "reference_import_provenance", 409)
        for stage, summary in summaries.items():
            if (summary.get("delivery_status") != "delivered"
                    or not isinstance(summary.get("session_id"), str) or not summary["session_id"]
                    or summary.get("session_id") != ({"author": author_session, "review": review_session}.get(stage, review_receipt.get("sessions", {}).get("research")))):
                if stage != "research":
                    raise FactoryError(f"official {stage} checkpoint summary does not match delivered session", "reference_import_provenance", 409)
        if research_summary.get("session_id") != review_receipt.get("sessions", {}).get("research"):
            raise FactoryError("official research checkpoint does not match bundled research session", "reference_import_provenance", 409)
        self._ledger_check(pilot, revision_request["leaf"], revision_request["revision_id"], summaries)
        try:
            official_context = None
            if coverage_proof["mode"] == "canonical_equivalent":
                official_context = _official_review_context(generation, review_stage_input, review_raw,
                                                            review_session)
            verified_coverage = profile._verify_read_events(review_delivery.get("read_events", []), generation,
                                                            read_views, official_context=official_context)
            if verified_coverage != coverage_proof:
                raise ValueError("persisted read coverage proof differs from recomputed official read evidence")
            source_ids = set(source_ids)
            profile.validate_review(reviewed, identity, author_session, review_session,
                                    len(review_input.get("observations", [])))
        except (ValueError, KeyError, TypeError) as error:
            raise FactoryError(f"independent review provenance failed verification: {error}", "reference_import_review", 409) from error
        return manifest, spec, rendered, expected_cases

    def import_reference(self, request):
        if (not isinstance(request, dict) or set(request) != {"pilot_id", "leaf", "revision_id", "generation_path", "package_sha256"}
                or not isinstance(request.get("pilot_id"), str) or not request["pilot_id"]
                or not isinstance(request.get("leaf"), str) or not _LEAF.fullmatch(request["leaf"])
                or not isinstance(request.get("revision_id"), str) or not _REVISION.fullmatch(request["revision_id"])):
            raise FactoryError("reference import requires a registered pilot, leaf, revision, generation path, and package SHA", "reference_import", 400)
        pilot, registered, input_binding, revision_request, event, revision_info = self._registered_revision(
            request["pilot_id"], request["leaf"], request["revision_id"])
        if revision_request.get("generation_path") != request["generation_path"]:
            raise FactoryError("generation path differs from registered revision binding", "reference_pilot_binding", 409)
        if event.get("effective_max_calls", 0) <= 0:
            raise FactoryError("revision has no completed budget authorization", "reference_ledger_incomplete", 409)
        generation = self._generation_dir(request["generation_path"], request["leaf"], request["revision_id"])
        archive_path = generation / "reference.zip"
        if archive_path.is_symlink() or not archive_path.is_file():
            raise FactoryError("generated frozen reference package is unavailable", "reference_package_unavailable", 409)
        manifest, spec, rendered, case_refs = self._verify_archive(
            archive_path, request["package_sha256"], generation, pilot, revision_request, input_binding)
        if manifest.get("revision_lineage", {}).get("revision_id") != request["revision_id"]:
            raise FactoryError("package lineage does not match registered revision", "reference_pilot_binding", 409)
        library = None
        if (Path(self.store.pack) / "mvp_apps.json").is_file():
            from .cases import CaseLibrary
            library = CaseLibrary(self.store, initialize=False)
        case_links = []
        for ref in case_refs or []:
            if library is None:
                raise FactoryError("CaseLibrary is unavailable for formal case binding", "reference_case_unavailable", 503)
            case = library.get_case(ref["case_id"], ref["revision"])
            if case.get("digest") != ref.get("digest"):
                raise FactoryError("package case reference digest differs from CaseLibrary", "reference_case_mismatch", 409)
            case_links.append({"case_id": ref["case_id"], "revision": ref["revision"], "digest": ref["digest"],
                               "url": f"/api/factory/v1/cases/{ref['case_id']}/revisions/{ref['revision']}"})
        for stage in ("author", "review"):
            matches = [call for call in revision_info.get("calls", [])
                       if call.get("stage") == f"reference/{stage}/{request['pilot_id']}/{request['revision_id']}"
                       and call.get("status") == "completed"]
            if len(matches) != 1:
                raise FactoryError(f"revision {stage} reservation is not uniquely completed", "reference_ledger_incomplete", 409)
        package_sha = request["package_sha256"]
        reference_id = "ref_" + package_sha[:32]
        archive_name = package_sha + ".zip"
        body = {"id": reference_id, "name": spec["product_shape"]["name"], "schema": spec["schema"],
                "package_sha256": package_sha, "reference_digest": digest(spec),
                "pilot_id": request["pilot_id"], "leaf": request["leaf"], "revision_id": request["revision_id"],
                "status": "static_review_passed", "application_status": "application_not_run",
                "publication_status": "not_published", "case_refs": case_links,
                "manifest": manifest, "reference": spec,
                "document": rendered.get("PRODUCT_REFERENCE.md", "")}
        destination = self.root / archive_name
        if not destination.exists():
            with tempfile.NamedTemporaryFile(dir=self.root, prefix=".reference-import-", delete=False) as temp:
                temp_path = Path(temp.name)
                shutil.copyfileobj(archive_path.open("rb"), temp)
                temp.flush()
                os.fsync(temp.fileno())
            try:
                os.replace(temp_path, destination)
            finally:
                temp_path.unlink(missing_ok=True)
        elif destination.is_symlink() or _sha(destination.read_bytes()) != package_sha:
            raise FactoryError("existing catalog archive does not match immutable package digest", "reference_catalog_integrity", 409)
        with self._connect(write=True) as con:
            existing = con.execute("SELECT * FROM product_reference WHERE package_sha256=?", (package_sha,)).fetchone()
            if existing:
                prior = json.loads(existing["body"])
                if (existing["id"] != reference_id or existing["archive_name"] != archive_name
                        or prior.get("reference_digest") != body["reference_digest"]):
                    raise FactoryError("package digest is already bound to different catalog content", "reference_catalog_conflict", 409)
                return prior
            con.execute("INSERT INTO product_reference(id,package_sha256,archive_name,body,imported_at) VALUES(?,?,?,?,?)",
                        (reference_id, package_sha, archive_name, canonical(body), now()))
        return body

    def list_references(self):
        with self._connect() as con:
            rows = con.execute("SELECT body FROM product_reference ORDER BY imported_at DESC,id").fetchall()
        return [self._summary(json.loads(row[0])) for row in rows]

    @staticmethod
    def _summary(body):
        return {key: body[key] for key in ("id", "name", "schema", "package_sha256", "reference_digest",
                                            "pilot_id", "leaf", "revision_id", "status", "application_status",
                                            "publication_status", "case_refs")}

    def get_reference(self, reference_id):
        if not isinstance(reference_id, str) or not re.fullmatch(r"ref_[a-f0-9]{32}", reference_id):
            raise FactoryError("product reference not found", "not_found", 404)
        with self._connect() as con:
            row = con.execute("SELECT body FROM product_reference WHERE id=?", (reference_id,)).fetchone()
        if not row:
            raise FactoryError("product reference not found", "not_found", 404)
        return json.loads(row[0])

    def download(self, reference_id):
        body = self.get_reference(reference_id)
        path = self.root / (body["package_sha256"] + ".zip")
        if path.is_symlink() or not path.is_file() or _sha(path.read_bytes()) != body["package_sha256"]:
            raise FactoryError("catalog package is unavailable or changed", "reference_catalog_integrity", 409)
        return path, f"{reference_id}.product-reference.zip", "application/zip"
