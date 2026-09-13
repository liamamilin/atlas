# Demand-side Platform / DSP

## Overview

A **Demand-side Platform (DSP)** is the advertiser's side of the automated digital-advertising marketplace. It is the platform an advertiser or agency uses to buy advertising automatically across many external sellers: the platform holds the advertiser's demand configuration — budgets, targeting, bids, and creatives — evaluates every available ad opportunity against it in real time through its own bid engine, wins impressions in automated auctions and deals, and reports spend and delivery back to the buyer.

The defining core is small:

```text
Advertiser or agency (buyer) the platform acts for
└── External supply reached automatically (exchanges, SSPs, networks, publishers)
    └── Buyer-configured demand: budgets, targeting, bids, creatives
        └── Evaluated per impression by the platform's own bid engine
            └── Spend, delivery, and conversions recorded back to the buyer
```

Everything else commonly associated with DSPs — audience data marketplaces, private marketplaces and guaranteed deals, AI-driven optimization, CTV and audio formats, identity frameworks, forecasting tools — is standard capability in mature products, not what makes a product a DSP. The first generation of demand-side platforms bought display impressions through exchanges with no streaming machinery, identity frameworks, or AI decisioning, and they were recognizably the same kind of product.

When the customer flips to the media owner's side (inventory, floors, revenue), the product is a Supply-side Platform. When the buying happens inside one named platform's console over that platform's own inventory, it is Advertising Campaign Management. When the product's world expands to the whole buying operation — cross-channel media plans, committed vendor orders, vendor-bill reconciliation — it is a Media Buying Platform, which may embed a DSP as one module.

## Users & Context

The primary user is the **advertising buyer** — the party spending media budgets on behalf of an advertiser:

- **Agency teams and trading desks** buying for a roster of advertiser clients; the platform's advertiser objects map naturally to clients and brands
- **In-house programmatic teams** at brands buying directly
- **Self-serve marketers** operating the console without intermediaries

Typical roles around the platform:

- **Programmatic traders / media buyers** build and manage the demand configuration — line items, targeting, bids, budgets — and monitor delivery and performance throughout the flight. This is the platform's center of gravity.
- **Ad-operations staff** handle creatives: uploading, auditing, trafficking tags, and troubleshooting ads that fail to serve.
- **Analytics / account managers** consume delivery, spend, and conversion reporting and translate it into optimization and client communication.
- **Finance** reconciles spend against the platform's consolidated billing.

The DSP is infrastructure that runs continuously in the background of the open internet: its users configure it and steer it, while the buying loop itself executes automatically at machine speed, impression by impression.

## Core Model

### The advertiser relationship of record

The platform's world is anchored on the **advertiser**: a registered object representing the client or brand whose advertising is being bought. An agency account holds many advertisers; each advertiser carries the defaults that govern everything bought under it (currency, time zone, the brand and category applied to its ads). Where the platform is sold to an advertiser directly, the advertiser object is the buyer's own organization.

The advertiser relationship is what gives the platform its side. The DSP never owns or resells the inventory; it buys on the advertiser's behalf, from sellers it does not represent.

### External supply, reached automatically

On the other side stands **external supply**: the exchanges, supply-side platforms, ad networks, and directly connected publishers whose ad opportunities the platform can buy. The platform maintains connections to many supply sources at once; a buyer does not sign contracts with each publisher or exchange, because the platform's existing marketplace connections are the access route. Supply reaches the buyer as structured, targetable inventory, with products surfacing inventory information at varying depth — from browsable site and app detail with volume and price estimates to category classifications and quality flags.

### The demand configuration

Between the advertiser and the supply sits the buyer's standing configuration, held as a hierarchy of objects:

- **The financial agreement** (commonly called an insertion order) — the total budget an advertiser allocates for a period, often with verification requirements; it groups the buying strategies beneath it.
- **Line items** — the individually managed buying strategies: how much budget goes to which offering, over which dates, against which targeting, at what bid. A line item is the unit that actually bids.
- **Targeting** — the conditions an impression must meet: audience segments, geography, device, site and app lists (allowed or blocked), content categories, context.
- **Creatives** — the actual ads, hosted by the platform or by third-party ad servers, attached to line items and subject to the platform's creative auditing.
- **Audience data** — segments built from pixels placed on the advertiser's own properties, first-party data files, and third-party data providers; segments are the retargeting and reach engine of the configuration.
- **Measurement objects** — conversion pixels and trackers that record what the bought impressions caused, tied back to specific line items.

The hierarchy is both an organizational device and a money device: budgets set at higher levels constrain what the line items beneath them can spend.

### The bid engine

The platform operates its **own bid engine** — a decisioning system that receives each ad opportunity, overlays whatever user and inventory data it holds, evaluates the opportunity against every eligible line item, computes a bid, and responds within the marketplace's real-time window. The engine is the platform's proprietary machinery: it is what turns a configured campaign into thousands of buying decisions per second, and it is why a DSP is infrastructure rather than an ordering form.

### The outcome record

Every transaction is logged — what was bought, at what price, from which seller — and aggregated into the buyer's reporting: spend, impressions, clicks, video completion, viewability, and conversions attributed back to the buying configuration. This record feeds in-flight optimization (shifting budget, adjusting bids and targeting) and settlement: depending on the product's commercial model, the platform either purchases media through its own marketplace seats and bills the buyer a single consolidated amount, or routes billing through the exchanges when the buyer uses its own seats.

### Standard capabilities around the core

Mature DSPs commonly add:

- **Deal machinery from the buyer side** — private marketplaces (invitation-only auctions), preferred/fixed-price deals, and programmatic guaranteed commitments with specific sellers, accessed through interoperable deal identifiers
- **Optimization machinery** — bidding algorithms, automatic pacing toward delivery goals, traffic splits that distribute a line item's budget across tactics, and AI-driven decisioning that reweights bids in real time
- **Omnichannel coverage** — display, online video, mobile in-app, native, audio, digital out-of-home, and streaming TV bought through the same configuration
- **Inventory quality and brand safety** — fraud protection, inventory audits, sensitive-category classifications, block lists
- **Forecasting and planning** — estimates of available impressions, reach, and price before money is committed
- **Measurement depth** — viewability methodology, brand-lift studies, cross-channel attribution, log-level data exports
- **APIs** — management and reporting parity with the console, plus event-level data feeds
- **Service postures** — self-serve operation, managed-service teams, or sales-led onboarding

## How It Works

### Connect the advertiser and install measurement

```text
Advertiser (or agency client) is registered
→ defaults set (currency, time zone, brand/category)
→ segment pixels placed on the advertiser's properties (audience building)
→ conversion pixels placed (outcome measurement)
→ first-party data files / third-party segments connected where used
```

### Configure the demand

```text
Create the financial agreement (budget for the period)
→ create line items beneath it (budget, dates, offering)
→ set targeting per line item (audience, geography, inventory lists, context)
→ set bidding strategy and price
→ upload and audit creatives, attach them to line items
→ optionally configure splits that distribute the budget across tactics
```

Changes take effect quickly — products document configuration changes becoming live within minutes — which is what makes the configuration a steering wheel rather than a setup form.

### The per-impression loop (continuous, automatic)

```text
Ad opportunity occurs on some seller's property
→ the platform receives the opportunity through its supply connections
→ user and inventory data are overlaid
→ the platform's bid engine evaluates eligible line items
→ a bid (price + creative) is returned within the marketplace window
→ the marketplace applies the seller's rules and picks the winner
→ won impressions are served or handed back to the seller to serve
→ the transaction is logged against the line item
```

The same machinery carries pre-agreed deals: a fixed-price or guaranteed deal makes the buyer's participation automatic on the deal's impressions, flowing through the same bid loop at the agreed terms rather than by manual trafficking.

### Operate and optimize

```text
Monitor spend, delivery, pacing, and conversions
→ compare tactics via splits and reporting dimensions
→ adjust bids, targeting, budgets, and creatives in flight
→ create or refresh deals with specific sellers
→ troubleshoot delivery (inventory, creative, price)
```

### Settle

Spend accrues against the buyer's account as media is bought. Settlement follows the product's commercial model: commonly the platform purchases media through its own marketplace seats and the buyer receives one consolidated bill, while buyers with their own exchange seats can route the media bill directly through the exchanges where the product supports it.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Advertiser / campaign setup

The structural backbone. Lists advertisers (clients or brands) and the buying hierarchy beneath them; primary actions: register advertisers, create financial agreements, create and clone line items, set defaults.

### Line item editor

Where buying strategy lives. Carries budget, flight dates, bidding strategy and price, and the full targeting set (audience segments, geography, device, inventory allow/block lists, categories); primary actions: create/edit, activate, pause, duplicate.

### Audience / segment management

The data surface. Lists pixel-built segments, first-party data uploads, and third-party segments with sizes; primary actions: create pixels, upload data, compose and combine segments, assign them to targeting.

### Inventory / supply discovery

Where supply becomes targetable: browsable inventory information (site and app detail, volume and price estimates where surfaced, category and sensitivity classifications, quality filters); primary actions: build allow/block lists, scope line items to inventory.

### Deal management

Where pre-negotiated commerce lives from the buyer's side: deals with specific sellers, their terms and statuses; primary actions: find/accept marketplace deals, create deals with partners, monitor deal delivery.

### Creative library

The ad surface: uploaded or third-party-hosted creatives with formats, audit status, and trackers; primary actions: upload (individually or in bulk), attach to line items, review audit results, troubleshoot.

### Reporting and optimization

The buyer's cockpit: spend, impressions, clicks, video and viewability metrics, conversions attributed to the configuration, broken down by line item, tactic, seller, geography, and format; primary actions: build reports, watch pacing, shift budget, adjust bids.

### Planning / forecasting

Where offered, forward estimates of available inventory, reach, and price for a planned configuration — used before committing money rather than after.

## Important Rules / Behaviors

- **Budgets are commitments that constrain bidding.** The financial agreement and line-item budgets bound what the bid engine can spend; pacing machinery paces delivery toward those budgets over the flight.
- **The buyer's rules are preferences; the seller's rules still bind.** A bid is an offer: the marketplace applies the seller's floors, access rules, and deal terms, and the win decision combines the bid amount with publisher preferences. Winning is not guaranteed by configuration alone.
- **Deal terms reshape the open market rather than replacing it.** A fixed-price deal wins at the agreed price; a guaranteed commitment obliges the buyer's line items to participate on the deal's impressions automatically — the pre-agreed terms still travel through the per-impression machinery, not around it.
- **Audience reach depends on the data layer.** Targeting segments only match impressions where the platform's data (pixels, files, providers, identity signals) recognizes the user; the buyer's chosen identity regime materially changes reachable scale.
- **Attribution is platform-side feedback, not neutral accounting.** Conversion pixels attribute outcomes to the platform's own impressions and clicks; the record optimizes buying and should be read as the platform's view of causality.
- **Creatives must pass review.** Ads are audited against platform and marketplace policies before they can serve; a rejected creative stops its line item from delivering with that ad.
- **Quality gates run on supply.** Fraud protection and inventory-quality screening sit between the marketplace and the buyer's budget; bad inventory is filtered before it can win.
- **Spend is real money on machine decisions.** The loop executes per impression at machine speed; reporting latency is short but nonzero, so steering is continuous rather than instantaneous.

## Variants

Common shapes of the same Type:

- **Independent buy-side DSPs** — buy-side-only platforms whose business is buying on the open internet; independence from owned media is often part of their positioning
- **Full-stack suite DSPs** — buying platforms sold inside suites that also contain sell-side and ad-serving products; the DSP's core is unchanged, but money and measurement can flow across the suite's own stack
- **Platform-affiliated DSPs** — buying platforms operated by companies with large owned inventory pools, which buy both inside and outside that inventory (market context; the affiliated part was not directly researched in this pass)
- **Self-serve vs managed-service** — consoles marketers operate directly vs platforms whose teams run the buying for the client
- **Agency-centric vs brand-direct** — hierarchies built around many advertiser clients vs single-brand in-house operation
- **Channel-emphasis variants** — CTV-first, audio-inclusive, retail-data-driven buying; some products extend into adjacent owned channels such as email or direct mail as part of one buying workflow
- **Segment packaging** — B2B/account-based buying emphasis, political, regulated-industry configurations
- **Regional and identity regimes** — the same core realized under different identity, privacy, and marketplace structures by geography

A variant remains a variant while the buying-side core holds. If the platform's primary object becomes the seller's inventory (→ SSP), one named platform's own campaigns (→ Advertising Campaign Management), or the whole cross-channel buying operation with plans and vendor-bill reconciliation (→ Media Buying Platform), it has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Supply-side Platform / SSP | mirror pole | The DSP's customer is the advertiser/agency; its objects are budgets, targeting, bids, creatives; its job is winning impressions. The SSP's customer is the media owner; its objects are inventory, floors, deals; its job is selling them. The two meet in the same per-impression marketplace. |
| Ad Server | adjacent, frequently bundled | The ad server's unit of work is selecting ads from a managed pool on known placements (priorities, forecasting); the DSP's unit of work is the bid on external opportunities across many sellers, with no placement registry of its own. Suites contain both. |
| Programmatic Advertising Platform | category vs pole | "Programmatic advertising platform" is the market-category name for the two-sided automated impression-trading layer; the DSP is its buy-side instantiation and the SSP its sell-side instantiation. |
| Media Buying Platform | layered (may contain a DSP) | Media buying holds the whole operation — cross-channel plans, committed orders, vendor-bill reconciliation — and may embed a DSP as its programmatic activation module; a DSP holds none of the plan/order/reconciliation structures. |
| Advertising Campaign Management | gradient | Campaign management governs campaign configuration, spend, and performance on named publisher platforms; the DSP transacts impressions on open external marketplaces under its own bid engine. The gradient is real — DSPs expose campaign-shaped objects, and some campaign tools operate DSP consoles — but the open-marketplace act is the DSP's center. |
| Data Management Platform / DMP | attached layer | DMPs and identity layers supply audience data; the DSP is the buying machinery they feed. A DSP's internal segment tooling is a capability, not the DMP Type. |
| Marketing Attribution Platform | feedback vs measurement of record | DSPs track conversions and attribute them to their own buys as optimization feedback; attribution platforms assign cross-channel credit across the advertiser's whole media mix. |
| ABM Platform | primary-object seam | Account lists enter DSPs as targeting inputs; the DSP's transacted unit remains the anonymous impression, not the named-account relationship. |
| Creative Management Platform | production vs delivery | CMPs produce and package the creatives; the DSP hosts and traffics them and applies audience decisioning at buy time. |
| Ad network | historical neighbor, different Type | The ad network aggregates and resells inventory as a principal; the DSP buys per impression on behalf of identified advertisers under the buyer's configuration. |

## Representative Products

- **The Trade Desk** — largest independent buy-side-only DSP; self-serve positioning, omnichannel coverage, identity and retail-data partnerships
- **Microsoft Invest (Xandr)** — strategic buying platform inside Microsoft's Buying and Selling Platforms suite; documented object hierarchy (member → advertiser → insertion order → line item → creative), proprietary bidder, exchange-seat billing
- **StackAdapt** — self-serve independent DSP pole for agencies and brands; programmatic core with owned-channel extensions and AI decisioning
- **Basis (embedded DSP)** — a DSP operated inside a media-buying platform, illustrating the layering seam between the two Types

The Core Model was checked against the sell-side sibling (SSP) and the two-sided category research to avoid absorbing either pole into this definition.

## Sources

Research date: **2026-09-08**

- Microsoft Invest — About Microsoft Invest: https://learn.microsoft.com/en-us/xandr/invest/about-invest
- Microsoft Invest — Object Hierarchy: https://learn.microsoft.com/en-us/xandr/invest/object-hierarchy
- Microsoft Invest — Ad Buying with Microsoft Advertising: https://learn.microsoft.com/en-us/xandr/invest/ad-buying-with-xandr
- Microsoft Invest — Basic Buy-side Setup Procedures: https://learn.microsoft.com/en-us/xandr/invest/basic-buy-side-setup-procedures
- Microsoft Invest — Product Documentation landing (module map): https://learn.microsoft.com/en-us/xandr/invest/
- The Trade Desk — Our Demand Side Platform: https://www.thetradedesk.com/us/our-demand-side-platform
- StackAdapt — homepage and platform page: https://www.stackadapt.com/ , https://www.stackadapt.com/platform
- Corroborating sibling research: The Trade Desk glossary and Microsoft Monetize documentation (research/programmatic-advertising-platform.md, fetched 2026-09-06); Basis DSP seam FAQ (research/media-buying-platform.md, fetched 2026-09-08)

> Sourcing limitations: Google Display & Video 360 (support.google.com) and Amazon DSP (advertising.amazon.com) documentation could not be fetched from the research environment; platform-affiliated DSP claims are therefore kept at market-context level. The Trade Desk's operational Knowledge Portal is login-walled; its evidence is positioning- and glossary-level. StackAdapt evidence is positioning-level. Operational details such as fee models, pacing defaults, and delivery-control specifics are intentionally not stated beyond what the fetched pages document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
