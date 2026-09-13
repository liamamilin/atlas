# Research Notes — Synthetic Monitoring

## Research Goal

Determine what a Synthetic Monitoring application is as an Application Type: its defining core, its standard capability set, its variants, and its boundaries against the neighboring monitoring Types (Digital Experience Monitoring, Metrics Monitoring, Network Monitoring, Infrastructure Monitoring, APM, Observability Platform) and the neighboring testing Types (End-to-end Testing Platform, Load Testing Platform).

Counterparty obligations carried into this pass (pre-hung flags to discharge):

- `digital-experience-monitoring` (§14, processed 2026-09-08) flagged a JOINT REVIEW: "the two Types share the consumer-side measurement skeleton (simulated interactions from vantage points satisfy DEM's measurement core); proposed seam from the DEM side — products centered on the probe machinery (monitor/script authoring, scheduling, assertions as the whole center) → Synthetic Monitoring; products centered on the unified service-experience picture, especially with the real-user posture → DEM."
- `metrics-monitoring` (§14, processed 2026-09-08) pre-hung: "producer-vs-series-layer: probes generate the measurements this Type consumes."
- `network-monitoring` (§14, processed 2026-09-09) pre-hung: "network monitoring uses active probes as one collection method with the network as object; synthetic's center is probe machinery against user-facing services — object differs, not technique."
- `end-to-end-testing-platform` (§12, processed 2026-09-08) pre-hung: "same journey mechanics, different loop: pre-release change-linked verdicts in test environments vs continuous production availability."
- `load-testing-platform` (§12, processed 2026-09-08) pre-hung with vendor evidence: "same script mechanics, opposite perturbation posture and loop (deliberately heavy load against test/staging targets vs minimal-load scheduled production probes; k6 routes production monitoring to its separate Grafana Cloud Synthetic Monitoring product; BlazeMeter splits API Monitoring from Performance Testing)."
- `performance-testing-application` (§12, processed 2026-09-09) carried the same seam forward.

## Initial Boundary (hypothesis before research)

- Synthetic monitoring is likely: software systems that continuously execute simulated interactions (HTTP requests, API calls, scripted user journeys) against user-facing services from measurement points outside the monitored system, on a schedule, evaluating results against expectations and alerting on failure.
- The market's own naming is layered: the simple pole is marketed as "uptime monitoring" / "availability monitoring"; the deep pole as "synthetic monitoring" (scripted browser/API journeys); "transaction monitoring" names the multi-step middle. Pingdom literally nests Uptime Monitoring, Page Speed, and Transaction Monitoring under a "Synthetic Monitoring" product umbrella.
- Likely confusions: DEM (shares the consumer-side measurement skeleton), uptime checking (is the simple pole the same Type?), E2E testing (same journey mechanics), load testing (same script engines), network monitoring (same probe techniques), metrics monitoring (results become series).
- Open questions going in: (1) is "simulated user behavior" definitional, given ping/port checks simulate no user? (2) is alerting definitional? (3) is the cloud/managed-probe-fleet model definitional, given private-probe poles? (4) where exactly does the check end and the test begin?

## Research Questions

1. What objects exist inside a synthetic monitoring system? (checks/monitors, steps/scripts, assertions, vantage points/probes, runs/results, alerts, dashboards, status pages)
2. What check types exist and what spectrum do they span? (network-level → protocol-level → multi-step API → scripted → browser/mobile)
3. How do checks execute? (scheduling, per-vantage-point independence, retries, on-demand runs)
4. How are results evaluated and surfaced? (pass/fail verdicts, response measurements, history, waterfalls/screenshots, uptime percentages)
5. What is the alerting loop? (failure confirmation, notification channels, maintenance windows)
6. How do results relate to other telemetry? (metrics/logs publication, APM trace correlation)
7. How is the check population managed? (UI vs monitoring-as-code, versioning, environments, CI/CD)
8. Where are the exact seams: vs DEM, vs metrics/network/infrastructure monitoring, vs E2E/load testing, vs status pages?

## Representative Products

Selection rationale: market representation across the poles of the category (pure-play enterprise, observability-suite module, OSS-lineage cloud, dev-first platform, classic SMB/consumer, minimal availability pole), documentation completeness, different product philosophies, different customer layers.

| Product | Pole | Customer layer | Evidence accessed |
|---|---|---|---|
| Grafana Cloud Synthetic Monitoring | OSS-lineage cloud (blackbox_exporter + k6) | Grafana Cloud users, SRE | grafana.com docs (introduction, check types) |
| Checkly | Dev-first platform (Playwright, monitoring-as-code) | modern engineering teams | checklyhq.com docs (what-is, concepts/checks) |
| Datadog Synthetics | Observability-suite module | enterprise + mid-market | docs.datadoghq.com/synthetics |
| Pingdom (SolarWinds) | Classic SMB/consumer; "Synthetic Monitoring" umbrella over uptime/page-speed/transaction | web/e-commerce teams, agencies | pingdom.com product pages |
| UptimeRobot | Minimal availability-check pole | individual developers, SMB | uptimerobot.com (FAQ, product pages) |
| Catchpoint (now LogicMonitor) | Pure-play enterprise pole | enterprise IT | logicmonitor.com/catchpoint/synthetic-monitoring (Catchpoint acquired by LogicMonitor; page fetched via redirect) |

Corroborating cross-references from the DEM pass (2026-09-08): Dynatrace Synthetic monitors (HTTP/browser/NAM; execute on demand at selected locations), Datadog Synthetics, ThousandEyes web-layer tests (Page Load, Transactions with scripting, waterfalls, screenshots).

## Sources

Fetched 2026-09-09:

- Grafana Cloud docs — Synthetic Monitoring introduction: https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/introduction/
- Grafana Cloud docs — Check types: https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/create-checks/checks/
- Grafana Cloud docs — Synthetic Monitoring hub: https://grafana.com/docs/grafana-cloud/testing/synthetic-monitoring/
- Checkly docs — What is Checkly: https://www.checklyhq.com/docs/what-is-checkly/
- Checkly docs — What are Checks: https://www.checklyhq.com/docs/concepts/checks/
- Checkly docs — Documentation index: https://www.checklyhq.com/docs/
- Datadog docs — Synthetic Testing and Monitoring: https://docs.datadoghq.com/synthetics/
- Pingdom — Synthetic Monitoring product page: https://www.pingdom.com/synthetic-monitoring/
- Pingdom — Uptime Monitoring product page: https://www.pingdom.com/product/uptime-monitoring/
- UptimeRobot — homepage/FAQ: https://www.uptimerobot.com/
- LogicMonitor (Catchpoint) — Synthetic Monitoring: https://www.catchpoint.com/synthetic-monitoring (redirects to https://www.logicmonitor.com/catchpoint/synthetic-monitoring)

Notes on sourcing:

- Catchpoint's own domain now serves LogicMonitor-branded pages ("Synthetic Monitoring by Catchpoint | LogicMonitor"); the pure-play pole is evidenced through the acquirer's product page. The DEM pass (2026-09-08) could not reach Catchpoint at all; this pass reached it via the LogicMonitor surface.
- Pingdom evidence is from product/marketing pages (Tier 2), not the help center; operational details (exact intervals, location counts) are quoted only where the vendor page states them and are kept in research notes, not asserted as Type-level facts.
- UptimeRobot evidence is from the homepage FAQ (Tier 2); plan-tier interval numbers are product-specific and kept out of the final document.
- No third-party historical reference was fetched; historical claims below are marked as low-precision inference.

## Product A — Grafana Cloud Synthetic Monitoring

### Key observations (evidence layer A — directly observed)

- **Self-definition**: "a black box monitoring solution provided as part of Grafana Cloud... assess your systems' availability, performance, and correctness by emulating user behavior from global probe locations." "Each execution of a check simulates a single user performing a single iteration from one location. This ensures consistent, lightweight monitoring that reflects real-world access patterns and allows for alerting and predictable scheduling."
- **Check as the central object**: "checks are tests that run on selected public or private probes at frequent intervals to continuously verify your systems."
- **Check types**: Ping (ICMP), HTTP/HTTPS (uptime + latency; SSL version/certificate-expiry/redirect options), k6 scripted checks (JavaScript workflows and validations), k6 browser checks (headless browser; web-based user flows; Web Vitals), MultiHTTP (multiple URLs in one check; results of one request usable in later ones; several assertions per request), DNS (resolution + validation against a specific server/response kind), TCP (connection to host/port), Traceroute (path from probes to targets, visualized over time).
- **Common check options**: enabled, job name, target, probe locations, frequency (documented range 10–3600 seconds), timeout (1–60 seconds), custom labels. Job name + target uniquely identify a check.
- **Probes**: "the agents responsible for emulating user interactions and collecting data from your specified targets across different global locations." Public probes = managed instances of the open-source Synthetic Monitoring Agent operated by Grafana Labs; private probes = customer-installed. "Each selected probe executes the check independently at every scheduled interval. The probes don't rotate or take turns." Execution count scales with probe count (billing consequence). Concurrent arrivals from different locations documented as a design consideration for targets.
- **Results**: saved as Prometheus metrics and Loki logs; common metrics `probe_duration_seconds`, `probe_success`, `sm_check_info`; system labels `config_version`, `instance`, `job`, `probe`. Metrics/logs published directly to the Grafana Cloud account for troubleshooting.
- **Alerting**: "Use Synthetic Monitoring to leverage Prometheus-style alerting to ensure if a check fails, alerts are making their way to the right people through the right notification method"; default alerting via Grafana Alerting/Alertmanager.
- **Configuration as code**: UI, API, Terraform, Grizzly.
- **Built on Prometheus blackbox exporter** (stated lineage).

## Product B — Checkly

### Key observations (evidence layer A)

- **Self-definition**: "an Application Reliability platform that enables teams to test, monitor, and observe their web applications, APIs, and other services using a developer or agentic workflow." Three capability layers: Detect (Testing, Uptime Monitoring, and Synthetic Monitoring with Playwright), Communicate (alerting, dashboards, status pages), Resolve (tracing, AI incident analysis).
- **Check as the central object**: "Checks are automated tests that monitor your application on a schedule... Each Check represents a specific test that runs on a schedule you define, whether that's a simple health check on an API endpoint or a complex, multi-step workflow through your entire application. Checks experience your application the same way real users would—clicking buttons, making API calls, filling forms, or connecting to services."
- **Check-type spectrum** (the product itself splits simple "monitors" from scripted "checks"): URL Monitors (HTTP/HTTPS availability/performance/SSL), TCP Monitors, Heartbeat Monitors ("Instead of actively testing your service, Heartbeat Monitors wait to receive a signal from your system" — reverse direction), DNS Monitor, ICMP Monitor, API Checks (setup/teardown scripts, complex assertions, custom request handling), Multistep Checks (Node.js scripts, multiple API requests in sequence with arbitrary code between), Browser Checks (headless browser via @playwright/test; navigate, screenshot, assert; mobile device emulation), Playwright Check Suites ("Run entire Playwright test suites and projects as production monitors without code rewrites... Converting existing E2E tests into monitoring").
- **Execution loop** (documented step-by-step): cron process picks up the check per schedule → validates not already in progress → queued to the next configured data-center location → setup script → check → teardown script → result stored in central database → on failure, retry strategy executes (setup/teardown re-run) → alerts sent only when the sequence completes and the final attempt failed ("no alerts sent for the initial attempts").
- **Use cases spanning the test/monitor loop**: Pre-Production Testing ("Validate functionality and performance in staging before deployment, catching regressions early") and Production Monitoring ("Continuously monitor critical user journeys, API endpoints, and application performance") are both first-class; Transaction Monitoring (checkout flows, payment processing); API Reliability (third-party integrations); Multi-Environment Validation; Compliance and SLA Monitoring.
- **Monitoring as Code**: "All check types at Checkly have a Construct or API endpoint... version control your monitoring logic, collaborate on it through code reviews, and deploy monitoring changes through the same CI/CD pipelines you use for application code."
- **Audience**: DevOps/SRE teams, full-stack engineering teams; "shift monitoring left."

## Product C — Datadog Synthetics

### Key observations (evidence layer A)

- **Self-definition**: "Synthetic tests allow you to observe how your systems and applications are performing using simulated requests and actions from around the globe... in a controlled and stable way, alerting you about faulty behavior such as regressions, broken features, high response times, and unexpected status codes."
- **Test types**: API tests at network layers — HTTP, SSL, DNS, WebSocket, TCP, UDP, ICMP, gRPC — single or chained (multistep API tests); browser tests ("monitor how your customers experience your webpages end-to-end from around the world"); mobile application tests (iOS/Android end-to-end from different device types); network path tests (TCP/UDP/ICMP with packet-route visualization).
- **Organization**: Test Suites ("organize multiple tests into logical collections grouped by user journey, environment, location, service, or team"); version history (run a previous version, restore, clone); test coverage tracking.
- **Locations**: managed locations + private locations ("monitor internal APIs and websites or create custom locations in areas that are mission-critical to your business").
- **SLOs**: "Computing SLOs on your key endpoints and user journeys."
- **Correlation**: "integration between Synthetic tests and APM traces to find the root cause of failures across frontend, network, and backend requests."
- **AI/agentic generation**: Bits Testing ("explore your application, map critical user journeys, and generate Synthetic tests that cover them") and Goal-Based tests ("verify users can reach a goal using non-deterministic, agentic testing").
- **Notifications**: pre-filled monitor messages, template variables, conditional alerting.
- **Creation surfaces**: Datadog application, API, Terraform.
- **CI/CD**: Continuous Testing Explorer covers "test runs or batches of tests running in CI/CD pipelines."

## Product D — Pingdom (SolarWinds)

### Key observations (evidence layer A, product pages)

- **Umbrella structure**: the product menu's top-level category is "SYNTHETIC MONITORING" with features Uptime Monitoring, Page Speed, Transaction Monitoring, Alerting; RUM is a separate sibling product. Tagline: "Simulate visitor interaction with your site to monitor the end user experience."
- **Synthetic Monitoring page**: "Simulate visitor interaction with your website, so you and your team are the first to know if your website is slow, broken, or unavailable. Get fast and accurate outside-in monitoring 24/7." Features: availability from all over the world; load performance of critical webpages; vital site flows working as expected; alerts via email/SMS; integrations (Slack, OpsGenie, PagerDuty).
- **Uptime monitoring**: "tests the availability of your website, applications and servers"; alerts via SMS/email/webhook/push; "Before alerting you we always perform a second check on every incident... to filter out false positives"; monitoring "from over 100 locations worldwide" (vendor-stated); root-cause tooling per incident (traceroute, server output, response codes); public status pages included in all plans.
- **Transaction monitoring**: "Transaction monitoring simulates visitor interaction with your site automatically and will alert you when your critical site flows stop working correctly. Monitor both simple or highly complex transactions, such as new user registrations, user login, search, shopping cart checkout, URL hijacking, and more. Test from probe servers across the globe as often as every five minutes to once per day" (vendor-stated range).
- **Page speed monitoring**: per-page-element load performance, timeline metrics, page speed history.
- **API**: "RESTful and HTTP-based... automate the creation of uptime and transaction checks at scale and in dynamic environments."
- **Positioning**: "Complete monitoring combines real user monitoring and synthetic monitoring for ultimate visibility" — synthetic and RUM as complementary, separately named products.

## Product E — UptimeRobot

### Key observations (evidence layer A, homepage/FAQ)

- **Self-definition**: "an uptime monitoring service that continuously checks websites, APIs, and other endpoints. It alerts you when anything goes down, degrades, or changes."
- **Monitor as the central object**: "An uptime monitor is a single tool that repeatedly verifies a target webpage or service is online and working as expected. When an uptime monitor detects a problem, it instantly sends alerts... It also records incidents with timestamps and details in your dashboard so that you can track reliability over time."
- **Monitor types**: HTTP/HTTPS, Keyword (in server responses and on-page), Ping (ICMP), Port, Cron jobs/heartbeats, Website change detection, Response time, DNS changes, SSL certificates, domain expiry.
- **Multi-location**: "Verify uptime from multiple global locations to eliminate false positives... spot regional outages, routing problems, or CDN edge issues that won't show up from a single vantage point."
- **False-positive machinery**: "rechecking failures across multiple checker nodes and locations before opening an incident"; maintenance windows to suppress alerts and keep uptime statistics accurate.
- **Alerting**: personal channels (email, SMS, voice call, push) + integrations (Slack, Teams, PagerDuty, Splunk On-Call, webhooks, Zapier, API, MCP).
- **Bundled operations surfaces**: status pages (branded, real-time, incident history), incident management tools (notes, timelines, status updates), team roles/permissions, response-time threshold alerts.
- **Interval model**: plan-dependent (vendor-stated: free every 5 minutes up to enterprise every 30 seconds) — product-specific, kept out of the final document.

## Product F — Catchpoint (LogicMonitor)

### Key observations (evidence layer A, via LogicMonitor product page)

- **Market-structure fact**: Catchpoint's synthetic-monitoring URL now serves a LogicMonitor page titled "Synthetic Monitoring by Catchpoint | LogicMonitor" — the canonical pure-play has been absorbed into a broader observability platform. The page also links WebPageTest pricing (WebPageTest is part of the LogicMonitor portfolio) and a separate "RUM Monitoring" product.
- **Self-definition**: "Test performance across internal, external, and third-party Internet Stack dependencies to detect issues early and reduce incident impact."
- **Scope language**: "Monitor from single URLs to full user journeys — Validate performance across everything from simple endpoint checks to complex user journeys"; "Monitor from the largest global agent network — Validate performance from a wide range of global locations to better understand how services behave across regions, providers, and real-world conditions"; "Gain visibility across external dependencies — Understand how third-party services and providers impact performance."
- **Capability frame**: Reach / Detect / Diagnose / Analyze / Extend — global agent network coverage; proactive performance testing of APIs, applications, third-party services; alerts on latency/uptime/reachability thresholds; trace issues across service paths; correlate across dependencies; anomaly/trend analysis; custom tests and monitors; integrations.
- **FAQ (vendor-drawn seam evidence)**: "How is synthetic monitoring different from RUM? Synthetic tests simulate user interactions to catch issues proactively, while RUM captures real user data. Together, they provide full visibility and faster issue detection." "What types of tests can I run? Run API, web, transaction tests – and many more – from simple endpoint checks to full user journeys." "Can I monitor third-party services? Yes."
- **Adjacent positioning**: "Internet Health — Use global vantage points to independently validate internet outages" (Internet Performance Monitoring as a sibling capability).

## Cross-product Comparison

| Dimension | Grafana SM | Checkly | Datadog Synthetics | Pingdom | UptimeRobot | Catchpoint/LM |
|---|---|---|---|---|---|---|
| Central object | check | check | test | check (uptime/transaction/page-speed) | monitor | test/monitor |
| Check-type floor | Ping/HTTP/TCP/DNS | URL/TCP/DNS/ICMP | HTTP/SSL/DNS/TCP/UDP/ICMP/gRPC | HTTP uptime | HTTP/Ping/Port/Keyword/DNS | endpoint checks |
| Check-type ceiling | k6 browser (headless) | Playwright suites | mobile app tests | transaction (recorded flows) | keyword/change detection | full user journeys |
| Scripted checks | k6 (JS) | Node.js/Playwright | recorded + agentic | recorded transactions | no | vendor-stated breadth |
| Vantage points | public probes (managed, open-source agent) + private probes | configured data-center locations | managed + private locations | 100+ locations (vendor-stated) | multiple global locations | "largest global agent network" (vendor-stated) |
| Execution model | every selected probe runs independently each interval; no rotation | cron → queue → next location; retry strategy; alerts only after final failed attempt | scheduled + on-demand; CI batches | scheduled (vendor-stated 5 min–1 day for transactions) | scheduled intervals (plan-dependent) | continuous |
| Result storage | Prometheus metrics + Loki logs | central database | platform (metrics/explorer) | dashboard/reports | dashboard/incident records | platform |
| Alerting | Grafana Alerting | channels after retry sequence completes | monitors + conditional alerting | email/SMS/webhook; double-check before alerting | multi-channel; recheck across nodes before incident | threshold alerts |
| False-positive machinery | per-probe independence | retry strategy | conditional alerting | second check per incident | recheck across checker nodes | (not detailed on page) |
| SLO/uptime reporting | via Grafana | SLA monitoring use case | SLOs on endpoints/journeys | uptime %, status pages | uptime %, status pages | trend analysis |
| Status pages | no (Grafana ecosystem separate) | yes (Communicate layer) | no (separate Datadog products) | yes (included) | yes (bundled) | no (separate) |
| Monitoring-as-code | Terraform/Grizzly/API | constructs/CLI/API (core philosophy) | API/Terraform | REST API | API/webhooks/Zapier/MCP | API |
| CI/CD / pre-production | (DevOps provisioning) | first-class (staging + production) | CI batches + coverage | no | no | no |
| Correlation to backend | metrics/logs in same account | OTel tracing | APM trace integration | root-cause tools per incident | incident notes | trace across service paths |
| AI generation | no | "agentic workflow" positioning | Bits/Goal-Based testing | no | no | Edwin AI (platform-level) |

Evidence layer B (cross-product commonality, 6/6 sampled): a persistent named check/monitor as the unit of record; recurring scheduled execution from measurement points outside the monitored system; a spectrum from simple endpoint checks to scripted/browser journeys; assertions/expectations defining pass/fail; retained result history with availability/response-time reporting; alerting on failure with false-positive filtering machinery; multi-location execution with per-location context; API/programmatic management.

Evidence layer C (canonical inference): the Type's unit of record is the check — a persistent, re-runnable definition of a synthesized interaction — and the Type's loop is schedule → execute from vantage points → evaluate against assertions → alert on failure. "Simulated user behavior" is the ceiling of the check spectrum, not its floor; the floor is a synthesized endpoint probe. The defining property of the interaction is that the monitoring system itself generates it, on a schedule, from outside the monitored runtime.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The check (monitor) as the unit of record** — a persistent, individually identified, re-runnable definition of a synthesized interaction against a target, carrying: the target (URL/endpoint/host/record/port/flow), the interaction content (request, steps, or script), the expectations (assertions/thresholds that define success), the schedule, and the vantage-point selection. Remove → a one-off test script (E2E territory) or ad-hoc probing with no memory.
2. **Recurring execution from vantage points outside the monitored system** — the platform's managed probe fleet and/or customer-deployed probes runs each check on its schedule, without a real user and not from inside the monitored application's runtime ("black box" / "outside-in" in the market's own vocabulary). Remove → in-process instrumentation (APM) or real-user observation (RUM/DEM).
3. **The watch loop** — each run is evaluated against the check's assertions into a pass/fail verdict with response measurements, results are retained as history, and failures trigger notifications through configured channels. Remove → a scheduled traffic generator, or a data feed nobody watches.

Jointly-held is load-bearing: 1 alone = a saved test script; 2 without 1 = unanchored probing; 3 without 1+2 = alerting over nothing; 1+2 without 3 = scheduled traffic generation with no watch; 1+3 without 2 = locally-scheduled testing (drifts toward test-runner territory); 2+3 without 1 = probing with no record.

### L1 — Common Mature Structure

- **Check-type spectrum**: network-level probes (ICMP ping, TCP/port, DNS, traceroute) → protocol-level requests (HTTP/HTTPS, SSL/TLS certificate checks, WebSocket, gRPC, UDP) → multi-step API chains (results of one request feeding the next) → scripted checks (general-purpose code: k6, Node.js) → browser checks (headless browser user journeys, screenshots, Web Vitals) → mobile app tests. All six sampled products occupy the floor; the ceiling varies.
- **Assertions/expectations per check or per step**: status codes, response body/keywords, headers, certificate validity, response-time thresholds.
- **Vantage-point fleet**: managed global locations operated by the vendor + customer-deployed private probes/locations for internal targets; per-vantage-point results.
- **Result history and reporting**: per-check availability/uptime percentages, response-time trends, per-run detail (step timings, waterfalls, screenshots, error output).
- **Alerting machinery with false-positive filtering**: retries/second-checks/multi-node corroboration before opening an incident; notification channels (email/SMS/chat/pager integrations/webhooks); maintenance windows to suppress expected downtime.
- **SLO/uptime computation** on checks and journeys (explicit in Datadog, Checkly use cases, Grafana ecosystem; uptime % universal).
- **Programmatic management**: API everywhere; monitoring-as-code (Terraform/CLI/constructs) in the dev-first and platform poles.
- **Correlation hooks** toward backend telemetry (metrics/logs publication, APM trace integration, per-incident root-cause tools).
- **Status pages** as a bundled or sibling communication surface (Pingdom, UptimeRobot, Checkly bundle; Grafana/Datadog leave it to sibling products).

### L2 — Variant / Optional Structure

- **Depth of the journey ceiling**: recorded clickpaths (Pingdom transactions) vs code-first Playwright suites (Checkly) vs recorded mobile tests (Datadog).
- **Reverse-direction checks**: heartbeat/cron monitors where the monitored system checks in with the monitor instead of the monitor probing (Checkly Heartbeat, UptimeRobot cron/heartbeat) — a dead-man's-switch pattern inside the same products.
- **Pre-production posture**: running the same checks against staging environments and in CI/CD pipelines (Checkly first-class; Datadog CI batches) — the bridge toward testing territory.
- **Third-party/dependency emphasis**: monitoring external providers and the "Internet Stack" (Catchpoint/LM positioning).
- **Network-path elaboration**: traceroute checks, packet-route visualization (Grafana, Datadog, Pingdom per-incident traceroute).
- **AI/agentic test generation** (Datadog Bits/Goal-Based; Checkly agentic positioning; LogicMonitor Edwin AI at platform level) — era-current.
- **Packaging**: standalone availability service (UptimeRobot, Pingdom) vs observability-suite module (Datadog, Dynatrace per DEM pass) vs dev-first platform (Checkly) vs OSS-lineage cloud (Grafana) vs pure-play absorbed into a platform (Catchpoint→LogicMonitor).
- **Audience**: web/e-commerce/marketing teams (Pingdom pole) vs SRE/engineering (Checkly/Grafana/Datadog) vs enterprise IT/NOC (Catchpoint).
- **Deployment**: SaaS-managed probes vs customer-hosted private probes vs (conceptually) fully self-hosted open-source agents.

### L3 — Vendor-specific (research notes only)

- Grafana: `probe_success`/`probe_duration_seconds`/`sm_check_info` metric names; frequency range 10–3600 s and timeout 1–60 s (documented); job/target as check identity; billing per probe execution; blackbox_exporter lineage; Grizzly.
- Checkly: setup/teardown scripts; retry strategy with alerts only after the final failed attempt; cron→queue→data-center execution description; constructs/CLI; Playwright Check Suites; "Application Reliability Platform" repositioning.
- Datadog: Bits Testing/Goal-Based (non-deterministic agentic) testing; test suites by journey/environment/location/service/team; version history; test coverage tracking; network path tests with packet-route visualization; mobile tests; private locations worker model.
- Pingdom: "over 100 locations worldwide" and transaction interval range "every five minutes to once per day" (vendor-stated); double-check false-positive filter; public status pages included in all plans; price point "starts at $10 per month" (vendor-stated); SolarWinds Observability family context.
- UptimeRobot: plan-tier intervals (free 5 min → enterprise 30 s, vendor-stated); 50 free monitors; checker-node rechecking; MCP integration; website change detection; domain expiry.
- Catchpoint/LogicMonitor: acquisition packaging; Internet Health/IPM sibling; WebPageTest in portfolio; Edwin AI platform correlation; "largest global agent network" claim (vendor-stated, unverified).
- Dynatrace (via DEM pass): HTTP/browser/NAM monitors; execute on demand at selected locations; Smartscape monitor model.

## Rejected Findings

- **"Synthetic monitoring = simulating a real user"** — rejected as the definition. The check spectrum's floor (ping/port/DNS/HTTP checks) simulates no user; UptimeRobot's whole product is endpoint availability. The invariant is a synthesized, machine-generated interaction; user-journey emulation is the ceiling (L1), not the floor.
- **"Synthetic monitoring requires a browser"** — rejected. Only the journey ceiling uses browsers; the floor is protocol-level.
- **"Synthetic monitoring is defined by the vendor's global probe fleet"** — rejected as invariant. Private/customer-deployed probes are first-class in Grafana, Datadog, Checkly (data-center locations); a self-hosted open-source agent satisfies the core. The invariant is execution from measurement points outside the monitored runtime, not whose machines they are.
- **"Uptime monitoring is a different Type from synthetic monitoring"** — rejected. The market itself nests uptime monitoring under synthetic monitoring (Pingdom's product taxonomy); the simple pole satisfies all three L0 legs; the difference is check depth, not structure. The directory has no separate uptime-monitoring leaf; the simple pole lives inside this Type as its minimal variant.
- **"Alerting is optional"** — rejected. Every sampled product centers notification on failure; without the watch loop the artifact is a traffic generator or a test suite, not monitoring. (Consistent with the metrics-monitoring pass, which held alerting definitional for the same structural reason.)
- **"Synthetic monitoring includes RUM"** — rejected. The market consistently separates them (Pingdom RUM as sibling product; LogicMonitor RUM as separate product; Datadog RUM & Session Replay as a separate documented product; Catchpoint FAQ draws the line explicitly). RUM belongs to DEM (which has no leaf of its own and is DEM's natural host per the DEM pass).
- **"A composite experience score is definitional"** — rejected; no sampled product centers one. Metrics are per-dimension (availability, response time, success).

## Boundary Findings

1. **vs Digital Experience Monitoring (§14, processed) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED with the DEM pass's center-of-gravity seam, sharpened structurally.** The two Types share the consumer-side measurement skeleton: a synthetic-only product satisfies DEM's measurement leg (consumer-side, experience metrics, location context). The seam is the unit of record and the posture set. Synthetic Monitoring's unit of record is the **check** — a definition of a simulated interaction — and its posture is simulation only; it never collects from real users' sessions. DEM's unit of record is the **monitored service experience** and its posture set includes real-user collection; DEM products bundle synthetic machinery as one collection posture among others. Remove-test: remove the unified experience picture and the real-user posture (keep probe machinery as the center) → Synthetic Monitoring; remove the probe machinery as the center (keep the experience picture) → DEM. Market corroboration: Pingdom sells RUM as a separate sibling product; LogicMonitor lists RUM Monitoring separately and its Catchpoint FAQ states the synthetic/RUM distinction; Datadog documents Synthetics and RUM as separate products. The market maintains the split; the directory's two leaves are sound.
2. **vs Metrics Monitoring (§14, processed) — producer-vs-series seam RATIFIED from this side.** Synthetic probes generate the measurements that metrics monitoring consumes: Grafana publishes check results as Prometheus metrics (`probe_success`, `probe_duration_seconds`) and Loki logs; other products store results in their own platforms. The seam: synthetic monitoring's center is the check machinery (authoring, scheduling, executing, evaluating); metrics monitoring's center is the series store/query/alert layer over identified numeric series from any source. Remove the probe machinery (keep series store/query/alerting) → Metrics Monitoring. Once a synthetic result becomes a derived named series with its own alerting, it has crossed into metrics-monitoring territory — the same one-way-bridge pattern the metrics pass recorded for logs-to-metrics.
3. **vs Network Monitoring (§14, processed) — object seam RATIFIED from this side.** Technique overlap is real (ICMP ping, TCP connect, traceroute checks exist in both families — Grafana ships Ping/TCP/Traceroute checks; Pingdom runs per-incident traceroute), but the object differs: network monitoring's estate is network infrastructure (devices/links with first-class interface state); synthetic monitoring's targets are user-facing services and endpoints (URLs, APIs, DNS records, ports, transaction flows) regardless of what network carries them. Network monitoring uses active probes as one collection method among several; synthetic monitoring's center is the probe machinery itself. Remove the user-facing-service framing (watch devices/links instead) → Network Monitoring.
4. **vs End-to-end Testing Platform (§12, processed) — loop/environment seam RATIFIED from this side.** Same journey mechanics (Playwright scripts, clickpaths, assertions), different loop and environment: E2E testing produces pre-release, change-linked verdicts in test environments consumed by a release process; synthetic monitoring produces continuous scheduled production availability with alerting. Vendor-drawn bridge evidence: Checkly ships both postures in one platform ("Pre-Production Testing — validate functionality and performance in staging before deployment" beside "Production Monitoring — continuously monitor critical user journeys") and markets "converting existing E2E tests into monitoring" (Playwright Check Suites); Datadog's Continuous Testing Explorer covers CI batches beside scheduled tests. The straddle is documented and the seam is the loop, not the mechanics.
5. **vs Load Testing Platform (§12, processed) — perturbation seam RATIFIED from this side with direct vendor evidence.** Same script engine lineage (k6), opposite perturbation posture: Grafana's own definition — "Each execution of a check simulates a single user performing a single iteration from one location... consistent, lightweight monitoring" — against load testing's controlled concurrent population and deliberately heavy load. The load-testing pass recorded k6 routing production monitoring to its separate Grafana Cloud Synthetic Monitoring product; this pass confirms the two products coexist under one vendor with the single-user/multi-user seam. Remove the minimal-load posture (add a controlled population) → Load Testing.
6. **vs Infrastructure Monitoring (§14, processed) — estate/instrument seam.** Infrastructure monitoring watches deployed components from inside the estate (agents/collectors on hosts); synthetic monitoring probes user-facing endpoints from outside. A synthetic HTTP check against a server's URL is a measurement of the service endpoint, not of the host. Consistent with the infrastructure pass's entity-centric framing.
7. **vs Application Performance Monitoring (§14, processed) — instrumentation-locus seam.** APM instruments the serving application's runtime (in-process traces); synthetic monitoring never enters the runtime. They meet at correlation surfaces (Datadog synthetic↔APM trace integration; Checkly OTel tracing). Consistent with the APM pass's recorded seam.
8. **vs Status Page Platform (§14, processed) — downstream communication.** Check status feeds status pages (Pingdom and UptimeRobot bundle status pages; Checkly's Communicate layer includes them). Measurement vs communication; no overlap in the core.
9. **vs Incident Management / On-call Management (§14, processed) — downstream consumer.** Synthetic alerts feed incident processes (integrations to PagerDuty-class tools are standard); the check record is not an incident record.
10. **vs Observability Platform (§14, processed) — bundling relationship.** Synthetic monitoring ships as a suite pillar/module (Datadog, Dynatrace, LogicMonitor/Catchpoint, Grafana Cloud) and equally as standalone products (Checkly, Pingdom, UptimeRobot); pillar packaging is variant, not identity — consistent with the observability pass's treatment of pillar packaging.
11. **vs Website-change-detection / content monitoring** — UptimeRobot ships website change detection as a monitor type; it is a variant capability inside the check frame (a synthesized fetch + content comparison), not a separate Type in this directory.

### "Remove what → becomes the other Type" summary

- Remove the check as unit of record (keep one-off journeys in test environments) → E2E Testing.
- Remove the minimal-load posture (add controlled concurrent population) → Load Testing.
- Remove the probe machinery as center (keep the unified experience picture + real-user posture) → DEM.
- Remove the probe machinery (keep the series store/query/alert layer) → Metrics Monitoring.
- Remove the user-facing-service object (watch network devices/links) → Network Monitoring.
- Remove the outside-in vantage points (instrument the runtime) → APM.
- Remove measurement (keep communication) → Status Page.

## Historical / Market-Sample Check (§24)

- **The core predates the modern machinery.** The first generation of hosted website-availability services — scheduled HTTP/ping checks from the provider's measurement points, email alerts on failure, uptime reports — satisfies all three L0 legs with no browser checks, no cloud dashboards, no AI. (Low-precision inference; no third-party historical source fetched this pass.) The transaction-monitoring generation (recorded multi-step flows from measurement points) adds the journey ceiling on the same core.
- **The self-hosted pole**: a scheduled script on an operator's own machine that fetches a URL, asserts on the response, and emails on failure is conceptually the same three legs with customer-operated vantage points — the private-probe products (Grafana private probes, Datadog private locations, Checkly data-center locations) are the commercialized form of this pole. Deployment is therefore variant, not definitional.
- **Regional/platform-native products**: regional availability-checking services and open-source self-hosted uptime tools fit the core; nothing in the core requires a specific geography, platform, or business model.
- **Era-current mass** (deliberately not definitional): browser/mobile journey checks, Web Vitals, AI/agentic test generation, SLO computation, monitoring-as-code, status-page bundling, OTel correlation.
- Conclusion: the L0 phrasing (check as record + recurring outside-in execution + watch loop) holds across eras and deployment poles; no precise dates asserted anywhere in the final document.

## Uncertainties

- Catchpoint's own documentation was not reachable as an independent surface (domain serves LogicMonitor pages post-acquisition); the pure-play pole is evidenced through the acquirer's product page at marketing depth. No operational details asserted for Catchpoint internals.
- Pingdom and UptimeRobot evidence is product-page/FAQ depth (Tier 2), not help-center depth; vendor-stated numbers (location counts, interval ranges, price points) are recorded in research notes only and excluded from the final document.
- The DEM seam is ratified from this side in agreement with the DEM pass's proposal; no counter-evidence found in the sampled products (all six maintain synthetic and RUM as separate surfaces or omit RUM entirely).
- Whether the market will keep "synthetic monitoring" as the umbrella name (Pingdom nests uptime under it; LogicMonitor titles the Catchpoint page "Synthetic Monitoring") or continue splitting "uptime monitoring" as a consumer-facing synonym is a naming trend, not a structural question — noted, not resolved.
- Heartbeat/reverse-direction checks were observed in two products (Checkly, UptimeRobot); whether deeper synthetic products (Datadog, Grafana) ship them was not verified — held as variant, not common-mature.

## Final Synthesis

A Synthetic Monitoring application is the outside-in watch machinery of the monitoring stack: it holds a population of checks — persistent, re-runnable definitions of synthesized interactions against user-facing targets, each carrying its steps/script, its assertions, its schedule, and its vantage-point selection — executes every check on its schedule from measurement points outside the monitored system (a managed global probe fleet and/or customer-deployed probes), evaluates each run against the check's assertions into a pass/fail verdict with response measurements, retains the results as history, and alerts when checks fail, with false-positive filtering before notification. Its defining core is the joint hold of three structures: the check as unit of record, recurring outside-in execution, and the watch loop. Around that spine, mature products add the check-type spectrum from endpoint probes to scripted browser/mobile journeys, per-vantage-point results, availability/response-time reporting, SLO computation, programmatic/monitoring-as-code management, correlation to backend telemetry, and bundled status pages. The Type is bounded by DEM (which owns the unified experience picture and real-user collection), Metrics Monitoring (the series layer the probes feed), Network Monitoring (same techniques, different object), E2E and Load Testing (same mechanics, different loop and perturbation posture), APM (instrumentation locus), and Status Pages (downstream communication). The market's "uptime monitoring" simple pole is this Type's minimal variant, not a separate Type; the pure-play leader has been absorbed into a broader platform, and the Type now lives equally as standalone products and as suite pillars.
