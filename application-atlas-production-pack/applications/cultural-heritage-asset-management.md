# Cultural Heritage Asset Management

## Overview

A **Cultural Heritage Asset Management** application is the registry-of-record software for cultural heritage assets: historic buildings, monuments, archaeological sites, parks and gardens, battlefields, cultural landscapes, districts, and comparable place-based heritage resources. It holds each asset as an individually identified, persistent record characterized in heritage terms — what it is, what period it belongs to, what is known about it, what protection status it carries — and anchored to a location in geographic space. Around that registry, the system captures the activities through which the heritage body understands, protects, and manages the assets: field surveys and investigations, designation and listing decisions, planning consultations, condition monitoring, and publication of the inventory to professionals and the public.

The defining core is deliberately small: a standing inventory of heritage asset records, heritage-domain characterization, and location anchoring. Everything else — interactive mapping, public web portals, consultation casework, community nomination, condition monitoring — is widely present in mature products but is an extension of the registry, not what makes the registry this Type of application.

The boundary matters as much as the definition: this Type does **not** hold objects in custody. It has no accessions, no storage locations, no loans. The moment a system must answer "which shelf is this object stored on and who may borrow it," it has become a collection-management system. Cultural heritage asset management answers a different question: "what is this place, where is it, what do we know about it, and what is its status?"

## Users & Context

Primary users:

- **heritage agency and registry staff** — national, provincial, or municipal bodies responsible for identifying, recording, and protecting heritage assets; they create and maintain the inventory, assess candidates, and carry out designation and review work
- **historic environment / conservation officers** — local-government officers who curate the inventory day to day, answer enquiries from planners and contractors, and advise on development proposals affecting heritage assets
- **casework and review officers** — staff who manage consultations and statutory review processes, from logging an incoming enquiry to recording recommendations and outcomes
- **surveyors, archaeologists, and contractors** — field professionals whose investigations produce the events, reports, and imagery that document the assets

Secondary users:

- **researchers, students, and local historians** — search the inventory and use its sources
- **planning departments and agencies** — consume inventory data (directly or through map services and APIs) when making land-use and development decisions
- **the public** — browse published records on interactive maps; in some products, register to submit and discuss candidate heritage assets
- **system administrators** — manage vocabularies, record models, user roles, and publication settings

Typical institutional contexts: national heritage registries and monuments records; local-government historic environment records serving the planning process; city-wide cultural resource surveys; heritage trusts and nonprofits operating official lists; research programs documenting endangered or little-recorded heritage; and heritage authorities in rural or regional jurisdictions building inventories from legacy paper records.

## Core Model

The world of the application is organized around one central object and a documentation layer gathered around it.

```text
Heritage organization (the responsible body)
  └── Standing heritage inventory
        └── Heritage asset record (identified, persistent)
              ├── heritage characterization (type / form, period, description)
              ├── location anchoring (position / extent)
              └── documentation gathered around the asset
                    ├── activities & events (investigations, designation, management actions, casework)
                    ├── sources (reports, archives, bibliography)
                    └── actors (people and organizations)
```

### Heritage asset record

The heritage asset record is the unit of the system. Each record is an individually identified, persistent description of a place-based resource — a monument, building, site, area, structure, or landscape — that the organization has reason to know about and look after. Records are added as heritage is discovered, surveyed, or threatened, and they persist even when knowledge about them changes; the record's history is part of its value. A record is not an object held by the institution: the castle, bridge, or earthwork exists in the world, and the record exists to make it knowable and manageable.

### Heritage characterization

What makes the record a heritage record rather than a generic database row is its documentation vocabulary: asset type and form, period and dating, description and statement of what the asset is and why it matters. Mature products govern this vocabulary with controlled terminologies and thesauri, so that entries made by different people over decades remain comparable and searchable. Data standards exist for exactly this layer — they define the minimum information an asset record should carry and the activities and sources that document it.

### Location anchoring

Every asset is anchored to geographic space. In current products this is usually realized as spatial geometry displayed and queried on interactive maps, integrated with geographic information systems; the location may be a point, a boundary, or an extent. But location anchoring, not mapping software, is the essential property: even paper-era monument inventories anchored each record to a location on a map. The location is what lets the system answer the characteristic question — "what heritage assets are affected by work in this area?" — by spatial selection.

### The documentation layer

Around the asset record, mature systems accumulate linked documentation:

- **Activities and events** — investigations and surveys that studied the asset, designation and protection decisions made about it, management actions taken on it, and casework in which it figured. An event record says what was done, when, by whom, and what it found or concluded.
- **Sources** — the reports, archive references, bibliography, and narrative syntheses behind the knowledge in the record. The inventory distinguishes what is known from the evidence that makes it known.
- **Actors** — people and organizations: discoverers, owners, investigators, consultees, decision-makers — each linked to the assets and events they relate to.

Some systems also record finds or objects *associated with* a place — material spotted in the landscape or recovered from a site — as documentation of the asset. These remain records about the asset, not accessioned holdings: the system does not track their storage, ownership, or circulation.

### Protection status

A heritage asset typically carries its official standing: whether it is listed, registered, scheduled, or otherwise recognized, and under which designation regime. This status connects the inventory to the legal and planning world around it. It is standard in registry-like deployments, while survey-based inventories may carry assets without formal status — the status layer is common and important, but an inventory without it is still this Type of application.

### Standard capabilities

Around this core, mature products commonly provide:

- map-first browsing, geospatial search, and integration with desktop GIS
- text, spatial, and temporal search over the whole inventory, with saved and advanced queries
- terminology/thesaurus management governing data entry and search
- designation and protection-status recording
- bulk import of legacy data and digitized records; export and reporting
- media and document attachments — photographs, drawings, reports — as managed representations of the asset and its documentation
- user and group permissions, audit trails of changes, and review of provisional entries before publication
- a public web surface publishing part of the inventory as searchable, mapped records
- APIs or map services for other systems (planning, GIS, data portals)

## How It Works

The application supports one standing loop — keeping the inventory true — plus several workflows that feed it.

### Build and maintain the inventory

```text
an asset becomes known (survey, fieldwork, research, report, public nomination, legacy records)
→ create or update the asset record: identity, type, period, description
→ anchor it to a location (geometry or map reference)
→ attach the sources that justify what the record says
→ entry is reviewed where required, then adopted into the standing inventory
```

Much of the practical work is ingestion: migrating legacy paper records and digitized archives, importing survey datasets in bulk, and capturing new observations in the field with mobile tools. The inventory is never finished; it is a living registry that grows and is corrected over time.

### Record what is known

```text
an investigation, visit, or management action takes place
→ create an activity/event record describing what was done and found
→ link it to the affected asset(s), the actors involved, and the resulting report or archive source
→ the asset's knowledge base and its record history deepen
```

This loop is what turns a list of places into a managed knowledge base: the asset record accumulates its own documentation history, each item of which is itself retrievable.

### Designate and list

```text
a candidate asset is proposed (by staff or by public nomination)
→ evidence is gathered and assessed against the designation criteria
→ a determination is recorded with its justification
→ the asset's protection status is set, and the entry enters the official list
```

Where community nomination exists, the public submits candidate sites with location, justification, and supporting images; staff review and adjudicate, give feedback, and record decisions with reasons — all under an audit trail, with accepted entries flowing into the inventory.

### Advise planning and manage casework

```text
an enquiry or development proposal arrives
→ the affected area is drawn or identified on the map
→ the system retrieves all heritage assets within or near that area
→ the officer records the consultation: type, dates, proposals, recommendations
→ actions and outcomes are tracked and archived against the case and its assets
```

In planning-linked deployments this casework machinery is the inventory's main operational output: heritage data entering land-use decisions. The system records and supports the consultation — the statutory process itself happens outside it.

### Monitor condition

Where supported, observations of an asset's state — damage, deterioration, risk, use — are captured, often in the field via mobile collection, and attached to the asset record over time as part of preventive conservation practice.

### Publish and serve

```text
records and maps reach an agreed state
→ selected data is published to the public portal or exposed through map services and APIs
→ planners, researchers, and the public search and browse
→ enquiries and corrections flow back into the inventory
```

Publication is governed: not everything recorded internally is published, and access tiers separate public, registered, and internal views.

## Interfaces

### Map-centered search and browse

The signature surface. Purpose: find assets by where they are as naturally as by what they are. Typical information: interactive base maps (often including historic map and satellite layers), asset geometries, search filters by type, period, designation, and date. Primary actions: pan/zoom, spatially select an area, filter and search, open an asset record, layer designation and survey data.

### Asset record editor

The working surface for registry staff. Purpose: create and maintain the full documentation of one asset. Typical information: identity and number, type and period, description, location and geometry, protection status, linked events, sources, actors, media. Primary actions: create/edit, link documentation and vocabulary terms, attach media, view change history.

### Consultation / casework screen

The advisory surface in planning-linked deployments. Purpose: manage a consultation from arrival to archived outcome. Typical information: consultee and type, log/target/completion dates, proposals, spatial extent, recommendations, outcomes, linked assets and documents. Primary actions: log a case, retrieve assets in the affected area, record recommendations and outcomes, generate reports.

### Nomination dashboard

The community-entry surface where supported. Purpose: adjudicate public candidate sites. Typical information: pending candidates with location, justification, and media; submission status; feedback threads. Primary actions: review, request improvements, approve/reject with recorded justification, publish accepted entries to the list.

### Public portal

The publication surface. Purpose: make the (published part of the) inventory searchable by everyone. Typical information: mapped assets, record summaries, images, protection status. Primary actions: search, browse the map, view records; in nomination-enabled products, register, submit candidates, and comment.

### Administration

Purpose: configure and govern the system. Typical information: vocabularies and thesauri, record models and forms, user roles and permissions, publication settings. Primary actions: manage terminology, configure record types, control access, audit changes.

## Important Rules / Behaviors

- **The record is of record.** Asset records persist and accumulate; changes are logged in audit trails, and prior states remain retrievable. Removing an asset from an official list is recorded as a decision, not an erasure.
- **Vocabulary is governed.** Characterization fields are populated from controlled terminologies so that decades of entries by different hands stay consistent and searchable. Terminology management is an administrative first-class activity, not an afterthought.
- **Spatial selection is a first-class operation.** "Everything within this area" is a core query of the Type, used constantly in casework and publishing; the map is both a working tool and an access route to records.
- **Access is tiered.** Internal, registered, and public views of the inventory differ; some recorded data is withheld from publication entirely, and unpublished or provisional entries are held for review before adoption.
- **Viewing is not consulting.** In planning-linked systems, using or reading the inventory explicitly does not substitute for the statutory consultation process; the system records casework, the legal process happens outside it.
- **Custody is absent by design.** Objects and finds appear as documentation of assets, not as accessioned holdings; the system does not model storage locations, ownership chains, or loans. This is the structural line between this Type and collection management.
- **Legacy data is a permanent concern.** Because these registries often descend from decades of paper records, bulk import, digitization, and reconciliation are standing features rather than one-time projects.

## Variants

- **National heritage register / monuments record** — a jurisdiction-wide registry of protected and recorded assets; emphasis on completeness, official status, and publication.
- **Local historic environment record** — a county or municipal inventory curated as an advisory service to planning; emphasis on casework, responsiveness, and integration with planning and GIS.
- **City survey inventory** — an urban cultural-resource survey maintained as a living inventory; emphasis on field survey campaigns and public transparency.
- **Designation-list platform with community nomination** — the public nominates, the authority adjudicates; emphasis on engagement workflows and determination records.
- **Thematic and research inventories** — endangered-heritage documentation, marine and underwater heritage, cultural routes, architectural corpora; emphasis on rapid condition/risk recording and open publication.
- **Agency program portal** — the inventory bound to heritage programs (registers, tax-credit and review processes); emphasis on application and review flows for agencies and municipalities.
- **Deployment form** — an open-source platform configured per organization; a commercial specialist package (desktop application integrated with third-party GIS, plus a web tier); or a government-built custom system.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | closest sibling; shares the family space | collection management centers on accessioned objects under custody — numbering, storage locations, movement, loans; heritage asset management holds records about places in the world, with no custody chain |
| Archaeological Collection Management | sibling with a specialized spine | adds an excavation-context hierarchy and per-object custody of recovered finds; heritage asset management documents the site as a place, not its excavated objects |
| Digital Collection Portal | adjacent | a publication surface fed by a registry; this Type owns and maintains the registry itself |
| Government GIS / Land Records / Cadastre | adjacent | those make parcels and administrative geometry the object of record; here spatial location is a property of the heritage record, which carries characterization and status |
| Building Asset Management / Building Condition Assessment | adjacent, drift risk | those manage buildings as operational/financial assets of an owner (maintenance, costs, facility condition); this Type manages heritage resources for protection and knowledge, in the public trust |
| Archives Management System | adjacent | archives manage document collections as custody objects; heritage inventories reference sources without managing the archive |
| Provenance Research Platform | adjacent | documents ownership history of art objects; heritage asset management documents places and their standing |
| Permit Management / Planning & Zoning Management | adjacent workflow | heritage systems act as consultees and advisors feeding planning; the permit/plan-control machinery lives in the planning system |
| Public Data Portal | adjacent | one-way publication of datasets; the heritage registry is the maintained source beneath any such publication |

The most important boundary is the custody line: shared vocabulary (sites, finds, archives, heritage) hides a structural difference — collection management tracks *objects the institution holds*, while this Type tracks *places the world holds* and the knowledge and protection standing attached to them.

## Representative Products

- **Arches** — open-source heritage data-management platform developed by the Getty Conservation Institute and World Monuments Fund; configurable, standards-based, GIS-native; the basis of national registries, city inventories, and research databases worldwide (including England's marine heritage record, the Greater London historic environment record, Wales' national site index, the British Columbia Register of Historic Places, and city surveys in California).
- **exeGesis HBSMR** — commercial specialist software for historic environment records, the dominant system in its UK market; desktop application with integrated third-party GIS, consultation casework, designation recording, and a web/API publication tier, plus a companion local-heritage-list platform with public nomination.
- **New York State CRIS (Cultural Resource Information System)** — a government-built heritage inventory and review portal operated by a state historic preservation office; GIS access to inventory forms, register documents, and survey reports serving statutory review processes and heritage programs.

## Sources

Research date: **2026-09-07**

- Arches Project — https://www.archesproject.org/what-is-arches/ ; https://www.archesproject.org/features/ ; https://www.archesproject.org/arches-for-hers/ ; https://www.archesproject.org/implementations-of-arches/
- Exegesis SDM — https://esdm.co.uk/hbsmr-features ; https://esdm.co.uk/hbsmr-consultations ; https://esdm.co.uk/local-heritage-list-platform ; https://hbsmrdocumentation.esdm.co.uk/
- New York State Office of Parks, Recreation and Historic Preservation — https://cris.parks.ny.gov/
- Forum on Information Standards in Heritage — MIDAS Heritage: http://www.heritage-standards.org.uk/midas-heritage/

> Sourcing limitations: Historic England's guidance pages were unreachable during research (HTTP 403). Full operational documentation for HBSMR is available to registered users only, so its module structure is verified from the public documentation index and vendor descriptions, and no field-level operational details are asserted for it. Deployment-specific figures (record counts, market-share claims) observed on vendor pages are intentionally not stated in this document. Claims about condition monitoring rest on deployment descriptions of one platform family and are phrased accordingly.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
