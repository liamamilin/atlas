"""Offline, bounded audit of a first-round pilot and its archived official sources."""
import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import re
import sqlite3
import tempfile
from unittest.mock import patch

from atlas_runtime import atomic_json
from oss_batch import BatchJobs
from oss_catalog import CatalogStore, canonical, decode_file, digest, plain_text
from oss_discovery import LicenseMatcher, ROOT


def audit_pilot(store, identifier, root=ROOT):
    root = Path(root)
    job = BatchJobs(store).get(identifier, detect_interruption=False)
    pilot = job.get("pilot", {})
    if job.get("scope") != "first_round" or not pilot.get("size"):
        raise ValueError("Not a first-round pilot")
    leaves = job["leaves"][:pilot["size"]]
    failures = []
    if job["status"] != "awaiting_acceptance" or any(leaf not in job.get("completed_leaves", []) for leaf in leaves):
        raise ValueError("Pilot has not finished")
    if job["leaf_errors"]:
        failures.append({"kind": "leaf_preparation", "leaves": list(job["leaf_errors"])})
    placeholders = ",".join("?" for _ in leaves)
    with store.connect() as con:
        selected = [dict(r) for r in con.execute("SELECT * FROM oss_batch_target WHERE job_id=?", (identifier,))]
        candidate_rows = [dict(r) for r in con.execute("SELECT * FROM oss_candidate WHERE leaf IN (" + placeholders + ")", leaves)]
        metadata = [json.loads(r[0])["meta"] for r in con.execute("SELECT data FROM oss_candidate")]
        scenarios = {r["id"]: json.loads(r["data"]) for r in con.execute("SELECT * FROM oss_scenario WHERE leaf IN (" + placeholders + ")", leaves)}
        selected_ids = {r["repository_id"] for r in selected if r["status"] in {"accepted", "partial"}}
        cards = {r["repository_id"]: json.loads(r["data"]) for r in con.execute("SELECT repository_id,data FROM oss_project")
                 if r["repository_id"] in selected_ids}
        matches = [json.loads(r[0]) for r in con.execute("SELECT m.data FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id WHERE s.leaf IN (" + placeholders + ")", leaves)]
        runs = [json.loads(r[1]) for r in con.execute("SELECT id,data FROM oss_run") if r[0] in set(job["runs"])]
    registry, raw_files, meta_by_id = {}, {}, {}
    for meta in metadata:
        meta_by_id[meta["id"]] = meta
        registry[("", digest(canonical(meta)))] = re.sub(r"\s+", " ", meta.get("description") or meta["full_name"])

    def register(file):
        if not file:
            return
        try:
            raw = decode_file(file)
        except (ValueError, UnicodeError):
            return
        key = (file.get("git_url", ""), digest(raw))
        registry[key] = plain_text(raw)
        raw_files[key] = file

    keys = {digest(canonical({"id": c["repository_id"], "pushed_at": c.get("pushed_at"), "branch": c.get("default_branch")}))
            for c in cards.values()}
    for row in candidate_rows:
        meta = json.loads(row["data"])["meta"]
        keys.add(digest(canonical({"id": meta["id"], "pushed_at": meta.get("pushed_at"), "branch": meta.get("default_branch")})))
    for key in keys:
        path = root / "sources" / (key + ".json")
        if path.exists():
            value = json.loads(path.read_text())
            for kind in ("readme", "license"):
                register(value.get(kind))
        path = root / "documentation" / (key + ".json")
        if path.exists():
            for doc in json.loads(path.read_text()).get("documents", []):
                register(doc["file"])

    quotes = 0
    def proof(value, repo, kind):
        nonlocal quotes
        key = (value.get("immutable_url", ""), value.get("source_sha256", value.get("sha256")))
        if key not in registry and key[0]:
            path = root / "evidence" / (digest(canonical({"url": key[0], "sha256": key[1]})) + ".json")
            if path.exists():
                register(json.loads(path.read_text())["file"])
        if key not in registry:
            failures.append({"repo": repo, "kind": kind, "error": "source_archive_missing"})
            return
        if value.get("excerpt"):
            quotes += 1
            if value["excerpt"].casefold() not in registry[key].casefold():
                failures.append({"repo": repo, "kind": kind, "error": "quote_mismatch"})
        elif kind not in {"source", "license"} and value.get("verification") not in {"source_based", "inferred"}:
            failures.append({"repo": repo, "kind": kind, "error": "missing_evidence_label"})

    checked_licenses = 0
    def cached_template(self, spdx):
        path = root / "spdx" / (spdx + ".json")
        return json.loads(path.read_text()) if path.exists() else None
    with patch.object(LicenseMatcher, "template", cached_template):
        for rid, card in cards.items():
            repo = card["full_name"]
            if card["github_url"] != "https://github.com/" + repo or not card.get("checked_at"):
                failures.append({"repo": repo, "error": "invalid_repository_or_time"})
            for field in ("summary", "scope", "positioning"):
                if card.get(field + "_evidence"):
                    proof(card[field + "_evidence"], repo, field)
            for feature in card["features"]:
                proof(feature["evidence"], repo, "feature")
            for source in card["sources"]:
                proof(source, repo, "source")
            license_source = card["license"].get("source")
            if license_source:
                proof(license_source, repo, "license")
            if card["license"]["status"] == "open_source":
                file = raw_files.get((license_source["immutable_url"], license_source["sha256"])) if license_source else None
                readme = next((raw_files.get((s["immutable_url"], s["sha256"])) for s in card["sources"] if s["kind"] == "readme"), None)
                result = LicenseMatcher(root).classify(meta_by_id[rid], file, readme)
                checked_licenses += 1
                if result["status"] != "open_source" or result["spdx"] != card["license"]["spdx"]:
                    failures.append({"repo": repo, "error": "license_recheck_mismatch"})
            elif card["license"]["status"] not in {"pending", "source_available"}:
                failures.append({"repo": repo, "error": "invalid_license_label"})
    for match in matches:
        proof(match["evidence"], str(match["scenario_id"]), "match")
        if match.get("applicability") not in {"direct", "conditional", "unverified"} or match.get("applicability") == "conditional" and not match.get("conditions"):
            failures.append({"scenario_id": match["scenario_id"], "error": "invalid_fit_label"})

    leaf_checks = []
    for leaf in leaves:
        targets = job["targets"][leaf]
        chosen = {t["repository_id"] for t in targets}
        deferred = [c for c in candidate_rows if c["leaf"] == leaf and c["repository_id"] not in chosen]
        valid = (len(targets) <= job["first_round_limit"] and all(t["status"] not in {"pending", "running"} for t in targets)
                 and all(c["status"] == "pending" for c in deferred) and len(deferred) == job["deferred_counts"][leaf])
        if not valid:
            failures.append({"leaf": leaf, "error": "quota_checkpoint_or_deferred_queue_mismatch"})
        leaf_checks.append({"leaf": leaf, "selected": len(targets), "deferred": len(deferred), "passed": valid,
                            "scenarios": sum(s.get("leaf") == leaf for s in scenarios.values())})
    source_windows = [r.get("source_timing") for r in runs if r.get("source_timing", {}).get("prefetched")]
    model_windows = [(t["started_at"], t["finished_at"]) for r in runs for t in r.get("model_tasks", {}).values()
                     if t.get("started_at") and t.get("finished_at")]
    overlap = sum(any(max(datetime.fromisoformat(s["started_at"]), datetime.fromisoformat(a)) <
                      min(datetime.fromisoformat(s["finished_at"]), datetime.fromisoformat(b)) for a, b in model_windows)
                  for s in source_windows)
    return {"job_id": identifier, "pilot_leaves": leaves, "structural_passed": not failures,
            "semantic_review_passed": False, "leaf_checks": leaf_checks, "failures": failures,
            "totals": {"selected": len(selected), "published_distinct_projects": len(cards), "scenarios": len(scenarios),
                       "quotes_checked": quotes, "verified_license_rechecks": checked_licenses,
                       "licenses": dict(Counter(c["license"]["status"] for c in cards.values())),
                       "applicability": dict(Counter(m["applicability"] for m in matches)),
                       "target_statuses": dict(Counter(t["status"] for t in selected)),
                       "deferred": sum(job["deferred_counts"].values()), "measured_overlapping_source_groups": overlap,
                       "model_calls": sum(r.get("model_calls", 0) for r in runs),
                       "source_fetches": sum(r.get("source_fetches", 0) for r in runs)},
            "note": "Source/quote/license checks are offline. Semantic review and isolated incremental verification must be recorded before release."}


def verify_incremental(store, identifier):
    job = BatchJobs(store).get(identifier, detect_interruption=False)
    leaves = job["leaves"][:job["pilot"]["size"]]
    with tempfile.TemporaryDirectory(prefix="atlas-first-round-replay-") as directory:
        path = Path(directory) / "copy.sqlite"
        with sqlite3.connect(store.path) as src, sqlite3.connect(path) as dst:
            src.backup(dst)
        copy = CatalogStore(path, bootstrap=False)
        selected = []
        with copy.connect() as con:
            for leaf in leaves:
                row = con.execute("SELECT p.repository_id,p.full_name FROM oss_leaf_project l JOIN oss_project p USING(repository_id) WHERE l.leaf=? ORDER BY p.repository_id LIMIT 1", (leaf,)).fetchone()
                if row:
                    selected.append((leaf, row["repository_id"], row["full_name"]))
        if not selected:
            return {"passed": False, "reason": "No real cards to replay"}
        copy.favorite(selected[0][1], True)
        def hashes():
            with copy.connect() as con:
                return {name: digest(canonical([list(r) for r in con.execute(query)])) for name, query in {
                    "projects": "SELECT repository_id FROM oss_project ORDER BY repository_id",
                    "memberships": "SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id",
                    "matches": "SELECT * FROM oss_match ORDER BY scenario_id,repository_id",
                    "favorites": "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id"}.items()}
        before = hashes()
        for leaf, rid, full_name in selected:
            card = copy.previous(full_name, leaf)
            with copy.connect() as con:
                copy._upsert(con, card, leaf)
        after = hashes()
        return {"passed": before == after, "production_database_modified": False,
                "real_cards_replayed": len(selected), "before": before, "after": after}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--job", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--db")
    args = parser.parse_args()
    store = CatalogStore(args.db, bootstrap=False)
    result = audit_pilot(store, args.job)
    result["incremental"] = verify_incremental(store, args.job)
    result["structural_passed"] = result["structural_passed"] and result["incremental"]["passed"]
    atomic_json(Path(args.output), result)
    print(canonical({"job_id": args.job, "structural_passed": result["structural_passed"], "totals": result["totals"], "failures": result["failures"][:10]}))


if __name__ == "__main__":
    main()
