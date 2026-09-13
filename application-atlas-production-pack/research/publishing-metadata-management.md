# Research Notes — Publishing Metadata Management

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Book Publishing Management, Publishing Editorial Workflow, Book Distribution Management, Author Management Platform, Magazine / Periodical Management — all processed; nearby: Media Asset Management, Royalty Management Platform)

Research date: 2026-09-10

## Research Goal

Understand what a Publishing Metadata Management application actually is as an Application Type: what object it centers on, what work users do to that object, how records reach the book trade, what quality machinery exists, and where the boundary lies against Book Publishing Management (which also holds title data), Book Distribution Management (which also sends ONIX), Publishing Editorial Workflow, generic PIM/DAM/MDM, and library cataloging.

This pass carries a mandatory joint-review duty: the Book Publishing Management pass (2026-09-06) flagged the title-record seam — "title data records, quality checks and ONIX export are standard capabilities inside publishing management suites; the metadata leaf should center on the data itself as primary object (consistent with the line drawn in book-distribution-management research from the other side)". The Book Distribution Management pass (2026-09-06) independently held that "metadata distribution to trading partners — Firebrand Eloquence pattern — is the metadata leaf's territory".

## Initial Boundary (hypothesis before research)

- Core use hypothesis: the publisher-side (and distributor/aggregator-side) system for creating, maintaining, quality-controlling, and delivering bibliographic product data — the record itself is the deliverable.
- Nearest neighbors: Book Publishing Management (title as commercial record with lifecycle/money), Book Distribution Management (trade operation: orders/stock/dispatch), Publishing Editorial Workflow (content process), PIM/DAM/MDM (generic product data / assets / master data), library cataloging (MARC, receiving side).
- Unknowns: does a standalone market exist beyond suite modules and ONIX tools? Is quality control definitional or common? Is delivery definitional? What is the receiving side's relationship to this Type?

## Research Questions

1. What exactly is the central object — a "title record", a "product record", a "metadata record"? How do work/edition/format/ISBN relate inside it?
2. What does the work consist of: authoring, enrichment, validation, transformation, delivery, monitoring?
3. What standards does the Type implement (ONIX 2.1/3.x, Thema, BIC, BISAC, MARC) and how tightly is the Type bound to ONIX specifically?
4. What quality machinery exists (schema validation, completeness scoring, mandatory vs best-practice checks, integrity checks, certification)?
5. How does delivery work (feeds, schedules, update triggers, per-recipient configuration, transmission methods, full vs incremental sends)?
6. Who operates it (metadata managers at publishers, distributors, aggregators, small publishers, self-published authors)?
7. What postures exist: standalone tool, distribution service, registry submission, national aggregator, suite module?
8. Where is the line against Book Publishing Management's title database, against Book Distribution Management's ONIX feeds, and against generic PIM?

## Representative Products

Selected for market coverage across four distinct postures and customer tiers, all with reachable official documentation:

| Product | Posture | Customer tier / philosophy |
|---|---|---|
| Firebrand Technologies — Eloquence on Demand | publisher-side metadata & asset distribution service | enterprise publishers; managed-service philosophy ("Gold Standard since 1996") |
| ONIXEDIT (Pro / Cloud / Server) | standalone ONIX toolchain: desktop editor → cloud editor → enterprise server | small publishers ($15/mo cloud) to distributors/aggregators (Server); tool philosophy |
| NielsenIQ BookData — Title Editor | registry submission surface (books-in-print database) | independent publishers & self-published authors (free); registry philosophy |
| BookNet Canada — BiblioShare (+ Webform) | national non-profit aggregation & certification infrastructure | Canadian market; shared-infrastructure philosophy |
| Stison (Onix Pre-Flight, Bibliographic Data Feeds) | metadata machinery inside a publishing management suite | SMB publishers; suite-module pole (cross-checks the sibling boundary) |

Cross-references from processed sibling passes (evidence inherited, marked per case): Klopotek Metadata Management apps, Consonance ONIX export/data quality, Firebrand TME "Editorial & Metadata Management" area, EDItEUR ONIX standard definition.

## Sources

- Firebrand — https://firebrandtech.com/eloquence-on-demand (fetched 2026-09-10); navigation surfaces for Eloquence on Alert / Flywheel / FlightDeck / trading-partners observed in page nav
- ONIXEDIT — https://www.onixedit.com/ (fetched 2026-09-10)
- NielsenIQ BookData — https://nielseniq.com/global/en/landing-page/nielseniq-bookdata-publish/ ; https://nielseniq.com/global/en/landing-page/nielseniq-bookdata-publishers/ ; https://www.nielsenisbnstore.com/documents/Important_Notes_For_Publishers.pdf ; video-tutorials landing page (fetched 2026-09-10 via search snapshots)
- BookNet Canada — https://booknetcanada.ca/standards/ ; https://www.booknetcanada.ca/bibliographic-data-distribution ; https://www.booknetcanada.ca/biblioshare-sign-up ; https://www.booknetcanada.ca/onix-standards ; https://booknetcanada.atlassian.net/wiki/display/UserDocs/ONIX+3.0+and+2.1+--+What+it+means+for+BiblioShare+data+aggregation+service+users (fetched 2026-09-10 via search snapshots)
- Stison — https://stison.zendesk.com/hc/en-us/articles/360008486353-Onix-Pre-Flight-Report ; .../40728201688593-Destination-Reports ; .../360002356377-Trouble-Shooting-Issues-with-ONIX-Feeds ; .../115000262144-Setting-up-Automated-ONIX-Feeds ; .../40678737532305-Introduction-to-Bibliographic-Data-Feeds (fetched 2026-09-10 via search snapshots)
- Sibling passes (2026-09-06/08/09): research/book-publishing-management.md, research/book-distribution-management.md, research/publishing-editorial-workflow.md — for cross-referenced observations and the joint-review flags

## Product Observations

### Firebrand Technologies — Eloquence on Demand — evidence layer A (official product page, fetched)

- Positioning: "The publishing industry's Gold Standard for global metadata and asset distribution since 1996"; category in vendor nav: **"Metadata and Asset Management"** (alongside Flywheel, FlightDeck; separate from "Publishing Workflow and Project Management" = TME).
- Purpose statement: distribute "richly formatted metadata, cover images, and digital assets to more than 600 retailers, wholesalers, distributors, libraries, and trading partners worldwide" (vendor metric); "Automate complex ONIX creation and delivery… ensure your product information remains consistent across every sales channel."
- **Authoring/maintenance**: "You simply maintain your core title information in the system, and we automatically generate and transmit the correct ONIX version required by each specific trading partner" (ONIX 2.1/3/custom handled by the service). Multiple ISBNs per work: "link multiple formats of the same work together. The system assigns ISBNs from your prefix blocks and propagates all key bibliographic information from the primary format (e.g., print) to the secondary formats (e.g., ebook, audio)." Tracks "multiple price types in multiple currencies, alongside robust author and contributor information, in one centralized location."
- **Quality**: "vetting your title information through built-in verification controls prior to distribution"; "weekly feedback reports and a complete distribution history so you can proactively address data issues before they reach retailers."
- **Delivery**: "hourly, daily, or weekly metadata feeds in ONIX 2.1, ONIX 3, or custom formats"; "automated delivery triggers or… emergency real-time feeds"; "more than 200 individual channel settings and data customizations" per trading partner (vendor metric); "partner-specific metadata distributions based on the format(s) and sales rights that each partner accepts"; "intelligent outbox for re-sending updated metadata and asset changes to appropriate partners"; "automatic monthly full data sends"; selective title feeds; ONIX delivery to NetGalley for pre-publication titles.
- **Assets**: "Securely manage and deliver a wide variety of digital files, including cover images, interior spreads, EPUBs, and audiobook files… in a single, accessible hub" (Elite tier: all content assets storage and distribution — ebook/POD/audiobook/marketing assets).
- **Audit**: "comprehensive Title History, which serves as an audit trail to track changes made to your title information"; "detailed distribution history and full audit of file transfers, so your leadership team always knows exactly what data and cover images were sent to which partner."
- **Integration**: "built directly into Title Management, allowing you to release approved title data and assets with a single click. If you use a different internal database, you can also set up automated imports via spreadsheets or API feeds."
- **Standards participation**: vendor states active participation in EDItEUR (ONIX) and BISG; support for "Thema, EAA, and EUDR" requirements.
- **FAQ framing**: "single source of truth" for product data; centralizing eliminates "menial, redundant data entry into multiple retailer portals that often leads to errors and fragmented listings"; "ghost listings" fixed by consistent feeds; AI-powered search needs "highly structured, consistently formatted data".
- **Adjacent extensions** (tier-dependent): Ebook Wholesale Program (Elite; distribution to 20+ partners with consolidated sales reporting); FlightDeck EPUB validation (Elite); Radley Books — metadata-driven publisher website built on EoD data (with sister company Supadu).
- Interpretation: a managed service whose entire job is the record estate + quality gates + per-partner delivery. No orders, no stock, no contracts — the commercial operation is absent by design.

### ONIXEDIT — evidence layer A (official site, fetched)

- Positioning: "Professional ONIX Metadata Management for the Entire Book Supply Chain" — "tools to create, validate and deliver compliant ONIX 2.1 and 3 metadata — for publishers, distributors, and metadata aggregators."
- Product family spans the same Type at three scales:
  - **Cloud** (from $15.25/mo): "Edit ONIX 2.1 & 3 metadata online"; "Real-time validation & export templates"; "Import/Export ONIX and Excel files"; "Transmit your metadata and covers to your partners"; team collaboration with version control.
  - **Pro** (Windows desktop, $475): "Create and update ONIX 2.1 & 3 records"; "Validate metadata using schemas"; "Bulk editing, filtering and metadata cleanup"; Excel/CSV/fixed-length import-export; "Embedded XSLT engine for advanced data transformations"; reports from ONIX files.
  - **Server** (enterprise, from $2,500): "Built on a NoSQL database engine optimized for millions of titles"; "Secure online metadata entry portal for your clients and publishing partners"; "Automate import of ONIX, Excel, images, and asset files"; "Auto-distribute ONIX feeds to your retailers and trading partners"; "Apply custom validation rules for improved quality control"; "Manage contributors with integrated authority control"; REST API ("ONIX API for integrations (ERP, DAM, PIM)"); cloud or on-premise.
  - Utilities: Converter (Excel/CSV↔ONIX batch), Bookstore (ONIX→Shopify sync via XPath mapping), Splitter (split/merge ONIX files).
- Quality framing: "Built-in error detection, scoring, and compliance monitoring — Eliminate costly errors before delivery with smart validation, rule enforcement, and feedback tools across all ONIXEDIT tools."
- Transmission: "automatically transmit your ONIX metadata via FTP, FTPS, or SFTP to distributors, retailers, and trading partners… supports multiple ONIX formats as well as both short and long tags depending on each partner's requirements."
- ONIX definition (vendor FAQ): "the international standard used by the book industry to transmit bibliographic and commercial metadata to distributors, booksellers, marketplaces, and digital platforms"; "Metadata is the digital equivalent of a book's back cover."
- Client base spans the supply chain: publishers (Macmillan, SourceBooks, Britannica, Thames & Hudson, Lerner, Merriam-Webster), a university press (Presses de l'Université du Québec), a distributor ("As a distributor, we rely on ONIXEDIT to manage a large number of titles from a wide range of publishers" — Lakeside Book), and a retailer running the receiving side (Indigo, "Canada's largest book retailer", selected ONIXEDIT Server "to automate its ONIX metadata workflows"; OCLC also listed).
- Interpretation: the pure tool pole — the record file/estate is the object; authoring, validation, transformation, and transmission are the whole product. The same Type serves the receiving side (distributors/aggregators/retailers ingesting many publishers' records), which extends the user base beyond the publishing house.

### NielsenIQ BookData — Title Editor — evidence layer A (official pages + publisher notes PDF, via search snapshots)

- Positioning: the submission surface of a books-in-print database: "Listing your book on the NielsenIQ BookData database, along with its bibliographic information, will ensure that booksellers and librarians have access to your print and e-books."
- Supply methods: "Our Title Editor online service / ONIX / Structured electronic file — recommended for larger publishers who have a catalogue of over 200 titles" (vendor threshold). Title Editor: "enables you to view and edit your book information, upload new titles and add cover images… free to use… the quickest way of supplying your data to our database." Recommended for "independent publishers and self-published authors."
- Quality standard: "Our FREE basic listing service allows you to list the bibliographic data required to meet the minimum Book Industry Communication (BIC) Basic Standard."
- Enrichment: "BookData Enhanced Service allows you to add… enriched metadata information including: Descriptions, Table of contents, Reviews, Promotional information, Author biographies, Keywords"; "Our Editorial Team will manage your information, ensuring accuracy, consistency, timeliness and completeness of your records."
- Dissemination (registry side): "data received from publishers in over 70 countries is widely disseminated in a range of services and formats to publishers, booksellers, internet retailers and libraries in more than 100 countries" (vendor claim).
- Training surface: video tutorials for register / edit a book / search / easy add / contributors / title and series / Thema instructions / formatted descriptions.
- Interpretation: the registry pole — delivery means *submission into an industry database* whose operator then disseminates. The publisher-side work is identical in kind (author, enrich, meet a standard), but the recipient is a registry rather than a list of direct partners. Free tier anchored to a minimum standard; enrichment is a paid service with human editorial.

### BookNet Canada — BiblioShare (+ Webform) — evidence layer A (official pages, via search snapshots)

- Positioning: "BiblioShare: A quality-controlled data aggregation and distribution system"; "a data aggregation service for ONIX, image, and position files that provides support to the Canadian book supply chain… intended for use by publishers and distributors to submit data."
- Intake constraint: "Metadata can only be sent using ONIX" — with **Webform** as the on-ramp: "an easy-to-use online tool that allows small operations to create and manage book metadata, without messing around with complex ONIX files. Once you've created your records in Webform, you can export them to BiblioShare with just a few clicks."
- Quality machinery: "Canadian Bibliographic Certification… tests a publisher's or distributor's production file for structure, content, and other criteria. Certification criteria is based on the three levels of the Canadian Bibliographic Standard and feedback from data aggregators"; "We have built quality reports into BiblioShare for quick and easy feedback"; schema validation documented per ONIX version (2.1 schema pinned to a fixed code-list issue; 3.0 schema tracks new issues).
- Custody posture: "BNC BiblioShare is unique in that we preserve publisher data as it is given to us — we certify ONIX data… that makes us a depository of actual ONIX data."
- Outbound: web services for downstream consumers — ONIX Web Service (full record per EAN), BiblioSimple ("thinner" display version), MARC web service (brief/stub or full MARC records for libraries), assets web service (records + images + samples per ISBN), Bibli-O-Matic browser extension (ISBN detection on any web page), Bookstore Builder Shopify plugin; feeds to wholesalers; CataList (online catalogue and order-management tool for the Canadian trade) and The 49th Shelf consume the database.
- Standards stewardship: BookNet runs the Canadian Bibliographic Committee and sits on the international ONIX Committee.
- Interpretation: the shared national-infrastructure pole — multi-publisher aggregation with certification, serving the trade from a central depository. Same object (the ONIX record + assets), same work (create → validate → distribute), different operator posture (non-profit industry infrastructure vs vendor service).

### Stison — Onix Pre-Flight & Bibliographic Data Feeds — evidence layer A (official help center, via search snapshots)

- Framing: "One of the key functions of the Stison system is a comprehensive approach to metadata communication… generate and send feeds using ONIX and a number of other formats, from the titles that you have contained within the Title Manager module. Once the feeds are set up, your metadata communication will be completely automated, meaning that all you need to focus on is updating and maintaining your metadata within the system."
- ONIX definition (help center): "the standard data format used to communicate information about books and book-related products. Think of it like a language that each computer system used by members of the supply chain is able to understand."
- Destinations: "Each recipient can be set up as an individual destination to send your ONIX to, with filters and options that can be set on each feed to configure exactly what you would like to send and how regularly"; scheduled recipients; full-file vs update-only sends ("the system is set up automatically to only send further ONIX messages when data is updated or changed").
- **Quality gate**: "The ONIX Pre-flight tool is designed to review the quality of the data in your title records"; report classes — *Mandatory* ("all of the data that Nielsen requires for a complete title record"), *Non-mandatory* ("items that indicate best practice in the industry… will not hinder a file being processed"), *Integrity Checks* ("information on the system that isn't matching up according to expectations", e.g., a children's title must carry a CBMC category). Per-check issue counts; click-through to the title record to amend; excluded-titles mechanism for permanent failures.
- **Feed-entry gate**: "To include a title in your Onix feed, it must pass all mandatory checks. In addition, it must have a pass rate greater than 85%" (vendor rule — precise threshold kept out of the canonical document); the traffic-light mechanism runs a pre-flight automatically when a title is ticked for distribution; mandatory failures block, non-mandatory warn.
- Practice guidance: "It is good practice to check this part of the system every month or indeed immediately after you add a new title… much easier to correct mistakes as you go along."
- Interpretation: the suite-module pole — inside a publishing management system, the metadata function appears as record maintenance + quality report + destination feeds. Exactly the machinery the Book Publishing Management pass observed from the other side; confirms that when the metadata function is the center of gravity, it looks like this.

### Cross-references from sibling passes (evidence inherited)

- **EDItEUR** (Layer A, via book-distribution research): ONIX for Books is "the international standard for representing and communicating book industry product information – metadata – in electronic form"; "overtly a commercial data format"; "not in itself a database… a way of communicating data between databases"; a single feed can serve all supply-chain partners; ONIX 3.x supports granular block updates for price/availability. Establishes the standard layer the Type implements.
- **Klopotek** (Layer A, via book-publishing research): enterprise suite exposes metadata management as named apps (Title Metadata Editor — "You decide which attributes and data should be included in your workflow"; Metadata Management — "You select or even design your own scenarios and workflows and decide which data has to be added at which point in time, in which quality"); product pool centralizes metadata for O2C. Suite-module pole at enterprise scale.
- **Consonance** (Layer A, via book-publishing research): ONIX export with data-quality checks and scheduled workflows ("customised metadata, digital assets and content files on any schedule, in the right format, to any recipient"); "We send ONIX to hundreds of recipients daily, accommodating the wide range of variance in what other systems can handle."
- **Firebrand TME** (Layer A, via book-publishing/editorial research): "Editorial & Metadata Management — Centralize your core bibliographic data and descriptive copy in one hub"; TME Lite includes "Seamless metadata distribution" — the workflow system hands its record estate to the metadata distribution service (same vendor splits the two Types across product lines).

## Cross-product Comparison

| Dimension | Eloquence (service) | ONIXEDIT (tool) | Nielsen Title Editor (registry) | BiblioShare (aggregator) | Stison (suite module) |
|---|---|---|---|---|---|
| Central object | title/product records + assets in one hub | ONIX records (file/estate) | title records in the BookData database | ONIX records + images + position files in a national depository | title records inside Title Manager |
| Authoring/maintenance | maintain core title info; ISBN assignment from prefix blocks; format linking + propagation | create/update ONIX 2.1/3; bulk edit; Excel↔ONIX; contributor authority control | view/edit/upload titles + covers; contributor, series, Thema tutorials | Webform creation for small operations; ONIX-only intake | update and maintain metadata in the system |
| Enrichment | descriptive copy, TOC, contributor bios, keywords, extensive keyword strings | media files of any kind attached | Enhanced Service: descriptions, TOC, reviews, promo, bios, keywords | images, interiors, samples, position files | best-practice fields flagged |
| Quality machinery | verification controls before distribution; weekly feedback reports | real-time schema validation; error detection, scoring, compliance monitoring; custom rules (Server) | BIC Basic minimum; editorial team ensures "accuracy, consistency, timeliness and completeness" | certification (3-level standard); quality reports; schema validation | Pre-Flight: mandatory / non-mandatory / integrity checks; feed-entry gate |
| Delivery | hourly/daily/weekly feeds; ONIX 2.1/3/custom; 600+ partners (claim); emergency real-time sends | FTP/FTPS/SFTP; short/long tags per partner; auto-distribute (Server) | submission into registry; registry disseminates to 100+ countries (claim) | web services (ONIX/BiblioSimple/MARC/assets), feeds to wholesalers, CataList | per-recipient destinations with filters and schedules; update-triggered sends |
| Per-recipient configuration | 200+ channel settings (claim); formats + sales rights per partner | export templates; tag styles per partner | n/a (single registry target) | fixed national feeds + token-based web services | filters and options per feed |
| Update propagation | intelligent outbox re-sends; monthly full sends | automated scheduling | ongoing editing keeps registry current | depository preserves as-given | automatic send on data change; full vs empty files |
| Audit/history | Title History + distribution history + file-transfer audit | version control (Cloud) | registry-held records | as-given preservation | destination/pre-flight reports emailed |
| Assets | covers, interiors, EPUBs, audio (tier-dependent) | import media files of any kind | cover images | images, position, samples | (not detailed on fetched pages) |
| Who operates | publishers (enterprise-heavy) | publishers, distributors, aggregators, a retailer (receiving side) | publishers, self-published authors | publishers/distributors submit; trade consumes | publishers (SMB) |
| Standards | ONIX 2.1/3, Thema, EAA; EDItEUR/BISG participation | ONIX 2.1/3.0/3.1; conversion/migration tools | BIC Basic; ONIX; Thema | ONIX 2.1/3.0; Canadian Bibliographic Standard; MARC out | ONIX + "a number of other formats"; Nielsen mandatory alignment |

Evidence layers: all five products = A for fetched pages. "Claim" marks vendor-stated metrics (not used in the canonical document). Absence on a fetched page is absence of evidence, not evidence of absence.

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being a publishing metadata management application:

```text
Bibliographic product records
(works/editions as identified, structured data objects)
└── Authoring & maintenance of the record estate as the primary work
    └── Delivery of records to recipients outside the publishing operation
       (standard or recipient-specific forms)
```

Three properties:

1. **Bibliographic product records as the managed estate** — the central object is the structured record describing a published work and its editions/products (identified, classified, priced, dated) — not the manuscript, not the contract, not the order. Remove it → there is nothing to manage.
2. **Record authoring/maintenance as the primary work** — building and keeping records complete and current is the application's job, and the record itself is the deliverable. In the sibling Types the record serves something else (a business lifecycle, an editorial process, a trade operation); here it serves nothing — it *is* the product. Remove this (records kept as a byproduct of other work) → the record estate of Book Publishing Management.
3. **Delivery to parties outside the publishing operation** — records are made available to supply-chain recipients (retailers, wholesalers, distributors, libraries, aggregators, registries) in standard or recipient-specific forms. Remove it → an internal title database, i.e., the title module of publishing management, not a metadata management application.

### L1 — Common Mature Structure

Present across the researched sample (Layer B unless noted):

- **Industry-standard serialization** — ONIX for Books (2.1 and 3.x) as the dominant exchange format, with classification vocabularies (Thema, BIC, BISAC) and code-list versioning; export/import to non-ONIX formats (Excel/CSV, custom, MARC toward libraries). [A×5 + EDItEUR]
- **Quality control before release** — schema validation, mandatory vs best-practice field checks, integrity/consistency checks, completeness scoring, pre-delivery gates that block or warn, feedback reports; formal certification programs in the aggregator/registry posture. [A×5]
- **Per-recipient feed configuration** — each recipient as a configurable destination: format and ONIX version, tag style, field selection, market/rights scoping, filters, schedule. [A×4: Eloquence, ONIXEDIT, Stison; BiblioShare fixed national feeds]
- **Scheduled and update-triggered distribution** — periodic full feeds plus automatic sends when data changes; full vs incremental sends; re-send mechanisms for corrections. [A×4]
- **Asset handling alongside records** — cover images and product assets (interiors, samples, EPUBs, audio) stored, governed, and delivered with the metadata. [A×4: Eloquence, ONIXEDIT, BiblioShare, Nielsen(covers)]
- **Delivery history and audit** — what was sent to whom and when; change history on records; as-given preservation in the depository posture. [A×4]
- **Ingestion and conversion** — import from spreadsheets/flat files, API feeds, migration between ONIX versions; on-ramps for small operations (webforms). [A×4]
- **Work/format structure** — multiple products (print/ebook/audio ISBNs) linked as formats of one work, with data propagation from a primary format. [A×2 direct: Eloquence, ONIXEDIT Server; B: implied by ONIX 3.0 work identifiers]

### L2 — Variant / Optional Structure

- **Packaging posture**: standalone tool (desktop/cloud/server), managed distribution service, registry submission surface, national non-profit aggregator, suite module inside publishing management.
- **Operator side**: publisher-outbound (dominant) vs distributor/aggregator multi-publisher estates vs retailer receiving-side automation (ONIXEDIT Server at a national retailer).
- **Channel monitoring**: watching how metadata performs/is represented across retail channels (Eloquence on Alert pattern).
- **Downstream data services**: web services/APIs serving records to websites, apps, and bookstores; metadata-driven website builders; bookstore plugins.
- **Commercial extensions**: ebook wholesale programs; enriched-metadata paid services with human editorial.
- **Regional/national infrastructure**: national bibliographic standards and certification schemes; national books-in-print registries; regional code-list conventions.
- **Library-facing outputs**: MARC record generation from publisher metadata.
- **AI-discovery positioning**: structuring metadata for AI-powered search (emerging vendor framing).

### L3 — Vendor-specific (Research Notes only)

- Eloquence: 600+ trading partners and 200+ channel settings (vendor claims); Enhanced vs Elite tiers; Ebook Wholesale Program (20+ partners); NetGalley ONIX delivery; FlightDeck EPUB validation; Radley Books/Supadu metadata-driven websites; since 1996.
- ONIXEDIT: family pricing (Cloud $15.25/mo, Pro $475, Server from $2,500, Converter $350); NoSQL engine "optimized for millions of titles"; XPath mapping (Bookstore); XSLT engine (Pro); Splitter utility; Indigo/OCLC as clients; 15+ years.
- Nielsen: free basic listing at BIC Basic minimum; 200-title threshold for structured electronic files (development fee); image spec (jpg, 650px, 100dpi); registration setup up to 10 days; 70+ countries in / 100+ out (claims); Enhanced Service with named editorial team.
- BiblioShare: ONIX 2.1 schema pinned to code-list Issue 36, 3.0 schema tracks new issues; three-level Canadian Bibliographic Standard; Bibli-O-Matic extension; Bookstore Builder; CataList/The 49th Shelf as consumers; token-based web services.
- Stison: 85% pass-rate feed-entry threshold; traffic-light mechanism; monthly pre-flight practice guidance; Nielsen-aligned mandatory checks; CBMC integrity-check example.

## Rejected Findings

- **"The Type = ONIX"** — rejected as definitional. ONIX is the dominant implementation (all five samples implement it), but the L0 says "standard or recipient-specific forms": registries accepted structured submissions before ONIX, Excel/custom feeds are documented delivery formats, MARC serves the library pole, and EDItEUR itself frames ONIX as one commercial data format among trade message suites. ONIX sits at L1 as the common mature serialization.
- **"Metadata management is only a suite capability, not a standalone Type"** — rejected. Standalone realizations exist across postures (ONIXEDIT toolchain, Eloquence service, BiblioShare infrastructure, Title Editor registry surface). The correct statement: the Type exists both as standalone products and as a capability inside publishing suites; this leaf documents the functional core, with the suite-module pattern recorded under Variants.
- **"Assets are the center"** — rejected. Assets are attached to and delivered with records; the record is the center. The asset-centered Type is Media Asset Management.
- **"Numeric thresholds/schedules are definitional"** — rejected (85% pass rate, 600 partners, hourly/daily/weekly, 200-title threshold): vendor-specific rules, kept in L3.
- **"The receiving side (retailer ingestion) belongs to this Type"** — rejected as the center; recorded as an operator-side variant. The same tools serve receivers, but the Type's canonical seat is the supplier side making records travel.

## Boundary Findings

- **vs Book Publishing Management (sibling, processed 2026-09-06) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED.** The sibling's proposed line holds: publishing management centers on the title as a commercial record serving a business lifecycle (acquisition decisions, contracts, production, royalties, sales); this Type centers on the record estate itself — its completeness, correctness, and reach are the point, and the record is the deliverable. The same title record appears in both: as the business's central commercial object there, as the managed data estate here. Suite products bundle both (Stison: Title Manager + Pre-Flight + feeds; Klopotek: TEP + Metadata Management apps; Firebrand: TME → Eloquence handoff — the vendor's own product line split is the boundary made visible). Remove-tests: add back lifecycle/contract/money machinery → Book Publishing Management; strip to record + quality + delivery → this Type. Both documents cross-referenced; no directory change.
- **vs Book Distribution Management (sibling, processed 2026-09-06) — boundary held, consistent with that pass's own line.** Distribution runs the trade operation: accounts, orders, stock, dispatch, returns, sales records. This Type moves *data*, not goods: no orders, no stock, no fulfillment anywhere in the sampled products. The distribution pass already assigned "metadata distribution to trading partners — the Firebrand Eloquence pattern — to the metadata leaf's territory"; this pass confirms from the metadata side (Eloquence has no order/stock machinery). Remove-test: add orders/stock/fulfillment → Book Distribution Management.
- **vs Publishing Editorial Workflow (sibling, processed 2026-09-09)** — the editorial workflow manages the content process (submissions, evaluation, editing, production release); this Type manages the data record. The editorial pass assigned "money/metadata/sales machinery" to publishing management, not to itself; metadata delivery appears there only as a workflow destination (OMP's ONIX/OAI-PMH distribution). Remove-test: add staged gates/assignments/editorial record → Publishing Editorial Workflow.
- **vs generic PIM (Product Information Management)** — PIM manages product data for commerce in any industry. This Type is defined by bibliographic identity (works/editions/ISBN structure), industry standards (ONIX/Thema/BIC/BISAC), and the book-trade recipient network (retailers, wholesalers, libraries, registries). Strip bibliographic semantics and trade standards → generic PIM. (ONIXEDIT Server explicitly markets its API "for integrations (ERP, DAM, PIM)" — positioning itself as the industry-specific estate beside generic systems.)
- **vs Media Asset Management / DAM** — assets (covers, interiors, EPUBs, audio) are handled here as record attachments delivered alongside metadata; a DAM centers on the asset itself (ingest, transcoding, rights, search over media). Remove the bibliographic record and keep asset machinery → MAM/DAM.
- **vs Master Data Management (generic)** — MDM is domain-agnostic stewardship of master data; this Type's records, standards, quality schemes, and recipients are industry-specific. Strip publishing semantics → MDM.
- **vs library cataloging / discovery registries (e.g., union catalogs)** — those are the receiving/consuming side (MARC, holdings, discovery); this Type is the producer-side supply machinery. The MARC web service (BiblioShare) is a bridge output, not the center.
- **Name-collision guard**: "Publishing Metadata Management" is not generic data-governance metadata management (schemas, lineage, catalogs of data assets) — the managed object here is the *published product's* data, not the publisher's data about data.
- **"去掉什么就变成另一个 Type" 判据**: remove delivery → internal title database (publishing management's title module); remove record primacy (records serve a lifecycle) → Book Publishing Management; add orders/stock → Book Distribution Management; add content-process stages → Publishing Editorial Workflow; strip bibliographic/trade semantics → generic PIM/MDM; center assets instead of records → MAM/DAM.

## Historical / Market-Sample Check

- **Era**: Eloquence has operated since 1996 (pre-ONIX 3, spanning the ONIX 2.1 era); ONIXEDIT claims 15+ years. The pre-ONIX floor — publishers maintaining title records for books-in-print registries and trade catalogs, supplying structured data to whoever could consume it — satisfies all three L0 legs with no ONIX dependence (the L0 deliberately says "standard or recipient-specific forms"). The registry pole (Nielsen) is the direct descendant of the paper books-in-print submission.
- **Region**: the reachable sample is US/UK/Canada-heavy; regional infrastructure (German VLB register, national committees) appears in the record as the regional-variant pole (L2), consistent with sibling passes' findings. The L0 presumes no specific market's infrastructure.
- **Position**: enterprise publishers (Eloquence/Macmillan), SMB and small publishers (ONIXEDIT Cloud, Stison), self-published authors (Nielsen free tier), distributors (Lakeside/ONIXEDIT), retailers as receivers (Indigo), non-profit industry infrastructure (BookNet) — all fit the same core. Nothing cloud/SaaS-specific leaked into L0 (ONIXEDIT Pro is desktop; Server is on-premise-capable).
- The definition therefore holds against older, regional, and differently positioned products.

## Uncertainties

1. **Certification criteria detail** — the Canadian Bibliographic Standard's three levels and BIC Basic's exact field lists were not fetched in detail; the final document says "certification programs test structure and content against published standards" without asserting specifics.
2. **Receiving-side systems** — how retailers/aggregators ingest and normalize feeds internally was not researched (out of scope; the Indigo/ONIXEDIT case shows receivers use supplier-side tools, but their internal machinery is a different territory).
3. **Standalone-product market depth** — beyond the sampled postures, smaller regional metadata-service vendors (e.g., continental European metadata service firms) were not directly documented; the Type stands on the sampled structure, not on exhaustive market coverage.
4. **Vendor metrics** (600+ partners, 200+ settings, 70/100 countries, millions of titles) — vendor marketing claims, unverified; not used in the final document.
5. **Suite-module share** — whether most publishers exercise this function inside suites vs standalone tools is unknown; both postures documented, no market-share claim made.
6. **Sample skew** — search-engine snapshots used for two sources (Nielsen, BookNet, Stison help center); page content is official but snapshot-mediated; no precise operational claims drawn beyond what snapshots showed.

## Final Synthesis

A Publishing Metadata Management application is the system of record for bibliographic product data as a managed estate. Its defining core is small: structured records describing published works and their editions/products (identified, classified, priced, dated) as the central object; authoring and maintaining that record estate as the primary work — the record itself is the deliverable; and delivery of records to recipients outside the publishing operation (retailers, wholesalers, distributors, libraries, aggregators, registries) in standard or recipient-specific forms. Around this core, mature products add the trade's standard machinery: ONIX serialization with classification vocabularies and version handling; quality control before release (schema validation, mandatory vs best-practice checks, integrity checks, completeness scoring, feed-entry gates, certification); per-recipient feed configuration (formats, tag styles, field selection, rights scoping, schedules); scheduled and update-triggered distribution with re-send mechanisms; asset handling (covers, interiors, samples, e/audio files) alongside records; delivery history and audit; ingestion/conversion on-ramps (spreadsheets, APIs, webforms); and work/format structure linking multiple ISBNs with data propagation. The market realizes the Type in five postures — standalone tool (desktop to enterprise server), managed distribution service, registry submission surface, national non-profit aggregator with certification, and suite module inside publishing management — serving publishers of every size, distributors and aggregators running multi-publisher estates, and even retailers automating the receiving side. The Type is bounded from Book Publishing Management (the record estate vs the business lifecycle it serves there — joint review discharged, keep-both ratified), Book Distribution Management (data movement vs the trade operation), Publishing Editorial Workflow (the record vs the content process), and generic PIM/DAM/MDM (bibliographic identity, industry standards, and the trade recipient network are the separators).
