# Product Catalog Management

## Overview

A **Product Catalog Management** application is the seller-side system for building and maintaining the structured, sellable catalog of products a business offers. It holds each product as an identified, described, priced record; organizes records into a browsable structure; defines the sellable units (variants); and controls where and to whom each product is available across the seller's sales channels.

The defining core is deliberately small:

```text
Seller-maintained catalog register
└── Product record (identified offer: name, description, price)
    └── Organization into a browsable structure (categories / collections)
    └── Availability for sale (where and to whom each product can be sold)
```

Everything else commonly associated with catalog work — variant/SKU machinery, media libraries, bulk import, B2B price lists — is standard capability that mature products add, not part of what makes the Type what it is. A paper-era mail-order catalog, a point-of-sale item file, and a modern hosted-store catalog all satisfy the same core.

The catalog is the *offer*, not the selling machine. The storefront presents it, the cart and checkout transact on it, the POS rings it up — catalog management is the surface where the offer itself is created and kept current.

## Users & Context

The primary user is the seller's catalog owner — a merchant, store admin, e-commerce manager, or merchandiser responsible for what the business sells and how it is presented. Typical work:

- add new products as the assortment changes
- keep prices, descriptions, images, and stock current
- organize the assortment so buyers can find it
- decide which products appear in which channel or location

Secondary users:

- staff with limited catalog permissions (some products gate item editing behind specific permissions)
- B2B sellers who maintain company-specific assortments and pricing
- content specialists who enrich records (copy, photography, attributes)

The work environment is an administrative back office: a products list, an editor per record, and organization tools. It is not customer-facing; customers meet the catalog's *output* in the storefront, the POS item grid, or a published catalog.

## Core Model

### The defining core

**Catalog register.** The application maintains a persistent, accumulating set of product records in one seller-controlled place. The register is the system of record for the offer: every product the business sells exists as a record here, whether or not it is currently visible anywhere.

**Product record.** The central object. At minimum it identifies the offer — a name, a description, a price — and carries whatever the seller needs buyers and operations to know: images, identifiers (SKU, barcode), category, tags. Records are individually created, edited, duplicated, and retired. In the researched sample every product carries a kind — physical good, digital/downloadable, service — and the kind shapes fulfillment expectations and sometimes the editable fields.

**Sellable organization.** Products are arranged into a browsable structure: categories, collections, or menus. This is what turns a pile of records into a *catalog*. Two patterns coexist:

- a navigational tree (the storefront's menu is often driven directly by it)
- parallel groupings (collections) that slice the same products by campaign, season, or theme

A product commonly belongs to more than one grouping, and groupings are merchant-defined; some products additionally offer rule-based membership (a collection computed from conditions rather than hand-picked).

**Sale orientation.** The catalog exists to be sold from. Records carry an availability state — working vs published, visible vs hidden — and are connected to the seller's sales channels (online store, point of sale, marketplaces, delivery apps). A record that is not published to any channel is still in the register but not on sale.

### Standard capabilities

Mature products add the machinery that makes a real catalog practical:

- **Variants as the sellable unit.** A product with choices (size, color) expands into variants — the concrete sellable items. Each variant carries its own SKU, price, stock, and often its own image; a product without options is its own single variant. Inventory is normally tracked against variants rather than the parent product.
- **Options vs fulfillment selections.** A recurring distinction: choices that *select a variant* (change which SKU is picked) versus choices that *modify fulfillment* (engraving, gift wrap, insurance) without changing the SKU. The latter may carry price adjustments.
- **Media management.** Images with a main/thumbnail convention, often video, occasionally 3D models, attached to products and variants.
- **Custom attributes.** Extensible fields beyond the base record — attributes, custom fields, metafields — for specifications, compliance data, or integration payloads.
- **Pricing overlays.** Beyond the base price: sale/compare-at prices, quantity-based pricing, and — in B2B-facing products — customer- or company-specific price lists and gated assortments.
- **Availability controls.** Per-channel publication, per-location assignment, and visibility gating by customer group; some products combine location and channel into a matrix of availability.
- **Bulk tooling.** Import/export (typically spreadsheet-based), bulk editing of prices/stock/categories, and duplication of an existing record as a starting point.
- **Inventory linkage.** Stock levels visible and editable from the catalog, normally tracked per variant and often per location.
- **Search and filter in the admin.** Locating records by name, SKU, status, category, or attribute across a growing register.
- **SEO fields.** Page titles and descriptions per product, since the catalog feeds searchable storefronts.
- **AI assistance.** Some current products generate product descriptions or suggest enrichment of names and descriptions from within the editor.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Product record
Realized as: product (hosted commerce), item (POS systems), product type variants (open-source plugins)

Concept:   Sellable organization
Realized as: category tree, collections (manual or rule-based), menus (food service)

Concept:   Availability
Realized as: channel publication, location assignment, customer-group visibility, shared B2B catalogs
```

A reader who has only seen one implementation — say, a hosted store's products-and-collections admin — should still recognize a POS item library or an enterprise B2B shared catalog as the same Type.

## How It Works

### Build the register

```text
Create a product record (name, price, description)
→ or import records in bulk from a spreadsheet / supplier file
→ assign a kind (physical / digital / service)
→ save as a working record
```

New records typically start in a non-public working state. The register accumulates: retired products are archived or hidden rather than deleted.

### Structure the offer

```text
Create categories / collections
→ assign products (manually, or by rule)
→ order products within the structure
```

The organization structure usually drives navigation on the selling surfaces directly, which is why catalog owners treat it as merchandising work, not filing.

### Define the sellable units

```text
Add options to a product (e.g. size, color)
→ the application generates the variant combinations
→ set per-variant SKU, price, stock, image
→ optionally add fulfillment selections (modifiers) with price adjustments
```

The variant is what stock, orders, and reporting attach to. Getting the option structure right early matters because variants are generated from option combinations.

### Enrich and price

```text
Add media (images, video)
→ fill attributes / custom fields
→ set SEO fields
→ set the base price and any overlays (sale price, quantity breaks, customer-specific pricing)
```

### Make it available

```text
Choose the sales channels / locations for the product
→ publish (or schedule publication)
→ the record appears on those selling surfaces
```

Availability is per product and reversible: unpublishing removes it from a channel without destroying the record. In B2B settings, availability and pricing can be scoped to a customer company rather than to a public channel.

### Maintain

```text
Monitor the register (search, filter, catalog summaries)
→ bulk-edit prices / stock / categories
→ duplicate records for similar products
→ archive retired products
```

Catalog maintenance is continuous: prices change, stock moves, assortments rotate. The application's job is to make the register stay true while the business changes around it.

## Interfaces

### Products list / grid

The register's front door.

- Purpose: see and work the whole assortment.
- Typical information: name, image thumbnail, SKU, price, stock, status/visibility, category.
- Primary actions: search/filter, create, open for editing, bulk edit, duplicate, archive, import/export.

### Product editor

The per-record workspace.

- Purpose: compose one product completely.
- Typical information: name, description, kind, media, options and variants, price fields, inventory, category assignment, attributes, SEO.
- Primary actions: edit fields, manage variants, upload media, set pricing, save/publish.

### Category / collection editor

The organization surface.

- Purpose: build and maintain the browsable structure.
- Typical information: hierarchy, member products, visibility, sort order.
- Primary actions: create/rename/reorder, assign or rule-match products, control visibility.

### Availability / publication panel

The channel connection surface.

- Purpose: control where a product sells.
- Typical information: channels, locations, per-channel status, customer-group visibility.
- Primary actions: publish/unpublish per channel, assign locations, scope to customer groups.

### Import / bulk tools

- Purpose: operate on the catalog at scale.
- Typical information: import templates, error reports, affected-record previews.
- Primary actions: import, export, bulk price/stock/category updates.

## Important Rules / Behaviors

- **The variant is the sellable unit.** Price, stock, and identifiers attach to variants; the parent product aggregates them. A product with no options still has one implicit sellable unit.
- **Not every choice creates a variant.** Fulfillment selections (engraving, add-ons) change the order, not the SKU; they cannot be stocked against.
- **Working vs published.** Records commonly exist in a non-public state before publication, and published records can be hidden or archived without deletion. Exact state names vary by product.
- **Availability is scoped, not global.** A record can be live in one channel or location and absent in another; visibility can additionally be gated by customer group. A product can be "enabled" yet invisible to a given audience.
- **Organization is merchant-defined.** Categories and collections are the seller's merchandising decisions; a product may sit in several groupings at once, and there is often no single "primary" grouping.
- **Edits propagate to selling surfaces.** A catalog change reflects across the connected channels — storefront, POS, apps — because they sell from the same register.
- **Catalog editing can be permission-gated.** In multi-staff settings, who may create or change items is controlled separately from who may sell.

## Variants

Common forms the Type takes:

- **Hosted commerce catalog** — products + collections inside an all-in-one store platform; multi-channel publication; SMB/mid-market focus.
- **Open-source storefront catalog** — the same structure as a plugin; product types (simple, variable, grouped, external) and self-hosting are the differentiators.
- **POS-embedded item library** — the catalog as the item file behind a point-of-sale system; items typed for the domain (retail goods, prepared food, services, tickets); availability managed as locations × channels.
- **Enterprise / B2B catalog** — company-scoped assortments and price lists (shared catalogs), customer-group gating, negotiated pricing layered over the public catalog.
- **Brand-side content-heavy catalog** — when the seller is a brand distributing rich product content to many retail endpoints, catalog work drifts toward product-information management (see Related Types).
- **Domain-specific catalogs** — food-service menus, telecom service offerings: same structural core, specialized objects and rules; treated as separate Types in this atlas.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Product Information Management / PIM | adjacent, upstream | PIM governs product *content* as master data — intake, enrichment, translation, quality — and syndicates it to *other parties'* selling systems; catalog management maintains the *sellable offer* for one's own channels. Commerce platforms embed authoring inside the catalog; PIM suites may publish buyer-facing catalogs — the boundary is one of center of gravity |
| Digital Product Catalog | output vs tool | the published, buyer-facing catalog (browsable, shareable) is a product of catalog management, not the management surface |
| E-commerce Platform / Online Store Builder | container | the platform adds storefront, cart, checkout, orders; catalog management is its offer-maintaining module. In the researched sample, standalone pure-play catalog products were rare — the Type is usually realized as a module |
| Retail POS | consumer of the catalog | POS transacts live against the item file; catalog maintenance is a separate back-office surface over the same data |
| Restaurant Menu Management | domain-specific sibling | same core (items, categories, modifiers) with food-service objects (menus, kitchen names, nutrition); separate Type |
| Telecom Product Catalog | domain-specific sibling | manages telco service offerings and their commercial structure; separate Type |
| Inventory Management / ERP item master | negative boundary | records what is stocked or procured, without sellable organization or channel availability; remove the sale orientation and a catalog becomes an item master |
| Master Data Management | broader discipline | org-wide data governance across domains; catalog management is specific to the sellable product offer |

## Representative Products

- **Shopify** — hosted commerce; products, collections, variants, and multi-channel publication
- **BigCommerce** — open SaaS; explicit catalog concepts (products, variants/SKUs, category tree, customer groups)
- **Square** — POS-embedded item library; typed items; locations-and-channels availability
- **Adobe Commerce** — enterprise open-source; category foundation, B2B shared catalogs
- **WooCommerce** — open-source WordPress plugin; product types and variations

## Sources

Research date: **2026-09-06**

- Shopify — Product object (GraphQL Admin API, official developer documentation): https://shopify.dev/docs/api/admin-graphql/latest/objects/Product
- BigCommerce — Catalog Overview (official developer documentation): https://developer.bigcommerce.com/docs/store-operations/catalog
- Square — Create and edit items (official Help Center): https://squareup.com/help/us/en/article/5328
- Adobe Commerce — Catalog menu (official admin documentation): https://experienceleague.adobe.com/en/docs/commerce-admin/catalog/catalog-menu
- WooCommerce — Adding and Managing Products (official documentation): https://woocommerce.com/document/managing-products/
- Salsify — product pages (PIM / Syndication / Catalog Sites), used for boundary reasoning only: https://www.salsify.com/

> Sourcing limitation: the Shopify Help Center was not reachable from the research environment (HTTP 403); Shopify evidence rests on the official developer product-model documentation, which describes the same admin objects. Salsify's help center returned no content, so its role in this document is limited to positioning-level boundary reasoning. Precise operational details (numeric limits, exact state names, plan-specific capabilities) are intentionally not asserted where the fetched evidence did not support them; such details remain in the paired Research Notes.
