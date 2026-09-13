# Library Discovery Platform

## Overview

A **Library Discovery Platform** is a library's patron-facing search layer over the library's resource universe. A patron enters a query and receives a ranked list of bibliographic records — books, journals, articles, e-books, videos, repository items — drawn from the library's own catalog together with the additional sources the library enables (subscriptions, indexes, digital collections). Each record shows how the item can be obtained through this library: read it online, borrow the print copy, request it from another library, or find it on the shelf.

The defining structure is small:

```text
The library's resource universe (library-configured, institution-bound)
└── Query → ranked, refinable bibliographic record results
    └── Per-record obtainability through this library
        (availability + a get-it path)
```

Everything else the market associates with the category — a single search box across catalog and subscription content, facets, relevance ranking, link resolvers, patron accounts, A-Z lists, admin consoles — is widespread in current products but is not what makes the product a discovery platform. A catalog-only search surface with availability and hold placement (the older public-catalog pattern) satisfies the same core with a smaller universe; modern products extend the universe outward.

The platform is a search-and-delivery layer, not an operational system: it does not run circulation, acquisitions, or cataloging. It reads holdings from operational library systems and forwards patron requests into them.

## Users & Context

**Primary users — patrons.** Students, faculty, public-library users, and staff of special libraries (corporate, government, health). They arrive typically from the library's website or from search boxes embedded on institutional pages. Their goal is task-shaped: find materials for a course, locate a known item, explore a topic, and get the item — online or physically.

**Secondary users — library staff.**

- **Systems / e-resources librarians** configure the platform: which sources and databases are searched, how collections display, how access links resolve, which authentication method applies.
- **Access-services / reference staff** depend on the request paths it exposes (holds, interlibrary loan) and troubleshoot what patrons report (broken links, missing availability).
- **Administrators** read usage analytics to understand how the collection is being used.

The work context is one library (or a consortium of libraries sharing a configuration). The platform is public-facing by default: anyone may search, while signing in unlocks personalized and entitlement-dependent actions.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a library discovery platform:

**1. The library's resource universe.** The search domain is institution-bound and library-configured: the library's own catalog holdings plus the sources the library chooses to enable — subscription indexes, open-access content, institutional repository and digital-collection content, and (in some products) live connections to remote databases. The patron searches "what my library can get me," not an unbounded corpus. This is the platform's organizing container and the main structural fact separating it from general scholarly search.

**2. The query → record loop.** A search box (basic or fielded/advanced) returns a ranked list of **bibliographic records** — descriptions of works and resources with title, author, subject, format, publication data. Records are the unit of result; refinement (facets, filters, sort) narrows the list. The loop is the platform's primary interaction.

**3. Per-record obtainability.** Each record carries an availability/access expression and at least one path to obtain the item through this library:

- a link to read the item online (full text, e-book, streaming media)
- the print copy's location and loan status (which branch, on shelf / on loan)
- a request action (place a hold, request via interlibrary loan)
- shelf-position help for physical items

The success condition of the Type is "get this item from my library" — not merely "find a description of it."

### Standard Capabilities

Mature products commonly add the following. They make the platform practical; they do not define it.

- **Multi-source aggregation behind one search box** — the modern "web-scale" pattern: catalog records, indexed subscription content, repository items, and digital collections searched together, with results merged into one list.
- **Facets and refinement** — availability, material type, date, subject, author, language, library/branch, source database.
- **Relevance ranking**, usually tunable by the library.
- **Full-text link resolution** — when a record's item is held in a subscription, an access link is computed from the library's holdings data (knowledge base) and routed through the library's access machinery (link resolver, proxy).
- **Patron sign-in and personalization** — saved items and lists, search history, alerts; sign-in also unlocks requests.
- **Request actions** — holds on print items, interlibrary-loan requests for items the library does not hold, course-reserve visibility.
- **Record detail** — full bibliographic data, editions and formats of the same work grouped or linked, citation export, persistent links, sharing.
- **Enrichment** — cover images, reviews, author information, similar-item suggestions.
- **A-Z list** — a companion surface listing the library's e-journal and database holdings by title.
- **Admin console** — source and collection configuration, display customization, usage analytics.
- **Authentication integration** — proxy servers, federated identity, IP recognition, institutional sign-in.
- **Embeddable search boxes** on the institution's web pages.

### One Structure, Many Implementations

The core is written conceptually. Implementations vary:

```text
Concept:  The library's resource universe
Implementations:
  - the library's own catalog only (the thin, older edge of the Type)
  - catalog + a shared central index of publisher/content-provider metadata
  - catalog + locally built index of harvested sources
  - catalog + live connections queried in remote databases at search time

Concept:  Availability expression
Implementations:
  - live status queried from the circulation system at display time
  - holdings and location data loaded from library holdings records
  - entitlement-derived access links from a knowledge base

Concept:  Get-it path
Implementations:
  - direct full-text link / one-click access
  - OpenURL link resolver
  - hold request into the circulation system
  - interlibrary-loan request into a resource-sharing service
```

A reader who has only seen a modern central-index product should still recognize a catalog-only discovery layer as the same Type at its thin edge.

## How It Works

### The search loop

```text
Patron enters a query (basic box or advanced/fielded form)
→ the platform searches the configured universe
→ results return as a ranked record list
→ patron refines with facets/filters or revises the query
→ patron opens a record
```

Ranking balances relevance signals in the metadata; libraries can commonly tune ranking and display to local needs. Where results from different source types merge into one list, products typically group or deduplicate different versions of the same work and show a representative record with its availability.

### The get-it decision

Opening a record leads to the access panel — the platform's decisive surface:

```text
Record
→ What does my library offer for this item?
   ├─ available online → access link (direct or via resolver/proxy)
   ├─ print copy held → branch / shelving location + loan status (+ shelf map in some products)
   ├─ not held, but requestable → hold or interlibrary-loan request
   └─ nothing available → alternative suggestions (editions, formats, other databases)
```

Which options appear depends on the library's holdings, subscriptions, and configuration — the same record can show different access options at different libraries.

### Signed-in actions

Searching is usually open to everyone. Actions with consequences — placing a hold, making an interlibrary-loan request, and in most products saving to personal lists — require signing in with the library account. The request is then handed to the operational system that fulfills it; the discovery platform records the patron's action and typically shows its status afterward.

### The configuration loop (library side)

```text
Library selects sources/databases to search
→ connects holdings and subscription data (knowledge base, catalog records, local holdings)
→ configures display, facets, ranking, access links, authentication
→ embeds search boxes on library web pages
→ monitors usage analytics and patron-reported problems (e.g., broken links)
```

This loop is continuous: subscriptions change, holdings change, and the discovery universe follows.

## Interfaces

### Search home / search box

The entry surface, usually the library's most prominent search element.

- a basic search box (often with an advanced-search link)
- scope or database selection in some products
- primary actions: search, open advanced search

### Results list

The record list with refinement.

- ranked records with title, author, format, availability hints, source label
- facet panel (availability, format, date, subject, language, library, database)
- primary actions: refine, sort, open a record, save an item, cite/share

### Record detail

The full description of one work or resource.

- complete bibliographic data, subjects, notes; editions/formats of the same work
- the access panel: online links, holdings and loan status, request buttons
- primary actions: access online, place hold, request via ILL, save, cite, share, locate on shelf

### My account

The patron's personal surface.

- saved items and lists, search history and alerts, current requests/holds (where the platform shows them)
- primary actions: sign in, manage lists, review requests

### A-Z list

Companion directory of the library's e-journals and databases by title.

- browse/search by title; per-title access links and coverage
- primary actions: find a specific journal or database, access it

### Admin console

The library-side configuration surface.

- source/database selection, collection and holdings connections, display and ranking settings, authentication setup, usage analytics
- primary actions: configure sources, adjust display/ranking, review reports

## Important Rules / Behaviors

- **The universe is configured, not crawled.** What patrons can find is determined by what the library enabled. A missing subscription or unconfigured collection is invisible to the search, not merely unlinked.
- **Availability is live and external.** Loan status and access rights come from other systems (circulation, knowledge base, subscriptions) at display time. Stale or missing connections surface as patron-visible problems — wrong availability, missing full-text links, broken links — which libraries actively troubleshoot.
- **Entitlement gates access, not discovery.** Records for items the library does not own may still appear (from indexes or as requestable items); what changes is the get-it path — access links appear only where the library is entitled, and requests take over where it is not.
- **Guest vs signed-in.** Search and discovery are typically open; consequential actions (holds, ILL, and in most products saved lists) require sign-in with the library account.
- **Requests are handed off, not fulfilled.** The platform records the patron's request and forwards it to the operational system; fulfillment status lives in that system.
- **Same work, many records.** Editions, formats, and copies of a work may exist as multiple records across sources; products commonly group or link them and show availability per version.
- **Access links can break.** Because links are computed from holdings data against live publisher platforms, products provide patron-facing "report a problem" paths and staff-side diagnostics.

## Variants

- **By segment** — academic libraries (the largest market), public libraries, schools, and special libraries (corporate, government, health). Segment shapes the universe (scholarly indexes vs popular reading vs internal knowledge) and the access model.
- **By index architecture** — shared central index of provider metadata; locally built index of harvested sources; live metasearch of remote databases; or a catalog-only universe. Many products combine these.
- **By suite pairing** — discovery sold as part of a same-vendor library platform (deep integration with that vendor's ILS) vs vendor-neutral discovery that connects to any ILS and any link resolver.
- **By deployment** — vendor-operated cloud service vs self-hosted open source.
- **By scale** — single institution vs consortium or national-scale deployments where member libraries share a universe while keeping local holdings and branding.
- **By access posture** — fully open public instance vs institution-restricted instance (common for corporate and government libraries).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Integrated Library System / ILS | operational counterpart | the ILS is the system of record for cataloging, circulation, acquisitions, and patron management; the discovery platform is the search-and-delivery layer that reads its data and forwards requests into it. Remove circulation/acquisitions from the ILS and the catalog/discovery layer is what remains |
| Academic Search Engine | nearest sibling | corpus-bound and institution-independent: a global scholarly corpus where entitlement is an access aid. The discovery platform is institution-bound: its container is the library's catalog + subscribed holdings, and its success condition is obtaining the item through the library |
| Digital Library Platform | source, not peer | hosts one institution's digital collection end-to-end (ingest, curation, delivery); the discovery platform indexes and searches across many such sources without hosting the items |
| Digital Collection Portal | publisher, not peer | publishes a specific corpus of collection-item records with media and rights for public access to collections; the discovery platform performs bibliographic resource discovery with holdings/entitlement paths |
| Vertical Search Engine / Metasearch Engine | technology overlap | generic search over a vertical with no library container, no holdings/entitlement machinery, and no request actions |
| Reference Manager | complementary | the individual's personal bibliographic tool; discovery platforms export citations into it |
| E-book Library Application | personal counterpart | the individual's own purchased/borrowed e-book collection; no institutional universe or entitlement machinery |
| Public Data Portal | different domain | publishes datasets for public reuse; no bibliographic records, holdings, or request paths |

The two most important boundaries: against the **ILS** (operations vs search layer — the two are partners, and the discovery platform is often a separate product paired with an ILS) and against the **Academic Search Engine** (institution-bound vs corpus-bound — the gradient is real, and the test is whether the library's holdings and get-it paths are the organizing container or merely an access aid).

## Representative Products

- **Primo / Primo VE** (Ex Libris, Clarivate) — central-index academic discovery service, tightly paired with the Alma library platform; VE variant for smaller institutions
- **Summon** (Ex Libris, Clarivate) — provider-neutral discovery layer for libraries of all sizes and types
- **WorldCat Discovery** (OCLC) — cooperative, catalog-centric discovery over WorldCat plus a content-neutral central index; pairs with WorldShare Management Services and other ILS
- **EBSCO Discovery Service** (EBSCO) — index-based discovery with vendor-neutral knowledge base/link resolver choice; broad segment spread
- **VuFind** (Open Library Foundation) — open-source discovery system spanning catalog-only to multi-source deployments; the historical/regional anchor

## Sources

Research date: **2026-09-08**

- OCLC Support — WorldCat Discovery help center (Get started; Configure; Display local data; Search; Search results; Reserve and request items): https://help.oclc.org/Discovery_and_Reference/WorldCat_Discovery — and Introduction to WorldCat Discovery: https://help.oclc.org/Discovery_and_Reference/WorldCat_Discovery/Get_started/Introduction_to_WorldCat_Discovery
- OCLC — WorldCat Discovery overview: https://www.oclc.org/en/worldcat-discovery.html
- VuFind — official site and features: https://vufind.org/vufind/ , https://vufind.org/vufind/features.html
- Ex Libris — Meet Primo: https://exlibrisgroup.com/products/primo-discovery-service/ ; Central Discovery Index: https://exlibrisgroup.com/products/leganto-reading-list-management-system/central-discovery-index-2/ ; Meet Summon: https://exlibrisgroup.com/products/summon-library-discovery/
- EBSCO — EBSCO Discovery Service (academic overview): https://www.ebsco.com/academic-libraries/products/ebsco-discovery-service ; Authentication & Links to Full Text: https://www.ebsco.com/academic-libraries/products/ebsco-discovery-service/authentication-links-to-full-text

> Sourcing limitation: Tier-1 operational help centers were reachable for OCLC and VuFind; for Primo, Summon, and EDS the reachable layer was official product pages (EBSCO's support portal failed to render and was abandoned). Operational details for those three vendors are therefore stated only at positioning level, and no precise numeric limits, defaults, or timing rules appear in this document. Detailed observations and evidence calibration are recorded in the paired Research Notes.
