# Restaurant POS

## Overview

A **Restaurant POS** is the restaurant's operator-facing transaction system: restaurant staff compose a guest's food-and-beverage request as an **order** by selecting from the operation's configured menu, the charges accumulate on a **check** that is the unit of amount due, **payments** settle the check, and closing the check completes and records the transaction.

Its defining core is small:

```text
Configured menu (items · prices · customization options)
└── Order — composed by staff on the restaurant's own transaction surface
    └── Check / tab — the accumulating settlement unit
        └── Payment(s)
        └── Controlled closure
```

Three properties hold jointly. Remove menu-configured staff order entry and what remains is a payment terminal, a cash register, or a customer self-service channel. Remove the check as an accumulating settlement container and what remains is a stream of immediate paid sales — retail sale semantics — or a kitchen ticket with no money. Remove payment-and-closure and what remains is order entry that never settles.

Everything commonly associated with modern restaurant POS — tables and floor plans, covers and seats, courses, tips, kitchen routing, cash drawers, dayparted menus, online-order integration, loyalty — is widespread in current products but is not part of the defining core. Older and differently-shaped implementations fit the same definition: the paper guest check written from a printed menu and settled at a cash drawer, and the fixed-workstation terminal generation still in service in many operations, both satisfy the core without any cloud, tablet, or integrated-payment requirement.

The Type's edges are sharp. When the composing actor becomes the customer on the customer's own surface, the product is drifting toward Restaurant Online Ordering or Self-service Restaurant Ordering. When the center becomes the plan-to-actual management loop rather than the live transaction, it is a Restaurant Management System. When the sale completes at the moment of payment with no open settlement container, it is Retail POS sale semantics.

## Users & Context

Primary users are the service staff who turn guest requests into transactions:

- **server** — creates and modifies table-service orders, courses items, presents and splits checks
- **counter / cashier staff** — builds quick-service orders and takes payment at the register
- **bartender** — maintains open tabs and beverage orders

Secondary users:

- **shift manager / manager on duty** — handles overrides, comps, voids, refunds, drawer access, and end-of-day closeout
- **administrator / owner** — configures the menu that reaches the ordering screens, permission sets, and operational settings

The work environment is the service floor itself: shared devices used at high pace during service, staff signed in with individual credentials or passcodes, and the transaction moving with the guest from order to fulfillment to settlement. An order is commonly started on one device and updated from another.

## Core Model

### The defining core

**Menu-configured order entry.** An authorized employee composes the guest's request as an order by selecting from the operation's configured menu — items carrying prices, organized in groups, with customization options (modifiers) that change or constrain each item. The menu configuration is what makes the transaction a restaurant transaction: the same surface without it is a payment terminal. Items not on the menu (for example a corkage charge) exist in some products as permission-gated exceptions, not as the primary path.

**The check as the accumulating settlement unit.** The order's charges — items, modifiers, taxes, adjustments — accumulate on a check (also called a tab or guest check) that is the unit of amount due. The check persists until settled: it can stay open across a service period, and while open it is subject to surgery — items added, discounted, comped, voided, moved between checks or guests, checks split, merged, or transferred between servers.

**Payment and controlled closure.** Payments settle the check, in full or across splits. Closing the check completes and records the transaction. Closure is gated: the balance must be settled, and the exceptions around it (voids, refunds, reopening) are permission-gated.

A useful conceptual reading separates the two central objects:

```text
Order = what must be fulfilled
Check = what must be settled
```

Products differ in how explicitly they draw this line. In the clearest articulations a single order contains one or more checks — a party of guests paying separately produces multiple checks on one order. In other products the two words are used interchangeably. The conceptual split holds across the researched sample even where the vocabulary does not.

### Standard capabilities

Mature products commonly carry most of the following. They are not what makes the product a Restaurant POS, but they make it operable in a live restaurant.

- **Service context on the order** — dining options (dine-in, takeout, delivery, curbside), the responsible server, tables organized in a floor plan, covers and seats, courses. Ownership travels with the check and can be transferred (change server, reassign, transfer checks).
- **Kitchen routing** — items carry routing targets (prep stations, item categories, kitchen printers, kitchen display screens); send/fire/hold semantics control when the kitchen begins preparation; coursing sequences multi-course service.
- **Money adjustments** — discounts, comps, voids with reasons, service charges, gratuities and tips (region-dependent), price overrides — all permission-gated.
- **Check surgery** — split checks, split payments, merge checks, move items between checks, guests, or seats, transfer checks between servers.
- **Order lifecycle** — conceptually open → paid → closed, with exact states and labels varying by product and tender; closed checks can be reopened in some products; refunds and voids after closure are controlled actions.
- **Cash management** — cash drawers assigned and opened under permission, drops and paid-outs recorded, and the service day ending in a closeout that reconciles cash and checks.
- **Roles and permissions** — job- or role-based permission sets; sensitive actions (voids, comps, refunds, discounts, drawer access) gated behind manager override or passcode; access to whole surfaces (table service, quick order, kitchen, payment terminal) granted per role.
- **Availability control** — items can be marked unavailable at the point of sale (the industry's "86"), with some products tracking quantity on hand.
- **Receipts and reporting** — guest receipts, order and sales reporting, server and end-of-day reports.
- **Offline resilience** — some cloud-era products continue to take orders and payments during connectivity loss and process them on reconnect.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:          the operational menu catalog
Implementations:  published from a menu-management back office, edited in the
                  POS's own administration surface, dayparted menu sets

Concept:          the settlement container
Implementations:  check, tab, guest check, bill

Concept:          kitchen routing target
Implementations:  prep stations, item categories, kitchen printers, KDS screens

Concept:          the money rail
Implementations:  integrated native card processing, third-party processors
```

A reader who has only seen a cloud-tablet product should still be able to recognize the fixed-workstation terminal generation — or the paper guest check — as the same Type from this core.

## How It Works

### Full-service table workflow

```text
Sign in
→ select table / party (open or create the order)
→ add items with modifiers
→ send / fire the order to the kitchen
→ add later courses as the meal progresses
→ present the check
→ split or adjust if needed
→ take payment (one or more tenders)
→ close the check
```

The table, covers, and course context are central here; the check lives open for the length of the meal.

### Quick-service workflow

```text
New order
→ add items with modifiers
→ take payment
→ close
→ order routes to fulfillment
```

Pay-first compresses the timeline — the check is created and closed in one motion — but the structure is the same: menu-configured order, settlement, closure. Handhelds used to capture orders in line are a common quick-service pattern.

### Bar / tab workflow

```text
Open a tab (commonly against a card pre-authorization)
→ add drinks across the visit
→ settle and close the tab
```

### Where the work goes

Sending the order routes it to the kitchen: items reach the prep station, printer, or display screen configured for them, and the kitchen's production workflow takes over on the fulfillment side. Payment settles the check; the closeout records the transaction into the day's sales.

### Core vs standard vs optional

**Defining core** — without these, not a Restaurant POS:

- menu-configured order entry by staff
- the check as the accumulating settlement unit
- payment and controlled closure

**Standard capabilities** — present in most mature products:

- service context (dining options, tables, covers, seats, courses, server ownership)
- kitchen routing with send/fire/hold and coursing
- money adjustments (discounts, comps, voids, service charges, tips) under permission
- check surgery (split, merge, move, transfer)
- order lifecycle with reopen/void/refund handling
- cash drawers, shift review, end-of-day closeout
- role-based permissions with manager overrides
- availability control, receipts, reporting

**Optional / variant** — depends on segment, region, scale, and packaging:

- bundled customer channels (online ordering, kiosk, QR, delivery dispatch)
- guest commerce modules (loyalty, gift cards, house accounts, customer credits)
- reservations/waitlist integration; hotel PMS posting at the hotel-F&B pole
- inventory, waste, and labor modules fed by POS sales
- multi-location configuration (shared menus, inheritance, local edit rights)
- fiscal compliance machinery (country-specific invoicing declarations)
- hardware form (tablet/handheld, fixed workstation, phone)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Order entry screen

The main transaction-building surface.

- typical information: menu categories and items, the current order/check with running totals, applied modifiers, dining option and table context
- primary actions: add item, modify item, adjust quantity, apply discount or void where permitted, send/hold/fire, proceed to payment

### Table / floor plan

The full-service entry surface mapping physical tables to active checks.

- typical information: table status, open checks per table, covers
- primary actions: select table, open order, set covers, move or merge checks

### Open checks / tabs

The list of transactions still financially or operationally open.

- typical information: check identifier, server, table, amount, age
- primary actions: reopen, add items, transfer, split, settle

### Payment / checkout

- typical information: amount due, tender options, split options, tip entry where customary, receipt action
- primary actions: take payment (full or split), apply tip, print or send receipt, close

### Orders hub

Common in multi-channel products: a consolidated view of orders from all sources — staff-entered, online, scheduled — in one stream the staff works from.

### Administration / back office

- typical information: the menu catalog with prices and modifier groups, permission sets, tax and service-charge configuration, device and station setup
- primary actions: edit and publish menu changes, manage employees and permissions, configure printers and routing, run end-of-day

### End-of-day / shift review

- typical information: open checks remaining, cash expected vs counted, tips and gratuities due, sales totals
- primary actions: close remaining checks, reconcile drawers, run and file the closeout report

## Important Rules / Behaviors

### The check is the settlement container

The check persists until settled and is editable while open. Closure normally requires the amount due to be satisfied; exceptions (comp the balance, void and close) are permission-gated. This open-container semantics is the Type's signature: it is what separates a restaurant transaction from an immediate paid sale.

### Money movement is permission-gated

Voids, comps, refunds, discounts, price overrides, drawer access, and no-sales each carry their own permission in mature products, typically exercised by managers. Comped and voided items commonly remain visible in sales and inventory reporting rather than disappearing.

### Lifecycle states are conceptual; labels are not universal

Open → paid → closed is the conceptual lifecycle; exact state names, and whether "paid" is a distinct state, vary by product and tender. Some products allow reopening a closed check; some restrict or archive orders after a period.

### The POS consumes the menu of record

Menu maintenance lives in an administration or menu-management surface; changes must be published or synced before they appear on the ordering screens. The POS holds the operational catalog that drives order entry; it does not own catalog maintenance as its center.

### Sales feed the siblings

Each closed sale is the depletion input for inventory and the raw input for management reporting. The POS does not own the stock record or the plan-to-actual control loop; it feeds them.

### Availability is controlled at the point of sale

Marking an item unavailable (86) is a live, in-service action taken on the ordering surface, distinct from the inventory system's stock record.

### Offline behavior

In products that support it, orders and payments captured during connectivity loss are processed when connectivity returns — evidence that payment processing is a separate concern from the transaction itself.

## Variants

Common service-model variants — these share the same transaction core and differ in which standard capabilities are emphasized:

- **full-service** — tables, covers, seats, courses, and server ownership central
- **quick-service / fast casual** — counter ordering, pay-first, line capture
- **bar / nightlife** — open tabs, card pre-authorization, tip-heavy settlement
- **café / bakery / food truck** — small menus, high transaction rate, single-device operation

Packaging and posture variants:

- **standalone POS vs suite-anchored POS** — the same transaction core either alone or bundled with management, channels, and guest commerce; bundling does not change the Type
- **hardware form** — tablet/handheld, fixed workstation, or phone app; form factor is not definitional
- **payment posture** — integrated native processing vs third-party processors
- **regional machinery** — tipping and gratuity handling in some markets; fiscal invoicing declarations in others
- **hotel F&B pole** — meal charges posted to the guest's hotel folio through a property-management integration

A variant remains a variant unless it changes the core: if the composing actor becomes the customer, or the open settlement container disappears, the product has become one of the neighboring Types instead.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Retail POS | adjacent, same spine | immediate paid sale + returns; no open settlement container or service context. Vendors ship both as modes of one product — the boundary is sale semantics, not structure |
| Restaurant Management System | broader, often bundled | the plan-to-actual management layer (menu economics, labor, purchasing, cost targets); the POS is the transaction surface it consumes actuals from |
| Restaurant Online Ordering | adjacent, customer-side | the customer composes the order on the customer's own surface; online orders land in the POS order stream, but composing actor and surface differ |
| Self-service Restaurant Ordering | adjacent, customer-side | customer-operated venue device (kiosk); the POS is staff-operated |
| Kitchen Display System / KDS | downstream | fulfills what the POS routes; kitchen production is its center; it captures no orders and takes no payment |
| Restaurant Menu Management | upstream sibling | owns the menu of record (catalog maintenance, pricing strategy, publication); the POS consumes the published catalog |
| Restaurant Inventory Management | sibling, fed by POS | owns the stock record (counts, receiving, valuation); the POS sale is its depletion input |
| Restaurant Reservation Platform | upstream, adjacent | commits a table at a time; the POS runs the meal transaction once the party arrives |
| Restaurant Delivery Management | adjacent | courier assignment and delivery execution; the POS may capture the order and hand it off |
| Payment Processing Platform / Gateway | underlying service | moves the money; the POS orchestrates the transaction and records tenders. Integrated processing is common but not definitional |

The most important boundary is with **Retail POS**: the two Types share the entire transaction spine (catalog-configured order → transaction → payment) and differ in sale semantics — the open, surgically editable settlement container between order and payment. The boundary is semantic rather than structural, and a single vendor commonly ships both as pre-configured modes of one product.

## Representative Products

- Toast — restaurant-native POS platform (SMB through enterprise)
- Square for Restaurants — generalist POS vendor's restaurant edition
- Oracle Simphony (MICROS line) — enterprise/legacy-lineage workstation generation
- SpotOn Restaurant — payments-led POS for independent restaurants

The core model was checked against the fixed-workstation terminal generation and against paper-era practice (handwritten guest check, cash drawer, manual closeout) to avoid defining the Type by the current cloud-tablet generation.

## Sources

Research date: **2026-09-09**

- Toast — Platform guide (orders, order states, menu hierarchy, permissions, glossary): https://doc.toasttab.com/doc/platformguide/index.html
- Square for Restaurants — Support Center (setup, menus, modes, checks): https://squareup.com/help/us/en/article/6407-get-started-with-square-for-restaurants
- Oracle Simphony — Help Center (POS user guide, workstation operations): https://docs.oracle.com/en/industries/food-beverage/simphony/index.html
- SpotOn Restaurant — Help center (front-of-house concept index): https://help.spoton.com/page/spoton-restaurant.md

> Sourcing limitations: SpotOn's article bodies did not render (dynamic content) — its evidence is index-level (concept set), and no procedural claims rest on it. Oracle Simphony was fetched at guide-preface/workstation-chapter depth, not article depth. Lightspeed Restaurant was unreachable (403 / transport errors) after repeated attempts and was abandoned; the European hospitality-POS pole is under-observed. Precise numeric limits, default timings, and product-specific state names are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary decisions are recorded in the paired Research Notes.
