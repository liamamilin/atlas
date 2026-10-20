import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))
spec = importlib.util.spec_from_file_location("meetings_trial", ROOT / "app/serve.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class NotebookTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.lib = app.Notebook(Path(self.tmp.name))

    def test_plaintext_preserved_and_stale_edit_cannot_overwrite(self):
        body = '决策\n|行动|人|\n<script>不执行</script>\n尾行 & 引号 "\n'
        with app.connect(self.lib.path) as db:
            row, _ = self.lib.change(db, "/notes", {"title": "测试", "body": body})
        with app.connect(self.lib.path) as db:
            current, _ = self.lib.change(
                db,
                "/notes/update",
                {
                    "id": row["id"],
                    "revision": 1,
                    "title": "更新",
                    "body": body + "完成",
                    "project_id": row["project_id"],
                },
            )
        with self.assertRaises(app.Error) as error, app.connect(self.lib.path) as db:
            self.lib.change(
                db,
                "/notes/update",
                {
                    "id": row["id"],
                    "revision": 1,
                    "title": "旧版本",
                    "body": "不得覆盖",
                    "project_id": row["project_id"],
                },
            )
        self.assertEqual(error.exception.status, 409)
        with app.connect(self.lib.path) as db:
            self.assertEqual(self.lib.note(db, row["id"])["body"], current["body"])
        self.assertIn("&lt;script&gt;", app.h(body))

    def test_project_archive_search_and_restore_keep_origin(self):
        with app.connect(self.lib.path) as db:
            project, _ = self.lib.change(db, "/projects", {"name": "项目A"})
            other, _ = self.lib.change(db, "/projects", {"name": "项目B"})
            row, _ = self.lib.change(
                db,
                "/notes",
                {"title": "Z", "body": "正文SearchOnly", "project_id": project["id"]},
            )
            self.lib.change(db, "/notes/pin", {"id": row["id"]})
            self.lib.change(db, "/notes/archive", {"id": row["id"]})
            self.assertEqual(self.lib.state(db, {})["notes"], [])
            self.assertEqual(len(self.lib.state(db, {"q": "searchonly"})["notes"]), 1)
            self.assertEqual(
                self.lib.state(db, {"project": other["id"], "q": "SearchOnly"})[
                    "notes"
                ],
                [],
            )
            self.lib.change(db, "/notes/trash", {"id": row["id"]})
            self.assertEqual(self.lib.state(db, {"q": "SearchOnly"})["notes"], [])
            restored, _ = self.lib.change(db, "/notes/restore", {"id": row["id"]})
            self.assertEqual(
                (
                    restored["project_id"],
                    restored["archived"],
                    restored["pinned"],
                    restored["body"],
                ),
                (project["id"], 1, 1, "正文SearchOnly"),
            )

    def test_empty_body_has_no_partial_write(self):
        for body in ["", "   ", None]:
            with self.assertRaises(app.Error), app.connect(self.lib.path) as db:
                self.lib.change(db, "/notes", {"title": "无效", "body": body})
        with app.connect(self.lib.path) as db:
            self.assertEqual(self.lib.state(db, {})["notes"], [])
            self.assertEqual(len(self.lib.projects(db)), 1)


if __name__ == "__main__":
    unittest.main()
