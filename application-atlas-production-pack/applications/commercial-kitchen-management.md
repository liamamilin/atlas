# Commercial Kitchen Management

## Overview

A **Commercial Kitchen Management** application is back-of-house production management software for professional foodservice kitchens. It holds the kitchen's production knowledge — recipes built from ingredients, quantities, yields, and portions — turns that knowledge into planned production work (production plans and prep lists assigned to staff and workstations), records the work as it is completed, and runs the food-safety checks that a working kitchen must perform and document every day.

It solves a specific operational problem: in a professional kitchen, what to make, how to make it, how much to make, whether it was made safely, and what it cost are all held in people's heads, binders, spreadsheets, and paper logs. This application makes them structured, shared, scheduled, and auditable.

Its boundary: it manages the **production side** of a foodservice operation — the kitchen as a production unit. It does not display live order tickets during service (that is a Kitchen Display System), does not operate the point of sale or the dining room, and does not run the accounting. It connects to those systems rather than replacing them.

## Users & Context

Primary users:

- **Executive chef / head chef** — owns the recipe library, costing, and production standards; approves menu and recipe changes.
- **Sous chef / kitchen manager** — builds production plans and prep lists for the day, assigns tasks to staff and workstations, monitors completion.
- **Kitchen staff (cooks, prep cooks)** — execute prep tasks and checklists at their workstation; take temperature checks; print date labels.
- **Food-safety / quality lead** — defines critical control points and hygiene routines, reviews temperature logs and irregularities, produces records for inspections.

Secondary users:

- **Operations / multi-site management** — oversees consistency, food-cost variance, and task completion across locations; manages central production kitchens supplying outlets.
- **Procurement / finance** — consume ingredient prices, purchase orders, invoice data, and food-cost reporting.
- **Front-of-house staff** — read live allergen and nutrition information that flows from the recipe data.

The work environment is a hot, fast, hands-on production floor: the same application is used from an office desktop (building recipes, costing, planning) and from tablets or phones mounted or carried in the kitchen (executing prep lists, checklists, and temperature checks), often alongside label printers and temperature probes.

## Core Model

The application's world is the **kitchen as a production unit**. Five structures make it up.

### The kitchen site

A physical kitchen — an outlet or location — is the container for everything. A site contains **workstations or stations** (prep area, pastry, grill, wash-up) that tasks can be assigned to. Multi-site operations manage many outlets side by side, including **central production kitchens** that prepare food for other outlets.

### The recipe library (production knowledge)

The recipe library is the system's center of gravity: structured data about what the kitchen makes and how.

- A **recipe** specifies ingredients with quantities, produces a defined **yield** (weight, volume, or number of portions), and carries preparation instructions, production time, and often photos or videos of each step.
- **Sub-recipes** are recipes used as ingredients of other recipes (a sauce inside a dish). The library is therefore a composition tree: menus contain dishes, dishes contain sub-recipes, sub-recipes contain ingredients.
- **Ingredients** are the leaf data: purchase packages, units of measure, yields and prep-loss factors, current prices, suppliers, and — in mature products — allergen and nutrition attributes.
- **Cost** is derived, not entered: the cost of a recipe or portion is computed from its ingredient quantities and current ingredient prices, and re-computed when prices change.
- Some recipes are marked **stockable**: their output is a semi-finished product that can be held in stock and consumed by later production, like an ingredient.

### The production loop

Production knowledge becomes today's work through a **production plan** (also called a prep list):

```text
Demand input (forecast / sales mix / menu cycle / internal orders)
  → Production plan: recipe × quantity × assignee × workstation × time
  → Prep execution (staff complete tasks, with evidence)
  → Completion recorded
```

A production plan item names the recipe, the number of portions or units to produce, the person responsible, and the workstation. In mature products, planning a recipe that contains sub-recipes commonly expands the plan automatically: the required quantity of each sub-recipe is added as its own task, and some products let the sub-recipe be deducted from stock instead of produced if it is already on hand. Plans can also carry **custom tasks** that are not recipes (cleaning a station, taking out waste). Plans have a lifecycle — drafted, started, worked through, completed — and can repeat on a schedule.

### The food-safety loop

Kitchens must continuously verify and document safe food handling. The application records this as first-class data:

- **Temperature checks** — taken manually with a probe or automatically from fixed sensors — logged against items, equipment, or checks.
- **Hygiene and operational checklists** — opening, closing, cleaning, delivery-inspection routines, scheduled by daypart and day of week.
- **Corrective actions** — when a measurement is out of range, the record shows the exception and what was done about it.
- **Date labeling** — prepared items get labels with preparation date and use-by information, printed at the point of prep.
- **Audit-ready records** — every completed check carries who performed it and when, so an inspector's question ("show me last month's records") is answered from the system.

In HACCP-shaped implementations, the safety program is modeled explicitly: critical control points are defined, tasks are attached to them, and irregularities roll up into reports.

### The resource loops

Three loops connect production to the kitchen's resources:

- **Inventory** — ingredient stock records with counts; consumption flows out through production and sales; waste is recorded with reasons; stockable recipe output flows in when produced.
- **Procurement** — suppliers, purchase orders, receiving; supplier price updates feed ingredient costs.
- **Demand linkage** — point-of-sale sales data is mapped to recipes (menu items linked to their recipes), so the sales mix informs production planning and shows each dish's real profitability.

A final layer of **insights** reads across all loops: food-cost variance between theoretical and actual consumption, task-completion rates, waste, and per-site performance.

## How It Works

### Build the production knowledge base

```text
Add ingredients (packages, units, yields, prices, allergens)
→ compose recipes (quantities, steps, sub-recipes, yield, portions)
→ attach training media (photos / videos per step)
→ group recipes into menus
→ costs compute automatically from ingredient prices
```

This is usually the onboarding heart of the product: migrating recipes from binders, spreadsheets, and documents into structured data. The library is version-controlled and shared: a recipe change propagates to every site that uses it, and re-costs every menu that contains it.

### Plan and run production

```text
Choose the outlet and the planning horizon
→ select recipes/menus to produce (from forecast, sales mix, or menu cycle)
→ enter quantities (portions/units), assignees, workstations
→ sub-recipes commonly expand into their own tasks
→ start the plan
→ staff complete tasks at their stations (progress visible to managers)
→ complete the plan
```

The plan is the daily operating rhythm of the kitchen: what gets made, by whom, where, and whether it is done. Completion is attributed — the system records who finished each task and when.

### Run the food-safety routine

```text
Scheduled checklists appear at their daypart (commonly with a start, a due time, and an expiry)
→ staff work through items (checkboxes, measurements, photos, scans)
→ temperature readings logged from probe or sensor
→ out-of-range values trigger corrective action and notifications
→ records accumulate as the inspection-ready audit trail
```

### Close the resource loops

```text
Production and sales deplete ingredient stock
→ periodic counts reconcile records; waste recorded with reasons
→ stockable recipe output added to stock when produced
→ shortfalls become purchase orders to suppliers; receipts update stock and prices
→ price changes re-cost recipes and menus automatically
→ insights report food-cost variance, completion, waste per site
```

### What is defining vs standard vs optional

**The defining core** — without these, the application is not kitchen management:

- the kitchen site as the managed unit, with workstations
- the structured recipe library (ingredients, quantities, yields, sub-recipes, portions)
- the production loop: plan → prep → record, with attribution

**Standard capabilities** in mature products:

- food costing and menu engineering
- food-safety execution (temperature logs, checklists, corrective actions, date labels)
- inventory linkage (counts, depletion, waste)
- allergen and nutrition data on recipes
- multi-site management and internal ordering between sites
- sales/demand linkage from the POS
- procurement (suppliers, orders, receiving)
- reporting and insights

**Optional / variant** capabilities, depending on segment and product:

- labor scheduling and time clocks
- kitchen training programs built from recipes
- traceability down to lot level; label-printing integrations
- customer-facing digital menus and QR menus
- emissions/carbon labelling
- AI assistance (recipe capture from documents, invoice extraction, forecasting)

## Interfaces

### Recipe library editor (back-office desktop)

The chef's authoring surface.

- Purpose: create and maintain the production knowledge base.
- Typical information: recipe tree (menus → dishes → sub-recipes), ingredient lines with quantities and units, yield, portions, cost per portion, allergen and nutrition panels, attached media.
- Primary actions: create/edit recipes and sub-recipes, set yields and prep-loss, update ingredient prices, generate recipe sheets or share by link/QR, generate a bill of materials for a recipe or menu.

### Production planning view (back-office desktop)

- Purpose: turn demand into the day's production work.
- Typical information: planned recipes with quantities, assignees, workstations, sub-recipe expansions, progress state.
- Primary actions: create/copy/schedule plans, adjust quantities, assign people and stations, start, monitor, complete.

### Kitchen execution surface (tablet / station)

The surface kitchen staff actually touch during the shift.

- Purpose: show each person their work and capture evidence.
- Typical information: current prep tasks and checklists for the station or person, step-by-step recipe instructions with photos/videos, due states, temperature-check prompts.
- Primary actions: complete tasks (check, measure, photograph, scan), record temperatures, print date labels, flag problems.

### Food-safety console

- Purpose: keep the safety program running and inspection-ready.
- Typical information: checklist schedules and completion, temperature logs and sensor alerts, irregularities and corrective actions.
- Primary actions: define checklists and critical control points, review exceptions, generate audit reports.

### Inventory & purchasing surfaces

- Purpose: keep ingredients available and costs current.
- Typical information: stock levels by site and storage area, count sheets, waste records, supplier price lists, purchase orders, received-goods matches.
- Primary actions: count (often by phone with barcode scanning), record waste, raise orders, receive goods, process supplier invoices.

### Insights / dashboards

- Purpose: read the kitchen's economics and discipline.
- Typical information: food-cost variance (theoretical vs actual), margin per dish, task-completion rates, waste, per-site comparison.
- Primary actions: drill into a site, period, or recipe; export reports.

## Important Rules / Behaviors

- **Attribution is structural.** Every completed task, checklist item, and temperature reading records who performed it and when. This is what turns kitchen work into an accountable, auditable record, and it is enforced through signed-in users on shared kitchen devices (some products add PIN or personal-mode sign-in).
- **Sub-recipe expansion is a common planning behavior.** Planning a parent recipe commonly generates the required quantity of each sub-recipe as its own task; some products allow deducting an in-stock sub-recipe instead of producing it.
- **Costs propagate live.** Ingredient price changes re-compute the cost of every recipe and menu that uses them; chefs and managers see margin movement without re-costing spreadsheets.
- **Allergens propagate with the recipe.** Changing an ingredient updates the allergen and nutrition disclosures of every dish and menu containing it, keeping guest-facing information consistent with what the kitchen actually makes.
- **Safety checks have time discipline.** Checklists commonly appear at a scheduled start, become late after a due time, and expire if never completed; overdue items and out-of-range measurements notify designated roles.
- **Stockable output can become stock.** In some products, a recipe can be marked stockable: when it is produced, its output is registered into inventory and can be consumed by later production like a purchased ingredient.
- **Roles gate actions.** Completing work, managing plans, editing recipes, and overriding safety exceptions are typically separated by role; a staff member can execute without being able to restructure the plan or the library.
- **Multi-site consistency is enforced centrally.** Recipes and standards are authored once and pushed to all sites; sites execute rather than re-invent, and central production kitchens supply outlets through internal orders.

## Variants

- **By segment**: full-service restaurants; hotel F&B (multiple outlets, banquets, room service under one kitchen organization); quick-service chains (tight prep standards, high volume); pubs and bars (beverage-inclusive stock); catering and banquets (event-driven production runs); institutional foodservice (menu cycles over weeks); ghost/cloud kitchens (production without a dining room); central production units (cooking for many outlets).
- **By emphasis**: recipe-and-cost-data-led products, where the value is the structured culinary library and live costing; execution-and-compliance-led products, where the value is checklists, temperature logging, and accountability on the floor. Most mature products cover both, but they lean one way.
- **By scale**: single-site lite editions; multi-unit groups; enterprise chain suites where kitchen management is one module beside labor, learning, and guest management.
- **By integration depth**: standalone culinary systems that sync to a separate back-office/inventory system; versus suites that include inventory, purchasing, and accounting natively.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Kitchen Display System / KDS | adjacent — and a naming hazard | A KDS displays live order tickets from the POS during service and routes them to stations; it is demand-driven and minute-scale. Commercial Kitchen Management is plan-driven and day-scale: knowledge, planning, prep, safety. Some vendors market a KDS under the name "kitchen management"; the two remain different Types. |
| Restaurant Inventory Management | capability overlap | Inventory-centric products make stock the primary object. Here, inventory is one loop serving production; the recipe library and production plan are primary. |
| Restaurant Food Cost Management | specialization | Food-cost analytics is one standard capability here; a standalone food-cost product lacks the production loop and safety execution. |
| HACCP Management / Food Safety Management | adjacent | Food-safety-plan-centric products manage hazards, critical control points, and compliance documentation as the primary object. Here, safety execution is one loop inside production management. |
| Food Manufacturing ERP | adjacent | An ERP runs a manufacturing business: financials, MRP, lot compliance, production orders. This Type runs a foodservice kitchen with culinary semantics — menus, portions, POS linkage, guest-facing allergen data. |
| Institutional Foodservice Management | adjacent | Institutional products manage meal-service programs (resident/patient menus, nutrition care, tray service). This Type is the kitchen production layer beneath such programs; menu-cycle planning is the overlap zone. |
| Restaurant Management System | broader | Restaurant management includes front-of-house (POS, reservations, payments). This Type is back-of-house only and integrates to the POS rather than operating it. |
| Catering / Banquet Management | adjacent | Event-driven production for booked functions; this Type supplies the ongoing production machinery beneath events. |
| Store Task Management | cousin | Retail-store checklist execution shares the task/attribution mechanics of the execution pole, but has no structured recipes or production planning; without those it is not kitchen management. |

## Representative Products

- **ApicBase** — recipe/food-cost data backbone with production planning, HACCP tasks, inventory, procurement, and POS linkage; multi-site groups, hotels, ghost kitchens, catering.
- **Kitchen CUT** — F&B operations platform: live-costed recipes, allergen/nutrition labelling, procurement, inventory, waste, and central production units; hotels, restaurants, pubs, QSR, leisure.
- **meez** — recipe-first "culinary system of record": structured recipes, live costing, scaling, kitchen training, allergen management; multi-unit restaurant groups.
- **Jolt** — execution-led kitchen operations: scheduled checklists with item-level attribution, temperature probes and sensors, date-code labeling; SMB restaurants and franchisees.
- **Crunchtime** — enterprise chain operations suite: inventory and food-cost management, operations execution (tasks, audits, temp monitoring, prep labeling), beside labor and KDS modules.

## Sources

Research date: **2026-09-07**

- ApicBase Help Center — https://support.apicbase.com/help (incl. Planning: Tasks & HACCP, Production Plan, Menu Planning; Menu Engineering; Inventory; Traceability)
- Kitchen CUT — https://kitchencut.com/ (module and sector pages, incl. Central Production Unit)
- meez — https://www.getmeez.com/ (feature pages and FAQ)
- Jolt / SmartSense — https://www.jolt.com/ and https://help.smartsense.co/en/ (incl. "Getting started with Jolt lists")
- Crunchtime — https://www.crunchtime.com/ (suite overview and module pages)

> Sourcing limitations: Galley Solutions, a market participant in production-planning-led kitchen software, was unreachable from the research environment (its web and help surfaces failed repeatedly) and is therefore not characterized here; the production-planning pole is evidenced by the sampled products above. The meez help center timed out, so meez observations rest on its official product pages and FAQ. Apicbase's marketing site was unreachable (HTTP 405); ApicBase evidence comes from its help center. Precise numeric limits, plan gating, and pricing are intentionally not stated; none were required for the model above.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
