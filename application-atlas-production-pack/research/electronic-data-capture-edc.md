# Research Notes — Electronic Data Capture / EDC

## Research Goal

Understand **Electronic Data Capture (EDC)** as an Application Type: the software category clinical trials use to replace paper case report forms with structured electronic capture at investigative sites. What objects exist in its world (studies, sites, participants, visits/events, forms/eCRFs, items, edit checks, queries), what its canonical operating loop is (build → go-live → site entry under validation → review/query → amend → lock/extract), who uses it (study builders/data managers on the design side, site coordinators and investigators on the entry side, monitors between them), what rules constrain it (GCP / 21 CFR Part 11 record posture, attribution, no silent edits), and — above all — where its boundary sits against the processed sibling **Clinical Data Management** (the joint-review flag from that pass must be discharged here).

Research date: 2026-09-07.

## Initial Boundary (pre-research hypothesis)

- Hypothesis (sharpened by the CDM pass's proposed seam): EDC is **the capture instrument** — study-built electronic forms, site-facing data entry, validation at entry — while Clinical Data Management is **the management discipline over the collected data** (validation-plan ownership, query resolution, coding, reconciliation, cleaning metrics, lock, extraction). Most products bundle both; the question is which structures are definitional for EDC itself.
- Likely confusion zones:
  1. **Clinical Data Management / CDMS** (processed sibling) — the flagged seam; the market actively entangles the names (products named CDMS contain EDC; EDC products claim to replace "clinical data management tools").
  2. **ePRO / eCOA** (sibling) — patient-facing data collection vs site-facing capture.
  3. **CTMS** (sibling) — trial operations vs trial data.
  4. **Online Form Builder / Survey Platform** (§03.11) — generic form design + entry + validation without trial semantics.
  5. **EHR** — the care record vs the trial record; EHR-to-EDC flows connect them.
- Risk to avoid: defining EDC as "everything the study-data platform does" (capture + cleaning + lock + export) — that would collapse it into the CDM leaf.

## Research Questions

1. What do vendors themselves define EDC as? (Their own definitional sentences are the best boundary evidence.)
2. What is the study/capture data model: study → sites → participants → visits/events → forms → items?
3. What does "study build" concretely consist of (form designer, item types, logic, computed fields, libraries, versioning, publishing)?
4. What does site-facing entry look like (per-visit form completion, status states, signatures)?
5. Is validation-at-entry definitional? How do products describe it (instant edit checks, re-evaluation on amendments/imports)?
6. How much of the cleaning machinery (queries, SDV, coding, lock, export) lives inside EDC products, and how do vendors attribute it between EDC and a separate CDMS/data-management layer?
7. Which roles have dedicated surfaces (CRC, investigator, monitor, data manager, administrator)?
8. What variants exist (deployment, customer tier, bundling posture, scale, offline/remote capture, paper heritage, AI)?
9. Does the definition survive the historical check (early remote-data-entry EDC, non-cloud, institution-hosted academic deployments)?
10. Joint review with the CDM leaf: do both leaves stand, and where exactly is the seam?

## Representative Products

Selection goal: market spread + product-philosophy diversity + customer-tier diversity + source reachability. All fetched 2026-09-07. (The prior CDM pass on the same date could not reach several of these hosts; this pass succeeded via root/product URLs.)

| Product | Positioning | Philosophy / tier | Reach |
|---|---|---|---|
| **Medidata Rave EDC** | "the leading Electronic Data Capture (EDC)"; #1 preferred EDC in an independent 2025 sponsor benchmark; cornerstone of the Medidata platform | enterprise-market-leader pole; EDC shipped beside a separate "Clinical Data Studio" data-quality product and a separate "Designer" study-build product | root + dedicated Rave EDC page with FAQ (Tier 2) |
| **OpenClinica** | eClinical platform (EDC, eConsent, eCOA, Randomization, EHR-to-EDC, Reporting & Analytics) for small-to-mid sponsors, CROs, academic teams; open-source heritage | mid-market + academic pole; EDC-centered platform; deepest operational documentation (role-based user guides) | EDC solution page (Tier 2) + docs root with full OC4/OC3 TOC (Tier 1) |
| **Ennov MACRO EDC / DataLabs EDC** | European life-sciences suite; two named EDC product lines grouped under its "Data Management" offering; CDMS framing ("clinical data management software" contains EDC) | European suite pole; EDC-as-capability-inside-CDMS packaging; academic case studies (Cardiff University, ARCAGY-GINECO) | MACRO EDC product page with detailed feature lists (Tier 2) + CDMS page (Tier 2) |
| **Castor** | "AI-native clinical trial platform"; sells **EDC** and **CDMS** as separate products ("capture clean clinical data from every study site" vs "manage, clean, and lock your study data faster") | cloud-first, self-service, decentralized-trials pole; strong academic/biotech/medtech presence | root + dedicated EDC page (Tier 2) |

Unreachable (abandoned per network rule; market context only, no claims): REDCap (projectredcap.org and www.project-redcap.org, transport errors ×2 this pass; also failed ×2 in the CDM pass), Veeva (docs.veeva.com transport error; veeva.com failed ×2 in the CDM pass), Castor's helpdesk/docs subdomain (not retried — main site succeeded), DATATRAK (failed ×2 in CDM pass).

## Sources

All fetched 2026-09-07.

- Medidata — Rave EDC page: https://www.medidata.com/en/data-experience/edc-systems/ (title: "Electronic Data Capture (EDC) Software - Medidata Rave") ; corporate root: https://www.medidata.com/
- OpenClinica — EDC solution page: https://www.openclinica.com/solutions/electronic-data-capture-edc/ ; documentation root (OC4 + OC3 user documentation TOC): https://docs.openclinica.com/
- Ennov — MACRO EDC product page: https://en.ennov.com/solutions/clinical/macro/ ; Clinical Data Management (CDMS) page: https://en.ennov.com/solutions/clinical/clinical-data-management/
- Castor — EDC page: https://www.castoredc.com/electronic-data-capture-system/ ; corporate root: https://www.castoredc.com/
- Prior-pass context (same date, sibling leaf): research/clinical-data-management.md — OpenClinica Tier-1 guides (Discrepancy Notes, Data Manager), Ennov CDMS page, SCDM discipline anchor.

## Product Observations

### Medidata Rave EDC (Evidence layer: A — directly observed, Tier 2 product page + FAQ)

**Vendor's own definitional sentence.** "Medidata Rave, the leading Electronic Data Capture (EDC) supports the capture, management, cleaning, and reporting of trial data so sites, study teams, and regulators can trust the results and keep studies moving." Note the span: even the market leader's EDC page claims capture through cleaning/reporting — bundling posture, tested below against its own product architecture.

**The four-tab workflow.** (1) *Accelerate timelines*: reduce EDC setup time with AI automating repetitive configuration tasks; "Reach interim and final analysis sooner with **automated study locking**." (2) *Simplify site experience*: SSO for sites, on-demand training, "integrations that bring eSource and EHR data into EDC, reducing manual entry and accelerating form completion." (3) *Secure continuity*: "managing protocol amendments and mid-study changes without downtime." (4) *Boost performance*: "Monitor workflows, study, and site performance in real time and report or extract full datasets anytime. Support reconciliation, review, and central or medical monitoring with **EDC data flowing into Medidata Clinical Data Studio** for centralized oversight."

**Architecture as seam evidence.** The Data Experience nav separates: **Rave** ("Electronic data capture"), **Rave Lite** ("EDC for Phase I, IV, and MedTech"), **Designer** ("Central study build hub"), **Clinical Data Studio** ("Data quality management"), **Coder+** ("Automated medical coding"), **Companion** ("eSource/EHR-to-EDC"), **Targeted SDV** ("Risk-based source data verification"), plus RTSM, eCOA, Imaging, Safety Gateway. I.e., the market leader itself splits capture (Rave) from data-quality management (Clinical Data Studio) and study build (Designer) as separately marketed products — direct evidence for the instrument-vs-discipline seam.

**FAQ evidence.** Mid-study changes "with absolutely no downtime… deploy changes to thousands of patients in hours rather than months"; Rave as "the cornerstone of the Medidata Platform, enabling the aggregation and reconciliation of data from multiple sources, including eConsent, eCOA, RTSM, and Imaging"; Rave Lite as "a cost-effective and focused version of Rave tailored for Phase I, Phase IV, and medical device post-market studies… flexible pricing model and faster study builds"; Rave Companion "allowing sites to automatically populate EDC forms with EHR data."

**Vendor-specific (L3):** Rave / Rave Lite / Designer / Clinical Data Studio / Companion / Coder+ / Targeted SDV product names; ISR #1-preferred claim; "certified site users" stat block; AI-configuration claims; fact-sheet URLs.

### OpenClinica (Evidence layer: A — directly observed, incl. Tier-1 documentation structure)

**EDC product page.** Headline: "One EDC Platform. No More Switching Between Clinical Data Management Tools." — the EDC product marketed as consolidating the CDM-tool category (mirror image of Ennov's framing). "Purpose-built electronic data capture and eCRF software for sponsors, CROs, and academic research teams who need 21 CFR Part 11 compliance, flexible study design…" Four-step "How it Works": **Build with confidence** ("Design your study with drag-and-drop tools or pre-built CDASH templates") → **Capture clean data** ("Sites enter data with real-time validation and edit checks that catch errors instantly") → **Monitor and collaborate** ("Track progress, manage queries, and perform SDV with centralized oversight") → **Report and submit** ("Export submission-ready data with complete audit trails"). "Ideal For": Multi-Site Studies; Academic & Investigator-Initiated Research; Complex Protocols; Device & Diagnostics Studies; Remote & Hybrid Data Capture; Regulatory Submission-Ready Trials. Features: free expert-managed study build; templated CRFs; real-time edit checks & validations; role-based permissions; audit-ready trials (21 CFR Part 11, HIPAA, GDPR); integrated medical coding (OpenClinica Code); drag-and-drop form builder. Modular: "Use EDC on its own, or connect it with Recruit, eCOA, Randomization, eConsent, EHR-to-EDC, or Reporting & Analytics."

**Tier-1 docs TOC — the role/surface map of a mature EDC.**
- *Section 2, Building Forms and Studies*: Create a Study; **Form Library (CDASH)**; Design a Study (sub-chapters: **Events & Forms**, **Using Form Designer**, Designing Contact Data Forms, Using the Form Template, **Form Logic**, **Functions** incl. a "Validated Functions Index", **Calendar** (basic calendaring + rules), Using the Content Library, Locating Object Identifiers, Create and Configure **Data Review Tables**); Module Management; Automating Participant Access.
- *Section 3, Launching and Managing Studies*: **Publishing Your Study**; **EDC Study Go-Live Checklist**; User Access & Sharing (Managing Form Access and Permissions, LMS Integration, MFA, **Publish History**, Editing Study Settings, **Adding Sites**, **Inviting Users**); **Generating Annotated eCRFs**; **Generating Blank CRFs**.
- *Sections 4–7, role guides*: **Using OpenClinica as a CRC** (Add Participants, **Entering Data**, Queries (CRC)); **as an Investigator** (**Signing Participant Records**); **as a Monitor** (**Source Data Verification**, Queries (Monitor)); **as an Administrator**.
- *Section 8, as a Data Manager*: Managing Sites; Queries; SDV; Reviewing and Managing Data; Participant Audit Log; Suggested SOPs.
- *Sections 9–13, modules*: Recruit; Randomize; Consent (eConsent forms, participant flow); **Participate** (ePRO: design forms, offline mode, invite participants, participant data entry); **Code** (activation/permissions, study design configuration, in Study Runner).
- *Sections 14–18*: Insight (SQL/API/reporting); **Importing Data** (XML files, tabular data); **How and When to Use APIs** (CDISC ODM XML; clinicaldata import; participants/events APIs; bulk actions log); **Completing Your Study**; **Getting Data for Your Study: Reports and Extracts** (Data Review Tables, Back-End Access Via Insight, **Extract Data**, **Generating Participant Casebooks**).
- *OC3 guides (the earlier-generation product, showing the durable model)*: Submit Data (Add Subject incl. assign/reassign to site; **Schedule an Event**; View/Update Events; **Electronic Signatures** — sign an event, **sign a casebook (entire subject record)**; **Entering Data for an Event Into CRFs** (Enter Data Into a CRF; CRF Unavailable; **Double Data Entry**; **CRF Status**; editing previously saved CRF sections); Import Data (validate and check the import file); **Notes and Discrepancies** (about/types/status/workflow); Remove/Restore/Delete events and CRFs; **Subject Matrix**). Monitor and Manage Data (SDV incl. reset status; **Study Audit Log** — "What the Study Audit Log Tracks"; Manage CRFs incl. **CRF Versions**; **CRF Version Migration**). Extract Data (Create Dataset; formats: tab-delimited, HTML, Excel, **SPSS**, Data Mart, **CDISC ODM**, **SAS data and syntax**; import into R/STATA). Study Setup (Build and Modify Study; Create and Modify **Case Report Forms (CRFs)** incl. **eCRF Specifications**, **CRF Versioning**, replace/add version; Create and Modify **Event Definitions**; **Subject Group Classes**; **Create Rules**; Create and Modify **Sites**; Users and Roles).

**Study data model (assembled from docs structure):** Study → Sites → Participants (Subjects) → Study Events (scheduled per protocol) → CRFs (forms per event) → Items, plus Subject Group Classes, Rules, and a Participant Matrix view; publishing machinery moves a designed study to live use; annotated/blank CRF PDFs document the instrument.

**Vendor-specific (L3):** module names (Recruit/Randomize/Consent/Participate/Code/Insight), "50% fewer data queries", 15,000-studies claim, free study build, DN vocabulary (four types / five statuses — recorded in the CDM notes), Participant Matrix naming.

### Ennov MACRO EDC (Evidence layer: A — directly observed, Tier 2 with unusually detailed feature lists)

**Framing.** MACRO page headline: "MACRO: Clinical Trial Management Software" with subtitle bullets: "Compliant with ICH Good Clinical Practice"; "Instant response validation for quick and easy data collection"; "Data validation, clarification, reports and alerts for smooth data management"; "Cloud-based or on-site installation". "MACRO EDC is valuable to customers because of the data integrity, data management and compliance features it provides… allows users to quickly enter, track and report on subject data to collect accurate and reliable data for analysis." "MACRO is suitable for studies at all clinical trial phases… single-site studies and multi-national trials."

**Feature groups (directly quoted structure):**
- *Compliance and Audit*: MHRA-audited; ICH GCP; EU Clinical Trial Directive; FDA 21 CFR Part 11; ISO 27001 data center; **audit log and audit trail**; **double timestamps**.
- *Study Design*: **drag and drop form design**; full control of page layout; **build your own library for easy re-use of study elements**; **conditional activation of visits, forms and questions**; **advanced calculations and derivations**; flexible and powerful editing controls; **test and training environments**; **repeating question tables**; a range of question types and **laboratory normal ranges**.
- *Data Input*: **online data entry**; **instant validation of values during data entry**; **re-evaluation of validation checks at enrollment**; **automatic calculation of derived values**; **e-signatures and approvals**; alerts, messages and reminders; **visual status overview**; **clinical coding with MedDRA integration**.
- *Data Management*: pre-defined and personalised reporting; export formats (**SPSS, SAS, STATA, CSV**); **integrated data clarification and source data validation processes**; **flexible database locking features**; data import and export; data archive; event-based rules and automated alerts.
- *System Management and Security*: create/save/manage databases; **permission sets**; **user roles for each study and site combination**; password properties; monitor system activities; SSL encryption and digital signatures; API.

**CDMS page (same pass).** "Within that foundation, **electronic data capture (EDC)** supports efficient data entry and review through controlled forms and edit checks" — the vendor's own definition of EDC as a capability inside its CDMS category. Ennov EDC core capabilities: quick and easy eCRF design; support for all data field formats; computed data fields and interval calculations; defined data field groups; dynamic data field activation; optional eCRF pages; configurable library of allowable values; **online or offline patient data entry**; attach photos to eCRF using iPad camera. Key features: requires no IT or programming skills; medical coding for MedDRA and WHO Drug; **CDISC, CDASH and SDTM compliant**; full web interface; 21 CFR Part 11; compatible with existing Ennov Clinical studies. "Designed for **multi-center trials**, Ennov EDC supports **flexible study build** and scalable deployment across different trial types and phases, including early-phase and late-phase studies, post-marketing programs, and observational designs." "Ennov EDC is designed to support that **from study build through data capture and review**."

**Vendor-specific (L3):** MACRO / DataLabs / IMPACT product names; MHRA audit; double timestamps; Cardiff University and ARCAGY-GINECO academic case studies ("stable, inspection-ready EDC platform… without the cost and complexity of pharma-sized systems").

### Castor (Evidence layer: A — directly observed, Tier 2)

**EDC vs CDMS as separate products (nav definitions).** "**EDC** — Capture clean clinical data from every study site" vs "**CDMS** — Manage, clean, and lock your study data faster". Also separate: eCOA/ePRO ("patient reported outcomes captured anywhere"), eConsent, Catalyst ("AI extracts source data, a human reviews everything"), Data Management as a *service* ("Our experts build, clean, and deliver your data"). Direct market evidence for the seam: the same vendor sells the instrument and the discipline as distinct products, while also offering the discipline as outsourced services.

**EDC page.** "Castor's electronic data capture system makes it easier to capture your clinical trial data and integrate it seamlessly with other data in your clinical research ecosystem." "Explore **Castor EDC/CDMS**, our most robust module" (the bundle name appears here even though the nav splits them — naming entanglement again). Build side: "**Build advanced eCRFs in minutes with our low-code eCRF Builder**; deploy low-complexity clinical trial EDC in as little as 3-4 weeks." Integration side: "Integrate study data from EHR, eCRF, ePRO/eCOA, laboratory, wearables, and other devices into a single clinical trial data environment"; open API; eSource. Visibility side: "live dashboards showing enrollment, data entry status, and key study metrics"; "monitoring outstanding queries and incomplete records across sites"; "Oversee Source Data Verification (SDV) status to ensure timely verification and regulatory readiness." Compliance side: "validated electronic data capture (EDC) system built for regulatory compliance, audit readiness, and global scale"; pre-built validated eCRF templates; multiple field types and conditional logic; reuse and clone eCRFs across studies; "Save study data in real time within the EDC platform"; certified compliant servers in supported regions; field-level encryption, 2FA, long-term data retention; amendments: "Manage amendments in a secure, traceable, and validation-friendly environment; maintain full audit trails for every change; **create separate test environments to validate updates before deployment**"; compliance list: FDA 21 CFR Part 11, ICH GCP, GDPR, HIPAA, ISO 27001, ISO 9001, HL7 FHIR alignment. Study-type spread: interventional trials "from startup to lock", chart review, patient registries, post-market follow-up.

**Vendor-specific (L3):** Catalyst product name and stats (6.6% manual-abstraction error rate framing, 99.8% submission success, 0.8% reviewer-changed values); 3-4-week / 63% build-time claims; Everest PEAK Matrix placement; 19,000+ studies claim; "Castor EDC/CDMS" bundle naming.

### Cross-pass anchor: research/clinical-data-management.md (Evidence layer: A for the sibling)

The CDM pass established: CDM's defining core = governed study data record + validation→discrepancy loop + resolution with contributors + controlled finalization (lock + extract); its OpenClinica Tier-1 evidence (Discrepancy Notes types/statuses, Data Manager role, soft removal, extract formats) and SCDM profession anchor. The proposed seam — EDC = capture instrument; CDM = management discipline — was flagged for joint review in this pass.

## Cross-product Comparison

| Dimension | Medidata Rave | OpenClinica | Ennov MACRO/EDC | Castor |
|---|---|---|---|---|
| EDC self-definition | "supports the capture, management, cleaning, and reporting of trial data" | "purpose-built electronic data capture and eCRF software"; "no more switching between clinical data management tools" | "efficient data entry and review through controlled forms and edit checks" (in CDMS framing); "from study build through data capture and review" | "capture clean clinical data from every study site" |
| Study build | AI-assisted configuration; separate "Designer" build-hub product | drag-and-drop + CDASH template library; Form Designer, Form Logic, Functions, Calendar; publish + go-live checklist; annotated/blank CRF output | drag-and-drop form design; element libraries; conditional activation of visits/forms/questions; calculations & derivations; repeating question tables; lab ranges; test & training environments | low-code eCRF Builder; validated eCRF templates; conditional logic; clone/reuse across studies |
| Entry model | site workflows; SSO; eSource/EHR auto-populate forms | per-participant per-event CRF entry; Subject/Participant Matrix; CRF status; double data entry (OC3) | online data entry (offline option); visual status overview | real-time save; multi-site |
| Validation at entry | implied ("reducing manual entry", quality claims) | "real-time validation and edit checks that catch errors instantly" | "instant validation of values during data entry"; re-evaluation at enrollment | conditional logic + pre-built validated templates |
| Amendments | protocol amendments/mid-study changes "without downtime" | CRF versioning + CRF version migration | flexible editing controls; amendment-friendly design | traceable amendment management; separate test environments |
| Queries | surfaced on Rave; central oversight in separate Clinical Data Studio | role-based query guides (CRC/Monitor/Data Manager); auto from failed checks; DN model (Tier-1) | "data validation, clarification, reports and alerts" | "outstanding queries… across sites" on dashboards |
| Coding | separate Coder+ product | OpenClinica Code module | clinical coding with MedDRA (WHO Drug on CDMS page) | (light coding mentioned in testimonial only) |
| SDV | separate "Targeted SDV" product | Monitor role guide + SDV screens | "integrated… source data validation processes" | SDV status oversight on dashboards |
| Lock & export | "automated study locking"; "extract full datasets anytime" | Completing Your Study; Extract Data (ODM/SAS/SPSS/Excel; casebooks); "database locks" analytics | "flexible database locking features"; exports SPSS/SAS/STATA/CSV; data archive | lock attributed to its separate CDMS product; EDC page covers collection |
| Record posture | "sites, study teams, and regulators can trust the results" | 21 CFR Part 11, audit logs, e-signatures (event + casebook) | audit log/trail, double timestamps, e-signatures, Part 11, MHRA-audited | real-time save, audit trails for every change, Part 11/GCP/GDPR/HIPAA, field-level encryption |
| External data | Companion (EHR→EDC); aggregating/reconciling multiple sources | Import Data (XML/tabular); APIs (CDISC ODM XML); EHR-to-EDC module | data import/export; API | EHR/lab/ePRO/device integration; open API; eSource |
| Roles with surfaces | sites/study teams/regulators named | CRC, Investigator, Monitor, Data Manager, Administrator (dedicated guides) | per-study-and-site permission sets; e-signature approvals | study builders, sites, sponsors |
| EDC-vs-CDMS packaging | EDC + separate data-quality product (Studio) | EDC platform claiming to consolidate CDM tools | EDC products inside a CDMS offering | EDC and CDMS as separate products |

**Stable across the sample (B-layer):** the study-built eCRF instrument (designer + per-protocol forms + per-participant visit/event organization); site-facing entry into a central per-study database; validation applied to captured data (instant checks in all products that describe it); the regulated record posture (audit trail, attribution, e-signatures, Part 11/GCP); multi-site distribution with per-study/per-site roles; form versioning and mid-study amendment handling; query/discrepancy machinery attached to captured data; SDV support; medical coding integration or adjacency; external-data import/integration; database lock and analysis-format export (attributed to the EDC product itself in three of four samples; Castor attributes finalization to its CDMS sibling); dashboards of enrollment/completion/queries.

**Product-shaped (kept general in the final doc):** exact query vocabulary (Discrepancy Notes vs queries vs clarifications); test-environment provisions (observed in two products); AI configuration/extraction (era-typical, product-specific claims); double data entry (single product, historical); annotated/blank-CRF PDF generation (single product's docs); specific export-format lists; "EDC/CDMS" bundle naming.

## Canonical Model

### L0 — Defining Invariant (deliberately small)

```text
The study-built capture instrument
  (electronic case report forms designed from the protocol —
   forms/items organized per participant across scheduled
   visits/events; built before go-live, versioned over time)
└── Site-based data entry
    (clinical site staff enter participant data into the
     study's central database, form by form, visit by visit)
└── Validation applied at capture
    (edit checks embedded in the instrument fire as data is
     entered/saved — ranges, required fields, logical consistency)
└── The entry is the trial's regulated record
    (attributable, time-stamped, change-tracked; no silent edits;
     e-signatures; designed for inspection and submission)
```

Four properties. Remove one and the Type stops being recognizable:
- without the protocol-specific instrument (participant×visit form structure), it is a generic form/survey builder;
- without site-based entry, it is patient-facing collection (ePRO/eCOA) or a management-only oversight layer;
- without validation at capture, the "clean at source" purpose disappears and only downstream cleaning remains (the CDM discipline without its instrument);
- without the regulated-record posture, it is an ordinary data-collection tool rather than trial documentation.

**Boundaries of the invariant set:** query resolution ownership, coding, external-data reconciliation, cleaning metrics, and the lock/extract handoff are NOT in L0 — they are the CDM sibling's defining machinery, carried by most EDC products as bundled capability (L1). This is what keeps the two leaves distinct.

### L1 — Common Mature Structure

- Study-build tooling: drag-and-drop form designers; item/field-type ranges; computed/derived fields; conditional/dynamic activation; repeating item groups; allowable-value libraries; lab normal ranges; CDASH-class template libraries; reusable form libraries; test/training environments; study publishing + go-live checklists; annotated/blank eCRF document generation
- Multi-site access machinery: site provisioning, per-study and per-site role assignment, role-based permissions
- Query/discrepancy machinery raised on captured data (automatically from failed checks; manually by reviewers) with role-differentiated surfaces — the sustained resolution loop belongs to the CDM discipline
- Review surfaces: participant matrices/listings, form/visit status states, completion and missing-form tracking, dashboards (enrollment, data-entry status, outstanding queries)
- SDV support for monitors
- Medical coding integration (MedDRA-class dictionaries) — integrated module or adjacent product
- External data: XML/tabular import with import validation; APIs (CDISC ODM-class); EHR/eSource flows; lab/device/ePRO feeds
- Finalization: database lock features and dataset extraction in analysis formats (CDISC ODM-class, SAS/SPSS-class), participant casebooks
- e-signatures of forms/events/records; 21 CFR Part 11 / ICH GCP / HIPAA / GDPR posture; audit logs
- Form versioning + mid-study amendment/migration handling without downtime

### L2 — Variant / Optional Structure

- Deployment: cloud SaaS vs on-premises vs institution-hosted/self-hosted lineages
- Customer tier: academic/investigator-initiated (self-service, low-code, grant-scale economics) vs pharma/CRO enterprise (validated vendor services, portfolio governance)
- Scale pole: lightweight editions for early-phase/post-market/device studies vs global multi-national programs
- Bundling posture: standalone EDC vs suite (eConsent/ePRO/RTSM/eSource/recruitment modules) vs EDC + separate CDMS products vs unified CDMS umbrella containing EDC
- Capture extensions: offline entry, tablet/iPad capture with photo attachments, remote/hybrid capture, decentralized components, EHR auto-population
- Paper heritage: double data entry modes; migration of paper-keyed data (single-product evidence — historical variant)
- AI-era features: AI-assisted study configuration; AI source-document extraction into eCRFs with human confirmation

### L3 — Vendor-specific (research notes only)

- Medidata: Rave/Rave Lite/Designer/Clinical Data Studio/Companion/Coder+/Targeted SDV/Safety Gateway names; ISR #1 preferred claim; "automated study locking"; AI-configuration claims; certified-site-user stats
- OpenClinica: module names (Recruit, Randomize, Consent, Participate, Code, Insight); Discrepancy-Note vocabulary (4 types/5 statuses); Participant Matrix; free expert-managed study build; "50% fewer queries"; 15,000-studies/3M-patients claims; one-click publishing
- Ennov: MACRO/DataLabs/IMPACT names; MHRA audit; double timestamps; single-tenancy; iPad camera eCRF; 450+ customers / 500,000 users claims
- Castor: Catalyst name and precision claims; 3-4-week/63% build-time claims; "Castor EDC/CDMS" bundle naming; 19,000-studies claim; Everest PEAK Matrix placement

## Boundary Findings

### vs Clinical Data Management / CDMS (§22 sibling, processed) — joint review DISCHARGED

The flagged seam holds and is now evidenced from the EDC side:
- **Medidata** ships Rave (EDC) and Clinical Data Studio ("data quality management") as separate products, with "EDC data flowing into Clinical Data Studio for centralized oversight" — the leader's own architecture separates instrument from discipline.
- **Castor** sells EDC ("capture clean clinical data from every study site") and CDMS ("manage, clean, and lock your study data faster") as separate products, plus data management as outsourced services.
- **Ennov** frames EDC inside its CDMS category but defines it narrowly: "EDC supports efficient data entry and review through controlled forms and edit checks", "from study build through data capture and review" — capture-first.
- **OpenClinica** blurs in the opposite direction (its EDC headline claims to consolidate "clinical data management tools"), but its own four-step workflow (build → capture → monitor → report) and its Tier-1 role docs show the query/SDV/review machinery as *one component* of the EDC product, with the sustained cleaning discipline (DN model, Data Manager SOPs, lock analytics) sitting exactly where the CDM leaf places it.

**Outcome: keep both leaves.** EDC's defining core = the capture instrument (study-built eCRFs, site entry, at-capture validation, regulated record). CDM's defining core = the management discipline over collected data (validation-plan ownership, discrepancy resolution, coding, reconciliation, cleaning metrics, lock, extraction). Products bundle both; the documents record the seam symmetrically. The CDM doc's Related-Types row already states the seam; this doc mirrors it. Historical check supports the split: paper-era data management existed without electronic capture (CDM side), and capture machinery is describable without the cleaning machinery.

### vs ePRO / eCOA (§22 sibling, unprocessed)

Who enters decides: EDC entry is by site-based clinical staff about protocol observations; ePRO/eCOA is the participant's own reporting (diaries, questionnaires). Evidence: OpenClinica separates "Participate" (participant data entry) from core EDC entry; Ennov separates ePRO ("patients can complete diaries") from EDC; Castor separates eCOA/ePRO from EDC; Medidata separates eCOA. Clean boundary; those leaves' own passes own the detail.

### vs Online Form Builder / Survey Platform (§03.11)

A generic form builder has design + entry + validation, but lacks: the participant×visit/event protocol structure, site-based role-scoped access, the regulated-record posture (GCP/Part 11 audit trail, e-signatures, inspection readiness), study versioning under amendments, and the analysis/submission pipeline. EDC products explicitly contrast themselves with "DIY tools" (OpenClinica academic framing). Clean boundary.

### vs Clinical Trial Management System / CTMS (§22 sibling, unprocessed)

Operations vs data: CTMS manages sites, monitoring visits, milestones, budgets; EDC captures the trial's data. Evidence: Medidata nav separates CTMS (Study Experience) from Rave (Data Experience); Ennov ships CTMS and Data Management/EDC as separate solution groups. Clean boundary.

### vs EHR (§22) and eSource flows

The EHR is the care record; the EDC database is the trial record. Products increasingly pull care data *into* the instrument (Rave Companion auto-population; OpenClinica EHR-to-EDC; Castor EHR integration) — the EHR is a data source, not the capture instrument. Boundary holds.

### vs Electronic Trial Master File / eTMF (§22 sibling, unprocessed)

Documents vs data: eTMF holds trial documents; EDC holds captured data values. Clean boundary (Ennov ships eTMF separately from its Data Management group).

### Historical / market-sample check (§24)

- **Early remote-data-entry EDC** (the paper-CRF replacement generation): study-specific forms entered at sites with range/consistency checks and audit trails — satisfies the four invariants without cloud, integrated coding, CDISC exports, AI, or eSource. The definition does not over-fit the modern platform bundle.
- **Institution-hosted academic deployments** (open-source lineage; the academic case studies sampled) satisfy the core with self-service builds and lighter machinery.
- **Single-site studies** (MACRO explicitly: "single-site studies and multi-national trials") satisfy the core — multi-site is the standard context, not the definition.
- Non-US regulatory regimes (EU CTD, MHRA audit) show the same structure — the definition is not US-Part-11-shaped.
- Therefore the invariant set (instrument + site entry + at-capture validation + regulated record) is era-, region-, and deployment-independent.

## Uncertainties

1. **REDCap (the academic/free institution-hosted pole) could not be fetched** (×2 this pass, ×2 in the CDM pass). Its specific model is NOT directly verified; no product-specific claims are made about it anywhere. The academic tier is evidenced through OpenClinica's academic positioning and Ennov/Castor academic case studies instead.
2. **Veeva Vault EDC remains unreachable** (docs.veeva.com transport error this pass; veeva.com ×2 in the CDM pass). The enterprise-suite pole beyond Medidata is therefore not directly observed; no claims about Veeva.
3. **Database-lock attribution varies**: three of four sampled EDC products name lock as an EDC-product feature (Rave "automated study locking"; MACRO "flexible database locking features"; OpenClinica "database locks" analytics + "Completing Your Study" chapter), while Castor attributes lock to its separate CDMS product. Treated as a common bundled capability whose presentation varies, with its disciplinary ownership recorded in the CDM leaf.
4. **Validation-at-entry in the earliest EDC generation** could not be verified from primary historical sources; the invariant is phrased as "validation applied when data is captured", which is directly supported by all four sampled products ("instant validation… during data entry"; "real-time validation and edit checks"; conditional logic/validated templates; edit-check framing).
5. **Query vocabulary and state models vary** (Discrepancy Notes / queries / clarifications); the final doc uses conceptual wording only.
6. **Exact form-version migration semantics, go-live checklists, and annotated-CRF generation** are Tier-1 documented for one product (OpenClinica); kept product-anchored or generalized with hedged wording.

## Final Synthesis

Electronic Data Capture is the **capture instrument of clinical trials made into software**. Its world: a **study-built instrument** — electronic case report forms designed from the protocol (form designers, item types, computed fields, conditional logic, template libraries), organized around participants progressing through scheduled visits/events, versioned and amended over the study's life; **site-based entry** — coordinators and investigators at clinical sites enter each participant's data form by form into the study's central database, with per-study/per-site roles; **validation at capture** — edit checks embedded in the instrument fire as data is saved (ranges, required fields, logical consistency), the "clean at source" principle that distinguishes EDC from paper and from downstream-only cleaning; and the **regulated record** — every value attributable and time-stamped, changes leaving traces (reason-for-change, audit trails, e-signatures), the database designed for inspection and submission. Around that core, mature products carry multi-site access machinery, query/discrepancy surfaces raised on captured data, SDV support for monitors, coding integration, external-data import and EHR/eSource flows, dashboards, and lock-and-extract finalization — the latter being the bundled-in edge of the clinical-data-management discipline, which is the sibling Type. EDC is used by sponsors, CROs, and academic teams; its variants span cloud/on-premises/institution-hosted deployment, academic self-service to enterprise vendor-built tiers, standalone to suite bundling, and AI-era configuration and source-extraction features. The joint-review flag with Clinical Data Management is discharged: both leaves stand, separated by the instrument-versus-discipline seam, and the market's own product architectures (EDC beside data-quality products; EDC and CDMS as separate products) corroborate it.
