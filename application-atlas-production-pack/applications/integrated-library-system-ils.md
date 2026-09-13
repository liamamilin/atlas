# Integrated Library System / ILS

## Overview

An **Integrated Library System (ILS)** is the library's operational system of record: the staff-side application in which a library describes what it holds, registers who may borrow, and runs the lending of items — check out, renew, return — together with the money path that brings items into the collection.

The defining structure is small:

```text
Bibliographic catalog of the institution's holdings
└── Patron records with borrowing privileges
    └── The loan (item × patron × due date, governed by circulation rules)
        └── Check out → renew → return, with item status and history retained
```

Everything else commonly associated with library software — acquisitions, serials, holds queues, fines, the public catalog (OPAC), interlibrary loan, electronic resource management, consortial networks — is standard or optional capability layered on this core, not what makes the product an ILS. The name's word "integrated" is historical: it marks the era when cataloging, circulation, acquisitions and serials were first merged into one database. It describes an implementation achievement, not the definition.

When the dominant surface shifts to patron-facing search across many sources, the product is drifting toward a different Application Type (Library Discovery Platform). When the content itself — digitized collections or the institution's own research output — becomes the product, that is the Digital Library Platform or Institutional Repository territory.

## Users & Context

The primary users are library staff operating a library — public, academic, school, special, or national:

- **Circulation staff / librarians at the desk** — check items out and in, register patrons, collect fines, handle holds at the pickup shelf. Their work is barcode-scan-driven and high-volume.
- **Catalogers** — create and maintain the bibliographic records and item records that describe the collection.
- **Acquisitions / collection staff** — select, order, receive, and invoice materials; manage funds and vendors; check in serial issues.
- **Systems librarians / administrators** — configure circulation rules, patron categories, locations, notices, permissions, and integrations.

Secondary users are the library's patrons, who touch the system mainly through its public catalog surface (OPAC): searching the collection, checking their account, renewing loans, and placing holds.

The work environment is the library itself — service desks, back offices, and (in multi-branch systems) many branches or member libraries sharing one system, often as a consortium.

## Core Model

### The Defining Core

```text
Bibliographic record (a published work the library holds)
└── Item / copy record (a physical or cataloged copy: barcode, location, status)
    └── Loan (item × patron × due date, under circulation rules)
        └── Patron record (identified borrower with category, privileges, account)
```

Three properties. If any one is removed, the product is no longer recognizable as an ILS:

- **The bibliographic catalog of holdings** — persistent descriptive records of published works, each carrying copy-level item records with barcode, shelving location, and circulation status. This is the library's account of what it owns. Without it there is no collection to operate — only an inventory or a search engine.
- **Patron records with borrowing privileges** — identified people registered with the library, carrying a category (which drives their entitlements), account state (blocks, restrictions, charges), and loan history. Without this, the catalog serves no borrowing public.
- **The loan as the managed transaction** — checking an item out to a patron computes a due date from the library's circulation rules; the loan persists until the item is returned (or renewed), the item's status and location update with each step, and the loan is retained in history. Without this, the system is a catalog with registered users but no lending — a library that has stopped being operated as one.

### Capabilities Shared by Mature Products

These are not what makes the product an ILS, but they make operating a library practical:

- **Circulation rules engine** — the library's lending policy held as configuration: patron category × item type × branch determine loan period, renewal limits, fine rates, and checkout limits. This is the evaluative frame behind every loan.
- **Holds / reservations** — a patron requests an item; the system maintains a queue, targets a copy, routes it, and marks it waiting at the pickup shelf. Staff work from operational reports: holds to pull, holds awaiting pickup, hold ratios.
- **Acquisitions** — the money path into the collection: selection lists, purchase orders, vendor records, fund accounting, receiving, invoices, and claims for items that never arrive.
- **Serials management** — prediction patterns for expected issues, check-in of received issues, holdings statements, binding, and routing lists.
- **Fines and fees** — overdue and damage charges posted to the patron's account, payable at the desk or online, with waivers and credits.
- **Renewals** — extending a loan under rule limits, with staff override and (in many products) patron self-renewal.
- **Branch transfers** — items checked in away from their home location enter an in-transit state until received at their destination.
- **Notices and slips** — overdue reminders, hold-available notifications, checkout and check-in receipts; template-driven and configurable.
- **Cataloging machinery** — MARC record editing, copy cataloging by searching external bibliographic sources (Z39.50), authority control for names and subjects, and batch import/export.
- **OPAC** — the public catalog: search over the library's holdings, plus patron self-service (account, renewals, holds, lists).
- **Reports and statistics** — circulation counts, collection analysis, overdue lists, fund expenditure.
- **Interlibrary loan / resource sharing** — borrowing and lending between libraries as a managed request workflow.
- **Multi-branch / consortial structure** — the organization modeled as branches or member libraries with shared or independent holdings, locations, and policies.

### One Structure, Many Implementations

The core model is written conceptually. Implementations vary:

```text
Concept:      Bibliographic record
Realizations: MARC21/UNIMARC records (dominant), lighter record formats in small products

Concept:      Item / copy record
Realizations: barcode-identified item records, copy statuses, piece-level tracking

Concept:      Circulation rules
Realizations: rule matrices by patron category × item type × branch; limit sets; hard due dates

Concept:      Public catalog
Realizations: built-in OPAC module, or a paired external discovery layer reading the ILS's holdings
```

## How It Works

### The circulation loop (the defining workflow)

```text
Identify the patron (scan card / search name)
→ system shows patron state: privileges, blocks, outstanding charges, waiting holds
→ scan the item barcode
→ system evaluates circulation rules (patron category × item type × location)
→ computes due date; raises warnings or blocks
   (patron restricted, too many checkouts, item on hold for another patron,
    item not for loan, item lost, age restriction)
→ staff confirm or override where permitted
→ loan recorded; item status changes to checked out; receipt printed
→ later: renew (extend under rule limits) or check in
→ on check-in: fines resolved, holds triggered ("hold found → confirm → waiting for pickup"),
   transfers initiated if the item must return to its home branch
```

The loop is barcode-scan-driven and built for volume. Every step updates the item's status, the patron's account, and the loan history.

### Building the collection (acquisitions)

```text
Select titles (staff suggestions, patron purchase requests, vendor lists)
→ create purchase orders against funds
→ send to vendors (directly or via EDI)
→ receive items → item records created → cataloged
→ invoices matched and paid against funds
→ claims for undelivered orders
```

For serials, the same path runs on a prediction pattern: expected issues are generated, received issue by issue, and bound into volumes.

### Describing the collection (cataloging)

```text
Search an external bibliographic source (Z39.50) or import a batch file
→ copy or overlay the bibliographic record
→ edit locally (MARC editor, authority-controlled headings)
→ attach holdings and item records (barcode, location, status)
→ record becomes searchable in the catalog and publishable to the OPAC
```

### The patron's public surface (OPAC)

```text
Search the catalog → view record and availability
→ sign in → renew loans, place holds, view charges, save lists
→ hold becomes ready → pickup at the chosen branch
```

### Core vs Common vs Optional

**Defining core** — without these, not an ILS:

- bibliographic catalog of holdings (bib records + item records)
- patron records with borrowing privileges
- the loan transaction under circulation rules

**Common mature structure** — present in essentially all mature products:

- circulation rules engine, holds, fines/fees, renewals, acquisitions, serials, OPAC, notices, reports, branch transfers, cataloging machinery (Z39.50, authorities, batch import)

**Optional / variant** — depends on segment, era, and deployment:

- ERM (electronic resources, licenses, usage data) — modern-era addition
- interlibrary loan / resource sharing workflows
- course reserves (academic-weighted)
- self-service machinery (SIP2 self-check, offline circulation)
- booking of bookable items (equipment, rooms)
- point of sale, preservation modules
- curbside pickup (era-specific)
- consortial/network-level operation
- external discovery layer instead of built-in OPAC

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Circulation desk (check out / check in)

The highest-traffic staff surface.

- patron lookup, item barcode field, current-loan summary, warning and block dialogs
- primary actions: check out, renew, check in, pay fines, print receipts, override (permission-gated)

### Patron record

The borrower's account of record.

- identity, category, addresses, privileges, blocks/restrictions, charges and credits, loan history, holds
- primary actions: register/edit patron, add block or flag, collect payment, renew or check in loans, place holds

### Cataloging editor

The bibliographic workbench.

- MARC record editor, authority lookup, holdings/item attachment, batch import queues
- primary actions: import/copy record, edit fields, attach items, save/publish

### Acquisitions workspace

The ordering money path.

- selection lists, purchase orders, vendor records, funds, invoices, receiving
- primary actions: create order, receive, match invoice, claim, close order

### Serials module

- prediction patterns, expected-issues grid, check-in, binding, routing lists

### Holds management

- queues (holds to pull, awaiting pickup), hold details, suspension, reordering
- primary actions: pull, mark waiting, cancel, suspend

### OPAC (public catalog)

- search, record detail with availability, patron account (loans, holds, charges, lists)
- primary actions: search, place hold, renew, pay charges, save to list

### Administration / settings

- circulation rules, patron categories, item types, locations/branches, notices templates, permissions, integrations

## Important Rules / Behaviors

### Circulation rules decide every loan

The due date, renewal eligibility, fine rate, and checkout limits are not set per transaction — they are computed from the library's rule configuration (patron category × item type × branch). Staff overrides exist but are permission-gated and recorded.

### Check-out can be blocked, and blocking is visible

A patron may be blocked by outstanding fines above a threshold, an account restriction, an unconfirmed address, or a lost card. Items can be blocked by not-for-loan status, hold placement for another patron, or lost status. Blocks surface as explicit messages; some are overridable by privileged staff, others are not.

### Check-in is not just "return"

Checking in an item can trigger a chain: a hold found on the item moves it to the pickup shelf; a return-policy mismatch initiates a transfer with an in-transit status; book-drop mode can roll the effective return date back to the last open day; fines may be forgiven at check-in. The item's status — not the patron's — is the state that drives the shelf.

### Items have a status lifecycle

Available → checked out → in transit → waiting (hold) → overdue → lost/missing → withdrawn. Exact status vocabularies vary by product, but the conceptual states are stable across the Type, and the item record is where they live.

### The catalog is shared; the loan is singular

Many patrons can be interested in one bibliographic record; an item (copy) can be in only one loan at a time. Holds exist precisely because copies are scarce relative to demand — hold queues and hold-ratio reports are the system's demand-management surface.

### Patron privacy and history

Loan history is sensitive; products differ in what history is retained and who may see it. Patron data handling is a structural concern of the Type, not an afterthought.

## Variants

- **Public-library ILS** — circulation-heavy, branch networks, patron self-service, community programs; often consortium-operated.
- **Academic ILS** — acquisitions and serials depth, course reserves, electronic resources, integration with campus identity and link resolvers.
- **Consortial / network ILS** — many member libraries on one system: shared catalogs, union holdings, cross-branch holds and transits, network-level administration.
- **Library Services Platform (LSP)** — the cloud-era packaging of the same Type: multi-tenant SaaS, electronic resource management integrated, modular architecture. Functionally an ILS; the label marks the architecture generation.
- **Open-source self-hosted vs vendor-hosted vs SaaS** — deployment variants of the same core.
- **Small-library / school variants** — lighter packaging, same core structures.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Library Discovery Platform | patron-facing search-and-delivery layer over the library's resource universe; reads ILS holdings and forwards holds/ILL into it; runs no circulation, acquisitions, or patron accounts. The ILS's built-in OPAC is this Type's thin ancestor and complementary surface |
| Digital Library Platform | hosts and delivers curated digital collections — the content is the product; the ILS operates the lending economy over holdings |
| Institutional Repository | hosts the institution's own scholarly output with an open-access posture; the ILS operates circulation of acquired published items |
| Archives Management System | describes unique, non-circulating aggregations of unpublished materials via finding aids; the ILS manages multiple copies of published items that circulate |
| Museum Collections Management | unique objects with custody accountability; the ILS holds copies of published works with circulation accountability — different unit of record and lifecycle |
| Reading Library Application | a personal book-record library; the ILS is the institution's holdings operation. Small-organization lending products graze this seam but lack the acquisitions/serials/circulation-rule depth |
| Student Information System | manages enrollment, grades, attendance; the ILS manages lending of materials — coexisting in schools but different object worlds |
| E-book Library Application | holds book content for reading; the ILS holds records about items the library lends |

The most important boundary is with the Library Discovery Platform: the two Types are ecosystem partners — the discovery layer is the search surface over the ILS's holdings, and the ILS is the operational record behind it. One product suite may ship both, but they remain distinct Types.

## Representative Products

- Koha — open-source ILS, worldwide public and academic libraries
- Evergreen — open-source ILS built for large public-library consortia
- FOLIO — open-source Library Services Platform, modular architecture
- Ex Libris Alma — commercial cloud Library Services Platform, academic segment

The core model was checked against the pre-digital library (card catalog, borrower registration, date-due desk) to avoid over-fitting to the modern integrated-database implementation.

## Sources

Research date: **2026-09-10**

- Koha Manual (en), latest — https://koha-community.org/manual/latest/en/html/ (manual index, module map, circulation chapter)
- Koha community documentation — https://koha-community.org/documentation/
- Evergreen Documentation, latest — https://docs.evergreen-ils.org/docs/latest/
- FOLIO Documentation (Sunflower release) — https://docs.folio.org/docs/
- Ex Libris Alma Knowledge Center — https://knowledge.exlibrisgroup.com/Alma

> Sourcing limitation: SirsiDynix product documentation was not accessible from the research environment; it is cited as a market anchor only, with no operational claims. Alma evidence is at knowledge-center structure level; deep operational pages were not fetched. Claims in this document are calibrated accordingly — precise numeric limits, thresholds, and defaults are intentionally not stated.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary reasoning are recorded in the paired Research Notes.
