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

    def _authorized_external_resume(self):
        from template_factory.frozen_review_additional import AUTH_SHA256, REMAINING_SECONDS
        activated = time.time() - 20
        resume = {
            "grant_id": "egrant_" + "a" * 32,
            "job_id": "job_b01427592b164863aab5bedf7b3863bb",
            "campaign_id": "atlas-v1-first-production-2026-10-19",
            "plan_id": "plan_87059846caf345d2b2fe690657cf324f",
            "product_id": "product-c42848f63251507bd9d911a5",
            "previous_deadline": 1792495312.855422,
            "paused_at": 1792490680.244128,
            "remaining_seconds": REMAINING_SECONDS,
            "activated_at": activated,
            "effective_deadline": activated + REMAINING_SECONDS,
            "authorization_digest": AUTH_SHA256,
            "external_cli_sessions": 1,
        }
        self.payload.update(deadline_source="authorized_external_pause_resume",
                            time_resume=resume, activated_at=activated,
                            effective_deadline=resume["effective_deadline"],
                            new_deadline=resume["effective_deadline"], generated_at=activated + 1)
        self.binding.update({key: resume[key] for key in ("campaign_id", "plan_id", "product_id")})
        self._write()
        return resume

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

    def test_accepts_only_pinned_authorized_external_g1_resume(self):
        resume = self._authorized_external_resume()
        self.assertEqual(self._read()["time_resume"], resume)

    def test_external_resume_rejects_wrong_scope_authorization_and_arithmetic(self):
        for field, value in (("campaign_id", "other-campaign"),
                             ("job_id", self.binding["job_id"]),
                             ("authorization_digest", "0" * 64),
                             ("remaining_seconds", 4632.611293),
                             ("external_cli_sessions", True),
                             ("paused_at", True),
                             ("effective_deadline", time.time() + 500)):
            with self.subTest(field=field):
                resume = self._authorized_external_resume()
                resume[field] = value
                self._write()
                with self.assertRaises(ValueError):
                    self._read()

    def test_external_resume_is_g1_only_and_generated_after_activation(self):
        self._authorized_external_resume()
        self.binding["segment"] = "T08"
        self._write()
        with self.assertRaisesRegex(ValueError, "T08"):
            self._read()
        self.binding["segment"] = "G1"
        resume = self._authorized_external_resume()
        self.payload["generated_at"] = resume["activated_at"] - 1
        self._write()
        with self.assertRaisesRegex(ValueError, "does not match"):
            self._read()

    def test_external_resume_cannot_extend_another_runtime_product_or_plan(self):
        for field in ("campaign_id", "plan_id", "product_id"):
            with self.subTest(field=field):
                self._authorized_external_resume()
                self.binding[field] = "other-scope"
                self._write()
                with self.assertRaisesRegex(ValueError, "outside"):
                    self._read(binding=dict(self.binding))


if __name__ == "__main__":
    unittest.main()
