# Research Notes — Self-service Restaurant Ordering

## Research Goal

Understand what a Self-service Restaurant Ordering application actually is, from real products: what objects exist inside it, who acts on them, how a customer's self-composed order flows into the venue's operation, what the operator configures and controls, and where the boundary lies against neighboring Types — above all Restaurant Online Ordering (whose pass flagged a seam for this pass to ratify), Restaurant POS, Restaurant Menu Management, Kitchen Display System, and adjacent venue payment/display surfaces.

## Initial Boundary

Working hypothesis at start:

- The Type is the venue-installed self-service ordering station — the market's "self-ordering kiosk": customers compose and submit food orders themselves on a device the venue provides and controls, on premises, and the order enters the venue's operation for fulfillment during the visit.
- Most likely confused with: Restaurant Online Ordering (customer self-service on the customer's own device), Restaurant POS (staff-mediated order entry), Restaurant Menu Management (the catalog behind the kiosk surface), KDS (downstream fulfillment), Cashless Venue Platform (venue payment without order semantics), digital menu boards (display without ordering).
- Prior sibling passes already fixed several seams:
  - **restaurant-online-ordering** (2026-09-09): adopted seam = device + location + fulfillment context (customer's own device, typically remote, order-ahead semantics vs venue-installed kiosk on-premises with immediate in-store handoff). Blur zone documented: QR table ordering (customer's own device, ON-premises) ships inside online-ordering products; Toast's docs explicitly separate "guests order and pay at the table using their own mobile device" from the online ordering channel's hours. **This pass must ratify the seam and decide QR-table ordering's Type allegiance.**
  - **restaurant-menu-management** (2026-09-09): kiosk named as one consuming surface of the menu catalog ("POS order entry, guest web/QR menu, kiosk, ordering profile, delivery platform, digital menu board").
  - **restaurant-pos** (2026-09-09): composing actor (customer vs staff) + surface is the load-bearing difference; shared catalog/order stream in suite products is bundling, not identity.
  - **kitchen-display-system-kds** (2026-09-08): order-capture sources (including online ordering) feed KDS tickets.
  - **family-entertainment-center-management** (2026-09-07): self-service kiosks appear as venue machinery inside FEC management — venue-context packaging, not this Type's center.

## Research Questions

1. What is the self-service ordering surface in real products — what hardware/software shapes does it take?
2. What objects exist? (kiosk menu, order, payment, order-ready identification, device/configuration layer)
3. What does the customer flow look like end to end (browse → customize → pay → order-ready → pickup)?
4. How does the kiosk relate to the venue's POS and menu? (channel of the POS? curated subset of the menu? same order stream?)
5. What does the operator configure and control? (menu visibility, checkout settings, notifications, device management, lockdown)
6. Is payment at the kiosk definitional or common? What payment postures exist?
7. Where exactly are the boundaries: kiosk vs online ordering (surface provider), kiosk vs POS (composing actor), kiosk vs menu board (order transaction), kiosk vs self-checkout (food semantics)?
8. Is QR table ordering a variant of this Type or of Restaurant Online Ordering?

## Representative Products

Selected for market representation + documentation quality + different product philosophy + different customer tier:

| Product | Form | Tier / philosophy |
|---|---|---|
| Square Kiosk | POS-embedded self-serve station (iPad hardware + Square Kiosk app) | SMB; kiosk as a mode of the POS platform |
| Olo (Kiosk channel) | enterprise ordering platform's kiosk channel, built on the Ordering API | enterprise chains; kiosk as one channel of the digital ordering platform |
| Grubbrr | kiosk-specialist platform | mid-market/enterprise specialist; kiosk ecosystem (kiosk + Line Buster + progress board + lockers) across many verticals |
| Bite | kiosk software specialist | QSR/fast-casual/convenience/foodservice; AI-driven upsell philosophy |
| Ziosk | tabletop guest-facing tablet platform | casual-dining chains; pay-at-table / guest-engagement center of gravity with ordering as one capability |

## Sources

Evidence layers: **A** = directly observed on an official source for that product; **B** = cross-product commonality; **C** = canonical inference.

Fetched 2026-09-09:

- Square Support Center: "Set up Square Kiosk" (article 8538), "Adjust Square Kiosk checkout and order notification settings" (article 8313); Square hardware topic index (server-rendered; lists kiosk articles 8312 manage menu items/categories, 8314 payment errors, 8315 connection/power, 8537 kiosk profiles, 8539 branding, 8540 preview diner experience, 8541 subscription).
- Olo Help Center: Ordering Platform Overview; Ordering category index; Kiosks section; "Creating a Kiosk Experience".
- Grubbrr: site root; "Self-Ordering Kiosks" product page; "Line Buster" product page.
- Bite: site root; "Kiosks" product page.
- Ziosk: site root (including FAQ).

Unreachable / not fetched:

- **Toast kiosk documentation**: doc.toasttab.com returned 403 on this pass (the same domain was reachable for the restaurant-online-ordering pass earlier the same day). Toast's kiosk offering is therefore evidenced only indirectly (Grubbrr's integration list; general market presence) — no Toast-internal kiosk mechanics are asserted anywhere in this research.
- **Grubbrr knowledge base** (help.grubbrr.com): 401, auth-gated. Grubbrr evidence is product-page strength.
- Square's help-center search is a JS shell; article URLs were located via the server-rendered hardware topic index instead.

## Product Observations

### Square Kiosk (evidence layer A)

- "Square Kiosk hardware (formerly known as Square Stand Mount) is a versatile iPad-driven unit that can be easily attached to a wall, secured to a countertop, or fixed to a VESA-compatible floor stand anywhere in your venue. With built-in contactless and chip card readers, you can process card payments either by tapping or inserting a card, as well as accepting mobile tap payments such as Apple Pay and Google Pay."
- "When Square Kiosk hardware is paired with the Square Kiosk app, it creates a self-serve station that empowers customers to place orders and complete the checkout flow independently."
- Setup flow (Dashboard → Settings → Device management → Kiosk): select location → name the kiosk → "Select what item categories you want to show on your Kiosk menu" → associate category images → generate a device code → sign in on the iPad. Kiosk Settings page then manages devices, categories/items, branding, new devices.
- Prerequisite: "You also need at least one active point of sale device (phone, iPad, or Square hardware) using the Square Point of Sale app." (companion POS required)
- Kitchen routing: "Square Kiosk, when used as a self-serve ordering station with the Square Kiosk app, cannot directly connect to accessories like barcode scanners and receipt printers… You can print kiosk order tickets from your companion point of sale devices if they are connected to your kitchen printers." Printer profiles carry an "Online & Kiosk order tickets" toggle; "These kitchen tickets will print through the printer setup via your point of sale device, along with any other kitchen ticket created from a point of sale order."
- Lockdown: Guided Access recommended "to prevent customers from tampering with your kiosk or closing the Square Kiosk app."
- Signage: downloadable templates (retractable banner, blade sign, wall poster) for signposting the station.
- Dual use: "you can also access the Square POS app through your Square Kiosk hardware" — the same hardware runs the staff POS app.
- Offline payments not supported on kiosk hardware running the kiosk app.
- Checkout settings (article 8313): "Customers can place orders at your Square Kiosk from the selection of items you add to your kiosk menu." Configurable: **dining options** ("such as For Here or To Go"), **payment** (gift card acceptance), **signature and receipt**, **tipping** (percentage or dollar amount, before/after taxes), **Smart Upsells** ("automated item recommendations to buyers during ordering").
- Order-ready notification: notify diners when the order is ready "using their name, table number, or order number"; optional text-message notifications with opt-out phone number; "Table number - to provide physical table numbers and deliver orders to the table"; "When customers enter their phone number for text message order ready notifications, the Square Kiosk app will automatically link their loyalty account."
- Kiosk profiles: "adjust the settings for multiple kiosk devices from Square Kiosk profiles."
- QR coexistence note: "If you are using other Square self-serve ordering features, such as QR code ordering with Square Online, keep in mind that your ordering hours for Square Kiosk and ordering hours with QR codes will remain the same." (Square treats QR ordering as a Square Online feature, separate from the Kiosk product.)

### Olo (evidence layer A)

- Ordering Platform Overview: "Our Ordering platform provides a foundation for restaurant brands to handle all their digital ordering needs. We integrate with popular POS systems, offer a fully branded white-label website/app experience, and API access for a full, end-to-end eCommerce experience."
- The Ordering category of the help center contains a dedicated **Kiosks** section beside Ordering Overview, Chargebacks, Order Throttling Strategies, Order Lead Time Strategies, Order with Google, Sync.
- "Creating a Kiosk Experience": "Through Olo's Ordering API, a restaurant can work with an agency to create a digital interface optimized for a physical device to be used in restaurants. Olo advises restaurants and agencies to think through what a user flow should be for an in-restaurant digital experience. **A kiosk ordering experience is different from a traditional digital ordering UI experience in that the kiosk has a physical footprint and is generally placed in a public location that may require a different workflow.**"
- (From the sibling pass's fetch of Olo's product page and help-center structure:) "Make it easy for guests to order directly—from your website, app, or kiosk"; the platform's operator model includes Dashboard (Store Settings, Handoff Modes), Menu admin, Ordering (incl. Kiosks), and an Expo kitchen-facing screen.

### Grubbrr (evidence layer A for product pages; mechanics at product-page strength)

- Root positioning: "GRUBBRR is a self-ordering kiosk platform for restaurants, stadiums, schools, and grocery operators, integrating with 93+ POS systems including Toast, Square, Clover, NCR, and PAR."
- Kiosk software features (product page): Smart Upselling Algorithms; Seamless POS Integration ("real-time data syncing"); Customizable User Interface ("Tailor the kiosk design, menu layout, and branding"); Multi-Language Support; Order Accuracy Enhancements ("allowing customers to review and confirm their orders directly"); Contactless Payments ("digital wallets, credit cards"); Dynamic Menu ("Update menu items, pricing, and promotions in real-time"); Loyalty Integration; Analytics & Reporting; ADA Compliant ("Adjustable displays, high-contrast text, and an onboard screen reader").
- Customer flow: "Customers can customize orders, verify choices, and indicate where they would like to get their order (their car, a stadium seat, or wherever else your business can bring their items)." "Restaurant self-service kiosk orders go straight to the kitchen, eliminating delays and miscommunications."
- Product family (separate product lines): Self-Ordering Kiosks; **Line Buster** (mobile kiosk); **Contactless Ordering**; Order Progress Board; **Self Checkout**; Kitchen Display; Digital Menu Board; Drive Thru; Food Lockers.
- Industries: restaurants, petroleum & c-store, corporate dining, grocery, venues & theaters, schools, ghost kitchens, stadiums & arenas, casinos & gaming, amusement parks, micro markets, retail.
- **Line Buster** (handheld venue device): "This handheld device empowers staff to take orders and process payments anywhere" AND "Put the power of ordering into the customer's hands… combines self-ordering and payment capabilities into a single device, so your customers can enjoy a seamless and personalized experience without relying on fixed-location hardware." "as soon as the customer pays, their order is sent directly to the kitchen." "All that's left is to collect their order from a designated location." — a venue-provided *mobile* ordering surface, still venue-owned hardware.

### Bite (evidence layer A for product pages)

- "Let guests browse the menu, customize their selections, and complete payment without needing to interact with a cashier."
- Verticals: QSR & Fast Casual, Convenience, Foodservice & Foodhalls.
- BiteLift: "analyzes every transaction in real-time to offer personalized, data-driven menu recommendations based on order history and various external factors."
- Integrations: "Point of Sale (POS), Loyalty, Gift Cards, and more, ensuring a truly omnichannel experience"; partners include Olo and PAR.
- Second product "Linebuster": "Streamline order-taking and minimize congestion to serve guests quickly during peak hours."

### Ziosk (evidence layer A for product pages/FAQ)

- "Ziosk is the pioneer of pay-at-the-table technology and a premier SaaS hospitality platform – offering the only guest-facing tablet that lives at the table – where service happens. Our core product suite includes solutions for pay-at-the-table, ordering, loyalty, guest engagement, guest feedback, advanced data collection, and actionable insights."
- "Ziosk is not a payment processor… integrates with major POS platforms including Aloha, Oracle, Micros, Positouch, Rezku, and Xpient," plus gateways/processors and loyalty platforms (Punchh, Paytronix).
- "Ziosk is device-agnostic. However, using our tablets ensures optimal performance as they feature rugged designs specifically built for the restaurant environment and Bluetooth."
- Center of gravity is pay-at-table + guest engagement (games, surveys, loyalty); **ordering is one capability of the tabletop platform** — the venue-installed tabletop form factor is the relevant evidence for this Type, not the engagement suite.

## Cross-product Comparison

| Dimension | Square Kiosk | Olo | Grubbrr | Bite | Ziosk |
|---|---|---|---|---|---|
| Surface provider | venue-installed Square hardware + kiosk app | venue device built on Olo's Ordering API (with agency) | venue-installed kiosks on vendor/market hardware | venue-installed kiosks | venue-installed tabletop tablets |
| Placement | wall / countertop / floor stand "anywhere in your venue" | "physical footprint… public location" | counter/lobby deployments across verticals | counter/lobby (QSR, c-store, foodservice) | at the table |
| Menu source | categories/items selected from the Square menus ("what item categories you want to show on your Kiosk menu") | Olo Menu admin (POS-mapped) | "Dynamic Menu — update menu items, pricing, and promotions in real-time"; POS-integrated | venue menu; POS/loyalty/gift integrations | venue POS menu via POS integration |
| Composing actor | customer, self-serve | customer | customer ("customize orders, verify choices") | customer ("without needing to interact with a cashier") | customer (at the table) |
| Payment | at the station: contactless/chip, Apple/Google Pay, cash sales, gift cards; tipping configurable | via the platform's payment machinery (Olo Pay per sibling pass) | contactless payments at kiosk | "complete payment" at kiosk | pay-at-table on the tablet |
| Order routing | kitchen tickets print via companion POS "along with any other kitchen ticket" | POS integrations; Expo screen | "orders go straight to the kitchen"; KDS/printer products | POS integration | POS integration (order + payment into POS) |
| Order-ready identification | order number / diner name / table number; optional text notifications | — (workflow advised per deployment) | Order Progress Board product (adjacent) | — | at-table (no handoff identification needed) |
| Upsell | Smart Upsells ("automated item recommendations… during ordering") | — | Smart Upselling Algorithms | BiteLift real-time recommendations | engagement prompts |
| Loyalty | auto-link via phone number at notification | platform loyalty | Loyalty Integration | loyalty integrations | Punchh/Paytronix partners |
| Configuration surface | Square Dashboard (Device management → Kiosk), per-device + profiles | Olo Dashboard + API | vendor dashboard (KB gated) | vendor dashboard | vendor platform |
| Lockdown / posture | Guided Access recommended; offline payments unsupported | — | — | — | rugged tablets "built for the restaurant environment" |
| Verticals | restaurants (Plus/Premium plans) | enterprise restaurant brands | restaurants, c-store, corporate, grocery, venues, schools, stadiums, casinos, parks, micro markets, retail | QSR & fast casual, convenience, foodservice & foodhalls | casual-dining chains |

### What is universal (B-layer, all sampled)

1. **The venue's menu is rendered as a customer-facing orderable catalog on the self-service surface** — the customer browses the venue's own items, prices, and customization options (Square: kiosk menu built from the Square menus; Grubbrr: dynamic menu; Bite: "browse the menu"; Ziosk: POS-integrated menu; Olo: platform menu admin).
2. **The customer composes the order themselves, without staff mediation**, on a surface the venue provides and controls (Square "self-serve station… independently"; Bite "without needing to interact with a cashier"; Grubbrr "customize orders, verify choices"; Olo "in-restaurant digital experience"; Ziosk guest-facing tablet).
3. **The composed order is recorded and handed into the venue's operation** — into the POS order stream / kitchen printing / KDS — as the instruction to prepare (Square kitchen-ticket mechanics; Grubbrr "orders go straight to the kitchen"; Olo POS integrations + Expo; Ziosk POS integration; Bite POS integration).
4. **The venue operates the surface as part of its estate**: per-device configuration, branding, menu curation, and (where documented) profiles across devices (Square Dashboard + kiosk profiles; Olo Dashboard; Grubbrr customizable UI; Bite/Ziosk vendor platforms).

### What is common but not definitional

- **Payment captured at the surface** — in all sampled products payment happens at the station/table (Square: card/contactless/cash/gift; Bite: "complete payment"; Grubbrr: contactless payments; Ziosk: pay-at-table). Whether an order-only kiosk configuration (pay elsewhere) exists in the market is **not directly evidenced** in this sample — held open, and payment is kept out of the defining core on conceptual grounds (the transaction spine belongs to the venue's POS; see Historical Check).
- Order-ready identification (order number / name / table number, text notifications) — Square-documented; adjacent machinery (progress boards) at Grubbrr.
- Upsell prompts / recommendations — Square Smart Upsells, Grubbrr smart upselling, Bite BiteLift; AI-driven at the specialist poles (era-current).
- Loyalty identification at the surface (Square phone-number auto-link; Grubbrr/Bite/Ziosk loyalty integrations).
- Multi-language UI, accessibility features (Grubbrr documents both; single-product-documented, held as example not invariant).
- Signage/discoverability of the station (Square sign templates).
- Analytics/reporting on kiosk orders (Grubbrr, Bite).
- Adjacent companion products in the same vendor families: order progress boards, food lockers, drive-thru boards, digital menu boards, self-checkout (Grubbrr sells each as a separate product line).

### Vendor-specific (L3 — stays here)

- Square: device codes (48-hour expiry), Guided Access lockdown procedure, printer-profile "Online & Kiosk order tickets" toggle, kiosk profiles, Smart Upsells, Vistaprint sign templates, Square Kiosk subscription plans, dual-use hardware (kiosk hardware runs the POS app), offline-payments-unsupported constraint, the ambiguous Kiosk-vs-QR ordering-hours note.
- Grubbrr: Line Buster handheld, Order Progress Board, Food Lockers, Drive Thru product, "93+ POS systems" claim, ROI calculator, SOC 2 Type II certification.
- Bite: BiteLift ML recommendations, Linebuster product name.
- Ziosk: Drop & Pay, zConnect, games, guest-engagement/survey center of gravity, "device-agnostic" posture.
- Olo: kiosk built via Ordering API with agency partners; Expo kitchen screen; Switchboard (digitized phone orders) as a separate channel.

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The venue's menu as a customer-facing orderable catalog on the self-service surface.** The venue's own offerings — items with prices and customization options — presented for the customer to browse and compose from. Remove → a digital menu board / signage (display without a transaction).
2. **Customer self-service composition on a venue-provided, venue-controlled surface located in the venue.** The customer — not staff — composes the order on a station the venue installs and operates, on site, without staff mediation. This is the load-bearing seam in both directions: remove the venue-provided surface → Restaurant Online Ordering territory (customer's own device); remove the customer self-service → Restaurant POS territory (staff-composed).
3. **The order of record handed into the venue's operation for in-visit fulfillment.** The composed order is recorded and transmitted into the venue's order flow (POS order stream, kitchen printer, KDS) as the instruction to prepare, and the customer takes the food within the visit — handoff at counter, table, or car side. The handoff is commonly matched by an identification token (order number, customer name, or table number), but the invariant is the in-visit handoff itself, not any particular identification scheme. Remove → a payment terminal or a sign-up screen; the order never reaches the kitchen.

Jointly-held load-bearing tests:

- 1 alone = digital menu board / menu display
- 2 without 1 = a locked-down device with nothing to sell
- 3 without 1+2 = staff-entered POS order
- 1+2 without 3 = a browse-only touchscreen menu
- 2+3 without 1 = a generic self-service terminal (ticketing/check-in class)
- 1+3 without 2 = online ordering (customer's own device) or staff POS entry

### L1 — Common Mature Structure

- payment captured at the surface (card/contactless dominant; cash and gift cards where documented; tipping)
- order-ready identification and notification (order number / name / table number; text messages)
- upsell prompts / item recommendations (rule-based to AI-driven)
- loyalty identification at the surface
- per-device configuration with profiles; branding; menu curation (subset selection, category images)
- dedicated-station posture with lockdown/kiosk mode (procedure documented at Square; the dedicated-device class is observable across the sample)
- analytics on kiosk orders

### L2 — Variant / Optional Structure

- form factor: floor-standing / countertop / wall-mounted kiosk, tabletop tablet, handheld venue device, drive-thru order board
- payment posture: pay-at-surface card-only vs cash-accepting; pay-at-table; (order-only/account-settled arrangements — unverified, held open)
- vertical packaging: QSR/fast-casual (canonical), convenience/petroleum, corporate & institutional dining, schools, stadiums/venues, grocery, ghost kitchens
- fulfillment destination: counter, table delivery, car/curbside, stadium seat, food lockers
- packaging: POS-embedded kiosk mode (Square), enterprise ordering-platform channel (Olo), specialist kiosk platform (Grubbrr, Bite), tabletop engagement platform with ordering (Ziosk)
- multi-language UI and accessibility features (Grubbrr-documented; single-product-documented in this sample)
- station signage/discoverability programs (Square-documented sign templates)
- AI-driven recommendations (era-current)
- dual-use hardware (same station runs staff POS — Square-documented)

### L3 — Vendor-specific

See Vendor-specific list; none of it enters the canonical document.

## Historical / Market-Sample Check

- **Early / order-only generation**: a touchscreen ordering station that prints an order ticket for the kitchen, with payment taken at the counter, satisfies all three L0 structures (venue-provided surface; customer composes from the menu; order handed to the kitchen with in-visit pickup). No payment hardware, no texts, no AI required. ✓
- **Institutional / regional deployments** (corporate cafeterias, school dining — verticals the sampled specialists explicitly serve): ordering on a venue station with settlement against a meal account rather than a card payment — the order semantics are identical; payment method is variant, not definition. (Account-settlement mechanics not directly fetched this pass — held as vertical-packaging inference, not asserted as observed mechanics.) ✓
- **Vending machines** fail the core: they dispense the product themselves; there is no composed menu order handed to a kitchen for preparation. ✓ (boundary holds)
- **QR table ordering** (customer's own device, on-premises): rides ordering machinery in sampled products but is packaged by vendors as an own-device product line (Square: QR ordering under Square Online, separate from Kiosk; Grubbrr: Contactless Ordering as a separate product beside its kiosks; Toast per the sibling pass separates at-table mobile ordering from channel hours). Assigned to Restaurant Online Ordering as a surface variant — see Boundary Findings. ✓
- Conclusion: the definition is not over-fitted to the modern pay-at-kiosk, AI-upsell era.

## Boundary Findings

1. **vs Restaurant Online Ordering — SEAM RATIFIED with refinement.** Both Types are customer self-service order capture from the venue's menu into the venue's operation. The sibling pass adopted "device + location + fulfillment context"; this pass refines the seam to its load-bearing leg: **who provides and controls the ordering surface**. Venue-provided, venue-controlled device (kiosk, tabletop tablet, handheld venue terminal) → this Type; customer's own device → Restaurant Online Ordering. Location and fulfillment context follow from the provider leg (venue device → on-premises, in-visit handoff; own device → typically remote, order-ahead semantics). Vendor behavior supports the provider leg as the real split: kiosk vendors package own-device ordering as **separate product lines** (Grubbrr: "Contactless Ordering" beside "Self-Ordering Kiosks" and the venue-owned handheld "Line Buster"; Square: QR ordering under Square Online with its own settings, Kiosk as a separate product; Toast per the sibling pass separates at-table mobile ordering from the online channel's hours).
2. **QR table ordering — DECISION.** QR table ordering (customer's own device, on-premises) is a **surface variant of Restaurant Online Ordering**, not of this Type. Rationale: the surface provider is the customer, not the venue; it ships inside online-ordering products in both passes' samples; no sampled kiosk product claims it as kiosk machinery. Venue-installed tabletop devices (Ziosk-class) and handheld venue devices (Grubbrr Line Buster-class) remain on this side despite being mobile or table-side — they are still venue-provided surfaces.
3. **vs Restaurant POS** — the composing actor and surface differ: POS is the staff-mediated transaction surface; the kiosk is a customer-facing capture channel. In POS-embedded products the kiosk shares the menu catalog and the order stream (Square: kiosk tickets print "along with any other kitchen ticket created from a point of sale order"; the same hardware can run either app). Removal test: remove customer self-service composition → what remains is a POS.
4. **vs Restaurant Menu Management** — menu management maintains the catalog of record; the kiosk consumes it as one publishing surface with a curated subset (Square: "select what item categories you want to show on your Kiosk menu"). Removal test: remove the order transaction → menu management stands; remove the catalog → the kiosk has nothing to sell.
5. **vs Kitchen Display System** — the kiosk produces orders; the KDS fulfills them. Kiosks are one of the order-capture sources feeding KDS tickets (per the KDS pass). Removal test: remove order capture → the kiosk collapses; remove fulfillment → the KDS collapses.
6. **vs Digital Menu Board** — display without an order transaction. Grubbrr sells Digital Menu Boards and Self-Ordering Kiosks as separate product lines — the vendor's own catalog draws the seam.
7. **vs Self-checkout / Cashless Venue Platform** — generic goods scanning or venue-wide stored-value payment lacks menu-composition and kitchen-fulfillment semantics. Grubbrr sells "Self Checkout" as a separate product from its kiosks.
8. **vs Food Delivery Marketplace** — no multi-seller aggregation; the kiosk is one venue's own surface. (Marketplace machinery is out of scope.)
9. **vs Restaurant Delivery Management** — kiosk orders are in-visit handoffs (counter/table/car-side at the venue); courier dispatch and delivery progression are the sibling Type's center. Drive-thru order boards (Grubbrr Drive Thru) sit at this Type's edge: venue-provided order capture on-premises, fulfilled by the venue's own lane — held as a form-factor variant.

## Uncertainties

- Toast's kiosk product could not be documented (doc.toasttab.com 403 this pass). Toast's kiosk existence is evidenced only indirectly (Grubbrr integration list). No Toast-internal mechanics asserted.
- Grubbrr and Bite evidence is product-page strength (Grubbrr's knowledge base is auth-gated; Bite's help content not reachable). Their internal mechanics (order lifecycle states, configuration depth) are not asserted.
- Whether order-only kiosk configurations (no payment at the surface) exist as a market pattern: not directly evidenced in-sample. Payment is kept out of the defining core on conceptual grounds; the uncertainty is recorded rather than resolved.
- Square's note that "ordering hours for Square Kiosk and ordering hours with QR codes will remain the same" is ambiguous in the fetched text (shared setting vs coincidental equality) — not asserted either way.
- Ziosk's ordering depth (whether its tabletop ordering is a full menu-composition flow or primarily order-at-the-table adjuncts) is not documented at operational level on the fetched pages; Ziosk is used as form-factor/variant evidence only.
- Olo's kiosk documentation is a single advisory article; the kiosk's operational depth (per-device settings, identification, payment) is not documented at help-center level — Olo evidence is held at channel-framing strength.

## Final Synthesis

A Self-service Restaurant Ordering application is the venue-operated self-service ordering surface — in market terms, the self-ordering kiosk. Its defining core is three jointly-held structures: the venue's menu rendered as a customer-facing orderable catalog on the self-service surface; customer self-service composition on a venue-provided, venue-controlled surface located in the venue; and the composed order recorded and handed into the venue's operation for in-visit fulfillment, with identification and handoff semantics. Everything else — payment at the surface, order-ready texts, upsell and AI recommendations, loyalty lookup, multi-language and accessibility machinery, per-device configuration — is common mature structure or variant capability, not definition. The Type sits between the customer's own device (Restaurant Online Ordering — the ratified seam, with QR table ordering assigned to that side), the staff-mediated transaction surface (Restaurant POS), the catalog behind it (Restaurant Menu Management), the kitchen fulfillment layer after it (KDS), and the display-only and payment-only surfaces it must not be confused with (digital menu boards, self-checkout, cashless venue platforms).
