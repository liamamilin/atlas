"""Factory file responses retain the content type selected by dispatch."""

from io import BytesIO
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest.mock import patch

PACK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACK))
import drafts_api  # noqa: E402


class FactoryContentTypeTests(unittest.TestCase):
    def make_handler(self):
        handler = object.__new__(drafts_api.Handler)
        handler.wfile = BytesIO()
        handler.responses = []
        handler.headers_sent = []
        handler.send_response = lambda code: handler.responses.append(code)
        handler.send_header = lambda name, value: handler.headers_sent.append(
            (name, value)
        )
        handler.end_headers = lambda: None
        return handler

    def content_type(self, handler):
        return next(
            value for name, value in handler.headers_sent if name == "Content-Type"
        )

    def test_file_honors_explicit_text_type_and_defaults_to_zip(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "result.json"
            path.write_text('{"ready":true}')
            explicit = self.make_handler()
            explicit._file(path, path.name, "text/plain;charset=utf-8")
            self.assertEqual(self.content_type(explicit), "text/plain;charset=utf-8")
            self.assertEqual(explicit.wfile.getvalue(), path.read_bytes())

            legacy = self.make_handler()
            legacy._file(path, "legacy.zip")
            self.assertEqual(self.content_type(legacy), "application/zip")

    def test_factory_passes_dispatch_content_type_to_file_response(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "result.txt"
            path.write_text("step output")
            handler = self.make_handler()
            parsed = SimpleNamespace(path="/api/factory/output", query="")
            with patch.object(
                drafts_api.factory_api,
                "dispatch",
                return_value=(path, "result.txt", "text/plain;charset=utf-8"),
            ):
                handler._factory("GET", parsed)
            self.assertEqual(self.content_type(handler), "text/plain;charset=utf-8")
            self.assertEqual(handler.wfile.getvalue(), b"step output")


if __name__ == "__main__":
    unittest.main()
