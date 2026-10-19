"""Versioned schema migrations for the shared case library."""

from __future__ import annotations

import json
import re

from .store import canonical, now


def migrate(store):
    """Apply case-library migrations atomically and import the legacy catalog.

    The base factory schema is owned by FactoryStore. Each migration and its
    version marker commit together, so a failed legacy import can be retried.
    """
    with store.connect() as con:
        exists = con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='schema_migration'").fetchone()
        if exists and con.execute("SELECT COALESCE(MAX(version), 0) FROM schema_migration").fetchone()[0] >= 2:
            return
    with store.connect(True) as con:
        con.execute("CREATE TABLE IF NOT EXISTS schema_migration (version INTEGER PRIMARY KEY, applied_at TEXT NOT NULL)")
        current = con.execute("SELECT COALESCE(MAX(version), 0) FROM schema_migration").fetchone()[0]
        if current < 1:
            for statement in _V1_SCHEMA:
                con.execute(statement)
            catalog_path = store.pack / "mvp_apps.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            if not isinstance(catalog, list) or len(catalog) != 33:
                raise ValueError("legacy application catalog must contain exactly 33 records")
            at = now()
            for item in catalog:
                if not isinstance(item, dict) or not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,199}", item.get("slug", "")):
                    raise ValueError("legacy application record has an invalid slug")
                slug = item["slug"]
                app = {
                    "app_id": "app:" + slug,
                    "legacy_slug": slug,
                    "name": item.get("name", slug),
                    "aliases": item.get("aliases", []),
                    "vendor": item.get("vendor"),
                    "tagline": item.get("tagline"),
                    "tasks": item.get("tasks", []),
                    "catalog_status": "catalog_only",
                    "source_identity": {"kind": "legacy_catalog", "slug": slug},
                    "created_at": at,
                }
                con.execute(
                    "INSERT INTO case_app(app_id, legacy_slug, body, created_at) VALUES(?,?,?,?)",
                    (app["app_id"], slug, canonical(app), at),
                )
            con.execute("INSERT INTO schema_migration(version, applied_at) VALUES(1,?)", (at,))
        if current < 2:
            # Directory classification is metadata, never new research evidence.
            # Keep the original legacy-reference fingerprint input untouched.
            classified_path = store.pack / "mvp_apps_classified.json"
            if classified_path.exists():
                classified = json.loads(classified_path.read_text(encoding="utf-8"))
                if not isinstance(classified, list):
                    raise ValueError("legacy classifications must be a list")
                for item in classified:
                    row = con.execute("SELECT app_id,body FROM case_app WHERE legacy_slug=?", (item["slug"],)).fetchone()
                    if row:
                        body = json.loads(row[1])
                        body["catalog_classification"] = item
                        con.execute("UPDATE case_app SET body=? WHERE app_id=?", (canonical(body), row[0]))
            con.execute("INSERT INTO schema_migration(version, applied_at) VALUES(2,?)", (now(),))


_V1_SCHEMA = (
    "CREATE TABLE case_app (app_id TEXT PRIMARY KEY, legacy_slug TEXT NOT NULL UNIQUE, body TEXT NOT NULL, created_at TEXT NOT NULL)",
    "CREATE TABLE source_snapshot (snapshot_id TEXT PRIMARY KEY, repository TEXT NOT NULL, repo_id TEXT, commit_sha TEXT NOT NULL CHECK(length(commit_sha)=40), strategy_version TEXT NOT NULL, digest TEXT NOT NULL, body TEXT NOT NULL, created_at TEXT NOT NULL, UNIQUE(repository, commit_sha, strategy_version))",
    "CREATE TABLE case_revision (case_id TEXT NOT NULL, revision INTEGER NOT NULL CHECK(revision>0), app_id TEXT NOT NULL REFERENCES case_app(app_id), digest TEXT NOT NULL, body TEXT NOT NULL, created_at TEXT NOT NULL, PRIMARY KEY(case_id, revision))",
    "CREATE TABLE evidence_observation (evidence_id TEXT NOT NULL, case_id TEXT NOT NULL, revision INTEGER NOT NULL, kind TEXT NOT NULL CHECK(kind IN ('documentation','code_observation','inference','runtime_verification')), digest TEXT NOT NULL, body TEXT NOT NULL, PRIMARY KEY(evidence_id, case_id, revision), FOREIGN KEY(case_id, revision) REFERENCES case_revision(case_id,revision))",
    "CREATE TABLE scenario_case_link (scenario_id TEXT NOT NULL, scenario_revision INTEGER NOT NULL, case_id TEXT NOT NULL, case_revision INTEGER NOT NULL, body TEXT NOT NULL, PRIMARY KEY(scenario_id, scenario_revision, case_id, case_revision), FOREIGN KEY(case_id, case_revision) REFERENCES case_revision(case_id,revision))",
    "CREATE TABLE case_idempotency (idempotency_key TEXT PRIMARY KEY, request_digest TEXT NOT NULL, case_id TEXT NOT NULL, revision INTEGER NOT NULL, FOREIGN KEY(case_id, revision) REFERENCES case_revision(case_id,revision))",
    "CREATE TABLE evidence_review (review_id TEXT PRIMARY KEY, evidence_id TEXT NOT NULL, case_id TEXT NOT NULL, revision INTEGER NOT NULL, evidence_digest TEXT NOT NULL, outcome TEXT NOT NULL CHECK(outcome IN ('accepted','rejected','uncertain')), reviewer TEXT NOT NULL, reviewer_kind TEXT NOT NULL CHECK(reviewer_kind IN ('human','independent_agent')), created_at TEXT NOT NULL, FOREIGN KEY(evidence_id,case_id,revision) REFERENCES evidence_observation(evidence_id,case_id,revision))",
    "CREATE INDEX case_revision_app ON case_revision(app_id, case_id, revision)",
    "CREATE INDEX scenario_case_case ON scenario_case_link(case_id, case_revision)",
)
