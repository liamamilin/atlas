"""Durable, versioned factory state. Agent output never changes job ownership."""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import time
import uuid


class FactoryError(ValueError):
    def __init__(self, message, code="invalid_request", status=400):
        super().__init__(message)
        self.code, self.status = code, status


def now():
    return datetime.now(timezone.utc).isoformat()


def uid(prefix):
    return prefix + "_" + uuid.uuid4().hex


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def text(value, name, maximum=8000):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise FactoryError(
            f"{name} must be non-empty text (up to {maximum} characters)"
        )
    return value.strip()


def lines(value, name):
    if not isinstance(value, list) or not value or len(value) > 50:
        raise FactoryError(f"{name} must contain 1–50 items")
    return [text(item, name, 2000) for item in value]


def integer(value, name, minimum, maximum):
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or not minimum <= value <= maximum
    ):
        raise FactoryError(f"{name} must be between {minimum} and {maximum}")
    return value


class FactoryStore:
    def __init__(self, root, pack):
        raw = Path(root).expanduser().absolute()
        if any(p.is_symlink() for p in (raw, *raw.parents)):
            # /tmp is an OS symlink on macOS; compare resolved parents instead.
            raw = raw.resolve()
        self.root, self.pack = raw.resolve(), Path(pack).resolve()
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.path = self.root / "factory.sqlite"
        if self.path.is_symlink():
            raise FactoryError("factory database must not be a symlink")
        with self.connect() as con:
            # UI readers and scheduler heartbeats must not block each other's
            # commits. SQLite still serializes writers and preserves fencing.
            con.execute("PRAGMA journal_mode=WAL")
            con.executescript("""
            CREATE TABLE IF NOT EXISTS scenario (
              id TEXT PRIMARY KEY, leaf TEXT NOT NULL, revision INTEGER NOT NULL,
              status TEXT NOT NULL, body TEXT NOT NULL, updated_at TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS scenario_history (
              id TEXT NOT NULL, revision INTEGER NOT NULL, body TEXT NOT NULL,
              PRIMARY KEY(id,revision));
            CREATE TABLE IF NOT EXISTS scenario_review (
              id TEXT PRIMARY KEY, scenario_id TEXT NOT NULL, revision INTEGER NOT NULL,
              job_id TEXT NOT NULL UNIQUE, body TEXT NOT NULL, created_at TEXT NOT NULL);
            CREATE INDEX IF NOT EXISTS scenario_review_scene ON scenario_review(scenario_id,created_at);
            CREATE TABLE IF NOT EXISTS batch (
              id TEXT PRIMARY KEY, state TEXT NOT NULL, config TEXT NOT NULL,
              created_at TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS job (
              id TEXT PRIMARY KEY, batch_id TEXT NOT NULL, kind TEXT NOT NULL,
              state TEXT NOT NULL, stage TEXT NOT NULL, attempt INTEGER NOT NULL,
              token TEXT, lease REAL, snapshot TEXT NOT NULL, error TEXT,
              created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
            CREATE INDEX IF NOT EXISTS job_batch ON job(batch_id,state);
            CREATE TABLE IF NOT EXISTS event (
              seq INTEGER PRIMARY KEY AUTOINCREMENT, job_id TEXT NOT NULL,
              attempt INTEGER NOT NULL, at TEXT NOT NULL, stage TEXT NOT NULL,
              message TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS checkpoint (
              job_id TEXT NOT NULL,name TEXT NOT NULL,body TEXT NOT NULL,
              PRIMARY KEY(job_id,name));
            CREATE TABLE IF NOT EXISTS acceptance (
              id TEXT PRIMARY KEY, artifact_id TEXT NOT NULL, digest TEXT NOT NULL,
              method TEXT NOT NULL, job_id TEXT NOT NULL, body TEXT NOT NULL,
              created_at TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS artifact (
              id TEXT PRIMARY KEY, job_id TEXT NOT NULL UNIQUE, digest TEXT NOT NULL,
              level TEXT NOT NULL, state TEXT NOT NULL, body TEXT NOT NULL,
              created_at TEXT NOT NULL);
            """)
        os.chmod(self.path, 0o600)
        from .v1_batches import migrate as migrate_batches
        migrate_batches(self)
        if (self.pack / "mvp_apps.json").is_file():
            from .migrations import migrate as migrate_cases
            migrate_cases(self)

    @contextmanager
    def connect(self, write=False):
        con = sqlite3.connect(self.path, timeout=30)
        con.row_factory = sqlite3.Row
        con.execute("PRAGMA foreign_keys=ON")
        con.execute("PRAGMA busy_timeout=30000")
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

    def leaf(self, slug):
        if not isinstance(slug, str) or not re.fullmatch(
            r"[a-z0-9][a-z0-9-]{0,199}", slug
        ):
            raise FactoryError("invalid leaf slug")
        db = self.pack / "atlas/atlas.sqlite"
        if not db.is_file():
            raise FactoryError(
                "Atlas corpus index is unavailable", "corpus_unavailable", 503
            )
        con = sqlite3.connect(db.as_uri() + "?mode=ro", uri=True)
        try:
            row = con.execute(
                "SELECT name,name_zh,defining_core,overview FROM leaf WHERE slug=?",
                (slug,),
            ).fetchone()
        finally:
            con.close()
        if not row:
            raise FactoryError("leaf not found", "not_found", 404)
        source = self.pack / "applications" / (slug + ".md")
        content = (
            source.read_text()
            if source.is_file()
            else "\n\n".join(str(x or "") for x in row)
        )
        return {
            "slug": slug,
            "name": row[0],
            "name_zh": row[1],
            "content": content,
            "fingerprint": hashlib.sha256(content.encode()).hexdigest(),
        }

    def complete_scenario_proposals(self, job_id, token, items, reason=""):
        # Token check, draft insertion and job completion share one transaction.
        # Cancellation cannot leave half a proposal set or late successful work.
        at = now()
        with self.connect(True) as con:
            row = con.execute(
                "SELECT * FROM job WHERE id=? AND kind='scenarios' AND token=? AND state='running' AND lease>?",
                (job_id, token, time.time()),
            ).fetchone()
            if not row:
                raise FactoryError(
                    "scenario proposal ownership lost", "lease_lost", 409
                )
            created = []
            for item in items:
                leaf = self.leaf(item["leaf"])
                body = {
                    **item,
                    "id": uid("scn"),
                    "revision": 1,
                    "status": "draft",
                    "leaf_name": leaf["name_zh"] or leaf["name"],
                    "updated_at": at,
                }
                con.execute(
                    "INSERT INTO scenario VALUES(?,?,?,?,?,?)",
                    (body["id"], body["leaf"], 1, "draft", canonical(body), at),
                )
                con.execute(
                    "INSERT INTO scenario_history VALUES(?,?,?)",
                    (body["id"], 1, canonical(body)),
                )
                created.append(body)
            # A separate CLI job reviews each saved draft. Generation remains
            # successful even when its independent review later fails.
            snapshot = json.loads(row["snapshot"])
            for body in created:
                self._queue_scenario_review(
                    con, row["batch_id"], body, snapshot["config"], snapshot["leaf"]
                )
            result = {
                "count": len(created),
                "reason": reason,
                "scenario_ids": [body["id"] for body in created],
            }
            con.execute(
                "INSERT INTO checkpoint VALUES(?,?,?)",
                (
                    job_id,
                    "scenario_proposals",
                    canonical({"result": result, "digest": digest(result)}),
                ),
            )
            con.execute(
                "UPDATE job SET state='completed',stage='completed',updated_at=? WHERE id=?",
                (at, job_id),
            )
            con.execute(
                "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                (
                    job_id,
                    row["attempt"],
                    at,
                    "completed",
                    (
                        "Scenario drafts created; independent reviews queued; human confirmation required"
                        if created
                        else "No new distinct scenarios: " + reason
                    ),
                ),
            )

    def scenarios(self, leaf=None):
        with self.connect() as con:
            rows = con.execute(
                "SELECT body FROM scenario"
                + (" WHERE leaf=?" if leaf else "")
                + " ORDER BY updated_at DESC",
                (leaf,) if leaf else (),
            ).fetchall()
            reviews = [
                json.loads(r[0])
                for r in con.execute(
                    "SELECT body FROM scenario_review ORDER BY created_at DESC,id DESC"
                )
            ]
            jobs = [
                self._job(r)
                for r in con.execute(
                    "SELECT * FROM job WHERE kind='scenario-review' ORDER BY created_at DESC,id DESC"
                )
            ]
        values = [json.loads(r[0]) for r in rows]
        from .scenario_review import scenario_input

        reviews_by_scene, jobs_by_scene = {}, {}
        for review in reviews:
            reviews_by_scene.setdefault(review["scenario_id"], []).append(review)
        for job in jobs:
            jobs_by_scene.setdefault(job["snapshot"]["scenario"]["id"], []).append(job)
        peer_groups = {}
        for value in sorted(values, key=lambda v: v["id"]):
            if value["status"] != "archived":
                peer_groups.setdefault(value["leaf"], []).append(scenario_input(value))
        # Currentness includes the leaf and peer context, as well as scene revision.
        fingerprints = {}
        for value in values:
            slug = value["leaf"]
            scene_reviews = reviews_by_scene.get(value["id"], [])
            scene_jobs = jobs_by_scene.get(value["id"], [])
            if not scene_reviews and not scene_jobs:
                value["reviews"], value["review_jobs"] = [], []
                continue
            if slug not in fingerprints:
                try:
                    fingerprints[slug] = self.leaf(slug)["fingerprint"]
                except FactoryError:
                    fingerprints[slug] = None
            peers = [p for p in peer_groups.get(slug, []) if p["id"] != value["id"]]
            peer_digest = digest(peers)
            value["reviews"] = [
                {
                    **r,
                    "current": r["scenario_revision"] == value["revision"]
                    and r["leaf_fingerprint"] == fingerprints[slug]
                    and r["peer_digest"] == peer_digest,
                }
                for r in scene_reviews
            ]
            value["review_jobs"] = [
                {
                    "id": j["id"],
                    "state": j["state"],
                    "error": j["error"],
                    "scenario_revision": j["snapshot"]["scenario"]["revision"],
                    "current": j["snapshot"]["scenario"]["revision"]
                    == value["revision"]
                    and j["snapshot"]["leaf"]["fingerprint"] == fingerprints[slug]
                    and j["snapshot"]["peer_digest"] == peer_digest,
                }
                for j in scene_jobs
            ]
        return values

    @staticmethod
    def _scenario_peers(con, scenario):
        from .scenario_review import scenario_input

        return [
            scenario_input(json.loads(row[0]))
            for row in con.execute(
                "SELECT body FROM scenario WHERE leaf=? AND id<>? AND status<>'archived' ORDER BY id",
                (scenario["leaf"], scenario["id"]),
            )
        ]

    def _queue_scenario_review(self, con, batch_id, scenario, config, leaf=None):
        from .scenario_review import scenario_input

        leaf = leaf or self.leaf(scenario["leaf"])
        peers = self._scenario_peers(con, scenario)
        snapshot = {
            "leaf": leaf,
            "scenario": scenario_input(scenario),
            "peer_scenarios": peers,
            "peer_digest": digest(peers),
            "config": {**config, "kind": "scenario-review"},
        }
        snapshot["input_digest"] = digest(
            {
                "leaf_fingerprint": leaf["fingerprint"],
                "scenario": snapshot["scenario"],
                "peer_scenarios": peers,
            }
        )
        if con.execute(
            "SELECT 1 FROM job WHERE kind='scenario-review' AND state IN ('queued','running') "
            "AND json_extract(snapshot,'$.input_digest')=?",
            (snapshot["input_digest"],),
        ).fetchone():
            raise FactoryError(
                "this scenario review is already queued or running", "conflict", 409
            )
        at = now()
        con.execute(
            "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
            (
                uid("job"),
                batch_id,
                "scenario-review",
                "queued",
                "scenario-review",
                1,
                None,
                None,
                canonical(snapshot),
                None,
                at,
                at,
            ),
        )

    def complete_scenario_review(self, job_id, token, result):
        from .scenario_review import validate_review
        from privacy import redact_value

        with self.connect(True) as con:
            row = con.execute(
                "SELECT * FROM job WHERE id=? AND kind='scenario-review' AND token=? "
                "AND state='running' AND lease>?",
                (job_id, token, time.time()),
            ).fetchone()
            if not row:
                raise FactoryError("scenario review ownership lost", "lease_lost", 409)
            snapshot = json.loads(row["snapshot"])
            report = validate_review(result, snapshot)
            body = redact_value(
                {
                    **report,
                    "id": uid("scv"),
                    "scenario_id": snapshot["scenario"]["id"],
                    "scenario_revision": snapshot["scenario"]["revision"],
                    "job_id": job_id,
                    "leaf_fingerprint": snapshot["leaf"]["fingerprint"],
                    "peer_digest": snapshot["peer_digest"],
                    "input_digest": snapshot["input_digest"],
                    "peer_scenarios": [
                        {"id": p["id"], "name": p["name"], "revision": p["revision"]}
                        for p in snapshot["peer_scenarios"]
                    ],
                    "model": snapshot["config"]["model"],
                    "created_at": now(),
                    "scope": "Independent model review of pinned leaf, scenario and supplied same-leaf peers; human confirmation required; no runtime or market validation.",
                }
            )
            con.execute(
                "INSERT INTO scenario_review VALUES(?,?,?,?,?,?)",
                (
                    body["id"],
                    body["scenario_id"],
                    body["scenario_revision"],
                    job_id,
                    canonical(body),
                    body["created_at"],
                ),
            )
            con.execute(
                "UPDATE job SET state='completed',stage='scenario-review',updated_at=? WHERE id=?",
                (now(), job_id),
            )
            con.execute(
                "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                (
                    job_id,
                    row["attempt"],
                    now(),
                    "scenario-review",
                    "Scenario review: " + body["outcome"],
                ),
            )
        return body

    def scenario(self, scenario_id):
        with self.connect() as con:
            row = con.execute(
                "SELECT body FROM scenario WHERE id=?", (scenario_id,)
            ).fetchone()
        if not row:
            raise FactoryError("scenario not found", "not_found", 404)
        return json.loads(row[0])

    def save_scenario(self, value, scenario_id=None):
        leaf = self.leaf(value.get("leaf"))
        status = value.get("status", "draft")
        if status not in {"draft", "ready", "archived"}:
            raise FactoryError("invalid scenario status")
        body = {
            "id": scenario_id or uid("scn"),
            "leaf": leaf["slug"],
            "leaf_name": leaf["name_zh"] or leaf["name"],
            "name": text(value.get("name"), "name", 160),
            "audience": text(value.get("audience"), "audience", 1000),
            "objective": text(value.get("objective"), "objective"),
            "workflow": lines(value.get("workflow"), "workflow"),
            "acceptance": lines(value.get("acceptance"), "acceptance"),
            "status": status,
            "updated_at": now(),
        }
        with self.connect(True) as con:
            previous = con.execute(
                "SELECT revision,leaf FROM scenario WHERE id=?", (body["id"],)
            ).fetchone()
            if scenario_id and not previous:
                raise FactoryError("scenario not found", "not_found", 404)
            if previous and (
                value.get("expected_revision") != previous[0]
                or leaf["slug"] != previous[1]
            ):
                raise FactoryError(
                    "scenario changed; refresh before saving", "revision_conflict", 409
                )
            body["revision"] = previous[0] + 1 if previous else 1
            con.execute(
                "INSERT OR REPLACE INTO scenario VALUES (?,?,?,?,?,?)",
                (
                    body["id"],
                    leaf["slug"],
                    body["revision"],
                    status,
                    canonical(body),
                    body["updated_at"],
                ),
            )
            con.execute(
                "INSERT INTO scenario_history VALUES (?,?,?)",
                (body["id"], body["revision"], canonical(body)),
            )
        return body

    def create_batch(self, value):
        kind = value.get("kind", "production")
        if kind not in {
            "production",
            "blueprint-production",
            "scenarios",
            "scenario-review",
        }:
            raise FactoryError("invalid batch kind")
        skip_generated = value.get("skip_generated", False)
        if not isinstance(skip_generated, bool):
            raise FactoryError("skip_generated must be a boolean")
        language = value.get("language", "zh")
        if language not in ("zh", "en"):
            raise FactoryError("language must be zh or en")
        model = text(value.get("model"), "provider/model", 200)
        if (
            not re.fullmatch(r"[a-zA-Z0-9._:/#-]+", model)
            or "/" not in model
            or model.startswith("-")
        ):
            raise FactoryError("model must use provider/model format")
        if kind == "blueprint-production" and value.get("source_url"):
            raise FactoryError(
                "cognition research uses multiple sources; do not supply a single code repository"
            )
        if value.get("source_url"):
            from .sources import github_repo

            github_repo(value["source_url"])
        configs = {
            "name": text(value.get("name"), "batch name", 160),
            "model": model,
            "concurrency": integer(value.get("concurrency", 1), "concurrency", 1, 8),
            "timeout": integer(value.get("timeout", 900), "timeout", 30, 7200),
            "repair_attempts": integer(
                value.get("repair_attempts", 1), "repair_attempts", 0, 5
            ),
            "kind": kind,
            "language": language,
        }
        if kind == "blueprint-production":
            protocol = value.get("acceptance_protocol")
            if protocol not in (None, "atlas.acceptance-runner.v1"):
                raise FactoryError("unsupported cognitive acceptance protocol")
            if protocol:
                configs["acceptance_protocol"] = protocol
            guidance = value.get("cognition_guidance", "")
            if not isinstance(guidance, str):
                raise FactoryError("cognition_guidance must be text")
            configs["cognition_guidance"] = (
                text(guidance, "cognition guidance", 12_000) if guidance.strip() else ""
            )
        ids = value.get("leaves") if kind == "scenarios" else value.get("scenario_ids")
        if not isinstance(ids, list) or not ids or len(ids) > 2000:
            raise FactoryError("select between 1 and 2000 catalog entries")
        ids = list(dict.fromkeys(text(x, "catalog entry", 200) for x in ids))
        snapshots = []
        for entry in ids:
            scenario = self.scenario(entry) if kind != "scenarios" else None
            if (
                kind in {"production", "blueprint-production"}
                and scenario["status"] != "ready"
            ):
                raise FactoryError(
                    "confirm each scenario before production", "scenario_not_ready", 409
                )
            leaf = self.leaf(scenario["leaf"] if scenario else entry)
            snapshots.append(
                {
                    "leaf": leaf,
                    "scenario": scenario,
                    "source_url": str(value.get("source_url") or "").strip(),
                    "config": configs,
                }
            )
        batch_id, at = uid("bat"), now()
        with self.connect(True) as con:
            if kind == "scenarios":
                # Check under the queue write lock: another tab may have queued
                # or completed this leaf after the client loaded its catalog.
                for snap in snapshots:
                    slug = snap["leaf"]["slug"]
                    active = con.execute(
                        "SELECT 1 FROM job j JOIN batch b ON b.id=j.batch_id "
                        "WHERE j.kind='scenarios' AND j.state IN ('queued','running') "
                        "AND b.state!='cancelled' AND json_extract(j.snapshot,'$.leaf.slug')=? LIMIT 1",
                        (slug,),
                    ).fetchone()
                    if active:
                        raise FactoryError(
                            f"scenario generation is already queued or running for {slug}; refresh the catalog",
                            "scenario_generation_active",
                            409,
                        )
                    covered = con.execute(
                        "SELECT 1 FROM scenario WHERE leaf=? LIMIT 1", (slug,)
                    ).fetchone()
                    researched = con.execute(
                        "SELECT 1 FROM job WHERE kind='scenarios' AND state='completed' "
                        "AND json_extract(snapshot,'$.leaf.slug')=? LIMIT 1",
                        (slug,),
                    ).fetchone()
                    if skip_generated and (covered or researched):
                        raise FactoryError(
                            f"{slug} already has scenarios or completed research; refresh or explicitly allow additional generation",
                            "scenario_already_generated",
                            409,
                        )
            con.execute(
                "INSERT INTO batch VALUES (?,?,?,?)",
                (batch_id, "running", canonical(configs), at),
            )
            for snap in snapshots:
                if kind == "blueprint-production":
                    current = json.loads(
                        con.execute(
                            "SELECT body FROM scenario WHERE id=?",
                            (snap["scenario"]["id"],),
                        ).fetchone()[0]
                    )
                    revisions = value.get("scenario_revisions")
                    if (
                        not isinstance(revisions, dict)
                        or revisions.get(current["id"]) != current["revision"]
                    ):
                        raise FactoryError(
                            "scenario changed; refresh before cognition production",
                            "revision_conflict",
                            409,
                        )
                    if current["status"] != "ready":
                        raise FactoryError(
                            "confirm each scenario before cognition production",
                            "scenario_not_ready",
                            409,
                        )
                    if con.execute(
                        "SELECT 1 FROM job WHERE kind='blueprint-production' AND state IN ('queued','running') AND json_extract(snapshot,'$.scenario.id')=?",
                        (current["id"],),
                    ).fetchone():
                        raise FactoryError(
                            "cognition production already queued or running for this scenario",
                            "conflict",
                            409,
                        )
                    snap["scenario"] = current
                if kind == "scenarios":
                    # Freeze the active catalog under the same write lock as
                    # queueing, rather than reading mutable peers in the worker.
                    existing = self._scenario_peers(
                        con, {"leaf": snap["leaf"]["slug"], "id": ""}
                    )
                    snap["existing_scenarios"] = existing
                    snap["existing_scenarios_digest"] = digest(existing)
                if kind == "scenario-review":
                    # Re-read under the write lock so edits cannot race queueing.
                    current = json.loads(
                        con.execute(
                            "SELECT body FROM scenario WHERE id=?",
                            (snap["scenario"]["id"],),
                        ).fetchone()[0]
                    )
                    revisions = value.get("scenario_revisions")
                    if (
                        not isinstance(revisions, dict)
                        or revisions.get(current["id"]) != current["revision"]
                    ):
                        raise FactoryError(
                            "scenario changed; refresh before review",
                            "revision_conflict",
                            409,
                        )
                    if current["status"] == "archived":
                        raise FactoryError("archived scenarios cannot be reviewed")
                    self._queue_scenario_review(
                        con, batch_id, current, configs, snap["leaf"]
                    )
                    continue
                con.execute(
                    "INSERT INTO job VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        uid("job"),
                        batch_id,
                        kind,
                        "queued",
                        "discovery",
                        1,
                        None,
                        None,
                        canonical(snap),
                        None,
                        at,
                        at,
                    ),
                )
        return self.batch(batch_id)

    def batches(self):
        with self.connect() as con:
            ids = [
                r[0]
                for r in con.execute(
                    "SELECT id FROM batch ORDER BY created_at DESC LIMIT 100"
                )
            ]
        return [self.batch(x) for x in ids]

    def batch(self, batch_id):
        with self.connect() as con:
            row = con.execute("SELECT * FROM batch WHERE id=?", (batch_id,)).fetchone()
            jobs = [
                self._job(r)
                for r in con.execute(
                    "SELECT * FROM job WHERE batch_id=? ORDER BY created_at,id",
                    (batch_id,),
                )
            ]
            results = {
                r[0]: json.loads(r[1])["result"]
                for r in con.execute(
                    "SELECT c.job_id,c.body FROM checkpoint c JOIN job j ON c.job_id=j.id "
                    "WHERE j.batch_id=? AND c.name='scenario_proposals'",
                    (batch_id,),
                )
            }
        if not row:
            raise FactoryError("batch not found", "not_found", 404)
        state = row["state"]
        if state == "running" and all(
            j["state"] not in {"queued", "running"} for j in jobs
        ):
            state = (
                "completed"
                if all(j["state"] == "completed" for j in jobs)
                else "needs_attention"
            )
        for item in jobs:
            item["snapshot"]["leaf"].pop("content", None)
            if item["id"] in results:
                item["generation_result"] = results[item["id"]]
        return {
            "id": row["id"],
            "state": state,
            "config": json.loads(row["config"]),
            "created_at": row["created_at"],
            "jobs": jobs,
        }

    @staticmethod
    def _job(row):
        result = dict(row)
        result["snapshot"] = json.loads(result["snapshot"])
        result.pop("token", None)
        result.pop("lease", None)
        return result

    def job(self, job_id):
        with self.connect() as con:
            row = con.execute("SELECT * FROM job WHERE id=?", (job_id,)).fetchone()
            events = [
                dict(x)
                for x in con.execute(
                    "SELECT seq,attempt,at,stage,message FROM event WHERE job_id=? ORDER BY seq DESC LIMIT 100",
                    (job_id,),
                )
            ]
            result = con.execute(
                "SELECT body FROM checkpoint WHERE job_id=? AND name='scenario_proposals'",
                (job_id,),
            ).fetchone()
            design_reviews = [
                {"stage": record["name"], **json.loads(record["body"])["result"]}
                for record in con.execute(
                    "SELECT name,body FROM checkpoint WHERE job_id=? AND name LIKE 'blueprint-spec-review-%' ORDER BY name",
                    (job_id,),
                )
            ]
        if not row:
            raise FactoryError("job not found", "not_found", 404)
        return {
            **self._job(row),
            "events": events,
            "design_reviews": design_reviews,
            **(
                {"generation_result": json.loads(result[0])["result"]} if result else {}
            ),
        }

    def batch_action(self, batch_id, action):
        self.batch(batch_id)
        if action not in {"pause", "resume", "cancel"}:
            raise FactoryError("invalid batch action")
        with self.connect(True) as con:
            row = con.execute(
                "SELECT state FROM batch WHERE id=?", (batch_id,)
            ).fetchone()
            if row[0] == "cancelled" and action != "cancel":
                raise FactoryError("cancelled batch cannot resume", "conflict", 409)
            con.execute(
                "UPDATE batch SET state=? WHERE id=?",
                (
                    {"pause": "paused", "resume": "running", "cancel": "cancelled"}[
                        action
                    ],
                    batch_id,
                ),
            )
            if action == "cancel":
                con.execute(
                    "UPDATE job SET state='cancelled',token=NULL,lease=NULL,updated_at=? WHERE batch_id=? AND state IN ('queued','running')",
                    (now(), batch_id),
                )
        return self.batch(batch_id)

    def claim(self, worker, lane=None):
        with self.connect(True) as con:
            # These limits hold across batches and schedulers, not merely in UI
            # or a local ThreadPool. The BEGIN IMMEDIATE lock fences races.
            running = con.execute("SELECT kind, snapshot FROM job WHERE state='running' AND lease>?", (time.time(),)).fetchall()
            production = sum(r["kind"] not in {"harness-review", "runtime-verification", "scenario-review", "cognitive-review", "blueprint-runtime"} for r in running)
            runtime = sum(r["kind"] in {"runtime-verification", "blueprint-runtime"} for r in running)
            if lane == "production" and production >= 2:
                return None
            if lane == "verification" and runtime >= 1:
                # Continue read-only reviews, but do not claim a second runtime.
                runtime_full = 1
            else:
                runtime_full = 0
            row = con.execute(
                """SELECT j.* FROM job j JOIN batch b ON b.id=j.batch_id
              WHERE j.state='queued' AND b.state='running'
              AND NOT EXISTS (
                SELECT 1 FROM v1_execution pe JOIN batch pb ON pb.id=pe.batch_id
                WHERE pe.plan_id=json_extract(j.snapshot,'$.v1.plan_id')
                  AND pb.state IN ('paused','cancelled'))
              AND ((j.kind IN ('runtime-verification','blueprint-runtime') AND
                (SELECT count(*) FROM job g WHERE g.state='running' AND g.lease>strftime('%s','now')
                 AND g.kind IN ('runtime-verification','blueprint-runtime')) < 1) OR
                (j.kind NOT IN ('runtime-verification','blueprint-runtime') AND
                 (SELECT count(*) FROM job g WHERE g.state='running' AND g.lease>strftime('%s','now')
                  AND g.kind NOT IN ('runtime-verification','blueprint-runtime')) < 2))
              AND (?=0 OR j.kind NOT IN ('runtime-verification','blueprint-runtime'))
              AND (? IS NULL OR (?='verification' AND j.kind IN ('harness-review','runtime-verification','scenario-review','cognitive-review','blueprint-runtime'))
                OR (?='production' AND j.kind IN ('production','scenarios','blueprint-production','case-research','application-development')))
              AND (SELECT count(*) FROM job a WHERE a.batch_id=b.id AND a.state='running'
                AND (? IS NULL OR (?='verification' AND a.kind IN ('harness-review','runtime-verification','scenario-review','cognitive-review','blueprint-runtime'))
                  OR (?='production' AND a.kind IN ('production','scenarios','blueprint-production','case-research','application-development'))))
                < json_extract(b.config,'$.concurrency') ORDER BY j.created_at,j.id LIMIT 1""",
                (runtime_full, lane, lane, lane, lane, lane, lane),
            ).fetchone()
            if not row:
                return None
            token = worker + ":" + uuid.uuid4().hex
            con.execute(
                "UPDATE job SET state='running',token=?,lease=?,updated_at=? WHERE id=?",
                (token, time.time() + 60, now(), row["id"]),
            )
            result = self._job(row)
            return {**result, "state": "running", "token": token}

    def owned(self, job_id, token):
        with self.connect() as con:
            return (
                con.execute(
                    "SELECT 1 FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                    (job_id, token, time.time()),
                ).fetchone()
                is not None
            )

    def heartbeat(self, job_id, token):
        with self.connect(True) as con:
            return (
                con.execute(
                    "UPDATE job SET lease=? WHERE id=? AND token=? AND state='running' AND lease>?",
                    (time.time() + 60, job_id, token, time.time()),
                ).rowcount
                == 1
            )

    def update(self, job_id, token, stage, message, state="running", error=None):
        from privacy import redact_text

        with self.connect(True) as con:
            row = con.execute(
                "SELECT attempt FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                (job_id, token, time.time()),
            ).fetchone()
            if not row:
                raise FactoryError(
                    "job no longer belongs to this worker", "lease_lost", 409
                )
            con.execute(
                "UPDATE job SET stage=?,state=?,error=?,updated_at=? WHERE id=?",
                (
                    stage,
                    state,
                    redact_text(str(error))[:3000] if error else None,
                    now(),
                    job_id,
                ),
            )
            con.execute(
                "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                (job_id, row[0], now(), stage, redact_text(message)[:3000]),
            )

    def recover(self):
        # Called only by the process holding worker.lock. Old attempts can never
        # publish after this token revocation. Explicit retry preserves evidence.
        with self.connect(True) as con:
            count = con.execute(
                "UPDATE job SET state='interrupted',token=NULL,lease=NULL,error='Worker interrupted; review and retry to resume checkpoints',updated_at=? WHERE state='running'",
                (now(),),
            ).rowcount
        return count

    def checkpoint(self, job_id, name, value=None, token=None):
        with self.connect(write=value is not None) as con:
            if value is not None:
                if not con.execute(
                    "SELECT 1 FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                    (job_id, token, time.time()),
                ).fetchone():
                    raise FactoryError("checkpoint ownership lost", "lease_lost", 409)
                con.execute(
                    "INSERT OR IGNORE INTO checkpoint VALUES(?,?,?)",
                    (job_id, name, canonical(value)),
                )
            row = con.execute(
                "SELECT body FROM checkpoint WHERE job_id=? AND name=?", (job_id, name)
            ).fetchone()
            return json.loads(row[0]) if row else None

    def expire_leases(self):
        with self.connect(True) as con:
            return con.execute(
                "UPDATE job SET state='interrupted',token=NULL,lease=NULL,error='Worker lease expired; review and retry',updated_at=? WHERE state='running' AND lease<?",
                (now(), time.time()),
            ).rowcount

    def retry(self, job_id):
        with self.connect(True) as con:
            row = con.execute(
                "SELECT state,batch_id FROM job WHERE id=?", (job_id,)
            ).fetchone()
            if not row:
                raise FactoryError("job not found", "not_found", 404)
            supersession_table = con.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND name='tf_job_supersession'"
            ).fetchone()
            if supersession_table and con.execute(
                "SELECT 1 FROM tf_job_supersession WHERE old_job_id=?", (job_id,)
            ).fetchone():
                raise FactoryError(
                    "superseded jobs cannot be retried; use the recorded successor",
                    "job_superseded", 409,
                )
            if row[0] not in {"failed", "interrupted", "cancelled", "needs_review"}:
                raise FactoryError(
                    "only failed or interrupted jobs can retry", "conflict", 409
                )
            batch = con.execute(
                "SELECT state FROM batch WHERE id=?", (row[1],)
            ).fetchone()
            if batch[0] == "cancelled":
                raise FactoryError(
                    "create a new batch after cancellation", "conflict", 409
                )
            con.execute(
                "UPDATE job SET state='queued',attempt=attempt+1,token=NULL,lease=NULL,error=NULL,updated_at=? WHERE id=?",
                (now(), job_id),
            )
        return self.job(job_id)

    def artifacts(self):
        from .v1_catalog import review_status, catalog_eligibility
        with self.connect() as con:
            values = [
                {
                    **json.loads(r["body"]),
                    "id": r["id"],
                    "level": r["level"],
                    "state": r["state"],
                    "digest": r["digest"],
                    "publication_status": r["state"],
                    "review_status": review_status(con, r["id"], r["digest"]) if json.loads(r["body"]).get("artifact_type") == "product-blueprint" else None,
                    "evidence_status": "fixed_case_basis" if json.loads(r["body"]).get("provenance", {}).get("case_basis") else "legacy_unverified",
                    "acceptances": self.acceptances(r["id"]),
                    "acceptance_jobs": self.acceptance_jobs(r["id"]),
                }
                for r in con.execute("SELECT * FROM artifact ORDER BY created_at DESC")
            ]
        return [{**value, **catalog_eligibility(self, value)} for value in values]

    def add_artifact(self, job_id, token, body):
        artifact_id = uid("tpl")
        with self.connect(True) as con:
            owned = con.execute(
                "SELECT 1 FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                (job_id, token, time.time()),
            ).fetchone()
            if not owned:
                raise FactoryError(
                    "job ownership lost before artifact registration", "lease_lost", 409
                )
            con.execute(
                "INSERT INTO artifact VALUES (?,?,?,?,?,?,?)",
                (
                    artifact_id,
                    job_id,
                    body["digest"],
                    "L0",
                    "draft",
                    canonical({**body, "job_id": job_id}),
                    now(),
                ),
            )
            if body.get("artifact_type") == "product-blueprint" and body.get("provenance", {}).get("v1"):
                snapshot = json.loads(con.execute("SELECT snapshot FROM job WHERE id=?", (job_id,)).fetchone()[0])
                con.execute("INSERT INTO v1_outbox VALUES(?,?,?,?,?)", (
                    uid("out"), job_id, artifact_id,
                    canonical({"method": "cognitive-review", "expected_digest": body["digest"],
                               "model": snapshot["config"]["model"], "timeout": snapshot["config"]["timeout"],
                               "language": snapshot["config"].get("language", "zh")}), "pending",
                ))
            con.execute(
                "UPDATE job SET state='completed',stage='completed',updated_at=? WHERE id=? AND token=?",
                (now(), job_id, token),
            )
            attempt = con.execute(
                "SELECT attempt FROM job WHERE id=?", (job_id,)
            ).fetchone()[0]
            con.execute(
                "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                (
                    job_id,
                    attempt,
                    now(),
                    "completed",
                    "Frozen L0 candidate ready for independent acceptance",
                ),
            )
        return artifact_id

    def reconcile_outbox(self):
        """Replay atomically recorded successor intents after any crash boundary."""
        with self.connect() as con:
            pending = [dict(r) for r in con.execute("SELECT * FROM v1_outbox WHERE state='pending'")]
        for intent in pending:
            self.create_acceptance(intent["artifact_id"], json.loads(intent["body"]), automatic=True)
            with self.connect(True) as con:
                con.execute("UPDATE v1_outbox SET state='done' WHERE id=?", (intent["id"],))

    def artifact_action(self, artifact_id, value):
        action = value.get("action")
        if action not in {"publish", "withdraw"}:
            raise FactoryError("invalid artifact action")
        review = text(value.get("review"), "review", 3000)
        with self.connect(True) as con:
            row = con.execute(
                "SELECT * FROM artifact WHERE id=?", (artifact_id,)
            ).fetchone()
            if not row:
                raise FactoryError("artifact not found", "not_found", 404)
            body = json.loads(row["body"])
            if body.get("artifact_type") == "product-blueprint":
                from .v1_catalog import publish
                publish(self, con, row, body, value, review)
                # Read after the transaction commits so response shows new state.
                cognitive = True
            else:
                cognitive = False
            if cognitive:
                pass
            elif value.get("expected_digest") != row["digest"]:
                raise FactoryError("artifact version changed", "revision_conflict", 409)
            if cognitive:
                return {**body, "id": artifact_id, "digest": row["digest"], "level": row["level"], "state": "published" if action == "publish" else "withdrawn", "publication_status": "published" if action == "publish" else "withdrawn"}
            level = value.get("level", row["level"])
            if level not in {"L0", "L1", "L2"}:
                raise FactoryError(
                    "L3 requires real downstream usage evidence; not automatically assigned"
                )
            if action == "publish":
                records = con.execute(
                    "SELECT body FROM acceptance WHERE artifact_id=? AND digest=?",
                    (artifact_id, row["digest"]),
                ).fetchall()
                if level == "L0" or not any(
                    json.loads(r[0]).get("outcome") == "passed" for r in records
                ):
                    raise FactoryError(
                        "Harness review or runtime acceptance must pass before publication",
                        "acceptance_required",
                        409,
                    )
            body["review"] = {"note": review, "at": now(), "action": action}
            con.execute(
                "UPDATE artifact SET state=?,level=?,body=? WHERE id=?",
                (
                    "published" if action == "publish" else "withdrawn",
                    level,
                    canonical(body),
                    artifact_id,
                ),
            )
        return next(a for a in self.artifacts() if a["id"] == artifact_id)

    def acceptance_jobs(self, artifact_id):
        with self.connect() as con:
            return [
                dict(r)
                for r in con.execute(
                    "SELECT id,kind,state,stage,updated_at FROM job WHERE kind IN ('harness-review','runtime-verification','cognitive-review','blueprint-runtime') AND json_extract(snapshot,'$.artifact_id')=? ORDER BY created_at DESC LIMIT 20",
                    (artifact_id,),
                )
            ]

    def acceptances(self, artifact_id):
        with self.connect() as con:
            return [
                json.loads(r[0])
                for r in con.execute(
                    "SELECT body FROM acceptance WHERE artifact_id=? ORDER BY created_at DESC",
                    (artifact_id,),
                )
            ]

    def create_acceptance(self, artifact_id, value, automatic=False):
        artifact = next((a for a in self.artifacts() if a["id"] == artifact_id), None)
        if not artifact:
            raise FactoryError("template not found", "not_found", 404)
        if value.get("method") == "blueprint-runtime":
            from .runtime_jobs import queue_runtime

            return queue_runtime(self, artifact, value)
        cognitive = artifact.get("artifact_type") == "product-blueprint"
        if cognitive and value.get("method") != "cognitive-review":
            raise FactoryError(
                "choose cognitive-review for this package",
                "blueprint_operation_unavailable",
                409,
            )
        if value.get("expected_digest") != artifact["digest"]:
            raise FactoryError("artifact version changed", "revision_conflict", 409)
        method = value.get("method")
        if method not in (
            {"cognitive-review"}
            if cognitive
            else {"harness-review", "runtime-verification"}
        ):
            raise FactoryError("choose an acceptance method for this artifact type")
        model = text(
            value.get("model", artifact["provenance"].get("model")),
            "provider/model",
            200,
        )
        if (
            not re.fullmatch(r"[a-zA-Z0-9._:/#-]+", model)
            or "/" not in model
            or model.startswith("-")
        ):
            raise FactoryError("model must use provider/model format")
        config = {
            "kind": method,
            "name": "Independent acceptance: " + artifact["manifest"]["name"],
            "model": model,
            "concurrency": 1,
            "language": value.get("language", "zh"),
            "timeout": integer(value.get("timeout", 900), "timeout", 30, 7200),
        }
        if config["language"] not in ("zh", "en"):
            raise FactoryError("language must be zh or en")
        snapshot = {
            "artifact_id": artifact_id,
            "artifact_digest": artifact["digest"],
            "bundle_path": artifact["bundle_path"],
            "leaf": self.job(artifact["job_id"])["snapshot"]["leaf"]
            if cognitive
            else self.leaf(artifact["leaf"]),
            "scenario": artifact["provenance"]["scenario"],
            "config": config,
        }
        original_snapshot = self.job(artifact["job_id"])["snapshot"]
        if original_snapshot.get("v1"):
            snapshot["v1"] = original_snapshot["v1"]
            snapshot["case_basis"] = original_snapshot.get("case_basis")
        batch_id, job_id, at = uid("bat"), uid("job"), now()
        with self.connect(True) as con:
            if automatic:
                existing = con.execute(
                    "SELECT batch_id FROM job WHERE kind=? AND json_extract(snapshot,'$.artifact_id')=? "
                    "AND json_extract(snapshot,'$.artifact_digest')=? ORDER BY created_at LIMIT 1",
                    (method, artifact_id, artifact["digest"]),
                ).fetchone()
                if existing:
                    return self.batch(existing[0])
                parent = con.execute(
                    "SELECT b.state FROM batch b JOIN job j ON j.batch_id=b.id WHERE j.id=?",
                    (artifact["job_id"],),
                ).fetchone()
                if not parent or parent[0] == "cancelled":
                    return None
                if snapshot.get("v1"):
                    batch_id = con.execute("SELECT batch_id FROM job WHERE id=?", (artifact["job_id"],)).fetchone()[0]
            active = con.execute(
                "SELECT 1 FROM job WHERE kind=? AND state IN ('queued','running') AND json_extract(snapshot,'$.artifact_id')=?",
                (method, artifact_id),
            ).fetchone()
            if active:
                raise FactoryError(
                    "this acceptance is already queued or running", "conflict", 409
                )
            con.execute(
                "INSERT OR IGNORE INTO batch VALUES(?,?,?,?)",
                (batch_id, "running", canonical(config), at),
            )
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    job_id,
                    batch_id,
                    method,
                    "queued",
                    "acceptance",
                    1,
                    None,
                    None,
                    canonical(snapshot),
                    None,
                    at,
                    at,
                ),
            )
        return self.batch(batch_id)

    def complete_acceptance(self, job_id, token, result):
        from privacy import redact_value

        with self.connect(True) as con:
            row = con.execute(
                "SELECT * FROM job WHERE id=? AND token=? AND state='running' AND lease>?",
                (job_id, token, time.time()),
            ).fetchone()
            if not row:
                raise FactoryError("acceptance ownership lost", "lease_lost", 409)
            snapshot = json.loads(row["snapshot"])
            outcome = result.get("outcome")
            if outcome not in {"passed", "blocked", "uncertain", "unavailable"}:
                raise FactoryError("invalid acceptance outcome")
            body = redact_value(
                {
                    **result,
                    "id": uid("acc"),
                    "method": row["kind"],
                    "artifact_id": snapshot["artifact_id"],
                    "digest": snapshot["artifact_digest"],
                    "job_id": job_id,
                    "created_at": now(),
                }
            )
            con.execute(
                "INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)",
                (
                    body["id"],
                    body["artifact_id"],
                    body["digest"],
                    body["method"],
                    job_id,
                    canonical(body),
                    body["created_at"],
                ),
            )
            if outcome == "passed" and row["kind"] in {"harness-review", "runtime-verification"}:
                con.execute(
                    "UPDATE artifact SET level='L1' WHERE id=? AND digest=? AND level='L0'",
                    (body["artifact_id"], body["digest"]),
                )
            con.execute(
                "UPDATE job SET state=?,stage='acceptance',error=?,updated_at=? WHERE id=?",
                (
                    "completed" if outcome == "passed" else "needs_review",
                    body.get("error"),
                    now(),
                    job_id,
                ),
            )
            con.execute(
                "INSERT INTO event(job_id,attempt,at,stage,message) VALUES(?,?,?,?,?)",
                (
                    job_id,
                    row["attempt"],
                    now(),
                    "acceptance",
                    row["kind"] + ": " + outcome,
                ),
            )

    def create_repair(self, artifact_id, value):
        artifact = next((a for a in self.artifacts() if a["id"] == artifact_id), None)
        if not artifact:
            raise FactoryError("template not found", "not_found", 404)
        if artifact.get("artifact_type") == "product-blueprint":
            from .cognition import queue_repair

            return queue_repair(self, artifact, value)
        if value.get("expected_digest") != artifact["digest"]:
            raise FactoryError("artifact version changed", "revision_conflict", 409)
        original = self.job(artifact["job_id"])["snapshot"]
        note = text(value.get("note"), "repair instructions", 4000)
        replan = value.get("replan", False)
        if type(replan) is not bool:
            raise FactoryError("replan must be a boolean")
        # Create a new job from the immutable scenario snapshot, even if the live catalog changed.
        config = {
            **original["config"],
            "name": "Repair: " + artifact["manifest"]["name"],
        }
        batch_id, job_id, at = uid("bat"), uid("job"), now()
        snapshot = {
            **original,
            "config": config,
            "repair_artifact": {
                "id": artifact_id,
                "digest": artifact["digest"],
                "bundle_path": artifact["bundle_path"],
                "note": note,
                "replan": replan,
                "plan": artifact["plan"],
                "manifest": artifact["manifest"],
                "acceptances": artifact["acceptances"],
            },
        }
        with self.connect(True) as con:
            con.execute(
                "INSERT INTO batch VALUES(?,?,?,?)",
                (batch_id, "running", canonical(config), at),
            )
            con.execute(
                "INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    job_id,
                    batch_id,
                    "production",
                    "queued",
                    "repair",
                    1,
                    None,
                    None,
                    canonical(snapshot),
                    None,
                    at,
                    at,
                ),
            )
        return self.batch(batch_id)
