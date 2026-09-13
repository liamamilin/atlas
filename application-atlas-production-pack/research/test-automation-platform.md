# Research Notes — Test Automation Platform

## Research Goal

Establish what "Test Automation Platform" is as an Application Type in directory §12 (Software Development & Product Engineering): what the central object of work is, how tests are authored, executed, and maintained, what execution/orchestration machinery exists, and where the Type's boundaries lie against neighboring Types — Software Test Management, End-to-end Testing Platform, Unit / Integration Test Runner (all §12), Device Testing Platform, Browser Compatibility Testing Platform, Continuous Integration Platform, API Development Workbench, Desktop Automation Application (§12), Robotic Process Automation Platform (§10), and the §13 evaluation Types.

Special attention: this leaf carries accumulated forward flags from at least five prior passes (software-test-management, end-to-end-testing-platform, device-testing-platform, browser-compatibility-testing-platform, product-test-management). Expected candidate outcomes were (a) keep-both with a record-vs-executable seam against Software Test Management, and (b) umbrella treatment relative to the layer-scoped testing siblings, per the E2E pass's taxonomy note. This pass discharges those flags with fresh evidence.

## Initial Boundary

Temporary hypothesis before research:

- Core use: authoring and executing automated software tests — software asserts the application's behavior instead of a person.
- Primary users: test automation engineers / SDETs, QA engineers, developers; at the no-code pole also manual testers and business analysts.
- Nearest neighbors: End-to-end Testing Platform (heaviest overlap — the E2E pass itself sampled Katalon and TestComplete), Software Test Management (record layer), Unit / Integration Test Runner (code-layer member of the same family), Device / Browser Compatibility platforms (environment providers), CI (pipeline runner of tests).
- Known unknowns: whether "multi-surface" is definitional or merely dominant; whether the management/orchestration layer is part of the Type or packaging; whether open-source frameworks fit the same Type as commercial suites; how to weight the maintenance loop (repositories, self-healing, model-based update).

## Research Questions

1. What is the central asset — how is an automated test defined, stored, organized, reused?
2. How are tests authored across products (record/playback, visual no-code, keyword, model-based, script), and what is shared beneath the philosophies?
3. How is the application's UI addressed — locators, object repositories, test objects, models — and how is change absorbed (maintenance loop)?
4. How does execution happen — local, agents, vendor clouds, external grids, CI, schedules — and what does a run produce?
5. What bridges exist — CI, issue trackers, test management (the results-import bridge flagged by the test-management pass)?
6. Who uses these products; does the user set differ across authoring philosophies?
7. What is the seam against: E2E Testing Platform, Unit/Integration Test Runner, Software Test Management, device/browser environment platforms, desktop-automation/RPA, evaluation Types?
8. Would older-generation products (WinRunner/QTP/SilkTest-class GUI testers, capture-replay, open-source keyword frameworks) satisfy the definition — is the core free of current-era implementation?

## Representative Products

Selected for market representation + documentation completeness + different authoring philosophies + different customer layers:

- **Katalon Studio / True Platform** — commercial hybrid IDE (record/spy + manual/script dual editors), multi-surface (web, API, mobile, desktop), platform layer (management analytics, TestCloud execution). Philosophy: record + keyword + script hybrid.
- **TestComplete** (SmartBear) — long-lived commercial testing environment for desktop, web, mobile, enterprise packaged apps; record + script; headless runner. Philosophy: record + script, object-aware.
- **Ranorex Studio** — commercial desktop-centric studio extended to web/mobile; repository + recording architecture; C# underneath. Philosophy: record + repository + code.
- **Leapwork** — no-code visual test automation platform; flows of building blocks; desktop/web/mobile/Citrix/mainframe; agents, cloud, external grids. Philosophy: no-code visual flows.
- **Tricentis Tosca** — enterprise model-based, codeless automation across a very wide technology set incl. SAP/Oracle/Salesforce; elastic cloud execution; sold beside qTest (separate test-management product). Philosophy: model-based, codeless.

Structural/historical check sample: **Robot Framework** (open-source keyword-driven automation framework for test automation and RPA), plus recognition of the QTP/WinRunner/SilkTest generation and capture-replay lineage.

## Sources

Fetched 2026-09-09:

- Katalon Docs — About Katalon Studio: https://docs.katalon.com/katalon-studio/about-katalon-studio
- Katalon Docs — Introduction to test maintenance: https://docs.katalon.com/katalon-studio/maintain-tests/introduction-to-test-maintenance
- SmartBear — TestComplete 15 Documentation hub: https://support.smartbear.com/testcomplete/docs/
- Ranorex Help Center — Ranorize Yourself Guide: https://support.ranorex.com/hc/en-us/articles/37993176545297-Ranorize-yourself-guide
- Ranorex Help Center — Repository Basics: https://support.ranorex.com/hc/en-us/articles/38080283293201-Repository-Basics
- Ranorex Help Center hub: https://www.ranorex.com/help/latest/
- Leapwork Docs — What is Leapwork?: https://docs.leapwork.com/leapwork-flow/latest/what-is-leapwork
- Leapwork Docs — Introducing Leapwork Flow: https://docs.leapwork.com/leapwork-flow/latest/working-with-leapwork/introducing-leapwork-flow
- Tricentis — Tosca product page (positioning-tier): https://www.tricentis.com/products/automate-continuous-testing-tosca
- Robot Framework — homepage: https://robotframework.org/

Source-access limitations:

- **Tricentis Tosca**: documentation.tricentis.com redirected to docs.tricentis.com, which twice returned unusable/empty content; the docs domain was abandoned after two failures. Tosca observations rest on the vendor product page (positioning/capability claims) at reduced strength; no Tosca-specific mechanics are asserted.
- TestComplete evidence is limited to what the docs hub names directly (structure-level, not deep mechanics).
- The E2E pass (2026-09-08) previously fetched Katalon About, TestComplete docs root, and mabl; its record is imported as corroborating evidence where cited.

## Product Observations

### Katalon Studio / True Platform (Layer A, vendor docs)

- Self-positioning: "an automated testing IDE built upon the Selenium framework ... create and execute tests across diverse applications."
- Multi-surface in one project: "Combine multiple application types (Web UI, API, Mobile & Desktop) in one project and execution flow."
- Authoring: Recorder and Spy utilities ("create tests by simply interacting with your application"); "interchangeable interfaces between manual and script editors" — one test case, two views; built-in + reusable custom keywords; BDD (Cucumber) integration; data-driven testing.
- Element addressing: "Test objects" as a first-class artifact (creating reliable test objects; refactoring; unused-object insight).
- Maintenance machinery: self-healing (broken locators repaired at execution), Smart Wait, Time Capsule (snapshot of the AUT as it was when a test failed on locator misses — repair test objects against historical state), failure-handling settings (continue vs stop on error). Docs define maintenance: "fixing tests so they stay up to date with code changes."
- Organization: test cases grouped into test suites and test suite collections; test projects as container; shared artifacts.
- Execution: local IDE runs; Katalon Runtime Engine (KRE) for CLI/CI/CD; Test Execution Cloud (TestCloud) for cross-browser/device runs; scheduling at the platform layer.
- Results/bridges: test reports (execution logs), platform analytics, notifications (email/Slack/Teams); bug submission to Jira; integrations hub.
- AI-era: AI assistant explaining snippets and generating code from prompts; TrueTest generating test cases from real user session recordings (adjacent surface).

### TestComplete (SmartBear) (Layer A from docs hub structure; corroborated by E2E pass record)

- Self-positioning: "an automated testing environment for a wide range of desktop, web and mobile application types and technologies" (plus broad language support list).
- Surfaces: Desktop / Web / Mobile sections + Enterprise Apps (Salesforce, Microsoft Dynamics 365, SAP GUI, Oracle Forms/EBS) — packaged-application reach.
- Workflow sections: Create and Record Tests → Parameterizing Tests → Run Tests → Test Results (log); data-driven testing with built-in data generators; BDD tests.
- Execution/team: Jenkins integration, source-control support, teamwork; TestExecute — a separate headless execution engine; mobile via device cloud.

### Ranorex Studio (Layer A, help center)

- Getting-started arc: install → plan → create solution (Solution Wizard) → record first test → analyze recording (recorded actions and how they connect) → run and check report. Workspace organized around: Recorder, Test Suite, Actions, Repository, Test Validation, Reporting.
- Repository (the maintenance centerpiece): "stores representations of the user interface (UI) elements you interact with in your tests" (repository items), organized in a tree mirroring the AUT's UI structure (app folders → rooted folders → items); each item carries a RanoreXPath that "uniquely identifies the corresponding UI element in your application under test (AUT)"; recordings and code modules reference repository items; repositories are files (.rxrep + C# representation + .rximg); multiple/embedded repositories; deleting a repository in use warns that linked actions break.
- Integrations: Selenium WebDriver, cross-browser testing, TestRail (test management) integration; Web & Mobile testing categories; API testing present.

### Leapwork (Layer A, docs)

- Self-positioning: "a no-code test automation platform that helps teams build and run end-to-end automation using a visual, flow-based approach instead of scripting"; flows are "reusable" and built "by connecting building blocks that perform actions and validations."
- Authoring: drag-and-connect building blocks (click element, start application, extract data...); Smart Recorder (desktop + web), Smart Mobile Recorder (native mobile), Fusion Recorders (D365, Salesforce); Strategy Editor (element-targeting strategy); sub-flows for reuse; projects.
- Execution: "Execute test cases instantly or as part of structured test suites"; remote execution via Leapwork Agents, Leapwork Cloud, or external providers (Selenium Grid, BrowserStack, Sauce Labs, LambdaTest); debugging via execution logs and video recordings (video recorded for all runs).
- Orchestration: Run Lists ("create and manage test plans by organizing test cases into structured run lists"); scheduling by time, manual trigger, or REST API; workflow management; teams/roles/permissions; shared automation assets.
- Results/reporting: real-time results, in-depth reports, dashboards (success/coverage), execution logs, video.
- Bridges: Azure DevOps Test Plans integration, JIRA, CI/CD pipelines, REST APIs.
- Automatable surfaces: desktop, web, mobile custom apps; packaged enterprise software; Citrix/Remote Desktop/terminal/mainframe environments; "cross-technology automation — a single automation flow that interacts across different applications and environments."

### Tricentis Tosca (positioning-tier; docs unreachable — reduced strength)

- "Codeless, AI-powered test automation"; "model-based testing, agentic AI, and unattended parallel execution on the cloud."
- Model-based decoupling: "separates the test model from the underlying application, so when the system changes, updates are quickly pushed to hundreds or thousands of test cases at once"; "a fix applied once propagates everywhere" (shared modules).
- Breadth: "Cover enterprise technologies, from SAP and Oracle to web and APIs"; "200+ technologies covered natively"; API simulation (virtual services standing in for unavailable dependencies; HTTP + async protocols).
- Execution: Elastic Execution Grid (E2G) auto-provisioning cloud and on-prem agents; parallel runs; authoring from any browser (SaaS).
- Democratization: "Enable analysts, manual testers, and business users to create and maintain test automation without coding skills."
- Vendor-drawn seam: Tricentis markets qTest separately as "Enterprise test management" while Tosca is "Test Automation" — management and automation are separate products in one vendor's own catalog.

### Robot Framework (Layer A, homepage — structural/historical check)

- "An open source automation framework for test automation and robotic process automation (RPA)"; "human-friendly and versatile syntax uses keywords and supports extending through libraries"; hundreds of third-party libraries (web via Selenium/Playwright-based libraries, mobile via Appium, Windows GUI via AutoIt, even Kafka); integrations with other tools; no licensing fees.
- Confirms the Type's abstract core is satisfiable without a commercial product, hosted cloud, or management layer: test assets as keyword-driven files, executed by a runner, producing logs/reports.

## Cross-product Comparison

| Structure | Katalon | TestComplete | Ranorex | Leapwork | Tosca | Robot Framework |
|---|---|---|---|---|---|---|
| Persistent re-runnable test asset | test case (manual/script dual view) | test (recorded/scripted) | recording/module actions | flow (building blocks) | model-derived test cases | keyword test files |
| Test organization | suites + suite collections, projects | projects, test items | solutions + test suites | projects + run lists | test cases in repository structure | files/suites (CLI-selectable) |
| Element addressing separated from test logic | test objects | object-aware (name mapping per E2E pass) | repository items + RanoreXPath | element targets + Strategy Editor | modules (model layer) | locators in library layer |
| Maintenance machinery | self-healing, Time Capsule, object refactor | parameterization, teamwork on assets | repository tree edit; linked-action impact | element fix-in-recorder; sub-flow reuse | model update propagates to many tests | keyword/library reuse |
| Authoring philosophies | record + keyword + script | record + script | record + code | no-code visual | codeless model-based | keyword text files |
| Surfaces | web, API, mobile, desktop | desktop, web, mobile, enterprise apps | desktop, web, mobile | desktop, web, mobile, Citrix/mainframe | SAP/Oracle/Salesforce/web/API/etc. | via libraries: web, mobile, desktop, protocols |
| Execution venues | local, KRE/CI, TestCloud | local, TestExecute, Jenkins, device cloud | local, CI | local, agents, own cloud, external grids | local/cloud agents (E2G), parallel | CLI runner, CI |
| Run output | execution logs, reports, analytics | results log | reports | logs, video of every run, dashboards | parallel run results (positioning) | log.html/report.html |
| Unattended/scheduled | yes (platform layer, KRE) | yes (TestExecute/Jenkins) | yes (CI) | yes (schedules, triggers, API) | yes (unattended parallel) | yes (CI/cron) |
| Test-management bridge | platform analytics + Jira | (SmartBear suite; Zephyr sibling) | TestRail integration | ADO Test Plans, JIRA | qTest (separate product) | community/CI-side |
| Data-driven | yes | yes (built-in generators) | — (not fetched) | data-driven building blocks | (positioning) | library/template-level |
| BDD support | yes | yes | — | — | — | (Gherkin via ecosystem) |

Reading: every sampled realization holds a persistent, organized, re-runnable test asset; executes it automatically against the software under test; separates element addressing from test logic in some form; and surrounds execution with evidence (logs at minimum, video/screenshots at the visual pole) and bridges (CI at minimum, test-management/issue-tracker integration commonly). Authoring philosophy, surface breadth, execution venue, and management depth vary widely — variant axes, not defining structure.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The automated test as the platform's central asset.** A persistent, named, re-runnable definition of stimulus + expected outcome, authored and edited inside the platform (by recording, visual composition, keyword/model building, or script), organized in suites/projects, and held as maintained capital that outlives any run. Remove → an automation library/driver substrate (no managed asset), or a test-management register (records, not executables).
2. **Automated execution producing verdicts with evidence.** The platform drives the run itself — locally, on dedicated agents, in vendor cloud, on external grids, or invoked by CI — without a human performing the steps, and produces per-test pass/fail results with failure evidence (logs, screenshots, video). Remove → an authoring/recording tool that never runs, or a runner with no held assets.
3. **Surface-spanning application reach in one authoring/execution model.** The asset addresses the application's user-facing surfaces — and commonly the API/service layer — with more than one surface/layer reachable in the same model and even the same test flow. Remove → the scope-disciplined family members (code-layer-only runner; single-loop E2E tool) or single-purpose point tools.

Jointly load-bearing: (1 alone) = an IDE/asset library nothing executes; (2 alone) = an execution service with no held tests; (3 alone) = generic scripting; (1+2 without 3) = a scoped family member; (1+3 without 2) = a test-design tool; (2+3 without 1) = ad-hoc scripting.

### L1 — Common Mature Structure

- Element addressing as a managed layer (repositories/test objects/modules/element targets) — the dominant mature pattern separating test logic from locators.
- Recorders/spies; reusable composition units (custom keywords, sub-flows, shared modules, reusable flows).
- Data-driven testing and parameterization; environment configuration.
- Unattended execution: schedules/triggers, parallel runs, headless runners, agents/cloud execution.
- Failure evidence beyond the log line: screenshots, video of runs, execution traces.
- Maintenance machinery: broken-locator repair, self-healing, snapshot-based repair aids, model/repository update propagation.
- CI integration (invoke runs from pipelines); notifications.
- Bridges outward: results/plans to test management, defects to issue trackers.
- Reporting/dashboards: run results, trends, coverage/success overviews.
- Team layer: shared projects, roles/permissions, source-control support.

### L2 — Variant / Optional Structure

- Authoring philosophy: code-first script vs record-and-playback vs keyword-driven vs visual no-code vs model-based vs AI-generated (all present in-sample; none definitional).
- Surface emphasis: web-centric; desktop-centric; mobile; cross-technology (Citrix/terminals/mainframe); enterprise packaged apps (SAP/Dynamics/Salesforce-class).
- Commercial suite vs open-source framework vs SaaS platform (Robot Framework pole proves commercial posture is NOT definitional).
- Bundled management/orchestration layer (platform analytics, test-ops) vs separate management product (qTest-class) vs none (framework pole).
- API testing depth: dedicated API test authoring vs API calls woven into flows; API simulation/service virtualization (enterprise pole).
- AI-era authoring (generation from natural language or session recordings, self-repair) — era-current, present but not defining.
- Deployment: installed IDE + local engine; server-managed agents; cloud SaaS.

### L3 — Vendor-specific (Research Notes only)

Katalon: Time Capsule, Smart Wait, KRE, TestCloud, TrueTest. Ranorex: RanoreXPath, .rxrep repository files, Ranorex Coach. Leapwork: building blocks, Fusion Recorders, Strategy Editor, Run Lists. Tosca: model-based decoupling, E2G. TestComplete: TestExecute headless engine, BitBar device cloud. Tricentis: qTest as separate management product.

## Rejected Findings

- "Test automation platforms are codeless/low-code" — REJECTED as definitional: code-first and hybrid authoring are equally present in-sample; authoring philosophy is the primary variant axis.
- "They execute in the vendor cloud" — REJECTED: local IDE + local engine poles (Ranorex/TestComplete desktop usage; Robot Framework CLI) satisfy the core; cloud execution is a variant posture.
- "They include test management (plans, runs, coverage records)" — REJECTED as definitional: Tricentis itself sells qTest separately from Tosca; the test-management pass recorded that execution-first products are this territory and management holds the record layer. Bundled analytics/orchestration is packaging.
- "They are QA-team tools, not developer tools" — REJECTED: code-first suites and open-source frameworks are developer-owned; user mix varies with authoring philosophy.
- "Object repositories are definitional" — REJECTED as a specific implementation: the invariant is element addressing separated from (or managed alongside) test logic; code-first locators-in-code realize the same concern differently.
- "Test generation by AI is part of the Type" — REJECTED: era-current capability, present in-sample but the pre-AI generation satisfies the core without it.
- "Multi-surface breadth means every product covers every surface" — REJECTED: breadth varies (web-centric to 200+-technology claims); the invariant is that the model is not confined to a single test layer, not uniform coverage.

## Boundary Findings

1. **vs End-to-end Testing Platform** — one product population, two directory leaves; seam = scope discipline. The E2E pass defined its Type as whole-application exercise through the real user interface (user-level journeys, pre-release verdicts) and itself recorded: "Test Automation Platform | umbrella sibling | market term with heavy overlap... E2E Testing Platform is the scope-disciplined member of that family." This pass ratifies from the umbrella side: the automation platform's center is the managed multi-surface test asset + execution + maintenance, not the journey scope; E2E members can be seen as the interface-journey-disciplined realization. Test: a product authoring/executing tests across surfaces and layers in one model → this Type; a product scoped to user-journey tests against the assembled app → E2E member. Keep-both.
2. **vs Unit / Integration Test Runner (unprocessed leaf)** — expected seam: runners execute code-level tests that live with the codebase, invoked by the build/test command; no managed platform asset, no recorder/repository machinery, single layer. The automation platform holds tests as managed platform-side assets spanning layers. Forward flag remains for that pass.
3. **vs Software Test Management** — record vs executable seam (ratifies that pass's forward flag): test management plans, tracks, records, and proves (cases, runs, verdicts, coverage); the automation platform authors and executes (the executable test is the asset). Bridge observed in both directions: Ranorex→TestRail integration, Leapwork→ADO Test Plans, Katalon→platform analytics + Jira; test-management products import automation results. Vendor-policed: Tricentis qTest vs Tosca.
4. **vs Device Testing Platform / Browser Compatibility Testing Platform** — environment provider vs authoring/execution (both passes recorded the same seam): those Types' artifact is the device/browser catalog; the automation platform's artifact is the test asset. Observed integration: Leapwork executes on BrowserStack/Sauce/LambdaTest/Selenium Grid; TestComplete mobile via device cloud; Katalon TestCloud. Remove the test asset → environment provider territory.
5. **vs Continuous Integration Platform** — CI runs tests on change events as one job among many (build, package, deploy); the automation platform is where tests are authored/maintained and from which runs are triggered/results produced. CI invokes the automation platform's runner (KRE, Jenkins→TestComplete). Remove test assets → CI.
6. **vs Desktop Automation Application / RPA Platform** — same GUI-driving machinery (record, target, replay), different job and artifact: doing the user's/organization's production work vs asserting expected behavior of software under test (both passes already drew the job seam; UiPath ships a separate test product line; Robot Framework itself spans test automation and RPA with the same syntax — job defines the Type, not mechanism).
7. **vs API Development Workbench** — collections with assertions run in CI drift toward API test automation; the workbench's tests are authored inline against requests (that pass's seam). In the automation platform, API tests are part of the managed suite beside UI tests, not requests-first tooling.
8. **vs Synthetic Monitoring** — same scripted-journey mechanics, different loop: production availability monitoring (ops-owned) vs pre-release correctness verdicts (dev/QA-owned, change-linked).
9. **vs LLM/Agent Evaluation Platforms** — deterministic pass/fail on deterministic systems vs graded, comparative, non-deterministic quality measurement (recorded by both §13 passes; the bridge is evaluation metrics converted into regression assertions).
10. **What this Type is NOT**: it is not the pipeline machinery (CI/CD), not the environment fleet (device/browser platforms), not the record layer (test management), not a user's personal automation (desktop automation), not production monitoring.

Boundary test distilled: remove the held, maintained, executable test asset → the product falls into a neighboring Type; remove the scope discipline → you are describing the umbrella that this leaf owns.

## Historical / Market-Sample Check

- 2000s GUI functional-test generation (WinRunner, QTP/UFT lineage, SilkTest, Rational Robot; TestComplete's own early generations): recorded/scripted test assets + object maps + suites + playback + result logs — satisfies L0 with no cloud, no AI, no management layer.
- 1990s capture-replay tools: authoring + execution + verdicts, minimal organization — satisfies the minimum core (asset + execution), weak on L1.
- Robot Framework (2005-, open source): keyword test files + runner + logs/reports, libraries spanning web/mobile/desktop/protocols — satisfies L0–L1 with no commercial platform at all.
- Conclusion: the definition is era-robust; current-era machinery (cloud grids, self-healing, AI authoring, dashboards) is L1/L2, not L0. The "platform" in the leaf name is realized from bare CLI framework to full SaaS suite — deployment posture is a variant axis, confirmed deliberately.

## Uncertainties

- Tosca's internal mechanics (module/repository structure, licensing of execution) unverifiable this pass — Tosca used only for positioning-level claims (multi-technology breadth, model-based maintenance claim, separate qTest).
- TestComplete deep mechanics (name mapping internals, distributed execution details) not re-fetched; held at docs-hub-structure strength; corroborated by the E2E pass's record.
- Whether a single-surface, journey-scoped product (web-only automated testing SaaS) should be counted in this Type or in the E2E member — market naming is inconsistent; documented as a gradient, not resolved.
- Unit / Integration Test Runner leaf unprocessed: its seam here is an expectation from the directory structure + family logic, not yet ratified from that side.
- Exact plan-tier boundaries of management/orchestration features (what ships free vs enterprise) not researched — deliberately excluded from the final document.

## Final Synthesis

A Test Automation Platform is the software team's system for authoring, executing, and maintaining automated tests as managed assets. Its defining core: (1) the automated test — a persistent, organized, re-runnable asset expressing actions and expected outcomes; (2) automated execution — the platform drives runs against the application under test without a human performing the steps, locally or on agents/cloud/grids/CI, producing per-test verdicts with failure evidence; (3) surface-spanning reach — one authoring/execution model addressing more than one application surface or test layer. Around this core, mature products add the maintenance loop (element addressing as a managed layer; repair machinery when the application changes), unattended orchestration (schedules, parallel runs), rich evidence (screenshots, video), and bridges (CI, issue trackers, test management). The market realizes the Type across authoring philosophies (script ↔ record ↔ keyword ↔ visual no-code ↔ model-based ↔ AI-generated) and postures (open-source framework ↔ installed IDE ↔ managed SaaS), with Tricentis's qTest/Tosca split and the test-management pass's results-import bridge confirming the record-vs-executable seam. The Type is the general, scope-free member of the automated-testing family whose layer-disciplined members (E2E Testing Platform; Unit/Integration Test Runner) are separate directory leaves; the Software Test Management leaf holds the record layer. This discharges the accumulated forward flags: keep-both with E2E (scope seam, umbrella-side ratification), keep-both with Software Test Management (executable-vs-record seam), environment-provider and job-based seams with the remaining neighbors.
