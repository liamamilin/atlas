# Restaurant Delivery Management

## Overview

A **Restaurant Delivery Management** application is the restaurant-side system for managing delivery as an order fulfillment channel. It takes ownership of delivery orders — restaurant orders destined for a customer's address — assigns each one to a fulfillment resource (the restaurant's own driver or an external delivery service), and tracks the delivery through to a closed outcome: delivered, canceled, or undelivered with a recorded action.

The defining core is small:

```text
Delivery order (restaurant order bound to a customer address)
└── Courier assignment (own driver or external delivery service)
    └── Delivery progression to a closed outcome
        (assigned → picked up → delivered / canceled / undeliverable)
```

Everything else commonly associated with restaurant delivery — multi-provider quote matching, checkout-time fee and ETA quotes, live customer maps, courier apps, proof-of-delivery checks — is standard equipment in current products but is not what makes the system this Type. A pizzeria dispatcher with a driver board and a phone satisfies the same core; a pure dispatch API with no operator interface satisfies it too.

When the perspective shifts to the consumer side — a venue that aggregates many restaurants and sells delivery demand — the product becomes a Food Delivery Marketplace. When courier assignment disappears and only order capture remains, it is Restaurant Online Ordering.

## Users & Context

Primary users:

- **Delivery coordinator / shift manager** — watches the delivery board, resolves stuck deliveries, reassigns or cancels, handles refunds and disputes.
- **Restaurant operator / owner** — configures the delivery program: whether delivery is offered, which providers fulfill it, what it costs, and under what conditions orders qualify.
- **Driver (own fleet)** — receives assigned or offered delivery jobs, confirms pickup and dropoff, shares location.

Secondary users:

- **Kitchen staff** — receive the delivery order like any other order and mark it ready for pickup.
- **Customer** — not an operator of the system, but a consumer of its outputs: the delivery fee and ETA at checkout, and the delivery tracking surface afterwards.
- **Enterprise brand teams** — configure delivery rules across many locations and read delivery performance analytics.

The work environment is the restaurant's off-premise operation: orders arrive continuously from the restaurant's own ordering channels (and, in some setups, from marketplaces under own-delivery agreements), the kitchen prepares them, and the delivery management system's job is to get each one from the pass to the customer's door with the least friction, cost, and risk.

## Core Model

### The Defining Core

**Delivery order.** The unit of record. A restaurant order designated for delivery: menu items and modifiers, the customer's name, phone, and address, payment state, and any delivery instructions. It is bound to the restaurant's normal order flow — in mature products it flows to the store and kitchen "like any other order"; the only difference is that a courier, not the customer, collects it. The delivery order is the object to which everything else attaches: the assigned courier, the lifecycle states, the fees, the exceptions.

**Fulfillment resource.** Whoever can carry the order to the customer. Two shapes exist and both are first-class:

- the restaurant's **own driver** — an identifiable person managed in the system, with a status (available, on a job, on break), linked to one or more locations;
- an **external delivery service** — a third-party courier network that supplies drivers on demand.

The conceptual object is the same in both cases: an assignable fulfillment resource. How it is employed (employee, gig network, contracted local service) is an implementation choice, not a structural difference.

**Courier assignment (dispatch).** The act of binding a delivery order to a fulfillment resource. It happens either by rule — automatic selection based on cost, speed, distance, time of day, or provider preference — or by hand, when a coordinator assigns a job from a live board. Some products solicit quotes from multiple providers per order and pick a winner; others hand the job to a single configured network or to the next available own driver. The assignment is the decision that sets the delivery in motion.

**Delivery lifecycle.** The delivery order advances through a progression to a closed outcome. Conceptually:

```text
created → assigned → courier en route to store → picked up
        → courier en route to customer → delivered
                     ↘ canceled (by customer / courier / restaurant / platform)
                     ↘ undeliverable → recorded action (e.g. return to store)
```

Exact state names vary by product. The invariant is that the delivery has a tracked state, the restaurant can see it, and it ends in a definite outcome rather than fading out.

### Standard Capabilities

Mature products commonly add the following. They make the operation practical; they do not define the Type.

- **Delivery availability configuration** — per store or location: delivery on/off, service hours, minimum and maximum order amounts that qualify for delivery.
- **Fulfillment-resource configuration** — preferred and blocked providers, auto-selection rules (cheapest, fastest, preferred partner, distance, time of day), allowed vehicle types, and ceilings that reject unsuitable quotes (maximum fee, maximum transit time).
- **Fee and tip economics** — who pays for delivery (the customer at checkout, the restaurant as a per-order cost, or a mix), how the fee is presented, and how tips flow between customer, restaurant, and driver.
- **Customer tracking** — a tracking link or embedded live view showing delivery progress, ETA, and courier identity, usually reachable from the order confirmation.
- **Courier app** — the driver-facing surface: receive or accept jobs, navigate to the store, confirm pickup and dropoff, share location, contact the store or customer.
- **Exception machinery** — cancellations from any party, undeliverable handling with a recorded action (commonly return to store), refunds to customers, automated support tickets, re-dispatch of failed deliveries, and fallback to another provider when no own driver is available.
- **Verification options** — proof of delivery by signature, photo, pin code, or barcode scan; age verification where products require it.
- **Scheduled orders** — advance orders with pickup/dropoff time windows.
- **Store handoff** — the delivery order enters the POS/kitchen flow so preparation starts on time relative to the courier's arrival.
- **Analytics** — delivery performance by provider and location, courier stats (deliveries, distance, tips), error and refund reasons.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:            Delivery order
Implementations:    order created in the restaurant's own checkout; order ingested
                    from a marketplace under an own-delivery agreement; delivery
                    object created via API by the merchant's own software

Concept:            Fulfillment resource
Implementations:    employed driver in a managed roster; on-demand courier network;
                    contracted local delivery service

Concept:            Dispatch decision
Implementations:    per-order quotes from multiple providers with a tie-breaker rule;
                    rule-based auto-selection per location; manual assignment from a
                    live board; single configured network

Concept:            Lifecycle visibility
Implementations:    operator live board; customer tracking link or embedded map;
                    webhook events to merchant systems; courier app status swipes
```

A reader who has only seen one shape — say, a checkout that quotes several courier networks — should still be able to recognize the own-fleet dispatch board and the API-only dispatch service as the same Type.

## How It Works

### The main loop: order to door

```text
Delivery order arrives (own checkout, marketplace own-delivery agreement, or API)
→ system checks delivery eligibility (availability, order size, address, hours)
→ dispatch: a fulfillment resource is selected (by rule or by hand)
→ courier is engaged and moves to the store; kitchen prepares the order
→ courier picks up (pickup confirmed)
→ courier delivers (dropoff confirmed; optional verification captured)
→ delivery closes as delivered — or fails into the exception path
```

Two properties of this loop matter:

- **The order is prepared, not re-created.** The delivery order enters the store's normal order flow; the delivery system orchestrates fulfillment around it rather than replacing the restaurant's ordering stack.
- **The dispatch decision is the pivot.** Until a courier is bound, the order is food in a kitchen; after it, the delivery has a trajectory the restaurant can watch.

### The configuration loop

Operators set the delivery program once and adjust it continuously:

```text
Enable delivery per location
→ choose fulfillment resources (own drivers, networks, or both)
→ set selection rules and ceilings (preferred providers, max fee, max transit time,
  vehicle types, order-size limits)
→ set fee policy (who pays, fee amounts or passthrough, tip distribution)
→ monitor performance and adjust
```

### The exception loop

Deliveries fail in ways normal orders do not, and the system's behavior here is a large part of its value:

```text
No courier accepts or none is available
→ re-offer, re-dispatch, or fall back to another provider

Courier cancels en route
→ reassign to another courier; the delivery's assignment history updates

Customer unreachable or address invalid
→ record undeliverable reason → execute the recorded action (commonly return to store)

Delivery late or failed
→ refund the customer (manually or automatically by rule) → log the incident
```

## Interfaces

### Operator dashboard / live board

The coordinator's primary surface.

- lists active delivery orders with their state, assigned courier, and timers
- live map or status columns showing courier progress
- primary actions: assign or reassign a courier, cancel a delivery, mark order ready, contact courier or customer, request a refund

### Delivery configuration console

The operator's program-setting surface, usually per location.

- delivery availability toggle, hours, order-size limits
- provider roster with preferred/blocked status and selection rules
- fee policy, tip distribution, notification routing

### Store-side order surface

The kitchen/counter view of incoming delivery orders (often a tablet app).

- incoming orders with items, modifiers, customer notes, and promised times
- primary actions: acknowledge, update preparation time, pack, mark ready for pickup, view courier status

### Courier app

The driver's mobile surface.

- offered or assigned jobs with pickup address, dropoff address, and earnings
- primary actions: accept or decline, confirm pickup, confirm delivery, report a problem, share location, go on break

### Customer tracking surface

Usually a link or embedded view on the order-confirmation page.

- delivery progress, ETA, courier first name and vehicle
- updates automatically until the delivery closes

### Analytics

- delivery volume, cost, and performance by provider, location, and time
- courier stats and exception/refund reasons

## Important Rules / Behaviors

- **Delivery availability is a switch, not an assumption.** Turning delivery off for a location removes the delivery option for customers immediately; operators use it to pause the channel during capacity crunches.
- **Quotes can be rejected.** Where providers quote per order, the system enforces operator ceilings — a quote above the maximum fee or transit time is refused, and delivery may become unavailable for that order rather than silently overpaying.
- **Assignment has authority modes.** In own-fleet operation, couriers may self-accept offered jobs, or the system can restrict assignment to a manager; a fallback rule can hand jobs to an external partner when no own driver is available.
- **The lifecycle ends in a definite outcome.** Delivered, canceled, or undeliverable-with-action. An undeliverable delivery commonly triggers a linked return delivery back to the store, and the failure reason is recorded.
- **Cancellation is multi-party.** Customer, courier, restaurant, and platform cancellations are distinguished, because they carry different financial consequences (who is refunded, who bears the courier cost).
- **Tips are distributed by rule.** The split of a customer tip between driver and restaurant is a configuration; at least one product warns operators that low driver tips tend to hurt courier acceptance and on-time rates.
- **Verification is conditional.** Signature, photo, pin code, or age checks apply only where configured or legally required; the delivery object carries both the requirement and the captured result.
- **Delivery orders obey store state.** A closed or paused store stops or delays delivery orders like other orders; scheduled orders carry explicit pickup and dropoff windows.

## Variants

- **Own-fleet operation** — the restaurant employs drivers; the system manages the roster, assignment, and courier stats, and may add cash handling, break status, and location-sharing enforcement. Fallback to external partners is a common safety valve.
- **Network-dispatched operation** — the restaurant owns no drivers; every delivery is dispatched to an external courier network, priced per order or as a flat fee.
- **Hybrid operation** — own drivers first, external networks for overflow, long distances, or peak periods; selection rules decide per order.
- **API-first form** — the system is a dispatch API plus webhooks with minimal or no operator UI; the merchant's own software (or another delivery management product) creates and monitors deliveries. This form proves the Type's core stands without any operator interface.
- **Marketplace-fed operation** — delivery orders originate from marketplaces under own-delivery agreements, entering the same dispatch and tracking machinery as direct orders.
- **Catering and high-value orders** — routed to specialist providers or handled with priority rules and larger vehicle requirements.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Food Delivery Marketplace | most confusable neighbor | The marketplace is the consumer-facing venue aggregating many restaurants, generating demand and supplying its own couriers for a commission; this Type is the restaurant-side fulfillment system. Vendors themselves split the two: merchant-side dispatch APIs are a different product from marketplace APIs |
| Restaurant Online Ordering | upstream, complementary | Ordering captures the order at checkout (customer side); this Type fulfills it (operator side). Delivery selection typically happens inside the ordering checkout, but the fulfillment machinery belongs here |
| Last-mile Delivery Platform / On-demand Delivery Platform | generic sibling | Generic platforms move any parcel for any merchant; here the unit is a restaurant order with menu items, preparation timing, and store handoff. Generic courier networks are often the substrate this Type orchestrates |
| Courier Management Platform | adjacent | The courier company's own business system (fleet, jobs, settlements) versus the merchant side; own-fleet management overlaps in objects but serves the restaurant's delivery channel, not a courier business |
| Delivery Scheduling Platform | adjacent | Pre-booked delivery slots and route planning as the center of gravity versus on-demand fulfillment of incoming orders; scheduled orders are a setting here, not the core |
| Proof of Delivery Platform | capability vs Type | Proof of delivery is one verification layer inside this Type, not the whole system |
| Restaurant POS | container / sibling | The POS is the restaurant's transaction system of record across all order types; this Type manages the delivery fulfillment channel. Platform vendors ship them as distinct product lines |
| Dispatch Management (transportation domain) | generic sibling | Industry-generic dispatch of vehicles and jobs versus food-specific delivery orders bound to restaurant order flow |

The boundary with the Food Delivery Marketplace is the critical one: the same delivery can involve both (a marketplace order fulfilled under an own-delivery agreement is managed by this Type on the restaurant side while the marketplace remains the consumer venue). The test is perspective — who operates the system, and whose economics it serves.

## Representative Products

- **Olo (Dispatch / Rails)** — enterprise orchestration: per-order quotes across many delivery service providers on brand-owned ordering, with marketplace-order consolidation as a sibling product
- **Toast (Toast Delivery Services)** — POS-anchored delivery inside a restaurant platform, fulfilled by partner courier networks
- **Deliverect (Dispatch / Courier App)** — integration-hub philosophy: orders from first-party and external platforms routed across own fleets and a global courier network, with store-side and courier apps
- **Uber Direct** — white-label dispatch API: merchant-side create/manage/monitor of deliveries fulfilled by a courier network, with no ordering layer of its own

## Sources

Research date: **2026-09-09**

- Olo — product pages (olo.com, olo.com/dispatch, olo.com/rails) and Help Center: Dispatch Overview, Dispatch Store Settings, Dispatch Order Tracker Overview (olosupport.zendesk.com)
- Toast — Toast Delivery Services (pos.toasttab.com/products/toast-delivery-services) and Third-party delivery integrations (pos.toasttab.com/third-party-delivery-integrations)
- Deliverect — deliverect.com, Dispatch by Deliverect (deliverect.com/en/dispatch), Help Center (help.deliverect.com) incl. Dispatch: My Couriers
- Uber Direct — developer documentation: Overview and Delivery Status Webhook (developer.uber.com/docs/deliveries)

> Sourcing limitations: DoorDash Drive's developer documentation was not reachable (access denied); the white-label-network pole is evidenced by Uber Direct directly and by DoorDash Drive's appearance as an integrated partner in Deliverect and Toast documentation. Toast evidence is product-page level; its operational help-center detail was not fetched, so Toast-specific workflow claims are held at scope level. Geographic delivery-zone configuration was not observed as a first-class object in any fetched source and is therefore not asserted. Detailed product-by-product observations and the full comparison matrix are in the paired Research Notes.
