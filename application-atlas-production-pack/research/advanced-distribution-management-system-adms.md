# Research Notes — Advanced Distribution Management System / ADMS

Research date: 2026-09-06
Slug: `advanced-distribution-management-system-adms`
Directory location: Section 19 — Energy, Utilities & Telecommunications

---

## Research Goal

Understand what an Advanced Distribution Management System (ADMS) actually is as a software Type: what objects exist inside it, who operates it, how daily and storm-mode work flows through it, which capabilities are defining vs. common vs. optional, and where its boundaries lie against SCADA, DMS, OMS, EMS, DERMS, and adjacent utility Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: ADMS is the distribution-side control-room platform combining SCADA (telemetry + control), DMS network applications (power flow, FLISR, Volt/VAR), and OMS (outage/trouble management) on a shared distribution network model.
- Likely confusions: Distribution Management System / DMS (sibling leaf — possibly the same thing under an older name), Outage Management System / OMS (sibling leaf — possibly a module), SCADA (sibling in §16), Energy Management System / EMS (transmission twin), DERMS (sibling leaf), Grid Operations Platform (sibling leaf), Utility GIS (model source).
- Key open question: is "ADMS" a distinct structure or just the modern market name for DMS? And is OMS part of the definition or a bundled module?

## Research Questions

1. What is the organizing structure of an ADMS? Is there a network model, and what does it contain?
2. What does the operator actually do minute-to-minute? What surfaces do they use?
3. How do outages flow: from telemetry/calls → event → dispatch → restoration → records?
4. How does planned work flow: switching requests → switching sheets → safety documents → execution?
5. Which "advanced applications" exist (FLISR, VVO, state estimation, fault location) and are they defining or optional?
6. How do real-time and study modes relate? What safety/authority rules gate control actions?
7. What roles/user types exist?
8. Where is the SCADA / DMS / OMS / ADMS boundary in the current market?
9. Would older or regional products (plain distribution SCADA, DMS without OMS, OMS without network model) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, product philosophy, and customer tier:

| Product | Vendor | Tier / philosophy | Evidence quality |
|---|---|---|---|
| Oracle Utilities Network Management System (NMS) | Oracle | Enterprise suite; SCADA+OMS+DMS+switching on one platform; deep public user/implementation guides | Tier 1 (operational docs, directly fetched) |
| GridOS ADMS | GE Vernova | "Grid orchestration" positioning; DMS+OMS+DERMS "three solutions in one"; platform + apps | Tier 2 (product pages + FAQ) |
| AspenTech OSI ADMS (formerly Open Systems International) | AspenTech | Control-room specialist; monarch SCADA platform + ADMS suite; operator training simulator emphasis | Tier 2 (product page) |
| SurvalentONE ADMS | Survalent | Mid-market (co-ops/municipals); modular: SCADA, OMS, DMS apps sold as separate products composing an ADMS | Tier 2 (product catalog) |

Attempted but unreachable (recorded per source-access limitation rules):
- Schneider Electric EcoStruxure ADMS — HTTP 403 (bot-blocked), dropped after 1 attempt.
- Hitachi Energy Network Manager — 404 on two URL guesses, dropped.
- Siemens Spectrum Power — 404 on two URL guesses, dropped.

## Sources

Tier 1 (official operational documentation, fetched 2026-09-06):
- Oracle Utilities Network Management System documentation library (Release 25.12): https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html
- NMS User Guide — table of contents + pages: Understanding User Types; Web Switching Management Overview; Suggested Switching Introduction; Understanding Event Details
- NMS Advanced Distribution Management System Implementation Guide — landing, Glossary, ADMS Applications Overview, FLISR chapter

Tier 2 (official product pages, fetched 2026-09-06):
- GE Vernova GridOS ADMS: https://www.gevernova.com/software/products/gridos/advanced-distribution-management-system
- GE Vernova GridOS Orchestration Software: https://www.gevernova.com/software/products/gridos/
- AspenTech OSI ADMS: https://www.aspentech.com/en/products/dgm/aspentech-osi-advanced-distribution-management-system
- AspenTech OSI acquisition page (osii.com redirect): https://www.osii.com/
- Survalent products catalog: https://www.survalent.com/products/

---

## Product A — Oracle Utilities Network Management System (Tier 1, evidence layer A)

The deepest directly-observed sample. Oracle ships an "Advanced Distribution Management System Implementation Guide" for NMS, i.e., the vendor itself frames NMS as an ADMS platform.

### Platform structure (observed)

- Modules per the ADMS Implementation Guide: **OMS Modules** (data model, SCADA adapters, trouble management & events, web switching) and **ADMS Modeling** (network model data: sources, loads, load profiles, transformers/voltage regulators, capacitors/reactors, DERs + DER profiles, switches and fuses, conductors; split model; phasing; nominal voltages; DER and weather zone forecasts; seasonal/temperature limits).
- User guide chapters: Web Workspace (Viewer, Control Tool, alarms, Work Agenda), Web Trouble Management (events, crews, call entry, callbacks, storm management, service alerts), Flex SCADA (SCADA status, FEP/IED monitors, calculations, historian, commissioning), SCADA Extensions (measurements, quality codes, limits, trend graphs, device locking, switching-management SCADA integration), Web Switching Management (switching sheets, safety documents), Power Flow, Distribution State Estimation, Suggested Switching, Network Optimization Tool (VVO), Management Reporting.

### Network model (observed)

- Glossary terms: **Electrical Island** ("a subset of the network model of devices & feeders that are electrically connected… energized or de-energized"); **Equivalent Source** (start of energization for an island, encapsulating upstream network as a Thévenin source); **Load** (where customer load is accounted: distribution transformer, LV feeder head, customer meter, or virtual aggregate); **Powerflow** ("rigorous unbalanced 3-phase solution of the voltages and current flows in an island"); kVA Solution / Connected kVA ("Ladder Solution") as lighter solution types; Distribution Xfmr vs Power Xfmr.
- Model data comes from external sources (GIS etc. — "Sources of Data" chapter), with phasing, nominal voltages, seasonal/temperature-based equipment limits.

### SCADA layer (observed)

- Flex SCADA: SCADA Status Window, FEP (front-end processor) Monitor, IED (intelligent electronic device) Monitor, Point Monitor, IED inputs/outputs, interpretation tables, analog scaling, jitter protection, calculation engine, historian (incl. PI historian tab), audit log, SCADA commissioning tool, bulk import.
- SCADA Extensions: measurements with quality codes, manual entry/override of measurement values, limits dialogs, trend graphs, remote SCADA operation warnings, SCADA device locking, "Switching Management SCADA Integration", vendor-specific integrations (e.g., OSI SCADA integration).

### Operations surfaces (observed)

- **Viewer**: one-line feeder schematics, device details, viewer coloring, traces, feeder focus, lens windows, real-time and study mode, commissioning tool, assessment tool (marking conductors as assessed), save case management, device event history.
- **Control Tool**: operating devices, instructed actions pane, tagging devices, placing grounds, disabling automatic throwover (ATO) switches, disabling network protectors, placing jumpers, repredicting upstream/downstream, creating momentary outages, aggregate device actions, alarm/control inhibit options, Look Ahead dialog, Control Failure dialog, associating documents with devices, damage assessments per device.
- **Authority model**: control zones; operators subscribe to a control zone and "take authority" via the Authority Tool; authority groups; changing the rule set.
- **Alarms**: alarms list, frozen alarms, nuisance alarm history, alarm shelving, abnormal devices list, emailing alarms.
- **Work Agenda**: filtered event lists; acknowledging events; reading pane.

### OMS layer (observed)

- **Events** (Work Agenda / Event Details): event #, phases out, # calls, customers out, critical customer counts (Emergency/Medical/Key/Sensitive), start date, estimated restoration time (ERT), restore date, est. time to repair, associated device, associated switching sheet #, clues, control zone. Tabs: Job Actions (restoration log with stages, per-stage CMI), Completion Actions (cause codes: system, sub-system, device type, failure, interrupting device, primary cause, weather, environment, vegetation, foreign interference, defective equipment, scheduled, utility error, remedy; interruption-indices exclusion with reason + post-completion edit log), Equipment Failure, Trouble Info (Callers / Customers / Supply Points / AMI Customers views), Damage Assessments (statuses New/Assessing/Assessed/Standing By/Fixed/Obsolete; patrol events), Event Log, Steps, Fault Location Analysis tab, FLISR Report tab, Optimization Report tab, Alarms, Attachments.
- **Calls**: Web Call Entry (search customer, enter call, fuzzy calls, informational calls, cancel), call history, event history; calls grouped into events by grouping rules; fuzzy call association; call transfer between events; moving customers to a different device triggers re-prediction ("The event is then re-analyzed using the new device information… Calls may be grouped into another existing event or a new event will be created").
- **Crews**: Crew Actions window; crew makeup (personnel, vehicles); assign to event → dispatch → en route → on site → offsite → suspend → release; crew contact times; bulk crew loading (admin).
- **Storm Management**: storm mode vs non-storm mode with different ERT algorithms; ERT overrides; full-operations / view-only / administration environments; storm report.
- **Callbacks**: assign callbacks by number or percentage; perform callbacks.
- **AMI integration**: AMI requests (meter ping, load-side status, voltage reading), AMI Customers view with meter status/ping results, AMI confirm for outages; integration via Smart Grid Gateway.
- **Reliability indices**: CMI computed per restoration stage; events can be excluded from interruption indices calculations with a reason (Trouble Reporting application).

### Switching management (observed)

- "Web Switching Management allows you to create and implement switching sheets and safety documents. Switching Sheets allow you to track proposed switching actions, analyze the results, and implement the plan. Safety Documents provide an electronic representation of paper safety documents, which are used for switching operations to record the issuance and release of tags on devices."
- Operating modes: **Real-Time Mode** (changes real-time device state; automatically enabled for emergency sheets) vs **Study Mode** (changes do not affect real-time data; only valid mode for template and outage-correction sheets).
- Switching sheet types: planned, emergency, template, outage correction (rework). Sheet states include Approved, Scheduled, Issued, In Progress, In Progress (Instructed). Steps can be reviewed in study mode, replayed, versioned; "Viewing Impacted Customers"; "Checking for Overlaps"; power flow analysis inside switching management; crew assignments (system crews, contractors); emailing/exporting sheets; miscellaneous log.
- Safety documents: types mapped to step types; issuance and release of tags; delegating control of a network area; stand-alone safety documents; completing/aborting documents.
- Switching requests: a dedicated "Switching Request" user type creates switching requests (field/planning side), which operations then work.
- Nominal vs current feeder/substation: as switching proceeds, devices may become associated with feeders other than the as-built nominal ones; both are tracked.

### DMS applications (observed, ADMS Applications Overview)

- **Power Flow**: "the core of the ADMS functionality, most other ADMS applications depend on the Power Flow module." Calculates voltages at every bus, derives current flows and real/reactive load flows; incorporates SCADA data to scale loads; uses historical load profiles. Real-time and study mode; Look Ahead; seasonal/temperature limits; disconnected DER handling; results in Viewer balloons and device details.
- **Feeder Load Management (FLM)**: system-wide overview of current loading conditions and optional future scenarios; island statistics.
- **FLISR**: "triggered by a breaker lockout… seeks to identify the faulted section. Through the use of SCADA controllable switches it will formulate a plan to isolate the faulted section and restore service to customers above and below the faulted section where possible." High-level algorithm (documented): (1) confirm genuine lockout from SCADA; (2) use fault-indication signals to identify faulted section; (3) run power flow with pre-trip loads; (4) identify all restoration scenarios; (5) run power flow on potential pickup feeders for current and near-future capacity; (6) evaluate every scenario with further power flow runs, considering DER on the faulted section and future loads; (7) select best option considering violations, safety blocks ("tags, grounds, crews"), same-transformer feeders, DER presence, post-restoration capacity.
- **Fault Location Analysis (FLA)**: predicts fault locations from fault currents reported by the relay of the tripped device, using short-circuit analysis.
- **Optimization (formerly VVO)**: "continuously monitors the distribution system looking for opportunities to optimize performance to meet pre-configured objectives." Study and real-time modes; optimization plans can be demoted to manual; aborted; setpoint limits; tracks number of operations on capacitors and penalizes them; optimization report; optimization events appear in the Work Agenda.
- **Suggested Switching**: study mode only; two scenario types — de-energize/isolate an energized device minimizing dropped load; restore power to a de-energized device by solving power flow for each eligible tie point with adjacent feeders to determine remaining capacity and overloads. Generates switching steps and can create/append to switching sheets.
- **Distribution State Estimation**: sources tab, results tab, weights, bad-data detection, network-wide estimates for unmeasured devices, tuning/convergence settings.

### User types (observed)

Administration; Crew Operations; Full Operations; Full Operations plus Switching; Full Operations plus Switching and SCADA Control; Switching Request; Trouble Maintenance; View Only; SCADA Maintenance; SCADA Commissioning; SCADA Maintenance plus Commissioning; Trainer. Flex client variants (Flex Call Taker/Administrator etc.). Edge DERMS user types: DERMS User / Supervisor / Administrator (events, strategies, configuration). Two-factor authentication at login.

### DERMS (observed)

- Separate "Edge DERMS" module with its own install/deploy guide and user types (events, strategies). DERs are also first-class in the network model (DER profiles, DER forecasts, DER in FLISR evaluation, customer DER units in Trouble Info).

---

## Product B — GE Vernova GridOS ADMS (Tier 2, evidence layer A→B)

- Positioning: "GridOS ADMS is the most advanced and scalable distribution management system available… transforms real-time data into actionable insights that drive grid reliability, resilience, and efficiency."
- **"Three solutions in one"**: Distribution Management System ("visualization, planning, monitoring, control, optimization, and overall management of the distribution grid"), Outage Management System ("management of planned and unplanned outage events. Includes field mobility, damage assessment, and predictive analytics"), DERMS ("built-in DER management capabilities… from initial integration and visualization to ongoing operation, control, and optimization").
- FAQ definition: "ADMS… is a real-time, integrated software platform used by electric utility companies to enhance the efficiency, reliability, and security of their electrical distribution networks," listing: OMS; real-time monitoring and control; load forecasting; FLISR; DER management; VVO.
- "How does ADMS work?" FAQ: real-time monitoring and control (power flows, voltages, outages, equipment status); fault detection and management with automated restoration; voltage optimization; load forecasting; DER integration; network optimization; data management and analytics.
- Reliability metrics named: CMI, SAIDI, SAIFI. "Blue sky and grey sky days" phrasing for normal vs storm operations. T&D coordination via "decentralized workflows… balance the grid, run advanced simulations."
- Platform claims (GridOS): federated grid data fabric with "common transmission and distribution network model to enable a grid digital twin"; zero-trust security; microservices; hybrid cloud deployment; AI/ML load prediction.
- Market evidence: Guidehouse Insights Leaderboard: ADMS Vendors (Q1 2023) quoted; customer stories (Alabama Power model-based FISR).

## Product C — AspenTech OSI ADMS (Tier 2, evidence layer A→B)

- Definition: "Integrated solution suite for active management of distribution grids including advanced applications, outage management and distributed energy resource management."
- Four capability pillars on the product page:
  1. **Advanced Distribution Management** — "Real-time network topology and power flow coupled with robust visualization and study mode across all functionality."
  2. **Outage Management** — "efficient job and crew management, mobile communication and reporting."
  3. **Operator Training Simulator** — "hands-on experience with events and scenarios ranging from switching, system faults, overloads, storm operations and more."
  4. **Switch Order Management** — "Conduct study, simulation and pre-operational checks fully integrated with SCADA, DMS and OMS."
- Sibling products confirm the family structure: monarch™ (SCADA platform: "real-time monitoring and control applications"), OSI EMS (transmission), OSI DERMS, CHRONUS historian, Cimphony Network Model Management.
- Customer evidence: JPS (Jamaica), SMUD, Salt River Project, Adani Electricity Mumbai.

## Product D — SurvalentONE ADMS (Tier 2, evidence layer A→B)

- Mid-market vendor (electric co-ops/municipals; also water/wastewater, transit, mining, oil & gas industries listed).
- Catalog structure is the key observation: the ADMS is composed of separately listed products — SurvalentONE SCADA; SurvalentONE OMS (Call Handler, Customer Outage Portal, OMS Dashboard, Damage Reporting and Assessment, Polaris map viewer); DMS applications grouped as Analysis & Forecasting (Distribution Power Flow, Distribution State Estimation, Short-Term Load Forecasting/Load Estimation), Demand Response (Dynamic Voltage Regulation, Load Curtailment, Rotational Load Shedding, Voltage Reduction), Distribution Automation (Distribution Contingency Analysis, Fault Location Analysis, "FLISR and Loss of Voltage", Power Factor Control, Protection Settings Manager, Volt/VAR Optimization); SurvalentONE DERMS; Advanced Applications (GeoBridge GIS integration, Operator Training Simulator, Operational Analysis Environment, Network Topology Processor, "Switch Orders and Guarantees", Helix historian, Schematic Generator, SurvCentral substation automation, Mirror, Live, WebSurv).
- Confirms: (a) SCADA, OMS, DMS apps are modules that compose an ADMS; (b) the same application names (power flow, state estimation, FLISR, FLA, VVO, load forecasting, training simulator, switch orders) recur across vendors; (c) the platform pattern extends to other network industries (water, transit) — the ADMS-as-Type remains electricity-distribution-specific while the SCADA/OMS substrate generalizes.

---

## Cross-product Comparison

| Structure / capability | Oracle NMS | GE GridOS ADMS | AspenTech OSI ADMS | SurvalentONE | Layer |
|---|---|---|---|---|---|
| Distribution network model (connectivity + electrical) as organizing core | Yes (ADMS Modeling; islands; phasing; limits) | Yes ("common T&D network model", digital twin) | Yes ("real-time network topology") | Yes (Network Topology Processor; GeoBridge from GIS) | B |
| Real-time telemetry monitoring on the model | Yes (Flex SCADA; Viewer) | Yes ("real-time monitoring") | Yes (monarch platform) | Yes (SCADA) | B |
| Supervisory control of field devices | Yes (Control Tool; SCADA Control user type) | Yes ("monitoring and control") | Yes ("monitoring and control applications") | Yes (SCADA control) | B |
| Operational event/alarm loop with recorded actions | Yes (Work Agenda, alarms, event logs, audit logs) | Yes (implied: outage management, metrics) | Yes (implied) | Yes (alarms/events agent) | B |
| OMS: calls → events → crews → restoration → records | Yes (deep: fuzzy calls, grouping, ERT, storm mode, callbacks, damage assessment) | Yes (OMS pillar; field mobility, damage assessment) | Yes (OMS pillar; job and crew management) | Yes (OMS product line) | B |
| Outage events carry ERT + critical-customer tracking + reliability indices | Yes (ERT, Emer/Med/Key/Sens, CMI/SAIDI-style indices, exclusions) | Yes (CMI, SAIDI, SAIFI named) | Yes (SAIDI in case study) | Yes (OMS dashboard) | B |
| Switching management: switching sheets/orders + safety documents/tags | Yes (sheets, states, safety documents, requests) | Yes (implied via control/OMS) | Yes (Switch Order Management pillar) | Yes (Switch Orders and Guarantees) | B |
| Power flow as computational core of network applications | Yes (explicit: "core of the ADMS functionality") | Yes (implied) | Yes ("real-time network topology and power flow") | Yes (Distribution Power Flow product) | B |
| State estimation | Yes (DSE chapter) | Not stated on fetched pages | Not stated on fetched page | Yes (product) | B (partial) |
| FLISR | Yes (documented algorithm) | Yes (named pillar capability) | Yes ("advanced applications") | Yes (named product) | B |
| Fault location analysis | Yes (FLA) | Not named on fetched pages | "advanced applications" | Yes (named product) | B |
| Volt/VAR optimization | Yes ("Optimization (formerly VVO)") | Yes (VVO in FAQ) | "advanced applications" | Yes (named product) | B |
| Load forecasting | Yes (load profiles, DER/weather forecasts, Look Ahead) | Yes (AI/ML load prediction) | Not stated on fetched page | Yes (Short-Term Load Forecasting) | B |
| Study mode (simulate without affecting real time) | Yes (explicit, per-tool) | Yes (simulations) | Yes ("study mode across all functionality") | Yes (Operational Analysis Environment) | B |
| Operator training simulator | Yes (Trainer user type) | Not stated on fetched pages | Yes (pillar) | Yes (named product) | B |
| DER management (DERMS) | Yes (Edge DERMS module + DER in model/apps) | Yes (built-in DERMS pillar) | Yes (suite incl. DERMS; ADMS page mentions DER management) | Yes (separate DERMS product) | B |
| Historian | Yes (historian + PI tab) | Not stated on fetched pages | Yes (CHRONUS, sibling product) | Yes (Helix) | B |
| GIS as model source | Yes ("Sources of Data") | Yes (data fabric) | Yes (Cimphony sibling) | Yes (GeoBridge) | B |
| AMI integration for outage confirmation | Yes (AMI requests/pings) | Not stated on fetched pages | Not stated on fetched page | Not stated on fetched pages | A (single-product, treat as common-implementation example) |
| Crew management | Yes (deep) | Yes (field mobility) | Yes (job and crew management) | Yes (OMS) | B |
| Storm mode | Yes (explicit storm/non-storm algorithms) | Yes ("severe weather", disruption management) | Yes (storm scenarios in OTS) | Yes (storm response hub) | B |
| Control zones / authority | Yes (explicit authority tool) | Not stated on fetched pages | Not stated on fetched page | Not stated on fetched pages | A (single-product detail; concept likely general but keep qualified) |
| Deployment: on-prem vs cloud/hybrid | On-prem/web clients (docs) | Hybrid cloud (platform claim) | Not stated on fetched page | Not stated on fetched pages | C/L2 |
| Automation posture of FLISR (advisory plan vs auto-execute) | "Formulate a plan" via controllable switches (plan-oriented) | "automates… restoration processes" | "intelligent automation" | Named capability, posture unstated | C/L2 |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

An ADMS is recognizable only if all four hold:

1. **Distribution network model** — a connected electrical model of the distribution system (feeders, switches/reclosers/breakers, transformers, phases, sources/islands) is the organizing structure of the system. Not a point list: connectivity is represented and maintained.
2. **Real-time monitoring on the model** — live telemetry/status from field devices is acquired and rendered on that network model.
3. **Supervisory control** — operators issue control/switching actions to field devices from the platform, with the action recorded.
4. **Operational event loop** — alarms/events are raised, assessed against the model, and answered with switching/restoration or other operational actions, leaving a persistent operational record (event/alarm/switching history).

Tests:
- Remove the network model → point-based SCADA remains (different Type).
- Remove real-time monitoring/control → planning/GIS/analysis tooling remains (different Type).
- Remove the operational event loop (no alarms/events/records, no operational response) → engineering analysis tool remains (different Type).
- Remove OMS, FLISR, VVO, training simulator → still an ADMS (a smaller one). Confirmed by the sample: Oracle treats OMS modules and ADMS applications as separately deployable; Survalent sells SCADA/OMS/DMS as separate products that compose an ADMS; GE/OSI present OMS and advanced apps as pillars/modules of the ADMS.

### L1 — Common Mature Structure (very common, not defining)

- OMS layer: trouble-call entry (incl. fuzzy calls), call→event prediction/grouping, outage events with ERT and critical-customer tracking, crew management (assign/dispatch/en route/on site/release), damage assessment, storm mode, callbacks, customer outage information, reliability indices (CMI/SAIDI/SAIFI).
- Switching management: switching sheets/orders with lifecycle states, safety documents (tags/grounds), switching requests from the field, overlap checks, impacted-customer preview, study-mode simulation of switching plans.
- Network applications built on power flow: state estimation, feeder load management, fault location analysis, FLISR, Volt/VAR optimization, load forecasting.
- Study mode across tools (simulate without touching real-time data).
- Alarm management (lists, shelving, nuisance handling, abnormal device lists).
- Historian (time-series storage of measurements/events).
- Operator training simulator.
- Integrations: GIS as the network-model source; AMI/meter pings for outage confirmation; DER visibility; crew mobile/field surfaces.
- Role model: operations vs switching vs SCADA-maintenance vs training vs view-only user types; control-zone authority.
- Reporting/dashboards (reliability metrics, storm reports, management reporting).

### L2 — Variant / Optional Structure

- DERMS depth: built-in module (GE, Oracle Edge DERMS) vs separate integrated product (AspenTech OSI DERMS, SurvalentONE DERMS); DER aggregation/market functions usually live in the DERMS side.
- Automation posture: FLISR as advisory plan (operator executes) vs supervised/automatic execution; VVO closed-loop vs recommendation.
- Module packaging: single integrated platform vs suite of separately licensed products (Survalent) vs platform+apps (GridOS).
- Deployment: on-prem control-room servers vs hybrid/cloud; web vs desktop clients.
- Network scope: distribution-only vs integrated T&D model and coordination (GE T&D coordination; Oracle models sub-transmission sources).
- Industry extension of the substrate: same SCADA/OMS pattern sold for water/gas (Oracle "OMS for Water"; Survalent water/transit/mining industries) — but the ADMS-as-Type (power flow, voltage, phases, FLISR) is electricity-specific.
- Regional operating-practice differences: safety-document regimes, switching-order conventions, terminology (Oracle glossary explicitly notes "regional and national differences exist").
- AI/ML additions: load prediction, disruption prediction (GE claims).

### L3 — Vendor-specific (research notes only)

- Oracle: Flex SCADA, Web Workspace, Work Agenda, Edge DERMS, Flex Operations client, "Optimization (formerly VVO)" renaming, Suggested Switching, Smart Grid Gateway integration, PI historian tab, control-zone rule sets, specific cause-code taxonomies.
- GE Vernova: GridOS platform, GridOS Data Fabric, Zero Trust grid security, GNM/VI/Field modules, microservices claims, Guidehouse leaderboard marketing.
- AspenTech: monarch™ platform, CHRONUS historian, Cimphony Network Model Management, Grid Apps.
- Survalent: Polaris, GeoBridge, Themis, Helix, SurvCentral, Utiliverse services.

## Vendor-specific Findings

- Oracle is the only sampled vendor with public operational documentation deep enough to verify internal workflows (switching sheet states, FLISR algorithm steps, event cause codes, user-type matrix). Claims about industry-wide workflow details (e.g., exact sheet states) must stay Oracle-specific or be marked as one implementation.
- GE's "grid orchestration vs grid management" framing is positioning, not structure; its structural claims (DMS+OMS+DERMS on a common model) match the other samples.
- Survalent's catalog is the clearest evidence that SCADA/OMS/DMS are composable modules rather than inseparable parts of one monolith.

## Boundary Findings

- **vs SCADA (§16 sibling)**: SCADA is the telemetry-and-control layer organized as points/devices without requiring a connected electrical network model; ADMS is operations on the network model (which consumes SCADA or embeds it). Test: remove the network model and network-aware applications → SCADA remains; remove nothing from ADMS and you cannot call it SCADA-only. In the sampled market SCADA is either a module inside the ADMS (Oracle Flex SCADA, GE CIMPLICITY lineage, AspenTech monarch) or an integrated sibling (SurvalentONE SCADA).
- **vs Distribution Management System / DMS (sibling leaf)**: historically DMS = the network-analysis application suite; in the current market "ADMS" is the umbrella term for the integrated platform (SCADA + DMS applications + OMS on one model/UI). Every sampled vendor markets "ADMS", not "DMS", for the integrated platform; Oracle's own implementation guide is titled "ADMS Implementation Guide" while the applications layer is still called DMS-style (power flow, FLISR, VVO). Probable supertype/alias relationship — flag for joint review when DMS is processed.
- **vs Outage Management System / OMS (sibling leaf)**: OMS is present as a module/pillar in every sampled ADMS, but a standalone OMS can exist without real-time network monitoring/control (call-center-centric OMS). Test: remove real-time network monitoring/control → OMS remains (different Type); remove OMS → ADMS remains. Capability/module relationship — flag for joint review when OMS is processed.
- **vs Energy Management System / EMS (sibling leaf)**: same structural pattern (network model + real-time monitoring/control + operational loop + network applications) applied to the transmission system, with transmission-specific applications (AGC, N-1 contingency analysis, market operations) and different operators. Related Type sharing the pattern, not a duplicate — same relationship as fleet-management vs robot-fleet-management.
- **vs DERMS (sibling leaf)**: DERMS centers on the DER fleet (aggregation, forecasting, dispatch, market participation); ADMS centers on the distribution network itself. In the sample DERMS appears both as an ADMS module (GE built-in, Oracle Edge DERMS) and as a separate platform integrated with the ADMS (AspenTech, Survalent). Flag for joint review when DERMS is processed.
- **vs Grid Operations Platform (sibling leaf)**: generic umbrella term; the sampled market uses "ADMS" as the concrete distribution control-room platform. Flag for joint review.
- **vs Utility GIS (sibling leaf)**: GIS holds the as-built geographic asset records and is the typical *source* of the ADMS network model; the ADMS runs real-time operations on an operational copy. Remove real-time operations → GIS remains.
- **"Advanced" is a market-era label, not a structural test**: the term ADMS emerged as DMS+OMS+SCADA converged; sampled vendors treat FLISR/VVO/DERMS as modules. The definition must not require any specific advanced application.

## Historical / Market-Sample Check

- Older distribution SCADA (point-based telemetry + control, no network model): does NOT satisfy L0 → correctly excluded (it is the SCADA Type).
- Older DMS (network model + power flow/VVO, no OMS, no outage management): satisfies L0 → included; the definition correctly does not require OMS.
- Standalone OMS (calls/crews/outage records, no real-time network model): does NOT satisfy L0 → correctly excluded (OMS Type).
- Regional products (European/Asian control-center systems with different safety-document regimes): L0 holds — the safety-document specifics are L1/L2, not definitional.
- Water/gas network operations platforms: share the SCADA/OMS substrate but lack the electrical network model (phases, voltage, power flow); the ADMS definition stays electricity-distribution-specific.

## Uncertainties

- Exact state machines (switching sheet states, event statuses) verified only in Oracle docs; treated as one implementation, not industry standard.
- Control-zone authority model verified only in Oracle docs; the general concept (zone-based operating authority) is standard industry practice but kept qualified in the final document.
- FLISR automation posture (advisory vs auto-execute) varies and vendor pages differ in emphasis; documented as a variant, not a rule.
- Hitachi Energy Network Manager, Siemens Spectrum Power, Schneider EcoStruxure ADMS could not be fetched; their structures are inferred from market position only and were NOT used as evidence.
- Training-simulator prevalence: verified in 3 of 4 samples (Oracle user type, OSI pillar, Survalent product); GE page silent — treated as common but not universal.

## Final Synthesis

An ADMS is the distribution utility's real-time operations platform: a connected electrical model of the distribution network, live telemetry rendered on it, operator control over field devices, and an operational loop that turns alarms, trouble calls, and switching plans into recorded, safety-gated actions on the network. Around that core, mature products add an outage-management layer (calls → events → crews → restoration → reliability records), a switching-management layer (sheets/orders + safety documents), and a family of network applications computed on the power-flow core (state estimation, fault location, FLISR, Volt/VAR optimization, load forecasting), plus study mode, historian, and a training simulator. DER management, cloud deployment, and automation depth are current-market differentiators, not defining structure. The defining core is deliberately small enough to include a 1990s-era DMS with a network model and control, and to exclude point-based SCADA, call-center-only OMS, GIS, and planning tools.
