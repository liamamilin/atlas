import json
import io
import os
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import github_settings  # noqa: E402
from oss_catalog import GitHub, CatalogError, GitHubServiceUnavailable  # noqa: E402
from urllib.error import HTTPError  # noqa: E402


class GitHubSettingsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "credentials.json"
        context = patch.dict(os.environ, {"ATLAS_GITHUB_CONFIG": str(self.path), "ATLAS_GITHUB_TOKEN": ""})
        context.start()
        self.addCleanup(context.stop)

    def test_write_only_save_keep_delete_and_private_file_permissions(self):
        secret = "test-local-secret-not-a-real-token"
        saved = github_settings.save({"token": secret})
        self.assertNotIn(secret, json.dumps(saved))
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o600)
        self.assertEqual(github_settings.token(), secret)
        github_settings.save({"token": ""})
        self.assertEqual(github_settings.token(), secret)
        github_settings.save({"remove": True})
        self.assertFalse(self.path.exists())
        self.assertFalse(github_settings.public_view()["configured"])

    def test_local_settings_take_effect_immediately_and_environment_is_fallback(self):
        with patch.dict(os.environ, {"ATLAS_GITHUB_TOKEN": "environment-test-token"}):
            self.assertEqual(github_settings.public_view()["source"], "environment")
            github_settings.save({"token": "local-test-token"})
            self.assertEqual(github_settings.token(), "local-test-token")
            github_settings.save({"remove": True})
            self.assertEqual(github_settings.token(), "environment-test-token")

    def test_invalid_input_never_echoes_credential(self):
        secret = "test-credential\nwith-newline"
        with self.assertRaises(ValueError) as raised:
            github_settings.save({"token": secret})
        self.assertNotIn(secret, str(raised.exception))
        self.assertFalse(self.path.exists())

    def test_token_is_only_used_in_github_authorization_header_and_probe_is_sanitized(self):
        secret = "test-local-secret-not-a-real-token"
        github_settings.save({"token": secret})
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, *args):
                return json.dumps({"resources": {"core": {"limit": 5000, "remaining": 4999, "reset": 1}, "search": {"limit": 30, "remaining": 29, "reset": 1}}}).encode()
        class Opener:
            def open(inner, request, **kwargs):
                self.assertTrue(request.full_url.startswith("https://api.github.com/"))
                self.assertEqual(request.get_header("Authorization"), "Bearer " + secret)
                return Response()
        with patch("oss_catalog.build_opener", return_value=Opener()):
            result = github_settings.test_connection()
        self.assertNotIn(secret, json.dumps(result))
        self.assertEqual(result["limits"]["core"]["limit"], 5000)
        with self.assertRaises(ValueError):
            GitHub().get("https://example.com/")

    def test_read_only_requests_retry_a_transient_network_failure_once(self):
        with patch.object(GitHub, "_get", side_effect=[CatalogError("无法连接或读取 GitHub", 502), {"ok": True}]) as get, patch("oss_catalog.time.sleep"):
            self.assertEqual(GitHub().get("/rate_limit"), {"ok": True})
        self.assertEqual(get.call_count, 2)

    def test_rate_limit_deadline_is_propagated_to_durable_batch_recovery(self):
        for status, headers, expected in [(429, {'Retry-After': '120'}, 120),
                                           (403, {'X-RateLimit-Remaining': '0', 'X-RateLimit-Reset': '2000'}, 1001)]:
            with self.subTest(status=status):
                error = HTTPError('https://api.github.com/repositories/101', status, '', headers, io.BytesIO(b'rate limit exceeded'))
                with patch('oss_catalog.build_opener') as build, patch('oss_catalog.time.time', return_value=1000), patch('oss_catalog.time.sleep') as sleep:
                    build.return_value.open.side_effect = error
                    with self.assertRaises(GitHubServiceUnavailable) as raised:
                        GitHub().get('/repositories/101')
                self.assertEqual(raised.exception.retry_after, expected)
                self.assertTrue(raised.exception.retryable)
                self.assertEqual(raised.exception.upstream_status, status)
                sleep.assert_not_called()

    def test_invalid_token_requires_attention_while_resource_permission_errors_stay_local(self):
        for status in (401, 403):
            with self.subTest(status=status), patch('oss_catalog.build_opener') as build:
                build.return_value.open.side_effect = HTTPError('https://api.github.com/repositories/101', status, '', {}, io.BytesIO(b'permission denied'))
                with self.assertRaises(CatalogError) as raised:
                    GitHub().get('/repositories/101')
                self.assertEqual(isinstance(raised.exception, GitHubServiceUnavailable), status == 401)
                if status == 401:
                    self.assertFalse(raised.exception.retryable)

    def test_gateway_520_get_has_a_short_retry_before_deferring_to_batch_recovery(self):
        class Response:
            def __enter__(self): return self
            def __exit__(self, *args): pass
            def read(self, *args): return b'{"id":101}'
        with patch('oss_catalog.build_opener') as build, patch('oss_catalog.time.sleep') as sleep:
            build.return_value.open.side_effect = [HTTPError('https://api.github.com/repositories/101', 520, '', {}, io.BytesIO(b'gateway failure')), Response()]
            self.assertEqual(GitHub().get('/repositories/101'), {'id': 101})
        self.assertEqual(build.return_value.open.call_count, 2)
        sleep.assert_called_once_with(2)

    def test_retry_after_date_and_gateway_wait_are_preserved(self):
        with patch('oss_catalog.time.time', return_value=0):
            self.assertEqual(GitHub.retry_delay({'Retry-After': 'Thu, 01 Jan 1970 00:02:00 GMT'}), 120)
        with patch('oss_catalog.build_opener') as build, patch('oss_catalog.time.sleep') as sleep:
            build.return_value.open.side_effect = HTTPError('https://api.github.com/repositories/101', 503, '', {'Retry-After': '180'}, io.BytesIO(b'gateway failure'))
            with self.assertRaises(GitHubServiceUnavailable) as raised:
                GitHub().get('/repositories/101')
            self.assertEqual(raised.exception.retry_after, 180)
            self.assertEqual(build.return_value.open.call_count, 1)
            sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
