# Research Notes — Emissions Monitoring / CEMS

Research date: 2026-09-08
Leaf: "Emissions Monitoring / CEMS" (DIRECTORY.md §21 Environment, Sustainability & Climate)
Slug: emissions-monitoring-cems

## Research Goal

Understand what the software application behind a Continuous Emissions Monitoring System (CEMS) actually is: what objects it manages, how instrument data becomes regulatory compliance data, who operates it, and where its boundary lies against ambient air quality monitoring, carbon accounting, SCADA/historians, and EHS platforms.

## Initial Boundary (hypothesis before research)

- Core hypothesis: this is the regulated-source instrument-data application — software that collects continuous measurements from stack/vent monitoring instruments, converts them into legally defined emission quantities, evaluates them against permit limits, and retains/reports them as compliance records. In the market this software is most often called a **DAS (Data Acquisition System)** or **DAHS (Data Acquisition and Handling System)** and is legally considered part of the CEMS.
- Adjacent types suspected: Air Quality Monitoring (ambient/duct networks), Carbon Accounting Platform (activity × factor), SCADA / Industrial Historian (process channels without compliance semantics), EHS/HSE Platform (program/corrective-action-centric), Environmental Monitoring Platform (broad multi-media).
- Open question: does the Type's core include the QA/QC test machinery (calibration checks, drift tests, RATA/QAL3) or is it optional? Does limit evaluation belong to the definition or is a recorder without limits still "CEMS"?

## Research Questions

1. What is the anchor record — source? stack? parameter?
2. How does instrument data flow in (protocols, data controllers, loggers)?
3. What calculations turn raw signals into emission values (corrections, reference conditions, averaging)?
4. How do validity/QA rules work (calibration checks, out-of-control status, substitution) in US Part 75 vs EU EN 14181/QAL regimes?
5. How are limits configured and exceedances handled?
6. What reports are produced and for whom (regulator formats)?
7. Who are the users (operator, environmental engineer, technician) and what surfaces do they use?
8. Does the same software span ambient air monitoring and source monitoring (shared DAHS machinery)?
9. Is PEMS (predicted emissions) a variant of this Type?

## Representative Products (sampled)

| Product | Vendor | Pole represented |
|---|---|---|
| StackVision / Prism / QAInsight | ESC Spectrum (now Alliance Technical Group), US | US pure-play DAS ecosystem, Part 75/60 deep compliance; "created by technicians for technicians" (Prism) |
| D-EMS 2020 | DURAG GROUP / DURAG DATA SYSTEMS, Germany | European instrument-group DAHS; TÜV EN 17255 certified; spans EU + US regulation |
| eSam (+ XR suite) | ENVEA, France | Shared DAHS for environmental monitoring (emissions + ambient AQMS); acquisition/validation layer |
| CEMS II e + Calcmet | Gasmet, Finland | Instrument-maker's analyzer-centric CEMS; FTIR multi-gas; analyzer software feeding compliance data |

Attempted but unreachable: Envirocare "EmiSec" (UK CEMS software) — domain guess failed, search engines localized/blocked; SICK MEAC3000-NA — not directly located. Recorded as source-access limitation; EU pole covered by DURAG/ENVEA/Gasmet.

## Sources

- ESC Spectrum (escspectrum.com): root site; StackVision page (alliancetg.com mirror); Prism page; QAInsight page; blog "Air Emissions Calibration Testing: Staying Compliant With Daily and Quarterly Requirements" (2025-07-09). Fetched 2026-09-08.
- DURAG GROUP (durag.com): "Emission and raw gas" solution page; D-EMS 2020 product page (features, certifications, conformities, technical data). Fetched 2026-09-08.
- ENVEA (envea.global): root; find-your-solution index; eSam product page. Fetched 2026-09-08.
- Gasmet (gasmet.com): root; CEMS II e product page; Calcmet software page. Fetched 2026-09-08.
- EPA pages attempted (epa.gov/power-sector/continuous-emission-monitoring-systems-cems → 404; epa.gov/power-sector/ecmps → 404). Official regulator context NOT directly fetched; regulatory machinery is evidenced through vendor documentation instead. Assertion strength on US/EU regulatory specifics is calibrated accordingly.

## Product Observations

### ESC Spectrum — StackVision (DAS) [Evidence layer A]

- "The #1 DAS in the U.S. More than 3,100 air emission sources rely on StackVision for continuous emissions monitoring and reporting." (vendor claim)
- "security-enabled users direct control over configurations, exceedance limits, alarms, and monitoring parameters, without programming knowledge or outside support" — limit/alarm configuration is a user-facing, in-product capability.
- "customizable dashboards… single source or managing a fleet… alerts that fire when conditions are met or exceeded."
- "review, query, and configure data… When adjustments are made, dependent calculations update automatically, so your records stay consistent from the source forward." — data-adjustment workflow with propagation.
- "supports the full cycle of QA and certification testing from running linearity checks and relative accuracy test audits to generating the reports regulators expect" — QA test execution + records.
- "compile and deliver accurate CEMS, CPMS, and COMS reports to the relevant state and federal agencies"; "supports ECMPS 2.0, producing required JSON outputs" — regulator-format reporting machinery (US).
- Flare GC case study: automated data feeds from analyzers, daily calibration reports, weekly trend data, immediate pass/fail notifications via text alerts, remote access for calibrations and cylinder gas audits.
- Video description: "A DAS is a set of tools for continuously collecting and validating your emissions data for air compliance reporting."

### ESC Spectrum — Prism (DAS) [A]

- "capture, analyze, calculate, and report emissions data for federal, state and local environmental compliance"; "scalable DAS software… stand-alone and enterprise environments."
- Works with the 8864 Data Controller (hardware) to "collect, monitor, QA, and report on emissions data from continuous monitoring systems."
- Observed panels: Overview (real-time conditions, logs, readings); Alarms panel "filtered by alarm type"; Bottle Manager (calibration-gas accuracy measurement); Calibration progress/status dashboard; Trends dashboard (user-configurable charts); day logs; calibrations; deviations reporting ("Reporting your continuous monitoring data and deviations is a critical obligation").
- "created by technicians for technicians."

### ESC Spectrum — QAInsight (companion QA tracking) [A]

- Single source for QA test data; replaces spreadsheets; schedules/plans/tracks QA tests; color-coded role-based dashboard (overdue/due windows); email notifications.
- Imports QA test completion dates, operating data, Recertification Event deadlines from StackVision.
- Imported test types: Calibration Gas Audits, Opacity Test Audits, Linearity, RATA, Permit RATA, Leak Check, Flowmeter Accuracy, Transmitter/Transducer, Primary Element Inspection.
- "over 30 pre-built workflows" organized per regulation: Part 75 (EDR, RATA, Appendix D, Linearity, Normal and 3 Load RATA, Leak Checks, NOx Correlation Test), Part 60 (RATA, Cylinder Gas Audit, Opacity), Certification Event Tests.
- Interpretation: QA-test program management exists both inside DAS products and as a companion product — common capability, packaging varies.

### ESC Spectrum — calibration blog (educational, US Part 60/75 framing) [A, single source for numeric details]

- Daily calibration error tests (zero/span), 7-day calibration drift tests, cycle/response time tests, probationary calibrations, offline calibrations with defined validity windows ("26 clock hours" / "26 unit operating hours" — precise numbers from this single vendor blog, NOT promoted to the final document).
- "When calibration errors exceed EPA-specified limits, data from that monitor becomes Out-of-Control (OOC). This status remains until a successful retest is completed." — OOC/validity status as a first-class data state.
- "Results must be recorded in your Quarterly EDR" — periodic electronic data report.
- "Automating calibration testing with a Data Acquisition System (DAS)… reduces manual effort, tracks OOC events."

### DURAG GROUP — D-EMS 2020 (DAHS) [A]

- Definition: "Data acquisition and handling system (DAHS) for the acquisition, calculation, long-term storage and visualization of data… Compliant with European and US EPA-based regulations." — the four-verb DAHS definition.
- Features: analog and digital data acquisition "with long-term data storage in accordance with legal requirements"; provision of data to customer systems via analog and digital interfaces; presentation of "current, historical or forecast measurement data as bar or line chart"; standalone and client-server architecture; role-based user management incl. LDAP(S); "additional modules such as GHG, QAL3, automatic backup".
- Certifications/conformities: TÜV certified EN 17255 parts 1–3; MCERTS; German conformities (TA Luft, multiple BImSchV, BEP 2023, SKK 2019, DIN EN 14181, VDI 4201/4204); EU (IED 2010/75/EU, MCP directive (EU) 2015/2193, EN 14181, EN 17255); US (40 CFR Part 60, Part 63, Part 75).
- Technical data: up to 1024/2048 analog inputs/outputs per server; interfaces 4-20mA, Modbus RTU/TCP, Profibus DP/Master (VDI 4201), Profinet, OPC UA, Mode 4, Ethernet IP; export PDF/XLS/XML/CSV; data buffer in D-MS 500 FC loggers with ring memory "up to 128 days"; encrypted communication; encrypted password-protected SQL database; alarm notification on storage-medium failure; reporting "daily, monthly, quarterly, yearly, etc."; "Alarm and event management with comment functionality and e-mail notification."
- Solution-page context: "Operators of industrial plants emitting air pollutants are obliged to measure their emissions. Limit values… have to be adhered to and monitored… the results of their monitoring have to be passed on to the competent authorities." Products "suitability-tested and certified for official emission monitoring."

### DURAG GROUP — DATACEMS (PEMS) [A, single product]

- "Software-based PEMS for continuous real-time monitoring of pollutants such as NOX, SO2, CO, HC or reference variables such as O2." — predictive emission monitoring: same outputs, model-inferred instead of instrument-measured. Recorded as a variant pole.

### ENVEA — eSam (DAHS) + XR suite [A]

- "Data acquisition and management system… handling all parameters: gas analysers, dust monitors, meteorological and temperature sensors."
- "remote, bi-directional access and control of analyzers and the EMS via a WEB based interface"; transmission to a central server running the XR software suite "able to handle thousands of AQMS stations in a town, city or region."
- Features: "data retrieval, data storage, visualisation, supervision"; "automatic prevalidation of the data"; "automatic calibration and instrument control"; web dashboard; MQTT; local database.
- Technical: acquisition at configurable frequency "from 5 seconds to 24 hours"; management of metrological context (analyser parameters, internal failures, technical measurements, external signals e.g. door opened, flow); "controls of lower and higher validity limits, sensitivity threshold, immobility, slope and follow-up of peak episodes"; automatic validation with quality code per value; quality indicators (min, max, standard deviation, over-threshold counts, availability ratio); calibration sessions with 5 span points, linearization adaptation, drift controls (absolute, relative, between span points), storage of calibration information.
- Note: main application listed as "Air quality monitoring stations: fixed or mobile" — the acquisition/validation machinery is shared between ambient networks and emission monitoring; the emission-specific layer (limit evaluation, regulatory calculation, compliance reporting) is what differentiates the source-monitoring use. Boundary-relevant.

### Gasmet — CEMS II e + Calcmet [A]

- Definition (Gasmet): "A CEMS is a permanently installed system that monitors key emission compounds, such as CO, CO₂, NOₓ, SO₂, HCl, and VOCs, directly from the stack, providing real-time data for compliance reporting and process control."
- Certified TÜV and MCERTS (QAL1); "certainty in passing regulatory QAL2, QAL3 and AST tests"; EN 15267.
- System components: FTIR analyzer, cabinet, sampling system, industrial computer, heated sample probe/line; options for ZrO2 oxygen analyzer, FID for TOC.
- Calcmet software: "collects, stores, and visualizes the FTIR spectrum of the sample gas and analyzes the concentrations of gas components"; re-analysis of stored spectra; "simultaneous detection, identification, and quantification of up to 50 different gas components"; cross-interference compensation.
- Integration: "typical inputs include analog signals and digital inputs from e.g. stack temperature and pressure sensors, flow measurement devices and particulate matter analyzers. Typical outputs include relay outputs…, outputs of measured concentrations, and serial Modbus output consolidating both measured concentrations and binary alarm/status signals."
- Reference-condition handling: "the water content of the sample gas is continuously measured… results can be reported on either a 'wet' or 'dry' basis. The results can also be compensated for the correct oxygen levels."
- "Both measuring data and alarm information can be transferred to other automation or reporting systems in analog or digital format."
- Insight digital solution: "secure and centralized 24/7 remote access to real-time data."

## Cross-product Comparison

| Dimension | StackVision/Prism (US) | D-EMS 2020 (DE) | eSam (FR) | CEMS II e/Calcmet (FI) |
|---|---|---|---|---|
| Anchor object | monitoring system / source (CEMS, CPMS, COMS) | emission data per plant area, source-driven | parameters from analysers/sensors (shared with AQMS) | analyser + stack measurement point |
| Acquisition | continuous from CEMS via data controller | analog/digital, logger buffer, client-server | configurable 5 s–24 h, serial/analog/digital, MQTT | analyzer-internal + analog/digital I/O, Modbus |
| Calculation layer | dependent calculations auto-update; deviation reporting | "calculation" named in DAHS definition; modules | prevalidation + quality codes; validity limits | concentration analysis; wet/dry; O₂ compensation |
| Limit evaluation | user-configurable exceedance limits + alarms | limit-value monitoring (regulatory framing) | validity limits, over-thresholds (validation-leaning) | alarm/status signals out |
| QA machinery | linearity, RATA, cal tests; QAInsight tracking; OOC state | QAL3 module; certification via EN 17255/EN 14181 | calibration sessions, drift controls, linearization | QAL1/2/3, AST; zero/span culture of FTIR |
| Records & reports | EDR / ECMPS 2.0 JSON; state/federal reports | long-term storage per legal requirements; periodic reports; PDF/XLS/XML/CSV | storage + supervision + central XR platform | data storage + transfer to reporting systems |
| Regime packaging | US Part 60/63/75 | EU (IED, EN 14181, national) + US parts | regime-neutral acquisition layer | EU QAL/MCERTS-centric |
| Deployment | Windows/SQL Server, stand-alone→enterprise | standalone or client-server; loggers + server | rack/desktop/fanless chassis; web | analyzer cabinet + external computer; cloud access optional |

Stable commonalities (observed in all/most sampled products):
1. Continuous acquisition from monitoring instruments at identified industrial emission points.
2. A calculation/validation layer turning raw signals into emission values under configured rules.
3. Limit/exceedance (or at minimum validity-threshold) evaluation with alarms/events.
4. Long-term, integrity-conscious storage "in accordance with legal requirements."
5. Periodic reports; in mature products, regulator-oriented structured outputs.
6. Calibration/QA cycles as a standing operational rhythm.
7. Real-time visualization + historical trends + configurable dashboards.
8. Interfacing outward (data to plant systems; SCADA/automation via Modbus/OPC/4-20mA).

## Abstraction Levels

### L0 — Defining Invariant (jointly-held)

1. **Identified monitored emission source(s)** — persistent record(s) for the regulated emission points (stack, vent, duct, flare) of an operating industrial facility, carrying the monitored parameters and the limits that apply. Remove → generic process historian/data logger.
2. **Continuous measurement acquisition** — the system continuously collects signals from monitoring instruments at those sources (concentration, flow, opacity, moisture, supporting process inputs) over the whole operating period, not periodic/manual entries. Remove → periodic stack-testing campaign tool / manual records.
3. **Prescribed transformation into emission quantities** — raw instrument data is converted under configured, regulation-shaped rules into defensible emission values (calibration/drift correction, unit conversion, dilution/moisture handling, reference-condition normalization such as O₂ basis, emission rates, defined averaging). Remove → raw signal logger.
4. **Limit evaluation + compliance record** — values are continuously evaluated against configured limits producing recorded exceedance/alarm events, and the resulting emissions record is retained with integrity (audit-conscious storage, event history, validity context) so it can support regulatory reporting. Remove (limits) → historian; remove (retained record) → real-time dashboard.

### L1 — Common Mature Structure

- Multi-source / fleet visibility with roll-up dashboards (single source → enterprise).
- QA/QC machinery: daily calibration checks, drift tests, certification test execution (linearity, RATA in US; QAL2/QAL3/AST-family in EU) with test records; sometimes as a companion scheduling/tracking product.
- Data review & adjustment workbench with propagation ("dependent calculations update"), quality/validity codes, per-regime invalidation and substitution rules.
- Alarm/event management with comments, filtering, notification (email/text).
- Periodic report generation (daily/monthly/quarterly/yearly) and export formats; structured regulator submissions (US: EDR/ECMPS; EU: EN 14181-aligned reporting) as the market-realized form.
- Real-time trends, historical charts, configurable dashboards.
- Outward integration (plant automation, corporate systems) via standard industrial protocols.
- Role-based user management; encrypted storage; local data buffering at the logger/controller.

### L2 — Variant / Optional Structure

- Regulatory regime packaging: US (Parts 60/63/75, ECMPS 2.0) vs EU (IED, EN 14181, EN 17255, MCERTS, QAL1–3, national schemes) vs others; regime is the largest packaging axis.
- Measurement basis: instrument-measured (CEMS) vs software-predicted (PEMS — one sampled product) vs hybrid.
- Packaging: standalone DAS software; instrument-maker bundle (analyzer + its software); DAHS shared across ambient+emissions; companion products for QA scheduling / reporting.
- Deployment: data-controller + local server; client-server enterprise; web/remote cloud access; logger ring-buffer hybrid.
- Source/scope breadth: combustion stacks; flares; process vents; mercury and dioxin systems; adjacent fenceline/ambient offerings from the same vendor.
- Industry tuning: power generation, waste incineration/WtE, cement, refining/petrochemical, glass, pulp & paper, universities/medical centers.
- Remote diagnostics / predictive maintenance services layered on the data.

### L3 — Vendor-specific (kept out of final document)

- StackVision 3,100+ sources claim; ECMPS 2.0 JSON specifics; 8864 Data Controller; Bottle Manager; DASProtect; QAInsight's 30+ workflows and color-coding rules; Prism day logs.
- D-EMS 2020: EN 17255 TÜV certificate numbers; 1024/2048 I/O counts; 128-day ring memory; D-MS 500 FC loggers; German BImSchV list; GHG/QAL3 module names.
- eSam: 5 s–24 h acquisition range; MQTT; XR suite station counts; 5-span-point calibration sessions.
- Gasmet: 50-gas FTIR library; 98.4% availability; 6-month maintenance interval; Insight.
- Numeric calibration windows (26-hour rules etc.) from ESC's blog — single-source precision, research-only.

## Vendor-specific Findings (detail)

- ESC Spectrum ecosystem sells services around the DAS (regulatory & reporting services, engineering, IT, 24/7 support) — evidence that the DAS is operationally load-bearing and staffed continuously; kept out of the Type definition.
- DURAG positions the DAHS as one node in an instrument group; ENVEA positions the DAHS as regime-neutral across AQMS and emissions; Gasmet positions analyzer software as the compliance data source. These are three packaging philosophies over one shared machinery.
- Alliances/acquisitions (Alliance Technical Group acquiring ESC Spectrum 2025) confirm a consolidating specialist market — market context only.

## Boundary Findings

- **vs Air Quality Monitoring (§21, processed)**: air-quality-monitoring's core = monitoring points + pollutant time series + presentation; CEMS's core adds the regulated-source semantics: source-bound permit limits, reference-condition normalization, validity/QA machinery, compliance records and regulator reporting. eSam shows the acquisition/validation machinery can literally be the same software spanning both domains — the seam is the unit of accountability (permitted industrial source vs ambient site) and the compliance transformation. The air-quality pass held duct/source monitoring as a Variant — flag for joint review: source-monitoring-without-compliance-semantics may straddle the seam.
- **vs Carbon Accounting Platform (§21, processed)**: activity × factor computation over organizational activity data vs physical continuous measurement at regulated sources. Complementary; D-EMS's GHG module shows CEMS data feeding GHG reporting. DISCHARGES the carbon-accounting pass's flag from this side: the two Types do not converge.
- **vs SCADA / DCS / Industrial Historian (§16)**: control systems own process control and store channels; the CEMS application owns emissions-specific calculation, validity, limits and regulatory records. Interfaces are tight (Modbus/OPC feeds), semantics differ. Not the same Type; also note DCS/SCADA leaves are unprocessed — no conflict observed.
- **vs EHS/HSE Platform (§21, processed)**: EHS is program/corrective-action-centric over organization-wide occurrences; CEMS is instrument-data-centric over monitored sources. An EHS platform may consume emissions summaries; it does not run the monitoring system.
- **vs Environmental Monitoring Platform (§21, unprocessed)**: expect that leaf to name the broader multi-media category; CEMS is the regulated-source instrument specialist within it.
- **vs source/stack testing services (periodic reference-method campaigns)**: campaign-based manual testing is a different workflow; CEMS QA tests (RATA) formally connect the two but the Type is the continuous system.
- **PEMS**: software-predicted emissions substitute instruments; sampled once (DATACEMS). Held as a variant of this Type (same objects, same outputs), not a separate Type — single-product basis, flagged as unverified generalization.
- **Remove-tests**: remove limits/alarm evaluation → industrial historian; remove continuous acquisition → stack-test/periodic-reporting tool; remove compliance record/reporting → process dashboard; remove source anchor (channels only) → data logger. Each removal lands in a different Type.

## Historical / Market-Sample Check (§24-style)

- US CEMS practice dates to 1970s performance specifications and the 1990 Acid Rain Program, which drove purpose-built DAS software; ESC claims 50+ years of lineage. A 1990s-era DAS (acquisition → calculation per permit formulas → limit alarms → quarterly electronic/paper reports) satisfies the L0 as written — no cloud, no JSON, no fleet dashboards needed.
- Earlier still, strip-chart recorders plus manual transcription satisfied the *system* (CEMS) but not the *software* Type; the software Type begins when the acquisition/handling becomes software. L0 as framed requires continuous acquisition and a retained record — a chart recorder is the analog ancestor, not a counterexample.
- Older EU practice (EN 14181 / national ordinances) fits: DAHS terminology itself comes from European standards; DURAG's conformities span decades of German BImSchV regimes. No era-specific technology (cloud, AI, JSON) is in L0. Historical check passes.

## Uncertainties

- EPA official documentation not fetched (404s); US regulatory machinery rests on vendor documentation (multiple vendors agree on Parts 60/63/75 + ECMPS, so cross-product strength B, but no primary regulator source).
- Envirocare (UK) unreachable — the UK MCERTS pure-play pole under-sampled; DURAG's MCERTS certificate partially covers it.
- QAInsight shows QA-test scheduling may be packaged separately; whether the Type's definition should include QA scheduling is a packaging question — held as common capability, not definitional.
- PEMS held as variant on a single product.
- Precise numeric regulatory windows deliberately excluded from the final document (single-source precision).
- eSam's datasheet is a PDF (not fetched); observations from the product page only.

## Final Synthesis

The Application Type is the **data-handling heart of continuous emissions monitoring**: software bound to identified, regulated industrial emission sources that (1) continuously acquires measurements from the monitoring instruments at those sources, (2) transforms raw signals into defensible emission values under prescribed, configured calculation and validation rules, and (3) evaluates those values against configured limits, recording exceedances and retaining the whole as an integrity-conscious compliance record that feeds regulator-facing reports. Around that defining core, mature products add fleet visibility, QA-test machinery, alarm/event workflows, reporting engines, industrial integrations, and remote access; regimes (US Part 75 vs EU EN 14181/QAL), deployment shapes, and packaging (standalone DAS vs instrument bundle vs shared DAHS) are variants. The market name for this software is DAS/DAHS; the leaf name "Emissions Monitoring / CEMS" names the system of which this software is the legally required data core.
