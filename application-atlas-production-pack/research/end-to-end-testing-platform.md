# Research Notes — End-to-end Testing Platform

## Research Goal

Understand, from real products, what an End-to-end (E2E) Testing Platform actually is: what objects it manages, how tests are authored and executed, what its run/result/debug surfaces are, and where its boundaries sit against neighboring testing Types (unit/integration runners, test management, browser/device platforms, synthetic monitoring, load testing).

## Initial Boundary

Initial hypothesis: an E2E Testing Platform lets teams author and run automated tests that drive the **whole assembled application** through its real user-facing interface (browser UI, mobile app UI, desktop UI — commonly supplemented by API calls), assert expected behavior, and report pass/fail results with failure evidence.

Neighboring Types to keep distinct:
- Unit / Integration Test Runner — code-level tests on isolated components
- Software Test Management — managed test-case/run/defect records, largely manual-execution oriented
- Test Automation Platform — umbrella term, heavy product overlap (taxonomy note below)
- Device Testing Platform / Browser Compatibility Testing Platform — grids and environment access as the product
- Synthetic Monitoring — same journey mechanics, production/monitoring purpose
- Load Testing Platform — concurrency/volume and performance, not single-journey correctness
- Browser automation libraries (Selenium WebDriver) — substrate, not a platform

## Research Questions

1. What is the core object model? (test/spec/case, step, assertion, suite, run, result, artifact, locator, environment, project)
2. How are tests authored? (code-first, record/playback, keyword/low-code, AI-generated)
3. What is executed, against what, and where? (browsers, mobile, desktop; local, CI, cloud)
4. How do results, reporting, and debugging work?
5. What rules and recurring mechanics govern test behavior? (waiting, isolation, retries/flake, environment configuration)
6. How does the platform attach to the delivery loop (CI/CD, PR feedback, notifications, issue trackers)?
7. Where are the boundaries against the neighboring Types?
8. Who uses it, and in what loop?

## Representative Products

| Product | Shape | Why selected |
|---|---|---|
| Playwright (Microsoft) | Open-source code-first framework + bundled runner | dominant modern web E2E framework; deep docs; code-first pole |
| Cypress (Cypress.io) | Open-source app + paid cloud | different architecture (in-browser run loop); app+cloud split; developer-loop pole |
| Katalon Studio / True Platform | Commercial hybrid IDE (record/spy + manual/script editors) built on Selenium | low-code+code pole; multi-surface (web/mobile/API/desktop); platform+management bundling |
| TestComplete (SmartBear) | Commercial testing environment | enterprise/legacy pole; desktop+web+mobile; record+script; long lineage (QTP-class) |
| mabl | Cloud-native SaaS testing platform | SaaS/managed pole; cloud execution, artifacts, migrations; different customer tier |

Boundary anchor (not counted as a Type sample): **Selenium** — browser automation project (WebDriver + Grid + IDE), the substrate several sampled products build on.

Selection covers: code-first vs record/low-code vs SaaS-managed philosophies; OSS/free vs commercial/enterprise tiers; web-only vs web+desktop+mobile scopes.

## Sources

- Playwright — Introduction/Installation: https://playwright.dev/docs/intro (fetched 2026-09-08)
- Playwright — Writing tests: https://playwright.dev/docs/writing-tests (fetched 2026-09-08)
- Cypress — Why Cypress: https://docs.cypress.io/app/get-started/why-cypress (fetched 2026-09-08)
- Katalon — Docs root: https://docs.katalon.com/ (fetched 2026-09-08)
- Katalon — About Katalon Studio: https://docs.katalon.com/katalon-studio/about-katalon-studio (fetched 2026-09-08)
- TestComplete 15 Documentation hub: https://support.smartbear.com/testcomplete/docs/ (fetched 2026-09-08)
- mabl — docs root (AI-agent mirror): https://docs.mabl.com/ (fetched 2026-09-08)
- mabl — mabl CLI overview: https://docs.mabl.com/docs/mabl-cli/mabl-cli-overview.html (fetched 2026-09-08)
- Selenium — Documentation: https://www.selenium.dev/documentation/ (fetched 2026-09-08)

### Source-access Limitations

- mabl primary help center (help.mabl.com) timed out; evidence limited to the AI-agent docs mirror (root, llms.txt index, CLI overview). mabl-specific claims kept product-specific and weak.
- TestComplete evidence is the documentation hub map (section structure), not deep pages; claims kept at doc-map level (sections, capabilities named by the vendor).
- Katalon True Platform sub-pages (TestOps/TestCloud/TrueTest) not fetched; platform claims drawn from docs navigation + Studio about page.
- Selenium used only as boundary substrate; not deep-researched.

## Product Observations

### Playwright (evidence layer A)

Self-definition: "Playwright Test is an end-to-end test framework for modern web apps. It bundles test runner, assertions, isolation, parallelization and rich tooling." Supports Chromium, WebKit, Firefox on Windows/Linux/macOS, locally or in CI, headless or headed, with native mobile emulation.

Core authoring model (Writing tests): "tests … perform actions and assert the state against expectations."
- **Locators** — "represent a way to find element(s) on the page at any moment" (re-evaluated, not stale references)
- **Auto-waiting / actionability** — waits for actionability checks before each action; "You don't need to add manual waits"
- **Assertions** — `expect` with async matchers that "wait until the expected condition is met" (e.g. toHaveTitle, toBeVisible, toContainText), plus generic sync matchers
- **Test isolation** — fixtures; each test gets a fresh Browser Context ("equivalent to a brand new browser profile")
- **Hooks/groups** — test.describe, beforeEach/afterEach, beforeAll/afterAll

Run & config: playwright.config.ts centralizes "target browsers, timeouts, retries, projects, reporters". Projects = same tests across browser configurations; parallelism; sharding; parameterization; web server (starts the app under test).

Results & debugging: HTML Reporter dashboard "filterable by the browser, passed, failed, skipped, flaky"; per-test errors, attachments, steps; UI Mode (watch mode, live step view, time travel); trace viewer; screenshots; videos.

Authoring aids: Codegen (test generator — record interactions → code), VS Code extension; also API testing, mock APIs, visual comparisons, aria snapshot testing, accessibility testing, component testing, test agents/MCP (AI-era).

### Cypress (evidence layer A)

Self-definition: "Cypress is a quality platform for teams shipping modern web applications. We bring together end-to-end testing, component testing, accessibility checks, and a clear view of test coverage into a connected workflow that runs locally and in CI."

E2E definition: "A typical E2E test visits the application in a browser and performs actions via the UI just like a real user would. They catch the failures your users would actually see, which is what makes them so valuable in the moments before code ships."

Products: Cypress App (free, open source, locally installed app "for writing and running tests"); Cypress Cloud (paid: "recording tests, surfacing test results, and providing test analytics"); UI Coverage; Accessibility.

Architecture: "executed in the same run loop as your application" — no Selenium/WebDriver; Node server process behind; native access to window/document/DOM/app objects.

Mechanics: automatic waiting; retry-ability; test isolation; cy.session() (authenticate once, restore saved session per test); network interception/stubs/spies/clocks; Time Travel snapshots + Command Log; cross-browser (Firefox and Chrome-family) locally and in CI; test retries; screenshots and videos; reporters.

Cloud: Smart Orchestration (parallelization, spec prioritization, auto cancellation), Test Replay ("replay the test exactly as it executed during the run"), flake detection/management, Branch Review (pre-merge test signal per PR), Test Analytics; integrations: GitHub/GitLab/Bitbucket, Slack, Jira, Microsoft Teams, Cloud MCP.

Authoring aids: Cypress Studio records interactions to generate/extend E2E tests; Studio AI suggests assertions; cy.prompt (AI test generation). Also: API testing via cy.request; component testing; accessibility.

### Katalon Studio / True Platform (evidence layer A, platform layer partial)

Self-definition: "Katalon Studio is an automated testing IDE built upon the Selenium framework" — "create and execute tests across diverse applications". Studio = "test automation IDE across web, mobile, API, and desktop testing". True Platform = agentic AI quality platform spanning Studio (automation), test management (TestOps), Test Execution Cloud (TestCloud), TrueTest (production insights).

Authoring: "Create tests by simply interacting with your application using Recorder and Spy. Then, edit your test case using interchangeable interfaces between manual and script editors." Built-in keywords + reusable custom keywords (keyword-driven); BDD/Cucumber; data-driven testing.

Objects: manage test projects; test cases; grouping into "test suites and test suite collections"; test objects (locator-based element repository); test artifacts.

Maintenance: self-healing (auto-fix broken locators), Smart Wait function, Time Capsule ("fix broken web test objects").

Execution: Studio (local); Katalon Runtime Engine (KRE) — CLI for CI/CD pipelines; Test Execution Cloud (TestCloud) — "Cross-browser & device testing in the cloud with minimal setup".

Reporting/integration: test reports / execution log; Jira bug submission; email/Slack/Teams notifications; platform analytics. AI: AI Assistant in Studio (explains code, generates code from natural language); TrueTest generates tests from real user session recordings; MCP servers.

### TestComplete (evidence layer A, doc-map level)

Self-definition: "TestComplete is an automated testing environment for a wide range of desktop, web and mobile application types and technologies." Language support: .NET, C#, VB.NET, C++, Java, Delphi, C++Builder, etc.

Documentation map (vendor-named sections):
- Desktop Testing / Web Testing / Mobile Testing (device cloud via BitBar)
- Enterprise Apps: Salesforce, Microsoft Dynamics 365, SAP GUI, Oracle Forms/EBS
- Create and Record Tests; Parameterizing Tests; Run Tests; **Test Results** (log)
- Data-Driven Testing (concepts + built-in data generators)
- BDD Tests; Simulating User Actions; Working With Controls (app objects)
- QA Process: Teamwork; Source Control Support; Jenkins Integration; CucumberStudio Integration; TestExecute (separate runner)

### mabl (evidence layer A-partial — mirror docs only)

Cloud SaaS testing platform. From the CLI/docs-mirror surfaces:
- Workspace components: workspaces, applications, environments, tests, DataTables, branches
- Running tests from CLI for quick feedback; "Integrating testing as part of your CI/CD build process"; CI Runner
- Test artifacts: screenshots, HAR files, console logs
- Imports: migrate tests from Playwright or Selenium (incl. Selenium Java Agent); exports: Playwright format among others
- Authoring from AI coding agents ("Author mabl tests from your AI coding agent"); mabl MCP: "your AI client can author and execute tests, query results, analyze…"
- Link Agent (for testing local/private environments — named in workspace component commands)
- Mobile build files managed via CLI (mobile testing support)

### Selenium (evidence layer A — boundary anchor)

"Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers." Components: WebDriver ("an interface to write instruction sets that can be run interchangeably in many browsers", implementations of the W3C WebDriver specification), Grid ("a distribution server for scaling browser allocation" / "run tests in parallel across multiple machines"), Selenium IDE ("a browser extension that records and plays back a user's actions"), Selenium Manager. Waits/Expected Conditions documented as explicit user-built strategies; test practices include page object models, test independency, fresh browser per test, avoiding shared state; performance testing listed under "Discouraged behaviors". Project sponsors include cloud grid vendors (BrowserStack, Sauce Labs, LambdaTest-class).

Interpretation for boundary: Selenium provides element-level automation primitives but no runner, no assertion library, no results/reporting — those come from the surrounding platform/framework. Katalon explicitly describes itself as "built upon the Selenium framework", confirming the substrate→platform relation.

## Cross-product Comparison

| Dimension | Playwright | Cypress | Katalon Studio | TestComplete | mabl |
|---|---|---|---|---|---|
| Product shape | OSS code-first framework+runner | OSS app + paid cloud | Commercial hybrid IDE + platform | Commercial IDE/environment | Cloud SaaS platform |
| Primary authoring | code (TS/JS/Py/Java/.NET); Codegen records → code | code (JS); Studio records; AI prompts | Recorder/Spy + manual(keyword)↔script editors; BDD | record + script (many languages) | AI-agent authoring; imports from Playwright/Selenium |
| Test asset unit | spec file / test | spec / test | test case → suites → suite collections | test items in project | test (+ plans, DataTables, branches) |
| Element addressing | Locators (re-evaluated) | commands + selectors | test objects (locator repository) | app objects / controls | (not surfaced in fetched docs) |
| Waiting strategy | built-in actionability auto-wait | built-in auto-wait + retry-ability | Smart Wait | (not surfaced) | (not surfaced) |
| Assertions | expect matchers (retrying) | should/chai + retry-ability | keywords / verification | checkpoints (doc-map) | step assertions (partial) |
| Isolation / state | fresh Browser Context per test | test isolation; cy.session caching | profiles/environments | parameterizing, data-driven | environments, DataTables, branches |
| Execution venues | local CLI (headless/headed); CI; sharding | local App; CI; Cloud orchestration | Studio; KRE (CLI); TestCloud (hosted browsers/devices) | IDE; TestExecute; Jenkins; BitBar device cloud | cloud runs; CLI triggers; CI Runner |
| Results | HTML report (filterable by browser, passed/failed/skipped/flaky) | Command Log; Cloud analytics | execution log/reports | Test Results log | run artifacts (screenshots, HAR, console logs) |
| Debug artifacts | trace viewer, videos, screenshots, UI mode time travel | Time Travel snapshots, Test Replay, screenshots/videos | Time Capsule; screenshots | screenshots in log (implied by section naming) | screenshots, HAR, console logs |
| Flake handling | retries; flaky status | retries; flake detection/management | self-healing locators | (not surfaced) | (not surfaced) |
| CI/CD attach | generated GitHub Actions workflow; CI docs | CI guides per system; Cloud PR integration (Branch Review) | KRE; Jenkins-class | Jenkins integration; TestExecute | CLI in pipeline; CI Runner |
| Notifications/trackers | (via reporters/CI) | Slack, Jira, Teams, GitHub/GitLab/Bitbucket | Jira, Slack, Teams, email | Jira-ecosystem (Zephyr), CucumberStudio | Atlassian-family via MCP (partial) |
| Surfaces beyond web UI | mobile emulation; API testing; component testing | API requests; component testing | API + mobile + desktop in one project | desktop + mobile + enterprise apps (SAP/Salesforce/Oracle) | web + mobile (build files) |
| Authoring aids | Codegen, VS Code extension, test agents/MCP | Studio AI, cy.prompt, Cloud MCP | Recorder/Spy, AI Assistant, TrueTest (session-replay generation), MCP | record tooling | AI-agent authoring, MCP |
| Cloud/management layer | (ecosystem, e.g. cloud grids) | Cypress Cloud (replay, flake, coverage, analytics) | True Platform (TestOps management, TestCloud, analytics) | BitBar; teamwork/source control | native cloud workspace |

### What repeats across the sample (candidate common mature structure)

1. Tests authored as persistent, named, re-runnable assets expressing user-level journeys over the real application. (5/5, different authoring modalities)
2. Execution against the real assembled application — visited/launched like a user would reach it. (5/5; Cypress states it verbatim)
3. Per-test pass/fail verdicts with a results surface. (5/5)
4. Failure evidence beyond the verdict — screenshots/videos/traces/logs/HAR/snapshots. (5/5, varied artifacts)
5. Element addressing + interaction machinery (locators/selectors/keywords/objects). (4/5 surfaced; mabl not surfaced in fetched docs)
6. Waiting/stability machinery as a first-class concern (auto-wait, retry-ability, Smart Wait; retries; self-healing). (4/5 surfaced)
7. Test isolation / controlled state (fresh context, session caching, environments/profiles, data-driven inputs). (5/5 in some form)
8. CI/CD attachment as the standard second venue for runs. (5/5)
9. Record/generate authoring aids on top of the primary authoring mode. (5/5 — codegen, Studio, Recorder/Spy, record+script, AI agent authoring)
10. Multi-browser/multi-surface matrix (browsers; mobile; desktop per product scope). (5/5 within each product's scope)
11. Parallelization/scaling runs. (Playwright parallelism/sharding, Cypress Cloud orchestration, Katalon suite collections+KRE, Selenium Grid as substrate, TestExecute; mabl cloud-native)

### Defining vs common (first pass)

- Defining (remove → different Type): whole-app subject; persistent re-runnable journey test; execution with verdicts + diagnosable failure evidence.
- Common but not definitional: rich media artifacts (trace/video/HAR), flake dashboards/analytics, recorders, parallelization, CI recipes, notifications, issue-tracker sync.
- Variant: authoring philosophy (code vs record/low-code vs AI), surfaces covered (web/desktop/mobile/API), cloud vs local execution, management/coverage add-ons, self-healing/AI.

## Canonical Model (synthesis target)

Three jointly-held structures:

1. **The application-under-test exercised as a whole** — tests drive the assembled application through its real user-facing interface in a real (test) environment: browser UI canonical today, plus native mobile/desktop UI and API calls within journeys depending on product scope. Not component-isolated, not code-level.
2. **The automated test scenario of record** — a persistent, named, re-runnable test asset expressing a user-level journey: navigation, interactions with the interface (element addressing), and expected outcomes (assertions/checkpoints). Organized into groups/suites/projects; configured per environment.
3. **Automated execution with per-test verdicts and failure evidence** — the platform runs the tests against the application (locally, in CI, or on hosted browsers/devices), records pass/fail (plus intermediate states such as skipped/flaky), and surfaces failure context (errors, assertion results, commonly screenshots/traces/videos/logs) sufficient to diagnose and fix.

Jointly-held is load-bearing:
- 1+2 without 3 → an automation library/recorder (Selenium WebDriver scripts; a recorder utility) — no managed run results.
- 2+3 without 1 → a unit/integration runner or API test tool — no whole-app user journey.
- 1+3 without 2 → ad-hoc automation or monitoring probes — no managed, owned, re-runnable test asset tied to the codebase.
- 1 alone → browser automation (Selenium-class substrate).
- 2 alone → test documentation (test management).

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. Whole-assembled-application exercise through its real user-facing interface (user-level journey; browser canonical today, desktop/mobile/API-in-journey per scope — NOT "browser" as defining word, per historical check).
2. Persistent automated test scenario of record (journey + expected outcomes; re-runnable; organized/configurable).
3. Automated execution producing per-test verdicts with diagnosable failure evidence.

### L1 — Common Mature Structure

- Element addressing layer (locators/selectors/test objects) + interaction actions
- Auto-wait / retry machinery as a stability philosophy; test retries
- Test isolation (fresh context/profile per test; session caching)
- Test organization (suites/projects/describe groups), hooks (setup/teardown), fixtures
- Environment/parameter configuration; data-driven testing
- Multi-browser (and per-scope multi-surface) matrices; parallel execution/sharding
- Reports (per-test results, filterable dashboards), run history/analytics
- Failure artifacts (screenshots, videos, traces, logs, HAR)
- Debug surfaces (interactive runner, command log, time travel, trace viewer)
- CI/CD integration (CLI, recipes, PR feedback); notifications
- Record/generate authoring aids

### L2 — Variant / Optional

- Authoring poles: code-first vs record-and-playback/keyword/low-code vs AI-generated (incl. generation from production sessions)
- Scope bundles: web-only; +desktop; +mobile; +API; enterprise-app adapters
- Execution venue: local-first vs cloud/managed (hosted browser/device grids — adjacent Type when it IS the product)
- Management/quality add-ons: test management, flake dashboards, coverage maps, branch review
- Adjacent capabilities bundled: visual testing, accessibility testing, component testing
- Network mocking/stubbing depth; private-environment bridging
- AI-era: assistants, MCP/agent integration, self-healing locators, test generation

### L3 — Vendor-specific (kept out of the final document)

- Cypress: in-browser run-loop architecture, Time Travel snapshots, cy.session, Branch Review, UI Coverage, cy.prompt
- Playwright: Browser Contexts/fixtures model, trace viewer, UI Mode, web server, test agents, Codegen
- Katalon: keyword system, manual↔script dual editors, Time Capsule, Smart Wait naming, KRE, TrueTest, TestCloud
- TestComplete: TestExecute, BitBar device cloud, enterprise app adapters (SAP/Salesforce/Dynamics/Oracle)
- mabl: Link Agent, plans/DataTables/branches vocabulary, cloud MCP tooling, export-to-Playwright

## Boundary Findings

1. **vs Unit / Integration Test Runner** — runner executes code-level tests against components/modules in isolation; E2E drives the assembled app through its real interface. Overlap risk: Cypress/Playwright also ship component testing (capability bundling). If the product's tests mount components rather than visit the app, it's the other Type.
2. **vs Browser Automation Library (substrate, not a directory leaf)** — Selenium-class libraries provide element automation without runner/assertions/results; platforms provide test semantics on top. Katalon self-describes as "built upon the Selenium framework".
3. **vs Software Test Management** — management holds test cases/runs/requirements/defects as records (execution usually manual or delegated); E2E platform's asset is the executable test it itself runs. Vendors bundle both (Katalon True Platform includes TestOps management).
4. **vs Test Automation Platform (directory sibling)** — heavy real-world overlap: sampled "test automation platforms" (Katalon, TestComplete) center on the same whole-app, UI-driven, verdict-producing execution. E2E Testing Platform is best held as the scope-disciplined member: whole app, user-level journeys, pre-release verdicts. Taxonomy note recorded.
5. **vs Device Testing Platform / Browser Compatibility Testing Platform** — those exist to provide environments (real devices/browsers, manual inspection, compatibility matrices); E2E platform exists for the test lifecycle. E2E products integrate/resell grids (TestCloud, BitBar) — integration, not identity. Seam question: is the product's core "run my test suite" (E2E) or "access/verify this environment" (device/compat)?
6. **vs Synthetic Monitoring** — same journey mechanics, different subject and loop: synthetic monitoring runs fixed journeys against production continuously for availability/broken-experience detection (ops/SRE-owned); E2E tests assert functional correctness of changes before release in test environments (dev/QA-owned, change-linked). Boundary markers: environment under test, purpose of the verdict, linkage to code changes.
7. **vs Load Testing Platform** — E2E asserts a single user's functional correctness; load testing generates concurrency/volume and measures performance. Cross-evidence: Selenium's own docs list performance testing under "Discouraged behaviors".

## Historical / Market-Sample Check

Would older, regional, differently-positioned products fit the L0?

- QTP/WinRunner/SilkTest-era (late 1990s–2000s) desktop-recorded GUI testing: real app exercised as whole (1), stored scripts/checkpoints (2), run with results logs and failure screenshots (3). **Fits L0** — no cloud, no browsers required (desktop UI), no parallelization pricing, no AI.
- Selenium-scripted E2E in CI with a results feed: fits 1+2+3 via the surrounding framework; Selenium alone is the substrate (consistent with boundary #2).
- Modern cloud SaaS (mabl): fits with authoring/exported formats as the test-of-record.
- Conclusion: L0 holds across eras and surfaces; "browser" and "code" are era/implementations, not definitional.

## Uncertainties

- mabl's authoring model (Trainer/browser recording) is widely known but NOT confirmed from fetched docs; kept out of strong claims.
- TestComplete deep mechanics (object mapping details, checkpoint types) confirmed only at doc-map level.
- Katalon True Platform management/analytics features not fetched directly; platform claims from navigation and Studio page.
- Numeric limits (parallel workers, timeouts, plan tiers) deliberately not asserted — plan-specific and version-specific.
- Directory sibling "Test Automation Platform" may be intended as the umbrella; if so, overlap is a taxonomy-level question flagged in STATUS Boundary Issues rather than resolved here.

## Final Synthesis

An End-to-end Testing Platform is the team's system for verifying that the whole assembled application works for a user: it holds persistent automated test scenarios that drive the application through its real interface, executes them (locally, in CI, or on hosted environments), and returns per-test verdicts with enough failure evidence to diagnose and fix — plus the stability machinery (waiting, isolation, retries) and delivery-loop attachment (CI, reports, notifications) that make the verdicts trustworthy at team scale. Browser UI is the dominant modern surface; desktop, mobile, and in-journey API calls are scope variants; authoring philosophy (code, record/low-code, AI) is a product-philosophy axis, not the Type.
