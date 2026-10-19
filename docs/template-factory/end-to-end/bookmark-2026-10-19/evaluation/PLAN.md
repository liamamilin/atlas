# Independent acceptance plan — bookmark pilot

## Frozen scope

Evaluate a personal bookmark manager for the scenario “生活待购与灵感收藏夹” (scenario revision 2). The ordinary user saves external pages for later, organizes them in simple categories, and finds and opens them when needed. This plan is independent of the implementation and will be run against the delivered application through its declared user interface and runtime.

The acceptance target is the complete core workflow: save a URL into the default category; create a separate category; save and move records among categories; browse by category; find a saved record with keyword search; open the record and return to its original external page; and restart the actual application process and verify the saved records and organization remain.

No multi-user, billing, account, or unrelated product requirements are included. The implementation's actual interface, run command, and persistence configuration must come from the newly produced template/application handoff. No endpoint, API, or internal method is presumed by this plan.

## Test isolation and evidence

Run only after the new template and application are delivered. Use a dedicated temporary data directory/database and an isolated local run, or a restricted Docker instance with synthetic records. Do not connect to a provider or use paid services. Do not modify application source during acceptance. Drive the declared UI with real Chromium through the available Playwright installation. Before execution, record the app source revision/hash, template artifact hash, runtime configuration, browser/runtime versions, and exact start/stop commands. Capture screenshots for the main workflow and relevant failure/security checks. Preserve logs and a machine-readable result manifest under this evaluation directory. The evaluator controls the inputs and observes the UI and resulting behavior; developer-reported results are not evidence.

Use stable synthetic content and unique run identifiers. The external-link check should use a controlled local HTTP fixture where practical, so navigation is observable without relying on changing public pages or network access. Any fixture must remain confined to the acceptance run.

## User workflow and acceptance checks

1. **Fresh library and default category:** start with an empty isolated store. Open the library in Chromium and identify the default category through visible UI. Save a synthetic external URL with a distinctive title/keyword without selecting a category. Confirm one record appears in the default category and the displayed URL/title correspond to the submitted values.
2. **Create a separate category:** use the UI to create a category such as `待购-<run-id>`. Confirm it is visible and can be selected. Attempt a whitespace-only category name and confirm the UI reports/requires correction without creating a blank category.
3. **Save and move:** save a second distinct URL directly into the new category. Move the first record from the default category into the new category using the UI. Confirm it disappears from the old category and appears once in the destination. Reload the page and confirm both records and the move remain.
4. **Browse and search:** browse the default and new categories and confirm category membership. Search by a distinctive keyword from each saved record; each query should find the matching record and not a nonmatching record. Clear search and return to category browsing.
5. **Open original page:** click a saved record's visible open link in Chromium. Confirm the browser reaches the exact submitted fixture URL and the fixture page identifies itself as the expected original page. Confirm the bookmark UI did not substitute a local detail page for the destination.
6. **Real process restart:** stop and start the actual application process using the same isolated persistence location, without resetting/reseeding its database. Reopen the UI in Chromium. Confirm both records, their exact URLs, category membership, and searchability persist. A page reload alone does not satisfy this check.

## Negative, safety, and duplicate-effect checks

- **Malformed or missing URL:** submit an empty URL and a malformed URL through the UI. Each must produce a visible validation outcome, create no bookmark, and leave category counts and existing records unchanged.
- **Unsafe URL scheme:** submit a `javascript:` URL as a bookmark destination. The app must reject it or render it inert so clicking a record cannot execute script. No script execution or unsafe navigation is acceptable.
- **Invalid category input:** submit an empty/whitespace category name. It must not create a blank category or alter existing records.
- **HTML output safety:** submit a title/keyword containing harmless HTML/script-shaped text, such as `<img src=x onerror=...>` with a unique sentinel. On list, search, and detail views, the value must render as text or otherwise be safely handled; no injected element, event execution, or dialog may occur. Confirm the sentinel remains searchable if the UI promises title search.
- **No duplicate side effects:** double-submit a save action through normal UI interaction if the interface allows it, and repeat a category-create submission once. Each deliberate action must result in one record/category, not duplicates. If the UI disables repeat submission, verify one result and record that behavior.
- **No dirty data after rejection:** after all rejected inputs, compare the visible record/category inventory with the pre-negative-check inventory; no rejected input may create or mutate data.

## Evidence and verdict rules

For every check record `pass`, `fail`, or `blocked`, the user actions, observed result, screenshot/log references, and relevant app/template hashes. Core workflow checks are all P0 and must pass. Negative/safety checks above must pass where their UI action is supported; if an action cannot be represented through the declared UI, record the limitation and ask the parent to resolve the contract rather than silently substituting an internal API. A blocked isolation or interface contract is not a pass. Do not weaken these frozen checks to accommodate an implementation failure.
