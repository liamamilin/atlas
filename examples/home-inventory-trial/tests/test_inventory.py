"""Regression checks supplement the independently frozen HTTP probe."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
from serve import Inventory, money  # noqa: E402 — load the standalone app after adding its directory
from web_support import Error  # noqa: E402


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.inventory = Inventory(self.directory)
        self.item = self.inventory.mutate(
            "/api/items",
            {
                "name": "灯",
                "location_id": "uncategorized",
                "value": "100.00",
                "notes": "Receipt <script>alert(1)</script>",
            },
        )[0]

    def tearDown(self):
        self.temp.cleanup()

    def test_invalid_writes_and_stale_archive_preserve_snapshot(self):
        before = self.inventory.state({"view": "all"})
        for value in ["-1", "NaN", "1e2", "0.001", "1000000000", 1, None]:
            with self.subTest(value=value), self.assertRaises(Error):
                self.inventory.mutate(
                    "/api/items/update", {**self.item, "value": value}
                )
            self.assertEqual(before, self.inventory.state({"view": "all"}))
        with self.assertRaises(Error) as caught:
            self.inventory.mutate(
                "/api/items/archive", {"id": self.item["id"], "revision": 0}
            )
        self.assertEqual(caught.exception.code, "revision_conflict")
        self.assertEqual(before, self.inventory.state({"view": "all"}))

    def test_concurrent_edits_cannot_both_commit(self):
        def save(name):
            try:
                return self.inventory.mutate(
                    "/api/items/update", {**self.item, "name": name, "value": "90"}
                )[1]
            except Error as error:
                return error.status

        with ThreadPoolExecutor(max_workers=2) as pool:
            self.assertEqual(sorted(pool.map(save, ["first", "second"])), [200, 409])
        self.assertEqual(self.inventory.get(self.item["id"])["revision"], 2)

    def test_demo_is_only_on_first_initialization_and_money_is_integer(self):
        before = self.inventory.state({"view": "all"})
        Inventory(self.directory, demo=True)
        self.assertEqual(before, self.inventory.state({"view": "all"}))
        self.assertEqual(money("00000000000000001.01"), 101)
        self.assertEqual(money("999999999.99"), 99999999999)
        self.assertEqual(
            self.inventory.state({"q": "RECEIPT", "location": "uncategorized"})[
                "summary"
            ],
            {"count": 1, "total_minor": 10000},
        )

    def test_html_escape_and_failed_form_draft(self):
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]
        base = f"http://127.0.0.1:{port}"
        process = subprocess.Popen(
            [
                sys.executable,
                str(ROOT / "app/serve.py"),
                "--port",
                str(port),
                "--data-dir",
                str(self.directory),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            for _ in range(100):
                try:
                    with urlopen(base + "/api/health", timeout=1):
                        break
                except OSError:
                    time.sleep(0.05)
            with urlopen(base) as response:
                body = response.read().decode()
            self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", body)
            self.assertNotIn("<script>alert(1)</script>", body)
            draft = {
                "name": "My unsaved <lamp>",
                "location_id": "uncategorized",
                "value": "-4",
                "notes": "Unsaved <b>memo</b>",
            }
            with self.assertRaises(HTTPError) as caught:
                urlopen(Request(base + "/items/create", urlencode(draft).encode()))
            self.assertEqual(caught.exception.code, 400)
            body = caught.exception.read().decode()
            for escaped in (
                "My unsaved &lt;lamp&gt;",
                'value="-4"',
                "Unsaved &lt;b&gt;memo&lt;/b&gt;",
            ):
                self.assertIn(escaped, body)
            self.assertEqual(self.inventory.state()["summary"]["count"], 1)
            updated = self.inventory.mutate(
                "/api/items/update", {**self.item, "name": "Fresh name", "value": "90"}
            )[0]
            stale = {
                **self.item,
                "name": "Unsaved conflict",
                "value": "70",
                "notes": "Keep conflict draft",
            }
            with self.assertRaises(HTTPError) as conflict:
                urlopen(Request(base + "/items/update", urlencode(stale).encode()))
            self.assertEqual(conflict.exception.code, 409)
            body = conflict.exception.read().decode()
            self.assertIn("Unsaved conflict", body)
            self.assertIn("Keep conflict draft", body)
            self.assertEqual(
                self.inventory.get(self.item["id"]), {**updated, "archived": 0}
            )
        finally:
            process.terminate()
            process.wait(timeout=10)


if __name__ == "__main__":
    unittest.main()
