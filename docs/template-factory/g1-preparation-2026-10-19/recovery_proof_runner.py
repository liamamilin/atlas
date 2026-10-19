"""Run local fake-CLI recovery regressions and retain their byte-level evidence."""
import hashlib
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "application-atlas-production-pack/tests"))
from test_factory_context_recovery_v1 import V1ContextRecoveryTests
from template_factory.artifacts import tree_manifest

WITNESSES = []


class CapturedRecoveryTests(V1ContextRecoveryTests):
    def tearDown(self):
        for job_dir in sorted((self.store.root / "jobs").iterdir()):
            first = job_dir / "attempt-1/blueprint-generate-0"
            second = job_dir / "attempt-2/blueprint-generate-0"
            if not first.is_dir() or not second.is_dir():
                continue
            receipt = second / "recovery-receipt.json"
            manifests = [tree_manifest(path / "source") for path in (first, second)]
            evidence = {name: hashlib.sha256((first / name).read_bytes()).hexdigest()
                        for name in ("input.json", "stdout.log", "result.json", "cli-summary.json")}
            checkpoint = self.store.checkpoint(job_dir.name, "blueprint-plan-0")
            WITNESSES.append({
                "test": self._testMethodName, "temporary_job_id": job_dir.name,
                "state": self.store.job(job_dir.name)["state"],
                "generation_cli_summaries": len(list(job_dir.glob("attempt-*/blueprint-generate-0/cli-summary.json"))),
                "input_bytes_equal": (first / "input.json").read_bytes() == (second / "input.json").read_bytes(),
                "source_bytes_equal": manifests[0] == manifests[1],
                "source_manifests": {"first": manifests[0], "rebuilt": manifests[1]},
                "original_delivery_sha256": evidence,
                "recovery_receipt": json.loads(receipt.read_text()) if receipt.exists() else None,
                "normalized_plan_checkpoint_digest": checkpoint["digest"] if checkpoint else None,
            })
        super().tearDown()


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(CapturedRecoveryTests))
    report = {"scope": "Temporary V1 stores and fake CLI only; no real provider, production queue or G1 acceptance.",
              "tests_run": result.testsRun, "successful": result.wasSuccessful(), "witnesses": WITNESSES}
    (HERE / "verification/recovery-byte-evidence.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    raise SystemExit(not result.wasSuccessful())
