"""Shared, immutable case research records for template work and app evidence."""

from __future__ import annotations

from datetime import datetime
import hashlib
import json
import re
import time
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
import uuid

from .store import FactoryError, canonical, digest, now
from .migrations import migrate


_SHA = re.compile(r"^[0-9a-f]{40}$")
_HEX = re.compile(r"^[0-9a-f]{64}$")
_KINDS = {"documentation", "code_observation", "inference", "runtime_verification"}


def _required(value, field, max_length=8000):
    if not isinstance(value, str) or not value.strip() or len(value) > max_length:
        raise FactoryError(f"{field} must be non-empty text (up to {max_length} characters)")
    return value.strip()


def _sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _safe_relative(value):
    if not isinstance(value, str) or "\\" in value:
        raise FactoryError("source file paths must be relative POSIX paths")
    path = PurePosixPath(value)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise FactoryError("source file path escapes the snapshot root")
    return path


def _validate_snapshot(raw, store_root):
    if not isinstance(raw, dict):
        raise FactoryError("source snapshot must be an object")
    repository = _required(raw.get("repository"), "repository", 1000)
    try:
        from .sources import github_repo
        parts = urlsplit(repository)
        port = parts.port
        if parts.scheme.lower() != "https" or parts.hostname is None or parts.hostname.lower() != "github.com" or parts.username or parts.password or port or parts.query or parts.fragment:
            raise FactoryError("invalid GitHub repository URL")
        repository = "https://github.com/" + github_repo("https://github.com" + parts.path).lower()
    except (FactoryError, ValueError) as exc:
        raise FactoryError("repository must be a canonical public GitHub root URL") from exc
    commit = raw.get("commit_sha")
    if not isinstance(commit, str) or not _SHA.fullmatch(commit):
        raise FactoryError("commit_sha must be a complete 40-character commit")
    strategy = _required(raw.get("strategy_version"), "strategy_version", 100)
    collected_at = _required(raw.get("collected_at"), "collected_at", 100)
    try:
        datetime.fromisoformat(collected_at.replace("Z", "+00:00"))
    except ValueError as exc:
        raise FactoryError("collected_at must be an ISO timestamp") from exc
    files = raw.get("files")
    if not isinstance(files, dict) or not files:
        raise FactoryError("snapshot files must be a non-empty path-to-sha256 manifest")
    root_raw = raw.get("local_root")
    if not isinstance(root_raw, str) or not root_raw:
        raise FactoryError("source snapshot requires a host local_root for validation")
    root_candidate = Path(root_raw)
    if not root_candidate.is_dir() or root_candidate.is_symlink():
        raise FactoryError("snapshot root must be an existing non-symlink directory")
    root = root_candidate.resolve(strict=True)
    store_root = Path(store_root).resolve(strict=True)
    root_lexical = root_candidate.absolute()
    if ".." in root_lexical.parts:
        raise FactoryError("snapshot root must be inside the factory store root")
    try:
        root.relative_to(store_root)
        lexical_relative = root_lexical.relative_to(store_root)
        inside_store = True
    except ValueError:
        inside_store = False
    if inside_store:
        current = store_root
        for part in lexical_relative.parts:
            current = current / part
            if current.is_symlink():
                raise FactoryError("snapshot root path contains a symlink")
    else:
        # The only permitted external root is a child of the host-owned
        # store.root/sources symlink. This keeps historical local_root bytes
        # valid after the source cache is moved without allowing arbitrary
        # host paths or alternate symlink routes.
        alias = store_root / "sources"
        if not alias.is_symlink():
            raise FactoryError("snapshot root must be inside the factory store root")
        try:
            alias_target = alias.resolve(strict=True)
            alias_relative = root_lexical.relative_to(alias)
            resolved_relative = root.relative_to(alias_target)
        except (OSError, ValueError) as exc:
            raise FactoryError("snapshot root must be inside the factory store root") from exc
        if (not alias_target.is_dir() or not alias_relative.parts or ".." in alias_relative.parts
            or not resolved_relative.parts):
            raise FactoryError("snapshot root must be a child of the sources alias")
        current = alias
        for part in alias_relative.parts:
            current = current / part
            if current.is_symlink():
                raise FactoryError("snapshot root path contains a symlink")
    normalized_files = {}
    for name, expected in files.items():
        relative = _safe_relative(name)
        if not isinstance(expected, str) or not _HEX.fullmatch(expected):
            raise FactoryError(f"invalid SHA-256 for source file {name}")
        target = root.joinpath(*relative.parts)
        # Reject symlinks anywhere in the path and ensure resolution stays rooted.
        current = root
        for part in relative.parts:
            current = current / part
            if current.is_symlink():
                raise FactoryError(f"source path contains a symlink: {name}")
        try:
            resolved = target.resolve(strict=True)
            resolved.relative_to(root)
        except (OSError, ValueError) as exc:
            raise FactoryError(f"source file is missing or escapes snapshot root: {name}") from exc
        if not resolved.is_file() or _sha256(resolved) != expected:
            raise FactoryError(f"source file digest mismatch: {name}")
        normalized_files[name] = expected
    license_files = raw.get("license_files", [])
    if not isinstance(license_files, list):
        raise FactoryError("license_files must be a list")
    for name in license_files:
        if name not in normalized_files:
            raise FactoryError("license and NOTICE paths must refer to files in the validated manifest")
    license_info = raw.get("license", {"status": "unknown"})
    if not isinstance(license_info, dict):
        raise FactoryError("license provenance must be an object")
    notice_hashes = license_info.get("notice_hashes", {})
    if not isinstance(notice_hashes, dict) or any(normalized_files.get(name) != value for name, value in notice_hashes.items()):
        raise FactoryError("license and NOTICE hashes must match fixed source files")
    archive_digest = raw.get("archive_sha256")
    if archive_digest is not None and (not isinstance(archive_digest, str) or not _HEX.fullmatch(archive_digest)):
        raise FactoryError("archive_sha256 must be a SHA-256 digest")
    body = {
        "repository": repository.rstrip("/"),
        "repo_id": raw.get("repo_id"),
        "commit_sha": commit,
        "collected_at": collected_at,
        "strategy_version": strategy,
        "files": dict(sorted(normalized_files.items())),
        "file_manifest_digest": digest(dict(sorted(normalized_files.items()))),
        "license_files": sorted(set(license_files)),
        "license_uncertainties": raw.get("license_uncertainties", []),
        "license": raw.get("license", {"status": "unknown"}),
        "archive_sha256": raw.get("archive_sha256"),
        "excluded_paths": raw.get("excluded_paths", []),
        "_validated_root": str(root),
    }
    return body


class CaseLibrary:
    """Case storage backed by FactoryStore's durable SQLite database."""

    def __init__(self, store, initialize=True):
        self.store = store
        if initialize:
            migrate(store)

    def list_apps(self):
        with self.store.connect() as con:
            return [json.loads(row[0]) for row in con.execute("SELECT body FROM case_app ORDER BY legacy_slug")]

    def get_app(self, app_id):
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM case_app WHERE app_id=? OR legacy_slug=?", (app_id, app_id)).fetchone()
        if not row:
            raise FactoryError("application not found", "not_found", 404)
        return json.loads(row[0])

    def list_cases(self, app_id=None, scenario_id=None):
        with self.store.connect() as con:
            if scenario_id:
                rows = con.execute(
                    "SELECT DISTINCT c.case_id,c.revision FROM case_revision c JOIN scenario_case_link l ON l.case_id=c.case_id AND l.case_revision=c.revision WHERE l.scenario_id=? ORDER BY c.case_id,c.revision",
                    (scenario_id,),
                )
            elif app_id:
                app = self.get_app(app_id)
                rows = con.execute("SELECT case_id,revision FROM case_revision WHERE app_id=? ORDER BY case_id,revision", (app["app_id"],))
            else:
                rows = con.execute("SELECT case_id,revision FROM case_revision ORDER BY case_id,revision")
            keys = [(row[0], row[1]) for row in rows]
        return [self.get_case(case_id, revision) for case_id, revision in keys]

    def get_case(self, case_id, revision=None):
        with self.store.connect() as con:
            if revision is None:
                row = con.execute("SELECT body FROM case_revision WHERE case_id=? ORDER BY revision DESC LIMIT 1", (case_id,)).fetchone()
            else:
                row = con.execute("SELECT body FROM case_revision WHERE case_id=? AND revision=?", (case_id, revision)).fetchone()
            if not row:
                raise FactoryError("case revision not found", "not_found", 404)
            body = json.loads(row[0])
            evidence = [json.loads(r[0]) for r in con.execute("SELECT body FROM evidence_observation WHERE case_id=? AND revision=? ORDER BY evidence_id", (body["case_id"], body["revision"]))]
            for observation in evidence:
                observation["reviews"] = [dict(r) for r in con.execute("SELECT review_id,outcome,reviewer,reviewer_kind,evidence_digest,created_at FROM evidence_review WHERE evidence_id=? AND case_id=? AND revision=? ORDER BY created_at,rowid", (observation["evidence_id"], body["case_id"], body["revision"]))]
            links = [json.loads(r[0]) for r in con.execute("SELECT body FROM scenario_case_link WHERE case_id=? AND case_revision=? ORDER BY scenario_id,scenario_revision", (body["case_id"], body["revision"]))]
            snapshots = [json.loads(r[0]) for r in con.execute("SELECT body FROM source_snapshot WHERE snapshot_id IN (%s)" % (",".join("?" for _ in body["snapshot_ids"]) or "NULL"), body["snapshot_ids"])]
        body["observations"], body["scenario_links"], body["source_snapshots"] = evidence, links, snapshots
        return body

    def case_ref(self, case_id, revision):
        case = self.get_case(case_id, revision)
        return {"ref": f"atlas:case:{case_id}:r{revision}", "digest": case["digest"]}

    def resolve_case_ref(self, ref, expected_digest=None):
        match = re.fullmatch(r"atlas:case:([A-Za-z0-9:_-]+):r([1-9][0-9]*)", ref or "")
        if not match:
            raise FactoryError("invalid atlas:case reference")
        case = self.get_case(match.group(1), int(match.group(2)))
        if expected_digest is not None and expected_digest != case["digest"]:
            raise FactoryError("case reference digest does not match", "revision_conflict", 409)
        return case

    def commit_research(self, payload, idempotency_key, ownership=None):
        key = _required(idempotency_key, "idempotency_key", 200)
        if not isinstance(payload, dict):
            raise FactoryError("research payload must be an object")
        request_digest = digest(payload)
        with self.store.connect(True) as con:
            if ownership is not None:
                if not isinstance(ownership, dict) or not ownership.get("job_id") or not ownership.get("token"):
                    raise FactoryError("invalid research ownership token", "lease_lost", 409)
                owned = con.execute(
                    "SELECT 1 FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                    (ownership["job_id"], ownership["token"], time.time()),
                ).fetchone()
                if not owned:
                    raise FactoryError("research ownership lost before case commit", "lease_lost", 409)
            previous = con.execute("SELECT request_digest,case_id,revision FROM case_idempotency WHERE idempotency_key=?", (key,)).fetchone()
            if previous:
                if previous[0] != request_digest:
                    raise FactoryError("idempotency key was used for different research", "conflict", 409)
                return {"case": self.get_case(previous[1], previous[2]), "replayed": True}
            raw_snapshots = payload.get("source_snapshots")
            if not isinstance(raw_snapshots, list) or not raw_snapshots:
                raise FactoryError("at least one fixed source snapshot is required")
            if any(not isinstance(item, dict) for item in raw_snapshots):
                raise FactoryError("each source snapshot must be an object")
            snapshots = [_validate_snapshot(item, self.store.root) for item in raw_snapshots]
            requested_app = payload.get("app_id")
            if requested_app:
                app_row = con.execute("SELECT app_id FROM case_app WHERE app_id=? OR legacy_slug=?", (requested_app, requested_app)).fetchone()
                if not app_row:
                    raise FactoryError("application not found", "not_found", 404)
                app_id = app_row[0]
            else:
                # Repository identity, never a display-name guess, defines a new app.
                repository = snapshots[0]["repository"]
                app_id = "app:repo:" + hashlib.sha256(repository.encode()).hexdigest()[:24]
                con.execute(
                    "INSERT OR IGNORE INTO case_app(app_id,legacy_slug,body,created_at) VALUES(?,?,?,?)",
                    (app_id, "repo-" + hashlib.sha256(repository.encode()).hexdigest()[:24], canonical({"app_id": app_id, "legacy_slug": None, "name": _required(payload.get("app_name", repository), "app_name", 200), "aliases": [], "catalog_status": "research_discovered", "source_identity": {"kind": "repository", "repository": repository}, "created_at": now()}), now()),
                )
            snapshot_ids = []
            at = now()
            for snapshot in snapshots:
                snapshot_id = "src_" + digest({k: snapshot[k] for k in ("repository", "commit_sha", "strategy_version")})[:24]
                # Collection time is metadata; identical pinned content from the
                # same repository, commit and strategy reuses the first snapshot.
                snapshot_digest = digest({
                    "repository": snapshot["repository"], "repo_id": snapshot.get("repo_id"),
                    "commit_sha": snapshot["commit_sha"], "strategy_version": snapshot["strategy_version"],
                    "files": snapshot["files"], "file_manifest_digest": snapshot["file_manifest_digest"],
                    "license_files": snapshot["license_files"], "archive_sha256": snapshot.get("archive_sha256"),
                    "excluded_paths": snapshot.get("excluded_paths", []),
                })
                existing = con.execute("SELECT snapshot_id,digest,body FROM source_snapshot WHERE repository=? AND commit_sha=? AND strategy_version=?", (snapshot["repository"], snapshot["commit_sha"], snapshot["strategy_version"])).fetchone()
                if existing:
                    if existing[1] != snapshot_digest:
                        raise FactoryError("fixed source snapshot metadata conflicts with the stored snapshot", "conflict", 409)
                    snapshot_id = existing[0]
                else:
                    persisted_snapshot = {key: value for key, value in snapshot.items() if not key.startswith("_")}
                    con.execute("INSERT INTO source_snapshot VALUES(?,?,?,?,?,?,?,?)", (snapshot_id, snapshot["repository"], snapshot.get("repo_id"), snapshot["commit_sha"], snapshot["strategy_version"], snapshot_digest, canonical({**persisted_snapshot, "snapshot_id": snapshot_id}), at))
                snapshot_ids.append(snapshot_id)
            research = payload.get("research")
            if not isinstance(research, dict):
                raise FactoryError("research must be an object")
            research_body = {
                "summary": _required(research.get("summary"), "research summary"),
                "scope": research.get("scope", ""),
                "unknowns": research.get("unknowns", []),
                "input_digest": _required(research.get("input_digest"), "research input_digest", 128),
                "task_id": research.get("task_id"),
            }
            case_id = payload.get("case_id") or ("case_" + uuid.uuid4().hex)
            if not isinstance(case_id, str) or not re.fullmatch(r"[A-Za-z0-9:_-]{3,200}", case_id):
                raise FactoryError("invalid case_id")
            previous_revision = con.execute("SELECT MAX(revision) FROM case_revision WHERE case_id=?", (case_id,)).fetchone()[0]
            revision = (previous_revision or 0) + 1
            raw_observations = payload.get("observations", [])
            raw_links = payload.get("scenario_links", [])
            if not isinstance(raw_observations, list) or not isinstance(raw_links, list):
                raise FactoryError("observations and scenario_links must be lists")
            observation_bodies = [self._observation(item, case_id, revision, snapshots) for item in raw_observations]
            evidence_ids = {item["evidence_id"] for item in observation_bodies}
            if len(evidence_ids) != len(observation_bodies):
                raise FactoryError("evidence IDs must be unique within a case revision")
            for item in observation_bodies:
                if item["kind"] == "inference" and any(ref not in evidence_ids for ref in item["location"]["depends_on"]):
                    raise FactoryError("inference references evidence outside this case revision")
            links = [self._link(con, item, case_id, revision, evidence_ids) for item in raw_links]
            body = {
                "case_id": case_id,
                "revision": revision,
                "app_id": app_id,
                "snapshot_ids": sorted(snapshot_ids),
                "research": research_body,
                "research_input_digest": research_body["input_digest"],
                "evidence_digest": digest([item["digest"] for item in sorted(observation_bodies, key=lambda x: x["evidence_id"])]),
                "created_at": at,
                "created_task_id": research_body["task_id"],
            }
            body["digest"] = digest(body)
            con.execute("INSERT INTO case_revision VALUES(?,?,?,?,?,?)", (case_id, revision, app_id, body["digest"], canonical(body), at))
            for item in observation_bodies:
                con.execute("INSERT INTO evidence_observation VALUES(?,?,?,?,?,?)", (item["evidence_id"], case_id, revision, item["kind"], item["digest"], canonical(item)))
            for item in links:
                con.execute("INSERT INTO scenario_case_link VALUES(?,?,?,?,?)", (item["scenario_id"], item["scenario_revision"], case_id, revision, canonical(item)))
            con.execute("INSERT INTO case_idempotency VALUES(?,?,?,?)", (key, request_digest, case_id, revision))
        return {"case": self.get_case(case_id, revision), "replayed": False}

    def _observation(self, item, case_id, revision, snapshots):
        if not isinstance(item, dict) or item.get("kind") not in _KINDS:
            raise FactoryError("observation kind must be documentation, code_observation, inference, or runtime_verification")
        kind = item["kind"]
        evidence_id = item.get("evidence_id") or ("ev_" + uuid.uuid4().hex)
        if not isinstance(evidence_id, str) or not re.fullmatch(r"[A-Za-z0-9:_-]{3,200}", evidence_id):
            raise FactoryError("invalid evidence_id")
        statement = _required(item.get("statement"), "observation statement")
        location = item.get("location")
        status = "model_extracted"
        if kind == "documentation":
            if not isinstance(location, dict) or not re.fullmatch(r"https://[^\s]+", str(location.get("url", ""))):
                raise FactoryError("documentation observations require an HTTPS URL")
            if not (location.get("material_version") or location.get("collected_at")):
                raise FactoryError("documentation observations require a material version or collection time")
            if not isinstance(location.get("content_digest"), str) or not _HEX.fullmatch(location["content_digest"]):
                raise FactoryError("documentation observations require a content digest")
        if kind == "code_observation":
            if not isinstance(location, dict):
                raise FactoryError("code observations require a source location")
            commit, path, file_digest = location.get("commit_sha"), location.get("path"), location.get("file_digest")
            _safe_relative(path)
            source = next((source for source in snapshots if commit == source["commit_sha"] and source["files"].get(path) == file_digest), None)
            if source is None:
                raise FactoryError("code observation must match a snapshot commit, file and verified digest")
            content = (Path(source["_validated_root"]) / path).read_text(encoding="utf-8", errors="replace")
            line_start, line_end = location.get("line_start"), location.get("line_end")
            if line_start is not None or line_end is not None:
                if type(line_start) is not int or type(line_end) is not int or line_start < 1 or line_end < line_start or line_end > len(content.splitlines()):
                    raise FactoryError("code observation line range is outside the pinned file")
            symbol = location.get("symbol")
            if symbol is not None and (not isinstance(symbol, str) or not symbol.strip() or symbol not in content):
                raise FactoryError("code observation symbol is absent from the pinned file")
            if line_start is None and symbol is None:
                raise FactoryError("code observations require a line range or symbol location")
            status = "source_located"
        review = item.get("review", {"status": "pending"})
        if not isinstance(review, dict) or review.get("status", "pending") != "pending":
            raise FactoryError("evidence review status is assigned only by the host review service")
        if kind == "runtime_verification":
            run_id, assertion_id = item.get("verification_run_id"), item.get("assertion_id")
            if not run_id or not assertion_id:
                raise FactoryError("runtime observations require a verification run and assertion ID")
            with self.store.connect() as con:
                run = con.execute("SELECT id,body FROM acceptance WHERE id=?", (run_id,)).fetchone()
            if not run:
                raise FactoryError("runtime verification must reference a persisted run", "not_found", 404)
            run_body = json.loads(run[1])
            if run_body.get("target_kind") != "upstream_case" or assertion_id not in run_body.get("assertion_ids", []):
                raise FactoryError("runtime evidence must reference an upstream_case assertion")
            location = {"verification_run_id": run_id, "assertion_id": assertion_id}
            status = "source_located"
        if kind == "inference":
            depends = item.get("depends_on", [])
            if not isinstance(depends, list) or not depends:
                raise FactoryError("inference must list its dependent evidence IDs")
            location = {"depends_on": depends, "assumptions": item.get("assumptions", []), "reasoning": _required(item.get("reasoning"), "inference reasoning")}
        body = {
            "evidence_id": evidence_id,
            "case_id": case_id,
            "case_revision": revision,
            "kind": kind,
            "statement": statement,
            "location": location,
            "observation_status": status,
            "review": review,
        }
        body["digest"] = digest(body)
        return body

    @staticmethod
    def _link(con, item, case_id, revision, evidence_ids):
        if not isinstance(item, dict):
            raise FactoryError("scenario link must be an object")
        scenario_id = _required(item.get("scenario_id"), "scenario_id", 200)
        scenario_revision = item.get("scenario_revision")
        if isinstance(scenario_revision, bool) or not isinstance(scenario_revision, int) or scenario_revision < 1:
            raise FactoryError("scenario_revision must be a positive integer")
        scene_row = con.execute("SELECT body FROM scenario_history WHERE id=? AND revision=?", (scenario_id, scenario_revision)).fetchone()
        if not scene_row:
            raise FactoryError("scenario revision does not exist", "not_found", 404)
        ids = item.get("evidence_ids", [])
        if not isinstance(ids, list) or any(evidence not in evidence_ids for evidence in ids):
            raise FactoryError("scenario link references evidence outside this case revision")
        return {
            "scenario_id": scenario_id,
            "scenario_revision": scenario_revision,
            "case_id": case_id,
            "case_revision": revision,
            "reason": _required(item.get("reason"), "scenario fit reason"),
            "workflow_support": item.get("workflow_support", []),
            "adopted_scope": item.get("adopted_scope", []),
            "exclusions": item.get("exclusions", []),
            "evidence_ids": ids,
        }

    def record_evidence_review(self, case_id, revision, evidence_id, outcome, reviewer, reviewer_kind, ownership=None):
        """Persist independent review tied to the immutable observation digest."""
        if outcome not in {"accepted", "rejected", "uncertain"} or reviewer_kind not in {"human", "independent_agent"}:
            raise FactoryError("invalid evidence review")
        reviewer = _required(reviewer, "reviewer", 200)
        with self.store.connect(True) as con:
            if ownership is not None:
                if not isinstance(ownership, dict) or not ownership.get("job_id") or not ownership.get("token"):
                    raise FactoryError("invalid research ownership token", "lease_lost", 409)
                owned = con.execute("SELECT 1 FROM job WHERE id=? AND token=? AND state='running' AND lease>?", (ownership["job_id"], ownership["token"], time.time())).fetchone()
                if not owned:
                    raise FactoryError("research ownership lost before evidence review commit", "lease_lost", 409)
            row = con.execute("SELECT digest FROM evidence_observation WHERE evidence_id=? AND case_id=? AND revision=?", (evidence_id, case_id, revision)).fetchone()
            if not row:
                raise FactoryError("evidence not found", "not_found", 404)
            review_id = "rev_" + digest({"evidence_id": evidence_id, "case_id": case_id, "revision": revision, "evidence_digest": row[0], "outcome": outcome, "reviewer": reviewer, "reviewer_kind": reviewer_kind})[:32]
            con.execute("INSERT OR IGNORE INTO evidence_review VALUES(?,?,?,?,?,?,?,?,?)", (review_id, evidence_id, case_id, revision, row[0], outcome, reviewer, reviewer_kind, now()))
        return {"review_id": review_id, "evidence_id": evidence_id, "case_id": case_id, "revision": revision, "evidence_digest": row[0], "outcome": outcome, "reviewer": reviewer, "reviewer_kind": reviewer_kind}

    def evidence_basis(self, case_refs, scenario_id=None, scenario_revision=None):
        if not isinstance(case_refs, list) or not case_refs:
            raise FactoryError("at least one fixed case revision is required")
        cases = []
        for ref in case_refs:
            if isinstance(ref, str):
                cases.append(self.resolve_case_ref(ref))
            elif isinstance(ref, dict):
                cases.append(self.get_case(ref.get("case_id"), ref.get("revision")))
            else:
                raise FactoryError("case references must be atlas:case refs or {case_id, revision}")
        if scenario_id is not None:
            if isinstance(scenario_revision, bool) or not isinstance(scenario_revision, int) or scenario_revision < 1:
                raise FactoryError("scenario_revision must be a positive integer")
            for case in cases:
                if not any(link["scenario_id"] == scenario_id and link["scenario_revision"] == scenario_revision for link in case["scenario_links"]):
                    raise FactoryError("case revision is not linked to the requested scenario revision", "evidence_basis_invalid", 409)
        refs, evidence, source = [], [], {}
        for case in cases:
            refs.append({"case_id": case["case_id"], "revision": case["revision"], "digest": case["digest"], "evidence_digest": case["evidence_digest"]})
            evidence.extend(case["observations"])
            for snapshot in case["source_snapshots"]:
                source[snapshot["snapshot_id"]] = snapshot
        all_evidence_ids = [item["evidence_id"] for item in evidence]
        if len(all_evidence_ids) != len(set(all_evidence_ids)):
            raise FactoryError("evidence IDs are ambiguous across selected case revisions", "evidence_basis_invalid", 409)
        basis = {
            "scenario_id": scenario_id,
            "scenario_revision": scenario_revision,
            "case_refs": sorted(refs, key=lambda item: (item["case_id"], item["revision"])),
            "source_snapshots": [source[key] for key in sorted(source)],
            "evidence_ids": sorted(item["evidence_id"] for item in evidence),
            "evidence_digests": {item["evidence_id"]: item["digest"] for item in sorted(evidence, key=lambda item: item["evidence_id"])},
            "evidence_digest": digest(sorted((item["evidence_id"], item["digest"]) for item in evidence)),
        }
        basis["basis_digest"] = digest(basis)
        return basis

    def validate_basis(self, basis):
        if not isinstance(basis, dict):
            raise FactoryError("evidence basis must be an object")
        expected = self.evidence_basis(basis.get("case_refs", []), basis.get("scenario_id"), basis.get("scenario_revision"))
        if basis.get("basis_digest") != expected["basis_digest"] or basis != expected:
            raise FactoryError("evidence basis is stale or has been altered", "evidence_basis_invalid", 409)
        return expected

    def require_admissible(self, basis):
        """Require an independently accepted, source-located core code observation per case."""
        fixed = self.validate_basis(basis)
        scenario_id, scenario_revision = fixed.get("scenario_id"), fixed.get("scenario_revision")
        for ref in fixed["case_refs"]:
            case = self.get_case(ref["case_id"], ref["revision"])
            linked_ids = set()
            for link in case["scenario_links"]:
                if link["scenario_id"] == scenario_id and link["scenario_revision"] == scenario_revision:
                    linked_ids.update(link["evidence_ids"])
            accepted = False
            for observation in case["observations"]:
                if observation["kind"] != "code_observation" or observation["observation_status"] != "source_located":
                    continue
                if scenario_id is not None and observation["evidence_id"] not in linked_ids:
                    continue
                latest = observation["reviews"][-1] if observation["reviews"] else None
                if latest and latest["outcome"] == "accepted" and latest["evidence_digest"] == observation["digest"]:
                    accepted = True
                    break
            if not accepted:
                raise FactoryError(f"case {ref['case_id']} lacks an independently accepted code observation for the pinned workflow", "evidence_basis_insufficient", 409)
        return fixed

    def accepted_evidence_ids(self, basis):
        self.validate_basis(basis)
        accepted = set()
        for ref in basis["case_refs"]:
            for observation in self.get_case(ref["case_id"], ref["revision"])["observations"]:
                latest = observation["reviews"][-1] if observation["reviews"] else None
                if latest and latest["outcome"] == "accepted" and latest["evidence_digest"] == observation["digest"]:
                    accepted.add(observation["evidence_id"])
        return accepted

    def accepted_facts_view(self, basis, source_research_digest):
        """Build a deterministic generation view from currently accepted linked observations."""
        fixed = self.require_admissible(basis)
        if not isinstance(source_research_digest, str) or not re.fullmatch(r"[0-9a-f]{64}", source_research_digest):
            raise FactoryError("raw research checkpoint digest is invalid", "case_facts_view_invalid", 409)
        accepted = self.accepted_evidence_ids(fixed)
        facts, unknowns = [], []
        scenario_id = fixed["scenario_id"]
        scenario_revision = fixed["scenario_revision"]
        for ref in fixed["case_refs"]:
            case = self.get_case(ref["case_id"], ref["revision"])
            unknowns.extend({"case_id": ref["case_id"], "case_revision": ref["revision"], "statement": value}
                            for value in case["research"].get("unknowns", []))
            linked_ids = set()
            for link in case["scenario_links"]:
                if link["scenario_id"] == scenario_id and link["scenario_revision"] == scenario_revision:
                    linked_ids.update(link["evidence_ids"])
            for observation in case["observations"]:
                evidence_id = observation["evidence_id"]
                if evidence_id in accepted and evidence_id in linked_ids:
                    facts.append({
                        "case_id": ref["case_id"],
                        "case_revision": ref["revision"],
                        "evidence_id": evidence_id,
                        "kind": observation["kind"],
                        "statement": observation["statement"],
                    })
        facts.sort(key=lambda item: (item["case_id"], item["case_revision"], item["evidence_id"]))
        view = {
            "schema": "atlas.accepted-case-facts.v1",
            "policy": "accepted-linked-observations-only-v1",
            "status": "accepted",
            "basis_digest": fixed["basis_digest"],
            "source_research_digest": source_research_digest,
            "accepted_evidence_ids": sorted(item["evidence_id"] for item in facts),
            "facts": facts,
            "unknowns": sorted(unknowns, key=lambda item: (item["case_id"], item["case_revision"], item["statement"])),
        }
        view["view_digest"] = digest(view)
        return view

    def legacy_facts_marker(self, basis):
        """Permit old checkpoints only when every pinned observation is accepted."""
        fixed = self.require_admissible(basis)
        accepted = self.accepted_evidence_ids(fixed)
        all_ids = set(fixed["evidence_ids"])
        if accepted != all_ids:
            raise FactoryError(
                "legacy generation checkpoint includes a mixed accepted/rejected case basis; create a formal case revision",
                "case_facts_view_required", 409,
            )
        marker = {
            "schema": "atlas.accepted-case-facts.v1",
            "policy": "legacy-checkpoint-all-canonical-observations-accepted-v1",
            "status": "legacy_all_accepted",
            "basis_digest": fixed["basis_digest"],
            "accepted_evidence_ids": sorted(all_ids),
        }
        marker["view_digest"] = digest(marker)
        return marker

    def validate_facts_view(self, view, basis):
        """Bind a frozen facts view to current evidence/review state."""
        if not isinstance(view, dict):
            return self.legacy_facts_marker(basis)
        if view.get("status") == "legacy_all_accepted":
            expected = self.legacy_facts_marker(basis)
        elif view.get("status") == "accepted":
            expected = self.accepted_facts_view(basis, view.get("source_research_digest"))
        else:
            raise FactoryError("unknown accepted facts view status", "case_facts_view_invalid", 409)
        if view != expected:
            raise FactoryError("accepted facts view is stale or altered", "case_facts_view_invalid", 409)
        return expected

    def require_design_evidence(self, basis, choices):
        accepted = self.accepted_evidence_ids(basis)
        known = set(basis.get("evidence_ids", []))
        for choice in choices:
            refs = set(choice.get("evidence_ids", []))
            if not refs <= known or (choice.get("disposition") != "not_adopted" and not refs <= accepted):
                raise FactoryError("borrowed design cites unaccepted evidence", "case_adaptation_invalid", 409)
        return accepted
