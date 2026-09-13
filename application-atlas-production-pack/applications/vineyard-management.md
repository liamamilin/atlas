# Vineyard Management

## Overview

A **Vineyard Management** application is the vineyard operation's system of record, organized around the vineyard planting — the long-lived block of winegrapes — as a persistent production asset. It holds the planting's identity, records the perennial cycle of viticultural care and protection work against it, and credits each vintage's fruit outcome back to it as an accumulating performance history — with the block's identity flowing with the fruit toward the winery where the system reaches that far.

The defining core is small:

```text
Vineyard planting (persistent asset)
└── block hierarchy with planting identity
    (variety; clone and rootstock where kept; commonly area,
     planting year, row spacing/trellis, appellation where the regime has one)
    └── perennial-cycle viticultural work recorded against the asset
        (pruning, canopy management, trellis/repair, crop reduction,
         spray, irrigation, nutrition; phenology block by block)
    └── the vintage's fruit outcome credited to the asset
        (maturity sampling and crop estimation → weighed harvest per block
         → block × vintage performance history → identity toward the winery)
```

Everything else commonly associated with modern vineyard software — GPS block mapping, spray-path recording, sensors and weather data, AVA lookups, labour-contractor payroll, weigh-tag flows into the cellar — is widespread in current products but is not what makes the product a vineyard management system. A paper block register with spray diaries, pruning tallies, maturity notebooks, and per-block yield books satisfies the same core.

When the center of gravity shifts to the season-scoped crop cycle, the product is Crop Management; when it shifts to the tree-fruit planting and its packhouse continuation, it is Orchard Management; when it shifts to fermentation and the wine production record, it is Winery Management; when it shifts to the harvest operation itself, it is Harvest Management.

## Users & Context

The primary user is the **vineyard manager or viticulturist** — the person accountable for what happens in the vineyards each day: which crews are working which blocks, whether pruning or canopy work is progressing, how the blocks are ripening, and what each block and variety is costing and yielding. The **grower or wine company** is the principal and data owner, watching quality, yield, and production cost across the estate. **Crew leaders and supervisors** capture work in the field. **Winery teams** are the downstream counterpart at estate operations — they consume ripening data, plan crush capacity, and receive the fruit whose identity began in the vineyard. A distinctive user in this Type is the **vineyard labour contractor**: a business that supplies crews to growers for pruning and harvest, using the system to record attendance and piece work, pay its workers, and invoice its clients.

The work environment is winegrape production — variety, clone, and rootstock chosen years in advance; the vine's structure (trunk, cordons, trellis, canopy) built and maintained over decades; and each vintage's quality determined by season-long decisions (how hard to prune, when to shoot-thin, when to pick). Work is seasonal and crew-heavy: winter pruning, spring canopy management and protection, summer irrigation and crop reduction, and an intense harvest in which ripening blocks are picked in a short window and delivered as weighed fruit to the crush pad. Much of the hand work is paid by piece rate — per vine or row pruned, per ton or bin picked — which makes row-level crediting a structural need.

## Core Model

### The Defining Core

**The vineyard planting as the persistent production asset.** The system's anchor is an identified planting — typically a vineyard or estate subdivided into **blocks**, each carrying its planting identity: the **variety**, with **clone and rootstock** where kept, commonly the area, planting year, row spacing or row configuration, and trellis; and, where the regime has one, the **appellation or region** the block sits in. Blocks commonly subdivide into **rows**, and, where viticulture is managed at that depth, into **individual vines**. This hierarchy is not a map layer: it is the persistent asset that outlives every vintage — the "crop" and the "land" at once. Work, observations, and outcomes all attach to it.

**Perennial-cycle viticultural work recorded against the asset.** The vineyard's year is a repeating cycle of care and protection — pruning, canopy management (shoot thinning, leaf pulling, hedging and tucking class work), trellis and vine repair, crop reduction (thinning or dropping fruit), spraying, irrigating, feeding — and the system records this work as dated, attributed, location-bound entries attached to the block or row. The vine's **phenology** is recorded block by block through the season — budbreak, flowering, fruit set, veraison — commonly against the modified E-L growth-stage scale, giving each block a dated developmental history that is compared vintage over vintage.

**The vintage's fruit outcome credited to the asset.** Through ripening, the system tracks each block's progress: **maturity sampling** (commonly sugar, acidity, and pH measures) and **crop estimation** (bunch and cluster counts, cluster and berry weights → progressive yield estimates, expected versus actual tons). At harvest, what each block produces is recorded as it comes in — loads, bins, or tons, commonly as weighed deliveries where the fruit moves to a crush pad — and credited to the block and variety. These outcomes accumulate into the asset's vintage-over-vintage performance history: yield, quality, and cost per block and variety, which is the record the next cycle's decisions are made from. Where the system reaches toward the winery, the block's identity — variety, vintage, appellation — travels with the fruit, so the wine can be traced back to the blocks that made it.

The three structures are jointly load-bearing. A block registry alone is a land record; work records without the asset are a free-floating task log; yield without the asset is a bare statistic; asset plus work without recorded outcomes is a journal with no production loop.

### One Structure, Many Implementations

The core is written in conceptual terms. Products realize each concept differently:

```text
Concept:   the persistent planting asset
Realized as:   vineyard/estate → block → row → vine;
               GPS-drawn block fences with automatic acreage;
               GIS/spatial imports of the block model

Concept:   planting identity
Realized as:   variety + clone + rootstock (common); area, planting year,
               row spacing, vine count (common); appellation/AVA
               (regional — sometimes resolved automatically from location)

Concept:   phenology
Realized as:   modified E-L growth stages (named in some products);
               dated stage observations block by block (universal)

Concept:   the vintage's outcome
Realized as:   weighed deliveries/weigh tags at the crush pad;
               loads/bins/tons credited per block;
               expected-vs-actual tons per block vintage
```

A reader who has only seen one realization — say, a winery suite whose vineyard module ends at weigh tags — should still be able to recognize a grower-side block-and-spray system as the same Type.

### Standard Capabilities

Mature products commonly add these. They make the system practical; they do not define the Type:

- **Variety catalog** — varieties with clone and rootstock detail, established before locations so work can be recorded variety-specifically.
- **Spray programs and records** — planned and recorded applications with rates (sometimes calculated from canopy size and growth stage), chemical inventory, and worker-safety intervals (re-entry, pre-harvest); in the Australian and New Zealand tradition, the **spray diary** kept to the standard of the winery buyers and industry bodies.
- **Job and crew machinery** — work orders assigned to blocks and crews ("today's blocks, today's tasks"), timesheets for teams and individuals, piece rates for pruning and harvest, payroll integration; for labour contractors, recording work to invoice clients.
- **Crop estimation machinery** — sampling requests, bunch and cluster counts, berry weights, progressive yield estimates, expected-versus-actual tons per block.
- **Maturity programs** — sampling linked to block and vintage, lab integration, year-over-year ripening comparison driving pick-date decisions.
- **Quality assessment of work** — in some products, pruning quality scores and crew performance on dashboards.
- **Block-level economics** — cost per block, variety, and vintage; block-level profit and loss; budget variance reported to owners or billed parties.
- **Vintage organization** — a vintage record per harvest year with block vintages beneath it, managed from planning through completion.
- **Harvest coordination** — crews and equipment, deliveries received at the scale, weight tickets, traceability of loads or bins back to the block.
- **Mobile field capture with offline capability**, paired with a web dashboard; GPS throughout (block boundaries; in some products, spray paths and located repair notes for broken trellis wires or missing vines).
- **Integration surface** — winery software (maturity samples, harvest intakes), sensor providers (climate, growing degree days), GIS and spatial data, payroll and finance systems.

## How It Works

### Set up the asset

```text
Create the variety catalog (variety, clone, rootstock)
→ add vineyards/estates
→ add blocks: draw or import boundaries, assign varieties,
  record area, planting year, row spacing, trellis, vine count
→ where needed, add rows and individual vines
→ define job types and pay rates
→ add staff and crews
```

Setup is done once and maintained over years; the block record persists as varieties change, areas are edited, and blocks are eventually replanted.

### Run the perennial cycle

```text
Prune (winter) → crews clocked in to blocks/rows; pruning jobs recorded
                per worker; quality assessed; piece rates settled
Protect and feed (spring–summer) → spray programs scheduled and recorded
                against blocks; safety intervals observed; chemical
                inventory drawn down
Canopy work → shoot thinning, leaf pulling, hedging recorded as they happen
Crop reduction → fruit dropped/thinned, recorded against the block
Irrigate and repair → operations and trellis/vine repairs recorded
Observe → phenology stages dated block by block; pest and disease
          sightings; weather and damage events logged
```

Each operation lands as a dated, attributed record on the block or row. The manager's daily view answers: what, where, and by whom is being done today — and how fast, at what cost.

### Ripen, estimate, decide

```text
Sample maturity (sugar, acidity, pH) per block, linked to the vintage
→ count bunches, weigh clusters → progressive yield estimates
→ compare ripening against previous vintages
→ make the pick-date call per block
→ schedule crews, equipment, and winery capacity around expected tons
```

### Harvest and credit

```text
Pick → fruit recorded per block (crews, loads/bins/tons)
     → deliveries weighed at the scale; weight tickets issued
     → credited to the block and variety; pickers credited for piece pay
     → block identity (variety, vintage, appellation) travels with the
       fruit toward the crush pad and, in winery-integrated systems,
       into the cellar record
```

### Close the vintage and look back

```text
Actual tons vs expected per block vintage → quality notes
→ costs by block, variety, and vintage → vintage-over-vintage comparison
→ decisions for next cycle (pruning severity, crop reduction, renewal)
→ (eventually) replant or rework a block, updating the planting record
```

### Capability tiers

**Defining core** — without these, not vineyard management:

- the persistent planting asset with planting identity
- perennial-cycle viticultural work recorded against the asset
- the vintage's fruit outcome credited to the asset as accumulating history

**Standard capabilities** — present in most mature products:

- variety catalogs; spray programs and records with safety intervals
- job/crew machinery with piece rates and payroll integration
- crop estimation and maturity sampling driving pick decisions
- block-level cost and profitability; vintage organization
- harvest crediting with weighed deliveries and block traceability
- mobile + offline capture with a web dashboard; GPS
- integration with winery software, sensors, and GIS

**Optional / variant** — depends on segment, region, and business model:

- appellation/AVA machinery (regional)
- vine-level identity and vine audits (deep-viticulture segment)
- grape contracts, grower payments, buyer settlements (fruit-trading structures)
- sustainability and certification tracking
- machinery/fleet management; damage-event recording
- bundled monitoring: sensors, weather, disease models, satellite data
- labour-contractor invoicing and workforce-compliance documents

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Setup / admin surface

The asset registry. Purpose: build and maintain the planting hierarchy and its catalogs. Typical information: vineyards, blocks, rows, vines, varieties with clone/rootstock, job types, pay rates, staff and crews. Primary actions: create and edit hierarchy levels, draw or import block boundaries, assign varieties, define jobs and rates.

### Field app

The crew-facing capture surface, used in the vineyard. Purpose: record work and observations as they happen. Typical information: today's blocks and tasks, rows with completion state, spray program details, sampling requests, phenology stages. Primary actions: clock in, record spray trips (with GPS path where offered), record pruning and canopy work per worker, enter maturity samples and bunch counts, drop repair pins, photograph issues. Offline operation is standard.

### Dashboard

The manager's web surface. Purpose: see the operation over time and get reports out. Typical information: block map with status, ripening curves against previous vintages, expected-versus-actual tons, yield and cost by block, variety, and vintage, crew productivity and pruning quality. Primary actions: filter, drill down, plan the vintage, export payroll and compliance reports.

### Records and reports surface

The compliance face. Purpose: produce the records regulators, winery buyers, and auditors ask for. Typical information: spray diaries and application histories with safety intervals, workforce and safety records, audit-ready exports. Primary actions: compile, fill, export.

### Winery handoff surface (where present)

In winery-integrated products, the surface where the vineyard's record becomes the winery's: weigh tags created at the crush pad, linked to the block vintage, carrying variety and appellation into the cellar record. Primary actions: receive fruit, create weigh tags, follow the lot into the cellar.

## Important Rules / Behaviors

### The asset outlives the vintage

Records bind to a block and its varieties across years. The unit of management is not "this year's crop" but the planting itself; vintage history accumulates on the asset. Replanting or reworking a block is an edit to the asset's record, not the creation of a new field.

### The vintage organizes the season

The harvest year is the system's season unit: records are stamped with the vintage (a winter pruning belongs to the vintage the season's fruit will feed), block vintages carry expected versus actual tons, and ripening is compared vintage over vintage. Exact vintage lifecycle stages vary by product.

### Ripening drives the pick

Maturity sampling and crop estimation are not passive records: they are the machinery of the season's central decision — when to pick each block, and with what crews and winery capacity. Samples link to the block and vintage so the decision trail is auditable.

### Piece-rate crediting ties work to pay

Vines or rows pruned, tons or bins picked are credited to named workers and flow to payroll. Rates are configurable per job and commonly per variety or block. For labour contractors, the same records drive client invoicing.

### Spray records carry legal and commercial weight

Applications are recorded with product, rate, timing, and location; worker re-entry and pre-harvest intervals gate subsequent work. In the Australian and New Zealand tradition, the spray diary is kept to the standard of winery buyers and industry bodies — a grower supplying several wineries must be able to produce spray records for each. Record-keeping requirements vary by jurisdiction; the record-keeping duty itself is structural.

### Block identity travels with the fruit

Where the system reaches the winery, the block's identity — variety, vintage, appellation — flows with the fruit into the cellar record, making wine traceable back to the blocks that made it. This is the structural reason the block, not the field, is the unit of record.

### Exact mechanics vary by product

State labels, rate structures, report formats, and integration depths differ across products. The behaviors above are the stable shape; their precise parameters are product decisions.

## Variants

- **Grower-side pole** — standalone systems centered on the planting asset and its work: spray programs, pruning and canopy jobs, crews and piece rates, block economics, harvest credited to blocks. Serves independent growers, estates, and vineyard management companies.
- **Winery-integrated pole** — vineyard modules inside winery production suites, where the block asset is the front end of the wine production record: ripening feeds pick decisions, weigh tags feed the cellar, block identity flows to the bottle. Serves estate wineries and wineries buying fruit.
- **Business-model variants** — estate winery's own vineyards; independent grower selling fruit under contract (grape contracts, buyer settlements); vineyard management company running client estates (billed-party reporting); vineyard labour contractor (crews supplied, workers paid, clients invoiced).
- **Regional regimes** — US appellation machinery (automated AVA resolution); Australian and New Zealand spray-diary and export-compliance tradition with industry-body submissions; other regions' treatment-record traditions.
- **Depth variants** — row-level standard; vine-level identity and vine audits in deep-viticulture operations; block-only recording in lighter products.
- **Monitoring-bundled vs monitoring-adjacent** — some operations run vineyard management beside a separate sensing/model service (weather stations, disease models, satellite imagery); bundling varies by vendor and region.
- **Crop-type scope** — winegrapes define the Type; some specialty-crop platforms extend the same machinery to other perennial crops, and some vineyard products generalize toward broader farm management.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Orchard Management | closest sibling | same perennial-asset family shape (persistent planting + perennial work + season outcome); the seam is domain binding and continuation — winegrapes with viticultural operations (canopy work, trellis repair, E-L-class phenology), maturity sampling as standard season machinery, and a winery-bound fruit flow vs tree fruit with per-tree piece work, grafting/top-working, and a packhouse-bound flow |
| Winery Management | downstream | begins at fruit intake and runs fermentation → production → bottling; the vineyard Type ends at weighed fruit credited to blocks with identity flowing toward the winery; winery suites package both sides, the vineyard module being this Type at module grain |
| Crop Management | genus sibling | its unit of record is the season-scoped crop (crop × field × season, closed with season history); the vineyard's unit is the persistent planting that outlives every vintage, with viticulture-specific operations and a winery-bound outcome the annual cycle lacks |
| Harvest Management | interlocking | its center is the harvest operation itself (crews, ticketing, crediting, handoff), crop-agnostic; the vineyard's harvest leg is the asset's outcome record, not the operation machinery |
| Farm Labor Management | interlocking | crew/time/piece-rate machinery is shared; the labor Type centers the workforce across the farm, the vineyard Type centers the asset; the vineyard labour contractor is a shared user |
| Crop Protection Management | interlocking | spray records, safety intervals, chemical inventory are that domain's machinery; vineyard management carries them as one recorded operation among many — plus the winery-facing spray diary |
| Irrigation Management | interlocking | water decisions are that Type's center; the vineyard records irrigation as one operation among many |
| Precision Agriculture / Agricultural IoT / Crop Remote Sensing | adjacent | sensing- and model-driven decision support; the monitoring pole lacks the asset record entirely, and vineyard management consumes monitoring without being defined by it |
| Field Management | substrate | the land-unit register (extent, soil, boundaries) is the ground the planting sits on — leg one alone |
| Farm Management Platform | broader | whole-operation scope (land, livestock, finance, equipment); vineyard management is production-scoped to the planting asset |
| Agricultural GIS | substrate | spatial machinery (boundaries, maps, layers) consumed by the vineyard model, not the record itself |
| Nursery Management | sibling | propagates plants as sale inventory; the vineyard grows fruit for harvest from planted vines |

The boundary with Orchard Management is the most important one, because the two Types share the perennial-asset family shape. The structural test: if the system's center is the winegrape planting with viticultural operations, maturity-driven picking, and a winery-bound fruit flow, it is Vineyard Management; if the center is the tree-fruit planting with per-tree piece work and a packhouse-bound flow, it is Orchard Management. The boundary with Winery Management is the crush pad: fruit credited to blocks on one side, wine production records on the other.

## Representative Products

- **AgCode (AgilityAg)** — US specialty-crop farm management with vineyard origin (began 2002 for grapes and vines; early customers include major wineries and a vineyard management company); grower-side operational pole with scale deliveries, certified weight tickets, and block-level profit and loss
- **Vinea** — New Zealand integrated vineyard management software for grape growers, wine companies, and labour managers; viticulture-depth pole with block → row → vine model, E-L-scale phenology, pruning quality assessment, and winery-software integration
- **VineTrack** — Australian vineyard management app built by a working vigneron; small-grower mobile-first pole with GPS blocks, canopy-based spray programs, E-L stages, and cost by block, variety, and vintage
- **Crush.wine** — US winery software whose vineyard module fronts the cellar; winery-integrated pole with block vintages, weigh tags, and automated AVA resolution
- **InnoVint** — US winery production suite with a vineyard tracking module and grape/grower contract management; winery-integrated pole at mid-market tier

Boundary specimens examined to draw seams: vintrace + eVineyard and Vinsight (winery suites carrying the vineyard module), JDE EnterpriseOne Grower Management (enterprise processor-side grower records), Semios and Integrape (monitoring/data poles), Wine Business Monthly's 2006 and 2011 vineyard software surveys (historical anchor).

## Sources

Research date: **2026-09-10**

- AgCode / AgilityAg — official site: https://agcode.com/ ; trade article on the product's vineyard origin: https://fruitgrowersnews.com/news/agcode-marks-20-years-of-software-solutions-for-specialty-crops
- Vinea — official site: https://www.vinea.co.nz/ (home, about, wine-companies, labour-managers pages); Microsoft Marketplace listing: https://marketplace.microsoft.com/en-us/product/saas/informationpowerlimited1610485179650.vinea_nova ; company LinkedIn page: https://linkedin.com/company/vinea-software
- VineTrack — official site: https://www.vinetrack.com.au/ (home, about, discover); App Store listing: https://apps.apple.com/au/app/vinetrack/id6761143377
- Crush.wine — Vineyard Management feature page: https://crush.wine/features/vineyards
- InnoVint — Vineyard Tracking product page: https://www.innovint.us/product/vineyard-tracking ; growing-season article: https://www.innovint.us/insight/vineyard-information-anywhere-anytime
- vintrace — eVineyard acquisition announcement: https://www.vintrace.com/vintrace-evineyard-bringing-the-winery-and-vineyard-closer-than-ever
- Oracle — JDE EnterpriseOne Grower Management documentation: https://docs.oracle.com/cd/E16582_01/doc.91/e15114/enter_farm_block_harvest.htm
- Wine Business Monthly — vineyard software surveys (2006, 2011) and Wines & Vines articles, via winebusiness.com / winebusinessanalytics.com
- Vinsight — products page: https://www.vinsight.net/products
- NZ Winegrowers member portal: https://portal.nzwine.com/

> Sourcing limitation: several vineyard-sector vendors could not be reached from the research environment (FarmSoft returned errors in a prior pass and was not retried; AgCode's vineyard segment page is not reachable on the rebranded site — its vineyard origin rests on a third-party trade article). Some corroborating sources (Vinsight, the trade-press surveys, Vinifera, Tabula) were captured via search-index excerpts rather than direct fetches. Precise operational details beyond what these pages support (exact rate structures, numeric limits, integration catalogs) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
