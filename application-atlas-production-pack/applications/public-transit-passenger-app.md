# Public Transit Passenger App

## Overview

A **Public Transit Passenger App** is the rider-facing companion to a scheduled public transport network: an application whose world is the network's lines, stops, and timetables, and whose central act is planning a journey on that network — then following it, and commonly paying for it, from the same surface.

The defining structure is small:

```text
The rider (a passenger of the service)
└── the scheduled transit network (lines/routes + stops + timetables)
    └── the journey (origin → destination itinerary)
        ├── planned: options compared, one chosen
        ├── followed: guidance and live information through execution
        └── paid: ticket or fare, where the product carries fares
```

Everything else the market associates with these apps — real-time vehicle positions, disruption alerts, step-by-step navigation, in-app tickets, favorites, crowdsourced data, multi-modal extras — is standard capability that mature products carry, not what makes the product a transit passenger app. A schedule-only journey planner and an info-only agency app both satisfy the core; a product that loses the network reference or the journey becomes something else (a general map, a stop-departure utility, an operator tool).

## Users & Context

The user is a **transit rider** — a commuter who rides the same lines daily, an occasional rider heading somewhere unfamiliar, a visitor in a new city. What they share is the situation: standing outside the system with a origin, a destination, and a need to know how the network gets them there, when it comes, and what it costs.

The *publisher* of the app varies, and this shapes the content:

- **The agency or authority itself** publishes official apps centered on its own network, often joined to its fare system.
- **Independent companies** publish multi-city apps that aggregate many networks for information, with fares added city by city through partnerships.
- **Platform vendors** supply white-label or co-branded versions of the same surface, operated under an agency's brand.

The usage context is overwhelmingly mobile and on the move: at home before departure, at the stop, on the vehicle. Web planners and watch/lock-screen companions exist as secondary surfaces.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as a transit passenger app:

- **Rider-facing orientation** — the user is a passenger *using* the service, not the operator *running* it. The app's job is to get one person through their day on transit. Without this, the product is operator-side territory (the operations platform that plans and controls the service) or a generic tool.
- **The scheduled transit network as the reference frame** — the app's world is the scheduled public transport service of the network or networks it covers: lines/routes, stops and stations, timetables. Real-time information only means something against this frame. Without it, the product is a general navigation or travel-planning tool in which transit happens to be one option.
- **Journey planning as the central act** — the rider states an origin and a destination; the app assembles itineraries from the network's scheduled services, with times, transfers, modes, and commonly fares. The journey is the unit of work around which everything else is organized. Without it, the product is a stop-departure board — useful, but not a journey app.

### Standard Capabilities Around the Core

Mature products commonly carry most of the following. They make the app practical; they do not define the Type.

- **The real-time layer over the schedule** — live departure times distinguished visibly from posted schedule times; live vehicle positions on the map; skipped/cancelled trip states; service alerts and disruption notices, both network-wide and subscribed per line; detour/diversion handling with temporary stops; crowding information where available.
- **Riding guidance** — step-by-step direction through the chosen itinerary, with notifications for when to leave, when to change lines, and when to get off; live re-timing of the journey as conditions change.
- **The personal layer** — favorite lines, stops, and locations; pinned lines with alert subscriptions; saved or recent trips; sometimes calendar integration so planned events become trips.
- **Fare payment and ticketing** — in-app purchase of the agency's fares, a ticket wallet, activation shortly before boarding, and display or scan for inspection; fare capping that upgrades accumulated single purchases to pass equivalents; stored value and card top-up; contactless payment options. Present in most mature products, but explicitly gated to "select cities" in the independent multi-city planners; standard in agency apps.
- **Accessibility support** — screen-reader support, accessible-route options in the planner, accessibility notifications.
- **Multi-modal extension** — bikeshare, scooters, ride-hail (and walking/cycling/driving comparisons) offered as options beside the transit network in planning.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:  The network reference
Realizations:  one agency's own network (official apps) ·
               many networks aggregated for information (independent multi-city apps)

Concept:  Real-time information
Realizations:  agency feeds consumed by the app · crowdsourced from riders on board ·
               schedule-only fallback where no feed exists

Concept:  Fare payment
Realizations:  in-app tickets with activation and display · stored value / smart-card top-up ·
               contactless account management · none (info-only apps)

Concept:  Publisher posture
Realizations:  official agency app · independent consumer app ·
               white-label platform operated under an agency's brand
```

A reader who has only met one implementation — say, an official metro app with QR tickets — should still be able to recognize an independent planner with no ticketing at all as the same Type.

## How It Works

### Orient

```text
Open the app
→ map shows the rider's location with nearby lines and their next departures
→ real-time departures are marked as live; the rest show the posted schedule
→ tap a line for later departures, the nearest stop, and the vehicle's position
```

The home surface answers "what's coming near me right now" before any search.

### Plan

```text
Enter a destination (typed, map point, favorite, or a calendar event)
→ compare itinerary options across the network's services and other modes
→ constrain by time if needed (leave now / leave at / arrive by)
→ choose an itinerary; inspect its legs, times, and fare where shown
```

Planning is where the network reference becomes concrete: the itinerary is assembled from the lines, stops, and timetables the app holds.

### Ride

```text
Start guidance on the chosen itinerary
→ notifications: when to leave, when to change lines, when to get off
→ live vehicle positions and re-timed arrivals en route
→ disruption alerts surface if the line changes under the rider
```

### Pay (where the product carries fares)

```text
Choose the fare → purchase against an account or wallet
→ activate shortly before boarding (activation is a deliberate act, not automatic)
→ display the activated ticket or scan its code for inspection
→ repeated single purchases may cap into pass equivalents automatically
```

### Maintain

```text
Pin frequently used lines (subscribing to their alerts)
→ save favorite stops and locations
→ set preferences (modes shown, accessibility needs, notifications)
→ optionally: report corrections or rate the ride, feeding data back to the network
```

The defining loop is the middle trio: **plan → ride → (pay)**. The orient and maintain loops are the standard machinery that makes daily use practical.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Nearby / home screen

The rider's entry surface.

- map with the rider's location, nearby lines, next departures with live/scheduled distinction
- primary actions: open a line's departures, start planning, access tickets and settings

### Trip planner

- destination input (typed, map, favorites, calendar), option comparison across modes and times, itinerary detail with legs and transfers
- primary actions: compare options, set leave-now/leave-at/arrive-by, choose an itinerary, start guidance

### Journey / guidance surface

- step-by-step progress through the itinerary, next-action notifications, live vehicle positions
- primary actions: follow the journey, dismiss or act on alerts, end guidance

### Line / stop detail

- the departures board for a line or stop: upcoming trips with live/scheduled/skipped/cancelled states, vehicle positions, crowding where available, active alerts and detours
- primary actions: track a departure, pin the line, report a problem

### Tickets / wallet

- the rider's fare surface: available fare products, purchase flow, wallet of owned tickets, activation, display/scan for inspection, payment methods, capping status
- primary actions: buy, activate, show, top up, redeem codes

### Personal / settings

- favorites, pinned lines, notification and accessibility preferences, account management

## Important Rules / Behaviors

### Real-time is a layer over the schedule, not a substitute

Departure information is explicitly marked as live or as posted schedule. When a network has no real-time feed, the app still works — it shows the timetable, and in some products riders on board fill the gap by sharing their vehicle's location. The schedule is the invariant frame; live data improves it.

### The app consumes; it does not operate

The rider-facing app does not run the service. Cancellations, diversions, and alerts originate with the agency and flow to the app through feeds; the app's own contributions are rider-side (crowdsourced positions, corrections, ratings). This is the structural seam with the operator-side operations platform, which produces exactly what this app consumes.

### Ticket activation is a deliberate act

Where fares are carried, a purchased ticket is not automatically valid: the rider activates it shortly before boarding, and the activated ticket is displayed or scanned for inspection. Activation may require connectivity. Tickets are typically bound to the app's own wallet and do not transfer between apps.

### Alerts are subscription-shaped

Network-wide disruptions reach everyone; line-specific alerts reach riders who pinned that line. The personal layer doubles as a notification-routing surface.

### The network frame bounds planning

Modes the rider disables drop out of both the nearby list and the trip planner; detours and stop closures are folded into planned itineraries. What the app holds about the network determines what it can plan.

### Fare rules belong to the agency

Fare products, capping thresholds, and validation rules are the network's, surfaced in the app. The app is the channel, not the fare authority.

## Variants

- **Official agency app** — one network, often joined to the agency's fare system; planning + real-time + the agency's own fare media (e.g. BVG Fahrinfo, Transport for NSW's Opal Travel).
- **Independent multi-city app** — many networks aggregated for information; fares added per city through partnerships, explicitly "in select cities" (e.g. Citymapper, Moovit, Transit).
- **White-label / co-branded platform** — the same rider surface operated under an agency's brand, supplied by a platform vendor (e.g. Umo-powered agency apps, Moovit's branded apps, Transit's agency partnerships).
- **Ticketing depth** — info-only (no fares in-app) → select-city partnership tickets → full fare media catalog with stored value, capping, and contactless account management.
- **Regional fare regimes** — QR-code validation, reloadable smart cards, account-based capping, card top-up — jurisdiction-dependent machinery around the same fare leg.
- **Crowdsourcing and feedback** — rider-shared vehicle locations, community data corrections, ride ratings and agency surveys; present in some products, absent in others.
- **Premium subscription** — paid tiers for the consumer app (extra features, ad-free posture); in at least one researched product, agencies can fund subscriptions for their riders.
- **Form factor** — native app dominant; web planners, watch and lock-screen companions as secondary surfaces.

A variant remains a variant while the defining core holds. When the center shifts — from the transit network to transactional integration of many providers under one account — the product has grown into a different Type (Mobility-as-a-Service).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Mobility-as-a-Service Platform | closest seam, ratified sibling | MaaS centers transactional integration of **multiple providers under one account** (plan → book → pay across operators); the transit passenger app centers the **scheduled transit network**, with per-agency fares. Remove the multi-provider booking/account layer from MaaS → a transit passenger app; add partner booking under one account → it grows into MaaS. Some authorities ship both side by side as separate apps. |
| Public Transit Operations Platform | operator-side counterpart | the ops platform *produces* the plan and the real-time data; the passenger app *consumes* them. Remove the rider surface → ops platform; remove the operator side → passenger app. |
| Rail Booking & Ticketing | adjacent commerce | long-distance rail products (intercity tickets, seat reservations, journey-priced sales) vs urban/regional scheduled transit usage with network fare media. Transit apps sometimes broker long-distance tickets, but the center stays the network. |
| Ride-hailing / Micromobility Sharing / Car Sharing | on-demand siblings | those supply or operate vehicles on demand; transit is scheduled shared capacity where the passenger never operates the vehicle. They appear inside transit apps as planning options, not as the center. |
| Parking Application | adjacent detail | parking appears as a mode/destination detail inside planning; never the center. |
| Employee Transportation Platform | adjacent program | an organization's own commissioned commuter network vs the open public network and its public fares. |
| General mapping / navigation products (no dedicated leaf) | different center | a general map with a transit mode filter centers places and driving; transit is one option. Here the transit network *is* the center. A dedicated transit journey planner (plan-only, web or app) is the thin pole of this Type. |

The most important boundary is the MaaS seam, because the two Types overlap on planning and ticketing. The structural test: whose transaction is it? Per-agency fares on a network center stay here; multi-provider booking under one account is MaaS.

## Representative Products

- **Citymapper** — independent multi-city planner (now part of Via); consumer app plus "Citymapper for Cities" co-branded/white-label offering for agencies.
- **Moovit** — independent planner with wallet/tickets "in select cities", crowdsourced data editing, and a branded-apps (white-label) arm for agencies and cities.
- **Transit** — independent planner with deep real-time machinery (GO crowdsourcing, departure states, detour detection), agency ticketing partnerships, and an official-app platform for 220+ agency partners.
- **Umo (Cubic Transportation Systems)** — fare-vendor passenger app platform: trip planning + real-time + mobile ticketing/contactless payments, white-labeled for agencies across participating systems.
- **BVG Fahrinfo** — official app of Berlin's transit authority: network planning, live timetable/navigation, and the authority's full fare media catalog.
- **Transport for NSW apps (Opal Travel, Trip Planner)** — official authority apps combining journey planning, real-time service information, and fare-account management.

The definition was checked against the info-only and schedule-only generations (planner-first web services, agency apps without in-app fares) so that the core does not over-fit today's real-time + mobile-ticketing packaging.

## Sources

Research date: **2026-09-09**

- Citymapper — https://citymapper.com/ ; https://citymapper.com/i/2809/making-bus-rides-better ; Via, "Citymapper for Cities" — https://ridewithvia.com/solutions/citymapper
- Moovit — app features: https://moovit.com/features/ ; branded apps: https://moovit.com/maas-solutions/branded-apps/
- Transit — https://transit.app/ ; help center articles: how to use Transit, plan a trip, what is GO crowdsourcing, track departures, buy tickets, fare capping, manage transit options (https://help.transitapp.com/)
- Umo (Cubic) — https://umomobility.com/ ; https://umomobility.com/riders/ ; https://umomobility.com/transit-agencies/umo-app/
- BVG — Fahrinfo app: https://www.bvg.de/en/subscriptions-and-tickets/all-apps/fahrinfo-app
- Transport for NSW — transport apps: https://transportnsw.info/apps

> Sourcing limitation: the official app pages of Transport for London (tfl.gov.uk) and the New York MTA (new.mta.info) were not reachable from the research environment (HTTP 403) and are not used as evidence; the info-only official-app pole is evidenced indirectly (schedule-only operation documented within Transit's own help center; Transport for NSW's planning-only Trip Planner app). Moovit's "Long Distance Tickets" page and one Umo page returned 404; those points are held at label strength. Precise operational details beyond what the fetched pages document (exact activation rules per product, offline behavior, numeric limits) are intentionally not stated. Detailed product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
