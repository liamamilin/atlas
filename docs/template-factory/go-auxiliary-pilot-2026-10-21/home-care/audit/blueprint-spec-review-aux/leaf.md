# Home Maintenance Application

## Overview

A **Home Maintenance Application** helps a homeowner stay on top of the recurring upkeep of their own home: it holds the home's care targets, turns them into a schedule of recurring care work, and keeps a record of the care that was done.

The defining structure is small:

```text
The user's own home (structure, systems, equipment) as the subject of care
└── Recurring upkeep plan (care items with cadences → due work over time)
    └── Upkeep record (completions accumulating into the home's care history)
```

Everything else commonly associated with these products — reminder notifications, built-in task libraries, appliance databases with manuals and warranties, receipts, pro recommendations, rewards — is widespread in current products but is not part of the defining core. The paper home-maintenance schedule pinned in a house book satisfies the same structure without any of them.

When the center of gravity shifts — to the household's routine labor (chores), to the whole-home information binder, to possession records, or to planned change-work — the product is drifting toward a different Application Type.

## Users & Context

The primary user is a homeowner responsible for a residential property — a first-time buyer facing an unfamiliar list of systems to care for, or a long-time owner keeping up a known routine.

Typical reasons to open the application:

- see what care is due now or coming up this season
- check how to do a care task, or who did it last time and what it cost
- record that a task was completed, with photos, receipts, or cost
- look up an appliance's manual, warranty, or service history

Secondary users are household members who share the care work. The context is consumer and personal: one's own home, used occasionally but over many years, mostly from a phone. Small-scale landlords who track upkeep across multiple rental properties are at the edge of this Type — at scale their needs belong to professional property-maintenance systems.

## Core Model

### The Defining Core

```text
The user's own home (structure, systems, equipment) as the subject of care
└── Recurring upkeep plan (care items with cadences → due work over time)
    └── Upkeep record (completions accumulating into the home's care history)
```

Three properties. If any one is removed, the product is no longer recognizable as a home maintenance application:

- **The home as the anchored subject of care.** The application holds a persistent record of the user's own home, and its care targets are the home's physical fabric — structure, systems, and equipment (roof, gutters, HVAC, water heater, detectors, appliances). Tasks hang from this record. Without it, the product is a generic to-do or reminder app, or a content site with no home of record.
- **The recurring upkeep plan.** Care items are held as scheduled, repeating work — seasonal, annual, monthly, or usage-based cadences that generate due work over time. Without the forward-looking plan, the product is a one-off repair log or home journal.
- **The upkeep record.** Completions are tracked and retained — what was done, when, and often at what cost and by whom — accumulating into the home's care history. Without it, the product is a static checklist or a reminder-only tool that never learns what has actually been done.

The three are load-bearing together: a plan without a record is a tips checklist; a record and schedule without the home anchor is a generic recurring to-do list; a home record with history but no plan is a service log.

### Standard Capabilities

Mature products commonly add these. They make the upkeep practical but do not define the Type:

- **Reminders and notifications** — due-date prompts delivered through the product's channels (text and email are observed; mobile apps also prompt in-app), so scheduled care actually happens.
- **Home profile** — the home's characteristics (location, age, systems, appliances) used to tailor which care items apply and when.
- **Appliance and equipment records** — per-device entries with make/model, manuals, and warranties, anchoring care tasks to specific equipment.
- **Service history with receipts** — logged completions carrying cost, provider, and documents.
- **Guidance content** — short how-to instructions attached to care tasks.
- **Household sharing** — more than one person can see and act on the plan.
- **Calendar or seasonal views** — the plan rendered as what's due this month or this season.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Products realize each concept differently:

```text
Concept:            The home as subject of care
Implementations:    a home profile with systems and appliances; a binder pre-loaded
                    from an inspection report; a property record in a household hub

Concept:            The recurring upkeep plan
Implementations:    built-in task libraries filtered by home characteristics;
                    user-defined recurring tasks; prompts generated from the profile

Concept:            The upkeep record
Implementations:    check-off with timestamps; a log of actions with receipts and
                    costs; service records attached to appliances
```

A reader who has only seen one implementation should still be able to recognize the others from the Core Model.

## How It Works

### Set up the home and its care targets

```text
Add the home (location, type, age)
→ add its systems and equipment (in partner-distributed products the home
   may arrive pre-loaded from an inspection report)
→ the application proposes applicable care items
→ adjust the plan: add, remove, re-cadence
```

The home record is the anchor: every task, appliance, and receipt belongs to this home.

### Work the plan over time

```text
Care items come due on their cadences
→ reminders surface what's due (and what's overdue)
→ the homeowner does the work (DIY, guided by attached instructions)
   or hires it out (some products recommend or connect to pros)
→ completion is recorded: date, notes, photos, cost, receipt, provider
→ the cycle resets; the next due date is computed
```

This is the interaction loop of the Type: due work → done work → recorded work → next due work. Over years the record becomes the home's care history — useful for warranties, resale, and deciding when replacement beats repair.

### Look up and decide

```text
Open an appliance or system record
→ see its manual, warranty, and past service
→ decide the next action (maintain, repair, replace)
```

### Core vs Common vs Optional

**Defining core** — without these, not a home maintenance application:

- the user's own home as the anchored subject of care
- recurring upkeep plan with cadences
- upkeep record / care history

**Common mature structure** — present in most current products:

- reminders and notifications
- home profile tailoring the plan
- appliance/equipment records with manuals and warranties
- service history with receipts and costs
- guidance content, household sharing, calendar/seasonal views

**Optional / variant** — depends on product and segment:

- pro recommendations or booking (marketplace leg)
- rewards for completed care
- recall alerts from stored make/model numbers
- sustainability/carbon tracking
- multi-property support
- self-hosted/open-source deployment
- distribution through real-estate professionals (pre-loaded binders)

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Home overview

The entry surface for the home as a whole.

- the home's profile (location, type, age), its systems and appliances at a glance
- what's due now, overdue, and coming up
- primary actions: open the plan, add an appliance, record a completion

### Upkeep plan / task list

The schedule surface.

- care items grouped by cadence, season, or system; due and overdue states
- primary actions: mark done, snooze/reschedule, edit cadence, add a custom task

### Task detail

The surface for one care item.

- cadence, last done, next due, instructions, attached photos/receipts
- primary actions: complete with notes/cost/receipt, view history, edit

### Appliance / equipment record

The per-device surface.

- make/model, manual, warranty, purchase details, past service entries
- primary actions: log service, attach document, link care tasks

### Care history / log

The record surface.

- chronological completions with dates, costs, providers, documents
- primary actions: filter by system or year, export or share (in some products)

### Settings / sharing

Household members, notification preferences, and (where offered) pro connections.

## Important Rules / Behaviors

### Cadence drives the plan

A care item's recurrence (seasonal, annual, monthly, usage-based) is what generates due work. Completing a task computes its next due date; the plan is self-perpetuating. Exact cadence options vary by product.

### The record is per-home and durable

Everything — tasks, appliances, completions, receipts — belongs to the home record and survives years of use. This is what makes the history valuable at resale or for warranty claims.

### The plan is tailored, not universal

Care items apply conditionally: a home's location, climate, age, and equipment determine which tasks apply and when. The same product proposes different plans for different homes.

### Reminders are prompts, not enforcement

The application surfaces due work; completing it remains the homeowner's responsibility. The plan does not disappear when ignored — items stay due until done or changed.

### DIY and hired work both feed the record

Whether the homeowner does the work or a pro does, the completion is recorded against the home. Some products recommend pros; the record remains the homeowner's.

## Variants

Common realizations of the Type:

- **suite-embedded** — maintenance reminders and histories as one capability of a whole-home binder (documents, inventory, projects, pros) distributed through real-estate professionals
- **log-and-rewards** — a home-anchored care log with prompts, receipts, and incentives for completed care
- **appliance-anchored** — the plan built outward from per-device records, manuals, and warranties
- **household-ERP / self-hosted** — upkeep machinery (equipment, recurring tasks, batteries) inside an open-source household system; documents the boundary toward chore/household tools
- **pro-connected** — the plan joined to recommended or bookable service professionals
- **multi-property** — the same upkeep machinery across several homes; at scale this drifts toward professional property-maintenance systems

A variant remains a **Variant** while the defining core holds. When the center of gravity shifts to the household's routine labor, the whole-home binder, possession records, or planned change-work, the product belongs to the neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Household Chore Application | recurring tasks too, but the subject is the household's routine living work (cleaning, laundry), not the home's physical fabric |
| Home Management Application | the whole-home binder/hub is the center; maintenance machinery is one capability beside documents, inventory, and finance |
| Home Inventory Application | the record is of possessions; appliance records overlap, but recurring-work machinery is the maintenance app's center |
| Home Improvement Planner | bounded, discretionary change-work (renovation, remodel) with a money plan, vs recurring preservation of existing systems; products bundle both with separate machinery |
| Property Maintenance Management | the professional/landlord operations system (work orders, vendors, tenants, portfolios); different subject of record and user |
| Home Services Marketplace | the hiring leg (finding and booking pros) vs the homeowner's upkeep plan and record; complementary |
| Home warranty / service-plan products | a service contract (coverage, claims, dispatch) vs the homeowner's own care plan; warranty apps may carry reminders as engagement features |
| CMMS / EAM | the same abstract shape (assets + recurring preventive tasks + history) but for organizations' physical assets; different subject, user, and scale |
| Smart Home Platform | device control and automation vs upkeep planning |

The most important boundary is with the Household Chore Application, because both hold recurring tasks with completion tracking. The structural difference is the task's subject: the home's fabric versus the household's routine.

## Representative Products

- HomeBinder — suite-embedded pole; binder distributed through home inspectors, lenders, and agents, with maintenance reminders and recall alerts
- Dwellin — log-and-rewards pole; home profile, appliance records, maintenance logging, prompts, rewards
- Under My Roof — Apple-ecosystem suite module; maintenance beside inventory, renovations, documents, and insurance
- Grocy — household-ERP / self-hosted pole; equipment, chores, and batteries machinery documenting the chore boundary

The dedicated maintenance-plan suite pole (HomeZada class) could not be reached during research and is intentionally not characterized here.

## Sources

Research date: **2026-09-08**

- HomeBinder — https://www.homebinder.com/
- Dwellin — https://dwellin.com/ , https://dwellin.com/app/how-it-works/ , https://dwellin.com/app/overview/
- Grocy — https://grocy.info/
- Under My Roof — via the paired Home Inventory research pass of 2026-09-08 (official surfaces reachable then; direct fetch timed out this pass)

> Sourcing limitation: several prominent products in this category were unreachable from the research environment on 2026-09-08 (HomeZada, BrightNest, HomeSmarts, HomeKeepr returned blocks or empty responses; Centriq and Homebrella domains have been recycled by unrelated businesses; major home-warranty vendors returned blocks). Claims in this document are calibrated accordingly: capabilities observed across multiple sampled products are described as common; capabilities observed in a single product are described as product-specific or optional; the dedicated maintenance-plan pole is under-evidenced and is not characterized.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
