# Research Notes — Digital Collection Portal

Research date: 2026-09-07

## Research Goal

Understand what a Digital Collection Portal is as a distinct Application Type: what its world consists of (objects, surfaces, roles), who uses it, what workflows it supports, what rules govern it, and where its boundaries lie against Museum/Archaeological Collection Management, Digital Library Platform, Institutional Repository, Library Discovery Platform, Media Asset Management, Online Encyclopedia / Information Portal, Public Data Portal, and Exhibition Planning Platform.

This leaf sits in §27 (Media, Entertainment, Creator & Culture) among the museum leaves. Two prior passes used this Type as a boundary anchor and must stay consistent with it:

- archaeological-collection-management research: "vs Digital Collection Portal: publication surface (…Online Collections) — a slice, usually a separate product/module feeding off the CMS."
- cultural-heritage-asset-management research: "vs Digital Collection Portal / Public Data Portal — portals are publication surfaces fed by a registry of record… Test: no editorial/curation power over the underlying records → portal."
- archaeological-collection-management STATUS flag: portal listed among CMS siblings as a "probable Capability relationship", flagged for joint review when the leaf is processed. **This pass addresses that flag** (verdict recorded in Boundary Findings and STATUS.md).

## Initial Boundary

Initial hypothesis (pre-research):

- A Digital Collection Portal is the public, web-based surface through which an institution's collection (museum objects, artworks, photographs, archival material, specimens) is published for discovery and viewing: search/browse + item detail pages rendering metadata and digital media.
- It is fed by a record system (collections management system, DAM, library platform) or by harvested partner metadata; it does not itself run custody or cataloging workflows (accessioning, storage locations, loans, ingest pipelines).
- Nearest Types: Museum Collections Management (record system), Archaeological Collection Management (record system), Digital Library Platform (§23 — owns items end-to-end and delivers them), Institutional Repository (§23), Library Discovery Platform (§23), Media Asset Management (§27), Online Encyclopedia, Public Data Portal, Digital Goods Store, Web Archive Viewer, Exhibition Planning Platform.
- Key prior tension: the Digital Library Platform pass lists "public collection portal" as one of its interfaces and "publication / exhibition-centered" as one of its variants — the split between the two Types must be drawn at ownership of the item store / curation machinery.

## Research Questions

1. What is the unit of record on a collection portal (item/object/entry/record) and what does a public item page render?
2. Where does the corpus come from — live integration with a record system, export/sync, or harvesting of partner metadata? Does the portal hold its own editorial power over records?
3. What discovery machinery is definitional (search, browse, facets, refine) and what is common presentation (highlights, exhibitions, galleries, stories)?
4. Who are the users — is the primary user really the unauthenticated public visitor? What roles exist on the publishing side?
5. What rules govern publication: selection of what is published, field-level exposure, rights statements, download permissions, access tiers?
6. What interaction does the public get (read-only vs accounts, sets, comments, transcription)?
7. Where is the line against the collections management system / digital library platform that feeds it, and against discovery layers and data portals?

## Representative Products

Selection rationale: different deployment philosophies (companion module vs split open-source front-end vs hosted SaaS publishing vs cross-institution aggregator), different customer tiers (large museums → small institutions and private collectors → national public service), and documented official sources.

1. **eMuseum (Gallery Systems)** — commercial "online collections" publishing companion to the TMS collections-management suite; used by large museums and archives.
2. **Pawtucket (CollectiveAccess / Whirl-i-Gig)** — open-source "front-end" publication and discovery platform, architecturally split from the Providence cataloguing backend.
3. **CatalogIt, HUB & Web Publishing (It Unlimited)** — SaaS cataloging product for small museums, historical societies, and private collectors, with optional public publishing via its HUB and embed/API options.
4. **DigitalNZ (National Library of New Zealand)** — national aggregation portal publishing 30M+ items from 200+ content partners; aggregator philosophy.

Also considered but unreachable during research (see Sources — limitations): Vernon Browser (Vernon Systems), PastPerfect Online (PastPerfect), Europeana, Digital Public Library of America, Lucidea Argus.

## Sources

Fetched successfully (all Layer A — directly observed from official vendor/government sources):

- Gallery Systems — "Online Collections with eMuseum" product page: https://www.gallerysystems.com/products-and-services/emuseum/ (fetched 2026-09-07)
- CollectiveAccess Documentation — welcome page and "Introduction to Pawtucket": https://docs.collectiveaccess.org/ and https://docs.collectiveaccess.org/pawtucket (fetched 2026-09-07)
- CatalogIt — product homepage incl. HUB & Web Publishing: https://www.catalogit.app/ (fetched 2026-09-07)
- DigitalNZ — homepage and About: https://digitalnz.org/ and https://digitalnz.org/about (fetched 2026-09-07)

Could not be fetched (1–2 attempts each, then abandoned per network-restriction rule):

- vernonsystems.com (root and product page returned empty responses)
- pastperfectsoftware.com (transport errors)
- europeana.eu and pro.europeana.eu (HTTP 403)
- dp.la (HTTP 405)
- lucidea.com (HTTP 403)
- eMuseum brochure PDF (response too large; product-page evidence retained)

## Product A — eMuseum (Gallery Systems)

Evidence layer: A (official product page).

Key observations:

- Positioned as "online collections software for museums and collecting institutions that integrates seamlessly with collections management software". Publishing is explicitly a companion role to the record system.
- Publishing scope: "fully configurable layouts, you can create dynamic digital exhibitions and publish them to your public-facing website or intranet" — note the intranet option: the audience is not always the open public.
- Discovery: "robust database searching with Google-like functionality".
- Media: "multiple media types and IIIF functionality" (image deep-zoom delivery standard present in the museum segment).
- Presentation: "look and feel customization" to match the institution's main website; the listed client sites are described as "identical in design and navigation to their institution's main website".
- Governance: "extensive administrative control and multi-level security tools" — access control over what is visible.
- Reach: "multilingual, Unicode-compliant publishing and searching".
- Feed: "full integration with the TMS Suite — eliminate the need for data extraction" — live integration with the collections management system rather than exports.
- Measurement & reuse: analytics for "collection-specific insights"; "flexible API and mobile-enabled software".
- Client roster spans art museums (The Frick Collection), encyclopedic museums (Royal Ontario Museum), archives (Hoover Institution Library & Archives), a national arts foundation (Danish Arts Foundation), university and small museums — the same product shape across collection domains.

## Product B — Pawtucket (CollectiveAccess)

Evidence layer: A (official documentation).

Key observations:

- Suite architecture is explicitly split: "Providence is the core cataloguing application … where data, media and metadata is input, edited, and managed. Pawtucket is the optional, public web-access tool for digital publication and discovery."
- Pawtucket self-described as "an optional 'front-end' publication and discovery platform for collections" and a "multi-faceted storytelling medium".
- Features: responsive mobile-friendly interface; full text search; "highly configurable search and browse interfaces for all record types"; "ability to browse within search results (aka. 'refine your search')"; "configurable detail displays for collection objects and all authorities — you can show as much or as little information from your database as you want"; built-in "galleries" — "simple online exhibitions using curator-defined sets"; user-created comments and presentations; export of search/browse results to PDF, Excel, PowerPoint; theming via CSS and templates.
- The backend/frontend split is the cleanest available proof that "publication + discovery surface" is a separable product half with its own configuration, distinct from cataloging machinery.

## Product C — CatalogIt (HUB & Web Publishing)

Evidence layer: A (official product site).

Key observations:

- SaaS cataloging product ("Collect anything. Catalog everything.") for museums, personal collectors, organizations, conservators; cataloging runs on web/mobile with accession, exhibition, loan, location documentation — the record-system half.
- Publishing is a distinct, optional capability with its own name and page: "Choose to share data through CatalogIt's flexible web publishing options, using the CatalogIt HUB or your own website, using our API, WordPress plugIn, or iframe integration."
- Selection control: "Include only the entries and data you want to share" — publication is a curated subset of the catalog, item- and field-level.
- The HUB is a public surface: "Museums, cultural organizations, community arts organizations, and private collectors use the CatalogIt HUB and Web Publishing capabilities to increase public access to their collections and collection information."
- Presentation is image-centric ("View and access your collections via images rather than lists of text or numbers").
- Customer tier: small historical societies, house museums, congregational and community archives — plus personal collectors; shows the Type extends below institutional scale to a single person's collection.

## Product D — DigitalNZ

Evidence layer: A (official government service site).

Key observations:

- Aggregator portal: "Search 30+ million New Zealand items across 300+ collections in one place"; "established by the National Library of New Zealand in 2008 to make it easier to access digital collections… more than 30 million items from over 200 content partners."
- Partners "range from small community archives to large national repositories"; partners "share their collections and metadata through us" — the portal publishes partner-supplied records rather than holding custody of the underlying objects.
- Content breadth: "photographs, audio recordings, video, maps, newspapers, artworks, research papers, and news articles" — not limited to museum objects.
- Each item has an addressable record page (records/<id>) with attribution and rights (e.g., CC licensing and "no known copyright" notices visible on items).
- Public contribution overlay: "Stories" — users collect found items, add their own text and images, keep private or share — user-generated sets layered over the published corpus without altering partner records.
- Reuse: free public API ("a key to content on DigitalNZ") for building external applications.
- Governance surfaces: terms of use; a dedicated "Copyright, accessibility, and privacy" section.

## Cross-product Comparison

| Dimension | eMuseum | Pawtucket | CatalogIt HUB | DigitalNZ |
|---|---|---|---|---|
| Deployment shape | companion publishing module to a CMS suite | separate open-source front-end of a cataloging suite | hosted SaaS publishing layer over a SaaS catalog | cross-institution aggregator service |
| Corpus source | live integration with the record system ("no data extraction") | the Providence database | the subscriber's catalog (curated subset) | metadata/media shared by 200+ content partners |
| Unit of record | object records | collection objects + authorities | entries | item records (records/<id>) |
| Discovery | Google-like database search | search + configurable browse + refine-within-results | browsing/searching over image-centric views | search across all partners' collections |
| Item page | configurable object displays | configurable detail displays for objects and authorities | entry profiles with images | record page with attribution and rights |
| Curated presentation | digital exhibitions, custom look & feel | "galleries" from curator-defined sets, theming | highlights via HUB profiles | featured collections; user "Stories" |
| Rights / governance | multi-level security tools, admin control | configurable display of database fields | "include only the entries and data you want to share" | per-item rights/attribution, terms of use |
| Public interaction | reading-oriented; analytics on engagement | comments, user presentations, exports | public viewing; optional sharing choices | user Stories (collect, annotate, share), API reuse |
| Audience | public-facing website or intranet | public web | public web | public web |

Observed across the whole sample (Layer B — cross-product commonality):

1. Every product is a **published web surface over a corpus of collection-item records** — the item (object / entry / record) is the unit, individually identified and addressed.
2. Every product provides **search and/or browse over the corpus** plus a **per-item detail view** rendering descriptive metadata; media presentation accompanies records where media exists.
3. Every product implements **publication control**: the institution (or partner) chooses what is published and how much of each record is exposed. This control is always exercised over a feed from a record system — none of the four portals is the system of record for the collection.
4. Every product carries **rights/attribution and terms surfaces** (credit lines, licenses, security tools, terms of use) — legal framing of the published material is structural.
5. Three of four offer **curated presentation layers** (exhibitions / galleries / highlights / stories) built from subsets of the corpus.
6. Three of four expose **programmatic reuse** (APIs); IIIF appears in the museum-focused module as the media-delivery standard.
7. All four are **read-mostly for the audience**; where the public contributes (comments, sets, stories), contributions are overlays and do not modify the authoritative records.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

```text
Published corpus of collection-item records
└── Public discovery surface (search / browse)
    └── Per-item public detail view (metadata + media where available)
        └── for an audience outside the cataloging staff
```

Three invariants; each is individually necessary:

1. **A published corpus of collection-item records** — items individually identified, described by metadata, commonly carrying a digital surrogate (image/audio/video/document). The corpus represents a collection (institutional or aggregated from partners). Without a corpus of collection records the thing is just a website.
2. **A public discovery surface** — search and/or browse open to people who are not the institution's cataloging staff. Without discovery the corpus is an unfindable archive; without the published-surface character the thing is a record system.
3. **A per-item public detail view** — each item renders as its own addressable page showing its description (and media where available). Without item-level views the thing is a highlights brochure, not a portal over the collection.

Role of the portal: it **presents and provides discovery over** the corpus; the authoritative records, custody, and cataloging workflows live in a feeding system (or in partner systems, for aggregators). "No editorial/curation power over the underlying records" is the prior passes' test and is preserved here.

Historical/market-sample check: pre-web collection catalogs on CD-ROM and early hand-authored HTML collection pages satisfy the same three invariants with "published access surface" as the invariant and the web as today's dominant realization (treated like the offline-distribution historical form in the Digital Library Platform pass). Regional products (DigitalNZ), platform-internal deployments (intranet publishing in eMuseum), and single-collector corpora (CatalogIt personal plans) all fit — so nothing modern-market-specific (IIIF, cloud hosting, open-access image downloads) is allowed into the invariant.

### L1 — Common Mature Structure

Very common in current products; not required to recognize the Type:

- faceted filtering / refine-within-results over structured metadata
- structured browse entries (by collection, classification/type, creator, date, place)
- media viewer (zoom/pan for images; players for A/V; IIIF common in the museum segment)
- curated presentation: highlights, featured items, digital exhibitions / galleries / stories from item sets
- rights statements, credit lines, copyright notices, terms of use per item or corpus
- download / share / citation actions where rights allow (open-access image delivery in parts of the museum segment)
- stable, citable item URLs / persistent addressing
- multilingual interface and Unicode content
- usage analytics for the publishing institution
- metadata/media exposure for reuse (APIs; harvesting interfaces in the library/archives ecosystem)

### L2 — Variant / Optional Structure

- **Deployment shape** (the main axis of variation): companion module to a collections system; split front-end of an open-source suite; hosted SaaS publishing layer; aggregator portal over many partners; fully custom-built institutional portal
- audience scope: open public (dominant) vs intranet/subscription/restricted-access deployments
- user accounts and overlays: saved items, personal sets/stories, comments, tagging, crowdsourced transcription
- commerce and service hooks: reproduction/print orders, image licensing requests
- storytelling/exhibition builders beyond simple galleries
- 3D/interactive object display
- offline delivery (CD-ROM-era catalogs — historical form)

### L3 — Vendor-specific Structure

(stays in Research Notes)

- eMuseum: TMS Suite live-integration specifics; "look and feel" theming; named client-site program
- Pawtucket: module list (ban_hammer etc.), Bootstrap-based theming, exports to PDF/Excel/PowerPoint, curator-defined gallery sets as a concrete mechanism
- CatalogIt: HUB as a hosted public domain; WordPress plugin / iframe / API embedding options; per-plan entry/user/storage allowances
- DigitalNZ: Stories tool; API-key developer program; partner onboarding ("Make it Digital"); content-type breadth including newspapers and research papers

## Boundary Findings

1. **vs Museum Collections Management / Archaeological Collection Management (§27)** — the load-bearing boundary, consistent with both prior passes. The record system runs custody and cataloging (accession, numbering, storage locations, movement/loans, condition); the portal publishes selected records for discovery and viewing. Test: strip custody machinery → the portal is unaffected; strip the public discovery surface → the portal is gone and the record system remains. This pass **discharges the prior "probable Capability relationship" flag as follows**: the portal is a real, independently marketed product half (eMuseum is sold as its own product; Pawtucket is separately installable; CatalogIt sells publishing as a named capability; DigitalNZ is a standalone service) — Type status retained, with the module/companion deployment shape documented as dominant rather than disqualifying. Joint review with museum-collections-management (unprocessed) recommended.
2. **vs Digital Library Platform (§23)** — the DLP pass defines its Type with staff curation machinery (add/describe/review/maintain) as definitional, and lists the public portal as one interface and "publication/exhibition-centered" as a variant. The line drawn here: the Digital Library Platform **owns** the item store end-to-end; the Digital Collection Portal is the **publication surface** over records owned elsewhere. Test: remove ingest/describe/approve machinery → DLP collapses; a portal still fully functions on its feed. Products that bundle both halves (CatalogIt, CollectiveAccess) contain both Types in one suite; this pass documents the portal half. Gray zone recorded for joint review in STATUS.md.
3. **vs Institutional Repository (§23)** — submission/deposit workflows and open-access policy machinery are curation; remove them and add public presentation of a curated corpus → portal. Not re-fetched this pass (source constraints); boundary held by structural reasoning from the DLP pass.
4. **vs Library Discovery Platform (§23)** — a discovery layer federates searches over external bibliographic sources; a collection portal publishes a specific corpus of collection item records with media and per-item pages. Aggregator portals (DigitalNZ) sit closer to discovery layers than single-institution portals do — but their unit is still the collection item record with rights/attribution and public media, and their purpose is public access to collections rather than library-resource discovery. Tension noted for joint review.
5. **vs Media Asset Management / DAM (§14/§27 family)** — DAM serves internal asset operations (ingest, renditions, rights, brand workflows); the portal's defining surface faces the external audience. A DAM can feed a portal; the roles differ.
6. **vs Online Encyclopedia / Information Portal (§02)** — encyclopedias publish authored articles; information portals aggregate general content. The collection portal's unit is the individually described collection item (object/specimen/artwork/photograph/document), not authored subject content.
7. **vs Public Data Portal / Government Open Data Portal (§24/§02)** — data portals publish datasets for download/reuse; collection portals publish collection items for viewing and context. Overlap exists (both may expose APIs), but the item page with media and rights/attribution is the portal's center.
8. **vs Digital Goods Store (§05.22) / e-commerce** — commerce (reproduction sales, licensing) is an optional overlay in the sampled products, not the defining structure; a transaction-first surface is a different Type.
9. **vs Exhibition Planning Platform (§27)** — planning tools manage the production of future exhibitions internally; portal exhibitions/galleries are public presentations of already-published subsets of the corpus.
10. **vs Web Archive Viewer (§02)** — archived web page corpora are a specific corpus kind with replay machinery; distinct from general collection item publication.

## Uncertainties

- **Tier-1 operational documentation depth**: for eMuseum and CatalogIt, evidence comes from official product pages (Tier 2), not from deep help centers; the brochure PDF was too large to fetch. Claims about those two products are kept at the level their product pages support; no precise limits, defaults, or configuration internals are asserted for them.
- **Vernon Browser, PastPerfect Online, Europeana, DPLA, Lucidea Argus** could not be fetched; they are cited only as market presence, never as evidence for any structural claim.
- **Non-museum segments** (university special collections portals, natural-history specimen portals, corporate archives portals) are inferred from the sample's breadth (eMuseum's archive/natural-history client types, DigitalNZ's content breadth) rather than from dedicated products fetched this pass; claims kept general.
- **Whether aggregator portals constitute a variant or a separate Type** is genuinely open; recorded as a boundary tension rather than resolved unilaterally.
- **Intranet/restricted deployments** are observed for one product (eMuseum); generalized cautiously as "restricted-access deployments occur" (Layer B for the concept, single-product for the specific evidence).

## Final Synthesis

A Digital Collection Portal is the published web surface of a collection: a public discovery-and-viewing environment over a corpus of individually identified collection-item records, fed by a record system or by partner systems, with publication control and rights framing on the publishing side and read-mostly interaction on the audience side.

The defining structure is exactly three things — a published corpus of collection-item records, a public discovery surface (search/browse), and per-item public detail views — serving an audience beyond the cataloging staff. Everything the market associates with polished portals (IIIF deep zoom, facets, exhibitions, stories, open-access downloads, APIs, multilingual UI) is common mature structure, not definition. Deployment ranges from a companion module of a collections management system to a split open-source front-end, a hosted publishing layer, or a cross-institution aggregator; audience scope is normally the open public with restricted-access deployments as a variant. The Type's identity rests on the publication role, not on any deployment shape: strip the custody/cataloging machinery and a portal still stands; strip the public discovery surface and only the record system remains.
