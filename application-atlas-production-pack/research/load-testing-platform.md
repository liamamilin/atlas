# Research Notes — Load Testing Platform

Research date: **2026-09-08**
Slug: `load-testing-platform` · Directory leaf: **Load Testing Platform** (§12 Software Development & Product Engineering)

---

## Research Goal

Determine, from real products' official documentation, what a Load Testing Platform actually is and how it works: its defining core, its common mature structure, its variant space, and its boundaries against neighboring Types (End-to-end Testing Platform, Synthetic Monitoring, APM, Capacity Management, CI, Performance Testing Application).

## Initial Boundary

Working hypotheses before research:

1. **What it is**: software that simulates many concurrent users/requests against a system (usually the team's own application or API) and measures how the system behaves under that load — throughput, latency, error rate.
2. **Who uses it**: performance engineers, QA, developers, SREs.
3. **Nearest neighbors**: End-to-end Testing Platform (functional correctness, single user), Performance Testing Application (§12 sibling leaf — suspected umbrella), Synthetic Monitoring (continuous production probing), APM (observes from inside), Capacity Management (observed real demand), CI Platform (trigger shell), stress/traffic-generation one-shot tools (below the Type).
4. **Pre-hung flags**: the end-to-end-testing-platform pass (2026-09-08) pre-hung the seam "single-user correctness vs concurrency" for this leaf; the capacity-management pass recorded "observed real demand vs synthetic demand"; the browser-compatibility pass lists Load Testing as a boundary.
5. **Unknowns**: whether pass/fail performance criteria (thresholds/SLAs) are definitional or common; whether distributed injection is definitional or a scale implementation; how the sibling "Performance Testing Application" leaf relates.

## Research Questions

1. What is a simulated user (virtual user), and how is the user's behavior defined?
2. How is "load" expressed and controlled (concurrency vs arrival rate, ramp, duration)?
3. What is the object model: scenario/script, profile, injectors, results?
4. What is measured, and how are results retained and compared across runs?
5. How do functional checks (assertions) interact with load metrics (error rate)?
6. What lifecycle does a test go through (author → validate → run → monitor → analyze → compare → automate)?
7. What rules make results valid or invalid (injector capacity, GUI-vs-CLI, partial load, session state)?
8. What are the exceptions (abort-on-threshold, crashing the target, injector overload)?
9. Where exactly is the boundary to single-user testing, monitoring, and APM?

## Representative Products

Selected to span market position, product philosophy, and customer tier:

| Product | Pole | Why chosen |
|---|---|---|
| **Apache JMeter** | OSS desktop GUI, multi-protocol, de-facto standard, oldest lineage | historical anchor; thread-based user simulation; explicit functional-vs-load split |
| **Grafana k6** | modern code-first CLI + cloud execution (Grafana Cloud k6) | developer-oriented philosophy; formal executor model (closed vs open load); first-class thresholds |
| **Locust** | OSS Python code-first, distributed swarming | pure-code philosophy; real-time web UI; custom load shapes |
| **BlazeMeter** | SaaS continuous-testing platform (Perforce), cloud engines + private locations | managed cloud execution pole; SaaS concept vocabulary (engines, VUs, baselines, debug tests) |

Enterprise-protocol pole (LoadRunner/OpenText) could not be fetched (see Sources — sourcing limitation); BlazeMeter carries the enterprise/SaaS tier evidence.

## Sources

All fetched 2026-09-08. Tier-1 (official operational documentation):

- JMeter User's Manual — index: https://jmeter.apache.org/usermanual/index.html
- JMeter — Elements of a Test Plan: https://jmeter.apache.org/usermanual/test_plan.html
- JMeter — Getting Started: https://jmeter.apache.org/usermanual/get-started.html
- JMeter — Remote (Distributed) Testing: https://jmeter.apache.org/usermanual/remote-test.html
- JMeter — "Help! My boss wants me to load test our application": https://jmeter.apache.org/usermanual/boss.html
- Grafana k6 — documentation root: https://grafana.com/docs/k6/latest/
- k6 — Using k6 (concepts index): https://grafana.com/docs/k6/latest/using-k6/
- k6 — Scenarios (executors): https://grafana.com/docs/k6/latest/using-k6/scenarios/
- k6 — Thresholds: https://grafana.com/docs/k6/latest/using-k6/thresholds/
- k6 — Average-load testing: https://grafana.com/docs/k6/latest/testing-guides/test-types/load-testing/
- Locust — What is Locust?: https://docs.locust.io/en/stable/what-is-locust.html
- BlazeMeter — Documentation root: https://help.blazemeter.com/
- BlazeMeter — Getting started: https://help.blazemeter.com/docs/guide/getting-started.html
- BlazeMeter — Glossary: https://help.blazemeter.com/docs/guide/getting-started-glossary.html

Failed fetches (1–2 attempts each, then abandoned per network rules):

- OpenText LoadRunner: https://admhelp.microfocus.com/pc/ (transport error) and https://www.microfocus.com/en-us/products/loadrunner-professional/overview (timeout)
- Secondary context only (not product evidence): sibling research notes in this repo (end-to-end-testing-platform, capacity-management, api-development-workbench, digital-experience-monitoring).

> Sourcing limitation: the classic enterprise protocol-level pole (LoadRunner-class commercial suites) is evidenced only at existence level (BlazeMeter glossary mentions LoadRunner script conversion: "can convert LoadRunner HTTP to JMeter"). No LoadRunner-specific claims are made anywhere; enterprise-vendor details (Vusers, Controller, Analysis) are known from general knowledge but were NOT verified this pass and are deliberately excluded from both files. Assertions calibrated accordingly.

---

## Product A — Apache JMeter (OSS, desktop GUI, multi-protocol)

### Key observations (evidence layer A — directly observed)

- **Object model**: Test Plan → Thread Group → elements. "A minimal test will consist of the Test Plan, a Thread Group and one or more Samplers."
- **Simulated concurrency**: "Each thread will execute the test plan in its entirety and completely independently of other test threads. Multiple threads are used to simulate concurrent connections to your server application." Thread Group controls: number of threads, **ramp-up period** ("how long to take to 'ramp-up' to the full number of threads"), loop count, thread lifetime (duration, startup delay).
- **Scenario content**: Samplers (HTTP, JDBC, JMS, LDAP, FTP, TCP, Mail, OS Process, JUnit) send requests; Logic Controllers shape order/repetition; Configuration Elements (defaults, cookie/header managers); Pre/Post-Processors extract and parameterize (e.g., Regular Expression Extractor setting per-thread variables); variables/properties parameterize tests (${HOST}, ${THREADS}...).
- **Timers = pacing**: "By default, a JMeter thread executes samplers in sequence without pausing. We recommend that you specify a delay by adding one of the available timers... If you do not add a delay, JMeter could overwhelm your server by making too many requests in a very short amount of time."
- **Assertions feed the error metric**: assertions validate responses ("the server may return a successful 'HTTP Response' code, but the page may have errors on it"); "Failed Assertions... will count towards the error %age for example in the Aggregate and Summary reports."
- **Functional/load split inside the product**: Test Plan "Functional Testing" checkbox records response data — "This option should be off if you are doing stress-testing (it is off by default)."
- **Results**: Listeners collect all sample data (graph plots of response times, tree view of requests/responses, aggregate/summary reports); CLI mode writes CSV/XML (JTL) results; HTML **Dashboard Report** generated after the run; **Real-time results** via Backend Listener; results can be saved for later analysis.
- **GUI vs execution split**: "GUI mode should only be used for creating the test script, CLI mode (NON GUI) must be used for load testing"; "Don't run load test using GUI mode!" — with injector-sizing instructions (CPU/memory/network, Java heap) as a first-class step of "Load Test running".
- **Distributed injection**: one client controls many remote JMeter engines; "if you set 1000 Threads and have 6 JMeter servers, you end up injecting 6000 Threads" (multiplication, not distribution); injector placement guidance ("machines on the same Ethernet segment as your application server... minimize the impact of the network on the test results without impacting the performance of the application server itself"); "you should always check that your client is not overloaded"; node-start retries for large-scale tests.
- **The discipline ladder** (from the "boss" page): "test (low-volume — can we benchmark our application?) → benchmark (the average number of users) → load-test (the maximum number of users) → test destructively (what is our hard limit?)"; questions to ask: anticipated average/peak users; "When is a good time to load-test... bearing in mind that this may very well crash one or more of our servers?"; "Does our application have state? If so, how does our application manage it (cookies, session-rewriting...)?"
- **Authoring aid**: built-in HTTP(S) proxy recorder ("used for recording HTTP or HTTPS browser sessions").
- **Tool-positioning context**: names Apache ab (single-shot C benchmark tool) as the lower-level alternative — the flood-without-scenario lower bound.

## Product B — Grafana k6 (code-first CLI + cloud)

### Key observations (evidence layer A)

- **Positioning**: "an open-source, developer-friendly, and extensible performance testing tool... optimized for minimal resource consumption and designed for running high-load performance tests such as spike, stress, or soak tests."
- **Scenario = behavior; executor = load shape**: scripts define a default function (what each VU does); **scenarios** configure "how VUs and iterations are scheduled... model diverse workloads, or traffic patterns"; **executors**: by iterations (shared-iterations, per-vu-iterations), **by number of VUs** (constant-VUs, ramping-vus), **by iteration rate** (constant-arrival-rate, ramping-arrival-rate); explicit **open vs closed model** concepts; scenarios run in parallel with per-scenario env/tags; graceful stop; startTime sequencing.
- **Built-in metrics are the deliverable**: end-of-test summary shows http_req_duration (avg/med/min/max/p(90)/p(95), with an {expected_response:true} sub-metric), http_req_failed (rate), http_reqs (count + rate/s), iterations, vus/vus_max, data_received/sent; metric types Counter/Gauge/Rate/Trend; custom metrics supported.
- **Thresholds = pass/fail on performance expectations**: "Thresholds are the pass/fail criteria that you define for your test metrics. If the performance of the system under test (SUT) does not meet the conditions of your threshold, the test finishes with a failed status." Expressions like `http_req_failed: rate<0.01`, `http_req_duration: p(95)<200`; abortOnFail stops the run when a threshold is crossed; thresholds "codify SLOs" and "are essential for load-testing automation."
- **Checks vs thresholds**: "checks are nice for codifying assertions, but unlike thresholds, checks do not affect the exit status of k6" — combining checks (functional assertions) with a threshold on the checks rate merges functional correctness into the verdict.
- **Workload taxonomy** (testing guides): average-load ("simulates the number of concurrent users and requests per second that reflect average behaviors in the production environment"; a.k.a. day-in-life/volume test; stages: ramp-up → sustain → ramp-down; ramp-up "gives your system time to warm up or auto-scale"), stress (above-average), spike, soak, smoke. Ramp-up sizing guidance exists (5–15% of duration) — vendor advice, kept out of the canonical doc.
- **Sizing the load from production**: "Know the specific number of users and the typical throughput per process... look through APMs or analytic tools that provide information from the production environment. If you can't access such tools, the business must provide these estimations."
- **Destructiveness is expected**: "Your application and infrastructure might not be as rock solid as you think. We've had thousands of users run load tests that quickly crash their applications (or staging environments)."
- **Adjacent postures from the same script**: "Performance and synthetic monitoring: you can schedule tests to run with minimal load very frequently, continuously validating the performance and availability of your production environment. For this, you can also use Grafana Cloud Synthetic Monitoring, which supports running k6 scripts." Also browser performance testing (k6 browser API), chaos traffic, CI/CD automation, extensions for other protocols.

## Product C — Locust (OSS Python code-first)

### Key observations (evidence layer A)

- **Identity**: "an open source performance/load testing tool for HTTP and other protocols... define your tests in regular Python code."
- **Outputs**: "Throughput, response times and errors can be viewed in real time and/or exported for later analysis."
- **Simulated users**: "Locust runs every user inside its own greenlet (a lightweight process/coroutine)... write your tests like normal (blocking) Python code."
- **Scale/distribution**: "run load tests distributed over multiple machines. It is event-based (gevent)... suitable for testing highly concurrent workloads."
- **Live control**: "web interface that shows the progress of your test in real-time. You can even change the load while the test is running. It can also be run without the UI, making it easy to use for CI/CD testing."
- **Any target**: "it can be used to test almost any system or protocol. Just write a client... custom load pattern" (custom load shape).
- **Philosophy statement**: born from frustration that "existing tools used clunky interfaces or verbose configuration files"; behavior as code, version-controlled like code; name from "swarming behavior".

## Product D — BlazeMeter (SaaS continuous-testing platform)

### Key observations (evidence layer A)

- **Positioning**: "The Complete Continuous Testing Platform... Performance testing, Functional testing, API testing, API monitoring, all integrated with support for test data and service virtualization." Performance Testing module: "lets users ensure that their application servers can handle a full load of users performing various actions concurrently when an application goes live."
- **Concept vocabulary** (glossary — evidence of the SaaS object model):
  - **test / bucket / project / workspace** organization; **environment** (variables, locations, notifications, integrations); **multi-test** ("run multiple-scenario performance tests by combining existing tests").
  - **engine**: "a virtual server that generates the actual load and simulates the number of threads (virtual users) specified in the script"; runs on **Taurus** ("abstraction layer over JMeter, Grinder, Gatling, and even Selenium"; YAML/JSON); **BlazeMeter agent** in **private location** ("on-premise environment for testing... behind a firewall"); **dedicated IP**; **load origin location** and **load distribution** ("run load tests across multiple locations"); **network emulation** ("impair the connection between engine and system under test to observe the impact on KPIs").
  - **virtual user (VU)**: "an emulation of the activities performed by an actual user of the application under test"; **concurrent users**; **ramp-up** ("period of time required to start all threads (virtual users)"); **iteration**; **variable unit / VUH** usage metering (concurrency × time as the pricing substrate).
  - **KPIs**: hits per second, requests per second, **latency**, connect time, **median** (50th percentile), KB/s; **waterfall report**; **End User Experience Monitoring** ("insights into the user experience when running load tests to measure application server performance").
  - **Verdict machinery**: by default a test "marks as 'failed' if the response code returned is anything other than a 2xx code" (with an assume-success option for negative testing); **baseline comparison**: "Users select a test run as a baseline against which subsequent runs can be compared. In addition, subsequent test runs can automatically be marked as failed if the performance degrades compared to the baseline."
  - **Pre-flight validation**: **debug test** ("small-scale test, run against a logical copy of a test configuration... validate test configurations") and **low scale test run** (minimal threads, bounded duration/iterations).
  - **Live control**: **remote control** ("remotely change the value of JMeter properties in real time... change the behavior of tests that are running"); **graceful shutdown** (close, archive artifacts).
  - **Result validity**: **partial load** — "a failure to deliver the expected pressure on a system under test (SUT). This issue **invalidates** a load test because the SUT is not subjected to the intended... peak conditions. Partial load commonly occurs because a test-related engine is either defunct or fails to start."
  - **Test data**: CSV data sets, data entities/parameters (${var}), fresh values per iteration.
  - **Recorder tooling**: Chrome extension (records JMX/YML), **proxy recorder** for web/mobile.
  - **Interoperability with the enterprise pole**: ShiftLeft Converter "changes test scripts from one format into another... can convert LoadRunner HTTP to JMeter" (existence-level evidence for that pole only).

---

## Cross-product Comparison

| Structure | JMeter | k6 | Locust | BlazeMeter | Layer |
|---|---|---|---|---|---|
| Scenario of record (persistent, re-runnable definition of simulated user behavior) | Test Plan/Samplers in JMX | JS script + default fn | Python user/task code | uploaded scripts (JMeter/Taurus/Gatling/Selenium), multi-test | A ×4 |
| Simulated population control | thread count + ramp-up + loops/duration | scenarios/executors: VU-count or arrival-rate, open vs closed | number of users (swarm), spawn rate, custom shapes | engines simulating VUs, concurrent users, ramp-up | A ×4 |
| Execution against the target | CLI run vs target server | `k6 run` vs SUT | local/web-UI run vs target | cloud engines/private agents vs SUT | A ×4 |
| Performance measurements as first-class outputs | listeners, aggregate reports, HTML dashboard, real-time backend | built-in metrics: duration percentiles, error rate, req/s | real-time throughput/response times/errors, exportable | KPI reports: hits/s, rps, latency, percentiles, waterfall | A ×4 |
| Session/state handling per simulated user | cookie manager, URL rewriting, per-thread variables | cookies per VU, connection reuse | Python per-user state | per-user sessions in scripts, test data | A ×3 (B), implied elsewhere |
| Pacing / think time | timers (else "overwhelm your server") | sleep in script; iteration model | wait_time in Python | think time (SV context); script pacing | A ×3 |
| Functional checks inside the scenario | assertions → error %age | checks (+ threshold on checks rate); expected_response | Python assertions (self-made) | default fail on non-2xx; negative testing option | A ×3–4 |
| Pass/fail performance criteria | not first-class (manual analysis) | **thresholds** (SLO codification, abortOnFail) | not observed this pass | baseline comparison auto-fail; KPI criteria | A ×2 (k6, BlazeMeter) — common, not universal |
| Distributed/cloud injection | remote engines (own machines) | cloud execution (Grafana Cloud k6) | distributed master/workers | cloud engines, private locations, geo distribution | A ×4 |
| Live monitoring & mid-run control | real-time backend listener | terminal/cloud live output | web UI, change load while running | real-time reports, remote control | A ×4 |
| Small-scale validation run | Validate on Thread Group / debug options | smoke-test guidance | (small user count) | debug test, low-scale run | A ×3 |
| Run comparison / baselines | (dashboard re-runs, manual) | automated baselines (learning path) | export + external | baseline comparison with auto-fail | A ×2 (B) — common |
| CI/CD automation | CLI mode, CSV output, plugins | automated performance testing guide | headless for CI/CD | API/CI integrations | A ×4 |
| Recorders / authoring aids | HTTP(S) proxy recorder | k6 Studio (visual generator) | (none this pass) | Chrome extension, proxy recorder | A ×3 — common |
| Authoring philosophy | GUI desktop | code-first | code-first | SaaS UI over scripts | variant |
| Injection venue | own machines | local + vendor cloud | own machines + master/worker | vendor cloud + private locations | variant |
| Protocol breadth | HTTP, JDBC, JMS, LDAP, FTP, TCP, Mail... | HTTP core + extensions (+ browser) | HTTP + custom clients | whatever underlying tool supports | variant |

## Canonical Model (three-layer abstraction)

### L0 — Defining Invariant (three jointly-held structures)

1. **The load scenario of record** — a persistent, re-runnable definition of what each simulated user does: a sequence of requests/actions against the target (with sessions, parameters, data). Remove → one-shot request flood / benchmark ping with no modeled behavior.
2. **The controlled simulated population** — the definition and control of *how much* load: a population of simulated concurrent users (or an arrival/iteration rate), shaped over time (ramp, sustain, ramp-down or step/spike), for a defined duration. Remove → single-user testing (functional/E2E/API workbench territory); the concurrency IS the "load" in load testing.
3. **Execution against the target system producing performance measurements of that system under load** — the platform runs scenario × population against the target and measures the target's behavior — throughput, response time, error rate as first-class aggregated outputs — retained as a result set for analysis and comparison across runs. Remove → traffic generator; or a proxy that perturbs but measures nothing.

Jointly-held is load-bearing:
- 1+3 without 2 = single-user latency measurement / functional test with timing.
- 1+2 without 3 = load generation without measurement (stress flood).
- 2+3 without 1 = patternless request hammering (health-check/benchmark territory).
- 1 alone = a script; 2 alone = a knob; 3 alone = monitoring.

### L1 — Common Mature Structure (evidence B: cross-product commonality)

- Session/state handling per simulated user (cookies, session ids, correlation/extraction of dynamic values, per-user variables).
- Parameterization and test data (CSV/entity data, per-iteration fresh values).
- Pacing/think time between steps; iteration and duration controls.
- Functional checks woven into the scenario feeding the error metric (assertions; non-2xx default failure).
- Pass/fail performance criteria (thresholds/SLAs on latency percentiles and error rates; baseline comparison with auto-fail) — dominant in modern/cloud products, not present as first-class in the classic desktop pole.
- Distributed or cloud load injection (multiple engines/injectors; geographic locations; private/on-prem agents).
- Real-time monitoring during the run and mid-run control (change load, stop, remote properties).
- Small-scale validation run before the real load (debug/smoke).
- Run history with comparison to baselines and goals; reporting dashboards (percentiles, per-request breakdowns, waterfalls).
- CI/CD attachment (headless/CLI execution, exit-status verdicts, APIs).
- Recorders/authoring aids (proxy recording, script generation, visual builders).
- Injector capacity management as a user responsibility (sizing, monitoring the generator itself).

### L2 — Variant / Optional Structure

- Authoring philosophy: GUI desktop editor vs code-first script vs SaaS visual/recorded vs YAML abstraction layers.
- Injection venue: local machine / self-managed fleet / vendor cloud engines / private on-prem locations.
- Load model: closed (fixed VU population) vs open (arrival rate) — both are realizations of the same leg.
- Protocol breadth: HTTP-centric vs multi-protocol vs extension/custom-client.
- Workload-type taxonomy as packaged guidance (average/peak/stress/soak/spike/smoke; benchmark→load→destructive ladder).
- Browser-level load generation (real browsers in the load mix) vs protocol-level simulation.
- Continuous/automated posture (scheduled regression performance tests in pipelines) vs project/pre-release posture.
- Network emulation, geo-distribution, dedicated IPs.
- Vertical realizations (e.g., storage workload generation products exist — observed indirectly at existence level in sibling research; not asserted further).
- Companion capabilities sold alongside: API monitoring, service virtualization, test data management, server-side experience monitoring during tests.

### L3 — Vendor-specific (research notes only)

- JMeter: JMX format, Thread Group/Sampler/Listener/Timer element names, Backend Listener, Stripped sample-sender modes, heap defaults, RMI/SSL keystore details.
- k6: executor names (shared-iterations, constant-arrival-rate...), gracefulStop, abortOnFail/delayAbortEval, xk6 extension/disruptor mechanism, k6 Studio, quickpizza demo target.
- Locust: gevent/greenlet machinery, custom load shape API, locust-plugins ecosystem.
- BlazeMeter: Taurus, "engine"/"bucket"/"workspace" terms, VU/VUH credit metering, ShiftLeft converter, End User Experience Monitoring module, JTL size limit, debug-test/low-scale free tier.

## Vendor-specific Findings

- k6's thresholds are a product feature (metric-expression pass/fail with abortOnFail); BlazeMeter implements the same function via baseline-comparison auto-fail and non-2xx default failure; JMeter has no first-class performance pass/fail (results analysis is manual). → The *concept* (judging a run against performance expectations) is L1-common; any specific mechanism is L3.
- JMeter's remote testing multiplies rather than distributes the thread count per server — implementation detail of one product; the general concept (aggregate population across injectors) is the invariant.
- BlazeMeter's "partial load" invalidation concept is vendor-articulated but plainly generic (any product's failed injector corrupts results); kept as behavior, wording neutralized.

## Rejected Findings (considered and NOT promoted)

- "Percentile latency reporting is definitional" — rejected: JMeter-class tools predate percentile-first dashboards; aggregates/medians satisfy. Percentiles are the modern dominant form (L1).
- "Thresholds/SLA verdicts are definitional" — rejected: classic desktop pole performs analysis without first-class pass/fail; verdict machinery is L1. What IS definitional: measurements retained as results that can be judged.
- "Distributed injection is definitional" — rejected: single-machine load generation satisfies the Type at small scale; distribution is the scale implementation (L1).
- "Browser-based user simulation is definitional" — rejected: protocol-level request simulation is the dominant and older form; browser-in-the-loop is a variant.
- "Code-defined scenarios are definitional" — rejected: GUI-built and recorded scenarios (JMeter, BlazeMeter) are equally valid realizations; the invariant is the persistent re-runnable scenario, not its format.
- "CI integration is definitional" — rejected: pre-CI-era tools satisfy the core; automation is L1.
- "Cloud SaaS delivery is definitional" — rejected: desktop OSS tools satisfy.

## Boundary Findings

1. **vs End-to-end Testing Platform** (§12 sibling, processed 2026-09-08 — ANSWERS that pass's pre-hung seam "single-user correctness vs concurrency"): both author persistent re-runnable scenarios against the team's own application, but the deliverables differ structurally. E2E: per-test functional verdicts for one user's journey; verdict per test. Load: measured behavior of the system under a *controlled population*; the deliverable is the performance result set (throughput/latency/errors), with per-user functional correctness relevant mainly as error counting. The seam is exactly the load-profile leg (L0 #2). Evidence: JMeter ships both postures in one product and explicitly separates them ("Functional Testing" checkbox "should be off if you are doing stress-testing"; GUI for building, CLI for load); k6 separates checks (functional) from thresholds (performance) and marks the load-posture doc pages (test types) distinct from functional testing. Keep-both; confirmed from this side.
2. **vs Synthetic Monitoring** (§14, unprocessed): same mechanics (scripted requests, assertions, scheduling) but opposite perturbation posture and loop. Load platform: deliberately heavy load against test/staging targets (destructive risk is documented: "may very well crash one or more of our servers"; k6 warns tests "quickly crash their applications (or staging environments)"), verdict = performance under load. Synthetic monitoring: minimal-load scheduled probes against production for availability/broken-experience detection. Direct evidence of the seam from the vendor's own split: k6 offers "performance and synthetic monitoring" by scheduling *minimal-load* runs of the same script and hands production monitoring to Grafana Cloud Synthetic Monitoring (a different product); BlazeMeter separates API Monitoring (continuous, public/private agents) from Performance Testing (load). Same script, different loop and risk posture → different Types.
3. **vs APM** (§12, processed 2026-09-06): APM observes from inside the application's runtime; load platform generates traffic and measures from the client/protocol side. Complementary and explicitly linked: k6 tells users to take production numbers "from APMs or analytic tools"; BlazeMeter sells server-side experience monitoring as a companion during load tests. Generation vs observation — no overlap of defining core.
4. **vs Capacity Management** (§14, processed 2026-09-06, seam already recorded "observed real demand vs synthetic demand"): confirmed from this side — load testing *synthesizes* demand to measure the system; capacity management *observes* real demand to plan supply. No further flag.
5. **vs Continuous Integration Platform** (§12, processed 2026-09-07): CI is the change-bound trigger shell that runs load tests as jobs and consumes exit statuses/reports (consistent with the CI pass's "test tooling: triggered execution shell + report consumption"); the load lifecycle (scenario, profile, injectors, results) lives in the load platform. k6 markets CI automation as an integration, not as the product.
6. **vs Performance Testing Application** (§12 sibling leaf, **unprocessed**) — TAXONOMY FLAG: the market does not maintain "load testing" and "performance testing" as separate product categories. k6 self-describes as "a performance testing tool... for running high-load performance tests"; BlazeMeter names its load-testing module "Performance Testing"; the discipline guides (k6 test types) treat load/stress/soak/spike as performance-testing species, all population-controlled. Every product evidenced this pass that could be called a "performance testing application" is load-centric. Held this pass: **Load Testing Platform is the concrete, product-real member**; Performance Testing Application is treated as the umbrella sibling (mirror of the end-to-end-testing-platform / test-automation-platform precedent). Recommend joint review when the sibling is processed; candidate outcomes: alias/umbrella consolidation, or keep-both with a scope seam if non-load performance methods are documented then.
7. **vs traffic generators / benchmark one-shots** (below the Type): a single-shot request flood or benchmark ping (Apache ab-class, named as the lower-level alternative in JMeter's own manual) lacks the persistent scenario and the result-set apparatus. Lower-bound marker, not a neighboring Type.
8. **vs browser/device compatibility platforms** (§12, processed): those sell *environment catalogs* (browser/device × version) for functional/visual verification; this Type sells load generation + performance measurement. Consistent with both passes' records.

## Historical / Market-Sample Check (§24)

- **Older products**: JMeter's own manual (a long-standing artifact of the category) satisfies the three-leg core with zero modern machinery: threads as simulated users, GUI-built test plans, CSV results, aggregate reports. No cloud, no scripting-language requirement, no CI, no percentile dashboards in the core. Definition holds.
- **Conceptual pre-digital/early form**: coordinating a fixed request sequence from many client machines/sessions against a server and timing the responses (the "benchmark → load-test" ladder articulated in JMeter's manual) satisfies the core without any specific tool era. The definition names no injection technology (threads/greenlets/cloud engines are implementations).
- **Regional/platform-native**: no geographic dependency observed; protocol-level vs browser-level poles both fit.
- **Anti-overfitting applied**: threshold verdicts, cloud injection, JS scripting, CI, percentiles — all excluded from the core despite being near-universal in the current market, each with an in-sample pole that satisfies the Type without it (or in the case of thresholds, without it *first-class*).

## Uncertainties

1. The enterprise protocol-suite pole (LoadRunner-class) could not be fetched (2 failed attempts). The Type's enterprise realization is inferred only via BlazeMeter's LoadRunner-conversion glossary entry (existence level). If that pole exposes a structurally different model (it is not expected to), the L0 may need revision. No LoadRunner claims were made.
2. Locust's pass/fail criteria machinery was not directly evidenced this pass (only outputs and CI usage); treated as "not observed" rather than "absent".
3. "Performance Testing Application" sibling leaf unprocessed — final alias/umbrella decision deferred to that pass (flag recorded).
4. Synthetic-monitoring sibling leaf unprocessed — seam #2 above is pre-hung for that pass, with this side's evidence recorded.
5. Exact vendor numbers (heap defaults, metering units, ramp-up guidance percentages, JTL limits) were observed but deliberately kept out of the final document per evidence-calibration rules.

## Final Synthesis

A Load Testing Platform is the system a software team uses to learn how its own system behaves under controlled simulated demand. Its world has three load-bearing parts: (1) a persistent, re-runnable **load scenario of record** defining what each simulated user does; (2) a **controlled simulated population** — how many concurrent users (or what arrival rate), shaped over time and sustained for a defined duration; (3) **execution against the target that yields performance measurements** — throughput, response time, error rate — retained as result sets that can be analyzed, compared across runs, and judged against performance expectations. Everything else commonly bundled (threshold verdicts, cloud engines, geo-distribution, recorders, CI gates, browser-in-the-loop, percentile dashboards) is mature market furniture, not the definition. Remove the population leg and the product is single-user testing; remove measurement and it is a traffic generator; remove the scenario and it is a flood.
