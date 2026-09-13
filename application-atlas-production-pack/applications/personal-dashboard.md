# Personal Dashboard

## Overview

A **Personal Dashboard** is a single, standing, at-a-glance surface that a person composes from multiple widgets, each surfacing a slice of their own life — tasks, events, metrics, habits, environment, or personally chosen information streams. The surface stays current automatically, so the person can orient at a glance and act lightly, while the records of record and the deeper work remain in the applications the dashboard mirrors, summarizes, or links to.

It solves a specific problem: a person's situation is scattered across many single-purpose places — the task app, the calendar, the fitness tracker, the weather service, the bookmark store. No one of those answers "what is my situation right now?" The personal dashboard is the one place assembled for exactly that question, revisited at the start of a day or a work session.

The defining core is deliberately small:

```text
The person's own life as the data substrate
└── Composed personal surface (one standing screen, user-assembled)
    └── Widget units (each surfacing one slice of the person's situation)
        └── At-a-glance currency (kept current, read in a glance, acted on lightly)
```

Everything commonly associated with the category — a particular widget set, third-party service connectors, the browser new tab, photo backgrounds and daily quotes, insights and correlations — is widespread in current products but is not what makes the product a personal dashboard. The 2000s widget-and-start-page era (personalized homepages, desktop widget engines, PDA today screens) satisfies the same core with none of those specifics.

## Users & Context

The user is an individual who wants a standing overview of their own situation. There is no second audience: the person who composes the surface is the person who reads it.

Typical contexts:

- **Start of the workday or work session** — open the dashboard (often literally the browser's new tab or the phone's home screen), read the day's shape: weather, today's events, today's tasks, one chosen focus.
- **Throughout the day, in passing** — glance between other activities: check a step count, a battery level, a headline, the next meeting.
- **Periodic self-review** — for aggregation-heavy products, look back over trends: how sleep, activity, mood, and output moved over weeks.

The work environment varies by delivery surface: a browser new tab for people who live in the browser, a phone's home or lock screen for people who live on mobile, a customized desktop for enthusiasts, a web page for people who want a start page they can reach from anywhere.

## Core Model

### The Defining Core

```text
The person's own life as the data substrate
└── Composed personal surface
    └── Widget units
        └── At-a-glance currency
```

Four properties. If any one is removed, the product is no longer recognizable as a personal dashboard:

- **The person's own life as the data substrate** — every unit surfaces a slice of the person's own situation: their tasks, their events, their metrics, their habits, their weather and location, or information streams they personally selected. The person is both the subject and the only audience. Without this, the product becomes a public portal, a kiosk display, or an organizational dashboard.
- **A composed personal surface** — one standing screen the person owns and returns to, assembled from multiple independent units. Without plurality, it is a single-purpose app; without the person's own composing hand (a vendor-fixed layout), it is a portal or a feed.
- **Widget units** — each unit is an independently added, removed, arranged, and configured panel that surfaces one kind of thing: a todo list, a forecast, a clock, a feed, a metric, a set of links. The widget is the unit of composition; the catalog is open-ended rather than a fixed list.
- **At-a-glance currency** — the surface is kept current (automatic refresh or sync) and built to be read in a glance and acted on lightly. Without currency, it is a static snapshot; without the glance posture — if records were created and managed here as the main activity — it would be a personal organizer rather than a dashboard.

### Standard Capabilities

Mature products commonly carry most of the following. They make the dashboard practical; they do not define the Type.

- **A widget catalog spanning life domains** — tasks and todos, calendar events, weather, clock and date, notes, links and bookmarks, news or feed headlines, habits, fitness and activity figures, sleep, media, system stats (battery, storage), finance figures. The common trio is tasks + calendar + weather, but the catalog is open-ended.
- **Light actions on the surface** — check off a todo, add a link, log a value, jot a note. Enough interaction to act on what the glance reveals, not enough to work in.
- **Layout and appearance customization** — arrange, resize, and theme the surface; backgrounds and dark mode; in one well-known pole of the market, the aesthetic layer (daily photos, quotes, greetings) is the signature.
- **Search entry** — a search box on the surface, since it often doubles as the session's starting point.
- **Cross-device sync** — the same surface configuration and data on phone, desktop, and web.
- **Connectors to sources** — links to the services and apps the widgets draw from, from calendar and fitness platforms to bookmark stores and news feeds.
- **Insights over the aggregated data** — trends, averages, correlations, periodic summaries. Common in the quantified-self pole, absent elsewhere; an optional capability.
- **Notifications and reminders** — surfaced on or from the dashboard's units.

### One Surface, Many Implementations

The core model is written in conceptual terms. Current products realize each concept differently:

```text
Concept:            The composed personal surface
Implementations:    browser new tab, web start page, desktop widget layer,
                    phone home/lock screen widget boards, dedicated web/mobile app

Concept:            The person's own situation, however sourced
Implementations:    data entered natively in the dashboard, data synced from
                    connected services, data mirrored from the device's apps,
                    personally selected external streams (feeds, bookmarks)

Concept:            Currency
Implementations:    live system meters, periodic service sync, scheduled feed
                    refresh, time-and-location-aware rotation of units
```

A reader who has only seen one implementation — say, a browser new-tab dashboard — should still be able to recognize a desktop widget engine or a phone's widget board as the same Type from the core model.

## How It Works

### Compose the surface

```text
Open the dashboard's edit/compose mode
→ choose widgets from the catalog (or connect source services)
→ arrange them on the surface (move, resize, stack)
→ configure each widget (location for weather, which list for todos, which feed)
→ save; the arrangement persists across sessions and devices
```

Composition is the user's job, not the vendor's: what appears, where it sits, and how it is configured are personal decisions. Some products ship a curated default set that the user adjusts; others start empty and are entirely user-assembled.

### The daily glance loop

```text
Arrive at the surface (open a new tab, unlock the phone, wake the desktop)
→ read the situation in a glance: time, weather, today's events, today's tasks, key numbers
→ act lightly: check off a task, set a focus, log a value, tap into the full app for anything deeper
→ leave; the surface remains, re-refreshing in the background
```

This loop is the product's reason for existing. It repeats many times a day and takes seconds each time. Anything that requires more than a glance or a tap belongs — by design — in the underlying application.

### Keep it current

```text
Connect the sources once (services, device apps, feeds, system sensors)
→ the dashboard pulls or receives updates automatically
→ widgets re-render with fresh values
→ the person never re-enters data the source already holds
```

The currency contract varies by pole: a desktop widget engine reads live system state; an aggregation dashboard syncs from connected services on a schedule; a phone's widget board mirrors whatever its source apps hold; a start page re-fetches feeds. In all forms, the person configures the flow once and the surface stays current without manual re-entry.

### Adjust over time

```text
Life changes → the surface changes
→ add a widget for a new concern (a new habit, a new metric)
→ remove widgets that stopped mattering
→ rearrange so the most-checked things sit where the eye lands first
```

### Capability tiers

**Defining core** — without these, not a personal dashboard:

- the person's own life as the data substrate
- a composed personal surface (one standing screen, user-assembled)
- multiple independent widget units
- at-a-glance currency (kept current, glance-and-go, light interaction)

**Standard capabilities** — present in most mature products:

- widget catalog across life domains
- light actions on the surface
- layout/appearance customization
- search entry
- cross-device sync
- connectors to sources
- notifications/reminders

**Optional / variant** — depends on the product's pole:

- insights, trends, correlations over the data
- an aesthetic/inspiration layer (photos, quotes, greetings)
- focus tooling (timers, routines) sitting on the surface
- sharing or team editions
- context-aware automatic rotation of units

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### The dashboard surface

The product itself. A single screen — a grid, a free-form canvas, or a stack of zones — holding the user's arranged widgets.

- typical content: the composed widgets, a greeting or time marker, often a search entry
- primary actions: read at a glance; light interactions per widget; tap through to source apps

### Compose / edit mode

The surface in arrangement state.

- typical content: the widget catalog or skin library, the current layout
- primary actions: add, remove, move, resize, stack widgets; enter a widget's configuration

### Widget configuration

Per-widget settings.

- typical content: the data source or scope (which list, which city, which feed, which metric)
- primary actions: choose source, set display options, set size

### Appearance settings

- typical content: themes, backgrounds, dark mode, units and formats
- primary actions: personalize the look of the surface

### Source connections (aggregation-heavy products)

- typical content: the list of connected services and apps, sync status
- primary actions: connect or disconnect a source, review what data flows in

## Important Rules / Behaviors

### The dashboard is a view, not the system of record

The dashboard's units mostly mirror, summarize, or link to data whose authoritative home is elsewhere — the task app, the calendar, the fitness service, the feed. Where a dashboard does hold native data (a lightweight todo, a sticky note, a manually logged value), that data exists to serve the glance; it is not a full management system for its domain. This is the structural line between the dashboard and the applications it sits above.

### Currency is the contract

The surface promises to reflect the person's current situation. Products therefore refresh automatically — live for system sensors, periodically for synced services and feeds. A widget that silently shows stale data breaks the Type's core promise; mature products make the refresh flow automatic and invisible.

### Light interaction boundary

Interactions on the surface are deliberately shallow: complete, log, jot, open. The moment work becomes deep — managing a project, writing, analyzing — the dashboard hands off to the application that owns the record. Products that violate this boundary stop being dashboards and become workspaces.

### Personal scope

The surface has exactly one intended audience: the person themselves. Sharing, when offered at all, is an optional extension (a shared team page, a published page), not the default posture.

### Composition persists

The arrangement is durable: it survives sessions, restarts, and (in mature products) follows the person across devices. The dashboard is a standing fixture of the person's environment, not a transient view.

## Variants

The Type is realized in several distinct poles, distinguished by delivery surface, data posture, and purpose:

- **Browser new-tab dashboard** — the dashboard replaces the browser's new tab; oriented around starting a focused work session (a daily focus, a lightweight todo, links, weather, search).
- **Web start page** — a reachable-from-anywhere page of user-arranged widgets; historically the oldest pole, often blending live widgets with personally selected feeds and bookmark collections.
- **Desktop widget engine** — the computer desktop itself becomes the canvas; users install and author widget skins (clocks, weather, system meters, visualizers) with near-total compositional freedom.
- **Platform-native widget boards** — the operating system's home, lock, or today screens host user-arranged widgets that mirror the device's apps; the OS hosts the surface and app data supplies it.
- **Aggregation (quantified-self) dashboard** — a dedicated app that pulls the person's data from many connected services plus manual entry into one cross-domain overview, often with trends and correlations.

A variant remains a variant while the defining core holds. If a product's surface becomes where records are created and managed as the main activity, it has crossed into personal-organizer territory; if its content becomes operator-published public information, it has crossed into portal territory.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Personal Organizer | the working application where the person's records of record are created and managed (events, tasks, contacts, notes); the dashboard is the composed at-a-glance view over such data, mostly mirrored or lightly edited |
| Life Planning Application | holds a plan of record — goals, decomposition, progress review; a dashboard can display goal or habit progress but holds no plan |
| Dashboard Platform (organizational) | name-level similarity only: organizational display systems over connected data sources, composed by builders for an audience of viewers; the personal dashboard is self-facing, over personal life data |
| Information Portal | organizes access to public, operator-published information and services; the dashboard organizes the person's own data and tasks. Widgets showing only one's own data → dashboard territory |
| Bookmark Manager | holds a collection of saved links as the record; a dashboard's units are live data slices. Link-grid start pages belong to the bookmark side of the seam |
| To-do / Calendar / Habit / Personal Finance Applications | single-purpose systems of record for their domain; the dashboard mirrors, summarizes, or lightly edits their data rather than managing it |
| Productivity Activity Tracker | automatically measures one activity domain as its record; an aggregation dashboard consumes such trackers as sources and spans all life domains |
| Personal Finance Management Application | money-domain system of record; its home screen is a capability of that Type, not a personal dashboard |

The most important boundary is with the **Personal Organizer**: both live in the person's daily environment and both touch the same data. The structural difference is where the records of record live and where the work happens — the organizer is the workspace, the dashboard is the window onto it.

## Representative Products

- Momentum — browser new-tab dashboard (focus/productivity pole)
- Exist — aggregation/quantified-self dashboard (web + mobile)
- Protopage — classic web start page
- Rainmeter — desktop widget engine for Windows (compose-your-own pole)
- Apple widgets (iOS Home Screen / Lock Screen / Today View) — platform-native widget boards

The core model was checked against the 2000s widget-and-start-page era (personalized start pages, desktop widget engines, PDA today screens) to avoid over-fitting to any current delivery surface or data posture.

## Sources

Research date: **2026-09-08**

- Momentum — https://www.momentumdash.com/
- Exist — https://exist.io/ , https://kb.exist.io/ (incl. "What's the difference between a service and an attribute?")
- Protopage — https://www.protopage.com/
- Rainmeter — https://www.rainmeter.net/
- Apple — https://support.apple.com/en-us/HT207122 ("How to add and edit widgets on your iPhone")

> Sourcing limitation: two candidate products could not be reached (a second start-page product timed out repeatedly; a health-dashboard candidate's domain resolved to an unrelated shop), and one sampled product's help center was unreachable, so its detail is homepage-level. The web-start-page pole therefore rests on thinner evidence than the other poles. Precise operational details (sync intervals, numeric limits, per-widget behaviors) are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
