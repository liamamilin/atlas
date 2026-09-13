# Research Notes — Travel Agency Management System

Directory position: Section 26 Travel, Hospitality, Food Service & Events (siblings: Online Travel Agency / OTA, Travel Package Booking Platform, Tour Operator Management System, Destination Management Company Platform, Travel Supplier Management, Hotel PMS/CRS, Travel Itinerary Planner).

Inherited flags to discharge:

- **tour-operator-management-system** (processed 2026-09-09) recorded a secondary flag vs this leaf: principal-with-margin vs commission-intermediary money models — quoting features overlap but fulfillment responsibility and the two-sided money record differ. This pass must corroborate or refute.
- **destination-management-company-platform** (processed 2026-09-07) recorded the same secondary flag vs this leaf (principal-with-margin vs commission-intermediary). Same discharge.

---

## Research Goal

Understand what a Travel Agency Management System actually is as an Application Type: the software a travel agency runs its business on — client relationships, booking files assembled from third-party travel supply, quotations and itineraries, client invoicing and payment collection, commissions and supplier settlement, agency accounting, and branch/network management. Determine the defining core, the standard mature capability ring, segment variants (leisure retail vs business travel/TMC vs host/broker networks), and the boundaries against neighboring Types (OTA, tour operator system, DMC platform, corporate travel management, generic CRM, itinerary planner).

## Initial Boundary

Initial hypothesis (to be verified, not asserted):

- Core job: the agency (an intermediary) sells travel supplied by other businesses to its own clients, earns commissions and/or service fees, and is responsible for the client relationship and the file — not for operating the travel.
- Likely core objects: client/traveller profile, booking/trip file, supplier service segments, quotation/proposal, invoice/receipt, commission, supplier payable, service fee, task/queue.
- Most confusable neighbors: OTA (same intermediary economy, different operator of the software), tour operator system (principal vs intermediary), DMC platform (principal vs intermediary), corporate travel management platform (client-side program vs agency business), generic CRM, itinerary planner.

## Research Questions

1. What objects exist inside such a system (clients, corporate accounts, travellers, bookings/orders/trips, service segments, suppliers, documents, fees, commissions, payments)?
2. Where do bookings come from — GDS/booking-tool capture, API/marketplace, manual entry? Is supplier-system integration definitional?
3. What is the unit of work — the per-client booking file/order? How do multi-service trips aggregate?
4. What does the money record look like on each side: client invoicing/payments/fees; supplier commissions/payables/settlement (BSP/ARC-style)?
5. What roles use the system (travel consultant, corporate counselor, branch manager, back-office finance, network/head office)?
6. What operations wrap the booking lifecycle (tasks, quality checks, schedule changes, unused tickets, cancellations/refunds)?
7. What document/communication outputs exist (quotes, invoices, itineraries, vouchers, portals)?
8. How do branch/host-agency/broker network structures appear (silos, commission splits, sub-agency settlement)?
9. Where is the line vs OTA, tour operator system, DMC platform, corporate travel management platform, CRM, accounting software, itinerary planner?
10. Historical check: would a paper-era retail travel agency's records satisfy the same structure?

## Representative Products

Selection principles: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Market / tier | Philosophy | Evidence level |
|---|---|---|---|
| **TravelJoy** (traveljoy.com) | US-centric; independent travel advisors, small agencies, host-agency teams | all-in-one front office for advisors: CRM + itineraries + payments + bookings + automations | A (official home + pricing); help center unreachable (timeout ×2) |
| **Tramada** (tramada.com, owned by CTM per site cross-links) | Australia/global; leisure & retail agencies, broker networks, large TMCs | 'front' + 'mid' office automation: GDS booking download, documentation, fees/commissions with GL mapping, reconciliation, accounting | A (official home + solutions page) |
| **Midoco** (midoco.de) | Germany/EU + global; business & leisure travel agencies, OTAs, tour operators; TMC clients incl. Amex GBT, Lufthansa City Center, CTM references | mid- & back-office ERP: automated booking import → order processing → invoicing → fees → reconciliation → accounting hand-off | A (official home + solution page with full feature tables + FAQ) |
| **Cornerstone / Upstream** (ciswired.com) | US/global; TMCs, OTAs, leisure agencies, corporates; 500+ customers | travel operations + data + spend platform: workflow automation (schedule change, unused tickets, policy), data acquisition/quality, spend | A (official home + platform nav); mid-office self-description via customer testimonial |
| **TripMatrix** (tripmatrix.com) | small agencies/operators/DMCs/advisors (EU-origin) | all-in-one inquiry→payment: trips, inventory, packages, suppliers, CRM, payments, traveler portal, website — sold across agency AND operator/DMC populations | A (official home + feature pages) |

Cross-reference from processed sibling passes: online-travel-agency-ota (2026-09-08) — traveler-facing retail of third-party supply; operator-side systems out of its scope. tour-operator-management-system (2026-09-09) — principal with own products; commission-intermediary agencies explicitly outside. destination-management-company-platform (2026-09-07) — destination-local supplier assembly for trade clients.

## Sources

Fetched 2026-09-09:

- TravelJoy — https://www.traveljoy.com/ (positioning "all-in-one platform for travel advisors"; feature blocks: CRM, itinerary builder, payments & authorizations, booking platform [hotels, activities, insurance], group trips, AI/automations, tasks; plan tiers with per-trip caps and processing-fee tiers); help.traveljoy.com unreachable (timeout ×2 — recorded limitation).
- Tramada — https://www.tramada.com/ (front/mid office framing; corporate/leisure/broker markets; GDS integration for profile upload + booking download; travel documentation [quotes, invoices, receipts, itineraries]; profile management & CRM; transaction fee management [automated fees/mark-ups, commissions, mapped GL codes]; reporting/BI; 50+ integrations; PCI DSS); https://www.tramada.com/solutions/ (Standard [leisure/retail: multi-GDS, content import Expedia TAAP/Stuba etc., itinerary partners Umapped/Axus/Travefy], Broker [IC/broker silos, branding, commission-earnings reporting], Premier [TMC/corporate: online booking engine integrations, traveller portal, BI, payment & expense, compliance/duty of care, reconciliation, "comprehensive travel accounting software with banking functionality"]; partner roster: Amadeus, Sabre, ARC, IATA, Cornerstone, Expedia TAAP, Stuba, Serko, SAP Concur…).
- Midoco — https://www.midoco.de/en (mid- & back-office ERP framing; "Automate Post-Booking Workflows"; NDC; automated invoicing; "Automate BSP and ARC reconciliation and supplier and commission settlements"; accounting hand-off; multi-currency/hedging; PCI credit cards; virtual credit cards; BI exports; 80+ integrations; FAQ defining mid/back-office); https://www.midoco.de/en/midoffice-software-travel/travel-agencies (full feature tables: automated order creation from booking systems [Amadeus, Booking.com], order templates, order history log, sub-agency settlement, invoicing + collective + splitting, voucher handling, EU Travel Directive, order quality management, multilingual invoicing, multi-currency, mandatory fields, GDPR; CRM [campaigns, full customer history, complaints, contact types, multiple addresses, blacklist, credit limits, Umbrella Profiles sync]; payment [PCI packages, POS terminals, payment reconciliation, cashbook]; accounting [supplier matching manual/automatic, agency/partner settlement = commission invoices, pre-invoice accrual booking, bank statement import, single margin bookings, accounting rules, booking journal, period closing, FX, dunning, statements, tax schemes]; transaction fee manager [manual + automatic]; task management linked to orders/customers; reporting; add-ons m.Doc/m.Sign/m.Rep/m.CC/m.Fee/m.BSP/m.Webservice).
- Cornerstone — https://ciswired.com/ (Upstream platform: Travel Operations [workflow, unused tickets, schedule change, policy management], Data [acquisition, quality, AI prep, insights, actions], Spend [expense, invoice, payment, human capital]; 63+ platforms integrated, 400+ data sources; verticals OTA/TMC/Leisure Agency/Organizations; roles finance/operations/supplier relations/procurement/IT/data scientist; Navan testimonials: "streamlined our mid office processes", "automate complex booking processes").
- TripMatrix — https://tripmatrix.com/ ("all-in-one platform for travel agencies, DMCs, tour operators, and travel advisors… entire workflow from inquiry to payment"; features: Trips [builder, dynamic price calculator, offers], Contacts, Inventory [products/services with pricing/rates], Payments, Suppliers, CRM, Packages [reusable], Traveler portal, CMS/website, Marketplace [hotel access], AI Import, B2B Partners).

Not reached (limitations): TravelJoy help center (timeout ×2); Tramada implementation-support/online-learning pages (not fetched); Midoco support portal (login-gated); Cornerstone platform subpages (nav-level only); TripMatrix feature subpages (nav-level only). No step-level procedures, exact state names, or numeric limits assertable beyond what pages state; see Source-access Limitation.

---

## Product Observations

### TravelJoy (evidence layer A — official home/pricing)

- Positioning: "The all-in-one platform for travel advisors… CRM, itineraries, and payments, all in one place." Audience: travel planning professionals (advisors); testimonials from independent agents. (A)
- Structure blocks (A): All-in-one CRM ("Your hub for communication, client details, and task management"); Itinerary builder ("Create branded proposals and itineraries to send to clients"); Payments and authorizations ("Process secure, compliant direct payments and authorizations"; invoices); Booking platform ("One place to book hotels, activities, insurance, and more"); Group trip management ("wrangle details for large group trips in one spot"); AI and automation ("automating repetitive tasks and recurring emails"; "Automated tasks and reminders ensure nothing slips through the cracks").
- Plan tiers shape scope: Starter caps trips per year and excludes team members; Pro adds unlimited trips, group bookings, team members, AI/automations. Processing-fee tiers per payment method. (A; tier specifics = vendor pricing detail)
- Client-facing outputs: branded itineraries/proposals, forms, emails. (A)
- Not evidenced on fetched pages: commission tracking from suppliers; GDS/booking-source integrations; supplier ledger. (limitation recorded)

### Tramada (evidence layer A — official home + solutions)

- Framing: "One platform to manage all customer transactions and travel itineraries, with built-in CRM and advanced reporting"; "a 'front' and 'mid' office travel management system designed to cater to the corporate, leisure and broker markets"; "full GDS integration to provide seamless profile upload and booking download capability"; "3,800,000 bookings annually"; "Designed by travel agents, for travel agencies". (A)
- Capability blocks (A): Travel Documentation (no-touch production and delivery of quotes, invoices, receipts, itineraries, brand-customized); Profile Management & CRM (customer and corporate profile database, real-time GDS profile synchronisation); Transaction Fee Management (automated fees and mark-ups, statistical fee tracking, commissions, mapped GL codes to the accounting system of choice); Real-time Reporting (management/sales/financial data, BI dashboards); Third-party Integration (50+ products: content engines, booking tools, offline workflows, expense and commission systems); Secure Payments (integrated gateway, PCI DSS).
- Solutions (A): Standard (leisure/retail: cloud, multi-GDS, payment gateway, itinerary partners Umapped/Axus/Travefy, travel content import Expedia/Stuba/etc., automation + reporting); Broker (broker networks and ICs: "Siloed access to clients, bookings and reporting by IC/Broker", IC-specific branding, "reporting tools to track and predict monthly commission earnings", head-office reporting); Premier (large TMC/corporate: consultant workflow automation + quality control, online booking engine integrations, online traveller portal, real-time analytics/BI, payment and travel expense management, "travel compliance and duty of care", "strong financial control and streamlined reconciliation processes", "comprehensive travel accounting software with banking functionality and controls").
- Partner roster evidences the settlement ecosystem: ARC (Airlines Reporting Corporation), IATA, Amadeus, Sabre, commission/expense systems. (A)

### Midoco (evidence layer A — official home + solution feature tables + FAQ)

- Framing: "Mid- & Backoffice / ERP travel software"; "Technology for Travel Management Companies — Automate Post-Booking Workflows"; FAQ: "mid- and backoffice software… automates and manages all processes after a booking is made, including accounting, invoicing, reporting, and customer service operations". Solutions for Travel Agencies (Business/Leisure), Online Travel Agencies (OTA), Tour Operators — one machinery, three audiences. (A)
- Order processing (A): "When an order is imported from a booking system such as Amadeus or Booking.com, Midoco Midoffice automatically creates an order and a customer record or assigns the order to a customer"; booking systems "provide performance data such as flights, train journeys, car rentals and hotels"; order templates; detailed order history log; settlement of sub-agencies; invoicing + batch/collective invoicing + invoice splitting (per-service, different recipients); voucher handling with redemption reconciliation; EU Travel Directive support; order quality management ("process to ensure mandatory tasks"); multilingual invoicing; multi-currency with hedging; mandatory fields; GDPR support.
- CRM (A): full customer history ("all processes associated with the customer, such as booked trips or changes to contact information"); campaign management (light/pro); complaint management with status; customizable contact types; multiple addresses; customer blacklist (non-service, e.g., payment arrears); credit limits with reachability check; traveler/company profile sync (Umbrella Profiles).
- Payment (A): PCI/DSS leisure/business card packages; POS terminal connection; payment reconciliation via backoffice cashbook; automated cash payments recording; automated server jobs (payment reminder, payment confirmation).
- Accounting (A): supplier invoice matching (manual + automatic); "Agency/Partner settlement: create commission invoices for travel agencies"; automatic booking of preliminary invoices (future liabilities to service providers); bank statement import + reconciliation; single margin bookings; custom accounting rules; fully searchable booking journal; monthly booking-period closing; foreign-currency balancing; automatic dunning; accounting statements (sales-tax reconciliation, open items per order, accrual lists); multiple tax schemes. Plus homepage: "Automate BSP and ARC reconciliation and supplier and commission settlements"; "Touchless preparation of accounting data for smooth financial workflows" (SAP hand-off per CFO testimonial).
- Fees (A): transaction fee manager — manual fees attached to an order; automatic differentiated service-fee rules integrated into workflows (m.Fee add-on tier).
- Tasks & reporting (A): tasks linked to orders and customers; personal task dashboards; task groups; revenue/booking/customer/billing lists; customizable MIS reports.
- Reference clients: TMCs and agency groups (Amex GBT, Lufthansa City Center, TUI, CTM, lastminute, Goway, Easy Avenues). (A, logo wall + case studies)

### Cornerstone / Upstream (evidence layer A — official home + nav)

- Framing: "The travel operations, spend and data platform"; three areas: Data Management (acquire from 400+ data sources, quality, AI prep, insights, actions), Spend Management (synchronize ERP, payment and HR systems with expense and AP), Travel Operations ("Automate workflow and services"). (A)
- Travel Operations modules (A): Workflow; Unused Tickets; Schedule Change (SCM); Policy Management. Scale stats: 63+ platforms integrated; 10B+ transactions processed. (A; stats are vendor-claimed)
- Verticals (A): OTA, TMC, Leisure Agency, Organizations. Roles served: Finance, Operations, Supplier Relations, Procurement, IT, Data Scientist. (A)
- Mid-office position confirmed by customer testimonial: "streamlined our mid office processes" (Navan VP Travel Operations); "automate complex booking processes" (Navan Director). (A, testimonial level)

### TripMatrix (evidence layer A — official home + feature list)

- Framing: "all-in-one platform for travel agencies, DMCs, tour operators, and travel advisors, that covers the entire workflow from inquiry to payment"; "Manage the entire travel agency back office from start to finish." (A)
- Audience blocks (A): Travel agencies ("day-to-day agency operations: faster itinerary creation, centralized client CRM, integrated payments and tracking, branded website with booking engine"); Tour operators ("centralized product and inventory management, custom and predefined tour creation, integrated bookings and payments, flexible pricing and margin control"); Travel advisors (tailor-made itineraries, client profiles, payments); DMCs ("supplier and pricing management, multi-day customized itineraries, automated margins and policies").
- Features (A): Trips module ("consolidate all your inquiries and offers… trip builder to craft detailed itineraries… send offers"; dynamic price calculator; "Manage payment and policies"); Contacts (individual + corporate clients, 360° overview); Inventory (add products/services — accommodations, transportation, experiences — with pricing and rates); Payments (initiate/process/manage, payment list, per-trip details, extra charges); Suppliers (details and services organized); CRM; Packages (reusable); Traveler portal (offers → feedback → booking/payment → documents); Website/CMS; Marketplace (worldwide hotel access); AI Import (PDF offers → structured trips); B2B Partners (reselling partner workflow).
- Integrations (A): Stripe, QuickBooks, Giata, Travelgate, Gmail, Google Maps.

---

## Cross-product Comparison

| Structure | TravelJoy | Tramada | Midoco | Cornerstone | TripMatrix | Verdict |
|---|---|---|---|---|---|---|
| Client/traveller records with history (agency CRM; corporate accounts + travellers) | CRM hub (client details, comms, tasks) | profile management & CRM (customer + corporate profiles) | full customer history, credit limits, blacklist, complaints, addresses | traveler/data acquisition & quality | Contacts + CRM (individual + corporate) | all 5 — definitional |
| Client-bound booking/trip file aggregating third-party services (flights/lodging/ground/tours/insurance) | trips + bookings (hotels, activities, insurance) | bookings downloaded from GDS consolidated per client; all customer transactions + itineraries | orders auto-created from booking-system data (flights, rail, cars, hotels); order history log | bookings from 63+ platforms; operations workflow over them | trips assembled from inventory/marketplace | all 5 — definitional |
| Two-sided money record: client-side invoicing/payments/fees | invoices, payments, authorizations | invoices, receipts, payment gateway | invoicing (collective/splitting), dunning, cashbook, cards, POS | spend: expense, invoice, payment | payments module | all 5 — definitional (client side) |
| Two-sided money record: supplier-side commissions/payables/settlement | not evidenced on fetched pages | commissions tracked; GL mapping; broker commission-earnings reporting; ARC/IATA partners; reconciliation processes | BSP/ARC reconciliation; supplier invoice matching; agency/partner settlement (commission invoices); pre-invoice accruals; margin bookings | supplier relations role; spend/invoice/payment sync | not evidenced (supplier records only) | 2 strong (Tramada, Midoco) + roles-level at Cornerstone — definitional-as-structure on B evidence; client-collection is the A-evidence half |
| Service-fee machinery | (processing fees are platform pricing, not agency fees — not evidenced) | automated fees and mark-ups | transaction fee manager (manual + automatic rules) | (not explicit) | extra charges | 2 strong — common-strong, not definitional |
| Booking capture from external systems (GDS/OBT/API/import) | booking platform (light); manual-centric | full GDS integration (profile upload + booking download); 50+ integrations | automated import from booking systems (Amadeus, Booking.com); 80+ integrations; NDC | 63+ platforms integrated; NDC solutions | marketplace/Giata/Travelgate hotel access; AI document import | dominant at mid/back-office pole, light at front-office pole — common-strong, NOT definitional |
| Quotation/proposal & itinerary assembly | itinerary builder, branded proposals | quotes + itineraries documentation | invoicing-side documents (quotes not explicit) | (not explicit) | trip builder + dynamic price calculator + offers | 3/4 explicit — common-strong |
| Document generation (invoices, receipts, itineraries, vouchers) | invoices, itineraries, forms | quotes, invoices, receipts, itineraries (no-touch, branded) | invoices, vouchers, travel documents (automated delivery) | invoice (spend side) | trip documents, offers | all 5 in some form — standard; voucher depth segment-shaped |
| Task/queue automation around bookings (reminders, quality checks, schedule change, unused tickets) | automated tasks & reminders | consultant workflow automation, quality control | tasks linked to orders/customers; order quality management; automated server jobs; payment reminders | workflow, unused tickets, schedule change, policy management | (light — inquiries/trips statuses) | all 5 at varying depth — standard |
| Reporting/BI | (light on fetched page) | real-time reporting, BI dashboards | MIS reports, revenue/booking lists, exports | data insights/actions core | (light) | all 5 at varying depth — standard |
| Branch/network machinery (ICs, sub-agencies, commission splits, head office) | team members (Pro tier) | Broker solution: IC silos, branding, head-office reporting | sub-agency settlement; employee bonus calculation | (organization-level data) | B2B partners | common (network/host pole) — not definitional |
| Integrated payment processing | cards/ACH processing | integrated gateway (PCI) | PCI card processing, POS, virtual cards | payment (spend side) | Stripe | all 5 — common-strong |
| Corporate-travel machinery (policy checks, unused tickets, duty of care, expense, traveler profiles) | not evidenced | Premier: compliance & duty of care, expense mgmt, traveller portal | business-travel shaped (profiles via Umbrella, credit limits, on-account) | core focus (workflow, unused tickets, schedule change, policy) | not evidenced | segment machinery (TMC pole) — variant |
| Accounting depth | none evidenced (external) | Premier: native travel accounting + banking; GL mapping | hand-off to accounting software + deep ledger machinery (journal, period closing, accruals, tax schemes) | ERP/expense synchronization | QuickBooks integration | variant axis (native ↔ hand-off ↔ none) |
| Regulatory packaging (EU PTR, GDPR, PCI) | PCI processing | PCI DSS | EU Travel Directive, GDPR, PCI, PSD2 | trust center | (not explicit) | regional/variant |
| Consumer-facing surfaces (traveler portal, website/booking engine, campaigns) | client-facing itineraries/forms/emails | traveller portal (Premier) | campaign management | (not explicit) | traveler portal, website, marketplace | optional/variant — agent remains the primary user |
| Own-product catalog with dated departures | absent | absent | absent (tour-operator solution is a separate audience page) | absent | Packages/Inventory lean this way (operator lens) | NOT part of the agency core — the operator/DMC seam |

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures. If any is removed, the software stops being recognizable as a travel agency management system:

1. **The agency's client record** — persistent identified clients of the agency: individual travellers (often household-grouped) and corporate accounts with their travellers, carrying relationship history and commercial standing. The agency's business is repeat relationships, so the client is the anchor to which every booking attaches. *Remove → a booking tool with no customer memory (supplier-side reservation territory) or generic bookkeeping.*
2. **The client-bound booking/trip file aggregating third-party travel services** — the unit of work: one file per client trip, created and maintained by agency staff, that assembles travel services supplied by other businesses (air, lodging, ground transport, tours/activities, insurance, cruise) as individually tracked segments carrying supplier, dates, price, status, and documents. The file is the agency's record of what was promised by whom, for whom, at what price — the agency does not operate the travel. *Remove → generic CRM, or a trip planner with no business record.*
3. **The two-sided intermediary money record** — client-side amounts due (the services' prices plus the agency's own service fees) invoiced, collected, and receipted; supplier-side amounts owed-to and owed (commissions receivable, supplier payables) reconciled and settled — the commission/fee economy of reselling others' supply, which is where the agency's revenue lives. *Remove → an itinerary planner (no money) or bare accounting software (no travel work).*

Jointly-held load-bearing checks: 1 alone = CRM/address book; 2 alone = trip tracker or a supplier's own reservation file; 3 alone = invoicing/accounting software; 1+2 without 3 = itinerary-planning tool; 2+3 without 1 = settlement engine over orphan bookings; 1+3 without 2 = CRM + bookkeeping with no travel work unit.

### L1 — Common Mature Structure (standard capabilities)

- Booking capture from external sources: GDS/booking-tool/API import (dominant at the business-travel/mid-office pole) or marketplace/content connections and manual entry (front-office pole). The system consolidates what was booked elsewhere into the agency's file.
- Quotation/proposal and itinerary assembly with pricing (rates, markups, dynamic calculation) and client-facing branded documents.
- Document generation: invoices, receipts, itineraries, vouchers; templated, brand-customized, automated delivery.
- Integrated payment processing (cards and account-to-account; PCI-oriented) with deposits and payment schedules.
- Service-fee machinery: manually attached or rule-driven differentiated fees/markups.
- Task/queue automation around the booking lifecycle: payment reminders, quality/completeness checks, schedule-change handling, unused-ticket tracking (TMC pole), cancellations/refunds.
- Reporting/BI: sales, revenue, commissions, consultant productivity, management information.
- Multi-branch/network machinery: sub-agency and independent-contractor silos, commission splits, head-office consolidation, employee incentives.
- Multi-currency handling; multi-language documents (regional depth varies).

### L2 — Variant / Optional Structure

- **Segment machinery**: business-travel/TMC pole (policy compliance checks, unused tickets, duty of care, expense integration, on-account billing with credit limits) vs leisure pole (itinerary-building depth, campaigns/marketing, consumer website/portal, group trips).
- **Accounting realization**: native travel accounting with banking (one pole) ↔ deep ledger machinery with touchless hand-off to external accounting (another pole) ↔ plain external export.
- **Booking-capture substrate**: GDS/NDC/OBT/API/file import ↔ marketplace/content APIs ↔ manual entry. Era- and segment-dependent, not definitional.
- **Consumer-facing surfaces**: traveler portals, branded booking websites, campaign management — optional extensions; the software's primary user remains agency staff.
- **Regulatory packaging**: EU Package Travel Directive support, GDPR tooling, PCI certification posture — regional/segment.
- **Deployment & scale**: cloud SaaS for independent advisors ↔ enterprise platforms for global TMCs; broker/host-network postures.
- **Audience extension**: the same mid/back-office machinery sold to OTAs and tour operators (one sampled vendor ships all three audiences) — adjacent population, documented at the boundary.

### L3 — Vendor-specific (research notes only)

- TravelJoy: Starter/Pro tier structure (per-year trip caps, team members), per-method processing-fee pricing, TravelJoy Funds Visa commercial cards, AI/automations gating.
- Tramada: Standard/Broker/Premier packaging; itinerary partners (Umapped, Axus, Travefy); content import partners (Expedia TAAP, Stuba, Room-Res, Helio, Rapidbook); CTM ownership framing; "3.8M bookings annually" claim.
- Midoco: m.* add-on catalog (m.Doc, m.Sign, m.Rep, m.CC Business/Leisure, m.Fee, m.BSP, m.Webservice); Umbrella Profiles companion; MTIX travel index; German/English bilingual feature tables; SAP hand-off testimonial.
- Cornerstone: Upstream platform naming; 63+/400+/10B+/500+ vendor-claimed stats; unused-ticket and schedule-change module naming; Navan/Pretium testimonials.
- TripMatrix: AI Import document processing; Traveler Portal; Marketplace via Travelgate/Giata; B2B Partners; Stripe/QuickBooks integrations; four-audience positioning (agencies/operators/DMCs/advisors).

## Vendor-specific Findings

- Tramada and Midoco are the two products with explicit supplier-side settlement machinery (commissions, supplier invoice matching, BSP/ARC reconciliation, agency/partner settlement invoices) — both sit at the mid/back-office pole serving business-travel-heavy agencies. Commission-side evidence is 2-product strong (B layer), corroborated by Cornerstone's supplier-relations/spend role framing; TravelJoy's and TripMatrix's fetched pages do not evidence commission tracking (limitation recorded).
- Midoco ships one mid/back-office product for three audiences (agencies, OTAs, tour operators) — the strongest single datum that the machinery is audience-portable and that the OTA/tour-operator seams are about the deployment's center, not the module list.
- Cornerstone is operations/data-first (workflow, unused tickets, schedule change, policy) with client CRM absent as a marketed module — evidence that the client record need not be the deepest layer for the system to remain in-type, but its data platform is traveler/booking-centric, keeping structure 1 at the data level.
- TripMatrix evidences the dual-population zone explicitly (agencies + operators + DMCs on one platform): its agency lens (trips from inventory + payments + CRM) vs operator lens (own packages, margin control) shows exactly where the seams run.

## Rejected Findings

- **GDS/NDC/booking-tool capture as definitional** — rejected: dominant at the mid/back-office pole (Tramada, Midoco, Cornerstone) but light/manual at the front-office pole (TravelJoy, TripMatrix) and absent by definition in the paper-era agency. The invariant is the booking file as the agency's own record, not where the booking data originates.
- **"Agency system = CRM"** — rejected: generic CRM structures are present in all samples but the Type's work unit is the travel booking file with supplier segments; a CRM without booking files/settlement does not run an agency.
- **"Agency system = accounting software"** — rejected: the money machinery is travel-shaped (per-service segments, supplier commissions, BSP/ARC-style settlement, vouchers); accounting depth varies from native to hand-off to absent. Generic accounting lacks the booking file.
- **Service fees as definitional** — held common-strong (Tramada, Midoco deep), not definitional: fee-based revenue models are segment-era-dependent; commission-based agency economics function without automated fee machinery.
- **Corporate-travel machinery (policy, unused tickets, duty of care) as definitional** — rejected: TMC-segment strength (Cornerstone, Tramada Premier); leisure-pole products function without it. Variant.
- **Integrated payment processing as definitional** — held common-strong, not definitional: money recording is the invariant; payment rails differ by market/era.
- **Consumer-facing portal/website as definitional** — rejected: optional extension in all samples; the primary user is agency staff in every product.
- **"Travel agency management = OTA back office"** — rejected as identity collapse: Midoco serves both, but the agency deployment centers agent-mediated client files; the OTA deployment centers consumer storefront retail (see Boundary Findings).
- **Own-product catalog with departures as part of the agency core** — rejected: that is the tour-operator/DMC structure; agency samples hold it only at TripMatrix's operator lens.

## Boundary Findings

- **vs Tour Operator Management System** (§26 sibling, processed 2026-09-09; secondary flag DISCHARGED from this side): **keep-both ratified on the money model and fulfillment responsibility.** The tour operator is a principal: it owns a catalog of its own tour products, sells them with margin on dated departures, and operates the travel. The travel agency is a commission/fee intermediary: it holds no product catalog of its own; its booking file aggregates third-party services; its revenue record is commissions receivable and service fees, reconciled against suppliers, with fulfillment responsibility resting with the suppliers. Corroboration from this pass: Tramada's money machinery is commission- and fee-shaped (commissions with GL mapping, broker commission-earnings reporting, ARC/IATA settlement partners); Midoco's is two-sided intermediary accounting (supplier invoice matching, agency/partner commission settlement, BSP/ARC reconciliation) — no sampled agency-side product centers owned departures; TripMatrix only grows that structure on its operator lens. Quoting/itinerary features overlap (both Types quote and document travel); the seams are the product of record, the money model, and who fulfills.
- **vs Destination Management Company Platform** (§26 sibling, processed 2026-09-07; secondary flag DISCHARGED from this side): same seam as the tour operator, sharpened — the DMC assembles destination-local supplier services into client-specific quotes as principal-with-margin and operates on the ground for trade clients; the agency records bookings of others' supply for its own clients and settles commission/fees. Both may quote from suppliers; only one takes principal money and ground-operation responsibility.
- **vs Online Travel Agency / OTA** (§26 sibling, processed 2026-09-08): both are intermediaries over third-party supply with commission-shaped economics; the seam is who operates the software and where the transaction is born — the OTA is the traveler-facing retail storefront (self-service consumer sessions); the agency system is the staff-facing system of record behind agent-mediated sales. Midoco shipping one mid/back-office product for both audiences documents a shared-machinery overlap zone (as with Tourplan's inbound/DMC split); keep-both on the deployment center.
- **vs Corporate Travel Management Platform** (§10 leaf): the corporate travel platform centers the corporate buyer's program (policy, approvals, spend, duty of care for the company's own travellers); the agency system centers the agency's business over all its clients. TMC-segment machinery inside agency systems (policy checks on bookings, unused tickets) is the agency-side mirror, not the buyer's program tool.
- **vs CRM (§07)**: the agency system contains CRM structures (clients, history, campaigns, complaints) but its distinguishing work unit is the multi-supplier booking file and the travel-shaped two-sided ledger; generic CRM has neither.
- **vs Invoicing/Accounting applications (§08)**: the money record here is bound to travel booking files and supplier commission semantics; generic accounting lacks both. Native accounting depth is a variant, not the identity.
- **vs Travel Itinerary Planner** (§26 sibling): the planner is a consumer/personal tool with no client base, no supplier settlement, no business money record; the agency system holds all three.
- **vs Travel Supplier Management** (§26 sibling, unprocessed): watch-item — the agency records suppliers as counterparties (names, services, invoices), but supplier contract/allotment management machinery (contracted rates, allocations) is operator-side; expect that leaf's center to be the supplier-contract relationship, not the reseller's booking file.
- **Strip-away test**: remove the two-sided money record (keep clients + trip files) → itinerary planning / client-management tool; remove third-party aggregation (agency's own products with departures) → Tour Operator Management System; remove the staff-mediated booking file (consumer self-service over third-party supply) → OTA; remove the travel booking file entirely → generic CRM + accounting.

## Historical / Market-Sample Check (§24)

Paper-era retail travel agency (1950s–1980s): client index/ledger cards (individuals, corporate accounts); a manila booking file per trip holding each supplier's confirmation (airline ticket, hotel voucher, car coupon, insurance policy); handwritten invoices and receipts; commission reconciliation against supplier statements and periodic airline settlement plans; service fees where charged; branch owner's bookkeeping. All three defining structures hold with zero modern machinery — no GDS, no payment gateway, no portals, no BI. Regional and platform-era variants (Japanese retail agencies with JRS-style tooling, consortia/host agencies with paper commission splits, early SABRE-era agencies downloading bookings) fit the same structures. The definition does not overfit the GDS-integrated, payment-integrated modern implementation.

## Uncertainties

- **No help-center-depth source reached for TravelJoy** (timeout ×2); its commission-tracking capability and booking-source integrations are unevidenced on fetched pages. The client-side money record is evidenced; the supplier side is not — held as a sourcing limitation, not asserted as absence.
- **Commission/settlement machinery is 2-product strong (Tramada, Midoco) at feature level**; Cornerstone corroborates at roles/platform level only. The two-sided money record is asserted as definitional on B-layer evidence plus the intermediary business model; A-layer confirmation at more vendors would strengthen it.
- **Cornerstone's client/CRM depth** unclear (data-platform framing dominates); its inclusion rests on bookings/workflow/settlement structures. If a future pass finds its center is purely data/spend analytics, it would sit closer to a cross-Type analytics layer — noted, not resolved here.
- **TripMatrix's "back office" self-label** is marketing breadth (its back office is trips+payments+inventory, not GL-grade accounting); treated as front-office all-in-one with operator/DMC extensions.
- **Exact booking-state vocabularies, BSP/ARC file formats, and numeric limits** not documentable at this evidence level; lifecycle described conceptually.
- **Sample skew**: no sampled product is a GDS-vendor agency suite (Amadeus/Sabre agency platforms, VAX-style agent booking portals) — those may be closer to booking-content platforms than management systems of record; flagged for any future pass touching them.

## Final Synthesis

The researched products describe one coherent Application Type: the travel agency's business system of record, operated by agency staff, whose defining core is the joint presence of (1) the agency's client records — individual travellers and corporate accounts with relationship history, (2) the client-bound booking/trip file that aggregates third-party travel services as per-supplier segments — the agency's record of what was promised by whom for whom, and (3) the two-sided intermediary money record — client-side invoicing/payments/service fees and supplier-side commissions/payables reconciled and settled. Around that core, mature products add booking capture from external systems (GDS/OBT/API/marketplace — dominant at the business-travel pole, light at the leisure front-office pole), quotation and itinerary assembly with branded documents, integrated payments, automated service fees, lifecycle task automation (reminders, quality checks, schedule changes, unused tickets), reporting/BI, and branch/network machinery (IC silos, sub-agency settlement, commission splits). Segment machinery varies (TMC policy/duty-of-care vs leisure itinerary depth), accounting realization varies (native ↔ hand-off), and consumer-facing portals remain optional extensions. The boundary against the tour operator and DMC is the principal-vs-intermediary money model and fulfillment responsibility (flags discharged, keep-both); the boundary against the OTA is who operates the software — staff-facing system of record vs traveler-facing storefront — with a documented shared-machinery overlap zone.
