"""Focused regression tests. Real-browser journeys are recorded separately."""
from contextlib import contextmanager
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

MODULE = Path(__file__).resolve().parents[1] / "app/serve.py"
spec = importlib.util.spec_from_file_location("bookmark_trial", MODULE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class TrialTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name)
        self.lib = app.Library(self.path)

    @contextmanager
    def running(self):
        server = app.ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        server.library = self.lib
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}"
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

    def test_original_url_unicode_search_and_persistence(self):
        url = "http://localhost/Path?x=Two%20Words&y=1#frag"
        with self.lib.connect() as db:
            row = self.lib.save(db, {"url": url, "title": "台灯 ABC", "description": "暖光 Desk", "category": "阅读"})
        reopened = app.Library(self.path)
        with reopened.connect() as db:
            for q in ("台灯", "abc", "LOCALHOST", "desk"):
                result = reopened.records(db, "阅读", q)
                self.assertEqual([r["id"] for r in result], [row["id"]])
                self.assertEqual(result[0]["url"], url)
            self.assertEqual(reopened.records(db, "阅读", "Two%20Words"), [])
            self.assertEqual(reopened.records(db, "missing", ""), [])

    def test_invalid_input_is_atomic_and_recoverable(self):
        for url in ("not a URL", "javascript:alert(1)", "ftp://example.com", "http://bad host", "http://", "http://x:bad"):
            with self.assertRaises(app.InputError), self.lib.connect() as db:
                self.lib.save(db, {"url": url, "category": "must-not-be-created"})
        with self.lib.connect() as db:
            self.assertEqual(self.lib.records(db), [])
            self.assertNotIn("must-not-be-created", [c["name"] for c in self.lib.categories(db)])
            row = self.lib.save(db, {"url": "https://example.com/valid"})
            self.assertEqual(row["url"], "https://example.com/valid")

    def test_initialization_does_not_resurrect_renamed_presets(self):
        with self.lib.connect() as db:
            cat = next(c for c in self.lib.categories(db) if c["name"] == "待购")
            self.lib.change_category(db, "rename", {"name": "我的采购"}, cat["id"])
        self.lib = app.Library(self.path, demo=True)
        with self.lib.connect() as db:
            self.assertEqual(self.lib.records(db), [])
            names = [c["name"] for c in self.lib.categories(db)]
            self.assertIn("我的采购", names)
            self.assertNotIn("待购", names)

    def test_move_trash_category_deletion_and_restore(self):
        with self.lib.connect() as db:
            row = self.lib.save(db, {"url": "https://example.com/item", "category": "旧分类"})
            row = self.lib.update(db, row["id"], "move", {"category": "新分类"})
            new_category = row["category_id"]
            self.lib.update(db, row["id"], "delete", {})
            self.assertEqual(self.lib.records(db), [])
            self.assertIsNotNone(self.lib.record(db, row["id"])["trashed_at"])
            self.lib.change_category(db, "delete", {}, new_category)
            restored = self.lib.update(db, row["id"], "restore", {})
            default = next(c for c in self.lib.categories(db) if c["is_default"])
            self.assertEqual(restored["category_id"], default["id"])
            self.assertEqual(default["count"], 1)

    def test_category_errors_leave_records_unchanged(self):
        with self.lib.connect() as db:
            row = self.lib.save(db, {"url": "https://example.com/"})
        for value in ("", "   ", "x" * 121, None):
            with self.assertRaises(app.InputError), self.lib.connect() as db:
                self.lib.update(db, row["id"], "move", {"category": value})
            with self.lib.connect() as db:
                self.assertEqual(self.lib.record(db, row["id"]), row)

    def test_http_errors_origin_and_html_escaping(self):
        with self.running() as base:
            req = Request(base + "/api/bookmarks", data=b'{broken', headers={"Content-Type": "application/json"})
            with self.assertRaises(HTTPError) as err:
                urlopen(req)
            self.assertEqual(err.exception.code, 400)
            self.assertEqual(json.load(err.exception)["error"]["code"], "bad_request")
            req = Request(base + "/api/categories", data=b'{"name":"evil"}', headers={"Content-Type": "application/json", "Origin": "https://other.invalid"})
            with self.assertRaises(HTTPError) as err:
                urlopen(req)
            self.assertEqual(err.exception.code, 403)
            with self.assertRaises(HTTPError) as err:
                urlopen(base + "/go/missing-record")
            self.assertEqual(err.exception.code, 404)
            self.assertEqual(json.load(err.exception)["error"]["code"], "not_found")
            req = Request(base + "/api/bookmarks", data=json.dumps({"url": "http://localhost/a?b=1&x=2", "title": '<script>alert(1)</script>'}).encode(), headers={"Content-Type": "application/json", "Origin": base})
            with urlopen(req) as response:
                self.assertEqual(response.status, 201)
                row = json.load(response)
            with urlopen(base) as response:
                text = response.read().decode()
                self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", text)
                self.assertIn('href="http://localhost/a?b=1&amp;x=2"', text)
                self.assertEqual(response.headers["Referrer-Policy"], "same-origin")
                self.assertNotIn('<script>', text)
            with self.lib.connect() as db:
                self.assertEqual(self.lib.record(db, row["id"])["url"], "http://localhost/a?b=1&x=2")


if __name__ == "__main__":
    unittest.main()
