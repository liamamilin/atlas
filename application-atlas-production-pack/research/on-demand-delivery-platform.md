# Research Notes — On-demand Delivery Platform

## Research Goal

Understand what an "On-demand Delivery Platform" actually is as an Application Type: what the unit of record is, how a delivery request enters and is fulfilled in near-real time, how delivery capacity is matched to requests, what the requester (business and end customer) sees, and how the Type separates from the dense §18 delivery cluster — especially **Last-mile Delivery Platform** (processed 2026-09-08, which explicitly left the on-demand seam open for this pass to settle), **Food Delivery Marketplace** (§26, processed), **Courier Management Platform** (processed), **Delivery Scheduling Platform** (processed), **Dispatch Management** (processed), and the unprocessed **Ride-hailing Platform**, **Proof of Delivery Platform**, **Parcel Management Platform**, **Shipment Visibility Platform**.

## Initial Boundary (hypothesis before research)

Working hypothesis: an on-demand delivery platform is delivery machinery centered on the **request→match→track loop** — a business (or its customers) requests a delivery for immediate/near-term fulfillment, the platform matches the request in real time to available delivery capacity (own fleet, contracted couriers, crowdsourced network, or third-party delivery services), and the requester follows the delivery live to a proof-of-delivery close. Expected neighbors: last-mile (route-centric orchestration), food-delivery marketplace (consumer aggregation), courier management (operator business frame), delivery scheduling (when-structure), ride-hailing (same matching machinery, people not goods).

The last-mile pass held this seam "conservatively on marketplace/demand-generation vs orchestration (near-now work is a work-mix mode inside last-mile)" and left final settlement to this pass.

## Research Questions

1. What is the unit of record — a delivery request? An order? A courier job? What does it carry?
2. What does "on-demand" actually mean operationally — ASAP only, or ASAP + scheduled windows on the same machinery?
3. How is a request matched to a courier/driver? Offer/accept mechanics? Auto-assignment? Third-party gateways?
4. Whose capacity fulfills the delivery — the platform's own network, the merchant's own drivers, or third-party services? Is network ownership definitional?
5. What does the requesting business see (dashboard, API, webhooks)? What does the end customer see (tracking page, notifications)?
6. How does the request close — POD, fees, tips, refunds, returns, failures?
7. Is per-delivery pricing/quote machinery definitional?
8. Is live GPS tracking definitional, or the modern layer over a thinner status-relay loop?
9. Where exactly is the seam vs Last-mile Delivery Platform (the open flag), Food Delivery Marketplace, Courier Management, Delivery Scheduling, Dispatch Management, Ride-hailing?
10. Historical check: does the paper-era courier dispatch desk (request slip + radio dispatch + status relay) satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers + different supply models:

| Product | Pole | Why sampled |
|---|---|---|
| **Uber Direct** | network-seller, white-label API-first (mega-platform) | The ride-hailing giant's goods-delivery arm sold as an API/dashboard; its own docs explicitly separate it from the Uber Eats marketplace — a vendor-drawn boundary between this Type and Food Delivery Marketplace |
| **Roadie** (a UPS company) | crowdsourced network-seller (same-day) | Nationwide crowdsourced driver network sold to businesses; same-day/hot-shot framing; retail/auto/pharmacy/airline verticals |
| **Dispatch** | enterprise orchestration hybrid (on-demand + own-fleet) | Enterprise industrial distribution; self-labels both "On-Demand Delivery" and "Last-Mile Logistics Platform" — the live straddle; own managed driver network + fleet-management module |
| **Shipday** | SMB own-fleet + third-party gateway (restaurant-centric) | Delivery-management SaaS for restaurants/shops; dispatches own drivers AND third-party services; its own API names the machinery "on-demand" (`/on-demand/assign`, `OnDemandDeliveryService`) |

Dropped during research: **DoorDash Drive** (doordash.com/drive and developer.doordash.com 403 ×3 — abandoned per network rule), **Burq** (burq.com and help.burq.com transport errors ×2 — abandoned), **DelyvaX** (empty response — abandoned). No claims rest on dropped products.

## Sources

### Uber Direct (Layer A — official developer documentation, directly fetched 2026-09-09)
- Overview — https://developer.uber.com/docs/deliveries/overview
- FAQ — https://developer.uber.com/docs/deliveries/faq
- Delivery Window guide — https://developer.uber.com/docs/deliveries/guides/delivery-window
- Proof of Delivery guide — https://developer.uber.com/docs/deliveries/guides/proof-of-delivery
- Delivery Status Webhook — https://developer.uber.com/docs/deliveries/daas/references/api/webhooks/delivery-status-webhook
- Docs index (product list incl. Direct vs Eats vs Guest Trips) — https://developer.uber.com/docs

### Roadie (Layer A — official site, directly fetched 2026-09-09)
- Homepage — https://www.roadie.com/
- Same-Day Delivery solution page — https://www.roadie.com/solutions/same-day

### Dispatch (Layer A — official site, directly fetched 2026-09-09)
- Homepage — https://www.dispatchit.com/
- On-Demand Delivery platform page — https://www.dispatchit.com/platform/on-demand-delivery

### Shipday (Layer A — official site + API docs, directly fetched 2026-09-09)
- Homepage — https://www.shipday.com/
- Docs home — https://docs.shipday.com/
- Delivery Order Object — https://docs.shipday.com/reference/delivery-order-object.md
- Assign (on-demand) endpoint — https://docs.shipday.com/reference/assign.md
- Docs index — https://docs.shipday.com/llms.txt

### Sibling-pass evidence (inherited, not re-fetched)
- research/last-mile-delivery-platform.md (L0, boundary table, the open on-demand flag)
- research/courier-management-platform.md (tenant-identity seam, via STATUS.md)
- research/delivery-scheduling-platform.md (when-structure seam, via STATUS.md)
- research/dispatch-management.md (transversal-machinery seam, via STATUS.md)
- research/food-delivery-marketplace.md (aggregation + order-of-record + fulfillment-coordination core)
- research/delivery-experience-platform.md (no-execution-machinery seam, via STATUS.md)

### Unreachable / limitations
- DoorDash Drive: 403 ×3 (marketing + developer docs) — the second mega-platform network-seller pole is under-observed; no DoorDash-specific claims made anywhere.
- Burq: transport errors ×2 — the multi-network aggregator pole is under-observed.
- DelyvaX: empty fetch — regional (SEA) pole under-observed.
- Uber Direct API reference pages (Direct API, Organizations API) render nav-only (JS); mechanics taken from the FAQ/guides/webhook pages, which are fully static.
- Roadie/Dispatch help centers not fetched; their evidence is product-page level (Tier 2) plus FAQ content embedded in those pages.

## Product Observations

### Uber Direct (evidence layer A — official developer docs)

**Positioning (Overview):** "This platform enables merchants like you to integrate your applications and services with Uber Direct's order delivery system. By leveraging our APIs, you can now easily automate the process of dispatching an Uber courier for pickup and deliveries." Docs cover "creating, managing, and monitoring deliveries using the Uber Direct platform."

**Vendor-drawn Type boundary (Overview):** "The difference Between Uber Direct APIs and Uber Eats Marketplace APIs — The Uber Direct API empowers merchants to seamlessly integrate their applications and services with the Uber Direct order delivery system. Once your application invokes Uber's Create Delivery endpoint, a dedicated Uber courier will be dispatched to collect the order from the store and deliver it to the customer. Conversely, the Uber Eats Marketplace APIs offer partners the capability to programmatically manage various aspects of your stores, menus, and orders on the Uber Eats app." → Direct = dispatch a courier for YOUR orders; Eats = manage presence ON the marketplace. Same vendor, two products, two Types.

**On-demand + scheduled (FAQ):** "Uber Direct empowers our merchants to provide on-demand (ASAP) and scheduled delivery services."

**Delivery windows (Delivery Window guide):** "Delivery windows are time blocks with start and end times that Uber Direct use as guidance… Delivery windows can be set using either the ASAP (As Soon As Possible) or Scheduled (Merchant-driven) methods." Pickup windows (`pickup_ready_dt` / `pickup_deadline_dt`) and dropoff windows (`dropoff_ready_dt` / `dropoff_deadline_dt`). "You can offer ASAP (As Soon As Possible) delivery, which can range from being as soon as 30 minutes after order placement to up to 30 days into the future (Scheduled Delivery)." ASAP guidance: "Drop Off expectation is < 90 minutes in the future from the order creation time."

**Quote → create (FAQ):** a Quote is generated first; "How long is the generated Quote & quote_id valid for? — 15 minutes." The delivery carries a `fee` ("Amount in cents… that will be charged if this delivery is created") and `tip`.

**Status lifecycle (Delivery Status Webhook):** `pending` ("accepted but does not yet have a courier assigned… Uber's actively looking for a courier") → `pickup` FALSE ("Courier is assigned and moving towards the pickup — Via the courier App (manually) after the courier accepted the delivery offer card") → `pickup` TRUE (imminent, GPS-triggered) → `pickup_complete` → `dropoff` FALSE/TRUE → `delivered`; plus `canceled` (CancelDelivery endpoint, Direct Dashboard, or internal), `returned` ("Delivery has been canceled and the undeliverable_action is return (default action)… a new delivery was created to return items to the sender", return IDs prefixed `ret_`), `shopping_completed` (Courier Pick & Pack only). `courier_imminent` = courier ~1 minute away.

**Live courier layer (FAQ + webhook):** Courier Update Webhook "fired every 20 seconds providing updated coordinates on the courier's location." Courier object: name, photo, rating, vehicle type/make/model/plate, lat/lng, anonymized phone + pin code ("Stores can call the anonymized phone_number… After entering the correct pin_code, the call will be connected to the courier"). `tracking_url` — "URL to track the courier during the delivery" (hosted on ubereats.com domain in the sample).

**Batching:** `batch_id` groups deliveries batched with the same courier; `dropoff_sequence_number`; "If a courier cancels the delivery while en route to pick up, we will assign the delivery to another courier; therefore, the batch_id will change."

**Stage-gated editability (FAQ):** an explicit table of which fields can be updated at which stage — e.g., manifest reference and dropoff lat/lng editable only while `Delivery created`/`Pickup started`; dropoff notes editable until `Dropoff imminent`; `tip_by_customer` editable only from `Dropoff started` onward.

**POD (guide):** verification options at pickup/dropoff/return: Signature (with signer name/relationship), Barcodes (scan at pickup/dropoff), Picture (auto-enabled for Leave-at-Door), Identification (government ID photo; "required for restricted items… alcohol, tobacco, and prescription medications"; min-age; failed ID → return trip), Pincode. A per-vertical table maps common verification patterns (Liquor: ID check; Grocery: barcode/picture/pincode; Restaurant: barcode/picture; Pharmacy: ID/signature/pincode; Retail: signature/pincode). POD images retrievable via API; retention windows stated (30 days API / 7 days dashboard for pictures).

**Commerce/ops machinery:** tips increase-only ("Uber's courier tip guarantee"); Refund API + refund webhook; undeliverable_reason/undeliverable_action; cancellation reasons attributed (CUSTOMER_CANCEL / COURIER_CANCEL / MERCHANT_CANCEL / UBER_CANCEL); Organizations API + Business Location Management API (merchant org/store structure, store-level role assignments); Courier Pick & Pack API (courier shops in-store, shopping-progress webhook); Direct Dashboard as the non-API surface; sandbox + robocourier automated delivery testing.

### Roadie (evidence layer A — official site)

**Positioning (homepage):** "Reliable Local Delivery Partner for Same-Day Last-Mile Needs"; "Roadie allows businesses to offer exceptional delivery experiences… with the nation's largest local same-day delivery network." 310,000+ independent drivers; 30K+ zip codes; 97% of U.S. households.

**Speed options (same-day page):** "2-hour, 4-hour, or end-of-day delivery"; configurable cut-off times ("Generally, you want to set cut-off times 2 hours before your pickup location closes"); Local Next-Day as a further option.

**On-demand urgency (homepage):** "Hot Shot Delivery — Urgent Orders, Delivered Fast. Enable your business to deliver in as fast as 2 hours. Hot shot delivery with Roadie enables on-demand, time-critical solutions for your last-minute or urgent order."

**Request creation (same-day page):** "Create deliveries online, by bulk upload, via API or through select UPS systems and integrate seamlessly with your existing infrastructure."

**Pricing (FAQ):** "Pricing for same-day delivery is based on several factors, including: Delivery location, Delivery distance, Item size and weight, Delivery urgency… You can get an instant quote by creating a business account."

**Live follow (FAQ + features):** "Roadie enables real-time tracking for all same-day deliveries. You and your customers can monitor the progress of the delivery, receive updates on its status, and get estimated arrival times."

**Consolidation:** "Consolidated Deliveries — The platform groups multiple deliveries for individual drivers, maximizing productivity."

**Product split:** Roadie Same Day® ("Delivered in 2-12 hours… Ideal for on-demand delivery within 4-6 hours or for ship-from-store deliveries"; "supplementing your own delivery drivers") vs RoadieXD™ ("Delivered in 6-24 hours… leveraging a network of cross-docks"; minimum 50 deliveries per pickup location). Multiple delivery attempts. Bill-to-UPS-account integration.

**Verticals:** retail, auto parts & tires, pharmacy ("pharmacy gig-certified drivers"), industrial, airlines (mishandled baggage), e-commerce, grocery, construction, home improvement. Customer quote: "We tried other on-demand delivery providers, but none could cover all of our stores."

### Dispatch (evidence layer A — official site)

**Positioning (homepage):** "Delivery Orchestration Platform for Enterprise Industrial Distribution"; "Dispatch is the orchestration engine behind modern delivery logistics — an AI-powered platform with a national driver network, built to give businesses control, confidence, and complete visibility over the last mile." "Dispatch unifies on-demand delivery, fleet operations, and integrations into one intelligent platform." "Unified Delivery Orchestration: Apply your business rules, SLAs, and intelligent routing across every delivery—optimizing your owned fleet while coordinating carriers and on-demand drivers in one platform." Scale claims: 57,000+ business locations served, 80+ markets, 30,000+ professional drivers.

**Platform modules:** On-Demand Delivery; Hotshot Delivery ("Get urgent deliveries fast… tracking, access to drivers, and delivery control"); Integrations (ERP/TMS/CRM/eCommerce); Fleet Management ("Optimize your owned fleet with route planning, vehicle capacity, driver assignments, and delivery schedules"); Partnerships; Capabilities.

**On-demand page:** "Schedule time-critical deliveries in minutes and track every mile in real time. Dispatch connects AI-powered routing with a nationwide network of delivery professionals to move what matters with flexible SLAs and transparent pricing."

**Pricing model:** "Price = Base Fare + Vehicle Size + Optional Equipment & Handling Services"; base fare "determined by the trip distance and how fast you need your items delivered"; vehicle classes car → mid-sized → pickup → cargo van → box truck with stated capacities; add-ons (liftgate, dolly, pallet jack, roof/ladder/pipe rack, ramp, dedicated vehicle, extra handling). Enterprise pricing via MSA with SLAs ("performance-backed commitments").

**Request/ops features:** Quick Estimator ("View price estimates, vehicle options, and ideal delivery windows"); Bulk Upload Orders (CSV template); Enhanced Reporting ("spending data, frequent orders, and future forecasts"); Multi-Stop Deliveries ("Schedule multiple deliveries all in one order"); Real-Time Driver ETAs ("View the ETA of the next stop on the route within the dashboard page"); Proof of Delivery ("Upload photos or use the optional signature field to provide customers with proof of delivery"); Branded Notifications ("Add your logo to all customer notifications"); Printable Parcel Labels.

**Self-label straddle:** the same vendor markets "On-Demand Delivery" as a platform module AND the whole platform as a "Last-Mile Logistics Platform"; its comparison table positions Dispatch against "Owned Fleet / DIY Delivery", "On-Demand Courier App", "Route Planning / TMS Software", and "Logistics Platform (Tech)". Its blog: "Delivery orchestration is the new buzzword in last-mile logistics… why routing software with a carrier directory doesn't qualify."

### Shipday (evidence layer A — official site + API docs)

**Positioning (homepage):** "Shipday: AI Delivery Management Software"; "Automate delivery, improve customer communication…"; "Automatically assign orders to your own drivers or delivery partners—without dispatching every order by hand." Built-for list: restaurants, pizzerias, e-commerce, couriers, retail, florists, liquor stores, grocery stores. Features: Branded Tracking, Review Management, Proof of Delivery ("photos, signatures, and accurate delivery timestamps"), Driver Management, Mobile App for Drivers, AI Agents, Reports, Refund Collection, AI Receptionist.

**Two supply poles (docs home):** "Using our APIs, you can build tools to manage your deliveries with your own drivers or use our Delivery Services Gateway and let Shipday handle the complexities of dealing with 3rd party delivery services." FAQ: "Shipday lets you manage your own drivers and third-party delivery providers in a single system. You can dispatch orders, track deliveries, and switch between providers without changing your workflow."

**Delivery Order Object (API):** customer (name/address/phone/geo), restaurant (pickup site), assignedCarrier (own driver or third-party; `null` if unassigned; isOnShift/isActive), distance, activityLog (placementTime → expectedPickupTime/expectedDeliveryDate/expectedDeliveryTime → assignedTime → startTime → pickedUpTime → arrivedTime → deliveryTime), costing (totalCost, deliveryFee, tip, cashTip, discount, tax), paymentMethod, orderItems, orderStatus (accepted; orderState), trackingLink ("Customer tracking url link"), feedback, **schedule flag** ("Indication for the order if it is a scheduled order or not"), etaTime, pickup/delivery instructions, proofOfDelivery (signature/image URLs + completion lat/lng).

**Status enum:** ACTIVE, NOT_ASSIGNED, NOT_ACCEPTED, NOT_STARTED_YET, STARTED, PICKED_UP, READY_TO_DELIVER, ALREADY_DELIVERED, FAILED_DELIVERY, INCOMPLETE.

**On-demand assign to third party (Assign endpoint):** "Assign to a specific 3rd party delivery service provider. Usually, after getting an estimate." API path `POST /on-demand/assign`; OpenAPI title literally "on-demand"; request carries provider name, orderId, tip, estimateReference, contactlessDelivery, podType (PHOTO/SIGNATURE/PIN/NONE); response carries thirdPartyName, thirdPartyFee + shipdayCharge = totalBillableAmount, trackingUrl, driverName/Phone/Lat/Lng, status. SDK class: `OnDemandDeliveryService`; sample: `shipday_obj.OnDemandDeliveryService.assign(order_id=1234, service_name='Uber')`.

**Other API machinery:** Insert/Edit Order, Unassign Order from Driver, Pickup Order Object (pickup-only jobs), Retrieve Carriers / Add a Carrier, Availability, Order Delivery Progress ("Retrieves the real-time delivery progress and ETA for a specific order. This endpoint is designed for public consumption, typically by end-customers, to track their delivery status" — plan-gated, rate-limited per trackingId), Order Status Update webhook, Driver Location Webhook (Beta).

**Customer-facing layer (homepage):** live driver tracking, text notifications, delivery confirmation via text and email, branded tracking pages, post-delivery review requests.

## Cross-product Comparison

| Aspect | Uber Direct | Roadie | Dispatch | Shipday |
|---|---|---|---|---|
| Unit of record | Delivery (del_ id; quote → create) | Delivery (created online/bulk/API/UPS systems) | Delivery order (dashboard/API/bulk CSV/ERP integration) | Delivery order (orderId; insert/edit API) |
| Request anatomy | pickup + dropoff (contact, address, notes) + manifest_items + windows + verification_requirements + fee/tip | pickup/dropoff, item size/weight, urgency, cut-off | pickup/dropoff, vehicle class, add-ons, multi-stop, SLA | customer + restaurant(pickup) + orderItems + expected times + instructions |
| Timing model | ASAP (<90 min expectation) or scheduled windows (up to 30 days) — same machinery | 2h/4h/EOD/next-day; configurable cut-offs; hot-shot urgent | "time-critical deliveries in minutes"; SLAs; hotshot module | per-order expected pickup/delivery times; `schedule` flag |
| Capacity pool | Uber's own courier network (offer card accepted by courier) | crowdsourced independent drivers (310K+) | own managed national network (30K+) + carriers + customer's owned fleet | own drivers + third-party delivery services (gateway) |
| Matching act | courier accepts delivery offer card; reassignment on courier cancel | platform dispatch to network drivers; consolidations | AI-powered routing + network dispatch; fleet optimization module | auto-assign to own drivers; assign-to-provider after estimate |
| Requester surfaces | REST API + webhooks + Direct Dashboard | web portal, bulk upload, API, UPS systems | dashboard, quick estimator, bulk CSV, ERP/TMS/CRM/eCom integrations, API | dashboard (dispatch.shipday.com), API, POS/storefront integrations |
| End-customer surface | tracking_url (live courier tracking) | real-time tracking + updates + ETAs for business and customers | branded notifications; POD shared to customers | trackingLink; public Order Delivery Progress API; text/email confirmations |
| Live telemetry | courier lat/lng webhook every 20s; courier_imminent | real-time tracking (mechanism not detailed on fetched pages) | real-time driver ETAs in dashboard | driver location webhook (Beta); ETA object |
| Closure | delivered + verification evidence (signature/barcode/picture/ID/pin); returned leg auto-created | delivery confirmation; multiple attempts | POD photos/signature; delivery complete | ALREADY_DELIVERED / FAILED_DELIVERY; POD signature/images + geo |
| Pricing | quote (15-min validity) → fee per delivery; tips increase-only | instant quote by distance/size/weight/urgency | base fare + vehicle + add-ons; enterprise MSA | estimate → third-party fee + platform charge; own-fleet deliveryFee can be 0 |
| Failure machinery | undeliverable_action (return default), refund API/webhook, cancel reasons attributed | multiple delivery attempts | (not detailed on fetched pages) | FAILED_DELIVERY state; refund-collection feature |
| Vertical flavor | general parcels; per-vertical verification table (liquor/pharmacy/retail…) | retail/auto/pharmacy/airline/industrial | industrial distribution (HVAC/electrical/plumbing/paint/solar…) | restaurants/pizzerias/liquor/florist/grocery (restaurant object in API) |
| Self-labels | "on-demand (ASAP) and scheduled delivery services" | "same-day delivery network"; "on-demand, time-critical" (hot shot) | "On-Demand Delivery" + "Last-Mile Logistics Platform" + "Delivery Orchestration" | "Delivery Management Software"; API module "on-demand" |

**Convergent reading:** all four organize around a per-delivery request that is priced/estimated, matched at request time to available capacity, executed with live status flowing back to the requester, and closed with delivery confirmation/POD. They differ on: whose capacity (platform network / crowdsourced / own fleet / third-party gateway), the dominant sales surface (API vs dashboard), vertical flavor, and how scheduled the work mix is. None generates consumer demand; all fulfill deliveries for businesses.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The on-demand delivery request as the unit of record.** A persistent, individually identified request for one goods movement — pickup point, drop-off recipient/destination, items/manifest, timing commitment, per-delivery commercial terms — advancing through a real-time status lifecycle (requested → courier assigned → picked up → in transit → delivered / failed / canceled) and closed by delivery confirmation with proof. Remove it → there is no delivery work to match, track, or close (bare courier directory or tracking page).

2. **Real-time matching of the request to available delivery capacity.** At request time, the platform matches the request to an available courier/driver drawn from a supply pool — the platform's own or managed network, a crowdsourced driver base, the business's own fleet, or third-party delivery services reached through a gateway — by per-request assignment (offer/accept, auto-assign, or assign-after-estimate), not by executing a pre-built route plan. Remove it → route-centric orchestration (Last-mile territory) or a static directory with no fulfillment.

3. **The requester-facing live delivery loop.** The requesting business — and commonly the end customer — initiates the delivery through the platform's surfaces (API, dashboard, storefront/checkout integration) and follows it through status events, courier identity/contact, ETAs, and proof of delivery returned to the requester; the platform is the delivery channel of record for the request. Thin historical form: initiate + status relayed on request; mature form: automated live tracking, webhooks, branded tracking pages. Remove it → an internal dispatch board with no service loop facing the requester.

**Jointly-held load-bearing:** (1 alone = a delivery order book with no fulfillment; 2 without 1 = matching machinery with nothing to match; 3 without 1+2 = a tracking/communication skin over someone else's execution = Delivery Experience territory; 1+2 without 3 = the thin historical ancestor — the courier dispatch desk — which satisfies the Type only in its thin form; 1+3 without 2 = request-taking with no capacity, not a platform; 2+3 without 1 = ephemeral dispatch with no record).

### L1 — Common Mature Structure

- Per-delivery quote/estimate before commitment (quote validity windows; estimate references; price by distance/speed/size/urgency/vehicle)
- Courier/driver app: offer cards or assignment feed, status swipes, navigation, POD capture
- Live courier telemetry (location streaming, courier-imminent signals) and ETAs
- End-customer tracking page/URL, branded and shareable; status notifications (SMS/email/push)
- POD capture (signature, photo, pin, barcode scan, ID check) with per-vertical verification patterns
- Batching/multi-stop on one courier; consolidation
- Failure machinery: failed-delivery states, undeliverable actions, return legs, refunds/claims, attributed cancellation reasons
- Merchant configuration: organizations/stores/locations, roles, vehicle classes, verification defaults, cut-off times
- Integration spine: e-commerce/POS/ERP intake, webhooks, SDKs
- Tips and courier-side economics (tip guarantees, increase-only rules)
- Reporting/analytics (spend, performance, forecasts)

### L2 — Variant / Optional Structure

- **Supply model** (the deepest axis): platform-owned/managed courier network (network-seller pole) vs crowdsourced driver base vs own-fleet dispatch software vs third-party gateway/aggregation — a business can be in-type without owning any drivers, and in-type while using only its own drivers
- **Sales form:** API-first white-label (embed delivery into the merchant's own checkout/app) vs dashboard-first SaaS vs hybrid
- **Timing mix:** ASAP-dominant vs scheduled-window-heavy vs urgent/hot-shot specialization; scheduled windows ride the same request machinery (a scheduled delivery is still a matched, tracked, POD-closed request)
- **Vertical packaging:** food/restaurant, industrial distribution, retail, pharmacy (regulated verification), auto parts, airlines, big & bulky (vehicle-class ladders, equipment add-ons)
- **Customer tier:** mega-platform API customers, enterprise (MSA/SLA commercial models), SMB self-serve
- **Geography:** US-dominant samples; regional on-demand couriers exist (under-observed this pass)
- **Adjacent modules:** fleet management/route planning (orchestration-hybrid pole), shopping/pick-and-pack (courier shops in-store), review/reputation machinery, refund collection services

### L3 — Vendor-specific (research notes only)

- Uber Direct: 15-minute quote validity; 20-second courier-update cadence; ~80 m courier_imminent threshold; `del_`/`ret_`/`bat_`/`rte_` ID scheme; robocourier sandbox testing; Sobriety check default on alcohol-flagged orders; tip increases allowed up to 3 weeks post-trip; POD image retention windows (7 days dashboard / 30 days API); anonymized courier phone + pin code; tracking hosted on an ubereats.com URL; Courier Pick & Pack API; per-vertical verification recommendation table
- Roadie: 310K+ drivers / 97% households / 30K+ zip codes coverage claims; 144-inch/300-lb item ceiling (150 lbs consumer); Same Day (2–12 h) vs RoadieXD (6–24 h, cross-dock network, 50-delivery minimum per pickup location); bill-to-UPS-account; cut-off guidance (2 h before location close)
- Dispatch: price formula (base fare + vehicle size + equipment/handling); vehicle class ladder with capacity specs (car 240 lbs → box truck 12,500 lbs / 12 pallets); add-on catalog (liftgate, dolly, pallet jack, racks, ramp, dedicated vehicle); National Delivery Guarantee tied to MSA; Gartner Digital Markets "Last-Mile Delivery Software" category recognition; 57,000+ locations / 30,000+ drivers scale claims
- Shipday: orderState enum values; activityLog field set; `/on-demand/assign` endpoint shape (thirdPartyFee + shipdayCharge = totalBillableAmount); POD enum PHOTO/SIGNATURE/PIN/NONE; public tracking endpoint plan-gated (BUSINESS ADVANCED) with per-trackingId rate limit; Delivery Services Gateway branding; AI receptionist/review/refund-collection feature set; 30-language localization

## Rejected Findings (considered and rejected as core)

- **ASAP-only semantics** — rejected: Uber Direct explicitly supports "on-demand (ASAP) and scheduled delivery services" up to 30 days ahead; Shipday carries a `schedule` flag; Roadie sells next-day. The invariant is per-request arrangement at request time, not immediacy per se. ASAP is the dominant mode, not the boundary.
- **Platform-owned courier network** — rejected: Shipday's own-fleet pole and third-party gateway prove a platform can be in-type without operating drivers; Roadie/Uber Direct/Dispatch prove the network pole. Supply model is the Type's deepest variant axis, not its definition.
- **API-first form** — rejected: Shipday and Dispatch are dashboard-first SaaS; API is common-mature, not definitional.
- **Per-delivery dynamic pricing** — rejected as definitional: quote/estimate machinery is common to all four, but own-fleet deliveries can carry zero delivery fee (Shipday `deliveryFee: 0`); held common-mature.
- **Live GPS tracking / courier-imminent signals** — rejected as definitional: common-mature in all four, but the historical thin form (status relayed on request) satisfies the Type; the automated live layer is era machinery (same reasoning as the last-mile pass's recipient-notification rejection).
- **POD as the product** — rejected: POD is the closing step of the request lifecycle here; the POD-centric product belongs to the proof-of-delivery-platform leaf (noted for that pass).
- **Food/restaurant semantics** — rejected: Shipday's restaurant object is origin flavor; Dispatch is industrial; Roadie is retail/auto/pharmacy/airline.
- **Consumer marketplace / demand generation** — rejected: no sampled product generates consumer demand; all fulfill deliveries the business already sold. The last-mile pass's tentative reading of this leaf as "consumer-facing instant-delivery marketplace with its own demand generation" is **corrected** by this pass: that description belongs to Food Delivery Marketplace (§26, processed). The actual market population of "on-demand delivery platform" products is merchant/business-facing delivery machinery.
- **Route optimization / route planning as core** — rejected: present as a module in the orchestration-hybrid pole (Dispatch Fleet Management, Shipday route planning) and absent as the organizing act in the network-seller pole; the organizing act here is per-request matching.
- **Return/refund machinery as core** — common-mature in the network-seller pole (Uber Direct return legs + refund API; Shipday refund collection), not observed on the fetched Dispatch pages; held optional.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| **Last-mile Delivery Platform** (processed) | closest sibling; **keep-both ratified; open flag settled** | Shared execution substrate (delivery tasks, drivers, live tracking, POD). The seam is the **organizing act**: here, each request is matched to capacity at request time (offer/assign-after-estimate), with no route plan as the organizing object; there, the operator's delivery work is organized as planned, sequenced, batched route execution over a day. On-demand work appears inside last-mile products as a work-mix mode (ratified by that pass); on-demand-native products organize around the request loop and sell delivery-as-a-service (white-label/API or managed network). Remove the near-now per-request matching → route-centric last-mile; remove route/day-plan orchestration and keep request→match→track → this Type. The straddle is real and documented: Dispatch self-labels both "On-Demand Delivery" and "Last-Mile Logistics Platform"; Roadie markets "same-day last-mile". Straddles are branding over a shared substrate, not structure. |
| **Food Delivery Marketplace** (§26, processed) | channel vs machinery; vendor-drawn seam | The marketplace aggregates many sellers on a consumer surface, owns the consumer order of record, and mediates demand; this Type is the delivery machinery behind any seller, with no consumer aggregation. Uber's own documentation draws the seam: Direct APIs "dispatch an Uber courier… to collect the order from the store and deliver it to the customer" vs Eats Marketplace APIs that "manage… stores, menus, and orders on the Uber Eats app." DoorDash's Drive (white-label delivery) vs DoorDash marketplace is the same two-products-one-vendor pattern (Drive itself unreachable this pass — pattern asserted from the Uber-side evidence only). Remove the delivery machinery → marketplace; remove the consumer aggregation → this Type. |
| **Courier Management Platform** (processed) | operator-business frame vs service loop | The courier Type is the delivery operator's *business* system: courier orders for external customer accounts, contracted-rate pricing, billing, driver pay. This Type is the request→match→track service loop itself, whether operated by a network seller (which internally needs courier-like machinery) or used by a merchant for its own fleet. The paper-era courier dispatch desk is the shared historical ancestor: with the operator business frame it grows into courier management; as a service sold to requesters it is this Type. Remove the request-loop service framing and add customer accounts/rates/billing → courier management. |
| **Delivery Scheduling Platform** (processed) | when-structure vs request-loop | Scheduling owns the when-structure: offered windows, availability rules, the schedule as the worked object, customer-facing slot booking. Here, timing is an attribute of the request (ASAP or a window) and scheduled windows ride the same matching machinery; there is no availability structure being worked. Remove the request/matching loop → scheduler; remove the when-structure center → this Type. |
| **Dispatch Management** (processed) | transversal machinery inside the Type | Dispatch owns the generic assignment loop (work queue × roster × assignment act × live picture) for any field work. This Type adds delivery-domain semantics: goods requests with pickup→dropoff anatomy, per-delivery pricing, requester-facing tracking, POD closure. Remove delivery semantics and the requester-facing service loop → generic dispatch. |
| **Delivery Experience Platform** (processed) | execution vs communication | Experience platforms assemble/normalize delivery state from carrier/fulfillment feeds and own the brand-facing communication surface, with **no execution machinery**. Here the platform executes the delivery it tracks. Remove execution → delivery experience; remove the experience layer → still this Type (thin form). |
| **Ride-hailing Platform** (unprocessed) | same matching machinery, different object | Both match real-time requests to nearby drivers with live tracking. The object differs: people-movement (ride) vs goods-movement (delivery request with items/manifest, POD, per-delivery pricing). Uber's own product split documents the seam — Guest Trips (rides) and Direct (deliveries) are separate API products. Note left for that pass. |
| **Proof of Delivery Platform** (unprocessed) | closing step vs POD-first product | POD here is the closure of the request lifecycle (one verification step among lifecycle machinery). The POD-centric product (capture-first, POD-as-deliverable) is a separate leaf; noted for that pass. |
| **Parcel Management Platform** (unprocessed) | different phase/model | Parcel management = shipper-side multi-carrier shipping execution (rate shopping, labels, manifesting, carrier accounts) before carrier handoff. Here the platform IS the (on-demand) carrier capacity or dispatches it per request. Note left for that pass. |
| **Shipment Visibility Platform** (unprocessed) | watching vs executing | Visibility aggregates/normalizes shipment state across carriers for freight the tenant does not execute; this Type executes (or dispatches) the delivery itself. |
| **Service Marketplace** (§05.02) | venue vs fulfillment | A service marketplace matches demand to service providers as the product; here matching is the fulfillment mechanism for goods the business already sold, not the market itself. |

## Uncertainties

1. **DoorDash Drive** unreachable (403 ×3). The second mega-platform network-seller pole is characterized only via the Uber-side vendor-drawn seam and Shipday's third-party integration surface (`service_name='Uber'` sample; DoorDash among Shipday's integration logos). No Drive-specific claims made.
2. **Burq** (multi-network aggregator pole) unreachable (transport errors ×2). The aggregator-of-networks variant — one platform routing requests across several courier networks — is under-observed; the gateway concept is evidenced only through Shipday's Delivery Services Gateway.
3. **Regional products** (DelyvaX SEA unreachable; AU/EU on-demand couriers not sampled). The Type is asserted to be geography-independent from the machinery's structure; regional verification is incomplete.
4. **Roadie/Dispatch operational depth** (driver-app mechanics, exact status vocabularies, failure handling) verified only at product-page level; their help centers were not fetched. Claims about these two products kept at the level their pages support.
5. **Exact status vocabularies** are product-specific (Uber Direct's pending/pickup/dropoff set vs Shipday's 10-value enum); the final document uses conceptual states.
6. **Whether a pure consumer-facing "on-demand delivery" app exists as a distinct software population** (as opposed to marketplaces) was not found; the consumer instant-delivery market is realized through marketplace products (Food Delivery Marketplace territory). If a future pass finds a consumer-facing on-demand delivery software population, the boundary row vs Food Delivery Marketplace should be revisited.
7. **The work-mix overlap with last-mile** is acknowledged rather than resolved away: products on both sides absorb the other's work mode. The seam is center of gravity, and straddle products (Dispatch) are documented as such.

## Final Synthesis

An On-demand Delivery Platform is the delivery-machinery Type whose defining core is three jointly-held structures: (1) the on-demand delivery request as the unit of record — a persistent, identified request for one goods movement (pickup → drop-off recipient, items, timing, per-delivery terms) advancing through a real-time status lifecycle to a POD-closed confirmation; (2) real-time matching of the request to available delivery capacity at request time — offer/accept, auto-assign, or assign-after-estimate against a supply pool that may be the platform's own network, a crowdsourced base, the business's own fleet, or third-party services via a gateway — rather than execution of a pre-built route plan; (3) the requester-facing live delivery loop — the business (and commonly the end customer) initiates through the platform's surfaces and follows status, courier identity, ETA, and proof of delivery to closure. Around this core sits the mature stack: per-delivery quotes, courier apps, live telemetry, branded tracking pages, per-vertical verification, batching, failure/return/refund machinery, merchant configuration, and an integration spine. The Type's deepest variant axis is the supply model (network-seller vs own-fleet vs third-party gateway); its deepest packaging axis is API-first white-label vs dashboard SaaS. The Type is defined by the request loop, not by demand generation — no sampled product generates consumer demand, which corrects the last-mile pass's tentative hold and locates the consumer-aggregation reading in Food Delivery Marketplace. Taxonomy verdict: **confirmed standalone Type; keep-both with Last-mile Delivery Platform on the organizing-act seam (settling that pass's open flag), with Food Delivery Marketplace on the channel-vs-machinery seam (vendor-drawn), with Courier Management on the operator-business-frame seam, and with Delivery Scheduling on the when-structure seam.** Historical check passed: the paper-era courier dispatch desk (request slip + dispatcher matching + status relay) satisfies all three legs in thin form; the definition names no GPS, apps, dynamic pricing, or API.
