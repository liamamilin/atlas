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
    args = parser.parse_args(argv)
    store = FactoryStore(args.root, args.pack)
    service = BatchService(store)
    try:
        if args.command == "queue-r5":
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
            result = ProductRecoveryService(store).resume_product(args.plan_id, json.loads(args.request.read_text()))
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
