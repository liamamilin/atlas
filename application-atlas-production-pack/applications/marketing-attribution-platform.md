# Marketing Attribution Platform

## Overview

A **Marketing Attribution Platform** is an advertiser-side measurement application that determines which marketing touchpoints deserve credit for the conversions an organization records — app installs, purchases, leads, pipeline stages, revenue — by linking recorded marketing interactions to those conversions under an explicit credit-assignment model, and by aggregating that credit into cross-channel views that inform budget and channel decisions.

The problem it exists to solve: every advertising platform reports only its own campaigns and tends to claim full credit for the same conversions. An attribution platform records the journeys, allocates each conversion's credit once under rules the advertiser controls, and reconciles the total across all channels into one independent view.

The defining core is small:

```text
Conversion of record
  ← preceded by → Attributed journey (touchpoints linked to the same user)
  → Attribution model (distributes the conversion's credit)
  → Channel / campaign / source credit aggregates
```

Everything commonly bundled with modern products — spend joins and ROAS/CPA views, de-duplication against platform-reported numbers, lookback windows, identity-resolution machinery, audience activation — is standard capability or variant, not the definition. When the center of gravity shifts to aggregate spend-effect modeling without user-level journeys, the product is drifting toward Marketing Mix Modeling; when it shifts to cross-channel KPI reporting without per-conversion credit, it is a Marketing Analytics Platform.

## Users & Context

Primary users are the people accountable for marketing spend:

- **performance / growth marketers** deciding where to put next month's budget
- **user-acquisition managers** (mobile-app context) optimizing install campaigns across ad networks
- **e-commerce marketing teams** reconciling paid social, search, email, affiliate, TV, and direct mail against orders
- **B2B marketing operations / revenue operations** crediting channels against pipeline stages and closed deals
- **agencies**, running attribution on behalf of client accounts

Secondary consumers: analysts and data teams (who take exports into warehouses and BI tools), and marketing leadership, who consume the budget-allocation outputs. Configuration work — pixels, SDKs, conversion definitions, ad-platform connections — is typically done by marketing ops with developer or tag-manager support.

The working context: the organization runs marketing across many platforms simultaneously, each with its own reporting and its own credit claims. The attribution platform is the independent layer that sits between the ad platforms' self-reported numbers and the organization's own conversion records.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being an attribution platform.

**Conversion of record.** A persistent, identified outcome event on the advertiser's own user population that credit is assigned for. What counts as a conversion varies by market — an app install, a purchase, a lead or pipeline stage, a closed deal with revenue value — but in every case it is a recorded event tied to an identified user, and it is the anchor everything else hangs from. Without it there is nothing to explain.

**Attributed journey.** The recorded marketing touchpoints — ad clicks, ad impressions/views, site sessions, email sends, engagements — captured across channels and linked to the same identified user, preceding the conversion in time. The journey is what credit is distributed across. Without it there is no path, and credit assignment is impossible.

**Attribution model.** The credit-assignment machinery: a selected or configured rule set (first touch, last touch, position-based, even split) or statistical model (data-driven, trained on the advertiser's own journeys) that distributes each conversion's credit across the journey's touchpoints. Because the model divides one conversion's fixed credit among the journey's touchpoints, the allocation is inherently single-counted — this is the conceptual basis of what vendors market as "de-duplication" against platforms that each claim full credit. Without the model the product is a path explorer, not attribution.

```text
Marketing touchpoints (clicks · impressions · sessions · engagements)
  └── linked to the same identified user
      └── journey preceding a conversion
          └── conversion of record (install / purchase / lead / stage / revenue)
              └── attribution model distributes the conversion's credit
                  └── channel / campaign / source credit aggregates
```

### Standard Capabilities

Mature products commonly add the following. They make attribution practical; they do not define the Type.

- **Spend ingestion and efficiency ratios** — ad-platform cost joined to credited outcomes, producing ROAS, CPA, ROI, and CAC views and budget-allocation analyses.
- **Independent vs platform-reported views** — side-by-side comparison of the platform's own claimed conversions with the platform's de-duplicated allocation, plus discrepancy diagnostics explaining why the numbers differ.
- **Multiple models** — rule-based models (first touch, last touch, linear, position-based) alongside data-driven models computed from the advertiser's own journey data; users switch between them and watch credit re-allocate.
- **Eligibility windows** — configurable lookback windows bounding which touchpoints qualify for credit; outcomes with no qualifying touchpoint fall into an organic / unattributed / direct bucket.
- **View-through attribution** — crediting ad impressions and views, not only clicks, typically with shorter windows than click-through.
- **Conversion configuration** — defining which events count as conversions (with exclusions for test traffic, admin users, returns), and QA over the capture.
- **Channel taxonomy mapping** — machinery that maps raw touchpoints (URL parameters, referrers, vendor names) into a managed channel / source / campaign hierarchy, with unmapped events surfaced for correction.
- **Identity resolution** — linking touchpoints to conversions across devices and sessions via device IDs, cookies, email, or (in B2B) contact-to-company mapping.
- **Reporting and export** — dashboards, scheduled reports, and warehouse/BI destinations.

### One Structure, Many Implementations

The core model is conceptual. Implementations differ sharply by market:

```text
Concept:            Conversion of record
Implementations:    app install / re-engagement (mobile) · purchase (e-commerce) ·
                    CRM stage / deal with revenue (B2B)

Concept:            Touchpoint capture
Implementations:    attribution links, install referrers, device-ID matching (mobile) ·
                    URL parameters, impression pixels, ad-server logs, promo codes,
                    post-purchase surveys, direct-mail matchback (e-commerce) ·
                    UTM-tagged sessions, CRM/marketing-automation events (B2B)

Concept:            Identity substrate
Implementations:    device IDs · cookies · email · logged-in accounts ·
                    contact-to-company (account) mapping

Concept:            Attribution model
Implementations:    last-touch rule · position-based rules · even split ·
                    data-driven/statistical model built on the advertiser's journeys
```

A reader who has only seen one implementation — say, last-click purchase attribution in an e-commerce dashboard — should still be able to recognize a mobile install-attribution product or a B2B revenue-attribution product from the core model.

## How It Works

### Connect sources and instrument capture

```text
Connect ad platforms (API credentials) and ingest their campaign/spend data
→ deploy capture on owned properties (site pixel / app SDK / tag manager)
→ connect the conversion source (e-commerce platform, webhooks, batch files, CRM)
→ map incoming touchpoints into the channel taxonomy
```

This is the onboarding-heavy phase: the platform's value depends on complete capture, so products invest heavily in integration guides per ad network and per commerce/CRM platform.

### Record conversions

Conversions arrive as events tied to an identified user — a purchase event from the commerce platform, an install event from the app SDK, a stage change or deal from the CRM. The advertiser configures which events count, excludes test and internal traffic, and (in e-commerce) ingests returns and third-party marketplace purchases so credited revenue reflects reality.

### Build journeys and apply the model

The platform links each conversion to the touchpoints recorded for the same user before the conversion — within the configured eligibility windows where the product uses them. The selected attribution model then distributes the conversion's credit across those touchpoints. Users can switch models and watch the value attributed to each channel change; comparing models is a first-class activity, not a hidden setting.

### Read credit views and act

```text
Cross-channel attribution report (credit by channel / source / campaign)
→ compare against platform-reported numbers (discrepancy diagnostics)
→ inspect journeys (paths, funnel position, channel overlap)
→ shift budget toward channels with stronger credited performance
→ optionally feed conversions back to ad platforms to improve their optimization
```

### Capability tiers

**Defining core** — conversion of record; attributed journey; attribution model.

**Standard capabilities** — spend joins and efficiency ratios; independent vs platform-reported views; multiple models including data-driven; eligibility windows; view-through attribution; conversion configuration and exclusions; channel taxonomy mapping; identity resolution; reporting/exports.

**Optional / variant** — audience activation and conversion-API feeds back to ad platforms; MMM and incrementality-testing siblings inside a measurement suite; enterprise custom model builders; agency/multi-client structures; new-vs-repeat customer splits; retargeting/re-engagement semantics (mobile).

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Cross-channel attribution report

The primary working surface.

- Purpose: show credited conversions/revenue by channel, source, and campaign under the selected model.
- Typical information: channel/source/campaign rows, credited conversions and value, spend and efficiency ratios where joined, comparison against platform-reported figures.
- Primary actions: switch attribution model, change date range, filter by channel or campaign, export.

### Journey / path explorer

- Purpose: inspect how individual users or aggregated cohorts traveled to conversion.
- Typical information: ordered touchpoint sequences, funnel positions, channel overlap, time-to-convert.
- Primary actions: filter journeys, drill into a segment, compare paths across models or periods.

### Conversion and model configuration

- Purpose: control what gets credited and how.
- Typical information: conversion event definitions, exclusions, eligibility windows, model catalog, taxonomy mappings, unmapped events.
- Primary actions: define/edit conversions, set windows, select or build models, map channels, QA capture.

### Data connection surface

- Purpose: maintain the integration fabric.
- Typical information: connected ad platforms and their auth status, pixel/SDK status, CRM/commerce connections, spend-report ingestion.
- Primary actions: connect/re-authenticate sources, verify pixel firing, schedule spend reports.

### Diagnostics

- Purpose: explain differences between the platform's numbers and every other system's numbers (ad platforms, web analytics, internal data).
- Typical information: per-platform discrepancy breakdowns, de-duplication effects, late-arriving conversions, historical revisions.
- Primary actions: drill into a discrepancy, adjust exclusions, backfill.

## Important Rules / Behaviors

### One model at a time; switching re-allocates everything

The displayed credit is always credit *under a selected model*. Switching from last-touch to a data-driven model re-allocates the same conversions across the same journeys and changes every channel's numbers. Products treat model comparison as a core interaction.

### Credit is a fixed budget per conversion

Each conversion's credit is allocated once across its journey's touchpoints — whether 100% to one touch or fractions across many. This is why an attribution platform's channel totals reconcile to the advertiser's actual conversion count while each ad platform's self-reported totals sum to more than reality.

### Eligibility windows bound the journey

Touchpoints qualify for credit only within defined windows preceding the conversion (products commonly make these configurable, with view-through windows shorter than click-through). Outcomes with no qualifying touchpoint are classified as organic / unattributed / direct — a first-class bucket, not an error state.

### Deterministic evidence usually outranks modeled evidence

Where both deterministic links (referrers, device IDs, URL parameters) and probabilistic/modeled touchpoints exist, products commonly prioritize the deterministic ones; clicks commonly outrank impressions as stronger engagement signals. The exact priority rules are implementation-specific and differ most in the mobile ecosystem.

### Attribution numbers change retroactively

Late-arriving conversions, returns, model updates, and data backfills mean credited numbers for past periods can be revised. Products document this explicitly and provide revision/backfill handling; users are trained not to expect immutable history.

### Identity resolution is a prerequisite

Touchpoints can only be credited if they can be linked to the converting user. Traffic that cannot be resolved lands in direct/unspecified/anonymous buckets. In B2B implementations, resolution extends from the person to their company so journeys can be read at the account level.

### Discrepancy is structural, not a bug

Ad platforms measure their own campaigns with their own windows and credit rules, so their numbers will not match the independent allocation. Attribution platforms ship diagnostics for exactly this gap.

## Variants

- **Mobile-app attribution (MMP)** — conversions are installs, re-engagements, and re-attributions; touchpoints are ad-network clicks/impressions matched via device IDs, install referrers, and platform-adjudicated APIs, with probabilistic modeling where IDs are unavailable; deep integration with the app-store/ad-network ecosystem and agency workflows.
- **E-commerce / DTC multi-touch attribution** — conversions are purchases (net of returns); the distinctive work is capturing hard-to-track channels — promo codes, post-purchase surveys, direct-mail address matching, TV spot logs — alongside standard digital touchpoints; strong budget-allocation and payback orientation.
- **B2B revenue attribution** — conversions are CRM stages and deals with revenue value; journeys are account-based timelines assembled from web tracking plus CRM/marketing-automation events across multiple stakeholders; "influenced vs attributed" distinctions and pipeline-stage scoping are characteristic.
- **Deterministic-first vs model-led philosophies** — products differ in how much credit allocation is a transparent rule the advertiser can fully explain versus a statistical estimate built from the advertiser's own data; explainability-vs-pattern-detection is the recurring trade-off.
- **Measurement-suite module** — attribution sold alongside marketing mix modeling and incrementality testing as complementary methodologies over one shared data foundation, each answering a different question (tactical credit vs strategic planning vs causal validation).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Marketing Analytics Platform | measures cross-channel marketing KPIs on consolidated data; per-conversion credit assignment is not its center — attribution platforms grow out of adding the model + journey machinery |
| Marketing Mix Modeling Application | models aggregate spend effects over time series without user-level journeys or identity; attribution works at the individual-journey level |
| Web Analytics (GA-class; no dedicated leaf) | measures site/app behavior; its last-click conversion reports overlap the surface but the center is behavior analytics, not cross-channel credit reconciliation |
| Customer Data Platform / Audience Management | resolves identity to build and activate audiences; attribution platforms consume identity in service of credit assignment |
| Ad Server / DSP / platform-native attribution | serve and optimize ads and measure their own campaigns in isolation; the attribution platform is the independent cross-channel reconciler |
| Performance & Attribution Platform (investment) | same word, unrelated universe — distributes portfolio returns across holdings/factors vs a benchmark, for asset managers; no shared objects, users, or workflows with marketing attribution |
| A/B Testing / Digital Experimentation Platform | establishes causal lift through controlled experiments; attribution assigns observational credit — incrementality testing is the sibling methodology between them |
| Marketing Automation / Campaign Management Platform | executes campaigns; attribution measures and credits their outcomes |
| Affiliate Network / Affiliate Management | credits individual partner referrals for commission settlement; attribution platforms ingest affiliate data as one channel among many |
| CRM / Lead Management | holds the customer relationship and journey history as activity records; the credit-allocation machinery is not its center — attribution outputs typically feed into it |

The closest seams are Marketing Analytics Platform (measurement without credit assignment) and Marketing Mix Modeling (modeling without user-level journeys). The practical test: if the product records journeys and allocates each conversion's credit under a selectable model, it is an attribution platform; if it reports KPIs on consolidated marketing data, it is an analytics platform; if it models spend effects over aggregate time series, it is MMM.

## Representative Products

- **AppsFlyer** — mobile-app attribution at app-ecosystem scale (install/re-engagement attribution, device-ID and platform-adjudicated methods, probabilistic modeling)
- **Rockerbox** — e-commerce/DTC multi-touch attribution over a first-party data foundation, including hard-to-track offline channels; ships MTA, MMM, and incrementality testing as distinct methodologies
- **Dreamdata** — B2B revenue attribution on account-based journeys from web tracking plus CRM, with rule-based and data-driven models over pipeline stages and deals

The core model was checked against older and manual implementations (UTM + spreadsheet last-touch joins, ad-server click-through conversion tags, coupon-code-per-channel tracking) to avoid over-fitting the definition to the current modeled-multi-touch generation.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (official documentation):

- AppsFlyer — "AppsFlyer attribution model" — https://support.appsflyer.com/hc/en-us/articles/207447053-AppsFlyer-attribution-model
- AppsFlyer — Attribution concepts section — https://support.appsflyer.com/hc/en-us/sections/6551394235409-Attribution-concepts
- AppsFlyer — Knowledge Base (Measure & Engage / Measure paid media structure) — https://support.appsflyer.com/hc/en-us
- Rockerbox — product page — https://www.rockerbox.com/
- Rockerbox — Help Docs (attribution types; marketing touchpoints tracking; conversion tracking; spend ingestion; UI views; discrepancies) — https://help.rockerbox.com/
- Dreamdata — Documentation (Overview of Attribution Models; Data Hub; Stage Models; Revenue Analytics; Sources; Glossary) — https://docs.dreamdata.io/

> Sourcing limitation: Northbeam and Triple Whale (additional e-commerce attribution candidates) could not be reached from the research environment and were dropped after repeated failures; the modeled/probabilistic multi-touch sub-pole is therefore evidenced mainly through one product, and claims about that sub-pole are held at correspondingly reduced strength. Precise operational parameters (default window lengths, model percentages, onboarding timelines) are product-specific facts recorded in the paired Research Notes and are not asserted as industry standards in this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
