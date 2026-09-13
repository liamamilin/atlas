# Research Notes — Museum Collections Management

Research date: 2026-09-08
Leaf: Museum Collections Management (§27 Media, Entertainment, Creator & Culture — museum/cultural-heritage cluster)
Slug: museum-collections-management

## Research Goal

Understand what a "Museum Collections Management" system actually is in the real market — the containing system of record for a museum's collection — and resolve the joint-review obligations pre-hung on this leaf by prior passes:

1. **museum-accession-cataloging** (processed 2026-09-08) flagged this leaf as the "containing system" and recommended keep-both-with-containment vs fold-as-documentation-layer — final call at this pass's joint review.
2. **archaeological-collection-management** (processed 2026-09-06) flagged a probable Variant-of relationship (shared custody spine; excavation-context layer as differentiator) — joint review at this pass.
3. **art-gallery-management** (processed 2026-09-06) flagged the commercial-disposition-loop boundary for joint review.
4. **digital-collection-portal** (processed 2026-09-07) and the **exhibition cluster** (planning / installation / logistics, all processed 2026-09-07) documented this leaf as their substrate/containing system and recommended joint review.
5. Unprocessed siblings museum-object-movement / museum-loan / museum-conservation / museum-condition-reporting and provenance-research-platform and museum-visitor-experience-platform are expected counterparties; noted, not discharged here.

The document must also define this Type against generic neighbors (Enterprise Asset Registry, Media Asset Management, Integrated Library System, Archives Management System, Cultural Heritage Asset Management).

## Initial Boundary

Hypothesis before research: Museum Collections Management (in museum practice, "CMS" = collections management system) is the museum's **operational system of record for the collection as a whole** — the object register plus the custody machinery (locations, movements, loans, condition/conservation, valuation, rights, exit) that the accession/cataloging workflow feeds. The directory has carved the workflow slices into sibling leaves; this leaf is the container. Confusion risks:

- Museum Accession / Cataloging (the record-creating workflow — its core; joint-review obligation)
- Archaeological Collection Management (discipline variant)
- Art Gallery Management (commercial disposition loop)
- Cultural Heritage Asset Management (place-based inventories without object custody)
- Digital Collection Portal (publication of records vs custody of objects)
- Exhibition Planning / Installation / Logistics (workflows over the records)
- Enterprise Asset Registry / asset inventory (generic assets without documentation mission)
- Media Asset Management (media files vs physical objects)
- Integrated Library System (bibliographic copies vs unique objects)

## Research Questions

1. What is the unit of record, and what does the system hold besides object records?
2. What does "custody accountability" mean operationally (locations, movement, inventory) and is it definitional?
3. Which custody-lifecycle events are standard (intake, movement, loans, condition, conservation, valuation, rights, exit/deaccession), and how are they attached to the object record?
4. Who uses the system (registrar, collections manager, curator, conservator, database manager) and what does each do?
5. What rules matter (location currency, numbering, audit, deaccession governance, confidentiality of lenders/donors/valuations, custody of non-owned objects)?
6. How do the four poles (enterprise incumbent, European incumbent, SMB cloud, open-source) realize the same Type differently?
7. Does the paper-era museum office satisfy the definition (historical check)?
8. Joint-review resolutions: keep-both-with-containment for accession-cataloging? variant status for archaeology? ratified boundary for galleries?

## Representative Products

Selected for market representation, documentation reachability, different product philosophy, and different customer tier (the same four poles the accession pass reached; Axiell, PastPerfect, Vernon, Lucidea remained unreachable — see Sources):

| Product | Vendor | Pole | Evidence level reached |
|---|---|---|---|
| TMS Collections | Gallery Systems | enterprise museum incumbent (800+ clients, 23 countries; Spectrum 5 compliant) | product page + detailed Collections Trust software-directory entry |
| MuseumPlus | Zetcom | European museum incumbent (900+ museums; SaaS or in-house) | product page (module/function level) |
| CatalogIt | It Unlimited, Inc. | SMB / cloud-native (museums, historic houses, collectors; also conservator/organization plans) | Tier-1 help center + product pages + vendor-authored articles |
| CollectiveAccess (Providence/Pawtucket) | Whirl-i-Gig | open-source, self-hosted | official documentation landing (positioning level) |

Backbone standard consulted: **Spectrum 5.1** (Collections Trust) — the UK museum collections-management standard used internationally, defining the procedure set the product category implements (9 primary procedures + 12 further procedures). Not a product.

Not usable (consistent with sibling passes): Axiell Collections (404/unreachable), PastPerfect (403 in two prior passes — not retried per network rules), Lucidea Argus (403), Vernon Systems (unreachable), Gallery Systems/Zetcom deep help centers (login-gated). No screen-level claims are made for products beyond what the reachable pages state.

## Sources

- Collections Trust — Spectrum 5.1 overview ("Spectrum is not software… many of our commercial Spectrum Partners have developed collection management systems that support some or all of the Spectrum procedures"): https://collectionstrust.org.uk/spectrum/
- Collections Trust — Spectrum primary procedures index (Object entry; Acquisition and accessioning; Location and movement control; Inventory; Cataloguing; Object exit; Loans in; Loans out; Documentation planning): https://collectionstrust.org.uk/spectrum/primary-procedures/
- Collections Trust — Spectrum all-procedures index (adds Use of collections; Condition checking and technical assessment; Collections care and conservation; Valuation; Insurance and indemnity; Emergency planning for collections; Damage and loss; Deaccessioning and disposal; Rights management; Reproduction; Collections review; Audit): https://collectionstrust.org.uk/spectrum/procedures/
- Collections Trust — Location and movement control (primary procedure page; scope statement on accountability): https://collectionstrust.org.uk/spectrum/primary-procedures/location-and-movement-control-spectrum-5-0-primary-procedures/
- Collections Trust — software directory entry "TMS Collections and eMuseum" (detailed operational description incl. location-history audit trail, Spectrum procedures list, deployment, licensing): https://collectionstrust.org.uk/software/tms/
- Gallery Systems — Collections Management with TMS Collections (positioning, roles, disciplines, companion solutions): https://www.gallerysystems.com/solutions/collections-management/
- Zetcom — MuseumPlus (core functions, modules, SaaS/in-house, 900+ clients): https://www.zetcom.com/en/museumplus-en/
- CatalogIt — product page (plans; Snap/Document/Use; "value, location, and condition… in real time"; Museum plan "Accession, exhibition, loan, and location documentation"): https://www.catalogit.app/
- CatalogIt — help center: What is an Entry? https://support.catalogit.app/en_US/entries/what-is-an-entry ; Museum Features category (Creating The First Entry, Museum Accession Profile, Museum Acquisition Profile, Museum Deaccession Profile, Generating Collections Forms): https://support.catalogit.app/en_US/museum-features
- CollectiveAccess — official documentation: https://manual.collectiveaccess.org/

Source-access limitations: doc/wiki hosts for CollectiveAccess beyond the manual landing remain unreachable (as in the accession pass) — CollectiveAccess evidence stays at positioning level. Axiell returned 404 on the attempted solutions URL and was abandoned after one retry attempt; PastPerfect/Lucidea/Vernon were not retried given repeated prior 403s. TMS/MuseumPlus operational depth beyond the directory entry is login-gated. Consequently, screen-level operational claims are anchored on CatalogIt's Tier-1 help center plus the Collections Trust directory entry for TMS; MuseumPlus and CollectiveAccess observations are module/positioning level. Precise numeric limits, exact state names, and plan-specific machinery stay in these notes (or are omitted) rather than being asserted as Type facts.

## Product / Standard Observations

### Spectrum 5.1 (Collections Trust) — domain standard [Evidence A for the standard's own content]

- Category definition by the standard itself: "Spectrum is not software (and can be used with paper-based systems) but many of our commercial Spectrum Partners have developed collection management systems that support some or all of the Spectrum procedures. We have validated some of these as Spectrum Compliant." — the domain's own statement that the product category = software (or paper) realizing the Spectrum procedure set.
- **Nine primary procedures**: Object entry; Acquisition and accessioning; Location and movement control; Inventory; Cataloguing; Object exit; Loans in (borrowing objects); Loans out (lending objects); Documentation planning.
- **Twelve further procedures**: Use of collections; Condition checking and technical assessment; Collections care and conservation; Valuation; Insurance and indemnity; Emergency planning for collections; Damage and loss; Deaccessioning and disposal; Rights management; Reproduction; Collections review; Audit.
- Location and movement control scope (primary procedure): "Keeping a record of where all the objects in your care can be found, and updating the location each time an object is moved." And: "As well as recording when objects move in and out of your museum you should also keep track of them within the museum too. Following this procedure promptly keeps your location records up to date, which is the key to being accountable for collections in your care." — the accountability framing of custody.
- (From the accession pass, same standard: accessioning = formal numbered intake with title-transfer evidence and long-term-care commitment; cataloguing = ongoing, never-complete record building per object; object number binds object ↔ record ↔ paperwork.)

### TMS Collections (Gallery Systems) — enterprise incumbent [Evidence A for vendor pages + Collections Trust directory entry]

- Positioning: "the world's leading collections management system for museums and institutions… handles every facet of your workflow" (product page); directory entry: "designed specifically for collections, content, media, exhibition, and loan management… organize and manage all collection types without compromise."
- Directory entry: "comprised of 11 interrelated modules, with supporting functionality for entering and tracking all collections data and management activities."
- Spectrum procedures supported (directory entry, verbatim): Object Entry (primary), Acquisition and accessioning (primary), **Location and movement control (primary)**, Inventory (primary), Cataloguing (primary), Object Exit (primary), Loans In (primary), Loans Out (primary), Condition checking and technical assessment, Collections care and conservation, Valuation, Insurance and indemnity, Damage and loss, Deaccessioning and disposal, Rights management, Use of collections, Audit. "Spectrum 5 compliant."
- **Location history**: "a complete location history audit trail is maintained for each object and component of an object."
- Audit machinery (directory entry): built-in audit trail capturing date, login ID, table, column, old value, new value, with user-entered explanations/approvals; separate Audit Manager product for configurable field-level auditing.
- Cataloguing machinery (directory entry): catalogue and cross-reference "from object data to constituents"; thesaurus as standard (supplied with Getty AAT and TGN); user-defined data-entry forms; object import; multilingual cataloguing; data-cleaning alerts ("e.g. the creation of an object record without a title being recorded").
- Rights (directory entry): integrated Rights and Reproductions module; Registration menu Rights and Reproduction screen records agreement send/receive/sign dates, rights granted, restrictions, credit line. Access control to "the names of lenders and donors, who wish to remain anonymous, by individual user account."
- Media (directory entry): integrated DAMS functionality — media module records for digital files and physical media objects; unlimited media linked to records; copyright tracked at object or media level.
- Roles (product page): Registrars, Collections Managers, Museum Conservators, Curators, Digital Asset Managers, Collections Database Managers.
- Disciplines (product page): fine art, history, natural history, archives & special collections, corporate art, private collections, public art, time-based media, university museum collections.
- Suite packaging: companion products TMS Conservation Studio (conservation documentation), TMS Media Studio (DAM), Audit Manager, eMuseum (online collections publishing); "TMS Collections lies at the centre of a multifaceted suite."
- Deployment/licensing (directory entry): web-based; web hosted or locally hosted; per-concurrent-user licensing; localized in 24 languages; 800+ clients in 23 countries; bibliographic and archival modules (ISAD(G), EAD, MARC) configurable.

### MuseumPlus (Zetcom) — European incumbent [Evidence A for its product page]

- "Web-based Museum Management… comprehensive, flexible standard application provides real-time museum management and fully documents any type of collection and all related workflow."
- Core functions: "Comprehensive cataloging, registration and management of all objects in your collection"; Customer Service ("central register for internal and external contacts"); Digital Assets ("images and other digital media can be linked to objects, artists, addresses and other entries"); **Contracts** ("management of agreements and contracts relating to exhibitions, loans and collection objects"); **Exhibition Management** ("coordination of participants, venues and lenders, as well as input and output protocols").
- "Additional modules such as event management, archiving, etc. can be seamlessly integrated."
- "High degree of flexibility in the definition of data fields, modules, forms and reporting"; API for data exchange.
- Deployment: in-house or SaaS ("all IT infrastructure is outsourced"). 900+ museums (Louvre, Museo Egizio, Nasjonalmuseet, etc.).
- Product family beside the CMS: eMuseumPlus (publishing), MuseumPlus Scan, Media Guide, Curator (3D exhibition planning add-on), ArtPlus.

### CatalogIt — SMB / cloud-native pole [Evidence A; Tier-1 help center + product pages]

- Entry (object record): "An Entry in CatalogIt represents one individual item (or object record) in your collection… Your Entry is the central, living record of that item — capturing what it is, where it came from, why it matters, and how it's managed. From an Entry, you can view and edit metadata, attach media, link related records, organize into Folders, generate reports, and keep your documentation up to date in one place." Related records attachable: "people, places, accessions, exhibitions, or documents."
- **Custody tracking on the record**: entries track "value, location, and condition — adding to their stories in real time" (product page, Document It).
- Museum plan capabilities (product page): "Authoritative data fields", **"Accession, exhibition, loan, and location documentation"**, "Workflow and multi-user capabilities."
- Profile structure (help center): Museum Accession Profile (formal intake); Museum Acquisition Profile ("Document items that are in your institution but are not intended to be a part of the permanent collection" — the non-owned/props distinction); Museum Deaccession Profile ("Learn how to deaccession an item from your collection"); Generating Collections Forms ("Generate standardized forms directly from your CatalogIt records" — deed of gift per vendor blog).
- The use loop (product page, "Use It"): "managing and maintaining your objects, coordinating exhibitions, and sharing your stories" — publishing via HUB, API, WordPress plugin, iframe, "Include only the entries and data you want to share."
- Roles/audiences (product page): museums, historic houses and preservation societies, libraries and archives, cultural centers; personal collectors; organizations (corporate collections, brand archives); consultants (installers, preparators, appraisers); conservators ("Condition and conservation-tracking capabilities… tracking each step for complete accountability").
- Capture posture: phone-camera capture "at a historic site, in a basement storage room, at an auction"; multi-user staff + volunteers; AI "Describe Image" assistant; bulk editing; Getty AAT terms.
- Permissions: "Users with Owner, Admin, Read/Write, and Editor permissions can create and edit Entries."
- Vendor-authored workflows: blog posts on traveling-exhibition tracking ("Track Every Mile") and deed-of-gift generation.
- Plan structure: Museum / Personal / Organization / Conservator — the same record core sold to four audiences; Personal plan tracks "acquisition, value, insurance, provenance"; Organization plan "tracking location, valuation, and acquisition information."

### CollectiveAccess / Providence — open-source pole [Evidence A for manual landing; positioning only]

- "CollectiveAccess is collections management and presentation software… The project began in 2003 as a response to the complete lack of non-commercial, affordable, open-source solutions for digital collections management."
- Component split: "Providence is the core cataloguing application of CollectiveAccess where data, media and metadata is input, edited, and managed. Pawtucket is the optional, public web-access tool for digital publication and discovery."
- "Designed to handle large, heterogeneous collections that have complex cataloging requirements and collections which need support for a variety of metadata standards and media formats."
- "Selected features are designed to handle various aspects relating to data modeling, workflow management, web publishing, granular control and digital preservation."
- Relational ("relationships between various items within a given collection, situating objects within a broader network"); configurable; DACS, Dublin Core, VRA Core; LCSH, Getty AAT; web-based, self-hosted; GPLv3; projects on 5 continents, "hundreds of institutions."

## Cross-product Comparison

| Dimension | TMS Collections | MuseumPlus | CatalogIt | CollectiveAccess | Spectrum (standard) |
|---|---|---|---|---|---|
| Object record as unit | object records + constituents cross-referenced; 11 modules around them | "management of all objects in your collection" | Entry = "one individual item (or object record)… central, living record" | Providence: "data, media and metadata is input, edited, and managed" | "a catalogue record for each object, or group of objects" (per accession pass) |
| Location/custody tracking | "complete location history audit trail… for each object and component" | module level only (not separately itemized on reachable page) | entries track "location… in real time"; Museum plan "location documentation" | not verified (positioning only) | primary procedure: record where objects "can be found", update on every move; "key to being accountable" |
| Movement/inventory | Location and movement control + Inventory procedures supported | "all related workflow" (module level) | workflow + multi-user; location updates in real time | "workflow management" (feature class named) | primary procedures (Location and movement control; Inventory) |
| Intake/exit events | Object Entry, Acquisition and accessioning, Object Exit, Deaccessioning and disposal procedures | Contracts module covers object agreements | Accession / Acquisition / Deaccession profiles; deed-of-gift forms | not verified | Object entry; Acquisition and accessioning; Object exit; Deaccessioning and disposal |
| Loans | Loans In / Loans Out (primary procedures) | Contracts (exhibition/loan agreements) | loan documentation (Museum plan); traveling-exhibition workflows (vendor blog) | not verified | Loans in; Loans out (primary procedures) |
| Condition/conservation | Condition checking; Collections care and conservation procedures; companion Conservation Studio | not itemized (reachable page) | condition tracked on entries; Conservator plan "condition and conservation-tracking… complete accountability" | "digital preservation" named (not conservation) | Condition checking; Collections care and conservation |
| Valuation/rights | Valuation; Insurance and indemnity; Rights management procedures; Rights & Reproduction screen | not itemized | value tracked on entries; insurance (Personal plan) | not verified | Valuation; Insurance and indemnity; Rights management; Reproduction |
| Exhibitions | Use of collections procedure; exhibition in directory positioning; sibling modules documented by exhibition passes | Exhibition Management (participants, venues, lenders, in/out protocols) | exhibition documentation + "coordinating exhibitions"; traveling-exhibition blog workflow | web publishing only | Use of collections |
| People records | constituents | central contact register | people/places attachable to entries | relational authorities (LCSH/AAT) | owner's-contribution / history-association info groups (per accession pass) |
| Media | integrated DAMS; 120 formats; media module | Digital Assets linked to objects | media central to Entry | media + metadata managed | (media as object-linked documentation) |
| Publishing companion | eMuseum (separate product) | eMuseumPlus (separate product) | HUB / API / WordPress / iframe (built-in, controlled subset) | Pawtucket (separate component) | (out of scope for the standard) |
| Audit | built-in audit trail old→new values + location history; Audit Manager product | not observed | not directly observed | "granular control" (positioning) | Audit procedure; tamperproof accession register (per accession pass) |
| Roles served | registrar, collections manager, conservator, curator, DAM manager, database manager | (institutions broadly) | museum staff + volunteers; conservators; consultants; collectors | (institutions/projects) | (procedures assume institutional roles) |
| Deployment | web-hosted or locally hosted; concurrent-user licensing | SaaS or in-house | cloud SaaS subscription | self-hosted open source | (paper allowed) |
| Segment | 800+ clients, 23 countries, 24 languages | 900+ museums, Europe-heavy | museums/historic houses/collectors (25k-entry plans) | hundreds of institutions, 5 continents | UK accreditation frame, used internationally |

Reading of the matrix: every pole realizes the same three-part structure — a per-object record of record, live location/custody tracking on that record, and a family of custody-lifecycle events (intake, movement, use, care, value, exit) written back to it. Segment determines packaging depth (suite companions, audit tooling, standards breadth), not the structure. The standard (Spectrum) names exactly this procedure family as what a collections management system implements.

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

Museum Collections Management is the museum's **collection system of record**: the operational system that holds the collection's register and runs its custody. Three jointly-loaded structures:

1. **The collection register of record.** A persistent, individually identified record per object (or defined object group) that together constitutes the authoritative register of what the institution holds — the hub record to which everything else attaches. (Remove → there is no collection to manage; workflows would operate on records that do not exist.)
2. **Object-level custody accountability.** Each object record carries the object's current physical location within the institution's place structure (storage locations, display spaces, off-site venues), updated whenever the object moves, with location history retained — so that at any moment the institution can answer "where is this object in our care?" and demonstrate accountability for it. (Remove → a documentation-only catalog: precisely the accession/cataloging sibling's territory, or a bibliographic/asset catalog with no custody picture.)
3. **The custody-lifecycle event layer.** The actions that change an object's custody status across its institutional life are recorded as events attached to the object record — intake (object entry, acquisition/accession), movement within custody (location updates, inventory checks), use (loans out, loans in, exhibition/display), care (condition checking, conservation treatment), and exit (deaccessioning, object exit/disposal) — accumulating into an auditable custody history per object and a managed lifecycle for the collection. (Remove → a located but static inventory: nothing is managed.)

Jointly-held is load-bearing: 1 alone = a catalog/database (the record-creating sibling's slice, or a bare object database); 2 alone = a location spreadsheet / asset tracker; 3 alone = workflow tooling over records that do not exist; 1+2 without 3 = frozen located inventory below the Type; 1+3 without 2 = custody paperwork over objects of unknown whereabouts; 2+3 without 1 = barcoded asset tracking with no documentation core.

Anchor evidence: Spectrum's procedure set (the domain's own normative definition of collections management) is exactly this structure — Cataloguing + Inventory (leg 1), Location and movement control (leg 2), and the event procedures Object entry / Acquisition and accessioning / Object exit / Loans in / Loans out / Condition checking / Collections care and conservation / Deaccessioning and disposal / Valuation / Insurance / Rights management / Audit (leg 3) — and all four sampled products carry the structure (TMS's directory-entry procedure list is the fullest single statement; CatalogIt states location/value/condition tracking on the Entry; MuseumPlus and CollectiveAccess state it at module/positioning level).

### L1 — Common Mature Structure (very common in mature products, not definitional)

- Formal accession machinery on intake (numbered, evidenced, policy-governed) and its paperwork (deed of gift etc.) — the accession/cataloging sibling's documented core; standard here, not the container's invariant
- Authority/terminology control (Getty AAT/TGN, LCSH) for consistent description
- Person/constituent records (donors, makers, lenders, borrowers, contacts) linked to object records
- Images and media attached to records; integrated DAM functionality (or companion product)
- Rights and reproduction management (agreements, credit lines, restrictions)
- Valuation and insurance-indemnity tracking
- Audit trails of record changes (old→new values, attributable); location history as a dedicated audit trail (TMS-documented; generalizable as common)
- Exhibition modules operating over the records (see the exhibition sibling leaves)
- Loans as structured agreements with terms, condition checks, and return obligations
- Search across the collection; batch editing; data import/migration; data-cleaning and consistency tooling; structured reports and registers
- Multi-user roles and permissions; confidentiality controls (e.g., anonymous donors/lenders visible only to some users)
- Inventory support (barcode/QR-assisted location verification) — current-era machinery
- Configurable record structure (fields, forms, screens per institution/discipline)

### L2 — Variant / Optional Structure

- Segment: national/large institutions (TMS, MuseumPlus) vs small museums, historic houses, historical societies (CatalogIt) vs resource-constrained/self-hosted projects (CollectiveAccess)
- Private-collector and corporate-collection postures: the same record+custody core sold to personal collectors (acquisition, value, insurance, provenance) and organizations (location, valuation, acquisition) without the museum's institutional policy frame
- Discipline breadth: fine art, history, natural history, archaeology (→ Archaeological Collection Management variant), archives & library hybrids (bibliographic/archival modules), corporate art, time-based media
- Deployment: vendor-hosted SaaS (CatalogIt; MuseumPlus SaaS option) vs on-prem/local hosting (TMS both options; MuseumPlus in-house) vs self-hosted open source (CollectiveAccess)
- Suite packaging: standalone CMS vs center-of-suite (conservation documentation, DAM, publishing, audit tooling as companion products)
- Public publishing: separate companion product (eMuseum/eMuseumPlus), separate component (Pawtucket), or built-in controlled publishing (CatalogIt HUB) — a separate Type (Digital Collection Portal) regardless of packaging
- Era machinery: AI image-description assistance, phone-camera capture, cloud hosting, mobile/web everywhere-access

### L3 — Vendor-specific (kept here, not in the final document)

- TMS Collections: 11-module composition; Registration menu with Rights and Reproduction screen; Audit Manager as a separate product; TMS Conservation Studio / TMS Media Studio companion products; concurrent-user licensing; eMuseum Network cross-organization retrieval; 120-format image viewer; OCR indexing of linked documents
- MuseumPlus: named Core Functions (Customer Service register, Digital Assets, Contracts, Exhibition Management); Curator 3D planning add-on; MuseumPlus Scan; eMuseumPlus
- CatalogIt: Entry/Folder/Profile terminology; Owner/Admin/Read-Write/Editor permission names; Strict Accessioning default with pattern tokens (per accession pass); plan structure (Museum/Personal/Organization/Conservator) and entry-count tiers; HUB publishing
- CollectiveAccess: Providence/Pawtucket component split; 2003 origin; GPLv3

## Vendor-specific vs Type Findings (explicit)

- The **Spectrum procedure list** is the domain's normative statement of the Type's workflow family — but a specific product's compliance with all 17 procedures is vendor posture (TMS documents it; others itemize differently). The Type claim is the structure (register + custody + event layer), not the full procedure checklist.
- **Location-history audit trail** is stated by one product at that depth (TMS directory entry); location tracking itself is cross-product (Spectrum primary procedure + CatalogIt explicit). Location tracking → Type-level; dedicated location-history audit trail machinery → common, single-product-verified at that depth.
- **Deed-of-gift form generation** and **strict numbering enforcement** are CatalogIt-verified machinery (accession pass) → standard capabilities, not invariants.
- **Anonymous donor/lender access control** is TMS-documented → common practice expected of incumbents, recorded as product-specific evidence for confidentiality behavior; the underlying rule (sensitive custodial data is access-controlled) is treated as common, not definitional.
- Suite companions (Conservation Studio, Media Studio, Curator, eMuseum, HUB) are packaging, not Type findings.

## Rejected Findings

- "Collections management = cataloging software" — REJECTED: cataloguing is one procedure family; the distinguishing structure is custody accountability and the lifecycle event layer (Spectrum's own primary-procedure set; every sampled product's module family).
- "A CMS is defined by its exhibition/loan/conservation modules" — REJECTED: those are the sibling workflow slices hosted in the container; the container's invariant is the record+custody+event structure they attach to.
- "Public web publishing belongs to this Type" — REJECTED: publishing is a separate surface (Digital Collection Portal; eMuseum/eMuseumPlus/Pawtucket/HUB are companions or built-in but controlled subsets); the market consistently splits custody software from publication software.
- "A CMS must be Spectrum-compliant" — REJECTED: Spectrum is the UK-framed standard (used internationally); CatalogIt and CollectiveAccess do not advertise Spectrum compliance while realizing the same structure; the structure is the invariant, not the standards checklist.
- "Collections management is generic asset management with museum vocabulary" — REJECTED: see Boundary Findings #7; the acquisition/documentation/mission semantics are structurally different.
- "Digital preservation / digitization is the core" — REJECTED: media and digitized surrogates are documentation classes on the record (CollectiveAccess's "digital preservation" is feature-level); the Type's subject is the physical object under custody.

## Boundary Findings

**1. vs Museum Accession / Cataloging (processed 2026-09-08) — the pre-hung joint-review flag, resolved here.** That leaf documented the record-creating workflow (accessioned intake + catalogue record + ongoing cataloguing loop) and observed it is not sold standalone — it is the core of every sampled CMS. This pass confirms from the container side: the object register leg of the CMS's L0 is exactly that leaf's object catalogue record; the intake/exit events are the CMS-level realization of its accessioned intake. Structural tests both directions hold: strip the custody/lifecycle machinery from a CMS and the record-creation system of record still stands (small-museum and collector products nearly realize this bare form; Spectrum explicitly allows paper); strip the record-creating core and the custody modules manage records that no longer exist. **Verdict: keep-both with containment framing** — the accession/cataloging leaf documents the record-creation workflow slice; this leaf documents the containing system (register + custody accountability + lifecycle events). Precedent-consistent (exhibition cluster, museum-object-movement/loan/condition siblings). No directory change made from this side; consolidation-as-one-type remains a taxonomy-owner option.

**2. vs Archaeological Collection Management (processed 2026-09-06) — variant flag, ratified here.** That pass observed the shared custody spine (object catalog, accession/deaccession, locations/movements, loans, condition, portal) with the excavation-context layer (site → context/stratum → object) plus site/project orientation as the differentiator, and flagged probable Variant-of. From this side: the sampled museum CMS realizes no excavation-context layer as first-class documentation (TMS's discipline pages include archaeology among collecting disciplines but the structure documented is the general custody spine); stripping provenience/context machinery from an archaeological system leaves exactly this Type. **Ratified: variant-of relationship** (discipline variant of Museum Collections Management), consistent with how the directory treats other discipline variants; no unilateral taxonomy change.

**3. vs Art Gallery Management (processed 2026-09-06) — ratified from this side.** The gallery leaf's boundary is the commercial disposition loop (stock whose terminal state is a sale; consignment settlement; Veevart/Artfundi repositioning as market evidence). From this side: the sampled CMS family realizes custody with a governed exit (deaccessioning under policy) and no sale loop as the terminus; commercial sale machinery is absent from the structure. Boundary holds; distinct Types.

**4. vs Cultural Heritage Asset Management (processed 2026-09-07).** Place-based heritage inventories (monuments/buildings/sites) hold records, not objects: no custody chain, no per-object location updates, no loans. MIDAS Heritage explicitly excludes recording museum collections (that pass's evidence). The test from this side: "which shelf/tray is this object in" → collections management; "what is this place and its status" → heritage inventory. Clean.

**5. vs Digital Collection Portal (processed 2026-09-07).** Complementarity confirmed from the container side: records created and governed here; the portal publishes a controlled subset for public discovery. The CMS family itself sells publishing companions (eMuseum, eMuseumPlus, HUB, Pawtucket) — packaging shape varies, the boundary does not. Clean.

**6. vs the workflow siblings hosted in the container (Museum Object Movement Management, Museum Loan Management, Museum Conservation Management, Museum Condition Reporting — unprocessed; Exhibition Planning / Installation / Logistics — processed).** All are custody-lifecycle event families of this Type's leg 3, sold as modules of the same systems (TMS modules, MuseumPlus modules, CatalogIt profiles/plans) and already documented as such by their own passes where processed. This leaf owns the container: the object record as hub, the location picture, and the event layer as a whole. Each sibling owns its workflow's internal structure. Consistent with the exhibition cluster's containment precedent.

**7. vs Enterprise Asset Registry / generic asset inventory (§10).** An asset registry tracks what the organization owns and where it is. The collection system adds: recorded acquisition events with source and method-of-acquisition semantics, formal intake under a collecting policy, permanent-custody commitment, provenance/scholarship as record content, governed exit (deaccession), and mission semantics (objects are unique, irreplaceable, held for preservation and interpretation — not consumable or replaceable operating assets). Remove the acquisition/documentation/deaccession semantics → asset registry. Distinct.

**8. vs Media Asset Management (§27, processed 2026-09-08).** MAM's unit of record is a media asset (master files + derivatives) moving through ingest→archive→delivery. The CMS's unit is a physical object under custody, with media as one documentation class attached to it (TMS's integrated DAMS and Media module are the module-level evidence that the market itself keeps the two distinguishable). When the "objects" are only digital files, MAM territory; when physical objects with media attached, CMS.

**9. vs Integrated Library System (§23) and Archives Management System (§23).** Library: records describe works held in replaceable copies, circulation is the lifecycle, no custody accountability per copy. Archives: accessioned materials too, but organized by provenance/series hierarchy with archival descriptive standards, not per-object custody locations (and the CMS products that ship archival modules — TMS's ISAD(G)/EAD support — are hybrids serving institutions that hold both). Adjacent, distinct.

**10. vs Museum Visitor Experience Platform (§26, unprocessed).** Audience-facing interpretation/wayfinding vs staff-facing custody of record. Expected clean; noted for that leaf's pass.

## Historical / Market-Sample Check

Paper-era form of the same institution: the accession register (bound ledger) + catalogue cards per object (leg 1); the location register / location cards kept current as objects moved, with a movement/outward-loan book recording departures and returns (leg 2); the object-entry forms, deed-of-gift files, loan files, condition report cards, conservation treatment files, insurance/valuation schedules, and deaccession files, all filed against the object number (leg 3). Spectrum itself states it "is not software (and can be used with paper-based systems)" and its Location-and-movement-control procedure is written procedure-first, medium-agnostic. The definition therefore names no software surface, no cloud, no barcode, no standards list — older, regional, paper-based, and platform-native realizations all fit. Modern machinery (SaaS, AI assistance, integrated DAM, publishing companions) is era layering, held outside the core.

## Uncertainties

- Screen-level operational detail for TMS Collections and MuseumPlus is login-gated; their observations rest on the Collections Trust directory entry (TMS) and the product page (MuseumPlus). No screen-level claims are made for them.
- CollectiveAccess operational workflow (how its movement/location machinery behaves) unverified — doc hosts unreachable beyond the landing page; positioning-level evidence only.
- Axiell Collections, PastPerfect, Vernon CMS, Lucidea Argus unreachable (consistent with sibling passes) — the small-museum desktop-heritage pole (PastPerfect) and the multi-domain enterprise pole (Axiell) are unverified this pass; the four-pole sample is taken as sufficient per stop conditions (new poles would repeat the documented structure), but their absence is recorded.
- The prevalence of barcode/RFID inventory tooling is asserted only as current-era common machinery (from directory-entry mentions of location tools and general market knowledge), not measured across the sample.
- Whether any market product positions itself as a standalone "location & movement" or "loan" tool outside a CMS could not be exhaustively excluded; nothing was found in the reachable sample (consistent with the exhibition-cluster and accession passes' observations).
- The L0's leg-2 phrasing ("updated whenever the object moves") is calibrated to Spectrum's normative wording; real-world deployments vary in how promptly locations are updated — the invariant is the maintained location picture, not any enforced real-time currency.

## Final Synthesis

Museum Collections Management is the museum's **collection system of record**: a persistent register of individually identified object records (the authoritative account of what the institution holds), each carrying its current physical location within the institution's place structure so the institution remains demonstrably accountable for objects in its care, together with the custody-lifecycle event layer — intake, movement, use, care, value, exit — recorded on the object record as an auditable custody history. The domain standard (Spectrum) defines collections management as exactly this procedure family and explicitly allows paper; every sampled product (enterprise incumbent, European incumbent, SMB cloud, open-source) realizes the same three-part structure with different packaging depth. The record-creating workflow (accession + cataloguing) is this system's core slice and its own documented leaf; movement, loans, conservation, condition, and exhibitions are its workflow siblings; public publishing is a separate Type; commercial disposition (sale) belongs to the gallery neighbor, not here. The Type stands as the containing system of the museum-cluster; keep-both-with-containment is ratified for the accession sibling and variant status for the archaeological sibling.
