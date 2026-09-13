# Research Notes — Environmental Data Platform

Research date: 2026-09-08
Directory leaf: Environmental Data Platform (§21 Environment, Sustainability & Climate)
Slug: environmental-data-platform

---

## Research Goal

Understand what software marketed as an **environmental data platform / environmental data management system** actually does: what the unit of record is, how environmental data enters and is quality-controlled, what the corpus is organized around, what evaluation and outputs it produces, and how this Type differs from adjacent Types — especially **Contaminated Site Management** (processed 2026-09-07, which flagged this leaf for joint review), Environmental Monitoring Platform, Environmental Laboratory Management, Environmental Compliance Management (processed 2026-09-08), and generic data-infrastructure Types (§13).

## Joint-review context (from the contaminated-site-management pass)

The sibling pass (2026-09-07) sampled ESdat, EQuIS, Locus EIM, EnFlection and recorded: "all four sampled products are simultaneously strong candidates for the environmental-data-platform leaf… joint review recommended when environmental-data-platform is processed — candidate outcomes: keep-both with the site-lifecycle seam (current framing) or re-scope this leaf's population toward register/case-led products."

This pass performs the data-platform side of that review. Design decision: the sample keeps the canonical environmental-data-management products (EQuIS, ESdat, Locus EIM) **and adds a fourth product (KISTERS WISKI) whose center is demonstrably NOT contamination/site-lifecycle** — a hydrological/meteorological agency data platform. If the Type's core holds on WISKI without any contamination frame, the "keep-both with the data-corpus vs site-lifecycle seam" outcome is evidenced rather than asserted.

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis)**: the system of record for an organization's or program's environmental data — a central, quality-controlled corpus of environmental observations (lab results, field measurements, sensor/logger time series, geological observations), organized by location and observation event, evaluated against environmental standards, and rendered into analysis and reporting outputs.
- **Who**: environmental scientists/engineers/data managers in consultancies; owner/custodian organizations (mining, energy, industry, defense); government agencies and cleanup/water programs; labs as data suppliers.
- **Nearest Types**: Contaminated Site Management, Environmental Monitoring Platform, Air Quality Monitoring, Environmental Water Monitoring, Environmental Laboratory Management, Environmental Compliance Management, Environmental Site Assessment, Environmental Remediation Management, Data Warehouse/BI (§13), Industrial Historian (§16), Government Open Data Portal (§24).
- **Unknowns**: (1) whether the Type's center is the lab-chemistry corpus (contaminated-land lineage) or generalizes to time-series/sensor corpora; (2) whether standards/exceedance comparison is definitional or common; (3) depth of the agency/program pole.

## Research Questions

1. What is the unit of record — dataset, location, sample, site, program?
2. How does data enter (lab deliverables, field, sensors, manual, historical migration), and what quality control gates it?
3. What shared environmental structure does the corpus enforce (locations, samples, analytes/parameters, units, methods, qualifiers)?
4. How are results evaluated (standards/guidelines, exceedances, QA objectives, trends, statistics)?
5. What outputs does the corpus produce (tables, graphs, maps, bore logs, dashboards, regulatory formats, public portals, feeds)?
6. Who operates the system, and how do consultant / owner / agency deployments differ?
7. What is deliberately NOT this Type (monitoring operations, lab workflow, compliance obligation management, generic BI)?

## Representative Products

Selection rationale: market representation (the environmental-data-management category's canonical vendors), documentation completeness, different product philosophies (desktop-professional workbench vs web-enterprise platform vs SaaS suite module vs agency water-information system), different customer tiers (consultancies, Fortune 500/DOE, defense/mining, public authorities/utilities), and — deliberately — one product outside the contaminated-land lineage to test the Type's boundary.

| Product | Vendor | Pole | Evidence tier reached |
|---|---|---|---|
| EQuIS (Professional / Enterprise & Schemas) | EarthSoft | enterprise environmental data management; "single source of truth"; agency + industry + consultancy | Tier-1 official pages ×2 (Professional; Enterprise — the page the sibling pass could not fetch) |
| ESdat | EScIS | consultant/owner/agency environmental data management (AU/NZ/CA/UK/US) | Tier-1 official pages ×2 (root; features) |
| Locus EIM | Locus Technologies | multi-tenant SaaS environmental information management inside a wider platform | Tier-1 official page ×1 (EIM overview) |
| WISKI | KISTERS | water/environmental information system for public authorities, utilities, consultants — hydrology/meteorology/water-quality time-series corpus, no contamination frame | Tier-1 official page ×1 |

Deliberately not sampled: EnFlection (Trihydro) — already documented Layer-A by the contaminated-site pass; remediation/post-closure anchored, adds no new pole here. TerraBase (403 in sibling pass). Bentley/Aquatic Informatics water-data products (WISKI already covers the water pole). EHS-suite environmental modules (Cority/Intelex/Enablon) — sampled by the compliance pass for the compliance Type; suite-module pole noted as variant direction only.

## Sources

Fetched 2026-09-08 (all Layer A unless noted):

- EarthSoft EQuIS Professional — https://earthsoft.com/products/professional/
- EarthSoft EQuIS Enterprise & Schemas — https://earthsoft.com/products/enterprise/
- ESdat root — https://esdat.net/
- ESdat Data Analysis & Reporting (features) — https://esdat.net/esdat-features/
- Locus EIM overview — https://www.locustec.com/applications/environmental-information-management/
- KISTERS WISKI — https://www.kisters.net/wiski

Context from sibling passes (not re-fetched this pass; used for boundary reasoning only):
- research/contaminated-site-management.md (2026-09-07) — ESdat/EQuIS/Locus EIM/EnFlection observations, LCRM canon
- STATUS.md Processed entries — environmental-compliance-management (2026-09-08), contaminated-site-management (2026-09-07)

No unreachable sources this pass; no claims rest on inaccessible material.

## Product Observations

### EQuIS (EarthSoft) — Key observations

Evidence: A (both pages fetched this pass).

- Professional positioning: "Advanced Data Management for Decision Support and Data Analysis"; "checking, editing, loading, reporting, and visualizing environmental and sample data"; "administrative capabilities of the EQuIS data management workflows"; "advanced tools for environmental scientists and engineers to review analytical chemistry, geology, and other environmental data."
- Professional tools: Reference Value management; Action Level and regulatory guideline management; import formats and rules (supports GeoTracker, ERPIMS, and others); advanced crosstab report engine; query building tools; Esri GIS, Bentley gINT, AutoCAD and other third-party exports; EnviroInsite for advanced data visualization, subsurface graphics and reports; user security and schema access; data qualification, verification, and validation support.
- Packaging: Professional libraries (Standard / Data / Graphics / Decision Support); written in VB.NET on SQL Server.
- Enterprise page: "EQuIS: Single Source of Truth for Environmental Data." "All EQuIS workflows require EQuIS Schemas (databases) in SQL Server… The EQuIS Schema is the licensed data structure, rules, and central data repository supporting all EQuIS software products and workflow services." Enterprise adds: workflow automation via user-defined dashboard/widget views in a browser; "Data loading, data quality checks, reporting, and visualization automated in Enterprise"; dashboards/widgets/query-building (charts, graphs, maps, tables). Enterprise levels Basic/Premium; schemas hosted on customer server or cloud.
- Product family (navigation): EQuIS Data Acquisition (EDP — EQuIS Data Processor; Collect — field; External Data Submitter license); EQuIS Live; DQM (Data Qualification Module); SPM (Sample Planning Module); EQuIS Geotech; EQuIS for ArcGIS / AutoCAD; EnviroInsite; Risk3T; EQuIS Helios; REST API; EDD Formats support area; Data Governance; hosting options.

### ESdat (EScIS) — Key observations

Evidence: A (both pages fetched this pass).

- Root positioning: "Environmental Data Management Software for Monitoring & Compliance"; "helps scientists and engineers import, manage, analyze and report data from laboratories, field programs, data loggers, sensors, historical sources, and regulatory standards. All in one place." Audience: "scientists, engineers, and managers who need to understand environmental, hydrogeological and related site investigation, monitoring, and compliance data."
- Feature set (nav + root): Laboratory Integration; Environmental Standards; Field Programs; Logger Data; Data Migration; Data Analysis and Reporting; Public Portal. Industries: Consultants, Mining, Government, Energy, Industry, Landfills.
- Laboratory integration: "Laboratories around the world are assessed and approved to upload their reports to ESdat where the data is validated, loaded and ready for analysis and reporting."
- Field programs: "plan, execute and report all stages of large or recurring field programs." Field App runs offline on PC/tablet/smartphone; pre-planned sampling; industry-specific forms (e.g., groundwater stabilization records); monitoring locations with distance and prior-results photos.
- Logger data: "Review your logger data in real-time and visualize trends. Receive alerts and flag problematic data"; instruments for weather, dust, water level, water quality.
- Bore logging: borehole, geology, groundwater data → automated report-ready bore logs.
- Analysis & reporting (features page): customizable dashboards (maps, graphs, shortcuts, notifications; click map point to update all widgets); exceedance tables (chemistry vs environmental standards; filter by lab report/location/date; export to Excel); maps (map-based querying; exceedance tables in map view; export locations to ArcGIS/MapInfo/QGIS; Bing imagery, WMS/WFS, own basemaps); graphs & trend analysis (time series; Mann Kendall and linear regression; regulatory limits on graphs; bulk print for appendices); geochemistry (mEq/L conversion; Piper, Durov, Schoeller, Ternary diagrams); data querying (SQL syntax; custom joins/views; live Excel connections).
- Validation & QA: "Your data is automatically validated upon import. Any errors detected will be reported back to you and the lab immediately. Assess Field and Lab QA data against your own Data Quality Objectives. Data approval mechanism built into the system." QA indicators: holding times, RPD values, detects in blanks, ionic balance.
- Standards: "US, Canadian, Australian, NZ, UK, and other regulatory guidelines are pre-loaded, plus add your own"; exceedance notifications on load; reminders for upcoming/overdue monitoring.
- Statistics: mins/maxes/std devs/95th percentiles; ProUCL export.
- Outputs/integration: Power BI, Excel Power Query, ArcGIS feeds; public portal ("publish approved results on the web to meet reporting obligations"); data sharing with permissions to view/add/edit per project/site; "Your data is tracked from the moment it is entered."

### Locus EIM (Locus Technologies) — Key observations

Evidence: A (page fetched this pass).

- Positioning: "Environmental Information Management (EIM) & Remediation"; "If you're managing environmental data across sites, labs, and field teams — Locus EIM was built for exactly this"; "used by Fortune 500 companies, water utilities, and the US Department of Energy since 1999."
- Framing vs sibling Types: "While ESG software summarizes sustainability efforts and EHS software manages compliance tasks, EIM software is the science-based engine underneath both — the place where your actual environmental data lives, gets validated, and becomes defensible."
- Media breadth: "handles water, soil, air, biological, geological, and radionuclide data from sample planning through regulatory reporting"; "whether our clients are boring soil, testing air quality, probing fish flesh, or assessing concentrations of PFAS in water."
- Ingestion: "quickly load water, air, soil, or any other analytical data via multiple EDD formats, FTP, Excel imports, surveys, mobile devices, email, or manual entry. Locus converts units, flags potential errors, and offers automated data validation to protect integrity."
- Sample Planning Module: "build, execute, and track a cradle-to-submitted sampling program"; tasks/workflows dispatch field crews to multiple sites at required intervals; Locus Mobile syncs field measurements, surveys, notes.
- Navigation of the corpus: dashboards and grids; search by location ID / field sample ID / parameter; wildcard search; Expert Query constructs custom SQL queries that are API-compatible.
- Visualization: dynamic forecasting charts, contours, augmented reality, smart-mapping (ArcGIS online compatible).
- Reporting: exports and regulatory reports "including DMRs, vapor intrusion, lithology, WQX, CIWQS."
- Integration: API connectors to ERP, Power BI, Tableau.
- Platform: multi-tenant cloud SaaS; SSO; SOC 1 Type 2 / SOC 2 Type 2; EIMone edition for smaller water utilities. Vendor counters (claims): 1,894,903 locations; 528,025,546 analytical records.

### WISKI (KISTERS) — Key observations

Evidence: A (page fetched this pass).

- Positioning: page title "Environmental data management system | WISKI"; "WISKI is KISTERS' modular Water Information System for managing, validating, analyzing & visualising hydrological & environmental data across its full lifecycle"; "a scalable data management platform used worldwide by public authorities, utilities & consultancy firms to manage water and environmental data"; "brings together data from multiple sources into one reliable system"; "Designed to scale from local monitoring networks to national systems."
- Value claims: "A single, trusted source of truth for water and environmental data"; "Reliable validation workflows to ensure data quality."
- Core capabilities: data integration and management ("Collect, harmonize & manage data from data loggers, smart sensors, SCADA systems, models & external sources in one central system"); data quality and validation ("automated & manual validation processes… consistent, reliable & auditable"); visualization and reporting ("dashboards, charts & reports tailored to different users & decision contexts"); analysis and decision support ("analysis, forecasting, and evaluation of data in accordance with national & international standards & regulations"); flexible deployment (on-premise or cloud).
- Application areas: hydrology (levels, temperature, flow, velocity); groundwater (level, flow rates, depth); water quality & biodiversity (chemical, physical, biological parameters); meteorology; flood & heavy rain (model integration, message templates, automated monitoring, alerts to users and residents); also dam monitoring, hydropower, river management, urban hydrology, water supply, wastewater.
- Extensions/modules: WISKI Web (publish trusted data in real time via secure web portals; access control; "transparent data sharing for compliance and public communication"); KiWQM & KiECO (water quality: "Combine laboratory results and sensor data into one consistent, auditable system"; trend analysis; compliance-ready workflows); FieldVisits (mobile field data collection, offline, sync to central system); KISTERS Analytics (automation of validation/alarming/analysis; AI, predictive modelling, digital twins); BIBER & SKED (discharge calculations, rating curves, ADCP support; "accurate, traceable and defensible hydrometric data").
- FAQ: "it imports, archive, validate and analyze data, it also produces clear, sharable reports, tables, graphs and observations." Customers: environmental agencies, municipalities, engineering firms, utility providers, hydropower producers, dam operators, mining companies.

## Cross-product Comparison

| Dimension | EQuIS | ESdat | Locus EIM | WISKI |
|---|---|---|---|---|
| Self-description | "Single Source of Truth for Environmental Data"; checking/editing/loading/reporting/visualizing environmental & sample data | "Environmental Data Management Software"; import/manage/analyze/report "all in one place" | "the place where your actual environmental data lives, gets validated, and becomes defensible" | "Environmental data management system"; "single, trusted source of truth"; manage/validate/analyze/visualise "across its full lifecycle" |
| Unit of record | EQuIS Schema — licensed data structure, rules, central repository (facility/location/sample/result) | organized environmental dataset per project/site (locations, samples, results, standards) | environmental corpus across sites/labs/field teams (locations, samples, results) | central time-series + observation corpus per monitoring network (stations, parameters, time series) |
| Ingestion sources | EDD formats (GeoTracker, ERPIMS, others); EDP/Collect/External Submitter; manual | labs (assessed & approved upload), field programs/app, loggers/sensors, historical migration, manual | EDD formats, FTP, Excel, surveys, mobile, email, manual | data loggers, smart sensors, SCADA, models, external sources; lab results (KiWQM); field app |
| Validation/QC | data qualification, verification, validation support; DQM module; data quality checks automated in Enterprise | automatic validation on import; errors reported back to lab; QA vs Data Quality Objectives; approval mechanism; holding times/RPD/blanks/ionic balance | converts units, flags errors, automated data validation | automated & manual validation workflows; auditable |
| Standards machinery | reference values; action level & regulatory guideline management | pre-loaded US/CA/AU/NZ/UK guidelines + custom; exceedance tables/maps/notifications | regulatory thresholds; exceedance queries (sibling pass) | "evaluation… in accordance with national & international standards & regulations" (weaker page-level evidence) |
| Analysis/visualization | crosstab reports; query building; EnviroInsite subsurface graphics; Esri GIS/gINT/AutoCAD exports | dashboards; exceedance tables; maps; time-series & Mann Kendall trends; statistics (95th pct, ProUCL); Piper/Durov/Schoeller/ternary; bore logs | dashboards/grids; forecasting charts; contours; smart mapping; Expert Query (SQL) | dashboards, charts, reports; trend analysis; forecasting; rating curves (BIBER/SKED) |
| Sampling/field machinery | SPM; Collect/EDGE field tools | field programs; offline Field App | Sample Planning Module; Locus Mobile | FieldVisits mobile app |
| Time-series/sensor | EQuIS Live | logger data with alerts/flagging | SCADA & sensors app | core (telemetry, SCADA, models) |
| Regulatory outputs | GeoTracker/ERPIMS format support | regional guideline libraries; public portal for reporting obligations | DMR, vapor intrusion, lithology, WQX, CIWQS | compliance-ready workflows; public data sharing (WISKI Web) |
| Portfolio scale | enterprise schemas; hosting options | enterprise multi-department; government intake | multi-tenant SaaS; Fortune 500/DOE; EIMone for small utilities | local networks → national systems |
| Governance/access | user security & schema access; Data Governance product | permissions per project/site; tracked from entry; ISO 27001 posture | roles, SSO, SOC 1/2 Type 2 | secure portals; access control; auditable |
| Integration spine | Esri GIS, gINT, AutoCAD, REST API | Power BI, Excel, ArcGIS, Web API, QGIS/MapInfo | Power BI, Tableau, ERP, API (JSON/OData) | models, SCADA, external sources; portals |
| Contamination frame | strong (site investigation/remediation lineage; GeoTracker/ERPIMS) | strong (contaminated-land lineage; but also mining/landfill/monitoring) | strong (remediation & liability) but media-broad (air, biological, radionuclide) | **absent** — hydrology/meteorology/water quality/flood |
| Delivery | self-hosted SQL Server or cloud | online SaaS (pre-configured) | multi-tenant SaaS | on-premise or SaaS |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three properties. Remove any one and the product is no longer recognizable as an environmental data platform:

1. **The environmental data corpus of record** — a persistent, central, authoritative store of environmental observations (analytical results, field measurements, instrument/logger readings, geological/hydrogeological observations) held in a shared environmental structure — locations/stations, samples or observation events, parameters/analytes, units, methods, quality state — and retained over the long term. Remove → a generic database, file share, or BI project with no environmental subject.
2. **Governed ingestion into that structure** — data produced outside the system (laboratory deliverables, field programs, instruments/loggers, historical sources, manual entry) enters through validation and normalization into the shared structure, rather than as loose files; errors are surfaced and corrected at the gate. Remove → a data dump; the "system of record" claim collapses.
3. **Environmental analysis and reporting outputs** — the corpus is queried and rendered into the outputs environmental professionals and regulators consume: summary/chemistry tables, trend charts and statistics, maps, subsurface/bore-log graphics, dashboards, regulatory-format reports, published datasets. Remove → a QC'd archive nobody can work with.

Jointly-held is load-bearing: (1 alone = generic archive; 2+3 without 1 = one-off lab-data conversion tool; 1+2 without 3 = QC'd store with no usable outputs; 1+3 without 2 = hand-keyed spreadsheet with charts).

Historical check (§24): pre-software practice satisfies all three — an agency's station-by-station hydrometric ledgers (corpus organized by station and observation, checked on entry, tabulated and plotted for reports), or a consultancy's lab-report binders with hand-typed chemistry tables compared against guideline values and plotted on maps. Cloud, GIS, EDD automation, telemetry, AI are NOT definitional. Passed.

### L1 — Common Mature Structure (standard capabilities; cross-product B evidence)

- **Location & spatial context** — sampling locations/stations/wells bound to coordinates; map surfaces; GIS interchange (ArcGIS/MapInfo/QGIS-class exports, basemaps/WMS/WFS). 4/4.
- **Sampling & monitoring program machinery** — planning and scheduling recurring sampling/monitoring events; field data capture (mobile/offline apps); dispatch of field crews. 4/4.
- **Laboratory deliverable ingestion** — electronic lab deliverable (EDD) formats; approved-lab upload programs; lab results combined with sensor data. 4/4.
- **QA/QC machinery** — automated validation on import with errors reported back to the source; QA indicators (holding times, duplicates/RPD, blanks, ionic balance); assessment against data quality objectives; data approval states; data qualification flags. 3/4 explicit (WISKI: automated & manual validation, auditable).
- **Standards/guideline comparison & exceedance machinery** — managed libraries of regulatory guideline values/action levels (regional pre-loading common) plus custom limits; exceedance tables/maps; exceedance notifications. Loud in 3/4; WISKI evidences evaluation "in accordance with standards & regulations" at page level only → held as common, NOT definitional (WISKI counter-test).
- **Time-series / sensor / telemetry ingestion** — data loggers, smart sensors, SCADA; real-time review with alerts and flagging. 4/4 (center of gravity in WISKI; capability in the other three).
- **Analysis & visualization depth** — trend analysis (named methods, e.g., Mann Kendall, linear regression), summary statistics (percentiles; ProUCL-class export), geochemistry diagrams (Piper/Durov/Schoeller/ternary), contouring, subsurface/bore-log graphics, forecasting charts. 3–4/4 varying depth.
- **Regulatory-format reporting** — named state/federal/program formats (GeoTracker, ERPIMS, DMR, WQX, CIWQS-class) and regional guideline libraries. 3/4 strong.
- **Portfolio / multi-site / multi-network operation** — cross-site queries, enterprise schemas, scale from single projects to national networks. 4/4.
- **Notifications** — exceedance alerts, overdue lab reports, upcoming/missed monitoring events, significant-data-event notices. 3/4.
- **Governance, permissions & provenance** — role/project-scoped access and data sharing; tracking from the moment of entry; auditability; security certification posture. 4/4.
- **Integration spine** — feeds to GIS, BI (Power BI/Tableau-class), Excel; APIs; model/SCADA connectivity. 4/4.
- **Public data publishing** — web portals publishing approved/trusted data for reporting obligations and public communication. 2/4 as product capability (ESdat, WISKI); deployment-dependent (see L2).
- **Historical data migration** — importing legacy/historical datasets as a first-class operation. 3/4.

### L2 — Variant / Optional Structure

- **Operator pole**: consultant workbench (per-project data management) vs owner/custodian portfolio (mining, energy, defense, utilities consolidating multi-consultant/multi-lab data) vs agency/program platform (public authorities running monitoring networks; receiving third-party submissions; publishing public data).
- **Domain emphasis pole**: discrete-sample chemistry corpus (lab-EDD-centric; contaminated-land/water-quality lineage) vs time-series telemetry corpus (station/sensor-centric; hydrology/meteorology) vs mixed multi-media corpora (water, soil, air, biological, geological, radionuclide).
- **Suite module vs standalone specialist**: EIM inside a wider EHS/ESG platform (Locus) vs dedicated environmental data management product line (EQuIS, ESdat) vs water-information system with extension modules (WISKI).
- **Delivery**: self-hosted relational database (SQL Server) vs multi-tenant SaaS vs single-tenant/on-premise.
- **Regional regulatory packaging**: US state/federal program formats; AU/NZ/CA/UK guideline libraries; national/international standards contexts.
- **Scale**: single project → enterprise → national monitoring networks.
- **AI/predictive assistance**: natural-language querying, AI/predictive modelling layers (era-typical; one product markets an analytics layer with AI/digital twins).

### L3 — Vendor-specific (research notes only; NOT in final document)

- **EQuIS**: Professional/Enterprise product split; licensed Schema packaging (Basic/Premium); module names EDP, EDGE, Collect, SPM, DQM, EnviroInsite, EQuIS Live, EQuIS Geotech, EQuIS for ArcGIS/AutoCAD, Risk3T, Helios; named GeoTracker/ERPIMS formats; VB.NET/SQL Server stack; library configurations; GSA contract; "schemas described as works of art."
- **ESdat**: EScIS branding; LabSync; Aquadata public portal (Shoalhaven Council case study); approved-lab assessment program; ProUCL export; Mann Kendall naming; ISO 27001 badges; client logo wall (Arcadis, AECOM, Stantec, Geosyntec, Tetra Tech, Rio Tinto, BHP, AU/CA/NZ defence, DCCEEW, NSW/QLD/NT).
- **Locus**: EIM/EIMone product names; Expert Query; GIS+; TRRP Commander (TCEQ); DMR/WQX/CIWQS/lithology/vapor-intrusion format names; Locus Mobile; vendor counters (1,894,903 locations / 528,025,546 analytical records); 99.992% uptime claim; SOC 1/2 Type 2; "probing fish flesh" phrasing; blockchain/AI marketing.
- **WISKI**: KiWQM, KiECO, FieldVisits, BIBER, SKED, KISTERS Analytics, WISKI Web module names; ADCP/rating-curve hydrometry; flood message templates; 24/7 support claim.

## Vendor-specific Findings

See L3. Named regulatory formats (GeoTracker, ERPIMS, DMR, WQX, CIWQS, TRRP) are product-specific realizations of the standard "regulatory-format reporting" capability and must not be promoted into the definition. Named QA indicators (RPD, ionic balance) are realizations of the standard "QA/QC machinery" capability.

## Rejected Findings

- **"Environmental data platform = contaminated-site data management."** Rejected as a collapse: the WISKI pole (hydrology/meteorology/water-quality agency corpus, no contamination frame) satisfies the same core. Contaminated land is one domain emphasis, not the definition. This resolves the sibling pass's joint-review question in favor of keep-both with the data-corpus vs site-lifecycle seam.
- **"Standards/exceedance comparison is definitional."** Rejected — WISKI's page-level evidence shows a recognizable environmental data platform whose standards machinery is not the chemistry-exceedance center. Held as common mature structure.
- **"GIS/mapping is definitional."** Rejected — historical (paper-era) corpora were mapped by hand; maps are standard capability.
- **"Lab EDD automation is definitional."** Rejected — manual entry paths exist in sampled products; the WISKI pole is sensor-centric.
- **"Time-series/telemetry is definitional."** Rejected — the chemistry-corpus pole centers discrete samples.
- **"Public portal is definitional."** Rejected — deployment-facing variant (owner-side deployments are commonly confidential).
- **"Cloud SaaS is definitional."** Rejected — EQuIS self-hosted SQL Server and WISKI on-premise are first-class realizations.
- **"AI/NLQ is definitional."** Rejected — era-typical addition.
- **"A licensed schema product = the definition."** The licensed data structure is one vendor's packaging of the corpus; conceptually the shared environmental structure is definitional, the licensing packaging is vendor-specific.

## Boundary Findings

1. **vs Contaminated Site Management (§21, processed 2026-09-07) — the sharpest seam; joint review performed this pass.** The two Types share their instrument set (validated lab-data ingestion, standards comparison, maps, reporting). The seam is the center: contaminated site management centers the *site* as unit of record — identification, contamination profile, lifecycle progression (investigation → remediation → monitoring → closure), long-term retention of the register. The environmental data platform centers the *data corpus* itself, serving any environmental program (site investigation, compliance monitoring, water quality, hydrology, air) with no contamination frame and no site lifecycle required. Remove-what tests: remove the site-lifecycle/contamination frame from contaminated site management → an environmental data platform; make sites (rather than the corpus) the unit of record with lifecycle state → contaminated site management. Outcome recorded: keep-both with this seam; the shared product population (ESdat/EQuIS/Locus EIM/EnFlection) is documented from both centers.
2. **vs Environmental Monitoring Platform (§21, unprocessed).** Monitoring platform = ongoing observation of current conditions (sensor networks, live readings, alarms, network health). Data platform = the validated long-term corpus of record. Overlap: sensor/telemetry ingestion (ESdat logger data, EQuIS Live, WISKI telemetry, Locus SCADA/sensors app) — the data platform ingests monitoring streams, but its center is the managed corpus, not live monitoring operations. WISKI (with KISTERS Analytics alarming) is the blur-zone specimen.
3. **vs Environmental Laboratory Management / LIMS (§21, unprocessed).** The lab system manages lab workflow (samples in → analyses → results out, lab accreditation); the data platform ingests the results as deliverables into the environmental corpus. Handoff at the electronic lab deliverable ("assessed and approved to upload their reports… validated, loaded" — ESdat; EDD formats — EQuIS/Locus). No merge.
4. **vs Environmental Compliance Management (§21, processed 2026-09-08).** Compliance management = obligation register + obligation-driven compliance work + evidence-backed compliance status. The data platform holds the measurement corpus that can serve as compliance evidence, but holds no obligations, no compliance status, no corrective-action loop. The compliance pass deliberately avoided Locus for this reason. Clean seam.
5. **vs Environmental Site Assessment / Environmental Remediation Management (§21, unprocessed).** Assessment execution and remediation project execution are process applications; their outputs (investigation data, remediation monitoring data) are ingested as corpus inputs here. Handoff, not overlap (consistent with the sibling pass's finding).
6. **vs Data Warehouse / BI Platform (§13).** Generic data infrastructure holds any data and produces any dashboard; the environmental data platform's product IS the environmental structure — analytes, units, methods, detection limits/qualifiers, media, stations/wells, guideline libraries, regulatory formats. EQuIS's licensed Schema ("data structure, rules, and central data repository") shows the structure is the product.
7. **vs Industrial Historian / SCADA (§16).** Process historians hold plant process time series for operations; the environmental data platform holds environmental observations for environmental programs, mixing lab chemistry and field/sensor data with QA and standards machinery. Adjacent at the telemetry leg.
8. **vs Government Open Data Portal (§24).** Publishing approved results is one output capability of this Type; the open-data portal's center is public dataset publication, not the organization's corpus of record.
9. **"Remove-what" tests:** remove the corpus (no persistent store) → one-off lab-data processing; remove validation/QC → file dump; remove environmental structure (analytes/locations/units) → generic database; remove outputs → archive; remove standards machinery entirely → still this Type (thin, WISKI-pole-adjacent); remove multi-source ingestion breadth → thin but still this Type.

## Uncertainties

- **WISKI's standards/exceedance depth** is evidenced only at page level ("evaluation… in accordance with national & international standards & regulations"; "compliance-ready workflows"); no exceedance-table mechanics observed. Standards machinery is therefore held at common strength with qualified wording for the water pole.
- **Agency/program pole depth** (regulator receiving third-party submissions, running program data flows) is evidenced indirectly: EQuIS External Data Submitter license + GeoTracker/ERPIMS formats; ESdat government page (sibling pass, Layer A); WISKI's public-authority customer base. Written at moderate strength.
- **EQuIS Enterprise workflow-automation depth** now rests on the fetched Enterprise page (Layer A this pass — upgrades the sibling pass's Tier-2 note), but module-level behavior (DQM, SPM, Live) is known from navigation/product names, not fetched module pages.
- **Vendor counters** (Locus locations/records, uptime) are vendor claims, recorded as claims only.
- **Suite-module pole** (EHS-suite environmental data modules) not directly sampled this pass; noted as variant direction from Locus's own platform framing and the compliance pass's vendor landscape.
- **EnFlection** not re-fetched this pass; its observations come from the sibling pass's Layer-A fetch (2026-09-07) and are used only for boundary reasoning.

## Final Synthesis

The Type is a **data-corpus-centered system of record for environmental data**. Its world: the environmental data corpus (observations held in a shared environmental structure — locations/stations, samples/events, parameters, units, methods, quality state) → governed ingestion (lab deliverables, field programs, instruments/loggers, historical sources, manual entry — validated, normalized, error-reported, approvable) → evaluation and analysis (standards/guideline comparison with exceedance surfacing where applicable, QA objectives, trends, statistics) → environmental outputs (chemistry tables, trend charts, maps, bore logs, dashboards, regulatory-format reports, published data, GIS/BI feeds). The corpus is the center; sites, projects, programs, and networks are containers; no contamination frame and no site lifecycle is required. Two dominant realizations: the discrete-sample chemistry corpus (lab-EDD-centric; contaminated-land/water-quality lineage) and the time-series telemetry corpus (station/sensor-centric; hydrology/meteorology lineage) — most mature products mix both. The seam with Contaminated Site Management is held on the corpus-vs-site-lifecycle center (joint review outcome: keep-both); the seams with Monitoring Platform, Laboratory Management, and Compliance Management are held on live-observation, lab-workflow, and obligation-register centers respectively.
