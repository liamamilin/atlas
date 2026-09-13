# Research Notes — Browser Compatibility Testing Platform

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Browser Compatibility Testing Platform really is as an Application Type: its defining core, its canonical object model, how the two dominant usage modes (manual live testing and automated grid testing) actually work, and where its boundaries lie against neighboring §12 testing Types, monitoring Types, and the shared cloud-browser substrate that newer agent platforms also consume.

## Initial Boundary

Working hypothesis before research:

- **What it is**: a platform that gives web teams on-demand access to a matrix of browser/OS/device environments so they can verify that a web application renders and functions correctly across that matrix — via interactive manual sessions and/or by executing the team's own test scripts against a hosted browser grid.
- **Who**: QA engineers, web/frontend developers, agencies testing client sites, enterprise QA teams.
- **Nearest neighbors**: Device Testing Platform, End-to-end Testing Platform, Test Automation Platform, Software Test Management, Synthetic Monitoring, Load Testing Platform, Web Browser, Agent Tool / Computer-use Platform (§12 — already processed; flagged a joint review with this leaf).
- **Unknowns at start**: whether "manual live sessions" or "automated grid" is definitional; whether cloud hosting is definitional; whether the "browser matrix" result view is a defining structure or vendor-specific; the exact scope creep of full-suite platforms.

## Research Questions

1. What is the core object model? (environment catalog, session, run, build, artifacts, matrix)
2. How does manual/live testing work end-to-end? (selection → session → debug → capture → report)
3. How does automated testing work? (frameworks, capabilities, execution, grouping, results)
4. How do platforms reach localhost/staging/private-network targets? (tunnel)
5. What result/observation surfaces exist? (live view, screenshots, videos, logs, per-environment status, matrix views, badges)
6. What varies by customer tier and era? (SMB live tools vs enterprise grids vs self-hosted; screenshot-only historical services)
7. Where is the boundary vs Device Testing, E2E/Test Automation, Synthetic Monitoring, Web Browser, and Agent Tool / Computer-use Platform?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Why sampled |
|---|---|
| **BrowserStack** | Market leader; full suite (Live manual + Automate grid + Percy visual + Test Management); mid-market→enterprise |
| **LambdaTest (rebranded TestMu AI, 2026)** | Direct competitor with slightly different packaging (Real Time + HyperExecute + SmartUI + KaneAI); docs hub openly machine-readable |
| **Sauce Labs** | Automation-first enterprise heritage (Selenium ecosystem pioneer); no strong manual surface observed — useful contrast |
| **TestingBot** | Smaller independent cloud platform; unusually complete and fetchable Tier-1 docs; SMB tier |
| **Browserling** | Manual-live-only, simple-form product (no automation grid); different philosophy; free/SMB tier |

Historical breadth check (per §24): attempted `browsershots.org` (2000s-era screenshot-only service) — transport error, abandoned after 1 attempt. Historical reasoning kept conceptual (see Historical / Market-Sample Check).

## Sources

All fetched 2026-09-06.

| # | Source | Tier | Status |
|---|---|---|---|
| 1 | BrowserStack Docs home — https://www.browserstack.com/docs/ | 1 | OK |
| 2 | BrowserStack Live product page — https://www.browserstack.com/live | 2 | OK (feature structure, "3,500+ browser combinations", real device cloud, local testing, DevTools, security/wipe claims) |
| 3 | BrowserStack Local Testing overview — https://www.browserstack.com/docs/local-testing/overview | 1 | OK (tunnel works "across automated, manual, and low-code testing") |
| 4 | BrowserStack /docs/live (docs page) | 1 | JS challenge, blocked ×1 — not retried; product page + docs home used instead |
| 5 | LambdaTest/TestMu AI docs hub — https://www.testmuai.com/support/docs/ | 1 | OK ("3000+ combinations"; full product map) |
| 6 | TestMu AI — Real-Time Desktop Web Browser Testing — …/getting-started-with-desktop-browser-real-time-testing/ | 1 | OK (complete manual flow: URL → OS/browser/version/resolution → Start → VM) |
| 7 | TestMu AI — Automated Screenshot Testing — …/automated-screenshot-testing/ | 1 | OK (bulk capture, scheduling, sharing; feature marked **deprecated** by vendor) |
| 8 | Sauce Labs docs home — https://docs.saucelabs.com/ ; What is Sauce Labs | 1 | OK |
| 9 | Sauce Labs — Platform Configurator — /basics/platform-configurator/ | 1 | OK (capability generation: API → device → OS → browser → screenshots/video/resolution → code) |
| 10 | Sauce Labs — Test Results hub — /test-results/ | 1 | OK (statuses, sharable links, **Status Badges and the Browser Matrix Widget**) |
| 11 | TestingBot docs — https://testingbot.com/support/ | 1 | OK ("6100+ real browsers and physical devices"; full product map) |
| 12 | TestingBot — Browser Matrix — /support/other/browser-matrix | 1 | OK (build grouping via capabilities; per-browser/platform pass-fail matrix image; badges) |
| 13 | TestingBot — List of available browsers — /support/web-automate/browsers | 1 | OK ("6723 combinations"; Chrome 36–151, Firefox 4–154, IE 8–11, Edge, Opera; Win 7–11, macOS 10.13→15-class, Linux, iOS, Android; beta/dev channels) |
| 14 | Browserling — https://www.browserling.com/ | 2 | OK (live interactive sessions; real browsers in VMs; old version lists; SSH tunnels; screenshots; no automation grid — headless API "coming soon") |

Not fetched / limitations:

- BrowserStack docs sub-pages are JS-gated for non-browser fetchers (one failure, not retried per network rule); Live internals (session time limits, concurrency defaults) therefore unverified — no precise numbers asserted anywhere.
- Sauce Labs manual-testing surface not observed in fetched pages; Sauce treated as automation-first sample.
- Browsershots (historical) unreachable — historical claims kept conceptual.
- BrowserStack/LambdaTest marketing numbers ("3,500+", "3000+", "6100+", "6723") are vendor-published catalog sizes; recorded as vendor claims (L3), not used as canonical facts.

## Product Observations

### BrowserStack (Evidence A unless noted)

From docs home + Live product page + Local Testing overview:

- Two named web-testing pillars: **Live** ("manual cross-browser testing") and **Automate** ("browser automation cloud / grid", Selenium / Playwright / Cypress / Puppeteer / JS Testing API). Mobile analogs: App Live / App Automate on real devices.
- Catalog claim: "instantly access 3,500+ real desktop & mobile browser combinations"; "new & old versions of Edge, Safari, Chrome, IE and Firefox on real iOS & Android, Windows and macOS devices"; 30,000+ real devices (app side).
- Live feature list: Real Device Cloud; 3,500+ browser combinations; **Test on dev environment** ("websites hosted on internal dev and staging environments, or behind firewalls"); **Multi-Device Testing** (simultaneous testing "on up to four real devices"); **Real-time debugging** ("pre-installed developer tools" — DevTools, Safari Web Inspector, network tab, inspect); **Security & Privacy** ("tamper-proof physical devices and desktop VMs, wiped clean of data after every session"); report-a-bug; location testing; network simulation; test analytics.
- **Local Testing**: "connects BrowserStack to websites and apps hosted on your localhost, staging, or private network, including anything behind a proxy, firewall, or VPN. The same secure tunnel works across automated, manual, and low-code testing." Local binary/desktop app, CLI flags, status API, proxy/SSL-inspection configs.
- Standalone free tools: **Screenshots** ("cross browser screenshots"), Responsive (responsiveness checks), SpeedLab (performance).
- Suite companions (adjacent capabilities, not the Type): Percy (visual testing & review), Test Management, Test Reporting & Analytics, Accessibility Testing, Load Testing, Low-Code Automation, Website Scanner, Automate Self-Hosted ("automation on your cloud"), Custom Device Lab, AI agents (test-case generation, self-healing, failure analysis, visual review), MCP server, Test Companion (agentic testing in IDE).

### LambdaTest / TestMu AI (Evidence A)

From docs hub + Real-Time doc + Screenshot doc:

- Docs hub tagline: "Test across 3000+ combinations of browsers, real devices & OS."
- **Real Time (manual)**: "test your websites and web applications directly on live desktop browsers… interact with their web applications across various browser environments, operating systems, and versions without the need to configure complex infrastructure on local machines."
  - Documented flow: navigate to Real Time Testing → Desktop → enter URL → select **Operating System** (Windows 11/10…, macOS Sequoia/Sonoma/Ventura…), **browser**, **browser version** ("versions displayed with release dates"), **screen resolution** → Start → "initiate the testing process" on a launched virtual machine.
  - Session options: **Tunnel** "for testing internal or locally hosted applications", Private Cloud toggle, pre-loaded Chrome extensions.
- **Automated**: Selenium / Cypress / Playwright / Puppeteer / K6 (browser) + Appium/Espresso/XCUI (app); **HyperExecute** (orchestration cloud with YAML/CLI, private cloud option).
- **Screenshot Testing** (bulk capture): "capture screenshots in bulk through different desktops and mobile devices running on various OS in a single go"; select browser-version × OS combinations; result page with per-screenshot download, download-all zip; recent sessions; preferences (resolution, quality, defer time, mobile layout portrait/landscape); **scheduling** (time/frequency/day); **share with expiry**; basic-auth support for password-protected pages; **saved browser-combination lists**. Vendor marks this feature **deprecated** (SmartUI is the successor visual product).
- **SmartUI** (visual regression), **KaneAI** (AI test authoring), **Test Manager** (test-case management), **Insights** (dashboards: flaky tests, build comparisons), Web Scanner (visual/accessibility scans), **Browser Cloud** (NEW: "launch session with SDK / agent skills", "connect to a session" — agent-substrate packaging), Agent Testing Platform, Testing Locally (tunnel: local pages, Docker tunnel, load balancing, IP whitelisting), SSO/SCIM, concurrency widget (metering surface).

### Sauce Labs (Evidence A)

From docs home, What-is page, Platform Configurator, Test Results hub:

- Positioning: "full-scale testing platform… regardless of the device, browser or operating system from which it is being accessed." Automation-first: quickstarts for Selenium, Appium, Espresso, XCUITest, Cypress, TestCafe, Playwright; `saucectl` CLI; REST API.
- **Platform Configurator** (capability authoring UI): select API (Selenium/Appium) → device type (desktop/mobile; Selenium includes iOS/Android/desktop) → **Operating System** → **Browser** (for Selenium) or test type (web/hybrid/app for Appium) → advanced configurations: "capture screenshots and record video are set by default", **Resolution** → "Copy Code": generates capabilities code in the tester's language to paste into the test script.
- **Test Results**: viewing test results; **sharing test results** (sharable links); **setting test statuses**; **"Status Badges and the Browser Matrix Widget"** — the same matrix visualization concept as TestingBot.
- Other sections: Sauce Trusted Connection (secure connections/tunnel — "Sauce Connect" family), CI, Insights, Performance, Visual (Sauce Visual — visual testing), Error Reporting, App Distribution, Real Device Access API, Data Center Endpoints, SSO, account & organization management.

### TestingBot (Evidence A)

From docs root, Browser Matrix page, browser list page:

- Positioning: "cloud testing platform with 6100+ real browsers and physical iOS and Android devices."
- **Automated web testing**: Selenium (per-language examples), Cypress, Puppeteer, Playwright, headless browsers, k6 browser testing, mobile web testing; **Test Configuration Options** (capabilities); **Selenium Grid** endpoint page; test annotation; network throttle/mock/intercept; performance testing in-session.
- **Manual web testing**: "remote testing with mouse and keyboard"; browser extension for one-click manual testing; ChromeOS web testing.
- **Environment catalog page**: "6723 combinations available for testing. Click a combination to see how to run an automated or manual test." Organized by OS (Windows 7/8/8.1/10/11; macOS High Sierra→Tahoe-class; Linux; iOS; Android) × browser × version — Chrome 36→151 (+beta/dev), Firefox 4→154 (+beta/dev), IE 11/10/9/8, Edge, Opera 50→134. Both manual and automated runs launch from the same catalog entries.
- **Builds & Browser Matrix**: tests grouped into a **build** via a capability (`"build": "build-1XXX"`); member area lists builds; test pass/fail states pushed via API; **Browser Matrix image** "shows the success state for every browser/platform in your build"; embeddable via markdown/HTML + **status badges**; auth-token scheme for private accounts.
- **Tunnel**: quickstart, multiple tunnels, upstream proxy, monitoring, CLI, troubleshooting.
- Visual Testing: automated + codeless screenshot comparison; results; stabilization.
- Codeless automation: add test → suites → **schedule** → alerts.
- Account mgmt: sub-accounts, roles & permissions, audit logs, 2FA, SSO; **billing via Parallel Calculator** (concurrency as the metering unit); REST API; CI/CD integrations (Jenkins, GitHub Actions, GitLab CI, CircleCI, Azure DevOps, …); issue-tracker integrations (Jira, GitHub, Trello, Asana); AI (codeless, MCP server, agent-framework integrations: Browser Use, Stagehand, AgentKit, …).

### Browserling (Evidence A)

From product page:

- Positioning: "Online cross-browser testing… Get a browser and start testing in 5 seconds!"
- "Live interactive sessions — Not just screenshots! You can interact with the browsers live as if they were installed on your computer."
- "Real browsers running on real computers… real desktop browsers on our servers in virtual machines. We don't use emulators or fake browsers."
- Browser/version catalog (old-version support as a core promise): Chrome 34→latest, IE 7–11, Firefox 32→114, Opera 39→94.
- Screenshots: "capture, save, and share screenshots of your web pages in all browsers… annotate them and send bug reports."
- Responsive testing: change screen resolution / resize browsers.
- **SSH tunnels for local testing**: "reverse-proxy your local host or local server into Browserling."
- Extensions/bookmarklets ("IE 11 on Windows 7"); **Live API** ("embed browsers in your own application on demand and automate them via a neat API"); geo-browsing (100+ locations); file transfers; session wiping.
- **No automated grid**: headless/automation API listed as "coming soon"; video recording and coworker screen-share also "coming soon".
- Same company also sells a **Browserling Cybersecurity** product ("secure browser sandboxes… investigate suspicious links") — the same remote-browser substrate packaged for a different job. Strong boundary evidence: substrate ≠ Type; the testing job defines the Type.

## Cross-product Comparison

| Dimension | BrowserStack | LambdaTest/TestMu | Sauce Labs | TestingBot | Browserling |
|---|---|---|---|---|---|
| Environment catalog (browser×version×OS) | Yes — "3,500+ combinations" claim; new+old versions; desktop VMs + mobile real devices | Yes — "3000+ combinations"; same shape | Yes — configured via Platform Configurator; data-center endpoints | Yes — 6,723 combinations enumerated publicly; Chrome 36–151, FF 4–154, IE 8–11 | Yes — small, manually enumerated; Chrome 34+, IE 7–11, FF 32–114 |
| Catalog includes environments not locally installable (old browsers, other OS) | Yes (IE on Mac cited in testimonials) | Yes (old versions with release dates) | Yes | Yes (IE 8–11 on modern Windows; FF 4+) | Yes (IE 7 on any host OS) |
| Manual live interactive session | Core (Live) | Core (Real Time) | Not observed in fetched docs (automation-first) | Yes ("remote testing with mouse and keyboard" + extension) | Core (the whole product) |
| Automated grid execution of customer test scripts | Core (Automate: Selenium/Playwright/Cypress/Puppeteer) | Core (+ HyperExecute orchestration) | Core (Selenium/Appium/Cypress/TestCafe/Playwright + CLI) | Core (same frameworks + Selenium Grid endpoint + headless) | No ("coming soon") |
| Capability-based environment selection | Yes (Automate capabilities; SDK) | Yes | Yes (Platform Configurator generates capabilities) | Yes (platformName/browserName/build examples) | n/a |
| Local/private target access via tunnel | Yes (Local binary, shared across products) | Yes (tunnel, Docker variant) | Yes (Sauce Connect family) | Yes (Tunnel product) | Yes (SSH reverse-proxy) |
| Bulk screenshot capture across configurations | Yes (standalone Screenshots tool) | Yes (screenshot testing; now deprecated in favor of SmartUI) | Screenshots/video per run (default-on per Configurator) | Yes (visual testing) | Yes (per-session capture/annotate) |
| Session artifacts (screenshots, video, logs) | Yes | Yes (test logs; videos) | Yes (video/screenshots default-on; error reporting) | Yes (recordings, logs, screenshots) | Screenshots only |
| Build/run grouping + per-environment result matrix | Build/test views (Automate) | Builds in Test Manager/Insights | **Browser Matrix Widget** + status badges | **Browser Matrix image** + status badges | n/a |
| Sharing/collaboration | Team/enterprise plans | Share w/ expiry; teams | Sharable links | Link/embed tests, badges, sub-accounts | Share screenshots/bug reports |
| CI/CD integration | Yes | Yes | Yes (CI section) | Yes (15+ systems) | No |
| Debugging tools in session | Yes (DevTools, network, inspect) | Yes (developer tools) | Yes (performance/error surfaces) | Yes (network throttle/mock) | Yes (responsive resize) |
| Concurrency/parallel metering surface | Not directly evidenced in fetch | Yes (concurrency widget) | Not directly evidenced in fetch | Yes (parallel calculator) | Free-tier session limits implied |
| Self-hosted / private option | Yes (Automate Self-Hosted, Custom Device Lab) | Yes (private cloud) | Data centers; not observed self-hosted | EU hosting | n/a |
| AI-era additions | Yes (agents, MCP, IDE companion) | Yes (KaneAI, Browser Cloud, MCP) | Yes (Sauce AI) | Yes (AI insights, MCP, agent integrations) | No |

### Findings that recur across the sample (Evidence B)

1. **Environment catalog as the product's backbone** — every product's home surface is the set of browser×version×OS(+device/resolution) combinations, explicitly enumerated or configurator-driven. Every product includes combinations the tester cannot practically run locally (old IE/Firefox versions, other OSes).
2. **On-demand observable execution** — the platform runs the customer's web target in the chosen environment and gives the tester eyes on it: live interactive session (4/5 products) and/or scripted runs (4/5) and/or one-shot bulk capture (4/5).
3. **Local tunnel as shared infrastructure** — present in all 5, always as a separate connecting component that exposes localhost/staging/firewalled targets to the hosted environments.
4. **Artifacts + per-environment results** — screenshots/videos/logs per session; pass/fail state per environment; matrix-style visualization of results across the environment set exists in ≥2 products as a named feature ("Browser Matrix" in both TestingBot and Sauce Labs).
5. **Standard-framework automation substrate** — the automated mode speaks the WebDriver/Playwright/Cypress/Appium ecosystem's protocol, with capabilities selecting the environment (4/5; Browserling the exception).
6. **Companion suite modules** — visual regression, accessibility, load, test management, analytics appear as adjacent modules in the larger platforms, consistently packaged as separate products/features, not as the compatibility core.

## Canonical Abstraction

### L0 — Defining Invariant

Keep deliberately small:

1. **Browser environment catalog** — a maintained, selectable set of browser environments defined at minimum by browser type + version × OS/platform (extended in many products by device and resolution). Its purpose is to span combinations the testing team cannot practically assemble locally.
2. **On-demand, observable execution of the customer's web target in a catalog-selected environment** — the user (or the user's test code) picks an environment; the platform instantiates it and runs the web application in it; the tester can observe the behavior (live view and/or recorded artifacts and/or per-environment pass/fail outcomes).

Remove either and the Type collapses:
- Remove the catalog's breadth/selection → it's just a browser (or the customer's own machine) — no compatibility dimension remains.
- Remove execution of *the customer's target* → it's a generic remote browser / agent substrate, not a testing platform (Browserling's own cybersecurity packaging proves the substrate is job-independent).

Note on purpose framing: the *job* is verifying consistent rendering/functioning of a web application across environments. The job, together with the two structures above, distinguishes the Type from the same substrate sold for agent execution or security investigation.

**Historical check (per §24)**: 
- A 2000s screenshot-only service (submit URL → receive screenshots across many browsers) satisfies both invariants (catalog + observable execution with screenshots as observation) with *neither* live sessions *nor* scripted runs — so neither mode belongs in L0; they are canonical realizations of "observable execution".
- A self-hosted Selenium Grid + locally maintained VM stack (pre-cloud practice) satisfies both invariants with *no vendor cloud* — so "cloud SaaS" does not belong in L0; the catalog may be self-maintained.
- Older/regional practice of testing on physical machine stacks likewise reduces to "catalog + on-demand execution".

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- **Manual live sessions** on hosted browsers/devices with real-time debugging tools (DevTools-style inspection, network views).
- **Automated grid execution**: the customer's existing test suites (Selenium/WebDriver, Playwright, Cypress, Puppeteer, Appium…) run against the grid; environment chosen via capabilities; **local tunnel** to reach private targets.
- **Session artifacts**: screenshots, video recordings, command/network logs per session.
- **Run/build grouping with per-environment results**: build identifiers group runs; per-browser/platform pass-fail; matrix visualization + status badges; sharable result links.
- **Bulk screenshot capture** across many configurations in one operation.
- **CI/CD integration** and issue-tracker integrations (bug reports from sessions).
- **Concurrency as the metering model** (parallel-session limits; pricing surface built around it).
- **Team/account administration** (members, roles, SSO at enterprise tiers).
- **Visual regression comparison** as a companion capability.
- **Environment-condition simulation**: network throttling, geolocation, screen resolution changes, pre-release (beta/dev) browser channels.

### L2 — Variant / Optional Structure

- **Real physical mobile devices** (real-device clouds) vs desktop VMs vs emulators — a posture choice; extends the browser matrix toward the sibling Device Testing Type.
- **Native/hybrid app testing** (Appium/Espresso/XCUITest) — extends beyond web targets.
- **Self-hosted / private-cloud deployments** ("automation on your cloud", private grids, EU-hosted).
- **Codeless/low-code test authoring and scheduling** — an extension into test-automation-adjacent territory.
- **AI-era layers**: AI test authoring, self-healing, failure analysis agents; agentic session surfaces ("browser cloud" for agents; MCP servers) — the substrate being resold to the Agent Tool / Computer-use Type.
- **Companion modules** in suites: load testing, accessibility scanning, website scanners, performance testing, app distribution.
- **Free-tier tools** (standalone screenshot/responsive checkers) as acquisition funnels.
- **One-shot historical form** (screenshot-only service) — no longer the market center, but a legitimate degenerate realization.

### L3 — Vendor-specific Structure (stays out of the final document)

- Product/brand names: Live/Automate/Percy/Test Companion (BrowserStack); Real Time/HyperExecute/SmartUI/KaneAI/Browser Cloud (LambdaTest/TestMu); Sauce Connect/saucectl/Sauce Visual (Sauce Labs); TestingBot Tunnel/Parallel Calculator; Browserling Live API/SSH-tunnel specifics.
- Numeric catalog sizes: 3,500+ / 3000+ / 6,723 / 6100+ (vendor-published, fluctuate).
- LambdaTest screenshot-testing caps (e.g. "up to 25 screenshots in a single session") on a feature the vendor has since deprecated.
- TestingBot's MD5-based auth-token scheme for public matrix images; open-source-account publicity defaults.
- Browserling's cybersecurity product line, geo-browsing location count, session-wipe mechanics.
- BrowserStack's security claims wording ("tamper-proof… wiped clean"), testimonial figures.

## Vendor-specific / Rejected Findings

- **"The platform must be a cloud SaaS"** — rejected. Automate Self-Hosted runs on the customer's cloud; HyperExecute has private-cloud setup; the historical self-hosted Selenium Grid satisfies the Type. The invariant is *platform-operated environment access*, not vendor-owned data centers.
- **"The platform must offer real devices"** — rejected. Browserling has none; classic browser-compat work is desktop-browser-centric. Real-device clouds are a common extension overlapping the Device Testing Type.
- **"The platform must support automated Selenium"** — rejected. Browserling is manual-only and still clearly this Type; historical screenshot services are neither.
- **"Visual regression / AI agents / test management are part of the Type"** — rejected as definitional; they are companion modules (consistently packaged separately even inside suites).
- **"The Browser Matrix view is one vendor's invention"** — rejected: it recurs as a named concept in ≥2 independent products; treated as common mature structure (L1).
- **"This is just remote browsing"** — rejected: remote-browser substrate is job-neutral (Browserling sells the same substrate for security investigation; agent platforms consume it for task execution). The testing job + evidence-return loop is what makes the Type.

## Boundary Findings

1. **vs Device Testing Platform (§12 sibling; unprocessed)** — center-of-gravity seam. Browser compat centers on the *browser×version×OS matrix for web applications*; device testing centers on *physical mobile devices/hardware for app QA*. Overlap is real: mobile *browser* testing and real-device clouds appear inside compat platforms (BrowserStack Live ships real Android/iOS browsers; TestingBot same). Test: remove the browser-version matrix → device farm; remove physical devices → the browser-compat core stands. Flag for joint review when the sibling leaf is processed.
2. **vs End-to-end Testing Platform / Test Automation Platform (§12 siblings; unprocessed)** — the E2E/automation Types center on *authoring and managing test logic* (tests as the artifact); this Type centers on *providing environments* (environments as the artifact; the test code belongs to the customer). The compat platform executes the customer's existing suites; authoring surfaces (codeless/AI) are newer optional extensions. Test: remove the environment catalog → a test runner; remove framework support → a live/screenshot service.
3. **vs Software Test Management (§12)** — management organizes test cases/plans/runs as records; compat platform executes sessions in environments. Suites bundle both; the centers differ.
4. **vs Synthetic Monitoring (§14 sibling; unprocessed)** — monitoring runs recurring, scheduled checks against live production to detect availability/performance degradation; compat testing is development/CI-time verification across an environment matrix. Scheduled screenshots exist on both sides (scheduling surface observed here), so scheduling alone is not the discriminator; the job (pre-release verification vs operational vigilance) is.
5. **vs Web Browser (§02.01)** — the platform provides browsers as *test substrate for someone else's web application*; it is not a consumer browsing surface.
6. **vs Agent Tool / Computer-use Platform (§12; processed — the flagged joint review)** — same cloud-browser substrate; different invoker and job. Here: a human tester or human-written test code drives the session to *verify expected behavior* of the customer's web app; there: a model decides actions at runtime to *accomplish tasks*. Both directions evidenced: the agent-tool pass recorded that a sampled tool platform lists automated testing as a use case; this pass observes the mirror image — compat vendors now sell agent-oriented session substrates (LambdaTest "Browser Cloud" with SDK/agent-skill launch + connect-to-session; TestingBot MCP + agent-framework integrations) *alongside* their testing products, confirming the substrate is shared infrastructure while the testing product remains distinct. Joint-review response: related Types, no merge; flag answered and can be closed when the sibling ledger is reviewed.
7. **vs Load Testing Platform / Performance Testing (§12)** — traffic simulation vs single-session behavior verification; load testing appears only as a bundled companion module in this sample.

## Uncertainties

- BrowserStack docs sub-pages were JS-gated; Live session internals (time limits, concurrent-session defaults) unverified → no precise operational numbers asserted anywhere in either file.
- Sauce Labs manual/live surface not directly observed; Sauce treated as automation-first sample; no claim that "all platforms have both modes" (sample proves modes vary).
- Browsershots unreachable; the historical screenshot-only form is reasoned from the sample's own bulk-capture features (e.g., LambdaTest's deprecated screenshot testing) rather than verified directly.
- Catalog sizes are vendor-published and fluctuate; treated as claims only.
- The exact current packaging of LambdaTest (TestMu AI rebrand, 2026) may still be in flux; product-map evidence fetched 2026-09-06.

## Final Synthesis

A Browser Compatibility Testing Platform is defined by two structures and one job: a **selectable catalog of browser environments** (browser + version × OS, commonly extended with devices and resolutions) that spans combinations teams cannot practically assemble locally; **on-demand, observable execution of the team's own web application in a chosen environment** — realized as interactive live sessions, scripted grid runs, or bulk captures; and the job of **verifying consistent rendering and functioning across that environment matrix**. Everything else observed — tunnels, artifacts, build grouping, matrix views and badges, CI/CD hooks, concurrency metering, team administration, visual regression, real-device clouds, self-hosting, and AI-era authoring — is common mature structure or variant posture, not definition.
