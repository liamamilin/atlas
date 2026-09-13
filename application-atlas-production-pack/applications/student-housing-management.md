# Student Housing Management

## Overview

A **Student Housing Management** application is the operator-side system of record for running student housing as a rental business: it holds the portfolio's leasable space inventory (properties, units, and — dominantly — individual beds), creates occupancy through lease agreements signed with individual student residents, rents on terms aligned to the academic year, and runs the whole business around a single annual rhythm — selling and placing next year's residents before the current year ends, then turning the entire portfolio over in a concentrated move-out/move-in window.

It is used by the organizations that own or operate student rental portfolios for revenue: purpose-built student accommodation (PBSA) operators, off-campus student-housing owners and managers, and multifamily companies with student communities — whether a few houses near a campus or global bed portfolios.

The defining structure is small:

```text
Student rental portfolio (properties → units → beds)
  → tenancy: a lease between the operator and an individual resident
    for a specific space and term (enrollment-aligned dates, installment rent,
    per-resident ledger; bed-level or unit-level granularity)
  → the enrollment cycle: pre-leasing of next-period occupancy → placement of
    residents into spaces → the annual turn → renewals/rebooking
```

Two things distinguish this from ordinary landlord software. First, the tenancy structure: a bed inside a shared unit can carry its own lease, rate, dates, and ledger independently of the other beds in that unit. Second, the calendar: the business's occupancy, sales, and operations are organized around the academic year, with next period's occupancy tracked and sold ahead of time as a first-class state. When a landlord simply rents units year-round to whoever applies — students included — that work belongs to residential property management; when the resident's right to occupy flows from an institutional assignment rather than a lease, it belongs to campus housing management (see Related Application Types).

## Users & Context

Primary users are the staff of the operating business:

- **Leasing staff** run the revenue machine: they work leads through the funnel (enquiry, application, qualification), issue and sign leases, and hit occupancy and pre-leasing goals. Their central metric is next-period occupancy — how many of the portfolio's beds are committed for the coming academic term, and how fast that number is moving.
- **Property/site managers** run the buildings: move-ins and move-outs, inspections, damage charges, maintenance, vendor work, and the resident relationship during the tenancy.
- **Central operations and accounting staff** run the money and the portfolio: rent ledgers and installments, deposits and refunds, arrears, corporate accounting, and reporting to owners and investors on occupancy, turnover, and financial performance.

Secondary participants:

- **Students** are the tenants — first-class actors through the resident portal: they enquire, apply, sign, pay, request maintenance, and connect with roommates. Qualification commonly runs through guarantors (often parents) rather than income history.
- **Owners and investors** receive the reporting output: occupancy and turnover by property, leasing velocity against goals, and financial performance.
- **Distribution channels** sit structurally connected rather than seated: listing sites and property websites feed the funnel; at one end of the market, operators also fill vacant beds through travel-booking channels.

The context is fundamentally seasonal. The business year is dominated by one leasing window (open well before the academic term starts), one turn (the compressed period when most of the portfolio changes occupants at once), and one rebooking cycle (getting current residents to commit to the next year). In-term operations — rent collection, maintenance, resident service — are steady-state work compressed between those peaks.

## Core Model

### The Defining Core

**Leasable space inventory.** The portfolio is modeled as individually leasable spaces organized in a hierarchy — property or community → building → unit/floorplan → **bed**. The bed is the characteristic unit of student housing: a shared apartment is not one rental but several, and the inventory exists so each bed can be marketed, priced, leased, and tracked on its own. The same structure carries unit-level leasing (whole apartments rented to a group) as a configuration rather than a different system. The inventory is the anchor everything else refers to.

**Tenancy.** Occupancy is created by a **lease or equivalent agreement between the operating business and an individual resident (or resident group) for a specific space and a fixed term**. The tenancy is produced by a commercial leasing funnel — enquiry, application, qualification and screening (commonly guarantor-based rather than income-based), offer, signed agreement — and it carries the resident's rent obligation on a **per-resident ledger**: even four roommates in one apartment are typically four independent financial records. Two structural properties of the tenancy matter:

- **Enrollment-aligned terms.** The lease term is keyed to the academic year, not an arbitrary anniversary. Rent is commonly structured as installments spreading the term's total across the occupancy period rather than a conventional monthly market rent.
- **Per-space granularity as a configuration.** Whether each bed is leased separately (the resident owes only their own rent) or the unit is leased jointly (signers share liability) is a business-model choice made per property — mature products support both explicitly.

**The enrollment cycle.** The third structure is temporal: the portfolio's occupancy is planned, sold, placed, and turned around the academic year.

- **Pre-leasing** — next-period occupancy is sold before the current period ends. The percentage of next term's beds committed (pre-leasing rate), leasing velocity, and goal attainment are the numbers the business runs on, tracked at property and bed level.
- **Placement** — applicants and returning residents are placed into specific beds and units, balancing their preferences (and roommate wishes) against availability. Placement is a continuous, board-shaped activity during the leasing window, not a one-time configuration.
- **The turn** — at term end, the portfolio executes a concentrated move-out → inspect/charge → make-ready → move-in cycle, operated in bulk across hundreds or thousands of spaces in a short window.
- **Rebooking/renewal** — getting current residents to sign for the next year is run as a campaign (bulk renewal offers, often with tiered pricing), because retaining a resident costs less than finding a new one.

These three structures are jointly load-bearing. An inventory with no leases is a listings database. Leases without the enrollment cycle are ordinary lease administration. A leasing cycle without tenancies is a sales pipeline. Together they are what makes the software a student-housing system rather than a generic one.

### Standard Capabilities Around the Core

Mature products commonly add:

- **Leasing funnel CRM** — leads and guest cards, automated prospect communication, online applications, tenant screening, e-signature leasing, and per-bed rate publication.
- **Roommate coordination** — matching questionnaires (lifestyle, habits, study), roommate search and self-selection before move-in, and matching-assisted placement.
- **Bulk operations** — the default operating mode at portfolio scale: bulk lease-term updates, bulk renewal offers, bulk notices and move-outs, bulk assignments, bulk communication.
- **Turn machinery** — move-in/move-out checklists, mobile inspections with photos, damage assessment and per-resident charges, make-ready tracking.
- **Rent machinery** — installment schedules, recurring payments, per-resident ledgers, deposits, arrears handling, and refunds.
- **Occupancy and revenue analytics** — pre-leasing percentages, velocity, bed-level KPIs and forecasts; at the enterprise tier, per-bed revenue management and market benchmarking.
- **Maintenance and facilities** — work orders, vendor management, unit condition.
- **Resident portal** — pay rent, request maintenance, complete move-in tasks, connect with roommates, receive communications.
- **Marketing and distribution** — property websites, listing syndication to student-rental sites; at the PBSA end, connectivity to travel-booking channels to fill vacant beds.
- **Accounting and owner reporting** — receivables and payables, general-ledger integration, owner/investor statements.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:   Leasable space
Implementations:  bed, room, unit/floorplan — configured per property

Concept:   Tenancy instrument
Implementations:  individual lease per bed, joint lease per unit
                  (jurisdictional contract naming varies: lease, tenancy
                  agreement, licence agreement)

Concept:   Qualification
Implementations:  credit/income screening, guarantor co-signing,
                  combinations of the two

Concept:   Rent structure
Implementations:  installment schedules across the term,
                  conventional periodic rent

Concept:   Placement
Implementations:  staff allocation, resident self-selection,
                  matching-assisted assignment
```

A reader who encounters only one implementation (for example, only by-the-bed US off-campus leasing) should still be able to recognize the others — a UK PBSA operator letting rooms on fixed-term agreements, or a small landlord running joint leases on student houses — from this core.

## How It Works

### The annual leasing cycle

```text
Configure the next term's inventory and rates (beds, floorplans, per-bed pricing)
→ open leasing: publish availability to websites and listing channels
→ work leads through the funnel: enquiry → application → screening/guarantor
→ issue and sign leases (offers, e-signature)
→ track progress against occupancy and pre-leasing goals (property and bed level)
→ place residents into specific beds/units as commitments accumulate
   (staff assignment or resident self-selection, roommate preferences applied)
```

This cycle is the system's defining rhythm and its main revenue engine. Everything in it is measured: how many beds are committed, at what rate commitments are arriving, which properties are behind goal, what price adjustments might close the gap.

### The turn

```text
Term ends → bulk move-outs processed across the portfolio
→ inspections performed (mobile, with photos) → damage charges posted to ledgers
→ units made ready → move-ins executed against signed leases
   (checklists, pre-arrival information, scheduled to avoid congestion)
```

The turn is time-boxed and portfolio-wide; bulk processing of move-outs, notices, inspections, and assignments is what makes a short window survivable at scale.

### Living-phase operations

```text
Resident in occupancy
→ rent collected per schedule (installments, recurring payments, arrears worked)
→ maintenance requests submitted and tracked → inspections and condition records
→ communication and community through the portal
```

### Rebooking and renewal

```text
Mid-cycle → renewal/rebooking campaign: bulk offers to current residents
(often tiered or revenue-managed pricing)
→ commitments roll the resident into next term's placement picture
→ remaining beds continue through the open leasing funnel
```

### Capability tiers

**Defining core** — without these, not student housing management:

- leasable space inventory with per-space granularity (bed-level capable)
- lease tenancy between operator and resident, produced by a leasing funnel
- per-resident rent ledger against the tenancy
- enrollment-aligned terms and the pre-leasing → placement → turn → rebooking cycle

**Standard capabilities** — present in most modern products:

- funnel CRM, screening, e-signature; roommate matching and self-selection
- bulk operations, turn machinery, inspections and damage charges
- installment rent, payments, deposits, arrears
- occupancy/pre-leasing analytics; maintenance; portals; accounting and owner reporting

**Variant / optional** — depends on segment, geography, and packaging:

- by-the-bed (several liability) vs by-the-unit joint leases — per-property configuration
- travel-channel distribution for vacant-bed fill; community/residence-life tooling
- revenue management, market benchmarking, and AI pricing at enterprise tiers
- ancillary products (insurance, deposit alternatives, utility billing)

## Interfaces

### Leasing pipeline / funnel CRM

The leasing staff's working surface.

- information: leads and guest cards by property, application status, screening results, leasing velocity against goals
- primary actions: work a lead, issue an offer, generate and sign a lease, communicate with prospects

### Placement board / assignment board

The occupancy-composition surface.

- information: per-property bed inventory, committed and open spaces, future residents awaiting placement, roommate preferences
- primary actions: place a resident into a bed or unit (individually or by bulk drag-and-drop), manage waitlists, generate placement documents

### Occupancy and pre-leasing dashboards

The management layer.

- information: pre-leasing percentages, leasing velocity, occupancy and turnover by property, bed-level rate and availability views, financial performance
- primary actions: adjust rates, compare properties against goals, forecast the leasing season

### Lease and application surfaces

- information: application forms, screening outcomes, lease documents, guarantor records, e-signature status
- primary actions: apply, qualify, co-sign, sign, execute the lease

### Turn and inspection surfaces

- information: move-in/move-out task checklists, inspection items with photos, outstanding make-ready work
- primary actions: process move-outs, record condition and damage, charge ledgers, schedule and complete move-ins (frequently mobile, on-site)

### Resident ledger and billing

- information: per-resident charges, installments due and paid, deposits, arrears
- primary actions: post charges, take payments, refund deposits, work delinquencies

### Resident portal

The tenant's self-service surface across the whole lifecycle.

- information: lease documents, balances and payment history, roommates, requests
- primary actions: enquire and apply, sign, pay rent, submit maintenance requests, complete move-in tasks, communicate with the operator and other residents

### Owner / investor reporting

- information: portfolio occupancy, leasing performance, financial statements
- primary actions: configure and deliver reports

## Important Rules / Behaviors

### One space, one active tenancy

A bed (or unit) holds one active lease at a time; availability shown to prospects and placement boards reflects that constraint in real time. The portfolio's sellable state is always the truth of which spaces are committed for which term.

### The lease governs occupancy

Occupancy rights flow from the signed agreement — its space, its dates, its money terms — not from administrative assignment. Mid-term occupancy changes (transfers, re-assignments) are therefore contract operations (new or amended agreements), not administrative edits.

### The next period is sold before the current one ends

Pre-leasing is a first-class tracked state, not a report written after the fact. Commitments for the coming term coexist with the current term's occupancy; the same bed can be occupied now and committed for next term.

### Money is per-resident, even inside one shared unit

Each resident carries an individual ledger for their share of the rent, deposits, and damage charges. Liability between roommates is a per-property configuration: under by-the-bed leasing each resident owes only their own rent; under a joint lease the signers share liability for the whole. Software that cannot hold independent ledgers inside one physical unit cannot run this business.

### The turn is a portfolio-scale bulk event

During the turn window, bulk processing is the normal mode of operation — bulk move-outs, notices, inspections, assignments, communications — because the volume compresses into weeks. Single-transaction workflows exist but are the exception path.

### Renewal is a campaign

Rebooking current residents into the next term runs as a bulk, deadline-driven campaign with its own pricing logic, tracked alongside new-lease sales in the same occupancy picture.

### Qualification is shaped to student renters

Students typically lack rentable income or credit history, so qualification commonly runs through guarantors (often parents) co-signing the lease; screening adapts accordingly. This shapes the funnel's data model (guarantor records bound to applications and leases) even though depth varies by product.

### Vacant stock can be redistributed

Some operators — most visibly PBSA specialists — fill unsold or short-gap beds through short-stay channels, connecting the same inventory to travel-booking distribution. The tenancy spine stays the center; this is an optional sales channel, not a second business model.

## Variants

- **PBSA specialist operators** (UK, Europe, Australia) — purpose-built portfolios let per room on fixed-term agreements; strong portal-centric resident experience; short-stay channel fill; in some deployments, community and resident-experience tooling carried over from campus practice.
- **Off-campus student communities (US multifamily style)** — by-the-bed individual leasing on installment schedules, guarantor-based qualification, revenue management per bed.
- **Generalist PM configured for student** — mid-market operators running student portfolios on a suite that also manages other property types; the student layer (placement boards, pre-leasing metrics, flexible lease structures) arrives as a capability set rather than a dedicated platform.
- **Lease-structure configurations** — by-the-bed (several liability), by-the-unit joint-and-several, or a mix across a portfolio; room-level or unit-level granularity per property.
- **Scale tiers** — enterprise platforms serving thousand-bed operators; mid-market suites; small operators running a handful of shared houses, where the same core appears with far lighter machinery.
- **Adjacent populations on the same structures** — co-living and staff housing share the per-room leasing pattern; boarding schools share the enrollment cycle; these are neighboring uses of the same software family rather than this Type's center.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Campus Housing Management | sibling (same phenomenon, other vantage) | The institution housing office's system: occupancy is created by a **governed assignment** of an institution-population member, eligibility derives from enrollment standing, charges flow to the student account, and residence-life operations are standard. Here, occupancy is created by a **lease with a commercial counterparty**, money flows as rent to a tenant ledger, and leasing velocity is the center. The platform market overlaps (one leading vendor sells both deployments), but removing the lease from this Type collapses it into that one, and removing assignment governance collapses that one into this. |
| Residential Property Management | closest neighbor | Both are lease-led landlord systems with ledgers, maintenance, and accounting. The seam is the **enrollment-cycle tenancy structure**: per-space (bed-level capable) tenancy granularity, academic-year terms with installment rent, pre-leasing-driven annual windows, roommate placement, and the portfolio-scale turn. A landlord renting ordinary year-round units to students is using residential property management; the moment the tenancy structure and operations organize around the enrollment cycle, this Type begins. |
| Hotel Property Management System | adjacent (transient lodging) | Nightly guests, folio per stay, housekeeping-driven room state — versus term-length tenancies with rent ledgers. The seam is bridged, not merged: some operators redistribute vacant beds through short-stay channels while the lease spine remains the record. |
| Hostel Management System | adjacent (transient lodging) | The dorm-bed inventory resembles the student bed, but stays are nightly and money is per-stay; student housing leases run on academic-year terms. |
| Short-term Rental Management | adjacent | Transient nightly inventory and calendars versus fixed academic-term tenancies. |
| Affordable Housing Management | adjacent (eligibility-governed) | Occupancy gated by housing-program rules (income certification) versus market leasing shaped to student renters (guarantors); different governing rule sources over a similar funnel. |
| Rental Application Platform / Tenant Screening Platform | funnel slices | Application intake and screening appear inside this Type's leasing funnel as capabilities; the standalone Types center only that slice. |
| Rent Collection Platform / Tenant-Resident Portal | capability slices | Payments and the resident-facing surface are standard capabilities here, not systems of record. |
| Property Listing Platform | upstream channel | Listing and syndication feed the funnel; they hold no tenancy, placement, or ledger state. |

## Representative Products

- **StarRez** — the leading student-housing platform, sold into both Higher Education (institution vantage) and Student Property Management/PBSA (operator vantage); included here for the PBSA/operator deployment and its international PBSA customer base
- **Entrata Student** — the student line of a major multifamily operating platform; leasing, turn, and bulk-assignment machinery with per-bed revenue tooling
- **RealPage Student (OneSite for Student Housing)** — the other major multifamily-stack student line; explicit by-the-bed/by-the-unit flexibility plus a dedicated student analytics and revenue-management tier
- **AppFolio** — a generalist property-management suite with gated student-housing capabilities (placement board, pre-leasing metrics, flexible by-the-bed/joint leasing), representing the configured-generalist pole

The definition was checked against that generalist pole and against the platform serving both vantages, so it does not depend on any one vendor's packaging, and against non-US (PBSA) practice so it does not depend on US lease structures.

## Sources

Research date: **2026-09-10**

- StarRez — Student Property Management (PBSA) solution: https://www.starrez.com/solutions/student-property-management-pbsa
- Entrata — Entrata Student: https://www.entrata.com/solutions/student
- RealPage — Property Management for Student: https://www.realpage.com/student/property-operations/
- AppFolio — Student Housing: https://www.appfolio.com/markets/student-housing

Corroborating official pages (search-verified): Entrata industries page (entrata.com/industries/student-housing) and Student Revenue Intelligence (entrata.com/products/srm); RealPage Student hub (realpage.com/student/), Renter Engagement for Student (realpage.com/student/renter-engagement/), Student Property Management brochure PDF, and Asset Optimization for Student (realpage.com/student/asset-optimization/); AppFolio Winter 2024 product update (appfolio.com/articles/2024-q4-product-update) and Granite customer story.

> Sourcing limitation: evidence rests on official product and solution pages; vendor help centers were not reachable from the research environment (login-walled or not publicly exposed). Behavioral descriptions are calibrated accordingly: operational specifics such as installment-count defaults, exact state names, and numeric limits are intentionally not asserted, and claims supported by fewer than two products are kept qualified. Vendor scale figures (channel counts, bed counts, satisfaction scores) are recorded in the research notes as vendor claims, not as structure. Detailed observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
