# Research Notes — Plumbing Business Management

Research date: 2026-09-09
Leaf: Plumbing Business Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster, line 2110)
Slug: plumbing-business-management

## Research Goal

Understand what "Plumbing Business Management" software actually is in the real market: what objects it manages, how plumbing work flows through it, what is plumbing-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings, fire protection/elevator with their compliance loops, water treatment/septic adjacencies, CMMS/EAM, construction project management, utility field service).

Family context carried into this pass: the fire-protection-service-management pass found a structurally distinct trade object (code-mandated recurring inspection program + persistent deficiencies + outward compliance reporting) and predicted that electrical/HVAC/plumbing differences would be "configuration/content tuning over the generic FSM spine". The electrical, garage-door, handyman, and HVAC passes all confirmed the two-pole family structure from their sides, and the garage-door and handyman passes explicitly placed plumbing in the trade-tuned pole. The open questions for plumbing: (1) does plumbing carry any structurally distinct trade object — most plausibly a code-mandated testing loop (backflow-prevention device testing is widely mandated by water jurisdictions) — or is it a trade-tuned variant like electrical/garage-door/handyman/HVAC? (2) what is the plumbing trade's own color within the trade-tuned pole (the HVAC pass found the equipment-and-membership economy; the locksmith pass found emergency-speed dispatch)?

Naming note: the leaf is "Plumbing Business Management" while siblings are "HVAC Service Management" / "Electrical Service Management". The market vocabulary is "plumbing software" / "plumbing business software" (ServiceTitan's page headline is literally "PLUMBING BUSINESS SOFTWARE"); the leaf-name difference is lexical, not structural.

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a plumbing service and installation company — residential service/replacement, light commercial, and commercial plumbing.
- Core objects likely: customer + service location, job/work order with lifecycle, estimate/proposal, schedule/dispatch, plumber (technician), invoice/payment, price book, memberships/service agreements.
- Trade-specific candidates to test: water heater replacement as the big-ticket product sale (the plumbing analog of HVAC system replacement), drain cleaning as a distinctive recurring service, backflow-testing compliance loops, emergency/24-7 call handling, water-treatment (softener/filtration) adjacency, repipe/fixture work, licensing/permit structures.
- Closest neighbors: Small Business Field Service Management (likely the same structural spine), trade siblings (HVAC/electrical/appliance repair/garage door/locksmith), Fire Protection / Elevator Service Management (compliance-loop siblings), Water Treatment Business Management and Septic (adjacent trade leaves), CMMS/EAM (asset-ownership line), Construction Project Management (commercial installation projects), Utility Field Service Management (different operator).

## Research Questions

1. What objects make up the system (customer, location, job, estimate, appointment/visit, technician, equipment, agreement, invoice, payment, price book)?
2. How does plumbing work flow from inquiry to payment? What is the work mix (service call, repair, maintenance visit, fixture/equipment replacement-install, commercial work)?
3. What is plumbing-specific in the market: water heater replacement economy, drain cleaning, backflow testing, emergency call handling, water-treatment adjacency, flat-rate pricing, membership plans?
4. Does plumbing carry any code-mandated, compliance-shaped program object (fire-protection style), or is recurring maintenance voluntary/commercial?
5. How do the residential, light-commercial, and commercial poles differ in the products?
6. Which interfaces do users actually operate (office dashboard, dispatch board, job detail, mobile app, customer-facing surfaces)?
7. Historical check: would older, regional, trade-agnostic, or paper-era operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers (mirroring the HVAC pass sample for family comparability, since the same vendors lead both trades):

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| ServiceTitan | flagship "software for the trades"; plumbing a headline trade; residential + commercial + construction poles over one platform; deepest trade content (estimating sub-page, platform-data trends articles) | Tier 2 (plumbing industry page + estimating sub-page + State-of-the-Trades data article) |
| FieldEdge | trades-heritage mid-market product ("We created FieldEdge, a plumbing software"); multi-truck SMB/mid-market positioning | Tier 2 (plumbing industry page incl. FAQ) |
| Workiz | SMB home-services platform, AI-forward; dedicated plumbing industry page | Tier 2 (plumbing industry page incl. FAQ) |
| Housecall Pro | micro-SMB residential home services; help center documents a dedicated preconfigured Plumbing package (one of only three industry packages) | Tier 1 (help center: Industry Packages collection + Plumbing Package Overview) |
| Kickserv | micro-SMB; simple, low-cost, trade-agnostic service business management | Tier 1 (knowledge center: Jobs article) |
| Service Fusion | SMB–mid; all-in-one multi-trade suite with a dedicated Plumbing industry page (~30 clone industry pages over one product) | Tier 2 (plumbing industry page incl. FAQ) |

Attempted-and-abandoned per source-access rules: Workiz plumbing at /industries/plumbing/ (404 ×1 — correct slug /industries/plumbing-software/ found via footer); Jobber (403 in prior sibling passes, not retried); Simpro and ServiceTrade (403 in the fire-protection pass, not retried); Successware (WAF-rejected in the garage-door pass).

## Sources

Fetched 2026-09-09:

- ServiceTitan (Tier 2): https://www.servicetitan.com/industries/plumbing-software — plumbing industry page incl. FAQ; https://www.servicetitan.com/industries/plumbing-software/estimating — plumbing estimating sub-page; https://www.servicetitan.com/toolbox/state-of-the-trades/trends/residential-water-heater-replacement-seasonal-trends — platform-data trends article (water heater replacement seasonality)
- FieldEdge (Tier 2): https://fieldedge.com/plumbing-software/ — plumbing page incl. FAQ
- Workiz (Tier 2): https://www.workiz.com/industries/plumbing-software/ — plumbing industry page incl. FAQ
- Housecall Pro (Tier 1): https://help.housecallpro.com/en/collections/19689640-industry-packages — Industry Packages collection; https://help.housecallpro.com/en/articles/15936858-plumbing-package-overview — Plumbing Package Overview
- Kickserv (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs — "Jobs" article (Kickserv Knowledge Center)
- Service Fusion (Tier 2): https://www.servicefusion.com/plumbing-software — "Plumbing Software" industry page incl. FAQ

Family counterparty sources (prior sibling passes, same date range): research/hvac-service-management.md, research/electrical-service-management.md, research/garage-door-service-management.md, research/handyman-business-management.md, research/fire-protection-service-management.md, research/appliance-repair-management.md, research/locksmith-business-management.md.

## Product A — ServiceTitan

### Key observations (evidence layer A unless noted)

- Plumbing is a headline trade in the residential nav ("Plumbing Software"), one of ~20 trade pages over one platform — same one-platform-many-trades packaging pattern the electrical/garage-door/HVAC passes observed. The commercial nav carries a separate "Plumbing" trade entry alongside Mechanical (HVAC), Refrigeration, Electrical, Water Treatment, Fire & Life Safety, Dock and Door. [Layer B support: FieldEdge, Workiz, Housecall Pro, Service Fusion show the same pattern.]
- Residential pole, trade-labeled: Marketing ("invest only in residential advertising strategies that keep your phone ringing"), Call Booking, Estimates ("Increase average tickets for residential plumbing jobs"), Customer Experience, Dispatching, Mobile App, Invoicing ("Modernize invoicing with residential plumbing software"), Accounting ("Streamline bookkeeping with plumbing accounting software").
- Commercial pole, trade-labeled: Proposals ("Easily build multi-option proposals to win more jobs"), Job Costing ("Ensure profitability on every commercial plumbing job"), CRM, Reporting, **Service Agreement ("Automate your commercial plumbing service agreements")**, Accounting, Pricing ("Grow your profit margins with plumbing pricing software"), Client Portal.
- Construction pole (installation work): Project Management, Billing ("Bill customers at every phase"), Crew Management, Inventory, Estimating, Dynamic Forms, WIP Reporting.
- FAQ definition: "Plumbing software automates your company's day-to-day scheduling, dispatching and billing systems to improve efficiency and profitability. This essential tool for plumbing companies makes it easy for techs to estimate residential, commercial, and construction plumbing jobs, view customer history, invoice customers as soon as they finish the job from a mobile tablet, and communicate with office staff at the same time." — entirely generic FSM vocabulary.
- FAQ: dispatchers "receive reminders to assure a technician's skills match the job's requirements, while maintenance agreements become easier to manage"; customers view "good-better-and-best service options"; GPS tracking for arrival times; Mobile 2.0 app; QuickBooks Online/Desktop integration.
- Estimating sub-page (Tier 2): "Price Commercial and Residential Jobs Accurately" — flat-rate pricebook imagery; Pricebook Pro "gives plumbers access to the catalogs of a range of key industry suppliers so the prices reflect the actual materials that will be used"; automated pricing updates across the pricebook; mobile Good-Better-Best proposals with financing; estimate follow-up tracking; after approval: electronic purchase orders, scheduling/dispatch of the work order, invoice generation, on-the-spot payments, QuickBooks/Intacct sync; tech scorecards track "number of calls per day, estimates closed, revenue generated, maintenance agreements sold". The commercial estimating process guide references quantity takeoff and dedicated takeoff tools (Planswift, FastPipe, McCormick) for construction plumbing.
- State-of-the-Trades data article (official vendor platform data, Aug 2026): "Residential water heater install volume jumps well above the yearly average every January" — January indexed 118 (2024) and 124 (2025) against a 100 baseline, a smaller October bump; "Water heaters have the shortest median replacement age of any major home system at 11.3 years"; guidance: plan staffing/inventory for the January peak, run replacement campaigns in November–December, "target outreach using equipment age" for proactive replacement conversations; "ServiceTitan helps plumbing contractors prepare for seasonal demand with scheduling and dispatch tools, customer and equipment history, targeted marketing". A related article benchmarks replacement lifespans for "Furnaces, ACs, Heat Pumps & Water Heaters" — water heaters treated inside the same equipment-replacement analytics as HVAC equipment. A financing article (tagged HVAC, Plumbing, Electrical) reports financed jobs carry a median ticket 64% higher.
- Marketing claims (kept out of the canonical document): 17% average revenue growth, 4.7/5 shop rating, 6% close-rate increase on the industry page; 16%/9%/10% claims on the estimating page; Roto-Rooter and Rainforest Plumbing & Air testimonials.

No plumbing-specific structural object on any fetched page; the trade layer is labeling + tuning (pricing, proposals, agreements, water-heater-seasonal marketing) over the platform.

## Product B — FieldEdge

### Key observations (evidence layer A)

- Trades-first self-positioning: "The Plumbing Software That Scales Multi-Truck Operations"; FAQ — "We created FieldEdge, a plumbing software, focused specifically on helping businesses streamline their daily operations including dispatching, payment processing, customer management, and much more." Same vendor carries HVAC/Electrician/Locksmith/Appliance Repair industry pages over one product.
- Feature blocks: Plumbing Dispatch Software ("Assign the right plumbers for the right job based on skills, location, and availability"; GPS tracking across trucks and job sites); QuickBooks sync; **Customer Management ("Access full work order histories, invoices, quotes, and service agreements from anywhere")**; Plumbing Invoicing (complete on-site, email, mobile payments); Plumber Mobile App ("Update work orders, capture photos, add notes, and make service recommendations from the field").
- Value pillars: flat rate tools ("Drive consistent pricing with flat rate tools that prevent revenue slippage on every job"); Proposal Pro ("Present Good-Better-Best options… to convert more quotes at higher ticket values"); MarketingEdge ("Build a repeatable sales process… to upsell service agreements and retain customers"); job-level profitability and plumber-efficiency reporting; multi-business-unit/multi-location scaling; standardized templates/forms/workflows.
- FAQ: scheduling/dispatch by "availability, location and skill set"; inventory management; CRM; automated appointment reminders and follow-ups; on-site payments.
- Marketing claims (kept out of canonical doc): 20+ hours saved/week, 138% ROI, 40,000+ users, 40 years of experience.

Nothing structurally plumbing-specific beyond the emphasis: the named trade objects are work order histories, quotes, and service agreements inside the customer record — generic-in-kind objects carrying trade weight.

## Product C — Workiz

### Key observations (evidence layer A)

- Dedicated plumbing page at /industries/plumbing-software/ ("Plumbing Software — Designed for Smart Plumbers… trusted by over 120,000 pros"); the platform serves ~50 industries with plumbing among six footer-listed trades.
- Trade-tuned sections:
  - **Service plans**: "Turn every job into recurring revenue. Boost slow months by pre-booking periodic tank cleanings, filter changes, and inspections." — the sample's most explicit plumbing work-content statement: tank cleanings (water heater maintenance) and filter changes (water treatment/filtration) as plan-covered recurring visits.
  - Sales proposals: "Close larger deals by quoting Good|Better|Best options that fit any budget."
  - Smart dispatching: "Dispatch the right tech with the right skills to every job… drag-and-drop calendar, or have AI do it for you."
  - Workiz Pay: "credit card, mobile wallet, cash, ACH, or consumer financing."
  - Multi-day projects: "Run complex projects without losing visibility. From non-consecutive multi-day scheduling, to section management, costs, materials, and billing… big plumbing projects."
  - Checklists: "templates for quoting, installs, repairs, and maintenance visits."
  - Reputation manager: "Clients want to work with plumbers who will fix the problem, not create a new one."
- **Emergency handling (explicit)**: FAQ — "Can Workiz handle schedule changes due to emergency calls? Absolutely!… Workiz's integrated Communications Suite can take calls 24/7 or whenever your dispatchers have their hands full, and the Online Booking feature enables customers to book your services anytime." Genius AI Answering "captures every lead 24/7 so you never miss a job."
- Partner logos on the plumbing page include HVAC equipment manufacturers (Carrier, American Standard, Trane, Bryant), JB Warranties (extended warranties), Angi, QuickBooks — the same partner ecosystem as the HVAC page; integrations include Thumbtack, Angi, Google Local Services Ads, Linxup GPS, Sunbit/Wisetack financing, NiceJob.
- FAQ definition: "Plumbing business software is a customizable field service management platform that streamlines your day-to-day operations… streamline scheduling, enhance customer management, and grow your business."

## Product D — Housecall Pro

### Key observations (evidence layer A, Tier 1 — help center)

- **Industry Packages collection: HVAC, Electrical, and Plumbing only** (4 articles incl. Tech Leaderboard) — plumbing is one of only three trades with a dedicated package; garage door, handyman, appliance repair, locksmith have none (documented from their sides in prior passes).
- Plumbing Package Overview article: "The Plumbing Package is Housecall Pro built specifically for residential and light-commercial plumbing businesses. It comes preconfigured with the tools, workflows, and settings plumbing Pros use every day, so you can get up and running fast without building from scratch."
- Package tier table (Basic/Essentials/MAX): core Housecall Pro features + **Plumbing KPI Dashboard** ("revenue, jobs, team performance, and memberships at a glance"), **Purchase Orders** ("tied to a job's material line items… what gets ordered, from which supplier, and when"), **Surcharging (no fee)**, Sales Proposal Tool, **Membership Plans**, **Price Book Commissions** ("Set commissions on individual price book line items so your techs are paid accurately for what they sell"), Pipeline (MAX), **Pricing Insights** (MAX: "Live pricing benchmarks built right into your Housecall Pro price book, based on real jobs across the Housecall Pro community").
- Selling Membership Plans on Jobs and Estimates: "Sell a membership plan right on any job or estimate with one signature and one payment."
- Also bundled: Photo Reports, Checklist Automations, Tasks on jobs/estimates, Job Splits, Automated Sales Tax, Marketing dashboard, QuickBooks Online sync, "plus all the standard tools in your plan, including scheduling, estimates, invoicing, payments, online booking, and reporting."
- Vendor typo recorded: the article's "New features built for Plumbing" section carries the heading "The following features are exclusive to the Electrical Package" — a copy-paste slip that itself evidences the packages are cloned across trades.
- The plumbing package's exclusive layer is entirely sales/recurring-revenue machinery (memberships, proposals, commissions, pricing insights, KPIs) plus purchasing — no new core object is introduced; identical in kind to the HVAC package's exclusive layer.

## Product E — Kickserv

### Key observations (evidence layer A, Tier 1)

- "Jobs are the heart of the Kickserv workflow. Jobs are what your technicians are completing out in the field and the main way you'll keep track of business activity."
- Jobs board: left-to-right workflow Unscheduled → In Progress → Completed, with optional On Hold column ("Jobs can skip the On Hold column").
- Job creation: service type, internal job description ("will not be seen by the customer"), external scope of work ("will be seen by the customer"), contact from customer records; custom data fields (Standard plans and above).
- Conversion path: "Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job!"
- Scheduling: inside the job, "Schedule work" → date/time, description for technicians, task type, assign tech (or unassigned) → "Add Event" — a work event is a child of the job.
- Start/Stop Job buttons move the job to In Progress; Mark Complete pops a confirmation to mark all work events complete; multi-visit guidance: "Depending on your industry, you might need to schedule several work events on a single job… keep the job open until all work events are completed, then send a final invoice."
- Job filters: service type, status, tag, assigned technician, time. Recurring Jobs: "Repeat this job" → frequency, day/date, end condition.
- Workflow ends "send an invoice… and get paid."
- Trade-agnostic: nothing plumbing-specific anywhere; plumbing companies are among the trades served. This product anchors the pole where the trade layer is pure configuration.

## Product F — Service Fusion

### Key observations (evidence layer A)

- "Plumbing Software" industry page — one of ~30 clone industry pages over one FSM suite (the pattern documented in the garage-door, electrical, appliance-repair, and locksmith passes). Page subtitle: "More than just plumbing management software, access a field service management suite of enterprise-level features at a small business price."
- Feature blocks: scheduling & dispatch ("See all jobs and estimates in one place and edit with drag and drop"); estimates & jobs ("Create and send estimates with pre-populated product and service line items… Convert estimates to jobs with one click"); mobile app ("Receive dispatched job and estimate assignments… Accept in-person payments with our easy-to-use Stripe mobile card reader… Take job photos and log notes… Capture pre-work and post-work signatures… Create and send invoices"); customer management ("easy-to-use customer web booking portal… automated pre-job text notifications… ServiceCall.ai" VoIP with call/text, auto-routing, call-reason tracking, recording/transcription); GPS fleet tracking; QuickBooks bi-directional sync (customers, products, services; job deposits, invoices, payments); Service Fusion Payments.
- FAQ definition: "Plumbing service software may include any combination of customer management, fleet tracking, estimate creation, invoice management, and payment processing tools designed for the field service industry… Comprehensive field service software programs aim to form more cohesive management systems than single-function programs such as solo plumbing estimating software and work for both residential and commercial service businesses." — the FAQ explicitly contrasts the all-in-one suite with "solo plumbing estimating software", acknowledging a standalone-estimating product market at the edge.
- Marketing claims (kept out of canonical doc): 5M+ jobs created annually, 6,500+ customers, 40% productivity, 95.7% CSAT, "1,000% ROI" GPS claims, no-per-user-fee pricing.

## Cross-product Comparison

| Structure / capability | ServiceTitan | FieldEdge | Workiz | Housecall Pro | Kickserv | Service Fusion | Assessment |
|---|---|---|---|---|---|---|---|
| Customer record with service location | ✓ (CRM) | ✓ (customer management) | ✓ (customer management) | ✓ (Customers) | ✓ (Customers & Contacts) | ✓ (customer management) | Universal — core |
| Job / work order with lifecycle | ✓ (work order management) | ✓ (work orders) | ✓ (jobs) | ✓ (Jobs) | ✓ ("heart of the workflow") | ✓ (jobs) | Universal — core |
| Office→field technician coordination (dispatch) | ✓ (Dispatch; skill reminders in FAQ) | ✓ (skills/location/availability; GPS) | ✓ (skills-matched, drag-and-drop or AI) | ✓ (scheduling, employees) | ✓ (assign tech; work events) | ✓ (drag-and-drop; text/call job info) | Universal — core |
| Estimate/proposal → approval → job | ✓ (multi-option proposals; follow-up tracking) | ✓ (Proposal Pro, good-better-best) | ✓ (Good\|Better\|Best) | ✓ (Sales Proposal Tool) | ✓ (Opportunity→estimate→Job) | ✓ (one-click estimate→job; eSign) | Universal — standard |
| Invoice + payment on completed work | ✓ (Invoicing, Payments) | ✓ (on-site invoicing, mobile payments) | ✓ (Workiz Pay: card/wallet/cash/ACH/financing) | ✓ (Payments) | ✓ (invoices) | ✓ (Service Fusion Payments, Stripe reader) | Universal — core |
| Technician mobile app | ✓ (Mobile 2.0) | ✓ (photos, notes, recommendations, payments) | ✓ (full mobile app; "On my way!" messages) | ✓ (mobile features) | ✓ (mobile app collection) | ✓ (dispatched assignments, photos, signatures, payments) | Universal — standard |
| Price book / line-item pricing | ✓ (Pricing; Pricebook Pro with supplier catalogs; flat-rate) | ✓ (FieldEdge Flat Rate) | ✓ (price book feature) | ✓ (Price Book; commissions; AI Pricing Insights) | ✓ (service types) | ✓ (pre-populated line items; Flat Rate integration) | Universal — standard |
| Maintenance plans / service agreements | ✓ (Service Agreement feature; "maintenance agreements become easier to manage"; agreements-sold on tech scorecards) | ✓ (service agreements in customer record; MarketingEdge upsell) | ✓ (Service plans: "periodic tank cleanings, filter changes, and inspections") | ✓ (Membership Plans; selling on jobs/estimates; memberships on KPI dashboard) | ✓ (Recurring Jobs only — weaker form) | — (not named on plumbing page) | Common-to-universal in trade-oriented products |
| Good-better-best replacement sales motion | ✓ (multi-option proposals) | ✓ (Proposal Pro) | ✓ (Good\|Better\|Best) | ✓ (Sales Proposal Tool) | — | — | Common — trade-typical sales motion |
| Flat-rate pricing presentation | ✓ (flat-rate pricebook; flat-rate services guidance) | ✓ (FieldEdge Flat Rate product) | — (price book present; flat-rate framing not explicit on page) | ✓ (Price Book Commissions) | — | ✓ (Flat Rate integration) | Common in trade-oriented products |
| Water heater / equipment replacement economy | ✓ (platform data: January replacement spike, 11.3-yr median lifespan, equipment-age outreach; equipment history in product) | — (equipment details implied in customer record) | ✓ ("periodic tank cleanings" as plan work) | — (not in package feature list) | — | — | Trade-tuned emphasis; strongest at ServiceTitan (data) and Workiz (plan content) |
| Emergency / 24-7 call handling | ✓ (AI Virtual Agent; "keep your phone ringing"; no-missed-calls story) | — | ✓ (explicit FAQ: emergency schedule changes; 24/7 AI answering; online booking anytime) | — (online booking standard) | — | ✓ (ServiceCall.ai auto-routing; AI call answering) | Common as call-capture; explicit emergency framing at Workiz |
| Consumer financing | ✓ (Integrated Financing; financed-ticket data article) | — | ✓ (Sunbit/Wisetack; financing in Workiz Pay) | — (financing per prior passes) | — | ✓ (Acorn homeowner financing) | Common/optional |
| Purchase orders / parts inventory | ✓ (Purchasing & Inventory; POs after estimate approval) | ✓ (inventory management in FAQ) | ✓ (inventory management) | ✓ (Purchase Orders in package) | — | — | Common |
| Multi-visit / multi-day work | ✓ (construction pole: phases, WIP) | ✓ (multi-phase projects claim) | ✓ (multi-day projects: non-consecutive scheduling, sections, milestone billing) | ✓ (standard tools) | ✓ (several work events per job) | — | Universal — standard |
| Commercial machinery (job costing, PM agreements, client portal) | ✓ (commercial plumbing: Job Costing, Service Agreement, Client Portal) | ✓ (multi-unit/multi-location; job-level profitability) | — (light) | — (light-commercial framing only) | — | ✓ ("residential and commercial service businesses") | Optional; commercial pole |
| Project machinery (phases, costs, WIP) | ✓ (construction pole) | ✓ (multi-phase) | ✓ (multi-day projects w/ costs, sections, billing) | — | — | — | Optional; install pole |
| Accounting sync | ✓ (QuickBooks, Intacct) | ✓ (QuickBooks automated sync) | ✓ (QuickBooks) | ✓ (QuickBooks Online) | ✓ (QuickBooks 2-way) | ✓ (QuickBooks bi-directional) | Universal — standard |
| Reporting / dashboards | ✓ (Reporting; tech/CSR scorecards) | ✓ (job-level profitability, plumber efficiency) | ✓ (reporting; reputation manager) | ✓ (Plumbing KPI Dashboard) | ✓ (Reports) | ✓ (reporting) | Universal — standard |
| Plumbing trade packaging | Plumbing trade page (residential/commercial/construction) + estimating sub-page | Plumbing-first page over multi-trade product | Plumbing industry page over ~50-industry platform | Plumbing industry package (1 of 3) | none (trade-agnostic) | Plumbing clone page (1 of ~30) | The Type's packaging pattern |
| AI assistants / answering | ✓ (AI Virtual Agent, Atlas) | — | ✓ (Genius Answering/Scheduling) | ✓ (HCP Assist per prior pass) | — | ✓ (AI call answering; Notes+) | Optional; era-typical |

### What is actually plumbing-specific (across sample)

1. **Trade-tuned packaging and configuration** — every multi-trade vendor sells "plumbing" as a labeled trade page, solution page, or (at Housecall Pro) a dedicated preconfigured package; Kickserv demonstrates the trade running on a fully trade-agnostic product. [Layer A ×6 vendors]
2. **The work mix: service calls, repairs, maintenance visits, and fixture/equipment replacement-installation** — replacement work is a product sale plus an installation, quoted with good-better-best options and commonly financed; the water heater is the trade's signature replacement product (ServiceTitan platform data: January replacement spike, 11.3-year median replacement age, equipment-age-based outreach; Workiz: tank cleanings as plan-covered recurring work). [Layer A: ServiceTitan data article + Workiz plan content; replacement sales machinery ×4 vendors]
3. **Maintenance memberships/service agreements as a recurring-revenue engine** — plan-selling in the field (one signature/one payment on a job or estimate), membership counts on KPI dashboards, agreements-sold on technician scorecards, plan content naming plumbing-specific work (tank cleanings, filter changes, inspections). [Layer A ×4 vendors; machinery generic, promotional weight trade-tuned]
4. **Emergency-driven demand and 24/7 call capture** — emergency schedule changes and 24/7 AI answering explicitly documented at Workiz; 24/7 call capture and no-missed-calls emphasis common across the sample (ServiceTitan AI Virtual Agent, Service Fusion auto-routing). [Layer A: explicit ×1 (Workiz); call-capture common]
5. **Flat-rate pricing culture and technician-sell compensation** — flat-rate price books (FieldEdge Flat Rate, ServiceTitan flat-rate guidance, Service Fusion Flat Rate integration); per-line-item commissions (Housecall Pro). [Layer A ×3–4 vendors]
6. **Seasonality as a managed pattern** — the water heater replacement cycle (winter peak) drives staffing/inventory/marketing guidance at ServiceTitan; "boost slow months" framing at Workiz. Not a structural object — a calendar/marketing pattern. [Layer A ×2 vendors explicit]

No sampled product showed a *structurally distinct* plumbing object of the fire-protection kind: there is no code-mandated inspection/testing program object, no regulator-facing deficiency pipeline, no compliance-reporting object in any fetched source. Backflow-prevention testing (a real code-mandated practice in many water jurisdictions) appears nowhere in the fetched plumbing pages — recorded as an uncertainty, not claimed in either direction. The trade difference is configuration, content, and business-model emphasis — not a different data model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, building, facility), so jobs bind to addresses; the customer may be a person, a business, or a property hierarchy.
2. **Plumbing job (work order)** — a requested piece of plumbing work (service call, repair, maintenance visit, or fixture/equipment replacement-installation) at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed).
3. **Plumber (field technician) as the executing role** — jobs are assigned to field plumbers and coordinated by the office (scheduling/dispatch).
4. **Billing of completed work** — the job produces an invoice that collects payment (estimate/proposal upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing. Remove billing → a dispatch board only. Remove "plumbing work" as the job's content → the generic Small Business Field Service Management Type.

Historical check: a paper-era plumbing shop (job tickets, a dispatch board, a price list, membership card files for annual maintenance, invoices) satisfies all four properties; 1990s–2000s dedicated field-service products satisfy them; trade-agnostic products configured by a plumbing company satisfy them (Kickserv demonstrates this pole directly; Workiz/Housecall Pro/Service Fusion serve plumbing from multi-trade platforms). None of the modern machinery (mobile apps, GPS, memberships, flat-rate books, AI answering, financing) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/proposals with line items — commonly good-better-best options for replacement work — customer approval (e-signature), conversion into jobs, and follow-up on unsold estimates
- Scheduling calendar + dispatch board; assignment weighted by skills, location, and availability in mature products; GPS-backed status views
- Technician (plumber) mobile app: assigned jobs, customer history, photos, notes, service recommendations, signatures, on-site payment, invoice creation
- Price book of services, parts, and materials; flat-rate presentation (parts+labor bundled as client-ready single prices) common in this trade; per-line-item technician commissions in some products
- Maintenance plans / service agreements: recurring visits (inspections, tank cleanings, filter changes) on a billing cadence, sold at the table or in the field; membership counts surfaced in reporting
- Customer notifications: booking confirmations, reminders, on-my-way alerts, invoice delivery
- Multi-visit jobs (diagnose-then-return) and multi-day installation jobs (non-consecutive scheduling, milestone billing)
- Purchase orders tied to job materials; parts inventory
- Reporting: jobs, revenue, technician performance, membership counts, job profitability
- Accounting sync (QuickBooks in the North American SMB market)
- 24/7 call capture (AI or live answering) so emergency calls are not missed

### Level 2 — Variant / Optional Structure

- Emergency posture: emergency calls as a first-class work class with schedule-displacement handling (explicit at one sampled product); after-hours online booking
- Water heater / equipment replacement economy: equipment-age-based outreach, replacement-lifespan benchmarks, extended-warranty integrations (install + protection sale + labor economics)
- Consumer financing for high-ticket replacement work
- Commercial pole: preventive-maintenance/service agreements, job costing, client portals, multi-business-unit scaling
- Construction/install pole convergence (project management, phase billing, quantity takeoff; standalone estimating/takeoff tools acknowledged at the edge)
- Adjacent-trade bundling: water treatment (softeners/filtration — filter-change plan work; a separate ServiceTitan trade page), septic, HVAC co-marketing (shared partner ecosystems)
- Segment packaging: plumbing-dedicated editions/packages vs trade pages vs trade-agnostic configuration
- AI answering/dispatch/assistant features (era-typical); GPS fleet tracking; payroll; review/reputation machinery

### Level 3 — Vendor-specific (kept out of the canonical document)

- Housecall Pro: Plumbing KPI Dashboard, no-fee credit-card surcharging, AI Pricing Insights, Pipeline, plan-tier gating (Basic/Essentials/MAX), the "Electrical Package" copy-paste typo in the Plumbing Package article
- ServiceTitan: Pro product tiers (Pricebook/Dispatch/Fleet/Marketing Pro…), Atlas, AI Virtual Agent, Follow-Ups, tech/CSR scorecards, Roto-Rooter/Rainforest testimonials, growth claims (17%/6%/4.7; 16%/9%/10%), State-of-the-Trades data series (January index values, 11.3-year median lifespan, 64% financed-ticket premium)
- FieldEdge: ESC/dESCO heritage product line, FieldEdge Flat Rate product, Proposal Pro, MarketingEdge, 40-years/40,000-user/138%-ROI claims
- Workiz: Genius suite (Answering/Scheduling/Marketing), JB Warranties integration, Linxup GPS, Sunbit/Wisetack, Workiz Pay, 120,000-pros claim, 22% revenue claim
- Service Fusion: ServiceCall.ai VoIP/call tracking, Notes+ AI note cleanup, Acorn homeowner financing, built-in GPS, Stripe M2 reader specifics, no-per-user pricing, 5M-jobs/6,500-customer claims
- Kickserv: "Opportunity" object naming for the pre-estimate stage

## Vendor-specific Findings

See Level 3. Notable patterns: Housecall Pro ships a genuinely *preconfigured* Plumbing package (the deepest trade layer in the sample, still made entirely of generic-in-kind capabilities — and its own copy-paste typo reveals the packages are cloned across trades); ServiceTitan is the only sampled vendor publishing platform-data content about the trade's work patterns (water heater replacement seasonality, equipment lifespans, financing economics); FieldEdge is trades-heritage with plumbing as a headline trade; Workiz is the only sampled vendor with an explicit emergency-call FAQ; Service Fusion's plumbing page is a re-skinned clone of its FSM page; Kickserv demonstrates the trade-agnostic pole.

## Rejected Findings

1. **Code-mandated testing/inspection loop (fire-protection style)** — no evidence anywhere in the sample; plumbing recurring maintenance is voluntary and commercial (sold as memberships/agreements). Backflow-prevention testing, though a real mandated practice in many jurisdictions, appears in no fetched source as a software object. Rejected as canonical; confirms the fire-protection pass's prediction that plumbing sits in the trade-tuned pole. (Uncertainty recorded below.)
2. **Licensing/permit structures as software objects** — plumbing is a licensed trade and larger jobs often require permits, but no fetched source documents any license/permit record or inspection-gate object in these products. Not claimed.
3. **Drain cleaning as a structurally distinct service object** — a real and distinctive plumbing service class, but no fetched source models it as anything other than job content/price-book items. Held at content level, not structure.
4. **"Plumbing + HVAC + electrical" as one mechanical-industrial Type** — vendors serve all three from one platform with separate trade packaging; the directory treats them as sibling leaves by trade semantics. One trade, one leaf; no merger proposed.
5. **Standalone plumbing estimating software as this Type** — Service Fusion's FAQ explicitly names "solo plumbing estimating software" as a different, single-function product class; takeoff tools (Planswift, FastPipe, McCormick) serve the construction pole. Estimating is a capability of this Type, not the Type itself.

## Boundary Findings

1. **vs Small Business Field Service Management** — the structural spine is identical (customer+location → job lifecycle → technician coordination → invoice/payment; verified across six products). Vendors ship "plumbing" as a preconfigured trade layer of one product (ServiceTitan trade page; Workiz industry page; FieldEdge trade-first page; Housecall Pro preconfigured package; Service Fusion clone page), and Kickserv demonstrates the trade running with no trade layer at all. Probable trade-Variant relationship rather than two independent Types — now convergently observed by the electrical, cleaning, appliance-repair, garage-door, handyman, HVAC, and locksmith passes. The durable difference is trade semantics: the water-heater/equipment replacement economy, emergency-heavy demand, flat-rate pricing culture, the replacement sales motion, and membership plans. Joint review with Small Business Field Service Management recommended.
2. **vs trade siblings (HVAC, electrical, garage door, appliance repair, locksmith)** — same family pattern; the trade wrapper differs, the spine does not. This pass discharges the fire-protection pass's family-structure question for the plumbing leaf from this side: plumbing belongs to the trade-tuned pole (electrical/HVAC/garage-door/handyman pole), not the compliance pole (fire protection, likely elevator). Family observations from this pass: plumbing shares the equipment-replacement economy with HVAC (water heater ≈ furnace/AC as the signature replacement product, with lifespan-based outreach), shares the emergency-call emphasis with locksmith, and carries the same membership/plan machinery the HVAC pass found most heavily promoted.
3. **vs Fire Protection Service Management / Elevator Service Management** — those siblings carry a structurally distinct trade object (code-mandated recurring inspection program, persistent deficiencies, compliance reporting). Plumbing shows no such loop in any fetched source; its recurring work is sold, not mandated.
4. **vs Water Treatment Business Management (§29 sibling leaf)** — water treatment (softeners, filtration) is a separate ServiceTitan trade page and appears inside plumbing plan work as "filter changes" (Workiz); the trades bundle commercially (plumbing companies often sell water treatment) but the directory keeps separate leaves. Same platform, sibling trade pages.
5. **vs Septic Service Management (§29 sibling leaf)** — septic appears as a separate ServiceTitan trade page; adjacent trade on the same platforms, separate leaf.
6. **vs Appliance Repair Management** — appliance repair's distinguishing object is the customer's appliance as the unit of repair; plumbing's unit of work is the building's fixed water systems and fixtures. The water heater sits near the boundary (fixed installation, appliance-like replacement economics) — the replacement-sale machinery is shared, the work content differs.
7. **vs CMMS / Enterprise Asset Management (§16)** — CMMS/EAM manages assets owned by the software's operator; any plumbing equipment records are a registry of *customer-owned* equipment maintained for service purposes. Different ownership side, different money flow.
8. **vs Construction Project Management (§17)** — commercial and installation work (repipes, new-construction plumbing, multi-day installs) drifts toward project machinery (phases, milestone billing, WIP, takeoff); the service-management center remains the dispatched service loop. Drift, not identity.
9. **vs Utility Field Service Management (§19)** — utility-side dispatch against network assets owned by the operator vs contractor-side business management serving customers.
10. **vs Appointment Scheduling Application** — booking is one fragment (online booking exists in several products); this Type is the whole business operation.
11. **vs Local Service Marketplace / Home Services Marketplace** — demand-side discovery/booking vs operator-side execution and billing; a marketplace lead (Angi/Thumbtack integrations in-sample) becomes a job here.
12. **vs Property Maintenance Management (§17)** — property managers coordinate maintenance across portfolios; this Type is the contractor's own business system — a property manager is a customer here.

## Uncertainties

1. **Backflow-prevention testing** — a real code-mandated annual-testing practice in many water jurisdictions, and a plausible candidate for a compliance-shaped software object (test records, reports to water authorities). No fetched source documents any such object; the sampled vendors' plumbing pages are silent. Not claimed in either direction; flagged for any future pass touching water-side trades.
2. **Drain cleaning / hydro-jetting / camera inspection tooling** — suspected as distinctive plumbing service content and possibly specialized tooling; not observed as software structure in any fetched source; not claimed.
3. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US payment/surcharge mechanics, US plan-selling culture). Regional variance could not be verified; the canonical document avoids region-specific claims.
4. **Jobber, Simpro, ServiceTrade, Successware** — major players serving plumbing companies; unreachable (403/WAF, this and prior passes). Market-coverage gap acknowledged; assertions calibrated to the six researched products.
5. **ServiceTitan data articles** — the water-heater seasonality and lifespan figures are the vendor's own aggregated platform data (explicitly "not nationally representative"); used here as evidence of how the vendor's product supports equipment-age outreach and seasonal planning, not as trade-universal statistics.
6. **Equipment registry depth in plumbing** — Workiz (per the HVAC pass's equipment-tracking observation) carries the fullest equipment model; the plumbing pages fetched this pass reference "customer and equipment history" (ServiceTitan) and work order histories (FieldEdge) but none documents a plumbing-specific per-unit registry (water heater serial/warranty records) at the depth the HVAC pass observed. Held as variant/optional with lower confidence than in HVAC.

## Final Synthesis

Plumbing Business Management is the business-management system of a plumbing service and installation company: it records customers and their service locations, carries each requested piece of plumbing work as a durable job with a lifecycle, coordinates the plumbers who perform the work in the field, and turns completed work into invoices and payments. The defining core is the field-service spine with plumbing work as the job's content. The trade's own color is a replacement-and-emergency economy: water heaters and fixtures replaced as product sales quoted with good-better-best proposals, flat-rate price books, commission-incentivized technicians, and consumer financing, on a winter-peaking replacement cycle that vendors help contractors plan around; emergency calls and 24/7 call capture as a first-class demand pattern; and recurring maintenance sold as memberships and service agreements whose covered visits include tank cleanings, filter changes, and inspections. At the commercial pole, service agreements, job costing, and client portals appear; at the construction pole, project machinery and takeoff tooling. Everything else commonly associated with these products (dispatch boards, mobile apps, notifications, purchase orders, reporting, GPS, AI) is standard or optional capability layered on a shared structure that vendors themselves ship as one platform configured per trade — and that at least one major vendor serves with no trade layer at all. The leaf is best understood as the plumbing trade instantiation of the field-service-management family — a distinct directory leaf by trade semantics, with a probable trade-Variant relationship to Small Business Field Service Management that should be ratified in joint review.
