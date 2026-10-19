"""Identity-scoped scenario policy contracts for cognition prompts."""

from pathlib import Path
import sys
import tempfile
import unittest
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from template_factory.cognition import (
    AGGREGATE_SEMANTIC_REVIEW_PROMPT,
    DESIGN_REVIEW_PROMPT,
    GENERATE_PROMPT,
    _case_adaptation_review_digest,
    _reuse_prepared_case_adaptation,
    _validate_design_review_checkpoint,
)
from template_factory.scenario_policy import (
    BOOKMARK_PRODUCT_ID,
    BOOKMARK_SCENARIO_ID,
    policy_for,
    policy_prompt,
    write_architecture_review_material,
)
from template_factory.error_contracts import required_branches
from template_factory.store import digest
from template_factory.store import FactoryError


class ScenarioPolicyTests(unittest.TestCase):
    def test_unrelated_budget_and_meeting_scenes_receive_no_bookmark_policy(self):
        for scenario, product_id in (
            ({"id": "scene-budget", "name": "Budget tracker"}, "product-budget"),
            ({"id": "scene-meeting", "name": "Meeting planner"}, "product-meeting"),
        ):
            self.assertIsNone(policy_for(scenario, product_id))
            self.assertEqual(policy_prompt(policy_for(scenario, product_id)), "")

    def test_policy_requires_both_pinned_scenario_and_product_identity(self):
        scenario = {"id": BOOKMARK_SCENARIO_ID}
        self.assertIsNone(policy_for(scenario, "another-product"))
        self.assertIsNone(policy_for({"id": "another-scene"}, BOOKMARK_PRODUCT_ID))
        policy = policy_for(scenario, BOOKMARK_PRODUCT_ID)
        self.assertEqual(policy["revision"], "CP-1")

    def test_bookmark_policy_names_category_and_search_contracts(self):
        policy = policy_for({"id": BOOKMARK_SCENARIO_ID}, BOOKMARK_PRODUCT_ID)
        rendered = policy_prompt(policy).lower()
        self.assertIn("a04", rendered)
        self.assertIn("a12", rendered)
        self.assertIn('"input_field": "name"', rendered)
        self.assertIn('"existing_category_identity_field": "category_id"', rendered)
        self.assertIn('"json_field": "category"', rendered)
        self.assertIn('"html_field": "category_id"', rendered)
        self.assertIn('"never_create_from_html_id": true', rendered)
        self.assertIn('"invalid_json_values": ["omitted", "json null", "empty", "whitespace_only", "121_characters"]', rendered)
        self.assertIn('"omitted_or_null_json": "use the default category."', rendered)
        self.assertIn('"unknown_get_filter": "return an empty result;', rendered)
        self.assertIn("retain submitted values, and make no writes", rendered)
        self.assertIn("title, hostname, and description", rendered)
        self.assertIn("does not match tags", rendered)
        self.assertIn("raw url substrings", rendered)
        self.assertIn("a02 may replace only its single-label-hostname rejection example", rendered)

    def test_a04_and_a12_policy_matches_host_error_branch_matrix(self):
        policy = policy_for({"id": BOOKMARK_SCENARIO_ID}, BOOKMARK_PRODUCT_ID)
        branches = required_branches()
        a04 = [row for row in branches if row["acceptance_ids"] == ["A04"]]
        self.assertTrue(a04)
        self.assertEqual({row["code"] for row in a04}, {"invalid_name"})
        self.assertEqual({row["field"] for row in a04}, {"name"})
        management = policy["category_contract"]["management"]
        expected_a04 = set()
        for transport in ("html", "json"):
            for operation in ("category_create", "category_rename"):
                values = ["omitted", "empty", "whitespace", "overlong_121"]
                if transport == "json":
                    values.append("null")
                expected_a04.update((transport, operation, "name", value) for value in values)
        actual_a04 = {(row["transport"], row["operation"], row["field"], row["value_kind"]) for row in a04}
        self.assertEqual(actual_a04, expected_a04)
        self.assertEqual(management["html_invalid_values"], ["omitted", "empty", "whitespace_only", "121_characters"])
        self.assertEqual(management["json_invalid_values"], ["omitted", "empty", "whitespace_only", "121_characters", "null"])
        a12 = [row for row in branches if row["acceptance_ids"] == ["A12"]]
        self.assertEqual({row["operation"] for row in a12}, {"bookmark_save", "bookmark_move"})
        self.assertEqual({row["code"] for row in a12}, {"invalid_category"})
        actual_a12 = {(row["transport"], row["operation"], row["field"], row["value_kind"]) for row in a12}
        expected_a12 = {
            ("html", "bookmark_save", "category", value)
            for value in ("empty", "whitespace", "overlong_121")
        } | {
            ("json", "bookmark_save", "category", value)
            for value in ("empty", "whitespace", "overlong_121")
        } | {
            ("html", "bookmark_move", "category_id", value)
            for value in ("omitted", "empty", "unknown_id")
        } | {
            ("json", "bookmark_move", "category", value)
            for value in ("empty", "whitespace", "overlong_121", "omitted", "null")
        }
        self.assertEqual(actual_a12, expected_a12)
        self.assertEqual(policy["category_contract"]["bookmark_save"]["invalid_values"], ["empty", "whitespace_only", "121_characters"])
        self.assertEqual(policy["category_contract"]["bookmark_move"]["invalid_json_values"], ["omitted", "JSON null", "empty", "whitespace_only", "121_characters"])

    def test_prepared_adaptation_reuses_choices_and_bound_policy_without_agent_call(self):
        choices = [{
            "evidence_ids": ["ev-search"], "disposition": "adjusted",
            "capability": "Preserve declared search fields.",
            "reason": "Prepared adaptation aligns with the pinned contract.",
        }]
        scenario = {"id": BOOKMARK_SCENARIO_ID, "name": "Personal bookmarks"}
        policy = policy_for(scenario, BOOKMARK_PRODUCT_ID)
        prepared = {
            "case_design": choices,
            "case_adaptation_input": {"target_profile": {"delivery_profile": "python-web"}},
        }
        checkpoint_calls = []

        def checkpoint(name, build):
            checkpoint_calls.append(name)
            return build()

        name, adaptation_input, result = _reuse_prepared_case_adaptation(
            prepared, scenario, policy, checkpoint
        )
        self.assertEqual(name, "case-adaptation-prepared-" + digest(choices)[:16])
        self.assertEqual(checkpoint_calls, [name])
        self.assertEqual(result, {"choices": choices})
        self.assertEqual(adaptation_input["scenario"], scenario)
        self.assertEqual(adaptation_input["scenario_policy"], policy)
        self.assertEqual(adaptation_input["target_profile"], {"delivery_profile": "python-web"})

    def test_global_generation_and_design_prompts_have_no_bookmark_rules(self):
        shared = "\n".join((GENERATE_PROMPT, DESIGN_REVIEW_PROMPT, AGGREGATE_SEMANTIC_REVIEW_PROMPT)).lower()
        for term in ("indexeddb", "dexie", "a02", "a04", "a12", "category_id", "hostname, and description"):
            self.assertNotIn(term, shared)
        self.assertIn("case_adaptation_policy.json", DESIGN_REVIEW_PROMPT.lower())
        self.assertIn("case_policy_digest", AGGREGATE_SEMANTIC_REVIEW_PROMPT)
        self.assertIn("spec.contract_coverage", GENERATE_PROMPT)
        self.assertIn('"spec":{"title"', GENERATE_PROMPT)
        self.assertIn('"limits":["..."],"contract_coverage":{"schema":"atlas.contract-coverage.v1"', GENERATE_PROMPT)
        self.assertNotIn("Include top-level contract_coverage", GENERATE_PROMPT)

    def test_architecture_review_material_contains_case_design_and_bound_policy(self):
        choices = [{
            "evidence_ids": ["ev-search"], "disposition": "adjusted",
            "capability": "Search title, hostname, and description.",
            "reason": "Keep declared target search semantics.",
        }]
        policy = policy_for({"id": BOOKMARK_SCENARIO_ID}, BOOKMARK_PRODUCT_ID)
        with tempfile.TemporaryDirectory() as directory:
            written = write_architecture_review_material(directory, choices, policy)
            self.assertEqual(set(written), {"CASE_DESIGN.json", "CASE_ADAPTATION_POLICY.json"})
            self.assertEqual(json.loads((Path(directory) / "CASE_DESIGN.json").read_text()), choices)
            self.assertEqual(
                json.loads((Path(directory) / "CASE_ADAPTATION_POLICY.json").read_text()),
                policy,
            )

    def test_cached_design_review_rejects_changed_policy_for_same_plan(self):
        plan = {"spec": {"title": "Same plan"}}
        choices = [{"evidence_ids": ["ev-search"], "disposition": "adjusted"}]
        old_policy = policy_for({"id": BOOKMARK_SCENARIO_ID}, BOOKMARK_PRODUCT_ID)
        new_policy = {**old_policy, "revision": "CP-2"}
        stale_cached_report = {
            "proposal_digest": digest(plan),
            "case_adaptation_review_digest": _case_adaptation_review_digest(choices, old_policy),
        }
        with self.assertRaisesRegex(FactoryError, "design review case adaptation changed"):
            _validate_design_review_checkpoint(stale_cached_report, plan, choices, new_policy)


if __name__ == "__main__":
    unittest.main()
