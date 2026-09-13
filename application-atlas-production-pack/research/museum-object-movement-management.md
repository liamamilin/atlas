# Research Notes — Museum Object Movement Management

Research date: 2026-09-08
Leaf: Museum Object Movement Management (§27 Media, Entertainment, Creator & Culture — museum/cultural-heritage cluster)
Slug: museum-object-movement-management

## Research Goal

Understand what "Museum Object Movement Management" actually is in the real market and in the domain's own standard: what the location system is, what a movement record contains, how the current location stays trustworthy, who authorises and performs moves, and where the boundary sits against the six already-processed §27 siblings that pre-hung counterparty guidance on this leaf:

1. **museum-collections-management** (container, processed 2026-09-08): hosts this leaf as one custody-lifecycle event family; its L0 leg 2 ("object-level custody accountability … current physical location … location history retained") is the slice this leaf must own the internals of.
2. **museum-condition-reporting** (processed 2026-09-08): "Movement owns the location picture and move transactions; condition owns the state assessment. Spectrum's own procedure cross-reference: 'If you need to move objects to check them, go to Location and movement control.'"
3. **museum-loan-management** (processed 2026-09-08): forward flag — "the loan is the legal agreement authorizing and bounding the object's absence, movement records track the physical relocation; CollectiveAccess models them as separate record types (ca_loans vs ca_movements) … expected clean seam."
4. **museum-conservation-management** (processed 2026-09-08): "objects move to/from conservation through location and movement control (and object exit for external conservators); conservation records the work, not the location."
5. **Exhibition cluster** (planning / installation / logistics, all processed 2026-09-06/07): all three documented this leaf as "internal location tracking and movement control for any reason," with themselves being movement/state organized by a display occasion.
6. **archaeological-collection-management** (processed 2026-09-06): "movement/location tracking is one machinery within the custody core."

Also to be defined against generic structural neighbors (Enterprise Asset Registry, WMS, Evidence Management System) and the Inventory procedure distinction.

## Initial Boundary

Hypothesis before research: this leaf is the museum's **location-and-movement machinery** — the domain standard's "Location and movement control" primary procedure (Spectrum 5.1). Its center is two structures held jointly: a maintained per-object location picture over a defined location system, and the attributed movement transaction that keeps the picture current. Confusion risks:

- Museum Collections Management (the container — owns the object register and the whole event layer)
- Museum Loan Management (the legal agreement layer vs the physical relocation records)
- Museum Condition Reporting (state assessment triggered by moves, vs the moves themselves)
- Museum Conservation Management (the treatment work vs the custody transfers around it)
- Exhibition Planning / Installation / Artwork Exhibition Logistics (movement organized by a display occasion)
- Inventory (periodic verification of the picture vs the ongoing move transactions)
- Enterprise Asset Registry / WMS / Evidence Management (same machinery shape, different object worlds)

## Research Questions

1. What exactly does the domain standard require of location and movement control (minimum requirements, procedural steps)?
2. What is a "location" in real systems — flat labels or a designed hierarchy with its own records?
3. What does a movement record contain (attribution, authorisation, reason, custody handover, dates)?
4. How is the current location kept current — and what is the relationship between movement records and the current-location field?
5. What verification machinery exists (inventory, unlocated-object follow-up)?
6. How do off-site moves (loans, external conservation, transit) appear in the location picture?
7. How do the sampled poles (enterprise incumbent, European incumbent, SMB cloud, small-institution cloud, open-source) realize the same structure?
8. Does the paper-era museum satisfy the definition (historical check)?
9. Joint-review resolutions: adopt/discharge the seams pre-hung by the six sibling passes.

## Representative Products

Selected for market representation, documentation reachability, different product philosophy, and different customer tier (consistent with the four-pole samples of the sibling museum passes; eHive added as a reachable small-institution cloud pole that prior passes could not reach):

| Product | Vendor | Pole | Evidence level reached |
|---|---|---|---|
| TMS Collections | Gallery Systems | enterprise museum incumbent (800+ clients, 23 countries; Spectrum 5 compliant) | Collections Trust software-directory entry (detailed operational description) |
| MuseumPlus | Zetcom | European museum incumbent (900+ museums; SaaS or in-house) | product page (module/function level only) |
| CatalogIt | It Unlimited, Inc. | SMB / cloud-native (museums, historic houses, collectors) | Tier-1 help center (operational article) + product pages |
| eHive | Vernon Systems | small-institution cloud CMS | Tier-1 help center (field-level documentation) |
| CollectiveAccess (Providence) | Whirl-i-Gig | open-source, self-hosted | official manual (data-model level) |

Backbone standard consulted: **Spectrum 5.1** (Collections Trust) — the UK museum collections-management standard used internationally; "Location and movement control" is one of its nine primary procedures. Not a product; used as the domain's normative definition of the workflow.

Not usable (consistent with sibling passes): Axiell Collections (404/unreachable), PastPerfect (403 in two prior passes — not retried per network rules), Lucidea Argus (403), Vernon desktop CMS (unreachable). Gallery Systems and Zetcom deep help centers are login-gated. No screen-level claims are made for products beyond what the reachable pages state.

## Sources

- Collections Trust — Spectrum 5.1 "Location and movement control" primary-procedure hub page (scope statement): https://collectionstrust.org.uk/spectrum/primary-procedures/location-and-movement-control-spectrum-5-0-primary-procedures/
- Collections Trust — Location and movement control: the Spectrum standard (policy questions + minimum requirements, fetched in full): https://collectionstrust.org.uk/resource/location-and-movement-control-the-spectrum-standard/
- Collections Trust — Location and movement control: suggested procedure (full procedural text incl. movement-record field list, movement tickets, barcode/RFID note): https://collectionstrust.org.uk/resource/location-and-movement-control-suggested-procedure/
- Collections Trust — software directory entry "TMS Collections and eMuseum" (location-history audit trail, Spectrum procedure list, audit machinery): https://collectionstrust.org.uk/software/tms/
- Zetcom — MuseumPlus product page (core functions, Exhibition Management "input and output protocols", additional modules, product family incl. MuseumPlus Scan): https://www.zetcom.com/en/museumplus-en/
- CatalogIt — help center, "Conducting an Inventory Project" (operational: structured search by location, folder/tag workflow for unlocated objects, current and previous locations on the Entry): https://catalogit.helpjuice.com/en_US/museum-practices/conducting-an-inventory-project
- CatalogIt — product page (entries track "value, location, and condition … in real time"; Museum plan "Accession, exhibition, loan, and location documentation"): https://www.catalogit.app/
- eHive — help center: Core fields for object records ("Current location" as a core field for all catalogue types): https://help.ehive.com/core-fields.htm
- eHive — help center: Current location field (field semantics, searchability): https://help.ehive.com/field-help/object/location.htm
- eHive — help center: Location fields (location history sets; current location calculated from location history): https://help.ehive.com/location-fields.htm
- CollectiveAccess — official manual, Primary Tables and Intrinsic Fields (ca_storage_locations, ca_objects Home location, ca_loans, ca_movements with editors-disable switches): https://manual.collectiveaccess.org/ (fetched via https://raw.githubusercontent.com/collectiveaccess/CollectiveAccessManual/main/providence/user/dataModelling/primaryTables.md)
- CollectiveAccess — official manual, Location in a Hierarchy Bundle: https://raw.githubusercontent.com/collectiveaccess/CollectiveAccessManual/main/providence/user/editing/loc_hierarchy_bundle.md

Source-access limitations: TMS Collections and MuseumPlus operational help are login-gated (consistent with all sibling passes) — TMS evidence rests on the Collections Trust directory entry, MuseumPlus on its product page; no screen-level claims for either. eHive's help center is field-level only (no workflow screens). CollectiveAccess evidence is data-model level (the manual documents tables and intrinsics, not step-by-step movement procedure). CatalogIt's location machinery was reached through the inventory-project article and product pages; dedicated location-hierarchy help articles were not individually fetched. Consequently, workflow-shape claims are anchored on Spectrum (full text) plus CatalogIt/eHive operational help; TMS/MuseumPlus/CollectiveAccess observations are directory/module/data-model level.

## Product / Standard Observations

### Spectrum 5.1 "Location and movement control" (Collections Trust) — domain standard [Evidence A for the standard's own content]

- Primary procedure scope: "Keeping a record of where all the objects in your care can be found, and updating the location each time an object is moved." And: "As well as recording when objects move in and out of your museum you should also keep track of them within the museum too. Following this procedure promptly keeps your location records up to date, which is the key to being accountable for collections in your care."
- **Minimum requirements** (the standard, quoted/condensed):
  1. "You have a system of recording all locations where objects are displayed or stored within your museum" — pinpoint the specific location of an object quickly; note locations not suitable for certain kinds of objects.
  2. Records needed to monitor whether agreed environmental standards are being met (per location).
  3. "You record every movement of an object, including the date moved, and change the location record in line with your policy" — "You know at all times where every object is."
  4. "You can access location information by object number and location name" — know what is in each exhibition space and store, and where every object is.
  5. "You record who has moved objects (and who authorised those moves if required)" — "Named individuals are accountable for moving objects. Objects are not moved without authorisation."
  6. "You have as full a history of objects' previous locations as practical" — compile a list of all objects in a location at a particular time, "which might later be needed for security or conservation reasons."
  7. Risk assessment for moves (objects and people), written mitigation plan where needed.
  8. Insurance or indemnity in place before transporting, particularly borrowed objects.
- **Policy questions** the standard requires the museum to answer: how location records are kept up to date and audited; "are there times when objects may be moved temporarily without updating their location records?"; "how will you keep location and movement records appropriately secure and confidential?"; "how will you ensure that objects are not moved into unsuitable locations?"; who can view/edit records; "who can request and approve the movement of objects around your museum?"; who can move them; restrictions on when objects may be moved; own transport vs external specialists; when a courier accompanies objects; care standards in transit; who pays transport costs.
- **Suggested procedure — locations side**: give each display and storage location a unique name or number; per-location record: location type, address (if separate site), environmental condition note + date, security note, access note; maintain the location system (new locations, closed stores/displays); optionally record environmental measurements (temperature/RH) per location with measurement dates.
- **Suggested procedure — object location side**: for each object record: object number + Current location (a location reference) + Location date (when first at that location) + optional Normal location ("not all museums assign their objects a normal location"). "There should usually be only one place in your documentation system to record an object's location, as this ensures consistency and accuracy."
- **Suggested procedure — moving**: "Object moves usually happen during the course of following another Spectrum procedure." Steps: obtain and record authorisation for all moves internal or external (Movement reference number, Movement authoriser, Movement authorisation date; "in smaller organisations, the person moving an object may be the same as the person authorising the move") → check the objects' condition to ensure fitness to move ("Go to, and return from, Condition checking and technical assessment") → check catalogue records for hazards, handling/packing/display/security/storage recommendations → assess route/access/handling risks → arrange conservation or packing needed ("Go to, and return from, Collections care and conservation") → if transport involved: establish means (policies, size/weight, cost, legal restrictions, routes, insurance/lenders' requirements, courier), circulate a briefing note, arrange insurance/indemnity, prepare accompanying documentation (receipts, customs, unpacking instructions), transport and confirm safe arrival (delivery receipt + condition report; a sent museum courier inspects on arrival) → **update movement and object location records**.
- **The movement record's fields** (standard's list): movement reference number; removal date; Movement contact (person carrying out the move); signature of person accepting custody; Movement reason (standard term source); Movement note; Planned removal date (when the object will return to its normal location); shipping fields (Organisation courier; Shipper + address + Shipper's contact; Shipping note with transit requirements). Plus location bookkeeping: Previous location with begin/end dates; new Current location + Location date + Normal location.
- **Movement paperwork**: the record "may be recorded on a separate movement recording form. If so, the information should be transferred as soon as possible to the master location record."
- **Guidance notes**: location records live in entry records (first location on intake), the catalogue record ("usually contained within a digital collections management system … usually the record of an object's more permanent location", following conventions like "Room X, shelf Y, box Z"), and temporary location lists. **Pre-printed triplicate object movement tickets** (Collections Trust sells them): top copy (white) left in place of the object; middle copy (yellow) placed in a temporary locations file in object-number order from where it updates the catalogue record; bottom copy (card) tied to the object; all parts destroyed when the object returns to its permanent location. "Movement may also be managed by systems that are semi-automatic such as barcodes or RFID … These will produce their own digital records."

### TMS Collections (Gallery Systems) — enterprise incumbent [Evidence A for directory entry]

- "A complete location history audit trail is maintained for each object and component of an object." (per-object AND per-component location history)
- Spectrum procedures supported (directory entry, verbatim list): **Location and movement control (primary)** and **Inventory (primary)** among the supported set; "Spectrum 5 compliant."
- Built-in audit trail capturing date, login ID, table, column, old value, new value, with user-entered explanations/approvals — the general record-change machinery the location history sits beside.
- Roles served (product page, via sibling pass): Registrars, Collections Managers, Museum Conservators, Curators, Digital Asset Managers, Collections Database Managers.
- No screen-level location/movement workflow detail is publicly reachable (help community login-gated).

### MuseumPlus (Zetcom) — European incumbent [Evidence A for product page; positioning only]

- "Comprehensive, flexible standard application provides real-time museum management and fully documents any type of collection and all related workflow."
- Core functions itemized: cataloging/registration/management of all objects; Customer Service register; Digital Assets; Contracts; **Exhibition Management ("coordination of participants, venues and lenders, as well as input and output protocols")** — the in/out protocol framing is the movement-adjacent surface visible at product-page level.
- Additional modules "such as event management, archiving, etc. can be seamlessly integrated"; a **MuseumPlus Scan** companion product exists in the product family (barcode-scanning positioning; its function not directly observed).
- No location-management module is itemized on the reachable page — location machinery unverified beyond "all related workflow" (limitation recorded).

### CatalogIt (It Unlimited) — SMB / cloud-native pole [Evidence A; Tier-1 help center + product pages]

- Entries track "value, location, and condition — adding to their stories in real time" (product page); Museum plan: "Accession, exhibition, loan, and location documentation."
- **Inventory Project article** (operational workflow): create an Inventory Project Profile (name, dates, staff/volunteers, goals, attached documentation) → generate an inventory list via Structured Search ("locate all records within a specific collection **or location**") → organize work in Folders ("Records to be Inventoried / Inventory Complete / Records Requiring Follow-Up / **Unlocated Objects**") → tag issues ("Needs Conservation / Needs Photography / **Location Review Required** / **Unlocated**") → associate objects with the project (per-entry or bulk) → update records during the inventory, including "**Verifying locations**" → **Track Unlocated Objects**: "Review information such as: **Current and previous locations**; Exhibition history; Loan history; Related documentation. Objects that require additional investigation can be placed in a dedicated Folder and tagged for follow-up. Documenting search efforts within the Entry record helps maintain a clear record of inventory findings."
- The Entry (object record) carries current **and previous** locations; exhibition history and loan history sit beside them on the same record (the container's event layer).

### eHive (Vernon Systems) — small-institution cloud pole [Evidence A; Tier-1 help center, field level]

- "**Current location**" is a **core field for all catalogue types** (every object record): "records where the object is right now"; a private pick-list field; searchable by location value (e.g. `loc: "bay 4/shelf 1"` → all objects in Bay 4/Shelf 1) — the location-name query direction.
- **Location fields page**: a **Location history** section holds repeating sets (location, location-history date, location-history notes) — "You can add multiple locations by selecting 'Add another set'. This allows you to store details about **location changes over time**," reorderable chronologically. The **current location can be entered manually or "calculated from the data in the location history fields"**: "When you update the location history fields, eHive will ask if you want to update the current location." Plus General location notes and a Place mark field (history records only).
- Field-level help only; no workflow-screen documentation (limitation recorded).

### CollectiveAccess / Providence — open-source pole [Evidence A; official manual, data-model level]

- **ca_storage_locations**: "Storage location records represent physical locations where objects may be located, displayed or stored. Like place records, storage locations are **hierarchical** and may be nested to allow notation location at various levels of specificity (**building, room, cabinet, drawer, etc.**). As with the other primary tables, each storage location may have arbitrarily rich cataloguing, including access restrictions…"; an **Is enabled?** flag marks a storage location available for use or not.
- **ca_objects** carries a **Home location** intrinsic ("formatted … evaluated relative to the home ca_storage_locations record. If no template is defined … the full hierarchical path of the home location is returned") — the normal-location concept at data-model level.
- **ca_movements**: "For more complex location tracking needs, **movement records** can be used to record in precise detail movement of objects between storage locations, **while on loan or while on exhibition**. Used as part of a location tracking or use history policy, movements can provide a **robust record of every movement event in an object's history**." Movement types are a configurable list; movements relate to objects (and other records) via the general relationship machinery.
- Notably, the movement editor ships **disabled by default** (`ca_movements_disable = 1` in app.conf; storage locations and loans ship enabled) — the minimal install locates objects via storage locations and the Home location; movement records are switched on "for more complex location tracking needs." Movement is a deliberate, optional layer over the location picture, not the picture itself.
- Places (a separate table) support floorplan images "used as the base layer in the object-place floorplan user interface" — spatial visualization machinery exists at model level.

## Cross-product Comparison

| Dimension | Spectrum (standard) | TMS Collections | MuseumPlus | CatalogIt | eHive | CollectiveAccess |
|---|---|---|---|---|---|---|
| Location system | system of all display/storage locations, each uniquely named/numbered with its own record (type, address, environment, security, access) | implied by location-history audit trail (module level) | not itemized on reachable page | locations are searchable attributes; structured search "within a specific … location" | current location is a pick-list; location values like "bay 4/shelf 1" imply shelf-level addressing | **hierarchical storage-location records** (building→room→cabinet→drawer) with rich per-location cataloguing and an enabled flag |
| Current location per object | Current location + Location date + optional Normal location; "only one place … to record an object's location" | maintained (audit-trail level) | "all related workflow" (positioning) | Entry carries current + previous locations | **core field on every object record**, searchable by location | Home location intrinsic referencing the home storage location |
| Movement record | full standard field list (ref no., date, mover, custody signature, reason, note, planned return, shipping fields) | location history audit trail per object **and component** | not itemized | movement implied through location changes + project/folder tracking; not a documented standalone record type | **location history sets** (location, date, notes), chronologically ordered | **dedicated ca_movements record type** ("every movement event in an object's history"; also used "while on loan or while on exhibition") |
| Current-location update mechanism | record every movement "as soon as possible"; change the location record per policy | audit trail maintained automatically | not observed | location updates on the Entry "in real time" | current location **calculated from** location-history entries (with confirmation) | object located via storage-location relationship; movements as an optional deeper layer |
| Attribution / authorisation | who moved + who authorised (if required); "objects are not moved without authorisation" | audit trail captures login ID + explanations/approvals (general machinery) | not observed | inventory staff/volunteers named on the project profile | cataloguer/date fields on records (general) | movement records attributed via submission user; general access control |
| Verification / inventory | Inventory is a **separate procedure**; audit of location records is a policy question | Inventory procedure supported | not itemized | **Inventory Project Profile** + verify-locations step + Unlocated folder/tags | not observed at workflow level | not sampled at workflow level |
| Off-site custody in the picture | "in and out of your museum" in scope; movement record carries shipping/courier fields | not observed at screen level | Exhibition Management "input and output protocols" (module level) | loan history + exhibition history on the Entry; unlocated review includes loan history | location values are free-form enough to hold off-site states (pick-list) | movements happen "while on loan or while on exhibition" |
| History / retrospection | previous locations with begin/end dates; "list of all objects in a location at a particular time" | complete location history audit trail per object and component | not observed | previous locations on the Entry; project documentation retained | location history sets over time | movement records as the object's movement history |
| Packaging | procedure (paper-satisfiable) | module inside the CMS | inside "all related workflow" | module inside the CMS (plan-gated) | fields inside every object record | optional record type + core storage-location table |

Reading of the matrix: every pole realizes the same two-part structure — a per-object **current location** held against a **defined location system**, kept truthful by **movement records/history entries** that both update the picture and accumulate as history. Poles differ in where the machinery lives (fields vs dedicated record type vs audit trail) and in how much workflow (authorisation, verification, shipping) is formalized. No pole sells location/movement as a standalone product.

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately small)

Museum Object Movement Management is the museum's **location-and-movement machinery**: the structure that keeps the institution able to answer, at any moment, where every object in its care is. Two jointly-loaded structures:

1. **The maintained location picture.** Every object in care carries a **current location** recorded against the institution's **location system** — a set of named/numbered display and storage locations — so that both questions are answerable at any time: "where is this object?" (object → location) and "what is/was here?" (location → objects, including retrospectively). The picture extends beyond the building: an object away from the museum (on loan, at an external conservator, in transit) is still in care and still holds a location state. (Remove → descriptive cataloguing with no custody accountability: precisely the container's territory minus its leg 2, or a documentation system that cannot say where anything is.)
2. **The move transaction.** Each physical relocation is recorded as a **discrete, attributed movement event** — what object, from where to where, when, by whom, authoriser where policy requires, why — and it is this recorded event that **updates the current location** and **accumulates into the object's location history**. (Remove → a manually edited location field or periodic snapshot: no movement control, no trustworthy picture, no history.)

Jointly-held is load-bearing: 1 without 2 = a location spreadsheet/field with no control over how it becomes wrong or right; 2 without 1 = movement paperwork that never resolves into a reliable "where is it now"; both together are the domain standard's own claim — keeping location records up to date "is the key to being accountable for collections in your care."

Anchor evidence: Spectrum's minimum requirements name exactly these two legs (requirements 1/2/4 = the location picture; requirements 3/5/6 = the move transaction and its history), and every sampled product realizes both (eHive as fields + history sets with calculated current location; CollectiveAccess as storage-location records + optional movement records + Home location; TMS as a per-object-and-component location history audit trail; CatalogIt as current/previous locations on the Entry with location-scoped search and unlocated follow-up; MuseumPlus at positioning level via "all related workflow" plus Exhibition Management's input/output protocols).

### L1 — Common Mature Structure (very common, not definitional)

- The location system as a designed **hierarchy** (building → room → cabinet → drawer/shelf) with per-location records: type, address, environmental conditions/measurements, security and access notes
- **Suitability knowledge**: locations marked unsuitable for certain kinds of objects; environmental standards monitored per location
- A **normal/home location** concept (where the object lives when idle) with planned-return dates on temporary moves
- **Authorisation workflow** for moves (request → approve → execute; named authoriser; policy may let mover = authoriser in small organisations)
- **Fitness-to-move interlocks**: condition check before/after moving; handling/packing/security recommendations read from the object record before the move
- **Verification/inventory machinery**: location audits, structured search by location, unlocated-object tracking and follow-up documentation (often barcode/QR/RFID-assisted)
- **Off-site transit machinery**: transport choice, courier accompaniment, shipping agent coordination, accompanying documentation (receipts, customs, unpacking instructions), delivery receipt and arrival condition check
- **Per-component location tracking** (parts of objects located individually)
- Location contents lists/registers and reports ("what is in each store"; "what was in this room on date X")
- Custody-handover recording on the movement record (who accepted custody)
- Confidentiality controls on location and movement records (security-sensitive information)

### L2 — Variant / Optional Structure

- Packaging: fields on the object record (small-cloud pole) vs dedicated movement record types (open-source, enabled per project) vs audit-trail machinery (enterprise) vs paper procedures (standard, small museums)
- Automation level: manual entry vs barcode/RFID "semi-automatic" movement capture vs real-time tracking (current-era machinery)
- Who moves and who authorises: registrar-centric control vs all-staff movement under policy
- Depth of transit machinery: none (internal-only practice) vs courier/customs/CITES-grade international shipping
- Spatial visualization: floorplan/place-based UIs (model level in at least one sampled system)
- Scale of the location hierarchy: a handful of rooms vs shelf-level barcoded addressing
- Whether movement records also serve use-history purposes (loan/exhibition stay-tracking) or stay purely physical

### L3 — Vendor-specific (kept here, not in the final document)

- Spectrum: pre-printed triplicate movement tickets (white copy left in place of the object, yellow in the temporary locations file, card tied to the object; destroyed on return); movement-ticket stationery as a product of the standard's publisher
- CollectiveAccess: `ca_movements_disable = 1` default (movement editor off until enabled); Home location display template (`home_location_display_template`); storage-location icon/color/enabled flags; object-place floorplan UI
- eHive: current location as a 200-character private pick-list; the "eHive will ask if you want to update the current location" confirmation flow; Place mark field on history records
- TMS Collections: per-component location history depth; Audit Manager as a separate configurable-audit product; concurrent-user licensing
- CatalogIt: Inventory Project Profile record type; Unlocated Objects / Location Review Required folder-and-tag convention; plan-gated location documentation
- MuseumPlus: MuseumPlus Scan companion; Exhibition Management "input and output protocols" phrasing

## Vendor-specific vs Type Findings (explicit)

- **The two-leg structure (location picture + move transaction) is Type-level**: it holds in the standard (minimum requirements 1–6), at field level (eHive), at data-model level (CollectiveAccess), at audit-trail level (TMS), and at workflow level (CatalogIt). Not vendor-specific.
- **Dedicated movement record types** are one packaging of the move transaction (CollectiveAccess; TMS's audit trail is another; eHive's history sets a third) — the structure is Type-level, the record-type packaging is product-specific.
- **Authorisation workflow** is standard-level ("objects are not moved without authorisation … if required") but its depth (separate request/approve states) is not screen-verified in any sampled product → held as common practice, not definitional; the invariant is **attribution** (who moved, who authorised where required).
- **Per-component location history** is TMS-verified at that depth (single product) → common-expected for enterprise, recorded as single-product evidence.
- **Normal/home location** is standard-optional ("not all museums assign their objects a normal location") → common, not invariant.
- **Inventory/verification machinery** is a separate Spectrum procedure; products host it beside movement (CatalogIt's inventory projects; TMS's Inventory procedure support) → the verification workflow is standard capability of the container/workflow family, not this leaf's invariant; its seam is recorded below.
- **Barcode/RFID capture** is standard-endorsed ("semi-automatic … will produce their own digital records") but era machinery → optional, not definitional.

## Rejected Findings

- "Movement management = generic asset tracking with museum vocabulary" — REJECTED: the object world differs structurally (unique, irreplaceable objects under public-trust custody; object-number binding to documentation; per-location environmental suitability; fitness-to-move condition interlocks; retrospective "what was here at date X" as a security/conservation instrument; movement as documentation of record rather than logistics optimization).
- "This Type is about transporting art" — REJECTED: transport is an optional sub-part of external moves (the standard routes it through means-selection, insurance, couriers) but the defining center is the location picture and the move transaction; carriage execution without a custody picture is a different territory (adjacent to the artwork-exhibition-logistics / art-shipping space).
- "Movement control = Inventory" — REJECTED: Spectrum keeps them as two procedures. Movement records relocations as they happen and keeps the picture current; inventory periodically verifies the picture against reality (and handles the unlocated). Products host both, but the structures are distinct (transaction vs verification).
- "Movement control requires a collections management system" — REJECTED: Spectrum is explicitly medium-agnostic and paper-satisfiable (triplicate tickets, temporary locations files); the workflow predates software and defines it, not the reverse.
- "Movement records are just a field on the object record" — REJECTED as a definition: the minimal realization is field-shaped (eHive's current-location core field), but the discipline includes the attributed event record and the accumulated history; eHive's own design (current location calculated from history entries) shows the field is the picture and the history is the machinery. A single mutable field with no event record fails the move-transaction leg.
- "Off-site movement is the loan sibling's territory" — REJECTED: the standard puts "in and out of your museum" inside this procedure; movements occur for many reasons (loans, external conservation, photography, storage reorganization, object exit), and the movement record carries shipping/courier fields regardless of reason. The loan owns the agreement; the movement owns the physical relocation.

## Boundary Findings

**1. vs Museum Collections Management (§27 container, processed 2026-09-08) — the containment relationship, ratified from this side.** The container's L0 leg 2 ("object-level custody accountability: current physical location … updated whenever the object moves, with location history retained") is exactly this leaf's slice; the container defers "the workflow's internal structure" to the siblings. This pass documents those internals: the location system's design, the move transaction's anatomy, the update mechanism, the verification loop. Removal tests: strip the location/movement machinery from a CMS → the register and the other event families stand (the container loses its custody accountability leg); strip the object records → movement machinery has nothing to locate (the container's leg 1 is presupposed). Spectrum confirms the split from the standard side: Location and movement control is one primary procedure among the family a CMS implements. **Verdict: keep-both with containment framing, consistent with the accession/cataloging, exhibition-cluster, loan, condition, and conservation precedents. No directory change made from this side.**

**2. vs Museum Loan Management (§27 sibling, processed 2026-09-08) — the forward flag, DISCHARGED as expected-clean.** The loan record is the legal agreement authorizing and bounding an object's absence (terms, insurance, care standards, return obligation); movement records carry out and account for the physical relocation. The loan pass's evidence holds from this side: CollectiveAccess ships ca_loans and ca_movements as separate record types (and the ca_movements documentation itself says movements happen "while on loan or while on exhibition" — the movement layer records custody reality during loan states, not the agreement); Spectrum keeps Loans in/out and Location and movement control as separate procedures, with the movement procedure routing transport/insurance steps for moves that loans prompt. Removal tests: remove loan records → objects still move for other reasons and still need location control; remove movement records → a loaned object's whereabouts during the loan would be untracked while the agreement stands. **Verdict: distinct sibling Types; clean seam.**

**3. vs Museum Condition Reporting (§27 sibling, processed 2026-09-08) — the condition pass's guidance, ADOPTED.** Movement owns the location picture and move transactions; condition owns the physical-state assessment. The interlock is documented at the standard level in both directions: the movement procedure routes "check the objects' condition to make sure they are fit to be moved" to Condition checking (before the move) and gets an arrival condition report back (after transit); the condition pass records Spectrum's own cross-reference ("If you need to move objects to check them, go to Location and movement control"). Removal tests hold both ways. **Verdict: distinct; movement prompts and consumes condition documentation but records no state assessments.**

**4. vs Museum Conservation Management (§27 sibling, processed 2026-09-08) — ratified from this side.** Objects move to and from conservation through location and movement control (including custody transfer to external conservators — the movement procedure's off-site custody states); conservation records the proposed/performed work, not the location. Spectrum routes "arrange any conservation or packing needed to make the objects safe for the move" through Collections care and conservation. **Verdict: distinct; clean seam as pre-agreed.**

**5. vs the exhibition cluster (Exhibition Planning Platform / Exhibition Installation Management / Artwork Exhibition Logistics, all processed 2026-09-06/07) — the occasion discriminator holds.** All three passes documented this leaf as "internal location tracking and movement control for any reason (storage ↔ gallery ↔ conservation)." Confirmed from this side: the Spectrum procedure is reason-neutral ("object moves usually happen during the course of following another Spectrum procedure" — loans, exhibitions, condition checks, conservation, inventory, exit). The exhibition siblings organize movement by a display occasion (external venues, install state, transport chain, cross-party handover); this leaf owns the everyday machinery those workflows call when anything moves anywhere. Removal tests: remove the display occasion → the location picture and movement records remain (everyday reshuffles, storage moves, conservation transfers); remove the location/movement machinery → exhibition logistics has no custody picture to build its chains on. **Verdict: distinct siblings; the movement leaf is the general machinery, the exhibition leaves are occasion-bound workflows over it.**

**6. vs Inventory (a Spectrum procedure, not a directory leaf — recorded as a seam, not a Type boundary).** Spectrum separates Location and movement control from Inventory: the former records relocations and keeps the picture current; the latter periodically verifies that objects are where the records say (and surfaces the unlocated). Products host both (TMS supports both procedures; CatalogIt's inventory projects verify locations and chase the unlocated). This leaf documents the transaction machinery; verification is treated as standard capability of the container/workflow family that consumes and repairs the picture. **No directory change; recorded to prevent future leaf duplication.**

**7. vs Enterprise Asset Registry / Warehouse Management System (§10 structural neighbors).** Same machinery shape (locations, moves, attribution) but a different object world and purpose: asset registries track replaceable operating assets; WMS optimizes throughput of stock in a fulfillment operation. Movement management serves custody accountability of unique, irreplaceable objects: per-location environmental suitability, fitness-to-move condition gating, retrospective location inventories "needed for security or conservation reasons," and movement as documentation of record. Remove the custody/documentation semantics → asset tracking. **Verdict: distinct Types.**

**8. vs Evidence Management System (§24, structural cousin, noted for that pass's context).** Police evidence management shares the chain-of-custody shape (unique items, location control, attributed transfers, authorization). The museum version differs in object world (collection objects under public-trust custody), in its documentation interlocks (condition/conservation), and in the location system's environmental/suitability semantics. **Family resemblance recorded; distinct Types.**

**9. vs Museum Visitor Experience Platform (§26, unprocessed).** Audience-facing interpretation/wayfinding vs staff-facing custody machinery. Expected clean; noted for that leaf's pass.

**10. Packaging reality.** In the reachable sample, **no standalone dedicated "object movement / location control" product exists**: the structure ships as fields and modules inside museum collection systems (eHive's core location fields + history sets; CollectiveAccess's storage-location table + optional movement records; TMS's location history audit trail; CatalogIt's location documentation + inventory projects; MuseumPlus inside "all related workflow") and as a procedure in the standard (paper-satisfiable). Consistent with the loan pass and the container pass's observations. Candidate outcome for joint review: keep-as-workflow-Type-with-containment (this pass's framing, consistent with how the directory already treats the Museum Loan/Movement/Condition/Conservation sibling set) vs fold the museum custody-workflow siblings into a single Type at a taxonomy pass.

## Historical / Market-Sample Check

Paper-era form of the same machinery: a location register or location cards kept current as objects moved (the catalogue record holding the permanent location, "Room X, shelf Y, box Z" conventions); the triplicate **object movement ticket** — white copy left in place of the object, yellow copy filed in a temporary locations file in object-number order to update the master record, card copy tied to the object, all destroyed on return; previous-location entries with dates; the temporary locations file itself. Every element of the L0 is satisfied without software: the maintained picture (register/cards), the move transaction (the attributed ticket), the history (the file). Spectrum states it "is not software (and can be used with paper-based systems)," and its movement procedure is written procedure-first, medium-agnostic. The digital lineage is continuous: Spectrum's Note 1 describes barcode/RFID movement systems as the semi-automatic successor of the same ticket; eHive's "current location calculated from location history" is the ticket-into-catalogue transfer automated. The definition therefore names no software surface, no barcode, no cloud, no RFID — older, regional, paper-based, and small-museum realizations all fit. Modern machinery (audit trails, calculated fields, inventory projects, floorplan UIs, RFID) is era layering, held outside the core.

## Uncertainties

- Screen-level operational behavior for TMS Collections and MuseumPlus is login-gated (consistent with all sibling passes); their evidence is directory-entry/product-page level. No screen-level claims made for them.
- MuseumPlus's location machinery is unverified beyond "all related workflow" and the Exhibition Management module's "input and output protocols"; MuseumPlus Scan's function was not directly observed. Recorded, not asserted.
- CollectiveAccess evidence is data-model level; the day-to-day movement workflow (how a registrar records a move in the UI) is not documented in the reachable manual. The "movement editor disabled by default" observation is from the manual's app.conf switches.
- eHive's help center is field-level; no workflow-screen documentation of authorisation or movement forms. The location-history → current-location calculation flow is documented and quoted.
- No standalone dedicated location/movement product was found in the reachable sample; absence cannot be exhaustively excluded (consistent with the loan pass's uncertainty). Nothing beyond CMS modules and the paper procedure was found.
- The prevalence of barcode/RFID tooling is asserted only from the standard's own note plus general market knowledge, not measured across the sample.
- Whether off-site custody states ("in transit", "at conservator") are first-class location values vs free text varies by product and was not comparable at screen level for the gated products.
- CatalogIt documents movement implicitly (location changes on the Entry; inventory verification); a dedicated movement-record type was not observed. Its machinery is recorded as field/workflow level.

## Final Synthesis

Museum Object Movement Management is the museum's location-and-movement machinery: a maintained **location picture** (every object in care holds a current location against a defined system of named display and storage locations, queryable in both directions and extending to off-site custody) kept truthful by the **move transaction** (each relocation recorded as a discrete attributed event — object, from, to, date, mover, authoriser where required, reason, custody handover — which updates the current location and accumulates as the object's location history). The domain standard defines exactly this procedure ("the key to being accountable for collections in your care") and allows paper; every sampled pole realizes the structure with different packaging (fields, history sets, audit trails, or dedicated movement record types). The defining core is deliberately small: attribution and the maintained picture are invariants; authorisation workflows, hierarchy design, normal locations, verification machinery, per-component tracking, and transit depth are standard capabilities; barcodes, RFID, and floorplan UIs are era layering. The leaf stands inside the museum-collections container (owning the custody-accountability slice's internals) with clean seams to loans (agreement vs relocation), condition (state vs location), conservation (work vs movement), and the exhibition cluster (occasion-bound vs any-reason movement); inventory is a distinct verification procedure hosted beside it, and no standalone product packaging was found in the reachable sample.
