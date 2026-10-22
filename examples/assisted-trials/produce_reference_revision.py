"""Revise the two fixed product-reference samples without resuming full production.

All model launches use the original ledger and a formally registered revision.
An existing result is replayed, never cleared to force a duplicate invocation.
"""
from __future__ import annotations

import argparse
import fcntl
import json
from pathlib import Path
import time

from atlas_runtime import atomic_json
from template_factory.cli import CLI
from template_factory.reference_pilot import ReferencePilotService
from template_factory.store import digest
from produce_all_leaves import ROOT, PLAN_ID, host
from produce_reference_pilot import PILOT, MODEL, DIRECTORY as PARENT, sha, read
from produce_with_opencode import fixed_json
import product_reference_profile as profile

DIRECTORY = ROOT / "docs/template-factory/product-reference-convergence-2026-10-22"
LEAVES = ("bookmark-manager", "polling-application")


def ref(path):
    path = Path(path)
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(path)}


def prepare(leaf, revision="r2", parent_revision=None):
    """Freeze the request; does not authorize or start a model call."""
    if leaf not in LEAVES:
        raise ValueError("only the two original samples are permitted")
    folder = DIRECTORY / leaf / revision
    folder.mkdir(parents=True, exist_ok=True)
    old = PARENT / leaf
    parent = DIRECTORY / leaf / parent_revision if parent_revision else old
    generation = parent / "generation"
    request = {"schema": "atlas.reference-pilot-revision.v1", "pilot_id": PILOT,
               "plan_id": PLAN_ID, "leaf": leaf, "revision_id": revision,
               "idempotency_key": f"{PILOT}:{leaf}:{revision}",
               "generation_path": str((folder / "generation").relative_to(ROOT)),
               "original_request_digest": read(PARENT / "REGISTER_RECEIPT.json")["request_digest"],
               "inputs_digest": ReferencePilotService._inputs_digest(read(PARENT / "REGISTER_REQUEST.json")),
               "latest_user_request": ref(DIRECTORY / "USER_REQUEST.txt"),
               "profile_version": profile.VERSION, "prompt_digest": profile.PROMPT_DIGEST,
               "production_source_sha256": sha(ROOT / "examples/assisted-trials/product_reference_profile.py"),
               "source_ci": {"code_sha": read(DIRECTORY / "HOST_REVISION.json")["code_sha"],
                             "host_revision_digest": digest(read(DIRECTORY / "HOST_REVISION.json"))},
               "parents": {"research": ref(generation / "research/RESULT.json"),
                           "research_receipt": ref(generation / "research/DELIVERED.json"),
                           "author": ref(generation / "author/RESULT.json"),
                           "author_receipt": ref(generation / "author/DELIVERED.json"),
                           "outcome": ref(parent / "OUTCOME.json")}}
    if parent_revision and read(parent / "OUTCOME.json").get("status") == "needs_changes":
        request["parents"]["review"] = ref(generation / "review/RESULT.json")
        request["parents"]["review_receipt"] = ref(generation / "review/DELIVERED.json")
    fixed_json(folder / "REQUEST.json", request)
    return request


def run_one(leaf, revision="r2"):
    store, full = host()
    state = full.status(PLAN_ID)
    if state["status"] != "paused" or state["active_calls"]:
        raise ValueError("full plan must be paused and drained before this serial runner")
    folder = DIRECTORY / leaf / revision
    request = read(folder / "REQUEST.json")
    receipt = ReferencePilotService(store).begin_revision(PILOT, request)
    stable_receipt = {key: value for key, value in receipt.items()
                      if key not in {"idempotent", "receipt_only"}}
    fixed_json(folder / "REGISTER_RECEIPT.json", stable_receipt)
    original = read(PARENT / "REGISTER_REQUEST.json")
    binding = next(x for x in original["leaves"] if x["leaf"] == leaf)
    inputs = read(ROOT / binding["input_path"])
    snapshot = read(ROOT / binding["snapshot_path"])
    budgets = {stage: {"ledger": full.ledger, "identity": PLAN_ID + ":" + leaf,
                      "phase": state["phase"], "plan_id": PLAN_ID,
                      "job_id": f"{PILOT}:{leaf}:{revision}:{stage}",
                      "stage": f"reference/{stage}/{PILOT}/{revision}", "kind": kind}
               for stage, kind in (("research", "research"), ("author", "production"), ("review", "review"))}
    adapter = profile.OfficialCheckpointAdapter(folder, cli=CLI(), budget_by_stage=budgets,
                                                model=MODEL, leaf_bytes=(PARENT / leaf / "leaf.md").read_bytes())
    parent_path = ROOT / request["parents"]["author"]["path"]
    target = folder / "OUTCOME.json"
    if target.is_file() and read(target)["status"] in {"failed", "needs_changes"}:
        return read(target)
    try:
        result = profile.revise(folder / "generation", inputs, snapshot,
                                parent_path.parent.parent, parent_path,
                                request["parents"]["author"]["sha256"], revision, adapter)
        outcome = {k: v for k, v in result.items() if k != "reference"}
        outcome["completed_stages"] = [s for s in ("research", "author", "review")
                                       if (folder / "generation" / s / "DELIVERED.json").is_file()]
    except Exception as error:
        outcome = {"status": "failed", "error_type": type(error).__name__,
                   "code": getattr(error, "code", None), "reason": str(error),
                   "completed_stages": [s for s in ("research", "author", "review")
                                        if (folder / "generation" / s / "DELIVERED.json").is_file()]}
    # This outcome is a checkpoint, not permission to alter earlier outcomes.
    outcome.update(leaf=leaf, revision_id=revision, recorded_at=time.time(),
                   application_runtime_status="not_run", publication_status="not_published")
    if target.exists():
        prior = read(target)
        if {k: v for k, v in prior.items() if k != "recorded_at"} != {
                k: v for k, v in outcome.items() if k != "recorded_at"}:
            raise ValueError("recorded revision outcome changed; preserve prior evidence")
        outcome = prior
    else:
        atomic_json(target, outcome)
    if outcome.get("reference_zip"):
        # An import failure is a separate host checkpoint. Resume reuses all model
        # deliveries; it does not turn a passed generation into a failed author.
        from template_factory.reference_catalog import ReferenceCatalog
        try:
            imported = ReferenceCatalog(store).import_reference({
                "pilot_id": PILOT, "leaf": leaf, "revision_id": revision,
                "generation_path": str((folder / "generation").relative_to(ROOT)),
                "package_sha256": sha(Path(outcome["reference_zip"]))})
            fixed_json(folder / "IMPORT_RECEIPT.json", imported)
        except Exception as error:
            atomic_json(folder / f"IMPORT_FAILURE.{time.time_ns()}.json", {
                "type": type(error).__name__, "reason": str(error),
                "generation_status": outcome["status"], "model_recall": False})
            raise
    return outcome


def run(leaf, revision="r2"):
    DIRECTORY.mkdir(parents=True, exist_ok=True)
    with (DIRECTORY / ".runner.lock").open("a+") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return run_one(leaf, revision)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "run", "status"))
    parser.add_argument("--leaf", choices=LEAVES)
    parser.add_argument("--revision", default="r2")
    parser.add_argument("--parent-revision")
    args = parser.parse_args()
    if args.action == "status":
        store, full = host()
        result = {"pilot": ReferencePilotService(store).get(PILOT), "full": full.status(PLAN_ID)}
    elif not args.leaf:
        parser.error("--leaf is required")
    elif args.action == "prepare":
        result = prepare(args.leaf, args.revision, args.parent_revision)
    else:
        result = run(args.leaf, args.revision)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
