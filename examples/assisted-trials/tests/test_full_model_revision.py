import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "application-atlas-production-pack"))
from template_factory.full_auxiliary import (
    FullAuxiliaryService, MODEL, REVISED_MODEL, ensure_schema, full_reservation_locked,
)
from template_factory.store import FactoryError, FactoryStore


class FullModelRevisionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        self.pack.mkdir()
        self.store = FactoryStore(self.root / "db", self.pack)
        self.service = FullAuxiliaryService(self.store, campaign_id="test", clock=lambda: 1000)
        self.plan_id = "plan-test"
        self.auth = self.root / "auth.txt"
        self.user_auth = self.root / "docs/template-factory/open-design-switch-2026-10-22/authorization/USER_MODEL_SWITCH.txt"
        self.scope = self.root / "scope.json"
        self.auth.write_text("authorized provider switch\n")
        self.user_auth.parent.mkdir(parents=True)
        self.user_auth.write_text("user authorizes provider switch\n")
        self.scope.write_text('{"full_plan_id":"plan-test","items":[{"leaf":"leaf"}]}')
        self.request = {
            "schema": "atlas.full-leaf-auxiliary-authorization.v1",
            "campaign_id": "test", "model": MODEL, "max_new_calls": 7200,
            "per_leaf_calls": 6, "concurrency": 2, "batch_size": 20,
            "window_seconds": 2592000, "baseline": 0, "full_plan_id": self.plan_id,
            "phase": "auxiliary-full-plan-test",
            "authorization": {"path": "auth.txt", "sha256": self.hash(self.auth)},
            "scope": {"path": "scope.json", "sha256": self.hash(self.scope)},
        }
        with self.store.connect(True) as con:
            ensure_schema(con)
        self.service.register(self.request)

    @staticmethod
    def hash(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def amendment(self):
        return {"schema": "atlas.full-leaf-model-revision.v1", "full_plan_id": self.plan_id,
                "previous_model": MODEL, "new_model": REVISED_MODEL,
                "authorization_sha256": self.request["authorization"]["sha256"],
                "authorization": {"path": "docs/template-factory/open-design-switch-2026-10-22/authorization/USER_MODEL_SWITCH.txt", "sha256": self.hash(self.user_auth)},
                "reason": "authorized provider replacement"}

    def pause(self):
        self.service.control(self.plan_id, "pause")

    def test_append_only_switch_idempotency_and_preserves_plan_limits(self):
        self.pause()
        req = self.amendment()
        receipt = self.service.register_model_revision(req)
        self.service.control(self.plan_id, "resume")
        self.assertEqual(self.service.register_model_revision(req), receipt)
        self.assertEqual(self.service.effective_model(self.plan_id), REVISED_MODEL)
        self.assertEqual(self.service.allowed_models(self.plan_id), [MODEL, REVISED_MODEL])
        status = self.service.status(self.plan_id)
        self.assertEqual((status["max_calls"], status["window_seconds"]), (7200, 2592000))
        self.assertEqual(status["model"], REVISED_MODEL)
        with self.store.connect() as con:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM auxiliary_full_event WHERE kind='model_revision'").fetchone()[0], 1)
        second = {**req, "previous_model": REVISED_MODEL, "reason": "second switch"}
        self.pause()
        with self.assertRaises(FactoryError):
            self.service.register_model_revision(second)
        self.assertEqual(self.service.effective_model(self.plan_id), REVISED_MODEL)

    def test_requires_pause_drain_original_files_and_exact_lineage(self):
        req = self.amendment()
        with self.assertRaises(FactoryError):
            self.service.register_model_revision(req)
        self.service.control(self.plan_id, "pause")
        for key, value in (("previous_model", "wrong"), ("authorization_sha256", "wrong")):
            bad = {**req, key: value}
            with self.assertRaises(FactoryError):
                self.service.register_model_revision(bad)
        self.auth.write_text("changed\n")
        with self.assertRaisesRegex(FactoryError, "authorization changed"):
            self.service.register_model_revision(req)

    def test_user_authorization_file_hash_is_separate_and_plan_model_is_verified(self):
        self.pause()
        req = self.amendment()
        for bad in ({**req, "authorization": {**req["authorization"], "sha256": "wrong"}},
                    {**req, "authorization": {"path": "../outside", "sha256": req["authorization"]["sha256"]}}):
            with self.assertRaises(FactoryError):
                self.service.register_model_revision(bad)
        self.user_auth.write_text("tampered\n")
        with self.assertRaisesRegex(FactoryError, "model revision authorization changed"):
            self.service.register_model_revision(req)
        self.user_auth.write_text("user authorizes provider switch\n")
        self.service.register_model_revision(req)
        with self.store.connect(True) as con:
            con.execute("UPDATE auxiliary_full_plan SET model=? WHERE id=?", (MODEL, self.plan_id))
        with self.assertRaisesRegex(FactoryError, "effective model binding changed"):
            self.service.effective_model(self.plan_id)

    def test_reservations_use_current_revision_and_original_scope(self):
        self.service.control(self.plan_id, "resume")
        self.service.update_leaf(self.plan_id, "leaf", "running", {})
        old_call = self.service.ledger.reserve(
            self.plan_id + ":leaf", self.request["phase"], requested_model=MODEL,
            plan_id=self.plan_id, stage="first/discovery/attempt-1",
        )
        self.service.ledger.finish(old_call["id"], "failed", outcome="fixture")
        self.pause()
        self.service.register_model_revision(self.amendment())
        with self.store.connect() as con:
            self.assertEqual(con.execute(
                "SELECT COUNT(*) FROM tf_budget_reservation WHERE id=?", (old_call["id"],)
            ).fetchone()[0], 1)
        with self.store.connect(True) as con:
            con.execute("UPDATE auxiliary_full_plan SET status='running' WHERE id=?", (self.plan_id,))
            con.execute("UPDATE auxiliary_full_leaf SET state='running' WHERE plan_id=?", (self.plan_id,))
            args = (con, "test", self.plan_id + ":leaf", self.request["phase"], self.plan_id)
            with self.assertRaisesRegex(FactoryError, "identity/model"):
                full_reservation_locked(*args, MODEL, "first/discovery/attempt-1", 1001)
            row = full_reservation_locked(*args, REVISED_MODEL, "first/blueprint-generate-aux/attempt-1", 1001)
            self.assertEqual(row["max_calls"], 7200)


if __name__ == "__main__":
    unittest.main()
