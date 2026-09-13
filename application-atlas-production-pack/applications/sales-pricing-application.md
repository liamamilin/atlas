# Sales Pricing Application

## Overview

A **Sales Pricing Application** is the selling organization's price-governance system: it holds the organization's prices as governed records, runs the managed cycle through which those prices are set, changed, approved, and released, and connects them to the selling motion — so that what sellers and selling systems actually charge is governed from one place instead of drifting through spreadsheets and ad-hoc overrides.

The defining structure is small:

```text
Governed price records (what may be charged, per product under conditions)
└── The setting-and-release cycle (strategy/rules → computed changes → simulate → approve → publish)
    └── The selling seam (sellers and selling systems consume the prices; realized outcomes return as evidence)
```

Everything else the market associates with modern pricing software — optimization engines, guidance ladders at quote time, agreements, market-data feeds, AI — is widely expected but not what makes the product a pricing application. Paper price lists under a price committee, ERP-era price tables, and spreadsheet price books all satisfy the core.

## Users & Context

The primary operators are the **pricing function** of a B2B sales organization:

- **pricing manager**: owns pricing strategy and structure — how prices are built, segmented, and governed
- **pricing analyst**: runs the recurring work — cost changes, scenario comparisons, price updates, exception review
- **pricing administrator / implementation engineer**: maintains master data, rules, integrations, and permissions

Secondary users are **consumers** of the pricing system's output rather than its operators:

- **sellers and account managers**, who receive prices and guidance inside their CRM or quoting tools
- **sales leadership and finance**, who see realized-price and margin performance
- **downstream systems** (ERP, CRM, CPQ, e-commerce, dealer/order systems), which receive published prices

The typical context is a B2B organization with large catalogs, many customers and regions, negotiated or customer-specific selling, and frequent cost or market movement — manufacturers, distributors, chemicals, parts and aftermarket businesses. The pain the software exists for is scale: prices set once by hand age quickly, cost changes arrive continuously, and per-deal improvisation leaks margin.

## Core Model

### The Defining Core

**1. Governed price records.** The center of the application is the price record: a maintained value for what the organization may charge for an offering under explicit conditions. Conditions are the dimensions that differentiate prices for the same product — customer or customer segment, region or country, channel, currency, volume, and validity period. Records are commonly organized in layers that the industry calls the **price waterfall**: a list or base price per product, from which regional, country, and customer-specific prices are derived, down to the guidance a seller may use on an individual deal. The application, not a spreadsheet or a quote, is the source of truth for this population.

**2. The setting-and-release cycle.** Prices are produced and updated by a managed cycle rather than by silent edits:

- **strategy and logic** — the organization's pricing approach (cost-plus, market/competitor-based, or value-based) encoded as rules, formulas, markups, indexes, corridors, and segments
- **computation** — price changes calculated or recommended across the catalog when costs, exchange rates, competitive data, or strategy move
- **simulation** — proposed changes tested for revenue and margin impact and compared against alternatives before anything goes live
- **approval and release** — changes routed to the right approvers, then published as the organization's sellable prices, commonly with effective dates and retained change history

**3. The selling seam.** The records connect to real selling. Selling systems obtain their prices from the pricing application — by direct publication or integration — and sellers receive prices and guidance inside the tools where they quote. What customers are actually charged can therefore be traced back to a governed record, and realized deal outcomes flow back as evidence for the next setting cycle.

Remove the governed records and prices are just fields inside quotes and item masters. Remove the cycle and the application is a static price table. Remove the selling seam and it is analytics that never touches a transaction.

### Capabilities Mature Products Commonly Add

- **Quote-time guidance** — a ladder of discount or price boundaries (commonly named start/target/floor or floor/target/stretch, with rationale) delivered into CRM/CPQ at the moment a seller prices a deal, sometimes with a health indicator comparing the entered discount to the ladder. Names and mechanics vary by product.
- **Optimization engines** — statistical or AI-driven recommendation of prices by segment, using elasticity and transaction history, constrained by guardrails such as floors, ceilings, rounding, and change limits.
- **Customer agreements** — negotiated customer-specific price agreements held as records with their own lifecycle (such as under negotiation → published → revised, with the published version serving as the active price record), so contract prices are governed records too.
- **Cost-change response** — visibility into cost movements and their margin impact, with passthrough strategies that recompute affected prices.
- **Currency and geographic derivation** — fixed exchange-rate periods, country and region price formulas that update automatically when global prices or rates change.
- **Market and competitor data ingestion** — external price signals feeding strategy and simulation.
- **Realized-price analytics** — price realization against the governed record, margin bridge, price-volume-mix decomposition, discount and leakage analysis, price-change history.
- **Integration spine** — publication into ERP, CRM, CPQ, and e-commerce; ingestion of transactions, costs, and customer data; APIs for configuration and retrieval.
- **Segmentation and roles** — customers and products grouped into tiers that carry different strategies; operator roles for the pricing team versus read/consume roles for sellers.

### One Structure, Many Implementations

```text
Concept:  Governed price records
Realized as:  price lists, base/global prices with derived country-region-customer prices,
              price grids, negotiated customer agreements

Concept:  Setting-and-release logic
Realized as:  hand-maintained rule tables, template-and-scenario workbooks,
              formula engines, statistical/AI optimization runs

Concept:  Selling seam
Realized as:  published price files into ERP, APIs into CRM/CPQ, embedded guidance
              fields on quote lines, dealer-network price distribution
```

A reader who has only seen one implementation — say, an AI-guided cloud platform — should still recognize a rules-driven price-management deployment, or a parts-pricing system feeding a dealer network, as the same Type.

## How It Works

The canonical operating loop:

```text
1. Establish the foundation
   products, costs, customers, historical transactions, currencies imported and structured

2. Define pricing logic
   segments + strategy models + rules/formulas (markups, indexes, corridors, floors)

3. Compute candidate prices
   cost/market/customer inputs → calculated or optimized price changes across the catalog

4. Simulate and compare
   what-if scenarios tested for margin, revenue, and volume impact; alternatives compared

5. Review, approve, publish
   changes validated and approved; released with effective dates into selling systems;
   change history retained

6. Sell under governance
   sellers price deals from published prices and quote-time guidance;
   deviations below the governed floor escalate for approval

7. Monitor and analyze
   realized prices vs governed records; margin bridge; discount leakage;
   findings feed the next strategy adjustment
```

Two rhythms matter in practice. The **event-driven rhythm** responds to triggers — a supplier cost increase, a currency move, new competitive data — recomputing affected prices and pushing them through simulation and approval quickly. The **calendar rhythm** runs periodic price reviews (annual list-price updates, contract renewals), which is precisely the work the software replaces spreadsheet-and-email workflows for.

A deal-time example of the seam: a seller opens a quote in the CRM, and the quoting tool fetches the governed standard price for the product-customer combination plus a guidance ladder; the seller's discount is compared to the floor; within the ladder it passes, below it the request routes for approval. The price the customer finally pays is one governed record plus one governed deviation.

## Interfaces

Exact layouts vary by product; these are the surfaces the Type is organized around.

### Price record workbench

The maintenance surface for the price population.

- typical information: products × conditions grid with current prices, validity dates, derivation sources
- primary actions: edit, bulk update, import, derive regional/customer prices, schedule changes

### Strategy and rule configuration

Where pricing logic is encoded.

- typical information: segments, strategy models, formulas, markups/indexes/corridors, guardrail settings
- primary actions: define rules, adjust segmentation, set floors and constraints

### Scenario / simulation workspace

The pre-release test bench.

- typical information: side-by-side strategy alternatives with projected margin, revenue, and volume impact
- primary actions: create scenario, apply strategy, run simulation, compare results, select for release

### Approval queue and change history

The governance surface.

- typical information: pending price changes with rationale, requester, affected records; past changes with attribution
- primary actions: approve, reject, request changes, audit

### Publication and integration console

The bridge to selling systems.

- typical information: publication targets (ERP/CRM/CPQ/e-commerce), sync status, effective-dated releases
- primary actions: publish, schedule release, configure integrations, inspect errors

### Seller-facing guidance (usually embedded in CRM/CPQ)

Not a standalone screen of the pricing product but its most user-visible output.

- typical information: standard price, target and floor boundaries, rationale, health indicator
- primary actions: accept guidance, request deviation

### Analytics dashboards

The closing loop.

- typical information: price realization, margin bridge, price-volume-mix, discount distribution, leakage hotspots
- primary actions: drill down by product/customer/region, export, raise a pricing action

## Important Rules / Behaviors

- **Published prices are governed, not editable in place.** Once released, records typically change only through the cycle (new change, approval, effective-dated publication). Negotiated agreements behave the same way: a published agreement is an official price record; updates happen through a revision, not silent edits.
- **Effective dating separates decision from effect.** A price change can be approved today and take effect at a defined date, so increases and renewals land on time without breaking in-flight quotes.
- **Guidance constrains, floors gate.** Quote-time guidance is advisory above the floor; prices below the governed floor are the exception path and route for approval. This is the daily enforcement surface of the whole system.
- **The pricing application designs; the ERP stores and executes.** Mature deployments publish approved prices into ERP and selling systems rather than treating the ERP price field as the design surface — the recurring boundary statement of the category.
- **Simulation precedes publication.** Margin and revenue impact is inspected before prices go live; bulk price changes across large catalogs are the norm and are too consequential to release untested.
- **Attribution is structural.** Price changes carry requester, approver, and effective date with retained history, because pricing decisions move real money and must be defensible.
- **Realization is compared against the record.** The governed price is the benchmark against which actual deal prices, discount behavior, and margin outcomes are measured; drift and creep are surfaced as findings, not discovered at month-end.

## Variants

- **Guidance-led vs platform-led vs margin-led** — products differ in center of gravity: some lead with sales-facing recommendations inside CRM; others with the full price-lifecycle platform; others with margin/profit analytics depth. The underlying structure is shared.
- **Industry tuning** — distribution (thousands of SKUs × customers), manufacturing and chemicals (cost volatility, passthrough), aftermarket parts (kit-based, lifecycle, and supersession pricing; harmonization against grey-market and cannibalization risk; dealer-margin economics), high-tech (channel and agreement complexity).
- **Suite posture** — standalone pricing deployments are common; larger suites attach quoting, rebates, promotions, and channel management to the same price core.
- **Optimization maturity** — deployments range from hand-maintained rule tables through template-driven scenario workbooks to statistical/AI optimization with guardrails. All are the same Type; optimization depth is maturity, not membership.
- **Customer tier** — mid-market editions with lighter machinery vs enterprise platforms with high data volumes and multi-region governance.
- **Delivery** — cloud SaaS dominates the current market; ERP-adjacent and integrated-suite deployments persist.

## Related Application Types

| Type | Distinction |
|---|---|
| Configure Price Quote / CPQ | CPQ configures an offer and produces the quote record, computing prices at quote time inside an embedded engine; it **consumes** governed prices. This Type owns the standing price population and the discipline that produces and releases it. Publication into CPQ is the designed seam. |
| Deal Desk / Commercial Approval Platform | Deal Desk runs the cross-functional approval process over commercial commitments and exceptions; approval here attaches to price changes and deviations, not whole deals. |
| Retail Pricing Management (§05.14 family) | Retail-side pricing manages shopper-facing price files, promotions, and markdowns for stores and e-commerce. Same subject matter, different operator, objects, and flows: the sales organization's governed prices vs the retailer's shelf/offer prices. |
| ERP price master | ERP stores price condition data and executes it in sales documents; this Type is where prices are designed, simulated, governed, and published from. ERP-native pricing modules are a deployment pole, not a different Type. |
| Billing / Subscription Billing | Billing invoices what was sold; this Type determines what may be charged. Upstream one-way handoff. |
| Sales Forecasting / Revenue Intelligence | Those project sales outcomes; this Type governs the prices those outcomes realize. Realized-price analytics here closes the pricing loop, it is not a forecast center. |
| Financial Modeling / FP&A | Elasticity and optimization models here are operational inputs to released prices, not planning artifacts; no budget or plan objects. |
| Airline/Hotel-style Revenue Management | Yield optimization over perishable inventory vs price governance over a product/customer catalog. Structurally different Types that can share a vendor family. |

## Representative Products

- Zilliant
- Pricefx
- Vendavo
- Syncron

The market category is generally labeled **price optimization and management** (analyst names observed on vendor pages: IDC "B2B price optimization and management applications", Gartner "B2B Pricing and Rebate Optimization Software", QKS "B2B Price Optimization & Management"). The Core Model was checked against the aftermarket/parts pole (Syncron) and against ERP-native and spreadsheet-era price management to avoid over-fitting to the modern AI-platform shape.

## Sources

Research date: **2026-09-07**

- Zilliant — product site and product documentation: https://www.zilliant.com/ , https://docs.zilliant.com/ (About Price Manager; About Pricing Engine; About Price IQ; Price Manager use cases; About agreements; Enable pricing guidance and data in quotes and agreements)
- Pricefx — product site, price-management capability page, and knowledge base: https://www.pricefx.com/ , https://www.pricefx.com/platform/price-management/ , https://knowledge.pricefx.com/
- Vendavo — product site and platform/pricing page: https://www.vendavo.com/ , https://www.vendavo.com/platform/pricing/
- Syncron — product site and service-parts pricing page: https://www.syncron.com/ , https://www.syncron.com/solutions/parts-pricing
- PROS — homepage banner only ("PROS B2B is now Conga!"); the B2B pricing product surfaces were unreachable (403), so no product-internal claims were drawn from that line.

> Sourcing limitation: operational Tier-1 depth (object models, workflow states, numeric parameters) was directly observed only for Zilliant; Pricefx was observed via its knowledge base and capability pages; Vendavo and Syncron via official product pages. The document therefore keeps operational specifics qualitative and asserts no numeric limits, defaults, or workflow state names. Detailed observations are in the paired Research Notes.
