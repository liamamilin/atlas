# Research Notes — Process Mining Platform

Research date: **2026-09-06**

---

## Research Goal

Understand what a Process Mining Platform actually is as an Application Type: its core data structures (event log, case, activity, variant), its canonical workflow (from raw system data to discovered process models to analysis to action), its interfaces and roles, its important rules and constraints, and its boundaries against BPM platforms, task mining, RPA, and BI.

## Initial Boundary

Initial hypothesis (pre-research):

- Core use: reconstruct and analyze how business processes *actually* run, by mining the digital traces (event logs) left in operational IT systems (ERP, CRM, ITSM, workflow systems), rather than relying on how people describe or model them.
- Users: process analysts / operational excellence teams, process owners, auditors, consultants, and business users consuming dashboards.
- Nearest neighbors likely confused with:
  - **Business Process Management Platform** — designs and executes process models; mining *derives* models from observed executions.
  - **Task Mining Platform** — mines user-level desktop/UI interaction; process mining works at business-transaction (case) level from system logs.
  - **BI Platform** — aggregates transactional data into reports; mining is case-sequence-centric and derives process structure.
  - **RPA Platform** — executes automation; mining identifies automation candidates.
- Unknowns at start: exact shape of the data pipeline (connectors/ETL), how conformance checking is productized, how insights turn into actions, deployment forms, whether "process intelligence" rebranding changes the Type.

## Research Questions

1. What is the event log, and which fields are required (case ID, activity, timestamp, resource, attributes)?
2. How does data get in — connectors, ETL, data transformation, business logic enrichment, refresh cadence?
3. How is process discovery presented (process graphs, BPMN discovery, variant explorers)?
4. How does conformance checking work in products (as-is vs designed model, deviations, compliance)?
5. How is performance quantified (throughput time, cycle time, waiting time, KPIs, thresholds, bottlenecks)?
6. How do insights become actions (alerts, automation triggers, value/opportunity tracking)?
7. What interfaces exist, and how do analyst vs business-user roles split?
8. What deployment forms exist (cloud, on-prem/self-hosted, open-source)?
9. Where do advanced capabilities sit: task mining, simulation/what-if, predictive monitoring, GenAI copilots, object-centric mining?

## Representative Products

Selected for market representativity, philosophical diversity, and customer-tier diversity:

| Product | Position / philosophy | Customer tier | Docs status |
|---|---|---|---|
| **UiPath Process Mining** | Module of an RPA/automation platform; insight-to-automation loop is first-class | Enterprise automation estates | **Tier 1 docs fetched (3 pages)** — strongest operational evidence |
| **Celonis Platform** | Pure-play market leader; "Process Intelligence / Execution Management" platform framing | Large enterprise | docs.celonis.com **401 auth-gated**; two Tier 2 product pages fetched |
| **Apromore** | Research-origin (academic alliance), model-centric, full-spectrum (mining + modeling + simulation + monitoring); now part of Salesforce | Mid-market/enterprise; free trial tier | Tier 2 product pages fetched (home + key features); docs portal unreachable |
| **SAP Signavio (Process Mining)** | ERP-suite-embedded mining | SAP enterprise base | **Not researched** — help.sap.com renders only a JS shell; signavio.com product URL 404. Abandoned after 2 attempts per network rules. Named only as a market anchor; **no operational claims drawn from it** |

Also used as definitional grounding (not a sampled product): Wikipedia "Process mining" (Tier 3) — anchors the academic canon (event log = case id + activity + timestamp; discovery / conformance / enhancement; XES standard; IEEE Task Force; Gartner "process mining platforms" category).

## Sources

| # | Source | Tier | Status |
|---|---|---|---|
| 1 | UiPath — Introduction to Process Mining (docs.uipath.com) | 1 (official user guide) | fetched, 2026-09-06 |
| 2 | UiPath — Working with dashboards and charts (docs.uipath.com) | 1 | fetched, 2026-09-06 |
| 3 | UiPath — Setting up Automation integration (docs.uipath.com) | 1 | fetched, 2026-09-06 |
| 4 | Celonis — Platform page (celonis.com/platform) | 2 (official product page) | fetched, 2026-09-06 |
| 5 | Celonis — Analyze Processes page (celonis.com/platform/analyze-processes) | 2 | fetched, 2026-09-06 |
| 6 | Apromore — Home page (apromore.com) | 2 | fetched, 2026-09-06 |
| 7 | Apromore — Key Features page (apromore.com/key-features) | 2 | fetched, 2026-09-06 |
| 8 | Wikipedia — Process mining | 3 | fetched, 2026-09-06 |
| 9 | Celonis — docs.celonis.com (process intelligence docs) | 1 | **401 auth-gated — abandoned** |
| 10 | SAP Help Portal (help.sap.com/docs/SAP_Signavio, help.sap.com/docs/signavio-process-mining) | 1 | **JS shell, no content — abandoned after 2 attempts** |
| 11 | signavio.com/products/process-mining | 2 | **404 — abandoned** |
| 12 | docs.apromore.org / apromore.org/end-user-manual | 1 | **transport error / 404 — abandoned** |

**Source-access limitation:** SAP Signavio and Celonis technical documentation were not reachable. Claims that rest only on Tier 2 marketing pages are labeled accordingly. No operational detail for these vendors has been filled in from model memory.

---

## Product Observations

### UiPath Process Mining (evidence layer A — Tier 1 official docs)

**Positioning:** "transforms data from your IT systems into visual interactive dashboards" revealing "bottlenecks, discrepancies, and root causes".

**Process mining cycle (as documented):**
1. **Data transformation** — extract data; transform and clean it to fit the app's expected input; add business logic and enrich to enhance analysis.
2. **Data analysis** — build *process apps*; configure for business roll-out; incorporate business procedures and rules as reference for business transactions across teams.
3. **Continuous monitoring** — deploy the app to business users; monitor the process over time; discover risks and optimization opportunities.

**Process apps / dashboards:**
- A process app consists of multiple dashboards; charts visualize data (process graph, bar chart, cross-analysis table).
- KPI bar at top shows key metrics with period-over-period comparison (black = selected period; up/down arrows vs previous period).
- **Thresholds**: predefined limits defining good / warning / critical performance, visualized on KPI charts (example given in docs: green < 3 days, yellow 4–5 days, red > 5 days for average throughput time end-to-end — illustrative example from docs, product-specific).
- Metrics: **Event throughput time** (event end → previous event end, includes waiting) and **Event cycle time** (event start → event end; requires event_start defined for all events). Transition waiting time = event_end → next event_start.
- Fields & metrics: dashboards categorize records by selected field (e.g. **Variant**) and metric (e.g. **Number of items**).
- **Data selections**: clicking/dragging in charts creates filters; selections carry across dashboards; advanced filter panel; trend selection creates custom period filters.
- **Details**: drill down to a Details dashboard to analyze objects at the lowest level (case level).
- Share dashboard URL (current view incl. filters/full-screen state).
- **Data restrictions**: restricted fields (e.g. personal data) hidden per data restrictions / record access policies.

**Automation integration (the action loop):**
- **Manual triggers**: business users select objects on published dashboards → "Trigger an automation" → one queue item per case in an Orchestrator queue → robot executes an automation workflow built in Studio. Input fields are mapped to app data fields; free-text **business user input** and read-only **analyst input** options exist.
- **Automatic triggers**: tags define trigger conditions; evaluated on every data load of the published app; each case meeting a condition → queue item. Each trigger condition evaluated separately (a case matching two tag conditions is queued twice).
- Maximum number of objects sent at once: default 50, adjustable 1–1000 (product-specific precise fact; research notes only).
- Example use case in docs: reminder email for a late payment case detected in Process Mining.

**Deployment forms (from docs nav):** Automation Cloud (SaaS), Automation Suite (self-hosted, multiple versions), standalone (legacy 2021.10). App templates exist (e.g. Purchase-to-Pay referenced in docs).

### Celonis Platform (evidence layer A for module existence, Tier 2 marketing pages)

- Platform framing: "process data, business knowledge, and intelligence from all of your systems... dynamic, real-time digital twin of your operations"; three layers: **Data Core** (extract from any source, query "billions of records"), **Context Model** (system-agnostic representation; root causes, predictions, recommendations, what-if), **Build Experience** (Analyze / Design / Operate).
- **Process Explorer**: "deep process analysis", visualize "how objects and events in your systems interact"; "no technical expertise required".
- **Process Adherence Manager**: "achieve optimal conformance by monitoring your mined processes against your modeled processes"; visualize deviations; identify root causes; baseline for new process models. → productized conformance checking.
- **Transformation Hub**: tag, track, share opportunities and results; value tracking for the mining investment.
- **Studio Views**: build custom analytical and operational apps, from reports/dashboards to full-scale apps.
- **Insight Explorer**: AI detection of patterns (process characteristics influencing KPIs, unusual KPI fluctuations).
- **Marketplace**: hundreds of pre-built dashboards/apps per process/industry.
- Integrations named on page: ERPs (SAP, Oracle, Infor), data platforms (Snowflake, BigQuery, Databricks), automation platforms, BI tools (Power BI, Tableau, Qlik), etc.
- Marketing claims ("real-time", "AI-driven") not treated as operational evidence.

### Apromore (evidence layer A for feature existence, Tier 2 product pages)

**Positioning:** "full spectrum process intelligence": process mining, task mining, process modeling, simulation, monitoring in one platform; research/academic lineage ("built on some of the most advanced process mining algorithms"); now part of Salesforce.

**Get-started flow (as documented):** Connect (collect transactional data from the digital footprint left by processes in IT systems) → Visualize (visual model of how processes work: what is done, in what order, by whom) → Analyze (bottlenecks, SLA violations, KPI-based weak spots) → Optimize (simulate interventions, pick by impact) → Monitor (monitor performance; predict deviations).

**Key features (as documented):**
- **Shared workspace of process models and logs** — collaborative repository for models and event logs.
- **Discovery of process maps and BPMN models** — "automatically discover a process map of your 'as-is' BPMN model from an event log"; switch between map and BPMN views; change perspective (resources, roles, business object states); simplified views.
- **Performance overlays** — frequencies and durations of activities and handovers overlaid on map/BPMN.
- **Visual filtering** — filter logs by case variant, timeframe, performance measures, execution paths, degree of rework, attribute-value pairs.
- **KPIs and Root Cause Analysis** — factors driving inefficiencies, KPI breaches, compliance violations; quantify impact (violation rate, risk ratio); compare compliant vs non-compliant cases via comparative process maps.
- **Performance dashboards** — statistics at different abstraction levels; case-by-case or by variant ("who did what, when, how often"); custom dashboards, KPI thresholds, reference lines.
- **Flow comparison and multi-log animation** — compare variants visually; animate temporal dynamics.
- **Compliance Center** — import risks/controls/obligations from corporate GRC; link controls to event logs for **automated control testing** (flow constraints, temporal/SLA constraints, resource constraints); link to BPMN for documentation; compliance analytics; simulate impact of change on control effectiveness.
- **Conformance checking** — compare expected/to-be BPMN model against as-is event log; spot flow deviations; assess impact.
- **Complete authoring environment** — create/edit BPMN models; share; find similar models; merge models; use as input for animation, conformance, simulation.
- **Model delta analysis** — differences between best-practice and actual models.
- **Roundtrip simulation** — auto-discover BPMN model with simulation parameters from the log; "digital twins of end-to-end processes"; what-if scenarios with comparative analytics.
- **Connectivity and ETL pipelines** — connect to client systems; schedule ETL pipelines at desired cadence (e.g. weekly, monthly); export analytics to third-party BI tools.
- **Predictive business process monitoring** — train ML models: case outcome, SLA violations, remaining time, next activity, case continuation; predictions refresh as cases unfold.
- **Copilot** — GenAI conversational assistant for discovery/analysis.
- **Task mining** — desktop-level user routines inside tasks; RPA-automation discovery.

### SAP Signavio — not observed

Official docs unreachable (see Sources). No operational observations. Retained in Representative Products as a market anchor only. Widely known to be the ERP-suite-embedded process mining offering, but per evidence rules this is *not* asserted with product detail anywhere in the final document.

### Definitional grounding (Wikipedia, Tier 3)

- Process mining = "family of techniques for analyzing event data to understand and improve operational processes"; logs contain **case id**, **activity**, **timestamp**, sometimes resources/costs.
- Three canonical technique classes: **process discovery**, **conformance checking**, **process enhancement** (incl. performance analysis).
- Event logs can come from workflow audit trails, ERP transaction logs, hospital EHR records — i.e., substrate is any process-aware information system, not one vendor's stack.
- IEEE XES standard (2016) for event log interchange; IEEE Task Force (2009); Process Mining Manifesto; term coined by Wil van der Aalst (~1999); ProM framework; alpha/heuristic/inductive miners; alignment-based conformance (2010).
- 2018: ~30 commercial tools; 2025: Gartner lists 40 tools in "process mining platforms" category. Category name in analyst taxonomy = "Process Mining Platforms" (matches the directory leaf).
- Historical check material: early academic tools (ProM, 2005) and first commercial offerings (Futura Pi 2007, ARIS PPM ~2002) already fit case+event+discovery+performance structure — supports a non-overfit L0 (see Historical Sample Check below).

---

## Cross-product Comparison

| Capability / structure | UiPath (A, T1) | Celonis (A, T2) | Apromore (A, T2) | Evidence layer |
|---|---|---|---|---|
| Event-log substrate from operational IT systems ("digital footprint", transactional data) | ✔ ("data from your IT systems"; event_start/event_end fields) | ✔ ("process data... from all of your systems"; Data Core) | ✔ ("transactional data from the digital footprint"; event logs named throughout) | **B** |
| Case / variant / activity semantics | ✔ (Variant field, case fields, Number of items) | implied (objects and events) | ✔ explicit (case variant, case-by-case, who did what when) | **B** (case/activity/timestamp canon also in [8]) |
| Automated discovery of the actual process model from the log | ✔ ("extract it to deliver real-time multidimensional process models") | ✔ ("mined processes"; Process Explorer over objects and events) | ✔ explicit ("automatically discover a process map of your 'as-is' BPMN model from an event log") | **B** |
| Process model visualization (process graph/map) | ✔ (process graph chart) | ✔ (Process Explorer) | ✔ (process map, BPMN views) | **B** |
| Performance measures on the process (frequencies, durations, throughput) | ✔ (throughput/cycle time, KPI bar, metrics) | implied (KPI fluctuations in Insight Explorer; "value opportunities") | ✔ explicit (performance overlays; durations of activities and handovers) | **B** |
| Dashboards with KPIs + thresholds for business users | ✔ (process apps, KPI bar, thresholds) | ✔ (Studio Views apps; Marketplace dashboards) | ✔ (performance dashboards, thresholds, reference lines) | **B** |
| Filtering / drill-down to case level | ✔ (data selections, Details dashboard) | implied | ✔ (visual filtering, case-by-case inspection) | **B** (drill-to-case explicit in 2 of 3) |
| Variant analysis (compare ways the process runs) | ✔ (Variant as primary field) | implied | ✔ (variant filtering, flow comparison, animation) | **B** |
| Conformance checking vs designed model | not directly evidenced | ✔ (Process Adherence Manager: mined vs modeled, deviations) | ✔ (conformance checking; model delta analysis; Compliance Center) | **B** (2 of 3 sampled + canon [8]; UiPath not evidenced) |
| Root cause analysis | ✔ (intro: "understanding the root-causes") | ✔ (Adherence Manager; Insight Explorer) | ✔ (KPIs and RCA) | **B** |
| Data pipeline machinery (extract → transform → enrich; scheduled refresh) | ✔ (extract/transform/clean/enrich; data runs) | ✔ (Data Core "extract from any source") | ✔ (ETL pipelines, scheduled cadence e.g. weekly/monthly) | **B** |
| Analyst ↔ business user split (build apps vs consume/act) | ✔ (configure app → deploy to business users) | ✔ ("no technical expertise required"; Studio Views for builders) | ✔ ("no-code platform... business users") | **B** |
| Action loop (alerts / automation triggering from insights) | ✔ explicit (manual + automatic automation triggers, queue items) | ✔ (Operate: orchestrate/monitor; Transformation Hub opportunities) | partial (RPA-opportunity discovery via task mining; simulation) | **B** with depth variance; UiPath most productized |
| BPMN model authoring / model management in-product | not evidenced | not evidenced (Marketplace blueprints only) | ✔ (full authoring environment, repository, merge) | product-apportioned; **common but uneven** |
| Simulation / what-if / digital twin | not evidenced | ✔ (what-if in Context Model marketing) | ✔ (roundtrip simulation, what-if) | Optional |
| Predictive monitoring (ML on running cases) | not evidenced | not evidenced (marketing-level "predictions") | ✔ (remaining time, next activity, outcome, SLA breach) | Optional |
| Task mining (desktop interaction logs) | (exists as separate UiPath product; not in fetched pages) | not evidenced on fetched pages | ✔ (companion capability) | Optional / sibling Type |
| GRC/compliance control testing against logs | not evidenced | not evidenced | ✔ (Compliance Center) | Optional |
| Value/opportunity tracking for improvement program | implied | ✔ (Transformation Hub) | not evidenced | Optional |
| Prebuilt app templates per process area (P2P/O2C) | ✔ (app templates; Purchase-to-Pay named) | ✔ (Marketplace) | not evidenced | **B** (common in 2 of 3) |
| Deployment: cloud SaaS / self-hosted / standalone | ✔ (Automation Cloud / Automation Suite / standalone) | SaaS (implied by signup) | free-trial cloud; OSS lineage | L2 variant, product-apportioned |
| GenAI copilot for analysis | not evidenced on fetched pages | ✔ (Insight Explorer is AI, not necessarily conversational) | ✔ (Copilot) | Optional, emerging |

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being a Process Mining Platform:

```text
Event-log substrate
  (transactional event records from operational systems,
   each carrying case identity + activity + timestamp)
└── Automated process discovery
    (the actual process structure is derived from the events,
     not drawn by hand)
    └── Execution-grounded process analytics
        (cases, variants, frequency/duration measures
         anchored to the discovered actual process)
```

Three invariants:

1. **Event-log substrate** — ingested event/transaction data whose rows can be grouped into cases and ordered by timestamps. Remove it and there is nothing to mine.
2. **Automated process discovery** — the platform reconstructs the as-is process (activity graph / process map / model) from those events. Remove it and the product is a modeling tool (BPM) or a reporting tool (BI).
3. **Execution-grounded analytics over cases/variants** — frequency and time measures computed per case, per variant, per activity from the same data. Remove it and the product is a static flow-diagram generator.

Deliberately NOT in L0: connectors/ETL machinery, conformance checking, dashboards for business users, root cause analysis, action/automation loop, BPMN support, simulation, prediction, real-time/streaming behavior, SaaS delivery, any process area (P2P/O2C) templates.

### L1 — Common Mature Structure

Present across the sampled products; expected in mature products; not definitional:

- data pipeline: connectors/extractors, ETL with cleaning and business-logic enrichment, scheduled data refresh
- process model visualization (process graph / map; some products also BPMN)
- variant analysis (variant views, flow comparison)
- performance KPIs with thresholds on dashboards (throughput time, cycle time, waiting time)
- drill-down from aggregate to case level; interactive filtering/selections
- conformance / adherence checking against a designed or target model with deviation visualization
- root cause analysis of performance and compliance problems
- analyst/business-user role split: analysts build and configure; business users consume dashboards and act
- process apps / dashboards published and shared as governed artifacts
- action loop: alerts, task/automation triggering, opportunity/value tracking
- prebuilt templates for common process areas (e.g. purchase-to-pay, order-to-cash)

### L2 — Variant / Optional Structure

Depends on segment, deployment, strategy:

- deployment form: cloud SaaS vs self-hosted suite vs standalone/legacy vs open-source lineage
- conformance orientation: monitoring-centric (adherence dashboards) vs model-delta/GRC-centric (controls testing, obligations)
- simulation / what-if / digital twin of the process
- predictive process monitoring (remaining time, next activity, outcome, SLA risk)
- task mining as companion capability (desktop-level mining)
- compliance center linking GRC risks/controls to logs
- value/opportunity management layer (tag/track savings)
- GenAI copilots for conversational analysis
- BI export / coexistence with third-party BI tools
- sensitive-data restrictions within mined data
- object-centric analysis (models over interacting business objects rather than a single flat case) — emerging; evidence thin in this sample
- process-area focus (P2P, O2C, ITSM...) via templates vs horizontal tooling

### L3 — Vendor-specific (research notes only)

- **UiPath**: Automation manager; Orchestrator queues with Specific Data JSON Schema; Studio-built workflows as automations; tags → automatic triggers evaluated per data load; per-condition evaluation (one case may enqueue twice); default max 50 objects (range 1–1000) per manual trigger; analyst input (read-only) vs business user input (free text); app templates (Purchase-to-Pay); event_start/event_end field naming and cycle-time availability rule (requires event_start non-null for all records).
- **Celonis**: Context Model (CCM) framing; Process Adherence Manager; Transformation Hub; Insight Explorer; Studio Views; Marketplace; "digital twin of your operations" positioning; 1,400+ companies claim (marketing).
- **Apromore**: Process Discoverer; roundtrip simulation; Compliance Center (GRC import; automated control testing against logs); Copilot; portal repository of models+logs; perspectives (resources/roles/business object states); Salesforce acquisition (2026 news).

## Vendor-specific Findings

- UiPath's automation loop is the most concretely productized insight→action mechanism in the sample (documented end-to-end at Tier 1). Treating "native automation triggering" as definitional would overfit to one vendor; Apromore's loop is analysis→simulation→optimization, and Celonis frames it as Operate/orchestration. The *common* structure is an action/monitoring loop; *automation triggering* is one implementation of it.
- Apromore uniquely (in sample) treats BPMN model authoring/repo/delta as a first-class half of the platform — heritage from the modeling/process-science side.
- Celonis's Transformation Hub (value tracking) and UiPath's thresholds/triggers have no direct counterpart in the other fetched pages — keep Optional.

## Boundary Findings

- **vs Business Process Management Platform**: BPM designs, validates, executes, and automates process definitions — the model *drives* work. Process mining derives models *from* executed work (event logs). Fetched evidence: Apromore uses its authoring environment as *input* to conformance/simulation (model as reference), not as the execution engine. Remove event-log discovery → you have a BPM suite. Note convergence: BPM suites embed mining and mining tools add modeling; packaging overlap is real but the defining cores differ.
- **vs Task Mining Platform**: task mining captures user-level desktop/UI interaction to reconstruct *tasks* inside process steps; process mining works at business-transaction level from system event logs. Apromore explicitly positions task mining as a *complement* ("dig deeper into the manual steps performed in desktop applications"). Task mining logs lack the case-transaction semantics by default (must be mapped to a process context).
- **vs BI Platform**: BI aggregates arbitrary data for reporting; process mining's unit of analysis is the *case sequence* (ordered events of one instance) and its distinctive output is derived process structure (graph/model with precedence, loops, rework, handovers), not aggregated charts alone. Remove case-ordered event derivation → BI on transactional tables.
- **vs RPA Platform**: RPA executes automation; mining discovers and prioritizes automation candidates (and, in some products, triggers automations). The trigger capability makes them adjacent, not identical: the mining core is observational, not actuatorial.
- **vs Application Performance Monitoring / Observability**: APM watches software health (latency, errors of services); process mining watches business-process behavior (flow, rework, throughput of cases). Different substrate and different questions.
- **"Remove what → becomes another Type" test**: remove *mining from event logs* → BPM (model-driven) or BI (data-driven reporting); remove *business-transaction semantics* → IT logging/observability or task mining; remove *process structure derivation* → generic analytics.

## Historical / Market-Sample Check

- Would older/regional/platform-native products still fit L0?
  - Academic-era tools (ProM and predecessors, ~2004–2005) fit: event logs (XES lineage), discovery, performance/conformance plugins. No dashboards for business users, no action loop, no cloud — L0 holds.
  - First commercial wave (ARIS PPM ~2002, Futura Pi 2007) fit: log ingestion + discovered/annotated process performance. L0 holds.
  - Regional/European enterprise tools (QPR, myInvenio/IBM, Mehrwerk/Qlik lineage) are consistent with the same core structure (not fetched, but the category canon [8] covers them at definitional level).
- Therefore L0 must not include: SaaS delivery, real-time/streaming, AI copilots, "execution management" framing, object-centric models, connector marketplaces — all of these are current-market features, not Type invariants.
- Naming check: analysts call the category "Process Mining Platforms" (Gartner, 2025, 40 tools listed); vendors increasingly rebrand toward "Process Intelligence / Execution Management". The directory leaf name matches the established category name; rebranding is a marketing trend, not a Type change. No taxonomy conflict.

## Uncertainties

1. **SAP Signavio internals unverified** (source unreachable). Its inclusion as a representative product rests on market notoriety and the analyst category, not on fetched evidence. No operational claim in the final document depends on it.
2. **Celonis operational detail** (how Process Explorer/Adherence behave step-by-step) rests on Tier 2 pages because docs are auth-gated. Claims kept at module-existence level.
3. **Conformance checking as L1, not L0**: UiPath's fetched pages do not document a conformance feature; two of three sampled products + the academic canon support it as common. If UiPath in fact lacks it entirely, "common" still holds, but the confidence is moderate.
4. **Object-centric process mining** (multi-object case models) is visible in the literature (OCPetri nets; Celonis "objects and events" language) but not enough to characterize how products implement it. Left as an emerging variant.
5. **Streaming/real-time mining**: Celonis markets "real-time"; UiPath runs analyses on data loads; Apromore demonstrates scheduled ETL. Actual refresh models vary and are not fully evidenced — final document phrases refresh behavior moderately.
6. **Pricing/segment spread** (mid-market vs enterprise) not researched; product selection compensated with philosophical diversity instead.

## Final Synthesis

A Process Mining Platform is an analysis platform whose substrate is the **event log** — transactional event records from operational systems, grouped into **cases** (process instances) and ordered by **timestamps** — from which it **automatically derives the actual process** (activity graphs/maps, process models) rather than relying on hand-drawn designs. Around this core, mature products add: a governed **data pipeline** (connect → transform/enrich → scheduled refresh), **variant analysis**, **performance analytics** (throughput/cycle/waiting time, KPIs with thresholds), **conformance checking** of actual behavior against designed/target models, **root cause analysis** with drill-down to individual cases, an **analyst/business-user split** with published **process apps/dashboards**, and an **action/monitoring loop** (alerts, automation triggering, value tracking). Optional extensions include simulation/what-if digital twins, predictive monitoring, task mining, GRC-linked compliance testing, and GenAI copilots. The Type is defined by observation of executed work through event data; remove that and the product becomes a BPM suite (model-driven), a BI tool (aggregate-driven), or a task/automation tool (interaction-driven).
