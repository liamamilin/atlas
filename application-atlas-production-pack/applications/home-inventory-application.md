# Home Inventory Application

## Overview

A **Home Inventory Application** keeps a detailed, organized record of the possessions in a household: what the household owns, what each thing is, what it is worth, where it is kept, and the documentation that proves it — photos, receipts, serial numbers, manuals.

The defining structure is small:

```text
The household's own home as the bounded scope
└── The item of record (one persistent record per possession)
    └── Descriptive and documentation attributes (product-chosen:
        name, category, photos, purchase details, serial, value,
        condition, documents, notes)
        └── The inventory maintained as a standing whole
            (kept current, answerable in aggregate)
```

Everything commonly associated with the category — room-by-room organization, item photos, QR labels, cloud sync, family sharing, insurance-policy machinery, coverage analysis, estate reports, moving checklists — is widespread in current products but is not what makes a product a home inventory. A written list of belongings with values kept for the insurer, or a spreadsheet with one row per possession, satisfies the same core. Conversely, a business's stock system or an organization's asset registry does not, because the subject is not a household's own things.

When the record stops belonging to the household — when a professional documents someone else's property for a specific insurance claim, or when the possessions catalog becomes one tab inside a whole-home binder — the product is drifting toward a different center of gravity.

## Users & Context

The primary user is a household member — a homeowner or renter — who builds and maintains the record of their own things. Typical moments of use:

- **Building the inventory**: walking the home room by room, photographing and describing belongings, often soon after moving in or after a scare (a burglary in the neighborhood, a neighbor's fire).
- **Keeping it current**: adding an item shortly after buying it, attaching the receipt, updating location after rearranging, removing things that were sold, given away, or discarded.
- **Using the record**: after a loss (fire, flood, theft), to file and support an insurance claim; when checking whether insurance coverage is adequate; when preparing to move; when settling an estate; when trying to remember what is in a box, a storage unit, or a closet.

Secondary users are the rest of the household: partners and family members who share and update the same inventory, and household members consulting it during a claim, a move, or an estate settlement. Some products also expect the record to be shown to outsiders — an insurance adjuster, a police officer, an estate lawyer — which shapes what the record must contain.

The work environment is the home itself. Capture is typically mobile (photographing items in place), while deeper cataloging — attribute entry, document attachment, report generation — commonly happens on a desktop or web surface sharing the same data.

## Core Model

### The Defining Core

Three structures, jointly held. If any one is removed, the product is no longer recognizable as a home inventory:

- **The item of record** — a persistent, individually identified record for each physical possession. The record carries descriptive and documentation attributes; which attributes a product chooses varies (name, category, photos, purchase price and date, serial or model number, condition, value, receipts, manuals, notes), but the per-possession record itself is the invariant. Without it there is no memory of individual things — only a photo gallery or a home dashboard.
- **The household's possessions as the bounded scope** — the collection is anchored to the user's own home and household, including extensions of the home such as storage units and off-site boxes. It is not a business's trade stock, an organization's asset base, or a single-type collection. Without this anchor the product is generic inventory software.
- **The maintained whole** — the inventory is a standing, evolving picture of the household's possessions as a totality: built up deliberately, kept current as things are acquired, moved, and disposed of, and answerable as a whole — searchable and browsable, with counts and total value. Without this, item records are scattered notes rather than an inventory.

### What the Item Record Carries

The attribute set is the product's choice, but mature products converge on a recognizable bundle:

- **Identity**: a name and usually a photo — enough to recognize the thing.
- **Classification**: a category or type, often with tags.
- **Acquisition**: purchase price, purchase date, and sometimes where it was bought.
- **Identification**: make, model, and serial number for items that have them.
- **Value**: what it cost, and in some products an estimated current value.
- **Condition and history**: condition notes, dated notes about repairs or modifications.
- **Documentation**: attached receipts, warranties, owner's manuals, and other files.
- **Where it lives**: its location (see below).

No single attribute is definitional — a quick-entry style in some products creates an item from just a photo and a name, to be enriched later — but the record exists so that the household can later prove what the thing was, what it was worth, and that it belonged to them.

### The Location Layer

Mature products commonly organize the collection by place: rooms, shelves, containers, boxes, storage units, often nested (a box inside a closet inside a room). "Where it lives" becomes a first-class attribute, and locations frequently become the primary way of browsing the inventory. Some products extend the location itself into a small record — its own photos, notes, and the total value of what it contains. Location organization is nonetheless a common mature structure, not part of the defining core: the paper-era inventory was often a flat list, and such a list is still a home inventory.

### The Home Record (adjacent extension)

Some products also keep information about the home itself — property details, assessment or value history, renovation and repair logs, maintenance schedules. This is an extension toward home management, useful to the same user, but not what the inventory consists of.

### One Structure, Many Implementations

```text
Concept:          Item of record
Implementations:  structured form with many fields; photo + name quick entry
                  enriched later; row in a spreadsheet (the thin incumbent)

Concept:          Household scope
Implementations:  one inventory per home; multiple inventories or collections
                  in one account; a binder per property

Concept:          Location layer
Implementations:  folders by location; nested location tree (room → shelf → box);
                  rooms as a property-detail structure

Concept:          Value
Implementations:  purchase price only; purchase price + estimated current value;
                  collection-level valuation

Concept:          Data posture
Implementations:  cloud account; device + personal-cloud sync; local file with
                  backups; self-hosted server
```

## How It Works

### Build the inventory

```text
Walk the home (room by room is the common guidance)
→ for each possession: capture a photo, give it a name
→ place it in a location (room / container)
→ add details: category, purchase price and date, serial number, value
→ attach the receipt, manual, or warranty document
→ repeat
```

Products invest heavily in making this fast, because the initial build is the largest effort in the whole workflow: photo-first quick entry that skips the full form, barcode scanning to pull product data, receipts forwarded from email into a holding area to be turned into items later, and CSV import from the spreadsheet the household already started.

### Keep it current

```text
Acquire something → add the item (often from the receipt or the box label)
Move something → update its location
Sell, give away, or discard → remove or mark the item
Insure something new → check it against the policy, if the product supports policies
```

The inventory's usefulness depends on this loop: a record that was never maintained answers questions badly exactly when they matter most.

### Use the record

```text
Search or browse (by location, category, tag) → find a thing or check what is in a box
→ generate a report or export (inventory list with photos and values,
  warranty expirations, moving checklist, per-heir list)
→ hand it to whoever needs it: the insurer after a loss, the agent at renewal,
  the movers, the lawyer, the family
```

The report is the point where the record leaves the application. In the insurance-oriented products this is the center of gravity: the inventory exists so that, after a loss, the household can produce a complete, evidenced list of what was destroyed or stolen instead of reconstructing it from memory.

### Share it

```text
Invite household members → they can view and update the same inventory
→ the record stays current from whoever notices the change
```

Sharing scope is deliberately limited: the default posture is household-private, with explicit invitations. Some products also support exporting a copy (for an advisor, or for transfer when a home is sold).

### Capability tiers

**Defining core** — without these, not a home inventory:

- per-possession item records with descriptive/documentation attributes
- the household's own possessions as the bounded scope
- the inventory maintained as a standing, answerable whole

**Common mature structure** — present in most current products:

- location/room organization, often nested
- item photos
- purchase details (price, date, source)
- serial/model numbers
- receipts and document attachments
- per-item value and aggregate views (total value, counts)
- reports/exports (PDF/CSV)
- search/browse by location, category, tag
- sharing with household members
- QR/barcode support (scan to add; label generation in some products)
- warranty tracking

**Variant / optional** — depends on product philosophy and purpose:

- insurance-policy machinery: stored policies, coverage analysis, claims tracking
- estate/heir assignment
- maintenance schedules and histories
- moving support (checklists, location-change reports)
- collections management (collector-oriented usage)
- home-record extension (property details, assessment history, renovation logs)
- business/asset-tracking crossover
- deployment: cloud service, self-hosted, local file, device-plus-personal-cloud

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Item list / gallery

The primary browsing surface.

- lists items with photo thumbnails, names, locations, values
- filterable and sortable by location, category, tag, value, purchase date
- primary actions: open an item, add an item, search

### Item detail

The record for one possession.

- photos, attributes (category, purchase, serial, value, condition), attached documents, notes
- primary actions: edit details, add photos/receipts, change location, delete

### Locations view

The place-oriented map of the home.

- rooms, containers, and storage places, often as a nested tree
- per-location item lists and, in some products, aggregate value
- primary actions: add/edit locations, move items between locations, browse a location's contents

### Capture surfaces

The mobile-first entry paths that make building the inventory practical.

- quick add (photo + name), full form, barcode scan, receipt forwarding/import
- primary actions: capture, place in a location, enrich later

### Reports / exports

The surface where the record is produced for outside use.

- inventory lists with photos and values, coverage summaries, warranty expirations, moving checklists, per-heir lists
- primary actions: configure scope, generate, print/export/share

### Sharing / settings

- household-member invitations and access levels
- data posture: sync, backup, export, and (in self-hosted products) server administration

## Important Rules / Behaviors

### The record is evidence

The inventory is built to be believed by outsiders. Photos, receipts, serial numbers, and purchase records exist to prove ownership, condition, and value to an insurer, a police report, an estate settlement, or a dispute. This is why documentation attachment is so prevalent, and why the report/export surface is a structural part of the Type rather than an afterthought.

### Items live in places

The common model is containment: an item is placed inside a location, and moving an item is an update to that placement. Containment can have real semantics — in at least one documented implementation, deleting a location deletes the items stored within it, so items must be moved out first. Location changes are also tracked as events in some products (a record of what moved, useful during a move).

### Value aggregates upward

Per-item values roll up — by location, by category, by collection, and in total. The total value of the household's possessions is one of the inventory's most-consulted numbers, both for insurance adequacy and for the household's own sense of what it owns.

### Household-private by default

The record describes the inside of a home and is sensitive. The default posture is private to the household; wider visibility is always an explicit act (inviting a family member, exporting a report, sharing a binder). Products differ in where the data physically lives — vendor cloud, personal cloud, local file, self-hosted server — and this is a primary differentiator between products, not a detail.

### No stock semantics

Unlike business inventory, a home inventory has no reorder points, stock thresholds, or units-of-sale. Possessions are unique; the quantity concept, where it exists at all, serves households with multiples of ordinary items, not trade stock. When a product's center is stock management (reorder alerts, purchase orders), its home-inventory face is a crossover, not the Type's center.

### The inventory serves moments, not sessions

Nothing in a home inventory is urgent day to day. The product's value concentrates in rare, high-stakes moments — the claim after a loss, the move, the estate — which is why the defining behaviors are about completeness, maintenance, and producibility rather than about any daily interaction loop.

## Variants

- **Insurance-first deep catalog** — the possessions catalog wrapped in policy machinery: stored insurance policies, coverage analysis that flags under-insured categories or single items, claim-readiness. The historical heart of the category.
- **Visual lightweight organizer** — photo-and-folder organization of everything in the home, optimized for quick capture and finding things again; often extends to moving and to labeling boxes with QR codes.
- **Self-hosted / open-source** — the same core run on the household's own server, with privacy as the selling point and no cloud dependency.
- **Desktop file-based catalog** — the inventory as a local document with deep per-item detail, backups, and rich reporting; the older generation of the category, still functional.
- **Suite module** — the possessions catalog as one feature inside a home-management binder (documents, maintenance, appliances, pros, finance), often distributed through home-inspection or real-estate professionals.
- **Platform crossover** — a general inventory platform whose item/folder/report structures are marketed toward households alongside its business use; the home face reuses the same machinery.
- **Collector-oriented usage** — the same item record pointed at a single collection (coins, instruments, media), with collection-level valuation; a purpose variant rather than a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Home Management Application | the whole-home hub (documents, maintenance, projects, finance, pros) with the home's information as center; inventory appears as one module. Here the possessions catalog is the center. |
| Home Maintenance Application | recurring care of the home and its systems — task schedules and histories. Here the record is of possessions; maintenance machinery, where present, is an adjacent capability. |
| Home Improvement Planner | plans bounded improvement work on the home with a money plan; the inventory has no project scope and no plan-of-work machinery — it is the possessions record those products explicitly exclude. |
| Inventory Management System (business) | trade stock: quantities, SKUs, reorder thresholds, warehouses, many identical units. Here: unique possessions, no stock semantics. |
| Enterprise Asset Registry / IT Asset Management | an organization's assets with custody, assignment, and lifecycle. Here: a household's own things, owned rather than assigned. |
| Collection-catalog applications | a single type of collectible with collector metadata. Here: all household possessions; collections are one usage inside the whole. |
| Estate Planning Application | produces legal instruments (wills, trusts). The inventory's heir assignment only produces a report to attach to such instruments. |
| Professional contents documentation (restoration/claims tools) | the same item/room/photo/report structures, but the record belongs to the restoration or claims professional, covers only damaged property, and lives inside a claim — not the household's standing record. |
| Photo albums / notes apps | hold media or free-form notes without per-possession structured records; no aggregate whole, no evidence posture. |

The boundary with Home Management Application is the closest one, because mature products increasingly bundle both. The structural test is the center of gravity: if the possessions catalog is the product, it is a home inventory; if the possessions catalog is one tab beside maintenance, documents, and finance, it is home management.

## Representative Products

- **Sortly** — cloud inventory platform with a dedicated home-inventory face (organizing, moving, collections; folders, photos, QR labels, total-value reports)
- **Homebox** — open-source, self-hosted home inventory (items, nested locations, templates, QR codes, CSV/BOM export)
- **Binary Formations Home Inventory** — long-lived Mac desktop catalog with deep insurance-policy machinery, coverage analysis, estate/heir assignment, and maintenance scheduling (no longer sold; replaced by its successor)
- **Under My Roof** — the current-generation Apple-ecosystem successor: iCloud sync and family sharing, item details, home details, documents, renovations, maintenance, collections, policies and claims tracking
- **HomeBinder** — home-management binder distributed through home-inspection and real-estate professionals, carrying home inventory as one module

The definition was also checked against the professional mirror image (a restoration-industry contents-documentation platform) to fix the whose-record-is-it boundary, and against the thin realizations the market itself names as incumbents — the spreadsheet and the paper household inventory list — to keep the defining core free of era-specific machinery.

## Sources

Research date: **2026-09-08**

- Sortly — https://www.sortly.com/ and https://www.sortly.com/solutions/home-inventory-software/
- Homebox — https://homebox.software/en/ (docs root), https://homebox.software/en/quick-start/, https://homebox.software/en/user-guide/items/, https://homebox.software/en/user-guide/locations/
- Binary Formations Home Inventory — https://binaryformations.com/products/home-inventory/ and https://binaryformations.com/support/home-inventory-faq/
- Under My Roof — https://undermyroof.app/
- HomeBinder — https://www.homebinder.com/
- Encircle (professional boundary specimen) — https://www.getencircle.com/ and https://www.getencircle.com/solutions/contents/

> Sourcing limitation: one home-management suite with a well-known inventory module (HomeZada) could not be reached from the research environment (repeated 403 responses, across two research passes); the suite-module pole is evidenced by HomeBinder and the Under My Roof product instead. Two further candidate products could not be verified because their former domains now host unrelated businesses. Precise operational details (item-count limits, exact field sets, pricing tiers) are intentionally not asserted in this document; product-by-product observations are recorded in the paired Research Notes.
