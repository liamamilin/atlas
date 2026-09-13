# Research Notes — Home Improvement Contractor Management

Research date: 2026-09-08
Leaf: Home Improvement Contractor Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster)
Slug: home-improvement-contractor-management

## Research Goal

Understand what "Home Improvement Contractor Management" software actually is in the real market: what objects it manages, how improvement/remodeling work flows from lead to paid completion, what is structurally distinct versus the generic field-service spine (established by the §29 sibling passes) and versus Construction Project Management (§17, processed), and where its boundaries lie.

Family context carried into this pass:

- The §29 trade-cluster passes established that most trade leaves (electrical, cleaning, appliance repair, garage door, handyman) are trade-tuned variants of the generic field-service spine (customer+location → job lifecycle → worker coordination → billing), while flooring carries a genuinely stronger vertical structure (measured-area basis, dye-lot inventory, fcB2B).
- The handyman pass drew this leaf's edge from the small-job side: "larger, longer, project-shaped work… The handyman center is the small dispatched job; project machinery appears only at the larger-improvement edge."
- The flooring pass drew it from the trade side: "home-improvement is the generalist pole."
- The construction-project-management pass (§17) recorded a "residential-SMB pole (client-facing approvals — selections/signatures — instead of contract-form instruments)" as a variant of its own Type — meaning that pole drifts toward this leaf.
- Open question for this pass: does Home Improvement Contractor Management have a defining structure of its own, or is it (a) a trade-Variant of Small Business Field Service Management, or (b) the residential-SMB Variant of Construction Project Management?

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a home improvement / remodeling contractor (general contractor for consumer improvement work, operative remodeler, design-build, exterior/interior replacement contractors).
- Core objects likely: homeowner lead/customer with a sales lifecycle, estimate/proposal/contract, the improvement job/project with a production plan, crews/subcontractors, payments structured across the job (deposit/progress/final), warranty/service, commissions, job costing.
- Distinct-structure candidates to test: the sale as the job-creation gate; the production plan (multi-step, multi-day) as the execution shape; the deposit→progress→final payment schedule; financing as a sale-closing instrument; warranty/service after completion; lead-generation/marketing machinery as a first-class module.
- Closest neighbors: Small Business Field Service Management (§29 sibling), trade siblings (roofing, painting, flooring, siding, gutters), Handyman Business Management (§29), Construction Project Management (§17), Construction Estimating (§17), CRM (§07), Local Service Marketplace (§29), Home Improvement Planner (§29 consumer leaf, unprocessed).

## Research Questions

1. What is the unit of work — job, project, work order? What lifecycle does it carry, and how long does work span?
2. How does the sale happen — in-home appointment, proposal, contract, deposit? Is the sale the gate that creates the job?
3. What does "production" mean in this trade, and how is it structured (tasks, phases, processes, crews, work orders, calendars)?
4. How is money handled — deposits, progress payments, final balances, financing, job costing, commissions?
5. What consumer-sales machinery exists (lead generation, marketing automation, referral/repeat campaigns, financing, e-signature)?
6. What happens after completion (warranty, service, surveys, reviews)?
7. Which interfaces do users actually operate?
8. Where is the seam to Small Business Field Service Management and to Construction Project Management?
9. Historical check: would a paper-era remodeling contractor satisfy the minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Pole / philosophy | Evidence tier |
|---|---|---|
| MarketSharp | purpose-built remodeler/home-improvement CRM + production; sales-centric SMB pole | Tier 1 (support.marketsharp.com help center) + Tier 2 (root, project-management, convert-leads-to-sales, payments pages) |
| ServiceTitan (Residential Remodeling) | flagship trades platform; construction-shaped suite pole over one platform | Tier 2 (industries/residential-remodeling page + industries map) |
| improveit 360 | enterprise remodeler CRM built on Salesforce; BI/reporting-heavy pole | Tier 2 (root + project-management feature page) |
| FieldPulse (Contractors) | horizontal SMB platform; generic-contractor pole with project machinery | Tier 2 (solutions/contractors page) |
| One Click Contractor | in-home sales/estimating specialist; the sales-pole capability supplier (not a full management system) | Tier 2 (root page) |
| CoConstruct → Buildertrend | market-structure evidence: CoConstruct absorbed into Buildertrend; the construction-management pole's feature set (specs, selections, budgeting) | Tier 2 (co-construct.com migration page) |

Attempted and abandoned per source-access rules: Buildertrend (buildertrend.com 403 ×2 — root + remodelers solution page), Houzz Pro (houzz.com 403; help.houzz.com JS-error shell), Leap (leapworks.com timeout ×2), Buildxact (403), JobNimbus (403), JobProgress (403), Summar (transport error), ServiceTitan /industries/remodeling-software (404 — correct slug /industries/residential-remodeling found via industries map). Buildertrend, Houzz Pro, Leap, Buildxact, and JobNimbus are major market players in this space; the coverage gap is acknowledged and assertions are calibrated to the researched products.

## Sources

Fetched 2026-09-08:

- MarketSharp (Tier 2): https://www.marketsharp.com/ (root); /features/streamline-project-management/; /features/convert-leads-to-sales/; /contractor-payments/
- MarketSharp (Tier 1, support.marketsharp.com Zendesk help center): category map (Contact Management / Jobs / Production / Marketing / Call Center / Reporting); /hc/en-us/articles/1500006458681-Job-Details; /hc/en-us/articles/1500006458941-Adding-Production-Tasks-Processes; /hc/en-us/articles/1500006510262-Production-Overview; /hc/en-us/articles/8735324171159-Converting-a-Lead-to-a-Customer; /hc/en-us/articles/19204977899543-MarketSharp-Payments-Setup-and-Overview; Jobs and Production category listings (article titles observed: Add a Lead; Add a Prospect and Transfer to a Lead; Revert Customer Back to a Lead; Add a Job Site Address; Enter Job Costs; Enter Commission; Commission Payment Report; Service Orders; Service Scheduling; Create a Work Order; Job Site Addresses; Production Status Report)
- ServiceTitan (Tier 2): https://www.servicetitan.com/industries (industries map — "Residential Remodeling Software" among Other Industries; demo form job-focus split "Service and Replacement" vs "Construction or Remodel"); https://www.servicetitan.com/industries/residential-remodeling
- improveit 360 (Tier 2): https://www.improveit360.com/ (root); https://www.improveit360.com/features/project-management/
- FieldPulse (Tier 2): https://www.fieldpulse.com/solutions/contractors
- One Click Contractor (Tier 2): https://oneclickcontractor.com/ (root)
- CoConstruct / Buildertrend (Tier 2, market structure): https://www.co-construct.com/ (migration page)

**Source-access limitation**: no Tier-1 help-center documentation was reachable for ServiceTitan, improveit 360, FieldPulse, or One Click Contractor; all their evidence is Tier-2 official product pages. MarketSharp is the only product with Tier-1 operational documentation in this pass. Structural claims below rest on multiple independent vendor pages agreeing; precise operational details (exact statuses, field names, limits, defaults) are stated only where directly observed (mostly MarketSharp) and are otherwise not asserted.

## Product A — MarketSharp

### Key observations (evidence layer A; Tier 1 where marked)

- Positioning: "The All-in-One CRM Software for Contractors Remodelers Home Pros"; "Remodeling CRM software programs are all-in-one platforms created to manage remodeling & home-improvement construction projects… designed with industry-specific tools like lead and customer management, production process workflows, and sales and estimating tools." FAQ audience list: remodelers, window & door installers, home improvement contractors, roofing contractors, painters, deck builders, drywall and insulation, siding and gutter professionals. [Tier 2]
- **Contact lifecycle with a sale-gated conversion** [Tier 1]: help-center articles "Add a Prospect and Transfer to a Lead", "Add a Lead", "Converting a Lead to a Customer", "Revert Customer Back to a Lead". Conversion mechanics (directly documented): an appointment on the contact record is resulted with an appointment-result option that has a "SOLD" flag; "if you choose an appointment result that does not have SOLD checked, then the lead will not convert to a customer"; on a sold result the save button becomes "Save & Create Job" — "The lead will now convert over to a customer and you will now be prompted to create a job." The stated purpose: "this will allow you to create jobs for the contact and schedule production steps such as installations, remeasures, and more."
- **Job with products** [Tier 1]: Contact Record → Jobs tab → Job with Product(s) → Product Details ("Add New Product Detail if there is more than one item"). Job Site Addresses are separately entered (articles "Add a Job Site Address", "Enter A Jobsite Address"). Jobs can be canceled; deletion errors documented.
- **Production module** [Tier 1]: "The Production module allows you to create production tasks and process steps required to complete the job. It tracks start/end dates, work crews assigned, and job completion." Roles on the job: Project Manager, Work Crew, Worker(s). Production Task fields: Description, Assign To, Expected Start/End Dates, Actual Start/End Dates; tasks attach to Activity Processes; tasks can be placed on calendars (multi-day tasks appear as all-day events). Production Processes are templated step sequences per product type ("Enter the steps/Tasks/Milestones required to complete the job or process… You may create up to 25 tasks per job/project type"), with per-step scheduler and work-order enablement; business-day rules ("If you do not include [Saturdays/Sundays] in your business week and a task falls on a Saturday/Sunday, MarketSharp will push the task next business day"). Production Tab: open/completed tasks filterable by date range/employee/task description, exportable; Production Status Report computes "AVG Days in PRODUCTION" and "AVG Days in STEP" per job/product/step; email automation can be triggered by production steps; work orders created per step.
- **Money on the job** [Tier 1 + Tier 2]: Jobs category contains "Enter Job Costs", "Enter Commission", "Commission Payment Report", "Financial Data & Payments". Payments (Tier 2 payments page + Tier 1 setup article): digital invoices from jobs "with a single click"; payment types include "Tax, Payment, Finance Charge, Down Payment, Cash, Finance, ACH, Credit Card, or Discount"; "Job deposits – collect payment upfront and ensure scheduled jobs are not canceled or deferred"; card-on-file; online payment forms; mobile payments via the RemodelerGo app; PaySimple gateway integration; PCI compliance; payment reporting (project type, payment methods, remaining balances, monthly reconciliation).
- **Sales machinery** [Tier 2]: Sales Activities (customizable activity/task reminders and processes, sales activity tracking and history, sales opportunity tracking, built-in sales closing tools); drip marketing campaigns ("40+ email campaigns built-in"); appointment reminders and two-way texting; pre-appointment roof measurement reports ordered in-system; homeowner financing powered by GreenSky and Mosaic ("Next-day and staged funding"); One Click Contractor integration ("Push in-home or online product presentation details into MarketSharp").
- **Project/service management** [Tier 2]: "Contract and Production Management; Customizable Workflow Automation; Service Management; Lead Paint compliancy; Commission Tracking / Job Costing; Jobsite Images and Document Attachment Tool"; documents include "contracts, change orders, and service documents"; CompanyCam integration for photos; warranty management (service calls viewable by date range/representative/type/status; service tasks created under the Jobs tab; automated warranty reminders); surveys attached to jobs [Tier 1 category].
- Scheduling: sales-appointment routing ("Plot out driving distances between construction projects and optimize travel time between appointments"); crew scheduling; color-coded calendars; slot scheduler [Tier 1 promoted article].
- Testimonial (positioning evidence): "running a multi-million dollar company with MarketSharp at its core for marketing, lead flow, production and service."

## Product B — ServiceTitan (Residential Remodeling)

### Key observations (evidence layer A, Tier 2)

- Dedicated trade page "Residential Remodeling Software" (listed under "Other Industries" on the industries map, alongside handyman, gutter, siding, locksmith, etc.). Audience named on the page: "general contractors, operative remodelers, design-build and project construction management companies."
- Pitch: "From managing schedules and budgets to tracking progress and resources… complete projects of any size."
- Construction-tab feature blocks: Project management ("From bid to completion, view project progress, compare budgeted costs with actual expenditures, and streamline collaboration, all from one project tracking hub"); Billing ("Bill customers at every phase and make payment a breeze"); Accounting (sync); Job costing ("Maximize job profitability and preserve cash flow"); Crew management ("Manage field crews from the office or a mobile device"); WIP reporting ("Boost efficiency by tracking job progress in real time"); Dynamic forms; Inventory.
- Residential-tab feature blocks: Scheduling ("schedule or reschedule contractors and crews for specific durations during remodel projects"); Marketing; Finance options ("Close bigger remodeling jobs with on-the-spot financing"); Invoicing; Field mobile app; Customer service; Estimating ("Quickly build multi-option home remodeling estimates"); Crew dispatching.
- Customer-experience claims: two-way SMS; "simple and convenient payment options, including financing with instant approvals"; "Allow clients to visualize their spaces through beautiful, tiered estimates with photos and videos."
- Efficiency claims: "Track work in progress and manage project costs in real-time to stay on schedule and budget"; "Accurately bid jobs with real-time job costing insights into labor, materials, and profit margins."
- Vendor-claimed stats (marketing, not independently verified): 15% average revenue growth; +5–10% YoY ticket size; +20% customer retention.
- FAQ: "Residential remodeling software helps your company manage every project… From managing schedules and budgets to tracking progress and resources in real time"; suitability "from small design-build outfits to larger companies with multiple crews and locations"; QuickBooks Online/Desktop Premier/Enterprise integration; "your crew leaders can easily generate invoices and purchase orders, then export them directly to QuickBooks."
- Market-structure observation: the ServiceTitan demo form asks "Select job focus: Service and Replacement | Construction or Remodel" — the vendor itself splits its residential platform into a service pole and a construction/remodel pole, and maintains separate solution pages (/market/field-service-management-software vs /market/construction-software). The remodeling trade page draws on both feature sets.

## Product C — improveit 360

### Key observations (evidence layer A, Tier 2)

- Positioning: "The Most Powerful Remodeler & Home Improvement CRM… Track, Estimate, Schedule, Quote, Report, and Manage Projects – All-in-One Enterprise CRM"; "Enterprise Software Built For Your Home Improvement Business"; built on Salesforce (login.salesforce.com; Salesforce partner badge).
- Feature map: CRM & Lead Management; Marketing Status & Lifecycle Automation; Appointment Scheduling; Online Invoicing & Payments; Project Management; Homeowner Financing; Lending; Sales Tools & Quoting; Marketing & Call Centers; Business Intelligence & Reporting.
- Value narrative: "Streamline Lead Conversion" (leads received instantly, nurtured to buy, block scheduling); "Increase Sales Opportunities" (sales tools & quoting, automated marketing campaigns); "Manage Your Projects" ("trackable job costs, payments & financing options, and templated tasks & activities… stay on budget, get paid on time, and never miss a deadline"); "Report in Real-time" (automated reports/dashboards, ROI reports); "Get Paid Faster" (online payments in-system).
- Project Management page (dedicated): "Built specifically for remodelers and home improvement businesses… delivers real-time visibility and control across every active job. Directly embedded in the improveit 360 CRM, project management brings scheduling, task dependencies, performance tracking, and payments into one connected workflow… manage jobs from first task through final payment."
  - "project timelines are visualized through Gantt charts and task dependencies that show how work flows from start to finish… clear sequencing and ownership."
  - "timelines, progress, and completion percentages are automatically calculated based on real activity—not manual updates or assumptions."
  - "projects tie directly into deposits, progress payments, and final balances—keeping financials aligned with real work as it happens."
  - "activity-level performance data highlights bottlenecks and inefficiencies across jobs."
- Customers named: Re-Bath (franchise bath remodeler), 3 Blind Mice Window Coverings, Renaissance Development. Franchisors & Manufacturers program exists (network pole).

## Product D — FieldPulse (Contractors solution)

### Key observations (evidence layer A, Tier 2)

- No dedicated home-improvement industry page; contractors addressed via the generic "Contractors" solution ("Software for Specialty Contractors… manage jobs, provide accurate estimates, and oversee complex projects") plus Residential/Home Services segments. FAQ: "Contractor software is designed to optimize project management, job scheduling, and invoicing for general contractors."
- Contractor scheduling: job scheduling/dispatch; contract storage; service history; renewal reminders.
- Contractor estimating: detailed quotes with cost breakdowns; estimates convert to invoices (one-click); contract-based pricing; profitability tracking.
- Contractor project management: "Task Assignment and Tracking: Break down large projects into tasks, assign them to the right team members, and track progress in real time"; "Resource Allocation: Manage resources, materials, and labor… each phase of the project"; "Project Timeline Monitoring: Track each phase of the project and ensure that milestones are hit on time, keeping your project within scope and budget." Imagery shows a project phase card "In Progress" with a task checklist and completion-percentage slider, plus job-status tags (New Job, On The Way, Pending, Completed, Canceled).
- Platform map (generic): Scheduling & Dispatching, Work Order Management, Job Management, Estimates & Invoices, Project Management, Pricebook, Job Costing, Inventory, Maintenance Agreements, Customer Portal, Booking Portal, Payments, Financing, Custom Forms, Mobile App, AI dispatching (Operator AI), ClearPath guided workflows.
- Reading: the generic-contractor pole realizes the same spine with lighter sales machinery (estimates rather than a managed in-home sales process) — the boundary pole toward Small Business Field Service Management.

## Product E — One Click Contractor (sales-pole capability supplier)

### Key observations (evidence layer A, Tier 2)

- Positioning: "Home Remodeling Estimating Software… Close More Deals with Fast Estimates and Easy Financing. Turn every appointment into a signed contract."
- Workflow (named steps): Capture & Measure (import measurements from EagleView/Hover or in-app tools; "Photos and documents are saved automatically to one digital job folder") → Build Estimates Fast ("Select a template, let measurements auto-fill line items, and apply locked-in pricing rules") → Present the Proposal ("polished, branded proposal… Adjust options live in the home") → Offer Financing Options ("single soft pull application… checks multiple lenders") → Sign & Collect Payment ("Turn the proposal into a contract, capture e-signatures in minutes, and process deposits or payments before you leave the home").
- Tagline: "Quote, Sign, and Fund Before You Leave the Driveway."
- Specialties: roofing, one-day bath, window replacement, exterior remodeling, interior remodeling.
- Reading: this is the in-home sales layer of the Type sold as a standalone product — it ends at the signed contract and deposit; production and back-office money are not in its core. Treated as a capability supplier to the Type (integrated into MarketSharp and others), not as the Type's center — same pattern as Measure Square in the flooring pass.

## Market-structure evidence — CoConstruct → Buildertrend

- CoConstruct's site is now a migration page: "CoConstruct's transition to Buildertrend is entering its final phase." CoConstruct's positioning: "Our focus on financial management means builders have clear guidance on profitability"; audience "home builders and remodelers."
- The migration page enumerates the construction-management pole's feature set: Specs ("detailed specifications… Organize materials, finishes and requirements"), Selections ("Simplify one of the most complex parts of the building process… help clients make decisions faster, track approvals"), Task management, Client Updates ("AI-powered progress updates and real-time project visibility"), Plans, Signatures and annotations, Better budgeting ("Track costs in real time, monitor profitability").
- Reading: the strongest construction-management pole (Buildertrend/CoConstruct class) serves builders and remodelers with client-facing project machinery (selections, specs, client portals) — this pole drifts toward Construction Project Management (§17), whose own pass recorded the "residential-SMB pole (client-facing approvals — selections/signatures)" as its variant. The two Types meet at this pole.

## Cross-product Comparison

| Structure / capability | MarketSharp | ServiceTitan (Remodeling) | improveit 360 | FieldPulse (Contractors) | One Click Contractor | Assessment |
|---|---|---|---|---|---|---|
| Homeowner contact with managed sales lifecycle (lead → sold customer) | ✓ Tier 1 (prospect→lead→customer; SOLD appointment result gates conversion) | ✓ (CRM, Marketing, call booking) | ✓ (CRM & Lead Management; lifecycle automation) | partial (customer management; estimates→jobs) | ✓ (appointment→signed contract is the whole product) | Universal in the purpose-built products; lighter at the generic pole — core |
| Estimate/proposal → recorded sale → job creation | ✓ Tier 1 ("Save & Create Job") | ✓ (multi-option estimates; bid → project) | ✓ (quoting; projects from sales) | ✓ (estimate → job/invoice conversion) | ✓ (proposal → contract → deposit) | Universal — core |
| Job/project of record at the home | ✓ Tier 1 (Job with Products; jobsite address) | ✓ (project tracking hub; "manage and track remodeling projects in real time") | ✓ (project management embedded in CRM) | ✓ (project records with phases) | partial (digital job folder; no production) | Universal — core |
| Production plan: sequenced steps/phases, expected vs actual dates, crews | ✓ Tier 1 (production tasks/processes; project manager/work crew/worker; work orders; production calendar) | ✓ (project management; crew management; scheduling "for specific durations") | ✓ (Gantt charts, task dependencies, auto-computed completion) | ✓ (phases, tasks, milestones, resource allocation) | ✗ | Universal in management products — core |
| Payment schedule across the job (deposit → progress → final) | ✓ (job deposits; down-payment type; digital invoices) | ✓ ("Bill customers at every phase") | ✓ ("deposits, progress payments, and final balances") | partial (invoicing/payments; deposit not explicit on page) | ✓ (deposits before leaving the home) | Common-strong (4/5 explicit) — core |
| Job costing / profitability on the job | ✓ Tier 1 (Enter Job Costs) | ✓ (job costing; budget vs actual) | ✓ (trackable job costs) | ✓ (profitability tracking) | ✗ | Universal — standard |
| Sales commissions | ✓ Tier 1 (Enter Commission; Commission Payment Report) | — (not on remodeling page) | — (not on fetched pages) | — | — | Common (sales-team pole) — standard |
| Homeowner financing | ✓ (GreenSky/Mosaic; lending) | ✓ (on-the-spot financing; instant approvals) | ✓ (homeowner financing; lending) | ✓ (FieldPulse Financing) | ✓ (1LOOK multi-lender) | Universal — standard (era-current) |
| E-signature contracts / change-order documents | ✓ (contracts, change orders as documents; SharpDoc) | ✓ (signatures/annotations per BT migration page; dynamic forms) | ✓ (documents) | ✓ (custom forms; PDF signatures per testimonial) | ✓ (e-sign in minutes) | Universal — standard |
| Lead generation / marketing automation | ✓ (lead providers, call tracking, drip campaigns, radius leads) | ✓ (Marketing; lead nurturing) | ✓ (marketing & call centers; lifecycle automation) | partial (booking portal; reviews) | ✗ | Common — standard |
| Warranty / service after completion | ✓ Tier 1 (Service Orders; Service Tab; warranty reminders) | — (not on remodeling page) | — (not on fetched pages) | ✓ (service call software; maintenance agreements) | ✗ | Common — standard |
| Customer status updates / portals | ✓ (automated status texts/emails) | ✓ (two-way SMS; customer portal) | ✓ (client updates per BT-class) | ✓ (customer portal; communication) | ✗ | Universal — standard |
| Reporting: production status / WIP / dashboards | ✓ Tier 1 (Production Status Report; AVG days in step) | ✓ (WIP reporting) | ✓ (BI & reporting; bottleneck analytics) | ✓ (dashboards & reporting) | ✗ | Universal — standard |
| Accounting sync | ✓ (QuickBooks-class; financial data) | ✓ (QuickBooks two-way) | ✓ (integrations) | ✓ (QuickBooks-class) | ✗ | Universal — standard |
| Mobile app (sales + field) | ✓ (RemodelerGo) | ✓ (field mobile app) | ✓ (proprietary mobile app) | ✓ (mobile app) | ✓ (iOS/Android) | Universal — standard |
| Multi-option / tiered estimates with photos | ✓ (build quotes in the field; templates) | ✓ (tiered estimates with photos and videos) | ✓ (sales tools & quoting) | ✓ (detailed quotes) | ✓ (live option adjustment) | Universal — standard |
| Client-facing project machinery (selections, specs, client portals) | — | — | partial | partial (customer portal) | ✗ | The construction-management pole (Buildertrend/CoConstruct) — variant |
| Trade layer realization | purpose-built remodeler CRM | dedicated Residential Remodeling trade page over a split platform | purpose-built remodeler CRM (enterprise) | generic Contractors segment | purpose-built in-home sales tool | The Type's packaging pattern |

### What is actually home-improvement-specific (across sample)

1. **The sale is the pivot, and selling is appointment-driven, in-home, and instrumented** — leads are worked through scheduled sales appointments; the recorded sale (a "SOLD" appointment result in MarketSharp, an accepted proposal/signed contract elsewhere) is what converts a lead into a customer and creates the job. The sales layer carries its own machinery: opportunity tracking, multi-option/tiered proposals with photos, financing offers, e-signature, deposit collection. [Layer A ×5; Tier 1 for MarketSharp's gate mechanics]
2. **Execution is a production plan, not a dispatched visit** — the job's work is organized as sequenced steps/phases (templated processes per product type, expected vs actual dates, project manager/work crew/worker roles, work orders, production calendars, multi-day scheduling). [Layer A ×4 management products; Tier 1 for MarketSharp]
3. **Money is structured across the job's life** — deposit at/after sale, payments tied to phases/progress, final balance at completion; job costs and (where sales teams exist) commissions are recorded against the job. [Layer A ×4 explicit]
4. **The after-sale loop is part of the system** — warranty/service orders, surveys, review requests, and repeat/referral campaigns hang off the completed job. [Layer A ×3–4]
5. **Consumer-financing is a standard closing instrument** — every sampled product offers homeowner financing (multi-lender matching, on-the-spot approval, staged funding). [Layer A ×5; era-current]

No sampled product showed a structurally distinct *trade* object (no measurement basis like flooring, no inspection/deficiency loop like fire protection, no equipment registry). The Type's distinctness is the sale→production→payment shape of the improvement project business, not trade content.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

A home improvement contractor management system is the operator-side business system of record for a contractor selling and producing improvement work in customers' homes. Its defining core is four jointly-held structures:

1. **The homeowner customer of record carried through a managed sale** — the customer is a persistent contact moving from inquiry/lead through estimate/proposal to a recorded sale; the recorded sale is the pivot that converts the contact into a customer-with-a-job. Remove → a production tracker or generic project tool with no front door.
2. **The improvement job of record at the home** — a persistent, individually identified job for the sold work at the customer's residence (jobsite address, products/scope), the container that production and money hang from. Remove → a contact list with quotes.
3. **Production as a planned multi-step effort** — the job's work is organized as sequenced steps/phases with expected vs actual dates, assigned project manager/crews/workers, and work orders, tracked from start to completion — a project shape spanning days to weeks, not a single dispatched visit. Remove → a field-service dispatch board.
4. **Money resolved across the job's life** — a deposit collected at/after the sale and further payments tied to progress or completion, with job costs (and, where sales teams exist, commissions) recorded against the job. Remove → a sales CRM with no fulfillment economics.

Jointly-held is load-bearing:
- 1+2 without 3+4 = lead tracker with a job list (CRM territory).
- 1+3 without 2+4 = sales pipeline with a task list, nothing produced or billed.
- 2+3 without 1+4 = production scheduler (construction-PM-lite without the business).
- 1+4 without 2+3 = sales CRM with invoicing (no fulfillment).
- 3+4 without 1+2 = generic project cost tracker.

Historical check (§24): a paper-era remodeling contractor — inquiry card file, in-home sales visit with a written proposal, signed contract with a deposit, a production schedule on a whiteboard or day-runner, progress payments as work advances, final payment at completion, a warranty log — satisfies all four structures with no software. A one-person remodeler collapses the sales/production/office roles into one person but keeps the structures. The check passes; nothing cloud/mobile/AI/financing-specific is in the core.

### Level 1 — Common Mature Structure (not definitional)

- Estimates/proposals: multi-option or tiered, with photos/videos, templates auto-populating priced products/services; measurement imports from specialist tools (aerial roof measurement, room measurement) as integrations
- Contracts and e-signature; change orders and other job documents; jobsite photo/document attachment
- Homeowner financing as a closing instrument (multi-lender matching, on-the-spot decisions, staged funding)
- Sales-appointment scheduling with routing; slot scheduling; appointment reminders and two-way texting
- Lead generation and marketing automation: lead-provider/call-tracking integrations, drip campaigns, jobsite-radius leads, direct mail
- Repeat/referral campaigns and online review requests after completion
- Production coordination: production calendar, work orders per step, templated production processes per product type, business-day scheduling rules, crew assignment (in-house or subcontracted)
- Warranty/service management: service orders, service scheduling, warranty reminders
- Surveys and review capture on completed jobs
- Reporting: production status (aging per step), WIP, job costing, commissions, marketing ROI, dashboards
- Accounting sync (QuickBooks in the North American market)
- Mobile apps for sales and field roles
- Customer status updates (automated texts/emails) and customer portals

### Level 2 — Variant / Optional Structure

- Product poles: sales-centric in-home selling pole (One Click Contractor class — sold as a capability supplier); CRM/production pole (MarketSharp, improveit 360); construction-management pole (Buildertrend/CoConstruct class — specs, selections, client portals, budgeting; drifts toward Construction Project Management); suite FSM pole (ServiceTitan construction module, FieldPulse project machinery)
- Customer scale: SMB vs enterprise; franchise/manufacturer network programs (franchisor roll-ups observed at improveit 360 and among MarketSharp-class customers)
- Crew model: in-house crews vs subcontracted labor
- Contract/payment models: lump-sum with deposit/progress schedule vs third-party financed (lender funds upfront)
- Design-build emphasis (selections/design machinery)
- Specialization pages per product family (roofing, bath, windows, siding) — trade content over the same spine
- Regional infrastructure: North American financing/lead-gen ecosystem (GreenSky/Mosaic-class lenders, lead providers, QuickBooks); regional variance unverified
- AI assistance (era-typical: AI progress updates, AI dispatching, AI estimating claims)

### Level 3 — Vendor-specific (kept out of the canonical document)

- MarketSharp: RemodelerGo mobile app; PaySimple gateway; SharpDoc; slot scheduler; on-demand roof measurement reports (flat fee, <4h); 40+ built-in email campaigns; 25-task process limit; EverPro Edge; "96% of texts read within 3 minutes" claim; 2.90%+$0.30 processing pricing
- improveit 360: Salesforce-platform basis; CRM ROI calculator; Gantt/task-dependency visualization; franchisor program
- ServiceTitan: 15%/+5-10%/+20% marketing stats; Atlas; Pro product line; the demo form's "Service and Replacement vs Construction or Remodel" split; "Other Industries" placement of the remodeling page
- FieldPulse: Operator AI, ClearPath, Engage VoIP; 78% YoY growth claim
- One Click Contractor: 1LOOK multi-lender financing; "quote in 3 minutes"; "$14B in project estimates"; "50% increased close rates" claims
- CoConstruct/Buildertrend: migration program; specs/selections/budgeting feature naming

## Vendor-specific Findings

See Level 3. Notable patterns: (1) the market's own naming is split — "remodeling CRM" (MarketSharp, improveit 360), "residential remodeling software" (ServiceTitan), "contractor software" (FieldPulse), "construction management" (Buildertrend/CoConstruct) — all describing overlapping businesses from different feature poles; (2) ServiceTitan's platform formally splits service vs construction/remodel, confirming the structural seam from the vendor side; (3) the sales layer is sold both inside suites and as standalone specialist products that integrate into them.

## Rejected Findings

1. **"Remodeling CRM = generic CRM"** — the sales pipeline fragment is shared with §07 CRM, but the job/production/money-on-job structures are not CRM structures. Rejected as identity; the CRM is one pole of this Type.
2. **Production plan as mere project management** — the machinery resembles generic project management, but its content is trade-shaped (production processes per product type, work orders, crews, installs/remeasures) and it hangs on the sold job of a consumer-sale business. Held as this Type's structure 3, with the §17 seam drawn separately.
3. **Financing as definitional** — universal in the current sample but era- and region-specific (consumer credit ecosystem); a paper-era contractor satisfies the core without it. Held at L1.
4. **Lead-generation/marketing machinery as definitional** — strong in the purpose-built products but absent/light at the generic pole (FieldPulse) and not structural. Held at L1.
5. **Trade-specific structures (measurement basis, inspection loops, equipment registries)** — none observed in any fetched source; these belong to the trade siblings (flooring, fire protection, appliance repair). Rejected for this Type.
6. **Client-facing selections/specs machinery as definitional** — present only at the construction-management pole (Buildertrend/CoConstruct class); a variant pole, not the core.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling)** — the family spine (customer → job → execution → billing) is shared, but the center of gravity differs structurally: here the unit of work is a sale-driven project with a multi-step production plan and a deposit→progress→final payment schedule; there it is a dispatched service call (often completed in one visit) with invoice-on-completion. Market evidence: ServiceTitan splits its own platform into "Service & Replacement" vs "Construction" solutions and asks prospects to self-select "Service and Replacement" vs "Construction or Remodel"; FieldPulse realizes the seam internally by bundling project machinery into its Contractors segment. The seam is real but gradual — small improvement jobs on an FSM product are the boundary pole. Flag for joint review with Small Business Field Service Management.
2. **vs Construction Project Management (§17, processed)** — §17's core is the multi-organization project community with formal cross-party coordination instruments; this Type is the single contractor's whole-business system (leads/sales/production/money) for consumer work. The §17 pass already recorded its "residential-SMB pole (client-facing approvals — selections/signatures)" as a variant — that pole is this Type's construction-management pole (Buildertrend/CoConstruct class). The two Types meet and interlock at the remodeler edge; joint review recommended. The durable seam: multi-party contractual coordination vs one business's sale-to-production operation.
3. **vs trade siblings (roofing, painting, siding, gutters, flooring, solar, etc.)** — this leaf is the generalist pole of improvement work (the market's own FAQ lists those trades as users of remodeling CRM); trade siblings add trade-specific structures (flooring's measured-area basis, roofing's aerial measurement integrations — which appear here only as integrations). Same-family siblings; cross-reference when those leaves are processed.
4. **vs Handyman Business Management (§29, processed)** — the handyman center is the small dispatched job (FSM shape); this Type's center is the larger project-shaped improvement job with a production plan. The handyman pass documented the drift at its own edge ("project machinery appears only at the larger-improvement edge"). Consistent seam.
5. **vs CRM (§07)** — the lead→opportunity→sale pipeline is shared; the job of record, production plan, and job-life money are not. A generic CRM cannot hold this Type's fulfillment half.
6. **vs Construction Estimating / Quantity Takeoff (§17)** — estimating tools (and measurement services like aerial roof measurement) appear as integrations ("Connect with industry-leading estimating tools"); they are capability suppliers to the sale, not the Type.
7. **vs Local Service Marketplace (§29)** — demand-side discovery/lead selling vs operator-side execution; lead providers feed this Type's lead stage. Complementary.
8. **vs Home Improvement Planner (§29 consumer leaf, unprocessed)** — consumer-side planning of one's own improvement project vs the contractor's business system. Different subject of record.
9. **vs Progress Billing / Change Order Management (§17)** — realized here in light form (phase billing, change-order documents) as capabilities, not as the organizing objects.
10. **vs Appointment Scheduling Application (§03.09)** — sales-appointment scheduling is one fragment; the Type is the whole business operation.

## Uncertainties

1. **Major vendors unreachable** — Buildertrend, Houzz Pro, Leap, Buildxact, JobNimbus, JobProgress all failed access (403/timeout). Buildertrend in particular is likely the category's flagship for the construction-management pole; the pole's evidence rests on the CoConstruct migration page (Tier 2) plus the §17 pass's residential-SMB observation. Assertions are calibrated to the five researched products.
2. **No Tier-1 documentation for four of five products** — ServiceTitan, improveit 360, FieldPulse, and One Click Contractor evidence is Tier-2 (official product pages). Exact object models, statuses, and rules for those products are not asserted; MarketSharp's Tier-1 help center carries the load for operational mechanics.
3. **Deposit/progress payment universality** — explicit in 4/5 sampled products (FieldPulse's contractors page does not name deposits); the pattern is held as core based on the sales-driven shape, but its exact realization (percentages, milestones, draw schedules) is unverified and not asserted.
4. **Regional coverage** — the sample is North America–dominant (financing ecosystem, QuickBooks, lead providers). European/Asian remodeling software not sampled; regional variants unverified.
5. **Subcontractor management depth** — crews/subs appear as assignment targets and payees, but dedicated subcontractor-portal machinery (beyond §17's scope) was not directly evidenced in fetched pages; held at variant level.
6. **Warranty/service depth at the suite pole** — ServiceTitan's remodeling page does not surface warranty machinery (its service side carries it); the after-sale loop is Tier-1-evidenced at MarketSharp and present at FieldPulse. Held as common, not universal.

## Final Synthesis

Home Improvement Contractor Management is the business system of record for a contractor that sells and produces improvement work in customers' homes. Its defining core is the jointly-held four: the homeowner customer carried through a managed sale (lead → estimate/proposal → recorded sale, the pivot that creates the job), the improvement job of record at the home (products/scope, jobsite address), production as a planned multi-step effort (sequenced tasks/phases with expected vs actual dates, project manager/crews, work orders — a project shape, not a dispatched visit), and money resolved across the job's life (deposit at sale, payments tied to progress/completion, job costs and commissions on the job). Around that core, mature products add the consumer-sale instrument set (multi-option proposals, e-signature contracts, homeowner financing, appointment routing, lead-generation and referral machinery), the after-sale loop (warranty/service, surveys, reviews), and the reporting layer (production aging, WIP, job costing, commissions). The market realizes the Type in four poles — purpose-built remodeler CRMs, a construction-management pole drifting toward §17, suite FSM construction modules, and a standalone in-home sales layer sold as a capability supplier — with ServiceTitan's own service-vs-construction platform split confirming the seam against Small Business Field Service Management. The leaf is a legitimate independent Type: its sale→production→payment shape is structurally distinct from both the dispatched-visit FSM spine and the multi-organizational construction coordination record, with joint review recommended against both neighbors.
