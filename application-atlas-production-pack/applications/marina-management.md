# Marina Management

## Overview

A **Marina Management** application is the marina operator's berthing system of record: it holds the facility's mooring spaces as managed inventory, records the agreements under which specific vessels occupy those spaces, tracks which berths are occupied right now, and turns berthing into money through recurring rent, transient fees, and usage charges.

The defining core is small:

```text
Berth / space inventory of record
└── Berthing agreement (long-term lease or transient stay)
    │    binding vessel × customer × space × term
└── Occupancy state of the spaces
     (the daily dock board, under size-fit constraints)
└── Berthing-to-money loop
     (recurring rent + transient fees + usage charges → invoices/payments)
```

Everything else commonly associated with these products — interactive dock maps, metered shore power, fuel docks, service-yard work orders, online booking, customer portals, renewal automation, dynamic pricing — is standard or optional machinery that mature products add on top, not what makes the Type what it is. The definition also covers older and differently shaped implementations: a paper-era marina office with a wall dock plan, lease files, a rent ledger, and a transient log book satisfies the same core, as does a desktop-era marina system with no cloud or online layer.

## Users & Context

The primary user is the marina operator — the business (or municipal harbour authority) that runs a waterside facility where recreational vessels moor.

Typical roles and their relationship to the system:

- **Marina manager / dockmaster** — owns the dock board: assigns vessels to slips, handles arrivals and departures, balances long-term tenants against transient demand.
- **Dock staff / handlers** — work the occupancy view dockside: check vessels in and out, move boats between slips, capture meter readings and photos.
- **Office / bookkeeping staff** — run the money loop: recurring rent billing, transient invoices, utility and fuel charges, deposits, renewals, delinquency.
- **Service yard staff** (at full-service operations) — work orders for maintenance, haul-out, storage, and launch scheduling.

The work context is a facility that runs on two clocks at once: the annual cycle (seasonal/annual contracts, renewals, recurring rent) and the daily cycle (who is arriving, who is leaving, which slips are free). The berthed population is dominantly long-term tenants; transient boaters are the variable, higher-churn layer on top.

## Core Model

### The Defining Core

**1. The berth/space inventory of record.** The facility's mooring spaces — wet slips, moorings, dry-stack racks, and commonly yard storage spaces — exist as individually identified records with their location on the docks and their capacity attributes (dimensions a vessel must fit, available power/water). This inventory is the facility's truth: every commitment and every charge refers back to a space in it. Without it there is nothing to fill, assign, or bill.

**2. The berthing agreement as the unit of work.** A persistent commitment binding a specific **vessel** (owned by a specific **customer**) to a specific **space** for a defined **term**. Two canonical shapes:

- the **long-term contract** — seasonal or annual lease of a slip or storage space, the marina's stable tenant base; and
- the **transient stay** — a short-term dockage booking, made as a reservation in advance or as a walk-in.

The agreement is the hub: occupancy, charges, deposits, documents (insurance), and services all attach to it. Without it, the system is an anonymous dock log.

**3. Occupancy state of the spaces.** At any moment each space is occupied, vacant, or reserved. This state layer is what dock staff actually operate from — the daily board of who is on the docks, what is opening up, and what fits where. Assignment is constrained by fit: a vessel's dimensions must match the space's capacity. Without it, the system is a lease ledger with no live operations.

**4. The berthing-to-money loop.** Berthing resolves into money on the customer's account:

- recurring rent on contracts, generated on billing cycles from rate configuration, with renewals continuing or ending the agreement;
- fees for transient stays, charged on arrival or departure;
- usage charges — metered utilities (electricity read from shore-power meters, sometimes water or phone lines), fuel dock sales, and store or service purchases — accumulated on the same account;
- all of it resolving into invoices and payments, with deposits held and released against the agreement.

Without this loop the roster is free and the business is gone.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Interactive marina map** — a visual layout of the docks where each slip shows its live state; the signature surface of the Type, present across the researched sample.
- **Vessel records** — the boat as a first-class record: dimensions (length overall and related measures), registration, insurance and other documents, tied to the owner's customer profile.
- **Customer/boater profiles** — contact and billing details, balances, stored payment methods, communication history.
- **Utility metering** — shore-power meter readings captured dockside or imported, converted into usage-based charges on the tenant's account.
- **Fuel dock and point of sale** — fuel sales and retail purchases recorded against the customer account or taken at the dock.
- **Service work orders** — maintenance jobs with parts, labor, and technician assignment for operations that run a service yard.
- **Dry-stack and launch scheduling** — managing racked storage and the launch/retrieve queue that moves boats between rack and water.
- **Online booking and customer portal** — boaters reserve transient slips and pay bills themselves; staff get mobile dockside tools.
- **Renewal machinery** — contract renewals with automated communications, so the annual tenant base rolls over without spreadsheets.
- **Reporting** — occupancy, slip utilization, rent rolls with revenue recognition, accounts receivable, vessel and insurance listings.
- **Accounting** — either a built-in accounting suite or integrations with external bookkeeping systems.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Berth/space inventory
Realizations:  wet slips, mooring balls, dry-stack racks, yard storage spaces,
               linear dockage measured in feet rather than discrete slips

Concept:  Berthing agreement
Realizations:  annual/seasonal lease contracts, multi-month bookings,
               transient reservations, walk-in dockage

Concept:  Occupancy board
Realizations:  interactive dock map with drag-and-drop, list/grid occupancy views,
               reservation calendar

Concept:  Usage charges
Realizations:  imported meter readings, dockside mobile meter capture,
               fuel-flow integration, POS postings
```

A reader who has only seen one implementation — say, a cloud product with an online booking portal — should still be able to recognize a desktop-era marina system or a club marina module as the same Type.

## How It Works

### Set up the harbor

The operator builds the facility in the system: docks, slips, and storage spaces as identified records with dimensions, utilities, and location. This inventory is the foundation everything else refers to.

### Fill the slips with contracts

```text
Prospect or existing tenant
→ vessel and customer records created or updated
→ space matched by fit (vessel dimensions vs space capacity)
→ contract created for a season or year at a configured rate
→ recurring rent billed on cycles; payments collected
→ at term end: renewal (new cycle) or vacancy (space returns to inventory)
```

The long-term contract is the marina's backbone. Recurring billing runs largely on its own; the operator's attention goes to renewals, delinquency, and the spaces that come free.

### Handle transient traffic

```text
Boater requests dockage (online, by phone, or walk-in)
→ reservation created against an available, fitting space
→ vessel arrives; staff check it in and settle it on the dock
→ stay charges accumulate (dockage, electricity, fuel, store)
→ departure; final invoice settled
→ space returns to vacant
```

Transient work is the daily rhythm: the dock board shows what is arriving and leaving today, and staff move vessels in and out without breaking the long-term tenants' assignments.

### Work the dock board

Staff read the map or occupancy view to see what is where, drag vessels between spaces when assignments change, and check availability before committing a new agreement. When demand exceeds supply, interested boaters can be held on a waiting list and offered spaces as they free up (common, though not universal, machinery).

### Capture usage and settle money

Meter readings flow into usage charges; fuel and store purchases post to the account; the billing engine turns contracts, stays, and usage into invoices; payments settle against the account; deposits are held while a vessel occupies a space and released when it departs in good order. Reporting closes the loop: occupancy, rent roll, receivables.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Marina map / dock board

The operator's primary surface.

- a visual layout of docks and spaces with live occupancy state
- typical information: space identity, current vessel, dimensions, utilities, arrival/departure dates
- primary actions: assign or move a vessel, check availability, open a space or agreement detail

### Reservation and agreement screens

Where commitments are made and maintained.

- typical information: vessel, customer, space, term, rate, deposit, documents
- primary actions: create a contract or transient reservation, modify term or space, renew, cancel, record deposit

### Customer and vessel records

- typical information: owner contact and balance; vessel dimensions, registration, insurance documents
- primary actions: edit records, attach documents, view berthing and payment history

### Billing and accounts

- typical information: open invoices, recurring charge schedules, meter-based charges, deposits held
- primary actions: generate billing runs, post charges and payments, handle refunds and deposit releases

### Service work orders (where the operation runs a yard)

- typical information: vessel, requested work, parts, labor hours, technician, status
- primary actions: create and assign work orders, track progress, post charges to the customer account

### Customer portal / online booking (where offered)

- boater-facing: reserve transient dockage, view and pay bills, upload documents

### Reports

- occupancy and slip utilization, rent roll and revenue, receivables aging, vessel and insurance listings

## Important Rules / Behaviors

- **Fit constrains assignment.** A vessel can only occupy a space its dimensions fit; the system's inventory attributes exist to enforce this before a commitment is made.
- **One commitment per space at a time.** The inventory truth prevents double-booking; a space under contract or reservation is not freely available. (Linear dockage is a recognized exception shape, where a long dock is filled proportionally rather than by discrete slips.)
- **Occupancy drives money.** Recurring rent follows the contract calendar; transient and usage charges follow the stay. A change in occupancy (arrival, departure, space move) is also a billing event.
- **The agreement outlives the visit.** Long-term contracts persist across seasons and renew year to year; the vessel and customer records persist across agreements, so history accumulates per boat and per owner.
- **Deposits and documents gate the agreement.** Security deposits are collected, held, and released against the agreement; insurance and registration documents are commonly required attachments (documented at sampled products; depth varies).
- **Usage must be read before it can be billed.** Metered utilities depend on readings being captured or imported; missed readings mean unbilled consumption — a known operational failure mode.

## Variants

- **Private recreational marina** — the standard shape: wet slips plus dry storage, long-term tenants with a transient layer, fuel dock and store.
- **Full-service marina / boatyard** — adds a deep service operation: work orders, haul-out, winter storage, launch scheduling.
- **Yacht club / club marina** — the berthed population is the club's members; permanent slips are held by members and transient dockage serves visiting members; billing flows into the club's member accounting.
- **Dry-stack-dominant operation** — racked storage with a launch queue as the core business, wet slips secondary.
- **Municipal / harbour-authority operation** — public harbours and moorings run by a public body; same core objects under public-stewardship rules (not directly observed in this research; recorded as a known market shape).
- **Multi-location enterprise** — marina groups running many properties on one platform with standardized workflows and consolidated reporting.
- **Marine dealership or rental-fleet operation** — the same vendor category often also sells boats or rents a fleet; those are neighboring businesses, not the marina core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Campground / RV Park Management | closest structural sibling | same shape over land: site inventory + reservations + stay lifecycle + billing; the marina's defining difference is the vessel as berthed subject and marine context (size-fit by vessel dimensions, wet/dry berthing, shore power, fuel dock, yard); products straddle, and some campground products bundle marina slips as adjacent inventory |
| Hotel Property Management System | shape-relative | binds guests to rooms for short stays with folios; a marina binds vessels to berths, dominantly on long-term contracts, with vessel/yard/fuel semantics; some hospitality PMS platforms can be reconfigured to run marinas, which shows the shape is portable but the marine objects are what define this Type |
| Boat / Yacht Charter Platform | demand-side neighbor | a charter platform sells time-use of vessels to the public; marina management runs the berths for the operator; marinas host charter bases but the systems do not merge |
| Self-storage Management | partial overlap | dry-stack racks resemble storage units and some vendors span both industries; the marina core is wet berthing plus vessel and marine services — a dry-stack-only operation is a marina variant, not self-storage |
| Port Terminal Operating System | different world | commercial cargo terminals (container moves, gate and crane operations) vs recreational berthing; different users, objects, and economics |
| Marine Fleet Management / Vessel Operations | other side of the dock | manages a vessel owner's fleet; marina management manages the facility operator's spaces and berthing business |
| Transient-dockage booking marketplaces | consumer-side neighbor | boater-facing listing/booking venues for transient slips; marina management is the operator-side system of record |

The campground boundary is the most important one: the two Types share the rentable-space operations skeleton, and software products genuinely straddle it. The test is the berthed subject — vessels with marine service context make it a marina; camping units with site semantics make it a campground.

## Representative Products

- **DockMaster** — long-established marine ERP for marinas, boatyards, and dealerships; visual marina map, dry-stack launch module, waitlists, deposits, metered utility billing, built-in accounting.
- **Storable Molo (Storable Marine)** — modern cloud-native marina platform; interactive harbor maps, seasonal/annual/transient contracts, online booking and customer portal, meter readings on mobile, multi-location support.
- **Jonas Club Marina Management** — marina module within a private-club management suite; member permanent slips plus transient reservations for members, graphical wet/dry storage display, billing into club accounting.

The definition was checked against older and differently positioned implementations (paper-era marina offices, desktop-era systems, hospitality PMS reconfigurations, club modules) to avoid over-fitting to the current cloud pattern.

## Sources

Research date: **2026-09-09**

- DockMaster — https://www.dockmaster.com/ and https://www.dockmaster.com/solutions/marina-management
- Storable Marine (Molo) — https://www.storablemarine.com/ , https://www.storablemarine.com/marina-management-software/ , https://www.storablemarine.com/services/slips-mooring-storage/
- Jonas Club — https://www.jonasclub.com/marina-management/
- RMS Cloud — https://www.rmscloud.com/ (boundary evidence only)

> Sourcing limitation: several marina software vendors' sites (including a prominent transient-reservation product and a UK harbour-management product) could not be fetched from the research environment on 2026-09-09. The researched sample therefore covers three products across three market positions. Precise operational details that were not directly evidenced (exact lifecycle state names, waitlist breadth across the market, deposit rules across the market) are intentionally not stated as general facts in this document; such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
