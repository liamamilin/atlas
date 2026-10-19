"""Host-side fixtures for effective G1 deadline snapshot validation only."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import time
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docker_acceptance


class EffectiveBudgetContextFixtureTest(unittest.TestCase):
    def setUp(self):
        self.binding = {
            "campaign_id": "campaign-fixture", "plan_id": "plan-fixture", "product_id": "product-fixture",
            "segment": "G1", "job_id": "job-fixture",
        }
        self.payload = {
            "schema": "atlas.g1-effective-budget.v1", "binding": self.binding,
            "base_started_at": time.time() - 30, "base_deadline": time.time() - 5,
            "effective_deadline": time.time() + 600, "deadline_source": "amendment",
            "amendment_id": "amendment-fixture", "activated_at": time.time() - 15,
            "new_deadline": time.time() + 600, "generated_at": time.time(),
        }
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "official-budget.json"
        self._write()

    def tearDown(self):
        self.temp.cleanup()

    def _write(self):
        self.path.write_text(json.dumps(self.payload), encoding="utf-8")
        self.sha = hashlib.sha256(self.path.read_bytes()).hexdigest()

    def _read(self, binding=None, sha=None):
        return docker_acceptance.read_pinned_budget_context(
            self.path, sha or self.sha, binding or self.binding,
        )

    def test_uses_official_amended_deadline_even_when_base_deadline_expired(self):
        self.assertEqual(self._read()["effective_deadline"], self.payload["effective_deadline"])

    def test_rejects_expired_deadline(self):
        self.payload["effective_deadline"] = time.time() - 1
        self._write()
        with self.assertRaisesRegex(ValueError, "expired"):
            self._read()

    def test_rejects_wrong_runtime_identity_or_segment(self):
        wrong = {**self.binding, "product_id": "other-product"}
        with self.assertRaisesRegex(ValueError, "binding"):
            self._read(binding=wrong)

    def test_rejects_snapshot_changed_after_host_pin(self):
        self.payload["effective_deadline"] += 1
        self.path.write_text(json.dumps(self.payload), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self._read()

    def test_rejects_unactivated_amendment(self):
        self.payload["activated_at"] = None
        self._write()
        with self.assertRaisesRegex(ValueError, "activation"):
            self._read()

    def test_t08_uses_its_own_base_deadline(self):
        self.binding["segment"] = "T08"
        self.payload.update(deadline_source="base", amendment_id=None, activated_at=None,
                            base_deadline=self.payload["effective_deadline"], new_deadline=None)
        self._write()
        self.assertEqual(self._read()["deadline_source"], "base")

    def test_t08_rejects_g1_amendment(self):
        self.binding["segment"] = "T08"
        self._write()
        with self.assertRaisesRegex(ValueError, "T08"):
            self._read()


if __name__ == "__main__":
    unittest.main()
