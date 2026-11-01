"""Observed first-round failures, retaining bounded search and strict plans."""
import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_model
from oss_catalog import CatalogError, GitHub, GitHubResponseTooLarge, ModelServiceUnavailable
from oss_discovery import Model, validate_plan


class PreparationRepairTests(unittest.TestCase):
    @staticmethod
    def plan():
        return {"scenarios": [{"name": "仪表故障排查", "description": "仪表技师排查控制器与输入输出设备故障。",
                               "search_queries": ["I/O diagnostics troubleshooting"]}]}

    def test_io_acronym_is_generic_but_repository_selectors_stay_rejected(self):
        self.assertEqual(validate_plan(self.plan(), "distributed-control-system-dcs")[0]["search_queries"],
                         ["input output diagnostics troubleshooting"])
        for query in ["repo:owner/project", "owner/project", "https://github.com/owner/project", "org:owner"]:
            plan = self.plan(); plan["scenarios"][0]["search_queries"] = [query]
            with self.subTest(query=query), self.assertRaises(CatalogError):
                validate_plan(plan, "distributed-control-system-dcs")

    def test_observed_translated_name_field_is_recovered_without_guessing(self):
        plan = self.plan()
        item = plan["scenarios"][0]
        item["中文场景名"] = item.pop("name")
        self.assertEqual(validate_plan(plan, "it-operations-management-itom")[0]["name"], "仪表故障排查")
        for value in [None, "", 123, "很" * 81]:
            bad = copy.deepcopy(plan); bad["scenarios"][0]["中文场景名"] = value
            with self.subTest(value=value), self.assertRaises(CatalogError):
                validate_plan(bad, "it-operations-management-itom")

    def test_oversized_search_splits_same_page_window_and_keeps_order(self):
        client = GitHub(); seen = []
        def get(path):
            params = parse_qs(path.split("?", 1)[1]); seen.append(params)
            size, page = int(params["per_page"][0]), int(params["page"][0])
            if size == 100:
                raise GitHubResponseTooLarge("oversize", 502)
            start = (page - 1) * size
            return {"items": [{"id": n} for n in range(start, start + size)], "total_count": 500,
                    "incomplete_results": page == 4}
        with patch.object(client, "_get", side_effect=get):
            response = client.get("/search/repositories?q=generic+task&per_page=100&page=2")
        self.assertEqual([m["id"] for m in response["items"]], list(range(100, 200)))
        self.assertEqual([(int(p["page"][0]), int(p["per_page"][0])) for p in seen], [(2, 100), (3, 50), (4, 50)])
        self.assertEqual(response["search_request_count"], 3)
        self.assertTrue(response["incomplete_results"])
        self.assertTrue(all(p["q"] == ["generic task"] for p in seen))

    def test_size_failure_stays_bounded_and_does_not_split_readme(self):
        client = GitHub()
        with patch.object(client, "_get", side_effect=GitHubResponseTooLarge("oversize", 502)) as get:
            with self.assertRaises(GitHubResponseTooLarge):
                client.get("/search/repositories?q=generic&per_page=100&page=1")
            self.assertEqual(get.call_count, 3)  # 100, 50, 25: stop before a fourth request.
            get.reset_mock()
            with self.assertRaises(GitHubResponseTooLarge):
                client.get("/repos/owner/project/readme")
            get.assert_called_once()

    def test_empty_completions_retry_then_cache_only_success(self):
        with tempfile.TemporaryDirectory() as directory:
            run = {"id": "empty-response-fixture", "model_calls": 0}
            model = Model(Path(directory), run, lambda _: None, fast=True)
            route = {"provider": "fixture", "model": "fixture", "base_url": "https://example.test/v1"}
            empty = {"text": "", "provider": "fixture", "model": "fixture", "usage": {"completion_tokens": 0}}
            reply = {**empty, "text": '{"ok":true}'}
            with patch.object(atlas_model, "resolve", return_value=route), \
                    patch.object(atlas_model, "resolved_view", return_value=route), \
                    patch.object(atlas_model, "complete", side_effect=[empty, reply]) as complete, \
                    patch("oss_discovery.time.sleep"):
                self.assertEqual(model.ask("scenarios_open", "Return JSON", {}), {"ok": True})
            self.assertEqual(complete.call_count, 2)
            self.assertEqual(run["model_errors"][0]["code"], "empty_response")
            self.assertEqual(len(list((Path(directory) / "model-cache").glob("*.json"))), 1)
            with patch.object(atlas_model, "resolve", return_value=route), \
                    patch.object(atlas_model, "resolved_view", return_value=route), \
                    patch.object(atlas_model, "complete", return_value=empty) as complete, \
                    patch("oss_discovery.time.sleep"):
                with self.assertRaises(ModelServiceUnavailable):
                    model.ask("another-stage", "Return JSON", {"different_input": True})
            self.assertEqual(complete.call_count, 3)


if __name__ == "__main__":
    unittest.main()
