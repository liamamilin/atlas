"""Isolated R8 frozen-revision fixture assembled from tracked review evidence."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys

PACK = Path(__file__).resolve().parents[1]
ROOT = PACK.parent
DOCS = ROOT / "docs/template-factory"
R8 = DOCS / "g1-r8-contract-convergence-2026-10-20"
R7 = DOCS / "g1-frozen-review-recovery-2026-10-20/additional-call-authorization"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_factory_frozen_link import FrozenReviewPipelineLinkTests  # noqa: E402


class FrozenRevisionFixture:
    """Reuse the isolated frozen bundle/library fixture; add tracked R8 bindings."""

    def setUp(self):
        self.base = FrozenReviewPipelineLinkTests(methodName="runTest")
        self.base.setUp()
        self.store, self.root = self.base.store, self.base.root
        self.request = json.loads((R8 / "prepare-request.json").read_text())
        self.r8_final_state = json.loads((R7 / "operations/final-paused-state.json").read_text())
        self.producer = json.loads((R8 / "PRODUCER_CHECKPOINTS.json").read_text())
        self.plan = json.loads((R7 / "operations/final-batch-report.json").read_text())["plan"]
        self._install_r8_inputs()

    def _install_r8_inputs(self):
        root = self.root
        # Authorization and four prepared replacement byte sources are the exact
        # tracked R8 materials; revision_authorizations remains the host registry.
        for rel in (
            "authorization/ATLAS_G1_R8_CONTRACT_CONVERGENCE_CODEX_INSTRUCTIONS.txt",
            "authorization/approved-revision.json",
            "prepared-programs/acceptance/README.md",
            "prepared-programs/acceptance/p0_library.py",
            "prepared-programs/acceptance/p1_maturity.py",
            "prepared-programs/acceptance/runner.json",
        ):
            source = R8 / rel
            target = root / "docs/template-factory/g1-r8-contract-convergence-2026-10-20" / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        approved = json.loads((R8 / "authorization/approved-revision.json").read_text())
        for material in approved["review_materials"]:
            rel = Path(material["path"])
            source = ROOT / rel
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

        frozen = self.r8_final_state["job"]
        acceptance = json.loads((R7 / "actual-attempt-3/acceptance.json").read_text())
        # Lift the old isolated frozen fixture to the real attempt-3 review row.
        with self.store.connect(True) as con:
            con.execute("UPDATE job SET state=?,stage=?,attempt=?,snapshot=?,error=?,updated_at=? WHERE id=?", (
                frozen["state"], frozen["stage"], frozen["attempt"], json.dumps(frozen["snapshot"], ensure_ascii=False),
                json.dumps(frozen["error"], ensure_ascii=False) if frozen["error"] is not None else None,
                frozen["updated_at"], frozen["id"]))
            con.execute("DELETE FROM acceptance WHERE job_id=?", (frozen["id"],))
            con.execute("INSERT INTO acceptance VALUES(?,?,?,?,?,?,?)", (
                acceptance["id"], acceptance["artifact_id"], acceptance["digest"], acceptance["method"],
                acceptance["job_id"], json.dumps(acceptance, ensure_ascii=False), acceptance["created_at"]))
            con.execute("INSERT OR REPLACE INTO v1_plan VALUES(?,?,?,?)", (
                self.plan["id"], self.plan["digest"], json.dumps(self.plan, ensure_ascii=False), self.plan["created_at"]))
            producer = self.producer["job"]
            con.execute("INSERT OR REPLACE INTO batch VALUES(?,?,?,?)", (
                producer["batch_id"], "completed", "{}", producer["created_at"]))
            con.execute("INSERT OR REPLACE INTO job VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (
                producer["id"], producer["batch_id"], producer["kind"], producer["state"], producer["stage"],
                producer["attempt"], None, None, json.dumps(producer["snapshot"], ensure_ascii=False),
                json.dumps(producer["error"], ensure_ascii=False) if producer["error"] is not None else None,
                producer["created_at"], producer["updated_at"]))
            for name, row in self.producer["checkpoints"].items():
                con.execute("INSERT OR REPLACE INTO checkpoint VALUES(?,?,?)", (
                    producer["id"], name, json.dumps(row, ensure_ascii=False)))

        # Upgrade only this temporary store to the tracked pre-resume ledger:
        # 82 factory sessions + one authorized external session = 83 total.
        from template_factory.frozen_review_additional import ensure_table
        with self.store.connect(True) as con:
            ensure_table(con)
            con.execute("DELETE FROM tf_budget_reservation WHERE campaign_id=?", (self.request["binding"]["campaign_id"],))
            for row in self.r8_final_state["reservations"]:
                keys = list(row)
                con.execute(f"INSERT INTO tf_budget_reservation ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                            tuple(row[k] for k in keys))
            con.execute("DELETE FROM tf_frozen_review_time_resume WHERE grant_id=?", (self.r8_final_state["time_resumes"][0]["grant_id"],))
            row = self.r8_final_state["time_resumes"][0]
            keys = list(row)
            con.execute(f"INSERT INTO tf_frozen_review_time_resume ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                        tuple(row[k] for k in keys))
            for grant in self.r8_final_state["grants"]:
                keys = list(grant)
                con.execute(f"INSERT OR REPLACE INTO tf_evidence_recovery_grant ({','.join(keys)}) VALUES ({','.join('?' for _ in keys)})",
                            tuple(grant[k] for k in keys))

