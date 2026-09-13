# Research Notes — Digital Product Catalog

## Research Goal

Understand what the market realizes under "digital product catalog" as an Application Type: what the core objects are, who uses it, how a catalog gets produced and consumed, and — critically given the sibling leaves in DIRECTORY section 05.04 (Product Information Management / PIM, Product Catalog Management) — what the distinct center of gravity is that justifies a separate Type.

## Initial Boundary

Working hypothesis before research:

- This is probably NOT a data-management Type (that territory is PIM and, for sellable-offer maintenance on own channels, Product Catalog Management).
- The likely center is the catalog as a **published, audience-facing presentation artifact** — products assembled into a browsable/shareable catalog (online catalog, portal, line sheet, data sheet, PDF/flipbook).
- Nearest neighbors: PIM (upstream content system), Product Catalog Management (sellable-offer register), E-commerce Platform (transactional storefront), Desktop Publishing / flipbook publishing tools (document producers with no product model), Data Catalog (name collision, different domain).
- Unknown: whether the market's "digital catalog" products require a structured product database, or whether page-oriented publishing tools that merely host catalogs count as the same Type.

## Research Questions

1. What objects exist in such an application? (products, catalogs/editions, sections/collections, audiences, publications)
2. What is the production workflow? (import products → curate/arrange → design → publish → share)
3. How does the catalog stay current against product data? (static vs synced)
4. Who consumes the catalog and through what surface? (buyers, retail partners, sales teams, internal staff)
5. Is ordering/transaction part of the Type, or an overlay?
6. What per-audience behavior exists (pricing tiers, hidden products, access controls)?
7. Where exactly is the boundary vs PIM, Product Catalog Management, e-commerce storefront, and document-publishing tools?

## Representative Products

| Product | Pole | Customer tier | Why chosen |
|---|---|---|---|
| Catalog Machine | Standalone catalog maker (product database → catalogs) | SMB sellers, wholesalers, small manufacturers | The clearest standalone realization; strong help center |
| Plytix (Brand Portals + Product Data Sheets) | Catalog as output surface of a PIM | SMB → mid-market brands/distributors | Shows the PIM→catalog seam from the catalog side; explicit non-transactional posture |
| Brandboom (Line Sheets & Presentations) | Catalog embedded in a B2B wholesale platform | Wholesale brands (fashion/apparel emphasis) | Line-sheet tradition; per-buyer catalog behavior; ordering overlay |
| FlippingBook | Document publishing used FOR catalogs (boundary sample) | General business, manufacturing, marketing | Tests whether product-record management is definitional |

Supporting observation: Catsy (PIM/DAM suite marketed with catalog language; catalog output emerges from the PIM database — supports the "record → publication" direction, but the platform itself is PIM territory).

## Sources

All fetched 2026-09-08 (Tier 1/2, official):

- Catalog Machine — homepage https://www.catalogmachine.com/ (product scope, workflow, sharing, ordering, automation); Help Center https://help.catalogmachine.com/ (collection structure: Catalogs / Products / Import / Showroom / Orders / Images / Designing / Sharing / API)
- Plytix — homepage https://plytix.com/ (platform scope); Brand Portals https://www.plytix.com/brand-portals/ (ecatalog add-on incl. FAQ)
- Brandboom — homepage https://brandboom.com/ ; Line Sheets & Presentations https://brandboom.com/presentations
- FlippingBook — homepage https://flippingbook.com/ (flipbook publishing; catalog use case)
- Catsy — homepage https://www.catsy.com/product-catalog-software (PIM/DAM suite observation)

Access notes: All root/product pages reachable. No Tier-1 article-per-article help-center pages were fetched beyond Catalog Machine's help index; product-page and FAQ depth was sufficient for the claims made. Plytix deep-dive URLs `/product-catalog-software` and `/product-catalog` returned 404. Enterprise vertical catalog realizations (e.g., industrial parts/fitment catalog platforms) were NOT fetched; anything said about them is flagged as unexplored.

## Product Observations

### Catalog Machine (evidence layer A)

- Positions as "online & PDF product catalogs" maker for manufacturers, wholesalers, retailers.
- Object structure visible in help center: **Products** (add/update, categories, collections), **Catalogs** (make/use catalogs, line sheets, templates, layouts), **Showroom** ("a dynamic online catalog of your products"), **Orders** ("product ordering system and payments"), **Images**, **Sharing**, **Import** (from e-stores, CSV, external sources), **Automation & API**.
- Workflow as stated on homepage: create/edit/import products and images → add to catalog template → design with templates/layouts and custom content → optional online ordering + payment inside the catalog → share (URL, email, social, embed, PDF download) with privacy levels/password protection and view statistics.
- Currency behavior: "Re-import or change your products in the database with **automatic update in your catalogs**"; clone catalog versions; customer testimonial: "one product database and all the catalogs are automatically updated each time we have a change in price, packaging, etc."
- Catalog artifact variety (named templates): line sheets (wholesale + retail), lookbooks, price lists, data sheets, product grids, order forms, showrooms with search.
- Per-audience: tiered pricing "to target different customers with catalogs and online stores"; "targeted mini catalogs for specific customer groups, events or markets".
- Ordering is an optional capability: "Enable orders right from your Catalog… receive order requests or accept payments."
- Multi-user teams; multiple accounts per login (agency mode).

### Plytix — Brand Portals + Product Data Sheets (evidence layer A)

- Brand Portals marketed as: "Create ecatalogs that are **always up-to-date** and accessible"; "Turn your product content into an interactive ecatalog."
- "Fully integrated with your PIM. No manual uploads or syncing headaches. Your portal **pulls live product data and assets straight from Plytix**, so everything updates automatically and stays accurate."
- No-code setup: "Pick attributes, apply filters, and adjust layouts… add your logo and colors."
- "One-link access. Share a secure link where partners can **view and export** product data anytime."
- Multiple editions: "Create as many portals as you need, tailored to different partners, teams, markets, or campaigns. Each one can show only the products, attributes, and files that matter most to that audience."
- Explicitly non-transactional (FAQ): "Can customers place orders through Brand Portals? **No**, Brand Portals aren't built for transactions. They're a central hub for sharing curated product information, media, and specs… to browse, export, and get exactly what they need."
- Audiences: sales teams on the road, external partners via website, internal teams in the office.
- Companion add-on Product Data Sheets: "Showcase your products in **live, customizable PDFs**" / "Build branded product sheets directly from your data."
- The PIM itself is the record system; portals are an output surface (FAQ: "Do I need to use Plytix to set up my Brand Portal? Yes! … it pulls data straight from your PIM so it's always up-to-date").

### Brandboom — Line Sheets & Presentations (evidence layer A)

- Core artifact: the **line sheet** / presentation / showroom — "digital line sheet and presentation builder… Create, customize, and share product catalogs with real-time inventory sync" (schema feature list).
- Build: "Import products from Shopify or upload via CSV. Add your logo, brand colors, and media. **Arrange products into collections**."
- Distribution: "Email or text your line sheet link to buyers. They can browse instantly — no account required until they're ready to order."
- Per-audience behavior: "Set account-specific pricing and discounts; hide certain products from specific retailers; show VIP pricing to VIP accounts only; create regional pricing structures; keep line sheets **private, public, or password-protected**."
- Currency: "Changes sync instantly to all active line sheets"; inventory sync to prevent overselling; pre-book vs at-once availability with delivery dates can coexist in one line sheet.
- Export/share: PDF (email/print/offline), CSV download, share via link, embed on website/portal.
- Consumption analytics: "See which buyers viewed your line sheets and what they clicked… abandoned carts… rep performance."
- Ordering/payments/rep commissions/marketplace of 200k buyers: present, but this is the wholesale-commerce platform around the catalog.

### FlippingBook (evidence layer A — boundary sample)

- Core identity: "converts PDFs into digital flipbooks you can share and track" — a **digital publishing** tool, not a product-data tool.
- Workflow: upload PDF → converted to flipbook → customize (branding, video, links, pop-up images, lead form) → share (link/email/embed) → track (page views, outbound clicks, time spent).
- Catalogs are one named use case among magazines, brochures, reports, textbooks ("Product catalogs come with pop-up image galleries… clickable table of contents… catalogs of 100+ pages").
- No product database, no product records, no per-audience catalog editions, no product-data sync anywhere in the observed material.
- Relevance: demonstrates the "publication shell" pole. It can carry a catalog document, but the application itself has no managed assortment — supporting the decision that a managed product assortment is definitional for the Type, and flipbook/PDF-only publishers are adjacent producers of catalog artifacts, not the Type itself.

### Catsy (supporting observation, layer A)

- Markets itself in the catalog space but the platform is PIM + DAM + syndication; the catalog-relevant capability is a self-serve portal ("getting content to internal and external teams easily… partners self-serve access") and sheets/catalogues regenerated from one database (customer quote: "we input all the information into one database and from that we created all our materials… made at one place and then repopulated our sheets and catalogues").
- Confirms the direction record → publication from another vendor, but Catsy itself belongs to the PIM Type.

## Cross-product Comparison

| Dimension | Catalog Machine | Plytix Brand Portals | Brandboom | FlippingBook |
|---|---|---|---|---|
| Managed product assortment (records) | Yes — in-app product database | Yes — lives in the PIM; portal pulls live | Yes — in-app products, imported/synced | **No** — pages of a document |
| Curation into catalog structure | Yes — templates, layouts, sections; collections/categories | Yes — pick attributes, filters, layouts, page components | Yes — arrange products into collections; drag & drop layouts | Page layout only (as PDF authoring, external) |
| Multiple catalogs/editions | Yes — many catalogs, versions/clones, targeted mini catalogs | Yes — portals per partner/team/market/campaign | Yes — line sheets per audience/season; pre-book vs at-once | Multiple documents (not audience editions) |
| Per-audience visibility/pricing | Tiered pricing; targeted mini catalogs | Per-portal products/attributes/files | Account-specific pricing, hidden products, VIP/regional pricing | None (document-level access only) |
| Published surface | Online catalog/showroom + PDF | Web portal + live PDFs | Web showroom/link + PDF | Flipbook (HTML5) |
| Distribution | URL, email, social, embed, PDF download | Secure one-link; embed; export/download | Link (email/text), embed, PDF, CSV | Link, embed, bookshelves |
| Access control | Privacy levels, password protection | Secure link per audience | Private/public/password | Password, domain restriction, download protection |
| Currency vs product data | Auto-update catalogs from database | Live pull from PIM ("always up-to-date") | Instant sync to all active line sheets | None — static publication |
| Consumption tracking | Catalog view statistics | (not observed on page) | Buyer activity (views, clicks, carts) | Page views, clicks, time, lead forms |
| Ordering/transaction | Optional order forms + payments | Explicitly **no** transactions | Yes — orders/payments (wholesale platform) | No |
| Export for audience | PDF download | View and export data/files | PDF, CSV | PDF flipbook download (controllable) |

Layer-B commonalities (observed across ≥3 of the four):
- products organized into collections/sections rather than presented as an undifferentiated list;
- multiple catalog artifacts/editions from one product source;
- branding/customization of the catalog surface;
- sharing by link + embed + PDF; access controls;
- audience-facing browse/search experience maintained by the seller;
- engagement analytics on the published catalog.

## Abstraction Levels

### L0 — Defining Invariant (jointly-held; deliberately small)

1. **Managed product assortment** — products held as individually identified records carrying presentational content (imagery, description, price/attributes). Remove → a page/document publisher (FlippingBook pole) or a plain file store.
2. **Catalog curation** — the assortment is selected and arranged into one or more catalog artifacts: ordered structure (sections/collections/layouts), curated content per artifact. Remove → a product database/list (PIM/PCM territory); "catalog" is precisely the curated presentation, not the data.
3. **Published audience-facing catalog surface** — the catalog is rendered as a viewable, shareable digital artifact (web catalog/portal, flipbook, PDF, line sheet) for an audience to browse/read; consumption (viewing/reading/exporting) is the primary act. Remove → internal data tooling; the publication leg is what makes it an audience-facing catalog.

Jointly-held is load-bearing: (1 alone = PIM / product database; 2 alone = a saved list or filter; 3 alone = a publishing tool; 1+2 without 3 = data maintenance without publication; 2+3 without 1 = document publishing; 1+3 without 2 = a raw feed/portal dump — a catalog needs the curation).

Historical/market-sample check: a seller publishing its catalog as a static PDF on its website (the thin 2000s-era form) satisfies all three legs — assortment + curation + published digital artifact — with no sync, no analytics, no access tiers. 1990s CD-ROM dealer catalogs satisfy leg 3 as digital distribution. Therefore auto-sync, tracking, access tiers, and per-audience pricing are NOT definitional — they are the mature modern implementation of the currency and audience legs. The Type name's "digital" is treated as definitional (the artifact is digitally distributed and consumed), with print-ready PDF as a common output format.

### L1 — Common Mature Structure

- Live currency: catalogs update automatically from the product source (PIM/database/inventory sync) — "always up-to-date" as the marketed ideal.
- Multiple editions from one source: catalogs/line sheets/portals per audience, market, season, or campaign.
- Per-audience visibility and pricing: tiered/VIP/regional pricing; hidden products; per-portal content selection.
- Access controls: private / link-shared / password-protected / public.
- Branded catalog surfaces: logo, colors, layouts, templates.
- Distribution set: shareable link, email, embed on website, PDF export/download; audience-side export (CSV/data files) in B2B forms.
- Consumption analytics: views, clicks, cart/activity signals; per-recipient tracking in B2B forms.
- Catalog variety by job: line sheets, lookbooks, price lists, data sheets, order forms, showrooms.

### L2 — Variant / Optional

- Transaction overlay: order forms and payments inside the catalog (Catalog Machine), full order/payments/rep machinery (Brandboom) — vs explicitly non-transactional portals (Plytix).
- Source system: in-app product database vs PIM-pulled vs commerce/ERP-synced inventory.
- Page-publication form: flipbook/page-turn rendering for PDF-style catalogs (publishing-tool pole).
- Marketplace/rep/showroom networks around the catalog (wholesale pole).
- Vertical forms (not researched in depth; low-confidence): industry-specific catalogs with technical/fitment emphasis.
- Print-ready output as a delivery format of a digital catalog tool.

### L3 — Vendor-specific (research notes only)

- Catalog Machine: AI Concierge catalog creation; REST API; multi-account agency mode; Shopify/Etsy/eBay/Magento/WooCommerce import; specific stats counters (e.g., "4,229 active catalogs last month").
- Plytix: plan tiers (Standard free / Pro / Enterprise, SKU/storage allowances); AI Content Studio; feed management as separate add-on; Shopify Content Manager.
- Brandboom: 200k+ buyer marketplace; Stripe/PayPal payment rails; rep commission auto-calculation; 30-language buyer experience; 9-minute line-sheet onboarding claim; Pipe17/NetSuite integration path.
- FlippingBook: 21-years-in-business claims; Canva/Google Analytics/WordPress/Zapier integrations; Salespal mobile sales app; bookshelves.
- Catsy: retailer-specific export templates (Amazon/Walmart/Home Depot class), readiness dashboards, MCP/API blog positioning.

## Rejected Findings

- "A digital product catalog requires online ordering" — rejected: Plytix Brand Portals explicitly non-transactional; static PDF catalogs satisfy the Type. Ordering is an overlay.
- "A digital product catalog is a PIM feature" — rejected as a definition: standalone catalog makers (Catalog Machine) and wholesale line-sheet tools realize the Type without a PIM; the PIM-output form is one implementation.
- "A digital product catalog = any flipbook/PDF publication" — rejected: document publishers with no managed assortment are adjacent producers (FlippingBook used as boundary evidence).
- "Per-audience pricing/editions are definitional" — rejected: single public catalogs are common; the thin historical form has one audience.
- "Live sync is definitional" — rejected by the historical check: static catalogs remain recognizable members of the Type.

## Boundary Findings

| Neighbour | Distinction | "Remove what → becomes the other" |
|---|---|---|
| Product Information Management / PIM | PIM governs product content as a system of record and distributes transformed data to channels; the DPC is the audience-facing browsable artifact itself. PIM portals add-ons (Plytix) show the seam: PIM = record + structure; portal = publication. | Remove the published audience surface → PIM. Remove the record system → publishing tool. |
| Product Catalog Management | PCM maintains the seller's structured, **sellable** catalog for own channels (variants, availability, prices as sale orientation; realized as commerce/POS catalog module). DPC's orientation is **presentation to an audience**; the catalog artifact is the deliverable, not the sellable register. | Remove sale-channel orientation and keep the curated published artifact → DPC; remove the published artifact and keep sellable-offer maintenance → PCM. |
| E-commerce Platform / Online Store | Storefront is transaction-first (cart/checkout/order). DPC is browse/read-first; ordering optional. | Add checkout as the center → storefront. |
| Desktop Publishing / Flipbook publishing tools | Document producers with no product records; can carry a catalog document but have no assortment, editions, or product-data currency. | Remove product records → publishing tool (FlippingBook evidence). |
| Data Catalog | Name collision only; subject is datasets/metadata for analytics, not sellable product assortment. | Different domain entirely. |
| Content Aggregator / Review Platform | Third-party surfaces over many sellers' products; DPC is seller/brand-controlled presentation of its own assortment. | Remove first-party control → discovery/review surfaces. |

Taxonomy note: section 05.04 holds PIM, Product Catalog Management, and Digital Product Catalog as three leaves. Research supports three distinct centers of gravity (governed content / sellable register / published presentation artifact). No alias collapse recommended; the DPC ↔ PCM seam is the thinnest of the three and is held by orientation (audience presentation vs channel sale-readiness).

## Uncertainties

- Enterprise vertical catalog platforms (industrial parts/fitment/CAD-download catalogs) were not fetched; their fit is asserted only weakly (L2 note) and could justify a future vertical variant study.
- Catalog Machine per-catalog operational details (exact privacy tier names, order-form mechanics beyond marketing description) come from homepage + help-index level, not article-level Tier 1; no precise limits are claimed.
- Plytix Product Data Sheets observed only via add-on summaries on two pages; internal mechanics (template editor depth) unverified.
- Whether buyer-side wholesale platforms (NuOrder, Joor class) should be read as DPC variants or as B2B commerce platforms was resolved pragmatically (catalog capabilities inside a commerce platform); a dedicated pass on Wholesale Commerce Platform could sharpen this.
- FlippingBook's suitability as "representative" is deliberately partial: included as boundary evidence, not as a core member of the Type.

## Final Synthesis

The market realizes "Digital Product Catalog" as a **seller-side catalog publication application**: a managed product assortment (records the seller controls, directly or via PIM/commerce sync) is curated into one or more branded catalog artifacts — online catalogs/showrooms, brand portals, line sheets, data sheets, price lists, flipbooks, PDFs — and published to an audience (buyers, retail partners, sales teams, internal staff) through shareable access-controlled surfaces, where browsing, searching, reading, and exporting are the primary acts and ordering/inquiry is an optional overlay. The Type's signature value is that the published catalog stays current against the product source (live-sync as the mature form; static publication as the thin historical form). The defining core is the jointly-held trio — managed assortment + curation into catalog artifacts + published audience-facing surface; everything else (sync, editions, pricing tiers, analytics, ordering, tracking) is mature but non-defining structure.
