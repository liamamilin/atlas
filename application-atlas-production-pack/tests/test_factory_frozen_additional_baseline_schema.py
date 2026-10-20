"""Schema-level guard for the exact failed predecessor reservation fields."""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from template_factory.evidence_grants import EvidenceGrantService
from template_factory.evidence_recovery import EvidenceRecoveryService
from template_factory.frozen_review_additional import (
    PREDECESSOR_ACCEPTANCE,
    PREDECESSOR_ACCEPTED_AT,
    PREDECESSOR_GRANT,
    PREDECESSOR_RESERVATION,
)


class AdditionalBaselineSchemaTests(unittest.TestCase):
    def test_uses_real_finished_column_and_acceptance_binding(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE tf_budget_reservation (
                id TEXT PRIMARY KEY,campaign_id TEXT,status TEXT,product_id TEXT,
                job_id TEXT,stage TEXT,finished REAL,outcome TEXT);
            CREATE TABLE tf_budget_repair (campaign_id TEXT,product_id TEXT);
            CREATE TABLE tf_evidence_recovery_grant (
                id TEXT PRIMARY KEY,status TEXT,consumed_reservation_id TEXT,call_attempt INTEGER);
            CREATE TABLE acceptance (id TEXT PRIMARY KEY,job_id TEXT,body TEXT,created_at TEXT);
            CREATE TABLE batch (id TEXT PRIMARY KEY,state TEXT);
        """)
        campaign = "atlas-v1-first-production-2026-10-19"
        product = "product-c42848f63251507bd9d911a5"
        job = "job_b01427592b164863aab5bedf7b3863bb"
        con.execute("INSERT INTO tf_budget_reservation VALUES(?,?,?,?,?,?,?,?)",
                    (PREDECESSOR_RESERVATION, campaign, "failed", product, job,
                     "cognitive-review:572da86649b4face", 1792490680.240822, "cli_failed"))
        for n in range(80):
            con.execute("INSERT INTO tf_budget_reservation VALUES(?,?,?,?,?,?,?,?)",
                        (f"call-{n}", campaign, "completed", product, job, "historical", 1.0, "ok"))
        for _ in range(7):
            con.execute("INSERT INTO tf_budget_repair VALUES(?,?)", (campaign, product))
        con.execute("INSERT INTO tf_evidence_recovery_grant VALUES(?,?,?,?)",
                    (PREDECESSOR_GRANT, "consumed", PREDECESSOR_RESERVATION, 2))
        con.execute("INSERT INTO acceptance VALUES(?,?,?,?)",
                    (PREDECESSOR_ACCEPTANCE, job, json.dumps({"job_attempt": 2,
                     "outcome": "unavailable", "code": "cli_failed",
                     "error": "provider.quota Go usage limit exceeded"}), PREDECESSOR_ACCEPTED_AT))
        con.executemany("INSERT INTO batch VALUES(?, 'paused')", (
            ("bat_6b4fc8bf5b4e42d79bc6a9069277e9f0",),
            ("bat_d13dc5920a574140be85da0ea6f5395b",),
        ))
        self.assertIn("finished", {row[1] for row in con.execute("PRAGMA table_info(tf_budget_reservation)")})
        self.assertNotIn("finished_at", {row[1] for row in con.execute("PRAGMA table_info(tf_budget_reservation)")})
        fake_store = SimpleNamespace(pack=SimpleNamespace(parent=Path(__file__).resolve().parents[2]))
        EvidenceGrantService._verify_frozen_additional_baseline_locked(con, fake_store)

    def test_legacy_grant_migration_preserves_created_at_column_order(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.execute("""CREATE TABLE tf_evidence_recovery_grant (
            id TEXT PRIMARY KEY,campaign_id TEXT NOT NULL,product_id TEXT NOT NULL,
            plan_id TEXT NOT NULL,job_id TEXT NOT NULL,request_key TEXT NOT NULL,
            proposal_digest TEXT NOT NULL,request_json TEXT NOT NULL,status TEXT NOT NULL,
            queued_job_id TEXT,consumed_reservation_id TEXT,created_at REAL NOT NULL,
            UNIQUE(campaign_id,request_key),UNIQUE(campaign_id,job_id))""")
        values = ("legacy-grant", "campaign", "product", "plan", "job", "key", "digest", "{}",
                  "consumed", None, "legacy-reservation", 1792490680.5)
        con.execute("INSERT INTO tf_evidence_recovery_grant VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", values)
        con.execute("CREATE INDEX legacy_grant_status_idx ON tf_evidence_recovery_grant(status)")
        EvidenceGrantService.initialize_locked(con)
        row = con.execute("SELECT created_at,call_attempt FROM tf_evidence_recovery_grant WHERE id='legacy-grant'").fetchone()
        self.assertEqual(tuple(row), (1792490680.5, None))
        self.assertEqual(con.execute("SELECT COUNT(*) FROM tf_evidence_recovery_grant").fetchone()[0], 1)
        self.assertEqual(con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='index' AND name='legacy_grant_status_idx'").fetchone()[0], 1)
        self.assertEqual(con.execute("SELECT migration_digest FROM tf_frozen_review_schema_migration WHERE version=1").fetchone()[0],
                         "grant-job-unique-to-sequential-v1")

    def test_legacy_recovery_migration_preserves_receipt_and_custom_index(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.execute("""CREATE TABLE tf_evidence_recovery (
            recovery_id TEXT PRIMARY KEY,job_id TEXT NOT NULL UNIQUE,grant_id TEXT NOT NULL UNIQUE,
            request_key TEXT NOT NULL UNIQUE,request_digest TEXT NOT NULL,proposal_digest TEXT NOT NULL,
            old_state TEXT NOT NULL,old_error TEXT,old_stage TEXT NOT NULL,old_attempt INTEGER NOT NULL,
            snapshot_digest TEXT NOT NULL,checkpoint_digest TEXT NOT NULL,checkpoint_names TEXT NOT NULL,
            old_events_json TEXT NOT NULL,created_at TEXT NOT NULL)""")
        values = ("legacy-recovery", "job", "grant", "request-key", "request-digest", "proposal-digest",
                  "needs_review", "quota", "cognitive-review", 2, "snapshot", "checkpoints", "[]", "[]", "created")
        con.execute("INSERT INTO tf_evidence_recovery VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)
        con.execute("CREATE INDEX legacy_recovery_state_idx ON tf_evidence_recovery(old_state)")
        EvidenceRecoveryService._initialize_locked(con)
        row = con.execute("SELECT recovery_id,job_id,old_attempt,old_error,created_at FROM tf_evidence_recovery").fetchone()
        self.assertEqual(tuple(row), ("legacy-recovery", "job", 2, "quota", "created"))
        self.assertEqual(con.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='index' AND name='legacy_recovery_state_idx'").fetchone()[0], 1)
        self.assertEqual(con.execute("SELECT migration_digest FROM tf_frozen_review_schema_migration WHERE version=2").fetchone()[0],
                         "recovery-job-unique-to-sequential-v1")


if __name__ == "__main__":
    unittest.main()
