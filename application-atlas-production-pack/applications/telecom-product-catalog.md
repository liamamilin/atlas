# Telecom Product Catalog

## Overview

A **Telecom Product Catalog** is the communications service provider's offer-definition system: the operator-side system of record that holds **what the operator sells** (sellable offers with their prices, bundles, and market scoping) and **how each offer is technically realized** (the service and resource specifications that turning an order into a working service must follow).

Its defining structure has three parts, and all three are needed for the Type to be recognizable:

```text
Offer-and-specification catalog (system of record)
└── Commercial-to-technical realization binding
    └── Governed publication, consumed at runtime by the commercial chain
```

- The **catalog of record** holds two linked kinds of persistent records: *offerings* — orderable entities carrying pricing, bundling structure, channel/market scoping, and validity windows — and *specifications* — reusable definitions of products, services, and resources with their characteristics.
- The **realization binding** links every sellable offer to the technical specifications that realize it: a product specification realized as customer-facing and resource-facing service specifications, which in turn require resource specifications — together with the relationships and rules (bundle composition, prerequisites, eligibility, decomposition rules) that downstream systems execute when orders flow.
- **Governed publication** moves catalog entities through managed lifecycle states with validity dating, and the published definitions become the runtime source of truth that sales channels, order management, charging, and provisioning all consume.

Remove the realization binding and the catalog degrades into a retail product list; remove the runtime consumption and it becomes a design-time modeling tool nobody executes against; remove the offers and only a technical specification library remains. The industry's own standard (TM Forum's product catalog API family) models exactly this pair — orderable offerings with pricing, plus the specifications "required to realize" them.

## Users & Context

The catalog sits between the operator's marketing/commercial organization and its fulfillment estate. It is authored by a small set of specialist roles and consumed by many systems and surfaces:

Primary authors:

- **product/offer designers** — build offerings and specifications, establish relationships between products, create bundles, assign the rules that govern how offers are sold
- **pricing designers / pricing managers** — maintain price books and price lists, configure promotions, discounts, and pricing schemes
- **catalog administrators** — set up and maintain the catalog's information structure, migrate data, run administrative jobs, manage permissions

Primary consumers:

- **sales agents and CSRs** — browse and search the catalog to find and sell the right offers (mature products provide guided product-selection search for this)
- **CPQ and quoting tools** — read offers, characteristics, and rules to configure and price deals
- **order management** — reads specifications, relationships, and decomposition rules at runtime to break a customer order into the technical fulfillment work
- **charging and billing** — consume offer prices, terms, and rating references
- **provisioning/activation** — consumes service and resource specifications that describe what to activate
- **digital channels and self-service** — surface published offerings to customers

The working context is an operator whose offers change constantly — bundles, promotions, convergence across mobile/fixed/TV, shorter product lifetimes, multiple sales channels. The catalog exists because those offers must be defined once, correctly, and consumed everywhere, rather than re-keyed per system.

## Core Model

### The defining core

```text
Catalog
├── Offering  (sellable, priced, scoped, validity-dated)
│   └── bound to → Product Specification
│                    └── realized as → Service Specification (customer-facing / resource-facing)
│                                       └── requires → Resource Specification
├── Characteristics  (design-time values; run-time values chosen at order capture)
├── Relationships & Rules  (bundling, realization, requirement, composition; eligibility and decomposition rules)
├── Pricing  (one-time / recurring charges, price lists, alterations, terms)
└── Lifecycle  (draft → published/active → retired; versions; validity windows)
```

**Offering.** The sellable entity — "orderable from the provider of the catalog," in the industry standard's wording. An offering carries its commercial identity: name, description, price(s), bundle membership, the channels, market segments, and places where it may be sold, commitment terms, and a validity window. An offering may be sellable standalone or only as a component of a bundle. Everything the customer sees and buys is an offering.

**Specification.** The reusable technical definition behind offers. Three kinds recur across the industry:

- *product specification* — the functional definition of what is sold (its characteristics, materials, terms); customer-facing; offers are realized from it
- *service specification* — the technical definition of a service, either customer-facing (CFS) or resource-facing (RFS); not sold to customers directly
- *resource specification* — the technical definition of a physical or logical resource (a device, a port, a SIM, network capacity); never customer-facing

Specifications carry **characteristics** — the attributes that describe them (speed, color, capacity, tenancy). Some characteristic values are fixed at design time; others are left open for the customer or sales agent to choose during order capture. An offering can restrict or override the specification's characteristic values (for example, offering only a subset of the specification's available options).

**The realization binding.** The structural signature of the Type: specifications are linked by typed relationships that determine how an order is fulfilled. Four relationship kinds recur across products and the industry standard (exact names vary by product):

- **bundling** — the offer or specification groups child offerings/specifications, often with mandatory/optional flags and minimum/default/maximum quantities
- **realization** — a product specification is realized by (implemented through) a service specification
- **requirement** — a service or product specification requires a resource specification to enable delivery
- **composition** — same-layer composition of specifications

Attached to these relationships sit **rules**: eligibility rules (which customers, channels, or contracts may buy what), availability rules, and **decomposition rules** — conditional logic, typically exclusion rules keyed on order-line characteristics, that determine which technical components an order for the offer actually generates.

**Pricing.** The catalog holds offer-level prices: one-time and recurring charges with their periods, price lists/price books scoped to channels, markets, or customer segments, alterations (discounts, allowances) often expressed as percentages, promotions, and commitment terms that influence price (a longer commitment commonly pricing cheaper than a short one). What the catalog does *not* hold is usage-rating logic — computing what a customer's actual consumption costs is the charging system's job, working from the plan the catalog defined.

**Catalog structure and lifecycle.** Offerings are organized into catalogs, categories, and product families. Every catalog entity carries a lifecycle state — typically draft, published/active, retired — and validity dating. Only published (or active/orderable) entities may be sold or consumed; drafts are work in progress; retired entities leave the sellable set. Mature products add versioning so that a specification or offering can be improved and re-published without destroying the definition that existing customers' services were built from.

### One structure, many implementations

The core model is conceptual. Implementations differ in where the lines are drawn:

```text
Concept:  Offer vs Specification
Implementations:  offer/product/service/resource spec types (spec-template authoring);
                  product offering + product/service/resource specification records;
                  commercial products vs technical products in one catalog

Concept:  Realization binding
Implementations:  typed specification relationships executed by order decomposition;
                  commercial↔technical product mapping consumed by orchestration;
                  service/resource specification references in the industry API family

Concept:  Governed publication
Implementations:  draft/published/retired/archived states; active+orderable flags;
                  lifecycle status + validity periods on every entity; version labels
```

## How It Works

### Authoring loop — define, compose, price, publish

```text
Define reusable building blocks (characteristics, picklists, object types, templates)
→ author specifications (product / service / resource) and their characteristics
→ link specifications with relationships (bundling / realization / requirement / composition)
→ attach rules (eligibility, availability, decomposition)
→ create an offering from a specification (the offer inherits the spec's data)
→ price the offering (one-time/recurring, price list, terms, promotions)
→ set the offering active and orderable → publish
```

The reusable-component pattern is the discipline's core economy: specifications are authored once and realized into many differently priced, differently targeted offers, so a new market offer is often a new price and scoping on an existing specification rather than a new definition.

### Change loop — version and retire

Offers change constantly. Mature products support creating a new version of a published specification or offering, updating its relationships, rules, and characteristics, and publishing the new version while the old one remains for existing customers. Offerings carry start and end dates; retiring an offer removes it from sale without disturbing in-flight orders or installed services. Keeping specifications current is operationally load-bearing: because change orders on existing services (moves, adds, changes, disconnects) are decomposed against the current specifications, out-of-date definitions surface as fulfillment failures — the reason versioning and retirement discipline matter.

### Consumption loop — the chain reads the catalog at runtime

```text
Sales channel / CPQ  → browse offerings, check eligibility, configure characteristics, price the deal
Order management     → decompose the accepted order against specifications,
                       relationships, and decomposition rules into
                       service orders (CFS/RFS) and resource orders
Charging             → rate usage against the plan the offer defined
Provisioning         → activate what the service/resource specifications describe
```

The catalog is not a document the chain consults occasionally; its definitions are executed. When a customer orders a bundled offer, the order-management system reads the bundling relationships to generate one order line per component, reads the realization relationships to generate customer-facing and resource-facing service orders, applies decomposition rules to include or exclude components based on the characteristics the customer actually chose, and uses quantity mappings to decide how many of each. This is why the catalog and order management are inseparable neighbors — the catalog defines, the order management executes.

### Capability tiers

**Defining core** — without these, not a telecom product catalog:

- sellable offerings with pricing, scoping, and validity
- product/service/resource specifications with characteristics
- the commercial-to-technical realization binding with relationships and rules
- lifecycle states gating what is sellable/consumable
- runtime consumption by the commercial chain

**Standard capabilities of mature products** — expected in the market, not definitional:

- catalog/category/family organization; bundle cardinalities (mandatory/optional, min/max quantities, group selections)
- offering-level overrides of specification characteristic values
- price lists/price books per channel or market; alterations and promotions; commitment terms
- eligibility/availability rules; versioning and effective dating
- designer tooling with reusable components; agent-facing browse/search; hierarchy views
- import/export and catalog federation; partner-product onboarding
- industry vocabulary alignment (offer/product/service/resource; customer-facing vs resource-facing service)

**Common variants** — see Variants below.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Designer / authoring workspace

The authors' primary surface: forms and graphical editors for specifications, offerings, characteristics, relationships, rules, and pricing components.

- typical information: specification hierarchies, characteristic definitions, relationship lists with type/mandatory/quantity fields, rule definitions, price components
- primary actions: create/edit/version entities, link specifications, attach rules, compose bundles, assign prices

### Pricing workspace

A dedicated surface for pricing designers: price books, price lists, pricing variables, promotions, discounts, charges, and time plans/policies, usually maintained as reusable components applied across many offerings.

### Catalog browse / search (agent- and CSR-facing)

The selling-side surface: agents and customer-service representatives browse catalogs and categories, search offerings, and check eligibility during lead, opportunity, quote, and order capture. Mature products add guided product-selection search that surfaces the most relevant customer solutions.

### Hierarchy / structure views

Verification surfaces showing the complete hierarchy of an offering and its associated product, service, and resource specifications — used to confirm that all entities and relationships have been defined and associated correctly before publication.

### Administration

Catalog administrators' surface: information-structure setup, data migration, administrative jobs, permissions.

### APIs and events

The integration surface through which consuming systems read the catalog: standardized operations to create, retrieve, update, and delete offerings, specifications, prices, categories, and catalogs; import/export jobs for catalog-to-catalog transfer; and lifecycle event notifications (create, attribute change, state change) so surrounding systems stay current. The TM Forum product catalog API is the industry's reference contract for this surface.

## Important Rules / Behaviors

### Publication gates selling

Only published (or active-and-orderable) offerings may be sold, quoted, or added to contracts; drafts are invisible to channels. This state gate is the catalog's primary control over what the market can buy.

### Sellable vs bundle-only

An offering may be sellable standalone or flagged as available only within a bundle. Bundle components carry mandatory/optional semantics and quantity bounds; a mandatory component is always included when the parent is ordered, an optional one only when the customer selects it.

### The catalog's rules are executed, not advisory

Decomposition rules keyed on order-line characteristics decide which service and resource orders an order generates; eligibility matrices decide which offers an agent may sell to a specific customer; quantity mappings decide how many domain orders a quantity produces. A rule error in the catalog propagates directly into fulfillment behavior.

### Stale specifications break change orders

Specifications must be kept current as products evolve; out-of-date specifications cause failures when MACD (move/add/change/disconnect) operations on existing services enter fulfillment. This is the operational reason versioning and retirement discipline matter.

### Offering-level characteristic control

An offering can restrict the specification's characteristic values (offering only a subset of the specification's options) and fix design-time values while leaving others to be chosen at order capture. The specification defines the possible; the offering decides the sellable.

### Price in the catalog, rating in charging

The catalog answers "what does the offer cost" (list prices, recurring periods, terms, alterations); the charging system answers "what did this usage cost" by rating consumption against the plan. The seam is stable even when deployment details vary.

### Validity windows

Catalog entities carry start/end (valid-for) dating; an offering outside its window is not sellable regardless of its lifecycle state. Effective dating lets operators prepare future offers and expire old ones without ad-hoc deletion.

## Variants

- **Catalog architecture** — a unified catalog holding commercial and technical definitions in one system (the dominant sampled pattern) versus the standards-family split of separate product, service, and resource catalogs linked by references. Both satisfy the realization binding.
- **Hosting and packaging** — licensed module on a CRM platform; platform applications inside a service-operations suite; portfolio component deployable alongside other vendors' OSS/BSS; component of a full BSS suite. All sampled products are suite components or licensed modules; the definition does not depend on hosting.
- **Industry breadth** — telecom-only catalogs versus multi-industry catalogs (communications, media, energy & utilities in one data model) and catalogs holding non-telco offerings alongside connectivity.
- **Tangible goods alongside services** — many catalogs also carry devices and equipment (the "tangible or intangible" span), so a phone and its activation service live in the same catalog; services-only catalogs are equally legitimate.
- **B2B depth** — enterprise offer hierarchies, site-level configuration, and hooks that let quoting tools run feasibility checks and pre-design against the catalog before an order is placed.
- **Partner and wholesale catalogs** — definitions exchanged with partners: onboarding a partner's products into the operator's catalog, or feeding partner systems with the technical descriptions of products the operator proposes to them.
- **Era-current assistance** — AI/GenAI-assisted offer configuration and catalog generation; an accelerating layer, not a structural one.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Telecom BSS | suite category that contains this component | BSS is the integrated commercial chain (sell → deliver → get paid → care); the catalog is the definition discipline the chain consumes |
| Telecom Order Management | primary runtime consumer | order management holds the order of record and orchestrates fulfillment by executing the catalog's specifications, relationships, and decomposition rules; it defines nothing about offers |
| Telecom Charging Platform | pricing seam | the catalog holds what the offer costs (prices, terms, alterations); charging computes what consumption costs (usage rated against plans/balances) |
| Telecom Provisioning Platform | downstream executor | provisioning activates what the catalog's service/resource specifications describe; the catalog never executes activation |
| Configure Price Quote / CPQ | selling-side consumer | CPQ reads the catalog to configure, price, and quote; the catalog is the foundation, CPQ the deal-level workflow |
| Product Information Management / PIM | same word, different world | PIM manages retail product content (descriptions, media, channel syndication) for goods; no technical realization layer, no runtime fulfillment consumption |
| Product Catalog Management (retail) | adjacent | organizes sellable items for merchandising; lacks the service/resource specification layer and decomposition/activation consumption |
| Digital Product Catalog | customer-facing sibling | an interactive catalog presented to shoppers; the telecom catalog is operator-side definition infrastructure |
| Business Rules Management System | rule overlap only | catalog rules are offer-scoped and attached to catalog entities; a BRMS is a general-purpose rule engine across domains |
| Master Data Management | data-governance neighbor | MDM governs cross-domain master data; the catalog is a domain system of record with offer semantics and chain consumption |

The boundary with Telecom Order Management is the most consequential: the two are joined at runtime (decomposition executes the catalog's definitions), and confusing them is easy because both speak the specification vocabulary. The structural test is simple — the system that holds the order of record and orchestrates fulfillment is order management; the system that holds the offer and specification definitions everyone reads is the catalog.

## Representative Products

- Salesforce — Enterprise Product Catalog (EPC) / Shared Catalog, Communications Cloud
- ServiceNow — Product Catalog (Order Management / Telecommunications, Media & Technology)
- Ericsson — Catalog Manager
- Amdocs — CatalogONE
- Netcracker — Commerce Management (unified Product Catalog)

Industry standard consulted as corroboration: TM Forum TMF620 Product Catalog Management API (v5.0.0).

## Sources

Research date: **2026-09-10**

- Salesforce — Trailhead: *Industries EPC Foundations* (Discover Industries EPC), *Industries Products and Product Bundles* (Explore Products and Product Specifications); developer docs: Product & Catalog Management data model, EPC REST APIs; salesforce.com/communications/wholesale-software
- ServiceNow — official product documentation (docs.servicenow.com, `australia` release, via official GitHub mirror): Setting up specifications and product offerings; Create specification relationships, quantity mapping, and decomposition rules; Order decomposition; Create product offerings; Create a product offering catalog; Product Catalog Management
- Ericsson — Catalog Manager product page (ericsson.com, Business and Operations Support Systems portfolio)
- Amdocs — CatalogONE positioning (amdocs.com product and use-case pages)
- Netcracker — Commerce Management product page (netcracker.com)
- TM Forum — TMF620 Product Catalog Management API v5.0.0 (official Open API specification mirror), API user guide and ODA directory entries

> Sourcing limitation: Amdocs' product pages were not directly fetchable from the research environment (access blocked); CatalogONE evidence is verbatim page text recovered through search excerpts and the prior Telecom BSS research pass. Netcracker and Ericsson evidence is product-page tier; no public operational manuals were reachable for those products. Precise operational parameters (exact state-machine names beyond those documented, numeric limits, default settings) are therefore not asserted in this document; product-specific observations remain in the Research Notes.
