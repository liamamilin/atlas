"""Thin operator CLI for the same versioned batch service used by HTTP."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .store import FactoryError, FactoryStore
from .v1_batches import BatchService
from .worker import ensure_worker


def main(argv=None):
    parser = argparse.ArgumentParser(description="Atlas V1 fixed batch plans (no model calls on preview)")
    parser.add_argument("--root", type=Path, default=Path(os.environ.get("ATLAS_FACTORY_ROOT", Path(__file__).resolve().parents[1] / "atlas/template-factory")))
    parser.add_argument("--pack", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    preview = commands.add_parser("preview", help="Persist a fixed plan from a JSON request")
    preview.add_argument("--request", type=Path, required=True)
    execute = commands.add_parser("run", help="Validate fixed inputs and queue idempotently")
    execute.add_argument("plan_id")
    execute.add_argument("--expected-plan-digest", required=True)
    execute.add_argument("--idempotency-key", required=True)
    for name in ("status", "report", "pause", "resume", "cancel"):
        sub = commands.add_parser(name)
        sub.add_argument("plan_id")
    amendment = commands.add_parser("amendment-register", help="Append one narrowly authorized budget amendment")
    amendment.add_argument("--request", type=Path, required=True)
    recovery = commands.add_parser("resume-product", help="Supersede one paused G1 job with a scoped product repair")
    recovery.add_argument("plan_id")
    recovery.add_argument("--request", type=Path, required=True)
    preparation = commands.add_parser("prepare-revision", help="Validate a pinned failed-draft patch without queueing or spending budget")
    preparation.add_argument("job_id")
    preparation.add_argument("--request", type=Path, required=True)
    r5 = commands.add_parser("queue-r5", help="Atomically activate inherited-deadline R5 authorization and queue exact prepared repair")
    r5.add_argument("plan_id")
    r5.add_argument("--request", type=Path, required=True)
    grant_register = commands.add_parser("protocol-grant-register", help="Register the fixed one-call protocol retry grant")
    grant_register.add_argument("--request", type=Path, required=True)
    grant_status = commands.add_parser("protocol-grant-status", help="Show one protocol retry grant")
    grant_status.add_argument("grant_id")
    protocol_recovery = commands.add_parser("recover-protocol", help="Resume the fixed paused protocol failure on the same job")
    protocol_recovery.add_argument("job_id")
    protocol_recovery.add_argument("--request", type=Path, required=True)
    evidence_prepare = commands.add_parser("evidence-prepare", help="Read-only prepare for the fixed R7 evidence review")
    evidence_prepare.add_argument("job_id")
    evidence_prepare.add_argument("--request", type=Path, required=True)
    evidence_register = commands.add_parser("evidence-grant-register", help="Register one prepared evidence review grant")
    evidence_register.add_argument("--request", type=Path, required=True)
    evidence_recovery = commands.add_parser("recover-evidence", help="Queue attempt 2 of the same fixed R7 job")
    evidence_recovery.add_argument("job_id")
    evidence_recovery.add_argument("--request", type=Path, required=True)
    evidence_saved = commands.add_parser("resume-evidence-result", help="Queue a checked host-only continuation with the saved result; no CLI retry")
    evidence_saved.add_argument("job_id")
    evidence_saved.add_argument("--request", type=Path, required=True)
    for name, help_text in (("frozen-review-prepare", "Read-only prepare for frozen review recovery"),
                            ("recover-frozen-review", "Recover the same frozen review once"),
                            ("resume-frozen-review-result", "Host-only submission of the saved frozen review")):
        sub = commands.add_parser(name, help=help_text)
        sub.add_argument("job_id")
        sub.add_argument("--request", type=Path, required=True)
    sub = commands.add_parser("frozen-review-grant-register", help="Register one prepared frozen review grant")
    sub.add_argument("--request", type=Path, required=True)
    args = parser.parse_args(argv)
    store = FactoryStore(args.root, args.pack)
    service = BatchService(store)
    try:
        if args.command in {"frozen-review-prepare", "frozen-review-grant-register", "recover-frozen-review", "resume-frozen-review-result"}:
            from .frozen_review_recovery import FrozenReviewRecoveryService
            frozen_service = FrozenReviewRecoveryService(store)
            request = json.loads(args.request.read_text())
            if args.command == "frozen-review-prepare":
                result = frozen_service.prepare(args.job_id, request)
            elif args.command == "frozen-review-grant-register":
                if not isinstance(request, dict) or set(request) != {"prepared_proposal", "request"}:
                    raise FactoryError("grant registration requires prepared_proposal and request", "frozen_recovery_schema", 400)
                result = frozen_service.register(request["prepared_proposal"], request["request"])
            elif args.command == "recover-frozen-review":
                result = frozen_service.recover(args.job_id, request)
            else:
                result = frozen_service.resume_saved_result(args.job_id, request)
        elif args.command == "queue-r5":
            from .r5_execution import R5ExecutionService
            result = R5ExecutionService(store).queue(args.plan_id, json.loads(args.request.read_text()))
        elif args.command == "protocol-grant-register":
            from .protocol_grants import ProtocolRetryGrantService
            request = json.loads(args.request.read_text())
            result = ProtocolRetryGrantService(store).register(request)
        elif args.command == "protocol-grant-status":
            from .protocol_grants import ProtocolRetryGrantService
            result = ProtocolRetryGrantService(store).get(args.grant_id)
        elif args.command == "recover-protocol":
            from .protocol_recovery import ProtocolRecoveryService
            result = ProtocolRecoveryService(store).recover(args.job_id, json.loads(args.request.read_text()))
        elif args.command == "evidence-prepare":
            from .evidence_recovery import EvidenceRecoveryService
            result = EvidenceRecoveryService(store).prepare(args.job_id, json.loads(args.request.read_text()))
        elif args.command == "evidence-grant-register":
            from .evidence_recovery import EvidenceRecoveryService
            request = json.loads(args.request.read_text())
            if not isinstance(request, dict) or set(request) != {"prepared_proposal", "request"}:
                raise FactoryError("grant registration requires prepared_proposal and request", "evidence_recovery_schema", 400)
            result = EvidenceRecoveryService(store).register(request["prepared_proposal"], request["request"])
        elif args.command == "recover-evidence":
            from .evidence_recovery import EvidenceRecoveryService
            result = EvidenceRecoveryService(store).recover(args.job_id, json.loads(args.request.read_text()))
        elif args.command == "resume-evidence-result":
            from .evidence_recovery import EvidenceRecoveryService
            result = EvidenceRecoveryService(store).resume_saved_result(args.job_id, json.loads(args.request.read_text()))
        elif args.command == "prepare-revision":
            from .plan_revision import PreparedRevisionService
            result = PreparedRevisionService(store).prepare(args.job_id, json.loads(args.request.read_text()))
        elif args.command == "preview":
            result = service.preview(json.loads(args.request.read_text()))
        elif args.command == "run":
            result = service.run(args.plan_id, {"expected_plan_digest": args.expected_plan_digest, "idempotency_key": args.idempotency_key})
            ensure_worker(store)
        elif args.command == "amendment-register":
            from .budget import BudgetAmendmentService
            request = json.loads(args.request.read_text())
            result = BudgetAmendmentService(store, campaign_id=request.get("campaign_id", "atlas-v1-first-production-2026-10-19")).register(request)
        elif args.command == "resume-product":
            from .product_recovery import ProductRecoveryService
            request = json.loads(args.request.read_text())
            result = ProductRecoveryService(store).resume_product(args.plan_id, request)
            if request.get("schema") not in {"atlas.product-resume.v2", "atlas.product-resume.v3", "atlas.product-resume.v4"}:
                ensure_worker(store)
        elif args.command in {"status", "report"}:
            result = service.report(args.plan_id)
        else:
            result = service.action(args.plan_id, args.command)
            if args.command == "resume":
                ensure_worker(store)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (FactoryError, ValueError) as error:
        print(json.dumps({"error": str(error), "code": getattr(error, "code", "invalid_request")}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
