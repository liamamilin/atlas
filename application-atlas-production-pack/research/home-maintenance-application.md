# Research Notes — Home Maintenance Application

Leaf: Home Maintenance Application (DIRECTORY.md §29 Home, Family, Personal & Local Services — home/family cluster, between Home Inventory Application and Home Improvement Planner)

Research date: 2026-09-08

## Research Goal

Understand what "Home Maintenance Application" software actually is in the real market: what the homeowner tracks, what structures exist inside such an application (care targets, recurring schedules, histories), how the upkeep plan is created and kept moving, what role service pros and records play, and where its boundaries lie — especially against Household Chore Application, Home Management Application, Home Inventory Application and Home Improvement Planner (§29 siblings), Property Maintenance Management (§17), home warranty products, home services marketplaces, and generic task/reminder tools.

## Initial Boundary (pre-research hypothesis)

- Core purpose: help a homeowner stay on top of recurring upkeep of their own home — scheduled/seasonal care tasks, reminders, and a record of what was done.
- Users: homeowners (possibly renters; small-scale landlords drift toward Property Maintenance Management).
- Nearest neighbors: Household Chore Application (recurring tasks, but household labor), Home Management Application (whole-home binder with maintenance as one module), Home Inventory Application (possession records; appliance records overlap), Home Improvement Planner (discretionary change-work vs recurring preservation), Property Maintenance Management (professional/landlord side), Home Services Marketplace (hiring leg), home warranty products.
- Key unknowns: is the recurring schedule the center, or is maintenance usually a module of a wider home binder? Is pro-hiring part of the Type? Is a home profile (location/systems) definitional or common?

## Research Questions

1. What is the central object — the task, the home system/component, the schedule, or the history?
2. How are maintenance tasks created — user-defined, from built-in libraries, or generated from a home profile?
3. What does a task carry — cadence, instructions, assignee, cost, service history?
4. Is there a home profile (location, age, systems, appliances) that drives task generation and tailoring?
5. How do reminders/notifications work (seasonal, recurring, channel)?
6. Is there service-history logging (what was done, when, by whom, cost, receipts)?
7. Is pro-hiring machinery (find/book a pro) core or optional?
8. Multi-home / multi-property support? Household sharing?
9. Where is the line against chore apps (household labor) and against home binders (whole-home hub)?
10. Do older/regional/platform-native forms (paper maintenance schedules, house books) fit the definition?

## Representative Products

1. **HomeBinder** — home-management binder distributed free-for-life through home inspectors, lenders, and real-estate agents; carries maintenance reminders and appliance-recall notifications beside documents, inventory, projects, and service pros. US. Suite-embedded pole. (Fetched this pass.)
2. **Dwellin** — consumer mobile app: digital home profile (property, appliances, maintenance needs), maintenance/repair logging, receipts, timely maintenance prompts, rewards for home care, family sharing, multi-property. US. Log-and-rewards pole; boundary anchor documented by the home-improvement pass. (Fetched this pass.)
3. **Under My Roof** (Binary Formations) — Mac/iPhone/iPad home management app: item details, home details, documents, renovations, maintenance, collections, insurance policies and claims tracking. Apple-ecosystem subscription pole. (Sampled via the home-inventory pass of 2026-09-08, where its official surfaces were reachable; direct fetch this pass timed out.)
4. **Grocy** — self-hosted, open-source "household ERP": stock, shopping list, recipes, meal plan, equipment (manuals), chores (recurring, last-done tracking), batteries, tasks. Boundary specimen toward Household Chore Application / household ERP; documents the chore-vs-maintenance seam from the household-ERP side. (Fetched this pass.)
5. **HomeZada** — known from the two prior sibling passes as the dedicated maintenance-module suite (maintenance calendar/schedules beside inventory, projects, documents, finance). **Unreachable this pass (403 ×2)** — recorded as a sampling gap; no product-specific claims made from memory.

Rejected/abandoned candidates (source-access limitations, recorded below): BrightNest (403 + transport error), HomeSmarts (empty responses ×2), HomeKeepr (empty responses ×2), Centriq (domain recycled — now an IT career-training company), Oply (transport error), Homebrella (domain recycled — now a blog), Frontdoor / HomeServe / American Home Shield / Cinch (403), Under My Roof (timeout ×2 this pass), HomeX (holding company, wrong product), Homechart (family/household hub with no dedicated maintenance feature — adjacent to Family Organizer, not this Type).

## Sources

Fetched 2026-09-08 (Layer A unless noted):

- HomeBinder — https://www.homebinder.com/ (root; product feature sections, About, partner model)
- Dwellin — https://dwellin.com/ (root), https://dwellin.com/app/how-it-works/ , https://dwellin.com/app/overview/ (product pages, FAQ excerpts)
- Grocy — https://grocy.info/ (root; feature carousel: equipment, chores, batteries, tasks)
- Homechart — https://homechart.app/ , https://homechart.app/docs/ (checked for maintenance feature; none — adjacent Type)
- Under My Roof — via research/home-inventory-application.md (sibling pass, 2026-09-08; official surfaces reachable then)

Unreachable/blocked this pass (limitations): homezada.com (403 ×2), brightnest.com (403 + transport), homesmarts.com (empty ×2), homekeepr.com (empty ×2), getcentriq.com/centriq.com (transport / domain recycled to unrelated business), oply.co (transport), homebrella.com (domain recycled to unrelated blog), frontdoorhome.com / homeserve.com / americanhomeshield.com / cinchhomeservices.com (403), undermyroofapp.com (timeout ×2), homex.com (holding-company site, wrong product).

## Product Observations

### HomeBinder (Layer A)

- Positioning: "Keep all of the information about your home in one place. Plus, get periodic maintenance reminders and product recall notifications tailored specifically for your home."
- Feature set (root page): Maintenance Reminders ("regular notifications, via text or email"), Home Improvements (projects, settable from the inspection report), Document Storage, Appliance Recalls (store make/model numbers to get notified), Service Providers ("recommended home pros to complete repairs"), Home Inventory.
- Distribution: only through an authorized partner network (home inspectors, mortgage lenders, real-estate agents); binder pre-loaded with the inspection report; "free for life".
- Reading: the center is the whole-home binder (documents, appliances, inventory, pros, finance); maintenance machinery is reminders + recall alerts — schedule-driven notifications, not a deep task-planning module. Maintenance is one capability of the binder. Consistent with the home-inventory and home-improvement passes' reading of this product.

### Dwellin (Layer A)

- Positioning: "Dwellin helps homeowners stay on top of maintenance, organize home details, and earn rewards for responsible home care."
- Home profile: "A smart home profile built around your property, appliances, and maintenance needs"; "add your home, track key assets, log maintenance, upload receipts".
- Actions: "simple home actions — like adding appliances, logging maintenance, uploading receipts, and tracking improvements"; "Track maintenance, repairs, upgrades, receipts, and key home details in one place."
- Binder: "Keep appliances, manuals, warranties, service records, and home documents easy to find."
- Prompts: "Timely maintenance prompts so you know what to do next."
- Rewards: "Build points from qualifying home actions and unlock more value with Premium Rewards."
- Household: "adding your family members to your profile."
- Sustainability: Home Carbon Footprint Calculator.
- FAQ: built for homeowners ("just moved in, have owned for years, or manage multiple properties"); single-family homes, townhouses, condos, apartments; iOS/Android.
- Reading: the center is the home-anchored care log — profile + appliance/asset records + logged actions + prompts — with rewards as the engagement engine. Improvements are logged, not planned (per the home-improvement pass). No pro-hiring machinery observed on the fetched pages.

### Under My Roof (Layer A via sibling pass, 2026-09-08)

- Per research/home-inventory-application.md: Mac/iPhone/iPad home management app with iCloud sync/sharing; item details, home details, documents, renovations, maintenance, collections, insurance policies and claims tracking. Successor to the 17-year desktop product "Home Inventory" (which carried "maintenance scheduling" beside deep per-item catalog and insurance machinery).
- Reading: maintenance is one module of an Apple-ecosystem home-management suite whose center is the possessions/home record. The sibling pass recorded the seam: recurring-work machinery vs possession records.

### Grocy (Layer A)

- Positioning: "ERP beyond your fridge" — self-hosted groceries & household management.
- Relevant modules: Equipment ("Keep all the instruction manuals and important information about your devices in one place"), Chores ("Think less about 'oh, when have I done last...'"), Batteries ("knowing when you charged them last"), Tasks ("Just another to do list").
- Reading: recurring-upkeep machinery exists (last-done tracking, recurrence) but the subjects are household routine (chores), consumables (stock), and small equipment/batteries — a household ERP, not a home-fabric maintenance plan. Documents the chore/equipment side of the seam. Self-hosted/open-source deployment is a variant realization.

### Homechart (Layer A — adjacent, not a sample)

- "Your Family's Mission Control": events, meals, chores, budgets, reminders, tasks. Docs list features: Bookmarks, Budget, Calendar, Contacts, Cook, Health, Inventory, Markdown, Notes, Plan, Reward, Shop — no dedicated maintenance feature. Confirms the family-hub pole belongs to Family Organizer / Home Management territory, not this Type.

### HomeZada (unreachable — no claims)

- Known from sibling passes as the dedicated maintenance-module suite. Not fetched this pass (403 ×2). No product-specific assertions made. Recorded as the main sampling gap: the dedicated maintenance-plan pole (HomeZada/BrightNest/HomeSmarts class) is under-evidenced.

## Cross-product Comparison

| Structure | HomeBinder | Dwellin | Under My Roof | Grocy |
|---|---|---|---|---|
| Home-anchored record | yes (binder per home, pre-loaded from inspection) | yes (home profile: property, appliances) | yes (home details) | weak (household ERP; no per-home fabric record) |
| Care targets = home fabric/systems/equipment | yes (maintenance reminders, appliance recalls) | yes (property, appliances, maintenance needs) | yes (maintenance module) | partial (equipment/batteries; chores are household routine) |
| Recurring schedule / cadence | yes (periodic reminders, text/email) | yes (timely maintenance prompts) | yes (maintenance scheduling per sibling pass) | yes (chore recurrence, last-done tracking) |
| Completion / history logging | thin (documents, service pros) | yes (log maintenance/repairs, receipts, service records) | yes (maintenance module) | yes (chore last-done tracking) |
| Appliance/equipment records + manuals/warranties | yes (make/model for recalls) | yes (appliances, manuals, warranties) | yes (item details) | yes (equipment manuals) |
| Guidance content | no (observed) | yes (simple guidance, Journal) | no (observed) | no |
| Pro connection | yes (recommended service pros) | not observed | not observed | no |
| Rewards/gamification | no | yes (points, Premium Rewards) | no | no |
| Recall alerts | yes | no | no | no |
| Sustainability/carbon | no | yes (carbon calculator) | no | no |
| Multi-property | not observed | yes (FAQ) | not observed | no |
| Household sharing | not observed | yes (family members) | yes (iCloud sharing per sibling pass) | yes (multi-user) |
| Distribution | partner-only (inspectors/lenders/agents) | consumer app stores | consumer (Apple ecosystem) | self-hosted/open-source |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The user's own home — its structure, systems, and equipment — as the anchored subject of care.** A persistent per-home record whose care targets are the home's physical fabric (roof, gutters, HVAC, water heater, detectors, appliances), not the household's routine living work. Remove → a generic to-do/reminder app or a content site with no home of record.
2. **The recurring upkeep plan.** Care items held as scheduled/recurring work — cadences (seasonal, annual, monthly, usage-based) that generate due work over time. Remove → a one-off repair log or home journal (records without a forward plan).
3. **The upkeep record.** Completion tracking that accumulates into the home's care history — what was done, when (often cost/who). Remove → a static seasonal checklist or a reminder-only tool (no memory of care).

Jointly-held is load-bearing:

- 1+2 without 3 = a seasonal checklist / content site (tips without tracking)
- 2+3 without 1 = a generic recurring to-do / chore app
- 1+3 without 2 = a repair/service log (home journal)

Historical/market-sample check: the paper home-maintenance schedule (seasonal checklist with checkmarks) and the house book (service receipts + a maintenance calendar kept for the house) both satisfy all three structures — no cloud, AI, pro network, photos, or appliance databases in the core. Conversely, a generic reminders app configured with home-maintenance lists fails structure 1 (no home-anchored record) — confirming the anchor is definitional, not incidental.

### L1 — Common Mature Structure

- Reminders/notifications ahead of due dates (push/email/text) — HomeBinder, Dwellin (B-layer)
- Home profile (property, systems, appliances) that tailors the plan — HomeBinder ("tailored specifically for your home"), Dwellin ("smart home profile built around your property, appliances, and maintenance needs") (B-layer)
- Appliance/equipment records with manuals/warranties — Dwellin, HomeBinder (make/model), Grocy (equipment), Under My Roof (B-layer; adjacent to Home Inventory)
- Service-history logging with receipts/costs — Dwellin, Under My Roof (B-layer)
- Calendar/seasonal views of due work — implied by schedule machinery; direct observation thin (held with moderate confidence)
- Built-in task libraries/templates keyed to home characteristics — plausible across the class but the dedicated-plan pole was unreachable; held at common with moderate confidence, not promoted to core
- Per-task guidance/how-to content — Dwellin (A, single-source at this depth)

### L2 — Variant / Optional Structure

- Pro-hiring machinery (recommended/bookable pros) — HomeBinder only in sample (A, product-specific; marketplace leg)
- Rewards/gamification for completed care — Dwellin (pole signature)
- Recall notifications from stored make/model — HomeBinder (product-specific)
- Sustainability/carbon tracking — Dwellin (product-specific)
- Multi-property support — Dwellin FAQ (drift toward Property Maintenance Management at scale)
- Household sharing/co-ownership — Dwellin, Under My Roof, Grocy (multi-user) (B-layer at the weak end)
- Distribution through professionals (partner-only, pre-loaded binders) — HomeBinder (channel variant)
- Self-hosted/open-source deployment — Grocy (deployment variant)
- Home-warranty/service-plan linkage, budgeting for maintenance, resale/home-report export — plausible from the class's positioning but not directly evidenced this pass; held as unverified optional

### L3 — Vendor-specific (Research Notes only)

- Dwellin points economy and "Premium Rewards" tier; Home Carbon Footprint Calculator
- HomeBinder Assistant (white-glove utility/service setup during move-in); Repair Pricer link; recall-alert machinery; "free for life" partner distribution
- Grocy's batteries module, barcode/stock machinery, feature flags
- Under My Roof's insurance-policy/claims tracking depth (documented in the sibling pass)

## Rejected Findings

1. **"Maintenance app = generic recurring to-do list with home tasks"** — rejected. Generic task tools configured with home-maintenance lists fail the home-anchored-record test (L0-1). The Type's products hold a per-home record (profile, systems, appliances) that tasks hang from.
2. **"Maintenance app = the binder"** — rejected. HomeBinder's center is the whole-home binder; maintenance machinery is one capability. The binder is a pole (suite-embedded), not the Type.
3. **"Maintenance app = a service that does the maintenance"** — rejected. Subscription maintenance services (Oply/Homebrella class, both domain-dead or recycled this pass) are services with apps; the Type is the homeowner's own planning/tracking surface.
4. **"Rewards are definitional"** — rejected. Dwellin-only; engagement pole signature.
5. **"Pro-hiring is definitional"** — rejected. Observed in one sample (HomeBinder, as recommendations, not booking); the marketplace leg is optional.
6. **"Appliance databases are definitional"** — rejected as core; they are common-mature (B-layer) and overlap Home Inventory. The care plan, not the possession catalog, is the center.

## Boundary Findings

1. **vs Household Chore Application (§29 sibling, unprocessed)** — both hold recurring tasks with completion tracking. Discriminator: the task's subject. Maintenance tasks target the home's physical fabric (systems, structure, equipment); chores target the household's routine living work (cleaning, laundry, dishes). Grocy documents the straddle from the household-ERP side: chores/equipment/batteries with recurrence, but no home-fabric record. Removal test: strip the home-fabric anchoring from a maintenance app → chore/generic to-do; add home-fabric tasks to a chore app → drifts toward this Type. Products can bundle both; center of gravity decides.
2. **vs Home Management Application (§29 sibling, unprocessed)** — HomeBinder documents the seam: its center is the whole-home binder (documents, appliances, inventory, pros, finance) with maintenance reminders as one capability. Removal test: strip maintenance from HomeBinder → still a home binder; strip the binder from a maintenance-centered product → still a maintenance app. Consistent with the family-organizer pass's premises-vs-people note: this leaf is premises-centered AND upkeep-bounded; home management is premises-centered and operation-wide.
3. **vs Home Inventory Application (§29 sibling, processed)** — possession records vs recurring-work machinery. Appliance records with manuals/warranties appear inside both (Dwellin, HomeBinder, UMR, Grocy equipment). Seam: the inventory's record is of things owned; the maintenance app's machinery is of work due and done. Removal test: strip maintenance from UMR → still a home inventory; strip item records from Dwellin → still a maintenance app (weaker).
4. **vs Home Improvement Planner (§29 sibling, processed)** — recurring preservation of existing systems vs bounded, discretionary change-work. Products bundle both with separate machinery (HomeBinder separates Projects and Maintenance tabs; Kukun carries a Maintenance Planner beside the estimator — per the planner pass). Center of gravity decides. The planner pass's forward note is confirmed: Dwellin and the maintenance-tab machinery belong to this leaf.
5. **vs Property Maintenance Management (§17)** — the professional/landlord operations system (work orders, vendors, tenants, portfolios, compliance) vs the consumer's self-care of their own home. Different subject of record (the business's portfolio vs the household's home) and different user. Multi-property maintenance apps drift toward the §17 Type at scale.
6. **vs Home Services Marketplace (§29)** — the hiring leg vs the upkeep plan/record. Marketplaces feed the pro-connection leg; the maintenance app holds the plan and history. Complementary.
7. **vs home warranty / service-plan products (no dedicated leaf; Frontdoor/AHS/HomeServe class)** — a service contract (coverage, claims, dispatch) vs the homeowner's upkeep plan. Warranty products may carry maintenance reminders as engagement features; the contract, not the care plan, is their subject of record. All major warranty vendors were unreachable this pass (403) — boundary held at positioning level only.
8. **vs CMMS / EAM (§16)** — the abstract shape is parallel (asset registry + recurring preventive tasks + work history), but the subject (a household's home), the user (the homeowner), and the scale make this a distinct consumer Type. No directory change proposed.
9. **vs Smart Home Platform (§29 sibling)** — device control/automation vs upkeep planning. Not directly evidenced this pass; held at positioning level.

## Uncertainties

1. The dedicated maintenance-plan pole (HomeZada, BrightNest, HomeSmarts, HomeKeepr — all unreachable this pass) is under-evidenced. Built-in task libraries, seasonal plan generation from home profiles, and budgeting machinery are held at common/optional with moderate confidence rather than promoted.
2. Whether "calendar/seasonal views" are a standard interface could not be confirmed directly (schedule machinery is evidenced; its calendar rendering is inferred).
3. Home-warranty linkage and resale/home-report export are plausible class features but not directly evidenced this pass.
4. Domain recycling is rampant in this niche (Centriq → IT training; Homebrella → blog; per the home-inventory pass, nestegg → children's investment, blueplum → cabinetry). Product identity must be verified before citing any domain.
5. The chore-vs-maintenance line inside products that bundle both (e.g., Grocy's chores vs equipment) is drawn by task subject; a future Household Chore Application pass should confirm from that side.

## Final Synthesis

Home Maintenance Application is the homeowner's application for the recurring upkeep of their own home. Its defining core is the jointly-held three: the user's own home — its structure, systems, and equipment — as the anchored subject of care; the recurring upkeep plan (care items with cadences that generate due work over time); and the upkeep record (completion tracking accumulating the home's care history). Around that core, mature products add reminders, home profiles that tailor the plan, appliance/equipment records with manuals and warranties, service-history logging with receipts, guidance content, and household sharing. The market realizes the Type in poles: suite-embedded (maintenance as one capability of a whole-home binder — HomeBinder), log-and-rewards (home-anchored care log with prompts and rewards — Dwellin), Apple-ecosystem suite module (Under My Roof), and household-ERP (Grocy, documenting the chore/equipment boundary). The dedicated maintenance-plan pole (HomeZada/BrightNest class) is under-evidenced this pass due to source-access limitations. The leaf is a legitimate independent Type: its subject (the home's physical fabric under recurring care) is structurally distinct from chore apps (household routine labor), home binders (operation-wide hubs), home inventory (possession records), the improvement planner (discretionary change-work), and the professional property-maintenance systems (§17).
