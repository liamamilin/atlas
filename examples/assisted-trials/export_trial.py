"""Small parameterized local exporter, using the existing template host functions."""

from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import zipfile

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "application-atlas-production-pack"))
from template_factory.cognition import render_candidate, validate_research  # noqa: E402
from template_factory.blueprints import (  # noqa: E402
    freeze_blueprint,
    export_development,
    verify_frozen,
    unpack_archive,
)
from template_factory.artifacts import tree_manifest  # noqa: E402
from template_factory.store import digest  # noqa: E402
from atlas_runtime import atomic_json  # noqa: E402


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def acceptance_inputs(directory):
    return {
        p.relative_to(directory).as_posix(): sha(p)
        for p in sorted(directory.rglob("*"))
        if p.is_file() and "__pycache__" not in p.parts
    }


def archive(source, path):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as out:
        for item in sorted(source.rglob("*")):
            if item.is_file() and "__pycache__" not in item.parts:
                out.write(item, item.relative_to(source))
    return sha(path)


def export_trial(inputs, destination, name, reuse=False):
    definition = json.loads((inputs / "definition.json").read_text())
    case = json.loads((inputs / "case-record.json").read_text())
    if definition.get("production", {}).get("full_plan_id"):
        from produce_all_leaves import verify_full_production
        verify_full_production(inputs, definition["production"],
            json.loads((inputs/"AUTHOR_INPUT.json").read_text()),
            json.loads((inputs/"source-snapshot.json").read_text()))
    if definition.get("production", {}).get("revision_request_digest"):
        from revise_with_opencode import verify_revision
        verify_revision(inputs, definition["production"],
                        json.loads((inputs / "AUTHOR_INPUT.json").read_text()),
                        json.loads((inputs / "source-snapshot.json").read_text()))
        if definition["case_ref"] != {k: case[k] for k in ("case_id", "revision", "digest")}:
            raise ValueError("revision case reference differs")
        from produce_batch import authored_definition
        expected = authored_definition({"production_mode": "opencode-cli-go"},
            json.loads((inputs / "AUTHOR_INPUT.json").read_text()), definition["scenario_record"], case,
            json.loads((inputs / "source-snapshot.json").read_text()))
        expected["production"] = definition["production"]
        if expected != definition:
            raise ValueError("revision definition differs from reviewed model content")
    acceptance = acceptance_inputs(inputs / "acceptance")
    if reuse and destination.exists():
        receipt = json.loads((destination / "EXPORT_RECEIPT.json").read_text())
        provenance = receipt["provenance"]
        if (
            provenance["definition_digest"] != digest(definition)
            or provenance["case_record_sha256"] != sha(inputs / "case-record.json")
            or receipt["export"]["project_name"] != name
        ):
            raise ValueError("fixed trial inputs changed; choose a new version/output")
        for filename, expected in receipt["archives"].items():
            if sha(destination / filename) != expected:
                raise ValueError("trial archive changed")
        with tempfile.TemporaryDirectory() as temporary:
            unpack_archive(
                (destination / "template-snapshot.zip").read_bytes(), temporary
            )
            verify_frozen(temporary, receipt["template_digest"])
            # Older receipts predate this input manifest. Compare with the
            # original verified bytes instead of rewriting historical freezes.
            expected = provenance.get("acceptance_inputs")
            if expected is None:
                expected = acceptance_inputs(Path(temporary) / "source/acceptance")
                # render_candidate always adds this host-owned plan. It was
                # not an authored acceptance input in legacy trial exports.
                expected.pop("plan.json", None)
            if acceptance != expected:
                raise ValueError(
                    "acceptance files changed; choose a new version/output"
                )
        return {**receipt, "reused": True}
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
    if definition.get("production"):
        atomic_json(candidate / "inputs/model-production.json", definition["production"])
    if definition.get("production", {}).get("full_plan_id"):
        atomic_json(candidate/"inputs/authored-cognition.json", json.loads((inputs/"AUTHOR_INPUT.json").read_text()))
        atomic_json(candidate/"inputs/source-partitions.json", json.loads((inputs/"SOURCE_INPUT.json").read_text()))
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
        "acceptance_inputs": acceptance,
        "official_publication": False,
        "upstream_runtime": "not_run",
        "independent_evidence_review": "pending",
        "note": "Static Codex source study; no model review or formal queue consumption. Local freeze fixes inputs only.",
    }
    production = definition.get("production")
    if production:
        # New auxiliary packages carry model provenance; old frozen bytes and
        # default receipt structure remain unchanged.
        provenance.update(model_production=production,
                          independent_evidence_review="passed_auxiliary_static",
                          note="OpenCode CLI + Go source study and separate-session review. No upstream/downstream runtime or strict certification.")
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
        "controlled_opencode_calls_added": production["controlled_opencode_calls_added"] if production else 0,
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
    parser.add_argument(
        "--reuse",
        action="store_true",
        help="Verify and reuse fixed outputs; never overwrite",
    )
    args = parser.parse_args()
    receipt = export_trial(
        args.inputs.resolve(), args.destination.resolve(), args.name, args.reuse
    )
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
