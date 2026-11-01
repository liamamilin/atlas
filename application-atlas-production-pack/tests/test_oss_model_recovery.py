"""Real workflow retry boundaries: no credential leaks, skipped candidates or endless requests."""
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import call, patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_model as model  # noqa: E402
from oss_batch import BatchJobs  # noqa: E402
from oss_catalog import CatalogStore, ModelServiceUnavailable  # noqa: E402
from oss_discovery import Model  # noqa: E402
from test_oss_discovery import SearchSource  # noqa: E402


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        env = patch.dict(os.environ, {model.CONFIG_ENV: str(self.root / "model-config.json")})
        env.start()
        self.addCleanup(env.stop)
        model.upsert_provider({"preset": "open-design", "api_key": "fixture-primary-custom-key"})
        model.upsert_provider({"preset": "opencode-go", "api_key": "fixture-go-key"})
        model.set_default("open-design", "deepseek-v4.1-flash")
        model.set_fallback({"enabled": True, "from_provider": "open-design", "provider": "opencode-go", "model": "deepseek-v4.1-flash"})
        self.run = {"id": "recovery-fixture", "model_calls": 0}
        self.saved = []
        self.extractor = Model(self.root, self.run, lambda r: self.saved.append(copy.deepcopy(r)), fast=True)

    @staticmethod
    def error(status=503, detail=b"upstream temporarily unavailable", headers=None):
        return HTTPError("https://example.test", status, "", headers or {}, io.BytesIO(detail))

    @staticmethod
    def reply():
        return {"model": "deepseek-v4.1-flash", "choices": [{"message": {"content": '{"ok":true}'}}], "usage": {"total_tokens": 12}}

    def ask(self):
        return self.extractor.ask("extract_open", "Return JSON", {"public": "fixture"})

    def test_transient_failure_recovers_and_then_uses_cache_without_repeating_request(self):
        with patch.object(model, "_post_json", side_effect=[self.error(), TimeoutError(), self.reply()]) as post, \
                patch("oss_discovery.time.sleep") as sleep:
            self.assertEqual(self.ask(), {"ok": True})
            self.assertEqual(self.ask(), {"ok": True})
        self.assertEqual(post.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(2), call(4)])
        self.assertEqual(post.call_args_list[0].args[1], post.call_args_list[2].args[1])
        self.assertEqual(self.run["model_calls"], 3)
        self.assertEqual(self.run["model_retry"]["state"], "recovered")
        self.assertEqual(self.run["model_errors"][0]["upstream_status"], 503)
        self.assertTrue(any(r.get("model_retry", {}).get("state") == "waiting" for r in self.saved))
        self.assertFalse(model.fallback_view()["active"])
        self.assertEqual(self.run["model_cache_hits"], 1)

    def test_rate_limit_respects_retry_after_without_switching_provider(self):
        with patch.object(model, "_post_json", side_effect=[self.error(429, headers={"Retry-After": "7"}), self.reply()]), \
                patch("oss_discovery.time.sleep") as sleep:
            self.ask()
        sleep.assert_called_once_with(7)
        self.assertFalse(model.fallback_view()["active"])
        self.assertEqual(self.run["model_errors"][0]["code"], "rate_limited")

    def test_long_retry_after_pauses_instead_of_retrying_earlier_than_requested(self):
        with patch.object(model, "_post_json", side_effect=self.error(429, headers={"Retry-After": "120"})) as post, \
                patch("oss_discovery.time.sleep") as sleep:
            with self.assertRaises(ModelServiceUnavailable):
                self.ask()
        self.assertEqual(post.call_count, 1)
        sleep.assert_not_called()
        self.assertEqual(self.run["model_retry"]["retry_after"], 120)
        self.assertFalse(self.run["model_retry"]["will_retry"])

    def test_permanent_http_errors_do_not_repeat_or_activate_fallback(self):
        for status in (400, 401, 403, 404, 422):
            with self.subTest(status=status), patch.object(model, "_post_json", side_effect=self.error(status)) as post, \
                    patch("oss_discovery.time.sleep") as sleep:
                with self.assertRaises(ModelServiceUnavailable):
                    self.ask()
                self.assertEqual(post.call_count, 1)
                sleep.assert_not_called()
                self.assertFalse(model.fallback_view()["active"])

    def test_supported_transient_statuses_and_disconnections_are_retryable(self):
        for error in [*[self.error(s) for s in (408, 425, 429, 500, 502, 503, 504)],
                      URLError("temporary name resolution failure"), TimeoutError(), ConnectionResetError("reset")]:
            with self.subTest(error=error):
                self.assertTrue(model._provider_error(error).retryable)
        self.assertFalse(model._provider_error(self.error(400, b"model is unavailable")).retryable)

    def test_retry_after_supports_http_date_and_invalid_values(self):
        with patch.object(model.time, "time", return_value=0):
            self.assertEqual(model._retry_after({"Retry-After": "Thu, 01 Jan 1970 00:00:09 GMT"}), 9)
        self.assertIsNone(model._retry_after({"Retry-After": "invalid"}))

    def test_all_server_error_statuses_preserve_the_upstream_code_and_allow_bounded_retries(self):
        for status in range(500, 600):
            with self.subTest(status=status):
                error = model._provider_error(self.error(status))
                self.assertTrue(error.retryable)
                self.assertEqual(error.upstream_status, status)
                self.assertEqual(error.code, "provider_error")

    def test_edge_520_with_retry_after_60_recovers_without_activating_go(self):
        with patch.object(model, "_post_json", side_effect=[self.error(520, b'Cloudflare could not parse the origin response', {"Retry-After": "60"}), self.reply()]) as post, \
                patch("oss_discovery.time.sleep") as sleep:
            self.assertEqual(self.ask(), {"ok": True})
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(60)
        self.assertEqual(self.run["model_errors"][0]["upstream_status"], 520)
        self.assertEqual(self.run["model_retry"]["state"], "recovered")
        self.assertFalse(model.fallback_view()["active"])

    def test_persistent_520_is_bounded_to_three_attempts_and_preserves_failure_details(self):
        def failed(*args):
            raise self.error(520, b'Cloudflare could not parse the origin response', {"Retry-After": "60"})
        with patch.object(model, "_post_json", side_effect=failed) as post, patch("oss_discovery.time.sleep") as sleep:
            with self.assertRaisesRegex(ModelServiceUnavailable, "HTTP 520"):
                self.ask()
        self.assertEqual(post.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(60), call(60)])
        self.assertEqual([r["upstream_status"] for r in self.run["model_errors"]], [520, 520, 520])
        self.assertEqual(self.run["model_retry"]["state"], "exhausted")
        self.assertFalse(list((self.root / "model-cache").glob("*.json")))
        self.assertFalse(model.fallback_view()["active"])

    def test_error_details_keep_http_status_but_redact_custom_keys_before_truncation(self):
        secret = "fixture-primary-custom-key"
        detail = ("x" * 380 + secret + " Bearer sk-secret-example-value").encode()
        with patch.object(model, "_post_json", side_effect=[self.error(502, detail), self.reply()]), \
                patch("oss_discovery.time.sleep"):
            self.ask()
        record = self.run["model_errors"][0]
        self.assertEqual(record["upstream_status"], 502)
        self.assertIn("[REDACTED]", record["message"])
        self.assertNotIn(secret, json.dumps(self.saved))
        self.assertNotIn("fixture-primary", record["message"])
        self.assertNotIn("sk-secret-example-value", json.dumps(self.saved))

    def test_quota_fallback_then_transient_go_failure_retries_go_and_caches_actual_provider(self):
        with patch.object(model, "_post_json", side_effect=[self.error(402, b"insufficient_balance"), self.error(), self.reply()]) as post, \
                patch("oss_discovery.time.sleep") as sleep:
            self.ask()
            self.ask()
        self.assertEqual(["open-design" in c.args[0] for c in post.call_args_list], [True, False, False])
        self.assertEqual(self.run["model_errors"][0]["provider"], "opencode-go")
        self.assertEqual(self.run["model_receipts"][-1]["provider"], "opencode-go")
        self.assertEqual(len(list((self.root / "model-cache").glob("*.json"))), 1)
        sleep.assert_called_once_with(2)

    def test_exhausted_retries_pause_real_job_and_resume_does_not_replay_saved_targets(self):
        store = CatalogStore(self.root / "test.sqlite", bootstrap=False)
        store.record_candidates("feed-reader", SearchSource().items, "fixture")
        seen = []
        def worker(store, leaf, run, selected_ids, search, on_candidate):
            for identifier in selected_ids:
                if not seen:
                    seen.append(identifier)
                    on_candidate(identifier, "accepted", "saved before outage")
                    continue
                Model(self.root, run, store._save_run, fast=True).ask("extract_open", "Return JSON", {"id": identifier})
                seen.append(identifier)
                on_candidate(identifier, "accepted", "saved after recovery")
        with patch("oss_batch.ROOT", self.root), patch.object(model, "_post_json", side_effect=lambda *a: (_ for _ in ()).throw(self.error())) as post, \
                patch("oss_discovery.time.sleep") as sleep:
            job = BatchJobs(store, worker, lambda *a, **kw: None).create(["feed-reader"], existing_only=True, auto_recovery=False)
        self.assertEqual((job["status"], job["processed"], job["total"]), ("paused_model", 1, 2))
        self.assertEqual(post.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(2), call(4)])
        self.assertIn("HTTP 503", job["pause_reason"])
        self.assertFalse(list((self.root / "model-cache").glob("*.json")))
        with store.connect() as con:
            run = json.loads(con.execute("SELECT data FROM oss_run WHERE id=?", (job["current_run"],)).fetchone()[0])
        self.assertEqual(len(run["model_errors"]), 3)
        with patch("oss_batch.ROOT", self.root), patch.object(model, "_post_json", return_value=self.reply()):
            resumed = BatchJobs(CatalogStore(store.path, bootstrap=False), worker, lambda *a, **kw: None).resume(job["id"])
        self.assertEqual((resumed["status"], resumed["processed"]), ("completed", 2))
        self.assertEqual(seen, [101, 102])


if __name__ == "__main__":
    unittest.main()
