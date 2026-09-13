# Ski Resort Recreation Application

## Overview

A **Ski Resort Recreation Application** is the guest-facing companion for a day of skiing or snowboarding at a mountain resort. It holds the resort's mountain as a navigable space, keeps the guest current on that mountain's live operating state, and organizes the experience around the guest's own day — where they are on the mountain, what they have skied, and what entitles them to be there.

The defining structure is small:

```text
The mountain as structured guest-facing space
    (trail map: named, difficulty-graded runs connected by lifts,
     on-mountain points — lodges, restaurants, facilities, patrol)
The mountain's live operating state
    (lift/trail open-closed status, grooming, snow and weather
     conditions, webcams, operational alerts)
The guest's mountain day as the personal frame
    (position on the mountain, tracked activity, pass/ticket
     entitlement, companions)
```

Everything else the market associates with these apps — automatic run tracking, friend location, leaderboards, mobile passes, on-mountain payments, booking, parking — is widespread in current products but is not what makes the product this Type. A resort app that only publishes the trail map, lift status, and snow report is the resort's information surface; a phone app that only records ski runs is an activity tracker. This Type begins where the mountain's space, the mountain's state, and the guest's own day are held together.

## Users & Context

The primary user is a guest — a skier or snowboarder — spending a day (or several days) at a resort. Three recurring situations shape usage:

- **Before the day**: checking conditions (snowfall, weather, webcams, which lifts are running), deciding where to go, and sorting out access (a lift ticket or season pass, parking, transit).
- **During the day**: navigating the mountain (which run is open, where am I, where are my friends), riding lifts, and staying safe (patrol access, warnings).
- **After the day**: reviewing what they skied — runs, vertical, top speed — and comparing it with friends or with their own season so far.

Secondary users and postures:

- **Season passholders and local regulars**, for whom the app is a standing utility: conditions each morning, entitlement and blackout rules, and a season-long record.
- **Destination visitors and families**, for whom the app is a trip tool: booking tickets and lessons, finding dining and rentals, meeting up on the mountain.
- **Resort and pass operators** are not users of the application but its publishers or data suppliers: the operating state the guest sees is produced by the resort's operations, and the app consumes it.

The dominant device is the phone in a jacket pocket, used in short glances between runs, often with poor reception and cold-drained batteries — a constraint that visibly shapes the product (offline maps, battery-conscious recording, glanceable stats).

## Core Model

### The Defining Core

**1. The mountain as structured guest-facing space.** The resort's terrain is held as a model the guest can navigate: named runs and trails, graded by difficulty; lifts that connect them; and on-mountain points of reference — lodges, restaurants, rental shops, restrooms, ski-patrol locations, terrain parks. The trail map is this model's surface. Without the mountain as a structured space, the product is a weather feed or a generic map.

**2. The mountain's live operating state.** The space is not static: lifts and runs open and close through the day, grooming changes the surface, snow and weather move, and the resort posts operational alerts. The application carries this state — lift and trail status, grooming and snow reports, weather, webcams, warnings — as the day's ground truth. The app reflects the resort's operational decisions; it does not make them. Without the live state, the product is a static trail map.

**3. The guest's mountain day as the personal frame.** The application is organized around the individual guest's own day. This frame is realized through personal surfaces — where the guest is on the mountain, what they have skied (tracked runs, vertical, speed), what entitles them to be there (a pass or ticket, with its access rules), and who they are with. Different products realize different subsets; a product with none of these is a publication rather than a guest application. Without the personal frame, the product is the resort's information surface.

### Capabilities Shared by Mature Products

These are common in current products and expected by guests, but they are additions to the core rather than the definition:

- **Activity tracking** — the day recorded automatically as runs and lifts: number of runs, vertical distance, distance, top and average speed, time on lifts versus time on runs. The strongest products segment the day automatically (detecting lifts and runs from GPS movement) and let the guest inspect and correct the timeline.
- **Season and lifetime totals** — the day record accumulates into a season-long and career-long personal history, with progression comparison.
- **Friends on the mountain** — seeing where companions are on the map, regrouping after separating, and comparing stats; sharing is consent-based and can be switched off.
- **Leaderboards and challenges** — private groups or public community rankings over stats such as vertical.
- **Webcams** — live views of the mountain as a conditions surface.
- **Pass and ticket in the app** — the guest's entitlement held and displayed: resort access, restricted or blackout dates, days remaining; in the resort-ecosystem products, the phone itself becomes the pass, scanned at the lift, and lift tickets can be purchased in-app.
- **On-mountain commerce and booking** — paying for food on the mountain, buying passes and tickets, booking lessons, rentals, and dining.
- **Safety surfaces** — direct access to ski patrol carrying the guest's GPS location; operational warnings and avalanche-related notices.
- **Facility and service finder** — dining, restrooms, rentals, patrol locations, parking availability, resort transit.
- **Offline capability** — maps and recording that keep working without cell reception, a hard requirement in mountain terrain.

### One Structure, Many Implementations

The core is conceptual; products implement it differently:

```text
Concept:  The mountain as structured space
Realized as:  the resort's official interactive trail map;
              a pass ecosystem's maps across many resorts;
              a third party's licensed/curated resort maps;
              a live panorama map blended with the village map

Concept:  The mountain's live operating state
Realized as:  operator-published lift/trail status and grooming reports;
              third-party live status feeds for partner resorts;
              community condition reports from other skiers;
              webcams and weather as the always-available floor

Concept:  The guest's day as the personal frame
Realized as:  GPS tracking with automatic run/lift segmentation;
              a pass-linked stats profile and leaderboard standing;
              the mobile pass and its entitlement rules;
              the guest's position and companions on the map
```

A reader who has only seen one implementation — say, a resort's own pass app — should still be able to recognize a third-party tracker or a European destination app as the same Type from the core model.

## How It Works

The application's natural loop is the day itself:

### Before the day: conditions and access

```text
Open the app in the morning (or the evening before)
→ check the mountain's state: snow report, weather, webcams,
  which lifts and runs are open, grooming, alerts
→ sort out access: view the pass and its rules,
  or buy a lift ticket in the app
→ plan the day: parking or transit, meeting points,
  lessons or rentals if needed
```

### During the day: navigate, ride, stay safe

```text
Arrive at the resort
→ the pass is scanned at the lift (phone-based where supported,
  physical card otherwise)
→ on the trail map: see current position, open runs and lifts,
  on-mountain facilities, and where friends are
→ ride and ski; if tracking is on, the day records itself —
  lifts and runs segmented automatically
→ consult status as it changes through the day
  (wind holds, closures, fresh grooming)
→ if needed: reach ski patrol with GPS location,
  or heed posted warnings
```

### After the day: the record

```text
Stop recording (or let the day close itself)
→ review the day: runs skied, vertical, distance, top speed,
  time on lifts versus runs
→ compare: with friends' days, group leaderboards,
  or one's own season and previous seasons
→ keep: photos and the GPS trace as the day's memory
→ the totals accumulate into the season's history
```

The loop repeats across days and seasons; the record is the part that persists.

### Capability tiers

- **Defining core** — mountain space model; live operating state; the guest's personal day frame.
- **Standard in mature products** — tracking with automatic segmentation, season totals, friend location, leaderboards, webcams, pass-in-app, safety surfaces, facility finder, offline support.
- **Variant / optional** — mobile pass with hands-free lift scanning, on-mountain payments, booking depth, parking availability, predictive wait times, public community leaderboards, destination-tourism extensions beyond the ski day, AI assistant surfaces.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Trail map

The application's central surface.

- the mountain's runs (difficulty-graded), lifts, and on-mountain points
- the guest's current position; friends' positions where shared
- open/closed state of lifts and runs where carried
- primary actions: locate yourself, search a run or lift or facility, open a point of interest, start or view a recording

### Conditions / mountain state

The day's ground truth, usually the morning's first stop.

- snow report, weather forecast, webcams, lift and trail status, grooming, operational alerts
- primary actions: check a resort's or a lift's status, view a webcam, read alerts

### Recording / day screen

The live surface while tracking is on.

- current stats (vertical, runs, speed, time), the day's accumulating timeline of lifts and runs
- primary actions: start/stop recording, switch activity type, view live position, share location with friends

### Pass / wallet

The entitlement surface.

- the guest's pass or ticket, access rights, restricted or blackout dates, days remaining; purchase of tickets or passes where offered
- primary actions: view entitlement, buy a ticket, present or activate the mobile pass

### Stats / history

The record surface.

- day, season, and lifetime totals; per-run detail; comparisons and leaderboards
- primary actions: review a day, compare with friends, share a result

### Crew / friends

The social surface.

- friends on the mountain, groups for the day, message and meet-up affordances, location-sharing controls
- primary actions: invite or add friends, toggle location sharing, find a friend, compare stats

### Resort services & booking

The practical surface around the day.

- dining, rentals, ski school, events, parking, transit; ticket shop and reservations where offered
- primary actions: find a service, book or buy, navigate to a point

### Profile / settings

- identity, tracked history, privacy controls (location sharing, tracking), notification subscriptions (alerts, powder reports)

## Important Rules / Behaviors

### The operating state is the resort's, not the app's

Lift and trail status, grooming, and alerts are produced by the resort's operations and published into the app. The app can lag the mountain; a run shown open can close at any time. Guests treat the map's state as advisory ground truth, and mature products surface the time-sensitivity of what they show.

### Entitlement gates the day

What the guest may ride is governed by their pass or ticket — access rights, restricted or blackout dates, remaining days. The app surfaces these rules; where the phone is the pass, the app also mediates the access act itself (scan at the lift). A displayed pass is a claim the lift infrastructure verifies, not a guarantee the app can enforce.

### Tracking is GPS-bound and terrain-challenged

Recording depends on satellite positioning; it does not work indoors and degrades with reception, weather, and battery cold. This is why offline recording, battery guidance, and manual correction of the recorded timeline (removing lift-line time, fixing a mis-segmented run) are standard behaviors rather than niceties.

### Location sharing is consent-based

Showing a guest's position to friends is opt-in and reversible. The same location data that powers "find my friends" also powers safety use (patrol locating a guest); products treat these as distinct, consent-governed flows.

### The record is personal and cumulative

The day's trace and stats persist and accumulate into season and lifetime history. This persistence is what makes comparison, progression, and leaderboards meaningful — and it is why privacy posture (who sees your data, whether it is sold) is a visible product dimension.

### Third-party context is second-hand

A third-party app's maps, status, and conditions are acquired data layers rather than the operator's own publications; their freshness and coverage vary by resort. Resort-official apps carry their own state but only for their own (or their pass portfolio's) mountains.

## Variants

- **Single-resort official app** — one resort's guest app: its map, its status, its tickets, its services; often blended with the destination's wider life (village dining, events, transit, road conditions in the European form).
- **Pass-ecosystem app** — a multi-resort pass portfolio's app: entitlement across many mountains, consolidated status and stats, on-mountain payments and rewards; increasingly replaces the individual resorts' local apps.
- **Third-party cross-resort app** — independent of any resort: deep recording and stats across all mountains, with resort maps, status, and conditions carried as data layers; commonly free-core with a paid premium tier.
- **Pure tracker (boundary variant)** — recording and stats with no resort context at all; functionally an activity tracker specialized to snow sports (see Related Types).
- **Regional shapes** — European apps blend resort and destination (public-transport timetables, access-road conditions, table reservations, piste grading and warning culture); North American apps center pass ecosystems, lift wait times, and parking; coverage of Asia-Pacific resorts appears as data expansion in cross-resort products.
- **Beyond the ski day** — resort apps in the destination-tourism shape extend past the ski day into the resort's year-round life (village dining, events, spa and activity discovery, access transit), reusing the same map and services machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Hiking / Trail Application | sibling pattern, different domain | same map-navigation grammar, but summer trail context; no lifts, no snow/operating state, no ski-day record. Remove lifts and snow state from this Type and it becomes a trail app |
| Workout Tracking Application | boundary pole | a pure ski tracker holds the personal record without the mountain's space or operating state — activity-tracking territory specialized to snow sports |
| Snow-report / weather applications | boundary pole | conditions without the on-mountain day: planning-first surfaces for choosing a resort, not companions for the day at one |
| Outdoor Recreation Discovery | adjacent | finding and choosing destinations versus being the companion at the destination; trip-planning features sit on this seam |
| Theme Park / Attraction guest applications | same grammar, different industry | park map + live status/wait times + ticket in app; the ski Type's specificity is the mountain model (lifts, runs, snow) and the ski-day record |
| Attraction / Event Ticketing | capability, not core | ticket commerce appears here as a guest convenience; the ticketing Types center the sale and access control themselves |
| Hotel PMS / resort operator systems | opposite side | operator-facing management of lodging and operations; this Type is guest-facing experience and consumes the operator's published state |
| Amenity Booking Platform | capability, not core | booking lessons, rentals, dining is a surface inside this Type, not its defining loop |

The most important boundary is against the two poles: a product with only the personal record (no mountain space or state) is a tracker; a product with only space and state (no personal frame) is the resort's publication. This Type is the held-together middle.

## Representative Products

- **My Epic** (Vail Resorts) — the pass-ecosystem pole: mobile pass scanned hands-free at lifts, interactive trail maps with GPS location and lift wait times, personalized stats, patrol assistance, on-mountain payments and rewards across the operator's resort portfolio.
- **Ikon Pass** (Alterra Mountain Company) — the second pass ecosystem: pass management (days remaining, blackout dates, credits, family profiles), crew location and stats, interactive maps, in-app food payment and parking across 70+ stated destinations.
- **Slopes** (Breakpoint Studio) — the third-party tracker pole: automatic run/lift recording with an editable day timeline, interactive resort maps for thousands of resorts, community condition reports, friend location, private leaderboards; free core with a premium subscription, privacy-first posture.
- **Matterhorn app** (Zermatt – Matterhorn) — the regional single-resort pole: live lift/piste status and webcams, ticket shop, pass-linked stats and public leaderboard (Peak Track), blended with the destination's village life (dining, events, transit, road conditions).

The pure-tracker boundary pole was probed with Ski Tracks (recording lineage back to 2010, no resort context in its core form) and corroborated by other tracker products; the snow-report boundary pole was probed with OnTheSnow.

## Sources

Research date: **2026-09-09**

Official vendor surfaces used (all vendor-authored):

- My Epic (Vail Resorts) — App Store listing: https://apps.apple.com/us/app/my-epic-skiing-snowboarding/id395375487
- Ikon Pass (Alterra Mountain Company) — App Store listing: https://apps.apple.com/us/app/ikon-pass/id1482191120
- Slopes (Breakpoint Studio) — official site: https://getslopes.com/ ; App Store listing: https://apps.apple.com/us/app/slopes-ski-snowboard/id643351983
- Ski Tracks — App Store listing: https://apps.apple.com/us/app/ski-tracks/id365724094
- Matterhorn app (Zermatt – Matterhorn) — App Store listing (CH): https://apps.apple.com/ch/app/matterhorn/id1440571628 ; official page: https://zermatt.swiss/matterhorn-app
- Boundary anchors: OnTheSnow (https://apps.apple.com/us/app/onthesnow-ski-snow-report/id300412347), Ski Tracker & Snow Forecast (id1448220616), EXA Ski Tracker (id1196252184), Ski Tracks Lite & GPS Maps (id368024976)

> Sourcing limitation: vendor help centers and product sites were largely unreachable from the research environment on 2026-09-09 (epicmix.com bot-blocked on two attempts; ikonpass.com JavaScript-gated; slopesapp.com timed out; skitracks.app empty response). Vendor-authored App Store listings and the Slopes official site were used as the reachable official layer. Precise operational details (scan behavior specifics, refresh intervals, offline map coverage, pricing) are intentionally not asserted; vendor-stated figures (e.g., "2,000+ resorts", "70+ destinations") are quoted as vendor claims.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
