# Research Notes — Integrated Library System / ILS

## Research Goal

Understand what an Integrated Library System actually is as an Application Type: what objects exist inside it, who operates it, how library work flows through it, and where its boundaries sit against the neighboring library-software Types already processed in this directory (library-discovery-platform, digital-library-platform, institutional-repository, archives-management-system, museum-collections-management, reading-library-application).

## Initial Boundary

Initial hypothesis: an ILS is the library's operational system of record — the staff-side software that runs cataloging, circulation, patron management, and acquisitions, with a public-facing catalog (OPAC) as one module. Nearest neighbors:

- **Library Discovery Platform** — patron-facing search layer over the library's resource universe (already processed; recorded seam: ILS = operational system of record, discovery = search-and-delivery layer; ILS's OPAC = thin ancestor)
- **Digital Library Platform** — host of curated digital collections (recorded seam: collection host vs circulation operations)
- **Institutional Repository** — host of the institution's own scholarly output (recorded seam: output host vs circulation operations)
- **Archives Management System** — description of unique non-circulating aggregations (recorded seam: published circulating items vs unique aggregations)
- **Museum Collections Management** — object-level custody vs bibliographic copies/circulation (recorded seam)
- **Reading Library Application** — personal book-record library (recorded seam: institutional vs personal; small-org lending variants graze the seam)

## Research Questions

1. What are the core objects of an ILS (bibliographic record, item/copy, patron, loan, order, …) and how do they relate?
2. What is the defining workflow loop (circulation)? What does check-out / check-in actually involve?
3. Which modules are universal across products (cataloging, circulation, patrons, acquisitions, serials, OPAC) and which are era/segment variants (ERM, preservation, point of sale, booking)?
4. How do circulation rules work (patron category × item type × location)?
5. How do multi-branch / consortium structures appear?
6. Where does the OPAC sit — part of the Type or a companion surface?
7. Is "Library Services Platform" (LSP) a different Type or a successor label for the same Type?
8. Historical check: does the definition survive the pre-digital library (card catalog, borrower card, date stamp)?

## Representative Products

Selected for market representability, documentation completeness, different product philosophies (community open-source vs commercial cloud), and different customer tiers (public libraries, academic libraries, consortia, national libraries):

| Product | Philosophy / tier | Documentation depth reached |
|---|---|---|
| **Koha** | first-generation open-source ILS (1999+, New Zealand public-library origin); self-hosted or vendor-hosted; worldwide public + academic | Tier-1 manual (full circulation chapter fetched) |
| **Evergreen** | open-source ILS built for a large public-library consortium (Georgia PINES); consortium-first design | Tier-1 docs (full TOC + circulation intro) |
| **FOLIO** | open-source Library Services Platform, modular app architecture; academic + consortia | Tier-1 docs (full TOC + welcome) |
| **Ex Libris Alma** | commercial cloud LSP, market-leading academic segment; consortium/network architecture | Tier-1 knowledge center (structure + community knowledge) |

SirsiDynix Symphony noted as the commercial incumbent anchor but not fetched (docs gated); no claims made from it.

## Sources

- Koha Manual (en), latest — https://koha-community.org/manual/latest/en/html/ — fetched 2026-09-10 (index, using-koha TOC, full circulation chapter)
- Koha community documentation page — https://koha-community.org/documentation/ — fetched 2026-09-10
- Evergreen Documentation, latest — https://docs.evergreen-ils.org/docs/latest/ — fetched 2026-09-10 (about + full TOC + circulation intro)
- FOLIO Documentation (Sunflower release) — https://docs.folio.org/docs/ — fetched 2026-09-10 (welcome + full TOC)
- Ex Libris Alma Knowledge Center — https://knowledge.exlibrisgroup.com/Alma — fetched 2026-09-10 (section structure, best-practice areas, community knowledge)
- Sibling passes recorded in STATUS.md: library-discovery-platform (2026-09-08), digital-library-platform (2026-09-07), institutional-repository (2026-09-08), archives-management-system (2026-09-10), museum-collections-management (2026-09-08), reading-library-application (2026-09-08)

## Product A — Koha

### Key observations (evidence layer A unless noted)

**Module map (manual "Using Koha" TOC):** Acquisitions, Cataloging, Circulation, Course reserves, ERM (Electronic resource management), ILL (Interlibrary loan requests), Lists and the cart, OPAC, Point of sale, Patrons, Preservation, Reports, Searching, Serials, Tools.

**Circulation (full chapter observed):**
- Check out: staff enters patron barcode/name → patron file → scan item barcode → due date computed from "circulation and fines rules"; options to override due date (permission-gated), automatic renewal, on-site checkout.
- Check-out blocking: patron owes too much in fines (threshold preference), patron restriction (overridable by staff with `force_checkout` permission), address confirmation flag, lost card, item lost status, item not-for-loan, too many checkouts, age-restricted material, item on hold for someone else, item already checked out.
- Renewals: from patron summary, from search bar, from Renew page; renewal limits from circulation rules; override permission; "unseen" renewal (renew without seeing item, e.g. by phone).
- Check in: scan barcode; settings for specify return date, book drop mode (roll back return date to last open day using the closed-days calendar), forgive overdue charges; messages: transfer required (item must return to home/holding library → status "in transit"), hold found (confirm → item waiting for pickup), patron notes on checkin, pieces/accompanying-materials confirmation.
- Holds: place in staff interface, manage (reorder queue, change level, suspend, delete), receive; reports: holds queue, holds to pull, holds awaiting pickup, hold ratios.
- Also: recalls, bookings (bookable items), curbside pickups, transfers, article requests, overdues with fines, in-house use tracking, self checkout, self check-in, offline circulation utilities (upload later), fast cataloging (add item on the fly during checkout).
- Permissions: `circulate` permission required for circulation functions; `force_checkout` for overrides; `superlibrarian`.
- Receipts: print slip / quick slip / summary / account balance / overdues / checkin slip; notices and slips customizable.
- Patron records: categories, restrictions, flags, fines/accounting tab.

**Cataloging:** MARC editing with value-builder plugins; the bibliographic record is MARC-based; item records (952 fields in MARC21) carry item-level data (barcode, status, location, lost status).

**Acquisitions:** separate module (selection lists, orders, vendors, funds — not fetched in depth this pass; module existence Tier-1).

**OPAC:** public catalog with patron self-service (renewals, holds, checkout notes "report a problem", lists/cart).

**Point of sale / cash management:** optional module for selling non-library items (e.g. printing, merchandise).

**Preservation:** optional module (recent addition).

## Product B — Evergreen

### Key observations

**Documentation structure (Tier-1 TOC):** System configuration (describing your organization — org unit trees; describing your people — patron data), Acquisitions (selection lists and purchase orders, invoices, patron purchase requests, blanket orders, claims), Cataloging (MARC editor, batch import, Z39.50 overlay import, authorities, holdings editor, item statuses, monograph parts, conjoined items), Staff Catalog, Serials (administration, receiving, routing lists, binding, holdings statements), Circulation (circulating items, holds management, billing, patron record, triggered events and notices, offline circulation, self checkout, booking module, curbside pickup), Reports, Public Access Catalog (my lists, my account, baskets), Course materials module, Integrations (EZProxy, PatronAPI, RESTful API, SIP server, OAI-PMH, Z39.50 servers, single sign-on, OpenAthens).

**Consortium-first:** "Describing your organization" = org unit tree; custom organizational unit trees; library groups; org unit proximity adjustments; hold targeting service; transit list; floating groups (items that stay at the borrowing branch); best-hold selection sort order. Built for a large multi-branch consortium.

**Circulation rules:** "Borrowing items: who, what, for how long" — loan periods, hard due dates, autorenewals, circulation limit sets; standing penalties; group penalty thresholds; billing types; cash reports (desk payments); credit card payments.

**Item status:** configurable item statuses (copy statuses); item alerts; statistical categories.

**Notices:** triggered events and notices (action/trigger framework); SMS/text messaging; hold-driven recalls.

**Self-service:** self checkout, SIP server (self-check machines), offline circulation, curbside pickup.

**OPAC:** public catalog with My Account, My Lists, metarecord holds; kids OPAC variant.

## Product C — FOLIO

### Key observations

**Top-level functional split (docs TOC):**
- Resource Access (Circulation): Check in, Check out, Circulation log, Courses, Reading room access, Requests; additional topics: Fees and fines, Loans
- Resource Management (Acquisitions): Claiming, Finance, Invoices, Orders, Organizations (vendors), Receiving, Serials Management; additional: central ordering, EDIFACT, invoice adjustments, order status
- Electronic Resource Management (ERM): Agreements, eHoldings, Licenses, eUsage, Local KB admin, ERM comparisons
- Metadata Management (Cataloging): Inventory, MARC authority, QuickMARC, Data import, Job profiles, Data export
- Users; Settings (per-module configuration incl. circulation rules, calendar, tenant, acquisition units); Reporting (Metadb, FOLIO Analytics, Reporting App); Lists; Bulk Edit; Export manager; Dashboard; Consortium manager

**Platform framing:** "open source Library Services Platform… moves the industry well beyond the traditional library management system" — modular apps on a platform; libraries choose service providers. The Type's functional content is the same as the traditional ILS; the packaging differs.

**Item status:** dedicated platform-essentials page — item status is a first-class concept.

**Consortium manager:** first-class multi-tenant consortial operation.

## Product D — Ex Libris Alma

### Key observations (structure-level; knowledge center fetched, deep pages not pulled)

**Knowledge-center section map:** Product Documentation (Alma Online Help), Best Practices and How-Tos grouped as: Acquisitions, Fulfillment, Resource Management (physical), Electronic Resource Management and the Community Zone, Analytics, APIs, Miscellaneous. Training tracks: Getting to Know Alma, Alma Administration, Collaborative Networks (Alma Consortia), Resource Sharing, Alma Digital, Analytics.

**Terminology observed:** "Fulfillment" = Alma's term for the circulation/resource-sharing function; "Resource Sharing" (lending/borrowing requests) as a first-class workflow; "Community Zone" (shared knowledge base of e-resource data); consortia via Network Zone (IZ/NZ institution/network zone split appears throughout community knowledge articles); Alma Digital as the digital-collection companion.

**Analytics:** a major section — evidence that reporting/analytics is a mature standard capability.

**Cross-record observation:** community articles reference physical items, portfolios (electronic), PO lines, funds, fiscal period rollover, fines and fees, course reserves, resource sharing — the same object world as the open-source products.

## Cross-product Comparison

| Structure | Koha | Evergreen | FOLIO | Alma | Verdict |
|---|---|---|---|---|---|
| Bibliographic catalog (MARC-based bib records) | ✓ | ✓ | ✓ (Metadata Management/Inventory) | ✓ (Resource Management) | universal |
| Item/copy records with barcode + status | ✓ | ✓ (item statuses) | ✓ (item status page) | ✓ (physical items) | universal |
| Patron/member records with categories & privileges | ✓ | ✓ | ✓ (Users) | ✓ (Users) | universal |
| Circulation: check out / check in / renew | ✓ | ✓ | ✓ | ✓ ("Fulfillment") | universal |
| Circulation rules engine (patron cat × item type × location) | ✓ (circulation and fines rules) | ✓ (circulation limit sets, loan periods) | ✓ (settings/circulation) | ✓ | universal |
| Holds / requests with queues & pickup | ✓ | ✓ | ✓ (Requests) | ✓ | universal |
| Fines/fees & patron account | ✓ | ✓ (billing, cash reports) | ✓ (Fees and fines) | ✓ (fines and fees) | universal |
| Acquisitions (orders, vendors, funds, invoices, receiving) | ✓ | ✓ | ✓ | ✓ | universal |
| Serials management | ✓ | ✓ | ✓ | ✓ | universal |
| OPAC / public catalog module | ✓ | ✓ | (pairs with discovery; FOLIO itself is staff-side) | (pairs with Primo) | universal in ILS-proper; discovery layer may be external |
| Cataloging machinery: Z39.50 copy cataloging, authority control, batch import | ✓ | ✓ | ✓ | ✓ | universal |
| Transfers / in-transit between branches | ✓ | ✓ (transit list, floating groups) | (locations) | ✓ | universal in multi-branch |
| Notices / overdue messaging | ✓ (notices & slips) | ✓ (triggered events) | (settings/notifications) | ✓ (letters) | universal |
| Reports/statistics | ✓ | ✓ (advanced reporter) | ✓ (Metadb/Analytics) | ✓ (Analytics) | universal |
| ILL / resource sharing | ✓ (ILL module) | (integrations) | (via requests/partners) | ✓ (Resource Sharing) | common |
| Course reserves | ✓ | ✓ (course materials) | ✓ (Courses) | ✓ (course reserves) | common (academic-weighted) |
| Self-service machinery (SIP2, self-check, offline circ) | ✓ | ✓ | (APIs) | ✓ | common |
| ERM (eHoldings, licenses, eUsage) | ✓ (recent) | — | ✓ | ✓ | common modern; era variant |
| Booking (bookable items/rooms) | ✓ | ✓ (booking module) | (reading room access) | — | optional |
| Point of sale | ✓ | — | — | — | optional, single-product in sample |
| Preservation | ✓ (recent) | — | — | (Alma Digital companion) | optional |
| Curbside pickup | ✓ | ✓ | — | — | era-specific (COVID-era), optional |
| Consortia / network-level operation | (hosting-dependent) | ✓ (org trees, floating) | ✓ (consortium manager) | ✓ (Network Zone) | common; segment variant |
| EDI/EDIFACT vendor ordering | (via integrations) | ✓ (EDI acquisitions) | ✓ | ✓ | common in acquisitions |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The bibliographic catalog of the institution's holdings** — persistent descriptive records of published works the library holds (bibliographic record), with copy-level records (items) attached carrying barcode, location, and status. Remove → a generic asset inventory or a search engine; the library's holdings account is gone.
2. **Patron records with borrowing privileges** — identified people registered with the library, carrying category, entitlements, and account state (blocks, charges). Remove → a catalog nobody can borrow from.
3. **The loan as the managed transaction** — check out (item × patron × due date under loan rules) → renew → return, with the item's status and location updated and the loan retained in history. Remove → a catalog + member database with no lending; the library stops being operated as a lending institution in the system.

Jointly-held load-bearing: (1 alone = bibliographic database / catalog; 2 alone = member CRM; 3 without 1+2 = a circulation log with no holdings or members; 1+2 without 3 = a catalog with registered users but no lending — not an operating library system).

### L1 — Common Mature Structure

- Acquisitions (selection → order → vendor → receive → invoice → fund accounting)
- Serials (prediction patterns, issue receiving, binding, routing)
- Holds/reservations with queues, pickup shelves, and hold-ratio reports
- Fines/fees with patron account and desk payments
- Renewals with limits and overrides
- Circulation rules engine (patron category × item type × branch → loan period/limits/fines)
- OPAC — public catalog with patron self-service (account, renewals, holds, lists)
- Cataloging machinery: MARC editor, Z39.50 copy cataloging, authority control, batch import/export
- Branch transfers with in-transit status
- Notices and slips (overdue, hold-available, receipts)
- Reports/statistics
- ILL / resource sharing
- Course reserves (academic-weighted)
- Self-service machinery: SIP2/self-check, offline circulation
- Multi-branch/consortial organization structure

### L2 — Variant / Optional

- ERM (electronic resources, licenses, eHoldings, usage data) — modern-era addition, absent in older systems
- Preservation module
- Point of sale / cash management
- Booking of bookable items (equipment, rooms, seats)
- Curbside pickup (era-specific)
- Discovery layer pairing (external product: Primo, VuFind, Summon, EDS) vs built-in OPAC
- Deployment: self-hosted OSS / vendor-hosted / SaaS
- Segment: public / academic / school / special / national library
- Consortial architecture: shared catalog vs independent institutions with resource sharing
- "Library Services Platform" packaging: cloud, multi-tenant, ERM-integrated, modular apps — same Type, successor architecture/label

### L3 — Vendor-specific (research notes only)

- Alma: Institution Zone / Network Zone, Community Zone, "Fulfillment" terminology, Alma Digital companion, Analytics evidence subject areas
- FOLIO: app-based modular architecture, tenant concept, Metadb/LDLite reporting stack, QuickMARC
- Koha: system-preference configuration surface, notices-and-slips tool, fast cataloging, item bundles
- Evergreen: OpenSRF middleware, hold-targeter service, floating groups, standing penalties, best-hold selection sort order

## Vendor-specific Findings

- Koha's Point of sale module and Preservation module are single-sample in this research — optional, not promoted.
- Evergreen's floating groups (items that remain at the borrowing branch instead of returning home) and standing penalties are product-specific mechanisms of universal concepts (branch logistics, patron penalties).
- Alma's IZ/NZ zone model is a vendor-specific consortial architecture; FOLIO's consortium manager is its counterpart. Consortial operation is common; the mechanism is vendor-specific.

## Boundary Findings

1. **vs Library Discovery Platform** — RATIFIED keep-both (discharges that pass's recorded recommendation). The ILS is the operational system of record: it owns holdings, loans, patrons, orders, and runs no cross-source search. The discovery platform is the search-and-delivery layer: it reads ILS holdings, forwards holds/ILL requests into the ILS, and runs no circulation or acquisitions. The ILS's built-in OPAC is the thin ancestor of the discovery platform and remains a complementary surface of this Type — not a submodule to merge. Removal tests: remove circulation/acquisitions from an ILS → it collapses toward a catalog + discovery surface; remove the library's holdings/entitlement from a discovery platform → it becomes an academic search engine.
2. **vs Digital Library Platform** — keep-both. The digital library platform hosts and delivers curated digital content (the collection is the product); the ILS operates the lending economy over physical (and cataloged electronic) holdings. Integration seam: catalog sync, discovery-layer delivery.
3. **vs Institutional Repository** — keep-both. IR hosts the institution's own scholarly output with an open-access delivery posture; the ILS operates circulation of published items the library acquires.
4. **vs Archives Management System** — keep-both. Archives describe unique, non-circulating aggregations via finding aids (a sampled archives product states it is not a circulation system); the ILS manages multiple copies of published items that circulate.
5. **vs Museum Collections Management** — keep-both. Museums hold unique objects with custody accountability; libraries hold copies of published works with circulation accountability. Different unit of record (object vs bibliographic copy) and different lifecycle (custody chain vs loan cycle).
6. **vs Reading Library Application** — keep-both. Personal book-record library vs institutional holdings operation. Small-org lending products (Libib-class) graze the seam but lack acquisitions/serials/circulation-rule depth; left as the personal Type's variant, consistent with that pass's recording.
7. **"Library Services Platform" (LSP)** — not a separate Type. Alma and FOLIO both self-describe with LSP-era language while carrying the identical functional content (cataloging + fulfillment/circulation + acquisitions + serials + ERM + patrons). LSP = cloud-era packaging variant of the ILS Type.
8. **vs Student Information System / School Management** — no seam issue: SIS manages enrollment/grades/attendance; the ILS manages lending of materials. Different object worlds despite coexisting in schools.

## Historical / Market-Sample Check

Pre-digital library operations: card catalog (bibliographic records), shelf list, borrower registration cards, date-due slips and the checkout desk ledger, acquisition order ledgers, serials check-in lists, the public card catalog as OPAC ancestor. All three L0 structures are satisfied with zero software: holdings description (card catalog + shelf list), patron registration (borrower card), the loan transaction (date stamp + due-slip + return). The "integrated" in the name refers to the 1980s innovation of merging previously separate modules (cataloging, circulation, acquisitions, serials) into one database — an implementation-era property, not part of the definition. MARC is the common implementation of the bibliographic record, not definitional (conceptual: descriptive record of a published work + copy-level records). The definition survives the historical check.

## Uncertainties

- SirsiDynix Symphony / BLUEcloud docs not fetched (gated) — market-breadth anchor only; no claims made.
- Alma deep operational pages not fetched this pass (knowledge center structure + community knowledge only); Alma claims kept at structure level.
- Koha acquisitions/serials chapters not fetched in depth; module existence is Tier-1, internal workflow detail not asserted.
- The exact boundary between "ILS with built-in OPAC" and "ILS + external discovery layer" varies by product and segment; treated as variant, not identity.

## Final Synthesis

An ILS is the library's operational system of record. Its defining core is three jointly-held structures: the bibliographic catalog of holdings (bibliographic records + item/copy records), patron records with borrowing privileges, and the loan as the managed transaction governed by circulation rules. Around this core, mature products add the acquisitions money path, serials, holds, fines, notices, reports, an OPAC surface, and multi-branch machinery; modern products add ERM, self-service, and consortial/network operation. The patron-facing discovery layer is a companion Type, not a submodule. "Library Services Platform" is the cloud-era packaging of the same Type.
