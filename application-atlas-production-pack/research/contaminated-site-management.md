# Research Notes — Contaminated Site Management

Research date: 2026-09-07
Directory leaf: Contaminated Site Management (§21 Environment, Sustainability & Climate)
Slug: contaminated-site-management

---

## Research Goal

Understand what software marketed for **contaminated site management** actually does: what the unit of record is, how sites are identified and tracked over time, what evidence accumulates on a site, how the site's lifecycle (investigation → remediation → monitoring → closure) is managed, and how this Type differs from adjacent environmental Types (Environmental Site Assessment, Environmental Remediation Management, Environmental Data Platform, Environmental Monitoring Platform).

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis)**: an application keeping the authoritative record of land/water sites affected — or suspected of being affected — by contamination, and managing each site through its environmental lifecycle, with the site retained as a record even after closure.
- **Who**: environmental regulators / cleanup program staff; environmental consultants; site owners and responsible parties (petroleum, industrial, defense, utilities).
- **Nearest Types**: Environmental Site Assessment, Environmental Remediation Management, Environmental Data Platform, Environmental Monitoring Platform, Environmental Compliance Management, Government GIS, Land Records, Waste Management.
- **Unknowns**: (1) whether the market center is data management (lab data) or site register/case management; (2) whether a pure-play "contaminated site management" product class exists distinct from environmental data management systems; (3) agency/regulator-side register products (reachability uncertain).

## Research Questions

1. What is the unit of record — site, case, project, or dataset — and how is a site identified?
2. What statuses/phases do sites move through, and who/what advances them?
3. What evidence accumulates on a site (assessments, sampling events, analytical results, documents)?
4. How do products compare results against regulatory screening criteria (guideline values, action levels)?
5. How is location handled (GIS, coordinates, sampling locations, wells/boreholes)?
6. What happens at and after closure? Are closed sites retained?
7. How do consultant-side vs owner-side vs regulator-side deployments differ?
8. What is deliberately NOT this Type (ESA fieldwork software, remediation project management, lab data engines, waste logistics)?

## Representative Products

Selection rationale: market representation (contaminated-land lineage), documentation completeness, different product philosophies (consultant workbench vs enterprise platform vs agency system-of-record), different customer tiers (consultancies, government/defense, Fortune 500, state programs).

| Product | Vendor | Pole | Evidence tier reached |
|---|---|---|---|
| ESdat | EScIS / EarthScience Information Systems | consultant/owner/agency environmental data management, contaminated-land anchored (AU/NZ/CA/UK/US) | Tier-1 official site ×4 (root, government, standards, NZ DoD case study) |
| EQuIS (Professional / Enterprise) | EarthSoft | enterprise environmental data platform widely used in site investigation/remediation and by agencies | Tier-1 official product pages ×2 (Professional fetched; Enterprise catalogued from navigation) |
| Locus EIM | Locus Technologies | commercial SaaS environmental information management incl. remediation & environmental liability management | Tier-1/Tier-2 official pages ×3 (EIM overview, remediation & liability, 2024 features) |
| EnFlection | Trihydro | consultancy-built environmental data system of record for site remediation / post-closure monitoring across US state programs | Tier-1 official product page ×1 |
| (TerraBase) | Tri-Coder | DoD-contaminated-site data management — **not reached (403)** | none — no claims |
| (Azimuth) | Trihydro | agency-side program platform — appears retired/replaced by EnFlection; not directly documented | none — no claims |

Domain context (non-product, regulatory canon):
- UK GOV.UK Land Contamination Risk Management (LCRM) — Environment Agency (+NIEA/SEPA/NRW): the 3-stage process canon (Stage 1 risk assessment, Stage 2 options appraisal, Stage 3 remediation and verification), incl. Part 2A contaminated land regime.

## Sources

Fetched 2026-09-07 (all Layer A unless noted):

- ESdat root — https://esdat.net/
- ESdat Government — https://esdat.net/government/
- ESdat Environmental Guidelines / Action Levels — https://esdat.net/environmental-standards/
- ESdat case study: NZ Department of Defence — https://esdat.net/nz-department-of-defence-manage-their-contaminated-sites-data/
- EarthSoft EQuIS Professional — https://earthsoft.com/products/professional/ (earthsoft.com/products/equis/ redirected to a training page; Enterprise page not fetched, product-family structure evidenced from site navigation — Tier-2)
- Locus EIM overview — https://www.locustec.com/applications/environmental-information-management/
- Locus EIM Remediation & Environmental Liability Management — https://www.locustec.com/applications/environmental-information-management/remediation/
- Locus blog "EIM Top Enhancements and Features in 2024" — https://www.locustec.com/products/eim/ (redirected to blog)
- Trihydro EnFlection — https://www.trihydro.com/digital-services/enflection/
- Trihydro Digital Solutions index — https://www.trihydro.com/software (Azimuth absent from current product line)
- GOV.UK LCRM — https://www.gov.uk/guidance/land-contamination-how-to-manage-the-risks

Unreachable / abandoned (recorded per source-access limitation; no claims rest on them):

- TerraBase (terrabase.com) — 403 ×1, abandoned
- Washington Ecology Cleanup Site Search (apps.ecology.wa.gov/cleanupsearch) — 403 ×1, abandoned
- Minnesota PCA "What's in My Neighborhood" — 404 ×1, abandoned
- Esdat /consulting/, /esdat-features/ pages not fetched (root already carried the feature set)
- EarthSoft Enterprise page not fetched (structure taken from official navigation — Tier-2 for Enterprise claims)

## Product Observations

### ESdat (EScIS) — Key observations

Evidence: A (directly observed on fetched pages).

- Positioning: "helps scientists and engineers import, manage, analyze and report data from laboratories, field programs, data loggers, sensors, historical sources, and regulatory standards" — for "site investigation, monitoring, and compliance data".
- Client base spans consultancies (Arcadis, AECOM, Stantec, Geosyntec, Tetra Tech, Golder, WSP, GHD), miners (Rio Tinto, BHP, MMG), and governments (Australian Dept of Defence, DCCEEW, NSW, Queensland, NT; Canadian Forces; NZ Defence via case study).
- Laboratory integration: "Laboratories around the world are assessed and approved to upload their reports to ESdat where the data is validated, loaded and ready for analysis and reporting" — validated electronic lab deliverable ingestion as a central mechanism.
- Environmental standards: "pre-compiled library of regulatory guidelines" — US/Canadian/Australian/NZ/UK action levels pre-loaded; users add own standards or site limits; real-time exceedance alerts; pH/hardness/depth and matrix dependencies supported; comparison on chemistry tables, maps, graphs.
- Exceedance tables: "Chemistry summary tables show analytical results compared against environmental standards"; exceedance notifications on load; reminders for upcoming/overdue monitoring.
- QA machinery: track holding times, RPD values, detects in blanks, ionic balance, "other quality indicators".
- Statistics: mins/maxes/std devs/95th percentiles; export to ProUCL.
- Field programs: plan, execute, report "all stages of large or recurring field programs"; logger data review with alerts and flagging; bore logging (borehole, geology, groundwater) with automated bore log generation.
- Maps: data points over built-in satellite imagery or own basemaps.
- Outputs: Power BI, ArcGIS, Excel, Web API feeds; public portal to "publish approved results on the web to meet reporting obligations".
- Government page: third-party data intake (receive/validate/import submissions from external agencies and private sector partners); complete data governance (track data origin, metadata, edits, use constraints, permissions); standardized workflows to normalize naming/units across sources; map-driven interface for technical and non-technical users; ISO 27001 / SOC 2 posture.
- NZ Department of Defence case study: custodian of a number of sites subject of contaminated site investigations; multiple consultants collect data; all lab and field results digitally loaded into the custodian's own system, quality reviewed, available for reporting through ESdat and internal systems such as ArcGIS.
- Testimonials reinforce: "long-running sites (historical data)", "management of sample data", "analyzing contaminated lands data", "EPA Appointed Contaminated Sites Auditor" users.

### EQuIS (EarthSoft) — Key observations

Evidence: A for Professional page; B/Tier-2 for Enterprise product-family structure (navigation only).

- Positioning: "checking, editing, loading, reporting, and visualizing environmental and sample data… advanced tools for environmental scientists and engineers to review analytical chemistry, geology, and other environmental data".
- Professional tools listed: reference value management; action level and regulatory guideline management; import formats and rules — supports GeoTracker (California state program) and ERPIMS (US Air Force) among others; advanced crosstab report engine; query building; Esri GIS, Bentley gINT, AutoCAD and other third-party exports; EnviroInsite for visualization and subsurface graphics; user security and schema access; data qualification, verification, and validation support.
- Library packaging: Standard / Data / Graphics libraries plus Decision Support modules.
- Product family (from navigation, Tier-2): EQuIS Enterprise (dashboards & widgets, workflow automation, Enterprise EDP, EQuIS Live, REST API); EQuIS Data Acquisition (EDP, Collect mobile/field, External Data Submitter license); Data Quality Module (DQM); Sample Planning Module (SPM); EQuIS for ArcGIS; EQuIS Geotech; Data Governance; hosting options (implying self-hosted SQL Server as well as hosted).
- The named import formats (GeoTracker, ERPIMS) evidence that agency/regulated-party data flows in state and federal cleanup programs are a core use case.

### Locus EIM — Key observations

Evidence: A (directly observed).

- Positioning: environmental information management platform used by "Fortune 500 companies, water utilities, and the US Department of Energy since 1999"; "EIM software is the science-based engine underneath both [ESG and EHS] — the place where your actual environmental data lives, gets validated, and becomes defensible".
- Data loading: "quickly load water, air, soil, or any other analytical data via multiple EDD formats, FTP, Excel imports, surveys, mobile devices, email, or manual entry"; converts units, flags potential errors, automated data validation.
- Sample Planning Module: build, execute, track "cradle-to-submitted sampling program"; tasks/workflows dispatch field crews to multiple sites at required intervals; flexible scheduling of single or recurring events based on common sampling frequencies; QC sample assignment; requested-analysis tracking; percent-complete views; Locus Mobile sync of field measurements/surveys/notes.
- Multi-site operation (2024 enhancements): multisite query options across GIS+, custom queries, quick views, analytical views, and exceedances — "view every recent benzene exceedance in all your projects… which sites are showing increasing trends in lead concentrations in water samples"; saved/pinned queries; project manager console.
- Remediation & Environmental Liability Management page: "manage multiple data streams throughout your environmental remediation projects and during subsequent operation and maintenance (O&M) of remediation treatment systems"; uses historical data + statistics to optimize wells sampled and reduce sampling frequency; task management (schedule tasks, track maintenance on equipment); calculation engine; configurable dashboards; data upload with validation/error checking/multiple EDD formats/customized valid values; formatted reports incl. integration with TRRP Commander for TCEQ (Texas) reporting; regulatory report formats (DMRs, vapor intrusion, lithology, WQX, CIWQS).
- Platform: multi-tenant cloud SaaS, SSO, SOC 1/2 Type 2; API (JSON/OData, JWT); GIS mapping (ArcGIS online compatible); visualization incl. contours/forecasting charts; vapor intrusion management and PFAS monitoring surfaced as use cases.
- Scale claims (vendor-published counters: 1,893,850 locations, 527,967,158 analytical records) — recorded as vendor claims only.

### EnFlection (Trihydro) — Key observations

Evidence: A (directly observed).

- Positioning: "centralizes data into a secure system of record, enabling controlled access and supporting transparency across stakeholders"; built from environmental project experience; supports "site remediation, post-closure monitoring, active site operations, carbon capture initiatives, and tracking of emerging contaminants".
- Regulatory frameworks named: RCRA, CERCLA, State Programs, NPDES, UIC Class VI.
- Data streams accommodated: groundwater, surface water, stormwater, CO2, leachate, soil sampling, oil/gas, air sampling, field parameters, fluid level, site characterization data.
- Features: interactive maps (visualize sampling data by location); real-time monitoring of project activities, datasets, KPIs; simultaneous access for designated team members; sampling planning ("avoid over-sampling"); define standards and analytical criteria for sample events; organize lab deliverable metadata; load data with method/analyte/unit synonyms aligned to previous datasets; validation tools flag analytical discrepancies; notifications for significant data events; query/filter/compare against regulatory standards or customized thresholds; saved shared queries; reproducible formatted tables/charts; "maintain a consistent record of data, analyses, and reports to support team transitions"; AI natural-language queries restricted to the site's data; role-based access controls; single-tenant Azure; data download/ownership; scale "from single sites to corporate-wide portfolios"; historical data upload service.
- Featured project: Superfund site — laboratory and field analytical data consolidation and management.
- Scale claims (500+ users, 38 states) — vendor-published, recorded as claims only.

### Domain context (GOV.UK LCRM) — Key observations

Evidence: A for the guidance page itself; used as domain canon, not product evidence.

- UK regulators (Environment Agency, NIEA, SEPA, NRW) expect risk management of historic land contamination to follow LCRM: Stage 1 risk assessment → Stage 2 options appraisal → Stage 3 remediation and verification; separate Part 2A contaminated land regime; "competent person" requirement; rapid measurement techniques protocol.
- Confirms the domain's process canon: assess → choose options → remediate → verify — with regulators as the approving parties. The software Types in this leaf orbit this process.

## Cross-product Comparison

| Dimension | ESdat | EQuIS | Locus EIM | EnFlection |
|---|---|---|---|---|
| Unit of record | site/project with locations, samples, results, standards, documents | site/facility + schema of locations/samples/results (facility-id anchored) | site + project + locations + samples/results | site/project as system-of-record container |
| Evidence accumulation | long-running historical data; validated lab loads; QA-tracked | check/edit/load/report workflows; qualification/validation | validation on load; historical data for statistics; "defensible" framing | consistent record supporting team transitions; historical upload service |
| Criteria comparison | pre-loaded guideline library + custom site limits; exceedance tables/maps/graphs; matrix dependencies | reference values; action level & regulatory guideline management | exceedance module (incl. cross-site exceedance queries) | standards + analytical criteria per sample event; comparison vs standards/thresholds |
| Sampling machinery | field programs (recurring); bore logging; logger data | Collect/EDGE field tools; SPM (Tier-2) | Sample Planning Module (recurring events, QC assignment); Locus Mobile | sampling planning; lab deliverable metadata |
| Validation/QA | holding times, RPD, blanks, ionic balance | data qualification/verification/validation (DQM) | automated data validation, error flags, unit conversion | validation flagging of analytical discrepancies; synonyms |
| Location/GIS | maps over satellite/basemaps; ArcGIS feeds | Esri GIS exports; EnviroInsite subsurface graphics | GIS+ (ArcGIS-compatible); contouring | interactive maps by sampling location |
| Lifecycle span | monitoring reminders; long-running sites | program data flows (GeoTracker/ERPIMS formats) | remediation projects → O&M of treatment systems; well optimization | site remediation → post-closure monitoring; project activity tracking |
| Tasks/actions | monitoring reminders; exceedance notifications | workflow automation (Enterprise) | task management; equipment maintenance tracking | notifications for significant data events; project progress tracking |
| Portfolio/multi-site | enterprise multi-department | enterprise schemas | explicit multi-site queries across portfolio | single site → corporate portfolios |
| Public/transparency | public portal publishing approved results | (agency hosting pattern) | (not observed as core) | "transparency across stakeholders" (internal framing) |
| Regulatory formats | regional guideline libraries (US/CA/AU/NZ/UK) | GeoTracker, ERPIMS import formats | TRRP/TCEQ reporting, DMR, WQX, CIWQS, vapor intrusion | RCRA/CERCLA/state/NPDES/Class VI framing |
| Access/governance | permissions, use constraints, ISO27001/SOC2 | user security, schema access | roles, SSO, SOC 1/2 | role-based access, single-tenant |
| AI | (not observed on fetched pages) | (not observed) | AI for EHS marketing; API for BI | natural-language smart queries scoped to site data |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

Three properties. Remove any one and the product is no longer recognizable as contaminated site management:

1. **The contaminated site record** — an identified, located place held as a managed unit because of actual or suspected contamination of its media (soil, groundwater, surface water, sediment, soil vapor, building interiors); its identity persists across years or decades, including after work stops or the site is closed. Remove → generic environmental data system or land registry.
2. **Cumulative site evidence** — the site's understanding is built up over time from dated, attributed investigation and monitoring records attached to the site (assessments, sampling events and analytical results, field measurements, inspections, reports); evidence accumulates and is qualified rather than replacing the record. Remove → a list of names; a one-off lab feed.
3. **Managed progression across the site's environmental lifecycle** — the site's phase of work (investigation/assessment → remediation → monitoring/post-closure → closure) is tracked as managed state advanced by recorded activities and events (sampling events, exceedances, actions, reports), so the site's standing is always expressible. Remove → a static inventory or a raw results archive.

Historical check (§24): pre-software practice — paper site files/registers with a status column, attached sampling reports in date order, map-drawer location indices — satisfies all three properties. Cloud, GIS, EDD automation, AI are NOT definitional. Passed.

### L1 — Common Mature Structure (standard capabilities, cross-product B evidence)

- Location & spatial context: sampling locations/wells/boreholes bound to coordinates; map surfaces; GIS interchange (ArcGIS-class).
- Sampling machinery: planning and scheduling of recurring monitoring events; field data capture (mobile/field tools); field parameters.
- Lab data ingestion & validation: electronic lab deliverable formats, automated loading, unit conversion/synonyms, QA/QC checks (holding times, duplicates/RPD, blanks, ionic balance), data qualification/flagging.
- Criteria comparison: managed libraries of regulatory guideline values / action levels (regional pre-loading common) + site-specific limits, with matrix/depth dependencies; exceedance tables, maps, graphs; exceedance alerts.
- Analysis & visualization: trend/time-series charts, statistics, contouring/subsurface visualization, crosstab/summary chemistry tables.
- Reporting outputs: formatted, reproducible tables/charts for reports; regulatory-format exports (state/federal program formats).
- Portfolio/multi-site operation: cross-site queries and roll-ups; enterprise scale.
- Document & record retention: system-of-record posture, historical data retention, continuity across staff/consultant turnover.
- Notifications: exceedance alerts, monitoring reminders, significant-data-event notices.
- Task management: remediation-phase and O&M-phase tasks (equipment maintenance, sampling tasks) — evidenced in 2/4 sampled products directly, present as workflow automation in a third.
- Access control & governance: roles/permissions, audit/governance of edits and provenance; security certification posture.
- Integration spine: GIS, BI (Power BI/Tableau-class), Excel, APIs, agency reporting endpoints.
- Public/transparency surfaces: publishing approved results (public portal at one product; stakeholder transparency at another) — common in agency-facing deployments, not universal (see L2).

### L2 — Variant / Optional Structure

- Operator pole: consultant workbench (per-project data management) vs owner/custodian portfolio (defense/industrial custodians consolidating multi-consultant data) vs agency/program platform (regulator receiving third-party submissions, running cleanup programs).
- Center-of-gravity pole: data-led (lab-data engine first) vs record/case-led (site register, status, program workflow first). The sampled population leans data-led; the register-led agency pole is inferred structurally (see Uncertainties).
- Regulatory regime packaging: US state/federal cleanup programs (GeoTracker, ERPIMS, TRRP/TCEQ, RCRA, CERCLA, NPDES), UK LCRM/Part 2A context, AU/NZ/CA guideline libraries; regional realization, not definition.
- Program context: petroleum/LUST, industrial/chemical, defense/military, mining, landfills, emerging contaminants (PFAS), vapor intrusion, carbon capture (Class VI) as data-stream contexts.
- Scale & delivery: single-site SaaS → multi-tenant enterprise SaaS → self-hosted SQL Server deployments; lab-specification ecosystems.
- AI assistance: natural-language querying scoped to site data (one product); AI marketing posture (another).
- Public portal / public registry output depth.

### L3 — Vendor-specific (research notes only; NOT in final document)

- ESdat: EScIS branding; LabSync; Aquadata public portal (Shoalhaven Council); ProUCL export; "assessed and approved" lab onboarding program; specific testimonial quotes; ISO 27001/SOC 2 badges.
- EQuIS: Professional/Enterprise product split; Standard/Data/Graphics/Decision-Support library packaging; module names EDP, EDGE, Collect, DQM, SPM, EnviroInsite, Risk3T, EQuIS Live, EQuIS for ArcGIS/gINT/AutoCAD; named GeoTracker and ERPIMS formats; Active Reports embedding; VB.NET/SQL Server stack; GSA contract; hosting options menu.
- Locus: EIM/EIMone product names; Expert/Intermediate/Quick/Analytical query module names; GIS+; TRRP Commander integration name; TCEQ/DMR/WQX/CIWQS format names; Locus Mobile; vendor counters (1,893,850 locations / 527,967,158 analytical records); 99.992% uptime claim; blockchain/AI marketing language.
- EnFlection: registered trademark product name; 500+ users / 38 states / 100% renewal claims; Class VI CO2 streams; single-tenant Azure architecture; smart-query AI.

## Vendor-specific Findings

See L3. The named state/federal formats (GeoTracker, ERPIMS, TRRP/TCEQ) are product-specific realizations of the standard "regulatory-format export" capability and must not be promoted to the definition.

## Rejected Findings

- **"Contaminated site management = environmental data management."** Rejected as a collapse: all four sampled products are data-led, but the leaf's distinguishing frame is the site as unit of record with lifecycle and long-term retention toward closure. The data machinery is the standard instrument of the Type, not the definition. (Boundary recorded below; joint review with environmental-data-platform recommended.)
- **GIS/mapping as definitional.** Rejected — historical registers were map-drawer/paper-map based; maps are standard, not defining.
- **Public portal as definitional.** Rejected — owner-side deployments are commonly confidential; publishing is a deployment-facing variant.
- **EDD/lab automation as definitional.** Rejected — manual entry paths exist in sampled products.
- **AI/NLQ as definitional.** Rejected — era-typical addition.
- **Multi-decade analytics/statistics as definitional.** Rejected — analytical depth varies; the retention discipline is definitional, the statistics are not.
- **Remediation project scheduling/execution as definitional.** Rejected — full remediation project management (schedules, contractors, cost) belongs to the remediation-management sibling; sampled products carry remediation as data streams + tasks, not as full project execution machinery.

## Boundary Findings

1. **vs Environmental Data Platform (§21 sibling, unprocessed) — the sharpest seam.** The sampled products are simultaneously the strongest candidates for that leaf. Proposed discriminator: contaminated site management centers the *site* as the unit of record — identification, lifecycle progression, evidence accumulation toward closure, long-term retention — where the data corpus exists to establish and defend the site's condition. An environmental data platform centers the *data corpus* itself across any environmental program (compliance monitoring, water quality, air) without requiring a contamination frame. Joint review recommended when that leaf is processed. Candidate outcomes: keep-both with site-lifecycle seam (current framing), or re-scope this leaf's population toward register/case-led products.
2. **vs Environmental Site Assessment (§21 sibling, unprocessed).** ESA = the assessment process/fieldwork application (Phase I/II investigation); here an assessment is a record attached to the site and its results are ingested as evidence. Remove the assessment-execution machinery and what remains is this Type's record; remove the site-centered record and what remains is ESA. Handoff, not overlap.
3. **vs Environmental Remediation Management (§21 sibling, unprocessed).** Remediation management = execution of remediation projects (plans, contractors, treatment systems, schedules). Here remediation appears as a lifecycle phase plus its data streams and tasks; one sampled product explicitly spans "remediation projects and subsequent O&M" (blur zone recorded — that product is the overlap specimen).
4. **vs Environmental Monitoring Platform (§21 sibling, unprocessed).** Monitoring platform = ongoing monitoring of operating facilities/parameters; here monitoring is the post-closure/long-term phase of a contaminated site (monitoring wells, trend evaluation against cleanup criteria). Overlap at long-term monitoring programs.
5. **vs Environmental Incident Management / Waste Management / Hazardous Materials Management.** Spills are one discovery path into this Type (the site record begins); waste logistics manage materials, not sites. No merge.
6. **vs Government GIS / Land Records / Cadastre (§24).** The spatial base (parcels, coordinates) is consumed as context; ownership of the site record lies with the contamination frame, not the cadastral frame.
7. **"Remove-what" tests:** remove site anchoring (results without sites) → lab data management / environmental data platform; remove lifecycle/status (static list of sites) → inventory; remove evidence accumulation (no sampling/results history) → property/land register; remove retention after closure → active casework system.

## Uncertainties

- **Agency/register pole under-evidenced.** Regulator-side cleanup-site registers (status codes, public site lookup, no-further-action listing) were not directly documented: TerraBase 403, Washington Ecology portal 403, MPCA 404, Azimuth apparently retired. The register pole is inferred structurally from: ESdat government page (third-party intake, defensible data for government decisions), EQuIS named state/federal formats (GeoTracker/ERPIMS), LCRM's regulator-facing process canon, and EnFlection's "system of record… transparency across stakeholders". All register-pole claims in the final document are written at moderate/qualified strength.
- **Closure formalities** (closure letters, no-further-action determinations as explicit record states) were not directly verified in any fetched product documentation; written conceptually.
- **Financial liability machinery** (costs, reserves, liability accounting) appears only as Locus's "environmental liability management" framing; depth unverified — kept out of standard capabilities, noted as variant direction.
- **Enterprise/EQuIS Enterprise claims** (dashboards, workflow automation, REST API) rest on official site navigation, not fetched page content (Tier-2).
- **Direct owner-side portfolio products** (pure contaminated-land portfolio managers for property owners/lenders) were not found as standalone products in this pass; the owner pole is evidenced via the NZ DoD custodian case study.

## Final Synthesis

The Type is a **site-centered system of record for contaminated land and water**. Its world: sites (identified places with contamination concerns) → contamination profiles (suspected vs confirmed, contaminants × media) → evidence (assessments, sampling events, lab/field results, documents — validated, qualified, accumulated) → managed progression (investigation → remediation → monitoring/post-closure → closure) → the retained register (sites kept as records after closure). The standard instrument set: guideline/action-level comparison with exceedance machinery, validated lab-data ingestion, sampling/monitoring scheduling, maps/GIS, reporting to regulatory formats, portfolio/multi-site operation, roles/governance. Two dominant realizations: the consultant/custodian data workbench (the sampled market's center of gravity) and the agency cleanup-program register (structurally inferred this pass). The Type stands as distinct from Environmental Data Platform on the site-lifecycle seam, pending joint review.
