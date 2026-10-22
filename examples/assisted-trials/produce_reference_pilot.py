"""Bounded real product-reference validation; never resumes the full dispatcher.

Preparation reuses immutable cases. Registration and reservations use formal
services and the original ledger. A failed item is recorded, not silently retried.
"""
from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
from pathlib import Path
import time

from atlas_runtime import atomic_json
from template_factory.cases import CaseLibrary
from template_factory.cli import CLI
from template_factory.reference_pilot import ReferencePilotService
from template_factory.store import digest
from template_factory.sources import source_storage_root
from produce_all_leaves import ROOT, PLAN_ID, host
from produce_with_opencode import fixed_json
from product_reference_profile import VERSION, PROMPT_DIGEST, OfficialCheckpointAdapter, generate

PILOT = "reference-two-shapes-2026-10-22"
DIRECTORY = ROOT / "docs/template-factory/product-reference-pilot-2026-10-22"
MODEL = "open-design/deepseek-v4.1-flash"
SAMPLES = (
    {"leaf": "bookmark-manager", "scenario": "scn_7756e0007f6a463a97316f3f49c15248",
     "case": "case:product-c42848f63251507bd9d911a5:faa52e6b1414", "revision": 1,
     "cache": "application-atlas-production-pack/atlas/template-factory/jobs/job_ae0f901f19824afcb8b53e9724f8ee6f/attempt-1/pinned-source",
     "files": ["LICENSE", "README.md", "src/App.tsrx", "src/includes/store.ts", "src/includes/utils.ts"],
     "shape": "Single-person accumulating collection; retain the confirmed scenario boundary."},
    {"leaf": "polling-application", "scenario": "scn_0da5ffd0b2124edf8183c82506cb2c61",
     "case": "case:assisted-ten-2026-10-21:dinner-poll", "revision": 1,
     "cache": "application-atlas-production-pack/atlas/template-factory/sources/assisted-ten-2026-10-21/dinner-poll",
     "files": ["COPYING", "README.md", "lib/Db/Poll.php", "lib/Db/Vote.php"],
     "shape": "Same-device group dinner poll, pseudonyms and host/member actions; no remote authentication platform."},
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def reuse_text_sources(store, original, sample):
    """Read only existing bytes matching the shared case; never resolve HEAD.

    The legacy case has located license text, not a verified SPDX identifier.
    Keep that status instead of promoting default-branch metadata to pin evidence.
    This reference pilot proposes design and does not redistribute upstream code.
    """
    target = source_storage_root(store.root) / PILOT / sample["leaf"]
    target.mkdir(parents=True, exist_ok=True)
    selected = {p: original["files"][p] for p in sample["files"]}
    for name, expected in selected.items():
        source = ROOT / sample["cache"] / name
        if source.is_symlink() or not source.is_file() or sha(source) != expected:
            raise ValueError(f"existing fixed source is unavailable or differs: {name}")
        data = source.read_bytes()
        data.decode("utf-8")
        out = target / name
        if out.exists() and (out.is_symlink() or sha(out) != expected):
            raise ValueError("existing external source cache differs")
        out.parent.mkdir(parents=True, exist_ok=True)
        if not out.exists():
            out.write_bytes(data)
    return {"repository": original["repository"], "commit_sha": original["commit_sha"],
            "files": selected, "local_root": str(target.absolute()),
            "license": original["license"], "license_files": original["license_files"],
            "license_status": "fixed_notice_located_spdx_not_independently_verified",
            "upstream_status": "not_run"}


def prepare():
    store, service = host()
    state = service.status(PLAN_ID)
    if state["status"] != "paused" or state["active_calls"]:
        raise ValueError("full production must remain paused with no active calls")
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    fixed_json(DIRECTORY / "BASELINE.json", {"plan_id": PLAN_ID,
               "new_calls": state["new_calls"], "baseline": state["baseline"],
               "deadline": state["deadline"], "model": MODEL})
    bindings = []
    library = CaseLibrary(store)
    for sample in SAMPLES:
        folder = DIRECTORY / sample["leaf"]
        folder.mkdir(exist_ok=True)
        leaf = store.leaf(sample["leaf"])
        scene = store.scenario(sample["scenario"])
        case = library.get_case(sample["case"], sample["revision"])
        original = case["source_snapshots"][0]
        # Deliberately selected text from the same case pin; original case and
        # its complete manifest remain unchanged, including binary exclusions.
        snapshot = reuse_text_sources(store, original, sample)
        fixed_json(folder / "CASE_REUSE.json", {
            "case_id": case["case_id"], "revision": case["revision"], "digest": case["digest"],
            "original_snapshot_digest": digest(original), "selected_files": snapshot["files"],
            "excluded_files": sorted(set(original["files"]) - set(snapshot["files"])),
            "case_created": False, "upstream_status": "not_run"})
        requirements = {"scenario": scene["objective"], "leaf-definition": leaf["name"]}
        requirements.update({f"flow-{i+1}": step for i, step in enumerate(scene["workflow"])})
        inputs = {"profile_version": VERSION, "leaf": {"id": sample["leaf"],
                  "name": leaf["name"], "content_sha256": hashlib.sha256(leaf["content"].encode()).hexdigest()},
                  "scenario": scene, "case_refs": [{k: case[k] for k in ("case_id", "revision", "digest")}],
                  "revision": PILOT + ":r1", "product_shape_guidance": sample["shape"],
                  "trusted_source_ids": {"requirements": requirements, "upstream": {
                      f"source-{i+1}": {"repository": snapshot["repository"], "commit_sha": snapshot["commit_sha"],
                                      "path": p, "sha256": value}
                      for i, (p, value) in enumerate(snapshot["files"].items())}}}
        inputs["digest"] = digest(inputs)
        fixed_json(folder / "INPUTS.json", inputs)
        fixed_json(folder / "SNAPSHOT.json", snapshot)
        body = leaf["content"].encode()
        target = folder / "leaf.md"
        if target.exists() and target.read_bytes() != body:
            raise ValueError("fixed leaf changed")
        target.write_bytes(body)
        with store.connect() as con:
            row = con.execute("SELECT body FROM auxiliary_full_leaf WHERE plan_id=? AND slug=?",
                              (PLAN_ID, sample["leaf"])).fetchone()
        frozen = json.loads(row[0])
        bindings.append({"leaf": sample["leaf"], "frozen_leaf_sha256": frozen["leaf_sha256"],
                         "input_path": str((folder / "INPUTS.json").relative_to(ROOT)),
                         "input_sha256": sha(folder / "INPUTS.json"),
                         "snapshot_path": str((folder / "SNAPSHOT.json").relative_to(ROOT)),
                         "snapshot_sha256": sha(folder / "SNAPSHOT.json")})
    result = {"schema": "atlas.reference-pilot-manifest.v1", "pilot_id": PILOT,
              "plan_id": PLAN_ID, "model": MODEL, "profile_version": VERSION,
              "prompt_digest": PROMPT_DIGEST, "max_calls": 6, "leaves": bindings,
              "application_runtime_status": "not_run", "strict_g1_t08": "unchanged"}
    fixed_json(DIRECTORY / "MANIFEST.json", result)
    return result


def register():
    store, _ = host()
    manifest = read(DIRECTORY / "MANIFEST.json")
    host_request = read(DIRECTORY / "HOST_REVISION.json")
    request = {"schema": "atlas.reference-pilot.v1", "pilot_id": PILOT,
               "idempotency_key": PILOT + ":register:v1", "plan_id": PLAN_ID,
               "campaign_id": "atlas-v1-first-production-2026-10-19",
               "leaves": manifest["leaves"], "profile_version": VERSION,
               "prompt_digest": PROMPT_DIGEST,
               "production_source_sha256": sha(ROOT / "examples/assisted-trials/product_reference_profile.py"),
               "source_ci": {"code_sha": host_request["code_sha"], "host_revision_digest": digest(host_request)},
               "user_request": {"path": str((DIRECTORY / "USER_REQUEST.txt").relative_to(ROOT)),
                                "sha256": sha(DIRECTORY / "USER_REQUEST.txt")}}
    fixed_json(DIRECTORY / "REGISTER_REQUEST.json", request)
    receipt = ReferencePilotService(store).register(request)
    atomic_json(DIRECTORY / "REGISTER_RECEIPT.json", receipt)
    return receipt


def verify_run_bindings(manifest, registered, receipt):
    if digest(registered) != receipt["request_digest"] or manifest["leaves"] != registered["leaves"]:
        raise ValueError("runner manifest differs from the formally registered inputs")
    if (manifest["profile_version"] != VERSION or registered["profile_version"] != VERSION
            or manifest["prompt_digest"] != PROMPT_DIGEST or registered["prompt_digest"] != PROMPT_DIGEST
            or manifest["model"] != MODEL):
        raise ValueError("registered runner model/profile/prompt differs")
    for binding in manifest["leaves"]:
        folder = DIRECTORY / binding["leaf"]
        if sha(folder / "leaf.md") != binding["frozen_leaf_sha256"]:
            raise ValueError("runner leaf bytes differ from original frozen scope")
        for path_key, sha_key in (("input_path", "input_sha256"), ("snapshot_path", "snapshot_sha256")):
            if sha(ROOT / binding[path_key]) != binding[sha_key]:
                raise ValueError("registered runner inputs changed")
        if read(ROOT / binding["input_path"])["leaf"]["content_sha256"] != binding["frozen_leaf_sha256"]:
            raise ValueError("product-reference leaf content binding differs")


def run():
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    with (DIRECTORY / ".runner.lock").open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        store, full = host()
        pilot = ReferencePilotService(store)
        status = pilot.get(PILOT)
        if status["status"] != "active":
            raise ValueError("formal pilot is not active")
        manifest = read(DIRECTORY / "MANIFEST.json")
        registered = read(DIRECTORY / "REGISTER_REQUEST.json")
        verify_run_bindings(manifest, registered, status)
        outcomes = []
        for binding in manifest["leaves"]:
            folder = DIRECTORY / binding["leaf"]
            # A recorded failed item is terminal in this validation, not a retry.
            if (folder / "OUTCOME.json").exists():
                outcomes.append(read(folder / "OUTCOME.json"))
                continue
            inputs, snapshot = read(ROOT / binding["input_path"]), read(ROOT / binding["snapshot_path"])
            phase = full.status(PLAN_ID)["phase"]
            budgets = {stage: {"ledger": full.ledger, "identity": PLAN_ID + ":" + binding["leaf"],
                       "phase": phase, "plan_id": PLAN_ID, "job_id": PILOT + ":" + binding["leaf"] + ":" + stage,
                       "stage": f"reference/{stage}/{PILOT}", "kind": kind}
                       for stage, kind in (("research", "research"), ("author", "production"), ("review", "review"))}
            adapter = OfficialCheckpointAdapter(folder, cli=CLI(), budget_by_stage=budgets,
                                                model=MODEL, leaf_bytes=(folder / "leaf.md").read_bytes())
            def bound_call(stage, payload, prompt, source):
                verify_run_bindings(manifest, registered, pilot.get(PILOT))
                return adapter(stage, payload, prompt, source)
            try:
                result = generate(folder / "generation", inputs, snapshot, bound_call)
                outcome = {k: v for k, v in result.items() if k != "reference"}
                if result["reference_zip"]:
                    package = Path(result["reference_zip"])
                    outcome["package_sha256"] = sha(package)
            except Exception as error:
                outcome = {"status": "failed", "error_type": type(error).__name__,
                           "code": getattr(error, "code", None), "reason": str(error),
                           "completed_stages": [s for s in ("research", "author", "review")
                                                if (folder / "generation" / s / "DELIVERED.json").is_file()]}
            outcome.update(leaf=binding["leaf"], recorded_at=time.time(),
                           application_runtime_status="not_run", publication_status="not_published")
            atomic_json(folder / "OUTCOME.json", outcome)
            print(json.dumps(outcome, ensure_ascii=False), flush=True)
            outcomes.append(outcome)
            current = full.status(PLAN_ID)
            if current["active_calls"]:
                # A launch with unknown terminal state requires investigation.
                pilot.action(PILOT, "pause", reason="active_or_uncertain_after_item")
                break
        if len(outcomes) == len(manifest["leaves"]):
            pilot.action(PILOT, "complete", reason="bounded validation reached terminal outcomes")
        report = {"pilot": pilot.get(PILOT), "outcomes": outcomes,
                  "full_plan": {k: full.status(PLAN_ID)[k] for k in ("status", "new_calls", "active_calls", "deadline")}}
        atomic_json(DIRECTORY / "RESULTS.json", report)
        return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "register", "run", "status"))
    args = parser.parse_args()
    if args.action == "status":
        store, _ = host()
        result = ReferencePilotService(store).get(PILOT)
    else:
        result = {"prepare": prepare, "register": register, "run": run}[args.action]()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
