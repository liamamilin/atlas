# Research Notes — Campus Housing Management

Research date: **2026-09-06**

## Research Goal

Understand what a Campus Housing Management application actually is as an Application Type: what exists inside it, who operates it, how students flow through it from application to check-out, what states and rules govern it, and where its boundaries sit against neighboring Types (property management, hotel PMS, SIS, campus card, student billing, student conduct systems).

## Initial Boundary (pre-research hypothesis)

- **What it is (hypothesis):** institution-side software used by a college/university housing or residence-life office to run institution-owned student housing: housing applications, room assignment/selection, roommates, check-in/out, billing, and residence-life operations.
- **Primary users (hypothesis):** housing office staff (assignments/occupancy), residence life staff (coordinators, resident assistants), students as self-service participants.
- **Nearest neighbors (hypothesis):** Residential Property Management (lease-based tenancy), Student Housing Management (directory sibling leaf in the real-estate family), Hotel PMS (space + assignment + guest), Student Information System (eligibility source), Campus Card Management (meal plans/access), Student Billing System (charge destination), Student Conduct/Behavior Management (incident handling).
- **Main unknowns:** whether room selection/lottery is definitional or common; how deep meal plans and residence-life programming sit inside the Type; how the directory's "Campus Housing Management" (education family) relates to "Student Housing Management" (real-estate family).

## Research Questions

1. What is the unit of inventory (room vs bed), and how is it structured?
2. How does a student become a resident: application → selection → assignment → offer/accept → check-in?
3. How do roommate matching, roommate groups, and room changes actually work?
4. How does the assignment lifecycle relate to the academic term/year cycle?
5. What financial objects exist (housing charges, meal plans, student-account handoff)?
6. What residence-life operations live inside the system (staffing, duty, programming, conduct, students of concern, guests)?
7. What integrations are structurally assumed (SIS, ERP, payments, SSO, access control, meal plans)?
8. How do variants differ: on-campus housing office vs PBSA/operator; large vs small institutions; conference/summer housing; boarding schools?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Position (as observed) | Why sampled |
|---|---|---|
| **StarRez** | Global market-leading platform for student housing; serves higher education (on-campus), PBSA student property management, build-to-rent, co-living, staff housing, boarding schools | The market anchor; broadest module surface; explicit on-campus higher-ed solution |
| **eRezLife** | Independent all-in-one "housing assignment & residence life" software, built by residence-life professionals; targets institutions of varying size | Independent challenger philosophy; unusually complete public product-page documentation of the assignment lifecycle |
| **Symplicity Residence** | Housing/selection module inside a student-affairs suite (sibling products: Advocate for student conduct, CSM for career services) | Represents the "suite module" philosophy and shows which parts of the Type are separable |
| **Adirondack Solutions — The Housing Director (THD)** | Long-established (founded 1998) US student-housing specialist: web room assignments, housing operations, conference management, visitor tracking; acquired by StarRez in 2022 | Historical/legacy sample for the older-generation shape of the Type |

Note: Roompact (residence-life-focused vendor) was selected initially but its site returned HTTP 403 on two attempts; per the network-restriction rule it was abandoned rather than retried further, and no claims in this research rest on it.

## Sources

| Source | URL | Status |
|---|---|---|
| StarRez — home / platform overview | https://www.starrez.com/ | Fetched 2026-09-06 |
| StarRez — Higher Education solution page | https://www.starrez.com/solutions/higher-education | Fetched 2026-09-06 |
| StarRez — Room & Roommate Solution page | https://www.starrez.com/solutions/room-and-roommate-solution | Fetched 2026-09-06 |
| StarRez — The Housing Director (THD) customer hub | https://www.starrez.com/company/the-housing-director | Fetched 2026-09-06 |
| Adirondack Solutions — home | https://www.adirondacksolutions.com/ | Fetched 2026-09-06 |
| eRezLife — home | https://erezlife.com/ | Fetched 2026-09-06 |
| eRezLife — Assignments product page | https://erezlife.com/assignments/ | Fetched 2026-09-06 |
| eRezLife — Residence Life product page | https://erezlife.com/residence-life/ | Fetched 2026-09-06 |
| Symplicity — Residence solution page | https://www.symplicity.com/higher-ed/solutions/residence | Fetched 2026-09-06 |
| Roompact | https://www.roompact.com/ | **Blocked (403 ×2) — abandoned** |
| THD Knowledge Base (Zendesk) | https://starrez-thd.zendesk.com/hc/en-us | **Login-walled — not readable** |
| StarRez StarCare Online support | https://starrez.zendesk.com/ | Login-walled (referenced only) |

**Source-access limitation:** all reachable evidence is Tier 1–2 official vendor material (product and solution pages); no deep help-center articles were readable (THD KB and StarCare both behind login; Roompact unreachable). Therefore: no precise operational parameters (numeric limits, exact state names, default windows, pricing) are asserted anywhere in this research or in the final document; behavioral claims are calibrated to product-page-level evidence and marked by evidence layer below.

## Product Observations

### StarRez

Evidence layer: **A** (directly observed on official pages), unless noted.

- Positioning (root page): "The Unified Platform for Thriving Student Communities"; serves on- and off-campus student living; four solution areas named: **Housing Management, Residence Life, Operations, Conference & Events**.
- **Housing Management** area description: "From room selection to roommate matching and meal plans"; components named: Student Portal ("PortalX"), StarRez Web, email scheduling, dashboards; billing and online payments; integrations.
- **Residence Life** area description: conduct, community operations, and student employment in one place ("Rez 360"); named items: duty rounds, visitor tracking, concern reporting, contributions & interactions, programs management, employment; "incident tracking to staff onboarding".
- **Operations** area description: inspections, maintenance, package tracking; named items: inventory & inspections ("room condition reports and automated work order management"), package management, maintenance & work orders, front desk (keys, guests, packages).
- **Conference & Events** area: group bookings, lodging, event logistics; inquiry → quoting → housing → billing → guest management.
- Higher-education solution page (student journey language): students "complete their housing applications, participate in self-service housing selection, sign contracts, and meet other residents"; "Support the resident journey from move-in to move-out"; automate "room change requests"; paperless "maintenance requests, room condition reports, and check in/out"; billing with "terms, pro-rating, and billing cycles" and "auto-populated financial aid information"; "real-time occupancy tracking"; reporting on "occupancy, turnover, and finances".
- Room & Roommate Solution page: residents "independently choose rooms or suites and assign roommates"; "real-time opportunities for securing their ideal accommodations"; advanced roommate matching to "minimize roommate conflicts"; **roommate agreements** tracked by in-hall staff with reports; **gender-inclusive housing** via self-selection "regardless of biological sex"; desktop and mobile.
- Integrations page (higher-ed): "student information and financials, online payment processors, single sign-on with your campus portal, security access, and meal plans"; integration methods: real-time, REST, XML, batch file, scheduled interfaces.
- Industries listed: Higher Education, Student Property Management (PBSA), Build to Rent, Co-Living, Staff Housing, Boarding Schools — the same platform is sold across institutional and commercial-operator populations.
- Vendor-claimed scale/satisfaction figures (1,300+ institutions; 2M+ applications annually; 98–99% satisfaction; "80% less time on room assignments") are marketing claims on vendor pages — recorded here only as vendor claims, **not** used as evidence in the final document.

### eRezLife

Evidence layer: **A**.

- Positioning: "All-in-One Housing Assignment & Residence Life Software"; "designed by residence life professionals"; pricing packages vary by institution size ("bed count, staff structure, and budgets").
- **Assignments** module (full lifecycle described):
  - *Customized application processes* — "fully client configured"; students provide "housing preferences to emergency contacts"; different questions per applicant type ("new vs. returning").
  - *RoomeeZ* — opt-in private social network: students "search for, connect with, and request roommates".
  - *Online room selection* — "students can see which rooms are available in real-time and pick their assignment based on their selection time" (time-slot-based self-selection).
  - *Room offer* — after placement, student is "sent an offer to officially accept the assignment and help reduce 'no-shows'".
  - *Real-time room assignments* (staff side) — "room-swap and applicant comparison interface to see roommate compatibility and process quick room changes".
  - *Custom roommate search* — "custom roommate matching questions … based on their responses and preferences".
  - *Check-in/out* — "real-time check in"; track "early arrivals and late stays"; "ensure all students are accounted for".
  - *Financial tracking* — "full payment schedule for housing and meal plans or simply store bill codes for your ERP".
  - *System integration* — "send any data back to your main campus database (SIS/ERP) … so assignments and billing are processed correctly".
  - *User-defined reporting* — occupancy: "capacity, how the beds have filled, and who is living on campus".
- **Residence Life** module:
  - Student interactions: student conduct; program attendance tracking; students-of-concern; roommate conflict & mediation; overnight guest tracking; student recognition; peer helping; 1-on-1 intentional conversations.
  - Work processes: programming; living-learning communities; budget requests and tracking; duty night logs; RA weekly reports; time-off requests; staff evaluations.
  - Student forms: holiday stay-over; exam extension requests; overnight guest approval; room change request.
  - Staff management (staff profiles, progress), student tracking ("all student interactions … conduct history, room change request, program attendance"), communications.
- Other modules: **Room Condition Reporting** (reports + work orders), **Staff Selection** ("a human resource system built for the complexity of Residence Life hiring and selection"), **Campus Life**, **Appointments**.
- Partner badges: Ellucian (Banner/Colleague verified), TouchNet, Transact, Nelnet Campus Commerce, InCommon (SSO federation) — corroborates the SIS/payment/SSO integration norm.

### Symplicity Residence

Evidence layer: **A** for listed features and framing; product-page depth is lower than eRezLife's.

- Positioning: "Streamline on-campus housing" for "residential life staff"; part of a student-affairs suite (Student Conduct = separate product "Advocate").
- Feature list on product page: **Placement Management, Smart Assignment Engine, Reporting, Roommate Networking, Applications, Room Conditions**.
- Value framing: automated workflows to "decrease staff work"; "store up-to-date student information and keep campus leaders informed"; "integrating student information systems and other third-party applications".
- Customer quotes: Duke University — "streamline our residential life selections process into one system"; Carlow University — used Residence for a **move-out process** and to "keep track of how many residents are on campus at any given time" (roster/occupancy use under exceptional conditions).
- Observation: the module centers on **selections/assignment + applications + room conditions**; conduct is deliberately a sibling product — evidence that full conduct case management is outside this Type's core.

### Adirondack Solutions — The Housing Director (THD)

Evidence layer: **A** for the thin facts below; deeper documentation login-walled.

- Home page: "web-based room assignments, housing operations, conference management, visitor tracking"; "designed by and for housing professionals" / "tested by student affairs professionals".
- Corporate fact (observed on StarRez THD hub): founded **1998**; "joined the StarRez family" in **2022** (acquisition); THD customers are being migrated to StarRez (customer stories about "seamless migration from THD to StarRez").
- Observation: a 1998-generation product already has the same core shape (room assignments + housing operations + conference housing) — supports the historical check that the defining core predates modern portals/social features.

## Cross-product Comparison

| Dimension | StarRez | eRezLife | Symplicity Residence | THD | Layer |
|---|---|---|---|---|---|
| Space inventory (buildings → rooms/spaces) | yes (inventory & inspections) | yes (beds, rooms, real-time availability) | yes (placement) | yes (room assignments) | **L0** |
| Resident = institution-population member (student record) | yes (SIS integration) | yes (SIS/ERP round-trip) | yes (SIS integration) | yes (campus systems) | **L0** |
| Assignment: student × space × period, via managed process | yes (applications, selection, contracts) | yes (application → selection → offer/accept) | yes (selections/placement) | yes (web room assignments) | **L0** |
| Occupancy tracking (who is where; real-time) | yes ("real-time occupancy tracking") | yes ("real-time check in"; "who is living on campus") | yes (Carlow roster use) | yes (housing operations) | **L0** |
| Housing application (configurable, per applicant type) | yes | yes (explicit: new vs returning) | yes (Applications) | (implied) | L1 |
| Self-service room selection / time-slot pick | yes ("self-service housing selection") | yes ("based on their selection time") | yes ("selections process") | (unknown) | L1 |
| Roommate matching + roommate requests/groups | yes (dedicated solution) | yes (RoomeeZ + matching questions) | yes (Roommate Networking) | (unknown) | L1 |
| Offer/accept + contract signing | yes ("sign contracts") | yes (Room offer) | (unknown) | (unknown) | L1 |
| Room change / swap handling | yes (automated room change requests) | yes (room-swap interface; room change request form) | (unknown) | (unknown) | L1 |
| Check-in / check-out; early arrival / late stay / break housing | yes (check in/out; any type of student/guest "throughout the calendar year") | yes (explicit early arrivals, late stays, holiday stay-over) | (move-out observed) | (unknown) | L1 |
| Room condition reports / inspections / damages | yes (room condition reports; inventory & inspections) | yes (dedicated module) | yes (Room Conditions) | (unknown) | L1 |
| Housing billing → student account / ERP; cycles, pro-rating | yes (terms, pro-rating, billing cycles, financial aid) | yes (payment schedules; bill codes for ERP) | (not shown) | (unknown) | L1 |
| Meal plans | yes (Housing Management includes meal plans; integration listed) | yes (financial tracking covers meal plans) | no evidence | (unknown) | L2 (linkage L1-adjacent) |
| Residence-life ops: staff duty, programming/attendance, 1-on-1s | yes (Residence Life area: duty rounds, programs, interactions) | yes (extensive) | no (out of module scope) | (unknown) | L1 (module-dependent) |
| Conduct incident logging | yes | yes (student interactions) | **no — sibling product** | (unknown) | L1 for logging; case management outside |
| Students of concern / wellbeing flags | yes (concern reporting) | yes (students-of-concern) | (not shown) | (unknown) | L1/L2 |
| Guest / visitor tracking | yes (visitor tracking) | yes (overnight guest tracking/approval) | (not shown) | yes (visitor tracking) | L1/L2 |
| Package / mailroom, front desk | yes (front desk & package management) | no evidence | no evidence | (unknown) | L2 |
| Maintenance work orders | yes | yes (RCR → work orders) | (not shown) | (unknown) | L1/L2 |
| Conference / summer / event housing | yes (dedicated solution area) | (conferences page exists) | no evidence | yes (conference management) | L2 |
| Student-staff (RA) hiring/selection | yes (employment) | yes (dedicated module) | no evidence | (unknown) | L2 |
| Occupancy / retention / finance reporting | yes | yes | yes (Reporting) | (unknown) | L1 |
| SIS/ERP/payments/SSO integrations | yes (explicit list) | yes (explicit partners) | yes (SIS integration) | yes | L1 |
| Student portal (self-service) | yes (PortalX) | yes (student-facing processes throughout) | (not shown) | (web-based era) | L1 |

**Reading:** the four-way overlap on inventory + student identity + assignment + occupancy is total; everything else is tiered. Residence-life operations are deep in StarRez and eRezLife but absent from Symplicity's housing module (handled by siblings) — so residence-life depth is *common mature structure*, and its breadth varies by packaging.

## Canonical Abstraction

### L0 — Defining Invariant

1. **Institution-held residential space inventory** — rooms/beds modeled as individually assignable units, organized within buildings/halls; the system knows every assignable space and its capacity.
2. **Resident drawn from an institution-administered population** — the occupant is not an anonymous tenant but an identified member of the institution's population (normally a student, with a record that can be matched to the student system).
3. **Assignment** — an administrative allocation binding a specific resident to a specific space for a defined period (normally an academic term/year), produced by a managed application/selection process rather than a free-market lease.
4. **Occupancy state** — the system continuously tracks which spaces are filled or vacant and who is currently in residence.

Test: remove the inventory → facilities registry, not housing management. Remove the institutional population/identity → generic property management. Remove assignment → a space list, not an operation. Remove occupancy state → housing operations cannot run.

### L1 — Common Mature Structure

Very common in mature products but not required for recognition:

- configurable **housing applications** (applicant-type-specific questions, preferences, emergency contacts)
- **self-service room selection** with real-time availability and ordered selection (time-slot/lottery-style)
- **roommate matching**: matching questions, roommate search/requests, roommate groups, compatibility views; roommate agreements
- **room offer / acceptance** (and contract signing) to confirm assignments and reduce no-shows
- **room changes / swaps** as a managed request workflow
- **check-in / check-out lifecycle** with early-arrival, late-stay, and break/holiday housing handling
- **room condition reports**, inspections, damage recording; work-order handoff
- **housing billing**: charges, payment schedules/cycles, pro-rating; export/sync to the student account / ERP; financial-aid data alignment
- **residence-life operations**: staff structures (coordinators/RAs), duty logs and reports, programming/event tracking with attendance, 1-on-1 interactions, roommate conflict mediation, students-of-concern, guest/visitor tracking
- **integrations assumed structurally**: SIS (student data in, assignments/billing out), payment processors, SSO, access control, meal plans
- **occupancy/retention/finance reporting** and dashboards
- **student self-service portal** and targeted communications

### L2 — Variant / Optional Structure

Depends on segment, geography, operator type, or packaging:

- meal-plan administration depth (boundary with Campus Card Management)
- conference / summer / event housing as a business line
- student-staff selection/hiring (RA recruitment as HR)
- front desk operations: packages/mailroom, key management, visitor management
- access-control/lock hardware integration
- on-campus housing office vs PBSA/commercial-operator (lease-flavored) deployment of the same structures
- living-learning communities and residential-curriculum programming depth
- gender-inclusive housing policy support
- emergency rosters / duty-of-care uses (e.g., tracking who is on campus during disruptions)
- adjacent populations: boarding schools, staff housing, co-living (same structures, different population rules)

### L3 — Vendor-specific (Research Notes only)

- StarRez: PortalX (student portal), Rez 360, StarRez Intelligence (AI), "Housing Core"; acquired ecosystem brands: The Housing Director (Adirondack, 2022), Mercury, Seattle Technology Group/Iris, College Pads (off-campus platform); SOC 2 / PCI / FERPA-ready / HIPAA-ready / GDPR compliance posture; marketing stats (1,300+ institutions, 2M+ applications/year, 98–99% satisfaction, 80%/65%/40%-hour efficiency claims).
- eRezLife: RoomeeZ (opt-in private social network); "Smart" packaging by bed count; developed by Kinetic; Cordance legal entity.
- Symplicity: "Smart Assignment Engine" naming; Residence as one of a student-affairs suite (Advocate, CSM, Accommodate); "6,000+ residential life staff" claim.

## Rejected Findings

- **"Roommate matching is part of the definition"** — rejected. Assignments can be entirely administrative; matching (and roommate social networks) is the modern common pattern, not the invariant. Older and small-institution operations assign without it.
- **"Self-service room selection is definitional"** — rejected. It is the current dominant *experience* (both StarRez and eRezLife lead with it), but assignment-by-housing-office remains a fully supported mode across the sample; the invariant is the assignment, not who clicks.
- **"Meal plans belong in the core"** — rejected. Meal-plan linkage is common (two of four products show it; StarRez lists it as an integration as well as a module), but deep meal-plan administration sits at the boundary with Campus Card Management and is absent from parts of the sample.
- **"Conduct case management is part of this Type"** — rejected. Incident/concern *logging* from residence-life staff is common; adjudication workflow is a separate Type (Symplicity ships it as a sibling product, Advocate; directory has Student Behavior Management).
- **"Lease-based tenancy like property management"** — rejected. The resident relationship is created by application → offer → acceptance of an *assignment* (a contract of occupancy administered by the institution), not by a negotiated commercial lease; this difference is structural, not cosmetic.
- **Marketing efficiency/scale numbers** — rejected as evidence (vendor claims; no independent verification; not needed to explain the Type).

## Boundary Findings

| Neighbor | Relationship | Distinction criterion |
|---|---|---|
| **Student Housing Management** (directory: real-estate family, §17) | **Probable near-duplicate / same Type, different vantage** | StarRez sells the *same platform* to "Higher Education" (on-campus) and "Student Property Management (PBSA)" (commercial operators); the objects (inventory, resident, assignment) are identical. The education-family leaf looks from the housing-office vantage; the real-estate-family leaf from the operator/lease vantage. **Flagged in STATUS as needing joint review — not silently merged.** |
| Residential Property Management | Adjacent (general landlord software) | Lease negotiation with a tenant vs application→assignment for an institution-population member; no academic terms, no roommate coordination, no residence life. Remove the institutional population + assignment governance → it becomes property management. |
| Hotel PMS | Adjacent (transient lodging) | Hotel: short-stay guest, folio + payment at center, room status driven by housekeeping. Campus: term-long assignment of an institution member, charges billed to the student account, occupancy driven by the academic cycle. Same "space + assignment" skeleton, different governing logic. |
| Student Information System | Upstream source | SIS owns the student record/eligibility; housing consumes it and returns assignment/billing data. Housing without SIS integration is possible but common products are built assuming it. |
| Student Billing System | Downstream destination | Housing computes and schedules charges; the student account/billing system collects. |
| Campus Card Management | Boundary-sharing | Meal plans and door access appear in both worlds. Campus card owns the *credential and entitlements* (including meal-plan accounting); campus housing references/links them. |
| Student Behavior / Conduct Management | Sibling (often separate product) | Residence-life staff log incidents/concerns inside housing systems; the conduct case workflow (hearing, sanctions) is its own Type. |
| Student Services Portal | Surface, not Type | The student-facing portal is one interface of the housing system (PortalX-style), not a standalone application family for housing. |
| Conference / Event housing | Variant module | Same inventory, different population (guests) and short-stay logic; sold as an add-on area (StarRez) or feature (THD). |
| Amenity Booking / Resource Scheduling | Capability adjacency | Room bookings/appointments exist (StarRez "Bookings & Appointments"; eRezLife Appointments) as support capabilities, not the Type's center. |

**"Remove what, and it becomes the neighbor" test:**

- Remove institutional population identity & term-bounded assignment → Residential Property Management.
- Remove assignment/occupancy governance, keep guest+folio → Hotel PMS.
- Remove inventory/assignment, keep program rules on occupancy eligibility → Affordable Housing Management (different governing rule source: income/housing program vs enrollment/housing contract).
- Keep only the credential+meal-plan accounting → Campus Card Management.

## Historical / Market-Sample Check

- **Older generation:** THD (1998) already centers room assignments + housing operations + conference management + visitor tracking — the L0 core predates modern portals, roommate social networks, and AI features. Fits the definition.
- **Regional:** the sampled market is North America-centric; StarRez's same platform also serves UK/Australia PBSA and boarding schools (industries listed) with the same structures (inventory, assignment, contracts). The definition does not depend on US-specific practices (e.g., gender-inclusive housing policies are a variant, not the core).
- **Platform-native / lighter deployments:** Symplicity Residence shows a reduced module (selections + placement + applications + room conditions) that still unambiguously *is* this Type — confirming the L0 set is sufficient for recognition and that residence-life breadth is not definitional.
- **Operator-side (PBSA) reuse:** StarRez's PBSA product is lease-flavored (commercial operator); the education-family definition still recognizes it via inventory + population + assignment, with the lease/contract flavor as a variant. This is the strongest signal behind the duplicate-leaf flag.

## Uncertainties

1. Exact object granularity (room vs bed as the assignable unit) varies by product and configuration; no authoritative mapping was readable (help centers login-walled). Stated generically in the final document.
2. The precise mechanics of selection ordering (lottery numbers, time slots, seniority) are institution-configured; eRezLife's "selection time" confirms the mechanism family but no defaults are asserted.
3. Whether directory leaf **Student Housing Management (§17)** is meant as the operator/PBSA variant or a duplicate could not be settled from available evidence — recorded as a boundary issue for joint review.
4. Roompact's residence-life/curriculum emphasis (unreachable) might have added a fifth philosophy (programming-centric); its absence is compensated by eRezLife's and StarRez's residence-life modules; claims about the residence-life layer rest on two products (marked accordingly).
5. Meal-plan depth inside housing products (vs campus card systems) could not be verified at feature level — kept at "linkage common, depth varies".
6. No non-English/regional vendor (e.g., UK-specific systems) was directly documented; regional generality rests on StarRez's multi-region industries page.

## Final Synthesis

A Campus Housing Management application is the institution-side system of record for running student housing. Its world is built from four permanent structures:

```text
Institution-held space inventory (rooms/beds in halls/buildings)
  + resident = member of the institution's administered population
  → assignment (resident × space × defined period, via managed application/selection)
  → occupancy state (who is assigned, who is in residence, what is vacant)
```

Around that core, mature products add the full residential lifecycle (application → selection → offer/accept → move-in → in-residence life → room changes → move-out/damages), the money path (housing charges → student account), the residence-life operations layer (staff, duty, programming, concerns, guests), and a standing integration set (SIS in; billing/payments/SSO/access/meal plans out). Variants — conference housing, PBSA operators, boarding schools, student-staff hiring — reuse the same core with different populations, periods, or rule flavors. The Type is distinguished from property management by the governed assignment of institution-population members rather than commercial leases, and from hotel PMS by term-length occupancy driven by the academic cycle rather than transient stays and folios.
