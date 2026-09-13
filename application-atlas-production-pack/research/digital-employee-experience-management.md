# Research Notes — Digital Employee Experience Management

Date: 2026-09-08
Leaf: Digital Employee Experience Management (DIRECTORY §14 IT, Cloud & Infrastructure, line 1088)
Slug: digital-employee-experience-management

## Research Goal

Understand what a Digital Employee Experience Management (DEX) platform actually is as an Application Type: what "experience" means operationally here, what is instrumented and how, how experience is quantified, what operational loop IT runs over it, and where the boundary lies against the neighboring Types in §14 (APM, Digital Experience Monitoring, Endpoint Management/UEM, RMM, Desktop & Application Delivery) and against the §09/§10 "employee experience" name-collision family.

Carried obligations from prior passes (STATUS.md Boundary Issues):

- employee-experience-platform vs digital-employee-experience-management (§14): "same two words, different structure — DEX monitors endpoint/application performance telemetry owned by IT (observability estate) while EX platforms deliver and measure HR/comms-owned organizational experience (content, listening, journeys, services); different buyers, objects, and rules; the leaf definition explicitly excludes IT telemetry to prevent a name-based collision." This pass must ratify from the DEX side.
- employee-service-management research (finding 9): "DEX monitors endpoint/application telemetry; ESM fulfills employee requests. Same word 'experience', different objects and owners."
- product-usage-adoption-platform research (finding 10): "Pendo's browser-extension employee analytics (app catalog, license utilization of third-party apps) approaches DEX territory; it is a variant posture of this Type, not the core."
- browser-security-platform research: enterprise browsers ship "DEX analytics" surfaces (Island) — an adjacent capability, not this Type's core.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: DEX management = IT-side observability + remediation over the employee's own endpoint estate (devices, apps, connectivity as the employee experiences them), quantified into experience scores and worked through a detect→diagnose→fix→verify loop. Distinct from APM (server-side, request-centric), from UEM (configuration/policy ownership), from HR-side Employee Experience Platforms, from ITSM (ticket-centric).
- Likely users: EUC/desktop engineering, IT ops, service desk; NOT the employee as primary operator.
- Likely confusion axes: the word "experience" (four different estates use it), the word "monitoring" (many monitoring families), endpoint management vs endpoint observation.

## Research Questions

1. What is the core object of record — the employee, the device, the application, the session, or the "experience"?
2. What telemetry is collected, from where, and how (agent, platform-native sensor, browser extension)? What are punctual vs continuous signals?
3. How is "experience" quantified (scores? issue states? both)? Over what windows, at what granularity?
4. What is the operational loop: detection → diagnosis → remediation → verification? Who acts, and how (remote actions, automations, scripts, guided self-help, ticket context)?
5. What role do employee surveys/sentiment play — definitional or complementary?
6. What strategic decisions does the platform feed (hardware refresh, license reclamation, OS migration)?
7. How does the Type relate to ITSM (proactive vs reactive), UEM (observe vs configure), APM (endpoint vs service)?
8. Deployment and packaging variants: pure-play vs platform-embedded vs service-desk-led; SaaS vs on-prem; MSP multi-tenancy.
9. Historical check (§24): would pre-"DEX"-label products (late-1990s/2000s endpoint monitoring, early-2010s VDI operations consoles) still fit the definition?
10. Where exactly do the seams run vs the not-yet-processed siblings Digital Experience Monitoring and Endpoint Management / UEM?

## Representative Products

Selection rationale: market representativeness (all are recognized DEX tools — Lakeside and TeamViewer cite the 2026 Gartner Magic Quadrant for "DEX Management Tools" / "DEX tools"), documentation completeness, different product philosophies, different heritages and customer tiers.

| Product | Heritage / posture | Segment |
|---|---|---|
| Nexthink (Infinity) | Pure-play "digital workplace observability and automation" leader; data-model-first (NQL); broadest module set | Large enterprise |
| Lakeside Software (SysTrack) | Deepest endpoint telemetry veteran (1990s origins); engineering persona split (Assist/Resolve/Prevent); on-prem + cloud | Large enterprise, regulated |
| ControlUp (ONE Platform) | VDI/EUC operations console heritage (early 2010s); real-time remediation-first; physical + virtual | Mid-market → enterprise; MSP multi-tenancy |
| TeamViewer DEX (1E) | Endpoint-management automation heritage (SCCM-era tooling); service-desk ticket-avoidance philosophy | Enterprise; federal |
| Microsoft (Endpoint analytics, Intune) | Platform-native/embedded pole — DEX as a capability of an endpoint-management suite | Intune estates, all sizes |

## Sources

Tier 1 (official operational documentation):

- Nexthink — https://docs.nexthink.com/ — Platform overview; Platform capabilities; Understanding key data platform concepts (Data we collect and store; Data organization); Infinity Products. Fetched 2026-09-08.
- ControlUp — https://support.controlup.com/ — Knowledge Center index (llms.txt); Experience Scores. Fetched 2026-09-08.
- Lakeside Software — https://documentation.lakesidesoftware.com/ — Documentation portal index (llms.txt); About SysTrack. Fetched 2026-09-08.

Tier 2 (official product pages):

- Lakeside Software — https://www.lakesidesoftware.com/ (platform, capabilities, use cases). Fetched 2026-09-08.
- 1E / TeamViewer — https://www.1e.com/ (platform capability map, DEX glossary positioning) and https://www.teamviewer.com/en/products/dex/features/experience-analytics/ (Experience Analytics). Fetched 2026-09-08.
- 1E support portal — https://support.1e.com/ (migration notice: 1E joined TeamViewer in 2025; DEX support moved to support.teamviewer.com). Fetched 2026-09-08.

Not reachable (Source-access Limitation):

- Microsoft Learn Endpoint analytics documentation — three URL variants returned 404 (2026-09-08): /mem/analytics/endpoint-analytics, /intune/intune-service/analytics/endpoint-analytics, /mem/intune/fundamentals/endpoint-analytics. Abandoned per the retry rule. No precise operational claims about Microsoft Endpoint analytics are made anywhere in this research or the final document; the platform-native pole is included as a named representative product with its existence as a member of the Type noted at low assertion strength only.
- 1E documentation site (docs.1e.com) returned an empty body on 2026-09-08; 1E evidence is Tier-2 product pages only.

## Product A — Nexthink (Infinity)

### Key observations (evidence layer A unless noted)

Self-positioning (Tier 1 docs): "the market's first automation and remediation platform"; "the leading digital workplace observability and automation platform". Visibility scope named as: "employee devices, applications, operating systems, physical locations, network connectivity".

Data model (Tier 1 — the strongest structural evidence in the sample):

- Two data kinds: **objects** and **events**.
  - Inventory objects: `device` (name, CPU, OS…), `user` (name, username, department…), `binary` (name, size, version…).
  - Configuration objects: `monitors` (thresholds, priority), `campaigns` (status, trigger method), `remote_actions`, `applications`.
  - Events (time-linked occurrences): punctual (`execution.crash` — associated to user+device+binary; `session.login` — user+device, with metrics time_until_desktop_ready/visible; `device_performance.boot` — boot_duration) and sampled (`execution.events` — per-process CPU time/memory/traffic; `device_performance.events` — device CPU/memory/disk; `session.events` — RTT, latency, interaction_time). Collector samples every 20–30 seconds, aggregated into 5- or 15-minute buckets.
- Operational data (granular, ~30-day retention) vs trends (aggregated 1-day/7-day samples, up to 13 months).
- **DEX score is a precomputed metric**: computed daily, based on the past 7 days, stored as a punctual event; exists per user (`dex.scores`) and per application per user (`dex.application_scores`). (Direct, precise — vendor-documented mechanics.)
- Events associate to inventory objects; org structure enters via device/user classifications (Business Unit, Region) and custom fields; custom trends explicitly exclude PII.

Capability pillars (Tier 1 capabilities page): Real-time Alerting ("prioritize issue detection based on employee impact", prevent escalation into major incidents), Intelligent Diagnostics ("real-time analysis of digital experience telemetry… correlating data across the digital environment… visualize the scope and impact of issues"), Automated Remediation ("behind-the-scenes fixes without disrupting employees… targeted self-help notifications"), Integrations (import organizational context), Desktop Virtualization Experience (end-to-end VDI visibility; warns that "VDI solutions may be incorrectly blamed").

Products/modules (Tier 1 products page): Workplace / VDI / Mobile Experience (core — extends DEX to company-managed and BYO mobile), Application Experience (performance, reliability, adoption, licensing of all app types), Collaboration Experience (Teams/Zoom call quality), Employee Engagement (campaigns: targeted one-click self-help, pop-up notifications, feedback collection "never during a presentation or important meeting"), Experience Central (strategic DEX view for IT leaders — "Where do I stand? What should I improve? Where should I invest?"), Flow (low-code workflows triggering detection/orchestration/remediation across Nexthink data, remote actions, third-party tools), Guides (in-app guidance/"Adopt"), Amplify (browser plugin injecting DEX context, checklists, and remote actions into any service-desk tool for L1 agents), Spark (personal IT agent for employees — autonomous L1 handling under IT guardrails), AI Drive (genAI tool usage visibility), Nexthink Assist (LLM assistant).

Tooling surfaces (Tier 1/2): Investigations (NQL query language), Live Dashboards, remote actions with recorded executions, campaigns with recorded responses, ratings, custom fields, audit logs, APIs.

## Product B — Lakeside Software (SysTrack)

### Key observations

Self-positioning (Tier 1 "About SysTrack"): "an end point monitoring platform that leverages our embedded AI engine and rich data set to enable IT teams to proactively resolve complex issues. SysTrack captures data such as CPU, disk, memory, and other 10,000+ data points directly from the workspace." Stated outcomes: lower help desk tickets, identify over/under-provisioning, reduce time to resolution, track SLA performance, measure rollout performance. (The "10,000+ data points every 15 seconds" figure also appears on the Tier-2 marketing site — vendor claim, kept out of the final document.)

Persona-structured tools (Tier 1 documentation portal):

- **Assist** (L1 help desk technician): view system data, detected issues, system checklist, performance, automation history, tools; also "Assist for ITSM — ServiceNow" and L1-with-ServiceNow flows.
- **Resolve** (L2/L3 service and support, desktop engineer): deep per-system tools — Black Box, Health, System Usage, Dependencies, Hardware (+Hardware Diagram), Software, Faults, Web Apps / Web History / Web Performance, Boot/Logon Time, Logon Process, Event Correlation, Graphing, Comparative Analytics; use cases documented for slow-system response and boot/login issues.
- **Prevent** (proactive): current issues, notifications, sensor details/trends/patterns, root cause analysis, adverse impact of changes, "Evergreen IT Control Panel", IT announcements.
- **Visualizer + Dashboard Builder**: Desktop / Persona / Enterprise / Risk / Server / Virtual Infrastructure dashboards over datasets (application faults, application latency, boot and login, health, people, power, storage, software packages, security risk, user resource consumption…); dashboards built from query/data blocks, personas, tags, categories.
- **Configure**: roles; a large alarm taxonomy (application, boot time, latency, memory leaks, disk/GPU/ICA/PCoIP/network/system, security, VMware host alarms); tool schedules; **Survey Scheduler**; **Self Help App** (employee-facing); application management; automation.
- **Reliability Engineering** workflow (Tier 1): find issues to work on → investigate and create a Problem → fix and validate issues — an explicit managed issue lifecycle.
- **DEX Packs**: prebuilt packs "to uncover experience issues" (monthly DEX Pack / Action release notes).
- Cloud and On-Premises releases; SysTrack AI (anomalies, natural-language queries); Power BI connector; API ("programmatic access").
- Marketing site capability headers: Help Desk, Digital Employee Experience, Proactive IT, IT Transformations, Observability & Insights; use cases include hardware optimization, software license optimization, help desk ticket reduction, boot & login analysis, endpoint compliance; integrations include ServiceNow, Qualtrics (surveys), Citrix/VMware (VDI), Splunk, Power BI, Moveworks.
- Personas addressed (marketing): Executive Leadership, IT Engineering, Help Desk.

## Product C — ControlUp (ONE Platform)

### Key observations

Platform naming (Tier 1 docs): "ControlUp ONE Platform", repeatedly called the "DEX Platform" in its own documentation (URLs and titles: "Add Users to ControlUp DEX Platform", "Block Access to Sections of the DEX Platform", "DEX audit log") — direct vendor self-identification with the DEX category.

Product family (Tier 1 docs index):

- **ControlUp for Desktops** ("Edge DX"): agent deployment for Windows/macOS/Linux plus thin clients (IGEL, HP ThinPro, Stratodesk NoTouch, 10ZiG) and ChromeOS; Devices list; **Device Score** and "Device Health Score – Algorithms and Calculations"; End User Activity; Network Performance; Peripherals; Blue Screen Errors; Windows Event Logs; Device Health & Rightsizing dashboard; Remote Management (file browser, registry editor, real-time process/storage/network); Remote Assistance (remote control/shadow, remote shell, send messages); deployment via Intune/Jamf/MDM; Windows 365 and Amazon WorkSpaces monitoring.
- **Employees / Experience**: **Employees View** + **Employee Experience Drilldown**; **Experience Scores** (see below); **Employee Sentiment** (survey templates, publish and distribute surveys, view results); **Employee Identification (Approved Domains)** — privacy/identity scoping control; capturing VDI data for employees.
- **Experience Scores** (Tier 1, full detail): an employee's experience score starts at 10, reduced when metric conditions are met (e.g., CPU > 90%, app crashes with a configurable "lasting effect" window), weighted by condition; computed **every minute** using the previous minute's data; classified perfect/good/fair/poor via time thresholds; **scoring profiles** are customer-configurable, scoped by active app/URL/UCC call and device groups/tags, with collection targets for safe experimentation; scores are not recalculated retroactively when profiles change.
- **ControlUp for VDI & DaaS**: hypervisor and broker integrations (Citrix CVAD, Omnissa Horizon, AVD, Azure, AWS, NetScaler, vSAN); Sessions/Hosts/Machines/Processes views; logon duration, protocol trends; Remote DX endpoint-client metrics; multi-tenancy "with ensuring that demands from Service Provider and Tenants are met".
- **ControlUp for Apps**: App Groups and **App Score**; discovered apps tracking; **tracking app license utilization and unused spend**; Microsoft 365 license usage and costs.
- **ControlUp for Compliance** (Secure DX): templates, security checks, remediation status, custom scans/remediations, patching with automatic reboots — a drift zone toward endpoint management/compliance.
- **Events/Incidents Management**: static threshold alerts and **anomaly detection** alerts on devices; alert routing incl. ServiceNow integration.
- **Triggers → automated actions**: trigger packs, stress levels, webhooks, script-based actions; script library; workflows.
- **Scoutbees** (synthetic monitoring — separate product), **Unified Communications monitoring** (Teams/Zoom, live callers dashboard), **ControlUp AI / Pulse AI** (assistant, resolve), MCP server.
- Platform governance: RBAC + IdP SSO (Entra/Okta/DUO SAML), IP restrictions, audit logs, tenant manager, subscription/licensing.

## Product D — TeamViewer DEX (1E)

### Key observations (evidence layer A for existence/positioning; Tier-2-only detail)

- 1E joined TeamViewer in 2025 (support-portal migration notice; both sites state it). The product is now "TeamViewer DEX"; TeamViewer states it was named a Leader in the 2026 Gartner Magic Quadrant for DEX tools (market-category confirmation, vendor-claimed).
- Positioning (1E site): "real-time, autonomous digital employee experience platform fixes digital workplace issues fast and forever"; "Anticipate and prevent IT help desk calls with Intelligent EUC automation"; intercept "compliance drift, digital friction, and end-user frustration".
- Capability map (Tier 2): Intelligence, Business Impact, Experience Analytics, Endpoint Troubleshooting, Employee Sentiment, Endpoint Automation, Application Experience Management (AXM), Inventory Insights, Patch Insights, Synthetic Monitoring, Content Distribution for Microsoft Configuration Manager, Automated Self Service for ServiceNow, Service Desk Augmentation for ServiceNow, Virtual Desktop Experience (VDX). Solutions: Frictionless Experience, Seamless IT Operations, DEX for Microsoft Intune, Device Refresh, Software Reclaim.
- Experience Analytics detail (TeamViewer product page): "experience scores and analytics for performance, responsiveness, stability, network, and boot-ups"; score from "four categories: stability, responsiveness, performance, and sentiment"; endpoint + software monitoring combined with direct sentiment feedback; diagnostics with device history alongside real-time insights.
- 1E's own DEX glossary definition (Tier 2): "From the software and hardware used each day to IT interactions, DEX is the total of all digital touchpoints an employee encounters at work."
- Heritage: endpoint-management automation (SCCM content distribution still a product pillar) — shows the DEX category absorbing endpoint-management capabilities when the same vendor sells both.
- Sourcing limitation: 1E's documentation site (docs.1e.com) returned an empty body; all 1E evidence is product-page level. No precise operational mechanics asserted for this product.

## Product E — Microsoft (Endpoint analytics)

### Key observations

- Not directly verified in this pass (Microsoft Learn unreachable; see Sources). The product exists as the platform-native/embedded pole: DEX-class analytics (startup/app reliability scores, proactive remediations) delivered inside the Intune endpoint-management suite. Included in the sample as a packaging pole, with all detail deliberately omitted rather than filled from model memory. Historical/market-breadth role: shows the Type also exists as a free/bundled capability layer, which constrains how much the definition may assume (e.g., dedicated agents, per-minute scoring, survey machinery cannot be definitional).

## Cross-product Comparison

| Structure | Nexthink | Lakeside SysTrack | ControlUp | TeamViewer DEX (1E) | Microsoft Endpoint analytics | Layer |
|---|---|---|---|---|---|---|
| Endpoint instrumentation (agent/collector on employee devices) | yes (Collector, 20–30s sampling) | yes (agent; "data directly from the workspace") | yes (Edge DX agent; incl. thin clients/ChromeOS) | yes (endpoint agent; detail unverified — docs unreachable) | yes (platform-native; not verified) | A |
| Employee/user as first-class entity alongside device | yes (user objects; per-user DEX scores; classifications) | yes (People datasets; personas) | yes (Employees View; per-employee experience score; approved-domain identification) | yes (per-user experience; sentiment) | yes (per-user; not verified) | A |
| Device + OS + application + endpoint-experienced network telemetry | yes (devices/binaries/sessions/RTT) | yes (health/faults/web/boot+logon datasets) | yes (devices/apps/network/BSOD/event logs) | yes (stability/responsiveness/performance/network/boot) | yes (not verified) | A |
| Experience quantification (score or classified state) per employee / device / app | yes (DEX score daily per user + per app; 7-day basis) | yes (issue/sensor states; dashboards; reliability engineering "problems") | yes (employee experience score 0–10 per minute; device score; app score) | yes (experience score from 4 categories incl. sentiment) | yes (not verified) | A/B |
| Issue detection prioritized by employee impact (monitors/sensors/anomaly detection) | yes (real-time alerting; anomaly insights) | yes (Prevent; alarms taxonomy; sensor patterns) | yes (static + anomaly detection alerts; events/incidents) | yes (Intelligence; issue identification) | n/v | A |
| Diagnosis surfaces (per-device/session deep tools; correlated timeline) | yes (Investigations; diagnostics drill-down) | yes (Resolve: Black Box, Event Correlation, Boot/Logon, Faults…) | yes (device detail; live process/storage/network; Windows event logs) | yes (Endpoint Troubleshooting; diagnostics with device history) | n/v | A |
| Remediation machinery (remote actions/scripts/automations) | yes (remote actions; Flow workflows; behind-the-scenes fixes) | yes (automations; 220+ prebuilt per marketing; automation history) | yes (remote management actions; script-based actions; trigger packs) | yes (Endpoint Automation) | yes (remediations; not verified) | A |
| Guided employee self-help / targeted notifications | yes (Employee Engagement one-click self-help; Spark agent) | yes (Self Help App/Portal; IT announcements) | yes (send messages; Pulse AI Resolve self-service) | yes (Automated Self Service) | n/v | A |
| Employee sentiment surveys / campaigns | yes (Campaigns; Employee Engagement) | yes (Survey Scheduler; Qualtrics integration) | yes (Employee Sentiment surveys) | yes (Employee Sentiment; sentiment in score) | n/v | A |
| Service desk integration (ticket context / deflection) | yes (Amplify plugin for any service desk tool) | yes (Assist for ITSM–ServiceNow) | yes (ServiceNow alert integration) | yes (ServiceNow self-service + augmentation) | n/v | A |
| Application experience layer (crashes/hangs/load; web apps) | yes (Application Experience product) | yes (Faults/Web Apps/Web Performance tools) | yes (ControlUp for Apps; App Score) | yes (AXM) | n/v | A |
| Software/license & hardware estate intelligence (reclaim, refresh, rightsizing) | yes (SaaS license reclaim; hardware lifecycle optimization) | yes (hardware refresh; software license optimization use cases) | yes (license utilization/unused spend; rightsizing dashboard) | yes (Device Refresh; Software Reclaim; Inventory Insights) | n/v | A |
| VDI / virtual environment depth | yes (VDI Experience product) | yes (virtual infrastructure datasets/tools) | yes (ControlUp for VDI & DaaS — heritage strength) | yes (VDX add-on) | n/v | A |
| Collaboration/UCC call-quality monitoring | yes (Collaboration Experience) | (via app telemetry; not a named module) | yes (UCC monitoring, Teams/Zoom) | n/v | n/v | B (common in current products; 2/4 named) |
| Synthetic monitoring | (not a named module) | (not a named module) | yes (Scoutbees) | yes (add-on) | n/v | B-minus (2/4; optional) |
| Compliance/patch/posture machinery | no (not in module set) | yes (endpoint compliance use case) | yes (ControlUp for Compliance) | yes (Patch Insights; compliance drift) | yes (not verified) | B (2–3/4; variant — drifts toward endpoint management) |
| Mobile device experience | yes (Mobile Experience product) | (multi-platform support claim) | (via ChromeOS/thin client agents) | n/v | yes (not verified) | B-minus |
| Digital adoption / in-app guidance | yes (Guides/Adopt) | no | no | no | no | C (1/4; optional) |
| Agentic AI support layer (employee-facing or IT-facing) | yes (Spark, Assist) | yes (SysTrack AI) | yes (Pulse AI) | yes (autonomous positioning) | n/v | B (era-current, near-universal in 2026 sample; NOT definitional) |
| On-prem / hybrid deployment option | (SaaS; edocs legacy exists) | yes (on-prem releases) | yes (on-prem COP; hybrid cloud) | n/v | (cloud) | B (variant) |
| MSP / multi-tenancy | no evidence | no evidence | yes (multi-tenancy for service providers) | n/v | no | B (variant) |
| Strategic/executive experience-governance layer | yes (Experience Central) | yes (Executive Essentials; Evergreen IT) | (cost saving dashboard) | yes (Business Impact) | n/v | A/B |

n/v = not verified (no evidence fetched; Microsoft column largely n/v by the sourcing limitation).

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant (deliberately small; three jointly-held structures)

1. **Employee-side endpoint instrumentation as the telemetry source.** The platform's observations are collected continuously from the endpoints the employees themselves work on (a deployed collector/agent, a platform-native sensor, or an equivalent on-device instrument), covering the device and OS, the applications (desktop, web, virtual) the employee runs, and the connectivity/latency as experienced at the endpoint. Remove → server-side APM / network monitoring / device inventory: nothing observed at the point of the employee's experience.

2. **Experience assessment attributed to employees, devices, and applications.** Telemetry is not merely stored; it is evaluated into experience quantities — composite scores (per-employee DEX score, device health, application score) and/or classified issue states (degraded/failing sensors, problem records) — each attributed to the affected person, device, or application, computed over defined windows of the collected signals. Remove → a raw endpoint-telemetry pipeline / performance data feed with no experience semantics.

3. **The IT-owned experience-operations loop.** EUC/IT operations work the assessed experience population as a standing duty: detect and prioritize degradation by employee impact, diagnose by correlating endpoint telemetry, remediate (automated fix, remote action, guided self-help, or context handed to a ticket), and observe the experience state change. Remove → passive scorecard/BI; and a loop without structure 1 collapses into generic IT ops tooling running on ticket/inventory data.

Joint hold is load-bearing: 1+2 without 3 = telemetry analytics; 2+3 without 1 = a dashboard over someone else's data; 1+3 without 2 = device monitoring without experience semantics (ordinary infrastructure monitoring pointed at endpoints).

Wording notes: "score" specifically is NOT L0 (older realizations quantify via issue/problem states — see historical check); "survey/sentiment" is NOT L0 (absent in older and embedded realizations); "proactive (pre-ticket)" posture is NOT L0 (the loop also serves reactive diagnosis — what matters is that diagnosis is grounded in endpoint telemetry, not that a ticket doesn't exist); "management = remediation" is held inside structure 3 at the strength "act on the assessed experience", which all sampled products satisfy, while automation depth varies.

### L1 — Common Mature Structure (very common; not definitional)

- Experience scores as the headline surface (per-employee composite; per-device health; per-application), with configurable thresholds/weights/scopes; classification ladders (good/fair/poor-class).
- Monitors/sensors + anomaly detection emitting prioritized issues/alerts ranked by employee impact.
- Application experience layer: crash/hang counts, load/startup times, web errors, adoption/usage.
- Remediation libraries: remote actions, script libraries, automation/trigger machinery, one-click fixes.
- Employee-facing engagement: sentiment surveys/campaigns, targeted self-help notifications, announcements.
- Service desk integration: DEX context injected into tickets/agent consoles; alert routing; ticket deflection.
- Estate intelligence for decisions: hardware health/rightsizing/refresh planning; software license utilization/reclaim; OS-migration readiness.
- Org-context mapping (users/devices to business units, locations, tags) and role-based access.
- Exports/integrations (ITSM, BI, SIEM-class), APIs; privacy and employee-identification configuration surfaces.

### L2 — Variant / Optional Structure

- Heritage/packaging: pure-play DEX platform vs endpoint-management-embedded (Intune-class analytics; endpoint-suite add-ons) vs VDI-operations-first vs service-desk-automation-first.
- Telemetry philosophy: deep always-on agent vs lightweight/platform-native sensor vs browser-extension supplements.
- Environment scope: physical desktops first vs VDI/DaaS-first; thin-client/ChromeOS estates; mobile/BYO extension.
- Deployment: SaaS vs on-prem/hybrid; multi-tenant for MSPs.
- Optional module families: synthetic monitoring, collaboration/UCC call quality, compliance/patch posture, digital adoption/in-app guidance, AI agents/copilots.
- Strategic governance layers (executive scorecards, business-impact quantification, cost/productivity models).

### L3 — Vendor-specific Structure (Research Notes only)

- Nexthink: NQL query language and Investigations; dex.scores computed daily over 7-day windows (precise mechanics are Nexthink-documented); Collector 20–30s sampling; 5/15-minute aggregation buckets; 30-day operational vs 13-month trend retention; "Infinity" product/module names (Workplace/VDI/Mobile Experience, Experience Central, Flow, Amplify, Spark, AI Drive, Guides); "managing over 15 million endpoints" (vendor claim).
- Lakeside: Assist/Resolve/Prevent/Visualizer tool naming; Black Box tool; reliability-engineering "Problem" object; DEX Packs; sensor/automation counts (1,300+/220+ — inconsistent between pages; excluded); "10,000+ data points every 15 seconds" (vendor claim); Evergreen IT Control Panel.
- ControlUp: experience score starting at 10, computed every minute, 5% classification thresholds; scoring profiles with app/URL/UCC scoping and collection targets; Edge DX agent; Scoutbees; Secure DX; trigger packs/stress levels; tenant manager.
- 1E/TeamViewer: 1E→TeamViewer acquisition (2025); Nomad/SCCM content-distribution heritage; "fast and forever" positioning; ServiceNow add-on pairs.
- Gartner category: "Magic Quadrant for DEX (Management) Tools" cited by two vendors — the market category name matches the directory leaf naming.

## Rejected Findings

- **"DEX = employee sentiment + surveys"** — rejected as defining. Surveys are absent from older realizations and from the embedded pole; telemetry-driven assessment carries the Type alone. Surveys are L1.
- **"DEX = Gartner-category tooling, therefore requires a composite DEX score"** — rejected. SysTrack's historical form and issue-state-based assessment satisfy the Type without a single composite score; the abstraction is "experience assessment" (scores and/or classified states).
- **"DEX management must be proactive (before any ticket)"** — rejected as invariant. The loop's trigger may be proactive detection or a help-desk ticket (SysTrack Assist's L1 use case; Amplify's in-ticket context); the invariant is that diagnosis is grounded in endpoint telemetry rather than in ticket records alone.
- **"DEX = any employee-facing IT tool"** — rejected. Employee self-help portals or IT communication tools alone lack structures 1–2 (no endpoint telemetry, no experience assessment).
- **"Endpoint telemetry collection makes DEX a surveillance/monitoring-of-people Type"** — rejected for the Type definition; products expose employee-identification scoping and privacy configuration, and the estate is IT-owned devices. (Ethical/regulatory variant noted in Uncertainties.)

## Boundary Findings

1. **vs Employee Experience Platform (§09, processed) — RATIFIED from the DEX side; keep-both.** Same two words, different estates. DEX (this leaf): IT-owned endpoint/application performance telemetry; buyers are EUC/IT ops; objects are devices/binaries/sessions/experience scores. EX platform: HR/comms-owned organizational experience (content, listening, journeys, services). Direct evidence of the separation: Nexthink — the most DEX-native vendor — names its HR-adjacent module "Employee Engagement" and keeps it campaign/notification-scoped, while the §09 sample excluded IT telemetry by definition. Remove endpoint instrumentation → EX platform; remove organizational-experience surfaces → DEX.

2. **vs APM (§14, processed) — keep-both; instrumentation locus is the seam.** APM instruments inside server-side application services and measures request/operation performance for engineering teams (per the APM pass's own L0). DEX instruments the employee's endpoint and measures experience of the whole workspace (device, OS, apps, connectivity) for IT/EUC teams. Both may observe "the same app is slow" from opposite ends; DEX platforms may consume APM context via integrations (Nexthink "intelligent integrations… importing data from current systems"). Remove endpoint instrumentation → APM/network monitoring territory; remove service-side request telemetry and DEX remains.

3. **vs Digital Experience Monitoring (§14, NOT yet processed) — flagged for joint review.** Both Types are "experience monitoring" families in §14. Working split proposed from this side: DEM measures application/service experience for the IT service owner (synthetic checks, real-user monitoring, network paths) where the employee is one of many traffic sources; DEX takes the employee's workspace itself as the unit (person + device + apps + connectivity as experienced) and adds the remediation/management loop. Overlap zone is real: some DEX tools ship synthetic monitoring (ControlUp Scoutbees, 1E add-on), and DEM tools measure employee-side sessions. Candidate relationship: sibling Types with a partial-overlap gradient; joint review when the DEM leaf is processed. Recorded in STATUS.md.

4. **vs Endpoint Management / UEM (§14, NOT yet processed) — keep-distinct; flag for cross-check.** UEM owns device configuration, policy, and security state (enforce settings, deploy software, wipe); DEX observes experience and acts on issues but owns no configuration policy. DEX consumes UEM context (deploy the DEX agent via UEM — ControlUp documents Intune/Jamf deployment; org structure often mirrors UEM groups). Drift zone: compliance/patch machinery inside DEX platforms (ControlUp for Compliance; 1E Patch Insights) — variant capability, not the core. Flag recorded so the UEM pass can confirm the seam.

5. **vs ITSM / Help Desk (§07, not yet processed) — complementary; no object overlap.** ITSM's record is the ticket; DEX's record is telemetry + experience assessment. Integration runs both ways (DEX context into ticket consoles; tickets enriched/created from DEX alerts) and a stated goal is ticket avoidance — but the DEX loop exists without tickets and vice versa.

6. **vs Employee Service Management (§10, processed) — ratified (finding 9 of that pass).** DEX monitors; ESM fulfills requests. Same word, different objects and owners.

7. **vs Remote Monitoring & Management (§14, not yet processed).** RMM is the MSP-operated device management/monitoring sibling: fleet health + remote access + patching across client organizations. Shared machinery (endpoint agents, remote actions) but the unit of concern differs (device fleet vs employee experience). ControlUp's MSP multi-tenancy shows the products can serve both postures from one platform — a variant, not an identity.

8. **vs Desktop & Application Delivery (§14, processed).** Delivery owns hosting and streaming apps/desktops to endpoints; DEX observes the experience of those (and native) workspaces. VDI sessions are a first-class monitored context in DEX (all sampled vendors), and the Nexthink docs explicitly frame "VDI may be incorrectly blamed" as the attribution problem DEX solves across delivery infrastructure.

9. **vs Product Usage / Adoption Platform (§07, processed) — seam noted by that pass.** Browser-extension employee analytics (app catalog, license utilization) approaches DEX from the marketing-analytics side; it remains a variant posture of that Type. The DEX side's center is endpoint/OS/device telemetry, which adoption platforms do not collect.

10. **vs Enterprise Browser DEX analytics (browser-security-platform research).** Enterprise browsers ship DEX-flavored analytics; scope is the browser session, not the workspace. Capability relationship; no leaf collision.

### "Remove what → becomes the other Type" summary

- Remove endpoint/employee-side instrumentation → APM, DEM, or generic IT ops (structure lost).
- Remove experience assessment → raw telemetry/logging pipelines.
- Remove the IT operations/remediation loop → DEX analytics scorecard (not "management").
- Remove the employee-as-subject framing (keep fleet aggregates only) → device/infrastructure monitoring.
- Remove telemetry + assessment, keep content/listening/journeys → Employee Experience Platform (§09).

## Historical / Market-Sample Check (§24)

- **Lakeside SysTrack predates the "DEX" label** (vendor heritage since the late 1990s as endpoint monitoring; the sampled documentation retains no score-centric definition — its spine is agent + sensors/alarms + per-system deep tools + problem lifecycle). It satisfies structures 1–3 without any composite experience score, confirming that "score" belongs to L1, not L0.
- **ControlUp began as a VDI/Terminal-Services operations console** (real-time session monitoring + actions) — satisfies the core with virtual sessions as the endpoint surface and score columns as assessment; the per-employee minute-cadence score is a modern layer.
- **Platform-native embedded pole** (Intune-class analytics) shows the Type without deep agents or survey machinery.
- **Early desktop-management suites** (inventory/deployment/config tools of the 2000s) would NOT satisfy the core — no experience assessment, no experience loop; they are the ancestor of UEM, which sharpens boundary 4.
- Conclusion: the L0 holds across eras if phrased as telemetry + assessment + loop; score compositing, sentiment, and AI layers are era-current mass.

## Uncertainties

- Microsoft Endpoint analytics detail unverified (docs unreachable); platform-native claims kept at existence-strength only.
- 1E operational mechanics unverified (docs site empty); product-page evidence only.
- Whether the market consolidates DEX into endpoint-management suites (TeamViewer/Intune/Workspace-ONE-class) faster than pure-plays — trend risk noted for the Type's packaging variants, not its definition.
- Privacy posture strength: sampled products expose privacy/identification controls (ControlUp approved domains; Lakeside Privacy settings page; Nexthink PII-free custom trends), but no cross-product privacy-regime claim is made beyond "configuration surfaces exist"; works-council/regulatory constraints on employee telemetry vary by jurisdiction and are not researched here.
- Exact scoring mechanics (windows, cadence, weights) are vendor-specific (Nexthink daily/7-day; ControlUp per-minute/0–10); no cross-product scoring standard exists or is claimed.

## Final Synthesis

A Digital Employee Experience Management platform is the IT-owned instrument-and-act layer over the employee's digital workspace. Its world has three jointly-held structures: telemetry collected continuously from the endpoints employees actually work on (devices, OS, applications, endpoint-experienced connectivity); that telemetry evaluated into experience assessments — composite scores and classified issue states — attributed to specific employees, devices, and applications; and an operations loop owned by EUC/IT teams that prioritizes degradation by employee impact, diagnoses it through correlated endpoint telemetry, remediates it (automation, remote actions, guided self-help, or ticket context), and observes the state change. Around that spine, mature products add scoring systems, application-experience and license/hardware estate intelligence, sentiment campaigns, service-desk integration, VDI and collaboration depth, and — in the current era — AI agents. The Type is bounded on one side by observability Types that measure services rather than the employee's workspace (APM, DEM), and on the other by the HR-owned Employee Experience Platform family that shares two words of the name but nothing of the estate. The market sells this category under the exact leaf name (vendor-cited "DEX Management Tools"), so the leaf stands as a distinct Type with ratified name-collision boundaries rather than an alias.
