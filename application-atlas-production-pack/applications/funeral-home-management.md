# Funeral Home Management

## Overview

A **Funeral Home Management** application is the operator-side business system of record for a funeral home. It organizes the home's entire work around the **funeral case** — one persistent, identified case per deceased person, opened at the first call and closed at final disposition — and carries, on that case, the custody and care of the deceased, the family's arrangement, and the legal paperwork that death care requires.

The defining structure is small:

```text
Funeral case of record
(one identified case per deceased person,
 from first call through final disposition)
├── Custody & care of the deceased
│   (where the body is, every transfer, the belongings
│    that came in with it — the chain of custody)
├── The arrangement
│   (the family-composed plan — disposition, services, merchandise —
│    priced from the home's price list and confirmed as the case's contract)
└── Statutory identity & authorization data
    (vital statistics for the death certificate, authorizations
     and permits, release forms — carried on the case, produced from it)
```

Everything else commonly associated with funeral home software — case types, service scheduling, staff coordination, payments and accounting, inventory, family portals, online arrangements — is standard capability layered on that spine. Remove the custody tracking, the arrangement, or the statutory paperwork, and the product is no longer a funeral home system: it is an event planner, a custody log, or a CRM with a calendar.

The center of gravity is the case plus the chain of custody: a funeral home's defining obligations are that the deceased in its care is always accounted for, that the family's plan is recorded and paid for as a contract, and that the paperwork for death, disposition, and release travels with the case.

## Users & Context

Primary users are the funeral home's own staff:

- **Funeral directors / arrangers** — take the first call, meet the family, conduct the arrangement conference, plan and oversee services; the case is their working file.
- **Administrators** — maintain cases, paperwork, contracts, payments, and records across the home.
- **Owners / managers** — oversee the whole operation: caseload, staff, schedules, finances, and (in multi-location firms) several homes from one system.
- **Care / preparation staff** — receive the deceased, record transfers and location, log preparation work, and manage personal belongings.

A second group participates without operating the system day to day: **families**. They sign contracts and authorizations (on paper or electronically), and in many modern products collaborate remotely — completing arrangements, uploading documents, viewing balances, and paying through a family-facing portal or online arrangement experience.

External partners appear at the edges: **answering services** that capture first calls into the system, **cemetery and crematory operators** who receive the deceased (sometimes connected by integration), **other funeral homes** in trade relationships, and **preneed providers** whose contracts a case may carry.

The operating context varies: traditional full-service homes, cremation-focused societies and disposition-only businesses, and combined operators running a funeral home alongside a cemetery or crematory.

## Core Model

### The Defining Core

**The funeral case.** The anchor object: one persistent, identified case per deceased person. It opens at the first call, accumulates everything the home does — identity details, family, custody events, arrangement, documents, money — and closes at final disposition. Cases are numbered, listed, filtered, searched, merged, and archived; the case listing is the home's daily working surface. Cases persist as the home's records, outliving the work they organized.

**Custody and care of the deceased.** From the moment of removal, the deceased is in the home's care, and the system records it: first-call and transfer details, location entries (facility, cooler, prep room, partner sites), every transfer between locations with who recorded it and when, and the **personal belongings** that came in with the decedent — each item logged with a disposition (remain with the decedent, return to family, dispose, donate), often with photos and signatures. In mature products this extends to scannable identification (QR/barcode tags assigned to the decedent) and mobile apps that timestamp each handoff, producing an auditable chain of custody that replaces clipboards and notebooks.

**The arrangement.** The family-composed plan, recorded on the case: the disposition method (burial, cremation…), the services (visitation, ceremony, their times and places), and the merchandise (casket, urn, memorial products). The arrangement is priced from the home's maintained **price list** of goods and services, assembled into a **contract** with the required disclosures, and confirmed by signature — after which the case's goods and services are locked into the home's accounting. Later changes are recorded as refunds and adjustments against the signed contract rather than silent edits.

**Statutory identity and authorization data.** The case carries the data the law requires: vital statistics and biographical details (the substance of the death certificate, including demographic fields), authorizations (for example, embalming authorization, cremation authorization where the home performs one), disposition permits, and release forms. The system holds this data as structured fields on the case and produces the documents from it — standard forms, custom templates, and, in some products, direct electronic submission of death registration to government systems.

Four properties, each with a removal test:

- Remove the **case of record** → there is no system, only scattered tools.
- Remove **custody and care** → nothing tracks the body the home is responsible for; it becomes an event planner with a forms clerk.
- Remove the **arrangement** → no funeral is being planned or sold; it becomes a custody log plus paperwork.
- Remove the **statutory data and authorizations** → the legal spine of funeral service disappears; it becomes a CRM with a calendar.

### What Mature Products Add

Standard capabilities found across mature products, which make the operation practical but do not define the Type:

- **Case types and conversion paths** — at-need (a death has occurred), pre-need (a plan made ahead), and imminent-need (death expected shortly) as the common trio; some products add trade cases (services performed for other funeral homes), cash sales (ancillary items such as extra death certificates), and pet cases. Pre-need and imminent cases convert to at-need when the death occurs, carrying their recorded wishes forward.
- **Service and resource scheduling** — a shared calendar for visitations, services, and removals; arrangement rooms, chapels, visitation rooms, vehicles, and staff as bookable resources; safeguards against double-booking; color-coded event types.
- **Task and staff coordination** — per-case tasks and checklists, staff assignments with acceptance and reminders, daily "whiteboard" views of the day's cases and services (digital, sometimes cast to displays), internal notes and messaging.
- **Payments and case-linked financials** — payments and adjustments on the case, receipts, card and ACH processing, invoicing (including trade and pet invoicing where supported), batch deposits, and export to bookkeeping systems; some products add insurance-assignment tracking, check writing, ledgers, and accounting controls.
- **Merchandise inventory** — caskets, urns, and memorial items tracked as inventory and linked to the price list and the case.
- **Document machinery** — standard forms attached to every case, custom templates with merge tags, obituary authoring and publishing to the home's website.
- **Family-facing collaboration** — online arrangements completed by families remotely, family portals for documents and balances, electronic signatures, planning pages that keep the family involved between conversations.
- **Dashboards and reporting** — configurable case listings and dashboards, status and tag filters, operational and financial reports.
- **Roles, permissions, and multi-location** — role-based access, branch-level configuration, consolidated reporting across several homes.
- **Integration spine** — answering services (first-call intake), print providers, electronic death registration, preneed providers, payment processors, websites, live streaming, aftercare services, and cemetery management systems.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:   Custody tracking
Implementations:  timestamped location entries recorded by staff;
                  QR/barcode tags scanned by mobile apps with GPS;
                  custody checkpoints inside the workflow

Concept:   The arrangement
Implementations:  staff-composed during an arrangement conference;
                  family self-service online arrangements;
                  hybrid — family drafts, staff finalize

Concept:   Statutory paperwork
Implementations:  structured vitals fields + printable standard forms;
                  custom document templates with merge tags;
                  electronic death registration integrations

Concept:   The contract
Implementations:  printed and hand-signed; e-signed remotely;
                  e-signed in person on a device
```

A reader who has only seen one product should still be able to recognize the others from the core.

## How It Works

The operational loop runs per case, with the case listing and calendar aggregating across cases:

### 1. Take the first call

```text
A death occurs → first call arrives (phone, answering service, online form)
→ a case is created for the deceased
→ first-call details captured: who died, where, when,
  who is calling, removal instructions
→ a transfer/removal is assigned to staff
```

The first call opens the case and starts custody. Some products let staff photograph or scan paperwork at the place of death and push it straight into the case from a mobile app.

### 2. Take the deceased into care

```text
Staff perform the removal
→ transfer and location recorded on the case (from → to, reason, time, by whom)
→ personal belongings logged with their disposition
→ the deceased moves between locations (cooler, prep room, chapel…)
→ every movement updates the chain of custody
```

### 3. Arrange with the family

```text
Arrangement conference (in person, or remotely via online arrangements)
→ disposition method, services, and merchandise selected
→ items priced from the home's price list
→ disclosures applied; contract generated
→ family signs (paper or e-signature)
→ goods and services locked to the case's accounting
```

Changes after signing are recorded as refunds and adjustments, and the contract is re-signed.

### 4. Prepare and schedule

```text
Care staff record preparation (where the product supports it:
authorization received, preparation status, dressing, appearance)
→ services placed on the shared calendar
→ rooms, vehicles, and staff booked; conflicts prevented
→ tasks and checklists assigned; the day's whiteboard updated
```

### 5. Hold services and dispose

```text
Visitation and ceremony held per the schedule
→ the deceased is transferred to the place of disposition
  (cemetery, crematory — recorded as a custody event)
→ disposition recorded on the case
```

Where the home operates its own crematory, the workflow carries the required authorizations, permits, and custody checkpoints inside the same case.

### 6. Complete the paperwork

```text
Vital statistics completed on the case
→ death certificate data filed or transmitted
  (print, or electronic death registration where integrated)
→ permits, releases, and certificates produced from the case
→ documents stored with the case
```

### 7. Settle and close

```text
Payments collected (at arrangement, or over time)
→ invoices and receipts issued
→ financials exported to the home's bookkeeping
→ case marked complete and archived — the record remains
```

## Interfaces

The following surfaces are described conceptually; exact names and layouts vary by product.

### Case listing / dashboard

The home's daily working surface.

- Purpose: see and work the active caseload.
- Typical information: case number, decedent name and date of death, case type, status, arrangement director, upcoming services; filterable by status, tag, and type.
- Primary actions: open a case, create a case, filter, search, work tasks.

### The case file

The spine of the product — a set of pages bound to one case.

- Typical pages: vitals/first call (identity and death details), family and friends (with planning roles), goods and services (the priced arrangement), payments and adjustments, documents and forms, care/custody (location events, belongings, preparation), schedule (the case's events), notes.
- Primary actions: record information, add contract items, sign, log custody events, generate documents, take payment.

### Care / custody view

The custody surface for care staff.

- Purpose: track where every decedent is and what came in with them.
- Typical information: current location, transfer history (from/to, reason, time, staff), personal belongings with actions and photos, preparation status and due dates.
- Primary actions: add a location entry, log a belonging, update preparation status, print custody or belongings reports.

### Calendar / schedule

- Purpose: coordinate services, removals, rooms, vehicles, and staff across the home.
- Typical information: events by day/week with color coding, resource bookings, staff assignments.
- Primary actions: create or move events, book resources, assign staff.

### Contract and payment surfaces

- Purpose: turn the arrangement into a signed, paid contract.
- Typical information: priced items with categories, disclosures, totals, signatures, payment history, balances, insurance assignments.
- Primary actions: add items, apply discounts, send for signature, take payment, print or email documents.

### Family-facing portal / online arrangements

- Purpose: let families participate remotely.
- Typical information: arrangement options and prices, documents to complete and sign, balances and payment.
- Primary actions: choose services and merchandise, complete forms, e-sign, pay.

### Settings and administration

- Purpose: configure the home's way of working.
- Typical information: price list, case statuses and tags, form templates, event types, users and roles, locations/branches, integrations.
- Primary actions: edit price list items and packages, manage templates, manage users and permissions, configure integrations.

## Important Rules / Behaviors

### Custody is continuous and attributed

From removal to disposition, the deceased always has a recorded location, and every transfer is a recorded event attributed to a staff member and a time. Custody does not lapse between steps; personal belongings follow the same discipline, with recorded dispositions and often signatures. This is the system's answer to funeral service's defining risk: a decedent or a belonging must never be unaccounted for.

### The paperwork travels with the case

Vital statistics, authorizations, permits, and releases are held as part of the case — not as side files — so the booking of a service, the custody of the body, and the legal documents all reference the same identified person. In several products the first-call form itself is shaped to capture jurisdiction-specific requirements.

### The signed contract locks the arrangement

Once the family signs, the case's goods and services become the accounting record of record. Later changes are recorded as refunds and adjustments with a re-signature, never as silent edits — the contract history stays reconstructable.

### Case types are a lifecycle, not just labels

Pre-need and imminent-need cases exist before a death and convert to at-need when it occurs, carrying recorded wishes forward. The conversion is a first-class operation, and pre-need selections are typically kept out of the home's revenue accounting until the death occurs and the case converts.

### The case is the home's memory

Cases persist after completion and are archived rather than discarded; the case listing, search, and reports work across years of history. Multi-location homes copy and consolidate cases across branches under shared definitions.

### Services are bound to the case

A scheduled service is not a rentable slot: it is bound to a decedent case, consumes the home's own rooms, vehicles, and staff, and carries custody implications (the deceased moves to and from it). Double-booking safeguards exist because the same hearse, chapel, or director cannot serve two cases at once.

## Variants

Common shapes of the same Type:

- **Traditional full-service home** — the classic shape: staff-led arrangements, visitation and ceremony services, merchandise sales, burial or cremation disposition, full back-office financials.
- **Cremation society / disposition-only business** — high-volume, lower-touch: online arrangements completed by families, simple price lists, drop-shipped merchandise, inquiry-stage records that convert into cases when a death occurs; custody tracking remains, ceremony machinery shrinks.
- **Combined operator (funeral + cemetery + crematory)** — the same case spine sharing one family record with cemetery and crematory modules; in-house cremation carries authorizations, permits, and custody checkpoints inside the funeral workflow.
- **Trade services provider** — a home serving other homes (removals, embalming, cremations) records that work as trade cases with their own contracts and invoices.
- **Website-led all-in-one** — management software bundled with the home's website, obituaries, online memorials, and marketing; the case spine is unchanged, the outward surface grows.
- **Regional and regulatory shapes** — price-list disclosures, death-certificate demographics, electronic death registration, and insurance-assignment payment patterns are jurisdiction-specific implementations; the core (case, custody, arrangement, statutory data) reads the same across jurisdictions, though the sampled documentation is US-heavy.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Crematory Management | holds the cremation **operation** — bookings, the cremation register, authorization paperwork, custody of cremated remains and their release. The funeral home holds the **case** — family, arrangement, custody of the deceased, disposition paperwork — and hands the deceased to the crematory. A funeral home's record of a cremation event is attached to its case; it is not a cremation register. |
| Cemetery Management | holds the **ground** — individually identified burial locations, the interment register, interment rights and deeds. The funeral home records disposition as data on the case (where and when), with no space inventory. Integration between the two is common; absorption is not. |
| CRM | records relationships with living customers and sales pipelines. The funeral system's organizing object is the decedent case with custody and statutory obligations; family records and pre-need prospects serve the case, not a pipeline. |
| Event Management / scheduling platforms | schedule occasions and rent resources. Funeral services are bound to a decedent case with custody obligations and statutory paperwork; rooms and vehicles are the home's own resources, not bookable inventory. |
| Preneed platforms | administer pre-need sales and trust products. The funeral system records pre-need cases and wishes, integrates with preneed providers, and converts cases at need; it does not administer the trust. |
| Aftercare / memorial platforms | serve families after the funeral (memorials, grief support, tributes). Funeral home software's center is the operator's case loop; memorial and aftercare surfaces are extensions. |
| Generic case management | tracks cases through statuses. The funeral case carries domain semantics generic tools lack: decedent identity, a custody chain, an arrangement-as-contract, and statutory data. |

The boundary with Crematory Management is the closest. The structural test: the funeral side's center of gravity is the case and the family; the crematory's is the register and the chain of custody of remains. Products from both sides document the seam — funeral case systems record cremation events on the case and hand off to crematories; crematory systems hold the operation without holding the funeral case.

## Representative Products

- Passare — case-first cloud funeral home system (chain-of-custody scanning, care center, family collaboration)
- Parting Pro — arrangement-first system oriented to cremation-focused homes and societies (online arranger, case management)
- PlotBox — deathcare platform whose funeral home module shares one record with its cemetery and crematory lines
- Tribute Management Software — operations-first "command center" extending case management to staff, schedule, and assets
- FrontRunner Professional (Pulse) — website-led all-in-one business system

Legacy vendors (SRS Computing, CRäKN, HMIS lineage) were unreachable during research; where documented, their absorption into current products is recorded in the paired Research Notes.

## Sources

Research date: **2026-09-08**

- Passare — support/help center (Getting Started; Managing Your Account; Accounting & Financials; Case types; Care Center; Goods and services; Vitals; Decedent tracking; Standard forms): https://support.passare.com/
- Passare — homepage: https://www.passare.com/
- Parting Pro — help center (Case Management collection; Care tab article): https://help.partingpro.com/en/
- Parting Pro — homepage: https://www.partingpro.com/
- PlotBox — Funeral Home Software (US): https://plotbox.com/funeral-home-software
- Tribute Technology — Tribute Management Software: https://www.tributetech.com/tribute-management-software
- FrontRunner Professional: https://www.frontrunnerpro.com/

> Sourcing limitation: two products (Passare, Parting Pro) were documented from their official help centers at operational granularity; the remaining three were documented from official product pages, so their capabilities are asserted at page granularity only. Several legacy vendors' sites were unreachable during research (two documented as absorbed into a sampled vendor from the acquirer's side), and no UK/EU funeral-management product was directly sampled — jurisdiction-specific details are therefore stated only where directly observed. Precise operational parameters (status vocabularies, limits, defaults, enforcement logic) are intentionally not stated; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the three-way boundary adjudication with the cemetery and crematory Types are recorded in the paired Research Notes.
