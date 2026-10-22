"""Budget guard tests for the scoped product-reference pilot."""
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.full_auxiliary import _reference_pilot_reservation_locked
from template_factory.store import FactoryError, digest


class ReferencePilotBudgetTests(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.con.executescript("""
        CREATE TABLE auxiliary_full_plan(id TEXT,campaign_id TEXT,phase TEXT,status TEXT,model TEXT,
          max_calls INTEGER,deadline REAL,request_json TEXT);
        CREATE TABLE auxiliary_full_leaf(plan_id TEXT,slug TEXT,state TEXT,body TEXT);
        CREATE TABLE auxiliary_reference_pilot(id TEXT,plan_id TEXT,campaign_id TEXT,phase TEXT,
          request_json TEXT,request_digest TEXT,max_calls INTEGER,status TEXT,pause_anchor INTEGER DEFAULT 0);
        CREATE TABLE tf_budget_reservation(campaign_id TEXT,phase TEXT,identity TEXT,stage TEXT,status TEXT);
        CREATE TABLE auxiliary_full_event(id INTEGER PRIMARY KEY,plan_id TEXT,slug TEXT,kind TEXT,body TEXT,created REAL);
        """)
        self.request = {"leaves": [{"leaf": "bookmark-manager"}, {"leaf": "polling-application"}]}
        encoded = json.dumps(self.request)
        self.con.execute("INSERT INTO auxiliary_full_plan VALUES(?,?,?,?,?,?,?,?)",
                         ("plan-x", "campaign-x", "auxiliary-full-plan-x", "paused",
                          "open-design/deepseek-v4.1-flash", 7200, 1795181744.123177, "{}"))
        for leaf in ("bookmark-manager", "polling-application"):
            self.con.execute("INSERT INTO auxiliary_full_leaf VALUES(?,?,?,?)",
                             ("plan-x", leaf, "reused", json.dumps({"leaf_sha256": "f" * 64})))
        self.con.execute("INSERT INTO auxiliary_reference_pilot VALUES(?,?,?,?,?,?,?,?,?)",
                         ("pilot-x", "plan-x", "campaign-x", "auxiliary-full-plan-x",
                          encoded, digest(self.request), 6, "active", 0))

    def tearDown(self):
        self.con.close()

    def _reserve(self, *, leaf="bookmark-manager", stage="reference/research/pilot-x",
                 status="paused", kind="research"):
        if status != "paused":
            self.con.execute("UPDATE auxiliary_full_plan SET status=?", (status,))
        return _reference_pilot_reservation_locked(
            self.con, "campaign-x", "plan-x:" + leaf, "auxiliary-full-plan-x",
            "plan-x", "open-design/deepseek-v4.1-flash", stage, 1.0, kind,
            self.con.execute("SELECT * FROM auxiliary_reference_pilot").fetchone())

    def test_registered_leaf_and_stage_pass_while_full_plan_stays_paused(self):
        row = self._reserve()
        self.assertEqual(row["status"], "paused")

    def test_unregistered_leaf_is_rejected(self):
        with self.assertRaises(FactoryError):
            self._reserve(leaf="general-social-network")

    def test_wrong_stage_or_kind_is_rejected(self):
        with self.assertRaises(FactoryError):
            self._reserve(stage="reference/repair/pilot-x")
        with self.assertRaises(FactoryError):
            self._reserve(kind="runtime")

    def test_full_plan_resume_or_pilot_pause_blocks_dispatch(self):
        with self.assertRaises(FactoryError):
            self._reserve(status="running")
        self.con.execute("UPDATE auxiliary_reference_pilot SET status='paused'")
        with self.assertRaises(FactoryError):
            self._reserve()

    def test_new_full_plan_pause_event_revokes_pilot(self):
        self.con.execute("INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,?,?,?)",
                         ("plan-x", "control", json.dumps({"action": "pause", "reason": "new user pause"}), 2))
        with self.assertRaises(FactoryError):
            self._reserve()

    def test_resumed_plan_first_stage_keeps_legacy_dispatch(self):
        from template_factory.full_auxiliary import full_reservation_locked, MODEL
        from template_factory.store import digest
        self.con.execute("ALTER TABLE auxiliary_full_plan ADD COLUMN request_digest TEXT")
        self.con.execute("ALTER TABLE auxiliary_full_plan ADD COLUMN started REAL")
        self.con.execute("ALTER TABLE auxiliary_full_plan ADD COLUMN window_seconds INTEGER")
        self.con.execute("ALTER TABLE auxiliary_full_plan ADD COLUMN baseline INTEGER")
        original = {"model": MODEL}
        self.con.execute("UPDATE auxiliary_full_plan SET status='running',model=?,request_json=?,request_digest=?,started=1,window_seconds=2592000,baseline=99",
                         (MODEL, json.dumps(original), digest(original)))
        self.con.execute("UPDATE auxiliary_full_leaf SET state='running'")
        self.con.execute("CREATE TABLE auxiliary_workflow_gate(plan_id TEXT,body TEXT,updated REAL)")
        row = full_reservation_locked(self.con, "campaign-x", "plan-x:bookmark-manager",
                                      "auxiliary-full-plan-x", "plan-x", MODEL,
                                      "first/discovery/attempt-1", 2.0, kind="production")
        self.assertEqual(row["status"], "running")


class ReferencePilotInputBindingTests(unittest.TestCase):
    def test_new_inputs_and_snapshot_are_content_bound(self):
        from template_factory.reference_pilot import ReferencePilotService, PROFILE_SOURCE
        from template_factory.store import FactoryStore
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "pack"
            pack.mkdir()
            (root / Path(PROFILE_SOURCE).parent).mkdir(parents=True)
            source = Path(__file__).resolve().parents[2] / PROFILE_SOURCE
            (root / PROFILE_SOURCE).write_bytes(source.read_bytes())
            store = FactoryStore(root / "state", pack)
            service = object.__new__(ReferencePilotService)
            service.store = store
            upstream = b"pinned requirements"
            inputs = {
                "profile_version": "product-reference-v1",
                "leaf": {"id": "bookmark-manager"},
                "scenario": {"name": "Save and find a bookmark"},
                "case_refs": [{"case_id": "case-1", "revision": 1, "digest": "a" * 64}],
                "revision": "f" * 40,
                "trusted_source_ids": {
                    "requirements": ["requirement-1"],
                    "upstream": {"source-1": {"repository": "https://github.com/owner/repo",
                                                  "commit_sha": "f" * 40, "path": "README.md",
                                                  "sha256": __import__("hashlib").sha256(upstream).hexdigest()}},
                },
            }
            inputs["digest"] = digest(inputs)
            snapshot = {"repository": "https://github.com/owner/repo", "commit_sha": "f" * 40,
                        "local_root": str(root / "external-cache"),
                        "files": {"README.md": __import__("hashlib").sha256(upstream).hexdigest()}}
            input_path, snapshot_path = pack / "input.json", pack / "snapshot.json"
            input_path.write_text(json.dumps(inputs))
            snapshot_path.write_text(json.dumps(snapshot))
            import hashlib
            binding = {"input_path": "pack/input.json", "input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                       "snapshot_path": "pack/snapshot.json", "snapshot_sha256": hashlib.sha256(snapshot_path.read_bytes()).hexdigest()}
            service._verify_leaf_input(binding, "bookmark-manager")
            input_path.write_text(input_path.read_text() + " ")
            with self.assertRaises(FactoryError):
                service._verify_leaf_input(binding, "bookmark-manager")

    def test_register_is_idempotent_and_rejects_conflicting_scope(self):
        import hashlib
        from template_factory.budget import BudgetLedger
        from template_factory.reference_pilot import ReferencePilotService, PROFILE_SOURCE
        from template_factory.store import FactoryStore
        from template_factory.full_auxiliary import ensure_schema
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pack = root / "repo"
            pack.mkdir()
            (pack / Path(PROFILE_SOURCE).parent).mkdir(parents=True)
            source = Path(__file__).resolve().parents[2] / PROFILE_SOURCE
            source_file = pack / PROFILE_SOURCE
            source_file.write_bytes(source.read_bytes())
            store = FactoryStore(root / "state", pack / "application-atlas-production-pack")
            campaign, plan_id, phase = "atlas-v1-first-production-2026-10-19", "pilot-plan", "auxiliary-full-pilot-plan"
            BudgetLedger(store, campaign_id=campaign)
            scope_path, auth_path = pack / "scope.json", pack / "auth.txt"
            frozen = "d" * 64
            scope = {"full_plan_id": plan_id, "items": [{"leaf": "bookmark-manager", "covered": True,
                                                           "leaf_sha256": frozen}]}
            scope_path.write_text(json.dumps(scope))
            auth_path.write_text("authorized")
            scope_sha, auth_sha = hashlib.sha256(scope_path.read_bytes()).hexdigest(), hashlib.sha256(auth_path.read_bytes()).hexdigest()
            original = {"scope": {"path": "scope.json", "sha256": scope_sha},
                        "authorization": {"path": "auth.txt", "sha256": auth_sha}}
            with store.connect(True) as con:
                ensure_schema(con)
                con.execute("INSERT INTO auxiliary_full_plan(id,campaign_id,phase,request_json,request_digest,baseline,max_calls,window_seconds,model,status,created,started,deadline,reason) VALUES(?,?,?,?,?,99,7200,2592000,?,'paused',1,1,1795181744.123177,NULL)",
                            (plan_id, campaign, phase, json.dumps(original), digest(original), "open-design/deepseek-v4.1-flash"))
                con.execute("CREATE TABLE case_revision(case_id TEXT,revision INTEGER,digest TEXT,PRIMARY KEY(case_id,revision))")
                con.execute("INSERT INTO case_revision VALUES(?,?,?)", ("case-1", 1, "a" * 64))
                con.execute("INSERT INTO auxiliary_full_leaf VALUES(?,?,?,?,?,?)",
                            (plan_id, "bookmark-manager", 0, "reused", json.dumps({"leaf_sha256": frozen}), 1))
            upstream = b"pinned requirements"
            inputs = {"profile_version": "product-reference-v1", "leaf": {"id": "bookmark-manager"},
                      "scenario": {"name": "Save one bookmark"}, "case_refs": [{"case_id": "case-1", "revision": 1, "digest": "a" * 64}],
                      "revision": "f" * 40, "trusted_source_ids": {"requirements": ["req-1"], "upstream": {"source-1": {
                          "repository": "https://github.com/owner/repo", "commit_sha": "f" * 40, "path": "README.md",
                          "sha256": hashlib.sha256(upstream).hexdigest()}}}}
            inputs["digest"] = digest(inputs)
            snapshot = {"repository": "https://github.com/owner/repo", "commit_sha": "f" * 40, "local_root": str(root / "external-cache"),
                        "files": {"README.md": hashlib.sha256(upstream).hexdigest()}}
            (pack / "input.json").write_text(json.dumps(inputs))
            (pack / "snapshot.json").write_text(json.dumps(snapshot))
            profile_sha = hashlib.sha256(source_file.read_bytes()).hexdigest()
            ci_path = pack / "ci.json"
            code_sha = "e" * 40
            ci_path.write_text(json.dumps({"sha": code_sha, "status": "completed", "conclusion": "success"}))
            host = {"code_sha": code_sha, "new_host_sha256": {PROFILE_SOURCE: profile_sha},
                    "ci_proof": {"path": "ci.json", "sha256": hashlib.sha256(ci_path.read_bytes()).hexdigest()}}
            with store.connect(True) as con:
                con.execute("INSERT INTO auxiliary_full_event(plan_id,kind,body,created) VALUES(?,'host_revision',?,1)",
                            (plan_id, json.dumps({"request": host, "request_digest": digest(host)})))
            user_path = pack / "user.txt"
            user_path.write_text("Run a two leaf reference pilot")
            leaf = {"leaf": "bookmark-manager", "frozen_leaf_sha256": frozen,
                    "input_path": "input.json", "input_sha256": hashlib.sha256((pack / "input.json").read_bytes()).hexdigest(),
                    "snapshot_path": "snapshot.json", "snapshot_sha256": hashlib.sha256((pack / "snapshot.json").read_bytes()).hexdigest()}
            request = {"schema": "atlas.reference-pilot.v1", "campaign_id": campaign, "pilot_id": "pilot-one",
                       "plan_id": plan_id, "idempotency_key": "pilot-one-key", "profile_version": "product-reference-v1",
                       "prompt_digest": "0" * 64, "production_source_sha256": profile_sha,
                       "source_ci": {"code_sha": code_sha, "host_revision_digest": digest(host)},
                       "user_request": {"path": "user.txt", "sha256": hashlib.sha256(user_path.read_bytes()).hexdigest()},
                       "leaves": [leaf]}
            import importlib.util
            spec = importlib.util.spec_from_file_location("_pilot_test_profile", source_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            request["prompt_digest"] = module.PROMPT_DIGEST
            service = ReferencePilotService(store, campaign_id=campaign)
            receipt = service.register(request)
            self.assertEqual(receipt["status"], "active")
            self.assertEqual(service.register(request), receipt)
            with store.connect() as con:
                pilot = con.execute("SELECT * FROM auxiliary_reference_pilot WHERE id='pilot-one'").fetchone()
                plan = con.execute("SELECT * FROM auxiliary_full_plan WHERE id=?", (plan_id,)).fetchone()
                service.verify_call(con, pilot, request, plan)
                con.execute("UPDATE case_revision SET digest=? WHERE case_id='case-1'", ("b" * 64,))
                with self.assertRaises(FactoryError):
                    service.verify_call(con, pilot, request, plan)
            altered = {**request, "pilot_id": "pilot-two"}
            with self.assertRaises(FactoryError):
                service.register(altered)


if __name__ == "__main__":
    unittest.main()
