"""Contract tests for repository identity, evidence, partial failures and updates."""
import copy
import json
from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from oss_catalog import (CatalogError, CatalogStore, DATA, GitHub, PILOT_LEAF,
                         build_card, curation_digest, license_info, manifest)


class SavedSources:
    def __init__(self):
        self.cards = {p["full_name"].lower(): p for p in json.loads((DATA / "pilot.snapshot.json").read_text())["projects"]}
        self.fail = set()

    def collect(self, candidate, previous=None):
        if candidate["repo"] in self.fail:
            raise CatalogError("测试网络中断", 502)
        return copy.deepcopy(self.cards[candidate["repo"].lower()])


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "catalog.sqlite"
        self.store = CatalogStore(self.path, bootstrap=False)
        self.client = SavedSources()

    def test_first_intake_and_repeated_refresh_preserve_identity_and_favorite(self):
        first = self.store.refresh(self.client)
        self.assertEqual((first["created"], first["failed"]), (7, 0))
        first_data = self.store.catalog(PILOT_LEAF)
        self.assertEqual([s["project_count"] for s in first_data["scenarios"]], [5, 3, 4])
        project = first_data["projects"][0]
        self.store.favorite(project["repository_id"], True)
        second = self.store.refresh(self.client)
        self.assertEqual((second["created"], second["updated"], second["unchanged"]), (0, 0, 7))
        reopened = CatalogStore(self.path, bootstrap=False).catalog(favorites=True)
        self.assertEqual([p["repository_id"] for p in reopened["projects"]], [project["repository_id"]])
        self.assertEqual(sum(s["project_count"] for s in self.store.catalog()["scenarios"]), 12)

    def test_partial_failure_retains_last_success_and_verification_time(self):
        self.store.refresh(self.client)
        before = self.store.previous("logseq/logseq")
        self.client.fail.add("logseq/logseq")
        run = self.store.refresh(self.client)
        self.assertEqual((run["status"], run["failed"], run["unchanged"]), ("partial", 1, 6))
        self.assertEqual(self.store.previous("logseq/logseq"), before)
        self.assertEqual(len(self.store.catalog()["projects"]), 7)

    def test_update_replaces_associations_and_preserves_other_leaves(self):
        self.store.refresh(self.client)
        card = self.client.cards["foambubble/foam"]
        with self.store.connect() as con:
            con.execute("INSERT INTO oss_scenario VALUES ('other','other-leaf',0,?)", (json.dumps({"id": "other", "name": "Other", "description": "Other"}),))
            con.execute("INSERT INTO oss_match VALUES ('other',?,?)", (card["repository_id"], json.dumps({"scenario_id": "other", "reason": "Other", "evidence": {}})))
        card["matches"] = card["matches"][:1]
        card["summary"] += " updated"
        run = self.store.refresh(self.client)
        self.assertEqual(run["updated"], 1)
        with self.store.connect() as con:
            ids = {r[0] for r in con.execute("SELECT scenario_id FROM oss_match WHERE repository_id=?", (card["repository_id"],))}
        self.assertEqual(ids, {"other", "pkm-network"})

    def test_repository_transfer_uses_numeric_id(self):
        self.store.refresh(self.client)
        card = self.client.cards["foambubble/foam"]
        self.store.favorite(card["repository_id"], True)
        card["full_name"] = "new-owner/foam"
        self.store.refresh(self.client)
        self.assertEqual(len(self.store.catalog()["projects"]), 7)
        self.assertTrue(self.store.catalog(favorites=True)["projects"][0]["favorite"])

    def test_search_scenario_license_and_favorite_filters(self):
        self.store.refresh(self.client)
        self.assertEqual(len(self.store.catalog(q="Foam")["projects"]), 1)
        self.assertEqual(len(self.store.catalog(q="双向链接")["projects"]), 1)
        self.assertEqual(len(self.store.catalog(scenario="pkm-plaintext")["projects"]), 3)
        self.assertEqual(len(self.store.catalog(license_status="open_source")["projects"]), 7)
        self.assertEqual(self.store.catalog(license_status="pending")["projects"], [])
        self.assertEqual(self.store.catalog(leaf="unknown")["projects"], [])

    def test_bootstrap_is_once_only_and_does_not_replace_personal_state(self):
        store = CatalogStore(self.path)
        self.assertEqual(len(store.catalog(PILOT_LEAF)["projects"]), 7)
        card = store.catalog(PILOT_LEAF)["projects"][0]
        store.favorite(card["repository_id"], True)
        self.assertEqual(len(CatalogStore(self.path).catalog(favorites=True)["projects"]), 1)

    def test_pagination_preserves_counts_and_never_loses_projects(self):
        self.store.refresh(self.client)
        complete = self.store.catalog(PILOT_LEAF)
        pages = [self.store.catalog(PILOT_LEAF, limit=3, offset=offset) for offset in (0, 3, 6)]
        self.assertEqual([p["repository_id"] for page in pages for p in page["projects"]],
                         [p["repository_id"] for p in complete["projects"]])
        for page in pages:
            self.assertEqual(page["pagination"]["total"], 7)
            self.assertEqual(page["scenarios"], complete["scenarios"])
        self.assertEqual([page["pagination"]["has_more"] for page in pages], [True, True, False])
        self.assertEqual(self.store.catalog(limit=3, offset=999)["projects"], [])

    def test_overview_is_small_and_does_not_read_candidate_material(self):
        self.store.refresh(self.client)
        complete = self.store.catalog()
        with patch.object(self.store, "candidates", side_effect=AssertionError("overview must not read candidates")):
            overview = self.store.catalog(overview=True)
        self.assertEqual(overview["projects"], [])
        self.assertEqual(overview["stats"], {"projects": 7, "scenarios": 3, "leaves": 1, "favorites": 0})
        self.assertEqual(overview["supported_leaves"], [{"slug": PILOT_LEAF, "name": "个人知识管理应用", "mode": "curated", "project_count": 7}])
        self.assertEqual(overview["scenarios"], complete["scenarios"])
        self.assertLess(len(json.dumps(overview)), len(json.dumps(complete)) / 5)

    def test_pagination_happens_after_filtering_and_sorting(self):
        self.store.refresh(self.client)
        complete = self.store.catalog()
        chosen = complete["projects"][-1]
        self.store.favorite(chosen["repository_id"], True)
        data = self.store.catalog(favorites=True, limit=1)
        self.assertEqual(data["projects"][0]["repository_id"], chosen["repository_id"])
        self.assertEqual(data["pagination"]["total"], 1)
        with self.store.connect() as con:
            card = json.loads(con.execute("SELECT data FROM oss_project WHERE repository_id=?", (chosen["repository_id"],)).fetchone()[0])
            card["checked_at"] = "2099-01-01T00:00:00+00:00"
            con.execute("UPDATE oss_project SET data=? WHERE repository_id=?", (json.dumps(card), chosen["repository_id"]))
        self.assertEqual(self.store.catalog(sort="recent", limit=1)["projects"][0]["repository_id"], chosen["repository_id"])
        self.assertEqual(self.store.catalog(q="Foam", limit=1)["pagination"]["total"], 1)

    def test_index_sees_writes_from_other_connections_and_favorites_do_not_rebuild(self):
        from oss_catalog import _CatalogIndex
        self.store.refresh(self.client)
        self.assertEqual(self.store.catalog(q="Foam", limit=5)["pagination"]["total"], 1)
        with self.store.connect() as con:
            con.execute("DELETE FROM oss_match WHERE repository_id IN (SELECT repository_id FROM oss_project WHERE full_name LIKE '%foam%')")
            con.execute("DELETE FROM oss_leaf_project WHERE repository_id IN (SELECT repository_id FROM oss_project WHERE full_name LIKE '%foam%')")
        self.assertEqual(self.store.catalog(q="Foam", limit=5)["pagination"]["total"], 0)
        chosen = self.store.catalog(limit=1)["projects"][0]
        with patch.object(_CatalogIndex, "build", side_effect=AssertionError("favorite must not rebuild")):
            self.store.favorite(chosen["repository_id"], True)
            data = self.store.catalog(favorites=True, limit=5)
        self.assertEqual([p["repository_id"] for p in data["projects"]], [chosen["repository_id"]])

    def test_paged_listing_without_type_reads_no_candidate_material(self):
        self.store.refresh(self.client)
        data = self.store.catalog(limit=3)
        self.assertEqual(data["discovery"]["items"], [])
        shown = {m["scenario_id"] for p in data["projects"] for m in p["matches"]}
        self.assertEqual({s["id"] for s in data["scenarios"]}, shown)

    def test_invalid_pagination_and_sort_fail_with_a_client_error(self):
        from oss_catalog import dispatch
        for kwargs in ({"limit": 0}, {"limit": 101}, {"limit": True}, {"offset": -1}, {"sort": "unknown"}):
            with self.subTest(kwargs=kwargs), self.assertRaises(CatalogError):
                self.store.catalog(**kwargs)
        with patch("oss_catalog.CatalogStore", return_value=self.store):
            for query in ("limit=no", "offset=1.5", "limit=-1", "sort=unknown"):
                with self.subTest(query=query), self.assertRaises(CatalogError):
                    dispatch("GET", "/api/oss/catalog", query)

    def test_evidence_is_required_and_license_unknown_is_pending(self):
        import base64
        candidate = manifest()["projects"][0]
        file = {"encoding": "base64", "content": base64.b64encode(b"No evidence").decode(),
                "sha": "a" * 40, "path": "README.md", "html_url": "https://github.com/x/y/blob/main/README.md", "git_url": "https://api.github.com/repos/x/y/git/blobs/" + "a" * 40}
        with self.assertRaisesRegex(CatalogError, "README"):
            build_card(candidate, {"id": 1, "full_name": "x/y"}, file, None, {})
        self.assertEqual(license_info("x/y", {"license": {"spdx_id": "MIT"}}, file)["status"], "pending")
        self.assertEqual(license_info("x/y", {}, None)["status"], "pending")
        # An unreviewed change to a known project's license must lose its verified label.
        self.assertEqual(license_info("foambubble/foam", {"license": {"spdx_id": "MIT"}}, file)["status"], "pending")

    def test_source_available_is_separate_from_open_source(self):
        import base64
        from oss_catalog import digest
        body = "A source-available license with additional restrictions"
        file = {"encoding": "base64", "content": base64.b64encode(body.encode()).decode(), "sha": "a" * 40,
                "path": "LICENSE", "html_url": "https://github.com/x/y/blob/main/LICENSE", "git_url": "https://api.github.com/repos/x/y/git/blobs/" + "a" * 40}
        reviews = {"x/y": {"sha256": digest(body), "spdx": "BUSL-1.1", "note": "Additional restrictions", "reviewed_at": "2026-10-23"}}
        original = Path.read_text
        def read(path, *args, **kwargs):
            return json.dumps(reviews) if path.name == "license-reviews.json" else original(path, *args, **kwargs)
        with patch.object(Path, "read_text", read):
            self.assertEqual(license_info("x/y", {}, file)["status"], "source_available")

    def test_unchanged_repository_reuses_evidence_but_refreshes_metadata(self):
        candidate = manifest()["projects"][0]
        previous = copy.deepcopy(self.client.cards[candidate["repo"].lower()])
        meta = {"id": previous["repository_id"], "full_name": previous["full_name"], "html_url": previous["github_url"],
                "pushed_at": previous["pushed_at"], "default_branch": previous["default_branch"]}
        with patch.object(GitHub, "get", return_value=meta) as get:
            result = GitHub().collect(candidate, previous)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(result["sources"], previous["sources"])
        self.assertNotEqual(result["checked_at"], previous["checked_at"])
        self.assertEqual(previous["curation_digest"], curation_digest(candidate))

    def test_concurrent_refresh_rejected_and_interrupted_run_recoverable(self):
        lock = self.store._lock()
        try:
            with self.assertRaises(CatalogError) as caught:
                self.store.refresh(self.client)
            self.assertEqual(caught.exception.status, 409)
        finally:
            lock.close()
        run = {"id": "oss_" + "a" * 32, "leaf": PILOT_LEAF, "status": "running"}
        self.store._save_run(run)
        self.assertEqual(self.store.run(run["id"])["status"], "interrupted")
        self.store._save_run(run)
        self.store.refresh(self.client)
        self.assertEqual(self.store.run(run["id"])["status"], "interrupted")

    def test_invalid_association_rolls_back_the_entire_card(self):
        self.store.refresh(self.client)
        before = self.store.previous("logseq/logseq")
        card = copy.deepcopy(before)
        card["summary"] = "should roll back"
        card["matches"][0]["scenario_id"] = "nonexistent"
        with self.assertRaises(Exception):
            with self.store.connect() as con:
                self.store._upsert(con, card)
        self.assertEqual(self.store.previous("logseq/logseq"), before)

    def test_all_published_cards_have_official_evidence_and_verified_licenses(self):
        self.store.refresh(self.client)
        for card in self.store.catalog()["projects"]:
            self.assertEqual(card["license"]["status"], "open_source")
            self.assertTrue(card["license"]["source"]["sha256"])
            for fact in [card["summary_evidence"], card["scope_evidence"], *(f["evidence"] for f in card["features"]), *(m["evidence"] for m in card["matches"])]:
                self.assertTrue(fact["excerpt"])
                self.assertTrue(fact["source_url"].startswith("https://github.com/"))
                self.assertTrue(fact["immutable_url"].startswith("https://api.github.com/repos/"))


if __name__ == "__main__":
    unittest.main()
