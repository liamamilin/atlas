# Template factory V1 CI baseline

Recorded 2026-10-19 on macOS 26.6.2 at HEAD `d0a206dd749e866619379e152b26a880d1d3c104` before this work. The checkout reports `git rev-parse --is-shallow-repository=false` and `git rev-list --count HEAD=68`. A scan of `application-atlas-production-pack/tests` found no test invoking repository history (`git log`, `git show`, or commit ancestry); its Git behavior tests create their own temporary repositories. No fixture was changed for shallow history because there was no dependent test to repair at this HEAD.

The targeted provider transport test passed after isolating `ATLAS_MODEL_CONFIG`, selecting a controlled provider and API key, and asserting `_post_json` was called once:

```text
python -m unittest discover -s application-atlas-production-pack/tests -p test_reliability.py -k provider_http_failure -v
Ran 1 test ... OK
```

Ruff passed for the three files with baseline findings repaired in this change:

```text
ruff check application-atlas-production-pack/template_factory/blueprints.py application-atlas-production-pack/template_factory/delivery.py application-atlas-production-pack/template_factory/runtime_jobs.py
All checks passed!
```

`python -m py_compile application-atlas-production-pack/tests/run_required_docker_integration.py` and `git diff --check` on the changed workflow, package manifest, provider test, and linted Python files both exited 0. The initial sandboxed Docker probe could not access `/Users/milin/.docker/run/docker.sock`; with the user's milestone runtime authorization, the elevated read-only probe confirmed daemon 28.3.2. Both initially absent images were pulled, then the strict runner passed against the local daemon:

```text
ATLAS_RUN_DOCKER_INTEGRATION=1 python application-atlas-production-pack/tests/run_required_docker_integration.py
Ran 18 tests in 54.585s
OK
{"daemon_version":"28.3.2","errors":0,"failures":0,"images":["node:22-bookworm-slim","python:3.12-slim"],"skipped":0,"status":"passed","tests_run":18}
```

This includes the existing API-queued frozen-source Docker test in addition to synthetic verifier integration cases. It is real local Docker execution evidence for repository tests, not a real generated application acceptance result. CI pulls both images on its ephemeral Ubuntu runner before invoking the same strict runner; the runner rejects a missing opt-in, CLI, daemon, image, test failure, or any skipped test.

For the T05 phase-evidence contract, `python -m unittest discover -s application-atlas-production-pack/tests -p test_blueprint_runtime.py -v` passed 14 tests. The focused runtime-job tests for missing independent evidence and changed frozen suite each passed (1 test each). The full runtime-job module passed 10 tests and skipped its one opt-in Docker case when run without the flag; the strict Docker gate above ran that opt-in case and had zero skips. These tests prove a passing suite with missing phase requirements remains unverified, changed app/suite inputs cannot reuse the run, and a host-written, digest- and target-bound external record can complete phase status. They use synthetic test evidence and do not prove a real generated application's external restart/concurrency checks.

The baseline Ruff check of the full `application-atlas-production-pack/template_factory` directory initially reported nine issues: unused variables/imports in `blueprints.py`, `budget.py`, and `delivery.py`, an unused import in `runtime_jobs.py`, and three E701 lines in `cli.py`. This change removed the four findings in `blueprints.py`, `delivery.py`, and `runtime_jobs.py`. The `budget.py` and `cli.py` findings belong to concurrent budget work and are not represented here as passing; the full directory lint result must be recorded after that work lands.

Local tool availability: Python 3.10.13, Node v22.21.1, npm 10.9.4, Docker CLI 28.3.2. The OpenCode executable is installed, but its version probe could not open the user-level OpenCode log due to sandbox `EPERM`; no OpenCode version is claimed. The full backend suite and either Playwright suite were not run in this task because the parent is running the full backend suite and no Playwright run was needed to validate the scoped changes.
