# Research Notes — Brewery Management

## Research Goal

Understand what a Brewery Management application actually is, from real products: what the central objects are (recipe, batch, tank, lot, keg, order), how the production workflow moves from recipe to packaged beer to sale, which brewing-specific structures make this a distinct Type rather than generic manufacturing software, and where the boundary lies with adjacent Types (Food Manufacturing ERP, Winery Management, Food Traceability, production planning/MES, CMMS).

## Initial Boundary (hypothesis before research)

- Expected core: beer recipes + production batches with a brew→ferment→package lifecycle + fermentation/process measurements + ingredient inventory + packaging (kegs/cases) + sales to distributors/taproom, with brewing science (gravity/ABV, yeast, water) as the domain-specific layer.
- Likely confusions: Food Manufacturing ERP (generic batch manufacturing), Winery Management (same shape, wine), Food Formulation Platform (recipe/R&D-centric), Food Traceability Platform (recall slice), Production Planning/APS/MES (generic execution), CMMS (equipment slice), Restaurant Inventory Management (taproom side), Farm Management (upstream raw material).

## Research Questions

1. What is the central object — the recipe, the batch, or the tank?
2. How does the batch lifecycle work (states, dates, who advances it)?
3. What brewing-specific measurements and science does the software capture (gravity, temperature, pH, VDK, DO, yeast lineage, water chemistry)?
4. How does inventory work (ingredient lots, deduction mechanics, packaging materials, finished goods)?
5. How do vessels/tanks factor in (scheduling, conflicts, contents visibility)?
6. How far does the Type extend commercially (sales orders, CRM, keg fleet, accounting/COGS, compliance reporting such as US TTB)?
7. What roles and team machinery exist (tasks, permissions, multi-site)?
8. What exceptions matter (batch failures, yield/beer loss, vessel conflicts, split/merged batches, out-of-stock on brew day)?
9. Where is the boundary with Food Manufacturing ERP / Winery Management / traceability / planning tools?

## Representative Products

| Product | Vendor | Why sampled |
|---|---|---|
| Beer30 | The 5th Ingredient Inc. | Commercial craft segment; explicitly "built around the brewing process"; data/QC-centric philosophy (300+ data points, fermentation curves, lab modules); full production+sales scope; strong documentation of compliance (TTB) and accounting integration |
| BrewPlanner | Crucible Fund | Production-planning/ERP philosophy; nano→regional tier; explicitly marketed as "Brewery ERP"; scheduling-across-vessels emphasis; also sells the same platform to wineries/cideries/meaderies/distilleries — useful for family-boundary analysis |
| BrewFather | Warpkode AS (Norway) | Recipe-designer philosophy; free/premium self-serve tier spanning hobbyist→commercial; richest official documentation (GitBook docs) giving direct Layer-A evidence of the batch state machine and recipe-snapshot mechanics |
| Ekos | Ekos (market anchor) | Widely referenced craft market leader; unreachable during research (see Sources) — positioning-level only |
| Orchestrated Beer / Ollie | (market anchors) | Named by Beer30 customers and BrewPlanner's own comparison pages as the products breweries switch from/to; sites unreachable — positioning-level only |

Three directly observed products with three different product philosophies (data/QC-first, planning/ERP-first, recipe-first) and three customer tiers (commercial craft mid-market, nano→regional, self-serve prosumer→commercial). Plus two positioning-level anchors confirming market structure.

## Sources

Fetched 2026-09-06. Evidence layers used below: **A** = directly observed on a specific source; **B** = cross-product commonality; **C** = canonical inference.

- Beer30 — homepage — https://the5thingredient.com/ (fetched 2026-09-06; full text)
- Beer30 — product page — https://the5thingredient.com/beer30-software/ (fetched 2026-09-06; full text)
- BrewPlanner — homepage — https://brewplanner.com/ (fetched 2026-09-06; full text, incl. feature grid, pricing tiers, FAQ, verticals)
- Brewfather — homepage — https://brewfather.app/ (fetched 2026-09-06; full text)
- Brewfather — documentation readme — https://docs.brewfather.app/ (fetched 2026-09-06; full text)
- Brewfather — Batches documentation — https://docs.brewfather.app/batches.md (fetched 2026-09-06; full text)
- Ekos — https://www.ekospm.com/ and https://www.ekospm.com/brewery-software/ (transport errors ×2 each — abandoned; Ekos retained as market anchor only)
- Brew Ninja — https://brewninja.biz/ (transport errors ×2 — abandoned)
- Orchestrated Beverage — https://orchestratedbeverage.com/ (transport errors ×2 — abandoned)

## Source Observations

### Beer30 by The 5th Ingredient (Tier 2 product pages — evidence A)

Positioning: "Customizable Brewery Management Software… organizes the chaos at your brewery… Track Inventory, Manage Sales & Distribution, Improve Production Processes." Claims analysis of "300+ data points" (marketing figure).

Production/process machinery:

- Brew logging: "Multiple users are able to enter real time data from the mash to the packaged product" (customer testimonial); replaces "paper batch cards" and brew logs
- Batch tracking: "precisely track the life cycle of our beer from the brewhaus all the way to our distributors"; COGS and batch tracking; batch history reports
- Fermentation data: "compare trends across batches and recipe variations, like daily gravity, pH, temperature, VDK"; "live fermentation curves… compares your current production to past batches" against "historical averages and… Gold Standard targets"; "catch problems with your beer before they happen" (avoid dumped batches)
- Tank machinery: "Tank Visibility & Scheduling… see exactly what's going on with your tanks and streamline your tank scheduling"; "tank monitoring, QA/QC, transfers, yeast management & batch tracking"; "day counters on the dashboard and tank action automation built into the recipes"; "tank tags keep the entire staff in the loop"; tank utilization on dashboards
- Yeast: "yeast management… visibility on where your generations came from" (yeast lineage)
- Lab/QA: custom "diacetyl testing module… tracked by batch and user"; QA department goals; sensory panel data
- Barrel aging program reports

Inventory & cost:

- Raw materials, packaging materials, packaged goods inventory; "live inventory values at all times and at all levels of our beer production"
- "Inventory updates itself automatically as you are going through the brewing process"
- "Proprietary lot traceability on all of your inputs, and finished goods traceability on your cases and kegs"
- "You'll never have inventory discrepancies due to negative inventory on certain inputs, or mid-process recipe adjustments, or split/merged batches. We'll account for every change… from costing to counts"
- COGS from raw materials to sold product; raw material costing over time; Xero / QuickBooks Online / NetSuite integration

Planning:

- Demand Planning (forecast sales and production, reconciled), Just-in-Time (JIT) reports (outgoing sales and packaging runs "down to the day", inventory days on hand), Material Resource Planner ("see the inventory impact of your planned production, even months in advance")

Sales & distribution:

- "CRM capabilities… full contact management suite, the ability to track account visits and activities, full sales order management, deliveries, and keg fleet tracking"
- Sales/COGS tracking; sales dashboards

Team & admin:

- Task management ("assign activities… monitor when and how they've been done"), optional text/email notifications, "full set of permissions", unlimited licenses
- Command Center real-time dashboards: sales, tank utilization, beer loss, supply chain vulnerabilities, COGS analyses

Compliance: "make TTB reporting as simple as a few clicks" (US Alcohol and Tobacco Tax and Trade Bureau reporting)

Ecosystem: Beer30 API; integrations page; NetSuite edition ("Enterprise-Level Power"); Beer30 Lite (lower tier); Pinty AI assistant; dedicated WhatsApp support channel; sister product Bucha30 for kombucha ("Industry-Leading Kombucha Software") — same pattern extended to another fermented beverage.

Competitor evidence from customers: multiple named customers switched from Orchestrated Beer (described as finance-first: "muddled in an ERP database that wasn't really designed for qualitative data"; production staff couldn't enter their own brew logs); one chose Beer30 over Ollie because Ollie's production module was "not integrated at all with the sales software… two completely different packages". One large customer runs Beer30 alongside an MRP/ERP: "The ERP is used for quantitative data while Beer30 is used for qualitative data… Beer30 serves as our QC and batch tracking database."

### BrewPlanner (Tier 2 product page — evidence A)

Positioning: "The production planning software breweries actually want to use… all-in-one brewing software platform with batch scheduling, inventory management, and recipe management… Brewery ERP and production scheduling that scales from nano breweries to regional wineries." Claims 500+ breweries & wineries (marketing figure).

Feature machinery:

- Batch Tracking Software: "Track every beer or wine batch from brew day to packaging. Monitor fermentation temps, log gravity readings, and maintain a complete batch history for compliance and quality control"
- Recipe Management: "Create, version, and scale brewing recipes and wine blends. Store grain bills, hop schedules, yeast strains, and process steps with one-click batch scaling"
- Inventory Management: "Track hops, malt, yeast, grapes, and packaging supplies with real-time stock levels. Automated reorder alerts and MRP calculations"
- Batch Scheduling & Production Planning: "Drag-and-drop batch scheduling across fermenters, brite tanks, and barrels. Avoid vessel conflicts and optimize brewing throughput with a visual production calendar"
- Quality Assurance: "Log QA checkpoints at every stage… Track dissolved oxygen, pH, gravity, and sensory data to ensure batch-to-batch consistency"
- Production Analytics & Reporting: "Track yield rates, production costs, and efficiency trends"
- Team Collaboration: "Assign tasks, share production notes" across shifts/locations
- Multi-Location: "Run multiple brewing or winemaking facilities from a single account. Compare production performance across locations and share recipes between sites"
- Keg tracking + API access (ERP tier)
- Purchase orders and sales orders (ERP tier)

Process vocabulary displayed on the page: Recipe → Grain → Milling → Mashing → Lautering → Boiling → Hops → Whirlpool → Cooling → Fermentation → Conditioning → Filtering → Carbonation → Packaging/Bottling → Quality → Distribution → Taproom (and the parallel wine chain: Crushing → Pressing → Aging → Blending).

Verticals: breweries, wineries, distilleries, cideries, meaderies — "one platform, multiple craft beverage producers". Owns dedicated comparison pages "Ekos Alternative" and "Ollie Alternative" (confirms both as market anchors).

Pricing tiers: Production Planning ($49/mo: scheduling, calendar, recipes, 3 users) vs Brewery ERP ($125/mo: + inventory/MRP, analytics, purchase/sales orders, keg tracking, API) — plan boundary is commercial machinery, not the production record.

### Brewfather (Tier 1 documentation — evidence A)

Positioning: "The all-in-one brewing app for recipe design, batch tracking, guided brew days and live fermentation monitoring… One account — every device, online or offline." Free tier + Premium + Premium Plus (AI). Explicitly allows commercial use: "features like lot numbers, best-before dates, batch cost per liter, a brewer field and printable stock lists support full batch traceability. Plenty of commercial breweries run on Brewfather."

Recipe machinery:

- Recipe designer with live recalculated OG, FG, ABV, IBU, color against style guidelines (BJCP and custom); choice of IBU formula; scaling to any batch size; recipe versioning ("every version" kept); recipe folders; equipment/mash/fermentation/water profiles; ingredient database; BeerXML/BeerJSON import-export (interchange standard)
- Water chemistry: "water profiles with salt additions and estimated mash pH"; multiple pH estimation engines
- Calculators: ABV, hydrometer/refractometer correction, carbonation, strike water, IBU, yeast pitch rate/starters

Batch lifecycle (docs.brewfather.app/batches — full state machine, directly observed):

- Status sections: **Planned → Brewing → Fermenting → Conditioning → Completed → Archived**
- "Conditioning is a sub-status within the Fermenting stage… A batch transitions to Conditioning when you advance it forward from Fermenting. From Conditioning, you can move the batch to Completed."
- "Archived batches are read-only — all measured value fields become non-editable."
- Batch created from a recipe ("brew button" on the recipe screen); "The batch records the exact recipe snapshot for that version."
- "When moving a batch through status transitions, the app automatically prompts you to set key dates: the brew date when moving to Brewing, the fermentation start date when moving to Fermenting, and the bottling date when moving to Conditioning or Completed."
- Batch cards: batch name and number ("My IPA #42"), measured ABV badge, status badges ("Brew Day!", "Overdue X days", "Day X" for fermenting, "in X days", age badge), taste rating, cost per liter for completed batches, attachment count
- Batch Overview dashboard: "Brew Day Today", "Overdue Planned", "Upcoming Brews (7d)", "Ready to Bottle", "Bottling Soon (7d)", "Ready to Drink", "In Progress", "Completed This Month"
- Readings: specific gravity, temperature, attenuation, ABV; manual readings or device streaming (Tilt, iSpindel, RAPT, Brewtools, Float, Plaato, BrewPiLess, Custom Stream HTTP endpoint); fermentation progress bar; fermentation chart with profiles and scheduled temperature steps
- Brewer attribution ("sort by Brewer — this is probably of more use in a commercial environment"); batch notes; file attachments ("photos, lab reports"); duplicate; export (PDF, BeerXML, BeerJSON, readings CSV); public view-only share links
- Guided brew day: recipe becomes "a step-by-step checklist with timers for every mash step, addition and rest"; alarms sync across devices
- Inventory: "tracks every gram in your store and deducts what you brew"; stock levels and cost per batch; shopping list
- AI assistant (Premium Plus): creates recipes from an idea, modifies open recipes ("replace out of stock ingredients"), answers from your batches and inventory ("What can I brew with what I have?")

What Brewfather notably does NOT show at this tier: vessel/tank management, sales orders/CRM, compliance reporting, multi-user permissions machinery (single-account model). This absence is analytically important: it shows the commercial machinery is tier- and segment-dependent, not definitional.

### Cross-source: market structure

- Beer30 testimonials + BrewPlanner alternative pages + the category's own vocabulary ("brewery management software", "brewery ERP", "brewing software") confirm a stable category with named players (Ekos, Orchestrated Beer, Ollie, Beer30, BrewPlanner, Brewfather…).
- Switching patterns show the axis of differentiation: process-data depth vs financial/ERP depth vs planning depth; and integrated sales+production vs separated modules.

## Cross-product Comparison

| Dimension | Beer30 | BrewPlanner | Brewfather |
|---|---|---|---|
| Philosophy | production/QC data-centric ("built around the brewing process") | planning/ERP-centric ("production planning… brewery ERP") | recipe/brewer-centric (design → brew → ferment) |
| Recipe | specified per batch; recipe variations; tank actions built into recipes | versioned, scaled, one-click batch scaling; grain bills/hop schedules/yeast strains/process steps | full designer; live stat calculation; versioning; style guidelines; BeerXML |
| Batch | batch lifecycle tracking; batch history reports | brew day → packaging; complete batch history | explicit state machine Planned→Brewing→Fermenting→Conditioning→Completed→Archived; recipe snapshot at brew |
| Process measurements | daily gravity, pH, temp, VDK; diacetyl module; fermentation curves vs Gold Standard | fermentation temps, gravity; DO, pH, sensory QA checkpoints | gravity, temp, attenuation, ABV; manual or 20+ device streaming; fermentation chart |
| Vessels/tanks | tank visibility, scheduling, day counters, transfers | drag-drop scheduling across fermenters/brite tanks/barrels; vessel conflict avoidance | none at this tier (per-batch model) |
| Yeast | yeast management, generation lineage | yeast strains in recipes; yeast inventory | yeast calculators, pitch rate, starters |
| Inventory | raw materials, packaging materials, packaged goods; automatic deduction through process; lot traceability in and out | hops/malt/yeast/packaging supplies; real-time stock; reorder alerts; MRP | ingredient stock & cost; deducts what you brew; shopping list; lot numbers, best-before dates |
| Finished goods / kegs | cases and kegs traceability; keg fleet tracking | keg tracking (ERP tier) | Plaato Keg device integration only |
| Sales/commercial | CRM, contacts, account visits, sales orders, deliveries | sales orders, purchase orders (ERP tier) | none |
| Accounting/COGS | Xero/QBO/NetSuite; COGS; batch costing | production costs analytics; cost tracking | cost per batch / per liter |
| Planning | demand planning, JIT, MRP | MRP, reorder alerts; visual production calendar | brew-date planning; overview dashboard |
| Compliance | TTB reporting "as simple as a few clicks" | batch history "for compliance" | traceability + best-before dates (compliance-adjacent) |
| Team | tasks, notifications, full permissions, unlimited licenses | task assignment, shared notes, multi-location | single-account; brewer field |
| Scope extension | Bucha30 (kombucha); NetSuite edition | wineries, cideries, meaderies, distilleries on one platform | homebrew→commercial; community recipe library |
| Devices/IoT | (not emphasized on fetched pages) | (not emphasized) | 20+ wireless hydrometers/controllers, custom stream, API/webhooks |

**Convergence (B):** all three sampled products organize the world around (1) recipes as controlled production definitions, (2) batches as tracked instances moving brew→ferment→package, (3) measurement records against batches (gravity/temperature at minimum), and (4) ingredient inventory consumed by production. Every product additionally carries some of the commercial machinery (planning, sales, COGS, kegs), but with large scope variance — and Brewfather proves the commercial machinery is absent at one viable tier.

**Divergence:** vessels/tanks, yeast lineage, sales/CRM, compliance reporting, and team permissions appear in the commercial-tier products but not in the recipe-centric one — these are segment/tier structure, not definition.

## Canonical Model (C)

```text
Recipe (beer production definition: grain bill, hop schedule, yeast, process parameters, target stats)
  └── Batch (identified production run of a recipe at a scale and date)
        └── production lifecycle: brew day → fermentation/conditioning → packaging → completed
              └── process & measurement record (readings over time: gravity/temperature at minimum;
                  brewery-defined QA checks; events like transfers, additions)
        └── consumed ingredient lots (materials inventory drawn down by production)
        └── packaged output (finished beer: kegs/cases/cans — finished-goods inventory)
  └── Vessels (tanks/barrels the batches occupy — commercial tier)
  └── Commercial machinery (planning, sales, keg fleet, costing — varies by segment)
```

L0 (defining invariant — minimal):

1. **Recipe as the controlled definition of a beer** (ingredients + process + target parameters)
2. **Batch as the tracked instance of a recipe**, carried through a production lifecycle ending in packaged beer
3. **Process/measurement records attached to the batch over its lifecycle** (gravity/temperature readings as the canonical example — fermentation is time-extended and measurement-driven)
4. **Material inventory that production draws on and adds to** (ingredients in → packaged beer out, on the same books)

Rationale: remove the recipe/batch/process model → generic food manufacturing ERP or inventory software; remove inventory (production records only) → a brew log / brew-day tracker, not brewery management; remove the fermentation/time dimension → generic batch manufacturing. The union is what makes the Type.

L1 (common mature structure — present in most mature commercial products): vessel/tank registers with scheduling and day-state; transfer and dry-hop/addition events on batches; yeast handling (generations, pitch rate); QA/lab checkpoints; packaging runs into kegs/cases with batch coding; lot traceability (both directions); finished-goods and keg-fleet tracking; production planning (scheduling, MRP, reorder alerts); sales orders/deliveries to wholesale accounts; costing/COGS and accounting sync; task assignment with team notifications; dashboards/reports (yield, beer loss, tank utilization); device integrations (wireless hydrometers/controllers) and API.

L2 (variant/optional): regulatory compliance reporting (US TTB observed; region-dependent); CRM depth; multi-site operations; ERP-embedded vs standalone postures (Beer30+NetSuite; Orchestrated Beer as SAP-flavored ERP; Pelican's split MRP+Beer30); prosumer/hobbyist tier with community recipe library (Brewfather free tier); multi-beverage platform variants (BrewPlanner: winery/cidery/meadery/distillery; Beer30's kombucha sister product); AI assistants; barrel-aging programs; taproom-brewpub vs production+distribution emphasis.

L3 (vendor-specific, stays here): "Gold Standard" fermentation curves; Command Center; Pinty AI; Beer30 Lite; Bucha30; "300+ data points", "$100k saved", "12% yield", "3 clicks" mantra (marketing figures); BrewPlanner 500+ customers / 99% on-time / 30% waste-reduction claims; Brewfather AI credits, free-tier 25 recipes/25 batches limit, specific plan prices; BrewPlanner $49/$125 tier structure; specific device brand lists.

## Historical / Market-Sample Check (§24 applied)

- Older/regional: pre-cloud craft breweries ran on spreadsheets + paper batch cards + whiteboards (explicitly named as the enemy by all three products). The paper-era structure (recipe card, batch card, gravity log) maps 1:1 onto the canonical model — the software digitizes records that already existed. Older products fit.
- Segment-native: Brewfather (hobbyist origin, self-serve) fits the model without tanks, sales, permissions — confirming the commercial machinery is not definitional. 
- Platform-embedded: Orchestrated Beer (ERP-based) and Beer30+NetSuite show the same records inside an ERP shell; Pelican runs Beer30 beside an MRP/ERP — the canonical records survive either packaging.
- Extended-family check: the same structure is sold for wine/cider/mead/kombucha/distilling (BrewPlanner, Bucha30). The defining core (recipe → batch → time-extended fermentation measurement → materials) holds across fermented-beverage production; the *beer-specific* flavor is in the process vocabulary (mash/boil/hops/gravity) — this is the wine/brewery boundary seam, not a definitional difference.

## Vendor-specific Findings

- Beer30: Gold Standard curves; Command Center dashboards; diacetyl testing module built with a customer; WhatsApp support channel; Pinty AI; Bucha30 sister product; "never negative inventory" positioning against competitors.
- BrewPlanner: drag-drop scheduling board; vertical breadth (winery/distillery/cidery/meadery); "Ekos Alternative"/"Ollie Alternative" comparison pages; two-tier packaging (planning vs ERP).
- Brewfather: 20+ consumer device integrations; BeerXML/BeerJSON interchange; community recipe library; AI assistant grounded in user's own data; free-forever tier.
- Orchestrated Beer (positioning-level, from customers): ERP-anchored (SAP Business One lineage implied by customers' "ERP" language); finance-first; production staff did not self-serve.

## Boundary Findings

- **vs Food Manufacturing ERP**: a food ERP models generic batch manufacturing (BOM, work orders, lots) without the brewing process model. Brewery management centers on the recipe→batch→fermentation record with brewing-specific measurement semantics (gravity, attenuation, yeast) and vessel occupancy over weeks. Remove the brewing process model and measurement semantics → food ERP. The reverse also holds: Beer30's own large customer deliberately runs ERP for finance + Beer30 for process ("qualitative data… not really designed for in an ERP").
- **vs Winery Management (sibling leaf, unprocessed)**: same family — fermented-beverage production management. BrewPlanner sells both from one platform; the process chains diverge (crush/press/aging/blending vs mash/boil/ferment/conditioning) and so do the records (vintage/varietal/grape lots vs grain bills/hop schedules). Likely a sibling-split of one family rather than two wholly distinct Types — flagged for joint review when winery-management is processed.
- **vs Food Traceability Platform**: traceability is a capability here (lot in → batch → packaged out), not the center. A traceability platform centers on recall/exposure workflows; here the batch record is the center and traceability falls out of it.
- **vs Food Formulation Platform**: formulation platforms are R&D-centric (nutrition, specs, labeling). The recipe object here exists to be brewed, not to be filed for regulatory specification. Remove the batch lifecycle → formulation.
- **vs Production Planning / APS / MES**: planning is one machinery layer here. These tools schedule/capacity-plan generically; brewery management owns the batch record with its measurements. BrewPlanner deliberately brands its planning tier "brewery ERP" but its own feature list keeps batch history at the center.
- **vs CMMS / Equipment Administration**: vessels appear as production containers with contents/state, not maintenance objects.
- **vs Restaurant Management / Taproom POS**: the taproom sale is a different Type; brewery management reaches it only through sales-order/POS integration and depleting finished goods.
- **去掉什么就变成另一个 Type 判据**: remove recipe/batch/process semantics → food ERP or generic inventory; remove inventory/materials → brew log; remove fermentation/time dimension → generic batch manufacturing; remove beer-specific process vocabulary and you have the fermented-beverage family (winery/cidery), not a different logic.

## Uncertainties

- Ekos (the most-cited market leader) could not be fetched (transport errors ×2); Orchestrated Beer, Ollie, and Brew Ninja also unreachable. Their structures are asserted only at positioning level from other vendors' pages/testimonials. The final document makes no product-specific claims about them.
- All three observed products are craft-oriented (none of the very largest macro-scale brewery systems, e.g., SAP-based manufacturing suites, were sampled) — the model is calibrated to the craft/mid-market where the category lives.
- TTB compliance depth is evidenced by one product (Beer30) plus BrewPlanner's generic "for compliance" wording — kept qualified and region-labeled in the final document.
- Beer30's tank automation, BrewPlanner's scheduling internals, and Brewfather's inventory deduction mechanics are known from marketing copy/docs summaries, not hands-on operational docs; no precise defaults or limits are asserted.
- Whether vessel/tank machinery should sit at L1 (chosen) or L0 is a judgment call: Brewfather demonstrates a functioning brewery-management product without it, which supports L1.

## Final Synthesis

A Brewery Management application is the brewery's system of record for its beer production business. It holds beer recipes as controlled production definitions; turns recipes into tracked, numbered batches; carries each batch through a production lifecycle — brew day, fermentation and conditioning over days-to-weeks, packaging into kegs and cases — while attaching time-stamped process measurements (gravity, temperature, and brewery-defined quality checks) that make fermentation itself visible and comparable across batches; and keeps the material books on both sides of that lifecycle (ingredient lots consumed, packaged beer produced). Around this core, mature commercial products add vessel/tank scheduling, yeast management, planning (MRP/reorder), sales orders and keg-fleet tracking, costing/COGS with accounting sync, task/permission machinery, and region-dependent compliance reporting. Product philosophies differ (process-data-first vs planning-first vs recipe-first) and tiers differ (self-serve hobbyist-to-commercial through ERP-adjacent), but the recipe→batch→measurement→materials core is stable across all sampled products and survives packaging as standalone, suite module, or ERP companion.
