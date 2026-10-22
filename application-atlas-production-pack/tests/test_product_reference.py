"""ProductReference v1 contract fixture and unittest-discover checks."""
from copy import deepcopy
import unittest

from template_factory.product_reference import (
    render_reference,
    select_scope,
    validate_reference,
)


def make_reference():
    """Small representative fixture available to other tests by import."""
    return {
        "schema": "atlas.product-reference.v1",
        "product_shape": {
            "name": "Personal Shelf", "audience": "One owner",
            "value": "Keep and find links", "delivery_profile": "Local web app",
            "boundary": "Private instance", "excluded": ["Sharing"],
        },
        "roles": [{"id": "owner", "name": "Owner", "goal": "Find saved links", "data_scope": "Own collection"}],
        "objects": [{
            "id": "bookmark", "name": "Bookmark",
            "fields": [{"name": "url", "meaning": "Original address"}],
            "states": ["active", "archived"], "relations": [],
        }, {
            "id": "collection", "name": "Collection",
            "fields": [{"name": "name", "meaning": "User supplied name"}],
            "states": ["active"], "relations": [],
        }],
        "actions": [
            {
                "id": "save", "name": "Save bookmark", "role_ids": ["owner"],
                "object_ids": ["bookmark"], "surface_ids": ["home"],
                "rule_ids": ["valid-url"], "preconditions": ["URL supplied"],
                "effects": ["Save the supplied URL"],
                "failures": [{"condition": "Invalid URL", "response": "Explain the URL error", "recovery": "Keep the form open"}],
                "basis_ids": ["design"], "depends_on": [],
                "transitions": [{"object_id": "bookmark", "from_states": [], "to_state": "active"}],
            },
            {
                "id": "bulk-archive", "name": "Bulk archive", "role_ids": ["owner"],
                "object_ids": ["bookmark"], "surface_ids": ["home"],
                "rule_ids": ["valid-url"], "preconditions": ["Rows selected"],
                "effects": ["Update selected bookmarks"],
                "failures": [{"condition": "Write failure", "response": "Show failure", "recovery": "Retry selection"}],
                "basis_ids": ["design"], "depends_on": [],
                "transitions": [{"object_id": "bookmark", "from_states": ["active"], "to_state": "archived"}],
            },
        ],
        "surfaces": [{
            "id": "home", "name": "Bookmark home", "kind": "web",
            "purpose": "Find and save bookmarks", "role_ids": ["owner"],
            "action_ids": ["save", "bulk-archive"], "sections": ["Search", "Results"],
            "navigation": [],
            "states": {"loading": "Show a loading indicator", "empty": "Offer the first save", "no_results": "Offer clear search", "error": "Keep conditions and retry", "forbidden": "Explain unavailable access"},
            "query": {"search": "Match URL and title text", "filter": "Filter by state", "sort": "Sort by title", "pagination": "No pagination for small collections", "bulk": "Explicit selection only", "export": "Not applicable; transfer has its own surface"},
        }],
        "journeys": [{
            "id": "find-save", "name": "Save a link", "goal": "Save a bookmark for later",
            "role_ids": ["owner"],
            "steps": [{"surface_id": "home", "action_id": "save", "role_id": "owner", "success": "The new bookmark appears"}],
            "completion": "Bookmark is available in the collection", "recovery": "Correct the URL and retry",
        }],
        "rules": [{"id": "valid-url", "statement": "Only valid HTTP or HTTPS URLs are saved", "object_ids": ["bookmark", "collection"], "basis_ids": ["design"]}],
        "assertions": [
            {"id": "save-works", "given": "An owner has a valid URL", "when": "They save it", "then": "One active bookmark appears", "negative": "Invalid input is retained with an error", "action_ids": ["save"], "rule_ids": ["valid-url"], "journey_ids": ["find-save"]},
            {"id": "archive-works", "given": "An owner selected bookmarks", "when": "They archive them", "then": "Only selected bookmarks are archived", "negative": "A failed write is not reported as successful", "action_ids": ["bulk-archive"], "rule_ids": ["valid-url"], "journey_ids": []},
        ],
        "scope_options": [{"id": "p0", "name": "P0", "journey_ids": ["find-save"], "extra_action_ids": [], "depends_on": [], "rationale": "Close the save and find loop"}],
        "basis": [
            {"id": "design", "kind": "design_inference", "statement": "Local-first single-owner design", "source_ids": [], "depends_on": ["requirement"]},
            {"id": "requirement", "kind": "requirement", "statement": "The owner can save links", "source_ids": [], "depends_on": []},
        ],
        "gaps": [],
    }


class ProductReferenceTests(unittest.TestCase):
    def test_fixture_validates_and_renders_deterministically(self):
        spec = make_reference()
        self.assertIs(validate_reference(spec), spec)
        rendered = render_reference(spec)
        self.assertEqual(rendered, render_reference(deepcopy(spec)))
        self.assertEqual(set(rendered), {"PRODUCT_REFERENCE.md", "PRODUCT_REFERENCE.json"})
        self.assertIn("### find-save", rendered["PRODUCT_REFERENCE.md"])
        self.assertIn("## Journeys", rendered["PRODUCT_REFERENCE.md"])
        self.assertIn("- 查询行为 / Query behavior:", rendered["PRODUCT_REFERENCE.md"])
        self.assertIn("- 成功结果 / Success: The new bookmark appears", rendered["PRODUCT_REFERENCE.md"])
        self.assertIn('"schema": "atlas.product-reference.v1"', rendered["PRODUCT_REFERENCE.json"])

    def test_dangling_duplicate_missing_entry_wrong_role_and_core_gap_rejected(self):
        mutations = [
            lambda s: s["journeys"][0]["steps"][0].update(action_id="missing"),
            lambda s: s["objects"].append(deepcopy(s["objects"][0])),
            lambda s: s["journeys"].clear(),
            lambda s: s["actions"][0].update(role_ids=["missing-role"]),
            lambda s: s["gaps"].append({"id": "core-gap", "statement": "Unknown core rule", "core": True, "action_ids": [], "resolution": "Resolve before review"}),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                spec = make_reference()
                mutate(spec)
                with self.assertRaises(ValueError):
                    validate_reference(spec)

    def test_dependency_cycle_is_rejected(self):
        spec = make_reference()
        spec["actions"][0]["depends_on"] = ["bulk-archive"]
        spec["actions"][1]["depends_on"] = ["save"]
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate_reference(spec)

    def test_explicit_transition_rejects_unsupported_state(self):
        spec = make_reference()
        spec["actions"][0]["transitions"][0]["to_state"] = "deleted"
        with self.assertRaisesRegex(ValueError, "state not declared"):
            validate_reference(spec)

    def test_malformed_nested_types_raise_value_error(self):
        mutations = [
            lambda s: s["journeys"][0].update(steps={}),
            lambda s: s["journeys"][0].update(steps=5),
            lambda s: s["actions"][0].update(role_ids=[["owner"]]),
            lambda s: s["actions"][0].update(object_ids=[["bookmark"]]),
            lambda s: s["surfaces"][0].update(kind=[]),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                spec = make_reference()
                mutate(spec)
                with self.assertRaises(ValueError):
                    validate_reference(spec)

    def test_empty_action_requirements_and_core_collections_rejected(self):
        for key in ("preconditions", "effects", "failures", "basis_ids"):
            with self.subTest(key=key):
                spec = make_reference()
                spec["actions"][0][key] = []
                with self.assertRaises(ValueError):
                    validate_reference(spec)
        for collection in ("roles", "objects", "actions", "surfaces", "journeys", "assertions"):
            with self.subTest(collection=collection):
                spec = make_reference()
                spec[collection] = []
                with self.assertRaises(ValueError):
                    validate_reference(spec)

    def test_unknown_source_ids_rejected_for_all_basis_kinds(self):
        spec = make_reference()
        spec["basis"][1]["source_ids"] = ["unknown-source"]
        with self.assertRaisesRegex(ValueError, "untrusted source"):
            validate_reference(spec, source_ids={"trusted-source"})

    def test_scope_excludes_mixed_assertion_when_independent_assertion_exists(self):
        spec = make_reference()
        mixed = deepcopy(spec["assertions"][0])
        mixed.update(id="mixed-save-and-archive", action_ids=["save", "bulk-archive"])
        spec["assertions"].append(mixed)
        sliced = select_scope(spec, "p0")
        self.assertEqual(sliced["action_ids"], ["save"])
        self.assertEqual(sliced["deferred_action_ids"], ["bulk-archive"])
        self.assertNotIn("mixed-save-and-archive", sliced["assertion_ids"])
        self.assertIn("save-works", sliced["assertion_ids"])
        self.assertEqual(sliced["surface_ids"], ["home"])
        self.assertIn("collection", sliced["object_ids"])

    def test_scope_rejects_when_only_mixed_assertion_covers_selected_action(self):
        spec = make_reference()
        spec["assertions"] = [
            {
                "id": "only-mixed", "given": "An owner has bookmarks", "when": "They save then archive",
                "then": "The selected work is complete", "negative": "Failures remain visible",
                "action_ids": ["save", "bulk-archive"], "rule_ids": ["valid-url"],
                "journey_ids": ["find-save"],
            }
        ]
        with self.assertRaisesRegex(ValueError, "add a separate assertion"):
            select_scope(spec, "p0")


if __name__ == "__main__":
    unittest.main()
