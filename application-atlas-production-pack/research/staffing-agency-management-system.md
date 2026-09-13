# Research Notes — Staffing Agency Management System

## Research Goal

Understand, from real products, what a **Staffing Agency Management System** is: the software a staffing/recruitment agency runs its own business on. Establish the defining core, the standard capability set, the variant space, and — critically — the boundaries against the already-processed neighbors: Applicant Tracking System (employer side), Recruiting Management Platform (umbrella), Contingent Workforce Management / VMS (buyer side), Payroll System, and Employee Scheduling.

## Initial Boundary (hypothesis before research)

- Core hypothesis: an agency-side business system binding three parties — the **client** (organization buying workers), the **job order** (the client's open position), the **candidate/worker** (the person supplied) — closed by the **placement** as the commercial event; for temp/contract staffing, the placement becomes an assignment that runs a pay-and-bill cycle (agency pays the worker, bills the client).
- Nearest neighbors: ATS (same pipeline shape, different operator), VMS/CWM (mirror image, buyer side), Recruiting Management Platform (umbrella, converges in agency mode), Payroll (one leg), Employee Scheduling (downstream step).
- Prior processed passes already frame this leaf:
  - contingent-workforce-management: "Mirror image (supplier side)… the operator's identity is the discriminator."
  - recruiting-management-platform: "convergent in agency mode — agency-side business management (timesheets, billing, consultant compliance) goes beyond the agency variant's client CRM, placements, and revenue tracking."
  - employee-scheduling-platform: "adjacent — manages client orders, placements, and billing for external workers; scheduling is one downstream step."
  - applicant-tracking-system-ats: Bullhorn sampled as the "staffing-agency side (ATS + client CRM, placements)."

## Research Questions

1. Who operates the system, and in what roles (recruiter, account manager/BD, resourcer, back-office/pay-bill admin, compliance, branch manager)?
2. What are the core objects, and how do they relate (client/company, contact, job order/opportunity, candidate, submittal, placement, assignment, timesheet, billable item, invoice, pay run)?
3. What is the fill loop end to end (win order → source → submit → interview → place → onboard → work → time → pay + bill)?
4. How does the money work: placement fee (perm) vs pay/bill spread (temp/contract); margin, burden, gross profit?
5. What compliance machinery exists (worker documents, expiries, right-to-work/I-9, client-specific requirements)?
6. How do agency systems connect to client-side VMS programs and to job boards?
7. What separates this Type from an employer ATS, from a VMS, and from a payroll system?
8. Historical check: would a paper-era agency (job order book, candidate card file, time cards, client invoices) and a perm-only desk satisfy the definition?

## Representative Products

| Product | Tier sampled | Why chosen |
|---|---|---|
| Bullhorn | Tier 2 (ATS&CRM product page + Middle Office product page + FAQ) | Market-leading platform for staffing agencies; supplies the industry's own front/middle/back-office vocabulary; ecosystem posture |
| Crelate | Tier 1 (help center index + 4 deep articles) | Mid-market all-in-one; richest operational documentation of core records and the pay/bill back office |
| Avionté | Tier 2 (homepage + Payroll & Billing page) | Front+back-office single-platform philosophy; quantifies back-office scale (W-2s, payroll volume) |
| JobAdder | Tier 2 (features index + Temporary Recruitment + Placement Management pages) | International (AU-origin) mid-market; integration-posture back office; explicit temp-desk machinery |

Sample spans: market leader vs mid-market; native back office vs integration back office; US-centric vs AU/global; platform/ecosystem vs all-in-one vs recruiter-experience philosophies.

## Sources

- Bullhorn — ATS & CRM product page: https://www.bullhorn.com/products/applicant-tracking-system/
- Bullhorn — Middle Office product page (incl. front/middle/back-office FAQ): https://www.bullhorn.com/products/middle-office/
- Crelate Help Center (index): https://help.crelate.com/
- Crelate — "What is a Placement in Crelate?": http://help.crelate.com/en/articles/4449282
- Crelate — "What is an Opportunity Record?": http://help.crelate.com/en/articles/4460654
- Crelate — "What are Billable Items?": http://help.crelate.com/en/articles/5247725
- Crelate — "VMS Opportunity": http://help.crelate.com/en/articles/5590902
- Avionté — homepage: https://www.avionte.com/
- Avionté — Payroll & Billing: https://www.avionte.com/payroll-billing/
- JobAdder — Features index: https://jobadder.com/features/
- JobAdder — Temporary Recruitment: https://jobadder.com/temporary-recruitment/
- JobAdder — Placement Management: https://jobadder.com/placement-management/

Research date: 2026-09-08.

> Source-access limitation: vendor help centers for Bullhorn (help.bullhorn.com), Avionté (support.avionte.com), and JobAdder (support.jobadder.com — one transport error, not retried) were not deeply fetched; Crelate's help center was reachable at article level. Claims about Bullhorn/Avionté/JobAdder rest on official product pages (Tier 2); precise operational details (stage names, numeric limits, default rates, plan gating) are not asserted. Crelate claims are Tier-1 article-backed.

## Product A — Bullhorn

### Key observations (evidence layer A unless noted)

- Positioning: "The best applicant tracking system software… for staffing agencies"; "trusted… for over 10,000 staffing firms globally"; sizes from solo desks/small agencies (plans for teams of 1–10) to enterprise; industries: Professional, Clerical & light industrial, Healthcare, Executive search.
- Product family names the industry's own three-layer division: ATS & CRM (front office), **Middle Office**, Onboarding, plus Search & Match, Automation, Reporting & Analytics, Amplify (AI).
- Middle Office page FAQ (direct vendor definition, quoted):
  - "Front office covers recruiting and sales: sourcing candidates, managing clients, and placing people in jobs."
  - "Middle office covers what happens next: time capture, pay and bill calculations, compliance checks, and invoicing."
  - "Back office covers payroll processing and financial reporting."
  - "Bullhorn's Middle Office connects front office activity to back office systems, closing the gap between a placement and a paycheck."
- Middle office mechanics observed: "time interpretation rules configured to match exact regulatory and client billing requirements"; audit checks such as "Confirm pay is below bill rate"; "compare a placement's rate card against similar active placements"; "flexible, client-specific invoicing — Configure invoices that meet individual client requirements and automate invoice generation"; "VMS integration" for time capture; "state wage rules, rate cards, and client billing structures" as the domain logic.
- Scale claims (marketing figures, recorded but not promoted): "Over 1 million workers are paid monthly through Bullhorn Middle Office" (elsewhere "1.3 million"); enterprise migration of "over 4,000 placements."
- ATS & CRM page: "Manage candidates, jobs, shifts, and clients in one platform"; CRM FAQ: "While your ATS handles candidate management and placements, the CRM helps you track sales activity, win new business, and manage your pipeline of leads"; automation includes "managing job order approvals."
- Companion products: Bullhorn Time & Expense (separate login, PeopleNet lineage), Bullhorn Talent Platform; marketplace of 300+ partners.

## Product B — Crelate

### Key observations (Tier 1 — help center)

- Core records (help-center structure): **Company** (types: Customer vs Potential Customer vs Department), **Contact** (types: Lead Contact vs Sales Contact vs Candidate), **Opportunity/Job** (the job order), **Placement**, plus Activities, Documents, Notes.
- Opportunity article (quoted): "An opportunity can signal any potential, active, or completed chance at revenue… the active job order I have for XYZ Company who is hiring for a Sales Manager… any lead or prospect for new business." → the job order is framed as a **revenue chance**, spanning BD leads → active orders → closed business.
- Placement article (quoted): "A placement in Crelate is used to indicate your 'win.' Its most frequent use case is after a candidate has accepted a role (perhaps with a signed agreement) to notate information such as the salary, pay rate, start date, fee percentage, etc. Whether or not you're placing contacts for Direct Hire, Contract or Hourly positions… Placements are ultimately intended to help you capture and report on the value your firm will accrue by having a candidate start a role for a client."
  - → placement covers **Direct Hire, Contract, Hourly**; carries pay rate AND fee percentage; the win is "candidate starts a role for a client."
- Placement machinery: Placement Grid, Placement Statuses, Placement Master Guide, placement forms, "Exporting Placement Relationships/Splits for Commissions" (recruiter split/commission accounting).
- Submittals: "Sending a Submittal Email," Submittal Templates, Submittal Items Grid, Resubmitting Candidates, branded/blinded resumes — the candidate→client presentation is a first-class record.
- Client Portal: client-side surface for requisitions, submissions, feedback; external permissions; portal workflow.
- Business Development: Sales Lead Pipeline, "Converting a Lead to an Open Job," BD workflow, MPC ("Employment Search (MPC) workflow" — most-placeable-candidate marketing to clients).
- Back office (Crelate Deliver/Hire collections — nav-level evidence, Tier 1 index):
  - **Timekeeping**: time cards, multiple entry formats, approvals, finalizing, overriding, exporting, geofencing, delivery types, time & expense types.
  - **Pay rules**: Pay Rules Master Guide, Pay Plans Setup, Assigning Pay Plans to Placements, Placement-Specific Pay Rules, OT pay plans.
  - **Payroll**: Manual Payroll (setup, running payroll, HR center/employee setup, paystub PDF/zip) and Integrated Payroll (employee center, deductions, garnishments, independent contractors, tax IDs, failed-payment handling, TPA access, pay schedules).
  - **Invoicing**: Billable Items, Billable Charge Codes, Invoicing Center, "How to Create and Send an Invoice," Invoice Templates, Billing Profile Templates, Recording Payments for Invoices, Invoice Reporting.
  - Billable Items article (quoted): "Billable items are the individual items that are claimed on invoice for a customer. All items that are invoiced through Crelate must be a billable item… They can be manually created or flow automatically from finalized Time & Expense entries… You may generate invoices by: Client, Employee & specific Job Order."
  - **Burden Rate and Burden Percentage** (advanced customization) — employer-cost loading on pay rate.
  - **Worksites** (assignment location records).
- Onboarding/compliance: Onboarding Master Guide, checklists, I-9 actions (beta), Work Authorization, W-4 state forms (Symmetry), WOTC (ADP), First Advantage background checks, Employee Portal, Compliance Center & Artifacts (artifact verification), EEOC/OFCCP tracking, GDPR management.
- VMS connectivity (quoted): "A VMS Opportunity is a system generated opportunity originating from a VMS Record. The intent here is to allow you to review the VMS created opportunity prior to transitioning this into an open requisition." VMS Center, VMS Records, VMS Pro.
- Job publishing: own job portal/careers page + syndication to Indeed/Dice/Monster/ZipRecruiter/CareerBuilder; application intake.
- Outreach: email campaigns/journaling, sequencing, SMS (RingCentral), click-to-dial; AI agents (Discover/Insights), resume parsing, Chrome extension.

## Product C — Avionté

### Key observations (Tier 2)

- Positioning: "The Staffing Intelligence Platform… connects your entire operation, front office to back office, in one intelligent platform that supports every placement, every client, and every hire."
- Platform pillars: CRM & ATS; **Payroll & Billing**; Reporting & Analytics; Mobile Experience; AI & Automation; API & Integrations; plus a VMS product ("Employer Experience — Simplify client interactions with a fully integrated VMS") and "Pay" (worker pay card, "CHANGE powered by rapid!").
- Payroll & Billing page (quoted fragments):
  - "Run the Entire Pay-to-Bill Lifecycle in One Place… captures time, processes pay, and generates invoices using data that flows directly from the work already recorded."
  - "Payroll and billing sit at the center of your agency's operations — shaping cash flow, compliance, client relationships, and the trust of your workforce."
  - Back-office blocks: "Time Capture & Assignment Data," "Payroll Processing & Pay Calculations," "Client Invoicing & Revenue Tracking."
  - FAQ: "Staffing payroll is more complex because workers may have different pay rates, assignments, locations, and schedules that change frequently. Agencies also need to connect hours worked to client billing and track gross profit."
  - FAQ: "supports high-volume processing, variable pay rates, assignment-based wages, and the connection between placements, time capture, payroll, and billing."
  - FAQ: "automated billing features that generate accurate, client-specific invoices based on approved time, rates, and custom billing rules."
  - Multi-jurisdiction: "automates tax calculations and filings across multiple states and localities"; year-end documentation.
- Scale claims (marketing, recorded not promoted): 4.6M W-2s processed annually; $15B payroll processed annually; 25k+ active users.
- Integration posture for adjacent machinery: background checks (AccuSource, Asurint…), time clocks (Timerack), tax credits (Experian), payroll funding (Scale Funding — invoice factoring for staffing), e-sign (Adobe Sign), Equifax Work Number.

## Product D — JobAdder

### Key observations (Tier 2)

- Positioning: ATS + CRM for recruiters and staffing agencies; solutions split **Permanent Recruitment / Temporary Recruitment / Recruitment and staffing agencies / In-house talent teams** (dual-sided product: agencies and in-house teams).
- Feature taxonomy includes use-case tags: "Middle office," "Temporary placement," "Business development," "Compliance," "Application management," "Database management," "Insights and reporting."
- Placement Management page:
  - "Place candidates with the right skills in the right job for the right cost."
  - Placement records; **Placement approval** ("Require Admin users or other users with permission to approve placements before they can be finalised"); e-signature for "offer letters, contracts and rates acceptance"; "Export to payroll, billing or onboarding — Sync placement data… to your payroll, billing, onboarding or HRIS platform."
  - Compliance: "Keep candidates in a pending status until their prerequisite criteria such as Documents and Notes have been met"; placement compliance errors if prerequisites missing/invalid; job compliance statuses (eligible/warning/not eligible); document expiry notifications; labour-hire document capture ("white cards, blue cards and any other tickets or licences" — Australian regime).
  - Workforce: "View working temps" on the Placements Grid; "Extend placements — Extending a Placement will produce a new Placement record… with new start and end dates"; "Convert temp to perm placement."
  - Jobs: "Create jobs from leads or requisitions"; "Job sources — Track where your Jobs are coming from, for example via business development or existing clients"; candidate matching (keyword, ranking, AI).
- Temporary Recruitment page: "Manage your entire temp desk in one place"; temp workforce visibility ("Monitor booked and working candidates, track contractors who are finishing their placements and view candidates who are available for new placements"); onboarding/hiring-kit forms; "Export placement records, export data to payroll platforms and manage shift scheduling, rostering and timesheet approvals… streamline your invoicing" — **pay/bill executed via integrations, not native**.
- Portals: Client Portal ("manage job requisitions, submissions and interview feedback"), Hiring Manager Portal, **Agency Portal** ("Manage and communicate with key agency recruitment partners through a simple vendor management system" — i.e., when JobAdder's customer is itself using sub-agencies), Candidate Portal.
- Opportunity Pipeline: "Capture, manage and oversee all your business development activity" (BD = winning new job orders/clients).
- 200+ job boards; SMS/WhatsApp outreach; email sync.

## Cross-product Comparison

| Dimension | Bullhorn | Crelate | Avionté | JobAdder |
|---|---|---|---|---|
| Client object | "clients" managed in CRM; sales pipeline for leads | Company (Customer/Potential Customer/Department) + Lead/Sales contacts | "every client"; CRM pillar | Client records + Client Portal; BD Opportunity Pipeline |
| Job order | "jobs" + "job order approvals" | Opportunity/Job = "chance at revenue"; VMS Opportunity → open requisition | assignment/job data feeding pay & bill | Job records "from leads or requisitions"; job sources |
| Candidate/submission | candidate database, search & match, tearsheets | Candidate contact type; Submittals (email/portal/grid) | candidate management in ATS | Candidate records; submissions via portal; matching |
| Placement | placements (ATS&CRM); 4,000-placement migrations | Placement = "your 'win'": salary/pay rate/start date/fee %; Direct Hire/Contract/Hourly; splits/commissions | "every placement"; placement→payroll→billing | Placement records; approval gate; extend; temp→perm |
| Pay/bill | Middle Office: time capture, pay & bill calc, compliance checks, invoicing; "pay below bill rate" checks; rate cards | Timekeeping → Billable Items → Invoices (by Client/Employee/Job Order); Pay Plans/Pay Rules; Manual+Integrated Payroll; Burden Rate | Native pay-to-bill lifecycle; gross profit tracking; multi-state tax; W-2s | Via integrations: export to payroll/billing; timesheet approvals via partners |
| Compliance | middle-office compliance checks; state-specific rules | Onboarding checklists, I-9, work auth, WOTC, artifacts, EEOC/OFCCP, GDPR | multi-jurisdiction tax; compliance checks in pay cycle | pending-until-prerequisites-met; document expiry; tickets/licences (AU) |
| Client-facing surfaces | client relationship management; (portals via ecosystem) | Client Portal (requisitions, submissions, feedback) | VMS product for employer experience | Client Portal + Hiring Manager Portal + Agency Portal |
| VMS posture | VMS integration for time capture | VMS Center ingests client VMS orders | ships its own VMS | Agency Portal (mini-VMS for sub-agencies); integrates to client VMS |
| Back-office depth | dedicated Middle Office product | native Deliver (time/pay/invoice) + Hire (payroll) | native, flagship differentiator | integration-export posture |
| Industry/size spread | small→enterprise; professional/clerical-light industrial/healthcare/exec search | mid-market staffing firms | high-volume temp/contract staffing | AU/global mid-market; perm+temp desks |

**Layer-B commonalities (cross-product):** client accounts with BD pipeline; client-owned job orders; candidate database with matching; submittal-to-client as a record; placement as the commercial win (fee or assignment); onboarding/compliance gates with document expiries; time capture → pay → client invoice chain for temp/contract; client-specific invoicing; reporting on fill/submittal/placement/GP; portals for clients (and workers); job-board syndication; VMS connectivity on both sides.

**Divergences:** back-office depth (native vs integration); whether the vendor ships a VMS (Avionté) or ingests VMS orders (Crelate) or both (Bullhorn integrates; JobAdder's Agency Portal serves the reverse seat); regional compliance flavor (US I-9/W-2/multi-state vs AU tickets/licences); AI depth.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

The **agency-side business system of record** whose world is the client–job order–candidate triangle, closed by the placement:

1. **The client account of record** — the agency's customers are client organizations that buy staffing services; the system holds them as commercial accounts (contacts, relationship history, terms) and anchors their demand. Remove → the operator becomes the employer; the product is an employer ATS.
2. **The client-owned job order** — the unit of demand: a position a client wants filled, carrying requirements and commercial terms (placement fee or pay/bill rates), owned by the agency on the client's behalf. Remove → a candidate database with no demand object.
3. **The candidate pool and the submission motion** — agency-sourced people held as records, matched against job orders, and **submitted to the client** (the submittal is the match motion made visible to the buyer). Remove → a sales CRM.
4. **The placement as the commercial outcome** — the record of the win binding candidate ↔ job order ↔ client, monetized either as a **fee-bearing direct hire** or as a **temp/contract assignment** (start/end dates, rates) that generates the recurring pay-and-bill cycle. Remove → a recruiting tracker with no revenue record.

Jointly-held is load-bearing: 1+2 without 3–4 = a sales CRM with a price list; 3+4 without 1–2 = a candidate database; the triangle is what makes it an agency system. The operator identity (a firm supplying workers to client organizations for revenue) is the posture that separates this Type from the employer-side ATS.

### L1 — Common Mature Structure

- **Client CRM / business development** — lead pipelines, account management, "converting a lead to an open job," activity/outreach tracking (email/SMS/phone), job-source attribution.
- **Sourcing & matching** — resume parsing, database search, keyword/AI matching, job-board syndication, careers/job portal.
- **Recruiting workflow** — per-job-order pipeline stages, interview scheduling, notes/activities, scorecards.
- **Submittal machinery** — submittal templates/emails/grids, branded or blinded resumes, resubmittals, client portal / hiring-manager portal with feedback.
- **Onboarding & compliance** — document capture with expiry tracking, prerequisite gates ("pending until met"), right-to-work/I-9-type checks, background checks, e-signature, certifications/licences.
- **Middle office (temp/contract staffing)** — time capture (timesheets, mobile, geofencing, clock integrations), timesheet approval, pay/bill rate checks ("pay below bill rate"), pay plans/pay rules (incl. overtime), burden/margin computation, payroll processing (pay runs, deductions, garnishments, paystubs, year-end forms), billable items → client invoices (client-specific templates, payment recording), gross-profit reporting.
- **Worker engagement** — candidate/worker portals, mobile apps, aftercare messaging.
- **Reporting & analytics** — time-to-fill, submittal/interview ratios, placements, revenue/GP, recruiter performance, KPI dashboards.
- **Integration spine** — job boards, VMS, payroll/funding providers, background checks, e-signature, HRIS/accounting.
- **AI assistance** (current generation) — matching, drafting, extraction, audit rules, chat over records.

### L2 — Variant / Optional Structure

- **Business mix** — perm/direct-hire-only desk (fee placements, no pay/bill) vs temp/contract-heavy desk (full middle office) vs blended; temp→perm conversion flows.
- **Back-office depth** — native payroll/billing in the same platform vs integration-export to specialist payroll/billing systems.
- **Industry verticals** — professional/IT, clerical & light industrial, healthcare (credentialing-heavy), executive search (retained, fee-only), hospitality/events.
- **Regional regimes** — US (I-9/E-Verify, W-2/multi-state tax, WOTC), AU/NZ (tickets/licences, labour-hire), UK/EU (right-to-work, GDPR), each shaping the compliance module.
- **Scale/structure** — solo desk → multi-branch/franchise networks; shared services back office.
- **VMS posture** — agency as supplier into client VMS programs (order ingestion, time export) vs agency shipping its own client-facing VMS/portal; sub-agency (master vendor) management.
- **Deployment** — cloud SaaS standard; legacy on-prem back offices persist in older installs.

### L3 — Vendor-specific (research notes only)

- Bullhorn: Amplify (Audit/Extract/Digital Workers), Middle Office as separately licensed product, Time & Expense (PeopleNet lineage), Automation (Herefish), Connexys/Jobscience (Salesforce lineage), Talent Platform (AbleTeams), marketplace of 300+ partners.
- Crelate: Deliver (time/billing), Hire (onboarding/payroll), Discover/Insights AI agents, MPC workflow, "Copy for LLM" docs, Compliance Center/Artifacts, VMS Pro.
- Avionté: BOLD platform, PIXEL (AI), "CHANGE powered by rapid!" worker pay, WorkN→Avionté Mobile, Scale Funding (payroll funding) partnership.
- JobAdder: Roi-AI/SmartAI, JoyAdders support branding, Agency Portal as mini-VMS, 200+ job-board network, SEEK TSC / LinkedIn RSC integrations.

## Historical / Market-Sample Check

- **Paper-era agency** (job order book/cards taken from clients, candidate card file or register, submittal slips to clients, placement fee invoices; temp desk: time cards → payroll checks + client invoices at a markup): satisfies all four L0 structures with zero digital machinery. Passed.
- **Perm-only recruitment desk** (no timesheets/payroll): satisfies L0 via fee-bearing placements; pay/bill machinery is absent but the Type is still recognizable → confirms pay/bill is **not** L0, it is the standard structure of the temp/contract form.
- **Older software-era staffing back offices** (1990s-era front/middle/back-office suites): same triangle; the front/middle/back-office division is the industry's own long-standing vocabulary (Bullhorn documents it as such today).
- No L0 item depends on cloud, AI, portals, or job-board syndication.

## Vendor-specific Findings

See L3 above. Notable single-product structures kept out of the canonical core: Bullhorn's separately licensed Middle Office/Amplify; Crelate's VMS Pro ingestion center; Avionté's shipped VMS and worker-pay card; JobAdder's Agency Portal for sub-agency management.

## Boundary Findings

| Neighbor | Seam | Test |
|---|---|---|
| **Applicant Tracking System / ATS** (§09, processed) | Operator identity + demand ownership | ATS: the employer runs its own requisitions and ends at a hire into its org. Agency system: the operator is a firm filling **client-owned** job orders; the pipeline ends at a **placement the agency monetizes**; a client CRM is bundled. Same pipeline shape, different seat. |
| **Contingent Workforce Management / VMS** (§09, processed) | Mirror image (buyer vs supplier) | VMS: buyer governs requests, selects among suppliers, approves invoices; never employs/pays workers. Agency system: the supplier side — wins the order, employs/pays the temps, bills. Direct evidence of the seam: Crelate ingests client VMS orders as "VMS Opportunities" → open requisitions; Bullhorn Middle Office integrates VMS time capture; Avionté ships its own VMS for the employer seat. |
| **Recruiting Management Platform** (§09, processed) | Center of gravity | Agency mode of dual-sided platforms covers client CRM + placements + revenue tracking; this Type's center of gravity adds the agency business operations (timesheets, pay/bill, compliance, AR). Convergence acknowledged; boundary held by center of gravity. |
| **Payroll System** (§08, processed) | One leg vs the triangle | Agency payroll exists to pay placed workers against assignments/timesheets and connect to billing (gross profit); a standalone payroll system has no job orders, placements, or clients. |
| **Employee Scheduling Platform** (§09, processed) | Downstream step | Temp coverage may involve rostering/shift scheduling (JobAdder: "shift scheduling, rostering and timesheet approvals" via partners), but scheduling is not the spine; the order→placement→pay/bill chain is. |
| **CRM (Sales)** (§07) | One face | The client CRM is one of four structures; without job orders/candidates/placements it is just a CRM. |
| **Talent Agency Management** (§27) | Different domain | Both are "agency" systems, but talent agencies manage artists' careers/engagements in entertainment; staffing agencies supply workers to employers. Different objects, money flows, and compliance regimes. |
| **Job Board / Career Site** (§09, processed) | Channel | Job-board syndication and agency job portals are intake/publishing channels feeding the job orders, not the system of record. |

"去掉什么就变成另一个 Type" judgments:
- Remove the client account + client-owned job orders (operator becomes the employer) → ATS.
- Remove the supplier-side employment/pay-bill posture (buyer governs, suppliers engage) → VMS/CWM.
- Remove placements as revenue events → candidate database / recruiting tracker.
- Remove job orders and candidates (keep clients + invoices) → services CRM / invoicing tool.

## Uncertainties

1. Exact pipeline stage vocabularies, numeric limits (submission caps, campaign limits), default rate structures, and plan gating vary by product and were not asserted (source-access limitation: Bullhorn/Avionté/JobAdder help centers not deeply fetched).
2. Whether the market fully merges "staffing agency software" and "recruitment agency software" into one category: sampled vendors serve both poles with one product; boundary held by center of gravity (agency business operations vs recruiting workflow), flagged for any future joint review.
3. Pay/bill as L0-vs-L1: resolved as L1-for-the-Type (definitional for the temp/contract variant, absent in the perm-only pole). If a future pass treats "Staffing Agency" as strictly temp/contract, the pay/bill cycle would move into L0 — recorded here as a deliberate judgment call.
4. Back-office execution split (native vs integrated) is a spectrum; JobAdder's integration posture shows the middle office can live partly outside the system of record without the Type dissolving.

## Final Synthesis

A Staffing Agency Management System is the **agency-side system of record for the staffing business**: the firm that supplies workers to client organizations runs its entire operation on it. The defining core is the client–job order–candidate triangle closed by the placement — the client account of record, the client-owned job order (demand with commercial terms), the candidate pool moved by submissions to the client, and the placement as the monetized win (fee-bearing hire or temp/contract assignment). Around that core, mature products standardize on the industry's own three-layer division: **front office** (client CRM/BD, sourcing, pipeline, submittals), **middle office** (onboarding/compliance gates, time capture, pay-and-bill calculation, client invoicing), **back office** (payroll processing, financial reporting) — with the middle office fully present in temp/contract staffing and absent in perm-only desks. The Type is the mirror image of the buyer-side VMS/contingent-workforce system and the client-side sibling of the employer ATS; the operator's identity and the placement-as-revenue-event are the discriminators.
