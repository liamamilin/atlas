# Independent acceptance preparation checks — 2026-10-19

**Classification: synthetic runner fixtures and static preparation checks only. This is not application/runtime evidence, does not establish a downstream scenario pass, and must not be registered as `atlas.phase-evidence.v1`.** No actual application bundle, runtime target binding, or external runtime evidence directory was supplied. No product app or real Chromium journey was run. One isolated synthetic stdlib app container was launched only for the explicitly approved relay mechanics probe below.

## Exact checks and outcomes

Ran:

```sh
python3 -m unittest \
  docs/template-factory/v1-2026-10-19/independent/phase_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/node_phase_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/binding_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/v1_bundle_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/network_none_contract_fixture_test.py
node docs/template-factory/v1-2026-10-19/independent/bookmark_contract_fixture_test.cjs
python3 -m py_compile \
  docs/template-factory/v1-2026-10-19/independent/docker_acceptance.py \
  docs/template-factory/v1-2026-10-19/independent/phase_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/node_phase_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/binding_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/v1_bundle_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/network_none_contract_fixture_test.py \
  docs/template-factory/v1-2026-10-19/independent/network_none_relay_probe.py
node --check docs/template-factory/v1-2026-10-19/independent/independent_ui_acceptance.cjs
node --check docs/template-factory/v1-2026-10-19/independent/bookmark_acceptance_adapter.cjs
node --check docs/template-factory/v1-2026-10-19/independent/bookmark_contract_checks.cjs
```

All commands exited 0. `python3 docs/template-factory/v1-2026-10-19/independent/docker_acceptance.py --help` also exited 0 and names the formal V1 submission layout. Python reported `Ran 16 tests ... OK`; Node reported `synthetic move/filter/persistence/concurrency and slash-normalization fixtures passed`. The Node harness fixture invoked the actual `independent_ui_acceptance.cjs` with a fake Playwright module and synthetic adapters: initial with six cases passed, initial self-reporting the restart case failed, and after-restart omitting restart failed. The binding fixtures covered a matching generated-application inventory and rejection of wrong target kind, phase, CLI digests, or verified inventory digest; they confirmed the binding check is ordered before the first Docker call. Official V1 bundle fixtures call production `prepare_application()` on a synthetic ZIP, compare its returned receipt byte-semantically as JSON to `delivery-receipt.json`, compare the application copy and extracted `app_root` inventories, verify formal runtime binding fields and archive pin, and reject mismatches before Docker. Bookmark contract fixtures rejected synthetic no-op move, ignored category/keyword filters, altered/missing acknowledged records, and verified root URLs with and without a trailing slash.

A separate static check compared the frozen bookmark scenario's planned cases to the adapter source. Outcome: all 7 case IDs appeared verbatim. SHA-256 verification matched `machineplan.json` to `PLAN.sha256`; the frozen digest remains `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a`.

## Synthetic network relay probe

Ran with approved elevated Docker access:

```sh
python3 docs/template-factory/v1-2026-10-19/independent/network_none_relay_probe.py \
  > docs/template-factory/v1-2026-10-19/independent/verification/network-none-relay-probe.json \
  2> docs/template-factory/v1-2026-10-19/independent/verification/network-none-relay-probe.stderr.log
```

Exit code 0. The preinstalled `docker.io/library/python:3.12-slim` image ID was `sha256:ce9a404c2c0138e747a43e6ea022d2f7e670ed868df35d627a663ba7fb940ea9`; no pull occurred. The synthetic app returned GET 200 and POST 302 with the exact `Location` preserved and no redirect follow. After restart, the container ID remained `ae9a4333eab2d28125ac107908ee1b5d9bf99bcf8e302574e23a85b40cbfac39`, `StartedAt` changed, mode remained `none`, `Networks` contained only `none`, and no ports were published. Probe JSON records relay/thread/container cleanup as successful. A subsequent elevated read-only `docker ps --filter name=bookmark-relay-probe` returned no containers. This probe validates only relay mechanics; it is not a generated application, actual frozen scenario run, or proof.

## Preparation artifact hashes

| File | SHA-256 |
| --- | --- |
| `machineplan.json` | `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a` |
| `docker_acceptance.py` | `c37db3a4aaf013fe80c43fbdcd19dcd90430e12c367c893309e21d37488df817` |
| `independent_ui_acceptance.cjs` | `14f996dce2616a630cc494aa7ad8e3d72c8a62ade5253273a66d4fe1fd712760` |
| `bookmark_acceptance_adapter.cjs` | `c35c6919e5d73929dd4b18f587df717da2c9a2eb8d0c52523106d8bf39aeee85` |
| `bookmark_contract_checks.cjs` | `0065f37e2d00e74da01fbde01de26f24904770d8379fb0f67b43a857b281e278` |
| `phase_contract_fixture_test.py` | `2b8c093e69a394c4913321b724f58448f83ea1fb37b8302a0788a3671b3ed4a0` |
| `node_phase_contract_fixture_test.py` | `5bbd8f31a061d569a258c8b55f95611554cc701d6946db5a98e45490dd89d664` |
| `binding_contract_fixture_test.py` | `d55b7559aa75e5cbbab631c7a85e7d27d72f4ac4597ad86cc3b4304211c179b8` |
| `bookmark_contract_fixture_test.cjs` | `baf1f63c57458a2143603661e47030218f62a8ca2012f7467e4484fa08ba0a7e` |
| `v1_bundle_contract_fixture_test.py` | `6bf9d1f701ed15facd58695d45f47a2755d66ebdf937ac168f0b812291beb1cb` |
| `network_none_contract_fixture_test.py` | `fe29735e20e0ec772a719b0dc9328a36b29f1b50cb07d5592daccbf54b5bd339` |
| `network_none_relay_probe.py` | `ea58b169d0f4376c6469a39c000a6ebe7dee9216c6ddc3d6e7d486d963001da4` |
| `verification/network-none-relay-probe.json` | `441f64c52f242221ba1c26d16b30682d85d7d89bcb021a3aba5042bce7c3896a` |
| `verification/network-none-relay-probe.stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The formal runner invocation also requires `--phase P0` and `--archive-sha256 <host-pinned application.zip SHA-256>`; `--template-digest` carries the binding's formal `artifact_digest`. The actual V1 runtime fields are `selected_phase`, `artifact_digest`, `application_digest`, `suite_digest`, and `case_basis_digest`.

The runtime adapter version is `bookmark-independent-adapter/1.0.0`; a real run report records its hash as `acceptance_adapter_sha256`. Runtime execution is not authorized or possible in this preparation state: the parent reported that no actual app artifact was produced and formally blocked the remaining product repair. Do not substitute fixtures or template sources for the missing app target.
