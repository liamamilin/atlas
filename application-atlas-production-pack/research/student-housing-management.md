# Research Notes — Student Housing Management

## Research Goal

Document the §17 leaf **Student Housing Management** as the *operator/landlord vantage* of student-housing software: the systems used by businesses that own or operate student rental portfolios (purpose-built student accommodation operators, off-campus student-housing owners, multifamily companies with student assets) to lease, occupy, and run those portfolios.

This pass also discharges two pre-hung flags:

1. **campus-housing-management (§23, processed 2026-09-06)** flagged "probable near-duplicate with Student Housing Management (§17)" — the market leader sells the same platform to "Higher Education" and "Student Property Management/PBSA". Joint review owed here.
2. **residential-property-management (§17, processed 2026-09-09)** left a forward flag: "student-housing-management (enrollment-cycle leasing and by-the-bed structures — AppFolio rent-by-the-bed: separate leases and tenant ledgers by-the-bed)".

Secondary inherited seams: **hostel-management-system** (§26, 2026-09-08) recorded "vs Student Housing Management (academic-year contracts vs nightly travelers)".

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this leaf is to Campus Housing Management what Residential Property Management is to a housing authority — the commercial operator's system: leases, rent, occupancy-for-revenue, leasing funnel — but shaped by student-housing economics: per-bed tenancy inside shared units, academic-year terms, installment rent, guarantors, one annual leasing window, one annual turn.
- Nearest neighbors: Campus Housing Management (§23 sibling), Residential Property Management (§17 sibling), Hotel PMS / Hostel Management (transient lodging), Rent Collection Platform / Tenant-Resident Portal (capability slices), Short-term Rental Management.
- Unknowns: whether the operator market sustains a distinct product population or is merely RPM configured for students; where the "by-the-bed" structure is definitional vs configurational; whether roommate machinery is definitional; what happens at the PBSA/short-stay seam (OTA channels).

## Research Questions

1. What is the inventory model (unit vs bed) and is bed-level leasing definitional or configurable?
2. What is the occupancy instrument — lease, license, assignment? Who is party to it (tenant, guarantor)?
3. How does the leasing funnel work (lead → application → screening → contract) and how does it differ from generic PM?
4. How is rent structured (installments vs monthly) and billed (per-bed ledgers, deposits, damages)?
5. What is the annual cycle: pre-leasing / rebooking / renewals / turn? Which metrics does the business run on?
6. What roommate machinery exists (matching, self-selection, placement boards, waitlists)?
7. What operator-side operations exist beyond leasing (maintenance, inspections, accounting, owner reporting)?
8. Where does marketing/distribution sit (websites, listing syndication, OTA channels, university channels)?
9. How does the operator vantage differ structurally from the institution vantage (§23 leaf)?
10. Where exactly is the seam to Residential Property Management, and where does the product market itself say "student is different"?

## Representative Products

| Product | Why selected | Customer tier / philosophy |
|---|---|---|
| **StarRez** (Student Property Management / PBSA solution) | Market leader; sells the *same platform* into "Higher Education" and "Student Property Management (PBSA)" industries — the product needed to adjudicate the near-duplicate flag. Strong international PBSA customer base (UK, Australia). | Enterprise; student-native platform serving both vantages |
| **Entrata Student** | The leading multifamily-stack vendor's dedicated student line ("we built a solution specifically for student housing operators"); deep leasing/turn/assignment machinery | Enterprise operators; multifamily OS with student specialization |
| **RealPage Student** (OneSite for Student Housing) | The other multifamily-stack student line; explicit "lease by the bed or by the unit" positioning; adds market analytics/revenue management tier | Enterprise operators; platform + data/revenue-management layer |
| **AppFolio** (Student Housing capabilities) | Generalist PM suite with gated student capabilities — the "RPM configured for student" pole needed for the RPM boundary flag | Mid-market operators; one platform for all property types |

## Sources

Fetched directly (2026-09-10):

- StarRez — Student Property Management (PBSA) solution page: https://www.starrez.com/solutions/student-property-management-pbsa (also visible: industries nav — Higher Education, Student Property Management, Build to Rent, Co-Living, Staff Housing, Boarding Schools)
- Entrata — Entrata Student solution page: https://www.entrata.com/solutions/student
- RealPage — Property Management for Student: https://www.realpage.com/student/property-operations/
- AppFolio — Student Housing market page: https://www.appfolio.com/markets/student-housing

Official pages surfaced via search highlights (snippets of official pages; treated as Tier-2 corroboration):

- Entrata — Student Housing industries page: https://www.entrata.com/industries/student-housing
- Entrata — Student Revenue Intelligence: https://www.entrata.com/products/srm
- Entrata — Leasing Center: https://www.entrata.com/products/leasing-center (via entrata.webflow.io mirror)
- RealPage — Student Living Software hub: https://www.realpage.com/student/
- RealPage — Renter Engagement for Student: https://www.realpage.com/student/renter-engagement/
- RealPage — Student Property Management brochure (PDF): https://www.realpage.com/storage/files/pages/pdfs/2020/02/vst-18-014-028-student-property-operations-brochure.pdf
- RealPage — Asset Optimization for Student: https://www.realpage.com/student/asset-optimization/
- AppFolio — "What's New in AppFolio: Winter 2024" (Flexible Leasing, Pre-Leasing Metrics): https://www.appfolio.com/articles/2024-q4-product-update
- AppFolio — Student Housing Property Management (guide page): https://www.appfolio.com/student-housing-property-management
- AppFolio — Granite customer story: https://www.appfolio.com/customer-stories/granite
- StarRez — customer stories: Abodus (UK PBSA), Journal Student Living (AU PBSA)
- UCISA (UK HE sector body) — StarRez showcase: "Student Accommodation Management solution powers 1300+ Global Higher Education and PBSA customers"

Contextual (Tier 3, used only for market-structure framing, no operational claims drawn):

- findmyplace.co blog "Student Housing Property Management Software (2026)"; proprietio.com blog "Best PM Software for Student Housing (2026)" — independent confirmation of the market's self-description (bed-as-billable-object, guarantor workflow, joint-and-several vs by-the-bed, tier split enterprise vs mid-market).

Not reachable / limitations:

- StarRez help center (StarCare, zendesk) — login-walled (consistent with the §23 pass).
- Entrata and RealPage do not expose public per-feature help documentation at the fetched URLs; evidence rests on official product/solution pages (Tier 2).
- No vendor pricing or numeric SLA claims were drawn from vendor pages except where explicitly flagged as vendor claims (e.g., StarRez "450+ OTA channels", "99% satisfaction") — kept in vendor-specific notes, not used as structure evidence.

## Product Observations

### StarRez — Student Property Management (PBSA)

Evidence layer: A (direct fetch of official solution page).

- **Positioning**: one of several industries served by the same platform ("Industries": Higher Education; Student Property Management (PBSA); Build to Rent; Co-Living; Staff Housing; Boarding Schools). The PBSA page is operator-business framed: "Scale Your Operations Effortlessly", "Trusted by major PBSA partners worldwide" (IQ Student Accommodation, UniLodge, Campus Living Villages, Scape, Iglu logos).
- **Leads → bookings → leases**: "From enquiry to booking — Streamline your leads to bookings with powerful tools that look after the entire process for you." "Lease signing & renewals — ...making it easy, secure, and fast to find a room and enter into a lease." "Schedule and automate moving processes — Schedule move-ins to avoid congestion..." — a commercial leasing funnel ending in *lease* documents, not institutional assignments.
- **Occupancy management**: "Residents can select their room, as well as, indicate their room preferences, lifestyle information, and profile information for roommate self-selection or staff allocation." — roommate self-selection OR staff allocation.
- **Money**: "We are a full accounts receivable and property payable platform that also integrates into general ledger solutions." "automatic recurring payments, flexible billing due dates, remittances, rent collecting". "Endless reporting... easily analyze occupancy, turnover, financial reporting". — operator-grade AR/AP, GL integration, owner-facing reporting ("communicate with owners or report to investors at any given time").
- **Distribution**: "Efficient Channel Management — Seamlessly connect StarRez with multiple Online Travel Agencies (OTAs) for a real-time, centralized view of inventory, availability, and pricing rates." "450+ OTA channels to fill vacant spaces" (vendor claim). "Easily choose which rooms to advertise, configure room visibility with specific min/max requirements, and easily adjust inventory, availability, and rates to accommodate seasonal changes or special events." — the PBSA operator fills vacant stock through short-stay channels; a bridge toward lodging territory, implemented inside this Type's inventory layer.
- **On-site operations**: mobile app for "inspections, review maintenance requests, make notes, take pictures"; front desk ("track visitors, package lockers, keys"); appointments; contactless move-in; package tracking; ESA/assistance-animal tracking; flexible gender options "defined by your operation"; community tools ("manage conduct, concerns, and interactions"); resident engagement programs.
- **Portal**: "A complete online student self-service portal" (pay rent, maintenance requests, payment options, community happenings).
- **Customer stories (PBSA operators, Tier-2 corroboration)**: Abodus (UK) — automation of "check-ins and parcel management", tenant communication, property-team efficiency; Journal Student Living (AU) — PortalX one-stop resident portal, "booking to maintenance requests", DocuSign lease/contract signing attaching documents to student profiles, direct-debit payments, dashboards as live operations data.
- **Context (UCISA listing)**: "Student Accommodation Management solution powers 1300+ Global Higher Education and PBSA customers, managing the student experience/wellbeing, occupancy, bookings, communications, reporting, conferences/events, revenue".

### Entrata Student

Evidence layer: A (direct fetch of official solution page).

- **Positioning**: "Student properties have their own way of operating. That's why we built a solution specifically for student housing operators." Solutions nav: Student = "Designed for the fast pace and seasonality of student housing." Industries page: "Student housing property management software is designed for high-turn, high-density portfolios serving universities and off-campus communities. Operators managing 500+ beds need tools that handle rapid leasing cycles, roommate matching, and bulk communication at scale."
- **Headline machinery** (the page's three lead features):
  1. "Automate roommate matching — Quickly determine matches based on responses to your own list of questions about personality factors, living habits, scholastic information, and more."
  2. "Simplify move-in checklists — Gather students' information before they arrive. View all outstanding items in one place and manage move-in days in real time."
  3. "Visualize your turn checklist — View all your move-in and move-out tasks. You can check them off and even perform a resident move-in or move-out directly from this checklist."
- **Bulk unit assignment board**: "just drag and drop residents onto unit spaces in the dashboard. Assignment letters are then generated automatically." — placement as a first-class, bulk, board-shaped operation.
- **Renewals/rebooking**: "Automate renewals — Auto-generate renewal offers or customize them for specific residents. Get offers to all residents faster with bulk-sending options."
- **Per-bed revenue**: Student Revenue Intelligence — "Find the best price for each bed available. Work toward your pre-lease goals." "Built for student communities... No need to reconfigure a multifamily solution." Leasing Center — "Establish per-bed rates so you can optimize occupancy and revenue. See how each available bed is performing"; "Track velocity and performance metrics in real time, and easily see where you stand with your pre-leasing goals."
- **Full-stack context**: the student solution rides on the platform's property-OS products (leasing/accounting/facilities/utility/BI) plus guarantor product (Homebody Guaranty) and screening (ResidentVerify) in the nav. Customers quoted: PeakMade Real Estate, Passco (student operators).

### RealPage Student (OneSite for Student Housing)

Evidence layer: A (direct fetch of official property-operations page; corroborating official pages via search).

- **Positioning**: "Whether you lease by the bed or by the unit, Realpage® Student Property Management brings flexibility, efficiency, predictability and scalability to all of your property management-related tasks. Start with a property management software solution that follows the complete student lifecycle, with processes like preleasing, roommate matching and unit assignment, to accounts receivable functions, forecasting, goal reporting and more."
- **By-the-bed billing**: "Recover even more NOI with utility billing and utility cost recovery, along with by-the-bed billing configurations, automated move-in and move-out processes and much more."
- **OneSite Student**: "Manage by the bed or by the unit—it's your choice... a customized, integrated property management solution that takes into account the unique challenges that only Student properties face." "OneSite Student manages the complete student renter lifecycle, from the time they enter the system until the day they move out." "Set up and enforce your own business rules complementing your business model."
- **Facilities/turn**: "track all inspections, take photos and process resident payments for assessed damages—on the spot"; "faster maintenance and turns".
- **Renter Engagement (corroborating official page)**: "Student renters just aren't the same as most conventional renters. Their motivations, leasing windows and even guarantors are different than in conventional markets." "maximize the value of their heads on beds." Student Leasing: "Lease management, with prospect communications, screening, online leasing and insurance"; "Flexible Terms — Set up multiple installment terms, move-in/move-out dates and floorplan styles, on demand, to cover any Student leasing scenario"; "Online Renewals — Renew students with automated, tiered pricing or a revenue management approach". Student Living: residents "connect with each other prior to move-in for potential roommate matching".
- **Brochure (corroborating official PDF)**: "Bulk processing — Streamline the turn during busy move-in and move-out seasons with bulk processing of unit assignments, waitlist, renewal offers, giving notices, maintenance orders and more." "Preleasing — Gain greater visibility into traffic, leases and return students, as well as lease activity and goals." "By-the-bed leasing — ...easily matching roommates and tracking deposits and damages for each student." "Roommate matching — automatically matching students based on a fully customizable questionnaire... Works with property waitlist and unit assignment, too."
- **Analytics tier (corroborating official page)**: Student Asset Optimization — "View pre-lease percentages, forecasts and KPIs down to the bed level"; "With a tight sales cycle and a big annual leasing window, pricing for Student Housing can be more than a challenge... forecast the upcoming leasing season as a whole"; "Get your pricing right—by the bed or by the unit".
- **Hub positioning**: "Leverage over 1 million Student beds of in-depth market data... Drive higher prelease rates" (vendor claim; market-data tier).

### AppFolio (Student Housing capabilities)

Evidence layer: A (direct fetch of official market page; corroborating release notes).

- **Positioning**: generalist "real estate performance platform" with a dedicated student-housing market page; "Student Housing Capabilities" and "Bulk Leasing Tools"/"Advanced Leasing Metrics" are gated to the Plus plan; the pitch is one platform for all property types ("If you have a separate software platform to manage only your student housing properties outside of your business's main property management system, it's harder to see your data...").
- **Leasing structure**: "With Pre-leasing Metrics and Flexible Leasing options... regardless of whether you are leasing by-the-bed or entire units." Release notes (Winter 2024): "With AppFolio Flexible Leasing, you can lease by the bed, or jointly and severally, depending on the market's needs and preferences. This ensures that you can fill all vacancies during pre-leasing."
- **Pre-leasing**: "Tracking pre-leasing percentages, knowing when to adjust your rates, and keeping track of your open spaces. Flexibly switching between by-the-bed and joint-and-several." "Monitor your Pre-Leasing Metrics... updates in real-time."
- **Placement**: "Placement Board — View all indirect pre-leases for a given property and the student housing inventory. Place students in beds with roommates who are looking to share a unit or bedroom."
- **Bulk operations**: "Our bulk management tools allow you to update lease terms, set prices, process move-outs, and view all future residents using the placement board with just a few clicks." (guide page adds "bulk renewals... renewing leases for large groups of student residents at the same time").
- **Rest of the stack**: standard PM modules (accounting & reporting, work orders, inspections & unit turns, portals & communication, purchase orders) — the student layer sits on a full residential PM base.
- **Customer evidence**: Granite (student housing, 11,000+ beds) — "individual leasing by the bedroom, all on one platform"; leasing metrics (leads, conversions, applications, screening); bulk leasing features.

## Cross-product Comparison

| Structure / capability | StarRez (PBSA) | Entrata Student | RealPage Student | AppFolio Student | Assessment |
|---|---|---|---|---|---|
| Student rental portfolio as managed inventory (properties/units/beds) | yes | yes | yes | yes | Core (4/4) |
| Lease/contract as the occupancy instrument (signed, e-signed, or "entered into") | yes ("enter into a lease"; DocuSign at Journal) | yes (leasing OS; offers→residents) | yes ("online leasing", "complete path to lease completion") | yes ("Flexible Leasing"; lease terms) | Core (4/4) |
| Per-space tenancy granularity: lease by bed *or* by unit (configurable) | yes (room-level selection/allocation; rooms advertiseable on channels) | yes (per-bed rates; bulk unit assignment) | yes (explicit "by the bed or by the unit—it's your choice") | yes (explicit "by-the-bed or entire units"; "by-the-bed or joint-and-several") | Core as *configurable granularity* (4/4); by-the-bed dominant realization, not definitional |
| Enrollment-cycle leasing: pre-leasing %, goals/velocity, leasing windows | yes (occupancy/turnover reporting; booking funnel) | yes ("pre-leasing goals", velocity metrics) | yes ("preleasing... lease activity and goals"; "big annual leasing window") | yes ("Pre-Leasing Metrics"; "fill all vacancies during pre-leasing") | Core (4/4) |
| Placement of residents into spaces (board-shaped, bulk) | yes (roommate self-selection or staff allocation) | yes (bulk unit assignment board; drag-and-drop) | yes (unit assignment; bulk processing of unit assignments, waitlist) | yes (Placement Board) | Core (4/4) |
| Roommate matching (questionnaire-based or social) | yes (advanced roommate matching; lifestyle/profile info) | yes (custom questions: personality, habits, scholastic) | yes (customizable questionnaire; prior-to-move-in connection) | partial (placement board mentions roommates seeking to share; no matching questionnaire surfaced) | Common mature structure (3.5/4) |
| Annual turn machinery (bulk move-out/move-in, checklists, inspections) | yes (mobile inspections; move-in scheduling) | yes (turn checklist; move-in checklists) | yes (bulk processing of move-in/out, giving notices; mobile inspections w/ damage assessment) | yes (bulk move-outs; inspections & unit turns in base) | Common mature structure (4/4) |
| Renewals / rebooking campaigns (bulk offers) | yes (lease signing & renewals) | yes (bulk-sending renewal offers) | yes (online renewals, tiered/revenue-managed pricing) | yes (bulk renewals) | Common mature structure (4/4) |
| Rent billing: installments / flexible schedules, per-resident ledgers, deposits & damages | yes (flexible billing due dates, recurring payments; deposits/damages via front desk/community) | yes (leasing & rent procedures; prorate charges) | yes (multiple installment terms; deposits and damages per student) | yes (lease terms, prices, per-bed ledgers implied by Granite quote) | Common mature structure (4/4); installment *mechanics* variant |
| Guarantor / screening workflow | not surfaced on the PBSA page (screening implied by leasing funnel; ESA tracking present) | yes (ResidentVerify, Homebody Guaranty in platform nav) | yes (screening; "even guarantors are different" positioning) | yes (tenant screening in stack; co-signer via stack per Tier-3 framing) | Common in mature products; depth varies (marked qualified) |
| Occupancy/revenue analytics at bed level | yes (occupancy, turnover, financial reporting; dashboards) | yes (SRM per-bed pricing; pre-lease goals) | yes (KPIs "down to the bed level"; revenue management) | yes (Advanced Leasing Metrics, Plus plan) | Common mature structure (4/4); AI/revenue-optimization depth is vendor tier |
| Marketing/distribution (websites, syndication) | yes (website integration; OTA channel management — 450+ channels, vendor claim) | yes (websites, lead capture, Leasing Center contact center) | yes (marketing/leasing suite) | yes (listing syndication per stack) | Common; OTA short-stay channel fill is StarRez-PBSA-specific |
| Maintenance / facilities / work orders | yes | yes (facilities management) | yes | yes | Common mature structure |
| Accounting (AR/AP, GL), owner/investor reporting | yes (explicit) | yes (accounting product) | yes (financial management; SmartSource) | yes (accounting & reporting; owner portals) | Common mature structure |
| Resident portal (pay, requests, community) | yes (self-service portal) | yes (ResidentPortal) | yes (resident engagement/living) | yes (portals & communication) | Common mature structure |
| Residence-life / community programming & conduct tools | yes (community management; conduct/concerns/interactions; resident engagement) | not surfaced | not surfaced | not surfaced | Optional — institution-vantage overlap; not definitional here |
| Conference/short-stay fill via OTA channels | yes (product-specific strength) | no evidence | no evidence | no evidence | Vendor-specific |

**Reading**: the four-way overlap is total on the operator spine (portfolio inventory → lease tenancy → placement → enrollment-cycle leasing/turn → money/operations). The starkest vendor contrast is philosophy: StarRez approaches from the residential-community side (carrying residence-life/community tools into PBSA), Entrata/RealPage from the multifamily-operations side (leasing velocity, turn, revenue), AppFolio from the generalist-suite side (student as a capability gate on one platform).

## Canonical Abstraction

### L0 — Defining Invariant

The operator vantage's defining core — three jointly-held structures:

1. **The student rental portfolio as leasable space inventory** — properties organized into units and (dominantly) beds, each space individually leasable and managed, held by a business operating for occupancy revenue. Remove → a listings site or CRM with nothing to operate.
2. **The per-space tenancy as the occupancy instrument** — occupancy is created by a *lease/contract between the operating business and an individual resident (or resident group) for a specific space and term*, produced by a leasing funnel (enquiry → application → qualification/screening → signed agreement) and billed as rent to that resident's ledger. The tenancy term is set on the **enrollment cycle** (academic-year/fixed-term aligned dates, with rent commonly structured as installments across the term), and tenancy granularity is configurable per space — a bed can carry its own lease, rate, ledger, and dates independently of the other beds in the same unit. Remove the lease → institution-governed assignment (Campus Housing Management territory); remove the enrollment alignment and per-space granularity → generic Residential Property Management; make stays nightly → hotel/hostel territory.
3. **Enrollment-cycle occupancy management** — the portfolio's occupancy is planned, sold, placed, and turned around the academic year: next-period occupancy is tracked and sold ahead of time (pre-leasing/rebooking against occupancy goals), residents are placed into specific spaces (staff allocation or resident self-selection, with roommate coordination), and the year's end is executed as a portfolio-scale turn (bulk move-outs, make-ready, move-ins). Remove → lease administration with no cycle (RPM); keep the cycle but remove the tenancy → a sales pipeline with nothing to occupy.

Jointly-held load-bearing (removal tests):

- 1 alone = property/listing inventory.
- 2 without 1+3 = plain lease administration (RPM with student tenants).
- 3 without 1+2 = leasing CRM / sales pipeline.
- 1+2 without 3 = generic RPM use (the small-landlord seam).
- 1+3 without 2 = assignment/allocation machinery (institution vantage) or a booking system.
- 2+3 without 1 = leasing funnel with no portfolio to place into.

### L1 — Common Mature Structure

Present across the sample (3–4 of 4) but not required for recognition:

- leasing-funnel CRM (leads/guest cards, applications, online leasing, e-signature)
- roommate matching questionnaires and roommate search/self-selection
- bulk operations as the default operating mode (bulk assignment, renewal offers, notices, move-outs, communication)
- turn machinery: move-in/move-out checklists, inspections with photos, damage assessment and charges, make-ready
- renewal/rebooking campaigns (bulk offers, tiered or revenue-managed pricing)
- rent machinery: installment schedules, per-resident ledgers, deposits, damage charges, payments/recurring billing
- guarantor/co-signer and screening workflow (depth varies; strongest at Entrata/RealPage)
- occupancy and leasing analytics (pre-leasing %, velocity, bed-level KPIs); revenue management at the enterprise tier
- maintenance/facilities/work orders
- resident self-service portal (pay rent, requests, roommate connection, community)
- marketing surfaces: property websites, listing syndication; OTA channel connectivity at the PBSA pole
- full accounting (AR/AP, GL integration) and owner/investor reporting

### L2 — Variant / Optional Structure

- **Leasing-liability configuration**: by-the-bed (several, per-tenant rent) vs by-the-unit joint-and-several — an explicit per-property choice (AppFolio "Flexible Leasing", RealPage "your choice").
- **Segment**: on-campus institution-operated vs off-campus private vs PBSA specialist operators; UK/Australia PBSA (contract flavors: tenancy agreements/licence agreements — product pages say "lease"; jurisdictional contract naming not asserted).
- **Population edges**: summer/conference and short-stay fills through OTA channels (StarRez); non-student rentals mixed into portfolios (AppFolio pole).
- **Residence-life/community layer**: carried into PBSA by StarRez (conduct, concerns, engagement programs); absent from the multifamily-stack and generalist operator stacks.
- **University relationships**: PBSA operators' partnerships with universities appear in customer-story framing; dedicated software support for nomination/master-lease blocks was *not* evidenced — not asserted.
- **Deep revenue management / AI pricing / market-data tiers** (Entrata SRM, RealPage Asset Optimization, AppFolio Max): enterprise-tier packaging, not structural.
- **Ancillary products**: renters insurance, deposit alternatives, utility billing/consolidation (SimpleBills-class), rewards/rent reporting.

### L3 — Vendor-specific (Research Notes only)

- **StarRez**: PortalX (student portal), Rez 360 (resident 360 view), StarRez Intelligence (AI), College Pads (off-campus listing platform, acquired; university-branded off-campus portals at no cost to universities), "450+ OTA channels", "99% customer satisfaction", 1,300+ institutions/organizations claim; PBSA customer logos (IQ, UniLodge, Campus Living Villages, Scape, Iglu); compliance posture (SOC 2, PCI, Cyber Essentials Plus, FERPA/HIPAA-ready, GDPR); industries list also includes Build to Rent, Co-Living, Staff Housing, Boarding Schools (same platform, different populations).
- **Entrata**: Entrata Student as a "solution" over the Entrata OS (OXP/RXP); Student Revenue Intelligence (SRM) "first-of-its-kind" per-bed revenue management; Leasing Center (outsourced leasing contact center with per-bed rate optimization); Homebody Guaranty (guarantor product); ResidentVerify (screening); bulk unit assignment board with auto-generated "assignment letters"; customers PeakMade, Passco.
- **RealPage**: OneSite for Student Housing / "OneSite Student Leasing & Rents"; Student Asset Optimization (market analytics + revenue management + BI, "1 million Student beds of data" claim); SimpleBills (utility bill consolidation billed to residents, vacant-unit handling during turn); Contact Center; "StudentSelect" naming appears in third-party coverage; brochure lists bulk processing of unit assignments, waitlist, renewal offers, giving notices, maintenance orders.
- **AppFolio**: Placement Board, Flexible Leasing (by-the-bed vs joint-and-several), Pre-Leasing Metrics, Bulk Leasing Tools / Advanced Leasing Metrics (Plus-plan gated), Realm-X AI; 50-unit minimum / plan gating; customers Granite (11,000+ beds), Chamberlin.

## Rejected Findings

- **"By-the-bed leasing is the definition"** — rejected. Two of four products explicitly position by-the-bed vs by-the-unit as a choice ("Manage by the bed or by the unit—it's your choice"; "lease by the bed, or jointly and severally"). The invariant is *per-space tenancy granularity as a configurable structure*; by-the-bed is the dominant student realization (and the market's own litmus test per Tier-3 sources), but a by-the-unit student operator on joint leases still runs this Type.
- **"Roommate matching defines the Type"** — rejected as a defining structure. Placement/allocation of residents into spaces is core (4/4); *automated matching questionnaires* are the modern common layer (3/4) and sit in the leasing/marketing loop.
- **"Residence-life/conduct tools belong to this Type"** — rejected as definitional. Present in StarRez's PBSA packaging (community management), absent from the multifamily-stack and generalist operator stacks; that layer is the institution-vantage leaf's standard structure. Recorded as an optional overlap here.
- **"Revenue management / AI pricing is definitional"** — rejected: enterprise-tier packaging (Entrata SRM, RealPage Asset Optimization, AppFolio Max); absent from lower tiers.
- **"OTA channel distribution is part of the Type"** — rejected: observed at StarRez PBSA only (the hostel/lodging seam); product-specific.
- **"This is just Residential Property Management with a student flag"** — rejected as a merge: the market maintains dedicated student product lines with structural machinery generic PM lacks (placement boards, pre-leasing metrics/goals, per-bed rate/ledger machinery, bulk turn tooling, installment-term configuration); vendors' own framing ("Student properties have their own way of operating"; "the unique challenges that only Student properties face") and independent market commentary agree the bed-as-billable-object is a structural, not cosmetic, difference. The boundary is nonetheless a *gradient at small scale* (documented in Boundary Findings), not a hard wall.
- **Vendor scale/efficiency numbers** (450+ channels, 1M beds, satisfaction %, time-saved %) — rejected as evidence of structure; vendor claims only.

## Boundary Findings

| Neighbor | Relationship | Distinction criterion |
|---|---|---|
| **Campus Housing Management** (§23, processed) | **Vantage sibling — keep-both ratified; near-duplicate flag discharged** | Same underlying phenomenon (managed student residential inventory) seen from two business sides. Operator leaf (this): occupancy instrument is a *lease/tenancy* with a commercial counterparty — leasing funnel, screening/guarantors, rent to a tenant ledger, occupancy-for-revenue, owner/investor reporting. Institution leaf: occupancy instrument is a *governed assignment* for an institution-population member — application/selection governance, eligibility from enrollment standing, charges to the student account, residence-life operations. StarRez sells one platform into both industries (nav: "Higher Education" and "Student Property Management (PBSA)") — the platform is shared, the vantages are structurally distinct (who owns the occupancy decision and where the money flows). Remove the lease and commercial tenancy machinery from this leaf → it collapses into the institution leaf; remove the assignment governance from that leaf → it collapses into this one. |
| **Residential Property Management** (§17, processed) | Closest structural neighbor — RPM forward flag discharged | Both are lease-led landlord systems. Seam = the **enrollment-cycle tenancy structure**: per-space (bed-level-capable) tenancy granularity, academic-year-aligned terms with installment rent, pre-leasing/goal-driven annual leasing windows, roommate placement, portfolio-scale annual turn, guarantor-shaped qualification. Remove the enrollment cycle and per-space structure → RPM used with student tenants (the documented small-landlord seam: a landlord running ordinary year-round leases to students is using RPM, not this Type). The market's own boundary marker: purpose-built products treat "a bed as a billable object" (Tier-3 phrasing); generalist suites bolt student capabilities on and explicitly say so. |
| **Hotel PMS / Hostel Management** (§26) | Adjacent (transient lodging) | Nightly guests vs term-length tenancies; folio per stay vs rent ledger per term. The seam is real but bridged: StarRez PBSA's OTA channel management lets operators fill vacant beds with short stays — a distribution capability inside this Type, not a merge (the tenancy/lease spine remains the center). Matches the hostel pass's recorded seam ("academic-year contracts vs nightly travelers"). |
| **Short-term Rental Management** (§17) | Adjacent | Transient nightly inventory vs academic-term tenancies; different calendars, rules, and money structures. |
| **Affordable Housing Management** (§17) | Adjacent (eligibility-governed occupancy) | Governing rule source differs: housing-program income/certification rules vs market leasing shaped to student renters (guarantors instead of income history); both are "eligibility-flavored" but the instruments differ (program certification vs lease + guarantor). |
| **Rent Collection Platform / Tenant-Resident Portal** | Capability slices | Payments and the resident-facing surface are standard capabilities here, not the system of record. |
| **Property Listing / Rental Application / Tenant Screening** | Funnel slices | Application and screening machinery appears inside this Type's leasing funnel as capabilities; the standalone Types center only that slice. |
| **Leasing CRM / Marketing platforms** | Funnel upstream | Lead-to-lease is one loop of this Type; the Type additionally owns occupancy, placement, turn, and the money/operations spine. |

**"Remove what, and it becomes the neighbor" tests** are embedded in the L0 removal analysis above (lease→campus-housing; enrollment-cycle+per-space→RPM; nightly→hotel/hostel; assignment→institution leaf).

## Historical / Market-Sample Check

- **Older practice**: a paper-era student landlord/hall operator — room-by-room lettings on academic-year agreements, one ledger per tenant, summer re-letting to fill the next session, a wall chart of rooms/beds, move-out inspections with deposit deductions — satisfies the core with no modern machinery (no portals, matching algorithms, or analytics). The pre-leasing structure exists as practice: next year's rooms are "let ahead" before the term starts.
- **Regional**: the sample is US-multifamily-heavy plus UK/AU PBSA (StarRez customers). UK PBSA historically lets per-room under tenancy/licence agreements — consistent with "per-space tenancy" (contract naming varies by jurisdiction; not asserted). The definition does not depend on US joint-lease law; the liability configuration (several vs joint-and-several) is recorded as a variant.
- **Platform-native / lighter deployments**: AppFolio demonstrates the reduced pole — a generalist PM suite with student *capabilities* (placement board, pre-leasing metrics, flexible leasing) satisfies the core without a student-first platform. Confirms the L0 set is what makes the Type recognizable, not the enterprise machinery.
- **Adjacent-population reuse**: StarRez's platform serves Build-to-Rent, Co-Living, Staff Housing, Boarding Schools from the same structures — evidence that the *core* generalizes, with the student-specific delta living in the tenancy-cycle structure rather than the inventory machinery. Co-living's per-room leasing is the nearest structural cousin (flagged for future passes, not asserted here).

## Uncertainties

1. **Contract naming by jurisdiction** (tenancy agreement vs lease vs licence agreement; UK ASTs): product pages say "lease"; jurisdictional instruments were not researched. Stated generically in the final document.
2. **Installment mechanics** (number of installments, due-date conventions, term alignment): confirmed as configurable ("multiple installment terms, move-in/move-out dates... on demand") but no defaults asserted.
3. **University nomination/master-lease support** (operators contracting blocks of beds to institutions): appears in customer-story framing only; dedicated software machinery not evidenced — not asserted.
4. **Guarantor workflow depth** at StarRez and AppFolio: the guarantor concept is explicit at RealPage and Entrata (platform nav); StarRez PBSA page does not surface it. Kept qualified ("common in mature products; depth varies").
5. **Help-center-level operational detail** (exact object model, state names, permission models): StarCare login-walled; Entrata/RealPage public docs not reachable at fetched URLs. All behavioral claims are calibrated to product-page evidence; no precise numeric/limit claims drawn.
6. **Residence-life depth in PBSA deployments** (how far operators actually use StarRez community/conduct tools): packaging evidence only; usage depth unknown.
7. **Meal plans** on the operator side: not evidenced in any operator stack (StarRez meal-plan features appear in its Higher-education materials); excluded from this leaf.

## Final Synthesis

**Student Housing Management** (§17, real-estate family) is the *operator vantage* of student-housing software: the system of record for a business that leases student residential space for revenue. Its defining core is three jointly-held structures:

```text
Student rental portfolio (properties → units → beds)
  ↓
Per-space tenancy (lease between operator and resident for a specific space + term;
enrollment-aligned terms; installment rent; per-resident ledger; configurable
bed-level or unit-level granularity)
  ↓ produced by the leasing funnel (enquiry → application → screening/guarantor → signed lease)
  ↓
Enrollment-cycle occupancy management (pre-leasing/next-period occupancy goals →
placement of residents into spaces with roommate coordination → portfolio-scale
annual turn → renewals/rebooking for the next cycle)
```

Everything else — bulk operations, matching questionnaires, turn checklists, rent automation, portals, marketing/distribution, accounting, analytics, and the residence-life tools that ride along at the PBSA pole — is common mature or optional structure layered on that spine.

**Keep-both ratified with Campus Housing Management (§23)**: one phenomenon, two business vantages, two occupancy instruments (lease vs governed assignment), two money paths (rent ledger vs student account). **RPM forward flag discharged**: the seam to Residential Property Management is the enrollment-cycle tenancy structure; students-as-tenants alone is RPM. **Hostel seam confirmed**: nightly travelers vs academic-year contracts, bridged only by distribution tooling at one vendor.
