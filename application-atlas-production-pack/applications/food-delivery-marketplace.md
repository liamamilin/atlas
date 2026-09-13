# Food Delivery Marketplace

## Overview

A **Food Delivery Marketplace** is a third-party platform that aggregates many independent prepared-food sellers on a single consumer surface, lets consumers place menu-based orders with one seller at a time, transmits each order to that seller as a fulfillment instruction, and coordinates the order's completion outside the restaurant — most commonly delivery by courier to the consumer's address, with consumer pickup as a widely supported alternative.

The defining structure is small:

```text
Third-party aggregation of many independent sellers
└── Order of record (consumer-composed, menu-based, bound to one seller)
    └── transmitted to that seller for fulfillment
        └── off-premises completion: delivery to an address or consumer pickup
            └── handoff of prepared food to the consumer
```

Everything commonly associated with modern food delivery platforms — an app-based courier network with live map tracking, platform-captured cashless payment, layered checkout fees, ratings, memberships, promotions, and expansion into groceries or convenience items — is widespread in current products but is not part of the defining core. Older and regional marketplace forms that merely list restaurants and forward orders to them, with the restaurant handling delivery or collection itself, satisfy the same definition.

When the surface stops aggregating multiple sellers on behalf of a third party, the product has drifted toward a different Application Type (most importantly Restaurant Online Ordering).

## Users & Context

Three user populations meet in the product, each with its own surface:

- **Consumer** — browses the marketplace, composes and pays for an order, follows its progress, receives the food, and reports problems. Motivated by wanting a specific meal from a specific nearby seller without visiting it.
- **Seller operator (restaurant partner)** — receives orders as fulfillment instructions, confirms or rejects them, manages menu content and item availability, and hands prepared food to the courier or the consumer. Motivated by incremental sales volume without building their own ordering channel.
- **Courier** (present in the courier-network model) — receives delivery offers, picks up prepared food from sellers, and delivers it to consumers. Motivated by delivery earnings. In seller-delivery forms this population is the restaurant's own staff and has no platform surface.

Secondary participants: the marketplace operator's support staff (adjudicating refunds, late orders, and disputes) and seller administrators (menu and store configuration). The consumer surface is mobile-first in current products; seller and courier surfaces are commonly separate applications because their users, contexts, and working rhythms differ completely.

## Core Model

### The Defining Core

Three structures. They only make sense together; each one's absence collapses the product into a different Application Type:

- **Multi-seller aggregation.** Many independent prepared-food sellers, each with its own identity and its own menu, are presented on one consumer surface operated by an entity that is not the food seller. This is what makes the product a marketplace rather than a single restaurant's ordering channel.
- **The order of record.** The consumer composes an order out of one seller's menu — items plus per-item selections — and the platform records it and transmits it to that seller as the instruction it fulfills. The platform is the channel of record for the order, not a directory or an advertising surface. This is what makes it a marketplace rather than a listings or review platform.
- **Off-premises fulfillment coordination.** The order carries fulfillment terms — delivery to an address, or consumer pickup — and completes as a handoff of prepared food outside the restaurant premises. The platform coordinates the order from placement to that handoff. The coordination can be thin (the seller receives the order with its terms and completes delivery itself) or deep (the platform assigns couriers, tracks the delivery, and manages the handoff). This is what makes it a food-fulfillment system rather than a generic goods shop.

If the aggregation is removed, what remains is Restaurant Online Ordering. If the order of record is removed, what remains is a listings/discovery platform. If off-premises fulfillment is removed, what remains is in-restaurant order taking or a generic e-commerce checkout.

### Standard Capabilities of Mature Products

These are not what makes the product a food delivery marketplace, but they make it work at market expectations:

- **Seller acceptance** — incoming orders are confirmed or rejected by the seller (closed, too busy, items unavailable); unavailable items are handled rather than silently fulfilled.
- **Menu structuring** — categories, item descriptions, pricing, and per-item customization (options, add-ons, exclusions), with availability toggling when an item runs out.
- **One-seller carts** — an order is built from a single seller's menu; combining several sellers in one cart is uncommon.
- **Layered checkout fees** — the food subtotal is joined by delivery-related and service-related fees and an optional tip, disclosed before payment; the exact layering varies by product and market.
- **Payment and payouts** — the platform commonly captures the consumer's payment and remits to sellers net of commission; historical and regional forms in which the seller collects payment also exist.
- **Order status visible to the consumer** — a progression from confirmation through preparation to delivery and completion, with the exact labels varying by product.
- **Courier allocation and tracking** (courier-network model) — delivery offers are accepted by couriers, nearby orders may be batched, and the consumer commonly sees live location and an estimated arrival.
- **Seller portal** — order queue, menu and availability management, store hours and preparation settings, payout statements.
- **Courier app** — offer queue, pickup/navigation/handoff steps, earnings view.
- **Ratings** — order-linked ratings for sellers and, in courier models, for the delivery experience.
- **Support and remediation** — reporting of missing or incorrect items, refunds or credits, compensation for late orders, cancellations.
- **Discovery machinery** — search, cuisine filters, distance/ETA/rating sorts, saved addresses, reorder from history.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Different products realize each concept differently:

```text
Concept:              Off-premises fulfillment
Implementations:      platform-operated courier network; seller's own delivery staff;
                      consumer pickup; (regionally) call-center-assisted delivery

Concept:              Order transmission to the seller
Implementations:      real-time order queue in a seller portal/tablet; automated acceptance;
                      historically: fax/phone/email forwarding

Concept:              Consumer payment
Implementations:      platform-captured cashless payment; seller-collected payment;
                      (regionally) cash on delivery
```

A reader who has only seen a courier-network product should still recognize an older seller-delivery marketplace as the same Application Type — and vice versa.

## How It Works

### Discover and choose a seller

```text
Open the marketplace surface
→ search or browse (cuisine, distance, rating, delivery estimates)
→ open a seller's page
→ review menu, ratings, fulfillment terms
```

### Build the order

```text
Select menu items
→ choose per-item customizations
→ add to cart (one seller per order)
→ review the cart
```

### Check out

```text
Choose fulfillment mode (delivery to an address, or pickup)
→ provide or select the address / pickup time (now or scheduled)
→ review the fee breakdown
→ pay
→ place the order
```

### Seller receives and confirms the order

The order is transmitted to the seller as a fulfillment instruction. The seller confirms it — or rejects it, or adjusts it when items are unavailable — and the consumer sees the resulting status. In mature products this step is commonly automated for well-stocked menus, with manual handling as the fallback.

### Prepare, allocate a courier, and deliver

- **Courier-network model:** while the seller prepares, the platform allocates a courier (offer → accept), the courier collects the prepared food at handoff, and the consumer follows live progress to the door.
- **Seller-delivery model:** the seller dispatches its own means of delivery; the consumer typically sees a thinner status picture.
- **Pickup:** the consumer collects at the seller's location when the order is ready.

### Complete and remediate

```text
Handoff of prepared food to the consumer
→ order marked complete
→ optional rating (seller; delivery quality where a courier network exists)
→ problems raised afterwards: missing/incorrect items, late delivery → refund or credit adjudicated through the platform
```

### Core vs Common vs Optional

**Defining core** — without these, not a food delivery marketplace:

- third-party aggregation of multiple independent sellers
- consumer-composed, menu-based order of record bound to one seller, transmitted to that seller
- off-premises fulfillment (delivery or pickup) coordinated through to handoff

**Common mature structure** — present in most current products:

- seller acceptance/rejection, item customization, layered fees, platform payment with seller payouts, consumer-visible order status, ratings, support/refund flows, discovery and reorder machinery
- courier allocation, batching, live tracking (courier-network model)

**Optional / variant** — depends on model, market, and business posture:

- subscription memberships for delivery-fee reduction
- promoted placement and advertising products
- non-restaurant verticals (grocery, convenience, alcohol)
- delivery-only kitchens and virtual brands as sellers
- white-label ordering/delivery services sold to chains
- regional payment forms (cash on delivery, local wallets), call-center-assisted ordering
- group ordering, corporate or campus networks, autonomous delivery experiments

## Interfaces

The following surfaces are described conceptually; layouts, names, and state labels vary by product.

### Consumer marketplace surface (mobile app / web)

The consumer's primary entry.

- discovery: search, cuisine and filter browsing, seller cards with rating, distance, and fulfillment estimates
- seller page: menu with categories and prices, customization options, ratings and reviews, fulfillment terms
- cart and checkout: order contents, fulfillment mode, address, scheduled time, fee breakdown, payment
- order tracking: status progression, and in courier models live map position and estimated arrival
- history and reorder; support surface for problems and refunds

Primary actions: search, configure items, check out, pay, track, rate, request remediation.

### Seller portal (web / tablet)

The seller's working surface during service hours.

- order queue: incoming orders with contents and fulfillment terms; accept/reject; preparation state
- menu management: items, categories, prices, customization options
- availability management: sold-out toggling, store hours, preparation-time settings
- payouts: statements, commission and remittance history

Primary actions: accept/reject order, mark readiness, adjust menu and availability, review payouts.

### Courier app (mobile, courier-network model)

The courier's working surface.

- offer queue: proposed deliveries with pickup and drop-off locations; accept/decline
- active delivery: pickup at seller, navigation, handoff to consumer, proof-of-completion steps
- earnings: per-delivery earnings view, commonly including customer tips

Primary actions: accept offer, confirm pickup, navigate, confirm handoff, view earnings.

### Support / operations surface

Used by the marketplace operator's staff to adjudicate refunds, late orders, and disputes, and to manage the seller base. Details are operator-facing and vary widely; the consumer-visible part is the refund/compensation outcome.

## Important Rules / Behaviors

- **Seller availability governs everything upstream of it.** Outside a seller's hours the seller is not orderable; a sold-out item is removed or disabled; a seller can reject an order it cannot fulfill. The marketplace does not overrule the seller's fulfillment capacity.
- **One seller per order.** The order of record is bound to a single seller's menu; this keeps preparation, acceptance, and fulfillment attributable. Multi-seller carts are uncommon precisely because they break that binding.
- **Fees are disclosed before payment.** The consumer sees the layered fee composition (food subtotal, delivery-related, service-related, tip) at checkout, before committing. Which fees exist and who funds them vary by product and market.
- **Payment and status are the coordination backbone.** The consumer's payment and the order's status progression are the platform's own records; sellers and couriers act on order state rather than on side agreements. This is what makes the platform the channel of record.
- **Remediation is platform-adjudicated.** Missing items, incorrect items, late orders, and non-delivery are reported through the platform and resolved as refunds or credits through it — including when the failure was the seller's or the courier's. The platform's payment position is what makes this possible.
- **Cancellation gets harder as the order advances.** Orders can commonly be cancelled freely before confirmation; once the seller has accepted and preparation begins, cancellation depends on the seller and may carry fees. Exact windows vary by product.
- **Ratings are order-linked.** Seller ratings aggregate over completed orders; delivery ratings (where present) attach to the courier's handoff. This binds reputation to the transaction record.
- **Courier allocation is mediated, not commanded.** In courier-network models, couriers accept or decline proposed deliveries; the platform influences (through incentives and batching) rather than assigns unconditionally. This shapes delivery reliability and is a common source of delay.

## Variants

- **Courier-network pole** — the platform operates its own courier fleet as the dominant fulfillment mode; live tracking and batching are central; commission and fees fund the logistics.
- **Aggregator pole** — the platform's role is aggregation and order transmission; sellers fulfill with their own means or consumers collect; logistics and tracking are thinner. Historically the earlier and, in several markets, the continuing form.
- **Hybrid** — both modes offered per seller or per market; the consumer may see "delivered by restaurant" versus platform courier as a difference in tracking depth.
- **Super-app embedded** — food delivery is one vertical inside a broader consumer platform (mobility, payments, groceries); the marketplace structure is unchanged, the surface is shared.
- **Vertical-extended** — grocery, convenience, alcohol, or pharmacy orders ride the same marketplace machinery; prepared-food semantics blur toward scheduled goods delivery for those verticals.
- **White-label / infrastructure** — the operator sells ordering or delivery infrastructure to chains under the chain's brand; the same machinery appears as a vendor service rather than a consumer marketplace.
- **Regional forms** — cash on delivery, call-center-assisted ordering, and seller-collected payment persist in some markets; these change the payment and interaction layer, not the core.
- **Delivery-only kitchens** — sellers without a storefront operate entirely through the marketplace; from the platform's view they are ordinary sellers.

A variant remains a **Variant** unless it changes users, core objects, workflow, or rules so much that the defining core no longer applies — as happens, for example, when multi-seller aggregation is removed (Restaurant Online Ordering) or prepared-food semantics are removed (On-demand Delivery Platform).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Restaurant Online Ordering | one seller's own ordering channel (branded or white-label under the seller's identity); no multi-seller third-party aggregation. The closest seam. |
| On-demand Delivery Platform | generic courier platform for any goods; no menu, no seller preparation, no food-fulfillment semantics. |
| Multi-vendor Marketplace | generic goods e-commerce; fulfills by shipping rather than time-critical preparation and address-bound courier handoff of prepared food. |
| Restaurant Delivery Management | seller-side tooling for a seller's own delivery operations; no consumer marketplace surface. |
| Service Marketplace | sells services rather than prepared food; fulfillment is scheduled work, not a food handoff. |
| Ride-hailing Platform | shares dispatch mechanics (offers, tracking) but transports passengers, not menu-built orders; no seller/preparation side. |
| Kitchen Display System | in-kitchen production display; consumes orders created elsewhere; no consumer marketplace, no payment, no aggregation. |
| Listings / Review Platform | discovery without an order of record; nothing is transmitted to sellers for fulfillment. |

The boundary with Restaurant Online Ordering deserves emphasis because the two share "order prepared food for delivery or pickup". The structural test is aggregation: many independent sellers on a third-party surface (marketplace) versus one seller under its own identity (direct channel). White-label storefront services blur this commercially, but the consumer-facing ownership test still separates them.

## Representative Products

- DoorDash
- Uber Eats
- Deliveroo
- Just Eat

The set spans the two fulfillment models: the first three are commonly described as operating courier networks; Just Eat originates from the aggregator model in which restaurants fulfill orders themselves. The defining core was checked against that seller-delivery pole so that the definition does not over-fit to the courier-network pattern.

## Sources

Research date: **2026-09-08**

- DoorDash — consumer Help Center (https://help.doordash.com/) and product pages (https://www.doordash.com/)
- Uber Eats — product/merchant pages (https://www.uber.com/, https://www.ubereats.com/)
- Deliveroo — Help (https://deliveroo.co.uk/help)
- Just Eat / Just Eat Takeaway.com — Help (https://help.just-eat.co.uk/) and corporate site (https://www.justeattakeaway.com/)

> Sourcing limitation: none of the attempted vendor help centers, product pages, or third-party reference sources could be retrieved from the research environment on 2026-09-08 (HTTP 403/404/429 responses or timeouts; full failure log in the Research Notes). This document is therefore written at the level of the category's shared, stable structure, with deliberately reduced assertion strength: no precise operational values (fee amounts or percentages, time windows, default settings, exact state labels, or numeric limits) are stated, and product-specific mechanics are not attributed to named products. All precise claims that such sources would be needed to confirm are recorded as uncertainties in the Research Notes instead.
