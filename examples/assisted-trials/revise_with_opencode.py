"""Bounded, resumable auxiliary draft revision. No strict G1 state changes.

The model returns content; the host owns lineage, immutable case identity,
budget, review binding, freeze/import and downloads. Run --until generated to
inspect the candidate and its isolated fixture evidence before independent review.
"""
from __future__ import annotations

import argparse
import base64
import copy
import difflib
import fcntl
import hashlib
import json
from pathlib import Path
import shutil
import urllib.request
import zipfile

from produce_batch import ROOT, authored_definition, request
from export_trial import export_trial
from produce_with_opencode import (CAMPAIGN, MODEL, CHECKS, checkpoint, fixed_json,
                                   manifest_files, readable_candidate, validate_generation,
                                   validate_review, validate_read_coverage, register_catalog,
                                   READABLE_REVIEW)
from template_factory.budget import BudgetLedger
from template_factory.cases import CaseLibrary
from template_factory.cli import CLI
from template_factory.store import FactoryStore, digest
from atlas_runtime import atomic_json

MUTABLE = {"objective", "workflow", "acceptance", "goals", "arch", "gaps"}
AUTHOR = """You are revising ONE existing auxiliary cognition template, not making an app.
Read input.json, source/candidate/READING_GUIDE.md, all candidate views, original
AUTHOR_INPUT.json, acceptance/probe.py and README.md. source/upstream is the SAME
fixed case; do not research new sources or change its 15 observations.
Return JSON {authored_updates:{only changed fields from objective,workflow,acceptance,
goals,arch,gaps},acceptance_files:{'probe.py':FULL source,'README.md':FULL text}}.
Host merges unchanged fields, preserving name, audience, observations, inference,
features and source identities. Fix all five input.request.issues in one revision.
Date contract is authoritative: latest=max(existing last_completed_on if present,
completed_on); new_due_on=max(old due_on, latest + interval_days). Store the true
latest, append actual completion and note, read/insert/update in one transaction.
Synchronize objective/goals/acceptance/arch/README. Keep old leap/month/year/later
backfill assertions and negative tests. Add BOTH initial backfills (explicit old due
2026-03-01 plus historical 2025-01-01/30 days, and no anchor creation-day due).
A01 compare EMPTY patch to latest successful PATCH full object INCLUDING updated_at.
Invalid category: all other fields valid, 422 VALIDATION_ERROR, entire list unchanged.
A02 use fresh equipment scopes; assert COMPLETE ID sets AND counts for every due
query; duplicate/extra/missing tasks must fail, retain status/date/filter checks.
A05 use stdlib HTMLParser to check actual relationships: every input labelled by
for/id, fieldset contains legend, due table caption and th scope=col, role=status,
aria-live=polite, html lang=en, and existing state feedback shell. No new features
or full accessibility certification. Keep ALL other existing core tests/contracts.
Do not execute code, write files, change upstream case, or claim application runtime.
All acceptance cases must still run sequentially against one disposable database.
Keep lines below 1900 chars so exact long-field views are readable. JSON only.
"""


def load(path):
    return json.loads(path.read_text())


def merge_revision(parent, result, snapshot):
    updates = result.get("authored_updates")
    if not isinstance(updates, dict) or not updates or set(updates) - MUTABLE:
        raise ValueError("revision changes fields outside the bounded content scope")
    authored = copy.deepcopy(parent)
    authored.update(updates)
    files = result.get("acceptance_files")
    if not isinstance(files, dict) or set(files) != {"probe.py", "README.md"}:
        raise ValueError("revision requires the same two complete acceptance files")
    return validate_generation({"authored": authored, "acceptance_files": files}, snapshot)


def write_candidate(target, authored, files):
    target.mkdir(parents=True, exist_ok=True)
    fixed_json(target / "AUTHOR_INPUT.json", authored)
    for name, content in files.items():
        path = target / "acceptance" / name
        path.parent.mkdir(exist_ok=True)
        if path.exists() and path.read_text() != content:
            raise ValueError("candidate bytes changed; use a new revision")
        path.write_text(content)
    return readable_candidate(target, authored)


def review_identity(req, authored, files, snapshot, scene):
    return digest({"request": req, "authored": authored, "acceptance_files": files,
                   "source_snapshot_digest": digest(snapshot), "scenario": scene})


def verify_revision(folder, production, authored, snapshot):
    """Revalidate actual sessions and all read bytes before freeze/import/replay."""
    req = load(folder.parent / "REQUEST.json")
    files = {p.name: p.read_text() for p in (folder / "acceptance").iterdir() if p.is_file()}
    scene = load(folder / "scenario.json")
    identity = review_identity(req, authored, files, snapshot, scene)
    if (production["review_input_digest"] != identity
            or production["revision_request_digest"] != digest(req)
            or production["parent"] != req["parent"]
            or production["source_snapshot_digest"] != digest(snapshot)):
        raise ValueError("revision provenance differs from reviewed content")
    sessions = {}
    for role in ("author", "review"):
        stage = folder / "calls" / production["stages"][role]
        binding, result, summary = (load(stage / n) for n in ("BINDING.json", "RESULT.json", "cli-summary.json"))
        if (load(stage / "DELIVERED.json") != {"binding_digest": digest(binding), "result_digest": digest(result)}
                or binding["input_digest"] != digest(load(stage / "input.json"))
                or binding["source"] != manifest_files(stage / "source")
                or binding["leaf_sha256"] != hashlib.sha256((stage / "leaf.md").read_bytes()).hexdigest()
                or summary.get("requested_model") != MODEL or summary.get("delivery_status") != "delivered"
                or summary.get("original_response_sha256") != hashlib.sha256((stage / "original-response.json").read_bytes()).hexdigest()):
            raise ValueError("revision real-call checkpoint changed")
        sessions[role] = summary["session_id"]
        if role == "author":
            expected = merge_revision(load(stage / "source/candidate/AUTHOR_INPUT.json"), result, snapshot)
            if expected != (authored, files):
                raise ValueError("revision no longer matches actual model return")
        else:
            if load(stage / "input.json")["input_digest"] != identity or digest(result) != production["review_result_digest"]:
                raise ValueError("cannot reuse an old review for a new revision")
            candidate = stage / "source/candidate"
            if (load(candidate / "AUTHOR_INPUT.json") != authored
                    or {p.name: p.read_text() for p in (candidate / "acceptance").iterdir() if p.is_file()} != files
                    or manifest_files(stage / "source/upstream") != snapshot["files"]):
                raise ValueError("reviewed materials differ from frozen candidate")
            validate_read_coverage(stage, authored)
            validate_review(result, identity, production["sessions"]["author"], summary["session_id"], len(authored["observations"]))
    if sessions != production["sessions"]:
        raise ValueError("revision sessions differ")


def publish_auxiliary(folder, req, store, api, production, authored, snapshot, scene, case):
    verify_revision(folder, production, authored, snapshot)
    if case["digest"] != req["parent"]["case_ref"]["digest"]:
        raise ValueError("existing case changed")
    item = {"key": folder.name, "production_mode": "opencode-cli-go"}
    definition = authored_definition(item, authored, scene, case, snapshot)
    definition["production"] = production
    fixed_json(folder / "case-record.json", case)
    fixed_json(folder / "definition.json", definition)
    frozen = export_trial(folder, folder / "packages", folder.name + "-trial", reuse=True)
    artifact = request(api, "blueprints/import", {"archive_base64": base64.b64encode((folder / "packages/template-snapshot.zip").read_bytes()).decode()})
    old = load(folder / "IMPORT_RECEIPT.json") if (folder / "IMPORT_RECEIPT.json").exists() else None
    if old and (old["artifact_id"] != artifact["id"] or old["digest"] != artifact["digest"]):
        raise ValueError("idempotent import identity changed")
    exported = old["export"] if old else request(api, f"artifacts/{artifact['id']}/development-package",
        {"expected_digest": artifact["digest"], "project_name": folder.name + "-trial", "phase": "P0"})
    with urllib.request.urlopen(api.removesuffix("/api/factory/") + exported["download_url"], timeout=90) as response:
        data = response.read()
    target = folder / "atlas-development-package.zip"
    if target.exists() and target.read_bytes() != data:
        raise ValueError("fixed downloaded package changed")
    target.write_bytes(data)
    with zipfile.ZipFile(target) as archive:
        for name in ("HANDOFF.md", "KNOWLEDGE.md", "ACCEPTANCE_CONTRACT.json", "CURRENT_PHASE.json", "APP_DELIVERY.md", "PROJECT_DECISIONS.json"):
            assert name in archive.namelist(), name
        assert load(folder / "case-record.json") == json.loads(archive.read("blueprint/inputs/shared-case-record.json"))
        assert json.loads(archive.read("blueprint/inputs/model-production.json")) == production
    receipt = {"artifact_id": artifact["id"], "digest": artifact["digest"], "parent": req["parent"],
               "original_frozen_digest": frozen["template_digest"], "case_ref": definition["case_ref"],
               "url": "http://127.0.0.1:5188/factory?view=artifacts&artifact_id=" + artifact["id"],
               "export": exported, "exported_zip_sha256": hashlib.sha256(data).hexdigest(),
               "application_runtime": "not_run", "source": "OpenCode Go bounded revision; fresh independent complete static review"}
    fixed_json(folder / "IMPORT_RECEIPT.json", receipt)
    register_catalog(item, folder)
    return receipt


def run(request_path, *, api, until="complete", round_number=1):
    req = load(request_path)
    root = request_path.parent
    if req["model"] != MODEL or req["campaign_id"] != CAMPAIGN or round_number not in (1, 2):
        raise ValueError("revision authorization binding differs")
    if hashlib.sha256((ROOT / req["authorization_ref"]).read_bytes()).hexdigest() != req["authorization_sha256"]:
        raise ValueError("authorization source changed")
    parent = ROOT / req["parent_folder"]
    imported = load(parent / "IMPORT_RECEIPT.json")
    if any(imported[k] != v for k, v in req["parent"].items()):
        raise ValueError("parent receipt binding differs")
    store = FactoryStore(ROOT / "application-atlas-production-pack/atlas/template-factory", ROOT / "application-atlas-production-pack")
    artifact = next(a for a in store.artifacts() if a["id"] == imported["artifact_id"])
    if artifact["state"] != "withdrawn" or artifact["digest"] != imported["digest"]:
        raise ValueError("original withdrawn candidate binding differs")
    case = CaseLibrary(store).get_case(imported["case_ref"]["case_id"], imported["case_ref"]["revision"])
    if case["digest"] != imported["case_ref"]["digest"]:
        raise ValueError("case r1 differs")
    scene = store.scenario(req["scenario_id"])
    if scene["revision"] != req["scenario_revision"]:
        raise ValueError("scenario r1 differs")
    snapshot = load(parent / "source-snapshot.json")
    if manifest_files(Path(snapshot["local_root"])) != snapshot["files"]:
        raise ValueError("fixed upstream bytes differ")
    ledger = BudgetLedger(store, campaign_id=CAMPAIGN)
    fixed_json(root / "REGISTRATION.json", ledger.register_auxiliary_revision(req["phase"], req["identity"], req))
    base = parent
    if round_number == 2:
        base = root / "home-care-r1"
        failure = load(base / "REVIEW_FAILURE.json")
        if failure.get("verdict") != "needs_changes" or not failure.get("issues"):
            raise ValueError("second content revision requires actual core review findings")
    folder = root / ("home-care-r" + str(round_number))
    folder.mkdir(exist_ok=True)
    leaf = (store.pack / "applications" / (req["leaf"] + ".md")).read_bytes()
    if hashlib.sha256(leaf).hexdigest() != load(parent / "REQUEST.json")["leaf_sha256"]:
        raise ValueError("leaf changed since original production")
    materials = folder / "materials"
    if not materials.exists():
        shutil.copytree(snapshot["local_root"], materials / "upstream")
    original = load(base / "AUTHOR_INPUT.json")
    original_files = {p.name: p.read_text() for p in (base / "acceptance").iterdir() if p.is_file()}
    views = write_candidate(materials / "candidate", original, original_files)
    author_payload = {"request": req, "round": round_number, "parent_content_digest": digest({"authored": original, "acceptance_files": original_files}),
                      "read_views": views, "inventory": manifest_files(materials), "scenario": scene}
    if round_number == 2:
        author_payload["additional_findings"] = load(base / "REVIEW_FAILURE.json")
    budget = {"ledger": ledger, "identity": req["identity"], "phase": req["phase"]}
    author_stage, review_stage = "blueprint-generate-aux-revision-" + str(round_number), "blueprint-spec-review-aux-revision-" + str(round_number)
    try:
        raw = checkpoint(folder / "calls" / author_stage, author_payload, AUTHOR, CLI(), {**budget, "kind": "production", "stage": author_stage}, materials, leaf)
        authored, files = merge_revision(original, raw, snapshot)
        write_candidate(folder, authored, files)
        fixed_json(folder / "source-snapshot.json", snapshot)
        fixed_json(folder / "scenario.json", scene)
        changes = []
        field_changes = [("authored/" + k, original[k] if isinstance(original[k], str) else json.dumps(original[k], ensure_ascii=False, indent=2),
                          authored[k] if isinstance(authored[k], str) else json.dumps(authored[k], ensure_ascii=False, indent=2)) for k in original]
        for name, before, after in [*field_changes, *[("acceptance/" + k, original_files[k], files[k]) for k in files]]:
            changes.extend(difflib.unified_diff([line + "\n" for line in before.splitlines()],
                [line + "\n" for line in after.splitlines()], fromfile="parent/" + name, tofile=folder.name + "/" + name))
        (folder / "CONTENT.diff").write_text("".join(changes))
        if until == "generated":
            return {"status": "generated", "folder": str(folder)}
        fixture = load(folder / "FIXTURE_RESULTS.json")
        if fixture.get("status") != "passed" or fixture.get("probe_sha256") != hashlib.sha256(files["probe.py"].encode()).hexdigest() or fixture.get("kind") != "isolated_fixture_not_application_runtime":
            raise ValueError("isolated deterministic checks must bind current probe before review")
        review_materials = folder / "review-materials"
        if not review_materials.exists():
            shutil.copytree(snapshot["local_root"], review_materials / "upstream")
        views = write_candidate(review_materials / "candidate", authored, files)
        identity = review_identity(req, authored, files, snapshot, scene)
        review_payload = {"input_digest": identity, "request": req, "scenario": scene, "read_views": views,
                          "inventory": manifest_files(review_materials), "checks": list(CHECKS), "revision_round": round_number}
        review = checkpoint(folder / "calls" / review_stage, review_payload, READABLE_REVIEW + "\nReview ALL existing core contracts, five corrections and interactions. Do not waive core defects; non-core feature/style wishes are follow-up only.", CLI(),
                            {**budget, "kind": "review", "stage": review_stage}, review_materials, leaf)
        sessions = {role: load(folder / "calls" / stage / "cli-summary.json")["session_id"] for role, stage in (("author", author_stage), ("review", review_stage))}
        validate_read_coverage(folder / "calls" / review_stage, authored)
        if review.get("verdict") == "needs_changes":
            fixed_json(folder / "REVIEW_FAILURE.json", review)
        validate_review(review, identity, sessions["author"], sessions["review"], len(authored["observations"]))
        used = ledger.segment_usage(req["phase"])["cli_sessions_used"]
        production = {"schema": "atlas.auxiliary-model-production.v1", "mode": "opencode-cli-go", "model": MODEL,
                      "campaign_id": CAMPAIGN, "phase": req["phase"], "review_status": "passed", "review_input_digest": identity,
                      "review_result_digest": digest(review), "source_snapshot_digest": digest(snapshot), "sessions": sessions,
                      "revision_request_digest": digest(req), "parent": req["parent"], "revision_id": folder.name,
                      "stages": {"author": author_stage, "review": review_stage}, "controlled_opencode_calls_added": used,
                      "application_runtime": "not_run", "upstream_runtime": "not_run"}
        fixed_json(folder / "MODEL_PRODUCTION.json", production)
        return publish_auxiliary(folder, req, store, api, production, authored, snapshot, scene, case)
    except Exception as error:
        atomic_json(folder / "STOP.json", {"error": str(error), "registered": (folder / "IMPORT_RECEIPT.json").exists(), "application_runtime": "not_run"})
        raise
    finally:
        atomic_json(root / "BUDGET_AFTER.json", ledger.snapshot())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--api", default="http://127.0.0.1:5199/api/factory/")
    parser.add_argument("--until", choices=("generated", "complete"), default="complete")
    parser.add_argument("--round", type=int, default=1)
    args = parser.parse_args()
    with args.request.parent.joinpath(".revision.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        print(json.dumps(run(args.request.resolve(), api=args.api, until=args.until, round_number=args.round), ensure_ascii=False, indent=2))
