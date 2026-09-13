# Research Notes — SRE Management

## Research Goal

Understand what the Application Type "SRE Management" is as a real product category: what objects its products hold as records, what loops they run, how they relate to the neighboring §14 Types (Observability Platform, Incident Management, On-call Management, ITSM), and whether the directory leaf is a coherent Type, an umbrella label, or an alias.

Special obligation carried into this pass: the on-call-management pass (processed 2026-09-09) left a forward flag — "practice umbrella (SLOs/error budgets/toil) vs one practice's machinery — joint review expected on that side". This pass must discharge it.

## Initial Boundary

Working hypothesis at start:

- SRE (Site Reliability Engineering) is a practice (Google-originated, formalized in the SRE books). "SRE Management" as an Application Type would be the tooling layer for that practice.
- Expected neighbors: Observability Platform (telemetry), Incident Management (response records), On-call Management (coverage machinery), ITSM (service management suite), Internal Developer Portal (service catalog).
- Expected risk: "SRE platform" may be a marketing umbrella over incident + on-call + SLO machinery rather than a distinct Type.

## Research Questions

1. What is the unit of record in products sold for SRE management — the incident, the service, the SLO, the toil item?
2. What is the SLO/error-budget machinery, exactly: what is defined, what is measured, what is computed, what triggers action?
3. Where does the measurement come from (telemetry? monitors? incidents? active tests?) and is that definitional or variant?
4. Do any products hold "toil" as a managed object?
5. Is there a coherent "SRE umbrella" product, or do "SRE platform"-labeled products reduce to neighboring Types plus an SLO module?
6. Where are the seams vs Observability, Incident Management, On-call, ITSM, and the service catalog / developer portal?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different packaging/customer tiers:

| Product | Philosophy / pole | Tier |
|---|---|---|
| Nobl9 | standalone SLO platform ("Reliability Center") — pure SLO/error-budget machinery over external telemetry | enterprise |
| SolarWinds Incident Response (formerly Squadcast) | incident-response suite with an SLO Tracker module — SLOs computed from incidents | mid-market |
| Gremlin | "Enterprise Reliability Platform" — reliability managed via active fault-injection testing and scoring | enterprise |
| Datadog (Service Level Objectives) | SLO machinery embedded in an observability mega-suite | enterprise |
| Grafana SLO | SLO machinery in an OSS-rooted observability stack | OSS → enterprise |

Market-structure evidence also collected: Blameless (formerly self-labeled "SRE platform") now redirects to FireHydrant, which positions as incident management (Plan/Respond/Improve: runbooks, on-call, service catalog, retrospectives) with no SLO machinery on its homepage. Squadcast was absorbed by SolarWinds. These consolidations are evidence about how the "SRE platform" umbrella label behaves in the market.

## Sources

All fetched 2026-09-09 (Layer A unless noted):

- Nobl9 — Documentation home ("Nobl9 Reliability Center"): https://docs.nobl9.com/
- Nobl9 — Service level objectives: https://docs.nobl9.com/service-level-objectives/
- SolarWinds Incident Response (Squadcast) — docs sitemap: https://support.incidents.cloud.solarwinds.com/sitemap.md
- SolarWinds Incident Response (Squadcast) — SLO Basics: https://support.incidents.cloud.solarwinds.com/slo-tracker/slo-basics.md
- SolarWinds Incident Response (Squadcast) — Configure and Monitor your SLOs: https://support.incidents.cloud.solarwinds.com/slo-tracker/configure-and-monitor-your-slos.md
- Gremlin — Docs home: https://www.gremlin.com/docs/
- Gremlin — Reliability Management overview: https://www.gremlin.com/docs/reliability-management-overview
- Gremlin — Reliability Score: https://www.gremlin.com/docs/reliability-management-reliability-score
- Datadog — Service Level Objectives: https://docs.datadoghq.com/service_management/service_level_objectives/
- Grafana — Grafana SLO overview: https://grafana.com/docs/grafana-cloud/alerting-and-irm/slo/
- FireHydrant (Blameless successor) — homepage: https://www.blameless.com/ (redirects to FireHydrant)

Unreachable / not fetched:

- Cortex docs (service catalog / scorecards): one 404 on the guessed SLO path; not retried per the network-restriction rule. The IDP seam below rests on the internal-developer-portal pass's recorded Tier-1 evidence (Port glossary "view scorecards"; Cortex report card), at moderate confidence.
- Google SRE book (sre.google) — cited by sampled vendors' own docs (Squadcast cites the SRE book's SLO chapter and workbook); not fetched directly. Practice-lineage statements rest on the vendors' citations.

## Product Observations

### Nobl9 (Layer A)

Positioning: "Nobl9 Reliability Center transforms reliability engineering into actionable insights by making service level objectives (SLOs) accessible and practical for your entire organization. Our enterprise-grade SaaS platform integrates with your existing monitoring and observability tools, enabling DevOps and SRE teams to define SLOs and track error budgets."

Object model:

- **SLO** — "the core concept of reliability engineering... defines the target performance level you expect from your service". In Nobl9, an SLO unit corresponds to a unique error budget calculation; every SLO requires a connection to a data source and at least one configured error budget; each additional SLO target creates another error budget to track.
- **SLI** — "quantifiable metrics that measure specific aspects of your service's performance".
- **Error budget** — "your allowance for failure — the acceptable number of errors or performance issues while still meeting your reliability targets. Error budgets help balance reliability with innovation."
- **Services and projects** as organizing containers; services carry assigned responsible users.
- **Composite SLOs** — multiple SLOs combined into a unified view.
- **Data sources** — external monitoring systems ingested via the Nobl9 agent (the platform does not itself collect telemetry).

Loops and features:

- Budget burn alerting: "Get notified when your budget burns too fast — receive alerts based on error budget conditions that get ahead of outages and signal action at the right level of urgency"; alert policies with fast-and-slow-burn use cases.
- SLI Analyzer — query historical SLI data from a source to pick targets before committing.
- Replay — backfill/recalculate error budgets when source data was missing.
- Budget adjustments — adjust budgets (API provided).
- Reliability Roll-Up report — "overall system Reliability Score, with an option to drill down into each SLO factor".
- Service health dashboard — "View service health at a glance... Keep your services organized so you always know where attention is required."
- SLO oversight (Enterprise) — reviews, data-anomaly auto-detection, oversight dashboard.
- SLOs as code — sloctl CLI, Terraform provider, OpenSLO spec (Nobl9-sponsored); SLODLC (SLO development lifecycle) community methodology.
- Framing: "With Nobl9, you can break the endless cycle of toil and tech debt: find the right balance between moving your product forward and fixing bugs." (Error-budget-policy framing; toil appears as practice vocabulary, not as a managed object.)

What it does NOT hold: no incident records, no on-call schedules, no telemetry collection of its own.

### SolarWinds Incident Response, formerly Squadcast (Layer A)

Positioning: an incident-management platform (services, alert dedup/routing/grouping, on-call schedules, escalation policies, incidents, postmortems, status pages, runbooks, workflows, analytics) with an **SLO Tracker** module. Its SLO docs frame SLOs as "a fundamental part of their Site Reliability Engineering (SRE) practice" and cite the Google SRE book.

SLO object:

- Definition: name, description, tags (owner/environment/type).
- **Services associated with this SLO** — multiple services linked; "Only incidents from these linked Services can then be mapped to the SLO".
- **SLIs** — "There could be one or more SLIs - like availability, response time, etc - that map to this SLO".
- **Target SLO in %** — the compliance target.
- **Error budget** — "auto-calculated based on the values entered for target SLO and duration. It is calculated in minutes and cannot be edited."
- **Duration** — rolling period (max 90 days) or fixed/calendar duration (max one year). At end of duration the SLO "transitions into an inactive state... uneditable".

Measurement substrate — **incidents**: the SLO list shows "Incidents Reported"; the detail page shows "Error Budget Consumed", MTTA/MTTR "of the SLO-violating incidents", and "Error Budget Consumed by SLIs" with per-SLI incident counts. Incidents are promoted to SLO violations (manually or via Workflows; product-specific rate limits documented). **False positives** — incidents initially counted against the SLO can be marked as false positives ("acts like an 'undo' button") and restored.

Error Budget Policy: alert conditions — budget breach, unhealthy burn rate ("error budget is burning faster than what's expected"), false positives exceeding a limit, budget below a limit — delivered as **Email or as an Incident created for the specified service**.

Health semantics: SLO Health "Healthy / Needs Attention", determined by how rapidly the budget is depleted relative to the elapsed share of the window (product-specific formula documented in FAQ).

Terminology page (Layer A, practice framing): SLA (agreement with consequences), SLO (agreement within an SLA about a metric over time), SLI (measurement of compliance), error budget (max acceptable downtime), burn rate (how fast the budget is consumed); rolling vs fixed windows; guidance to keep SLOs "slightly stricter than what you detail in your SLAs"; a 7-step definition process (user journey → services/SLI type → SLI → SLO → error budget policy → monitor/report → periodic re-evaluation).

### Gremlin (Layer A)

Positioning: "The Enterprise Reliability Platform". Two halves: **Reliability Management (RM)** and **Chaos Engineering** (fault injection: experiments, scenarios, GameDays; Failure Flags; Foresight AI). Use-case list includes "Build a Reliability Program".

RM object model:

- **Services** — "a discrete unit of functionality provided by one or more systems... In Gremlin, services are the units used to test and measure the reliability of your system" (process on hosts/containers/Kubernetes; auto-onboarding).
- **Dependencies** — automatically identified and testable.
- **Detected Risks** — "Continuously monitor systems for critical reliability risks."
- **Test suites / reliability tests** — "tests several key reliability behaviors of each service including its scalability, redundancy, and ability to tolerate failed or slow dependencies."
- **Health checks** — monitor service state before/during/after tests; "if your systems become unstable... Health Checks will automatically halt ongoing tests".
- **Reliability Score** — "a value between 0 and 100 that indicates how well your services are meeting your team's reliability standards. The reliability score isn't a measure of uptime or availability, but instead provides a standard way of measuring reliability across all teams and services in your organization." Computed from detected risks + reliability-test outcomes (+ optional "Extra Credit" scenario runs); per-test scores (passed 100 / expired 75 / failed 50 / not-run 0 — product-specific), averaged over categories (Redundancy, Scalability, Dependencies, Other); weekly score; tests expire if not re-run.

What it does NOT hold: no SLO objects, no error budgets, no incident records, no on-call. The "expectation" is embodied in the team's reliability standards realized as the service's test suite; the "tracked state" is the score; the loop is test → score → fix risks → re-test.

### Datadog — Service Level Objectives (Layer A)

Positioning: observability platform; "Service Level Objectives, or SLOs, are a key part of the site reliability engineering toolkit. SLOs provide a framework for defining clear targets around application performance, which ultimately help teams provide a consistent customer experience, balance feature development with platform stability, and improve communication with internal and external users."

Object model (terminology): SLI ("a metric or an aggregation of one or more monitors"), SLO ("a target percentage for an SLI over a specific period of time"), SLA ("explicit or implicit agreement... stipulating... consequences"), error budget ("the allowed amount of unreliability derived from an SLO's target percentage (100% - target percentage) that is meant to be invested into product development").

SLO types: metric-based (count-based: good events / total events), monitor-based (time-based: monitor uptime), time-slice (custom uptime definition without requiring a monitor).

Mechanics:

- Rolling time windows (7/30/90 days); targets strictly below 100% required ("Setting a 100% target means having an error budget of 0%... you face difficulty finding alignment between the conflicting priorities of maintaining customer-facing reliability and investing in feature development"; also division-by-zero in alert evaluation).
- Error-budget-remaining formula; grouped SLOs show per-group status and budget.
- **Burn-rate indicators** on the SLO list: rolling 2-hour window; critical above a threshold, elevated between thresholds (product-specific numeric thresholds documented); filterable by Critical/Elevated/Healthy; links to the service page.
- **SLO status corrections** — exclude time periods from status/budget calculations (scheduled maintenance, outside business hours, deployment, other; one-time or recurring per iCalendar RRULE; per-SLO limits).
- SLO alerts (burn-rate-based); audit events for SLO and correction changes; RBAC permissions (slos_write, slos_corrections); saved views; grouping by any tag (service, team, user journey, tier); calendar view; dashboards widgets; SLO data source for historical graphing; Terraform resource; mobile app.

What the SLO machinery does NOT hold: incident records (separate Incident Management module), on-call (separate module), coverage machinery.

### Grafana SLO (Layer A)

Positioning: "Grafana SLO (Service Level Objective) provides a framework for measuring the quality of the service you provide to users. Use SLOs to collect data on the reliability of your systems over time and as a result, help engineering teams reduce alert fatigue, focus on reliability, and provide better service to your customers. By creating SLIs and SLOs, you define what an acceptable level of service is and how to react if you are not providing the expected level of service."

Features (from the docs overview): SLO concepts and best practices; a five-step SLO creation process with alert-rule configuration; an SLO dashboard showing "burn rate, error budget, SLI results and more"; **maintenance windows** — "Schedule planned work to pause error budget consumption and burn rate alerting for selected SLOs."

### FireHydrant / Blameless absorption (Layer A, market structure)

blameless.com now serves FireHydrant's site: "All-in-One Alerting, On-Call, and Incident Management... One platform that does it all. On-call, AI-enriched automation, retrospectives." Platform pillars: Plan (automated runbooks, on-call & alerting, service catalog), Respond (collaboration, AI insights, status pages), Improve (AI-enhanced retrospectives, follow-ups, analytics). No SLO/error-budget machinery on the homepage. The formerly "SRE platform"-labeled Blameless has been absorbed into an incident-management platform. (Whether SLOs exist deeper in FireHydrant was not verified; the absorption itself is the evidence used.)

## Cross-product Comparison

| Dimension | Nobl9 | SolarWinds IR (Squadcast) | Gremlin | Datadog | Grafana |
|---|---|---|---|---|---|
| Reliability expectation record | SLO: target + SLI + budget, per data source | SLO: target % + SLIs + linked services + window | team's reliability standards embodied in the service's test suite | SLO: target % on SLI over window | SLO: SLI + target |
| Subject of the objective | services (in projects) | services (multiple per SLO) | services | monitors/metrics, grouped by service/team tags | services (labels) |
| Measurement substrate | external telemetry via agent/sources | incidents on linked services | fault-injection test outcomes + detected risks | native metrics / monitors / time slices | native metrics |
| Managed quantity | error budget(s) per target | error budget in minutes (incident-derived) | reliability score 0–100 (weekly) | error budget remaining % | error budget + burn rate |
| Burn / health evaluation | burn alerts (fast/slow burn policies) | Healthy / Needs Attention; burn-rate policy alerts | score decay via test expiry; detected risks | burn-rate indicators (elevated/critical) | burn-rate alerts |
| Action delivery | alert policies / notifications | email or incident creation | test halts, risk surfacing, reports | alerts; links to service page | alert rules |
| Aggregation | composite SLOs; Reliability Roll-Up score | per-SLO detail; MTTA/MTTR of violating incidents | per-service score; category averages | grouping by tags; SLO list widgets | SLO dashboard |
| Exclusions / adjustments | budget adjustments; Replay backfill | false-positive marking | extra credit (additive only) | status corrections (categories, RRULE, limits) | maintenance windows |
| Program surfaces | oversight reviews; data-anomaly detection; as-code (OpenSLO/sloctl/Terraform) | embedded in incident suite (postmortems, status pages) | GameDays; DR tests; Foresight AI | audit events; saved views; calendar; Terraform | best-practices docs; dashboard |
| Incident response in the same product | no | yes (the platform's center) | no | separate module | separate (IRM) |
| On-call in the same product | no | yes | no | separate module | separate (IRM) |
| Toil as a managed object | no (vocabulary only) | no | no | no | no |

Reading of the comparison:

- The **reliability expectation held as a record for a service** is present in all five — as an explicit SLO object in four, as test-suite-embodied standards in Gremlin.
- The **tracked reliability state** is present in all five — as error budget/compliance in four, as a score in Gremlin.
- The **management loop** (state → alerts/action → re-evaluation) is present in all five.
- The **error budget** specifically is 4/5 — common-mature, not definitional (Gremlin's score pole proves the Type survives without it).
- The **SLI substrate** differs across all five poles — telemetry, incidents, tests, monitors — clearly a variant axis, not definitional.
- **Incident response and on-call** appear in only one of five (the incident-suite pole) — bundling, not identity.
- **Toil** appears in none as a managed object — practice vocabulary only.

## Canonical Model

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The reliability objective as the unit of record.** A persistent, identified record of a defined reliability expectation for an identified subject — dominantly a service — expressed as a target on a measured indicator over a time window (the market's SLO), or embodied as the standards a subject must continuously meet (the testing pole's test suite). Remove → monitoring dashboards with no objective, or a catalog with target annotations and no measurement.
2. **The tracked reliability state.** Ongoing measurement or verification of actual reliability against the objective, computed and held as a state over the window: compliance percentage, error budget remaining/burned, or a reliability score, with health/burn evaluation. Remove → raw telemetry charts (Observability territory) or one-off test reports.
3. **The reliability management loop.** The objective's state drives action — alerts when the budget burns too fast or compliance is at risk, delivery into notification/incident channels, remediation or testing responses — and the objective itself is periodically re-evaluated and revised. Remove → a static targets document or scorecard report.

Jointly-held load-bearing analysis:

- 1 alone = a targets document / annotated service catalog
- 2 without 1 = telemetry dashboards / threshold monitoring (Infrastructure Monitoring / Observability territory)
- 3 without 1+2 = generic alerting with nothing managed
- 1+2 without 3 = a static scorecard/report
- 1+3 without 2 = aspirations with no measurement
- 2+3 without 1 = threshold alerting (monitoring territory)

### Level 1 — Common Mature Structure

- Error-budget computation and remaining/burned tracking (4/5 sampled)
- Burn-rate evaluation and burn-rate-based alerting, with urgency tiers (fast/slow burn) (4/5)
- SLI definition machinery: metric queries, monitor uptime, time slices, incident mapping, test outcomes
- SLO dashboards: compliance %, budget remaining, history, per-group breakdowns
- Time windows (rolling / fixed-calendar) and governed exclusions (maintenance windows, status corrections, budget adjustments, false-positive marking)
- Aggregation: composite SLOs, roll-up scores, per-service scores, tag grouping
- Ownership, tags, permissions, audit history of objective changes
- Definition-as-code and APIs (OpenSLO, Terraform, CLIs)
- Delivery of burn alerts into notification and incident-creation channels

### Level 2 — Variant / Optional Structure

- **SLI substrate** (the sharpest variant axis): external telemetry ingestion (Nobl9) / native monitors and metrics (Datadog, Grafana) / incident-derived (Squadcast) / active fault-injection tests (Gremlin)
- **Packaging**: standalone SLO platform / observability-suite-embedded / incident-suite module / testing-platform program layer
- **Managed-quantity realization**: error budget (dominant) vs reliability score (Gremlin)
- **Program surfaces**: SLO oversight reviews, data-anomaly detection, GameDays / DR tests, service-catalog integration, SLA linkage guidance (keep SLOs stricter than SLAs)
- **Toil**: practice vocabulary in vendor copy; not a managed object in any sampled product — not even a standard capability

### Level 3 — Vendor-specific Structure

- Nobl9: sloctl CLI; OpenSLO spec and SLODLC stewardship; Replay backfill; SLI Analyzer; Reliability Roll-Up; budget-adjustments API; Nobl9 Assist (AI); Enterprise SLO oversight
- Datadog: burn-rate indicator thresholds (2-hour rolling window; numeric critical/elevated bands); status corrections with iCalendar RRULE recurrence and per-SLO limits; SLO calendar view; 15-month SLO data source; metric/monitor/time-slice SLO typing; monitor-based SLOs bound to monitor definitions
- SolarWinds IR (Squadcast): incident-promotion model with documented rate limits (per-hour promotion cap; overlapping-incident cap); false-positive marking with undo; SLO becomes inactive/uneditable at window end; MTTA/MTTR per SLO; error budget auto-calculated in minutes, non-editable
- Gremlin: 0–100 weekly reliability score with per-test scoring table (passed/expired/failed/not-run), category averaging, Extra Credit additive points, health-check-gated test halting, detected risks, dependency discovery, GameDays, DR tests, Foresight AI
- Grafana: five-step SLO creation; maintenance windows pausing budget consumption and burn alerting

## Vendor-specific Findings

- The "SRE platform" umbrella label dissolves on inspection: Blameless (formerly the label's clearest carrier) is absorbed into FireHydrant's incident-management platform; Squadcast is absorbed into SolarWinds Incident Response; both keep incident response as the center and SLOs as a module (Squadcast) or drop SLOs from the front door entirely (FireHydrant).
- Squadcast's SLO model is incident-derived — a structurally different measurement substrate from Datadog/Grafana (monitors/metrics) and Nobl9 (external telemetry) — the strongest single piece of evidence that the SLI substrate is variant, not definitional.
- Gremlin proves the Type survives with no SLO object and no error budget at all: standards embodied in test suites + a score + a test-fix-retest loop.
- Datadog's own docs articulate the budget's purpose as the alignment mechanism ("balance feature development with platform stability"), matching Nobl9's and Squadcast's framing — the reliability-vs-velocity negotiation is the practice's center of gravity, realized in product as budget states and burn alerts.

## Boundary Findings

**vs Observability Platform — keep both.** Unit-of-record seam: observability holds telemetry signals (multi-signal ingestion + shared context + cross-signal investigation); SRE Management holds reliability objectives and the program loop over measured state. Consistent with the observability pass, which held SLOs as standard-NOT-definitional for that Type. The Nobl9 pole (no telemetry collection of its own; integrates with existing monitoring) proves an SRE-management product needs no telemetry engine; an observability platform needs no objective layer.

**vs Incident Management — keep both.** Unit-of-record seam: incident management holds the response record (declare → respond → resolve); SRE Management holds the reliability objective that incidents are measured against. Fusion is common and runs both directions: Squadcast computes budgets from incidents and delivers burn alerts as incidents; Datadog ships SLOs and Incident Management as separate modules. Neither pole merges: Nobl9, Gremlin, and the Datadog/Grafana SLO machinery hold no incident record.

**vs On-call Management — keep both; FORWARD FLAG DISCHARGED.** The on-call pass flagged "practice umbrella (SLOs/error budgets/toil) vs one practice's machinery". Findings: the umbrella reading fails. (a) No sampled product holds incident + on-call + SLO + toil as one coherent SRE-specific record base — the products marketed as "SRE platforms" are incident platforms with an SLO module (Squadcast) or have been absorbed into incident platforms (Blameless → FireHydrant). (b) Toil is held as a managed object by no sampled product — it is practice vocabulary in vendor copy. The "one practice's machinery" reading is closer but needs generalizing: the machinery is the reliability-objective practice (SLO/error-budget being its dominant realization), and the Type's core is the objective + tracked state + management loop — not the union of neighboring Types' machinery. On-call and incident response remain separate Types that SRE-management products consume as action channels (burn alerts delivered as pages/incidents). The on-call pass's Related-Types row ("practice umbrella; on-call is one practice within it") is hereby refined: on-call is not "within" SRE Management as a record base; it is an adjacent Type whose mobilization machinery SRE management may trigger.

**vs IT Service Management — keep both.** ITSM's service levels are SLAs measured on the service desk's ticket handling (response/resolution times) inside a demand-processing loop; SRE Management's objectives are internal engineering targets measured on production behavior (telemetry, incidents, tests) inside a reliability-improvement loop. Different users (IT service organization vs engineering product teams), different measurement substrate, different loop. Suites may carry both without the Types merging. Squadcast's own docs preserve the distinction (SLO "slightly stricter than" the SLA; SLA = agreement with consequences).

**vs Internal Developer Portal / service catalog — keep both (moderate confidence).** The portal's catalog is the inventory/ownership/discovery spine with self-service actions; its scorecards track attribute compliance per service (has owner, has runbook, meets practices). SRE Management holds measured reliability state (budgets/scores) and the budget machinery. Overlap exists where portals render SLO/scorecard data for services, but the portal's center is discovery + self-service, not reliability measurement. Evidence from the portal pass's recorded Tier-1 sources; Cortex not fetched directly this pass.

**vs fault-injection / resilience testing tooling.** At the Gremlin pole, fault injection is the verification engine feeding the program layer (services, standards, scores, risks). A pure fault-injection tool with no program layer (no services held as managed subjects, no tracked reliability state, no management loop) is testing territory, not SRE Management. The directory has no chaos-engineering leaf; nearest §12 neighbors are the test-management/performance-testing leaves.

**vs SLA management (conceptual ancestor/adjacent).** SLAs are contractual instruments with penalties, measured for account/commercial purposes; SLOs are internal targets with error budgets, measured for engineering prioritization. The SRE book's own SLA-vs-SLO distinction (cited by sampled vendors) marks the seam. SLA management is held as the conceptual ancestor; the internal-target framing is what makes the modern Type.

## Historical / Market-Sample Check

- The named practice is young (Google-originated SRE; the SRE book's SLO chapter is the sampled vendors' common citation), but the structure is older: an operations team tracking an availability target for a service, measuring actual uptime over a period, and acting when the downtime allowance is exceeded — on spreadsheets and whiteboards — satisfies all three legs at analog level. The definition names no cloud, no SaaS, no agents, no burn-rate formula, no OpenSLO.
- The error-budget/burn-rate machinery is the current dominant implementation (4/5 sampled), deliberately held OUT of the defining core: the Gremlin score pole and the pre-SRE spreadsheet practice both satisfy the core without it.
- Regional/platform-native check: the object model is practice-defined, not region- or platform-defined; non-US SRE teams use the same structures. No region-specific machinery was found in the sampled docs.
- SLA-management lineage (enterprise IT, pre-SRE) fits the core's shape but not its framing (contractual vs internal); held as ancestor, not absorbed.

## Uncertainties

- Cortex / OpsLevel scorecard depth not directly verified (one 404, not retried). The IDP seam rests on the portal pass's recorded evidence — moderate confidence.
- Whether FireHydrant (Blameless successor) retains any SLO machinery deeper in the product was not verified; the absorption is used as market-structure evidence only.
- Nobl9's oversight/review mechanics are known from the docs navigation and overview copy, not from deep page fetches — held at feature-list strength.
- Squadcast's incident→SLO association is currently manual or workflow-driven ("Can I automatically associate incidents with an SLO? We're working on something") — product-specific current state, likely to change.
- No sampled product holds toil as a managed object; this is a negative finding at sample strength (5 products). A toil-tracking product outside the sample would not break the L0 — it would simply be a program surface this sample did not observe.
- Gremlin's fit is at the program-layer level (services + standards + score + loop); its fault-injection engine is the verification substrate. If the taxonomy later grows a chaos-engineering leaf, the Gremlin pole's placement should be revisited.

## Final Synthesis

SRE Management is the **reliability program's system of record**: it holds the organization's reliability objectives for its services as persistent records (the SLO being the dominant form), continuously measures actual reliability against them from whatever substrate the product has (telemetry, monitors, incidents, or active tests), holds the resulting state — error budgets, burn rates, compliance, scores — as the managed quantity, and turns that state into managed action: burn alerts at graduated urgency, delivery into notification and incident channels, remediation and testing responses, and periodic re-evaluation of the objectives themselves.

The Type is NOT the union of incident + on-call + SLO + toil tooling. The market's "SRE platform" umbrella label dissolves into incident platforms with SLO modules; the durable, distinct structure is the reliability-objective layer that no neighboring Type owns as its unit of record. The error budget is the signature common-mature machinery but not the invariant (the score pole proves it); the SLI substrate is a variant axis with four distinct realizations in the sample; toil is practice vocabulary, not product structure.
