"""Verify real collected licenses and replay sample cards in an isolated database."""
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[2]
PACK = REPO / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, decode_file, digest
from oss_discovery import ROOT, LicenseMatcher
from oss_batch import BatchJobs

LEAVES = ["bookmark-manager", "calendar-application", "expense-tracking-application"]
store = CatalogStore(bootstrap=False)
files = {}
for directory in ("sources", "documentation", "evidence"):
    for path in (ROOT / directory).glob("*.json"):
        data = json.loads(path.read_text())
        entries = ([data.get("readme"), data.get("license")] if directory == "sources" else
                   [data["file"]] if directory == "evidence" else [d["file"] for d in data.get("documents", [])])
        for file in entries:
            if file:
                try:
                    files[(file["git_url"], digest(decode_file(file)))] = file
                except (ValueError, UnicodeError):
                    pass


def cached_template(self, identifier):
    path = ROOT / "spdx" / (identifier + ".json")
    return json.loads(path.read_text()) if path.exists() else None


license_checks = []
with patch.object(LicenseMatcher, "template", cached_template):
    for leaf in LEAVES:
        metadata = {c["repository_id"]: c["data"]["meta"] for c in store.candidates(leaf)}
        for card in store.catalog(leaf)["projects"]:
            if card["license"]["status"] != "open_source":
                continue
            source = card["license"]["source"]
            file = files[(source["immutable_url"], source["sha256"])]
            readme = next((files[(s["immutable_url"], s["sha256"])] for s in card["sources"] if s["kind"] == "readme"), None)
            result = LicenseMatcher(ROOT).classify(metadata[card["repository_id"]], file, readme)
            assert result["status"] == "open_source", card["full_name"]
            assert result["spdx"] == card["license"]["spdx"], card["full_name"]
            license_checks.append({"leaf": leaf, "repo": card["full_name"], "spdx": result["spdx"], "result": "passed"})
(Path(__file__).parent / "LICENSE_CHECKS.json").write_text(json.dumps(license_checks, ensure_ascii=False, indent=2) + "\n")

samples = json.loads((Path(__file__).parent / "SAMPLE_SOURCES.json").read_text())
with tempfile.TemporaryDirectory(prefix="atlas-incremental-acceptance-") as directory:
    copied = Path(directory) / "catalog.sqlite"
    with sqlite3.connect(store.path) as source, sqlite3.connect(copied) as destination:
        source.backup(destination)
    isolated = CatalogStore(copied, bootstrap=False)
    first = isolated.previous(samples[0]["full_name"], samples[0]["leaf"])
    isolated.favorite(first["repository_id"], True)

    def state():
        with isolated.connect() as con:
            return {"projects": con.execute("SELECT COUNT(*) FROM oss_project").fetchone()[0],
                    "memberships": con.execute("SELECT COUNT(*) FROM oss_leaf_project").fetchone()[0],
                    "matches": digest(canonical([list(r) for r in con.execute("SELECT * FROM oss_match ORDER BY scenario_id,repository_id")])),
                    "favorites": digest(canonical([list(r) for r in con.execute("SELECT repository_id,favorite FROM oss_project ORDER BY repository_id")])),
                    "runs": con.execute("SELECT COUNT(*) FROM oss_run").fetchone()[0]}
    before = state()
    for sample in samples:
        card = isolated.previous(sample["full_name"], sample["leaf"])
        with isolated.connect() as con:
            isolated._upsert(con, card, sample["leaf"])
    identifier = json.loads((Path(__file__).parent / "JOB.json").read_text())["id"]
    result = BatchJobs(isolated, worker=lambda *a, **kw: (_ for _ in ()).throw(AssertionError("Completed job replayed"))).resume(identifier)
    after = state()
    assert before == after, (before, after)
    assert result["status"] == "completed" and result["processed"] == 834
    with patch("oss_batch.ROOT", Path(directory) / "batch-state"), \
            patch("oss_discovery.Model.ask", side_effect=AssertionError("Terminal candidates must not call the model")), \
            patch("oss_workflow.GitHub.get", side_effect=AssertionError("Existing-only replay must not fetch sources")):
        replay = BatchJobs(isolated).create(LEAVES, existing_only=True)
    replay_state = state()
    assert replay["status"] == "completed" and replay["processed"] == replay["total"] == 0
    assert {k: v for k, v in replay_state.items() if k != "runs"} == {k: v for k, v in after.items() if k != "runs"}
    report = {"result": "passed", "sample_cards_replayed": len(samples), "duplicate_projects_added": 0,
              "before": before, "after": after, "production_database_modified": False,
              "completed_job_resume_started_new_runs": False, "license_claims_rechecked": len(license_checks),
              "new_existing_only_batch": {"status": replay["status"], "total": replay["total"], "processed": replay["processed"], "model_calls": 0, "source_fetches": 0}}
    (Path(__file__).parent / "INCREMENTAL.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"result": "passed", "sample_cards": len(samples), "licenses_checked": len(license_checks)}, ensure_ascii=False))
