"""Offline final audit of the frozen campaign; production is opened read-only.

This does not change the pilot gate, resume a job, or make upstream requests.
"""
from bisect import bisect_left
import argparse
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys
import tempfile

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import CatalogStore, canonical, decode_file, digest, plain_text
from oss_discovery import LicenseMatcher

JOB = "batch_4812ef3db57543c3acc1871b8ea5ba6e"
DB = PACK / "atlas/oss-catalog.sqlite"
ROOT = PACK / "atlas/oss-discovery"


def readonly(path=DB):
    suffix = "?mode=ro" if path == DB else "?mode=ro&immutable=1"
    con = sqlite3.connect("file:" + str(path) + suffix, uri=True)
    con.row_factory = sqlite3.Row
    return con


def table_hash(con, query):
    h = hashlib.sha256()
    for row in con.execute(query):
        h.update(canonical(list(row)).encode())
        h.update(b"\n")
    return h.hexdigest()


@lru_cache(maxsize=16)
def cached_template(identifier):
    path = ROOT / "spdx" / (identifier + ".json")
    return json.loads(path.read_text()) if path.exists() else None


class OfflineMatcher(LicenseMatcher):
    def template(self, identifier):
        return cached_template(identifier)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=BASE)
    output = parser.parse_args().output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    con = readonly()
    con.execute("BEGIN")
    job = json.loads(con.execute("SELECT data FROM oss_batch_job WHERE id=?", (JOB,)).fetchone()[0])
    manifest = json.loads((BASE / "MANIFEST.json").read_text())
    expected = [v["slug"] for v in manifest["leaves"]]
    failures = []

    def fail(kind, **detail):
        failures.append({"kind": kind, **detail})

    leaves = [dict(r) for r in con.execute("SELECT * FROM oss_batch_leaf WHERE job_id=? ORDER BY position", (JOB,))]
    if expected != job["leaves"] or expected != [r["leaf"] for r in leaves]:
        fail("frozen_manifest_mismatch")
    if job["status"] not in {"completed", "partial"} or set(job["completed_leaves"]) != set(expected):
        fail("campaign_not_finished")
    if job["leaf_errors"]:
        fail("leaf_errors", count=len(job["leaf_errors"]))
    if (job["first_round_limit"], job["batch_size"], job["source_pipeline"]) != (60, 16, True):
        fail("campaign_configuration_mismatch")
    accepted_path = ROOT / "acceptance" / (JOB + ".json")
    if digest(accepted_path.read_text()) != job["pilot"]["report"]["report_sha256"]:
        fail("accepted_pilot_file_changed")
    target_counts = dict(con.execute("SELECT status,COUNT(*) FROM oss_batch_target WHERE job_id=? GROUP BY status", (JOB,)))
    selected = sum(target_counts.values())
    if any(target_counts.get(v) for v in ["pending", "running"]):
        fail("unfinished_selected_targets")
    leaf_checks = []
    for row in leaves:
        leaf = row["leaf"]
        chosen = con.execute("SELECT COUNT(*) FROM oss_batch_target WHERE job_id=? AND leaf=?", (JOB, leaf)).fetchone()[0]
        deferred = con.execute("SELECT COUNT(*),SUM(c.status!='pending') FROM oss_candidate c WHERE c.leaf=? AND NOT EXISTS (SELECT 1 FROM oss_batch_target t WHERE t.job_id=? AND t.leaf=c.leaf AND t.repository_id=c.repository_id)", (leaf, JOB)).fetchone()
        candidates = con.execute("SELECT COUNT(*) FROM oss_candidate WHERE leaf=?", (leaf,)).fetchone()[0]
        valid = (row["state"] == "first_round_done" and chosen == row["selected_count"] <= 60
                 and deferred[0] == row["deferred_count"] and not deferred[1]
                 and candidates == row["candidate_total"] == chosen + deferred[0])
        if not valid:
            fail("leaf_limit_or_pending_mismatch", leaf=leaf)
        leaf_checks.append({"leaf": leaf, "position": row["position"], "selected": chosen,
                            "candidate_total": candidates, "deferred_pending": deferred[0], "passed": valid})
    print(canonical({"stage": "coverage", "leaves": len(leaves), "selected": selected, "failures": len(failures)}), flush=True)

    metadata, meta_by_id, archive_keys_by_id = {}, {}, {}
    provenance = Counter()
    scope_set = set(expected)
    for row in con.execute("SELECT leaf,data FROM oss_candidate"):
        value = json.loads(row["data"])
        meta = value["meta"]
        metadata[digest(canonical(meta))] = re.sub(r"\s+", " ", meta.get("description") or meta["full_name"])
        meta_by_id[meta["id"]] = {k: meta.get(k) for k in ["id", "full_name", "license"]}
        archive_keys_by_id.setdefault(meta["id"], set()).add(digest(canonical({
            "id": meta["id"], "pushed_at": meta.get("pushed_at"), "branch": meta.get("default_branch")})))
        if row["leaf"] in scope_set:
            provenance["candidates"] += 1
            provenance["with_real_search_hits"] += bool(value.get("search_hits") and value.get("search_verified_at"))
            provenance["private"] += bool(meta.get("private"))
    if provenance["candidates"] != provenance["with_real_search_hits"] or provenance["private"]:
        fail("candidate_discovery_provenance", counts=dict(provenance))

    project_ids = {r[0] for r in con.execute("SELECT DISTINCT repository_id FROM oss_batch_target WHERE job_id=? AND status IN ('accepted','partial')", (JOB,))}
    matches_by_id = {}
    for row in con.execute("SELECT m.repository_id,m.data FROM oss_match m JOIN oss_scenario s ON s.id=m.scenario_id JOIN oss_batch_leaf b ON b.leaf=s.leaf WHERE b.job_id=?", (JOB,)):
        matches_by_id.setdefault(row[0], []).append(json.loads(row[1]))
    registry, raw_files = {}, {}
    counters = Counter()
    license_counts, completeness, project_types = Counter(), Counter(), Counter()
    matcher = OfflineMatcher(ROOT)

    def register(file):
        if not file:
            return
        try:
            raw = decode_file(file)
        except (ValueError, UnicodeError):
            # GitHub can archive an unavailable/non-text response. It is not
            # evidence; any card referencing it still fails proof() below.
            counters["unreadable_archived_responses"] += 1
            return
        key = (file.get("git_url", ""), digest(raw))
        registry[key], raw_files[key] = plain_text(raw), file

    def archive(path, documentation=False):
        if not path.exists():
            return
        value = json.loads(path.read_text())
        if documentation:
            for doc in value.get("documents", []):
                register(doc.get("file"))
        else:
            for field in ["readme", "license"]:
                register(value.get(field))

    def proof(value, repository, kind):
        key = (value.get("immutable_url", ""), value.get("source_sha256", value.get("sha256")))
        if not key[0] and key[1] in metadata:
            text = metadata[key[1]]
        else:
            if key not in registry and key[0]:
                path = ROOT / "evidence" / (digest(canonical({"url": key[0], "sha256": key[1]})) + ".json")
                if path.exists():
                    register(json.loads(path.read_text())["file"])
            text = registry.get(key)
        if text is None:
            fail("source_archive_missing", repository=repository, evidence_kind=kind, source_sha256=key[1])
            return
        counters["evidence_references_checked"] += 1
        if value.get("excerpt"):
            counters["quotes_checked"] += 1
            if value["excerpt"].casefold() not in text.casefold():
                fail("quote_mismatch", repository=repository, evidence_kind=kind, source_sha256=key[1])
        elif kind not in {"source", "license"} and value.get("verification") not in {"source_based", "inferred"}:
            fail("missing_evidence_label", repository=repository, evidence_kind=kind)

    for row in con.execute("SELECT repository_id,data FROM oss_project ORDER BY repository_id"):
        rid = row["repository_id"]
        if rid not in project_ids:
            continue
        card = json.loads(row["data"])
        registry.clear(); raw_files.clear()
        key = digest(canonical({"id": rid, "pushed_at": card.get("pushed_at"), "branch": card.get("default_branch")}))
        # Shared repositories may retain older matches from another leaf.
        # Resolve every archived version referenced by its frozen candidates.
        for version_key in archive_keys_by_id.get(rid, set()) | {key}:
            archive(ROOT / "sources" / (version_key + ".json"))
            archive(ROOT / "documentation" / (version_key + ".json"), True)
        repo = card["full_name"]
        if card["github_url"] != "https://github.com/" + repo or not card.get("checked_at"):
            fail("invalid_repository_or_time", repository=repo)
        for field in ["summary", "scope", "positioning"]:
            if card.get(field + "_evidence"):
                proof(card[field + "_evidence"], repo, field)
            else:
                fail("missing_fact_evidence", repository=repo, field=field)
        for feature in card["features"]:
            proof(feature["evidence"], repo, "feature")
        for source in card["sources"]:
            proof(source, repo, "source")
        license_value = card["license"]
        license_source = license_value.get("source")
        if license_source:
            proof(license_source, repo, "license")
        if license_value.get("restriction_evidence"):
            proof(license_value["restriction_evidence"], repo, "license_restriction")
        if license_value["status"] == "open_source":
            file = raw_files.get((license_source["immutable_url"], license_source["sha256"])) if license_source else None
            readme = next((raw_files.get((s.get("immutable_url", ""), s["sha256"])) for s in card["sources"] if s["kind"] == "readme"), None)
            result = matcher.classify(meta_by_id[rid], file, readme)
            counters["verified_license_rechecks"] += 1
            if result["status"] != "open_source" or result["spdx"] != license_value["spdx"]:
                fail("license_recheck_mismatch", repository=repo)
        elif license_value["status"] not in {"pending", "source_available"}:
            fail("invalid_license_label", repository=repo)
        if license_value["status"] == "pending" and (license_value.get("spdx") or not license_value.get("note")):
            fail("unknown_license_not_labeled", repository=repo)
        for match in matches_by_id.get(rid, []):
            proof(match["evidence"], repo, "match")
            if match.get("applicability") not in {"direct", "conditional", "unverified"} or match.get("applicability") == "conditional" and not match.get("conditions"):
                fail("invalid_applicability_label", repository=repo, scenario_id=match["scenario_id"])
        if card.get("generation_method") == "metadata" or card.get("completeness") == "partial":
            if not (card.get("missing_fields") or card.get("collection_notes")) and not any(m.get("applicability") == "unverified" for m in card.get("matches", [])):
                fail("partial_without_labeled_limits", repository=repo)
        license_counts[license_value["status"]] += 1
        completeness[card.get("completeness", "unspecified")] += 1
        project_types[card.get("project_type", "unspecified")] += 1
        counters["projects_checked"] += 1
        if counters["projects_checked"] % 10000 == 0:
            print(canonical({"stage": "sources", "projects": counters["projects_checked"], "failures": len(failures)}), flush=True)
    if counters["projects_checked"] != len(project_ids):
        fail("published_target_project_missing")
    missing_membership = con.execute("SELECT COUNT(*) FROM oss_batch_target t WHERE t.job_id=? AND t.status IN ('accepted','partial') AND NOT EXISTS (SELECT 1 FROM oss_leaf_project l WHERE l.leaf=t.leaf AND l.repository_id=t.repository_id)", (JOB,)).fetchone()[0]
    if missing_membership:
        fail("missing_leaf_membership", count=missing_membership)
    (output / "FINAL_SOURCE_CHECKS.json").write_text(json.dumps({"job_id": JOB,
        "counters": dict(counters), "failures": failures, "licenses": dict(license_counts),
        "completeness": dict(completeness), "project_types": dict(project_types)}, ensure_ascii=False, indent=2) + "\n")

    runs, model_receipts, source_windows, model_windows = [], Counter(), [], []
    run_ids = set(job["runs"])
    for row in con.execute("SELECT id,data FROM oss_run"):
        if row["id"] not in run_ids:
            continue
        run = json.loads(row["data"]);runs.append(run)
        for receipt in run.get("model_receipts", []):
            model_receipts[receipt.get("provider", "") + " / " + receipt.get("model", "")] += 1
        if run.get("source_timing", {}).get("prefetched"):
            source_windows.append(run["source_timing"])
        model_windows.extend((v["started_at"], v["finished_at"]) for v in run.get("model_tasks", {}).values() if v.get("started_at") and v.get("finished_at"))
    model_windows.sort()
    starts, prefix_ends = [], []
    for start, end in model_windows:
        starts.append(start);prefix_ends.append(max(end, prefix_ends[-1] if prefix_ends else end))
    overlap = 0
    for window in source_windows:
        idx = bisect_left(starts, window["finished_at"]) - 1
        overlap += idx >= 0 and prefix_ends[idx] > window["started_at"]
    max_workers = max((v.get("concurrency", {}).get("model_workers", 0) for v in runs), default=0)
    if max_workers != 4 or not overlap:
        fail("pipeline_not_proven", max_workers=max_workers, overlapping_groups=overlap)

    preservation = {}
    backup = Path("/private/tmp/atlas-before-first-round-2026-10-26.sqlite")
    with readonly(backup) as old:
        for name, query in {
            "repository_ids": "SELECT repository_id FROM oss_project",
            "memberships": "SELECT leaf,repository_id FROM oss_leaf_project",
            "favorites": "SELECT repository_id FROM oss_project WHERE favorite=1",
            "matches": "SELECT scenario_id,repository_id,data FROM oss_match",
        }.items():
            before = {tuple(r) for r in old.execute(query)}
            after = {tuple(r) for r in con.execute(query)}
            preservation[name] = {"before_count": len(before), "missing_after": len(before - after), "passed": before <= after}
            if before - after:
                fail("pre_campaign_data_not_preserved", table=name, count=len(before - after))
    favorite_before = table_hash(con, "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id")
    con.close()
    print(canonical({"stage": "incremental_copy", "source_failures": len(failures)}), flush=True)
    with tempfile.TemporaryDirectory(prefix="atlas-final-replay-") as directory:
        copy_path = Path(directory) / "copy.sqlite"
        with readonly() as src, sqlite3.connect(copy_path) as dst:
            src.backup(dst)
        copy = object.__new__(CatalogStore);copy.path = copy_path
        replay = []
        with copy.connect() as dst:
            for leaf in expected:
                row = dst.execute("SELECT p.repository_id,p.full_name FROM oss_project p JOIN oss_leaf_project l USING(repository_id) WHERE l.leaf=? ORDER BY p.repository_id LIMIT 1", (leaf,)).fetchone()
                if row:
                    replay.append((leaf, row[0], row[1]))
            dst.execute("UPDATE oss_project SET favorite=1 WHERE repository_id=?", (replay[0][1],))
        def hashes():
            with copy.connect() as dst:
                return {name: table_hash(dst, query) for name, query in {
                    "project_keys": "SELECT repository_id,full_name FROM oss_project ORDER BY repository_id",
                    "memberships": "SELECT * FROM oss_leaf_project ORDER BY leaf,repository_id",
                    "matches": "SELECT * FROM oss_match ORDER BY scenario_id,repository_id",
                    "favorites": "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id",
                }.items()}
        before = hashes()
        outcomes = Counter()
        for leaf, rid, repo in replay:
            card = copy.previous(repo, leaf)
            with copy.connect() as dst:
                outcomes[copy._upsert(dst, card, leaf)] += 1
        after = hashes()
        incremental = {"passed": before == after and bool(replay), "production_database_modified": False,
                       "real_cards_replayed": len(replay), "distinct_repositories": len({r[1] for r in replay}),
                       "leaves_with_no_published_card": len(expected) - len(replay), "outcomes": dict(outcomes), "before": before, "after": after}
        if not incremental["passed"]:
            fail("incremental_preservation_mismatch")
    with readonly() as final:
        if table_hash(final, "SELECT repository_id,favorite FROM oss_project ORDER BY repository_id") != favorite_before:
            fail("production_favorites_changed_during_audit")
    result = {"job_id": JOB, "checked_at": datetime.now(timezone.utc).isoformat(), "scope": "all_frozen_first_round_leaves",
              "structural_passed": not failures, "semantic_review_passed": False,
              "production_status": job["status"], "finished_at": job["finished_at"],
              "manifest_sha256": digest((BASE / "MANIFEST.json").read_text()), "frozen_manifest_exact": expected == job["leaves"] == [r["leaf"] for r in leaves],
              "leaf_checks": leaf_checks, "failures": failures, "incremental": incremental, "pre_campaign_preservation": preservation,
              "totals": {"leaves": len(leaves), "selected_processed": selected, "target_statuses": target_counts,
                         "deferred_pending": sum(r["deferred_count"] for r in leaves), "candidates": sum(r["candidate_total"] for r in leaves),
                         **dict(counters), "licenses": dict(license_counts), "completeness": dict(completeness), "project_types": dict(project_types),
                         "discovery_provenance": dict(provenance), "model_receipts": dict(model_receipts), "model_workers": max_workers,
                         "source_model_overlapping_groups": overlap, "runs": len(runs)},
              "method": "Read-only production SQLite; all campaign published targets, archived source hashes and literal quotes; offline official SPDX templates; exact frozen manifest and every pending queue; real all-leaf card replay in a disposable SQLite backup. No pilot gate or job state altered."}
    (output / "FINAL_STRUCTURAL.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(canonical({k: result[k] for k in ["structural_passed", "totals", "incremental"]}), flush=True)
    print(canonical({"failures": failures[:20], "failure_count": len(failures)}), flush=True)


if __name__ == "__main__":
    main()
