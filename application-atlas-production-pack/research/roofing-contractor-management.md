# Research Notes — Roofing Contractor Management

## Research Goal

Understand what a Roofing Contractor Management application actually is, from real products: what objects exist inside it, what users do with them, how a roofing job flows from first contact to final payment, which structures are roofing-specific rather than generic field-service machinery, and where the Type's boundaries sit against the already-processed §29 trade-business siblings (Small Business Field Service Management, Home Improvement Contractor Management, Flooring Contractor Management, Restoration Contractor Management, Plumbing/HVAC/Electrical, etc.).

## Initial Boundary

Hypothesis before research: roofing sits at the intersection of several already-processed neighbors —

- the **field-service family spine** (customer + service location → job lifecycle → field role coordination → billing) shared by plumbing/HVAC/electrical/garage-door/handyman (all processed as trade-tuned variants of Small Business Field Service Management);
- the **sale-driven project shape** of Home Improvement Contractor Management (lead → estimate/proposal → recorded sale → production → payment schedule);
- the **measured-area quantity basis** of Flooring Contractor Management (job content quantified from measurements);
- the **insurance-claim payment path** of Restoration Contractor Management (storm/hail damage work paid through carrier review).

Open question: is roofing a trade-tuned FSM variant (like plumbing), or does it carry structurally distinct objects (like flooring's measured-area basis, restoration's loss-driven job, fire-protection's compliance loop)?

## Research Questions

1. What is the unit of record — job, project, lead? What lifecycle does it carry?
2. Is the primary surface a dispatch board (service shape) or a sales pipeline (sale shape)?
3. How do measurements enter the system, and what do they drive?
4. How do materials get ordered, and is the order bound to the job?
5. Who executes the work — in-house crews, subcontractors — and how is execution documented?
6. How does money resolve — retail sale, financing, insurance claim? What role do supplements/depreciation play?
7. What is storm/catastrophe machinery (hail mapping, canvassing) and is it definitional?
8. Do generic FSM vendors serve roofing with or without trade-specific structure?
9. Historical check: would a paper-era roofing contractor's system satisfy the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier | Evidence reached |
|---|---|---|---|
| **AccuLynx** | roofing-dedicated, production-first all-in-one | mid-market/large; "residential insurance restoration and retail roofing" | Tier 2 (official site + production feature page); knowledge base unreachable |
| **Roofr** | roofing-dedicated, measurement/estimate-first, free-tier entry | SMB | Tier 1 (help center, multiple articles) + Tier 2 (official site) |
| **JobNimbus** | roofing-dedicated, CRM/sales-first with boards | SMB/mid-market | Tier 1 (help center, multiple pages); marketing site 403 |
| **ServiceTitan (Roofing)** | horizontal trades platform with a dedicated roofing configuration | enterprise/multi-location | Tier 2 (official roofing industry page) |

Rejected/considered: Jobber (roofing industry page exists per prior passes; site 403 on 2026-09-09, consistent with multiple prior passes — abandoned per retry rule), Housecall Pro roofing page (403), Sumo/Leap/CompanyCam (capability suppliers or unreachable; not sampled).

## Sources

All fetched 2026-09-09:

- AccuLynx — https://acculynx.com/ (root; FAQ, integrations, feature nav) — Tier 2
- AccuLynx — https://acculynx.com/features/roofing-production-management/ — Tier 2
- AccuLynx knowledge base — https://support.acculynx.com/hc/en-us — **unreachable** (transport error, then timeout; abandoned)
- Roofr — https://roofr.com/ (root; product suite, FAQs) — Tier 2
- Roofr Help Center — https://help.roofr.com/en/ (collection index) — Tier 1
- Roofr — https://help.roofr.com/en/collections/19667276-jobs-crm (Jobs & CRM collection) — Tier 1
- Roofr — https://help.roofr.com/en/articles/15533109-how-to-use-the-roofr-job-board — Tier 1
- Roofr — https://help.roofr.com/en/collections/19666554-measurement-reports (Measurement Reports collection) — Tier 1
- Roofr — https://help.roofr.com/en/articles/15649776-how-to-use-the-insurance-section-on-the-job-card — Tier 1
- Roofr — https://help.roofr.com/en/collections/19667281-catalog-ordering (Catalog & Ordering collection) — Tier 1
- JobNimbus Help Center — https://support.jobnimbus.com/ (root) — Tier 1
- JobNimbus — https://support.jobnimbus.com/jobs-contacts-and-boards — Tier 1
- JobNimbus — https://support.jobnimbus.com/financials — Tier 1
- JobNimbus — https://support.jobnimbus.com/how-do-integrated-suppliers-interact-with-material-orders — Tier 1
- JobNimbus — https://support.jobnimbus.com/how-do-i-create-a-work-order — Tier 1
- ServiceTitan — https://www.servicetitan.com/industries/roofing-software (roofing industry page incl. retail/insurance/integrations sections) — Tier 2
- Jobber — https://www.getjobber.com/industries/roofing-software/ — **403** (abandoned; consistent with prior passes)
- Housecall Pro — https://www.housecallpro.com/industries/roofing-software/ — **403** (abandoned)

## Product A — AccuLynx (roofing-dedicated, production-first)

### Key observations (Tier 2, official site)

- Self-positioning: "#1 roofing software"; "the all-in-one management platform that powers every aspect of a roofing business, connecting everyone—from the field to the office—in real time."
- FAQ: "AccuLynx software is designed for roofing companies that primarily focus on **residential insurance restoration and retail roofing**." Sizes: "from growing startups with as little as 3 users to multi-location operations with hundreds of users."
- Core feature pillars: **Sales/CRM** ("the roofing industry's CRM innovator… optimize your sales processes and help you get more contracts signed"), **Production** ("industry-leading project management tools streamline production from beginning to end"), **Finance**, **Business Management**.
- Sales/CRM: "AI-powered lead intelligence and real-time analytics"; "speed up estimation with **seamless measurement data and live material pricing**"; "custom sales proposals that you can present or share on the fly"; "state-of-the-art mobile roofing app."
- Production page (deeper):
  - **Digital job files** — "Manage every aspect of a project from the AccuLynx job file… estimates, contracts, documents, photos, measurements, and more—together, in one place."
  - **Messages & activity feed** — live activity feed; job message board with team tagging.
  - **Production calendar** — "all of the company's appointments, **deliveries**, and scheduled labor from a single production calendar" (deliveries are first-class calendar items).
  - **Labor manager** — "Organize **subcontractors and crews**… capture contact details, maintain up-to-date records, and control what job information is shared."
  - **Scheduling** — "Schedule crews for jobs… team members are automatically notified."
  - **Ordering** — "Build material orders quickly and place them directly to QXO, SRS, and ABC Supply without leaving AccuLynx. Use the **Order Manager** to stay on top of every order."
- Solutions: document automation, text messaging, customer portal, payments (AccuPay), **crew management (mobile crew app)**, financing (AccuFi), custom reporting, data mart, **private-equity/portfolio company solutions**.
- FAQ: "What is roofing project management software? … tools that help roofing contractors manage their projects, customers, and teams… move projects from the **initial lead to the final invoice**."
- Integrations FAQ: "material suppliers, **aerial measurements**, **canvassing and photo apps**, **hail mapping technology**, accounting software… Popular integrations include ABC Supply, SRS Distribution, QXO, EagleView, CompanyCam, and QuickBooks."
- Customization: "job milestones, checklists, automations & workflows, proposal templates."

## Product B — Roofr (roofing-dedicated, measurement/estimate-first, SMB)

### Key observations (Tier 1 help center + Tier 2 site)

- Product suite (site): **CRM** ("manage your entire sales process from end to end"), **Instant Estimates**, **Proposals**, **Measurements** ("accurate roof reports"), **Payments & Invoicing**, **Material Ordering** ("order materials and get supplier quotes in one place"), **Calendar**, **Roofr Sites** (AI-built website). Partners: ABC Supply, Goodleap (financing), CertainTeed (manufacturer), CompanyCam, QXO, SRS.
- **Job Board (Tier 1)**: "Your job board stages reflect your complete workflow from **initial lead to final payment**." Stage categories: customizable **New Incoming Leads** (lead qualification), **Qualified Leads** ("sales activities through proposal signing"), **Won Jobs** ("all post-sale activities (pre-production, production, completion, invoicing)"); **locked** categories: Completed Jobs, Lost Jobs, Unqualified Leads. "Stage categories impact dashboard metrics like **speed-to-lead and conversion rates**." Filters: assignees, stages, lead sources, time in stage. Settings: lead sources with job counts; job cards show customer name or address; default job folders; "**Adjust Job Costing to be accessible to Only managers or the entire team**."
- **Job Cards & Tasks (Tier 1)**: job card captures customer details, lead source data, notes, tasks, multiple assignees, tags, file manager, sequential Job IDs; **Insurance Section** (below).
- **Insurance Section on the Job Card (Tier 1)**: toggle reveals structured fields — insurance company name, **date of loss**, **deductible**, policy/account number, **type of damage**, claim notes, **claim number**, **claim amount**, plus adjuster/insurance-representative contact ("Add contact"). Rationale: "Remove the need to store insurance information in job notes… standardized format across all jobs."
- **Measurement Reports (Tier 1)**: collections for **Roofr Reports** (ordered; multi-building reports; measurements dashboard managing ordered + DIY reports; PDF vs dashboard view; edit a report by opening in DIY), **ESX Files** (order and download ESX — Xactimate-compatible format), **DIY Reports** ("draw and measure roof reports yourself"; from blueprint imagery; on mobile), **Pitchless Reports** (add pitch manually when slope data unavailable). Site: report contains "roof area, facets, pitch, eaves, valleys, and hips"; "material lists are part of your Roofr Reports."
- **Catalog & Ordering (Tier 1)**: **Catalog** ("item listings… setting up accurate pricing, configuring **area mapping**" — catalog items map to measurement areas; CSV upload; material purchase tax column); **Jumpstart** (curated item list with supplier prices); **Material Orders** ("create orders and send straight from Roofr"; from a proposal, or BETA from a template without a proposal); **Work Orders** ("convert your existing job information into a detailed work order to edit and manage your **scope of work**").
- **Instant Estimator (Tier 1)**: "Offer homeowners quotes in seconds and capture their information to qualify leads"; embeddable "in ads, on website, door knockers, social"; Google Reviews and CompanyCam showcase widgets on the results page.
- **AI Receptionist (Tier 1)**: "Answers every call 24/7. Screen your junk, give homeowners an instant estimate, book an appointment, and log the whole thing as a customer and job right in Roofr."
- Getting Paid collection: "Payments, invoicing and **job costing**." Communication & Performance collection exists. Team Roles & Permissions article. Change Orders article. Google Calendar sync.

## Product C — JobNimbus (roofing-dedicated, CRM/sales-first)

### Key observations (Tier 1 help center)

- Top-level structure: **Jobs, Contacts, and Boards** ("Create your customer base and define your job process"), Calendar and Tasks, **Financials**, Reports, Settings, Automations, Engage (texting), AssistAI, Marketing, Payments, QuickBooks, **Suppliers**, Integrations.
- **Jobs and Contacts**: create jobs and contacts; **turn a contact into a job and vice versa**; relate contacts; merge jobs/contacts; custom lead sources; notes; import.
- **Boards**: kanban boards; "move a job into another status using boards"; board filters; board components; mobile boards.
- **Documents & Photos**: upload/download; request signature on custom documents (multiple signature areas); photo conversation threads; take/upload/edit photos; scan documents; **company photo feed**.
- **Subcontractors as Contacts**: add a subcontractor as a contact; configure their notifications; **send a work order to a subcontractor**; deactivate inactive subs.
- **Financials**: Estimates (create; override total price; send for signing or sign in person; estimate statuses; multiple locations; custom financing options; mobile sales experience); Invoices; **Work Orders**; **Material Orders**; **Margin and Markup** (profit settings, margin slider); Products and Services (**separate materials from labor**; location-based products); Taxes; **Measurements** (fence measurements tool; **upload reports to Measurements**; **order measurement reports in-product**; "**which measurements will auto-populate in estimates**"; **measurement tokens and calculations**); **Profit Tracker** ("track my job costs"); Payments (collect/record; **job deposit**; overpayment); Credit Memos; **Financing** (JobNimbus Financing; Wisetack connection; "track financing and get paid").
- **Work Order creation (Tier 1, detailed)**: created from a Contact or Job page under a "Material & Work Orders" tab; Work Order Builder fills from an existing Estimate or manually; design templates; saved work orders; start/due/end dates → "the Work Order will appear on your Calendar"; Type and Status bound to configurable Work Order Workflows; **assign to a team member or to a Subcontractor**; line items from Products & Services; sections; **Special Instructions** ("visible to the recipient"); **Internal Note** ("only visible to your team"); save as template. Cross-sell note: "Do you work in multiple different trades? … Work Orders can help you keep your business organized."
- **Material Orders + integrated suppliers (Tier 1, detailed)**: order from integrated suppliers **SRS, QXO, ABC Supply**; supplier sends information back to the Job record when the Material Order reaches Completed status; per-supplier capability table — status updates (all three), **supplier invoice import** (SRS/QXO → imported as private document in Job Documents; ABC not supported), **proof-of-delivery photos** (SRS → PDF in Job Documents; QXO → individual photos; ABC → link in the Job Activity Feed). Material Order statuses: **Draft → Order Received → In Progress → Ready for Review → Fulfilled → Invoiced** (+ Cancelled), each mapped to supplier-side statuses (e.g., SRS "En Route"/"Arrived"; ABC "Pickup Scheduled"/"Delivered"/"Partial").
- **Suppliers section**: ABC Supply, QXO, SRS Distribution, Third-Party Suppliers.
- **Integrations list** (Tier 1): Angi (lead marketplace), ArcSite, BirdEye, CompanyCam, **EagleView**, Get The Referral, Global Payments, **HailTrace** (hail mapping), **Hover**, Leap, mySalesman, naturalForms, Podium, **RoofScope**, **SalesRabbit** (canvassing), Simplii, Solo, Spotio, SumoQuote, **Sunlight Financial** (financing), Toolsey, **Wisetack** (financing), **Xactimate**, Zapier.
- Settings: Workflows, Templates, Forms, Team, Groups. Automations: event-based, time-based, recipes.

## Product D — ServiceTitan Roofing (horizontal platform, dedicated roofing configuration)

### Key observations (Tier 2, official roofing industry page)

- Positioning: "Professional roofing software… ServiceTitan helps top roofing and **exterior** contractors scale profitably on one powerful end-to-end solution." Page structured as **Retail / Insurance / Integrations**.
- **Retail pole**: Marketing (reviews/referrals), **Sales Scheduling** ("booking the right sales rep for the right opportunity"), **Estimating** ("Good, Better, Best estimate templates and financing options to close more deals on the spot"), **Material Tracking** ("Automatically track and order materials across projects and sites for real-time insights and analysis on spend"), **Crew Scheduling** ("bulk scheduling and daily or weekly rescheduling"), **Project Management**, **Invoice** (AI invoice summaries; collections statuses), **Reporting**.
- **Insurance pole** ("Master Roofing Insurance Work"): "ServiceTitan simplifies roofing insurance claims by **integrating with Verisk's Xactimate to sync data**. Automate insurance sales, manage **supplements**, and reduce **adjuster delays**…"
  - Insurance Scheduling: "Let homeowners self-book… automated text reminders and live estimator tracking to be the first on the roof, ready to **document the damage and win the claim**."
  - **Insurance Sales Queue**: "Bridge the gap between the initial inspection, the adjuster, and the office. The Insurance Sales Queue organizes the estimation handoff from the moment damage is found."
  - Roof Estimating: "two-way **Xactimate sync** transfers line items and photos instantly to eliminate double entry. Use AI to summarize **carrier docs** and identify **scope gaps**."
  - Claim Estimate: "Centralize supplements, financials, and job costing… from the first inspection to the final **depreciation check**."
  - **Change Order Software**: "Master your roofing **supplements**. Use digital Change Orders to document scope gaps for faster **carrier approval**. Maximize **RCV**…"
  - Production Management: field mobile app; "crews can create tasks and update progress instantly."
  - Communication: "Sync your crew, office, and **adjusters** directly inside the claim."
  - Financial: "instant visibility into your total **uncollected depreciation** to prioritize closeouts and maximize project cash flow."
- **Integrations**: Measurements — "EagleView, **GAF QuickMeasure**, and Hover, generate fast and accurate measurements and calculations directly into ServiceTitan's estimating tools"; Suppliers — "direct access to industry leading roofing suppliers like **ABC Supply Co, QXO and SRS Distribution**"; Operations — "Verisk Xactimate, Zapier, CompanyCam, and iPermit"; Leads — "Google Local Services, Angi, Thumbtack"; Financing; Accounting — "QuickBooks, NetSuite, Sage…"
- Also: commercial roofing presence (commercial nav lists "Commercial Roofing"; commercial-roofing customer testimonials), Atlas AI assistant, Enterprise Hub (multi-location), Private Equity solutions.

## Cross-product Comparison

| Structure / capability | AccuLynx | Roofr | JobNimbus | ServiceTitan Roofing | Layer |
|---|---|---|---|---|---|
| Customer/contact + job at a property (job of record) | ✅ job files | ✅ job cards + Job IDs | ✅ jobs/contacts | ✅ jobs/projects | A×4 |
| Sales pipeline as primary surface (lead → won stages) | ✅ Sales/CRM pillar | ✅ Job Board w/ stage categories | ✅ Boards | ✅ sales scheduling + queues | A×4 |
| Inspection → estimate/proposal → signed contract | ✅ proposals, contracts | ✅ proposals + e-sign | ✅ estimates + signing | ✅ estimating + Good-Better-Best | A×4 |
| **Roof measurement as quantity basis** | ✅ "seamless measurement data"; EagleView int. | ✅ ordered/DIY/ESX reports; area mapping | ✅ Measurements section; order in-product; tokens auto-populate estimates; EagleView/Hover/RoofScope int. | ✅ EagleView/GAF QuickMeasure/Hover into estimating | A×4 |
| **Material orders bound to the job** | ✅ Ordering + Order Manager | ✅ Material Orders (from proposal/template) | ✅ Material Orders w/ supplier status sync | ✅ Material Tracking ("track and order materials") | A×4 |
| **Supplier-direct ordering to roofing distributors** | ✅ QXO/SRS/ABC | ✅ ABC/QXO/SRS partner integrations | ✅ SRS/QXO/ABC + status/invoice/POD sync | ✅ ABC/QXO/SRS partnerships | A×4 |
| **Work orders / crew execution** | ✅ labor manager, crew app, production calendar | ✅ Work Orders (scope of work) | ✅ Work Orders → team member or subcontractor | ✅ crew scheduling + production mobile app | A×4 |
| Deliveries as schedulable production items | ✅ production calendar | ✅ ("delivered on time" ordering copy) | ✅ material order statuses incl. delivery/POD | ✅ material tracking across sites | A×4 |
| Estimates → invoices → payments (deposits, online pay) | ✅ Finance pillar, AccuPay | ✅ Getting Paid collection | ✅ invoices, payments, deposits | ✅ invoice + payments | A×4 |
| Job costing / profit visibility | ✅ project cost tracking | ✅ job costing (role-gated) | ✅ Profit Tracker, margin/markup | ✅ job costing | A×4 |
| Financing options on proposals | ✅ AccuFi | ✅ Goodleap partner | ✅ JobNimbus Financing/Wisetack/Sunlight | ✅ integrated financing | A×4 |
| **Insurance-claim context on the job** | ✅ positioning "insurance restoration and retail"; hail mapping int. | ✅ structured insurance fields (claim #, adjuster, date of loss, deductible…) | ✅ Xactimate integration | ✅ full claim machinery (sales queue, supplements, depreciation, adjuster comms) | A×4 (depth varies) |
| Supplements / change orders for carrier approval | (not fetched at this depth) | ✅ change orders article | (via Xactimate workflow) | ✅ digital change orders, RCV | A×2–3 |
| Depreciation holdback tracking | — | — | — | ✅ uncollected depreciation | A×1 (product-specific depth) |
| Storm machinery: hail mapping, canvassing | ✅ hail mapping int. | (instant estimator for storm response implied) | ✅ HailTrace, SalesRabbit, Spotio | ✅ "first on the roof" scheduling | A×3 |
| Lead capture: instant estimates, AI receptionist, lead marketplaces | ✅ AI lead intelligence | ✅ Instant Estimator + AI Receptionist | ✅ custom lead sources + Angi int. | ✅ Google LSA/Angi/Thumbtack | A×4 |
| Customer portal | ✅ | (not observed) | (not observed) | ✅ (platform feature) | A×2 |
| Multi-trade / exteriors bundling | (roofing-focused) | (roofing-focused) | ✅ "multiple trades on one project" | ✅ "roofing and exterior contractors" | A×2 |
| Commercial roofing | (residential focus per FAQ) | (residential focus) | (not observed) | ✅ commercial pole | A×1 |
| Manufacturer warranty registration | not observed | not observed | not observed | not observed | — (uncertainty) |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

The roofing contractor's business system of record, whose defining core is **five jointly-held structures**:

1. **The roofing job of record** — a persistent identified job binding a customer to the property whose roof is worked on, carried from first contact (lead/inspection) through a sale-driven lifecycle (estimate/proposal → signed contract → production → completion → billing). Remove → a contact list with quotes, or generic task tracking.
2. **The measured roof as the quantity basis** — the job's material and price content is quantified from measurements of the roof itself (ordered aerial/satellite reports, self-drawn DIY measurements, or field measurement), and those quantities feed estimates and material lists. Remove → a generic FSM job whose content is typed in by hand (Small Business Field Service Management territory) or a bare estimating tool.
3. **Job-bound material procurement** — material orders are created from the job (commonly from the sold proposal or the measurement's material list), placed to suppliers — in the current market, directly to integrated roofing distributors — and their fulfillment/delivery is tracked against the job. Remove → labor-only scheduling, or purchasing disconnected from jobs.
4. **Crew-based production execution** — the sold job converts into work orders / crew schedules executed on site, with crews or subcontractors as the executing roles coordinated by the office, and execution documented against the job. Remove → a quoting/procurement system with no execution, or a dispatch board with no production shape.
5. **Money resolution against the job** — the completed job resolves into customer billing (deposits, invoices, payments, commonly financing) with job costing visible on the job; in claim work, payment commonly arrives through the carrier's review process. Remove → a schedule board with no economics.

Jointly-held is load-bearing:

- 1 alone = CRM/job list; 2 without 1 = measurement service (aerial-measurement vendor territory); 3 without 1 = supplier portal; 4 without 1 = crew scheduling tool; 5 without 1 = invoicing tool.
- 1+4+5 without 2+3 = generic field-service spine → Small Business Field Service Management.
- 1+2 without 3+4+5 = measurement/estimating tool → Quantity Takeoff / Construction Estimating territory.
- 2+3 without 1+4+5 = distributor/measurement pipeline with no job being run.
- 1+2+3 without 4+5 = quoting and procurement without execution.
- 1+3+4+5 without 2 = generic project purchasing with crews (the trade-agnostic pole).

### L1 — Common Mature Structure (standard capabilities; 4/4 or 3/4 observed)

- Sales pipeline board with customizable stages and locked outcome categories; speed-to-lead/conversion metrics.
- Inspection capture and estimate/proposal building from measurements + a material/service catalog; good-better-best presentation; e-signature; proposal-to-job conversion.
- Material/service catalog with pricing (commonly supplier-priced), area mapping to measurements, measurement-driven line-item auto-population.
- Production calendar holding appointments, material deliveries, and labor together.
- Crew/subcontractor management with mobile execution surfaces, photo documentation, progress updates.
- Deposits, online payments, consumer financing options on proposals.
- Job costing / profit tracking (margin vs markup), role-gated visibility.
- Insurance-claim context on the job (claim number, adjuster, date of loss, deductible, damage type) and claim-path tooling at varying depth (Xactimate sync, supplements as change orders, depreciation tracking).
- Lead-capture machinery: instant estimators, AI call answering, lead-source tracking, lead-marketplace and canvassing integrations.
- Customer communications (text/email automation), customer portals (2/4 observed), review/referral machinery.
- Accounting sync (QuickBooks dominant), reporting/dashboards, automations/workflows, role permissions.

### L2 — Variant / Optional Structure

- Payment path mix: retail sale (deposit + final payment, financed) vs insurance claim (adjuster approval, supplements, ACV/RCV, depreciation holdback) — companies run either or both.
- Storm/catastrophe response machinery: hail mapping, targeted canvassing, rapid inspection scheduling — prominent in hail-belt markets, absent elsewhere.
- Commercial/flat-roof roofing: project-shaped work, service agreements (observed at one sampled product's commercial pole).
- Multi-trade / exteriors bundling (gutters, siding, windows) on one project.
- Crew model: in-house crews vs subcontracted crews (subcontractors-as-contacts pattern).
- Measurement realization: ordered third-party reports vs in-product DIY drawing vs blueprint import vs field measurement.
- Supplier integration depth: direct API ordering with status/invoice/POD sync vs manual order records.
- Customer portal, AI receptionist, AI estimating assistance — era-current additions.

### L3 — Vendor-specific (Research Notes only)

- AccuLynx: AccuPay/AccuFi branded payments/financing; Order Manager; Reports+/Data Mart; private-equity portfolio solutions; "9 hours saved/32% more profit" marketing stats.
- Roofr: $13-per-report pricing with 2-hour delivery; Jumpstart catalog import; Roofr Sites (AI-built website); Roofr of the Month; seat-based plans (Starter 3 / Essentials 5 / Scale unlimited); 13-minute support reply marketing.
- JobNimbus: Engage texting; AssistAI; Boards/Workflows terminology; per-supplier capability matrix (ABC lacking invoice import); Legacy section (migrated feature set).
- ServiceTitan: Insurance Sales Queue; Atlas AI; Pro Products; Enterprise Hub; Convex prospecting; two-way Xactimate sync framing; iPermit integration.

## Vendor-specific Findings

See L3 above. Additional packaging observation: the three roofing-dedicated products represent three philosophies (production-first, measurement-first, sales-CRM-first) while the horizontal platform ships roofing as a dedicated configuration — i.e., even the strongest generic FSM vendor treats roofing as requiring trade-specific machinery (measurements, supplier ordering, claim workflow), not just a trade page.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling, unprocessed)** — probable structural sibling-with-additions, NOT a pure trade-tuned variant. The shared spine (customer+location → job → field execution → billing) is identical, but 4/4 sampled products carry two structures the generic FSM spine lacks: the measured-roof quantity basis and job-bound supplier-direct material procurement; and the job shape is sale-driven production (lead → proposal → sold → production) rather than a dispatched service visit. The strongest generic vendor serves roofing through a dedicated configuration carrying exactly those structures. Seam: remove measurement + material procurement + the sale-driven production shape → generic FSM. A roofer running a trade-agnostic tool with no measurement/material machinery sits at this boundary (the trade-agnostic pole). Joint review recommended when the FSM leaf is processed.
2. **vs Home Improvement Contractor Management (§29, processed)** — sibling; roofing is a trade-specific instantiation of the sale-driven exterior-remodeling shape. Home improvement's generalist production plan (templated multi-step phases, selections) vs roofing's measurement→material→crew production chain. The recorded sale as lead→customer pivot is shared. Keep-separate: roofing's measured-roof basis and distributor-direct material loop have no home-improvement analog in that pass's evidence.
3. **vs Flooring Contractor Management (§29, processed)** — closest structural sibling (five-leg parallel: job of record + measured-area basis + material sourcing + installation execution + money resolution). Seams: the measured object (exterior roof planes, pitch, facets vs interior floor areas, seam/waste planning); the supply chain (roofing distributors with aerial-measurement ecosystem vs flooring dealers + fcB2B exchange); the execution shape (crew tear-off/install with deliveries vs installer work orders); the insurance-claim path's prominence (storm work) in roofing. Keep-separate; both pass the "remove the measured object and the trade's supply chain → the other trade" test.
4. **vs Restoration Contractor Management (§29, processed)** — the insurance overlap. Restoration's L0 makes the loss-driven job + evidentiary file + payer-review payment path definitional because restoration work is *defined* by the damage event. Roofing's insurance work shares the claim context (claim #, adjuster, supplements, depreciation) but the roofing job is not loss-defined — retail replacement is an equal pole — and the evidentiary machinery is lighter (photos + measurements + claim fields, not moisture maps/contents/pack-out). Seam: loss-driven vs sale-or-claim-driven. A roofing company doing full insurance restoration drifts toward the restoration Type.
5. **vs Construction Project Management (§17)** — commercial-roofing pole drifts toward project machinery, but the sampled center is the contractor's own business system (sale → production → billing), not multi-organization contractual project coordination.
6. **vs Quantity Takeoff / Construction Estimating** — the measurement layer alone (ordered reports, DIY drawing) is a capability supplier to this Type, not the Type.
7. **vs CRM** — the front half (leads, pipeline, proposals) only; the Type is defined by production + procurement + money resolution behind the sale.
8. **vs Local Service Marketplace** — demand-side discovery vs operator-side execution; a marketplace lead becomes a job here (consistent with ~10 sibling passes).
9. **Aerial measurement services (EagleView, Hover, GAF QuickMeasure, RoofScope)** — no directory leaf; they are integration suppliers feeding measurements INTO this Type (documented at all four sampled products).

## Historical / Market-Sample Check (§24)

Paper-era roofing contractor: customer card file; ladder-and-tape measurement written on an estimate pad; signed proposal/contract; material order phoned to the lumber yard or supplier with a delivery date; crew board on the shop wall; invoice and payment record; adjuster meetings and supplement letters for storm jobs. **All five L0 legs are satisfied with zero modern machinery** — no aerial reports, no supplier APIs, no kanban boards, no e-signature. The kanban pipeline, aerial measurement reports, supplier API sync, and instant estimators are dominant modern realizations, not the definition. Regional check: UK/European roofing and flat/commercial roofing satisfy the same five legs (job, measurement, materials, crews, billing); the insurance-claim machinery is a North-American-market prominence, held as standard-capability-with-variant-depth, not definitional.

## Uncertainties

1. **Manufacturer warranty registration / contractor certification machinery** (e.g., manufacturer-certified installer programs, warranty registration flows) — suspected in the trade but **not observed in any fetched source**; not claimed anywhere.
2. **Sales-rep commission tracking** — standard in the sibling home-improvement pass, but not directly observed in this pass's fetched roofing sources; not claimed as roofing-specific.
3. **AccuLynx depth** — knowledge base unreachable (transport error ×2); AccuLynx asserted at Tier-2 site depth only; its supplement/claim tooling depth is unverified.
4. **JobNimbus/AccuLynx marketing-site positioning** — JobNimbus root 403; its self-positioning language is taken from the help center only.
5. **Permit/inspection-regulation machinery for roofing** (jurisdictional roofing permits) — not observed in fetched sources; iPermit appears only as a ServiceTitan integration name.
6. **Regional markets outside North America** — not sampled; all four products are North-American.
7. **Roofr insurance depth** — Roofr documents claim *fields* on the job card but no claim-workflow machinery was fetched; depth beyond fields unverified.

## Final Synthesis

Roofing Contractor Management is the roofing contractor's business system of record. It shares the field-service family spine (customer + property → job → field execution → billing) but is not a pure trade-tuned variant: the market maintains a dedicated vertical ecosystem (production-first, measurement-first, and sales-first dedicated products), and the strongest horizontal vendor serves roofing through a dedicated configuration rather than a trade page. What makes the Type structurally distinct is the pairing of **the measured roof as the quantity basis** (the job's material and price content derives from roof measurements — ordered aerial reports or self-drawn — which feed estimates and material lists) with **job-bound material procurement** (material orders created from the job and placed to roofing distributors, with delivery tracked against the job) and **crew-based production execution** (sold jobs convert into work orders and crew schedules, with subcontractors as first-class executing roles), all carried on a **sale-driven job lifecycle** (lead → inspection → proposal → signed contract → production → billing) with **money resolved against the job** (deposits, invoices, payments, financing; commonly also the insurance-claim path with supplements and depreciation tracking as a standard, depth-varying capability). The historical paper-era roofer satisfies all five legs without any modern machinery, confirming the abstraction sits above the current market's dominant implementation.
