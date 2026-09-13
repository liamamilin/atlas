# Electronic Data Capture / EDC

## Overview

An **Electronic Data Capture (EDC)** application is the capture instrument of clinical trials: a study-specific set of electronic case report forms, designed from the trial protocol and organized around participants and their scheduled visits, into which clinical site staff enter trial data while validation checks fire at the moment of capture — producing the trial's regulated, attributable record.

EDC exists to replace paper case report forms. Its purpose is not just digitization but **clean data at the source**: because the form structure, allowed values, and cross-field logic are designed into the instrument before the study goes live, errors are caught when the data is entered, at the site, rather than months later. Everything captured there becomes the trial's source record — the data regulators inspect and statisticians analyze.

Its boundary is deliberate: capturing trial data is EDC's territory. Cleaning, coding, reconciling, and finally declaring that data complete is the territory of **Clinical Data Management** — a discipline so entangled with capture in today's products that the two are usually sold together, yet conceptually distinct (see Related Application Types). Running the trial's operations — sites, visits, budgets — belongs to a CTMS, and the patient's own reporting belongs to ePRO/eCOA systems.

The defining core is small. Early remote-data-entry systems that replaced paper forms, and institution-hosted academic deployments built by self-service study builders, satisfy it as fully as modern cloud platforms — none of which require cloud delivery, integrated coding, standard-format exports, or AI assistance to be EDC.

## Users & Context

The software serves a regulated production process whose participants sit at different places in the trial:

- **Study builders / data managers (design side)** — translate the protocol into the capture instrument: forms, items, validation logic, visit schedules. In many studies they design the study themselves; in others a vendor or CRO builds it for them. Once the study is live, they also review data and manage queries within the same system.
- **Site coordinators (CRCs)** — the primary daily users. They enroll participants, schedule visits, complete the forms for each visit, correct data, and answer questions raised about it.
- **Investigators** — medically responsible for the data; they review and electronically sign participant records.
- **Monitors / clinical research associates** — verify that recorded data matches the site's source documents (source data verification) and raise their own questions.
- **Administrators** — manage users, roles, and study settings.

Operating contexts: pharmaceutical, biotech, and medical-device sponsors; contract research organizations running studies for sponsors; and academic medical centers running investigator-initiated research under the same regulatory discipline. Studies range from single-site to multi-national and multi-center; trial phases from first-in-human through post-market, plus observational designs and registries run in the same machinery.

## Core Model

### The Defining Core

```text
The Study-Built Capture Instrument
  (protocol-designed eCRFs: forms and items, organized per
   participant across scheduled visits/events)
└── Site-Based Data Entry
    (site staff enter participant data into the study's
     central database, form by form, visit by visit)
└── Validation at Capture
    (edit checks fire as data is entered and saved —
     ranges, required fields, logical consistency)
└── The Trial's Regulated Record
    (every value attributable, time-stamped, change-tracked;
     no silent edits; e-signatures; built for inspection)
```

Four structures. If any one is removed, the software stops being EDC:

- **The study-built capture instrument.** Every study has its own instrument, designed from its protocol before any data exists: which forms exist, which items each form collects, which items are required, what values are allowed, how fields compute or activate conditionally, and how forms are organized across each participant's visits and events. The instrument is built in a designer, tested, and published to go live — and it is versioned, because protocols change mid-study. Without the protocol-specific structure (participants moving through visits, forms attached to visits), the software is a generic form builder.
- **Site-based data entry.** Data is entered by clinical staff at the sites where participants are seen — not by the participant (that is ePRO/eCOA) and not by a central team transcribing documents (that was the paper-era pattern EDC replaced). Each participant has a record in the study's central database; entry proceeds form by form as visits occur, and the study's progress is visible as per-participant, per-visit completion.
- **Validation at capture.** The instrument carries the study's expectations — ranges, required fields, date logic, cross-field consistency — and applies them as data is saved. A value that fails a check is flagged immediately, at the point of entry. This is the property that gives EDC its reason to exist: the correction loop starts at the source, not downstream. Without it, the software is only a data bucket and all quality work would happen after the fact.
- **The trial's regulated record.** What sites enter is not a working copy; it is the trial's source data. Every value records who entered it and when. Changes — especially to already-completed data — leave traces and typically require a recorded reason. Records can be signed electronically. The audit trail is not a feature bolted on for compliance; it is the evidentiary spine that makes the electronic record substitutable for paper in a regulatory trial.

### What Mature Products Add

Around that core, essentially all current products carry a common set of machinery:

- **Study-build tooling** — drag-and-drop form designers, libraries of reusable and template forms (industry-standard form libraries), computed and derived fields, conditional display and activation, repeating item groups, allowed-value libraries and laboratory normal ranges, test/training environments, study publishing with go-live checklists, and generated blank/annotated form documents for protocol documentation.
- **Multi-site access machinery** — sites as an organizing layer, users provisioned per study and per site, role-based permissions that let the same data be visible to some and editable by others.
- **Query/discrepancy machinery** — failed validation checks automatically raise a query record attached to the data point; reviewers can raise additional queries manually. Query worklists are differentiated by role (the site answers, reviewers raise and close). The sustained loop of resolving these queries across a study is the working heart of the clinical-data-management discipline — EDC is where queries are born and answered, not necessarily where the cleaning program is run.
- **Data review surfaces** — participant matrices and listings, form and visit status states, completion and missing-form tracking, dashboards of enrollment, data-entry status, and outstanding queries per site.
- **Source data verification support** — screens where monitors compare entered data against source documents and mark verification status.
- **Medical coding integration** — reported adverse events and medications coded against standard medical dictionaries, either as an integrated module or an adjacent product.
- **External data import and integration** — importing lab results, device readings, and patient-reported data with the same validation applied to imports; APIs and standard interchange formats; increasingly, flows that populate EDC forms directly from electronic health records (eSource).
- **Finalization machinery** — database lock features and dataset extraction into analysis-oriented formats and standards, plus complete per-participant record exports. In products that separate an EDC product from a data-management product, this machinery may live on the data-management side.
- **Regulatory-grade infrastructure** — validated-system postures, encryption, access control, and audit logging aligned with ICH GCP and 21 CFR Part 11-class requirements.

### One Structure, Many Implementations

```text
Study-built instrument:   drag-and-drop designers · template libraries ·
                          expert-managed build services
Validation:               instant checks on save · re-evaluated on amendments
                          and imports · conditional logic engines
Entry surface:            web browser · tablet with offline capture ·
                          forms pre-populated from EHR/eSource data
The regulated record:     cloud-hosted database · on-premises deployment ·
                          institution-hosted deployments
```

A reader who has only seen one shape — a cloud platform where site coordinators fill in forms and validation messages pop up as they type — should still recognize an on-premises deployment keyed by double data entry from scanned paper, and a multi-national program whose forms are pre-populated from hospital records, as the same Type.

## How It Works

### Study build

```text
Protocol arrives
→ design the instrument: forms per visit, items per form,
   allowed values, computed fields, conditional logic
→ embed the validation design (what counts as wrong, decided here)
→ test in a test/training environment
→ publish the study; add sites; provision users by role
→ go-live checklist; the database opens for entry
```

Build is where the study's data quality is decided. Because validation is designed into the instrument, every check that will ever fire was specified before the first participant was enrolled.

### The capture loop (the defining loop)

```text
Site enrolls a participant
→ visits are scheduled per protocol
→ for each visit: complete the attached forms
   → validation fires on save: failures are flagged instantly
→ coordinator corrects or explains flagged values
→ forms are marked complete; investigator reviews and signs records
→ repeat across every participant, visit, and site
```

This is the daily loop of the trial's conduct phase, running concurrently at every site. Its outputs are captured data, instantly-checked data, and a visible per-participant completion state.

### Review alongside capture

```text
Failed checks raise queries automatically
→ monitors perform source data verification and raise their own queries
→ reviewers (data managers) screen the accumulating data
→ queries are assigned to the site; the site answers or corrects
→ the query cycle continues until the data is clean
```

The resolution machinery — assignment, follow-up, closure, and the metrics that track it — is operated as the clinical-data-management discipline. An EDC product hosts the surfaces where this happens; the discipline, its practice standards, and its professional roles are the sibling Type's subject.

### Amending the instrument

```text
Protocol amendment arrives
→ forms are versioned or redesigned
→ changes are validated (test environments, traceable deployment)
→ the running study is updated without downtime
→ existing data is migrated to the new form versions with its history intact
```

Mid-study change is a defining stress test of the Type: the instrument must evolve while the record it produced stays defensible.

### Close-out

```text
Enrollment ends; last data arrives; queries are resolved
→ the study database is locked (the record becomes read-only)
→ datasets are extracted for analysis and submission
```

Some products present lock and extraction inside the EDC product; others package them in a companion data-management product. The pattern — freeze the clean record, then extract — is shared.

## Interfaces

Surfaces described conceptually; exact names and layouts vary by product.

### Study designer / build surface

The builder's workbench, used before go-live and again at each amendment.

- typical information: the form tree by visit and event, item definitions, validation rules, computed fields, form versions
- primary actions: create and arrange forms and items, set validation and conditional logic, version forms, test, publish the study

### Participant matrix / study home (site view)

The site staff's primary entry surface — the study's population at a glance.

- typical information: participants by site, their visits/events, per-form completion and status, open queries
- primary actions: add a participant, schedule a visit, open a form for entry, filter and track completion

### Data entry form

The instrument itself, as the site experiences it.

- typical information: protocol-defined items for the visit, field-level validation messages, item states, signature status
- primary actions: enter and save data, correct flagged values, attach explanatory notes where a value cannot be supplied, mark the form complete, sign

### Query / clarification views

Where raised questions live, embedded in the form and in worklists.

- typical information: queries by status, age, site, and form; who owes the next action
- primary actions: answer a query, correct the data, raise a new query, verify and close

### Source data verification screens

The monitor's comparison surface.

- typical information: entered values against verification status, per form or per participant
- primary actions: mark values verified, reset verification, raise queries

### Oversight dashboards

- typical information: enrollment, data-entry status, outstanding queries and incomplete records by site, verification progress
- primary actions: drill into sites and participants, export reports

### Extraction and administration

- extraction: define and generate datasets, download in analysis formats and standard interchange formats
- administration: users and roles per study and site, audit logs of every change, system settings

## Important Rules / Behaviors

### Nothing is silently edited or deleted

The record is deliberately non-destructive. Completed data changed after the fact forces a recorded reason for change; removals are implemented as soft operations (retained, viewable, excluded from use) rather than deletions; the audit trail answers who changed what, when, and why for any value in the study.

### Validation is designed, not improvised

What counts as wrong is fixed at study build. Every automatic flag during the study traces back to a rule somebody specified in the designer — which is why build quality dominates data quality, and why imported data is checked against the same rules as hand-entered data.

### Roles are separated and scoped by study and site

Site staff enter and explain; investigators sign; monitors verify; builders and data managers control the instrument and the review process. Permissions attach to the study-site-role combination, so a user's powers differ per study and per site. The same value can be visible to all and editable by one.

### Forms carry states, and states protect the record

A form moves through states (in progress, complete, signed). Completing and signing restrict further editing; edits after that point require a reason and leave a trail. Query status encodes responsibility — whose turn it is to act — and a query's trail is kept even when raised in error.

### The lock is gated and terminal

The database cannot be locked while expected work remains open. After lock, the record is read-only; changes require a governed exception. Products present the gating criteria differently, but clean-then-freeze, freeze-then-extract is the shape of close-out.

### Entry is expected to be timely

The captured record substitutes for paper source documents in a regulated trial. Timeliness and attribution are therefore not UX preferences but protocol obligations — the system's dashboards and aging metrics exist to keep the loop moving.

## Variants

- **Deployment variants** — cloud SaaS (dominant), on-premises or dedicated hosting for data-control-sensitive organizations, and institution-hosted deployments with self-service study building (common in academic research).
- **Customer-tier variants** — academic and investigator-initiated studies (self-service builds, template forms, grant-scale economics) versus sponsor/CRO enterprise deployments (expert-managed study builds, validation services, portfolio-scale governance).
- **Scale variants** — lightweight editions for early-phase, post-market, and device studies versus global multi-national programs with thousands of site users.
- **Bundling-posture variants** — standalone EDC; eClinical suites where EDC sits beside eConsent, ePRO/eCOA, randomization/trial supply, and recruitment modules; vendors that ship EDC and a separate data-management/cleaning product; vendors that sell one unified study-data platform. The bundling is packaging; the instrument-plus-record core persists across all of them.
- **Capture-mode variants** — offline and tablet capture for low-connectivity sites; remote and hybrid capture; forms pre-populated from EHR data (eSource); decentralized-trial components feeding the same record.
- **Paper-heritage variants** — double data entry modes and migration of keyed paper data, legible in some products as legacy features.
- **AI-era variants** — AI-assisted study configuration; AI extraction of source documents into form values with human confirmation before commit. Emerging; not definitional.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Clinical Data Management | closest sibling; the flagged joint-review pair | EDC is the capture instrument — study-built forms, site entry, validation at capture, the regulated record. Clinical Data Management is the management discipline over the collected data — validation-plan ownership, query resolution, coding, reconciliation, cleaning metrics, database lock, and analysis-ready extraction. The market bundles them constantly (products named CDMS contain EDC; EDC products claim to replace data-management tools), and the largest vendors architecturally split them into separate products. Both leaves stand; the seam is instrument versus discipline |
| ePRO / eCOA Platform | adjacent, often bundled | patient-reported collection: the participant enters their own diaries and questionnaires, on their own devices. EDC entry is by site-based staff about protocol observations; different entrant, different record semantics |
| Clinical Trial Management System / CTMS | adjacent, separately packaged | CTMS manages trial operations — sites, monitoring visits, milestones, budgets. EDC manages the trial's data. Suite vendors ship them as separate solutions |
| Online Form Builder / Survey Platform | name-adjacent, different world | generic form tools share design-plus-entry-plus-validation, but lack the participant×visit protocol structure, site-scoped roles, the regulated record posture (GCP audit trails, e-signatures, inspection readiness), amendment machinery, and the analysis/submission pipeline |
| Electronic Health Record / EHR | adjacent data source | the EHR is the care record; the EDC database is the trial record. EHR-to-EDC and eSource flows pull care data into the instrument; they do not merge the Types |
| Electronic Trial Master File / eTMF | adjacent | eTMF holds the trial's documents; EDC holds its captured data values |
| Laboratory Information Management System / LIMS | name-adjacent | LIMS manages lab specimens and workflows; lab results arrive in EDC as external data to be reconciled |

## Representative Products

- **Medidata Rave EDC** — the enterprise market leader; its own product architecture (Rave beside a separate data-quality product and a separate study-build hub) makes the instrument-versus-discipline seam visible
- **OpenClinica** — EDC-centered eClinical platform for small-to-mid sponsors, CROs, and academic teams; open-source heritage; unusually explicit role-based user documentation (coordinator, investigator, monitor, data manager)
- **Ennov MACRO EDC / DataLabs EDC** — named EDC product lines within a European life-sciences suite that frames them inside a clinical-data-management offering; detailed study-design and data-input feature documentation; strong academic deployments
- **Castor** — cloud-first, self-service platform selling EDC and CDMS as separate products, with strong academic, biotech, and medical-device presence and decentralized-trial capabilities

## Sources

Research date: **2026-09-07**

- Medidata — Rave EDC product page: https://www.medidata.com/en/data-experience/edc-systems/ ; corporate root: https://www.medidata.com/
- OpenClinica — EDC solution page: https://www.openclinica.com/solutions/electronic-data-capture-edc/ ; user documentation root (OpenClinica 4 and OpenClinica 3 guides): https://docs.openclinica.com/
- Ennov — MACRO EDC product page: https://en.ennov.com/solutions/clinical/macro/ ; Clinical Data Management Software (CDMS) page: https://en.ennov.com/solutions/clinical/clinical-data-management/
- Castor — EDC product page: https://www.castoredc.com/electronic-data-capture-system/ ; corporate root: https://www.castoredc.com/
- Paired Research Notes (same date) record product-by-product observations, the cross-product comparison, and the joint review with the Clinical Data Management leaf (processed the same date from its own sources, including the Society for Clinical Data Management as the discipline anchor).

> Sourcing limitation: several prominent vendors' official pages were unreachable from the research environment (REDCap and Veeva failed repeatedly on 2026-09-07, and had also failed in the same-day sibling research pass). They are therefore represented only as unverified market context, with no product-specific claims. Enterprise-tier evidence rests on the market leader's own product page; the academic tier is evidenced through the sampled products' academic positioning and case studies. Exact query-state vocabularies, form-versioning procedures, numeric limits, and vendor performance claims are deliberately not stated in this document; they remain in the Research Notes.
