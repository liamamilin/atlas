# Research Notes — Restoration Contractor Management

Research date: 2026-09-09
Leaf: Restoration Contractor Management (DIRECTORY.md §29 Home, Family, Personal & Local Services — trade-business cluster, line 2121)
Slug: restoration-contractor-management

## Research Goal

Understand what "Restoration Contractor Management" software actually is in the real market: what objects it manages, how restoration work (water, fire/smoke, mold, storm) flows through it, what is restoration-trade-specific versus generic field-service structure, and where its boundaries lie with neighboring Application Types (generic small-business field service management, trade siblings, construction project management, insurance claims management, carrier-side compliance apps, estimating platforms, contents/pack-out tooling, environmental remediation).

Family context carried into this pass: the §29 trade-business cluster passes (fire-protection, electrical, HVAC, plumbing, garage-door, handyman, appliance-repair, locksmith, cleaning, landscaping, lawn-care, pest-control, pool-service) established a two-pole family structure — a **compliance pole** (fire protection: code-mandated recurring inspection programs, persistent deficiencies, regulator-facing reporting) and a **trade-tuned pole** (most other trades: generic FSM spine with trade content/configuration). The open questions for restoration: (1) does restoration carry any *structurally distinct* trade object, or is it a trade-tuned variant like plumbing/HVAC? (2) what is the restoration trade's own color within the family? Early hypothesis: restoration's insurance-claim economy (adjusters, carriers, TPA programs, Xactimate) might constitute a structural layer no other §29 trade has.

Naming note: the leaf is "Restoration Contractor Management"; market vocabulary is "restoration software" / "restoration management software" / "restoration job management software" (Albi's headline is literally "Restoration Management Software"; Encircle's is "Restoration Field Documentation to Estimate"). The difference is lexical, not structural.

## Initial Boundary

Working hypothesis at start:

- It is the business-management system of a property-restoration contractor — a company that responds to damage events (water intrusion, fire/smoke, mold, storm, biohazard) at buildings and restores them.
- Core objects likely: job/claim bound to a loss event at a property, field documentation (photos, notes, readings), moisture/drying machinery, scope → estimate (Xactimate), contents/pack-out, crews, invoices to carriers/adjusters.
- Trade-specific candidates to test: insurance claim as a first-class job attribute; adjuster/carrier/TPA as reviewing payers; drying-equipment and moisture-reading loops (IICRC S500); contents pack-out (inventory, storage, total loss); emergency response SLAs; CAT (catastrophe) surge operations; Xactimate as the estimating exchange standard.
- Closest neighbors: Small Business Field Service Management (family spine), Construction Project Management (reconstruction pole), Insurance Claims Management / Claims Adjuster Platform (§08, carrier/adjuster side), carrier compliance apps (MICA/Mitigate, CleanClaims — a different product class), Xactimate (estimating platform), Cleaning Business Management (routine vs post-loss cleaning), Environmental Remediation Management (§21, contamination remediation).

## Research Questions

1. What is the unit of record — job, claim, or project? How do job and claim relate?
2. What does the job file contain, and who consumes it (office, crews, adjusters, carriers, TPAs)?
3. How does work flow from loss event to payment? What are the phases (emergency response, mitigation, drying, contents, reconstruction)?
4. What is the drying/monitoring loop for water work, and is it structural or content?
5. What role does Xactimate play, and where does estimating live?
6. What is the TPA/carrier program layer, and how does it shape the software?
7. What is contents/pack-out, and is it part of this Type or a separate one?
8. Which interfaces do users actually operate (field app, office web app, adjuster-facing reports, dashboards)?
9. Historical check: would older, regional, paper-era, or general-tool-configured operations still fit a minimal definition?

## Representative Products

Selected for market representation + documentation access + different product philosophies + different customer layers:

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Encircle | documentation-first restoration platform ("field documentation to estimate"); SMB through national franchise brands (Belfor, Paul Davis, Rainbow, PuroClean, Restoration 1 logos); ships an adjuster-facing surface; deepest trade-machinery documentation (Hydro, Contents, Scope to Estimate, TPA program page) | Tier 1 (Zendesk help center, Restorers + Adjusters audiences) + Tier 2 (solution pages, TPA program page) |
| Albi (Albiware) | all-in-one restoration operations ("The Only System to Run Your Entire Restoration Business"), built by restorers; SMB | Tier 1 (HubSpot help center) + Tier 2 (feature pages) |
| Assured Software (JobCheck + PackOut + TrackIt) | restoration + contents job management built on Salesforce; contents/pack-out depth; franchise-scale; also sells to independent adjusters | Tier 2 (product pages) |

Attempted-and-abandoned per source-access rules:

- **Next Gear Solutions (DASH)** — the enterprise/claims-program-centric pole — returned empty responses twice (root + software page); abandoned.
- **iRestore** — 403 on both www and bare domain; abandoned.
- **restorationmanager.com** — fetched, but it is a *hobbyist car/bike restoration tracker* (PCW 2006 review), unrelated to the property-restoration market. Product mismatch recorded; not a sample member.
- **Xactimate / Verisk** — verisk.com program URL 404, xactimate.com 403; the estimating ecosystem is documented only through integration partners' pages (Encircle, Encircle TPA page).
- **Jobber** — 403 in prior sibling passes; not retried. The trade-agnostic pole (general FSM used by restoration companies) is therefore *inferred from the family pattern*, not directly evidenced for restoration.

## Sources

Fetched 2026-09-09:

- Encircle (Tier 2): https://www.getencircle.com/ — platform overview, solutions nav, Scope to Estimate flow, customer logos; https://www.getencircle.com/solutions/water-mitigation/ — Hydro page (S500 checklist, equipment calculator, moisture maps, psychrometrics, alerts, offline, multi-tech, "defensible drying report", compliance-app contrast, roles)
- Encircle Help Center (Tier 1): https://help.encircleapp.com/hc/en-us — Restorers + Adjusters audiences; sections: Setting Up Your First Claim, Encircle for Admins, Custom Forms, Remote Document Signatures, Photos/Videos/Notes, Scoping & Estimating, Floor Plan, Sketch, Hydro, Contents, Payments (Stripe), The Edge, Integrations; adjuster sections: Working With the Claim, Managing Contents (depreciation/tax), Creating Reports
- Encircle TPA program page (Tier 2): https://discover.getencircle.com/tpa-program/ — TPA definition, examples (Contractor Connection, Sedgwick, Alacrity Solutions), scorecard categories, common SLAs (with "programs vary" note), TPA workflow, RIA 2025 TPA Scorecard Report references
- Albiware (Tier 2): https://albiware.com/ — positioning, plan tiers (Base/Pro/Enterprise), integrations incl. Encircle; https://albiware.com/features/job-management/ — WorkBook 2.0 (dry plan, equipment, job status, reports), Field Documentation; https://albiware.com/features/business-operations/ — people/asset/financials/referrals/file management, custom sales cycle
- Albi Help Center (Tier 1): https://help.albiware.com/ — sections: Mobile App, Projects, Dashboard, Settings, Assets, Customer & Relationships, Scheduler, Staff, Payments (Albi Pay), Integrations, Communications
- Assured Software (Tier 2): https://www.assuredsoftware.com/ — JobCheck/PackOut/TrackIt products, restoration + insurance-adjuster solutions; https://www.assuredsoftware.com/job-check/ — claim notifications, insurance/adjuster/loss/claim info, job feed, workflow engine, Daily Digest, Milestone Performance Chart, dispatch mapping, budgeting, referrals & programs dashboards, non-salvage replacement pricing, QuickBooks Desktop

Family counterparty sources (prior sibling passes): research/plumbing-business-management.md, research/hvac-service-management.md, research/fire-protection-service-management.md, research/electrical-service-management.md, research/garage-door-service-management.md, research/handyman-business-management.md, research/appliance-repair-management.md, research/locksmith-business-management.md, research/cleaning-business-management.md, research/flooring-contractor-management.md, research/home-improvement-contractor-management.md.

## Product A — Encircle

### Key observations (evidence layer A unless noted)

- Positioning: "Restoration Field Documentation to Estimate"; "The most trusted way to document a job now writes the estimate too"; "Trusted by 3,000+ restoration shops". Customer logos are national restoration brands (BELFOR, Paul Davis, Rainbow Restoration, PuroClean, Restoration 1, Rytech, AdvantaClean, First Onsite) plus independents — the product spans SMB to large franchise systems.
- Solution set: Field Documentation (photos, videos, 360°, notes — "automatically labeled and organized by room"); Reports ("Automatically generated, carrier-ready"); Floor Plan (2D digital floor plans from a smartphone walk); Scoping and Estimating (AI-generated scope → Xactimate); Water Mitigation / Hydro (drying logs, moisture maps); Office Admin Tools (payments, e-signatures, forms); Contents (inventory, AI descriptions, packouts); ROM / The Edge (production and labor rate — Rough Order of Magnitude estimates).
- **The claim is the job's frame.** Help center has two first-class audiences: **Restorers** and **Adjusters**. Restorer section "Setting Up Your First Claim" — "Learn the basics of setting up a job within the Encircle app" (job = claim setup). Adjuster sections: "Working With the Claim" (add claims, request photos from the policyholder, manage claim media), "Managing Contents" (edit items, price items, manage depreciation and tax), "Creating Reports" (PDF and Excel). The adjuster is a served *user*, not just a report recipient.
- **Hydro (water mitigation)** — the trade's signature machinery, documented in depth: "guides field teams through an S500 checklist"; instant reading capture (photo of moisture meter → OCR extracts Temperature/Relative Humidity into the drying log); "S500 equipment calculator" (air mover and dehumidifier requirements computed from IICRC S500 standard + drying-chamber conditions — "a defensible number for your invoice"); moisture mapping and psychrometrics (moisture points, drying equipment on the map; automatic dew point and vapor pressure calculation; alerts "if drying conditions aren't being met"); guided workflows ("a drying expert in your pocket"); fully offline capture with sync; multiple technicians on the same file simultaneously. "Defensible drying report" = moisture maps + psychrometric readings + equipment calculations + time-stamped meter photos.
- **The documentation-for-billing economy, stated outright**: "You can't bill for what you can't prove"; "Invoices get scrubbed when drying data is incomplete"; failure modes listed: "Data gets faked / Readings get lost / Equipment gets left off the invoice / Scrubbed estimates due to lack of justification". Roles named: Field Tech, Project Manager ("monitor the drying progress of every job from your desk… know when to pull equipment"), Business Owner ("defend your margins").
- **Carrier compliance apps as a distinct contrast class**: "When technicians are forced to use clunky 'compliance' apps built for insurance carriers, critical data falls through the cracks" — named: Mitigate (Mica) ("built for insurance carriers to audit your data"), CleanClaims ("enforces strict, linear workflows"). FAQ: "some carriers mandate specific compliance tools" — restorers use Encircle as the primary field tool and enter data into MICA/Mitigate where required. This documents a separate carrier-side product class from the contractor side.
- **Scope to Estimate flow**: Describe → Document (photos, video, 360°, moisture readings, sketches, contents — offline) → Scope ("Encircle AI turns your field data into an IICRC-aligned mitigation scope"; "project narrative, room by room tasks, and IICRC aligned justification for every line item") → Send ("scope and floor plan straight to Xactimate in one click… first-draft estimate, sketch, room-by-room and project-level line items") → Review (estimator reviews and approves).
- **Contents**: "Document, pack out, track and price damaged personal property in one pass, then generate a schedule of loss report your adjuster can approve without back-and-forth."
- **TPA program page** (the program-work layer, documented by a vendor): "A Third-Party Administrator (TPA) acts as a middle layer between insurance carriers and restoration contractors. They assign jobs, set expectations, and manage compliance." Examples: Contractor Connection, Sedgwick, Alacrity Solutions. TPA scorecard categories: Quality & Accuracy (estimate revisions/supplements, reinspection rates, file documentation quality), Customer Experience (post-job surveys, complaint rates), Review + approvals (time to accept assignment, time to first contact, time to first inspection, estimate upload time, total job cycle time), Compliance & Engagement (adherence to guidelines — pricing, line items, documentation; "use of required technology (portals, mobile apps, Xactimate)"; timeliness on milestone updates). Common SLAs (published with an explicit "programs vary" note): first customer contact within 1 hour, site inspection within 4 hours, initial job documentation within 12 hours, daily job status updates, initial estimate submission within 3–5 days. TPA workflow: claim reported & assigned → first contact & site visit within SLA → documentation & estimate → review & approval → work completed & payment → Q/A & scorecard update ("your performance impacts future assignments").
- CAT resources nav item (catastrophe response is a recognized operating mode). IICRC credits program (trade-standard alignment as vendor marketing).
- Marketing claims (kept out of canonical doc): 4x faster documentation, 90–95% scope completeness, 10–25% claim profitability, 10% fewer carrier disputes, 5–8% higher revenue per job, #1 ROI in C&R State of the Industry Report 2023/2024.

## Product B — Albi (Albiware)

### Key observations (evidence layer A)

- Positioning: "Restoration Management Software — The Only System to Run Your Entire Restoration Business"; origin story: "As restorers, we felt the same way and created Albi – a restoration management software that combines all your core business functions in one easy-to-use platform."
- Plan tiers name the trade's base machinery: **Base** — Photo Documentation, Mobile Scheduler, E-Signatures, **Equipment Scanning**, Timeclock, **Moisture Mapping**; **Pro** — Call Tracking & Recording, Analytics, Financials; **Enterprise** — onboarding/support tiers. Moisture mapping and equipment scanning are base-tier restoration features, not add-ons.
- **WorkBook 2.0** (job management): "Easily create a **dry plan** out in the field, keep track of **equipment**, effortlessly track **job status**, view critical data points, and simplify the process of sending **detailed reports to all parties**." Field Documentation: "signing of documents, taking of photos, creation of **moisture maps**, and documentation of correspondence while in the field."
- Help center structure (Tier 1): **Projects** ("Manage all your jobs from start to finish. Track progress, update job details, upload documents, and collaborate with your team in one central hub"), Mobile App, Dashboard (real-time metrics/KPIs), Settings (permissions/configurations), **Assets** ("Track and manage equipment, vehicles, and other company assets"), Customer & Relationships (CRM — organizations and contacts, activities, notes), Scheduler ("Schedule jobs, assign tasks… field and office teams in sync"), Staff (time, roles, performance), Payments (Albi Pay — deposits, transactions), Integrations, Communications.
- Business operations page: "people management, asset management, **financials, referrals**, file management, and **custom sales cycle configuration**"; features: Financial Reports, Employee Time Tracking, Asset Map Tracking, Vehicle Management; "collaborate with your team members and **subcontractors** in real-time"; "custom sales cycle configuration, allowing you to tailor the software to your specific business needs… each stage of your restoration projects."
- **Integrations include Encircle** — the documentation-first platform is a listed integration of the ops-first platform: the market itself treats field documentation and business operations as complementary layers that can be bought separately. Other integrations: QuickBooks (Online + Desktop), Xero, CompanyCam, Kahi, Twilio, SendGrid, Mailchimp, Zapier, Gmail.
- Marketing claims (kept out of canonical doc): 7-minute support response, 24-hour resolution, 30-day onboarding, "thousands of restorers worldwide."

## Product C — Assured Software (JobCheck + PackOut + TrackIt)

### Key observations (evidence layer A)

- Positioning: "a restoration and contents job management platform that's built on Salesforce® Cloud"; "job management for any-size restoration company"; scalable "perfect for any-size franchise."
- **JobCheck (job management)**: "New claim notifications"; "Real-time visibility into claims/job information relating to **Insurance, adjuster, loss and claim information**" — the claim/adjuster/loss context is a named part of the job file. Job feed: technicians text each other inside the job file, with photos/documentation, time-and-date-stamped. Custom workflow engine: "when a PackOut is completed, your crew simply taps it complete… JobCheck automatically assigns the task to the person responsible to schedule the contents pick up" — stage-triggered task assignment across emergency, reconstruction, and restoration jobs. Daily Digest email of completed tasks and overdue milestones. **Milestone Performance Chart** — "which stages and which jobs are behind schedule" (production meetings organized around it). Dispatch mapping: interactive job map + scheduler; crew assignment creates calendar events and puts the member on the job. Budgeting: "worksheets turn your estimates and work orders into plans"; compare plans to actuals via QuickBooks import. **"Owner dashboards identify leading referrals & programs"** — referral sources and programs (carriers/TPAs/franchise programs) are CRM-level objects. "Seamless sharing of **non-salvage items for replacement pricing**." Contents lists and CRM for contents jobs. QuickBooks Desktop integration. Mobile app with task notifications.
- **PackOut (contents)**: "Standardize your listing process; Retrieve, store, restore jobs quickly"; "PackOut screens standardize the process of listing"; "Items automatically organized by room"; "PackOut app reads **barcode tags on items and boxes**". Insurance-adjuster solution: "Adjusters can process payments faster with our detailed image-based reports produced using Assured PackOut." Testimonials name "inventory lists and **total loss reports**" as the job coordinator's output.
- Solutions for: Restoration Contractors **and Independent Adjusters** — the adjuster again appears as a served audience.
- TrackIt — third product (asset/equipment tracking per nav; detail page not fetched).

## Cross-product Comparison

| Structure / capability | Encircle | Albi | Assured JobCheck/PackOut | Assessment |
|---|---|---|---|---|
| Loss-driven job as unit of record (job = claim setup) | ✓ ("Setting Up Your First Claim" = job setup; adjuster claim tools) | ✓ (Projects; custom sales-cycle stages) | ✓ (new claim notifications; insurance/adjuster/loss/claim info in job file) | Universal — core |
| Field documentation (photos/notes/e-sign/forms, room-organized) | ✓✓ (core product; offline; 360°; auto-labeling) | ✓ (Photo Documentation base tier; Field Documentation) | ✓ (photos/notes/documentation in job file) | Universal — core |
| Claim/payer context on the job | ✓✓ (carrier-ready reports; adjuster audience; TPA page) | ✓ (referrals; reports "to all parties"; financials) | ✓✓ (explicit insurance/adjuster/loss/claim fields; referrals & programs dashboards) | Universal — core |
| Water-loss drying machinery (readings, moisture maps, equipment calc, drying logs) | ✓✓ (Hydro: S500 checklist, OCR readings, equipment calculator, psychrometrics, alerts) | ✓ (Moisture Mapping + Equipment Scanning base tier; dry plan in WorkBook) | — (not on fetched pages) | Common; signature trade machinery (2/3 explicit) |
| Contents / pack-out (inventory, tagging, storage, total loss) | ✓ (Contents: inventory, packouts, schedule of loss) | — (not named on fetched pages; Kahi integration) | ✓✓ (PackOut product: barcode tags, room organization, total loss reports, replacement pricing) | Common; dedicated modules where present |
| Xactimate estimating exchange | ✓✓ (Scope to Estimate: send scope + floor plan to Xactimate) | — (not on fetched pages) | — (not on fetched pages) | Common; ecosystem-standard (TPA required-technology lists name Xactimate) |
| Job statuses / milestones / stage workflows | ✓ (guided workflows, alerts) | ✓ (custom sales cycle; Automations) | ✓✓ (workflow engine; Milestone Performance Chart; Daily Digest) | Universal — standard |
| Crew scheduling / dispatch | ✓ (Mobile Scheduler) | ✓ (Scheduler) | ✓ (dispatch mapping + scheduler) | Universal — standard |
| In-file team communication | ✓ (multi-tech same file) | ✓ (Communications) | ✓✓ (job feed with time/date stamps) | Universal — standard |
| CRM with referral sources / programs | ✓ (light; office admin tools) | ✓ (CRM; referrals in business ops) | ✓ (CRM; "leading referrals & programs" dashboards) | Universal — standard |
| Equipment / asset tracking | ✓ (equipment readings; equipment calculator) | ✓ (Assets: equipment, vehicles; asset map) | ✓ (TrackIt product) | Universal — standard |
| Carrier/adjuster-facing reports | ✓✓ ("carrier-ready"; defensible drying report; schedule of loss) | ✓ ("detailed reports to all parties") | ✓✓ (image-based reports adjusters "process payments" with) | Universal — core |
| Payments / e-signatures | ✓ (Stripe; e-signatures; forms) | ✓ (Albi Pay; e-signatures) | — (not on fetched pages) | Common |
| Accounting sync | — (not on fetched pages) | ✓ (QuickBooks Online/Desktop, Xero) | ✓ (QuickBooks Desktop) | Common |
| Dashboards / reporting | ✓ (office admin; field metrics health check) | ✓ (Dashboard; Analytics; Financial Reports) | ✓ (owner dashboards; profitability tracking) | Universal — standard |
| TPA / carrier program layer | ✓✓ (dedicated TPA page: scorecards, SLAs, workflow; CAT resources) | — (not on fetched pages) | — (franchise "programs" in dashboards) | Variant; business-model layer (program contractors) |
| Adjuster as served user | ✓✓ (adjuster help-center audience; adjusters add claims, price contents) | — | ✓ (independent-adjuster solution page) | Distinctive of the Type; not universal |
| AI assistance | ✓✓ (AI scope generation, OCR reading capture, AI content descriptions) | ✓ (Albi AI) | — | Optional; era-typical |
| Subcontractor collaboration | — | ✓ (business ops page) | — | Optional |
| Budgeting / job costing | — (ROM estimating present) | ✓ (Financials) | ✓ (budgeting worksheets, plans vs actuals) | Common; reconstruction pole |

### What is actually restoration-specific (across sample)

1. **The loss event + claim context as the job's frame** — every sampled product anchors the job to a damage event and carries insurance/adjuster/loss/claim information on the job file (Encircle: claim setup = job setup, adjuster audience; Assured: explicit claim/adjuster/loss fields and claim notifications; Albi: projects with referral/financial context). No other §29 trade binds its job file to a third-party payer's claim. [Layer A ×3]
2. **The evidentiary documentation economy** — the job file is built to justify scope and cost to a reviewing party: "carrier-ready" reports, "defensible drying report", schedule of loss, image-based reports adjusters pay from; the stated failure mode is the scrubbed invoice. [Layer A ×3; Encircle states the economy explicitly]
3. **The drying/monitoring loop for water work** — moisture/psychrometric readings over repeated monitoring visits, drying logs, moisture maps, drying-chamber equipment calculation aligned to the IICRC S500 standard, alerts when conditions stall, equipment placement/tracking. Explicit at 2/3 sampled products (Encircle Hydro deepest; Albi base-tier moisture mapping + equipment scanning + dry plan); Assured's fetched pages silent. [Layer A ×2 explicit; trade signature]
4. **Contents / pack-out as a first-class work stream** — itemized inventory (room-organized, barcode/QR-tagged), pack-out/pack-back tracking, cleaning/storage, total-loss vs salvage determination, replacement pricing for non-salvageable items, schedule-of-loss/contents reports for adjusters. Dedicated modules at 2/3 (Encircle Contents, Assured PackOut — the latter a standalone product feeding job files). [Layer A ×2]
5. **Xactimate as the estimating exchange standard** — scope/floor-plan hand-off into Xactimate (Encircle's Scope to Estimate); Xactimate named in TPA required-technology lists. The estimate lives in an external industry-standard tool; the management product feeds it. [Layer A ×1 direct + TPA page; Layer B ecosystem]
6. **The TPA/carrier program layer** — program work arrives as assigned claims with SLA clocks (first contact, site inspection, documentation upload, estimate submission), scorecard metrics (cycle times, documentation quality, guideline adherence, required technology), and review-then-payment. Documented in depth by Encircle's program page; franchise "programs" visible in Assured dashboards. [Layer A ×1 deep + ×1 partial]
7. **Emergency/loss-response entry** — new-claim notifications, response-time SLAs, daily status updates during drying. [Layer A ×3]

No sampled product is a *pure* trade-tuned clone of a generic FSM product: even the ops-first product (Albi) ships moisture mapping and equipment scanning in its base tier, and the job-management product (Assured) carries claim/adjuster/loss fields as named job-file content. The restoration-specific layer is structural, not configuration.

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

1. **The loss-driven restoration job as the unit of record** — a job responding to a damage event (water, fire/smoke, mold, storm) at a customer's property, carried from loss response through mitigation and (commonly) reconstruction to completion; the job anchors documentation, scheduling, and billing.
2. **The evidentiary job file** — field-captured documentation (photos, notes, readings, sketches/floor plans, scope, contents) organized on the job as the defensible record of the loss and the work performed; the file exists to justify the scope and the cost to a reviewing party.
3. **The payer-review payment path** — the job carries its payer context — commonly an insurance claim with carrier/adjuster/loss details, and in program work a TPA assignment with response-time and documentation obligations — and payment follows review/approval of the documented file rather than a simple point-of-sale transaction.

Remove the loss-event job → generic field service or construction tracking. Remove the evidentiary file → a claim tracker that cannot defend invoices (the trade's central failure mode). Remove the payer-review path → a field-documentation app or generic FSM; the claim/payer economy is what makes the Type restoration-specific rather than a configured generic tool. Jointly-held load-bearing: 1 alone = generic FSM job; 2 without 1 = standalone photo/documentation app; 3 without 1+2 = carrier-side claims tooling (Insurance Claims Management territory); 1+2 without 3 = trade-agnostic field documentation; 1+3 without 2 = claim administration without execution evidence; 2+3 without 1 = claims paperwork with no job being run.

Historical check: a paper-era restoration contractor (job tickets keyed to claims, a photo file and moisture-reading log sheets per job, Xactimate-era or handwritten estimates, contents on paper tags, invoices mailed to carriers/adjusters for review) satisfies all three properties. 1990s–2000s desktop restoration products satisfy them. A restoration company running a general field-service tool with disciplined file hygiene satisfies them. None of the modern machinery (mobile apps, OCR, AI scope generation, offline sync, dashboards) is definitional. The check passes.

### Level 1 — Common Mature Structure

- Mobile field app with offline capture: photos, videos, 360°, notes (auto-organized by room), e-signatures, custom forms
- Water-loss machinery: moisture-content and psychrometric readings (temperature/RH, dew point, vapor pressure), drying logs across monitoring visits, moisture maps with drying equipment placed on them, drying-chamber equipment calculation aligned to the IICRC S500 standard, alerts when drying conditions stall
- Floor plans / sketches captured on site
- Scope → estimate flow into Xactimate (the industry-standard estimating exchange); ROM (rough-order-of-magnitude) estimating in some products
- Contents / pack-out: itemized inventory organized by room, commonly barcode/QR-tagged items and boxes; pack-out/pack-back tracking; cleaning/storage status; pricing; total-loss vs salvage determination; replacement pricing for non-salvageable items; schedule-of-loss and contents reports
- Job milestones/statuses with configurable stage workflows; automated task assignment on stage completion; in-file team communication (job feed) with time/date stamps
- Crew scheduling and dispatch; time tracking
- Carrier/adjuster-facing report generation (documentation report, drying report, contents/total-loss reports)
- CRM with referral sources and programs (carriers, TPAs, agents, property managers, franchise programs)
- Payments and e-signature collection; accounting sync (QuickBooks in the North American market)
- Dashboards/reporting: job progress, milestone performance, profitability, referral-source performance

### Level 2 — Variant / Optional Structure

- TPA/carrier program operations: SLA clocks, scorecard metrics, program-portal uploads, required-technology compliance (portals, mobile apps, Xactimate), estimate revisions/reinspections
- CAT (catastrophe) event response: storm/hurricane surge operations
- Reconstruction-phase project machinery: budgets vs actuals, phase billing, subcontractor coordination
- Carrier-mandated compliance apps (MICA/Mitigate, CleanClaims) as companion tools the contractor also feeds — a separate product class
- Franchise / multi-location structures; adjuster-side surfaces (some products serve independent adjusters directly)
- AI assistance: OCR reading capture, AI content descriptions, AI scope generation
- Payments/financing; payroll; vehicle management; equipment rental billing

### Level 3 — Vendor-specific (kept out of the canonical document)

- Encircle: Hydro (S500 equipment calculator, instant reading capture OCR), Scope to Estimate, The Edge (ROM), Encircle AI, adjuster-side product surface (adjusters add claims, request photos, price contents with depreciation/tax), IICRC credits program, TPA readiness quiz, "Documentation Excellence" workshop, Field Metrics health check, pricing claims (4x documentation, 90–95% scope completeness, 10–25% claim profitability, 10% fewer carrier disputes, 5–8% revenue), 3,000+ shops claim, not-seat-based pricing
- Albi: WorkBook 2.0 (dry plan), Albi Pay, Albi Capture (floor plans), Albi AI, Albi Analytics, Albi Automations, Base/Pro/Enterprise tiers, 7-minute support response / 24-hour resolution / 30-day onboarding claims, "built by restorers" origin
- Assured: JobCheck (job feed, Daily Digest, Milestone Performance Chart, dispatch mapping, budgeting worksheets, QuickBooks Desktop), PackOut (barcode tags, room organization, total loss reports), TrackIt, Salesforce platform basis, independent-adjuster solution page, "any-size franchise" positioning

## Vendor-specific Findings

See Level 3. Notable patterns: the market has (at least) two product shapes — **documentation-first** (Encircle: the field record is the product, estimate generation built on it, adjuster-facing surface included) and **operations-first** (Albi: full business run — CRM, scheduler, financials, assets — with trade machinery in the base tier); Assured sits between with job management + a dedicated contents product. That Albi lists Encircle as an integration shows the two shapes coexist as complementary layers in real stacks. Encircle is the only sampled vendor documenting the TPA program layer and the carrier-compliance-app contrast in depth; Assured is the only one with a dedicated pack-out product and an independent-adjuster solution page.

## Rejected Findings

1. **"Restoration Contractor Management = generic FSM with a restoration label"** — rejected as the whole story: the claim/payer spine, the evidentiary file, the drying loop, and the contents stream are structural objects in every sampled product, not configuration. (The trade-agnostic pole — a general FSM tool used by a restoration company — likely exists per the family pattern, but was not directly evidenced for restoration this pass; recorded as uncertainty.)
2. **"Restoration management = insurance claims management"** — rejected: the seat is the contractor executing the work; claim administration is carrier-side (§08 Insurance Claims Management). The claim object appears on both sides with different ownership and different jobs.
3. **Carrier compliance apps (MICA/Mitigate, CleanClaims) as this Type** — rejected: built for carriers to audit contractor files; restoration products position against them and feed them where mandated. A distinct product class at the boundary.
4. **Xactimate as this Type** — rejected: an external estimating platform (Verisk); estimating is a capability here, realized as scope/quantity hand-off into Xactimate. Same rejection pattern as the plumbing pass's "solo plumbing estimating software."
5. **"Restoration Manager" (restorationmanager.com)** — product mismatch: a hobbyist car/bike restoration tracker (parts tagging, jobs lists), unrelated to the property-restoration market. Not a sample member; noted to prevent future confusion.
6. **Contents/pack-out as a separate Application Type** — held inside this Type: pack-out is a work stream of restoration jobs (Assured ships it as a sibling product, but its output feeds the job file and adjuster reports). No evidence of a contents-management market outside restoration.
7. **"Restoration = cleaning + construction"** — rejected: neither routine cleaning (§29 Cleaning Business Management: recurring, direct-pay, no loss file) nor voluntary improvement construction (§29 Home Improvement Contractor Management) carries the loss-event + payer-review structure.

## Boundary Findings

1. **vs Small Business Field Service Management (§29 sibling, unprocessed)** — the family question returns, but restoration is *not* a pure trade-tuned variant: it carries structurally distinct objects (claim/payer context on the job, the evidentiary file as a load-bearing structure, the drying loop, the contents stream). The generic-FSM spine (customer + location, job lifecycle, crew coordination, invoice) is present underneath, but the restoration-specific layer is thicker than plumbing/HVAC-style trade tuning. Joint review should treat restoration as a structurally distinct member of the family, not a configured clone.
2. **vs the §29 trade-tuned siblings (plumbing, HVAC, electrical, …)** — same family spine, but restoration's job file is built for a third-party reviewing payer; plumbing's file is built for the customer and the office. Restoration also lacks the other trades' replacement-product-sale economy (good-better-best proposals to homeowners) — its money conversation is with an adjuster.
3. **vs Fire Protection Service Management (§29)** — the compliance-pole sibling. Both face an external reviewing party, but fire protection's gate is *code-mandated recurring inspection* (regulator-facing), restoration's is *payer review of a loss file* (carrier/TPA-facing). Restoration sits between the family's two poles: externally governed by contract (program SLAs/scorecards), not by law.
4. **vs Construction Project Management (§17)** — the reconstruction phase drifts toward project machinery (budgets vs actuals, phase billing, subcontractors — present at Albi/Assured); the restoration center remains the loss job + evidentiary file. Drift, not identity.
5. **vs Insurance Claims Management (§08)** — carrier/payer-side claim administration vs contractor-side job execution. The claim is the shared object across the seam; ownership and workflow differ.
6. **vs Claims Adjuster Platform (§08)** — adjuster-side workbench vs contractor-side management. Encircle and Assured ship adjuster-facing surfaces (adjusters as served users), which tightens but does not erase the seam: the Type's seat is the contractor.
7. **vs carrier compliance apps (MICA/Mitigate, CleanClaims)** — carrier-mandated field-audit tools; a distinct product class documented from the contractor side (Encircle's comparison pages). Restoration management products are the contractor's primary field system; compliance apps are the carrier's audit surface.
8. **vs Xactimate / estimating platforms** — the estimate lives in an external industry-standard tool; this Type feeds it (scope, floor plans, quantities) and receives approved amounts back. Estimating capability ≠ business management.
9. **vs Cleaning Business Management (§29)** — routine recurring cleaning (direct-pay, no loss file, no payer review) vs post-loss remediation/cleaning (loss-driven, documented, claim-funded). Fire/smoke cleaning and mold remediation belong here; janitorial recurrence does not.
10. **vs Environmental Remediation Management (§21)** — environmental-sector contamination remediation (site-scale, regulatory) vs property restoration (building-scale, insurance). Mold remediation sits near this boundary; in sampled products it appears as restoration job content, not a regulatory program.
11. **vs CMMS / Enterprise Asset Management (§16)** — equipment tracking here manages the *contractor's own* drying equipment and vehicles (deployment, readings, return), not customer-owned assets or maintained plant.
12. **vs Property Maintenance Management (§17) / Home Improvement Contractor Management (§29)** — property managers coordinate portfolios; home-improvement contractors run voluntary improvement work. Restoration is loss-driven with payer review; a property manager or carrier is the counterpart, not the seat.
13. **vs Local Service Marketplace (§29)** — demand-side discovery vs operator-side execution; in restoration, assignment often flows *from* carriers/TPAs rather than from consumer discovery — the referral-source CRM object reflects this.

## Uncertainties

1. **Enterprise/claims-program pole under-sampled** — DASH (Next Gear Solutions) and iRestore unreachable (empty responses / 403 ×2). The sample is calibrated to three products; the claims-program-centric enterprise shape (deep TPA/XactAnalysis integration) is evidenced only indirectly (Encircle's TPA page, Assured's program dashboards).
2. **Xactimate/XactAnalysis official documentation unreachable** (404/403) — Xactimate's role is documented only through integration partners' pages and the TPA required-technology list. Its internal workflow is not characterized here.
3. **TPA SLA figures** (1h contact / 4h inspection / 12h documentation / daily updates / 3–5 day estimate) are Encircle's published illustrative values, explicitly annotated "programs vary"; not claimed as universal.
4. **Trade-agnostic pole for restoration** — Jobber (403 in prior passes) not retried; whether general FSM products actively market a restoration configuration could not be verified. The family pattern suggests they do; asserted nowhere in the canonical document.
5. **Drying machinery at Assured** — not on fetched pages; may exist deeper in the product. The drying loop is asserted as common (2/3 explicit), not universal.
6. **Regional markets** — the sample is North America–dominant (Xactimate, TPA programs, IICRC S500, QuickBooks). Regional variance (e.g., European restoration markets, different estimating standards) could not be verified; the canonical document avoids region-specific claims.
7. **Mold/biohazard regulatory machinery** — mold remediation often carries regulatory/licensing obligations; no fetched source documents any license/permit/regulatory-program object. Not claimed in either direction.
8. **Reconstruction-phase depth** — budgeting/phase machinery observed at Albi (financials) and Assured (budgeting worksheets) but not deeply documented; the reconstruction pole's project machinery is held at variant level.

## Final Synthesis

Restoration Contractor Management is the restoration contractor's business system of record: it anchors each job to a loss event at a property, builds an evidentiary file — photos, notes, moisture readings, floor plans, scope, contents — that justifies the work and its cost to a reviewing payer, coordinates crews through loss response, mitigation, drying, contents, and reconstruction, and converts the reviewed file into payment. Its defining core is the field-service spine (customer + property, job lifecycle, crew coordination, billing) *plus* a structural layer no other §29 trade carries: the claim-bound, payer-review economy — insurance/adjuster/loss/claim context on the job, TPA program assignments with SLA clocks and scorecards, and documentation whose explicit purpose is to survive adjuster scrutiny ("you can't bill for what you can't prove"). The trade's signature machinery is the drying loop (S500-aligned readings, moisture maps, equipment calculation) and the contents/pack-out stream (tagged inventories, total-loss reports); its estimating exchange standard is Xactimate. The market realizes the Type in (at least) two product shapes — documentation-first and operations-first — which coexist as complementary layers in real stacks. The leaf is a structurally distinct member of the §29 field-service family: not a compliance-pole trade (no code-mandated program object), but not a pure trade-tuned variant either — the payer-review layer is its own structure, and it is what makes restoration restoration.
