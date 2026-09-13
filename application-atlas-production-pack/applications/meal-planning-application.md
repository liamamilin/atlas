# Meal Planning Application

## Overview

A **Meal Planning Application** is an application for deciding ahead of time what to eat: it holds a plan of meals on future days and eating occasions, ties each planned meal to real food content (a recipe or dish), and derives from that plan a consolidated shopping list.

The defining structure is small:

```text
Forward Meal Plan (meals bound to future dates + occasions)
└── Planned meals reference food content (recipes / dishes)
    └── Plan-derived shopping list (ingredients consolidated across meals)
```

Everything else commonly found in modern products — automatic plan generation, calorie and macro targets, pantry tracking, delivery handoffs, family sharing — varies by product and is not part of the defining core. A paper weekly menu pad with an attached grocery list and a recipe box satisfies the same structure.

The seam to keep in mind: this Type is **prescriptive and future-facing** (what will be eaten). Applications centered on **descriptive and past-facing** records (what was actually eaten) are Food / Calorie Tracking Applications, however much the two product families borrow from each other.

## Users & Context

The primary user is a person who cooks for themselves or a household — an individual, a couple, or a family — who wants to stop deciding dinner at dinnertime:

- plan the coming week's meals in one sitting, instead of day-by-day improvisation
- avoid repeated "what's for dinner" decisions and repeated grocery trips
- match meals to household preferences, allergies, or a diet they follow
- shop once, with a list that already contains everything the week's meals need

Secondary users and postures:

- individuals with explicit nutrition goals (calorie or macro targets) who let the system assemble plans to hit those targets
- health, fitness, and nutrition professionals who build meal plans for clients using the same plan-building machinery
- household members who consult the plan or the list (sharing depth varies by product)

The context is domestic: home kitchens, weekly grocery trips, and the recurring rhythm of a week of meals. There is no production kitchen, no census, no money moving through the system — that is the world of institutional foodservice, not this Type.

## Core Model

### The Defining Core

```text
Forward Meal Plan
└── Meal entry (date × eating occasion × food content)
    └── Recipe / Dish (ingredients, servings)
    └── Shopping list derived from the plan
```

Three properties, held together. If any one is removed, the product is no longer recognizable as a meal planning application:

- **The forward meal plan is the object of record.** Meals are assigned to future dates and eating occasions, persistently held and revisable. The plan — not the recipe collection, not a consumption log — is what the product exists to maintain. Without it, the product is a recipe library or a calendar.
- **Planned meals carry food substance.** Each entry on the plan references a recipe or dish with ingredient content — the thing that will actually be cooked and eaten — not merely a calendar event labeled "dinner". Without this, the plan is just a calendar.
- **The plan drives provisioning.** The application derives a shopping list from the planned meals, consolidating ingredients across them so one shopping trip can cover the plan. Without this, the product is a menu display; the operational loop that makes planning worth doing is gone.

### Standard Capabilities

Mature products almost universally add:

- **Eating occasions / meal-time slots** — breakfast, lunch, dinner, snack as the vertical axis of the plan; typically customizable (rename, add, recolor, reorder).
- **Serving counts and scaling** — plans and recipes are sized for a number of people; scaling a planned recipe updates the shopping list quantities.
- **Aisle-organized shopping list** — list items grouped by grocery category or aisle, with ingredients from different meals merged when they match (quantity aggregation, e.g. eggs from three recipes appearing once with a combined amount).
- **On-hand suppression** — a pantry or staples inventory of items already at home, which are excluded from (or de-prioritized on) the shopping list.
- **Recipe acquisition** — either importing/clipping recipes from the web into a personal recipe book, or a curated recipe/food library supplied by the product; often both entry paths exist.
- **Reusable menus / templates** — saved collections of meals (single occasions or multi-day patterns) that can be dropped onto a future week.
- **Week as the dominant horizon** — the week is the canonical planning unit, with monthly and daily views common.
- **Print / share / export** — printed plans and lists, calendar handoff, email or messaging sharing.

### One Structure, Many Implementations

The Core Model is written conceptually; specific products realize each piece differently:

```text
Concept:           Food content beneath the plan
Implementations:   personal recipe book (clipped/created), product-curated recipe library,
                   food database entries

Concept:           Plan assembly
Implementations:   manual drag-and-drop onto a calendar, auto-generation from a
                   preference profile, auto-generation from calorie/macro targets,
                   applied templates / reusable menus

Concept:           On-hand suppression
Implementations:   pantry with stock and expiry tracking, static staples list,
                   virtual pantry consumed by the generator with priority
```

A reader who has only seen one pole (say, a target-driven automatic planner) should still be able to recognize a manual calendar-style planner as the same Type from the Core Model.

## How It Works

### The weekly loop

The canonical operational loop, as the products themselves frame it, is **plan → shop → cook**:

```text
Build the plan
→ assign meals to days and occasions (by hand, from a template,
   or by generating from preferences/targets)
→ review the week
→ generate / refresh the shopping list (ingredients consolidated, on-hand items removed)
→ shop (check items off; optionally hand the list to a delivery service)
→ cook (the recipe surfaces as a reference at meal time)
→ repeat next week
```

The plan is revisable throughout the week; the list follows the plan's current state.

### Building the plan

Two assembly philosophies exist, and many products sit between them:

```text
Manual assembly:   browse your recipe book → drag a recipe onto a date and meal-time
                   → adjust servings → repeat → optionally save the week as a reusable menu

Auto-generation:   set a preference profile (diet style, exclusions, servings) or
                   targets (calories, macros, meals per day) → the system fills the
                   days with matching meals → swap or regenerate individual meals
```

Both produce the same object — meals bound to future dates — which is why they are variants of one Type rather than two Types.

### Deriving the shopping list

The list is computed from the plan, not maintained independently:

```text
Take the planned meals in the list's date range
→ collect their ingredients (scaled for servings)
→ merge matching ingredients into single line items
→ group by aisle/category
→ suppress items marked as on hand (pantry / staples)
→ hand the list to the shopper (in-app checkoff, print, or delivery service)
```

Changing the plan changes the list: moving a meal, swapping a recipe, or changing serving sizes is reflected the next time the list is viewed or refreshed. Lists are scoped to a date range so that last week's items do not silently linger.

### Professional plan building

In the professional posture, the same machinery runs with a different operator: a professional assembles or generates plans **for clients**. The plan-building core is identical; what is absent in this Type is the client-relationship machinery (client management, adherence tracking, coaching communication) that would make it a coaching platform.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Meal planner (calendar)

The center of the product.

- a day × meal-time grid for the week (commonly also daily and monthly views)
- shows each slot's planned meal, servings, and often a photo
- primary actions: add a meal (recipe, note, or menu) to a slot; drag to move; copy/swap/delete; change servings; jump to the recipe; generate a plan; print the plan

### Recipe library / recipe detail

The food content the plan draws on.

- searchable, categorized collection of recipes with ingredients, directions, servings, times, and often nutrition information
- import path (web clipping or import) and manual creation
- primary actions: save/edit recipe, scale servings, add to the plan, add to the shopping list directly

### Shopping list

The provisioning surface.

- items grouped by aisle/category, with merged quantities and per-item checkoff
- scope to a date range; add custom items; remove items already owned
- primary actions: check off while shopping, add/remove/merge items, share, print, send to a delivery or pickup service

### Pantry / staples

The on-hand inventory (present in many, not all, products).

- items already at home, sometimes with quantities and expiry dates
- primary actions: add items, mark purchased/used, move items between list and pantry

### Plan assembly / preferences

Where generation-driven products concentrate their controls.

- diet style, exclusions/allergies, servings, calorie and macro targets, meals per day
- primary actions: generate a plan, regenerate or swap individual meals

### Settings

- meal-time slots (names, order, colors), week start day, units, sync account

## Important Rules / Behaviors

### The list follows the plan

The shopping list is a derived view of the plan's current state within a date range. Plan edits propagate to the list; conversely, manual list edits (adding a custom item, removing an owned item) are user overrides layered on top of the derivation. Several products document the confusion this can cause ("why is my list empty / why are old items here") — the plan↔list coupling is the behavior users must understand.

### Ingredients merge by identity

Consolidation across meals matches on ingredient identity and unit; near-matches (different wording, different units) may not merge automatically and can be merged manually. Products treat this as best-effort aggregation, not guaranteed accounting.

### On-hand items are suppressed, not tracked to zero

Pantry/staples features exclude known-on-hand items from the list (or let the generator use them first). The inventory is a convenience layer over the shopping trip, not a full stock-keeping system with depletion accounting.

### Plans persist into the past

The planner is forward-facing by purpose, but past plans typically remain viewable and searchable — the plan history doubles as a record of what the household intended to eat.

### Nutrition is a layer, not the engine (except where it is)

In most products, nutrition information attaches to recipes and can be displayed or tallied over the plan; it does not drive anything. In target-driven variants, the nutrition target is an *input* to plan generation — it remains prescriptive (what you plan to eat), never a record of consumption.

### No transaction, no production

Money and production belong to other systems. The list ends at the store (or at a handoff to a delivery service); nothing in the Type prices ingredients, tracks a budget by default, or schedules kitchen production.

## Variants

- **Manual calendar planner (recipe-library-centric)** — the user assembles plans from a personal recipe collection; the product invests in recipe acquisition (web clipping), organization, and cooking-time ergonomics; nutrition is optional. Often sold as a one-time purchase.
- **Calendar-first community planner** — web-based planner organized around the planning calendar, with recipe import and a community/teaching layer; subscription model.
- **Preference-driven auto planner (mobile-first)** — the user configures a preference profile; the system fills the week from a curated recipe library and produces the list automatically; oriented to quick weeknight cooking.
- **Target-driven diet planner** — calorie/macro targets and meals-per-day are the primary inputs; the system generates complete plans to hit them; appeals to fitness and weight-management users; commonly offers a professional tier.
- **Curated plan subscription** — services that deliver ready-made weekly plans (with lists) rather than user-assembled ones; the user subscribes to the plan source instead of building the plan. (Existence of this variant is widely known, but it was not verified from official documentation in this research pass; described here without product-specific claims.)
- **Professional plan-builder posture** — any of the above sold to professionals who produce plans for clients; the plan machinery is unchanged, the operator is not the eater.

A variant remains a Variant unless it changes users, core objects, workflow, or rules so much that the Core Model no longer applies. Meal kits, for example, cross that line in the other direction: there the vendor decides the meals and the "list" arrives at the door — that is subscription commerce, not this Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Food / Calorie Tracking Application | closest blend | plans what to eat in the future (prescriptive; plan is the record); that Type records what was eaten (descriptive; consumption log is the record, resolved per-entry into nutrients). Trackers embed plans and planners show nutrition, so the seam is center of gravity: intent vs act. |
| Nutrition Coaching Platform | adjacent | the coach–client relationship (client management, programming, adherence, communication) is the core there; here planning is self-serve. Professional tiers of planners build plans for clients but carry no coaching machinery. |
| Family Organizer | overlapping module | household hubs include a meal-planning loop (recipes → plan → shopping list) beside the family calendar and lists; the dedicated planner is where the meal plan — not the household — is the system of record. |
| Institutional Foodservice Management | different world | professional menu planning binds menus to census, diet orders, production quantities, and money; household planning binds dishes to home dates and one shopping trip. |
| Recipe applications / recipe managers | supporting structure | recipe-centric apps center on finding and storing recipes; here recipes are plan inputs. Recipe managers that carry the full plan loop belong to this Type; pure recipe discovery/storage sits below it. |
| Subscription Commerce Platform (meal kits) | adjacent commerce | meal-kit services decide the meals and deliver the ingredients under a transaction; here the user decides and shops. |
| Calendar Application | surface overlap | calendars hold meal-time events but have no food semantics, recipe substance, or list derivation; plan→calendar export is a handoff. |
| Grocery / shopping-list tools | below-Type | a list tool without plan and recipes is only the third leg of the core. |

## Representative Products

- Mealime — preference-driven mobile planner (plan → shop → cook framing; auto grocery list)
- Paprika Recipe Manager — recipe-manager-anchored planner with web clipping, pantry, and menus
- Plan to Eat — calendar-first web planner (recipe book / meal planner / shopping list)
- Eat This Much — target-driven automatic planner with professional tier

The Core Model was checked against the analog ancestor (weekly menu pad + grocery list + recipe box) to avoid over-fitting to the modern mobile auto-generation pattern. A fifth intended sample (an editor-curated plan subscription) was dropped because its official documentation was not reachable; no claims in this document depend on it.

## Sources

Research date: **2026-09-08**

Official product surfaces (fetched directly):

- Mealime — https://www.mealime.com/ (positioning, plan→shop→cook loop, personalization, auto grocery list)
- Paprika Recipe Manager — https://www.paprikaapp.com/ and user guide https://www.paprikaapp.com/help/mac/ (sections, recipe fields, grocery/pantry/planner mechanics, menus)
- Plan to Eat — help center https://help.plantoeat.com/ with Meal Planner (https://learn.plantoeat.com/help/meal-planner) and Shopping List (https://learn.plantoeat.com/help/shopping-list) documentation (planner calendar, serving-size propagation, ingredient merging, staples, date ranges)
- Eat This Much — https://www.eatthismuch.com/ (automatic planner, calorie/macro inputs, virtual pantry, grocery lists, professional tier)

> Sourcing limitation: a fifth representative product (an editor-curated subscription planner) was excluded after its official pages proved unreachable on 2026-09-08; the curated-plan variant is described only in general terms and no product-specific claims about it are made. Product-specific details observed in documentation (exact merge rules, toggle behaviors, import formats, integration partners, shutdown notices) are recorded in the paired Research Notes rather than asserted here.
