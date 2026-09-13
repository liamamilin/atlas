# Archaeological Collection Management

## Overview

An **Archaeological Collection Management** application catalogs and stewards objects recovered from archaeological excavation. It maintains an identified catalog of artifacts (or bundles of artifacts such as lots and assemblages), documents the excavation context each object came from — the site, and within it the excavation units, strata, or contexts that produced it — tracks the physical custody of every object in hierarchical storage locations, and manages the collection's lifecycle from acquisition into an institution's holding through cataloging, movement, inventory, loans, condition care, and recorded disposition.

The problem it solves is twofold: making a physically held collection **intellectually retrievable** (what is this object, and exactly where did it come from) and **physically retrievable** (where is it stored right now, and how did it get there), while preserving custody accountability for material held in the public or institutional trust.

Its boundary: it is not a heritage or site inventory (which registers places and monuments without holding objects), not an excavation field-recording system (which captures data during fieldwork, before objects enter custody), and not a public collections portal (which is a publication surface fed by it).

## Users & Context

Primary users:

- **collections managers and registrars** — accession objects, assign identifiers, maintain location and movement records, run inventories, process loans and deaccessions
- **curators and archaeologists** — catalog objects, document provenience and context, classify material, period, and culture, and prepare the collection for research use
- **repository and collections technicians** — shelve and move objects, reconcile physical inventories, photograph and digitize
- **conservators** — record condition assessments and treatment documentation against object records

Secondary users:

- **researchers and students** — search the catalog, request access or loans
- **volunteers and interns** — data entry and imaging under restricted permissions
- **database administrators** — configure vocabularies, numbering policies, user roles
- **the public** — through an optional online collections portal

Typical institutional contexts: museums with archaeology departments, university collections, government heritage agencies and state repositories, contract (cultural-resource-management) archaeology repositories, and historical societies holding mixed collections in which archaeology is one catalog among several.

## Core Model

The defining core has four structures. Everything else in the product exists to serve them.

```text
Site / Project
  └── Excavation context (unit / stratum / context)
        └── Object (artifact) or lot / assemblage
              ├── catalog documentation (material, period, culture, dimensions, description)
              ├── storage location (building → room → cabinet → tray)
              ├── condition / conservation records
              └── custody events (movement, inventory, loan, exhibition, deaccession)
```

### Collection object records

Every artifact — or a deliberately bundled group of artifacts — is an individually identified, cataloged record. Each record carries a unique identifier governed by the institution's numbering policy, a record type, descriptive cataloging (material, cultural attribution, period, dimensions, condition notes), and relationships to people and organizations (excavator, donor, researcher) and to places. Objects may also be organized in a hierarchy (an object that is part of another object, or a parent assemblage with child items).

### Excavation context

What makes this an archaeological collection rather than a general one: objects are documented against **where they came from**. A site or project record anchors the collection; beneath it, context records describe the excavated units, layers, or strata; objects link to the context that produced them. Exact naming varies by product and by national recording tradition (site, unit, stratum, context, lot, feature), and some products implement context as hierarchical place records while others give it dedicated record types — but the structure itself, a documented provenience hierarchy that objects hang from, is the distinguishing layer. An object whose context is lost loses most of its scientific value, which is why context is treated as first-class data rather than a descriptive field.

### Storage locations and custody tracking

Physical locations are modeled as a hierarchy (building → room → cabinet → drawer → tray) as their own records. Each object has a home location; movements between locations are recorded as events, so the system can answer not only "where is it" but "how did it get there." Some products also let locations be flagged unavailable. Periodic physical inventories reconcile the catalog against what is actually on the shelves.

### Custody lifecycle

The institution holds the collection in trust, and the record system mirrors that accountability:

```text
acquisition / accession (often as a lot: one accession covering many objects)
  → cataloging (item-level records under the lot)
  → housing and location tracking (storage, movement, inventory)
  → circulation (loans out, loans in, exhibitions)
  → disposition (deaccession with type, date, and notes — recorded, never silently deleted)
```

A common structural split: registrarial information (the deed of gift, the accession transaction) lives on the **lot** record, while item-level cataloging lives on each **object** record beneath it.

### Standard capabilities

Mature products commonly add, around that core:

- condition reports and conservation treatment documentation attached to objects
- loans in and out (with dates, shipping, insurance) and exhibition associations
- media attachments — photographs, drawings, scans, documents — as managed digital representations of objects
- authorities and controlled vocabularies for people, organizations, places, materials, and cultural/period terms, often with integration to published vocabularies
- search across all catalog fields, reporting, and batch/mass updating
- user roles and granular permissions (for example, volunteers who may add records but not delete them)
- cataloging workflow statuses (such as pending accession → accessioned) and public/private visibility flags that govern what appears on public surfaces
- an optional public web portal for online collections

## How It Works

### Bring objects into custody

```text
create an accession (lot) for the acquisition or excavation assemblage
→ assign lot and object identifiers under the numbering policy
→ link the lot/objects to the source site and context records
→ catalog each object (or catalog at lot level for bulk material)
→ attach media and record condition
```

### Document provenience

```text
create the site / project record
→ create context records for excavated units, layers, or strata
→ associate each object with the context that produced it
→ refine over time (reclassification, joins between fragments)
```

Some products support recording joins between fragments of the same original object recovered separately — a domain-specific operation known as cross-mending or refitting.

### House and track

```text
define the storage-location hierarchy
→ assign each object a home location
→ record every movement as an event (shelf moves, loans, exhibitions)
→ run periodic inventories and reconcile discrepancies
```

### Care and circulate

```text
record condition assessments and conservation treatments
→ prepare outgoing loans (dates, shipping, insurance) and receive incoming loans
→ associate objects with exhibitions, tracking their location while out
```

### Dispose and share

```text
deaccession with a recorded type, date, and notes (sold / destroyed / transferred)
→ the record persists with its disposition history
→ publish selected records to the public portal under visibility flags
→ produce reports for researchers, audits, and accreditation
```

## Interfaces

### Object catalog record (editor)

The working surface. Purpose: create and maintain an object's full documentation. Typical information: identifier, type, description, material, period/culture, provenience/context links, dimensions, condition, media, relationships. Primary actions: create/edit record, link context and authorities, attach media, print or export.

### Site / context browser

The provenience surface. Purpose: navigate the collection by where things came from. Typical information: site and project details, context hierarchy, associated object counts. Primary actions: create sites and contexts, associate objects, browse downward into finds.

### Storage location browser and movement tools

The custody surface. Purpose: know where everything is and move it safely. Typical information: location hierarchy, current occupants, movement history. Primary actions: assign home locations, record movements, flag locations unavailable, run inventory checklists.

### Loans and exhibitions registers

Purpose: manage circulation. Typical information: loan parties, dates, shipping and insurance, object lists. Primary actions: create loans, track in/out status, associate exhibitions.

### Search and reporting

Purpose: make the catalog usable at scale. Typical information: results across all fields, saved queries, statistical reports. Primary actions: search, filter, batch-update, generate reports.

### Public portal (optional)

Purpose: publish selected records online. Typical information: object descriptions, images, site/context summaries. Primary actions: browse, search, view — governed by the visibility flags set on records.

### Administration

Purpose: configure the system. Typical information: vocabularies and authorities, numbering policies, user roles and permissions, record-type configuration. Primary actions: manage lists, users, and templates.

## Important Rules / Behaviors

- **Identifiers are governed.** Object and lot identifiers follow the institution's numbering policy; uniqueness is typically enforced or configurable.
- **Lot vs object split.** Registrarial and transactional information is recorded at the accession-lot level; item-level cataloging stays on object records. An object belongs to at most one lot.
- **Deaccession is an event, not a deletion.** Removing an object from the collection produces a recorded deaccession (type, date, notes, disposal date); the historical record persists.
- **Provenience integrity is the point.** The context linkage is treated as core scientific data; cataloging practice pushes for every object to carry its provenience.
- **Visibility is a record property.** Public/private access flags on records determine what surfaces on public portals; cataloging workflow statuses (pending accession, accessioned) track progress and are informational rather than functional.
- **Permissions gate custody actions.** Roles determine who may create, edit, move, or delete records; restricted roles (volunteers, read-only users) are a normal configuration.
- **Movements are recorded, not overwritten.** Location history is kept as events, supporting audit and use-history questions ("where has this been").

## Variants

- **Multidisciplinary CMS with an archaeology catalog** — one product holding art, history, natural history, archives, and archaeology catalogs side by side with a consistent interface; common in small and mid-sized institutions.
- **Configured open-source platform** — a fully configurable cataloging system shaped per project; archaeology structure is realized through configuration rather than a fixed module.
- **Enterprise museum suite** — collections management at the center with separate companion products for conservation documentation, online collections, and digital asset management.
- **Repository / government deployment** — emphasis on regulatory cataloging regimes, accountability, and reporting; regional standards overlays vary by jurisdiction.
- **Active-project vs legacy-collection emphasis** — some deployments center on ongoing excavations and their finds (sometimes with mobile capture), others on backlog cataloging of long-held collections.
- **Deployment form** — installed desktop (legacy and mid-market), web-based, or hosted/cloud.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Museum Collections Management | closest sibling; shares the custody spine | lacks the excavation-context layer (site → context → object) as first-class documentation; archaeology adds provenience-centered structure and repository regimes |
| Museum Accession / Cataloging | capability slice | accessioning and cataloging are functions inside a collection management system, not the whole |
| Museum Object Movement Management | capability slice | movement/location tracking is one machinery within the custody core |
| Museum Loan Management | capability slice | loans are one circulation event type within the lifecycle |
| Museum Conservation Management / Condition Reporting | capability slice | condition and treatment documentation attaches to object records; conservation suites extend it |
| Digital Collection Portal | publication surface | public discovery fed by the collection system; no custody machinery |
| Cultural Heritage Asset Management | adjacent, structurally distinct | inventories places, monuments, and heritage assets with geospatial visualization; no per-object custody, accession, or storage-location tracking |
| Provenance Research Platform | adjacent | documents ownership history of art objects; archaeology documents excavation context, not chain of ownership |
| Archives Management System | adjacent, often same suite | manages document collections with finding aids; collection management manages physical objects |

The most important boundary is with **Museum Collections Management**: the two share the entire custody spine, and the archaeology leaf is distinguishable by its excavation-context layer and site/project orientation. The second most important is with **heritage inventory platforms**: shared vocabulary (sites, heritage, archaeology) but a different center of gravity — places and assets without object custody.

## Representative Products

- **CollectiveAccess** — open-source, fully configurable collections management (Providence cataloging back-end; Pawtucket public front-end)
- **Re:discovery Proficio** — multidisciplinary collections management with a dedicated archaeology catalog (site → context → artifact hierarchy); strong state-agency and repository clientele
- **Gallery Systems TMS Collections** — enterprise museum collections management, international
- **Axiell Collections / EMu** — European enterprise multidisciplinary collections management

## Sources

Research date: **2026-09-06**

- CollectiveAccess — Documentation site: https://docs.collectiveaccess.org/ (About; Introduction to Providence; Data Modelling; Primary Tables and Intrinsic Fields)
- Re:discovery Software — https://rediscoverysoftware.com/ (home; Archaeology Module; Collections Module)
- Gallery Systems — https://www.gallerysystems.com/solutions/collections-management/ (TMS Collections)
- Axiell — https://www.axiell.com/ (Axiell Collections; EMu)
- Arches Project (boundary reference) — https://www.archesproject.org/what-is-arches/

> Sourcing limitations: PastPerfect's site and support pages were unreachable (HTTP 403) during research and it was excluded as a verified sample. Operational documentation for TMS Collections and Axiell Collections sits behind client portals; claims about those products are limited to their public positioning pages, and no archaeology-specific operational detail is asserted for them. Precise field vocabularies, numbering conventions, and regional regulatory specifics are intentionally not stated in this document; they vary by product and national recording tradition.
