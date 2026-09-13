# Artwork Exhibition Logistics

## Overview

An **Artwork Exhibition Logistics** application organizes the physical journey of artworks to, between, and from the occasions on which they are displayed: exhibitions, art fairs, and similar shows. It keeps a definitive answer to "where is this work right now and how did it get there," plans and coordinates each movement — packing, transport, receipt — and attaches the documentation that proves each handover happened in acceptable condition.

The defining core is small:

```text
Display occasion (exhibition / fair: venue(s) + dates)
└── Checklist of the specific works gathered for the occasion
    └── Per-work movement chain
        (origin → venue → return or onward to the next occasion)
        ├── Custody continuity: current location always known,
        │   every change recorded into movement history
        └── Handover documentation attached to each leg
            (condition at release / receipt, dispatch / receipt records)
```

Everything else the market associates with this work — transport booking, insurance, packing requirements, courier visibility, loan agreements, touring rotation — is a standard or optional capability layered onto that spine. When the display occasion disappears from the picture, the software is object movement tracking or art shipping; when the movement chain disappears, it is exhibition planning or installation management.

## Users & Context

The primary operators are the people professionally accountable for artworks in transit:

- **Registrars and collections managers** (museums and institutions): assemble exhibition checklists, arrange transport with art handlers and carriers, record condition at each handover, track works out to venues and back, and share logistics records with partner institutions. The registrar is the role the software's world is built around.
- **Gallery exhibition managers and registrars** (commercial galleries): move inventory between the gallery, art fair booths, viewing rooms, client placements, and returning storage, often on tight schedules between consecutive shows.
- **Artist and estate studio managers**: send works to exhibitions organized by others and keep track of where works are and when they are due back.

Counterparties appear at the edges of the system rather than as operators: partner museums and lenders (who run their own records of the same movements from their side), art handlers and specialized shippers (who receive schedules and requirements), couriers, insurers, and conservators (who produce condition documentation). The work environment alternates between an office desk — planning, scheduling, generating documents — and the accelerated rhythm around openings, closings, and install dates, when batch movements and last-minute condition checks dominate.

## Core Model

### Artwork records with custody continuity

The unit of tracking is always the **specific physical work** — one record per unique piece, never a quantity. Each work record carries:

- **Current location** — where the work physically is at this moment (gallery, storage, in transit, fair booth, partner venue). A work has exactly one current location at a time.
- **Movement history** — an ordered record of past locations and the changes between them, usually with dates and sometimes with who last examined the work. History accumulates; it is the work's itinerary.
- **Logistics-relevant attributes** — dimensions and weight (which drive packing and transport), condition documentation (reports, photographs), insurance values, and shipping/handling requirements.

This current-location-plus-history structure is the substrate on which everything else operates: an exhibition move is, mechanically, a set of controlled location changes with documentation.

### The display occasion

An **exhibition or fair record** is the bounded context that pulls works into a logistics effort: it names the occasion, carries venue(s) and dates, and holds the **checklist** — the list of specific works selected to appear. The checklist is the operational hinge between planning and logistics: it defines what must be ready, where each work is coming from, and what must come back.

### The movement chain

Each work's journey decomposes into **legs**: a release from its origin (with an outgoing condition check and dispatch record), the transport itself, and a receipt at the destination (with an incoming condition check). After the display period the chain closes with a return leg to the work's home location, or a forward leg if the work travels directly to the next occasion. The chain is the workflow backbone: scheduling, readiness, documentation, and location updates all attach to its legs.

### Handover documentation

Movements of unique, high-value, fragile objects are inseparable from their paperwork. The system carries — or links to — the documentation tied to each leg: condition reports taken before release and on arrival, dispatch and receipt confirmations, packing records, and the museum-side in/out protocols that document works entering and leaving an exhibition. This documentation exists to allocate responsibility: it establishes that a work left one party in one condition and arrived at the next in the same condition, forming an audit trail of due care.

### Parties

The model distinguishes: the **organizing operator** (registrar/exhibition manager running the system), the **venues and lenders** whose spaces and works are involved, the **transport providers** (art handlers, shippers, carriers) who execute legs, and the **insurer** who covers them. Partner institutions maintain their own view of the same movements from their side; logistics records are therefore routinely shared or exchanged across organizations.

### Standard capabilities around the core

Mature products commonly add, on top of the defining structure:

- transport coordination: shipment schedules, carrier details, delivery confirmations; or quote-and-book handoff to specialized shipping platforms
- readiness management: per-work shipping requirements, transport-ready states, and flags such as "condition report needed"
- standardized location records (to prevent name variants) and bulk location updates for batch moves
- generated documents: location reports, condition report templates, packing and requirement sheets
- insurance values on records and transit coverage for legs
- cross-party distribution: logistics reports to partner museums, lenders, and art handlers; shared condition and transit records
- packing and crating as a modeled step, whether self-packed or delegated to a specialized shipper

## How It Works

### Plan the occasion

```text
Create the exhibition/fair record (venue(s), dates)
→ build the checklist from works eligible to travel
→ for each work: confirm origin location, condition status, and shipping requirements
→ identify gaps (condition report missing, values not recorded, requirements unknown)
```

Readiness is the planner's first discipline: a work that lacks current condition documentation or known handling requirements is not yet movable.

### Move works out

```text
For each checklist work:
→ complete outgoing condition check and link it to the record
→ arrange packing (in-house or via art handler) and book transport
  (directly, or by requesting quotes from a shipping platform)
→ record the dispatch: new location = "in transit"; previous location enters history
→ on arrival: record receipt and incoming condition check; location becomes the venue
```

Moving a set of works to one destination is a batch operation — the same occasion moves dozens of works through identical legs, which is why mature products make bulk location updates and per-occasion worklists first-class.

### During the display period

The work's current location is the venue. Some operators additionally record internal movements (case to wall, wall to store) as finer-grained history; the defining requirement is only that custody never becomes unknown.

### Close and return

```text
At the end date:
→ deinstall; complete outgoing condition check at the venue
→ record the return or forward leg (next venue or home storage)
→ on arrival home: final condition check; location restored to home storage
→ the movement history now shows the complete round trip
→ the occasion's checklist is closed out: every work accounted for, back or onward
```

The closing discipline — every checklist work reconciled to a terminal location — is what distinguishes a run logistics operation from a busy inbox.

### A continuously running loop

Exhibition logistics is not a single project; it is a rotation. Works flow from one occasion to the next, storage is the resting state between occasions, and the operator runs several occasions concurrently at different stages. This is why the work-level view (where is this piece; what is it committed to) and the occasion-level view (what must move, when, and is it ready) are both permanent fixtures of the interface.

## Interfaces

The surfaces below are described conceptually; exact names and layouts vary by product.

### Exhibition / occasion record

The container for one display event.

- typical information: name, venue(s), dates, checklist of works, per-work status, deliverables and deadlines
- primary actions: add/remove works, mark readiness, generate checklists and documents, track completion

### Artwork record — location & shipping view

The custody surface of a single work.

- typical information: current location with detail and date, movement history, condition documentation, insurance value, shipping/handling requirements
- primary actions: update current location (pushing the previous one into history), view history timeline, attach condition reports, record examination

### Movement / shipment schedule

The transport calendar across an occasion or the whole program.

- typical information: legs with dates, carriers/providers, dispatch and delivery confirmations, exceptions
- primary actions: schedule a leg, record carrier details, confirm actual delivery, chase exceptions

### Condition reporting

The documentation surface, whether built in or linked.

- typical information: work identity, condition findings, photographs, examiner, date, linked movement
- primary actions: create a report for an upcoming handover, compare against the previous report, share with the counterpart party

### Reports and cross-party documents

- location reports (current whereabouts of a set of works), checklist reports, condition report printouts, requirement sheets — routinely generated to hand to partner institutions, lenders, or art handlers rather than consumed only inside the operator's own system.

## Important Rules / Behaviors

### One current location, history is append-only

A work has exactly one current location; changing it pushes the previous value into an ordered history rather than overwriting it. The history is the audit trail — retroactive rewrites would defeat the purpose, so movement is recorded as new entries, typically with dates.

### Documentation rides with the movement

Condition statements belong to specific legs, not to the work in general. The pairing of "condition at release" with "condition at receipt" is what makes a handover verifiable; reports float uselessly if they cannot be tied to the moment of custody change.

### Nothing moves undocumented

The practical rule the software enforces through readiness flags and required fields: a work with an open "condition report needed" state, unknown handling requirements, or missing insurance value is not ready to travel. Transport-readiness is a recorded state, not an assumption.

### Custody is two-sided

Each organization records the movements it controls from its own side: the lender's record and the borrower's record of the same physical move are separate views, shared or reconciled by documents (reports, protocols, condition forms). The software does not assume a single global truth of custody — it assumes disciplined documentation on each side.

### The checklist must reconcile

An occasion is complete only when every checklist work is accounted for at close: returned home or forwarded onward, each with its closing condition record. Unreconciled works are the standing exception condition — works delayed in transit, retained at a venue by agreement, or traveling directly to a later show must all be recorded as explicit dispositions rather than left open.

### Commercial and institutional variants share the spine, differ in overlays

A fair booth move and a museum loan move run the same location-and-documentation spine; they differ in the layers around it — agreements and couriers on the institutional side, quotes, speed, and sales context on the commercial side. See Variants.

## Variants

- **Museum / institutional exhibitions** — the deepest variant: movements under loan agreements, formal condition protocols, couriers, insurance policies, and in/out protocols; touring exhibitions rotate the same works across multiple venues under a shared plan.
- **Commercial gallery and art fair operations** — higher frequency, shorter cycles: booth moves, temporary placements, quote-driven shipping through integrated platforms, and location churn between gallery, fair, viewing, and storage.
- **Artist and estate studios** — the outbound side: sending works to exhibitions organized by others, tracking "where they are and when they're due back," often documented through consignment-style paperwork.
- **Corporate and private collections** — movements between storage, offices, and loan requests, typically with the same custody discipline and lighter formality.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Exhibition Planning Platform | upstream sibling | curatorial concept, design, budget, and production planning before anything moves; logistics begins at the physical chain |
| Exhibition Installation Management | venue-side sibling | the work of mounting and deinstalling inside the venue; this Type covers getting works to and from that venue and custody continuity |
| Museum Object Movement Management | broader internal sibling | location tracking and movement control for any reason (storage, conservation, display); this Type is movement organized by a display occasion with cross-party handover |
| Museum Loan Management | agreement-layer sibling | the legal structure of borrowing and lending (requests, approvals, terms, return obligations); logistics is the physical layer those agreements trigger — commonly sibling modules of one museum system |
| Artwork Consignment Management | commercial-basis adjacent | retained-ownership placement with sale/settlement dispositions; exhibitions borrow consignment paperwork in practice, but the structures differ (settlement vs custody chain) |
| Museum Collections Management | containing system (museum side) | the full object-record catalog and stewardship world; exhibition logistics operates as one workflow over its records |
| Art Gallery Management | containing system (commercial side) | inventory, clients, sales; exhibition/fair movement is one capability among many |
| Art shipping / fulfillment platforms | execution layer | quote → book → track transport for unique items without a display occasion; integrated with, not equal to, this Type |
| Convention / Exhibition Management (event industry) | namesake only | manages event logistics for exhibitors and booths (people, stands, freight of goods); no unique-object custody chain |

The densest boundary is with the museum-side siblings, because in real systems they ship as modules of one collection platform. The structural tests: remove the display occasion and only object movement remains; remove the movement chain and only loan management or planning remains; remove the handover documentation and the operator can no longer prove due care — the invariant that makes this its own workflow.

## Representative Products

- **Gallery Systems TMS Collections** — museum incumbent; exhibitions, loans, and shipping as sibling modules beside the object record, with checklists, readiness flags, and condition documentation
- **Zetcom MuseumPlus** — European museum incumbent; exhibition management coordinating participants, venues, and lenders with in/out protocols, beside a contracts module
- **Artlogic** — commercial gallery suite; exhibition and fair records over an artwork location/shipping core with movement history, integrating shipping quotes and condition reporting
- **ARTA** — specialized transport-execution platform (quoting, booking, insurance, tracking for art and collectibles) — the execution layer exhibition logistics systems integrate with
- **Articheck** — specialized condition-reporting and transit-visibility platform shared across galleries, museums, conservators, and shippers

## Sources

Research date: **2026-09-06**

- Gallery Systems — Software for Registrars — https://www.gallerysystems.com/roles/software-for-registrars/
- Gallery Systems — Enhancing Museum Workflows with the TMS Suite — https://www.gallerysystems.com/enhancing-museum-workflows-with-tms-suite/
- Zetcom — MuseumPlus — https://www.zetcom.com/en/museumplus-en/
- Artlogic Support — Finding, creating and updating artwork location details — https://support.artlogic.net/hc/en-gb/articles/360010220119
- Artlogic Support — Integrate with Arta — https://support.artlogic.net/hc/en-gb/articles/360013420399
- Artlogic Support — How to prepare your systems ahead of an art fair — https://support.artlogic.net/hc/en-gb/articles/16269347601820
- Arta Manual — Shipment lifecycle — https://manual.arta.io/guides/getting-started/shipment-lifecycle
- Arta Manual — Logistics services — https://manual.arta.io/guides/logistics
- Arta — https://www.shiparta.com/
- Articheck — https://articheck.com/

> Sourcing limitations: detailed museum-side help documentation (Gallery Systems client community; Zetcom help center) was not reachable on 2026-09-06, so museum-pole observations rest on official product pages and vendor-authored operational articles at module level; screen-level workflow details are deliberately not asserted. The UK museum documentation standard's transportation pages returned errors and were not used. Operational specifics (exact state names, numeric limits, insurance mechanics) are intentionally kept qualitative. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
