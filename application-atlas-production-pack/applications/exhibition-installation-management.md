# Exhibition Installation Management

## Overview

An **Exhibition Installation Management** application is the venue-side execution layer of exhibitions: it tracks the mounting of a defined set of works and display elements into a venue space for a specific display occasion, and the mirror-image removal when the occasion ends.

The defining structure is small:

```text
Display occasion (the exhibition: venue space + date window,
                  install → open → close → deinstall)
└── Install scope: the checklist of works/elements gathered for the occasion
    └── Per-element installation state
        (awaiting install → installed in place → deinstalled/removed),
        recorded as entering and leaving the exhibition context
```

Everything else commonly associated with exhibition production — condition reporting, touring schedules, loan agreements, crate lists, online exhibit publishing — is standard capability layered around this core, much of it shipped as sibling modules in the same systems. Two boundaries matter. Upstream, curatorial concept, design and budget belong to exhibition planning; this Type begins when a venue space is taken over for mounting. Around the venue, the transport of works to and from the venue belongs to exhibition logistics; this Type covers what happens inside the venue between the arrival and the return.

One market reality should be stated plainly: in the researched sample, this structure is not sold as a standalone product. It lives as the exhibition layer inside museum collection systems and gallery management suites, while the physical mounting work itself (wall construction, rigging, placement, lighting) is coordinated outside the software with generic tools. The document below describes the structure as it actually exists in those systems.

## Users & Context

The primary users are the museum and gallery staff who are accountable for what is on display and what happens to it:

- **Registrar / collections manager** — owns the records: builds the checklist, records each work's entry into and exit from the exhibition, attaches condition documentation, answers "what is installed right now."
- **Exhibition / production manager** — owns the window: the install and deinstall schedule against the opening date, across one or more venues.
- **Curator** — selects the works and approves placement; the checklist reflects curatorial decisions, while the record-keeping reflects registration discipline.

Secondary participants:

- **Preparators / art handlers** — execute the mounting; in the researched systems they appear as consumers of printed checklists and condition documents rather than as users of a work-scheduling module.
- **Conservators** — produce the condition documentation attached at the handover moments.
- **Registrars at partner venues** — in touring exhibitions, each venue records its own leg of the same occasion.

The work context is the gallery floor during the install window: crates opening, works unwrapped, condition checked, walls painted, cases set, works placed, labels printed, lighting adjusted — and the same in reverse after close. The software's role is to keep the authoritative record of that transformation: which works are in the occasion, their state as they go in and come out, and the documentation produced at each handover.

## Core Model

### The defining core

```text
Display occasion (the exhibition: venue space + date window,
                  install → open → close → deinstall)
└── Install scope: the checklist of works/elements gathered for the occasion
    └── Per-element installation state
        (awaiting install → installed in place → deinstalled/removed),
        recorded as entering and leaving the exhibition context
```

Three structures. If any one is removed, the product is no longer recognizable as exhibition installation management:

- **A display occasion anchored to a venue space and a date window.** The exhibition is a bounded context — an in-house show, a touring stop, a gallery show — whose lifecycle runs from install through open and close to deinstall. Without the occasion, object statuses and condition records exist, but there is nothing being installed; the software is generic collection or movement tracking.
- **An install scope: the checklist of works and elements for the occasion.** The checklist says what will be mounted. It is drawn from the collection (or from loans arriving for the occasion) and is worked collaboratively — refined, approved, and eventually reconciled against what actually got installed. Without it there is no install to manage, only a calendar entry or a design idea.
- **Per-element installation state, recorded as entering and leaving the exhibition context.** Each work or element carries a display state against the occasion: awaiting install, installed in place, deinstalled or removed. The state change is recorded — works are documented as going into the exhibition and coming out of it — so the system can always answer: what is installed in this exhibition now, and when did each piece go in and come out. Without this state layer the software is planning (before) or logistics (around), not installation management.

### Standard capabilities around the core

Mature systems consistently add these capabilities. They make the core operational; they do not define the Type.

- **Condition documentation at the handover moments.** Condition statements or reports are attached as a work arrives for install, as it is placed, and as it is deinstalled — the moments when custody and handling change. Institutional practice treats this as inseparable from the install itself; some systems add readiness flags that mark records whose condition documentation is still outstanding.
- **Venues and touring.** An occasion may move through several venues; the record tracks the venues, their windows, and the participating lenders, with the install/deinstall cycle repeating at each stop.
- **Exhibition history per object.** Each object record accumulates the exhibitions it has appeared in — an authoritative display history that outlives any single occasion.
- **Linked movement records.** Shipments, crates and couriers are recorded against the occasion — the seam where this Type hands off to exhibition logistics. Where shipments are modeled, crate lists (contents, dimensions, packing) are a documented artifact.
- **The agreement layer as a sibling.** Loans and contracts (who lends what, on what terms, with what return obligations) usually trigger the install; they live in a sibling module or record type, not inside the install state itself.
- **Collaborative checklists with access control.** The checklist is worked by several roles at once; systems provide user access levels over the exhibition record and its lists.
- **Reporting and dashboards.** Status overviews over the checklist — what is installed, what is pending, what documentation is missing — and exportable reports for partner institutions.
- **Publication adjacency.** The exhibition record commonly doubles as the source for online exhibits and public portals — an adjacent capability that drifts toward collection-publishing products.

### One structure, many implementations

The core is written conceptually. Different systems realize it differently:

```text
Concept:            Display occasion
Implementations:   an exhibition module record (museum suites), an exhibition
                   profile linked to loans and shipments, an exhibition record
                   in a gallery suite, exhibit references on object history

Concept:            Install scope (checklist)
Implementations:   curated object packages/lists, works linked via loan
                   records, artwork lists attached to the exhibition record

Concept:            Per-element installation state
Implementations:   object status fields monitored through the exhibition
                   lifecycle, documented "input and output" protocols for
                   works entering/leaving the exhibition, per-object
                   exhibition history entries, condition checks recorded
                   at each handover
```

A reader who has only seen one implementation — say, a museum suite where installation is a set of object statuses inside an exhibition module — should still be able to recognize the same structure in a gallery suite where it is an exhibition record with an artwork list, or in a small-institution tool where it is an exhibition profile with linked loans.

## How It Works

### Build the occasion and its checklist

```text
Create the exhibition record
→ define venue space(s) and the date window (install start → open → close → deinstall)
→ assemble the checklist of works/elements (from the collection and incoming loans)
→ refine and approve the checklist with the stakeholders
→ attach requirements: condition notes, handling instructions, display details
```

The checklist is the working document for everything that follows. In the researched systems it is a curated list of records (a "package" of objects, or works linked through loan records), not a static text file — each entry stays connected to its object record.

### Receive and condition-check

```text
Works arrive at the venue (transport handled by the logistics layer)
→ each work is unpacked and inspected
→ condition is documented and attached to the record
→ the work is marked as received/ready for install
```

The arrival condition check is the handover point from logistics to installation. Documentation produced here protects both the venue and the lender, and it is the baseline against which the deinstall check will be compared.

### Install

```text
Prepare the space (walls, cases, lighting — coordinated outside the system)
→ place each work/element per the plan
→ record the work as installed (entering the exhibition context)
→ attach install-time condition notes and placement documentation
→ reconcile the checklist: everything planned is either installed or resolved
```

The record-level action is deliberate and small: each work's state changes from awaiting-install to installed, with the date and documentation attached. The physical work around that state change — building, rigging, hanging, positioning — is real and skilled, but in the researched sample it is coordinated with generic tools (spreadsheets, task lists, drawings) outside the software; the systems track the authoritative state, not the crew schedule.

### Open, period, deinstall

```text
Exhibition opens and runs
→ period checks and condition updates as needed
→ at close: deinstall begins, mirroring the install
→ each work is removed, condition-checked against the arrival baseline
→ the work is recorded as leaving the exhibition context
→ works return to their home locations or travel onward (logistics layer)
```

The deinstall is the install run in reverse, and it closes the occasion's record: every checklist entry ends in a documented exit. What remains afterward is the durable by-product — each object's exhibition history has grown by one entry.

### Touring

```text
Occasion closes at one venue
→ works travel to the next venue (new movement records)
→ install/deinstall cycle repeats at each stop
→ the occasion record accumulates venues, legs, and per-venue documentation
```

### Capability tiers

**Defining core** — without these, not installation management:

- display occasion with venue space and date window
- checklist of works/elements for the occasion
- per-element installation state recorded as entering and leaving the exhibition context

**Standard capabilities** — present in most mature systems:

- condition documentation at handover moments
- venues/touring tracking; per-object exhibition history
- linked movement records (shipments, crates, couriers)
- sibling agreement layer (loans/contracts)
- collaborative checklists with access control; reporting/dashboards
- publication of the record as online-exhibit content

**Variant / optional** — depends on segment and scale:

- readiness flags for outstanding documentation (implementation varies by product)
- formal condition-report protocols vs informal notes
- design/layout artifacts attached to the record (floor plans, mount drawings)
- time-based media / AV install specifics
- permanent-gallery rotation as an ongoing form of the same cycle
- deep physical-work coordination inside the system (not observed in the researched sample)

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Exhibition record

The organizing surface for one occasion.

- occasion identity, type, venue(s), date window, status
- linked checklists, loans, shipments, condition media, text and image documentation
- primary actions: create/edit the occasion, manage access, attach documentation, track statuses

### Checklist view

The working list of what will be (or is) installed.

- each entry: the work/element, its object-record link, its current state, its documentation status
- primary actions: add/remove works, refine the list, update per-entry status, flag missing documentation, export the list for the floor

### Object record (with exhibition history)

The substrate surface — where install state ultimately lives.

- the object's identity, images, location, condition media
- its exhibition history: the occasions it has appeared in, with dates
- primary actions: update location/state, attach condition reports, review display history

### Venue / schedule view

The touring surface for multi-venue occasions.

- venues, their windows, participating lenders/partners
- primary actions: add venues, track per-venue progress, coordinate documentation with partners

### Reports and dashboards

The oversight surface.

- checklist status overviews, documentation gaps, venue progress
- primary actions: run/export reports, share with partner institutions

### Mobile capture

The on-site surface during install and deinstall.

- condition and location updates from the gallery floor, photo capture
- primary actions: record condition, update location/state, attach images

## Important Rules / Behaviors

### The in/out duality is the record's spine

A work's participation in an exhibition is recorded as an entry into and an exit from the exhibition context — not as a single "is in the show" flag. This is what makes the record answerable over time: what was installed, when it went in, when it came out, and what condition it was in at each moment. Exact state vocabularies vary by product; the enter/leave structure does not.

### Condition documentation clusters at the handover moments

The moments when custody or handling changes — arrival, placement, deinstall, release — are where condition documentation is produced and attached. Institutional practice treats an undocumented handover as a liability gap; some systems surface this as explicit readiness flags on records that still need documentation.

### The checklist is reconciled, not just planned

The checklist begins as intent and ends as a record of what actually happened. Entries that were planned but not installed, or installed but not planned, are resolved explicitly — the finished occasion record is the authoritative account of the display.

### The physical work lives outside the system

In the researched sample, the software tracks the authoritative state (what is installed, its condition, its history) while the physical coordination — crew scheduling, wall construction, equipment installation — is handled with generic tools. Treating the software as a work-scheduling system for the install crew would misread what the researched products actually do.

### Exhibition history is cumulative and permanent

Each occasion adds to each object's display history. The history is not edited retroactively when an exhibition closes; it is the object's institutional memory of where it has been shown.

### Access follows role

Checklists and occasion records are worked by multiple roles (registrar, curator, conservator, external partners in touring contexts); systems provide user-level access control over who can see and change the record and its documentation.

## Variants

- **Museum temporary exhibition** — the canonical form: a bounded occasion in the museum's own or a partner's space, with loans, condition protocols, and a full install/deinstall cycle.
- **Permanent-gallery rotation** — the same cycle applied to ongoing collection displays: works enter and leave the displayed state as galleries are rehung; no external venues, lighter documentation.
- **Traveling exhibition** — one occasion, many venues: the install/deinstall cycle repeats at each stop, with movement legs and per-venue documentation between them.
- **Commercial gallery show** — shorter window, sales overlay, lighter condition formality; the checklist and in/out structure remain.
- **Art-fair booth** — a days-long occasion where the booth is the venue; works move in and out on a compressed cycle (documented in gallery suites as fair records with artwork lists).
- **Historic-house reinstall** — collection displays in period settings; the install state layer matters more than venue logistics.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Exhibition Planning Platform | upstream sibling | concept, curation, design, budget and the production plan before anything is mounted; installation begins at the venue-space takeover |
| Artwork Exhibition Logistics | around-the-venue sibling | the movement of works to, between, and from venues with custody continuity; installation is what happens inside the venue between the arrival and return legs; they meet at the condition-checked handover |
| Museum Collections Management | substrate | the object record system on which install states, condition media and exhibition histories hang; remove the occasion and collection management continues unchanged |
| Museum Object Movement Management | adjacent sibling | internal location tracking and movement control for any reason; installation is movement/state organized by a display occasion and ending in a display placement |
| Museum Condition Reporting | adjacent sibling | condition documentation as a standalone discipline at any moment; installation consumes it at handover points but is not constituted by it |
| Museum Loan Management | adjacent sibling | the legal/agreement layer (requests, approvals, terms, returns) that usually triggers the install; shipped as a sibling module in every researched system |
| Convention / Exhibition Management | different object world | the event-industry "exhibition" is a trade show — exhibitors, booths, services, attendees; its installation world is service execution around event infrastructure, not a collection-object lifecycle |
| Digital Collection Portal | downstream adjacency | publishes collection/exhibition content to the public; the exhibition record commonly feeds it, but publishing is not installation |

The load-bearing boundary is with Artwork Exhibition Logistics: the two Types share the occasion and the checklist and meet at the condition-checked handover, but logistics owns the movement chain between locations while installation owns the placement state inside the venue. Remove the movement chain and installation tracking remains; remove the install state and logistics remains.

## Representative Products

The researched market expresses this Type inside museum collection systems and gallery suites rather than as a standalone product; the following are the exhibition-management systems in which the structure was verified:

- **TMS Collections (Gallery Systems)** — museum incumbent; Exhibitions Module with object packages as checklists, planning stages, venues, object statuses, and per-object exhibition histories
- **MuseumPlus (Zetcom)** — European museum incumbent; Exhibition Management module coordinating participants, venues and lenders with documented input/output protocols for works
- **Argus (Lucidea)** — small/mid-museum pole; exhibits at object-history level with mobile on-site condition and location capture
- **CatalogIt** — smallest-institution pole; Exhibition profile linked to Loan, Shipment and Shipping Container profiles; also serves art installers and preparators as object-documentation users
- **Collector Systems** — cloud CMS pole; exhibition management as a standard tab with mobile location updates

No standalone dedicated exhibition-installation product was identified in the researched sample; the physical mounting work is coordinated with generic tools outside these systems.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces:

- Gallery Systems — The Essential Guide to Managing Exhibitions in TMS Collections (guide outline) — https://www.gallerysystems.com/resources/the-essential-guide-to-managing-exhibitions-in-tms-collections/
- Gallery Systems — Collections Management (TMS Collections) — https://www.gallerysystems.com/solutions/collections-management/
- Gallery Systems — site results for "exhibition" (EODEM, webinar listings) — https://www.gallerysystems.com/?s=exhibition
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/
- Lucidea — Argus — https://lucidea.com/argus/
- CatalogIt — product site and Help Center — https://www.catalogit.app/ , https://support.catalogit.app/
- CatalogIt — "Track Every Mile: Using CatalogIt for Traveling Exhibitions" — https://www.catalogit.app/post/track-every-mile-using-catalogit-for-traveling-exhibitions
- Collector Systems — https://www.collectorsystems.com/

Prior in-repo research used for boundary context (same production line, 2026-09-06): research/artwork-exhibition-logistics.md, research/art-gallery-management.md, research/artwork-consignment-management.md.

> Sourcing limitation: detailed help-center documentation for the museum incumbents is login-gated (Gallery Systems community) or was unreachable (Zetcom help center; Vernon Systems and Axiell sites returned errors and were abandoned per research rules). Evidence for those products is module-description level rather than screen-level. Precise operational details (exact status vocabularies, field lists, protocol formats) are therefore not stated in this document; such details remain in the Research Notes. The finding that no standalone installation-management product exists is bounded to the reachable sample.
