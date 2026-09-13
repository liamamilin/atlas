# Museum Collections Management

## Overview

A **Museum Collections Management** system is the museum's operational system of record for its collection: a persistent register of individually identified object records, each carrying the object's current physical location so the institution can always account for everything in its care, together with a recorded custody life — entry, movement, use, care, and exit — kept as an auditable history on the object record.

Museums hold objects in public trust, often for decades or centuries. The defining problem this software solves is **accountability**: for any object, at any moment, the institution must be able to answer what it is, where it physically is, how it got there, who owns it or who lent it, what condition it is in, and whether and how it may leave the building. The system holds the authoritative register of holdings and runs the custody machinery that keeps that answer true.

The defining core is deliberately small:

```text
Collection register of record
└── Object record (per object or object group)
    ├── Current location (place structure + location history)
    ├── Custody events (entry, movement, use, care, exit)
    └── Documentation (identification, description, media, people, links)
```

Everything else commonly associated with these products — controlled vocabularies, integrated media libraries, valuation and insurance tracking, exhibitions and loans as structured workflows, publishing companions — is standard capability of mature products, not what makes the system a collections management system. A paper accession register, a card catalogue, and a kept-current location book satisfy the same structure; the domain standard for this practice explicitly allows paper-based systems.

The record-creating part of this world — formally accessioning objects and building their catalogue records — is a core workflow of the system and is documented separately under Museum Accession / Cataloging. The public-facing publication of collection records is a different Type (Digital Collection Portal). Commercial selling of collection objects belongs to gallery software, not here.

## Users & Context

Primary users are the museum's collection-care staff:

- **Registrar** — owns custody accountability: records objects entering and leaving, manages movement and loan transactions, keeps insurance and valuation documentation current, and produces the registers and reports that demonstrate accountability to the governing body, insurers, and accreditors.
- **Collections manager** — runs day-to-day custody: assigns and updates storage locations, plans and executes moves, conducts inventory checks, and keeps the location picture reconciled with physical reality.
- **Curator** — builds and uses the intellectual content: catalogue depth, attributions, scholarship, and the selection of objects for display and research.
- **Conservator** — records condition assessments and treatment work on the objects they examine.

In larger institutions these roles are distinct, with collections database managers and digital asset managers alongside. In small museums, historic houses, and historical societies the same duties are carried by a curator-registrar hybrid plus volunteers, working in the same system.

The work environment is back-office and physical: storage rooms and shelves, galleries, loading docks, conservation studios, and the registrar's desk — with mobile capture on the floor (photographing and documenting objects in storage) increasingly normal. The governing context is the institution's collections management policy, which defines what may be acquired, how objects are numbered, under what conditions they may travel or be borrowed, and the exceptional procedure by which an object may leave the collection permanently.

## Core Model

### The object record

The unit of the system is the **object record** — one persistent, individually identified record per object (or per defined group of objects treated as a unit). It is the central, living record of that item: what it is, where it came from, why it matters, and how it is managed. Everything else in the system attaches to it — images and documents, the people associated with it (maker, donor, lender, borrower), the events of its custody life, its condition and treatment history, its valuations, and its appearances in exhibitions and loans. Object records are long-lived: they outlive the staff who wrote them, and institutions migrate them across systems and generations of software.

Together the object records form the **collection register of record** — the authoritative account of what the institution holds. Depth of documentation is set by each institution's policy and varies enormously; the register, not any fixed level of description, is the constant.

### Location and the place structure

Every object record carries the object's **current location** within a place structure the institution defines — storage rooms, shelving and drawer hierarchies, gallery spaces, off-site venues. When an object moves, the record is updated; the trail of past locations is retained as the object's location history. The domain standard describes this procedure plainly: keep a record of where all objects in care can be found, and update it each time an object is moved, because an up-to-date location record is the key to being accountable for the collection.

```text
Object record
  ├── current location → place in the institution's place structure
  ├── location history → where it has been, in order
  └── custody events → what happened to it, in order
```

### Custody events

The actions that change an object's custody status are recorded as events on its record, forming a managed lifecycle:

- **In** — object entry and formal acquisition into the collection (with the accessioning machinery: source, method of acquisition, title evidence, and a unique number that binds the physical object to its record and paperwork)
- **Within custody** — location changes, inventory verification
- **Use** — display in exhibitions, loans out to other institutions, loans in from lenders
- **Care** — condition checks and technical assessments, conservation treatment
- **Value and rights** — valuations, insurance and indemnity, reproduction and rights agreements
- **Out** — object exit, including the governed exception of deaccessioning and disposal

Each event is attributed and accumulates on the record, so the system answers not only "where is it now" but "what has ever happened to it."

### Supporting records

Around the object record, mature systems hold:

- **People records** — donors, makers, artists, lenders, borrowers, contacts — linked to objects and to transactions
- **Media** — images and files attached to records (in many products backed by integrated digital-asset functionality, or a companion product)
- **Exhibition and loan records** — the occasions and agreements through which objects are used, each linking the participating objects and parties
- **Bibliographic and archival records** in institutions whose holdings extend beyond objects

### One structure, many implementations

The core model is conceptual; realizations differ. Object numbering follows each institution's numbering scheme (accession-derived numbering being the common museum pattern). Place structures range from a few room-level locations to shelf-and-tray hierarchies. Event vocabularies differ by product and institution. What does not vary is the three-part spine: the register, the maintained location picture, and the event layer.

## How It Works

The system's work is a set of recurring loops over the object record, not a single pipeline:

**Intake and numbering.** An object enters through recorded object entry and, if it joins the permanent collection, formal acquisition and accessioning: source and method of acquisition are documented, title evidence is retained, and a unique number is assigned — the number that binds the physical object to its record and its acquisition paperwork. Cataloguing then builds the record's descriptive content, an open-ended process documented under Museum Accession / Cataloging.

**Housing and tracking.** The object is assigned a storage location. Every subsequent move — between shelves, to a gallery, to a conservation studio, to a borrowing institution — updates the location on the record and adds to its location history. Movements may be initiated as recorded transactions with approvals, especially when an object leaves the building.

**Use.** When an object is chosen for an exhibition, the exhibition record links to it and its use history accumulates. When it travels to another institution, a loan record structures the transaction: request and approval, agreement terms, condition checking at release and return, transport and insurance arrangements, and the eventual return that restores the object to its home location. Borrowing works symmetrically: borrowed objects are tracked in the same system under their loan records, clearly distinct from owned collection.

**Care.** Condition checks are recorded at natural moments (intake, release for loan, return, before and after treatment) and conservation treatments are documented as work performed on specific objects, with their reports and imagery attached to the record.

**Value, insurance, and rights.** Valuations are recorded and revised over time; insurance and indemnity coverage is documented against objects and against specific transactions such as loans. Rights and reproduction agreements — who may photograph or license an object, with what credit line — are kept against the record.

**Counting.** Institutions periodically verify that the location picture matches physical reality, checking locations against the register (increasingly assisted by barcode or similar scanning). Discrepancies become investigations on the record.

**Exit.** Objects leave the collection only through a governed exit procedure — deaccessioning under the collections management policy, with the decision, justification, method of disposal, and outcome recorded on the object record, which is retained even after the object is gone.

**Publication (adjacent).** A controlled subset of records is typically published to a public or internal web surface through a companion capability — a separate product or component in many suites. Publication reads from the register; it does not run custody.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Object record detail

The hub surface — one screen per object.

- Typical information: identification and description, images, current location, object number, associated people, condition notes, valuation, links to exhibitions, loans, and treatments, event history
- Primary actions: edit metadata, attach media and documents, update location, record an event, navigate to linked records and transactions

### Search and collection browsing

The way staff work across the register.

- Typical information: result lists and image grids over the whole collection, saved queries, filtered views by classification, location, or event status
- Primary actions: search, refine, batch-select, export, open records

### Location and movement tools

The custody picture and its updates.

- Typical information: place-structure browser (storage hierarchies, galleries, off-site), objects at a place, pending and historical movements, per-object location history
- Primary actions: record a move, plan a move, verify locations during inventory, print or scan location labels

### Loan and exhibition workspaces

The transaction surfaces for use of the collection.

- Typical information: loan requests and agreements (parties, terms, dates, insurance), checklists of participating objects with per-object status, exhibition checklists and schedules
- Primary actions: create and progress a loan or exhibition, attach objects, record condition checks at handover, close and confirm returns

### Condition and conservation documentation

The care surface.

- Typical information: condition reports with imagery, treatment proposals and reports, examination records
- Primary actions: create a condition or treatment record, attach media, link to the object record

### Registers and reports

The accountability surface.

- Typical information: accession registers, location listings, valuation schedules, loan and exhibition reports, event histories
- Primary actions: generate, filter, and export

### Data and configuration tools

- Primary actions: import and migrate records, batch edit, clean and reconcile data, configure fields and forms, manage users and permissions

### Publishing companion

A separate surface (often a separate product) that renders a chosen subset of records for public or internal discovery — the Digital Collection Portal Type.

## Important Rules / Behaviors

**The location picture must match physical reality.** Custody accountability is the point of the system: an object's recorded location is a claim the institution makes to its governing body, insurers, and accreditors. Procedures therefore emphasize prompt recording of every move, and inventory verification exists to reconcile record against reality.

**The object number is the binding thread.** The unique number assigned at accession links the physical object, its record, and its paperwork. All events, documents, media, and transactions reference the object through this identity. Numbering schemes are institutional policy and are commonly enforced by the system.

**Custody events accumulate; records persist.** An object's record is append-oriented history, not a mutable snapshot: earlier states remain reconstructible, changes are attributable, and records survive the object's exit from the collection. Institutions depend on this across staff turnover and decades.

**Not everything in the building belongs to the institution.** Objects on loan in, and property held but not accessioned (teaching and handling collections, props), live in the same system but under distinct custody semantics — their records mark what the institution is accountable for versus what it owns. Conflating the two is a named failure the record structure exists to prevent.

**Loans impose obligations in both directions.** A lent object is bound by an agreement: fixed dates, condition requirements, transport and insurance arrangements, and a return obligation. The loan record structures these as tracked, checkable states rather than informal arrangements.

**Exit is a governed exception.** Removing an object from the collection permanently (deaccessioning) runs under the collections management policy with recorded justification and method of disposal; sale of collection objects is not a normal terminus of this software's world — that is the commercial gallery's structure, not the museum's.

**Sensitive custodial data is access-controlled.** Valuations, donor identities (including donors who wish to remain anonymous), and security-relevant location detail are the kinds of information whose visibility is restricted by role.

**Auditable change.** In mature products, changes to records are captured with who, when, and what changed; the accession record in particular is maintained as tamper-resistant with security copies, reflecting the legal weight of ownership evidence.

## Variants

- **Enterprise suites** — the incumbent pattern for large institutions: the collections core surrounded by companion products for conservation documentation, digital assets, publishing, and audit tooling; heavy configuration; on-premises or vendor-hosted deployment.
- **Cloud-native products for small institutions** — subscription systems for museums, historic houses, historical societies, and collectors; simplified configuration, mobile capture, built-in multi-user collaboration, publishing built in rather than as a companion.
- **Open-source, self-hosted platforms** — configurable cataloguing cores with a separate optional public front-end; chosen by resource-constrained institutions and projects needing heterogeneous, standards-flexible data models.
- **Discipline breadth** — fine art, history, natural history, and mixed collections differ in classification systems and descriptive depth, not in structure; institutions holding archives or libraries run hybrid modules beside the object register.
- **Archaeological collection management** — the discipline variant for excavated material: the same custody spine with an excavation-context documentation layer (site → context/stratum → object) as first-class content.
- **Private-collector and corporate postures** — the same record-plus-custody core sold to personal collectors (acquisition, value, insurance, provenance) and corporate or brand collections (location, valuation, acquisition), without the institutional policy frame.
- **Multi-site and touring** — organizations managing several venues, or touring exhibitions rotating works across venues, run the same machinery across a wider place structure.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Accession / Cataloging | core workflow slice | the record-creating workflow (accessioned intake, catalogue records, ongoing enrichment) documented as its own Type; it is this system's core, not sold standalone |
| Archaeological Collection Management | discipline variant | same custody spine plus the excavation-context layer (site → context/stratum → object) as first-class documentation |
| Museum Object Movement Management | workflow sibling | internal location tracking and movement control as one procedure family inside this system |
| Museum Loan Management | workflow sibling | the legal/agreement structure of borrowing and lending — one custody-event family here |
| Museum Conservation Management / Museum Condition Reporting | workflow siblings | care and condition documentation workflows run on this system's records |
| Exhibition Planning / Installation Management / Artwork Exhibition Logistics | workflow siblings | display-occasion workflows (selection, install state, movement chain) operating over the object records; shipped as modules of the same suites |
| Digital Collection Portal | publishing complement | public discovery over a controlled subset of records governed here; no custody machinery of its own |
| Art Gallery Management | nearest commercial neighbor | galleries hold commercial stock whose terminal state is a sale (offer → invoice → consignment settlement); museums hold a permanent collection under governed, non-commercial exit — remove the sale loop from gallery software and what remains is this Type's territory |
| Cultural Heritage Asset Management | registry neighbor | place-based heritage inventories (monuments, buildings, sites) hold records, not objects under custody — no per-object locations, movements, or loans |
| Enterprise Asset Registry / asset inventory | generic neighbor | tracks what an organization owns and where; lacks acquisition events under a collecting policy, provenance and scholarship content, permanent-custody commitment, and governed deaccession |
| Media Asset Management | file-world neighbor | manages media files (masters and derivatives) as the unit of record; here media is documentation attached to physical objects under custody |
| Integrated Library System / Archives Management System | institution neighbor | bibliographic copies under circulation, or archival materials organized by provenance and series — different object worlds and legal semantics from unique objects under permanent custody |
| Museum Visitor Experience Platform | audience-facing neighbor | visitor-side interpretation and experience; this system is staff-facing custody of record |

## Representative Products

- **TMS Collections** (Gallery Systems) — enterprise incumbent serving large museums; collections core with companion products for conservation documentation, digital assets, publishing, and audit
- **MuseumPlus** (Zetcom) — European incumbent; collection management with contracts and exhibition management, deployed in-house or as SaaS
- **CatalogIt** (It Unlimited) — cloud-native system for small museums, historic houses, historical societies, and collectors; also sells the same core into conservator, organization, and personal plans
- **CollectiveAccess** (Whirl-i-Gig) — open-source, self-hosted collections management with a separate optional public front-end (Providence / Pawtucket)

The definition was checked against the domain standard (Spectrum, the UK museum collections-management standard used internationally, which explicitly allows paper-based systems) and against the sibling leaves already documented in this atlas, to avoid fitting the Type to one vendor's suite packaging.

## Sources

Research date: **2026-09-08**

- Collections Trust — Spectrum 5.1 (standard overview; primary and further procedures; Location and movement control procedure): https://collectionstrust.org.uk/spectrum/ , https://collectionstrust.org.uk/spectrum/primary-procedures/ , https://collectionstrust.org.uk/spectrum/procedures/ , https://collectionstrust.org.uk/spectrum/primary-procedures/location-and-movement-control-spectrum-5-0-primary-procedures/
- Collections Trust — software directory entry "TMS Collections and eMuseum": https://collectionstrust.org.uk/software/tms/
- Gallery Systems — Collections Management with TMS Collections: https://www.gallerysystems.com/solutions/collections-management/
- Zetcom — MuseumPlus: https://www.zetcom.com/en/museumplus-en/
- CatalogIt — product page and help center (What is an Entry?; Museum Features: accession/acquisition/deaccession profiles, forms): https://www.catalogit.app/ , https://support.catalogit.app/en_US/entries/what-is-an-entry , https://support.catalogit.app/en_US/museum-features
- CollectiveAccess — official documentation: https://manual.collectiveaccess.org/

> Sourcing limitation: deep operational documentation for the enterprise incumbents (TMS Collections, MuseumPlus) is login-gated, and several other market products (Axiell Collections, PastPerfect, Vernon CMS, Lucidea Argus) were unreachable from the research environment on 2026-09-08 (or in prior sibling passes). Observations for those products rest on vendor product pages and the Collections Trust software directory; screen-level claims are avoided for them. Precise numeric limits, plan terms, and product-specific machinery are deliberately not asserted in this document; detailed evidence is recorded in the paired Research Notes.
