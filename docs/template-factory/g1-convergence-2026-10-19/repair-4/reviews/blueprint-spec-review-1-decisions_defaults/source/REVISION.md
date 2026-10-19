请对固定的旧冻结候选进行一次正式聚合修订，范围以同一请求中的 REPAIR_SCOPE.json 为准；reuse_spec=false，必须先预审规格，再生成/修订程序，冻结前执行宿主 authored-field 与程序 diff
门禁。不要调用或建议任何未授权模型/工具行为，不要声称测试或运行已通过。请返回完整的新规格及限定的五个程序文件，不能只做 spec-only 补丁。

## Intended aggregate contract

This request revises the pinned draft only. It does not state that the old candidate passed, that repair-2 froze, or
that any acceptance program ran. All original P0 feature IDs, phases, current-required status, and capabilities remain.
A02 single-label hostname rejection is the sole authorized semantic replacement. Every other assertion intent remains;
changes to its implementation may only add the specified browser/UI and directly necessary adaptations. F14/A15 stays
P1.

### Current-required contract coverage

The new `contract_coverage` object maps every P0 `current required` feature to a design basis, user entry, action,
success state/navigation, failure, recovery, and existing acceptance IDs. Host checks enforce fixed schema/review-rule
versions, feature and acceptance references, and completeness of the mapping. The frozen independent reviewer still
judges whether each route is a real complete journey; field presence or keywords do not establish semantic completeness.

### URL policy and A02 change

A record URL must be an absolute, parseable HTTP(S) URL with a valid nonempty hostname. A single-label hostname such as
`http://localhost` is valid. No DNS lookup, network reachability, or target fetch is required. Keep the original
submitted URL string for persistence and opening; opening must navigate to that exact value. Saving, opening, and
actively fetching are distinct; no P0 fetch is added. Preserve negative cases for missing scheme, unsupported schemes,
empty/invalid hostname and assert rejection does not write. Move only the single-label hostname from A02's negative set
to an explicit positive boundary example. Preserve the upstream dotted-host regex as a source observation and explain
its target mapping as `adjusted`, because a dot is not a general URL-validity requirement. If the existing update API
accepts a changed URL, recompute `hostname` from that URL. Do not move duplicate URL behavior to P0: F14/A15 remains P1.

### UI contract and selectors

The browser adapter must use these stable selectors (and may use semantic equivalents only if the frozen authored
contract explicitly declares them): category manager link `a[data-testid="category-manager"]`; create form `form[data-
testid="category-create-form"]` with `input[name="name"]`; rename form `form[data-testid="category-rename-form"]` with
`input[name="category_id"]` and `input[name="name"]`; category-delete form `form[data-testid="category-delete-form"]`
with `input[name="category_id"]`; category-search form `form[data-testid="category-search-form"]` with `select` or
`input[name="category"]` (category name) and `input[name="q"]`; category links and GET `/` preserve both query values.
Rename/delete forms carry `input[name="category_id"]`. Per-record move/delete/restore forms `form[data-testid="record-
move-form"]`, `record-delete-form`, `record-restore-form` carry `input[name="record_id"]`; move uses
`select[name="category_id"]` (API category ID), translated by the HTML handler to the category name expected by the
existing move endpoint. Visible count is `[data-testid="category-count"][data-category-id]`; record row is `tr[data-
testid="record-row"][data-record-id]` with `a[data-testid="record-open-link"]` pointing to the exact saved URL,
`target="_blank"`, `rel="noopener"`; validation feedback is `[data-testid="form-error"]`. Category create/rename/delete
submissions must operate through real forms, report duplicate/invalid/protected-category errors without mutation,
preserve invalid input or provide an actionable recovery path, and navigate to the resulting category state on success.
Category deletion migrates both active and soft-deleted records to `未整理`; a soft-deleted record remains restorable.

Category search is submitted from the real category page and preserves both selected category and q. Show selected
category, retained query and matching/empty results. Test the same keyword across two categories and a no-match query
within one category. The sidebar count is visibly rendered and counts active (non-trashed) records only; compare with
the API and actual list after move, delete, and restore. Move, delete, restore and open are attributed to the selected
row via `data-record-id`; open assertion verifies actual link/navigation target and exact saved URL. Form errors must
not cause 5xx or mutate data; malformed JSON retains the existing `bad_request` and no-write behavior. Keep existing
JSON API acceptance. Remove the unpaired “edit entry” UI promise; do not add a new P0 record-editing feature. Preserve
any existing URL-update API contract and recalculate hostname if URL changes.

### Existing assertions and decision explanations

Preserve all existing P0 obligations not explicitly listed as additions or the A02 replacement: save and stable cross-
restart data (A01), default/preseeded category and save behavior (A03), category move/persistence (A05), category
filtering and counts (A06), keyword fields and empty result (A07), exact original URL opening/unknown ID (A08), soft-
delete/restart/restore (A09), unknown IDs and malformed request non-mutation (A10), health/empty shell (A11), and
invalid category save/move non-mutation (A12). Do not weaken status/error/data-integrity assertions for convenience.
Keep D04's repair-2 impact correction: `trashed_at`, default list filtering, and `/restore`; do not reintroduce
undefined `purge`. Clarify D07 with category-plus-keyword and active-only count behavior. Clarify D08 to describe the
Python-web/SQLite/SSR target and its independent HTTP acceptance. D12 concerns flat category depth, not schema
migration. The architecture describes `schema_meta(version)` and transactional versioned migrations; remove the
erroneous attribution of migration strategy to D12.

### Case adaptation input and source/target boundary

Run case adaptation under a new `case-adaptation-aggregate-v1` input/revision while retaining logical retry scope `case-
adaptation`. The actual formal adaptation input must include target profile `{delivery_profile: python-web, python:
3.12, storage: SQLite, rendering: server-rendered HTML}`, the URL policy stated above, and explicit adaptations: F08/F11
IndexedDB/Dexie + SPA are source facts while target uses SQLite + SSR; preserve local persistence/cross-session and
single-user intent but mark implementation adjusted; preserve upstream dotted-host regex as source fact but map it as
adjusted; source observations are not target requirements. Correct case-design explanations and derived `PRODUCT.md`:
F08 must say persistence behavior is adopted but storage implementation is adjusted; F11 must say target is SSR rather
than an adopted SPA shell. Use only valid IDs from the fixed case evidence basis for adopted/adjusted/not_adopted, and
no invented evidence IDs. New target policies may cite this explicit instruction, not claim upstream evidence. Preserve
fixed case revision, upstream commit, case-basis digest, and all 29 immutable facts.

### Allowed files and exact comparison

The only authorized program paths are `acceptance/p0_library.py`, `acceptance/p0_organize.py`,
`acceptance/p0_find_open.py`, `acceptance/p0_recovery.py`, and `acceptance/README.md`. Keep all other existing
acceptance/reference program files and their assertion intents. Do not edit `acceptance/plan.json`, dependencies, or
application code. `common.py` is not authorized absent a demonstrated concrete helper gap; if such a gap is found, stop
and prepare a separately reviewed scope instead of expanding this request. The host must compare authored fields and
program files to the pinned baseline before freezing. Review the exact pre-freeze authored diff and program diff,
including unchanged identities/phases/current-required statuses and all preserved assertions. Rendered `template.json`,
product docs, host metadata and integrity files are derived outputs and are guarded by authored scope plus host digests,
not treated as acceptance program edits.

### Historical repair-2 reconciliation

The earlier repair-2 request was spec-only and never froze. Preserve its history and baseline. Carry forward its
`bad_request` malformed-JSON correction and corrected D04 impact. Do not carry forward its dotted-host restriction: this
request's explicit target URL policy supersedes that one patch. The original three-point request remains historical
evidence and is not treated as the current complete scope.