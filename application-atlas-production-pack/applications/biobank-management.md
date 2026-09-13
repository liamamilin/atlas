# Biobank Management

## Overview

A **Biobank Management** application is the operational system of record for a biorepository — a facility that preserves biological specimens (blood, tissue, DNA/RNA, cells, microorganisms, and similar material) for years or decades and makes them available for research use under defined governance.

Its job is to answer, at any moment and for any specimen: *what is this material, where exactly is it stored, where did it come from, who may use it and for what, and what has happened to it over its lifetime.* It replaces spreadsheets and paper freezer-box maps with a governed inventory in which every specimen is individually identified, every storage position is modeled, and every custody-affecting movement is recorded.

The defining core is small:

```text
Identified specimen inventory
└── Source / provenance linkage (donor, subject, organism, study, collection, or depositing client)
    └── Structured storage estate with tracked occupancy
        └── Recorded custody lifecycle
            (accession in → locate → move / reserve / release → ship or consume → dispose)
```

Everything else commonly associated with modern biobank software — aliquot genealogy, visual freezer maps, barcode and scanner workflows, request-and-ship distribution, consent management, temperature monitoring — is standard capability that mature products add to make long-term preservation operable, not what makes the product a biobank system.

## Users & Context

Primary users are the biobank's own staff:

- **Biobank technicians** — accession incoming specimens, aliquot and derive new units, place them into storage positions, pick requested specimens, prepare shipments, record disposal.
- **Biobank / repository managers** — own the collection structure, storage layout, governance rules, and the balance between preservation and distribution.
- **Quality / compliance staff** — maintain SOPs, review audit trails, prepare for accreditation and inspections, manage non-conformities.

Secondary users act on the collection from outside the storage room:

- **Researchers and study teams** — search the catalog, submit specimen requests, receive shipments.
- **Clinical / study coordinators** — register donors or participants, record consent, link collections to protocols and visits.
- **Facility / equipment staff** — maintain freezers and monitoring systems.

The work environment is a laboratory or storage facility: specimens arrive from collection sites or clinics, are processed at a bench, and live in freezers, refrigerators, and cryogenic tanks. The software is used at desks, at benches with barcode scanners and label printers, and increasingly on mobile surfaces inside the storage room itself.

## Core Model

### The Defining Core

**Specimen.** The central object is the specimen: an individually identified unit of biological material — a tube, vial, bag, straw, slide, or block. Specimens carry type (blood, plasma, tissue, DNA, cell line…), quantity, collection date, and configurable attributes. A specimen is unique and irreplaceable; unlike commercial stock, it cannot be reordered, which is why its identity, location, and history are tracked at unit level rather than as aggregate quantities.

**Source / provenance linkage.** Every specimen is tied to its source context. For human biobanks this is the donor or patient record, often organized in families, with consent records governing permitted use. For other collections the source may be an organism, an environmental sample, a study or protocol, a named collection (tumor bank, DNA bank, serum bank, strain bank), or a depositing client in a commercial storage service. Provenance is what gives the inventory its scientific value — a tube without its source context is anonymous material.

**Storage estate.** Storage is modeled as a structured hierarchy of units and positions — commonly site, building, room, freezer or nitrogen tank, rack, box, and position within the box. Products typically let the organization configure this tree freely and track occupancy: which positions are filled, by which specimen, and how much capacity remains. Mature products render this estate visually, so staff can see a freezer's layout and find a specimen's position without opening the door.

**Custody lifecycle.** A specimen moves through a custody lifecycle: accessioned in, placed into a storage position, possibly relocated or subdivided, reserved or checked out for use, shipped to a requester, consumed or exhausted, and finally disposed. Each custody-affecting movement is recorded with attribution — who did what, when. This recorded chain of custody is the audit backbone of the repository.

### Standard Capabilities of Mature Products

These capabilities appear across the researched products and make the core operable at scale:

- **Aliquot and derivative genealogy** — create child aliquots or derivatives from a parent specimen, deduct parent quantity automatically, pool specimens, and trace lineage in both directions (from a parent to all its derivatives and back).
- **Visual storage maps** — graphical representation of freezers, racks, and boxes with occupancy and capacity; drag-and-drop or scan-based placement; relocation of whole boxes or sections.
- **Label and scan machinery** — barcode or 2D-coded label printing (cryogenic-rated labels), rack readers that read a whole box at once, scan-based accessioning and box-level quality checks.
- **Requests and distribution** — researchers or teams submit specimen requests; staff approve, deny, or track them; picked specimens are packaged and shipped with chain-of-custody documentation; shipments are tracked to the recipient.
- **Specimen availability states** — each unit carries a state such as available, locked, requested, checked out, exhausted, or disposed; exact state sets vary by product.
- **Audit trail** — tamper-resistant, timestamped, user-attributed records of logins, data changes, structural changes, and deletions, framed to support regulatory expectations (for example 21 CFR Part 11 in US-regulated settings).
- **Consent and donor governance** — for human material: donor/patient records, consent capture and re-consent, restriction of use to consented purposes, and field-level protection of personally identifiable data.
- **Study, protocol, and collection context** — specimens organized under studies with arms, protocols with visits, specimen kits generated per visit, and named collections; cohort and longitudinal projects spanning multiple sites.
- **Search, reports, and dashboards** — multi-criteria search over any recorded field, saved searches, activity and inventory statistics, and data export.
- **Roles and permissions** — role-based access control, group-level visibility of samples, and field-level protection for sensitive clinical data.
- **Equipment and environment stewardship** — registry of storage equipment with maintenance and calibration records; temperature monitoring with alerts, either built in or integrated with third-party monitoring systems.
- **Multi-site operation** — compartmentalized data per site with configurable sharing and inter-site transfers, supporting multi-center cohorts and biobank networks.
- **Integration surface** — REST APIs, spreadsheet import/export, instrument and monitoring-system integrations.

## How It Works

### Accession a specimen into the repository

```text
Specimen arrives from a collection site / clinic / study visit
→ identify its source (donor, subject, organism, study, or client deposit)
→ record type, quantity, collection context, and attributes
→ print and apply a barcode label
→ assign (manually or automatically) a storage position in the estate
→ specimen is now in custody, at a known location, with full provenance
```

### Process and derive

Where protocols require it, staff aliquot or fractionate specimens: child units are created from a parent, parent quantity is reduced, and each child inherits lineage and provenance while receiving its own identity and storage position. Worklists and workflow rules can propose the next preparation step based on sample type and visit.

### Store, find, and verify

Day-to-day operation is a loop of placement and verification: specimens are placed into positions (manually or by barcode-driven auto-assignment), located on visual maps or by search, and verified by scanning boxes or racks against the recorded inventory. Expiry and quality alerts surface specimens or equipment needing attention.

### Fulfill a request

```text
Researcher submits a specimen request
→ biobank staff review against governance (consent, use restrictions, availability)
→ approve / deny / negotiate
→ pick specimens from storage (recorded as a custody movement)
→ package and ship with chain-of-custody documentation
→ track shipment; record receipt, return, or consumption by the recipient
```

### End of life

A specimen leaves the inventory by consumption (used up in analysis), exhaustion (quantity depleted), or disposal — each recorded, often under documented quality procedures for non-conforming or destroyed material. The record itself persists: a disposed specimen's history remains part of the repository's audit trail.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Specimen registry / search

The primary working surface for finding material.

- lists specimens with type, status, location, source, and key attributes
- multi-criteria search over any recorded field; saved searches
- primary actions: open a specimen record, build a worklist, export results

### Specimen detail

The full record of one unit.

- identity, type, quantity, source and consent context, lineage (parent/derivatives), status, complete event history
- primary actions: edit attributes, aliquot/derive, relocate, reserve, check out, dispose

### Storage map / explorer

The spatial surface of the repository.

- visual tree and graphical views of freezers, tanks, racks, boxes, and positions with occupancy and capacity
- primary actions: place a specimen, relocate units or whole boxes, check capacity, verify by scan

### Worklists and workflow queues

Task-oriented surfaces for daily operations.

- shared lists of specimens awaiting a step (accession, aliquoting, picking, QC)
- primary actions: execute the step, record the outcome, hand off to another user or site

### Requests and shipments

The distribution surface.

- incoming requests with requester, purpose, and requested specimens; approval state
- shipment preparation with chain-of-custody documents; shipment tracking
- primary actions: approve/deny, pick, pack, ship, record receipt

### Donor / subject / study records

The provenance surface for human and study-based collections.

- donor or participant identity (protected), family links, consent records and re-consent, protocol and visit structure
- primary actions: register, record consent, link collections and visits

### Dashboards and reports

Management and quality surfaces.

- inventory statistics, activity reports, storage utilization, expiry and equipment alerts
- primary actions: configure reports, export, schedule delivery

## Important Rules / Behaviors

- **Location fidelity is the core discipline.** The system's value depends on the recorded position matching physical reality; scan-based verification and box-level QC exist precisely to reconcile the two.
- **Every custody movement is an event.** Receipts, relocations, checkouts, shipments, and disposals are recorded with user and timestamp; the resulting chain of custody is the audit evidence regulators and accreditors expect.
- **Governance gates distribution.** A specimen's availability for a request is constrained by its status (locked, reserved, exhausted), by consent and use restrictions for human material, and by role permissions; approval is a recorded decision, not an informal handoff.
- **Lineage preserves provenance.** Aliquots and derivatives inherit their parent's source context; quantity deduction keeps the inventory truthful about what physically remains.
- **Sensitive data is protected at field level.** Donor identity and clinical attributes are access-controlled separately from the scientific inventory, with view-level auditing in regulated settings.
- **The storage estate is configuration, not code.** Organizations define their own hierarchy, container types, and storage constraints; products do not impose a fixed layout.
- **Equipment health is part of specimen integrity.** Freezer maintenance, calibration records, and temperature alarms are treated as specimen-protection infrastructure, not generic facility management.

## Variants

Common shapes of the same Type:

- **Hospital / clinical biobank** — human specimens collected under protocols; deep consent and donor governance; clinical annotations (for example tumor banks with pathology data); accreditation-driven quality systems.
- **Population cohort / longitudinal study repository** — multi-site collection over years; visit-based kits; compartmentalized multi-site data with inter-site transfers.
- **Cell line, organism, and strain repositories** — organism-level source linkage; sub-culturing and distribution of living material; less consent machinery.
- **Commercial biostorage and biospecimen services** — specimens held or distributed for clients; service catalogs (storage, testing, purchase requests), client portals, and billing.
- **Small team-lab inventory** — the same core (specimens, locations, movements, provenance) without distribution governance, used by a single research group.
- **Environmental / zoological collections** — non-human sources; provenance via organism, location, or expedition context.

A variant remains a variant of this Type as long as the defining core — identified specimens, storage occupancy, recorded custody, provenance — still describes it.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Laboratory Information Management System / LIMS | adjacent | LIMS is test/assay-centric: samples flow through processing to produce results. Biobank Management is custody-centric: specimens persist in storage awaiting governed use; testing is peripheral QC. Vendor labels like "biobanking LIMS" blur the naming, not the structure. |
| Blood Bank Management | adjacent | Blood bank units move donor → testing → issue to patient transfusion with short shelf life and transfusion-safety semantics. Biobank distribution ends at a research user under consent governance, with preservation horizons of years. |
| Research LIMS | sibling | Shares the research-lab context, but centers experiment and lab workflows rather than long-term specimen custody. |
| Electronic Lab Notebook / Scientific Data Management System | adjacent | Inventory exists there to document experiments and data (FAIR research data); in Biobank Management the inventory itself is the long-lived governed asset. |
| Inventory Management System | adjacent | Generic inventory tracks reorderable stock quantities; biobank inventory tracks unique irreplaceable units whose value lies in provenance, consent, and position fidelity. |
| Scientific Core Facility Management | adjacent | Manages facility services and resource booking; the biobank's managed object is the specimen inventory itself. |
| Research Animal Facility Management | adjacent | Manages animal colonies and husbandry; biobank manages preserved material derived from sources. |
| Clinical Trial sample systems (IRT/RTSM, CTMS) | adjacent | Trial specimen logistics may interoperate with a biobank, but trial systems center visit schedules, randomization, and kit supply — not permanent repository custody. |

## Representative Products

- **FreezerPro** (Azenta Life Sciences) — cloud and on-premises sample management with a "digital twin" storage representation, aliquot lineage, chain-of-custody documentation, and optional shipping/clinical modules.
- **Freezerworks** (Dataworks Development) — long-established sample management software (since 1987) with edition tiers scaling from team labs to study management with consent tracking and visit-based kits.
- **MBioLIMS BioBanking** (Modul-Bio) — modular, biobank-dedicated platform used by hospital resource centers and multi-site cohorts; consent, storage-tree, temperature-monitoring, and collection-catalog capabilities.
- **CloudLIMS** (CloudLIMS.com) — cloud SaaS biorepository LIMS emphasizing ISO 20387 accreditation support, chain of custody, genealogy, and commercial-biorepository service management.

## Sources

Research date: **2026-09-06**

- FreezerPro (Azenta Life Sciences) — product page and FAQ: https://www.azenta.com/products/freezerpro-sample-management-software
- Freezerworks (Dataworks Development) — homepage and features: https://www.freezerworks.com/ , https://www.freezerworks.com/freezerworks-features
- Modul-Bio — homepage and MBioLIMS BioBanking product page: https://www.modul-bio.com/ , https://www.modul-bio.com/nos-solutions/mbiolims-biobanking/
- CloudLIMS — homepage and Biorepository LIMS solution page: https://www.cloudlims.com/ , https://cloudlims.com/lims-solutions/biobanking-lims-software/
- openBIS (SIS) — homepage, used for boundary comparison only: https://openbis.ch/

> Sourcing limitation: research relied on official product pages, FAQs, and vendor-published case-study/testimonial summaries. Detailed user manuals and help-center articles were not reachable from the research environment. Claims in this document are therefore kept at structural and conceptual strength; precise numeric limits (storage capacities, position counts, license terms, workflow timings) are intentionally not stated. Detailed product-by-product observations are recorded in the paired Research Notes.
