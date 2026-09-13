# Research Notes — Airline Crew Management

## Research Goal

Understand what an Airline Crew Management application really is from real products: what objects exist inside it (crew, pairings, duties, rosters, qualifications), who uses it, how legal crew assignment is built and maintained from planning through the day of operation, and where its boundary lies against airline operations platforms, generic employee scheduling, training systems, and time & attendance.

## Initial Boundary

- Hypothesis going in: crew management is the airline-side system that turns a published flight schedule into legal, published crew rosters and keeps them working on the day of operation.
- Likely operators: airline crew planning / crew control departments; crew members as self-service users; training and records staff.
- Nearest neighbors: Airline Operations Platform (broader OCC scope), Employee Scheduling Platform (generic shifts), Workforce Management for Contact Centers (interval demand), Flight Planning Application (aircraft-side dispatch), Corporate LMS / Training Management (training delivery), Time & Attendance (actuals).
- Unknowns going in: exact object model (pairing vs duty vs roster); how legality is computed and when it is checked; how bidding/trading works; how disruption recovery works; whether pay integration is part of the Type; how small operators and business aviation differ from large network carriers.

## Research Questions

1. What are the core objects — pairing, duty, roster, qualification — and how do they relate?
2. What does "legality" cover (duty/flight-time limits, rest, qualification currency) and when is it checked (planning, assignment, day-of-ops)?
3. What is the two-stage planning pipeline (pairing → rostering) and when is it absent?
4. How do crew members interact with the system (bidding, trading, mobile roster, notifications)?
5. What happens during disruption (IROPS): detection, recovery, re-assignment?
6. How are training and qualifications managed relative to the roster?
7. How does the roster relate to pay/time data? (evidence check)
8. How do products split planning (mid-term) vs tracking (day-of-ops)?
9. What differs between network carriers, LCCs, and business aviation?
10. Where is the boundary vs Airline Operations Platform and vs generic Employee Scheduling?

## Representative Products

| Product | Vendor | Why selected |
|---|---|---|
| Jeppesen Crew Solutions (Crew Pairing / Crew Rostering / Crew Tracking / Fatigue Risk Management / Manpower Planning) | Jeppesen (Boeing) | Enterprise market standard; optimization-led philosophy; full module suite documented publicly |
| Flightscape Crew Management (Crew Planner / Crew Manager / Training / Crew Access / Crew Engagement) | CAE | Enterprise competitor; AI/ML and recovery-led philosophy; crew self-service apps |
| iFlight (Airline Operations incl. Crew Planning & Crew Management) | IBS Software | Carrier-side platform packaging; enterprise + mid-market (iFlight Core) tiers; Lufthansa crew-ops case |
| FL3XX (Crew module) | FL3XX GmbH | Business-aviation/charter segment; crew scheduling as one module of an all-in-one ops platform; live-check philosophy |

Rejected/abandoned samples: Sabre AirCentre Crew (current sabre.com no longer documents the crew line; legacy product URL returns 500; archive fetch timed out), NetLine/Crew (Lufthansa Systems site unreachable), Merlot Aero, AIMS, PDC Aviation (all unreachable). Recorded under Source-access Limitation.

## Sources

Fetched 2026-09-06 (all official vendor pages):

- Jeppesen — Crew Solutions overview: https://ww2.jeppesen.com/airline-crew-optimization-solutions/
- Jeppesen — Crew Pairing: https://ww2.jeppesen.com/airline-crew-optimization-solutions/airline-crew-pairing/
- Jeppesen — Crew Rostering: https://ww2.jeppesen.com/airline-crew-optimization-solutions/crew-rostering/
- Jeppesen — Crew Tracking: https://ww2.jeppesen.com/airline-crew-optimization-solutions/airline-crew-tracking/
- CAE — Flightscape Crew Management: https://www.cae.com/civil-aviation/aviation-software/flightscape/crew-management/
- IBS Software — Airline Operations (iFlight): https://www.ibsplc.com/product/airline-operations-solutions
- IBS Software — corporate overview (platform framing): https://www.ibsplc.com/
- FL3XX — platform overview: https://www.fl3xx.com/
- FL3XX — Crew module: https://www.fl3xx.com/product/crew

Unreachable (1–2 attempts each, then abandoned): sabreairlinesolutions.com (500), sabre.com crew product pages (404 / not listed), lufthansa-systems.com (transport error), merlot.aero (timeout/transport), aimsinc.aero (transport), pdc.aero (transport), leon.aero (empty JS shell), web.archive.org (timeout).

## Product A — Jeppesen Crew Solutions (Boeing)

### Key observations (evidence layer A unless noted)

- Suite framing: "Jeppesen Crew Management System" — six solutions operating "as one comprehensive ecosystem": Crew Pairing, Crew Rostering, Crew Tracking, Fatigue Risk Management, Manpower Planning (+ product training). "From long-term planning through day of operation." Positioning: staff are "an airline's greatest expense behind fuel".
- **Crew Pairing**: creates "cost-effective, optimized and **anonymous crew itineraries**" via a "market-leading optimization engine". User-controlled parameters; planners configure "rules, reports, data interfaces and cost drivers". Handles "multiple crew bases, variable crewing, various agreements, numerous flights and diverse aircraft types". What-if simulations "for timetable analysis, crew base assessments and negotiations". "Hotel forecasting" and inputs to manpower planning. "Fatigue-model integration … during the planning phase". SaaS with on-prem option; "seamlessly integrates with your existing crew management system". Claimed "cost savings or operational efficiency gains of 3% to 15%" (vendor claim, not independently verified).
- **Crew Rostering**: monthly roster construction "considering legality, crew availability, training, reserves, crew preferences, and other critical factors". Optimizers allow roster construction "closer to the day of operation". Rosters "respect regulation and union rules, considers pre-assignments, meets training requirements, and maximizes stability and bid satisfaction". Handles "standbys, training, qualifications and visa requirements, with preferential bidding enabling crew influence". Bid models: "weighted fair share, strict seniority (points or bid groups), or lifestyle". Integrates with complementary modules to form the Crew Management system.
- **Crew Tracking**: day-of-operations recovery. "Detecting, resolving and following up on changes to the originally published crew plans." **Alert Monitor** surfaces problems "such as crew members with short connections, missed check-ins or crew missing passports". **Tracking Editor**: "view, analyze, and adjust trips and rosters while legality checking runs instantly and automatically". Recovery options and what-if scenarios "based on your key performance objectives". "Flexible rules engine allows you to configure the system to match your business rules". Works with Crew Rostering and Crew Pairing. A "Crew Exchange" customer-story PDF is linked from the page (trip-trading product exists in the portfolio; details not fetched).
- Fatigue Risk Management and Manpower Planning exist as named modules (pages not fetched; names and placement only).

## Product B — CAE Flightscape Crew Management

### Key observations

- Suite framing: "end-to-end crew management ecosystem"; AI/ML-powered resource planning; "optimize schedules, forecast crew resources, maintain safety standards, and recover from disruptions".
- **Crew Planner**: "pairing optimizer … reduce crew costs while improving the quality of life for your crew members"; "roster optimizer … improves crew utilization, ensures the appropriate distribution of duties … while ensuring compliance with **regulatory and company rules**".
- **Crew Manager**: "unified, powerful workspace to manage crew operations, especially in times of turmoil. Recover from **crew IROPS** … using our powerful crew recovery engine. This one-step solution will fix broken pairing and re-assign flights accordingly." Simulated plans "based on forecasted disruption or cancellation packages". "**Open Time Solver** technology … automating your daily crew scheduling tasks. Scalable, configurable and respectful of **labour and legal policies**."
- **Crew Manager Training Solution**: "optimally schedule and track all aspects of crew training … ground training, flight training & recencies, simulators, and external training."
- **Crew Access**: mobile app; "real-time cloud-enabled information about their roster schedule"; chat feature for crew communication.
- **Crew Engagement**: RosterBuster crew app ("over 400,000 users globally and over 500 airlines currently supported" — vendor claim) — crew "connect to their airline operations, communicate among crew, sync and share their busy schedule"; RB Logbook (digital pilot logbook).
- Related modules on the same platform: Operations Control, Flight Management, Airport Management, In-Flight Services Management, Training Management — crew management is one pillar of a flight-ops suite.

## Product C — IBS Software iFlight (Airline Operations)

### Key observations

- Platform framing: "Covering the full spectrum from fleet planning all the way through to **crew optimization and tracking**, the iFlight platform is comprised of different modules that enable end-to-end airline operations and crew management." Menu: "Flight Operations | Crew Planning | Crew Management | Hub Management | MRO".
- Two tiers: iFlight "For Large / Enterprise Carriers" and iFlight Core "For Small & Mid-Sized Airlines / LCCs".
- OCC framing: operations control centers are "siloed, manual, and reactive"; iFlight provides "real-time dynamic situational awareness", "early warning indicators flag potential irregular operations and automate proactive and cost-aware disruption management".
- **Lufthansa case study**: "Crew member allocation and deployment at Lufthansa used to run on a highly complex patchwork of new and legacy systems … replacing the entire platform was key" — evidence that crew allocation/deployment is a platform-scale replacement project at flag-carrier scale.
- White paper: "Scenario-planning for crew pairing optimization" — "Crew planning and optimization are central to any airline's operations, cost management, and customer service delivery … complex, **cost-aware, and legally compliant** decisions … at the planning stage or adapting to last-minute changes."
- Crew training: ebook on "crew training challenges" — Training Management System capabilities: "dynamic scheduling and automated compliance tracking … grading, real-time feedback" for "pilots and crew".
- Customers shown: Air Canada, British Airways, China Southern, Copa, easyJet, Emirates, Etihad, FedEx, Garuda, JAL, KLM, LATAM, Lufthansa, Malaysia, Qantas, WestJet (marquee logos).

## Product D — FL3XX (Crew module, business aviation)

### Key observations

- Platform framing: "charter sales, flight dispatch, crew scheduling, maintenance visibility, post-flight workflows, and reporting … one live view of the operation." Crew is one module among Sales/Crew/Dispatch/Maintenance/Docs/Reporting.
- Scheduler side: "Assign crew in seconds, with **live checks on flight time, duty, and rest**"; "See **licenses, training, and upcoming expiries** — all in one place"; "Approve leave or adjust rosters without scrambling future flights."
- Crew side (app): "Schedules, duty, and training status are always up to date, right in the app"; "Receive instant updates on flight status and services"; "Time off requests happen in a tap."
- Compliance: "qualified and achieved **FTL compliance** across EMEA, APAC, and Americas" (flight-time-limitation rules configured per region).
- Integrations: 180+ integrated services including crew services (training providers, logbook services, crew dosimetry, compliance tools).
- No pairing optimization, no bidding, no reserve pool mentioned — crew are assigned per trip/flight with live legality checks. This is the structural contrast with the airline suites.

## Cross-product Comparison

| Dimension | Jeppesen | CAE Flightscape | IBS iFlight | FL3XX |
|---|---|---|---|---|
| Crew register with qualifications | qualifications, visas (rostering) | training/qualifications tracked | training compliance tracking | licenses, training, expiries |
| Flight schedule as demand | "numerous flights", timetable what-ifs | forecast crew resources vs demand | fleet planning → crew optimization | trips/flights in one platform |
| Legality checking | instant & automatic in tracking; rules in pairing/rostering | regulatory + company rules; labour & legal policies | "legally compliant" decisions | live checks on flight time, duty, rest |
| Pairing construction | dedicated optimizer, anonymous itineraries | pairing optimizer | crew pairing optimization (white paper) | absent (per-trip assignment) |
| Rostering | monthly rosters; reserves; pre-assignments | roster optimizer; duty distribution | crew management module | rosters adjusted without scrambling future flights |
| Bidding / preferences | preferential bidding; 3 bid models | quality-of-life objectives | (not evidenced on fetched pages) | absent; leave requests instead |
| Open time / trading | Crew Exchange (named, not fetched) | Open Time Solver | (not evidenced) | (not evidenced) |
| Day-of-ops tracking | Crew Tracking: Alert Monitor + Tracking Editor | Crew Manager: IROPS recovery engine | crew tracking; early-warning indicators | "stay ahead of the day"; instant updates |
| Training scheduling | training in rosters; meets training requirements | dedicated training solution | TMS capabilities (scheduling, compliance) | training status visible; expiry warnings |
| Fatigue tooling | Fatigue Risk Management module; fatigue-model integration in pairing | (not on fetched page) | (not evidenced) | (not evidenced) |
| Crew self-service | (portal products exist; not fetched) | Crew Access app + chat; RosterBuster | (crew apps implied) | crew app; time-off requests |
| Manpower planning | dedicated module | forecast crew resources | fleet planning linkage | absent |
| Packaging | standalone crew suite (SaaS/on-prem) | suite pillar of flight-ops platform | module of airline-ops platform (2 tiers) | module of bizav ops platform |
| Segment | network/complex airlines | airlines (large + 500-airline app reach) | enterprise + SMB/LCC | charter / bizav / air ambulance |

### Evidence layer B (cross-product commonality)

Present in all four sampled products (layer B, supports L0/L1):

- identified crew population with role and qualification data (licenses/ratings/training/visas)
- the flight schedule/trips as the demand the crew must cover
- legality checking against duty/flight-time/rest rules and qualification currency, with rules configurable per airline (regulator + union/company agreements)
- the per-crew roster as the central object, visible to the crew member
- day-of-operations tracking and adjustment when reality diverges from plan
- crew-facing mobile/self-service surface (app or portal)

Present in three of four or strongly in the airline tier (layer B, supports L1):

- pairing construction as an intermediate planning object (Jeppesen, CAE, IBS — absent in bizav)
- optimization engines for pairing and rostering (Jeppesen, CAE, IBS)
- recovery/re-planning tooling with what-if scenarios (Jeppesen, CAE, IBS)
- training scheduling integrated with the roster (Jeppesen, CAE, IBS; FL3XX shows status only)
- reserve/standby handling (Jeppesen explicit; others implied)
- open-time management / automation of daily assignment (CAE explicit; Jeppesen Crew Exchange named)

## Canonical Model (L0–L3)

### L0 — Defining Invariant

```text
Crew register (identified crew members: role, qualifications, availability)
└── Flight schedule as crew demand (flights/trips need qualified crew, positioned where the aircraft is)
    └── Legality-constrained assignment
        (duty / flight-time / rest rules + qualification currency, configurable per regulator & agreement)
        └── Per-crew roster (the crew member's published schedule of duties)
            └── Maintained through the day of operation (tracked, adjusted as the operation changes)
```

Five properties. Remove any one and the product stops being recognizable as airline crew management:

- **Crew register** — without identified, qualified crew records there is nothing to assign; the product becomes a generic shift scheduler with anonymous staffing slots.
- **Flight schedule as demand** — without flights/trips as the demand object, it is generic workforce scheduling; the demand here is aircraft rotations that move crew between stations.
- **Legality-constrained assignment** — without the aviation legality regime (duty/flight-time/rest limits and qualification currency) enforced on every assignment, it is generic employee scheduling; this is the reason the Type exists as a distinct category.
- **Per-crew roster** — without a per-individual published schedule of duties there is no roster to bid on, trade, track, or pay against.
- **Maintained through the day of operation** — without tracking/adjustment the product is a planning-only roster builder, not an operations system; every sampled product includes the day-of-ops loop.

Historical check (§24): mainframe-era crew scheduling enforced duty-time limits and produced printed rosters without optimization engines, mobile apps, bidding systems, fatigue models, or AI — the L0 chain holds for them. Business-aviation products (FL3XX) skip pairings and bidding entirely and still fit. Therefore pairing, bidding, mobile apps, fatigue models, and AI are NOT part of L0.

### L1 — Common Mature Structure

- **Pairing construction** (large scheduled airlines): anonymous multi-day duty itineraries built by an optimization engine under configurable rules and cost drivers, before individual assignment.
- **Roster optimization**: assignment of pairings/duties to individuals balancing legality, utilization, fairness, training, reserves, preferences.
- **Preferential bidding & bid models**: crew influence over roster construction (weighted fair share, seniority/points/bid groups, lifestyle bidding — Jeppesen's named models).
- **Open time & trip trading**: unassigned work pool, automated coverage (CAE "Open Time Solver"), crew-to-crew trading (Jeppesen "Crew Exchange" exists as a named product).
- **Crew self-service**: mobile app/portal with roster view, change notifications, chat/communication (CAE Crew Access, RosterBuster; FL3XX crew app).
- **Training & qualification scheduling**: training events as roster activities; recency/expiry tracking feeding assignment legality (CAE training solution; IBS TMS; Jeppesen "meets training requirements").
- **Reserve / standby management**: standby duties as roster elements (Jeppesen explicit).
- **Disruption recovery tooling**: alert monitors, recovery engines, what-if/simulation, re-assignment with instant legality checks (Jeppesen, CAE, IBS).
- **Fatigue-risk tooling**: fatigue models integrated into planning; dedicated FRM module (Jeppesen).
- **Manpower planning**: long-term crew supply vs demand forecasting (Jeppesen module; CAE "forecast crew resources").
- **Roster → downstream data**: the roster is the basis for crew pay and time accounting in the industry; **not directly evidenced in fetched pages — treated as unverified, kept out of the final document's claims** (see Uncertainties).

### L2 — Variant / Optional Structure

- Planning posture: two-stage pairing→roster pipeline (network carriers) vs direct flight-to-crew rostering vs per-trip assignment (business aviation/charter).
- Bid culture: seniority-driven bidding (common in some markets/union agreements) vs company-assigned rosters with preference input only; some operators have no bidding at all.
- Crew scope: pilots only vs pilots + cabin crew in one system (sampled suites handle both; cabin-crew scale can dominate roster counts).
- Segment: scheduled airline (network/LCC/regional) vs charter/bizav vs cargo/air-ambulance operators.
- Regulatory regime: duty/flight-time rules differ by regulator and are configured per airline/region (FL3XX: FTL compliance across EMEA/APAC/Americas; Jeppesen: "regulation and union rules"); FRMS adoption varies.
- Deployment: SaaS vs on-premises (Jeppesen offers both).
- Packaging: standalone crew suite vs module of an airline-operations platform (IBS, CAE, FL3XX) vs best-of-breed point products.
- Optimization posture: mathematical optimization engines vs AI/ML positioning (CAE) vs live-check simplicity (FL3XX).

### L3 — Vendor-specific (Research Notes only)

- Jeppesen: "anonymous crew itineraries" phrasing; ePairing I training course; weighted-fair-share bid datasheet; "3% to 15%" savings claim; Crew Exchange product name; SaaS + on-prem options.
- CAE: "Open Time Solver" branding; RosterBuster (400k users / 500+ airlines claims); RB Logbook; Crew Access chat; "one-step" recovery engine framing.
- IBS: iFlight vs iFlight Core tiering; Lufthansa platform-replacement case; Air France–KLM quote; OCC "dynamic situational awareness" framing.
- FL3XX: 180+ integrations; FL3XX Chat; BRIGHT/SOURCE product names; FTL-qualification claim across regions.

## Vendor-specific Findings

See L3 above. None of these entered the canonical core. The Jeppesen savings claim and CAE user-count claims are marketing figures and are not treated as evidence of structure.

## Boundary Findings

- **vs Airline Operations Platform**: ops platforms (IBS iFlight, CAE Flightscape) sell crew management as a module; the OCC covers flight ops/dispatch/tail assignment/OCC collaboration. Structural test: remove dispatch, fuel, tail assignment, and OCC flight management and keep crew assignment/legality/rosters — still crew management; remove crew and keep dispatch — ops platform. The crew system consumes the published schedule and returns crew status; packaging overlap is real but the object sets are disjoint.
- **vs Employee Scheduling Platform (§09 HR)**: generic scheduling assigns people to shifts from demand forecasts; no aviation legality regime, no qualification currency tied to licenses/medicals, no pairing object, no flight-schedule coupling, no day-of-ops recovery against aircraft rotations. Remove the legality regime and flight demand → generic employee scheduling.
- **vs Workforce Management for Contact Centers**: interval-level demand forecasting and adherence; different demand object and different legality regime entirely.
- **vs Time & Attendance**: records actual worked time after the fact; crew management plans and assigns ahead of time and tracks the roster through the operation. Actuals feed back (post-flight) but the core object is the assignment, not the time punch.
- **vs Training Management / Corporate LMS**: crew systems schedule training events and track qualification currency as data feeding legality; the delivery of training content/grading is the LMS/TMS Type. Boundary: the crew system needs training as (a) qualification records and (b) schedulable activities; it does not deliver the training.
- **vs Flight Planning Application**: dispatch plans the aircraft's flight (route, fuel, weather); crew management plans the people. Both consume the schedule; neither replaces the other.
- **vs Airline Reservation / Passenger Service System**: passengers and itineraries vs crew and rosters; different populations, different legality regimes.
- **"去掉什么就变成另一个 Type" 判据**: remove the aviation legality regime and flight-schedule demand → Employee Scheduling; remove crew and keep flights/dispatch → Airline Operations Platform; remove assignment and keep only training delivery → Training Management; remove planning and keep only actual-time capture → Time & Attendance.

## Uncertainties

- **Roster → payroll linkage**: industry-standard and widely expected, but no fetched page stated it directly. Kept out of the final document's affirmative claims; mentioned only as unverified in these notes.
- **Exact legality parameters** (duty-hour caps, rest minima, augmentation rules): deliberately not stated; they are regulator- and agreement-specific and no source in the sample states numbers.
- **Pairing-generation mechanics** (column-generation etc.): vendor pages describe optimizers but not algorithms; not stated.
- **Bid-group mechanics details**: Jeppesen names three bid models; inner mechanics not documented in fetched pages.
- **Crew portal product specifics** (Jeppesen crew-facing products beyond Crew Exchange): not fetched; crew self-service evidenced via CAE/FL3XX instead.
- **Sabre AirCentre Crew**: could not be reached in any form; its historical existence and market position are known but not evidenced here — excluded from the sample and from the final document's product list.
- **NetLine/Crew (Lufthansa Systems)**: unreachable; Lufthansa's crew ops are evidenced via the IBS case study instead.

## Final Synthesis

An Airline Crew Management application is the airline-side operational system that converts a published flight schedule into legal, published crew rosters and keeps those rosters working through the day of operation. Its world is built on: a register of identified, qualified crew; the flight schedule as the demand for qualified crew; legality-constrained assignment under duty/flight-time/rest rules and qualification currency (configured per regulator and labor agreement); the per-crew roster as the central object, visible to the crew member; and a day-of-operations loop that detects divergence and re-assigns legally. Around this spine, mature airline products add pairing optimization, roster optimization, bidding and trip trading, open-time automation, training scheduling, reserve management, fatigue tooling, manpower planning, and crew self-service apps. The Type's boundary against generic employee scheduling is the aviation legality regime plus flight-schedule demand; against airline operations platforms it is the crew object set (pairings/rosters/legality) versus the flight object set (dispatch/tail/OCC); against training systems it is scheduling-and-currency versus delivery.
