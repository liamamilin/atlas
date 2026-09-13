# Art Gallery Management

## Overview

An **Art Gallery Management** application is the operating system of a commercial art gallery. It keeps a record for every artwork the gallery handles, tracks where each work physically is and on what basis the gallery holds it, manages the gallery's relationships with collectors, and moves works through offer, invoice and payment to a recorded sale — including settling what is owed back to the artist or owner when a sold work was held on consignment.

The defining core is small:

```text
Artwork record (one specific physical work)
└── Custody & availability state
    └── Sale disposition (offer → invoice → payment)
        └── Client record linked to the sale
```

Everything else commonly associated with these products — consignment management, artist portals, exhibitions, certificates, websites, viewing rooms, mobile presentation apps, payment processing — is standard equipment in mature products but not what makes the category what it is. A gallery running on a desktop database or even spreadsheets satisfies the same core: a list of works, where each one is, who wants it, and what sold to whom.

When the commercial sale loop disappears — as in museum and collection stewardship software — the product belongs to a different Application Type, even though both sides speak the same language of provenance, condition and custody.

## Users & Context

Primary users, all inside one gallery business:

- **Gallery director / owner** — sets prices and consignment terms, approves offers and discounts, oversees the pipeline.
- **Sales directors / associates** — work the collector relationships: present works, send offers, follow up, close sales.
- **Registrar / inventory manager** — owns the artwork database: cataloguing, imagery, locations, movement, condition and provenance records.
- **Gallery assistant / registrar assistant** — updates records, prepares documents (price lists, labels, certificates), handles logistics.

Secondary users:

- **Artists and their studios** — in many products, submit new works or view their sales and inventory through a connected portal or account.
- **Accountants / bookkeepers** — receive invoices, payments and reports through exports or integrations.

The work context is distinctive: the merchandise is unique, high-value, and physically mobile. Works move between the gallery floor, storage, the artist's studio, framers, art fairs, and collectors' homes on approval. Sales are relationship-driven and often conducted remotely — a work is offered, held, invoiced and shipped rather than tendered over a counter. The software is therefore used continuously throughout the day from a web database, with mobile surfaces used in front of clients and at fairs.

## Core Model

### The defining core

**Artwork record.** The central object. One record represents one specific physical work — not a product type with stock quantity. A record carries the artist attribution, title, year, medium, dimensions, edition number where applicable, high-resolution imagery, price, and typically provenance and attached documents. Sold works remain in the database alongside available stock; the inventory spans "current and sold."

**Custody & availability state.** Each artwork has a physical location (gallery floor, storage room, artist studio, framer, art fair, a client's home) and a commercial status (available, on hold, on approval, sold, or returned to a consignor). Location and status are the two facts a gallery staff member needs most often, and mature products make both first-class, queryable fields with movement history.

**Sale disposition.** A work leaves availability through a tracked commercial loop: an offer or quotation to a specific client, optional hold or approval period, an invoice, and payment. The sale is recorded against both the artwork and the client, closing the work's availability.

**Client record.** Every sale has an identified counterparty. Client records hold contact details, interests (typically catalogued by artist and medium), purchase history, and follow-up notes. The link between clients, the works they bought, and the works they want is the gallery's relationship memory.

### Standard capabilities around the core

Mature products commonly add:

- **Consignment management** — works supplied by artists, estates or other owners (consignors) rather than owned by the gallery. The system records the consignment basis, terms and percentages, movements and returns, and — after a sale — the amount due to the consignor, settled through statements or payable reports.
- **Artist records** — profiles for represented artists, linked to their works, clients' interests, and (in many products) submission portals through which artists propose new works for review and acceptance into inventory.
- **Editions and prints** — handling for numbered editions of a work, where one image exists in multiple numbered copies.
- **Sales pipeline** — opportunities and offers with statuses, follow-up reminders, and staff attribution, often with commission tracking per salesperson.
- **Document generation** — invoices, quotations, certificates of authenticity, price lists, tear sheets, wall labels, insurance and valuation reports, usually produced from templates populated by the artwork record; some products also generate condition reports, in some cases through specialist condition-reporting integrations.
- **Exhibitions** — an exhibition record that binds a set of artworks, dates, press materials and installation photos, and can publish the show to the gallery's website.
- **Roles and permissions** — staff-level control over who can see prices and costs, edit records, or approve discounts, with change history and audit trails.
- **Reporting** — sales over time, outstanding payments, tax, consignment status, insurance valuations, top collectors and top-selling artists.
- **Publication surfaces** — a gallery website (or website integrations) that syncs with the inventory so availability changes update online automatically; private online viewing rooms for invited clients; e-commerce for select works.
- **Mobile presentation surfaces** — apps to browse and present works, send offers on the spot, and scan labels to pull up a record.
- **Payments and accounting handoff** — card and online payment acceptance on invoices, multi-currency handling, and exports or integrations to accounting systems.

### One structure, many implementations

The core is conceptual, and products implement it differently:

```text
Concept:  Custody & availability
Implementations:  location fields + status fields, check-in/check-out
                  against registered locations, movement history logs

Concept:  Sale disposition
Implementations:  offer pipelines that convert to invoices, direct
                  invoicing, point-of-sale style checkout for in-person
                  purchases

Concept:  Consignment settlement
Implementations:  payable reports per consignor, settlement statements,
                  automatically calculated amounts due from invoice history
```

## How It Works

### Cataloguing and intake

```text
A work enters the gallery's world
→ create the artwork record (artist, title, medium, dimensions, edition,
  imagery, price)
→ attach provenance, documents and condition information
→ record where the work physically is and its availability status
→ if the work is consigned: record the consignor and the agreed terms
```

In many products the artist (or their studio) initiates this by submitting the work through a portal; gallery staff review and accept it into inventory.

### Placement and movement

Works move constantly, and the record moves with them:

```text
Check a work out of storage → hang on gallery floor / send to art fair
→ place with a client on approval → return to stock or convert to sale
```

Each movement updates the work's location and often its status, so that at any moment the gallery can answer two questions: *where is this work?* and *is it available, and on what basis?*

### The selling loop

```text
Identify candidate works for a client (from interests and inventory)
→ send an offer or quotation (often as a branded PDF or private online room)
→ place the work on hold / send it on approval
→ client commits → convert the offer into an invoice
→ collect payment (card, online payment link, transfer)
→ issue the certificate of authenticity and arrange shipping
→ the work's status becomes sold; it leaves availability everywhere
  (inventory, website, future offers)
```

### Consignment settlement

When a sold work belonged to a consignor:

```text
Sale invoice recorded
→ system computes the consignor's share from the agreed percentage/terms
→ amount appears as due to the consignor
→ settlement statement or payable report issued; payment recorded
```

This closes the loop that makes consignment manageable at scale: the gallery can see, per artist or estate, what stock is held, what sold, and what money is owed.

### The relationship loop

Around sales runs a continuous relationship practice: record what each collector looks at and buys, tag interests by artist and medium, set follow-up reminders, announce new works and exhibitions (by email or private online rooms), and track event attendance. New inventory is matched against known client interests.

### Reporting and accounting handoff

Staff and owners report on sales, outstanding invoices, taxes, consignment balances and insurance values; invoices, contacts and payments flow to accounting systems through exports or integrations.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Artwork database (list and record detail)

The system's center of gravity.

- Purpose: hold and query every work, current and sold.
- Typical information: thumbnail, artist, title, year, medium, dimensions, edition, price, status, location, consignor.
- Primary actions: create/edit records, search and filter (by artist, status, location), flag works, generate lists and documents from a selection.

### Artwork record detail

- Purpose: the full dossier of one work.
- Typical information: imagery, details, price and cost, provenance, exhibition history, documents, location and movement history, linked offers/invoices.
- Primary actions: edit fields, upload images/documents, change status or location, attach to an exhibition or offer.

### Contacts / collectors

- Purpose: manage collector and artist relationships.
- Typical information: contact details, interests by artist/medium, purchase history, notes, correspondence.
- Primary actions: record interests, log interactions, set follow-ups, generate targeted lists.

### Sales pipeline / offers

- Purpose: track deals from interest to commitment.
- Typical information: client, offered works, amounts, status, responsible staff member, follow-up date.
- Primary actions: create an offer from inventory, send it, update status, convert to invoice.

### Invoices and payments

- Purpose: bill and collect.
- Typical information: client, works, prices, discounts, taxes, payment status.
- Primary actions: create invoice from an offer or directly, record payment, send payment links, credit notes.

### Consignments

- Purpose: manage works held from consignors.
- Typical information: consignor, terms/percentages, consigned works, movements, returns, amounts due.
- Primary actions: record a consignment, check works in/out, produce consignment reports and settlement statements.

### Documents and reports

- Purpose: produce the gallery's paper and digital output.
- Typical outputs: certificates of authenticity, price lists, tear sheets, wall labels, condition reports, insurance/valuation reports, sales and tax reports.
- Primary actions: select records, choose a template, generate and download/share.

### Website and viewing rooms

- Purpose: publish selected inventory to the public or to invited clients.
- Typical behavior: availability-driven sync (a sold work disappears from the site), online viewing rooms for private presentations, optional e-commerce.
- Primary actions: choose works to publish, build exhibition or viewing-room pages, review inquiries.

### Mobile presentation app

- Purpose: work in front of clients and at fairs.
- Typical actions: browse/search inventory, present works, send an offer on the spot, scan a label to retrieve a record.

### Settings, users and permissions

- Purpose: control the team's access.
- Typical content: user accounts, roles, visible price/cost fields, backup and security settings.

## Important Rules / Behaviors

- **One work, one state.** An artwork is a unique physical object: it can only be in one place and one commercial state at a time. Status and location changes are the system's most frequent edits, and conflicts (offering a work that is on approval elsewhere) are the failure mode this structure exists to prevent.
- **Availability is the master switch.** A work's status drives what can be offered and what appears on the website. Selling a work removes it from availability everywhere at once.
- **Consigned works are not the gallery's property.** Until sold, a consigned work belongs to the consignor; the gallery's obligation is custody, care and reporting. A sale creates a payable to the consignor computed from the agreed terms — the gallery's revenue is its share, not the full price.
- **Holds and approvals are real intermediate states.** A work on hold or on approval has physically or commercially left open availability; products track these states explicitly because they are where deals are won or lost.
- **Sold does not mean deleted.** Sold works remain in the inventory as records — for provenance, client history, reporting and future resale — which is why the database spans "current and sold."
- **Certificates follow the sale.** The certificate of authenticity is generated from the artwork record and issued with or after the sale; it is one of the document types the system exists to produce.
- **Money visibility is role-restricted.** Prices, costs and margins are sensitive; mature products restrict who sees them and keep change history for accountability.
- **The record is the archive.** Provenance, condition, exhibition history and documents accumulate on the artwork record over time; the system is the gallery's institutional memory for each work.

## Variants

- **Primary-market gallery** — represents living artists; heavy consignment intake from artist studios, artist relationships and submission portals dominate.
- **Secondary-market dealer** — trades works it owns or takes on consignment from collectors/estates; provenance, condition and authenticity documentation carry more weight.
- **Artist studio edition** — the same vendors sell a sibling product for artists themselves: portfolio and production replace consignment intake, and clients become direct buyers.
- **Collector / private collection edition** — inventory and custody without the sale loop; stewardship of an owned collection.
- **Multi-location and fair-heavy galleries** — multiple premises with their own branding and tax settings; seasonal intensive use around art fairs, with works shipped out and sold off-site.
- **Marketplace-participating galleries** — publication extends to third-party marketplaces or the vendor's own marketplace, beyond the gallery's own website.
- **Adjacent verticals** — the same structure is repackaged for other unique high-value-object retail (e.g., jewelry and boutiques), confirming that the core generalizes beyond fine art while keeping its unique-object shape.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | nearest neighbor, different mission | permanent collection under accession/deaccession, conservation and scholarship; no commercial sale loop — remove selling from gallery management and you get this |
| Artwork Consignment Management | narrower sibling | centers the consignor↔gallery relationship (agreements, movements, settlements) alone; gallery management embeds it as one capability inside the full inventory/CRM/sales world |
| Customer Relationship Management / CRM | component relationship | the collector side of gallery software is a CRM, but generic CRMs lack artwork inventory, custody and consignment semantics |
| Retail Point of Sale | different transaction shape | POS sells interchangeable stock over a counter with immediate tender; gallery sales are unique-object, relationship-driven, often remote and invoiced |
| Retail Inventory Management | different object model | manages stock quantities of SKUs; gallery inventory manages one record per unique physical work with custody and supply basis |
| Exhibition Planning Platform | container vs lifecycle | in gallery software an exhibition is a container binding artworks, dates and publication; exhibition planning as a standalone Type centers the exhibition lifecycle itself |
| Online Auction Platform | different price discovery | auction lots sell through bidding with hammer mechanics; galleries sell at (often negotiable) fixed prices through private offers |

## Representative Products

- **Artlogic** — UK-origin all-in-one platform (management database, websites, sales pipeline, marketing, payments) used by solo dealers through large multi-location galleries, with sibling editions for artists and collectors.
- **Art Galleria** — cloud art-inventory platform for small and mid-size galleries, strong in cataloguing, consignments, labels/QR output and private online viewing rooms.
- **ArtCloud** — US gallery manager with an integrated website builder and marketplace, point-of-sale style sales suite, and connected artist accounts for consignment and submissions.

These three were the researched sample; they differ in geography, tier and product philosophy while sharing the core model described above.

## Sources

Research date: **2026-09-06**

- Artlogic — product pages: https://www.artlogic.net/ , https://www.artlogic.net/products/gallery/management ; support help centre (Management, Sales, Websites, Mobile Apps sections) and the Artist Payables guide: https://support.artlogic.net/hc/en-gb
- Art Galleria — product pages: https://www.artgalleria.com/ , https://www.artgalleria.com/for-galleries
- ArtCloud — product pages: https://artcloud.com/ , https://artcloud.com/manager-for-galleries

> Sourcing limitation: a fourth candidate product (a mobile-first inventory and sales vendor) could not be fetched from the research environment and was excluded; no claims in this document depend on it. Two other well-known "art management" vendors were examined and found to have repositioned to museum operations and enterprise collection stewardship respectively; they informed the boundary with collection management but are not representative of this Type. Precise plan limits, prices and vendor-specific tool names are intentionally omitted from this document; they are recorded, where relevant, in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
