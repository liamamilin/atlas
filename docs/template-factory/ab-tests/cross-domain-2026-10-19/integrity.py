"""Host receipts, input identity and evidence consistency, not efficacy scoring."""

import hashlib
import json
from prepare import HERE, MODEL, hashes, save


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    mapping = json.loads((HERE / "condition-map.json").read_text())
    common = (HERE / "COMMON_DEVELOPMENT.md").read_text()
    cells, stages = {}, {}
    normalized_permissions = set()
    for case, labels in mapping.items():
        package = HERE / "cases" / case / "development-package"
        expected = json.loads(
            (HERE / "cases" / case / "template-ready.json").read_text()
        )["package_sha256"]
        assert hashes(package) == expected
        full_digests = set()
        for label, condition in labels.items():
            root = HERE / "runs" / case / label
            for stage in sorted(root.glob("*/attempt-*/scenario-review")):
                freeze = json.loads((stage / "input-freeze.json").read_text())
                assert hashes(stage / "source") == freeze["source_sha256"]
                prompt = (stage / "task-prompt.txt").read_text()
                assert (
                    prompt.startswith(common)
                    and hashlib.sha256(prompt.encode()).hexdigest()
                    == freeze["prompt_sha256"]
                )
                for name in ["REQUEST.md", "CONTRACT.md", "request.json"]:
                    assert sha(stage / "source" / name) == sha(
                        HERE / "cases" / case / name
                    )
                assert freeze["model"] == MODEL and freeze["reasoning_effort"] == "high"
                actual_input = stage / "actual-user-input.json"
                if actual_input.exists():
                    recorded = json.loads(actual_input.read_text())
                    provider, model_id = MODEL.split("/", 1)
                    for message in recorded.get("assistant_usage_records", []):
                        if message.get("model"):
                            assert message["model"]["providerID"] == provider
                            assert message["model"]["id"] == model_id
                            assert message["model"]["variant"] == "atlas-effort-high"
                config = json.loads((stage / "opencode.json").read_text())
                agent = next(iter(config["agents"]))
                normalized = (
                    json.dumps(config, sort_keys=True, ensure_ascii=False)
                    .replace(str(stage), "$STAGE")
                    .replace(agent, "$AGENT")
                )
                normalized_permissions.add(
                    hashlib.sha256(normalized.encode()).hexdigest()
                )
                if condition != "no_template":
                    assert hashes(stage / "source/product-context") == expected
                    full_digests.add(sha(stage / "source/FULL_TEMPLATE.md"))
                else:
                    assert (
                        not (stage / "source/product-context").exists()
                        and not (stage / "source/FULL_TEMPLATE.md").exists()
                    )
                assert bool(freeze["attachment"]) == (condition == "full_upfront")
                if freeze["attachment"]:
                    assert (stage / freeze["attachment"]).stat().st_size == freeze[
                        "attachment_bytes"
                    ]
                summary = stage / "cli-summary.json"
                if summary.exists():
                    cli = json.loads(summary.read_text())
                    assert (
                        cli["requested_model"] == MODEL
                        and cli["reasoning_effort"] == "high"
                    )
                failure = stage / "failure.json"
                forbidden_completed = []
                for line in (stage / "events.jsonl").read_bytes().splitlines():
                    try:
                        event = json.loads(line)
                    except (ValueError, UnicodeDecodeError):
                        continue  # Active trailing partial line is not completion.
                    part = event.get("part") or {}
                    state = part.get("state") or {}
                    if (
                        event.get("type") not in ["tool", "tool_use"]
                        or state.get("status") != "completed"
                    ):
                        continue
                    if part.get("tool") not in ["read", "write", "edit"]:
                        forbidden_completed.append(part.get("tool"))
                assert not forbidden_completed, (
                    "Unexpected completed author tool: " + str(forbidden_completed)
                )
                stages[str(stage.relative_to(HERE))] = {
                    "input_identity_checks": "passed",
                    "status": "failure_preserved"
                    if failure.exists()
                    else ("cli_finished" if summary.exists() else "pending"),
                    "failure": json.loads(failure.read_text())
                    if failure.exists()
                    else None,
                    "attachment": "supplied according to host input-freeze and driver branch; raw CLI argv/provider payload not independently captured"
                    if freeze["attachment"]
                    else "none",
                }
            for round_name in ["initial", "repair"]:
                cell = root / round_name
                if not (cell / "delivery.json").exists():
                    continue
                delivery = json.loads((cell / "delivery.json").read_text())
                result = {
                    "delivery_status": delivery["status"],
                    "runtime_evidence": "pending",
                }
                app = cell / "application"
                if app.exists():
                    delivered_hash = delivery["source_sha256"]
                    assert hashes(app) == delivered_hash
                    result["application_matches_delivery"] = True
                else:
                    delivered_hash = None
                index = (
                    HERE / "evaluation/results" / case / label / "evidence-index.json"
                )
                if index.exists():
                    index_data = json.loads(index.read_text())
                    entry = index_data.get("rounds", {}).get(round_name)
                    if entry:
                        evidence = index.parent / entry["directory"]
                        assert evidence.resolve().parent == index.parent.resolve()
                        freeze = HERE / "evaluation" / entry["oracle_freeze_file"]
                        assert (
                            entry["oracle_version"] == 3
                            and sha(freeze) == entry["oracle_freeze_sha256"]
                        )
                        assert sha(evidence / "result.json") == entry["result_sha256"]
                        prov = json.loads((evidence / "provenance.json").read_text())
                        if delivered_hash is None:
                            assert delivery["status"] == "failed_delivery"
                            assert (
                                prov["commands_executed"] == []
                                and prov["services_started"] == []
                            )
                            assert prov["delivery_receipt_sha256"] == sha(
                                cell / "delivery.json"
                            )
                            result["runtime_evidence"] = (
                                "v3 explicit not_run; failed delivery receipt hash matches"
                            )
                            cells[f"{case}/{label}/{round_name}"] = result
                            continue
                        assert (
                            prov["application_sha256_before"]
                            == prov["application_sha256_after"]
                            == delivered_hash
                        )
                        expected_tools = json.loads(freeze.read_text())["source_sha256"]
                        assert all(
                            prov["toolchain_sha256"].get(n) == digest
                            for n, digest in expected_tools.items()
                        )
                        assert prov["toolchain_sha256"]["freeze.json"] == sha(freeze)
                        result["runtime_evidence"] = (
                            "v3/source/result/tool hashes match"
                        )
                    probe = index_data.get("exploratory", {}).get("EP01_" + round_name)
                    if probe:
                        probe_dir = index.parent / probe["directory"]
                        assert probe_dir.resolve().parent == index.parent.resolve()
                        assert sha(probe_dir / "result.json") == probe["result_sha256"]
                        probe_result = json.loads(
                            (probe_dir / "result.json").read_text()
                        )
                        probe_freeze = HERE / "evaluation" / probe["freeze"]
                        assert probe_result["freeze_sha256"] == sha(probe_freeze)
                        assert all(
                            sha(HERE / "evaluation" / name) == digest
                            for name, digest in json.loads(probe_freeze.read_text())[
                                "source_sha256"
                            ].items()
                        )
                        assert (
                            probe_result["application_sha256_before"]
                            == probe_result["application_sha256_after"]
                            == delivered_hash
                        )
                        assert probe_result["core_scores_changed"] is False
                        result["exploratory_evidence"] = (
                            "EP01 posthoc/source/result/tool hashes match; core unchanged"
                        )
                cells[f"{case}/{label}/{round_name}"] = result
        assert len(full_digests) <= 1, (
            f"{case}: template representations differ across conditions or rounds"
        )
    assert len(normalized_permissions) <= 1, (
        "Author permissions/runtime configuration differ"
    )
    expected_initial = {
        f"{case}/{label}/initial"
        for case, labels in mapping.items()
        for label in labels
    }
    missing_initial = sorted(expected_initial - cells.keys())
    pending = [
        name for name, value in cells.items() if value["runtime_evidence"] == "pending"
    ]
    pending_stages = [
        name for name, value in stages.items() if value["status"] == "pending"
    ]
    save(
        HERE / "integrity.json",
        {
            "status": "all_expected_initial_cells_accounted_for_and_receipts_consistent"
            if not (missing_initial or pending or pending_stages)
            else "available_receipts_consistent_with_pending_work",
            "missing_initial_cells": missing_initial,
            "pending_runtime_evidence": pending,
            "pending_stages": pending_stages,
            "cells": cells,
            "stages": stages,
            "normalized_author_configuration_hashes": sorted(normalized_permissions),
            "limits": [
                "Input checks prove supplied local bytes and declared host driver branch, not complete provider context exposure.",
                "Same common prompt prefix is followed by intentional condition instructions and optional observed repair feedback.",
                "Source and evidence checks do not establish efficacy or security; independent runtime/review are separate.",
                "Reviewers get original app documentation, which may reveal template provenance despite withheld mapping.",
            ],
        },
    )
    print(
        "Verified", len(stages), "available stages and", len(cells), "delivery receipts"
    )


if __name__ == "__main__":
    main()
