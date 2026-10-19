# Blueprint runtime Docker validation

Date: 2026-10-19

The opt-in integration tests ran against the local Docker daemon using synthetic applications and frozen acceptance programs created by the test fixture. No user application, provider, external service, or paid model was used.

## Environment

- Docker server: `28.3.2`, Linux `aarch64`
- `python:3.12-slim`: `sha256:ce9a404c2c0138e747a43e6ea022d2f7e670ed868df35d627a663ba7fb940ea9` (`arm64`)
- `node:22-bookworm-slim`: `sha256:cd2df7ff65c5fce1f8a18ce89e3aac24a80c1db3776d5842a4cf86bc27f300a2` (`arm64`)

## Commands and outcomes

The default mode was checked first. The seven Docker integration cases skip unless the explicit opt-in variable is set:

```sh
python -m unittest tests.test_blueprint_runtime_docker -v
```

Real Docker run:

```sh
ATLAS_RUN_DOCKER_INTEGRATION=1 python -m unittest tests.test_blueprint_runtime_docker -v
```

Result: **7 tests passed in 50.352 seconds**.

The run covered a stdlib Python web app with mixed Python and Node acceptance cases; a Node web app served to a Python acceptance tester; a valid failed acceptance result with exit code 1; a synthetic web process that raises and exits, retaining its traceback while blocking all acceptance cases; startup stderr capture from a caught diagnostic exception in a still-serving app; a Python CLI smoke command plus frozen CLI cases that perform valid addition and verify a negative-input error; source inventory preservation; and cleanup after a two-second total verification timeout. CLI fixtures and outputs live under `{data_dir}`. Every test checked that containers carrying its unique `atlas.factory` owner label were absent at teardown.

Additional checks:

```sh
python -m py_compile tests/test_blueprint_runtime_docker.py
python -m unittest tests.test_blueprint_runtime -v
python -m compileall -q template_factory/blueprint_runtime.py
```

The focused unit suite passed all 13 tests. The opt-in integration module passed syntax compilation and is skipped by default. A trailing-whitespace scan of the four assigned module/test/documentation files found no issues; `git diff --check` passed for the tracked assigned Python modules.

## Limits

The integration run used only the already available trusted image IDs above; it did not test pulling images. The failed-startup case waits for the verifier's 30-second readiness window before asserting the blocked result and captured traceback. The tests do not exercise third-party dependency installation, a real user ZIP, browser/UI behavior, or a network-egress probe. They verify the synthetic app files remain unchanged and that this test run's owned containers are cleaned up.
