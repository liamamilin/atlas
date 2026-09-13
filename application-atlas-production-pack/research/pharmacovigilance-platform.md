# Research Notes — Pharmacovigilance Platform

Research date: 2026-09-09
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1 (internal; not referenced in the final document)

## Research Goal

Understand what a Pharmacovigilance Platform actually is as an Application Type: the system of record used by pharmaceutical companies (marketing authorization holders), CROs offering safety services, and health authorities to collect, process, assess, and report adverse events associated with medicinal products — and to determine which structures are defining vs. merely common in the current market.

## Initial Boundary

Working hypothesis at start:

- Core purpose: drug safety. Collect adverse event reports (spontaneous, clinical-trial, literature, partner/licensee, authority), process each into a structured safety case (ICSR), assess medically, and produce regulator-facing outputs (expedited case reports + periodic aggregate reports) plus safety signal detection.
- Likely users: PV/drug-safety case processors, safety physicians/medical reviewers, coding specialists, QA, PV operations, regulatory affairs; CRO safety teams; national PV centers (regulator side).
- Nearest neighbors: Medical Device Post-Market Surveillance (same loop shape over the device object — a forward flag from that pass recommends joint review), Clinical Trial Management System / EDC (trial SAEs), Regulatory Information Management / RIM, Life Sciences QMS / CAPA, Complaint & Escalation Management, Public Health Surveillance Platform.
- Unknowns at start: whether signal detection is definitional or common; whether aggregate reporting is definitional; the regulator-side realization; how multivigilance products straddle the device boundary.

## Research Questions

1. What is the unit of record? What anatomy does a case carry?
2. What is the case-processing lifecycle in real products (stages, reviews, states)?
3. How do coding terminologies (MedDRA, WHODrug) appear?
4. How do products determine reportability and produce expedited reports? How is E2B exchange handled (outgoing and incoming)?
5. How are periodic/aggregate reports (PSUR/PBRER, DSUR, PADER, IND/NDA) supported?
6. What signal-detection machinery exists — definitional or common?
7. What intake channels exist (spontaneous, email, literature, forms, incoming E2B, trials, medical info)?
8. What roles and review gates exist? What compliance machinery (audit, locks, validation)?
9. How does the regulator-side realization differ (national centers)?
10. How do multivigilance products span drug/device/cosmetic/nutrition domains, and what does that imply for the boundary with Medical Device Post-Market Surveillance?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

1. **Oracle Argus Safety** (Safety One Argus) — the dominant enterprise incumbent; validated classic architecture; public Tier-1 documentation (Oracle Help Center). Serves large pharma and CROs (PrimeVigilance, EVERSANA named as customers on Oracle's PV page).
2. **ArisGlobal LifeSphere MultiVigilance** — cloud-native, automation-first ("touchless case processing"); enterprise + SME tier (RapidPV offering); also serves government health authorities.
3. **AB Cube SafetyEasy** — modular mid-market multivigilance SaaS; SME-to-mid tier; serves biotechs, CROs, health authorities (incl. ANSM in client portfolio), cosmetics/nutraceutical companies; priced per case volume.

Considered and rejected/abandoned:
- **Veeva Vault Safety** — cloud-native pole of interest, but help center and product page both unreachable (timeout/transport error, 2 attempts). Abandoned per network rule; noted as sourcing limitation.
- **UMC VigiFlow** (regulator-side, national PV centers) — who-umc.org paths 404 twice. Abandoned; regulator-side realization documented only indirectly.
- **Ennov Pharmacovigilance** — ennov.com paths 404 twice. Abandoned.
- **EXTEDO "Safety Management Hub"** — turned out to be SafetyEasy powered by AB Cube (reseller page); used as a secondary source for SafetyEasy, not a fourth product.

## Sources

Tier 1 (official operational documentation):
- Oracle Argus Safety Documentation landing page — https://docs.oracle.com/en/industries/health-sciences/argus-safety/ (definition-grade product description)
- Oracle Argus 8.4.1 Get Started — https://docs.oracle.com/en/industries/life-sciences/argus-safety/8.4.1/index.html
- Oracle Argus 8.4.1 Books list — https://docs.oracle.com/en/industries/life-sciences/argus-safety/8.4.1/books.html (component-level documentation titles)
- Oracle Argus Safety User's Guide 8.4.1 TOC — https://docs.oracle.com/en/industries/life-sciences/argus-safety/8.4.1/aeoaf/toc.htm (chapter/section-level structure of case entry, processing, expedited and periodic reporting)

Tier 2 (official product pages):
- Oracle Pharmacovigilance solution page — https://www.oracle.com/industries/life-sciences/pharmacovigilance/
- ArisGlobal LifeSphere MultiVigilance — https://www.arisglobal.com/lifesphere/safety/multivigilance-system/
- AB Cube SafetyEasy Suite — https://www.ab-cube.com/ and SafetyEasy Vigilance — https://www.ab-cube.com/vigilance/
- EXTEDO Safety Management Hub (SafetyEasy by AB Cube) — https://www.extedo.com/software/pharmacovigilance-and-drug-safety

Unreachable (recorded limitations):
- Veeva (help.veevavault.com timeout; veeva.com transport error) — cloud-native pole documented via other vendors' cloud claims instead.
- UMC VigiFlow (who-umc.org 404 ×2) — regulator-side product evidence indirect only.
- Ennov (404 ×2).

## Product A — Oracle Argus Safety (Tier 1, direct observation)

**Landing-page definition (A):** "Use Argus Safety to enter and intake adverse event cases, code medical and product terms, perform medical and quality assessments, and generate expedited and periodic reports for health authorities and partners." — This is a vendor-stated statement of the whole loop: intake → coding → medical/quality assessment → expedited + periodic reporting to authorities AND partners.

**Component constellation (A, from the Books list):**
- Argus Safety (core case management; User's Guide)
- Argus Interchange — "handling of ICSR reports… configuration, validation, viewing, transmitting, monitoring, and import of E2B reports" (bidirectional E2B gateway)
- Argus Dossier — "a tool that works within the Argus Safety application and enables you to generate periodic reports"
- Argus Insight — "create queries, execute queries to generate a case series, and generate reports on the case series" (analytics companion)
- Argus Mart — "analysis and reporting in medical product safety and pharmacovigilance" (data mart)
- Argus Affiliate — "configuration… functions performed by Central Users and Affiliate Users" (partner/licensee exchange)
- Argus Unblinding — trial unblinding application
- Aggregate Reporting (Oracle Analytics Publisher-based)
- Regional best-practice guides: CBER eVAERS, CDER Combination Product, CDRH eMDR (device), China NMPA E2B(R3), EC Manufacturer Incident Report (device), PMDA Japan device reporting + PSR/ReSD, South Korea MFDS E2B(R3), EDQM routes/dose forms — showing both the multi-regime E2B reality and the device straddle at the incumbent.
- Oracle's separate PV page (Tier 2): Safety One Argus (intake, case management, signal detection, regulatory workflows) + Empirica as a separate signal-management product ("data mining, signal detection, and review").

**Case anatomy (A, User's Guide TOC ch. 2):** a case is entered through sections — general information (incl. study information, reporter information, literature information); patient information (current medical status, patient notes/details, pregnancy, death details, other relevant history, lab data, parent); product information (product search incl. WHO Drug Browser; drug tab with dosage regimens, indications, quality control; **device tab** with device components; **vaccine tab** with administration/history); event information (events tab, diagnosis-event relationship, event coding, seriousness criteria incl. death/hospitalization details, event assessment with product-event details); attachments; narrative (implied by FAQs about narrative differences); Japan local data entry.

**Case processing (A, ch. 3):** search/assigned cases; view assigned and unassigned; case workload; workflow status; **route a case to another workflow state**; **add a follow-up event**; **unblind cases to a study**; copy case; **lock or unlock a case**; delete/undelete; **formally close a case**; print; correspondence (generate letters, track correspondence); **case action items** (incl. query-type action items with due dates); **revisions**; **audit log**; coding status; **perform a medical review**; **perform a coding review**; **perform a regulatory submission review**.

**FAQ-level behaviors (A):** case owner and reassignment; when a case becomes open; formally-close conditions; unblinding effect on the study; tracking which revision contains significant follow-up information; comparing two narratives; lock states (local vs global; per-country local locks; Japan local locking); medical review can change outcome and causality; case assessment values; receipt date / aware date / date received semantics; letters carry sent/due dates tied to action items; SUSAR case icon exists (trial serious unexpected cases are a first-class case kind); "I can't change the assessed seriousness of a case" and "I can't change the determined listedness of a case" — assessed seriousness and determined listedness are protected fields in certain states.

**Coding (A, ch. 5):** autocode a term; manually code a term; MedDRA browser; five MedDRA levels; synonyms; SMQs; non-current terms; Null Flavor (reasons for missing data); "Which dictionaries does Argus Safety support?" (multiple dictionaries; WHO Drug Browser used for product search).

**Expedited reporting (A, ch. 6):** schedule an expedited report (manually or **auto-schedule**); create unscheduled reports or batch print; review draft; review scheduled reports; view status; submit = generate → approve → **transmit ICSR** (single or bulk, with routing details); print; store in Documentum; track outgoing status, transmit status, failed imports; **manage incoming ICSRs** — track incoming (incl. bulk), **search for duplicate reports** (duplicate search options, differences report, **accept initial E2B cases as follow-up**), view processed reports, **find overdue reports**. FAQ: scheduled vs generated report; what approval does; difference between submitting and transmitting; **"expedited reporting rules algorithm"** affecting components incl. **suppression of duplicate reports** and **blinded or forced distribution**; when follow-up reports and amendments are created.

**Periodic reporting (A, ch. 7):** aggregate reports (Case Data Analysis, CIOMS II Line Listing, case listing); periodic report types library; **Clinical Trial Periodic Report (CTPR)**; **ICH PSUR/PBRER** (incl. PBRER sections 6.2/6.3 cumulative tabulations, FDA PSUR support info); **US IND periodic report**; **NDA periodic report**; **Data Lock Point (DLP)** versioning and DLP queries; inclusion criteria; line listings; data elements; case grouping; summary tabulations; scheduling and frequency; report templates; security level; submission details; transmit; reopen submitted reports; track routing history.

**Scale/architecture (A):** multi-tenant environment with global worklist across tenants; multi-tenancy administration guide; multi-tenancy = enterprise/multi-affiliate architecture.

## Product B — ArisGlobal LifeSphere MultiVigilance (Tier 2)

- "MultiVigilance powered by NavaX is the industry's first and leading end-to-end automated **touchless case processing** system… scalable, efficient, and harmonized **case management**." (A)
- Automation "from **intake to submission**" (A).
- "Comprehensive Compliance… support for global and regional regulations, including the **FDA's E2B(R3) requirements**" (A).
- "**One Global Database**… single, harmonized global database… cloud-based, multitenant platform" (A).
- "**Format-Agnostic Intake**… ingestion of Safety data across multiple formats, including structured, semi-structured, and unstructured formats… captured at the point of intake" (A).
- "AI-Powered Translation… multilingual case processing" (A).
- Module constellation (navigation, A): MultiVigilance (case processing), Advanced Intake, Literature Intelligence, Advanced Signals, Business Intelligence, Document Distribution, Advanced Compliance Docs, Reporter (reporter-facing), Product Complaints (separate product), Regulatory suite (RIM etc.) and Quality suite sold separately.
- Customer tiers (A): "220+ global life sciences companies, CROs, and government health authorities"; RapidPV — "smaller organizations… in under two months" (SME tier).
- Positioning: "founded on over 30 years of safety expertise… in use across hundreds of organizations globally."

## Product C — AB Cube SafetyEasy (Tier 2, incl. EXTEDO reseller page)

- "SafetyEasy® Suite is AB Cube's all-in-one ecosystem for automated **multivigilance** management… modular, cloud-based platform that automates every step of the vigilance process, from early stage data capture to **regulatory reporting** and advanced analytics." (A)
- FAQ: "SafetyEasy® is a pre-validated, cloud-based **safety database** designed to manage **adverse event reporting across clinical and post-marketing phases**." (A)
- Pricing: "based on the **number of adverse events (cases) processed annually** & the number of vigilances selected"; packages from "up to 20 cases/year" to ">1000 cases/year". (A) — the case is the priced unit of work.
- How it works (A): Capture Cases (import safety data from multiple sources) → Automate Workflows (rules + automated coding) → Ensure Compliance (generate reports aligned with global standards) → Gain Insights (detect signals, track trends).
- Data Management (A): **E2B R2/R3 import, export, and validation**; gateway integration; **MedDRA & SMQs**; IME (important medical event) list support; **HL7 Gateway for medical devices**; MedDRA recoding.
- Signal Detection (A): **PRR, ROR**, qualitative analysis; FDA combination product support.
- Regulatory Reporting (A): **PSUR, DSUR, PBRER, PADER**; MDCG 2020-10/2, MDCG 2024-04 (device periodic reports); ad-hoc queries; customized reports.
- Automation (A): customized workflows; **Reportability Matrix** ("create rules to automatically route cases to your partners based on global reporting requirements"); automatic labeling & submission; **duplicate checks**; translation tools; customized lists; **customized anonymization**.
- Advanced (A): AI-powered follow-up narrative generation ("detects differences between the initial case and new information"); instance-level customization of fields/workflows/templates.
- Vigilance domains (A): Pharmacovigilance, Medical Device Vigilance, Cosmetovigilance, Nutrivigilance, Biovigilance.
- Lifecycle coverage (A): clinical trials Phase I–III ("AEs, SAEs, and SUSARs"), Phase IV/post-authorization studies, post-marketing surveillance ("spontaneous reports, literature cases, and patients feedback"), other studies.
- Customers (A): biotechs, CROs (PSI testimonial), health authorities (ANSM in portfolio), pharma/nutraceutical/cosmetics companies (Septodont, Air Liquide, L'Oréal, Clarins…); "more than 300 organizations across 90 countries" (EXTEDO page).
- Compliance (A): GAMP®5, FDA 21 CFR Part 11, EU GMP Annex 11, EMA GVP guidelines; pre-validated framework; EMA-certified gateway ("direct link to the regulatory authorities, eliminating the need for manual submission") (EXTEDO page).
- Intake modules (EXTEDO page, A): CasEasy AI (verbatim → case via NLP; suggests MedDRA-coded AEs; flags potential serious cases); Converter (OCR from CIOMS/MedWatch/SAE forms); Literature Manager (PubMed-connected AI triage → cases); Email2Case; **iTAP** ("triage and assessment of your ICSRs in the E2B(R3) format… L2A and/or MLM cases are retrieved from the EudraVigilance database and assessed… every decision for each ICSR you make is tracked"); MedInfo (medical information inquiries); Queries module ("create, dispatch, track, and resolve case-related clarification requests").
- Anonymization (EXTEDO page, A): customizable anonymization for case output formats (XML E2B R2/R3, CIOMS, MedWatch) for GDPR.
- eMDR XML file creation supported (EXTEDO page, A) — device straddle again.

## Cross-product Comparison

| Structure | Oracle Argus Safety | ArisGlobal LifeSphere | AB Cube SafetyEasy | Layer |
|---|---|---|---|---|
| Adverse-event case as unit of record (reporter/patient/product/event/assessment) | Yes (Tier-1: case sections) | Yes ("case management", "case processing") | Yes ("safety cases"; priced per case) | B (cross-product) |
| Case processing lifecycle with workflow states, routing, follow-up, closure | Yes (Tier-1: route between workflow states, follow-up events, formally close) | Yes ("intake to submission", "touchless case processing") | Yes ("automate workflows"; workflow tracking) | B |
| Duplicate detection (at entry and on incoming ICSRs) | Yes (Tier-1: check duplicates; duplicate search on incoming; suppression in rules algorithm) | Not stated on fetched page | Yes ("duplicate checks") | B (2/3 explicit) |
| Standardized coding (MedDRA; product dictionary) | Yes (Tier-1: MedDRA browser, autocode, SMQs; WHO Drug Browser) | MedDRA Coding Agent exists (NavaX) | Yes (MedDRA & SMQs, recoding) | B |
| Medical assessment: seriousness / expectedness(listedness) / causality | Yes (Tier-1: assessed seriousness, determined listedness, causality in medical review; product-event assessment) | Implied ("case management", compliance) | Yes (assessment of ICSRs via iTAP; IME lists; reportability matrix) | B |
| Expedited report machinery: schedule → generate → approve → transmit | Yes (Tier-1, full chain) | Yes ("intake to submission"; E2B(R3)) | Yes (automatic labeling & submission; EMA-certified gateway) | B |
| Electronic interchange (E2B) outgoing + incoming | Yes (Tier-1: Interchange; incoming ICSR queue; accept as follow-up) | Yes (E2B(R3) support) | Yes (E2B R2/R3 import/export/validation; gateway) | B |
| Periodic/aggregate reports (PSUR/PBRER, DSUR, etc.) | Yes (Tier-1: Dossier; CTPR/PSUR/IND/NDA; DLP) | Yes (Advanced Compliance Docs module) | Yes (PSUR/DSUR/PBRER/PADER) | B |
| Reportability rules engine | Yes (Tier-1: expedited reporting rules algorithm; configure regulatory reporting rules) | Not stated explicitly | Yes (Reportability Matrix) | B |
| Signal detection / analytics over case corpus | Yes — but as companion products (Insight/Mart/Empirica), not the core case app | Yes (Advanced Signals, BI modules) | Yes (BI module: PRR/ROR) | B (common, not core-app-invariant) |
| Literature surveillance | Yes (literature information section; Oracle PV page) | Yes (Literature Intelligence) | Yes (Literature Manager) | B |
| Partner/licensee (affiliate) case exchange | Yes (Tier-1: Argus Affiliate; "reports for health authorities and partners") | Not stated on fetched page | Yes (Reportability Matrix routes to partners) | B (2/3 explicit) |
| Clinical-trial safety (study cases, SUSAR, unblinding) | Yes (Tier-1: study info, SUSAR icon, Unblinding app) | Not stated on fetched page | Yes (Phase I–III AEs/SAEs/SUSARs) | B (2/3 explicit) |
| Multivigilance (device/cosmetic/nutrition domains) | Partial (device/vaccine tabs; eMDR/MIR/PMDA device guides) | Yes (product name) | Yes (5 domains) | B (variant axis) |
| Multi-tenant / global affiliate architecture | Yes (Tier-1) | Yes (multitenant cloud) | Not stated | B (2/3) |
| AI/automation layer (intake OCR, autocode, narrative, translation) | Present in current release (Oracle PV page: AI-driven analytics, automated intake) | Yes (NavaX agents, touchless) | Yes (CasEasy AI, Converter, narrative generation) | B (era machinery) |
| Compliance posture (Part 11 / GAMP5 / GVP / audit) | Yes (validation/security guides; audit log Tier-1) | Yes ("comprehensive compliance") | Yes (GAMP5, Part 11, GVP, audit-ready) | B |
| Regulator-side customers | CROs named; authorities via ArisGlobal claim | "government health authorities" (A) | Health authorities in portfolio (A) | B (indirect for regulator-side usage) |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The adverse-event safety case as the unit of record.** A persistent, individually identified record binding an identified patient's adverse event(s) to a suspect medicinal product, carrying the reporter, coded event terms, and the product-event assessment. Remove it → a complaint log or a medical-records store; nothing safety-regulatory remains.
2. **Governed case processing to a documented medical assessment.** A structured lifecycle — intake/triage (incl. duplicate detection), data entry, standardized coding, quality and medical review, follow-up, closure — executed under workflow states, attribution, and audit, ending in recorded assessments of seriousness, expectedness against labeling, and causality. Remove it → a raw adverse-event intake form store or a passive AE log.
3. **The regulatory reporting loop.** Per-case and periodic safety outputs directed to health authorities (and contractual partners) under obligation: reportability determined per case against regime rules, expedited case reports produced and exchanged in required formats (electronic interchange, both outgoing and incoming), and periodic aggregate reports compiled from the accumulated case corpus and tracked to submission. Remove it → clinical data capture or safety analytics with no obligation loop; the "pharmacovigilance" discipline disappears.

Jointly-held is load-bearing:
- 1 alone = adverse-event registry / complaint log
- 2 without 1 = workflow tool with nothing safety-shaped
- 1+2 without 3 = safety data capture without the regulatory discipline (EDC-like)
- 3 without 1+2 = a submission tool with no case world
- 1+3 without 2 = unassessed case forwarding (a conduit, not PV)

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Signal detection / safety analytics over the accumulated case corpus (case series, disproportionality methods, dashboards). Evidence note: Oracle sells signal management (Empirica) and analytics (Insight/Mart) as products *beside* the core case app — strong evidence this is a standard capability, not part of the defining core.
- Literature surveillance (screening → potential cases).
- Intake automation: email-to-case, OCR/form conversion, AI verbatim-to-case, reporter portals, medical-information intake bridging.
- Partner/licensee (affiliate) safety data exchange and global safety database consolidation.
- Aggregate-report authoring depth (line listings, summary tabulations, templates, DLP handling).
- Workflow automation ("touchless" processing), AI coding and narrative assistance, translation.
- Queries/action items, correspondence letters with due dates, overdue surfacing.
- Multi-tenant / multi-affiliate architecture, global worklists.
- Blinded-trial support (SUSAR handling, unblinding workflows).
- Compliance machinery: audit trails, lock states, e-signature-style approvals, validated-system posture (GAMP5/Part 11), anonymization on outputs.

### L2 — Variant / Optional Structure

- Customer type: MAH (industry) vs CRO (service provider running many sponsor databases) vs health authority / national PV center (regulator side; e.g., processing cases received from reporters and forwarding to a global programme — documented indirectly in-sample).
- Vigilance-domain scope: drug-only vs multivigilance (drug + device + cosmetic + nutrition + bio) — one platform family, domains as configurations.
- Deployment: validated on-premises enterprise vs cloud SaaS (multitenant) vs vendor-hosted cloud service.
- Regional regime packs: Japan local data entry/locking, China NMPA E2B(R3), Korea MFDS, PMDA device, EU MIR/MDCG device reports, FDA eVAERS/combination products.
- Scale and pricing: per-case-volume tiers (20/year to >1000/year in one sample) to enterprise global databases.
- Product-object breadth within a case: drug, vaccine, device, combination product tabs.

### L3 — Vendor-specific (kept out of the final document)

Argus Affiliate / Dossier / Interchange / Unblinding / Insight / Mart / Empirica naming; Safety One Argus branding; LifeSphere NavaX agents, RapidPV, ReporterX, Advanced Intake/Literature Intelligence/Advanced Compliance Docs module names; SafetyEasy iTAP / Converter / Email2Case / MedInfo / CasEasy AI / IntakeEasy module names, Qlik-based BI, unlimited-users pricing, 20/50/200/1000-case package ladders; Oracle Documentum storage integration; specific customer names.

## Vendor-specific Findings

- Oracle splits signal management (Empirica) and analytics (Insight/Mart) from the core case application — packaging evidence that analytics is a companion capability.
- ArisGlobal markets "touchless" end-to-end automated case processing as its differentiator; RapidPV = SME full-service offering.
- AB Cube prices by annual case volume and vigilance-domain count; unlimited users; pre-validated out-of-the-box posture; resold by EXTEDO.
- Argus has Japan-specific local data entry and per-country local locking — regional regime depth as a variant.

## Boundary Findings

- **vs Medical Device Post-Market Surveillance (joint-review flag from that pass):** Same loop shape (field events → case processing → reportability → regulator reports → trends) over a different regulated object. Multivigilance products (SafetyEasy's five domains; LifeSphere MultiVigilance; Argus's device tabs + eMDR/MIR/PMDA guides) realize both domains as configurations of one platform family. Seam: the regulated object and its regime artifacts — drug side carries E2B/MedDRA-WHODrug/GVP/PSUR-PBRER; device side carries eMDR/MIR/HL7-device-gateway/MDCG templates. Keep-both ratified; the flag is discharged from this side.
- **vs Clinical Trial Management System / EDC:** CTMS/EDC manage trial conduct and capture SAEs as trial data; the PV platform receives trial cases as safety cases with regulatory reporting duties (SUSAR icon, unblinding, Clinical Trial Periodic Report in Argus). Trial cases flow INTO the PV platform; the trial systems do not run the reporting loop.
- **vs Regulatory Information Management / RIM:** RIM = registration/dossier/submission estate; PV = safety-event record world. ArisGlobal and EXTEDO sell them as separate suites; Oracle's PV page is separate from its RIM offerings. Confirms the seam proposed by the device pass.
- **vs Life Sciences QMS / CAPA Management:** quality events (deviations, nonconformances) vs safety events (adverse events); CAPA may be triggered by safety findings but the record worlds and lifecycles differ.
- **vs Complaint & Escalation Management:** unregulated customer complaints vs regulated adverse-event cases; vendors offer product-complaints modules beside safety (ArisGlobal Product Complaints) — a complaint may launch a safety case, but complaint handling is not the defining loop.
- **vs Public Health Surveillance Platform:** population-level disease monitoring vs per-case product safety; different unit of record (aggregate signals vs individual cases).
- **vs EHR / Health Information Exchange:** patient-care records vs product-safety case records; the PV case is product- and event-centric, not care-centric.

**Removal test for the Type:** remove the medicinal-product binding and drug-regime artifacts → Medical Device Post-Market Surveillance (device object) or generic adverse-event logging. Remove the regulatory reporting loop → EDC/safety data capture. Remove the case → analytics dashboard over imported data.

## Historical / Market-Sample Check

Paper-era pharmacovigilance (post-thalidomide spontaneous reporting systems, 1960s–80s): a case file per adverse report (received form, reporter/patient/product/event details), coding against WHO-ART (MedDRA's predecessor), medical assessment of seriousness/causality, expedited report forms to authorities, typed periodic compilations, signal review at national centers. All three L0 legs are satisfied with no E2B, no MedDRA (WHO-ART era), no cloud, no AI. The definition holds for older and regional products; E2B(R3), MedDRA versions, GVP module names, cloud, and AI are era machinery, not invariants. Regulator-side national centers (the original PV institutions) satisfy the same legs with the reporting loop pointed at the global programme rather than at a market authorization — supporting the abstract phrasing of leg 3 ("directed to the overseeing authority/programme").

## Uncertainties

1. **Regulator-side realization under-documented.** VigiFlow (UMC) unreachable; regulator-side usage documented only indirectly (health authorities in AB Cube/ArisGlobal customer claims; SafetyEasy iTAP processing EudraVigilance L2A/MLM cases). Final document phrases the regulator side as a variant with reduced assertion strength.
2. **Veeva Vault Safety unreachable** — the cloud-native pole is documented via other vendors' cloud claims; no Vault-Safety-specific observations included.
3. **Exact workflow state names** not captured for any product (Argus documents routing between states without enumerating the full state list on fetched pages) — the final document describes the lifecycle conceptually, not as a universal stage list.
4. **Signal-detection method specifics** (PRR/ROR) observed in one product only (SafetyEasy) — kept product-specific; Empirica described generically as data mining/signal detection.
5. **No precise reporting timelines** (e.g., day-counts) asserted anywhere — fetched pages reference deadlines/overdue states without numbers; the final document follows suit.
6. **LifeSphere medical-review step** not explicitly named on the fetched page (Tier 2 only) — the medical-assessment leg rests on Argus Tier-1 + SafetyEasy evidence + industry framing, not on LifeSphere-specific wording.
7. **Aggregate-report authoring as part of the core vs companion module** varies (Argus: Dossier inside the core app; LifeSphere: Advanced Compliance Docs module; SafetyEasy: built-in) — held as standard capability with packaging variance, not as a definitional sub-structure beyond the reporting loop itself.

## Final Synthesis

A Pharmacovigilance Platform is the drug-safety system of record: it receives adverse-event reports about medicinal products from many channels, turns each into a structured safety case bound to patient/product/event, processes it through a governed lifecycle to a documented medical assessment (seriousness, expectedness vs labeling, causality), and discharges the regulatory reporting loop — expedited case reports exchanged electronically with authorities and partners, plus periodic aggregate reports compiled from the accumulated case corpus — while the growing case corpus feeds signal detection and ongoing safety evaluation. The defining core is the case + the governed processing + the reporting loop; signal detection, literature surveillance, intake automation, partner exchange, AI assistance, multivigilance breadth, and regional regime packs are standard capabilities or variants, not the definition.
