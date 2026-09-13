"""Durable U17 project state, separate from the generated corpus database."""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import uuid

from atlas_runtime import PACK


SCHEMA_VERSION = 5
PROJECT_MODES = {"new", "existing"}
TASK_KINDS = {"analysis", "document", "code"}
TASK_STATES = {"planned", "queued", "running", "waiting_permission",
               "waiting_input", "completed", "failed", "stopped", "unknown"}
EXECUTION_STATES = TASK_STATES - {"planned"}
ACCEPTANCE_STATES = {"pending", "passed", "failed", "waived"}
APPLICATION_STATES = {"not_applicable", "pending", "applied", "conflict", "failed"}
SCOPE_STATES = {"current", "later", "excluded"}
READ_STATES = {"unread", "read", "reviewed"}
ITERATION_STATES = {"planned", "active", "completed", "abandoned"}
DOCUMENT_AUTHORS = {"ai", "human", "import", "unknown"}


class ProjectStoreError(RuntimeError):
    pass


class ProjectStore:
    def __init__(self, path: str | Path | None = None):
        configured = os.environ.get("ATLAS_PROJECT_STORE")
        self.path = Path(path or configured or PACK / "projects/atlas-projects.sqlite").resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def create_project(self, name: str, objective: str, workspace: str | Path | None,
                       mode: str) -> dict:
        if mode not in PROJECT_MODES:
            raise ValueError("mode must be new or existing")
        project_id = _id("prj")
        now = _now()
        try:
            workspace_value = os.fspath(workspace) if workspace is not None else ""
        except TypeError:
            raise ValueError("workspace must be a path") from None
        if not workspace_value.strip():
            if mode == "existing":
                raise ValueError("workspace is required for an existing project")
            workspace_value = str(self.path.parent / "workspaces" / project_id)
        workspace = str(Path(workspace_value).expanduser().resolve())
        with self._transaction() as con:
            con.execute("""INSERT INTO project
                (id,name,objective,workspace,mode,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?)""",
                (project_id, _required(name, "name"), _required(objective, "objective"),
                 workspace, mode, now, now))
        return self.get_project(project_id)

    def get_project(self, project_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("SELECT * FROM project WHERE id=?", (project_id,)).fetchone()
        if not row:
            raise ProjectStoreError("project not found")
        return dict(row)

    def list_projects(self) -> list[dict]:
        with self._connect() as con:
            rows = con.execute(
                "SELECT * FROM project ORDER BY updated_at DESC,id").fetchall()
        return [dict(row) for row in rows]

    def create_document(self, project_id: str, kind: str, title: str, content: str,
                        basis: list[dict] | None = None, author: str = "human",
                        change_summary: str = "") -> dict:
        document_id, version_id = _id("doc"), _id("dver")
        now = _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            normalized_basis = self._normalize_basis(con, project_id, basis or [])
            con.execute("""INSERT INTO document
                (id,project_id,kind,title,current_version,created_at,updated_at)
                VALUES (?,?,?,?,1,?,?)""",
                (document_id, project_id, _required(kind, "kind"),
                 _required(title, "title"), now, now))
            self._insert_version(con, version_id, document_id, 1, content, normalized_basis, now,
                                 author, change_summary)
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_document(document_id)

    def add_document_version(self, document_id: str, content: str,
                             basis: list[dict] | None = None,
                             expected_current_version: int | None = None,
                             author: str = "human", change_summary: str = "") -> dict:
        now, version_id = _now(), _id("dver")
        with self._transaction() as con:
            document = con.execute(
                "SELECT current_version,project_id FROM document WHERE id=?",
                (document_id,)).fetchone()
            if not document:
                raise ProjectStoreError("document not found")
            current = document["current_version"]
            if expected_current_version is not None and current != expected_current_version:
                raise ProjectStoreError("document version conflict")
            number = current + 1
            normalized_basis = self._normalize_basis(
                con, document["project_id"], basis or [])
            self._insert_version(con, version_id, document_id, number, content,
                                 normalized_basis, now,
                                 author, change_summary)
            con.execute("UPDATE document SET current_version=?,updated_at=? WHERE id=?",
                        (number, now, document_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, document["project_id"]))
        return self.get_document(document_id)

    def get_document(self, document_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("""SELECT d.*,v.id AS version_id,v.content,v.content_sha256,
                v.basis_json,v.author,v.change_summary,v.created_at AS version_created_at
                FROM document d JOIN document_version v
                ON v.document_id=d.id AND v.version=d.current_version WHERE d.id=?""",
                (document_id,)).fetchone()
        if not row:
            raise ProjectStoreError("document not found")
        result = dict(row)
        result["basis"] = json.loads(result.pop("basis_json"))
        result["review"] = self._document_review(result["project_id"], result["basis"],
                                                  result["version_created_at"])
        return result

    def list_documents(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            ids = [row[0] for row in con.execute(
                "SELECT id FROM document WHERE project_id=? ORDER BY updated_at DESC,id",
                (project_id,)).fetchall()]
        return [self.get_document(document_id) for document_id in ids]

    def list_document_versions(self, project_id: str, document_id: str) -> list[dict]:
        with self._connect() as con:
            row = con.execute("SELECT 1 FROM document WHERE id=? AND project_id=?",
                              (document_id, project_id)).fetchone()
            if not row:
                raise ProjectStoreError("document not found")
            rows = con.execute("""SELECT id AS version_id,document_id,version,content,
                content_sha256,basis_json,author,change_summary,created_at
                FROM document_version WHERE document_id=? ORDER BY version DESC""",
                (document_id,)).fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["basis"] = json.loads(item.pop("basis_json"))
            item["review"] = self._document_review(
                project_id, item["basis"], item["created_at"])
            result.append(item)
        return result

    def create_task(self, project_id: str, title: str, objective: str,
                    input_document_versions: list[str] | None = None,
                    requirement_ids: list[str] | None = None,
                    iteration_id: str | None = None,
                    kind: str = "code", write_paths: list[str] | None = None,
                    verification_commands: list[str] | None = None) -> dict:
        task_id, now = _id("tsk"), _now()
        versions = input_document_versions or []
        requirements = requirement_ids or []
        if kind not in TASK_KINDS:
            raise ValueError("task kind must be analysis, document, or code")
        normalized_write_paths = _relative_paths(write_paths or [], "write_paths")
        commands = _text_list(verification_commands or [], "verification_commands", 20)
        if kind == "analysis" and normalized_write_paths:
            raise ValueError("analysis tasks cannot declare write paths")
        with self._transaction() as con:
            self._require_project(con, project_id)
            for version_id in versions:
                row = con.execute("""SELECT 1 FROM document_version v JOIN document d
                    ON d.id=v.document_id WHERE v.id=? AND d.project_id=?""",
                    (version_id, project_id)).fetchone()
                if not row:
                    raise ProjectStoreError("document version does not belong to project")
            for requirement_id in requirements:
                row = con.execute("SELECT 1 FROM requirement WHERE id=? AND project_id=?",
                                  (requirement_id, project_id)).fetchone()
                if not row:
                    raise ProjectStoreError("requirement does not belong to project")
            if iteration_id:
                iteration = con.execute("SELECT * FROM iteration WHERE id=? AND project_id=?",
                                        (iteration_id, project_id)).fetchone()
                if not iteration:
                    raise ProjectStoreError("iteration does not belong to project")
                if iteration["status"] not in {"planned", "active"}:
                    raise ProjectStoreError("iteration no longer accepts tasks")
                iteration_versions = set(json.loads(iteration["input_versions_json"]))
                iteration_requirements = set(json.loads(iteration["requirement_ids_json"]))
                if not set(versions).issubset(iteration_versions):
                    raise ProjectStoreError("task document version is outside iteration scope")
                if not set(requirements).issubset(iteration_requirements):
                    raise ProjectStoreError("task requirement is outside iteration scope")
            con.execute("""INSERT INTO task
                (id,project_id,iteration_id,kind,title,objective,write_paths_json,
                 verification_commands_json,execution_status,acceptance_status,
                 acceptance_evidence_json,input_versions_json,requirement_ids_json,
                 created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (task_id, project_id, iteration_id, kind, _required(title, "title"),
                 _required(objective, "objective"), _json(normalized_write_paths),
                 _json(commands), "planned", "pending", "[]",
                 _json(versions), _json(requirements), now, now))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_task(task_id)

    def get_task(self, task_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("SELECT * FROM task WHERE id=?", (task_id,)).fetchone()
        if not row:
            raise ProjectStoreError("task not found")
        result = dict(row)
        result["input_document_versions"] = json.loads(result.pop("input_versions_json"))
        result["requirement_ids"] = json.loads(result.pop("requirement_ids_json"))
        result["acceptance_evidence"] = json.loads(result.pop("acceptance_evidence_json"))
        result["write_paths"] = json.loads(result.pop("write_paths_json"))
        result["verification_commands"] = json.loads(
            result.pop("verification_commands_json"))
        return result

    def list_tasks(self, project_id: str, iteration_id: str | None = None) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            if iteration_id:
                row = con.execute("SELECT 1 FROM iteration WHERE id=? AND project_id=?",
                                  (iteration_id, project_id)).fetchone()
                if not row:
                    raise ProjectStoreError("iteration does not belong to project")
                rows = con.execute("""SELECT id FROM task WHERE project_id=? AND iteration_id=?
                    ORDER BY created_at,id""", (project_id, iteration_id)).fetchall()
            else:
                rows = con.execute("""SELECT id FROM task WHERE project_id=?
                    ORDER BY created_at,id""", (project_id,)).fetchall()
        return [self.get_task(row["id"]) for row in rows]

    def add_reference(self, project_id: str, source_kind: str, source_ref: str,
                      source_version: str, locator: str = "", excerpt: str = "",
                      note: str = "", read_status: str = "unread") -> dict:
        if read_status not in READ_STATES:
            raise ValueError("invalid read status")
        reference_id, now = _id("ref"), _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            existing = con.execute("""SELECT id FROM reference WHERE project_id=?
                AND source_kind=? AND source_ref=? AND source_version=? AND locator=?""",
                (project_id, source_kind, source_ref, source_version, locator)).fetchone()
            if existing:
                raise ProjectStoreError("reference already saved")
            con.execute("""INSERT INTO reference
                (id,project_id,source_kind,source_ref,source_version,locator,excerpt,note,
                 read_status,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (reference_id, project_id, _required(source_kind, "source_kind"),
                 _required(source_ref, "source_ref"), _required(source_version, "source_version"),
                 locator, excerpt, note, read_status, now, now))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self._row("reference", reference_id)

    def get_reference(self, project_id: str, reference_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("SELECT * FROM reference WHERE id=? AND project_id=?",
                              (reference_id, project_id)).fetchone()
        if not row:
            raise ProjectStoreError("reference not found")
        return dict(row)

    def list_references(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            rows = con.execute("""SELECT * FROM reference WHERE project_id=?
                ORDER BY updated_at DESC,id""", (project_id,)).fetchall()
        return [dict(row) for row in rows]

    def update_reference(self, project_id: str, reference_id: str,
                         note: str | None = None,
                         read_status: str | None = None) -> dict:
        if note is None and read_status is None:
            raise ValueError("note or read_status is required")
        if note is not None and not isinstance(note, str):
            raise ValueError("note must be text")
        if read_status is not None and read_status not in READ_STATES:
            raise ValueError("invalid read status")
        now = _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            if not con.execute("SELECT 1 FROM reference WHERE id=? AND project_id=?",
                               (reference_id, project_id)).fetchone():
                raise ProjectStoreError("reference not found")
            if note is not None:
                con.execute("UPDATE reference SET note=?,updated_at=? WHERE id=?",
                            (note, now, reference_id))
            if read_status is not None:
                con.execute("UPDATE reference SET read_status=?,updated_at=? WHERE id=?",
                            (read_status, now, reference_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_reference(project_id, reference_id)

    def create_requirement(self, project_id: str, content: str,
                           recommended_scope: str | None = None,
                           recommendation_reason: str = "",
                           acceptance_conditions: list[str] | None = None,
                           reference_ids: list[str] | None = None) -> dict:
        if recommended_scope is not None and recommended_scope not in SCOPE_STATES:
            raise ValueError("invalid recommended scope")
        requirement_id, now = _id("req"), _now()
        references = reference_ids or []
        with self._transaction() as con:
            self._require_project(con, project_id)
            self._require_references(con, project_id, references)
            con.execute("""INSERT INTO requirement
                (id,project_id,content,recommended_scope,recommendation_reason,
                 confirmed_scope,confirmation_reason,acceptance_json,reference_ids_json,
                 created_at,updated_at) VALUES (?,?,?,?,?,NULL,'',?,?,?,?)""",
                (requirement_id, project_id, _required(content, "content"), recommended_scope,
                 recommendation_reason, _json(acceptance_conditions or []),
                 _json(references), now, now))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_requirement(requirement_id)

    def update_requirement(self, project_id: str, requirement_id: str,
                           content: str | None = None,
                           recommended_scope: str | None = None,
                           recommendation_reason: str | None = None,
                           acceptance_conditions: list[str] | None = None,
                           reference_ids: list[str] | None = None) -> dict:
        if all(value is None for value in (content, recommended_scope, recommendation_reason,
                                           acceptance_conditions, reference_ids)):
            raise ValueError("at least one requirement field is required")
        if recommended_scope is not None and recommended_scope not in SCOPE_STATES:
            raise ValueError("invalid recommended scope")
        if recommendation_reason is not None and not isinstance(recommendation_reason, str):
            raise ValueError("recommendation_reason must be text")
        now = _now()
        with self._transaction() as con:
            row = con.execute("SELECT * FROM requirement WHERE id=? AND project_id=?",
                              (requirement_id, project_id)).fetchone()
            if not row:
                raise ProjectStoreError("requirement not found")
            references = reference_ids if reference_ids is not None \
                else json.loads(row["reference_ids_json"])
            self._require_references(con, project_id, references)
            new_content = _required(content, "content") if content is not None else row["content"]
            new_acceptance = acceptance_conditions if acceptance_conditions is not None \
                else json.loads(row["acceptance_json"])
            if not isinstance(new_acceptance, list) or not all(
                    isinstance(value, str) and value.strip() for value in new_acceptance):
                raise ValueError("acceptance_conditions must contain non-empty text")
            meaning_changed = (new_content != row["content"] or
                               _json(new_acceptance) != row["acceptance_json"] or
                               _json(references) != row["reference_ids_json"])
            con.execute("""UPDATE requirement SET content=?,recommended_scope=?,
                recommendation_reason=?,acceptance_json=?,reference_ids_json=?,
                confirmed_scope=?,confirmation_reason=?,updated_at=? WHERE id=?""",
                (new_content,
                 recommended_scope if recommended_scope is not None else row["recommended_scope"],
                 recommendation_reason if recommendation_reason is not None
                 else row["recommendation_reason"],
                 _json(new_acceptance), _json(references),
                 None if meaning_changed else row["confirmed_scope"],
                 "" if meaning_changed else row["confirmation_reason"], now, requirement_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_requirement(requirement_id)

    def confirm_requirement(self, requirement_id: str, scope: str, reason: str) -> dict:
        if scope not in SCOPE_STATES:
            raise ValueError("invalid confirmed scope")
        now = _now()
        with self._transaction() as con:
            requirement = con.execute(
                "SELECT project_id FROM requirement WHERE id=?", (requirement_id,)).fetchone()
            if not requirement:
                raise ProjectStoreError("requirement not found")
            con.execute("""UPDATE requirement SET confirmed_scope=?,confirmation_reason=?,
                updated_at=? WHERE id=?""", (scope, _required(reason, "reason"), now, requirement_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, requirement["project_id"]))
        return self.get_requirement(requirement_id)

    def get_requirement(self, requirement_id: str) -> dict:
        result = self._row("requirement", requirement_id)
        result["acceptance_conditions"] = json.loads(result.pop("acceptance_json"))
        result["reference_ids"] = json.loads(result.pop("reference_ids_json"))
        return result

    def list_requirements(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            ids = [row[0] for row in con.execute(
                "SELECT id FROM requirement WHERE project_id=? ORDER BY created_at,id",
                (project_id,)).fetchall()]
        return [self.get_requirement(requirement_id) for requirement_id in ids]

    def record_decision(self, project_id: str, statement: str, rationale: str,
                        reference_ids: list[str] | None = None) -> dict:
        decision_id, now = _id("dec"), _now()
        references = reference_ids or []
        with self._transaction() as con:
            self._require_project(con, project_id)
            self._require_references(con, project_id, references)
            con.execute("""INSERT INTO decision
                (id,project_id,statement,rationale,reference_ids_json,created_at)
                VALUES (?,?,?,?,?,?)""",
                (decision_id, project_id, _required(statement, "statement"),
                 _required(rationale, "rationale"), _json(references), now))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        result = self._row("decision", decision_id)
        result["reference_ids"] = json.loads(result.pop("reference_ids_json"))
        return result

    def list_decisions(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            rows = con.execute(
                "SELECT * FROM decision WHERE project_id=? ORDER BY created_at,id",
                (project_id,)).fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["reference_ids"] = json.loads(item.pop("reference_ids_json"))
            result.append(item)
        return result

    def create_iteration(self, project_id: str, title: str, objective: str,
                         input_document_versions: list[str], requirement_ids: list[str],
                         activate: bool = True) -> dict:
        iteration_id, now = _id("itr"), _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            self._require_document_versions(con, project_id, input_document_versions)
            for requirement_id in requirement_ids:
                row = con.execute("""SELECT confirmed_scope FROM requirement
                    WHERE id=? AND project_id=?""", (requirement_id, project_id)).fetchone()
                if not row:
                    raise ProjectStoreError("requirement does not belong to project")
                if row["confirmed_scope"] != "current":
                    raise ProjectStoreError("iteration requires confirmed current-scope requirements")
            sequence = con.execute(
                "SELECT COALESCE(MAX(sequence),0)+1 FROM iteration WHERE project_id=?",
                (project_id,)).fetchone()[0]
            status = "active" if activate else "planned"
            try:
                con.execute("""INSERT INTO iteration
                    (id,project_id,sequence,title,objective,status,input_versions_json,
                     requirement_ids_json,created_at,updated_at)
                    VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    (iteration_id, project_id, sequence, _required(title, "title"),
                     _required(objective, "objective"), status,
                     _json(input_document_versions), _json(requirement_ids), now, now))
            except sqlite3.IntegrityError as error:
                if activate and "iteration.project_id" in str(error):
                    raise ProjectStoreError("project already has an active iteration") from None
                raise
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_iteration(iteration_id)

    def get_iteration(self, iteration_id: str) -> dict:
        result = self._row("iteration", iteration_id)
        result["input_document_versions"] = json.loads(result.pop("input_versions_json"))
        result["requirement_ids"] = json.loads(result.pop("requirement_ids_json"))
        return result

    def list_iterations(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            rows = con.execute("""SELECT id FROM iteration WHERE project_id=?
                ORDER BY sequence DESC,id DESC""", (project_id,)).fetchall()
        return [self.get_iteration(row["id"]) for row in rows]

    def update_iteration_status(self, iteration_id: str, status: str) -> dict:
        if status not in ITERATION_STATES - {"planned"}:
            raise ValueError("iteration status must be active, completed, or abandoned")
        now = _now()
        with self._transaction() as con:
            row = con.execute("SELECT * FROM iteration WHERE id=?", (iteration_id,)).fetchone()
            if not row:
                raise ProjectStoreError("iteration not found")
            allowed = {
                "planned": {"active", "abandoned"},
                "active": {"completed", "abandoned"},
                "completed": set(),
                "abandoned": set(),
            }
            if status not in allowed[row["status"]]:
                raise ProjectStoreError("invalid iteration status transition")
            if status == "completed":
                tasks = con.execute(
                    "SELECT acceptance_status FROM task WHERE iteration_id=?", (iteration_id,)).fetchall()
                if not tasks or any(task["acceptance_status"] not in {"passed", "waived"}
                                    for task in tasks):
                    raise ProjectStoreError("all iteration tasks require acceptance before completion")
            try:
                con.execute("UPDATE iteration SET status=?,updated_at=?,completed_at=? WHERE id=?",
                            (status, now, now if status in {"completed", "abandoned"} else None,
                             iteration_id))
            except sqlite3.IntegrityError:
                if status == "active":
                    raise ProjectStoreError("project already has an active iteration") from None
                raise
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, row["project_id"]))
        return self.get_iteration(iteration_id)

    def record_acceptance(self, task_id: str, status: str, evidence: list[dict]) -> dict:
        """Record product acceptance separately from engine execution completion."""
        if status not in ACCEPTANCE_STATES - {"pending"}:
            raise ValueError("acceptance status must be passed, failed, or waived")
        if not isinstance(evidence, list) or not all(
                isinstance(item, dict)
                and isinstance(item.get("kind"), str) and item["kind"].strip()
                and isinstance(item.get("summary"), str) and item["summary"].strip()
                for item in evidence):
            raise ValueError("acceptance evidence must contain kind and summary")
        if status != "waived" and not evidence:
            raise ValueError("acceptance evidence is required")
        now = _now()
        with self._transaction() as con:
            task = con.execute(
                "SELECT project_id,kind FROM task WHERE id=?", (task_id,)).fetchone()
            if not task:
                raise ProjectStoreError("task not found")
            if status == "passed" and task["kind"] in {"code", "document"}:
                execution = con.execute("""SELECT application_status FROM execution
                    WHERE task_id=? ORDER BY created_at DESC,id DESC LIMIT 1""",
                    (task_id,)).fetchone()
                if execution and execution["application_status"] in {
                        "pending", "conflict", "failed"}:
                    raise ProjectStoreError(
                        "apply the isolated execution result before passing acceptance")
            con.execute("""UPDATE task SET acceptance_status=?,acceptance_evidence_json=?,
                updated_at=? WHERE id=?""", (status, _json(evidence), now, task_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, task["project_id"]))
        return self.get_task(task_id)

    def save_snapshot(self, project_id: str, snapshot: dict, phase: str,
                      task_id: str | None = None) -> dict:
        if phase not in {"before", "after", "applied", "observed"}:
            raise ValueError("phase must be before, after, applied, or observed")
        payload = _json(snapshot)
        snapshot_id, now = _id("snap"), _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            if task_id:
                self._require_task(con, task_id, project_id)
            con.execute("""INSERT INTO workspace_snapshot
                (id,project_id,task_id,phase,workspace_root,fingerprint,manifest_json,created_at)
                VALUES (?,?,?,?,?,?,?,?)""",
                (snapshot_id, project_id, task_id, phase, snapshot.get("root"),
                 hashlib.sha256(payload.encode()).hexdigest(), payload, now))
            con.execute("UPDATE project SET updated_at=? WHERE id=?", (now, project_id))
        return self.get_snapshot(project_id, snapshot_id)

    def get_snapshot(self, project_id: str, snapshot_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("""SELECT * FROM workspace_snapshot
                WHERE id=? AND project_id=?""", (snapshot_id, project_id)).fetchone()
        if not row:
            raise ProjectStoreError("workspace snapshot not found")
        result = dict(row)
        result["manifest"] = json.loads(result.pop("manifest_json"))
        return result

    def list_snapshots(self, project_id: str) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            rows = con.execute("""SELECT * FROM workspace_snapshot
                WHERE project_id=? ORDER BY created_at DESC,id DESC""", (project_id,)).fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["manifest"] = json.loads(item.pop("manifest_json"))
            result.append(item)
        return result

    def create_execution(self, task_id: str, engine: str, engine_session_id: str,
                         before_snapshot_id: str | None = None,
                         workdir: str = "", input_state: dict | None = None,
                         capabilities: dict | None = None,
                         source_workdir: str = "",
                         application_status: str = "not_applicable") -> dict:
        execution_id, now = _id("exe"), _now()
        if (input_state is not None and not isinstance(input_state, dict)) or \
                (capabilities is not None and not isinstance(capabilities, dict)):
            raise ValueError("execution input_state and capabilities must be objects")
        if application_status not in APPLICATION_STATES:
            raise ValueError("invalid execution application status")
        with self._transaction() as con:
            task = con.execute("SELECT project_id,execution_status FROM task WHERE id=?",
                               (task_id,)).fetchone()
            if not task:
                raise ProjectStoreError("task not found")
            if task["execution_status"] in {
                    "queued", "running", "waiting_permission", "waiting_input"}:
                raise ProjectStoreError("task already has an active execution")
            requirement_ids = json.loads(con.execute(
                "SELECT requirement_ids_json FROM task WHERE id=?", (task_id,)).fetchone()[0])
            for requirement_id in requirement_ids:
                scope = con.execute("SELECT confirmed_scope FROM requirement WHERE id=?",
                                    (requirement_id,)).fetchone()
                if not scope or scope["confirmed_scope"] != "current":
                    raise ProjectStoreError("task has a requirement not confirmed for current scope")
            if before_snapshot_id:
                row = con.execute("""SELECT 1 FROM workspace_snapshot
                    WHERE id=? AND project_id=? AND task_id=? AND phase='before'""",
                    (before_snapshot_id, task["project_id"], task_id)).fetchone()
                if not row:
                    raise ProjectStoreError("before snapshot does not belong to task")
            try:
                con.execute("""INSERT INTO execution
                (id,task_id,engine,engine_session_id,status,before_snapshot_id,
                 workdir,source_workdir,application_status,input_state_json,
                 capabilities_json,raw_state_json,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (execution_id, task_id, _required(engine, "engine"),
                 _required(engine_session_id, "engine_session_id"), "queued",
                 before_snapshot_id, _absolute_path(workdir, "workdir") if workdir else "",
                 _absolute_path(source_workdir, "source_workdir") if source_workdir else "",
                 application_status,
                 _json(input_state or {}), _json(capabilities or {}), "{}", now, now))
            except sqlite3.IntegrityError as error:
                if (workdir and "execution.workdir" in str(error)) or \
                        (source_workdir and "execution.source_workdir" in str(error)):
                    raise ProjectStoreError(
                        "workspace already has an active execution") from None
                raise
            con.execute("UPDATE task SET execution_status='queued',updated_at=? WHERE id=?",
                        (now, task_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, task["project_id"]))
        return self.get_execution(execution_id)

    def record_execution_application(self, execution_id: str, status: str,
                                     state: dict,
                                     applied_snapshot_id: str | None = None) -> dict:
        if status not in APPLICATION_STATES - {"not_applicable", "pending"}:
            raise ValueError("application status must be applied, conflict, or failed")
        if not isinstance(state, dict):
            raise ValueError("application state must be an object")
        now = _now()
        with self._transaction() as con:
            row = con.execute("""SELECT e.application_status,e.task_id,t.project_id
                FROM execution e JOIN task t ON t.id=e.task_id WHERE e.id=?""",
                (execution_id,)).fetchone()
            if not row:
                raise ProjectStoreError("execution not found")
            allowed = {
                "pending": {"applied", "conflict", "failed"},
                "conflict": {"applied", "conflict", "failed"},
                "failed": {"applied", "conflict", "failed"},
                "applied": {"applied"},
                "not_applicable": set(),
            }
            if status not in allowed[row["application_status"]]:
                raise ProjectStoreError("invalid execution application transition")
            if applied_snapshot_id:
                owned = con.execute("""SELECT 1 FROM workspace_snapshot
                    WHERE id=? AND project_id=? AND task_id=? AND phase='applied'""",
                    (applied_snapshot_id, row["project_id"], row["task_id"])).fetchone()
                if not owned:
                    raise ProjectStoreError("applied snapshot does not belong to task")
            con.execute("""UPDATE execution SET application_status=?,
                application_state_json=?,applied_snapshot_id=COALESCE(?,applied_snapshot_id),
                applied_at=?,updated_at=? WHERE id=?""",
                (status, _json(state), applied_snapshot_id,
                 now if status == "applied" else None, now, execution_id))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, row["project_id"]))
        return self.get_execution(execution_id)

    def update_execution(self, execution_id: str, projection: dict,
                         engine_message_id: str | None = None,
                         after_snapshot_id: str | None = None) -> dict:
        state = projection.get("state")
        if state not in EXECUTION_STATES:
            raise ValueError("invalid execution state")
        now = _now()
        with self._transaction() as con:
            row = con.execute("""SELECT e.task_id,e.status,t.project_id FROM execution e
                JOIN task t ON t.id=e.task_id WHERE e.id=?""", (execution_id,)).fetchone()
            if not row:
                raise ProjectStoreError("execution not found")
            allowed = {
                "queued": EXECUTION_STATES,
                "running": EXECUTION_STATES - {"queued"},
                "waiting_permission": EXECUTION_STATES - {"queued"},
                "waiting_input": EXECUTION_STATES - {"queued"},
                "unknown": EXECUTION_STATES - {"queued"},
                "completed": {"completed"},
                "failed": {"failed"},
                "stopped": {"stopped"},
            }
            if state not in allowed[row["status"]]:
                raise ProjectStoreError("invalid execution state transition")
            if after_snapshot_id:
                owned = con.execute("""SELECT 1 FROM workspace_snapshot
                    WHERE id=? AND project_id=? AND task_id=? AND phase='after'""",
                    (after_snapshot_id, row["project_id"], row["task_id"])).fetchone()
                if not owned:
                    raise ProjectStoreError("after snapshot does not belong to task")
            finished_at = now if state in {"completed", "failed", "stopped"} else None
            con.execute("""UPDATE execution SET status=?,engine_message_id=COALESCE(?,engine_message_id),
                after_snapshot_id=COALESCE(?,after_snapshot_id),raw_state_json=?,
                updated_at=?,finished_at=? WHERE id=?""",
                (state, engine_message_id, after_snapshot_id, _json(projection), now,
                 finished_at, execution_id))
            con.execute("UPDATE task SET execution_status=?,updated_at=? WHERE id=?",
                        (state, now, row["task_id"]))
            con.execute("UPDATE project SET updated_at=? WHERE id=?",
                        (now, row["project_id"]))
        return self.get_execution(execution_id)

    def get_execution(self, execution_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("SELECT * FROM execution WHERE id=?", (execution_id,)).fetchone()
        if not row:
            raise ProjectStoreError("execution not found")
        result = dict(row)
        result["raw_state"] = json.loads(result.pop("raw_state_json"))
        result["input_state"] = json.loads(result.pop("input_state_json"))
        result["capabilities"] = json.loads(result.pop("capabilities_json"))
        result["application_state"] = json.loads(result.pop("application_state_json"))
        return result

    def list_executions(self, project_id: str, task_id: str | None = None) -> list[dict]:
        with self._connect() as con:
            self._require_project(con, project_id)
            if task_id:
                self._require_task(con, task_id, project_id)
                rows = con.execute("""SELECT e.id FROM execution e JOIN task t ON t.id=e.task_id
                    WHERE t.project_id=? AND e.task_id=? ORDER BY e.created_at DESC,e.id DESC""",
                    (project_id, task_id)).fetchall()
            else:
                rows = con.execute("""SELECT e.id FROM execution e JOIN task t ON t.id=e.task_id
                    WHERE t.project_id=? ORDER BY e.created_at DESC,e.id DESC""",
                    (project_id,)).fetchall()
        return [self.get_execution(row["id"]) for row in rows]

    def task_context(self, task_id: str) -> dict:
        """Return only Atlas-owned records needed to hand a task to a new engine."""
        task = self.get_task(task_id)
        project = self.get_project(task["project_id"])
        iteration = self.get_iteration(task["iteration_id"]) if task.get("iteration_id") else None
        version_ids = task["input_document_versions"]
        with self._connect() as con:
            documents = []
            if version_ids:
                marks = ",".join("?" for _ in version_ids)
                rows = con.execute(f"""SELECT v.id AS version_id,v.version,v.content,
                    v.content_sha256,v.basis_json,v.created_at,d.id AS document_id,
                    d.kind,d.title FROM document_version v JOIN document d
                    ON d.id=v.document_id WHERE v.id IN ({marks})""", version_ids).fetchall()
                by_id = {row["version_id"]: row for row in rows}
                for version_id in version_ids:
                    row = by_id.get(version_id)
                    if not row:
                        raise ProjectStoreError("task references a missing document version")
                    item = dict(row)
                    item["basis"] = json.loads(item.pop("basis_json"))
                    documents.append(item)
            snapshots = []
            for row in con.execute("""SELECT * FROM workspace_snapshot
                    WHERE task_id=? ORDER BY created_at,id""", (task_id,)).fetchall():
                item = dict(row)
                item["manifest"] = json.loads(item.pop("manifest_json"))
                snapshots.append(item)
            executions = []
            for row in con.execute("""SELECT * FROM execution
                    WHERE task_id=? ORDER BY created_at,id""", (task_id,)).fetchall():
                item = dict(row)
                item["raw_state"] = json.loads(item.pop("raw_state_json"))
                item["input_state"] = json.loads(item.pop("input_state_json"))
                item["capabilities"] = json.loads(item.pop("capabilities_json"))
                item["application_state"] = json.loads(
                    item.pop("application_state_json"))
                executions.append(item)
            requirements = [self.get_requirement(item) for item in task["requirement_ids"]]
            decisions = []
            for row in con.execute("SELECT * FROM decision WHERE project_id=? ORDER BY created_at,id",
                                   (project["id"],)).fetchall():
                item = dict(row)
                item["reference_ids"] = json.loads(item.pop("reference_ids_json"))
                decisions.append(item)
        return {"project": project, "iteration": iteration, "task": task, "documents": documents,
                "requirements": requirements, "decisions": decisions,
                "snapshots": snapshots, "executions": executions}

    def _initialize(self):
        with self._transaction() as con:
            version = con.execute("PRAGMA user_version").fetchone()[0]
            if version not in {0, 1, 2, 3, 4, SCHEMA_VERSION}:
                raise ProjectStoreError(f"unsupported project store schema {version}")
            if version == 1:
                _execute_statements(con, """
                    CREATE TABLE iteration (
                        id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                        sequence INTEGER NOT NULL, title TEXT NOT NULL, objective TEXT NOT NULL,
                        status TEXT NOT NULL, input_versions_json TEXT NOT NULL,
                        requirement_ids_json TEXT NOT NULL, created_at TEXT NOT NULL,
                        updated_at TEXT NOT NULL, completed_at TEXT,
                        UNIQUE(project_id,sequence));
                    ALTER TABLE task ADD COLUMN iteration_id TEXT REFERENCES iteration(id);
                    CREATE UNIQUE INDEX one_active_iteration_per_project
                        ON iteration(project_id) WHERE status='active';
                """)
            _execute_statements(con, """
                CREATE TABLE IF NOT EXISTS project (
                    id TEXT PRIMARY KEY, name TEXT NOT NULL, objective TEXT NOT NULL,
                    workspace TEXT NOT NULL, mode TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS document (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    kind TEXT NOT NULL, title TEXT NOT NULL, current_version INTEGER NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS document_version (
                    id TEXT PRIMARY KEY, document_id TEXT NOT NULL REFERENCES document(id),
                    version INTEGER NOT NULL, content TEXT NOT NULL, content_sha256 TEXT NOT NULL,
                    basis_json TEXT NOT NULL, author TEXT NOT NULL, change_summary TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    UNIQUE(document_id,version));
                CREATE TABLE IF NOT EXISTS iteration (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    sequence INTEGER NOT NULL, title TEXT NOT NULL, objective TEXT NOT NULL,
                    status TEXT NOT NULL, input_versions_json TEXT NOT NULL,
                    requirement_ids_json TEXT NOT NULL, created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL, completed_at TEXT,
                    UNIQUE(project_id,sequence));
                CREATE TABLE IF NOT EXISTS task (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    iteration_id TEXT REFERENCES iteration(id),
                    kind TEXT NOT NULL DEFAULT 'code', title TEXT NOT NULL, objective TEXT NOT NULL,
                    write_paths_json TEXT NOT NULL DEFAULT '[]',
                    verification_commands_json TEXT NOT NULL DEFAULT '[]',
                    execution_status TEXT NOT NULL,
                    acceptance_status TEXT NOT NULL, acceptance_evidence_json TEXT NOT NULL,
                    input_versions_json TEXT NOT NULL, requirement_ids_json TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS reference (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    source_kind TEXT NOT NULL, source_ref TEXT NOT NULL, source_version TEXT NOT NULL,
                    locator TEXT NOT NULL, excerpt TEXT NOT NULL, note TEXT NOT NULL,
                    read_status TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS requirement (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    content TEXT NOT NULL, recommended_scope TEXT, recommendation_reason TEXT NOT NULL,
                    confirmed_scope TEXT, confirmation_reason TEXT NOT NULL,
                    acceptance_json TEXT NOT NULL, reference_ids_json TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS decision (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    statement TEXT NOT NULL, rationale TEXT NOT NULL,
                    reference_ids_json TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS workspace_snapshot (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    task_id TEXT REFERENCES task(id), phase TEXT NOT NULL, workspace_root TEXT,
                    fingerprint TEXT NOT NULL, manifest_json TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS execution (
                    id TEXT PRIMARY KEY, task_id TEXT NOT NULL REFERENCES task(id), engine TEXT NOT NULL,
                    engine_session_id TEXT NOT NULL, engine_message_id TEXT,
                    status TEXT NOT NULL, before_snapshot_id TEXT REFERENCES workspace_snapshot(id),
                    after_snapshot_id TEXT REFERENCES workspace_snapshot(id),
                    applied_snapshot_id TEXT REFERENCES workspace_snapshot(id),
                    workdir TEXT NOT NULL DEFAULT '', source_workdir TEXT NOT NULL DEFAULT '',
                    application_status TEXT NOT NULL DEFAULT 'not_applicable',
                    application_state_json TEXT NOT NULL DEFAULT '{}', applied_at TEXT,
                    input_state_json TEXT NOT NULL DEFAULT '{}',
                    capabilities_json TEXT NOT NULL DEFAULT '{}', raw_state_json TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL, finished_at TEXT);
                CREATE UNIQUE INDEX IF NOT EXISTS one_active_iteration_per_project
                    ON iteration(project_id) WHERE status='active';
            """)
            task_columns = {
                row[1] for row in con.execute("PRAGMA table_info(task)").fetchall()}
            for name, declaration in (
                    ("kind", "TEXT NOT NULL DEFAULT 'code'"),
                    ("write_paths_json", "TEXT NOT NULL DEFAULT '[]'"),
                    ("verification_commands_json", "TEXT NOT NULL DEFAULT '[]'")):
                if name not in task_columns:
                    con.execute(f"ALTER TABLE task ADD COLUMN {name} {declaration}")
            execution_columns = {
                row[1] for row in con.execute("PRAGMA table_info(execution)").fetchall()}
            for name, declaration in (
                    ("workdir", "TEXT NOT NULL DEFAULT ''"),
                    ("source_workdir", "TEXT NOT NULL DEFAULT ''"),
                    ("application_status", "TEXT NOT NULL DEFAULT 'not_applicable'"),
                    ("application_state_json", "TEXT NOT NULL DEFAULT '{}'"),
                    ("applied_snapshot_id", "TEXT REFERENCES workspace_snapshot(id)"),
                    ("applied_at", "TEXT"),
                    ("input_state_json", "TEXT NOT NULL DEFAULT '{}'"),
                    ("capabilities_json", "TEXT NOT NULL DEFAULT '{}'")):
                if name not in execution_columns:
                    con.execute(f"ALTER TABLE execution ADD COLUMN {name} {declaration}")
            con.execute("""CREATE UNIQUE INDEX IF NOT EXISTS one_active_execution_per_workdir
                ON execution(workdir) WHERE workdir != '' AND status IN
                ('queued','running','waiting_permission','waiting_input')""")
            con.execute("""CREATE UNIQUE INDEX IF NOT EXISTS one_active_execution_per_source
                ON execution(source_workdir) WHERE source_workdir != '' AND status IN
                ('queued','running','waiting_permission','waiting_input')""")
            version_columns = {
                row[1] for row in con.execute("PRAGMA table_info(document_version)").fetchall()}
            if "author" not in version_columns:
                con.execute("ALTER TABLE document_version ADD COLUMN author TEXT NOT NULL DEFAULT 'unknown'")
            if "change_summary" not in version_columns:
                con.execute("ALTER TABLE document_version ADD COLUMN change_summary TEXT NOT NULL DEFAULT ''")
            con.execute(f"PRAGMA user_version={SCHEMA_VERSION}")

    @contextmanager
    def _connect(self):
        con = sqlite3.connect(self.path, timeout=10)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys=ON")
        try:
            yield con
        finally:
            con.close()

    @contextmanager
    def _transaction(self):
        with self._connect() as con:
            con.execute("BEGIN IMMEDIATE")
            try:
                yield con
                con.commit()
            except BaseException:
                con.rollback()
                raise

    @staticmethod
    def _insert_version(con, version_id, document_id, number, content, basis, now,
                        author, change_summary):
        if not isinstance(content, str):
            raise ValueError("content must be text")
        if author not in DOCUMENT_AUTHORS:
            raise ValueError("invalid document author")
        if not isinstance(change_summary, str):
            raise ValueError("change_summary must be text")
        con.execute("""INSERT INTO document_version
            (id,document_id,version,content,content_sha256,basis_json,author,
             change_summary,created_at) VALUES (?,?,?,?,?,?,?,?,?)""",
            (version_id, document_id, number, content,
             hashlib.sha256(content.encode()).hexdigest(), _json(basis or []),
             author, change_summary, now))

    @staticmethod
    def _require_project(con, project_id):
        if not con.execute("SELECT 1 FROM project WHERE id=?", (project_id,)).fetchone():
            raise ProjectStoreError("project not found")

    @staticmethod
    def _require_task(con, task_id, project_id):
        if not con.execute("SELECT 1 FROM task WHERE id=? AND project_id=?",
                           (task_id, project_id)).fetchone():
            raise ProjectStoreError("task does not belong to project")

    @staticmethod
    def _require_references(con, project_id, reference_ids):
        for reference_id in reference_ids:
            if not con.execute("SELECT 1 FROM reference WHERE id=? AND project_id=?",
                               (reference_id, project_id)).fetchone():
                raise ProjectStoreError("reference does not belong to project")

    @staticmethod
    def _require_document_versions(con, project_id, version_ids):
        for version_id in version_ids:
            if not con.execute("""SELECT 1 FROM document_version v JOIN document d
                    ON d.id=v.document_id WHERE v.id=? AND d.project_id=?""",
                    (version_id, project_id)).fetchone():
                raise ProjectStoreError("document version does not belong to project")

    @staticmethod
    def _normalize_basis(con, project_id, basis):
        if not isinstance(basis, list):
            raise ValueError("basis must be a list")
        seen = set()
        normalized = []
        for item in basis:
            if not isinstance(item, dict):
                raise ValueError("basis entries must be objects")
            if "source" in item and "fingerprint" in item:
                if not isinstance(item["source"], str) or not isinstance(item["fingerprint"], str):
                    raise ValueError("external basis source and fingerprint must be text")
                normalized.append(dict(item))
                continue
            kind, item_id = item.get("kind"), item.get("id")
            if kind not in {"reference", "requirement", "decision", "document_version",
                            "workspace_baseline"} \
                    or not isinstance(item_id, str):
                raise ValueError("invalid basis entry")
            key = (kind, item_id)
            if key in seen:
                raise ValueError("duplicate basis entry")
            seen.add(key)
            if kind == "document_version":
                row = con.execute("""SELECT v.content_sha256,v.version FROM document_version v
                    JOIN document d
                    ON d.id=v.document_id WHERE v.id=? AND d.project_id=?""",
                    (item_id, project_id)).fetchone()
                value = {"kind": kind, "id": item_id, "version": row["version"],
                         "fingerprint": row["content_sha256"]} if row else None
            elif kind == "workspace_baseline":
                row = con.execute("""SELECT fingerprint,created_at,manifest_json
                    FROM workspace_snapshot WHERE id=? AND project_id=? AND phase='observed'""",
                    (item_id, project_id)).fetchone()
                try:
                    is_baseline = row and json.loads(row["manifest_json"]).get("purpose") \
                        == "project-baseline"
                except (TypeError, ValueError):
                    is_baseline = False
                value = {"kind": kind, "id": item_id, "version": row["created_at"],
                         "fingerprint": row["fingerprint"]} if is_baseline else None
            elif kind == "reference":
                row = con.execute("""SELECT source_version FROM reference
                    WHERE id=? AND project_id=?""", (item_id, project_id)).fetchone()
                value = {"kind": kind, "id": item_id,
                         "version": row["source_version"]} if row else None
            elif kind == "requirement":
                row = con.execute("""SELECT content,recommended_scope,recommendation_reason,
                    confirmed_scope,confirmation_reason,acceptance_json,reference_ids_json,updated_at
                    FROM requirement WHERE id=? AND project_id=?""",
                    (item_id, project_id)).fetchone()
                if row:
                    payload = _json({key: row[key] for key in row.keys() if key != "updated_at"})
                    value = {"kind": kind, "id": item_id, "version": row["updated_at"],
                             "fingerprint": hashlib.sha256(payload.encode()).hexdigest()}
                else:
                    value = None
            else:
                row = con.execute("""SELECT created_at FROM decision
                    WHERE id=? AND project_id=?""", (item_id, project_id)).fetchone()
                value = {"kind": kind, "id": item_id,
                         "version": row["created_at"]} if row else None
            if value is None:
                raise ProjectStoreError(f"basis {kind} does not belong to project")
            normalized.append(value)
        return normalized

    def _document_review(self, project_id, basis, version_created_at):
        reasons = []
        with self._connect() as con:
            for item in basis:
                if not isinstance(item, dict):
                    continue
                if item.get("kind") == "requirement":
                    row = con.execute("""SELECT content,recommended_scope,recommendation_reason,
                        confirmed_scope,confirmation_reason,acceptance_json,reference_ids_json,
                        updated_at FROM requirement WHERE id=? AND project_id=?""",
                        (item.get("id"), project_id)).fetchone()
                    if row and item.get("fingerprint"):
                        payload = _json({key: row[key] for key in row.keys() if key != "updated_at"})
                        changed = item["fingerprint"] != hashlib.sha256(payload.encode()).hexdigest()
                    else:
                        changed = row and (
                            (item.get("version") is not None and item["version"] != row["updated_at"])
                            or (item.get("version") is None and row["updated_at"] > version_created_at))
                    if changed:
                        reasons.append({"kind": "requirement_changed", "id": item["id"]})
                elif item.get("kind") == "document_version":
                    row = con.execute("""SELECT d.current_version,v.version,d.id AS document_id
                        FROM document_version v JOIN document d ON d.id=v.document_id
                        WHERE v.id=? AND d.project_id=?""",
                        (item.get("id"), project_id)).fetchone()
                    if row and row["version"] != row["current_version"]:
                        reasons.append({"kind": "upstream_document_changed",
                                        "id": item["id"], "document_id": row["document_id"]})
                elif item.get("kind") == "workspace_baseline":
                    rows = con.execute("""SELECT id,manifest_json FROM workspace_snapshot
                        WHERE project_id=? AND phase='observed'
                        ORDER BY created_at DESC,id DESC""", (project_id,)).fetchall()
                    current_id = None
                    for row in rows:
                        try:
                            if json.loads(row["manifest_json"]).get("purpose") == "project-baseline":
                                current_id = row["id"]
                                break
                        except (TypeError, ValueError):
                            continue
                    if current_id and current_id != item.get("id"):
                        reasons.append({"kind": "workspace_baseline_changed",
                                        "id": item["id"],
                                        "current_baseline_id": current_id})
        return {"status": "needs_review" if reasons else "current", "reasons": reasons}

    def _row(self, table: str, item_id: str) -> dict:
        if table not in {"reference", "requirement", "decision", "iteration"}:
            raise ValueError("unknown table")
        with self._connect() as con:
            row = con.execute(f"SELECT * FROM {table} WHERE id=?", (item_id,)).fetchone()
        if not row:
            raise ProjectStoreError(f"{table} not found")
        return dict(row)


def _id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex}"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds")


def _json(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _required(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required")
    return value.strip()


def _text_list(values, name: str, maximum: int) -> list[str]:
    if not isinstance(values, list) or len(values) > maximum:
        raise ValueError(f"{name} must be a list of at most {maximum} entries")
    result = []
    for value in values:
        text = _required(value, name)
        if text not in result:
            result.append(text)
    return result


def _relative_paths(values, name: str) -> list[str]:
    result = []
    for value in _text_list(values, name, 50):
        normalized = value.replace("\\", "/").rstrip("/") or "."
        path = Path(normalized)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"{name} must stay inside the execution workspace")
        normalized = path.as_posix()
        if normalized not in result:
            result.append(normalized)
    return result


def _absolute_path(value: str, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required")
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise ValueError(f"{name} must be an absolute path")
    return str(path.resolve())


def _execute_statements(con: sqlite3.Connection, script: str):
    """Execute simple schema DDL without sqlite3.executescript's implicit commit."""
    for statement in script.split(";"):
        if statement.strip():
            con.execute(statement)
