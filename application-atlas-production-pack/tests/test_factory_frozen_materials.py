"""Lossless frozen-review presentation and read-only ACL tests against archived failure evidence."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from template_factory.cognition import REVIEW_PROMPT
from template_factory.frozen_review_materials import (
    PROMPT_APPEND, append_review_prompt, build_materials,
    extend_readonly_config, registered_read_resources, validate_readonly_config,
)

PACK = Path(__file__).resolve().parents[1]
REPO = PACK.parent
JOB = REPO / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/actual-frozen-review/job_b01427592b164863aab5bedf7b3863bb"


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _pointer_parts(value):
    return [part.replace("~1", "/").replace("~0", "~") for part in value.split("/")[1:]]


def _at(value, pointer):
    current = value
    for token in _pointer_parts(pointer):
        current = current[int(token)] if isinstance(current, list) else current[token]
    return current


class FrozenReviewMaterialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_bytes = (JOB / "input.json").read_bytes()
        cls.leaf_bytes = (JOB / "leaf.md").read_bytes()
        cls.source = JOB / "source"
        cls.input_doc = json.loads(cls.input_bytes)

    def test_real_diffs_and_long_texts_are_lossless_complete_and_deterministic(self):
        before = {p.relative_to(self.source).as_posix(): _sha(p.read_bytes()) for p in self.source.rglob("*") if p.is_file()}
        material = build_materials(self.input_bytes, self.leaf_bytes, self.source)
        again = build_materials(self.input_bytes, self.leaf_bytes, self.source)
        self.assertEqual(material["files"], again["files"])
        self.assertEqual(material["manifest"], again["manifest"])
        self.assertEqual(material["tree_digest"], again["tree_digest"])
        after = {p.relative_to(self.source).as_posix(): _sha(p.read_bytes()) for p in self.source.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

        entries = material["manifest"]["entries"]
        by_origin = {}
        for entry in entries:
            raw = material["files"][entry["path"]]
            self.assertEqual(_sha(raw), entry["sha256"])
            self.assertEqual(raw.decode("utf-8").encode("utf-8"), raw)
            for origin in entry["origins"]:
                by_origin[(origin["relative_path"], origin.get("json_pointer"))] = raw

        cumulative = self.input_doc["aggregate_repair_diff"]
        program_diffs = cumulative["program_diffs"]
        self.assertEqual(len(program_diffs), 6)
        for target, text in program_diffs.items():
            raw = by_origin[("input.json", "/aggregate_repair_diff/program_diffs/" + target.replace("~", "~0").replace("/", "~1"))]
            self.assertEqual(raw, text.encode("utf-8"))
            if target != "acceptance/runner.json":
                self.assertGreater(len(raw), 2000)
            self.assertIn(target, next(row["target_paths"] for row in entries if raw in [material["files"][row["path"]]]))

        r7 = cumulative["r7_incremental_diff"]
        for target, text in r7["program_diffs"].items():
            pointer = "/aggregate_repair_diff/r7_incremental_diff/program_diffs/" + target.replace("~", "~0").replace("/", "~1")
            self.assertEqual(by_origin[("input.json", pointer)], text.encode("utf-8"))
        for index, change in enumerate(r7["prepared_incremental_diff"]["spec_changes"]):
            for field in ("old", "new"):
                text = change.get(field)
                if isinstance(text, str) and len(text.encode()) > 2000:
                    pointer = f"/aggregate_repair_diff/r7_incremental_diff/prepared_incremental_diff/spec_changes/{index}/{field}"
                    self.assertEqual(by_origin[("input.json", pointer)], text.encode())

        # Cumulative architecture and generated metadata strings are independently indexed.
        for pointer in ("/aggregate_repair_diff/authored_fields_before/architecture_markdown",
                        "/aggregate_repair_diff/authored_fields_after/architecture_markdown",
                        "/aggregate_repair_diff/generated_metadata/files/acceptance~1plan.json/unified_diff"):
            self.assertIn(("input.json", pointer), by_origin)
            self.assertEqual(by_origin[("input.json", pointer)], _at(self.input_doc, pointer).encode())
        self.assertIn(("leaf.md", None), by_origin)
        self.assertIn(("input.json", "/leaf/content"), by_origin)
        self.assertEqual(by_origin[("input.json", "/leaf/content")], self.leaf_bytes)
        # Six original diffs appear in both input and frozen aggregate diff; dedup must preserve both origins.
        source_origin = ("source/inputs/aggregate-repair-diff.json", "/program_diffs/acceptance~1p0_library.py")
        input_origin = ("input.json", "/aggregate_repair_diff/program_diffs/acceptance~1p0_library.py")
        self.assertEqual(by_origin[input_origin], by_origin[source_origin])
        self.assertGreater(len(next(row for row in entries if row["path"] == next(e["path"] for e in entries if input_origin in [(o["relative_path"],o.get("json_pointer")) for o in e["origins"]]))["origins"]), 1)

        self.assertTrue(material["manifest"]["scan"]["long_physical_lines"])
        for segment in material["manifest"]["segments"]:
            joined = b"".join(material["files"][part["path"]] for part in segment["parts"])
            self.assertEqual(_sha(joined), segment["roundtrip_sha256"])
            self.assertTrue(all(len(material["files"][part["path"]]) <= 1600 for part in segment["parts"]))

    def test_prompt_only_appends_reading_instructions_and_config_acl_is_exact(self):
        prompt, identity = append_review_prompt(REVIEW_PROMPT)
        self.assertTrue(prompt.startswith(REVIEW_PROMPT))
        self.assertEqual(prompt[len(REVIEW_PROMPT):], identity["append_text"])
        self.assertEqual(identity["append_text"], "\n\n" + PROMPT_APPEND)
        self.assertEqual(identity["old_prompt_sha256"], _sha(REVIEW_PROMPT.encode()))
        self.assertEqual(identity["new_prompt_sha256"], _sha(prompt.encode()))

        materials = build_materials(self.input_bytes, self.leaf_bytes, self.source)
        original_config = json.loads((JOB / "opencode.json").read_bytes())
        original_reads = [r["resource"] for r in original_config["permissions"] if r["action"] == "read"]
        input_read = next(value for value in original_reads if value.endswith("/input.json"))
        original_dir = Path(input_read).parent
        with tempfile.TemporaryDirectory() as temp:
            effective_dir = Path(temp) / "attempt-2" / "cognitive-review"
            effective_dir.mkdir(parents=True)
            material_root = effective_dir / "review-materials"
            for rel, raw in materials["files"].items():
                path = material_root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            config, config_id = extend_readonly_config(original_config, original_dir, effective_dir, materials["manifest"])
            self.assertEqual(validate_readonly_config(config, effective_dir, materials["manifest"], config_id), config_id)
            resources = registered_read_resources(effective_dir,
                expected_manifest_digest=materials["manifest_digest"], expected_tree_digest=materials["tree_digest"])
            self.assertIn("review-materials", resources["relative"])
            self.assertIn(str(material_root.resolve()), resources["absolute"])
            added = set(resources["relative"])
            actual_reads = {r["resource"] for r in config["permissions"] if r["action"] == "read"}
            actual_reads_abs = {value for value in actual_reads if value.startswith("/")}
            self.assertTrue(all(path in actual_reads for path in added))
            self.assertTrue(all(path in actual_reads_abs for path in resources["absolute"]))
            ordered_resources = [rule["resource"] for rule in config["permissions"] if rule["action"] == "read"]
            expected_additions = [*resources["relative"], *resources["absolute"]]
            self.assertEqual(ordered_resources[-len(expected_additions):], expected_additions)
            self.assertFalse(any(r["action"] in {"write", "execute", "shell", "websearch", "webfetch"} for r in config["permissions"]))
            self.assertEqual([r for r in config["permissions"] if r["action"] == "*"][0],
                             {"action": "*", "resource": "*", "effect": "deny"})

            tampered = json.loads(json.dumps(config))
            tampered["permissions"].append({"action": "read", "resource": "review-materials/**", "effect": "allow"})
            with self.assertRaises(ValueError):
                validate_readonly_config(tampered, effective_dir, materials["manifest"])
            extra = material_root / "unregistered.txt"
            extra.write_text("not in manifest")
            with self.assertRaises(ValueError):
                registered_read_resources(effective_dir)
            extra.unlink()
            indexed = material_root / materials["manifest"]["entries"][0]["path"]
            indexed.write_bytes(indexed.read_bytes() + b"tamper")
            with self.assertRaises(ValueError):
                registered_read_resources(effective_dir)
            indexed.write_bytes(materials["files"][materials["manifest"]["entries"][0]["path"]])
            config2, config_id2 = extend_readonly_config(original_config, original_dir, effective_dir.parent / "attempt-3" / "cognitive-review", materials["manifest"])
            self.assertEqual(config_id2["config_digest"], config_id["config_digest"])


if __name__ == "__main__":
    unittest.main()
