"""Versioned host checks for current-required UI contracts and aggregate repairs."""

from __future__ import annotations

from .store import FactoryError, digest

REVIEW_RULES_VERSION = "atlas.current-required-contract.v1"
REPAIR_SCOPE_VERSION = "atlas.aggregate-repair-scope.v1"
COVERAGE_SCHEMA = "atlas.contract-coverage.v1"


def _fail(message):
    raise FactoryError(message, "contract_scope_invalid", 409)


def validate_contract_coverage(spec, *, required=False):
    """Validate mapping identity/references; semantic reachability remains reviewer-owned."""
    coverage = spec.get("contract_coverage")
    if coverage is None and not required:
        return None
    if not isinstance(coverage, dict) or coverage.get("schema") != COVERAGE_SCHEMA or coverage.get("review_rules_version") != REVIEW_RULES_VERSION:
        _fail("contract coverage schema or review rules version differs")
    feature_rows, case_rows = spec.get("features"), spec.get("acceptance")
    if not isinstance(feature_rows, list) or not isinstance(case_rows, list):
        _fail("contract coverage requires feature and acceptance inventories")
    features = {x["id"]: x for x in feature_rows if isinstance(x, dict) and isinstance(x.get("id"), str)}
    cases = {x["id"]: x for x in case_rows if isinstance(x, dict) and isinstance(x.get("id"), str)}
    if len(features) != len(feature_rows) or len(cases) != len(case_rows):
        _fail("contract coverage inventories contain malformed or duplicate IDs")
    rows = coverage.get("features")
    if not isinstance(rows, list):
        _fail("contract coverage requires feature rows")
    mapped = {}
    fields = ("design_basis", "entry", "action", "success_state", "navigation", "failure", "recovery", "acceptance_ids")
    for row in rows:
        if (not isinstance(row, dict) or not isinstance(row.get("feature_id"), str)
                or row["feature_id"] not in features or row["feature_id"] in mapped):
            _fail("contract coverage has unknown or duplicate feature ID")
        if any(not isinstance(row.get(key), str) or not row[key].strip() for key in fields[:-1]):
            _fail("contract coverage row is missing a required journey field")
        refs = row.get("acceptance_ids")
        if (not isinstance(refs, list) or not refs or any(not isinstance(ref, str) for ref in refs)
                or len(set(refs)) != len(refs) or not set(refs) <= set(cases)):
            _fail("contract coverage acceptance references are invalid")
        feature = features[row["feature_id"]]
        feature_cases = feature.get("acceptance")
        if not isinstance(feature_cases, list) or any(not isinstance(item, str) for item in feature_cases):
            _fail("contract coverage feature acceptance references are invalid")
        if not set(refs) <= set(feature_cases):
            _fail("contract coverage references acceptance outside its feature")
        mapped[row["feature_id"]] = row
    required_ids = {fid for fid, feature in features.items() if feature.get("phase") == "P0" and feature.get("applicability") == "current required"}
    if required_ids - set(mapped):
        _fail("current-required P0 features lack contract coverage")
    if set(mapped) - set(features):
        _fail("contract coverage references unknown features")
    return coverage


def validate_repair_scope(scope, spec, edit_paths):
    if not isinstance(scope, dict) or scope.get("version") != REPAIR_SCOPE_VERSION:
        _fail("versioned aggregate repair scope is required")
    paths = scope.get("edit_paths")
    fields = scope.get("authored_field_paths")
    if (not isinstance(paths, list) or not paths or any(not isinstance(path, str) for path in paths)
            or paths != edit_paths or len(set(paths)) != len(paths)):
        _fail("repair scope program paths must match edit_paths")
    if not isinstance(fields, list) or not fields or any(not isinstance(path, list) or not path or not all(isinstance(x, str) and x for x in path) for path in fields):
        _fail("repair scope needs explicit authored field paths")
    if len({tuple(x) for x in fields}) != len(fields):
        _fail("repair scope authored paths must be unique")
    if not isinstance(scope.get("known_blockers"), list) or not scope["known_blockers"]:
        _fail("repair scope must bind known blockers")
    features = {row["id"] for row in spec.get("features", [])}
    acceptance = {row["id"] for row in spec.get("acceptance", [])}
    decisions = {row["id"] for row in spec.get("decisions", [])}
    for blocker in scope["known_blockers"]:
        if (not isinstance(blocker, dict)
                or not isinstance(blocker.get("feature_id"), str)
                or not isinstance(blocker.get("acceptance_id"), str)
                or (blocker.get("decision_id") is not None and not isinstance(blocker.get("decision_id"), str))
                or blocker.get("feature_id") not in features
                or blocker.get("acceptance_id") not in acceptance
                or blocker.get("decision_id") not in decisions | {None}
                or not isinstance(blocker.get("basis"), str) or not blocker["basis"].strip()):
            _fail("repair blocker must reference an existing feature, acceptance, and optional decision")
    authorized = scope.get("authorized_assertion_changes")
    if not isinstance(authorized, list) or len(authorized) != 1:
        _fail("repair scope must explicitly bind its sole assertion semantic replacement")
    change = authorized[0]
    if (not isinstance(change, dict) or change.get("acceptance_id") != "A02"
            or change.get("change") != "single_label_hostname_negative_to_positive"
            or not isinstance(change.get("rationale"), str) or not change["rationale"].strip()):
        _fail("only the explicitly authorized A02 hostname boundary assertion may change semantically")
    allowed_programs = {
        "acceptance/p0_library.py", "acceptance/p0_organize.py",
        "acceptance/p0_find_open.py", "acceptance/p0_recovery.py",
        "acceptance/README.md",
    }
    if set(paths) - allowed_programs:
        _fail("repair scope includes an unauthorized program path")
    for path in fields:
        if path == ["architecture_markdown"]:
            exists = isinstance(spec.get("architecture_markdown"), str)
        elif len(path) == 3 and path[0] in {"features", "decisions", "acceptance"}:
            rows = spec.get(path[0], [])
            found = [row for row in rows if row.get("id") == path[1]]
            exists = len(found) == 1 and path[2] in found[0] and path[2] not in {"id", "phase", "status", "applicability"}
        elif len(path) == 2 and path[0] == "contract_coverage":
            exists = path[1] in {"schema", "review_rules_version", "features"}
        else:
            exists = False
        if not exists:
            _fail("repair scope names a missing or immutable authored field")
    return scope


def validate_repair_diff(before_spec, after_spec, before_files, after_files, scope):
    """Reject spec edits outside the pinned fields and unauthorized file edits/deletions."""
    allowed = {tuple(path) for path in scope["authored_field_paths"]}
    fields = ("title", "roles", "features", "decisions", "phases", "acceptance", "architecture_markdown", "limits", "contract_coverage")
    for field in fields:
        if before_spec.get(field) == after_spec.get(field):
            continue
        if field in {"features", "decisions", "acceptance"}:
            old = {row["id"]: row for row in before_spec.get(field, [])}
            new = {row["id"]: row for row in after_spec.get(field, [])}
            if old.keys() != new.keys():
                _fail("aggregate repair cannot add/remove authored identities")
            for identity, oldrow in old.items():
                for key in oldrow.keys() | new[identity].keys():
                    if oldrow.get(key) != new[identity].get(key) and (field, identity, key) not in allowed:
                        _fail("aggregate repair changed an unauthorized authored field")
        elif field == "contract_coverage":
            # Coverage content is allowed only when its exact top-level field is scoped.
            changed = {key for key in set(before_spec.get(field) or {}) | set(after_spec.get(field) or {}) if (before_spec.get(field) or {}).get(key) != (after_spec.get(field) or {}).get(key)}
            new_coverage = after_spec.get(field)
            if (before_spec.get(field) is None
                    and (not isinstance(new_coverage, dict) or new_coverage.get("schema") != COVERAGE_SCHEMA)):
                _fail("new contract coverage must use the fixed schema")
            if any((field, key) not in allowed for key in changed):
                _fail("aggregate repair changed unauthorized contract coverage")
        elif (field,) not in allowed:
            _fail("aggregate repair changed an unauthorized authored field")
    if before_spec.get("phases") != after_spec.get("phases"):
        _fail("aggregate repair cannot change phases")
    if before_spec.get("features") and after_spec.get("features"):
        before = {x["id"]: x for x in before_spec["features"]}
        after = {x["id"]: x for x in after_spec["features"]}
        for fid, row in before.items():
            if row.get("phase") != after[fid].get("phase") or row.get("applicability") != after[fid].get("applicability"):
                _fail("aggregate repair cannot change feature identity, phase, or current-required status")
    allowed_files = set(scope["edit_paths"])
    # Rendered prose, integrity.json, template.json, and host-owned inputs are
    # derived from the authored proposal. The immutable-program contract applies
    # to the pinned acceptance/reference file inventory only.
    def is_program(path):
        return path.startswith(("acceptance/", "references/")) and path != "acceptance/plan.json"
    before_programs = {path for path in before_files if is_program(path)}
    after_programs = {path for path in after_files if is_program(path)}
    if before_programs != after_programs:
        _fail("aggregate repair cannot add or delete program files")
    all_paths = before_programs | after_programs
    for path in all_paths:
        if before_files.get(path) != after_files.get(path) and path not in allowed_files:
            _fail("aggregate repair changed program outside authorized paths: " + path)
    return True


def aggregate_semantic_diff_digest(*, scope, baseline_digest, before_spec, after_spec,
                                   before_program_hashes, after_program_hashes,
                                   case_design_before, case_design_after,
                                   case_adaptation_revision, case_adaptation_input):
    """Digest only semantic authored inputs, excluding rendered IDs and timestamps."""
    return digest({
        "scope_digest": digest(scope),
        "baseline_digest": baseline_digest,
        "authored_fields_before": before_spec,
        "authored_fields_after": after_spec,
        "program_hashes_before": before_program_hashes,
        "program_hashes_after": after_program_hashes,
        "case_design_before": case_design_before,
        "case_design_after": case_design_after,
        "case_adaptation_revision": case_adaptation_revision,
        "case_adaptation_input": case_adaptation_input,
    })


def aggregate_semantic_budget_stage(diff_digest):
    """Stable for a semantic candidate, distinct for a new official revision."""
    if not isinstance(diff_digest, str) or len(diff_digest) != 64:
        _fail("aggregate semantic budget stage requires a SHA-256 digest")
    return "aggregate-semantic-review:" + diff_digest
