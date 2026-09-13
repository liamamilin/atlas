# Research Notes — Archaeological Collection Management

## Research Goal

Understand what "Archaeological Collection Management" software actually is as an Application Type: what objects exist inside it, who uses it, what workflows it supports, how the archaeology-specific part differs from general museum collections management, and where its boundaries run against heritage-inventory platforms and field excavation-recording systems.

## Initial Boundary

Working hypothesis at start:

- Core use: cataloging and stewardship of objects recovered from archaeological excavation — provenience/context documentation, physical custody tracking, condition, movement, access.
- Primary users: collections managers, registrars, curators, archaeologists, repository staff, conservators.
- Nearest Types: Museum Collections Management (sibling under §27), Museum Accession / Cataloging, Museum Object Movement / Loan / Conservation leaves, Cultural Heritage Asset Management, Archives Management System (§23).
- Confusion risks: (a) it may be only a discipline-variant of Museum Collections Management; (b) heritage inventory platforms (site/monument registers) are a different thing despite shared vocabulary; (c) excavation field-recording systems (not in the directory) are a different Type.

## Research Questions

1. What is the core object model? (object record, accession lot, site/context, storage location, condition, loan, deaccession)
2. How does archaeology-specific structure enter the model? (site, provenience, stratigraphic context, assemblage/lot, refitting)
3. What is the custody lifecycle? (accession → catalog → location → movement/inventory → loan/exhibit → deaccession)
4. Who uses it and in which institutions? (museums, universities, government repositories, contract archaeology)
5. What rules matter? (numbering policies, lot vs object cataloging, access visibility, roles, retention of deaccession records)
6. What separates it from Museum Collections Management, from heritage inventory platforms, and from field-recording systems?
7. Would older / regional / non-web products still fit the definition (historical check)?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, and different customer tiers:

| Product | Tier / Philosophy | Evidence quality |
|---|---|---|
| CollectiveAccess (Whirl-i-Gig, open source) | open-source, fully configurable, web-based; museums/archives/community | A — official documentation site fully public (Providence manual, primary tables) |
| Re:discovery Proficio (+ Archaeology Module) | US mid-market; multidisciplinary CMS with a dedicated archaeology catalog; strong government/state-agency clientele | A — official product pages describe module structure explicitly; no deep manual online |
| Gallery Systems TMS Collections | enterprise museum standard, international, web-based | B — official product page only (positioning, roles, modules); operational docs behind client portals |
| Axiell Collections / EMu | European enterprise, multidisciplinary (museums/archives/libraries); EMu strong in natural history | B — official product/landing pages only; help center unreachable during research |
| Arches (Getty Conservation Institute + World Monuments Fund, open source) | boundary case: heritage inventory platform, not a collections management system | A — official site fully public |

PastPerfect (US SMB museum CMS) was sampled in plan but its site/support pages returned HTTP 403 on two attempts; it was dropped as a verified sample and recorded as a sourcing limitation.

## Sources

- CollectiveAccess — https://docs.collectiveaccess.org/ (Welcome / About), https://docs.collectiveaccess.org/providence/ (Introduction to Providence), https://docs.collectiveaccess.org/providence/category/data-modelling (Data Modelling index), https://docs.collectiveaccess.org/providence/user/dataModelling/primaryTables (Primary Tables and Intrinsic Fields). Fetched 2026-09-06.
- Re:discovery Software — https://rediscoverysoftware.com/ (home), https://rediscoverysoftware.com/archaeology-module/ (Archaeology Module), https://rediscoverysoftware.com/collections-module/ (Collections Module). Fetched 2026-09-06.
- Gallery Systems — https://www.gallerysystems.com/solutions/collections-management/ (TMS Collections). Fetched 2026-09-06.
- Axiell — https://www.axiell.com/ (landing: Axiell Collections, EMu positioning). Fetched 2026-09-06.
- Arches — https://www.archesproject.org/what-is-arches/. Fetched 2026-09-06.
- PastPerfect — https://support.pastperfect.com/ and https://www.pastperfect.com/ returned 403 (two attempts each level); abandoned per network-restriction rule.

## Product Observations

### CollectiveAccess (Providence + Pawtucket)

Evidence layer: A (official documentation).

Key observations:

- Positioning: "collections management and presentation software"; relational database for "large, heterogeneous collections that have complex cataloging requirements"; two components — Providence (back-end cataloguing) and Pawtucket (public web discovery/publishing).
- Providence features (documented): fully customizable metadata fields, user interfaces, and reports; complex hierarchies (collections→items, place authorities); "management of administrative data relating to use, condition and conservation of materials"; "robust location tracking pertaining to specific materials"; standards support (DACS, PBCore, Dublin Core, VRA Core); integration with LCSH, Getty vocabularies (AAT/TGN), GeoNames; media handling (audio/video/image); web-based but runnable offline.
- Primary record types (documented table list with intrinsic fields):
  - **Objects** (ca_objects): identifier (idno) under a configurable numbering policy, type, parent (hierarchy), access (public/private for Pawtucket), cataloguing workflow status (informational), **lot_id** (accession lot grouping, object belongs to at most one lot), acquisition type, accession status ("accessioned" / "pending accession" / "non-accessioned item"), deaccession flag + deaccession type ("Sold", "Destroyed", "Transferred" as examples) + deaccession date + disposal date + notes, extent + units, **home location** derived from a storage-location record.
  - **Object Lots** (ca_object_lots): "Lots record the accession or acquisition of one or more objects… Registrarial information, such as the Deed of Gift, may be recorded in a lot record while cataloging for each accessioned object remains at the object level."
  - **Entities** (ca_entities): people/organizations related to objects via configurable relationship types (creator, donor, etc.).
  - **Places** (ca_places): hierarchical place authorities (geographic or otherwise); GeoNames/TGN integration for common place names.
  - **Occurrences** (ca_occurrences): events, exhibitions, productions, citations.
  - **Collections** (ca_collections): groupings of objects; also used for archival finding aids (DACS).
  - **Storage Locations** (ca_storage_locations): "physical locations where objects may be located, displayed or stored… hierarchical and may be nested… (building, room, cabinet, drawer, etc.)"; can be flagged enabled/unavailable.
  - **Loans** (ca_loans): incoming and outgoing loans; dates, shipping, insurance.
  - **Movements** (ca_movements): "movement records can be used to record in precise detail movement of objects between storage locations, while on loan or while on exhibition. Used as part of a location tracking or use history policy… a robust record of every movement event in an object's history." (disabled by default in app.conf — an optional machinery)
  - **Object Representations** (ca_object_representations): digital media attached to objects (images/video/audio/PDF), with rights/reproduction fields.
- Access model: every record has access (public/private for public-facing Pawtucket) and a workflow status; per-table editors can be disabled; user/group permission machinery exists (Administration section).
- Archaeology-specific structure: none hard-coded — the platform is fully configurable; provenience would be modeled via Places/place hierarchies and relationships configured per project. (Community configurations exist but were not verified — do not overclaim.)

### Re:discovery Proficio + Archaeology Module

Evidence layer: A (official product pages; feature descriptions, not a full manual).

Key observations:

- Positioning: "collections management software for art museums, archives, libraries, **archaeological collections**, historical museums…"; clients include "archaeological sites, government agencies"; 30+ years.
- Multidisciplinary catalogs in one product: "Proficio includes an Art Catalog, History Catalog, Natural History Catalog, Hierarchical Archives, Reference Library **and Archaeology**, all in one place designed to look and feel the same."
- Collections module (shared substrate, documented): accession / object / deaccession records; track "exhibits, loans, locations, conditions, and appraisal information"; "guidelines for object preservation, conservation, shipping, and restrictions"; "conduct regular inventories"; names for "artists, eminent figures, researchers, and donors"; per-user permissions ("volunteers access to only certain parts without the ability to delete records"); required-field configuration; mass updating; keyword search across all fields including attached multimedia; digital assets (images/video/audio/PDF) attachable to records; reports; Proficio for the Web (public online portal); Proficio Mobile (inventory/update on mobile); Cloud and Elements (small-institution) editions.
- **Archaeology module (explicit hierarchy, documented)**:
  - "Proficio's Archaeology Module provides a complete catalog for an active archaeological project starting with the **site**. You can individually catalog each **artifact** recovered and describe the physical **context** of each excavated **layer** within a site."
  - Documented hierarchy: "Individual Site → Master Context → Context Levels → Individual Artifacts → Objects".
  - Additional features: "Manage Many Projects", "**Cross-mend** Artifacts" (refitting joins), "Document Conservation", "Manage Exhibits", "Track Loans In or Out".
- Interpretation: the archaeology catalog is the collections-management spine (object records + custody machinery) extended upward with a site→context hierarchy that objects hang from, and sideways with project management. "Cross-mending" is a domain-specific operation (refitting fragments) implemented as a record-level feature.

### Gallery Systems TMS Collections

Evidence layer: B (official product page; no operational docs accessible).

Key observations:

- Positioning: "the world's leading collections management system for museums and institutions"; web-based; integrates with conservation documentation, online collections, digital asset management.
- Documented capabilities (marketing level): multi-language diverse collections; term searching and query filters; "catalogue and cross-reference everything, from object data to constituents"; attach finding aids to archive records; customizable dashboard and data entry forms; "integrated thesaurus for precise and consistent object descriptions"; preconfigured reports; 24/7 browser access.
- Roles section of the site: software for Registrars, Collections Managers, Museum Conservators, Curators, Digital Asset Managers, Collections Database Managers — confirms the standard collections-management role set.
- Compliance badge: "Spectrum compliant and a Spectrum Partner (Collections Trust)" — evidence that cataloging-standard compliance is a marketed property of the Type.
- No archaeology-specific structures visible on the public site; TMS serves archaeology collections in practice (university/natural-history museums) but this was not verifiable from official docs — do not claim.

### Axiell Collections / EMu

Evidence layer: B (official landing/product pages; help center timed out).

Key observations:

- Axiell Collections: "web-based collections management software"; "Manage collections data, media, locations, and movements with Axiell's multidisciplinary solution"; "Standards-based to ensure compliance, but flexible enough to meet your collection's needs"; "Robust security and permissions"; "Easy reporting"; "Open API for data sharing"; AI data enrichment; bundled DAM and digital engagement (mobile guides, online exhibitions).
- EMu: "a powerful multidisciplinary collections management system"; Axiell's museum solutions page lists Historical & Arts, Moving Image, and Natural History collections — archaeology is not broken out as its own solution page, consistent with archaeology being served inside the multidisciplinary CMS rather than as a separate product.
- Axiell Move exists as a separate product for collection moves — evidence that large-scale movement projects are a distinct adjacent tool in the enterprise market.

### Arches (boundary case)

Evidence layer: A (official site).

Key observations:

- "Arches is an open-source data management platform… originally developed for the cultural heritage field"; "at its inception, Arches was specifically designed as a generic **heritage inventory management system**".
- Capabilities: data management, discovery/visualization (geospatial), project/task management (workflows), mobile data collection app (Arches Collector).
- Uses: Heritage Inventory, Heritage Science, Digital Humanities, Infrastructure/Construction Project Management; specializations include Arches for HERs (Historic Environment Records), Arches for Science, Arches for Reference and Sample Collections (RaSColls).
- Community sectors include archaeology — archaeology is a major user domain, but the platform's center of gravity is place/site/heritage-asset inventory and geospatial visualization, not object-level custody tracking. This makes it the cleanest structural contrast against collections management.

## Cross-product Comparison

| Dimension | CollectiveAccess | Proficio (+Archaeology) | TMS Collections | Axiell Collections/EMu | Arches (contrast) |
|---|---|---|---|---|---|
| Collection object records (identified, typed, hierarchical) | yes (A) | yes (A) | yes (B) | yes (B) | not the center (resource models are place/asset-oriented) |
| Accession lot + object-level split | yes (A: lots, deed of gift at lot) | yes (A: accession records; accession/deaccession listed) | not documented publicly | not documented publicly | no accession machinery observed |
| Site / provenience / context structure | configurable (places + relationships; no hard-coded archaeology) (A) | explicit: site → master context → context levels → artifacts (A) | not visible on public docs | not visible on public docs | site/place inventory is the core (A) |
| Storage location hierarchy + location tracking | yes (A: nested building→drawer; home location; movement records) | yes (A: locations tracked; inventories; mass location updates) | yes (B: "locations and movements" not stated; roles imply) — actually Axiell states this; TMS not documented publicly | yes (Axiell: "collections data, media, locations, and movements") (B) | no object custody |
| Movement / inventory events | yes (A: ca_movements; inventories implied by features) | yes (A: inventories, mass updating) | not documented publicly | yes (B: "movements") | n/a |
| Condition / conservation documentation | yes (A) | yes (A) | separate product line (B) | bundled DAM/engagement; conservation separate (B) | heritage science specialization (A) |
| Loans in/out | yes (A) | yes (A) | not documented publicly | not documented publicly | n/a |
| Media / digital representations | yes (A: representations, DAM-adjacent) | yes (A: digital assets) | separate DAM product (B) | yes (B) | yes (geospatial/media) |
| Controlled vocabularies / authorities | yes (A: LCSH, Getty AAT/TGN, GeoNames; lists & authorities) | yes (A: standardized terminology; directories) | yes (B: integrated thesaurus) | yes (B: standards-based) | yes (A: standards-based, CIDOC CRM-oriented — cite as standards page; not fetched, keep weak) |
| Roles / permissions | yes (A) | yes (A: volunteer read-only example) | implied by roles pages (B) | yes (B: robust security and permissions) | yes (A: project/task workflows) |
| Public web portal | yes (A: Pawtucket; access flags) | yes (A: Proficio for the Web) | separate "Online Collections" product (B) | yes (B: digital engagement) | yes (A: public discovery) |
| Cataloging standard compliance marketed | standards support (A) | not prominent | Spectrum badge (B) | "standards-based to ensure compliance" (B) | standards/interoperability page (A) |
| Open source | yes (A) | no | no | no | yes (A) |

Legend: A = directly observed in official documentation for that product; B = official marketing/product page only.

## Canonical Model (Synthesis Draft)

### L0 — Defining Invariant (smallest recognizable structure)

1. **Identified collection object records** — every artifact (or bundle of artifacts: lot, lot group, assemblage) is an individually numbered, cataloged record in an institutional catalog.
2. **Documented excavation context linked to objects** — a first-class record structure for where objects came from: site/project, and within it the excavation units / contexts / strata that objects are associated with. Removing this collapses the Type into generic museum collections management; keeping only sites without object custody collapses it into heritage inventory.
3. **Physical custody tracking** — hierarchical storage-location records and an assignment of each object to a location, with the ability to record movement between locations (and reconcile against physical inventory).
4. **Custody lifecycle events on a held collection** — the institution holds the collection in trust: objects enter through acquisition/accession and exit (if ever) through recorded deaccession/disposition; movement, loan, and exhibition are recorded as trackable events, not silent edits.

Test: remove object catalog → not collections management; remove context linkage → generic museum CMS; remove custody/location → heritage inventory or a bare find catalog; remove lifecycle/custody events → a plain database with no accountability structure.

### L1 — Common Mature Structure (expected in modern products, not definitional)

- condition reports and conservation treatment documentation
- loans in and out (with dates, shipping, insurance), exhibition association
- media attachments / digital representations (photos, drawings, PDFs), increasingly with DAM features
- authorities and controlled vocabularies (people/organizations, places, materials, cultures/periods; Getty TGN/AAT-style integration)
- search across all fields; reporting; batch/mass updating
- user roles and granular permissions (volunteers/read-only through administrators)
- cataloging workflow statuses (e.g., pending accession → accessioned) and access/visibility flags for public surfaces
- public web portal / online collections publication
- numbering policies governing identifiers
- physical inventory tooling (stocktaking, reconciliation)

### L2 — Variant / Optional Structure

- discipline breadth: single-discipline archaeology repository vs multidisciplinary CMS with an archaeology catalog among art/history/natural-history/archives catalogs
- deployment: installed desktop (legacy/mid-market), web, cloud/hosted
- active-project orientation (managing ongoing excavations and their finds, sometimes with field/mobile capture) vs legacy-collection orientation (backlog cataloging of held collections)
- regulatory/standards regime overlays: cataloging standards compliance (e.g., Spectrum in the UK market), government repository regimes (regional; specifics vary and were not directly verified in this sample)
- depth of public access (static search portal vs rich online exhibitions)
- geospatial/GIS integration depth (site mapping; stronger in the heritage-inventory world)
- integration with excavation field-recording systems (import of field data) — plausible and discussed in the domain, but not directly evidenced in the sampled official docs; treat as optional/unverified
- large-scale moves as a dedicated concern (enterprise vendors ship separate move-planning products)

### L3 — Vendor-specific (research notes only)

- Proficio: "Master Context" / "Context Levels" naming; "cross-mend artifacts" feature; catalog styles branded per discipline; Elements/Cloud/Mobile/For-the-Web packaging.
- CollectiveAccess: concrete table names (ca_objects, ca_object_lots, ca_movements default-disabled, ca_storage_locations, ca_places, Pawtucket); access/status value conventions; tours/tour-stops machinery; interstitial relationship data.
- Gallery Systems: TMS/Constituents terminology; Spectrum Partner badge; e-museum/online-collections product split.
- Axiell: Quria/CultureConnect/Arena/Move product constellation; EMu's natural-history strength.

## Historical / Market-Sample Check (per §24 thinking)

- Would a 1990s-era installed desktop catalog (pre-web) satisfy the L0? Yes: object records + site/context fields + location tracking + accession/deaccession exist in desktop-era products (Proficio's 30-year lineage; Re:discovery's origins in state-government survey data). The definition does not depend on web portals, DAM, or cloud — those stay in L1/L2.
- Would a non-US product fit? Yes: CollectiveAccess (used internationally), Axiell (European), TMS (international); Spectrum (UK) compliance appears as a regional standard overlay (L2), not structure.
- Would a small historical society with a mixed collection fit? Yes — via multidisciplinary catalogs where "Archaeology" is one catalog style among several; the Type does not require a dedicated archaeology-only product.
- Check outcome: the definition must not assume web delivery, DAM, public portals, or named vendor hierarchies. It should not assume a specific context-naming scheme (unit/stratum/context/lot vary by national tradition).

## Vendor-specific Findings

See L3 above. Also note product-form finding: no sampled vendor sells "archaeological collection management" as a standalone product — it ships as (a) a discipline catalog/module inside a collections-management product (Proficio), (b) a configuration of a configurable CMS (CollectiveAccess), or (c) an unsegmented capability of a museum CMS (TMS, Axiell). The Type is real in the market's vocabulary and in product structure, but it is institutionally realized as an instantiation of collections management.

## Boundary Findings

1. **vs Museum Collections Management (sibling leaf)**: shares the entire custody spine (object catalog, accession/deaccession, locations/movements, loans, condition, portal). The archaeology leaf's differentiator is the excavation-context layer (site → context/stratum → object) as first-class documentation, plus a project/site orientation and repository regimes. Test: strip provenience/context machinery and the product is still a complete museum CMS; strip the object-catalog/custody spine and nothing remains. Verdict: gradient boundary; probable Variant-of/overlap relationship to flag for joint review when Museum Collections Management is processed. No unilateral taxonomy change.
2. **vs Cultural Heritage Asset Management / heritage inventory platforms (Arches)**: inventories of places, monuments, sites and heritage assets with geospatial visualization; no per-object custody tracking, no accession/deaccession. Test: object custody (where is this artifact stored, who may borrow it) exists → collection management; only place/asset records → heritage inventory. Arches confirms the split empirically (a deliberately different platform serving overlapping archaeology users).
3. **vs excavation / field-recording systems (no directory leaf)**: systems used during fieldwork to record contexts and finds in situ (mobile capture, stratigraphy drawing). Collection management begins post-recovery, when objects become held collection items. Some products add mobile capture (Arches Collector, Proficio Mobile) but the center remains the held collection.
4. **vs Museum Accession / Cataloging, Object Movement, Loan, Conservation, Condition Reporting (§27 siblings)**: in the sampled products these are all capabilities/modules of one collections-management system, consistent with flags already raised for other CMS-sibling leaves; probable Capability relationships.
5. **vs Digital Collection Portal**: publication surface (Pawtucket, Proficio for the Web, Online Collections) — a slice, usually a separate product/module feeding off the CMS.
6. **vs Archives Management System (§23)**: adjacent and often same-suite; archives manage document collections with finding aids (DACS); collection management manages objects. CollectiveAccess notably supports both (collections records configurable for DACS) — suites blur the line; the center differs.

## Uncertainties

- PastPerfect unreachable (403 ×2): SMB-segment evidence relies on Proficio Elements; SMB archaeology cataloging specifics unverified.
- TMS and Axiell operational documentation is behind client portals: their archaeology-specific handling could not be observed; all claims about them kept at positioning level.
- Exact archaeology field vocabularies (site-number formats, context-numbering conventions like single-context vs stratigraphic-unit traditions) were not verifiable from sampled docs; no precise conventions asserted.
- Field-recording-system integration: plausible, not directly evidenced in sampled official docs; kept optional/unverified.
- Whether any standalone "archaeology repository" product exists outside general CMS frameworks: not found in this pass; treated as market observation, not a claim of absence.
- NAGPRA-style repatriation workflows: mentioned nowhere in the accessible official docs; deliberately not asserted in the final document beyond a weak "regional regulatory overlays exist" variant note (evidence: vendors market standards compliance generally).

## Final Synthesis

Archaeological Collection Management is the discipline-specific instantiation of collections management for excavated material culture. Its world = a catalog of identified objects (or lots) hanging from documented excavation contexts (site → context/stratum), physically housed in tracked storage locations, and moving through an accountable custody lifecycle (accession → cataloging → location/inventory → loan/exhibit → deaccession). Around that spine, mature products add condition/conservation, media, authorities/vocabularies, reporting, roles, and public portals. Deployment and breadth vary (module of multidisciplinary CMS vs configured open-source platform); enterprise vendors segment archaeology only implicitly. The strongest structural boundaries: heritage inventory (places without object custody) and field recording (capture during excavation, before custody). The leaf likely overlaps Museum Collections Management at the spine level — flagged for a joint review, with the excavation-context layer as the candidate differentiator.
