# Research Notes — Winery Management

## Research Goal

Understand "Winery Management" as an Application Type: what its managed object is (the wine production record), who runs it, how the crush-to-bottle cycle is organized in real products, where its boundaries sit against the already-processed neighbors (vineyard-management — upstream; brewery-management — fermented-beverage sibling; harvest-management — handoff) and unprocessed siblings (distillery-management), and — explicitly — whether the leaf is a genuine Type or a beverage-flavored variant of Brewery Management / Food Manufacturing ERP.

Two forward flags must be discharged in this pass:

- vineyard-management research (2026-09-10) §Boundary 2: "The seam is the crush pad. Vineyard Management's leg 3 ends at weighed fruit credited to blocks, with block identity flowing toward the winery; Winery Management begins at fruit intake/receiving and runs fermentation → production → storage → bottling → compliance… The winery pass should hold: vineyard module = Vineyard Management's structure; crush intake = the handoff object owned by the winery side."
- brewery-management research (2026-09-06) §Boundary: "same family — fermented-beverage production management. BrewPlanner sells both from one platform; the process chains diverge (crush/press/aging/blending vs mash/boil/ferment/conditioning) and so do the records (vintage/varietal/grape lots vs grain bills/hop schedules). Likely a sibling-split of one family rather than two wholly distinct Types — flagged for joint review when winery-management is processed."

## Initial Boundary

- Core use hypothesis: the winery's production business system of record — wine lots (batches) carrying varietal/vintage/origin identity, held in a vessel estate (tanks/barrels/bins), changed by recorded cellar operations (crush/press/ferment/rack/transfer/blend/addition/top/bottle), measured by lab analyses, costed per lot, closed into compliance reporting (US TTB 5120.17; regional excise equivalents) and traceability (lot → bottle; additive lot → wine).
- Users hypothesis: winemaker/assistant winemaker, cellar master and cellar hands, lab technician, production/operations manager, compliance officer, finance (cost accounting), owner/GM; custom-crush client winemakers at custom crush facilities.
- Neighbors: Vineyard Management (upstream, crush-pad seam), Brewery Management (fermented-beverage sibling), Distillery Management (unprocessed; DSP modules appear inside winery products), Food Manufacturing ERP (generic batch manufacturing), Food Traceability (capability vs center), Restaurant POS / tasting-room retail (downstream sale surface).
- Unknowns: is the compliance closure definitional or standard? Is the barrel estate definitional or common? How deep does the DTC/sales side reach into the Type? Does a distinct winery-specific product population exist vs multi-beverage platforms?

## Research Questions

1. What is the central production record — lot, batch, wine? What identity does it carry (varietal, vintage, vineyard/block, appellation)?
2. What is the vessel model — tanks, barrels, bins; capacity, contents, location, groups?
3. What operations exist and how are they recorded — crush/press, fermentation, rack, transfer, blend, addition, topping, filtration, bottling? What is conserved at each operation?
4. How does fruit enter — weigh tags, intake scheduling, grower deliveries, bulk wine intake?
5. How do lab analyses attach — Brix/pH/TA/SO2, fermentation curves, device integrations?
6. How does blending work — trial blends, composition computation, label-rule checking (varietal/AVA/vintage percentages)?
7. How does bottling close the loop — products/SKUs, case goods, composition and cost inheritance?
8. What compliance machinery exists — TTB 5120.17, excise, declarations, in-bond/taxpaid, formula wines, record auditability?
9. How does costing work — fruit/freight, operations, storage, overhead, COGS per lot/SKU?
10. What surrounds production — work orders, dry goods, purchasing, sales orders, allocations, custom-crush billing, vineyard module?
11. What interfaces — lot detail, vessel/tank views, work orders, lab entry, blending bench, compliance console, mobile at the tank?
12. What rules and states matter — quantity conservation, composition propagation, immutability, capacity limits, bonded/taxpaid state, lot-code mandates?

## Representative Products

| Product | Market position | Philosophy in sample | Evidence tier |
|---|---|---|---|
| vintrace | Global mid-market+ winery production software (AU origin; now Encompass "Vintrace Wine Cloud"); strong help center | Production-led standalone; deep winemaking + compliance + costing + custom-crush breadth | Tier 1: marketing site + full Zendesk help center (sections + articles fetched) |
| InnoVint | US mid-market winery suite (GROW/MAKE/SUPPLY/FINANCE) | Suite pole: production + vineyard + inventory + cost accounting + TTB compliance as pillars | Tier 1: root + Wine Production (MAKE) product page |
| Crush.wine | US small/mid wineries (500–50,000 cases) | Compute-from-operations pole: "record it once, at the tank"; quantity/composition/cost conserved; TTB computed from operations | Tier 1: root + full crush-to-cellar walkthrough |

Market anchors (not sampled first-hand): Ekos (multi-beverage business management; ekosgear.com and ekosapp.com both unreachable — 2 transport errors each), Orchestrated (ERP-grade winery suite; orchestrated.com unreachable — 2 transport errors), Vinsight (AU winery+vineyard; live domain now serves an unrelated agriculture product — see Sources).

## Sources

Fetched 2026-09-10 (all direct fetches unless noted):

- vintrace — winery production page: https://www.vintrace.com/wine-production-software
- vintrace — Help Center home: https://support.vintrace.com/hc/en-us
- vintrace — Web category (section list): https://support.vintrace.com/hc/en-us/categories/32300716099860-vintrace-Web
- vintrace — Winemaking section (article list): https://support.vintrace.com/hc/en-us/sections/32300810431892-Winemaking
- vintrace — Lot Tracking Traceability article: https://support.vintrace.com/hc/en-us/articles/32301358718356-Lot-Tracking-Traceability
- InnoVint — root: https://www.innovint.us/
- InnoVint — Wine Production (MAKE): https://www.innovint.us/product/wine-production/
- Crush.wine — root: https://crush.wine/
- Crush.wine — Crush to Cellar walkthrough: https://crush.wine/crush-to-cellar
- Cross-pass: research/vineyard-management.md (2026-09-10) — vintrace+eVineyard seam statements, Vinsight winery side (search-index capture), Wine Business Monthly 2006/2011 vineyard-software reviews (historical anchors)
- Cross-pass: research/brewery-management.md (2026-09-06) — fermented-beverage family structure and seam statement

Source-access limitations:

- Ekos: both domains transport-errored twice — abandoned per network rule; no structural claims made; held as market anchor only.
- Orchestrated: transport-errored twice — abandoned; market anchor only (ERP-grade pole inferred from market position, not verified).
- Vinsight: https://vinsight.co/ now serves "Bountiful" (agricultural yield forecasting) — the winery product observed by the vineyard pass via search index is no longer verifiable live; its winery-side observations are used only as cross-pass corroboration, not as primary evidence.
- No pricing, plan-tier, or numeric-capacity claims are made for any product beyond what fetched pages state.

## Product A — vintrace

### Key observations (evidence layer A unless noted)

- Positioning (marketing page): "Cloud-based solutions that help winemakers track and manage their operations from grape to bottle"; product nav: Winery Management, Vineyard Management, vintrace Mobile, wineadds Calculator. Production stages named on the page: track & manage dry goods (stock levels, low-stock alerts, tracked against lots, food-safety standards); bottling logistics (bottling, storage, wholesale orders, purchases, delivery); locate stock (multiple warehouses, stock counts); smart work processes ("create and allocate work orders and keep track of additions, contents of the tank, barrel usage and analysis. Plan and schedule your fruit intake and crush pad operations"); direct purchasing & sales (purchase orders to suppliers, sales orders and invoices to clients); intelligent reporting ("manage your compliance requirements, understand your profit and losses").
- Integrations named: lab analyzers (Thermo, ChemWell, FOSS, BioSystems, ETS Laboratories, Anton Paar), accounting (QuickBooks, Xero), tank control (TankNet), barrel analysis (BarrelWise), vineyard management (eVineyard, AgCode, GrapeWeb), eCommerce (Lightspeed), vinCreative, GrapeLink, vinwizard.
- Help-center section map (the object model, operational grade):
  - **Barrel Management** (17 articles): barrel groups (breaking a barrel out of a group, changing group details, combining barrels/groups), changing barrel locations, deactivating barrels, customizing the Vessels page → barrels are individually identified vessels, groupable, locatable.
  - **Bottling and Inventory** (28 articles): adjusting stock levels, bottled wine and dry goods details, bottling by bulk dispatch, breaking a case into bottles, configuring defaults on stock items → bottling converts bulk wine into stocked finished goods; cases can be broken into bottles; dry goods are stocked items.
  - **Compliance** (16 articles): "Using the Scalehouse for Commodity Intakes and Dispatches", "Declaring Wine" (Wine Declaration Console; by Alcohol Analysis; by Product Treatment; from the Product Page) → intake/dispatch at a scalehouse; wine declarations as a compliance act with multiple declaration bases.
  - **Costing** (16 articles): fruit and freight cost importer; adding costs for wine/juice received in bulk; adding costs to operations; storage costs for wines in vessel; allocating overhead to bulk wine and finished goods; bottling and dry-goods costing → cost attaches at intake, per operation, per storage period, and overhead allocates to bulk and finished goods.
  - **Custom Crush Billing** (11 articles): ad hoc billing charges; work vs client billing report; billing clients for inventory work; billing for tank and barrel storage, hire, and hosting; charging clients for winery work; installments → the custom-crush business model (making wine for clients) is a first-class module: work is attributed to clients and billed.
  - **Distilled Spirits Plant** (17 articles): moving distilling material from a bonded winery to a DSP bond; dealcoholization (removing aromas; producing spirits and low-alcohol wine; moving wine between bonded winery and DSP bonds) → US bonded-premises semantics extend beyond wine.
  - **Finished Goods Allocations** (14 articles): product demand, fulfilling allocations, tracking allocations on transfers → scarce finished goods allocated against demand.
  - **Lab work** (24 articles): dynamic MSO2 calculation; lab requests with adjustable analysis dates; transferring data from an Anton Paar DMA 35; backdating analysis and live metrics; cap management → analyses attach to vessels/lots; devices feed readings; fermentation support (cap management).
  - **Purchases / Sales**: purchase orders and purchase types; receiving barrels from a purchase order; sales price lists; excise tax handling (New Zealand); Wine Equalisation Tax (Australia); importing sales orders; stock commitments → regional alcohol-tax machinery on the sales side.
  - **Sparkling Wine** (14 articles): tirage bin fill times; tirage groups; bins; gyro cages; gyro cycles → sparkling-specific vessel/program machinery.
  - **Winemaking** (39 articles): prevent overfilling vessels; notes/attachments to wine; transferring wine between wineries; equipment treatments; bulk dispatch (inter-winery); adding/removing staves; adding concentrate and spirits to wine; **blending in bond and taxpaid wines**; tank yield; measuring a vessel; transferring a trial blend to multiple tanks; evaporating juice into concentrate and reconstituting; **flagging a wine as a formula wine**; bulk wine intake; bulk wine search; changing a batch code during transfer; changing a wine batch's properties; correcting received fruit after it's processed; managing trial blends; fixing a wine's composition; **generating a wine's history**; **lot tracking traceability**; printing QR codes for vessels; scanning vessels; product treatments; sustainability flag; tagging wines; the product page.
  - **Work orders** (16 articles): creating manually; rollback and replay; equipment treatment jobs; sanitizing tanks; vessel forecasting → work orders drive cellar work; vessel capacity forecast exists.
- Lot Tracking Traceability article (full read): additives can be set up with batch tracking; receiving stock REQUIRES a lot code for tracked additives; lot codes route to storage areas; expiring-lot dashlets; when performing an addition the operator selects the specific lot used; the Product page's Adds tab summarizes "By Additive and Lot"; the **Wine Addition Impact Report** shows which wines (current, dispatched bulk, packaged) used a given additive lot, with add date, rate, add total, add batch, add vessel; packaging work orders carry the lot code → two-directional traceability: additive lot → wines → packaged goods, and wine batch → additives used.
- Roles and Permissions article exists (linked) → role model present.
- Cross-pass corroboration (vineyard pass, layer A there): vintrace+eVineyard acquisition framing — "one unified system where vineyard and winery teams work in sync — from tracking fruit development in the field to optimizing fermentation in the cellar"; "full traceability from vineyard block to final bottle"; "Track costs per vineyard block".

## Product B — InnoVint

### Key observations (evidence layer A)

- Positioning: "Your Winery Operating System… InnoVint helps wineries of all sizes grow, make, and sell wine"; pillars GROW (Vineyard Tracking), MAKE (Wine Production), SUPPLY (Inventory and Order Management), FINANCE (Cost Accounting), plus TTB Compliance, Intelligent Winery Workflows, Lab & Analyses Management, 3D Tank Maps, InnoApp mobile.
- MAKE (Wine Production page): "Manage all of your wine production – from grape to bottle – in one centralized location."
  - Cellar activity & workflows: "Flexible work orders to run your cellar operations online or printed"; "Assign work to individuals or teams by program or client, with complete traceability back to the grape sources"; work "from anywhere, regardless of cell service or wifi access, with InnoApp" (offline mobile).
  - Compliance: "Automatically generate a fully-auditable TTB 5120.17 report"; state-specific reporting; "full FDA traceability"; "Catch and correct issues before they lead to audits."
  - Lot & vessel tracking: "Know the precise location and contents – whether they are barrels, tanks, bins, or kegs – with InnoVint's comprehensive lot and vessel tracking"; interactive 3D tank maps for real-time tank contents.
  - Labs & analyses: "easily capture and analyze lab results"; "easily monitor fermentations, plan pumpovers and write your harvest work orders all in one place"; integrations with ETS Laboratories, TankNet, VinWizard, Anton Paar, FOSS, Barrelwise, myEnologist, CloudSpec, Lodi Wine Laboratories, Wine Lab.
  - Dry goods: "Manage all dry goods, additive, and packaging supplies"; "Stay FDA Compliant"; "full traceability of ingredients per lot"; "accurately carry dry good costs to the lot as they are consumed."
- Root page role framing: Winemaking ("Schedule and knock out work… Catch any 'oops' scenarios before you add or blend… Manage winery work from anywhere, even offline"); Finance ("Easy, precise COGS reporting… Cost allocations across inventory… profitability & margin transparency by SKU"); Vineyard (block activities, grape contracts, yield estimations, maturity data); Operations ("Document your SOPs for every workflow… real-time inventory… quality control"); Compliance ("Automate TTB 5120.17 (old 702) report generation… Track ingredients and allergens… Full audit trail of all historic and current winery activity… Instant access to archived lot and vessel histories"); Sales + Marketing ("Instant access to historical wine data like composition, barrel types, pH, TA… create up-to-date Tech Sheets").
- SUPPLY: "Track physical inventory; Manage product allocations; Record inventory depletions."
- FINANCE: "Assign costs to the wine as supplies are used; Real-time visibility into costs by lot, broken down by cost category; Report on profitability per SKU."
- Commerce integration: Commerce7 (DTC) in the partner wall.

## Product C — Crush.wine

### Key observations (evidence layer A)

- Positioning: "Cellar software for small and mid-size wineries that follows your wine from crush to cellar. Every rack, transfer, and blend recorded at the tank. Composition, costing, and TTB reports automated. Built for wineries producing 500–50,000 cases who've outgrown spreadsheets." Tagline: "Record it once, at the tank."
- Four pillars: Vineyards & Harvest (GPS block mapping, AVA resolution, ripeness tracking, "bring fruit in on the weigh tag that starts each lot's history"); Cellar ("Record racks, transfers, blends, and additions at the tank. Quantity, composition, and cost are computed from each operation, never typed twice"); Lab ("SO2, pH, TA, Brix — entered once and shown on the tank or block they belong to"); Back Office ("TTB 5120.17 (the old Form 702) computed from the season's operations. Every line drills back to the transfer or weigh tag behind it; a snapshot freezes the filing").
- Crush-to-cellar walkthrough (the lot lifecycle, step by step):
  1. Veraison to pick decision — block mapped once with GPS fence; all overlapping AVAs resolved; Brix/pH/TA samples tied to block vintage; "that block's varietal, vintage, and appellation set are already on file before a single grape moves."
  2. The weigh tag — "fruit becomes a lot": "It captures the tonnage, the block it came from, and the vintage, and it inherits that block's AVA set automatically. This is the origin of the lot's composition: a real, measured quantity of fruit carrying its varietal, vintage, and appellation. Everything downstream is computed from here — nothing about the wine's identity is typed in twice."
  3. Crush, ferment, press — "Each move is recorded as an operation, and each operation conserves quantity: what leaves one vessel, minus measured loss, is exactly what arrives in the next. The wine left in the press pan or the hose isn't quietly dropped — it's booked as loss, with its real cost following the volume out."
  4. Racking, topping, additions — "logged on a phone, right at the tank… the lab's chemistry for that vessel sits on the same page… The moment an operation commits, the vessel's current contents and composition update." (Topping replaces "the angels' share".)
  5. Blending — "the new wine's composition isn't an estimate — it's the exact, quantity-weighted consequence of the two inputs. Varietal percentages, vintage percentages, AVA percentages, and cost all combine automatically. That is what makes a label claim defensible: when you say 'Napa Valley' you can show the wine clears the 85% AVA rule, and 'Cabernet Sauvignon' the 75% varietal rule, straight from the operations you recorded." Trial blends testable before commit (wine label checker runs "the same 27 CFR Part 4 rules").
  6. Bottling — "the finished product inherits the full composition and cost history of everything that flowed into it. The case count, the blend percentages, and the per-bottle cost all trace back through the season to that first weigh tag… you bottle knowing the label clears."
  7. Back office — "Because every operation left an immutable snapshot, your TTB 5120.17 report… is computed from the season's actual work — grape receipts, transfers, losses, taxable removals — not reconstructed from whiteboards. Every line item drills back to the operation behind it, and a snapshot freezes the filed numbers for good." Excise: Form 5000.24 with small-producer credit.
- Stated invariants: "Quantity is conserved" (tracked to four decimal places of a gallon — product-specific precision, held here); "Composition follows the wine" (varietal, vintage, AVA, and cost move proportionally on every transfer and blend; "real cost follows volume even into loss"); "History is immutable" ("Every committed operation writes a permanent snapshot. You can see exactly what any vessel held at any point in the season").
- Free tools: TTB excise calculator (Form 5000.24), wine label checker (75% varietal / 85% AVA), US AVA map; guides to TTB Form 5120.17 and harvest yield math (tons to gallons).

## Cross-pass Evidence

From the vineyard-management pass (2026-09-10), the winery-integrated pole observed from the vineyard side:

- **vintrace + eVineyard** (A there): "one unified system where vineyard and winery teams work in sync — from tracking fruit development in the field to optimizing fermentation in the cellar"; "full traceability from vineyard block to final bottle"; "Track costs per vineyard block."
- **Vinsight** (search-index capture there; live domain now unrelated): "In the Winery — Maturity data on vineyards and blocks; Varieties and clone information; Fruit and bulk wine/juice received into the winery…"
- **InnoVint** (A there): "From the moment the buds break in the vineyard to the departure of your finished product from your winery, we're there with you to track every activity from start to finish"; grape contracts and farming costs "critical to measure, capture and report on for raw goods costing"; harvest planning "scheduling incoming fruit to forecast expected tonnage to receive per day."
- **Historical anchors (WBM 2006 / Wines & Vines 2011 reviews)**: eSkye — "Weigh tags in field may be tracked all the way through winery to shipping of product… Tying wine attributes back to vineyard" (reviewer: "clearly winery-focused"); Wine Management Systems — "history of each vineyard block included in a particular blend as well as a display of which tanks contain grapes from particular blocks"; 2011 buyer criteria — "Does the application facilitate tracking of harvested fruit from vineyard to winery (and traceability back to the vineyard)?" → the winery-side structure (weigh tag → tanks → blend → shipping; block-in-wine traceability) is two decades old in this market.

From the brewery-management pass (2026-09-06), the family structure: recipe as controlled production definition + batch as tracked instance with a production lifecycle + time-stamped process measurements + material inventory on both sides (ingredients in, packaged product out); vessels/tanks with scheduling; QA checkpoints; lot traceability both directions; production planning; sales orders; costing/COGS; compliance reporting (US TTB). The pass's own seam note: "remove beer-specific process vocabulary and you have the fermented-beverage family (winery/cidery), not a different logic."

## Cross-product Comparison

| Dimension | vintrace | InnoVint | Crush.wine |
|---|---|---|---|
| Central record | Wine batch (batch codes; properties; history generation; notes/attachments) | Lot (fruit, juice, and wine lots) with vessel binding | Lot ("one lot, start to finish"; origin = weigh tag) |
| Vessel estate | Tanks, barrels (individual + groups), bins; capacity (overfill prevention); locations; QR codes; measuring; vessel forecasting | Barrels, tanks, bins, kegs; location + contents; 3D tank maps | Tanks/barrel lots; contents update on operation commit |
| Operations | Transfers (incl. inter-winery, in-bond/taxpaid), additions (concentrate, spirits, staves), racking, blending (trial + committed), bottling/packaging, bulk intake/dispatch, equipment treatments | Work orders (online or printed; assigned by program or client); activity tracking for fruit/juice/wine lots; additions; blends with "oops" warnings | Racks, transfers, blends, additions recorded at the tank; crush/press; topping; bottling |
| Conservation semantics | Overfill prevention; tank yield; correcting received fruit; fixing composition | Compliance warnings "before you add or blend"; audit trail | Quantity conserved (loss booked with cost); composition computed proportionally; immutable snapshots |
| Lab | Lab requests, MSO2, device transfers (Anton Paar DMA 35), cap management, backdating | Lab & analyses management; fermentation monitoring; pumpover planning; device integrations | SO2/pH/TA/Brix on the tank or block page |
| Fruit intake | Scalehouse for commodity intakes/dispatches; correcting received fruit; fruit & freight cost importer | Harvest work orders; grape contracts (GROW) | Weigh tag = grape reception record starting the lot's history |
| Blending & label | Trial blends; blending in bond and taxpaid; formula wine flag; fixing composition | "Catch oops before you add or blend"; historical composition for tech sheets | Quantity-weighted composition; 75% varietal / 85% AVA label checks; trial blends |
| Bottling & finished goods | Bottling & inventory (28 articles); breaking cases into bottles; products with demand/allocations | SUPPLY: case goods inventory, allocations, depletions | Product inherits composition + cost; case count |
| Costing | Fruit/freight, per-operation costs, storage costs, overhead allocation, bottling & dry-goods costing | Costs by lot by category; COGS; profitability per SKU; accounting reconciliation | Cost computed from operations; per-bottle cost traces to weigh tag |
| Compliance | Compliance section (declarations by alcohol analysis/treatment; scalehouse intakes/dispatches; DSP; NZ excise; AU WET) | TTB 5120.17 automated; state reporting; FDA traceability; audit trail | TTB 5120.17 computed from operations with drill-back; snapshot freezes filing; Form 5000.24 excise |
| Work management | Work orders (16 articles; rollback/replay; sanitizing; vessel forecasting) | Intelligent winery workflows; SOPs; scheduling | Operations recorded at the tank on a phone |
| Custom crush | Custom Crush Billing section (client billing for work/storage/hire) | Work assigned "by program or client" | (not visible) |
| Vineyard module | Vineyard Management product (eVineyard) + integrations | GROW pillar | Vineyards & Harvest pillar |
| Sales side | Sales orders, price lists, stock commitments, excise/WET handling | Depletions; Commerce7 integration; margins by SKU | (not visible) |
| Pole | Production-led standalone, broad module breadth | Suite (grow→make→supply→finance) | Compute-from-operations cellar focus, small-winery tier |

Convergent across all three (layer B): wine lot/batch as central record; vessel estate (tanks/barrels/bins); recorded operations (transfer/rack/blend/addition/bottling); lab analyses attached to vessels/lots; fruit intake as the lot's origin; dry goods/additives inventory with lot traceability; bottling into finished goods; cost attached to the lot; compliance reporting computed from the operation record; mobile/at-tank capture; work orders; vineyard integration or module.

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures over one subject binding (the winery's own wine production business):

1. **The wine lot as the persistent production record of identity.** An identified quantity of wine (from fruit intake through must/juice/wine to bulk dispatch or bottle) carrying its composition identity — variety/varietal, vintage, and origin (vineyard/block source, appellation where the regime has one) — and accumulating its production history. Remove → anonymous liquid inventory or a tank-level gauge list; the "wine" the system manages stops existing as a managed identity.

2. **The vessel estate as the physical container population.** Tanks, barrels, and bins held as identified containers with capacity, location, and current contents; lots live IN vessels; the system maintains what is in which vessel, how full, and where. Remove → a batch list with no physical placement; cellar work (racking, topping, sampling) has no object to work on.

3. **The recorded cellar operation as the unit of change.** Crush/press, rack, transfer, blend, addition, topping, and bottling recorded as events that move or transform wine between vessels — conserving quantity (losses booked, not dropped) and carrying composition and cost proportionally — accumulating into the lot's history as the authoritative record. Remove → a static inventory snapshot with no production loop; the season's work leaves no record.

Jointly-held load-bearing tests:

- 1 alone = a wine registry / liquid-inventory list
- 2 alone = a tank & barrel chart
- 3 without 1+2 = operations over anonymous volumes (a work log)
- 1+2 without 3 = a static cellar map that goes stale
- 1+3 without 2 = batches with no physical placement
- 2+3 without 1 = vessel movements with no wine identity

Subject binding: the winery's own wine production. Remove the binding → generic batch manufacturing / food ERP territory. The binding shows up concretely: the lot's identity is wine-label identity (varietal/vintage/appellation), the vessel estate is barrel-heavy with aging semantics, the calendar is organized around the crush season, and the record-keeping standard is the alcohol regime's.

### L1 — Common Mature Structure

- **Lab & analyses** — Brix/pH/TA/SO2-class measurements attached to vessels/lots; fermentation monitoring (cap management, pumpover planning); lab-device integrations.
- **Work orders** — planned/scheduled cellar work, assigned to people/teams/clients, executed (often mobile, sometimes offline) and completed back into the record.
- **Fruit intake & crush scheduling** — weigh tags / grape reception records as the lot's origin; intake scheduling against crush-pad capacity; corrections after processing.
- **Dry goods & additives inventory** — stocked supplies with lot codes and expiry where tracked; consumption carried to the lot as cost; ingredient traceability per lot.
- **Bottling/packaging → finished goods** — packaging operations convert bulk wine into products/SKUs and case-goods inventory; composition and cost inherit from the lots.
- **Cost tracking to the lot** — fruit/freight, per-operation costs, storage costs, overhead allocation; COGS per lot and per SKU.
- **Compliance & traceability closure** — the operation record rolls up into the alcohol regime's production/excise reporting (US TTB 5120.17 the most-documented instance; AU WET and NZ excise on the sales side; declarations; in-bond/taxpaid semantics) and two-directional lot traceability (additive lot → wines → packaged goods; wine → blocks/sources).
- **Blending machinery** — trial blends (what-if before commit), composition computation, label-rule checking where the regime defines one (US 75% varietal / 85% AVA).
- **Barrel programs** — barrels as individually identified vessels, groupable, locatable, with topping and staves; barrel-analysis integrations.
- **Bulk wine intake/dispatch** — wine received and shipped in bulk between wineries, with cost and compliance handling.
- **Purchasing & sales orders** — purchase orders (supplies, barrels, grapes), sales orders and price lists for bulk and finished goods.
- **Mobile/at-tank capture** — phone-based operation recording at the vessel; QR/barcode vessel identification; offline capability.
- **Roles & permissions** — role-gated operations and visibility.
- **Reporting** — production, inventory, bottling, cost, and compliance reports; wine-history generation.

### L2 — Variant / Optional Structure

- **Vineyard module** — the winery-integrated pole packages Vineyard Management (block assets, ripening, contracts) as a module; the module is that Type's structure at module grain, not part of this Type's core.
- **Custom crush billing** — client attribution and billing for winery work, storage, and hire (custom crush facilities).
- **Finished-goods allocations & DTC adjacency** — allocation management against demand; depletions; DTC commerce integrations.
- **Multi-beverage platform** — one platform selling winery+brewery+cidery+meadery+distillery (BrewPlanner pattern from the brewery pass); hard-seltzer and DSP/dealcoholization modules inside winery products.
- **Sparkling-wine machinery** — tirage, gyros, riddling cycles.
- **Regional regime variants** — US TTB/bonded semantics vs AU WET vs NZ excise vs EU regimes; label-rule machinery differs by regime.
- **ERP-embedded vs standalone posture** — ERP-grade suites (Orchestrated, market anchor) vs production-led standalone products.
- **Accounting integration** — QuickBooks/Xero/NetSuite reconciliation.

### L3 — Vendor-specific (research notes only)

- Crush.wine's "four decimal places of a gallon" precision claim; "record it once, at the tank" tagline; free AVA map/label checker/excise calculator; 500–50,000 cases positioning.
- InnoVint's GROW/MAKE/SUPPLY/FINANCE pillar naming; 3D tank maps; InnoApp; "saving 15-30 hours per week" and Chandon $75K case-study claims; State of Winery Health Report.
- vintrace's dashlets, wineadds calculator, EncompassIQ/AI framing, "8.5M tons of grapes crushed" and "7.6K winemaking team members across 19 countries" marketing stats, SOC 1/2 badges, plan structure.
- All pricing/plan-tier details.

## Vendor-specific Findings

- **Custom crush billing as a first-class module** — directly observed only in vintrace (11-article section); InnoVint shows client attribution ("by program or client") without visible billing machinery. Held L2, single-product depth.
- **DSP/dealcoholization** — vintrace only. Held L2.
- **Sparkling machinery (tirage/gyro)** — vintrace only. Held L2.
- **3D tank maps** — InnoVint only. Held L3.
- **In-bond/taxpaid blending, formula-wine flag** — vintrace explicit (US bonded semantics); Crush implies the same regime via TTB drill-back but does not name the states. US-regime flavor; held L2.
- **Scalehouse** — vintrace names the scalehouse as the intake/dispatch instrument; Crush's weigh tag is the same instrument named differently. Convergent concept, different vocabulary.

## Boundary Findings

1. **vs Vineyard Management — the crush-pad seam, DISCHARGED from this side: keep-both RATIFIED.** The vineyard pass's expectation is confirmed with first-hand winery-side evidence: the winery Type begins at fruit intake, and the intake record (Crush's weigh tag — "the grape reception record… the origin of the lot's composition"; vintrace's scalehouse commodity intakes; InnoVint's harvest work orders) is owned by the winery side. Downstream of the weigh tag the object is the wine lot, not the planting asset: the winery Type's center is the production record (lots/vessels/operations), the vineyard Type's center is the planting asset (blocks/vines/vintages). The winery-integrated pole packages the vineyard side as a module (InnoVint GROW, vintrace Vineyard Management, Crush Vineyards & Harvest) — that module is Vineyard Management's structure at module grain, exactly as the vineyard pass predicted. Removal tests hold both directions: strip the lot/vessel/operation machinery and keep blocks → vineyard-shaped; strip the block asset and keep lots → winery-shaped. The handoff is the weigh tag: fruit credited to blocks on one side, a lot's history begun on the other.

2. **vs Brewery Management — the fermented-beverage family seam, JOINT REVIEW DISCHARGED from this side: keep-both RATIFIED (sibling Types, one family).** The brewery pass's structure (recipe→batch→time-extended fermentation→materials in/packaged out; vessels; QA; traceability; costing; TTB compliance) is the family shape, and this pass confirms the same shape from the wine side (lot→vessels→operations→bottling; costing; TTB). The ratified seam is the record flavor, three strands: (a) **identity basis** — the wine lot's identity is blend-computed label composition (varietal %, vintage %, appellation % computed from operations and checked against label law; "nothing about the wine's identity is typed in twice") vs the beer batch's identity as recipe-executed (grain bill/hop schedule/gravity targets); (b) **process chain** — crush/press/ferment/press-off/rack/age(months-to-years)/blend/bottle with topping-and-loss accounting over a barrel-heavy estate vs brew day/mash/boil/ferment(days-to-weeks)/condition/package; (c) **calendar** — the crush season as the annual structural peak vs brew-day cadence. Multi-beverage platforms (BrewPlanner selling both; vintrace's hard-seltzer/DSP modules) are platform variants, not Type boundaries — the same lot/vessel/operation logic re-instantiated per beverage. Neither Type collapses into the other; both stand beside Food Manufacturing ERP.

3. **vs Food Manufacturing ERP.** Generic batch manufacturing has batches, materials, and production orders but not the wine lot's composition-identity semantics (label-law-computable varietal/vintage/appellation percentages), the barrel-heavy aging estate with topping/loss accounting, or the alcohol regime's bonded-premises record. A winery can run on a food ERP; the winery Type exists where the lot's identity and the cellar's operation ledger are the center.

4. **vs Food Traceability Platform.** Two-directional lot traceability is a capability here (vintrace's Wine Addition Impact Report; Crush's drill-back), built on the operation ledger — but the center is production management, not traceability as a program.

5. **vs Distillery Management (unprocessed sibling).** DSP/dealcoholization appears as a module inside a winery product (vintrace, 17 articles, bonded-premises semantics). The distillery Type's center (spirits production: distillation runs, spirits runs, proof) is different machinery. Forward flag for that pass: the DSP module inside winery/brewery products is the seam; expect the same module-grain pattern as the vineyard seam.

6. **vs Restaurant POS / tasting-room retail.** The sale surface (tasting room, wine club, DTC) is downstream; winery products integrate with commerce (Commerce7, Lightspeed) but the production record is the center. Allocations/depletions sit at the seam.

7. **vs Inventory Management System.** Generic inventory tracks stock levels; the winery system's stock is composition-carrying (what leaves one vessel arrives in the next with its varietal/vintage/AVA percentages and cost) — inventory without composition propagation is not this Type.

## Uncertainties

- **Compliance closure: L0 or L1?** Held as L1 (standard capability) because a cellar-ops-only system remains recognizably a winery management application, and the compliance machinery is regime-shaped (US TTB vs AU/NZ excise) rather than universal in form. But all three sampled products ship it as a headline, the historical winery always kept the legal record, and the operation ledger's audit-grade immutability exists substantially to serve it. If a future pass finds a market pole with no compliance machinery at all, this call should be revisited.
- **DTC/sales depth.** Allocations and depletions observed in two products; full DTC/club machinery lives in adjacent products (Commerce7, WineDirect-class). The sales side is held L1/L2; the boundary with DTC commerce platforms was not researched in this pass.
- **Ekos / Orchestrated poles unverified.** The business-management-led pole (Ekos) and ERP-grade pole (Orchestrated) are market anchors only — both domains unreachable. The L0's independence from the suite-vs-standalone axis is inferred from the three sampled products spanning standalone/suite/compute poles, not from those two.
- **Vinsight's current status.** Live domain now serves an unrelated product; the vineyard pass's search-index capture is the surviving evidence. Used only as corroboration.
- **Non-US regimes.** AU/NZ evidence is thin (vintrace WET/excise articles; Vinsight cross-pass). EU regimes not directly observed; compliance leg worded regime-neutrally.
- **Bulk-wine market depth.** Bulk intake/dispatch observed in vintrace (intake, search, dispatch, inter-winery transfer) and implied by Crush's taxable removals; market depth (bulk-wine brokerage adjacency) not researched.

## Final Synthesis

Winery Management is the winery's wine-production system of record. Its defining core is three jointly-held structures: the wine lot as the persistent production record of identity (an identified quantity of wine carrying varietal, vintage, and origin from fruit intake to bottle, accumulating its history); the vessel estate as the identified container population (tanks, barrels, bins with capacity, location, and current contents, the lots living in them); and the recorded cellar operation as the unit of change (crush/press, rack, transfer, blend, addition, topping, bottling recorded as events that conserve quantity — losses booked, not dropped — and carry composition and cost proportionally into an authoritative, audit-grade history). Around this core, mature products add lab analyses on vessels and lots, work orders with mobile at-tank execution, fruit intake and crush scheduling on weigh tags, dry-goods inventory with lot-coded traceability, bottling into finished goods with composition and cost inheritance, cost tracking to the lot (COGS per lot/SKU), the alcohol regime's compliance closure (TTB 5120.17-class reports computed from operations, declarations, excise), blending machinery with trial blends and label-rule checks, barrel programs, bulk intake/dispatch, purchasing and sales orders, roles, and reporting. The Type spans poles — production-led standalone, full business suite, compute-from-operations small-winery, ERP-grade — sharing one core; the pole is a variant axis, not a Type boundary. Both flagged seams are resolved: the crush pad separates this Type from Vineyard Management (the weigh tag starts the lot's history on the winery side; the vineyard module inside a winery suite is that Type at module grain), and the record flavor (blend-computed label identity, barrel-heavy aging, crush-season calendar) separates it from Brewery Management within the shared fermented-beverage family shape. The historical check passes: the paper-era winery — cellar book of tank and lot records, weigh tags at the scale, blend ledgers, Form 702 filings — satisfies all three legs, and the 2006-era products already show the same structure (weigh tags tracked through the winery to shipping, tanks displaying which block's grapes they contain).
