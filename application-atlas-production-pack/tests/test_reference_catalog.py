"""The reviewed ProductReference catalog is immutable and ledger-gated."""
import hashlib
import copy
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch

from template_factory.api import dispatch
from template_factory.reference_catalog import ReferenceCatalog
from template_factory.store import FactoryError, FactoryStore, canonical, digest

_ASSISTED_TESTS = Path(__file__).resolve().parents[2] / "examples/assisted-trials/tests"
sys.path.insert(0, str(_ASSISTED_TESTS))
from test_product_reference_profile import fixture_reference, profile  # noqa: E402


class ReferenceCatalogTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pack = self.root / "pack"
        (self.pack / "atlas").mkdir(parents=True)
        with sqlite3.connect(self.pack / "atlas/atlas.sqlite") as con:
            con.execute("CREATE TABLE leaf(slug,name,name_zh,defining_core,overview)")
        self.store = FactoryStore(self.root / "factory", self.pack)
        self.catalog = ReferenceCatalog(self.store)

    def _record(self):
        data = b"formal reviewed reference fixture"
        package_sha = hashlib.sha256(data).hexdigest()
        ref_id = "ref_" + package_sha[:32]
        archive = self.catalog.root / (package_sha + ".zip")
        archive.write_bytes(data)
        body = {"id": ref_id, "name": "Bookmark Manager — Personal Link Library", "schema": "atlas.product-reference.v1",
                "package_sha256": package_sha, "reference_digest": "b" * 64, "pilot_id": "pilot-example",
                "leaf": "bookmark-manager", "revision_id": "r2", "status": "static_review_passed",
                "application_status": "application_not_run", "publication_status": "not_published",
                "case_refs": [], "manifest": {}, "reference": {}, "document": "# Personal Shelf"}
        with self.catalog._connect(write=True) as con:
            con.execute("INSERT INTO product_reference VALUES(?,?,?,?,?)",
                        (ref_id, package_sha, archive.name, canonical(body), "2026-10-22T00:00:00Z"))
        return body, data

    def test_catalog_read_routes_expose_reference_status_case_links_and_download(self):
        body, data = self._record()
        rows, status = dispatch("GET", "/api/factory/product-references", store=self.store)
        self.assertEqual(status, 200)
        self.assertEqual(rows[0]["id"], body["id"])
        self.assertEqual(rows[0]["status"], "static_review_passed")
        self.assertEqual(rows[0]["application_status"], "application_not_run")
        detail, status = dispatch("GET", f"/api/factory/product-references/{body['id']}", store=self.store)
        self.assertEqual(status, 200)
        self.assertEqual(detail["document"], "# Personal Shelf")
        package, name, mime = dispatch("GET", f"/api/factory/product-references/{body['id']}/download", store=self.store)
        self.assertEqual(package.read_bytes(), data)
        self.assertEqual(name, f"{body['id']}.product-reference.zip")
        self.assertEqual(mime, "application/zip")

    def test_import_requires_a_registered_local_revision_and_rejects_traversal(self):
        with self.assertRaises(FactoryError):
            self.catalog.import_reference({"pilot_id": "unregistered", "leaf": "bookmark-manager",
                                           "revision_id": "r2", "generation_path": "docs/a/bookmark-manager/r2/generation",
                                           "package_sha256": "a" * 64})
        with self.assertRaises(FactoryError):
            self.catalog.import_reference({"archive_base64": "arbitrary pass", "status": "static_review_passed"})
        with self.assertRaises(FactoryError):
            self.catalog._generation_dir("../../outside/bookmark-manager/r2/generation", "bookmark-manager", "r2")

    def test_download_refuses_tampered_immutable_package(self):
        body, _ = self._record()
        archive = self.catalog.root / (body["package_sha256"] + ".zip")
        archive.write_bytes(b"changed")
        with self.assertRaises(FactoryError) as caught:
            self.catalog.download(body["id"])
        self.assertEqual(caught.exception.code, "reference_catalog_integrity")

    def test_actual_revise_freeze_is_validated_only_after_completed_ledger_rows(self):
        source_root = self.root / "pinned"
        source_root.mkdir()
        source = source_root / "docs.md"
        source.write_text("# Notes\nThe product stores personal notes.\n", encoding="utf-8")
        source_sha = hashlib.sha256(source.read_bytes()).hexdigest()
        snapshot = {"repository": "https://github.com/example/notes",
                    "commit_sha": "0123456789abcdef0123456789abcdef01234567",
                    "local_root": str(source_root), "files": {"docs.md": source_sha}, "status": "not_run"}
        inputs = {"profile_version": profile.VERSION, "leaf": "fixture-leaf",
                  "scenario": {"name": "Save a note"},
                  "case_refs": [{"case_id": "case-fixture", "revision": 1, "digest": "a" * 64}],
                  "revision": "scenario-r1",
                  "trusted_source_ids": {"requirements": {"req-leaf": "The owner can save notes"},
                                          "upstream": {"source-doc": {"repository": snapshot["repository"],
                                              "commit_sha": snapshot["commit_sha"], "path": "docs.md", "sha256": source_sha}}}}
        inputs["digest"] = digest(inputs)
        spec = fixture_reference()
        observations = [["documentation", "docs.md", 1, 2, "The supplied docs describe saved notes."]]
        leaf_root = self.root / "docs/factory/fixture-leaf"
        parent_generation = leaf_root / "generation"
        parent_generation.mkdir(parents=True)
        registered_input = leaf_root / "INPUTS.json"
        registered_input.write_text(canonical(inputs), encoding="utf-8")
        def callback_for(result_spec, active_directory, sessions):
            def call(stage, payload, prompt, source_context):
                if stage == "research":
                    result = {"findings": ["The source describes notes"],
                              "observed_upstream": copy.deepcopy(observations), "gaps": ["Runtime not checked"]}
                elif stage == "author":
                    if isinstance(payload.get("revision"), dict):
                        return {"result": {"patch": [{"op": "replace", "path": "/surfaces/0/kind", "value": "cli"}]},
                                "session_id": sessions[stage]}
                    result = {"reference": copy.deepcopy(result_spec)}
                else:
                    result = {"input_digest": payload["input_digest"], "own_questions": ["Can the owner recover after a failed write?"],
                              "checks": {name: True for name in profile.CHECKS},
                              "observations": [{"index": 0, "accepted": True, "reason": "The cited source lines support the observation."}],
                              "verdict": "pass", "issues": []}
                    events = []
                    for name, entry in payload["material_manifest"].items():
                        if entry.get("required_read"):
                            events.append({"tool": "read", "status": "completed", "path": name,
                                           "content": (active_directory / name).read_text(encoding="utf-8")})
                    response = {"result": result, "session_id": sessions[stage], "read_events": events}
                    return response
                return {"result": result, "session_id": sessions[stage]}
            return call

        bad_spec = copy.deepcopy(spec)
        bad_spec["surfaces"][0]["kind"] = "phone"
        with self.assertRaises(ValueError):
            profile.generate(parent_generation, inputs, snapshot,
                             callback_for(bad_spec, parent_generation, {"research": "fixture-research", "author": "fixture-initial-author", "review": "unused"}))

        research_checkpoint = leaf_root / "official-checkpoints/research"
        research_checkpoint.mkdir(parents=True)
        for name in ("BINDING.json", "RESULT.json", "DELIVERED.json"):
            (research_checkpoint / name).write_bytes((parent_generation / "research" / name).read_bytes())
        (research_checkpoint / "cli-summary.json").write_text(json.dumps({"delivery_status": "delivered",
            "session_id": "fixture-research", "reservation_id": "bud_fixture_research",
            "requested_model": "fixture-model"}), encoding="utf-8")
        adapter_input = {"profile_payload": {"inputs": inputs, "snapshot_digest": digest({
            "snapshot": snapshot, "files": {"docs.md": source_sha}})}}
        adapter_binding = {"model": "fixture-model", "input_digest": digest(adapter_input)}
        (research_checkpoint / "input.json").write_text(canonical(adapter_input), encoding="utf-8")
        (research_checkpoint / "BINDING.json").write_text(canonical(adapter_binding), encoding="utf-8")
        research_result = json.loads((research_checkpoint / "RESULT.json").read_text(encoding="utf-8"))
        response = {"text": canonical(research_result)}
        (research_checkpoint / "original-response.json").write_text(canonical(response), encoding="utf-8")
        summary_path = research_checkpoint / "cli-summary.json"
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        summary["original_response_sha256"] = hashlib.sha256((research_checkpoint / "original-response.json").read_bytes()).hexdigest()
        summary_path.write_text(canonical(summary), encoding="utf-8")
        (research_checkpoint / "events.jsonl").write_text("", encoding="utf-8")
        (research_checkpoint / "DELIVERED.json").write_text(canonical({
            "binding_digest": digest(adapter_binding), "result_digest": digest(research_result)}), encoding="utf-8")

        revision_generation = leaf_root / "r2/generation"
        revision_generation.parent.mkdir(parents=True)
        parent_author = parent_generation / "author/RESULT.json"
        parent_author_sha = hashlib.sha256(parent_author.read_bytes()).hexdigest()
        revision_callback = callback_for(spec, revision_generation,
                                         {"research": "fixture-research", "author": "fixture-r2-author", "review": "fixture-r2-review"})
        result = profile.revise(revision_generation, inputs, snapshot, parent_generation, parent_author,
                                parent_author_sha, "r2", revision_callback)
        self.assertEqual(result["status"], "static_review_passed")
        archive = Path(result["reference_zip"])

        def write_official_stage(stage, reservation_id, session_id):
            checkpoint = revision_generation.parent / "official-checkpoints" / stage
            checkpoint.mkdir(parents=True, exist_ok=True)
            for name in ("BINDING.json", "RESULT.json", "DELIVERED.json"):
                (checkpoint / name).write_bytes((revision_generation / stage / name).read_bytes())
            (checkpoint / "cli-summary.json").write_text(json.dumps({"delivery_status": "delivered",
                "session_id": session_id, "reservation_id": reservation_id}), encoding="utf-8")
        write_official_stage("author", "bud_fixture_author", "fixture-r2-author")
        write_official_stage("review", "bud_fixture_review", "fixture-r2-review")

        revision_request = {"revision_id": "r2", "leaf": "fixture-leaf", "profile_version": profile.VERSION,
                            "prompt_digest": profile.PROMPT_DIGEST,
                            "parents": {"research": {"sha256": hashlib.sha256((parent_generation / "research/RESULT.json").read_bytes()).hexdigest()},
                                        "research_receipt": {"sha256": hashlib.sha256((parent_generation / "research/DELIVERED.json").read_bytes()).hexdigest()},
                                        "author": {"sha256": parent_author_sha}}}
        binding = {"input_path": str(registered_input.relative_to(self.root)),
                   "input_sha256": hashlib.sha256(registered_input.read_bytes()).hexdigest()}
        pilot = {"id": "pilot-fixture", "campaign_id": "campaign-fixture", "phase": "phase-fixture", "plan_id": "plan-fixture"}
        with self.store.connect(True) as con:
            con.execute("CREATE TABLE tf_budget_reservation (id TEXT, campaign_id TEXT, identity TEXT, phase TEXT, kind TEXT, status TEXT, stage TEXT)")
        args = (archive, hashlib.sha256(archive.read_bytes()).hexdigest(), revision_generation, pilot, revision_request, binding)
        with patch("template_factory.reference_catalog._profile_module", return_value=profile):
            with self.assertRaises(FactoryError) as caught:
                self.catalog._verify_archive(*args)
        self.assertEqual(caught.exception.code, "reference_ledger_incomplete")
        with self.store.connect(True) as con:
            for rid, stage, kind in (("bud_fixture_research", "reference/research/pilot-fixture", "research"),
                                      ("bud_fixture_author", "reference/author/pilot-fixture/r2", "production"),
                                      ("bud_fixture_review", "reference/review/pilot-fixture/r2", "review")):
                con.execute("INSERT INTO tf_budget_reservation VALUES(?,?,?,?,?,?,?)",
                            (rid, pilot["campaign_id"], "plan-fixture:fixture-leaf", pilot["phase"], kind, "completed", stage))
        with patch("template_factory.reference_catalog._profile_module", return_value=profile):
            manifest, verified_spec, rendered, case_refs = self.catalog._verify_archive(*args)
        self.assertEqual(manifest["revision_lineage"]["revision_id"], "r2")
        self.assertEqual(verified_spec, spec)
        self.assertIn("PRODUCT_REFERENCE.md", rendered)
        self.assertEqual(case_refs, inputs["case_refs"])

        with zipfile.ZipFile(archive) as original:
            archive_files = {item.filename: original.read(item.filename) for item in original.infolist()}
        revision_record = json.loads(archive_files["revision.json"])
        revision_record["diagnostics"].append("unbound alteration")
        altered_record = canonical(revision_record).encode() + b"\n"
        archive_files["revision.json"] = altered_record
        changed_manifest = json.loads(archive_files["manifest.json"])
        changed_manifest["file_sha256"]["revision.json"] = hashlib.sha256(altered_record).hexdigest()
        archive_files["manifest.json"] = canonical(changed_manifest).encode() + b"\n"
        altered_archive = self.root / "altered-revision.zip"
        with zipfile.ZipFile(altered_archive, "w", compression=zipfile.ZIP_DEFLATED) as changed:
            for name, content in archive_files.items():
                changed.writestr(name, content)
        altered_args = (altered_archive, hashlib.sha256(altered_archive.read_bytes()).hexdigest(),
                        revision_generation, pilot, revision_request, binding)
        with patch("template_factory.reference_catalog._profile_module", return_value=profile):
            with self.assertRaises(FactoryError) as caught:
                self.catalog._verify_archive(*altered_args)
        self.assertEqual(caught.exception.code, "reference_import_provenance")

        del archive_files["revision.json"]
        missing_manifest = json.loads(archive_files["manifest.json"])
        missing_manifest["file_sha256"].pop("revision.json")
        archive_files["manifest.json"] = canonical(missing_manifest).encode() + b"\n"
        missing_archive = self.root / "missing-revision.zip"
        with zipfile.ZipFile(missing_archive, "w", compression=zipfile.ZIP_DEFLATED) as changed:
            for name, content in archive_files.items():
                changed.writestr(name, content)
        missing_args = (missing_archive, hashlib.sha256(missing_archive.read_bytes()).hexdigest(),
                        revision_generation, pilot, revision_request, binding)
        with patch("template_factory.reference_catalog._profile_module", return_value=profile):
            with self.assertRaises(FactoryError) as caught:
                self.catalog._verify_archive(*missing_args)
        self.assertEqual(caught.exception.code, "reference_package_invalid")


if __name__ == "__main__":
    unittest.main()
