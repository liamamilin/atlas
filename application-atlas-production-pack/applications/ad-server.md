# Ad Server

## Overview

An **Ad Server** is the request-time execution engine of digital advertising. It holds a managed pool of ads — registered on behalf of advertisers and organized into campaigns, each carrying delivery rules — and, for every ad call that arrives from a delivery surface, it decides which ad, if any, to deliver: filtering by eligibility, resolving competition among qualifying ads, and returning the selected creative for rendering. Every delivery is recorded, and those records are the substrate for reporting, pacing, and billing.

The defining structure is small:

```text
Managed ad pool (ads + campaigns + delivery rules)
└── Per-request ad call from a delivery surface
    └── Rule-based selection decision (eligibility → competition → winner)
        └── Response returning the selected ad for rendering
            └── Recorded delivery events (impressions, clicks, conversions)
```

Everything else commonly associated with modern ad serving — real-time bidding, header bidding, unified auctions, first-party audience segments, forecasting, self-service portals, retail-media formats — is widespread in current products but is not part of the defining core. Self-hosted ad servers from the tag-and-banner era satisfy the same definition without any of those specifics, as do API-first engines that never render anything themselves.

When the per-request decision disappears (scheduled sends, planned buys only), or the paid, accountable nature of the content disappears (organic content selection), the product has drifted into a different Application Type.

## Users & Context

The primary users are advertising operations staff — commonly ad ops or traffickers — who turn sold deals into running delivery: they create campaigns, attach creatives, set targeting and goals, and watch delivery against commitments.

Around them:

- **yield managers / ad sales operations** — own the competition rules (priority tiers, reservation, programmatic fill) and inventory availability
- **advertisers and agencies** — increasingly through self-service portals: create campaigns, monitor delivery and performance
- **publishers** — configure the placements where ads appear and consume delivery and revenue reports
- **developers** — integrate the delivery surface: ad tags, mobile SDKs, or server-to-server calls
- **analysts / finance** — consume delivery and revenue reports for billing and reconciliation

The work context is a live production system: campaigns run against real traffic in real time, delivery commitments have financial consequences, and mistakes (wrong targeting, broken creative, mis-set caps) are immediately visible on production placements.

## Core Model

### The Defining Core

```text
Managed ad pool
└── Per-request ad call
    └── Selection decision
        └── Response with the selected ad
            └── Recorded delivery events
```

Five properties. If any one is removed, the product is no longer recognizable as an ad server:

- **Managed ad pool** — the system holds the ads it delivers: paid promotional content registered on behalf of advertisers, organized into campaigns, each carrying rules for when, where, to whom, and how much to deliver. Without it there is nothing to deliver.
- **Per-request ad call** — at delivery time, a surface (a tag on a web page, an in-app SDK, a server-to-server API call, a video template, or a downstream system) calls the platform and identifies a placement plus its context. Without it, delivery is not request-time.
- **Rule-based selection decision** — the platform evaluates which ads are eligible for this request (targeting, schedule, size, caps, frequency) and resolves competition among the eligible ones (priority tiers, weights, or an auction) to pick a winner — or none. Without it, the system is a scheduler or a content rotator.
- **Response with the selected ad** — the platform returns the creative, or decision data from which the surface renders the ad. Without it, no delivery occurs.
- **Recorded delivery events** — impressions (and typically clicks and conversions) are logged against the delivered ad and campaign. This accountability is what makes delivery governable: pacing, capping, reporting, and billing all depend on it.

### The Two-Sided Registry

Mature products organize the ad pool and the delivery surfaces as two hierarchies that meet at the moment of delivery:

```text
Demand side                          Supply side
Advertiser                           Publisher / Site owner
└── Campaign                         └── Site / Property
    └── Flight / Line item               └── Placement / Zone
        └── Ad / Creative                    └── (tag / SDK / API surface)
```

- A **campaign** is the advertiser's unit of commitment: a budget or goal, a schedule, and a set of delivery rules. Products differ in how many levels sit between campaign and ad (a mid-layer often named flight or line item), but the shape — advertiser → campaign → rules-and-ads — is stable.
- A **placement** (commonly called a zone) is a defined ad position on a surface, with an expected size or format, exposed to the platform through a tag, SDK, or API endpoint. Groupings of placements (sites, channels, placement groups) let campaigns be aimed at many positions at once.
- The **creative** is the actual displayed content — image, video, native composition, or a reference to a third-party-hosted ad — held in a library and attached to ads. Hosting is separable from decisioning: products commonly serve creatives they host and track creatives hosted elsewhere.

The link between the two sides is the delivery rule set: which campaigns may serve on which placements, under what conditions, and with what precedence.

### Standard Capabilities

A typical modern product carries most of the following. They are not what makes the product an ad server, but they make it operable at scale:

- **Targeting** — conditions an ad places on its own delivery: geography, device and platform, keyword or contextual signals, custom key–values passed with the request, audience segments (first-party or third-party), day and time windows, and frequency capping (limiting exposures per user over a period).
- **Goals, pacing, and caps** — a campaign's goal (a number of impressions, clicks, conversions, a revenue amount, or a share of traffic) drives throttling so the goal is reached by the end date; pacing shapes delivery over time (even, front-loaded, or back-loaded); caps are hard limits that switch a campaign off.
- **Competition model** — when several ads qualify for the same request, precedence must be resolved. Common mechanisms: priority tiers (higher tiers fill first, unfilled impressions cascade down a waterfall), relative weights (proportional rotation), and auctions (highest expected value wins). Many products combine several.
- **Fallback chain** — when nothing qualifies, the platform serves a default: a house ad promoting the publisher itself, or programmatic backfill purchased from external demand sources.
- **Delivery-event tracking** — impression, click, and conversion recording through pixels, redirect URLs, or server events; hygiene rules distinguishing counted impressions from raw requests.
- **Reporting** — delivery against goals, click-through and conversion rates, revenue by rate type (per thousand impressions, per click, per action, or flat), with breakdowns by campaign, placement, geography, and time; custom and scheduled reports; log-level export in data-heavy products.
- **Forecasting** — estimating future availability for a placement and targeting combination, and how a new campaign would contend with existing reservations.
- **Creative management** — hosting creatives or tracking third-party-hosted ones, size and type validation, third-party ad tags, macros for click and data passing, and rotation strategies across multiple creatives of one ad (even, weighted, or performance-optimized).
- **Programmatic demand integration** — connecting external demand sources (real-time bidding endpoints, header bidding) as a fill layer beneath direct campaigns.
- **Conversion tracking / attribution** — tying downstream user actions back to delivered ads.
- **Roles and portals** — an operations console for staff; scoped access and often white-labeled self-service portals for advertisers and publishers.

### One Structure, Many Implementations

The core model is conceptual. Specific products realize each concept differently:

```text
Concept:            Per-request ad call
Implementations:    JavaScript tag on a page, mobile SDK, server-to-server API call,
                    video ad template (VAST), email zone tag, call from a downstream platform

Concept:            Competition model
Implementations:    priority waterfall, static weights, eCPM auction, unified auction
                    with programmatic demand, hybrid (guaranteed tiers + RTB fill)

Concept:            Delivery event
Implementations:    impression pixel/redirect, click redirect, server-to-server conversion,
                    log-level event streams
```

A reader who has only seen one implementation — say, a JavaScript-tag web ad server — should still be able to recognize a server-to-server retail-media engine or a self-hosted banner server from the core model.

## How It Works

### Set up the two sides

```text
Register publishers and their placements (or sites/zones)
→ define sizes and formats per placement
→ generate the integration: ad tags, SDKs, or API endpoints
→ place the integration on the delivery surfaces
```

### Register demand

```text
Create the advertiser
→ create a campaign with schedule, goal/budget, and rate type
→ attach creatives
→ set targeting and frequency rules
→ assign the campaign to placements (directly or through competition rules)
```

### Configure the competition

```text
Define precedence: priority tiers (direct-sold above house, programmatic beneath)
→ choose the selection method within each tier (weights or auction)
→ set the fallback: house ad or programmatic backfill
→ optionally reserve inventory for guaranteed commitments
```

### The delivery loop (per request)

```text
Ad call arrives (placement + context: size, location, user/key, keywords, custom data)
→ filter: which campaigns are eligible? (schedule, targeting, size, caps, frequency)
→ compete: among eligible ads, resolve precedence (tier order → weights or auction)
→ select a winner — or fall through to the fallback chain
→ respond: return the creative or decision data
→ the surface renders the ad
→ record: impression (and later click / conversion) against the ad and campaign
```

The loop runs for every request, in real time, across all live traffic. The decision itself is usually logged, so delivery can be audited and explained.

### Operate over time

```text
Monitor delivery vs goals (pacing dashboards, campaign views)
→ adjust: raise weights or bids, loosen targeting, fix under-delivery; cap or pause over-delivery
→ forecast upcoming availability for new commitments
→ rotate or optimize creatives by measured performance
→ report and bill: revenue by rate type, reconciled with advertisers and publishers
```

### Core vs common vs optional

**Defining core** — without these, not an ad server:

- managed ad pool (ads + campaigns + delivery rules)
- per-request ad call
- rule-based selection decision
- response returning the selected ad
- recorded delivery events

**Standard capabilities** — present in most mature products:

- two-sided registry (advertiser/campaign/creative vs publisher/placement)
- targeting and frequency capping
- goals, pacing, caps
- competition model (tiers/weights/auction) with fallback chain
- impression/click/conversion tracking and reporting
- creative management with rotation
- forecasting
- programmatic demand integration
- roles, scoped access, self-service portals

**Common variants / optional** — depends on side, surface, scale, and business model:

- real-time bidding and header bidding as fill or primary demand
- unified auction across direct and programmatic demand
- video/CTV server-side insertion, audio, DOOH, email, in-app surfaces
- retail-media formats (sponsored products, sponsored listings) driven by a product catalog
- advertiser-side third-party serving with brand verification
- self-hosted open-source deployment
- white-label marketplaces

## Interfaces

The following surfaces are described conceptually. Names and layouts vary by product.

### Campaign / trafficking console

The operations core where demand is registered and maintained.

- campaign lists with status, delivery progress, and schedules
- campaign editors: goal and budget, rate type, dates, targeting, attached creatives
- primary actions: create/duplicate campaign, attach creative, set targeting and goals, activate/pause/archive

### Inventory and integration management

Where the supply side is registered and exposed.

- publishers/sites and their placements (sizes, formats, classification)
- tag/SDK/API endpoint generation per placement
- primary actions: create placement, generate and copy tags, group placements, set classification

### Delivery monitoring

The live view of the delivery loop.

- delivery vs goal per campaign (pacing indicators), today/yesterday/lifetime
- under-delivery and over-delivery warnings; per-placement fill
- primary actions: adjust pacing, pause/enable, rebalance weights or priorities

### Reporting

The accountability surface.

- dimensions (campaign, creative, placement, geography, time) × metrics (impressions, clicks, CTR, conversions, revenue, effective rates)
- custom report builders, scheduled reports, log-level export in data-heavy products
- primary actions: build report, schedule, export

### Forecasting

Availability planning for future commitments.

- available impressions and total capacity for a targeting combination
- contending campaigns; reservation of inventory for guaranteed deals
- primary actions: run forecast, reserve inventory

### Self-service advertiser portal

A scoped, often white-labeled surface where advertisers create and watch their own campaigns.

- campaign creation with guided targeting; performance dashboards
- access limited to the advertiser's own objects

### Integration surfaces (tags / SDKs / APIs)

The machine-facing side of the platform.

- ad tags and SDKs that trigger ad calls and render responses
- server-to-server decision APIs (submit request context, receive decision data)
- management APIs (create and update campaigns, placements, creatives)
- reporting APIs and event endpoints

## Important Rules / Behaviors

### A request can legitimately return no ad

Eligibility filtering can eliminate every candidate; the platform then walks a fallback chain (lower-priority demand → house ad → programmatic backfill → blank). "Nothing qualified" is a normal outcome, not an error.

### Guaranteed vs best-effort delivery

A committed (guaranteed) campaign reserves inventory: the platform treats its goal as an obligation and forecasts against it. Non-guaranteed campaigns serve best-effort beneath the reserved tier. Reservation changes what else can be sold into the same placements.

### Precedence is explicit

Higher-priority tiers fill first; unfilled impressions cascade downward. Within a tier, selection follows the tier's method — proportional weights or an auction. Rate and price affect delivery only where the selection method uses them (auction-style); under pure weight rotation, price is reporting metadata, not a delivery input.

### Goals pace; caps cut off

A goal throttles delivery over the campaign's lifetime to land on target by the end date; a cap is a hard stop. Caps can be slightly overshot under traffic surges — some products document this behavior rather than promising exact cutoffs.

### Frequency capping requires knowing the user

Per-user caps depend on a user identifier carried by the request. Unidentified users may bypass frequency caps; some products make serving to unidentified users an explicit choice.

### Requests are not impressions

An ad request (a call to the platform) does not always produce a counted impression (a rendered, measurable ad). Mature products track both and explain the difference.

### Creative eligibility is structural

A creative's size and type must match what the placement accepts; mismatches silently prevent delivery. Multi-creative ads rotate under the campaign's rotation strategy (even, weighted, or performance-optimized).

### Ad quality and competitive separation

Platforms enforce rules about which creatives may appear on which inventory (content categories, brand restrictions, competitive exclusions). Where rules exist at two levels — for example a network-wide profile and a per-publisher profile — sampled products commonly make the stricter rule win: the more local restriction can tighten but not loosen the broader one.

### Campaign states

Campaigns and their mid-layer units move through states — inactive (being prepared), active (delivering), completed/expired (goal reached or dates passed), archived (hidden from working lists). State changes are the operator's main lever on live traffic. Exact labels vary by product.

## Variants

- **Publisher-side ad server** — the classic form: a publisher or network manages direct-sold campaigns over its own placements, with programmatic demand as backfill or competition (most sampled products).
- **Advertiser-side ad server** — serves an advertiser's campaigns across many publishers' surfaces for consistent measurement and brand control; the object model is the same demand hierarchy without owned placements.
- **Combined suite** — one product containing the ad server plus selling machinery (deals, payment rules) and/or buying machinery (bidding); common at enterprise level.
- **API-first / embedded delivery** — the platform is consumed as an API by companies building their own ad or sponsored-content products (retail media, marketplaces, promoted listings); the UI is secondary.
- **Surface variants** — display web, in-app, video (VAST templates, server-side insertion for streaming TV), audio, digital out-of-home, email newsletters, native in-feed. The delivery loop is identical; the request transport and rendering differ.
- **Commerce / retail media** — placements are on-site commercial surfaces (search results, category pages, product pages); ads are often generated from a product catalog rather than uploaded creatives.
- **Deployment variants** — SaaS (most), hosted open source, self-hosted open source for operators who run their own infrastructure.
- **Business-model variants** — internal tool for one publisher; white-label platform powering many publishers' self-service marketplaces; infrastructure for media networks.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Ad Delivery Platform | probable alias | in market usage the two names describe the same functional system — the request-time selection and delivery engine; every researched product self-identifies as an "ad server"/"ad serving" system, and "ad delivery" is the delivery-centric framing of it. Flagged for a joint review of the two directory entries |
| Demand-side Platform / DSP | adjacent (buy-side) | a DSP responds to external bid requests on behalf of advertisers across many sellers; it holds no placement structure. Remove the managed ad pool and placement registry, keep only auction bidding → DSP |
| Supply-side Platform / SSP | adjacent (sell-side) | an SSP packages and sells inventory (deals, payment rules, buyer eligibility); request-time selection is not its core. Remove selection and keep selling machinery → SSP. Enterprise suites often contain both |
| Programmatic Advertising Platform | umbrella | a marketing term spanning DSP + SSP + exchange + data; no distinct structure of its own |
| Advertising Campaign Management | upstream | plans and manages campaigns (budgets, channels, trafficking instructions) but does not execute request-time delivery; its output is trafficked into an ad server |
| Creative Management Platform / DCO | upstream (creative) | produces and adapts creatives; the ad server decides when and where they render. Its output enters the ad server as creatives |
| Recommendation / Personalization Engine | structural neighbor | also selects an item per request from a candidate pool — but the content is organic and there is no per-delivery accountability to a paying advertiser. Remove paid/accountable semantics → personalization engine |
| Email Marketing Platform | different mechanism | scheduled sends to a list; no per-request placement call, no impression semantics. (Serving ads *inside* newsletters is a surface variant of this Type, not email marketing) |
| CDN / creative hosting | infrastructure only | transports content but performs no selection decision and holds no campaign rules |

The boundary with DSP and SSP is the most important one, because enterprise products bundle all three. The structural test is the unit of work: the ad server's unit is the managed ad pool and the per-request selection on known placements; the DSP's unit is the bid response in external auctions; the SSP's unit is the packaged inventory offering to buyers.

## Representative Products

- Kevel — API-first ad server; retail media and sponsored-listing infrastructure
- Microsoft Monetize (Xandr) — enterprise suite combining an ad server with selling and buying machinery
- AdButler — independent multi-channel ad server with self-service portals; SMB and commerce media
- Revive Adserver — free open-source, self-hosted ad server (phpAdsNew lineage)

Google Ad Manager — the dominant publisher ad server — is a market anchor for this Type, but its documentation could not be reached during research (see Sources); no product-specific claims about it are made here.

## Sources

Research date: **2026-09-06**

- Kevel — official developer documentation: Introduction to Kevel, Ad Decision Engine Overview — https://dev.kevel.com/docs/understanding-kevel.md , https://dev.kevel.com/docs/delivery-basics.md
- Microsoft Monetize (Xandr) — official product documentation on Microsoft Learn: About Monetize, Object Hierarchy — https://learn.microsoft.com/en-us/xandr/monetize/about-monetize , https://learn.microsoft.com/en-us/xandr/monetize/object-hierarchy
- AdButler — official help center: How AdButler serves ads (plus related articles: What is AdButler?, Requests vs. impressions, Glossary) — https://www.adbutler.com/help/article/how-adbutler-serves-ads , https://www.adbutler.com/help
- Revive Adserver — official repository README (vendor site returned HTTP 403; README used as the official description) — https://github.com/revive-adserver/revive-adserver
- Equativ — homepage positioning only (publisher-solution lines naming an ad server alongside an SSP; product docs unreachable) — https://equativ.com/

> Sourcing limitation: Google Ad Manager documentation (support.google.com, developers.google.com) was unreachable from the research environment on 2026-09-06 after repeated attempts and was abandoned. The model above is derived from the four directly evidenced products; claims are calibrated accordingly, and precise numeric behaviors (priority ranges, pacing defaults, cap tolerances) are intentionally not stated. Advertiser-side ad serving is evidenced through the buy-side structure and third-party-creative tracking of the sampled enterprise suite rather than a dedicated advertiser-side product.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
