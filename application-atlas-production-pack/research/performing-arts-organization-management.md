# Research Notes — Performing Arts Organization Management

## Research Goal

Understand what software sold to performing arts organizations (theatres, orchestras, dance companies, opera companies, performing arts centers) actually is, from real products: what the core objects are, who uses it, how audience/business work flows through it, and where it separates from adjacent Types (Event Ticketing Platform, Nonprofit CRM / Donor Management, Venue Management System, Theater Production Management, Event Management Platform).

## Initial Boundary

Hypothesis: this is the **organization/audience/business side** of a performing arts organization — ticketing, subscriptions, fundraising, membership, marketing — as opposed to the production side (making shows), which is Theater Production Management. The likely center is a **unified patron database** where ticket sales, donations, memberships and marketing all attach to the same person record.

Nearest neighbors: Event Ticketing Platform, Ticket Inventory Management, Nonprofit CRM, Donor Management System, Fundraising Management Platform, Membership Management System, Venue Management System, Theater Production Management, Event Management Platform, Marketing platforms.

## Research Questions

1. What is the central object — the ticket, the event, or the patron?
2. How do ticketing, fundraising, membership and marketing relate to each other in one system?
3. What does the box office / online selling flow look like?
4. How do subscriptions / season packages work (a performing-arts signature)?
5. Who are the users inside the organization (box office, development, marketing, leadership)?
6. Where is the boundary with pure ticketing platforms and with nonprofit CRMs?

## Representative Products

- **Tessitura** — enterprise unified platform for arts & culture; the sector's reference product (large orchestras, opera, performing arts centers, museums)
- **Spektrix** — cloud platform for theatres and arts organizations, UK-origin, strong public support documentation
- **PatronManager** — Salesforce-based ticketing + fundraising + marketing CRM for small/mid arts organizations (500+ orgs)
- **AudienceView** — ticketing-first platform expanded into connected fundraising/marketing/payments; multi-edition (Professional / Unlimited / Campus)

Selection covers: enterprise unified-platform philosophy (Tessitura), cloud mid-market (Spektrix), CRM-platform-built (PatronManager), ticketing-first expansion (AudienceView); different customer scales and geographies.

## Sources

- Tessitura — https://www.tessituranetwork.com/ (root/features/markets pages; feature list: Unified CRM, Ticketing & Admissions, Fundraising, Memberships, Digital & E-commerce, Education, Marketing, Reporting & Insights, Payment Processing, Retail, Ticket Scanning & Access Control) — fetched 2026-09-10
- Spektrix Support Centre — https://support.spektrix.com/hc/en-us (Tier-1: categories for Events/Offers/Subscriptions/Merchandise setup; Sell items and fulfill Orders; hardware; payments; Reporting; Customer Record/Customer Lists/Tags; Email Campaigns; Donations/Gift Aid/Membership schemes/Opportunities Interface; Agents; website integration) — fetched 2026-09-10
- PatronManager — https://patronmanager.com/ ("ticketing, fundraising, and marketing together in one connected platform. All your data is housed in a single system"; built on Salesforce; segments: orchestras, dance, theatres, arts councils, museums) — fetched 2026-09-10
- AudienceView — https://www.audienceview.com/ (Create & Manage: Tickets/Packages/Products, Series & Events, Donations & Memberships, Analyze Data; Sell & Fundraise: Box Office Ticketing, Online Sales; Engage & Grow: Know/Engage/Find Customers; editions) — fetched 2026-09-10

Source-access limitation: Spektrix marketing site returned 403; its public support centre was reachable and used instead (higher evidence tier). Tessitura and AudienceView evidence is Tier-2 (official product pages); no Tier-1 operational manuals were fetched for them, so workflow details below are calibrated accordingly.

## Product Observations

### Tessitura (evidence layer A for feature existence, B for workflow)

- Positions as "ONE PLATFORM built to run your whole arts & culture organization"
- Feature set: Unified CRM, Ticketing & Admissions, Fundraising, Memberships, Digital & E-commerce, Education Programs, Marketing, Reporting & Insights, Payment Processing, Retail, Ticket Scanning & Access Control, Cloud Hosting
- Markets: dance, ensembles & presenting organizations, festivals, museums, opera, orchestras, performing arts centers, theatre, zoos/aquariums/gardens, educational institutions — i.e., the arts-and-culture sector broadly, not only performing arts
- Has an e-commerce web product (TNEW) for online purchase paths; success stories describe membership conversion through the purchase path
- Versioned releases (v15/v16), community conference (TLCC), retainer consulting — enterprise-suite posture

### Spektrix (evidence layer A, Tier-1 support centre)

Support-centre category structure reveals the system's object model:

- **Set up**: Events, Seating Plans, Tickets, Pricing, Offers, Commissions, VAT & Tax, Ticket Subscriptions, Fixed Series, Merchandise
- **Sell & fulfill**: Sales, Returns and Exchanges, Gift Vouchers, printing Tickets, managing Orders
- **Hardware**: Ticket Printers, Scanners, PIN Pads, Box Office App
- **Payments**: methods of payment, payment service providers, Account Credit & Gift Vouchers, reconciliation
- **Reporting**: configuring/building/running Reports, Accounting Date
- **Understand customers**: the Customer Record, Customer Lists, Tags, Reports
- **Communicate**: Email Campaigns and Mailings, Contact Preferences, mailing analysis, System Emails
- **Customer loyalty and fundraising**: Donations, Gift Aid, Membership schemes, cultivating donor relationships, the Opportunities Interface
- **Agents**: enabling third parties to sell on the organization's behalf
- **Website integration**: the relationship between Spektrix and the organization's own website

This is the clearest structural evidence: events → tickets/orders → customer record → lists/tags → campaigns; donations/memberships on the same customer record.

### PatronManager (evidence layer A)

- "Brings ticketing, fundraising, and marketing together in one connected platform. All your data is housed in a single system"
- Built on Salesforce — the CRM is the substrate; ticketing is a native module on it
- Serves symphony orchestras ("manage subscriptions, donor relationships and concert activity in one connected system, with patron data at the center of every interaction"), dance, theatres, arts councils, museums
- Community meeting with sessions "across ticketing, fundraising, and marketing"

### AudienceView (evidence layer A)

- Organized as Create & Manage (Tickets/Packages/Products, Series & Events, Donations & Memberships, Analyze Your Data), Sell & Fundraise (Box Office Ticketing, Online Ticket Sales & Donations, Payments, Mobile Ticketing), Engage & Grow (Know Your Customers, Engage Customers, Find New Customers, Promotions, Digital Marketing)
- Explicit thesis: "More than a ticketing software… connected data… across ticketing, fundraising, marketing, and payments"; "Every ticket and donation is a growth opportunity but only if your platform treats them as connected"
- Editions by scale: Professional (venues/arts orgs), Unlimited (enterprise), Campus (higher ed combining athletics + performing arts)
- Industries include performing arts but also live music, museums, higher ed, not-for-profit

## Cross-product Comparison

| Structure | Tessitura | Spektrix | PatronManager | AudienceView |
|---|---|---|---|---|
| Unified patron/customer database | Yes ("Unified CRM") | Yes (Customer Record, Lists, Tags) | Yes (single system, Salesforce) | Yes ("Know Your Customers", first-party data) |
| Ticketing for own events (box office + online) | Yes | Yes (Sales, Orders, box office app, printers) | Yes | Yes |
| Seating plans / reserved seating | Yes (admissions) | Yes (Seating Plans) | Yes (implied) | Yes (seat maps) |
| Subscriptions / packages / series | Yes (Memberships + subscriptions) | Yes (Ticket Subscriptions, Fixed Series) | Yes (orchestra subscriptions) | Yes (Packages, Series) |
| Donations / fundraising | Yes | Yes (Donations, Gift Aid, Opportunities) | Yes (fundraising core) | Yes (Donations & Memberships) |
| Membership schemes | Yes | Yes | Yes (implied) | Yes |
| Marketing / email campaigns / segmentation | Yes | Yes (Email Campaigns, Contact Preferences) | Yes (marketing) | Yes (Engage & Grow) |
| Reporting / analytics | Yes | Yes | Yes (implied) | Yes (Analyze Your Data) |
| Payments | Yes | Yes | Yes (payouts) | Yes (AV Payments) |
| Ticket scanning / access control | Yes | Yes (Scanners) | — (not surfaced) | — (mobile ticketing) |
| Merchandise / retail | Yes (Retail) | Yes (Merchandise) | — (not surfaced) | Yes (Products) |
| Education programs | Yes | — (not surfaced) | — | — (Campus variant) |
| Agent/third-party selling | — (not surfaced) | Yes | — | — (not surfaced) |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The unified patron record** — one persistent record per audience member/donor/visitor in the organization's own database, to which ticketing, donation, membership and communication activity all attach. Remove → a ticketing platform with anonymous buyers, or a donor database with no ticketing.
2. **Selling admission to the organization's own events/performances** — the organization configures its events (with seats/pricing where applicable) and sells tickets to them through its own channels (box office and online), recording each sale as an order/transaction against a patron. Remove → a pure CRM/donor tool.
3. **The relationship loop over recorded transactions** — the recorded purchase/donation history feeds ongoing cultivation: fundraising asks, membership schemes, and targeted communication to segments of the patron base. Remove → a box office terminal with no audience relationship.

Binding: the customer is the **performing arts / arts-and-culture organization itself** selling its own program to its own audience — not a third-party ticketing marketplace, not a generic event organizer.

### L1 — Common Mature Structure

- reserved seating / seating plans
- subscriptions, season packages, fixed series (the sector's signature revenue model)
- membership schemes with benefits
- gift vouchers / account credit
- email campaigns with contact-preference management
- reporting with accounting dates
- payment processing and reconciliation
- ticket printing/scanning hardware and access control
- merchandise/retail

### L2 — Variant / Optional

- education program management (Tessitura)
- agent/third-party selling (Spektrix)
- retail POS breadth
- multi-department campus models (AudienceView Campus)
- admissions-based (museums) vs performance-based (theatre/orchestra) selling
- deployment: Salesforce-native (PatronManager) vs proprietary platform
- e-commerce website product vs website-integration APIs

### L3 — Vendor-specific

- TNEW (Tessitura's e-commerce web product), TLCC community conference, Spektrix "Opportunities Interface" naming, Dotdigital program integration, Gift Aid (UK-specific), AudienceView edition names. These stay here.

## Vendor-specific Findings

- Gift Aid (Spektrix) is UK tax-relief specific — not definitional.
- Tessitura's Education module and Retail module are suite breadth, not Type structure.
- PatronManager's Salesforce substrate is an implementation choice, not a structure.

## Boundary Findings

- **vs Event Ticketing Platform / Ticketmaster-class**: those sell tickets to many organizers' events as a marketplace/box-office service; here the system is the organization's own system of record for its own audience relationship, and the patron record — not the ticket — is the center. Remove the unified patron relationship loop → ticketing platform.
- **vs Nonprofit CRM / Donor Management System**: donations primary, no admission selling. Remove ticketing → donor management; remove fundraising → box office ticketing.
- **vs Theater Production Management** (sibling leaf, processed 2026-09-09): that system's unit of record is the production (making and running shows: company, calls, reports); this system's unit of record is the patron relationship (selling and cultivating the audience). The theater-production pass explicitly excluded ticketing/donor machinery as belonging here. Boundary confirmed from both sides.
- **vs Venue Management System**: venue/space operations (booking the building, tenants) vs organization/audience business. A presenting organization without its own venue is still in-type.
- **vs Event Management Platform**: conferences/attendee lifecycle vs recurring performance seasons and donor cultivation.
- **"去掉什么就变成另一个 Type" 判据**: remove the patron unification → ticketing platform; remove ticketing → nonprofit CRM; remove the relationship loop → box office terminal.

## Historical / Market-Sample Check

Pre-digital performing arts organizations ran on a box office ledger + season-subscription books + paper donor lists + printed season brochures — the same three structures (patron records, selling own performances, cultivation loop) held without software, seating software, email campaigns, or scanning hardware. Subscriptions, though iconic, are common-mature rather than definitional (an organization selling single tickets and donations only remains in-type). The definition passes the historical check.

## Uncertainties

- Exact workflow details inside Tessitura and AudienceView (order lifecycle, subscription renewal mechanics) were not verified from Tier-1 documentation; kept at capability level.
- PatronManager's membership and scanning capabilities were not surfaced on the fetched page; not asserted.
- Whether education programs deserve their own Type was not researched; recorded as a possible taxonomy question but not pursued.

## Final Synthesis

Performing Arts Organization Management software is the arts organization's audience-and-revenue system of record: a unified patron database at the center, ticketing for the organization's own performances as the primary transaction, and a cultivation loop (fundraising, membership, marketing) that turns recorded transactions into ongoing audience relationships. Its identity comes from holding all three together in one system for the organization's own audience — which is exactly what distinguishes it from ticketing platforms (no patron relationship), donor CRMs (no ticketing), and production-side theater software (no audience).
