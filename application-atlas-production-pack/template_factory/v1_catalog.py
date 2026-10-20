"""Cognitive publication policy, independently bound to canonical case evidence."""
from __future__ import annotations

import json

from .store import FactoryError, canonical, now


def review_status(con, artifact_id, artifact_digest):
    """Latest request wins, including incomplete/failed requests; no historical-pass fallback."""
    job = con.execute("SELECT id,state,attempt FROM job WHERE kind='cognitive-review' AND "
                      "json_extract(snapshot,'$.artifact_id')=? AND json_extract(snapshot,'$.artifact_digest')=? "
                      "ORDER BY created_at DESC,rowid DESC LIMIT 1", (artifact_id, artifact_digest)).fetchone()
    if not job:
        return "unavailable"
    result = con.execute("SELECT body FROM acceptance WHERE job_id=? AND digest=? ORDER BY created_at DESC,rowid DESC LIMIT 1", (job["id"], artifact_digest)).fetchone()
    if not result or job["state"] in {"queued", "running", "failed", "cancelled", "interrupted", "paused_budget"}:
        return "unavailable"
    body = json.loads(result[0])
    # Legacy attempt-one records predate job_attempt. A recovered job cannot
    # inherit such a verdict while its own acceptance has not been committed.
    if body.get("job_attempt", 1) != job["attempt"]:
        return "unavailable"
    return body.get("outcome", "unavailable")


def catalog_eligibility(store, artifact):
    blockers = []
    if artifact["state"] != "published":
        blockers.append({"code": "not_published", "reason": "This version is not published."})
    if artifact.get("artifact_type") == "product-blueprint":
        if artifact.get("review_status") != "passed":
            blockers.append({"code": "cognitive_review_required", "reason": "The latest review request has not passed."})
        basis = artifact.get("provenance", {}).get("case_basis")
        if not basis:
            blockers.append({"code": "case_evidence_required", "reason": "Legacy package has no canonical case evidence."})
        else:
            from .cases import CaseLibrary
            try:
                library = CaseLibrary(store, initialize=False)
                library.require_admissible(basis)
                from .api import controlled_path
                from .blueprints import verify_frozen
                spec = verify_frozen(controlled_path(store, artifact["bundle_path"]), artifact["digest"])
                if spec.get("case_facts_view") is None:
                    library.legacy_facts_marker(basis)
                else:
                    library.validate_facts_view(spec["case_facts_view"], basis)
                library.require_design_evidence(basis, spec.get("case_design", []))
            except FactoryError as error:
                blockers.append({"code": error.code, "reason": str(error)})
    return {"catalog_eligible": not blockers, "catalog_blockers": blockers}


def publish(store, con, row, body, value, review):
    from .blueprints import verify_frozen
    from .cases import CaseLibrary
    from .api import controlled_path
    if value.get("expected_digest") != row["digest"]:
        raise FactoryError("artifact version changed", "revision_conflict", 409)
    if value["action"] == "publish":
        bundle = controlled_path(store, body["bundle_path"])
        spec = verify_frozen(bundle, row["digest"])
        basis = body.get("provenance", {}).get("case_basis")
        if not basis or spec.get("case_basis") != basis:
            raise FactoryError("legacy/unverified package lacks fixed canonical case evidence", "case_evidence_required", 409)
        library = CaseLibrary(store, initialize=False)
        library.require_admissible(basis)
        if spec.get("case_facts_view") is None:
            library.legacy_facts_marker(basis)
        else:
            library.validate_facts_view(spec["case_facts_view"], basis)
        library.require_design_evidence(basis, spec.get("case_design", []))
        if review_status(con, row["id"], row["digest"]) != "passed":
            raise FactoryError("latest independent review of this exact digest must pass", "cognitive_review_required", 409)
        if not spec.get("case_design"):
            raise FactoryError("missing case adaptation rationale", "case_adaptation_required", 409)
        from .blueprint_runtime import validate_runner_manifest
        validate_runner_manifest(bundle / "source", spec)
    body["review"] = {"note": review, "at": now(), "action": value["action"], "digest": row["digest"]}
    state = "published" if value["action"] == "publish" else "withdrawn"
    con.execute("UPDATE artifact SET state=?,body=? WHERE id=? AND digest=?", (state, canonical(body), row["id"], row["digest"]))
