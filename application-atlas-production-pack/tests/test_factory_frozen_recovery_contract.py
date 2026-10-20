"""Focused negative contracts for the fixed frozen-review grant."""
from __future__ import annotations

import copy
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_factory_frozen_link import FrozenReviewPipelineLinkTests

from template_factory.budget import BudgetLedger
from template_factory.frozen_review_recovery import (
    AUTH_REF, AUTH_SHA256, JOB_ID, REQUEST_KEY, FrozenReviewRecoveryService,
)
from template_factory.store import FactoryError, digest


class FrozenReviewRecoveryContractTests(FrozenReviewPipelineLinkTests):
    def _request(self):
        return {"schema": "atlas.frozen-review-prepare.v1", "request_key": REQUEST_KEY,
                "source_authorization": {"source_ref": AUTH_REF, "source_digest": AUTH_SHA256},
                "source_gate": {"source_commit": "a" * 40, "source_tree_digest": "b" * 64,
                                "ci_evidence": [{"path": "docs/template-factory/g1-frozen-review-recovery-2026-10-20/fixture-ci.json",
                                                 "sha256": "c" * 64, "run_id": 4242, "head_sha": "a" * 40,
                                                 "required_checks": ["check", "docker-integration"]}]}}

    def _service(self):
        return FrozenReviewRecoveryService(self.store, clock=lambda: 1792489000,
                                           source_gate_validator=lambda _store, value: value)

    def test_ungranted_retry_none_and_changed_stage_cannot_reserve(self):
        ledger = BudgetLedger(self.store, campaign_id=CAMPAIGN,
                              clock=lambda: 1792489000)
        for retry, stage in ((None, "cognitive-review:new-payload"), (1, "cognitive-review:572da86649b4face")):
            with self.subTest(retry=retry, stage=stage), self.assertRaises(FactoryError) as caught:
                ledger.reserve(PRODUCT, "G1", "review", 1800, job_id=JOB_ID,
                               requested_model="opencode-go/deepseek-v4.1-flash", stage=stage,
                               retry=retry, retry_scope="cognitive-review", plan_id=PLAN_ID)
            self.assertEqual(caught.exception.code, "evidence_grant_binding")

    def test_changed_proposal_or_same_key_changed_request_is_rejected(self):
        request = self._request()
        service = self._service()
        proposal = service.prepare(JOB_ID, request)
        changed = copy.deepcopy(proposal)
        changed["materials"]["frozen_review_call"]["timeout_seconds"] = 1801
        changed["proposal_digest"] = digest({k: v for k, v in changed.items() if k != "proposal_digest"})
        with self.assertRaises(FactoryError):
            service.register(changed, request)
        with self.assertRaises(FactoryError):
            service.register(proposal, {**request, "source_gate": {**request["source_gate"], "source_commit": "d" * 40}})


PRODUCT = "product-c42848f63251507bd9d911a5"
PLAN_ID = "plan_87059846caf345d2b2fe690657cf324f"
CAMPAIGN = "atlas-v1-first-production-2026-10-19"


if __name__ == "__main__":
    unittest.main()
