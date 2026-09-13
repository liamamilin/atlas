# Research Notes — Restaurant Online Ordering

## Research Goal

Understand what a Restaurant Online Ordering application actually is, from real products: what objects exist inside it, who acts on them, how an order flows from a customer's device into the restaurant's operation, what the operator configures and controls, and where the boundary lies against neighboring Types (Food Delivery Marketplace, Restaurant POS, Self-service Restaurant Ordering, Restaurant Menu Management, Restaurant Delivery Management, generic e-commerce).

## Initial Boundary

Working hypothesis at start:

- The Type is the restaurant's **own first-party ordering channel**: customer-facing surfaces (web, app, QR) where customers compose orders from the restaurant's menu, check out, and the order flows into the restaurant's fulfillment.
- Most likely confused with: Food Delivery Marketplace (third-party multi-seller), Restaurant POS (staff-mediated in-store), Self-service Restaurant Ordering (kiosk), Restaurant Menu Management (the catalog behind it), Restaurant Delivery Management (fulfillment side).
- Prior sibling passes already fixed several seams:
  - **food-delivery-marketplace** (2026-09-08): "order of record + off-premises fulfillment coordination without multi-seller aggregation = Restaurant Online Ordering" — the marketplace pass explicitly assigned the single-seller pole to this leaf.
  - **restaurant-menu-management** (2026-09-09): "Online Ordering captures the customer's order and checkout on guest surfaces. Menu management maintains the catalog those surfaces sell."
  - **kitchen-display-system-kds** (2026-09-08): online ordering named as one of the order-capture sources feeding KDS tickets.
  - **restaurant-delivery-management** (2026-09-09): restaurant-side fulfillment for delivery orders — the execution side of what online ordering captures.

## Research Questions

1. What objects exist? (menu/catalog, cart, order, fulfillment terms, customer, payment)
2. What does the customer flow look like, end to end?
3. What fulfillment terms does an order carry (handoff modes, timing)?
4. How does the order reach the restaurant, and what happens on receipt?
5. What does the operator configure and control (hours, availability, delivery terms, capacity)?
6. Is online payment definitional or common?
7. Where exactly are the boundaries: marketplace vs first-party; kiosk vs remote; POS vs customer-side; menu catalog vs ordering surface?

## Representative Products

Selected for market representation + documentation quality + different product philosophy + different customer tier:

| Product | Form | Tier / philosophy |
|---|---|---|
| Toast Online Ordering | POS-suite-embedded ordering channel | SMB/mid-market; ordering as part of the POS platform |
| Square (Online Ordering Profile) | POS-suite-embedded ordering channel | SMB; free branded ordering profile on the POS catalog |
| ChowNow Direct Online Ordering | standalone first-party ordering | independents; commission-free, flat-subscription philosophy |
| GloriaFood | standalone free ordering system | micro businesses; free core, premium add-ons |
| Olo Ordering | enterprise ordering platform | enterprise chains; API-first, white-label, scale machinery |

## Sources

Evidence layers: **A** = directly observed on an official source for that product; **B** = cross-product commonality; **C** = canonical inference.

Fetched 2026-09-09:

- Toast platform guide (doc.toasttab.com): Orders Hub overview, Toast Online Ordering overview, Online ordering hours overview, Dining options for Toast online orders. (support.toasttab.com articles not fetched; platform guide used instead.)
- Square Support Center: Set up and manage your online ordering profile (8566), Set up delivery options for your online ordering profile (8609), Online topic index.
- ChowNow: get.chownow.com root + Direct Online Ordering product page. (www.chownow.com and help center not reachable/attempted after root 403; product-page strength only.)
- GloriaFood: root, /online-ordering (how it works), /restaurant-order-taking-app, /online-food-ordering-system-for-restaurants.
- Olo: olo.com root + /ordering product page; Olo Help Center (Zendesk): Ordering Platform Overview, How to Enable Dine-In, section indexes (Ordering, Handoff Modes, Store Settings, Menu).

## Product Observations

### Toast (evidence layer A)

- "Toast Online Ordering makes it easy to accept, process, and deliver online orders. Guests place online orders on your restaurant's Toast Online Ordering website or on the Local by Toast app." Settings live in Toast Web under Takeout & delivery > Availability > Online ordering; gated by the Restaurant Operations Setup permission.
- **Orders Hub** (POS screen): "displays all off-premise orders. An order is considered off-premise if the dining behavior is: Takeout, Delivery, or Curbside." Quote times displayed at the top "affect orders placed using the Toast Online Ordering website, the Local by Toast app, or the Toast POS app. The quote time does not apply to online ordering channel orders (for example, DoorDash, Uber Eats, or Grubhub)."
- **Manage Online Orders** dialog (permission-gated): "Turn on, snooze, or turn off online ordering availability; Adjust takeout and delivery delays; Turn on, off, or pause third-party online ordering channels." Changes sync with the Toast Web online ordering dashboard.
- **New Order button** opens Quick Order: staff manually enter an off-premise order (phone orders) — a POS function, distinct from the customer-side channel.
- **Online ordering hours**: "determine the hours during a business day when guests can place online orders for immediate or future fulfillment… displayed on your restaurant's Toast Online Ordering website and the Local by Toast app. Online ordering hours do not restrict when you can place orders on Toast POS devices or when guests can order and pay at the table using their own mobile device." (Explicit three-way separation: online ordering channel vs POS vs customer-device table ordering.)
- Scheduled-orders settings, minimum lead times, first/last online ordering time slots are separate configuration pages.
- **Dining options for online orders**: configured dining options (delivery, takeout, curbside) are displayed on the ordering website; "If you configure only one dining option, that option will be set as default for all Toast online orders. If you configure more than one, guests choose an option while placing their order." Dining options map to the restaurant's dining-option behaviors.
- **Firing**: online orders fire to the kitchen (autofire devices; offline support pages cover firing and payment when offline).
- **First-party delivery**: delivery area configuration, delivery minimum, delivery service charge, Toast Delivery Services notifications/statuses.
- Third-party channels are managed as a separate section (on/off/pause per channel; menu visibility per channel).

### Square (evidence layer A)

- "Online ordering profiles offer a branded online presence for food and beverage businesses at no extra cost (processing fees apply), functioning with the ease of a mobile app without the commissions or fees typically associated with marketplace platforms. **Online ordering profiles use your menus and menu items to build an online catalog that customers can browse and purchase from.**"
- Prerequisite: "Before you create your online ordering profile, you need to create a menu."
- Profile settings (one Dashboard page): branding (logo, color), basic info (profile name, Cashtag), about, **pickup and delivery options**, checkout options (tipping, customer notes, enhanced payment verification), taxes, service charges, **store policies** ("cancellations, refunds, prep time, and quality issues… shown when your customers place orders"), item fulfillment methods.
- Menu hours: "Make your menus available during certain times of the day (think breakfast, lunch, dinner, etc.) to accommodate your menu hours."
- Sharing: "Promote your profile by sharing your link or QR code on various platforms such as Google, social media, or even your countertop." Order with Google integration sends the profile URL and menus with item pricing to Google.
- Payment: "Enable customers to place instant, secure orders using Cash App, credit, or debit"; discounts, promo codes, gift cards redeemable at checkout.
- **Item fulfillment methods**: "By default, items use your location's fulfillment methods (pickup, local delivery, self-serve ordering, shipping). You can verify or change this setting from the item editor… To override fulfillment for a specific item, turn off Use location default." (Per-item fulfillment eligibility with location default.)
- **Delivery options** (article 8609): in-house delivery (own couriers) or on-demand delivery (Square delivery partners); settings include prep time, lead time, delivery time, delivery courier (DoorDash or "Best Available" via Nash), ordering hours (can differ from location hours), service fee, **minimum order amount**, scheduled downtime, order timing (cut-off time; orders after cut-off scheduled for next day), **large order limit** (item or price cap), ticket printing (print based on pickup/delivery time or when placed), delivery area (postal code or radius) with per-area delivery fee, fee modes (free / flat / free-over-minimum / distance-based / fallback), no-contact delivery.
- Pause: toggle Ordering on/off from Dashboard, or from the Square POS app Orders tab.

### ChowNow (evidence layer A for product pages; mechanics at product-page strength)

- "Direct Online Ordering gives you a commission-free channel on your own website and app." "An embedded ordering widget lets diners browse and check out without leaving your site."
- Business model: "You pay a flat monthly subscription and a standard card processing fee — no per-order cut to a marketplace."
- Operations: "Orders sync to your POS and flow straight to the kitchen and printers — no errors, no double entry." "Update your menu anytime through the ChowNow Dashboard. Add, edit, or 86 items in just a few clicks." Refunds controllable "through the tablet… full or partial refunds without having to call support."
- Catering: "scheduling and lead time tools help our kitchens plan ahead and prep properly across locations."
- Data: "Restaurants get full access to diner ordering data and contact information… You own 100% of diner contact and ordering data."
- Product family around the ordering core: Branded Mobile Apps, Website Builder, Marketplace (own consumer app), Discovery Network (Google etc.), QR Code Ordering (dine-in), Catering, Flex Delivery, Order Aggregation ("pulls every channel into a single dashboard"), Email & SMS Marketing, Rewards.
- POS integrations: Toast, Square, Revel, Clover, 20+.

### GloriaFood (evidence layer A)

- Setup sequence (official how-it-works page): 1) restaurant profile (name, contact info, preferred payment types, opening hours); 2) online menu builder ("Add categories, menu items, allergen-free icons and modifiers"); 3) download the free order-taking app ("Get notified instantly whenever an order is placed. Alerts get sent to your mobile device… as soon as your customers place an order"); 4) add the "See MENU & Order" button to the website (copy-paste code snippet).
- FAQ definition: "An online ordering system enables food businesses such as table service restaurants, coffee shops, or food trucks to accept orders online for pickup, delivery, and dine-in."
- Order-taking app: "The device will notify you every time you get a new order, and your customers will know exactly when you've accepted it." (Manual acceptance with customer-visible acceptance state.) "Mark menu items & add-ons as out-of-stock… preventing customers from ordering something that's no longer available." "Pause a selected service or all of them… adding a timeframe and a personalized message." "Automatically print accepted orders directly from the mobile order taking app… connecting the order taking app with a thermal printer."
- Surfaces: website widget, Facebook smart-link, QR code ordering (including "on premise ordering… individual QR codes for your tables"), branded app (premium), hotel room-service ordering.
- Scheduled orders ("Order for later") and table reservations (with deposits) ride the same platform.
- Online payments and digital tipping are **premium** features — the free core is order capture without online payment.
- Multi-location dashboard for chains; delivery-zone heatmaps; promotions module; analytics.

### Olo (evidence layer A)

- Platform overview (help center): "Our Ordering platform provides a foundation for restaurant brands to handle all their digital ordering needs. We integrate with popular POS systems, offer a fully branded white-label website/app experience, and API access for a full, end-to-end eCommerce experience. Once live, you can manage your menus, track sales, run reports, and set up permissions all through the Dashboard."
- Product page: "Make it easy for guests to order directly—from your website, app, or kiosk." Benefits list: free custom-branded storefront, passwordless sign-in + checkout, "Support for pickup, delivery, curbside, and other handoff modes", API + webhook library, coupon manager, AI/ML cross-selling, **order throttling**, **customizable capacity rules engine**, centralized menu management for all digital channels, support for virtual brands, predictive quoting and capacity management.
- **Dine-In handoff mode** (help article): "enables brands to allow a Dine-In handoff mode… a dedicated handoff mode that identifies orders meant for in-store consumption." Functionality: configurable by menu item; loyalty earning/redemption; custom fields triggered by the mode (e.g., table number); cash/credit/gift card payment; web (Serve), mobile app, API, Switchboard support. Time modes: "Immediate (ASAP), Scheduled, Manual Fire." Setup: enable at channel and vendor level; set Dine-In handoff-mode hours per store; configure per-product eligible handoff modes; optional custom fields; thank-you messaging per brand/vendor. POS support matrix (Aloha, Brink, MICROS, OloCloud, POSitouch, Revel, Simphony, Toast, Xpient).
- Help-center structure confirms the operator model: Dashboard (Store Settings, Handoff Modes), Brand (User Management, Coupons), Menu (Company Menu Admin, Store Menu Admin, Menu Design), Ordering (Catering+, Ordering Overview, Chargebacks, Kiosks, Order Throttling Strategies), Expo (kitchen-facing screen), Dispatch (direct delivery), Rails (marketplace delivery), Switchboard (digitized phone orders).

## Cross-product Comparison

| Dimension | Toast | Square | ChowNow | GloriaFood | Olo |
|---|---|---|---|---|---|
| Customer surface | branded ordering website + consumer app | branded ordering profile (link/QR) | embedded widget on restaurant's site + branded app | website widget, social smart-link, QR, premium app | white-label web/app (Serve) or API-built front-end |
| Menu source | the POS's menu catalog | the POS's menus ("use your menus… to build an online catalog") | ChowNow Dashboard menu, synced to POS | GloriaFood menu builder | Olo Menu Admin (company/store, POS-mapped) |
| Fulfillment terms on the order | dining options: takeout / delivery / curbside | pickup / local delivery / self-serve / shipping (per item, location default) | pickup/delivery; catering lead times; QR dine-in | pickup / delivery / dine-in | handoff modes incl. pickup, delivery, curbside, dine-in, "other" |
| Timing | immediate or future fulfillment; scheduled-order settings; minimum lead times; first/last slots | ASAP; order scheduling (days ahead); cut-off time | ASAP; catering lead times | ASAP; "order for later" | time modes: ASAP / Scheduled / Manual Fire |
| Ordering hours | dedicated online ordering hours, separate from POS hours | per-fulfillment-method hours, can differ from location hours | availability + pause | opening hours + pause with message | store hours per handoff mode |
| Capacity / throttling | quote times, takeout/delivery delays, snooze | prep/lead time, orders per 15-min window, large-order limits | — | pause services | order throttling, capacity rules engine, predictive quoting |
| Delivery configuration | delivery area, minimum, service charge, TDS | area (postal/radius), fee modes, minimum, courier choice | Flex Delivery module | delivery zones | Dispatch (direct) / Rails (marketplace) |
| Order receipt | Orders Hub on POS; autofire to kitchen | Dashboard/POS; ticket printing | POS sync → kitchen/printers | order-taking app accept → thermal print | Dashboard + Expo; POS integration |
| Acceptance | auto (autofire) or staff | auto | auto via POS sync | **manual accept**, customer notified | auto or manual; cancel from Dashboard |
| Online payment | yes (Toast payments) | yes (Cash App/card) | yes (processing fee) | **premium add-on** — free core is order-only | yes (Olo Pay) |
| Operator config surface | Toast Web | Square Dashboard | ChowNow Dashboard | GloriaFood dashboard + app | Olo Dashboard |
| Business model | POS suite module | POS suite module (free profile) | flat subscription, commission-free | free + premium | enterprise SaaS |

### What is universal (B-layer, all 5 sampled)

1. The restaurant's **own menu** is rendered as a customer-facing orderable catalog under the restaurant's identity (Square's wording is explicit; all others structurally identical).
2. The **customer** composes and submits the order themselves through that surface (item selection, customization/modifiers, cart, checkout/contact details).
3. The submitted order is **recorded and transmitted into the restaurant's operation** as a fulfillment instruction, carrying **fulfillment terms** (handoff mode + timing) — via POS integration, kitchen firing, order-taking app, or printer.
4. The operator controls **availability**: ordering hours and/or pause/snooze switches, and item availability (86) propagates to the ordering surface.
5. The operator configures **fulfillment terms**: which handoff modes are offered, and (where delivery) areas/fees/minimums.

### What is common but not definitional

- Online payment at checkout (5/5 sampled support some form, but GloriaFood's free core is order-only with payment optional; pay-at-pickup/cash flows exist; historical ordering predates online payment).
- Customer accounts, loyalty/rewards, promotions/coupons, tipping.
- Scheduled/order-ahead (future fulfillment) — common but ASAP-only systems are still this Type.
- Order-status communication to the customer (confirmation, ready/delivered states).
- Third-party marketplace integration / order aggregation (ChowNow Order Aggregation, Toast third-party channels, Olo Rails) — an add-on around the first-party core.
- Marketing machinery (email/SMS, campaigns, data ownership claims).
- Multi-location / brand-level management (Olo company menu admin, GloriaFood multi-location dashboard, Square/Toast location settings).
- Capacity machinery at scale (throttling, capacity rules, predictive quoting — Olo; quote times/delays — Toast).

### Vendor-specific (L3 — stays here)

- Square "Cashtag" identity and Cash App one-tap checkout; "Neighborhoods" rewards program; "self-serve ordering" as a named fulfillment method (kiosk/QR semantics not further documented in fetched pages — not asserted).
- Toast "Local by Toast" consumer app; Toast Delivery Services (TDS); Autofire devices; quote-time strategy engine; permission codes (1.5, 3.29, 1.2).
- ChowNow Profit Protector; Discovery Network; Flex Delivery; 100% chargeback/fraud protection framing.
- GloriaFood end-of-life notice (April 30, 2027, Oracle) — market fact, not Type-relevant.
- Olo Serve (white-label front-end), Switchboard (digitized phone orders), Olo Network (second-party app), Guest Data Platform, Expo screen.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The restaurant's menu as a customer-facing orderable catalog under the restaurant's identity.** The restaurant's own offerings — items with prices and customization options — presented on an ordering surface the customer can browse and compose from. Remove → a digital menu / brochure site (menu-management or website territory).
2. **Customer-side self-service order composition and submission.** The customer — not staff — selects, customizes, and submits the order through that surface, away from the counter. Remove → phone/fax ordering or staff POS entry (Restaurant POS territory).
3. **The submitted order as the restaurant's fulfillment instruction.** The order is recorded — the ordering channel is the order of record — and transmitted into the restaurant's operation (POS, kitchen, order-taking app, printer) carrying its fulfillment terms (handoff mode: pickup/delivery/curbside/dine-in; timing: ASAP or scheduled). Remove → a cart/checkout that never reaches the restaurant (generic e-commerce), or a menu with no order.

Jointly-held load-bearing tests:

- 1 alone = digital menu / QR menu (menu-management territory)
- 2 without 1 = generic form/checkout intake (e-commerce territory)
- 3 without 1+2 = staff-entered phone orders (POS territory — Toast's own New Order/Quick Order function)
- 1+2 without 3 = browsable menu with a cart that never produces a restaurant order
- 2+3 without 1 = ordering without restaurant menu semantics (generic goods checkout)
- 1+3 without 2 = staff-mediated remote ordering (phone/POS), not customer self-service

### L1 — Common Mature Structure

- online payment at checkout (with tipping, taxes, service charges)
- customer contact capture / optional accounts, order history, reorder
- promotions (discounts, promo codes), gift cards, loyalty
- scheduled/future orders with lead times and time slots
- order confirmation and status communication to the customer
- item availability (86) propagation and sold-out handling
- per-item fulfillment eligibility
- delivery configuration (areas, fees, minimums) inside the ordering settings
- sharing/discovery plumbing (links, QR codes, Order-with-Google class integrations)

### L2 — Variant / Optional Structure

- dine-in handoff (Olo dine-in mode; GloriaFood dine-in; QR table ordering riding the same machinery) vs off-premises-only
- delivery fulfillment machinery depth: none (customer-arranged) → own couriers → on-demand partner dispatch (straddles toward Restaurant Delivery Management / on-demand delivery)
- third-party marketplace aggregation (straddles toward Food Delivery Marketplace machinery)
- catering as a distinct order class (lead times, large-order controls)
- multi-location / brand governance, virtual brands
- capacity/throttling machinery (enterprise scale)
- white-label vs hosted-profile front-end; API-first headless ordering
- business model: free, flat subscription, POS-bundled, enterprise SaaS

### L3 — Vendor-specific

See Vendor-specific list above; none of it enters the canonical document.

## Historical / Market-Sample Check

- **Pre-smartphone / early-web era**: a restaurant website with a menu and an order form, order submitted and phoned/faxed/emailed to the kitchen, payment at pickup or on delivery — satisfies all three L0 structures (menu as orderable catalog; customer-side composition; order transmitted with fulfillment terms). No online payment, no app, no live tracking required. ✓
- **Phone ordering entered by staff into the POS** fails structure 2 (staff-mediated) — Toast's own documentation treats staff-entered off-premise orders as a POS function (Quick Order), separate from the online ordering channel. ✓ (boundary holds)
- **Fax-era multi-restaurant order services** fail the single-seller identity of structure 1 — they are the marketplace ancestor (Food Delivery Marketplace territory). ✓
- **QR table ordering** (customer's own device, on-premises) rides online-ordering machinery in sampled products (GloriaFood on-premise QR, ChowNow QR ordering) — treated as a variant surface of this Type, while venue-installed kiosks remain the neighboring Self-service Restaurant Ordering Type. Toast's docs explicitly separate "guests order and pay at the table using their own mobile device" from the online ordering channel's hours — evidence that vendors themselves see these as adjacent-but-distinct surfaces sharing machinery.
- Conclusion: the definition is not over-fitted to the modern app/payment era.

## Boundary Findings

1. **vs Food Delivery Marketplace** — the sharpest seam. Marketplace = many independent sellers aggregated on one consumer surface operated by an entity that is not the food seller; Online Ordering = one restaurant's own channel under the restaurant's identity. The food-delivery-marketplace pass pre-ratified this ("2+3 without 1 = Restaurant Online Ordering"). Straddle products: ChowNow Marketplace and Olo Rails (ordering vendors operating marketplace surfaces) — the marketplace surface is a different Type riding the same order machinery. Removal test: remove multi-seller aggregation → marketplace collapses into this Type; add it → this Type's surface becomes a marketplace.
2. **vs Restaurant POS** — POS is the staff-mediated in-store transaction surface (order entry, checks, payment); Online Ordering is the customer-mediated remote capture channel. Toast's docs draw the seam operationally: online ordering hours "do not restrict when you can place orders on Toast POS devices"; the Orders Hub (a POS screen) *receives* online orders; staff-entered off-premise orders are a POS function. In POS-embedded products the two share the menu catalog and the order stream, but the composing actor and the surface differ. Removal test: remove customer self-service composition → what remains is a POS.
3. **vs Self-service Restaurant Ordering (kiosk)** — both are customer self-service order capture. Seam: device and location (customer's own device, typically remote, order-ahead semantics vs venue-installed kiosk on-premises with immediate handoff). The QR-table case (customer's own device, on-premises) is the blur zone — sampled products ship it as part of online ordering. Flag for the kiosk pass; no directory change proposed.
4. **vs Restaurant Menu Management** — menu management maintains the catalog of record; online ordering consumes it as an orderable customer surface and adds the order transaction. Ratified from the menu-management side ("consumer of the menu"). Removal test: remove the order transaction → menu management stands; remove the catalog → online ordering has nothing to sell.
5. **vs Restaurant Delivery Management** — online ordering captures the order and its delivery terms; delivery management executes fulfillment (courier assignment, progression tracking). Square bundles delivery configuration into the ordering profile (straddle), but execution machinery (dispatch, driver management, live tracking) is the sibling Type's center. Removal test: remove courier assignment/tracking → online ordering stands; remove order capture → delivery management still fulfills orders from other channels.
6. **vs E-commerce Platform / Online Store Builder / Checkout Platform** — generic goods commerce lacks restaurant service semantics: menu items with modifier groups and selection constraints, dining/handoff options, prep/quote times, ordering hours, kitchen routing, 86 availability. Checkout is one stage inside the ordering flow, not the whole. Removal test: swap the menu semantics for a generic product catalog → the product becomes an online store builder, not a restaurant ordering system.
7. **vs Restaurant Reservation Platform** — reservations commit a table/seat at a time; ordering composes food for fulfillment. GloriaFood bundles both (reservation deposits + food pre-orders) — adjacent bundling, different objects.

## Uncertainties

- ChowNow evidence rests on official product pages; its help center was not fetched (root domain 403; product site used instead). ChowNow-internal mechanics (order lifecycle states, acceptance modes) are stated at product-page strength only.
- Toast's support.toasttab.com "Getting Started with Online Ordering" article was not fetched; the platform guide (doc.toasttab.com) was used and is sufficient for the claims made.
- Square's "self-serve ordering" fulfillment method: semantics (kiosk vs QR vs counter) not documented in fetched pages — deliberately not asserted.
- Exact fee structures, quote-time algorithms, throttling parameters: not asserted anywhere (precision not supported by fetched evidence).
- Whether dine-in handoff is common across the Type or an Olo/GloriaFood-led pattern: only 2 of 5 sampled products document dine-in explicitly (Toast's online dining options are takeout/delivery/curbside); dine-in is therefore held as a variant, not standard.

## Final Synthesis

A Restaurant Online Ordering application is the restaurant's own customer-side ordering channel. Its defining core is three jointly-held structures: the restaurant's menu rendered as a customer-facing orderable catalog under the restaurant's identity; customer-side self-service composition and submission of the order; and the submitted order recorded and handed to the restaurant's operation as a fulfillment instruction carrying its terms (handoff mode and timing). Everything else — online payment, accounts and loyalty, scheduled orders, delivery configuration depth, marketplace aggregation, marketing, multi-location governance, capacity machinery — is common mature structure or variant capability, not definition. The Type sits between the menu catalog behind it (Restaurant Menu Management), the staff-mediated transaction surface beside it (Restaurant POS), the venue-installed self-service surface (Self-service Restaurant Ordering), the fulfillment machinery after it (Restaurant Delivery Management), and the multi-seller aggregation it deliberately is not (Food Delivery Marketplace).
