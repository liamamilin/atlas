# Independent executor static review — 2026-10-19

This review covers the frozen preparation implementation below. It is a static code and contract review only: the reviewer did not run tests, Docker, Chromium, an application, a provider, or any live job. It does not establish an application pass, a G1 pass, or external phase evidence. Only this review record was written; implementation files and frozen plans were not changed by the reviewer.

| Reviewed file | SHA-256 |
| --- | --- |
| `docker_acceptance.py` | `8c201e56c51f54d83ad2280bcd11671adc9e0474cc2a950bd39707defa6cca87` |
| `bookmark_acceptance_adapter.cjs` | `c35c6919e5d73929dd4b18f587df717da2c9a2eb8d0c52523106d8bf39aeee85` |
| `bookmark_contract_checks.cjs` | `0065f37e2d00e74da01fbde01de26f24904770d8379fb0f67b43a857b281e278` |
| `independent_ui_acceptance.cjs` | `14f996dce2616a630cc494aa7ad8e3d72c8a62ade5253273a66d4fe1fd712760` |
| `phase_contract_fixture_test.py` | `2b8c093e69a394c4913321b724f58448f83ea1fb37b8302a0788a3671b3ed4a0` |
| `machineplan.json` | `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a` |

The observed `machineplan.json` hash matches `PLAN.sha256`. The plan and its seven bookmark cases remain unchanged.

## Execution blocker

**P1 — Application egress contradicts the declared G1 network scope.** At `docker_acceptance.py:779–803`, the runner creates an ordinary bridge, rejects an internal bridge, and attaches the application container to that network. The report explicitly records `network_none: false` and that egress is not enforced (`:683–684`, and its `limitations` field). The current `G1_MANIFEST.json` declares `support_scope.network = "none"`. Chromium's origin allowlist does not constrain network calls made by the application process. Consequently, executing this frozen runner would allow application outbound traffic despite the declared scope. The error text mentioning a parent-approved fallback is not evidence of authorization for a new run.

Required bounded correction before actual execution: enforce the declared application network isolation and expose only the owned host-loopback HTTP path needed by Chromium, without an automatic ordinary-bridge fallback. If that isolated transport is unavailable, record an environment block and emit no passing proof. The controlled fixture is visited by host Chromium and does not require application Internet access. No network probe or application execution was performed in this review.

## Previously identified defects resolved in this frozen version

- The bundle verifier calls the production `delivery.prepare_application()` and `artifacts.tree_manifest()`, compares the official receipt and stored application copy, then hashes the verified application root. This matches `delivery.py:94–178` and `runtime_jobs.py:75–106`: root `.` excludes removed control `delivery.json`; root `app` hashes paths relative to `app/`. The runtime binding uses the formal `artifact_digest` and `selected_phase` fields, and verified content must match `application_digest` before Docker.
- The Python runner passes six non-restart assertions to the actual Node harness initially and all seven after restart. Both layers reject an initial restart assertion. The final combined check retains all frozen cases.
- Move checks require a changed category field, inclusion in the new category, and exclusion from the old category. Search checks include independent category and keyword controls, a nonmatching query, and rendered UI exclusions. Opening requires the exact local-fixture URL.
- Post-restart checks retain original primary/control identities and each of the five original concurrent acknowledgements; they do not substitute newly created replay records for persistence evidence. Container restart checks require equal container IDs, running state on both sides, and changed `StartedAt`.
- The application is mounted read-only and its before/after source hashes must match. Cleanup verifies container/network absence and fixture/thread/temporary-state removal; cleanup or journal failures downgrade a preliminary pass before the proof-writing branch. Proof requires both validated phases and unchanged binding, assertion manifest, adapter, and plan files.

No additional execution blocker was supported by this targeted static review. This conclusion is specific to the hashes above and does not approve a later network-transport revision without review.

## Verification limits

`preparation-2026-10-19.md` reports 14 Python synthetic fixtures, a Node assertion-helper fixture, and syntax checks passing. The reviewer read their implementation and report but did not independently execute them. The Node phase fixture invokes the real harness with fake Playwright and synthetic assertions. The V1 bundle fixture calls production delivery preparation on a synthetic ZIP with root `.`; it does not directly exercise root `app` or a real application. These fixtures remain preparation evidence only. No actual application bundle or real browser journey was inspected or validated, and no `proof.json` was produced by this review.

## Final network-only follow-up — 2026-10-19

The earlier P1 above applies to the historical `8c201e56…` implementation. A subsequent targeted static review of the final network-only correction found that **the original network P1 is closed**, with no additional execution blocker supported within that narrow scope.

| Reviewed file | Final SHA-256 |
| --- | --- |
| `docker_acceptance.py` | `c37db3a4aaf013fe80c43fbdcd19dcd90430e12c367c893309e21d37488df817` |
| `network_none_relay_probe.py` | `ea58b169d0f4376c6469a39c000a6ebe7dee9216c6ddc3d6e7d486d963001da4` |
| `network_none_contract_fixture_test.py` | `fe29735e20e0ec772a719b0dc9328a36b29f1b50cb07d5592daccbf54b5bd339` |

The final runner fixes Docker to `--network none`, contains no port publication or bridge fallback, and checks the effective network mode, sole `none` attachment, and absence of published ports both after creation and after restart. Its host relay listens only on `127.0.0.1` and forwards through `docker exec` to the fixed application container's loopback port. Methods, origin-form paths, body/response sizes, concurrency and timeouts are bounded; upstream redirects are returned without following them. Relay shutdown, request draining and thread termination participate in the cleanup result required before a passing proof can be written.

The reviewer read `verification/network-none-relay-probe.json`: it explicitly classifies itself as a synthetic relay capability probe, records network mode `none` with no published ports before and after the same-container restart, and reports container absence and relay drain/thread cleanup. This is **synthetic transport evidence only, not P0 application acceptance, G1 completion, or `atlas.phase-evidence.v1` proof**. The reviewer did not run that probe, tests, Docker, Chromium, an actual application, a provider, or a live job.

The frozen `machineplan.json` remains SHA-256 `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a`, matching `PLAN.sha256`; no frozen scenario or case was changed. Only this follow-up review record was appended by the reviewer; no implementation source was modified.
