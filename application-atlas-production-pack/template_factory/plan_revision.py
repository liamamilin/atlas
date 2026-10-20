"""Read-only preparation of a bounded revision of a failed, pinned draft.

Preparation is not a repair reservation, queue, review, publication or G1 pass.
The existing repair service must revalidate the request and enforce the ledger
before its effective plan can be consumed by production.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

from .error_contracts import ERROR_SCHEMA, bookmark_bound, required_branches, validate_error_contract
from .store import FactoryError, digest

PREPARATION_SCHEMA = "atlas.failed-plan-revision.v1"
G1_FAILED_JOB = "job_a53c47f3694047489c4f82cfc2e346be"
G1_PLAN_1_DIGEST = "b82eaafd6126d5e21e1ccd734a590b5e8a417f51497465e72a4574ab20873894"
# Exact A04/A12 + search clarification reviewed in this work package. This is
# deliberately not a general-purpose permission to rewrite those text fields.
G1_PATCH_DIGEST = "76673a0a9b28bd52aab8d44208ea58a6764aa78d0d9b541af2ff41e4d237241c"
ALLOWED_SPEC_PATHS = {("acceptance", "A04", "goal"), ("acceptance", "A12", "goal"), ("architecture_markdown",)}

# R6 is a distinct, versioned preparation. Its inputs and this allowlist are
# intentionally fixed to the authorized source-alignment revision.
R6_PREPARATION_SCHEMA = "atlas.failed-plan-revision.v2"
R6_PROGRAM_REUSE_SCHEMA = "atlas.prepared-program-reuse.v1"
R6_SOURCE_JOB = "job_7742b1c124be4c9ab3a0096da5cdd772"
R6_PLAN_DIGEST = "f190b65275ab7c7136f523ba92aecde7c9392440d7676b070393e62ff9137b58"
R6_CASE_BASIS_DIGEST = "a22ff1c065d27aecb0cee21dc6b597f5607375bc8ebc297a3451e708f4da5589"
R6_FACTS_VIEW_DIGEST = "241bf3d99ff497c30be8349cbc70529e08df6146736cb749b55268271889aa4b"
R6_AUTHORIZATION_REF = "docs/template-factory/g1-r6-source-alignment-2026-10-20/authorization/ATLAS_G1_R6_SOURCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt"
R6_AUTHORIZATION_SHA256 = "7c36e8048393bf7b3fd7eecc78c3af76e3189d462310d88955ce283dd4ce0168"
R6_APPROVED_REVISION_REF = "docs/template-factory/g1-r6-source-alignment-2026-10-20/authorization/approved-revision.json"
R6_SOURCE_ARRAYS = {
    "F01": (["S02", "S04", "S06", "S17"], ["S02", "S04", "S06"]),
    "F07": (["S15", "S08"], ["S15"]),
    "F08": (["S09", "S13", "S06", "S11"], ["S01", "S06", "S13"]),
    "F10": (["S04", "S08"], ["S04", "S02"]),
    "F11": (["S10", "S18"], []),
    "F12": (["S14", "S21", "S08"], ["S14", "S21"]),
    "F24": (["S15", "S17"], ["S15"]),
}
R6_REASON_FEATURES = {"F01", "F02", "F03", "F07", "F08", "F09", "F10", "F11", "F12", "F13", "F14", "F17", "F24"}
R6_ARCHITECTURE_OLD = "上游 S04 的点域名正则与 S08 getHostname 是源观察，映射为 adjusted：点不是通用 URL 有效性要求；target 采用上述解析策略。"
R6_ARCHITECTURE_NEW = "上游 S04 记录点域名正则限制，S02 记录新记录包含派生 hostname；这些是固定来源观察。target 的绝对 HTTP(S) URL 解析、允许单标签 hostname 与保留原始 URL 文本，是本模板的 adjusted 设计，采用上述解析策略。"
R6_PROGRAM_PATHS = (
    "acceptance/common.py", "acceptance/p0_library.py", "acceptance/p0_organize.py",
    "acceptance/p0_find_open.py", "acceptance/p0_recovery.py", "acceptance/p1_maturity.py",
    "acceptance/requirements.txt", "acceptance/README.md", "acceptance/runner.json",
)


def _fail(message):
    raise FactoryError(message, "plan_revision_conflict", 409)


def apply_bounded_patch(plan, choices, patch):
    """No whole-spec replacement; untouched fields come from the host baseline."""
    if not isinstance(patch, dict) or set(patch) != {"spec_changes", "file_plan_changes", "case_design_changes"}:
        _fail("revision requires only explicit spec/file-plan/case-design deltas")
    result, design = deepcopy(plan), deepcopy(choices)
    seen = set()
    changes = patch["spec_changes"]
    if not isinstance(changes, list) or not changes or len(changes) > 3:
        _fail("spec patch must contain 1–3 bounded existing-field deltas")
    for change in changes:
        if not isinstance(change, dict) or set(change) != {"path", "old", "new"}:
            _fail("spec patch needs exact old/new values")
        path = change["path"]
        if not isinstance(path, list) or not all(isinstance(x, str) for x in path):
            _fail("invalid spec path")
        key = tuple(path)
        if key not in ALLOWED_SPEC_PATHS or key in seen:
            _fail("spec patch is outside A04/A12/architecture clarification scope")
        seen.add(key)
        target = result["spec"]
        if len(path) == 3:
            matches = [r for r in target[path[0]] if r.get("id") == path[1]]
            if len(matches) != 1:
                _fail("acceptance identity changed")
            target = matches[0]
        field = path[-1]
        if target.get(field) != change["old"] or not isinstance(change["new"], str) or not change["new"].strip():
            _fail("spec old value changed or replacement is not text")
        if key == ("architecture_markdown",) and not change["new"].startswith(change["old"] + "\n"):
            _fail("architecture may only append the clarification; previous contracts remain")
        target[field] = change["new"]
    updates = patch["file_plan_changes"]
    if not isinstance(updates, list) or len(updates) != 1:
        _fail("only the p0_organize file-plan purpose may be revised")
    update = updates[0]
    if not isinstance(update, dict) or set(update) != {"path", "old", "new"} or update["path"] != "acceptance/p0_organize.py":
        _fail("file-plan patch must bind the existing organize purpose")
    matches = [r for r in result["file_plan"] if r.get("path") == update["path"]]
    if len(matches) != 1 or matches[0].get("purpose") != update["old"] or not isinstance(update["new"], str) or not update["new"].strip():
        _fail("file-plan purpose changed")
    matches[0]["purpose"] = update["new"]
    updates = patch["case_design_changes"]
    if not isinstance(updates, list) or len(updates) != 1:
        _fail("only one existing search adaptation may be clarified")
    update = updates[0]
    if (not isinstance(update, dict) or set(update) != {"index", "old", "new"}
            or type(update["index"]) is not int or not 0 <= update["index"] < len(design)):
        _fail("case design patch requires an existing index and exact old/new values")
    old, new = design[update["index"]], update["new"]
    if (old != update["old"] or not isinstance(new, dict) or set(new) != set(old)
            or any(new.get(k) != v for k, v in old.items() if k not in {"capability", "reason"})
            or not all(isinstance(new.get(k), str) and new[k].strip() for k in ("capability", "reason"))):
        _fail("case patch may clarify capability/reason only; evidence and disposition remain pinned")
    design[update["index"]] = new
    # Branch definitions and all references are generated by the host, not
    # supplied as an alternative model-owned copy of the specification.
    branches = required_branches()
    coverage = result["spec"]["contract_coverage"]
    coverage["error_contract"] = {"schema": ERROR_SCHEMA, "branches": branches}
    for row in coverage["features"]:
        refs = [b["id"] for b in branches if row["feature_id"] in b["feature_ids"]]
        if refs:
            row["error_branch_ids"] = refs
    for row in result["file_plan"]:
        refs = [b["id"] for b in branches if row["path"] == b["implementation"]]
        if refs:
            row["error_branch_ids"] = refs
    validate_error_contract(result["spec"], result["file_plan"], required=True)
    return result, design


def _feature_by_id(spec, feature_id):
    matches = [row for row in spec.get("features", []) if isinstance(row, dict) and row.get("id") == feature_id]
    if len(matches) != 1:
        _fail(f"R6 feature identity changed: {feature_id}")
    return matches[0]


def _r6_paths():
    return ({("features", fid, "sources") for fid in R6_SOURCE_ARRAYS}
            | {("features", fid, "reason") for fid in R6_REASON_FEATURES}
            | {("architecture_markdown",)})


def _spec_changes(before, after):
    changes = []
    if before.get("architecture_markdown") != after.get("architecture_markdown"):
        changes.append({"path": ["architecture_markdown"],
                        "old": before.get("architecture_markdown"),
                        "new": after.get("architecture_markdown")})
    old_features = {row.get("id"): row for row in before.get("features", []) if isinstance(row, dict)}
    new_features = {row.get("id"): row for row in after.get("features", []) if isinstance(row, dict)}
    if old_features.keys() != new_features.keys():
        _fail("R6 feature identities changed")
    for fid in sorted(old_features):
        for field in ("sources", "reason"):
            old, new = old_features[fid].get(field), new_features[fid].get(field)
            if old != new:
                changes.append({"path": ["features", fid, field], "old": deepcopy(old), "new": deepcopy(new)})
    return changes


def _apply_r6_patch(plan, patch):
    if not isinstance(patch, dict) or set(patch) != {"spec_changes"}:
        _fail("R6 accepts only the fixed specification source-alignment patch")
    changes = patch["spec_changes"]
    if not isinstance(changes, list):
        _fail("R6 spec_changes must be a list")
    spec = deepcopy(plan["spec"])
    seen = set()
    source_seen = set()
    for change in changes:
        if not isinstance(change, dict) or set(change) != {"path", "old", "new"}:
            _fail("R6 changes require exact old/new values and paths")
        path = change["path"]
        if not isinstance(path, list) or not all(isinstance(part, str) for part in path):
            _fail("R6 change path is invalid")
        key = tuple(path)
        if key in seen:
            _fail("R6 patch repeats a path")
        seen.add(key)
        old, new = change["old"], change["new"]
        if len(path) == 3 and path[0] == "features" and path[2] == "sources":
            feature = _feature_by_id(spec, path[1])
            if path[1] not in R6_SOURCE_ARRAYS or old != R6_SOURCE_ARRAYS[path[1]][0] or new != R6_SOURCE_ARRAYS[path[1]][1]:
                _fail(f"R6 source array change is not authorized: {path[1]}")
            if feature.get("sources") != old:
                _fail(f"R6 source array baseline changed: {path[1]}")
            feature["sources"] = deepcopy(new)
            source_seen.add(path[1])
        elif len(path) == 3 and path[0] == "features" and path[2] == "reason":
            if path[1] not in R6_REASON_FEATURES or not isinstance(old, str) or not isinstance(new, str) or not old.strip() or not new.strip():
                _fail("R6 reason path/value is outside the authorized explanation fields")
            feature = _feature_by_id(spec, path[1])
            if feature.get("reason") != old:
                _fail(f"R6 reason baseline changed: {path[1]}")
            feature["reason"] = new
        elif path == ["architecture_markdown"]:
            text = spec.get("architecture_markdown")
            if (not isinstance(text, str) or old != text or old.count(R6_ARCHITECTURE_OLD) != 1
                    or new != old.replace(R6_ARCHITECTURE_OLD, R6_ARCHITECTURE_NEW, 1)):
                _fail("R6 architecture must be the exact full-field source sentence replacement")
            spec["architecture_markdown"] = new
        else:
            _fail(f"R6 patch path is outside the authorized source explanation fields: {path}")
    if source_seen != set(R6_SOURCE_ARRAYS):
        _fail("R6 patch must include all seven exact feature source-array changes")
    if ("architecture_markdown",) not in seen:
        _fail("R6 patch must include the exact architecture source explanation replacement")
    updated = deepcopy(plan)
    updated["spec"] = spec
    return updated


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _resolve_bound_file(root, relative_path):
    root = Path(root).resolve(strict=True)
    candidate = root / relative_path
    try:
        # Reject symlinks in every path component, including the final file.
        current = root
        for part in Path(relative_path).parts:
            current = current / part
            if current.is_symlink():
                _fail(f"approved R6 input may not contain symlinks: {relative_path}")
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root)
        if not resolved.is_file():
            _fail(f"approved R6 input is not a regular file: {relative_path}")
        return resolved
    except (OSError, ValueError):
        _fail(f"approved R6 input is missing or invalid: {relative_path}")


def _read_bound_json(root, relative_path):
    """Read a regular, nonsymlink project JSON file whose path remains under root."""
    try:
        return json.loads(_resolve_bound_file(root, relative_path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        _fail(f"approved R6 input is missing or invalid: {relative_path}")


def _validate_approved_r6_patch(root, source_authorization, patch):
    expected_auth = {"source_ref": R6_AUTHORIZATION_REF,
                     "source_digest": R6_AUTHORIZATION_SHA256,
                     "revision_ref": R6_APPROVED_REVISION_REF}
    if (not isinstance(source_authorization, dict)
            or set(source_authorization) != set(expected_auth) | {"revision_digest"}
            or any(source_authorization.get(key) != value for key, value in expected_auth.items())
            or not isinstance(source_authorization.get("revision_digest"), str)):
        _fail("R6 request does not bind the fixed approved-revision record")
    authorization_path = _resolve_bound_file(root, R6_AUTHORIZATION_REF)
    authorization = authorization_path.read_bytes()
    if _sha256(authorization) != R6_AUTHORIZATION_SHA256:
        _fail("R6 source authorization bytes changed")
    revision = _read_bound_json(root, R6_APPROVED_REVISION_REF)
    revision_digest = digest(revision)
    if source_authorization["revision_digest"] != revision_digest:
        _fail("R6 approved-revision record digest changed")
    if (revision.get("schema") != "atlas.authorized-source-alignment.v1"
            or revision.get("source_ref") != R6_AUTHORIZATION_REF
            or revision.get("source_digest") != R6_AUTHORIZATION_SHA256
            or revision.get("base_plan_digest") != R6_PLAN_DIGEST
            or revision.get("patch_ref") != "docs/template-factory/g1-r6-source-alignment-2026-10-20/patch.json"
            or not isinstance(revision.get("patch_digest"), str)):
        _fail("R6 approved-revision record does not bind the authorized source and base plan")
    approved_patch = _read_bound_json(root, revision["patch_ref"])
    if digest(approved_patch) != revision["patch_digest"]:
        _fail("R6 approved patch content digest changed")
    paths = [change.get("path") for change in approved_patch.get("spec_changes", []) if isinstance(change, dict)]
    if (not isinstance(revision.get("spec_paths"), list) or paths != revision["spec_paths"]
            or patch != approved_patch):
        _fail("R6 patch differs from the exact host-approved 21-field revision")
    return approved_patch


def _checkpoint_result(store, job_id, name, expected_digest=None):
    record = store.checkpoint(job_id, name)
    if not record or not isinstance(record.get("result"), dict):
        _fail(f"required source checkpoint missing: {name}")
    if (not isinstance(record.get("digest"), str)
            or digest(record["result"]) != record["digest"]
            or (expected_digest is not None and record["digest"] != expected_digest)):
        _fail(f"source checkpoint digest mismatch: {name}")
    return record


def _validate_research_view_binding(facts_view, research_checkpoint):
    if facts_view.get("source_research_digest") != research_checkpoint.get("digest"):
        _fail("R6 accepted facts view is not bound to the current research checkpoint")


def _validate_pinned_case_design(snapshot, checkpoint_name, checkpoint):
    prepared = (snapshot.get("cognitive_repair") or {}).get("prepared_revision")
    if not isinstance(prepared, dict):
        _fail("R6 failed snapshot does not contain the prepared case-design baseline")
    choices = checkpoint.get("result", {}).get("choices")
    expected = prepared.get("case_design")
    expected_digest = prepared.get("case_design_digest")
    if (not isinstance(expected, list) or digest(expected) != expected_digest
            or not isinstance(choices, list) or choices != expected
            or digest(choices) != expected_digest
            or checkpoint_name != "case-adaptation-prepared-" + expected_digest[:16]):
        _fail("R6 case-design checkpoint differs from the original prepared revision")


def build_program_reuse_manifest(store, job_id=R6_SOURCE_JOB):
    """Build the exact R6 reuse manifest from attempt-4 CPs and delivered bytes."""
    if job_id != R6_SOURCE_JOB:
        _fail("program reuse is bound to the original R6 failed job")
    plan_cp = _checkpoint_result(store, job_id, "blueprint-plan-0", R6_PLAN_DIGEST)
    plan = plan_cp["result"]
    generated_root = store.root / "jobs" / job_id / "attempt-4" / "context" / "generated-0"
    rows = {row.get("path"): row for row in plan.get("file_plan", []) if isinstance(row, dict)}
    if len(rows) != 9 or set(rows) != set(R6_PROGRAM_PATHS):
        _fail("attempt-4 plan does not contain the pinned nine program paths")
    entries = []
    for index, path in enumerate(R6_PROGRAM_PATHS):
        name = f"blueprint-code-0-{index}"
        record = _checkpoint_result(store, job_id, name)
        result = record["result"]
        if result.get("path") != path or not isinstance(result.get("content"), str):
            _fail(f"attempt-4 program checkpoint path/content mismatch: {name}")
        content = result["content"].encode("utf-8")
        content_sha = _sha256(content)
        if result.get("reused_sha256") is not None and result["reused_sha256"] != content_sha:
            _fail(f"attempt-4 reused checkpoint hash mismatch: {name}")
        output_path = generated_root / path
        try:
            resolved_root = generated_root.resolve(strict=True)
            resolved = output_path.resolve(strict=True)
            resolved.relative_to(resolved_root)
            on_disk = resolved.read_bytes()
        except (OSError, ValueError):
            _fail(f"attempt-4 delivered program file is missing or outside generated root: {path}")
        if on_disk != content:
            _fail(f"attempt-4 checkpoint bytes differ from delivered file: {path}")
        input_path = store.root / "jobs" / job_id / "attempt-4" / name / "input.json"
        input_digest = None
        input_body = None
        if input_path.is_file():
            input_bytes = input_path.read_bytes()
            input_digest = _sha256(input_bytes)
            try:
                input_body = json.loads(input_bytes)
            except (UnicodeDecodeError, json.JSONDecodeError):
                _fail(f"attempt-4 author input is invalid JSON: {name}")
        elif result.get("reused_sha256") is None:
            _fail(f"newly generated program is missing its author input: {name}")
        elif rows[path].get("reuse") is not True:
            _fail(f"reused source bytes are not marked reuse in pinned plan: {path}")
        source_identity = digest({"file_plan_entry": rows[path], "author_input": input_body,
                                  "reused_sha256": result.get("reused_sha256")})
        entries.append({"path": path, "sha256": content_sha, "checkpoint_name": name,
                        "checkpoint_digest": record["digest"], "input_digest": input_digest,
                        "source_identity_digest": source_identity})
    return {"schema": R6_PROGRAM_REUSE_SCHEMA, "source_job_id": job_id, "source_attempt": 4,
            "source_plan_checkpoint_name": "blueprint-plan-0",
            "source_plan_checkpoint_digest": plan_cp["digest"],
            "source_proposal_digest": plan_cp["digest"], "entries": entries}


def program_reuse_contents(store, manifest):
    """Revalidate a prepared manifest against immutable CPs/files, then return UTF-8 strings."""
    if not isinstance(manifest, dict) or manifest.get("schema") != R6_PROGRAM_REUSE_SCHEMA:
        _fail("unsupported prepared program reuse manifest")
    expected = build_program_reuse_manifest(store, manifest.get("source_job_id"))
    if manifest != expected:
        _fail("prepared program reuse manifest no longer matches attempt-4 checkpoints and files")
    root = store.root / "jobs" / manifest["source_job_id"] / "attempt-4" / "context" / "generated-0"
    contents = {}
    for entry in expected["entries"]:
        raw = (root / entry["path"]).read_bytes()
        if _sha256(raw) != entry["sha256"]:
            _fail(f"prepared program bytes changed: {entry['path']}")
        try:
            contents[entry["path"]] = raw.decode("utf-8")
        except UnicodeDecodeError:
            _fail(f"prepared program is not UTF-8: {entry['path']}")
    return contents


class PreparedRevisionService:
    def __init__(self, store):
        self.store = store

    def prepare(self, job_id, request):
        if isinstance(request, dict) and request.get("schema") == R6_PREPARATION_SCHEMA:
            return self._prepare_r6(job_id, request)
        if not isinstance(request, dict) or set(request) != {"schema", "binding", "patch"} or request.get("schema") != PREPARATION_SCHEMA:
            _fail("unsupported bounded draft revision request")
        if job_id != G1_FAILED_JOB or digest(request["patch"]) != G1_PATCH_DIGEST:
            _fail("this preparation supports only the exact current G1 clarification patch")
        job = self.store.job(job_id)
        snapshot = job["snapshot"]
        if job["kind"] != "blueprint-production" or job["state"] != "failed" or not bookmark_bound(snapshot):
            _fail("preparation requires the bound failed bookmark product")
        binding = request["binding"]
        v1, scenario = snapshot["v1"], snapshot["scenario"]
        if not isinstance(binding, dict) or set(binding) != {"job_id", "checkpoint_name", "checkpoint_digest", "plan_id", "plan_digest", "product_id", "scenario_id", "scenario_revision", "case_basis_digest", "case_design_checkpoint_digest"}:
            _fail("complete fixed job/plan/scenario/case/checkpoint binding is required")
        if binding["checkpoint_digest"] != G1_PLAN_1_DIGEST:
            _fail("preparation must bind the exact current plan-1 digest")
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM v1_plan WHERE id=?", (v1["plan_id"],)).fetchone()
        if not row:
            _fail("fixed batch plan is missing")
        fixed_plan = json.loads(row[0])
        if digest({k: v for k, v in fixed_plan.items() if k != "digest"}) != fixed_plan.get("digest"):
            _fail("fixed batch plan digest changed")
        expected = {"job_id": job_id, "checkpoint_name": "blueprint-plan-1",
                    "plan_id": v1["plan_id"], "plan_digest": fixed_plan["digest"],
                    "product_id": v1["product_id"], "scenario_id": scenario["id"],
                    "scenario_revision": scenario["revision"],
                    "case_basis_digest": snapshot["case_basis"]["basis_digest"]}
        if any(binding.get(k) != val for k, val in expected.items()) or fixed_plan["campaign_id"] != v1["campaign_id"]:
            _fail("revision identity differs from the pinned failed product")
        seeds = [s for s in fixed_plan.get("seeds", []) if s.get("product_id") == v1["product_id"]]
        if (len(seeds) != 1 or seeds[0].get("scenario") != scenario
                or (seeds[0].get("case_basis") is not None
                    and seeds[0]["case_basis"] != snapshot["case_basis"])):
            _fail("failed product no longer agrees with its fixed plan seed")
        checkpoint = self.store.checkpoint(job_id, binding["checkpoint_name"])
        adaptation = self.store.checkpoint(job_id, "case-adaptation-aggregate-v1")
        for record, expected_digest in ((checkpoint, binding["checkpoint_digest"]), (adaptation, binding["case_design_checkpoint_digest"])):
            if not record or record.get("digest") != expected_digest or digest(record.get("result")) != expected_digest:
                _fail("checkpoint is missing, changed or has a mismatched recorded digest")
        effective, choices = apply_bounded_patch(checkpoint["result"], adaptation["result"]["choices"], request["patch"])
        from .cognition import validate_file_plan
        from .contract_scope import validate_contract_coverage
        validate_file_plan(effective, allow_reuse=True, require_runtime=True)
        validate_contract_coverage(effective["spec"], required=True)
        return {"schema": PREPARATION_SCHEMA, "state": "prepared_not_queued", "binding": deepcopy(binding),
                "request_digest": digest(request), "base_proposal_digest": checkpoint["digest"],
                "effective_plan": effective, "effective_plan_digest": digest(effective),
                "case_design": choices, "case_design_digest": digest(choices),
                "case_adaptation_input": {"mode": "host-exact-search-clarification", "prior_checkpoint_digest": adaptation["digest"], "search_fields": ["title", "hostname", "description"], "case_basis_digest": binding["case_basis_digest"]},
                "evidence_scope": "Host preparation only; independent design/frozen review and real runtime remain required. No queue, calls, repairs, limits or windows changed."}

    def _prepare_r6(self, job_id, request):
        if set(request) != {"schema", "binding", "patch", "source_authorization", "program_reuse_manifest"}:
            _fail("R6 preparation requires the exact authorization and program-reuse bindings")
        if job_id != R6_SOURCE_JOB:
            _fail("R6 preparation is bound to the original failed job")
        repo_root = self.store.pack.resolve().parent
        approved_patch = _validate_approved_r6_patch(repo_root, request["source_authorization"], request["patch"])

        job = self.store.job(job_id)
        snapshot = job["snapshot"]
        if job["kind"] != "blueprint-production" or job["state"] != "failed" or job["attempt"] != 4 or not bookmark_bound(snapshot):
            _fail("R6 requires the pinned failed attempt-4 bookmark job")
        binding = request["binding"]
        required_binding = {"job_id", "attempt", "snapshot_digest", "checkpoint_name", "checkpoint_digest",
                            "plan_id", "plan_digest", "product_id", "scenario_id", "scenario_revision",
                            "case_basis_digest", "facts_view_checkpoint_name", "facts_view_checkpoint_digest",
                            "facts_view_digest", "case_design_checkpoint_name", "case_design_checkpoint_digest",
                            "original_proposal_digest"}
        if not isinstance(binding, dict) or set(binding) != required_binding:
            _fail("complete R6 job, plan, source-view and case-design binding is required")
        v1, scenario = snapshot["v1"], snapshot["scenario"]
        expected = {"job_id": job_id, "attempt": 4, "snapshot_digest": digest(snapshot),
                    "checkpoint_name": "blueprint-plan-0", "checkpoint_digest": R6_PLAN_DIGEST,
                    "plan_id": v1["plan_id"], "product_id": v1["product_id"],
                    "scenario_id": scenario["id"], "scenario_revision": scenario["revision"],
                    "case_basis_digest": R6_CASE_BASIS_DIGEST,
                    "facts_view_checkpoint_name": "blueprint-accepted-facts-view",
                    "facts_view_digest": R6_FACTS_VIEW_DIGEST,
                    "original_proposal_digest": R6_PLAN_DIGEST}
        if any(binding.get(k) != value for k, value in expected.items()):
            _fail("R6 request binding differs from the pinned failed product and current inputs")
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM v1_plan WHERE id=?", (v1["plan_id"],)).fetchone()
        if not row:
            _fail("fixed R6 batch plan is missing")
        fixed_plan = json.loads(row[0])
        if (fixed_plan.get("digest") != binding["plan_digest"]
                or digest({k: v for k, v in fixed_plan.items() if k != "digest"}) != fixed_plan.get("digest")
                or fixed_plan.get("campaign_id") != v1["campaign_id"]):
            _fail("R6 fixed plan digest or campaign changed")
        seeds = [seed for seed in fixed_plan.get("seeds", []) if seed.get("product_id") == v1["product_id"]]
        if (len(seeds) != 1 or seeds[0].get("scenario") != scenario
                or (seeds[0].get("case_basis") is not None
                    and seeds[0]["case_basis"] != snapshot["case_basis"])):
            _fail("R6 failed product no longer agrees with its fixed plan seed")

        plan_cp = _checkpoint_result(self.store, job_id, binding["checkpoint_name"], binding["checkpoint_digest"])
        facts_cp = _checkpoint_result(self.store, job_id, binding["facts_view_checkpoint_name"], binding["facts_view_checkpoint_digest"])
        facts_view = facts_cp["result"]
        if facts_view.get("view_digest") != binding["facts_view_digest"] or facts_view.get("basis_digest") != R6_CASE_BASIS_DIGEST:
            _fail("R6 accepted facts view is stale or has changed")
        from .cases import CaseLibrary
        cases = CaseLibrary(self.store, initialize=False)
        cases.require_admissible(snapshot["case_basis"])
        cases.validate_facts_view(facts_view, snapshot["case_basis"])
        design_cp = _checkpoint_result(self.store, job_id, binding["case_design_checkpoint_name"], binding["case_design_checkpoint_digest"])
        if not binding["case_design_checkpoint_name"].startswith("case-adaptation-prepared-") or not isinstance(design_cp["result"].get("choices"), list):
            _fail("R6 requires the pinned prepared case-design checkpoint")
        _validate_pinned_case_design(snapshot, binding["case_design_checkpoint_name"], design_cp)
        cases.require_design_evidence(snapshot["case_basis"], design_cp["result"]["choices"])

        effective = _apply_r6_patch(plan_cp["result"], approved_patch)
        research_cp = _checkpoint_result(self.store, job_id, "blueprint-research")
        _validate_research_view_binding(facts_view, research_cp)
        research_sources = research_cp["result"].get("sources")
        eligible = set(facts_view.get("accepted_evidence_ids", []))
        if not isinstance(research_sources, list) or not isinstance(eligible, set):
            _fail("R6 current research/source view is malformed")
        current_sources = [row for row in research_sources if isinstance(row, dict) and row.get("name") in eligible]
        current_sources.append({"id": "S01"})
        from .source_references import validate_feature_source_references
        reference_report = validate_feature_source_references(effective["spec"], current_sources,
                                                              binding={"job_id": job_id, "attempt": 4,
                                                                       "facts_view_digest": binding["facts_view_digest"],
                                                                       "case_basis_digest": binding["case_basis_digest"]})

        from .cognition import validate_file_plan
        from .contract_scope import validate_contract_coverage
        validate_file_plan(effective, allow_reuse=True, require_runtime=True)
        validate_contract_coverage(effective["spec"], required=True)
        actual_manifest = build_program_reuse_manifest(self.store, job_id)
        if request["program_reuse_manifest"] != actual_manifest:
            _fail("R6 program-reuse manifest differs from attempt-4 checkpoints and delivered bytes")
        # Resolve and verify every exact byte now, before any resumed author call.
        program_reuse_contents(self.store, actual_manifest)
        choices = deepcopy(design_cp["result"]["choices"])
        actual_spec_changes = _spec_changes(plan_cp["result"]["spec"], effective["spec"])
        if not actual_spec_changes or any(tuple(change["path"]) not in _r6_paths() for change in actual_spec_changes):
            _fail("R6 effective specification contains an unexpected or empty change")
        old_repair = snapshot.get("cognitive_repair", {})
        old_scope = old_repair.get("repair_scope")
        if not isinstance(old_scope, dict) or not isinstance(old_scope.get("authored_field_paths"), list):
            _fail("R6 cumulative repair scope is missing from the original failed job")
        cumulative_scope = deepcopy(old_scope)
        cumulative_paths = [list(path) for path in cumulative_scope["authored_field_paths"]]
        for change in actual_spec_changes:
            path = change["path"]
            if path not in cumulative_paths:
                cumulative_paths.append(path)
        cumulative_scope["authored_field_paths"] = cumulative_paths
        incremental_diff = {"base_proposal_digest": plan_cp["digest"],
                            "effective_plan_digest": digest(effective),
                            "spec_changes": actual_spec_changes,
                            "program_byte_changes": 0,
                            "program_reuse_manifest_digest": digest(actual_manifest)}
        return {"schema": R6_PREPARATION_SCHEMA, "state": "prepared_not_queued",
                "binding": deepcopy(binding), "request_digest": digest(request),
                "base_proposal_digest": plan_cp["digest"], "effective_plan": effective,
                "effective_plan_digest": digest(effective), "case_design": choices,
                "case_design_digest": digest(choices), "source_reference_report": reference_report,
                # Keep the established prepared-revision response contract so
                # cognition can bind and reuse the existing case-design choice
                # checkpoint without asking for a new adaptation call.
                "case_adaptation_input": {
                    "mode": "host-exact-search-clarification",
                    "prior_checkpoint_digest": design_cp["digest"],
                    "search_fields": ["title", "hostname", "description"],
                    "case_basis_digest": binding["case_basis_digest"],
                },
                "prepared_program_reuse": deepcopy(actual_manifest),
                "incremental_diff": incremental_diff,
                "cumulative_repair_scope": cumulative_scope,
                "evidence_scope": "Host preparation only; source references and all nine attempt-4 program bytes are bound. No queue, model calls, budget, repair limit or window changed."}
