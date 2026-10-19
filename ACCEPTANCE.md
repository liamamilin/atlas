# ACCEPTANCE

## Page Inventory
- [x] All current routes and shared shell are inventoried.
  - Evidence: `docs/U17_PAGE_AUDIT.md` route matrix.
  - Validation: `node --input-type=module` browser crawl in the audit worktree.
  - Status: passed

## Runtime Smoke
- [x] Valid routes render a main heading in an isolated local API/frontend run.
  - Evidence: desktop route crawl; no page errors.
  - Validation: `npx playwright test --repeat-each=3`
  - Status: passed

## Findings Reproduction
- [x] Type source 404, fallback behavior and mobile overflow are recorded with evidence.
  - Evidence: `docs/U17_PAGE_AUDIT.md` sections 2 and 4.
  - Validation: Chromium desktop/mobile crawl.
  - Status: passed

## P1 Correctness Fixes
- [x] Dirty draft body cannot be promoted; body revision/hash is enforced.
  - Evidence: UI disables dedupe/translation/promotion while dirty; API returns 409 for stale body hash; promotion rechecks before publish.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability.CorpusTests.test_draft_body_revision_rejects_stale_save_and_promote -q`; `cd atlas-web && npx playwright test --grep "draft editor"`
  - Status: passed

- [x] Generation completion hydrates the editor and active generation lists bypass stale cache.
  - Evidence: no-store generation list request; recursive detail polling; generating→draft body hydration E2E.
  - Validation: `cd atlas-web && npm test && npx playwright test --grep "draft generation completion"`
  - Status: passed

- [x] Published/draft status conflicts fail closed and slug/write races are rejected.
  - Evidence: promoted/review disagreement projects as `status_conflict`; UI and write APIs become read-only; per-slug file lock serializes create/save/dedupe/promote/delete; review entry is removed with an explicit draft delete.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (195 passed)
  - Status: passed

- [x] Source manifest mapping and no-404 empty state.
  - Evidence: missing manifest returns a 200 empty contract; type pages render `full_md` static fallback or a stable no-source state; preview/dev proxy target and allow-list are constrained.
  - Validation: `cd atlas-web && npx playwright test --grep "source fallback"`; backend source contract regression
  - Status: passed

- [x] Public aliases are searchable and relation/data gates are explicit.
  - Evidence: type/application aliases are generated and scored; search has an in-page editor; relation ids and app leaf references are validated.
  - Validation: `cd atlas-web && npm run gen && npm run verify-data && npx playwright test --grep "aliases"`
  - Status: passed

- [x] Public catalog labels, provenance, and canonical links are navigable in both languages.
  - Evidence: generated app entries carry bilingual names/taglines/task labels and classification evidence; relation targets/kinds have bilingual labels; `.md` links resolve to type routes; the verifier rejects missing canonical link targets and malformed provenance.
  - Validation: `cd atlas-web && npm run gen && npm run verify-data && npx playwright test --grep "public catalog"`
  - Status: passed

- [x] Draft polling exposes stale/disconnected state and retry.
  - Evidence: AbortController-backed single-flight polling with backoff, stale/last-success banner, manual retry, dirty server revision warning, translation single-flight/recovery marker, explicit failed-generation restart, and Router dirty blocker.
  - Validation: `cd atlas-web && npx playwright test --repeat-each=3`（24/24）
  - Status: passed

- [x] Project/iteration identity prevents stale nested state.
  - Evidence: acceptance uses default snapshot ignores rather than focus paths; latest execution alone projects task status; document/requirement approval uses revision CAS; project detail subtree is keyed by project id; unknown generation basis fails closed.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (198 passed); `cd atlas-web && npx playwright test --grep "project detail state"`
  - Status: passed

- [x] Generation/delete and restore lifecycle operations fail closed.
  - Evidence: per-project thread/file locks cover generation prepare/execute/apply, backup, and delete; delete rejects active lifecycle work; restore journal schema 2 records database and artifact ownership fingerprints, atomically installs artifact directories, and explicit recovery refuses replaced content.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（204 passed，含 generation lock 与 restore crash fixtures）
  - Status: passed

- [x] New tasks and acceptance records retain auditable input provenance.
  - Evidence: API task creation requires at least one pinned document version and confirmed requirement; Atlas appends a server-owned acceptance binding with execution, baseline, document versions, requirement revisions, and acceptance-condition snapshot; the project detail page renders the binding and rejects forged binding evidence.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（206 passed）；`cd atlas-web && npm run typecheck && npm test && npx playwright test --grep "project"`
  - Status: passed

- [x] New acceptance decisions record an explicit human result for every pinned condition.
  - Evidence: the API and store require a complete, matched result for every pinned condition; the server-owned binding stores result and note; the project detail page edits and displays each result; legacy bindings without results are explicitly labeled as not backfilled.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q`（207 passed）；`cd atlas-web && npm run typecheck && npm test && npx playwright test --repeat-each=3`
  - Status: passed

- [x] A real OpenCode Go execution can complete and explicitly apply in an isolated workspace.
  - Evidence: using the locally stored OpenCode Go credential without persisting it in the repository, `opencode-go/deepseek-v4.1-flash` completed a disposable analysis and a code task; fixed verification passed, the change stayed in scope, apply adopted a new baseline, and no product acceptance was automatically recorded.
  - Validation: current/clean Python 209 passed; real provider smoke/execute/apply evidence captured in `WORKLOG.md`; targeted Ruff and `git diff --check` passed.
  - Status: passed

- [x] Real generation, backup validation, and restore-to-empty-store preserve the generation result.
  - Evidence: a disposable `deepseek-v4.1-flash` generation completed; its backup passed schema/hash validation; restoring into a new empty store preserved the project and completed generation result; source workspace was not included and no generation result was applied.
  - Validation: current/clean Python 211 passed; real provider generation/backup/restore evidence captured in `WORKLOG.md`; targeted Ruff and `git diff --check` passed.
  - Status: passed

- [x] Classification provider has a real success and a safe, explicit failure boundary.
  - Evidence: disposable `qwen3.8-flash` returned 16 candidates; explicit `opencode-go/deepseek-v4.1-flash` returned provider `model_unavailable`. The classifier maps provider failures to redacted stable codes, does not retry or switch models, and returns classification evidence without changing requirements or corpus state; the pilot adapter follows `ATLAS_ADJUDICATOR` and lazy credential loading.
  - Validation: real classification success/failure smoke; `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (218 passed); `ruff check application-atlas-production-pack/classify.py application-atlas-production-pack/classify_pilot.py`; `git diff --check`
  - Status: passed

- [x] Browser backup/restore management provides a controlled, explicit restore-to-empty-store entry.
  - Evidence: the browser lists validated backups without absolute archive paths, prepares an opaque server-owned `restore_id`, requires a confirmation dialog and API confirmation token, restores only to a new empty store, exposes restore status, and explains that source files are excluded. The API rejects `target_store` and other host-path fields; restore targets overlapping the source workspace are rejected.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (219 passed); `cd atlas-web && npm run typecheck && npm test`; `npx playwright test --grep "backup"` (1/1); `npm run build`; `git diff --check`
  - Status: passed

- [x] Backup lifecycle cleanup is explicit and recoverable.
  - Evidence: archive deletion requires `delete_backup`; interrupted restore cleanup requires `cleanup_partial_restore`; both actions are confirmed in the browser, invalidate the list cache, and preserve project/source data. Atlas does not automatically prune archives.
  - Validation: backend lifecycle/API regressions; frontend typecheck/unit; backup E2E verifies download, restore, delete confirmation, and refreshed list count; `git diff --check`
  - Status: passed

- [x] Provider generation artifacts stay inside Atlas runtime or registered artifact roots.
  - Evidence: generation now initializes a disposable Git project root, writes the V2 policy under `.opencode/`, permits edit access only to `result.json`, and records source-tree additions/mutations/removals in `provider-artifact-violation.json` before failing closed. A disposable real `opencode-go/deepseek-v4.1-flash` generation completed with `artifact_root=runtime`; the repository remained free of provider artifacts.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (213 passed); targeted containment regressions; `ruff check application-atlas-production-pack/project_generation.py`; disposable real generation smoke; `git diff --check`
  - Status: passed

- [x] Generation/provider/backup/restore failures expose stable recovery contracts.
  - Evidence: targeted API errors include `error`, `code`, `retryable` and `details`; generation runs persist `error_code`; the frontend `AtlasApiError` maps conflict, not-found, invalid-request and provider-unavailable states to bilingual recovery messages without automatic retry.
  - Validation: full backend 221 passed; frontend typecheck/unit 9/9; `npx playwright test --repeat-each=3` 51/51; critical-path Ruff/compile; `git diff --check`
  - Status: passed

- [x] Legacy acceptance migration is dry-run first, explicit, transactional and idempotent.
  - Evidence: the migration report identifies missing historical condition results, preserves `acceptance_status`, writes only `not_backfilled` metadata after a fixed confirmation, records a source fingerprint, and is included in project exports; the workbench exposes the report and confirmation flow.
  - Validation: full backend 221 passed; migration store/API/export tests; frontend typecheck and 8 unit tests; `git diff --check`
  - Status: passed

- [x] Local threat-model and security-boundary review is explicit.
  - Evidence: `docs/U17_SECURITY_REVIEW.md` records assets, trust boundaries, residual risks, local evidence and external release blockers; it explicitly excludes OS/container sandbox claims and distinguishes loopback, permission policy, fixed verifiers and path detection from process isolation.
  - Validation: local security pattern scan; 219 backend tests; `git diff --check`
  - Status: passed

- [x] Permission resources, verifier integrity and scan limits fail closed.
  - Evidence: write permission replies require relative resources inside `write_paths`; protected tests/fixtures/verifier files are hash-checked before fixed verification; workspace snapshots reject broad roots and exceed file/byte/depth limits.
  - Validation: `python3 -m unittest application-atlas-production-pack.tests.test_reliability -q` (198 passed)
  - Status: passed

- [x] Unknown routes and route-level failures have explicit recovery.
  - Evidence: wildcard route renders a 404 page; data-router error boundary shows generic reload/home recovery instead of a blank page.
  - Validation: `cd atlas-web && npx playwright test --repeat-each=3` (27/27)
  - Status: passed

- [x] Search and tutorial language paths are explicit and bounded.
  - Evidence: search has an in-page editor and 100-result display cap; English tutorial renders an English source instead of the long Chinese Markdown.
  - Validation: `cd atlas-web && npx playwright test --grep "aliases|English tutorial"`; full E2E 36/36
  - Status: passed

- [x] Apps hash links focus their target and explain missing targets.
  - Evidence: Apps reads `location.hash`, scrolls/focuses the matching card, and renders a recovery message for unknown hashes.
  - Validation: `cd atlas-web && npx playwright test --grep "apps hash"`
  - Status: passed

## Accessibility and Responsive UI
- [x] No unintended body overflow at 320/375/768px.
  - Evidence: 375px browser checks cover Browse, a generated leaf and the draft editor; Prose owns horizontal overflow.
  - Validation: `cd atlas-web && npx playwright test --grep "mobile pages"`
  - Status: passed

- [x] Visible form controls have accessible names.
  - Evidence: draft body textarea has an explicit bilingual accessible name; source tabs expose selected/tabpanel state; Browse disclosures expose expanded/controls state.
  - Validation: `cd atlas-web && npm run typecheck && npx playwright test --grep "draft editor"`
  - Status: passed

- [x] The ten public and project routes have repeatable normal/error/empty, language, responsive, and accessible-name coverage.
  - Evidence: `e2e/tests/matrix.spec.ts` exercises all ten routes at 375/768px, English labels and control names, injected failures, representative empty states, canonical link navigation, and the 404/tutorial import boundary; shared EmptyState and focus-visible/reduced-motion styles are covered.
  - Validation: `cd atlas-web && npx playwright test --repeat-each=3`（51/51）
  - Status: passed

## Documentation
- [x] Page audit and prioritized polish plan exist.
  - Evidence: `docs/U17_PAGE_AUDIT.md`, `docs/U17_PAGE_POLISH_PLAN.md`.
  - Validation: `git diff --check`
  - Status: passed

## Final Marker

`PROJECT_ACCEPTED` is intentionally not written yet: T025/T026 product gates, final cross-cycle verification, and documented external-environment limitations remain.
