# Directory Application

## Overview

A **Directory Application** is a lookup application: it maintains a catalog of standing entries about entities of one defined class — businesses, people, companies, government agencies, or any other population fixed by the directory's scope — and organizes that catalog so a user can find a specific entity and reach it.

The defining core is deliberately small:

```text
Defined entity class
└── Standing entry — one structured record per entity of the class
    └── Attribute profile — identity + reach attributes (name, contact, location …)
    └── Retrieval organization — browse structures and search keys over the catalog
```

If any of these is removed, the product stops being a directory: remove the bounded entity class and maintained catalog and it becomes a general search engine or an unbounded index; strip the attributes from entries and it no longer routes anyone to the entity; remove browse and search and it is just a pile of records.

Everything else commonly associated with directories — reviews, self-service claiming, paid placement, maps, verification badges, APIs — is widespread but not definitional. The same core covers the print-era yellow pages and residential phone book, paper membership rosters, and today's web directories, which is why none of those era-specific features belong in the definition.

## Users & Context

Two user populations face the same catalog from different sides:

**Lookup users** (usually the overwhelming majority):

- a consumer looking for a local plumber's phone number
- a buyer trying to verify a company exists and find its registered details
- a citizen looking up which government agency handles a matter and how to contact it
- anyone who has a fragment — a phone number, an address, a company number — and needs to know who or what is behind it

Their job starts from a need to *reach or evaluate an entity* and ends when they have contact details, an office location, a website, or enough attributes to judge whether the entity is what they need.

**Entity-side and operator users:**

- entity representatives who create, claim, or correct their own entry (where the directory allows it)
- the directory operator's editorial or data staff who curate entries, manage categories, and handle corrections, disputes, and removal requests

The work context is task-driven and brief: a lookup session typically lasts moments, and the value of the directory lies in returning the right entity quickly — not in keeping the user engaged.

## Core Model

### The defining core

**Entity class.** Every directory fixes one kind of thing it covers — residential people, businesses, registered companies, government agencies. The class determines the entry schema: a person entry carries phone numbers and addresses; a company entry carries registration identifiers and officers; an agency entry carries contact channels and office finders. A product that spans classes usually runs them as separate catalogs within one service (for example, a company search and a separate officer search over the same filings).

**Standing entry.** The unit of the catalog is one record per entity — not per offer, not per article. The entry persists as long as the entity plausibly exists and represents the entity itself. This standing quality is what distinguishes a directory from a listings surface: a for-sale listing dies when the sale completes; a directory entry survives until the entity does (and even beyond — terminated companies, historical records).

**Attribute profile.** Each entry presents the entity's identity together with attributes sufficient to identify, distinguish, evaluate, and reach it. The floor is identity plus reachability — name and some combination of phone, address, website, or official contact channel. Richer profiles add descriptions, categories, hours, credentials, related parties, and links into underlying records (for instance, a company entry linking to its filed documents).

**Retrieval organization.** The catalog is organized for lookup along two complementary paths:

- **Browse** — standing structures that expose the catalog without a query: category taxonomies (a directory of businesses organized by trade), alphabetical indexes, geographic grids (city pages, jurisdiction lists)
- **Search** — keyed retrieval: by entity name, and frequently by attribute keys, so a phone number, an address, or a registration number can serve as the starting point rather than the answer

```text
                     ┌──────────────────────────────┐
   Browse            │  Catalog of standing entries │            Search
   category ▶───────▶│  (one record per entity of   │◀──────── name, phone,
   A–Z ▶────────────▶│   the defined class)         │◀──────── address, number,
   place ▶──────────▶│  each: identity + attributes │◀──────── officer, keyword
                     └──────────────┬───────────────┘
                                    ▼
                          Entry detail surface
                          (full profile + reach actions)
```

### Standard capabilities of mature directories

These are common across the researched sample and expected in a mature product, but a directory without them is still a directory:

- **Entry detail surface** — a dedicated page per entity aggregating the full attribute profile, reach actions (call, website, directions, official contact), and links to related records or documents
- **Reverse / attribute lookup** — treating attributes as query keys: find the person behind a phone number, the company behind a registration number, the officers behind a company
- **Geographic axis** — location as a first-class retrieval dimension (required location fields, city browse pages, jurisdiction scoping, "find an office near you" locators)
- **Faceted / advanced search** — narrowing by structured attributes of the class; common in register-style directories and aggregators
- **Entry lifecycle states** — register-style directories track a record's status (active, dissolved, historical); the status is itself lookup information
- **Derived directories** — secondary catalogs computed from the same source material: officers derived from company filings, offices and sub-locators derived from an agency, relatives and associates derived from shared records
- **Programmatic access** — an API or bulk channel exposing the same catalog to other systems

### One structure, many implementations

```text
Concept:        Standing entry
Implementations: aggregated public records · self-service listings ·
                statutory filings · official editorial curation

Concept:        Retrieval organization
Implementations: category × city browse · A–Z indexes ·
                keyword search · reverse phone/address/number lookup ·
                faceted advanced search

Concept:        Reach attributes
Implementations: phone / address / website / contact forms ·
                registered office and filings · agency contact channels
```

## How It Works

### The lookup loop

The defining workflow is short and repeatable:

```text
Arrive with a need (a trade, a name, a number, an address, a jurisdiction)
→ choose a retrieval path: browse (category / A–Z / place) or search (name / attribute key)
→ scan the candidate list (identity, location, key attributes)
→ open the entry detail surface
→ use the reach attributes: call, visit the website, get directions, contact the office
→ optionally: refine and search again, or save/follow the entry
```

No account is typically required to look up. The catalog is the product; the user's loop ends at the moment of contact.

### How entries come into existence

A directory must populate its catalog, and the sourcing model is a major design choice that varies without changing the Type:

- **Aggregation** — records compiled from public sources and linked into one identity record per entity
- **Self-service submission** — entities add or claim their own listing (a "free listing" signup is a common pattern in business directories)
- **Statutory filing** — entities are legally obligated to file, and the register is the by-product (company registers work this way; accuracy responsibility stays with the filer)
- **Editorial / official curation** — the operator maintains entries directly (typical for government and institutional directories)

Most commercial directories mix these: an aggregated or editorial baseline, self-service claiming on top, and paid visibility as the monetization layer.

### Maintenance and correction

Entries are standing records, so keeping them current is part of the job: entity-side editing where claiming exists, operator-side correction and dispute handling, removal or suppression requests (particularly sensitive for people directories), and lifecycle handling when an entity closes, merges, or dissolves — at which point the entry may be marked rather than deleted, because historical lookup is itself a use case.

### Where monetization usually attaches

- advertising and paid placement around search results and entries
- freemium gating of attribute depth (fuller contact details behind a subscription)
- data licensing — API and bulk access to the same catalog for verification, enrichment, and fraud-prevention uses

None of these change what the application is; they change who pays for it.

## Interfaces

Described in conceptual terms; exact layouts vary by product.

### Search surface (home)

The primary entry point.

- a query field — often split into *what* (entity, trade, keyword) and *where* (location), or a single field accepting names, numbers, or identifiers
- primary actions: run a search, pick a retrieval path (browse entry points), switch lookup mode (people / reverse phone / reverse address, or companies / officers)

### Browse surfaces

Standing structures exposing the catalog without a query.

- category indexes (trades, topics), often presented as popular-entry shortcuts plus deeper hierarchies
- alphabetical indexes over the entity class or over names within it
- geographic grids (city pages, jurisdiction lists) frequently combined with categories

### Results list

Candidates matching the query or browse node.

- per-result identity and disambiguating attributes (location, category, key identifiers)
- primary actions: open an entry, refine the query, filter or sort

### Entry detail surface

The full profile of one entity.

- identity block (name, class-specific identifiers), reach attributes (phones, addresses, websites, contact channels), descriptive attributes, lifecycle status where applicable
- links into related records: underlying documents, filed data, related parties, sub-offices
- primary actions: contact, navigate, view related records, report a correction, follow/save (where offered)

### Entity-side management surface

Where claiming or submission exists: create or claim an entry, edit attributes, respond to operator review. In statutory registers, this surface becomes the filing surface itself.

### Operator / moderation surface

Catalog management: curation, category management, correction and dispute queues, suppression and removal handling.

## Important Rules / Behaviors

### Entries are standing, not transactional

A directory entry represents the entity, not a current offer. It persists across sessions and, commonly, beyond the entity's active life (terminated companies remain look-up-able as historical records). This persistence rule is what makes the directory a reference surface rather than a marketplace.

### The entry, not the document, is the object

Where a directory links to underlying records (filed documents, certificates, source data), those are attachments to the entry — the entry remains the stable handle by which the entity is found.

### Provenance is the operator's stated posture

Every sourcing model implies a truth posture: statutory registers typically state that they do not verify filed information; aggregators publish provenance principles; editorial directories stand behind their curation; self-claimed entries rest on the claimant. The application's rules make this posture visible rather than hiding it.

### People directories carry privacy obligations that business directories do not

When the entity class is people, lookup power is personal-data exposure. The observed commercial pattern is attribute gating — part of the catalog free, fuller contact and history details behind a subscription — and privacy functions as a structural constraint on what the catalog exposes, rather than a marketing afterthought.

### Paid visibility must not break lookup

Where advertising or paid placement exists, the catalog's usefulness depends on organic results remaining retrievable; mature directories separate paid prominence from the standing catalog's completeness.

## Variants

Common forms of the Type. The core model holds across all of them:

- **Residential / people directory** — the digitized phone book: people lookup plus reverse phone and reverse address; freemium attribute gating; drift toward identity-verification data services
- **Local business directory** — the digitized yellow pages: category × geography retrieval, business profiles, self-service listings, advertising-funded; often with an attached content layer (guides, articles); drift toward marketing services for the listed businesses
- **Statutory company register** — filing-driven records of legal entities with registration identifiers, officers, lifecycle status, and underlying documents; free public service; accuracy responsibility disclaimed onto filers
- **Cross-jurisdiction entity aggregation** — unified company/officer records assembled from many official registers under one search, with explicit provenance principles; commonly sells API and bulk access
- **Institutional / agency directory** — editorially maintained official catalog of organizations and their contact channels and office locators; no claiming, no advertising
- **Bounded-population directories** — the same structure scoped to a closed roster, such as an association's member directory or an organization's staff directory, where the population is defined by membership or employment rather than by a market or jurisdiction

A variant stops being a Directory Application when its record stops being a standing entity profile: point-in-time offers move it to a Listings Platform, opinion content to a Review Platform, and unbounded indexing to a search engine.

## Related Application Types

| Type | Distinction |
|---|---|
| Listings Platform | records are current offers (things for sale, rent, hire) that expire or consummate, vs standing entity records that persist with the entity |
| Information Portal | organizes content — news, links, resources — around a topic, vs organizing entity records for lookup |
| Review Platform / Comparison Platform | centers on opinions about entities (ratings, reviews, comparisons); directories center on the entities' own attribute records, with opinions at most an attached layer |
| General / Vertical Search Engine | indexes an unbounded corpus and returns links; a directory maintains a bounded, structured, curated catalog whose entries are first-class records |
| General Reference Database | holds facts and knowledge about things; a directory's signature output is routing the user to a contactable entity |
| Social Profile Network | centers on self-authored profiles, feeds, and social graphs; people directories center on identity/contact lookup regardless of self-authorship |
| Member Directory | same structure scoped to a closed membership roster — most plausibly a domain-scoped instance of this Type; deserves joint review |
| Contact Discovery / Sales Data Enrichment Platforms; Master Data Management | consume entity data as feeds for workflows; the directory is the human lookup surface over such records — several real products operate on both sides of this seam |
| CRM | manages an organization's own relationship records and commercial workflows; a directory's entries are public-standing records with no deal progression |

The most load-bearing boundary within its own family is with the Listings Platform: both are "organized retrievable records," and the test is whether a record describes the entity itself (directory) or a current offer about the entity (listing).

## Representative Products

- Whitepages — US residential/people directory; freemium; reverse lookup
- Yellow Pages Australia — category-organized business directory; advertiser-funded; print-book companion
- Companies House (Find and update company information) — UK statutory company register; filing-sourced; free public service
- USA.gov A–Z index of U.S. government departments and agencies — official institutional directory; editorial curation
- OpenCorporates — cross-jurisdiction company/officer aggregation; provenance-led; API/data-supply drift

Together they cover the main entity classes (people, businesses, companies, agencies), the main sourcing models (aggregation, claiming, statutory filing, editorial curation), and the main business models (freemium, advertising, public service, data licensing).

## Sources

Research date: **2026-09-07**

- Whitepages — https://www.whitepages.com/
- Yellow Pages Australia (Thryv Australia) — https://www.yellowpages.com.au/
- Companies House — https://find-and-update.company-information.service.gov.uk/
- USA.gov — https://www.usa.gov/federal-agencies
- OpenCorporates — https://opencorporates.com/

> Sourcing limitation: help-center and support documentation for the major consumer business directories (and several B2B directories, people directories, and member-directory products) was not reachable from the research environment on the research date; evidence above rests on official home/landing/service pages of the five listed products. Claims are calibrated accordingly: no numeric limits, pricing specifics, review mechanics, or claiming-workflow details are asserted, and capabilities observed at only one product are marked as product-dependent rather than general. Detailed per-product observations, the cross-product comparison matrix, and the failed-source log are in the paired Research Notes.
