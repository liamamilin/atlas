# Research Notes — Kitchen Display System / KDS

Research date: 2026-09-08
Slug: kitchen-display-system-kds
Directory leaf: Kitchen Display System / KDS (§26 Travel, Hospitality, Food Service & Events)

## Research Goal

Understand what a Kitchen Display System (KDS) actually is as an Application Type: what objects exist inside it, who uses it, how the fulfillment loop works, which structures are definitional vs merely common in today's market, and where its boundaries sit against Restaurant POS, kitchen printers, delivery management, and commercial kitchen management software.

## Initial Boundary (pre-research hypothesis)

- A KDS is the back-of-house fulfillment display: it receives orders from order-capture systems (POS, online ordering, delivery platforms) and presents them as tickets to kitchen staff, who work them and mark them complete ("bump").
- Nearest neighbors: Restaurant POS (order capture + payment), Restaurant Online Ordering / Food Delivery Marketplace (order sources), Restaurant Delivery Management (courier side), Commercial Kitchen Management (production planning: recipes, prep lists, food safety), Institutional Foodservice Management (meal programs).
- Suspected over-fitting risks: color-coded timers, station routing, all-day counts, and analytics are ubiquitous in modern products but may not be definitional (paper-ticket rails predate all of them).

## Research Questions

1. What exactly does a KDS display? What is on a ticket?
2. Where do tickets come from, and how do they arrive (integration postures)?
3. What is the ticket lifecycle — states, completion, undo/recall?
4. How does station routing work (screens per station, item routing, prep vs expo roles)?
5. What timing/urgency machinery exists (timers, color transitions, alerts)?
6. What queue-management behaviors exist (sort, prioritize, hold, all-day counts)?
7. What configuration exists (layouts, fonts, modifier highlighting, order types)?
8. What analytics/reports does a KDS produce?
9. What hardware surrounds it (bump bars, kitchen-grade screens, printers)?
10. Where are the boundaries: vs POS, vs kitchen printer, vs delivery management, vs commercial kitchen management?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Square KDS | POS-embedded KDS, SMB | Tier-1 help center reachable; Android-app KDS sold as an add-on to Square for Restaurants |
| Fresh KDS | Standalone POS-agnostic KDS | Independent KDS vendor; Tier-1 glossary + training guide reachable; integrates with 30+ POS systems |
| Crunchtime Kitchen (formerly QSR Automations ConnectSmart Kitchen) | Enterprise dedicated KDS | 30+ year dedicated-KDS heritage, casual-dining chains; Tier-2 product page + vendor KDS guide reachable; also the "Kitchen Management" naming-collision case |

Rejected/abandoned samples:
- **Toast KDS** — www.toasttab.com returned 403 on two different paths (WAF); abandoned per network rule. Toast is the largest US restaurant-platform pole; its absence is recorded as a sourcing limitation. No Toast-specific claims are made anywhere in this pass.
- **Lightspeed KDS** — lightspeedhq.com/kds 403; abandoned.
- **TouchBistro KDS** — touchbistro.com/kds 403; abandoned.
- **QSR Automations** — qsrautomations.com now serves Crunchtime content ("ConnectSmart® Kitchen is now Crunchtime Kitchen"); treated as the same product as Crunchtime Kitchen, not a separate sample.

## Sources

Tier 1 (official operational documentation):
- Square Support Center — "Set up Square KDS" (article 7924/7944): https://squareup.com/help/us/en/article/7924-beta-kds-android — fetched 2026-09-08
- Square Support Center — "Complete and recall orders with Square KDS" (8171): https://squareup.com/help/us/en/article/8171-complete-orders-with-square-kds — fetched 2026-09-08
- Square Support Center — "Route orders to the kitchen with Square KDS" (7959): https://squareup.com/help/us/en/article/7959-route-orders-with-your-kds — fetched 2026-09-08
- Fresh KDS Help Center — "The Fresh KDS Glossary": https://help.freshkds.com/en/articles/6657677-the-fresh-kds-glossary — fetched 2026-09-08
- Fresh KDS Help Center — "Fresh KDS Training Guide": https://help.freshkds.com/en/articles/6546044-fresh-kds-training-guide — fetched 2026-09-08
- Fresh KDS Help Center — Getting Started collection index: https://help.freshkds.com/en/collections/1402725-getting-started — fetched 2026-09-08

Tier 2 (official product pages):
- Square KDS product page: https://squareup.com/us/en/kitchen-display-system — fetched 2026-09-08
- Crunchtime Kitchen product page ("KITCHEN DISPLAY SYSTEM"): https://www.crunchtime.com/kitchen — fetched 2026-09-08
- Crunchtime homepage (suite nav; "Kitchen Management — Kitchen Display System (KDS) software"): https://www.crunchtime.com/ — fetched 2026-09-08
- Fresh KDS homepage: https://www.freshkds.com/ — fetched 2026-09-08

Tier 2/3 (official vendor educational content):
- Crunchtime blog — "What Is a KDS? An Easy Guide to Kitchen Display Systems": https://www.crunchtime.com/blog/what-is-a-kds-a-guide-to-kitchen-display-systems — fetched 2026-09-08

Unreachable (recorded limitations):
- toasttab.com — 403 ×2 (www paths) — Toast pole unverified
- lightspeedhq.com/kds — 403
- touchbistro.com/kds — 403
- Fresh KDS individual "How do I clear orders" article not fetched (training guide covers the same interactions)

## Product Observations

### Square KDS (evidence layer: A — Tier-1 help center + Tier-2 product page)

- Definition (vendor's own): "Square KDS is a Kitchen Display System application that is Android-operated and allows you to view, track, and fulfill orders via digital tickets in your back of house, replacing traditional paper tickets and kitchen printers." (product page FAQ)
- Order sources: "connects with Square Point of Sale, Square Online, Square for Restaurants, Square for Retail, and third-party ordering and delivery platforms." Product page: "Whether you take orders through POS, your online ordering page, or delivery apps like Postmates, everything is sent to and fulfilled directly from the kitchen."
- Routing: per-device routing configuration — a KDS device can be set to "View point of sale orders" from selected POS devices, and/or "View online, kiosk and delayed fulfillment orders"; also "Filter orders by category". (help 7959 + related 8170)
- Device roles: two KDS device types — **Prep** ("kitchen staff who focus on preparing a certain piece of each order... granular view of only the items they need to make") and **Expeditor/Expo** ("bridge front-of-house and back-of-house... finalize orders... high-level visibility and control over prep stations"). (help 7924)
- Completion semantics: complete a single item (tap the item) or the whole ticket (tap the ticket header); configurable propagation — "Complete for all devices" vs "Complete only on this device"; Expo devices show a green checkmark for items completed by Prep stations; recall (undo) a completed ticket from the Completed tab; 3-second undo window for accidental taps. (help 8171)
- Timers & alerts: configurable **Yellow timer** and **Red timer** (minutes), optional sound "when new tickets arrive", custom alert sound/volume "helpful in loud kitchen environments". (help 7924)
- Modifier handling: per-modifier-option KDS text colors and a separate "Kitchen name" ("customize how this modifier appears on KDS and kitchen printers"). (help 7924)
- Ticket content configuration: item sort order on tickets (default/alphabetical/category), modifier-set order for kitchen tickets. (help 7924)
- Staggered item prep times: "items within a ticket will appear on the KDS at staggered times based on their individual prep times, so kitchen staff can start each item at the right moment" (requires item prep times in catalog). (help 7924)
- All Day counts: "show how many of each item you need across all open orders on your KDS"; optional separate **fired** (actively being prepared) vs **held** (waiting to be fired, incl. held courses and fully-held upcoming tickets) counts. (help 7924)
- Layout: ticket layout, number of columns, text size configurable per device. (help 7924)
- Third-party status linkage: "Automatic Order Update" — order statuses update to **Ready** on third-party platforms when the ticket is completed on at least one Expo device; "Send order-ready texts" exists as a related feature. (help 8171 + related articles)
- Reports: "reports that give you insights on prep times and more" (product page).
- Hardware: kitchen-grade Android devices (MicroTouch 10.1"/15.6"/21.5", VESA mount); previously iPad-based (migration documented). Requires Square Plus/Premium subscription + per-device monthly fee. (help 7924, product page)
- Testimonial evidence of value: "two-way ticket interaction that paper receipts can't offer" (marking items complete). (product page)

### Fresh KDS (evidence layer: A — Tier-1 glossary/training guide; Tier-2 homepage)

- Definition (vendor's own): "Fresh KDS is a kitchen display system that runs as an app on iPads and Android tablets. Fresh KDS connects to your point of sale, and every order appears on screen the moment it is rung in, with items, modifiers, notes, and a timer already on the ticket. Your team taps items off as they finish them, then clears the ticket when the order is ready." (homepage FAQ)
- Glossary definitions (Tier-1, quoted):
  - **Bump**: "Once an order is complete, it can be bumped, or cleared, from the KDS screen."
  - **Bump Bar**: "a small device (similar to a keyboard) that can be used to select, move, or close orders on the KDS without physically touching the screen."
  - **Queue**: "the line or sequence in which orders appear on the KDS. By default, tickets will display in the order received, from oldest to newest; however, all tickets can be rearranged."
  - **Modifier**: "a line item that makes a minor change or addition to a menu item... you can choose to strike through individual modifiers or the whole item at once."
  - **Screen**: "tablets serve as 'screens' and can be placed at any workstation in your kitchen, such as a Hot Bar, Cold Bar, Takeout Station, etc."
  - **Transition Times**: "Color-coded ticket transitions... Set the time and color that a ticket will turn to indicate Caution or Late."
  - **Printer Emulation**: "Fresh KDS integrates with many systems if set up as a printer in your POS. In most cases, this is the default connection option."
  - **Cross Screen Communication**: "simultaneously clear orders on multiple KDS screens or forward orders from one screen to another; useful in assembly lines" (Premium).
  - **Take Out View**: dedicated to-go station screen showing "Customer Name, Pickup Time, Vehicle Description, Delivery Address" for third-party/takeout orders.
  - **Order Tracker**: customer-facing screen (Fire TV Stick) listing orders in two status columns, "Being Prepared" & "Ready".
  - **Bump Time Reports**: "kitchen's performance, average bump times, and other KDS fulfillment metrics."
  - **I'm Here Notifications**: customer SMS link triggers a notification on the KDS Take Out View.
  - Roles/permissions exist only on the web dashboard: "these permissions do not transfer when accessing the Fresh KDS app on tablet devices" — the line has no login.
- Core interactions (training guide): mark an item or modifier complete (tap line item); clear entire orders (tap ticket header); recall cleared orders (recall button); place orders on hold (action menu → hold).
- Connection postures: Printer Emulation (local network, POS treats KDS as a printer) or API cloud connection (Square Orders API, Zapier, KDS Cloud API, webhooks on order received/bumped).
- Display modes: Tiled / Classic / Split (Split organizes tickets by Order Type — "For Here tickets on the top; Pickup/Delivery tickets on the bottom"); font sizes; color options for order types and transitions.
- Homepage features: automatically sort orders (by prep and pickup time); quickly prioritize orders ("Move urgent or delayed orders forward"); print labels and tickets; multi-station screen communication; ingredient all-day counts ("See live item totals for all open orders"); modifier styles (colors, bold, italics); color-coded timers ("green to yellow to red as they get close to being late"); recall previously cleared tickets; route tickets by order type.
- Delivery orders: "For DoorDash, Uber Eats, and Grubhub orders, Fresh KDS can display the delivery service on the ticket."
- On The Fly (companion app): kitchen score, open tickets, lead ticket time, speed-of-service metrics, station/lead delays, compare locations/hours/channels.
- Enterprise: manage device settings and screen configurations across locations from one place; standardize workflows; compare locations.
- Hardware: iOS/Android tablets, kitchen-grade screens, USB bump bars, Bluetooth ticket/label printers (Bixolon, Zebra, Epson). Pricing per screen.
- Positioning: "built around one question: are your orders going out on time?... measuring each against its target rather than a kitchen average"; "kitchens replacing paper tickets".

### Crunchtime Kitchen / formerly QSR Automations ConnectSmart Kitchen (evidence layer: A for naming/self-description — Tier-2 product page; B for category framing — vendor guide)

- Naming collision (direct evidence): Crunchtime suite nav lists "**Kitchen Management** — Kitchen Display System (KDS) software that manages demand, directs order flow, and keeps every station in sync"; the product page headline is "KITCHEN DISPLAY SYSTEM"; "ConnectSmart® Kitchen is now Crunchtime Kitchen" (rebrand note). This discharges the flag hung by the commercial-kitchen-management pass (2026-09-07): Crunchtime's "Kitchen Management" product IS a KDS, distinct from the Commercial Kitchen Management Application Type (production planning).
- Category definition (vendor guide): "A kitchen display system is a digital order viewer that replaces your paper tickets and kitchen printers (and so much more). Beyond showing orders, a KDS manages how food is routed through the kitchen, supports recipe preparation, and monitors real-time kitchen data."
- POS-KDS seam (vendor-articulated): "some kitchen display systems serve as a proprietary appendage to a point-of-sale system... But remember, a POS and KDS aren't the same. A more advanced KDS would integrate with the kitchen to gather accurate data and provide up-to-the-minute order statuses."
- Enterprise capabilities: "dynamic load balancing and real-time routing... orders are automatically distributed based on station capacity"; "customizable routing, pacing, and prep stations"; "line routing and bin management to guide staff through orders step-by-step. By automating ticket sequencing, helping staff prep for rush periods, and course timing"; **bin management** ("product projection and forecasting tool... reminding team members what to cook, when to cook it, and how much of each item to prepare—all while tracking usage"); **order ready boards** (customer-facing; "show the customer name, transaction status, order number... send an SMS message to the guest when their food is ready"); meal coursing/pacing; delayed routing (cook-time-based: salmon 12-min vs steak 20-min example); capacity management.
- View types (vendor guide): order views (fixed/flex grid), item views, "AccuPrep" (plating times), order-ready views (customer-facing).
- Insights: "ticket times, station performance, and throughput metrics... across all locations"; "visibility into prep times, order statuses, and performance metrics across all locations."
- Integrations: "80+ point-of-sale systems... orders flow directly from the POS to the right station in the kitchen without manual intervention"; solution partners Olo, Flybuy, Smart Bar USA, Curbit.
- Heritage: "trusted by leading brands for over 30 years"; "Used in 21 of the top 25 nation's largest casual-dining chains"; hardware page exists (Kitchen Hardware).

## Cross-product Comparison

| Structure | Square KDS | Fresh KDS | Crunchtime Kitchen | Layer |
|---|---|---|---|---|
| Tickets received from order-capture systems (POS/online/delivery) | ✓ (POS, Square Online, third-party) | ✓ (30+ POS + Olo/Cuboh/Otter; DoorDash/UE/GH labels) | ✓ (80+ POS; Olo etc.) | A→B core |
| KDS captures no orders, takes no payment | ✓ (fulfillment only) | ✓ | ✓ | B core |
| Ticket shows items, modifiers, notes, order context | ✓ | ✓ ("items, modifiers, notes, and a timer") | ✓ | B core |
| Kitchen-facing screen(s) at workstations | ✓ (Prep/Expo devices) | ✓ (screens at Hot Bar/Cold Bar/Takeout) | ✓ (prep stations) | B core |
| Active ticket queue ordered by arrival | ✓ (routing/filtering) | ✓ (Queue: oldest→newest, rearrangeable) | ✓ (ticket sequencing) | B core |
| Item-level completion (strike/tap off) | ✓ (tap item) | ✓ (tap line item; modifier strike-through) | ✓ (line routing step-by-step) | B core |
| Whole-ticket completion = bump/clear | ✓ (tap header) | ✓ (tap header; "bumped, or cleared") | ✓ | B core |
| Recall/undo completed tickets | ✓ (Recall from Completed tab; 3-s undo) | ✓ (recall button) | (not directly evidenced) | B common |
| Completion state recorded / feeds reporting | ✓ (prep-time reports) | ✓ (Bump Time Reports) | ✓ (ticket times, station performance) | B common |
| Order-age timers with color transitions | ✓ (Yellow/Red timers) | ✓ (Caution/Late; green→yellow→red) | ✓ (cook times/pacing framing) | B common |
| Audio alert on new tickets | ✓ (toggle + custom sound) | ✓ (tone/volume/repeat) | (not directly evidenced) | B common |
| Station routing (multiple screens, item/category routing) | ✓ (per-device source/category filters; Prep/Expo) | ✓ (screens per station; cross-screen forward) | ✓ (line routing, station capacity) | B common |
| Prep vs Expo role split | ✓ (named device types) | ✓ (implicit; expo/takeout views) | ✓ (expo window framing) | B common |
| All-day counts (aggregate item totals across open tickets) | ✓ (fired vs held) | ✓ (ingredient all-day counts) | (bin management is adjacent but different) | B common |
| Prioritize / rearrange queue | ✓ (Prioritize orders article) | ✓ (move urgent forward; rearrange) | ✓ (station-specific priorities) | B common |
| Hold tickets | (not directly evidenced) | ✓ (hold action) | ✓ (held courses framing in Square; Crunchtime pacing) | B common |
| Display configuration (layout/columns/fonts/modifier colors) | ✓ | ✓ (Tiled/Classic/Split, fonts, colors) | ✓ (configurable views) | B common |
| Order-type/channel awareness on tickets | ✓ (online/kiosk/delayed filters) | ✓ (Split view by order type; delivery labels) | ✓ (in-house vs off-premise capacity) | B common |
| Fulfillment analytics (bump/prep/ticket times) | ✓ | ✓ | ✓ | B common |
| Bump bar hardware support | (hardware page; not directly evidenced in fetched text) | ✓ (USB bump bars) | ✓ (Kitchen Hardware page exists) | B common |
| Printer/label printing from KDS | ✓ (kitchen printers referenced; modifier "Kitchen name" for KDS+printers) | ✓ (Bluetooth ticket/label printers) | (not directly evidenced) | B common |
| Recall of third-party platform status on completion | ✓ (Automatic Order Update → Ready) | (SMS ready notifications instead) | ✓ (order-ready boards + SMS) | B common |
| Customer-facing ready board / order tracker | (order-ready texts) | ✓ (Order Tracker, Premium) | ✓ (order ready boards) | B common |
| SMS order-ready notifications | ✓ (related feature) | ✓ (Premium) | ✓ | B common |
| Course pacing / delayed routing by cook time | ✓ (staggered item prep times) | ✓ (sort by prep/pickup time) | ✓ (meal coursing, delayed routing) | B common |
| Made-to-stock bin/quantity prompts | ✗ | ✗ | ✓ (bin management) | A vendor-leaning |
| Dynamic load balancing by station capacity | ✗ | ✗ | ✓ | A vendor-specific |
| Kitchen score / speed-of-service companion app | ✗ | ✓ (On The Fly) | ✗ (Insights suite instead) | A vendor-specific |
| Multi-location standardization & remote screen management | (location-scoped devices) | ✓ (Enterprise; Brand Screen Settings) | ✓ (across all locations) | B common (enterprise tier) |
| Webhooks/API for order events | (Square platform APIs) | ✓ (webhooks on received/bumped) | ✓ (Data Streaming) | B common |
| No login for line staff | ✓ (device-code sign-in, not per-shift user) | ✓ ("no login for the line"; web-only roles) | (not directly evidenced) | B common |

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

A KDS is recognizable only when ALL three hold:

1. **The fulfillment ticket of record** — orders arrive from order-capture systems (POS, online ordering, delivery platforms) as tickets carrying items, modifiers, notes, and service context (table/name/order type/channel). The KDS itself captures no orders and takes no payment.
   - remove → an order feed / printer stream with nothing fulfilled against it
2. **The kitchen-facing ticket display** — screens placed at kitchen workstations present the active ticket queue to fulfillment staff (cooks, expeditors, to-go stations).
   - remove → back-office order management; the kitchen stops being the user
3. **The bump lifecycle** — staff mark items (commonly) and whole tickets as complete; completed tickets leave the active queue; recall/undo exists; the completion act is recorded and commonly feeds timing metrics.
   - remove → a passive order viewer (a "screen printer"), or a generic task board if tickets aren't bound to real orders

Jointly-held is load-bearing:
- 1 alone = order stream / kitchen printer output
- 2 alone = passive screen
- 2+3 without 1 = generic task/checklist board (tickets not bound to real orders)
- 1+2 without 3 = tickets displayed but never state-tracked (paper rail photographed on a screen)
- 1+3 without 2 = order-status backend with no kitchen surface

### L1 — Common Mature Structure (very common, not definitional)

- order-age timers with configurable color transitions (caution/late thresholds) and audio alerts on new tickets
- item-level and ticket-level completion with strike-through/tap-off interaction
- recall/undo of completed tickets
- station routing: multiple screens per kitchen, per-device source/category filters, prep vs expo roles, cross-screen clear/forward
- all-day counts (aggregate item totals across open tickets; fired vs held distinction in one product)
- queue management: default oldest-first ordering, rearrange, prioritize, hold
- display configuration: layouts (columns/tiled/split), text size, per-modifier colors/highlighting, kitchen-facing item/modifier names
- order-type/channel awareness (dine-in / takeout / delivery / kiosk; delivery-platform labels)
- fulfillment analytics: bump times, prep times, ticket times, station performance
- hardware ecosystem: bump bars, kitchen-grade screens, ticket/label printers alongside the display
- enterprise multi-location: standardized screen settings, remote device management, cross-location comparison

### L2 — Variant / Optional Structure

- customer-facing surfaces: order-ready boards, order trackers ("Being Prepared"/"Ready"), SMS order-ready / "I'm here" notifications
- course pacing and delayed routing driven by cook times (staggered item appearance)
- made-to-stock quantity prompting (bin management) — QSR made-to-stock contexts
- dynamic load balancing / capacity management across stations
- companion analytics apps (kitchen score, speed-of-service dashboards)
- connection posture: printer emulation (LAN) vs API/cloud integration — an implementation axis, not the Type
- offline/reliability posture: hardwired vs Wi-Fi guidance observed; explicit offline-mode behavior NOT directly evidenced (uncertainty)
- deployment: app on commodity tablets vs dedicated kitchen hardware; per-screen vs per-subscription pricing

### L3 — Vendor-specific (kept out of the final document)

- Square: Prep/Expo device-type naming, "Complete for all devices" vs "Complete only on this device" semantics, 3-second undo window, Automatic Order Update to third-party platforms, MicroTouch hardware line, Square Plus/Premium gating, per-device pricing
- Fresh: On The Fly kitchen score, Take Out View, Order Tracker on Fire TV Stick, I'm Here notifications, printer-emulation default, per-screen pricing tiers, Brand/Company/Location hierarchy
- Crunchtime: ConnectSmart heritage and rebrand, bin management, AccuPrep view, order-ready boards with guest SMS, "80+ POS integrations", "12-minute or less ticket time 80% of the time" marketing claim, "21 of top 25 casual-dining chains" claim

## Rejected Findings (considered, not promoted)

- **Color-coded timers as definitional**: rejected — the paper bump rail predates color timing; early monochrome KDS era; timing thresholds are configurable per product. L1.
- **Station routing as definitional**: rejected — a single-screen KDS in a small cafe remains a KDS; routing scales with kitchen complexity. L1.
- **All-day counts as definitional**: rejected — present in 2/3 sampled products, absent as such in the third (bin management is a different made-to-stock structure). L1.
- **"Replaces paper tickets" as the definition**: rejected — that is the historical anchor and marketing frame, not the structure. The Type is defined by what the digital system does, not by what it replaced.
- **KDS = "kitchen management"**: rejected as a Type equation — the market name collision (Crunchtime) is documented; the Commercial Kitchen Management Type (production planning: recipes/prep/food-safety) is a different center of gravity.
- **Offline mode as definitional**: rejected — no direct evidence in the fetched sample; held as uncertainty.

## Boundary Findings

| Neighboring Type | Seam | Remove-what test |
|---|---|---|
| Restaurant POS | POS captures orders and payment; KDS consumes already-captured orders for fulfillment. Vendor-articulated: "a POS and KDS aren't the same" (Crunchtime guide). KDS never takes payment or builds the order from a menu. | Remove ticket display/bump from a POS-fulfillment loop → POS; give the KDS order entry + payment → it has become a POS |
| Kitchen printer (not a Type) | The printer is the analog predecessor and still an integration substrate (Fresh "printer emulation"; Square "Kitchen name... on KDS and kitchen printers"). A printer outputs tickets but holds no state, no bump, no recall. | Add state + bump + recall to a printer stream → KDS; remove them → printer |
| Restaurant Delivery Management | Delivery management dispatches couriers/routes/drivers; a KDS may show delivery orders as tickets (with platform labels) but manages no couriers. | Remove kitchen prep display, add courier assignment/tracking → delivery management |
| Restaurant Online Ordering / Food Delivery Marketplace | Customer-side order capture vs kitchen-side fulfillment display; the KDS is a downstream consumer of those orders. | Remove the kitchen surface, add the customer cart/checkout → online ordering |
| Commercial Kitchen Management Application | Production planning (recipes, prep lists, food safety, costing) vs during-service ticket flow. Naming collision: Crunchtime sells its KDS as "Kitchen Management" — the collision is on the KDS side; the §20 pass already recorded the seam. | Remove the live ticket queue/bump, add recipe/production planning → commercial kitchen management |
| Institutional Foodservice Management | Standing meal programs for a known population vs anonymous à-la-carte ticket flow during service. | Remove tickets, add diner population + cycle menus → institutional foodservice |
| Task Management / generic boards | KDS tickets are bound to actual orders arriving from order systems; staff cannot create free-standing tasks. | Allow free task creation detached from orders → generic task board |

## Historical / Market-Sample Check

- **Paper bump rail (analog ancestor)**: POS printer prints tickets; tickets hang on a rail in the work area; cooks work them left-to-right; expo pulls ("bumps") them off when complete. Satisfies all three L0 legs at analog level: tickets from the order system, displayed at the pass, completion marked by removal. No color timers, no routing software, no analytics. → timing/routing/analytics are NOT definitional. ✓
- **Early KDS generation (1990s QSR, monochrome screens + bump bars)**: satisfies the core without color transitions, cloud, or analytics; Crunchtime's own heritage claim ("trusted... for over 30 years") corroborates the lineage. ✓
- **Hardware/platform variance**: dedicated kitchen hardware (Crunchtime), commodity Android tablets (Square), iOS/Android tablets (Fresh) — all satisfy; hardware form is variant. ✓
- **Regional check**: not deeply sampled (US-centric market evidence); no region-specific structure was baked into the core — the three legs are region-neutral. Held as minor uncertainty.

## Uncertainties

1. **Toast pole unverified** — www.toasttab.com 403 ×2. Toast is the largest US restaurant platform; its KDS is presumably structurally similar to Square's POS-embedded pole, but no Toast-specific claim is made. Sourcing limitation recorded.
2. **Offline behavior** — no direct evidence in fetched docs (Fresh documents hardwiring guidance; Square testimonial praises wireless). Offline-mode semantics deliberately not asserted.
3. **Recall in Crunchtime** — not directly evidenced in fetched text (implied by category norms); held as B-layer common from Square + Fresh only.
4. **Precise thresholds/limits** — no numeric timer defaults, ticket-count limits, or time windows asserted anywhere; all such values are product-configurable per the fetched docs.
5. **Regional KDS markets** (e.g., UK/EU dedicated KDS vendors) not sampled; core abstraction is region-neutral but the sample is US-weighted.

## Final Synthesis

The KDS is the kitchen-side half of the restaurant order loop: the POS/ordering side decides what is sold and paid; the KDS side gets orders made and handed off. Its defining core is exactly three jointly-held structures — the fulfillment ticket received from order-capture systems, the kitchen-facing display of the active ticket queue, and the bump lifecycle that tracks each ticket (and commonly each item) to completion with recall. Everything else the market associates with KDS — color timers, station routing, all-day counts, prioritize/hold, display configuration, channel labels, reporting, bump bars, ready boards, SMS notifications, pacing, load balancing, multi-location standardization — is standard mature capability or optional variant, not definition. The Type's name is stable in the market ("Kitchen Display System / KDS"); one major vendor (Crunchtime, via the QSR Automations acquisition) brands its KDS product "Kitchen Management," which is a naming collision with the Commercial Kitchen Management Application Type, not a Type merger — Crunchtime's own product page self-describes it as "Kitchen Display System (KDS) software."

## Boundary Issues (for STATUS.md)

1. Naming collision DISCHARGED from this side: commercial-kitchen-management pass (2026-09-07) flagged that Crunchtime sells its KDS under the name "Kitchen Management". Direct vendor evidence this pass: Crunchtime suite nav "Kitchen Management — Kitchen Display System (KDS) software..." and product page headline "KITCHEN DISPLAY SYSTEM"; "ConnectSmart® Kitchen is now Crunchtime Kitchen". The two Types remain distinct (during-service ticket fulfillment vs production planning); the collision is branding only.
2. No new taxonomy problems. The leaf stands as an independent Type.
