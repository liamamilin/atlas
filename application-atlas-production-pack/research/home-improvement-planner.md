# Research Notes — Home Improvement Planner

Leaf: Home Improvement Planner (DIRECTORY.md §29 Home, Family, Personal & Local Services — home/family cluster, between Home Maintenance Application and Smart Home Platform)
Slug: home-improvement-planner
Research date: 2026-09-08
Methodology: v1.1

## Research Goal

Understand what "Home Improvement Planner" software actually is in the real market: what the homeowner plans, what objects exist inside such an application, how planning flows into hiring and execution, what money machinery it carries, and where its boundaries lie — especially against Home Improvement Contractor Management (§29 sibling, processed), Home Maintenance Application and Home Management Application (§29 siblings, unprocessed), spatial design tools, home-service marketplaces, and generic project management / budgeting.

## Initial Boundary

Working hypothesis going in: a consumer-side application for planning improvement/renovation work on one's own home — scope, budget, ideas, hiring, tracking.

Nearest types identified up front:

- Home Improvement Contractor Management (§29 sibling, processed) — the contractor's business system; the sibling pass explicitly recorded this leaf as "consumer-side planning of one's own improvement project vs the contractor's business system. Different subject of record."
- Home Maintenance Application (§29 sibling, unprocessed) — recurring upkeep vs bounded improvement work.
- Home Management Application (§29 sibling, unprocessed) — whole-home hub; the family-organizer pass left a center-of-gravity note (premises-centered vs people-centered).
- Project Management Application (§03.07) — generic team project machinery.
- Budgeting Application (§08) — whole-finances budgeting.
- Travel Itinerary Planner (§26, unprocessed) — the same "consumer planner of a bounded real-world effort" pattern in another domain.
- Spatial design tools (floor plan / 3D home design; no dedicated directory leaf; nearest is Architecture Design Application §16).
- Home Services Marketplace / Local Service Marketplace (§29) — the hiring leg.

Open question for this pass: does Home Improvement Planner have a defining structure of its own, or is it (a) a consumer Variant of generic Project Management, (b) a fragment of Home Improvement Contractor Management, or (c) a bundle of unrelated poles (design tools + marketplaces + binders) with no shared core?

## Research Questions

1. What is the subject of record — the home, the project, the idea collection, or the money?
2. Which planning structures exist across products: scope, money, time/tasks, ideas, hiring, logging?
3. How does the plan relate to execution — DIY vs hired pros; who holds the schedule?
4. What money machinery exists (estimates, budgets, bids, ROI, home-value linkage)?
5. What interfaces does the homeowner actually face?
6. What rules/states matter (plan revision, bid comparison, value updates, transfer on sale)?
7. Where are the exact seams vs contractor systems, maintenance apps, home-management suites, design tools, marketplaces?
8. Historical/market-sample check: would paper-era, regional, or platform-native planning practice still fit the definition?

## Representative Products

Sample (5 researched; different product philosophies and different market layers):

1. **Kukun (iHomeManager)** — estimation/value-first planner: renovation cost estimation with ROI against home value, maintenance planner, neighborhood permit data, contractor matching. US; freemium consumer product plus white-label distribution to banks/realtors.
2. **HomeBinder** — home-management binder with a dedicated Projects tab; distributed free-for-life through home inspectors, lenders, and real-estate agents. US.
3. **Planner 5D** — design-led planning: 2D/3D floor plans and visualization with mood boards and shopping-list cost estimates. Global; consumer plus professional tiers.
4. **Sweeten** — marketplace-led renovation support: post project, get matched vetted general contractors, collect and compare bids with expert guidance. US metros; free to homeowners.
5. **Dwellin** — maintenance-centered home-care log with rewards; improvements are logged, not planned. US consumer app. Sampled deliberately as the boundary anchor toward Home Maintenance Application.

Rejected during sampling (product mismatch):

- **Handoff (handoff.ai)** — AI estimating/project platform for remodelers and handymen; contractor-side. Belongs to Home Improvement Contractor Management territory, not this leaf. (handoff.com is an unrelated Figma design-system tool — name collision only.)
- **Bolster (bolsterbuilt.com)** — construction management software sold to remodelers/builders/contractors. Contractor-side; excluded.

Known category members that could not be verified this pass (see Uncertainties):

- **HomeZada** — home-management suite with a renovation-projects module; homezada.com returned 403 (www and bare), help subdomain transport error, web-archive snapshot timed out twice.
- **Houzz** — inspiration/ideabook platform with pro discovery; houzz.com returned 403; App Store page fetch geo-redirected to a store front page.
- **Block Renovation** — renovation planner (scope/design/budget/pro matching); blockrenovation.com returned 404 on both attempts (defunct or moved).

## Sources

All fetched 2026-09-08. Evidence layer recorded per observation: A = directly observed on an official source for that product; B = cross-product commonality; C = canonical inference.

- Kukun — root page (https://www.mykukun.com/), iHomeManager product page (https://mykukun.com/ihomemanager), Remodel Cost Estimator page (https://mykukun.com/Home-Renovation-Costs). (A)
- HomeBinder — root page (https://www.homebinder.com/), Knowledge Base index (https://pages.homebinder.com/knowledge-base), Homeowner Help Center (https://pages.homebinder.com/homeowner-help-center-0) — the homeowner-dashboard article is Tier-1 operational documentation. (A)
- Planner 5D — root page (https://www.planner5d.com/). (A)
- Sweeten — root page (https://www.sweeten.com/). (A)
- Dwellin — root page (https://www.dwellin.com/) and How It Works page (https://dwellin.com/app/how-it-works/). (A)
- Handoff — root page (https://handoff.ai/) — used only to establish product mismatch. (A)
- Bolster — root page (https://bolsterbuilt.com/) — used only to establish product mismatch. (A)
- Failed/abandoned per network rule: homezada.com (403 ×2, help subdomain transport error, web.archive.org timeout ×2), houzz.com (403; App Store fetch geo-redirected), blockrenovation.com (404 ×2), igoclients.com/knowledge/homebinder (404; correct KB found at pages.homebinder.com).

## Product Observations

### Kukun (iHomeManager) — estimation/value-first pole

Key observations (all A unless noted):

- Positioning: "The ultimate tool to manage and grow your home's value"; iHomeManager = "a powerful suite of data-driven home investment insight products"; homeowner claims their home by address ("Register & Claim your home free").
- **Home dashboard anchored to the user's own home**: home value estimate with value range (land value vs new-home value), PICO™ property-condition score vs neighborhood average, five-year value forecast, neighborhood comps/sales map.
- **Renovation cost estimator**: "Create estimates for dozens of projects" — a project-type catalog (kitchen, bathroom, interior paint, flooring, deck, sunroom, window replacement, garage remodel, in-law suite, electrical panel, …); "Just follow a few steps to get your remodel, addition, or expansion cost in minutes"; "Plan and customize your dream home renovation in minutes."
- **Money plan with value framing**: the estimator returns cost AND return — worked example shows per-project costs (bathroom $14,140, home office $12,750, bedroom $6,400, living room $8,950), total cost to renovate ($42,240), increase in home value ($48,365), and profit ($6,125). "See the return on investment specifically for your plan instantly, and easily run scenarios to optimize your budget and ROI."
- **Maintenance planner** (adjacent structure in the same product): "The maintenance scheduler recommends typical tasks based on your home and location"; weekly to-do list with per-task guidance and done-marking; "Easily schedule and communicate with the people who help you with projects"; digital reminders.
- **Neighborhood data**: active building permits near the user ("Know who's building before they start… See what people are spending on renovations"), comparable sales.
- **Hiring**: FindAPro contractor matching ("premier builders in your community, thoroughly rated"); financing offers (home-improvement loans); PrepToSell (light improvements recommended for a faster sale, with costs and ROI).
- **Distribution**: white-label products for banks/lenders/realtors (cost calculator, home management, contractor sourcing embedded in partner sites); a separate consumer iPhone app for home hunters.
- Reading: the plan here is composed as project types with costs and ROI against the home's value; the home (its value, condition, neighborhood) is the anchor; execution is delegated (find a pro, financing). No homeowner-side task schedule for the improvement work itself (the task machinery that exists serves maintenance).

### HomeBinder — suite-embedded pole (binder center, Projects tab)

Key observations (all A; homeowner-dashboard article is Tier-1):

- Positioning: "residential home management platform that centralizes everything you need for your home"; distributed through inspectors/lenders/agents; free for life; binder pre-loaded with the inspection report; transferable when the home is sold.
- **Homeowner dashboard tabs (Tier-1)**: Projects, Maintenance, Home Pros, Appliances, Docs, Pics, Property Details, Home Finance, Marketplace.
- **PROJECTS tab**: "Here is where homeowners can keep track of any projects or renovations. They can even use it to plan or scope out future projects." — the planner structure inside the binder: track renovations AND plan/scope future ones. Marketing page: "Home Improvements — Now you can set up projects directly from your inspection report, or at any time for ease of tracking."
- **MAINTENANCE tab**: "all of the maintenance tasks set up for them. They can edit, remove, or add additional tasks." (recurring upkeep machinery, separate from Projects)
- **HOME PROS tab**: save contact info of pros who worked on the house; pros recommended by the inspector/agent/lender surface first; Thumbtack integration for a wider network.
- **APPLIANCES tab**: make/model capture (photo of the plate auto-extracts model/serial), recall alerts, purchase details.
- **DOCS / PICS**: unlimited document storage (pre-populated from the inspection); photos tied to the property; home inventory for insurance purposes.
- **PROPERTY DETAILS tab**: rooms, structures, paints/finishes with color codes and manufacturers — the home's physical record.
- **HOME FINANCE tab**: Home Value Estimate "based on transaction price, market changes, home improvement projects, and maintenance completions. Values are updated every 90 days… the homeowner can edit the property value, add the purchase price and see adjustments based on home improvements, appliances added, and maintenance performed." — completed improvement projects feed the home's value record.
- **Sharing & transfer**: co-owner or viewer access ("Share Binder"); transfer the whole binder to a family member or transfer a copy via the Seller Report to a buyer; public Seller Report link for listing.
- Reading: the binder (documents, appliances, inventory, pros) is the center; the Projects tab carries the planner structures (plan/scope/track renovations) and the value record responds to completed projects. This is the suite-embedded realization: planning lives inside whole-home management.

### Planner 5D — design-led pole

Key observations (all A):

- Positioning: "Draw a floor plan and create a 3D home design… all-in-one AI-powered home design software"; audiences span homeowners, interior designers, architects, real estate, enterprise, schools.
- **Spatial design as the plan's body**: 2D floor plans from scratch or from an uploaded/recognized plan (AI floorplan recognition), 3D furnishing with an 8,000+ item library, 4K renders, 360° walkthrough, AR, cross-platform continuity, import of custom 3D models.
- **Mood boards**: "Collect images, ideas and inspiration easily to personalize your space" — the idea-collection layer attached to the design.
- **Money plan attached to the design**: "Shopping list — Get insights into your project's cost estimate. Easily switch between budget and luxury widget options." — the design's items price out as a project cost estimate with finish-tier switching.
- **Collaboration and hiring**: "Design together" collaboration tool; "hire a designer to help you with your build" (marketplace of designers); AI interior design ("experience your design virtually before committing to starting the project… avoid costly decorating mistakes").
- Reading: the plan's body is the designed space; the money plan is the priced shopping list; ideas feed the design. No work-schedule/task machinery and no contractor bidding — execution is out of scope; the design and its cost are the deliverable. This is the design-led realization of the planner: the project scope is expressed spatially.

### Sweeten — marketplace-led pole

Key observations (all A):

- Positioning: "Hire the right general contractor and build your vision… Curated, vetted general contractors. Expert guidance and support. Our services are free!"
- **The posted project as the planning unit**: the homeowner starts a "renovation journey" (intake flow) posting their project; renovation types enumerated (bathroom, kitchen, entire home, basement, ADU/garage, outdoor spaces, attic).
- **Hiring machinery**: personalized matching to vetted general contractors ("based on location, budget, expertise and experience with projects like yours"); the homeowner controls which contractors can contact them; "You'll get 3-5 competing estimates."
- **Bid-leveling**: a free service to compare estimates, including bids from contractors not found on the platform ("I appreciated being able to review and compare multiple bids with the Sweeten team, even bids that came from contractors *not* found on Sweeten").
- **Guidance through execution**: "Sweeten's team is dedicated to your renovation's success… Contractors are held accountable to you for the duration of your project"; regular check-ins documented in testimonials.
- **Cost guides**: remodeling cost guides as planning content (per project type).
- Reading: the money plan takes the form of competitive contractor bids against the posted scope; the platform's value is vetting + bid comparison + guidance. The homeowner's own planning record beyond the posted project is thin — the schedule and production live with the contractor. This is the marketplace-led realization: the planner's money plan is realized as bids.

### Dwellin — maintenance-centered boundary anchor

Key observations (all A):

- Positioning: "Dwellin helps homeowners stay on top of maintenance, organize home details, and earn rewards for responsible home care."
- **Home digital profile**: "track appliances, maintenance, documents, receipts, and improvements"; "Log home actions. Track maintenance, repairs, upgrades, receipts, and key home details in one place."
- **Binder**: "Keep appliances, manuals, warranties, service records, and home documents easy to find."
- **Rewards**: "Build points from qualifying home actions and unlock more value with Premium Rewards."
- **Household**: family members added to the profile; multiple property types (single-family, townhouse, condo, apartment; multiple properties allowed).
- **Sustainability**: home carbon-footprint calculator.
- Reading: improvements appear here as LOGGED past actions (repairs, upgrades), not as planned future work; there is no project scope composition, no money plan, no hiring machinery. The center is home care (maintenance + records + rewards). This product documents the boundary: home-anchored records without project planning are Home Maintenance / Home Management territory.

## Cross-product Comparison

| Structure | Kukun | HomeBinder | Planner 5D | Sweeten | Dwellin | Evidence |
|---|---|---|---|---|---|---|
| Home as anchored, persistent subject (your home: address/property, spaces, records) | ✓✓ (claimed home, value, condition, neighborhood) | ✓✓ (binder bound to the property; transferable) | ✓ (design your home; saved designs) | ✓ (project posted for your home) | ✓✓ (home profile, multiple properties) | B — universal (5/5) |
| Improvement project as defined scope (spaces + work items) | ✓ (project-type composition in estimator) | ✓ (Projects tab: plan/scope/track renovations) | ✓ (the designed space/project) | ✓✓ (posted project scope) | △ (improvements logged, not planned) | B (4/5 planning; 1/5 logging-only) |
| Money plan attached to the work | ✓✓ (cost + ROI + scenarios) | △ (value estimate responds to projects; no per-project budget evidenced) | ✓ (shopping-list cost estimate, finish tiers) | ✓✓ (3–5 competitive bids; bid-leveling) | ✗ (receipts only) | B (3/5 strong + 1/5 indirect) |
| Idea/inspiration collection | ✓ (blog/guides) | — (not observed) | ✓✓ (mood boards) | ✓ (inspiration content) | — | B (common) |
| Hiring machinery | ✓ (FindAPro, financing) | ✓ (Home Pros list, Thumbtack integration) | ✓ (hire a designer) | ✓✓ (vetted GCs, competitive bids, bid-leveling) | — | B (common) |
| Work-plan tasks/schedule for the improvement | ✗ (task machinery serves maintenance) | △ (Projects tab tracks; depth unknown) | ✗ | ✗ (schedule lives with the GC) | ✗ | A×1–2, weak — held below the core |
| Progress/completion logging | △ (remodeling history updates condition score) | ✓ (Projects tracking; Pics; value updates) | — | — (contractor-held) | ✓✓ (log actions, receipts) | B (common) |
| Document storage | — | ✓✓ (Docs tab, pre-populated) | — | — | ✓ (documents, warranties) | B (common; binder pole) |
| Design/visualization | — | — | ✓✓ (2D/3D, renders, walkthrough) | — | — | A×1 (pole signature) |
| Home-value / ROI framing | ✓✓ (PICO, forecast, profit) | ✓ (value estimate tied to projects) | — | — (cost guides only) | — | B (2/5; pole-leaning) |
| Marketplace/bidding | — | — | — | ✓✓ | — | A×1 (pole signature) |
| Maintenance machinery in the same product | ✓ (Maintenance Planner) | ✓ (Maintenance tab) | — | — | ✓✓ (center) | B (common adjacency) |
| Sharing with co-owner/partner | — | ✓ (co-owner/viewer; transfer) | ✓ (design collaboration) | — | ✓ (family members) | B (common) |

## Canonical Model

### Level 0 — Defining Invariant (three jointly-held structures)

1. **The user's own home as the anchored subject.** A persistent, personalized record of the user's home — the property, its spaces/details, its records — that all planning hangs from. The plan belongs to THIS home, not to a generic project. Remove → generic remodeling calculators, content sites, or marketplaces with no home of record.
2. **The improvement project as a defined, revisable plan of work.** The intended change-work (renovation, remodel, addition, upgrade) held as a scope — which spaces, which work items — that the homeowner composes and revises over time, before and during execution. Remove → a home journal/photo album of past work, or a maintenance task list.
3. **The money plan attached to the work.** Planned cost held against the scope — estimates (per work item, often with finish tiers), a budget, contractor bids, scenario comparisons — the decision variable the planner exists to inform. Remove → an idea board or a design toy with no decision to make.

Jointly-held is load-bearing:

- 1 without 2+3 = a home binder/inventory (HomeBinder's center, Dwellin's center) → Home Management territory.
- 2+3 without 1 = a generic remodeling calculator or spreadsheet → content, not a planner application.
- 1+2 without 3 = a mood board / design toy → inspiration, not planning.
- 1+3 without 2 = a home-value dashboard with cost guides → data surface, not a plan.

Evidence: structure 1 is B-layer universal (5/5). Structure 2 is B-layer across the four planning products (Kukun, HomeBinder, Planner 5D, Sweeten); Dwellin documents the logging-only counter-case. Structure 3 is B-layer across the three Type-proper poles (estimation-led, design-led, marketplace-led) plus indirect at HomeBinder (value responds to projects); Dwellin documents the no-money-plan counter-case. The L0 is stated at C-layer (canonical inference) built on these B-layer observations.

### Level 1 — Common Mature Structure

- **Idea & inspiration collection** — mood boards, ideabooks, saved photos/products feeding the scope (Planner 5D mood boards; blog/guide content at Kukun/Sweeten; the Houzz-class pattern, unverified this pass).
- **Hiring machinery** — pro directories/matching, request-for-bid flows, bid comparison support (Sweeten bid-leveling; Kukun FindAPro; HomeBinder Home Pros + Thumbtack; Planner 5D designer hiring).
- **Progress & completion logging** — photos, receipts, completed-work records; completed projects feed the home's record and sometimes its value estimate (HomeBinder, Dwellin, Kukun condition updates).
- **Document storage** — contracts, permits, manuals, warranties attached to the home/project (HomeBinder Docs; Dwellin documents).
- **Work-plan layer** — task lists/schedules for the improvement work; strongest where the homeowner self-executes or tracks (HomeBinder Projects tracking; Kukun's scheduler serves the maintenance side). Evidence is thin — held here, NOT in the core.
- **Sharing** — co-owner/partner access; family members (HomeBinder share/transfer; Planner 5D collaboration; Dwellin household).
- **Home-value linkage** — value estimates that respond to completed improvements (HomeBinder Home Finance; Kukun PICO/value).
- **Maintenance adjacency** — the same product often carries a maintenance planner/task list (Kukun, HomeBinder, Dwellin).
- **Mobile + web surfaces.**

### Level 2 — Variant / Optional Structure

- **Pole: estimation-led** — data-driven cost/ROI estimation against home value as the planning engine (Kukun).
- **Pole: design-led** — the scope expressed as a spatial design (floor plans, 3D, renders) with priced shopping lists (Planner 5D; RoomSketcher/HomeByMe class unverified).
- **Pole: marketplace-led** — the money plan realized as competitive bids from vetted pros with guidance (Sweeten; Houzz/Angi class unverified).
- **Pole: suite-embedded** — planning as a Projects module inside a home-management binder (HomeBinder; HomeZada class unverified).
- **Prep-to-sell framing** — light improvements selected for sale ROI/speed (Kukun PrepToSell; HomeBinder Seller Report).
- **Maintenance-adjacent packaging** — improvement planning bundled with maintenance planning in one product.
- **Embedded/white-label distribution** — the planner embedded in banks', realtors', inspectors' surfaces (Kukun white-label; HomeBinder partner network).
- **Multi-property** — managing several homes in one account (Dwellin; HomeBinder per-property binders).
- **AI-era assistance** — AI design generation, AI plan generation (era-current; observed only at the design pole and in adjacent products; role in the core unverified).

### Level 3 — Vendor-specific Structure (research notes only)

- Kukun: PICO™ property-condition score, ARVE renovation-cost data, KIO investment-outlook score, permit-data intelligence, white-label estimator for partner sites, separate Kukun Homes app for home hunters.
- HomeBinder: Repair Pricer repair estimates, HomeBinder Assistant move-in concierge, CPSC recall-check flow, 90-day value-update cadence, Seller Report public link, inspector/lender/agent distribution.
- Planner 5D: 4K renders, AI floorplan recognition, 360° walkthrough, Apple Vision Pro surface, item shop, designer marketplace, education/enterprise tiers.
- Sweeten: bid-leveling service, contractor-vetting methodology, metro-locations model, free-to-homeowners business model (contractor-side acquisition).
- Dwellin: rewards points/Premium Rewards, carbon-footprint calculator, sustainability positioning.

## Historical / Market-Sample Check

Would older, regional, platform-native planning practice still fit the L0?

- **Paper era**: a homeowner planning a kitchen renovation with a graph-paper sketch of the space, a clippings/idea folder, a budget worksheet with per-item costs, a folder of contractor bids, and a calendar — this satisfies all three L0 structures (the house as the subject; the renovation as a defined scope being composed; the money plan as worksheet + bids). No app, no cloud, no 3D required. → passes.
- **Platform-native**: a spreadsheet (scope + budget), a documents folder (bids, contracts), and a photo board (ideas) — the same three structures with generic tools. The Type exists as the dedicated application that integrates them around the home. → passes.
- **Regional**: German owner-builder ("Bauherren") tools for self-managed house building/renovation and UK extension-planning services appear (from general knowledge, NOT directly sampled this pass — inference only, C-layer) to carry the same core with heavier construction machinery; they would sit at the heavy end of the variant spectrum. Not asserted as fact.
- **Era check against over-fitting**: nothing in the L0 requires 3D design, AI, marketplace vetting, home-value models, or mobile apps. The estimation-led, design-led, marketplace-led, and suite-embedded poles are all realizations, not definitions. → no era/vendor over-fit detected.

## Vendor-specific Findings

See Level 3. None of these entered the canonical model. The closest calls:

- **Home-value/ROI framing** (Kukun signature, also HomeBinder) — held at L1/L2, not the core: a planner without value analytics is still a planner (Planner 5D, Sweeten have none/limited).
- **Bid-leveling** (Sweeten signature) — a marketplace-pole service, not a Type structure.
- **Rewards/sustainability** (Dwellin signature) — belongs to the maintenance-centered neighbor, not this Type.

## Rejected Findings

1. **"Planner = generic project management for consumers"** — rejected. Generic PM's project→tasks→team→schedule machinery is not what these products center: the sampled products hold scope+money+ideas+records around the home; task/schedule machinery is thin or absent (and when the work is hired out, the schedule lives with the pro). The home-domain objects (spaces, work-item catalogs, finish tiers, bids, home value) are not PM structures.
2. **"Planner = the contractor's system with a homeowner login"** — rejected. Client portals of contractor systems (Buildertrend/CoConstruct class, per the sibling pass) bind the homeowner to the contractor's job record; this Type's record belongs to the homeowner across projects and across contractors. Different subject of record.
3. **"Design tools are this Type"** — rejected as identity. A spatial design tool plans the SPACE; this Type plans the WORK and its MONEY. Planner 5D is the documented straddle: design-led realization carrying the money plan (shopping-list estimate). A design tool with no work/money plan is a different Type (no dedicated directory leaf; nearest Architecture Design Application §16).
4. **"Marketplace = this Type"** — rejected as identity. Sweeten holds the hiring leg with guidance; the homeowner's persistent planning record is not its center. Marketplace is a pole/leg, not the Type.
5. **"Home-value tracking = this Type"** — rejected as identity. A value dashboard with cost guides (no project composition) fails the removal test; value framing is a pole signature (Kukun) and a common capability (HomeBinder).
6. **"AI plan generation is definitional"** — rejected for now. Era-current capability; observed only at the design pole (Planner 5D AI design) and in adjacent products; held at L2 as era-current assistance.

## Boundary Findings

1. **vs Home Improvement Contractor Management (§29 sibling, processed)** — different subject of record: the homeowner's own project vs the contractor's business system (leads→sale→production→money). The sibling pass drew this boundary; this pass confirms it from the consumer side. The interlock point is the contractor system's client portal (homeowner sees schedule/selections/budget of ONE job inside the contractor's record) vs the homeowner's own planner (holds the plan across ideas, scenarios, bids, projects, and contractors). No joint review required — the seam held both ways.
2. **vs Home Maintenance Application (§29 sibling, unprocessed)** — improvement work is bounded, discretionary change-making (renovation/remodel/addition/upgrade); maintenance is recurring preservation of existing systems. Products bundle both (Kukun carries a Maintenance Planner beside the estimator; HomeBinder separates Projects and Maintenance tabs) — the center of gravity decides. Forward note for the home-maintenance pass: Dwellin (log-and-rewards home care) and the maintenance-tab machinery documented here belong to that leaf; the discriminator is planned change-work vs recurring upkeep.
3. **vs Home Management Application (§29 sibling, unprocessed)** — HomeBinder's center is the whole-home binder (documents, appliances, inventory, pros, finance) with Projects as one tab; the planner structures (project scope + money plan) are the seam. Consistent with the family-organizer pass's premises-vs-people center-of-gravity note: this leaf is premises-centered AND project-bounded, whereas home management is premises-centered and operation-wide. Forward note for the home-management pass.
4. **vs spatial design tools (no directory leaf; nearest Architecture Design Application §16)** — design tools plan the space; this Type plans the work and its money. Planner 5D straddles and is documented as the design-led pole. If a future leaf for consumer home-design tools is created, the seam is the money/work plan.
5. **vs Home Services Marketplace / Local Service Marketplace (§29)** — the hiring leg vs the planning record. Sweeten documents the marketplace pole (vetted pros, bids, guidance) with only a thin homeowner planning record; marketplaces feed the planner's hiring machinery. Complementary, not identical.
6. **vs Project Management Application (§03.07)** — generic PM organizes a team's work on a project; this Type organizes a household's decisions about change-work on a home, with the money plan first-class and execution often delegated. Shared vocabulary (project, tasks), different world model.
7. **vs Budgeting Application (§08)** — the money plan here is scoped to the project's work items (and often tied to home value/ROI), not whole-finances budgeting.
8. **vs Travel Itinerary Planner (§26, unprocessed)** — the same "consumer planner of a bounded real-world effort" pattern (subject anchor + composed plan + money); different subject (a home vs a trip). Family resemblance only.
9. **vs Construction Estimating / Quantity Takeoff (§17)** — Kukun's estimator is consumer-facing cost guidance (project types, finish tiers, ROI), not trade takeoff from plans. Capability-adjacent; different audience and object.
10. **vs inspiration/review platforms (Houzz class, unverified this pass)** — idea collection is a standard capability (L1); an inspiration platform without a home-anchored project+money plan is a content/marketplace Type, not this one.

## Uncertainties

1. **Major category members unreachable** — HomeZada (403 ×2; help subdomain transport error; web-archive timeout ×2), Houzz (403; App Store fetch geo-redirected), Block Renovation (404 ×2 — defunct or moved). The dedicated "planner proper" pole (a standalone project planner with budget + tasks + schedule for the homeowner) is therefore under-evidenced; assertions about task/schedule machinery are calibrated down (held at L1, explicitly not in the core). No details of these products are asserted from memory.
2. **No interactive Tier-1 documentation for four of five products** — HomeBinder's homeowner Help Center is the only Tier-1 operational documentation in the sample; Kukun, Planner 5D, Sweeten, and Dwellin evidence is official product-page level (Tier 2). Exact object fields, statuses, limits, and defaults are not asserted.
3. **Regional coverage** — the sample is US-dominant (Kukun, HomeBinder, Sweeten, Dwellin) plus one global design tool (Planner 5D). European/Asian consumer renovation planners were not sampled; the regional reading in the historical check is inference (C-layer), not observation.
4. **Work-plan/tasks depth** — only HomeBinder's Projects tab ("plan or scope out future projects") evidences homeowner-side planning machinery beyond scope+money; its depth (tasks? budgets? schedules inside a project?) is not documented in reachable sources.
5. **Money-plan universality** — 3/5 sampled products attach a direct money plan to the work (Kukun, Planner 5D, Sweeten) and HomeBinder indirectly (value responds to projects); Dwellin does not (logging-only). The L0 claim for the money plan rests on the planning products' shared promise and the removal test; the logging-only pole is documented as the boundary case.
6. **AI-era drift** — AI design/plan generation is appearing across the space (Planner 5D AI design; Kukun's separate AI home-hunter app; the contractor-side AI wave documented in the sibling pass). Its eventual role in the homeowner planner's core is unverified; held as era-current assistance.

## Final Synthesis

Home Improvement Planner is the homeowner-side planning application for improvement work on one's own home. Its defining core is the jointly-held three: the user's own home as the anchored, persistent subject of the plan; the improvement project as a defined, revisable plan of work (which spaces, what work items); and the money plan attached to that work (estimates, budgets, bids — the decision variable). Around that core, mature products add idea collection, hiring machinery (pro matching, competitive bids, bid comparison), progress/completion logging, document storage, sharing with co-owners, home-value linkage, and an adjacent maintenance planner. The market realizes the Type in four poles — estimation-led (cost/ROI data as the engine), design-led (the scope expressed as a spatial design with priced shopping lists), marketplace-led (the money plan realized as competitive bids with guidance), and suite-embedded (planning as a Projects module inside a home-management binder) — with a maintenance-centered logging pole (Dwellin) documenting the boundary toward Home Maintenance Application. The leaf is a legitimate independent Type: its subject (the homeowner's own home and plan) and its money-plan-first shape are structurally distinct from the contractor's business system (the processed sibling), from recurring-upkeep maintenance apps, from whole-home binders, from spatial design tools, and from marketplaces. The main evidence gap is the dedicated planner-proper pole (HomeZada/Block class unreachable or defunct), so task/schedule machinery is held at the common-capability layer rather than the core.
