# Museum Object Movement Management

## Overview

A **Museum Object Movement Management** system is the staff-facing structure that keeps a museum able to answer, at any moment, one question: *where is every object in our care right now?*

It does this with two structures held together:

- a **current location** for every object, recorded against a defined system of named display and storage locations, and
- a **movement record** for every physical relocation — an attributed event that is what actually updates the current location and accumulates into the object's location history.

The domain's own standard (Spectrum, maintained by Collections Trust) calls this procedure *Location and movement control* and describes its purpose bluntly: keeping location records up to date "is the key to being accountable for collections in your care." Unlike commercial inventory, the point is not throughput or stock accuracy for its own sake — it is demonstrable custody accountability for unique, often irreplaceable objects held in public trust, whether they are in a storeroom downstairs, in a gallery, at an external conservator, or in transit.

The boundary of this Type follows from that purpose. It is not the system that documents *what* the objects are (cataloguing), not the legal agreement that authorizes an object's absence (loan management), not the discipline that assesses *what state* an object is in (condition reporting), not the management of treatment work (conservation), and not movement organized around a specific exhibition occasion (the exhibition workflow siblings). It is the everyday machinery underneath all of those: wherever an object needs to move, for whatever reason, this is the structure that records it and keeps the location picture true.

## Users & Context

The work happens mostly behind the scenes, in storerooms, galleries, and loading areas, and it involves nearly everyone who touches the collection:

**Primary users:**

- **registrar / collections manager** — traditionally owns the location records: defines and maintains the location system, authorizes moves, records or reviews movement records, and answers the "where is it?" and "what's in that store?" questions for the institution
- **preparators, art handlers, technicians, and collections staff** — physically move objects and update the records (or file movement paperwork that updates them)
- **curators and conservators** — request and prompt moves (for display, research, treatment) and consume the location picture when planning work

**Secondary users:**

- **volunteers and inventory staff** — carry out location verification and update records during inventory projects, common in small and mid-sized institutions
- **security and facilities staff** — the location picture feeds their responsibilities (what is in which room, when objects are moving, when spaces are open)
- **shippers and couriers** — external participants in off-site moves, coordinated through the movement record's shipping details

Typical occasions that trigger the machinery: routine storage reshuffles, gallery rotations and installations, loan dispatches and returns, transfers to and from conservation, photography or survey work, object entry and exit, and scheduled inventory audits.

## Core Model

The defining structure is small, and everything else in this Type elaborates it:

```text
The Identified Object (object number)
└── The Location System (named display & storage locations)
    └── Current Location (per object — "where is it now?")
        └── updated by → The Movement Record (attributed move transaction)
            └── accumulated as → Location History
```

### The identified object

Every location claim attaches to an identified object — the object number. The number is the link between the physical thing, its documentation record, and its location data; a location without an object number is meaningless in this world. The object record itself (description, provenance, images) belongs to the museum's collection system; this Type presupposes that record and adds the custody picture to it.

### The location system

The institution defines a set of **locations** — every place where an object can be displayed or stored — and gives each one a unique name or number. Locations are commonly organized as a hierarchy (building → room → cabinet → shelf), and each location carries its own record: type of space, address if off-site, environmental conditions, security and access notes. The location system is itself maintained: new stores and galleries are added, old ones closed. Locations are not just coordinates — the system records which locations are *suitable* for which kinds of objects (a watercolour does not go under direct light; a humid store may be off-limits for iron), making the location system part of the museum's care apparatus, not just its geography.

### Current location

Each object holds exactly one **current location** — where it is right now — together with when it arrived there. Many institutions also track a **normal location** (where the object lives when it is not in use), so a temporary move has an expected destination to return to. The current location answers the object-to-place question; the same data answers the place-to-object question (what is in this store), and both directions are ordinary, everyday queries. One behavioral rule is near-universal in practice: an object's location should be recorded in *one* place of record in the documentation system — duplicating location data is how pictures drift out of truth.

### The movement record

A movement record is the transaction that changes the picture. It is not just "the location changed" — it is a discrete, attributed event. Its recurring content:

- the object (by number) and the move it underwent
- **from** location and **to** location
- the date (and time, where operations are tight)
- **who carried out the move** and, where policy requires, **who authorized it** — moves are attributed work, and "objects are not moved without authorisation" is the standard's own phrasing
- the **reason** for the move (coded: exhibition, loan, treatment, inventory, storage reorganization…)
- a signature or record of **who accepted custody** at the destination — movement is a custody handover, not just a displacement
- a note, and for temporary moves a **planned return** (when the object comes back to its normal location)
- for off-site moves: shipping details — who transported, whether a courier accompanied, transit requirements

### Location history

Previous locations are retained with their begin and end dates. The accumulated history serves two purposes: it lets the institution reconstruct any object's whereabouts over time, and it lets the institution answer a retrospective question that security incidents and conservation queries routinely demand — *what else was in this location, on that date?* Location history is custody evidence as much as convenience.

### Off-site custody is still a location

The location picture does not end at the museum door. An object on loan to another venue, with an external conservator, or in transit is still in the institution's care and still holds a location state — "at [venue]", "at [conservator's studio]", "in transit". The standard's scope statement makes this explicit: record when objects move in and out of the museum, *and* track them within it. The movement record's shipping fields (shipper, courier, transit notes) exist precisely to carry the picture across the gap between two custody points.

## How It Works

### 1. Build and maintain the location system

Before anything can be located, the institution defines its locations: every display space and storage unit, uniquely named or numbered, described (type, environment, security, access), and organized so that a location reference points to exactly one real-world place. As the estate changes, the system changes with it — new locations added, closed ones retired.

### 2. Record where everything is

Every object gets a current location — starting from the moment it enters the museum (even the temporary first location, "registrar's office, quarantine bay", is recorded). From then on the rule of practice is that the location of record stays current: when an object moves, the record is updated promptly, because a stale picture is functionally the same as no picture.

### 3. The move loop

A typical move runs through the same skeleton whether it crosses a corridor or a continent:

```text
A move is needed (usually prompted by another workflow —
  an exhibition, a loan, a treatment, an inventory decision)
→ obtain authorization per policy
  (movement reference, authoriser, authorisation date;
  in small organisations the mover may be the authoriser)
→ prepare: check the object is fit to move
  (condition check; read handling/packing/security
  recommendations from the object record; assess route
  and risks; arrange packing or treatment if needed)
→ move — internal relocation, or transport with
  shipper/courier, insurance, and accompanying
  documentation; confirm safe arrival
  (delivery receipt, arrival condition check)
→ record the movement: from/to, date, who moved,
  who authorised, reason, custody acceptance
→ the current location updates; the old location
  moves into history with its dates
```

The prepare step is where movement management interlocks with the neighboring disciplines: the object's record is consulted for hazards and handling recommendations, a condition check confirms fitness to travel, and — for higher-stakes transport — insurance is arranged and documentation (receipts, customs papers, unpacking instructions) accompanies the object.

### 4. Verify the picture

The picture is only as good as its last update, so institutions periodically **verify** it: walk the stores, confirm objects are where the records say, and update or chase the discrepancies. Products support this with location-scoped searches ("everything in Bay 4, Shelf 1"), checklists, and follow-up tracking for objects that cannot be found — recording where the object *should* be, where it has been (current and previous locations, loan and exhibition history), and the search effort itself. Verification is a distinct procedure from movement control in the domain standard: movement records relocations as they happen; inventory checks the picture against reality.

### 5. Serve the other workflows

Movement control in a museum is rarely an end in itself. The domain standard notes that object moves "usually happen during the course of following another" procedure — a loan is dispatched, an exhibition is installed, an object goes to treatment, an inventory relocates items. This machinery is what those workflows call when anything has to physically move: it supplies the authorization step, the custody handover, the location update, and the history entry, and hands back a picture that is still true after the workflow has done its work.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Object location view

Part of the object record. Shows the object's current location and location date, its normal location, and its location history (previous locations with dates, optionally notes).

- Typical information: object number, current location reference, dates, normal location, history entries
- Primary actions: view history, update current location, record a movement

### Location system browser

The management surface for locations themselves.

- Typical information: hierarchy of locations (building → room → unit → shelf), per-location details (type, environment, security, access), active/inactive status
- Primary actions: create/edit locations, retire locations, navigate the hierarchy

### Location contents and search

The place-to-object direction.

- Typical information: all objects currently in a given location; searchable by location name or number
- Primary actions: search by location, list contents, export lists (for inventories, security reviews, or relocations of whole stores)

### Movement record form and movement lists

The transaction surface.

- Typical information: object number, from/to, date, mover, authoriser, reason, custody acceptance, note, planned return, shipping details
- Primary actions: create a movement record, authorize, attach documents, review movement history

### Inventory / verification workspace

The audit surface (where the product provides one).

- Typical information: checklists of objects by location, verification status, discrepancies, unlocated objects with their last known locations
- Primary actions: verify locations in the field, flag and track unlocated objects, document search efforts, bulk-update records

### Reports and registers

Location contents reports, movement histories per object, and retrospective "what was here on date X" listings — the accountability outputs that security reviews, insurance matters, and conservation queries draw on.

## Important Rules / Behaviors

### One place of record for location

An object's location should be recorded in one authoritative place in the documentation system. Duplicate or informal location records (shelf-end lists, personal notes) are tolerated as temporary measures, but the master record is the single source of truth — this is the standard's own consistency rule, and it is what keeps the picture queryable in both directions.

### Moves are attributed — and authorized where policy requires

Every movement records who moved the object; named individuals are accountable for moving objects. Many institutions additionally require a named authorizing role before a move happens — the domain standard makes authorisation a policy question ("who authorised those moves if required") and notes that in smaller organisations the person moving an object may be the same as the person authorising the move. Whether formalised or combined, the attribution remains.

### Promptness is part of the definition

"Record every movement … and change the location record" is the standard's minimum requirement, and the procedure is to be followed *promptly* — the standard explicitly frames up-to-date location records as the key to custody accountability. Whether an object may be moved *temporarily* without updating records is a recognized policy question (e.g. brief in-room repositions), not a license: the institution must decide and document it.

### Location and movement data is security-sensitive

Where objects are, and when they move, is exactly what a thief or vandal wants to know. The standard requires museums to keep location and movement records "appropriately secure and confidential," and movement restrictions (e.g. not moving objects while visitors are present) are a policy concern. Location data is custodial information, not public information.

### Fitness to move is gated by the object's state

The move loop consults the object record and, where warranted, a condition check *before* moving: handling recommendations, packing requirements, hazards, environmental sensitivities. The location system mirrors this on the destination side — locations carry suitability knowledge (which spaces are wrong for which materials), and the standard requires museums to ensure objects are "not moved into unsuitable locations."

### Off-site is still in care

An object away from the building holds a location state like any other, and the standard requires insurance or indemnity to be in place before transporting objects — particularly borrowed ones. Arrival is confirmed (delivery receipt, and where appropriate an arrival condition check) before the movement record closes out the transit.

### The picture is retrospective

Because previous locations are retained with dates, the system can answer not only "where is it?" but "what was in this room on that date?" — a capability the standard ties to security and conservation needs. This retroactive accountability is a signature behavior distinguishing custody documentation from ordinary asset tracking.

## Variants

- **Paper-based practice** — the historical and still-viable baseline: a location register or catalogue record kept current by hand, with movement paperwork (the classic triplicate movement ticket: one copy left in the object's former position, one filed to update the master record, one attached to the object, destroyed on return). The domain standard explicitly supports paper-based realization.
- **Field-level tracking in small institutions** — the current location lives as a field on each object record with a location-history section beneath it; current location may be updated manually or derived from the history entries. No dedicated movement module; discipline is provided by procedure and inventory projects.
- **Movement records as first-class records** — larger systems model each move as its own record type, related to the object (and often to the loan, exhibition, or treatment that prompted it), enabling precise, policy-governed movement histories. In at least one open-source system this layer ships switched off by default and is enabled for institutions needing detailed location tracking.
- **Audit-trail machinery** — enterprise systems maintain a complete location history audit trail per object (including per-component), with record-level change auditing beside it.
- **Barcode / RFID-assisted movement** — semi-automatic capture of moves and shelf-level verification; the standard acknowledges these systems explicitly as movement-managed-by-tooling. Real-time tracking is current-era machinery layered on the same structure.
- **Registrar-centric vs all-staff movement** — organizations differ in whether only registrars/collections staff may move objects (with formal authorization) or whether trained staff across the institution move objects under policy, with the registrar's team auditing the records.

A variant remains a variant of this Type as long as the two defining structures — the maintained location picture and the attributed move transaction — are present. If location tracking disappears (objects documented but not located), the work has drifted into pure cataloguing territory; if custody accountability disappears (movements tracked for throughput, not accountability), it has drifted into generic asset or warehouse management.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | container | the collection system of record that owns the object register and the whole custody-lifecycle event layer; location/movement control is one procedure family inside it — this Type owns that family's internal machinery |
| Museum Loan Management | sibling workflow | the loan is the legal agreement authorizing and bounding an object's absence; movement records carry out and account for the physical relocation — separate record types in the same systems |
| Museum Condition Reporting | sibling discipline | movement prompts before/after condition checks; condition owns the physical-state assessment, movement owns the location picture — neither records the other's content |
| Museum Conservation Management | sibling discipline | objects move to and from conservation through movement control (including custody transfer to external conservators); conservation records the work performed, not the location |
| Exhibition Planning / Installation / Artwork Exhibition Logistics | occasion-bound siblings | those organize movement around a display occasion (venues, install state, transport chains, cross-party handovers); this Type is the general, reason-neutral machinery — remove the occasion and everyday movement management remains |
| Enterprise Asset Registry | structural neighbor | tracks what the organization owns and where, but for replaceable operating assets; unique irreplaceable objects, per-location environmental suitability, condition-gated moves, and retrospective custody evidence are the difference |
| Warehouse Management System | name-adjacent | a WMS optimizes throughput of stock in fulfillment operations; movement management maintains accountability of unique objects — the record is documentation of custody, not a picking instruction |
| Evidence Management System | structural cousin | chain-of-custody tracking of unique items with attributed transfers; same machinery shape, different object world (legal evidence vs collection objects) and different documentation interlocks |

The most consequential boundary is with the collections-management container: this Type is the machinery inside the container's custody-accountability leg. Strip the object register and nothing here has anything to locate; strip the location/movement machinery and the collection system becomes a documentation-only catalogue that cannot say where anything is.

## Representative Products

- **TMS Collections** (Gallery Systems) — enterprise incumbent; maintains a complete location history audit trail per object and component, and lists Location and movement control among its supported primary procedures
- **MuseumPlus** (Zetcom) — European incumbent; realizes the workflow within its collection-management and exhibition modules (including input/output protocols around object moves)
- **CatalogIt** (It Unlimited) — SMB cloud platform; location documentation on object records plus structured inventory projects with location verification and unlocated-object tracking
- **eHive** (Vernon Systems) — small-institution cloud CMS; current location as a core field on every object record, with location-history entries that can drive the current location
- **CollectiveAccess** (Whirl-i-Gig) — open-source, self-hosted; hierarchical storage-location records at the core, with movement records as an optional dedicated layer for detailed location tracking

The defining structure was checked against the domain standard (Spectrum 5.1's Location and movement control procedure) and against the paper-era realization (location registers and triplicate movement tickets), so the definition does not depend on any current software packaging.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1, "Location and movement control" (primary procedure): scope statement, the Spectrum standard (policy questions and minimum requirements), and suggested procedure, all fetched in full — https://collectionstrust.org.uk/spectrum/primary-procedures/location-and-movement-control-spectrum-5-0-primary-procedures/
- Collections Trust — software directory entry "TMS Collections and eMuseum" (location history audit trail, supported Spectrum procedures) — https://collectionstrust.org.uk/software/tms/
- Gallery Systems — TMS Collections product page (positioning, roles) — https://www.gallerysystems.com/solutions/collections-management/
- Zetcom — MuseumPlus product page (core functions, modules, product family) — https://www.zetcom.com/en/museumplus-en/
- CatalogIt — Help center: "Conducting an Inventory Project" (location verification, unlocated-object tracking) and product pages — https://catalogit.helpjuice.com/en_US/museum-practices/conducting-an-inventory-project , https://www.catalogit.app/
- eHive (Vernon Systems) — Help center: "Core fields for object records", "Current location field", "Location fields" — https://help.ehive.com/location-fields.htm
- CollectiveAccess — official manual: Primary Tables and Intrinsic Fields (ca_storage_locations, ca_objects Home location, ca_movements), Location in a Hierarchy Bundle — https://manual.collectiveaccess.org/

> Sourcing limitations: operational help for TMS Collections and MuseumPlus is login-gated, so their evidence is at directory-entry and product-page level respectively; no screen-level workflow claims are made for them. eHive's documentation is field-level; CollectiveAccess's is data-model level. In the reachable sample no standalone dedicated location/movement product exists — the structure ships inside museum collection systems and as a paper-satisfiable standard procedure — so statements about standalone packaging are deliberately not made. Precise product-specific limits and mechanisms (field sizes, default switches, ticket stationery details) are held in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the joint-review boundary resolutions with the sibling museum workflow Types are recorded in the paired Research Notes.
