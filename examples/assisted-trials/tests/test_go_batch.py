"""No real CLI calls: selected model binding and conservative three-item limits."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from produce_with_opencode import MODEL, AUTHOR, REVIEW, DISCOVERY, READABLE_REVIEW, checkpoint, prompts
from template_factory.budget import BudgetLedger
from template_factory.store import FactoryStore, FactoryError

MODEL_NEW = "opencode-go/minimax-m3.1-flash-free"


class GoBatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.store = FactoryStore(self.root / "store", self.root)
        self.now = [1000.0]
        self.ledger = BudgetLedger(self.store, campaign_id="test", clock=lambda: self.now[0])
        self.request = {"schema": "atlas.auxiliary-model-batch.v1", "campaign_id": "test", "phase": "auxiliary-batch-test",
                        "identity": "three-leaves", "model": MODEL_NEW, "max_cli_calls": 9, "window_seconds": 28800,
                        "authorization_sha256": "fixed", "items": [{"key": str(n), "leaf": "leaf-" + str(n), "leaf_sha256": "fixed", "scenario": "scenario"} for n in range(3)]}

    def test_batch_cap_is_shared_across_items_jobs_restarts_and_failures(self):
        self.ledger.register_auxiliary_batch(self.request["phase"], self.request["identity"], self.request)
        for n in range(9):
            row = self.ledger.reserve("three-leaves", self.request["phase"], requested_model=MODEL_NEW, job_id="item-" + str(n % 3))
            self.ledger.finish(row["id"], "failed", outcome="fixture")
        reloaded = BudgetLedger(self.store, campaign_id="test", clock=lambda: self.now[0])
        reloaded.register_auxiliary_batch(self.request["phase"], "three-leaves", self.request)
        with self.assertRaisesRegex(FactoryError, "limit exhausted"):
            reloaded.reserve("three-leaves", self.request["phase"], requested_model=MODEL_NEW, job_id="new-job")
        self.assertEqual(reloaded.snapshot()["cli_sessions_used"], 9)
        self.assertEqual(reloaded.snapshot()["segments"][0]["deadline"], 29800)

    def test_fixed_batch_cannot_change_model_leaf_or_get_new_window(self):
        self.ledger.register_auxiliary_batch(self.request["phase"], "three-leaves", self.request)
        for mutate in (lambda r: r.update(model=MODEL), lambda r: r.update(max_cli_calls=10),
                       lambda r: r["items"][0].update(scenario="changed"),
                       lambda r: r["items"][0].update(leaf="leaf-1")):
            changed = copy.deepcopy(self.request)
            mutate(changed)
            with self.assertRaises(FactoryError):
                self.ledger.register_auxiliary_batch(changed["phase"], "three-leaves", changed)
        self.ledger.begin_segment(self.request["phase"])
        self.now[0] += 28801
        self.ledger.register_auxiliary_batch(self.request["phase"], "three-leaves", self.request)
        with self.assertRaisesRegex(FactoryError, "deadline exhausted"):
            self.ledger.reserve("three-leaves", self.request["phase"], requested_model=MODEL_NEW)

    def test_selected_model_survives_checkpoint_and_cannot_relabel_old_result(self):
        class Fake:
            calls = 0
            def run(inner, directory, prompt, model, *args, **kwargs):
                inner.calls += 1
                return {"selected": model}
        cli, folder = Fake(), self.root / "calls/stage"
        result = checkpoint(folder, {}, "prompt", cli, {}, model=MODEL_NEW)
        self.assertEqual(result["selected"], MODEL_NEW)
        self.assertEqual(checkpoint(folder, {}, "prompt", cli, {}, model=MODEL_NEW), result)
        self.assertEqual(json.loads((folder / "BINDING.json").read_text())["model"], MODEL_NEW)
        with self.assertRaises(ValueError):
            checkpoint(folder, {}, "prompt", cli, {}, model=MODEL)
        self.assertEqual(cli.calls, 1)

    def test_other_segments_do_not_change_revision_provenance_call_count(self):
        for phase in ("old-revision", "new-batch"):
            for _ in range(2 if phase == "old-revision" else 3):
                reservation = self.ledger.reserve("item", phase, requested_model=MODEL_NEW)
                self.ledger.finish(reservation["id"], "completed")
        self.assertEqual(self.ledger.snapshot()["cli_sessions_used"], 5)
        self.assertEqual(self.ledger.segment_usage("old-revision")["cli_sessions_used"], 2)

    def test_generic_prompts_do_not_inject_home_care_or_rewrite_historical_prompts(self):
        self.assertEqual(prompts(), (DISCOVERY, AUTHOR, REVIEW, READABLE_REVIEW))
        discovery, author, review, readable = prompts("leaf-scenario-v1")
        self.assertNotIn("home/recurring-plan/history", discovery)
        self.assertNotIn("home/equipment anchoring", author)
        self.assertNotIn("home+recurring", review + readable)
        self.assertIn("fixed scenario", review)

    def test_failure_isolated_and_focused_replay_preserves_other_results(self):
        import hashlib
        import produce_go_batch as batch
        folder = self.root / "batch"
        folder.mkdir()
        pack = self.root / "pack"
        (pack / "applications").mkdir(parents=True)
        authorization = folder / "AUTHORIZATION.md"
        authorization.write_text("operator instruction")
        request = copy.deepcopy(self.request)
        request.update(authorization_ref=str(authorization), authorization_sha256=hashlib.sha256(authorization.read_bytes()).hexdigest())
        for item in request["items"]:
            source = pack / "applications" / (item["leaf"] + ".md")
            source.write_text("fixed leaf")
            item["leaf_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        request_path = folder / "BATCH_REQUEST.json"
        request_path.write_text(json.dumps(request))
        class Store:
            def __init__(inner, *args):
                inner.pack = pack
            def leaf(inner, slug):
                return {"slug": slug}
        class Ledger:
            def __init__(inner, *args, **kwargs):
                pass
            def register_auxiliary_batch(inner, phase, identity, value):
                return {"request": value}
            def snapshot(inner):
                return {"cli_sessions_used": 93}
        visited = []
        def fake_run(path, api):
            data = json.loads(path.read_text())
            item = data["items"][0]
            visited.append(item["key"])
            item["state"] = "blocked" if item["key"] == "0" else "registered_template_only"
            path.write_text(json.dumps(data))
            if item["key"] == "0":
                raise ValueError("retained first-item failure")
            return item
        with patch.object(batch, "FactoryStore", Store), patch.object(batch, "BudgetLedger", Ledger), patch.object(batch, "run", fake_run):
            batch.execute(request_path, "fixture://")
            self.assertEqual(visited, ["0", "1", "2"])
            batch.execute(request_path, "fixture://", only="1")
            values = json.loads((folder / "RESULTS.json").read_text())["items"]
            self.assertEqual([item["state"] for item in values], ["blocked", "registered_template_only", "registered_template_only"])
            self.assertEqual(visited, ["0", "1", "2", "1"])


if __name__ == "__main__":
    unittest.main()
