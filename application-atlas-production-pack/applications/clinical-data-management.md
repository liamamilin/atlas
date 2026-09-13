# Clinical Data Management

## Overview

**Clinical Data Management** software is the data-management system of clinical trials: it holds each study's collected trial data as a governed, attributable record, checks that data against study-specific validation rules, drives every problem it finds through a documented query-and-resolution loop with the people who supplied the data, reconciles external data sources and coded terminology into the record, and finally declares the record complete and clean in a controlled event — the database lock — from which analysis-ready data is extracted for statistics and regulatory submission.

Its purpose is the quality half of trial data work. Capturing trial data at sites is the territory of electronic data capture (EDC); running the trial's operations is the territory of a CTMS. Clinical data management is what happens to the data between those two: the sustained cleaning, verifying, and finalizing work performed by sponsor and CRO data-management teams, whose profession has its own international standards body, practice guide, and certifications. In the current market the software almost always bundles capture alongside management, and often randomization and patient-reported collection as well; that bundling is a packaging posture, not the substance of the Type. The substance is the governed study record and the machinery that turns raw trial data into a declared-clean database.

## Users & Context

The software serves a regulated production process with separated responsibilities:

- **Data managers** (lead and study-level) — own the study database, the validation plan, and the cleaning cycle; assign and close queries, manage coding, plan the database lock, and produce the extracts. The role is formalized in products as a distinct working mode and is a certified profession (clinical data management certifications exist with tiered credentials).
- **Site contributors** — study coordinators and investigators who enter and correct the data and answer queries about it; investigators electronically sign participant records.
- **Monitors / clinical research associates** — perform source data verification (checking recorded data against site source documents) and raise their own queries.
- **Coders and medical reviewers** — map reported adverse events, medications, and medical history to standard dictionaries; medical reviewers examine clinically sensitive findings.
- **Biostatisticians and downstream consumers** — receive the extracted, locked datasets; their requirements shape what "clean" means.
- **QA and regulatory staff** — consume the audit trail and documentation during inspections.

Operating contexts: pharmaceutical, biotech, and medical-device sponsors; contract research organizations running studies for sponsors (including multi-tenant, multi-study portfolios); and academic medical centers running investigator-initiated research under the same regulatory discipline. Deployments range from cloud services used by small and mid-size organizations to enterprise suites operated on-premises or in dedicated clouds.

## Core Model

### The Defining Core

The world of this application consists of four structures. If any one is removed, the software stops being clinical data management and becomes something simpler — a capture tool, a ticketing system, or a reporting layer.

**The governed study data record.** Each study has a structured record of its collected data: participants (subjects) organized under sites, with visits or events, each holding the protocol-specified data items — forms capturing diagnoses, medications, measurements, adverse events, and everything else the protocol requires. Every value is attributable (who entered or changed it, when, and why), and the record is deliberately non-destructive: nothing meaningful is silently deleted. This record is the system of record for the trial's data — the thing the rest of the machinery cleans, defends, and finally freezes.

**Validation that raises discrepancies.** Before data ever arrives, the study carries a validation design: edit checks and rules expressing what values and combinations are expected — ranges, required fields, logical consistency across items. When captured or imported data violates an expectation, the system automatically raises a **discrepancy record** (most of the market calls these queries). Data managers can also raise queries manually on values that pass automated checks but look wrong to a human. Each discrepancy attaches to a specific data element and carries a status that expresses who is responsible for the next action.

**The resolution loop.** A discrepancy is a conversation with an endpoint: the query is assigned to the person who can answer it (usually at the site), that person either corrects the data or explains it, the originator verifies the response, and the discrepancy is closed. Closed discrepancies are final — they are never deleted, even if raised in error, because the query trail is itself evidence. Changes to already-completed data force a recorded reason for change. This loop, repeated across thousands of data points and months of enrollment, is the heartbeat of the Type: capture creates data, the loop makes it clean.

**Controlled finalization — lock and extraction.** The work has a terminal event. When the study's data is in, discrepancies are resolved, and reconciliations are complete, the study database is **locked**: the record becomes read-only as the declared-clean, analysis-ready version of the trial's data. Data managers plan for this event throughout the study — dashboards track query aging and completeness precisely because open items block the lock. From the locked database, datasets are extracted for statistical analysis and submission. If something must change after lock, the unlock is a governed exception performed with a recorded reason and a re-lock.

### What Mature Products Add

Around that core, essentially all current products carry a common set of machinery:

- **Study build and versioning** — designing the data-entry forms and the validation rules from the protocol, publishing the study to sites, and migrating data safely when form versions change mid-study.
- **Data capture surfaces** — the forms sites use to enter data, with validation firing at the moment of entry; in the paper-era form of this discipline, keying and double-keying paper records played this role, and some products retain double data entry as a mode.
- **Medical coding** — mapping reported adverse events, medications, and medical history to standard dictionaries (MedDRA-class for reported terms, drug dictionaries for medications), with uncoded or ambiguously coded items routed back through the query loop.
- **External data reconciliation** — importing and reconciling data collected outside the study forms (central laboratory results, patient-reported data, device readings) against the clinical record, with import errors raising the same discrepancy machinery.
- **Source data verification support** — screens where monitors compare recorded data against source documents and mark verification status per form or per participant.
- **Cleaning oversight** — dashboards and reports of query aging by site and month, open query counts, form completion and missing forms, and verification progress; these are the instruments data managers use to steer the study toward the lock.
- **Extraction and formats** — dataset extraction in analysis-oriented formats and CDISC-family standards, plus participant casebooks for archival.
- **Regulatory-grade recordkeeping** — audit logs, electronic signatures, role-based access, and validated-system postures aligned with ICH GCP and 21 CFR Part 11-class requirements.

### One Structure, Many Implementations

```text
Governed study record:    per-study cloud database · on-premises deployment ·
                          self-hosted open-source lineage
Validation:               real-time checks at entry · batch rules over saved data ·
                          statistical/central review detecting discrepancies
Resolution loop:          in-product threaded queries · queries answered in the
                          site's capture surface · external review layers raising
                          findings back into the source system
Coding:                   integrated coding modules · separate coding products ·
                          intelligent/automated coding with human confirmation
Finalization:             named database-lock features · freeze-then-lock flows ·
                          soft removal and restoral of records with recorded reasons
```

A reader who has only seen one shape — a cloud platform where sites enter data and data managers chase queries — should still recognize the paper-era discipline of double-keyed records and paper query forms, and the sponsor-side review platform that watches another company's capture system, as the same Type.

## How It Works

### Study setup

```text
Protocol arrives
→ design the study data structure (forms per visit, items per form)
→ specify validation (edit checks, allowed values, consistency rules)
→ set coding conventions and external-data specifications
→ publish the study to sites and train roles
→ database goes live; data begins to arrive
```

Setup is where "clean" is defined. The validation rules fixed here determine every discrepancy the study will raise.

### The cleaning cycle (the defining loop)

```text
Data arrives (site entry, imports, patient-reported feeds)
→ validation fires automatically: violating values raise discrepancies
→ data managers review listings and dashboards; raise manual queries
   on values that passed checks but look wrong
→ queries are assigned to the responsible contributor (usually the site)
→ the contributor corrects the value or explains it
→ the originator verifies and closes the query
→ repeat continuously across the study's enrollment period
```

Alongside the query loop run the parallel work streams: coding (reported terms mapped to dictionary terms, coding questions routed through the same loop), source data verification by monitors, and reconciliation of imported data against the record. Dashboards of query aging, completeness, and verification status tell the data manager where the cleaning stands and which sites need attention.

### Locking and delivering

```text
Near study end: confirm all expected data is in, all queries are closed,
   all reconciliations and coding complete
→ database lock: the record becomes the declared-clean version
→ extract datasets for analysis and submission
→ any post-lock change is a governed exception:
   recorded reason → correction → re-lock
```

The lock is the deliverable. Everything in the Type exists to make that moment uneventful — which is why the metrics that matter during the study are precisely the ones that gate it.

### Who does what

Data managers live in the query worklist and the dashboards; they assign, chase, verify, and close, and they plan the lock. Site coordinators live in the forms; they enter, correct, and answer. Monitors work the source-verification screens. Coders and medical reviewers work their queues. Statisticians receive extracts, not screens. Every action lands in the audit trail with a name and a timestamp.

## Interfaces

Surfaces described conceptually; exact names and layouts vary by product.

### Study / participant data browser

The record's primary viewing surface — typically a matrix or list of participants by site, drillable into a participant's visits and forms.

- typical information: participants, sites, visit/event status, form completion, record flags
- primary actions: open a record for review, remove or restore a participant where the product offers it (recorded reason; removed records typically excluded from extracts), reassign a participant between sites, filter to active or removed records

### Query / discrepancy worklist

The data manager's and monitor's primary working surface.

- typical information: open queries by status, age, site, form, and type; who owes the next action
- primary actions: raise a query on a data point, assign it, respond, propose resolution, verify, close (closed queries remain visible, immutable)

### Data entry form (in products that bundle capture)

The site-facing surface where data arrives and validation fires at entry.

- typical information: protocol-defined forms per visit, field-level validation messages, entry state
- primary actions: enter and save data, mark forms complete, flag an item with an explanatory note instead of a value, sign records

### Coding workbench

- typical information: uncoded reported terms, dictionary candidates, coding status
- primary actions: select and verify dictionary terms, route ambiguous items to queries, record coding decisions

### Cleaning / oversight dashboards

- typical information: query aging by site and month, open query counts, form completion, missing forms, verification progress, adverse-event alerts
- primary actions: drill into cohorts and sites, redistribute workload, export reports for study teams and sponsors

### Extraction console

- typical information: dataset definitions, export formats, generated and archived files
- primary actions: define and generate datasets, download in analysis formats, produce casebooks

### Administration and audit

- typical information: user roles and study permissions, audit logs of every change, system configuration
- primary actions: grant and scope access, inspect the audit trail for any record, configure study parameters

## Important Rules / Behaviors

### Nothing is silently deleted

Discrepancy records, once raised, cannot be deleted — closing them is the only exit, and even a query raised in error stays in the trail. The audit trail — who changed what, when, and why — is the evidentiary spine of the whole system, because trial data is subject to regulatory inspection.

Removal of participants or data is typically implemented as a soft operation rather than a deletion: the record is retained and viewable but excluded from editing and extracts, restorable later, with the change recorded and a reason attached.

### Changes to completed data require a reason

Once a form or record is marked complete, edits force a recorded reason for change. This converts silent corrections into documented events and keeps the record's history defensible.

### Query status encodes responsibility

A query's status tells the organization who must act next: raised, awaiting response, resolution proposed, verified and closed. Only authorized roles can close a query. The loop ends only when the originator accepts the answer — the site's reply alone does not clean the data.

### The lock is gated and terminal

A database cannot be locked while expected work remains: open queries, incomplete forms, unresolved coding, or unreconciled external data each block the declaration. After lock, the record is read-only; changes happen only through a governed unlock with recorded reason and re-lock. Products present the gating criteria differently, but the pattern — clean-then-freeze, freeze-then-extract — is the discipline's shape.

### Separation of duties

Site contributors enter and explain data; monitors verify it against source; data managers control the record and close the loop; coding and medical review sit with qualified specialists. Access rights follow these roles, and the same value can be seen by everyone while being editable by only one of them.

### Validation is designed, not improvised

What counts as wrong is fixed at study build — allowed values, ranges, cross-field logic, required fields. The software can only be as good as the validation design, which is why rule specification is a first-class activity and why imported data is checked against the same rules as hand-entered data.

## Variants

- **Unified platform (dominant modern form)** — capture, management, coding, and often randomization/trial-supply and patient-reported collection in one product; the capture side is prominent but the management machinery remains the substance.
- **Management over external capture** — the record and its cleaning run against data collected in other systems; sponsor-side review and central-monitoring platforms operate this way, watching capture systems, operations systems, and safety databases from above.
- **Paper-era heritage** — keyed or double-keyed paper records feeding the study record; manual query forms; still legible in older product features (double data entry modes, form-version migration of keyed data).
- **Customer-tier variants** — academic and investigator-initiated studies (lightweight builds, template forms, grant-scale economics); small-to-mid sponsors and CROs; large pharma portfolios with enterprise governance.
- **Deployment variants** — cloud SaaS; on-premises or dedicated hosting for data-control-sensitive organizations; self-hosted open-source lineage.
- **Regulatory emphasis variants** — the same discipline under US (Part 11) or EU (GDPR-plus-GCP) emphasis; international ICH GCP is the shared floor.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Electronic Data Capture / EDC | closest sibling; usually bundled | the capture instrument — form design and site-facing data entry — is EDC's center; the validation plan's ownership, query resolution, coding, reconciliation, lock, and extraction are this Type's center. The market's own naming blurs them (products named CDMS contain EDC; EDC products claim to replace "clinical data management tools"), and the two leaves deserve joint review |
| Clinical Trial Management System / CTMS | adjacent, separately packaged | CTMS manages trial operations — sites, monitoring visits, milestones, budgets; this Type manages the trial's data. Suite vendors ship them as separate solutions |
| Pharmacovigilance Platform | adjacent | PV processes individual safety cases and expedited reporting; this Type cleans study data. Both code terms with MedDRA-class dictionaries, but the record types and workflows differ; safety databases appear here only as external data to reconcile |
| ePRO / eCOA and IRT / RTSM | adjacent, often bundled in | patient-reported collection and randomization/supply have their own record types (diaries, allocations); where a product bundles them into its data-management offering, bundling is packaging, not a change of Type |
| Data Quality / Data Catalog Platforms | name-adjacent, different world | generic data-quality tools profile datasets and enforce schemas; this Type's rules, queries, and lock are bound to clinical-trial semantics (visits, sites, protocol, GCP audit posture) and to a regulated profession's practice standard |
| Clinical Data Repository / Health Information Exchange | name-adjacent | those hold clinical care data for treatment contexts; no validation-plan, query-resolution, or database-lock discipline |

## Representative Products

- **OpenClinica** — eClinical platform for small-to-mid sponsors, CROs, and academic teams; its documentation is unusually explicit about the data-management role, discrepancy/query model, soft-removal semantics, and extraction formats
- **Ennov Clinical Data Management** — a vendor product line explicitly named "Clinical Data Management Software (CDMS)", with EDC, randomization/trial supply, and patient-reported collection inside the same offering
- **CluePoints** — sponsor/CRO-side risk-based quality management and clinical data review platform (central monitoring, intelligent coding, query detection) operating above capture and operations systems — the clearest representative of the management-over-external-capture shape
- **SCDM (Society for Clinical Data Management)** — included as the discipline's professional anchor: its practice standards and certifications define the profession this software serves (not a product)

The market's largest enterprise-suite vendors in this category (not directly verified this research pass) are conventionally counted here as well.

## Sources

Research date: **2026-09-07**

- OpenClinica — https://www.openclinica.com/ ; EDC solution page: https://www.openclinica.com/solutions/electronic-data-capture-edc/ ; Analytics: https://www.openclinica.com/solutions/clinical-data-reports-and-analytics/ ; Trust & Compliance: https://www.openclinica.com/trust-and-compliance/
- OpenClinica user documentation — https://docs.openclinica.com/ ; "Reviewing and Managing Data" (Data Manager guide): https://docs.openclinica.com/oc4/using-openclinica-as-a-data-manager/oc4-data-management/ ; "Notes and Discrepancies": https://docs.openclinica.com/3-1/openclinica-user-guide-submit-data-module-overview/openclinica-user-guide-monitor-and-manage-data-notes-and-discrepancies/
- Ennov — Clinical Data Management Software (CDMS): https://en.ennov.com/solutions/clinical/clinical-data-management/ ; corporate root: https://www.ennov.com/
- CluePoints — https://www.cluepoints.com/
- Society for Clinical Data Management — https://scdm.org/

> Sourcing limitation: several prominent vendors' official pages were unreachable from the research environment on 2026-09-07 (Veeva, Medidata, Oracle Health Sciences, Castor, REDCap, DATATRAK — abandoned after repeated failures) and are therefore represented here only as market context, with no product-specific claims. The enterprise-suite pole of the market is consequently documented through a structurally equivalent mid-market suite vendor's official pages. Exact lock criteria, query-status vocabularies, and numeric claims are deliberately not stated; product-specific findings (double data entry, named dashboards) are held to the sources that document them. Detailed product-by-product evidence, the cross-product comparison, and vendor-specific details are recorded in the paired Research Notes.
