import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import project_generation as pg  # noqa: E402


class GenerationContainmentTests(unittest.TestCase):
    """The API server's own state must not read as a provider write."""

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        pack = self.root / "pack"
        atlas = pack / "atlas"
        for path in ("atlas/assistant", "atlas/ask", "atlas/oss-discovery", "atlas/template-factory",
                     "projects/generation-runs/prj_a/gen_a", "projects/workspaces/prj_b", "src"):
            (pack / path).mkdir(parents=True)
        self.files = {
            "catalog": atlas / "oss-catalog.sqlite", "shm": atlas / "oss-catalog.sqlite-shm",
            "recovery": atlas / "oss-catalog.recovery.json", "thread": atlas / "assistant/ast_1.json",
            "projects_db": pack / "projects/atlas-projects.sqlite",
            "credentials": atlas / "model-config.json", "corpus": atlas / "atlas.sqlite",
            "source": pack / "src/app.py", "other_workspace": pack / "projects/workspaces/prj_b/main.py",
        }
        for path in self.files.values():
            path.write_text("before")
        self.run_dir = pack / "projects/generation-runs/prj_a/gen_a"
        env = patch.dict(os.environ, {
            "ATLAS_OSS_STORE": str(self.files["catalog"]),
            "ATLAS_FACTORY_ROOT": str(atlas / "template-factory"),
            "ATLAS_MODEL_CONFIG": str(self.files["credentials"]),
        })
        env.start()
        self.addCleanup(env.stop)
        import atlas_ask, atlas_assistant, oss_discovery
        for module, name, value in [(atlas_ask, "ASK_ROOT", atlas / "ask"),
                                    (atlas_assistant, "ROOT", atlas / "assistant"),
                                    (oss_discovery, "ROOT", atlas / "oss-discovery")]:
            patcher = patch.object(module, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def check(self, *changed):
        roots = (self.run_dir, *pg._server_state_roots(self.run_dir))
        before = pg._snapshot_source_tree(self.root, roots)
        for key in changed:
            self.files[key].write_text("after, longer")
        after = pg._snapshot_source_tree(self.root, roots)
        return pg._source_tree_violations(before, after)

    def test_server_state_changes_are_not_violations(self):
        violations = self.check("catalog", "shm", "recovery", "thread", "projects_db")
        self.assertEqual(violations, {"added": [], "removed": [], "changed": []})

    def test_credentials_corpus_source_and_other_workspaces_stay_checked(self):
        for key in ("credentials", "corpus", "source", "other_workspace"):
            with self.subTest(key=key):
                violations = self.check(key)
                self.assertEqual(len(violations["changed"]), 1, violations)

    def test_new_file_in_atlas_is_still_a_violation(self):
        roots = (self.run_dir, *pg._server_state_roots(self.run_dir))
        before = pg._snapshot_source_tree(self.root, roots)
        (self.root / "pack/atlas/planted.py").write_text("x")
        after = pg._snapshot_source_tree(self.root, roots)
        self.assertEqual(pg._source_tree_violations(before, after)["added"], ["pack/atlas/planted.py"])

    def test_directory_mtime_alone_is_not_a_violation(self):
        roots = (self.run_dir,)
        before = pg._snapshot_source_tree(self.root, roots)
        os.utime(self.root / "pack/atlas", (1, 1))
        after = pg._snapshot_source_tree(self.root, roots)
        self.assertEqual(pg._source_tree_violations(before, after)["changed"], [])


if __name__ == "__main__":
    unittest.main()
