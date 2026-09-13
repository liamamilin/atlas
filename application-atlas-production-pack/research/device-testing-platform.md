# Research Notes — Device Testing Platform

Research date: 2026-09-08
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what a Device Testing Platform really is as an Application Type: its defining core, its canonical object model (device fleet, session, app under test, artifacts), how the two dominant usage modes (interactive remote-access sessions and automated device-farm runs) actually work, how the platform operates a physical device fleet, and where its boundaries lie against the sibling Browser Compatibility Testing Platform, the testing-family Types, endpoint-management Types, and the agent platforms that consume the same hosted-device substrate.

## Initial Boundary

Working hypothesis before research:

- **What it is**: a platform that gives mobile app teams on-demand access to a fleet of hosted devices (typically real physical phones/tablets) as a selectable catalog, so they can install their app binaries on chosen devices and verify app behavior via interactive remote sessions and/or automated test runs, with device-level artifacts returned.
- **Who**: mobile QA engineers, mobile developers reproducing device-specific bugs, automation engineers, enterprise mobile teams.
- **Nearest neighbors**: Browser Compatibility Testing Platform (§12 sibling — flagged joint review), End-to-end Testing Platform, Test Automation Platform, Software Test Management, Mobile App Development Platform, Endpoint Management / UEM (§14), Remote Monitoring & Management (§14), Application Performance Monitoring (§14), Agent Tool / Computer-use Platform (§12 — joint-review flag from two prior passes).
- **Unknowns at start**: is "physical real device" definitional (vs emulators/simulators)? Is cloud SaaS definitional (vs on-prem/private labs)? Is automation definitional (reservation-based manual-only OEM labs may not have it)? Is mobile the boundary (TVs/wearables observed in OEM sample)? What actually distinguishes the device catalog from a browser-version matrix?

## Research Questions

1. What is the core object model? (device catalog, device instance, session, run, app binary, artifacts, results)
2. How does manual/interactive device testing work end-to-end? (search device → launch session → install app → interact → capture → end)
3. How does automated device testing work? (frameworks, capabilities, upload app+tests, parallel execution, results)
4. What attributes define a device in the catalog? How is the fleet operated as physical inventory?
5. How do platforms meter access? (device slots, concurrency, reservations, bundles)
6. What varies? (cloud vs private/on-prem labs, real vs virtual devices, OEM free labs, device families beyond phones)
7. Where is the boundary vs Browser Compatibility Testing, E2E/Test Automation, Test Management, UEM/RMM, APM, and Agent Tool platforms?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Why sampled |
|---|---|
| **AWS Device Farm** | Hyperscaler device farm; usage-based pay-per-use; unusually strong Tier-1 docs (developer guide + API reference); automation-first with manual remote access; also sells a separate desktop-browser pillar (TestGrid) — useful contrast |
| **BrowserStack App Live / App Automate** | Commercial market leader's real-device cloud; manual-first (App Live) + automation cloud (App Automate); same vendor as the browser-compat Type — ideal for the sibling seam |
| **Kobiton** | Device-farm pure-play; distinctive philosophy: cloud **or on-prem/private** device lab management (customer's own devices operated by the platform); rich fetchable docs |
| **Samsung Remote Test Lab** | OEM-operated free lab for Samsung's own Galaxy fleet (phones, foldables, tablets, TVs, watches); reservation-based, manual-interactive; platform-native/regional pole; §24 market-breadth check |

Historical breadth reasoning kept conceptual (see Historical check): the pre-cloud in-house device lab is the degenerate form; Firebase Test Lab attempted but unreachable (see Sources).

## Sources

All fetched 2026-09-08.

| # | Source | Tier | Status |
|---|---|---|---|
| 1 | AWS Device Farm product page — https://aws.amazon.com/device-farm/ | 2 | OK (positioning, real-device rationale, private device lab, test-framework choice, CI integration, benefits structure) |
| 2 | AWS Device Farm API Reference Welcome — https://docs.aws.amazon.com/devicefarm/latest/APIReference/Welcome.html | 1 | OK (two pillars: TestGrid desktop browsers vs real mobile devices) |
| 3 | AWS Device Farm Developer Guide — Test frameworks and built-in tests — https://docs.aws.amazon.com/devicefarm/latest/developerguide/test-types.html | 1 | OK (service-side execution architecture, frameworks, client-side Appium, built-in fuzz) |
| 4 | AWS Device Farm Developer Guide — Remote access — https://docs.aws.amazon.com/devicefarm/latest/developerguide/remote-access.html | 1 | OK (manual session model, features, device slots, security note) |
| 5 | BrowserStack App Live product page — https://www.browserstack.com/app-live | 2 | OK (real device cloud, gestures, debugging, multi-device, app upload/store install, Custom Device Lab, real-device features) |
| 6 | Kobiton product page — https://kobiton.com/ | 2 | OK (platform pillars, cloud/on-prem, manual→automation conversion, device features, Session Explorer) |
| 7 | Kobiton Docs hub — https://docs.kobiton.com/ | 1 | OK (complete product map: devices/apps/manual/automation/scriptless/debugging/organization/test management/reporting/device lab management) |
| 8 | Kobiton Docs — Start a manual session — https://docs.kobiton.com/manual-testing/start-a-manual-session | 1 | OK (device search → launch → on-screen controls flow) |
| 9 | Kobiton Docs — Device metadata — https://docs.kobiton.com/devices/device-metadata | 1 | OK (full device attribute set incl. UDID/IMEI/ICCID/carrier/location/health/usage) |
| 10 | Samsung Remote Test Lab — https://developer.samsung.com/remote-test-lab | 2 | OK (device catalog incl. TV/watch, free sign-up, remote control, partner program reservations) |

Not fetched / limitations:

- **Firebase Test Lab** — https://firebase.google.com/docs/test-lab and /android/get-started both timed out (2 attempts) → abandoned per network rule. No Firebase-specific claims made anywhere.
- **BrowserStack App Automate product page** — JS challenge (1 attempt, not retried; sibling pass observed the same gating). BrowserStack automation-side detail relies on the App Live page + the sibling research file (browser-compatibility-testing-platform.md), which documents App Automate as the "mobile app automation cloud".
- **Samsung RTL doc internals** (device/reservation pages) — JS-rendered, body unreachable (2 attempts on doc pages). Reservation mechanics asserted only at the level visible on the main page ("longer device reservations", "select your preferences").
- Catalog sizes ("2,500+ devices", "30,000+ real devices", "365+ device models") are vendor-published catalog claims; recorded as claims, not used as canonical facts.

## Product Observations

### AWS Device Farm (Evidence A unless noted)

From the product page, API reference, and developer-guide pages:

- Positioning: "an application testing service that lets you improve the quality of your web and mobile applications by testing them across an extensive range of desktop browsers and real mobile devices, without having to provision and manage any testing infrastructure." Concurrent testing on multiple devices "to speed up the execution of your test suite"; generates "videos and logs to help you quickly identify issues."
- Real-device rationale: "Unlike emulators, physical devices give you a more accurate understanding of the way users interact with your application by taking into account factors like memory, CPU usage, location, and modifications made by manufacturers and carriers to the firmware and software." Fleet claim: 2,500+ devices (vendor claim).
- Manual + automated: "Manually reproduce issues and run automated tests in parallel. We collect videos, logs, and performance data… For automated tests, we'll identify and group issues."
- Condition simulation: "configuring location, language, network connection, application data, and installing prerequisite apps to simulate real-world customer conditions."
- Test choice: "Run our built-in test suite (no scripting required) or customize your tests by selecting from open source test frameworks like Appium, Calabash, and Espresso. You can also perform manual tests with remote access."
- Workflow integration: "service plugins and API to automatically initiate tests and get results from IDEs and continuous integration environments like Android Studio and Jenkins."
- Private device lab: "choose iOS and Android devices for your exclusive use… provisioned with the exact configurations you need, and lets you persist settings between sessions… you don't have to wait for other users to finish using them."
- Desktop-browser pillar sold separately (TestGrid): managed Selenium browser grid with videos/console logs/action logs/webdriver logs and pay-per-minute pricing — the same vendor keeps browser environments in a distinct product from the device farm.
- **API-level Type split**: API Reference: "Testing on desktop browsers" (APIs with `TestGrid` in their names) vs "Testing on real mobile devices… test apps on physical phones, tablets, and other devices in the cloud."
- **Service-side execution architecture** (test-types page): "Device Farm runs automated tests by having you upload your app and tests to a secure Amazon S3 bucket managed by the service. Once uploaded, it spins up the underlying infrastructure, including service-managed test hosts, and executes the tests in parallel on multiple devices. The test results are stored in a service managed S3 bucket." Alternatively, client-side execution: "With a remote access session, you can run client-side Appium tests" via an Appium endpoint.
- Frameworks: Android — Appium, Instrumentation; iOS — Appium, XCTest, XCTest UI; web apps via Appium. Built-in test type: fuzz (Android and iOS) — "test your application on multiple devices without having to write and maintain test automation scripts."
- **Remote access (manual) model** (remote-access page): "Remote access, or manual testing, allows you to swipe, gesture, and interact with a device through your web browser in real time to test functionality and reproduce customer issues. You interact with a specific device by creating a remote access session with that device." Features: app upload (.apk, .ipa) or web browsers; Appium Endpoint from the session; orientation change; network shaping (pre-configured or custom profiles); location mocking (lat/long); screenshot; video recording; logs (live Appium stream; device/network/activity logs at session end).
- Session semantics: "A session in Device Farm is a real-time interaction with an actual, physical device hosted in a web browser. A session displays the single device you select when you start the session." Concurrency: "the total number of simultaneous devices limited by the number of device slots you have… purchased based on the device family (Android or iOS devices)."
- Fleet curation + security: "Device Farm currently offers a subset of devices for remote access testing. New devices are added to the device pool all the time." "For security reasons, we recommend that you avoid providing or entering sensitive information… during a remote access session."

### BrowserStack App Live / App Automate (Evidence A for App Live; sibling notes for App Automate)

From the App Live product page:

- Positioning: "Test Your Mobile Apps on Real Devices — Instant access to 30,000+ real iOS and Android devices on the cloud. Say goodbye to your device lab." Catalog claim: 30,000+ real devices, 365+ device models (vendor claims).
- Real Device Cloud: "iPhone, Samsung Galaxy, Pixel, Nexus & more on multiple Android and iOS versions."
- Natural gestures: "Interact with your mobile app on the remote device. Tap, scroll, zoom, swipe & more, just like on a physical device."
- Real-time debugging: "Debug your app, view crash reports and logs, inspect UI element, and use stacktrace to find and fix bugs instantly." DevTools menu: Inspect tool, Appium Inspector integration, record test session, Firebase Crashlytics, Charles Proxy, app and device logs, network logs, ADB shell.
- Multi-Device Testing: simultaneous testing "on up to four real devices"; test different app variations or flows across multiple apps.
- **App under test**: "Upload, test & collaborate on your dev APK/AAB/IPA files or install production apps from Play Store/App Store."
- Real-world conditions: "30+ native device features like biometrics, physical SIM, file transfer & more." Real Device Features pages: media injection, payment & security workflows, physical SIM, accessibility testing, location and device settings.
- Device-state controls (iOS): device state, date & time, accessibility & appearance, low battery mode, app settings.
- Local testing: BrowserStack Local App for apps behind proxy/firewall/VPN.
- **Custom Device Lab**: exclusive access to real devices (smartphones, tablets) and desktop browsers; "custom configurations like app persistence and real device features like SIM binding"; isolated environments for security/compliance (BFSI, healthcare).
- Case-study framing: "150 real device-OS combinations tested"; "New devices are readily available on BrowserStack App Live from Day 0"; quality framed as "device, location, and network coverage."
- App Automate ("mobile app automation cloud") documented from the sibling pass's product-map evidence and this page's nav; automation detail not re-fetched (JS-gated).

### Kobiton (Evidence A)

From the product page and docs hub:

- Positioning: "Mobile App Testing on Real Devices — Test, automate, and release mobile apps faster with Kobiton's real device cloud for QA and engineering teams." Headline posture: "Real devices, not emulators; Manual and automated testing."
- Deployment axis: "The Fastest Mobile Test Automation Platform In the Cloud or On-Prem." AT&T case study: "Flexible deployment options for AT&T's mobile device labs."
- Platform pillars: **Device Lab Management** ("empowers QA teams to build their own mobile lab perfectly tailored to your QA team's needs"), **Mobile Device Cloud** ("device-in-hand experience, virtually"), **Mobile Test Execution**, **Mobile App Dev Tools**, **Test Results & Collaboration** (Session Explorer — "an iMovie-like experience to relive the test execution, rapidly pinpoint issues, and assign defects"), **AI Augmented Testing**, **No-Code Validations**, **Mobile Test Management**.
- Manual→automation bridge: "Kobiton converts manual test sessions captured on real devices into production-ready Appium scripts" (Java, Python, NodeJS, C#); "One manual test… replay it across multiple devices without scripting."
- Device-level features: biometrics simulation (fingerprint / Face ID), image injection (camera: receipt scanning, ID verification, boarding passes, barcodes), location mocking (GPS: geofencing, store locators, delivery zones), real-time device metrics (memory, CPU, network, battery, temperature).
- Session Explorer: session timeline, screen-load-time thresholds flagged, permanent links to exact test steps, share via Slack/Jira, one-click Jira bug filing "pre-populated [with] session link, OS, resolution, device info, logs, crash logs, and Appium logs", network captures export as HAR.
- Frameworks: Appium, XCUITest, Espresso. AI-era layer: Claude Code plugin / MCP tools — "writes end-to-end tests, uploads builds, reserves real devices, runs tests, and analyzes results from your IDE."
- **Docs map (operational model)**:
  - *Devices*: search for a device (views, categories, statuses), manage devices, **local or private devices** (connect to a private network, cleanup policies, network payload capture), manage preinstalled apps, device metadata, IP allowlists for public/Kobiton-hosted devices.
  - *Apps*: manage apps, app metadata, supported app filetypes and size, upload via portal/API/CI (Bitrise, Buildkite, CircleCI), biometric-authentication SDK, image-injection SDK.
  - *Manual testing*: start a manual session, **start a virtual session**, install an app, device controls, metrics, device logs, inspector, Apple Pay / Google Pay in-session, screen-reader testing (TalkBack/VoiceOver), audio injection, image injection, adb shell commands, custom gestures, shake gesture, mixed session, resume a session.
  - *Automation testing*: supported client libraries, Appium Inspector, capabilities (auto-generate), scripting, session ID, run in CI/CD (Azure DevOps, Bitrise, Buildkite, CircleCI), session timeouts, Turbo Test Execution, Appium AI (natural-language locators).
  - *Scriptless automation*: baseline session, run scriptless test (incl. API).
  - *Debugging*: virtualUSB (attach local tooling to devices as USB), CLI, iOS file sharing.
  - *Session Explorer*: search, custom queries, manage, analytics (timeline, reinspect Appium elements, network payloads, system metrics, crash logs, device logs), validations (accessibility), session metadata.
  - *Organization*: RBAC, teams, roles/permissions, team devices, team cleanup policy, **device bundles**, SSO, "create a shared account for automation tests".
  - *Test Management*: test cases, test runs, test suites, test reruns, remediations.
  - *Reporting*: **device availability report**, **device summary report**, usage report, system latency report.
  - *Device lab management*: **deviceConnect** (hardware requirements, logs, service restarts, host-machine capacity), deviceShare, iOS device onboarding (prepare device, signing certificate + provisioning profile, import into Mac mini host, add device), Android device onboarding, standalone/on-prem (including **air-gapped iOS devices**), tidy up devices.
- Manual session flow: Devices tab → search via views/categories/statuses → **Launch** → on-screen device controls.
- **Device metadata** (attribute set of a catalog device): device name, OS, OS version, UDID (iOS) / serial (Android), manufacturer, resolution, tags, installed browser, CPU platform, total memory, phone IMEI/ICCID/IMSI, security patch, carrier, network type, battery temperature, battery health, mobile number, current user ("Used By"), usage duration, device health, network status, device model, **physical location (e.g. "Atlanta, US")**, Lightning-mode capability.

### Samsung Remote Test Lab (Evidence A, Tier 2)

From the product page:

- Positioning: "Use the Remote Test Lab service to test your applications on a real device… Don't have a Samsung device to test your app? No Problem! Test your apps on the latest Samsung Galaxy devices in our Remote Test Lab."
- Device catalog spans form factors: Galaxy phones (S26 Ultra), foldables (Z Fold8, Z Flip8), tablets (Tab S11), QLED 4K TV, watches (separate Galaxy Watch product area); "Remote Test Lab for TV — test and verify your Tizen TV App on a real device."
- Access model: free sign-up → "Select your preferences" → "Go to the Remote Test Lab page, and click START TESTING" — web-based, three steps.
- "Remote Test Lab is a service that enables developers to control devices remotely"; web client for mobile-app testing through a browser.
- Partner Program: "longer device reservations, premium services, and a chance to try the latest Galaxy devices" — access is **reservation-shaped**.
- No automation grid surfaced on the fetched page (docs internals unreachable); OEM pole observed as manual-interactive remote device access for the vendor's own device fleet.

## Cross-product Comparison

| Dimension | AWS Device Farm | BrowserStack App Live/Automate | Kobiton | Samsung Remote Test Lab |
|---|---|---|---|---|
| Device catalog as product backbone | Yes — device fleet, "2,500+ devices" claim, constantly adding devices | Yes — "30,000+ real devices, 365+ models" claim, day-0 new devices | Yes — device search/views/statuses, supported-device lists | Yes — Samsung's own fleet: phones, foldables, tablets, TV, watches |
| Device = hardware model × OS (+ physical attributes) | Yes ("physical phones, tablets, and other devices") | Yes (device models across Android/iOS versions) | Yes — metadata includes IMEI/ICCID/IMSI, carrier, battery health, physical location | Yes (real Samsung hardware incl. TV) |
| Real-physical emphasized vs emulators | Yes (explicit emulator contrast) | Yes ("Real devices… say goodbye to your device lab") | Yes ("Real devices, not emulators") + virtual sessions as complement | Yes ("a real device") |
| App binary as object under test | Yes — upload .apk/.ipa (+ tests) | Yes — upload APK/AAB/IPA or install from Play/App Store | Yes — app repository, upload portal/API/CI, preinstalled apps | Yes (apps installed on reserved device; implied) |
| Web-app testing also possible | Yes (web browsers in remote access; TestGrid pillar separate) | Yes (mobile web + separate Live product) | Yes ("manually test your websites and apps"; browser metadata attribute) | Not surfaced in fetched page |
| Interactive manual session (remote control) | Yes — remote access session, gestures via browser | Yes — natural gestures on remote device | Yes — on-screen device controls, custom gestures, shake | Yes — "control devices remotely" via web client |
| Automated runs of customer test code | Yes — service-side execution, parallel on devices; Appium/Instrumentation/XCTest/XCTest UI | Yes — App Automate (mobile app automation cloud) | Yes — Appium/XCUITest/Espresso, capabilities, CI/CD | Not surfaced in fetched page (docs unreachable) |
| Built-in/no-script tests | Yes — built-in fuzz | Not surfaced on fetched page | Scriptless automation (replay recorded manual sessions) | No |
| Artifacts: screenshots/video/logs | Yes (video of each session; live + end-of-session logs) | Yes (record session, crash reports, device/network logs) | Yes (Session Explorer: timeline, metrics, crash/device/Appium logs, HAR) | Not evidenced in fetched page |
| Device-level condition simulation | Yes (location, language, network profiles, app data, prerequisite apps) | Yes (biometrics, SIM, location, media injection, device state) | Yes (biometrics, image/audio injection, GPS mocking, metrics) | Not evidenced in fetched page |
| Device exclusivity + concurrency metering | Yes — device slots purchased per device family | Yes — team/enterprise plans; multi-device (4) simultaneous | Yes — device bundles, team device assignment, shared automation accounts | Reservation-based (partner program = longer reservations) |
| Fleet hygiene / device state | Session artifacts wiped (private lab persists settings) | "Say goodbye to your device lab"; Custom Device Lab persistence | Cleanup policies per device/team; tidy up devices; preinstalled apps | Not evidenced in fetched page |
| Devices as physical inventory (hosts, health, location) | Test hosts service-managed; devices hosted by AWS | Real-device cloud data centers | Mac mini hosts, device health, location, availability/usage/latency reports | OEM-operated |
| Private / on-prem device lab | Yes — private device lab (exclusive devices, persistent settings) | Yes — Custom Device Lab (exclusive, persistent, isolated) | Yes — deviceConnect/deviceShare, standalone on-prem, air-gapped devices | n/a (OEM fleet) |
| CI/CD + IDE integration | Yes (plugins, API, Jenkins, Android Studio) | Yes (integrations; sibling-documented) | Yes (CI integrations; CLI; IDE plugins; MCP) | Not surfaced |
| Bug-reporting / result sharing | Issue grouping for automated tests | Report a bug; case studies | One-click Jira filing with pre-populated session context | Not surfaced |
| Organization/roles | AWS account model | Teams/enterprise | RBAC, teams, roles, SSO, device bundles | Samsung developer account |
| Web-browser pillar sold separately | Yes (TestGrid) | Yes (Live/Automate — the compat sibling) | No (device-centric) | No |

### Findings that recur across the sample (Evidence B)

1. **The device catalog/fleet is the product's backbone** — every product's home surface is a selectable set of devices defined by hardware model × OS version, extended with manufacturer, form factor, and physical attributes. The catalog's purpose is to span devices the team cannot practically assemble or keep current ("say goodbye to your device lab", "we are always adding devices", day-0 availability).
2. **On-demand, observable execution of the customer's app on a chosen device** — the user (or the user's test code) selects a device; the platform grants access to it; app behavior is observed live (interactive remote session) and/or captured as artifacts (screenshots, video, device/crash/network logs, performance metrics). Present in all four; interactive sessions in all four (automation absent only where evidence was unreachable).
3. **The app binary is the object under test** — mobile apps are uploaded as APK/AAB/IPA files (or installed from public app stores); this distinguishes the flow from URL-based browser testing. Web-app testing on devices exists as a secondary surface in most products.
4. **Physicality is the market posture** — all four explicitly anchor on real physical devices and contrast with emulators; device attributes are hardware/physical (UDID, IMEI, carrier, battery, physical location, device health). Virtual/emulator sessions appear as a complement (Kobiton "Start a virtual session"), not the anchor.
5. **Sessions and runs are the working units** — interactive "sessions" (remote access; single selected device; start/resume/timeout lifecycle) and automated "runs" (app+tests executed in parallel across devices); concurrency metered via device slots, device bundles, or reservations.
6. **The platform operates a physical fleet** — devices are inventory: hosts (Mac minis for iOS), health monitoring, cleanup/wipe policies between users, physical locations, availability reports, IP allowlists. This operational layer has no analog in the browser-matrix sibling.
7. **Device-level condition simulation** — location mocking, network shaping, biometrics/image/audio injection, device state (date/time, battery) recur across products as the way to reproduce real-world conditions.
8. **Standard mobile automation ecosystem** — automation speaks the customer's existing frameworks (Appium, XCUITest, Espresso, Instrumentation/XCTest), with capabilities/tags/bundles selecting devices; CI/CD and IDE integration is standard; manual→automation bridges (record/replay, script generation) appear as accelerators.
9. **Result-analysis and bug-handling surfaces** — session replay/timelines, per-device results, issue grouping, one-click bug reports into trackers with device context.
10. **Private/exclusive device pools and lab management** — exclusive devices with persistent settings (AWS private device lab, BrowserStack Custom Device Lab) and customer-owned fleets operated by the platform (Kobiton deviceConnect/on-prem) — a deployment variant, not a third Type.

## Canonical Abstraction

### L0 — Defining Invariant

Keep deliberately small:

1. **Device catalog (fleet)** — a maintained, selectable set of device environments defined at minimum by device hardware + operating system (extended in products with manufacturer, form factor, screen, carrier/SIM, physical location). Its purpose is to span app-relevant devices the testing team cannot practically own, procure, or keep current.
2. **On-demand, observable execution of the customer's app on a selected device** — the user (or the user's test code, or an agent acting for the user) picks a device from the catalog; the platform instantiates access to it, installs/runs the customer's app on it, and returns observable behavior: live interactive control and/or captured artifacts (screenshots, video, logs, device metrics).
3. **The device-coverage job** — the purpose the two structures serve: verifying an application's behavior and quality across a fleet of devices (device/hardware compatibility and reproduction of device-specific issues).

Remove any one and the Type collapses:

- Remove the catalog's breadth/selection → the team tests on its own hand-held device(s); no device-coverage dimension remains.
- Remove execution of *the customer's app* → it is remote device access as infrastructure (screen mirroring / agent substrate), not an app-testing platform.
- Remove the device-hardware axis (keep only browser+version×OS environments) → it is the sibling Browser Compatibility Testing Platform.

Note on purpose framing: the *job* (device coverage for app QA) plus the two structures distinguishes the Type from the same hosted-device substrate sold for IT endpoint management, support, or agent task execution.

**Historical / market-sample check (per §24)**:

- The **pre-cloud in-house device lab** (a shelf of physical phones/tablets; testers manually install each build; a video/log may be captured by hand or camera) satisfies catalog + observable execution + coverage job with **no vendor cloud, no automation framework, no pay-per-minute** — so none of those belong in L0.
- **Samsung Remote Test Lab** (OEM-operated, free, reservation-shaped, manual-interactive, spanning phones/tablets/TV/watches) satisfies the core without commercial SaaS packaging or automation evidence — so "automation grid" and "pay-per-use cloud" do not belong in L0; reservation-based access and OEM ownership are variant poles.
- **Kobiton on-prem / AWS private device lab** — the catalog can be the *customer's own* fleet operated by the platform software — so "vendor-owned cloud devices" does not belong in L0; platform-operated access does.
- Older regional practice (in-house labs, OEM developer programs) reduces to the same two structures; the sample's OEM pole also shows the device axis extends beyond phones (TVs, watches) without changing the Type.

### L1 — Common Mature Structure

Present in most mature products; expected by the market but not definitional:

- **Interactive remote-access sessions** with gesture control from a browser, on-screen device controls, orientation change, custom gestures.
- **Automated device-farm runs**: customer's Appium/XCUITest/Espresso/Instrumentation suites executed in parallel across selected devices; service-side or client-side execution; capabilities/tags/device bundles for device selection.
- **App repository**: upload via portal/API/CI; versioning/metadata; preinstalled apps; installing production apps from public stores.
- **Session/run artifacts**: screenshots, video recording, device logs, crash logs, network logs/captures (HAR), Appium command logs.
- **Device-level observability**: performance metrics (CPU, memory, network, battery, temperature) tied to the session timeline; session replay (Session-Explorer-class surfaces).
- **Condition simulation**: location mocking, network shaping/profiles, biometric simulation, image/audio injection (camera/SIM workflows), device state (date/time, battery, language).
- **Debugging tools in session**: UI inspector (Appium Inspector-class), adb shell, DevTools/proxy integration, virtualUSB-class local tool attachment.
- **CI/CD and IDE integration**: trigger runs and fetch results from pipelines; plugins/CLI/API.
- **Concurrency and access metering**: device slots per platform family, parallel-run limits, device bundles, reservations; usage/availability reporting.
- **Fleet hygiene and state rules**: cleanup/wipe policies between sessions, session timeouts, private pools with persistent settings, preinstalled-app management.
- **Result analysis + bug handling**: per-device pass/fail, issue grouping, session links, one-click bug reports with device context into issue trackers.
- **Organization surfaces**: teams, RBAC, SSO, shared automation accounts.
- **Companion modules in suites** (packaged separately): visual testing, accessibility testing, test management, performance testing.

### L2 — Variant / Optional Structure

- **Virtual devices** (emulators/simulators) as a complement tier alongside real devices (observed as a Kobiton surface; widely present in the market — but emulator-only samples were not documented in this pass; assertion kept at complement level).
- **Web-app testing on device browsers** as a secondary surface (AWS remote access "test on web browsers", Kobiton website/app manual testing) — the browser-version matrix remains the sibling Type's center.
- **Deployment postures**: public cloud farm; private/exclusive cloud pools (persistent settings); on-prem/private lab management of customer-owned devices (including air-gapped); OEM-operated free labs.
- **Access model**: on-demand slot metering vs reservation-shaped access (OEM partner program).
- **Device-family breadth**: phones/tablets as the center; TVs, watches, "other devices" (AWS wording) at the edges.
- **Manual→automation accelerators**: record-and-replay of manual sessions, Appium script generation, scriptless/no-code automation, AI test authoring; MCP/agent integrations (Claude Code-class plugins that upload builds, reserve devices, run tests, analyze results).
- **Built-in/no-script test types** (e.g., fuzz-class exploratory automation) for coverage without test code.
- **Companion suite modules**: test management, visual testing, accessibility testing, app performance testing, app distribution.

### L3 — Vendor-specific Structure (stays out of the final document)

- Brand names: Device Farm/TestGrid/remote access (AWS); App Live/App Automate/Custom Device Lab/Testing Toolkit (BrowserStack); deviceConnect/deviceShare/virtualUSB/Session Explorer/Turbo Test Execution/Appium AI/Lightning mode (Kobiton); Remote Test Lab/Partner Program/Samsung Automation Studio (Samsung).
- Catalog-size claims: 2,500+ (AWS), 30,000+ devices / 365+ models (BrowserStack) — vendor-published, fluctuate.
- Kobiton specifics: 2-second screen-load threshold flagging; supported-filetype/size list; Appium 2 beta server; obfuscation helpers; HAR export; system-latency report; air-gapped iOS device management; Lightning-mode capability filter.
- AWS specifics: S3-bucket architecture wording; device-slot purchase per device family; fuzz as the sole built-in type; Calabash framework listing; subset-of-devices remote-access policy.
- Samsung specifics: partner-program tiers, Galaxy device lineup, Tizen TV verification.

## Vendor-specific / Rejected Findings

- **"The platform must offer real physical devices only"** — rejected as L0. All sampled products anchor on real devices, but Kobiton documents virtual sessions as a complement, and the platform can operate customer-owned devices. The invariant is the *device-hardware + OS catalog*, with real physical devices the dominant realization; virtual devices recorded as common complement (L2), because no emulator-only device-testing product was directly documented in this pass (assertion deliberately weak).
- **"The platform must be a cloud SaaS"** — rejected. AWS private device lab, BrowserStack Custom Device Lab, Kobiton cloud-or-on-prem (deviceConnect, standalone, air-gapped) — the invariant is *platform-operated device access*, not vendor-owned data centers.
- **"The platform must support automated test execution"** — rejected as definitional. Samsung RTL (fetched surface) is reservation-based manual-interactive; the pre-cloud in-house lab passes the historical check without automation. Automation is the market's dominant mode (L1) and its absence marks a pole, not a different Type.
- **"Mobile phones are the boundary"** — rejected. AWS says "physical phones, tablets, and other devices"; Samsung spans phones/tablets/TV/watches. The invariant is the device catalog, with phone/tablet the market center.
- **"Device testing = browser testing on devices"** — rejected. The same vendors that sell device farms sell browser matrices as *separate products* (AWS TestGrid; BrowserStack Live/Automate). The catalog's defining axis differs (hardware+OS vs browser+version), the object under test differs (app binary vs URL), and the fleet-operations layer exists only on the device side.
- **"Test management / visual / accessibility / AI modules are part of the Type"** — rejected as definitional; they recur as separately packaged companion modules (Kobiton Test Management; BrowserStack Percy/Test Management; suite structure generally).
- **"Session Explorer-style replay is one vendor's invention"** — treated cautiously: named as such in one product, but per-run artifacts + issue grouping recur across the sample; recorded as L1 surface, not L0.

## Boundary Findings

1. **vs Browser Compatibility Testing Platform (§12 sibling — joint-review flag answered from this side)** — center-of-gravity seam, ratified. Compat centers on the *browser×version×OS matrix for web applications* (URL as input); device testing centers on the *device hardware×OS fleet for apps* (app binary as input). Evidence for the seam: AWS sells TestGrid (browser) and the device farm as separate products with separate APIs; BrowserStack sells Live/Automate (web) and App Live/App Automate (devices) as separate products. Both sides genuinely overlap at the edges (mobile-browser testing on devices; real-device clouds inside compat platforms — recorded by the sibling pass). Test: remove the browser-version matrix → the device-farm core stands; remove physical devices + app binaries → the compat core stands. Shared substrate (hosted environments, tunnels, capabilities, concurrency metering) confirmed as shared infrastructure, not a Type identity.
2. **vs Agent Tool / Computer-use Platform (§12; joint-review flag from two prior passes — answered from this side)** — same hosted-device/session substrate; different invoker and job. Here: a human tester, human-written test suites, or an agent *acting for the testing job* verify expected behavior of the customer's own app on the catalog; there: a model-driven agent decides actions at runtime to accomplish tasks. Evidence from this side: Kobiton's MCP/Claude Code integration positions the agent as *another client of the testing platform* — it "writes end-to-end tests, uploads builds, reserves real devices, runs tests, and analyzes results" — i.e., the agent consumes the testing Type's objects (builds, devices, sessions, results) rather than replacing the Type. Related Types, no merge; flag can be closed.
3. **vs End-to-end Testing Platform / Test Automation Platform (§12 siblings)** — those Types center on *authoring and managing test logic* (tests as the artifact); this Type centers on *providing device environments* (devices as the artifact; test code belongs to the customer, authored in the ecosystem's frameworks). The device platform executes the customer's suites; authoring surfaces (record/replay, scriptless, AI authoring) are newer optional extensions. Test: remove the device catalog → a test runner/authoring tool; remove framework support → a manual remote-access service.
4. **vs Software Test Management (§12)** — management organizes test cases/plans/runs as records; the device platform executes sessions/runs on devices and returns artifacts. Suites bundle both (Kobiton ships a Test Management module), confirming the seam.
5. **vs Endpoint Management / UEM and Remote Monitoring & Management (§14)** — sharpest substrate overlap outside the testing family: both remotely access and operate real devices. Distinction: UEM/RMM manage *the organization's workforce/managed endpoints* for IT operations (inventory, patching, security, support); the device testing platform provides a *catalog of test-substrate devices* (platform- or lab-owned) whose whole purpose is app QA. The "Used By/usage/device health" metadata and cleanup policies here serve test-fleet hygiene, not IT service management.
6. **vs Application Performance Monitoring / mobile observability (§14)** — monitoring observes *live production* apps on real users' devices (operational vigilance); device testing is *pre-release* verification on platform-provided devices. Per-device performance metrics captured during sessions (L1) do not change the job.
7. **vs Mobile App Development Platform (§12)** — development platforms build apps (SDKs, toolchains, build/sign); the device platform tests built binaries. Integration point: CI systems hand binaries to the device platform.
8. **vs Load/Performance Testing (§12)** — load simulates many users; here per-device performance *measurement* is an artifact of sessions, not traffic generation.

## Uncertainties

- Firebase Test Lab unreachable (2 timeouts) — the emulator+physical hybrid posture and dev-tooling-integrated packaging could not be verified from primary sources; no Firebase-dependent claims are made. The L2 "virtual devices as complement" finding rests on Kobiton's documented "Start a virtual session" surface plus market familiarity, and is deliberately worded as complement-level.
- BrowserStack App Automate internals JS-gated (this pass and sibling pass) — automation-side claims for BrowserStack kept at product-positioning level.
- Samsung RTL docs internals unreachable — reservation durations/quotas, device-state handling, and (non-)automation evidence not verified; absence of automation asserted only as "not surfaced on the fetched page".
- Catalog sizes are vendor claims that fluctuate.
- Exact concurrency/timeout numbers vary per product and plan; none asserted in the final document.
- Perfecto / enterprise-pure-play vendors not directly sampled; the enterprise pole is covered indirectly (BrowserStack Custom Device Lab, Kobiton enterprise posture, AT&T case).

## Final Synthesis

A Device Testing Platform is defined by two structures and one job: a **selectable catalog of device environments** (device hardware + OS, commonly extended with manufacturer, form factor, screen, carrier, physical location) that spans app-relevant devices teams cannot practically own or keep current; **on-demand, observable execution of the customer's application on a selected device** — realized as interactive remote-control sessions, automated parallel runs of the customer's own test suites, or both — with behavior returned as live view and artifacts (screenshots, video, logs, device metrics); and the job of **device-coverage verification** for app QA. Everything else observed — app repositories, condition simulation (location, network, biometrics, injection), debugging surfaces, CI/CD hooks, concurrency metering via slots/bundles/reservations, fleet hygiene (cleanup, health, hosts, allowlists), private/exclusive/on-prem labs, organization surfaces, result analysis and bug reporting, manual→automation accelerators, and AI-era agent integrations — is common mature structure or variant posture, not definition.
