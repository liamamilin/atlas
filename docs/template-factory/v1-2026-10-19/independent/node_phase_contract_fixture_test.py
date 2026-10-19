"""Run the actual Node acceptance harness through synthetic phase adapters.

The fake Playwright module and adapters are runner fixtures only, not app evidence.
"""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
HARNESS = HERE / "independent_ui_acceptance.cjs"
PLAN = json.loads((HERE / "machineplan.json").read_text(encoding="utf-8"))
SCENARIO = PLAN["scenarios"][0]
ALL_CASES = SCENARIO["planned_core_cases"]
RESTART = next(case for case in ALL_CASES if "restart" in case.lower())
INITIAL_CASES = [case for case in ALL_CASES if case != RESTART]


FAKE_PLAYWRIGHT = r"""
exports.chromium = { launch: async () => ({
  newContext: async () => ({
    route: async () => {},
    newPage: async () => ({ on: () => {}, goto: async () => {} }),
    close: async () => {},
  }),
  close: async () => {},
}) };
"""

FIXTURE_ADAPTER = r"""
exports.run = async ({ phase }) => {
  const required = JSON.parse(process.env.REQUIRED_ASSERTIONS_JSON);
  const mode = process.env.FIXTURE_MODE;
  let assertions = required.map(id => ({ id, passed: true, detail: 'synthetic fixture only' }));
  if (mode === 'initial-self-reports-restart') assertions.push({ id: process.env.RESTART_ID, passed: true });
  if (mode === 'after-restart-omits-restart') assertions = assertions.filter(item => item.id !== process.env.RESTART_ID);
  return { assertions, metadata: { fixture: true, phase } };
};
"""


class NodePhaseContractFixtures(unittest.TestCase):
    def invoke(self, phase, required, mode):
        with tempfile.TemporaryDirectory(prefix="atlas-node-phase-fixture-") as tmp:
            root = Path(tmp)
            playwright = root / "fake_playwright.cjs"
            adapter = root / "fixture_adapter.cjs"
            playwright.write_text(FAKE_PLAYWRIGHT, encoding="utf-8")
            adapter.write_text(FIXTURE_ADAPTER, encoding="utf-8")
            env = {
                "PATH": os.environ["PATH"],
                "PLAYWRIGHT_MODULE": str(playwright),
                "PLAYWRIGHT_EXECUTABLE": str(root / "fake-chromium"),
                "APP_URL": "http://127.0.0.1:8000/",
                "FIXTURE_BASE": "http://127.0.0.1:9000",
                "ACCEPTANCE_ADAPTER": str(adapter),
                "SCENARIO_ID": SCENARIO["scenario_id"],
                "REQUIRED_ASSERTIONS_JSON": json.dumps(required, ensure_ascii=False),
                "PHASE": phase,
                "FIXTURE_MODE": mode,
                "RESTART_ID": RESTART,
            }
            return subprocess.run(["node", str(HARNESS)], env=env, text=True, capture_output=True, timeout=15)

    def test_initial_phase_passes_with_six_non_restart_cases(self):
        proc = self.invoke("initial", INITIAL_CASES, "normal")
        self.assertEqual(0, proc.returncode, proc.stderr)
        self.assertEqual(INITIAL_CASES, [item["id"] for item in json.loads(proc.stdout)["assertions"]])

    def test_initial_phase_cannot_self_report_restart_as_passed(self):
        proc = self.invoke("initial", INITIAL_CASES, "initial-self-reports-restart")
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("restart assertion cannot pass before container restart", proc.stderr)

    def test_after_restart_phase_fails_when_restart_case_is_missing(self):
        proc = self.invoke("after-restart", ALL_CASES, "after-restart-omits-restart")
        self.assertNotEqual(0, proc.returncode)
        self.assertIn("adapter omitted required assertions", proc.stderr)
        self.assertIn(RESTART, proc.stderr)


if __name__ == "__main__":
    unittest.main()
