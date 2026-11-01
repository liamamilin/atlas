"""Audit the completed first 100 leaves against archived official material, offline."""
import json
from collections import Counter, defaultdict
from pathlib import Path
import re
import sqlite3
import sys
from unittest.mock import patch

BASE = Path(__file__).resolve().parent
PACK = BASE.parents[1] / "application-atlas-production-pack"
sys.path.insert(0, str(PACK))
from oss_catalog import canonical, decode_file, digest, plain_text
from oss_discovery import ROOT, LicenseMatcher

con = sqlite3.connect("/private/tmp/atlas-100-acceptance-2026-10-25.sqlite")
con.row_factory = sqlite3.Row
job = json.loads(con.execute("SELECT data FROM oss_batch_job WHERE id=?", (
    "batch_cd8f7a777e3c4e6885de1cf3162e004c",)).fetchone()[0])
leaves = set(job["leaves"])
scenarios = {r["id"]: {**json.loads(r["data"]), "leaf": r["leaf"]}
             for r in con.execute("SELECT * FROM oss_scenario")}
members = [(r[0], r[1]) for r in con.execute("SELECT * FROM oss_leaf_project") if r[0] in leaves]
ids = {rid for _, rid in members}
cards = {r["repository_id"]: json.loads(r["data"]) for r in con.execute("SELECT * FROM oss_project")
         if r["repository_id"] in ids}
matches = defaultdict(list)
for row in con.execute("SELECT * FROM oss_match"):
    if scenarios[row["scenario_id"]]["leaf"] in leaves:
        matches[(scenarios[row["scenario_id"]]["leaf"], row["repository_id"])].append(json.loads(row["data"]))
metadata, registry, files = {}, {}, {}
for row in con.execute("SELECT data FROM oss_candidate"):
    meta = json.loads(row[0])["meta"]
    metadata[meta["id"]] = meta
    registry[("", digest(canonical(meta)))] = re.sub(r"\s+", " ", meta.get("description") or meta["full_name"])
archive_errors = []
for directory in ("sources", "documentation", "evidence"):
    for path in (ROOT / directory).glob("*.json"):
        value = json.loads(path.read_text())
        entries = ([value.get("readme"), value.get("license")] if directory == "sources" else
                   [d["file"] for d in value.get("documents", [])] if directory == "documentation" else
                   [value["file"]])
        for file in entries:
            if not file:
                continue
            try:
                raw = decode_file(file)
                key = (file["git_url"], digest(raw))
                registry[key] = plain_text(raw)
                files[key] = file
            except (ValueError, UnicodeError) as error:
                archive_errors.append({"path": str(path.relative_to(ROOT)), "error": type(error).__name__})

failures, source_checks, license_checks = [], [], []
quotes = 0
def check_proof(proof, rid, kind):
    global quotes
    if not proof or not proof.get("source_url", "").startswith("https://"):
        failures.append({"repo": cards[rid]["full_name"], "kind": kind, "reason": "missing source"})
        return
    key = (proof.get("immutable_url", ""), proof.get("source_sha256", proof.get("sha256")))
    if key not in registry:
        failures.append({"repo": cards[rid]["full_name"], "kind": kind, "reason": "archive missing", "source": proof})
        return
    if proof.get("excerpt"):
        if proof["excerpt"].casefold() not in registry[key].casefold():
            failures.append({"repo": cards[rid]["full_name"], "kind": kind, "reason": "quote mismatch"})
        quotes += 1
    elif proof.get("verification") not in {"source_based", "inferred"} and kind not in {"license", "source"}:
        failures.append({"repo": cards[rid]["full_name"], "kind": kind, "reason": "missing verification label"})

def cached_template(self, identifier):
    path = ROOT / "spdx" / (identifier + ".json")
    return json.loads(path.read_text()) if path.exists() else None

with patch.object(LicenseMatcher, "template", cached_template):
    for rid, card in cards.items():
        assert card["github_url"] == "https://github.com/" + card["full_name"]
        assert card["checked_at"] and card["license"]["status"] in {"open_source", "source_available", "pending"}
        proofs = [("summary", card["summary_evidence"]), ("scope", card["scope_evidence"])]
        if card.get("positioning_evidence"):
            proofs.append(("positioning", card["positioning_evidence"]))
        proofs += [("feature", f["evidence"]) for f in card["features"]]
        for kind, proof in proofs:
            check_proof(proof, rid, kind)
        for source in card["sources"]:
            check_proof({**source, "source_url": source["url"]}, rid, "source")
        license_source = card["license"].get("source")
        if license_source:
            check_proof({**license_source, "source_url": license_source.get("url")}, rid, "license")
        if card["license"]["status"] == "open_source":
            if not license_source:
                failures.append({"repo": card["full_name"], "reason": "open source without license evidence"})
                continue
            file = files.get((license_source["immutable_url"], license_source["sha256"]))
            readme = next((files.get((s["immutable_url"], s["sha256"]))
                           for s in card["sources"] if s["kind"] == "readme"), None)
            actual = LicenseMatcher(ROOT).classify(metadata[rid], file, readme)
            passed = actual["status"] == "open_source" and actual["spdx"] == card["license"]["spdx"]
            license_checks.append({"repo": card["full_name"], "spdx": card["license"]["spdx"], "passed": passed})
            if not passed:
                failures.append({"repo": card["full_name"], "reason": "license recheck differs", "actual": actual["status"]})
        source_checks.append({"repo": card["full_name"], "proofs": len(proofs), "license_status": card["license"]["status"]})

for (leaf, rid), relations in matches.items():
    assert (leaf, rid) in members
    for match in relations:
        check_proof(match["evidence"], rid, "match")
        assert match.get("applicability", "direct") in {"direct", "conditional", "unverified"}
        if match.get("applicability") == "conditional":
            assert match.get("conditions")

summary = []
for leaf in job["leaves"]:
    leaf_ids = [rid for slug, rid in members if slug == leaf]
    leaf_scenarios = [s for s in scenarios.values() if s["leaf"] == leaf]
    summary.append({"leaf": leaf, "scenarios": len(leaf_scenarios), "projects": len(leaf_ids),
                    "candidates": len(job["targets"][leaf]),
                    "target_statuses": dict(Counter(t["status"] for t in job["targets"][leaf])),
                    "associations": sum(len(matches[(leaf, rid)]) for rid in leaf_ids),
                    "unassociated_projects": sum(not matches[(leaf, rid)] for rid in leaf_ids),
                    "empty_scenarios": [s["id"] for s in leaf_scenarios
                                        if not any(m["scenario_id"] == s["id"] for rid in leaf_ids for m in matches[(leaf, rid)])]})
run_ids = set(job["runs"])
runs = [json.loads(row["data"]) for row in con.execute("SELECT id,data FROM oss_run") if row["id"] in run_ids]
receipts = [receipt for run in runs for receipt in run.get("model_receipts", [])]
totals = {"leaf_count": len(leaves), "processed": job["processed"], "targets": job["total"],
          "target_statuses": dict(Counter(t["status"] for items in job["targets"].values() for t in items)),
          "distinct_projects": len(cards), "memberships": len(members), "scenarios": sum(s["leaf"] in leaves for s in scenarios.values()),
          "associations": sum(len(v) for v in matches.values()), "quotes_checked": quotes,
          "licenses": dict(Counter(p["license"]["status"] for p in cards.values())),
          "completeness": dict(Counter(p.get("completeness", "legacy") for p in cards.values())),
          "applicability": dict(Counter(m.get("applicability", "direct") for relations in matches.values() for m in relations)),
          "model_receipts": dict(Counter(r["provider"] for r in receipts)),
          "four_worker_runs": sum(r.get("concurrency", {}).get("model_workers") == 4 for r in runs),
          "recovery_cycles": job.get("recovery", {}).get("cycles"),
          "license_claims_rechecked": len(license_checks), "integrity_failures": len(failures),
          "archive_decode_errors": archive_errors, "empty_scenarios": sum(len(s["empty_scenarios"]) for s in summary)}
for filename, value in (("TOTALS.json", totals), ("LEAF_SUMMARY.json", summary), ("SOURCE_INTEGRITY.json", source_checks),
                        ("LICENSE_CHECKS.json", license_checks), ("AUDIT_FAILURES.json", failures)):
    (BASE / filename).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(totals, ensure_ascii=False))
