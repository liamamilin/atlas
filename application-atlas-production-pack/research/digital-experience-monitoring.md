# Research Notes — Digital Experience Monitoring

## Research Goal

Determine what a Digital Experience Monitoring (DEM) application is as an Application Type: its defining core, its standard capability set, its variants, and — most importantly — its boundaries against the neighboring §14 monitoring Types (Synthetic Monitoring, APM, Network/Infrastructure Monitoring, Observability Platform, Digital Employee Experience Management) and against downstream operational Types (Incident Management, Status Page).

Counterparty obligations carried into this pass:

- `digital-employee-experience-management` (§14, processed 2026-09-08) flagged a JOINT REVIEW with this leaf, proposing: "DEM measures application/service experience for the IT service owner (synthetic + RUM + network paths; employee is one traffic source), DEX takes the employee's workspace itself as the unit (person + device + apps + endpoint-experienced connectivity) and adds the remediation/management loop; overlap zone is real (DEX tools shipping synthetic monitoring; DEM tools measuring employee-side sessions)." This pass must answer that flag from the DEM side.
- `application-performance-monitoring-apm` (§14, processed 2026-09-06) recorded: "vs Digital Experience Monitoring / RUM: DEM/RUM center on the end user's session quality (browser/mobile); APM centers on server-side application components" and rejected "APM must include RUM/browser/synthetic monitoring" as a bundling pattern. This pass must hold that seam from the DEM side.
- Directory observation: §14 has a `synthetic-monitoring` leaf (unprocessed) but **no Real User Monitoring leaf**. DEM is the only leaf where RUM can live. This shapes the boundary work.

## Initial Boundary (hypothesis before research)

- DEM is likely the Gartner-coined market category (~2020): availability/performance monitoring of digital services **from the user's side of the delivery path**, realized through synthetic monitoring (simulated interactions from vantage points) + real user monitoring (passive observation of actual sessions), often with network-path attribution.
- Likely confusions: Synthetic Monitoring (probe machinery as its own leaf), APM (in-process instrumentation), Network Monitoring (device/link health), Observability Platform (umbrella bundling), DEX (employee workspace as unit), Product Analytics (usage/behavior vs performance).
- Open question going in: is DEM a coherent Type or just a Gartner umbrella over synthetic + RUM? The directory keeps Synthetic Monitoring separate, so the seam must be made explicit.

## Research Questions

1. What objects exist inside a DEM system? (monitors/tests, vantage points/agents, user sessions/events, journeys/steps, errors, paths)
2. What collection postures exist and how do they relate? (synthetic vs real-user; endpoint agents?)
3. What metrics constitute "experience"? (availability, response time, success, vitals/satisfaction-class measures)
4. How is degradation attributed? (location, ISP/network path, page/step, component)
5. What is the operational loop? (configure → collect → evaluate → alert → attribute → correlate → verify)
6. Who uses it, and what interfaces do they face?
7. How do suite vendors vs platform vendors vs network-first vendors package it?
8. Where are the exact seams: vs Synthetic Monitoring, vs APM, vs Network Monitoring, vs DEX, vs product analytics?

## Representative Products

Selection rationale: market representation (three poles of the DEM market), documentation completeness, different product philosophies, different customer layers. Catchpoint (the canonical pure-play) was attempted first but its site was unreachable (404 ×2, support portal empty ×1) — recorded as a sampling limitation. Riverbed (endpoint-RUM pole) and IBM (403) also unreachable. The endpoint-agent RUM posture is nonetheless directly evidenced inside the ThousandEyes sample (Endpoint Agents with Real User Tests), so no pole is missing entirely.

| Product | Pole | Customer layer | Evidence accessed |
|---|---|---|---|
| Dynatrace | Suite vendor; sells "Digital Experience" as a named product area = RUM + Session Replay + Synthetic | Enterprise, application/IT teams | docs.dynatrace.com (DEM hub, RUM, RUM data model, Synthetic pages) |
| Datadog | Platform vendor; decomposed packaging — RUM & Session Replay and Synthetic Testing sold/documented as separate products | Enterprise + mid-market, frontend/SRE teams | docs.datadoghq.com (Synthetics, RUM & Session Replay) |
| Cisco ThousandEyes | Network-intelligence-first DEM; vantage points + tests + path visualization, endpoint agents | Enterprise IT / NOC / network ops | docs.thousandeyes.com (docs index + structure) |

## Sources

Fetched 2026-09-08:

- Dynatrace docs — Digital Experience hub: https://docs.dynatrace.com/docs/observe/digital-experience (quotes Gartner's DEM definition; lists DEM = RUM + Session Replay + Synthetic Monitoring)
- Dynatrace docs — RUM: https://docs.dynatrace.com/docs/observe/digital-experience/rum
- Dynatrace docs — RUM data model: https://docs.dynatrace.com/docs/observe/digital-experience/rum/concepts/data-model
- Dynatrace docs — Synthetic Monitoring: https://docs.dynatrace.com/docs/observe/digital-experience/synthetic
- Datadog docs — Synthetic Testing and Monitoring: https://docs.datadoghq.com/synthetics/
- Datadog docs — RUM & Session Replay: https://docs.datadoghq.com/real_user_monitoring/
- ThousandEyes docs — documentation index: https://docs.thousandeyes.com/ and https://docs.thousandeyes.com/llms.txt (full product-documentation tree)

Unreachable (source-access limitation, 2026-09-08):

- Catchpoint: www.catchpoint.com paths 404 ×2; support.catchpoint.com empty ×1 — pure-play DEM positioning evidenced at existence level only, no operational detail asserted.
- Riverbed (docs.riverbed.com transport error), IBM Instana (ibm.com/docs 403), Exoprise (docs.exoprise.com 400) — abandoned after 1 failure each per the network-restriction rule.
- Wikipedia (Real user monitoring) — timed out; no third-party historical reference obtained. Historical claims below are marked as inference, kept at low precision, and excluded from the final document's precise claims.

## Product A — Dynatrace

### Key observations (evidence layer A — directly observed)

- **DEM is a named product area.** The docs hub "Digital Experience" states DEM is "defined by Gartner as an availability and performance monitoring discipline that supports the optimization of the operational experience and behavior of a digital agent, human, or machine, as it interacts with enterprise applications and services," and groups **Real User Monitoring, Session Replay, and Synthetic Monitoring** under it. A "Digital Experience" tag organizes the docs tree.
- **RUM object model** (RUM data model page): RUM captures end-user data as **user events** (ID, start/end time, duration; context: OS, geolocation, device, browser) in a `user.events` table; **user sessions** summarize all events of the same end user within a time frame (ending after inactivity or max duration; `user.sessions` table); event kinds include **pages/views/navigations** (views supported on web and mobile; mobile view = screen), **user interactions** (clicks, scrolls, mouseover; mobile touches/gestures/rotations), **user actions** ("a meaningful interaction initiated by an end user that triggers a distinct piece of application behavior and produces an observable outcome" — duration from interaction to user-visible result, examples "click on order on /cart"), **requests** (URL, method, status, W3C Resource/Navigation Timing), **errors** (failed requests, uncaught exceptions, CSP violations, mobile crashes, ANR). **Event/session properties** add business context (cart value, A/B variant, customer tier).
- **RUM apps**: Experience Vitals (entry point for web/mobile frontend monitoring), Users & Sessions (individual user journeys/behavior), Error Inspector (frontend errors for "developers and IT teams").
- **RUM operations**: "Analyze and alert" — built-in metrics, health alerts, DQL analysis; a dedicated **data privacy** page ("Ensure that your RUM setup complies with the data privacy regulations of your region"); **permissions** page.
- **Synthetic object model**: create/configure **HTTP, browser, and NAM monitors**; results in a **Synthetic app**; metrics include "availability rate, number of monitor executions, sum of step durations"; **execute monitors on demand at selected locations** (UI or API/workflow); monitor model includes **monitors, steps, locations** (Smartscape); synthetic alerting overview; access control.

## Product B — Datadog

### Key observations (evidence layer A)

- **Decomposed packaging.** "Synthetic Testing and Monitoring" and "RUM & Session Replay" are separate documented products. Yet RUM's docs navigate to it via "**Digital Experience** > Performance Summary" — the grouping word survives in product navigation even where the packaging is decomposed.
- **Synthetic tests**: simulated "requests and actions from around the globe" — API tests at network layers (HTTP, SSL, DNS, WebSocket, TCP, UDP, ICMP, gRPC), multistep API tests, **browser tests** ("monitor how your customers experience your webpages end-to-end"), **mobile application tests** (iOS/Android "end-to-end"), **network path tests** (TCP/UDP/ICMP with packet-route visualization), **private locations** ("monitor internal APIs and websites... custom locations in areas that are mission-critical"), **test suites** (grouped by user journey/environment/location/service/team), **SLOs computed on key endpoints and user journeys**, CI/CD execution, notifications with conditional alerting, version history, coverage tracking.
- **RUM**: "end-to-end visibility into the real-time activity and experience of individual users"; four use cases — **Performance** (pages, screens, user actions, network requests, frontend code), **Error Management** (bugs/issues over time and versions), **Analytics/Usage** (who uses the app — country/device/OS; journeys; interactions), **Support** ("retrieve all of the information related to one user session to troubleshoot an issue").
- **RUM session definition**: "a user journey on your web or mobile application," including RUM Views, RUM Actions, RUM Resources, RUM Errors, crashes — "a faithful representation of the user experience." Technical limitations documented (session max duration, inactivity timeout, event/attribute caps — product-specific numbers, kept out of the final document).
- **RUM platform breadth**: browser, Android, iOS, Flutter, React Native, Roku, Unity, Kotlin Multiplatform; capabilities table includes distributed tracing of network requests, view/action tracking, error tracking + source mapping, crash symbolication, session replay, **frustration signals**, web/mobile vitals (Core Web Vitals for web; hang rate for iOS).
- **Correlation**: "Integration with logs, APM, and profiler — view backend traces, logs, and infrastructure metrics down to the exact line of code... corresponding to user experiences"; synthetic↔APM trace integration "to find the root cause of failures across frontend, network, and backend requests."
- **Privacy/permissions**: Session Replay privacy controls; RUM application permissions with role-based restriction.

## Product C — Cisco ThousandEyes

### Key observations (evidence layer A, from the docs tree; depth is structural rather than per-page)

- **Vantage points are a first-class object family**: "Global Vantage Points" — **Cloud Agents** (global managed locations), **Enterprise Agents** (virtual/physical appliances, Docker, installed on Cisco switches/routers), **Endpoint Agents** (Windows/macOS + browser extension, mobile agent on Android/ChromeOS, Cisco Secure Client module), plus **Connected Devices** tests.
- **Test types** span the whole delivery path: HTTP Server, **Web-Layer tests** (Page Load, Transactions with scripting, waterfall charts, screenshots), **Network tests** (agent-to-agent), DNS, **Voice** (SIP server, RTP stream), **BGP**, API tests, instant tests, templates, "Multi-Service Views."
- **Endpoint Experience** area: **Real User Tests** captured from endpoint-agent browser sessions (alongside scheduled tests and dynamic tests), "Endpoint Agent End-user Experience," Local Networks view — i.e., real-user measurement from employee endpoints inside a network-first product.
- **Path attribution**: "Path Visualization" with hop-by-hop path trace, MPLS tunnel inference, troubleshooting guides — network-path decomposition is the product's signature diagnostic layer.
- **Operations**: Alerts, Dashboards, Internet Insights (outage visibility), API, test settings, tags.

## Cross-product Comparison

| Dimension | Dynatrace | Datadog | ThousandEyes |
|---|---|---|---|
| Packaging | DEM as named product area (RUM + Replay + Synthetic) | Decomposed: two separate products under a "Digital Experience" nav | Network intelligence platform; Browser Synthetics + Endpoint Experience areas |
| Monitored unit | user events / user sessions per frontend; synthetic monitors (HTTP/browser/NAM) | RUM sessions (views/actions/resources/errors); synthetic tests per type | tests per type; endpoint-agent real-user sessions |
| Real-user posture | RUM SDK/beacon on web+mobile frontends | RUM SDKs across 9+ platform families | Endpoint Agent "Real User Tests" |
| Simulated posture | monitors from "selected locations" | API/browser/mobile/network-path tests from managed + private locations | Cloud/Enterprise agent tests (HTTP/page load/transaction/DNS/voice/BGP) |
| Vantage-point concept | monitor execution locations | managed locations + private locations | Cloud/Enterprise/Endpoint agents — the most elaborated |
| Experience metrics | availability rate, executions, step durations; frontend vitals; errors | response/success per test; Core Web Vitals; mobile vitals; frustration signals | response time, latency/loss/jitter, transaction success, waterfall timings |
| Attribution surface | monitor → steps → locations; error inspector | test ↔ trace across frontend/network/backend; RUM ↔ APM line-of-code | hop-by-hop path visualization, BGP routes, MPLS inference |
| Alerting | synthetic alerting; RUM health alerts | notifications/monitors on tests; RUM monitors | alerts on tests; Internet Insights events |
| Privacy surface | RUM data-privacy doc page | replay privacy options; RUM app permissions | endpoint-agent data-collection docs |

Evidence layer B (cross-product commonality, 3/3 sampled): consumer-side measurement (real-user and/or synthetic); experience metrics in availability/responsiveness/success terms; per-location/vantage-point result context; step/journey decomposition; alerting on experience thresholds; a privacy surface on real-user collection; correlation hooks toward backend telemetry.

Evidence layer C (canonical inference): the Type's unit of concern is the **experienced quality of digital services as delivered to their consumers, measured from outside the serving system, attributed along the delivery path** — collection posture is implementation.

## Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The monitored service experience as the unit of record** — a defined set of user-facing digital services/interactions (websites, applications, transactions/journeys) whose experienced quality is what the system tracks. Remove → component monitoring with nothing experienced to measure.
2. **Consumer-side measurement** — experience data originates at the consumption point of the delivery path: from instrumented real users' clients (browser/mobile/endpoint) and/or from synthetic vantage points simulating user interactions; never only from inside the serving application's runtime. Remove → APM / infrastructure monitoring.
3. **Experience attribution across the delivery path** — results are evaluated as experienced quality (reachability/availability, responsiveness/duration, interaction success/failure, errors-as-experienced) and decomposed along consumption context — vantage point/location, client/device, journey step, network path — so degradation can be located between user and service. Remove → a bare up/down status checker or a log stream.

Jointly-held is load-bearing: 1+2 without 3 = raw result feed; 2+3 without 1 = unanchored network probing; 1+3 without 2 = server-side dashboards (APM territory).

### L1 — Common Mature Structure

- **Dual collection posture** (synthetic + real-user) held in one experience picture — the market-defining combination; present in all three samples in some form (Datadog as separate products under one nav).
- Synthetic monitor types: single-URL/HTTP checks, browser clickpaths/page loads, multi-step transactions, multi-step API chains, network-path checks; on-demand and scheduled execution; assertions/thresholds.
- RUM event model: sessions; views/pages; user actions/interactions; resources/requests; errors/crashes; session replay; vitals/satisfaction-class scores; frustration signals.
- Experience evaluation: thresholds/baselines → status/alerts; SLO computation on journeys/endpoints (Datadog explicit).
- Attribution tooling: waterfalls, step breakdowns, per-location/ISP breakdowns, path visualization, error inspection.
- Correlation to backend telemetry (traces/logs) via shared identifiers.
- Vantage-point fleet management: managed global locations + customer-deployed private/enterprise locations.
- Privacy surfaces for real-user data (redaction, masking, consent configuration); role-based access.

### L2 — Variant / Optional Structure

- Packaging: suite DEM module (Dynatrace) vs decomposed platform products (Datadog) vs network-first platform (ThousandEyes) vs pure-play (Catchpoint — existence-level evidence only).
- Center of gravity: web/digital-app experience vs enterprise SaaS/UCaaS delivery from branches vs network-path-first (BGP/voice tests).
- Endpoint-agent RUM pole (employee endpoints as vantage points) — approaches DEX territory; variant posture, not the core.
- Mobile-app experience emphasis; session replay attach; connected-device/IoT tests.
- Audience split: digital/web product teams vs NOC/network ops vs service owners.
- AI/agent-era extensions (agentic test generation — Datadog Bits/Goal-Based testing).

### L3 — Vendor-specific (research notes only)

- Dynatrace: `user.events` / `user.sessions` Grail tables; OpenPipeline enrichment; Experience Vitals / Users & Sessions / Error Inspector app names; NAM monitors; Smartscape model; DQL.
- Datadog: exact session limits (4h max, 15-min inactivity, 10M events — product-specific, excluded from final doc); intake domains; platform support matrix; Bits/Goal-Based testing; "Digital Experience > Performance Summary" nav path.
- ThousandEyes: Cloud/Enterprise/Endpoint agent taxonomy; TEVA/TEPA appliances; BrowserBot; test-type catalog (SIP/RTP/BGP/MPLS inference); Internet Insights; Cisco Secure Client module; Webex cloud agents.
- Gartner DEM category framing quoted at second hand via Dynatrace docs.

## Rejected Findings

- **"DEM = synthetic monitoring + RUM, by definition"** — rejected as the definition. The dual posture is the dominant market shape (L1), but the invariant is the consumer-side experience object with attribution; each posture alone realizes the measurement, and packaging varies (Datadog splits them; ThousandEyes folds RUM into endpoint agents). Defining DEM as the bundle would make the Type an umbrella over two other leaves/capabilities rather than a Type with its own center.
- **"DEM requires a composite experience score"** — rejected. No sampled product's documentation centers a single composite DEM score; metrics are per-dimension (availability, response time, success, vitals). Scoring is per-metric and product-specific.
- **"DEM is a web-product-analytics tool"** — rejected. Usage/behavior analytics overlap (RUM "Analytics/Usage" use case) exists, but the Type's center is experienced quality (performance/errors), not audience/behavior measurement.
- **"DEM must include hop-by-hop network path visualization"** — rejected as invariant. Path decomposition depth varies (ThousandEyes signature; Dynatrace/Datadog rely on waterfall + backend correlation). The invariant is attribution by consumption context, of which network path is one elaboration.
- **"DEM = employee experience monitoring"** — rejected (name collision with DEX); the consumer population of a monitored service is not necessarily employees, and no remediation-loop ownership was observed in the DEM sample.

## Boundary Findings

1. **vs APM (§14, processed) — hold from this side; keep-both.** The APM pass's own L0: in-process instrumentation of the server-side service population, request/operation-centric, for engineering teams. DEM measures from the consumption point (real-user clients / vantage points), experience-centric, for service owners/IT ops. The same slow transaction is observable from both ends; products correlate them via shared identifiers (Datadog RUM↔APM "down to the exact line of code"; Dynatrace platform correlation). Remove consumer-side measurement → APM; remove in-process service telemetry and DEM remains. Consistent with the APM pass's recorded seam.
2. **vs Synthetic Monitoring (§14, unprocessed) — sharpest seam; flagged for joint review.** The two Types share the measurement skeleton (consumer-side, experience metrics, location context): a synthetic-only product satisfies DEM's L0 *measurement* structure but its *center of gravity* is the probe machinery (authoring scripts/monitors, scheduling, assertions), while DEM's center is the unified service-experience picture — which additionally owns **real-user monitoring** (RUM has no leaf of its own in the directory; DEM is its natural host). Working seam: probe-machinery-centered product → Synthetic Monitoring; experience-view-centered product (esp. with real-user posture) → DEM. Recorded for joint review when synthetic-monitoring is processed.
3. **vs Digital Employee Experience Management (§14, processed 2026-09-08) — joint-review flag DISCHARGED from the DEM side; keep-both RATIFIED.** DEM's unit of record is the digital service's experienced quality as delivered to its consumers (customers and employees alike are traffic sources); its diagnostic motion is attribution along the delivery path, and it owns no device/OS estate and no remediation loop. DEX's unit is the employee's workspace (person + device + apps + endpoint-experienced connectivity) with an IT-owned remediation loop and endpoint telemetry (device/OS health) that DEM does not collect. Overlap zone is real and asymmetric: endpoint-agent-based real-user measurement (ThousandEyes Endpoint Agent "Real User Tests") uses employee devices as *vantage points* while keeping the service experience as the object — a variant posture of DEM, not DEX; conversely DEX tools shipping synthetic checks (per the DEX pass) remain DEX-centered. Remove service-experience attribution → endpoint telemetry estate (DEX/UEM territory); remove the workspace/remediation loop → DEM.
4. **vs Network Monitoring / Infrastructure Monitoring (§14, unprocessed) — keep-distinct.** Network monitoring's objects are devices/links/health; DEM's object is experienced service quality. Network data enters DEM as an attribution layer (path visualization, ISP/backbone breakdowns), and network-first products (ThousandEyes) blur the seam at product level, but the remove-test holds: strip the experience framing (transactions, journeys, user-facing success) → network monitoring.
5. **vs Observability Platform (§14, unprocessed) — bundling relationship.** DEM capabilities are commonly bundled in observability suites (all three samples are suite/platform members); that is packaging, not identity. DEM has its own center (consumer-side experience) and stands alone in pure plays.
6. **vs Incident Management / On-call (§14) — downstream consumer.** DEM alerts feed incident processes; DEM itself evaluates and attributes experience, it does not own the incident record.
7. **vs Status Page Platform (§14) — no overlap.** Status pages communicate status publicly; DEM measures.
8. **vs Product Usage / Adoption Platform (§07, processed) — adjacent analytics.** RUM's usage/analytics use case touches product analytics, but the DEM center is performance/error experience, not adoption/feature usage.
9. **vs Error Tracking Platform (§12) — partial overlap on frontend errors.** Error tracking centers the exception workflow for engineering; DEM surfaces errors as one experience dimension among availability/responsiveness/success.

### "Remove what → becomes the other Type" summary

- Remove consumer-side measurement (keep in-process instrumentation) → APM.
- Remove the unified experience view and real-user posture (keep probe machinery) → Synthetic Monitoring.
- Remove experience framing (keep device/link health) → Network/Infrastructure Monitoring.
- Remove the service-experience object (keep workspace telemetry + remediation loop) → DEX.
- Remove measurement entirely (keep communication) → Status Page.

## Historical / Market-Sample Check (§24)

- The consumer-side measurement skeleton is old: synthetic transaction monitoring from distributed measurement points, with per-location/backbone breakdowns, predates the "DEM" label by two decades (industry lineage; no third-party reference obtained this pass — Wikipedia unreachable; stated here as low-precision inference only). Such products satisfy L0's measurement structures and read as the Synthetic Monitoring lineage; the DEM Type as a named category consolidated when real-user observation joined synthetic probing under one experience view.
- The real-user posture and session replay are later arrivals (L1), not definitional.
- Platform-native/embedded poles (CDN/edge vendors, load-testing tools) ship adjacent capabilities at existence level; no impact on the core.
- Conclusion: L0 phrased as service-experience + consumer-side measurement + attribution holds across eras; the dual posture, replay, vitals, and SLO computation are era-current mass. No precise dates asserted anywhere in the final document.

## Uncertainties

- Pure-play DEM documentation (Catchpoint) unreachable — no claims about pure-play product internals; the pure-play pole is evidenced at existence level only.
- Gartner's definition is quoted at second hand (via Dynatrace docs); the primary report was not accessed.
- ThousandEyes observations derive from the documentation tree structure rather than deep per-page reads; operational details (agent quotas, test intervals) deliberately not asserted.
- The synthetic-monitoring vs DEM seam is set from this side only; the synthetic-monitoring leaf is unprocessed and may counter-propose.
- Whether the market will keep "DEM" as a suite module name or dissolve it into decomposed RUM/synthetic products (Datadog pole) is a packaging trend, not a definition question — noted, not resolved.

## Final Synthesis

A Digital Experience Monitoring application is the consumer-side half of the monitoring stack: it holds a defined set of user-facing digital services as monitored objects, measures their experienced quality from the consumption point of the delivery path — through instrumented real users' clients and/or synthetic vantage points that simulate user interactions — and attributes degradation along that path (vantage point/location, client/device, journey step, network path), so a service owner can answer not only "is it broken" but "who experiences it broken, where, and at which step." Its defining core is the joint hold of three structures: the monitored service experience as unit of record, consumer-side measurement, and experience attribution across the delivery path. Around that spine, mature products add the dual collection posture in one picture, journey/step decomposition, session replay, vitals/satisfaction measures, alerting and SLO computation on experience terms, vantage-point fleet management, privacy surfaces for real-user data, and correlation to backend telemetry. The Type is bounded by APM (instrumentation locus), Synthetic Monitoring (center of gravity on probe machinery), Network Monitoring (object of health), and DEX (unit = employee workspace + remediation loop) — each seam ratified or flagged with a concrete remove-test. The leaf stands as an independent Type, and is additionally the directory's home for real-user monitoring, which has no leaf of its own.
