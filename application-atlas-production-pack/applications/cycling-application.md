# Cycling Application

## Overview

A **Cycling Application** is an end-user application whose world is organized around the bicycle ride. It gives an individual cyclist a persistent record of the rides they actually did — or plans to do — carrying cycling-specific performance data, and builds the surrounding experience on that record: maps and tracks, bike-aware route planning and navigation, device connectivity, gear management, analysis, and, in many products, a social or training layer on top.

The defining structure is deliberately small:

```text
Ride (the unit of record)
└── cycling-specific performance semantics
    └── originating from the rider's own riding
```

Everything else commonly associated with cycling software — GPS track display, route planners, turn-by-turn navigation, bike computers, FTP and power analysis, segments and leaderboards, virtual indoor worlds, social feeds — is widespread in current products but is not part of what makes the application a Cycling Application. A manual ride log without GPS, a navigation-first route planner, and an indoor virtual-training product all satisfy the same core.

When the ride record stops being the unit of record — because the product is really a device hub, a coach's plan, an event organizer, or a general social feed — it has drifted toward a different Application Type.

## Users & Context

The primary user is an individual who rides a bicycle: commuters, road cyclists, mountain bikers, gravel riders, e-bike riders, racers, and casual weekend riders. The application is personal — one cyclist's rides, bikes, routes, and progress — and is used across the whole arc of riding:

- **before a ride** — plan or choose a route, check surfaces, elevation, and conditions
- **during a ride** — record the ride, follow navigation, see live metrics, occasionally take photos or hear audio cues
- **after a ride** — review the ride in detail, accumulate statistics, maintain gear mileage, share, compare, and train

Secondary usage is organizational rather than separate-user-based in most products: settings (units, privacy, connected devices) and optional premium subscriptions. Some products extend to club or group contexts, where rides and routes are shared among riding partners.

Typical surfaces are the smartphone first (recording and navigation happen on the handlebar or in a pocket), a website for planning and deep analysis, and a family of connected devices — bike computers, smartwatches, power meters, smart trainers, e-bike systems.

## Core Model

### The Defining Core

**Ride (activity/tour/session).** The central object: one cycling session, dated, belonging to the individual cyclist, and labeled with a cycling sport identity (road ride, mountain bike ride, gravel ride, e-bike ride, virtual/indoor ride). The ride persists — it accumulates into a personal history that can be revisited, edited, and analyzed.

**Cycling-specific performance semantics.** A ride is not an opaque blob; it carries metrics that mean something for cycling — distance, duration, speed, elevation gain as the baseline set, and richer sensor data (heart rate, cadence, power) where devices provide it. The bike context is intrinsic to what the numbers mean: products distinguish bike types (including e-bike), and some estimate effort or duration against the type of bike being ridden.

**Origin in the rider's own riding.** The record represents riding the user actually did or will do. Mature products accept the same ride through several entry paths — live recording in the app, sync from a GPS device or third-party app, import of a ride file, manual entry, or generation indoors from trainer data. The mechanism varies; the first-person provenance does not.

### What Mature Products Add

Mature cycling applications commonly carry most of the following. They make the application practical without defining it:

- **GPS track and map** — the ride is drawn on a map; maps offer layers, and rides accumulate into personal heatmaps or yearly recaps in some products.
- **Route planning** — the rider builds routes by placing start, destination, and intermediate waypoints; the planner routes according to the chosen cycling sport (favoring paved roads for road cycling, trails for mountain biking), offers round trips and reversed directions, and surfaces elevation profile, surfaces, way types, estimated duration and difficulty, sometimes weather and alerts along the way.
- **Navigation** — a saved route is followed during the ride, with turn cues, offline map support, and re-routing when the rider deviates.
- **Device connectivity** — pairing and syncing with bike computers, smartwatches, power meters, smart trainers, and e-bike systems; rides flow between device and application in both directions.
- **Gear and bike management** — bikes (and shoes, in multi-sport products) as named gear records with accumulated mileage; deeper products model individual bike components (wheels, chains, drivetrain parts) and retire them when replaced. Some products let a gear item be the default for a given sport type.
- **Analysis and progress** — ride-detail surfaces (metrics, splits, elevation, map) and longer-horizon progress: totals, trends, personal bests; power-meter products add threshold-based intensity, training load, power curves, and fitness modeling.
- **Social and community layer** — following other riders, a feed of activities, clubs or groups, challenges, and in some products competition on specific stretches of road or trail (segments with leaderboards).
- **Commerce** — a free base with subscription tiers or region unlocks; some models extend to hardware or recap products.

### One Structure, Many Implementations

```text
Concept:  Ride record
Realizations:  GPS-tracked outdoor ride · device-synced ride · imported ride file ·
               manually entered ride · indoor trainer session in a virtual world

Concept:  Cycling semantics
Realizations:  sport-type labels per bike style · bike-type-aware routing and duration estimates ·
               bike/gear records · e-bike distinctions

Concept:  Maps and routes
Realizations:  recorded-track maps · interactive route planner · turn-by-turn navigation ·
               community-contributed map content
```

A reader who has only met the social-activity-tracker style should still be able to recognize the navigation-first planner and the indoor virtual product as Cycling Applications from the defining core.

## How It Works

### Record a ride

```text
Choose the sport type (road / MTB / gravel / e-bike / …)
→ start recording (or let a paired device / trainer capture it)
→ ride; the application tracks position and metrics; live cues (navigation, audio) as configured
→ stop and save
→ the ride appears in the personal history, drawn on the map with its metrics
```

Alternative entry paths converge here: sync a device that recorded the ride, import a ride file, or enter a past ride manually. After saving, the ride can be edited — renamed, re-typed to a different sport, re-assigned to a different bike, or corrected.

### Plan and navigate a route

```text
Pick a cycling sport for the planner (routing follows the sport)
→ set start and destination; add or drag waypoints; switch one-way / round trip
→ review elevation profile, surfaces, way types, estimated duration and difficulty
→ save the route
→ during the ride, follow the saved route with turn-by-turn guidance, offline where needed
```

Route review is a first-class part of the loop: community photos along the route, points of interest (including e-bike charging in some products), and warnings for conditions along the way.

### Analyze, maintain, and share

```text
Open a ride → inspect map, metrics, elevation, effort
→ totals and trends accumulate into personal progress
→ the ride's mileage accrues to the assigned bike and components
→ optionally share to a feed, compare on leaderboards, or join clubs and challenges
```

For training-oriented riders, analysis extends into threshold-based intensity, training load, power curves, and fitness/fatigue modeling — the ride record remains the base on which all of it is computed.

### Ride indoors

```text
Pair a smart trainer (or ride a smart bike)
→ pedal; the trainer's power/speed/cadence data drives movement in a virtual environment
→ the session saves as a ride like any other
→ join group rides, events, and races with other riders in the same virtual world
```

The indoor variant keeps the ride as the unit of record; what changes is that routes and maps become virtual courses and provenance comes from trainer sensors rather than GPS.

## Interfaces

### Record / ride screen

The live surface used while riding.

- current metrics (speed, distance, time, elevation; sensor data when paired), map position, record/pause controls
- primary actions: start/stop recording, lock screen, take a photo, hear audio cues, follow navigation

### Map and route planner

A full-screen map working surface, usually on web and mobile.

- map with layers, searchable places, community highlights and points of interest, elevation profile with distance/duration/difficulty estimates
- primary actions: add/move/reorder waypoints, switch sport and route preferences, reverse or round-trip the route, save, export

### Ride detail

The post-ride surface for one ride.

- map of the track, metric summary, elevation profile, per-section detail, gear used, visibility and edit controls
- primary actions: edit ride, change gear assignment, analyze sections, share, delete

### History and progress

The personal archive of rides.

- chronological list or calendar, totals, trends, personal bests, goals; in training-oriented products, load and fitness curves
- primary actions: filter, search, open a ride, review progress over time

### Gear / bikes

The equipment inventory.

- bikes and other gear with accumulated mileage, components with replacement state, default gear per sport type
- primary actions: add/edit/retire gear, add components, assign to activities

### Feed / community

The shared surface, where present.

- rides from followed riders and clubs, kudos/comments, group events, challenges, leaderboards on segments
- primary actions: react, comment, join, filter, configure visibility

### Devices and settings

- pairing screens for sensors and devices, units and privacy configuration, subscription/region management

## Important Rules / Behaviors

### Sport type governs interpretation

The cycling sport label of a ride (and of a planned route) determines how the system treats it: which metrics are emphasized, how routes are routed, how duration and difficulty are estimated. Changing the sport type after the fact is a normal, supported operation.

### Every product offers several ways in, one canonical record

Recording live, syncing a device, importing a file, entering manually, and riding indoors all end in the same place: one persisted ride record. Editing after the fact is expected — rides are corrected, re-typed, and re-assigned without losing their identity.

### Privacy is structural

Rides reveal where a person lives, rides, and when. Visibility of rides (and even of ride start times or gear) is a configurable surface in mature products, not an afterthought. Products that push rides to social feeds carry additional privacy weight.

### Equipment mileage is derived, not typed

Gear mileage accumulates from the rides assigned to that gear. Riders cannot simply type a total; historical mileage is brought in by assigning (possibly manual) rides to the gear item. Components retire in ways that preserve or restructure the bike record depending on the product.

### Physical conditions are estimates and warnings, not guarantees

Route surface types, elevation, estimated durations, and difficulty reflect map data and models; planners explicitly treat them as preferences and estimates. Real-world conditions can diverge — which is why route alerts, user-reported conditions, and re-routing during navigation exist.

### Offline is a first-class case

Riding happens where connectivity is poor. Navigation on saved routes and map display commonly work offline, with maps or regions prepared in advance; sync resumes when connectivity returns.

## Variants

- **Social-activity tracker** — the ride feeds a community: follow graph, activity feed, kudos, clubs, and competition on segments with leaderboards; analysis and training analytics often strong.
- **Navigation / route-first** — the planner and guided navigation are the center; recording exists to log what was ridden; the community contributes to the map (highlights, photos, conditions) more than it competes.
- **Indoor virtual riding** — the trainer-driven virtual world is the product; racing, events, and structured riding; no real-world routes at all.
- **Training-science oriented** — threshold, load, and plan-driven structure dominate; often pairs with coaches or training platforms.
- **Device-ecosystem companion** — the application organizes around a vendor's devices (bike computers, watches, trainers); rides sync in from hardware as the primary entry path.
- **Club / event oriented** — routes and rides organized around groups, scheduled events, and cue-sheet-style planning.

A variant remains a variant as long as the ride record with cycling semantics stays the unit of work. A product that drops the ride record entirely (route browsing only), the cycling semantics (generic workouts), or the rider's own perspective (organizer-side) has crossed into a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Running Application | sibling (same directory family) | same record→analyze→share skeleton, running semantics: pace/cadence/stride, shoes instead of bikes; joint review recommended when that leaf is processed |
| Workout Tracking Application | adjacent | generic workout records without cycling semantics — no bike context, no bike-type routing, no elevation-for-cycling model |
| Endurance Training Platform | adjacent | plan- and coach-centric structured training across sports; the ride is training input, not the unit of record |
| Wearable Fitness Platform | adjacent | device/wearable is the hub organizing all activity data; a cycling app is ride-centric even when it pairs devices |
| Hiking / Trail Application | adjacent | trail discovery and outdoor navigation for many activities; no ride-record loop or cycling metrics |
| Outdoor Recreation Discovery | adjacent | finding places and routes without the record-ride/analyze-ride loop; pure route browsing is not a Cycling Application |
| Race Management Platform | adjacent, organizer-side | event operations for organizers; a cycling app's event features are rider-side conveniences |
| Social Network | drift risk | when feed and profile become primary and rides degenerate into shareable content; the test is whether the ride with analysis attached remains the unit of record |

The two most important seams: against **Running Application** (deliberate sport-specific siblings — the boundary is the sport data model, not the workflow) and against **Workout Tracking Application** (the presence of cycling semantics — bike context, bike-type distinctions, cycling routing — is exactly what the generic tracker lacks).

## Representative Products

- **Strava** — social-activity-tracker pole; cycling among core sports; strong analysis and gear model
- **Komoot** — navigation/route-first pole; sport-specific routing; community map contribution
- **Zwift** — indoor virtual-riding pole; trainer-driven sessions in a virtual world with racing and events

The defining core was checked against the indoor pole and against manual-entry rides to avoid overfitting to the modern GPS social-tracker pattern.

## Sources

Research date: **2026-09-07**

- Strava Help Center — https://support.strava.com/hc/en-us (Supported Sport Types; Adding Gear to Your Activities; Strava Training Glossary for Cycling; help-center collections on recording/uploading, maps, stats, and community)
- Komoot Help Center — https://support.komoot.com/hc/en-us (Supported sport types; Plan routes on the website; "Using komoot" sections: Get Started, komoot Map, Planning and Routes, Navigation and Recording, Community and Contributions; Connected Devices and Integrations category)
- Zwift — https://www.zwift.com/how-it-works (equipment, devices, membership, racing/events)

> Sourcing limitations: Ride with GPS and Garmin Connect documentation could not be fetched from the research environment and were excluded; the sample therefore omits the club/event route-planning pole and the device-ecosystem pole as directly documented cases. Zwift's support-site articles were not extractable, so its claims rest on the product page and are kept correspondingly modest. Precise numeric details (training-zone definitions, recovery-band values, region pricing, leaderboard rules) observed during research are intentionally not stated in this document and remain in the paired Research Notes.
