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


SCHEMA_VERSION = 1
PROJECT_MODES = {"new", "existing"}
TASK_STATES = {"planned", "queued", "running", "waiting_permission",
               "waiting_input", "completed", "failed", "stopped", "unknown"}
EXECUTION_STATES = TASK_STATES - {"planned"}
ACCEPTANCE_STATES = {"pending", "passed", "failed", "waived"}
SCOPE_STATES = {"current", "later", "excluded"}
READ_STATES = {"unread", "read", "reviewed"}


class ProjectStoreError(RuntimeError):
    pass


class ProjectStore:
    def __init__(self, path: str | Path | None = None):
        configured = os.environ.get("ATLAS_PROJECT_STORE")
        self.path = Path(path or configured or PACK / "projects/atlas-projects.sqlite").resolve()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def create_project(self, name: str, objective: str, workspace: str | Path,
                       mode: str) -> dict:
        if mode not in PROJECT_MODES:
            raise ValueError("mode must be new or existing")
        project_id = _id("prj")
        now = _now()
        workspace = str(Path(workspace).expanduser().resolve())
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

    def create_document(self, project_id: str, kind: str, title: str, content: str,
                        basis: list[dict] | None = None) -> dict:
        document_id, version_id = _id("doc"), _id("dver")
        now = _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            con.execute("""INSERT INTO document
                (id,project_id,kind,title,current_version,created_at,updated_at)
                VALUES (?,?,?,?,1,?,?)""",
                (document_id, project_id, _required(kind, "kind"),
                 _required(title, "title"), now, now))
            self._insert_version(con, version_id, document_id, 1, content, basis, now)
        return self.get_document(document_id)

    def add_document_version(self, document_id: str, content: str,
                             basis: list[dict] | None = None,
                             expected_current_version: int | None = None) -> dict:
        now, version_id = _now(), _id("dver")
        with self._transaction() as con:
            document = con.execute(
                "SELECT current_version FROM document WHERE id=?", (document_id,)).fetchone()
            if not document:
                raise ProjectStoreError("document not found")
            current = document["current_version"]
            if expected_current_version is not None and current != expected_current_version:
                raise ProjectStoreError("document version conflict")
            number = current + 1
            self._insert_version(con, version_id, document_id, number, content, basis, now)
            con.execute("UPDATE document SET current_version=?,updated_at=? WHERE id=?",
                        (number, now, document_id))
        return self.get_document(document_id)

    def get_document(self, document_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("""SELECT d.*,v.id AS version_id,v.content,v.content_sha256,
                v.basis_json,v.created_at AS version_created_at
                FROM document d JOIN document_version v
                ON v.document_id=d.id AND v.version=d.current_version WHERE d.id=?""",
                (document_id,)).fetchone()
        if not row:
            raise ProjectStoreError("document not found")
        result = dict(row)
        result["basis"] = json.loads(result.pop("basis_json"))
        return result

    def create_task(self, project_id: str, title: str, objective: str,
                    input_document_versions: list[str] | None = None,
                    requirement_ids: list[str] | None = None) -> dict:
        task_id, now = _id("tsk"), _now()
        versions = input_document_versions or []
        requirements = requirement_ids or []
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
            con.execute("""INSERT INTO task
                (id,project_id,title,objective,execution_status,acceptance_status,
                 acceptance_evidence_json,input_versions_json,requirement_ids_json,
                 created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (task_id, project_id, _required(title, "title"),
                 _required(objective, "objective"), "planned", "pending", "[]",
                 _json(versions), _json(requirements), now, now))
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
        return result

    def add_reference(self, project_id: str, source_kind: str, source_ref: str,
                      source_version: str, locator: str = "", excerpt: str = "",
                      note: str = "", read_status: str = "unread") -> dict:
        if read_status not in READ_STATES:
            raise ValueError("invalid read status")
        reference_id, now = _id("ref"), _now()
        with self._transaction() as con:
            self._require_project(con, project_id)
            con.execute("""INSERT INTO reference
                (id,project_id,source_kind,source_ref,source_version,locator,excerpt,note,
                 read_status,created_at,updated_at) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                (reference_id, project_id, _required(source_kind, "source_kind"),
                 _required(source_ref, "source_ref"), _required(source_version, "source_version"),
                 locator, excerpt, note, read_status, now, now))
        return self._row("reference", reference_id)

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
        return self.get_requirement(requirement_id)

    def confirm_requirement(self, requirement_id: str, scope: str, reason: str) -> dict:
        if scope not in SCOPE_STATES:
            raise ValueError("invalid confirmed scope")
        now = _now()
        with self._transaction() as con:
            if not con.execute("SELECT 1 FROM requirement WHERE id=?", (requirement_id,)).fetchone():
                raise ProjectStoreError("requirement not found")
            con.execute("""UPDATE requirement SET confirmed_scope=?,confirmation_reason=?,
                updated_at=? WHERE id=?""", (scope, _required(reason, "reason"), now, requirement_id))
        return self.get_requirement(requirement_id)

    def get_requirement(self, requirement_id: str) -> dict:
        result = self._row("requirement", requirement_id)
        result["acceptance_conditions"] = json.loads(result.pop("acceptance_json"))
        result["reference_ids"] = json.loads(result.pop("reference_ids_json"))
        return result

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
        result = self._row("decision", decision_id)
        result["reference_ids"] = json.loads(result.pop("reference_ids_json"))
        return result

    def record_acceptance(self, task_id: str, status: str, evidence: list[dict]) -> dict:
        """Record product acceptance separately from engine execution completion."""
        if status not in ACCEPTANCE_STATES - {"pending"}:
            raise ValueError("acceptance status must be passed, failed, or waived")
        if status != "waived" and not evidence:
            raise ValueError("acceptance evidence is required")
        now = _now()
        with self._transaction() as con:
            if not con.execute("SELECT 1 FROM task WHERE id=?", (task_id,)).fetchone():
                raise ProjectStoreError("task not found")
            con.execute("""UPDATE task SET acceptance_status=?,acceptance_evidence_json=?,
                updated_at=? WHERE id=?""", (status, _json(evidence), now, task_id))
        return self.get_task(task_id)

    def save_snapshot(self, project_id: str, snapshot: dict, phase: str,
                      task_id: str | None = None) -> dict:
        if phase not in {"before", "after", "observed"}:
            raise ValueError("phase must be before, after, or observed")
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
        return {"id": snapshot_id, "phase": phase,
                "fingerprint": hashlib.sha256(payload.encode()).hexdigest()}

    def create_execution(self, task_id: str, engine: str, engine_session_id: str,
                         before_snapshot_id: str | None = None) -> dict:
        execution_id, now = _id("exe"), _now()
        with self._transaction() as con:
            task = con.execute("SELECT project_id FROM task WHERE id=?", (task_id,)).fetchone()
            if not task:
                raise ProjectStoreError("task not found")
            requirement_ids = json.loads(con.execute(
                "SELECT requirement_ids_json FROM task WHERE id=?", (task_id,)).fetchone()[0])
            for requirement_id in requirement_ids:
                scope = con.execute("SELECT confirmed_scope FROM requirement WHERE id=?",
                                    (requirement_id,)).fetchone()
                if not scope or scope["confirmed_scope"] != "current":
                    raise ProjectStoreError("task has a requirement not confirmed for current scope")
            if before_snapshot_id:
                row = con.execute("""SELECT 1 FROM workspace_snapshot
                    WHERE id=? AND project_id=?""", (before_snapshot_id, task["project_id"])).fetchone()
                if not row:
                    raise ProjectStoreError("snapshot does not belong to project")
            con.execute("""INSERT INTO execution
                (id,task_id,engine,engine_session_id,status,before_snapshot_id,
                 raw_state_json,created_at,updated_at)
                VALUES (?,?,?,?,?,?,?,?,?)""",
                (execution_id, task_id, _required(engine, "engine"),
                 _required(engine_session_id, "engine_session_id"), "queued",
                 before_snapshot_id, "{}", now, now))
            con.execute("UPDATE task SET execution_status='queued',updated_at=? WHERE id=?",
                        (now, task_id))
        return self.get_execution(execution_id)

    def update_execution(self, execution_id: str, projection: dict,
                         engine_message_id: str | None = None,
                         after_snapshot_id: str | None = None) -> dict:
        state = projection.get("state")
        if state not in EXECUTION_STATES:
            raise ValueError("invalid execution state")
        now = _now()
        with self._transaction() as con:
            row = con.execute("""SELECT e.task_id,t.project_id FROM execution e
                JOIN task t ON t.id=e.task_id WHERE e.id=?""", (execution_id,)).fetchone()
            if not row:
                raise ProjectStoreError("execution not found")
            if after_snapshot_id:
                owned = con.execute("""SELECT 1 FROM workspace_snapshot
                    WHERE id=? AND project_id=?""", (after_snapshot_id, row["project_id"])).fetchone()
                if not owned:
                    raise ProjectStoreError("snapshot does not belong to project")
            finished_at = now if state in {"completed", "failed", "stopped"} else None
            con.execute("""UPDATE execution SET status=?,engine_message_id=COALESCE(?,engine_message_id),
                after_snapshot_id=COALESCE(?,after_snapshot_id),raw_state_json=?,
                updated_at=?,finished_at=? WHERE id=?""",
                (state, engine_message_id, after_snapshot_id, _json(projection), now,
                 finished_at, execution_id))
            con.execute("UPDATE task SET execution_status=?,updated_at=? WHERE id=?",
                        (state, now, row["task_id"]))
        return self.get_execution(execution_id)

    def get_execution(self, execution_id: str) -> dict:
        with self._connect() as con:
            row = con.execute("SELECT * FROM execution WHERE id=?", (execution_id,)).fetchone()
        if not row:
            raise ProjectStoreError("execution not found")
        result = dict(row)
        result["raw_state"] = json.loads(result.pop("raw_state_json"))
        return result

    def task_context(self, task_id: str) -> dict:
        """Return only Atlas-owned records needed to hand a task to a new engine."""
        task = self.get_task(task_id)
        project = self.get_project(task["project_id"])
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
                executions.append(item)
            requirements = [self.get_requirement(item) for item in task["requirement_ids"]]
            decisions = []
            for row in con.execute("SELECT * FROM decision WHERE project_id=? ORDER BY created_at,id",
                                   (project["id"],)).fetchall():
                item = dict(row)
                item["reference_ids"] = json.loads(item.pop("reference_ids_json"))
                decisions.append(item)
        return {"project": project, "task": task, "documents": documents,
                "requirements": requirements, "decisions": decisions,
                "snapshots": snapshots, "executions": executions}

    def _initialize(self):
        with self._transaction() as con:
            version = con.execute("PRAGMA user_version").fetchone()[0]
            if version not in {0, SCHEMA_VERSION}:
                raise ProjectStoreError(f"unsupported project store schema {version}")
            con.executescript("""
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
                    basis_json TEXT NOT NULL, created_at TEXT NOT NULL,
                    UNIQUE(document_id,version));
                CREATE TABLE IF NOT EXISTS task (
                    id TEXT PRIMARY KEY, project_id TEXT NOT NULL REFERENCES project(id),
                    title TEXT NOT NULL, objective TEXT NOT NULL, execution_status TEXT NOT NULL,
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
                    after_snapshot_id TEXT REFERENCES workspace_snapshot(id), raw_state_json TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL, finished_at TEXT);
            """)
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
    def _insert_version(con, version_id, document_id, number, content, basis, now):
        if not isinstance(content, str):
            raise ValueError("content must be text")
        con.execute("""INSERT INTO document_version
            (id,document_id,version,content,content_sha256,basis_json,created_at)
            VALUES (?,?,?,?,?,?,?)""",
            (version_id, document_id, number, content,
             hashlib.sha256(content.encode()).hexdigest(), _json(basis or []), now))

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

    def _row(self, table: str, item_id: str) -> dict:
        if table not in {"reference", "requirement", "decision"}:
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
