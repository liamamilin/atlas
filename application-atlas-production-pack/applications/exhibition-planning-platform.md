# Exhibition Planning Platform

## Overview

An **Exhibition Planning Platform** is the curator- and registrar-side planning layer for exhibitions: it holds each display occasion as a planned record, manages the curated checklist of works selected for it, and advances the occasion through planning — refinement, approvals, and coordination of the lenders, venues, and participants it depends on — toward its execution window.

The defining structure is small:

```text
Exhibition record (the planned display occasion: name, venue(s), dates)
└── Curated checklist: the specific works/elements selected for the occasion,
    each entry linked to its object record
    └── Planning progression: refinement, approvals, coordination of
        participants — advancing the occasion toward realization
```

Everything else commonly associated with exhibition planning — checklist collaboration with access control, loan-status checks during selection, touring coordination, spatial design tools, publication of the show online — is a standard or optional capability layered around that spine, most of it shipped as sibling modules in the same systems.

One market reality should be stated plainly: in the researched sample, this planning structure is not sold as a standalone product. It lives as the exhibition layer inside museum collection systems and gallery management suites, and the single dedicated planning-adjacent product identified (a 3D spatial-planning tool) is an add-on bound to one vendor's suite. The document below describes the structure as it actually exists in those systems.

## Users & Context

The primary users are the staff who decide and prepare what will be shown:

- **Curator** — the author of the plan: conceives the exhibition, selects the works, builds and refines the checklist, and shares it with collaborators while controlling who can edit it.
- **Registrar / collections manager** — the keeper of record discipline: turns the selection into linked, standardized records, checks each candidate object's loan and display status, and tracks approvals and participants.
- **Exhibition / production manager** — owns the runway: the occasion's dates and venues, and the coordination that must complete before the installation window opens.

Secondary participants:

- **Designers and preparators** — consumers of the plan (checklists, object details, and, where supported, spatial layouts and floor plans); in the researched sample the design layer is often worked in separate design tools.
- **Partner institutions** — lenders and receiving venues whose participation the occasion coordinates; they appear as participants and counterparties, not as operators of the organizer's system.

The work context is the planning cycle of a display: an exhibition is conceived and its works selected well before anything is mounted or shipped, and the plan keeps evolving — objects added and removed, loans requested, venues confirmed, text and images written — until the occasion is handed off to installation and logistics. In commercial galleries the same planning rhythm is shorter and sales-adjacent: shows are planned, artworks attached, and the record prepared for publication.

## Core Model

### The defining core

```text
Exhibition record (the planned display occasion: name, venue(s), dates)
└── Curated checklist: the specific works/elements selected for the occasion,
    each entry linked to its object record
    └── Planning progression: refinement, approvals, coordination of
        participants — advancing the occasion toward realization
```

Three structures. If any one is removed, the software is no longer recognizable as exhibition planning:

- **The exhibition record as a planned display occasion.** An exhibition is held in the system as a named, dated, venue-scoped record — an in-house show, a traveling exhibition, a gallery show, a collection rotation — created while the show is still a plan and maintained through its realization. Institutions catalog all their exhibition types in the same record structure. Without the occasion, there are only object records and notes; the show itself does not exist in the system.
- **The curated checklist.** The list of specific works and elements selected to appear. It is drawn from the institution's own collection and from prospective loans, built and refined collaboratively during planning — objects added, dropped, and substituted as the concept firms up — and every entry stays linked to its object record rather than being a free-text line. Without the checklist, the software is an event calendar or a website page, not a planning tool.
- **The planning progression.** The occasion is worked toward realization: the checklist is refined, decisions are approved as the plan firms up, and the participants the show depends on — lenders, venues, partner institutions — are coordinated around its dates. Products describe this as managing planning stages; the stage vocabulary varies by product, but the progression from idea to approved plan to realized show is the workflow that makes the record a plan rather than a static entry.

### Standard capabilities around the core

Mature systems consistently add these capabilities. They make the core operational; they do not define the Type.

- **Collaboration with access control on the checklist.** Planning is a multi-role activity (curators, registrars, conservators, educators, designers), and the checklist is the shared working document. Systems let its owner create, edit, and share it while custom authorization settings govern who can see and change it.
- **Availability and loan-status checks at selection time.** The museum-incumbent implementations make this explicit: before proposing a work — and before filing a loan request for it — the planner can see whether the object has already been requested and what its current status is. The checklist's object linkage is what makes such checks possible; the object's state elsewhere in the system constrains the plan.
- **The loan and agreement layer as a sibling.** The agreements that bring borrowed works to the show (requests, approvals, terms) live in sibling modules or record types; the exhibition plan coordinates around them. Contracts relating to exhibitions, loans, and collection objects are managed beside the exhibition record.
- **Venues and touring coordination.** An occasion may involve several venues and lenders; the record tracks the participants and their engagements, and the touring case repeats the pattern across stops.
- **Object-record detail in the selection view.** While considering a work, the planner sees its full record: high-resolution images, condition reports, and its exhibition history — the information a selection decision actually rests on.
- **Exhibition history per object.** Linking objects to exhibitions builds each object's display history — a cumulative, permanent record of the occasions an object has appeared in.
- **Enrichment and documentation.** Text entries and media (curatorial statements, essays, installation views) are attached to the exhibition record; data-entry standards keep records consistent; dashboards and reports summarize the state of the institution's exhibitions.
- **Publication adjacency.** The exhibition record commonly doubles as the source for public surfaces — online collection portals, the institution's website exhibitions, virtual exhibitions. This is a downstream capability, not the planning itself.

### One structure, many implementations

The core is written conceptually. Different systems realize it differently:

```text
Concept:              Exhibition record (planned display occasion)
Implementations:     an exhibition module record with planning stages (museum
                     suites), an exhibition profile beside loan and location
                     profiles (small-institution tools), an exhibition record
                     with artworks and dates tied to the website (gallery suites)

Concept:              Curated checklist
Implementations:     curated object packages/lists linked to object records,
                     artworks added to the exhibition record, artwork lists
                     and documents generated for the show

Concept:              Planning progression
Implementations:     named planning stages with approvals tracking, coordination
                     of participants/venues/lenders from the exhibition record,
                     multi-user workflow on the exhibition profile
```

A reader who has only seen one implementation — say, a museum suite where planning is a set of stages inside an exhibition module — should still be able to recognize the same structure in a gallery suite where the exhibition is a record of artworks and dates feeding a website, or in a small-institution tool where it is an exhibition profile linked to loan records.

## How It Works

### Conceive and record the occasion

```text
Create the exhibition record
→ name it, choose its type (in-house show, traveling exhibition, gallery show, rotation)
→ set venue(s) and the date window
→ begin enriching the record: concept text, images, supporting media
```

The record exists from the first planning moment — before any object is confirmed, before any loan is requested — and remains the single container for everything that follows.

### Build and refine the checklist

```text
Search and browse the collection for candidate works
→ inspect each candidate's record (images, condition, exhibition history)
→ add the work to the exhibition checklist
→ for each entry, check its availability: outstanding loan requests, current status
→ share the checklist with collaborators; refine it as the concept evolves
→ track approvals as the selection firms up
```

The checklist is a living selection, not a snapshot: works are added, dropped, and substituted through the planning cycle, and each entry remains linked to its object record so the plan is always grounded in current object information.

### Coordinate what the show depends on

```text
Identify works coming from other institutions
→ check/request loan status; the agreement layer records terms (sibling modules)
→ confirm venues and participant institutions against the date window
→ keep the record current: participants, venues, documentation
```

Much of planning is coordination around the record: which works must arrive from where, under what agreements, and which venues and partners are engaged. The exhibition record carries this coordination; the agreements themselves live in the sibling loan/contract layer.

### Advance through planning to the handoff

```text
Checklist and participants converge
→ approvals complete; the plan is fixed for production
→ the occasion crosses into execution: installation takes over the venue
→ logistics moves the works to and from it
```

Planning ends where the other exhibition workflows begin. The handoff is the same occasion and the same checklist passing to the venue-side install state tracking and the movement chain — different workflows over one record.

### After realization

```text
The show opens, runs, and closes
→ the record completes: what was shown, where, when
→ each participating object's exhibition history gains an entry
→ the record feeds publication: online exhibits, website pages, virtual exhibitions
```

The finished exhibition record is the authoritative account of the display, and the object-linkage it built is the durable by-product: every object now carries the occasion in its permanent display history.

### Capability tiers

**Defining core** — without these, not exhibition planning:

- exhibition record as a planned, dated, venue-scoped display occasion
- curated checklist of works/elements linked to object records
- planning progression: refinement, approvals, coordination toward realization

**Standard capabilities** — present in most mature systems:

- checklist collaboration with access control
- availability/loan-status checks during selection
- sibling loan/contract agreement layer
- venues and touring coordination
- object-detail selection view; per-object exhibition history
- record enrichment, reporting, dashboards
- publication of the record to public surfaces

**Variant / optional** — depends on segment and product:

- spatial/design planning as software: 3D room models, artwork and lighting placement, environment testing, floor-plan export (documented in one sampled product as a suite-bound add-on)
- virtual-only exhibitions as a record type and output
- art-fair presentations as a sibling record type (commercial pole)
- sales overlays around shows: proposals, consignments, price context (commercial pole)
- budget and task machinery inside planning: plausible museum practice, not directly documented in the researched sample — treat as unverified

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Exhibition records list

The program-level entry surface: the institution's exhibitions over time.

- occasions with names, types, venues, dates, and current planning state
- primary actions: create an exhibition, open one, review what is upcoming, in progress, or closed

### Exhibition record

The organizing surface for one occasion.

- occasion identity, type, venue(s), date window, planning state
- linked checklist, participants and lenders, text and media documentation
- primary actions: edit the occasion, manage the checklist, track participants and approvals, attach documentation

### Checklist editor

The working surface of the selection.

- each entry: the work, its object-record link, its availability/status
- primary actions: add/remove works, reorder and refine, share with controlled access, export the list for collaborators

### Object-record browser (selection view)

The surface the planner works from while choosing works.

- candidate objects with images, condition reports, and exhibition history
- primary actions: search/filter the collection, inspect a candidate, add it to the checklist

### Venues and participants view

The coordination surface for what the show depends on.

- venues, lenders, partner institutions against the date window
- primary actions: add participants, track their engagement, align dates

### Reports and dashboards

- exhibition status overviews, record completeness, history and activity reporting
- primary actions: run/export reports for management and partners

### Publication settings

- how the exhibition record surfaces publicly (online portal, website exhibitions, virtual exhibitions)
- primary actions: select what is published, publish/update

### Optional 3D room planner

Where supported, a spatial surface: place artworks, panels, and lighting in a model of the real rooms, test the environment, and export floor plans for every room and wall.

## Important Rules / Behaviors

### The checklist is linked, not detached

Checklist entries are references to object records, not free-text lines. This is what lets the plan answer questions ("is this work available?", "what condition is it in?") and what turns the finished record into per-object exhibition history. A checklist that loses its object links stops being a planning artifact.

### Selection consults the object's world

An object's state elsewhere in the system constrains the plan: an outstanding loan request, a prior reservation for another show, its condition, its recent display history. Planning surfaces this state at the moment of selection — the plan is made against the collection's reality, not an abstract wish list.

### Access control is part of the planning surface

The checklist is the show's central working document, edited by several roles and shared with stakeholders; systems treat who can see and change it as a first-class configuration, not an afterthought.

### Stage vocabularies vary; the progression does not

The named planning stages are product-specific. What is structural is that the occasion moves through a refinement-and-approval progression toward its dates — exact labels should be read as local vocabulary.

### Exhibition history is cumulative and permanent

Each realized occasion adds one entry to each participating object's display history. The history is not edited retroactively; it is the object's institutional memory of where it has been shown, and planning is the workflow that creates it.

### The record is the plan and the account

The same record that holds the evolving plan becomes the authoritative account of the realized display — and, in most systems, the source for its public presentation. Publishing is adjacent, but the record's continuity from plan to publication is why institutions maintain it in the collection system rather than in generic documents.

## Variants

- **Museum temporary exhibition** — the canonical form: a bounded occasion with its own checklist, loans, approvals, and venues, planned over a long runway.
- **Traveling / touring exhibition** — one occasion coordinated across multiple venues and lenders; the planning record carries the participants and the repetition across stops.
- **Permanent-gallery rotation** — the same spine applied to ongoing collection displays: occasions are rehangs of gallery spaces, with lighter coordination and no external lenders.
- **Commercial gallery show** — the gallery pole: shorter cycles, artworks attached from inventory, sales context (proposals, consignments) around the show, and the record prepared for the website's exhibitions page.
- **Art-fair presentation** — a days-long occasion in the commercial pole, recorded as its own record type beside exhibitions in gallery suites.
- **Virtual-only exhibition** — an occasion realized purely online; the record and checklist are the same, the venue is the web.
- **Spatial-design planning layer** — where supported, 3D planning of rooms, placement, and lighting is added on top of the record and checklist; in the researched sample this exists as a suite-bound specialist product rather than a generic expectation.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Exhibition Installation Management | downstream sibling | the venue-side execution layer: per-work install/deinstall state once the space is taken over; planning delivers the occasion and checklist to it |
| Artwork Exhibition Logistics | downstream sibling | the movement chain of works to, between, and from venues with custody continuity; planning decides what moves, logistics executes the moving |
| Museum Loan Management | agreement-layer sibling | requests, approvals, terms, and returns for borrowed works; planning consults loan status during selection but does not constitute the agreements |
| Museum Collections Management | substrate | the object-record system the checklist draws from and reports into; remove exhibitions and collection management continues unchanged |
| Museum Object Movement Management | adjacent sibling | internal location tracking for any reason; planning organizes *future* display intent, not current-location control |
| Convention / Exhibition Management | namesake only | the event-industry "exhibition" is a trade show — exhibitors, booth inventory, registration; no collection objects are selected or displayed |
| Digital Collection Portal | downstream adjacency | publishes collection and exhibition content to the public; the exhibition record feeds it, but publishing is not planning |
| Event Management Platform | different object world | events center on attendees, registration, and programs; exhibition planning centers on a curated set of objects and the lenders/venues around them |

The load-bearing boundaries are the two downstream siblings, because real systems ship all three as workflows of one exhibition module: they share the occasion and the checklist, and differ in which state layer they own. Planning owns the progression toward realization (selection, approval, coordination); installation owns the in/out state at the venue; logistics owns the movement chain between locations. Remove the planning progression and installation and logistics still function; remove the occasion and checklist and none of the three exists.

## Representative Products

The researched market expresses this Type inside museum collection systems and gallery suites rather than as a standalone product; the following are the systems in which the planning structure was verified:

- **TMS Collections (Gallery Systems)** — museum incumbent; Exhibitions module with planning stages, object packages as checklists, approvals and venues tracking, and per-object exhibition histories
- **MuseumPlus (Zetcom)** — European museum incumbent; Exhibition Management coordinating participants, venues, and lenders, beside a contracts module covering exhibition and loan agreements
- **Curator (Zetcom)** — dedicated 3D exhibition planning and design add-on (spatial placement, lighting, floor-plan export) bound to the MuseumPlus suite
- **Argus (Lucidea)** — small/mid-museum pole; curation and exhibit capabilities at object level with multimedia exhibit building
- **CatalogIt** — smallest-institution pole; exhibition documentation beside loan and location profiles, with multi-user workflow
- **Artlogic** — commercial gallery suite; exhibition records with artworks and dates feeding the website, with artwork lists and documents for exhibitions and loans

No standalone dedicated exhibition-planning platform was identified in the researched sample; the planning workflow ships as the exhibition layer of these systems.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces:

- Gallery Systems — The Essential Guide to Managing Exhibitions in TMS Collections — https://www.gallerysystems.com/resources/the-essential-guide-to-managing-exhibitions-in-tms-collections/
- Gallery Systems — Software for Curators — https://www.gallerysystems.com/roles/software-for-curators/
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/
- Zetcom — Curator — https://www.zetcom.com/en/curator/
- Lucidea — Argus — https://lucidea.com/argus/
- CatalogIt — https://www.catalogit.app/
- Artlogic — Gallery Management — https://www.artlogic.net/products/gallery/management
- Artlogic Support — help-center search results for "exhibition" — https://support.artlogic.net/hc/en-gb/search?query=exhibition

Prior in-repo passes used for boundary context (same production line): research/exhibition-installation-management.md, research/artwork-exhibition-logistics.md, applications/convention-exhibition-management.md.

> Sourcing limitation: detailed help-center documentation for the museum incumbents is login-gated (Gallery Systems community; Zetcom help center), so museum-pole evidence is guide-outline, role-page, and product-page level rather than screen-level. A direct Artlogic help article was unreachable (404); its evidence rests on help-center search snippets. Budget and task machinery inside planning modules could not be verified in any reachable source and are intentionally not asserted. The finding that no standalone planning product exists is bounded to the reachable sample. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
