# Research Notes — Driver Management

## Research Goal

Determine what "Driver Management" is as an Application Type. The leaf sits in DIRECTORY.md §18 (Transportation, Mobility & Logistics) between Dispatch Management and Electronic Logging Device / HOS Platform. The prior **fleet-management-system** research explicitly flagged this leaf:

> "driver records/scores/assignments are L1 inside FMS; a standalone Driver Management Type would center the driver rather than the fleet. Boundary deserves a joint pass when that leaf is processed." (research/fleet-management-system.md, Boundary Findings)

The central research question is therefore: **is Driver Management a real standalone Type centered on the driver as the managed entity, or only a capability/module of Fleet Management Systems (and of TMS/dispatch products)?** If it is a real Type, what is its minimal defining core, and where exactly does it separate from FMS, TMS, Dispatch, ELD/HOS, and generic HR systems?

## Initial Boundary

Working hypothesis before research: "Driver management" in the market has at least two readings:

1. **Capability reading** — the driver roster/assignment/score module inside a Fleet Management System, TMS, or dispatch product (confirmed by the FMS, Dispatch Management, and Courier Management research passes as L1/Common inside those Types).
2. **Standalone-Type reading** — products whose system of record is the *driver* (a person), not the vehicle or the freight: driver qualification/compliance files, license checking, driver risk management, driver training administration.

Adjacent leaves that must not absorb it: Fleet Management System, Trucking Management System, Dispatch Management, Electronic Logging Device / HOS Platform, Airline Crew Management (aviation sibling), plus HR-side types (ATS, HRIS, LMS) and the "driver app" surface of fleet platforms.

## Research Questions

1. What is the system of record — the person (driver) or the vehicle/freight? What does a driver record contain?
2. What state does the Type govern? Is there a governed "entitlement / fitness to drive" state?
3. What is the core loop: onboarding → monitoring → alert → remediation? What triggers alerts (expiries, new violations, behavior)?
4. How do checks work: periodic vs continuous record checks (MVR-class), consent/notice handling?
5. Which capabilities are common mature structure: risk scoring, training/coaching, driver self-service, vehicle coupling (company vehicles vs grey fleet), hiring intake?
6. Does a standalone product market exist that is not an FMS/TMS module? (Resolves the FMS flag.)
7. Does the Type hold under a historical check (paper driver qualification files, pre-telematics license checking)?
8. Where are the exact seams vs FMS / TMS / Dispatch / ELD-HOS / Crew Management / HR?

## Representative Products

| Product | Pole | Segment / customers | Evidence tier |
|---|---|---|---|
| Foley (foley.io, foleyservices.com) | US DOT/FMCSA compliance — driver qualification files + credential monitoring + screening | Owner-operators to large fleets; expanded cross-industry (waste, utilities, F&B, healthcare, manufacturing) | A (homepage + Driver Qualification Files product page + compliance/monitoring product structure) |
| eDriving (edriving.com, a Solera company) | Global digital driver risk management — continuous license monitoring + behavioral scoring + coaching | Large corporate fleets (sales/service/delivery drivers; 125 countries claimed) | A (homepage + Driver Risk Monitoring product page) |
| TTC Group / Continuum (thettcgroup.com; Licence Bureau is now part of TTC) | UK duty-of-care — licence checks, grey-fleet compliance, permit to drive, driver training | UK organisations incl. police, councils, construction, fleets; site section literally named "Driver Management" | A (Driver & Fleet Management section + product structure) |

Boundary poles (not members of the Type, used for the seam):
- Fleet Management System products (from research/fleet-management-system.md): driver data present as L1 module.
- Dispatch/Courier products (from research/dispatch-management.md, research/courier-management-platform.md): drivers appear as dispatchable resources; schedules/settlements live there.

Attempted but unreachable (source-access limitation): DriverReach (403 ×2), Tenstreet (403 ×2), J.J. Keller Encompass driver product page (jjkeller.com 403; jjkellersafety.com reachable but that surface documents the generic EHS suite, not the driver product), Motive driver-app page (404), Samsara driver-app page (404). The recruiting/onboarding-heavy pole of the market is therefore under-sampled; claims in that direction are kept general.

## Sources

Research date: 2026-09-07. All fetches of official vendor surfaces (Tier 1–2). No help-center article depth was fetched for any product (login-gated or unreachable); no third-party reviews were needed.

- Foley — https://www.foleyservices.com/ (redirect surface of foley.io) and https://www.foley.io/compliance/driver-files/ — product structure: Hiring & Onboarding / Compliance / Data Monitoring / Background Checks; DQF product page with create/convert/organize/maintain workflow and compliance-manager case quote.
- eDriving — https://www.edriving.com/ and https://www.edriving.com/driver-risk-monitoring/ — continuous license monitoring, risk ratings, FCRA handling, DriverINDEX, Mentor app description.
- TTC Group — https://www.licencebureau.co.uk/ (redirects to https://www.thettcgroup.com/fleet-driver-management/) — Driver Management section, Continuum platform, driver licence checks, grey fleet checks, Permit to Drive, driver training, driver app.
- Paired research (Layer B/C): research/fleet-management-system.md; research/dispatch-management.md; research/courier-management-platform.md.

## Product A — Foley

### Key observations (evidence layer A)

- Positioning: "all-in-one platform" for "compliance, safety, and screening data"; audience framed as people who "manage 5 drivers or 500"; "Foley's roots are planted in transportation" (30 years claimed); industries beyond trucking include retail/F&B, utilities & construction, waste, agriculture, healthcare, manufacturing.
- Product families: Hiring & Onboarding (candidate management, onboarding, recruiting); Compliance (FMCSA Clearinghouse TPA service, DOT Physical Management, DOT Background Checks, Drug & Alcohol Testing, MVRs, **Driver Qualification Files**); Data Monitoring (Audit Risk Monitor, **MVR Monitor**, CSA Monitor); Background Checks (pre/post-employment, verifications, criminal, social media).
- **Driver Qualification Files page** — the clearest structural evidence:
  - DQF applicability described in regulatory terms (interstate drivers, GVWR/GCWR thresholds, passenger counts, hazmat placarding) — US FMCSA regime.
  - Four-step product workflow: **Create** driver files from scratch; **Convert** paper files to electronic (including required documents such as MVR check records); **Organize** scattered electronic documents "in a single secure platform"; **Regularly maintain** — "certain documents, like medical cards, are valid [only over time]" and "Foley's software alerts you when a file is due for an update."
  - Compliance-manager persona quote: "If a CDL needs to be renewed or a driver needs his DOT physical, I can see that right from my Foley dashboard. Everything is right there in one place." — dashboard over per-driver credential status.
  - "automatically running annual MVR checks on each driver, to a comprehensive alert system that notifies you when action is required" — periodic checks + action-required alerts.
  - Industry variants: CDL trucking, delivery drivers in box trucks/cargo vans, garbage truck operators.
- MVR Monitor: "alerts you when a driver gets a new violation, license suspension, or other reportable event" — event-driven monitoring between periodic checks.
- CSA Monitor: "alerts you to crashes, inspections, and violations for every driver."
- Clearinghouse TPA: registers the company, manages **driver consent**, runs required queries, files records — consent machinery attached to the driver record.
- Hiring pole: "With just a license photo, applicants can kick off the process—letting you instantly pre-screen and identify qualified drivers" — license data drives applicant screening; the applicant becomes a driver file ("From job ad to background check to employee file").

### Type reading

Foley's center of gravity is the **per-driver file of qualification evidence and its timeliness**. Vehicles appear only as regulatory thresholds (what the driver drives), never as managed assets — no maintenance, fuel, telematics, or vehicle register in the driver product. The managed object is the person's qualification state.

## Product B — eDriving

### Key observations (evidence layer A)

- Positioning: "global digital driver risk management"; "helps organizations around the world to reduce incidents, collisions, injuries, license violations, carbon emissions, and total cost of fleet ownership through its patented digital driver risk management programs." Audience: "sales, service and delivery drivers" for large corporates; vendor claims of 2M+ drivers across 125 countries (marketing figures — vendor claims, not independently verified).
- **Driver Risk Monitoring (DRM) page** — structural evidence:
  - Explicit contrast: "While periodic motor vehicle record (MVR) checks provide coverage for a single day, eDriving's DRM service provides **coverage for 365 days!**" — continuous vs periodic monitoring is a marketed axis.
  - Baseline license check / MVR with: "license status, restrictions, suspensions, revocations and expirations"; **assignment of risk rating (Low, Med, High)**.
  - **End-to-end management of Fair Credit Reporting Act (FCRA) compliance**: distribution of federally-mandated notices, securing **drivers' consent** (digital or printed, state-dependent).
  - "Continuous monitoring of driving record for new activity"; "timely notification… of change in status or activity"; "**automatic**, subsequent MVR check to obtain details following identified activities."
  - Benefits framing: protection from liability "resulting from drivers making deliveries using suspended, restricted, revoked or expired licenses"; "80% of risk derives from 20% of drivers; identify and focus coverage on your riskiest drivers"; MVR monitoring as an insurance-rate requirement (vendor claim).
  - **DriverINDEX**: "combines MVR ratings with Mentor driver performance data for a comprehensive view of driver risk" — record-based and behavior-based data merged per driver.
- Mentor app (homepage): "identifies risky driving behaviors for intervention and safe driving habits for recognition"; in-app "micro-training and coaching, gamification, collision reporting, vehicle inspections, and an individual FICO® Safe Driving Score validated to predict the likelihood of being involved in a collision."
- Driver-facing surface: the driver is an active participant (app, training, rewards — Mentor Rewards).

### Type reading

eDriving's center of gravity is the **driver as a continuously monitored risk entity**: entitlement (license status) plus behavior (scores) plus remediation (training/coaching), with consent/notice machinery. Vehicles appear as context (vehicle inspections in the driver app), not as managed assets.

## Product C — TTC Group (Continuum)

### Key observations (evidence layer A)

- Site section literally titled **"Driver Management"** ("Welcome to the future of driver management"; "The home of driver and fleet risk management"). Licence Bureau (a well-known UK licence-check provider) is now part of TTC — evidence that licence checking is the same market.
- Duty-of-care framing (UK regime): "If you employ a driver – even if it's only one – you are responsible for making sure they're as safe as possible, **entitled to drive** and that their vehicle is taxed and roadworthy."
- Product structure:
  - **Identify driver risk**: "Dynamically profile all your drivers, identify the riskiest and positively intervene with automated tools, tasks and alerts"; driver risk assessment questionnaires; drug & alcohol screening; in-vehicle and employee data integration (telematics data imported).
  - **Manage driver compliance**: "automated driver licence and grey fleet checks… never get caught out by driving bans, insurance expiry and missing documents again"; **Driver Licence Checks**; **Grey Fleet** licence, MOT & insurance checks; **Permit to Drive** (a named eligibility artifact).
  - **Driver training**: Driver CPC course booking, workshops, on-road coaching, eLearning; training records managed with reminders ("get reminders so you never miss a deadline").
  - **Continuum platform**: "brings risk, compliance and driver training together… evidence your duty of care"; "fully documented audit trails"; management information/reporting; **Continuum for drivers / mobile app** (driver-facing).
- **Grey fleet** is structurally significant: employees driving their *own* vehicles — the compliance record joins the person (their licence) with documents about the vehicle they drive (insurance, MOT). This is only possible if the system of record is the driver, not the vehicle.
- Vendor claims: 750,000 drivers, 4,000+ clients (marketing figures).

### Type reading

TTC's center of gravity is **organizational duty of care over its drivers**: entitlement checks, risk profiling, remediation (training/coaching), and evidence/reporting. Same core as Foley and eDriving under a different regulatory vocabulary (UK/EU duty of care vs US DOT compliance).

## Cross-product Comparison

| Structure | Foley (US compliance pole) | eDriving (global risk pole) | TTC Continuum (UK duty-of-care pole) | Verdict |
|---|---|---|---|---|
| Per-driver record of identity + employment context + driving credentials | ✔ (driver qualification files; CDL, medical cards) | ✔ (drivers enrolled in programs; license data) | ✔ (drivers profiled; licence data) | **All 3 → Core** |
| Driving-specific credentials with validity over time (licence class/status/expiry, medical, program participation) | ✔ (CDL renewal, DOT physical/medical cards, DQF documents) | ✔ (license status, restrictions, suspensions, revocations, expirations) | ✔ (licence entitlement, driving bans) | **All 3 → Core** |
| Aggregated per-driver qualification/compliance state (complete / action-required / not entitled; rating) | ✔ (DQF completeness; dashboard status) | ✔ (risk rating Low/Med/High) | ✔ (Permit to Drive; compliance status) | **All 3 → Core** |
| Checks against external record sources (MVR/licence class) | ✔ (annual MVR checks; Clearinghouse queries) | ✔ (baseline + automatic subsequent MVR; continuous monitoring) | ✔ (automated licence checks) | **All 3 → Core** (periodicity varies: periodic vs continuous — implementation axis) |
| Expiry/change monitoring + alerts | ✔ ("alerts you when a file is due"; new violation/suspension alerts) | ✔ (notification of change in status; automatic follow-up check) | ✔ (alerts; "never get caught out… again") | **All 3 → Core** (automation degree varies) |
| Remediation loop (renew, restrict, train, re-check) | ✔ (action-required alerts; maintain files) | ✔ (intervention; riskiest-driver focus) | ✔ ("positively intervene with automated tools, tasks and alerts") | **All 3 → Core** (shape varies) |
| Audit/evidence reporting | ✔ (DOT audit readiness; "offsite DOT audits") | ◐ (liability framing; program documentation) | ✔ (duty-of-care evidence, audit trails) | Strong common → Core-adjacent; keep as defining-adjacent, assert as common |
| Risk scoring per driver | ◐ (CSA scores are regulatory; MVR-based alerting) | ✔ (Low/Med/High; FICO Safe Driving Score from behavior) | ✔ (dynamic risk profiling) | Common (behavior-based scoring not universal) |
| Training/coaching administration | ◐ (not in driver-file product core; hiring/onboarding focus) | ✔ (micro-training, coaching, gamification) | ✔ (CPC, eLearning, workshops, records + reminders) | Common |
| Driver self-service surface | ◐ (candidate onboarding; consent flows) | ✔ (Mentor app: training, inspections, collision reporting, score) | ✔ (Continuum for drivers / mobile app) | Common |
| Consent / notice machinery for record checks | ✔ (Clearinghouse consent management) | ✔ (FCRA notices + consent) | ◐ (implied in licence checks; not explicit on fetched page) | Common (regime-dependent naming) |
| Hiring/recruiting intake into the record | ✔ (license-photo pre-screen; job ad → employee file) | ◐ (program enrollment) | ✘ (not observed) | Common, pole-dependent |
| Drug & alcohol program administration | ✔ (testing, consortium, Clearinghouse TPA) | ✘ (not observed) | ◐ (screening product; administration unclear) | Variant (US-regime-flavored) |
| Vehicle coupling to the driver's record | ◐ (only as GVWR thresholds) | ◐ (vehicle inspections by driver) | ✔ (grey fleet: insurance/MOT/tax joined to the person; company vehicles) | Variant — important: coupling exists but vehicle *asset management* does not |
| Telematics/behavioral data integration | ✘ (not observed in driver product) | ✔ (Mentor behavior data; telematics-class) | ◐ (in-vehicle and employee data integration) | Variant |
| Vehicle register / maintenance / fuel / asset lifecycle | ✘ | ✘ | ✘ | **Absent in all 3** — this is the FMS boundary |
| Freight/loads/orders; driver assignment to work; driver pay/settlement | ✘ | ✘ | ✘ | **Absent in all 3** — TMS/dispatch boundary |
| Duty-status / hours-of-service logging | ✘ (ELD positioned as a separate topic hub) | ✘ | ✘ | ELD/HOS boundary |

### Historic check (older / pre-digital / regional realizations)

- US paper DQF era: driver qualification files predate SaaS; the file-completeness + expiry-tracking + audit-readiness structure was realized with paper files and clerks, and third-party paper-file maintenance services. The L0 (record + time-bound entitlement + maintenance loop) holds without any cloud, scoring, or app. Pass.
- UK/EU duty-of-care licence checking predates telematics scoring (paper/phone licence checks; Licence Bureau lineage). Pass.
- Behavioral scoring (telematics-derived), gamification, continuous (365-day) monitoring, AI guidance: modern layered structure — L1/L2, not definitional. Pass.

## Canonical Abstraction

### L0 — Defining Invariant (jointly held; deliberately minimal)

1. **Driver of record** — a persistent, individually identified person who drives for the organization, carrying driving-specific entitlement data: licence/qualification credentials and driving-related documents attached to the *person*, not to a vehicle or a job.
2. **Time-bound driving entitlement as a governed state** — the record aggregates its credential/check evidence into a state that governs whether this person is currently entitled/fit to drive for the organization (entitled / action-required / not entitled; rated where applicable). Entitlement expires.
3. **The maintenance loop** — the application keeps entitlement current: re-checking/re-validation against time (expiries) and events (new violations/changes), flagging lapses to the organization, and driving remediation (renew, re-train, restrict, re-check) until the state is restored.

Removal tests: remove (1) → generic HR/employee record or a fleet-asset system; remove (2) → a document store with no governed state; remove (3) → a static snapshot, not management (the "management" in the Type name is this loop).

### L1 — Common Mature Structure

- credential/compliance calendar with expiry alerts per driver
- periodic or continuous external record checks (MVR/licence class) with change alerts
- per-driver risk rating/score (record-derived and/or behavior-derived)
- training/coaching assignment with completion records and reminders
- driver self-service portal/app (document upload, consent, training, inspections, scores)
- onboarding/hiring intake that creates the record (applicant → qualified driver file)
- organizational scoping (sites/divisions/groups) and manager-vs-driver role split
- audit/evidence reporting (duty-of-care / DOT-audit posture)

### L2 — Variant / Optional Structure

- regulatory regime: US DOT/FMCSA (DQF, Clearinghouse, drug & alcohol consortium) vs UK/EU duty-of-care (licence checks, grey fleet, CPC) vs generic corporate risk programs
- vehicle coupling depth: none / thresholds only / inspections / grey-fleet vehicle documents joined to the person
- telematics/behavioral data integration and behavioral scoring
- gamification and rewards
- hiring/recruiting depth (CDL-recruiting pole exists in market — under-sampled here)
- consent/notice machinery naming (FCRA-class in US evidence)

### L3 — Vendor-specific (Research Notes only)

Foley: Dash platform, Navigator AI, CSA Monitor, "12,000 collection sites", #1-DOT-compliance-provider claim. eDriving: Mentor, FICO Safe Driving Score, DriverINDEX, Crash-Free Culture five-stage methodology, Mentor Rewards, mileage/driver-count claims. TTC: Continuum platform name, Permit to Drive as a brand, NDORS/police-referred courses, Driver CPC booking, driver-count claims.

## Vendor-specific Findings

- Foley is the clearest "qualification file" pole: the file itself (create → convert → organize → maintain) is the product's spine.
- eDriving is the clearest "continuous monitoring + behavior" pole: the 365-day-vs-periodic contrast is its headline, and behavior data merges with record data (DriverINDEX).
- TTC is the clearest "entitlement gate + duty-of-care evidence" pole (Permit to Drive; grey fleet; audit trails), and the only sampled product that fuses vehicle *documents* (insurance/MOT) into the driver's record.
- None of the three does driver scheduling, dispatch, settlement, or vehicle asset management — despite the market label "driver management" sometimes being used loosely for FMS driver modules (naming-variance risk recorded).

## Boundary Findings

- **vs Fleet Management System** (resolves the flag from research/fleet-management-system.md): the two Types share *some* substrate (a roster of drivers and vehicles exist on both sides) but the **system of record differs structurally**. FMS: vehicle is the primary record — asset lifecycle, maintenance, fuel, telematics; driver data (assignment, scores, HOS) attaches to vehicles/trips. Driver Management: person is the primary record — entitlement, credentials, checks, remediation; vehicles (when present) attach to the person. Removal tests both ways: strip drivers from an FMS and it still manages vehicles; strip vehicles from a driver-management product (Foley DQF, TTC grey fleet, eDriving programs) and the driver record remains fully functional. The prior "probable Capability/Variant" hypothesis is **refuted for the standalone market segment** (three independent standalone vendors verified) and remains true only for the module reading inside FMS. **Verdict: distinct sibling Type centered on the person; flag resolved, both leaves kept.**
- **vs Trucking Management System / Dispatch Management**: those center on freight/orders/jobs and assign drivers to work (schedules, routes, settlements). Driver Management is job-independent — a driver's entitlement state exists whether or not work is assigned today. Driver schedules/pay were absent in all three sampled products.
- **vs Electronic Logging Device / HOS Platform**: ELD/HOS centers on duty-status logging against hours regulations; the driver is the subject of the log. Driver Management centers on qualification/entitlement; HOS data may feed risk but is not the record of record.
- **vs Airline Crew Management**: aviation sibling — crew records, qualifications/licences, duty/pairing legality. Crew Management is pairings-and-rostering-centric (duty planning as the core loop); Driver Management's core loop is entitlement maintenance. Adjacent sibling under the same "manage the humans, not the vehicles" family logic.
- **vs HR types (ATS / HRIS / LMS)**: overlap at the poles (Foley hiring; training everywhere) but HR systems lack driving-credential semantics (licence classes, endorsements, medical certification, driving-record checks) and the governed driving-entitlement state. Center-of-gravity test applies.
- **vs "driver app" surfaces**: driver-facing apps of fleet platforms are surfaces of other Types; in this Type the driver app is a self-service surface of the driver record (L1), not the Type itself.

## Uncertainties

1. DriverReach and Tenstreet (recruiting/onboarding-heavy pole) unreachable — the market breadth of "driver lifecycle from recruitment" is under-sampled; recruiting is kept at L1/Common with a noted sampling gap.
2. J.J. Keller Encompass (driver risk management product) unreachable — enterprise pole covered by Foley + TTC instead; training administration depth in a DQF product not directly verified.
3. Driver *scheduling/rostering* as part of "driver management" in some market segments (paratransit, transit, shuttle) — not observed in the sample; possible naming variance between this Type and scheduling tools. Left as an open naming risk; nothing asserted.
4. Precise regulatory mechanics (exact DQF document lists, retention periods, FCRA timing windows, UK check frequencies) were not researched and are not asserted anywhere.
5. Whether "continuous" monitoring is now the market norm or a differentiator of one vendor — only eDriving headlines it as contrast; Foley/TTC show periodic+event hybrid. Kept as an implementation axis.

## Final Synthesis

Driver Management is a real standalone Application Type: the operator-side system of record for the **people who drive** for an organization. Its defining core is exactly three jointly-held structures: the **driver of record** (a persistent, individually identified person carrying driving-specific credentials and documents — remove → generic HR record or fleet-asset system); the **time-bound driving entitlement** (the record aggregates credential and check evidence into a governed entitled/action-required/not-entitled state that expires — remove → document store with no governed state); and the **maintenance loop** (re-checking against time and events, flagging lapses, driving remediation to restore entitlement — remove → static snapshot, not management). The market realizes this core in three recognizable poles — US regulatory compliance (qualification files, screening, Clearinghouse), global corporate risk (continuous monitoring, behavioral scoring, coaching), and UK/EU duty of care (licence checks, grey fleet, permit-to-drive, CPC training) — all sharing the same spine. Mature products commonly add risk scoring, training administration, driver self-service apps, hiring intake, and audit evidence; vehicles may couple to the person (grey fleet, inspections) but vehicle asset management, freight, dispatch, and hours logging belong to the neighboring Types. The leaf stands as a distinct sibling of Fleet Management System (person-centered vs asset-centered), resolving the flag raised in the FMS pass.
