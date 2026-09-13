# Research Notes — Software Test Management

## Research Goal

Establish what "Software Test Management" is as an Application Type in directory §12 (Software Development & Product Engineering): what objects exist inside it, who uses it, how the testing loop works, what states and rules matter, and where its boundaries lie against neighboring Types — Test Automation Platform (§12, unprocessed), End-to-end Testing Platform (§12, processed), Unit/Integration Test Runner (§12, unprocessed), Issue Tracker / Bug Tracking System (§12, processed), Engineering Project Management Platform (§12, processed), Requirements Management Platform (§12, processed, alias of engineering-requirements-management), Continuous Integration Platform (§12, processed), and Product Test Management (§16, processed — joint review forwarded to this pass).

## Initial Boundary

Working hypothesis before research:

- This is the software team's system of record for its testing effort: test cases, test plans, test runs, recorded results, defect links, requirement coverage.
- Nearest confusion risks: (a) test automation platforms (execution vs management), (b) issue trackers (defect records), (c) requirements management (traceability source), (d) the §16 sibling Product Test Management (same object vocabulary, different subject).
- The §16 pass pre-drew the seam: §16 = product/engineering-program instance (verification of engineered products against product requirements, regulatory/design-review sign-off); §12 = expected software-team instance (application build/release cycle, automation frameworks, CI). Joint review recommended at this pass.

## Research Questions

1. What is the core object — the test case? What does it carry (steps, expected results, preconditions, types)?
2. What is a test run / test set / cycle? How does a planned execution relate to the case library?
3. How are verdicts recorded (statuses, per-step results, evidence, history)?
4. How do plans/milestones/releases organize runs?
5. How do defects link to failed executions? Who owns the defect record?
6. How does requirement coverage work — native object or external reference?
7. How does automation integrate (results import, CI attachment)? Does the management system itself execute?
8. What roles/permissions exist (tester, test lead, admin)?
9. What reports/metrics does the management loop produce (progress, pass rate, coverage, release readiness)?
10. Where exactly is the boundary vs test automation platforms, issue trackers, requirements management, and the §16 sibling?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer level:

1. **TestRail** (SmartBear/Gurock) — standalone dedicated test case management; the category archetype; mid-market/enterprise.
2. **PractiTest** — independent SaaS test management; analytics/methodology-first; SMB/mid-market.
3. **Zephyr** (SmartBear, ex-TM4J/Zephyr Scale) — Jira-native test management app; team-level, ecosystem-embedded.
4. **qTest** (Tricentis) — enterprise test management inside a broader quality platform (Tosca etc.); large-org pole.
5. **Codebeamer** (PTC) — ALM platform whose test management serves software AND product/hardware programs; the regulated/ALM pole that discharges the §16 joint review.

## Sources

Research date: 2026-09-09.

- TestRail Support Center (Tier 1): https://support.testrail.com/hc/en-us — Introduction to TestRail; Submitting test results; Introduction to reference and defect integrations; section listings (test cases, test planning and execution, reporting, enterprise guide, test automation/CLI, API).
- PractiTest Help Center (Tier 1): https://www.practitest.com/help/ — Tests; Test Sets & Runs; help-center category structure (requirements, issues, dashboards, automation integration, API).
- Zephyr Documentation (Tier 1): https://support.smartbear.com/zephyr/docs/en/ — Test Cases Overview; Test Cycles (Overview); docs tree (test plans, automation, CI, reports, REST API, permissions, custom fields); Atlassian Marketplace listing (Tier 2).
- qTest (Tier 2 only): https://www.tricentis.com/products/qtest — product page. Tricentis documentation portals unreachable (docs.tricentis.com returned empty; documentation.tricentis.com 404; docs.tricentis.com/qtest login-walled). Assertions about qTest held at product-page strength.
- Codebeamer (Tier 2 only): https://codebeamer.com/ — homepage (core capabilities list incl. "QA and Test Management"; industry solutions medical/automotive/aviation/pharma). intland.com QA page unreachable (2 transport errors); PTC Help Center welcome page reachable but test-management section URL not located; deep mechanics not verified in this pass (consistent with the §16 pass's own Codebeamer limitation).
- Xray: docs.getxray.app requires JS (4 URL patterns returned only the portal shell) — abandoned per network rules; Xray NOT used as a sampled product. Zephyr substituted as the Jira-native pole.

## Product Observations

### TestRail (Layer A — directly observed, deep)

- Self-description: "a web-based test case management tool… used by QA engineers, developers, and team leads to manage, track, and organize software testing efforts."
- **Test case**: consists of a description of the test's prerequisites, a list of test steps, and the expected result; "can ideally be verified by a single tester in a short period of time and confirms a specific functionality."
- **Organization**: cases organized into sections and sub-sections (per project module/feature); projects are the main organizational unit; suites hold cases ("a test suite is just like a plan that specifies how an application is tested").
- **Test run**: started for a suite; can include all cases, specific cases, or a dynamic filter; "a run consists of individual tests for each case"; multiple concurrent runs for different configurations (e.g., OS); runs assigned to milestones; closing a run archives it — tests of a closed run cannot be edited, and later case-attribute changes do not propagate into the closed run.
- **Verdicts**: each test has a status; default set Untested / Passed / Failed / Retest / Blocked (customizable); once a result is added, a test can never return to Untested.
- **Result dialog**: status (only mandatory field), comment, attachments, assign-to, version (build under test), elapsed time (with in-product timer), defects field, per-step results with actual result for steps templates; custom result fields supported.
- **Result tracking**: results & comments (chronological per case in run), history & context (chart of the case's results over time + latest result per run), defects view (all defects of the same case over time).
- **Test plans & configurations**: a plan starts multiple runs at once; configurations (OS/browser combos) generate one run per configuration combination.
- **Milestones**: release anchors (public release, internal test version, beta); runs assigned to milestones; milestone-level progress tracked.
- **Assignment & coordination**: tests assigned to team members; per-user to-do lists; team leads assign by workload; email notifications; subscribe to tests/runs.
- **Progress & reporting**: status/activity/progress views on runs and milestones; project history; charts and dashboards; reports module.
- **Defect integration**: defects tracked in external trackers; link by ID, push new defects from the result dialog (defect plugins), hover to fetch live defect data, defect status surfaced on runs/plans/milestones.
- **Requirements**: NO native requirement object — a References field on cases/runs/plans/milestones holds requirement/user-story IDs or URLs from external systems; coverage and traceability reports are generated from references.
- **Automation**: TestRail CLI ("open source command-line tool that makes it easy to upload test automation results"); JUnit-to-TestRail mapping; API for importing results; integrations with automation frameworks (Ranorex, Postman, WebdriverIO, JMeter, k6…) and CI tools (Jenkins, GitHub Actions, GitLab CI, Azure Pipelines, CircleCI).
- **Enterprise tier**: test case versioning, test case review & approvals, test parameterization/variables/datasets, project-level administration.

### PractiTest (Layer A — directly observed, deep)

- Self-description: managing "the entire QA process from requirements through tests to issues, all on one centralized platform"; can "automatically show you which requirements are not covered by tests."
- **Test Library**: where tests are created, managed, stored; four test types — Scripted (predefined steps), Exploratory (charters + on-the-fly annotations, session-based, runs once), BDD (Gherkin scenarios; scenario outlines expand to per-example instances), Automated (results via REST API, FireCracker XML conversion from CI/CD, or xBot internal framework).
- **Test Sets & Runs**: a Test Set is a group of tests run together (per feature, per task such as regression/sanity, or per tester/day); a Test Instance is "a dynamic duplicate" of the library test — editing an instance does not alter the original; each instance can run multiple times; the set grid shows the last run's status.
- **Run mechanics**: step-level pass/fail during the run; "Fail & Issue" reports a defect from the steps already executed and links it to the run (internal Issues module, or directly into Jira/external tracker with 2-way sync); link-existing-issue supported; N/A steps don't fail the run.
- **Run status computation** (documented algorithm): NO RUN → FAILED if any step failed → BLOCKED if any blocked → NOT COMPLETED while partially run → PASSED only when all steps passed/N-A → N/A if all N/A. The library shows the test's last run status across all sets.
- **Fast Run**: bulk verdicts (Pass All / Fail All / Block All / No Run All) without step detail.
- **Traceability tab on a test**: its instances across sets, issues found by it, requirements it covers, tests calling it.
- **Test workflow** (Corporate tier): statuses Draft / Ready / To repair / Obsolete + custom, with transitions, role-gated transitions, edit locks and execution locks per status.
- **Requirements module**: native; coverage views (uncovered requirements); test sets can be created from requirements' linked tests.
- **Issues module**: native defect records; Linked Issues tab on test sets aggregates all issues from its runs.
- **Dashboards & reports**: dashboards, reports, PTQL query language; drill-down from dashboards to instance view.
- **Milestones; time management** (estimated vs actual run duration, timers); **parameters** (step parameters per instance; BDD examples as static parameters); **test set permutations** (combinations); **enforce run order** (sequential execution gating, license-tier feature); **followers/notifications**; batch edit/clone; import from Excel/CSV/Google Sheets.

### Zephyr (Layer A — directly observed, medium depth)

- Positioning (marketplace): "Test Management and Automation for Jira"; "a dedicated testing system of record, not an extension of Jira work items"; "centralize test cases, execution history, and outcomes in one auditable system… full traceability across Jira work items… measurable proof of release readiness."
- **Test case**: "a defined set of conditions, inputs, actions, and expected results for checking if a specific feature or function works as expected"; created as Jira issue type; organized in hierarchical folders; shared/reusable steps; parameters; call-to-test (modular design); version control of cases; Gherkin/BDD; data-driven design; attachments per step; import from Excel/CSV.
- **Test cycle**: "a focused set of test cases grouped to achieve specific testing goals… assigned to specific testers and test environments. Examples… regression tests, build-verification tests, end-to-end tests." When a case is executed, the result is linked to the cycle, storing tester, execution date, defects raised, environment used, and status (passed/failed/…). Cycle view tracks estimated vs actual effort, success/completion rates, issues raised; progress bars with per-status breakdown.
- **Test plan**: "test cycles often make up parts of a test plan, which is used to track large-scale testing iterations, like an entire release or new version."
- **Traceability**: across requirements (Jira issues), tests, executions, defects; traceability in test cases/cycles/plans/executions; end-to-end traceability reports.
- **Automation**: JUnit/NUnit/pytest/Robot/TestNG/Cucumber integrations; Jenkins/Bamboo CI; REST API; plus bundled no-code automation/record-and-play (Advanced edition) — an execution capability inside a management product.
- **Configuration**: custom fields for test cases, cycles, plans, steps, and executions; environments/labels/iterations; datasets; priorities/statuses configurable; permissions; delete/archive.
- **Reports**: traceability reports, cross-project reports, custom templates, Jira gadgets, Power BI.

### qTest (Tier 2 — product page only; assertions held at that strength)

- Positioning: "enterprise test management"; "unified quality, test coverage, and actionable insights at scale"; part of the Tricentis quality platform.
- Test case management "across projects and methodologies… including approval workflows, version control, and role-based access."
- End-to-end traceability: "which test case version failed, which changes were approved, and which tests were executed"; requirements→tests traceability via "real-time ALM integrations."
- Automation orchestration: "manage, schedule, and report on automated tests across frameworks, tools, and environments"; universal agent; CI/CD integration; parameterized test cases "automatically generate test run combinations."
- Analytics: "60+ built-in widgets and customizable dashboards and reports indicating defect status, test coverage, and readiness"; release-readiness framing.
- Exploratory testing (qTest Explorer): capture sessions (notes, screenshots, steps) and "convert session outcomes into documented test cases and automated scripts."
- Jira synchronization; open integrations with CI/CD, APM, DevOps tools.

### Codebeamer (Tier 2 — homepage + §16 pass's prior observations)

- Positioning: "integrated Application Lifecycle Management platform"; core capabilities list includes Requirements Management, Software Development, **QA and Test Management**, Risk Management; industry solutions for medical, automotive, aviation, pharmaceutical.
- Confirms the market pattern: one ALM platform sells the same test-management capability to software teams and to product/hardware programs (the §16 pass reached the same conclusion and used Codebeamer as Tier-2 confirmation).
- Deep object mechanics not verified in this pass (help-center section not located; wiki login-walled) — held at market-structure strength only.

## Cross-product Comparison

| Aspect | TestRail | PractiTest | Zephyr | qTest | Codebeamer |
|---|---|---|---|---|---|
| Test case of record | Yes — prerequisites + steps + expected result, in sections/suites | Yes — library with 4 types (scripted/exploratory/BDD/automated) | Yes — Jira issue type, folders, steps/params/BDD | Yes (product page) | Yes (market pattern; §16 pass) |
| Planned execution container | Test run (from suite, filtered); test plan = multiple runs × configurations | Test Set → Test Instances → Runs | Test Cycle → executions; Test Plan → cycles | Runs; parameterized run combinations | Test plans/runs (§16 pass) |
| Verdict recording | Per-test status (5 defaults, customizable); per-step results; result history | Per-step pass/fail; documented run-status computation; Fast Run bulk | Execution status linked to cycle (tester/date/defects/environment) | Yes (product page) | Yes (market pattern) |
| Assignment / to-dos | Yes — assign tests, to-do lists, notifications | Yes — assignees, followers, enforce run order | Yes — assign testers per cycle | Yes (role-based access) | Yes (market pattern) |
| Defect linkage | External trackers (link/push/hover) | Native Issues module + 2-way Jira sync | Native (Jira issues) | Yes (defect status in dashboards) | Native (ALM) |
| Requirement coverage | References field + coverage/traceability reports (no native object) | Native Requirements module + coverage | Jira issue links + traceability reports | ALM integrations, real-time | Native (ALM) |
| Automation results import | CLI (JUnit mapping), API, framework + CI integrations | REST API, FireCracker (CI XML), xBot | JUnit/NUnit/pytest/Robot/TestNG/Cucumber, Jenkins/Bamboo, REST API | Universal agent, CI/CD | Yes (market pattern) |
| Execution by the management product itself | No (manual execution recorded; automation imported) | No (xBot is an optional internal runner) | Partially — bundled no-code automation (Advanced edition) | Orchestration/scheduling of external automation | Not verified |
| Reports / dashboards | Charts, dashboards, reports module | Dashboards, reports, PTQL | Traceability/cross-project reports, gadgets, Power BI | 60+ widgets, release readiness | Yes (market pattern) |
| Case versioning / approvals | Enterprise tier | Test workflow (statuses/locks, Corporate) | Version control | Approval workflows, version control | Baselines (§16 pass) |
| Exploratory / session testing | — (not observed as first-class) | Native test type (charters, annotations) | Record-and-play toward automation | qTest Explorer | — |
| Host substrate | Standalone web app | Standalone SaaS | Jira app | Standalone, part of Tricentis platform | ALM suite module |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The test case of record** — a persistent, individually identified, re-runnable definition of how to verify a piece of the product's behavior: what to do and the basis for judgment (expected results/acceptance checks), held in an organized library (sections/folders/suites). The step list is the dominant realization, not the invariant — exploratory/charter-style and BDD-style cases exist in-sample without predefined steps. Remove → a wiki/document/issue pile with no verification memory.
2. **The test run with recorded verdicts** — a planned execution that instantiates selected cases against a specific scope (release/build/configuration/environment), tracks each case instance to a recorded verdict evaluated against the case's expected basis, and retains the verdict with context (who, when, notes/evidence, commonly per-step outcomes). Remove → a case library with no execution memory, or ad-hoc checklists.
3. **The managed testing effort** — runs organized under planning containers (plans/cycles/milestones/releases), execution assigned to testers, progress tracked against the plan, and status/coverage aggregated and reported so the effort can be managed and release decisions informed. Remove → an execution log (record-keeping without management), or a schedule with nothing behind it.

Jointly-held load-bearing: 1 alone = test-case document library; 2 without 1 = ad-hoc run sheets; 3 without 1+2 = dashboard over nothing; 1+2 without 3 = execution log, not management; 1+3 without 2 = planning shell with no recorded truth; 2+3 without 1 = one-off checklists with no reusable definitions.

### L1 — Common Mature Structure

- **Requirement linkage & coverage** — cases linked to the requirements/stories they verify; coverage and traceability views/reports. Dominant modern organizing structure, but NOT definitional: TestRail holds requirements only as external references and still is archetypal test management; paper-era test plans keyed to specification documents satisfy the Type without formal requirement records.
- **Defect linkage loop** — failed executions raise/link tracked defects; defect status surfaced on runs/plans; re-test after fix (Retest-class statuses). Ownership of the defect record stays with the issue tracker (or a bundled module — packaging).
- **Automation results import** — results from automation frameworks/CI imported via CLI/API/adapters onto the managed runs; the management system plans and proves, the frameworks execute. Bundled execution engines (Zephyr Advanced no-code automation, PractiTest xBot, qTest orchestration) are packaging, not identity.
- **Assignment & coordination** — tests/instances assigned to testers; to-do lists; notifications/followers; workload balancing.
- **Configurations, environments, parameterization** — one case executed across OS/browser/environment combinations; data-driven cases; run permutations.
- **Reports & dashboards** — progress, pass rates, effort (estimated vs actual), coverage, release readiness.
- **Case versioning, review/approval workflows** — enterprise-tier machinery (TestRail Enterprise, Zephyr version control, qTest approvals, PractiTest workflow locks).
- **Reuse machinery** — shared steps, call-to-test, cross-project clone, import from spreadsheets/other tools.

### L2 — Variant / Optional Structure

- **Host substrate** — standalone web application (TestRail, PractiTest) vs issue-tracker-embedded app (Zephyr in Jira) vs quality-platform module (qTest in Tricentis) vs ALM-suite module (Codebeamer). The substrate does not change the object model.
- **Case authoring forms** — scripted steps (dominant) vs BDD/Gherkin vs exploratory/session charters vs automated-only records; several products support several forms side by side.
- **Posture** — manual-first with imported automation vs automation-orchestration-centric (enterprise pole).
- **Regulated-industry evidence depth** — audit trails, baselines, approvals, traceability matrices (shared with the §16 sibling; depth varies by customer, not by Type).
- **Deployment** — cloud SaaS vs server/on-premises (TestRail ships both).
- **Era-current layers** — AI test generation/agents, MCP access, natural-language authoring (Zephyr Rovo agent, qTest agentic creation, PractiTest SmartFox) — not definitional.

### L3 — Vendor-specific (Research Notes only)

- TestRail: default 5-status set with colors; closed runs immutable/archived; References field mechanics; TRCLI; JUnit-to-TestRail mapping; defect plugins with push templates; Enterprise parameterization/datasets.
- PractiTest: Test Instance concept; documented run-status computation algorithm; FireCracker/xBot; PTQL; Fast Run; enforce run order; test set permutations; time management timers.
- Zephyr: cycles/plans as Jira issue types; Rovo agent skills (coverage discovery, release risk); Standard/Advanced editions; Power BI.
- qTest: "60+ widgets" claim; universal agent; Explorer session capture; Tricentis platform bundling.
- Codebeamer: tracker-based item model (unverified in this pass); industry solution packaging.

## Vendor-specific Findings

See L3. None promoted to the canonical model. The run-status computation algorithm (PractiTest) and the exact default status sets (TestRail) are product-specific; the canonical claim is only "each case instance resolves to a recorded verdict; exact status vocabularies vary and are commonly customizable."

## Rejected Findings

- "Test management tools execute automated tests" — rejected as definitional. In the sampled management products, execution is manual (recorded) or imported; bundled execution engines are packaging. Execution-first products are the Test Automation Platform / E2E Testing Platform territory.
- "Requirement coverage requires a native requirements module" — rejected; TestRail's references-based coverage proves the invariant is the linkage + coverage computation, not the native object.
- "Test cases must be step-scripted" — rejected; exploratory/BDD forms in-sample carry the same record semantics (what to verify + basis for judgment) without predefined steps.
- "Defects live inside the test management tool" — rejected; TestRail and Zephyr both treat the defect record as external (issue tracker/Jira), linked from results. PractiTest's native Issues module is bundling.

## Boundary Findings

1. **vs Product Test Management (§16, processed) — JOINT REVIEW DISCHARGED from this side.** Keep-both RATIFIED as sibling domain instances of one test-management family (LIMS/industrial-lab precedent), exactly as the §16 pass recommended. The two leaves share the generic test-management shape (test definitions, runs, verdicts, plans — parallel L0s confirmed: this pass's test case of record / run with verdicts / managed testing effort mirrors §16's test of record / execution record / managed testing effort). The seam is **subject + ecosystem of judgment**: §16 verifies engineered products (hardware + embedded software) against product requirements, with design-review/regulatory sign-off as the deliverable; §12 manages the software application's build/release testing cycle, with CI/automation frameworks as the execution ecosystem. The market sells one capability across both worlds (Codebeamer serves software and product programs; Jama/Polarion per the §16 pass), so the boundary is a center-of-gravity seam, not an exclusive-capability wall. Removal tests hold both directions: strip the product/engineering-program subject (requirements-anchored V&V, regulatory evidence) and keep the software build/release cycle → this Type; strip the software build/release cycle and keep requirements-anchored product verification → §16.
2. **vs End-to-end Testing Platform (§12, processed) — DISCHARGES that pass's pre-hung seam.** Keep-both RATIFIED on the asset seam exactly as that pass framed it: the E2E platform's asset is the **executable test it itself runs** (drives the assembled application, produces verdicts from its own execution); test management's asset is the **managed record** (cases, runs, verdicts, coverage) — execution is manual-recorded or delegated/imported. Vendors bundle both (Katalon True Platform per the E2E pass; Tricentis qTest+Tosca; SmartBear Zephyr's bundled automation) — bundling does not merge the Types.
3. **vs Test Automation Platform (§12, unprocessed) — forward flag.** Expected seam: automation platforms author/execute automated tests (the executable test is the asset); test management plans, tracks, records, and proves (the managed record is the asset); results import is the observed bridge. The market bundles heavily (Katalon True Platform; Tricentis; SmartBear). Joint review recommended at that pass; candidate outcomes: keep-both with the record-vs-executable seam, or umbrella treatment for the automation leaf.
4. **vs Issue Tracker / Bug Tracking System (§12, processed)** — the defect record and its lifecycle belong to the issue tracker; test management links defects to runs/results and surfaces their status but does not own defect workflow. TestRail's own integration model (link/push/hover to external trackers) and Zephyr's Jira-native defects confirm the seam. Note the substrate nuance: in Jira-native products the test case is hosted as an issue type, but its identity remains a verification record, not a delivery work item — hosting inside an issue tracker does not dissolve the Type.
5. **vs Requirements Management Platform (§12, processed; alias of engineering-requirements-management)** — the requirement record, its structure, and its traceability machinery are the requirements Type's center; test management consumes requirements as coverage targets. TestRail holds requirements only as external references; PractiTest/Codebeamer bundle requirements modules (packaging). Consistent with the requirements pass's own traceability seam (test cases as downstream links).
6. **vs Continuous Integration Platform (§12, processed)** — CI runs automated validation automatically on change events; test management plans and records the testing effort and ingests CI/automation results. CI attachment is a common integration, not the center.
7. **vs Engineering Project Management Platform (§12, processed)** — delivery work items (features/stories/bugs with workflow states toward release) vs verification records (cases/runs/verdicts toward coverage evidence). Different unit of record and different loop.
8. **vs Unit/Integration Test Runner (§12, unprocessed)** — expected seam: runners execute isolated component tests in the build; test management holds the managed record. Forward flag only; no dedicated research in this pass.
9. **vs Laboratory Information Management System (§22, processed)** — samples/lots vs software builds; different subject and judgment ecosystem; no overlap observed in-sample.

## Historical / Market-Sample Check (§24)

- Paper-era practice: a test-case binder (steps + expected results), a test plan per release, execution logs with pass/fail initials, defect reports cross-referenced — satisfies all three L0 structures with no software, no Jira, no CI, no automation import. The definition does not over-fit the modern stack.
- 2000s-generation tools (HP Quality Center/TestDirector lineage): test cases, test sets/runs, defects, requirement linkage — satisfy the core without cloud/AI/CI-native machinery.
- Excel-based test tracking (cases in spreadsheets, run sheets with verdicts) is the no-application pole of the same practice — useful as the "remove the application" contrast, not a Type member.
- The step-scripted case is the dominant modern realization but not the timeless definition (exploratory charters, BDD scenarios in-sample; paper-era procedures without per-step scripts).

## Uncertainties

- qTest object-level mechanics unverified (docs login-walled); held at product-page strength. Its inclusion as the enterprise pole rests on Tier-2 positioning plus market-structure reasoning.
- Codebeamer test-management mechanics unverified in this pass (help-center section not located; wiki login-walled); used as Tier-2 confirmation of the ALM-pole pattern, consistent with the §16 pass's own limitation.
- Xray (major Jira-native competitor) not sampled — docs require JS; Zephyr substituted as the Jira-native pole. If a future pass samples Xray, the Jira-embedded findings should be re-confirmed.
- Whether any management product executes automated tests itself as a first-class center (rather than bundled capability) could not be fully settled; observed bundling (Zephyr Advanced, xBot, qTest orchestration) treated as packaging per the anti-overfitting rule.
- Exact status vocabularies vary and are commonly customizable; no universal status set is claimed.

## Final Synthesis

Software Test Management is the software team's system of record for its testing effort. Its defining core is three jointly-held structures: the **test case of record** (a persistent identified re-runnable verification definition — what to do and the basis for judgment — held in an organized library), the **test run with recorded verdicts** (a planned execution instantiating selected cases against a specific build/release/configuration, tracking each case instance to a recorded verdict with context), and the **managed testing effort** (runs organized under plans/milestones, execution assigned, progress tracked, status and coverage aggregated and reported for release decisions). Around that core, mature products add requirement linkage with coverage views, a defect-linkage loop, automation results import, assignment/coordination machinery, configurations and parameterization, reports and dashboards, case versioning/approvals, and reuse tooling. The market realizes the Type as standalone dedicated tools (TestRail, PractiTest), issue-tracker-embedded apps (Zephyr in Jira), enterprise quality-platform modules (qTest), and ALM-suite modules (Codebeamer). It is distinct from the execution-first testing Types (E2E platform, test automation platform, unit/integration runner — executable test vs managed record), from the issue tracker (defect record ownership), from requirements management (requirement record ownership), from CI (change-triggered automated runs), and from its §16 sibling Product Test Management (same family, product/engineering-program subject vs software build/release subject — joint review discharged, keep-both ratified).
