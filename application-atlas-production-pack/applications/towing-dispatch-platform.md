# Towing Dispatch Platform

## Overview

A **Towing Dispatch Platform** is the operator-side system a towing and vehicle-recovery business runs its operation on. Calls to recover, move, or service a specific vehicle — from police rotation programs, motor clubs and insurers, private-property accounts, direct payers, and commercial transport customers — enter the system; the company's tow trucks and drivers are held as a live, capability-matched fleet; each call is allocated to a specific truck-and-driver; the job is tracked through arrival, hook-up, and transport to its destination; and the completed job closes into the company's commercial record — the invoice to whoever stands behind the call, the driver's commission, and, where the vehicle stays, its life in the storage lot.

The defining core is deliberately small:

```text
Vehicle-recovery call (vehicle + incident location + service + destination + call source)
  ↓ allocated against
Live availability of the capability-matched tow fleet (trucks by class/equipment + drivers)
  ↓ tracked through
Job lifecycle → destination / disposition → billing against the call source + driver commission
```

Everything else commonly associated with modern towing technology — GPS tracking, driver apps, digital motor-club feeds, embedded payments, lien automation, auctions — is widespread in current products but is not what makes the system a towing dispatch platform. Phone-and-paper dispatch offices working a rotation list by telephone, radio-dispatched fleets, and 1990s electronic job-transfer links all satisfied the same core; today's products are that operation carried into software.

The boundary that matters most: this is the **tow operator's own** system. The assistance organizations, breakdown clubs, and agencies that send work are upstream principals, not the operator of this system — their dispatches arrive here as inbound calls. When the software's job is to mediate a stranded motorist's incident across a contracted network of providers, with coverage rules deciding who pays, that is a roadside assistance platform instead.

## Users & Context

Primary users, all on the tow company's side:

- **Dispatchers / controllers** — the operational heart. They take calls, watch the live board and map, and bind each call to a truck-and-driver — by hand or with system assistance — then shepherd jobs through arrival, hook-up, and drop-off, handling refusals, delays, and changes along the way. In the UK recovery tradition this role sits in a "control room"; in the US, in the towing company's dispatch office.
- **Tow truck operators / drivers** — receive assigned calls, progress their status from the road, document the vehicle before moving it, collect payment or signature where the call requires it, and deliver the vehicle to its destination or the company's lot.
- **Owners / managers** — configure rates and call types, manage truck and driver records, watch response times and revenue, and run billing, commissions, and compliance.

Secondary participants:

- **Call sources** — the parties whose work arrives as calls: police and transportation authorities (rotation and incident tows), motor clubs and insurers (member and policyholder tows), private-property accounts (parking enforcement), vehicle owners and businesses (direct calls), and commercial accounts (dealer, auction, and equipment transports). They do not operate the system; their identity on the call determines authorization and payment.
- **Lot / impound staff** — receive stored vehicles, track inventory and fees, process releases, and prepare lien and auction paperwork.
- **Motorists** — the drivers of towed or serviced vehicles; they may receive arrival updates and tracking links, pay at the scene or on release, and search for a towed vehicle where the jurisdiction provides it.

The work context is continuous, unscheduled, and time-pressured: calls arrive around the clock, response-time commitments (a motor club's ETA promise, a rotation program's response rule) are contractual, and every job moves someone else's property — which makes documentation and custody discipline part of daily operations. The system is the business's system of record: the calls, the fleet's availability, the money, and the compliance trail all live here.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and the product stops being a towing dispatch platform:

**1. The vehicle-recovery call.** The unit of work is a call: a request to recover, move, or service one specific vehicle. A call carries the vehicle's identity (make, model, plate or VIN), the incident or pickup location, what is needed (a tow — light, medium, or heavy duty — or a light service such as a jump-start or tire change), the destination (repair shop, storage lot, dealer, residence — where the vehicle is to be taken), and the **call source**: who requested the tow and under what authority. The call source is structural, not a note on the record — it determines who authorized the tow and which payment path the completed job will follow. Calls may be immediate or scheduled, single- or multi-vehicle, point-to-point or multi-destination.

**2. The capability-matched tow fleet.** Trucks and drivers are held as the supply. Each truck carries its duty class and equipment type — flatbed/rollback, wheel-lift/wrecker, heavy-duty underlift, rotator — because the call's requirements must match the truck's capability: a wheel-lift call needs a wheel-lift truck, a commercial-vehicle recovery needs heavy equipment. Each driver carries identity, certifications, and an availability state (on shift or on patrol, committed to a job, off). Availability is the fleet's state of record: assignment consumes it, completion restores it.

**3. The allocation act.** An incoming call starts unassigned. The central managed transition is binding it to a specific truck-and-driver — by a dispatcher's hand, by system recommendation (nearest truck, best match), or automatically under configured rules. For authority work the rule is often a **rotation**: contracted companies are called in list order, and serving a call sends a company to the bottom of the list. For response-time work the rule is proximity and ETA. The act is visible on the live board and reversible (calls can be reassigned).

**4. The tracked lifecycle closing into the commercial record.** Every call is tracked from receipt through allocation and performance — en route, on scene, hook-up, transport — to a terminal state: completed at its destination (with the vehicle's disposition recorded), cancelled, or refused. Completion produces the commercial record: charges under the applicable basis, billed to the party behind the call source — the motor club invoiced directly at its contracted rates, the authority under its program's fee schedule, the private payer at the scene or on release, the account on statement — plus the driver's commission. The call history is the company's business record.

```text
Call (vehicle, location, service, destination, source)
  → unassigned queue
  → ALLOCATION (manual / assisted / automatic; rotation order or proximity)
  → truck-and-driver bound
  → en route → on scene → hook-up → transport
  → destination reached; vehicle disposition recorded
  → billed against the call source; driver commission recorded
terminal exceptions: cancelled / refused / uncovered
```

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Call intake
Realizations:  phone and radio, digital feeds from motor clubs and work providers,
               web request forms, agency/CAD-generated tow requests,
               driver-initiated patrol pickups

Concept:  Call source / authorization
Realizations:  police rotation program, motor club or insurer contract,
               private-property account, direct private pay, commercial transport account

Concept:  Capability matching
Realizations:  duty-class divisions (light / medium / heavy), equipment attributes
               (flatbed, wheel-lift, rotator), vehicle-identity lookup to pick the right truck

Concept:  Allocation rule
Realizations:  dispatcher assignment, nearest-truck / fastest-ETA, rotation list order,
               automatic assignment under configured rules

Concept:  Commercial record
Realizations:  motor-club direct billing and payment import, authority fee schedules,
               at-scene or on-release payment, account invoicing, driver commissions
```

A reader who has only seen one implementation — say, an app-centric motor-club operation — should still be able to recognize a phone-and-rotation-list dispatch office, or a UK control room receiving breakdown-club jobs electronically, as the same Type from this core.

### Standard Capabilities of Mature Products

These are common in current products and expected by the market, but they are additions to the core, not the definition:

- **Digital call intake** — motor-club, insurer, and work-provider jobs arrive as electronic dispatches straight into the call queue, with no manual re-entry; web request forms and quotes for direct customers.
- **GPS and truck tracking** — real-time positions from the driver app or integrated telematics providers, feeding proximity suggestions, ETAs, and the live map.
- **Driver app** — call acceptance, status progression, navigation context, geocoded photos, signatures, payment capture, receipts.
- **Damage documentation** — time-stamped photos, condition reports, and walkaround video recorded **before the vehicle is moved**, protecting the company against damage claims on someone else's property.
- **Impound / storage lot management** — vehicle inventory with aging, storage-fee calculation, release handling, and lot-search for staff and (in some jurisdictions) vehicle owners.
- **Lien processing and notification** — identification of owners and lienholders, state-compliant notification letters, deadline tracking.
- **Auction / disposal machinery** — moving unclaimed vehicles to auction or sale.
- **Motor-club direct billing** — invoicing clubs at contracted rates, importing their payment files, and reconciling accounts; accounting-package integration.
- **Commissions and payroll** — per-driver commission calculation and payout reporting.
- **Compliance records** — driver licences and certifications, truck inspections, insurance, with expiry reminders.
- **Motorist communication** — SMS stage updates, live tracking links, and location-share links so the stranded driver can watch the truck approach.
- **Vehicle identity lookup** — plate/VIN decode to populate call details and match equipment.
- **Reporting** — response times against ETAs and service targets, call volumes by source, revenue by account, truck and driver productivity.

## How It Works

### The dispatch loop

The daily operation is a continuous loop over a stream of calls:

```text
1. CAPTURE    A call arrives — by phone, by digital feed from a motor club or
              work provider, by web request, or as a tow request generated from
              an agency's dispatch system. The system records the vehicle, the
              incident location, the service needed, the destination, and the
              call source; duplicate and account rules are applied.

2. QUEUE      The call enters the unassigned queue, visible on the dispatch
              board with its location, priority, and requirement flags
              (duty class, equipment, light service).

3. ALLOCATE   The call is bound to a truck-and-driver:
              - manually, by a dispatcher reading the board and map;
              - by recommendation, with the system proposing the nearest
                or best-matched truck;
              - automatically, under configured rules — rotation order for
                authority work, proximity/ETA for response-time work.
              The driver receives the call on the driver app.

4. PERFORM    The driver progresses the job: en route, on scene, hook-up,
              transport. Before moving the vehicle the driver documents its
              condition (photos, condition report); position updates flow to
              the live map; the motorist may watch the truck approach.

5. DISPOSITION  The vehicle reaches its destination — a repair shop, a dealer,
              a residence — or the company's lot. Where it enters storage it
              becomes lot inventory: fees accrue, release is processed, and
              unclaimed vehicles move through lien notification to auction.

6. CLOSE      The job completes: charges are computed under the applicable
              basis and billed to the party behind the call source — the club
              invoiced directly, the authority under its fee schedule, the
              private payer captured at the scene or on release — and the
              driver's commission is recorded. The call becomes part of the
              company's history and reporting.
```

Steps 1–4 run continuously and concurrently across dozens of calls; the dispatch board is the shared working surface where the whole operation is visible at once.

### The availability loop

Allocation is only as good as the availability picture behind it:

```text
Driver starts a shift (check-in, often with an equipment inspection)
  → truck associated
  → driver posted available (on patrol or on the board)
  → allocation assigns a call; availability changes
  → call performed; driver returns to available (or ends shift)
```

Duty-class and equipment attributes gate the match: a heavy-duty call is allocated only to heavy-capable trucks, and a company that cannot respond within its rotation program's time rule forfeits its turn. Where fleets run divisions — light towing, heavy towing, roadside service — the division is the first filter on both calls and trucks.

### The disposition arc

What distinguishes towing's lifecycle from most dispatch work is that the towed vehicle often stays with the operator after the drive:

```text
Vehicle stored at the lot
  → inventory record with arrival time and condition
  → storage fees accrue while the vehicle is held
  → release: owner or insurer claims the vehicle; charges collected
  → or unclaimed: statutory notifications to owner and lienholders
  → lien perfected; vehicle auctioned or disposed; proceeds applied
```

The lot is run from the same system as the dispatch board — the vehicle's job history, its photographs, and its charges are one record from call to disposition.

### Exceptions that shape the design

- **Refused or forfeited calls** — a company that cannot respond in time loses its rotation turn; the call passes to the next capable operator.
- **No truck available** — the call waits, escalates, or (for club work) risks the service-level commitment; dispatchers rebalance patrols and hold calls against incoming supply.
- **Mid-job escalation** — a light-service call that cannot fix the vehicle becomes a tow; the call record follows the escalation and its pricing changes.
- **Damage claims** — the vehicle is damaged during hook-up or transport; the pre-move condition report and photographs are the company's defense.
- **Cancelled calls** — by the motorist, the club, or the officer before arrival; recorded, with cancellation fee rules where they apply.
- **Unreleased vehicles** — storage aging into the statutory lien process; deadlines tracked because missed notifications void the lien.
- **Failed payment** — card declined at the scene or on release; recorded against the job until resolved.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Dispatch console

The dispatcher's primary working surface.

- **Purpose:** capture calls, watch the operation, allocate trucks.
- **Typical information:** call queue (unassigned / assigned / active) with vehicle, location, source, and requirement flags; live map with truck positions and statuses; driver availability; incoming digital dispatches.
- **Primary actions:** create/edit a call, assign or reassign a truck-and-driver, message a driver, handle exceptions, record times and outcomes.

### Live map

- **Purpose:** the spatial picture of supply and demand.
- **Typical information:** truck positions and statuses, call locations, patrol coverage.
- **Primary actions:** locate a truck or call, judge coverage, support allocation decisions.

### Driver app

- **Purpose:** the operator's side of the loop.
- **Typical information:** assigned calls with location, vehicle, and service details; navigation context; current job state.
- **Primary actions:** accept a call, progress status, photograph and document the vehicle, collect signature or payment, record the drop-off, message dispatch.

### Intake channels

- **Purpose:** bring demand into the system.
- **Typical surfaces:** phone (call-taker), digital feeds from motor clubs, insurers, and work providers, web request forms, agency tow-request integrations.
- **Primary actions:** receive and confirm calls, quote prices, schedule transports.

### Lot / impound screens

- **Purpose:** run the storage operation.
- **Typical information:** vehicle inventory with arrival times, aging, accrued charges, hold and lien status.
- **Primary actions:** record arrivals, calculate and quote fees, process releases, generate notification letters, send vehicles to auction.

### Back office

- **Purpose:** run the business around the operation.
- **Typical surfaces:** rate and call-type configuration, truck and driver records with compliance documents, motor-club billing and payment import, accounts receivable, commission and payroll reporting, performance dashboards.
- **Primary actions:** configure rates, maintain records, invoice accounts, settle drivers, review performance.

## Important Rules / Behaviors

### The call source determines authorization and payment

A call is never just a location and a vehicle: who requested the tow decides whether the tow is lawful and who will pay. Authority rotation tows are performed under the agency's program rules and fee schedule; club tows are billed to the club at contracted rates; private tows require the property owner's or vehicle owner's authorization; direct calls are collected at the scene or on release. The completed job bills along the path its source defines.

### Capability gates allocation

A call is allocated only to a truck whose duty class and equipment match the job's requirements — and, for authority work, only to a company holding its place on the applicable rotation list. The availability state is both a working picture and an access rule: it prevents double-assignment and phantom capacity.

### Rotation fairness is a contract, not a preference

Authority rotation programs distribute calls in list order under written rules — commonly response-time limits, forfeiture of the turn for failure to respond, and prohibitions on referring calls to other operators. Dispatch software for rotation-heavy operations makes the rotation explicit and auditable — every assignment and timestamp logged, so fairness is visible to the agency, the companies, and the public.

### The vehicle is documented before it moves

Because the towed vehicle is someone else's property, the condition record — photographs, condition report, often a walkaround video, time-stamped before hook-up — is a first-class part of the job, not an optional attachment. It is the company's evidence in damage disputes and its record in custody questions.

### Custody continues after the drive

A stored vehicle is inventory with a legal clock: storage fees accrue, releases are processed against identification and payment, and unclaimed vehicles move through statutory notification to lien and auction on mandated timelines. The system tracks the steps because the lien — and the money and the title behind it — depend on them being done on time and in order.

### Response time is the operational currency

Club contracts and rotation programs alike measure the tower on time-to-arrival. Products record promised ETAs against actual arrivals, report response performance by account, and surface stalled jobs — because the service-level commitment, not the tow itself, is what the principals buy.

### Terminal states are recorded, not silent

Cancelled, refused, and forfeited calls remain in the record with reasons. They feed rotation audits, club reporting, driver disputes, and revenue analysis.

## Variants

- **Call-source mix.** Rotation/police-heavy operations (incident and impound tows under municipal or state programs), motor-club-heavy operations (member service at contracted rates), private-property operations (parking enforcement accounts), and transport-heavy operations (dealer, auction, and equipment moves on hourly or port-to-port rates).
- **Duty class.** Light/medium-duty generalists versus heavy-duty recovery specialists (rotators, heavy wreckers, air cushions); many companies run both as divisions of one operation.
- **Service breadth.** Tow-only operations versus towers who also perform light roadside services — jump-starts, tire changes, fuel delivery, lockouts — as ordinary call types, with the tow as the escalation when the roadside fix fails.
- **The agency-side twin.** Some vendors serve public agencies as well as towers: rotation management with fair-distribution rules, tow requests generated automatically from agency dispatch systems with status flowing back, private-tow intake and verification, and public search for towed vehicles. The tower-side and agency-side products meet at the tow request.
- **Regional regime.** US operations under state impound/lien statutes and municipal rotation ordinances; UK and Irish recovery operators under breakdown-club service-level culture, connected to clubs and insurers through industry job-transfer networks.
- **Scale and packaging.** Free or entry tiers for owner-operators; all-in-one cloud systems for small and mid-size companies; multi-location and municipal-impound systems for larger operations; consolidated suites bundling payments, liens, tracking, and auctions around the dispatch core.
- **Deployment.** Cloud SaaS is dominant; legacy terminal-era and on-premises systems still run the same core.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Dispatch Management | generic sibling | Shares the dispatch spine (work queue + resource availability + assignment + live picture). The tow-specific semantics — vehicle-recovery calls with authorization sources, capability-matched trucks, custody and disposition, multi-principal billing — are what make this a separate Type. |
| Taxi Dispatch Platform | same spine, different work semantics | Allocates passenger rides with fare machinery, licensed driver-and-vehicle pairing, and tariff rules. Towing allocates vehicle recoveries with truck-class matching, custody/lien arcs, and multi-principal billing. No passenger, no fare meter. |
| Roadside Assistance Platform | upstream mediator, most confusable | The assistance organization mediates a stranded motorist's incident across a contracted provider network, with coverage rules deciding who pays. Its dispatches arrive in the tower's system as inbound club calls. The tower's platform runs its own fleet and bills the principals; it performs no coverage adjudication. Towing companies typically sit on both sides — own dispatch software plus platform job feeds. |
| Computer-aided Dispatch / CAD | agency-side seam | CAD dispatches public-safety resources to emergencies; tow requests are generated from CAD events and flow to the tower (or to the agency's rotation system) with status flowing back. The rotation list governs tow allocation, not emergency response. |
| Fleet Management System | estate vs assignment | The FMS owns the vehicle estate — telematics, maintenance, fuel, compliance. Towing dispatch platforms consume GPS feeds from such systems and keep light inspection records, but the trucks exist here as dispatchable supply, not as an estate under oversight. |
| Courier Management Platform | goods vs vehicles | Both move things between points with custody, but parcels move for commercial recipients; towed vehicles are subjects of authorization, storage, and statutory lien — often with no recipient waiting. |
| Collision Repair Management | post-tow adjacency | The tow ends at drop-off; the repair estimate, workflow, and parts are another Type. Damage documentation here serves the tow's liability, not the repair. |
| Impound / lot management | module, not a separate Type | Lot inventory, storage fees, liens, and auctions ride inside this Type's products (and on the agency side of the seam) rather than forming a standalone product category of their own. |

The sharpest boundary is the **upstream/downstream seam with the roadside assistance platform**: club and insurer dispatches are this Type's inbound calls, and the tower's own fleet, lot, and lien files are what the roadside side merely reaches through its provider network.

## Representative Products

- **Towbook** (Extric LLC) — independent cloud platform and market leader for private towers in the US; dispatch, impound management, liens, auctions, motor-club direct billing, and accounting in one system; call-volume-tiered pricing.
- **Autura** (Autura NewCo; the 2024 combination of Autura/AutoReturn and Traxero) — the consolidated ecosystem: private-side towing management systems (Dispatch Anywhere, TOPS, TraxeroGo, Omadi, InTow, Tracker) and the government-side Aries line (tow request and rotation management, CAD integration, private-tow intake, impound management).
- **Apex RMS** (Apex Networks) — the UK and Ireland regional leader for vehicle recovery operators; control-room dispatch connected to breakdown clubs and insurers through industry job-transfer networks, with rate structures per work provider and DVSA/DVLA-aligned compliance.

These three were chosen for different product philosophies (independent all-in-one / consolidated public-private ecosystem / regional specialist), different customer tiers (SME towers to enterprises, agencies, sole operators to national fleets), and different regulatory regimes (US impound/lien law, UK breakdown-club culture). Other products exist in this market but were not directly reachable during this research pass; no claims are made about them here.

The defining core was checked against the phone-and-rotation-list era, radio-dispatch requirements, and the 1990s electronic job-transfer standard (Turbo Dispatch) to avoid defining the Type by today's app-and-cloud implementation.

## Sources

Research date: **2026-09-10**

- Towbook — home, features, pricing, AAA partner page, support: https://towbook.com/ , https://towbook.com/features , https://www.towbook.com/pricing , https://towbook.com/partners/aaa , https://towbook.com/support
- Autura — home and towing-lifecycle pages: https://www.autura.com/ ; towing management: http://autura.com/towing-and-recovery/towing-management-software , https://autura.com/towing-recovery-systems , https://autura.com/towing-recovery-systems/towing-management/dispatch-anywhere ; government side: https://www.autura.com/government/tow-request-and-rotation , https://autura.com/government-towing-systems , http://autoreturn.com/ ; support: https://support.autura.com/en-us/articles/15936096-can-autura-integrate-with-my-current-cad-system ; https://autura.com/about
- Apex Networks — home and vehicle-recovery product page: https://www.apex-networks.com/ , https://www.apex-networks.com/vehicle-recovery-how-we-help/ ; AVRO directory listing: https://www.avrouk.com/advertiser.asp?aID=10&p=Automotive%20Software
- Corporate / market structure: BusinessWire, "Autura and Traxero Join Forces" (2024-10-17); GlobeNewswire, "Traxero North America Announces Combination…" (2022-04-14); Tow Times (2022-05-06); Prince William County, VA press release (2025-10-20)
- Regulatory / agency corpus (rotation lists and truck classes): Spanish Fork (UT) PD Tow Truck Rotation List Policy; California Highway Patrol Rotation Tow Program; Arkansas towing rotation regulations (130.00.04 Ark. Code R. § 003); Beaumont (TX) PD Non-Consent Towing Rotation System Regulations; Salt Lake City PD Rotation Application; Philadelphia PD Directive 12.5 and the City's 2018 letter to towers; Santa Cruz (CA) Municipal Code 10.75
- Historical: Wikipedia, "Turbo Dispatch" (UK electronic job-transfer standard, 1994–); FleetRabbit tow-fleet blog (Tier 3, "radio check" framing and dispatch-integration statement)

> Sourcing limitations: Tracker Management's own site was unreachable (timeout) and is known only through corporate sources; Towbook's knowledge-base articles and parts of Autura's help center were not directly fetched. Exact per-product status vocabularies, numeric limits, fee schedules, and plan-gated capabilities are intentionally not asserted in this document; vendor performance claims (response-time percentages, vehicle volumes) were treated as vendor statements and excluded from the canonical description. Product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
