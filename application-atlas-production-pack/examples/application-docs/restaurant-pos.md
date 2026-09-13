# Restaurant Point of Sale

## Overview

A **Restaurant Point of Sale (Restaurant POS)** is an operator-facing transaction application used to turn a guest's food-and-beverage request into a controlled restaurant order, check and payment.

Its stable core is:

```text
Menu
→ Order
→ Restaurant service context
→ Check / Tab
→ Payment
→ Closure
```

What distinguishes it from a generic Retail POS is the restaurant-specific context around the transaction: modifiers, dining options, tables, guests/covers, seats, courses and tabs may all influence how an order is constructed and fulfilled.

A Restaurant POS may be part of a much broader restaurant suite, but payroll, deep inventory, marketing, delivery dispatch and loyalty do not define the Type.

## Users & Context

Typical primary users include:

- **server** — enters and modifies table-service orders
- **cashier / counter staff** — builds quick-service orders and takes payment
- **bartender** — maintains tabs and beverage orders

Secondary users include:

- **shift manager** — performs overrides, comps, voids and exception handling
- **administrator / restaurant manager** — configures menu, permissions and operational settings

The software is used at the point where restaurant service becomes a transaction that must be accurately priced, fulfilled and settled.

## Core Model

### Menu → Item → Modifier

The **Menu** defines what can be sold.

A **Menu Item** is a sellable food or beverage item.

A **Modifier / Option** changes or constrains the item:

```text
Burger
├── cooking temperature
├── cheese
├── side
└── extra toppings
```

Modifiers are important because restaurant products are often configurable rather than fixed SKU-like items.

### Order

The **Order** represents what the guest has requested.

It may carry restaurant-specific service context such as:

- dine-in / takeaway / delivery
- table
- party size / covers
- seat
- course

### Check / Tab

A **Check** or **Tab** represents the amount owed in a settlement context.

Order and Check are closely related but should not always be treated as identical.

A useful conceptual distinction is:

```text
Order = what must be fulfilled
Check = what must be settled
```

A single operational session may involve:

- one order and one check
- split checks
- multiple payments
- an open tab

### Payment

A **Payment** settles part or all of a check.

This makes the financial end of the transaction explicit:

```text
Check
→ Payment(s)
→ amount due satisfied
→ close
```

## How It Works

### Full-service table workflow

```text
Staff login
→ select table / party
→ create or open order
→ add items
→ apply modifiers / seats / courses
→ send/fire order
→ add later items as needed
→ open check/payment
→ split if needed
→ collect payment
→ close
```

Here the table and guest-service context are central.

### Quick-service workflow

```text
New order
→ add items
→ apply modifiers
→ choose dining option
→ collect payment
→ send for fulfillment
```

The same transaction model is present, but table/seat/course semantics may disappear.

### Core vs common vs optional

**Core**

- menu/item selection
- order construction
- item customization/modifiers
- check/tab amount due
- payment
- closure

**Common**

- dining options
- tables/floor plan
- covers/seats
- courses
- discounts/comps
- split checks/payments
- tips
- receipts
- order history

**Optional / adjacent suite capabilities**

- online ordering
- delivery dispatch
- KDS
- loyalty
- deep inventory
- labor/payroll
- advanced analytics

## Interfaces

### Order Entry

The main transaction-building surface.

Typical layout includes:

- menu categories/items
- current order/check
- totals
- context-sensitive actions

Primary actions:

- add item
- modify item
- adjust quantity
- apply service context
- send/hold/fire
- discount/void where permitted
- proceed to payment

### Table / Floor Plan

Common in full-service operation.

It maps physical service resources to active checks/orders.

A staff member may begin by selecting:

```text
Table
→ party/covers
→ active order
```

### Open Checks / Tabs

Shows transactions that are still financially or operationally open.

This is particularly important in bars and table service.

### Payment / Checkout

Shows:

- amount due
- payment methods
- split options
- tip/receipt context
- closure action

### Order Hub / Orders

Multi-channel products may consolidate:

- dine-in
- takeout
- scheduled
- online
- delivery

This is common but not required to define POS core.

## Important Rules / Behaviors

### Order/check lifecycle

A safe canonical high-level lifecycle is:

```text
Open
→ Active / Sent
→ Paid
→ Closed
```

Products differ in whether `Paid` and `Closed` are separate states.

### Restaurant constraints

Typical rules include:

- a modifier may be required or limited
- menu availability may depend on time/location/channel
- voids, comps or refunds may require elevated permission
- full closure normally requires the amount due to be settled
- full-service flow may require table/party context

### Permissions

A common operational distinction is:

```text
Server / Cashier
→ normal order & payment

Manager
→ void / comp / refund / override

Admin
→ menu / permissions / configuration
```

### Important edge cases

- item becomes unavailable after order starts
- guest moves tables
- checks are split or merged
- partial payment
- open card tab / preauthorization
- void after item has been sent
- refund after closure
- online order enters the same operational queue

## Variants

Common workflow variants:

- full-service restaurant POS
- quick-service restaurant POS
- bar POS
- cafe POS
- food-truck POS

These normally share the same transaction core and should not automatically become separate canonical Types.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Retail POS | generic product/cart transaction; restaurant service semantics are not primary |
| Restaurant Management System | broader operational suite beyond point-of-sale transaction |
| Kitchen Display System | kitchen production and fulfillment are primary |
| Restaurant Online Ordering | customer-side remote order capture is primary |
| Restaurant Inventory Management | ingredients/stock/control are primary |

## Representative Products

- Toast POS
- Square for Restaurants
- Lightspeed Restaurant

## Sources

Research date: **2026-09-05**

Primary research sources:

- Toast — Ordering Screens  
  https://support.toasttab.com/en/article/New-POS-Experience-Ordering-Screens
- Toast — Managing Payments  
  https://support.toasttab.com/en/article/New-POS-Managing-Payments?lang=en_US
- Toast — Starting / Sending an Order  
  https://support.toasttab.com/en/article/Starting-Sending-an-Order
- Toast — Orders API Overview  
  https://doc.toasttab.com/openapi/orders/overview/
- Square — Get started with Square for Restaurants  
  https://squareup.com/help/us/en/article/6407-get-started-with-square-for-restaurants
- Square — Create menus with Square for Restaurants  
  https://squareup.com/help/us/en/article/6424-create-menus-with-square-for-restaurants
- Square — Take orders tableside  
  https://squareup.com/help/us/en/article/8152-take-orders-tableside-with-square-for-restaurants-mobile-pos

See the paired Research Notes for detailed evidence and boundary decisions.
