# Research Notes — HVAC Service Management

Research date: 2026-09-08
Leaf: HVAC Service Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster)
Slug: hvac-service-management

## Research Goal

Understand what "HVAC Service Management" software actually is in the real market: what objects it manages, how HVAC work flows through it, what is HVAC-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings, fire protection/elevator with their compliance loops, CMMS/EAM, building-side systems, construction project management, utility field service).

Family context carried into this pass: the fire-protection-service-management pass found a structurally distinct trade object (code-mandated recurring inspection program + persistent deficiencies + outward compliance reporting) and predicted that electrical/HVAC/plumbing differences would be "configuration/content tuning over the generic FSM spine". The electrical, garage-door, and handyman passes all confirmed the two-pole family structure from their sides. The open question for HVAC: does HVAC carry a structurally distinct trade object (installed-equipment registries, maintenance-agreement machinery, refrigerant/compliance loops, seasonal scheduling structures), or is it a trade-tuned variant like electrical/garage-door/handyman?

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of an HVAC (heating, ventilation, air conditioning) service and installation company — residential service/replacement, light commercial, and commercial mechanical service.
- Core objects likely: customer + service location, job/work order with lifecycle, estimate/proposal, schedule/dispatch, technician, equipment record, invoice/payment, price book, maintenance agreements.
- Trade-specific candidates to test: installed-equipment records (serial/model/warranty/install date), membership/service agreements (annual tune-up plans), flat-rate price books, replacement sales machinery (good-better-best, financing), seasonal demand patterns, refrigeration/commercial-kitchen adjacency, refrigerant-regulation structures, load-calculation/design tools.
- Closest neighbors: Small Business Field Service Management (likely the same structural spine), trade siblings (plumbing/electrical/appliance repair/garage door), Fire Protection / Elevator Service Management (compliance-loop siblings), CMMS/EAM (asset-ownership line), Building Management System / Building Asset Management (§17 building-side views of the same equipment), Construction Project Management (installation projects), Utility Field Service Management (different operator).

## Research Questions

1. What objects make up the system (customer, location, job, estimate, appointment/visit, technician, equipment, agreement, invoice, payment, price book)?
2. How does HVAC work flow from inquiry to payment? What is the work mix (service call, repair, maintenance/tune-up, system replacement-install, commercial maintenance)?
3. What is HVAC-specific in the market: installed-equipment records with serial/warranty, membership plans/service agreements, flat-rate pricing, replacement sales motions, seasonal patterns, extended warranties, refrigeration adjacency?
4. Does HVAC carry any code-mandated, compliance-shaped program object (fire-protection style), or is recurring maintenance voluntary/commercial?
5. How do the residential, light-commercial, and commercial poles differ in the products?
6. Which interfaces do users actually operate (office dashboard, dispatch board, job detail, mobile app, customer-facing surfaces)?
7. Historical check: would older, regional, trade-agnostic, or paper-era operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| ServiceTitan | flagship "software for the trades"; HVAC is a headline trade; residential + commercial + construction poles over one platform | Tier 2 (HVAC industry page + FAQ) |
| FieldEdge | HVAC-heritage mid-market product ("We created FieldEdge, an HVAC software"); multi-truck SMB/mid-market positioning | Tier 2 (homepage + HVAC page) |
| Workiz | SMB home-services platform, AI-forward; HVAC first-listed industry of ~50 | Tier 2 (homepage + HVAC page + equipment-tracking feature page + FAQ) |
| Housecall Pro | micro-SMB residential home services; help center documents a dedicated HVAC industry package | Tier 1 (help center: collection map + HVAC Package Overview) |
| Kickserv | micro-SMB; simple, low-cost, trade-agnostic service business management | Tier 1 (knowledge center: Jobs article) |

Attempted-and-abandoned per source-access rules (from this and prior sibling passes): Jobber (403 ×2 in electrical pass, not retried), Service Fusion (used by garage-door pass; same-suite clone-page pattern already captured there), Simpro (403 ×2 in fire-protection pass), ServiceTrade (403 ×3 in fire-protection pass), Successware (WAF-rejected in garage-door pass).

## Sources

Fetched 2026-09-08:

- ServiceTitan (Tier 2): https://www.servicetitan.com/industries/hvac-software — HVAC industry page incl. FAQ
- FieldEdge (Tier 2): https://fieldedge.com/ — homepage; https://fieldedge.com/hvac-software/ — HVAC page incl. FAQ
- Workiz (Tier 2): https://www.workiz.com/ — homepage; https://www.workiz.com/industries/hvac/ — HVAC industry page incl. FAQ; https://www.workiz.com/features/equipment-tracking/ — equipment-tracking feature page incl. FAQ
- Housecall Pro (Tier 1): https://help.housecallpro.com/en/ — help-center collection map; https://help.housecallpro.com/en/collections/19689640-industry-packages — Industry Packages collection; https://help.housecallpro.com/en/articles/15935808-hvac-package-overview — HVAC Package Overview
- Kickserv (Tier 1): https://kickserv.helpscoutdocs.com/article/32-jobs — "Jobs" article (Kickserv Knowledge Center)

Family counterparty sources (prior sibling passes, same date range): research/electrical-service-management.md, research/garage-door-service-management.md, research/handyman-business-management.md, research/fire-protection-service-management.md, research/appliance-repair-management.md.

## Product A — ServiceTitan

### Key observations (evidence layer A unless noted)

- HVAC is the headline trade in the residential nav ("HVAC Software"), one of ~20 trade pages over one platform — same one-platform-many-trades packaging pattern the electrical and garage-door passes observed. [Layer B support: Workiz, FieldEdge, Housecall Pro show the same pattern.]
- Residential pole, trade-labeled: Marketing ("keep your phone ringing"), Call Booking/Scheduling, Estimates ("Increase average tickets for residential HVAC jobs"), Customer Experience (GPS technician tracking, SMS notifications, financing options, customer payment portal), Dispatching, Mobile App ("Empower field techs with a user-friendly mobile app"), Invoicing, Accounting ("Streamline bookkeeping with HVAC accounting software").
- Commercial pole, trade-labeled: Proposals ("Easily build multi-option proposals to win more jobs"), Job Costing ("Ensure profitability on every commercial HVAC job"), CRM, Reporting, **Service Agreement ("Automate your commercial HVAC service agreements")**, Pricing ("Grow your profit margins with HVAC pricing software"), Client Portal.
- Construction pole (installation work): Project Management, Billing ("Bill customers at every phase"), Crew Management, Inventory, Estimating, Dynamic Forms, WIP Reporting.
- Platform claim: "all-in-one, configurable platform streamlines daily operations like scheduling, dispatching, work order management, and billing"; mobile app "keeps technicians connected with real-time data access".
- FAQ definition: "HVAC service software streamlines operations for residential, construction, and commercial HVAC companies… With tools for job scheduling, dispatching, invoicing, and customer management, it keeps operations organized" — entirely generic FSM vocabulary.
- FAQ: "Will I still need a separate HVAC sales software? You will not…" — estimates/proposals built from the field or office with direct pricebook connection; "Follow-Ups feature applies automation to ensure that staff tracks and follows up on unsold estimates to close more deals."
- Marketing claims (kept out of the canonical document): 17% average revenue growth, 6% close-rate increase, named HVAC customer stories.

No HVAC-specific structural object on the page; the trade layer is labeling + tuning (pricing, proposals, agreements) over the platform.

## Product B — FieldEdge

### Key observations (evidence layer A)

- HVAC-first self-positioning: homepage — "Trusted by SMB and Mid-Market Service Leaders in HVAC, Plumbing, and Electrical"; HVAC page — "The HVAC Software That Scales Multi-Truck Operations"; FAQ — "We created FieldEdge, an HVAC software, specifically to help service businesses, including HVAC companies." Heritage product (ESC/dESCO lineage preserved as a separate product line).
- Product map: FieldEdge Software (business management), FieldEdge Mobile, FieldEdge Payments, **FieldEdge Flat Rate** ("Drive consistency in your pricing to prevent revenue shortfalls. Price jobs accurately… Guide customers to make informed decisions on repairs and replacements"), **Proposal Pro** ("Create a high-quality 'kitchen table' experience… Offer Good-Better-Best options to homeowners while on the job"), MarketingEdge ("Build a sales motion to upsell more service agreements"), Scheduling & Dispatching.
- HVAC page feature blocks: HVAC Dispatch Software ("Assign the right tech for the right job based on skills, location, and availability"; GPS tracking); QuickBooks sync; **Customer Management ("Access full service histories, equipment details, agreements, and billing info from anywhere")**; HVAC Invoicing (on-site completion, email, mobile payment); HVAC Mobile App ("Update work orders, capture photos, add notes, and make service recommendations from the field").
- Office-team framing: "Create a playbook to sell more service agreements and ensure better transitions between your Field and Sales teams."
- Marketing claims (kept out of canonical doc): "60% Less Spent on managing service agreements", "20+ Hours Saved per week", 40,000+ users, 40 years of experience.
- Multi-truck/multi-location/business-unit positioning; job-level profitability and tech-efficiency reporting; centralized dispatch board; standardized templates/forms/workflows.

Nothing structurally HVAC-specific beyond the emphasis: the named trade objects are equipment details and service agreements inside the customer record — both generic-in-kind objects carrying trade-specific weight.

## Product C — Workiz

### Key observations (evidence layer A)

- Homepage: "AI growth engine for home service businesses… Proud partner to home services in over 50 industries" with HVAC first in the industry list; growth-engine loop: Lead Capture (AI answering) → Book jobs → Dispatch → Sell ("Quote good-better-best on-site") → Collect payment (Workiz Pay) → Remarket.
- HVAC industry page, trade-tuned sections:
  - Sales proposals: "From the repair to the replacement, close bigger jobs by quoting Good - Better - Best options that fit any budget."
  - **Service plans**: "Get recurring revenue all year round. Pad slow months with predictable maintenance work for existing clients."
  - **Flat-rate pricing** (Pricebook Pro): "Empower techs to quote with confidence from the field with pre-made, client-ready pricebooks"; FAQ — materials and labor can be bundled and "display it as a single item in your pricebook… your client will simply see the flat rate item in the estimate and invoice."
  - **Equipment tracking**: "Remember every unit you ever installed or serviced — Track every piece of equipment, saving model numbers, serial numbers, installation dates, and service history. Your techs will arrive with the right parts."
  - Genius Marketing: "Past clients should keep your schedule packed during shoulder seasons. Easily send them targeted SMS and email marketing campaigns for seasonal promotions, and tune-ups." — seasonality explicit.
  - Multi-day projects: "Run complex HVAC projects without losing visibility. From non-consecutive multi-day scheduling, to section management, costs, materials, and milestone billing… big install jobs."
  - **Extended warranties** (JB Warranties integration): "Get paid three times for one HVAC job: on the initial install, for selling extended protection, and for the labor on future service calls."
  - Consumer financing: "Break down expensive HVAC work into low monthly payments… close more premium, high-efficiency system sales."
- Equipment-tracking feature page + FAQ — the fullest equipment model in the sample: record serial number, model, make, warranty information, installation dates, installation location, service history; label scanner pulls serial/model/make automatically; equipment assigned to a job also appears on the client's CRM profile; each piece of equipment is linked to a property address; history includes installations, services, and removals; third-party equipment (not installed by the team) can be manually added to client profiles; services logged per unit link to jobs; mobile app supports full functionality; used to "schedule maintenance", win "the big replacement" when "repairs stop making sense", and provide a paper trail in warranty disputes.
- Partner logos include HVAC equipment manufacturers (Carrier, American Standard, Trane, Bryant) and JB Warranties — the vendor ecosystem mirrors the trade's replacement economics.
- FAQ definition: "HVAC software is a comprehensive business management software solution designed specifically for HVAC contractors… including scheduling and dispatching, invoicing, customer management, extended warranties, and more"; beneficiaries include "Air conditioning and refrigeration companies."

## Product D — Housecall Pro

### Key observations (evidence layer A, Tier 1 — help center)

- Whole-product structure (generic): Company Dashboard, Customers, Customer Portal, Employees, Franchise, Fleet Management, Jobs/Invoices/Estimates (62 articles), Job Inbox, Leads, Pipeline, Price Book (23 articles), Scheduling, **Service Plans (22 articles)**, Payments (71 articles), Invoicing, Notifications, Reporting, Checklists, Purchase Orders, Payroll, Multi-Day Jobs Appointments, Voice, HCP Assist, App Store.
- Service Plans collection description: "Create, maintain, send, and cancel recurring service plans otherwise known as Maintenance Plans, Planned Maintenance Programs, Care Clubs and Membership Plans."
- **Industry Packages collection: HVAC, Electrical, and Plumbing only** (4 articles) — HVAC is one of only three trades with a dedicated package; garage door, handyman, appliance repair have none (the garage-door and handyman passes documented this absence from their sides).
- HVAC Package Overview article: "The HVAC Package is Housecall Pro built specifically for residential and light-commercial HVAC businesses. It comes preconfigured with the tools, workflows, and settings HVAC Pros use every day."
  - HVAC-exclusive tooling: **HVAC KPI Dashboard** ("revenue, jobs, team performance, and memberships at a glance"); **Purchase Orders** ("tied to a job's material line items… what gets ordered, from which supplier, and when"); **Credit-card surcharging with no added fees**; **Selling Membership Plans on Jobs and Estimates** ("Sell a membership plan right on any job or estimate with one signature and one payment, so you can grow recurring revenue from the field"); **Price Book Commissions** ("Set commissions on individual price book line items so your techs are paid accurately for what they sell"); **AI Pricing Insights** (MAX tier: "Live pricing benchmarks built right into your price book, based on real jobs across the Housecall Pro community"); Pipeline (MAX).
  - Also bundled: Sales Proposal Tool, Membership Plans, Photo Reports, Checklist Automations ("Auto-add checklists based on tags, job fields, or line items"), Job Splits, Automated Sales Tax, marketing dashboard, QuickBooks Online sync, and "all the standard tools in your plan, including scheduling, estimates, invoicing, payments, online booking, and reporting."
  - Related article: "Service Plan Template for HVAC" — an HVAC-specific service-plan template exists in the help center.
- The HVAC package's exclusive layer is entirely sales/recurring-revenue machinery (memberships, proposals, commissions, pricing insights, KPIs) plus purchasing — no new core object is introduced; membership plans themselves are a generic Service Plans capability.

## Product E — Kickserv

### Key observations (evidence layer A, Tier 1)

- "Jobs are the heart of the Kickserv workflow. Jobs are what your technicians are completing out in the field and the main way you'll keep track of business activity."
- Jobs board: left-to-right workflow Unscheduled → In Progress → Completed, with optional On Hold column ("Jobs can skip the On Hold column").
- Job creation: service type, internal job description ("will not be seen by the customer"), external scope of work ("will be seen by the customer"), contact from customer records; custom data fields (Standard plans and above).
- Conversion path: "Many Jobs start out as an Opportunity that turns into an estimate. Once the estimate is approved by the customer, the Opportunity transforms into an unscheduled Job!"
- Scheduling: inside the job, "Schedule work" → date/time, description for technicians, task type, assign tech (or unassigned) → "Add Event" — a work event is a child of the job.
- Start/Stop Job buttons move the job to In Progress; Mark Complete pops a confirmation to mark all work events complete; multi-visit guidance: "Depending on your industry, you might need to schedule several work events on a single job… keep the job open until all work events are completed, then send a final invoice."
- Job filters: service type, status, tag, assigned technician, time.
- Recurring Jobs: "Repeat this job" → frequency, day/date, end condition → repeating jobs added to the schedule.
- Workflow ends "send an invoice… and get paid."
- Trade-agnostic: nothing HVAC-specific anywhere; HVAC companies are among the trades served. This product anchors the pole where the trade layer is pure configuration.

## Cross-product Comparison

| Structure / capability | ServiceTitan | FieldEdge | Workiz | Housecall Pro | Kickserv | Assessment |
|---|---|---|---|---|---|---|
| Customer record with service location | ✓ (CRM) | ✓ (customer management) | ✓ (CRM; equipment linked to property address) | ✓ (Customers) | ✓ (Customers & Contacts) | Universal — core |
| Job / work order with lifecycle | ✓ (work order management) | ✓ (work orders) | ✓ (jobs) | ✓ (Jobs, 62-article collection) | ✓ ("heart of the workflow") | Universal — core |
| Office→field technician coordination (dispatch) | ✓ (Dispatch; skill-match in Pro per prior pass) | ✓ (dispatch board; skills/location/availability) | ✓ (drag-and-drop dispatch) | ✓ (Employees, scheduling) | ✓ (assign tech; work events) | Universal — core |
| Estimate/proposal → approval → job | ✓ (multi-option proposals; Follow-Ups on unsold estimates) | ✓ (Proposal Pro, good-better-best) | ✓ (good-better-best sales proposals) | ✓ (Sales Proposal Tool) | ✓ (Opportunity→estimate→Job) | Universal — standard |
| Invoice + payment on completed work | ✓ (Invoicing, Payments) | ✓ (FieldEdge Payments) | ✓ (Workiz Pay) | ✓ (HCP Payments, 71 articles) | ✓ (invoices) | Universal — core |
| Technician mobile app | ✓ (Mobile App) | ✓ (HVAC Mobile App: photos, notes, recommendations, payments) | ✓ (full mobile app) | ✓ (mobile-only features) | ✓ (mobile app collection) | Universal — standard |
| Price book / line-item pricing | ✓ (HVAC pricing software; Pricebook Pro per prior pass) | ✓ (FieldEdge Flat Rate) | ✓ (Pricebook Pro; flat-rate bundling) | ✓ (Price Book, 23 articles; commissions) | ✓ (service types) | Universal — standard |
| Maintenance plans / service agreements | ✓ (Service Agreement feature; "Automate your commercial HVAC service agreements") | ✓ (agreements in customer record; office playbook to "sell more service agreements"; MarketingEdge upsell) | ✓ (Service plans: "recurring revenue all year round") | ✓ (Service Plans, 22 articles; HVAC package: selling plans on jobs/estimates + memberships on KPI dashboard + HVAC plan template) | ✓ (Recurring Jobs only — weaker form) | Universal in trade-oriented products; the trade's signature recurring machinery |
| Installed-equipment records | ✓ (equipment scanning per commercial Dock & Door page — prior pass) | ✓ ("equipment details" in customer record) | ✓ (full model: serial/model/make/warranty/install date+location/history/removals; label scan; third-party equipment) | — (not in HVAC package feature list; Property Profile collection exists, content not fetched) | — | Common-to-optional; strongest in trade-dedicated/mid-market products |
| Good-better-best replacement sales motion | ✓ (multi-option proposals) | ✓ (Proposal Pro) | ✓ (sales proposals) | ✓ (Sales Proposal Tool bundled in HVAC package) | — | Common — trade-typical sales motion |
| Flat-rate pricing presentation | ✓ (Pricing; Pricebook Pro per prior pass) | ✓ (FieldEdge Flat Rate product) | ✓ (flat-rate bundling in pricebook) | ✓ (Price Book Commissions; AI Pricing Insights) | — | Common in trade-oriented products |
| Seasonal marketing | — | ✓ (MarketingEdge; email/text) | ✓ (explicit: shoulder seasons, seasonal promotions, tune-ups) | ✓ (Marketing Center, 45 articles) | — | Common; explicit seasonal framing at Workiz |
| Purchase orders / parts inventory | ✓ (Purchasing & Inventory) | ✓ (inventory management in FAQ) | ✓ (inventory management; low-stock alerts) | ✓ (Purchase Orders in HVAC package) | — | Common |
| Multi-visit / multi-day work | ✓ (job types and phases per prior pass; construction pole) | ✓ (multi-phase projects claim) | ✓ (Multi-day projects: non-consecutive scheduling, sections, milestone billing) | ✓ (Multi-Day Jobs Appointments) | ✓ (several work events per job) | Universal — standard |
| Extended-warranty machinery | — | — | ✓ (JB Warranties: install + protection sale + labor) | — | — | Optional; integration-level |
| Consumer financing | ✓ (Integrated Financing) | — | ✓ (Sunbit/Wisetack) | ✓ (financing per prior passes) | — | Common/optional |
| Project machinery (phases, costs, WIP) | ✓ (construction pole: Project Management, WIP) | ✓ (multi-phase projects) | ✓ (multi-day projects w/ costs, sections, milestone billing) | — (light) | — | Optional; commercial/install pole |
| Refrigeration adjacency | separate Refrigeration + Kitchen Equipment trade pages | — | FAQ: "Air conditioning and refrigeration companies" | — | — | Adjacent trades served by the same platforms |
| Accounting sync | ✓ (QuickBooks; ERPs) | ✓ (QuickBooks automated sync) | ✓ (QuickBooks Online/Desktop) | ✓ (QuickBooks Online/Desktop) | ✓ (QuickBooks 2-way) | Universal — standard |
| Reporting / dashboards | ✓ (Reporting) | ✓ (job-level profitability, tech efficiency) | ✓ (reporting; KPI claims) | ✓ (Reporting; HVAC KPI Dashboard) | ✓ (Reports) | Universal — standard |
| HVAC trade packaging | HVAC trade page (residential/commercial/construction) | HVAC-first product + HVAC page | HVAC industry page over ~50-industry platform | HVAC industry package (1 of 3) | none (trade-agnostic) | The Type's packaging pattern |
| AI assistants / answering | ✓ (AI Virtual Agent per prior pass; Atlas) | — | ✓ (Genius Answering/Scheduling/Marketing) | ✓ (HCP Assist) | — | Optional; era-typical |

### What is actually HVAC-specific (across sample)

1. **Trade-tuned packaging and configuration** — every multi-trade vendor sells "HVAC" as a labeled trade page, solution page, or (at Housecall Pro) a dedicated preconfigured package; Kickserv demonstrates the trade running on a fully trade-agnostic product. [Layer A ×5 vendors]
2. **The work mix: service calls, repairs, tune-ups, and system replacement-installation** — replacement jobs are a product sale plus an installation ("from the repair to the replacement", "close more premium, high-efficiency system sales"), quoted with good-better-best options and commonly financed; installations can run as multi-day projects with milestone billing. [Layer A ×4 vendors]
3. **Maintenance memberships/service agreements as the trade's recurring-revenue engine** — plan-selling in the field (one signature/one payment on a job or estimate), membership counts on KPI dashboards, office playbooks to sell agreements, plan templates for HVAC, seasonal framing ("pad slow months", tune-up visits in shoulder seasons). [Layer A ×4 vendors; the machinery is generic (recurring plans/agreements) but its promotional weight is distinctively HVAC]
4. **Installed-equipment records with per-unit identity and history** — serial/model/make, warranty information, installation date and location, per-unit service history including removals; label-scanning capture; third-party equipment registration; replacement-timing and warranty-dispute uses. [Layer A: full model at Workiz; named at FieldEdge; commercial pole at ServiceTitan; absent from Housecall Pro's HVAC package feature list — depth varies by product]
5. **Flat-rate pricing culture and technician-sell compensation** — flat-rate price books bundling parts+labor into client-ready single-price items; per-line-item commissions so "techs are paid accurately for what they sell". [Layer A ×3–4 vendors]
6. **Seasonality as a managed pattern** — heating/cooling shoulder seasons drive marketing campaigns and plan-selling; not a structural object, a calendar/marketing pattern. [Layer A ×2 vendors explicit]

No sampled product showed a *structurally distinct* HVAC object of the fire-protection kind: there is no code-mandated inspection program, no regulator-facing deficiency pipeline, no compliance-reporting object in any fetched source. HVAC maintenance is voluntary and commercial (sold as memberships/agreements), not mandated. Refrigerant-handling regulation was not observed as any software structure. The trade difference is configuration, content, and business-model emphasis — not a different data model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **Customer with a service location** — work is performed at the customer's premises (home, building, facility), so jobs bind to addresses; the customer may be a person, a business, or a property hierarchy.
2. **HVAC job (work order)** — a requested piece of HVAC work (service call, repair, maintenance/tune-up visit, or equipment replacement-installation) at that location, carried through a managed lifecycle (requested → scheduled → assigned → performed → completed → billed).
3. **HVAC technician as the executing role** — jobs are assigned to field technicians and coordinated by the office (scheduling/dispatch).
4. **Billing of completed work** — the job produces an invoice that collects payment (estimate/proposal upstream of larger work).

Remove the customer/location → generic task tracking. Remove the job lifecycle → an address book or invoicing tool. Remove technician coordination → pure invoicing. Remove billing → a dispatch board only. Remove "HVAC work" as the job's content → the generic Small Business Field Service Management Type.

Historical check: a paper-era heating-and-air shop (job tickets, a dispatch board, a price list, membership card files for annual tune-ups, invoices) satisfies all four properties; 1990s–2000s dedicated field-service products satisfy them; trade-agnostic products configured by an HVAC company satisfy them (Kickserv demonstrates this pole directly, Workiz/Housecall Pro serve HVAC from multi-trade platforms). None of the modern machinery (mobile apps, GPS, memberships, equipment registries, flat-rate books, AI) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Estimates/proposals with line items — commonly good-better-best options for system replacement — customer approval, conversion into jobs, and follow-up automation on unsold estimates
- Scheduling calendar + dispatch board; assignment by skills, location, and availability in mature products; GPS-backed status views
- Technician mobile app: assigned jobs, customer/equipment history, photos, notes, service recommendations, signatures, on-site payment, invoice creation
- Price book of services, parts, and equipment; flat-rate presentation (parts+labor bundled as client-ready single prices) common in this trade; per-line-item technician commissions in some products
- Maintenance plans / service agreements: recurring tune-up visits on a billing cadence, sold at the kitchen table or in the field; membership counts surfaced in reporting
- Customer notifications: booking confirmations, day-of reminders, on-my-way alerts, invoice delivery
- Multi-visit jobs (diagnose-then-return) and multi-day installation jobs (non-consecutive scheduling, milestone billing)
- Purchase orders tied to job materials; parts inventory
- Reporting: jobs, revenue, technician performance, membership counts, job profitability
- Accounting sync (QuickBooks in the North American SMB market)
- Seasonal marketing campaigns over the customer base (tune-up promotions in shoulder seasons)

### Level 2 — Variant / Optional Structure

- Installed-equipment registry depth: per-unit records with serial/model/make, warranty, installation date/location, full service history, removals, third-party equipment — common in trade-dedicated and mid-market products, thinner elsewhere
- Extended-warranty integrations (install + protection sale + labor economics); equipment-manufacturer partner ecosystems
- Consumer financing for high-ticket system replacement
- Commercial pole: preventive-maintenance agreements, client portals, equipment scanning, project machinery (phases, costs, WIP), job costing
- Construction/install pole convergence (project management, phase billing)
- Refrigeration and commercial-kitchen-equipment service as adjacent trades on the same platforms
- Segment packaging: HVAC-dedicated editions/packages vs trade pages vs trade-agnostic configuration
- AI answering/dispatch/assistant features (era-typical); GPS fleet tracking; payroll; review/reputation machinery

### Level 3 — Vendor-specific (kept out of the canonical document)

- Housecall Pro: HVAC KPI Dashboard, no-fee credit-card surcharging, AI Pricing Insights, Property Profile collection (content not fetched), HCP Assist, plan-tier gating (Basic/Essentials/MAX)
- Workiz: Genius suite (Answering/Scheduling/Marketing/Phone), JB Warranties integration ("paid three times"), label scanner, Linxup GPS, Pricebook Pro, Workiz Pay
- FieldEdge: ESC/dESCO heritage product line, FieldEdge Flat Rate product, Proposal Pro "kitchen table experience", MarketingEdge, 40-years/40,000-user claims
- ServiceTitan: Pro product tiers (Pricebook/Dispatch/Fleet Pro…), Atlas, Convex prospecting, Follow-Ups feature, skill-match dispatch, HVAC growth claims (17%/6%)
- Kickserv: "Opportunity" object naming for the pre-estimate stage

## Vendor-specific Findings

See Level 3. Notable patterns: Housecall Pro ships a genuinely *preconfigured* HVAC package (the deepest trade layer in the sample, still made entirely of generic-in-kind capabilities); FieldEdge is the sample's only HVAC-heritage product (trade-first company positioning); ServiceTitan splits the trade into residential/commercial/construction marketing poles over one platform; Workiz's ecosystem (manufacturer partners, warranty integrations) mirrors the trade's equipment-replacement economics. Extended-warranty machinery appears at only one vendor — held optional/integration-level.

## Rejected Findings

1. **Code-mandated inspection/deficiency loop (fire-protection style)** — no evidence anywhere in the sample; HVAC recurring maintenance is voluntary and commercial. Rejected as canonical; confirms the fire-protection pass's prediction that HVAC sits in the trade-tuned pole.
2. **Refrigerant-regulation structures as software objects** — the trade is regulated (technician certification and refrigerant handling are real), but no fetched source documents any refrigerant record/compliance object in these products. Not claimed.
3. **Load-calculation / design tools (Manual-J-class) as part of this Type** — suspected as a separate design-tool market adjacent to replacement sales; absent from all fetched pages. Not claimed; recorded as an uncertainty.
4. **Seasonality as a structural object** — real and explicitly marketed (shoulder seasons, tune-up promotions) but implemented as marketing campaigns and recurring plans, not a distinct data structure. Held at Level 1/2, not definitional.
5. **"HVAC + plumbing + electrical" as one mechanical-industrial Type** — vendors serve all three from one platform with separate trade packaging; the directory treats them as sibling leaves by trade semantics. One trade, one leaf; no merger proposed.

## Boundary Findings

1. **vs Small Business Field Service Management** — the structural spine is identical (customer+location → job lifecycle → technician coordination → invoice/payment; verified across five products). Vendors ship "HVAC" as a preconfigured trade layer of one product (ServiceTitan trade page; Workiz industry page; FieldEdge trade-first product; Housecall Pro preconfigured package), and Kickserv demonstrates the trade running with no trade layer at all. Probable trade-Variant relationship rather than two independent Types — now convergently observed by the electrical, cleaning, appliance-repair, garage-door, handyman, and HVAC passes. The durable difference is trade semantics: the membership/agreement revenue engine, installed-equipment records, flat-rate pricing culture, the replacement sales motion, and seasonality. Joint review with Small Business Field Service Management recommended.
2. **vs trade siblings (plumbing, electrical, garage door, appliance repair, locksmith)** — same family pattern; the trade wrapper differs, the spine does not. This pass discharges the fire-protection pass's family-structure question for the HVAC leaf from this side: HVAC belongs to the trade-tuned pole (electrical/garage-door/handyman pole), not the compliance pole (fire protection, likely elevator). The HVAC pass adds a family observation: the membership/plan machinery is most heavily promoted in this trade of all researched siblings, suggesting trade emphasis is a gradient even within the trade-tuned pole.
3. **vs Fire Protection Service Management / Elevator Service Management** — those siblings carry a structurally distinct trade object (code-mandated recurring inspection program, persistent deficiencies, compliance reporting). HVAC shows no such loop in any fetched source; its recurring work is sold, not mandated.
4. **vs Appliance Repair Management** — appliance repair's distinguishing object is the customer's appliance as the unit of repair; HVAC's unit of work is the building's fixed comfort systems, installed and tracked as per-location equipment records with installation/warranty history. The equipment registry is stronger here than in the appliance pass.
5. **vs CMMS / Enterprise Asset Management (§16)** — CMMS/EAM manages assets owned by the software's operator; the HVAC equipment record is a registry of *customer-owned* equipment maintained for service purposes. Different ownership side, different money flow.
6. **vs Building Management System / Building Energy Management (§17)** — BMS/BEM operate and measure the building's own plant in real time; this Type runs the contractor's business that services that plant. A BMS contractor is a customer here. The equipment record is a service ledger, not a control point.
7. **vs Building Asset Management (§17)** — the building owner's portfolio view of installed assets vs the contractor's job-centric service view of customer equipment.
8. **vs Construction Project Management (§17)** — commercial and installation work (system change-outs, multi-day installs) drifts toward project machinery (phases, milestone billing, WIP); the service-management center remains the dispatched service loop. Drift, not identity.
9. **vs Utility Field Service Management (§19)** — utility-side dispatch against network assets owned by the operator vs contractor-side business management serving customers.
10. **vs Appointment Scheduling Application** — booking is one fragment (online booking exists in several products); this Type is the whole business operation.
11. **vs Local Service Marketplace / Home Services Marketplace** — demand-side discovery/booking vs operator-side execution and billing; a marketplace lead becomes a job here.
12. **vs Property Maintenance Management (§17)** — property managers coordinate maintenance across portfolios; this Type is the contractor's own business system — a property manager is a customer here.

## Uncertainties

1. **Load-calculation/design tooling** (Manual J/S/D-class residential design software) — strongly suspected as a separate adjacent market feeding replacement sales; not observed in any fetched source; not claimed.
2. **Refrigerant compliance tracking** — suspected in the commercial refrigeration segment; not observed; not claimed.
3. **FieldEdge operational depth** — only marketing/FAQ pages fetched; the vendor's Salesforce-hosted support portal was not entered; FieldEdge claims limited to what its site states.
4. **Housecall Pro Property Profile collection** — exists (1 article) but was not fetched; its content (property-scoped records?) is unknown and unclaimed.
5. **Jobber, Service Fusion, Simpro, ServiceTrade** — major players serving HVAC companies; unreachable (403/WAF, this and prior passes). Market-coverage gap acknowledged; assertions calibrated to the five researched products.
6. **Regional markets** — the sample is North America–dominant (QuickBooks-centrism, US payment/surcharge mechanics, US plan-selling culture). Regional variance could not be verified; the canonical document avoids region-specific claims.

## Final Synthesis

HVAC Service Management is the business-management system of an HVAC service and installation company: it records customers and their service locations, carries each requested piece of HVAC work as a durable job with a lifecycle, coordinates the technicians who perform the work in the field, and turns completed work into invoices and payments. The defining core is the field-service spine with HVAC work as the job's content. The trade's own color is the equipment-and-membership economy: installed comfort systems tracked as per-unit equipment records with service and warranty history; recurring maintenance sold as memberships and service agreements whose tune-up visits follow the heating and cooling seasons; replacement jobs sold at the kitchen table with good-better-best proposals, flat-rate price books, commission-incentivized technicians, and consumer financing; and, at the commercial pole, preventive-maintenance agreements and multi-day installation projects. Everything else commonly associated with these products (dispatch boards, mobile apps, notifications, purchase orders, reporting, GPS, AI) is standard or optional capability layered on a shared structure that vendors themselves ship as one platform configured per trade — and that at least one major vendor serves with no trade layer at all. The leaf is best understood as the HVAC trade instantiation of the field-service-management family — a distinct directory leaf by trade semantics, with a probable trade-Variant relationship to Small Business Field Service Management that should be ratified in joint review.
