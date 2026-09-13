# Research Notes — Performance Testing Application

Research date: **2026-09-09**
Slug: `performance-testing-application` · Directory leaf: **Performance Testing Application** (§12 Software Development & Product Engineering)

---

## Research Goal

Determine, from real products' official surfaces, what a Performance Testing Application is as a product Type — and resolve the pre-hung taxonomy flag from the load-testing-platform pass (2026-09-08): is "Performance Testing Application" a distinct Type, or the discipline-level name of the same product category already documented as **Load Testing Platform**? The joint review recommended at that pass (alias/umbrella consolidation vs keep-both with a scope seam) is discharged here.

## Initial Boundary

Working hypotheses before research:

1. "Performance testing" is the name of a QA **discipline** (evaluating a system's speed, stability, scalability under workload); "load testing" is one **method** within it.
2. The sibling pass's evidence suggests every product sold under the "performance testing" name is load-centric (k6 self-description; BlazeMeter module naming).
3. Candidate scope seam to test: non-load performance methods — front-end page-load auditing (WebPageTest-class), mobile app performance, in-process profiling. If any product family sold as "performance testing" is NOT population-controlled simulated demand, a keep-both seam might exist.
4. Neighbors: Load Testing Platform (sibling leaf), End-to-end Testing Platform, Synthetic Monitoring (§14, unprocessed), APM (§12, processed), Profiler, Capacity Management (§14, processed), Continuous Integration Platform (§12, processed), Software Test Management.

## Research Questions

1. How do vendors define "performance testing" as a discipline, and which species do they enumerate?
2. Are all enumerated species population-controlled simulated demand (scenario × population-shape × duration × measurement)?
3. Do any products sold under the "performance testing" name lack the load-centric core?
4. How do vendors use the two names "performance testing" and "load testing" — interchangeably for one category, or for different categories?
5. What does the enterprise pole add (protocol breadth, SLA machinery, APM correlation, cloud injection)?
6. Where are the boundaries: E2E, synthetic monitoring, APM/profiler, capacity management, CI, test management?

## Representative Products

Selected to span market position, product philosophy, and customer tier — with deliberate weight on products whose **own naming** bears on the umbrella question:

| Product | Pole | Why chosen |
|---|---|---|
| **Grafana k6** | code-first OSS CLI + cloud execution; self-names "performance testing tool" | the naming evidence + the most formal discipline taxonomy (test-types guide) |
| **Tricentis NeoLoad** | enterprise suite (SAP/mainframe protocol coverage, agentic AI, SLA gates, cloud injection) | enterprise "performance testing" naming; page title pairs both names |
| **SmartBear LoadNinja** | SaaS scriptless, real-browser load generation | scriptless/real-browser philosophy; page title pairs both names |
| **Perforce BlazeMeter** | SaaS continuous-testing platform | product menu maps "Performance Testing" → load-testing product; explicit umbrella statement |
| **Apache JMeter** | classic OSS desktop GUI (Tier-1 evidence from sibling pass, 2026-09-08) | historical anchor |
| **OpenText LoadRunner (class)** | legacy enterprise pole | unreachable ×3 across passes; existence-level only |

## Sources

Fetched 2026-09-09 unless noted:

- Grafana k6 — documentation root: https://grafana.com/docs/k6/latest/ (Tier 1)
- k6 — Load test types: https://grafana.com/docs/k6/latest/testing-guides/test-types/ (Tier 1)
- k6 — Breakpoint testing: https://grafana.com/docs/k6/latest/testing-guides/test-types/breakpoint-testing/ (Tier 1)
- Tricentis NeoLoad — product page: https://www.tricentis.com/products/performance-testing-neoload (Tier 2)
- Tricentis NeoLoad — Migrate from LoadRunner: https://www.tricentis.com/products/performance-testing-neoload/migrate-from-loadrunner (Tier 2)
- SmartBear LoadNinja — home: https://loadninja.com/ (Tier 2)
- Perforce BlazeMeter — "Performance Testing vs. Load Testing vs. Stress Testing" (via https://www.blazemeter.com/performance-testing): https://www.blazemeter.com/blog/performance-testing-vs-load-testing-vs-stress-testing (Tier 2/3, corroborated by product-menu mapping)
- BlazeMeter Tier-1 glossary/help evidence from sibling pass (2026-09-08): https://help.blazemeter.com/
- JMeter Tier-1 user-manual evidence from sibling pass (2026-09-08): https://jmeter.apache.org/usermanual/

Failed fetches (1–2 attempts each, then abandoned per network rules):

- OpenText LoadRunner: https://www.opentext.com/products/loadrunner → HTTP 444. (Third failure across passes: admhelp.microfocus.com transport error + microfocus.com timeout in the sibling pass.) Abandoned.
- WebPageTest: https://www.webpagetest.org/ → 403; https://docs.webpagetest.org/ → 404. Abandoned.
- Tricentis operational docs: https://docs.tricentis.com/ → login/JS wall; https://docs.tricentis.com/neoload/ → login wall. NeoLoad evidence is product-page level (Tier 2), not manual level.

> Sourcing limitation: the classic enterprise suite (LoadRunner-class) remains evidenced only at existence level — via a competitor's migration page ("the Micro Focus suite of performance testing tools") and BlazeMeter's LoadRunner-conversion glossary entry (sibling pass). No LoadRunner-specific structural claims are made anywhere. The front-end web-performance niche (WebPageTest-class) could not be fetched at all; see Uncertainties.

---

## Product A — Grafana k6 (code-first OSS + cloud)

### Key observations (evidence layer A — directly observed)

- **Self-naming**: "Grafana k6 is an open-source, developer-friendly, and extensible **performance testing tool** that helps you catch performance issues early and proactively improve reliability." And: "designed for running **high-load performance tests** such as spike, stress, or soak tests." The tool's own definition of its performance-testing purpose is high-load, population-controlled testing.
- **Use list** (docs root): Load and performance testing; Browser performance testing (k6 browser API, mixable with other performance tests); Performance and synthetic monitoring (minimal-load scheduled runs — routed to a separate product, Grafana Cloud Synthetic Monitoring); Automation of performance tests (CI/CD); Chaos and resilience testing; Infrastructure testing (extensions).
- **Discipline taxonomy** (Load test types guide): "Many things can go wrong when a system is under load... To prepare for these performance risks, teams use load testing." Species enumerated: **smoke** (validate script + minimal load), **average-load** (expected normal conditions), **stress** (above average), **soak** (extended periods), **spike** (sudden short massive increases), **breakpoint** (gradual increase to find capacity limits). The cheat sheet defines every species by exactly two axes: **VUs/Throughput × Duration** — i.e., every species is a point in the population-shape space.
- **Naming instability is vendor-acknowledged**: "no consensus even exists about the names of these test types"; "The categories themselves are relative to use cases. A stress test for one application is an average-load test for another."
- **Breakpoint testing** (dedicated page): "aims to find system limits"; "also known as capacity, point load, and limit testing"; uses ramping-arrival-rate so load keeps increasing even as the system degrades; stopped manually or via threshold (`abortOnFail`); failure-point ladder: degraded performance → troublesome performance → timeouts → errors → system collapse; elasticity caveat: in elastic cloud environments the test may find "only the limit of your cloud account bill" — turn off elasticity.
- **Method guidance**: start with smoke, progress to higher loads/longer durations; simple ramp-up/plateau/ramp-down shapes; "no single test type eliminates all risk."

## Product B — Tricentis NeoLoad (enterprise suite)

### Key observations (evidence layer A at Tier 2 — product pages; operational docs behind login)

- **Page title**: "AI-driven automated **performance & load testing** tool - Tricentis NeoLoad" — both names in one title for one product.
- **Site navigation**: "Performance Testing → NeoLoad — Load and performance testing."
- **Case-study titles use the names interchangeably**: "Dell chooses NeoLoad for **SAP load testing**"; "Raiffeisen migrates Avaloq **performance testing** to NeoLoad."
- **Platform structure** (product-page diagram): AI/agentic layer (Agentic Performance Testing "APT", AI Chat, MCP) over the NeoLoad platform core (Protocol coverage, RealBrowser, Test design, Analysis, CI/CD) over an integration layer (APM, cloud providers, pipeline tools).
- **Enterprise protocol coverage**: SAP (GUI, Fiori, RFC, IDoc, S/4HANA), web/API (HTTP/S, REST, SOAP, WebSocket), enterprise apps (Oracle, Salesforce, ServiceNow, Workday, Citrix), RealBrowser (Chrome, Firefox, Edge, Salesforce Lightning, SAP Fiori), mobile (iOS/Android native/hybrid), mainframe (TN3270, TN5250/AS-400, VT terminals), messaging (JMS, MQTT, AMQP, Kafka), AI (MCP servers).
- **Protocol + browser in one test**: "Easily combine backend protocol data alongside frontend performance in a single test, so results accurately reflect what users experience"; RealBrowser "captures frontend performance alongside backend metrics."
- **Design philosophy**: "Codeless visual design, YAML as-code authoring, CLI execution... coexist as equally capable paths in a single platform"; "automated script updates that preserve parameterization, SLAs, and scenario logic."
- **Continuous posture**: "Automated go/no-go decisions validate every CI/CD commit"; "automated SLO-based pass/fail decisions across Jenkins, Azure DevOps, GitLab, and more."
- **Scale**: "Dynamic Infrastructure provisions from virtually any global location in minutes and releases resources when tests complete"; "cloud-based load generation scales to millions of virtual users on demand."
- **Analysis**: "real-time dashboards and SLA monitoring during execution"; "AI-powered analysis automatically surfaces anomalies and bottlenecks"; "cross-release trend analysis that tracks drift across every release"; "automated reports that deliver verdicts, evidence, and action items."
- **APM integration**: "Bidirectional APM integrations carry test data into production monitoring so performance visibility is continuous"; Dynatrace, Datadog, AppDynamics, New Relic, Prometheus; migration page: "One-click APM integration for bi-directional Dynatrace, AppDynamics, and New Relic data for quick analysis and pass/fail automation."
- **Migration page (LoadRunner existence evidence)**: "Organizations are increasingly finding that the **Micro Focus suite of performance testing tools**, that they've relied on for years, cannot keep pace..." — the legacy enterprise pole is named, by a competitor, as "performance testing tools." Also: "Single tool for protocol and browser-based testing"; functional-asset reuse ("One-click functional test reuse (from Tricentis Tosca, Selenium, Ranorex, and Worksoft Certify) as performance tests"); "Make performance a team sport" (broadening the user base beyond specialists).

## Product C — SmartBear LoadNinja (SaaS scriptless, real browsers)

### Key observations (evidence layer A at Tier 2)

- **Page title**: "LoadNinja | **Performance Testing and Load Testing Tool**" — both names, one product.
- **Positioning**: "Anyone on your team can **load test** with instant playback, an easy-to-use interface, and real browsers for reliable data."
- **Scriptless authoring**: InstaPlay Recorder — "create web and API load tests in minutes. No coding is required... if you know how to use your web app, you can load test with LoadNinja."
- **Real browsers as the load**: "Your end users use real browsers. So you should test on real browsers... it uses real browsers to provide the most realistic representation of load on the infrastructure. No maintaining or setting up load emulators."
- **Correlation eliminated**: "Manual correlation can be complicated and very time-consuming... Let your browsers handle the load and create complex performance tests without complex correlation."
- **Diagnosis**: "Diagnose performance issues in your web apps and APIs in real time... browser-based navigation timings that developers and performance testers are used to."
- **Continuous posture**: "Incorporate continuous performance testing into your deployment schedule... parameterizing tests, then automating them using our public REST API or custom CI/CD plugins."
- **Feature set**: Record and Playback Scripts; Load Test with Real Browsers; Analyze Performance Results; Load Test Internal Applications (private apps from cloud load generators).

## Product D — Perforce BlazeMeter (SaaS continuous-testing platform)

### Key observations (evidence layer A at Tier 2 + sibling-pass Tier-1 glossary)

- **Product-menu mapping (the sharpest naming evidence)**: the site's product navigation contains an item literally named "**Performance Testing**" whose link target is the load-testing product page (`/product/blazemeter/load-testing`). The discipline name is used as the label for the load-testing product.
- **The umbrella statement** (blog "Performance Testing vs. Load Testing vs. Stress Testing"):
  - "There are multiple types of tests that fall under the **performance testing umbrella**. For instance, load testing and stress testing are both performance testing types that check how your application performs when many people use it at once."
  - "comparing performance testing vs load testing does not make sense, since performance testing is an '**umbrella**' term for all activities including (but not limited to): Load Testing. Stress Testing. Soak Testing (also called Endurance Testing). Spike Testing. And more. Therefore, **load testing is only a part of performance testing**."
  - "Performance testing is a testing method that evaluates how the system behaves and performs... examines responsiveness, stability, scalability, reliability, speed, and resource usage of your software and infrastructure."
  - Comparison table: Performance Testing = "Broad evaluation of system speed, stability, and scalability" (metrics: response times, throughput, resource usage, error rates); Load = expected load; Stress = beyond limits/breaking points; Soak = long-term stability (memory leaks, degradation); Spike = sudden extreme bursts.
  - **Volume and Scalability testing** also named as performance testing types ("Volume testing examines system performance when handling large amounts of data, while scalability testing evaluates how performance changes as system resources or load increases").
  - Tool definition: "Performance testing tools are platforms that evaluate and analyze the speed, scalability, robustness and stability of the system under tests... Many such platforms can integrate with CI/CD tools."
  - KPIs: virtual users, hits per second, errors per second, response time, latency, bytes per second (throughput).
- **Sibling-pass Tier-1 glossary evidence** (2026-09-08, carried forward): engines (virtual servers generating load), VUs, ramp-up, iterations, baseline comparison with auto-fail, partial-load invalidation, debug tests/low-scale runs, private locations, Taurus abstraction layer, LoadRunner script conversion (existence-level evidence for the enterprise pole).

## Product E — Apache JMeter (classic OSS desktop; cross-pass Tier-1 evidence, 2026-09-08)

- Threads as simulated users; test plans; ramp-up; timers as pacing; assertions feeding the error percentage; GUI-for-authoring vs CLI-for-load split; distributed injection via remote engines; the benchmark → load-test → destructive-test ladder articulated in its own manual.
- JMeter's own manual uses "load testing" for the activity; the broader market routinely cites JMeter as a performance testing tool (BlazeMeter's performance-testing blog illustrates its types with JMeter screenshots). The classic pole satisfies the same three-part core with no cloud, CI, thresholds, or percentile dashboards.

## Product F — OpenText LoadRunner (class) — existence level only

- Named "the Micro Focus suite of **performance testing tools**" in NeoLoad's migration literature; BlazeMeter glossary documents LoadRunner→JMeter script conversion (sibling pass). Official documentation unreachable (3 failed fetches across two passes). No structural claims made.

---

## Cross-product Comparison

| Structure | k6 | NeoLoad | LoadNinja | BlazeMeter | JMeter (sibling) |
|---|---|---|---|---|---|
| Self-naming | "performance testing tool" | "performance & load testing tool" (title) | "Performance Testing and Load Testing Tool" (title) | menu item "Performance Testing" → load-testing product | cited as performance testing tool by the category |
| Scenario of record | JS script + scenarios | codeless/YAML-as-code projects | recorded InstaPlay tests | uploaded scripts / multi-tests | JMX test plan |
| Population control | executors: VU-count or arrival-rate, open vs closed | VUs; dynamic cloud infrastructure | browser instances as VUs, cloud | engines simulating VUs, ramp-up | threads + ramp-up |
| Species taxonomy | smoke / average-load / stress / soak / spike / breakpoint | peak-load scenarios, SLA validation (packaged guidance) | load tests, continuous posture | load / stress / soak / spike / volume / scalability | benchmark → load → destructive ladder |
| Measurement outputs | built-in metrics: duration percentiles, error rate, req/s | real-time dashboards, SLA monitoring, cross-release trends | real-time diagnosis, browser navigation timings | KPIs: hits/s, rps, latency, percentiles | listeners, aggregate reports, HTML dashboard |
| Verdict machinery | thresholds (abortOnFail) | SLO-based pass/fail CI gates | CI automation (REST API/plugins) | baseline comparison auto-fail; non-2xx default | not first-class (manual analysis) |
| Injection venue | local + Grafana Cloud | dynamic cloud infra, any global location | vendor cloud (incl. private apps) | cloud engines + private locations | own machines (remote engines) |
| Browser-in-loop | k6 browser API, mixable | RealBrowser: protocol + browser in one test | real browsers ARE the load | via underlying tools | not core |
| Protocol breadth | HTTP core + extensions | SAP/mainframe/messaging/enterprise-app suites | web + API | underlying-tool protocols | multi-protocol samplers |
| CI attachment | automation guide | native CI gates (Jenkins/Azure/GitLab) | REST API + CI plugins | CI integrations | CLI mode |
| APM correlation | sizes loads from APM production data | bidirectional APM integrations | — | EUM companion | — |
| Authoring philosophy | code-first | codeless + as-code + CLI coexist | scriptless record/replay | SaaS UI over scripts | GUI desktop |

## The Umbrella Question — Naming Evidence (joint-review core)

Direct vendor-language evidence that "performance testing" and "load testing" name **one product category**:

1. **k6** docs root: "performance testing tool... designed for running high-load performance tests such as spike, stress, or soak tests" — the tool's own definition of its performance-testing purpose is high-load, population-controlled testing.
2. **NeoLoad** page title: "AI-driven automated performance & load testing tool" — both names in one title, one product. Case-study titles use "SAP load testing" and "performance testing" interchangeably.
3. **LoadNinja** page title: "Performance Testing and Load Testing Tool."
4. **BlazeMeter** product navigation: the menu item named "Performance Testing" links to the load-testing product page. Blog: "performance testing is an 'umbrella' term... load testing is only a part of performance testing."
5. **LoadRunner-class** = "the Micro Focus suite of performance testing tools" (NeoLoad migration page, existence level).
6. **Discipline taxonomies enumerate only population-controlled species**: k6's test-types cheat sheet defines every species by VUs/throughput × duration; BlazeMeter's taxonomy (load/stress/soak/spike/volume/scalability) is likewise simulated-demand in every row. No vendor taxonomy contains a "performance testing" species that is not population-controlled simulated demand.
7. **BlazeMeter**: "load testing and stress testing are both performance testing types that check how your application performs when many people use it at once."

**Verdict of the joint review**: the discipline "performance testing" is the umbrella; its enumerated species are all population-controlled simulated-demand methods; the products sold under the discipline name are the same load-centric tooling family sold under the method name. **Performance Testing Application and Load Testing Platform name one Type** — "performance testing" is the discipline/umbrella name, "load testing" the concrete method name. No scope seam exists in the sampled market.

**Candidate seam tested and not adopted**: front-end page-load auditing (WebPageTest-class). Unreachable this pass (403/404). Even at existence level, that niche is single-page-load diagnostic/audit tooling — closer to synthetic monitoring / developer tools than to the §12 QA-discipline tooling population. The verdict does not depend on it: the §12 leaf's referent is the QA-discipline tooling, which is uniformly load-centric in the sample. Recorded as a boundary uncertainty, not asserted either way.

## Canonical Model

### L0 — Defining Invariant

The same three jointly-held structures ratified in the load-testing-platform pass, confirmed from this side:

1. **The load scenario of record** — a persistent, re-runnable definition of what each simulated user does: a sequence of requests/actions against the target (with sessions, parameters, data). Remove → one-shot flood/benchmark ping with no modeled behavior.
2. **The controlled simulated population** — how many concurrent users (or what arrival rate), shaped over time (ramp/sustain/ramp-down, step/spike), for a defined duration. Remove → single-user testing (E2E/API territory); the "load" is gone.
3. **Execution against the target producing performance measurements of that system under load** — throughput, response time, error rate as first-class aggregated outputs, retained as comparable result sets. Remove → traffic generator, or a proxy that perturbs but measures nothing.

Jointly-held is load-bearing (same decomposition as the sibling pass):
- 1+3 without 2 = single-user latency check.
- 1+2 without 3 = load generation without measurement.
- 2+3 without 1 = patternless hammering.
- The discipline umbrella adds **nothing structural**: every species the vendors enumerate is a point in the (scenario × population-shape × duration × measurement) space. The umbrella is a naming fact, not a structural one.

### L1 — Common Mature Structure (evidence layer B)

- Pass/fail performance criteria: thresholds/SLAs on latency percentiles and error rates (k6 thresholds with abortOnFail; NeoLoad SLO-based CI gates; BlazeMeter baseline auto-fail) — dominant in modern/cloud products, absent first-class in the classic desktop pole.
- Distributed/cloud injection with geographic origins and private/on-prem locations (NeoLoad dynamic infrastructure; LoadNinja cloud incl. private apps; BlazeMeter engines/private locations; k6 cloud; JMeter remote engines).
- Real-time monitoring during runs and mid-run control.
- Small-scale validation runs before real load (k6 smoke-first guidance; BlazeMeter debug tests).
- Run history, baselines, and trend comparison (NeoLoad cross-release trends; BlazeMeter baselines).
- CI/CD attachment (all sampled products).
- Recorders/authoring aids (LoadNinja InstaPlay; NeoLoad record + codeless; BlazeMeter proxy/Chrome extension; k6 Studio).
- APM correlation (NeoLoad bidirectional integrations; k6 sizes loads from APM production data).
- Browser-in-the-loop options (LoadNinja real browsers as the load; NeoLoad RealBrowser mixing protocol + browser data; k6 browser API mixable).
- Injector-capacity management as a user responsibility (sibling pass).

### L2 — Variant / Optional Structure

- Authoring philosophy: GUI desktop / code-first / scriptless-recorded / YAML-as-code — NeoLoad documents codeless, as-code, and CLI "coexist[ing] as equally capable paths."
- Injection venue: local machine / self-managed fleet / vendor cloud / private on-prem locations.
- Protocol breadth: HTTP-centric vs enterprise protocol suites (SAP GUI/RFC/IDoc, mainframe TN3270/TN5250, messaging JMS/MQTT/Kafka, Citrix) vs browser-level.
- Posture: project/pre-release vs continuous/CI-gated ("test at least once before you release" vs "test continuously" — BlazeMeter's own waterfall/agile framing).
- Species mix as packaged guidance (which species a product leads with varies; names drift — k6: "no consensus even exists about the names").
- AI/agentic analysis overlays (NeoLoad APT/AI Chat; BlazeMeter AI positioning) — current-market add-on.
- Network emulation, chaos-traffic mixing, service virtualization companions.

### L3 — Vendor-specific (research notes only)

- k6: executor names (shared-iterations, constant-arrival-rate...), abortOnFail, xk6 extensions/disruptor, k6 Studio, quickpizza demo target, Grafana Cloud k6 vs Synthetic Monitoring product split.
- NeoLoad: Agentic Performance Testing (APT), AI Chat, MCP workflows, RealBrowser (branded), Dynamic Infrastructure (branded), Solex SAP certification, Tosca/qTest/Selenium/Ranorex/Worksoft functional-asset reuse, "expert level in three days of training," "60-75% faster maintenance" claims.
- LoadNinja: InstaPlay Recorder (branded), "no correlations" positioning, SmartBear support/docs portal.
- BlazeMeter: Taurus, engines/buckets/workspaces vocabulary, VUH credit metering, ShiftLeft converter, End User Experience Monitoring module, "two million VUs from 56 locations" marketing numbers.
- JMeter: JMX format, Thread Group/Sampler/Listener/Timer element names, Backend Listener.

## Vendor-specific Findings

- The umbrella statement itself ("performance testing is an umbrella term; load testing is only a part of it") is BlazeMeter-blog-articulated, but the same structure is independently visible in k6's test-types guide (species all population-controlled, names acknowledged as non-consensual) and in the title/menu pairing at NeoLoad and LoadNinja. The umbrella *concept* is cross-product; each vendor's species list and labels differ.
- NeoLoad's "single tool for protocol and browser-based testing" and LoadNinja's "real browsers as the load" are opposite resolutions of the same variant axis (protocol-level vs browser-level simulation) — variant, not core.
- k6's elasticity caveat for breakpoint tests (auto-scaling targets may reveal "only the limit of your cloud account bill") is vendor guidance reflecting a generic property (elastic targets confound limit-finding); kept as behavior with neutral wording in the final document.

## Rejected Findings (considered and NOT promoted)

- "Performance Testing Application is a distinct Type covering non-load performance methods" — REJECTED: every evidenced product under the name is load-centric; the vendors' own discipline taxonomies enumerate only population-controlled species; no scope seam found in the sampled market.
- "Front-end page-load auditing belongs under this leaf" — NOT ADOPTED: primary sources unreachable (403/404); the niche is single-page-load diagnostics closer to synthetic monitoring/dev-tools; recorded as uncertainty, not asserted either way.
- "AI/agentic analysis is definitional" — rejected: current-market overlay (L2/L3).
- "Browser-level load generation is definitional" — rejected: protocol-level is the older and dominant form; browser-in-loop is a variant axis with both poles in-sample.
- "Enterprise protocol breadth is definitional" — rejected: HTTP-centric OSS poles satisfy the Type fully.
- "Any specific species list (load/stress/soak/spike) is definitional" — rejected: names drift by vendor admission; the invariant is the scenario × population × measurement space, not the taxonomy labels.

## Boundary Findings

1. **vs Load Testing Platform (§12 sibling, processed 2026-09-08) — SAME TYPE. The joint-review flag is discharged.** The market does not maintain two product categories. Evidence: (a) vendor page titles pairing both names for one product (NeoLoad, LoadNinja); (b) a vendor product-menu item named "Performance Testing" linking to the load-testing product (BlazeMeter); (c) discipline taxonomies enumerating only population-controlled species (k6, BlazeMeter); (d) case-study titles using the names interchangeably (NeoLoad). The two directory leaves name one Type at two levels of speech: "performance testing" = the discipline/umbrella name; "load testing" = the concrete method name all evidenced products realize. **Recommendation recorded in STATUS.md Boundary Issues: alias/umbrella consolidation** (Load Testing Platform is the concrete product-real member; this leaf is its discipline-level name). This document is written to stand alone and to remain true under either directory outcome.
2. **vs End-to-end Testing Platform** — the concurrency leg is the seam (ratified in the sibling pass; confirmed): E2E = single-user journey verdicts; this Type = controlled population + performance result set.
3. **vs Synthetic Monitoring (§14, unprocessed)** — perturbation posture and loop: deliberately heavy load against test/staging targets (destructive risk documented in-category) vs minimal-load scheduled production probes. Vendor-drawn evidence: k6 routes production monitoring to a separate Synthetic Monitoring product; BlazeMeter splits API Monitoring from Performance Testing. Seam pre-hung for that pass with this side's evidence.
4. **vs APM / Profiler** — generation vs observation. NeoLoad's bidirectional APM integrations make the complementarity explicit (test data flows to APMs; APM production data sizes tests). k6: take production numbers "from APMs or analytic tools" (sibling pass). No overlap of defining core.
5. **vs Capacity Management (§14, processed)** — synthesized demand vs observed real demand (ratified; consistent).
6. **vs Continuous Integration Platform (§12, processed)** — CI is the trigger shell consuming exit statuses/reports; the performance lifecycle lives here (consistent with the CI pass's test-tooling seam).
7. **vs Software Test Management** — governance of test assets/cycles vs the performance tooling itself; NeoLoad integrates with qTest (test management) as a separate product.
8. **vs stress/soak/spike "tools"** — species, not Types; no separate product categories exist for them (vendor taxonomies treat them as configurations of the same tooling).
9. **vs traffic generators / benchmark one-shots** — below the Type (no persistent scenario, no result-set apparatus); lower-bound marker (sibling pass).

## Historical / Market-Sample Check (§24)

- **Older products**: the LoadRunner-class enterprise suites (1990s lineage) are named "performance testing tools" in current migration literature; JMeter (2000s desktop) satisfies the three-leg core with no cloud/CI/thresholds/percentiles. The umbrella reading is era-stable: "performance testing" has named this same load-centric tool family across its history.
- **Species-name drift is vendor-acknowledged** (k6: "no consensus even exists about the names of these test types"; breakpoint = "capacity, point load, and limit testing") — the definition must not freeze any species list; the invariant is the (scenario × population × measurement) space.
- **Regional/platform-native**: no geographic dependency observed; protocol-level and browser-level poles both fit.
- **Anti-overfitting applied**: threshold verdicts, cloud injection, AI analysis, browser-in-loop, enterprise protocol breadth — all excluded from the core despite near-universal presence in the current market, each with an in-sample pole satisfying the Type without it.

## Uncertainties

1. LoadRunner official documentation unreachable (3 failed fetches across two passes: admhelp transport error, microfocus timeout, opentext 444). The enterprise pole is evidenced at existence level only (competitor migration page + conversion glossary). If its model differed structurally (not expected), the L0 would need revision. No LoadRunner-specific claims made.
2. WebPageTest (front-end web-performance niche) unreachable (403 root, 404 docs). Whether that niche self-describes as "performance testing" and whether it would resist the load-centric umbrella could not be verified from primary sources. The verdict does not depend on it (the §12 leaf's referent is the QA-discipline tooling population, uniformly load-centric in sample). Boundary uncertainty recorded.
3. NeoLoad operational documentation behind a login/JS wall; product pages (Tier 2) used. NeoLoad's scenario/VU mechanics are asserted at product-page level, not manual level.
4. LoadNinja evidence is Tier-2 (marketing pages); its support/docs portal was not fetched. Structural claims (record, real browsers, CI) are consistent with the category and the sibling pass's evidence, but no manual-level detail asserted.
5. BlazeMeter's umbrella statement is a blog post (Tier 2/3), corroborated by the product-menu mapping and by k6's independent taxonomy — but it is not a Tier-1 manual statement.

## Final Synthesis

"Performance Testing Application" is the **discipline-level name** of the product Type whose concrete realization is the load-centric tooling family documented as Load Testing Platform. The discipline — evaluating a system's speed, stability, and scalability under workload — is practiced through population-controlled simulated-demand species (load, stress, soak, spike, volume/scalability, breakpoint/capacity, smoke), and every product sold under the discipline name in the researched sample realizes the same three-part core: a persistent re-runnable **scenario of record**, a **controlled simulated population**, and **measured execution** producing comparable performance result sets. The two directory leaves (Load Testing Platform, Performance Testing Application) therefore name one Type; **alias/umbrella consolidation is recommended**, with this document written to stand alone under either directory outcome.
