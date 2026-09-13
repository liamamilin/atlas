# Restaurant Menu Management

## Overview

A **Restaurant Menu Management** application maintains the restaurant's menu as a structured, centrally managed catalog of record — items organized into sections, each carrying its price and ordering attributes — and keeps the surfaces that present or consume that menu (POS order entry, guest-facing digital menus, kiosks, online ordering, delivery platforms) in step with it.

The defining core is small:

```text
Menu of record (structured catalog: sections → items with price and options)
└── Maintenance loop (edit, price, schedule, control availability)
    └── Operational publication (the catalog drives at least one ordering/display surface)
```

Everything else commonly associated with modern menu software — multi-channel syndication to delivery platforms, QR guest menus, daypart scheduling, per-location price overrides, AI menu generation — is widespread in current products but is not what makes the product a menu management application. A single-location POS whose back office maintains the item catalog that its order screens consume satisfies the same definition.

The boundary matters: this application governs *what can be sold, at what price, where, and when*. It does not execute the sale (Restaurant POS), does not capture the customer's order (Restaurant Online Ordering), does not cost the recipes behind the items (Restaurant Food Cost Management), and does not manage the restaurant's other operating domains (Restaurant Management System).

## Users & Context

Primary users are the people accountable for what the restaurant sells:

- **Owner / operator** — sets prices, adds and removes offerings, decides which channels carry the menu.
- **General / shift manager** — adjusts availability during service, schedules menu changes.
- **Menu manager (chains)** — a dedicated role in multi-location brands; maintains the menu of record across sites and channels.
- **Chef / culinary lead** — contributes item content, descriptions, and preparation routing.

Secondary users:

- **Marketing staff** — run limited-time offers, featured items, and channel-specific promotions that live in the menu.
- **Franchise / brand teams** — govern menu consistency and approved variations across locations.

The work happens in a back-office web dashboard, occasionally supplemented by quick availability controls on POS devices during service. Menu changes are driven by seasonality, ingredient supply, cost movements, dayparts (breakfast/lunch/dinner, happy hour), and campaigns. The rhythm is a mix of planned cycles (seasonal menu launches, price updates) and in-service reactions (an item runs out and must be pulled from every surface immediately).

## Core Model

### The menu of record

The center of the application is the menu held as a persistent structured catalog — not a designed document and not a pile of transaction-side entries:

- **Menus** are the top-level containers, typically corresponding to the restaurant's physical menus or service periods (food, drinks, lunch, dinner, happy hour).
- **Sections / menu groups** organize items within a menu (appetizers, salads, entrees, desserts).
- **Items** are the sellable offerings. Each item carries its ordering attributes: price, name (including a kitchen-facing name where the order-entry or kitchen surface needs different wording), description, images, and commonly dietary information such as calories, allergens, or alcohol labeling.
- **Customization options** (modifier or option groups) attach to items or whole sections and define what guests or staff may choose: sizes, cooking temperatures, sides, add-ons. Option groups carry selection constraints — some are required, some enforce a minimum or maximum number of choices — and options may reference other menu items (a side that exists both as an item and as an add-on choice).

Items and option groups are typically reusable: the same item can appear in several sections or menus, and one option group can serve many items. This reuse is what keeps the catalog maintainable as it grows.

### Time, availability, and placement

Three control dimensions sit over the catalog:

- **Schedules** — menus and sections can be scoped to times of day or date ranges: distinct lunch and dinner menus, happy-hour pricing windows, limited-time offers. Outside their window, a menu is either hidden or shown as not yet orderable, depending on the surface.
- **Availability** — each item carries an availability state: in stock, sold out, or limited count. Marking an item sold out — "86ing" it in restaurant practice — removes it from orderable surfaces; limited-count items can decrement automatically as orders are sent and sell out at zero.
- **Placement** — visibility is controlled per **channel** (POS order entry, guest web or QR menu, kiosk, ordering profile, delivery platforms, digital menu boards) and per **location**. The same catalog serves all of them; each surface shows the slice of the catalog assigned to it.

### Consuming surfaces

The menu of record exists to feed surfaces that present it:

- staff-facing order entry on POS devices
- guest-facing digital menus (websites, QR-code menus, ordering profiles)
- self-service kiosks
- third-party delivery platforms
- digital menu boards (signage)

### Publishing

Changes to the catalog reach these surfaces through a publish or sync step. Mature products treat this as a first-class mechanism: edits are drafted and reviewed, then published to the chosen channels and locations — immediately, on a schedule, or as grouped change sets. Some products update guest-facing surfaces in near real time; others require an explicit publish action. The concept is constant: **a saved edit is not necessarily a live edit**.

### Supporting classifications

Alongside the guest-facing structure, items carry operational classifications: reporting categories for sales analytics, kitchen routing attributes (prep stations, printer routing) that direct order items to the right production surface, and tax behavior. These ride on the same catalog but serve back-office and kitchen needs rather than the guest.

## How It Works

### Build the menu of record

```text
Create menus and sections
→ add items with price, description, images, kitchen-facing name
→ attach option groups (sizes, sides, add-ons) with selection constraints
→ classify items (reporting category, kitchen routing, tax)
```

Large or migrating restaurants skip manual entry: products commonly offer bulk import from spreadsheets, import from another platform or from a photo/file of an existing menu, and increasingly AI-generated starter menus that the operator then edits.

### Maintain it

```text
Edit prices (bulk or per item; per-location or time-scoped overrides)
→ add seasonal items, retire dead ones
→ schedule daypart menus and limited-time offers
→ adjust item content and images
```

### Publish and place it

```text
Assign the menu to locations and channels
→ set per-channel and per-location visibility
→ publish (immediately or on a schedule)
→ verify the menu appears correctly on each surface
```

### Operate in service

```text
Item runs out mid-service
→ mark it sold out (86)
→ change propagates to order entry, kiosks, web menus, delivery platforms
→ restocked → mark in stock again
```

Availability is the fastest-moving part of the menu; the rest changes on a slower cycle.

### Govern across locations (chains)

Multi-location operators maintain the menu at brand level with per-location variation: a menu is assigned to many locations, individual items can carry location-specific prices or configurations, and editing rights are scoped so a manager can only change the menus of the locations they are responsible for. Standalone menu-management products push this further, positioning themselves as a layer above the POS that synchronizes menu details to every first-party and third-party channel from one brand-level control point.

## Interfaces

### Menus dashboard

The entry surface: lists the restaurant's menus with their assigned locations, channels, and schedules.

- typical information: menu name, locations, sales channels, hours, item count
- primary actions: create a menu, edit, duplicate, rearrange menu order, publish

### Menu editor

The working surface for one menu: its sections, items, and option groups.

- typical information: section hierarchy, items with price and channel/location columns, option groups
- primary actions: add/edit/reorder sections and items, attach option groups, bulk edit, assign channels and locations

### Item detail page

The full record for one menu item.

- typical information: names (guest-facing and kitchen-facing), price(s), description, image, option groups, availability state, channel and location visibility, reporting category, tax behavior
- primary actions: edit fields, change availability, adjust visibility, duplicate

### Availability controls

Fast, low-friction surfaces for in-service changes: sold-out toggles in list views, quick-edit modes, and 86 controls reachable from POS devices during service, sometimes with a report of everything currently 86'd.

### Visibility and publishing controls

Surfaces for placement and release: channel and location selectors per menu/section/item, per-delivery-partner visibility, and a publishing center where pending changes are reviewed, published, or scheduled.

### Import / migration tools

Bulk spreadsheet import, import from another platform, upload of an existing menu file or photo, and AI-assisted starter menus — all feeding the menu of record.

### Guest-facing preview

A preview of how the menu appears on each consuming surface (web menu, kiosk, delivery platform) before or after publishing.

### Item performance analytics

Common but not universal: reports on item sales, popular and slow dishes, and sold-out history, used to decide what to add, reprice, or retire.

## Important Rules / Behaviors

- **A saved edit is not necessarily a live edit.** Changes reach consuming surfaces through a publish or sync step. Some products require an explicit publish (and may offer scheduled publishing or grouped change sets); others propagate automatically. Some publish models have no rollback — reverting means making the change back and publishing again.
- **Availability propagates.** Marking an item sold out removes it from orderable surfaces across channels; in several products a limited-count item automatically sells out when its count reaches zero. Until the change propagates, staff and guests may still see the item — propagation timing is product-dependent.
- **Visibility composes.** An item is orderable on a channel only when its menu, its section, and the item itself are all visible there; hiding a parent hides its children regardless of their own settings. Option groups carry their own channel visibility — an option group not assigned to a channel does not appear there even if its item does.
- **Constraints must be satisfiable per channel.** A required option group that is invisible on a channel silently drops from orders on that channel; a minimum-selection group must have enough visible options on every channel for the requirement to be met. This is a classic menu-configuration failure mode.
- **Time-scoped menus behave differently per surface.** On guest web menus, a scheduled menu is often visible but orderable only in its window (to let guests order ahead); on kiosks it may be hidden; on POS order entry it appears flagged as not yet available, with overrides reserved for staff with the right permission or passcode.
- **Menu editing is permission-scoped.** Menu changes are gated by item/menu permissions and, in multi-location setups, by location assignment: a manager can edit only the menus of locations they are assigned to, and editing a menu shared across locations requires access to all of them.
- **Duplicated menus are independent.** Duplicating a menu creates a separate copy; later changes to the original do not flow to the copy. Third-party delivery channels are commonly not carried over automatically.
- **The menu of record is the single source.** Items must exist in the catalog — and usually in a section of a published menu — to appear on any surface; per-surface item lists are derived, not independent.

## Variants

The Type is realized in three common product forms, which are packaging and surface variants rather than different applications:

- **POS-embedded menu management** — the menu of record lives inside the restaurant POS and its primary consumer is staff order entry; other channels (web ordering, kiosks, delivery apps) are fed from the same catalog. The dominant form for small and mid-size restaurants.
- **Standalone multi-channel menu management** — a layer above the POS that synchronizes menu details, prices, and promotions across many first-party and third-party channels from one control point, typically at brand level for enterprise chains.
- **Guest-facing digital menu platforms** — QR-code and web menus as the primary surface, where guests browse, order, and pay directly and the operator edits the menu in real time; common for cafes, bars, and independents.

Common optional capabilities that vary by segment and product:

- AI menu generation and AI menu assistants (starter menus, stock checks, bulk restructuring)
- digital menu boards (signage) as a managed channel
- menu-level promotions and featured items
- menu engineering analytics (item profitability and popularity)
- multilingual menus
- combos, portions, alcohol labeling, open-priced items
- print-template outputs (posters, table tents) adjacent to the digital menu

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Restaurant POS | bundled neighbor | POS executes the sale — orders, checks, payment. Menu management governs what can be sold, at what price, where, and when. POS products bundle menu management as their configuration layer; the transaction core is what makes them POS. |
| Restaurant Online Ordering | consumer of the menu | Online Ordering captures the customer's order and checkout on guest surfaces. Menu management maintains the catalog those surfaces sell. Removing the ordering transaction leaves menu management intact. |
| Restaurant Food Cost Management | downstream neighbor | Food cost manages the costed recipes and plate economics behind menu items; menu management manages the guest- and staff-facing offering. The menu is the commercial face; the recipe cost is the money behind it. |
| Restaurant Management System | broader layer | A management system spans multiple operating domains (menu, labor, stock, cost) with a plan-to-actual control loop. Menu management is the single menu domain — a sibling, not a subset. |
| Kitchen Display System / KDS | adjacent consumer | KDS runs kitchen production flow. Menu management supplies the routing attributes (prep stations, printer categories) that send items to the right production surface, but does not run production. |
| Digital Product Catalog / PIM | generic analog | PIM manages product information for commerce generally. The restaurant menu carries restaurant service semantics — option groups with selection constraints, dayparts, 86 availability, kitchen routing, channel visibility — that have no analog in generic catalogs. |
| Nutrition Analysis Application | adjacent specialist | Nutrition analysis computes nutritional content; menu management may carry nutrition fields as item content without computing them. |
| Menu design / desktop publishing tools | out of Type | Producing a designed menu document (print or PDF) with no operational consumption is layout work, not menu management. A static menu file that nothing orderable consumes is the boundary case. |

## Representative Products

- **Toast** — POS-embedded menu management with a deep menu hierarchy (menus, groups, items, modifier groups), explicit publishing machinery, 86/stock control, and multi-location versioning.
- **Square for Restaurants** — POS-embedded menu management positioned as the central hub for what is sold across POS modes, online ordering, kiosks, and delivery apps, with menu hours, drafts, and per-location/per-channel visibility.
- **Checkmate (EveryWare)** — standalone "unified restaurant menu management": a layer above the POS synchronizing menu details, pricing, and promotions across first- and third-party channels at brand level for enterprise chains.
- **MenuTiger** — guest-facing QR/digital menu platform: interactive menus edited and repriced in real time, with QR ordering, translations, and item-performance analytics for independents.

## Sources

Research date: **2026-09-09**

Official operational documentation:

- Toast platform guide — Menu hierarchy: https://doc.toasttab.com/doc/platformguide/adminMenuHierarchy.html
- Toast platform guide — Publishing updates to POS location configuration: https://doc.toasttab.com/doc/platformguide/platformPublishingOverview.html
- Toast platform guide — Menu item inventory overview: https://doc.toasttab.com/doc/platformguide/adminMenuItemInventoryOverview.html
- Toast platform guide — Specifying ordering channel visibility: https://doc.toasttab.com/doc/platformguide/adminSpecifyingOrderingChannelVisibility.html
- Square Support Center — Items and inventory topic: https://squareup.com/help/us/en/topic/items-and-inventory
- Square Support Center — Create and update menus: https://squareup.com/help/us/en/article/6424-create-menus-with-square-for-restaurants
- Square Support Center — Manage your menus across locations and sales channels: https://squareup.com/help/us/en/article/8553-manage-your-menus-across-locations-and-sales-channels

Official product pages:

- Checkmate — EveryWare: Unified Restaurant Menu Management: https://www.itsacheckmate.com/solutions/everyware
- Checkmate — company site: https://www.itsacheckmate.com/
- MenuTiger — product home and features: https://www.menutiger.com/ , https://www.menutiger.com/features

> Sourcing limitations: the operator-facing help centers of two sampled vendors (Toast support center, TouchBistro help center) and the Checkmate help center could not be fetched from the research environment; Toast evidence was drawn from its official platform documentation instead, and Checkmate/MenuTiger evidence rests on official product pages rather than operational help articles. Claims about those two products' internal mechanics are therefore stated at product-page strength, and precise operational details (sync latencies, per-platform mapping workflows, availability mechanics for the QR-menu pole) are intentionally not asserted. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
