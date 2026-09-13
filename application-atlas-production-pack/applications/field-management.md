# Field Management

## Overview

A **Field Management** application is the land-unit system of record for a farming operation. It holds the operation's fields — also called paddocks, blocks, plots, or beds — as a persistent register of individually identified land units; it defines each unit as a distinct piece of land with an extent and, where kept, standing characteristics such as soil or mapped infrastructure; and it accumulates, attached to each field, the history of what happened on and to that land across seasons and years.

Its purpose is to give the farm a durable, spatially grounded memory of its land: which pieces of ground exist, what each one is, and what has been done to it. Crops, animals, machines, and people pass over the land; the field record stands.

The boundary is equally clear. This Type centers the land unit itself. It does not center the whole business of the farm (Farm Management Platform), the crop grown on the land in a given season (Crop Management), the georeferenced land base and its spatial analysis (Agricultural GIS), or any single agronomic domain such as soil or irrigation (their own Types).

## Users & Context

The primary user is the farm operator or farm manager who is responsible for the land: registering new fields, keeping boundaries and characteristics current, and reviewing what each field's history says before deciding what to do with it next.

Around that center:

- **field staff and crews** record work and observations against fields as they occur, often from mobile devices in areas without signal;
- **agronomists, consultants, and advisors** work across many client farms' fields, reading field history and attaching plans, recommendations, or notes;
- **family members and teammates** share the same farm map and records under role-based access.

Typical moments of use: setting up the farm's fields when adopting the product (drawing or importing boundaries), recording that something happened on a field, checking a paddock's condition before moving stock onto it, comparing fields for a decision, and answering "what did we do with this field in past years?" for planning, audits, or compliance.

## Core Model

### The Defining Core

```text
Field register of record
└── Field (persistent, individually identified land unit)
    ├── Definition & standing characterization
    │   (extent — area and/or boundary; soil, land features, infrastructure where kept)
    └── Field-anchored history
        (dated records of activities, inputs, observations,
         outcomes, and changes to the field itself, across seasons)
```

Three structures. If any one is removed, the product is no longer recognizable as field management:

- **The field register of record** — the operation's land units held as persistent, individually identified records. Identity outlasts any season, crop, or year: the field that grew corn in one year and soybeans the next is the *same* record. Without a standing land register, a product is season-scoped crop record-keeping or a monitoring dashboard — the field is merely a tag, not a managed asset.
- **The field's definition and standing characterization** — each record defines the land unit as a distinct piece of land with an extent. In most current products the extent is boundary geometry on a map (drawn by hand, selected from pre-delineated or cadastral land units, imported from files, or auto-detected from satellite imagery) together with an area figure; in simpler forms a measured area with a location reference can carry the same meaning. Where kept, the record also holds standing land characteristics — soil, land class, usage category — and mapped infrastructure such as fences, water points, or hazards. Without a defined land unit, "fields" collapse into location labels on generic records.
- **Field-anchored history** — records of what happened on and to each field attach to the field record and accumulate across seasons as the field's retained history, retrievable per field: work performed, inputs applied, observations and scouting notes, soil tests, harvest outcomes, and changes to the field itself. Without this, the product is a static digital farm map — a drawing of the land with nothing managed.

### What Mature Products Add

These capabilities are widespread and expected, but they refine the core rather than define the Type:

- **An interactive farm map as the organizing surface** — the user navigates the operation by map, clicks a field, and drills into its details and history.
- **A container hierarchy above the field** — fields grouped under farms, clients, or parent land units; the exact shape varies by product and account type.
- **Per-field record families** — activities and input applications, observations and scouting notes, soil tests, harvest and yield outcomes.
- **Multi-year and cross-field views** — a field's records across years; side-by-side comparison, sorting, and grouping of fields.
- **Field lifecycle operations** — create (draw, select, import, or auto-delineate), rename, edit boundaries, archive or delete.
- **Mobile capture with offline sync** — recording from the field without connectivity, syncing later.
- **Sharing and roles** — teammates, advisors, and contractors with governed access to the same fields and records.

### One Structure, Many Implementations

The core is written conceptually; realizations differ:

```text
Concept:   Extent of the land unit
Forms:     drawn boundary geometry · pre-delineated/cadastral unit selection ·
           imported shape files · satellite auto-delineation · measured area

Concept:   Standing characterization
Forms:     soil test records on the field · soil data layers ·
           land class / usage categories · mapped infrastructure and landmarks

Concept:   Field-anchored history
Forms:     log entries referencing the field · season- or year-filtered records ·
           crop-rotation entries on the field · grazing movement records
```

A reader who has only seen one map-first implementation should still recognize a record-first field system from the core.

## How It Works

### Register the land

```text
Set up the operation
→ define the land units: draw boundaries on the map, select pre-delineated
  fields or cadastral units, import boundary files, or trace auto-detected fields
→ name each field and record its area
→ add standing characteristics where kept (soil, land class, infrastructure)
→ organize fields under farms/clients where the product uses a hierarchy
```

This is the one-time, maintained foundation: everything else in the product attaches to these records.

### Record against a field

```text
Something happens on the land
→ open the field (from map or list)
→ record the event: work performed, input applied, observation, soil test,
  grazing move, harvest outcome
→ the dated record attaches to the field and accumulates into its history
```

Recording is deliberately low-friction and often happens in the field itself, offline, with photos and GPS; records sync when connectivity returns.

### Use the field's history

```text
A decision or question arises
→ open the field and read its accumulated history across seasons
→ compare fields on characteristics, condition, or outcomes
→ plan the next season's use of the field (crop, grazing, improvements)
→ produce reports for planning, audits, or compliance from the same records
```

The field's history is the product's payoff: it turns the register from a map into institutional memory.

### Maintain the field itself

```text
The land changes
→ edit boundaries to match reality (some products version boundary changes by
  season so past records stay attributable to the geometry of their time)
→ rename, re-categorize, or archive fields that go out of use
→ history remains attached to the field record through these changes
```

## Interfaces

Described conceptually; names and layouts vary by product.

### Farm map

The visual heart of most implementations.

- the operation's land drawn to scale, fields as outlined polygons, infrastructure and landmarks where mapped
- click a field to open its record; color-coding by usage category or current state where supported
- primary actions: select a field, edit boundaries, measure distances, place landmarks

### Field detail

The record surface for one land unit.

- identity (name, container), extent (boundary, area), standing characteristics
- the field's accumulated history: dated, attributed records across seasons
- primary actions: record an event, add an observation or soil test, edit field information, view history by year

### Field list

The register as a table.

- one row per field: name, area, container, current use or state
- primary actions: sort, filter, group, compare across fields, add or import fields

### Recording surfaces (mobile)

The capture layer used in the field.

- the current field or location, quick-entry forms for work/observations/movements, photo and GPS attachment, offline queue

### Reports

Structured output drawn from the same records.

- per-field and cross-field summaries over chosen periods; audit- and compliance-oriented exports where the product supports them

## Important Rules / Behaviors

- **Field identity is durable.** Renaming, recategorizing, or changing boundaries does not reset the field's history; the record persists and history stays attributable to it. How geometry changes interact with history varies — some products version boundaries by season so each era's records match the geometry of its time.
- **The field outlives its contents.** The crop on a field, the mob grazing it, and the season in question are all time-bounded; the field record is not. Records reference the standing field, not a seasonal copy.
- **Extent is maintained, not assumed.** Boundaries and areas are user-maintained data. Products differ in how precisely they support correction (point-level editing, cutting out unusable areas, adjusting against imagery), but the extent on the record is the basis for every area-based measure (application rates, stocking rates, yields per unit).
- **Records are attributed and dated.** Field history is only trustworthy for planning and audit if each entry carries who and when; mature products enforce or encourage this.
- **Archiving over deleting.** Where land goes out of use, products typically archive or retire the field record rather than destroy it, preserving the operation's land memory. Deletion exists in some products; it forfeits the history.

## Variants

- **Row-crop / arable realization** — fields organized under farms or clients, extent maintained against satellite or machinery data, history dominated by crop rotations, input applications, and yields.
- **Grazing / paddock realization** — paddocks as the map unit, history dominated by stock movements; standing state includes feed on offer, stocking rate, and grazing days; movement records recalculated against the paddock record.
- **Horticultural / small-area realization** — beds and small blocks as land units, with plantings tracked as contents that move onto and off the land.
- **Record-keeping-first pole** — the register and its history are the product's center, organized around records and reports.
- **Data-platform-first pole** — the register is the substrate onto which data layers (imagery, yield, sensor) are organized; the deeper the center of gravity moves into monitoring and prescriptions, the closer the product sits to Precision Agriculture.
- **Advisor-managed accounts** — consultants or retailers maintain fields and records across many client operations.

## Related Application Types

| Type | Distinction |
|---|---|
| Farm Management Platform | centers the whole operation — the business entity with its inputs, labor, finances, and production subjects; the field register is its land substrate, not its center |
| Crop Management | centers the crop-season — a defined crop grown on an identified field for one cycle; the field appears as the season's substrate, and the managed loop is planning → operations → harvest |
| Agricultural GIS | centers the georeferenced land base — spatial layers, imagery, and analysis over many properties; here geometry is one attribute of the operator's field record |
| Soil Management | centers soil itself — testing programs, fertility, amendments; soil data attaches to fields here as one characterization among several |
| Precision Agriculture Platform | centers data-driven optimization — imagery, variable-rate prescriptions, sensor feeds; fields are the addressing layer, the monitoring loop is the point |
| Irrigation / Nutrient / Crop Protection Management | center single agronomic domains as managed programs; each attaches to fields but owns one subject class |
| Agronomy Management | centers agronomic decisions and recommendations; recommendations may be authored at field level, but the managed subject is the advice, not the land |
| Construction Field Management | shares only the word "field" — a construction site-execution system (daily site records and work items), unrelated to land management |

The most delicate boundary is with Farm Management Platform and Crop Management, because the field register appears in both. The discriminator is the center of gravity: remove the whole-operation business scope and a Farm Management product collapses to this Type; remove the crop-cycle records and a Crop Management product collapses to it; keep only the crop-season loop or only the business loop and the land center is gone.

## Representative Products

- farmOS — open-source farm record keeping with an explicit land-asset model
- Climate FieldView — field-centric data platform for row-crop operations
- AgriWebb — paddock-centered grazing management (Australia / New Zealand / UK / US)
- OneSoil — satellite-based field platform with field-boundary management at its base
- Agworld — collaborative field-level records and planning with advisors

The definition was checked against the grazing/paddock tradition, the record-first and data-first poles, and the paper-era farm field book, so it does not depend on any single region's vocabulary or the modern satellite/mapping implementation.

## Sources

Research date: **2026-09-08**

- farmOS User Guide — https://farmos.org/guide , https://farmos.org/guide/assets
- Climate FieldView — https://climate.com/ , https://climate.com/en-us/resources/getting-started.html , https://climate.com/en-us/resources/getting-started/fieldview-101-overview/map-your-fields.html
- AgriWebb — https://www.agriwebb.com/ , https://www.agriwebb.com/solutions/farm-mapping/ , https://help.agriwebb.com/en/
- OneSoil — https://onesoil.ai/en , https://help.onesoil.ai/en/ (Fields articles: adding fields; editing field information and boundaries)
- Agworld — https://www.agworld.com/

> Sourcing limitation: Agworld evidence is product-page depth only, and Climate FieldView's knowledge-center articles were not retrievable as individual pages. Claims relying on those sources are stated at cross-product strength, and no precise operational details (numeric limits, plan-specific behavior) are asserted for them. Product-by-product observations and the evidence record are kept in the paired Research Notes.
