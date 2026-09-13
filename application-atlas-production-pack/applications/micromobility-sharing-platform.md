# Micromobility Sharing Platform

## Overview

A **Micromobility Sharing Platform** is a mobility application that gives riders self-service access to a shared fleet of small electric vehicles — e-scooters and e-bikes — for short urban trips, billed per use.

The defining structure is a single loop:

```text
Registered rider
  → finds an available vehicle on the map
  → unlocks it self-service (scan / code / phone / key)
  → rides it personally through the city service area
  → releases it at a defined place and state
  → trip closes with usage-based charging
  → vehicle returns to the pool for the next rider
```

Everything else commonly associated with the category — geofenced speed zones, parking photos, per-minute rounding, subscriptions, swappable batteries, dockless operation — is a widespread implementation of the current market, not part of the definition. Dock-based station systems with physical keys and kiosks, hub-based bike networks, and app-unlocked free-floating scooters all satisfy the same loop.

When the shared vehicles are cars, the product is a Car Sharing Platform. When a driver is supplied, it is ride-hailing. When access requires a staffed counter and per-day pricing, it has drifted into vehicle rental.

## Users & Context

**Riders** are the primary users: urban residents, commuters, and visitors making short point-to-point trips — the first/last mile of a commute, an errand, a crossing the transit network doesn't serve well. They interact with the platform to find vehicles, unlock and ride them, release them correctly, and pay for use.

**Fleet-operations teams** work behind the rider surface: charging and battery swapping, rebalancing vehicles across the city, maintenance, and retrieval of broken or mis-parked vehicles. Their work is what keeps the map's promise — an available, rideable vehicle nearby — true.

**Cities and universities** are a third party in every ride: they permit operations, set parking and riding rules, and charge compliance fees that appear in the ride price.

**Businesses and institutions** are a secondary audience: companies buy memberships for employees; campuses and cities sponsor programs.

The usage context is overwhelmingly mobile and outdoor: the rider's phone is simultaneously the key, the map, the meter, and the rulebook.

## Core Model

### The Defining Core

Four structures. Remove any one and the product stops being a micromobility sharing platform:

- **Shared micromobility fleet** — a pool of small electric vehicles owned and operated by the service, circulating among many riders in short successive turns. No rider owns the vehicle they ride. This is what "sharing" means structurally.
- **Rider account as the access gate** — a registered account binding identity and payment. The gate is deliberately lighter than car sharing's: none of the products researched requires a driver's license to ride a bike or scooter, and where regulation demands it, age verification is performed at signup or first ride.
- **Self-service locate-unlock-ride loop** — the rider finds an available vehicle, unlocks it without staffed assistance, and operates it personally for one trip. No handover, no driver, no guide.
- **Release-and-close act** — the rider ends the trip at a defined place and state (a dock, a hub or drop-off, a parking pin, an approved location) so the vehicle becomes available to the next rider, and the trip closes with usage-based charging — per-minute, per-ride, or included in a plan.

The four are jointly load-bearing:

```text
Fleet alone                          → a vehicle catalog
Account without fleet                → a payment account with nothing to ride
Unlock without fleet + account       → borrowing a friend's bike
Release without self-service access  → drop boxes
Loop without release                 → abandonment; the fleet depletes
Fleet + loop without accounts        → unregistered public infrastructure
```

### What Riders Work With

- **Vehicle** — the central resource: individually identified (QR code, plate or frame number), positioned on the map, and described by type and availability state (commonly including battery level — a depleted vehicle is not a ride).
- **Service area and zones** — the geography of rules. A service zone bounds where riding is offered at all; inside it, shaded zones restrict where vehicles may travel, how fast they may go, and where they may be released.
- **Trip** — the unit of service and billing. It opens when the vehicle unlocks and closes when the release is confirmed. Everything monetary attaches to it: the unlock charge, the time-based rate, city fees, penalties.
- **Release targets** — parking pins, mandatory parking areas, station docks, or hub drop-offs, depending on the product's release geography.
- **Pricing plan** — how use converts to money: pay-per-ride, prepaid passes, recurring subscriptions or memberships, plan-included rides.

### One Loop, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:            Release geography
Implementations:    free-floating zone (leave anywhere legal in the zone)
                    station dock (physical docking hardware)
                    hub / drop-off network (designated spots shown in the app)

Concept:            Unlock credential
Implementations:    QR scan, manual code entry, phone-as-key,
                    physical key, kiosk ride code

Concept:            Charging model
Implementations:    unlock fee + per-minute rate, flat per-ride price,
                    passes and subscriptions, membership-included rides
```

A reader who has only seen dockless sidewalk scooters should still recognize a station-dock bike system as the same Type from the core model.

## How It Works

### Join (once)

```text
Download the app
→ sign up with identity + payment method
→ (some cities) verify age with a government ID
→ account ready to ride
```

Verification depth varies by city and vehicle class; the common pattern is a light gate — account plus payment — rather than credential review.

### Find a vehicle

```text
Open the map
→ see nearby vehicles with availability state (commonly battery level)
→ see the zones that will govern the ride
→ optionally hold a vehicle briefly before walking to it
```

The map is the platform's primary surface: it shows supply, and it shows the rules as geography.

### Unlock and ride

```text
Scan the vehicle's QR code (or enter a manual code)
→ vehicle unlocks; trip opens
→ ride through the service area
   (no-go zones stop the vehicle; low-speed zones slow it)
→ optionally pause the ride mid-trip, keeping the vehicle held
```

Unlocking is the moment the platform's control is most visible: the trip starts only when the app says so, and the vehicle is dead to everyone else while it is held.

### Release and close

```text
Ride to an approved release point
   (parking pin / dock / drop-off / anywhere legal in the zone)
→ end the ride in the app
→ confirm the release the product requires
   (photo of the parked vehicle, dock confirmation, physical lock)
→ billing settles: unlock + time + city fees + any penalties
```

Releasing correctly is a real skill the platform teaches: leaving the vehicle is not ending the trip. Charges continue until the app confirms the end; mis-parked vehicles can draw warnings or penalties; docks confirm with a light before the trip is considered closed.

### When things go wrong

The failure modes are a stable part of the Type, and mature products document each:

- **Can't start** — unreadable code (manual-code fallback), vehicle error (take another vehicle; the broken one gets retrieved), payment error (update the payment method).
- **Can't end** — GPS drift (move closer to the pin), poor connection, expired card. The ride keeps billing until it is properly closed.
- **Broken vehicle mid-ride** — report it; support and retrieval follow.
- **Overcharge or unrecognized charge** — refund machinery.
- **Accident** — a documented reporting process, with insurance coverage included in some markets.

### The operator side

Behind the rider surface sits the fleet operation that makes the loop sustainable: charging and battery swapping, rebalancing vehicles to where demand is, maintenance turnover, retrieval of broken or mis-parked vehicles, and compliance with each city's operating rules. Some operators run this in-house as a brand pillar; others contract it. The rider never sees it directly — only its results: vehicles where the map says they are, charged, and rideable.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Map

The primary discovery surface.

- shows vehicles with real-time availability, commonly with battery level
- shows the service area and its zones (no-ride, slow, parking-restricted)
- shows release targets: parking pins, stations, drop-offs
- primary actions: select a vehicle, hold it, navigate to it

### Ride screen

The rider's control panel while a trip is open.

- vehicle identity, elapsed time, ride state
- primary actions: pause, report a problem, end ride

### Release confirmation

The gate that closes the trip.

- pin proximity check, guided photo of the parked vehicle, or dock/hub confirmation
- local parking rules surfaced at the moment of release

### Pricing and payment

- the rate for the location shown before the ride (tap the vehicle or scan its code)
- itemized city fees where they apply
- passes, subscriptions, and memberships with their terms
- receipts and trip history

### Support

- trouble starting/ending, vehicle issues, overcharge and refunds, accident reporting
- safety guidance and local riding rules

### Account

- payment methods, ride history, subscriptions, privacy and data controls

## Important Rules / Behaviors

### Release discipline holds the Type together

The entire service rests on vehicles coming back correctly. Every product defines where a vehicle may be left and in what state (upright, out of walkways, at a pin/dock/drop-off), and every product bills violations — parking warnings, penalties, fines. A mis-released vehicle is lost supply and a city complaint at once.

### Ending a trip is an explicit, confirmed act

Walking away is not ending. The trip closes only when the app confirms — after a photo, a dock light, or a successful end-ride call. Charges continue until then, and products warn about this explicitly because a forgotten open trip either bills the rider indefinitely or strands the vehicle.

### Zones govern the ride as geography

Rules are encoded on the map, not just in text: no-go zones bring the vehicle to a stop (the rider walks it out), low-speed zones cap its speed, no-parking zones refuse release, mandatory-parking zones require release at pins, and the service-zone boundary ends ridability. The vehicle itself enforces what the map shows.

### The gate is light but real

An account with payment is required; age verification applies where regulation requires it; none of the products researched requires a driver's license for bikes or scooters. This lightness — versus car sharing's license verification — is structural: it is what makes spontaneous minute-scale urban trips possible.

### The city is a third party in every ride

Operating permits, per-city parking and riding rules, compliance fees itemized in the ride price, insurance regimes, and parking-fine enforcement all come from the regulator. The same product behaves differently from city to city, and mature products surface the local rules in the app at the moment they matter.

### Battery state is part of availability

A vehicle's charge level is commonly displayed with its availability; a depleted vehicle is not supply. Fleet charging — swap or plug-in — is the operator's answer, invisible to the rider except as it keeps the map honest.

## Variants

- **Dockless free-floating** — vehicles circulate in a service zone; riders release them anywhere legal in the zone, guided by pins and zones. The dominant scooter pattern.
- **Dock-based station systems** — vehicles live in station docks; riders unlock by app, key, or kiosk code and return to any station with an open dock. The founding bike-share pattern, still operating at scale.
- **Hub / drop-off networks** — a middle shape: no docks, but release only at designated spots shown in the app.
- **Hybrid** — one product mixes shapes (e.g., free-floating with parking-station hardware, or docks plus app-based overflow parking when docks fill).
- **Vehicle mix** — standing scooters, seated scooters, e-bikes, and classic pedal bikes; some operators run several in one app.
- **Pricing posture** — pay-per-ride, day/week/month passes, recurring subscriptions, multi-city memberships, company memberships.
- **Regional regulatory shapes** — permit regimes, fee structures, insurance coverage, and parking enforcement vary substantially by city and country; the same product behaves differently across its markets.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Car Sharing Platform | closest sibling, same loop | same find-unlock-ride-release loop and per-use billing; the seam is vehicle class (small two-wheelers vs cars), the eligibility gate (no driver's license vs verified license), and trip scale (minutes vs hours/days) |
| Ride-hailing Platform | clean separation | ride-hailing supplies a driver; the passenger never operates the vehicle. Micromobility supplies the vehicle; the rider is always the operator |
| Vehicle Rental Platform | adjacent | rental centers on staffed-counter handover, per-day pricing, and multi-day durations; micromobility is self-service, per-minute/per-ride, short successive turns |
| Public Transit Passenger App | adjacent in the journey | transit is scheduled shared capacity operated by an authority; the passenger never operates the vehicle. Micromobility is on-demand and self-operated |
| Fleet Management System | supporting layer | fleet management is operator-side administration (maintenance, telematics, compliance); micromobility's defining surface is rider-facing access. The operator side exists here, but as support |
| Parking Application | feature overlap only | parking rules and pins live inside the ride loop, but finding and paying for parking is not what the platform is for |
| Mobility-as-a-Service Platform | aggregator vs operator | MaaS plans and books trips across providers; a micromobility platform operates the fleet being consumed. MaaS apps may distribute micromobility rides |

## Representative Products

- **Lime** — global operator; scooters and e-bikes; zone machinery and parking pins; the sample's richest rider-rule documentation
- **Bird** (with Spin) — US pioneer; scooters and e-bikes; city-priced rides with compliance fees
- **Dott** (TIER, merged 2024) — European operator; bikes and scooters; in-house fleet operations; passes and included insurance in eligible markets
- **Veo** — US city-partnership operator; standing and seated scooters and bikes
- **Donkey Republic** — bike-only hub/drop-off model with multi-city memberships; the different-philosophy pole

The defining core was checked against the dock-based station-system pattern (Citi Bike: docks, keys, kiosk codes, any-station return) to avoid defining the Type by the current dockless-scooter implementation.

## Sources

Research date: **2026-09-09**

- Lime Help Center — Starting your ride; Ending your ride; Riding and parking zones; Ride costs and rates; Age verification — https://help.li.me/hc/en-us
- Bird & Spin Support Center — Starting/ending your ride and parking your vehicle; Cost to ride; Getting Started category — https://help.bird.co/hc/en-us
- Dott official site — Ride with us; company pages — https://ridedott.com/ , https://ridedott.com/ride-with-us/
- Veo official site — How it works; Rider Guide — https://www.veoride.com/ , https://www.veoride.com/rider-guide-how-to-ride/
- Donkey Republic official site — How to rent a bike; memberships; cities — https://donkey.bike/
- Citi Bike Help — How to start a ride; How to dock a bike; Taking a ride category — https://help.citibikenyc.com/hc/en-us

> Sourcing limitations: the Lime marketing site was not reachable (403); Lime evidence rests on its help center. One Bird zones article was not retrievable; zone mechanics are documented through Lime's help center plus Bird's and Dott's zone mentions. The Dott help center is app-rendered and could not be read; Dott observations rest on its official product pages. A general encyclopedia article on bicycle-sharing history timed out; the pre-scooter dockless generation is treated as context only, without specific claims. Precise vendor figures (hold durations, code lengths, prices, city counts, battery ranges) are kept in the Research Notes and deliberately not stated as general facts of the Type.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
