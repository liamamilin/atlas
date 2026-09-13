# Forestry Management

## Overview

A **Forestry Management** application is the forest estate's system of record: it holds the forest as a managed estate divided into mapped, addressed management units, maintains a standing inventory of what grows on each unit, and plans and records the multi-year program of silvicultural treatment and harvest that works that forest across years and decades.

Three structures define the Type, and all three must be present:

```text
Forest estate of record
└── mapped, addressed management units (stand / compartment / coupe / block)
    └── standing forest inventory per unit
        └── silviculture-and-harvest program planned and recorded per unit
```

Everything else commonly associated with modern forestry software — web-GIS mapping engines, mobile cruise apps, LiDAR and remote-sensing inventory, optimization-based harvest scheduling, valuation models, certification reporting — is widespread in current products but is not what makes the product a forestry management system. The paper-era working-plan tradition (compartment registers, stand maps, cruise tally sheets, rotation plans) satisfies the same definition without any of it.

When the center of gravity shifts to executing the harvest job itself, or to the flow of logs to mills, the product is drifting toward a different Application Type (Logging Operations Management, Timber Supply Chain Management).

## Users & Context

Primary users:

- **forest manager / forester** — owns the estate record: keeps unit and inventory data current, plans treatments, records what was done, reports on condition
- **planner / analyst** — builds the estate-level picture: schedules harvest and silviculture across units and years, compares scenarios, projects growth and value
- **field crew / contractor supervisor** — captures cruise and inspection data in the field, records completed work against units

Secondary users:

- **landowner / asset manager** — reads valuation, condition, and program progress; in investment-grade estates this is the primary lens
- **government or agency administrator** — manages a public multi-use estate with stronger accountability and public-reporting needs
- **consultant** — runs the same record world on behalf of many small owners

The work context is long-horizon land stewardship: a decision made today (planting, thinning, deferring a harvest) shapes the forest for decades. This time signature — inventory that grows, plans that span decades, records that outlive individuals — is what separates forestry management from most other land-management software.

## Core Model

### The Defining Core

**The forest estate of record.** The forest is held as a managed estate — an ownership or tenure holding — organized into spatially addressed management units. Regional vocabulary varies (stand, compartment, coupe, block), but the structure is stable: each unit carries identity, area, location, and the tenure or ownership context it sits in. The unit is the anchor everything else hangs on; it is persistent, and it survives any number of treatments and harvests.

**Standing forest inventory per unit.** Each unit carries a description of the growing forest — species composition, age or size class, stocking or volume — maintained as living data. The inventory is what makes the forest an asset rather than just land: it is measured (field cruise, mobile capture, remote sensing) and/or modeled (growth projection), and it is consumed by everything downstream — planning, valuation, reporting. Unlike warehouse stock, this inventory grows on its own between interventions; keeping the record aligned with that slow biological reality is the standing work of the Type.

**The multi-year silviculture-and-harvest program.** Treatments are planned and recorded per unit across years to decades: regeneration and planting, tending, fertilization, thinning, and finally harvest. Each unit accumulates its treatment history — a forest's record is its biography. The mature form schedules this program across the whole estate (harvest scheduling, sustained-yield planning), because what one unit yields in a year must be balanced against the growth of the rest.

All three are jointly load-bearing:

- estate alone → a land registry or map viewer
- inventory alone → a one-shot cruise calculator or report
- program alone → a generic task tracker with no forest in it
- estate + inventory without the program → an inventory census or valuation snapshot
- estate + program without inventory → activity mapping with no forest state behind it
- inventory + program without the estate → plot-level records with no holding they belong to

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the Type practical; they do not define it.

- **Map-centric estate view** — units as polygons over base imagery, with layers; the map is the dominant way to navigate the estate.
- **Mobile field capture** — cruise and inspection apps that record plot or tree observations on-site and sync them into the inventory.
- **Remote-sensing inventory update** — aerial imagery, satellite, or LiDAR-derived inventory as a modern alternative or complement to ground cruise.
- **Growth projection** — forecasting how the standing stock develops over years and decades.
- **Scenario planning and harvest scheduling** — comparing alternative treatment and harvest programs against yield, value, and constraint trade-offs; optimization engines are the enterprise expression of this.
- **Valuation** — the estate's timber and land value, sometimes including environmental value such as carbon.
- **Roads and infrastructure records** — access planning coupled to harvest, since a scheduled harvest needs a road.
- **Permits, environmental documentation, certification reporting** — the accountability layer for regulators and certification schemes.
- **Activity tracking** — scheduling and completing work on units, including contractor activity, with dashboards and operational reporting.

### One Structure, Many Implementations

```text
Concept:          Estate organized into management units
Implementations:  stands, compartments, coupes, blocks, plots; property→block→stand hierarchies

Concept:          Standing inventory
Implementations:  ground cruise (mobile tally), remote sensing / LiDAR models, growth-and-yield projection

Concept:          The treatment-and-harvest program
Implementations:  working plans, silvicultural prescriptions, harvest schedules, annual operating plans, work orders
```

A reader who has only seen one realization — for example a LiDAR-inventory dashboard — should still be able to recognize a cruise-notebook-and-working-plan operation as the same Type.

## How It Works

### Establish the estate

```text
Register the property/tenure
→ divide it into management units on the map
→ describe each unit (area, location, site, tenure context)
→ seed the inventory (cruise, imagery, or existing records)
```

The estate record is standing infrastructure: it changes slowly (boundaries, acquisitions), and everything else references it.

### Maintain the inventory

```text
Plan a cruise / order an imagery or LiDAR update
→ capture observations in the field (or receive modeled data)
→ update unit-level inventory attributes
→ project growth forward
```

Inventory maintenance is cyclical and never finished — the stock changes whether or not anyone acts.

### Plan and run the program

```text
Inspect units and projected growth
→ prescribe treatments per unit (planting, tending, thinning)
→ schedule harvest across the estate against yield, value, and constraints
→ execute season by season
→ record completions back onto the unit
→ report condition, yield, and compliance
```

The loop closes on the unit record: every executed treatment and harvest updates the unit's history and its inventory state, and feeds the next planning round. A harvest does not delete the unit — on a replanted estate it starts the unit's next rotation.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- forest estate of record
- mapped, addressed management units
- standing forest inventory per unit
- multi-year silviculture-and-harvest program with per-unit treatment history

**Common mature structure** — present in most modern products:

- map/GIS estate view
- mobile field capture
- remote-sensing/LiDAR inventory
- growth projection
- scenario planning / harvest scheduling
- valuation
- roads records
- permits / certification / regulatory reporting
- activity and contractor tracking with dashboards

**Variant / optional** — depends on customer shape, region, and era:

- nursery and seedling production; breeding/genetic programs
- carbon accounting and environmental value modeling
- machine- and load-level execution machinery (belongs to adjacent Types; appears here only as packaging)
- urban-tree object world (see Variants and Related Types)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Estate map

The primary navigation surface.

- units drawn as polygons over base imagery, with toggleable layers
- typical information: unit identity, area, species/age coloring, program status
- primary actions: select a unit, inspect details, draw or adjust boundaries, plan an action on a selection

### Unit detail record

The system-of-record view of one management unit.

- typical information: attributes (area, site, tenure), current inventory, treatment history, planned activities, documents
- primary actions: edit attributes, record an observation or treatment, plan the next intervention

### Inventory workspace

Where the forest's measured state is maintained.

- typical information: cruise projects or sensor-derived inventories, plot/tree observations, per-unit rollups, growth projections
- primary actions: plan and load a cruise, capture or import observations, recompute unit inventories

### Planning workspace

Where the estate's future is shaped.

- typical information: scenario alternatives, harvest and silviculture schedules by period, yield/value projections
- primary actions: build or copy a scenario, apply constraints, compare outcomes, commit a schedule

### Operations / activity views

Where committed work is run.

- typical information: scheduled activities by unit and season, completion status, contractor activity
- primary actions: schedule, dispatch or hand off, record completion, review progress on dashboards

### Mobile field surface

Crew- and inspector-facing capture.

- simplified views over the same records: current unit, forms for observations and completions, offline capture with sync

### Reporting

Accountability output for owners, regulators, and certification schemes: condition summaries, yield and program progress, compliance evidence.

## Important Rules / Behaviors

### The unit record outlives the harvest

Harvest ends the standing stock of a rotation, not the record. On managed estates the unit persists into its next rotation, carrying its accumulated history. Records are biographies, not transactions.

### Inventory has its own clock

Stock changes through growth even with no human action. A management system that only updated inventory at harvest would drift out of reality; hence the standing machinery of cruise cycles, imagery updates, and growth projection.

### The program is estate-coupled

What one unit yields this year is balanced against the growth and constraints of the whole estate — sustained yield and schedule feasibility are estate-level properties, not per-unit ones.

### Treatment history constrains the next decision

Silvicultural history (what was planted, when it was thinned, what remains) is input to the next prescription; the record is not just documentation but the working basis of planning.

### Accountability is structural

Regulatory and certification reporting draws directly on the record — activities, areas, environmental documentation. In many deployments the reporting obligation shapes how rigorously activities must be recorded, but it is a driver, not the defining structure.

## Variants

- **Integrated estate-management suites** — the full record world (estate, inventory, program, reporting) for large industrial or investment-grade estates, often sold alongside execution and logistics product lines.
- **Planning-and-optimization-led deployments** — the record and analytics focused on long-horizon scheduling and valuation, with field and execution systems supplied elsewhere; the optimization engine is the product's center of gravity.
- **Inventory-first slices** — remote-sensing or cruise products that maintain the inventory layer and hand off to planning tools; a capability slice at the Type's edge rather than a separate Type.
- **Government / agency estates** — multi-use public land with stronger public-accountability, permits, and multi-value (recreation, water, habitat) reporting alongside timber.
- **Consultant and small-owner practice** — the same record world, lightweight, serving many small holdings; regional silvicultural traditions shape terminology and program shapes (plantation vs natural forest, even-aged vs uneven-aged management).
- **Urban/community forestry (closest cross-boundary relative)** — individually addressed trees rather than stands; care programs and removals rather than silviculture and harvest; municipal/university/nonprofit audiences. It shares the inventory-of-record + care-program structure but replaces the estate object world, and is best treated as a boundary case rather than a variant of this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Logging Operations Management | adjacent (execution sibling) | runs the harvest job — crews, machines, production, loads; forestry plans and records the harvest on the estate, logging executes it |
| Timber Supply Chain Management | adjacent (downstream sibling) | moves logs from landing to mill and trades them; forestry holds the estate, not the log flow |
| Farm Management Platform | adjacent (agricultural cousin) | annual crops on fields that reset each season vs forests that persist for decades with growing standing stock |
| Conservation Management | adjacent (inverted purpose) | protection/restoration orientation on the land vs production orientation of the estate; field-data tooling may be shared |
| Fisheries Management | adjacent (parallel governance) | records authorized harvest of a wild common stock against entitlements; forestry manages an owned standing asset the owner actively grows and shapes |
| Government GIS / Land Records | substrate | parcel and cadastral records without growing-stock semantics or a treatment program |
| Natural Resource Rights Management | partial overlap | rights/permits as the whole world vs tenure and permits as a layer inside the estate record |
| Utility Vegetation Management | distinct subject | vegetation managed for infrastructure clearance vs forest managed as a production/stewardship estate |
| Precision Agriculture / Agricultural GIS | tooling overlap | shared geospatial tooling; different object world and time signature |

The most important boundary is with Logging Operations Management: vendors themselves split the market this way — forest management product lines hold the estate, inventory, and silviculture/harvest program, while separate operations lines carry machine, crew, and load machinery. Remove the estate record and only job execution remains (logging); remove the job execution and the estate record remains (forestry management).

## Representative Products

- Remsoft (FMS / INFLOR Forest, Woodstock Optimization Studio, Prism, AFRIDS)
- Trimble Forestry (Connected Forest family)
- PlanIT Geo TreePlotter (urban-forestry boundary pole)

The Core Model was checked against an individual-tree urban product (TreePlotter) to test which structures are estate-specific versus shared inventory-and-program machinery, and against an execution-and-logistics product family (Remsoft Operations/Logistics) to establish the seam toward Logging Operations and Timber Supply Chain.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Remsoft — https://www.remsoft.com/ , https://remsoft.com/solutions/fms/ , https://remsoft.com/woodstock-optimization-studio/
- PlanIT Geo (TreePlotter) — https://planitgeo.com/treeplotter/
- Trimble Forestry — https://www.trimble.com/en/industries/forestry (positioning page only)

> Sourcing limitation: vendor help centers and user guides were not reachable from the research environment on 2026-09-08 (Trimble product pages are JavaScript-gated and returned navigation shells on repeated attempts; additional candidate vendors were unreachable — domain lapsed or timed out). Evidence therefore rests on official product/solution pages of the reachable vendors plus cross-checking against an independent urban-forestry product. Precise operational details (attribute schemas, cruise methods, schedule granularity, numeric limits, default settings) are intentionally not stated in this document; such specifics remain out of scope rather than estimated. The historical (paper-era) check is conceptual, drawn from the discipline's documented working-plan tradition, not from a fetched historical source.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary tests are recorded in the paired Research Notes.
