# Research Notes — Product Catalog Management

Research date: 2026-09-06
Slug: product-catalog-management
Directory leaf: Product Catalog Management (§05.04 Product Information)

## Research Goal

Understand what a Product Catalog Management application actually is as a Type: what objects it maintains, what users do with them, how the catalog connects to selling, and where its boundary lies against Product Information Management (PIM), Digital Product Catalog, E-commerce Platform, Retail POS, and domain-specific catalog Types (Restaurant Menu Management, Telecom Product Catalog).

## Initial Boundary

Working hypothesis before research:

- Product Catalog Management = the seller-side system for building and maintaining the structured, sellable catalog of products a business offers: product records, variants/SKUs, categories/collections, attributes, media, prices, availability — organized so products can be presented and sold through sales channels.
- Nearest neighbors: PIM (upstream content authoring/governance/syndication), Digital Product Catalog (buyer-facing published catalog), E-commerce Platform (storefront/checkout), Retail POS (transaction surface), Restaurant Menu Management / Telecom Product Catalog (domain-specific catalog Types).
- Risk: market usage of "catalog management" is inconsistent; many commerce platforms embed the function as a module; PIM vendors also call their output "catalogs."

## Research Questions

1. What objects constitute the catalog (product, variant/SKU, category/collection, attribute, media, price, availability)?
2. How are variants modeled (options × values)? What is the sellable unit?
3. How are products organized (category trees, collections, menus)? Manual vs rule-based membership?
4. What lifecycle/states do product records carry (draft/active/archived, visibility)?
5. How does the catalog connect to sales channels / locations / customer groups?
6. What rules and constraints matter (required fields, SKU identity, option structure, visibility gating)?
7. What is the boundary with PIM? With the e-commerce platform? With Digital Product Catalog?
8. What varies by segment (SMB vs B2B: price lists, shared catalogs, customer groups)?
9. Historical check: do older / platform-native / POS item files / marketplace seller catalogs still fit the definition?

## Representative Products

| Product | Why selected | Evidence tier reached |
|---|---|---|
| Shopify | dominant hosted commerce platform; SMB/mid-market; product model documented in official developer docs | A (official dev docs, product model) |
| BigCommerce | open SaaS, mid-market/enterprise; catalog concepts documented explicitly | A (official catalog overview) |
| Square | POS-embedded item library; SMB retail/services; different surface philosophy | A (official help center article) |
| Adobe Commerce | enterprise open-source commerce; B2B shared catalogs | A (official admin docs) |
| WooCommerce | open-source WordPress plugin; different packaging philosophy | A (official docs) |
| Salsify | brand-side PIM/PXM anchor used to draw the PIM boundary | B (official product pages, positioning only) |

## Sources

- Shopify — Product object, GraphQL Admin API: https://shopify.dev/docs/api/admin-graphql/latest/objects/Product (fetched 2026-09-06)
- BigCommerce — Catalog Overview: https://developer.bigcommerce.com/docs/store-operations/catalog (fetched 2026-09-06)
- Square — Create and edit items (Help Center): https://squareup.com/help/us/en/article/5328 (fetched 2026-09-06)
- Adobe Commerce — Catalog menu: https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog-menu (fetched 2026-09-06)
- WooCommerce — Adding and Managing Products: https://woocommerce.com/document/managing-products/ (fetched 2026-09-06)
- Salsify — homepage / product navigation (PIM, Syndication, Catalog Sites, GDSN, SXM): https://www.salsify.com/ (fetched 2026-09-06)

Source-access limitations:
- Shopify Help Center (help.shopify.com) returned HTTP 403 on both attempts; Shopify evidence rests on the official developer product-model documentation (which describes the same admin objects).
- BigCommerce support knowledge base returned 404 on the first URL; the developer catalog overview succeeded.
- Square developer docs 404'd on two guessed paths; the Help Center article succeeded.
- Salsify help center returned an empty body; only marketing/product pages were reachable → Salsify findings are positioning-level (Tier 2), used only for boundary reasoning, not for operational claims.

## Product Observations

### Shopify (evidence layer A — official developer product-model docs)

Key observations:

- The `Product` object "lets you manage products in a merchant's store"; products are "the goods and services that merchants offer to customers."
- Product carries: title, description (HTML), price range, media (images, 3D models, videos), options (e.g. size, color), variants, collections, category (from a Standard Product Taxonomy), vendor, product type, tags, SEO fields, handle (URL slug), status.
- Product status is an explicit three-state enum: DRAFT / ACTIVE / ARCHIVED (plus an `unlisted` filter value). "Shopify only displays products with an ACTIVE status in online stores, sales channels, and apps."
- Variants: "product variants … create or update different versions of the same product"; per-variant SKU, price, barcode; product has `hasOnlyDefaultVariant` (a product with no options has a single default variant).
- Collections: products "organized by grouping them into a collection"; collections can be custom or smart (query-filtered) — the collection query filter supports `collection_type: custom | smart`.
- Channel publication: products are published to publications/channels (online store, Point of Sale channel, other app channels); per-channel published status values (published / hidden / intended / unavailable); `onlineStoreUrl` is null when not published to the online store.
- B2B: publications can target `COMPANY_LOCATION` catalog type (B2B); contextual pricing "a price might vary depending on the customer's location."
- Inventory: `tracksInventory`, `totalInventory`, per-variant inventory; out-of-stock variant flags.
- Metafields: custom fields with namespace/key attached to products and variants.
- Other structures: selling plan groups (subscriptions), gift cards, bundles (bundle components), combined listings (combining separate products into one listing via a shared option), compare-at price range (sale pricing), events feed on the product.

### BigCommerce (evidence layer A — official catalog overview)

Key observations:

- "The Catalog refers to a store's collection of physical and digital products. The Catalog includes all the information about a product such as MPN, warranty, price, and images."
- "Products are the primary catalog entity, and the primary function of the ecommerce platform is to sell products on the storefront and other channels." Products can be physical or digital (digital includes downloadable files and services).
- Variants: "represent an item as it sits on the shelf in the warehouse or a particular saleable product"; "Everything you can buy should be a variant." A simple product without options is its own "base variant." Variants "are usually what you track inventory against"; can have own price/weight/dimensions/image or inherit from the product; "Must have a SKU code (unless they are a base variant)."
- Variant options: "any choices that the shopper needs to make that will result in selecting a variant" (color, size); multiple-choice types only; "Will automatically generate variants when created in the control panel."
- Modifier options: choices that "change how the merchant fulfills the product" (engraving text, insurance checkbox); "will not change the SKU/variant fulfilled"; can carry price/weight adjusters; cannot be part of a variant.
- Complex rules: conditions across option selections adjusting price/weight/image/purchasability.
- Categories: "a hierarchy of products available on the store, presented in a tree structure"; "A store's category structure determines the primary menu structure of most storefront themes." Products can belong to multiple categories; "no primary category." Category visibility can be gated by customer group ("A category can be enabled and have products assigned yet still not appear on the storefront if it's excluded from a customer group's category access permissions").
- Brands as a catalog entity; custom fields (name/value); bulk pricing rules (quantity-based); metafields; product reviews (API-created); images with single-thumbnail rule; videos (YouTube-hosted); per-category product sort order; catalog summary endpoint (counts, price ranges, inventory value).

### Square (evidence layer A — official help center)

Key observations:

- "Items are sellable goods and services that make up your item catalogue." The Item library is "one centralized hub" to "organize items, track inventory across multiple locations, manage variants, and streamline your product information."
- Items created/edited from Dashboard and from the POS app; "the change will reflect in your Square Dashboard, point of sale app, and website."
- Item type drives a dynamic attribute sheet: Prepared food and beverage (nutritional info, calorie counts, dietary preferences, allergens), Physical good (inventory and SKU fields), Event (tickets with location/times), Digital (file for download), Other (manual fulfillment).
- Item fields: name (customer-facing name; kitchen name on POS), price, description (with AI-generated descriptions, including from scanned-item third-party databases), SKU, inventory tracking, images, modifiers.
- Organization: "categories for retail items, or menus for prepared food and beverage items."
- Assignment: items are assigned to locations and sales channels (point of sale, website, delivery apps); per-location channel overrides ("an item can be available on all of your websites, but websites that show a specific location where the item isn't available won't display your item at that location"); modifier sets carry their own channel visibility with warnings on mismatch.
- Related capabilities: item options/variations, modifiers, per-location price overrides, bulk import, unit types (e.g., food by weight).
- Permissions: article addressed to "Sellers with general items permissions" (permission-gated catalog editing).

### Adobe Commerce (evidence layer A — official admin docs)

Key observations:

- Catalog menu provides "product creation, category, and inventory management tools, shared catalogs for custom pricing in B2B stores, and catalog enrichment for AI-assisted discovery."
- Products: "Create products of every type and manage your inventory" (products grid).
- Categories: "Create the category structure that is the foundation of your store's navigation."
- Shared Catalogs (B2B module): "give you the ability to make custom pricing available to different companies."
- Catalog enrichment (PaaS): "review and apply AI-suggested improvements to product names and long descriptions so your catalog is represented accurately in LLM and AI-assisted discovery."

### WooCommerce (evidence layer A — official docs)

Key observations:

- "Before you can start selling, you need products to offer." Products can be added "with just a name and a price," with more detail improving search performance.
- Product types: Simple (single item, no variations), Grouped (multiple products on one page, each addable to cart individually), External/Affiliate (link out to another site), Variable (variations with own price, SKU, stock level); Virtual and Downloadable designations (services/memberships; digital files).
- Product editor as the comprehensive interface for prices, stock, descriptions, images; attributes for variable products.
- Bulk editing (prices, stock, categories across many products); duplicate/delete; feature/filter/sort (featured products, admin filtering, front-end sort order).
- Organization questions framed as merchant decisions: categories, tax, stock tracking, shipping dimensions/weight, variations, attributes, reviews (site-wide, per product, or none).

### Salsify (evidence layer B — official product pages, positioning only)

Key observations (positioning-level; no operational claims drawn from this):

- PXM platform: PIM as "one central system of record" for product content; syndication "to every consumer touch point"; GDSN data pool for standardized attribute synchronization; "Catalog Sites — share secure, on-brand, and always up-to-date digital product catalogs" (buyer-facing published catalogs); SXM (retailer-side supplier onboarding / product listing / content enrichment); digital shelf analytics; AI capabilities.
- Confirms the PIM pole: content governance + syndication to *other parties'* selling systems, and the Digital Product Catalog pole: published buyer-facing catalog sharing.

## Cross-product Comparison

| Dimension | Shopify | BigCommerce | Square | Adobe Commerce | WooCommerce |
|---|---|---|---|---|---|
| Catalog vocabulary | products + collections | "Catalog" (products primary entity) | "item catalogue" / Item library | Catalog menu (products, categories) | products |
| Product record | title, description, price, media, options, tags, vendor, SEO, status | name, price, weight, type (physical/digital), images, custom fields | item with type-driven dynamic attributes | products of every type | name, price, description, images, attributes |
| Sellable unit | variant (default variant when no options) | variant/SKU ("everything you can buy should be a variant") | item variation | (not directly observed in fetched pages) | variation (per-variation price/SKU/stock) |
| Options model | options → variants | variant options (must select) vs modifier options (fulfillment, adjusters) | item options/variations + modifiers | (not observed) | attributes → variations |
| Organization | collections (custom/smart) + standard product taxonomy | category tree = storefront nav; multiple categories, no primary | categories (retail) or menus (food) | category tree = foundation of navigation | categories (+ tags) |
| Lifecycle/visibility | explicit DRAFT/ACTIVE/ARCHIVED status | is_visible + customer-group gating | assignment to locations/channels | (not observed in fetched pages) | (publish state not directly observed in fetched page) |
| Channel connection | publications to sales channels (online store, POS, apps) | storefront + other channels; customer-group category access | locations + sales channels (POS, website, delivery apps) with per-location overrides | websites; shared catalogs per company (B2B) | storefront (WordPress site) |
| Pricing overlays | compare-at price range; contextual pricing (markets); B2B company-location catalogs | bulk pricing rules (quantity-based); customer groups | per-location price overrides | shared catalogs = custom pricing per company | (not observed) |
| Inventory linkage | tracksInventory per variant | "variants are usually what you track inventory against" | inventory tracking per item/location | inventory management tools in catalog menu | stock per variation |
| Media | images, 3D models, videos; featured media | images (single thumbnail rule), YouTube-hosted videos | item images | (not observed) | product images |
| Bulk/import | (not directly observed in fetched pages) | CSV import referenced (V2) | bulk import items | (not observed) | bulk editing |
| Custom data | metafields (namespace/key) | custom fields + metafields | (type-driven attributes) | (attribute system implied) | attributes |
| AI features | (not observed in fetched pages) | (not observed) | AI-generated descriptions (incl. from scanned-item databases) | catalog enrichment for AI/LLM discovery | (not observed) |
| B2B structures | company-location catalogs, contextual pricing | customer groups (category access, pricing) | (not observed) | shared catalogs per company | (not observed) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

1. **Seller-maintained catalog register** — a persistent, seller-side set of product records, each an identified offer (name/title, description, price) that the seller creates, edits, and retires in one place.
2. **Product record as the managed unit** — records are individually addressable and editable; the register accumulates over time.
3. **Sellable organization** — products are arranged into a browsable/structured offer (categories/collections/menus) so the catalog can be navigated and presented.
4. **Sale orientation** — the catalog is maintained in order to present and sell the products through the seller's sales channels (storefront, POS, channels).

Test: remove the register → no catalog; remove organization → it is a product database, not a catalog; remove sale orientation → it is generic product data management (PIM/MDM territory). All four hold across the sample, including POS item files (Square) and open-source storefronts (WooCommerce).

Historical check: pre-digital mail-order catalogs, POS item/PLU files (item, department, price), and marketplace seller item lists all satisfy L0 — register + organization + for-sale orientation — without any modern feature (channels, variants-as-SKU, AI, B2B price lists). The definition does not over-fit the current hosted-commerce era.

### L1 — Common Mature Structure

Present across most of the sample; not required for recognition:

- **Variants/SKUs as the sellable unit** — options × values generate variants; per-variant SKU, price, stock, image; a no-option product is its own single variant (Shopify, BigCommerce, WooCommerce explicit; Square variations).
- **Media management** — images with main/thumbnail conventions; video support; 3D models in one product (Shopify).
- **Working/published distinction** — draft vs active/published vs archived/hidden states (Shopify explicit three-state; WooCommerce/WordPress publish states; BigCommerce visibility flags; Square assignment-based availability). Exact labels vary.
- **Bulk operations and import/export** — bulk edit, CSV import/export, duplicate product (BigCommerce, Square, WooCommerce observed; Shopify admin commonly provides CSV import/export but was not directly observed in fetched pages).
- **Custom attributes/fields** — metafields, custom fields, attributes extending the base record (Shopify, BigCommerce, WooCommerce).
- **Inventory linkage** — stock tracked against variants/items, surfaced in the catalog (all five commerce products).
- **Availability controls** — per-channel publication, per-location assignment, customer-group visibility (Shopify, Square, BigCommerce, Adobe).
- **Pricing overlays beyond base price** — sale/compare-at price, quantity-based pricing, customer/company-specific pricing (Shopify, BigCommerce, Adobe, Square).
- **Admin surfaces** — products list/grid with search/filter/sort, product editor, category/collection editor (all five).
- **SEO fields** on product records (Shopify, BigCommerce; Adobe implied by catalog enrichment for discovery).
- **Product kind** — physical vs digital vs service distinction shaping fulfillment (BigCommerce, WooCommerce, Square, Shopify).

### L2 — Variant / Optional Structure

Depends on segment, domain, or product philosophy:

- **B2B catalog structures** — shared catalogs / company-specific price lists / customer-group pricing and category access (Adobe B2B, Shopify B2B company-location catalogs, BigCommerce customer groups).
- **Rule-based organization** — smart/dynamic collections computed from conditions (Shopify smart collections; single-product observation in sample).
- **Standard product taxonomies** — a fixed, platform-defined category taxonomy vs free-form merchant categories (Shopify Standard Product Taxonomy).
- **Type-driven dynamic attributes** — item type determines the editable attribute set, including domain packs (Square: food nutrition/allergens, event tickets; BigCommerce physical/digital; WooCommerce simple/grouped/external/variable).
- **Modifier-style options** — selections that change fulfillment without changing the SKU (BigCommerce modifiers, Square modifiers).
- **Domain-specific organization** — menus for food service (Square), service catalogs.
- **AI assistance** — generated descriptions, AI-suggested enrichment for AI/LLM discovery (Square, Adobe).
- **Subscriptions, gift cards, bundles, combined listings** (Shopify).
- **Reviews attached to products** (BigCommerce, WooCommerce).
- **Multi-market/multi-currency contextual pricing** (Shopify markets).
- **Brand/manufacturer as a catalog entity** (BigCommerce brands; Shopify vendor field).

### L3 — Vendor-specific Structure (kept out of the final document)

- Shopify: publications/channel model internals, handles/URL slugs, Standard Product Taxonomy IDs, combined-listing roles, selling-plan mechanics.
- BigCommerce: base-variant concept, modifier adjusters, complex rules, 4-decimal pricing precision, YouTube-only video hosting, catalog summary endpoint.
- Square: item types incl. event tickets, kitchen names, per-location channel overrides, menus, AI description from scanned-item databases.
- Adobe Commerce: shared-catalog B2B module, catalog enrichment for LLM discovery, store-view scoping.
- WooCommerce: simple/grouped/external/variable type taxonomy, WordPress integration.

## Vendor-specific Findings

- BigCommerce's explicit separation of *variant options* (change the SKU) vs *modifier options* (change fulfillment, with price/weight adjusters) is the clearest articulation of a distinction that other products implement implicitly (Square modifiers; Shopify options are variant-forming).
- Square's *location × channel* availability matrix (with per-location channel overrides) is the most granular availability model observed.
- Adobe's *shared catalogs* and Shopify's *company-location catalogs* are two different mechanisms for the same B2B concept (company-scoped pricing/assortment).
- Shopify is the only sampled product with an explicit, named three-state product status (draft/active/archived).

## Boundary Findings

1. **vs Product Information Management / PIM** — the most important boundary. PIM centers on product *content* as governed master data: multi-source intake, enrichment workflows, translation, data quality, and syndication to *other parties'* selling systems (retailers, digital shelf, GDSN). Product Catalog Management centers on the *sellable offer*: structure, variants, categories, prices, availability for one's own sales channels. Test: if the system's job is to make product content trustworthy and deliverable to other parties' selling systems → PIM; if the job is to maintain the sellable catalog that one's own channels sell from → PCM. The boundary blurs in practice: commerce platforms embed content authoring (PIM-like) inside catalog management, and PIM vendors publish buyer-facing "catalog sites." Documented by center of gravity.
2. **vs E-commerce Platform / Online Store Builder** — PCM is usually realized as the catalog module of a commerce platform; the platform adds storefront, cart, checkout, orders. The catalog is the offer; the platform is the selling machine. A standalone pure-play "catalog management" product is rare in the sample — the Type is mostly a module surface. This is a realization pattern, not a reason to merge the Types.
3. **vs Digital Product Catalog** — the published, buyer-facing catalog (browsable/shared with buyers, e.g., Salsify "Catalog Sites") is an *output* of catalog management, not the management surface itself. PCM is seller-side maintenance; Digital Product Catalog is buyer-side presentation.
4. **vs Retail POS** — the POS transacts against the catalog; catalog maintenance (item library) is a separate surface of the same data (Square demonstrates the split: edit in Dashboard, sell in POS app). POS's defining job is the live transaction; PCM's defining job is maintaining the offer.
5. **vs Restaurant Menu Management / Telecom Product Catalog** — domain-specific catalog Types share the structural core (items, categories, modifiers) but carry specialized objects and rules (menus/kitchen names; telco service offerings). Separate leaves; PCM is the generic form.
6. **vs ERP item master / Inventory Management** — an ERP material master records what is stocked/procured; it lacks the sellable organization (browsable categories, presentation, channel availability) and sale orientation. Negative boundary: remove the sellable-organization + channel orientation and you get an item master, not a catalog.
7. **vs Master Data Management** — MDM governs data across domains org-wide; PCM is domain-specific to the sellable product offer.

## Uncertainties

- Lifecycle states: only Shopify showed an explicit named status enum in fetched pages; WooCommerce/Adobe publish-state details were not directly observed. Final doc states the distinction qualitatively.
- Shopify admin bulk import/export: commonly known but not directly observed in fetched pages; the final doc attributes bulk import/export to the sample generally (BigCommerce/Square/WooCommerce observed) without Shopify-specific claims.
- Adobe Commerce variant/attribute mechanics were not observed in the fetched pages (only the catalog menu overview); Adobe is used for enterprise/B2B posture evidence only.
- Salsify evidence is positioning-level; used only for boundary reasoning.
- Standalone pure-play PCM products (outside commerce platforms) were not sampled; the "module realization" pattern is drawn from the five commerce products and should be stated as a sample observation, not a market census.

## Final Synthesis

Product Catalog Management is the seller-side discipline and application surface for maintaining the structured, sellable catalog of a business's offer: identified, described, priced product records; variants as the sellable units; organization into browsable structure; availability across the seller's channels. Its defining core is small (register + organization + sale orientation); everything else — variant machinery, media, bulk tooling, B2B price lists, AI enrichment — is mature but non-defining structure. The Type is overwhelmingly realized as the catalog module of commerce platforms and POS systems, with PIM as the adjacent upstream discipline for governed product content and syndication.
