# Feed Management

## Overview

A **Feed Management** application manages the feed side of animal production as its own subject: the ingredients and their nutrient composition and cost, the rations that define what should be fed to which animals, and the quantified movement of feed from supply through mixing to the animals that consume it.

Its defining structure is small:

```text
Feed items (ingredients / mixes, with composition + cost)
└── Ration (recipe: ingredient mix bound to nutrient targets, per recipient)
    └── Quantified feed flow (batches / loads / schedules)
        └── Recorded usage: delivered, consumed, lost — feed cost made computable
```

Everything commonly associated with modern products — least-cost optimization engines, guided mixing on mobile devices with connected scales, shrink analytics, robotic feeding, compliance labeling, cloud collaboration across plants — is widespread in today's market but is not what makes the software feed management. A paper-era operation with feed-composition tables, hand-computed rations, a feed ledger and a daily mixing sheet satisfies the same core.

The subject here is the feed, not the animal. Products whose unit of record is the individually identified animal belong to herd/livestock management; they may embed or link a feeding layer, but their world is organized around the animal. Conversely, formulation software that produces recipes for saleable products — pet food, food products — without binding them to animal groups and a daily feeding loop is food formulation, not feed management.

## Users & Context

Primary users, on the livestock-operation side (dairy, beef, swine, poultry and mixed farms):

- **feed manager / feeder** — sets up and adjusts rations, plans feeding schedules, executes and records loads
- **farm owner / manager** — watches feed cost and loss, the operation's largest recurring input expense
- **farmhand operating the mixer wagon or feeding equipment** — follows guided mixing instructions per load

Primary users, on the feed-industry side (mills, premix and feed producers):

- **nutritionist / formulator** — builds and revises recipes against nutrient targets, ingredient prices and legal constraints
- **purchasing / planning staff** — manage ingredient supply, contracts and availability that formulation depends on
- **quality manager** — keeps ingredient composition data and product specifications current

Secondary users include external nutrition consultants who manage rations across multiple client farms, and herd managers who consume feeding reports. The work environment on farms is dominated by the barn and the mixer wagon: feeding happens early, repeatedly and often under poor connectivity, which shapes how the software is operated — mobile surfaces, scale connections, quick guided flows.

## Core Model

### The Defining Core

```text
Feed items
└── Ration (plan of record per recipient)
    └── Quantified feed flow
        └── Recorded usage and cost
```

Three structures are jointly held. Remove any one and the product is no longer feed management:

- **Feed items as managed records** — every ingredient or commodity the operation can buy, store, mix or feed is a record carrying what it is nutritionally and what it costs. Mixed feeds and premixes are feed items too, so rations can compose from other rations' outputs. This is the substrate formulation stands on; without it, the tool is a generic recipe book or a commodity ledger with no nutrition semantics.
- **The ration as the feeding plan of record** — a recipe binding a mix of feed items to nutrient targets for a defined recipient: an animal group or pen, a species or life stage, or (on the mill side) a feed product. Rations are maintained over time, revised as ingredients, prices, production stages and performance change. Without the ration, the software is feed inventory or usage accounting with no answer to "what should these animals eat".
- **The quantified feed loop** — the ration becomes measured reality: batch or load quantities, mixing instructions, delivery to groups, and recorded actual usage from supply through to consumed feed, including what was picked back up or lost. This is what makes feed cost, intake and shrink computable rather than estimated. Without it, the software is a nutrition calculator with no managed supply behind it.

Two abstractions recur throughout and are worth naming:

- **The recipient** is whatever the ration is assigned to and fed against — most often a group of animals, sometimes a species/life-stage definition or a manufactured feed product. The animal appears here as a group being fed, not as an individually tracked subject.
- **The feed flow** is the movement of quantities: purchased or harvested feed enters supply, supply is drawn into mixes, mixes are delivered, leftovers and losses are picked back up or written off. Every step is a quantity against a feed item, which is why cost and loss can be computed end to end.

### Standard Capabilities of Mature Products

These capabilities are common across the researched sample and expected in the market, but they extend the core rather than define it:

- **Formulation machinery** — nutrient requirement targets per recipient, ingredient inclusion limits and ratios, and computation of a mix that meets them; least-cost optimization against ingredient prices, with marginal-price and what-if analysis. Some formulation-focused products make this the whole product.
- **Feeding schedules and load plans** — rations scheduled per group per feeding, expanded into batch or load quantities scaled to the group's current animal count.
- **Guided mixing / execution support** — step-by-step ingredient loading instructions during actual mixing, on mobile clients connected to scales or mixer-wagon data, recording each load as it happens.
- **Inventory and supply tracking** — on-hand quantities in bins, silos or feed-storage areas; purchases and usage; shrink and loss (including weighback of refusals) surfaced as analysis.
- **Feed economics** — cost per ton, per animal or per day; planned-versus-actual comparisons; scenario simulation when ingredient prices shift.
- **Ingredient data maintenance** — composition tables (nutrient matrices) kept current, in mature products increasingly fed by sample or lab analysis data.
- **Integration spine** — animal counts from herd-management systems so loads match real groups; connections to weighing and mixing hardware; performance data (milk yield, growth) fed back into ration decisions; on the industry side, purchasing, production and quality systems.
- **Compliance and documentation** (industry side) — generated specifications and declarations, including regulated labeling such as medicated feed where the market requires it.

### One Structure, Many Implementations

```text
Concept:          Feed items with composition + cost
Implementations:  ingredient databases, nutrient matrices, feedstuff composition files

Concept:          Ration as plan of record
Implementations:  recipes / formulas, ration sheets, per-pen feeding programs

Concept:          Quantified feed loop
Implementations:  batch mixing sheets, per-pen load plans with guided mixing,
                  robotic feeding driven by a feed-kitchen setup

Concept:          Recipient
Implementations:  pens/groups synced from herd software, species/life-stage definitions,
                  manufactured feed products at a mill
```

A reader who has only seen one pole — say, a dairy operation's mobile feeding app — should still recognize the mill-side formulation suite, and vice versa, as the same Type realized at different points of one supply chain.

## How It Works

### Set up the feed base and the recipients

```text
Enter ingredients with their composition and prices
→ define the animals to be fed (groups/pens, or species/life stages)
→ connect or record the animal counts that drive quantities
```

### Formulate the ration

```text
Choose the recipient and its nutrient targets
→ compose the mix from available feed items
  (by hand, or optimized against price and inclusion constraints)
→ review the resulting composition and cost
→ save as the recipient's current ration
```

On the industry pole this loop is the center of gravity: formulators maintain large recipe portfolios, refresh ingredient matrices from sample data, and re-optimize continuously as markets move, simulating scenarios before committing a change.

### Plan and execute feeding

```text
Schedule the ration over the feeding day
→ expand each feeding into batch/load quantities for the group's current count
→ execute: mix and deliver with guided, weighed instructions
→ record the load as mixed (actual quantities, deviations, leftovers)
```

In automated operations the execution step is performed by feeding machinery working from the same ration and group definitions; the software's role shifts to configuring, supervising and reconciling what the machines did.

### Track, cost, and adjust

```text
Actual usage posts against inventory (purchases, storage, mixes)
→ refusals/weighback and losses are picked up or written off
→ feed cost per group/animal/day and loss (shrink) become visible
→ rations, schedules or purchasing are adjusted accordingly
→ performance feedback (milk, growth) informs the next formulation round
```

This loop — formulate, feed, measure, adjust — is the interaction rhythm of the Type. The economics are inseparable from the nutrition: feed is typically the largest recurring cost in animal production, and the software exists precisely to make that cost visible and manageable while keeping animals fed to target.

## Interfaces

Described conceptually; exact layouts vary by product.

### Ration / recipe editor

The formulation workbench.

- typical information: the recipient's nutrient targets, the ingredient mix under composition, computed nutrient levels, cost of the mix, constraint status
- primary actions: add or remove ingredients, set inclusion limits, optimize or manually balance, save or revise the ration, simulate alternatives

### Ingredient / matrix maintenance

The composition substrate.

- typical information: feed items with their nutrient values and prices, sample-analysis updates, price history
- primary actions: add or edit items, update composition and prices, import analysis data

### Feeding schedule / load planner

The bridge between ration and execution.

- typical information: groups and their assigned rations over the feeding day, load quantities per feeding, expected versus scheduled
- primary actions: assign rations to groups, adjust schedules, scale loads to current counts, hand the plan to the mixing surface

### Guided mixing screen (mobile)

The in-barn execution surface, operated while standing at the mixer.

- typical information: the current load's ingredients in order with target weights, live scale readings, progress through the load
- primary actions: step through ingredients, confirm weighed amounts, complete and record the load, note leftovers or deviations

### Inventory view

The supply picture.

- typical information: on-hand quantities per feed item and storage location, incoming purchases, consumption to date, shrink and loss
- primary actions: record purchases and adjustments, review usage, investigate loss

### Analysis and reports

The management surface where cost and nutrition meet.

- typical information: feed cost per group/animal/day, planned versus actual feeding, loss analysis, ration composition against targets, performance correlations where performance data is integrated
- primary actions: run comparisons, drill into a group or load, export or share for consultants and advisors

### Settings

Recipients and groups, feeding times, storage locations, equipment and scale connections, users and roles (in operations large enough to matter).

## Important Rules / Behaviors

### The ration is versioned and recipient-bound

A ration always belongs to a recipient and changes over time. A revision affects future feedings; already-executed loads keep their recorded quantities. Some products treat ration changes as a formal transition with an effective date; at minimum, history is retained so past feeding can be reconstructed.

### Loads are scaled to the group

Load quantities are computed from the ration × the group's current animal count. When counts come from an integrated herd system, the load plan stays aligned with reality; when counts are maintained manually, keeping them current is the feeder's responsibility and stale counts surface as over- or under-feeding.

### Actual versus planned is the loss signal

The loop deliberately records what was actually mixed, delivered, refused and picked back up, not just what was planned. The gap between the two is how the operation sees shrink and mixing error — many products treat making this gap visible as their core management value.

### Composition data drives everything downstream

Ingredient composition and prices are upstream facts: when they change, computed ration values, costs and sometimes optimal mixes change with them. Mature products keep composition data deliberately current (some feed it from sample analysis) precisely because stale matrices quietly falsify every downstream number.

### Formulation is constrained

Whether a ration is hand-built or optimized, it lives under constraints: nutrient targets to meet, inclusion limits and ratios to respect, and (on the industry side) legal and labeling requirements that bound what a recipe may contain. An "optimal" mix that violates a constraint is not a valid ration.

### Connectivity is assumed intermittent on farms

Feeding happens in the barn, not at a desk. Products built for on-farm use keep execution usable without reliable connectivity and reconcile records when the device reconnects; the recorded load is the source of truth, not the moment of syncing.

## Variants

The Type is realized at two poles of one supply chain, with a spread of forms between:

- **on-farm feeding management** — the operation mixes its own feed: rations per pen/group, schedules, guided mixing with scales, shrink tracking; strongest in dairy and feedlot settings, present across swine and poultry
- **automated-feeding operations** — feeding executed by machinery from the same ration and group definitions; the software configures and supervises rather than guides a person, and consumption reconciliation is continuous
- **feed-industry formulation and recipe management** — mills, premix and specialty feed producers: large recipe portfolios, ingredient matrices refreshed from lab data, least-cost re-optimization against markets, production and compliance documentation; the "recipient" is often a manufactured feed product
- **minimal desktop formulation** — a single formulator computing least-cost rations and batch sheets without inventory or execution recording; the Type's lower bound, above which "management" begins
- **consultancy mode** — a nutritionist maintaining ration programs across many client farms from one login, with reports flowing back per client

A variant remains a variant unless it changes the core: a system that manages crops rather than fed rations, tracks animals rather than feed, or formulates saleable food products without a feeding loop has crossed into a different Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Dairy Farm Management / Livestock Management | the individually identified animal is the unit of record there (lactation, reproduction, health); feeding appears as a layer or event. Here the ration and feed supply are the record; animals appear as groups being fed |
| Aquaculture Management | feeding there is an execution/recording activity inside the rearing loop; the formulation and feed-supply discipline owned by this Type sits outside it |
| Farm Management Platform | crop-centric: grows the feed and manages harvests as commodities. This Type consumes feed into animals and manages it as ration components with nutrition semantics |
| Food Formulation Platform | shares the recipe/nutrient-matrix machinery, but binds recipes to saleable products, not to animal groups and a daily feeding/consumption loop; pet-food formulation is the adjacent instance |
| Grain Management / Grain Elevator Management | grain as stored/traded commodity; here grain appears only as a ration ingredient with a nutritional role |
| Feed-mill ERP / business systems | contracts, logistics and production business layer around feed manufacturing; the formulation core belongs to this Type where the two stand apart |

The most consequential boundary is with herd/livestock management, because the two interlock daily: the herd system supplies group counts and performance data, the feed system supplies what was fed. Products exist at every depth of embedding a feeding layer into a herd system; what keeps this a separate Type is that the ration, the feed supply and the feeding loop form a discipline of their own, with specialists (nutritionists, feed managers) whose daily work lives here, not in the animal record.

## Representative Products

- VAS FeedComp — on-farm dairy feeding management (ration entry, guided mixing, usage/shrink tracking, herd integration)
- BESTMIX (Adifo Software) — feed-industry formulation, recipe management and quality/ERP suite for mills and feed producers
- WinFeed — minimal desktop least-cost formulation tool
- Lely Vector with its farm-management layer — automated feeding (robot + feed kitchen) with ration-per-group management embedded in the feeding system

## Sources

Research date: **2026-09-08**

- VAS (FeedComp) — https://vas.com/ , https://vas.com/feedcomp/ — fetched 2026-09-08
- BESTMIX / Adifo Software — https://www.adifo.com/en/ , https://www.adifo.com/en/products/bestmix-recipe-management-feed — fetched 2026-09-08
- WinFeed — http://www.winfeed.com/ — fetched 2026-09-08
- Lely — https://www.lely.com/en/innovation/automatic-feeding/ , https://www.lely.com/solutions/feeding/vector/ — fetched 2026-09-08

> Sourcing limitation: one further well-known on-farm ration/feeding product could not be reached from the research environment, and a major nutrition-services platform's domain returned no product documentation. Claims in this document are therefore kept at cross-product strength; precise operational figures (optimization parameters, accuracy claims, limits) are deliberately omitted. Product-by-product observations are recorded in the paired Research Notes.
