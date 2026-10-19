"""Read-only, source-bound V1 batch report enrichment."""
import copy
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.store import FactoryStore, canonical, now
from template_factory.v1_batches import BatchService
from template_factory.v1_reporting import enrich_report

PACK = Path(__file__).resolve().parents[1]


class FactoryReportEnrichmentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        shutil.copy(PACK / "mvp_apps.json", self.pack / "mvp_apps.json")
        (self.pack / "atlas").mkdir()
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
            con.execute("INSERT INTO leaf VALUES('bookmark-manager','Bookmarks','书签','Save links','Links')")
        self.store = FactoryStore(self.root / "state", self.pack)
        scene = self.store.save_scenario({
            "leaf": "bookmark-manager", "name": "Save and reopen", "audience": "Personal",
            "objective": "Save links and reopen", "workflow": ["save", "read"],
            "acceptance": ["Saved links remain"], "status": "ready",
        })
        self.service = BatchService(self.store)
        plan = self.service.preview({"scenario_ids": [scene["id"]], "model": "fixture/model"})
        self.plan = plan
        self.service.run(plan["id"], {
            "expected_plan_digest": plan["digest"], "idempotency_key": "run:" + plan["id"],
        })
        self.report = self.service.report(plan["id"])

    def tearDown(self):
        self.temp.cleanup()

    def _add_research_case(self, task_id):
        seed = self.plan["seeds"][0]
        scenario = seed["scenario"]
        app_id, case_id = "app:repo:fixture", "case_fixture"
        at = now()
        snapshot_body = {"files": {"README.md": "x"}, "file_manifest_digest": "manifest"}
        snapshot_id = "src_fixture"
        case_body = {
            "case_id": case_id, "revision": 1, "app_id": app_id,
            "snapshot_ids": [snapshot_id], "research": {"task_id": task_id},
            "created_task_id": task_id, "created_at": at,
        }
        link = {"scenario_id": scenario["id"], "scenario_revision": scenario["revision"],
                "case_id": case_id, "case_revision": 1, "evidence_ids": ["ev_doc"]}
        observation = {"evidence_id": "ev_doc", "kind": "documentation", "statement": "secret raw text"}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO case_app VALUES(?,?,?,?)", (app_id, "fixture-app", canonical({}), at))
            con.execute("INSERT INTO source_snapshot VALUES(?,?,?,?,?,?,?,?)", (
                snapshot_id, "https://example.invalid/repo", None, "a" * 40, "snapshot-v1", "snapshot-digest",
                canonical(snapshot_body), at,
            ))
            con.execute("INSERT INTO case_revision VALUES(?,?,?,?,?,?)", (
                case_id, 1, app_id, "case-digest", canonical(case_body), at,
            ))
            con.execute("INSERT INTO evidence_observation VALUES(?,?,?,?,?,?)", (
                "ev_doc", case_id, 1, "documentation", "obs-digest", canonical(observation),
            ))
            con.execute("INSERT INTO scenario_case_link VALUES(?,?,?,?,?)", (
                scenario["id"], scenario["revision"], case_id, 1, canonical(link),
            ))

    def test_enrichment_traces_case_increment_and_reports_safe_usage_without_mutation(self):
        research_job = "job_research_fixture"
        snapshot = {"v1": {"plan_id": self.plan["id"]}, "product_id": self.plan["seeds"][0]["product_id"]}
        with self.store.connect(True) as con:
            con.execute("INSERT INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                research_job, self.report["batch"]["id"], "case-research", "completed", "research", 1,
                None, None, canonical(snapshot), None, now(), now(),
            ))
        self._add_research_case(research_job)
        job = next(item for item in self.report["batch"]["jobs"] if item["id"] != research_job)
        stage = self.root / "state" / "jobs" / job["id"] / f"attempt-{job['attempt']}" / "review"
        stage.mkdir(parents=True)
        summary = {
            "requested_model": "provider/requested", "observed_model": "provider/observed",
            "usage_events": [{"event_type": "step_finish", "event_id": "evt1", "session_id": "sess1",
                              "message_id": "msg1", "cost": 0.25, "tokens": {
                                  "input": 12, "output": 5, "reasoning": 2,
                                  "cache": {"read": 3, "write": 1}},
                              "reported_usage": {"cost": 0.25, "tokens": {"input": 12, "output": 5,
                                  "reasoning": 2, "cache": {"read": 3, "write": 1}}},
                              "secret": "must not leak"}],
        }
        (stage / "cli-summary.json").write_text(json.dumps(summary))
        before_report = copy.deepcopy(self.report)
        with self.store.connect() as con:
            before_db = con.execute("SELECT count(*) FROM case_revision").fetchone()[0]

        enriched = enrich_report(self.store, self.report)

        self.assertEqual(self.report, before_report)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT count(*) FROM case_revision").fetchone()[0], before_db)
        increment = enriched["application_evidence_increment"]
        self.assertEqual(increment["new_case_revisions"], [{
            "case_id": "case_fixture", "revision": 1, "created_task_id": research_job, "app_id": "app:repo:fixture",
        }])
        self.assertEqual(increment["observation_kinds"]["documentation"]["count"], 1)
        self.assertEqual(increment["apps"]["new_app_ids"], [])
        self.assertEqual(increment["apps"]["classification_unknown_app_ids"], ["app:repo:fixture"])
        stage_record = next(item for item in enriched["usage"]["stages"] if item["job_id"] == job["id"])
        self.assertEqual(stage_record["requested_model"], "provider/requested")
        self.assertEqual(stage_record["observed_model"], "provider/observed")
        self.assertEqual(stage_record["usage_events"][0]["tokens"]["cache"], {"read": 3, "write": 1})
        self.assertIsNone(stage_record["cost_currency"])
        self.assertIsNone(enriched["usage"]["provider_requests"])
        self.assertNotIn("secret", json.dumps(enriched))

    def test_ratio_denominators_are_explicit_and_zero_ratio_is_unknown(self):
        report = {"plan": {"id": "plan_empty", "seeds": []}, "products": {}, "artifacts": []}
        enriched = enrich_report(self.store, report)
        self.assertEqual(enriched["ratios"]["product_reviewed"], {
            "numerator": 0, "denominator": 0, "ratio": None,
            "numerator_ids": [], "denominator_ids": [],
        })
        self.assertEqual(enriched["application_evidence_increment"]["product_denominator"], {
            "count": 0, "product_ids": [],
        })

    def test_legacy_usage_extracts_only_step_finish_and_keeps_unknown_currency(self):
        job = next(iter(self.report["batch"]["jobs"]))
        stage = self.root / "state" / "jobs" / job["id"] / f"attempt-{job['attempt']}" / "legacy"
        stage.mkdir(parents=True)
        (stage / "cli-summary.json").write_text(json.dumps({"requested_model": "x"}))
        (stage / "events.jsonl").write_text("\n".join([
            json.dumps({"type": "text", "text": "private prompt"}),
            json.dumps({"type": "step_finish", "id": "evt", "sessionID": "s", "part": {
                "cost": 0.4, "tokens": {"input": 7, "output": 2, "reasoning": 1,
                                          "cache": {"read": 4, "write": 0}},
            }}),
        ]) + "\n")
        enriched = enrich_report(self.store, self.report)
        item = next(record for record in enriched["usage"]["stages"] if record["stage"] == "legacy")
        self.assertEqual(len(item["usage_events"]), 1)
        self.assertEqual(item["usage_events"][0]["event_id"], "evt")
        self.assertEqual(item["usage_events"][0]["tokens"]["input"], 7)
        self.assertIsNone(item["usage_events"][0]["cost_currency"])
        self.assertNotIn("private prompt", json.dumps(enriched))

    def test_all_prior_attempts_are_included_with_bounded_safe_sources(self):
        job = self.report["batch"]["jobs"][0]
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET attempt=3 WHERE id=?", (job["id"],))
        jobs_root = self.root / "state" / "jobs" / job["id"]

        first = jobs_root / "attempt-1" / "generate"
        first.mkdir(parents=True)
        (first / "cli-summary.json").write_text(json.dumps({
            "requested_model": "requested/old", "observed_model": "observed/old",
            "exit_code": 1, "cli_status": "completed", "delivery_status": "failed", "failure_code": "cli_failed",
            "usage_events": [{"event_type": "step_finish", "event_id": "old-step", "cost": 1.0,
                              "tokens": {"input": 11, "output": 2}}],
        }))

        second = jobs_root / "attempt-2" / "research"
        second.mkdir(parents=True)
        (second / "cli-summary.json").write_text(json.dumps({"requested_model": "requested/middle", "cli_status": {}, "delivery_status": []}))
        (second / "events.jsonl").write_text(json.dumps({"type": "step_finish", "id": "middle-step",
            "part": {"cost": 2.0, "tokens": {"input": 22, "output": 3}}}) + "\n")

        third = jobs_root / "attempt-3" / "review"
        third.mkdir(parents=True)
        (third / "cli-summary.json").write_text(json.dumps({
            "requested_model": "requested/current", "usage_events": [{
                "event_type": "step_finish", "event_id": "current-step", "cost": 3.0,
                "tokens": {"input": 33, "output": 4},
            }],
        }))

        # Nested generated/source trees are not host stage summaries and must not be read.
        nested = first / "source-untrusted" / "fake-stage"
        nested.mkdir(parents=True)
        (nested / "cli-summary.json").write_text(json.dumps({"usage_events": [{"event_id": "fake"}]}))
        # A symlink to data outside the store is skipped, never followed.
        outside = self.root / "outside.json"
        outside.write_text(json.dumps({"usage_events": [{"event_id": "escaped"}]}))
        linked = jobs_root / "attempt-1" / "linked"
        linked.mkdir()
        (linked / "cli-summary.json").symlink_to(outside)

        enriched = enrich_report(self.store, self.report)
        records = [item for item in enriched["usage"]["stages"] if item["job_id"] == job["id"]]
        records.sort(key=lambda item: item["attempt"])
        self.assertEqual([item["attempt"] for item in records], [1, 2, 3])
        self.assertEqual([item["usage_events"][0]["event_id"] for item in records],
                         ["old-step", "middle-step", "current-step"])
        self.assertEqual(records[0]["requested_model"], "requested/old")
        self.assertEqual(records[0]["exit_code"], 1)
        self.assertEqual(records[0]["delivery_status"], "failed")
        self.assertEqual(records[0]["failure_code"], "cli_failed")
        self.assertIsNone(records[1]["exit_code"])
        self.assertIsNone(records[1]["cli_status"])
        self.assertIsNone(records[1]["delivery_status"])
        self.assertEqual(records[2]["requested_model"], "requested/current")
        self.assertTrue(all(item["usage_source_sha256"] for item in records))
        self.assertEqual(enriched["usage"]["unsafe_files_skipped"], 1)
        self.assertNotIn("fake", json.dumps(enriched))
        self.assertNotIn("escaped", json.dumps(enriched))

    def test_malformed_legacy_summary_is_reported_as_truncated_without_reading_symlink(self):
        job = self.report["batch"]["jobs"][0]
        stage = self.root / "state" / "jobs" / job["id"] / f"attempt-{job['attempt']}" / "malformed"
        stage.mkdir(parents=True)
        (stage / "cli-summary.json").write_text("{invalid json")
        enriched = enrich_report(self.store, self.report)
        item = next(record for record in enriched["usage"]["stages"] if record["stage"] == "malformed")
        self.assertTrue(item["usage_events_truncated"])
        self.assertEqual(item["usage_events"], [])
        self.assertTrue(item["summary_sha256"])

    def test_report_record_and_source_byte_caps_are_explicit(self):
        job = self.report["batch"]["jobs"][0]
        for attempt in (1, 2):
            stage = self.root / "state" / "jobs" / job["id"] / f"attempt-{attempt}" / "generate"
            stage.mkdir(parents=True)
            (stage / "cli-summary.json").write_text(json.dumps({
                "usage_events": [{"event_type": "step_finish", "event_id": f"step-{attempt}",
                                  "tokens": {"input": attempt}}],
            }))
        with patch("template_factory.v1_reporting.MAX_USAGE_RECORDS_PER_REPORT", 1):
            limited_records = enrich_report(self.store, self.report)
        self.assertEqual(len(limited_records["usage"]["stages"]), 1)
        self.assertTrue(limited_records["usage"]["truncated"])

        with patch("template_factory.v1_reporting.MAX_USAGE_SOURCE_BYTES_PER_REPORT", 1):
            limited_bytes = enrich_report(self.store, self.report)
        self.assertTrue(limited_bytes["usage"]["truncated"])
        self.assertEqual(limited_bytes["usage"]["stages"][0]["usage_events"], [])
        self.assertEqual(limited_bytes["usage"]["stages"][0]["summary_hash_scope"], "read_prefix")


if __name__ == "__main__":
    unittest.main()
