# Research Notes — Library Discovery Platform

Research date: 2026-09-08
Leaf: Library Discovery Platform (DIRECTORY.md §23 Education, Research & Knowledge Institutions)
Slug: library-discovery-platform

## Research Goal

Understand what a Library Discovery Platform is as an Application Type: what the searchable universe is and who configures it, what the unit of result is, how availability and entitlement work per record, what actions a patron can take on a result, how the platform relates to the ILS and to subscription/knowledge-base machinery, which interfaces exist, and where the boundary lies against neighboring Types — above all Integrated Library System (unprocessed sibling), Academic Search Engine (processed 2026-09-08, left a joint-review flag for this pass), Digital Library Platform (processed 2026-09-07), Digital Collection Portal (processed, left a joint-review flag), Institutional Repository (processed 2026-09-08), and generic Vertical/Metasearch.

## Initial Boundary

- Working hypothesis: a Library Discovery Platform is the library's patron-facing search layer that searches across the library's resource universe (its catalog plus the subscription/indexed sources the library enables) and routes the patron to obtain each item through that library.
- Nearest Types: ILS (operational system of record), Academic Search Engine (corpus-bound discovery), Digital Library Platform (host of one digital collection), Digital Collection Portal (collection-item publishing), Vertical Search Engine / Metasearch Engine (generic), Reference Manager (personal tool), E-book Library Application (personal library).
- The institutional-repository pass (2026-09-08) already framed the ecosystem: "collection host vs circulation operations vs cross-source search layer" — this pass is the cross-source search layer.
- The academic-search-engine pass left this flag: "corpus-bound vs institution-bound discovery — entitlement/access is an aid inside academic search but the organizing container (catalog + subscribed holdings) of library discovery; gradient boundary, flagged for joint review when Library Discovery Platform is processed."
- The digital-collection-portal pass left this flag: "both federate many sources; held apart by unit and purpose (collection-item record with media/rights/attribution and public item pages vs bibliographic resource discovery) — genuine tension noted for joint review."

## Research Questions

1. What is the searchable universe, and who decides what is in it?
2. What is the unit of result, and how are results ranked and refined?
3. How does the platform express availability and entitlement per record?
4. What can a patron do with a result (view online, hold, ILL, save, cite, locate)?
5. What is the relationship to the ILS — what is read, what is written, where do requests go?
6. What role do the central index, knowledge base, and link resolver play?
7. What interfaces exist (search box, results, record detail, account, A-Z list, admin)?
8. What rules matter (authentication modes, guest vs signed-in, access rights, source configuration)?
9. What variants exist (segment, index architecture, suite pairing, deployment)?
10. Historical check: does the definition hold for OPAC-era and open-source products, not just today's central-index services?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

1. **Primo / Primo VE (Ex Libris, Clarivate)** — market-leading academic discovery service; central-index architecture; tightly paired with the Alma library platform (Primo VE for smaller institutions on Alma).
2. **Summon (Ex Libris, Clarivate; ProQuest heritage)** — one of the original "web-scale discovery" services; provider-neutral delivery posture; all library sizes/types.
3. **WorldCat Discovery (OCLC)** — cooperative/catalog-centric philosophy; searches WorldCat (shared bibliographic database) plus a content-neutral central index; pairs with WorldShare Management Services but usable with other ILS; best-documented of the sample (Tier-1 help center reachable).
4. **EBSCO Discovery Service / EDS (EBSCO)** — index-based competitor; explicitly vendor-neutral on ILS and on knowledge base/link resolver choice; broadest segment spread (academic, health care, corporations, public libraries, schools).
5. **VuFind (open source, Open Library Foundation)** — open-source "discovery system"; spans "a basic Library catalog search to a sophisticated dashboard of data from many sources"; the historical/regional anchor for the §24 check.

## Sources

Tier 1 (official operational documentation):

- OCLC Support — WorldCat Discovery help center: https://help.oclc.org/Discovery_and_Reference/WorldCat_Discovery (fetched 2026-09-08)
- OCLC Support — Introduction to WorldCat Discovery: https://help.oclc.org/Discovery_and_Reference/WorldCat_Discovery/Get_started/Introduction_to_WorldCat_Discovery (fetched 2026-09-08)
- VuFind — official site and features page: https://vufind.org/vufind/ , https://vufind.org/vufind/features.html (fetched 2026-09-08)

Tier 2 (official product pages):

- Ex Libris — Meet Primo: https://exlibrisgroup.com/products/primo-discovery-service/ (fetched 2026-09-08)
- Ex Libris — Central Discovery Index: https://exlibrisgroup.com/products/leganto-reading-list-management-system/central-discovery-index-2/ (fetched 2026-09-08)
- Ex Libris — Meet Summon: https://exlibrisgroup.com/products/summon-library-discovery/ (fetched 2026-09-08)
- OCLC — WorldCat Discovery overview: https://www.oclc.org/en/worldcat-discovery.html (fetched 2026-09-08)
- EBSCO — EBSCO Discovery Service (academic overview): https://www.ebsco.com/academic-libraries/products/ebsco-discovery-service (fetched 2026-09-08)
- EBSCO — Authentication & Links to Full Text: https://www.ebsco.com/academic-libraries/products/ebsco-discovery-service/authentication-links-to-full-text (fetched 2026-09-08)

Source-access limitations:

- EBSCO Connect (connect.ebsco.com) failed to render (Salesforce CSS error) on 2026-09-08 — abandoned after one attempt per the retry rule. EDS operational detail therefore rests on product pages only; assertion strength for EDS reduced accordingly.
- Ex Libris Knowledge Center (knowledge.exlibrisgroup.com) was not fetched; Primo/Summon operational detail rests on product pages. No precise operational claims (limits, defaults, timing) are made for Primo/Summon/EDS.
- OCLC and VuFind provided Tier-1 depth; precise operational facts are stated only where directly observed (and are kept in these notes, not promoted to the canonical document).

## Product Observations

### Primo (Ex Libris / Clarivate) — evidence layer A (product pages), positioning-level

- Positioned as "a Library Discovery Service"; described as "the entry point to your library's collection."
- Content exposure via the Central Discovery Index (CDI): "discovery of commercial and Open Access content available through the Ex Libris Central Discovery Index (CDI) as well as library local resources." Coverage described as journal articles, ebooks, videos, reviews, legal documents; aggregated from a provider network and enriched by a metadata-librarian team; records carry subject terms, controlled vocabularies, author keywords, A&I metadata, CrossRef DOIs, peer-reviewed indicators.
- Library-side control: "advanced harvesting and normalization tools, adjust how collections are displayed and fine-tune search result rankings to meet local needs."
- Integration: "seamless integrations with Alma and other library solutions," open APIs; "designed for both individual institutions and consortia."
- Unique/local content surfaced via "showcases and special collections"; analytics "to demonstrate value to decision-makers."
- Primo VE variant for smaller institutions (deployed with Alma); Primo Research Assistant (generative AI, RAG, grounded in CDI) as an era-current add-on.

### Summon (Ex Libris / Clarivate) — evidence layer A (product page), positioning-level

- Positioned as a "Library Discovery Layer … connecting patrons to academic content"; "improves the discovery of your library's collection and institutional resources."
- Universe: "content from your electronic subscriptions, print collections, Open Access sources, and unique institutional repositories in one simple intuitive interface."
- Breadth claim: "supports libraries of all sizes and types … integrates with dozens of library systems."
- Delivery: "multiple pathways for connecting users to content. Quicklinks offer one-click, direct access … and OpenURL is a reliable standard. Summon is provider-neutral, but you may prioritize content sources as needed."
- Admin: "integrated resource management … robust search analytics through extensive but easy-to-use administrative tools."
- Summon Research Assistant (generative AI grounded in CDI) as era-current add-on.

### WorldCat Discovery (OCLC) — evidence layer A (Tier-1 help center + product page)

- Definition (help center): "a cloud-based application that helps people easily find resources available at their library and in libraries worldwide through a single search. Library users and staff use their WorldCat Discovery instance to search the WorldCat database, to identify materials they need, and to see where they are available."
- Universe: WorldCat (shared bibliographic database; product page cites 610M+ records) + a "content-neutral central index" (product page cites 3,428+ collections, 4B+ items) + metasearch "remote databases" + knowledge-base collections; NISO Open Discovery Initiative support cited for content neutrality.
- Get-it mission (product page): "Connect people to the resources they identify, whether they access the full text electronically, get a print copy in your library, request items through interlibrary loan, or buy them from a content provider."
- Configuration surface (help center): configure databases to search; configure content/staff/patron-facing features; knowledge base collections and metasearch content databases; proxy settings; account roles; holdings audience levels; Google Analytics integration.
- Local data display: A-Z List; full-text link display; local bibliographic data (LBD) and local holdings records (LHR) field mapping; display order of branches/shelving locations/items; "Report a broken link"; fulfillment and discovery options; chat with a librarian.
- Search: query syntax; filter and refine; advanced search; "Search the Central Index and Remote Databases"; search history, saved searches, alerts.
- Results: browse the shelf; locally held formats; format display; editions and formats; "representative record and availability display on grouped search results"; saved items and personal lists; share records and create citations; StackMap locate; LibKey integration.
- Requests: hold requests; item status display in the OPAC; course reserves; ILL request button (EZproxy/OpenAthens-aware; Z39.50 ILL linking to SHAREit documented).
- Access control: institutions can restrict the whole instance (Hosted EZproxy + IP policies, or IP-only); sign-in required for actions such as placing a hold or making an ILL request; session-timeout behavior documented (25 min inactivity + 5 min countdown — product-specific precise fact, kept here only).
- Integration: WorldShare Collection Manager as the knowledge base; link resolution for e-content; search boxes for institution web pages.

### EBSCO Discovery Service (EBSCO) — evidence layer A (product pages), positioning-level

- Positioned as "an all-inclusive search solution"; "Unlock the power of your library's collection and improve the end-user search experience."
- Stated features: sophisticated search (rich metadata, relevance ranking); "Direct Access to Full Text — one-click access directly through the results list"; intuitive interface; integrations with multiple platforms.
- Authentication: OpenAthens single-login support.
- Access machinery: "Your Choice of Knowledge Base and Link Resolver" — EDS "may be powered by SFX, Uresolver, 360 Link and others"; EBSCO's Full Text Finder described as knowledge base + holdings management + publication finder + journal browsing + link resolver.
- Segment spread: dedicated EDS pages for academic libraries, health care, corporations, public libraries, schools.

### VuFind (open source) — evidence layer A (official site, Tier-1)

- Self-description: "a discovery system designed and developed for libraries by libraries … enable your users to search and browse through all of your resources in a single consistent and user-friendly interface."
- Universe: "Catalog records, Institutional repository content, Open access journal articles, Digitized library materials, Websites, Items available for interlibrary loan, Licensed content (where supported by providers), Other collections and resources — just add metadata!"
- Architecture: "completely modular … from a basic Library catalog search to a sophisticated dashboard of data from many sources. It supports building a local index and/or integrating with a variety of existing third-party services."
- Features: faceted results from a basic search box; "Real Time Record Status and Location Information — live status of a record through real-time querying of the underlying catalog system"; "More Like This"; favorites lists (private or public, shareable via URL); browse mechanisms (alphabetical heading browse, facet-driven category browse, channels); persistent URLs; Zotero/reference-manager compatibility (COinS, exports); 30+ interface languages; OAI-PMH/APIs/Solr backend; third-party enrichment (covers, reviews, author bios).

## Cross-product Comparison

| Aspect | Primo | Summon | WorldCat Discovery | EDS | VuFind |
|---|---|---|---|---|---|
| Self-positioning | library discovery service; entry point to the collection | discovery layer connecting patrons to academic content | single search of library + worldwide collections | all-inclusive search solution | discovery system for libraries |
| Search universe | central index (CDI) + local resources | subscriptions + print + OA + IR | WorldCat + central index + metasearch remote DBs + KB collections | EBSCO index + library collection | local index and/or third-party services; catalog + IR + OA + digitized + websites |
| Result unit | bibliographic records | bibliographic records | bibliographic records (WorldCat + central-index records) | records | records |
| Availability expression | via Alma/ILS integration | via library-systems integration | live availability; LHR/LBD; OPAC status | via KB/link resolver | real-time query of the underlying catalog |
| Get-it paths | link resolution (SFX family); requests via paired ILS | Quicklinks + OpenURL | access online / print copy / ILL / purchase | one-click full text; OpenURL via chosen resolver | links; ILL items in scope |
| Patron personalization | (via paired platform) | (admin-oriented) | My Account: saved items, personal lists, search history, alerts | (institution auth) | favorites lists, public/shareable |
| Admin surface | harvesting/normalization, display, ranking tuning | admin tools, analytics | service configuration: databases, features, roles | KB/link-resolver choice, customization | configuration, facets, modules |
| Segment emphasis | academic (VE for smaller) | all sizes/types | academic + public + national | academic/health/corp/public/schools | any library |
| Deployment | SaaS | SaaS | cloud | SaaS | self-hosted open source |

Cross-product commonalities (evidence layer B):

1. All five describe themselves as the library's search layer over the library's own resource universe — the universe is institution-bound and library-configured.
2. All five return bibliographic records (works, editions, articles, ebooks, videos, repository items) — not web pages, not collection-item pages.
3. All five express, per record, how the patron can get the item through this library (online access link, print availability, request/ILL path).
4. All five are configured by the library (which sources are searched, how results display, how access links resolve).
5. All five integrate with an operational library system (ILS) and/or knowledge base/link resolver for availability and fulfillment.
6. All five provide refinement (facets/filters) and a record-detail surface.
7. All five sit on the library's website as the primary entry point (search boxes embeddable on institution pages — documented for WorldCat Discovery, marketed by Summon/Primo).

Divergences (implementation, not Type):

- Index architecture: shared central index (Primo CDI, Summon, EDS, WorldCat central index) vs locally built index (VuFind) vs live metasearch of remote databases (WorldCat metasearch content databases).
- Suite pairing: same-vendor ILS pairing (Primo+Alma, WorldCat Discovery+WMS) vs vendor-neutral over any ILS (EDS, Summon, VuFind).
- Personalization depth varies (WorldCat Discovery and VuFind document patron accounts; Primo/Summon delegate to the paired platform or admin tooling).
- AI research assistants appear in the Ex Libris products (era-current add-on; not observed in the OCLC/VuFind surfaces fetched).

## Canonical Model (L0–L3)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Library Discovery Platform:

1. **The library's resource universe as the configured search domain.** The search domain is institution-bound: this library's own holdings (catalog) plus the additional sources this library enables (subscriptions, repositories, digital collections). The library decides what is in the universe. Remove the institution-bound container → corpus-bound academic search or a generic vertical search.
2. **Query → bibliographic record results over that universe.** A search loop that takes a patron query and returns a ranked, refinable list of bibliographic records describing works/resources. Remove the search loop → an A-Z list / source directory / browse-only portal.
3. **Per-record obtainability through this library.** Each record carries an availability/access expression and at least one path to obtain the item via this library — view online, get the print copy, request/hold/ILL, or locate on shelf. Remove the obtainability leg → an academic search engine scoped to library sources; the "get it from my library" success condition is gone.

Jointly-held is load-bearing:

- 1 alone = a configured source list (A-Z directory)
- 2 without 1 = academic search engine / generic search
- 3 without 1+2 = a link resolver / request form
- 1+2 without 3 = library-branded academic search
- 1+3 without 2 = browse-only catalog with availability
- 2+3 without 1 = a search engine with access links (Google-Scholar-with-library-links shape)

### L1 — Common Mature Structure

Present in most modern products; not required to recognize the Type:

- One search box across multiple source types (local catalog + central index + institutional repository/digital collections + remote databases) — the "web-scale discovery" pattern
- Facets/filters (availability, format/material type, date, subject, author, language, library/branch, source database)
- Relevance ranking, locally tunable
- Full-text link resolution (OpenURL link resolver + knowledge base) and direct publisher links
- Patron sign-in and personalization (saved items/lists, search history, alerts)
- Request actions: holds, ILL, course-reserve visibility
- Record detail with editions/formats grouping, citation export, persistent URLs, sharing
- Enrichment (cover images, reviews, author bios, similar-item suggestions)
- A-Z e-resource list as a companion surface
- Admin console: source/collection configuration, display customization, analytics
- Authentication integration (EZproxy, OpenAthens, IP ranges, institutional SSO)
- Embeddable search boxes on institution web pages

### L2 — Variant / Optional Structure

- Segment: academic / public / school / special (corporate, government, health)
- Index architecture: shared central index vs local index vs live metasearch of remote databases
- Suite pairing: embedded in a same-vendor library platform vs vendor-neutral over any ILS
- Deployment: vendor SaaS vs self-hosted open source
- Consortial / national-library scale deployments (shared universes across member libraries)
- AI research assistants / natural-language search (era-current add-ons)
- Access-restriction posture: fully open public instance vs institution-restricted instance (documented for special/corporate/government libraries)

### L3 — Vendor-specific (research notes only)

- Ex Libris CDI, SFX, Quicklinks, Primo VE, NDE UI, Primo/Summon Research Assistant branding
- EBSCO Full Text Finder, OpenAthens pairing
- OCLC WorldCat, WorldShare Collection Manager, LBD/LHR machinery, FirstSearch lineage, Z39.50 ILL linking to SHAREit, session-timeout numbers (25+5 min), holdings audience levels
- VuFind Solr backend, channels, COinS embedding
- LibKey, StackMap (third-party integrations surfaced inside discovery results)

## Historical / Market-Sample Check (§24)

- **OPAC (online public access catalog)** — the ancestor. A catalog-only search surface with availability display and hold placement satisfies all three L0 legs with the universe = the library's own catalog. VuFind explicitly spans "a basic Library catalog search" to "many sources," confirming that catalog-only deployments sit at the thin edge of this Type rather than outside it. Therefore the L0 must NOT require a central index, multi-source federation, or any modern capability.
- **Older federated-search predecessors** (live metasearch across databases via connectors) satisfy the L0 in a weaker form (universe + query + access paths); the central-index pattern is the modern implementation that made cross-source search fast and complete — an implementation, not the invariant.
- **Regional/national products** (e.g., national discovery catalogs documented by OCLC news) fit the same core with consortial universes.
- Conclusion: the defining core is phrased as institution-bound universe + query→records + obtainability; "one search box across catalog + central index + local digital content" is held as the common mature realization of the modern category, not the definition.

## Vendor-specific Findings

- Primo/Summon Research Assistant (generative AI over CDI) — vendor-specific era-current add-on.
- WorldCat Discovery's WorldCat-record vs central-index-record distinction and "best fulfillment option" toggle — product-specific machinery.
- EDS's "choice of knowledge base and link resolver" positioning — vendor-specific commercial posture, but it evidences the general fact that discovery services are provider-neutral on access machinery.
- VuFind's public/shareable favorites lists and channels — product-specific implementations of personalization/browsing.

## Boundary Findings

1. **vs Integrated Library System (ILS)** — the ILS is the operational system of record (cataloging, circulation, acquisitions, patron management). The discovery platform is the patron-facing search-and-delivery layer over sources: it reads catalog/holdings data and forwards requests (holds, ILL) into operational systems, but it does not run circulation/acquisitions workflows. Test: remove circulation/acquisitions operations from an ILS → what remains is the catalog/discovery layer; remove the search layer from the discovery platform → nothing patron-facing remains. The ILS's public OPAC module is the thin ancestor of this Type; the modern discovery platform is the same patron-facing surface extended beyond the catalog and commonly packaged as a separate product (paired or vendor-neutral).
2. **vs Academic Search Engine** — corpus-bound vs institution-bound. The academic search engine's corpus is a global scholarly corpus independent of any institution; entitlement appears only as an access aid. The discovery platform's organizing container is the library's catalog + subscribed holdings, and its success condition is "get this item from my library." Test: remove the library's holdings/entitlement → the academic search engine still stands; remove the global corpus → it collapses into a library catalog/discovery. Gradient boundary acknowledged (both surface scholarly records); this pass RATIFIES keep-both and discharges the academic-search-engine joint-review flag.
3. **vs Digital Library Platform** — the digital library platform hosts one institution's digital collection end-to-end (ingest, curation, delivery); the discovery platform searches across many sources and does not host the items it surfaces. A digital library platform is one of the sources a discovery platform indexes. Test: remove the hosted item store and search external indexes instead → discovery platform.
4. **vs Digital Collection Portal** — the collection portal publishes a specific corpus of collection-item records with media, rights, and attribution for public access to collections; the discovery platform performs bibliographic resource discovery with obtainability paths. Aggregator portals federate many sources but their unit is the collection-item record, not the bibliographic record with holdings/entitlement. Tension discharged: keep-both, unit-and-purpose seam.
5. **vs Vertical Search Engine / Metasearch Engine** — generic search over a vertical with no library container, no holdings/entitlement machinery, no request actions. The discovery platform's defining difference is the institutional container and the get-it path, not the search technology.
6. **vs Reference Manager** — personal bibliographic tool for the individual's own library vs institutional discovery of the library's resource universe. Discovery exports citations to reference managers; they are complementary.
7. **vs E-book Library Application / Reading Library Application** — the individual's personal collection vs the institution's resource universe; no entitlement/holdings machinery in the personal Types.

## Uncertainties

- Primo/Summon/EDS operational detail (admin configuration model, account behavior, exact availability mechanics) rests on product pages; Tier-1 help centers were not reachable for these vendors on 2026-09-08. No precise operational claims are made for them in the canonical document.
- Whether the patron account lives in the discovery product or in the paired ILS varies by product pairing; only WorldCat Discovery and VuFind document patron-facing account behavior directly in the fetched sources.
- The exact boundary behavior of "metasearch remote databases" (live querying) vs central-index coverage in WorldCat Discovery is documented at the help-center level but not exercised; treated as an implementation variant.
- AI research assistants are documented only for the Ex Libris products in this sample; their spread across the Type is unverified.

## Final Synthesis

A Library Discovery Platform is the library's patron-facing search layer over the library's resource universe. Its defining core is three jointly-held structures: (1) the institution-bound, library-configured search universe (the library's catalog plus the sources the library enables); (2) the query → ranked, refinable bibliographic-record results loop over that universe; (3) per-record obtainability through this library — availability expression plus at least one get-it path (view online, print copy, request/hold/ILL, shelf locate). Everything the market associates with the category — one search box across catalog + central index + repositories, facets, relevance ranking, link resolvers and knowledge bases, patron accounts, A-Z lists, admin consoles, AI assistants — is common mature structure layered on that core, and varies by product philosophy: central-index suite leaders, provider-neutral index services, cooperative catalog-centric services, and open-source discovery layers. The Type's edges: toward the ILS (operations vs search/delivery layer), toward the Academic Search Engine (institution-bound vs corpus-bound), toward the Digital Library Platform / Digital Collection Portal (host/publisher of one corpus vs search layer over many), and toward generic Vertical/Metasearch (no library container, no get-it path).
