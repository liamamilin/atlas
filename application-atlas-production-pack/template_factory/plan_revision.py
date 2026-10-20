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

# R7 is a separate, explicitly authorized continuation of the failed R6
# candidate. It does not alter the R1/R6 preparation contracts above.
R7_PREPARATION_SCHEMA = "atlas.failed-plan-revision.v3"
R7_PROGRAM_REVISION_SCHEMA = "atlas.prepared-program-revision.v1"
R7_SOURCE_JOB = "job_f3e32b56036b4ec7bea0c00d6a2a8dc4"
R7_SOURCE_ATTEMPT = 1
R7_SOURCE_PROPOSAL_DIGEST = "6f806d9416cd1c5a724e980dece7330dac651c8a838d469db409d940a493f158"
R7_SOURCE_CANDIDATE_SHA256 = "3259239fd8a87fc3f4bf6c6ccd442f507a572db54e8e70b9dc9889c68f3855d3"
R7_AGGREGATE_DIGEST = "78150ff8071af6e1e4a35365d965b8644140d2157ad27356e91ccad644981672"
R7_CASE_BASIS_DIGEST = R6_CASE_BASIS_DIGEST
R7_FACTS_VIEW_DIGEST = R6_FACTS_VIEW_DIGEST
R7_AUTHORIZATION_REF = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/authorization/ATLAS_G1_R7_ACCEPTANCE_ALIGNMENT_CODEX_INSTRUCTIONS.txt"
R7_AUTHORIZATION_SHA256 = "5fb0792b769739f070f68af6ea196473671c791cd895989026ebf9520e282562"
R7_APPROVED_REVISION_REF = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/authorization/approved-revision.json"
R7_PATCH_REF = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/patch.json"
R7_PROGRAMS_REF = "docs/template-factory/g1-r7-acceptance-alignment-2026-10-20/prepared-programs/acceptance"
R7_PROGRAM_PATHS = R6_PROGRAM_PATHS
R7_REPLACE_PATHS = {"acceptance/p0_library.py", "acceptance/p0_find_open.py",
                    "acceptance/README.md", "acceptance/runner.json"}


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


R7_SPEC_PATHS = {
    ("features", "F01", "acceptance"), ("acceptance", "A12", "features"),
    ("contract_coverage", "error_contract", "branches", "html.bookmark_save.category.empty", "feature_ids"),
    ("contract_coverage", "error_contract", "branches", "html.bookmark_save.category.whitespace", "feature_ids"),
    ("contract_coverage", "error_contract", "branches", "html.bookmark_save.category.overlong_121", "feature_ids"),
    ("contract_coverage", "error_contract", "branches", "json.bookmark_save.category.empty", "feature_ids"),
    ("contract_coverage", "error_contract", "branches", "json.bookmark_save.category.whitespace", "feature_ids"),
    ("contract_coverage", "error_contract", "branches", "json.bookmark_save.category.overlong_121", "feature_ids"),
    ("contract_coverage", "error_contract", "schema"),
    ("contract_coverage", "features", "F01", "acceptance_ids"),
    ("contract_coverage", "features", "F01", "error_branch_ids"),
    ("contract_coverage", "features", "F02", "recovery"),
    ("contract_coverage", "features", "F02", "success_state"),
    ("contract_coverage", "features", "F04", "error_branch_ids"),
    ("contract_coverage", "features", "F11", "success_state"),
    ("architecture_markdown",),
}
R7_FILE_PLAN_PATHS = {"acceptance/p0_library.py", "acceptance/p0_organize.py",
                      "acceptance/p0_find_open.py", "acceptance/p0_recovery.py",
                      "acceptance/README.md", "acceptance/runner.json"}
R7_CASE_FIELDS = {("capability",), ("reason",)}
R7_EXPECTED_JOB_ERROR = "aggregate repair semantic review did not pass; candidate was not frozen"
R7_AGGREGATE_CHECKPOINT = "aggregate-semantic-review-f153e3550ceaeeb5"


def _at_path(root, path):
    """Resolve only identity-addressed list rows and ordinary object keys."""
    current = root
    index = 0
    while index < len(path):
        part = path[index]
        if isinstance(current, list):
            identity = part
            matches = [row for row in current if isinstance(row, dict)
                       and (row.get("id") == identity or row.get("feature_id") == identity)]
            if len(matches) != 1:
                _fail(f"R7 patch identity is missing or ambiguous: {identity}")
            current = matches[0]
            index += 1
            continue
        if isinstance(current, dict) and part not in current and index == len(path) - 1:
            return None
        if not isinstance(current, dict) or part not in current:
            _fail(f"R7 patch field is missing: {part}")
        current = current[part]
        index += 1
    return current


def _set_path(root, path, value):
    parent = root
    index = 0
    while index < len(path) - 1:
        part = path[index]
        if isinstance(parent, list):
            identity = part
            matches = [row for row in parent if isinstance(row, dict)
                       and (row.get("id") == identity or row.get("feature_id") == identity)]
            if len(matches) != 1:
                _fail(f"R7 patch identity is missing or ambiguous: {identity}")
            parent = matches[0]
            index += 1
            continue
        parent = parent[part]
        index += 1
    last = path[-1]
    if isinstance(parent, list):
        _fail("R7 patch path cannot end at a list")
    parent[last] = deepcopy(value)


def _apply_r7_patch(plan, choices, patch):
    if (not isinstance(patch, dict)
            or set(patch) != {"spec_changes", "file_plan_changes", "case_design_changes", "program_changes"}):
        _fail("R7 requires exact spec, file-plan, case-design and program deltas")
    spec_changes = patch["spec_changes"]
    if (not isinstance(spec_changes, list) or len(spec_changes) != len(R7_SPEC_PATHS)
            or any(not isinstance(row, dict) or not isinstance(row.get("path"), list)
                   or not all(isinstance(part, str) for part in row["path"]) for row in spec_changes)
            or {tuple(row["path"]) for row in spec_changes} != R7_SPEC_PATHS):
        _fail("R7 specification patch must contain the exact approved field allowlist")
    effective = deepcopy(plan)
    seen = set()
    for change in spec_changes:
        if (not isinstance(change, dict) or set(change) != {"path", "old", "new"}
                or not isinstance(change["path"], list)
                or not all(isinstance(part, str) for part in change["path"])):
            _fail("R7 spec changes require exact old/new values")
        path = change["path"]
        key = tuple(path)
        if key in seen or key not in R7_SPEC_PATHS:
            _fail("R7 spec path is duplicated or unauthorized")
        seen.add(key)
        target_path = ["spec", *path]
        if _at_path(effective, target_path) != change["old"]:
            _fail(f"R7 spec baseline changed at {path}")
        _set_path(effective, target_path, change["new"])

    rows = patch["file_plan_changes"]
    if (not isinstance(rows, list) or len(rows) != len(R7_FILE_PLAN_PATHS)
            or any(not isinstance(row, dict) or not isinstance(row.get("path"), str) for row in rows)
            or {row["path"] for row in rows} != R7_FILE_PLAN_PATHS):
        _fail("R7 file-plan patch must bind exactly the four changed and two reuse rows")
    by_path = {row.get("path"): row for row in effective.get("file_plan", []) if isinstance(row, dict)}
    if len(by_path) != len(effective.get("file_plan", [])):
        _fail("R7 base file-plan has duplicate paths")
    for change in rows:
        if not isinstance(change, dict) or set(change) != {"path", "old", "new"}:
            _fail("R7 file-plan changes require whole old/new rows")
        path = change["path"]
        old, new = change["old"], change["new"]
        if (not isinstance(old, dict) or not isinstance(new, dict)
                or path not in R7_FILE_PLAN_PATHS or by_path.get(path) != old or new.get("path") != path
                or set(old) != set(new) or any(old.get(k) != new.get(k) for k in set(old) - {"purpose", "reuse"})
                or not isinstance(new.get("purpose"), str) or not new["purpose"].strip()
                or type(new.get("reuse")) is not bool):
            _fail(f"R7 file-plan change exceeds purpose/reuse fields: {path}")
        by_path[path].update({"purpose": new["purpose"], "reuse": new["reuse"]})
    expected_modes = {path: path not in R7_REPLACE_PATHS for path in R7_FILE_PLAN_PATHS}
    # Every pinned source file remains present; only the exact four replacements change mode.
    for row in effective["file_plan"]:
        path = row["path"]
        if path in R7_PROGRAM_PATHS and row.get("reuse") != expected_modes.get(path, True):
            _fail(f"R7 file-plan reuse mode does not match the authorized program set: {path}")

    updates = patch["case_design_changes"]
    if not isinstance(updates, list) or len(updates) != 4:
        _fail("R7 case-design patch must contain exactly two capability/reason pairs")
    design = deepcopy(choices)
    original_by_capability = {row.get("capability"): row for row in design if isinstance(row, dict)}
    seen_case = set()
    for change in updates:
        if (not isinstance(change, dict) or set(change) != {"choice_id", "path", "old", "new"}
                or not isinstance(change["choice_id"], str)
                or change["path"] not in (["capability"], ["reason"])):
            _fail("R7 case-design changes may edit only capability or reason by old capability identity")
        identity = change["choice_id"]
        token = (identity, tuple(change["path"]))
        if token in seen_case:
            _fail("R7 case-design patch repeats a field")
        seen_case.add(token)
        target = original_by_capability.get(identity)
        if target is None or target.get(change["path"][0]) != change["old"] or not isinstance(change["new"], str) or not change["new"].strip():
            _fail("R7 case-design baseline or replacement is invalid")
        target[change["path"][0]] = change["new"]
    if len({identity for identity, _ in seen_case}) != 2 or {field[0] for _, field in seen_case} != {"capability", "reason"}:
        _fail("R7 must revise exactly two target capability/reason pairs")
    return effective, design


def _r7_repo_root(store):
    return store.pack.resolve().parent


def build_program_revision_manifest(store, patch=None, repo_root=None):
    """Derive the nine-file R7 revision from the pinned failed delivery and host patches."""
    repo_root = Path(repo_root) if repo_root is not None else _r7_repo_root(store)
    if patch is None:
        patch = _read_bound_json(repo_root, R7_PATCH_REF)
    changes = patch.get("program_changes") if isinstance(patch, dict) else None
    if (not isinstance(changes, list) or len(changes) != len(R7_REPLACE_PATHS)
            or any(not isinstance(row, dict) or not isinstance(row.get("path"), str) for row in changes)
            or {row["path"] for row in changes} != R7_REPLACE_PATHS):
        _fail("R7 program patch must replace exactly the four authorized files")
    changes_by_path = {row["path"]: row for row in changes}
    plan_record = _checkpoint_result(store, R7_SOURCE_JOB, "blueprint-plan-0", R7_SOURCE_PROPOSAL_DIGEST)
    if plan_record["digest"] != R7_SOURCE_PROPOSAL_DIGEST:
        _fail("R7 source plan checkpoint changed")
    aggregate = _checkpoint_result(store, R7_SOURCE_JOB, R7_AGGREGATE_CHECKPOINT, R7_AGGREGATE_DIGEST)
    prepared_root = R7_PROGRAMS_REF
    plan_rows = {row.get("path"): row for row in plan_record["result"].get("file_plan", []) if isinstance(row, dict)}
    if len(plan_rows) != 9 or set(plan_rows) != set(R7_PROGRAM_PATHS):
        _fail("R7 source file plan does not contain the exact nine programs")
    candidate_rel = f"jobs/{R7_SOURCE_JOB}/attempt-1/candidate-0/template.json"
    candidate_path = _resolve_bound_file(store.root, candidate_rel)
    if _sha256(candidate_path.read_bytes()) != R7_SOURCE_CANDIDATE_SHA256:
        _fail("R7 source candidate bytes changed")
    entries = []
    for index, path in enumerate(R7_PROGRAM_PATHS):
        cp_name = f"blueprint-code-0-{index}"
        cp = _checkpoint_result(store, R7_SOURCE_JOB, cp_name)
        result = cp["result"]
        if result.get("path") != path or not isinstance(result.get("content"), str):
            _fail(f"R7 program checkpoint path/content mismatch: {cp_name}")
        before = result["content"].encode("utf-8")
        if result.get("reused_sha256") is not None and result["reused_sha256"] != _sha256(before):
            _fail(f"R7 source reused digest mismatch: {path}")
        source_ref = f"jobs/{R7_SOURCE_JOB}/attempt-1/context/generated-0/{path}"
        actual_source = _resolve_bound_file(store.root, source_ref).read_bytes()
        if actual_source != before:
            _fail(f"R7 source checkpoint differs from actual delivery: {path}")
        mode = "replace" if path in R7_REPLACE_PATHS else "reuse"
        spans = []
        after = before
        if mode == "replace":
            change = changes_by_path[path]
            if not isinstance(change, dict) or set(change) != {"path", "mode", "patch"} or change["mode"] != "replace" or not isinstance(change["patch"], list) or not change["patch"]:
                _fail(f"R7 replacement patch is malformed: {path}")
            try:
                text_value = before.decode("utf-8")
            except UnicodeDecodeError:
                _fail(f"R7 source program is not UTF-8: {path}")
            for span in change["patch"]:
                if not isinstance(span, dict) or set(span) != {"old", "new"} or not isinstance(span["old"], str) or not span["old"] or not isinstance(span["new"], str):
                    _fail(f"R7 exact replacement span is malformed: {path}")
                if text_value.count(span["old"]) != 1:
                    _fail(f"R7 replacement span must match exactly once: {path}")
                text_value = text_value.replace(span["old"], span["new"], 1)
                spans.append(deepcopy(span))
            after = text_value.encode("utf-8")
        elif path in changes_by_path:
            _fail(f"R7 reuse program has a supplied patch: {path}")
        prepared_ref = f"{prepared_root}/{Path(path).name}"
        prepared_path = _resolve_bound_file(repo_root, prepared_ref)
        prepared = prepared_path.read_bytes()
        if prepared != after:
            _fail(f"R7 prepared program bytes differ from applying the exact patch: {path}")
        clauses = {
            "acceptance/p0_library.py": "R7 §3.1 A02 and §3.3 A11 only",
            "acceptance/p0_find_open.py": "R7 §3.2 A07 only",
            "acceptance/README.md": "R7 §5.4 README factual correction only",
            "acceptance/runner.json": "R7 §3.4 A11 argument binding only",
        }
        authorization_clause = clauses.get(path, "R7 §3.0 exact byte-for-byte reuse")
        entries.append({"path": path, "source_job_id": R7_SOURCE_JOB, "source_attempt": 1,
                        "checkpoint_name": cp_name, "checkpoint_digest": cp["digest"],
                        "before_sha256": _sha256(before), "mode": mode,
                        "after_sha256": _sha256(after), "patch": spans,
                        "patch_digest": digest(spans), "prepared_ref": prepared_ref,
                        "authorization_clause": authorization_clause})
    return {"schema": R7_PROGRAM_REVISION_SCHEMA, "source_job_id": R7_SOURCE_JOB,
            "source_attempt": 1, "source_proposal_digest": R7_SOURCE_PROPOSAL_DIGEST,
            "source_candidate_sha256": R7_SOURCE_CANDIDATE_SHA256,
            "source_plan_checkpoint_name": "blueprint-plan-0",
            "source_plan_checkpoint_digest": plan_record["digest"],
            "source_aggregate_checkpoint_name": R7_AGGREGATE_CHECKPOINT,
            "source_aggregate_checkpoint_digest": aggregate["digest"], "entries": entries}


def program_revision_contents(store, manifest):
    """Revalidate original checkpoints, patch spans and prepared bytes, then return strings."""
    if not isinstance(manifest, dict) or manifest.get("schema") != R7_PROGRAM_REVISION_SCHEMA:
        _fail("unsupported prepared program revision manifest")
    root = _r7_repo_root(store)
    patch = _read_bound_json(root, R7_PATCH_REF)
    expected = build_program_revision_manifest(store, patch, root)
    if manifest != expected:
        _fail("prepared program revision no longer matches pinned source and approved bytes")
    contents = {}
    for entry in expected["entries"]:
        raw = _resolve_bound_file(root, entry["prepared_ref"]).read_bytes()
        if _sha256(raw) != entry["after_sha256"]:
            _fail(f"R7 prepared program hash changed: {entry['path']}")
        try:
            contents[entry["path"]] = raw.decode("utf-8")
        except UnicodeDecodeError:
            _fail(f"R7 prepared program is not UTF-8: {entry['path']}")
    return contents


def _validate_approved_r7(root, source_authorization, patch, manifest, binding=None):
    expected_auth = {"source_ref": R7_AUTHORIZATION_REF,
                     "source_digest": R7_AUTHORIZATION_SHA256,
                     "revision_ref": R7_APPROVED_REVISION_REF}
    if (not isinstance(source_authorization, dict)
            or set(source_authorization) != set(expected_auth) | {"revision_digest"}
            or any(source_authorization.get(k) != v for k, v in expected_auth.items())):
        _fail("R7 request does not bind the fixed authorization record")
    if _sha256(_resolve_bound_file(root, R7_AUTHORIZATION_REF).read_bytes()) != R7_AUTHORIZATION_SHA256:
        _fail("R7 authorization source bytes changed")
    record = _read_bound_json(root, R7_APPROVED_REVISION_REF)
    if digest(record) != source_authorization["revision_digest"]:
        _fail("R7 approved-revision record digest changed")
    if (record.get("schema") != "atlas.g1-bounded-revision-authorization.v1"
            or record.get("source_ref") != R7_AUTHORIZATION_REF
            or record.get("source_digest") != R7_AUTHORIZATION_SHA256
            or record.get("base_proposal_digest") != R7_SOURCE_PROPOSAL_DIGEST
            or record.get("candidate_sha256") != R7_SOURCE_CANDIDATE_SHA256
            or record.get("aggregate_checkpoint_digest") != R7_AGGREGATE_DIGEST
            or record.get("patch_ref") != R7_PATCH_REF
            or record.get("patch_digest") != digest(patch)
            or record.get("program_revision_digest") != digest(manifest)
            or record.get("program_ref") != R7_PROGRAMS_REF
            or record.get("binding_digest") != digest(binding)):
        _fail("R7 approved-revision record does not bind this exact patch and program revision")
    if _read_bound_json(root, R7_PATCH_REF) != patch:
        _fail("R7 request patch differs from the fixed host patch file")
    return record


class PreparedRevisionService:
    def __init__(self, store):
        self.store = store

    def prepare(self, job_id, request):
        if isinstance(request, dict) and request.get("schema") == R7_PREPARATION_SCHEMA:
            return self._prepare_r7(job_id, request)
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

    def _prepare_r7(self, job_id, request):
        required_top = {"schema", "binding", "patch", "source_authorization", "prepared_program_revision"}
        if set(request) != required_top or job_id != R7_SOURCE_JOB:
            _fail("R7 preparation requires the exact fixed failed job and request shape")
        root = _r7_repo_root(self.store)
        patch = request["patch"]
        manifest = request["prepared_program_revision"]
        _validate_approved_r7(root, request["source_authorization"], patch, manifest, request.get("binding"))
        job = self.store.job(job_id)
        snapshot = job["snapshot"]
        if (job["kind"] != "blueprint-production" or job["state"] != "failed"
                or job["attempt"] != R7_SOURCE_ATTEMPT or job["stage"] != "aggregate-semantic-review"
                or job.get("error") != R7_EXPECTED_JOB_ERROR or not bookmark_bound(snapshot)):
            _fail("R7 requires the pinned failed aggregate-review attempt")
        binding = request["binding"]
        keys = {"job_id", "attempt", "snapshot_digest", "stage", "job_error_digest",
                "plan_checkpoint_name", "plan_checkpoint_digest", "proposal_digest",
                "candidate_path", "candidate_sha256", "aggregate_checkpoint_name",
                "aggregate_checkpoint_digest", "campaign_id", "plan_id", "plan_digest",
                "product_id", "scenario_id", "scenario_revision", "case_basis_digest",
                "facts_view_checkpoint_name", "facts_view_checkpoint_digest", "facts_view_digest",
                "case_design_checkpoint_name", "case_design_checkpoint_digest", "cli_total",
                "business_repairs_used", "active_jobs", "old_grant_id", "old_grant_used",
                "previous_amendment_id", "absolute_deadline"}
        if not isinstance(binding, dict) or set(binding) != keys:
            _fail("R7 request must bind the complete failed job, accepted inputs and preserved ledger")
        v1, scenario = snapshot["v1"], snapshot["scenario"]
        expected = {"job_id": R7_SOURCE_JOB, "attempt": 1,
                    "snapshot_digest": digest(snapshot), "stage": "aggregate-semantic-review",
                    "job_error_digest": digest(job["error"]),
                    "plan_checkpoint_name": "blueprint-plan-0",
                    "plan_checkpoint_digest": R7_SOURCE_PROPOSAL_DIGEST,
                    "proposal_digest": R7_SOURCE_PROPOSAL_DIGEST,
                    "candidate_path": f"jobs/{R7_SOURCE_JOB}/attempt-1/candidate-0/template.json",
                    "candidate_sha256": R7_SOURCE_CANDIDATE_SHA256,
                    "aggregate_checkpoint_name": R7_AGGREGATE_CHECKPOINT,
                    "aggregate_checkpoint_digest": R7_AGGREGATE_DIGEST,
                    "campaign_id": v1["campaign_id"], "plan_id": v1["plan_id"],
                    "plan_digest": v1["plan_digest"],
                    "product_id": v1["product_id"], "scenario_id": scenario["id"],
                    "scenario_revision": scenario["revision"],
                    "case_basis_digest": R7_CASE_BASIS_DIGEST,
                    "facts_view_checkpoint_name": "blueprint-accepted-facts-view",
                    "facts_view_digest": R7_FACTS_VIEW_DIGEST,
                    "case_design_checkpoint_name": "case-adaptation-prepared-aaf080ba52611126",
                    "cli_total": 71, "business_repairs_used": 6, "active_jobs": 0,
                    "old_grant_id": "pgrant_f3595368c14d4b23b6ab536f6d198007",
                    "old_grant_used": 1,
                    "previous_amendment_id": "bamd_100a302fe8424d9493dafe62d6e43db9",
                    "absolute_deadline": 1792495312.855422}
        if any(binding.get(key) != value for key, value in expected.items()):
            _fail("R7 request identity differs from the pinned failed product or authorization baseline")
        with self.store.connect() as con:
            row = con.execute("SELECT body FROM v1_plan WHERE id=?", (v1["plan_id"],)).fetchone()
        if not row:
            _fail("fixed R7 batch plan is missing")
        fixed_plan = json.loads(row[0])
        if (fixed_plan.get("digest") != binding["plan_digest"]
                or digest({k: v for k, v in fixed_plan.items() if k != "digest"}) != fixed_plan.get("digest")
                or fixed_plan.get("campaign_id") != v1["campaign_id"]):
            _fail("R7 fixed plan digest or campaign changed")
        if fixed_plan.get("campaign_id") != "atlas-v1-first-production-2026-10-19":
            _fail("R7 campaign identity changed")
        seeds = [seed for seed in fixed_plan.get("seeds", []) if seed.get("product_id") == v1["product_id"]]
        if (len(seeds) != 1 or seeds[0].get("scenario") != scenario
                or (seeds[0].get("case_basis") is not None
                    and seeds[0].get("case_basis") != snapshot.get("case_basis"))):
            _fail("R7 failed product no longer agrees with its fixed plan seed")
        plan_cp = _checkpoint_result(self.store, job_id, binding["plan_checkpoint_name"], binding["plan_checkpoint_digest"])
        aggregate_cp = _checkpoint_result(self.store, job_id, binding["aggregate_checkpoint_name"], binding["aggregate_checkpoint_digest"])
        if aggregate_cp["digest"] != R7_AGGREGATE_DIGEST:
            _fail("R7 aggregate review checkpoint changed")
        candidate = _resolve_bound_file(self.store.root, binding["candidate_path"])
        if _sha256(candidate.read_bytes()) != binding["candidate_sha256"]:
            _fail("R7 failed candidate bytes changed")

        facts_cp = _checkpoint_result(self.store, job_id, binding["facts_view_checkpoint_name"], binding["facts_view_checkpoint_digest"])
        facts_view = facts_cp["result"]
        if facts_view.get("view_digest") != binding["facts_view_digest"] or facts_view.get("basis_digest") != R7_CASE_BASIS_DIGEST:
            _fail("R7 accepted facts view is stale or has changed")
        from .cases import CaseLibrary
        cases = CaseLibrary(self.store, initialize=False)
        cases.require_admissible(snapshot["case_basis"])
        cases.validate_facts_view(facts_view, snapshot["case_basis"])
        design_cp = _checkpoint_result(self.store, job_id, binding["case_design_checkpoint_name"], binding["case_design_checkpoint_digest"])
        _validate_pinned_case_design(snapshot, binding["case_design_checkpoint_name"], design_cp)
        cases.require_design_evidence(snapshot["case_basis"], design_cp["result"]["choices"])
        research_cp = _checkpoint_result(self.store, job_id, "blueprint-research")
        _validate_research_view_binding(facts_view, research_cp)

        effective, choices = _apply_r7_patch(plan_cp["result"], design_cp["result"]["choices"], patch)
        eligible = set(facts_view.get("accepted_evidence_ids", []))
        research_sources = research_cp["result"].get("sources")
        if not isinstance(research_sources, list):
            _fail("R7 current research sources are malformed")
        current_sources = [source for source in research_sources if isinstance(source, dict) and source.get("name") in eligible]
        current_sources.append({"id": "S01"})
        from .source_references import validate_feature_source_references
        source_report = validate_feature_source_references(effective["spec"], current_sources,
                                                           binding={"job_id": job_id, "attempt": 1,
                                                                    "facts_view_digest": binding["facts_view_digest"],
                                                                    "case_basis_digest": binding["case_basis_digest"]})
        if not source_report.get("valid"):
            _fail("R7 current source-reference policy validation did not pass")
        cases.require_design_evidence(snapshot["case_basis"], choices)
        from .cognition import validate_file_plan
        from .contract_scope import validate_contract_coverage
        validate_file_plan(effective, allow_reuse=True, require_runtime=True)
        validate_contract_coverage(effective["spec"], required=True)
        actual_manifest = build_program_revision_manifest(self.store, patch, root)
        if manifest != actual_manifest:
            _fail("R7 program revision manifest differs from source checkpoints and prepared bytes")
        program_revision_contents(self.store, actual_manifest)

        changed_spec = []
        for change in patch["spec_changes"]:
            changed_spec.append(deepcopy(change))
        actual_case_changes = deepcopy(patch["case_design_changes"])
        old_repair = snapshot.get("cognitive_repair", {})
        old_scope = old_repair.get("repair_scope")
        if not isinstance(old_scope, dict):
            _fail("R7 cumulative repair scope is missing from the failed snapshot")
        cumulative_scope = deepcopy(old_scope)
        cumulative_scope["version"] = "atlas.aggregate-repair-scope.v2"
        field_paths = [list(path) for path in cumulative_scope.get("authored_field_paths", [])]
        for change in changed_spec:
            path = change["path"]
            # Contract-coverage nested rows are authored through their existing top-level field.
            if path[0] == "contract_coverage":
                path = ["contract_coverage", path[1]]
            if path not in field_paths:
                field_paths.append(path)
        cumulative_scope["authored_field_paths"] = field_paths
        edit_paths = list(cumulative_scope.get("edit_paths", []))
        for path in sorted(R7_REPLACE_PATHS):
            if path not in edit_paths:
                edit_paths.append(path)
        cumulative_scope["edit_paths"] = edit_paths
        cumulative_scope["edit_paths"].sort()
        cumulative_scope["authored_field_paths"] = sorted(field_paths)
        incremental_diff = {"base_proposal_digest": plan_cp["digest"],
                            "effective_plan_digest": digest(effective),
                            "spec_changes": changed_spec,
                            "case_design_changes": actual_case_changes,
                            "program_changes": [{"path": row["path"], "before_sha256": row["before_sha256"],
                                                 "after_sha256": row["after_sha256"], "patch_digest": row["patch_digest"]}
                                                for row in actual_manifest["entries"] if row["mode"] == "replace"],
                            "reuse_paths": [row["path"] for row in actual_manifest["entries"] if row["mode"] == "reuse"],
                            "program_revision_digest": digest(actual_manifest)}
        return {"schema": R7_PREPARATION_SCHEMA, "state": "prepared_not_queued",
                "binding": deepcopy(binding), "request_digest": digest(request),
                "base_proposal_digest": plan_cp["digest"], "effective_plan": effective,
                "effective_plan_digest": digest(effective), "case_design": choices,
                "case_design_digest": digest(choices), "source_reference_report": source_report,
                "case_adaptation_input": {"mode": "host-exact-r7-target-adaptation",
                                          "prior_checkpoint_digest": design_cp["digest"],
                                          "case_basis_digest": binding["case_basis_digest"]},
                "prepared_program_revision": deepcopy(actual_manifest),
                "incremental_diff": incremental_diff,
                "cumulative_repair_scope": cumulative_scope,
                "evidence_scope": "Read-only host preparation. R7 proposal, current case evidence, source view, four exact program replacements and five reused source bytes are bound; no production state, queue, budget, worker, call or window was changed."}
