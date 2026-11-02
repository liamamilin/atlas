import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import atlas_assistant  # noqa: E402
from atlas_assistant import AssistantError  # noqa: E402

REAL_REQUEST = atlas_assistant._request


def call(name, arguments, call_id="c1"):
    return {"id": call_id, "type": "function",
            "function": {"name": name, "arguments": json.dumps(arguments)}}


def reply(content="", calls=()):
    calls = list(calls)
    return {"content": content, "tool_calls": calls, "usage": {"total_tokens": 10},
            "raw": {"choices": [{"message": {"content": content, "tool_calls": calls}}]}}


class FakeModel:
    def __init__(self, *replies):
        self.replies = list(replies)
        self.seen = []

    def __call__(self, messages, **_):
        self.seen.append(json.loads(json.dumps(messages)))
        return self.replies.pop(0) if self.replies else reply("完成")


class AssistantTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = patch.object(atlas_assistant, "ROOT", Path(temp.name))
        root.start()
        self.addCleanup(root.stop)
        # Run workers inline so tests see the finished state.
        start = patch.object(atlas_assistant, "_start", atlas_assistant._worker)
        start.start()
        self.addCleanup(start.stop)
        self.requests = []
        request = patch.object(atlas_assistant, "_request", self.fake_request)
        request.start()
        self.addCleanup(request.stop)

    def fake_request(self, method, path, query, body):
        self.requests.append((method, path, query, body))
        return 200, {"ok": True, "path": path}

    def run_turn(self, model, text="帮我做"):
        thread = atlas_assistant.create_thread()
        with patch.object(atlas_assistant.atlas_model, "chat", model):
            atlas_assistant.send_message(thread["id"], text, {"path": "/discover", "title": "发现项目"})
        return atlas_assistant.read_thread(thread["id"])

    def test_denied_and_uncatalogued_requests_are_refused(self):
        for method, path in [
            ("POST", "/api/settings/model/providers"),
            ("POST", "/api/settings/github"),
            ("GET", "/api/ask/threads"),
            ("POST", "/api/assistant/threads"),
            ("POST", "/api/factory/v1/anything"),
            ("GET", "http://example.com/api/projects"),
            ("GET", "/api/projects/../settings/model"),
        ]:
            with self.subTest(path=path), self.assertRaises(AssistantError):
                atlas_assistant.check_request(method, path)

    def test_settings_allow_model_choice_but_never_credentials(self):
        for method, path in [
            ("POST", "/api/settings/model/providers"),
            ("DELETE", "/api/settings/model/providers/openai"),
            ("POST", "/api/settings/model/import"),
            ("POST", "/api/settings/model/embedding"),
            ("POST", "/api/settings/github/test"),
        ]:
            with self.subTest(path=path), self.assertRaises(AssistantError):
                atlas_assistant.check_request(method, path)
        for path in ["/api/settings/model/default", "/api/settings/model/fallback",
                     "/api/settings/model/providers/openai/test"]:
            self.assertEqual(atlas_assistant.check_request("POST", path)[2]["risk"], "write")

    def test_every_write_route_has_a_body_hint_and_known_risk(self):
        for route in atlas_assistant.ROUTES:
            if route["method"] == "GET":
                self.assertEqual(route["risk"], "read")
            else:
                self.assertIn(route["risk"], {"write", "destructive"}, route["pattern"])
                self.assertIn("body", route, route["pattern"])
            if route["risk"] == "destructive":
                self.assertTrue(route.get("typed"), route["pattern"])

    def test_constant_confirmation_is_typed_by_the_operator(self):
        path = "/api/projects/prj_abc/backups/20261101T010203Z-0a1b2c3d.zip/restore"
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "POST", "path": path,
            "body": {"restore_id": "restore_" + "1" * 32, "confirm": "restore_to_new_store"}})]))
        thread = self.run_turn(model)
        pending = thread["pending"]
        self.assertEqual(pending["body"], {"restore_id": "restore_" + "1" * 32})
        self.assertEqual(pending["confirm_text"], "restore_to_new_store")
        with patch.object(atlas_assistant.atlas_model, "chat", FakeModel(reply("已恢复"))):
            atlas_assistant.decide(thread["id"], pending["id"], "approve", "restore_to_new_store")
        self.assertEqual(self.requests[-1][3], {"restore_id": "restore_" + "1" * 32,
                                               "confirm": "restore_to_new_store"})

    def test_encoded_paths_are_decoded_before_matching(self):
        with self.assertRaises(AssistantError):
            atlas_assistant.check_request("POST", "/api/settings%2Fmodel/providers")
        with self.assertRaises(AssistantError):
            atlas_assistant.check_request("GET", "/api/%61sk/threads")
        path, _, route = atlas_assistant.check_request("POST", "/api/oss/projects/12/favorite")
        self.assertEqual(route["risk"], "write")
        self.assertEqual(path, "/api/oss/projects/12/favorite")

    def test_reads_run_immediately_and_writes_wait_for_approval(self):
        model = FakeModel(
            reply(calls=[call("call_api", {"method": "GET", "path": "/api/oss/catalog", "query": {"q": "foam"}})]),
            reply(calls=[call("call_api", {"method": "POST", "path": "/api/oss/projects/7/favorite",
                                           "body": {"favorite": True}}, "c2")]),
            reply("我会收藏这个项目。"),
        )
        thread = self.run_turn(model)
        self.assertEqual(self.requests, [("GET", "/api/oss/catalog", "q=foam", None)])
        pending = thread["pending"]
        self.assertEqual(pending["body"], {"favorite": True})
        self.assertEqual(thread["messages"][-1]["status"], "awaiting_confirmation")
        # The page context reaches the model.
        self.assertIn("/discover", model.seen[0][0]["content"])

        follow = FakeModel(reply("已收藏。"))
        with patch.object(atlas_assistant.atlas_model, "chat", follow):
            atlas_assistant.decide(thread["id"], pending["id"], "approve")
        self.assertEqual(self.requests[-1], ("POST", "/api/oss/projects/7/favorite", "", {"favorite": True}))
        thread = atlas_assistant.read_thread(thread["id"])
        self.assertIsNone(thread["pending"])
        self.assertEqual([m["role"] for m in thread["messages"]], ["user", "assistant", "action", "assistant"])
        self.assertIn("执行结果", follow.seen[0][-1]["content"])

    def test_approval_runs_the_stored_request_once(self):
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "POST", "path": "/api/oss/projects/7/favorite", "body": {"favorite": True}})]))
        thread = self.run_turn(model)
        action_id = thread["pending"]["id"]
        with patch.object(atlas_assistant.atlas_model, "chat", FakeModel(reply("好"))):
            atlas_assistant.decide(thread["id"], action_id, "approve")
            with self.assertRaises(AssistantError):
                atlas_assistant.decide(thread["id"], action_id, "approve")
        self.assertEqual(len([r for r in self.requests if r[0] == "POST"]), 1)

    def test_reject_records_without_calling_the_api(self):
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "POST", "path": "/api/oss/projects/7/favorite", "body": {"favorite": True}})]))
        thread = self.run_turn(model)
        atlas_assistant.decide(thread["id"], thread["pending"]["id"], "reject")
        self.assertEqual(self.requests, [])
        self.assertEqual(atlas_assistant.read_thread(thread["id"])["messages"][-1]["decision"], "reject")

    def test_destructive_confirmation_must_be_typed_by_the_operator(self):
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "DELETE", "path": "/api/projects/prj_abc", "body": {"confirm": "prj_abc"}})]))
        thread = self.run_turn(model)
        pending = thread["pending"]
        self.assertEqual(pending["body"], {})
        self.assertEqual(pending["confirm_text"], "prj_abc")
        with self.assertRaises(AssistantError):
            atlas_assistant.decide(thread["id"], pending["id"], "approve")
        with self.assertRaises(AssistantError):
            atlas_assistant.decide(thread["id"], pending["id"], "approve", "prj_other")
        self.assertEqual(self.requests, [])
        with patch.object(atlas_assistant.atlas_model, "chat", FakeModel(reply("已删除"))):
            atlas_assistant.decide(thread["id"], pending["id"], "approve", "prj_abc")
        self.assertEqual(self.requests, [("DELETE", "/api/projects/prj_abc", "", {"confirm": "prj_abc"})])

    def test_pending_action_survives_a_restart(self):
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "POST", "path": "/api/oss/projects/7/favorite", "body": {"favorite": False}})]))
        thread = self.run_turn(model)
        atlas_assistant._RUNNING.clear()
        stored = json.loads((atlas_assistant.ROOT / f"{thread['id']}.json").read_text())
        self.assertEqual(stored["pending"]["path"], "/api/oss/projects/7/favorite")

    def test_new_message_supersedes_a_pending_action(self):
        model = FakeModel(reply(calls=[call("call_api", {
            "method": "POST", "path": "/api/oss/projects/7/favorite", "body": {"favorite": True}})]))
        thread = self.run_turn(model)
        with patch.object(atlas_assistant.atlas_model, "chat", FakeModel(reply("好的，不收藏了"))):
            atlas_assistant.send_message(thread["id"], "算了")
        thread = atlas_assistant.read_thread(thread["id"])
        self.assertIsNone(thread["pending"])
        self.assertEqual(self.requests, [])

    def test_navigate_accepts_app_pages_only(self):
        model = FakeModel(reply(calls=[call("navigate", {"path": "https://example.com"}),
                                       call("navigate", {"path": "/repos/42"}, "c2")]),
                          reply("已打开"))
        thread = self.run_turn(model)
        message = thread["messages"][-1]
        self.assertEqual(message["navigate"], "/repos/42")
        self.assertTrue(message["steps"][0]["error"])

    def test_large_results_are_clipped(self):
        def big(method, path, query, body):
            return 200, {"items": ["x" * 100] * 500}
        with patch.object(atlas_assistant, "_request", big):
            result = atlas_assistant.execute("GET", "/api/projects", "", None)
        self.assertTrue(result["result"]["truncated"])

    def test_request_line_is_ascii_encoded(self):
        sent = {}

        class Connection:
            def __init__(self, *args, **kwargs):
                pass

            def request(self, method, target, body=None, headers=None):
                target.encode("ascii")
                sent.update(method=method, target=target, headers=headers)

            def getresponse(self):
                class Response:
                    status = 200
                    def read(self, _):
                        return b"{}"
                    def getheader(self, _):
                        return "application/json"
                return Response()

            def close(self):
                pass

        with patch.object(atlas_assistant, "_request", REAL_REQUEST), \
                patch.object(atlas_assistant.http.client, "HTTPConnection", Connection):
            result = atlas_assistant.execute("GET", "/api/oss/catalog", "q=笔记&limit=1", None)
            self.assertTrue(result["ok"])
            self.assertEqual(sent["target"], "/api/oss/catalog?q=%E7%AC%94%E8%AE%B0&limit=1")
            atlas_assistant.execute("POST", "/api/oss/refresh", "", {})
            self.assertEqual(sent["headers"]["Content-Type"], "application/json")

    def test_old_conversations_are_pruned_at_the_limit(self):
        with patch.object(atlas_assistant, "MAX_THREADS", 2):
            first = atlas_assistant.create_thread()["id"]
            os.utime(atlas_assistant.ROOT / f"{first}.json", (1, 1))
            atlas_assistant.create_thread()
            atlas_assistant.create_thread()
        self.assertEqual(len(atlas_assistant.list_threads()), 2)
        with self.assertRaises(AssistantError):
            atlas_assistant.read_thread(first)

    def test_routes_list_by_area(self):
        routes = atlas_assistant.list_routes("projects")["routes"]
        self.assertTrue(routes)
        self.assertTrue(all("pattern" in item for item in routes))
        self.assertIn("error", atlas_assistant.list_routes("nope"))


if __name__ == "__main__":
    unittest.main()
