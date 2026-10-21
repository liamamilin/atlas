"""Execute an authored auxiliary manifest; no model or upstream code execution.
Codex supplies research and scenario definitions. Services own persisted records.
"""

import argparse
import base64
import hashlib
import json
from pathlib import Path
import sys
import urllib.request
import zipfile

from export_trial import export_trial

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "application-atlas-production-pack"))
from template_factory.store import FactoryStore, digest  # noqa: E402
from template_factory.cases import CaseLibrary  # noqa: E402


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def request(base, route, body=None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        base + route, data, {"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=90) as response:
        return json.load(response)


def authored_definition(item, authored, scene, case, snap):
    model_production = item.get("production_mode") == "opencode-cli-go"
    origin_note = ("OpenCode CLI 研究与编写（渠道与模型见调用记录）；独立会话静态审阅通过，上游和下游应用均未运行。"
                   if model_production else "Codex研究与编写；静态案例未独审、上游未运行。")
    sources = []
    for i, observation in enumerate(case["observations"], 2):
        loc = observation["location"]
        sources.append(
            {
                "id": f"S{i:02}",
                "name": observation["evidence_id"],
                "url": loc.get(
                    "url",
                    snap["repository"]
                    + "/blob/"
                    + snap["commit_sha"]
                    + "/"
                    + loc.get("path", "LICENSE"),
                ),
                "version": snap["commit_sha"],
                "license": authored["license"],
                "license_url": snap["repository"]
                + "/blob/"
                + snap["commit_sha"]
                + "/" + authored.get("license_path", "LICENSE"),
                "facts": observation["kind"] + ": " + observation["statement"],
                "reuse": ("只参考设计；不复制上游代码。" + origin_note if model_production
                          else "只参考设计；不复制上游代码。独立审阅pending，上游运行not_run。"),
            }
        )
    features, cases = [], []
    for i, (name, goal) in enumerate(zip(authored["features"], authored["goals"]), 1):
        fid, aid = f"F{i:02}", f"A{i:02}"
        features.append(
            {
                "id": fid,
                "name": name,
                "phase": "P0",
                "applicability": "current required",
                "reason": goal,
                "sources": ["S01", *[s["id"] for s in sources]],
                "acceptance": [aid],
            }
        )
        cases.append(
            {
                "id": aid,
                "phase": "P0",
                "type": "positive",
                "goal": goal,
                "features": [fid],
                "implementation": "acceptance/probe.py",
            }
        )
    scope = (
        "# 辅助试用范围\n\n"
        + authored["objective"]
        + "\n\n"
        + "\n".join("- " + gap for gap in authored["gaps"])
        + "\n\n" + origin_note + "模板先于应用；仅代表场景后续开发应用。严格G1/T08不因本包通过。"
    )
    return {
        "scenario_record": scene,
        "case_ref": {
            "case_id": case["case_id"],
            "revision": case["revision"],
            "digest": case["digest"],
        },
        "research": {
            "summary": "同一共享案例记录的静态研究与明确的设计推断；完整定位见inputs/shared-case-record.json。",
            "sources": sources,
            "gaps": (["辅助静态独审通过，不代表运行通过"] if model_production else ["证据独立审阅pending"])
                    + ["上游not_run", *authored["gaps"]],
        },
        "spec": {
            "title": authored["name"],
            "roles": [
                {
                    "id": "R01",
                    "name": authored["audience"],
                    "responsibility": authored["objective"],
                }
            ],
            "features": features,
            "acceptance": cases,
            "decisions": [
                {
                    "id": "D01",
                    "question": "首版运行与数据边界？",
                    "default": authored.get("execution_default", "单用户本机、独立SQLite；显式保存，无账户、云端和协作。"),
                    "when_to_ask": "确需公网托管或多人数据时先确认，不自行扩展。",
                    "impact": "保护本地数据，避免默认外发。",
                    "status": "assisted default",
                },
                {
                    "id": "D02",
                    "question": "是否复刻上游？",
                    "default": authored["inference"],
                    "when_to_ask": "目标变化、破坏已有数据或需要引入上游实现/依赖时先确认。",
                    "impact": "不混淆来源事实与目标设计。",
                    "status": "assisted default",
                },
            ],
            "phases": [
                {
                    "id": "P0",
                    "title": "核心可用",
                    "goal": authored["objective"],
                    "features": [f["id"] for f in features],
                    "acceptance": [c["id"] for c in cases],
                }
            ],
            "architecture_markdown": authored["arch"],
            "limits": ["辅助试产，非严格G1/T08。", *authored["gaps"]],
        },
        "trial_scope": scope,
    }


def produce(folder, item, store, base, batch_id):
    p = folder / item["key"]
    authored = json.loads((p / "AUTHOR_INPUT.json").read_text())
    production = None
    if item.get("production_mode") == "opencode-cli-go":
        production = json.loads((p / "MODEL_PRODUCTION.json").read_text())
        if (production.get("schema") != "atlas.auxiliary-model-production.v1"
                or production.get("review_status") != "passed"
                or not production.get("review_input_digest")):
            raise ValueError("model production requires its bound review receipt")
    snap = json.loads((p / "source-snapshot.json").read_text())
    if production:
        from produce_with_opencode import verify_production
        verify_production(p, production, authored, snap)
    leaf = store.leaf(item["leaf"])
    raw = (store.pack / "applications" / (item["leaf"] + ".md")).read_bytes()
    if production and hashlib.sha256(raw).hexdigest() != json.loads((p / "REQUEST.json").read_text())["leaf_sha256"]:
        raise ValueError("leaf changed after independent review")
    leaf_receipt = {
        "slug": item["leaf"],
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
    }
    if (p / "LEAF.json").exists():
        if json.loads((p / "LEAF.json").read_text()) != leaf_receipt:
            raise ValueError("leaf changed; new version required")
    else:
        save(p / "LEAF.json", leaf_receipt)
    scene_input = {
        k: authored[k]
        for k in ("name", "audience", "objective", "workflow", "acceptance")
    }
    scene_input.update(leaf=leaf["slug"], status="draft")
    save(p / "scenario-request.json", scene_input)
    if (p / "scenario.json").exists():
        scene = store.scenario(json.loads((p / "scenario.json").read_text())["id"])
    else:
        matches = [
            s for s in store.scenarios(item["leaf"]) if s["name"] == authored["name"]
        ]
        # Freeze canonical data, excluding live review annotations in list projections.
        scene = store.scenario(matches[0]["id"]) if matches else store.save_scenario(scene_input)
    if any(scene[k] != v for k, v in scene_input.items()):
        raise ValueError("scenario changed; do not silently rewrite")
    save(p / "scenario.json", scene)
    observations = []
    for i, (kind, path, start, end, statement) in enumerate(
        authored["observations"], 1
    ):
        location = (
            {
                "commit_sha": snap["commit_sha"],
                "path": path,
                "file_digest": snap["files"][path],
                "line_start": start,
                "line_end": end,
            }
            if kind == "code_observation"
            else {
                "url": snap["repository"] + "/blob/" + snap["commit_sha"] + "/" + path,
                "material_version": snap["commit_sha"],
                "content_digest": snap["files"][path],
            }
        )
        observations.append(
            {
                "evidence_id": "ev_assisted_"
                + item["key"].replace("-", "_")
                + "_"
                + str(i),
                "kind": kind,
                "statement": statement,
                "location": location,
            }
        )
    observations.append(
        {
            "evidence_id": "ev_assisted_" + item["key"].replace("-", "_") + "_design",
            "kind": "inference",
            "statement": authored["inference"],
            "depends_on": [o["evidence_id"] for o in observations],
            "reasoning": "按当前叶子和具体用户旅程收敛为本机单人核心；不是对上游完整复刻。",
            "assumptions": ["上游未运行", "辅助静态独审通过，运行未验证" if production else "独立证据审阅pending", *authored["gaps"]],
        }
    )
    existing_case = (
        json.loads((p / "case-record.json").read_text())
        if (p / "case-record.json").exists()
        else None
    )
    payload = {
        "case_id": existing_case["case_id"]
        if existing_case
        else item.get("shared_case_id", "case:" + batch_id + ":" + item["key"]),
        "app_name": authored["repo_name"],
        "source_snapshots": [snap],
        "research": {
            "summary": ("OpenCode CLI静态研究与独立会话审阅；" if production else "Codex静态研究；") + authored["inference"],
            "scope": authored["objective"],
            "unknowns": [
                "upstream not_run",
                "auxiliary independent static review passed; runtime not_run" if production else "independent review pending",
                *authored["gaps"],
            ],
            "input_digest": digest(scene),
            "task_id": batch_id + "-" + item["key"],
        },
        "observations": observations,
        "scenario_links": [
            {
                "scenario_id": scene["id"],
                "scenario_revision": scene["revision"],
                "reason": authored["objective"],
                "evidence_ids": [o["evidence_id"] for o in observations],
                "adopted_scope": authored["features"],
                "exclusions": authored["gaps"],
            }
        ],
    }
    save(p / "case-request.json", payload)
    result = CaseLibrary(store).commit_research(
        payload, batch_id + "-" + item["key"] + "-research-v1"
    )
    case = result["case"]
    if production:
        library = CaseLibrary(store)
        for observation in case["observations"]:
            library.record_evidence_review(case["case_id"], case["revision"], observation["evidence_id"],
                                           "accepted", production["sessions"]["blueprint-spec-review-aux"],
                                           "independent_agent")
        case = library.get_case(case["case_id"], case["revision"])
    save(p / "case-record.json", case)
    save(
        p
        / (
            "case-replay-receipt.json"
            if result["replayed"]
            else "case-service-receipt.json"
        ),
        {
            "case_id": case["case_id"],
            "revision": case["revision"],
            "digest": case["digest"],
            "replayed": result["replayed"],
            "service": "CaseLibrary.commit_research",
        },
    )
    definition = authored_definition(item, authored, scene, case, snap)
    if production:
        definition["production"] = production
    if (p / "definition.json").exists():
        if json.loads((p / "definition.json").read_text()) != definition:
            raise ValueError("authored specification changed; new version required")
    else:
        save(p / "definition.json", definition)
    if (
        definition["scenario_record"] != scene
        or definition["case_ref"]["digest"] != case["digest"]
    ):
        raise ValueError("authored definition must bind exact saved scene and case")
    receipt = export_trial(p, p / "packages", item["key"] + "-trial", reuse=True)
    source = p / "packages/template-snapshot.zip"
    artifact = request(
        base,
        "blueprints/import",
        {"archive_base64": base64.b64encode(source.read_bytes()).decode()},
    )
    details = request(base, f"artifacts/{artifact['id']}/blueprint")
    assert details["digest"] == artifact["digest"]
    prior = (
        json.loads((p / "IMPORT_RECEIPT.json").read_text())
        if (p / "IMPORT_RECEIPT.json").exists()
        else None
    )
    if prior:
        if (
            prior["artifact_id"] != artifact["id"]
            or prior["digest"] != artifact["digest"]
        ):
            raise ValueError("registered artifact identity changed")
        if (
            hashlib.sha256(
                (p / "atlas-development-package.zip").read_bytes()
            ).hexdigest()
            != prior["exported_zip_sha256"]
        ):
            raise ValueError("existing development package changed")
        exported = prior["export"]
    else:
        exported = request(
            base,
            f"artifacts/{artifact['id']}/development-package",
            {
                "expected_digest": artifact["digest"],
                "project_name": item["key"] + "-trial",
                "phase": "P0",
            },
        )
        with urllib.request.urlopen(
            base.removesuffix("/api/factory/") + exported["download_url"]
        ) as response:
            (p / "atlas-development-package.zip").write_bytes(response.read())
    with zipfile.ZipFile(p / "atlas-development-package.zip") as z:
        assert json.loads(z.read("blueprint/inputs/shared-case-record.json")) == case
    imported = {
        "artifact_id": artifact["id"],
        "digest": artifact["digest"],
        "original_frozen_digest": receipt["template_digest"],
        "case_ref": definition["case_ref"],
        "url": "http://127.0.0.1:5188/factory?view=artifacts&artifact_id="
        + artifact["id"],
        "export": exported,
        "exported_zip_sha256": hashlib.sha256(
            (p / "atlas-development-package.zip").read_bytes()
        ).hexdigest(),
        "source": "OpenCode CLI authored and independently reviewed; provider/model preserved in stage records; host persistence/freeze/export/import" if production else "Codex authored; service persistence and existing freeze/export/import",
        "application_runtime": "not_run",
    }
    save(p / "IMPORT_RECEIPT.json", imported)
    if (p / "upstream-evidence.zip").exists():
        with zipfile.ZipFile(p / "upstream-evidence.zip") as z:
            for name, expected in snap["files"].items():
                assert hashlib.sha256(z.read(name)).hexdigest() == expected
    else:
        with zipfile.ZipFile(
            p / "upstream-evidence.zip", "w", zipfile.ZIP_DEFLATED
        ) as z:
            for name, expected in snap["files"].items():
                data = (Path(snap["local_root"]) / name).read_bytes()
                assert hashlib.sha256(data).hexdigest() == expected
                z.writestr(name, data)
            z.writestr(
                "source-snapshot.json", (p / "source-snapshot.json").read_bytes()
            )
    return {
        "state": "registered",
        "scenario_id": scene["id"],
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "artifact_id": artifact["id"],
        "original_frozen_digest": receipt["template_digest"],
        "export_reused": receipt.get("reused", False),
        "case_replayed": result["replayed"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--item")
    parser.add_argument("--api", default="http://127.0.0.1:5199/api/factory/")
    args = parser.parse_args()
    path = args.manifest.resolve()
    manifest = json.loads(path.read_text())
    pack = ROOT / "application-atlas-production-pack"
    store = FactoryStore(pack / "atlas/template-factory", pack)
    failed = False
    for item in manifest["items"]:
        if args.item and args.item != item["key"]:
            continue
        try:
            item.update(
                produce(path.parent, item, store, args.api, manifest["batch_id"])
            )
            # The failed-attempt file remains evidence; current state must not
            # keep a stale error after a successful, same-item continuation.
            item.pop("error", None)
            if (
                item.get("application_runtime")
                == "core_browser_and_same_dir_restart_passed"
            ):
                item["state"] = "registered_and_trial_running"
            elif not item.get("develop_representative"):
                item["state"] = "registered_template_only"
            print(item["key"], item["state"], item["artifact_id"])
        except Exception as error:
            failed = True
            item.update(state="failed", error=str(error))
            save(
                path.parent / item["key"] / "failure.json",
                {
                    "error": str(error),
                    "resume": f"python3 examples/assisted-trials/produce_batch.py --manifest {path} --item {item['key']}",
                    "history_preserved": True,
                },
            )
            print(item["key"], "failed", str(error))
        save(path, manifest)
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
