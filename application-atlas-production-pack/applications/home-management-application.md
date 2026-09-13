# Home Management Application

## Overview

A **Home Management Application** is the homeowner's application of record for a home: it keeps the information life of one's own home — property details, documents, appliances and equipment, possessions, maintenance, improvements, service pros, and sometimes the home's value — consolidated in one standing, home-anchored place, kept current as the home is lived in and worked on, and produced outward at the home's key moments: a recall or service call, an insurance claim, the sale or transfer of the house.

The defining structure is small:

```text
Home of record (the property as the anchored subject)
└── Consolidated whole-home binder
    (documents · appliances/equipment · possessions · property details · service pros)
    └── Operating life kept in the record
        (maintenance · improvements/projects · service history)
        └── Produced outward at key moments
            (service · claims · sale/transfer)
```

Everything else the market associates with the category — inventory modules, home-value estimates, marketplaces, rewards, insurance machinery, partner distribution, self-hosting — is widespread in current products but is not part of the defining core. The paper-era equivalent, the house book or home file (deed, manuals, warranties, receipts, paint codes, a maintenance calendar, handed to the next owner with the house), satisfies the same structure without any software.

When the center of gravity shifts to one bounded operation — the possessions catalog, the recurring upkeep plan, the project-and-money plan — or to the household's people and schedule, the product belongs to a neighboring Application Type (Home Inventory, Home Maintenance, Home Improvement Planner, Family Organizer).

## Users & Context

The primary user is a homeowner — the owner of a residential property (house, townhouse, condo, apartment) — who needs the home's scattered information in one place that survives years of ownership.

Typical reasons to open the application:

- look up an appliance's model number, manual, or warranty
- store or retrieve a home document (contract, receipt, agreement)
- see what maintenance is due and record that it was done
- track a renovation or improvement, with costs and photos
- find the pro who worked on the house, or a recommended one
- answer a recall notice or prepare an insurance claim
- prepare the home's record for a sale or hand it to the next owner

Secondary users are co-owners and family members, who share the record with graded access. The context spans the whole ownership life: the record is often established at purchase — some products arrive pre-loaded with the inspection report through the inspector, lender, or agent — and is maintained across move-in, upkeep, projects, and claims; in some products it is handed forward at sale. Multi-property owners keep one record per home.

## Core Model

### The Defining Core

Three structures held jointly. Remove any one and the product stops being a home management application:

- **The home of record** — a persistent, identified record of the user's own home: the property's identity, details, spaces, and structures (rooms, paint finishes, systems). Everything in the product hangs from this home; the record belongs to the house, not to a person's generic life or a family's schedule. Without it, the product is generic document storage or a personal organizer.
- **The consolidated whole-home binder** — the home's scattered information gathered and organized as one standing, browsable whole: documents (deed, contracts, manuals, receipts), appliance and equipment records (make/model, manuals, warranties, purchase details), possessions, property details, and the service pros who worked on the house. The consolidation across kinds of home information is what defines it; which modules a product carries varies. Without it, the product is a set of disconnected single-purpose tools.
- **The operating life kept in the record** — the record is maintained as the home is operated: maintenance schedules and reminders with their completions, improvements and projects tracked or logged, service history accumulating — and the standing record is produced outward at the home's key moments. Without it, the product is a static archive (a filed inspection report), not management.

### Standard Capabilities

Mature products commonly carry most of the following. They make the binder practical; they do not define the Type:

- **Appliance/equipment records** — make, model, serial, purchase details, manuals, warranties; recall alerts derived from the recorded models in some products.
- **Document storage** — the home's paper trail held digitally; sometimes pre-populated from the inspection report.
- **Maintenance reminders** — scheduled upkeep tasks with notifications and completion tracking.
- **Project/improvement tracking** — renovations and upgrades logged with costs, photos, receipts, and contractor information; some products also support planning or scoping future work.
- **Possessions/inventory module** — a catalog of household items, often framed for insurance purposes.
- **Property details** — rooms, structures, paints and finishes with color codes and manufacturers.
- **Service pro directory** — saved contacts for pros who worked on the house; some products add recommended pros or access to a wider professional network.
- **Home value / finance view** — a value estimate that can respond to recorded improvements and maintenance, editable by the owner, in some products.
- **Photos** tied to the property, its rooms, and its records.
- **Sharing** — co-owner or view-only access for family members.
- **Mobile and web surfaces.**

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Home of record
Realized as:  binder bound to the property (partner-provisioned) ·
              digital home profile (mobile app) ·
              home details inside a possessions app

Concept:   Consolidated binder
Realized as:  one tab per module (projects, maintenance, appliances, docs…) ·
              a unified home profile with logged actions ·
              sections inside a single app

Concept:   Operating life
Realized as:  reminder lists with completion ·
              action logging (sometimes rewarded) ·
              schedules plus repair/renovation histories

Concept:   Key moments
Realized as:  recall alert → service pro ·
              claim → inventory + documents ·
              sale → binder transfer or seller report
```

## How It Works

### Establish the home of record

```text
Accept or claim the home
→ the record is created for the property
→ pre-loaded from the inspection report (in products that arrive
   through a professional partner) or built manually
   (property details, rooms, structures)
```

There is no team, no workspace, no membership: the record is bound to one home (or one home per record in multi-property accounts).

### Build the binder

```text
Add appliances and equipment (make/model — in some products captured
from a photo of the equipment plate)
→ attach manuals, warranties, receipts
→ store the home's documents
→ catalog possessions (inventory module, where present)
→ record rooms, structures, paints and finishes
→ save the pros who worked on the house
```

### Keep it current

```text
Maintenance reminders arrive (text/email/in-app)
→ task completed → recorded against the home
→ improvements and projects logged with cost, photos, receipts
→ service history accumulates
→ (in some products) the home's value estimate updates from the recorded work
```

### Use it at key moments

```text
Recall notice → open the appliance record → check → contact a pro
Insurance claim → produce the inventory, photos, and documents
Selling the home → hand the record forward (where supported):
                    transfer to a family member, or a seller-facing copy to a buyer
```

### Core vs standard vs optional

**Defining core** — without these, not home management:

- home of record
- consolidated whole-home binder
- operating life kept in the record, produced outward at key moments

**Standard capabilities** — present in most mature products:

- appliance records (with recall alerts in some products), document storage, maintenance reminders, project tracking, possessions module, property details, pro directory, sharing, photos, mobile+web

**Optional / variant** — depends on product and business model:

- home value estimates, marketplaces and services shopping, rewards for home-care actions, sustainability/carbon tracking, insurance policy and claims machinery, collections, move-in concierge services, record transfer at sale / seller-facing reports, self-hosting, multi-property

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Home dashboard

The primary entry surface, organized as one section or tab per module.

- typical information: maintenance due, recent activity, the home's profile summary
- primary actions: open any module, add a record, see reminders

### Appliance/equipment records

Per-equipment records with identity and documentation.

- typical information: make, model, serial, purchase details, manuals, warranties, service history
- primary actions: add an appliance (in some products from a photo of the make/model plate), attach documents, check recalls

### Documents library

The home's paper trail held digitally.

- typical information: contracts, agreements, manuals, receipts, inspection reports
- primary actions: upload/scan, categorize, retrieve

### Maintenance list

The recurring-upkeep surface.

- typical information: scheduled tasks, cadence, due state, history
- primary actions: complete a task, edit the schedule, add tasks

### Projects / improvements

The change-work surface.

- typical information: project name, status, cost, photos, receipts, contractor
- primary actions: log a project, track progress, plan or scope future work (in some products)

### Property details

The home's physical record.

- typical information: rooms, structures, paints/finishes with color codes, systems
- primary actions: add rooms/structures, record finishes

### Home finance / value (where present)

The home's money view.

- typical information: value estimate, purchase price, adjustments from recorded work
- primary actions: view, edit the value, add the purchase price

### Sharing / transfer settings

The record's control surface (where supported).

- typical information: shared members and their access level, transfer options
- primary actions: share with view-only or full access, transfer the record, create a seller-facing report

## Important Rules / Behaviors

### The record is per-home and can outlive ownership

The binder is bound to the property, not the person. Some products support handing the record forward at sale — transferring it in full to a family member, or passing a seller-facing copy (a report of the home's records) to a buyer while the original owner retains control of their record. Where supported, this makes the record an asset that travels with the house rather than an account that dies with the ownership.

### Sharing is graded

Household sharing distinguishes view-only access from full (co-owner) access. The record is private to the household; products differ in vendor-access posture — one states the vendor cannot access the data at all, another states it never shares or sells it.

### The record consolidates but does not execute

Home management holds information and produces it outward; it does not itself run the transactions. Service pros are referenced, not booked; marketplaces, where present, are shopping surfaces; hiring happens in marketplace products. This is a structural difference from marketplace and contractor-management Types.

### Modules feed one record

The modules are distinct surfaces over one home record: completed maintenance and improvements can update the home's value estimate; appliance models power recall alerts; inventory and documents serve claims. The integration around the home — not any single module — is the product.

### Derived values are editable

Where a value estimate exists, it is a derived, owner-editable figure that responds to recorded work — not an authoritative valuation.

## Variants

Common realizations of the Type:

- **partner-distributed binder** — provided free through home inspectors, lenders, or agents, pre-loaded with the inspection report, transferable at sale (e.g. HomeBinder)
- **mobile-first care/rewards** — a digital home profile with action logging, family sharing, and rewards for home-care behavior (e.g. Dwellin)
- **inventory-core-expanding** — a possessions catalog adding whole-home records (home details, documents, renovations, maintenance, insurance) on desktop/mobile with cloud sync (e.g. Under My Roof)
- **suite-style home management** — inventory, maintenance, projects, documents, and finance sold as one subscription suite (a recognized market pole; its flagship could not be verified during research — see Sources)
- **self-hosted posture** — open-source, self-hosted household or home records for privacy-conscious users (adjacent products exist; the household-ERP pole belongs to chore/consumables territory)
- **multi-property** — one account holding a record per home

A variant remains a variant while the defining core holds. When the center of gravity shifts — to the possessions catalog, the upkeep plan, the project-and-money plan, the household's people, or device control — the product belongs to the neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Home Inventory Application | the possessions catalog is the center; here inventory is one module beside documents, appliances, maintenance, and finance |
| Home Maintenance Application | the recurring-upkeep plan is the center; here maintenance is one module of the whole-home binder |
| Home Improvement Planner | the project-and-money plan is the center; here projects are tracked/logged as part of the home's record, without a per-project money plan |
| Family Organizer | centers the household's *people* — shared calendar, meals, chores, budgets; home management centers the *premises* |
| Household Chore Application | household labor tasks and routines; home management's recurring machinery targets the home's fabric and equipment |
| Smart Home Platform | controls and automates the home's devices; home management keeps the home's information and operating record |
| Home Services Marketplace | the hiring transaction is the center; home management's pro list is a record-keeping directory that may link out to one |
| Property Management System | landlord-side operations over tenanted properties (leases, rent, tenants); home management is owner-side record-keeping of one's own home |
| Personal Organizer / Personal Dashboard | generic life organization with no property anchor; home management is anchored to a specific home of record |
| Document Management / Cloud Drive | generic document storage; home management is a home-scoped binder with home-native record types (appliances, property details, value, transfer) |

The closest boundaries are the three bounded siblings (inventory, maintenance, improvement planner) and the family organizer. The structural test in every case is the center of gravity: home management is premises-centered and operation-wide — the whole-home binder is the product, and each sibling's structures appear, at most, as one module.

## Representative Products

- HomeBinder
- Dwellin
- Under My Roof

The core model was checked against boundary specimens from adjacent poles (Homechart — family-hub, people-centered; Grocy — self-hosted household ERP, consumables/chores-centered) to confirm that "household" naming alone does not make a home management product.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- HomeBinder — https://www.homebinder.com/ , Homeowner Help Center: https://pages.homebinder.com/homeowner-help-center-0 (operational documentation)
- Dwellin — https://www.dwellin.com/ , https://dwellin.com/app/how-it-works/
- Under My Roof — https://undermyroof.app/
- Homechart (boundary specimen) — https://homechart.app/
- Grocy (boundary specimen) — https://grocy.info/

> Sourcing limitation: HomeZada — the suite-style product most prominently marketed as "home management software" — could not be fetched (site blocked on repeated attempts across research passes, including this one), and one further candidate (HomeKeepr) returned unusable responses. Assertions about the suite/finance-led pole are therefore calibrated down and no details of those products are stated. Precise operational details (numeric limits, default settings, exact field sets, pricing) are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical (paper-era house book) check are recorded in the paired Research Notes.
