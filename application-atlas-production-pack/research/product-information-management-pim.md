# Research Notes — Product Information Management / PIM

Research date: 2026-09-06
Slug: product-information-management-pim
Directory leaf: Product Information Management / PIM (§05.04 Product Information)

## Research Goal

Understand what a Product Information Management (PIM) application actually is as a working system: its core objects, its data model, the enrichment work users perform, how product data flows in and out, and where the Type's boundary sits against Product Catalog Management, Digital Product Catalog, MDM, DAM, PLM, and commerce platforms.

## Initial Boundary (working hypothesis before research)

- Core use: centralize and govern product *content* (descriptions, attributes, specs, media, translations) as master data; enrich it to completeness/quality standards; distribute it to sales and marketing channels.
- Users: product data managers, catalog/content teams, e-commerce managers, IT admins, external contributors.
- Likely confusions: Product Catalog Management (sellable offer), MDM (multi-domain), DAM (assets), PLM (engineering lifecycle), E-commerce Platform (storefront), Digital Product Catalog (buyer-facing output).
- Known prior context: sibling leaf `product-catalog-management` was processed 2026-09-06 with a joint-review flag: boundary held by center of gravity (PCM = sellable offer for own channels; PIM = governed content syndicated to other parties' selling systems). This research pass must confirm or amend that boundary with direct PIM-side evidence.

## Research Questions

1. What is the central object model: product/item/SKU, attributes, families, variants, categories, assets, references?
2. How is the data structure defined by the organization (schema building)?
3. What does "enrichment" concretely mean: completeness, validation, translation, workflow?
4. How does intake work: imports, supplier onboarding, APIs?
5. How does output/syndication work: channels, connectors, feeds, print, data pools?
6. What lifecycle states and rules govern records (draft/approved/published, scoping, inheritance)?
7. Who uses it, and what interfaces do they work in?
8. Where is the boundary vs PCM, DAM, MDM, PLM, commerce platforms, feed management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence level obtained |
|---|---|---|
| Akeneo | Open-core PIM; data-quality/completeness philosophy; Community + Enterprise editions; mid-market→enterprise | Tier 1 (official developer documentation root, docs.akeneo.com) |
| Pimcore | Open-source platform (PXM); developer-centric; data-model heavy; bundles PIM/MDM/DAM/CMS/commerce | Tier 1 (official documentation, pimcore.com/docs) |
| Plytix | SMB-focused SaaS PIM; pragmatic grid+channels tooling | Tier 1 (official help center, help.plytix.com) |
| Salsify | Cloud-native PXM platform; supplier-side syndication network; brand + retailer two-sided | Tier 2 (official product pages; help center not fetchable) |
| inRiver | Enterprise PIM; content-lifecycle orchestration posture; B2B-manufacturer heavy | Tier 2 (official product pages; community docs login-walled) |

## Sources

Fetched 2026-09-06:

- Akeneo — https://docs.akeneo.com/ (PIM definition, EAV model, families/attributes/categories/channels, jobs/connectors, import/export, workflows nav, ACLs, reference entities, onboarder, rules, mass edit, version purge, REST API, locales/scopes). Deep page `technical_overview/product_information/index.html` returned 404 (1 attempt; not retried).
- Pimcore — https://pimcore.com/docs/ (platform intro), https://pimcore.com/docs/platform/Pimcore_Overview/ (six domains, PXM positioning), https://pimcore.com/docs/platform/Pimcore_Overview/Pimcore_Data_Elements (Data Objects/Assets/Documents, class editor, localized fields, inheritance, variants, classification store, versioning, workflows, permissions, scheduling, dependencies). Note: https://pimcore.com/en/docs returned 404; correct path found via root.
- Plytix — https://help.plytix.com/ (help center root), https://help.plytix.com/en/using-plytix (full section map), https://help.plytix.com/en/product-status-draft-completed (status lifecycle), https://help.plytix.com/en/sharing-your-data (exports/channels/brand portals/connectors).
- Salsify — https://salsify.com/ (platform map), https://www.salsify.com/pxm/pim (PIM positioning). https://help.salsify.com/ returned empty content (1 attempt); https://salsify.com/products/pim returned 404 (1 attempt). Knowledge base is a JS-heavy Salesforce site — not fetchable; Salsify evidence is positioning-level.
- inRiver — https://www.inriver.com/ (home), https://www.inriver.com/product/ (product overview, lifecycle model, module map). Support/community docs are login-walled; evidence is positioning-level.

Not fetched (budget): Akeneo user help center (help.akeneo.com), Pimcore Datahub deep pages, Plytix individual article bodies beyond status page, Sales Layer / Catsy / Contentserv / Stibo STEP.

## Product Observations

### Akeneo (evidence layer A unless noted)

From docs.akeneo.com (developer documentation root, v7.0):

- Definition (vendor's own): "A Product Information Management (PIM) solution is aimed to centralize all the marketing data, to enrich, translate and prepare it for exports to multiple channels. It is a productivity tool helping the contributors to serve the product information in different languages and for different purposes."
- Data model: Entity-Attribute-Value (Product – Attribute – ProductValue). Products carry properties as *attributes*; attribute types include text, price (value + currency), picture (media), date.
- **Family** = "product type" built from a set of attributes; products are created inside a family.
- Products are organized in one or multiple **Categories**.
- **Channels**: "provide a different data for each product according to the selected destination" — examples given: eCommerce website, mobile application, paper catalog.
- Import/export via **Jobs** in **Connectors**: import = read → map/validate into products → save; export = read → process into XML/JSON/CSV → export to files or web service. Multiple pre-built connectors exist (open-source ecosystem).
- Data dimensions: **locales** (localized labels) and **scopes** (scopable labels — channel-level scoping) are first-class in the data format.
- Catalog structure customization: families, family variants, attribute groups, categories, groups, options, reference data.
- **Reference Entities** (Enterprise Edition): rich records for non-product shared data (e.g., brands, suppliers) with their own attributes and completeness.
- **Teamwork Assistant** (EE): projects over product selections with per-project completeness tracking and notifications — enrichment campaign machinery.
- **Collaborative workflow** (EE): "simple workflow" and "partial workflow" pages exist (state machinery for draft/review/approval; exact state names not fetched).
- **Onboarder** (EE): supplier onboarding module — suppliers contribute product data into the PIM (synchronization machinery documented).
- **Rule engine**: custom action rules over products (conditional mass-updates).
- Mass edit operations; ACLs (role-based access control); measurement families/units; version history with purge tooling ("version purger"); REST API with a documented "standard format"; event subscription; scheduled jobs.
- Scalability guidance discusses catalogs with >10k attributes, >10k families, >10k categories, >100k products to export — indicating the intended operating scale of the record store.
- Two editions: Community (open source) and Enterprise; deployment self-hosted or Akeneo cloud offers (Flexibility/Serenity).

### Pimcore (evidence layer A)

From pimcore.com/docs (2026.2):

- Positioning: "open-core platform for Product Experience Management (PXM)... PXM goes beyond classic Product Information Management. While PIM focuses on collecting and maintaining product data, PXM covers the entire lifecycle: creating, managing, delivering, and optimizing product data and experiences across all channels."
- Six domains: PIM ("Central repository for structured product data. Manage attributes, descriptions, translations, and relationships across all channels"), MDM (non-product entities), DAM (digital files), CDP (customer data), DXP/CMS, Digital Commerce. All share one data foundation, one admin UI (Pimcore Studio), one permission system.
- Core data elements: **Data Objects** (structured data — products, categories, suppliers...), **Assets** (digital files), **Documents** (page content). Natively cross-referenced.
- Data Objects: structure defined by a **class definition** created in a visual **class editor** (no code); fields with data types (text, number, date, relation, select...); system generates DB schema + PHP classes.
- Key object capabilities: **localization** (fields configured as localized — different values per language), **inheritance** (child objects inherit field values from parent), **variants** ("model product variants (e.g., sizes, colors) as lightweight children of a parent product"), **classification store** ("handle dynamic, category-specific attributes without changing the class definition"), bulk editing via folder list views.
- Shared capabilities across all elements: **versioning** (every save creates a version; compare/restore), **properties** (key-value metadata with tree inheritance), **scheduling** (publish/unpublish at date/time), **dependencies** (track which elements reference each other), **tags**, **notes & events**, **workflows** ("configurable workflow states, transitions, and actions to govern the lifecycle of any element"), **permissions** (element-level, role-based).
- Channel independence: "data is stored independently from its output channel, it can be delivered to any target: websites..., mobile apps (via REST or GraphQL APIs), commerce platforms, marketplaces, print catalogs, digital signage, or internal systems like ERP and CRM. The same data serves all channels without channel-specific copies."
- Data Onboarding & Distribution module (Datahub); automated pipelines for scheduled imports/exports/transformations; web-to-print from the same content; e-commerce framework module.

### Plytix (evidence layer A)

From help.plytix.com:

- Surfaces: **Product Overview** (grid page: search bar, filters, bulk edit, table views, product data sheets), **Product Detail** (attribute editing, categories, variants/sub-variants, status, comments, automations), **Asset Management** (asset library with categories, link/unlink to products, bulk linking, AI image editing, CSV asset import), **Product Lists** (smart lists), **Relationships** (product-to-product links, e.g., accessories; exportable; publishable to portals), **Settings** (product categories, asset categories, views, brand guidelines, attributes, FTP/SFTP/Dropbox connections, system limits), **Product Families** (assign products to families; formulas in families).
- Attributes: attribute groups; typed attributes; **formula attributes** (computed from other attributes via a function library: date/info/logical/lookup/math/operator/statistical/text); **attribute transformations** for channels and portals; dropdown option restriction on import; AI autofill for text attributes; bulk AI text transformation.
- **Product Status** is a system attribute dropdown: **Draft / Complete / Archived** — "a quick way to know if your product is ready to be shared with the world... especially useful to filter products in smart lists for use in Channels and Catalogs"; settable on import; bulk-editable.
- Sharing data: **Exports** (product data, PDF export, export logs, per-attribute/media format settings), **Webhooks** (incl. Make/Zapier), **Brand Portals** (shareable branded product portals with password protection, downloads, notifications — visitor-facing), **Channels** (CSV/XLSX/XML/NDJSON feeds with templates and format definitions, scheduled), platform connectors (Shopify, BigCommerce with field mapping and metafields), syndication guides for WooCommerce/Magento/Facebook/Google Shopping/Amazon Seller Central, shopping engines (Idealo, Google Shopping, Pinterest, Microsoft), marketplaces (Meta, Snapchat, Leroy Merlin, Conrad, Houzz, TikTok Shop), feed-management tools.
- Admin: account, billing, **team roles**.
- Import: CSV import of products and assets; status settable at import.

### Salsify (evidence layer B — positioning-level; operational docs not fetchable)

From salsify.com product pages:

- PIM = "Manage all product content in one central system of record"; "central system of record for all product data"; "Create a trusted source of truth for all your stakeholders."
- "Enforce Data Quality — bring structure and consistency... while still adhering to each endpoint's unique requirements."
- "Manage for Every Channel — confidently manage unique versions of your product information for each channel and/or region... maintain traceability as your content is transformed to meet different downstream requirements."
- "Adapt to New Requirements — add attributes, import new types of data, or implement validation rules — without having to redo your entire data schema."
- "Automate Business Processes — no-code workflow builder and integrated task workspace to centrally manage, automate, and govern essential go-to-market tasks."
- "Unified PIM and Syndication — manage and directly publish product experiences in one unified platform... strategic retailer relationships... continuously adaptive syndication network."
- Modules: PIM, Syndication, Enhanced Content, Intelligence Suite (AI), GDSN Data Pool, Catalog Sites ("share secure, on-brand, always up-to-date digital product catalogs"), Digital Shelf Analytics, Grocery Accelerator.
- Two-sided: SXM (Supplier Experience Management) for retailers — supplier onboarding against retailer schema requirements, product listing, content enrichment.
- Forrester quote (vendor-published): PIM "powers teams with AI to match data attributes and classifications; organize multimillion SKUs with thousands of attributes using industry templates, taxonomies, and data pools; and syndicate the information to thousands of volatile channel endpoints."
- Integrations: SAP, Adobe Commerce, Salesforce, Shopify, Oracle, Informatica.

### inRiver (evidence layer B — positioning-level; community docs login-walled)

From inriver.com product pages:

- "Inriver PIM orchestrates the end-to-end product content lifecycle... onboard, enrich, and localize product content faster while maintaining compliance and control."
- Lifecycle model (vendor-articulated): four stages — **Ingest** (consolidate data from ERP, PLM, suppliers, partners; AI maps, structures, identifies gaps), **Enrich** (create and localize content for markets, languages, channels), **Syndicate** (deliver channel-ready content to retailers, distributors, e-commerce platforms), **Optimize** (performance insights improve content and trigger updates) — governed by two continuous layers: **Validate** (rules, channel requirements, brand standards) and **Orchestrate** (ownership, handoffs, approvals within workflows).
- Modules: Content Onboarding (supplier data), Syndicate Advance, Digital Shelf Analytics, Brand Store (for partners, distributors, internal stakeholders), Inspire AI, Print & Publish ("complex print catalogues with Adobe InDesign integrations").
- Integrations: ERP, PLM, suppliers; ecommerce partners SAP, Shopify, Amazon, Microsoft.
- Audience: B2B industrial manufacturers, apparel, furniture, electronics, vehicles — "From 1,000 SKUs to 1,000,000."
- G2 review quote (vendor-published): "the most flexible data modeling platform."

## Cross-product Comparison

| Dimension | Akeneo | Pimcore | Plytix | Salsify | inRiver |
|---|---|---|---|---|---|
| Central product record store | Yes (A) | Yes — Data Objects (A) | Yes — Product Overview/Detail (A) | Yes — "central system of record" (B) | Yes — "one system to govern product information" (B) |
| Organization-defined structure | Families + attributes + attribute groups (A) | Class editor; classification store (A) | Attributes + attribute groups + families (A) | "add attributes... without redoing schema" (B) | "flexible/elastic data model" (B) |
| Variants | Family variants / product models (A, nav) | Variants as children of parent (A) | Variants & sub-variants (A) | not directly observed | not directly observed |
| Categories / classification | Category trees (A) | Folders + classification store + tags (A) | Product categories (A) | "classifications... taxonomies" (B) | not directly observed |
| Assets | Media attributes; external asset storage option (A) | Assets element type (DAM) (A) | Asset library linked to products (A) | Enhanced Content / rich media (B) | not directly observed |
| Completeness / validation | Completeness (reference entities, Teamwork Assistant) (A) | Workflow states + validation via processes (A) | Status Draft/Complete/Archived (A) | "Enforce Data Quality", validation rules (B) | Validate layer (B) |
| Localization | Locales first-class (A) | Localized fields (A) | Multi-language via channels/Shopify markets (A, nav) | "unique versions... for each channel and/or region" (B) | "localize content for markets, languages" (B) |
| Channels / distribution | Channels + export jobs/connectors (A) | Channel-independent delivery to any target (A) | Channels (CSV/XLSX/XML/NDJSON) + connectors + exports (A) | Syndication network, direct publishing (B) | Syndicate stage; Syndicate Advance (B) |
| Intake | Import jobs, connectors, Onboarder (A) | Datahub, scheduled pipelines (A) | CSV import, FTP/Dropbox connections (A) | supplier onboarding (SXM) (B) | Ingest from ERP/PLM/suppliers (B) |
| Workflow / approval | Collaborative workflow (EE) (A, nav) | Configurable workflows (states/transitions/actions) (A) | Status + automations + comments (A) | no-code workflow builder + task workspace (B) | Orchestrate layer (ownership/handoffs/approvals) (B) |
| Roles / permissions | ACLs (A) | Element-level role permissions (A) | Team roles (A) | not directly observed | "ownership, handoffs" (B) |
| Versioning | Version history + purge (A) | Every save creates a version (A) | not directly observed | "maintain traceability" (B) | not directly observed |
| Buyer-facing output | not observed as core | Web-to-print; commerce framework (A) | Brand Portals (A) | Catalog Sites (B) | Brand Store; Print & Publish (B) |
| Syndication network / standards | Connectors ecosystem (A) | Marketplace/commerce integrations (A) | Marketplace/shopping-engine feed guides (A) | PXM Network + GDSN data pool (B) | Syndication partners (B) |
| AI | not observed in fetched pages | Copilot module; Agent bundle (A, nav) | AI autofill, bulk AI, AI image editing (A) | Intelligence Suite, Angie assistant (B) | Inspire AI agents (B) |
| Print | Paper catalog named as channel (A) | Web-to-print (A) | PDF export (A) | not directly observed | Print & Publish (InDesign) (B) |
| Deployment | Open-source CE / EE; self-hosted or vendor cloud (A) | Open core (POCL); self-hosted / PaaS (A) | SaaS (A) | Cloud-native multi-tenant SaaS (B) | SaaS (B) |

Reading of the comparison:

- Every sampled product, regardless of philosophy or tier, is built around a **central store of identified product records whose structure the organization defines** and whose purpose is **delivery of that data to downstream channels**. This is the candidate defining core (layer C inference).
- The machinery that makes the store trustworthy and usable — families/templates, variants, categories, assets, completeness/validation, localization, workflow, roles, versioning, bulk tooling — appears across the sample with different depths. These are common mature structure (layer B), not definitional.
- The per-channel model differs in form (Akeneo "channels" as data scopes; Plytix "channels" as feed definitions; Pimcore as channel-independent delivery; Salsify/inRiver as syndication networks) but the concept — one master record, many destination-specific renditions — is shared (layer B/C).
- Buyer-facing outputs (portals, catalog sites, brand stores, print) are present in most products but as *output surfaces* of the same store, not as the management surface (layer B).

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the system is not recognizable as a PIM:

1. **Central store of identified product records** — products exist as individually identified managed records (SKU/item-level identity) held in one authoritative place, consolidating product content that would otherwise be scattered across spreadsheets and systems.
2. **Organization-defined data structure** — the organization defines what data a product carries: typed attributes, grouped, assembled into product types/families; the schema is configurable per business, not fixed by the vendor.
3. **Outbound distribution to downstream channels** — the store exists to deliver product data, transformed per destination, to selling and marketing channels (commerce platforms, marketplaces, print, partners, data pools).

Historical check (§24): older/regional products — enterprise product-data repositories feeding print catalogs (e.g., Stibo STEP lineage), catalog-management systems of the 2000s, commerce-suite catalog modules — all satisfy these three properties without any modern machinery (no AI, no syndication networks, no portals). The definition does not over-fit to the current SaaS/PXM market. Conversely, a system with only property 1 is a product database; with 1+2 it is still just a structured database; distribution (3) is what makes it *information management for channels*. Enrichment/governance machinery is the defining *activity* but its concrete mechanisms (completeness scores, validation rules, approval workflows) are L1 — a minimal PIM could govern quality through process alone.

### L1 — Common Mature Structure

Present across the sample; expected in any serious product; not definitional:

- Attribute types and attribute groups; product families as templates of required attributes
- Variant modeling (option axes; variant as child of a parent product model) with shared vs variant-specific data
- Category trees / classification (internal taxonomy; sometimes standard industry taxonomies)
- Digital assets (images, documents) linked to products; asset library (DAM-lite)
- Completeness and data-quality machinery (completeness indicators, validation rules, quality scoring)
- Localization: per-language (and often per-currency/market) values on the same record
- Channel model: named destinations with per-channel attribute selection, mapping, and output format
- Intake: file imports (CSV/Excel/XML), APIs, supplier data onboarding
- Bulk editing / mass actions; rules or automations (conditional updates, computed/formula attributes)
- Workflow: draft → review/approve → published-ready states; task assignment
- Roles and permissions (scoped by category, attribute, locale, or channel)
- Search/filter over the record store; saved views/lists; grid as the primary working surface
- Versioning / change history
- API + webhooks + connector ecosystem
- Product-to-product relationships (accessories, substitutes, upsell)
- Reference/dictionary data (dropdown options, units of measure, shared entities like brands)

### L2 — Variant / Optional Structure

Depends on segment, side of the supply chain, industry, deployment:

- Supplier onboarding portals (inbound collaboration at scale)
- Syndication networks to retailer endpoints; GS1/GDSN data pools (grocery/CPG standard-based exchange)
- Print catalog production (InDesign integration, PDF/paper output)
- Buyer-facing shareable outputs: brand portals, catalog sites, brand stores
- Digital shelf analytics / listing-performance feedback loop (optimize stage)
- AI assistance: autofill, translation, extraction from assets, agentic enrichment
- Formula/computed attributes
- B2B specifics: per-customer/per-channel assortments, rich technical spec depth
- Deployment posture: open-source self-hosted, SaaS multi-tenant, platform/PaaS, commerce-suite module
- PXM/platform bundling: PIM + DAM + CMS + commerce in one system
- Industry accelerators (grocery, fashion & beauty, industrial)

### L3 — Vendor-specific (research notes only)

- Akeneo: two-level product model (product model → product) inside family variants; Reference Entities (EE); Teamwork Assistant projects; Onboarder; rule-engine JSON format; measurement families; Community vs Enterprise split; Serenity/Flexibility cloud offers; documented scalability thresholds (10k attributes/families/categories, 100k-product exports).
- Pimcore: class editor generating DB schema + PHP classes; classification store; object bricks/field collections; Datahub (GraphQL); Perspectives; POCL open-core license; Studio UI; six-domain bundling.
- Plytix: Brand Portals; smart lists; formula-attribute function library ("Operations"); system attributes (Status); AI autofill/bulk AI; FTP/SFTP/Dropbox channel connections; per-connector field mapping (Shopify metafields, markets).
- Salsify: PXM Network; SXM (retailer-side supplier experience); Catalog Sites; GDSN Data Pool; Grocery Accelerator; Angie AI assistant; Intelligence Suite; Digital Shelf Analytics.
- inRiver: Ingest/Enrich/Syndicate/Optimize lifecycle naming; Validate + Orchestrate layers; Inspire AI; Content Onboarding; Syndicate Advance; Print & Publish (Adobe InDesign); Brand Store; "elastic data model."

## Vendor-specific Findings

- The term **PXM (Product Experience Management)** is a vendor-coined repositioning used by Salsify, Pimcore, and inRiver (and others) to extend PIM toward experience/analytics; it is market language, not a structurally different Application Type. Pimcore explicitly frames PXM as "beyond classic PIM" while still defining its PIM domain as the central product repository.
- inRiver's four-stage lifecycle (Ingest→Enrich→Syndicate→Optimize) is the clearest vendor articulation of the end-to-end flow, but each stage maps to machinery present in other products under different names.
- Salsify is the only sampled product that is explicitly two-sided (brand-side PXM + retailer-side SXM supplier onboarding) and network-centric (syndication network + GDSN data pool).
- Plytix is the only sampled product whose lifecycle states are directly observable as a simple three-value system attribute (Draft/Complete/Archived) rather than a workflow engine.
- Pimcore is the only sampled product where the schema builder generates executable code artifacts (PHP classes) — a developer-platform realization of the same concept.

## Boundary Findings

1. **vs Product Catalog Management (§05.04 sibling — joint-review flag)** — confirmed by center of gravity, now with direct PIM-side evidence. PCM maintains the *sellable offer* (structure, variants, prices, availability) for one's own sales channels; PIM governs *product content as master data* and delivers it to channels — including other parties' selling systems (retailers, marketplaces, distributors, data pools). Evidence: none of the sampled PIMs treats price/stock-as-selling-state as its center (Akeneo has a price *attribute type* — data, not offer state); all five center on content governance + distribution. The boundary blurs in practice: commerce platforms embed PIM-like content authoring; PIM vendors publish buyer-facing catalog sites (Salsify Catalog Sites, inRiver Brand Store, Plytix Brand Portals). Keep both leaves; document the blur. Joint-review recommendation from the PCM pass is satisfied by this pass.
2. **vs Digital Product Catalog (§05.04 sibling)** — the buyer-facing published catalog (portal/site/PDF) is an *output surface* of PIM (and of PCM), not the management system. Remove the management store and keep the published artifact → Digital Product Catalog.
3. **vs Master Data Management (§13)** — MDM governs golden records across multiple data domains org-wide (customers, suppliers, products...) with matching/deduplication focus; PIM is product-domain-specific and output/syndication-oriented. Pimcore literally ships both as separate domains over one data foundation — evidence that the market treats them as distinct capabilities. PIM is sometimes called "product MDM"; the channel-delivery orientation is the distinguishing test.
4. **vs DAM** — PIMs hold product-linked media (asset library, media attributes); a DAM is an asset-centric system (asset lifecycle, rights, renditions) that may serve many consumers. Pimcore bundles both as separate domains; Akeneo documents storing assets externally. PIM asset handling is DAM-lite in service of product records.
5. **vs PLM (§16)** — PLM manages the engineering product definition upstream (BOM, CAD, engineering changes); PIM manages the commercial/marketing content downstream. inRiver names ERP and PLM as *upstream sources* to ingest from — the systems are complementary, not the same Type.
6. **vs E-commerce Platform / Online Store Builder (§05.01)** — the commerce platform sells (storefront, cart, checkout, orders); the PIM feeds it product data. Plytix's Shopify/BigCommerce connectors and inRiver's SAP/Shopify/Amazon integrations show PIM→commerce as a delivery relationship.
7. **vs Feed Management / shopping-feed tools (§06 adjacency)** — feed tools transform an existing catalog for ad/exchange channels; the PIM is the master record upstream. Plytix lists "Feed Management Tools" as *integration targets*, evidencing the layering.
8. **vs ERP item master (§10 adjacency)** — an ERP material master records what is stocked/procured/manufactured; it lacks the marketing content model (rich descriptions, media, translations, channel renditions). inRiver/Salsify position ERP as an integration source, not a competitor surface.
9. **Negative boundary test** — remove distribution (L0-3) → a structured product database / MDM-lite; remove org-defined structure (L0-2) → a fixed-schema product list inside a commerce platform; remove the central store (L0-1) → a syndication/feed tool. Each removal lands in a different Type.

## Uncertainties

- Salsify and inRiver operational surfaces (grid/edit forms, exact states, permission model) were not directly observed — positioning-level evidence only. All Salsify/inRiver-specific claims in the final document are kept qualitative.
- Akeneo's exact workflow state names (simple/partial workflow) were not fetched; the final document describes approval workflow machinery qualitatively.
- Akeneo family-variant mechanics come from the docs navigation and data-structure file list, not a fetched deep page; treated as A-level for existence, qualitative for behavior.
- Plytix versioning/history was not observed; not claimed.
- Market-share or vendor-count claims deliberately not made (no evidence fetched).
- The "PIM is overwhelmingly multi-channel commerce-oriented" framing rests on the five-product sample; older print-catalog-era systems were checked conceptually (Stibo STEP lineage) but not fetched.

## Final Synthesis

A PIM is the organization's central system of record for product *content*: identified product records whose structure (attributes, families, variants, categories) the organization itself defines, worked on by enrichment teams (complete, translate, validate, approve) until channel-ready, then distributed — transformed per destination — to the channels where the products are sold or marketed. Its defining core is small: central identified record store + organization-defined structure + outbound channel distribution. Everything else — variant machinery, assets, completeness scoring, workflow, localization, portals, syndication networks, AI — is mature but non-defining structure. The Type sits upstream of commerce platforms and feed tools, downstream of PLM/ERP, domain-specific next to MDM, and output-oriented next to DAM; its closest sibling, Product Catalog Management, is distinguished by center of gravity (sellable offer for own channels vs governed content delivered to any channel, including other parties' selling systems).
