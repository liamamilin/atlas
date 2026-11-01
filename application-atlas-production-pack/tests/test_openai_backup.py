"""Luna request compatibility and safe .env import into an existing route."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_model as model
import configure_openai_backup as setup


class OpenAIBackupTests(unittest.TestCase):
    def setUp(self):
        self.values = {"OPENAI_API_KEY": "fixture-openai-key"}
        self.target = {"provider": "openai", "model": "gpt-6-luna",
                       "api_key": "fixture-openai-key", "base_url": "https://api.openai.com/v1", "style": "openai"}
        self.reply = {"choices": [{"message": {"content": "OK"}, "finish_reason": "stop"}],
                      "usage": {"prompt_tokens": 8, "completion_tokens": 1}}
        self.view = {"default": {"provider": "open-design", "model": "deepseek-v4.1-flash"},
                     "fallback": {"enabled": True, "provider": "opencode-go", "model": "deepseek-v4.1-flash"},
                     "providers": [{"id": "opencode-go", "models": ["deepseek-v4.1-flash"]}],
                     "presets": {"openai": {"models": ["gpt-6-luna"]}}}

    def test_luna_fast_and_tool_calls_use_official_parameters(self):
        for tools, thinking in [(None, False), ([{"type": "function", "function": {"name": "fixture"}}], True)]:
            with self.subTest(tools=bool(tools)), patch.object(model, "_post_json", return_value=self.reply) as post:
                reply = model._chat_openai(self.target, [], tools, 0, 128, None, 30, thinking)
                body = post.call_args.args[1]
                self.assertEqual(body["reasoning_effort"], "none")
                self.assertEqual(body["max_completion_tokens"], 128)
                self.assertNotIn("max_tokens", body)
                self.assertNotIn("thinking", body)
                self.assertEqual(reply["usage"]["completion_tokens"], 1)

    def test_reasoning_omits_temperature_and_gateway_keeps_its_parameters(self):
        with patch.object(model, "_post_json", return_value=self.reply) as post:
            model._chat_openai(self.target, [], None, 0, 128, None, 30, True)
            self.assertEqual(post.call_args.args[1]["reasoning_effort"], "medium")
            self.assertNotIn("temperature", post.call_args.args[1])
            gateway = {**self.target, "base_url": "https://example.test/v1"}
            model._chat_openai(gateway, [], None, 0, 128, None, 30, False)
            self.assertEqual(post.call_args.args[1]["thinking"], {"type": "disabled"})
            self.assertEqual(post.call_args.args[1]["max_tokens"], 128)

    def test_env_is_parsed_without_shell_evaluation_and_check_does_not_call_network(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / ".env"
            path.write_text('# comment\nexport OPENAI_API_KEY="fixture-$(never-run)"\n')
            self.assertEqual(setup.read_env(path)["OPENAI_API_KEY"], "fixture-$(never-run)")
        with patch.object(setup, "settings_request") as request, patch.object(model, "_post_json") as post:
            result = setup.configure(self.values)
        request.assert_not_called()
        post.assert_not_called()
        self.assertFalse(result["applied"])
        self.assertNotIn("fixture-openai-key", str(result))

    def test_missing_key_nonlocal_api_and_old_runtime_do_not_mutate_settings(self):
        with patch.object(setup, "settings_request") as request:
            for values in [{}, {**self.values, "ATLAS_API_URL": "https://example.test"}]:
                with self.assertRaises(ValueError):
                    setup.configure(values, apply=True)
            request.assert_not_called()
        old = {**self.view, "presets": {}}
        with patch.object(setup, "settings_request", return_value=old) as request:
            with self.assertRaisesRegex(ValueError, "尚未加载"):
                setup.configure(self.values, apply=True)
            self.assertEqual(request.call_count, 1)

    def test_failed_probe_keeps_existing_route_and_credentials(self):
        with patch.object(setup, "settings_request", return_value=self.view) as request, \
                patch.object(model, "_chat_openai", side_effect=model.ModelConfigError("fixture", code="unauthorized")):
            with self.assertRaises(model.ModelConfigError):
                setup.configure(self.values, apply=True)
        self.assertEqual(request.call_count, 1)
        self.assertEqual(self.view["fallback"]["provider"], "opencode-go")

    def test_verified_import_preserves_default_and_selects_luna_backup(self):
        saved = copy.deepcopy(self.view)
        saved["fallback"] = {"enabled": True, "provider": "openai", "model": "gpt-6-luna", "active": False}
        responses = [self.view, self.view, {}, {}, saved]
        with patch.object(setup, "settings_request", side_effect=responses) as request, \
                patch.object(model, "_post_json", return_value=self.reply) as post:
            result = setup.configure(self.values, apply=True)
        self.assertEqual(post.call_args.args[1]["max_completion_tokens"], 32)
        self.assertEqual(result["default"], self.view["default"])
        self.assertTrue(result["credential_verified"])
        calls = request.call_args_list
        self.assertEqual(calls[2].args[1], "/providers")
        self.assertEqual(calls[3].args[2]["from_provider"], "open-design")
        self.assertEqual(calls[3].args[2]["provider"], "openai")
        self.assertNotIn("fixture-openai-key", str(result))


if __name__ == "__main__":
    unittest.main()
