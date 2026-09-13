# Research Notes — Corporate Travel Management Platform

Research date: **2026-09-08**

## Research Goal

Understand what a Corporate Travel Management Platform actually is as an Application Type: what objects live inside it, who uses it, how a business trip moves through it, what rules govern it, and where its boundaries run against the neighboring Types (consumer OTA, expense management, duty-of-care platforms, agency-side systems).

## Initial Boundary

Preliminary hypothesis before research:

- Core use: a company (the travel program owner) manages its employees' business travel — policy-constrained booking, approvals, central payment, consolidated records and reporting.
- Primary users: business travelers, arrangers/delegates (EAs), managers (approvers), travel managers (program admins), finance; fulfillment often involves TMC agents.
- Likely neighbors: Online Travel Agency / OTA (consumer-side), Expense Management Platform (post-trip), Travel Risk / Duty of Care Platform (separate directory leaf), Travel Agency Management System (agency-side), Corporate Card & Spend Platform (payment program), TMS (freight, not people).
- Risk of confusion: modern products bundle travel + expense, so the pre-trip/post-trip seam must be tested, not assumed.

## Research Questions

1. What are the core objects? (trip/itinerary, booking, travel policy, traveler profile, approval, cost object, invoice, content/rates)
2. How does the booking flow work end to end — search → policy evaluation → approval → confirmation → in-trip → settlement?
3. How is policy expressed and enforced? What happens on out-of-policy selections?
4. Who books for whom? What role model exists (traveler, arranger, approver, travel manager, finance, TMC agent)?
5. How does money work — who pays, on what instrument, and how does the company receive the record (consolidated invoice, card feed, virtual card)?
6. How much duty-of-care / traveler tracking belongs to this Type vs the dedicated Travel Risk / Duty of Care Platform leaf?
7. Where does expense management start and this Type end?
8. Do older / TMC-operated / white-label products still fit the same definition (historical check)?

## Representative Products

Selected for market coverage, different operating philosophies and different customer tiers:

| Product | Pole | Customer tier | Evidence level reached |
|---|---|---|---|
| SAP Concur (Concur Travel) | expense-led T&E suite, ERP-adjacent incumbent | enterprise | Tier 2 (official product pages with operational FAQ) |
| Navan (ex-TripActions) | modern all-in-one travel+expense+payment SaaS | mid-market/enterprise | Tier 2 (product pages with FAQ) |
| Perk (TravelPerk + Yokoy) | travel-first SMB/mid-market, now travel+spend | SMB/mid-market | **Tier 1 help center** + Tier 2 product pages |
| BCD Travel (TripSource / GetGoing) | TMC-led pole: platform bundled with agency service | enterprise | Tier 2 (official site) |
| GetThere (Serko) | historical/structural: white-label self-booking tool powering TMC programs | enterprise programs | Tier 2 (official site) |

Egencia (Amex GBT) was planned as an additional TMC-hybrid sample but was unreachable (see Sources).

## Sources

Reached (2026-09-08):

- Perk — https://www.travelperk.com/ (root); /travel-solutions/policies-approvals/; /travel-solutions/centralized-invoicing/
- Perk Help Center (Tier 1) — https://support.perk.com/hc/en-us; Travel category; "Book a trip for someone else"; "Approvers in Perk"
- SAP Concur — https://www.concur.com/en-us (root); https://www.concur.com/products/concur-travel
- Navan — https://navan.com/ (root); https://navan.com/product/business-travel
- BCD Travel — https://www.bcdtravel.com/
- GetThere (Serko) — https://www.getthere.com/

Not reached / abandoned (network-restriction rule applied):

- egencia.com — HTTP 403, two attempts (root and /en/). No Egencia-specific claims made. Secondary evidence only: SAP Concur lists an Egencia integration on its integrations page.
- help.sap.com/docs/SAP_CONCUR — empty response (JS-rendered portal).
- community.concur.com — HTTP 403.
- Navan in-app help center (app.navan.com) — empty response (auth-gated app surface).

Consequence: SAP Concur, Navan and BCD claims rest on official product/marketing pages (Tier 2) rather than help-center articles (Tier 1); assertion strength calibrated accordingly. Perk is the only product with Tier-1 procedural documentation; procedural claims in the final document are therefore worded as common patterns rather than universals where only Perk's help center shows the mechanics.

## Product Observations

### Perk (TravelPerk) — evidence layer A (Tier 1 help center) + B (Tier 2)

**Positioning (Tier 2):** "The intelligent platform for travel and spend"; travel features list: flights, rail, accommodation, car rental, travel alerts, policies and approvals, duty of care, centralized invoicing, VAT recovery, travel reporting; add-ons: 24/7 travel support, FlexiTravel, VIP experience, insurance; spend side: expense processing, workflow designer, corporate cards, lodge card.

**Policies & approvals (Tier 2):** travel policy defined as "a set of rules that outline how employees should book and expense their business travel", with restrictions and exceptions; dynamic budgets — percentage caps on flights/hotels relative to cheapest or median available option; manual approval when needed; automated approvals with full context (trip, policy, cost, reason).

**Booking flow (Tier 1, help center):**
- Book a trip for someone else: "All roles except guests can book trips for other people"; the person booked for "must have a profile on your company's Perk account"; flow = enter trip details → add a traveler → search → select services → select invoicing details and payment method → confirm payment. "Depending on the person's account settings, you may need to complete custom fields, add cost objects, and/or request approval." Confirmation email goes to booker and traveler once "approved or confirmed".
- Roles: roles exist beyond traveler (account admin, approver, financial reviewer, guest); "Approvers" approve "expenses and invoices submitted by employees" and **trips** (article: "Approve submitted expenses, trips, and invoices"); two approval strategies — line-manager flow vs cost-object flow; approval surface: Spend > My tasks > Approvals (web + mobile); financial reviewers (a separate function) handle card transaction/expense matching.
- Offline channel: "Book a trip you can't find on Perk" and the Concierge (Premium/Pro) — travel experts book outside the online inventory; "One of our travel experts will book your trip… they'll get in touch with you."
- Booking mechanics: confirmation number/booking reference; virtual credit card for hotel payment; visa requirement check; flight/train vouchers applied to trips; corporate rates for rental cars; government rates for hotels; hotel labels; blocking hotels from the account; cost objects and custom fields completed before confirming a trip; real-time disruption tracking; hotel invoice collection service.

**Centralized invoicing (Tier 2):** consolidated invoices delivered per trip, weekly, bi-weekly or monthly, PDF/CSV; invoice & payment profiles per legal entity ("Automate which branch of your business receives which type of invoice, and determine who pays"); payment methods: Amex/Visa/Mastercard, SEPA direct debit, top-up; expense software integrations (Ramp, Moss, Pleo, Expensify, etc.); VAT recovery reports.

### SAP Concur (Concur Travel) — evidence layer B (Tier 2, official product pages with operational FAQ)

**Positioning:** "Concur Travel is a corporate travel management platform and online booking tool"; search/compare/book flights, hotels, rail, rental cars in one platform; policy applied during booking; integrations with TMCs, GDSs, ERP, HR, finance, expense ("freedom to work with any TMC or GDS").

**Out-of-policy handling (official FAQ, quite operational):** flags non-compliant choices in real time during reservation; displays policy guidance during booking; highlights preferred options and negotiated rates; may require justification for exceptions; routes bookings through approval workflows for exceptions; tracks and reports violations; enforcement levels configurable — "ranging from warning messages to mandatory approvals or even blocking certain bookings entirely".

**Suite context (product taxonomy on concur.com):** Concur Expense, Concur Travel, Concur Invoice, Concur Request (pre-trip request/approval), Concur TripLink (captures bookings made outside the corporate channel — direct with suppliers), Trip Approval, Company Bill Statements, Budget, Concur Detect/Intelligent Audit/Verify (audit/compliance), Managed Rate Administration, TMC products (Concur Compleat, TravPay Hotel, Traveler Self-Service). Duty of care as a solution campaign: "centralized view of traveler itineraries and bookings"; TripLink extends tracking beyond in-channel bookings.

**Expense seam:** "travel bookings automatically populate expense reports" when combined with Concur Expense; corporate card transaction import + receipt matching; approval hierarchies configurable by spend thresholds and org structure.

**Scale claims (marketing, recorded but not used as structure):** 20,000+ organizations, ~1.7M travel transactions/week, 150+ countries.

### Navan (ex-TripActions) — evidence layer B (Tier 2 with FAQ)

**Booking loop (stated as four steps):** Search → Book → Approve → Track.
- Search: personalized results from booking history, membership programs, team trends.
- Book: "Travelers see in-policy options"; flight stats, hotel reviews, hotel-to-office distances; changes/cancellations in a click.
- Approve: "Either automatically approve all in-policy bookings or direct each request to a set approver based on who's booking or why they're traveling. Out-of-policy bookings are either flagged for review or rejected based on your company's preset approval process."
- Track: traveler location, company trends, carbon footprint, cost savings, spend by department — customizable dashboards.

**Policy:** "Add your company's travel policy once. Travelers see their personalized limits and options. Turn on dynamic policies that adapt automatically to market conditions"; budget limits by category, department, or trip type (FAQ).

**Booking modes:** for yourself / for others ("Delegate employees to book travel for executives, employees, and guests from one account. Traveler preferences and details are applied automatically") / for groups ("Create events with custom spend controls, get cost estimates, and invite travelers to book… Control bookings, budgets, RSVP status").

**Payments:** Navan Travel Payments — "For every travel booking, Navan generates a virtual card for each transaction, so payment details are automatically matched to the correct booking and invoice"; travelers "don't need to enter payment details, front their own money, or submit expense reports"; accounting integrations (NetSuite, QuickBooks, Xero).

**Other:** inventory = flights, hotels, trains, rental cars, black cars sourced from corporate providers, consumer-site partnerships, direct connections; negotiated rates; loyalty points preserved; Navan Rewards (incentive for booking below budget); 24/7 in-house travel agents (chat/call); Navan Pro (Reed & Mackay) for VIP travelers; duty of care: restrict travel to locations, block low-rated hotels, track travelers in real time, targeted notifications.

### BCD Travel — evidence layer B (Tier 2; TMC-led pole)

**Positioning:** "Managed business travel. Open by design." Solutions: Booking & trip management; Program & payment insights; Meetings & events; Consulting (Advito). Technology: TripSource platform, DecisionSource (reporting/insights), BCD Pay, BCD Marketplace, Connect by BCD, APIs.

**Program statement:** "Book and rebook travel with ease. Authorize and automate approvals. Set spend guardrails supported by flexible payment options and productivity-boosting expense solutions. All this and more within a single platform."

**Service layer:** 24/7 customer care, emergency support service; GetGoing = "ready-to-go, all-in-one travel and expense management solution" for smaller programs. Structure confirms the TMC-led realization: same loop (booking + approval + guardrails + payment + expense) delivered as a platform wrapped in agency service.

### GetThere (Serko) — evidence layer B (Tier 2; historical/structural sample)

**Positioning:** "GetThere is the travel management platform designed to handle the most complex travel programs, while remaining intuitive for both travelers and travel managers." Long-lived self-booking tool (founded in the GDS era, historically Sabre-owned; now Serko) still marketed as a "Corporate Travel Management Platform".

**Structural evidence:** white-label capability — TMCs and global programs brand it as their own; "Configure supplier preferences and travel policies at any level – for individuals, teams, or your entire organization"; "algorithms return the best combinations of fares and rates, based on your travel program preferences and evaluated through your travel policies"; content from multiple sources including NDC; integrations with expense management and ERP systems; Conferma partnership (virtual card payments); localization in 16 languages; powers "the world's biggest global programs and travel management companies".

**Historical significance:** this is the early-2000s corporate self-booking tool archetype — no dynamic budgets, no in-app chat agents, no virtual cards at origin — yet it carries the same core: policy evaluation at booking, program-level configuration, corporate content, TMC fulfillment relationship, expense/ERP data handoff. Confirms the Type is older than the current SaaS generation and not defined by any single modern mechanism.

## Cross-product Comparison

| Structure | Perk | SAP Concur | Navan | BCD Travel | GetThere | Verdict |
|---|---|---|---|---|---|---|
| Company-owned traveler population with profiles | A (profiles required; guests bookable) | B (HR integration; traveler records) | B (invite employees & guests; preferences stored once) | B (TripSource travelers) | B (program users) | Defining |
| Travel policy evaluated at booking with consequences | A (policy rules; dynamic budgets; approval) | B (real-time flags; justify; approve; block) | B (personalized limits; auto-approve or route; reject) | B ("authorize and automate approvals", "spend guardrails") | B (policies evaluated through shopping) | Defining |
| Governed booking of record for an identified traveler | A (booking + confirmation + reference) | B (bookings; TripLink captures out-of-channel) | B (Search→Book loop; changes/cancellations) | B (book & rebook) | B (self-booking of record) | Defining |
| Company-side control & visibility (approvals + program reporting) | A (approver role; My tasks; travel reporting) | B (approval workflows; violation reporting; dashboards) | B (Approve step; Track step; dashboards) | B (DecisionSource insights) | B (program reporting feeds; adoption/compliance focus) | Defining |
| Aggregated multi-supplier content (air/hotel/rail/car) + corporate rates | A/B (inventory; Perk rates; corporate car rates; gov rates) | B ("unmatched supplier content"; negotiated rates) | B (multi-source inventory; negotiated rates) | B (marketplace) | B (multi-source incl. NDC) | Common core |
| Delegated booking (arranger for others, guests) | A (explicit article) | B (arranger/delegate behavior; TripLink) | B (explicit "for others" mode) | B (arranger tools) | B (agency+traveler mixed use) | Common |
| Approval machinery (routes, reason/justification, roles) | A (approver role; strategies; trip approval) | B (explicit FAQ) | B (explicit loop step) | B (authorize) | partial (program-configurable) | Common |
| Central payment & settlement (consolidated invoicing, corporate/virtual cards, cost objects) | A/B (centralized invoicing; VCC; cost objects) | B (Company Bill; card feeds; payment providers) | B (virtual card per booking) | B (BCD Pay) | B (Conferma virtual cards) | Common |
| Offline/agent channel (TMC or in-house agents, 24/7) | A (Concierge; 24/7 support) | B (TMC integrations; TMC products) | B (in-house agents 24/7; Pro) | B (TMC service layer) | B (TMC fulfillment behind tool) | Common |
| Expense connection (bookings → expense report/ERP) | B (expense integrations) | B (auto-populate expense reports) | B ("never file an expense report"; accounting sync) | B (expense solutions) | B (expense/ERP integration) | Common |
| Itinerary delivery, changes, disruption handling | A (emails, vouchers, disruption tracking) | B (Trip Changes; itineraries) | B (live trip updates) | B (trip management) | B (trip management) | Common |
| Traveler location visibility (duty-of-care baseline) | B (traveler tracker; duty of care page) | B (centralized itinerary view) | B (track travelers real time) | B (TripSource visibility) | not emphasized | Common (baseline) |
| Group/event travel with own budgets | B (Group Trip add-on) | not observed as core | B (explicit group mode) | B (Meetings & events solution) | not observed | Optional |
| Unused tickets / vouchers applied to future trips | A (voucher article) | B (community topics: flight credits) | not directly observed | not observed | not observed | Optional |
| Sustainability / carbon / VAT reclaim | B (Green Trip; VAT recovery) | B (sustainability campaign; global tax) | B (carbon footprint dashboards) | B (sustainability solution) | B (CO2 display) | Optional |
| AI assistant layer | B (Perk AI) | B (Joule, Booking Agent, Policy Navigator) | B (AI assistant) | B (AI-enabled processes) | B (modern retailing) | Optional (current-market) |

## Canonical Model

### L0 — Defining Invariant (minimal)

Three structures, jointly held:

1. **The company travel program as container** — an organization-owned configuration over a population of travelers: who may travel (profiles with traveler-specific data), under what rules (the travel policy), and with what company content (preferred suppliers / negotiated rates / program preferences). *Remove → a consumer OTA or generic booking site.*
2. **The governed booking of record** — a persistent booking for an identified traveler (self-booked or delegated), created through in-platform search over aggregated travel content, with the policy evaluated at the moment of booking and a real consequence attached (guidance, flag, justification, approval, block). *Remove → a listing/search site; nothing is governed.*
3. **The management loop on the company side** — booking events and program state roll up to company-side actors: approval where configured, plus consolidated visibility (who is traveling, where, what it costs, against which budget/cost object). *Remove → a self-booking storefront with no program behind it.*

The joint hold is load-bearing: (1+2) without (3) is an OTA pointed at employees; (3) without (2) is a reporting/expense layer, not travel management.

Deliberately **not** in L0 (all common but removable): approval as a mandatory stage (configurable — auto-approve is a documented mode), central payment machinery (a white-label OBT delegates settlement to its TMC), expense reports, traveler tracking, 24/7 agents, negotiated rates as a hard requirement, mobile app, AI.

### L1 — Common Mature Structure

- Aggregated multi-supplier content: flights, hotels (incl. OTA-sourced lodging), rail, car rental, ground transport; corporate/negotiated rates surfaced and preferred.
- Traveler profile: personal details, preferences, loyalty programs, seat choices, travel documents/visa needs; preferences applied automatically on delegated bookings.
- Delegated booking and guest travelers (arranger books for executives/employees/guests; guests without accounts bookable by others).
- Approval machinery: approver roles, approval queues, reason/justification capture, configurable routing (line manager vs cost object vs auto-approve), send-back/reject outcomes.
- Central payment and settlement: consolidated invoicing (per-trip or periodic), payment profiles per legal entity, corporate cards, virtual cards per booking, cost-object/cost-allocation fields at booking.
- Itinerary lifecycle: confirmation records/numbers, emails, self-service changes and cancellations, vouchers/unused-ticket credits applied to future trips, disruption alerts.
- Agent/offline channel: in-house or TMC agents (24/7), offline booking requests for content not available online, service tiering for VIP travelers.
- Program reporting/analytics: spend by department/trip type, compliance, savings, carbon; customizable dashboards.
- Expense and ERP/accounting connections: bookings and card transactions flow into expense processing and financial systems.
- Baseline traveler visibility: itinerary-grounded view of where travelers are (duty-of-care entry level).
- Role model: traveler, arranger/delegate, approver, travel manager/program admin, finance, (TMC) agent; guests as non-account subjects of bookings.

### L2 — Variant / Optional Structure

- Operating model: independent SaaS vendor vs TMC-bundled platform vs white-label OBT operated by/for TMCs.
- Suite shape: travel-first with expense add-on vs full T&E suite vs expense-led suite with travel module.
- Policy philosophy: static rule sets vs dynamic budgets/policies that move with market prices; enforcement strictness from warning-only to hard block.
- Customer tier: SMB self-serve instant setup vs enterprise configured programs (multi-entity, multi-country, HR/ERP integration depth).
- Group/event travel (offsites, conferences) with separate budgets and RSVP machinery.
- Sustainability/carbon tooling, VAT reclaim, travel insurance, VIP services.
- AI assistance layer (agents, policy Q&A, auto-rebooking).

### L3 — Vendor-specific (research notes only)

- Navan: Navan Rewards (funded incentive), Navan Edge, Navan Pro/Reed & Mackay, Navan Connect, Navan Travel Payments virtual-card-per-booking.
- Perk: Concierge, FlexiTravel (cancel-for-refund), Green Trip, Perk Card/Lodge Card/UBS & Visa card programs, hotel labels, MCP server.
- SAP Concur: TripLink, Concur Request, Company Bill Statements, Joule (Booking Agent, Meeting Planning Agent, Policy Navigator, Trip Changes), Concur Compleat/TravPay (TMC products), Intelligent Audit/Detect/Verify, Managed Rate Administration.
- BCD: TripSource, DecisionSource, BCD Pay, BCD Invite, BCD Marketplace, GetGoing, Advito consulting.
- GetThere: white-label branding, Serko lineage, NDC content, Conferma partnership.

## Rejected Findings (checked and kept out of the canonical core)

- **"Travel management = expense management"** — every sampled product bundles expense, but the expense-report/reimbursement machinery is its own Type; here it appears as a *connection* (bookings populate expense). Rejected as defining.
- **"Dynamic budgets/policies are the definition of modern policy"** — Perk and Navan center percentage-based/dynamic budgets; Concur documents threshold/approval-based enforcement. Static rule sets remain valid. Variant, not invariant.
- **"Virtual card per booking"** — common current implementation of payment; GetThere-era programs settled via TMC consolidated billing without per-booking cards. Common implementation, not definition.
- **"Approval is mandatory for every trip"** — auto-approve of in-policy bookings is a documented mode in at least two products; the invariant is policy evaluation with consequences, not universal human approval.
- **"24/7 agent support is part of the definition"** — GetThere's classic deployments carry agent support via the TMC outside the tool; Perk/Navan/Concur embed it. Common, not defining.
- **Marketing metrics** (95% compliance, 16% savings, transaction volumes) — vendor claims, not structure; excluded.

## Boundary Findings

- **vs Online Travel Agency / OTA:** the decisive test — remove the program container (profiles + policy + program reporting) and what remains is an OTA pointed at employees. Conversely, an OTA has no approver role, no policy consequence, no cost objects, no consolidated company billing. The traveler-facing booking UX is deliberately convergent (products advertise "consumer-like" booking); the governance layer is the Type.
- **vs Expense Management Platform (§08 sibling, unprocessed at pass time):** center-of-gravity seam — pre-trip governed booking vs post-trip expense report/reimbursement. The seam object is the booking record: this Type produces it and hands it forward; expense consumes it. All sampled products blur the line at product level (bundled suites), so joint review is recommended when the expense-management-platform leaf is processed. Recorded in STATUS.md Boundary Issues.
- **vs Travel Risk / Duty of Care Platform (§10 sibling):** this Type's tracking is itinerary-grounded visibility (where are my travelers, what did we book) — a reporting capability. The dedicated duty-of-care Type adds risk monitoring, alerting, and case response operations. Direction of data flow: itinerary records flow from this Type into duty-of-care tooling.
- **vs Travel Agency Management System (§26):** opposite side of the commercial relationship — the agency's own operations (client files, commissions, PNR fulfillment queue) vs the buying company's program. The same trip may exist in both systems; the PNR handoff is the seam.
- **vs Corporate Card & Spend Platform (§08):** payment-program center vs travel-program center. This Type *uses* cards (corporate, lodge, virtual) as instruments; the card Type defines and governs the card population. Virtual-card-per-booking products sit at the seam.
- **vs TMS (§18):** freight/goods vs people; "transportation management" in the freight sense shares only vocabulary.
- **vs Travel Itinerary Planner / OTA-adjacent consumer Types (§26):** no program, no policy, no company money — consumer-side planning/booking.

## Uncertainties

- Exact approval-state vocabularies per product (submitted → approved → ticketed/confirmed) were not fully traversable at help-center level for Concur/Navan; final document describes conceptual states without asserting exact labels.
- Whether *every* product supports cost objects at booking is unverified (Perk documents it explicitly; Concur/Navan show cost-center/department dimensions in reporting and policy scoping) — final doc says "commonly" not "always".
- Egencia (Amex GBT) unreachable; the TMC-hybrid pole is carried by BCD Travel and GetThere instead. No Egencia-specific claims.
- Historical depth beyond GetThere (e.g., 1990s-era proprietary corporate booking systems) was not directly researched; the GetThere generation plus the TMC-fulfillment model is treated as sufficient evidence for the historical check.
- The precise boundary of "management" when a TMC fulfills everything offline (some small programs): the software still holds policy/booking/reporting; fulfillment depth varies. Not resolved further — recorded as variant.

## Final Synthesis

A Corporate Travel Management Platform is the **buying organization's system for running employee business travel as a governed program**. Its world is built from three jointly-held structures: the company travel program (traveler population + policy + company content), the governed booking of record created by travelers or their delegates under policy evaluation, and the company-side management loop (approvals plus consolidated program visibility). Around this core, mature products add multi-supplier content aggregation, delegated booking, central payment and settlement (consolidated invoices, corporate/virtual cards, cost objects), itinerary lifecycle and disruption handling, an agent/TMC service channel, program analytics, and connections into expense and accounting. The Type predates the current SaaS generation — the classic TMC-operated self-booking tool carries the same core without modern payments or AI — and its boundary against consumer OTAs, expense platforms, duty-of-care platforms, and agency-side systems is stable: governance and the program are what make it this Type.
