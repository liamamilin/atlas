# Research Notes — Clinical Data Management

## Research Goal

Understand **Clinical Data Management (CDM)** as an Application Type: the software category behind the clinical-data-management discipline in clinical trials. What objects exist in its world (study data records, discrepancies/queries, coding, extracts, locks), what its canonical operating loop is (build → capture → clean → code → reconcile → lock → export), who operates it (sponsor/CRO data-management teams and site contributors), what rules constrain it (GCP / 21 CFR Part 11 audit posture, no-deletion, reason-for-change, lock gating), and where its boundaries sit against neighboring §22 leaves — above all **Electronic Data Capture / EDC** (unprocessed sibling), plus CTMS, ePRO, IRT/RTSM, and Pharmacovigilance (all unprocessed), and the market-adjacent RBQM / central-monitoring pole.

Research date: 2026-09-07.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: Clinical Data Management software is the **sponsor/CRO-side system for ensuring clinical trial data is complete, consistent, valid, and analysis-ready**: study-scoped trial data as a governed record + rule-based validation producing discrepancies/queries + a query-resolution loop with site contributors + medical coding + external-data reconciliation + a controlled database lock and analysis-ready export.
- Likely confusion zones:
  1. **Electronic Data Capture / EDC** (sibling, unprocessed) — expected to be the sharpest seam. Market expectation: EDC = capture side (form design, site data entry); CDM = management side (validation, queries, coding, cleaning, lock). Risk: the market itself may treat "CDMS" as the umbrella platform containing EDC.
  2. **CTMS** — trial operations (sites, visits, milestones, budgets) vs trial data.
  3. **ePRO / eCOA, IRT/RTSM** — data-collection siblings often bundled inside CDMS offerings.
  4. **Pharmacovigilance** — safety case processing vs trial-data cleaning; both use medical dictionaries (MedDRA).
  5. **RBQM / central statistical monitoring** — a data-review layer above EDC/CTMS (CluePoints-style); no dedicated directory leaf identified in §22.
- Evidence posture anticipated: the category name names a profession (there is a professional body and certifications for it), and the dominant market framing may be "CDMS = the study data platform" (capture + management bundled). The canonical definition must be tested against the discipline-centered reading (data quality machinery) rather than collapsing into "EDC by another name."

## Research Questions

1. What does the market itself mean by "Clinical Data Management" / "CDMS"? Is it the discipline (cleaning/validation/lock) or the whole study-data platform (EDC + coding + RTSM + ePRO)?
2. What are the core objects: study data record structure, discrepancy/query records, coding mappings, extracts, locks?
3. What is the canonical loop from study build through data cleaning to database lock and export?
4. Who uses it, in which roles, and how is responsibility divided (data manager vs monitor vs site vs coder vs statistician)?
5. What rules are definitional: audit trail, no-deletion, reason-for-change, role separation, lock gating?
6. How do products relate to the EDC sibling (unified vs adjacent vs oversight-layer)?
7. What variants exist (paper/double-data-entry heritage, academic vs pharma, cloud vs on-prem, RBQM layer)?
8. Does the definition survive the historical/market-sample check (paper-era data management, non-US trials, academic studies)?
9. What taxonomy problem does the market's own naming create for the EDC leaf?

## Representative Products

Selection goal: market spread + product-philosophy diversity + customer-tier diversity, constrained by source reachability. Fetched 2026-09-07.

| Product | Positioning | Philosophy / tier | Reach |
|---|---|---|---|
| **OpenClinica** | eClinical platform (EDC, eConsent, eCOA, Randomization, EHR-to-EDC, Reporting & Analytics) for small-to-mid sponsors, CROs, academic teams; open-source heritage | mid-market + academic pole; deepest operational documentation obtained | root, EDC solution page, Analytics solution page, Trust & Compliance page, docs root + OC4 Data Manager guide + OC3 Discrepancy Notes guide (Tier 1) |
| **Ennov Clinical** | life-sciences suite vendor; **"Clinical Data Management" is a named product line** (Ennov Clinical Data Management / CDMS) with MACRO EDC and DataLabs EDC as sibling products; RTSM and ePRO inside the same offering | European enterprise/mid-market suite pole; explicitly names the category | root + dedicated "Clinical Data Management Software (CDMS)" page with category FAQ (Tier 1/2) |
| **CluePoints** | "RBQM and clinical data review platform for Sponsors and CROs" — centralized risk detection, intelligent medical coding, medical & safety review, intelligent query detection | RBQM / data-review oversight pole (adjacent boundary anchor, sits above EDC/CTMS) | root page (Tier 2) |
| **SCDM** (Society for Clinical Data Management) | professional body for the CDM discipline; GCDMP industry-standard practice guide; CCDM/CCDA/CCDS certifications | profession/discipline anchor (not a product) | root page (Tier 3, authoritative non-vendor) |

Unreachable (1–2 attempts each, abandoned per network rule; used as market context only, no claims): Veeva (veeva.com, 2 transport errors), Castor (docs/info.castoredc.com, 2 errors), Medidata (medidata.com, 2×404), Oracle Health Sciences (oracle.com, 2×404), REDCap (projectredcap.org, 2 errors), DATATRAK (2 errors), Ennov's /en/ path (1×404, recovered via root).

## Sources

All fetched 2026-09-07.

- OpenClinica — root: https://www.openclinica.com/ ; EDC solution page: https://www.openclinica.com/solutions/electronic-data-capture-edc/ ; Analytics page: https://www.openclinica.com/solutions/clinical-data-reports-and-analytics/ ; Trust & Compliance: https://www.openclinica.com/trust-and-compliance/
- OpenClinica documentation (Tier 1) — docs root: https://docs.openclinica.com/ ; OC4 Data Manager guide ("Reviewing and Managing Data"): https://docs.openclinica.com/oc4/using-openclinica-as-a-data-manager/oc4-data-management/ ; OC3 "Notes and Discrepancies": https://docs.openclinica.com/3-1/openclinica-user-guide-submit-data-module-overview/openclinica-user-guide-monitor-and-manage-data-notes-and-discrepancies/ (docs TOC also confirms chapter structure: Data Manager role section, Completing Your Study, Extract Data incl. CDISC ODM/SAS/SPSS formats, OpenClinica Code, Double Data Entry, Study Audit Log, SDV, Importing Data, APIs)
- Ennov — root: https://www.ennov.com/ ; Clinical Data Management page: https://en.ennov.com/solutions/clinical/clinical-data-management/ (title: "Clinical Data Management Software (CDMS) for Clinical Trials")
- CluePoints — root: https://www.cluepoints.com/
- SCDM — root: https://scdm.org/

## Product Observations

### OpenClinica (Evidence layer: A — directly observed, incl. Tier-1 operational docs)

**Category self-framing.** EDC solution page headline: "One EDC Platform. **No More Switching Between Clinical Data Management Tools.**" — direct terminology evidence that the vendor positions its EDC as consolidating what the market calls clinical data management tools. Footer: "practical eClinical platform that unites EDC, eConsent, eCOA, Randomization, EHR-to-EDC, analytics, and patient recruitment… Built for small to mid-size sponsors, CROs, and academic teams."

**Study build & capture machinery (product page).** Drag-and-drop study builder; templated CDASH CRFs; one-click study publishing; free expert-managed study build ("send us your protocol and get a complete, validated study"); "real-time validation and edit checks that catch errors instantly"; role-based permissions; audit-ready trials (21 CFR Part 11, HIPAA, GCP, GDPR); "integrated medical coding — code adverse events and medications where your data lives—no third-party tools or audit trail gaps" (OpenClinica Code module); four-step "How it Works": Build with confidence → Capture clean data → **Monitor and collaborate ("Track progress, manage queries, and perform SDV with centralized oversight")** → Report and submit ("Export submission-ready data with complete audit trails").

**Discrepancy Notes — the query/discrepancy machinery (OC3 docs, Tier 1).**
- A Discrepancy Note (DN) attaches to a single data element — usually a CRF Item (diagnosis, medication, weight), sometimes the Subject record or the Study Event. It is a threaded record: parent note + child notes ("the thread of a single parent Note with the child Notes under it is referred to as one Discrepancy Note").
- Created **automatically** by edit checks / rules / import validation ("OpenClinica can automatically create a Discrepancy Note when you save a CRF that contains errors in the data, as determined by OpenClinica's edit checking") or **manually** by users (e.g., a Data Manager raising a query on data that passed automated checks).
- Four note types: **Failed Validation Check** (data does not comply with expected values), **Query** (asks a question about data), **Reason for Change** (mandatory when study is configured with "Force Reason for Change" and a completed CRF is altered), **Annotation** (comments/information not representable in the CRF).
- Status ladder with responsibility semantics: **New → Updated → Resolution Proposed → Closed** (final; immutable thereafter; only certain roles may close), plus **Not Applicable** for Reason-for-Change/Annotation. "The status for a Discrepancy Note provides an indication of who is responsible for the next step."
- Documented query workflow (Query type): originator creates the note (New), assigns it to the user who can answer; the assignee adds a child note, may or may not modify the data value, sets Resolution Proposed (or Updated if more work needed); the originator verifies and closes.
- **Immutability rule:** "Once a Discrepancy Note is created, it cannot be deleted. If a Discrepancy Note is created in error, a common practice is to add a new Child Note with a Status of Closed."
- Missing required fields: must either supply a value or attach an explanatory note ("You can leave a required field in a CRF empty if you provide a Discrepancy Note that provides an explanation").
- Import validation: data-import errors automatically generate Failed Validation Check DNs (ties external-data import into the same machinery).

**Data Manager role (OC4 docs, Tier 1).**
- Dedicated role-based guide section: "Using OpenClinica as a Data Manager" (managing sites, queries, SDV, reviewing/managing data, participant audit log, suggested SOPs). A "Data Manager and Study Director Home Page" exists as a distinct role surface (OC3).
- "Typically, Data Managers and Monitors are responsible for reviewing data" — review happens in the **Participant Matrix**, **Queries**, or **Source Data Verification** screens.
- **Soft removal:** "Removing a Participant does not delete the Participant, but instead removes access to that Participant's data. The data… can still be viewed, but cannot be edited and will not be included in data extracts." Removal/restoration requires a recorded reason; icon flips Remove↔Restore.
- **Reassignment:** Data Managers reassign participants between sites (eligibility depends on participant status; "Reassigning a Participant does not modify any Participant data or associated records. All attributes, forms, events, signature statuses, attestations, and consent records remain unchanged. Participant reassignment is recorded in the audit log").
- **Form migration:** transferring data between form versions (participant-by-participant or batch) is a Data-Manager-only action once data exists; migration outcomes are enumerated per version-difference scenario.
- Event-level actions: view, edit, **lock**, remove, restore events (event removal also requires a reason).
- **Suggested SOPs** page exists for the Data Manager role — the software frames itself inside the sponsor's SOP-driven quality system.

**Completion & extraction (docs structure, Tier 1).**
- Chapters: "Completing Your Study"; "Getting Data for Your Study: Reports and Extracts" (Data Review Tables, Extract Data, Generating Participant Casebooks); OC3 "Extract Data" module: create/define datasets, generate and download datasets, archived export files, formats include tab-delimited, HTML, Excel, SPSS, **CDISC ODM**, **SAS data and syntax**, plus R/STATA import guides.
- OC3 includes a **Double Data Entry** section under data entry (2.4.3) — the classic paper-era keying discipline survives as a product feature.
- Audit: "Study Audit Log" / "Participant Audit Log" chapters ("What the Study Audit Log Tracks"); electronic signatures (sign events, sign a casebook/entire subject record); SDV with per-CRF/subject status tracking and reset.

**Analytics page (Tier 2).** "Track study performance across your portfolio with real-time snapshots for **database locks, SDV tracking, and query management**." "Faster data cleaning — Identify errors, outliers, and patterns early and often—**before database lock**—so you're not scrambling at the end." "Ideal for… **Data managers planning database locks**." Pre-built reports: CRF Completion by Event, Missing Forms, **Query Aging by Month, Site, and Study**, SDV by Event and Site, AE/SAE alerts. Dashboards "tailored for different stakeholders—data managers, CRAs, safety officers, or sponsors". Access to "clinical data, ePRO data, query data, monitoring data, audit logs".

**Compliance page.** ICH GCP E6(R2) compliant, 21 CFR Part 11 compliant, HIPAA, GDPR, SOC 2 Type II, ISO 27001.

**Vendor-specific (L3):** "50% fewer data queries"/"50% reduction in rework" claims; 15,000 studies / 3M patients claims; OpenClinica Insight (SQL/back-end reporting), OpenClinica Code, OpenClinica Randomize/Consent/Participate module names; DN four-type/five-status vocabulary (product vocabulary, generalized out); Participant Matrix naming.

### Ennov Clinical (Evidence layer: A — directly observed, category-defining page)

**The category is named and bounded by the vendor.** Dedicated page titled "**Clinical Data Management Software (CDMS) for Clinical Trials**". Nav structure: Clinical → "**Data Management**" group containing **Ennov Clinical Data Management**, **MACRO EDC**, **DataLabs EDC** (two acquired EDC products listed as siblings), plus RTSM anchored in the same section; CTMS and eTMF are separate sibling groups. Suite statement: "The Ennov Clinical suite consists of **Clinical Data Management applications** as well as Clinical Trial Management applications… available for deployment in the cloud or on premises."

**Vendor's own category definitions (FAQ).**
- "What is clinical data management software?" → "Clinical data management software helps clinical teams capture, validate, and manage clinical trial data in a structured, traceable way. It supports consistent data collection across sites, improves oversight during study conduct, and helps teams maintain data quality throughout the trial lifecycle."
- "used for" → "design study data capture, apply edit checks and validation, manage changes over time, and support **clean exports** and reporting. It helps reduce manual reconciliation and improves visibility into study progress and data completeness."
- Quality & traceability → "supports data quality through controlled forms, validations, and consistent rules applied during data capture and review. Traceability comes from maintaining an auditable history of updates, approvals, and changes so teams can understand what changed, when, and why."
- Users → "data managers, clinical trial managers, CRAs/monitors, biostatisticians, and site teams. Sponsors, CROs, and research sites rely on clinical data management software to coordinate data capture and maintain study oversight across geographies."
- Selection criteria → "strong data validation, audit-ready traceability, role-based access, and the ability to configure workflows to match your study design and SOPs."

**Pain-point framing (the discipline's economics).** "Clinical trial data capture is only valuable when it is consistent, reviewable, and ready for downstream analysis. When data collection and management rely on manual handoffs, disconnected tools, or inconsistent definitions across sites, teams lose time to **reconciliation, query cycles, and late data cleaning**, and oversight becomes harder as study complexity grows."

**Platform shape.** CDMS described as "a structured foundation for capturing, validating, and tracking protocol-specific data throughout a study. Within that foundation, **electronic data capture (EDC)** supports efficient data entry and review through controlled forms and edit checks" — i.e., the vendor treats EDC as a capability inside the CDMS category. Sub-offerings: Ennov EDC (eCRF design, computed fields, dynamic field activation, configurable allowable-value libraries, online/offline entry), **Ennov RTSM** (randomization incl. stratification/minimization + trial supply management, integrated IWRS; "Data managers can define how randomization is requested, which parameters are used…"), **Ennov ePRO** (patient diaries/questionnaires, VAS scales, veterinary studies).

**Standards/compliance.** "Medical coding for **MedDRA and WHO Drug**"; "CDISC, **CDASH** and **SDTM** compliant"; 21 CFR Part 11 (on EDC, RTSM, ePRO); ISO 9001 & 27001; audit trails and e-signatures.

**Vendor-specific (L3):** MACRO EDC / DataLabs EDC product names; "unlimited number of strata" claims; 450+ customers / 500,000 users claims; single-tenancy; iPad camera attachment for eCRF; App Store availability; case-study stats (MHRA-approved platform, 100 trials, 13 years).

### CluePoints (Evidence layer: A — boundary anchor, RBQM/clinical data review pole)

- Self-positioning: "CluePoints is the leading **RBQM and clinical data review platform for Sponsors and CROs**, combining centralized risk detection, site-level action, **intelligent medical coding, safety review, and query detection** in a single, regulatory-grade, ICH E6(R3)-aligned platform."
- Enterprise framing: "Managing a global pipeline across multiple CRO partners, **EDC systems, CTMS platforms, and safety databases** demands oversight that scales" — treats EDC/CTMS/safety systems as external systems it oversees; the data-review layer is distinct infrastructure.
- Solution set: Central Monitoring Platform (CMP), Site Profile & Oversight Tool (SPOT), **Intelligent Medical Coding (IMC)**, **Medical & Safety Review (MSR)**, **Intelligent Query Detection (IQD)** ("Identify true data discrepancies with 80%+ precision, so your team can confirm findings rather than chase false positives"), Consulting & Services (CtQ framework, KRI/QTL design, "medical coding governance, safety review workflows, and inspection-readiness support").
- Regulatory frame: "ICH E6(R3) cements RBQM as a core GCP requirement… documented, proportionate, end-to-end oversight from protocol design through final study report."
- Serves: Large Pharma, Mid-Market Pharma, CROs.
- Vendor-specific (L3): product naming; 18,900+ users / 2,800+ studies / 320,000+ potential-issues claims; ~50% coding-effort reduction claim; 80%+ precision claim.

### SCDM (Evidence layer: A — profession anchor, non-vendor)

- "The Society for Clinical Data Management (SCDM) is an influential community that promotes industry best practices, education, and innovation." "As the go-to resource for clinical data management professionals worldwide, we are at the forefront of the industry's transition to clinical data science."
- **GCDMP©** ("Good Clinical Data Management Practices") — "GCDMP industry standards" knowledge bank; SCDM Knowledge organized into four "work streams" through "Clinical Data Management."
- **CDM Competency Framework** ("sets the gold standard for excellence… skills, knowledge, and behaviors needed for mastery in the CDM profession"); tiered certifications **CCDA / CCDM (Certified Clinical Data Manager) / CCDS**; global conferences; journal (JSCDM).
- Reading: "Clinical Data Management" is a formal, international profession with a codified practice standard — the software Type documents here is the tooling of that profession.

## Cross-product Comparison

| Dimension | OpenClinica | Ennov CDMS | CluePoints (adjacent pole) | SCDM (discipline) |
|---|---|---|---|---|
| Category self-name | EDC platform that consolidates "Clinical Data Management Tools" | **Clinical Data Management Software (CDMS)** — named product line | "RBQM and clinical data review platform" | profession: "Clinical Data Management" |
| Study-data record | study → sites → participants → events → forms (Participant Matrix view) | "structured CDMS foundation… capture and manage study data" | ingests data from external EDC systems | (practice standard, not product) |
| Validation | real-time edit checks; auto-generated Failed Validation Check notes; Rules | "validations, edit checks, and audit-ready traceability" | statistical/central risk detection; intelligent query detection | GCDMP covers data validation practices |
| Discrepancy/query loop | full thread model: types + status ladder + assignment + close (Tier-1 docs) | "query cycles" named as the pain the software reduces | IQD detects discrepancies; confirmation workflow | GCDMP query-management practice |
| Coding | OpenClinica Code (AEs, medications) | MedDRA + WHO Drug coding | IMC (intelligent coding) | coding governance in consulting/services |
| External data | import XML/tabular; import errors raise validation notes | "Easily import data, clean exports" | ingests multi-system data (EDC/CTMS/safety) | — |
| Review roles | Data Manager + Monitor (SDV) role guides | data managers, CRAs/monitors, biostatisticians | sponsor/CRO reviewers | CCDM certification |
| Lock/finalization | "database locks" ×3 mentions; Completing Your Study chapter; soft removal excluded from extracts | "clean exports and reporting"; "manage changes over time" | oversight "through final study report" | GCDMP standard |
| Export/analysis | Extract Data (CDISC ODM, SAS, SPSS, Excel, R/STATA) | CDISC/CDASH/SDTM compliant | inspection-ready evidence trail | — |
| Compliance posture | ICH GCP E6(R2), 21 CFR Part 11, HIPAA, GDPR, SOC 2, ISO 27001 | 21 CFR Part 11 ×3 products, ISO 9001/27001 | "regulatory-grade, ICH E6(R3)-aligned" | professional ethics/standards |
| Capture bundling | EDC is the platform's center; eCOA/eConsent/Randomization as modules | EDC + RTSM + ePRO inside the CDMS offering | none (works over external EDCs) | — |
| Deployment | cloud (mid-market, free study build) | cloud or on-premises, single-tenant | SaaS platform | — |
| Customer tier | academic, small-mid sponsors/CROs | pharma/biotech/medtech/academic, EU-flavored | large pharma, mid-market, CROs | — |

**Stable across the sample (B-layer):** study-scoped trial data as the governed record; validation rules applied against study-specific expectations; discrepancy/query records with responsibility-bearing status; a resolution loop reaching site contributors; medical coding against standard dictionaries; import/reconciliation of externally sourced data; role separation between data management, monitoring, and site entry; audit trail + GCP/Part 11 posture; extracts in analysis-oriented formats; "database lock" as the terminal controlled event (named directly by one product; implicit in "final study report" oversight framing and the discipline standard).

**Product-shaped (kept general in the final doc):** the exact discrepancy-record vocabulary (OpenClinica's four DN types / five statuses); Participant Matrix naming; RTSM/ePRO bundling (Ennov); free study build (OpenClinica); acquired EDC product lines (Ennov).

## Canonical Model

### L0 — Defining Invariant (deliberately small)

```text
Study-scoped clinical trial data as a governed record
  (per-study database; participant/visit-structured; attributable)
└── Validation against study-specific rules
    → discrepancy/query records with responsibility-bearing status
└── Resolution loop with data contributors
    (raise → assign → respond/correct → verify → close)
└── Controlled finalization
    (data declared complete/clean — the database lock —
     and extraction of analysis-ready data)
```

Four properties. Remove one and the Type stops being recognizable:
- without the governed study record, it is generic data-quality tooling;
- without rule-based validation producing discrepancy records, there is no data-management discipline (just capture);
- without the resolution loop, discrepancies never become clean data;
- without controlled finalization (lock + extract), the work never delivers the analysis-ready database that is the whole point.

**Audit-trail integrity** (attribution, no silent deletion, reason-for-change) is treated as part of the governed-record property, not a separate invariant — it is the mode in which all of the above is legally required to operate.

### L1 — Common Mature Structure

- Study build: form/eCRF design + the validation plan (edit-check specification) + coding conventions; study publication/versioning
- Data-entry surfaces for site contributors (in unified products the capture surface; historically paper keying / double data entry)
- Medical coding (AEs/medications/history against MedDRA/WHO Drug-class dictionaries) with coding discrepancies routed through the same query machinery
- External-data import & reconciliation (central labs, ePRO, devices, safety systems)
- SDV (source data verification) support for monitors; investigator e-signature of records
- Data-cleaning metrics: query aging, open-query counts, form completion, missing forms; dashboards per stakeholder
- Role-based permissions (data manager / monitor / coordinator / investigator / read-only consumers)
- Extract machinery: datasets, casebooks, analysis formats (CDISC ODM/SDTM-class, SAS/SPSS-class)
- 21 CFR Part 11 / ICH GCP compliance posture: audit logs, e-signatures, validated systems
- Soft-removal semantics: removal ≠ deletion; excluded from extracts; restorable with recorded reason

### L2 — Variant / Optional Structure

- Capture bundling posture: standalone-with-capture (dominant modern form) vs management-over-external-capture vs review-layer-only
- Paper-era heritage features: double data entry, form-version migration of keyed data
- RTSM (randomization/trial supply) and ePRO as in-category bundles (Ennov) or separate products (directory's own leaf split)
- EHR-to-EDC eSource flows; offline/iPad capture
- RBQM/central statistical monitoring as an overlay discipline (CluePoints pole)
- Deployment: cloud SaaS vs on-premises vs self-hosted open-source heritage; single- vs multi-tenant (CRO operation)
- Customer tier: academic/investigator-initiated vs pharma/CRO; mid-market vs enterprise suite membership
- Regional/regulatory flavor: ICH GCP is international, but marketing/posture varies (US Part 11 emphasis vs EU GDPR emphasis)

### L3 — Vendor-specific (research notes only)

- OpenClinica: Discrepancy Note four types (Failed Validation Check / Query / Reason for Change / Annotation) and five statuses (New / Updated / Resolution Proposed / Closed / Not Applicable); Participant Matrix; OpenClinica Insight (SQL access); OpenClinica Code / Randomize / Consent / Participate module names; "50% fewer queries" and 15,000-studies claims; free study build; "one-click study publishing"
- Ennov: MACRO EDC / DataLabs EDC / Ennov RTSM / Ennov ePRO product names; unlimited-strata claim; 450+ customers / 500,000 users claims; single-tenancy; iPad camera eCRF attachments; App Store availability
- CluePoints: CMP / SPOT / IMC / MSR / IQD product names; CtQ / KRI / QTL framework vocabulary; 18,900+ users / 2,800+ studies / 320,000+ issues / ~50% coding effort / 80%+ precision claims
- SCDM: GCDMP©, CCDA/CCDM/CCDS certification names, elev8, JSCDM

## Boundary Findings

### vs Electronic Data Capture / EDC (§22 sibling, unprocessed) — THE key finding; joint-review flag

The market's own terminology actively entangles the two directory leaves:
- Ennov groups MACRO EDC and DataLabs EDC **under its "Data Management" nav group** and states "EDC supports efficient data entry and review" **within** the CDMS foundation; its CDMS page covers capture machinery in detail.
- OpenClinica's EDC product page headline: "One EDC Platform. No More Switching Between **Clinical Data Management Tools**" — i.e., its EDC is marketed as consolidating the CDM-tool category.
- (Market context, no fetch: Medidata Rave is historically marketed as EDC/CDMS; Veeva names its product Vault CDMS with EDC inside. Not directly observed this pass — recorded as market expectation only.)

**Working seam proposed from the CDM side:** the two leaves document two disciplines over one shared substrate.
- *EDC leaf's center:* the capture instrument — form/eCRF design, site-facing data entry, event scheduling, real-time validation at entry.
- *CDM leaf's center:* the management discipline over the collected data — validation-plan ownership, discrepancy/query resolution, coding, external-data reconciliation, cleaning metrics, database lock, analysis-ready extraction.
- Empirically most products bundle both; historically (paper era) and in oversight-layer products (CluePoints) the management discipline exists **without** operating the capture instrument — so the capture side is not definitional for CDM.
- Recommended joint review when electronic-data-capture-edc is processed. Candidate outcomes: (a) keep both leaves with the discipline-vs-instrument seam recorded in both documents; (b) umbrella + slice. Do not silently merge.

### vs Clinical Trial Management System / CTMS (§22 sibling, unprocessed)

CTMS manages trial operations (sites, monitoring visits, milestones, budgets, documents); CDM manages trial **data**. Direct evidence of the seam: Ennov ships CTMS and Data Management as **separate solution groups**; CluePoints names "EDC systems, CTMS platforms, and safety databases" as three distinct external system classes. Clean boundary; no flag needed beyond awareness.

### vs Pharmacovigilance Platform (§22 sibling, unprocessed)

PV processes individual safety cases (ICSR lifecycle, expedited reporting); CDM cleans trial data. They share dictionary coding (MedDRA) and exchange AE data, but the record types and workflows differ (case vs data point). Evidence: Ennov separates the Pharmacovigilance suite entirely; CluePoints ships a distinct "Medical & Safety Review" product beside its coding product and names "safety databases" as external. Clean boundary.

### vs ePRO / eCOA and IRT/RTSM (§22 siblings, unprocessed)

Empirically these are often **bundled inside** CDMS offerings (Ennov puts RTSM and ePRO inside its CDMS page; OpenClinica ships Randomize/Participate modules). Bundling is packaging posture, not Type collapse: their record types (patient diary, allocation) differ from the study-data-record/cleaning core. Boundary note for those leaves' own passes.

### vs RBQM / central statistical monitoring (no dedicated §22 leaf identified)

CluePoints represents a real market category (sponsor-side data-quality oversight: central statistical monitoring, KRI/QTL, intelligent coding/query detection) that sits **above** EDC/CTMS systems. No obvious directory leaf in §22 carries it; closest neighbors are unprocessed siblings. Recorded as a possible taxonomy gap — flagged for human/taxonomy review rather than force-fitted here.

### Historical / market-sample check (§24)

- **Paper-era data management** (paper CRFs → data-entry clerks → double entry → manual validation → query forms → lock) satisfies the L0 definition with zero electronic capture, no cloud, no integrated coding — the definition does not over-fit the modern EDC-bundled form.
- **Academic/investigator-initiated studies** (OpenClinica's academic tier; lightweight deployments) satisfy the core with minimal machinery.
- **Non-US trials**: ICH GCP is an international standard; the sampled European vendor (Ennov) shows the same structure with EU compliance emphasis — the definition is not US-regulator-shaped.
- Therefore the invariant set (governed study record + validation→discrepancy loop + resolution + controlled finalization) is era-, region-, and deployment-independent.

## Uncertainties

1. **Enterprise-suite pole not directly observed.** Veeva, Medidata, Oracle (the largest vendors in this market) were unreachable this pass. Their shape (CDMS umbrella containing EDC) is inferred from Ennov's equivalent structure and market context; no claims about those specific products are made anywhere.
2. **"Database lock" as a named, universal feature.** Directly observed only in OpenClinica's product/analytics pages ("database locks", "before database lock", "Data managers planning database locks"). Ennov says "clean exports" / "manage changes over time" without naming lock; CluePoints frames oversight "through final study report". Lock is additionally supported as industry-standard practice by the existence of the SCDM discipline standard, but its chapter content was not fetched. Final doc states lock as the terminal controlled event with moderate-strong wording; exact lock criteria deliberately not enumerated.
3. **Double data entry** evidence is single-product (OpenClinica OC3 docs) → recorded as a historical variant, not generalized.
4. **Exact query-record states/types** are OpenClinica vocabulary → generalized to a conceptual status/responsibility model.
5. **Coding dictionary scope** (which dictionaries where) varies; MedDRA/WHO Drug observed in two sources (Ennov, CluePoints) — treated as common but not enumerated exhaustively.
6. Whether any products implement CDM **without any capture bundling at all** in the modern market (pure management-over-third-party-EDC) — CluePoints is close (review layer over external EDCs) but includes its own coding/review products; the pure form is hypothesized from the oversight pole, not confirmed as a standalone product category this pass.

## Final Synthesis

Clinical Data Management is the data-management discipline of clinical trials made into software. Its world: a **governed study database** (per-study record of participants, visits/events, and collected protocol data, attributable and non-deletable); a **validation layer** (study-specific edit checks and rules that raise **discrepancy/query records**); a **resolution loop** (queries assigned to site contributors, answered or corrected, verified and closed — with reason-for-change enforcement on completed data); **coding and reconciliation** (coded terms against medical dictionaries; external data imported and reconciled into the record); **cleaning oversight** (query aging, completeness, SDV status); and a **controlled terminal event** — the **database lock** — after which the record is declared complete and clean and analysis-ready data is extracted for statistics and submission. It is operated by sponsor/CRO data-management teams (a profession with its own standards body and certifications), with sites, monitors, coders, and statisticians as counterpart roles. In the modern market it is almost always bundled with data capture (EDC) and often with randomization/supply and patient-reported collection — bundling the final document records as posture, not definition. The sharpest taxonomy issue is the entanglement with the Electronic Data Capture leaf, flagged for joint review.
