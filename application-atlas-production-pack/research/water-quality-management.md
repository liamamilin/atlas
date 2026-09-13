# Research Notes — Water Quality Management

## Research Goal

Understand what "Water Quality Management" is as an Application Type: what system a water utility runs to manage the quality of the drinking water it delivers — what objects live inside it (sampling locations, monitoring schedules, lab results, standards/limits, compliance determinations, reports), what work flows through it (plan → sample → validate → evaluate → report → respond), who uses it, and where its boundaries lie against the processed water family (water-network-monitoring §19, wastewater-compliance-management §21, wastewater-utility-management §19, environmental-laboratory-management §22, environmental-data-platform §21, environmental-compliance-management §21, environmental-permit-management §21) and the unprocessed siblings (water-utility-management §19, environmental-water-monitoring §21).

This pass must also discharge the **naming-collision watch** inherited from wastewater-compliance-management: the market label "water quality management" is used for (a) discharger-side compliance products (Intelex WQM — NPDES/WSER/MCERTS), (b) ambient water-quality monitoring, and (c) the water utility's drinking-water quality program. A center-of-gravity test must decide what this §19 leaf is.

## Prior-Pass Context (inherited seams this pass must honor or discharge)

1. **water-network-monitoring (§19, processed 2026-09-10)** — forward seam: "the operational real-time quality signal inside the network condition (chlorine/turbidity events) belongs to that leaf's condition; the quality-assurance/compliance program (sampling plans, drinking-water standards reporting) is expected to be this leaf's center." Must be honored/discharged from this side.
2. **wastewater-compliance-management (§21, processed 2026-09-10)** — naming-collision watch (above) + the established compliance-monitoring grammar (regulated source + monitoring data estate + limit evaluation + regulator-facing record). This leaf is expected to be the drinking-water twin of that grammar. Its L2 already noted "Drinking-water twin (same products serve drinking-water compliance — WaterTrax, Locus)".
3. **environmental-laboratory-management (§22, processed)** — "utility-side water-quality program vs the laboratory that analyzes the samples; producer/consumer seam again."
4. **wastewater-utility-management (§19, processed 2026-09-10)** — utility business system (customers/billing/service) vs quality program; no object overlap expected.
5. **environmental-water-monitoring (§21, unprocessed — 2026-09-08 run failed)** — receiving waters vs the utility's own water; flag stands for that pass.
6. **pool-service-management (§26, processed)** — recorded that "Water Quality Management" is a different domain entirely from consumer pool water care.

## Initial Boundary (hypothesis before research)

- Core purpose hypothesis: the water utility's (public water system's) system of record for its drinking-water quality program — compliance monitoring locations and schedules, lab/field data, evaluation against drinking-water standards, exceedance handling, and regulator/consumer-facing reporting.
- Likely users: water quality administrators/compliance managers, lab and sampling staff, plant operators, utility leadership.
- Nearest neighbors: water-network-monitoring (live network condition), wastewater-compliance-management (effluent twin), environmental-water-monitoring (ambient waters), environmental-laboratory-management (lab side), water-utility-management (business system).
- Unknowns: the center of gravity of the market label; whether operational quality management (residual control, process data) belongs here or to network monitoring; whether backflow/cross-connection control belongs here; how much of the market realizes this as a standalone Type vs suite modules.

## Research Questions

1. What is the central object — the sampling/monitoring location? What does it carry (parameters, standards, schedule)?
2. What data does the system hold — lab sample results, field readings, instrument/SCADA feeds? How does data enter?
3. How are standards evaluated — MCL comparison, averaging (LRAA-class), exceedance detection? What happens on exceedance (alerts, corrective action, notification duties)?
4. What reporting artifacts — monthly operating reports, consumer confidence reports, electronic state/EPA submissions (CMDP-class)?
5. What supporting machinery — sampling schedules/reminders, chain of custody, data validation/audit trail, bench sheets, dashboards/GIS?
6. Who uses it, and at which customer tiers?
7. Where does the operational real-time quality signal (online analyzers) belong — here or in network monitoring?
8. Do companion programs (backflow/cross-connection control, pretreatment) belong to this Type?
9. Where are the boundaries vs the sibling Types listed above?

## Representative Products

| Product | Vendor | Pole | Customer tier | Why sampled |
|---|---|---|---|---|
| WaterTrax + Hach WIMS / WIMS Rio | Aquatic Informatics (Veralto) | water-sector specialist (compliance + operations data management for water utilities) | municipal utilities & agencies, small–large | the clearest specialist family; serves drinking water AND wastewater — the twin-product evidence |
| Locus Drinking Water Quality (Locus Water) | Locus Technologies | environmental-data-platform app | smallest township → largest investor-owned utility | names the full SDWA compliance cycle, CCR/MOR generation, LIMS EDD, MCL tracking |
| SAMS Water | NJBSoft | pure-play SDWA compliance automation | municipal + investor-owned utilities (SAWS, LADWP, Phoenix, Seattle, Veolia-class) | literally titles itself "Water Quality Management Software for Regulatory Compliance"; built-in rule packs, CMDP submissions, bench sheets/LRAA |
| Water Quality Management | Intelex | EHS-suite module | enterprise industrial dischargers | the naming-collision specimen: same label, discharger-side sense (NPDES/WSER/MCERTS) — boundary evidence, not a Type member |

Regulatory substrate (not products, but the regime the software serves): US EPA SDWA compliance monitoring (PWSS/primacy agencies), Public Notification Rule, EPA CMDP electronic compliance-data portal (via Arizona ADEQ), EPA OWQM-DS online-monitoring guidance.

## Sources

Fetched directly (research date 2026-09-10):

- Locus Technologies — Water Data Management: https://www.locustec.com/applications/water-data-management (fetched OK)
- Locus Technologies — Drinking Water Quality: https://www.locustec.com/applications/environmental-information-management/drinking-water-quality/ (fetched OK)
- Aquatic Informatics — Drinking Water solution: https://aquaticinformatics.com/solutions/applications/drinking-water-data-management/ (fetched OK)
- Aquatic Informatics — WIMS Rio product: https://aquaticinformatics.com/products/water-compliance-operations-solution-rio/ (fetched OK)
- NJBSoft — SAMS Water: https://njbsoft.com/sams-water/ (fetched OK)
- US EPA — Public Notification Rule: https://www.epa.gov/dwreginfo/public-notification-rule (fetched OK)
- US EPA — SDWA Compliance Monitoring: https://www.epa.gov/compliance/safe-drinking-water-act-compliance-monitoring (search excerpt)
- Arizona ADEQ — CMDP Compliance Monitoring Data Portal: https://azdeq.gov/CMDP (search excerpt)
- US EPA — Online Water Quality Monitoring Resources / OWQM-DS guidance: https://www.epa.gov/waterresilience/online-water-quality-monitoring-resources (search excerpt)
- Intelex — Water Quality Management Software: https://www.intelex.com/products/applications/water-quality-management-software (search excerpt; full Layer A fetch in research/wastewater-compliance-management.md, 2026-09-10)

Inherited Layer A evidence (fetched in the wastewater-compliance-management pass, 2026-09-10):

- Aquatic Informatics — WaterTrax product page: https://aquaticinformatics.com/products/wastewater-compliance-software/
- Aquatic Informatics — Hach WIMS product page: https://aquaticinformatics.com/products/water-information-management-solution-wims/
- Cority — Water Management Software (search-index excerpt only)

Unreachable / dropped:

- Aquatic Informatics drinking-water product URL guess (…/water-quality-compliance-software/) → 404; the Drinking Water solution page covers the sense. One failure, dropped per network rule.
- No Tier-1 help-center/user-manual documentation reachable for any sampled product; all product evidence is product/solution-page level (Tier 2). Precise operational parameters (exact averaging windows per rule, exact report formats, numeric thresholds) are therefore NOT asserted in the final document.
- SUEZ/Xylem operational-quality products not fetched this pass: the operational-quality seam is already ratified from the water-network-monitoring pass with first-hand vendor evidence; no claim here depends on them.

## Product Observations

### Aquatic Informatics — WaterTrax / Hach WIMS / WIMS Rio (Layer A; Rio + Drinking Water solution fetched this pass, WaterTrax/WIMS inherited)

- Drinking Water solution page: "monitor the health of infrastructure and water resources to proactively preserve potable water from contamination"; "diligent maintenance, testing, sampling, and continuous monitoring"; "managing the intricacies and details of all system assets, events, and **monitoring locations**".
- "Ensuring accurate data for **defensible compliance** — reviewing the quality of data being collected and trusting what's being reported to the EPA or local regulators to reduce risk and liability."
- "automatic data validation, custom alerts triggered from changes in water quality, and preservation of historic and corrected data for trend analysis and audits."
- South Bend Utilities (Director of Water Quality and Laboratory): "South Bend's next review for **lead and copper testing**… Results from around the **distribution system** will be entered into WaterTrax directly from the labs and this data will then be easy for us to access, map, and **report to ensure compliance**."
- "Built-in templates for regional or federal regulators allow for automated report generation"; customizable dashboards.
- Riverside Public Utilities quote (inherited): "combining information from SCADA, UWAM, and WaterTrax gives us the big picture" — SCADA and WaterTrax are separate systems.
- WIMS Rio: "Regulatory Compliance & Operational Data Management for Drinking Water & Wastewater"; "centralize daily workflows for drinking water and wastewater utilities of any size"; central secure database integrating "lab, process, field, and other data sources"; mobile app for remote data collection + validation; "Track critical metrics, visualize trends, produce regulatory reports (NetDMR, MORs, etc), and use customizable alerts"; "historical records with defensible audit trails."
- WaterTrax (inherited): "helps agencies and utilities monitor and manage their water and wastewater compliance data"; exceedance alerts, automated sampling events, automatic lab data transfers; "Defensible data to produce reliable, accurate reports for regulatory requirements… with a click-of-a-button."

### Locus Technologies — Drinking Water Quality / Locus Water (Layer A, fetched)

- Water Data Management page: "Our clients manage water volume, backflow devices, DMR deadlines, and **CCRs** from one platform"; "Locus Water manages **drinking water quality**, backflow, pretreatment, stormwater, metrics, and more — all on the same cloud platform."
- "Locus Drinking Water Compliance software **automates the full SDWA compliance cycle**, from **sample planning** and field collection to **lab data validation, MCL tracking, and regulatory report generation**. Build monitoring schedules for **TCR, Lead and Copper, DBPs, Radionuclides, VOCs, PFAS**, and all other regulated contaminants. Generate **Consumer Confidence Reports (CCRs) and Monthly Operating Reports (MORs)** with a single click. Connect directly to your **LIMS** for automatic EDD loading, **flag out-of-range results in real time**, and maintain **audit-ready records for state and EPA review**. From the smallest township to the largest investor-owned utility…"
- Drinking Water Quality page: "drinking water quality management software saves you time and resources on your scheduled data collection, tracking, and reporting"; Sample Planning: "Plan and schedule sampling and configure notifications for **late or missing samples or exceedances** or pre-defined limits"; CCR: "Streamline Consumer Confidence Reports (CCR) and routine **chlorine and coliform reporting**"; Quality Control: "Manage field equipment and keep up with QC calibrations with the asset tracker app"; SCADA integration; mobile app.
- Companion apps on the same platform: Backflow Prevention ("centralizes customer records, test results, and installation and inspection schedules… automates notifications… compliance enforcement letters… certified testers"), Industrial Pretreatment, Stormwater Inspections, Customer Complaints ("taste, odor, illness, color" types), Test Equipment Management, Watershed Maintenance.
- Case study named: San Jose Water Company — "automates, optimizes drinking water quality management compliance data."

### NJBSoft — SAMS Water (Layer A, fetched)

- Title: "**Water Quality Management Software for Regulatory Compliance**… Confidence in Every Drop"; "No more chasing spreadsheets or worrying about what you missed."
- "SAMS water quality management software **automatically applies built-in rules for TCR, Lead and Copper, DDBP, Radionuclides, VOCs, SOCs**, and more. With the flexibility to add custom rules tailored to your system."
- "**Chain of Custody Tracking** — QR code–enabled audit trails record each step from collection to upload."
- "**Bench Sheets & Data Management** — smart bench sheets that instantly compute averages, min/max, and **locational running annual averages**."
- "**LIMS Integration** — automatically processing results and generating reports with a single click."
- "**SCADA Integration** — connect safely… via secure APIs or file transfers, gaining real-time visibility into treatment processes **without exposing control systems**."
- "**Electronic Reporting & Submissions** — Automate submissions to **state systems like CMDP**. SAMS tracks deadlines and supports API and XML integration."
- "**Permit Management** — Manage all permits in one place… triggers, and required actions."
- AI/ML: "detect anomalies, **flag missing samples**, and identify trends."
- FAQ: "SAMS Water is a comprehensive water compliance software that simplifies all aspects of **SDWA compliance**… Generate essential water quality reporting like **lead and copper reports, MRDL reports, DBP reports, chlorine reports, and MORs**."
- FAQ: laboratory compliance workflow — "sample scheduling, result entry, **MCL comparison, exceedance alerts, and state-formatted compliance report generation**… automatically cross-referenced against applicable regulatory limits under SDWA."
- FAQ: "goes beyond compliance to support utility operations management… mobile field data collection, operations reports, preventive maintenance tracking."
- Customers: San Antonio Water System, LADWP, City of Phoenix, City of Seattle, Veolia, Aqua, Golden State Water, Honolulu, Mesa, Glendale-class Arizona cities.
- Sibling products: SAMS Wastewater, SAMS Cross Connection, SAMS IPP, SAMS FOG, SAMS Stormwater, SAMS Air Quality, SAMS Asset Management.

### Intelex — Water Quality Management (Layer A via wastewater pass + search excerpt; collision specimen)

- "centralizes, manages and meets all global water quality-related **compliance obligations**… meet **NPDES (US), WSER (Canada), MCERTs (UK)**"; permit limits "for every **point source**"; sample collection + chain of custody; DMR generation; LIMS integration; load calculation engine.
- Reading: identical label, but the subject is the **discharger's effluent** under discharge permits — the wastewater-compliance-management Type's territory, already sampled there. Not a member of this leaf's center.

### Regulatory substrate (Layer A — regulator documents)

- **SDWA compliance monitoring (EPA)**: "Public water systems must meet health-based federal standards for contaminants, including performing regular monitoring and reporting." "EPA and primacy agencies monitor public water system compliance with the SDWA… by reviewing and evaluating **analytical results of water samples collected and reported by public water systems**." Primacy agencies (states with EPA approval) implement the program; PWS serve ~90% of the public; ≥15 connections or 25 persons.
- **Public Notification Rule (EPA)**: systems must notify customers when they violate drinking water regulations "**including monitoring requirements**" or provide water that may pose risk; three tiers of escalating urgency (immediate for acute risk → annual, consolidated with the Consumer Confidence Report); notices carry required elements (violation description, health effects language, corrective actions, contact…). "Water systems test regularly for approximately 90 contaminants."
- **CMDP (EPA portal, via Arizona ADEQ)**: states require PWS to submit water quality compliance data through EPA's Compliance Monitoring Data Portal; per-rule result categories (IOCs, LCR, PFAS, RTCR, DBP, VOCs, SOCs, radionuclides…); "Accurate **Chain of Custody** forms ensure timely results… The correct public water system name, ID, and **sampling location**"; systems must notify the agency of total coliform-positive samples; state SDWIS/Drinking Water Watch publishes results.
- **OWQM-DS (EPA guidance)**: online water quality monitoring in distribution systems is a **surveillance/response practice** — monitoring locations, event detection, support for "chlorine residual management and corrosion control" — distinct from "regulatory compliance data" records, which it lists as a separate information category.

## Cross-product Comparison

| Dimension | WaterTrax / WIMS / Rio | Locus Drinking Water | SAMS Water | Intelex WQM (collision) |
|---|---|---|---|---|
| Central subject | water/wastewater compliance + operations data for utilities | drinking-water quality program (SDWA cycle) | SDWA compliance program | discharge compliance obligations per location |
| Monitoring location identity | ✔ "monitoring locations" around the distribution system | ✔ sample planning per location | ✔ sampling locations + GIS | point sources (outfalls) |
| Standards/limits held | implied (alerts vs compliance) | ✔ MCL tracking | ✔ built-in rule packs (TCR, LCR, DBP…) + MCL comparison | ✔ permit limits per point source |
| Monitoring data estate | ✔ central secure DB (lab/process/field) | ✔ lab EDD + field + SCADA | ✔ lab results + field + bench sheets | ✔ sample results via LIMS |
| Data acquisition | lab transfers, SCADA, mobile | LIMS EDD, mobile, SCADA | LIMS, mobile (offline), SCADA (read-only) | LIMS flat files |
| Schedule machinery | ✔ automated sampling events | ✔ sample planning + late/missing notifications | ✔ automated per-rule sampling + missing-sample flags | ✔ scheduled collection + escalations |
| Chain of custody | implied (defensibility) | implied (audit-ready) | ✔ QR-code CoC audit trail | ✔ CoC generation |
| Validation / defensibility | ✔ validation, historic + corrected data, audit trail | ✔ lab data validation, audit-ready records | ✔ audit trails, validation | implied |
| Evaluation / exceedance | ✔ alerts vs compliance | ✔ out-of-range flags, exceedance notifications | ✔ MCL comparison, exceedance alerts | ✔ breach warnings |
| Regulatory reporting | ✔ NetDMR, MORs, regulator templates | ✔ CCR + MOR single click, state/EPA review | ✔ MOR, LCR/DBP/MRDL reports, CMDP submissions | ✔ DMR generation |
| Consumer-facing artifact | — | ✔ CCR | ✔ CCR (Tier-3 consolidation named by EPA) | — |
| Dashboards/trends/GIS | ✔ dashboards, mapping | ✔ visualization, GIS | ✔ dashboards, GIS (ESRI) | ✔ benchmarking |
| Operations breadth | ✔ process/field data, daily workflows (Rio/WIMS pole) | companion apps, not core | ✔ operations management "beyond compliance" | — |
| Regime naming | NetDMR, MOR | SDWA, TCR/LC/DBP/PFAS, CCR/MOR, CMDP-class | SDWA rules, CMDP, MOR/CCR | NPDES, WSER, MCERTS, DMR |

Reading: the three utility-side products hold the same triple — identified monitoring locations bound to regulated parameters and drinking-water standards, a monitoring data estate fed from labs/field/instruments with defensibility machinery, and compliance evaluation feeding regulator-facing (and consumer-facing) reports. The specialist pole (WaterTrax/WIMS/Rio) wraps the triple in plant-operations data management; the platform pole (Locus) wraps it in the environmental-data corpus and companion water apps; the pure-play pole (SAMS) wraps it in rule-pack automation and electronic submissions. Intelex's identically-named product points the same grammar at the discharger's effluent instead of the utility's product water — the wastewater sibling.

## Abstraction Levels

### L0 — Defining Invariant (jointly-held triple)

1. **The water-quality monitoring program of record** — the utility's drinking-water quality obligations held as structured configuration: identified sampling/monitoring locations (source water, treatment, distribution system) bound to the parameters/contaminants they are monitored for, the drinking-water standards/limits that apply to them, and the monitoring requirements (which parameters, where, how often) that produce the required data. Remove → an anonymous lab data store or a spreadsheet with no program identity.
2. **The water-quality data estate** — the results the program produces: laboratory sample results and field/instrument readings held persistently against location, parameter, and date, with the validation and defensibility machinery (audit trail, preservation of original and corrected values) that makes them reportable. Remove → a schedule with no data of record.
3. **Compliance evaluation and the regulator-facing record** — results evaluated against the applicable standards (limit comparison, averaging-class computations), exceedances and missed-monitoring failures surfaced and handled (alerts, corrective actions, notification duties), and the periodic regulatory reports (monthly operating report class, consumer confidence report class, electronic submissions to state/EPA-class systems) assembled from the data and submitted. Remove → a monitoring dashboard with no compliance semantics, or report templates over nothing.

Jointly-held load-bearing: 1 alone = sampling-site register / compliance calendar; 2 without 1 = anonymous lab data store (environmental-data-platform / lab territory); 3 without 1+2 = report templates over nothing; 1+2 without 3 = monitoring data archive (environmental-monitoring territory); 1+3 without 2 = compliance calendar with no data; 2+3 without 1 = reporting over anonymous data.

Subject binding: **the utility's own drinking water** — the water the utility produces and delivers, from source through treatment to the distribution system, as the medium that must meet drinking-water standards; the utility is the regulated party (public water system). Remove the binding → the discharger's effluent compliance (wastewater-compliance-management) or ambient environmental waters (environmental-water-monitoring).

### L1 — Common Mature Structure

- Monitoring schedules with automated reminders, task assignment, and late/missing-sample flags (4/4)
- Lab data integration: LIMS/EDD import, electronic lab transfers (4/4)
- Data validation + audit trail + preservation of historic and corrected data — "defensibility" (4/4)
- Exceedance alerts/notifications (4/4)
- Regulatory report generation: MOR-class, CCR-class, state/electronic submissions with deadline tracking (4/4)
- Mobile field collection (4/4)
- Dashboards, trends, GIS mapping of results (4/4)
- Chain of custody for compliance samples (2/4 explicit — SAMS, Intelex; implied in others)
- Bench sheets / computation machinery (averages, min/max, LRAA-class) (2/4 explicit — SAMS, WIMS-class)
- SCADA/instrument feeds as complementary data (3/4)
- Permit tracking (2/4 explicit — SAMS, Locus)

### L2 — Variant / Optional Structure

- Rule-pack breadth per regime: US SDWA rule families (TCR, Lead & Copper, DBPs, radionuclides, VOCs, SOCs, PFAS) named by 3/3 utility-side products; other national regimes analogous but not directly sampled
- Operations-data breadth: daily rounds, bench sheets, process data, preventive maintenance (WIMS/Rio pole; SAMS "beyond compliance")
- Companion programs sold as sibling products on the same machinery: backflow/cross-connection control (Tokay, SAMS Cross Connection, Locus Backflow), industrial pretreatment (Linko, SAMS IPP, Locus IPP), stormwater, FOG
- Customer-complaint tracking (taste/odor/color) as a quality signal (Locus)
- Test-equipment/QC calibration management (Locus)
- Consumer-facing artifacts (CCR) vs regulator-facing only
- Packaging: standalone specialist vs platform app vs EHS-suite module
- Historical data migration from spreadsheets/legacy systems (SAMS)
- AI/ML anomaly detection, missing-sample prediction (SAMS; era-current)

### L3 — Vendor-specific (Research Notes only)

- Product names: WaterTrax, Hach WIMS, WIMS Rio, Tokay, Linko (Aquatic Informatics/Veralto family); Locus Drinking Water Quality / Locus Water apps; SAMS Water / SAMS platform (NJBSoft); Intelex Water Quality Management; Cority Water Management.
- SAMS: QR-code chain of custody, SOC 2 Type II, ESRI partnership, CMDP API/XML submissions, "unlimited users" pricing posture.
- Locus: 500M+ analytical records, 99.99+% uptime claims, AWS hosting, SOC 1/2 Type 2; San Jose Water case study.
- Aquatic Informatics: Veralto water-quality platform membership; Hach partnership/handover of WIMS; Penn Yan "90% time-savings on NetDMR" case figure (wastewater side).
- South Bend lead-and-copper quote (WaterTrax); Riverside SCADA+UWAM+WaterTrax quote.

## Vendor-specific Findings

See L3. None promoted to the canonical core.

## Boundary Findings

1. **vs water-network-monitoring (§19, processed) — INHERITED SEAM DISCHARGED, RATIFIED from this side.** The operational real-time quality signal (online analyzers, chlorine/turbidity events, quality anomalies in the network) belongs to that leaf's network condition; this leaf is the quality **program** — sampling plans, standards evaluation, compliance records, reports. Evidence: the WaterTrax customer quote treats SCADA and WaterTrax as separate systems combined for "the big picture"; SAMS integrates SCADA read-only ("without exposing control systems"); EPA's OWQM-DS guidance treats online monitoring as a surveillance/response practice and lists "regulatory compliance data" as a separate information category. Removal test: remove the live condition/detection/event loop → this Type intact; remove the program-of-record/compliance-report semantics → network monitoring. Keep-both.
2. **vs wastewater-compliance-management (§21, processed) — the effluent twin.** Same compliance-monitoring grammar, different subject and regime: drinking-water standards over the utility's **product water** (SDWA-class: MCLs, monitoring schedules, MOR/CCR, state primacy submissions, public-notification duties) vs discharge permits over the **effluent** (NPDES-class: outfall limits, DMRs). The same product families serve both (WaterTrax, WIMS/Rio, Locus, SAMS siblings) — one grammar, two Types, like AQM vs CEMS. Keep-both; the split is the regulated medium.
3. **vs environmental-water-monitoring (§21, unprocessed)** — the utility's own product water vs ambient/receiving environmental waters; compliance program vs observation loop. Flag stands for that pass.
4. **vs environmental-laboratory-management (§22, processed) — producer/consumer seam confirmed.** The lab analyzes samples and delivers validated results; the utility's quality program consumes them via LIMS/EDD import and holds the compliance record. Removal test: remove lab workflows → this Type intact. Keep-both.
5. **vs environmental-data-platform (§21, processed)** — the validated long-term corpus vs the compliance program; Locus realizes both in one platform (EIM corpus + drinking-water app). Ingestion handoff. Keep-both.
6. **vs environmental-compliance-management (§21, processed)** — obligation register + conformance loop vs the operational media program (locations + data + standards evaluation + reports). The sampled utility-side products carry no obligation register. Same seam the wastewater pass drew. Keep-both.
7. **vs environmental-permit-management (§21, processed)** — permit tracking present in some products (SAMS, Locus) but standards/limits are configured inputs; the center is the monitoring program, not the permit lifecycle. Keep-both.
8. **vs water-utility-management (§19, unprocessed)** — forward seam: the customer-service business system (accounts, charges, bills) vs the quality program. No object overlap expected. To be honored when that leaf is processed.
9. **vs backflow/cross-connection control products (Tokay, SAMS Cross Connection, Locus Backflow)** — a companion program sold as its own product: the utility manages backflow devices, certified testers, and test schedules on **customers' premises** — an authority-over-external-parties shape (like pretreatment), not the utility's own water-quality record. Held as adjacent companion program; TAXONOMY OBSERVATION: §19 has no leaf for cross-connection/backflow program management although the market realizes it as a distinct product family — recorded for the taxonomy owner.
10. **vs SCADA (§16, processed)** — control/telemetry machinery vs quality program; SCADA appears as a data source (read-only integrations). Keep-both.
11. **vs pool-service-management (§26, processed)** — different domain entirely (consumer pool water care); that pass already recorded the disclaimer.
12. **NAMING-COLLISION RESOLUTION (center-of-gravity test)** — the market label "water quality management" spans: (a) the water utility's drinking-water quality program — WaterTrax, WIMS/Rio, SAMS Water ("Water Quality Management Software for Regulatory Compliance" for SDWA), Locus ("drinking water quality management software") — **this leaf's center**; (b) the discharger-side sense — Intelex WQM (NPDES/WSER/MCERTS, point sources, DMRs) — already documented as wastewater-compliance-management (§21); (c) the ambient-monitoring sense — environmental-water-monitoring (§21, unprocessed); (d) consumer pool care — pool-service-management (§26). The §19 position (water family, between Water Network Monitoring and Wastewater Utility Management) and the market's utility-facing usage agree on sense (a). No directory change.

## Historical / Market-Sample Check

Paper-era analog: the water utility's quality laboratory and compliance office — the sampling route schedule pinned at the lab, bench sheets and lab bench logs, the exceedance log, the monthly operating report and the annual water quality report filled on pre-printed forms and mailed to the state primacy agency, with chain-of-custody sheets accompanying samples to the certified lab. All three L0 legs are satisfied with no software: identified monitoring locations with standards, a monitoring data record, and periodic evaluation feeding certified reports. The UK/EU statutory-sampling tradition (supply points and water supply zones, prescribed sampling frequencies, returns to the drinking-water regulator) fits the same structure with different regime names. No cloud, AI, dashboards, SCADA, rule-pack automation, or any specific national regime is in the L0. Historical check passes.

## Uncertainties

1. No Tier-1 operational documentation (help centers/user manuals) was reachable for any sampled product; all product evidence is product/solution-page level. Exact per-rule averaging windows, exact report formats, numeric thresholds, and workflow states are intentionally absent from the final document.
2. Non-US regimes (UK/EU statutory drinking-water sampling, other national standards) are reasoned by analogy from the regulatory-substrate structure; no EU/UK specialist product was fetched — regime-neutral claims are held at "the structure generalizes" strength.
3. The operational-quality pole (SUEZ/Xylem quality applications) was not fetched this pass; the seam vs network monitoring rests on the water-network-monitoring pass's first-hand evidence plus the EPA OWQM-DS distinction. No claim here depends on those products.
4. Backflow/cross-connection control was observed at product-page level only (Tokay/SAMS/Locus positioning); its internal structure (device inventories, tester coordination) belongs to a dedicated pass if the taxonomy owner adds a leaf.
5. The pure-play market beyond the sampled poles is under-sampled; market-breadth claims are held at "commonly" strength.
6. Whether any product natively executes corrective-action field work (crews) rather than tracking tasks: none observed in-sample; corrective actions appear as tracked tasks/notifications, with field work living in adjacent systems.

## Final Synthesis

Water Quality Management (§19) is the water utility's drinking-water quality program system of record. Its defining core is the jointly-held triple: the water-quality monitoring program of record (identified sampling/monitoring locations across source, treatment, and distribution, bound to regulated parameters, applicable drinking-water standards, and monitoring requirements) + the water-quality data estate (lab results and field/instrument readings held against location/parameter/date with validation and defensibility machinery) + compliance evaluation and the regulator-facing record (limit evaluation, exceedance and missed-monitoring handling, and periodic regulatory reports — monthly operating report class, consumer confidence report class, electronic submissions — assembled and submitted). Around that core, mature products add scheduling automation, LIMS/EDD integration, chain of custody, bench-sheet computations, exceedance alerting, dashboards/GIS, and mobile collection. The market realizes one Type in three packaging poles — water-sector specialist (WaterTrax/WIMS/Rio), environmental-data-platform app (Locus), pure-play SDWA compliance automation (SAMS) — with the operations-data breadth (WIMS/Rio, SAMS operations) as a common extension and companion programs (backflow, pretreatment, stormwater) sold as sibling products. The Type is the drinking-water member of the compliance-monitoring grammar whose effluent member is wastewater-compliance-management and whose ambient member is environmental-water-monitoring; the live operational quality signal stays with water-network-monitoring. The naming-collision watch is resolved: the leaf's center of gravity is the utility-side drinking-water program.
