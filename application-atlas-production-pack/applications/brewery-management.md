# Brewery Management

## Overview

A **Brewery Management** application is the brewery's system of record for its beer production business. It holds beer recipes as controlled production definitions, turns each recipe into a numbered batch, carries that batch through a production lifecycle — brew day, fermentation and conditioning over days to weeks, packaging into kegs and cases — while recording time-stamped process measurements along the way, and keeps the material books on both sides of production: ingredients drawn down, packaged beer produced.

The defining core is deliberately small:

```text
Recipe (production definition)
  └── Batch (tracked production run of a recipe)
        └── lifecycle: brew → ferment/condition → package → completed
        └── process measurements recorded over time
  └── Materials inventory (ingredients consumed, packaged beer produced)
```

Planning, tank scheduling, sales, costing, and compliance reporting are standard commercial machinery layered around this core — widespread in mature products but dependent on the brewery's size and market, not part of what makes the software a brewery management system. When the process model drifts away from recipe-driven, time-extended fermentation toward generic manufacturing orders, the product is drifting toward a Food Manufacturing ERP; when the beverage and process records change to grapes, vintages and barrels, it has become the equivalent application for another fermented beverage (e.g. wine).

## Users & Context

The primary users are the people who make and sell the beer:

- **Head brewer / production manager** — designs and versions recipes, plans batches, owns yield and consistency
- **Brewers / cellar staff** — run brew days, take readings, perform transfers and additions, package the beer; in mature products they enter their own production records
- **Owner / general manager** — watches cost, margin, inventory value, and sales
- **Taproom or sales staff** (where present) — consume the finished-goods picture and place or fulfill orders

The context is a production facility running a small number of vessels in parallel, each holding an active batch for days or weeks. Unlike transaction software, the work here is mostly **logging and monitoring over time**: the beer changes on its own schedule, and the software's job is to make that invisible process visible, comparable, and costed. Breweries range from nano and brewpub scale to regional producers; the software scales with them by adding machinery, not by changing the core model.

## Core Model

### The Defining Core

**Recipe.** The controlled definition of a beer: the grain bill, hop schedule, yeast, and process parameters (mash steps, boil, fermentation profile), together with target figures — original and final gravity, ABV, bitterness, color. Recipes are versioned as they evolve and can be scaled to any batch size. The recipe is the thing that makes production repeatable; everything else is an instance of it.

**Batch.** The tracked production run of a recipe at a specific scale and date, normally carrying an auto-incremented batch number and the name of the brewer responsible. The batch is the center of the system: measurements, events, costs, and packaged output all attach to it. A batch typically records the exact recipe snapshot it was brewed from, so later recipe edits do not retroactively alter production history.

**The batch lifecycle.** A batch moves through a sequence of production states — planned, on brew day, fermenting, conditioning, completed — that products implement as explicit, user-visible statuses (conceptual states shown; exact labels and boundaries vary by product):

```text
Planned → Brewing (brew day) → Fermenting → Conditioning → Completed → Archived
```

The stages after brew day run on the beer's own clock — fermentation takes days to weeks, and the software tracks the batch across that time with day counters, due dates (ready to package, ready to drink) and overdue flags. Completed batches become the permanent production record; some products make archived batches read-only to protect the history.

**Process measurements.** Gravity and temperature readings are the canonical record, taken manually or streamed automatically from in-tank devices; products compute attenuation and ABV from them and draw fermentation curves against past batches so abnormal fermentations are visible early. Depending on the product, additional checks (pH, dissolved oxygen, sensory and lab results) log against the batch under the brewery's own quality program.

**Materials inventory.** The same books cover both sides of production: raw ingredients (malt, hops, yeast, adjuncts) and packaging materials enter stock; batches consume them as brewing proceeds; packaging converts finished beer into finished-goods inventory (kegs, cans, cases) identified by batch. This is what connects the brew log to money — batch cost, and ultimately margin, derive from materials charged to batches.

### Standard Capabilities of Mature Products

These are widespread in commercial-tier products and expected by serious breweries, but their presence or absence does not change what the software is:

- **Vessels and tanks** — a register of fermenters, brite tanks and barrels with what is currently in each, day-in-state counters, and scheduling of upcoming batches to avoid conflicts (drag-and-drop calendars in some products)
- **Cellar events** — transfers between vessels, dry-hop and other additions, yeast handling including generation lineage, recorded against the batch
- **Quality checkpoints** — brewery-defined QA steps and lab results logged per batch
- **Lot traceability** — ingredient lots consumed and finished goods produced are linked through the batch, so any ingredient problem can be traced forward to affected packages and any returned package back to its batch
- **Production planning** — scheduling upcoming batches, material requirements projections from planned production, and reorder alerts on ingredients
- **Sales and distribution** — sales orders, deliveries to wholesale accounts, keg-fleet tracking, and in some products lightweight CRM for account management
- **Costing** — batch cost and COGS, often synced to accounting software
- **Team machinery** — task assignment, notifications, and role permissions for staff
- **Device integrations and APIs** — in many products, wireless hydrometers and fermentation controllers feed readings automatically; export interfaces move records out
- **Reporting** — yield, beer loss, tank utilization, production costs

The clearest evidence that these are tier structure rather than definition: self-serve products used successfully by commercial breweries exist without tanks, sales, or permission machinery, while ERP-flavored products exist where these records live inside a broader financial suite.

## How It Works

The canonical workflow runs from recipe to revenue:

```text
Design or adjust the recipe
→ plan a batch (date, scale, vessel where applicable; check material availability)
→ brew day: execute and log the brew against the recipe
→ cellar: record readings and events while the beer ferments
→ package into kegs/cans/cases (finished-goods inventory, coded by batch)
→ sell: fulfill orders from finished goods; kegs circulate and return
→ review: compare batches, yields, and costs
```

**Design and plan.** The brewer maintains the recipe; target figures recalculate as ingredients change. Planning a batch means scheduling a brew date (and, in vessel-aware products, reserving a tank), with material projections showing whether ingredients will last until then.

**Brew day.** The recipe becomes a guided checklist — mash steps, additions, boil times, with timers — and the brewer records what actually happened: actual volumes, temperatures, gravity readings. This brew log is the batch's birth record.

**Cellar.** Over the following days and weeks, readings accumulate into a fermentation curve, compared against prior batches of the same recipe so drift is caught while the beer can still be saved. Transfers to other vessels, dry hops, yeast cropping, and quality checks are logged as dated events on the batch.

**Packaging.** When the beer is ready, it is packaged into kegs, cans, or cases. The packaging run converts tank contents into finished-goods inventory identified by batch (and often lot-coded with dates), completing the chain from ingredient to sellable unit.

**Sell and review.** Sales orders draw down finished goods; kegs are tracked out and back. Continuously or periodically, the brewery reviews the accumulated record — batch-to-batch comparisons, brewhouse yield, beer loss, ingredient and batch costs — which is where the software pays for itself.

## Interfaces

The surfaces below are described conceptually; exact layouts vary by product.

### Dashboard

The operational entry point: batches grouped by lifecycle status (planned, brewing, fermenting, completed), brew-day and overdue flags, tank utilization, and task queues. Purpose: answer "what needs attention today" in one view.

### Recipe editor

Ingredient lists and process steps with live-calculated targets (gravity, ABV, bitterness, color) against style references; version history; scaling controls. Primary actions: create/edit recipe versions, scale, start a batch from a recipe.

### Batch detail

The heart of the system: the brew log, the readings table and fermentation chart, dated events (transfers, additions, packaging), costs, and attachments such as lab reports. Primary actions: advance the batch's state, add readings and events, record packaging.

### Tank / vessel board

Commercial-tier surface showing each vessel, its current batch, days in state, and upcoming schedule. Primary actions: schedule a batch into a vessel, log a transfer, check what is where.

### Inventory

Ingredient stock with lot detail and reorder state, packaging materials, and finished goods by batch. Primary actions: receive stock, adjust counts, trace lots, view cost.

### Sales / orders

Where present: sales orders and deliveries to accounts, keg movements, customer records. Primary actions: create/fulfill orders, track kegs out and returned.

### Reports

Batch comparisons, yield and loss, production costs, and — depending on region and product — compliance reports prepared from the batch record.

## Important Rules / Behaviors

- **The batch records history, not intentions.** A batch captures the recipe snapshot and the actuals measured on the day; later recipe changes do not rewrite past production records. Archived batches are read-only.
- **The lifecycle runs on the beer's clock.** State advancement is driven by dated events (brew date, fermentation start, packaging date), and the software flags overdue or due batches — the batch is a time-extended object, unlike a transaction.
- **Inventory follows the process.** Ingredient stock is drawn down as brewing proceeds and finished goods appear at packaging; products that handle the edge cases (mid-process recipe changes, split or merged batches) account for every correction so counts and costs stay trustworthy.
- **Measurements are the quality instrument.** Gravity and temperature over time, compared across batches, are how problems are caught before batches are lost — the reason readings are first-class records rather than notes.
- **Traceability runs both directions** through the batch: ingredients forward into packaged beer, and any packaged unit back to its batch and input lots.
- **Vessels are exclusive.** A tank holds one batch at a time; scheduling machinery exists to prevent conflicts and make occupancy visible.
- **Permissions follow the production floor.** In team products, production staff record their own work while managers control configuration, approvals, and financial views.

## Variants

- **Recipe-first self-serve products** — recipe design, brew-day guidance, and fermentation tracking for hobbyists through small commercial breweries; commercial depth (tanks, sales, costing) arrives as paid tiers rather than modules
- **Planning-first products** — visual batch scheduling and material requirements as the headline, marketed as "brewery ERP"; strongest at nano-to-regional scale
- **Data/QC-first products** — deep process measurement, lab and fermentation analytics, batch costing, with full production-to-distribution scope for established craft breweries
- **ERP-embedded deployments** — the same production records living inside or beside a financial ERP; larger breweries sometimes deliberately split: ERP for money, brewery management for process
- **Multi-beverage platforms** — the same record structure sold to wineries, cideries, meaderies, distilleries, and kombucha producers, with the process vocabulary swapped
- **Brewpub vs production emphasis** — taproom-led businesses use the sales/inventory side differently from distribution-led producers

## Related Application Types

| Application Type | Distinction |
|---|---|
| Food Manufacturing ERP | models generic batch manufacturing (BOM, work orders, lots) without the brewing process model — recipe-driven fermentation, gravity/yeast semantics, vessel occupancy over weeks; remove those and this Type collapses into it |
| Winery Management | the sibling fermented-beverage equivalent: same record structure, different process chain (crush, press, aging, blending; vintages and grape lots) |
| Food Formulation Platform | R&D-centric recipe development (nutrition, specifications, labeling); its recipes are filed, not brewed — no batch lifecycle |
| Food Traceability Platform | centers on recall/exposure workflows; here traceability is a capability that falls out of the batch record, not the center |
| Production Planning / APS / MES | generic manufacturing scheduling and execution; planning is one machinery layer here, and the batch record with its measurements is the center |
| CMMS / Equipment Administration | treats vessels as maintenance objects; here they are production containers with contents and state |
| Restaurant Management / Restaurant POS | the taproom sale is a different Type; this software touches it only through sales orders, inventory depletion, and integrations |

## Representative Products

- Beer30 (The 5th Ingredient) — production/QC-data-centric, commercial craft
- BrewPlanner — production-planning/"brewery ERP", nano to regional; also sold for wineries and cideries
- Brewfather — recipe-first self-serve product spanning hobbyist to commercial breweries
- Ekos — widely cited craft market leader (referenced as market anchor; not directly examined in this research pass)

## Sources

Research date: **2026-09-06**

- Beer30 — product pages — https://the5thingredient.com/ , https://the5thingredient.com/beer30-software/
- BrewPlanner — product page — https://brewplanner.com/
- Brewfather — product page and documentation — https://brewfather.app/ , https://docs.brewfather.app/ , https://docs.brewfather.app/batches.md

> Sourcing limitation: Ekos (ekospm.com), Brew Ninja (brewninja.biz), and Orchestrated Beverage (orchestratedbeverage.com) could not be fetched from the research environment and were abandoned after repeated transport errors. They are referenced only as market anchors; no structural claims about them are made. Precise vendor figures (marketing claims, plan prices, numeric limits) are intentionally excluded from this document; the evidence base rests on three directly examined products across three product philosophies and customer tiers.
