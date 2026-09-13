# Research Notes — Food Delivery Marketplace

## Research Goal

Understand the Application Type "Food Delivery Marketplace" from real products and produce a vendor-neutral Application Document that explains what this type of software is, who uses it, what exists inside it, how work moves through it, and where its boundaries lie against adjacent Types (especially Restaurant Online Ordering, On-demand Delivery Platform, and generic Multi-vendor Marketplace).

## Initial Boundary

Working hypothesis before research:

- A Food Delivery Marketplace is a third-party platform that aggregates many independent prepared-food sellers, lets consumers place menu-based orders with one seller at a time, transmits each order to that seller for fulfillment, and coordinates completion of the order outside the restaurant premises — most commonly delivery by courier to the consumer's address, with consumer pickup as a widely supported alternative.
- Three user populations: consumers (order and pay), sellers/restaurants (accept, prepare, hand off), couriers (in the platform-courier model; absent or optional in the seller-delivery "aggregator" model).
- Closest confusable Types:
  - Restaurant Online Ordering — single-seller owned/branded ordering channel
  - On-demand Delivery Platform — generic courier platform without food ordering semantics
  - Multi-vendor Marketplace — generic goods e-commerce marketplace
  - Restaurant Delivery Management — seller-side delivery operations tooling
  - Service Marketplace — services rather than prepared food
- Obvious unknowns at the start:
  - whether platform-operated courier networks belong in the definition (aggregator products suggest not)
  - whether platform-captured payment belongs in the definition (historical seller-collected/cash models suggest not)
  - the exact shape of the order lifecycle and rejection/refund paths (documentation-dependent)

## Research Questions

1. What is the consumer's core loop: discovery → menu selection → cart → checkout → order → tracking → receipt?
2. What is the order lifecycle, including seller acceptance/rejection and cancellation paths?
3. How does the seller side work: onboarding, menu management, item availability, acceptance, preparation, payouts?
4. How does courier allocation work in the platform-courier model, and what does the seller-delivery model look like instead?
5. How does money move: consumer charges (food + fees + tip), seller commission, courier pay?
6. Which structures are shared by both fulfillment models (platform-courier vs seller-delivery), and which are model-specific?
7. What exceptions matter: sold-out items, rejected orders, late orders, missing/incorrect items, undelivered orders, refunds and compensation?
8. Where are the Type boundaries, and what removed from this Type turns it into each neighbor?

## Representative Products

Selected a priori on market standing, geographic spread, and differing fulfillment philosophy (not yet validated against documentation at selection time):

1. **DoorDash** — US-led market leader; logistics-heavy model operating its own courier network; also offers seller self-delivery participation and white-label delivery services.
2. **Uber Eats** — global platform; courier network shared with a ride-hailing background; marketplace plus logistics.
3. **Deliveroo** — UK/EU player; own rider network; subscription membership; grocery/convenience expansion.
4. **Just Eat** — UK/EU origin aggregator; historically a pure marketplace in which restaurants take orders and fulfill with their own means; later group operations include both marketplace and own-delivery forms. Included deliberately as the counter-pole to the logistics-heavy model, to keep the definition from over-fitting to the courier-network pattern.

Regional anchors considered and not individually researched: talabat/foodpanda (Middle East/Asia), GrabFood (SE Asia super-app), Swiggy/Zomato (India), Meituan/Ele.me (China).

## Sources & Access Limitation

Research date: 2026-09-08.

Every attempted source was unreachable from the research environment:

| Source | Attempted URL(s) | Result |
|---|---|---|
| DoorDash consumer Help Center | https://help.doordash.com/consumers/s/ | HTTP 403 |
| DoorDash Dasher signup page | https://www.doordash.com/dasher/signup/ | HTTP 403 |
| Just Eat UK Help Center | https://help.just-eat.co.uk/hc/en-gb | HTTP 403 |
| Just Eat Takeaway corporate site | https://www.justeattakeaway.com/ | HTTP 429 |
| Deliveroo Help | https://deliveroo.co.uk/help | HTTP 403 |
| Uber merchant page | https://www.uber.com/us/en/merchant/ | HTTP 404 |
| Wikipedia (DoorDash, Just Eat, Online food ordering) | en.wikipedia.org, en.m.wikipedia.org | timeout (repeated) |
| foodpanda corporate About | https://www.foodpanda.com/about/ | HTTP 403 |

**Consequences applied (per evidence rules):**

- Evidence Layer A (direct product observation) is **absent** for this pass. Nothing below may be read as product-verified.
- All model-level statements in the Research Notes and the Application Document are Layer B (cross-category commonality of the type as commonly described) or Layer C (canonical inference from type-boundary reasoning), and are written with hedged wording.
- No precise operational values are stated anywhere (no fee amounts or percentages, no time windows, no default settings, no exact state labels, no numeric limits), because no source supports that precision.
- The representative-product set was chosen for market standing a priori; product-level confirmation was not possible and is recorded as the principal uncertainty of this pass.

## Evidence Posture

Because official operational documentation could not be fetched, this pass relies on:

- **Layer B (cross-product commonality, degraded):** widely shared, category-level descriptions of how food delivery marketplaces work, stable across the sampled set as market knowledge. Suitable for Level 1 (common mature structure) statements with hedged wording ("mature products commonly...", "a typical implementation...").
- **Layer C (canonical inference):** abstraction derived from the type's own structure and boundary reasoning (e.g., the aggregator-vs-logistics axis proves that platform-courier operation cannot be a defining invariant). Suitable for the defining core, written as "the defining structure is...".

Any statement that would require product-specific precision has been either omitted or explicitly marked as unverified.

## Product Observations (market-standing level, not directly verified)

Evidence layer for everything below: **B/C (degraded)**. These are a priori market-standing observations retained only where they carry structural weight, not operational detail.

### DoorDash

- US-led marketplace; three-sided structure: consumers, restaurant partners, independent courier contractors.
- Platform operates its own courier network as the dominant fulfillment mode; seller self-delivery participation is also described.
- Broad surface set commonly described: consumer app, seller portal (order and menu management), courier app, plus operator-side services (white-label delivery for merchants, storefront services) and expansions beyond restaurant food.
- Subscription membership for delivery-fee reduction is described.
- Operational specifics (fee names and amounts, courier pay structure, batch sizes, compensation policies) — **unverified in this environment; deliberately not recorded**.

### Uber Eats

- Global marketplace riding on a ride-hailing background; courier network shared with ride-hailing supply.
- Same three-sided structure; strong live-tracking presentation commonly described.
- Subscription membership; grocery/convenience/alcohol expansion commonly described.
- Operational specifics — **unverified; not recorded**.

### Deliveroo

- UK/EU player; own rider network as dominant fulfillment mode.
- Consumer surface, rider app, and restaurant partner portal commonly described.
- Subscription membership; grocery/convenience expansion; dark-kitchen site operations commonly described.
- Operational specifics — **unverified; not recorded**.

### Just Eat

- Aggregator origin: historically a pure marketplace — the platform aggregated restaurants and forwarded orders; restaurants fulfilled themselves (their own drivers or consumer collection), and consumer payment historically could be settled outside the platform.
- Group operations later span both the marketplace form and own-delivery forms in different markets; this split across markets is the reason the defining core must not require platform-courier operation or platform-captured payment.
- Operational specifics — **unverified; not recorded**.

## Cross-product Comparison

Axes across the sampled set (all statements hedged; not product-verified):

| Axis | Logistics-heavy pole (DoorDash / Uber Eats / Deliveroo) | Aggregator pole (Just Eat heritage) | Reading |
|---|---|---|---|
| Multi-seller aggregation on one consumer surface | Yes (commonly described) | Yes (commonly described; the origin feature) | Defining for the Type |
| Consumer builds a menu-based order with one seller | Yes | Yes | Defining for the Type |
| Order transmitted to seller for fulfillment | Yes | Yes (historically forwarded by fax/phone/email in early forms) | Defining for the Type |
| Fulfillment off premises (delivery to address or consumer pickup) | Yes, delivery-dominant | Yes, delivery or collection | Defining for the Type |
| Platform-operated courier network | Yes, dominant | No (seller fulfills; own-delivery added in some markets later) | Model variant, **not** defining |
| Platform-captured consumer payment | Yes (commonly described today) | Historically not always (seller-collected/cash existed) | Common mature structure, not defining |
| Seller acceptance/confirmation step | Yes | Yes | Common mature structure |
| Order status visible to consumer | Yes | Yes (thinner in early forms) | Common mature structure |
| Fee layering at checkout (food + delivery-related fees + service-related fees + tip) | Yes | Yes (shape varies by model and market) | Common mature structure |
| Seller commission / payout mechanics | Yes | Yes | Common mature structure |
| Live map tracking + ETA | Yes, courier-network products | Not necessarily (no platform courier to track) | Model-dependent |
| Subscription membership | Yes | Yes | Variant/optional |
| Promoted placement / advertising inside search | Yes (commonly described) | Yes (commonly described) | Variant/optional |
| Non-restaurant verticals (grocery/convenience/alcohol) | Yes (commonly described) | Varies | Variant/optional |

**The load-bearing observation:** the two fulfillment models share the aggregation + order-transmission + off-premises-fulfillment structure and differ precisely in who performs delivery and how much logistics the platform operates. Therefore the shared structure is the definitional core, and the courier network is the common implementation of one pole.

## Canonical Model (abstraction levels)

### Level 0 — Defining Invariant

Three jointly-held structures. Removing any one collapses the product into a different Type:

1. **Third-party multi-seller food aggregation.** Many independent prepared-food sellers (restaurants in common usage; delivery-only kitchens operate through the same structure), each presented with its own identity and its own menu, on one consumer surface operated by an entity that is not the food seller. *Remove → single-seller ordering channel (Restaurant Online Ordering).*
2. **The order of record, built from a specific seller's menu and transmitted to that seller as a fulfillment instruction.** The consumer composes an order out of one seller's menu (with per-item selections), the platform records it, and the seller receives it as the instruction it fulfills. The platform is the channel of record for the order, not a mere advertiser. *Remove → directory / review / lead-generation platform.*
3. **Off-premises fulfillment coordination ending in handoff of prepared food to the consumer.** The order carries fulfillment terms (delivery to an address, or consumer pickup) and completes as a handoff of prepared food outside the restaurant premises; the platform coordinates the order from placement to that handoff. The coordination may be thin (aggregator: seller receives the order with its fulfillment terms and completes delivery itself) or deep (logistics pole: platform assigns couriers, tracks, and manages the delivery). *Remove → in-premises order taking (Restaurant POS territory), or generic goods marketplace without food-fulfillment semantics.*

Jointly-held is load-bearing:

- 1+2 without 3 → pre-order/goods-marketplace behavior with no food-fulfillment semantics.
- 2+3 without 1 → Restaurant Online Ordering (one seller).
- 1+3 without 2 → directory/listings/discovery platform (no order of record).

Deliberately **not** in Level 0 (each fails the historical/variant check):

- Platform-operated courier network (aggregator pole exists without it; fax-era order forwarding satisfies the core).
- Platform-captured cashless payment (seller-collected payment and cash models existed and arguably persist regionally).
- Live map tracking, ETA, app-based anything.
- Apps as such; web-only and even phone-assisted marketplace forms satisfy the core.
- Ratings, promotions, subscriptions.

### Level 1 — Common Mature Structure

Very common in current mature products; expected by the market but not definitional:

- Seller acceptance/confirmation of the incoming order, with rejection paths (closed, too busy, items unavailable) and automatic handling of unavailable items.
- Item-level customization (options/add-ons/exclusions per menu item) and menu structuring (categories, descriptions, pricing).
- One-seller-per-order cart behavior; multi-seller carts are rare.
- Checkout fee architecture layered on the food subtotal (delivery-related fee, service/platform-related fee, optional tip), disclosed before payment.
- Platform-captured payment with payouts to sellers net of commission; payment methods retained for reuse.
- Order status progression visible to the consumer (confirmed/preparing/on its way/delivered class of states; exact labels vary).
- Live map tracking and ETA in the courier-network model; courier allocation through offer/accept, batching of nearby orders, courier pickup and handoff steps.
- Seller portal: order queue, menu and availability management (sold-out toggling, hours, preparation-time settings), payout statements.
- Courier app: offer queue, pickup/navigation/handoff steps, earnings view.
- Order-linked ratings and reviews (seller, and in courier models courier/delivery quality).
- Support and remediation flows: missing/incorrect item reporting, refund or credit handling, late-order compensation, cancellation.
- Search/browse organization (cuisine filters, distance/ETA/rating sorts), saved addresses, reorder.
- Promotions (platform- or seller-funded discounts, free-delivery thresholds) and scheduled (future) orders.

### Level 2 — Variant / Optional Structure

Depends on market, geography, model, and business posture:

- Fulfillment model axis itself: platform-courier dominant, seller-delivery dominant, hybrid.
- Subscription memberships for delivery-fee reduction and perks.
- Promoted placement / advertising products sold to sellers.
- Vertical expansion: groceries, convenience, alcohol, pharmacy riding the same marketplace machinery.
- Dark/cloud kitchens and delivery-only virtual brands as sellers.
- White-label/branded ordering or delivery services sold by the platform to chains (platform becomes a vendor of ordering/delivery infrastructure).
- Regional payment forms: cash on delivery, local wallets; call-center-assisted ordering in some markets.
- Group ordering / bill-splitting; corporate or campus closed networks.
- Autonomous delivery (robots/drones) experiments.

### Level 3 — Vendor-specific Structure

Named programs, branded terminology, and proprietary fee/compensation constructions exist across the sampled set (membership program names, courier program names, named fee line items, white-label delivery brand names). Because no vendor documentation was reachable, **no specific vendor program, fee name, numeric policy, or default is recorded here**; the layer is acknowledged structurally and left unpopulated.

## Vendor-specific Findings

- See Level 3 above: the layer exists (every sampled product differentiates through branded membership/courier/fee constructions) but is unpopulated in this pass due to source-access failure.
- Model-axis positioning is the one vendor-differentiating dimension retained conceptually: which seller population the product starts from (restaurant-delivery heritage vs courier-network heritage) shapes its fee and tracking presentation. This is kept as a variant axis, not vendor detail.

## Boundary Findings

| Neighbor Type | Relationship | Sharpest seam / "remove what" test |
|---|---|---|
| Restaurant Online Ordering | closest seam | Marketplace aggregates many sellers on a third-party surface and owns the consumer relationship and order of record; direct online ordering is one seller's own channel (its branded site/app, or a white-label storefront operating under the seller's identity). Remove multi-seller third-party aggregation → Restaurant Online Ordering. |
| On-demand Delivery Platform | adjacent | Generic courier platform carries any goods/parcels with no menu, no seller preparation, no food handoff semantics. Remove menu-structured ordering and seller preparation → On-demand Delivery Platform. |
| Multi-vendor Marketplace | adjacent | Generic goods marketplace fulfills by shipping with no time-critical preparation or address-bound courier handoff of prepared food. Remove prepared-food fulfillment semantics → Multi-vendor Marketplace. |
| Restaurant Delivery Management | seller-side tooling | Manages a seller's own delivery operations; no consumer marketplace surface, no multi-seller aggregation. |
| Service Marketplace | adjacent | Sells services (labor/time) rather than prepared food; fulfillment is scheduling/work, not food handoff. |
| Ride-hailing Platform | mechanical cousin | Shares dispatch mechanics (offer/accept, tracking) but the transported thing is a passenger, not a menu-built order; no seller/preparation side. |
| Kitchen Display System | adjacent tooling | In-kitchen production display; consumes orders produced by ordering surfaces; no consumer surface, no payment, no marketplace. |

The most important boundary is with Restaurant Online Ordering: both share "order prepared food for delivery/pickup". The seam is whether the surface aggregates many independent sellers under a third-party operator (marketplace) or represents one seller under its own identity (direct channel). White-label storefronts blur this commercially but the consumer-facing ownership test holds.

## Historical / Market-Sample Check

Test: would older, regional, or differently positioned products still fit the Level 0 core?

- **Fax/lead-era marketplace (early-2000s European aggregator origin):** multi-seller listing ✓; order composed from the seller's menu on the platform and forwarded (fax/phone/email) to the seller as fulfillment instruction ✓; fulfillment terms delivery-or-collection with off-premises handoff ✓. Fits with no app, no platform couriers, no platform payment. → Core holds.
- **Regional phone-assisted marketplaces (call-center ordering relayed to sellers):** aggregation ✓; order of record (operator-created but platform-recorded) ✓; off-premises fulfillment ✓. Fits at the margin; recorded as a variant, not normalized into the core.
- **Phone-based pizza/takeaway ordering (no platform):** fails leg 1 and 2 → correctly excluded.
- **Courier-only delivery services (no ordering):** fail legs 1–2 → On-demand Delivery Platform, correctly excluded.
- **Single-brand chain app:** fails leg 1 → Restaurant Online Ordering, correctly excluded.

The check confirms: platform-courier operation, platform payment capture, apps, live tracking, and subscriptions are all era/model-bound implementations and stay out of the defining core.

## Uncertainties

1. **Product-level verification is entirely absent.** All observations are category-level; no product's own documentation confirmed any specific behavior. Principal uncertainty of this pass.
2. Exact composition and ordering of checkout fee layers, and who funds which fee, vary by product and market; recorded only as "layered fee architecture, disclosed before payment".
3. The degree to which seller acceptance is automated vs manual in current products; recorded only as "acceptance/rejection paths exist".
4. Whether platform payment capture has become universal (aggregator heritage products historically allowed seller-collected payment); recorded as common-but-not-definitional.
5. Regional forms (cash on delivery, call-center ordering) are described at variant level only; their current prevalence was not verifiable.
6. The boundary test against white-label storefront services (a marketplace operator selling a single-brand storefront to a chain) is conceptual; the market prevalence of edge cases was not verifiable.

## Final Synthesis

The Food Delivery Marketplace is canonically: **a third-party platform whose defining structure is (1) aggregation of many independent prepared-food sellers on one consumer surface, (2) the consumer-composed, menu-based order of record transmitted to a specific seller for fulfillment, and (3) coordination of that order's completion off the restaurant premises — delivery to an address or consumer pickup — ending in a handoff of prepared food.**

Everything else — courier networks, platform payments, live tracking, fees, ratings, memberships, promotions, vertical expansion — is the common mature or variant implementation layered on that structure. The two fulfillment models (platform-courier vs seller-delivery) are the type's deepest split and prove the abstraction: what all forms share is exactly the three-part core; where they differ is implementation.

Boundaries held: against Restaurant Online Ordering via multi-seller third-party aggregation; against On-demand Delivery Platform via menu/order/preparation semantics; against generic marketplace via prepared-food fulfillment semantics; against seller-side tooling via the consumer marketplace surface.
