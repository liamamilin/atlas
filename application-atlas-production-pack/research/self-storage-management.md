# Research Notes — Self-storage Management

Research date: 2026-09-09
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what self-storage management software actually is as an Application Type: what objects exist inside it, what facility staff and operators do with them, how the rental work flows, what states and rules matter, and where its boundary lies against neighboring Types (residential/commercial property management, marina management, campground/RV park management, moving-company storage modules, package & mailroom management, warehouse management).

## Initial Boundary

Initial hypothesis before research:

- Core use: operating self-storage (mini-storage) facilities — renting small individual units to tenants who store their own goods.
- Primary users: facility managers (front desk), district/regional managers, corporate operators, owners/REITs.
- Likely nearest neighbors: Residential/Commercial Property Management (leases, rent, tenants), Marina Management (space inventory + berthing agreements), Campground/RV Park Management (space inventory + stays), Moving Company Management (movers' storage-in-transit modules), Package & Mailroom Management (custody of third-party goods).
- Key unknowns: unit taxonomy (sizes/types/climate/parking), the delinquency→lien→auction machinery, gate/access-control integration depth, multi-site structure, regional spread outside the US.

## Research Questions

1. What is a "unit"? How is the unit inventory structured (identification, size, type, amenities, floors, parking)?
2. What is the rental lifecycle: inquiry/reservation → move-in → occupied → transfer → move-out → vacant?
3. How does the money loop work: recurring rent, autopay, fees, deposits, proration, move-out settlement?
4. What is the delinquency machinery: late fees, notices, gate lockout/overlock, lien process, auction?
5. How does gate/access-control integration work, and is it definitional or peripheral?
6. What roles exist (manager, assistant manager, district/corporate, owner) and how do permissions work?
7. What interfaces does the manager actually work from (site map, tenant profile, dashboards)?
8. Where is the boundary vs property management, marina, campground/RV, moving storage, mailroom, WMS?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophy + different customer tier:

| Product | Vendor | Tier / philosophy |
|---|---|---|
| SiteLink Web Edition | SiteLink (Storable) | Market leader; single-store through top-100 operators; deep operations + huge integration marketplace |
| Yardi Breeze Premier (Self Storage) | Yardi | Property-management-suite vendor pole; self-storage as one property type in a multi-type PM platform |
| Hummingbird | Tenant Inc. | Modern cloud challenger; AI/automation-first; operator-built; portfolio-scale |
| Self Storage Manager (SSM) | E-SoftSys | Enterprise/REIT pole; multi-facility standardization; 25-year vendor |
| SC Navigator | Storage Commander | Mid-market; 25+ years; automation + lien compliance emphasis |

Rejected/adjusted: Easy Storage Solutions (small-operator pole) — site unreachable after two transport errors; replaced by Storage Commander as the mid/small-operator-adjacent pole.

## Sources

All fetched 2026-09-09 (Tier 1/2 official vendor surfaces):

- SiteLink — https://www.sitelink.com/ ; https://www.sitelink.com/products/self-storage-software ; https://www.sitelink.com/products/self-storage-software/web-edition ; https://www.sitelink.com/marketplace/auction-lien ; https://www.sitelink.com/marketplace/gate-access
- Yardi Breeze — https://www.yardibreeze.com/ ; https://www.yardibreeze.com/self-storage-features/
- Tenant Inc. — https://tenantinc.com/ ; https://www.tenantinc.com/products/hummingbird
- Self Storage Manager — https://www.selfstoragemanager.com/ ; https://www.selfstoragemanager.com/contents/managementsoftware.aspx
- Storage Commander — https://www.storagecommander.com/ ; https://www.storagecommander.com/SC-navigator

Source-access limitation: no vendor's deep help-center/knowledge-base articles (per-feature operational docs) were reachable in this pass; evidence is from official product/marketing/FAQ surfaces. Consequently, precise operational details (exact fee timing, exact notice counts, exact grace periods, specific gate-system command sets) are NOT asserted anywhere. Assertions are calibrated to what these surfaces directly support.

## Product Observations

### SiteLink Web Edition (SiteLink / Storable)

Evidence layer: A (directly observed on official pages).

- Positioning: "turnkey software solution to operate your self-storage business"; single-store and multi-store operators; "more than 14,000 stores"; "most of the top 100 operators"; founded 1996; Windows + cloud ("SiteLink Web Edition offers speed and data access when Internet service is unavailable" — evidence for the pre-cloud installed-client generation being in-type).
- **Interactive Property Map**: "The birds-eye-view of your store is a great visual tool for daily operations including move-in, payments, transfers and searches."
- myHub (browser/tablet companion) actions: "take payments, move tenants in/out, transfer units, electronically sign and manage leases and documents, perform interactive walk-thru audits of your property, run real-time reports."
- Tenant lifecycle: "SiteLink collects all notes for the lifetime of the tenant, keeps data even after tenants move out and even lets you apply payments after move-out."
- eSign: "capture electronic signatures on leases, letters and forms... including leases, payment authorizations and insurance addendums."
- Money: SiteLink Merchant Services (card + ACH); "Web Pay & Reserve — from your website, offer online payments and reservations"; Price Optimizer ("create business rules for changing rates so current and new tenants always pay the right amount").
- Delinquency/collections: "automate tenant notifications and collections"; Tenant Notifications (messaging, emails, letters, mail outsourcing); Marketplace category "Auction & Lien" with online auction platforms (Lockerfox, SelfStorageAuction.com, StorageAuctions.com/.net, StorageTreasures, Bid13) — "eliminate manual entry and tedious tracking of past due tenants... automating and better tracking your past due process."
- Access control: Marketplace "Gates & Access" (Storable Access Control, SpiderDoor, INSOMNIAC CIA, PTI, BearBox, Sentinel, Stor-Guard); "SiteLink integrates with many gate and access systems."
- Roles: "different access levels for managers, assistant managers and other staff. You can disable menus and access to reports"; example: disable move-in menu, force all rentals through Inquiries and Reservations.
- Multi-site: "Corporate Control Center delivers... reporting and back-end functionality... Standardize settings for one or multiple stores including user levels, forms, discount plans and revenue management."
- Lead-to-lease: TOTAL CRM, LeadAlert, TeleTracker call tracking; FAQ: "Owners know they need more than just moving tenants in and out and taking payments. Successful storage operations manage rate changes, collect internet leads and convert them to rentals, automate tenant notifications and collections and rely on accurate reporting and accounting."
- Accounting: TOTAL Accounting ("industry standard for financial reporting... financial controls and auditing").
- Regional: "numerous language versions... Spanish, French, Portuguese and Chinese... adapted to regional operating system settings, measurements, currencies, taxes and laws."

### Yardi Breeze Premier — Self Storage (Yardi)

Evidence layer: A.

- Positioning: property-management suite covering residential, commercial, affordable housing, self storage, associations, manufactured housing — self-storage is one property type in a PM platform (suite-vendor pole).
- Property Management: "Track unit types and amenities and manage discounts"; "Manage auctions"; "Track RVs and boats"; "Control security for all users at the menu level"; "See your daily, weekly and monthly task and activity calendar."
- Marketing & Leasing: "Showcase available units on popular listing sites, including StorageCafe.com"; "Complete reservations, screening and leases online"; "Rent multiple units to one tenant"; "Track and sell retail items"; "Automate move-in and move-out workflows to reduce risk"; "Offer an integrated stored goods protection plan."
- Rent Collection: "Set up advanced rent, discount and pricing management"; "Let tenants view balances and pay rent online"; "Get paid faster when tenants set up autopay"; "Collect rent via debit, credit card and ACH"; "Automate recurring rent and fee postings"; "Track delinquencies and fee schedules."
- Accounting: full GL, payables, owner tools (third-party-management pole: "Manage properties by owner and fraction ownership... Calculate owner payments").
- Feature list also names: "Security gate integration", "Vacancy & prospect tracking", "Auction manager", "Role-based security tools", "Enhanced rent, discount & pricing tools", "RV & boat tracking", "Stored goods protection plan".

### Hummingbird (Tenant Inc.)

Evidence layer: A.

- Positioning: "The property management system built for self-storage operators"; "AI-enabled PMS built by self-storage operators, for self-storage operators"; SOC-II; platform = Hummingbird (PMS) + Mariposa (online rentals/e-commerce) + Nectar (API).
- **Interactive Facility Map and Task Center**: "Real-time unit status, quick actions, configurable tasks, and space notes with maintenance history across every facility."
- SuperLease: "Every lease is digital, version-controlled, and compliant from the moment it is signed."
- Automation Engine: "Delinquency timelines, late notices, payment reminders, and move-in/move-out workflows run on your schedule without manual triggering."
- Rate Management Center: "Occupancy-based rent increases, promotion triggers, and rate controls apply across your portfolio from one dashboard."
- Tenant Communications: "Automated notices, two-way SMS, and expiring payment URLs."
- Portfolio Level Management: "One login covers every facility... dynamic grouping by region, management team, or ownership structure. Rate increases, tasks, and reporting apply across locations simultaneously or selectively."
- Compliance: "State-specific compliance built into every workflow — delinquency processes, notices, and documents are vetted by the Self Storage Legal Network... Operators never... discover a documentation gap during a lien proceeding."
- Tenant profile quote: "We can go to a tenant profile and see everything about that tenant: their delinquency, their status, and lock them out."
- Remote-managed pole: "We are a professionally remote managed operation. Every one of my facilities uses software and technology to replace what a manager would do on-site."

### Self Storage Manager (E-SoftSys)

Evidence layer: A.

- Positioning: "enterprise class cloud-based property management software... built for multi-facility self storage operators, large storage operators, and REITs"; incorporated 2000; 1000+ facilities; UK version; multi-currency/multi-language (French, German, Spanish, Dutch).
- Feature list (directly observed):
  - "Provide real time unit inventory for prospective customers 24x7 through the facility website for Online Reservations and Online Rentals, enable pre-reservations and waiting list"
  - "Customer Portal for tenants to manage their accounts and pay online"
  - "Maintain flexible pricing for units with ability to offer various discounts including online specials"
  - "Advanced revenue management to fluctuate pricing based on occupancy or competition pricing, enable automatic rent increases based on customer longevity, current occupancy, previous rental increases"
  - "User-definable fees and charges, including any recurring charges"
  - "Quote multiple unit sizes for inquiries or reservations with options to set up automated follow-ups"
  - "Equipment rental and merchandise sales with inventory management and ability to sell merchandise packs"
  - **"Perform Move-in, Move-out, Transfer, Payment functions using the color-coded dynamic site map"**
  - "Generate Rental agreement, Custom invoices, Late Notices and Auction Letters"
  - "Generate separate contracts for rental goods, vehicle/trailer rentals"
  - **"Lock delinquent tenants at the gates and charge late or lien fees automatically during end of day"**
  - "Interfaces with access control/gate systems such as DigiGate, Sentinel, PTI, QuikStor, WHAM, Door King, GateEase, Demco, Axcys, SC Solutions, Bearbox, StorGuard"
  - Accounting interfaces (Sage, Peachtree, Great Plains, Yardi, QuickBooks); e-CRM; call-center interfaces.

### SC Navigator (Storage Commander)

Evidence layer: A.

- Positioning: mid-market, 25+ years; "tenant management, unit tracking, online rentals, payment processing, marketing services, and insurance."
- Key features (directly observed): "Automated Payments & Billing — Eliminate late payments and streamline invoicing with automated rent collection"; "Multi-Site Management"; "Smart Unit & Tenant Management — automated move-ins, move-outs, and reservation tracking"; **"Compliance & Lien Management — built-in lien enforcement tools. Reduce risk... with automated notices and compliance tracking."**
- Migration: "We import your data into SC Navigator software using your unit list and rent roll data from your current property management software."
- FAQ defines the category: "Self-storage software automates key parts of facility management, including move-ins, move-outs, rent payments, and billing. It also supports online rentals, integrates with gate access systems, and provides real-time reporting."

## Cross-product Comparison

| Structure | SiteLink | Yardi Breeze | Hummingbird | SSM | SC Navigator | Layer |
|---|---|---|---|---|---|---|
| Unit inventory w/ types & amenities | ✔ (property map, availability API) | ✔ ("track unit types and amenities") | ✔ (real-time unit status) | ✔ ("real time unit inventory") | ✔ ("unit tracking") | Core (5/5) |
| Rental agreement / lease per tenant×unit | ✔ (eSign leases) | ✔ (online leases) | ✔ (SuperLease digital leases) | ✔ ("Generate Rental agreement") | ✔ (tenant management) | Core (5/5) |
| Move-in / move-out / transfer | ✔ (map: "move-in, payments, transfers") | ✔ ("automate move-in and move-out workflows") | ✔ (move-in/move-out workflows) | ✔ ("Move-in, Move-out, Transfer... site map") | ✔ ("automated move-ins, move-outs") | Core (5/5) |
| Occupancy/vacancy state | ✔ | ✔ ("vacancy & prospect tracking") | ✔ (real-time unit status) | ✔ (real-time inventory) | ✔ ("keep bays filled") | Core (5/5) |
| Recurring rent + payments | ✔ (merchant services, web pay) | ✔ ("automate recurring rent and fee postings", autopay) | ✔ (payment reminders, expiring URLs) | ✔ ("recurring charges", end-of-day fees) | ✔ ("automated rent collection") | Core (5/5) |
| Delinquency machinery (late fees/notices/lockout) | ✔ (notifications, collections) | ✔ ("track delinquencies and fee schedules") | ✔ (delinquency timelines, "lock them out") | ✔ ("lock delinquent tenants at the gates") | ✔ (lien enforcement tools) | Common (5/5) |
| Lien/auction path | ✔ (Auction & Lien marketplace) | ✔ ("manage auctions", "auction manager") | ✔ (lien-proceeding compliance) | ✔ ("Auction Letters") | ✔ (lien management) | Common (5/5) |
| Gate/access-control integration | ✔ (Gates & Access marketplace) | ✔ ("security gate integration") | (integrations page exists; not itemized in fetched pages) | ✔ (12+ named gate systems) | (implied by category FAQ) | Common (4/5 direct) |
| Reservations/waitlists/online rentals | ✔ (Web Pay & Reserve) | ✔ (reservations, online leasing) | ✔ (Mariposa SuperLease) | ✔ (pre-reservations, waiting list) | ✔ (online rentals) | Common (5/5) |
| CRM / lead-to-lease | ✔ (TOTAL CRM, LeadAlert, TeleTracker) | ✔ (CRM queue) | ✔ (call management add-on) | ✔ (e-CRM, drip campaigns) | (marketing services) | Common (4/5 direct) |
| Revenue/rate management | ✔ (Price Optimizer) | ✔ ("advanced rent, discount and pricing management") | ✔ (Rate Management Center) | ✔ (advanced revenue management) | (dynamic pricing per FAQ) | Common (4/5 direct) |
| Tenant portal / online payments | ✔ | ✔ | ✔ (two-way SMS, URLs) | ✔ (Customer Portal) | ✔ | Common (5/5) |
| Retail merchandise / equipment rental | (marketplace ancillary) | ✔ ("track and sell retail items") | — | ✔ (merchandise packs, equipment rental) | — | Optional (2/5) |
| Insurance / protection plans | ✔ (marketplace category) | ✔ ("stored goods protection plan") | ✔ (protection enrollment metric) | — | ✔ (tenant insurance product) | Common-US (4/5) |
| Multi-site / corporate control | ✔ (Corporate Control Center) | ✔ (portfolio) | ✔ (portfolio grouping) | ✔ (corporate/district standardization) | ✔ (multi-site) | Common (5/5) |
| Accounting depth | ✔ (TOTAL Accounting) | ✔ (full GL, owner statements) | (data warehouse/BI) | ✔ (accounting interfaces) | ✔ (report finances) | Common (varies in depth) |
| Kiosk / unstaffed operation | ✔ (kiosk marketplace category) | — | ✔ (remote-managed testimonial) | — | — | Optional/variant |
| RV/boat/parking units | — | ✔ ("RV & boat tracking") | — | ✔ (vehicle/trailer rental contracts) | ✔ (boat insurance product) | Variant (3/5) |

## Canonical Model

### L0 — Defining Invariant (minimal)

Four jointly-held structures. Remove any one and the product stops being recognizable as self-storage management:

1. **The rentable unit inventory of record** — the facility's storage units held as individually identified, size/type-defined rentable spaces (the facility's inventory truth). Without it: a space registry, or a generic lease ledger with nothing to fill.
2. **The rental agreement as the unit of work** — a persistent commitment binding a tenant to a unit under a recurring-rent term, advancing through move-in → occupied → move-out. The tenant keeps custody of their own goods: the operator rents space and never holds identified contents. Without it: generic recurring billing; without the custody boundary: a moving/valet-storage shape, not self-storage. (Cycle length — month-to-month being the industry-common realization — was not directly evidenced in the fetched sources and is held as an uncertainty; the invariant is the recurring term itself.)
3. **The live occupancy state of the inventory** — unit states (vacant / occupied / reserved / delinquent…) that drive availability, the daily operating map, and what prospects can rent. Without it: a contract archive with no live operations.
4. **The recurring-rent money loop** — rent charged on the billing cycle, payments (incl. autopay), fees, account balance, and settlement at move-out. Without it: an occupancy tracker with no economics.

Jointly-held load-bearing:
- 1 alone = space registry
- 2 without 1 = lease ledger with nothing to fill
- 3 without 1+2 = occupancy board over nothing
- 4 without 2 = generic invoicing
- 1+2 without 3 = contract archive with no live operations
- 1+3 without 2 = empty map
- 1+2+3 without 4 = occupancy tracking with no rental economics
- 2+3 without 1 = agreements against unidentified space

### L1 — Common Mature Structure (very common, not definitional)

- Delinquency escalation machinery: late fees → notices (email/SMS/letter) → gate lockout/overlock → state-specific lien process → auction (increasingly via integrated online auction platforms) → unit cleared. 5/5 sampled; the industry's signature legal machinery (US state lien laws; compliance-vetted notice documents).
- Gate/access-control integration: per-tenant access codes, gate hours, lockout on delinquency; integration with dedicated access-control vendors. 4/5 direct.
- Reservations, waitlists, online rentals, tenant portal/self-service payments. 5/5.
- CRM / lead-to-lease: inquiries, quotes of multiple unit sizes, follow-up tasks, call tracking. 4/5 direct.
- Revenue/rate management: occupancy-based rent increases, promotions/discounts, existing-tenant rate management. 4/5 direct.
- E-signature leases and digital document storage. 3/5 direct.
- Multi-site/portfolio management with corporate standardization and role-based (menu-level) security. 5/5.
- Reporting/accounting: operational + financial reports; accounting built-in or interfaced. 5/5.
- Tenant communications: automated notices, reminders, two-way SMS. 5/5.
- Facility site map as the daily operating surface (color-coded unit states; move-in/payment/transfer actions from the map). 3/5 explicit ("interactive property map", "dynamic site map", "interactive facility map") — treated as the dominant realization of leg 3.
- Walk-thru/unit audits. 2/5 explicit.
- Insurance/protection plans (US market). 4/5.
- Retail merchandise (locks/boxes) and equipment rental. 2/5.

### L2 — Variant / Optional Structure

- Unit-type mix: climate-controlled, drive-up, interior, upper-floor/elevator, parking spaces for RVs/boats/vehicles (3/5 sampled name RV/boat/vehicle handling).
- Staffing model: fully staffed front desk ↔ remote-managed/unstaffed (kiosk, smart entry) — a real market pole (remote-managed portfolio testimonial; kiosk marketplace category).
- Regional/legal regime: US state lien-law machinery vs UK/EU regimes (SSM UK version, multi-currency/language; BearBox as a European gate vendor). Language/currency adaptation.
- Business model of the operator: own single store ↔ third-party management (owner statements, owner payments — Yardi owner tools) ↔ REIT portfolio.
- Ancillary lines: truck/trailer rental, merchandise, insurance, vehicle parking.
- Deployment: cloud browser vs installed Windows client (SiteLink supports both; the installed-client generation is in-type).
- Online-demand stack: listing services, facility websites, call centers, AI chat/voice (era-current).

### L3 — Vendor-specific (research notes only)

- SiteLink: myHub, Corporate Control Center, TeleTracker, LeadAlert™, Price Optimizer, TOTAL CRM/TOTAL Accounting, eSign™, Marketplace.
- Tenant Inc.: Hummingbird/Mariposa/Nectar naming; SuperLease™; Alita AI chat/voice; Charm call management; Mobile Manager; Tenant Data Warehouse; Storelocal membership programs.
- Yardi: Breeze/Breeze Premier packaging; RentCafe.com storage leads; StorageCafe.com listing; stored goods protection plan; investment management add-on.
- SSM: SAMARA, Call Tracker, Site Walkthrough app, IVR payment module, Power BI module.
- Storage Commander: SC Navigator, SC Pay, SC Risk Assurance (tenant insurance), SC Marketing.

## Vendor-specific Findings

See L3. None of these entered the canonical core. The Storable family (SiteLink + storEDGE + SpareFoot) spans management software, payments, marketplace listings, access control and auctions — an ecosystem pattern, not a Type structure.

## Boundary Findings

1. **vs Residential/Commercial Property Management** — PM manages dwellings/commercial space for habitation or business use under leases with maintenance, screening, and often longer terms; self-storage manages storage units whose contents belong to the tenant and are never handled by the operator, under short recurring terms with a delinquency/lien machinery unique to the industry. The suite-vendor pole is itself evidence: Yardi ships self-storage as a distinct property type beside residential/commercial. Remove the storage-unit character (tenant-owned goods, no contents handling, recurring-rent cycle, lien/auction) → property management territory.
2. **vs Marina Management** — dry-stack racks resemble storage units and vendors straddle both industries (recorded in the marina pass: "Storable spans both"); the marina core is wet berthing + vessel + marine services. A dry-stack-only operation is a marina variant, not self-storage. Remove the vessel/marine context → self-storage shape.
3. **vs Campground/RV Park Management** — campgrounds sell transient overnight stays with hospitality semantics; self-storage RV/boat parking is long-term parking of a stored asset under a recurring rental. Remove the stay/hospitality character → self-storage.
4. **vs Moving Company Management** — the mover's storage module holds the mover's customer's goods in the operator's custody (storage-in-transit, vaulted goods) as part of a move; self-storage rents space to a tenant who keeps custody. The moving pass recorded this seam from the other side. Remove tenant custody → moving/valet storage shape.
5. **vs Package & Mailroom Management** — the mailroom pass explicitly used "anonymous package storage = self-storage territory" as its remove-condition: mailroom holds third-party in-transit items briefly for a named recipient; self-storage holds tenant-owned goods long-term under lease with no per-item records. Remove the transit/recipient character → self-storage.
6. **vs Warehouse Management System** — WMS tracks the operator's own inventory through receiving/put-away/picking/fulfillment; self-storage rents empty space and never touches the goods. Remove tenant ownership of goods → WMS territory.
7. **vs Rent Collection Platform / Tenant Portal** — single-function slices of the money loop / tenant self-service; self-storage management is the facility's whole system of record.

## Historical / Market-Sample Check

- Paper-era self-storage office: wall unit-availability board, rental ledger/agreement cards, late notices, lien letters, auction postings, physical locks and gate keys — satisfies all four L0 legs at analog level with no software machinery. The definition therefore names no cloud, no online rentals, no revenue management, no gate integration.
- Pre-cloud software generation: SiteLink (founded 1996) documents its installed Windows client alongside the cloud product ("speed and data access when Internet service is unavailable") — the installed-client generation is in-type. SSM (2000) similarly predates the current cloud/AI era.
- Regional: SSM ships a UK version with multi-currency/multi-language support (French, German, Spanish, Dutch); SiteLink documents Spanish/French/Portuguese/Chinese versions adapted to regional "measurements, currencies, taxes and laws"; a European gate vendor (BearBox) is integrated. The core holds outside the US; the lien/auction machinery is the US-market-dominant realization of the delinquency leg and is held at L1, not L0.
- Staffing poles: staffed front desk and remote-managed/unstaffed operations both satisfy the core (remote-managed testimonial; kiosk category).

## Uncertainties

- Exact operational parameters (late-fee timing, notice counts/day-gaps in the lien sequence, grace periods, gate-hour defaults) were not reachable from official help-center docs in this pass; none are asserted anywhere.
- The dominant billing-cycle length (month-to-month) is industry-common knowledge but was not directly stated in the fetched sources; the defining invariant is held at "recurring-rent term" and the cycle length is left unstated in the final document.
- Gate/access-control integration is directly documented at 4/5 sampled products (Hummingbird's fetched pages do not itemize it; an integrations page exists but was not fetched). Held at L1 with 4/5 evidence.
- Whether any product operates without any delinquency machinery is unverified; the delinquency leg is held at L1 (common mature) rather than L0 out of caution, though 5/5 sampled products carry it.
- Kiosk/unstaffed operation depth is evidenced by marketplace category + testimonial only; held at L2.
- storEDGE (Storable's other PMS) was not separately sampled to avoid double-counting one vendor family; the Storable ecosystem pattern is noted as L3 context.

## Final Synthesis

Self-storage Management is the self-storage facility operator's system of record. Its defining core is four jointly-held structures: the rentable unit inventory of record (individually identified, size/type-defined units — the facility's inventory truth), the rental agreement as the unit of work (tenant × unit × recurring-rent term, advancing move-in → occupied → move-out, with the tenant keeping custody of their own goods — the operator rents space, never holds contents), the live occupancy state of the inventory (vacant/occupied/reserved/delinquent — driving availability and the daily operating map), and the recurring-rent money loop (cycle rent → payments/fees → balance → move-out settlement). Everything else — delinquency escalation through late fees/notices/lockout/lien/auction, gate-access integration, online rentals and tenant portals, CRM/lead-to-lease, revenue management, retail, insurance, multi-site corporate control, kiosks — is standard or optional machinery that mature products add. The Type is the storage sibling of marina and campground/RV management (space-inventory rental Types), distinguished from property management by the anonymous-contents storage unit and the recurring-rent lien-backed cycle, from moving/valet storage by tenant custody, and from WMS by the fact that the operator never touches the goods.
