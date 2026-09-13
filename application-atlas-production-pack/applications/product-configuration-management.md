# Product Configuration Management

## Overview

A **Product Configuration Management** application is the manufacturer's system of record for a product's variant space: the options a product can be built with, the rules that define which combinations are valid, and the machinery that turns a set of selections into a concrete, buildable product definition.

Its defining core is small — three structures that only exist together:

```text
Configuration model (options + validity rules + linkage to the product's structure)
└── Variant resolution (selections validated against the rules → a buildable variant definition)
    └── Maintained model lifecycle (the model itself is tested, released, and changed over time)
```

The resolved output is a *product definition* — a variant bill of materials, a manufacturing route, order-specific design or manufacturing data — consumed by engineering and production. That build-side orientation is what separates this Type from sell-side configuration tools, whose center of gravity is the priced offer and the quote.

Everything else commonly associated with the category — declarative constraint languages, effectivity dates, cross-system APIs, 3D visual configuration, AI-assisted modeling — is accumulated market structure or era-typical capability. The definition survives without any of it: a paper option catalog with written combination rules, a manually assembled order-specific build sheet, and a revised catalog satisfies the same three structures.

## Users & Context

The Type serves manufacturers whose products are configurable — from assemble-to-order with variable features to engineer-to-order with order-specific engineering.

Primary users:

- **product engineers / product managers** — define the options, the rules that govern valid combinations, and how options map to the product's structure
- **configuration model administrators** — maintain, test, and release model versions as the product evolves

Secondary users:

- **sales and sales engineers** — run configuration sessions against the released model when quoting or entering orders
- **manufacturing / industrial engineering** — consume the generated variant bills of materials and routes
- **IT / integration owners** — keep the model synchronized across PLM, ERP, CPQ, and service systems

The recurring pain the Type addresses is drift: when options and rules live in spreadsheets and in separate systems, invalid combinations reach quoting, ordering, or production, and products get sold that cannot be built as ordered.

## Core Model

### The Defining Core

**The configuration model.** One persistent model defines one product's variant space. It contains:

- *selectable characteristics* — the options or attributes a configuration can choose from (feature sets, materials, sizes, performance levels)
- *validity rules* — the constraints that define which combinations are allowed, ranging from simple inclusion/exclusion rules to declarative constraint expressions and computed values
- *structure linkage* — the mapping from options to the product's structure: which bill-of-material lines and route operations each option brings in, and which properties it sets

The model is the shared source of truth for what the product can be. Mature products emphasize exactly this: options and rules "directly linked to the bill of material," consolidated from the spreadsheets and disconnected systems where they otherwise live.

**Variant resolution.** A configuration session takes a set of selections over the model, validates them against the rules, and resolves them into a concrete variant definition — a variant bill of materials and route, or order-specific design and manufacturing data. The resolved variant is an identified record in its own right, trackable through inventory and production. The underlying pattern is a master structure carrying all options — in industry usage often called a "150% BOM" — from which each configuration's specific structure is generated.

**The maintained model lifecycle.** The model itself is a controlled artifact. It is tested before release, versioned, and changed under control as the product evolves — so the variant space stays current, and every consumer works from the same released logic.

### Standard Capabilities

Mature products commonly add the machinery that makes the core usable across an organization:

- **option/attribute catalogs** with enterprise-wide visibility, replacing scattered spreadsheets
- **declarative rule authoring** — constraint expressions, table constraints, case tables, calculations — so models can be maintained without custom code
- **model validation and test sessions** before release, with conflict-resolution guidance when rules contradict each other
- **effectivity management** — rules and options that are valid per date, product line, or plant
- **cross-system delivery** — APIs and synchronization so ERP, CPQ, PLM, and service systems consume the same model instead of maintaining their own copies
- **guided configuration surfaces** — structured selection pages, templates, and attribute groups that walk a user to a valid configuration
- **portfolio views** — product family matrices and offered-vs-sold analysis over the variant space (present in some products)

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:   selectable characteristics
Realized as: options, attributes, characteristics, choices

Concept:   validity rules
Realized as: expression constraints, table constraints, rule logic, constraint solvers

Concept:   structure linkage
Realized as: conditional BOM lines and route operations, CAD model generation, manufacturing data generation

Concept:   resolved variant
Realized as: a variant BOM + route with its own ID, generated CAD models and drawings, validated configuration data delivered by API
```

## How It Works

### Define the variant space

```text
Identify the product family and its common structure
→ define the selectable options/attributes
→ write the rules that govern valid combinations
→ link options to BOM lines, route operations, or design elements
```

### Validate and release the model

```text
Test the model with trial configuration sessions
→ resolve rule conflicts
→ create a model version
→ approve and activate it for use
```

A released version is what sales, ordering, and production see. Until a version is released for use, it cannot be configured against.

### Resolve a configuration

```text
Start a configuration session (from a quote, an order line, or engineering)
→ select options, guided by the rules
→ invalid combinations are rejected as they are chosen
→ complete the selection set
→ the system generates the variant definition: variant BOM, route, and/or design deliverables
→ the resolved variant is recorded with its own identity and tracked downstream
```

### Change the product

```text
A product change arrives (new option, changed rule, new component)
→ the model is updated and re-tested
→ a new version is released
→ effectivity rules determine which configurations and plants the change applies to
→ downstream systems pick up the updated model
```

### The recurring loop

Model definition → validation/release → configuration sessions → variant generation → consumption by engineering, production, and sales → product changes → model updates. The model is the hub; every other step reads from it or writes back to it.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Model editor

The authoring surface for the configuration model.

- the model's structure as a navigable tree (components, subcomponents, attributes, rules, BOM lines, route operations)
- primary actions: define options and attribute types, write rules and constraints, map options to structure elements, consolidate models from other systems

### Validation / test surface

Where a model is proven before release.

- trial configuration sessions, rule-conflict listings, per-constraint and whole-model checks
- primary actions: run a test configuration, inspect conflicts, fix rules, mark the model ready

### Version / release management

The control surface for the model lifecycle.

- model versions with status, approval and activation steps, effectivity settings
- primary actions: create version, approve, activate, retire

### Configuration session

The guided surface where a variant is resolved.

- selection pages organized by attribute groups, templates for common configurations, real-time validity feedback, sometimes 3D visualization
- primary actions: select options, resolve conflicts, complete the configuration, generate the variant

### Generated-output views

The resolved variant's definition.

- variant bill of materials, manufacturing route, generated drawings/models or manufacturing data, the configuration's identity
- primary actions: review, release to production, hand off to ERP or manufacturing systems

### Integration / API surfaces

Where other systems consume the model.

- model-consumption APIs, synchronization to ERP/CPQ/PLM, variant release across sites or companies

## Important Rules / Behaviors

### Only valid combinations resolve

The rules are enforced at configuration time: selections that violate constraints are rejected while the user is still choosing, not discovered later in production. This is the behavior the Type exists to guarantee.

### Completeness gates generation

A configuration must be a complete, consistent selection set before the system generates the variant definition; if the BOM or route cannot be produced from the selections, the session commonly fails with an error rather than producing a partial product.

### Released versions are the only configurable truth

Model versions are commonly gated by approval and activation before they can be used in configuration sessions. What sales and production configure against is a released version, not a work-in-progress edit.

### Each resolved variant is an identified record

The output of a session is not just data — it is a tracked record with its own identity, carried through inventory, production, and the supply chain.

### Effectivity bounds the variant space over time

Rules and options commonly carry validity conditions (dates, product lines, plants), so the same model serves successive product generations without forking.

### Model changes propagate under control

Changes to options and rules are synchronized to the systems that consume them — plant-specific production information, quoting systems, service documentation — so the variant space does not drift out of alignment across the enterprise.

## Variants

The Type is realized at several hosting loci, which are packaging variants of one model rather than separate Types:

- **standalone configuration layer** — a dedicated system holding the shared configuration model, consumed by PLM, ERP, and CPQ through APIs; the posture marketed as "configuration lifecycle management"
- **PLM-embedded variant management** — options, choices, and rules managed beside the BOM and CAD data inside the product-lifecycle estate, with change management and effectivity inherited from the suite
- **ERP-native product configuration** — configuration models maintained in the ERP's product master, configured from sales and production order lines, generating variant BOMs and routes directly into the supply chain
- **CAD-embedded design automation** — rules maintained beside the CAD system, generating order-specific models, drawings, and manufacturing data; commonly packaged with configurator and CPQ surfaces on top
- **CPQ-suite configuration component** — the configuration engine inside a sell-side suite, where design automation and order fulfillment hang off the quote loop

Other variant axes:

- **production strategy**: configure-to-order (variable features on a common platform) vs engineer-to-order (order-specific engineering), with migration programs between them
- **rule depth**: from simple attribute matrices with trivial rules to declarative constraint systems with computed values
- **output flavor**: BOM+route generation vs CAD deliverable generation vs validated model data delivered by API
- **visual configuration**: 3D/interactive configuration surfaces for sales use, over the same model

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Configure Price Quote / CPQ | closest neighbor, sell-side | CPQ's center is the commercial offer — valid sellable offer, computed price, quote, approvals; this Type's center is the variant space and its buildable resolution. The same model can feed both; vendors themselves sell the configuration layer and the CPQ layer as separate products |
| Bill of Materials Management | structural sibling | BOM management owns the controlled structure of specific product definitions (item + structure + revision); this Type owns the rule-governed space that generates many concrete BOMs from one model. Configurable BOMs are a capability there; the variant space is the center here |
| Product Lifecycle Management / PLM | broader estate | PLM owns the product-data estate (CAD/PDM/BOM/change/documents); variant and configuration management is one capability inside it. A standalone configuration layer sits across PLM/ERP/CPQ without owning the estate |
| Engineering Change Management | process sibling | ECM owns the change process (requests, orders, approvals) over engineering objects; this Type embeds model versioning and release as one leg, scoped to the configuration model |
| Product Information Management / PIM | content sibling | PIM manages commercial/catalog content for selling channels; this Type manages technical variant logic and buildable definitions. Option lists may appear in both with different content and purpose |
| Product Catalog Management | adjacent | catalogs organize sellable offerings; they may expose options but do not resolve selections into buildable definitions |
| Manufacturing Execution System / MES | downstream consumer | MES executes released production orders; the resolved variant definition produced here is an input to planning and execution, not the execution itself |
| Visual product configurators (e-commerce) | selling surface | buyer-facing 3D/visual configuration is a channel over the configuration model, not the model's system of record |

The boundary with CPQ is the most important one, because both are called "configuration." The structural test: if the product's center of gravity is the priced offer and the quote loop, it is CPQ; if it is the variant space and the buildable definition, it is this Type.

## Representative Products

- **Configit Ace** — standalone SaaS configuration and variant management layer; the model-centric "shared source of truth" posture
- **PTC Windchill** (variant management / configuration management) — PLM-embedded variant management linked to BOM and CAD data
- **Microsoft Dynamics 365 Supply Chain Management** (product configuration) — ERP-native constraint-based configuration models resolved from order lines
- **DriveWorks** — SOLIDWORKS-embedded design automation and configurator; the CAD-deliverable pole
- **Tacton** — CPQ-centered suite with design automation; included as boundary evidence for the sell-side seam

The defining core was checked against older and simpler realizations (paper option catalogs, the 1980s expert-system configurator generation, 1990s ERP configurators) to avoid defining the Type by the current SaaS/AI-era packaging.

## Sources

Research date: **2026-09-09**

- Configit — Configuration Lifecycle Management (approach), Configit Ace (product), Align Engineering Data (solution), home page — https://configit.com/solutions/clm/ , https://configit.com/configit-ace/ , https://configit.com/solutions/align-engineering-data/ , https://configit.com/
- PTC — Windchill PLM, Product Variant Management, Product Configuration Management (capability pages) — https://www.ptc.com/en/products/windchill , https://www.ptc.com/en/technologies/plm/product-variability-management , https://www.ptc.com/en/technologies/plm/product-configuration-management
- Microsoft — Dynamics 365 Supply Chain Management, "Product configuration overview" — https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/build-product-configuration-model
- DriveWorks — home page — https://www.driveworks.co.uk/
- Tacton — Design Automation (use case) — https://www.tacton.com/use-case/design-automation/

> Sourcing limitation: SAP's help portal (Advanced Variant Configuration) and Siemens Teamcenter documentation were not reachable from the research environment (JavaScript shells / gated portals); Aras product pages returned errors. The ERP pole therefore rests on Microsoft's Tier-1 documentation, and the PLM pole on PTC's product pages. SAP- and Siemens-specific operational details are intentionally not asserted. Vendor marketing figures (percentages, error counts) are recorded as claims in the Research Notes, not as facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
