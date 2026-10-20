"""Host-side structural coverage and aggregate repair scope checks."""
import unittest

from template_factory.contract_scope import (
    REVIEW_RULES_VERSION,
    REPAIR_SCOPE_VERSION,
    REPAIR_SCOPE_VERSION_R7,
    aggregate_semantic_diff_digest,
    validate_contract_coverage,
    validate_repair_diff,
    validate_repair_scope,
)
from template_factory.store import FactoryError


class ContractScopeTests(unittest.TestCase):
    def setUp(self):
        self.spec = {
            "features": [{"id": "F03", "phase": "P0", "applicability": "current required", "acceptance": ["A04"], "reason": "current requirement"}],
            "acceptance": [{"id": "A04", "features": ["F03"]}],
            "decisions": [{"id": "D04", "impact": "safe behavior"}],
            "architecture_markdown": "Architecture",
        }
        self.coverage = {
            "schema": "atlas.contract-coverage.v1",
            "review_rules_version": REVIEW_RULES_VERSION,
            "features": [{
                "feature_id": "F03", "design_basis": "Scenario workflow",
                "entry": "Category management form", "action": "Submit category name",
                "success_state": "Category persists", "navigation": "Return to category list",
                "failure": "Visible validation feedback", "recovery": "Correct and resubmit",
                "acceptance_ids": ["A04"],
            }],
        }
        self.scope = {
            "version": REPAIR_SCOPE_VERSION,
            "known_blockers": [{"feature_id": "F03", "acceptance_id": "A04", "decision_id": "D04", "basis": "current required P0"}],
            "authorized_assertion_changes": [{"acceptance_id": "A02", "change": "single_label_hostname_negative_to_positive", "rationale": "Single-label hosts are valid absolute HTTP(S) URL hosts."}],
            "authored_field_paths": [["architecture_markdown"], ["decisions", "D04", "impact"]],
            "edit_paths": ["acceptance/p0_organize.py"],
        }

    def test_coverage_requires_each_current_required_feature_and_valid_refs(self):
        self.assertEqual(validate_contract_coverage({**self.spec, "contract_coverage": self.coverage}, required=True), self.coverage)
        with self.assertRaises(FactoryError):
            validate_contract_coverage(self.spec, required=True)
        bad = {**self.coverage, "features": [{**self.coverage["features"][0], "acceptance_ids": ["A99"]}]}
        with self.assertRaises(FactoryError):
            validate_contract_coverage({**self.spec, "contract_coverage": bad}, required=True)

    def test_scope_rejects_program_and_immutable_field_escape(self):
        validate_repair_scope(self.scope, {**self.spec, "contract_coverage": self.coverage}, self.scope["edit_paths"])
        for scope in (
            {**self.scope, "edit_paths": ["acceptance/p1_maturity.py"]},
            {**self.scope, "authored_field_paths": [["features", "F03", "phase"]]},
            {**self.scope, "authored_field_paths": [["features", "F99", "reason"]]},
        ):
            with self.subTest(scope=scope), self.assertRaises(FactoryError):
                validate_repair_scope(scope, {**self.spec, "contract_coverage": self.coverage}, self.scope["edit_paths"])

    def test_r7_scope_version_adds_only_runner_manifest(self):
        r7 = {**self.scope, "version": REPAIR_SCOPE_VERSION_R7,
              "edit_paths": ["acceptance/p0_organize.py", "acceptance/runner.json"]}
        validate_repair_scope(r7, {**self.spec, "contract_coverage": self.coverage}, r7["edit_paths"])
        bad = {**r7, "edit_paths": [*r7["edit_paths"], "acceptance/p1_maturity.py"]}
        with self.assertRaises(FactoryError):
            validate_repair_scope(bad, {**self.spec, "contract_coverage": self.coverage}, bad["edit_paths"])

    def test_diff_allows_scoped_reason_but_rejects_feature_phase_or_outside_program(self):
        before = {**self.spec, "contract_coverage": self.coverage}
        after = {**before, "decisions": [{"id": "D04", "impact": "safe behavior clarified"}]}
        self.assertTrue(validate_repair_diff(before, after, {"acceptance/p0_organize.py": "old"}, {"acceptance/p0_organize.py": "new"}, self.scope))
        self.assertTrue(validate_repair_diff(before, after,
            {"acceptance/p0_organize.py": "old", "PRODUCT.md": "before", "template.json": "old", "acceptance/plan.json": "plan1"},
            {"acceptance/p0_organize.py": "new", "PRODUCT.md": "rendered", "template.json": "new", "acceptance/plan.json": "plan2"}, self.scope))
        phase_change = {**before, "features": [{**before["features"][0], "phase": "P1"}]}
        with self.assertRaises(FactoryError):
            validate_repair_diff(before, phase_change, {}, {}, self.scope)
        with self.assertRaises(FactoryError):
            validate_repair_diff(before, before, {"acceptance/p0_library.py": "old"}, {"acceptance/p0_library.py": "new"}, self.scope)

    def test_legacy_baseline_can_gain_explicit_fixed_coverage_schema(self):
        before = dict(self.spec)
        after = {**before, "contract_coverage": self.coverage}
        scope = {**self.scope, "authored_field_paths": [
            ["architecture_markdown"], ["decisions", "D04", "impact"],
            ["contract_coverage", "schema"], ["contract_coverage", "review_rules_version"],
            ["contract_coverage", "features"],
        ]}
        validate_repair_scope(scope, before, scope["edit_paths"])
        self.assertTrue(validate_repair_diff(before, after, {}, {}, scope))
        scope["authored_field_paths"].remove(["contract_coverage", "schema"])
        with self.assertRaises(FactoryError):
            validate_repair_diff(before, after, {}, {}, scope)

    def test_semantic_diff_digest_excludes_derived_render_timestamp_and_binds_real_changes(self):
        args = {
            "scope": self.scope, "baseline_digest": "pinned", "before_spec": self.spec,
            "after_spec": self.spec, "before_program_hashes": {"acceptance/a.py": "old"},
            "after_program_hashes": {"acceptance/a.py": "new"}, "case_design_before": [],
            "case_design_after": [], "case_adaptation_revision": "case-adaptation-aggregate-v1",
            "case_adaptation_input": {"target_profile": "python-web"},
        }
        # Render timestamps/IDs never enter this semantic basis, so a resumed
        # render of the same authored proposal reuses the same review checkpoint.
        self.assertEqual(aggregate_semantic_diff_digest(**args), aggregate_semantic_diff_digest(**args))
        changed = {**args, "after_program_hashes": {"acceptance/a.py": "different"}}
        self.assertNotEqual(aggregate_semantic_diff_digest(**args), aggregate_semantic_diff_digest(**changed))


if __name__ == "__main__":
    unittest.main()
