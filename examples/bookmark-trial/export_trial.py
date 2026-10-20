"""Export a local R8 trial with existing host functions; no Store/API/model calls."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import zipfile

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "application-atlas-production-pack"))
from template_factory.cognition import research_from_accepted_facts, render_candidate  # noqa: E402
from template_factory.blueprints import freeze_blueprint, export_development, verify_frozen  # noqa: E402
from template_factory.store import digest  # noqa: E402

R8 = REPO / "docs/template-factory/g1-r8-contract-convergence-2026-10-20"
OLD = REPO / "docs/template-factory/g1-r7-evidence-recovery-2026-10-20/actual-frozen-review/job_b01427592b164863aab5bedf7b3863bb/source"
EXPECTED = "8bf361dbaae383b02cb3fd48020cfa6d9a229edc2f08a00e5f92029fb8c3e3a4"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def archive(source, target):
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as out:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                out.write(path, path.relative_to(source))
    return sha(target.read_bytes())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, required=True,
                        help="New output directory; never overwrite an existing snapshot")
    args = parser.parse_args()
    target = args.destination.resolve()
    target.mkdir(parents=True, exist_ok=False)
    prepared = json.loads((R8 / "prepared-response.json").read_text())
    checkpoints = json.loads((R8 / "PRODUCER_CHECKPOINTS.json").read_text())
    if not digest(prepared["effective_plan"]) == prepared["effective_plan_digest"] == EXPECTED:
        raise ValueError("R8 prepared plan digest mismatch")
    snapshot = copy.deepcopy(checkpoints["job"]["snapshot"])
    snapshot["case_facts_view"] = checkpoints["checkpoints"]["blueprint-accepted-facts-view"]["result"]
    snapshot["case_design"] = prepared["case_design"]
    research = research_from_accepted_facts(
        checkpoints["checkpoints"]["blueprint-research"]["result"], snapshot["case_facts_view"])
    programs, verified = {}, []
    for entry in prepared["prepared_program_revision"]["entries"]:
        source = ((R8 / "prepared-programs" / entry["path"]) if entry["mode"] == "replace"
                  else (OLD / entry["path"]))
        data = source.read_bytes()
        if sha(data) != entry["after_sha256"]:
            raise ValueError(f"Prepared program bytes mismatch: {source}")
        programs[entry["path"]] = data.decode("utf-8")
        verified.append({"path": entry["path"], "mode": entry["mode"], "sha256": sha(data),
                         "source": str(source.relative_to(REPO))})
    if len(verified) != 9:
        raise ValueError("Expected nine prepared programs")
    render_candidate({"spec": prepared["effective_plan"]["spec"], "files": programs},
                     research, snapshot, target / "candidate", "local-assisted-trial-bookmark-r8")
    provenance = {
        "origin": "assisted-trial", "note": "Local input snapshot only; no official artifact, independent pass, runtime proof or queue consumption.",
        "scenario": snapshot["scenario"], "case_basis": snapshot["case_basis"],
        "case_facts_view": snapshot["case_facts_view"], "case_design": snapshot["case_design"],
        "original_job_id": "job_dcb163d70a8e400fb07bc606570e2313",
        "prepared_plan_digest": EXPECTED, "leaf": snapshot["scenario"]["leaf"],
        "authorization_sha256": sha((REPO / "docs/template-factory/bookmark-assisted-trial-2026-10-20/AUTHORIZATION.txt").read_bytes()),
    }
    frozen = freeze_blueprint(target / "candidate", target / "template-snapshot", provenance)
    verify_frozen(target / "template-snapshot", frozen["digest"])
    exported = export_development(target / "template-snapshot", frozen["digest"],
                                  target / "development-package", "bookmark-trial", "P0")
    scope = (Path(__file__).parent / "TRIAL_SCOPE.md").read_text()
    (target / "TRIAL_SCOPE.md").write_text(scope)
    (target / "development-package/TRIAL_SCOPE.md").write_text(scope)
    receipt = {"origin": "assisted-trial", "prepared_plan_digest": EXPECTED,
               "template_digest": frozen["digest"], "export": exported,
               "provenance": provenance, "programs": verified,
               "controlled_opencode_calls_added": 0, "official_queue_consumed": False,
               "archives": {"template-snapshot.zip": archive(target / "template-snapshot", target / "template-snapshot.zip"),
                            "development-package.zip": archive(target / "development-package", target / "development-package.zip")}}
    (target / "EXPORT_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"destination": str(target), "template_digest": frozen["digest"],
                      "programs_verified": len(verified), "archives": receipt["archives"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
