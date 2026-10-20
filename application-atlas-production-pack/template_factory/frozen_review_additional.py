"""Narrow timing restoration record for one explicitly authorized frozen review."""
from __future__ import annotations

from .store import FactoryError

REQUEST_KEY = "atlas-g1-r7-frozen-review-additional-2026-10-20-attempt3"
AUTH_REF = "docs/template-factory/g1-frozen-review-recovery-2026-10-20/additional-call-authorization/USER_AUTHORIZATION.txt"
AUTH_SHA256 = "4384d1c263c8c553c73b85b2fe6e11533325b64f95c9343fe63a49f4fd97767e"
TIMING_AUTH_REF = "docs/template-factory/g1-frozen-review-recovery-2026-10-20/additional-call-authorization/TIMING_OVERRIDE_AUTHORIZATION.txt"
TIMING_AUTH_SHA256 = "373c24f9861e8a789ce71053c6f7a6412921f99a244953c857f9a0c87852a7c9"
PREDECESSOR_AUTH_REF = "docs/template-factory/g1-frozen-review-recovery-2026-10-20/authorization/ATLAS_G1_FROZEN_REVIEW_RECOVERY_CODEX_INSTRUCTIONS.txt"
PREDECESSOR_AUTH_SHA256 = "65976f3c72613dfc7208d86cea7ce4c9ec0688ef04c881efba8abacf7f642101"
REMAINING_SECONDS = 4632.611294
DIAGNOSTIC_PATH = "docs/template-factory/provider-connectivity-2026-10-20/diagnostic.json"
DIAGNOSTIC_SHA256 = "0b1383c72e5f1d5db80c6cbd42baea2da5733367c0d22f345d327ff0d7c8ded7"
PREDECESSOR_GRANT = "egrant_c06325f363b84bd9bb1c8fa46f93f945"
PREDECESSOR_RESERVATION = "bud_c06f643f77bb4ce9a7bad57f30f161e1"
PREDECESSOR_ACCEPTANCE = "acc_c0cbb5e84d6f475dade4875d8af60174"
PREDECESSOR_ACCEPTED_AT = "2026-10-20T10:04:40.244128+00:00"


def ensure_table(con):
    con.execute("""CREATE TABLE IF NOT EXISTS tf_frozen_review_time_resume (
        grant_id TEXT PRIMARY KEY, job_id TEXT NOT NULL UNIQUE, campaign_id TEXT NOT NULL,
        plan_id TEXT NOT NULL, product_id TEXT NOT NULL, previous_deadline REAL NOT NULL,
        paused_at REAL NOT NULL, remaining_seconds REAL NOT NULL, activated_at REAL NOT NULL,
        effective_deadline REAL NOT NULL, authorization_digest TEXT NOT NULL,
        external_cli_sessions INTEGER NOT NULL DEFAULT 1)""")


def get_time_resume_locked(con, *, campaign_id, product_id, plan_id, grant_id=None):
    """Return the one formal activated timing resume, checking its fixed scope."""
    try:
        if grant_id:
            row = con.execute("SELECT * FROM tf_frozen_review_time_resume WHERE grant_id=?", (grant_id,)).fetchone()
        else:
            row = con.execute("SELECT * FROM tf_frozen_review_time_resume WHERE job_id='job_b01427592b164863aab5bedf7b3863bb'").fetchone()
    except Exception as exc:
        if "no such table" in str(exc):
            return None
        raise
    if not row:
        return None
    if (row["campaign_id"] != campaign_id or row["product_id"] != product_id
            or row["plan_id"] != plan_id or row["job_id"] != "job_b01427592b164863aab5bedf7b3863bb"):
        return None
    if (float(row["remaining_seconds"]) != REMAINING_SECONDS
            or float(row["effective_deadline"]) != float(row["activated_at"]) + REMAINING_SECONDS
            or float(row["previous_deadline"]) != 1792495312.855422
            or float(row["paused_at"]) != 1792490680.244128
            or row["external_cli_sessions"] != 1):
        raise FactoryError("activated frozen-review timing row is malformed", "evidence_grant_binding", 409)
    grant = con.execute("SELECT * FROM tf_evidence_recovery_grant WHERE id=?", (row["grant_id"],)).fetchone()
    if not grant or grant["request_key"] != REQUEST_KEY or grant["job_id"] != row["job_id"]:
        return None
    import json
    proposal = json.loads(grant["request_json"])
    if (proposal.get("schema") != "atlas.frozen-review-recovery-proposal.v1"
            or proposal.get("request_key") != REQUEST_KEY
            or proposal.get("source_authorization") != {"source_ref": AUTH_REF, "source_digest": AUTH_SHA256}
            or proposal.get("timing_override_authorization") != {"source_ref": TIMING_AUTH_REF, "source_digest": TIMING_AUTH_SHA256}
            or proposal.get("predecessor_source_authorization") != {"source_ref": PREDECESSOR_AUTH_REF, "source_digest": PREDECESSOR_AUTH_SHA256}
            or row["authorization_digest"] != AUTH_SHA256
            or proposal.get("timing_policy") != {"remaining_seconds": REMAINING_SECONDS,
                "external_cli_sessions": 1, "previous_deadline": 1792495312.855422,
                "paused_at": 1792490680.244128}
            or proposal.get("materials", {}).get("binding", {}).get("predecessor_grant_id") != PREDECESSOR_GRANT
            or proposal.get("materials", {}).get("binding", {}).get("predecessor_reservation_id") != PREDECESSOR_RESERVATION
            or proposal.get("materials", {}).get("binding", {}).get("predecessor_acceptance_id") != PREDECESSOR_ACCEPTANCE
            or grant["proposal_digest"] != proposal.get("proposal_digest")):
        raise FactoryError("activated frozen-review timing binding differs from its grant", "evidence_grant_binding", 409)
    return dict(row)
