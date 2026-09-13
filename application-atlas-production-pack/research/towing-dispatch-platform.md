# Research Notes — Towing Dispatch Platform

Research date: 2026-09-10
Slug: towing-dispatch-platform (DIRECTORY §18 Transportation, Mobility & Logistics)

## Research Goal

Understand what a Towing Dispatch Platform actually is as an Application Type: the operator-side software a towing (and vehicle recovery) company runs its dispatch operation on. Produce a vendor-neutral Application Document explaining the core structure, the dispatch workflow, the interfaces, the rules that matter, and the boundaries against neighboring Types — especially Roadside Assistance Platform (which hung a "keep-both" forward flag against this leaf from its 2026-09-09 pass), Taxi Dispatch Platform (which recorded a same-spine/different-work-semantics relationship on 2026-09-10), and Dispatch Management (which named towing as industry work semantics of the generic machinery).

## Initial Boundary (hypothesis before research)

- Hypothesis: the tow operator's own system of record — tow/recovery calls in (from police/authority rotation, motor clubs, private property, private payers, transport accounts), live truck/driver availability, allocation, job lifecycle through hook-up/transport/drop-off, closing into billing (motor club direct billing, authority contract, private pay, accounts) and the impound/storage/lien/auction arc for towed vehicles.
- Nearest neighbors: Dispatch Management (generic spine), Taxi Dispatch Platform (same spine, passenger-transport semantics), Roadside Assistance Platform (assistance-organization mediation over a contracted network), Computer-aided Dispatch / CAD (agency-side emergency dispatch), Fleet Management System (vehicle estate), Courier Management (goods), Collision Repair Management (post-tow), Impound/lot management (no separate directory leaf).
- Pre-hung flags to discharge from the towing side:
  - roadside-assistance-platform pass (2026-09-09): "FORWARD FLAG to unprocessed towing-dispatch-platform: keep-both recommended on the mediation seam — the towing operator's own dispatch of its tow fleet (tow-specific work items, own equipment, Dispatch Management machinery specialized to tows) vs this Type's assistance-organization incident mediation (multi-service catalog with tow as the escalation backbone + contracted external provider network + coverage adjudication + payer↔provider money loop); towing companies sit on both sides (own dispatch software — the Honk provider sample names Towbook/Autura integration — AND platform job alerts/API)… ratify from the towing side when that pass runs."
  - taxi-dispatch-platform pass (2026-09-10): "towing-dispatch-platform remains unprocessed (same-spine/different-work-semantics relationship recorded structurally, no definition asserted)"; also ratified dispatch-management's carve-out pattern (generic four-structure dispatch spine shared; specialized leaves bound to their own work semantics).
  - dispatch-management pass (2026-09-07): "Towing Dispatch Platform | industry-specialized sibling | Specializes the work item to tows and roadside recoveries. Same core loop underneath."
  - collision-repair-management pass (per roadside pass citation): "dispatching tow trucks is a different Type".

## Research Questions

1. What is the unit of work (the "call"), and what does it carry (vehicle, location, service, destination, call source/authorization)?
2. What call sources exist (police/authority rotation, motor clubs/insurers, private property, private pay, transport/commercial accounts) and how does the source shape the job?
3. What is the supply side — how are trucks and drivers held (duty class, equipment type, certifications, availability)?
4. How does allocation happen (manual, assisted, automatic; rotation rules; nearest-truck)?
5. What is the job lifecycle, including hook-up, transport, destination, and disposition of the vehicle?
6. What happens after drop-off — impound/storage lot, storage fees, release, lien processing, auctions?
7. How does money work — who is billed for what (motor club direct billing, authority rates, private pay at scene, storage/lien fees), and how do driver commissions work?
8. What tow-specific risk machinery exists (damage documentation, condition reports, signatures)?
9. What interfaces exist (dispatch board/map, driver app, intake channels, back office, lot screens)?
10. Is there an agency-side twin (rotation management, CAD integration) and how does it relate?
11. What variants exist (duty class, geography/regulatory regime, scale, deployment)?
12. Historical check: would phone-and-paper rotation-list dispatch, radio dispatch, and 1990s electronic job transfer (Turbo Dispatch) still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels and geographies:

| Product | Pole | Geography | Evidence tier reached |
|---|---|---|---|
| Towbook (Extric LLC) | independent market leader; all-in-one cloud (dispatch + impound + accounting) for private towers | US/global | Tier 1–2: features, pricing, AAA-partner pages (knowledge base not article-fetched) |
| Autura (Autura NewCo; ex-Traxero: Dispatch Anywhere/Beacon, TOPS, Omadi, InTow, Tracker, TraxeroGo; ex-AutoReturn government line) | consolidated ecosystem spanning the private tower (Dispatch Anywhere light/medium-duty, TOPS multi-location+impound, TraxeroGo free owner-operator) and the public agency (Aries Dispatch: rotation, CAD integration, private-tow intake) | US | Tier 1–2: product pages, government pages, support article, help center (via search), merger press releases |
| Apex Networks (Apex RMS) | UK/Ireland regional leader for vehicle recovery operators; breakdown-club/insurer connectivity; control-room culture | UK/IE | Tier 1–2: home, vehicle-recovery product page, AVRO directory listing |

Rejected/abandoned samples and notes:
- Tracker Management — www.trackermanagement.com request timed out ×1; not directly observed; known only through Traxero/Autura corporate sources. Not used for product-specific claims.
- Omadi — own site now folds into Autura; observed via App Store listing and 2017–18 TomTom press coverage (Tier 3) only.
- Spire Software (UK) — thin official site; noted as a second UK sample but not deep-fetched.
- Swoop (Agero) tow-management tooling — provider-side software of a roadside platform; treated as an overlap-zone data point, not a sample of this Type's independent products.
- Shifton / OctopusPro / FleetRabbit — horizontal field-service or fleet tools with towing marketing pages; used only as Tier 3 corroboration where noted.

## Sources

Official product (fetched 2026-09-10):
- Towbook — https://towbook.com/ ; https://towbook.com/features ; https://www.towbook.com/pricing ; https://towbook.com/partners/aaa ; https://towbook.com/support
- Autura — https://www.autura.com/ ; http://autura.com/towing-and-recovery/towing-management-software ; https://autura.com/towing-recovery-systems ; https://autura.com/towing-recovery-systems/towing-management ; https://autura.com/towing-recovery-systems/towing-management/dispatch-anywhere ; https://www.autura.com/government/tow-request-and-rotation ; https://autura.com/government-towing-systems ; http://autoreturn.com/ ; https://support.autura.com/en-us/articles/15936096-can-autura-integrate-with-my-current-cad-system ; https://www.autura.com/contact ; https://autura.com/about
- Apex Networks — https://www.apex-networks.com/ ; https://www.apex-networks.com/vehicle-recovery-how-we-help/ ; AVRO advertiser directory https://www.avrouk.com/advertiser.asp?aID=10&p=Automotive%20Software

Corporate / market structure (Tier 2–3):
- BusinessWire (2024-10-17), "Autura and Traxero Join Forces to Revolutionize Towing Management Software" — merger of public (Autura/AutoReturn) and private (Traxero) platforms; 3,000+ customers, 50,000+ daily tows (vendor claims).
- GlobeNewswire (2022-04-14), "Traxero North America Announces Combination of the Leading Software Providers in the Towing Industry" — Tracker Management, TOPS Dispatch, Dispatch Anywhere, Omadi PPI, InTow, TraxeroGo, TowSpec, BudgetGPS, TowLien, TowMail, Auction Simplified.
- Tow Times magazine (2022-05-06) — same combination, product family list.
- Prince William County, VA press release (2025-10-20) — Autura private-tow intake launch; residents' towed-vehicle search.

Regulatory / agency corpus (Tier 2 official government documents, used for rotation and truck-class structure):
- Spanish Fork (UT) Police Department, "Tow Truck Rotation List Policy" (PDF) — rotation list mechanics, 15-minute response, fall-to-bottom, storage requirement, 24-7 phone.
- California Highway Patrol, "Rotation Tow Program" page — Tow Service Agreement, rotation tow list, truck-class/equipment questions, chargeable-time rule.
- Arkansas State Police towing rotation regulations (130.00.04 Ark. Code R. § 003, via Legal Information Institute) — light/heavy rotation lists; wheel-lift / rollback / underlift / heavy-duty equipment requirements; forfeit-call-rotation rule.
- Beaumont (TX) Police Department, "Non-Consent Towing Rotation System Regulations" (PDF) — light/heavy lists, one slot per company, no referral of calls.
- Salt Lake City Police Department, "Rotation Application" (PDF) — per-truck records with carrier type (wheel lift / flat bed / 4x4 / heavy duty).
- Philadelphia Police Department Directive 12.5 (PDF) — AutoReturn rotational system; rotation definition; flatbed dispatch; vehicle information conveyed.
- City of Philadelphia letter to towers (2018, phila.gov PDF) — pre-AutoReturn state: "a dispatcher calling down a list of towing companies".
- Santa Cruz (CA) Municipal Code 10.75 — rotation list, minimum equipment standards, radio-dispatch requirement (historical regulatory baseline).

Historical / industry (Tier 3, used only for structure-existence claims):
- Wikipedia, "Turbo Dispatch" — UK public-domain standard since 1994 for electronic transfer of job details between motoring organisations and 400+ recovery agents; packet radio → internet; automatic acknowledgement; queue awaiting manual acceptance; controller accepts/rejects; ~92% of ~4M garaged breakdowns by 2005.
- FleetRabbit blog (2026), "Tow Truck Fleet Management Software" — "Radio Check (Old Way)" framing; heavy-duty equipment (rotators, heavy wreckers); explicit statement that fleet software "integrates with dispatch platforms like Towbook, Dispatch Anywhere, or TOPS" rather than replacing them.
- Omadi/TomTom press coverage (CCJ 2017; PRNewswire) — geofence-based dispatch to roadside/PD calls, automatic arrival timestamps.

## Product Observations

### Towbook (evidence layer A unless noted)

Positioning: "cloud based towing software for dispatching, impounds, & accounting"; "your all-encompassing solution for Private Property, Police Calls, Transport, Local Calls, Motor Clubs, and more"; "towing, roadside and impound software"; built for "owners, managers, drivers, and dispatchers".

Call intake and call types:
- Call taxonomy in the pitch itself: Private Property, Police Calls, Transport, Local Calls, Motor Clubs — the call source is the primary segmentation of demand.
- Digital Dispatching & Email Processing: "Never enter a call from a motor club manually again" — inbound digital dispatches from a long list of motor clubs/insurers/programs (AAA, Agero, Allstate, GEICO, Progressive, Honk, Swoop, Urgently, Tesla, Copart, IAA, FleetNet, Road America, Nation Safe Drivers, Lease Plan USA, …). Motor-club calls can be accepted "directly to your mobile application".
- Web Request Form and Customer Quotes as intake features; Voice Dispatch; Advanced Notification Service; Call Chat; Custom Call Requirements (pricing tiers).

Dispatch:
- "Accepting calls, assigning calls, tracking job progress" as the dispatch loop; customizable dispatch screen; advanced search; driver messaging.
- Automatic Truck/Driver Assignments (upper tiers); GPS tracking via iOS/Android apps or integrated providers (Azuga, DriverLocate, Samsara, US Fleet Tracking, Verizon Connect, Webfleet).
- Transport options: hourly rate items (port-to-port), multi-vehicle tows, multi-destination tows — transport jobs as a call class.

Driver side:
- Mobile apps (iOS/Android, unlimited devices): drivers accept calls dispatched to them; update status; attach geocoded photos to a call; update call location via GPS coordinates; collect customer signatures; indicate method of payment; create a vehicle damage report; email/text a receipt.
- Equipment Inspections / Driver Check-In: drivers check in "to indicate that they are on the clock" and complete equipment inspection reports sent to managers.
- Commission/payroll reporting; driver/truck volume analytics.

Impound / lot / disposition:
- Impound Manager: "record and manage your impounded/stored vehicles"; state-required letters built in; Auto Data Direct integration; Impound/Task Reminders; Multi-Impound/Lot Management; Notification/State Impound Forms; Tow Out Functionality; Vehicle Lookup; Impound Inventory QR Codes; Auction Manager (beta).
- Damage-claim posture: "Minimize Damage Claims" — geocoded photos, damage reports, signatures as the evidence trail.

Money:
- Motor Club Direct Billing ("submit your invoices to several major motor clubs for payment"); Motor Club Payment Importing (auto-marks paid); customer invoicing/receipts; configurable statements; payment verification tracking; Square integration; QuickBooks Desktop/Online integration; sales-tax reporting; audit & lock calls; call workflow management.
- Pricing tiers by monthly call volume (250/500/1,000/1,500 calls; overage fees) — the call is the metered unit of the business. Multi-company/division linking (e.g., "Heavy Towing, Light Towing, and Roadside" divisions).

AAA partnership page: dedicated offer for AAA service providers — the tower's system is the receiving end of club-dispatched work.

### Autura (evidence layer A unless noted)

Positioning: "Unified Towing Software: Dispatch, Operations, Impound & Sales"; "connecting the complete towing lifecycle, from dispatch to disposition"; serves both "Towing & Recovery" businesses and "Government & Public Safety" agencies. FAQ: "Autura does not own tow trucks or vehicle storage facilities, does not employ any tow operators, does not set towing or storage fees, and does not provide tow services."

Private-side Towing Management Systems (family: Dispatch Anywhere (Beacon), TOPS, Omadi, InTow, Tracker, TraxeroGO):
- Dispatch: "Your dispatchers see every active job, truck location, ETA, and driver status on one screen"; job queue ("see what's waiting, moving, and done"); mobile driver app ("accept jobs, update status, and attach photos from the road"); smart operator assignment; VIN lookups; photo recognition to populate vehicle details.
- Dispatch Anywhere: "designed for the established towing and recovery businesses primarily performing motor club and light- and medium-duty jobs"; reporting module with "job breakdowns by operators, actual arrival times against ETAs, commission payouts, and over 250 other reports"; TowPay embedded card processing; QuickBooks/Whiterail/GPS integrations; "Receive digital dispatches from Allstate, GEICO, Tesla, Agero, Nation Safe Drivers, and more".
- TOPS: "Built for multi-faceted towing operations and impound management" — multi-location and municipal impound with advanced workflows and lien processing.
- TraxeroGo: "Mobile-first digital dispatching for businesses that are just getting started" (free tier for owner-operators).
- Motor-club jobs "directly into your dispatch queue. No manual re-entry."
- Billing/invoicing; lot management ("See every vehicle on your lot… how long it's been there, how much is owed, and the full job history"; automatically calculated charges and fees; send vehicle info by email/text from the lot screen).
- Companion products around the hub: TowPay (payments), TowLien (lien processing and notification; "state-approved in 32+ states"; dashboard with Action Required / Scheduled Tasks / Expired Tasks / Reminders), BudgetGPS (fleet tracking/cameras), Autura Marketplace (unclaimed-vehicle auctions; "moves 77,000 unclaimed vehicles a year" — vendor claim).

Government & Public Safety side (Aries Dispatch, ex-AutoReturn):
- Tow Request and Rotation: agencies manage tow programs digitally; "Contracted providers receive requests directly through the mobile app, accept the job, and complete it digitally. Assignments follow the agency's rotation rules, so the work is distributed fairly, and everyone can see that it was."
- CAD integration: "A CAD integration can generate tow requests automatically… Two-way sync: CAD events create tow requests, and status flows back automatically"; live truck tracking and ETA inside the CAD workflow; "Every request, assignment, and timestamp logged for analytics".
- Officers/telecommunicators submit tow requests digitally (MDC/mobile) "instead of by phone, which clears the radio and the phone lines"; Smart Dispatch "sends tow requests directly to the nearest truck".
- Private Tow Intake: agencies gain visibility into private tows; "tow providers logging tows directly into a centralized system so agencies always know where vehicles are, who moved them, and why" (Prince William County: tow companies enter vehicle info into the portal; staff verify and upload to NCIC/VCIN; residents search towed vehicles online).
- Impound Management (agency side): "streamlining storage lookup, automating regulated fees, and simplifying lien and notification workflows".
- Heritage: AutoReturn contracts (San Diego 2009 — ARIES/Dispatch integrated with SDPD CAD, officers enter tow requests via MDTs, "fully automated… except in special cases"; Philadelphia 2018 rotational tow system).

Corporate: Autura (public towing; Nexa Equity) + Traxero (private towing; Radian Capital) merged 2024-10; combined "3,000+ customers… 50,000+ daily tows" (vendor claims); Traxero had itself combined Beacon Software, TOPS Dispatch, Tracker Management, Omadi, TowLien, Auction Simplified (2022).

### Apex RMS — Apex Networks (evidence layer A unless noted)

Positioning: "Vehicle recovery software that runs every job, end to end"; "used by vehicle recovery operators across the UK and Ireland to dispatch faster, manage every callout from roadside to invoice, and stay connected to the breakdown clubs and insurers you work with"; "Over 1,000 operators… 4M+ annual jobs, 7K active drivers, 4.5K control room staff" (vendor claims); AVRO directory: "market leading software supplier to the rescue and recovery sector".

Job flow:
- "manage every callout from first contact to final invoice — in one place"; real-time job allocation; "direct ANS network connectivity means jobs from breakdown clubs and insurers arrive in your system without a phone call".
- Job Dispatch: "Receive and allocate recovery callouts — direct from work providers via ANS or from your own customers".
- Driver app (Android): "accept jobs, update status at every stage of a callout, capture vehicle condition reports with photos and video, and record customer sign-off… Everything logged digitally from the roadside, nothing relying on paperwork back at the office."
- Paperless job records: "vehicle details, location, job type, work carried out, time on site, and customer sign-off… accurate, timestamped, and accessible instantly".
- Automated invoicing: "When a job closes, the invoice goes out automatically — calculated from the job details your driver logged in the field. Different rate structures for work providers, direct customers, and storage jobs are all handled within RMS."
- Reporting: "response times, job volumes, and revenue by account… data to back your SLA performance".
- Compliance: "Track MOTs, insurance, driver licences, and vehicle checks across your recovery fleet — with timed reminders"; Workshop PDA app with "DVSA-approved inspection sheets".
- Vehicle tracking: "dispatch the right vehicle to every callout"; "always send the nearest available vehicle and meet the response targets your work providers expect".
- PinPoint: stranded motorists share exact location by link. ResQTrac: live tracking link for the motorist. SMS updates at each stage ("driver is allocated, on route, and close").
- Vehicle Registration Lookup: "DVLA-verified vehicle information the moment a job comes in — confirm the make, model, and spec so you always send the right recovery vehicle and the right equipment."
- VCRF (Vehicle Condition Report): "drivers can record a walkaround video of the vehicle alongside images and a digital Vehicle Condition Report (VCRF) — creating a secure, time-stamped record before the vehicle is moved. If a damage claim arises, the evidence is already there."
- Rate cards per work provider (review mentions "a very complicated and long rate card for a new customer"); RMS Lite for smaller operators; modular add-ons; exports to accounting packages.

### Regulatory / agency corpus (evidence layer A for the rotation and truck-class structures; Tier 2–3)

Rotation lists (authority-side allocation):
- Santa Cruz M.C. 10.75: "Rotation list shall mean a list maintained by the police department of operators… from which the police department will make calls for towing services on a sequentially rotating basis"; minimum equipment standards; "Radio dispatching equipment… Dispatching shall be from a central dispatching point available by telephone twenty-four hours per day" (historical baseline).
- Spanish Fork PD: officer requests dispatch contact "the tow truck company at the top of the list"; failure/15-minute response → "fall to the bottom of the list"; storage at the company's facility unless owner authorizes otherwise; 24-7 phone required.
- Beaumont PD: two lists (light duty; heavy duty ≥10,000 lbs GVW); "one slot per company"; list held by the 911 center; "A towing company may not refer non-consent tow calls to other companies".
- Philadelphia Directive 12.5: "Rotation Tow System: A method of selecting a towing company from an authorized list… Once the assignment is made, that towing company rotates to the bottom of the list"; dispatch "the proper tow truck to the scene (flatbed, etc.)"; vehicle info conveyed (location removed from, make/model, registration/VIN, location taken). City letter (2018): the prior state was "a dispatcher calling down a list of towing companies".
- CHP Rotation Tow Program: Tow Service Agreement; rotation tow list; truck classes (a "B, C, or D" class truck may hold a place on a lighter list "if the vehicle is equipped with the proper equipment"); "Chargeable time begins at the place of business or the point of dispatch, whichever is closer".
- Arkansas rotation regulations: separate light/heavy lists; equipment requirements (wheel-lift, rollback, underlift, heavy-duty); if the called company lacks the required equipment, "the next available towing business having such equipment shall be called and the towing business not providing such equipment shall forfeit that particular call rotation".

Truck classes / capability axis:
- Salt Lake PD rotation application records each truck with "Type of Carrier (circle all that apply): Wheel Lift / Flat Bed / 4x4 / Heavy Duty".
- Arkansas: wheel-lift-equipped, rollback-equipped, underlift-equipped, heavy-duty classes.
- FleetRabbit (Tier 3): heavy-duty/commercial recovery "requires specialized equipment — rotators, heavy wreckers, air cushions".

Historical / regional:
- Turbo Dispatch (UK, 1994–): motoring organisation's computer transmits job details to the recovery operator's computer (packet radio, later internet); automatic acknowledgement; "job details… in a queue awaiting manual acceptance by the recovery operator's controller"; controller "accepting, or rejecting the job"; by 2005 ~92% of ~4M annual garaged breakdowns transmitted this way. Documents (a) the digital-intake structure predating modern SaaS, (b) the work-provider (breakdown club) call source, (c) the pre-electronic state (phone-based job passing).
- Apex testimonial: "15 years with a notebook and my phone" — paper/notebook-era operator practice (Tier 3, anecdotal).

## Cross-product Comparison

| Structure | Towbook | Autura (private TMS) | Autura (Aries/agency) | Apex RMS | Regulatory/historical corpus |
|---|---|---|---|---|---|
| Unit of work | Call (Private Property / Police / Transport / Local / Motor Club) | Job/call; motor-club jobs into dispatch queue; transport options | Tow request (from officer/MDC or CAD event) | Callout (from work providers via ANS or own customers) | Rotation tow request; vehicle + location + reason |
| Call source / authorization recorded | Yes — call type is the primary segmentation | Yes — motor club vs private vs police | Yes — agency program, rotation rules | Yes — work provider / direct customer / storage | Yes — rotation (authority) vs owner-request |
| Vehicle identity on the job | Vehicle lookup; photos; damage reports | VIN lookup; photo recognition | Vehicle info from CAD event | DVLA reg lookup (make/model/spec) | Registration/VIN conveyed (Philadelphia) |
| Destination recorded | Multi-destination tows; lot drop | Lot/destination; full job history | Location taken (CAD) | Storage jobs; destination implicit in job record | "Location where vehicle was taken" |
| Supply held as records | Trucks + drivers; check-in; equipment inspections | Drivers + trucks; driver status; ETA | Contracted providers (companies) on rotation | Drivers + vehicles; compliance (MOT/licences) | Rotation lists of companies; per-truck equipment records |
| Capability matching | Divisions (Heavy/Light/Roadside); truck/driver assignment | Smart operator assignment; nearest truck | Rotation rules; nearest truck | "Right recovery vehicle and right equipment" (reg lookup) | Equipment-based list placement; forfeit rule |
| Allocation act | Manual + automatic truck/driver assignment | Manual + smart/automatic | Automatic per rotation rules; provider accepts in app | Real-time allocation; nearest available | Dispatcher calls top of list; rotates to bottom |
| Live picture | Dispatch screen; GPS via apps/integrations | Active jobs + truck location + ETA on one screen | Live truck tracking/ETA in CAD workflow | Control-room view; vehicle tracking dashboard | Radio/phone dispatch; 24-hour dispatch point |
| Job lifecycle | Accept → assign → progress → close; status updates, geocoded photos | Accept → en route → on scene → drop; photos from road | Request → accepted → arrived (timestamps) | Allocated → on route → on scene → sign-off | Called → responds (15-min rule) → tow → store |
| Disposition after drop | Impound Manager; storage; liens; auctions | Lot management; TowLien; Marketplace auctions | Agency impound; regulated fees; lien workflows | Storage jobs as rate structure | Storage facility requirement; state lien processes |
| Money | Motor club direct billing + payment import; QuickBooks; commissions | TowPay; invoicing; commission payouts | Regulated fee schedules (agency programs) | Rate structures per work provider / direct / storage; auto-invoice | Chargeable-time rules; fee schedules; no-charge penalties |
| Damage/risk documentation | Geocoded photos; damage reports; signatures | Photos on job details; "protect your business" | — (agency side) | VCRF + walkaround video, time-stamped before move | Officer directives on-scene |
| Response-time discipline | ETA/mapping features | Actual arrival vs ETA reporting | 12.5-min response claims (vendor) | Response times vs SLA targets | 15-minute rotation response rules |
| Intake automation | Digital dispatching/email processing from ~30 clubs | Digital dispatches from major clubs | CAD auto-creation of tow requests | ANS connectivity from clubs/insurers | Turbo Dispatch (1994): electronic job transfer + manual acceptance |

Convergent findings (evidence layer B across the sample):
1. The call is segmented by source, and the source determines authorization and the payment path — present in every product and in the regulatory corpus (rotation vs owner-request).
2. Trucks are held as records with class/equipment, and matching job requirements to truck capability is explicit in all poles (divisions, smart assignment, reg-lookup equipment matching, equipment-based rotation lists).
3. The lifecycle continues past drop-off into disposition (lot/storage/lien/auction) in the US poles and as storage rate structures in the UK pole; the agency corpus regulates storage and liens.
4. Damage documentation before moving the vehicle is a first-class, product-level structure in all three product poles (geocoded photos/damage reports; photos "protect your business"; VCRF walkaround video) — driven by the fact that the towed vehicle is someone else's property.
5. Motor club / work-provider digital intake is universal in the current market (Towbook's club list, Autura's club list, Apex's ANS) and predates SaaS (Turbo Dispatch, 1994).
6. Driver commissions and per-driver/per-truck productivity reporting are common to all private-side products.
7. Response-time discipline (ETA vs actual, SLA targets, rotation response rules) is a shared operational currency.

## Canonical Model

### L0 — Defining Invariant

Four structures, jointly held. Remove any one and the product stops being a towing dispatch platform:

1. **The vehicle-recovery call as the unit of work.** A persistent, identified request to recover, move, or service a specific vehicle: the vehicle (identity — make/model/plate/VIN), the incident/pickup location, what is needed (tow or light service), the destination (repair shop, storage lot, dealer, residence — where the vehicle is to be taken), and the call source / authorization (authority rotation, motor club/work provider, private property, private payer, commercial account). The call source is structural, not metadata: it determines who authorized the tow and the payment path the completed job will follow. Remove → a generic dispatch work item (Dispatch Management).

2. **The capability-matched tow fleet as live dispatchable supply.** Trucks held as records with duty class and equipment type (light/medium/heavy duty; flatbed/rollback, wheel-lift/wrecker, rotator) together with drivers, each carrying a live availability state (on shift/on patrol, committed, out). Job requirements are matched against truck capability — a wheel-lift call needs a wheel-lift truck; a heavy recovery needs heavy equipment. Assignment consumes availability; completion restores it. Remove → a generic resource roster (the supply side loses its tow-specific identity).

3. **The allocation act over a live dispatch picture.** The binding of a call to a specific truck-and-driver — by dispatcher hand, with system assistance (nearest truck, smart assignment), or automatically under configured rules (rotation order for authority work; proximity for response-time work) — visible on a live board/map shared by the operation. Remove → not dispatch at all.

4. **The tracked job lifecycle closing into the operator's commercial record.** Every call is tracked from receipt through allocation and performance (en route → on scene → hook-up → transport) to a terminal state — completed at its destination (with the vehicle's disposition recorded), cancelled, or refused — and completion produces the commercial record: charges under the applicable basis billed to the party standing behind the call source (motor club direct billing, authority contract rates, private payment at the scene or on release, account invoicing), plus the driver's commission record. Remove → a dispatch log with no business record.

### L1 — Common Mature Structure

Present in most current products; expected by the market; not definitional:

- Digital call intake from motor clubs / insurers / work providers (Towbook digital dispatching & email processing; Autura club feeds; Apex ANS connectivity; historically Turbo Dispatch since 1994).
- GPS / truck tracking — via the driver app or integrated telematics providers.
- Driver mobile app — accept calls, progress status, navigation context, photos, signatures, receipts.
- Impound / storage lot management — vehicle inventory, storage-fee calculation, aging, release handling.
- Lien processing and notification — owner/lienholder identification, state-compliant letters, deadline tracking.
- Unclaimed-vehicle auction / disposal machinery.
- Motor-club direct billing, payment importing, accounting integration (QuickBooks-class).
- Damage documentation — geocoded photos, condition reports (VCRF), walkaround video, signatures.
- Driver commissions / payroll; per-truck and per-driver productivity reporting.
- Compliance records — driver licences, truck inspections, insurance; timed reminders.
- Motorist notifications — SMS stage updates, live tracking links, location-share links.
- Vehicle identity lookup — VIN/plate decode to populate job details and match equipment.
- Reporting — response times vs ETA/SLA, revenue by account/call source, call volumes.

### L2 — Variant / Optional Structure

- Call-source mix — rotation/police-heavy, motor-club-heavy, private-property-heavy, or transport-heavy operations.
- Agency-side twin — rotation management, CAD integration, private-tow intake, public towed-vehicle search (Autura Aries pole); some vendors serve both sides of the seam.
- Duty-class specialization — light/medium-duty generalists vs heavy-duty/recovery specialists (rotators, air cushions); divisions inside one company.
- Light roadside services as call types — jump-starts, tire changes, fuel delivery, lockouts (towers do light service; the tow is the escalation backbone).
- Regional regulatory regime — US state impound/lien statutes and municipal rotation ordinances; UK breakdown-club SLA culture and DVLA/DVSA compliance.
- Scale and packaging — free owner-operator tiers (TraxeroGo), SME all-in-one (Towbook, RMS Lite), multi-location enterprise (TOPS), consolidated suites.
- Deployment — cloud SaaS dominant; legacy on-prem/terminal-era systems still run the same core.
- Payment collection posture — embedded processing (TowPay), third-party integrations (Square), at-scene or on-release collection.

### L3 — Vendor-specific Structure

(Research Notes only — not for the Application Document.)
- Towbook: pricing tiers metered by monthly call volume with overage fees; "What Towbook Is Not" page; Voice Dispatch; Out-of-Network Program; Auction Manager (beta); AAA partner program.
- Autura: Aries brand (government), TraxeroGo/Dispatch Anywhere/TOPS product ladder; TowLien "state-approved in 32+ states"; BudgetGPS; TowPay; Autura Marketplace (77,000 vehicles/year vendor claim); Fort Worth / Utah Highway Patrol / San Diego / Philadelphia case studies; 12.5-minute response and "50% faster dispatches" claims; AutoReturn heritage (2009 San Diego CAD integration; 2018 Philadelphia rotation contract).
- Apex: ResQTrac, PinPoint, VCRF, CSSP portal, Workshop PDA (DVSA-approved sheets), RMS Lite, Android-only driver app.
- Omadi: TomTom WEBFLEET/PRO-terminal integration; virtual geofencing with automatic arrival timestamps; "Omadi PPI".
- Traxero/Autura corporate history (2022 combination; 2024 merger; 3,000+ customers / 50,000+ daily tows vendor claims).

## Vendor-specific Findings

- Towbook's call-volume pricing makes the call itself the metered commercial unit — corroborates the call-as-unit-of-work abstraction, but the pricing mechanics are vendor-specific.
- Autura is unique in the sample in operating on both sides of the public/private seam (agency rotation management + tower TMS) and in explicitly disclaiming being a towing company ("does not own tow trucks… does not provide tow services") — useful boundary evidence, vendor-specific posture.
- Apex's DVLA registration lookup and DVSA inspection sheets are UK-regime realizations of the vehicle-identity and compliance structures — regime-specific implementations, not Type structure.
- Omadi's geofence auto-arrival timestamps are one product's automation of the on-scene event — the event itself is common; the automation is vendor-specific.

## Boundary Findings

### vs Dispatch Management (generic sibling) — ratifying dispatch-management's carve-out from the towing side

The generic dispatch spine is fully present here: dispatchable work items (calls), a resource roster with live availability (trucks + drivers), the assignment act, and the live dispatch picture. What makes this a separate Type is the tow-specific work semantics bound to that spine:
- the call carries vehicle-recovery semantics (specific vehicle, incident location, destination, authorization source) rather than an arbitrary work item;
- the supply is capability-matched tow equipment (duty class, equipment type), not generic labor;
- the job's authorization/payment structure is multi-principal (authority rotation, motor club, private property, private pay, account) rather than a single customer frame;
- the lifecycle extends into vehicle custody and disposition (lot, storage fees, lien, auction) — the towed vehicle is cargo that becomes inventory.
Remove those semantics and the residue is exactly the generic dispatch machinery — consistent with dispatch-management's "industry-specialized sibling" classification. RATIFIED.

### vs Taxi Dispatch Platform (same spine, different work semantics) — discharging the taxi pass's structural note

Same four-structure spine (work queue + availability + assignment + live picture + commercial closure). The work semantics differ on every axis:
- work item: passenger ride with pickup/destination and fare basis vs vehicle recovery/movement with incident location, vehicle identity, destination, and authorization source;
- supply: licensed driver-and-vehicle pairing for carrying people vs capability-matched tow trucks for carrying vehicles;
- money: intrinsic fare machinery (metered tariffs, regulated rates) vs multi-principal billing (motor club direct billing, authority contract rates, private pay, storage/lien fees);
- culture: shift/zone availability and fairness queues vs rotation lists (authority work) and response-time SLAs (club work);
- risk machinery: passenger service quality vs damage documentation on the towed vehicle and custody/lien compliance.
No fare meter, no passenger, no zone-queue taxi culture here; no impound/lien arc in taxi. Keep-both. RATIFIED.

### vs Roadside Assistance Platform (the mediation seam) — discharging the roadside pass's forward flag; keep-both RATIFIED from the towing side

The roadside pass proposed: the towing operator's own dispatch of its tow fleet (tow-specific work items, own equipment) vs the assistance organization's incident mediation (multi-service catalog with tow as the escalation backbone + contracted external provider network + coverage adjudication + payer↔provider money loop). This pass confirms the seam from the towing side:
- The tower's system receives work FROM the assistance organizations: Towbook's digital dispatching lists AAA, Agero, Honk, Swoop, Urgently (all roadside-platform/motor-club principals) as inbound call sources; Autura names Allstate, GEICO, Tesla, Agero, Honk; Apex receives jobs "from breakdown clubs and insurers" via ANS. The roadside platform dispatches the tower; the tower's own platform dispatches its own trucks. The two systems are upstream/downstream of each other, not competitors for the same product.
- The tower's system has no coverage adjudication: a club call arrives already authorized; the tower bills the club under its contracted rate structure. The coverage/eligibility machinery and the payer↔provider money loop live on the roadside side.
- The tower's system owns what the roadside platform's provider network merely reaches: the trucks, the drivers, the lot, the lien files. Autura's FAQ line ("does not own tow trucks… does not provide tow services") marks the same line from the software-vendor side.
- Towing companies sit on both sides (own dispatch software AND platform job alerts/API), exactly as the roadside pass recorded. The roadside platform's provider-side tow-management tooling (e.g., Swoop's) is an overlap zone: platform-distributed provider software vs the tower's own system of record — a deployment posture, not a Type collapse.
KEEP-BOTH RATIFIED.

### vs Computer-aided Dispatch / CAD (agency-side seam)

CAD dispatches public-safety resources to emergency incidents under response-priority rules; it has no commercial settlement. The tow request is a handoff point: Autura's CAD integration "generates tow requests automatically" from CAD events "and status flows back" — two-way sync across a Type boundary. The agency-side rotation product (Aries) is the tow-program management layer that sits between CAD and the towers; the tower-side platform receives the resulting request. The rotation list itself (Santa Cruz, Spanish Fork, CHP, Beaumont, Philadelphia) is the authority's allocation rule over tow companies — it governs this Type's authority-work allocation but is not the emergency dispatch of CAD. Distinct Types; the seam is the tow request.

### vs Fleet Management System (estate vs assignment)

The FMS owns the vehicle estate (telematics, maintenance, fuel, compliance). Towing dispatch platforms consume location feeds from GPS providers (Towbook: Azuga, Samsara, Verizon Connect, Webfleet; Autura: BudgetGPS) and carry light truck-maintenance/inspection touches, but the estate system of record is the FMS. Third-party corroboration is explicit: FleetRabbit — "Does FleetRabbit replace my dispatch software? No — it integrates with dispatch platforms like Towbook, Dispatch Anywhere, or TOPS." Assignment is central here; estate oversight is secondary.

### vs Collision Repair Management (post-tow adjacency)

The tow job ends at drop-off (shop, lot, dealer); the repair is another Type's workflow. Consistent with the collision-repair pass's recorded judgment that "dispatching tow trucks is a different Type." The tow platform's damage documentation (photos, condition reports) serves the tow's liability, not the repair estimate.

### vs Courier / Last-mile Delivery (goods vs vehicles)

Both move things between locations with custody, but the unit differs: parcels vs vehicles-as-subjects. Towing's custody arc is regulatory (impound, lien, auction under state law), not commercial fulfillment; the "recipient" is often absent (tow at authority request) and the destination is frequently the operator's own lot. Distinct Types.

### Impound/lot management (no separate directory leaf)

Lot management appears as a module inside this Type's products (Towbook Impound Manager; Autura lot management; TOPS municipal impound; Apex storage rate structures) and on the agency side (Autura government impound management). No separate leaf exists in the directory; the structure is documented here as part of the tow lifecycle's disposition arc. If the agency-side impound/lien/auction machinery were ever split, it would be a new-leaf question — noted, no directory change requested.

## Uncertainties

- Exact per-product status vocabularies for the call lifecycle were not asserted (knowledge-base articles not fetched for Towbook; Autura help center only partially reachable via search). The conceptual cycle is corroborated; the labels are not.
- Tracker Management's own product pages were unreachable (timeout); its capabilities are known only through Traxero/Autura corporate descriptions — no product-specific claims made.
- Heavy-duty/recovery specialization: no standalone heavy-recovery dispatch product was identified in this pass; heavy work appears as divisions/equipment classes inside the same products. Whether a distinct heavy-recovery software niche exists remains unverified.
- The precise boundary between a tower's TMS and a roadside platform's provider-side tooling (Swoop tow management) is a deployment posture question; both were not deep-fetched in this pass.
- UK storage/lien practice: Apex shows storage as a rate structure; the UK regulatory lien arc (vs US state statutes) was not researched in depth — the disposition arc's US intensity is well-evidenced, its UK depth less so.
- Historical depth: the paper-era tow office (call tickets, tow bills, radio dispatch) is evidenced indirectly (Philadelphia's "dispatcher calling down a list", Santa Cruz's radio-dispatch ordinance, Turbo Dispatch's pre-electronic context, Apex's "notebook and my phone" testimonial) rather than from a dedicated trade-history source.

## Final Synthesis

A Towing Dispatch Platform is the tow operator's own dispatch system: the operational and commercial system of record for a vehicle-recovery business. Its defining core is four jointly-held structures:

1. the **vehicle-recovery call** — unit of work carrying the specific vehicle, the incident location, the service needed, the destination, and the call source/authorization that determines the payment path;
2. the **capability-matched tow fleet** — trucks with duty class/equipment plus drivers, held with live availability that assignment consumes and completion restores;
3. the **allocation act over a live dispatch picture** — binding call to truck-and-driver by hand, with assistance, or automatically (rotation order for authority work, proximity for response work);
4. the **tracked job lifecycle closing into the commercial record** — receipt → allocation → en route → on scene → hook-up → transport → destination/disposition → billed against the call source, with driver commissions recorded.

Around that core, mature products add: digital intake from motor clubs/work providers, GPS tracking, driver apps, impound/lot management, lien processing, auctions, damage documentation, compliance records, motorist notifications, and reporting. The market's distinctive structures — rotation lists governing authority work, truck-class capability matching, the custody/disposition arc, multi-principal billing, and damage documentation before the vehicle moves — are all realizations of the four core structures under towing's regulatory and commercial conditions, not additions to them.

The Type sits in a confirmed three-way seam: generic Dispatch Management supplies the shared spine; Taxi Dispatch shares the spine with passenger-transport semantics; Roadside Assistance Platform is the upstream mediator whose club/insurer dispatches arrive as this Type's inbound calls. All three boundaries were ratified from the towing side in this pass; keep-both in every case.
