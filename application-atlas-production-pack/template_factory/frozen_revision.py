"""Deterministic, authorized revisions of a reviewed frozen candidate.

This is the frozen-candidate branch of PreparedRevisionService, not a retry
or a second producer. Preparation never changes queue or budget state.
"""
from __future__ import annotations

from copy import deepcopy
import difflib
import hashlib
import json
from pathlib import Path

from .store import FactoryError, digest

SCHEMA = "atlas.frozen-plan-revision.v1"
PROGRAM_SCHEMA = "atlas.frozen-program-revision.v1"
SCOPE_VERSION = "atlas.aggregate-repair-scope.v3"
PROGRAM_PATHS = (
    "acceptance/common.py", "acceptance/p0_library.py", "acceptance/p0_organize.py",
    "acceptance/p0_find_open.py", "acceptance/p0_recovery.py", "acceptance/p1_maturity.py",
    "acceptance/requirements.txt", "acceptance/README.md", "acceptance/runner.json",
)
REPLACE_PATHS = {
    "acceptance/p0_library.py", "acceptance/p1_maturity.py",
    "acceptance/README.md", "acceptance/runner.json",
}
SPEC_PATHS = {("architecture_markdown",), ("acceptance", "A03", "goal")}


def fail(message):
    raise FactoryError(message, "frozen_revision_conflict", 409)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bound_file(root, reference):
    from .plan_revision import _resolve_bound_file
    if not isinstance(reference, str) or not reference or Path(reference).is_absolute() or ".." in Path(reference).parts:
        fail("revision material must be a bounded relative file")
    return _resolve_bound_file(root, reference)


def authorization(store, value):
    """Resolve an exact source/approved-revision entry reviewed with host code."""
    if not isinstance(value, dict) or set(value) != {"source_ref", "source_digest", "revision_ref", "revision_digest"}:
        fail("complete source and approved-revision authorization is required")
    try:
        registry = json.loads(Path(__file__).with_name("revision_authorizations.json").read_text())
        entries = registry["authorizations"]
        matches = [row for row in entries if row.get("source_ref") == value["source_ref"]
                   and row.get("source_digest") == value["source_digest"]
                   and row.get("revision_ref") == value["revision_ref"]
                   and row.get("revision_digest") == value["revision_digest"]]
        if len(matches) != 1:
            fail("source/approved revision is not in the checked host authorization registry")
        root = store.pack.resolve().parent
        source = bound_file(root, value["source_ref"]).read_bytes()
        record = json.loads(bound_file(root, value["revision_ref"]).read_bytes())
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise FactoryError("revision authorization is unavailable or malformed", "frozen_revision_conflict", 409) from error
    if sha(source) != value["source_digest"] or digest(record) != value["revision_digest"]:
        fail("revision authorization bytes or approved record changed")
    if (record.get("schema") != "atlas.frozen-revision-authorization.v1"
            or record.get("source_authorization") != {k: value[k] for k in ("source_ref", "source_digest")}):
        fail("approved revision is detached from its original authorization")
    return record


def apply_patch(plan, patch):
    """Keep unaddressed fields from the host, with no whole-spec replacement."""
    from .plan_revision import _at_path, _set_path
    if not isinstance(patch, dict) or set(patch) != {"spec_changes", "file_plan_changes", "program_changes"}:
        fail("frozen revision accepts only explicit spec/file-plan/program changes")
    changes = patch["spec_changes"]
    if not isinstance(changes, list) or not changes or len(changes) > 2:
        fail("frozen revision requires one or two bounded spec changes")
    result = deepcopy(plan)
    seen = set()
    for change in changes:
        if (not isinstance(change, dict) or set(change) != {"path", "old", "new"}
                or not isinstance(change["path"], list) or not all(isinstance(p, str) for p in change["path"])):
            fail("spec changes need identity-addressed paths and exact old/new values")
        path = tuple(change["path"])
        if path not in SPEC_PATHS or path in seen:
            fail("spec change is outside the authorized contract convergence fields")
        if (_at_path(result["spec"], list(path)) != change["old"]
                or not isinstance(change["new"], str) or not change["new"].strip()
                or change["new"] == change["old"]):
            fail("spec baseline changed or replacement is empty/unchanged")
        _set_path(result["spec"], list(path), change["new"])
        seen.add(path)
    if ("architecture_markdown",) not in seen:
        fail("contract convergence must clarify the architecture")
    rows = patch["file_plan_changes"]
    if not isinstance(rows, list):
        fail("file-plan changes must be explicit")
    by_path = {row["path"]: row for row in result["file_plan"]}
    if set(by_path) != set(PROGRAM_PATHS) or len(result["file_plan"]) != 9:
        fail("frozen revision must preserve the exact nine-file inventory")
    changed = set()
    for change in rows:
        if not isinstance(change, dict) or set(change) != {"path", "old", "new"}:
            fail("file-plan changes need complete old/new rows")
        path, old, new = change["path"], change["old"], change["new"]
        if (path not in by_path or path in changed or old != by_path[path]
                or not isinstance(new, dict) or set(new) != set(old)
                or any(old[k] != new[k] for k in old if k not in {"purpose", "reuse"})
                or type(new.get("reuse")) is not bool
                or not isinstance(new.get("purpose"), str) or not new["purpose"].strip()
                or (path not in REPLACE_PATHS and new["purpose"] != old["purpose"])):
            fail("file-plan change exceeds exact reuse/purpose scope")
        by_path[path].update(new)
        changed.add(path)
    for path, row in by_path.items():
        if row.get("reuse") is not (path not in REPLACE_PATHS):
            fail("file-plan modes must be four replacements and five exact reuses")
    return result


def _checkpoint(store, job_id, name, expected_digest):
    cp = store.checkpoint(job_id, name)
    if not cp or cp.get("digest") != expected_digest or digest(cp.get("result")) != expected_digest:
        fail("source checkpoint changed: " + name)
    return cp["result"]


def base_context(store, binding):
    """Verify the actual latest blocked review, frozen bytes and originating inputs."""
    from .api import artifact as find_artifact, controlled_path
    from .blueprints import verify_frozen
    from .cases import CaseLibrary
    from .v1_batches import BatchService
    keys = {"job_id", "attempt", "snapshot_digest", "artifact_id", "artifact_digest", "archive_sha256",
            "acceptance_id", "acceptance_digest", "producer_job_id", "campaign_id", "plan_id", "plan_digest",
            "product_id", "scenario_id", "scenario_revision", "case_basis_digest", "facts_view_digest",
            "plan_checkpoint_name", "plan_checkpoint_digest", "facts_view_checkpoint_digest",
            "case_design_checkpoint_name", "case_design_checkpoint_digest", "research_checkpoint_digest"}
    if not isinstance(binding, dict) or set(binding) != keys:
        fail("complete frozen candidate, latest review and producer binding is required")
    review = store.job(binding["job_id"])
    snap = review["snapshot"]
    artifact = find_artifact(store, binding["artifact_id"])
    if (review["kind"] != "cognitive-review" or review["state"] != "needs_review"
            or review["attempt"] != binding["attempt"] or digest(snap) != binding["snapshot_digest"]
            or snap.get("artifact_id") != artifact["id"] or snap.get("artifact_digest") != binding["artifact_digest"]
            or artifact["digest"] != binding["artifact_digest"] or artifact["job_id"] != binding["producer_job_id"]):
        fail("frozen review or candidate is stale, changed or not a valid blocked baseline")
    with store.connect() as con:
        latest = con.execute("SELECT id,attempt FROM job WHERE kind='cognitive-review' "
                             "AND json_extract(snapshot,'$.artifact_id')=? "
                             "AND json_extract(snapshot,'$.artifact_digest')=? "
                             "ORDER BY created_at DESC,rowid DESC LIMIT 1", (artifact["id"], artifact["digest"])).fetchone()
        row = con.execute("SELECT body FROM acceptance WHERE job_id=? AND digest=? "
                          "ORDER BY created_at DESC,rowid DESC LIMIT 1", (review["id"], artifact["digest"])).fetchone()
    acceptance = json.loads(row[0]) if row else None
    if (not latest or latest["id"] != review["id"] or latest["attempt"] != review["attempt"]
            or not isinstance(acceptance, dict) or acceptance.get("id") != binding["acceptance_id"]
            or digest(acceptance) != binding["acceptance_digest"]
            or acceptance.get("job_attempt", 1) != review["attempt"]
            or acceptance.get("outcome") not in {"blocked", "uncertain"}):
        fail("revision requires this candidate's latest valid blocked/uncertain acceptance")
    bundle = controlled_path(store, artifact["bundle_path"])
    frozen = verify_frozen(bundle, artifact["digest"])
    archive = controlled_path(store, artifact["archive_path"])
    if sha(archive.read_bytes()) != binding["archive_sha256"]:
        fail("frozen candidate archive changed")
    producer = store.job(artifact["job_id"])
    original = producer["snapshot"]
    v1, scene, basis = original.get("v1", {}), original.get("scenario", {}), original.get("case_basis", {})
    expected = {"campaign_id": v1.get("campaign_id"), "plan_id": v1.get("plan_id"),
                "plan_digest": v1.get("plan_digest"), "product_id": v1.get("product_id"),
                "scenario_id": scene.get("id"), "scenario_revision": scene.get("revision"),
                "case_basis_digest": basis.get("basis_digest")}
    if producer["state"] != "completed" or any(binding[k] != value for k, value in expected.items()):
        fail("candidate identity differs from its completed producer")
    if (snap.get("v1") != v1 or snap.get("scenario") != scene or snap.get("case_basis") != basis
            or frozen.get("scenario") != scene or frozen.get("case_basis") != basis):
        fail("frozen scenario/case identity changed")
    plan = BatchService(store).plan(binding["plan_id"])
    seeds = [seed for seed in plan.get("seeds", []) if seed.get("product_id") == binding["product_id"]]
    if (plan.get("digest") != binding["plan_digest"] or plan.get("campaign_id") != binding["campaign_id"]
            or plan.get("segment") != "G1" or len(seeds) != 1 or seeds[0].get("scenario") != scene):
        fail("frozen revision no longer matches its fixed G1 seed")
    proposal = _checkpoint(store, producer["id"], binding["plan_checkpoint_name"], binding["plan_checkpoint_digest"])
    facts = _checkpoint(store, producer["id"], "blueprint-accepted-facts-view", binding["facts_view_checkpoint_digest"])
    adaptation = _checkpoint(store, producer["id"], binding["case_design_checkpoint_name"], binding["case_design_checkpoint_digest"])
    research = _checkpoint(store, producer["id"], "blueprint-research", binding["research_checkpoint_digest"])
    if (facts.get("view_digest") != binding["facts_view_digest"] or facts != frozen.get("case_facts_view")
            or facts.get("source_research_digest") != digest(research)):
        fail("accepted facts are detached from the fixed research/frozen view")
    library = CaseLibrary(store, initialize=False)
    library.require_admissible(basis)
    library.validate_facts_view(facts, basis)
    choices = adaptation.get("choices")
    library.require_design_evidence(basis, choices)
    if choices != artifact.get("provenance", {}).get("case_design"):
        fail("case adaptation changed from the frozen candidate")
    # A derived frozen spec may add host metadata, never change authored fields.
    if any(frozen.get(k) != value for k, value in proposal["spec"].items()):
        fail("producer authored proposal differs from the frozen specification")
    return artifact, bundle, proposal, choices, research, facts, acceptance


def build_program_manifest(store, binding, patch, prepared_root):
    """Apply exact spans to frozen source bytes and bind four prepared files."""
    from .api import artifact as find_artifact, controlled_path
    artifact = find_artifact(store, binding["artifact_id"])
    source = controlled_path(store, artifact["bundle_path"]) / "source"
    rows = patch.get("program_changes")
    if (not isinstance(rows, list) or len(rows) != 4
            or any(not isinstance(row, dict) or not isinstance(row.get("path"), str) for row in rows)
            or {row["path"] for row in rows} != REPLACE_PATHS):
        fail("program changes must contain exactly the four authorized replacements")
    changes = {row["path"]: row for row in rows}
    entries = []
    for path in PROGRAM_PATHS:
        before = bound_file(source, path).read_bytes()
        after = before
        spans = []
        reference = None
        if path in REPLACE_PATHS:
            row = changes[path]
            if set(row) != {"path", "patch"} or not isinstance(row["patch"], list) or not row["patch"]:
                fail("replacement requires exact nonempty patch spans")
            value = before.decode("utf-8")
            for span in row["patch"]:
                if (not isinstance(span, dict) or set(span) != {"old", "new"}
                        or not isinstance(span["old"], str) or not span["old"]
                        or not isinstance(span["new"], str) or value.count(span["old"]) != 1):
                    fail("replacement span must match the current bytes exactly once: " + path)
                value = value.replace(span["old"], span["new"], 1)
            spans = deepcopy(row["patch"])
            after = value.encode("utf-8")
            reference = str(Path(prepared_root) / Path(path).name)
            if bound_file(store.pack.resolve().parent, reference).read_bytes() != after or after == before:
                fail("prepared replacement differs from its exact patch or is unchanged: " + path)
        entries.append({"path": path, "mode": "replace" if path in REPLACE_PATHS else "reuse",
                        "before_sha256": sha(before), "after_sha256": sha(after),
                        "patch": spans, "patch_digest": digest(spans), "prepared_ref": reference})
    return {"schema": PROGRAM_SCHEMA, "artifact_id": artifact["id"], "artifact_digest": artifact["digest"],
            "source_bundle_path": artifact["bundle_path"], "prepared_root": prepared_root, "entries": entries}


def program_contents(store, manifest):
    from .api import controlled_path
    if not isinstance(manifest, dict) or manifest.get("schema") != PROGRAM_SCHEMA:
        fail("unsupported frozen program revision")
    source = controlled_path(store, manifest["source_bundle_path"]) / "source"
    rows = manifest.get("entries")
    if (not isinstance(rows, list) or len(rows) != 9
            or {row.get("path") for row in rows if isinstance(row, dict)} != set(PROGRAM_PATHS)):
        fail("program manifest must bind each of the nine source paths exactly once")
    result = {}
    for row in rows:
        path = row["path"]
        before = bound_file(source, path).read_bytes()
        after = before
        mode = "replace" if path in REPLACE_PATHS else "reuse"
        if row.get("mode") != mode or row.get("before_sha256") != sha(before) or digest(row.get("patch")) != row.get("patch_digest"):
            fail("program source or patch binding changed: " + path)
        if mode == "replace":
            value = before.decode("utf-8")
            for span in row["patch"]:
                if value.count(span["old"]) != 1:
                    fail("source replacement no longer matches: " + path)
                value = value.replace(span["old"], span["new"], 1)
            after = value.encode("utf-8")
            if bound_file(store.pack.resolve().parent, row["prepared_ref"]).read_bytes() != after or after == before:
                fail("prepared program no longer matches: " + path)
        elif row.get("patch") != [] or row.get("prepared_ref") is not None:
            fail("reuse cannot carry replacement bytes")
        if sha(after) != row.get("after_sha256"):
            fail("program output hash changed: " + path)
        result[path] = after.decode("utf-8")
    return result


def prepare(store, job_id, request):
    if not isinstance(request, dict) or set(request) != {"schema", "binding", "patch", "source_authorization", "prepared_program_revision", "review_config"} or request.get("schema") != SCHEMA:
        fail("unsupported frozen revision request shape")
    record = authorization(store, request["source_authorization"])
    for material in record.get("review_materials", []):
        if sha(bound_file(store.pack.resolve().parent, material["path"]).read_bytes()) != material["sha256"]:
            fail("approved review material changed before preparation")
    if (request["binding"].get("job_id") != job_id or record.get("binding") != request["binding"]
            or record.get("patch_digest") != digest(request["patch"])
            or record.get("program_revision_digest") != digest(request["prepared_program_revision"])
            or record.get("review_config") != request["review_config"]):
        fail("request differs from its approved candidate, exact patch, program bytes or review config")
    config = request["review_config"]
    if (set(config) != {"model", "language", "timeout", "repair_attempts"}
            or config != {"model": "opencode-go/deepseek-v4.1-flash", "language": "zh", "timeout": 1800, "repair_attempts": 0}):
        fail("revision must use the authorized model/language/timeout with author repairs disabled")
    artifact, bundle, plan, choices, research, facts, acceptance = base_context(store, request["binding"])
    effective = apply_patch(plan, request["patch"])
    manifest = build_program_manifest(store, request["binding"], request["patch"], record["prepared_root"])
    if manifest != request["prepared_program_revision"]:
        fail("program manifest differs from frozen baseline and approved replacements")
    program_contents(store, manifest)
    from .cognition import validate_file_plan
    from .contract_scope import validate_contract_coverage, validate_repair_scope
    from .source_references import validate_feature_source_references
    validate_file_plan(effective, allow_reuse=True, require_runtime=True)
    validate_contract_coverage(effective["spec"], required=True)
    available = [row for row in research["sources"] if row.get("name") in set(facts["accepted_evidence_ids"])]
    available.append({"id": "S01"})
    source_report = validate_feature_source_references(effective["spec"], available, binding={"artifact_id": artifact["id"], "facts_view_digest": facts["view_digest"]})
    scope = deepcopy(record["repair_scope"])
    validate_repair_scope(scope, plan["spec"], scope["edit_paths"])
    if set(map(tuple, scope["authored_field_paths"])) != SPEC_PATHS or set(scope["edit_paths"]) != REPLACE_PATHS:
        fail("approved repair scope exceeds the contract convergence boundary")
    return {"schema": SCHEMA, "state": "prepared_not_queued", "binding": deepcopy(request["binding"]),
            "request_digest": digest(request), "base_proposal_digest": digest(plan),
            "effective_plan": effective, "effective_plan_digest": digest(effective),
            "case_design": choices, "case_design_digest": digest(choices), "source_reference_report": source_report,
            "case_adaptation_input": {"mode": "host-frozen-contract-convergence", "prior_checkpoint_digest": request["binding"]["case_design_checkpoint_digest"], "case_basis_digest": request["binding"]["case_basis_digest"]},
            "prepared_program_revision": manifest, "cumulative_repair_scope": scope,
            "source_authorization": deepcopy(request["source_authorization"]), "review_config": deepcopy(config),
            "authorization_limits": deepcopy(record["limits"]), "authorization_timing": deepcopy(record["timing"]),
            "incremental_diff": deepcopy(request["patch"]), "baseline_acceptance_digest": digest(acceptance),
            "evidence_scope": "Read-only deterministic preparation; no queue, call, repair or window activation."}


def review_evidence(store, prepared, request, contents):
    """Give reviews actual old/new programs and authorization, not just file-plan prose."""
    from .api import controlled_path
    checked = prepare(store, request["binding"]["job_id"], request)
    if digest(checked) != digest(prepared) or program_contents(store, prepared["prepared_program_revision"]) != contents:
        fail("prepared review material changed")
    source = controlled_path(store, prepared["prepared_program_revision"]["source_bundle_path"]) / "source"
    files = {}
    for path, value in contents.items():
        files["program-evidence/source/" + path] = bound_file(source, path).read_bytes()
        files["program-evidence/prepared/" + path] = value.encode("utf-8")
    record = authorization(store, request["source_authorization"])
    root = store.pack.resolve().parent
    for key in ("source_ref", "revision_ref"):
        ref = request["source_authorization"][key]
        files["program-evidence/authorization/" + Path(ref).name] = bound_file(root, ref).read_bytes()
    for row in record.get("review_materials", []):
        raw = bound_file(root, row["path"]).read_bytes()
        if sha(raw) != row["sha256"]:
            fail("review disposition material changed")
        files["program-evidence/authorization/" + Path(row["path"]).name] = raw
    manifest = {"schema": "atlas.prepared-phase-review-program-evidence.v1", "prepared_request_digest": prepared["request_digest"],
                "effective_plan_digest": prepared["effective_plan_digest"], "prepared_program_revision": prepared["prepared_program_revision"],
                "files": {path: sha(raw) for path, raw in sorted(files.items())}}
    files["program-evidence/PROGRAM_EVIDENCE.json"] = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True).encode()
    return {"manifest": manifest, "files": files, "digest": digest(manifest)}


def program_diff(store, prepared, candidate):
    from .api import controlled_path
    manifest = prepared["prepared_program_revision"]
    contents = program_contents(store, manifest)
    source = controlled_path(store, manifest["source_bundle_path"]) / "source"
    diffs = {}
    for entry in manifest["entries"]:
        path = entry["path"]
        raw = (candidate / path).read_bytes()
        if raw != contents[path].encode():
            fail("candidate bytes do not match approved program manifest: " + path)
        if entry["mode"] == "replace":
            diffs[path] = "".join(difflib.unified_diff((source / path).read_text().splitlines(keepends=True), contents[path].splitlines(keepends=True), fromfile="frozen-baseline/" + path, tofile="revised/" + path))
    return {"schema": "atlas.frozen-revision-diff.v1", "binding": prepared["binding"],
            "prepared_request_digest": prepared["request_digest"], "spec_changes": prepared["incremental_diff"]["spec_changes"],
            "program_manifest": manifest, "program_diffs": diffs, "source_authorization": prepared["source_authorization"]}
