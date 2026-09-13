# Research Notes — Painting Contractor Management

## Research Goal

Understand what software for painting contractors actually is as an Application Type: what objects exist inside it, how a painting job flows from lead to payment, what is genuinely painting-specific versus generic small-business field-service machinery, and where its boundaries lie with neighboring Types (generic field service management, home improvement contractor management, construction estimating, CRM, invoicing).

## Initial Boundary

- Hypothesis: business-management software for painting contractors (companies selling interior/exterior painting work for residential and commercial properties), covering the lead → estimate → scheduled job → crew execution → invoice → payment lifecycle.
- Nearest neighbors: Small Business Field Service Management (generic), Home Improvement Contractor Management (broader multi-trade remodelers), Construction Estimating / Construction Project Management (commercial construction scale), Appointment-based Service Business Management (recurring-visit businesses), CRM, Invoicing Application.
- Key boundary question: is there a painting-specific signature at all, or is this just generic field-service software marketed at painters? (Product Pollution / anti-overfit check.)

## Research Questions

1. What are the core objects? (customer/contact, property, lead, estimate/quote, job, crew, work order, invoice, payment, materials/products)
2. How is a painting estimate built, and what in its structure is painting-specific? (areas, surfaces, measurements, coats, production rates, coverage, prep, products/colors)
3. How does an accepted estimate become executed work? (job creation, scheduling, crew assignment, work orders, completion)
4. How does money flow? (deposits, progress payments, final invoice, card/ACH, refunds, accounting sync)
5. What roles exist and what permissions matter?
6. Where is the boundary with generic field-service software and with construction-scale tools?

## Representative Products

Selected for market representativeness, different product philosophies, and different packaging models:

1. **PaintScout** — painting-native platform (estimating-first, painting-specific estimating machinery). Tier-1 documentation accessible (GitBook help center).
2. **Estimate Rocket** — multi-trade contractor platform (57+ trade templates including residential/commercial painting), estimating-centric. Tier-2 official product pages (help center returned 403).
3. **Jobber** — generic home-service platform with a dedicated painting-contractor vertical. Tier-2 official painting vertical page (help center and main site returned 403; content obtained via search-indexed official pages).
4. **LawnPro** — multi-vertical (lawn-care origin) platform with a painting vertical. Tier-2 official painting vertical page.
5. **FieldPulse** — generic field service management (no painting vertical) — used as a boundary anchor showing the trade-agnostic chassis.

## Sources

- PaintScout Help Center (GitBook): https://help.paintscout.com/ — full documentation index (llms.txt) fetched 2026-09-10; key articles fetched directly:
  - What is PaintScout? — https://help.paintscout.com/support/getting-started/what-is-paintscout.md
  - Understanding Production Rates — https://help.paintscout.com/support/customization/pricing-and-rates/introduction-to-production-rate-estimation.md
  - PaintScout Operations Guide — https://help.paintscout.com/support/operations/crm/paintscout-operations-guide.md
- PaintScout product/pricing pages (search-indexed): https://www.paintscout.com/ , https://www.paintscout.com/pricing , https://www.paintscout.com/painting-estimates
- Estimate Rocket: https://www.estimaterocket.com/ and https://www.estimaterocket.com/features/project-management (support.estimaterocket.com returned 403)
- Jobber painting vertical: https://www.getjobber.com/industries/painting-contractor-software (help.getjobber.com and getjobber.com root returned 403)
- LawnPro painting vertical: https://www.lawnprosoftware.com/industries/painting
- FieldPulse: https://www.fieldpulse.com/
- Research date: 2026-09-10

Source-access limitations: Jobber and Housecall Pro help centers were unreachable (403, two attempts each, then abandoned per network rule). Jobber evidence is limited to its official painting vertical page as indexed by search. Estimate Rocket's support hub was unreachable (403); evidence from official product pages only. PaintBIDDER and ServiceTitan painting pages were unreachable (transport error / 404). Assertions relying on these degraded sources are marked accordingly.

## Product A — PaintScout (painting-native)

Evidence layer: A (direct observation, Tier-1 official documentation).

### Key observations

- Self-description: "sales and estimating platform built specifically for painting contractors"; FAQ: "Most contractor tools are built for general trades... PaintScout was built specifically for painting contractors — the workflows actually match how painting businesses sell and operate."
- **Estimate as the central document.** Estimate page carries: title, status, tabs, contact info, estimate ID, date; sidebar with activity, chat, follow-ups, calculations, presentation, terms, payment settings.
- **Painting estimating structure (the signature):**
  - Estimate composed of **Areas** (rooms/spaces: "Bedroom", reusable area names) containing **surfaces/substrates** (walls, ceiling, baseboards, window frames, doors).
  - **Production rates** (time-based rates): sqft/hr, lnft/hr, hrs/item — the core pricing method ("time-based estimation": total hours × hourly rate + materials). Documented worked example: 12×15×8 bedroom, walls 432 sqft @ 85 sqft/hr, ceiling 180 sqft @ 60 sqft/hr, baseboards 54 lnft @ 25 lnft/hr, window frames 2 @ 0.5 hrs/item, door+frame 1 @ 1.5 hrs/item → 13.5 hours.
  - **Coats** as a per-substrate parameter (dropdown; "show coats" option).
  - **Prep hours** as a separate labor component per substrate.
  - **Products** (paint products) with **coverage rates** (sqft/gallon, lnft/gallon, gallons/item) → automatic material quantity calculation; product rounding configuration.
  - **Sherwin-Williams integration**: product browser and color catalogue.
  - Estimate types: Interior, Exterior, Cabinets (organize rates, terms, presentations, reporting).
  - Hourly rate configuration (labor + overhead + materials + profit in one number); sales rate metric (price ÷ hours).
- **Estimate → customer:** presentations (multi-page branded proposals), terms, sending via email/text, customer views and e-signs to accept; accept on-site; customer-accepted optional items; auto follow-ups (email/SMS) on estimate status; estimate activity log (created/sent/viewed/accepted/paid), version history, restore.
- **Estimate → production:** work orders generated for the crew (hour breakdowns, crew notes hidden from customers, hidden items shown on work orders, translation to another language); share with team.
- **Operations add-on (CRM + production):** deals with customizable pipeline stages ("from lead request through job completion"), linked estimates/invoices/contacts/tasks; **Sales Events** (estimate appointments, walkthroughs, follow-ups) on a Sales Calendar with availability and automated customer emails; **Jobs** scheduled on a **Production Calendar** with project manager and **Crew** assignment (crews have name, lead, calendar color); weather forecast in production calendar; tasks/checklists; automations moving deals through stages based on estimate/invoice status; lead forms creating contacts+deals; lead source tracking.
- **Money:** invoices created from estimates (manually or automatically on acceptance); payment requests for **deposits, progress payments, remaining balances**; card/ACH via native PaintScout Payments or Stripe; surcharging; refunds; receipts; Wisetack financing integration; QuickBooks sync.
- **Users & permissions:** Owner, Sales user, Team user, Painter user (employees and subcontractors, field workflows), custom permissions; estimate transfer on deactivation.
- **Reporting:** win rate, close rate, dollars won, estimator performance, job costing/profitability on production deals, outstanding invoices, payments, lead conversions, additional-work (change order) reports.
- Offline estimating mode; mobile web app.

## Product B — Estimate Rocket (multi-trade, estimating-centric)

Evidence layer: A for product-page claims (Tier-2 official pages); help center inaccessible.

### Key observations

- "All-in-one platform built for service contractors... trusted by contractors in 50+ trades" — trade list includes Residential Painting, Commercial Painting, plus 50+ others (roofing, landscaping, HVAC...).
- Modules: Sales & Customer Growth (estimates, proposals, automated follow-ups), Project Management (projects, crews, schedules, job costs), Invoice & Payments, Client Hub (CRM), Business Insights (25+ reports, profitability).
- Trade-specific estimating: "Ready to use templates for 57+ trades. Just measure, count, and click"; "Built-in pricing and markup tools"; estimate templates → fast-fill proposals.
- Painting-relevant language: "stay on top of colors & scopes" (painting customers quoted in testimonials: Ryan Amato Painting, First Choice Professional Painting, H.J. Holtz & Sons).
- Project management: job file holds "Photos, Notes, Emails, Messages, Estimates, Change Orders, Work Orders, Invoices, and Payments"; crew & sales schedule with drag-and-drop rescheduling; to-do tasks; time tracking (labor, travel, expenses) rolling up to projects; job costing (budget vs actuals against the estimate); work map view; user permissions; field mobile access.
- Invoicing & payments: send invoices, collect payments, track cash flow; QuickBooks Online sync; Zapier; CompanyCam photo integration; online booking integration.
- Franchise module (multi-location account management) — vendor-specific.

## Product C — Jobber (generic home-service platform, painting vertical)

Evidence layer: A for the painting vertical page's claims (Tier-2, search-indexed official page); help center inaccessible — operational details degraded.

### Key observations

- Positioning: "painting contractor software... send estimates, schedule jobs, invoice, and get paid—all in one place"; Jobber is a general home-service platform ("50+ home service industries") with a painting vertical page.
- Quote: optional line items, quote follow-ups, quote approvals, markups; "enter your job costs and markups once" with estimated margin visible.
- Schedule: drag-and-drop calendar, map and routing, progress tracking, team push notifications; reschedule/reassign jobs to painters with automatic phone notification.
- Complete job: invoicing (convert work order into invoice), invoice follow-ups, online card payments, automatic payments.
- QuickBooks Online sync; time tracking.
- No painting-specific estimating machinery visible on the vertical page (no production rates, coverage, coats) — the painting vertical is marketing packaging over the generic quote/schedule/invoice chassis.

## Product D — LawnPro (multi-vertical platform, painting vertical)

Evidence layer: A for the painting vertical page's claims (Tier-2, search-indexed official page).

### Key observations

- Lawn-care-origin platform with a painting vertical: "Quote, schedule, and finish paint jobs."
- Painting-specific features listed: "Build precise estimates by room, wall, or square footage"; "Surface-based pricing & takeoffs"; "Color & finish selections"; "Before/after & progress photos"; "Change orders & punch lists"; "Schedule crews by project phase and track progress"; "Store colors, finishes, and change orders in one thread"; estimate option sets ("premium paint, add-on trim").
- Common chassis: customer CRM, client portal, estimates/quotes → jobs, scheduling, invoicing, online payments (cards & ACH), expenses, QuickBooks Online sync, online booking/requests, calls & SMS.
- Confirms the painting signature from a second, independent vendor: surface-based takeoffs, color/finish selection, punch lists, project-phase scheduling.

## Product E — FieldPulse (generic FSM, boundary anchor)

Evidence layer: A for product-page claims (Tier-2).

### Key observations

- Generic field service management: scheduling & dispatching, work order management, job management, estimates & invoices, payments, project management, customer management/communication/portal, pricebook, custom workflows, dashboards.
- Industry solutions: HVAC, electrical, plumbing, garage door, locksmith, septic, appliance repair... — no painting vertical.
- Demonstrates the trade-agnostic chassis that painting-vertical products package: customer → estimate → scheduled job → work order → invoice → payment.

## Cross-product Comparison

| Structure | PaintScout | Estimate Rocket | Jobber (painting vertical) | LawnPro (painting vertical) | FieldPulse (generic) |
|---|---|---|---|---|---|
| Customer/contact records | Contacts & Companies | Client Hub CRM | Client management | Customer CRM | Customer Management |
| Lead capture / pipeline | Lead forms, deals, stages, lead sources | Leads, auto follow-ups | — | Online booking/requests | Lead routing (dashboard) |
| Estimate/quote as unit of sale | Estimates (areas→surfaces→rates) | Estimates + trade templates | Quotes (line items, markups, approvals) | Estimates by room/wall/sqft + options | Estimates |
| Painting estimating machinery | Production rates (sqft/hr, lnft/hr, hrs/item), coats, prep hours, coverage sqft/gallon, product library, SW catalog, estimate types (Interior/Exterior/Cabinets) | Trade templates ("measure, count, click"), colors & scopes | none visible | Surface-based pricing & takeoffs, color & finish selections | none |
| Proposal presentation & acceptance | Presentations, e-signature, accept on-site, customer chat | Branded proposals, on-spot approvals | Quote approvals | Branded quotes, client portal | Customer portal |
| Crew scheduling | Jobs on Production Calendar, crews (name/lead/color), PM assignment, weather | Crew & sales schedule, drag-drop, work map | Drag-drop calendar, routing, reassign + notifications | Schedule crews by project phase | Scheduling & dispatching |
| Crew-facing execution | Work Orders (crew notes, hours, hidden items, translation) | Work orders, photos, notes, time tracking | Work order → invoice | Progress tracking, punch lists | Work orders |
| Change orders | Additional work/change orders with approval + signature | Change orders in job file | — | Change orders | — |
| Money loop | Invoices from estimates (auto on acceptance), deposits/progress/final payment requests, card/ACH, financing, refunds | Invoices, payments, cash flow | Work order → invoice, card payments, automatic payments | Invoices, online payments (cards & ACH) | Invoices, payments |
| Job costing | Job costing on production deals | Time tracking → budget vs actuals | — | Time tracking | Job costing |
| Accounting sync | QuickBooks | QuickBooks Online | QuickBooks Online | QuickBooks Online | QuickBooks |
| Photos/media | Media on estimates/deals | Photos & notes in job file | — | Before/after & progress photos | — |
| Automated customer comms | Auto follow-ups, event emails, payment emails | Auto follow-ups | Quote/invoice follow-ups | Reminders, SMS | Customer communication |

### Reading of the comparison

- The **common chassis** across all five: customer records → estimate/quote → scheduled job with crew assignment → execution record (work order/photos/notes) → invoice → payment, plus accounting sync and automated customer communication. This is the small-business trade-contractor job economy.
- The **painting signature** appears only in products that target painting as a first-class trade (PaintScout, LawnPro's painting vertical, Estimate Rocket's painting templates): surface/area-based takeoff estimating (rooms, walls, linear trim, counted items), coats, prep, paint products with coverage, color/finish selection, punch lists, project-phase scheduling. Generic FSM (Jobber vertical page, FieldPulse) carries none of it.
- Packaging poles: painting-native (PaintScout) vs multi-trade template library (Estimate Rocket) vs generic platform with painting vertical (Jobber, LawnPro). Same job economy, different trade depth.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The painting contractor's job-economy system of record. Four jointly-held structures:

1. **Customer/property records for painting work** — identified customers (and commonly companies for commercial work) bound to the properties/sites where painting work happens. Remove → generic contact database.
2. **The estimate/quote as the unit of sale** — painting work is sold per project through a written, itemized estimate that the customer accepts (signature/approval); the accepted estimate is what becomes the job. Remove → a lead list or a calendar with no sales instrument.
3. **Scheduled crew execution of accepted work** — accepted estimates become jobs placed on a calendar and assigned to the contractor's crew(s) for execution at the property. Remove → a quoting tool with no operational follow-through.
4. **The money loop** — the accepted/completed work resolves into invoicing and recorded payment (deposits, progress payments, final balance are the characteristic rhythm). Remove → a schedule board with no economics.

Trade binding: the work being sold, scheduled, and invoiced is painting work at residential/commercial properties. Remove the binding → generic small-business field service management.

Jointly-held load-bearing checks:
- 1 alone = contact/CRM database
- 2 without 1 = anonymous quote generator
- 3 without 1+2 = calendar tool
- 4 without 1–3 = invoicing application
- 1+2 without 3 = sales pipeline with no production
- 2+3 without 1 = job tracker with no customer memory
- 1+3 without 2 = scheduling tool with no sale instrument (walk-in work)

### L1 — Common Mature Structure

- Lead capture and pipeline management (lead forms, lead sources, deal stages spanning sales and production)
- Branded proposal presentation and e-signature acceptance (including on-site acceptance)
- Work orders as the crew-facing document (scope, hours, crew notes, photos)
- Change orders / additional work with customer approval
- Photo documentation (estimate media, before/after, progress)
- Time tracking feeding job costing (budget vs actuals against the estimate)
- Payment processing (card/ACH), deposits and progress payments, payment status tracking
- Automated customer communications (follow-ups, confirmations, reminders, payment emails)
- QuickBooks / accounting sync
- Reporting: win/close rates, estimator performance, outstanding invoices, job profitability
- Mobile field access; user roles and permissions (owner / sales / office / field crew)

### L2 — Variant / Optional Structure

- **Painting-specific estimating machinery** (the painting-native pole's depth): production rates (sqft/hr, lnft/hr, hrs/item), coverage rates (sqft/gallon) with automatic material quantities, coats per substrate, prep hours, paint product libraries, color catalogs, estimate types (Interior/Exterior/Cabinets/decks/floor coatings), surface-based takeoffs. Present in painting-native and painting-vertical products; absent in generic FSM serving painters — therefore variant, not definitional.
- Residential vs commercial focus; deck/cabinet/floor-coating extensions
- Customer financing integration; surcharging; offline estimating; work-order translation; punch lists; recurring/maintenance work (rare for painting vs appointment trades)
- Packaging: standalone vs add-on modules (PaintScout Operations is a paid add-on)

### L3 — Vendor-specific (Research Notes only)

- Sherwin-Williams product browser + color catalogue + branded presentation pages (PaintScout)
- Wisetack financing (PaintScout); PaintScout Payments vs Stripe choice; sales leaderboards; 14-day weather in production calendar; work-order translation; Success Packages onboarding
- Franchise module (Estimate Rocket); CompanyCam/YouCanBookMe integrations
- ClearPath guided workflows, Operator AI dispatcher (FieldPulse)
- LawnPro's shared lawn/painting booking language ("mowing, fertilization" requests on the painting page)

## Vendor-specific Findings

See L3 above. None of these are load-bearing for the Type.

## Boundary Findings

- **vs Small Business Field Service Management (generic):** the generic Type is the trade-agnostic chassis (customer → quote → scheduled job → invoice → payment). Painting Contractor Management is the painting-trade binding of the same job economy. The decisive seam is the estimating/execution content: painting-native products carry surface-based takeoffs, coats, coverage, color/product selection, punch lists; generic FSM does not. A painting contractor running entirely on generic FSM still exercises the L0 core — which is why the painting-specific machinery is L2, not L0. Keep-both relationship (industry Variant of the trade-business family), consistent with the directory's pattern of industry-specific leaves under §29.
- **vs Home Improvement Contractor Management:** broader multi-trade remodelers (multiple trades per job, larger project structures). Painting is single-trade; the sampled painting products are built around one trade's estimate→job economy.
- **vs Construction Estimating / Construction Project Management:** construction-scale tools handle commercial construction documents, bids, schedules of value, retainage, submittals. Painting contractor software is small-business job economy: one-page estimates, deposits, crew scheduling. Different scale and object world.
- **vs Appointment-based Service Business Management (cleaning, salon, lawn recurring):** painting is project-based (one-off jobs sold via estimate and executed over days), not recurring-visit based. Recurring booking machinery is absent or peripheral in the painting sample.
- **vs CRM:** customer records exist here to drive the job economy (estimate → job → invoice), not relationship management as an end. Pipeline stages run "from lead request through job completion" — sales and production in one pipeline.
- **vs Invoicing Application:** invoicing is one leg of the money loop; the Type's center is the whole job economy.
- **"去掉什么就变成另一个 Type" 判据:** remove the painting-trade binding (surface takeoffs, paint products/colors, painting job semantics) → generic Small Business Field Service Management. Remove the job economy (keep only estimating) → Construction Estimating territory. Remove the crew/production side → a sales-estimating tool, not contractor management.

## Historical / Market-Sample Check

Would older, regional, or differently-positioned painting contractors fit the L0? A painting contractor of the paper era kept customer/job records (job folders, carbon-copy estimate books), sold work through written estimates that customers signed, scheduled crews on a wall calendar, and invoiced with payment terms and deposits. All four L0 structures hold without any modern implementation (production-rate calculators, e-signature, online payments, pipelines). The modern machinery is L1/L2. Historical check passed.

Also checked: a painting contractor running on generic FSM (Jobber) or spreadsheets still exercises the L0 core — confirming that painting-specific estimating machinery must not be placed in L0.

## Uncertainties

- Jobber's operational depth for painting (whether its quote machinery supports painting-specific structures beyond line items/markups) could not be verified — help center inaccessible. Claims about Jobber are limited to its painting vertical page.
- Estimate Rocket's painting template internals (what "measure, count, click" computes for painting specifically) could not be verified at documentation depth — support hub inaccessible.
- Market share/adoption ordering among painting-native products (PaintScout vs others like PaintBIDDER, Pricely) not established; PaintBIDDER unreachable.
- Whether commercial painting contractors (larger firms) use the same product class or move to construction-scale tools — sampled evidence is residential/small-commercial weighted.

## Final Synthesis

Painting Contractor Management is the painting contractor's job-economy system of record. Its defining core is four jointly-held structures — customer/property records, the accepted estimate as the unit of sale, scheduled crew execution, and the money loop — bound to painting work at residential/commercial properties. Around that core, mature products add the standard trade-contractor machinery (pipelines, proposals/e-signature, work orders, change orders, photos, time tracking, job costing, payments, accounting sync, automated communications). The painting-native pole adds a genuinely painting-specific estimating layer — surface-based takeoffs, production rates, coats, prep hours, paint products with coverage, color/finish selection — which is the trade's signature but a variant depth, not the definition: the same core runs on generic field-service software. Packaging poles (painting-native vs multi-trade templates vs generic platform with painting vertical) are market packaging, not Type boundaries.
