# Mobility-as-a-Service Platform

## Overview

A **Mobility-as-a-Service Platform** is a traveler-facing service that integrates multiple transport providers — public transit, shared bikes and scooters, shared cars and mopeds, taxi and ride-hailing — into a single service, so that one account can plan a journey across those providers' modes and then book and pay for the chosen services without leaving the platform.

The defining structure is a three-part loop:

```text
One account (identity + payment, verified where modes require)
  → plan a journey across multiple providers' modes
  → book the chosen option in-product
  → pay through the unified payment arrangement
  → trip recorded, receipted, and supported
```

Everything else commonly associated with the category — real-time arrival data, price and carbon comparison, subscription bundles, employer-funded mobility budgets, physical mobility stations, operator analytics — is widespread in current products but is not what makes the product a MaaS platform. A service that only plans journeys is a journey planner; a service that only handles one provider's vehicles is that provider's app; a multi-operator fare card without planning or booking is fare integration, not a mobility service.

## Users & Context

**Travelers** are the primary users: commuters, residents, and visitors making door-to-door trips in a city or region. They come to combine modes — a train plus a shared bike, a bus plus a taxi — or to replace several single-provider apps with one. The usage context is overwhelmingly mobile and on the move, though some deployments deliver the same loop as a web planner embedded in a transit authority's or city's website.

**The operating organization** stands behind the service. It may be a public transit authority or city (the dominant pattern for city-branded services), a private operator, an employer offering staff mobility, or a community program. It decides which providers are integrated, on what commercial terms, and under which local rules.

**Integrated mobility providers** are the third party in every booking: transit agencies, car-sharing and bike-sharing operators, micromobility fleets, taxi and ride-hailing companies. The platform mediates their services to the traveler; the traveler's booking relationship with each provider is created and governed through the platform.

**Platform vendors** are the supply side behind many branded services: they build and operate the white-label apps, the routing engines, the provider integrations, and the operator back offices on which authority- and city-branded services run.

## Core Model

### The Defining Core

Three structures, jointly held. Remove any one and the product stops being a MaaS platform:

- **Multimodal journey planning across multiple integrated providers** — the traveler enters an origin and destination and receives route options that combine modes from more than one provider: scheduled transit alongside shared vehicles, on-demand rides, or commercial transport. The plan is the discovery surface for everything that follows. Without the multi-provider integration, the product is a single-provider app; without planning, it is a booking portal with no way to discover options.
- **The single mobility account** — one registration binding the traveler's identity and payment method, usable across all integrated providers, so the traveler does not re-register with each one. Where a mode requires a credential (typically driving a car or moped), the account carries a verified licence or ID that gates exactly those services. Providers are commonly activated per service — the traveler connects to the ones they intend to use, and only connected providers receive the data needed to fulfill a journey. Without the standing account, the product degenerates into per-provider guest checkout and the "as-a-Service" relationship disappears.
- **Booking and payment through the platform** — the chosen option is transacted in-product: a public-transport ticket is purchased and held for display, a shared vehicle is reserved and unlocked, a taxi or ride-hail trip is booked. Payment runs through the unified arrangement stored on the account, and the completed journey is recorded on the platform side with its price, date, and services used. Without this leg, the product is a read-only planner or a link-out directory.

The three are jointly load-bearing:

```text
Planning alone                       → a journey planner (information only)
Account alone                        → a fare card or payment wallet
Booking without planning + account   → a set of booking forms
Planning + account without booking   → a planner with saved payment and no transactions
Account + booking without planning   → a booking portal without discovery
```

### What Travelers Work With

- **Journey options** — the route alternatives the planner returns for a request, each combining one or more modes and providers, described by duration, price, and commonly other decision factors (comfort, carbon, accessibility).
- **Providers and services** — the integrated mobility offerings behind the options. Each provider carries its own operating rules, which the platform surfaces at the point of use: how a vehicle is unlocked, how pricing is computed, what condition a vehicle must be returned in.
- **Tickets and bookings** — the transacted objects. A purchased ticket is a right to travel held for validation; a vehicle booking is a reservation or an open usage; a booked ride is a commitment to a driver-supplied trip.
- **Trips** — the platform-side record of completed journeys: what was used, when, at what price. Trips are the basis for receipts, invoices, and support.
- **Payment arrangements** — the payment methods stored once on the account and charged for all providers; some services add prepaid balances, vouchers, or employer-funded budgets as payment sources.
- **Credentials** — the verified documents (identity, driving licence) attached to the account that determine which services may be used.

### One Structure, Many Implementations

The core model is conceptual. Products realize each part differently:

```text
Concept:            Journey planning
Implementations:    in-app multimodal search, embedded web planner on an
                    authority's site, planner exposed through an API/SDK

Concept:            Provider integration
Implementations:    deep in-app booking with per-provider rules and support,
                    ticket purchase and display, wallet-based payment,
                    shallower planner-plus-wallet forms

Concept:            Commercial model
Implementations:    pay-as-you-go per trip, subscription bundles,
                    employer mobility budgets, prepaid vouchers
```

A reader who has only seen one city's branded mobility app should still recognize a web-based regional planner with booking, or an API platform powering several cities, as the same Type from the core model.

## How It Works

### Join once

```text
Create the account (email, mobile verification)
→ add a payment method
→ verify credentials where needed (e.g. driving licence for car/moped modes)
→ connect to the providers you intend to use
```

Registration happens once for all modes. Connection to individual providers is typically opt-in per service, and connections that require a verified licence stay locked until verification completes. The traveler's existing accounts with individual providers do not carry over — the platform account is a new, separate relationship, and purchases commonly remain scoped to the app in which they were made.

### Plan

```text
Enter a destination (or pick a mode directly)
→ see route options across the integrated providers
   with times, prices, and availability
→ compare and choose
```

The planner is the entry point for most journeys. Mature products layer real-time information — vehicle positions, arrival predictions, service disruptions — on top of scheduled data, and present options side by side so the traveler can weigh time against price, weather, or preference.

### Book and pay

```text
Select an option
→ the platform transacts it:
   transit ticket → purchased, held for display/validation
   shared vehicle → reserved, unlocked (scan/code/PIN)
   taxi / ride-hail → booked
→ charged to the unified payment arrangement
→ guidance continues through usage (unlock instructions, trip end)
```

The platform carries each provider's operating specifics into the flow — an unlock code here, a pricing rule there, a vehicle-condition check — so the traveler completes the whole journey without opening the provider's own app.

### Close and account for

```text
Complete the journey
→ trip recorded with date, price, services used
→ receipt / invoice available per trip
→ confirmation communicated
→ problems routed to the provider actually booked
```

Trip history is the traveler's financial and practical memory of the service: per-trip receipts, invoice downloads, and a record of which provider was used. Support follows the same grain — questions about a specific booking go to the provider that fulfilled it, reachable from within the platform; questions about the service itself go to the operator.

### The operator side

Behind the traveler surface sits the machinery that makes the service operable: administration of user issues and feedback, fraud controls, restrictions on specific vehicle classes, financial and usage reporting, promotional campaigns, and monitoring of the service in real time. Platform vendors deliver this as the back office of their product, together with analytics over usage patterns and tools for maintaining the underlying transport data (stops, schedules, fares). The traveler never sees this layer directly — only its results: providers that work, prices that settle, and support that answers.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Home / map

The primary surface.

- shows nearby services, stations, and stops
- asks where the traveler wants to go
- primary actions: enter a destination, pick a mode, open the ticket store

### Journey planner

The discovery surface.

- route options across modes and providers with duration, price, and availability
- real-time layers (arrivals, disruptions) where offered
- primary actions: compare options, select one, set preferences (accessibility, speed vs cost)

### Booking / trip flow

The transaction surface.

- step-by-step guidance through the chosen provider's flow (unlock codes, vehicle details, pickup points)
- primary actions: confirm booking, unlock, follow the trip, end it

### Tickets

The transit-ticket surface.

- fare catalog for the integrated transit network(s)
- purchased tickets held for display or validation
- primary actions: buy a fare, present a ticket

### Trips / payments

The account surface.

- trip history with prices and services used; receipts and invoices
- stored payment methods; vouchers, budgets, or prepaid balances where offered
- connected providers and their status; credential verification state
- primary actions: download an invoice, add a payment method, connect or disconnect a provider, verify a credential

### Support

- per-provider contact routes (call or message the provider actually booked)
- service-level help and reporting (parking problems, damaged vehicles, account issues)

## Important Rules / Behaviors

### Integration is real but bounded

The platform genuinely replaces per-provider registration and payment — one account, one payment method, bookings across providers. But integration has visible edges in practice: purchases are scoped to the platform in which they were made (a ticket bought in the operator's own transit app is not automatically usable in the mobility app, and vice versa), third-party subscriptions bought elsewhere do not carry over, and each app shows only what was bought in it. The promise is one relationship instead of many — not the disappearance of the providers.

### The account gates by credential, per mode

Services that involve operating a vehicle require verified credentials (typically a driving licence, often with an identity document); services that do not (transit tickets, some shared bikes) need only the account. Verification is a state on the account: it can expire or lapse, and when it does, exactly the credential-gated services lock while the rest keep working. Some operators re-verify periodically.

### Provider rules travel with the booking

Each integrated provider keeps its own operating rules — how trips are priced, when a booking can be cancelled, what condition a vehicle must be returned in, what happens with a low battery or an empty tank. The platform surfaces these rules at the point of use and routes support to the provider that fulfilled the booking. Cancellation in particular is provider-specific: some bookings can be cancelled in-app with fees shown, others can only be ended, not cancelled.

### Payment is unified but enforceable

One stored payment method serves all providers. Consequences follow: an outstanding charge can block the whole account — some services retry collection automatically before leaving it blocked — and prepaid vouchers or budgets must be selected as the payment source before booking, with any cost above their value falling back to the traveler's own payment method where such instruments are offered.

### The trip record is the platform's ledger

Every completed journey is recorded with its date, price, and services, and is receipted. This record is what the traveler disputes charges from, what the operator reports on, and what makes the platform — rather than any single provider — the traveler's financial relationship for mobility.

## Variants

- **City-authority-led service** — a transit agency or city brands and operates the service, integrating private sharing and taxi providers around its own network; commonly pay-as-you-go plus transit ticketing.
- **Subscription-bundle service** — the traveler buys a monthly mobility plan covering a set of services; usage within the plan is included. The archetype pattern for private MaaS operators.
- **Employer / corporate mobility** — the employer funds mobility budgets that employees spend through the platform; an administration console manages budgets and costs. Also covers closed employee-only apps.
- **Equity / community programs** — accessibility-first deployments for underserved populations, often with mobility wallets (subsidized travel credit) and simplified admin for small providers.
- **Platform-vendor delivery** — the same structure delivered as a white-label app, an API/SDK for integrators, or a journey-planner widget/embedded web planner for authority websites.
- **Scope shapes** — single city, region, or multi-city; urban core vs regional deployments that add demand-responsive transport.
- **Physical hubs** — some services bind the digital layer to physical stations where shared vehicles concentrate, including places where drop-off is restricted to the service's own locations.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Public Transit Passenger App | closest sibling, one-provider pole | centers one transit agency's network — planning, tickets, and service info for that network; MaaS integrates multiple providers with transit as one option among several. A transit app that adds partner booking grows into this Type |
| Ride-hailing Platform | aggregated operator | supplies drivers and operates its own fleet/dispatch; MaaS books it as one option among many |
| Car Sharing Platform | aggregated operator | operates the shared cars; MaaS is the intermediary that plans, books, and pays across such operators |
| Micromobility Sharing Platform | aggregated operator | operates the scooters/bikes; the same aggregator-vs-operator seam — MaaS apps may distribute micromobility rides |
| Taxi Dispatch Platform | aggregated operator | single-provider dispatch; taxi is one bookable service inside a MaaS platform |
| Travel Itinerary Planner / Online Travel Agency | different trip grain | centers multi-day travel commerce (flights, hotels, packages); MaaS centers urban door-to-door mobility consumed as individual trips or subscriptions |
| Corporate Travel Management Platform | employer-side adjacent | manages business travel authorization and reporting for the organization; mobility budgets fund the traveler, but the plan-book-pay loop and account remain the traveler's |
| Journey planners (planning-only tools) | upstream capability | plan without account-bound booking and payment; a planning layer of this Type, not the whole Type |

The boundary with the Public Transit Passenger App is the most important one, because the two overlap on planning and ticketing. The structural difference is whether the service centers one agency's network or the integration of multiple providers under one account.

## Representative Products

- **Jelbi** (BVG, Berlin) — city-authority-led service integrating transit tickets with car, moped, bike, scooter sharing and taxi; the clearest documented example of the register-once / connect-per-provider / book-and-pay loop
- **Trafi** — B2B white-label platform powering city services (Berlin, Brussels, Munich, Zurich, Vilnius, among others); register-once principle, intermodal routing, operator back office, mobility budgets
- **Moovit** — global planner-first consumer app with a mobility wallet and ticketing, plus a modular MaaS solutions arm for agencies and cities
- **SkedGo (TripGo)** — API-first MaaS platform; powers web planners, subscription trials, corporate apps, and equity programs across several continents

The subscription-bundle archetype (Whim, Helsinki) is widely cited as the category's founding consumer service; its official documentation could not be reached during research, so it is recorded here as a market anchor without product-specific claims.

## Sources

Research date: **2026-09-09**

- Jelbi (BVG) — official site, app page, and FAQ — https://www.jelbi.de/en/home/ , https://www.jelbi.de/en/jelbi-app-2/ , https://www.jelbi.de/en/faq/
- Trafi — official site and white-label product page — https://www.trafi.com/ , https://www.trafi.com/white-label-product
- Moovit — official site, app features, and MaaS solutions pages — https://moovit.com/ , https://moovit.com/features/ , https://moovit.com/maas-solutions/
- SkedGo — official site and MaaS definitional article — https://skedgo.com/ , https://skedgo.com/what-is-mobility-as-a-service-maas/

> Sourcing limitations: the subscription-bundle archetype's official surfaces (Whim / MaaS Global) were unreachable from the research environment (repeated transport errors), and one public-authority MaaS app (HSL HOP) returned access errors; both were abandoned after repeated failures. The subscription commercial model is therefore evidenced indirectly (through a platform vendor's deployment descriptions) and is held as a variant, not a defining structure. Precise vendor figures (provider counts, city counts, verification cycles, specific payment-provider arrangements) are kept in the Research Notes and deliberately not stated as general facts of the Type.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
