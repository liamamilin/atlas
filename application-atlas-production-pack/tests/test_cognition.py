"""Cognition queue/production contracts with fake CLI. Not model-quality evidence."""

from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import test_blueprints as blueprint_fixtures
from template_factory.blueprints import import_blueprint
from template_factory.cognition import (
    DESIGN_DIMENSIONS,
    DIMENSIONS,
    apply_file_response,
    apply_review_reference_repair,
    apply_spec_revision,
    pinned_research,
    research_context,
    scoped_file_plan,
    validate_file_plan,
    validate_research,
    validate_review,
)
from template_factory.pipeline import Pipeline
from template_factory.store import FactoryError, digest


class FakeCognitionCLI:
    def __init__(self, source):
        self.source = source
        self.calls = []
        self.fail_generation = False
        self.bad_structure_once = False
        self.review_outcome = "passed"
        self.review_invalid_path = None
        self.review_repair_response = None
        self.on_generate = None
        self.fail_file_once = False
        self.reuse_files = False
        self.bad_manifest_once = False
        self.bad_patch_count = 0
        self.design_blocks = 0
        self.design_block_dimension = None
        self.design_outcome = "passed"
        self.design_sources = []
        self.design_requests = []
        self.spec_repair_requests = []
        self.fail_design_dimension_once = None
        self.research_with_reserved_source = False
        self.fail_research_repair = False

    def info(self, *args, **kwargs):
        return {"available": True, "backend": "test-double"}

    def run(self, directory, prompt, model, timeout, cancelled, progress):
        stage = directory.name
        self.calls.append(stage)
        fixture = json.loads((self.source / "template.json").read_text())
        if stage == "blueprint-research":
            sources = deepcopy(fixture["sources"][1:])
            if self.research_with_reserved_source:
                sources.insert(
                    0,
                    {
                        "id": "S01",
                        "name": "Atlas local input",
                        "url": "file:///workspace/input.md",
                        "version": "fixture",
                        "facts": "Local confirmed Atlas input; not external research.",
                        "license": "unknown",
                        "reuse": "uncertain",
                    },
                )
            return {
                "sources": sources,
                "summary": "Fixture category research; not live evidence.",
                "gaps": ["Sources not fetched by this fake CLI."],
            }
        if stage.startswith("blueprint-generate-research-repair"):
            if self.fail_research_repair:
                return {"remove_source_indexes": []}
            supplied = json.loads((directory / "source/PRIOR_RESEARCH.json").read_text())
            assert json.loads((directory / "source/VALIDATION_ERROR.json").read_text())
            return {
                "remove_source_indexes": [
                    i for i, row in enumerate(supplied["sources"])
                    if row.get("id") == "S01"
                ]
            }
        if stage.startswith("blueprint-spec-review"):
            files = sorted(
                path.relative_to(directory / "source").as_posix()
                for path in (directory / "source").rglob("*")
                if path.is_file()
            )
            self.design_sources.append(files)
            supplied = json.loads((directory / "input.json").read_text())
            assert files == supplied["source_inventory"]
            self.design_requests.append(supplied)
            dimensions = supplied.get("review_dimensions", list(DESIGN_DIMENSIONS))
            if self.fail_design_dimension_once == dimensions[0]:
                self.fail_design_dimension_once = None
                raise FactoryError(
                    "synthetic dimension failure", "cli_output_truncated", 409
                )
            block_dimension = self.design_block_dimension or DESIGN_DIMENSIONS[0]
            block = self.design_blocks and dimensions[0] == block_dimension
            outcome = "blocked" if block else self.design_outcome
            if block:
                self.design_blocks -= 1
            return {
                "summary": "Fixture specification review only; no runtime evidence.",
                "checks": [
                    {
                        "dimension": dimension,
                        "outcome": outcome if i == 0 else "passed",
                        "files": ["DRAFT.md"],
                        "reason": "Fixture design finding, not a real model assessment.",
                    }
                    for i, dimension in enumerate(dimensions)
                ],
                "suggestions": [
                    "Close the declared user journey before authoring programs."
                ],
            }
        if stage.startswith("blueprint-generate"):
            if self.on_generate:
                self.on_generate()
            if self.fail_generation:
                raise FactoryError("synthetic CLI failure")
            supplied = json.loads((directory / "input.json").read_text())
            if supplied.get("repair_mode") == "exact-spec-patch":
                source_files = sorted(
                    path.relative_to(directory / "source").as_posix()
                    for path in (directory / "source").rglob("*")
                    if path.is_file()
                )
                assert source_files == supplied["source_inventory"]
                self.spec_repair_requests.append(
                    {"source_inventory": source_files, "input": supplied}
                )
                current = json.loads(
                    (directory / "source/SPECIFICATION.json").read_text()
                )["spec"]
                if current["features"][0]["sources"] == ["missing"]:
                    return {
                        "spec_changes": [
                            {
                                "path": [
                                    "features",
                                    current["features"][0]["id"],
                                    "sources",
                                ],
                                "old": ["missing"],
                                "new": fixture["features"][0]["sources"],
                            }
                        ]
                    }
                return {
                    "spec_changes": [
                        {
                            "path": ["title"],
                            "old": current["title"],
                            "new": current["title"] + " revised",
                        }
                    ]
                }
            spec = {
                key: deepcopy(fixture[key])
                for key in [
                    "title",
                    "roles",
                    "features",
                    "decisions",
                    "phases",
                    "acceptance",
                    "architecture_markdown",
                    "limits",
                ]
            }
            if self.bad_structure_once:
                spec["features"][0]["sources"] = ["missing"]
                self.bad_structure_once = False
            # Even unsupported author claims must not become execution facts.
            for case in spec["acceptance"]:
                case["status"] = "passed"
            for phase in spec["phases"]:
                phase["status"] = "implemented"
            files = {
                p.relative_to(self.source).as_posix(): p.read_text()
                for base in ["acceptance", "references"]
                for p in (self.source / base).rglob("*")
                if p.is_file()
                and p.name != "plan.json"
                and "__pycache__" not in p.parts
            }
            return {
                "spec": spec,
                "file_plan": [
                    {
                        "path": name,
                        "purpose": "Fixture program " + name,
                        "reuse": self.reuse_files,
                    }
                    for name in files
                ],
            }
        if stage.startswith("blueprint-code"):
            if self.fail_file_once and stage.endswith("-1"):
                self.fail_file_once = False
                raise FactoryError("synthetic single-file failure")
            value = json.loads((directory / "input.json").read_text())
            name = value["file"]["path"]
            if self.bad_patch_count:
                self.bad_patch_count -= 1
                return {
                    "path": name,
                    "replacements": [
                        {"old": "absent pinned content", "new": "corrected"}
                    ],
                }
            if self.bad_manifest_once and name == "acceptance/package.json":
                self.bad_manifest_once = False
                self.bad_manifest_stage = stage
                return {"path": name, "content": '{"name":"broken"\n"private":true}'}
            return {"path": name, "content": (self.source / name).read_text()}
        if stage == "cognitive-review-reference-repair":
            value = json.loads((directory / "source/ORIGINAL_REVIEW.json").read_text())
            supplied = json.loads((directory / "input.json").read_text())
            assert isinstance(supplied["source_inventory"], list)
            if self.review_repair_response is not None:
                return self.review_repair_response
            return {
                "remove_file_indexes": [
                    {
                        "dimension": row["dimension"],
                        "indexes": [
                            i for i, path in enumerate(row["files"])
                            if path not in supplied["source_inventory"]
                        ],
                    }
                    for row in value["checks"]
                    if any(path not in supplied["source_inventory"] for path in row["files"])
                ]
            }
        if stage == "cognitive-review":
            return {
                "outcome": "passed",
                "summary": "Fake reviewer contract fixture; no model or runtime verification.",
                "checks": [
                    {
                        "dimension": dimension,
                        "outcome": self.review_outcome if i == 0 else "passed",
                        "files": (
                            [self.review_invalid_path, "PRODUCT.md"]
                            if i == 0 and self.review_invalid_path
                            else ["PRODUCT.md"]
                        ),
                        "reason": "Fixture content reference; not a real semantic review.",
                    }
                    for i, dimension in enumerate(DIMENSIONS)
                ],
                "suggestions": ["Fixture suggestion"],
            }
        raise AssertionError("unexpected CLI stage " + stage)


class CognitionTests(unittest.TestCase):
    setUp = blueprint_fixtures.BlueprintTests.setUp

    def test_missing_or_reserved_spec_fields_rejected_before_program_authoring(self):
        fixture = json.loads((self.source / "template.json").read_text())
        keys = (
            "title",
            "roles",
            "features",
            "decisions",
            "phases",
            "acceptance",
            "architecture_markdown",
            "limits",
        )
        spec = {key: fixture[key] for key in keys}
        proposal = {
            "spec": spec,
            "file_plan": [{"path": "acceptance/README.md", "purpose": "Setup"}],
        }
        validate_file_plan(proposal)
        for invalid in [
            {k: v for k, v in spec.items() if k != "limits"},
            {**spec, "evidence": []},
        ]:
            with (
                self.subTest(fields=list(invalid)),
                self.assertRaisesRegex(FactoryError, "authored fields"),
            ):
                validate_file_plan({**proposal, "spec": invalid})

    tearDown = blueprint_fixtures.BlueprintTests.tearDown
    data = blueprint_fixtures.BlueprintTests.data

    def test_review_source_prefix_maps_only_to_an_existing_exact_file(self):
        report = {
            "summary": "Scoped static review, no execution.",
            "checks": [
                {
                    "dimension": "architecture_contract",
                    "outcome": "passed",
                    "files": ["source/ARCHITECTURE.md"],
                    "reason": "Concrete contract in the supplied architecture.",
                }
            ],
        }
        clean = validate_review(report, self.source, ("architecture_contract",))
        self.assertEqual(clean["checks"][0]["files"], ["ARCHITECTURE.md"])
        self.assertEqual(
            clean["citation_aliases"],
            [{"reported": "source/ARCHITECTURE.md", "canonical": "ARCHITECTURE.md"}],
        )
        self.assertEqual(report["checks"][0]["files"], ["source/ARCHITECTURE.md"])
        for path in (
            "source/absent.md",
            "source/source/ARCHITECTURE.md",
            "source/../ARCHITECTURE.md",
            "/ARCHITECTURE.md",
        ):
            invalid = deepcopy(report)
            invalid["checks"][0]["files"] = [path]
            with self.subTest(path=path), self.assertRaises(FactoryError):
                validate_review(invalid, self.source, ("architecture_contract",))

    def test_spec_delta_preserves_unaddressed_contracts_rows_and_original(self):
        plan = {
            "spec": {
                "title": "sample",
                "architecture_markdown": "before\nwrong contract\nafter",
                "decisions": [{"id": "D01", "default": "old", "question": "retained"}],
                "features": [{"id": "F01", "name": "keep"}],
            },
            "file_plan": [
                {"path": "acceptance/a.cjs", "purpose": "same interface", "reuse": True}
            ],
        }
        original = deepcopy(plan)
        revised = apply_spec_revision(
            plan,
            {
                "spec_changes": [
                    {
                        "path": ["architecture_markdown"],
                        "replacements": [
                            {"old": "wrong contract", "new": "correct contract"}
                        ],
                    },
                    {
                        "path": ["decisions", "D01", "default"],
                        "old": "old",
                        "new": "corrected",
                    },
                ],
                "file_plan_changes": [{"path": "acceptance/a.cjs", "reuse": False}],
            },
        )
        self.assertEqual(plan, original)
        self.assertEqual(
            revised["spec"]["architecture_markdown"], "before\ncorrect contract\nafter"
        )
        self.assertEqual(revised["spec"]["features"], original["spec"]["features"])
        self.assertEqual(
            revised["spec"]["decisions"][0],
            {"id": "D01", "default": "corrected", "question": "retained"},
        )
        self.assertEqual(
            revised["file_plan"],
            [{"path": "acceptance/a.cjs", "purpose": "same interface", "reuse": False}],
        )

    def test_spec_delta_rejects_identity_evidence_inventory_and_fuzzy_edits(self):
        plan = {
            "spec": {
                "title": "sample",
                "architecture_markdown": "twice twice",
                "decisions": [{"id": "D01", "default": "old", "status": "proposed"}],
            },
            "file_plan": [{"path": "acceptance/a.cjs", "purpose": "keep"}],
        }
        good = {"path": ["title"], "old": "sample", "new": "corrected"}
        invalid = [
            {"spec": plan["spec"]},
            {"spec_changes": [good], "evidence": "invented"},
            {"spec_changes": [{"path": ["schema"], "old": "x", "new": "y"}]},
            {
                "spec_changes": [
                    {"path": ["decisions", "D01", "id"], "old": "D01", "new": "D02"}
                ]
            },
            {
                "spec_changes": [
                    {
                        "path": ["decisions", "D01", "status"],
                        "old": "proposed",
                        "new": "confirmed",
                    }
                ]
            },
            {
                "spec_changes": [
                    {
                        "path": ["decisions", "D02", "default"],
                        "old": "old",
                        "new": "new",
                    }
                ]
            },
            {"spec_changes": [{"path": ["title"], "old": "absent", "new": "new"}]},
            {"spec_changes": [good, good]},
            {
                "spec_changes": [
                    {
                        "path": ["architecture_markdown"],
                        "replacements": [{"old": "twice", "new": "one"}],
                    }
                ]
            },
            {
                "spec_changes": [
                    {
                        "path": ["architecture_markdown"],
                        "old": "twice twice",
                        "new": "full rewrite",
                    }
                ]
            },
            {
                "spec_changes": [good],
                "file_plan_changes": [
                    {"path": "acceptance/new.cjs", "purpose": "invented"}
                ],
            },
        ]
        for response in invalid:
            with self.subTest(response=response), self.assertRaises(FactoryError):
                apply_spec_revision(plan, response)

    def test_addressed_field_replace_requires_exact_proposal_version(self):
        from template_factory.store import digest

        plan = {
            "spec": {
                "architecture_markdown": "retain other paragraphs",
                "decisions": [
                    {
                        "id": "D01",
                        "default": "long original value",
                        "status": "proposed",
                        "impact": "retained",
                    }
                ],
            },
            "file_plan": [],
        }
        response = {
            "base_proposal_digest": digest(plan),
            "spec_changes": [
                {"path": ["decisions", "D01", "default"], "new": "corrected"}
            ],
        }
        changed = apply_spec_revision(plan, response)
        self.assertEqual(
            changed["spec"]["decisions"][0],
            {
                "id": "D01",
                "default": "corrected",
                "status": "proposed",
                "impact": "retained",
            },
        )
        self.assertEqual(plan["spec"]["decisions"][0]["default"], "long original value")
        for invalid in (
            {"spec_changes": response["spec_changes"]},
            {**response, "base_proposal_digest": "wrong"},
            {
                **response,
                "spec_changes": [
                    {"path": ["architecture_markdown"], "new": "full rewrite"}
                ],
            },
            {
                **response,
                "spec_changes": [
                    {"path": ["decisions", "D01", "status"], "new": "confirmed"}
                ],
            },
            {
                **response,
                "spec_changes": [
                    {"path": ["decisions", "D02", "default"], "new": "invented"}
                ],
            },
        ):
            with self.subTest(response=invalid), self.assertRaises(FactoryError):
                apply_spec_revision(plan, invalid)

    def test_research_context_keeps_full_long_prose_readable(self):
        prose = "真实调研结论与未知项" * 1000
        research = {
            "summary": prose,
            "sources": [{"id": "S02", "facts": prose}],
            "gaps": ["全文没有获取；不能宣称已核实。"],
        }
        rendered = research_context(research)
        self.assertLess(max(map(len, rendered.splitlines())), 2000)
        self.assertEqual(rendered.replace("\n", "").count("真实调研结论与未知项"), 2000)
        self.assertIn("全文没有获取", rendered)

    def scenario(self):
        value = json.loads((self.source / "inputs/scenario.json").read_text())
        return self.store.save_scenario(value)

    def batch(self, scene=None, **overrides):
        scene = scene or self.scenario()
        return self.store.create_batch(
            {
                "kind": "blueprint-production",
                "name": "Cognition fixture",
                "model": "fake/flash",
                "language": "en",
                "scenario_ids": [scene["id"]],
                "scenario_revisions": {scene["id"]: scene["revision"]},
                **overrides,
            }
        )

    def pipeline(self):
        self.cli = FakeCognitionCLI(self.source)
        return Pipeline(self.store, cli=self.cli)

    def produce(self):
        batch = self.batch()
        pipeline = self.pipeline()
        pipeline.run(self.store.claim("test", "production"))
        return batch, pipeline, self.store.artifacts()[0]

    def test_end_to_end_generation_freezes_then_independently_reviews_without_runtime(
        self,
    ):
        batch, pipeline, artifact = self.produce()
        self.assertEqual(
            [s for s in self.cli.calls if not s.startswith("blueprint-code")],
            ["blueprint-research", "blueprint-generate-0"]
            + [
                "blueprint-spec-review-0-" + dimension
                for dimension in DESIGN_DIMENSIONS
            ],
        )
        self.assertTrue(any(s.startswith("blueprint-code") for s in self.cli.calls))
        research_input = json.loads(
            (
                self.store.root
                / "jobs"
                / artifact["job_id"]
                / "attempt-1"
                / "blueprint-research/input.json"
            ).read_text()
        )
        self.assertRegex(research_input["research_date"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertEqual(artifact["artifact_type"], "product-blueprint")
        self.assertEqual(artifact["state"], "draft")
        self.assertEqual(artifact["level"], "L0")
        self.assertEqual(len(artifact["acceptance_jobs"]), 1)
        self.assertEqual(self.store.batch(batch["id"])["state"], "completed")
        review = self.store.claim("reviewer", "verification")
        self.assertEqual(review["kind"], "cognitive-review")
        self.assertEqual(review["snapshot"]["config"]["language"], "en")
        self.assertNotEqual(review["id"], artifact["job_id"])
        pipeline.run(review)
        latest = self.store.artifacts()[0]
        self.assertEqual(latest["acceptances"][0]["outcome"], "passed")
        self.assertEqual(latest["level"], "L0")
        self.assertIn("no program execution", latest["acceptances"][0]["scope"])
        candidate = self.store.root / artifact["bundle_path"] / "source"
        spec = json.loads((candidate / "template.json").read_text())
        self.assertEqual(spec["scenario"], self.store.scenario(spec["scenario"]["id"]))
        self.assertEqual(spec["evidence"], [])
        self.assertTrue(all(case["status"] == "not_run" for case in spec["acceptance"]))
        self.assertTrue(
            all(phase["status"] == "not implemented" for phase in spec["phases"])
        )
        self.assertIn("NOT been executed", (candidate / "VALIDATION.md").read_text())

    def test_runtime_enabled_production_authors_binding_and_revision_retains_protocol(self):
        fixture = json.loads((self.source / "template.json").read_text())
        (self.source / "acceptance/runner.json").write_text(json.dumps({
            "schema": "atlas.acceptance-runner.v1", "result_schema": "atlas.acceptance-result.v1",
            "cases": {row["id"]: {"args": ["--case", "{case_id}", "--base-url", "{base_url}"]} for row in fixture["acceptance"]},
        }))
        self.batch(acceptance_protocol="atlas.acceptance-runner.v1")
        pipeline = self.pipeline()
        job = self.store.claim("test", "production")
        pipeline.run(job)
        artifact = self.store.artifacts()[0]
        candidate = self.store.root / artifact["bundle_path"] / "source"
        self.assertTrue((candidate / "acceptance/runner.json").is_file())
        generation = self.store.root / "jobs" / job["id"] / "attempt-1/blueprint-generate-0"
        self.assertIn("atlas.acceptance-runner.v1", (generation / "source/FORMAT.md").read_text())
        revision = self.store.create_repair(artifact["id"], {
            "note": "Preserve all contracts and repair the acceptance adapter documentation.",
            "model": "fake/flash", "expected_digest": artifact["digest"],
        })
        self.assertEqual(revision["jobs"][0]["snapshot"]["config"]["acceptance_protocol"], "atlas.acceptance-runner.v1")

    def _configure_runtime_protocol(self):
        fixture = json.loads((self.source / "template.json").read_text())
        (self.source / "acceptance/runner.json").write_text(json.dumps({
            "schema": "atlas.acceptance-runner.v1",
            "result_schema": "atlas.acceptance-result.v1",
            "cases": {
                row["id"]: {
                    "args": ["--case", "{case_id}", "--base-url", "{base_url}"]
                }
                for row in fixture["acceptance"]
            },
        }))

    def test_runtime_protocol_block_repairs_spec_before_any_program_authoring(self):
        self._configure_runtime_protocol()
        self.batch(acceptance_protocol="atlas.acceptance-runner.v1")
        pipeline = self.pipeline()
        self.cli.design_blocks = 1
        self.cli.design_block_dimension = "runtime_protocol"
        pipeline.run(self.store.claim("test", "production"))
        runtime_stage = "blueprint-spec-review-0-runtime_protocol-v1"
        self.assertIn(runtime_stage, self.cli.calls)
        repair_stage = "blueprint-generate-1"
        self.assertIn(repair_stage, self.cli.calls)
        first_code = next(i for i, call in enumerate(self.cli.calls) if call.startswith("blueprint-code"))
        self.assertLess(self.cli.calls.index(runtime_stage), self.cli.calls.index(repair_stage))
        self.assertLess(self.cli.calls.index(repair_stage), first_code)
        self.assertEqual(self.cli.calls.count("blueprint-spec-review-1-runtime_protocol-v1"), 1)
        self.assertIn(
            "RUNTIME_PROTOCOL.md",
            self.cli.spec_repair_requests[0]["source_inventory"],
        )
        self.assertIn(
            "RUNTIME_CONTRACT.md",
            self.cli.spec_repair_requests[0]["source_inventory"],
        )
        attempt = self.store.root / "jobs" / self.store.artifacts()[0]["job_id"] / "attempt-1"
        repaired = json.loads((attempt / "blueprint-generate-1/result.json").read_text())
        self.assertEqual(set(repaired), {"spec_changes"})
        self.assertEqual(
            self.store.artifacts()[0]["provenance"]["spec_review"]["outcome"],
            "passed",
        )
        contract = attempt / "context/RUNTIME_CONTRACT.md"
        self.assertIn("never the application's database", contract.read_text())

    def test_legacy_five_dimension_aggregate_checkpoint_does_not_skip_runtime_review(self):
        self._configure_runtime_protocol()
        self.batch(acceptance_protocol="atlas.acceptance-runner.v1")
        pipeline = self.pipeline()
        job = self.store.claim("test", "production")
        legacy_report = {
            "outcome": "passed",
            "summary": "Legacy five-dimension aggregate.",
            "checks": [
                {
                    "dimension": dimension,
                    "outcome": "passed",
                    "files": ["DRAFT.md"],
                    "reason": "Earlier cached design review.",
                }
                for dimension in DESIGN_DIMENSIONS
            ],
            "suggestions": [],
            "proposal_digest": "legacy-pinned-proposal-digest",
            "subreviews": [],
        }
        self.store.checkpoint(
            job["id"],
            "blueprint-spec-review-0",
            {"result": legacy_report, "digest": digest(legacy_report)},
            job["token"],
        )
        pipeline.run(job)
        self.assertEqual(
            self.cli.calls.count("blueprint-spec-review-0-runtime_protocol-v1"), 1
        )
        self.assertIsNotNone(
            self.store.checkpoint(job["id"], "blueprint-spec-review-0-runtime-v1")
        )
        self.assertEqual(len(self.store.artifacts()), 1)

    def test_batch_rejects_draft_stale_and_active_duplicates(self):
        scene = self.scenario()
        with self.assertRaises(FactoryError):
            self.batch(scene, scenario_revisions={scene["id"]: 999})
        batch = self.batch(scene)
        with self.assertRaises(FactoryError):
            self.batch(scene)
        self.store.batch_action(batch["id"], "cancel")
        draft = self.store.save_scenario(
            {**scene, "status": "draft", "expected_revision": scene["revision"]},
            scene["id"],
        )
        with self.assertRaises(FactoryError):
            self.batch(draft)
        self.assertEqual(len(self.store.batches()), 1)

    def test_invalid_structure_is_repaired_with_actual_failed_proposal(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.bad_structure_once = True
        pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(
            [s for s in self.cli.calls if not s.startswith("blueprint-code")],
            [
                "blueprint-research",
                "blueprint-generate-0",
            ]
            + ["blueprint-spec-review-0-" + d for d in DESIGN_DIMENSIONS]
            + ["blueprint-generate-1"]
            + ["blueprint-spec-review-1-" + d for d in DESIGN_DIMENSIONS],
        )
        artifact = self.store.artifacts()[0]
        self.assertEqual(artifact["manifest"]["feature_count"], 18)
        attempts = list(
            (self.store.root / "jobs" / artifact["job_id"]).glob(
                "attempt-*/blueprint-generate-1/source/SPECIFICATION.json"
            )
        )
        self.assertEqual(len(attempts), 1)
        self.assertIn("missing", attempts[0].read_text())

    def test_failed_generation_retry_reuses_immutable_research_checkpoint(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.fail_generation = True
        job = self.store.claim("test", "production")
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        self.assertEqual(self.store.job(job["id"])["state"], "failed")
        self.cli.fail_generation = False
        self.store.retry(job["id"])
        pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(self.cli.calls.count("blueprint-research"), 1)
        self.assertEqual(self.cli.calls.count("blueprint-generate-research-repair-0"), 0)
        self.assertIsNotNone(
            self.store.checkpoint(job["id"], "blueprint-research-response")
        )
        self.assertEqual(len(self.store.artifacts()), 1)

    def test_legacy_normalized_research_checkpoint_survives_generation_retry(self):
        self.batch()
        pipeline = self.pipeline()
        fixture = json.loads((self.source / "template.json").read_text())
        normalized = validate_research(
            {
                "sources": fixture["sources"][1:],
                "summary": "Fixture category research; not live evidence.",
                "gaps": ["Sources not fetched by this fake CLI."],
            }
        )
        job = self.store.claim("test", "production")
        self.store.checkpoint(
            job["id"],
            "blueprint-research",
            {"result": normalized, "digest": digest(normalized)},
            job["token"],
        )
        self.cli.fail_generation = True
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        self.assertEqual(self.cli.calls.count("blueprint-research"), 0)
        self.assertIsNone(
            self.store.checkpoint(job["id"], "blueprint-research-response")
        )
        self.cli.fail_generation = False
        self.store.retry(job["id"])
        pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(self.cli.calls.count("blueprint-research"), 0)
        self.assertEqual(len(self.store.artifacts()), 1)

    def test_rejected_reserved_non_https_source_is_removed_by_bounded_protocol_repair(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.research_with_reserved_source = True
        job = self.store.claim("test", "production")
        pipeline.run(job)
        self.assertEqual(self.cli.calls.count("blueprint-research"), 1)
        self.assertEqual(
            self.cli.calls.count("blueprint-generate-research-repair-0"), 1
        )
        raw = self.store.checkpoint(job["id"], "blueprint-research-response")
        self.assertEqual(raw["result"]["sources"][0]["id"], "S01")
        self.assertEqual(
            self.store.checkpoint(job["id"], "blueprint-research-validation-error")[
                "result"
            ]["message"],
            "research needs unique source IDs and HTTPS primary URLs",
        )
        repaired = self.store.checkpoint(
            job["id"], "blueprint-research-protocol-repair-0"
        )
        self.assertEqual(repaired["result"], {"remove_source_indexes": [0]})
        self.assertEqual(len(self.store.artifacts()), 1)

    def test_research_protocol_repair_failure_stops_without_publishing(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.research_with_reserved_source = True
        self.cli.fail_research_repair = True
        job = self.store.claim("test", "production")
        with self.assertRaisesRegex(FactoryError, "must remove only protocol-invalid"):
            pipeline.run(job)
        self.assertEqual(self.store.artifacts(), [])
        self.assertIsNotNone(
            self.store.checkpoint(job["id"], "blueprint-research-response")
        )
        self.assertIsNotNone(
            self.store.checkpoint(job["id"], "blueprint-research-protocol-repair-0")
        )

    def test_single_file_failure_reuses_plan_and_completed_programs(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.fail_file_once = True
        job = self.store.claim("test", "production")
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        self.assertEqual(self.store.artifacts(), [])
        self.store.retry(job["id"])
        pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(self.cli.calls.count("blueprint-research"), 1)
        self.assertEqual(self.cli.calls.count("blueprint-generate-0"), 1)
        self.assertEqual(self.cli.calls.count("blueprint-code-0-0"), 1)
        self.assertEqual(self.cli.calls.count("blueprint-code-0-1"), 2)
        self.assertEqual(len(self.store.artifacts()), 1)

    def test_invalid_dependency_manifest_repairs_only_that_file_and_keeps_original(
        self,
    ):
        self.batch()
        pipeline = self.pipeline()
        self.cli.bad_manifest_once = True
        job = self.store.claim("test", "production")
        pipeline.run(job)
        artifact = self.store.artifacts()[0]
        base = self.store.checkpoint(job["id"], self.cli.bad_manifest_stage)
        self.assertIn('"broken"', base["result"]["content"])
        fixed = self.store.checkpoint(
            job["id"], self.cli.bad_manifest_stage + "-repair-0"
        )
        self.assertIsInstance(json.loads(fixed["result"]["content"]), dict)
        self.assertEqual(self.cli.calls.count("blueprint-research"), 1)
        self.assertEqual(self.cli.calls.count("blueprint-generate-0"), 1)
        self.assertEqual(len([c for c in self.cli.calls if "-repair-" in c]), 1)
        self.assertIsInstance(
            json.loads(
                (
                    self.store.root
                    / artifact["bundle_path"]
                    / "source/acceptance/package.json"
                ).read_text()
            ),
            dict,
        )

    def test_cancelled_production_cannot_register_or_queue_review(self):
        batch = self.batch()
        pipeline = self.pipeline()
        self.cli.on_generate = lambda: self.store.batch_action(batch["id"], "cancel")
        with self.assertRaises(FactoryError):
            pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(self.store.artifacts(), [])
        self.assertIsNone(self.store.claim("reviewer", "verification"))

    def test_cancellation_between_freeze_and_auto_queue_prevents_new_call(self):
        batch = self.batch()
        pipeline = self.pipeline()
        original = self.store.add_artifact

        def freeze_and_cancel(*args):
            value = original(*args)
            self.store.batch_action(batch["id"], "cancel")
            return value

        with patch.object(self.store, "add_artifact", side_effect=freeze_and_cancel):
            pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(len(self.store.artifacts()), 1)
        self.assertEqual(self.store.artifacts()[0]["acceptance_jobs"], [])

    def test_blocked_uncertain_and_unavailable_reviews_never_mark_passed(self):
        for outcome in ["blocked", "uncertain"]:
            with self.subTest(outcome=outcome):
                batch, pipeline, artifact = self.produce()
                self.cli.review_outcome = outcome
                pipeline.run(self.store.claim("reviewer", "verification"))
                current = next(
                    a for a in self.store.artifacts() if a["id"] == artifact["id"]
                )
                self.assertEqual(current["acceptances"][0]["outcome"], outcome)
                self.assertEqual(current["level"], "L0")
                self.assertEqual(
                    self.cli.calls.count("cognitive-review-reference-repair"), 0
                )
        artifact = import_blueprint(self.store, self.data())
        self.store.create_acceptance(
            artifact["id"],
            {
                "method": "cognitive-review",
                "model": "fake/flash",
                "expected_digest": artifact["digest"],
            },
        )
        pipeline = self.pipeline()

        def failure(*args):
            raise FactoryError("synthetic provider unavailable")

        self.cli.run = failure
        with self.assertRaises(FactoryError):
            pipeline.run(self.store.claim("reviewer", "verification"))
        current = next(a for a in self.store.artifacts() if a["id"] == artifact["id"])
        self.assertEqual(current["acceptances"][0]["outcome"], "unavailable")

    def test_revision_pins_prior_scenario_and_preserves_original_with_no_new_research(
        self,
    ):
        _, pipeline, original = self.produce()
        pipeline.run(self.store.claim("reviewer", "verification"))
        batch = self.store.create_repair(
            original["id"],
            {
                "note": "有依据的修订要求" * 1000 + "最终约束不弱化验收",
                "model": "fake/flash",
                "expected_digest": original["digest"],
                "language": "en",
            },
        )
        job = self.store.claim("test", "production")
        self.assertEqual(job["batch_id"], batch["id"])
        self.assertEqual(
            job["snapshot"]["scenario"]["revision"], original["scenario_revision"]
        )
        self.cli.reuse_files = True
        code_calls = len([v for v in self.cli.calls if v.startswith("blueprint-code")])
        pipeline.run(job)
        revision = next(a for a in self.store.artifacts() if a["id"] != original["id"])
        self.assertEqual(revision["supersedes"], original["id"])
        self.assertEqual(self.cli.calls.count("blueprint-research"), 1)
        self.assertTrue((self.store.root / original["bundle_path"]).exists())
        self.assertNotEqual(original["digest"], revision["digest"])
        self.assertEqual(revision["manifest"]["version"], "0.1.1")
        revised_source = self.store.root / revision["bundle_path"] / "source"
        revised_spec = json.loads((revised_source / "template.json").read_text())
        original_source = self.store.root / original["bundle_path"] / "source"
        original_spec = json.loads((original_source / "template.json").read_text())
        self.assertEqual(revised_spec["research"], original_spec["research"])
        self.assertEqual(
            (revised_source / "CATEGORY.md").read_text().count("## S02"), 1
        )
        companion = (
            self.store.root
            / "jobs"
            / job["id"]
            / "attempt-1/blueprint-generate-0/source/REVISION.md"
        )
        self.assertIn("最终约束不弱化验收", companion.read_text().replace("\n", ""))
        self.assertLess(max(map(len, companion.read_text().splitlines())), 2000)
        self.assertEqual(
            len([v for v in self.cli.calls if v.startswith("blueprint-code")]),
            code_calls,
        )

    def test_legacy_revision_uses_original_structured_checkpoint_and_rejects_tampering(
        self,
    ):
        _, _, artifact = self.produce()
        bundle = self.store.root / artifact["bundle_path"]
        spec = json.loads((bundle / "source/template.json").read_text())
        expected = spec.pop("research")
        self.assertEqual(pinned_research(self.store, artifact, bundle, spec), expected)
        checkpoint = self.store.checkpoint(artifact["job_id"], "blueprint-research")
        checkpoint["result"]["gaps"] = ["altered"]
        with patch.object(self.store, "checkpoint", return_value=checkpoint):
            with self.assertRaises(FactoryError):
                pinned_research(self.store, artifact, bundle, spec)

    def test_exact_file_patch_preserves_prior_and_rejects_ambiguous_edits(self):
        prior = self.store.root / "prior"
        (prior / "acceptance").mkdir(parents=True)
        target = prior / "acceptance/test.cjs"
        target.write_bytes(b"keep\r\nunique\r\nkeep\r\n")
        patched = apply_file_response(
            {
                "path": "acceptance/test.cjs",
                "replacements": [{"old": "unique", "new": "corrected"}],
            },
            "acceptance/test.cjs",
            prior,
        )
        self.assertEqual(patched["content"], "keep\r\ncorrected\r\nkeep\r\n")
        self.assertEqual(target.read_bytes(), b"keep\r\nunique\r\nkeep\r\n")
        for old in ("keep", "missing"):
            with self.assertRaises(FactoryError):
                apply_file_response(
                    {
                        "path": "acceptance/test.cjs",
                        "replacements": [{"old": old, "new": "changed"}],
                    },
                    "acceptance/test.cjs",
                    prior,
                )
        with self.assertRaises(FactoryError):
            apply_file_response(
                {"path": "elsewhere.cjs", "content": "bad"},
                "acceptance/test.cjs",
                prior,
            )

    def test_bad_patch_repairs_only_failed_file_with_bounded_feedback(self):
        _, pipeline, artifact = self.produce()
        self.store.create_repair(
            artifact["id"],
            {
                "note": "Fix the actual pinned program without weakening behavior assertions.",
                "model": "fake/flash",
                "expected_digest": artifact["digest"],
            },
        )
        self.cli.bad_patch_count = 1
        job = self.store.claim("test", "production")
        pipeline.run(job)
        calls = [v for v in self.cli.calls if "-patch-repair-" in v]
        self.assertEqual(len(calls), 1)
        call = next(
            (self.store.root / "jobs" / job["id"]).glob(
                "attempt-*/" + calls[0] + "/input.json"
            )
        )
        self.assertIn("matches 0", json.loads(call.read_text())["failure_evidence"][0])
        self.assertEqual(len(self.store.artifacts()), 2)

        revision = self.store.artifacts()[0]
        self.store.create_repair(
            revision["id"],
            {
                "note": "Retain failed candidates; do not retry endlessly or apply fuzzy patches.",
                "model": "fake/flash",
                "expected_digest": revision["digest"],
            },
        )
        self.cli.bad_patch_count = 2
        job = self.store.claim("test", "production")
        before = len(self.cli.calls)
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        self.assertEqual(
            len([v for v in self.cli.calls[before:] if v.startswith("blueprint-code")]),
            2,
        )
        self.assertEqual(len(self.store.artifacts()), 2)

    def test_scoped_revision_copies_unselected_files_even_when_author_ignores_reuse(
        self,
    ):
        _, pipeline, artifact = self.produce()
        for paths in (
            [],
            ["../outside"],
            ["AGENT.md"],
            ["acceptance/plan.json"],
            ["acceptance/missing.cjs"],
            ["acceptance/README.md"] * 2,
        ):
            with self.subTest(paths=paths), self.assertRaises(FactoryError):
                self.store.create_repair(
                    artifact["id"],
                    {
                        "note": "Only revise the declared paths.",
                        "model": "fake/flash",
                        "expected_digest": artifact["digest"],
                        "edit_paths": paths,
                    },
                )
        self.store.create_repair(
            artifact["id"],
            {
                "note": "Only revise the acceptance guide; preserve pinned programs byte for byte.",
                "model": "fake/flash",
                "expected_digest": artifact["digest"],
                "edit_paths": ["acceptance/README.md"],
            },
        )
        before = len(self.cli.calls)
        job = self.store.claim("test", "production")
        pipeline.run(job)
        self.assertEqual(
            len([v for v in self.cli.calls[before:] if v.startswith("blueprint-code")]),
            1,
        )
        raw = self.store.checkpoint(job["id"], "blueprint-plan-0")["result"][
            "file_plan"
        ]
        self.assertTrue(all(not row.get("reuse") for row in raw))
        revision = self.store.artifacts()[0]
        self.assertEqual(revision["provenance"]["edit_paths"], ["acceptance/README.md"])
        old = self.store.root / artifact["bundle_path"] / "source"
        new = self.store.root / revision["bundle_path"] / "source"
        for row in raw:
            if row["path"] != "acceptance/README.md":
                self.assertEqual(
                    (old / row["path"]).read_bytes(), (new / row["path"]).read_bytes()
                )
        with self.assertRaises(FactoryError):
            scoped_file_plan(raw[:-1], old, ["acceptance/README.md"])

    def test_review_rejects_coverage_holes_bad_references_and_derives_outcome(self):
        self.cli = FakeCognitionCLI(self.source)
        result = self.cli.run(Path("cognitive-review"), "", "", 0, None, None)
        self.assertEqual(validate_review(result, self.source)["outcome"], "passed")
        blocked = deepcopy(result)
        blocked["checks"][0]["outcome"] = "blocked"
        self.assertEqual(validate_review(blocked, self.source)["outcome"], "blocked")
        for mutate in [
            lambda r: r["checks"].pop(),
            lambda r: r["checks"].append(r["checks"][0]),
            lambda r: r["checks"][0].update(files=["../escape"]),
            lambda r: r["checks"][0].update(files=["absent.md"]),
        ]:
            value = deepcopy(result)
            mutate(value)
            with self.assertRaises(FactoryError):
                validate_review(value, self.source)

    def test_review_reference_repair_only_removes_invalid_indexes_and_preserves_judgments(self):
        result = FakeCognitionCLI(self.source).run(
            Path("cognitive-review"), "", "", 0, None, None
        )
        for outcome in ("blocked", "uncertain"):
            original = deepcopy(result)
            original["summary"] = "Preserve this original summary."
            original["checks"][0]["outcome"] = outcome
            original["checks"][0]["reason"] = "Preserve this original reason."
            original["checks"][0]["files"] = ["leaf.md", "PRODUCT.md"]
            repaired = apply_review_reference_repair(
                original,
                {
                    "remove_file_indexes": [
                        {"dimension": DIMENSIONS[0], "indexes": [0]}
                    ]
                },
                self.source,
            )
            report = validate_review(repaired, self.source)
            self.assertEqual(report["summary"], original["summary"])
            self.assertEqual(report["outcome"], outcome)
            self.assertEqual(report["checks"][0]["outcome"], outcome)
            self.assertEqual(report["checks"][0]["reason"], original["checks"][0]["reason"])
            self.assertEqual(report["checks"][0]["files"], ["PRODUCT.md"])
            self.assertEqual(repaired["suggestions"], original["suggestions"])

    def test_review_reference_repair_rejects_all_invalid_bad_indexes_valid_deletion_and_verdict_edit(self):
        original = FakeCognitionCLI(self.source).run(
            Path("cognitive-review"), "", "", 0, None, None
        )
        original["checks"][0]["files"] = ["leaf.md", "PRODUCT.md"]
        invalid_responses = [
            {"remove_file_indexes": [{"dimension": DIMENSIONS[0], "indexes": [2]}]},
            {"remove_file_indexes": [{"dimension": DIMENSIONS[0], "indexes": [0, 0]}]},
            {"remove_file_indexes": [{"dimension": DIMENSIONS[0], "indexes": [1]}]},
            {
                "remove_file_indexes": [{"dimension": DIMENSIONS[0], "indexes": [0]}],
                "outcome": "passed",
            },
        ]
        for response in invalid_responses:
            with self.subTest(response=response), self.assertRaises(FactoryError):
                apply_review_reference_repair(original, response, self.source)
        all_invalid = deepcopy(original)
        all_invalid["checks"][0]["files"] = ["leaf.md"]
        with self.assertRaisesRegex(FactoryError, "retain a valid source citation"):
            apply_review_reference_repair(
                all_invalid,
                {"remove_file_indexes": [{"dimension": DIMENSIONS[0], "indexes": [0]}]},
                self.source,
            )

    def test_review_with_one_invalid_citation_repairs_once_and_retains_original_response(self):
        _, pipeline, artifact = self.produce()
        self.cli.review_outcome = "blocked"
        self.cli.review_invalid_path = "leaf.md"
        job = self.store.claim("reviewer", "verification")
        pipeline.run(job)
        self.assertEqual(self.cli.calls.count("cognitive-review"), 1)
        self.assertEqual(self.cli.calls.count("cognitive-review-reference-repair"), 1)
        attempt = self.store.root / "jobs" / job["id"] / "attempt-1"
        original = json.loads((attempt / "cognitive-review/result.json").read_text())
        saved_original = json.loads(
            (attempt / "cognitive-review/original-result.json").read_text()
        )
        self.assertEqual(original, saved_original)
        self.assertIn("leaf.md", original["checks"][0]["files"])
        repair = json.loads(
            (attempt / "cognitive-review-reference-repair/result.json").read_text()
        )
        self.assertEqual(
            repair["remove_file_indexes"],
            [{"dimension": DIMENSIONS[0], "indexes": [0]}],
        )
        receipt = json.loads(
            (attempt / "cognitive-review/reference-repair-receipt.json").read_text()
        )
        self.assertEqual(receipt["removed_invalid_citations"][0]["paths"], ["leaf.md"])
        report = json.loads(
            (attempt / "cognitive-review/report.json").read_text()
        )
        self.assertEqual(report["outcome"], "blocked")
        self.assertEqual(report["checks"][0]["outcome"], "blocked")
        self.assertIn("Only file citations", report["protocol_note"])
        current = next(a for a in self.store.artifacts() if a["id"] == artifact["id"])
        self.assertEqual(current["acceptances"][0]["outcome"], "blocked")

    def test_program_only_revision_keeps_spec_and_skips_model_planning(self):
        _, pipeline, artifact = self.produce()
        with self.assertRaises(FactoryError):
            self.store.create_repair(
                artifact["id"],
                {
                    "note": "Only repair the actual acceptance program.",
                    "model": "fake/flash",
                    "expected_digest": artifact["digest"],
                    "reuse_spec": True,
                },
            )
        self.store.create_repair(
            artifact["id"],
            {
                "note": "The requirement is unchanged; repair only the acceptance guide.",
                "model": "fake/flash",
                "expected_digest": artifact["digest"],
                "reuse_spec": True,
                "edit_paths": ["acceptance/README.md"],
            },
        )
        before = len(self.cli.calls)
        pipeline.run(self.store.claim("test", "production"))
        self.assertEqual(len(self.cli.calls[before:]), 1)
        self.assertTrue(self.cli.calls[-1].startswith("blueprint-code"))
        revision = self.store.artifacts()[0]
        self.assertTrue(revision["provenance"]["reuse_spec"])
        old = json.loads(
            (
                self.store.root / artifact["bundle_path"] / "source/template.json"
            ).read_text()
        )
        new = json.loads(
            (
                self.store.root / revision["bundle_path"] / "source/template.json"
            ).read_text()
        )
        for key in (
            "title",
            "roles",
            "features",
            "decisions",
            "phases",
            "acceptance",
            "architecture_markdown",
            "limits",
            "research",
        ):
            self.assertEqual(old[key], new[key])

    def test_design_review_blocks_before_any_program_and_exposes_findings(self):
        self.batch(cognition_guidance="必须把单条删除与恢复的用户流程说清楚。")
        pipeline = self.pipeline()
        self.cli.design_blocks = 2
        job = self.store.claim("test", "production")
        with self.assertRaises(FactoryError) as error:
            pipeline.run(job)
        self.assertEqual(error.exception.code, "cognition_design_blocked")
        self.assertFalse(any(s.startswith("blueprint-code") for s in self.cli.calls))
        self.assertEqual(self.store.artifacts(), [])
        reports = self.store.job(job["id"])["design_reviews"]
        self.assertEqual([r["outcome"] for r in reports], ["blocked", "blocked"])
        self.assertTrue(all(r["proposal_digest"] for r in reports))
        context = self.store.root / "jobs" / job["id"] / "attempt-1/context"
        self.assertIn("单条删除", (context / "GUIDANCE.md").read_text())
        self.assertIn(
            "Close the declared user journey",
            (context / "DESIGN_FEEDBACK.md").read_text(),
        )

    def test_design_uncertainty_is_retained_without_becoming_an_automatic_block(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.design_outcome = "uncertain"
        pipeline.run(self.store.claim("test", "production"))
        artifact = self.store.artifacts()[0]
        self.assertEqual(artifact["provenance"]["spec_review"]["outcome"], "uncertain")
        self.assertEqual(artifact["level"], "L0")
        self.assertEqual(artifact["acceptances"], [])
        self.assertEqual(len(artifact["acceptance_jobs"]), 1)

    def test_design_feedback_repairs_spec_once_then_authors_programs(self):
        self.batch()
        pipeline = self.pipeline()
        self.cli.design_blocks = 1
        job = self.store.claim("test", "production")
        pipeline.run(job)
        first_code = next(
            i
            for i, name in enumerate(self.cli.calls)
            if name.startswith("blueprint-code")
        )
        self.assertLess(
            self.cli.calls.index("blueprint-spec-review-1-" + DESIGN_DIMENSIONS[-1]),
            first_code,
        )
        artifact = self.store.artifacts()[0]
        self.assertEqual(artifact["provenance"]["spec_review"]["outcome"], "passed")
        path = self.store.root / "jobs" / job["id"] / "attempt-1"
        raw = json.loads((path / "blueprint-generate-1/result.json").read_text())
        self.assertEqual(set(raw), {"spec_changes"})
        record = json.loads((path / "context/SPEC_REVISION_1.json").read_text())
        self.assertEqual(record["changed_fields"], [["title"]])

    def test_repair_design_review_sees_only_proposed_spec_and_requirements(self):
        _, pipeline, original = self.produce()
        self.store.create_repair(
            original["id"],
            {
                "expected_digest": original["digest"],
                "note": "Keep the confirmed journey; clarify its entry point.",
            },
        )
        pipeline.run(self.store.claim("repair", "production"))
        self.assertEqual(
            self.cli.design_sources[-1],
            [
                "ARCHITECTURE.md",
                "DRAFT.md",
                "RESEARCH.md",
                "REVISION.md",
            ],
        )
        # Programs remain available to file authoring and full review, but
        # neither previous code nor reviewer judgments enter design review.
        last = self.store.artifacts()[0]
        context = self.store.root / "jobs" / last["job_id"] / "attempt-1/context"
        self.assertTrue((context / "previous/acceptance").is_dir())
        self.assertTrue((context / "REVIEWS.md").is_file())

    def test_failed_design_dimension_cannot_pass_and_retry_reuses_completed_checks(
        self,
    ):
        self.batch()
        pipeline = self.pipeline()
        self.cli.fail_design_dimension_once = "architecture_contract"
        job = self.store.claim("test", "production")
        with self.assertRaises(FactoryError):
            pipeline.run(job)
        self.assertFalse(any(s.startswith("blueprint-code") for s in self.cli.calls))
        self.assertEqual(self.store.artifacts(), [])
        self.assertEqual(self.store.job(job["id"])["design_reviews"], [])
        self.store.retry(job["id"])
        pipeline.run(self.store.claim("retry", "production"))
        for dimension in DESIGN_DIMENSIONS:
            expected = 2 if dimension == "architecture_contract" else 1
            self.assertEqual(
                self.cli.calls.count("blueprint-spec-review-0-" + dimension), expected
            )
        self.assertEqual(self.cli.calls.count("blueprint-generate-0"), 1)
        report = self.store.artifacts()[0]["provenance"]["spec_review"]
        self.assertEqual(report["outcome"], "passed")
        self.assertEqual(len(report["subreviews"]), len(DESIGN_DIMENSIONS))
        self.assertTrue(
            all(
                r["projection_digest"] and r["proposal_digest"]
                for r in report["subreviews"]
            )
        )
        requests = self.cli.design_requests
        self.assertEqual(
            {d for r in requests for d in r["projection_fields"]},
            {
                "title",
                "roles",
                "features",
                "decisions",
                "phases",
                "acceptance",
                "limits",
            },
        )
        self.assertTrue(
            all(
                r["file_plan_included"]
                == (r["review_dimensions"] == ["phase_acceptance"])
                for r in requests
            )
        )


if __name__ == "__main__":
    unittest.main()
