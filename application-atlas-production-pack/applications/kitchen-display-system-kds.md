# Kitchen Display System / KDS

## Overview

A **Kitchen Display System (KDS)** is the kitchen-side fulfillment application of a restaurant: it receives orders from order-capture systems — the point of sale, online ordering, kiosks, and delivery platforms — and presents them as tickets on screens in the kitchen, where staff work each ticket and mark it complete. It replaces the paper ticket rail and kitchen printer, and it is the system of record for what the kitchen is making, what has been made, and how long each order took.

The defining core is small. A KDS:

- holds **fulfillment tickets** that arrive from order-capture systems (it captures no orders itself and takes no payment),
- displays the **active ticket queue** on screens placed where kitchen staff work, and
- runs the **bump lifecycle**: staff mark items and whole tickets complete, completed tickets leave the queue (with recall when something must be remade), and the completion act is recorded.

Everything else the market associates with KDS — color-coded order timers, station routing, all-day counts, fulfillment reports, customer-facing "order ready" boards — is standard capability that mature products add, not what makes the product a KDS. The paper bump rail that preceded every KDS already had tickets, a display surface, and completion-by-removal; it had none of the rest.

When the center of gravity shifts to capturing orders and taking payment, the product is a Restaurant POS. When it shifts to planning production — recipes, prep lists, food safety — it is Commercial Kitchen Management. The KDS sits between them: it turns sold orders into made orders.

## Users & Context

The primary users are **kitchen fulfillment staff**, and they use the KDS differently by position:

- **Line/prep cooks** work the tickets routed to their station, tapping off items as they finish them.
- **Expeditors** sit at the pass where orders come together; they watch every ticket, coordinate stations, and give the final bump that sends food out.
- **To-go/takeout staff** work a queue of pickup and delivery orders, often with customer names, pickup times, and vehicle or delivery details on the ticket.

Secondary users are **managers and operators**: they configure screens, routing rules, timers, and order types; they watch service live; and they review fulfillment reports afterward. Configuration happens in a web or back-office dashboard; the kitchen screens themselves are deliberately minimal — in several products the line has no login at all, because a screen is shared by everyone on the shift.

The work environment is hot, greasy, loud, and fast. This shapes the Type: large text, high-contrast tickets, color instead of fine reading, audio alerts for new orders, optional hardware bump bars for hands-off operation, and kitchen-grade screens. The KDS runs *during service*, in real time — it is not a planning tool consulted before the shift.

## Core Model

### The Defining Core

```text
Order-capture systems (POS / online ordering / delivery platforms)
  ↓ send orders
Fulfillment Ticket (items + modifiers + notes + service context)
  ↓ appears in
Active Ticket Queue — displayed on kitchen screens
  ↓ worked by staff
Bump (item-level and ticket-level completion)
  ↓
Completed (recallable) — completion recorded, timing captured
```

Three structures, held together:

- **The fulfillment ticket of record.** Each order that reaches the kitchen exists as a ticket: the items, their modifiers ("no onion", "extra shot", allergy notes), kitchen-facing item names, and the service context — order type (dine-in, takeout, delivery), table or customer name, pickup or promised time, and, for delivery orders, often the platform it came from. The ticket is created upstream; the KDS receives it, displays it, and tracks it. The KDS never prices, discounts, or settles anything.

- **The kitchen-facing ticket display.** The KDS's world is a set of screens, each placed at a workstation — grill, fry, cold bar, expo, takeout. Each screen shows that station's active queue of tickets, typically ordered oldest-first, each ticket carrying an age timer. The queue is the shared truth of "what needs making right now"; every screen in the kitchen draws from the same orders.

- **The bump lifecycle.** The KDS's defining interaction is marking work done. Staff tap individual items (or modifiers) off as they finish them — the line strikes through — and tap the ticket header to bump the whole ticket when the order goes out. A bumped ticket leaves the active queue into a completed view, from which it can be **recalled** if an item must be remade. Every bump is a recorded state change, and the accumulated bump times are the raw material of the KDS's fulfillment reporting.

If any of the three is removed, the product stops being a KDS: tickets without a kitchen display are an order feed; a display without tickets is a passive screen; a display without bumping is a printer rendered on glass; a bump board over tickets not bound to real orders is just a task list.

### Standard Capabilities

Mature products commonly add the following. They make a KDS effective but do not define it:

- **Order-age timers and color transitions.** Each ticket carries a running timer; tickets change color as they age past configurable caution and late thresholds (commonly green → yellow → red), and a sound plays when new tickets arrive. This is the KDS's urgency language — a cook reads the wall of color before reading any words.
- **Station routing.** Routing rules decide which tickets (and which items within tickets) appear on which screen — by item, category, or course — so each station sees only its own work. A common role split is prep screens (item-level, granular) versus an expo screen (whole tickets, final control), with completions propagating across stations so no station re-makes finished food.
- **All-day counts.** A running total of each item across all open tickets — how many burgers the grill owes right now — so stations can batch prep. Some products separate items already fired from items held for later.
- **Queue control.** Rearranging tickets, prioritizing a late or urgent order, holding a ticket (or a course within it) until it should be fired.
- **Display configuration.** Ticket layouts and column counts, text sizes, per-modifier colors and emphasis, kitchen-facing names for items and modifiers, per-screen settings.
- **Order-type and channel awareness.** Dine-in, takeout, delivery, and kiosk orders distinguished on the ticket; delivery-platform labels so staff know which orders go out through which service; dedicated takeout views showing customer name, pickup time, and vehicle or address details.
- **Fulfillment reporting.** Bump times, prep times, ticket times, and station performance — by shift, daypart, channel, and location — the KDS being the only system that knows when the kitchen actually finished each order.
- **Hardware ecosystem.** Bump bars, kitchen-grade screens, and ticket or label printers working alongside the display.

### Optional Capabilities

Depending on the product and segment:

- **Customer-facing surfaces**: order-ready boards and tracker screens ("being prepared" / "ready"), SMS notifications to guests when an order is ready or when they arrive for pickup.
- **Course pacing and delayed routing**: firing items at staggered times based on cook times so all dishes of a table finish together.
- **Made-to-stock prompting**: quantity prompts telling made-to-stock kitchens what to cook ahead, with usage tracking (quick-service contexts).
- **Load balancing and capacity management**: distributing orders across stations by capacity, and factoring in-house versus off-premise load into quoting and pacing.
- **Companion analytics**: live kitchen-health scores and speed-of-service dashboards on managers' phones.
- **Multi-location standardization**: centrally managed screen settings and workflows across a brand's locations, with cross-location comparison.
- **Open integration surfaces**: webhooks and APIs that fire on order received / bumped events, letting the KDS participate in a wider restaurant stack.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Ticket arrival
Ways:     printer-emulation on the local network (the POS treats the KDS as a printer)
          cloud/API integration with the POS or ordering platforms

Concept:  Kitchen display surface
Ways:     commodity tablets (iOS/Android), dedicated kitchen-grade screens,
          per-station screens with role-based views (prep vs expo)

Concept:  Completion
Ways:     touch tap-off, hardware bump bar, per-item vs whole-ticket,
          per-station vs kitchen-wide propagation
```

A reader who has only seen one implementation — say, a tablet on a cafe counter — should still be able to recognize an enterprise multi-station installation, and the paper rail before both, from the core model alone.

## How It Works

### Connect the kitchen to the order stream

```text
Provision a screen (app on a tablet, or dedicated hardware)
→ bind it to a location and a role (prep / expo / takeout)
→ connect it to the order-capture systems (printer emulation or API)
→ set routing: which sources and which items reach this screen
→ set timers, colors, sounds, and layout
→ send a test order from the POS
```

From then on the flow is automatic: every order rung in upstream appears on the right screen within seconds, with its timer already running.

### Work a ticket (the core loop)

```text
Ticket arrives (color fresh, timer running, sound plays)
→ cook works the items, tapping each off (line strikes through)
→ expo watches the ticket come together across stations
→ expo bumps the ticket header when the order goes out
→ ticket leaves the queue into the completed view
→ if something must be remade: recall the ticket, it returns to the queue
```

Item-level completion matters as much as the ticket bump: it tells the expo which items are ready, tells other stations not to duplicate work, and — in some products — can automatically update the order's status to "ready" on the delivery platform it came from, or trigger a customer text.

### Run the pass during a rush

The KDS's live behaviors are all about the rush: tickets re-sort and re-color as they age; staff prioritize a late order or hold a course; all-day counts tell each station what to batch; managers watch open-ticket counts and lead times from a companion view and step in before service slips.

### Read the shift afterward

Bump and prep times accumulate into reports — average ticket times by station, daypart, channel, and location — which operators use to find bottlenecks and tune routing, timers, and staffing.

### Defining vs standard vs optional

- **Defining**: ticket arrival from order systems, kitchen-facing queue display, item and ticket bump with recall, recorded completion.
- **Standard**: timers and color transitions, station routing, all-day counts, queue control, display configuration, channel labels, fulfillment reporting, bump bars and printers.
- **Optional**: customer-facing ready boards and SMS, course pacing, made-to-stock prompting, load balancing, companion analytics, multi-location standardization, webhooks.

## Interfaces

### Ticket queue screen (the KDS itself)

The product's primary surface, designed to be read in two seconds.

- Typical information: tickets in columns or tiles, each with order number/type, age timer, items with modifiers and notes, customer or table name, pickup/promised time, delivery-platform label where relevant.
- Primary actions: tap an item to mark it complete, tap the ticket header to bump, recall a completed ticket, prioritize or hold, rearrange the queue.

### Station views

Per-workstation variants of the queue screen: a prep view showing only the items routed to that station, an expo view showing whole tickets with per-item completion state from the stations, and a takeout view showing pickup/delivery orders with customer, time, and vehicle or address details.

### All-day counts panel

A running tally of item quantities across all open tickets, optionally split into fired versus held; usually a side panel or a dedicated screen.

### Configuration dashboard (web/back office)

Where managers work: screens and device management, routing rules (sources, categories, items), timer thresholds and alert sounds, layouts, fonts, modifier colors, order types, users and locations, and subscription/billing in standalone products.

### Reporting views

Fulfillment metrics — bump times, prep times, ticket times, station performance — filterable by location, device, shift, and channel; some products add a live companion view (open tickets, lead times, kitchen score) on a manager's phone.

### Customer-facing surfaces (optional)

Order-ready boards above the counter or drive-thru, and tracker screens showing "being prepared" / "ready"; driven by the same bump state the kitchen works.

## Important Rules / Behaviors

### The KDS never owns the order's money

Orders, prices, taxes, and payments live in the POS and ordering systems. The KDS receives the ticket and tracks fulfillment; it does not price, discount, refund, or settle. This is the sharpest structural line between KDS and POS.

### Completion is a state change, not a gesture

Bumping removes the ticket from the active queue and records the completion — which is why recall exists. Remakes and mistakes are handled by recalling the ticket back into the queue, not by editing history. Some products give a brief undo window for accidental taps before the ticket settles into the completed view.

### Completions propagate across stations

In multi-screen kitchens, an item completed at one station is marked as done on the other screens that show it, so no station remakes finished food. Whether a completion applies kitchen-wide or only to one screen is a per-installation configuration.

### The queue is shared truth, ordered by urgency

Tickets arrive in order and age visibly. Staff may rearrange or prioritize, but the queue — not anyone's memory — is what the kitchen works from. When the network or a screen fails, orders stop appearing; reliability posture (wired connections, kitchen-grade hardware) is a real operational concern, though specific offline behavior varies by product and is not uniform across the market.

### Timers are configured, not universal

Caution and late thresholds, colors, and alert sounds are set per installation and often per order type. There is no industry-standard timer value; a ticket "late" in one kitchen is normal in another.

### The line has no accounts

Kitchen screens are shared surfaces; staff typically do not log in per shift. Permissions and user management live in the configuration dashboard, not on the line.

## Variants

- **POS-embedded KDS** — a KDS sold as an add-on to a POS platform; deepest integration with that POS, order sources limited to its ecosystem (the Square-style pole).
- **Standalone POS-agnostic KDS** — an independent KDS that connects to many POS and ordering platforms, often via printer emulation or APIs; bought precisely because the kitchen display should outlive any POS decision (the Fresh-style pole).
- **Enterprise dedicated KDS** — a dedicated KDS product line for chains and large kitchens: advanced routing, pacing, load balancing, made-to-stock prompting, customer-facing boards, multi-location standardization, and its own hardware (the Crunchtime/QSR-heritage pole).
- **Segment shapes** — quick-service and fast-casual kitchens run ticket grids and made-to-stock prompting; full-service kitchens lean on coursing, expo views, and plating support; cafes and food trucks run a single screen; ghost kitchens run multi-brand ticket streams into one line.
- **Hardware posture** — commodity tablets versus kitchen-grade screens and bump bars; per-screen versus bundled pricing.

A variant remains a variant unless it changes the core: a product that stopped displaying tickets to kitchen staff, or stopped tracking completion, would no longer be a KDS no matter what else it did.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Restaurant POS | upstream sibling | POS captures orders and takes payment; KDS consumes already-captured orders for fulfillment. Vendors themselves warn against conflating the two. Give the KDS order entry and payment and it has become a POS. |
| Restaurant Online Ordering | upstream channel | customer-side order capture; its orders arrive as tickets on the KDS |
| Food Delivery Marketplace | upstream channel | third-party delivery orders reach the KDS as tickets (often platform-labeled); the marketplace, not the KDS, runs couriers and consumer surfaces |
| Restaurant Delivery Management | adjacent, dispatch-side | manages couriers, routes, and driver handoff; the KDS manages kitchen prep and knows nothing about drivers |
| Commercial Kitchen Management | adjacent, planning-side | production planning — recipes, prep lists, food safety, costing — before and around service; the KDS is the during-service ticket flow. Naming caution: one major vendor brands its KDS product "Kitchen Management"; the product is a KDS, not a production-planning system |
| Institutional Foodservice Management | adjacent segment | standing meal programs for a known population (cycle menus, tray service) rather than anonymous à-la-carte ticket flow during service |
| Kitchen printer | predecessor, not a Type | the printer outputs tickets but holds no state: no bump, no recall, no timing. A KDS may even emulate a printer as its integration method — the printer is a substrate, not the Type |

## Representative Products

- **Square KDS** — POS-embedded KDS for Square for Restaurants; Android app on kitchen-grade tablets; prep/expo device roles
- **Fresh KDS** — standalone POS-agnostic KDS running on iOS/Android tablets; integrates with 30+ POS and ordering platforms
- **Crunchtime Kitchen** (formerly QSR Automations ConnectSmart Kitchen) — enterprise dedicated KDS for chains; advanced routing, pacing, and made-to-stock prompting; sold within Crunchtime's suite under the product name "Kitchen Management"

The defining core was checked against the paper bump rail and the early dedicated-KDS generation to avoid defining the Type by today's tablet-and-cloud implementation.

## Sources

Research date: **2026-09-08**

- Square — KDS product page: https://squareup.com/us/en/kitchen-display-system
- Square Support Center — "Set up Square KDS": https://squareup.com/help/us/en/article/7924-beta-kds-android
- Square Support Center — "Complete and recall orders with Square KDS": https://squareup.com/help/us/en/article/8171-complete-orders-with-square-kds
- Square Support Center — "Route orders to the kitchen with Square KDS": https://squareup.com/help/us/en/article/7959-route-orders-with-your-kds
- Fresh KDS — product site: https://www.freshkds.com/
- Fresh KDS Help Center — "The Fresh KDS Glossary": https://help.freshkds.com/en/articles/6657677-the-fresh-kds-glossary
- Fresh KDS Help Center — "Fresh KDS Training Guide": https://help.freshkds.com/en/articles/6546044-fresh-kds-training-guide
- Crunchtime — Kitchen (KDS) product page: https://www.crunchtime.com/kitchen
- Crunchtime — "What Is a KDS? An Easy Guide to Kitchen Display Systems": https://www.crunchtime.com/blog/what-is-a-kds-a-guide-to-kitchen-display-systems

> Sourcing limitation: Toast (the largest POS-embedded KDS pole) could not be reached — its site returned access errors on every attempted path on 2026-09-08 — and Lightspeed and TouchBistro KDS pages were likewise unreachable. No claim in this document depends on those products. Precise operational values (timer defaults, limits, pricing details) are deliberately not stated: all such values are product- and installation-configurable per the sources above. Detailed product-by-product evidence is recorded in the paired Research Notes.
