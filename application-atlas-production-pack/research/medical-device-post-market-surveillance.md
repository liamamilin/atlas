# Research Notes — Medical Device Post-market Surveillance

## Research Goal

Understand what "Medical Device Post-market Surveillance" actually is as an Application Type: what record world the software maintains for devices already on the market (complaints, adverse events/incidents, malfunctions, field feedback), how reportability and regulator-facing reporting work, how population-level trending/signal analysis and post-market clinical follow-up (PMCF) fit, who uses it, and where its boundaries run against Life Sciences QMS, Medical Device Lifecycle Management, Pharmacovigilance Platform, CAPA Management, Complaint & Escalation Management, and Regulatory Information Management.

## Initial Boundary

- **Working hypothesis (Step 1)**: the medical-device manufacturer's post-market safety/vigilance system of record — field events captured from the market, assessed for reportability, reported to regulators, trended across the device population, and fed back into risk management and CAPA.
- **Nearest types**: Life Sciences QMS (§22, processed — quality-event/action loop as the quality system's evidence of record; complaints appear there as one quality-event class), Medical Device Lifecycle Management (§22, processed 2026-09-08 — pre-hung seam: "vigilance/safety loop over the marketed device (complaints, adverse events, trend reporting, PMCF) as its own record world vs this Type's design chain with post-market linkage as the downstream leg feeding changes"), Pharmacovigilance Platform (§22, unprocessed — same loop shape for drugs), CAPA Management (§16, processed), Complaint & Escalation Management (§07, processed — generic customer complaints), Regulatory Information Management (§22, unprocessed — submissions/dossiers estate), Clinical Trial Management / EDC (§22, processed — PMCF studies may run on clinical machinery).
- **Unknowns**: whether the market sells this as a distinct product category (vs. a module inside eQMS or a safety platform); whether the leaf is an alias of the device pole of Life Sciences QMS; which record classes are definitional vs regime-specific (PMCF, PSUR-class periodic reports); how the device subject attaches (UDI/lot/serial).

## Research Questions

1. What record classes does the software actually carry (complaints, adverse events/incidents, malfunctions, vigilance cases, PMCF studies, periodic summary reports)?
2. What is the unit of record — the event, the case, the report?
3. How does reportability determination work in the software (criteria, rules, timelines, submission tracking, acknowledgement)?
4. How does the marketed device attach to events (product/family, lot/serial, device-linked surveys)?
5. How does the loop close back into risk management and CAPA?
6. Who uses it (complaints team, vigilance/medical safety, QA/RA, product development)?
7. What is the boundary vs Life Sciences QMS (complaints as quality events), vs Pharmacovigilance Platform (drug side), vs Medical Device Lifecycle Management (design chain), vs CAPA Management, vs Complaint & Escalation Management?
8. Is the leaf a real Type or a module/alias?

## Representative Products

Selected to span market structure (device-native mid-market eQMS / enterprise QMS suite / enterprise safety platform / EU multivigilance specialist), with different product philosophies and customer tiers:

1. **Greenlight Guru** — device-native eQMS platform; sells "Managing Postmarket Quality" as an initiative and Complaint Management + Post-Market Clinical Surveys (PMCF) as named modules. Mid-market device companies.
2. **MasterControl** — enterprise QMS suite for regulated manufacturing; sells **Postmarket** as a named add-on ("Postmarket Excellence") beside Quality/Manufacturing/Asset suites. Enterprise life-sciences manufacturers.
3. **ArisGlobal LifeSphere** — enterprise safety/regulatory platform family; **MultiVigilance** (case processing) + **Product Complaints** (complaint intake unified with Quality, Safety, Medical Information). Large pharma/device/health-authority customers.
4. **AB Cube SafetyEasy Suite** — EU-based multivigilance platform (Pharmacovigilance, **Medical Device Vigilance**, Cosmetovigilance, Nutrivigilance, Biovigilance); modular, priced by annual case volume; serves biotechs, CROs, health authorities, cosmetics/nutraceutical and device-adjacent companies.

Rejected/abandoned: Oracle Argus Safety (device module) — product URL 404 on first fetch, abandoned per network rules; Sarjen — root nav shows pharmacovigilance but no device-vigilance surface on the fetched page, dropped as a sample.

## Sources

All fetched 2026-09-08 (Tier 2 official product/solution pages; no Tier-1 help-center articles were reachable in this pass — see Sourcing Limitation):

- Greenlight Guru — root/platform nav; "Managing Postmarket Quality" (https://www.greenlight.guru/postmarket-surveillance-medical-device); Complaint Management (https://www.greenlight.guru/complaint-management-software); Post-Market Survey / PMCF (https://www.greenlight.guru/post-market-survey)
- MasterControl — root nav; Postmarket (https://www.mastercontrol.com/postmarket/)
- ArisGlobal — root nav; LifeSphere MultiVigilance (https://www.arisglobal.com/lifesphere/safety/multivigilance-system/); Product Complaints (https://www.arisglobal.com/product-complaints/)
- AB Cube — SafetyEasy Suite root (https://www.ab-cube.com/); SafetyEasy Vigilance (https://www.ab-cube.com/vigilance/)

**Sourcing Limitation**: vendor help centers / user guides were not fetched in this pass (login-gated or not attempted within budget); evidence is product/solution-page depth. Per evidence rules, precise operational details (exact reporting timelines, specific form names beyond those printed on fetched pages, numeric thresholds, plan gating) are NOT asserted in the final document. The AB Cube vigilance page is the deepest source (feature-level lists); Greenlight Guru pages include FAQ-level operational statements.

## Product A — Greenlight Guru (device-native eQMS pole)

### Key observations (Evidence Layer A — direct from fetched pages)

- Positioning: "The #1 QMS for Medical Devices"; platform = Quality Management + Product Development + Clinical Evidence. "Managing Postmarket Quality" is one of six named initiatives; "Post-Market" is a named org-type solution.
- Post-market framing: "Establish robust postmarket quality processes with a powerful QMS so your team is ready when a complaint surfaces or an auditor comes knocking." Post-market quality = CAPA, Audit, Nonconformance, and Complaint handling processes.
- Complaint Management module: "Customer feedback and complaint management is a key part of postmarket surveillance." Capture/document/log all types of customer feedback including complaints; automate the complaint workflow inside the QMS; "Quickly determine whether feedback requires immediate action and if regulatory reporting is required. Automatically set a task for someone to generate the report to send to the FDA and document your decision for future reference."
- Interlinking: "Capture feedback and complaints in the same system as your product's design, management, and risk with interlinking capabilities so you can see everything impacted by customer feedback."
- Escalation: "If a complaint is identified as a systemic issue, you can escalate it to a CAPA."
- FAQ (postmarket page): "The system is designed to identify complaints, adverse events, or quality signals that meet your predefined thresholds and route them into CAPA or further investigation workflows." Legacy complaint/feedback data can be migrated for "trend analysis, and full visibility across past and current post-market activity."
- PMCF leg: Post-Market Clinical Surveys — "Collect scientifically valid and compliant post-market data … specifically built for medical device and diagnostics post-market surveys under EU MDR and FDA"; "pre-validated per ISO 14155:2020 and enables GCP compliance out-of-the-box"; collects "patient outcome measures, safety and vigilance data, usability and clinical experience, survey or registry data under post-market surveillance"; surveys can be "fully anonymous, partially anonymous, or linked to a specific subject or device profile"; distribution via email/SMS/QR; longitudinal tracking; eConsent; built on the vendor's Clinical EDC platform.
- Compliance posture: 21 CFR Part 11 compliant review/approval workflows; audit-ready records.
- Teams named: Product Development (root cause, investigative studies), Quality (complaint process, visibility into quality issues), Leaders (escalation decisions).

### Reading

The eQMS pole realizes post-market surveillance as: complaint/feedback records + reportability determination + FDA-report task generation + CAPA escalation + trend analysis + PMCF survey data collection — all inside the quality system, interlinked with design and risk. No named adverse-event case-processing or E2B-exchange machinery appears on the fetched pages (adverse events appear as signals routed to CAPA/investigation).

## Product B — MasterControl (enterprise QMS suite pole)

### Key observations (Layer A)

- **Postmarket** is a named add-on in the Quality Excellence Suite (beside Supplier, Regulatory, Clinical, Data & Analytics add-ons).
- "MasterControl improves product quality and safety with an integrated, closed-loop system designed to help you proactively manage postmarket surveillance processes and customer feedback throughout your regulated product's lifecycle."
- "MasterControl puts the power of postmarket surveillance in the palm of your hand, allowing you to simultaneously manage product safety and ensure quality compliance."
- Proactively Mitigate Risk: "robust reporting tools that keep you up to date by tracking customer feedback according to product groups, elapsed times, average times and responses pending regulatory acknowledgement."
- Connect The Dots, Close The Loop: "MasterControl integrates postmarket activities and customer feedback in one system to help you improve issue tracking, analysis and risk management."
- Link Safety And Quality With A Single Action: "MasterControl seamlessly unites postmarket surveillance activities with core quality processes to enable you to effectively manage risk and ensure compliance."
- Referenced data sheets: "MasterControl Customer Complaints"; solution overview "MasterControl Postmarket Excellence."
- Platform context: Quality Event Management, CAPA, Deviations, Nonconformance, Risk are sibling modules; Medical Device is a named industry solution (eDHR etc.).

### Reading

The enterprise-QMS pole realizes post-market surveillance as a closed-loop add-on: customer complaints + feedback tracking (by product group, elapsed time, pending regulatory acknowledgement) + analysis/risk management + unification with core quality processes. Same center of gravity as Greenlight Guru's pole, packaged as a suite add-on.

## Product C — ArisGlobal LifeSphere (enterprise safety platform pole)

### Key observations (Layer A)

- LifeSphere family: Safety / Regulatory / Medical Affairs / Quality. Safety nav: MultiVigilance, Advanced Intake, Literature Intelligence, ReporterX, Advanced Signals, Business Intelligence, Document Distribution, Advanced Compliance Docs.
- **MultiVigilance**: "the industry's first and leading end-to-end automated touchless case processing system, built to help safety teams worldwide achieve scalable, efficient, and harmonized case management while improving patient safety and compliance." Features: end-to-end automation "from intake to submission"; "most robust, up-to-date support for global and regional regulations available," including "the FDA's E2B(R3) requirements"; "single, harmonized global database"; format-agnostic intake (structured, semi-structured, unstructured); AI translation. Page title frames it as a drug safety system; "MultiVigilance" names the multi-domain vigilance scope.
- **Product Complaints**: "a single, structured system to capture, manage, and process product quality complaints, including those associated with adverse events." Multi-channel intake (emails, call centers, field representatives, portals); mobile/web reporting for "consumers, HCP's, patient support programs, and other users"; end-to-end workflow "across intake, data validation, classification and assessment"; "ensure regulatory timelines and escalation requirements are met"; audit trails; "Seamlessly bring together Quality, Safety, and Medical Information processes … This includes establishing direct linkage between product complaints and adverse event cases"; future: "AI-driven complaint classification, automated detection of adverse events within complaints."
- Positioning: "220 organizations … including leading biopharmaceutical firms and regulatory bodies such as FDA, Health Canada, and NMPA."

### Reading

The safety-platform pole realizes the same loop from the pharmacovigilance side: case processing (intake → validation → classification/assessment → submission) with E2B exchange, plus a complaint layer that links product complaints to adverse-event cases and routes escalations under regulatory timelines. The complaint↔AE-case linkage is explicit. Device-specific artifacts are not itemized on the fetched pages (MultiVigilance's device scope is implied by the name and the vendor's health-authority customer base; held at weaker strength).

## Product D — AB Cube SafetyEasy Suite (EU multivigilance pole)

### Key observations (Layer A — deepest feature-level evidence in the sample)

- "SafetyEasy® Suite is AB Cube's all-in-one ecosystem for automated multivigilance management … a modular, cloud-based platform that automates every step of the vigilance process, from early stage data capture to regulatory reporting and advanced analytics." "a flexible platform for Pharmacovigilance, Device Vigilance, and beyond."
- Modules: **IntakeEasy** ("Seamlessly capture adverse events from any channel (email, literature, form, and beyond) and automatically create cases"); **SafetyEasy Vigilance** ("Manage all vigilance types in one compliant platform with built-in automation and global reporting tools"); **SafetyEasy BI** ("Visualize safety data with dynamic dashboards for compliance tracking, insights, and smarter decisions").
- Vigilance flow: Capture Cases (import safety data from multiple sources) → Automate Workflows (rules, automated coding) → Ensure Compliance (generate reports aligned with global standards) → Gain Insights (detect signals and track trends across domains).
- Data Management features: "E2B R2/R3 import, export, and validation; Gateway integration; MedDRA & SMQs; IME list support; **HL7 Gateway for medical devices**; MedDRA recoding."
- Signal Detection: "PRR, ROR, qualitative analysis; FDA combination product support."
- Regulatory Reporting: "PSUR, DSUR, PBRER, PADER; **MDCG 2020-10/2, MDCG 2024-04**; Ad-hoc queries; IME list support; Customized reports." (MDCG-numbered templates = EU medical-device-regulation guidance artifacts.)
- Automation: "Customized Workflows; **Reportability Matrix**; Automatic labeling & submission; Duplicate checks; Translation tools; Customized lists; Customized Anonymization." Advanced: "Dynamic Reportability Matrix: Create rules to automatically route cases to your partners based on global reporting requirements."
- Supported Vigilance Types: Pharmacovigilance, **Medical Device Vigilance**, Cosmetovigilance, Nutrivigilance, Biovigilance.
- Lifecycle coverage: "Clinical trials (Phase I–III) … Post-authorization studies (Phase IV) … **Post-marketing surveillance: Track spontaneous reports, literature cases, and patients feedback** … Other studies."
- FAQ: "SafetyEasy® is a pre-validated, cloud-based safety database designed to manage adverse event reporting across clinical and post-marketing phases." Pricing "based on the number of adverse events (cases) processed annually & the number of vigilances selected," with volume-tiered packages (Entry ≤20 cases/year … Intensive >1000 cases/year).
- Compliance: "pre-validated framework aligned with GAMP®5 and FDA CFR21 Part 11."
- Clients include a health authority (ANSM logo) and device-adjacent manufacturers (dental, medical gases).

### Reading

The multivigilance pole is the clearest evidence that device vigilance is sold as a domain of a safety-case platform: case capture from any channel, automated coding, reportability rules routing cases per global reporting requirements, E2B exchange plus a device-specific HL7 gateway, EU-MDR-guidance report templates alongside drug-regime periodic reports, and signal detection/trend tracking. The device domain is one configuration of the same case machinery.

## Cross-product Comparison

| Structure | Greenlight Guru | MasterControl | ArisGlobal LifeSphere | AB Cube SafetyEasy |
|---|---|---|---|---|
| Marketed device/product as surveillance subject | ✓ (complaints interlinked with product design/risk; surveys linked to device profiles) | ✓ (feedback tracked by product groups) | ✓ (centralized complaints repository unified across the product lifecycle) | ✓ (vigilance domains per product; FDA combination-product support) |
| Field event capture (complaints/feedback) | ✓ (capture/document/log all customer feedback incl. complaints) | ✓ (customer complaints; feedback tracking) | ✓ (multi-channel intake: email/call center/field reps/portals; mobile+web reporting) | ✓ (IntakeEasy: any channel → auto-create cases; spontaneous reports, literature, patient feedback) |
| Adverse-event / incident case processing | partial (adverse events as signals routed to CAPA/investigation; no named AE-case module on fetched pages) | not on fetched pages | ✓ (direct linkage between product complaints and adverse event cases; MultiVigilance case processing) | ✓ (case management: E2B import/export, coding, follow-up narratives) |
| Reportability determination | ✓ ("determine whether … regulatory reporting is required"; decision documented) | ✓ (tracking of "responses pending regulatory acknowledgement") | ✓ ("ensure regulatory timelines and escalation requirements are met") | ✓ (Reportability Matrix: rules route cases per global reporting requirements) |
| Regulator-facing report generation/submission | partial (auto-set task to generate the report to send to the FDA) | partial (acknowledgement tracking) | ✓ (automation "from intake to submission"; E2B(R3)) | ✓ (E2B R2/R3 + gateway integration; MDCG-numbered device templates; automatic labeling & submission) |
| Trend / signal analysis | ✓ (predefined thresholds; trend analysis over migrated history) | ✓ (reporting by product groups, elapsed times, average times) | ✓ (product quality trends, earlier risk identification; Advanced Signals module) | ✓ (PRR/ROR signal detection; dashboards; trend tracking across domains) |
| PMCF / post-market clinical data collection | ✓ (Post-Market Clinical Surveys, ISO 14155, EU MDR/FDA; device-linked) | not on fetched pages (Clinical add-on exists in suite) | not on fetched pages | partial (post-marketing surveillance stage: spontaneous reports, literature, patient feedback; post-authorization studies) |
| Feedback into quality loop (CAPA/risk) | ✓ (escalate systemic complaints to CAPA; interlink with design/risk) | ✓ ("Link Safety And Quality With A Single Action"; unites postmarket with core quality processes) | ✓ (unified with Quality, Safety, Medical Information) | partial (cross-vigilance intelligence; quality-system linkage not explicit on fetched pages) |
| Regulated-record posture | ✓ (21 CFR Part 11, audit-ready) | ✓ (GxP platform) | ✓ (audit trails, inspection readiness) | ✓ (GAMP5, Part 11, pre-validated) |

**Cross-product commonalities (Layer B)**: field-event capture from multiple channels; the event as individually identified, investigated/assessed record; reportability determination with documented decisions; regulator-facing reporting tracked to acknowledgement; trending/analysis across events; feedback into quality/risk processes; regulated-record posture (attributed, traceable, audit-ready).

**Pole differences (Layer A)**: the eQMS/QMS poles center complaints + quality-event escalation + PMCF surveys; the safety-platform poles center case processing + E2B/gateway exchange + signal detection. The complaint record is the shared spine; the safety-exchange machinery (E2B, gateways, reportability matrices) is the safety pole's depth; the PMCF/clinical leg is the device-native pole's depth.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The marketed device as the surveillance subject of record** — persistent, individually identified records of the marketed device (or device family) under surveillance; field events, reports, and post-market data all attach to it. Remove → a complaint log or safety case system with nothing device-shaped at the center.
2. **The field safety event of record** — complaints, adverse events/incidents, malfunctions, and other field feedback arriving from outside the manufacturer (users, healthcare providers, distributors, call centers, literature, registries) held as individually identified records, each investigated and assessed. Remove → a product registry with no event record; the surveillance input is gone.
3. **The regulatory safety loop over events** — each event assessed against the regime's reportability criteria with the decision documented; reportable events produce regulator-facing reports/submissions tracked to acknowledgement; events are trended/analyzed across the device population and findings feed back into risk management and corrective action. Remove → customer-service complaint handling (no regulatory safety loop), or per-event case processing with no population-level surveillance.

**Jointly-held is load-bearing**: 1 alone = device/product registry; 2 alone = complaint log / feedback tracker; 3 without 1+2 = a reporting rules engine with nothing to report on; 1+2 without 3 = complaint handling (QMS complaint module / Complaint & Escalation Management territory); 2+3 without 1 = generic safety/vigilance case system (pharmacovigilance territory); 1+3 without 2 = reporting machinery with no field input.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Multi-channel intake (email, call center, field representatives, portals, mobile/web reporting forms)
- Adverse-event case processing with medical coding and structured exchange (E2B R2/R3-class; device-specific gateways such as an HL7 gateway for medical devices)
- Reportability rules engines / matrices; automatic labeling & submission; duplicate checks
- Periodic summary reporting (PSUR/DSUR/PBRER/PADER-class; MDCG-numbered device templates) — regime-dependent
- Trend/signal analysis (thresholds, PRR/ROR-class statistics, dashboards, BI)
- CAPA/risk/design linkage (escalation of systemic events; interlinking with the device's design and risk records)
- PMCF data collection (post-market clinical surveys/studies, device-linked, GCP-grade) — EU-MDR-era emphasis
- Literature monitoring; registry data
- Audit trails, e-signatures, Part 11/GAMP5 validation posture
- AI assistance (intake classification, adverse-event detection within complaints, narrative generation) — era-current

### L2 — Variant / Optional Structure

- Packaging pole: eQMS/QMS-embedded (complaints+CAPA+PMCF inside the quality system) vs standalone safety platform (case processing + exchange + signals) vs multivigilance platform (device as one domain among drug/cosmetic/nutri/bio)
- Regulatory regime emphasis: FDA reporting-centric vs EU MDR vigilance-centric vs multi-regime
- Device class: hardware devices, IVDs/diagnostics, SaMD, combination products
- Customer scale: SMB self-serve vs enterprise; pricing by case volume (one sampled vendor)
- Vigilance breadth: device-only vs multi-domain
- PMCF depth: dedicated survey/study machinery vs none on the fetched surface

### L3 — Vendor-specific (Research Notes only)

- Greenlight Guru: Post-Market Survey built on its Clinical EDC platform; "90-second" study-builder claim; white-labeling; SMS subject validation; ROI stats ($125k saved per project, etc.) — marketing claims, not structural.
- MasterControl: "Postmarket Excellence" module name; Insights analytics add-on; eDHR/MES sibling suite.
- ArisGlobal: NavaX AI agents (MedDRA coding, signals, distribution); RapidPV packaged offering; ReporterX; "touchless case processing" branding; health-authority customers (FDA, Health Canada, NMPA).
- AB Cube: volume-tiered packages (≤20 … >1000 cases/year); unlimited-users pricing; IME list support; customized anonymization; specific MDCG template numbers printed on the page.

## Vendor-specific Findings

See L3 above. Additionally: Greenlight Guru's postmarket page frames the discipline as "postmarket quality" (CAPA/Audit/NC/Complaint workspaces) — a vendor framing of the same record world; MasterControl's page uses "postmarket surveillance processes and customer feedback" — closer to the leaf name. The leaf name itself ("post-market surveillance") is the discipline name used across all four vendors' pages, not one vendor's branding.

## Boundary Findings

- **vs Life Sciences QMS (§22, processed)** — keep-both RATIFIED from this side. eQMS centers the quality-event/action loop (deviations, NCs, CAPAs, audits as the quality system's evidence of record); this Type centers the field-safety-event → reportability → surveillance loop over marketed devices. Complaints appear in both: in eQMS as one quality-event class; here as the primary safety record class with reportability consequences. The safety-platform pole (ArisGlobal, AB Cube) is clearly not a QMS, confirming the Type is broader than the eQMS device pole. Vendor-side confirmation: MasterControl sells Postmarket as a separate named add-on beside its QMS modules; ArisGlobal sells Product Complaints and MultiVigilance as separate products from LifeSphere Quality.
- **vs Medical Device Lifecycle Management (§22, processed 2026-09-08)** — DISCHARGES that pass's forward flag from this side: keep-both RATIFIED. That Type = the device's design-control record chain + controlled change (concept → design → market); this Type = the vigilance/safety loop over the marketed device (field events → reportability → trends → PMCF). The linkage is real and bidirectional in the market (Greenlight Guru interlinks complaints with design/risk; MasterControl "connect design, manufacturing, and feedback"), but the centers of gravity are distinct record worlds.
- **vs Pharmacovigilance Platform (§22, unprocessed)** — same loop shape (case processing, E2B exchange, signal detection, periodic reports) over a different regulated object (medicinal products vs medical devices) with different regime artifacts (device vigilance regimes, MDCG templates, device identifiers, PMCF). The multivigilance pole (AB Cube; ArisGlobal MultiVigilance) realizes both domains on one platform as configurations — evidence that the loop machinery is shared while the domain binding differs. JOINT REVIEW recommended when that leaf is processed.
- **vs CAPA Management (§16, processed)** — CAPA is the corrective-action process; here CAPA is a downstream destination: systemic field events escalate into CAPA (Greenlight Guru explicit). CAPA Management centers the action process; this Type centers the field-event/surveillance loop that feeds it.
- **vs Complaint & Escalation Management (§07, processed)** — that Type is customer-service complaint handling for any industry (service recovery, escalation); here complaints are a regulated safety record class whose assessment drives regulator-facing reporting. The regulated-safety binding is the seam; a device manufacturer's complaint module without the regulatory safety loop is that Type, not this one.
- **vs Regulatory Information Management (§22, unprocessed)** — regulator-facing safety reports are produced FROM this Type's event record world; the registration/dossier/submission estate is RIM territory. FORWARD FLAG: proposed seam — RIM = regulatory-affairs system of record (dossiers, registrations, submission planning); this Type = safety-event record world whose vigilance outputs may be filed through regulatory channels.
- **vs Clinical Trial Management / EDC (§22, processed)** — PMCF studies/surveys may run on clinical machinery (Greenlight Guru's Post-Market Survey is built on its clinical EDC platform, ISO 14155-grade). Held as a capability implementation, not the defining core: the PMCF leg is regime-specific (EU-MDR-era emphasis) and absent from the safety pole's fetched surfaces.
- **Removal tests**: remove the device subject → generic safety/vigilance case system or complaint tooling; remove the field-event record → device registry; remove the regulatory safety loop → complaint handling / customer feedback tooling; remove trending → per-event case processing without surveillance; remove the regime anchor (reportability/reporting semantics) → generic quality-event tracking.

## Historical / Market-Sample Check (§24)

- Paper-era manufacturer's post-market file: device/product file + complaint/incident files with reportability determinations + regulator report forms (FDA medical-device reporting era) + complaint trend logs + corrective actions — satisfies all three L0 legs at analog level. Pre-MDR European device-vigilance regimes and pre-cloud safety databases satisfy.
- Early-electronic era: standalone complaint databases and safety databases (case intake → coding → reportability → submission) satisfy without AI, cloud, dashboards, or signal-statistics packages.
- Therefore the canonical abstraction is the record world + regulatory safety loop, NOT any modern machinery: E2B versions, HL7 gateways, AI intake, PRR/ROR statistics, cloud multitenancy, volume-tiered pricing are all standard-NOT-definitional.
- PMCF and MDCG-numbered periodic reports are EU-MDR-era regime artifacts — held as L1/L2, not definitional (the FDA-centric pole satisfies the core without them).

## Uncertainties

- Device-specific artifacts on the safety pole: ArisGlobal's device-vigilance scope is implied by "MultiVigilance" naming and health-authority customers but not itemized on fetched pages; AB Cube provides the explicit device evidence (Medical Device Vigilance domain, HL7 gateway for medical devices, MDCG templates). Device-vigilance depth on the safety pole is held at moderate strength.
- Whether adverse-event case processing is definitional: the eQMS pole's fetched pages show adverse events as signals routed to CAPA rather than a named AE-case module; the safety pole shows full case processing. Held as L1 (common mature structure), with the field-event record (complaints/incidents/feedback) as the definitional unit.
- Exact reporting timelines, form names, and numeric thresholds: not asserted anywhere (no Tier-1 help-center evidence).
- Importer/distributor reporting obligations (EU regime) as a software concern: no direct evidence in the sample; not asserted.
- Trend-reporting as a named deliverable (vs generic trending): AB Cube lists MDCG-numbered templates without titles; not interpreted further.

## Final Synthesis

Medical Device Post-market Surveillance is the medical-device manufacturer's post-market safety system of record. Its defining core is exactly three jointly-held structures: (1) the marketed device as the surveillance subject of record — persistent identified device/family records to which all field events, reports, and post-market data attach; (2) the field safety event of record — complaints, adverse events/incidents, malfunctions, and field feedback captured from outside the manufacturer as individually identified, investigated, assessed records; (3) the regulatory safety loop over events — reportability determination with documented decisions, regulator-facing reports/submissions tracked to acknowledgement, population-level trending/signal analysis, and findings fed back into risk management and corrective action. The market realizes the Type in three packagings — eQMS/QMS-embedded (complaints + CAPA escalation + PMCF surveys), standalone safety platform (case processing + E2B/gateway exchange + signal detection), and multivigilance platform (device as one domain) — across FDA-centric and EU-MDR-centric regimes and device classes (hardware, IVD, SaMD, combination). Complaint handling, adverse-event case processing, periodic summary reports, PMCF, signal detection, AI intake, and the regulated-record posture are the standard capability layer — common but not definitional. The seams to Life Sciences QMS (quality-event center), Medical Device Lifecycle Management (design-chain center), Pharmacovigilance Platform (drug-object same-loop sibling), CAPA Management (action-process center), Complaint & Escalation Management (unregulated complaint handling), and Regulatory Information Management (dossier estate) are all held from this side, with the medical-device-lifecycle-management pass's forward flag discharged.
