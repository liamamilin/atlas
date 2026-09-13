# Research Notes — Non-emergency Medical Transportation Platform

Research date: 2026-09-09
Slug: non-emergency-medical-transportation-platform
Directory leaf: Non-emergency Medical Transportation Platform (Section 18, Transportation, Mobility & Logistics)

---

## Research Goal

Understand what a Non-emergency Medical Transportation (NEMT) Platform is as an Application Type: the core objects, users, workflows, states and rules, and its boundaries against neighboring Types (EMS Operations, Ride-hailing, Paratransit/demand-response transit, Employee Transportation, School Transportation, Fleet Management, Dispatch Management, TMS, Patient Scheduling, Prior Authorization).

## Initial Boundary

Working hypothesis before research:

- NEMT software manages scheduled, non-emergency transportation of patients/members to and from healthcare services, typically as a benefit administered by Medicaid agencies / managed care organizations through broker organizations, delivered by transportation provider networks.
- Nearest neighbors: EMS Operations Platform (emergency + clinical documentation), Ride-hailing (public on-demand), Paratransit scheduling (transit-agency demand-response), Employee Transportation Platform (employer workforce), School Transportation (student population), Fleet Management (vehicles as assets), Dispatch Management (generic machinery), TMS (freight), Patient Scheduling (appointments, not rides), Prior Authorization (payer-side coverage machinery).
- Prior passes already recorded seams:
  - `ems-operations-platform` (2026-09-07): "Scheduled medical transport (dialysis runs, recurring treatments, facility bookings) is a workload variant of the same platform... A pure NEMT broker platform (routing/brokerage, no emergency response, no clinical documentation) is a different Type." — this leaf is that different Type.
  - `computer-aided-dispatch-cad` (2026-09-07): NEMT/inter-facility transport queues are a non-emergency workload variant of CAD.
  - `employee-transportation-platform` (2026-09-08): NEMT listed as the patient-population sibling.

## Research Questions

1. What is the "trip" object and what does it bind (passenger, addresses, appointment, mode, provider, vehicle, driver, legs)?
2. Who initiates trip requests and through which channels (member, facility, plan, broker call center, broker feed)?
3. How does eligibility/authorization gate trips (benefit enrollment, needs assessment, standing orders)?
4. How are trips scheduled and assigned (mode determination, provider network, subcontracting, route building, multiloading)?
5. What is the trip lifecycle and its states?
6. How does day-of-service dispatch work (manifests, driver apps, status updates, exceptions)?
7. How does billing work (per-trip claims to payers, broker billing files, subcontractor reimbursement, member mileage reimbursement)?
8. What compliance machinery exists (driver credentials, vehicle standards, no-show documentation, audits, FWA)?
9. What interfaces exist (broker console, provider portal, driver app, member app/portal, facility portal, IVR)?
10. Where are the boundaries vs EMS, ride-hailing, paratransit, employee transportation, fleet, dispatch, patient scheduling?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| MTM Link (MTM Health) | broker-operated program platform (broker administers the benefit for Medicaid/Medicare programs, MCOs, state/county governments) | largest-broker pole; member portal/app + facility portal + provider access all documented |
| RouteGenie (provider edition + Broker Edition) | modern provider-side all-in-one + broker-side software | documents the full provider operation (scheduling/dispatch/billing/fleet/driver app/passenger app) AND the broker's subcontractor management machinery |
| TripMaster (CTS Software / Transit Technologies) | established provider-side suite with paratransit/transit heritage | demand-response + paratransit + NEMT in one suite; documents the broker-integration relationship from the provider side |

Rejected/unreachable samples:

- RoutingBox — routingbox.com returned only a page title on two attempts (JS-heavy site); abandoned per network rule.
- WellRyde — wellryde.com returned HTTP 403; abandoned.
- Modivcare (LogistiCare) — broker-operator competitor of MTM; not fetched (broker pole already covered by MTM; noted as uncertainty that the second broker pole is unverified).
- Trapeze MOD/PASS — paratransit heritage check partially covered by TripMaster's own paratransit/public-transit/microtransit scope; Trapeze not fetched.

## Sources

Tier 1/2 official pages fetched 2026-09-09:

- MTM Health — https://www.mtm-inc.net/mtm-link/ (member portal/app user-facing description)
- MTM Health — https://www.mtm-inc.net/healthcare/nemt/ (broker service description, MTM Link feature list, NEMT FAQ, VeyoRide network)
- MTM Health — https://www.mtm-inc.net/service-providers/ (transportation provider network composition)
- MTM Health — https://www.mtm-inc.net/healthcare-providers/ (facility-side trip intake, standard forms incl. Level of Need, Physician Certification Statement)
- RouteGenie — https://routegenie.com/ (all-in-one provider software, module list)
- RouteGenie — https://routegenie.com/nemt-broker-software/ (Broker Edition: subcontractor trip management, credentialing, eligibility, reimbursement)
- RouteGenie — https://routegenie.com/nemt-billing-software/ (billing capabilities)
- RouteGenie — https://routegenie.com/nemt-scheduling-software/ (scheduling capabilities)
- TripMaster — https://www.cts-software.com/ (suite overview, module list, broker partnerships, sectors)

Unreachable: cts-software.com (522, then www succeeded), routingbox.com (title-only ×2), wellryde.com (403).

---

## Product A — MTM Link (MTM Health) — broker-operated program platform

### Key observations (evidence layer A unless noted)

**Positioning.** MTM Health is "one of the nation's largest and most experienced transportation brokers"; it "manages every aspect of the transportation programs we operate... to better manage transportation benefits for Medicaid and Medicare programs, state and county governments, and Managed Care Organizations (MCOs)." Established 1995 "for the sole purpose of coordinating disparate NEMT services."

**What NEMT is (vendor FAQ, layer A):** "a vital benefit that provides transportation for Medicaid and Medicare members who need assistance getting to and from medical appointments... doctor visits, dialysis treatments, physical therapy, and behavioral health appointments." Federal regulations require state Medicaid programs to provide NEMT for eligible members. Modes: sedan (ambulatory), rideshare and public transit, wheelchair-accessible vehicles, non-emergency ambulance, stretcher transport. Medicare Advantage plans offer supplemental NEMT benefits.

**Member-facing surfaces (MTM Link member portal + mobile app):**
- Request a ride (date, pickup where/when, drop-off where), review existing rides, cancel rides.
- Calendar view of rides per day; ride status, pick-up time and address, drop-off address, transportation provider information per ride.
- Return ride: book during the initial request, or request on demand ("I'm Ready" button; vendor states driver should arrive within one hour — product-specific claim, kept here).
- "Where's My Ride?" real-time tracking: ride status, provider name, ETA, map with driver's current location updating as the driver moves.
- Special requests: additional passenger (caregiver), wheelchair-accessible vehicle.
- GMR (gas mileage reimbursement) claims submitted in the app: "I'm Leaving" / "I'm Here" buttons; location matched against the doctor's location; reimbursement submitted after location verified for all legs. "No more paper trip logs."
- Rule: changes to already-scheduled rides require calling the health plan's transportation line (self-service covers request/status/cancel only) — product-specific.

**Broker-side technology (MTM Link as platform):**
- "Automated Trip Scheduling and Optimization: intelligent routing algorithms to match members with the most efficient transportation option."
- "Real-Time GPS Tracking" for plans/agencies; "GPS tracking ensures rides occur as scheduled, reducing fraud, waste, and abuse."
- "Member and Medical Facility Portals: self-service portals allow members and healthcare facilities to book, modify, and track trips in real time."
- "MTM Link Driver App: transportation providers use our mobile app for real-time trip management, turn-by-turn navigation, and instant ride verification."
- "Data Analytics and Reporting: in-depth performance insights."
- Cloud-based "peer-to-peer dispatching" combined with GPS tracking; system "automatically detects and adjusts for issues like traffic or vehicle breakdowns without disrupting service"; proprietary algorithm predicts demand from historical/future trip data, utilization patterns, projected pick-up times and delays.
- Dashboards: "trip activity, including scheduling, routes, member communication, payment, and driver feedback"; insights into "costs, service levels, driver documents and credentials, utilization rates, and member trends."
- FWA: "real-time GPS tracking and electronic trip verification processes confirm that rides occur as scheduled, eliminating fraudulent billing for unfulfilled trips"; anomaly detection ("excessive trip requests or unusual routing patterns"); "routine audits and provider credentialing."
- Call center: 600+ agents, 21 states, "13.5 million calls annually" (vendor marketing claim — layer A for the existence of a large call-center channel, not for the precise numbers).

**Provider network composition (service-providers page):**
- Commercial transportation providers ("the backbone of the network"; companies with multiple drivers and vehicles, contracted).
- Independent Driver Providers (IDPs) — VeyoRide rideshare drivers (own vehicle, gig model, healthcare-credentialed: first aid, CPR, HIPAA, ADA, patient sensitivity, hand-to-hand service).
- Community Volunteer Drivers — volunteers reimbursed for mileage.
- (HCBS providers — non-transportation adjacent service line.)
- Transportation providers "Log into MTM Link to access your trips."
- Driver standards: "strict healthcare standards... ADA education; CPR certification; and HIPAA, sensitivity, and medical needs training... drug testing and multi-level background checks."

**Facility-side intake (healthcare-providers page):**
- Medical facilities book trips online (facility portal registration form).
- Community Outreach team trains facility staff on "the trip intake process and MTM's self-service trip management tools"; scheduling assistance around "routine and life sustaining appointments."
- Standard forms: **Level of Need** form; **Certificate of Transportation Services** (Illinois only); **Physician Certification Statement** (Illinois only); **Medical Necessity** (medically necessary attendant); **Parental Consent**; Holiday Schedule; Inclement Weather; Distance Verification. State-specific facility forms for CT, ID, IA, MN, MO, NV, northern MN, RI, TX — the program is administered state by state.

**Level of Need (LON)** is a form the facility completes — evidence that the passenger's assistance/mobility level is a recorded attribute that shapes the trip (layer A for existence of the form; the classification scale itself not documented on fetched pages).

## Product B — RouteGenie — provider all-in-one + Broker Edition

### Key observations

**Provider edition (root + scheduling + billing pages):**
- "Modern software for non-emergency medical transportation providers, built to improve scheduling, billing, routing, and dispatching processes."
- Daily-challenge vocabulary: "vehicle breakdowns, traffic problems, cancelations, driver call-offs, will calls, no shows, add-on trips, on-demand trips."
- Modules: DispatchGenie (real-time adjustments; "find the best vehicle for every passenger, look for multiload opportunities"), BillingGenie (electronic billing files "like 837P files and CMS 1500 forms"; paper invoices; payment tracking), ImportGenie ("transportation providers receive trip requests from a variety of sources, including brokers and private pay customers"; real-time integrations), FleetGenie ("keep your vehicles properly inspected, insured, and certified with all of your payers"), Pre-RouteGenie ("builds the most efficient schedules every day based on vehicle capacity"), NoShowGenie ("automated calling system sends out calls a day in advance and the day of the trip"), DriverGenie App ("guides your drivers through their days, giving them a real-time connection with your dispatchers... pre and post-shift checklists... collect payments right from the app"), CustomerGenie App ("passengers... book and track rides, communicate with drivers when they're in route, rate their experience, and edit any upcoming trip details"), HRGenie (hiring documents, time sheets, commissions, license renewals).
- Scheduling: "find the best vehicle and driver for every passenger"; "schedule trips ahead of time so they can be dispatched on time"; "pinpoints the best pick-up and drop-off windows for every trip"; multiloading; GPS tracking; real-time dispatcher↔driver communication; web-based, any device.
- Billing: attestations ("syncs with your payer... automatically identifies which trips were completed and which were not"); clearinghouse integration (claim status, remittance file uploads); "identifies which medical codes are needed for every trip"; "generate dozens of billing templates to fit your broker's specifications"; paper/PDF invoices, CMS 1500; EDI transactions; "track the status of every trip including claim status, claim issues, and payments"; HIPAA-compliant.
- Payer plurality: "NEMT businesses deal with multiple payers. These insurance companies have different requirements that NEMT providers have to correctly meet when they submit a claim... Create HIPAA-compliant electronic billing files for every payer, including Medicaid."
- Private pay: "integrated private pay function" (testimonial); "trip requests from... private pay customers."
- Adjacent variants: PACE software page; non-emergency ambulance variant pages (routing/client app/fleet/scheduling/broker integration/driver app/dispatch/billing/management); paratransit software page; Uber Health partnership (2026 blog: "bring Uber's rideshare network into its medical transportation platform... giving 600+ fleets, health systems, and health plans on-demand rides alongside their own vehicles and contracted providers"); hospital discharge transportation blog ("a discharge call is urgent because a patient got better, and the bed now belongs to someone else... makes discharge transportation its own category of NEMT").
- Customer base (testimonials): cab companies, medical transport companies, PACE organizations, school-bus company (JusTranzit), courier — the software serves NEMT-shaped operations regardless of vehicle heritage.

**Broker Edition (broker page):**
- "A cutting-edge software platform for non-emergency medical transportation brokers developed to simplify brokers' scheduling, credentialing, and billing duties."
- Subcontractor trip management: "versatile trip assignment automation scenarios: assign all trips for a passenger to a specific subcontractor, assign all trips that are part of a single standing order to a subcontractor, or... assign all trips individually each day based on efficiency."
- **Trip turnback**: "If a subcontractor cannot handle the trip load, RouteGenie supports the trip turnback function to release trips back to the broker."
- Subcontractor portal: providers "manage their areas of responsibility, service hours, and capacity."
- Trip completion: subcontractors "complete trip data manually. Essential fields are required to mitigate human error... maintaining accurate billing records."
- Trip import/export: "Subcontractors can import trip rosters to the software of their choosing and upload trips in bulk once completed."
- Credentialing: "Review of completed profiles, approval of qualified drivers, and submission of correction requests have all gone digital"; "smart validation fields"; "automatically deactivate the driver or vehicle once their certifications expire"; "Automatic reminders... (CPR, HIPAA, vehicle insurance, etc.)... RouteGenie will not authorize non-compliant drivers and vehicles until certifications are up-to-date"; electronic credentialing for subcontractor onboarding.
- Eligibility: "Streamlined Client Eligibility Management... automate verification and handle various benefits and plans by electronically exchanging member enrollment data through HIPAA 834 file uploads. Live eligibility verification is conducted via EDI 270/271 transactions."
- No-show verification: "If a passenger misses the trip, the broker NEMT scheduling software will automatically document the no-show. This verification process is essential for future dispute resolutions."
- Trip data for audits: "collects and stores essential trip data like GPS tracking, timestamps, and route details. Any audit or complaint resolution will be backed by precise and auditable data confirming every trip completion."
- Subcontractor reimbursement: "Customizable Rate Structures... Each subcontractor can benefit from flexible rate structures"; "Trip Confirmation for Accuracy... verify the details of each trip before processing payments"; "brokers can batch and submit subcontractor invoices automatically or manually" per billing cycle; "automatically determines the subcontractor's reimbursement."
- Passenger app + communication: view trip details, live updates (vehicle location, ETA, trip progress), feedback/rating of drivers and contractors; automated trip reminder system (voice calls); text-message and WhatsApp notifications.
- **Standing order** concept appears ("all trips that are part of a single standing order") — recurring trip authorization generating multiple trips.

## Product C — TripMaster (CTS Software / Transit Technologies) — provider suite with paratransit heritage

### Key observations

- "TripMaster provides efficient, cost-effective NEMT software, demand-response, and paratransit software for public and private transit agencies."
- Module list: Automated Scheduling; Reservation Management; Mobile Data Terminals; Automated Vehicle Location; Mapping; Reporting and Billing; Interactive Voice Response; **Trip Broker Integration**; Rider Portal; Rider Ticketing; Vehicle Maintenance Module; Camera Solution; Microtransit; Intelligent Voice Assistant.
- Sectors: NEMT, Public Transit, PACE, Senior Living Communities, Healthcare.
- "A Premier Broker Partner": "the only software product to be named a Premier and Preferred Partner by three of the leading trip brokers; ModivCare (formerly LogistiCare), Alivi, and OneCall" — evidence of the broker→provider software integration market (providers run their own software and integrate with brokers' systems).
- "complete auditing support, manpower and vehicle resource management, cost control, payroll tracking, route management, statistical reporting, computer-assisted scheduling, electronic billing."
- Rider app + rider portal + IVR — passenger self-service and phone channels.
- Customer quotes: county transportation (Mitchell County NC), United Transit System — public/nonprofit transit operators running NEMT workloads.

---

## Cross-product Comparison

| Dimension | MTM Link (broker pole) | RouteGenie (provider + broker) | TripMaster (provider/transit) | Layer |
|---|---|---|---|---|
| Passenger of record | member (Medicaid/Medicare) with portal/app account; special needs captured | client eligibility managed via 834 enrollment + 270/271 live verification | rider portal/app accounts; reservation management | B |
| Trip as unit of work | ride request with date, pickup, drop-off, return; status; provider info | trip with pickup/drop-off windows, vehicle/driver assignment, legs ("all legs of your ride" at MTM) | reservations/trips; computer-assisted scheduling | B |
| Healthcare binding | rides to medical appointments (dialysis, PT, behavioral health); facility books for patients | trips to/from healthcare visits; hospital discharge category | healthcare sector; PACE; senior living | B |
| Mode / accommodation | sedan, rideshare, public transit, WAV, non-emergency ambulance, stretcher; caregiver passenger | "best vehicle and driver for every passenger" based on needs | Wheelchair Guardian module | B |
| Intake channels | member portal/app, call center, facility portal | broker feed (ImportGenie), private pay, passenger app | IVR, rider portal, broker integration | B |
| Scheduling & routing | automated scheduling + optimization, intelligent routing, demand prediction | automated schedule building, multiloading, pick-up/drop-off windows | computer-assisted scheduling, mapping | B |
| Dispatch & tracking | cloud peer-to-peer dispatching, GPS, auto-adjust for traffic/breakdowns | DispatchGenie real-time adjustments; GPS; dispatcher↔driver comms | AVL, mobile data terminals, mapping | B |
| Driver surface | MTM Link Driver App (trip management, navigation, ride verification) | DriverGenie (checklists, navigation implied, payments, dispatcher link) | mobile data terminals | B |
| Exceptions | traffic, vehicle breakdowns auto-handled; will-calls mentioned | add-ons, on-demand, will calls, no-shows, cancellations, driver call-offs, breakdowns | (implied by demand-response heritage) | B |
| No-show machinery | electronic trip verification (FWA framing) | NoShowGenie reminder calls; automatic no-show documentation for disputes | (not evidenced on fetched pages) | A (RouteGenie) |
| Provider network mgmt | commercial providers + IDPs + volunteer drivers; credentialing standards | subcontractor portal, credentialing, auto-deactivation, turnback | broker partnerships (ModivCare/Alivi/OneCall) | B |
| Money loop | payment insights; GMR mileage reimbursement claims in app | 837P/CMS-1500 claims, broker billing templates, clearinghouse, attestations, claim status; subcontractor invoicing/reimbursement | electronic billing, reporting and billing | B |
| Compliance | driver credentialing (ADA/CPR/HIPAA/sensitivity), FWA monitoring, audits | credential validation, expiry reminders, deactivation, audit-grade trip data | auditing support, vehicle maintenance | B |
| Analytics | dashboards: trip activity, costs, service levels, utilization, member trends | filtering/reporting by driver/vehicle/location/trip type | statistical reporting, custom reporting | B |
| Variants | VeyoRide rideshare fleet; mileage reimbursement; HCBS/SDOH adjacent lines | PACE, non-emergency ambulance, paratransit, Uber Health rideshare augmentation | paratransit, microtransit, public transit, senior living, rider ticketing | A |

### What is shared (candidate canonical structure)

1. A persistent **passenger/member record** carrying identity plus transportation needs (mobility/assistance level, accommodation requirements) — the subject every trip is for.
2. The **trip** as the managed unit of work: a scheduled non-emergency journey binding the passenger to pickup and drop-off (commonly residence ↔ healthcare facility) at times tied to healthcare appointments, with a required mode/accommodation, advanced through request → scheduled → dispatched → performed → completed.
3. A **managed fulfillment network**: vehicles/drivers/providers (own fleet and/or contracted subcontractors and/or rideshare augmentation) held as schedulable, credentialed resources to which trips are assigned and dispatched, with day-of exception handling.
4. The **completion-to-payment loop**: completed trips are verified (timestamps, GPS, attestations, no-show documentation) and resolved into money — claims to payers, billing files to brokers, invoices to facilities/private pay, reimbursement to subcontractors or members.

### What varies (candidate L2)

- Who runs the system: broker (administers a program, subcontracts fulfillment) vs transportation provider (operates fleet, receives trips from brokers) vs transit agency (paratransit heritage running NEMT workloads).
- Funding substrate: Medicaid/Medicare program claims, broker-specific billing templates, facility contracts, private pay, member mileage reimbursement.
- Mode mix and rideshare augmentation.
- Regional program rules (state-specific forms/rules in the US sample).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

Four jointly-held structures:

1. **The passenger of record with transportation needs** — a persistent identified passenger (member/patient/rider) whose recorded mobility/assistance needs and eligibility context shape every trip. Remove → anonymous ride booking (ride-hailing/taxi dispatch territory).
2. **The trip as the unit of work** — a scheduled, non-emergency journey for that passenger between specified locations and times (commonly home ↔ healthcare appointment), carrying a required mode/accommodation, advanced through a request→scheduled→performed→completed lifecycle. Remove → fleet tracker or dispatch board with nothing to fulfill.
3. **The managed fulfillment network** — vehicles/drivers/providers held as schedulable, credentialed resources (own fleet and/or contracted network) to which trips are assigned and dispatched. Remove → a booking site with no operation.
4. **The completion-to-payment loop** — trip completion verified and recorded (timestamps/GPS/attestation; no-shows documented) and resolved into reimbursement (claims/invoices/billing files to payers, brokers, facilities, or private pay). Remove → dispatch operation with no economic loop.

Jointly-held load-bearing:
- 1 alone = passenger CRM
- 2 without 1 = anonymous ride bookings
- 1+2 without 3 = booking site with no fulfillment
- 1+2+3 without 4 = dispatch operation with no revenue loop
- 2+3 without 1 = anonymous dispatch
- 1+3 without 2 = fleet/provider management
- 2+4 without 1+3 = billing shell

Anti-overfit notes:
- **Medicaid/Medicare machinery is NOT definitional.** Private-pay NEMT exists (RouteGenie documents "private pay customers" and an "integrated private pay function"); facility-contracted transport (hospital discharge) exists. The L0 concept is the passenger-with-needs + trip + network + payment loop; the *program benefit* is the dominant funding realization, not the invariant.
- **Healthcare-appointment binding** is held as the Type's purpose (transportation administered for healthcare/health-related service access), but the L0 wording is "scheduled non-emergency journey for a passenger with recorded needs," with the healthcare purpose carried in the trip's typical content — because MTM's own adjacent lines (SDOH/community services) extend destinations beyond clinical appointments.
- **Broker structure is NOT definitional.** The broker pole (MTM) and the provider pole (RouteGenie, TripMaster) are two postures of one Type: the same four structures appear with the broker as network manager or the provider as network owner.
- **Specific modes are NOT definitional** (sedan/WAV/stretcher/ambulance/rideshare/transit all observed as alternative realizations of "mode/accommodation requirement").
- **US program machinery (834/270/271, 837P, CMS-1500, state forms) is NOT definitional** — it is the dominant regional realization of eligibility and billing.

### L1 — Common Mature Structure

- Multi-channel trip intake: call center, member portal/app, facility portal, broker feed, IVR.
- Automated scheduling/optimization: route building, multiloading, pick-up/drop-off windows, demand prediction.
- Real-time dispatch with GPS/AVL; driver app (manifest, navigation, status updates, ride verification, sometimes payments).
- Member-facing tracking ("where's my ride"), reminders/notifications (calls, texts).
- Standing orders / recurring trips.
- No-show and will-call handling; no-show documentation for disputes.
- Provider credentialing and compliance monitoring (licenses, insurance, training; expiry-driven deactivation).
- Reporting/analytics (on-time performance, utilization, costs).
- Mileage reimbursement (member self-transport reimbursement) as an alternative trip form.
- Vehicle maintenance/fleet modules.

### L2 — Variant / Optional Structure

- Operator posture: broker-operated program vs provider-operated fleet vs transit-agency (paratransit heritage) operation.
- Funding substrate: Medicaid/MCO claims, Medicare Advantage supplemental benefit, broker billing templates, facility contracts (hospital discharge), private pay, member mileage reimbursement.
- Mode mix: sedan / wheelchair-accessible / stretcher / non-emergency ambulance / public transit / rideshare augmentation.
- Population programs: PACE, senior living communities, HCBS/SDOH-adjacent services.
- Regional rules: state-specific forms and requirements (US); program rules vary by payer contract.
- Rideshare/IDP network augmentation; volunteer driver programs.

### L3 — Vendor-specific (research notes only)

- MTM: VeyoRide IDP model (acquired Veyo 2022), call-mining platform, Navigator Line, IVA systems, per-plan user-guide split ("migrated"/"non-migrated" plans), specific health-plan client list, marketing metrics (600+ agents, 13.5M calls/yr, 95%+ satisfaction, "lowering NEMT costs by up to 25%").
- RouteGenie: Genie-branded modules (DispatchGenie, BillingGenie, ImportGenie, FleetGenie, Pre-RouteGenie, NoShowGenie, DriverGenie, CustomerGenie, HRGenie), Uber Health partnership (2026), WhatsApp notifications, marketing metrics (98% fewer unbilled claims, 25% more trips, 25–30% fewer no-shows, "6 hours to 45 minutes" scheduling).
- TripMaster: Wheelchair Guardian, camera solution, rider ticketing, intelligent voice assistant, Premier/Preferred partner badges (ModivCare, Alivi, OneCall), two-week fee waiver.
- MTM product-specific rule: changes to scheduled rides require phone call; "I'm Ready" will-call return ride with one-hour arrival expectation.

## Boundary Findings

1. **vs EMS Operations Platform.** EMS = emergency response incidents + clinical care documentation (ePCR) + crewed medical units. NEMT = scheduled non-emergency journeys with no clinical care documentation. Non-emergency ambulance/stretcher transport is a *mode inside NEMT* (transport without emergency response); the EMS pass itself recorded that "a pure NEMT broker platform... is a different Type." Remove the emergency-response/clinical pole from EMS and you get NEMT; add it to NEMT and you get EMS territory.
2. **vs Ride-hailing Platform.** Ride-hailing: open public, on-demand, no eligibility, no appointment binding, per-ride consumer payment. NEMT: closed eligible/registered population, scheduled (with on-demand exceptions), healthcare-purpose binding, program/broker/facility-funded. Rideshare fleets can *fulfill* NEMT trips (VeyoRide, Uber Health) — the population/eligibility/program-billing structure is the boundary, not the vehicle or the app form.
3. **vs Paratransit / demand-response transit.** Shared scheduling/dispatch machinery (TripMaster explicitly serves both; RouteGenie ships a paratransit page). Boundary: paratransit serves the transit agency's general eligible public under transit rules; NEMT serves healthcare access under health-program rules with program billing. Same machinery, different program wrapper — held as adjacent Types sharing a software lineage, not one Type.
4. **vs Employee Transportation Platform.** Employer-admitted workforce population, commute purpose, employer-funded. NEMT: patient/member population, healthcare-access purpose, program-funded. (Sibling structure, different population and purpose.)
5. **vs School Transportation Management.** Student population, school-calendar recurring routes. Different population/purpose; shared route/scheduling machinery.
6. **vs Fleet Management System.** Fleet management holds vehicles as assets (maintenance, telematics, utilization). NEMT holds *trips* as the unit of work; fleet/maintenance appears as a module (FleetGenie, TripMaster Vehicle Maintenance Module), not the Type.
7. **vs Dispatch Management.** Generic dispatch machinery (assignment, status, routing) is a component inside NEMT. NEMT adds the passenger-with-needs record, eligibility gating, mode/accommodation semantics, and program billing.
8. **vs TMS / freight.** Freight movements vs passenger journeys; different objects entirely.
9. **vs Patient Scheduling.** Patient scheduling owns the clinical appointment; NEMT owns the ride bound to the appointment time. The trip references the appointment but does not manage it.
10. **vs Prior Authorization Platform.** Trip-level authorization (e.g., physician certification for certain modes) is a rule inside the NEMT trip lifecycle; the PA Type is payer-side pre-service coverage machinery across medical services generally.
11. **vs Taxi Dispatch Platform.** Some NEMT providers are cab companies (RouteGenie testimonials), but taxi dispatch is public on-demand hailing without eligibility/program structure. The NEMT program wrapper is the boundary.

"去掉什么就变成另一个 Type" 判据:
- 去掉 passenger-with-needs 记录（匿名乘客）→ ride-hailing / taxi dispatch。
- 去掉 scheduled non-emergency 生命周期（改为应急响应 + 临床记录）→ EMS operations。
- 去掉 healthcare/program 目的与计费（改为通勤）→ employee/school transportation。
- 去掉 trip 单元（只管车辆资产）→ fleet management。
- 去掉 fulfillment network（只做资格与请求转发）→ prior-authorization/benefits territory。

## Historical / Market-Sample Check (§24)

- Paper-era realization: a county/program office with a phone-based scheduler, paper passenger files recording needs, trip tickets/manifests, a roster of contracted cab companies with credential files, mileage-reimbursement forms, and invoices to the program — satisfies all four L0 legs with no software. The Type is not defined by apps/GPS/algorithms.
- Transit/paratransit heritage: TripMaster's demand-response/paratransit lineage and RouteGenie's cab-company customers show the scheduling/dispatch machinery is shared with older demand-response operations; the NEMT-specific layer is the passenger-needs + program-eligibility + program-billing wrapper.
- Regional check: the fetched sample is US-centric (Medicaid/Medicare vocabulary). Non-US patient-transport services (e.g., UK patient transport service scheduling, Australia community transport) plausibly fit the same four-leg shape, but no non-US official documentation was fetched — recorded as an uncertainty; the L0 definition is written region-neutral (no US program machinery in the invariant).
- Older broker generation (LogistiCare-era) referenced by TripMaster's partnership page (ModivCare "formerly LogistiCare") — the broker posture predates current apps; fits.

## Uncertainties

1. Second broker-operator pole (Modivcare) not fetched — broker-side observations rest on MTM + RouteGenie Broker Edition; broker-posture commonality is B-layer across two sources, acceptable but thinner than the provider side.
2. RoutingBox and WellRyde unreachable — provider-side sample breadth limited to RouteGenie + TripMaster.
3. Exact trip-state vocabularies (state names per product) not documented on fetched pages — lifecycle written conceptually; no precise state lists claimed.
4. Level of Need classification scale contents not documented (form existence confirmed only).
5. Non-US NEMT/patient-transport software not sampled — regional generality of the L0 asserted at C-layer inference only.
6. Whether trip *leg* is a first-class object in all products: MTM's GMR flow references "all legs of your ride"; RouteGenie references legs implicitly via multiloading/pickup-dropoff windows. Leg-level modeling held as common implementation, not invariant.
7. Prior-authorization-style trip gating (e.g., PCS forms) observed as forms at MTM (Illinois-specific); how widely software encodes this as workflow gates is not evidenced.

## Final Synthesis

A Non-emergency Medical Transportation Platform is the system of record for scheduled, non-emergency medical transportation: it holds the passenger of record with transportation needs, manages trips as the unit of work (request → eligibility/needs → schedule/assign → dispatch → perform → verify → bill), orchestrates a credentialed fulfillment network (own fleet and/or contracted providers and/or rideshare augmentation), and resolves completed trips into reimbursement against the funding program (payer claims, broker billing, facility contracts, private pay, member mileage reimbursement). The Type has two dominant postures — broker-operated program platforms and provider-operated fleet platforms — plus a transit/paratransit heritage posture; all realize the same four jointly-held structures. Medicaid/Medicare machinery, specific modes, rideshare augmentation, and US forms are dominant realizations, not invariants.
