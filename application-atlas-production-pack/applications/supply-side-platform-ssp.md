# Supply-side Platform / SSP

## Overview

A **Supply-side Platform (SSP)** is the media owner's side of the automated digital-advertising marketplace. It is the platform a publisher, app developer, or streaming service uses to sell its advertising inventory automatically to external demand: the platform registers the seller and their inventory, exposes each ad opportunity to demand sources in real time, enforces the seller's pricing and access rules on every impression, and reports the resulting revenue back to the seller.

The defining core is small:

```text
Media owner (seller) and their registered inventory
└── Automated exposure of each ad opportunity to external demand
    └── Seller-controlled monetization rules (floors, demand access, deal terms)
        └── Winner selected under those rules
            └── Revenue recorded and reported back to the seller
```

Everything else commonly associated with SSPs — multi-demand mediation, header bidding, private marketplaces, programmatic guaranteed deals, identity layers, CTV machinery — is standard capability in mature products, not what makes a product an SSP. The first generation of sell-side platforms exposed publisher inventory to multiple demand sources with publisher-set floors and no header bidding, identity graphs, or streaming machinery, and they were recognizably the same kind of product.

When the customer flips to the advertiser's side (campaigns, budgets, bids), the product is a Demand-side Platform. When the platform takes ownership of inventory and resells it under its own terms, it is an ad network — a different, older kind of business.

## Users & Context

The primary user is the **media owner** — the party that owns or legitimately represents sellable advertising inventory:

- **Publishers** monetizing websites (display, online video, native)
- **App developers** monetizing mobile applications (banners, interstitials, video, native)
- **Streaming services and CTV/OTT content owners** monetizing ad breaks in streams
- **Resellers** — parties that monetize inventory sourced from third-party partners rather than owned outright (products explicitly support declaring inventory as direct vs indirect)

Typical roles around the platform:

- **Yield / monetization managers** configure floors, demand partners, and deals; watch fill rates and revenue; adjust pricing in response to market signals. This is the platform's center of gravity.
- **Ad-operations staff** set up and maintain inventory (sites, apps, ad units), integrations, and troubleshooting.
- **Sales / partnerships staff** negotiate deals with buyers and manage marketplace relationships; some platforms provide dedicated demand-facilitation teams as part of the service.
- **Executives** consume revenue reporting.

The SSP is infrastructure that runs continuously in the background of every page view, app session, and stream: its "users" configure it and monitor it, while the transaction loop itself executes automatically at machine speed.

## Core Model

### The seller relationship of record

The platform's world is anchored on the **media owner**: a registered account representing the party whose inventory is being sold. Under the seller sit structured inventory objects — the sites, apps, properties, and placements offered for sale. Mature products organize this as a hierarchy (account → publisher → property/brand → supply → ad units; exact levels and names vary by product), where each **ad unit** identifies a place where an ad can be displayed, and each node carries the settings that govern it. Inventory may be **direct** (owned by the account holder) or **indirect** (sourced from a third-party partner) — resold inventory is a supported, declared case.

The seller relationship is what gives the platform its side. The SSP never takes ownership of the inventory; it represents it.

### Demand sources

On the other side stands **external demand**: the DSPs, exchanges, ad networks, agencies, and direct buyers that compete for the seller's impressions. The SSP maintains connections to many demand sources and exposes inventory to them through standardized, automated interfaces. Demand sources are themselves managed objects: they can be enabled, prioritized, restricted, or blocked per inventory.

### The seller's monetization rules

Three families of rules, all set by (or on behalf of) the seller and enforced by the platform on every impression:

- **Price floors** — the minimum price the seller will accept for an impression (expressed as a CPM). Floors attach to inventory-hierarchy nodes and are inherited by the units beneath them. Floor-setting is the seller's most fundamental control: it converts "sell everything to whoever bids" into "sell at no less than this."
- **Demand access control** — which demand may participate at all: blocked or allowed buyer seats, blocked advertiser domains and categories, creative review (approving or rejecting specific ads), and general ad-quality standards. Blocked attributes are communicated to buyers in the request itself, and the platform enforces them on responses.
- **Deal terms** — pre-negotiated agreements with specific buyers that change the conditions of the transaction: private access to specific inventory, agreed fixed prices, or committed volume. Deals are first-class objects with their own lifecycle (active, paused, expired).

### The transaction loop

For every ad opportunity, the platform runs an automated request-and-bid cycle: it describes the opportunity (placement, format, content context, consent state, identity signals where available) and sends it to the eligible demand sources; demand sources respond with bids (price plus the ad to serve); the platform applies the seller's rules — floors, access restrictions, deal terms — and selects the winner; the winning ad is returned to the placement. The whole cycle completes in real time, while the ad opportunity is pending. Even pre-agreed deals flow through this machinery: a fixed-price deal makes bids at or above the agreed price eligible, and the winner pays the agreed price rather than their bid.

### The revenue record

Every won impression is logged — what filled, at what price, from which buyer — and aggregated into the seller's revenue reporting: requests, fills, fill rate, impressions, and revenue (commonly split into gross figures before the platform's share and net figures after). This record is the basis for payment and for the seller's yield management. Some products provide transaction-level "receipts" (impression-level audit logs) as a transparency feature.

### Standard capabilities around the core

Mature SSPs commonly add:

- **Multi-demand mediation** — exposing each opportunity to many demand sources at once (or in configured sequences) to maximize competition; supply-path optimization tooling
- **Deal machinery depth** — open exchange access, private marketplaces (invitation-only auctions), preferred/fixed-price deals, programmatic guaranteed (committed budget from the buyer, committed delivery from the seller), auction packages and curated marketplaces that package inventory for strategic buyers
- **Yield optimization** — floor recommendations from marketplace signals, traffic shaping, throttling of low-quality or oversaturated demand
- **Ad quality and fraud controls** — creative inspection, blocked categories/domains, fraud detection on both supply and demand sides
- **Omnichannel format coverage** — display, online video, mobile in-app, native, audio, digital out-of-home, and streaming TV (with streaming-specific machinery such as ad-break construction, competitive separation, and server-side ad insertion)
- **Identity and data layers** — connecting inventory and publisher data to identity frameworks and data platforms, with ID-less fallbacks
- **Transparency standards** — participation in industry supply-chain transparency mechanisms (sellers.json, ads.txt / app-ads.txt), consent and privacy-regime signaling
- **Reporting and APIs** — seller-facing analytics down to impression level, plus management APIs

## How It Works

### Connect the inventory

```text
Media owner signs up / is onboarded
→ inventory is registered (sites, apps, ad units, streams)
→ integration is chosen:
     - tags or SDKs placed in the property (no ad server of their own), or
     - OpenRTB connection from the publisher's own ad server or reseller setup
→ formats and settings configured per inventory node
```

Media owners without their own ad-serving technology integrate directly via tags or SDKs; those with in-house ad servers (or resellers) connect over standardized programmatic interfaces so the SSP sits behind their existing serving stack.

### Configure monetization

```text
Set floors on inventory nodes (inherited downward)
→ choose which demand sources may access which inventory
→ set ad-quality rules (blocked domains/categories, creative review)
→ negotiate and create deals with specific buyers
     (private marketplace, fixed price, programmatic guaranteed, packages)
```

### The per-opportunity loop (continuous, automatic)

```text
Ad opportunity occurs (page view / app screen / stream ad break)
→ platform describes the opportunity and calls eligible demand
→ demand sources bid
→ platform applies seller rules (floor, access, deal terms)
→ winner selected; ad returned to the placement
→ transaction logged (fill, price, buyer)
```

### Operate and optimize

```text
Monitor fill rate, revenue, buyer mix, quality
→ adjust floors (often guided by marketplace-signal recommendations)
→ shape or block underperforming demand
→ create/refresh deals and packages for premium inventory
→ resolve delivery issues with bid-level diagnostics
```

### Get paid

Revenue accrues to the seller's account per the agreed economics (typically a revenue share or take rate on transacted value); the platform's reporting is the shared basis for settlement.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Inventory management

The structural backbone. Lists the hierarchy of properties and ad units with their settings; primary actions: add/edit inventory nodes, configure formats, set or inherit floors, declare direct vs indirect sourcing, toggle inventory on/off.

### Deal management

Where pre-negotiated commerce lives. Lists deals with type, buyer, price terms, targeting, status (active/paused/expired); primary actions: create a deal (private marketplace, fixed-price, programmatic guaranteed, package), edit terms, pause/expire, troubleshoot delivery.

### Pricing / floor controls

Floor configuration per inventory node with inheritance visibility (which node a floor is inherited from), plus simulation or recommendation surfaces that estimate revenue at different floor settings.

### Demand partner management

The roster of connected demand sources with per-partner controls: enable/disable, seat-level blocking, transparency settings (what identity or data signals are shared with which partners).

### Ad quality controls

Blocked advertiser domains and category lists, creative review queues (approve/reject), and quality-policy configuration; enforcement is visible in reporting as rejected or blocked transactions.

### Reporting and analytics

The seller's revenue cockpit: requests, fills, fill rate, impressions, revenue (gross/net), broken down by inventory node, demand source, buyer, geography, and format; impression-level audit detail in transparency-focused products.

### Diagnostics

Where offered, bid-level troubleshooting tools that show, for a specific opportunity, what was requested and what came back — used to answer "why is this inventory not filling?" or "why did this buyer stop bidding?"

## Important Rules / Behaviors

- **The floor is a promise to the seller.** An impression is not sold below the applicable floor; the platform enforces this on every transaction, and floors inherit down the inventory hierarchy unless overridden.
- **Deal terms reshape the open market rather than replacing it.** A fixed-price deal makes bids at or above the agreed price eligible and the winner pays the agreed price; a private marketplace restricts an auction to invited buyers; a programmatic guaranteed deal carries mutual commitments — the buyer commits budget, the seller commits delivery of a specified number of impressions.
- **Seller access rules bind the platform.** Blocked buyer seats, advertiser domains, and categories are both communicated to buyers (so they don't waste bids) and enforced on responses; creative that fails review does not run.
- **Guaranteed delivery creates obligations on the seller's side.** Where a deal commits delivery, the platform tracks pacing toward the committed volume — the seller's side of the bargain is machine-managed too.
- **Identity and transparency are declared, not implied.** The platform's role in the supply chain is published through industry transparency mechanisms; resold or indirect inventory must be declared as such.
- **Quality gates run in both directions.** Demand is screened for fraud and quality before it can win, and supply is throttled or rejected when it endangers platform performance or quality (excessive request rates, poor-performing inventory).
- **Revenue is reported gross and net.** The seller sees both the transacted value and their payout after the platform's share; the difference is the commercial basis of the product.

## Variants

Common shapes of the same Type:

- **Web-first SSPs** — tag/header integrations for browser inventory; often paired with a header-bidding wrapper product that mediates demand sources ahead of the ad server
- **Mobile-first SSPs** — SDK-based integration for app developers; enrichment of ad requests with behavioral/contextual signals is a common emphasis
- **Streaming/CTV-first SSPs** — ad-break construction, competitive separation, server-side insertion, and live-stream handling for video-first media owners
- **Pure-play vs suite** — independent sell-side specialists vs sell-side product lines inside broader platforms (which may bundle ad serving, buying tools, or both)
- **With buyer-side products** — some SSP vendors also sell deal-management consoles to buyers, making the same marketplace accessible from both ends
- **Curation and marketplace extensions** — packaged, curated inventory offerings (sometimes with data vendors or commerce/retail-media partners) sold on top of the core exchange
- **Self-serve vs managed** — consoles the seller operates directly vs service-heavy models with platform-run yield teams and demand facilitation
- **Reseller-oriented configurations** — platforms that accept standardized programmatic connections from publisher-side ad servers and resellers, treating them as first-class sellers

A variant remains a variant while the seller-side core holds. If the platform's primary object becomes the buyer's campaign (→ DSP) or owned inventory resold under the platform's own terms (→ ad network), it has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Demand-side Platform / DSP | mirror pole | DSP's customer is the advertiser/agency; its objects are campaigns, budgets, bids, targeting; its job is winning impressions. The SSP's customer is the media owner; its objects are inventory, floors, deals; its job is selling them. |
| Ad Server | adjacent, frequently bundled | The ad server's unit of work is selecting ads from a managed pool on known placements (priorities, forecasting); the SSP's unit of work is transacting inventory with external demand. Products bundle both (an SSP that also serves, or an ad server that takes programmatic demand as backfill), but the seam holds. |
| Programmatic Advertising Platform | category vs pole | "Programmatic advertising platform" is the market-category name for the two-sided automated impression-trading layer; the SSP is its sell-side instantiation and the DSP its buy-side instantiation. |
| Ad Exchange | absorbed role | The exchange is the neutral auction venue; the SSP is the seller's agent. Current SSP products run their own auction machinery, so the venue survives as a role inside SSP platforms rather than as a separate product shape. |
| Ad network | historical neighbor, different Type | The ad network takes ownership of (or exclusive rights to) inventory and resells it under its own terms; the SSP never takes ownership — it sells the seller's inventory under the seller's rules. |
| Advertising Campaign Management | opposite side | Campaign management governs advertising campaigns on specific publisher platforms (buy-side consoles); the SSP is the sell-side machinery those campaigns buy from. |
| Media Buying Platform | different side and scope | Media buying is the whole buying operation (planning, negotiation, insertion orders, reconciliation across channels); the SSP is sell-side infrastructure and shares neither customer nor objects with it. |
| Data Management Platform / DMP | attached layer | DMPs and identity layers supply audience data to the marketplace; the SSP is the transaction machinery they attach to. |
| Header-bidding wrapper | adjacent technique/product | A wrapper mediates demand sources on the publisher's side ahead of ad serving; when sold by an SSP vendor it is a companion product, not the SSP itself. |

## Representative Products

- **Magnite** — largest independent sell-side company; suite of sell-side product lines spanning display/video SSP, streaming video (ad serving + mediation + programmatic), header-bidding wrapper management, and CTV
- **PubMatic** — sell-side platform with publisher and buyer consoles, self-serve deal activation, and a header-bidding wrapper product
- **Index Exchange** — independent supply-side platform and exchange; standards-first positioning (co-author of major supply-chain transparency standards), transaction-level audit logs
- **OpenX** — independent SSP ("The Intelligent SSP™") decomposed into named product lines: curation/deal creation, partner-embedded decisioning, publisher yield platform, and the exchange itself
- **Verve (Smaato SPX)** — mobile-first SSP pole: SDK-based app monetization extended across CTV and web, with curated brand demand

## Sources

Research date: **2026-09-08**

- Magnite — magnite.com (homepage, /sellers/); help.magnite.com/help (Help Center structure) and help.magnite.com/help/glossary (public glossary)
- PubMatic — help.pubmatic.com (Help portal root: Publisher / Activate / Buyer / Commerce Media / OpenWrap)
- Index Exchange — indexexchange.com (homepage, /solution/publishers/, /platform/programmatic-deals/); kb.indexexchange.com (Knowledge Base: Getting started for Media Owners; Creating and managing deals)
- OpenX — openx.com (homepage; product lines OpenXSelect / OpenXBuild / OpenXControl / OpenXExchange)
- Verve Group (Smaato) — verve.com (publisher monetization pages; technical specifications)
- Corroborating sibling research (fetched 2026-09-06): The Trade Desk official glossary; Microsoft Monetize (Xandr) documentation on Microsoft Learn — recorded in research/programmatic-advertising-platform.md

> Sourcing limitations: PubMatic's operational documentation (publisher console, OpenWrap) is login-walled; PubMatic evidence is positioning-level plus the public help-portal root. Magnite's deep help articles require single sign-on; the public glossary and help-center structure were used. OpenX and Verve evidence is product-page level. No numeric limits, fee percentages, or timing windows are stated beyond what the fetched pages document. Historical first-generation SSP documentation was not fetched; the historical breadth of the definition is argued structurally, not from archived sources.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
