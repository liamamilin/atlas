# Research Notes — Last-mile Delivery Platform

## Research Goal

Understand what a Last-mile Delivery Platform actually is as an Application Type: what the unit of record is, how final-leg delivery work enters, is orchestrated, executed, confirmed, and communicated, and how the Type separates from the extremely dense §18 delivery cluster (courier-management-platform, delivery-scheduling-platform, dispatch-management, delivery-experience-platform, on-demand-delivery-platform, route-optimization-platform, proof-of-delivery-platform, shipment-visibility-platform, parcel-management-platform).

## Prior-pass context (sibling seams to inherit)

- **courier-management-platform** (processed 2026-09-07): L0 = courier order + dispatch to own workforce + recorded execution ending in POD + courier-business frame (customer accounts, contracted rates, billing). Explicitly predicted: "Remove this [frame] and the same software becomes a shipper's internal fleet tool — a last-mile delivery platform." Flags a JOINT REVIEW with this leaf. Elite EXTRA documented as the drift pole (brands itself "last mile software" while serving courier operators).
- **delivery-scheduling-platform** (processed 2026-09-07): L0 = scheduled delivery + delivery schedule + availability structure (the when-structure). Flags JOINT REVIEW with route-optimization-platform (unprocessed) and this leaf. Bringg-class enterprise promise pole under-observed (403/timeout ×4).
- **dispatch-management** (processed 2026-09-07): L0 = work queue + resource roster with availability + assignment act + live dispatch picture. States: "Last-mile Delivery Platform / On-demand Delivery Platform own shipper-side delivery orchestration/customer experience; a dispatch core may sit inside them. Final placement should be settled in those passes."
- **delivery-experience-platform** (processed 2026-09-08): L0 = delivery journey of record + consumer-facing branded surface + proactive comms. Boundary recorded: last-mile orchestrates execution; delivery experience holds no execution machinery.

## Initial Boundary (working hypothesis before research)

A Last-mile Delivery Platform orchestrates the final leg of goods delivery — from the point where the tenant's order flow hands over (store, warehouse, kitchen, hub) to the end recipient. Hypothesis: the tenant is not necessarily a courier business (that is courier management's frame); deliveries are often derived from commerce/order systems; execution machinery (routing, dispatch, driver app, POD) plus recipient-facing visibility are the substance. Main confusion risks: courier management (business frame), dispatch management (generic assignment), delivery scheduling (when-structure), delivery experience (consumer surface), route optimization (engine center), on-demand delivery (consumer marketplace).

## Research Questions

1. What is the unit of record (task? delivery order? stop?) and what does it carry?
2. How does work enter the system — manual entry, order-system integrations, API, import?
3. How is execution orchestrated — routing, auto-assignment, dispatch to own vs third-party capacity?
4. How is field execution captured (driver app, status events, POD) and governed (corrections, force-complete)?
5. Is recipient-facing delivery communication (notifications, tracking pages, ETAs) part of the product's center or a common layer?
6. Is courier-business machinery (rate tables, client accounts, billing) definitional or a variant suite?
7. Is route optimization definitional or a capability (tier-gated anywhere)?
8. What work mixes exist (routed/planned rounds vs on-demand near-now)?
9. What verticals and tenant types does the market serve, and does tenant identity change the core?
10. Where exactly do the seven seam siblings separate, by the remove-what test?

## Representative Products

| Product | Why sampled | Tier / philosophy | Sources reached |
|---|---|---|---|
| **Onfleet** | self-positions as last-mile delivery API/platform; role-based operational help center | API-first, mid-market/enterprise; verticals incl. food, pharmacy, retail; ships a courier-client suite as an add-on | support.onfleet.com (root site 403) |
| **Shipday** | SMB self-serve "delivery management", food-centric origin with multi-vertical spread, third-party gateway | SMB/multi-location restaurants + couriers + retail; operations-layer philosophy | shipday.com, docs.shipday.com |
| **Elite EXTRA** | self-labels "Last Mile Software"; suite (Routing & Dispatch + Delivery Network + Returns Automation); distributor vertical | distributor/enterprise; routing-led suite philosophy | eliteextra.com (3 pages) |
| **Detrack** | POD/tracking-first delivery management, global (60+ countries), tier-gated optimization, 3PL rate cards | global SMB/mid, price-per-driver; POD-first philosophy | detrack.com |

Rejected/deferred as core samples: Tookan (2 fetch failures — dropped per network rule); Bringg (403 in this pass and the delivery-scheduling pass — enterprise pole unverified); Routific/OptimoRoute/Circuit/Dispatch (already sampled by the delivery-scheduling pass; used here only as boundary references); Dispatch Science / CXT / OnTime 360 (courier-frame products, already sampled by the courier pass).

## Sources

Fetched 2026-09-08:

- Shipday — https://www.shipday.com/ (homepage: features, use cases, integrations, FAQs); https://docs.shipday.com/ (API index); https://docs.shipday.com/reference (API reference); https://docs.shipday.com/reference/delivery-order-object.md (Delivery Order Object + orderState enum)
- Elite EXTRA — https://eliteextra.com/ (suite overview); https://eliteextra.com/routing-and-dispatch/ (Integrate→Route→Dispatch→Inform→Fulfill→Manage); https://eliteextra.com/delivery-network/ (third-party platform mechanics)
- Detrack — https://www.detrack.com/ (product overview, industries, integrations, pricing tiers)
- Onfleet — https://support.onfleet.com/hc/en-us (support center root); Dispatcher category (task management, routing, driver management, task import); Task Status; Task Management; Create a Task; Courier and Courier Client category

Source-access limitations:

- onfleet.com root marketing site returns 403 (also in prior sibling pass); evidence drawn from the reachable support center instead — role-based operational documentation, arguably stronger for this research.
- bringg.com returns 403 (second consecutive pass; delivery-scheduling pass recorded 403/timeout ×4). The enterprise delivery-orchestration/customer-promise pole remains unverified; no promise-engine claims are made.
- tookanapp.com transport-failed twice (homepage, /features); dropped.

## Product Observations

### Onfleet (Evidence layer A — directly observed)

- Unit of record is the **Task**: "the core unit of work to be completed by drivers (ex: a pickup OR delivery)". Required fields: recipient (name + phone; a "No recipient" checkbox suppresses all notifications for the task), task type (dropoff or pickup), destination (valid street address; geocoding skippable if coordinates entered). Optional: recipient notes (persist per recipient phone), task details, delivery time window (**Complete After / Complete Before**), route-optimization constraints (quantity, service time), assignment (at creation or later, to a driver or a Connected Organization). Task templates, cloning, custom fields, metadata.
- **Task status** (dashboard + map): Unassigned (grey) → Assigned (purple) → In Transit ("being executed with active notifications and recipient location tracking", blue) → Succeeded (green) / Failed (red). **Delayed** indicator (gold dot) when the current time or projected ETA passes the Complete Before time; drivers with delayed tasks are flagged too.
- Dispatcher surfaces: map + sidebar, table view, filters/search, mobile dispatching, dashboard analytics, ETA view, task pin clustering. **Auto-assignment** setting exists. Manual reordering of a driver's task list (drag on map, reverse order).
- **Routing and Route Optimization** section: Command Center, Route Optimization setup/operating, Route Plans, End Route / Return to Hub — optimization is a distinct, enableable capability ("You must enable Route Optimization to see and use this feature"), not the default object model.
- **Task Import**: manual/API import, scheduled import, international phone handling — integration-fed intake is first-class.
- **Task Management** (dispatcher governance): **force complete** an active task (examples given: driver forgot, device battery died, "Order is canceled by the customer while delivery is in progress"), with success/failure selection, notes, and optional recipient notification; **edit completion status after the fact** (Failed → Succeeded and vice versa) with change information.
- **Driver & Driver Management**: add/remove drivers, driver profile, driver schedule, driver status, single-device login.
- **Courier and Courier Client suite** (optional add-on family): Accessorial Charges, Adding and Managing Courier Clients, **Assigning Rates and Services to Clients**, Creating and Editing **Rate Table**, Client Order CSV Import, barcode scanning for couriers and clients, **Client Portal** (create/view/edit orders, service availability, notifications and tracking page, client dashboard). → the courier-business frame exists as an optional suite, not as the platform's base object model.
- Roles documented: Admins, Dispatchers, Drivers, **Couriers**, Developers; API docs are a primary product surface.

### Shipday (Evidence layer A)

- Positioning: "AI Delivery Management Software… Automate delivery, improve customer communication…"; "Shipday acts as your delivery operations layer". Use cases: restaurants, pizzerias, e-commerce, **couriers**, retail, florists, liquor, grocery. Claims 6,000+ businesses, 30m+ orders, 100+ countries.
- **Delivery Order Object** (API): orderId; orderNumber ("Order reference of customer platform" — the order originates outside); company + operational **area**; **customer** (name, address, phone, email, lat/lng); **restaurant** (pickup-side object — food-centric origin); **assignedCarrier** (the driver, with on-shift flag); distance; **activityLog** (placementTime, expectedPickupTime, expectedDeliveryDate/Time, assignedTime, startTime, pickedUpTime, arrivedTime, deliveryTime); costing (totalCost, deliveryFee, tip, discount, tax); paymentMethod; orderItems; orderStatus; **trackingLink** (customer tracking URL); feedback (customer rating); **schedule flag**; ETA; pickup/delivery instructions; **proofOfDelivery** (signature image, lat/lng where completed, photo URLs).
- **orderState enum**: ACTIVE, NOT_ASSIGNED, NOT_ACCEPTED, NOT_STARTED_YET, STARTED, PICKED_UP, READY_TO_DELIVER, ALREADY_DELIVERED, FAILED_DELIVERY, INCOMPLETE.
- API also covers: insert/edit orders, **unassign order from driver**, retrieve carriers/add carriers, **Assign to a specific 3rd-party delivery service provider ("Usually, after getting an estimate")**, provider availability, order status updates, driver-location webhook; **Order Delivery Progress** endpoint is "designed for public consumption, typically by end-customers, to track their delivery status".
- Homepage features: **branded tracking** ("live updates, offers, and promotions"), review management, **proof of delivery** (photos, signatures, timestamps), driver management, mobile app for drivers, AI agents, reports, refund collection for third-party delivery failures, AI receptionist.
- FAQ-level behavior statements: "manage your own drivers and third-party delivery providers in a single system… switch between providers without changing your workflow"; "built-in access to 3rd party delivery services"; automated driver assignment; live tracking reduces "Where is my order?" calls; automatic post-delivery review requests.
- Integrations: POS (Toast, Square, Lightspeed, Oracle, Heartland, GloriaFood), e-commerce (Shopify, Wix, Squarespace), delivery marketplaces/networks (DoorDash, Grubhub, Uber, Lyft, Otter, Flipdish, Zuppler, Deliverect); public API docs.

### Elite EXTRA (Evidence layer A)

- Positioning: "Last Mile Software Solutions"; suite of three products: **Routing & Dispatch** ("Last Mile Logistics Software"), **Delivery Network** ("Third-Party Delivery Platform"), **Returns Automation**. Since 2008; 325,000+ users claimed. Testimonial base: automotive parts retailers, paint distributors, truck centers.
- **Routing & Dispatch** six-stage flow: **Integrate → Route → Dispatch → Inform → Fulfill → Manage**.
  - Integrate: "Elite EXTRA integrates seamlessly with your existing business systems to ensure orders are automatically and efficiently passed into the dispatch workflow. Whether you're using an ERP, POS, eCommerce platform, or a custom solution."
  - Route: "optimization engine that works according to your rules. Optimize based on efficiency, time windows, customer priority."
  - Dispatch: "Dispatch routes and orders to drivers within your fleet or… drivers from crowdsourced and courier fleets."
  - Inform: "email and text notifications complete with a tracking page to follow their orders. ETAs and order updates can also be viewed by your own team"; "live tracking page tailored to your brand".
  - Fulfill: "EXTRA Driver mobile app, guiding them through each task from dispatch to completion. Capture every detail along the way, including signatures, photos, and time stamps."
  - Manage: "reporting engine, manager's dashboard, route whiteboard."
- **Delivery Network** mechanics: Connect (third-party providers incl. crowdsourced fleets — DoorDash/Uber-class — and regional/local courier fleets; "No individual contracts are required – they are all handled within the system"); Compare ("Price and time shop for the option that works best for you" per delivery); Dispatch (compare network drivers vs internal fleet "at the point of dispatch"); Automate (business rules + preferred providers; orders enter from ERP/eCommerce; third-party fleet picks up at the tenant's location); Inform (delivery status updates from providers flow back and are shareable with customers); Manage ("Handle payments through the Delivery Network system so you don't have to contract with each third-party provider" + provider analytics).
- **eCommerce same-day** flow: Delivery Network integrates into the e-commerce platform; "Customers are given the option for same day delivery at checkout"; "The delivery cost is added right to the customer's bill at checkout"; orders auto-sent to the best third-party fleet; both tenant and customer kept informed.
- Feature set named: optimized route planning, automated routing & dispatching, real-time GPS tracking, customer ETA notifications, photo & signature capture, driver app, route scheduling, reporting suite.

### Detrack (Evidence layer A)

- Positioning: "delivery management software that brings live driver tracking, proof of delivery, and automatic customer notifications together in one platform. It replaces paper run sheets and 'where's my order?' phone calls." Customer testimonials describe replacing "paper based POD system" and manual scanning of PODs.
- Features: **Electronic Proof of Delivery** (digital signatures, photos, timestamps, location), live delivery tracking (driver locations + job progress), **customer notifications** (SMS, WhatsApp, email; branded tracking links), **route planning/optimization** ("plan the most efficient routes… re-optimise as jobs are added"; driver groups, start times), vehicle checks (custom checklists), reports & analytics, **Rate Cards** ("Create custom rate cards within delivery jobs, set up commissions for contractors" — 3PL-oriented), fleet management.
- Pricing structure confirms capability tiering: Pro tier ($29/driver) = POD + tracking + notifications + branded links + "custom field mapping and job statuses"; **Advanced tier adds route optimisation, recurring jobs, scheduling view (calendar tools), capacity reporting**; Enterprise adds dedicated support. Web users unlimited; pricing per driver app.
- Industries list: freight & 3PL, construction, distributors & suppliers, food & beverage, retail & e-commerce, services & trades, plus couriers, waste, cold chain, furniture, medical/pharma. "Designed for any operation that makes deliveries and needs real-time visibility from dispatch to doorstep."
- Integrations: Shopify, WooCommerce, MYOB, Xero, QuickBooks, Twilio, Zapier, AfterShip, Shopee; REST API + webhooks ("From order creation through to proof of delivery"). 60+ countries.

## Cross-product Comparison

| Structure / capability | Onfleet | Shipday | Elite EXTRA | Detrack | Assessment |
|---|---|---|---|---|---|
| Delivery task/order as unit of record with status lifecycle | Task (pickup or dropoff) | Delivery Order (orderState enum) | orders/dispatches per named stage flow | jobs | **Core** (4/4, different names) |
| Recipient/destination + timing on the record | recipient + Complete After/Before | customer + expectedDeliveryDate/Time + ETA | time windows in routing rules; ETA notifications | recipients + jobs (window detail not fetched) | **Core** (4/4) |
| Order intake from tenant's commerce systems (POS/ERP/e-commerce/API/import) | Task Import, scheduled import, API | orderNumber from customer platform; POS/shop integrations | Integrate stage (ERP/POS/eCommerce) | Shopify/WooCommerce/ERP/API/webhooks | **Core-leaning** (4/4; depth varies) |
| Dispatch/assignment incl. auto-assignment | Auto-assignment setting; manual reorder | automated driver assignment; unassign API | Dispatch stage (own fleet or network) | job assignment to drivers | **Core** (4/4) |
| Driver mobile app executing tasks | Drivers role + app docs | Mobile App for Drivers | EXTRA Driver app | driver app (+ manager/scanner apps) | **Core** (4/4) |
| Field-captured delivery confirmation (POD) | completion states; barcode/custom pins | proofOfDelivery object (signature, photos, geotag) | signatures, photos, time stamps | ePOD signature/10 photos/location/timestamps | **Core** (4/4) |
| Recipient notifications + live tracking | In Transit = "active notifications and recipient location tracking" | trackingLink; public delivery-progress endpoint | Inform stage: email/text + tracking page | SMS/WhatsApp/email + branded tracking links | Common (4/4 modern; channels/branding vary) |
| Route optimization | enableable capability w/ constraints | "advanced route planning" | optimization engine per rules | **tier-gated to Advanced plan** | Common, **not definitional** (absent from one product's base tier; manual dispatch possible) |
| Third-party delivery networks w/ price/time comparison | not observed in fetched pages (partners page exists) | Delivery Services Gateway; Assign after estimate | Delivery Network (compare, automate, pay centrally) | not observed | Common-leaning in market (2/4 direct) — variant |
| Courier-business machinery (client accounts, rate tables, billing) | **Courier suite** (clients, rate tables, accessorials, client portal) | courier use-case, no rate machinery fetched | central contracting/billing for network providers (vendor-managed) | **Rate Cards** for 3PL contractor commissions | Variant (2/4 as suite/pole) — NOT definitional |
| Status correction / dispatcher override | force complete; edit completion status | unassign; edit order | route whiteboard re-dispatch | custom job statuses | Common (management layer over field capture) |
| Delay/at-risk surfacing | Delayed gold-dot logic (ETA vs Complete Before) | etaTime on order | ETA notifications; customer ETA alerts | milestone reports (expected vs actual) | Common |
| Analytics/reporting | Dashboard analytics | Reports and AI insights | Business analytics & reports; provider analytics | Reports and analytics; capacity utilization | Common |
| Scheduling/calendar surfaces | Task templates; Route Plans; driver schedules | schedule flag on orders; scheduled delivery | route scheduling | scheduling view (tier-gated); recurring jobs (tier-gated) | Common, secondary (when-structure is not the center) |
| Reviews/reputation machinery | not observed | Review Management; post-delivery Google review requests | not observed | not observed | Product-specific |
| Returns/pickup handling | pickup task type | pickup order object (separate API object) | Returns Automation suite module | jobs cover "deliveries and pickups" | Pickup common; returns automation product-specific |
| AI overlays | not observed (support center) | AI agents, AI receptionist | not observed | Detrack MCP server access (pricing page) | Product-specific/era-current |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (deliberately minimal)

Three structures. Remove any one and the product stops being recognizable as a Last-mile Delivery Platform:

1. **The delivery task as the unit of record** — a final-leg goods movement to an end destination (a delivery, commonly paired with pickup legs), carried as a persistent record binding recipient/destination, timing (window or expected time), and items/instructions, whose status advances through execution (unassigned → assigned → in transit → delivered / failed). Without it there is no delivery work to orchestrate — just a map or a tracking feed.
2. **Orchestration of final-leg execution over the operator's delivery capacity** — the platform's central managed activity is planning, sequencing, and assigning those deliveries to drivers — the tenant's own workforce, contracted drivers, or integrated third-party delivery networks — individually or batched into routes, with reassignment as a managed operation. Without it the product is a tracking page or a visibility feed, not a delivery platform.
3. **Field execution captured to delivery confirmation** — drivers work from a mobile surface (assigned task list, navigation, status updates) and each delivery closes with field-captured confirmation (signature / photo / timestamp / location) held as the delivery's closing evidence. Without it, work is dispatched but never evidentially completed — a dispatch board, not a delivery execution system.

Deliberately NOT in L0 (tested and rejected): recipient-facing notifications/tracking (near-universal modern signature layer, but historically thin — early delivery operations communicated by phone; channels vary), route optimization (tier-gated in a sampled product; manual dispatch documented), courier-business machinery (optional suite), third-party network intermediation (2/4), GPS telemetry (era machinery), consumer marketplace/demand generation (absent from the Type), food-order semantics (one product's origin flavor).

Tenant neutrality is part of the L0 posture rather than a fourth structure: the Type is defined by the execution substrate, not by a business frame. The tenant may be the shipper/brand (retailer, distributor, food & beverage operator, pharmacy), or a delivery operator (courier/3PL) — the sampled products serve both without the core changing. The courier-business frame (external client accounts, contracted rate tables, billing of delivery as revenue) is a variant suite, which is exactly the seam the courier-management pass drew from the other side.

Historical check: the 2008-generation last-mile suites (Elite EXTRA's own lineage: routing + dispatch + notifications + driver app + signature/photo capture) satisfy all three legs with no AI, no crowdsourced networks, no cloud assumptions beyond SaaS delivery. The manual predecessor (paper run sheets, radio dispatch, phone-based customer updates — documented in Detrack's own customer testimonials as the replaced baseline) satisfies the legs in manual form; the definition names no GPS, no apps, no optimization, no cloud. Regional breadth: Detrack (60+ countries, APAC origin) and Shipday (100+ countries claimed) support the concept holding outside North America. The definition survives the historical check.

### L1 — Common Mature Structure

- Recipient-facing delivery communication: automatic notifications (SMS/email/WhatsApp/push) with live tracking pages and ETAs, commonly brandable; driven by execution events; bound to the recipient record (suppressible when no recipient exists)
- Route optimization with business constraints (time windows, priority, quantity, service time, driver groups/zones), operating as an enableable engine over the task pool
- Auto-assignment / assisted dispatch; manual drag-reorder of routes; reassignment and unassignment
- Delay / at-risk surfacing (ETA projected against window commitments); customer ETA alerts
- Integration-fed intake from the tenant's systems: e-commerce platforms, POS, ERP, marketplaces; API + webhooks; CSV/scheduled import
- Dispatcher control surfaces: map + list/table dashboards, status colors/pins, filters, mobile dispatching, route whiteboards
- Exception machinery: failed-delivery states, force-complete, post-hoc status correction, cancellation mid-execution
- Pickup tasks and returns pickup alongside deliveries
- Analytics: delivery success/on-time, driver performance, delay analytics, manager dashboards; third-party provider analytics where networks are used
- Task templates, recurring jobs, scheduling/calendar views (secondary to execution)
- Reference data: recipients/address books with per-recipient notes, areas/zones, geocoding

### L2 — Variant / Optional Structure

- Courier/3PL business-frame machinery as an optional suite: client accounts/portals, rate tables, accessorials, contractor commissions (Onfleet courier suite, Detrack rate cards; the courier-management Type centers this)
- Third-party delivery network intermediation: multi-provider price/time comparison, automated network dispatch, central network contracting/payment (Elite EXTRA Delivery Network, Shipday Delivery Services Gateway)
- Pre-purchase delivery promise touchpoints: same-day option and delivery cost surfaced at checkout via e-commerce integration (Elite EXTRA eCommerce flow)
- Vertical tuning: food/restaurant (pickup-delivery pairing, order costing with tips/fees), pharmacy, distributors/auto parts (B2B recipients, route-heavy), big & bulky
- Work-mix emphasis: routed/planned rounds vs on-demand near-now vs mixed
- Packaging: standalone platform vs suite modules (returns automation, telematics sibling products) vs courier-suite add-ons
- Reputation/growth machinery attached to the delivery experience (review management, refund recovery for failed third-party deliveries)
- API-first product posture (API as primary surface) vs UI-first SMB tools
- Pricing/deployment shape: per-driver SaaS self-serve vs enterprise contracting

### L3 — Vendor-specific (kept out of the final document)

- Onfleet: Task model vocabulary, Complete After/Before fields, Connected Organizations, Command Center, gold-dot delayed logic, single-device driver login, courier-suite article set
- Shipday: orderState enum values, restaurant object, "AI receptionist/agents" branding, refund-collection feature, 30-language support claim, BUSness-plan gating of the public tracking endpoint
- Elite EXTRA: Integrate→Route→Dispatch→Inform→Fulfill→Manage naming, Delivery Network provider roster (DoorDash/Uber/Roadie), RTx/RAx product names, Epicor ownership, route whiteboard, 8-week release cycle
- Detrack: Pro/Advanced/Enterprise tier split, per-driver pricing, vehicle-check checklists, Detrack MCP server, 10-photo POD detail

## Vendor-specific Findings

See L3. Single-product findings that must not generalize:

- Review/reputation management and refund collection (Shipday only)
- Returns Automation suite with policy enforcement and digital chain of custody (Elite EXTRA only)
- Courier-client portal suite with rate tables and accessorials (Onfleet suite; Detrack rate cards is the thinner analog)
- Pre-purchase checkout delivery-cost integration (Elite EXTRA eCommerce flow)
- AI receptionist/agents (Shipday); MCP server access (Detrack)

## Rejected Findings (considered and rejected as core)

- **Route optimization as definitional**: tier-gated to a paid tier in one sampled product (Detrack Advanced); enableable-but-optional in Onfleet; manual dispatch/reorder documented everywhere. Consistent with the courier and scheduling passes' rejections.
- **Recipient-facing tracking/notifications as definitional**: the modern signature layer (4/4) but historically thin — pre-software delivery operations ran on phone calls; channels and branding vary. Held as common structure with the explicit note that it is the market's most emphasized capability.
- **Courier-business machinery as definitional**: present as optional suites in two products; the execution core is identical without it. This is the ratified courier seam.
- **Real-time GPS/telematics as definitional**: fails the historical check; telematics is a separate product family (Elite EXTRA sells Fleet Telematics as a sibling product).
- **Third-party network intermediation as definitional**: 2/4 direct evidence; own-fleet-only operations remain fully in-type.
- **Consumer marketplace/demand generation**: no sampled product generates consumer demand; where e-commerce checkout is touched, the platform executes the delivery the retailer already sold.
- **Food-order semantics as definitional**: the food object model (restaurant, tips) is one product's origin flavor; distributor and B2B products lack it.
- **POD as the product**: POD is one closure step of the delivery lifecycle here; the proof-of-delivery-platform leaf owns the POD-centric product (Detrack's POD-first pole is the nearest straddle, noted for that pass).

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| Courier Management Platform | closest sibling; ratified keep-both | The courier Type is the delivery operator's *business* system: courier orders for external customer accounts, contracted-rate pricing of every order, billing, driver pay. Remove the business frame and the same execution machinery remains — this Type. From this side: courier machinery reappears here only as an optional suite (Onfleet courier suite; Detrack rate cards), confirming the seam from both directions. Elite EXTRA straddles by branding ("last mile software") while serving courier operators — the substrate is shared; the frame differs. |
| Dispatch Management | machinery inside the Type | Dispatch owns the transversal assignment loop (work queue × roster × assignment act × live picture) for any field work. This Type adds delivery-domain semantics: delivery tasks with windows and POD, recipient layer, delivery networks, commerce intake. Remove delivery semantics and orchestration scope → generic dispatch. |
| Delivery Scheduling Platform | upstream neighbor | Scheduling owns the when-structure (offered times, availability rules, the schedule as the worked object). Here, windows are attributes of tasks and schedule surfaces are secondary (tier-gated in one product). Remove execution orchestration → scheduler; remove the when-structure center → this Type. |
| Delivery Experience Platform | downstream surface neighbor | Experience platforms own the consumer-facing post-purchase presentation/communication and hold **no execution machinery**. Here, notifications/tracking attach to the execution record the platform itself produces. Remove execution orchestration → delivery experience; remove the experience layer → still this Type (thin form). |
| Route Optimization Platform | capability vs center | The optimization engine is a common capability here (and tier-gated in one product); when the engine and its solves are the defining object, that is Route Optimization. A platform without optimization at all remains in-type (manual dispatch). |
| Proof of Delivery Platform | capability slice | POD is the closing step of the delivery lifecycle here. The POD-centric product (capture-first, POD-as-deliverable) is a separate leaf; Detrack's POD-first heritage is the nearest straddle. |
| On-demand Delivery Platform (unprocessed) | held conservatively | On-demand delivery = consumer-facing instant-delivery marketplace with its own demand generation. This Type includes near-now work as a *work-mix mode* (restaurant orders, on-demand network dispatch) without demand generation. Final seam settlement belongs to that pass; held on marketplace/demand-generation vs orchestration. |
| Shipment Visibility Platform | different object | Visibility aggregates/normalizes shipment state across carriers for freight the tenant does not execute. This Type executes the final leg over its own/mixed capacity. |
| Parcel Management Platform (unprocessed) | different phase/model (moderate confidence) | Parcel management = shipper-side multi-carrier shipping execution (rate shopping, labels, manifesting) before carrier handoff. This Type orchestrates own-fleet/mixed final-leg completion after the handoff decision. Held moderately; that pass pending. |
| Food Delivery Marketplace (§26) | consumer marketplace vs operations layer | Marketplaces generate consumer demand and mediate restaurants/consumers; products sampled here serve as the restaurant's/distributor's own delivery operations layer behind any storefront. |
| Transportation Management System | business-frame + unit-of-work seam | TMS runs freight (loads, carriers, tendering, audit/pay). Here the unit is the final-leg delivery to an end recipient, and the freight business frame is absent. |
| Fleet Management System | estate vs work | FMS owns vehicles/telematics/maintenance as the system of record; here vehicles are executing resources and the delivery task is the record. |

## Uncertainties

1. **Bringg (enterprise delivery-orchestration/customer-promise pole)** unreachable this pass (403) and in the delivery-scheduling pass (403/timeout ×4). The enterprise pole — delivery-window promises at scale, promise engines — is characterized only via the sampled products' enterprise-facing surfaces; no promise-engine mechanics are claimed.
2. **Onfleet marketing/positioning pages** (solutions verticals, pricing) behind 403; evidence comes from the support center's operational articles. Marketing-level claims about Onfleet are not made.
3. **Tookan** dropped after two failed fetches; the SMB template-breadth pole is under-observed. No claims rest on it.
4. **Driver-app operational depth** (offline modes, device requirements, exact scan workflows) verified only partially (Onfleet single-device login observed; others' help centers not fetched). Final doc keeps driver-app description conceptual.
5. **Exact status vocabularies** are product-specific (Onfleet's 5+delay vs Shipday's 10-value enum); the final doc uses conceptual states and notes variance.
6. **Detrack window/commitment fields** not verified at feature-page depth (homepage-level only); timing claims for Detrack kept generic.
7. **Regional last-mile suites** (EU/JP/LATAM) not sampled beyond Detrack/Shipday's international presence; assertions kept conceptual.

## Final Synthesis

A Last-mile Delivery Platform is the orchestration system for the final leg of goods delivery. Its defining core is three structures: (1) the delivery task as the persistent unit of record — recipient/destination, timing, items, status advancing unassigned → assigned → in transit → delivered/failed; (2) orchestration of that leg over the operator's delivery capacity — planning, sequencing, assignment/dispatch to own, contracted, or third-party-network drivers, with reassignment managed; (3) field execution captured to delivery confirmation — driver-side execution ending in signature/photo/timestamp evidence. Around this core sits the mature stack: recipient-facing notifications/tracking (the market's signature layer), route optimization as an enableable engine, commerce-system intake, exception machinery, analytics, and scheduling surfaces. The Type is defined by the execution substrate, not by a business frame: the same machinery serves retailers, distributors, food operators, pharmacies, and courier/3PL operators, with courier-business machinery appearing only as optional suites — which is precisely where courier management begins. All three inherited seams hold from this side: courier (tenant frame), scheduling (when-structure), dispatch (transversal machinery), experience (no execution machinery). Taxonomy verdict: confirmed standalone Type; the §18 delivery-cluster joint-review obligations are discharged from this side, with route-optimization-platform and on-demand-delivery-platform passes still to settle their sides.
