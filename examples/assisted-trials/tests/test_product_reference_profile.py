"""Fixture-only tests for the opt-in product-reference pipeline."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import shutil
import tempfile
import threading
import os
import subprocess
import unittest
import zipfile
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".." / "application-atlas-production-pack"))
import product_reference_profile as profile
from template_factory.store import digest


class ContractStabilityTests(unittest.TestCase):
    def test_prompt_and_contract_identity_are_stable_across_python_hash_seeds(self):
        script = "import product_reference_profile as p; import json; print(p.PROMPT_DIGEST); print(json.dumps(p.CONTRACT_SCHEMA,sort_keys=True))"
        path = str(Path(__file__).resolve().parents[1]) + os.pathsep + str(Path(__file__).resolve().parents[3] / "application-atlas-production-pack")
        outputs = [subprocess.check_output([sys.executable, "-c", script], env={**os.environ, "PYTHONPATH": path,
                   "PYTHONHASHSEED": str(seed)}, text=True) for seed in (1, 2, 100)]
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], outputs[2])


def fixture_reference():
    return {
        "schema": "atlas.product-reference.v1",
        "product_shape": {"name": "Tiny note keeper", "audience": "One person", "value": "Keep and find notes", "delivery_profile": "cli", "boundary": "A local personal tool", "excluded": ["Sync"]},
        "roles": [{"id": "role_owner", "name": "Owner", "goal": "Keep a note", "data_scope": "Own local notes"}],
        "objects": [{"id": "object_note", "name": "Note", "fields": [{"name": "text", "meaning": "The note text"}], "states": ["active"], "relations": []}],
        "actions": [{"id": "action_save", "name": "Save note", "role_ids": ["role_owner"], "object_ids": ["object_note"], "surface_ids": ["surface_notes"], "rule_ids": ["rule_save"], "preconditions": ["Text is supplied"], "effects": ["An active note is saved"], "failures": [{"condition": "Storage fails", "response": "Show an error", "recovery": "Keep entered text for retry"}], "transitions": [{"object_id": "object_note", "from_states": [], "to_state": "active"}], "basis_ids": ["basis_req"], "depends_on": []}],
        "surfaces": [{"id": "surface_notes", "name": "Notes", "kind": "cli", "purpose": "Save and find personal notes", "role_ids": ["role_owner"], "action_ids": ["action_save"], "sections": ["Text input", "Saved notes"], "navigation": [], "states": {"loading": "Loading notes", "empty": "No notes yet", "no_results": "No matches", "error": "Storage unavailable", "forbidden": "Local owner only"}, "query": {"search": "Search note text", "filter": "No filters", "sort": "Newest first", "pagination": "All notes", "bulk": "Not offered", "export": "Deferred"}}],
        "journeys": [{"id": "journey_save", "name": "Save a note", "goal": "Keep a note for later", "role_ids": ["role_owner"], "steps": [{"surface_id": "surface_notes", "action_id": "action_save", "role_id": "role_owner", "success": "The note appears in the saved list"}], "completion": "The note can be found again", "recovery": "Retry after storage becomes available"}],
        "rules": [{"id": "rule_save", "statement": "Saving creates one active note", "object_ids": ["object_note"], "basis_ids": ["basis_req"]}],
        "assertions": [{"id": "assert_save", "given": "A valid note is entered", "when": "The owner saves", "then": "One active note is listed", "negative": "Storage failure preserves input and creates no success indication", "action_ids": ["action_save"], "rule_ids": ["rule_save"], "journey_ids": ["journey_save"]}],
        "scope_options": [{"id": "scope_core", "name": "Core notes", "journey_ids": ["journey_save"], "extra_action_ids": [], "depends_on": [], "rationale": "Deliver the save and rediscovery loop"}],
        "basis": [{"id": "basis_req", "kind": "requirement", "statement": "The user needs to retain notes", "source_ids": ["req-leaf"], "depends_on": []}],
        "gaps": [{"id": "gap_sync", "statement": "Cross-device sync is not designed", "core": False, "action_ids": [], "resolution": "Consider only if product boundary changes"}],
    }


class ProductReferencePipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source_root = self.root / "pinned"
        self.source_root.mkdir()
        self.source = self.source_root / "docs.md"
        self.source.write_text("# Upstream\nIt stores text notes.\n", encoding="utf-8")
        self.snapshot = {"repository": "https://github.com/example/notes", "commit_sha": "0123456789abcdef0123456789abcdef01234567", "local_root": str(self.source_root),
                        "files": {"docs.md": hashlib.sha256(self.source.read_bytes()).hexdigest()}, "status": "not_run"}
        self.inputs = {"profile_version": profile.VERSION, "leaf": "personal-notes", "scenario": {"name": "save a note"},
                       "case_refs": [{"case_id": "case-fixture", "revision": 1, "digest": "a" * 64}], "revision": "rev-1",
                       "trusted_source_ids": {"requirements": {"req-leaf": "leaf.md"}, "upstream": {"up-docs": {"repository": self.snapshot["repository"], "commit_sha": self.snapshot["commit_sha"], "path": "docs.md", "sha256": self.snapshot["files"]["docs.md"]}}}}
        self.inputs["digest"] = digest({k: value for k, value in self.inputs.items() if k != "digest"})

    def callback(self, *, same_session=False, review_result=None):
        calls = []
        spec = fixture_reference()
        observations = [["documentation", "docs.md", 1, 2, "The supplied fixture documentation describes text notes."]]

        def call(stage, payload, prompt, source):
            calls.append(stage)
            if stage == "research":
                result = {"findings": ["Text notes are described"], "observed_upstream": observations, "gaps": ["No runtime observation"]}
            elif stage == "author":
                result = {"reference": copy.deepcopy(spec), "observations": copy.deepcopy(observations)}
            else:
                if review_result is not None:
                    result = copy.deepcopy(review_result)
                else:
                    result = {"input_digest": payload["input_digest"], "own_questions": ["Can the owner recover after storage failure?"], "checks": {x: True for x in profile.CHECKS}, "observations": [{"index": 0, "accepted": True, "reason": "The cited lines describe text notes only."}], "verdict": "pass", "issues": []}
            events = []
            if stage == "review":
                for name, entry in payload["material_manifest"].items():
                    # This fixture callback returns an explicit full-content receipt;
                    # it does not represent or claim a real model session.
                    events.append({"tool": "read", "status": "completed", "path": name,
                                   "content": (Path(self.output) / name).read_text(encoding="utf-8")})
            session = "fixture-author-review-same" if same_session and stage in {"author", "review"} else "fixture-" + stage
            return {"result": result, "session_id": session, "read_events": events}

        return call, calls

    def run_pipeline(self, directory, call):
        self.output = Path(directory)
        return profile.generate(directory, self.inputs, self.snapshot, call)

    def test_revision_reuses_research_and_requires_fresh_review_and_parent_binding(self):
        parent = self.root / "parent"
        callback, parent_calls = self.callback()
        broken = fixture_reference()
        broken["surfaces"][0]["kind"] = "mobile"

        def broken_parent(stage, payload, prompt, source):
            if stage == "author":
                parent_calls.append(stage)
                return {"result": {"reference": copy.deepcopy(broken),
                                    "observations": [["documentation", "docs.md", 1, 2, "The supplied fixture documentation describes text notes."]]},
                        "session_id": "fixture-author"}
            return callback(stage, payload, prompt, source)

        with self.assertRaisesRegex(ValueError, "unsupported surface kind"):
            self.run_pipeline(parent, broken_parent)
        parent_result = parent / "author/RESULT.json"
        parent_sha = hashlib.sha256(parent_result.read_bytes()).hexdigest()
        revised = copy.deepcopy(fixture_reference())
        revision_calls = []

        def revision_callback(stage, payload, prompt, source):
            revision_calls.append(stage)
            if stage == "author":
                self.assertEqual(payload["revision"]["parent_reference"], broken)
                self.assertTrue(any("unsupported surface kind" in x for x in payload["revision"]["diagnostics"]))
                result = {"patch": [{"op": "replace", "path": "/surfaces/0/kind",
                                      "value": revised["surfaces"][0]["kind"]}]}
            else:
                result = {"input_digest": payload["input_digest"], "own_questions": ["Can the owner recover after storage failure?"],
                          "checks": {x: True for x in profile.CHECKS},
                          "observations": [{"index": 0, "accepted": True, "reason": "The cited lines describe text notes only."}],
                          "verdict": "pass", "issues": []}
            events = []
            if stage == "review":
                for name in payload["material_manifest"]:
                    events.append({"tool": "read", "status": "completed", "path": name,
                                   "content": (Path(self.revision_output) / name).read_text(encoding="utf-8")})
            return {"result": result, "session_id": "revision-" + stage, "read_events": events}

        self.revision_output = self.root / "revision-r2"
        result = profile.revise(self.revision_output, self.inputs, self.snapshot, parent,
                                "author/RESULT.json", parent_sha, "r2", revision_callback)
        self.assertEqual(result["status"], "static_review_passed")
        self.assertEqual(result["reference"], revised)
        self.assertEqual(revision_calls, ["author", "review"])
        self.assertEqual(parent_calls, ["research", "author"])
        with zipfile.ZipFile(result["reference_zip"]) as archive:
            manifest = json.loads(archive.read("manifest.json"))
            self.assertEqual(manifest["artifact_kind"], "atlas.product-reference")
            self.assertEqual(manifest["revision_lineage"]["revision_id"], "r2")
        replay_calls = []
        replay = profile.revise(self.revision_output, self.inputs, self.snapshot, parent,
                                "author/RESULT.json", parent_sha, "r2",
                                lambda *args: replay_calls.append(args[0]))
        self.assertEqual(replay["status"], "static_review_passed")
        self.assertEqual(replay_calls, [])
        with self.assertRaisesRegex(ValueError, "SHA-256 differs"):
            profile.revise(self.root / "bad-parent", self.inputs, self.snapshot, parent,
                           "author/RESULT.json", "0" * 64, "r4", revision_callback)
        changed_inputs = copy.deepcopy(self.inputs)
        changed_inputs["scenario"]["name"] = "a different scenario"
        changed_inputs["digest"] = digest({k: value for k, value in changed_inputs.items() if k != "digest"})
        with self.assertRaisesRegex(ValueError, "parent inputs or pinned snapshot differ"):
            profile.revise(self.root / "bad-input", changed_inputs, self.snapshot, parent,
                           "author/RESULT.json", parent_sha, "r5", revision_callback)

    def test_revision_uses_bound_needs_changes_findings_for_valid_parent(self):
        parent = self.root / "needs-changes-parent"
        base_call, _ = self.callback()
        parent_calls = []

        def needs_changes_call(stage, payload, prompt, source):
            parent_calls.append(stage)
            response = base_call(stage, payload, prompt, source)
            if stage == "review":
                response["result"].update(verdict="needs_changes", issues=["Clarify recovery after a failed save.",
                    {"location": "journey", "issue": "Missing recovery"}])
                response["result"]["checks"]["journeys"] = False
            return response

        self.run_pipeline(parent, needs_changes_call)
        parent_result = parent / "author/RESULT.json"
        parent_sha = hashlib.sha256(parent_result.read_bytes()).hexdigest()
        revision_output = self.root / "needs-changes-revision"
        revision_calls = []

        def revised_call(stage, payload, prompt, source):
            revision_calls.append(stage)
            if stage == "author":
                self.assertIn("parent review: Clarify recovery after a failed save.",
                              payload["revision"]["diagnostics"])
                self.assertIn('parent review: {"issue":"Missing recovery","location":"journey"}',
                              payload["revision"]["diagnostics"])
            response = base_call(stage, payload, prompt, source)
            if stage == "review":
                response["read_events"] = [
                    {"tool": "read", "status": "completed", "path": name,
                     "content": (revision_output / name).read_text(encoding="utf-8")}
                    for name in payload["material_manifest"]
                ]
            return response

        result = profile.revise(revision_output, self.inputs, self.snapshot, parent,
                                "author/RESULT.json", parent_sha, "r3", revised_call)
        self.assertEqual(result["status"], "static_review_passed")
        self.assertEqual(parent_calls, ["research", "author", "review"])
        self.assertEqual(revision_calls, ["author", "review"])

        stale_parent = self.root / "stale-needs-changes-parent"
        self.run_pipeline(stale_parent, needs_changes_call)
        stale_input = stale_parent / "REVIEW_INPUT.json"
        altered = json.loads(stale_input.read_text(encoding="utf-8"))
        altered["reference"]["product_shape"]["value"] = "stale modified input"
        stale_input.write_text(json.dumps(altered), encoding="utf-8")
        stale_author = stale_parent / "author/RESULT.json"
        stale_sha = hashlib.sha256(stale_author.read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, "parent review result is not bound"):
            profile.revise(self.root / "stale-review-revision", self.inputs, self.snapshot,
                           stale_parent, "author/RESULT.json", stale_sha, "r3", revised_call)

    def test_machine_schema_matches_exact_root_and_enums(self):
        schema = profile.CONTRACT_SCHEMA
        self.assertEqual(set(schema["properties"]), {
            "schema", "product_shape", "roles", "objects", "actions", "surfaces",
            "journeys", "rules", "assertions", "scope_options", "basis", "gaps",
        })
        self.assertEqual(set(schema["required"]), set(schema["properties"]))
        surface = schema["properties"]["surfaces"]["items"]["properties"]
        self.assertEqual(set(surface["states"]["properties"]),
                         {"loading", "empty", "no_results", "error", "forbidden"})
        self.assertEqual(set(surface["kind"]["enum"]),
                         {"web", "desktop", "cli", "api", "library", "other"})
        allowed = profile._allowed_source_ids(self.inputs)
        basis_sources = profile._contract_schema_for(self.inputs)["properties"]["basis"]["items"]["properties"]["source_ids"]["items"]["enum"]
        self.assertEqual(basis_sources, allowed)
        spec = fixture_reference()
        spec["basis"][0]["source_ids"] = ["obs-01", "dc-01", "gap-01"]
        with self.assertRaisesRegex(ValueError, "untrusted source IDs: dc-01, gap-01, obs-01"):
            profile.validate_reference(spec, source_ids=set(allowed))
        issues = profile.diagnose_reference(spec, source_ids=set(allowed),
                                             observed_source_ids={"up-docs"})
        self.assertTrue(any("dc-01, gap-01, obs-01" in issue for issue in issues))

    def test_author_receives_host_owned_observation_ids(self):
        out = self.root / "host-observations"
        callback, _ = self.callback()
        seen = {}

        def inspect_author(stage, payload, prompt, source):
            if stage == "author":
                seen.update(payload)
            return callback(stage, payload, prompt, source)

        self.run_pipeline(out, inspect_author)
        self.assertEqual(seen["allowed_source_ids"], ["req-leaf", "up-docs"])
        self.assertEqual(seen["observation_evidence"][0]["source_id"], "up-docs")
        self.assertEqual(seen["contract_schema"]["properties"]["basis"]["items"]["properties"]["source_ids"]["items"]["enum"],
                         ["req-leaf", "up-docs"])

    def test_revision_patch_is_minimal_immutable_and_rejects_root_escape(self):
        parent = fixture_reference()
        payload = {"revision": {"parent_reference": parent}}
        patch = {"patch": [{"op": "replace", "path": "/product_shape/value",
                            "value": "Keep and find a note collection"}]}
        resolved = profile.resolve_authored_reference(patch, payload)
        self.assertEqual(resolved["product_shape"]["value"], "Keep and find a note collection")
        self.assertEqual(parent, fixture_reference())
        self.assertEqual(resolved["actions"], parent["actions"])
        for bad in (
            {"patch": [{"op": "replace", "path": "/", "value": {}}]},
            {"patch": [{"op": "replace", "path": "/schema", "value": "other"}]},
            {"patch": [{"op": "replace", "path": "/status", "value": "passed"}]},
            {"patch": [{"op": "replace", "path": "/product_shape/missing", "value": "x"}]},
            {"patch": [{"op": "replace", "path": "/product_shape~2value", "value": "x"}]},
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                profile.resolve_authored_reference(bad, payload)

    def test_authored_patch_parent_resolves_from_checkpoint_input(self):
        old = fixture_reference()
        old["product_shape"]["value"] = "parent value"
        author_input = {"revision": {"parent_reference": fixture_reference()}}
        author_result = {"patch": [{"op": "replace", "path": "/product_shape/value",
                                     "value": "parent value"}]}
        resolved = profile.resolve_authored_reference(author_result, author_input)
        self.assertEqual(resolved, old)

    def test_pass_export_and_zero_callback_replay(self):
        out = self.root / "output"
        callback, calls = self.callback()
        result = self.run_pipeline(out, callback)
        self.assertEqual(result["status"], "static_review_passed")
        self.assertTrue((out / "reference.zip").is_file())
        with zipfile.ZipFile(out / "reference.zip") as archive:
            receipt = json.loads(archive.read("review.json"))
            reviewed = json.loads(archive.read("review-result.json"))
        review_input = json.loads((out / "REVIEW_INPUT.json").read_text())
        self.assertEqual(receipt["snapshot_digest"], result["snapshot_digest"])
        self.assertEqual(receipt["snapshot_digest"], review_input["snapshot_digest"])
        self.assertEqual(digest(reviewed), receipt["review_result_digest"])
        self.assertEqual(calls, ["research", "author", "review"])
        replay = self.run_pipeline(out, callback)
        self.assertEqual(replay["status"], "static_review_passed")
        self.assertEqual(calls, ["research", "author", "review"])

    def test_changed_source_fails_durable_binding(self):
        out = self.root / "output"
        callback, _ = self.callback()
        self.run_pipeline(out, callback)
        self.source.write_text("# changed source\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_pipeline(out, callback)

    def test_read_metadata_aliases_preserve_raw_research_and_zero_call_replay(self):
        out = self.root / "metadata"
        original, calls = self.callback()
        def alias_call(stage, payload, prompt, source):
            response = original(stage, payload, prompt, source)
            if stage == "research":
                response["result"]["observed_upstream"][0][:2] = ["doc", "source/upstream/docs.md"]
            return response
        result = self.run_pipeline(out, alias_call)
        self.assertEqual(result["status"], "static_review_passed")
        raw = json.loads((out / "research/RESULT.json").read_text())
        self.assertEqual(raw["observed_upstream"][0][:2], ["doc", "source/upstream/docs.md"])
        proof = json.loads((out / "RESEARCH_METADATA_ADAPTATION.json").read_text())
        self.assertEqual(proof["raw_result_digest"], digest(raw))
        self.assertFalse(proof["statement_content_changed"])
        self.assertEqual(proof["canonical_observations"][0][:2], ["documentation", "docs.md"])
        with zipfile.ZipFile(out / "reference.zip") as archive:
            self.assertEqual(hashlib.sha256(archive.read("research.json")).hexdigest(), proof["raw_result_sha256"])
            self.assertEqual(json.loads(archive.read("research-metadata-adaptation.json")), proof)
        self.run_pipeline(out, alias_call)
        self.assertEqual(calls, ["research", "author", "review"])
        for bad in (["doc", "source/upstream/../docs.md", 1, 2, "Same claim"],
                    ["executed", "docs.md", 1, 2, "Same claim"],
                    ["doc", "docs.md", 1, 999, "Same claim"]):
            with self.assertRaises(ValueError):
                profile._observations([bad], self.snapshot, self.inputs["trusted_source_ids"])

    def test_export_interruption_resumes_after_review_without_new_calls(self):
        out = self.root / "output"
        callback, calls = self.callback()
        original = zipfile.ZipFile.writestr
        def interrupted(archive, name, data, *args, **kwargs):
            if name == "review.json":
                raise OSError("fixture interruption during compression")
            return original(archive, name, data, *args, **kwargs)
        with patch.object(zipfile.ZipFile, "writestr", interrupted):
            with self.assertRaisesRegex(OSError, "fixture interruption"):
                self.run_pipeline(out, callback)
        self.assertFalse((out / "reference.zip").exists())
        self.assertTrue((out / "REVIEW_RESULT.json").is_file())
        self.assertEqual(self.run_pipeline(out, callback)["status"], "static_review_passed")
        self.assertEqual(calls, ["research", "author", "review"])

    def test_source_identity_and_case_revision_must_be_fixed(self):
        malformed = copy.deepcopy(self.inputs)
        malformed["trusted_source_ids"]["upstream"]["up-docs"]["path"] = "../docs.md"
        malformed["digest"] = digest({k: value for k, value in malformed.items() if k != "digest"})
        with self.assertRaises(ValueError):
            profile._validate_inputs(malformed, self.snapshot)
        malformed = copy.deepcopy(self.inputs)
        malformed["case_refs"][0]["revision"] = 0
        malformed["digest"] = digest({k: value for k, value in malformed.items() if k != "digest"})
        with self.assertRaises(ValueError):
            profile._validate_inputs(malformed, self.snapshot)

    def test_new_review_content_cannot_reuse_prior_pass(self):
        out = self.root / "output"
        callback, _ = self.callback()
        self.run_pipeline(out, callback)
        review_input = out / "REVIEW_INPUT.json"
        changed = json.loads(review_input.read_text())
        changed["reference"]["product_shape"]["value"] = "Different content"
        review_input.write_text(json.dumps(changed), encoding="utf-8")
        with self.assertRaises(ValueError):
            self.run_pipeline(out, callback)

    def test_same_session_author_reviewer_rejected(self):
        out = self.root / "output"
        callback, _ = self.callback(same_session=True)
        with self.assertRaisesRegex(ValueError, "distinct actual sessions"):
            self.run_pipeline(out, callback)
        self.assertFalse((out / "reference.zip").exists())

    def test_bad_review_does_not_launch_second_review(self):
        out = self.root / "output"
        malformed = {"input_digest": "wrong", "checks": {}, "verdict": "pass", "issues": []}
        callback, calls = self.callback(review_result=malformed)
        with self.assertRaisesRegex(ValueError, "identity differs"):
            self.run_pipeline(out, callback)
        with self.assertRaisesRegex(ValueError, "identity differs"):
            self.run_pipeline(out, callback)
        self.assertEqual(calls.count("review"), 1)
        self.assertFalse((out / "reference.zip").exists())

    def test_needs_changes_is_retained_without_export(self):
        out = self.root / "output"
        identity = "will-be-replaced"
        result = {"input_digest": identity, "own_questions": ["Can the owner recover after storage failure?"], "checks": {x: False for x in profile.CHECKS}, "observations": [{"index": 0, "accepted": False, "reason": "The source is documentation only."}], "verdict": "needs_changes", "issues": ["Journey recovery is incomplete"]}
        callback, calls = self.callback(review_result=result)
        def bound_call(stage, payload, prompt, source):
            response = callback(stage, payload, prompt, source)
            if stage == "review":
                response["result"]["input_digest"] = payload["input_digest"]
            return response
        result = self.run_pipeline(out, bound_call)
        self.assertEqual(result["status"], "needs_changes")
        self.assertIsNone(result["reference_zip"])
        self.assertEqual(calls.count("review"), 1)

    def test_numbered_garbage_and_partial_reads_are_rejected(self):
        target = self.root / "view.txt"
        target.write_text("alpha\nbeta\n", encoding="utf-8")
        manifest = {"view.txt": {"sha256": hashlib.sha256(target.read_bytes()).hexdigest(), "required_read": True}}
        (self.root / "READ_VIEWS.json").write_text(json.dumps(manifest), encoding="utf-8")
        garbage = [{"tool": "read", "status": "completed", "path": "view.txt", "content": "1: alpha\n2: forged\n"}]
        with self.assertRaisesRegex(ValueError, "differs from bound line"):
            profile._verify_read_events(garbage, self.root, manifest)
        partial = [{"tool": "read", "status": "completed", "path": "view.txt", "content": "1: alpha\n"}]
        with self.assertRaisesRegex(ValueError, "full-content read coverage"):
            profile._verify_read_events(partial, self.root, manifest)

    def test_callback_cannot_change_review_material(self):
        out = self.root / "output"
        callback, _ = self.callback()
        def mutating(stage, payload, prompt, source):
            response = callback(stage, payload, prompt, source)
            if stage == "review":
                target = next((out / name for name, row in payload["material_manifest"].items()
                               if row.get("required_read")))
                target.write_text("mutated", encoding="utf-8")
            return response
        with self.assertRaisesRegex(ValueError, "review material changed"):
            self.run_pipeline(out, mutating)
        self.assertFalse((out / "reference.zip").exists())

    def test_corrupt_export_is_not_reused(self):
        out = self.root / "output"
        callback, calls = self.callback()
        self.run_pipeline(out, callback)
        (out / "reference.zip").write_bytes(b"corrupt")
        with self.assertRaises(Exception):
            self.run_pipeline(out, callback)
        self.assertEqual(calls, ["research", "author", "review"])

    def test_official_adapter_forwards_fixed_checkpoint_inputs_and_actual_events(self):
        budgets = {stage: {"ledger": object(), "identity": "fixture-identity",
                           "phase": "fixture-phase", "job_id": "fixture-job",
                           "stage": "first/" + stage + "/attempt-1", "kind": kind}
                   for stage, kind in profile.OfficialCheckpointAdapter._KINDS.items()}
        observed = {}

        def mocked_checkpoint(folder, payload, prompt, cli, budget, source, leaf, *, model):
            observed.update(folder=folder, payload=payload, prompt=prompt, cli=cli,
                            budget=budget, source=source, leaf=leaf, model=model)
            self.assertEqual((source / "upstream/docs.md").read_text(), self.source.read_text())
            self.assertTrue((source / "snapshot.json").is_file())
            (folder).mkdir(parents=True, exist_ok=True)
            (folder / "cli-summary.json").write_text(json.dumps({
                "delivery_status": "delivered", "session_id": "real-checkpoint-session",
                "requested_model": model}), encoding="utf-8")
            (folder / "events.jsonl").write_text('{"actual":"event"}\n', encoding="utf-8")
            return {"findings": []}

        cli = object()
        adapter = profile.OfficialCheckpointAdapter(self.root / "adapter", cli=cli,
                                                     budget_by_stage=budgets, model="test/model",
                                                     leaf_bytes=b"fixed leaf\n",
                                                     checkpoint_fn=mocked_checkpoint)
        source = {"snapshot": self.snapshot, "files": {"docs.md": self.source.read_text()}}
        prompt = "fixed stage prompt"
        response = adapter("research", {"a": 1}, prompt, source)
        self.assertEqual(response, {"result": {"findings": []},
                                    "session_id": "real-checkpoint-session",
                                    "read_events": [{"actual": "event"}]})
        self.assertIs(observed["cli"], cli)
        self.assertIs(observed["budget"], budgets["research"])
        self.assertEqual(observed["model"], "test/model")
        self.assertEqual(observed["leaf"], b"fixed leaf\n")
        self.assertEqual(observed["prompt"], prompt)
        self.assertEqual(observed["payload"]["adapter"]["prompt_sha256"],
                         hashlib.sha256(prompt.encode()).hexdigest())

    def test_official_adapter_requires_explicit_stage_budgets(self):
        with self.assertRaisesRegex(ValueError, "explicit research, author, and review budgets"):
            profile.OfficialCheckpointAdapter(self.root / "adapter", cli=object(),
                                              budget_by_stage={}, model="test/model",
                                              leaf_bytes=b"leaf", checkpoint_fn=lambda *a: None)

    def test_official_adapter_pipeline_reads_copied_checkpoint_paths(self):
        """Fixture integration of the real bridge; never launches a provider."""
        output = self.root / "pipeline-bridge"
        fixture_call, calls = self.callback()
        budgets = {stage: {"ledger": object(), "identity": "fixture", "phase": "fixture",
                           "job_id": "fixture", "stage": "first/" + stage + "/attempt-1", "kind": kind}
                   for stage, kind in profile.OfficialCheckpointAdapter._KINDS.items()}

        def checkpoint(folder, payload, prompt, cli, budget, source, leaf, *, model):
            stage = budget["stage"].split("/")[1]
            folder.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, folder / "source")
            response = fixture_call(stage, payload["profile_payload"], prompt, {})
            (folder / "cli-summary.json").write_text(json.dumps({
                "delivery_status": "delivered", "session_id": response["session_id"],
                "requested_model": model}))
            events = []
            if stage == "review":
                for name, row in payload["profile_payload"]["material_manifest"].items():
                    copied = folder / "source/review" / name
                    content = copied.read_text()
                    events.append({"part": {"tool": "read", "state": {
                        "status": "completed", "input": {"path": str(copied)},
                        "output": "\n".join(f"{i}: {line}" for i, line in enumerate(content.splitlines(), 1))}}})
            (folder / "events.jsonl").write_text("\n".join(json.dumps(event) for event in events))
            return response["result"]

        adapter = profile.OfficialCheckpointAdapter(output / "bridge", cli=object(),
            budget_by_stage=budgets, model="fixture/model", leaf_bytes=b"fixture leaf",
            checkpoint_fn=checkpoint)
        result = self.run_pipeline(output, adapter)
        self.assertEqual(result["status"], "static_review_passed")
        self.run_pipeline(output, adapter)
        self.assertEqual(calls, ["research", "author", "review"])

    def test_same_directory_concurrent_generation_fails_fast(self):
        out = self.root / "output"
        callback, _ = self.callback()
        entered, release = threading.Event(), threading.Event()
        errors = []

        def paused(stage, payload, prompt, source):
            entered.set()
            if not release.wait(5):
                raise RuntimeError("test callback timed out")
            return callback(stage, payload, prompt, source)

        def first_run():
            try:
                self.run_pipeline(out, paused)
            except Exception as error:  # surfaced below in the test thread
                errors.append(error)

        worker = threading.Thread(target=first_run)
        worker.start()
        self.assertTrue(entered.wait(5))
        try:
            with self.assertRaisesRegex(RuntimeError, "already active"):
                self.run_pipeline(out, callback)
        finally:
            release.set()
            worker.join(10)
        self.assertFalse(worker.is_alive())
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
