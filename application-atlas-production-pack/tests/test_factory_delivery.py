import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch

from template_factory.delivery import SCHEMA, prepare_application
from template_factory.store import FactoryError


def make_zip(files, metadata=None, symlink=None):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        for name, content in files.items():
            archive.writestr(name, content)
        if metadata is not None:
            archive.writestr("delivery.json", json.dumps(metadata))
        if symlink:
            info = zipfile.ZipInfo(symlink)
            info.create_system = 3
            info.external_attr = (0o120777 << 16)
            archive.writestr(info, "target")
    return buffer.getvalue()


def runtime(**updates):
    value = {"profile": "python-web", "port": 8080, "start": ["python3", "app.py"]}
    value.update(updates)
    return value


def metadata(files, root=".", runtime_value=None):
    return {"schema": SCHEMA, "root": root, "files": files,
            "runtime": runtime_value or runtime()}


class FactoryDeliveryTests(unittest.TestCase):
    def prepare(self, payload):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        return prepare_application(payload, Path(temp.name) / "out")

    def test_root_and_single_app_prefix_normalization_have_equivalent_inventory(self):
        plain = self.prepare(make_zip({"app.py": "print('hi')"}, metadata(["app.py"])))
        prefixed = self.prepare(make_zip({"app/app.py": "print('hi')"}, metadata(["app.py"], root="app")))
        alias = self.prepare(make_zip({"app/app.py": "print('hi')"}, metadata(["app.py"])))
        self.assertEqual(plain["files"], prefixed["files"])
        self.assertEqual(alias["files"]["app/app.py"], plain["files"]["app.py"])
        self.assertEqual(alias["normalizations"], [{"declared": "app.py", "path": "app/app.py"}])
        self.assertEqual(plain["app_root"], ".")
        self.assertEqual(prefixed["app_root"], "app")

    def test_rejects_traversal_absolute_backslash_and_repeated_prefix(self):
        for path in ("../app.py", "/app.py", "a/../../b", r"app\app.py", "app/app/app.py"):
            with self.subTest(path=path):
                payload = make_zip({"app.py": "x"}, metadata([path]))
                with self.assertRaises(FactoryError):
                    self.prepare(payload)

    def test_rejects_ambiguous_app_aliases_duplicate_and_undeclared_files(self):
        cases = (
            ({"app.py": "a", "app/app.py": "b"}, ["app.py"]),
            ({"app.py": "a"}, ["app.py", "app/app.py"]),
            ({"app.py": "a", "other.py": "b"}, ["app.py"]),
        )
        for files, declared in cases:
            with self.subTest(files=files, declared=declared):
                with self.assertRaises(FactoryError):
                    self.prepare(make_zip(files, metadata(declared)))
        duplicate = io.BytesIO()
        with zipfile.ZipFile(duplicate, "w") as archive:
            archive.writestr("app.py", "x")
            archive.writestr("app.py", "y")
            archive.writestr("delivery.json", json.dumps(metadata(["app.py"])))
        with self.assertRaises(FactoryError):
            self.prepare(duplicate.getvalue())

    def test_rejects_repeated_app_prefix_aliases_but_accepts_exact_nested_paths(self):
        with self.assertRaises(FactoryError):
            self.prepare(make_zip({"app/app.py": "x"}, metadata(["app/app/app.py"])))
        with self.assertRaises(FactoryError):
            self.prepare(make_zip({"app/app/app.py": "x"}, metadata(["app/app.py"], root="app")))
        exact = self.prepare(make_zip({"app/app.py": "x"}, metadata(["app/app.py"])))
        self.assertEqual(set(exact["files"]), {"app/app.py"})
        self.assertEqual(exact["normalizations"], [])

    def test_rejects_secret_internal_and_symlink_entries(self):
        for files, symlink in (({".env": "secret"}, None), ({".git/config": "x"}, None), ({"app.py": "x"}, "link")):
            with self.subTest(files=files, symlink=symlink):
                with self.assertRaises(FactoryError):
                    self.prepare(make_zip(files, metadata(list(files)), symlink=symlink))

    def test_root_app_allows_only_app_tree_and_keeps_metadata_out_of_inventory(self):
        result = self.prepare(make_zip({"app/index.html": "hi"}, metadata(["index.html"], root="app", runtime_value=runtime(profile="static-web", start=["python3", "-m", "http.server", "8080"]))))
        self.assertEqual(result["app_root"], "app")
        self.assertEqual(set(result["files"]), {"index.html"})
        with self.assertRaises(FactoryError):
            self.prepare(make_zip({"app/index.html": "hi", "extra.txt": "x"}, metadata(["index.html"], root="app", runtime_value=runtime(profile="static-web", start=["python3", "-m", "http.server", "8080"]))))

    def test_runtime_schema_and_command_allowlist_are_enforced(self):
        invalid = (
            runtime(port=True), runtime(port=80), runtime(start=["sh", "-c", "id"]),
            runtime(readiness_path="//example.com/"), runtime(readiness_path="/ok?token=x"),
            {"profile": "cli", "smoke": ["python3", "smoke.py"], "port": 8080},
            {"profile": "node-web", "port": 8080, "start": ["python3", "server.py"]},
            {"profile": "cli", "smoke": ["node", "smoke.js"]},
        )
        for config in invalid:
            with self.subTest(config=config):
                with self.assertRaises(FactoryError):
                    self.prepare(make_zip({"app.py": "x"}, metadata(["app.py"], runtime_value=config)))
        with self.assertRaises(FactoryError):
            self.prepare(make_zip({"app.py": "x"}, metadata(["app.py"], runtime_value=runtime(extra=True))))

    def test_preparation_never_runs_uploaded_commands(self):
        with tempfile.TemporaryDirectory() as temp:
            payload = make_zip({"app.py": "print('not executed')"}, metadata(["app.py"], runtime_value=runtime(install=[["pip", "install", "-r", "requirements.txt"]])))
            with patch("subprocess.Popen", side_effect=AssertionError("must not run")), patch("subprocess.run", side_effect=AssertionError("must not run")):
                result = prepare_application(payload, Path(temp) / "output")
            self.assertEqual(result["runtime"]["install"], [["pip", "install", "-r", "requirements.txt"]])


if __name__ == "__main__":
    unittest.main()
