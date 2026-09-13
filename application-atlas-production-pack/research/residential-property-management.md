# Research Notes — Residential Property Management

Research date: 2026-09-09
Leaf: Residential Property Management (DIRECTORY.md §17 Construction, Real Estate & Facilities)
Slug: residential-property-management

---

## Research Goal

Understand what a Residential Property Management (RPM) application is as an Application Type: what objects it manages (properties, units, tenancies, rent, maintenance, owners), how the lead-to-lease and recurring tenancy loops flow, how turnover works, and where the Type's boundaries sit against the many neighboring §17 Types (Commercial PM, Affordable Housing Management, Rent Collection, Property Maintenance, Rental Application, Tenant/Resident Portal, HOA, Short-term Rental, Student Housing, Security Deposit, Listing Platform, Lease Administration).

This pass also carries joint-review obligations recorded by earlier passes:

- affordable-housing-management (processed 2026-09-06) flagged "joint review when Residential Property Management is processed" — the shared-spine/program-layer seam.
- rental-application-platform (processed 2026-09-09) recorded the suite-pole seam (application = intake step of the lead-to-lease cycle inside PM suites) and left a forward flag for tenant-screening-platform.
- lease-administration (processed 2026-09-08) left an evidence-gap note: lessor-side lease-administration structures inside PM suites were unobserved; future PM passes should corroborate.
- rent-collection-platform (processed) recorded the money-in-slice seam with removal tests.
- property-maintenance-management (processed) recorded the maintenance-module seam.

## Initial Boundary

Working hypothesis before research:

- RPM is the operator-side system of record for running rental residential housing: property/unit inventory, tenancies under leases, rent charges and collection, leasing of vacancies, maintenance, and (for third-party managers) owner accounting.
- Expected neighbors: Commercial PM (negotiated lease instruments vs standardized consumer leases), Affordable Housing (program/compliance layer), Rent Collection (money-in slice), Property Maintenance (work-item primacy), Rental Application Platform (application machinery), Tenant/Resident Portal (resident-facing surface), HOA/Community Association (owner assessments vs tenant rent), Short-term Rental (transient stays), Student Housing (enrollment cycles), Security Deposit Management (deposit trust machinery), Property Listing Platform (public demand-side venue), Lease Administration (occupier side).
- Risk: the market phrase "property management software" is used loosely — vendors sell one platform across residential, commercial, association, student, storage, and vacation markets. The Type must be anchored on the residential tenancy operation, not on vendor platform breadth.

## Research Questions

1. What are the core objects (property, unit, tenant/resident, lease, charge, payment, work order, applicant/prospect, owner, vendor)?
2. How does the lead-to-lease cycle work (marketing/listing syndication → inquiries/leads → showings → application → screening → lease execution → move-in)?
3. How does the recurring tenancy loop work (rent posting, autopay, late fees, arrears, renewals, increases)?
4. How does turnover work (notice, move-out, inspection/condition reports, deposit disposition, make-ready, re-marketing)?
5. How is maintenance handled (requests → triage → staff/vendors → completion → charge-back)?
6. What owner accountability machinery exists (statements, distributions, trust accounting), and is it definitional or operator-type dependent?
7. How do product shapes differ across customer tiers (professional PM companies vs self-managing landlords)?
8. What is regional/variant machinery vs the stable core?

## Representative Products

Selected for market representation + documentation accessibility + different philosophies + different customer tiers:

| Product | Vendor family | Segment / philosophy | Evidence level obtained |
|---|---|---|---|
| Buildium | RealPage | All-in-one platform for professional PM companies and landlords; accounting-first; SMB/mid | Tier 1–2 (homepage + residential portfolio page + Help Hub with official article summaries) |
| AppFolio | AppFolio, Inc. | Mid/enterprise cloud platform; leasing-funnel and AI-forward; mixed markets | Tier 2 (homepage + marketing & leasing product page) |
| Propertyware | RealPage | Single-family PM companies; customization-first, open API | Tier 2 (homepage + feature catalog) |
| Rent Manager | London Computer Systems | Configurable multi-industry platform; accounting/reporting depth; mid-market | Tier 2 (homepage + residential industries page) |
| TurboTenant | TurboTenant, LLC | DIY landlord-first; free core, tenant-pays model; small portfolios | Tier 2 (homepage + features page) |

The sample spans: DIY individual landlords (TurboTenant) → SMB professional PM companies (Buildium, Propertyware) → mid/large operators (AppFolio, Rent Manager); and four product philosophies: accounting-first suite (Buildium), leasing-funnel/AI platform (AppFolio), customization/open platform (Propertyware, Rent Manager), free-tenant-pays DIY tool (TurboTenant).

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Buildium — homepage: https://www.buildium.com/ (Tier 2; includes official FAQ with product history and positioning)
- Buildium — Residential Property Management: https://www.buildium.com/portfolios/residential-property-management/ (Tier 2)
- Buildium — Help Hub: https://www.buildium.com/help-hub/ (Tier 1 landing page; official summaries of knowledgebase articles: accounting start date, opening balances, bank reconciliation, locking accounting books for trust-accounting compliance, eSignature for leasing, data import of tenants and leases, tenant screening powered by TransUnion, ePay basics, ePay hold days, recording bank deposits)
- AppFolio — What is property management software: https://www.appfolio.com/property-management-software/ (Tier 2)
- AppFolio — Marketing & Leasing: https://www.appfolio.com/property-manager/marketing-leasing (Tier 2)
- Propertyware — homepage: https://www.propertyware.com/ (Tier 2; full feature catalog in navigation)
- Rent Manager — homepage: https://www.rentmanager.com/ (Tier 2)
- Rent Manager — Residential Properties: https://www.rentmanager.com/residential-properties/ (Tier 2)
- TurboTenant — homepage: https://www.turbotenant.com/ (Tier 2)
- TurboTenant — Features: https://www.turbotenant.com/features/ (Tier 2)

Failed / limited sources (per retry discipline):

- Buildium knowledgebase topic catalog (https://help.buildium.com/hc/s/topiccatalog) and individual help articles (e.g. /hc/s/article/Data-Import-Tenants-and-leases) are a Salesforce-hosted SPA that returns a CSS error to the fetcher on both attempts — direct article text unreachable. Evidence from the Help Hub landing page (official article titles + one-line official summaries) is used instead; no precise operational parameters (fee amounts, hold-day counts, state rules) are asserted from memory.
- Yardi (yardi.com) was not attempted this pass: prior sibling passes (commercial PM, affordable housing) recorded 403s on Yardi enterprise surfaces; Yardi Breeze is retained as a market anchor only, consistent with those passes.
- RealPage corporate surfaces were not attempted: prior passes recorded help center behind product login and 404s. Buildium and Propertyware (both RealPage companies) were used as the reachable RealPage-family evidence.
- No non-US (UK/EU/AU) vendor was directly sampled this pass; regional practice is handled via the historical/market-sample check and is asserted cautiously.

## Product Observations

### Product A — Buildium (professional PM companies + landlords; US)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "all-in-one property management software… purpose-built for the unique tasks of property managers and real estate professionals." Official FAQ: "Buildium is purpose-built for residential property management—including single-family and multi-family rentals and community associations—and can also handle mixed portfolios with student housing, commercial properties, storage units, and more." Customers "include both landlords and third-party property management businesses with mixed portfolios… growing portfolios all the way to fifteen thousand plus" (vendor claim). Founded 2004; software launched 2008 (official FAQ).
- Platform capability map (official navigation): Leasing; Accounting and Payments; Resident Experience; Portfolio + Revenue Growth; Marketing; Business Operations; AI; Automation; Customization.
- Key features (official): property accounting (automatic bank reconciliation, 1099 e-filing, property-specific financial reporting); online rent collection (ACH and credit card, funds auto-transferred, optional transaction fees); maintenance requests (work orders, 24/7 status tracking, recurring tasks, integrated bill/invoice management); rental listing syndication ("one-touch syndication… across top rental sites"); tenant screening (instant credit, criminal, eviction reports; custom pre-screening criteria per property); property management website; online leasing ("100% digital, paper-free leasing process"); Resident Center; maintenance contact center; marketplace integrations; open API.
- Residential page workflow framing: "Manage operations and communication with applicants, tenants, vendors, and owners." Four named jobs: attract higher-quality tenants (free website → post listings → receive applications → screen → execute online leases with eSignatures → accept security deposits via online payment); keep residents happy and renewing (residents submit maintenance requests and manage payments from mobile; announcements board); keep property owners in the loop (owner portal: financial statements, leases, receipts; email/mailing templates); eliminate vendor paperwork (manage and pay vendor expenses alongside company bills; track productivity so work orders are assigned to the most efficient vendors).
- Help Hub (Tier 1 article summaries, official): accounting start date as a "line in the sand" between bank and software; entering opening balances per property; bank reconciliation ("a critical task in property management"); locking accounting books — "set lock dates for accounting periods so you're in compliance with trust accounting rules and regulations"; eSignature for leasing (lease templates, prepare and send lease agreements); data import order — "After your properties and units have been entered into Buildium, you can begin to add your people… adding a tenant and a lease to a unit easy by creating both at the same time"; tenant screening "powered by TransUnion"; ePay basics (tenants pay electronically); ePay hold days; recording bank deposits "from tenants, association owners, or rental owners" (three payer types in one system).

### Product B — AppFolio (mid/enterprise operators; US)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "Rental property management software helps landlords and property managers manage rental properties, residents, and payments. It typically includes features like tenant screening, lease agreement management, rent collection, tenant communication, work order management, and financial reporting." Official FAQ describes the property management company's job: "marketing and advertising available properties, screening tenants, collecting rent, responding to tenant requests, maintaining properties, and managing finances."
- Marketing & Leasing page — the leasing funnel as a first-class structure: "complete command over every stage of the leasing funnel… from lead generation to qualification and — before you know it — move in."
  - Leasing CRM: "one guest card for every lead, tracked across your portfolio"; automated prioritized to-do lists.
  - AI leasing assistant (Realm-X Leasing Performer): autonomously handles lead-to-lease — nurturing leads, scheduling tours, updating guest cards.
  - FolioScreen screening: customizable rental applications, criminal/background checks, income/ID/employment verification, fraud detection, Fair Housing compliance.
  - Leasing Signals: pricing suggestions for units and renewals from comparable public data.
  - Vacancy machinery: vacancy dashboard (all posting links and tasks), one-click vacancy posting to website + internet listing services, premium listing syndication (pay-per-verified-lead), marketing campaigns for multiple identical units (multifamily/student).
  - Applications and leases: online rental applications; online leases ("customized, branded lease or renewal offers… e-sign on the spot on any mobile device"); renewal automation ("default offer that automatically updates lease dates, rent amounts, and status upon the current lease expiration").
  - Tours: 3D virtual tours, self-guided tours, virtual showings, ID verification for showings.
  - Scale operations: bulk move-outs ("move out a large number of residents at once, set move-out dates, add charges and credits, and create work orders in a few steps"); bulk lease renewals (predefined offers, renewal offers and monthly charges in one workflow); bulk pricing; rent by-the-bed (separate leases and tenant ledgers by-the-bed for student housing).
- Separate product surfaces for the same platform: Resident portal, Owner portal, Vendor portal, Investor portal logins. Markets: single-family, multifamily, student housing, affordable housing, community associations, commercial.

### Product C — Propertyware (single-family PM companies; US)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "the most powerful, customizable and open platform designed for performance-minded Single Family property management companies."
- Feature catalog (official navigation): Online Leasing (websites, lead tracking, listing & syndication, application portal, tenant screening, electronic signature, leasing contact center); Property Management (payments, tenant & owner portals, text messaging, contact center); Maintenance (inspections, work orders, maintenance contact center); Accounting (receivables/payables, bank reconciliation, fee management — described as "Owner Management"); Operations & Risk (reporting, open API two-way data exchange, multi-location management, owner and tenant insurance, utility management & billing).
- Differentiators claimed: custom dashboards, unlimited custom reports, self-service owner portal, customization of workflows, open data access.
- Pricing is per unit per month with monthly minimums (marketing figures — recorded in notes only, not asserted in the final document).

### Product D — Rent Manager (configurable multi-industry platform; US)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "property management software for companies that handle real estate portfolios of every type and size… From accounting and operations to leasing and maintenance, it unifies every aspect of your business in one fully integrated platform."
- Accounting: "complete accounting system… functions in cash and accrual accounting simultaneously"; AR/AP, payments, electronic bank reconciliations, tax tools, budgeting.
- Reporting: 450+ reports including "property management specifics like Rent Rolls and Vacancy Reports"; report writer; financial report writer.
- Marketing & Leasing: "push your unit and property information directly from your database onto the industry's major ILS platforms"; guest cards; online applications ("Rent Manager will automatically create a new prospect record for you upon completion"); screening via built-in AmRent integration (credit, criminal, rental history); signable documents signed in the Tenant Web Access (TWA) portal.
- Business operations: automated notifications; task automation "perfect for recurring charges, bills, and fees that require monthly posting"; custom workflows; KPIs; Market Rent Analysis report (Gross Potential Rent for units); Profit & Loss Forecast; owners module; call center; renters insurance (LeaseTrack — "automatically tracks compliance and force-places uninsured residents onto a master policy").
- Maintenance: service issues; maintenance scheduling; work orders/billing; inspections; make-ready boards ("streamline the labor- and time-intensive make-ready process"); utility management; mobile app where "maintenance techs can check in and out of jobs."
- Communication: texting, phone broadcast, email, web chat; built-in word processor with letter templates.
- Resident app (rmResident): "make and view payments, submit maintenance requests and review the status of existing issues."
- Industries served: residential, commercial, manufactured housing, associations, student housing, RV park & campgrounds, self storage, affordable housing, vacation homes.

### Product E — TurboTenant (DIY landlords; US)

Evidence layer: A (directly observed on official pages).

Key observations:

- Positioning: "property management services and software for landlords… For the hands-on landlord, TurboTenant puts professional-grade software in their hands to centralize rental marketing, rental applications, tenant screenings, state-specific lease agreements, rent collection and daily landlord workflows without relying on filing cabinets and spreadsheets." Two modes: DIY software (free) or fully managed service ("Autopilot", flat fee).
- Business model: "core functionality, including rental property marketing, tenant screening, and rent collection, is free for landlords. We make money when tenants pay for a screening or submit their rent payments."
- Feature set (official features page): rental advertising (build one listing, auto-post to "dozens of popular renter sites — like Rent., Redfin, and Craigslist"; lead tracking with pre-screeners — move-in timeline, smoking, pets; in-app messaging; showing scheduling with reminders); rental applications (industry-standard questions, up to 5 custom questions on premium, screening report paid by the tenant, fraud detection via Snappt on premium); screening (credit, criminal, eviction; $0 for landlords); leases (state-specific lease builder — "select which state your rental is located, add your lease specifics, and generate an up-to-date lease agreement"; e-sign; month-to-month and room-rental variants; addendums; landlord forms pack); condition reports ("move the outdated process of move-in and move-out inspections online… send it to tenants for signatures"); maintenance requests (tenants submit from their portal "so you can keep a paper trail"); rent payments (autopay; custom late fees — "choose between one-time or daily rules"; automatic reminders "until they pay"; receipts "even if it isn't through TurboTenant" — offline payment recording); accounting (income and expenses by property, expense tracking, "retire your spreadsheets"); renters insurance requirement (upload proof or purchase through partner).
- Property types: single-family homes, townhomes, condos, small multi-family (2–4 doors), apartment buildings (5+ doors), room rentals, other (RV park, garage space).
- Scale claims (marketing, notes only): 1m+ landlords, 2m+ units, 12m+ renters, $6b+ rent.

## Cross-product Comparison

| Dimension | Buildium | AppFolio | Propertyware | Rent Manager | TurboTenant |
|---|---|---|---|---|---|
| Managed stock | properties + units (import order: properties/units first) | units, unit types, campaigns | properties | properties/communities | properties (SFH → apartments, rooms) |
| Tenancy record | tenant + lease created together on a unit | lease + renewal offers; move-ins | leases | tenant records + signable lease docs in TWA | lease builder + e-sign + condition reports |
| Rent cycle | ePay ACH/card; hold days; deposits via online payment | rent payments; renewal rent updates | payments module | recurring charges/bills/fees auto-posted monthly; AR | autopay; custom late fees (one-time or daily); reminders; offline receipts |
| Leasing pipeline | one-touch listing syndication; applications; screening (TransUnion); e-sign leases | full funnel: guest cards → CRM → AI assistant → applications → screening → online lease → move-in; renewal automation; bulk ops | websites, lead tracking, listing & syndication, application portal, screening, e-signature | ILS push; guest cards; online applications auto-create prospect; screening (AmRent); signable docs | 25+ site syndication; leads + pre-screeners; showing scheduling; applications; screening (tenant-paid); state-specific lease builder |
| Maintenance | work orders; recurring tasks; contact center; vendor productivity tracking | maintenance module; work orders created at bulk move-out | inspections; work orders; contact center | service issues; scheduling; make-ready boards; inspections; mobile tech check-in/out | tenant-submitted requests; paper trail |
| Owner layer | owner portal (statements, leases, receipts); owner deposits | owner portal | owner portal; fee management ("Owner Management") | owners module; owner communication | none (landlord is the owner) |
| Accounting depth | full property accounting: GL, bank rec, trust-accounting lock dates, 1099 e-filing | accounting & reporting; AI bill entry | AR/AP; bank reconciliation; fee management | full GL cash+accrual; budgeting; 450+ reports; tax tools | income/expense tracking by property (no GL) |
| Resident surface | Resident Center (requests, payments, announcements) | resident portal | tenant portal | TWA portal + rmResident app | renter portal + app |
| Communication | templates; announcements | texting/email; AI lead replies | text messaging; contact centers | texting, phone broadcast, email, web chat, letter templates | in-app messaging; reminders |
| Portfolio breadth | residential core + associations, mixed-use, SF, multifamily, commercial, student, enterprise | single-family, multifamily, student, affordable, associations, commercial | single-family focus | residential + commercial, manufactured housing, associations, student, RV, storage, affordable, vacation | single-family → apartments, rooms (consumer scale) |

### What is shared (candidate common structure)

All five products, across tiers and philosophies, share:

1. A persistent stock of properties and rentable units held as the operator's portfolio.
2. A tenancy record binding a resident (household) to a unit under a lease/rental agreement.
3. A recurring rent cycle: periodic rent charges, online payment collection, late fees, arrears/reminders.
4. A leasing pipeline that fills vacancies: listing/marketing (with syndication to rental sites), lead capture, applications, screening, electronic lease execution, move-in.
5. Maintenance request intake and work-order handling tied to the unit/tenancy.
6. A resident-facing self-service surface (portal/app) for payments, requests, and communication.
7. Communication tooling with residents, applicants, vendors, and (where present) owners.

Professional-tier products (Buildium, AppFolio, Propertyware, Rent Manager) additionally share: owner accountability layer (owner portals, statements, management-fee handling), full property accounting (GL, bank reconciliation, trust-accounting controls), reporting/analytics, vendor management, and scale machinery (bulk operations, multi-location).

### Where products differ

- Customer tier: DIY landlords (TurboTenant — no owner layer, no GL, tenant-pays monetization) vs professional PM companies (the other four).
- Philosophy: accounting-first (Buildium), leasing-funnel/AI-first (AppFolio), customization/open-API (Propertyware, Rent Manager), free-DIY (TurboTenant).
- Portfolio breadth: residential-pure (TurboTenant, Propertyware) vs mixed-portfolio platforms serving associations/commercial/student/storage as additional markets (Buildium, AppFolio, Rent Manager).
- Turnover machinery: explicit make-ready boards and bulk move-outs (AppFolio, Rent Manager); condition reports (TurboTenant); not surfaced on the fetched Buildium/Propertyware pages (recorded as not-surfaced, not absent).

## Canonical Model (draft, pre-abstraction)

```text
Managed rental stock (properties → rentable residential units, occupancy state)
  └── Tenancy of record (resident household ↔ unit, lease/rental agreement, fixed periodic rent)
        ├── Rent cycle (recurring charges → payments/autopay → late fees → arrears → renewal/increase)
        ├── Maintenance (requests → work orders → staff/vendors → completion → charge-back)
        └── End of tenancy (notice → move-out → inspection/condition → deposit disposition)
  └── Turnover / leasing pipeline (vacancy → marketing/syndication → leads → showings
        → application → screening → e-sign lease → move-in → new tenancy)
  └── Owner accountability (third-party tier: statements, distributions, trust accounting)
  └── Property accounting (charges/payments/bills → per-property ledger → financials)
```

## Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable as Residential Property Management:

1. **The managed rental stock** — persistent properties and rentable residential units held as the operator's portfolio, each unit carrying occupancy state over time. Remove → a unit/asset inventory, or a listing site with no memory.
2. **The residential tenancy of record** — a resident household bound to a unit under a lease/rental agreement with a fixed periodic rent, living through move-in → occupancy → renewal or move-out. Remove → tenant contact records, or a lease database with no property substrate.
3. **The tenancy's rent cycle** — recurring rent and charges posted on the tenancy's terms, payments collected, arrears and late fees tracked. Remove → a leasing/occupancy CRM with no money loop.
4. **Turnover of the stock** — when a tenancy ends the unit returns to vacancy and is re-let to a new household; the system carries the unit across successive tenancies (the leasing pipeline is the machinery of this leg). Remove → an occupied-portfolio ledger that cannot refill units (rent-collection territory).

Jointly-held load-bearing: 1 alone = unit inventory; 2 alone = tenant contact records; 3 without 1+2 = billing/rent-collection machinery; 4 alone = leasing pipeline/listing tool; 1+2 without 3+4 = occupancy registry; 1+3 without 2 = anonymous unit billing; 2+3 without 1+4 = rent ledger (rent-collection territory); 1+2+3 without 4 = occupied-portfolio ledger that can't refill; 1+2+4 without 3 = leasing/occupancy CRM; 2+3+4 without 1 = lease database without property substrate.

Rationale: maintenance, owner accounting, portals, syndication networks, screening integrations, and full GL are all standard capabilities — a product lacking any one of them is still recognizable as RPM (TurboTenant proves the DIY floor: no owner layer, no GL, still unmistakably RPM). But remove the stock, the tenancy record, the rent cycle, or the turnover loop and the product becomes a neighboring Type.

### L1 — Common Mature Structure

Very common in mature products, not required for recognition:

- leasing pipeline machinery: listing creation and syndication to rental sites, lead/guest-card capture, showing scheduling, online applications, tenant screening (credit/criminal/eviction), electronic lease execution, move-in
- maintenance: resident-submitted requests, work orders with status, assignment to staff/vendors, vendor bill linkage, charge-back, recurring tasks, make-ready/turnover boards, inspections
- resident self-service portal/app (payments, requests, status, documents, announcements)
- communication tooling (text/email/phone/web chat, templates, reminders)
- owner accountability layer (owner statements, owner portals, management fees, distributions) — third-party tier
- property accounting (per-property ledgers, AR/AP, bank reconciliation, trust/escrow handling where third-party management requires it, owner distributions, tax-form support)
- reporting/analytics (rent roll, vacancy, delinquency, owner/property financials)
- vendor management (vendor records, work-order assignment, bill payment, productivity tracking)
- document management (leases, addenda, notices, receipts, condition reports)
- renewals (renewal offers, rent increases, lease-date updates)

### L2 — Variant / Optional Structure

Depends on segment, operator type, geography, scale, business model:

- operator type: self-managing landlords (no owner layer, simple accounting) vs third-party PM companies (owner funds, trust accounting, management fees) vs institutional multifamily operators (scale machinery, by-the-bed leasing)
- portfolio composition: single-family vs multifamily vs mixed; adjacent markets served by the same platform (associations, commercial, student, affordable, storage, vacation) as separate property-type configurations
- regional/jurisdictional machinery: state-specific lease templates and landlord-tenant law awareness (TurboTenant), trust-accounting regimes (Buildium lock dates), renters-insurance compliance/force-placement (Rent Manager), 1099 e-filing (Buildium) — US-flavored implementations; other markets have their own deposit-scheme and tenancy regimes (not directly sampled this pass)
- monetization shape: per-unit SaaS pricing (professional tier) vs free-landlord/tenant-pays (TurboTenant) vs managed-service flat fee
- era-current layers: AI leasing assistants, pricing suggestions, contact centers (leasing/maintenance), self-guided tours, ID verification, fraud detection, rent reporting to credit bureaus
- deployment: cloud SaaS dominant; open APIs/marketplaces as ecosystem strategy

### L3 — Vendor-specific Structure

Stays in Research Notes:

- Buildium: Resident Center, ePay hold days, maintenance contact center, Buildium Marketplace, Open API, Essential/Growth/Premium plans, "line in the sand" accounting start date, TransUnion-powered screening
- AppFolio: Realm-X Leasing Performer, Leasing CRM guest cards, FolioScreen Trusted Renter, Leasing Signals pricing, Premium Listing pay-per-verified-lead, rent by-the-bed, bulk move-outs/renewals/pricing, four portal types (resident/owner/vendor/investor), FUTU*RE* conference
- Propertyware: AssetProtect master insurance, leasing/maintenance contact centers, multi-location management, utility management & billing, per-unit pricing tiers (Basic/Plus/Premium)
- Rent Manager: rmAppSuite Pro (tech check-in/out), Make Ready Boards, TWA portal, rmResident app, LeaseTrack force-placement insurance, AmRent screening, Orion AI, 450+ reports, Rent Manager University/certification, RMUC conference
- TurboTenant: tenant-pays monetization, Snappt fraud detection (premium), 25+ listing sites, state-specific lease builder, Home Guide, Landlord Forms Pack (32 forms), Autopilot managed service, Team Roles
- Vendor-published numbers (not asserted in final doc): Buildium plan prices ($62/$192/$400 starting), 12,000+/2,600+/1,300+ unit customer quotes; Propertyware $100–$200 per unit/month; TurboTenant 1m+ landlords / 2m+ units / 12m+ renters / $6b+ rent / "28 leads per listing"; Rent Manager 450+ reports

## Vendor-specific Findings

- Buildium's official FAQ explicitly frames the Type: "purpose-built for residential property management—including single-family and multi-family rentals and community associations" with mixed portfolios as an extension — direct vendor testimony that residential is the center and other markets are configurations.
- Buildium's data-import guidance encodes the object dependency order: properties and units first, then "your people" (tenants + leases created together on a unit) — the stock precedes the tenancy.
- Buildium's "locking your accounting books… in compliance with trust accounting rules" and "record a bank deposit… from tenants, association owners, or rental owners" show the third-party accountability layer and the multi-payer ledger inside one system.
- AppFolio's marketing-leasing page presents the leasing funnel as an explicit managed pipeline (lead → qualification → move-in) with renewal automation closing the loop — the turnover leg as product surface.
- AppFolio's bulk move-outs ("set move-out dates, add charges and credits, and create work orders in a few steps") tie move-out, charges, and maintenance into one turnover action.
- Rent Manager's "task automation… for recurring charges, bills, and fees that require monthly posting" is direct evidence of the recurring rent cycle as scheduled machinery.
- Rent Manager's make-ready boards and Rent Manager's/AppFolio's turnover machinery show move-out→make-ready→re-lease as a managed workflow.
- TurboTenant proves the minimal floor: no owner layer, no GL, tenant-pays screening — yet the stock/tenancy/rent-cycle/turnover spine is fully present. This is the strongest single piece of evidence for what is definitional vs tier-dependent.
- TurboTenant's "receipts… even if it isn't through TurboTenant" (offline payment recording) shows the ledger, not the payment rail, is the system's money record.

## Boundary Findings

1. **vs Commercial Property Management (§17, processed)** — RATIFIED from this side on the commercial pass's recorded seam. The two share the family spine (property → tenant → lease → billing → maintenance → owner), and the same vendors sell both (Buildium, AppFolio, Rent Manager all list commercial as a market). The differentiator is the lease's economic shape: residential tenancies are consumer households under largely standardized agreements with fixed periodic rent; commercial tenancies are negotiated instruments (escalations, recoverable charges, options, sales-based rent) driving lease-structured billing plus operating-expense recovery machinery. Structural tests: add negotiated-term billing + recovery machinery as the center → Commercial PM; strip them → RPM remains. Keep-both.
2. **vs Affordable Housing Management (§17, processed) — JOINT REVIEW FLAG DISCHARGED** — RATIFIED keep-both. Shares the entire property-operations spine (units/leases/charges/collection/maintenance/accounting); the differentiator is the program layer (eligibility determination, certification/recertification, program-constrained rent, authority reporting). Structural test: remove the program layer → RPM remains. Corroborated in-market: AppFolio lists "Affordable Housing" as a separate market and Rent Manager as a separate industry — the affordable Type appears at property-type/module grain inside general PM platforms, exactly as the affordable pass recorded ("vendors ship both as one suite with affordable as a property-type configuration or module").
3. **vs Rent Collection Platform (§17, processed)** — RATIFIED from this side on that pass's removal tests ("add leasing + maintenance + full accounting as the center → RPM; strip everything but charges/payments/status → this Type"). The sampled RPM products all center the whole tenancy operation; the money-in slice is one loop inside it. TurboTenant's rent-collection feature is a module of an RPM tool, not the whole product.
4. **vs Property Maintenance Management (§17, processed)** — RATIFIED from this side on that pass's seam ("maintenance is one module here"). All five sampled products carry maintenance as a module beside tenancy/rent/leasing; none makes the work item the primary object of record.
5. **vs Rental Application Platform (§17, processed)** — RATIFIED from this side on that pass's suite-pole seam: the application is the intake step of the lead-to-lease cycle; the suite's record is the tenancy and portfolio. All five sampled products embed application machinery at module grain (Buildium applications, AppFolio rental applications, Propertyware application portal, Rent Manager online applications, TurboTenant applications) — the same Type at module grain, as that pass recorded.
6. **vs Tenant Screening Platform (§17, unprocessed)** — corroborates the rental-application pass's forward flag from the suite side: screening appears inside RPM as reports attached to applications in the leasing pipeline (Buildium "powered by TransUnion", AppFolio FolioScreen, Rent Manager AmRent, TurboTenant tenant-paid reports). The consumer-report machinery (bureaus, scores, per-report compliance) is not the RPM record. Keep-both proposed; ratify at that pass.
7. **vs Tenant / Resident Portal (§17, unprocessed)** — working seam for that pass: the portal is the resident-facing delivery surface (payments, requests, announcements, documents); RPM is the operator-side system of record the portal feeds. All five products ship a resident surface as a standard capability, not as the product's center. Forward flag.
8. **vs HOA / Community Association Management (§17, unprocessed)** — working seam: assessments levied on member-owners vs rent charged to tenant households under leases. Vendors sell both as separate portfolio types (Buildium "Community Associations" portfolio; AppFolio associations market; Rent Manager associations industry), and Buildium's deposit article names "association owners" as a distinct payer type inside one platform — adjacent served markets, not the same record. Forward flag for that pass.
9. **vs Short-term Rental Management (§17, unprocessed)** — working seam: transient nightly bookings vs periodic tenancies; different charge shape and relationship duration. Rent Manager lists "Vacation Homes" as a separate industry — the market itself separates them. Forward flag.
10. **vs Student Housing Management (§17, unprocessed)** — working seam: enrollment-cycle leasing and by-the-bed structures (AppFolio rent-by-the-bed: "separate leases and tenant ledgers by-the-bed rather than the unit as a whole") vs the general residential tenancy. Forward flag.
11. **vs Security Deposit Management (§17, unprocessed)** — working seam: deposits appear inside RPM as a chargeable item at move-in and a disposition at move-out (Buildium: "Accept security deposits via online payment"); the trust/escrow-governed deposit lifecycle as the primary record is that Type's center. Forward flag.
12. **vs Property Listing Platform (§17, processed)** — consistent with that pass's venue seam: RPM's leasing module markets vacancies and syndicates listings outward (one-touch syndication, ILS push, 25+ sites), but the RPM record is the tenancy on the managed stock, not a pooled public listing with market-state lifecycle. The syndication feed-out is documented, not an overlap of centers.
13. **vs Lease Administration (§17, processed)** — partially corroborates that pass's evidence-gap note from the residential side: the residential lease is held as the tenancy's terms (fixed periodic rent, dates, charges), not as an abstracted negotiated instrument with options/critical dates/recovery pools; no lessor-side lease-administration machinery (lease review, critical-date management, obligation tracking) was observed on the fetched residential surfaces. The gap note concerned commercial-grade lessor lease-admin inside PM suites; this pass neither confirms nor refutes it for commercial suites — it shows the residential lease does not carry that machinery.
14. **vs Real Estate Brokerage CRM / Property Showing Platform (§17)** — demand-side adjacency: lead capture and showing scheduling exist inside the leasing pipeline (TurboTenant showing scheduling; AppFolio self-guided tours), but the brokerage CRM's client/deal record and the showing platform's scheduling gate are different records. Consistent with the showing pass's recorded seam.
15. **vs Real Estate Investment Management (§17, processed)** — capital side (acquisitions, funds, investor capital) vs operating side (tenancies, rent, maintenance). AppFolio sells Investment Manager as a separate product with a separate login — the market itself splits the seam.

## Uncertainties

- Buildium's knowledgebase articles could not be fetched directly (Salesforce SPA CSS error on both attempts); evidence rests on the official Help Hub landing page's article titles and one-line summaries. Precise operational parameters (ePay hold-day counts, fee amounts, state-specific rules) were deliberately not asserted.
- Move-out/deposit-disposition machinery was directly observed only at AppFolio (bulk move-outs with charges/credits), Rent Manager (make-ready boards), and TurboTenant (condition reports); Buildium/Propertyware fetched pages did not surface their move-out flows — recorded as not-surfaced rather than absent.
- No non-US vendor was directly sampled; regional regimes (UK letting practice, Australian bonds, EU tenancy law) are covered only by the historical check and jurisdiction-aware features observed in US products (state-specific leases, trust-accounting lock dates). The core is asserted as region-neutral because nothing in it is US-specific, but regional product structure is unverified.
- Yardi (the largest PM vendor family) was not directly sampled this pass (prior passes recorded 403s); it is retained as a market anchor only. No structural claim depends on it.
- Institutional multifamily operators (large REIT-scale) were not directly sampled; scale machinery is inferred from AppFolio/Rent Manager bulk features and Buildium's stated customer range (vendor claims).

## Historical / Market-Sample Check

- Paper-era property management office: a card file of properties and units, a lease file per tenancy, a rent book (charges, payments, arrears), newspaper advertising + applications + signed leases when a unit turned over, a maintenance log, and (for third-party managers) monthly owner statements. All four L0 legs hold with no software: stock, tenancy record, rent cycle, turnover.
- Early desktop-era PM software (Buildium's own founding generation, 2004–2008 per its official FAQ) carried the same spine without portals, syndication networks, AI, or contact centers — in-type.
- The DIY floor (TurboTenant) shows the Type without owner layer, GL, or trust accounting — still unmistakably RPM. The professional ceiling (AppFolio/Rent Manager) adds scale machinery — still the same spine.
- Regional check: nothing in the L0 is US-specific (no US-form machinery in the core; state-specific leases, trust-accounting regimes, and insurance force-placement are L2). UK letting-agent practice (referencing, deposit schemes, periodic tenancies) would satisfy the same four legs.
- Conclusion: the definition is not over-fitted to the current AI/syndication-heavy US SaaS market.

## Final Synthesis

Residential Property Management is the operator-side application Type for running rental residential housing as a continuous business. Its defining core is a four-part jointly-held structure: the managed rental stock (properties → units with occupancy state), the residential tenancy of record (a household bound to a unit under a lease with fixed periodic rent, living from move-in to move-out/renewal), the tenancy's rent cycle (recurring charges → collection → arrears), and turnover of the stock (tenancies end, units are re-let through a leasing pipeline). Around that core, mature products add the standard operating layer: leasing machinery (syndication, applications, screening, e-signature), maintenance work orders, resident portals, communication, owner accountability and property accounting (third-party tier), reporting, and vendor management. The Type varies by operator type (self-managing landlord → third-party PM company → institutional operator), portfolio composition, and regional regime; its sharpest boundaries are with Commercial PM (lease economics), Affordable Housing Management (program layer), and the point-tool Types (rent collection, maintenance, applications, portals) that each hold one slice of the spine.
