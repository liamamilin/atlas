# Research Notes — Restaurant Point of Sale

## Research Goal

Understand the stable operational core of a Restaurant POS and distinguish it from generic Retail POS, Restaurant Management Systems, online ordering and kitchen-production systems.

## Initial Boundary

Target:

> Restaurant Point of Sale

Working hypothesis:

> Restaurant POS is a restaurant-specific transaction system centered on constructing an order/check from a menu, applying dining-service semantics, taking payment and closing the transaction.

## Research Questions

- What is the difference among Menu, Item, Modifier, Order and Check?
- How does full-service table ordering differ from quick-service ordering?
- Which restaurant-specific concepts distinguish this from Retail POS?
- What does payment close?
- Which actions require manager permission?
- What order states are truly POS core versus off-premise fulfillment extensions?
- Which adjacent restaurant modules are bundled but not defining?

## Representative Products

| Product | Why selected |
|---|---|
| Toast POS | restaurant-native POS with explicit order/check/table workflow |
| Square for Restaurants | major alternative spanning full-service, quick-service and bar operation |
| Lightspeed Restaurant | additional market anchor for restaurant-oriented POS structure |

Primary detailed evidence used: Toast + Square.

## Sources

Research date: 2026-09-05

### Toast

- Ordering Screens  
  https://support.toasttab.com/en/article/New-POS-Experience-Ordering-Screens
- Managing Payments  
  https://support.toasttab.com/en/article/New-POS-Managing-Payments?lang=en_US
- Starting / Sending an Order  
  https://support.toasttab.com/en/article/Starting-Sending-an-Order
- Order Hub Overview  
  https://support.toasttab.com/en/article/Order-Hub-Overview
- Orders API Overview  
  https://doc.toasttab.com/openapi/orders/overview/

### Square

- Get started with Square for Restaurants  
  https://squareup.com/help/us/en/article/6407-get-started-with-square-for-restaurants
- Create menus with Square for Restaurants  
  https://squareup.com/help/us/en/article/6424-create-menus-with-square-for-restaurants
- Take orders tableside  
  https://squareup.com/help/us/en/article/8152-take-orders-tableside-with-square-for-restaurants-mobile-pos
- New order and pay capabilities  
  https://squareup.com/help/us/en/article/8421-new-order-and-pay-capabilities-with-square-for-restaurants

## Product Observations

### Toast

Observed visible concepts:

- menu/group/item
- modifier
- order
- guest check
- table
- seat/course context
- payment
- open/paid/closed operational concepts
- off-premise order hub

Toast's order model is particularly useful for confirming that **Order**, **Check** and **Payment** are related but conceptually distinct.

### Square for Restaurants

Observed concepts:

- menu/menu groups/items
- floor plan/table
- guests/covers
- order
- checkout/payment
- full-service / quick-service / bar workflows

This supports a shared transaction core with different service-mode interfaces.

## Cross-product Comparison

| Finding | Toast | Square Restaurants | Canonical decision |
|---|---|---|---|
| menu/item catalog | yes | yes | Core |
| item options/modifiers | yes | yes | Core/Common |
| order transaction | yes | yes | Core |
| check/tab/payment context | yes | yes | Core |
| payment/closure | yes | yes | Core |
| table/floor plan | yes | yes | Common; core for full-service variant |
| guests/covers | yes | yes | Common; full-service |
| quick-order mode | yes | yes | Common; quick-service variant |
| split payment/check | yes | supported | Common |
| online/delivery orders | yes | yes | Common/bundled |
| KDS | ecosystem/module | ecosystem/module | Adjacent |
| payroll | broader suite | not defining | Optional |
| deep inventory | broader suite | broader suite | Optional/adjacent |

## Canonical Model

The defining transaction structure is:

```text
Menu
├── Item
│   └── Modifier / Option
│
↓ selected into

Order
├── service context
│   ├── dining option
│   ├── table
│   ├── seat
│   └── course
│
└── Check / Tab
      └── Payment(s)
            ↓
          Closed
```

Not every product represents Order and Check identically, but the distinction is useful:

- **Order** — what the guest has ordered / what must be fulfilled
- **Check/Tab** — what is owed and settled
- **Payment** — settlement against the amount due

## Operational Loops

### Full-service

```text
table / party
→ order
→ send/fire
→ later additions
→ check
→ payment
→ close
```

### Quick-service

```text
order
→ item customization
→ dining option
→ payment
→ fulfillment
```

The two variants share the same transaction core but expose different service context.

## State Findings

A safe high-level canonical lifecycle:

```text
Open
→ Active / Sent
→ Paid
→ Closed
```

Exact product states differ.

Off-premise order states such as:

```text
Needs Approval
Scheduled
Ready
Completed
```

belong to channel/fulfillment extensions and should not be treated as universal POS states.

## Vendor-specific / Rejected Findings

Do not make these Restaurant POS core:

- payroll
- loyalty
- marketing
- delivery dispatch
- deep ingredient inventory
- advanced analytics

## Boundary Findings

### vs Retail POS

Restaurant POS adds service semantics such as:

- modifiers
- tables/covers/seats
- courses
- tabs/checks
- dining options

### vs Restaurant Management System

Restaurant Management is broader and may contain labor, inventory, purchasing, CRM and analytics.

### vs KDS

KDS centers on kitchen production/fulfillment after an order is sent.

### vs Online Ordering

Online Ordering centers on customer-side remote order capture.

## Uncertainties

- Order vs Check object boundaries vary by product
- “Paid” and “Closed” may be one or two states depending on system
- table/seat/course concepts are not universal in quick-service operation

## Final Synthesis

Canonical Restaurant POS:

```text
restaurant transaction
=
menu-configured order
+ service context
+ check/tab
+ payment
+ controlled closure
```
