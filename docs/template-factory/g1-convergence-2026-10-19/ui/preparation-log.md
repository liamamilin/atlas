# G1 independent UI acceptance preparation

**Status:** executor preparation complete; no generated application bundle or actual runtime target binding was supplied to this work package. This log records adapter fixtures and deadline-contract validation only. It is not application/runtime evidence, does not establish P0 or G1 pass, and must not be registered as `atlas.phase-evidence.v1`.

The independent Chromium adapter is now `bookmark-independent-adapter/2.0.0`. It drives category create/rename/delete, record move, category-page search, soft-delete/restore, invalid-form recovery, and URL opening through the documented semantic HTML controls. It verifies the selected category and keyword survive a real form submit, the count shown in the sidebar matches active API results, deleting a category migrates active and trashed rows to the default category, and the actual Chromium popup reaches the exact saved URL. APIs remain limited to fixture setup, persisted-state readback, and concurrent write inputs.

The supplementary selector contract and frozen-plan compatibility notes are in [ADAPTER_REVISION_2.md](../../v1-2026-10-19/independent/ADAPTER_REVISION_2.md). The original `machineplan.json` still hashes to `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a`, matching `PLAN.sha256` exactly.

The Docker/Chromium runner now requires a host-pinned response from the official effective-budget API for the exact campaign, plan, product, segment, and runtime job. G1 is the default segment; T08 must be selected explicitly and cannot use the G1 amendment deadline. It verifies the snapshot hash and binding and rejects an expired `effective_deadline` before runtime setup, Docker preflight, each Chromium phase, same-container restart, and proof creation. The prior base deadline is retained as context; a properly activated G1 amendment uses the official effective deadline. The snapshot digest and checks are recorded in the run evidence and phase proof.

## Checks run

All final commands below exited 0. The browser command was run with the local Chromium installation outside the normal process sandbox because the sandboxed launch fails at macOS `MachPortRendezvousServer` bootstrap before page navigation.

```sh
node --check docs/template-factory/v1-2026-10-19/independent/bookmark_acceptance_adapter.cjs
node --check docs/template-factory/v1-2026-10-19/independent/ui_contract_fixture_test.cjs
node docs/template-factory/v1-2026-10-19/independent/ui_contract_fixture_test.cjs
node docs/template-factory/v1-2026-10-19/independent/bookmark_contract_fixture_test.cjs
python3 -m unittest docs/template-factory/v1-2026-10-19/independent/budget_context_fixture_test.py
python3 -m py_compile docs/template-factory/v1-2026-10-19/independent/docker_acceptance.py docs/template-factory/v1-2026-10-19/independent/budget_context_fixture_test.py
python3 docs/template-factory/v1-2026-10-19/independent/docker_acceptance.py --help
```

Real Chromium reported: `real Chromium detected missing move control and category-dropping search form while fixture APIs remained functional`. The negative fixtures have a working category-plus-keyword JSON query and move endpoint, but one page omits the move form and the other submits a disabled category selection; the adapter rejected both. The updated bookmark helper fixture passed, including a cross-category record with the same keyword; a query-only result is rejected because it includes that control in the combined results. Seven pinned-budget cases passed: valid amended deadline despite expired base deadline, expired deadline rejection, runtime binding mismatch rejection, changed pinned bytes rejection, missing amendment activation rejection, T08 base deadline acceptance, and T08 rejection of a G1 amendment. Python compilation and runner CLI help succeeded.

## Frozen file digests

| File | SHA-256 |
| --- | --- |
| `machineplan.json` | `5e352e1cdbad18d5dbf827e37e9e0f394f0e7fbf919b0dd18713f7affb6ebb3a` |
| `bookmark_acceptance_adapter.cjs` | `730b154c798e821875c57ff3115162eb5cc2f456a3ce46b9c2b483e51b9588ac` |
| `bookmark_contract_checks.cjs` | `efb55bcccf52a6bc3c7855ae8acdd0341dbd964bbe4aeb604677c3aa0c1e5602` |
| `bookmark_contract_fixture_test.cjs` | `0de87e01562ad27330037f7b146e29dde285da56caead7d3bcb7f064b6329795` |
| `docker_acceptance.py` | `7dfa5cc10d61adde10178818d5e161bec5f79261cf552d45857ba9065d0bb508` |
| `ui_contract_fixture_test.cjs` | `00b5ce6bc92dd62552ff403461c12ee9f7209b791cecae452380438d896c2dba` |
| `budget_context_fixture_test.py` | `c4931d62aaa43140bc23383e07ccdd4268ff6f2a3a9d838d615529c1f5650729` |
| `ADAPTER_REVISION_2.md` | `1978dbe6d3f4463def4bdc06ed7371ac23afb718da3d504951c6e5f3a4070618` |

Actual runtime acceptance remains pending the parent-provided official runtime job IDs and host-pinned effective-budget API response, plus the actual P0 application submission, target binding, template/suite/case-basis digests, and required-assertion manifest. No real runtime command was run here.

Parent integration clarification: the final visible anchor href is the exact original URL; `/go/{id}` remains a separate API redirect assertion. The HTML invalid-URL action uses an unsupported `ftp://` URL, which is syntactically URL-shaped and reaches standard HTML URL validation while violating the product HTTP(S) policy; feedback retains that exact input and correction submits a valid controlled HTTP URL. This avoids confusing browser-native syntax rejection with server-rendered form-error coverage. No application runtime pass is claimed.
