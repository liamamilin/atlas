"""Small parameterized local exporter, using the existing template host functions."""

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
from template_factory.cognition import render_candidate, validate_research  # noqa: E402
from template_factory.blueprints import (  # noqa: E402
    freeze_blueprint,
    export_development,
    verify_frozen,
)
from template_factory.artifacts import tree_manifest  # noqa: E402
from template_factory.store import digest  # noqa: E402
from atlas_runtime import atomic_json  # noqa: E402


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def archive(source, path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as out:
        for item in sorted(source.rglob("*")):
            if item.is_file() and "__pycache__" not in item.parts:
                out.write(item, item.relative_to(source))
    return sha(path)


def export_trial(inputs, destination, name):
    definition = json.loads((inputs / "definition.json").read_text())
    case = json.loads((inputs / "case-record.json").read_text())
    original = definition["scenario_record"]
    # User explicitly chose this fixed draft revision for auxiliary development.
    # This is local confirmation only: never changes the formal scenario record.
    scene = copy.deepcopy(original)
    scene["status"] = "ready"
    scene["local_confirmation"] = (
        "User authorized this exact id/revision for assisted trial; formal draft unchanged."
    )
    snapshot = {
        "scenario": scene,
        "config": {"language": "zh"},
        "cognitive_repair": {"version": "assisted-trial-0.1.0"},
    }
    result = {
        "spec": definition["spec"],
        "files": {
            "acceptance/" + str(p.relative_to(inputs / "acceptance")): p.read_text()
            for p in (inputs / "acceptance").rglob("*")
            if p.is_file() and "__pycache__" not in p.parts
        },
    }
    destination.mkdir(parents=True, exist_ok=False)
    candidate = destination / "candidate"
    render_candidate(
        result,
        validate_research(definition["research"]),
        snapshot,
        candidate,
        "local-assisted-" + name,
    )
    atomic_json(candidate / "inputs/shared-case-record.json", case)
    atomic_json(candidate / "inputs/original-scenario-record.json", original)
    (candidate / "TRIAL_SCOPE.md").write_text(definition["trial_scope"])
    atomic_json(
        candidate / "integrity.json",
        {
            "template_version": "assisted-trial-0.1.0",
            "sha256": {
                k: v
                for k, v in tree_manifest(candidate).items()
                if k != "integrity.json"
            },
        },
    )
    provenance = {
        "origin": "assisted-trial",
        "scenario": original,
        "local_confirmation": scene["local_confirmation"],
        "case_ref": {
            "case_id": case["case_id"],
            "revision": case["revision"],
            "digest": case["digest"],
        },
        "case_record_sha256": sha(inputs / "case-record.json"),
        "definition_digest": digest(definition),
        "official_publication": False,
        "upstream_runtime": "not_run",
        "independent_evidence_review": "pending",
        "note": "Static Codex source study; no model review or formal queue consumption. Local freeze fixes inputs only.",
    }
    frozen = freeze_blueprint(candidate, destination / "template-snapshot", provenance)
    verify_frozen(destination / "template-snapshot", frozen["digest"])
    exported = export_development(
        destination / "template-snapshot",
        frozen["digest"],
        destination / "development-package",
        name,
        "P0",
    )
    (destination / "development-package/TRIAL_SCOPE.md").write_text(
        definition["trial_scope"]
    )
    receipt = {
        "origin": "assisted-trial",
        "template_digest": frozen["digest"],
        "export": exported,
        "provenance": provenance,
        "controlled_opencode_calls_added": 0,
        "official_queue_consumed": False,
        "archives": {
            n + ".zip": archive(destination / n, destination / (n + ".zip"))
            for n in ("template-snapshot", "development-package")
        },
    }
    atomic_json(destination / "EXPORT_RECEIPT.json", receipt)
    return receipt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    receipt = export_trial(args.inputs.resolve(), args.destination.resolve(), args.name)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
