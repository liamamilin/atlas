# Research Notes — OEE Management Platform

## Research Goal

Determine what an "OEE Management Platform" is as a distinct Application Type: what the OEE measurement model actually consists of in real products, what objects these systems manage, how measurement turns into "management", and where the boundaries lie against the dense §16 cluster — Factory Operations Management (joint-review flag pre-hung against this leaf), MES (OEE held there as a derived view), machine monitoring / Industrial IoT, CMMS, SPC/Manufacturing QMS, Shop Floor Management, and generic BI.

Two pre-hung flags from prior passes must be discharged from this side:

1. **factory-operations-management (2026-09-08)**: "JOINT REVIEW RECOMMENDED with oee-management-platform — OEE measurement present in 4/4 samples but held as standard capability, not definitional (removing the response loop degenerates exactly into that neighbor)"; boundary held there as "vs OEE Management Platform (OEE = output of the record, not the center)".
2. **manufacturing-execution-system-mes (2026-09-09)**: "oee-management-platform pass should note OEE present across all sampled products as a derived view, non-definitional" (in MES products).

## Initial Boundary (working hypothesis, pre-research)

- Core use: measuring and improving Overall Equipment Effectiveness — the share of planned production time that produces good output at reference speed — across machines/lines/shifts/plants.
- Likely users: production managers, continuous-improvement staff, plant management; operators as data captors and dashboard consumers; maintenance as a downstream consumer of downtime data.
- Likely nearest neighbors: Factory Operations Management (live ops + response loop), MES (execution + as-built), machine monitoring/IIoT (data substrate), CMMS (maintenance), SPC/QMS (quality records), Shop Floor Management (response loop), BI (generic analytics).
- Unknowns: is the full Availability × Performance × Quality formula definitional, or do real products ship partial versions? Is the improvement loop part of the Type or just common? Where exactly is the seam with production monitoring / machine monitoring, which uses nearly the same data?

## Research Questions

1. What is the OEE computation model as implemented (components, denominators, reference rates)? Do all products compute full A×P×Q?
2. What objects does the system manage (equipment hierarchy, shifts/calendars, products/reference rates, downtime reasons, counts, targets)?
3. How is data captured (automatic machine connectivity vs operator entry vs hybrid), and is automatic collection definitional?
4. What does "management" add beyond measurement (targets, benchmarks, Pareto, trends, review meetings, improvement verification)?
5. Where are the seams: vs Factory Operations Management (response loop), vs MES (OEE as derived view), vs machine monitoring/IIoT (raw signals), vs CMMS, vs SPC/QMS, vs BI?
6. Would the definition survive the paper-era / spreadsheet-era OEE practice (TPM boards, OEE spreadsheets) — the historical check?

## Representative Products

Chosen for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| Evocon | dedicated OEE software (self-labeled "OEE software"), automatic sensor collection, visual/shift-centric | SME → global multi-site (food, packaging, building materials) | excellent (official product pages + OEE methodology articles fetched) |
| MachineMetrics | machine-data-centric production monitoring with OEE & production analytics; CNC/discrete heritage | SME → enterprise discrete manufacturers | medium (official marketing/product pages fetched; support docs timed out — assertion strength reduced) |
| FourJaw | plug-and-play SME manufacturing analytics; **partial OEE (Availability + Quality only)** | SME-heavy UK base, some global | excellent (official product, OEE feature, CI function pages + help center fetched) |

Cross-referenced adjacent-platform evidence (layer A, fetched 2026-09-08 in the factory-operations-management pass, URLs and verbatim quotes recorded in `research/factory-operations-management.md`): **L2L** (Machine Data Sync "automate OEE calculations and downtime tracking"; downtime/OEE dashboards), **Tulip** (machine states Running/Stopped/Idle + downtime reasons "feed OEE calculations and analytics"), **Siemens Opcenter** (suite pole: "performance analysis — up-to-the-minute reporting of actual manufacturing operations"; "equipment and personnel performance — track resource usage based on elapsed usage time and production quantities").

Rejected/failed samples: Mingo/SensrTrx (transport error ×2 — abandoned), Amper (transport error ×2 — abandoned), Matics (transport error ×2 — abandoned), MachineMetrics support subdomain (timeout; 404 on /solutions/oee), Evocon docs subdomain docs.evocon.com (transport error). Mid-market and plastics-vertical poles under-sampled — recorded under Uncertainties.

## Sources

All fetched 2026-09-09 unless noted:

- Evocon — homepage: https://evocon.com/
- Evocon — OEE software product page: https://evocon.com/oee-software/
- Evocon — "What Is OEE and How Does It Work?" (methodology article, from "OEE at Work" by Wetherill & Künnapuu): https://evocon.com/articles/what-is-oee-and-how-does-it-work/
- Evocon — OEE Dashboard feature page: https://evocon.com/feature/oee-dashboard/
- Evocon — How Evocon Works: https://evocon.com/how-evocon-works/
- Evocon — OEE Monitoring software page: https://evocon.com/oee-monitoring-software/
- MachineMetrics — homepage: https://www.machinemetrics.com/
- MachineMetrics — Production Monitoring (OEE & production analytics): https://www.machinemetrics.com/production-monitoring
- FourJaw — homepage: https://www.fourjaw.com/
- FourJaw — OEE Monitoring feature page: https://fourjaw.com/features/oee-machine-monitoring
- FourJaw — Continuous Improvement function page: https://fourjaw.com/functions/continuous-improvement
- FourJaw — Help Center index: https://help.fourjaw.com/knowledge
- Cross-referenced (fetched 2026-09-08, prior pass): L2L platform/production-management pages; Tulip knowledge base (machine states doc); Siemens Opcenter portfolio pages — see research/factory-operations-management.md §Sources for URLs.

Not reachable: docs.evocon.com, support.machinemetrics.com (timeout), matics.ai / mingoadaptive.com / amper.com (transport errors ×2 each). No independent standards text (e.g., an ISO OEE definition) was fetched; the A×P×Q model rests on vendor-published methodology (Evocon's detailed public article) plus the TPM lineage that vendors themselves state.

## Product Observations

### Evocon (dedicated OEE software pole)

Key observations (evidence layer A — official pages):

- Self-label: "a visual and user-friendly OEE software"; product page titled "OEE software. Easy to use. Easy to understand."
- OEE definition (methodology article): "a lean manufacturing tool and universal best practice to monitor, evaluate and improve the effectiveness of a production process. This could be an assembly line, machine cell, packaging line, filling machine, etc." Primary purpose: "drive improved asset performance... through visualizing, quantifying, and systematically eliminating sources of production loss."
- "Hidden factory" framing: OEE shows what was produced vs "what we could have produced – our hidden factory".
- Calculation model, verbatim structure: **OEE = Availability × Performance × Quality**.
  - Availability = Run Time / Planned Productive Time; planned productive time = "the sum of your scheduled shifts minus planned shutdowns and lack of demand".
  - Performance = actual throughput / maximum throughput (based on "Maximum demonstrated rate" (MDR) or "ideal cycle time").
  - Quality = right-first-time / total production ("total production – rejects").
- Six Big Losses (stated origin: TPM): unplanned stops + planned stops (availability); micro stops + slow cycles (performance); production rejects + start-up rejects (quality).
- Important boundary rule stated by the vendor: planned activities such as maintenance shutdowns, major plant overhauls, and demand-idled shifts are NOT counted as availability loss and are excluded from the OEE calculation.
- Common calculation mistakes documented: excluding too many stops (changeovers are losses when they overrun); unknown MDR → performance over 100% ("You can solve this by contacting your machine manufacturer... If that is not possible, you can set a benchmark based on the fastest recorded shift"); manual scrap counting; quality data arriving weeks late ("include the data in the OEE calculation in hindsight").
- Data collection: sensor detecting products on the line → Evocon IIoT device → cloud (AWS) → browser display. Alternates: existing sensor, PLC output via relay (e.g., Andon lights), or a "hardware-free solution" reading a local database via HTTPS API.
- Configuration inputs required at setup: machine type; signals to track (pieces, time, meters, liters, flow); products and cycle times; shift times; loss reasons; operators.
- Interfaces: **Shift View** (real-time shift performance across dates, stations, factories, countries); **OEE Dashboard** (widgets for OEE, downtime, speed loss, scrap, checklists; comparison with previous periods; trend lines; performance vs target; filter by factory/station/time period/reason; automatic tab rotation for always-on shop-floor displays; time periods from the ongoing shift to the last 12 months); **Factory Overview** (live machine/factory status); **Reports** (downtime tracking and analysis); **Checklists** (recurring quality/maintenance checks driven by real-time machine data).
- Operator role: on shop-floor displays, "operators can record reasons for stoppages and get real-time feedback about production performance".
- Management loop: "Real-time production data keeps your daily and weekly meetings on track"; customer quote: "Evocon is at the heart of our daily follow-ups regarding production, and we also use it on a daily basis to cover the needs of maintenance and activity planning"; another: "engaged the whole shop-floor working with the losses, resulting in faster solving of problems and improved quality of waste elimination projects."
- Spreadsheet lineage artifact: the vendor ships a free **OEE Excel template** ("to easily track and calculate your OEE") and an OEE calculator — the manual-practice baseline the software digitizes.
- ERP/BI integration exists (case study: Evocon + Business Central + Power BI).

Interpretation: the purest in-sample expression of the Type — the OEE measure and its loss decomposition are the product's center; everything else (checklists, factory overview) hangs off the measurement model.

### MachineMetrics (machine-data-centric pole)

Key observations (evidence layer A for the marketing/product pages; support docs not fetched — assertion strength reduced accordingly):

- Production monitoring page: "MachineMetrics production monitoring software monitors OEE, machine utilization, and downtime for maximum production efficiency and deep operational insights. No manual data entry required."
- OEE capability, verbatim: "Visualize, analyze, and optimize actual cycle times for performance, machine availability, and quality metrics to monitor and improve OEE." — the three components named explicitly.
- Collection: MachineMetrics Edge device connected to the machine control's ethernet port; data processed at the edge and streamed to the cloud; universal connectivity across makes/models (MTConnect, OPC UA, Ethernet/IP, etc.); "No Manual Data Entry Required — Automatically collect production data from equipment without requiring any input from operators."
- Analytics: "Report on downtime events and quality issues with Pareto charts to highlight the most common reasons for inefficiency"; "Monitor the performance of each production run, measuring it against historical data and breaking it down at the shift, cell, machine, and operator levels"; utilization "by hour, shift, day, week, and month... uncover hidden capacity".
- Live surfaces: KPI dashboards "with simple color-coded tiles"; alerts + notifications with workflows ("reassignment, resolution, and full audit tracking").
- Management rhythm: "Daily Production Dashboard" — "Every day, production leaders across the shop floor start their morning the same way: open the Daily Production Dashboard, scan dozens of machines..." (now with AI summaries).
- Job context via ERP connectors (work order tracking); scheduling and MES-adjacent modules exist but are separate applications.
- Benchmarking/comparison: "Compare performance across machines, shifts, and part operations to identify inefficiencies, unlock hidden capacity."

Interpretation: same measurement model, entered from the machine-data side; OEE is one application among several on the data platform. Useful as the pole showing the OEE platform's dependence on (and seam with) machine monitoring.

### FourJaw (SME plug-and-play pole — partial OEE)

Key observations (evidence layer A — official pages + help center):

- Self-label: "Factory Intelligence. Made Simple."; "plug-and-play manufacturing analytics platform".
- **Partial OEE, explicitly**: "FourJaw's machine monitoring platform is designed to measure and track Availability and log and report on Quality." The FAQ names the three-factor model ("The OEE measure in manufacturing looks at three factors: Quality, Performance and Availability") but the product ships two of them. Performance is not reported.
- Availability definition: "monitors a machine, cell, or factory's actual runtime versus planned runtime... A score of 100% means your machine ran continuously throughout its planned production time — no stops at all."
- Quality definition: "the proportion of the parts your machines produce that are good, not scrapped or reworked"; Production Quantity report shows "total good quantity, scrap quantity, and quality percentage... broken down by job reference, machine, and machine area".
- Loss attribution: "OEE in FourJaw tracks the availability of your machine using the downtime reasons logged by machine operators. Examples of Availability Downtime reasons include: Machine fault, Tool broken, Set Up, Unplanned maintenance."
- Trend surfaces: "See your overall Availability OEE trend by hour, day or shift. Zoom out or in — see your OEE trend by factory, cell, production line or machine." Downtime Pareto "to reveal the top causes".
- Collection: sensor clipped to machine power cables → MachineLink IoT device → WiFi; "works on ANY Machine, regardless of age or type". Operators "use tablets on the shop floor to log downtime reasons quickly and accurately"; managers/CI leads "use the web app".
- Management loop, verbatim (DMAIC mapping): "Define problems using real downtime data. Measure performance with live OEE and utilisation metrics, analyse root causes with downtime Pareto, improve by tracking interventions in real-time, and control results with ongoing visibility." Also: before/after comparison of improvement initiatives ("Compare before-and-after performance, track key metrics like OEE or uptime"); data used in "daily meetings and quarterly director reviews"; daily huddles, kaizen events, tier meetings.
- Boundary statement (FAQ), verbatim: "How is FourJaw different from MES or ERP systems? FourJaw is a machine monitoring and production analytics platform... Unlike traditional MES and ERP systems, which can be complex, expensive, and time-consuming to implement... Many manufacturers use FourJaw alongside their existing MES or ERP system to gain the real-time shop floor insights that traditional systems often lack."
- Job roles addressed: Managers, Continuous Improvement, Finance, Planners, Machine Operators.
- Spreadsheet lineage artifact: case study titled "From Spreadsheets to Clarity in Automotive Remanufacturing".

Interpretation: proves the component scope is variable — a product can be squarely an OEE management platform while shipping only a subset of the canonical components. The full A×P×Q formula therefore cannot be the defining invariant; the loss-accounting model can.

### Cross-referenced adjacent platforms (evidence from the FOM pass, layer A)

- **L2L**: Machine Data Sync integration package — "Connect L2L to your PLCs, SCADA systems, and IIoT devices to automate OEE calculations and downtime tracking"; dashboards for downtime and OEE; OEE sits inside the Stabilize → Standardize → Optimize improvement method. OEE is a capability of a broader connected-operations platform.
- **Tulip**: machine states (default Running/Stopped/Idle) and a default downtime-reason list; "states feed OEE calculations and analytics". OEE is an output of the machine-state model inside a composable frontline-operations platform.
- **Siemens Opcenter** (suite pole): "performance analysis — up-to-the-minute reporting of actual manufacturing operations"; "equipment and personnel performance — track resource usage based on elapsed usage time and production quantities". Effectiveness/performance analysis is a named MOM capability inside the suite, beside MES execution, quality, and planning.

Interpretation: across adjacent platform Types, OEE appears consistently as a **derived view** — computed from state/count data that some other center (execution, operations, connectivity) owns. This corroborates the MES pass flag and sharpens this leaf's identity: here the measure is the center, not the output.

## Cross-product Comparison

| Dimension | Evocon | MachineMetrics | FourJaw | L2L / Tulip / Opcenter (cross-ref) |
|---|---|---|---|---|
| Self-label | "OEE software" | "production monitoring... monitors OEE" | "manufacturing analytics" / OEE Monitoring application | OEE as capability inside MOM / frontline platform |
| Effectiveness measure | full A×P×Q | A, P, Q components named; OEE reported | **Availability + Quality only** (partial) | OEE computed as derived view |
| Planned-time accounting | explicit (scheduled shifts − planned shutdowns − lack of demand) | implied (utilization vs available time) | explicit ("actual runtime versus planned runtime") | shift/line grain (L2L), state-based (Tulip) |
| Reference rate for performance | MDR / ideal cycle time; fallback = fastest recorded shift | actual vs ideal cycle times | not applicable (no Performance component) | cycle-time/rate based |
| Loss attribution | coded loss reasons; Six Big Losses taxonomy; changeover overrun example | downtime reasons + Pareto; quality issues Pareto | operator-logged downtime reasons (Machine fault, Tool broken, Set Up...) + Pareto | downtime reasons (Tulip default list; L2L failure modes) |
| Capture posture | sensor/IIoT device; PLC relay; hardware-free API variant | edge device, fully automatic, "no manual data entry" | power-cable sensor + operator tablets for reasons | PLC/SCADA/IIoT sync (L2L); machine triggers + operator apps (Tulip) |
| Live surfaces | Shift View, Factory Overview, shop-floor TVs/tablets | KPI dashboards, color-coded tiles, operator view | dashboards, alerts | live boards (L2L), station apps (Tulip) |
| Trend/analysis | trends, vs previous periods, vs target, 12-month lookback | per-run vs historical; hour→month utilization | trends by hour/day/shift; factory→machine zoom | OEE/downtime dashboards; analytics modules |
| Management loop | daily/weekly meetings on the data; targets; "working with the losses" | daily production dashboard (morning ritual); alerts→workflows | DMAIC mapping; before/after initiative verification; huddles/kaizen/tier meetings | Stabilize→Standardize→Optimize (L2L); CI tooling |
| Improvement verification | trend lines, vs-target analysis | per-run vs historical benchmarks | explicit before/after comparison | RCA + corrective actions (L2L) |
| Downstream consumers | maintenance & activity planning (customer quote) | maintenance (condition data → CMMS work orders) | finance, planners (costing, scheduling) | maintenance work orders (L2L), quality (Tulip) |
| ERP integration | yes (Business Central case study) | yes (ERP connectors, job context) | alongside MES/ERP (FAQ) | ERP sync (L2L), ERP system-of-record (Tulip) |
| Spreadsheet/manual lineage artifact | OEE Excel template shipped by vendor | "No more clipboards" (customer quote) | "From Spreadsheets to Clarity" case study | — |

Evidence layer B findings (cross-product commonality):

- **The loss-accounting measurement model** (planned production time vs downtime; output vs reference; good vs total) — present in all three deep samples in at least two components each; full A×P×Q in two of three.
- **Loss attribution through coded reasons + Pareto** — 3/3 deep samples; Tulip's default reason list and L2L's failure-mode tracking corroborate across platform poles.
- **The management loop anchored on the measure** (targets/benchmarks, trends over time, meeting rhythm, improvement verification) — 3/3 deep samples, phrased differently (meetings / daily dashboard / DMAIC) but structurally identical.
- **Automatic machine-data collection as the dominant posture** — 3/3, but NOT required: Evocon documents a hardware-free/operator-entry variant; FourJaw's reasons are operator-logged; the paper-era practice satisfies the core without any connectivity.
- **Operator as data captor and dashboard audience** — 3/3 (shop-floor displays/tablets).
- **Multi-grain rollup** (machine → cell/line → factory → multi-site; shift → day → month) — 3/3.
- **Downstream hand-off** of downtime/quality data to maintenance, planning, finance — 3/3 in differing depths.
- **ERP-adjacent posture** — the Type consumes order/product context where available but does not own orders (Evocon integrates; MM connectors; FourJaw "alongside your existing MES or ERP").

## Canonical Model (Layer C)

### L0 — Defining Invariant

An OEE Management Platform is the manufacturer's system for measuring and managing equipment effectiveness. Three structures, jointly held:

1. **The effectiveness measurement model.** A defined production unit (machine, line, cell, station) is measured against a time-and-output accounting structure: planned production time (the denominator, with explicit exclusions), lost/stopped time, output against a reference rate, and good vs total output — computed into an effectiveness score (OEE) or a documented subset of its canonical components (Availability, Performance, Quality). Remove this leg → machine data collection / metering with no effectiveness model; the Type collapses into monitoring substrate.

2. **Loss attribution.** The score is decomposable into attributed losses: coded downtime/stop reasons, component-level breakdown (which of availability/performance/quality was lost, and why), typically surfaced as reason analyses and Pareto views. Remove this leg → an unexplained score; the measure cannot drive action.

3. **The effectiveness-management loop.** The measure is managed over time: targets or benchmarks are set, trends are tracked, losses are reviewed on a defined rhythm (daily/weekly meetings, tier reviews), and improvement actions are verified against the same measure (before/after comparison). Remove this leg → passive OEE reporting/analytics — the seam where this Type degenerates into production monitoring.

Jointly-held is load-bearing:

- 1 alone = machine metering / data collection
- 2 without 1 = a downtime log or spreadsheet with no computed measure
- 3 without 1+2 = generic KPI/goal tracking with no effectiveness model
- 1+2 without 3 = passive OEE analytics (the production-monitoring seam)
- 1+3 without 2 = score-chasing without loss structure

The full Availability × Performance × Quality formula is the **dominant realization** of leg 1, not the invariant itself: a sampled product ships Availability + Quality only and remains squarely in-type. What is invariant is the accounting structure (planned time, losses, output, quality of output) — not the completeness of the canonical decomposition.

### L1 — Common Mature Structure

- Automatic machine-data collection (sensors on the line, PLC/edge connections, protocols such as OPC UA/MTConnect class) producing states and counts without operator input — dominant but not required (operator-entry and hybrid postures documented; paper-era practice satisfies the core).
- Real-time/live surfaces: shift views, factory overviews, shop-floor displays (TVs, tablets, wall boards), color-coded status.
- Operator data capture: reason entry for stops on shop-floor devices.
- Downtime Pareto and reason analysis; utilization reporting alongside OEE.
- Alerts/notifications routed to responsible roles.
- Multi-grain, multi-site rollup and comparison (machine/cell/line/factory; shift/day/week/month).
- ERP integration for order/product/job context; export/BI integration (APIs, Power BI-class).
- Recurring checks/checklists driven by machine state (quality/maintenance checks at the point of work).
- AI assistance (summaries of daily production, suggestions) — emerging, not definitional.

### L2 — Variant / Optional Structure

- Component scope: full A×P×Q vs partial (Availability-only or Availability+Quality) — a primary segmentation axis documented in-sample.
- Reference-rate discipline: machine-nameplate/ideal cycle time vs maximum demonstrated rate vs fastest-recorded-shift benchmark.
- Collection posture: fully automatic vs operator-entry vs hybrid; plug-and-play sensor kits vs PLC integration vs software-only/API.
- Standalone product vs suite-embedded module (dedicated OEE vendors vs MOM/MES suites and frontline platforms carrying OEE as a capability).
- Industry packaging: discrete/CNC vs packaging/food/FMCG vs plastics/process.
- Deployment: cloud SaaS vs on-premise; hardware-inclusive vs bring-your-own.
- Adjacent applications bundled on the same data: energy monitoring, condition monitoring/predictive maintenance, scheduling.

### L3 — Vendor-specific (Research Notes only)

- Evocon: Shift View / Factory Overview naming; IIoT device + sensor kit shipped for trials; OEE Excel template and OEE calculator as lead artifacts; "5-Day Guide to Launch OEE Monitoring"; "Decoding World-Class OEE" report (vendor-analyzed dataset of 3,500+ machines across 50+ countries — marketing number, excluded from canonical statements); checklists module.
- MachineMetrics: Edge device; Max AI; Production Schedule Intelligence; "Intelligent MES" self-labeling (market-label noise — the OEE/monitoring application is the relevant part here); Daily Production Dashboard with AI summaries.
- FourJaw: MachineLink IoT hardware (power-cable sensors); Productivity Accelerator Programme (structured CI engagement); UK Manufacturing Productivity Index; energy monitoring application; "Factory Intelligence. Made Simple." positioning.
- L2L: Machine Data Sync package; Stabilize/Standardize/Optimize method. Tulip: default state/reason lists. Siemens: Opcenter Performance/Intelligence module names.

## Vendor-specific Findings

See L3. Additional product-specific statements kept out of the canonical document: Evocon's customer-quote claims about waste-elimination project quality; FourJaw's customer ROI percentages (10–30% productivity improvements); MachineMetrics' customer utilization/capacity percentages. All are marketing claims without operational-documentation support.

## Boundary Findings

- **vs Factory Operations Management (the pre-hung joint review — DISCHARGED from this side).** FOM's defining core: live operational picture + event-and-response loop + operational performance record. This Type's defining core: the effectiveness measurement model + loss attribution + the measure-anchored management loop. The seam: **FOM centers the running operation and the response to events; this Type centers the effectiveness measure and its improvement.** In FOM products OEE is "the output of the record, not the center" (FOM pass wording); here it is the center. Removing the response/dispatch loop from FOM degenerates into this Type's territory (FOM pass's own observation); removing the effectiveness-measurement center from this Type leaves machine monitoring. Both directions confirm two Types sharing data (states, downtime reasons, counts) with different centers. Keep-both RATIFIED; both documents cross-referenced.
- **vs Manufacturing Execution System / MES.** The MES pass held OEE as "a derived view, present in all sampled products but non-definitional" for MES. Confirmed from this side: MES centers execution enforcement + the as-built record; OEE here is computed from execution/state data. Suite poles bundle both (Opcenter). Remove the effectiveness-measurement center → MES/monitoring territory; add enforcement + as-built → MES.
- **vs Industrial IoT Platform / machine monitoring.** IIoT/monitoring is the connectivity-and-signals substrate; this Type consumes its data to compute the effectiveness model. A machine-monitoring product without the planned-time/loss/output accounting stays monitoring. In-sample, MachineMetrics straddles both markets (monitoring platform with an OEE application) — a product-level straddle, not Type identity. Evocon and FourJaw both describe themselves against "machine monitoring" while shipping the OEE model on top.
- **vs CMMS / EAM.** Maintenance is a downstream consumer: downtime reasons and condition data feed maintenance action; the asset-care center (work orders, asset registry, PM schedules) stays with CMMS. Customer evidence: Evocon used "daily... to cover the needs of maintenance and activity planning"; MM pushes condition data into CMMS work orders.
- **vs SPC / Manufacturing QMS.** Quality counts (scrap, rejects, good-part proportion) feed the Quality component; formal quality records, control charts, and CAPA stay with the quality leaves. Evocon's checklists digitize recurring checks but are not a QMS record center.
- **vs Shop Floor Management.** The response loop is shared territory (FOM pass already drew this seam). This Type's delta is the effectiveness measure as the managed center; a shop-floor visual-management practice can exist with no computed effectiveness score.
- **vs BI / analytics platforms.** Generic BI lacks the OEE measurement model — the planned-time denominator, reference rates, and the loss taxonomy are domain structure, not generic charting. Several products export to BI (Evocon→Power BI case study; MM→Power BI/Tableau/Grafana connectors) — the export relationship confirms the seam.
- **vs Production Planning / APS.** The plan is consumed (planned time, planned output, order context), not owned. No sampled product owns the forward plan.
- **"Remove what → becomes the neighbor" test:** remove the effectiveness model → machine monitoring/IIoT; remove loss attribution → a bare score/meter; remove the management loop → passive OEE reporting (production-monitoring seam); add the live event-response dispatch loop as the center → Factory Operations Management; add execution enforcement + as-built record → MES; keep only the quality component's records → QMS territory.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **TPM-era origin (1980s Japan):** OEE was introduced as a manual improvement metric within Total Productive Maintenance — planned-time accounting on paper, the Six Big Losses as the loss taxonomy, and kaizen/team meetings as the management loop. All three L0 legs are satisfiable without software: a shift plan with planned time, a coded downtime/loss ledger, and a target-and-review routine. The vendors' own lineage statements (Evocon: Six Big Losses "has its origins in the development of TPM") support this.
- **Spreadsheet era:** OEE tracked in spreadsheets — still a living practice the sampled vendors explicitly digitize (Evocon ships an OEE Excel template; FourJaw's case study "From Spreadsheets to Clarity"; MachineMetrics customer quote "No more clipboards needed"). The spreadsheet satisfies legs 1–3 with manual capture.
- **Regional variants:** OEE is a global lean/TPM standard practice; utilization-only or availability-only regional variants correspond to the partial-component pole already documented in-sample (FourJaw).
- The modern era adds automatic machine connectivity, real-time surfaces, and AI — era-current capability, not definitional.

Conclusion: L0 passes the historical check; machine connectivity, the full A×P×Q decomposition, real-time display, and cloud delivery are held outside the defining core.

## Uncertainties

1. Mid-market and vertical poles under-sampled: Mingo/SensrTrx, Amper, and Matics were unreachable (transport errors ×2 each, abandoned per network rules). Assertions about the mid-market OEE-tool landscape rest on the three deep samples plus cross-referenced platform evidence.
2. MachineMetrics evidence is marketing/product-page only (support subdomain timed out); workflow-level detail for that pole is inferred from product pages. Its claims are used for boundary triangulation, not canonical structure.
3. Evocon's documentation subdomain (docs.evocon.com) was unreachable; product pages and the public methodology article were used instead — coverage of admin/configuration UI detail is thinner than the methodology detail.
4. No independent standards text (an ISO OEE definition or similar) was fetched; the A×P×Q model and its denominators rest on vendor-published methodology (Evocon's detailed article) plus the TPM lineage vendors themselves state. The model is nevertheless cross-corroborated: MachineMetrics names the same three components; FourJaw's FAQ names the same three factors.
5. The enterprise-suite pole (Siemens/GE-class) was not directly fetched this pass; its OEE-as-capability status is corroborated through the FOM pass's layer-A evidence (Opcenter pages, fetched 2026-09-08).
6. Vendor benchmark numbers ("world-class OEE", productivity-improvement percentages) were excluded from all canonical statements per evidence rules.
7. Whether any product computes OEE with zero loss attribution (a bare score) was not observed; the load-bearing analysis treats 1+3-without-2 as a theoretical degenerate, not a documented market form.

## Final Synthesis

The OEE Management Platform is the equipment-effectiveness management system: it holds a defined production unit against a time-and-output accounting model (planned production time, lost time, output vs reference rate, good vs total output), computes an effectiveness score — canonically Availability × Performance × Quality, sometimes a documented subset — decomposes the score into attributed, coded losses (reason taxonomies, component breakdowns, Pareto), and manages the measure over time: targets and benchmarks, tracked trends, a review rhythm (daily/weekly meetings, tier reviews), and improvement actions verified against the same measure. Data arrives predominantly from automatic machine connectivity, with operator reason-entry and even fully manual postures as documented variants. The Type sits downstream of machine connectivity (IIoT/monitoring substrate), beside MES and Factory Operations Management (which own execution and the live response loop respectively, and compute OEE only as a derived view), and upstream of CMMS/quality/planning consumers. Its market forms range from dedicated OEE products through machine-data platforms with OEE applications to suite-embedded modules — one Type, one center: the effectiveness measure as the managed object.
