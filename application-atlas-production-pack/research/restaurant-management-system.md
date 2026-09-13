# Research Notes — Restaurant Management System

## Research Goal

Understand what a "Restaurant Management System" (RMS) is as an Application Type, given that:

- the directory separates **Restaurant POS** (transaction surface) from **Restaurant Management System** (this leaf);
- the `restaurant-pos` example document defines this leaf as "broader operational suite beyond point-of-sale transaction";
- the `restaurant-inventory-management` pass (2026-09-09) recorded this leaf as the **"suite pillar"** and held seams against it;
- the market label is used loosely: POS-suite vendors (Toast, Lightspeed, TouchBistro) apply "restaurant management" to their whole stack including the POS, while back-office vendors (Restaurant365, Crunchtime, Nory, Fourth/HotSchedules) apply it to a management layer **without** a POS.

The research question is therefore: **is there a distinct, definable management layer beneath the loose market label — and what is its minimal defining structure?**

## Initial Boundary

Working hypothesis at start:

- Core use: run the restaurant **business** (not the transaction, not the guest experience) — plan and control menu/pricing, labor, stock, and cost, and see performance.
- Primary users: owner/operators, general managers, multi-unit/franchise operators, back-office finance roles.
- Nearest neighbors: Restaurant POS (transaction), Restaurant Inventory Management / Restaurant Food Cost Management / Employee Scheduling / Restaurant Menu Management (single-domain siblings), Institutional Foodservice Management (institution feeding), Catering Management (booked events), Commercial Kitchen Management (production layer), Business Management Suite / ERP (generic business), Retail Store Management System (retail analog), Hotel PMS (lodging analog).
- Known unknowns: whether the market term collapses into "POS suite" (alias risk); whether any single resource domain (e.g., labor) is definitional; how the actuals side is sourced (native vs integration).

## Research Questions

1. What do products that self-label "restaurant management system/software" actually contain?
2. Is the POS part of the definition, or is the Type definable without it?
3. Which resource domains (menu, labor, stock, money) are definitional, and which are packaging?
4. What is the recurring management workflow (the "loop") that makes this a *management* system rather than a bundle of tools?
5. How do single-location and multi-location postures differ?
6. Where exactly are the seams vs the single-domain sibling Types (inventory, food cost, scheduling, menu)?
7. Would older / regional / non-POS products still fit the definition?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Pole | Customer tier | Why sampled |
|---|---|---|---|
| Toast | POS-anchored suite ("Restaurant POS" + "Restaurant Management Suite" in same nav) | SMB → enterprise (single site to chains) | dominant US POS-suite vendor; shows how the management layer relates to the POS |
| Crunchtime | Multi-unit operations management suite (no POS) | enterprise chains/QSR (850+ brands, 150,000+ locations claimed) | pure back-office/ops pole; integrates with POS rather than being it |
| Restaurant365 | Accounting-anchored back office ("restaurant management software", self-described cloud ERP for restaurants) | SMB → franchise/multi-location groups (52,000+ restaurants claimed) | the P&L/accounting center of gravity; absorbed Compeat |
| Nory | AI-era operations platform ("restaurant operating system") | multi-location groups, independent → enterprise (Europe/US) | modern forecasting/AI-assistant pole |
| HotSchedules (Fourth) | Labor-anchored management ("workforce management platform"; Fourth "Restaurant Operations Suite") | enterprise chains (120,000 locations claimed) | labor-centric pole; integrates with PAR/Toast/Oracle Micros/NCR Aloha POS |

## Sources

Fetched 2026-09-09 (Layer A unless noted):

- Toast — home (nav: full suite structure incl. "Restaurant Management Suite"): https://www.toasttab.com/
- Toast — "How Does Toast Work?": https://www.toasttab.com/how-toast-works
- Crunchtime — home: https://www.crunchtime.com/
- Crunchtime — Product Suite Overview: https://www.crunchtime.com/suite-overview
- Restaurant365 — home: https://www.restaurant365.com/
- Restaurant365 — Why R365: https://www.restaurant365.com/why-r365/
- Nory — home: https://nory.ai/
- Fourth / HotSchedules — home: https://www.hotschedules.com/ (serves Fourth's "Restaurant Operations Suite")

Failed / abandoned (per network-restriction rule):

- Lightspeed Restaurant — https://www.lightspeedhq.com/pos/restaurant/ (403) and https://help.lightspeedhq.com/hc/en-us (transport error) — abandoned after 2 failures. Lightspeed is market-known to self-label "restaurant management system"; this could not be verified from primary sources this pass. **Sourcing limitation recorded; POS-suite-pole naming evidence rests on Toast + the restaurant-pos example document.**
- Compeat — https://www.compeat.com/ (transport error) — abandoned. Indirect evidence: Restaurant365's partner-login domain is `compeat.my.site.com`, consistent with R365 having absorbed Compeat.
- Toast product pages `/products/benchmarking` and `/products/multi-location-management` — 404; suite membership evidenced from site navigation only.

## Product Observations

### Toast (Layer A)

- Site navigation separates **"Restaurant POS"** from a **"Restaurant Management Suite"** (Benchmarking, Multilocation management, Integrations) — the vendor itself distinguishes the transaction surface from a management suite.
- "How Toast Works" framing: "Point of sale is just the beginning." Journey stages: Take Orders → Prep & Serve → Dine & Pay → **Manage & Grow**.
- Manage & Grow items: "Onboard & pay employees — Employee hours and punch data sync automatically" (Payroll & Team Management); "Attract & retain guests" (Loyalty/Marketing); "Process & Automate Invoices — Take control of inventory, automate accounts payable, and streamline back-office tasks" (xtraCHEF).
- Broader suite structure in nav: Operations Suite (POS, Toast Now management app, catering, payments), Marketing Suite, Team Management Suite (Scheduling, Tips), Digital Storefront Suite, Supplier & Accounting Suite (xtraCHEF cost analytics, Inventory management), Payroll Suite, Restaurant Management Suite (Benchmarking, Multilocation management), Finance (Capital, Checking).
- Toast IQ (AI assistant) sample insights: "Tomorrow's sales are forecasted to be 15% higher than your weekday average"; "Your Classic Double Smash Burger drove 22.4% of total revenue over the last four weeks"; "You could save 14 labor hours this week by shifting to a leaner closing crew after 8 p.m." — forecast → compare → act pattern across sales, menu, labor.
- Scale framing: "If you want to own one location or 100…" — single- and multi-location both first-class.

### Crunchtime (Layer A)

- Self-labels: "restaurant operations management suite"; "operations software that multi-unit restaurants use to manage profitability, drive great customer experiences, and grow confidently."
- Suite: Inventory Management (counts, ordering, reconciliation, recipe management, Food Cost Management "AvT" [actual vs theoretical], AI Forecasting); Labor & Scheduling (scheduling, labor cost management, labor law compliance); Operations Execution (tasks, audits, alerts, corrective actions; temp monitoring; food prep labeling); Kitchen Management (KDS); Guest Management (host); Operational Intelligence ("Insights", "Data Streaming"); Learning & Development.
- Operational Intelligence framing: "Brands use Crunchtime as the trusted data source for what is really happening across their operation and in each store–from food and labor costs to food safety compliance, training completions, and more"; "Have a source of truth for operational costs and activities"; "Know what's happening in every store in real time"; "Identify top performing stores and opportunities for improvement."
- Integrations page: **Point-of-Sale integrations** ("Send staff schedules and employee information to your POS, and sync your menu mix, sales mix, and time punches in Crunchtime"); **Accounting integrations** ("Send your accounts payable, accounts receivable, sales, inventory, location transfers… to your accounting system"); **HR & Payroll** (two-way sync); **Vendors & Suppliers** (order guides, PO confirmations, invoices, purchase orders, bid sheets); APIs. → Crunchtime is a management layer **around** POS/accounting/payroll, not the POS itself.

### Restaurant365 (Layer A)

- Self-labels: page title "Restaurant Management Software | Restaurant365"; "#1 Rated Restaurant Management Software"; "Leading Restaurant Management System"; "restaurant back office"; LinkedIn company slug "restaurant365-cloud-erp-for-restaurants".
- Center of gravity: "R365 AI is the only intelligence engine trained on your full restaurant P&L - connecting what was sold, what it cost, what was paid, and what you made. Available now across Accounting, Inventory, Payroll, and Workforce."
- Modules: **Accounting** (AP automation, banking, fixed assets, budgeting & forecasting, financial reporting, bookkeeping, dispute resolution); **Inventory & Purchasing** (inventory management, recipes, prep, purchasing & receiving, cash management, commissary); **Workforce Management** (scheduling, sales forecasting, employee training, time & attendance, task management, logbook & chat, tip automation); **Payroll & HR** (hiring, onboarding, HR, payroll).
- Control-loop language: "Pinpoint food cost variance to eliminate waste and grow margins"; "R365 AI shows food cost variances across every location in real time"; "Monitor actual vs. theoretical labor to prevent costly overstaffing"; "R365 AI connects sales forecasts, labor budgets, and scheduling data, giving you guidance to act on labor overruns before they happen"; customer quote: "R365 merged all of our data, gave us deeper analysis, and a real time P&L."
- "50% Increase in Back Office Efficiency — With accounting, inventory, scheduling, and POS data on one AI-powered system." → POS data is an **input**, consumed from POS systems.
- Who they serve: Small Business / Franchise Brands / Multi-Location Groups / Accounting Firms; restaurant styles QSR → fine dining. Franchisee benchmarking: franchisees "see immediately how their results compare to other franchisees and the company performance" (Sbarro CFO quote).

### Nory (Layer A)

- Self-labels: page title "Restaurant Management Software | AI-Powered Operations"; "The agentic AI restaurant operating system that predicts demand, builds schedules, manages ordering and payroll, and keeps your P&L on track — across every location."
- Modules: Business Intelligence (demand forecasting, review analysis); Inventory (ordering, waste, supply chain); Workforce (scheduling, compliance); Payroll. AI assistants: Scheduling, Customer Reviews, Ordering, Compliance, Payroll, Invoicing.
- Positioning: "Forecasting, scheduling, inventory, payroll, and BI connected in one system. AI that predicts what's next and acts before you need to." "Labour and food will make or break your P&L." "Your best performing site, multiplied. Same forecasts. Same discipline. Same standards. Applied to every location at once."
- Customer evidence of the loop: Black Sheep Coffee — "having forecasting, labour and inventory connected in one place means every new site launches into an already established operating model. The controls are already there from day one." CUPP — replaced "Google Sheets, an old ePOS system, and Planday" (disconnected tools) with one system.
- Solutions: Independent brands / Franchise Networks / Multi-Location Brands / Enterprise Groups.

### HotSchedules / Fourth (Layer A)

- HotSchedules self-label: "The leading workforce management platform that's built for the hustle" — the labor-anchored pole.
- Fourth's wider **"Restaurant Operations Suite"**: Workforce Management (Scheduling, Schedule Scoring, Task Management, Time and Attendance, Restaurant Labor Compliance, Restaurant Manager LogBook, Tipping Management, Earned Wage Access); Inventory Management (Purchasing/Receiving & Invoicing, **Recipe & Menu Engineering Management**, Dynamic Production and Prep, Operations & Cash Management); Restaurant Data and Analytics (Business Intelligence Analytics, AI Forecasting for labor & inventory); Human Capital Management (talent acquisition, HR & payroll, PEO). Products: Adaco, HotSchedules, MacromatiX, Red Book Solutions.
- POS relationship: "Integrate with leading POS systems like **PAR POS, Toast, Oracle Micros, NCR Aloha**, and more to sync sales and labor data in real time. Managers get instant visibility into performance, labor costs, and demand trends, so every schedule, shift, and staffing decision is backed by data." → management layer consuming POS actuals; also names the legacy POS generation (Aloha, Micros) as the *other* side of the seam.
- Control-loop language: "Build accurate schedules in minutes using real sales and labor data"; "Match staffing to demand automatically… reduce overtime, cut waste"; "Predictive scheduling, labor law alerts, and built-in reporting."

## Cross-product Comparison

| Structure | Toast | Crunchtime | Restaurant365 | Nory | HotSchedules/Fourth | Layer |
|---|---|---|---|---|---|---|
| Restaurant operation (location/group) as managed unit | Y (1→100 locations) | Y (multi-unit, "every location") | Y (multi-location groups, franchise) | Y ("across every location") | Y (120k locations) | A |
| Labor & scheduling records | Y (Team Mgmt Suite) | Y | Y (Workforce) | Y (Workforce) | Y (core) | A |
| Stock / purchasing records | Y (xtraCHEF inventory) | Y | Y (Inventory & Purchasing) | Y (Inventory) | Y (Adaco/MacromatiX) | A |
| Menu / recipe records | Y (menu mgmt; xtraCHEF plate cost) | Y (recipe mgmt in inventory) | Y (Recipes; Fourth: Recipe & Menu Engineering) | unclear (not explicit on homepage) | Y (Fourth) | A (4/5) |
| Cost / financial targets (budgets, P&L) | partial (IQ insights, benchmarking) | Y (food/labor cost mgmt) | Y (budgeting, real-time P&L) | Y ("P&L on track") | Y (labor budgets, BI) | A |
| Sales forecasting | Y (Toast IQ) | Y (AI Forecasting) | Y (Sales Forecasting) | Y (demand forecasting) | Y (AI Forecasting) | A (5/5) |
| Plan-to-actual variance loop | Y (IQ insights; AvT via xtraCHEF) | Y (AvT; "what is really happening") | Y (actual vs theoretical labor; food cost variance; real-time P&L) | Y (labor cost variance; forecast accuracy) | Y (sales/labor data → schedules; BI) | A (5/5) |
| Multi-location comparison / standards rollout | Y (Multilocation mgmt, Benchmarking) | Y ("top performing stores") | Y (franchisee benchmarking) | Y ("best site, multiplied") | Y (across every location) | A (5/5) |
| POS as native surface | Y (Toast IS the POS) | N (integrates) | N (POS data input) | N (integrations) | N (integrates) | variant |
| Native payroll/HCM | Y | N (integrates) | Y | Y (payroll) | Y (HCM) | variant |
| Native accounting/GL | N (xtraCHEF AP automation; sends to accounting) | N (sends to accounting) | Y (full accounting) | N | N (sends to accounting) | variant |
| Ops execution (tasks/audits/food safety) | N (not surfaced) | Y | Y (task mgmt, logbook) | partial (compliance assistant) | Y (task mgmt, LogBook) | variant |
| KDS / guest-facing modules | Y (separate products) | Y | N | N | N | variant |
| Marketing / loyalty / gift cards | Y | N | N | N | N | variant |
| Finance services (capital, banking) | Y | N | Y (banking) | Y (Capital) | N | variant |
| Labor-law compliance machinery | Y (payroll compliance) | Y | Y (via payroll/HR) | Y (compliance assistant) | Y | common, regional |
| Benchmarking (cross-location/industry) | Y | Y (top performers) | Y (franchisee) | Y (benchmark page) | — | common |

Reading: **every sampled product** organizes around a managed restaurant operation, holds plan-side records in **multiple** resource domains, and runs a **plan-to-actual control loop** with location-level comparison. Everything else — POS anchoring, native accounting, payroll, ops execution, KDS, marketing, finance services — varies by product. No single resource domain beyond the multi-domain property itself is safe to call definitional (menu/recipes is 4/5 with Nory unconfirmed; accounting is 1/5 native).

## Abstraction (internal levels)

### L0 — Defining Invariant (three jointly-held structures)

1. **The restaurant operation as the managed unit of record** — a persistent, configured operating unit (a single site or a group of sites) that the system manages as a business: carrying its operating configuration and accumulating its performance history. Remove → generic BI / workforce / accounting tooling with no restaurant operation bound to it.
2. **Management records spanning multiple operating domains** — structured plan-side records governing at least two of the restaurant's resource domains (menu/recipes & pricing, labor & schedules, stock & purchasing, cost/financial targets), held in one system so the domains are managed together. Remove → the single-domain sibling Types (restaurant inventory management, employee scheduling, food cost management, menu management).
3. **The plan-to-actual control loop** — execution actuals (sales, labor worked, stock consumed/purchased, money spent) flow back against the plan records; performance is computed and surfaced (variances, cost percentages, forecasts vs actual, location comparisons) for management action back into the plan. Remove → static record-keeping; the "management" is gone.

Jointly-held load-bearing:

- 1 alone = generic company dashboard / BI territory
- 2 without 1 = disconnected domain tools (a scheduling app plus an inventory app)
- 3 without 1+2 = reporting over nothing
- 1+2 without 3 = a static configuration database; no management
- 1+3 without 2 = a dashboard over a restaurant with no plan records to act on

### L1 — Common Mature Structure

- forecast-driven labor scheduling (5/5)
- inventory/purchasing with invoice processing (5/5)
- sales/demand forecasting (5/5)
- performance dashboards & reports; variance surfacing (5/5)
- multi-location management: shared standards, location comparison (5/5)
- role-based permissions (manager vs corporate/admin) (observed across sample)
- mobile manager app (Toast Now, R365 Mobile, Fourth iQ App, Nory app) (4/5)
- payroll integration or native payroll (4/5 native, 1/5 integrated)
- menu/recipe records with plate costing (4/5)

### L2 — Variant / Optional Structure

- POS anchoring (Toast) vs POS-integrated back office (Crunchtime, R365, Nory, Fourth) — the dominant variant axis
- native accounting/GL (R365) vs hand-off to external accounting (Crunchtime, Fourth, Toast)
- ops execution layer: tasks, audits, checklists, food-safety/temp monitoring (Crunchtime, Fourth, R365)
- KDS / guest/host management (Crunchtime; Toast as separate products)
- marketing/loyalty/gift cards/guest CRM (Toast)
- finance services: capital, banking, instant deposit (Toast, R365, Nory)
- labor-law compliance machinery (regional: US predictive scheduling, EU working-time rules)
- benchmarking across locations/industry (Toast, Crunchtime, R365, Nory)
- franchise governance (R365 franchise brands; Crunchtime franchisee solutions; Nory franchise networks)
- commissary/production planning (R365 commissary; Fourth dynamic production)
- learning & development (Crunchtime, R365)
- AI assistance posture (era-current: Toast IQ, R365 AI, Nory agentic assistants, Fourth iQ, Crunchtime AI forecasting)

### L3 — Vendor-specific (research notes only)

- Toast: "Restaurant Management Suite" as a nav category (Benchmarking, Multilocation management); Toast IQ; Toast Now management app; xtraCHEF branding; Toast Capital/Checking; Toast Tables; claimed 180,000 locations.
- Crunchtime: "AvT" (actual vs theoretical) terminology; product lines Teamworx, Zenput/Ops Execution, Squadle, QSR Kitchen+Host; claimed 850+ brands / 150,000+ locations.
- Restaurant365: "R365 AI", "Chef's Table" early access; Compeat heritage (partner login domain compeat.my.site.com); claimed 52,000+ restaurants; LinkedIn self-label "cloud ERP for restaurants".
- Nory: agentic assistant crew (Scheduling/Ordering/Compliance/Payroll/Invoicing/Customer Reviews); Nory Capital; benchmark page.
- Fourth/HotSchedules: Fourth iQ; Adaco; MacromatiX; Red Book Solutions; Manager LogBook; Schedule Scoring; claimed 120,000 locations.
- Customer-count and result-percentage claims are vendor marketing figures; not generalized.

## Historical / Market-Sample Check

- **Paper-era check (conceptual, medium confidence — no primary source fetched):** a restaurant manager's office before software — menu & price list (menu/pricing governance), weekly staff schedule (labor plan), stock counts & order book (stock/purchasing), daily sales & cost figures vs targets, and a monthly P&L review (control loop) — satisfies all three L0 legs at analog level. The definition names no device, channel, cloud, or AI requirement.
- **Legacy back-office generation:** Fourth's own integration page names **NCR Aloha** and **Oracle Micros** as POS systems it syncs sales/labor data from — direct evidence that the 1990s–2000s POS generation (Aloha, Micros) sat on the *transaction* side while management layers (like Fourth's Adaco/HotSchedules lineage) sat on the *management* side consuming their actuals. The back-office-module generation (inventory + labor + reporting over a POS feed) therefore fits the definition. (Medium confidence: the Aloha/MICROS back-office products themselves were not directly fetched this pass.)
- **Regional check:** Nory (Europe-origin) and Fourth (US/EMEA/APAC regions) show the same structure across jurisdictions; labor-law machinery differs regionally and is held at L2.
- Conclusion: the definition is not overfit to the current cloud/AI generation.

## Vendor-specific Findings

See L3 above. Key one for the taxonomy: **Toast's own navigation separates "Restaurant POS" from "Restaurant Management Suite"** — direct vendor evidence that the market itself distinguishes the transaction surface from the management layer, supporting keeping both directory leaves.

## Boundary Findings

| Neighbor | Seam | Removal test |
|---|---|---|
| **Restaurant POS** | transaction surface vs management layer | strip the management layer (labor, stock, cost control, performance) → a POS remains; strip the transaction surface → a back-office management system remains (Crunchtime/R365/Nory/Fourth pole proves it) |
| **Restaurant Inventory Management** | single domain (stock) vs multi-domain center | strip costed recipes + variance loop → a stock system remains (per that pass); strip all but the stock domain → this Type collapses into it |
| **Restaurant Food Cost Management** | money/variance center vs multi-domain center | strip counting/receiving → costing survives on invoice prices (per that pass); strip all but the cost loop → collapses into it |
| **Employee Scheduling Platform** | labor domain vs multi-domain center | a scheduling-only product is the sibling; this Type holds labor as one domain among several |
| **Restaurant Menu Management** | guest-facing menu vs plan-side governance | menu management owns the menu object's depth; this Type holds menu/pricing as one plan domain |
| **Kitchen Display System / KDS** | kitchen fulfillment vs business management | KDS captures no orders and takes no payment (per that pass); orthogonal surface |
| **Restaurant Online Ordering / Reservation / Delivery Management** | customer-facing capture/fulfillment vs management layer | remove the customer surface → this Type unaffected; remove the management loop → those Types unaffected |
| **Institutional Foodservice Management** | commercial restaurant business vs institution feeding program (defined diner population, cycle menus, meal-service loop — confirmed from that pass) | remove the diner population/program machinery → commercial RMS; remove the commercial P&L center → institutional |
| **Catering Management** | discrete booked events vs ongoing operations | catering's spine is the booked event (per that pass); RMS has no event object |
| **Commercial Kitchen Management (§20)** | production-layer center (recipes/prep/food-safety execution) vs business-management center | Crunchtime spans both but its center is multi-unit ops management; strip production/food-safety execution → RMS remains |
| **Business Management Suite / ERP (§10)** | generic business management vs restaurant-domain operating content | R365's "cloud ERP for restaurants" self-label shows family resemblance; the restaurant content (menu, recipes, covers, food cost, labor rules) is the differentiator |
| **Retail Store Management System / Store Operations Platform (§05.11)** | retail analog | retail semantics (shrink, planogram, assortment) vs restaurant semantics (food cost, covers, kitchen) |
| **Hotel PMS** | lodging stay lifecycle vs restaurant operations | different center object (stay vs operating plan) |

**Naming observation (not a taxonomy error):** the market label "restaurant management system/software" is applied both to POS suites (Toast markets both; Lightspeed/TouchBistro market their POS as restaurant management systems — Lightspeed unverified this pass) and to POS-free back-office systems (R365, Crunchtime, Nory, Fourth). The directory's split (Restaurant POS | Restaurant Management System) is defensible: the canonical line is **management layer vs transaction surface**, and products bundle both. No directory change proposed.

## Uncertainties

1. **Lightspeed Restaurant unreachable** (403 + transport error). It is market-known to self-label "restaurant management system"; the POS-suite-pole naming evidence therefore rests on Toast's own nav split plus the restaurant-pos example document. Assertion strength reduced accordingly.
2. **Toast Benchmarking / Multilocation product pages 404** — suite membership evidenced from navigation only; depth of those modules not verified.
3. **Nory menu/recipe depth unconfirmed** — homepage inventory module description does not explicitly mention recipes; menu/recipes held at 4/5, not promoted to definitional.
4. **Historical back-office systems (Aloha Back Office, MICROS back office, Adaco history) not directly fetched** — historical check is conceptual + indirect (Fourth's integration page). Medium confidence.
5. **Module packaging/tiering** varies and changes frequently; no packaging claims made.
6. **Exact variance formulas, period-close mechanics, permission matrices** not researched to precision; deliberately not stated in the final document.

## Final Synthesis

A Restaurant Management System is the **restaurant business's management layer**: the system of record for the restaurant's operating plan — what it sells and at what prices, who works when, what stock to buy, and what costs to hit — held across multiple resource domains in one place, bound to a managed operation (a site or a group of sites), and coupled to a **plan-to-actual control loop**: execution actuals (sales, labor worked, stock consumed, money spent) flow back from the transaction and time systems (native or integrated), performance is computed against the plan, variances are surfaced, and management acts back into the plan.

The Type is definable **without** the POS: the back-office pole (Crunchtime, Restaurant365, Nory, Fourth/HotSchedules) proves a management layer that consumes POS actuals through integration. The Type is also realized **with** the POS: the POS-anchored pole (Toast) bundles the transaction surface and the management layer in one platform. The defining property is neither the POS nor any single resource domain — it is the **multi-domain plan + control loop over a managed restaurant operation**.
