"""Quota-only failover, official Go transport, and durable routing state."""
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_model as model  # noqa: E402


class ModelFallbackTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "model-config.json"
        self.env = patch.dict(os.environ, {model.CONFIG_ENV: str(self.path)})
        self.env.start()
        self.addCleanup(self.env.stop)
        model.upsert_provider({"preset": "open-design", "api_key": "fixture-primary-key"})
        model.upsert_provider({"preset": "opencode-go", "api_key": "fixture-go-key"})
        model.set_default("open-design", "deepseek-v4.1-flash")
        model.set_fallback({"enabled": True, "from_provider": "open-design", "provider": "opencode-go", "model": "deepseek-v4.1-flash"})

    @staticmethod
    def quota():
        return HTTPError("https://example.test", 402, "", {}, io.BytesIO(b'{"error":{"code":"insufficient_balance"}}'))

    @staticmethod
    def reply():
        return {"model": "deepseek-v4.1-flash", "choices": [{"message": {"content": '{"ok":true}'}, "finish_reason": "stop"}], "usage": {"total_tokens": 12}}

    def test_quota_retries_same_request_then_persists_go_without_calling_primary_again(self):
        seen = []
        def post(url, body, headers, timeout):
            seen.append((url, body, headers))
            if "open-design" in url:
                raise self.quota()
            self.assertEqual(headers["x-opencode-session"], "batch-fixture")
            self.assertEqual(body["model"], "deepseek-v4.1-flash")
            self.assertEqual(headers["Authorization"], "Bearer fixture-go-key")
            return self.reply()
        messages = [{"role": "user", "content": "fixture"}]
        with patch.object(model, "_post_json", side_effect=post):
            first = model.complete(messages, session_id="batch-fixture", thinking=False)
            second = model.complete(messages, session_id="batch-fixture", thinking=False)
        self.assertEqual(["open-design" in request[0] for request in seen], [True, False, False])
        self.assertEqual(seen[0][1]["messages"], seen[1][1]["messages"])
        self.assertEqual(first["fallback"]["reason"], "quota_exhausted")
        self.assertEqual(second["provider"], "opencode-go")
        self.assertEqual(model.load_config()["default"]["provider"], "open-design")
        self.assertEqual(model.resolve()["source"], "fallback")
        self.assertEqual(model._fallback_state_path().stat().st_mode & 0o777, 0o600)
        self.assertNotIn("fixture-go-key", model._fallback_state_path().read_text())
        self.assertNotIn("fixture-primary-key", json.dumps(model.public_view()))

    def test_ordinary_rate_limit_network_and_auth_errors_do_not_activate_go(self):
        for status, detail, code in [(429, b"rate limit exceeded", "rate_limited"), (401, b"invalid key", "unauthorized"),
                                      (500, b"upstream unavailable", "provider_error"),
                                      (402, b'{"error":"Endpoint is unavailable"}', "provider_error")]:
            with self.subTest(status=status, detail=detail):
                error = HTTPError("https://example.test", status, "", {}, io.BytesIO(detail))
                with patch.object(model, "_post_json", side_effect=error) as post:
                    with self.assertRaises(model.ModelConfigError) as raised:
                        model.complete([{"role": "user", "content": "fixture"}])
                self.assertEqual(raised.exception.code, code)
                self.assertEqual(post.call_count, 1)
                self.assertFalse(model.fallback_view()["active"])

    def test_quota_in_429_or_403_is_distinct_from_normal_rate_limiting(self):
        for status, detail in [(429, b'{"error":{"code":"insufficient_quota"}}'), (403, '余额不足，请充值'.encode())]:
            with self.subTest(status=status):
                error = HTTPError("https://example.test", status, "", {}, io.BytesIO(detail))
                self.assertEqual(model._provider_error(error).code, "quota_exhausted")

    def test_explicit_provider_stays_explicit_and_reset_restores_primary(self):
        with patch.object(model, "_post_json", side_effect=self.quota()) as post:
            with self.assertRaises(model.ModelConfigError):
                model.complete([], provider="open-design")
        self.assertEqual(post.call_count, 1)
        self.assertFalse(model.fallback_view()["active"])
        model._activate_fallback(model.resolve())
        self.assertEqual(model.resolve(provider="open-design")["provider"], "open-design")
        model.set_fallback({"reset": True})
        self.assertEqual(model.resolve()["provider"], "open-design")

    def test_both_providers_failing_is_bounded_and_keeps_the_active_route(self):
        with patch.object(model, "_post_json", side_effect=[self.quota(), self.quota()]) as post:
            with self.assertRaises(model.ModelConfigError):
                model.complete([])
        self.assertEqual(post.call_count, 2)
        self.assertTrue(model.fallback_view()["active"])

    def test_legacy_go_url_migrates_and_public_model_list_has_no_auth_header(self):
        model.upsert_provider({"id": "opencode-go", "base_url": "https://opencode.ai/zen/go/v1"})
        self.assertEqual(model.resolve(provider="opencode-go", model="deepseek-v4.1-flash")["base_url"], model.PRESETS["opencode-go"]["base_url"])
        with patch.object(model, "_get_json", return_value={"data": [{"id": "deepseek-v4.1-flash"}]}) as get:
            self.assertEqual(model.list_models("opencode-go"), ["deepseek-v4.1-flash"])
        self.assertEqual(get.call_args.args[0], "https://opencode.ai/inference/go/v1/models")
        self.assertNotIn("Authorization", get.call_args.args[1])

    def test_disabled_route_and_invalid_self_fallback(self):
        with self.assertRaises(model.ModelConfigError):
            model.set_fallback({"enabled": True, "from_provider": "open-design", "provider": "open-design", "model": "m"})
        model.set_fallback({"enabled": False})
        with patch.object(model, "_post_json", side_effect=self.quota()) as post:
            with self.assertRaises(model.ModelConfigError):
                model.complete([])
        self.assertEqual(post.call_count, 1)

    def test_catalog_cache_and_receipt_use_the_effective_fallback_provider(self):
        from oss_discovery import Model
        root = Path(self.temp.name) / "cache"
        run = {"id": "batch-fixture", "model_calls": 0}
        extractor = Model(root, run, lambda run: None, fast=True)
        with patch.object(model, "_post_json", side_effect=[self.quota(), self.reply()]) as post:
            self.assertEqual(extractor.ask("fixture", "Return JSON", {}), {"ok": True})
            self.assertEqual(extractor.ask("fixture", "Return JSON", {}), {"ok": True})
        self.assertEqual(post.call_count, 2)
        self.assertEqual(run["model_cache_hits"], 1)
        self.assertEqual(len(list((root / "model-cache").glob("*.json"))), 1)
        self.assertEqual(run["model_receipts"][-1]["provider"], "opencode-go")
        self.assertEqual(run["model_receipts"][-1]["fallback"]["from_provider"], "open-design")

    def test_go_connection_test_verifies_credential_with_the_selected_fallback_model(self):
        with patch.object(model, "_get_json", return_value={"data": [{"id": "deepseek-v4.1-flash"}]}), \
                patch.object(model, "_post_json", return_value=self.reply()) as post:
            result = model.test_provider("opencode-go")
        self.assertTrue(result["ok"])
        self.assertTrue(result["credential_verified"])
        self.assertEqual(result["tested_model"], "deepseek-v4.1-flash")
        self.assertEqual(post.call_args.args[1]["model"], "deepseek-v4.1-flash")
        self.assertIn("x-opencode-session", post.call_args.args[2])

    def test_fallback_settings_route_is_write_only_and_survives_provider_edits(self):
        import drafts_api
        handler = object.__new__(drafts_api.Handler)
        handler._body = lambda: {"enabled": True, "from_provider": "open-design", "provider": "opencode-go", "model": "deepseek-v4.1-flash"}
        handler._json = lambda value, status=200: (value, status)
        body, status = handler._settings_model_post("/api/settings/model/fallback")
        self.assertEqual(status, 200)
        self.assertEqual(body["provider"], "opencode-go")
        self.assertNotIn("api_key", body)
        model.upsert_provider({"id": "opencode-go", "name": "Go updated"})
        self.assertTrue(model.load_config()["fallback"]["enabled"])


if __name__ == "__main__":
    unittest.main()
