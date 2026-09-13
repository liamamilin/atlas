# Research Notes — Restaurant Delivery Management

Research date: 2026-09-09

## Research Goal

Understand what a Restaurant Delivery Management application actually is from real products: what objects exist inside it, who operates it, how a delivery order flows from the restaurant to a customer's door, how fulfillment resources (own drivers vs third-party delivery services) are represented and dispatched, what configuration and rules govern the operation, and where the Type's boundary sits against Food Delivery Marketplace, Restaurant Online Ordering, and generic last-mile delivery platforms.

## Initial Boundary

Working hypothesis before research:

- Core use: the restaurant-side system for managing delivery as an order fulfillment channel — delivery orders, courier/driver dispatch, delivery progress tracking, delivery availability/fee configuration.
- Primary users: restaurant operators/managers, delivery coordinators, own drivers; enterprise digital teams.
- Nearest neighbors: Food Delivery Marketplace (consumer side), Restaurant Online Ordering (customer-side order capture), Last-mile / On-demand Delivery Platform (generic logistics), Courier Management Platform (courier company's own business system), Delivery Scheduling Platform, Proof of Delivery Platform, Dispatch Management (generic), Restaurant POS / Restaurant Management System.
- Unknowns: weight of own-fleet vs white-label-network vs marketplace-mediated fulfillment; whether driver apps and zone configuration are definitional; historical shape.

## Research Questions

1. What is a "delivery order" in these systems, and how does it relate to the restaurant's normal order flow (POS / online ordering)?
2. How are fulfillment resources represented — own drivers vs third-party delivery service providers (DSPs)? How are they dispatched (manual vs rule-based)?
3. What is the delivery lifecycle? What states exist from order acceptance to delivered/failed?
4. What delivery configuration exists (availability, fees, order-size limits, transit-time limits, vehicle types, provider selection rules)?
5. Which surfaces exist: operator dashboard, store-side app, courier app, customer tracking, settings, analytics?
6. How are exceptions handled: no courier available, courier cancellation, undeliverable, refunds, cancellations?
7. How do marketplace orders (own-delivery agreements) enter the system, and is that part of this Type or an adjacent capability?
8. Historical check: would older / regional / own-driver-only restaurant delivery operations fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence quality |
|---|---|---|---|
| Olo (Dispatch + Rails) | Enterprise orchestration: multi-DSP quote/bid dispatch on brand-owned ordering; marketplace-order consolidation as a sibling product | Enterprise chains | Tier 1 (Help Center) + Tier 2 (product pages) |
| Toast (Toast Delivery Services + third-party delivery integrations) | POS-anchored: delivery service inside the restaurant platform; partner-network drivers; separate marketplace-integration product line | SMB / mid-market | Tier 2 (product pages) |
| Deliverect (Dispatch + Courier App + DMA) | Integration hub: orders from first-party and external platforms; hybrid own-fleet + global courier-network routing; store-side tablet app | Enterprise / multi-location / dark kitchens | Tier 1 (Help Center) + Tier 2 (product pages) |
| Uber Direct | White-label delivery-network API: merchant-side create/manage/monitor deliveries dispatched to Uber couriers; no ordering layer of its own | Any merchant incl. restaurants | Tier 1 (developer docs) |

DoorDash Drive was intended as a second white-label-network pole; its developer docs returned HTTP 403 (see Sources — limitations). The pole is instead covered by Uber Direct directly plus Deliverect/Toast documentation of DoorDash Drive as an integrated partner.

## Sources

Fetched 2026-09-09:

- Olo product pages: https://www.olo.com/ , https://www.olo.com/dispatch , https://www.olo.com/rails
- Olo Help Center (Zendesk): search results for "dispatch"; Dispatch Overview (article 115000835946); Dispatch Store Settings (article 360026943032); Dispatch Order Tracker Overview (article 360055693951)
- Toast: https://www.toasttab.com/ ; Toast Delivery Services (https://pos.toasttab.com/products/toast-delivery-services); Third-party delivery integrations (https://pos.toasttab.com/third-party-delivery-integrations)
- Deliverect: https://www.deliverect.com/ ; Dispatch by Deliverect (https://www.deliverect.com/en/dispatch); Help Center root (https://help.deliverect.com/) incl. Dispatch / Courier App / My Couriers / Live View / DMA collections; Dispatch: My Couriers (article 9399812)
- Uber Direct developer docs: Overview (https://developer.uber.com/docs/deliveries/introduction); Delivery Status Webhook (https://developer.uber.com/docs/deliveries/daas/references/api/webhooks/delivery-status-webhook)

Limitations:

- https://developer.doordash.com/docs/drive → HTTP 403 (not retried further per network rules). DoorDash Drive is therefore evidenced only indirectly (as a dispatch partner inside Deliverect/Toast documentation).
- Toast evidence is product-page level (Tier 2); Toast's operational help-center articles for delivery were not fetched. Claims from Toast are held at positioning/scope strength, not workflow detail.
- help.deliverect.com search URL 404'd; the help-center root and the My Couriers article were fetched successfully instead.
- No pricing, numeric limits, or SLA figures are asserted in the final document beyond what fetched pages state.

## Product Observations

### Olo — Dispatch (and Rails)

Evidence layer: A (direct observation, Help Center + product pages).

- Page title of the Dispatch product page is literally "Restaurant Delivery Management Software | Olo Dispatch" — the market's own naming for this Type.
- Positioning: "Satisfy demand for direct delivery and eliminate the need to manage a courier fleet"; "By automatically pairing third-party couriers with delivery orders, Dispatch provides a consistent guest experience."
- Workflow (Dispatch Overview, Help Center):
  1. Customer orders on the brand's own site/app and pays ahead.
  2. At checkout the customer selects Delivery and enters an address.
  3. The system returns the best-matched quote from available DSPs; customer sees delivery fee + estimated delivery time.
  4. The order is sent to the store "like all online orders"; a DSP courier picks up and delivers.
  5. Customer tracks the whole delivery live from the ordering site/app.
- "Orders are processed just like all other online orders, with a delivery courier making the pickup instead of a customer."
- Direct-channel framing: brand owns the guest relationship and data; loyalty integration; no per-order commission (customer pays delivery in the Dispatch model).
- Store Settings (per store): Dispatch on/off toggle (delivery availability); Multiple Quote Tie-Breaker (fastest vs cheapest); Min/Max Dispatch Order Amount; Max Dispatch Delivery Fee (quotes above are rejected); Max Transit Time (quotes above are rejected); Allowed Delivery Vehicle Types (walker, bicycle, delivery bicycle, car, van); Preferred Providers (first right of refusal; tiered bidding); Blocklisted Delivery Providers; Cancel Notification Emails; Support CC emails; Pickup Instructions shown to the courier in their app; Quick Ticket (automated support tickets); Automated Guest Refunds for unsuccessful deliveries; delivery-fee tax toggle; Allow Advance Orders (future/scheduled orders); Priority Order Value and Provider (high-value orders to specialist providers); Dispatch Fee Tiers (fee types incl. direct passthrough of DSP fee to guest); Driver Tip Distribution (percentage of guest tip to driver vs restaurant).
- "Delivery providers and self-delivery options" — own-driver operation is a supported mode alongside DSPs.
- Automated Delivery Rescue — automated re-dispatch when a delivery fails.
- Order Tracker (customer surface): real-time map on the order-confirmation page; courier location polled and auto-updated; ETA and driver info; stops updating at "Delivered"; customizable "Pickup In Progress" messaging.
- Rails (sibling product, marketplace side): consolidates orders from multiple third-party marketplaces into one place, two-way menu/pricing/availability sync, no manual entry, sales/error analytics. Distinct product line from Dispatch.

### Toast — Toast Delivery Services + third-party delivery integrations

Evidence layer: A for scope/positioning (product pages); workflow detail not fetched.

- Toast Delivery Services sits in the "Digital Storefront Suite" next to Online Ordering, Websites, Branded Mobile App, and "Grubhub, Uber Eats, DoorDash" integrations.
- Positioning: "Low-cost, zero commission delivery… flat-fee delivery, staffed by our delivery partner network of on-demand drivers."
- "We've got a network of on-demand Uber and DoorDash drivers… You choose the solution that works for you." — provider choice at setup.
- Expense controls: "options to adjust minimum ticket sizes or to pass portions of your delivery fee on to your guests."
- Guest relationship: "We build your guest directory from direct orders, in-store or online."
- Third-party delivery integrations (separate product line): sync Uber Eats/Grubhub/DoorDash orders directly to the POS — "orders flow straight to the kitchen, double entry disappears… ditch the extra tablets"; centralized third-party menu management; 86 items across platforms; "just like any other order at your restaurant."

### Deliverect — Dispatch + Courier App + Delivery Manager App (DMA)

Evidence layer: A (product pages + Help Center).

- Dispatch positioning: "Automatically route orders to the best last-mile partner every time, whether it's the cheapest, fastest, or your preferred provider"; "distributing orders across owned and third-party fleets automatically."
- Stated flow: (1) an order arrives from first-party channels or external platforms; (2) Dispatch evaluates rules to select the best last-mile partner; (3) order details transfer to the courier instantly.
- Routing rules: cheapest provider, fastest delivery time, preferred partner, day and time, delivery distance; per-location configuration.
- Global courier network across 52 countries; partners named include Uber Direct, DoorDash Drive, Wolt Drive, Stuart; dozens of per-partner configuration articles (A2B, DLIVRD, Cartwheel, Glovo On-Demand, Foodora Go, …).
- FAQ: "an all-in-one delivery management platform… combining your own fleet management with access to top global on-demand drivers." Use cases include "handling orders from third-party delivery apps under an 'own-delivery' agreement."
- Own-fleet pole (Deliverect for Couriers / Courier App / My Couriers, Help Center):
  - My Couriers page: manage couriers, status, locations they deliver for; add a courier by having them scan a QR code in the Couriers App; link/unlink locations; per-courier stats (total deliveries, distance, earned tips).
  - Settings: enable cash payments (track cash held, cash-out threshold); "assign orders to a delivery partner when none of my couriers are available" (fallback); "allow only the store manager to assign new delivery jobs" (couriers notified but cannot self-accept; jobs assigned from Live View); enforce location sharing; geofencing check when marking "Delivered"; couriers can mark themselves on break.
- Store-side surface: Delivery Manager App (tablet/web) — manage orders, amend order, pack items, update preparation time, view a rider's location (dispatch partners), courier updates, order status and flow, cancel the delivery of an order, request multiple couriers, mark order as ready for pickup, order alerts; usable with or without an integrated POS.
- Dispatch console surfaces: Live View page (assignment/monitoring), Deliveries page, Insights, Auto-selection configuration, per-location partner activation.
- Sibling capabilities: Sentinel (store status monitoring, auto-reopening offline stores), Deliverect Restaurants (order/menu hub), Deliverect Direct (first-party ordering).

### Uber Direct

Evidence layer: A (developer documentation).

- Positioning: merchant-side white-label delivery. "Once your application invokes Uber's Create Delivery endpoint, a dedicated Uber courier will be dispatched to collect the order from the store and deliver it to the customer."
- Explicit Type boundary, from Uber's own docs: Uber Direct APIs (merchant-side dispatch) vs Uber Eats Marketplace APIs (managing stores/menus/orders on the consumer marketplace). Two different products.
- Delivery lifecycle (Delivery Status Webhook): pending (accepted, no courier yet) → pickup (courier assigned, en route; courier_imminent flag when ~1 minute away) → pickup_complete → dropoff (en route; imminent flag) → delivered; plus canceled and returned (undeliverable with return action creates a linked return delivery with its own lifecycle); shopping_completed for the Pick & Pack variant.
- Delivery object: pickup and dropoff with addresses/contacts/notes; pickup_ready/pickup_deadline and dropoff_ready/dropoff_deadline windows; ETAs; fee; tip; manifest items (name, quantity, size, dimensions, price); courier info (name, vehicle type, masked phone with pin code, live location, license plate); tracking_url; verification requirements and results (signature with signer name/relationship, barcode scan, photo, pincode, ID min-age check); undeliverable_reason/undeliverable_action; cancellation reasons (CUSTOMER_CANCEL / COURIER_CANCEL / MERCHANT_CANCEL / UBER_CANCEL); batching (multiple deliveries to one courier; batch id changes on courier reassignment).
- Webhook events: delivery status, courier update, refund request, shopping progress.
- Companion APIs: Direct API, Organizations API, Courier Pick & Pack API, Refund API, Business Location Management API; guides for proof of delivery, pincode, delivery window, geocoding; a Direct Dashboard for managing deliveries; sandbox + pilot onboarding process.

## Cross-product Comparison

| Dimension | Olo Dispatch | Toast Delivery Services | Deliverect Dispatch | Uber Direct |
|---|---|---|---|---|
| Delivery order bound to restaurant order flow | Yes — order flows to store "like all online orders" | Yes — inside the restaurant platform; orders flow to POS/kitchen | Yes — orders from first-party channels or external platforms; DMA handles order prep states | Partially — generic delivery object (manifest items are packages); restaurant is one merchant type |
| Fulfillment resources | 27+ DSPs + self-delivery option | Partner network of on-demand Uber/DoorDash drivers | Own couriers + global courier-network partners (52 countries) | Uber courier fleet only |
| Dispatch decision | Automatic quote/bid across DSPs; tie-breaker fastest/cheapest; preferred providers first right of refusal | Provider chosen at setup | Rule-based auto-selection (cheapest/fastest/preferred/time/distance) per location; manual assignment option (Live View; manager-only mode) | Merchant (or its software) creates the delivery; Uber dispatches internally |
| Delivery lifecycle tracking | Yes — statuses incl. Pickup In Progress, Delivered; customer tracker | Implied by product scope (not fetched in detail) | Yes — Live View, courier updates, order status and flow | Yes — explicit state machine (pending → pickup → pickup_complete → dropoff → delivered; canceled/returned) |
| Customer-facing tracking | Yes — live map, ETA, courier info | Not observed in fetched pages | Yes — rider location view; courier updates (incl. forwarding updates to Uber Eats) | Yes — tracking_url |
| Courier-facing app | DSPs' own apps; pickup instructions delivered to courier app | Partner drivers' apps | Own Couriers App (QR onboarding, job accept/assignment, location sharing, break status) + partner apps | Uber courier app (offer card, swipes, GPS-imminent detection) |
| Availability / eligibility configuration | Per-store toggle; min/max order amount; max fee; max transit time; vehicle types | Minimum ticket sizes; fee pass-through options | Per-location partner activation; auto-selection rules; opening hours/busy mode (DMA) | Delivery windows; geocoding; business location management |
| Fee economics | Fee tiers; passthrough; tip distribution; delivery-fee tax | Flat fee per order; pass portions of fee to guests | Cost-based partner selection | Fee + tip fields on the delivery object |
| Exception handling | Automated Delivery Rescue; Automated Guest Refunds; Quick Ticket; cancel notification emails | Not observed in fetched pages | Fallback to partner when no own courier; cancel delivery; order alerts; Sentinel store monitoring | Canceled/returned states; undeliverable reason/action; refund webhook; courier reassignment |
| Proof of delivery / verification | Not observed in fetched pages | Not observed | Geofencing check on "Delivered" | Signature, photo, pincode, barcode, ID min-age |
| Scheduled orders | Allow Advance Orders | Not observed | Ordering slots (Direct Suite); delivery windows (Uber Direct as partner) | Delivery windows (pickup/dropoff ready/deadline) |
| Marketplace-order ingestion | Sibling product (Rails) | Sibling product line (third-party delivery integrations) | In-scope: orders from external platforms under own-delivery agreements | No (out of scope by design) |
| Form factor | Operator dashboard + embedded customer tracker | Platform module | Operator dashboard + store tablet app + courier app | REST API + webhooks + dashboard |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Restaurant Delivery Management application:

1. **The delivery order as the unit of record** — a restaurant order designated for off-premise delivery to a customer address: menu items, customer contact and address, payment state, bound to the restaurant's order flow (it is "just like any other order" except that a courier, not the customer, collects it). Remove → a generic courier/parcel dispatch system or a last-mile platform.
2. **Courier assignment (dispatch)** — each delivery order is bound to a fulfillment resource: the restaurant's own driver or an external delivery service, chosen by rule (auto-selection, quote/bid) or by hand (manager assignment). Remove → online ordering / order aggregation with no fulfillment machinery.
3. **Delivery progression tracking to a closed outcome** — the delivery advances through a lifecycle (assigned → en route to pickup → picked up → en route to customer → delivered, with canceled / undeliverable outcomes) and its state is visible to the restaurant, commonly also to the customer. Remove → a static dispatch list or order report; the operational loop is gone.

Jointly-held load-bearing analysis:

- 1 alone = a list of delivery orders (channel report), no fulfillment.
- 2 without 1 = driver roster / courier network with nothing restaurant-specific to deliver.
- 3 without 1+2 = generic shipment tracking.
- 1+2 without 3 = a dispatch board with no closure — "management" gone.
- 1+3 without 2 = order tracking without fulfillment assignment (marketplace-style tracking page).

### L1 — Common Mature Structure

Present across the sample; expected in mature products but not definitional:

- Delivery availability configuration per store/location (enable/disable delivery, hours, min/max order amounts).
- Fulfillment-resource configuration: preferred / blocklisted providers, auto-selection rules (cheapest, fastest, preferred, time of day, distance), allowed vehicle types, quote-rejection ceilings (max fee, max transit time).
- Fee economics: who pays the delivery cost (customer vs restaurant), fee presentation at checkout, tips and tip distribution between guest/restaurant/driver.
- Customer-facing delivery tracking (tracking link or live map, ETA, courier identity).
- Courier-facing app: job offer/assignment, pickup and dropoff confirmations, location sharing.
- Exception machinery: cancellations from multiple parties, undeliverable handling (return), refunds, automated support tickets, re-dispatch ("rescue"), fallback to another provider when no courier is available.
- Proof-of-delivery / verification options (signature, photo, pincode, barcode, age verification).
- Scheduled / advance orders with pickup/dropoff windows.
- Handoff of the order into store systems (POS / kitchen) so delivery orders are prepared like all other orders.
- Delivery analytics (performance by provider/location, courier stats, error/refund reasons).

### L2 — Variant / Optional Structure

Depends on segment, geography, business model:

- Fulfillment mix: own fleet only / third-party network only / hybrid with fallback rules.
- Marketplace-order ingestion as a delivery-order source (own-delivery agreements with marketplaces) — present in some products, a sibling product line in others, absent by design in the API pole.
- Menu/pricing synchronization to marketplaces (adjacent capability, sometimes bundled).
- Store-status monitoring with automatic reopening (single-product-dominant in sample).
- White-label API form factor (no operator UI of its own) vs operator-dashboard form factor.
- Cash-on-delivery handling and cash-out thresholds (own-fleet pole).
- Geofencing enforcement on delivery completion; alcohol/age verification.
- Catering / high-value orders routed to specialist providers.
- Batched deliveries (one courier, multiple dropoffs).

### L3 — Vendor-specific (stays in Research Notes)

- Olo: Dispatch/Rails product split; Skip the Line; Quick Ticket; Automated Guest Refunds; Food Freshness; Multiple Quote Tie-Breaker; Priority Order settings; "27+ DSPs / 96% covered by 2+" marketing stats.
- Toast: Toast Delivery Services flat-fee packaging; guest-directory building; Toast Local; "20%+ more in sales" internal-data claim.
- Deliverect: Sentinel; DMA tablet; Courier App QR onboarding; geofencing setting; "52 countries / 29-minute average" marketing stats; Deliverect AI agents.
- Uber Direct: robocourier automated testing; pincode; Organizations API; Courier Pick & Pack (shopping tasks); batch/route identifiers; masked courier phone with pin code.

## Anti-overfitting Notes

- **Third-party DSP networks are NOT definitional.** The own-fleet pole exists in-sample (Deliverect for Couriers; Olo's self-delivery option) and dominated historically. The invariant is the assignment of a fulfillment resource, whatever its employment shape.
- **Multi-provider quote/bid marketplaces are NOT definitional.** Toast (single network choice at setup), Uber Direct (single network), and own-fleet operation all satisfy the Type without bid matching. Olo's tie-breaker settings and Deliverect's auto-selection rules are one realization of dispatch decisioning, not the definition.
- **Customer live map is NOT definitional.** Progress tracking is L0; the auto-updating map is the modern realization (Uber Direct exposes a tracking_url; older operations used phone check-backs).
- **Checkout-time fee/ETA quotes are NOT definitional.** They presuppose the multi-DSP pattern; own-fleet and single-network operations price delivery by flat fee or policy instead.
- **Marketplace-order ingestion is NOT definitional.** It appears as a sibling product (Olo Rails, Toast integrations), as in-scope order source (Deliverect), or not at all (Uber Direct). The dispatch core stands without it.
- **POS integration is NOT definitional as a mechanism.** Uber Direct has no POS surface at all; the conceptual requirement is that the delivery order belongs to the restaurant's order flow, however that flow is realized.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Pre-app pizzeria with own drivers: phone order marked "delivery" with a customer address (delivery order); dispatcher assigns a driver from the driver board (assignment); run sheet and phone check-backs until the driver returns (progression to closed outcome). Fits all three legs.
- Restaurant contracting a local white-label delivery service: order phoned/faxed to the service, which sends a driver; restaurant follows up by phone. Fits (assignment via the contracted service).
- Modern API-first merchant (any vertical, incl. restaurants) calling a create-delivery endpoint and consuming webhooks. Fits — this is Uber Direct's exact shape, and it proves the Type survives without any operator UI.
- Marketplace-only restaurant (no own delivery, no white-label): orders arrive with the marketplace's own courier already attached; the restaurant controls preparation, not dispatch. This sits at the boundary — the restaurant side of that relationship is order management (Rails/Toast-integrations territory), not delivery management. Recorded as a boundary finding, not a failure of the definition.

The definition therefore does not over-fit to the current multi-DSP, app-mediated market shape.

## Vendor-specific Findings

See L3 above. None of these enter the canonical core.

## Boundary Findings

| Neighboring Type | Relationship | Distinction | "Remove what to become the other Type" |
|---|---|---|---|
| Food Delivery Marketplace | adjacent, most confusable | Marketplace is the consumer-facing venue aggregating many restaurants with its own demand, courier fleet, and commission economics; RDM is the restaurant-side fulfillment system. Uber's own docs split Direct (merchant-side) from Eats Marketplace APIs; Olo contrasts "you control the guest experience" with "sending customers to a marketplace" | Remove the restaurant-side operator perspective and add consumer-facing multi-restaurant aggregation → marketplace |
| Restaurant Online Ordering | upstream, complementary | Ordering captures the order (customer-side checkout); RDM fulfills it (operator-side dispatch). Olo Dispatch explicitly rides on the ordering checkout ("at checkout, the customer selects Delivery") | Remove courier assignment and delivery lifecycle → online ordering |
| Last-mile / On-demand Delivery Platform | substrate / generic sibling | Generic platforms move any parcel for any merchant; RDM's unit is a restaurant order (menu items, prep timing, food context, store handoff). Uber Direct is the generic substrate that RDM products orchestrate | Remove the restaurant-order context (deliver arbitrary packages) → last-mile/on-demand delivery platform |
| Courier Management Platform | adjacent | The courier company's own business system (fleet, jobs, settlements) vs the merchant side. Deliverect's My Couriers is merchant-side fleet management — overlaps in objects, differs in frame | Change the operator from the merchant to the courier business → courier management |
| Delivery Scheduling Platform | adjacent | Pre-booked delivery slots/routes as the center vs on-demand fulfillment of incoming orders; advance orders are a setting here, not the core | Make pre-booked scheduling the center → delivery scheduling |
| Proof of Delivery Platform | capability vs Type | POD is one verification layer inside RDM (Uber Direct verification requirements; Deliverect geofencing) | Keep only the verification loop → POD platform |
| Restaurant POS / Restaurant Management System | container / sibling | POS is the restaurant's transaction system of record (incl. in-store orders); RDM manages the delivery fulfillment channel. Toast ships both as separate product lines; Olo integrates to POS via partners | Remove the delivery-fulfillment focus and generalize to all restaurant transactions → POS |
| Dispatch Management (generic, transportation domain) | generic sibling | Industry-generic dispatch of vehicles/jobs vs food-specific delivery orders bound to restaurant order flow | Remove food/restaurant semantics → generic dispatch management |

Taxonomy note: the leaf holds as an independent Type. No alias/variant collapse recommended. The strongest seam is with Food Delivery Marketplace and with On-demand Delivery Platform; both are documented above with product-side evidence.

## Uncertainties

- DoorDash Drive's own developer documentation was unreachable (403); its behavior is evidenced only through partner-side documentation (Deliverect, Toast). Confidence in the white-label-network pole rests on Uber Direct.
- Geographic delivery-zone configuration (polygons/radiuses) was not observed as a first-class object in any fetched source; availability emerges from provider coverage, quote-rejection rules (Olo), per-location partner activation (Deliverect), and geocoding (Uber Direct). Zone-based configuration likely exists in some products but is unverified — not asserted in the final document.
- Cash on delivery: observed only at the own-fleet pole (Deliverect setting). Prevalence across the Type unknown.
- Driver compensation beyond tips (payroll, per-delivery payouts for own fleets) was not researched.
- Toast's operational help-center detail (workflow-level) was not fetched; Toast claims are held at scope/positioning strength.
- Marketplace "own-delivery" agreement mechanics (who pays whom) observed only at Deliverect's FAQ level.

## Final Synthesis

A Restaurant Delivery Management application is the restaurant-side system of record for delivery as an order fulfillment channel. Its defining core is three jointly-held structures: (1) the delivery order — a restaurant order bound to a customer address and to the restaurant's order flow; (2) courier assignment — binding each delivery order to a fulfillment resource (own driver or external delivery service) by rule or by hand; (3) delivery progression tracking — the delivery advances through a lifecycle to a closed outcome (delivered, canceled, or undelivered-with-action), visible to the restaurant and commonly to the customer.

Around that core, mature products add: delivery availability and eligibility configuration, fulfillment-resource configuration and selection rules, fee/tip economics, customer tracking, courier apps, exception machinery (cancellations, undeliverables, refunds, re-dispatch, fallback), verification options, scheduled orders, store-system handoff, and analytics. Product form factors span operator dashboards (Olo, Deliverect, Toast), store-side tablet apps (Deliverect DMA), courier apps (Deliverect Couriers App, Uber courier app), and pure APIs (Uber Direct). The Type is bounded against the consumer-side marketplace (different perspective and business model), against online ordering (capture vs fulfillment), and against generic last-mile platforms (restaurant orders vs arbitrary parcels).
