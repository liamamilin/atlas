# Seed Production Management

## Overview

A **Seed Production Management** application is the seed-producing organization's multiplication system of record. It plans which varieties are multiplied on which fields by which growers, tracks every seed lot's identity, generation, and quality from the parent seed that goes into the ground to the labeled bag that leaves the warehouse, and gates each lot's release for sale on recorded inspection and test results.

The work it manages is unlike ordinary crop production. The harvested product is not food or feed but **planting seed**, and its value lies in being exactly the named variety at the expected generation of multiplication, genetically pure and physically clean. That is why the application is organized around lots that carry varietal identity and lineage, rather than around fields or SKUs alone. Everything else a seed business does — contracting growers, conditioning seed, testing it in the lab, storing and selling it — hangs off that lot spine.

The boundary is equally clear: this is the **production side** of the seed business. It is not the breeding program that creates varieties (though some platforms bundle breeding modules), and it is not the certification agency that officially inspects and certifies seed (the agency is an external authority whose outcomes this system records and reacts to).

## Users & Context

The primary user is the **seed production organization**: a seed company, a breeder with a multiplication program, a cooperative or production organization multiplying varieties for seed companies, or a contract-multiplication specialist. Typical roles:

- **Production manager / planner** — builds the multiplication plan: which varieties, which generation of parent seed, how much area, on which fields and growers; balances expected demand against contracted supply
- **Grower relations / field officers (production agronomists)** — recruit and manage contract growers, agree contracts, provide parent seed and technical guidance, monitor crops in season, support roguing and pollination management
- **Contract growers** — execute the field work under contract; in some deployments they report activities and receive settlements through the system
- **Conditioning plant manager / operators** — run cleaning, drying, grading, treatment, and bagging against production orders, keeping lot identity intact
- **QA / laboratory staff** — sample lots, record germination, purity, moisture, and seed-health results, decide or recommend lot disposition
- **Inventory / warehouse staff** — store lots by location and state, manage carryover between seasons
- **Sales / distribution** — sell and ship against specific lots
- **Finance** — grower settlements and lot-level production costing

The rhythm is **seasonal and multi-year**: a multiplication cycle spans sowing to sale, lots carry over between seasons, and generations chain across years (this year's certified lot is next cycle's parent seed). Work happens in the office (planning, contracts, records), in the field (monitoring, inspection — often on mobile, sometimes offline), and in the plant (conditioning, bagging).

## Core Model

### The defining core

Three structures, held together, make this application what it is:

```text
Variety (master data, with generation/class of seed stock)
  ↓ multiplication plan
Production contract (grower × variety × field × season)
  ↓ harvest intake
SEED LOT (unit of record: variety + generation + lineage + quality record)
  ↓ conditioning & testing under identity
Released lot → inventory → sale / next-cycle parent seed
```

**1. The seed lot as unit of record.** A seed lot is a persistent, identified quantity of seed of a named variety. It carries its generation or class of seed stock (the chain that runs from breeder/basic seed down through certified classes, however the organization names it), its lineage — which parent lot and which field produced it — and its own lifecycle from harvest intake through conditioning, testing, and disposition. The lot accumulates its quality record as it moves and remains addressable after completion: in inventory, in carryover, in a recall, or as the ancestor of later lots. If the unit of record were the field or the SKU instead of the lot, the application would be crop management plus a warehouse system.

**2. Variety-anchored multiplication planning over contracted production.** The application holds the plan that decides which variety is multiplied where, by whom, and at what scale: variety and parent-seed generation on one side, grower, field, area, and expected yield on the other, bound by a production contract that carries quality standards and settlement terms. Seed-specific siting constraints are applied at allocation — isolation from other kinds, previous-crop requirements, and the rule that the class of seed planted determines the class the field can produce. Without this planned multiplication, growers and fields are just contract farming.

**3. Identity-and-quality gatekeeping to lot release.** Field inspections (isolation, off-types, weeds, disease, conformity to the variety description) and laboratory tests (germination, purity, moisture, seed health) are recorded against the field and the lot. Results determine the lot's status — approved, held, downgraded, rejected — and whether it may progress to packaging and sale, and at what class or label. Lot identity must be preserved through every movement and processing step; the quality record travels with the lot. Without these gates, lots move on logistics alone, and the application becomes a produce-traceability tool.

The **binding** across all three: the managed product is planting seed, whose worth is varietal identity and genetic purity. Remove that — manage the same fields, contracts, and lots as anonymous commodity — and the territory becomes grain management.

### Standard capabilities

Mature products commonly add, on top of the defining core:

- **Grower contracts and settlements** — contract lifecycle from creation through execution to settlement, with payment computed from delivered quantity, quality results, and contract terms (deductions for sub-standard lots are part of the same calculation)
- **Field records and technical monitoring** — plots with boundaries and history, in-season activity records, monitoring visits, mobile (often offline) capture of observations and photos
- **Conditioning and processing orders** — cleaning, drying, grading, blending, and treatment executed as orders at the plant, with barcode/QR identification keeping lot identity through the line
- **Lot inventory** — lots held by location and state (raw, conditioned, treated, bagged), supporting allocation to orders and carryover between seasons
- **Laboratory management** — test requests, results, and reports of analysis linked to the lots they concern
- **Demand planning** — sales forecasts and bookings feeding the multiplication plan and grower allocations
- **Sales and distribution** — orders, deliveries, and invoicing at lot/batch level
- **Dashboards and reporting** — plan versus actual, quality outcomes, inventory position, across sites

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:  generation/class of seed stock
Implementations:  certification classes (breeder → foundation → registered → certified
                  under official schemes), or internal company class schemes

Concept:  production contract
Implementations:  paper-era contracts digitized as records, portal-signed agreements,
                  contract line items with price formulas and quality-grade deductions

Concept:  lot identity
Implementations:  lot numbers on tags and bulk certificates, barcode/QR on bags and
                  pallets, batch genealogy chains from grower lot to finished goods

Concept:  quality gate
Implementations:  internal QA release, official certification status per lot,
                  or both layered together
```

A reader who has only seen one implementation — say, certified production under a government scheme — should still recognize a company running internal QA classes on its own farms as the same application.

## How It Works

The canonical loop runs once per multiplication season, with lots chaining across seasons:

**1. Plan the multiplication.** Demand forecasts and sales bookings set variety-level quantity targets. The production planner selects growers and fields, agrees production contracts (area, expected yield, quality standards, price and settlement terms), and allocates parent seed of the right generation to each field — checking isolation and previous-crop constraints before committing.

**2. Support and monitor the growing crop.** Parent seed and inputs are issued to growers. Field officers record activities and monitoring visits, guide roguing, and — in hybrid crops — track pollination. Field inspections are scheduled and recorded; a failed inspection can be corrected and re-inspected, but an uncorrected failure removes the field's seed from its intended class.

**3. Harvest and intake.** Growers report harvest; delivered seed is weighed in and becomes a **grower lot** tied to the field, variety, and class that produced it. From this point the lot, not the field, is the moving unit.

**4. Condition and test.** Lots move into conditioning — cleaning, drying, grading, treatment, sometimes blending — under production orders that preserve identity. Samples are drawn and tested (germination, purity, moisture, health). Results post against the lot and update its status: approved, held, downgraded, or rejected.

**5. Package, inventory, release.** Approved lots are bagged and labeled with the identifiers that make them traceable — lot number, variety, class. They enter inventory by location and state, and become sellable when their quality and (where applicable) certification status is complete.

**6. Sell, ship, and settle.** Orders are allocated against specific lots; deliveries and invoices reference the batch. Grower settlements are computed from delivered quantity, quality results, and contract terms.

**7. Carry over and chain the generations.** Unsold lots carry over into the next season, remaining in inventory and in the genealogy chain. Lots reserved or returned to the multiplication program become the parent seed of the next cycle, extending the chain from the original breeder seed to the bag the farmer buys.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Production planning workspace

The planner's home for the season.

- variety × area × grower plan, demand versus contracted supply, parent-seed availability
- primary actions: create/adjust the plan, allocate fields and parent seed, check siting constraints

### Grower and contract records

The counterpart registry and the contract lifecycle.

- grower profiles (farms, fields, capability, history), contract terms (variety, area, expected yield, quality standards, price/settlement), contract status
- primary actions: onboard grower, create/amend contract, record performance, run settlement

### Field / plot records

The agronomic backbone.

- field boundaries and maps, crop history, current multiplication (variety, generation, class), activity log
- primary actions: allocate to plan, record activities and monitoring visits, schedule/record inspections

### Mobile field and inspection capture

The in-field surface for officers and inspectors.

- observation forms, photos, GPS context, offline capture with later sync
- primary actions: record monitoring visit, capture inspection result, flag issues for correction

### Lot register with genealogy

The system's center of gravity once harvest starts.

- lot list and detail: variety, generation/class, lineage (parent lot, field), quantities, state, quality record, certification status
- primary actions: create lot at intake, record movements and processing, attach test results, change status, trace genealogy up and down the chain

### Quality / laboratory results

- test requests and reports of analysis (germination, purity, moisture, health) linked to lots
- primary actions: request test, enter results, set lot disposition

### Processing orders (conditioning plant)

- production orders for cleaning, drying, grading, treatment, blending; barcode/QR scanning at the line
- primary actions: create order from lot, record processing steps and outputs, keep identity through the line

### Inventory

- lots by location and state; allocation to orders; carryover view
- primary actions: move, allocate, re-test carryover, adjust

### Sales and distribution

- orders, pick/ship against lots, batch-level invoicing
- primary actions: allocate lot to order, ship, invoice

### Settlements and costing

- grower settlement runs (quantity × quality × terms), lot-level production cost
- primary actions: compute settlement, review deductions, post costs

## Important Rules / Behaviors

- **Identity is preserved through everything.** A lot's identity — variety, generation, lineage — must survive harvest, conditioning, blending, storage, and bagging. Records must account for every incoming quantity and final disposition; this is what makes recall and genealogy possible.
- **Quality results gate progression.** A lot does not move to packaging and sale on schedule alone; recorded test results (and, where applicable, certification status) decide. Held lots wait; failed lots are downgraded or rejected.
- **Siting constraints bind at planning time.** Isolation distances, previous-crop rules, and the class of the planted seed constrain which field may produce which class. A field planted with registered-class seed is produced and inspected as the next lower class — the class system flows through the plan, not around it.
- **Failed inspections have consequences.** A field that fails inspection must typically be corrected and re-inspected before harvest; an uncorrected failure removes the seed from its intended class. Failed fields usually cannot simply be withdrawn from the program.
- **Settlement follows the contract.** Grower payment is a computed outcome of delivered quantity, quality results, and contract terms — including deductions for sub-standard lots — not a flat price conversation.
- **Blending is rule-bound.** Lots of the same variety and class may commonly be blended with the class retained; blending across varieties or classes breaks identity and is constrained accordingly.
- **Carryover is a managed state.** Unsold lots persist between seasons as part of inventory and genealogy rather than disappearing at season end; products commonly provide a carryover view and re-testing support for carried lots.
- **Traceability is bidirectional.** From any bag or lot, the system can trace back to the field and parent seed, and forward to everything produced or sold from it.

## Variants

- **By certification regime** — markets with mandatory official certification (agency inspections, tags, bulk certificates) push certification paperwork into the product; markets or companies running internal QA keep the same gates but with company-owned class schemes
- **By species** — self-pollinating field crops, hybrids (with pollination management), vegetable seed (often smaller lots, nursery-raised transplants, biennial cycles such as seed-to-bulb-to-seed), fodder and floral species
- **By production model** — contract multiplication through grower networks (the dominant pattern) versus vertically integrated production on company-owned farms; the lot spine is identical, the contract layer thins
- **By platform packaging** — dedicated seed-production suites; seed verticals built on horizontal ERP platforms; agri-intelligence platforms strong on field monitoring that pair with an external ERP for the industrial and financial layers
- **By scope** — production-only deployments (connected to a separate ERP for sales/finance) versus full-chain deployments that also carry sales, distribution, and grower payments
- **Adjacent bundles** — breeding and trialing modules, royalty/trait-fee management for traited varieties, organic-program charters, consumer-facing authenticity QR codes

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Farm Management Platform / Crop Management | adjacent, shares the field layer | manages a farm's crop for food/feed harvest; no varietal identity, no generation/class, no lot genealogy or quality gate to release |
| Contract Farming (within agribusiness ERPs) | overlapping machinery | grower contracts exist in both; in seed production the contract anchors variety multiplication with parent-seed provision, and outcomes roll into identified lots, not anonymous commodity deliveries |
| Food Traceability Platform | shares "lot traceability" vocabulary | its lot is a food-safety record (origin, handling); the seed lot carries varietal identity, generation, and certification status, and the purpose is genetic purity, not food safety |
| Grain Management / Grain Origination | commodity neighbor | grain quality is grade factors; no variety-identity requirement, no class system, no isolation constraints |
| Government Inspection Management (certification-agency systems) | external authority counterpart | the agency inspects and certifies and keeps its own records (applications, inspection reports, certificates, tags); this application manages production and consumes those outcomes as gates |
| Nursery Management | propagation neighbor | manages plant propagation batches in greenhouses; seed production manages field-multiplicated lots under a class system (vegetable seed blurs at specialized nurseries, but the lot spine stays decisive) |
| Breeding management software | upstream neighbor | breeding creates varieties; seed production multiplies them; some platforms bundle both, but the multiplication side is this Type |
| Inventory Management System / WMS | capability overlap | lot inventory exists here with variety/class/lineage semantics and the field-production upstream; a bare inventory system has neither |

The most consequential boundary is against **crop/contract farming**: the same growers, fields, and contracts appear in both. What makes this a distinct Type is the lot — a unit of record that carries varietal identity and generation, is gated on identity-preserving quality evidence, and chains across seasons.

## Representative Products

- **Agreo Seeds** (SMAG) — dedicated seed-production business suite covering planning, contracting, technical monitoring, processing, laboratory, and batch-level sales; used by breeders, multipliers, and cooperatives in Europe
- **ERP for Seed** (Unify Dots, built on Microsoft Dynamics 365) — seed-specific verticalization of a horizontal ERP: grower contracts, production and processing, batch genealogy, quality-linked inventory
- **FarmERP — Seed Production & Traceability** (Shivrai Technologies) — seed vertical of a multi-vertical agribusiness ERP platform with mobile offline field capture
- **Cropin Cloud for seed production** (Cropin) — agri-intelligence platform for seed companies: multiplication planning, field monitoring, multi-generational traceability, paired with enterprise systems
- **Folio3 AgTech Seed Management** (Folio3) — build-to-order seed suite spanning grower contracts, lot tracking, conditioning, and distribution; also builds inspection apps for certification agencies

## Sources

Research date: **2026-09-10**

- SMAG — Agreo Seeds product page and launch announcement: https://smag.tech/en/our-software/seed-production-management-software , https://smag.tech/en/blog/smag-launches-agreo-seeds , http://smag.tech/en/blog/kws-chooses-agreo-seeds
- ERP for Seed (Unify Dots) — module pages: https://erpforseed.com/ , https://erpforseed.com/grower-contracts/ , https://erpforseed.com/seed-production-processing/
- FarmERP — solution suite: https://digital.farmerp.com/ , https://www.farmerp.com/
- Cropin — seed production solution and case study: https://www.cropin.com/seed-production , https://www.cropin.com/wp-content/uploads/2025/07/Seed-Producer-Global-agri-operations-transformation-on-Cropin-Cloud.pdf
- Folio3 AgTech — Seed Management Software: https://agtech.folio3.com/seed-management-software
- North Dakota State Seed Department — Certified Seed Grower's Manual and certification pages: https://www.seed.nd.gov/field-seed/seed-certification , http://seed.nd.gov/sites/www/files/documents/CertifiedSeedGrowersManualFinal.pdf
- eCFR — 7 CFR Part 201 (Certified Seed): https://www.ecfr.gov/current/title-7/subtitle-B/chapter-I/subchapter-K/part-201
- SATHI seed traceability portal (India): https://issca.icrisat.org/scalable-solutions/seed-traceability-authentication-and-holistic-inventory-sathi-portal
- SD Crop Improvement / CSGA Seed Tracking System manual: https://agsci.colostate.edu/seeds/wp-content/uploads/sites/145/2025/12/NEW-CO-Seed-Tracking-System-Instruction-Manual-CSGA.pdf
- eOrganic — Seed Production Contracting guidelines: https://eorganic.org/node/381

> Sourcing limitation: the Folio3 product page could not be fetched directly (HTTP 403) on the research date; its observations rest on search-index excerpts of the official page and are treated as lower-strength evidence. Precise numeric limits, prices, default settings, and jurisdiction-specific class names are intentionally not stated in this document; exact certification-class vocabulary varies by scheme and jurisdiction.
