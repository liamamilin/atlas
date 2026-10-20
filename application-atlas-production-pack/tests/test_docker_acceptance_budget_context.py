import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[2]
EXECUTOR = ROOT / "docs/template-factory/v1-2026-10-19/independent/docker_acceptance.py"
SPEC = importlib.util.spec_from_file_location("atlas_docker_acceptance_budget_test", EXECUTOR)
docker_acceptance = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(docker_acceptance)


class DockerAcceptanceBudgetContextTests(unittest.TestCase):
    def _payload(self):
        now = time.time()
        return {
            "schema": "atlas.g1-effective-budget.v1",
            "binding": {"campaign_id": "campaign", "plan_id": "plan", "product_id": "product",
                        "segment": "G1", "job_id": "job-successor"},
            "effective_deadline": now + 86399,
            "generated_at": now,
            "deadline_source": "amendment_superseding_timing",
            "amendment_id": "bamd_" + "a" * 32,
            "activated_at": now - 1,
            "new_deadline": now - 1 + 86400,
            "supersedes": {"deadline_source": "authorized_external_pause_resume",
                           "source_id": "egrant_" + "b" * 32,
                           "activated_at": now - 10000,
                           "effective_deadline": now - 5000,
                           "authorization_digest": "c" * 64},
            "source_authorization": {"source_ref": "authorization.txt", "source_digest": "d" * 64},
        }

    def _read(self, payload):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "budget.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            expected = {"campaign_id": "campaign", "plan_id": "plan", "product_id": "product",
                        "segment": "G1", "job_id": "job-successor"}
            checksum = hashlib.sha256(path.read_bytes()).hexdigest()
            return docker_acceptance.read_pinned_budget_context(path, checksum, expected)

    def test_accepts_official_superseding_source_and_24_hour_summary(self):
        payload = self._payload()
        self.assertEqual(self._read(payload)["effective_deadline"], payload["new_deadline"])

    def test_rejects_incorrect_window_summary_or_missing_supersedes_binding(self):
        payload = self._payload()
        payload["new_deadline"] += 1
        with self.assertRaisesRegex(ValueError, "24-hour"):
            self._read(payload)
        payload = self._payload()
        del payload["supersedes"]["source_id"]
        with self.assertRaisesRegex(ValueError, "source, or authorization binding"):
            self._read(payload)

