# Grain Management

## Overview

A Grain Management application protects grain after it has been placed in storage. It continuously measures the physical condition of the grain mass inside identified storage units (bins, silos), watches that condition against safe-storage limits, and drives the storage's conditioning equipment — aeration fans and heat — to bring the grain to and hold it at a target temperature and moisture until it goes to market.

The problem it solves is storage loss: grain in a bin is a living, perishable mass. Temperature and moisture gradients inside a bin lead to hot spots, condensation, mold, insect activity and shrink (weight and grade loss), often invisibly until the damage is done. A Grain Management application replaces the old routine — climbing the bin, dropping a probe, consulting a chart, switching fans by hand at night — with continuous sensing, automatic alerting, and fan control that responds to real conditions in and around the grain.

Its boundary: it manages the **condition** of stored grain, not the **commerce** of grain. It does not weigh deliveries, write contracts, settle with growers, or track whose bushels are in which bin — that is the territory of grain-elevator management systems. It also does not manage the crop in the field — that is farm and crop management territory.

## Users & Context

Primary users:

- **Grain producer / farm operator** — stores part of the harvest on-farm in bins; uses the system to keep grain safe between harvest and sale, protect grade, avoid shrink, and in some markets deliberately rehydrate grain to target moisture before delivery.
- **Commercial storage / facility operator** — runs larger storage footprints (elevator storage annexes, silo plants, commercial bins); uses the system to coordinate conditioning across many bins and sites and to defend large volumes against large-scale spoilage.

Secondary users:

- **Dealer / installer** — typically creates the site in the platform, installs sensor cables, associates devices with bins, and trains the customer; ongoing service relationship is common.
- **Farm staff / seasonal workers** — respond to alerts; some products offer a simple handheld reader for on-site checks.

The work context is seasonal and round-the-clock: harvest fills bins quickly, grain then sits for months across changing weather, and the moments that matter (a rising hot spot, a warm front causing condensation) happen without anyone watching. This is why remote access, alerting, and automation are central to the product experience rather than conveniences.

## Core Model

The system's world has three joined parts: what it senses, what it watches for, and what it does.

```text
Storage unit (bin / silo)
└── Sensor points in the grain mass (temperature, moisture)
    └── Condition readings over time, bound to the bin
        └── Out-of-condition watch (safe-storage limits → alerts)
            └── Conditioning response (aeration fans, heat)
                └── Target condition reached and held
```

### The defining core

Three structures together make the application what it is:

- **Sensed grain condition in identified storage.** The managed subject is the grain itself, not the building. Temperature and moisture are measured at points inside the grain mass — most commonly by sensor cables hung from the bin roof and anchored to the floor, at multiple depths and zones — and every reading is bound to an identified bin. The purpose of the sensing is early spoilage detection. Ambient conditions (outside air, weather, air at the fan) are sensed as well, because they determine what conditioning can achieve.
- **The out-of-condition watch.** Readings are interpreted against safe-storage limits. When grain moves out of condition — a hot spot forming, moisture climbing, CO₂ rising, condensation risk building — the system notifies the user (text, email, in-app, audible alarms depending on product). This is what turns a sensor network into a management system: the user learns about the problem before it becomes a loss.
- **The conditioning response loop.** The system actuates — or directs the actuation of — the storage's aeration fans and heaters. The response scales across three realizations: the user switches fans remotely; the system runs fans automatically when conditions are favorable; the system autonomously works toward a defined target (cooling, drying, rehydrating, or holding condition) using ambient-air science that decides whether the outside air will improve or harm the grain before running the fans at all.

Remove any one and the application stops being recognizable: without sensing, fan automation is blind; without the watch, it is a readout, not a manager; without the response loop, it is passive monitoring and the human still does all the management.

### Standard capabilities of mature products

Mature products typically add, beyond the core:

- **Ambient/environment layer** — weather station data or ambient temperature/relative-humidity sensing at the fan, feeding conditioning decisions.
- **CO₂ sensing** — elevated CO₂ as an early chemical warning of spoilage before temperature spikes are visible.
- **Physical fill-level sensing** — how full each bin is, sometimes with approximate volume estimation; strictly a sensor reading of grain height, not commercial inventory.
- **Historical trends** — per-bin charts of temperature and moisture over the storage season.
- **3D visualization** — a spatial view of the bin/silo interior showing sensor positions and where a problem sits in the grain.
- **Estate views** — every bin, and often multiple sites or facilities, on one dashboard; mobile apps and web dashboards sharing the same data.
- **Configurable alerts** — per-bin thresholds the user can tune.
- **Manual override** — automation can always be overridden by hand.
- **Ecosystem compatibility** — systems commonly read existing third-party sensor cables, so a monitoring upgrade does not force rewiring the bin.

### Concept vs implementation

The concepts above are realized differently across products, and a reader familiar with only one product should still recognize the others:

```text
Concept: sensor in the grain        → cables (fixed, hung from roof), moveable wireless spears, handheld probe readers
Concept: conditioning response      → remote on/off switch, threshold automation, target-driven strategies
Concept: out-of-condition watch     → threshold alerts, hot-spot detection, CO₂ alarms, condensation-risk logic
Concept: storage structure          → site → yard → bin → cable → depth; facility → silo → sensor
```

## How It Works

### Put the site on the map

A storage site is configured in the platform: the bins are named and grouped (often by yard or site, with grain type recorded), sensor cables are installed and associated with specific bins, and conditioning equipment (fans, heaters) is connected through control modules or relays. This is commonly done by the dealer during installation, and it is what later lets the system say not just "something is wrong" but "where to look."

### Watch the grain

Once running, the system reads the in-grain sensors continuously or on a short cycle (hourly in several products; daily on simpler tiers), together with ambient air and weather. The user's standing view is a dashboard: each bin with its current temperature and moisture, alarm state, and fan state. Drilling into a bin shows the reading profile by depth or zone — the shape of the grain's condition, where hot spots and moisture fronts form — sometimes rendered as a 3D view of the bin interior. Historical charts show how each bin has trended since harvest.

### Respond when grain moves out of condition

When a bin crosses a threshold, the system notifies the user. From there the response can be:

- **Manual and remote** — turn the fan on or off from the app or dashboard (no more driving to the bin at night).
- **Automated by rules** — the system runs fans when outside conditions are favorable: cool air for cooling, dry air for drying, humid air for rehydrating.
- **Automated toward a target** — the user sets what the grain should end up as (cooled for summer holding, dried to target moisture, rehydrated up to target moisture, or held at condition), and the system works the fans — and sometimes heaters — toward that target using equilibrium-moisture logic: it runs the fans only when the outside air will actually improve or maintain the grain's condition, and stops them when it would harm it.

The loop then closes: conditioning changes the grain, the sensors see the change, and the bin returns to — or holds at — target condition.

### The harvest-to-market arc

Across a season the workflow reads: fill bins at harvest → dry or cool grain down to safe condition → hold through winter (cooling cycles as ambient temperatures drop) → manage the spring warm-up carefully so condensation does not form, keeping grain temperature near ambient → optionally rehydrate to target moisture before delivery → empty the bin to market. The application's job is to make every step of that arc observable and automatic where possible, because quality and weight carried into the market are the storage's profit.

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Web dashboard

The main working surface. Purpose: see and operate the whole storage estate. Typical information: bin list with current condition, alarm and fan states; site/facility grouping; current ambient/weather data. Primary actions: open a bin, acknowledge alerts, switch fans, adjust settings.

### Bin detail view

The single-bin surface. Purpose: understand one bin's internal state. Typical information: temperature and moisture readings by depth/zone (often with a 3D bin visualization), sensor-cable layout, fan status, trend charts since harvest. Primary actions: read cables, interpret hot spots, control that bin's fans, set or change its conditioning target.

### Mobile app

Remote access surface, usually mirroring the dashboard: current conditions, alerts as push notifications, remote fan switching. Primary actions: check status from anywhere, respond to alerts, toggle fans.

### Alerting channels

Text message, email, in-app and sometimes audible alarms, configured per bin and per threshold. Purpose: bring the out-of-condition bin to the user's attention without the user watching.

### Handheld reader (common variant surface)

A pocket device or phone-based reader that plugs into bin cables on site and shows the readings directly — the digitized form of the old probe. Purpose: on-site spot checks independent of the network; simplest entry into the product family.

### Settings / strategy configuration

Where conditioning behavior is defined: target moisture, cooling or rehydration strategies, thresholds for alerts, fan run parameters, manual-vs-automatic mode per bin.

## Important Rules / Behaviors

- **The outside air is the tool, and it is not always safe to use.** Conditioning works by moving outside air through the grain. Fans must run only when that air will improve or maintain condition — drying air that is too humid does nothing, air that is too dry over-dries (shrink = lost weight = lost money), and warm air on cold grain causes condensation. This is the central rule the automation encodes, and mature products document it explicitly (equilibrium-moisture-based fan control).
- **Over-drying is a cost; rehydration is a deliberate strategy.** Systems aim at target moisture, not minimum moisture. In some products the user can set the system to add moisture deliberately (pulling humid air into the bin) — weight recovered is revenue.
- **Summer holding has its own rule.** As outside temperature rises, grain held into warm months must be warmed slowly and kept near ambient temperature, or condensation forms on the grain. Several products automate this "maintain" behavior.
- **Automation never removes the override.** All sampled products document manual control of fans regardless of automation tier.
- **Spoilage announces itself chemically before it announces itself thermally.** Where CO₂ sensing is present, it is positioned as the early warning — elevated CO₂ signals mold/insect respiration before a hot spot is big enough to read on a cable.
- **Fill-level readings are estimates, not weights.** Where offered, volume/level sensing gives an approximate picture of how much grain is in a bin; it does not replace weighing, and products are explicit that it is not precise.
- **Location is part of the alarm.** Because sensors are bound to specific bins and depths, an alert points at where to look — the reason site configuration (which cable belongs to which bin) matters at installation.

## Variants

- **Monitoring-only entry tiers** — products in this family are commonly sold in ascending tiers: handheld reader → daily wireless readings → hourly readings with remote fan control → full automation. A monitoring-only configuration sits below the full Type: it watches but does not act, one upgrade step away from complete management.
- **Farm scale vs commercial/industrial scale** — on-farm bin sites (simple installs, cellular connectivity, battery/solar power) vs commercial silo plants and multi-site estates (facility-wide dashboards, coordinated conditioning, integration hooks).
- **Independent specialist vs bin-manufacturer-attached** — the Type exists both as standalone systems that work with any bin and third-party cables, and as a storage-equipment maker's own software layer sold alongside its bins.
- **Strategy-mode vs single-parameter automation** — some products expose named conditioning strategies (dry / cool / rehydrate / maintain) the user picks per bin; others compress the decision into one parameter (equilibrium moisture content, with per-crop calibration) the system applies.
- **Regional flavor** — North American farm pole and European industrial-silo pole realize the same core with different channel structures and hardware conventions; nothing in the core is region-specific.
- **Companion hardware lines** — handheld moisture meters/analyzers and moveable sensor spears often ship from the same vendors as adjacent products for field and spot checks.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Grain Elevator Management | adjacent sibling | manages grain commerce at a facility: weighed ticketed movements, contracts, settlement and payment to growers, bushels as commercial inventory; Grain Management manages grain's physical condition in storage. Fill-level sensing is the shared boundary object — a sensor reading here, commercial position there |
| Grain Origination Platform | adjacent sibling | the grower-acquisition and contracting front end (offers, contracts, cash bids); carries no storage-condition machinery |
| Farm Management Platform | broader, adjacent | the whole-operation record: fields, crop seasons, inputs, machinery; grain in storage appears at most as a hand-off point, without condition sensing or conditioning control |
| Crop Management / Precision Agriculture | upstream | manage the crop before harvest; this Type begins when the crop is in the bin |
| Agricultural IoT Platform | substrate | a sensing backbone without the protective mission (condition watch + conditioning response) is sensor plumbing; monitoring-only tiers of this Type sit on that seam |
| Building Management System | structural analogy only | same sense → alarm → actuate loop, but the subject is building climate, not stored grain |

The most consequential boundary is with Grain Elevator Management, because both are found at the same facility. The dividing line: elevator systems answer *whose grain, how much was delivered, what is owed*; Grain Management answers *what condition is the grain in, and what must the fans do about it*. In practice the two can coexist at one operation — the commerce system records the bushels, the management system keeps them sound.

## Representative Products

- OPI Systems (BLUE Lite / EPIQ / BLUE, ManageGrain.com) — independent full-automation specialist, grower to commercial
- Bin-Sense (Direct / Solo / Live / Plus) — wireless-first family, handheld to automatic conditioning
- AgroLog (TMS systems, AgroLog Manager, aeration control) — European industrial silo monitoring
- GSI GrainVue — bin manufacturer's own grain-management layer with strategy-based automation

## Sources

Research date: **2026-09-08**

Official product pages (all fetched directly):

- OPI Systems — homepage; "Grain Management"; "OPI BLUE Smart Conditioning" — https://opisystems.com , https://opisystems.com/grain-management/ , https://opisystems.com/opi-blue-full-automation/
- Bin-Sense — homepage; Products & FAQ — https://www.binsense.com , https://www.binsense.com/products/
- AgroLog — homepage; AgroLog Manager software; Aeration Control — https://www.agrolog.com/ , https://www.agrolog.com/agrolog-software , https://www.agrolog.com/aeration-control
- GSI — GrainVue product page; Grain Management category — https://www.grainsystems.com/na/en/products/grain-management/grainvue/ , https://www.grainsystems.com/na/en/products/grain-management/

> Sourcing limitation: vendor help centers, manuals and deep support documentation were not reachable/retrieved in this research pass. Assertions in this document are calibrated to official product-page evidence; precise operational figures (sensor spacing, refresh intervals, threshold defaults, pricing) are intentionally not stated. Vendor-published numbers (e.g., marketing statistics and worked pricing examples) remain in the Research Notes.

Detailed evidence, cross-product comparison, and the boundary analysis against Grain Elevator Management and Grain Origination Platform are recorded in the paired Research Notes.
