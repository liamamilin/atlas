"""Cold discovery, provenance, cached updates and multi-leaf isolation contracts."""
import base64
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oss_catalog import CatalogError, CatalogStore  # noqa: E402
from oss_discovery import (  # noqa: E402
    LicenseMatcher, Model, discover_leaf, normalize_license, quote_evidence,
    validate_plan, review_card, QualityRejection, extracted_card, response_items,
)

TEXT = "A complete personal application for following subscriptions and tracking read state. Supports OPML subscription imports."


def file_data(repo, path, body=TEXT):
    return {"path": path, "sha": "a" * 40, "encoding": "base64", "content": base64.b64encode(body.encode()).decode(),
            "html_url": f"https://github.com/{repo}/blob/main/{path}", "git_url": f"https://api.github.com/repos/{repo}/git/blobs/" + "a" * 40}


class SearchSource:
    def __init__(self):
        self.calls = []
        self.items = [{"id": i, "name": f"demo-{i}", "full_name": f"test/demo-{i}", "private": False,
                       "archived": False, "fork": False, "pushed_at": "2026-10-23T00:00:00Z", "default_branch": "main",
                       "language": "Python", "url": f"https://api.github.com/repos/test/demo-{i}",
                       "html_url": f"https://github.com/test/demo-{i}", "description": TEXT,
                       "stargazers_count": 200, "license": None} for i in (101, 102)]

    def get(self, path):
        self.calls.append(path)
        if path.startswith("/search/repositories?"):
            return {"total_count": 2, "items": copy.deepcopy(self.items)}
        if path.startswith("/repositories/"):
            return copy.deepcopy(next(m for m in self.items if m["id"] == int(path.rsplit("/", 1)[1])))
        repo = path.removeprefix("/repos/").rsplit("/", 1)[0]
        if path.endswith("/readme"):
            return file_data(repo, "README.md")
        if path.endswith("/license"):
            raise CatalogError("GitHub 资源不存在或不再公开", 502)
        if "/git/trees/" in path:
            return {"tree": []}
        raise AssertionError(path)


class Extractor:
    invalid_quote = False
    unknown_id = False

    def ask(self, stage, instruction, data):
        if stage == "scenarios":
            return {"scenarios": [{"name": f"测试任务 {i}", "description": f"独立的用户任务 {i}", "search_queries": [f"generic task{i}"]} for i in range(3)]}
        if stage == "screen":
            return {"selected_ids": [999] if self.unknown_id else [c["id"] for c in data["candidates"]]}
        return {"items": [{"repository_id": 999 if self.unknown_id else r["repository_id"], "relevant": True,
                           **{field: {"text": "有原文支持的测试事实", "quote": "Invented unsupported statement" if self.invalid_quote else TEXT}
                              for field in ("positioning", "summary", "scope")},
                           "features": [{"text": "订阅与阅读状态", "quote": TEXT}],
                           "matches": [{"scenario_id": s["id"], "reason": "原文明确描述订阅与阅读状态", "quote": TEXT} for s in data["scenarios"][:2]]}
                          for r in data["repositories"]]}


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = CatalogStore(self.root / "test.sqlite", bootstrap=False)
        self.github, self.model = SearchSource(), Extractor()

    def run_leaf(self, leaf="feed-reader", recheck=False):
        self.sequence = getattr(self, "sequence", 0) + 1
        run = {"id": "test-" + leaf + str(self.sequence), "leaf": leaf, "status": "running", "created": 0, "updated": 0,
               "unchanged": 0, "failed": 0, "processed": 0, "errors": []}
        # No network license matching: missing licenses must remain pending.
        discover_leaf(self.store, leaf, run, github=self.github, model=self.model, root=self.root, recheck=recheck)
        return run

    def test_cold_start_searches_without_any_curated_shortlist_and_repeats_without_duplicates(self):
        with patch("oss_catalog.manifest", side_effect=AssertionError("A curated shortlist must not be read")):
            first = self.run_leaf()
            self.assertEqual((first["status"], first["created"]), ("completed", 2))
            self.assertEqual(len([p for p in self.github.calls if p.startswith("/search/")]), 4)
            project = self.store.catalog("feed-reader")["projects"][0]
            self.store.favorite(project["repository_id"], True)
            self.github.calls.clear()
            second = self.run_leaf()
        self.assertEqual((second["created"], second["updated"], second["unchanged"]), (0, 0, 2))
        self.assertEqual((second["source_cache_hits"], second["source_fetches"]), (2, 0))
        self.assertEqual(self.store.previous(project["full_name"])["sources"][0]["retrieved_at"], project["sources"][0]["retrieved_at"])
        self.assertTrue(all(p.startswith(("/search/", "/repositories/")) for p in self.github.calls))
        self.assertEqual(len(self.store.catalog("feed-reader", favorites=True)["projects"]), 1)
        self.assertTrue(second["gaps"])

    def test_same_repository_shared_by_multiple_leaves_keeps_every_association(self):
        self.run_leaf("feed-reader")
        second = self.run_leaf("diagramming-application")
        self.assertEqual(second["created"], 0)
        self.assertEqual(len(self.store.catalog()["projects"]), 2)
        self.assertEqual(len(self.store.catalog("feed-reader")["projects"]), 2)
        self.assertEqual(len(self.store.catalog("diagramming-application")["projects"]), 2)
        self.assertEqual(len(self.store.previous("test/demo-101")["matches"]), 4)

    def test_fabricated_quote_cannot_replace_previously_saved_facts(self):
        self.run_leaf()
        before = self.store.previous("test/demo-101")
        self.model.invalid_quote = True
        result = self.run_leaf()
        self.assertEqual((result["status"], result["failed"]), ("failed", 2))
        self.assertEqual(self.store.previous("test/demo-101"), before)

    def test_quote_repair_can_reject_a_category_mismatch_without_a_transport_failure(self):
        original = self.model.ask
        self.model.invalid_quote = True
        def ask(stage, instruction, data):
            if stage == "extract_repair":
                return {"items": [{"repository_id": r["repository_id"], "relevant": False, "decision": "exclude", "rejection_reason": "官方文档确认属于相邻分类"} for r in data["repositories"]]}
            return original(stage, instruction, data)
        self.model.ask = ask
        result = self.run_leaf()
        self.assertEqual((result["failed"], result["rejected"]), (0, 2))
        self.assertFalse(self.store.catalog("feed-reader")["projects"])

    def test_model_cannot_add_a_repository_that_search_did_not_return(self):
        self.model.unknown_id = True
        result = self.run_leaf()
        self.assertEqual(result["status"], "failed")
        self.assertFalse(self.store.catalog("feed-reader")["projects"])
        self.assertEqual(result["created"], 0)
        self.assertEqual(len(self.store.candidates("feed-reader")), 2)

    def test_single_item_response_can_be_normalized_without_guessing_repository_identity(self):
        self.assertEqual(response_items({"repository_id": "101", "relevant": False}, {101})[0]["repository_id"], 101)
        for response in ({"repository_id": "999"}, {"repository_id": True}, {"items": [{"repository_id": 101}, {"repository_id": 101}]}):
            with self.assertRaises(CatalogError):
                response_items(response, {101})

    def test_readme_change_requires_new_source_read(self):
        self.run_leaf()
        self.github.calls.clear()
        for item in self.github.items:
            item["pushed_at"] = "2026-10-24T00:00:00Z"
        self.run_leaf()
        self.assertEqual(sum(p.endswith("/readme") for p in self.github.calls), 2)

    def test_previously_public_candidate_cannot_send_new_private_content_to_model(self):
        original = self.github.get
        def changed(path):
            response = original(path)
            if path.startswith("/repositories/"):
                response["private"] = True
            return response
        self.github.get = changed
        result = self.run_leaf()
        self.assertEqual(result["failed"], 2)
        self.assertFalse(self.store.catalog("feed-reader")["projects"])
        self.assertFalse(any(path.endswith("/readme") for path in self.github.calls))

    def test_plan_cannot_target_a_known_repository_but_similar_scenarios_are_retained(self):
        value = self.model.ask("scenarios", "", {})
        value["scenarios"][0]["search_queries"] = ["repo:someone/known-project"]
        with self.assertRaises(CatalogError):
            validate_plan(value, "feed-reader")
        value = self.model.ask("scenarios", "", {})
        value["scenarios"][1]["name"] = value["scenarios"][0]["name"]
        self.assertEqual(len({s["id"] for s in validate_plan(value, "feed-reader")}), 3)

    def test_valid_model_response_is_cached_with_actual_usage_receipt(self):
        run = {"model_calls": 0}
        model = Model(self.root, run, lambda _: None)
        response = {"text": '{"value":123}', "model": "fixture", "provider": "fixture", "usage": {"total_tokens": 20}}
        with patch("atlas_model.complete", return_value=response) as complete:
            self.assertEqual(model.ask("fixture", "Return a JSON value", {"input": "public"}), {"value": 123})
            model.ask("fixture", "Return a JSON value", {"input": "public"})
            self.assertEqual(complete.call_count, 1)
        self.assertEqual(run["model_calls"], 1)
        self.assertTrue(run["model_receipts"][-1]["cached"])

    def test_license_match_does_not_ignore_appended_restrictions_or_operative_copyright_clauses(self):
        standard = "Permission is hereby granted without restriction.\nThe above copyright notice must be retained."
        root = self.root / "spdx"
        root.mkdir()
        for identifier in ["MIT", "Apache-2.0", "GPL-3.0-only", "GPL-2.0-only", "AGPL-3.0-only", "BSD-3-Clause", "BSD-2-Clause", "MPL-2.0"]:
            (root / (identifier + ".json")).write_text(json.dumps({"data": {"licenseText": standard, "isOsiApproved": True}, "source_url": "https://spdx.org/licenses/MIT.html", "sha256": "test", "retrieved_at": "2026-10-23"}))
        matcher = LicenseMatcher(self.root)
        meta = {"full_name": "test/license", "license": {"spdx_id": "MIT"}}
        exact = matcher.classify(meta, file_data("test/license", "LICENSE", standard))
        custom = matcher.classify(meta, file_data("test/license", "LICENSE", standard + "\nCommercial use is prohibited."))
        prefixed = matcher.classify(meta, file_data("test/license", "LICENSE", "Commercial use is prohibited.\n" + standard))
        copyright_restriction = matcher.classify(meta, file_data("test/license", "LICENSE", "Copyright (c) 2026 Example. Commercial use is prohibited.\n" + standard))
        restricted_readme = matcher.classify(meta, file_data("test/license", "LICENSE", standard),
                                            file_data("test/license", "README.md", "## License\nIcons may not be used in commercial products.\n## Running\nRun locally."))
        self.assertEqual(exact["status"], "open_source")
        self.assertEqual(custom["status"], "pending")
        self.assertEqual(prefixed["status"], "pending")
        self.assertEqual(copyright_restriction["status"], "pending")
        self.assertEqual(restricted_readme["status"], "pending")
        self.assertIn("Icons may not", restricted_readme["restriction_evidence"]["excerpt"])
        self.assertIn("copyrightholder", normalize_license("copyright holder must approve redistribution"))

    def test_source_bound_review_prevents_republishing_excluded_results(self):
        path = self.root / "reviews.json"
        path.write_text(json.dumps({"test/app": {"readme_sha256": "hash", "exclude": True, "reason": "Only a product brochure"}}))
        card = {"full_name": "test/app", "summary_evidence": {"source_sha256": "hash"}, "matches": []}
        with patch("oss_discovery.PROJECT_REVIEWS", path):
            with self.assertRaisesRegex(QualityRejection, "product brochure"):
                review_card(card)
            card["summary_evidence"]["source_sha256"] = "changed"
            with self.assertRaisesRegex(QualityRejection, "README 已变化"):
                review_card(card)

    def test_quote_check_rejects_short_or_missing_evidence(self):
        source = {"url": "url", "immutable_url": "blob", "sha256": "sha"}
        for quote in ("RSS", "This fabricated phrase does not occur in the source"):
            with self.assertRaises(CatalogError):
                quote_evidence(quote, TEXT, source)

    def test_candidates_over_batch_limit_remain_queued_and_next_run_advances(self):
        sample = self.github.items[0]
        self.github.items = [{**sample, "id": i, "full_name": f"test/demo-{i}", "name": f"demo-{i}"} for i in range(100, 120)]
        first = self.run_leaf()
        self.assertEqual((first["created"], first["candidate_counts"]["pending"]), (8, 12))
        repeated = self.run_leaf(recheck=True)
        self.assertEqual((repeated["created"], repeated["updated"], repeated["unchanged"]), (0, 0, 8))
        self.assertEqual(repeated["selected_ids"], first["selected_ids"])
        second = self.run_leaf()
        self.assertEqual((second["created"], second["candidate_counts"]["pending"]), (8, 4))
        self.assertEqual(len(self.store.catalog("feed-reader")["projects"]), 16)
        self.assertEqual(len(self.store.candidates("feed-reader")), 20)

    def test_existing_scenarios_are_preserved_when_model_proposes_another_set(self):
        with self.store.connect() as con:
            self.store._scenarios(con, [{"id": "retained", "name": "历史场景", "description": "先保留，后归并"}], "feed-reader", prune=False)
        self.run_leaf()
        self.assertIn("retained", {s["id"] for s in self.store.catalog("feed-reader")["scenarios"]})

    def test_changed_published_project_is_refreshed_before_unread_backlog(self):
        sample = self.github.items[0]
        self.github.items = [{**sample, "id": i, "full_name": f"test/demo-{i}", "name": f"demo-{i}"} for i in range(100, 120)]
        first = self.run_leaf()
        changed_id = first["selected_ids"][0]
        next(m for m in self.github.items if m["id"] == changed_id)["pushed_at"] = "2026-10-24T00:00:00Z"
        second = self.run_leaf()
        self.assertEqual(second["selected_ids"][0], changed_id)
        self.assertEqual(second["updated"], 1)
        self.assertEqual(second["created"], 7)

    def test_conditional_fit_requires_conditions_and_can_cite_official_document(self):
        scenarios = validate_plan(self.model.ask("scenarios", "", {}), "feed-reader")
        item = self.model.ask("extract", "", {"repositories": [{"repository_id": 101}], "scenarios": scenarios})["items"][0]
        document = "Official guide: Subscribe to RSS feeds and organize incoming articles."
        resources = {"readme": file_data("test/demo-101", "README.md"), "license": None, "retrieved_at": "2026-10-23",
                     "documents": [{"file": file_data("test/demo-101", "docs/guide.md", document), "retrieved_at": "2026-10-23"}]}
        item["matches"] = [{"scenario_id": scenarios[0]["id"], "reason": "兼容的期刊订阅可用于目录跟踪", "applicability": "conditional", "conditions": [], "source_id": "doc-1", "quote": document}]
        with self.assertRaisesRegex(CatalogError, "成立条件"):
            extracted_card(item, self.github.items[0], resources, scenarios, LicenseMatcher(self.root))
        item["matches"][0]["conditions"] = ["期刊提供兼容的 RSS 订阅源"]
        card = extracted_card(item, self.github.items[0], resources, scenarios, LicenseMatcher(self.root))
        self.assertEqual(card["matches"][0]["evidence"]["source_kind"], "documentation")
        item["matches"][0]["source_id"] = "unread-document"
        with self.assertRaisesRegex(CatalogError, "未读取"):
            extracted_card(item, self.github.items[0], resources, scenarios, LicenseMatcher(self.root))

    def test_document_selection_reads_text_guides_not_code_or_dependency_notices(self):
        from oss_sources import document_paths
        tree = {"tree": [{"type": "blob", "path": p} for p in ["README.md", "docs/features.md", "src/password.py", "LICENSE.txt", "docs/third-party.md", "CONTRIBUTING.md", "docs/usage.md", "docs/superpowers/plans/2026-feature.md", "tests/README.md", "docs/code-review.md", ".claude/skills/feature-addition.md", "docs/STYLE_AND_BEST_PRACTICES.md", "release-notes.md"]]}
        self.assertEqual(document_paths(tree, file_data("test/demo-101", "README.md"), "test/demo-101"), ["docs/features.md", "docs/usage.md"])


if __name__ == "__main__":
    unittest.main()
