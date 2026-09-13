# Research Notes — Mobile POS

Research date: **2026-09-08**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)
Joint-review context: this leaf was flagged for joint review by the sibling pass `research/retail-point-of-sale.md` (2026-09-06), which assessed Mobile POS as "likely Variant/Alias of Retail POS" and deferred the decision to this pass. The decision is discharged in §Boundary Findings below.

---

## Research Goal

Understand what a Mobile POS (mPOS) application is as an Application Type in its own right: what the sale surface is, what hardware and software participate, who uses it and where the sale happens, which workflows and rules are specific to selling from a portable device, and how the Type relates to the sibling leaf Retail Point of Sale (fixed-counter sale execution), to payment products, and to customer-side mobile commerce.

## Initial Boundary

Initial hypothesis (before research):

- Core use: executing item-level in-person sales from a portable device (phone/tablet/handheld, typically with a paired or built-in card-acceptance capability), carried to wherever the exchange happens — a counter, the sales floor, a queue, a market stall, a pop-up, a customer's door.
- Primary users: micro-merchants without fixed premises (markets, pop-ups, mobile services); store associates doing line-busting or floor selling; occasionally field/delivery sellers.
- Nearest types: Retail Point of Sale (fixed-counter form of the same spine — the flagged sibling), Restaurant POS (different sale semantics, but restaurant handhelds use a mobile surface), Payment Processing Platform / card terminals (money rails vs sale execution), e-commerce/mobile-commerce checkout (customer-operated, remote), mobile wallets (consumer-side).
- Unknowns: does a distinct mPOS market/category exist with products that are mobile-native rather than "modes" of a counter POS? Which parts of the sale workflow change when the surface is portable? How do connectivity and device security rules work? Is "portability" a definitional invariant or merely a deployment option?

## Research Questions

1. What constitutes the sale surface (device + acceptance hardware), and what hardware classes exist?
2. How is the seller's catalog held and how are sales composed on a small touchscreen?
3. How does in-person payment capture work on a portable device (paired reader, built-in NFC/software-only, all-in-one terminal)?
4. Where do sales happen? Which contexts do vendors themselves name (market, pop-up, line busting, tableside, on-the-go)?
5. What is common vs variable in receipts, cash handling, inventory decrement, and back-office sync when there is no fixed counter?
6. What rules matter: device security, permissions, connectivity, offline selling, refund handling on the go?
7. Who are the users at each pole of the market?
8. Where is the boundary against Retail POS (counter form), payment terminals, mobile commerce, and restaurant handhelds — and is Mobile POS a Type or a Variant?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers. Products A–D were newly researched for this leaf; supplementary products E–G reuse directly attributed evidence from the 2026-09-06 retail-POS pass.

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Square Point of Sale (mobile surfaces: phone/tablet app, Readers, Handheld, Tap to Pay) | Micro-SMB→SMB; payments-first; the archetypal mPOS lineage (phone + dongle reader) | Best-in-class help center; documents the full mobile surface spectrum from dongle to software-only acceptance |
| Shopify POS (mobile use) | SMB→mid; commerce-platform-first; mPOS as one selling surface of a unified back office | Vendor publishes its own mPOS definition guide and a POS-types taxonomy naming "mobile POS" |
| SumUp | Micro-merchant; European; mobile-first merchant kit (readers + app) | Non-US-centric sample; help center exposes the full product structure of a portable-first kit |
| PayPal Point of Sale (Zettle by PayPal) | Micro→SMB; European mPOS lineage (iZettle → Zettle → PayPal POS) | The original European phone+reader mPOS; vendor segments its own customers by "On-the-go" selling |
| (suppl.) Clover | SMB–mid; hardware-app-platform | Handheld/edition evidence from developer docs (prior pass) |
| (suppl.) Loyverse | Global SMB; free mobile-first POS app | Phone/tablet-native product; topic-inventory evidence (prior pass) |
| (suppl.) Erply | Mid-market/enterprise suite | Ships "Mobile POS" as a named edition of one suite (prior pass) |

## Sources

### Shopify (official product page + vendor guide — Tier 2 + vendor explainer)

- POS product page incl. POS-types FAQ: https://www.shopify.com/pos (fetched 2026-09-08)
- "How To Choose a Mobile POS (mPOS) System" guide: https://www.shopify.com/blog/mobile-pos-system (fetched 2026-09-08)
- Limitation: Shopify Help Center returned HTTP 403 in the 2026-09-06 pass (twice-confirmed; not retried this pass). Shopify operational detail is kept at product-page/guide level.

### Square (official help center — Tier 1)

- Payments topic (article inventory): https://squareup.com/help/us/en/topic/payments (fetched 2026-09-08)
- "Accept payments with Tap to Pay on iPhone" (full article): https://squareup.com/help/us/en/article/7786-get-started-with-tap-to-pay-on-iphone (fetched 2026-09-08)
- "Accept payments with Square Handheld" (full article): https://squareup.com/help/us/en/article/8499-accept-payments-with-square-handheld (fetched 2026-09-08)
- Referenced titles (inventory only, not individually fetched): Reader for magstripe (5174), Reader for contactless and chip (5672), Square Terminal (6543), Square Stand (5175), Tap to Pay on Android (7960), offline payments (7777), tableside mobile POS (8152), split payments (5097), custom sale amounts (5429), print/send receipts (6139), customize payment types (6389)
- Prior-pass fetches (2026-09-06): Register checkout flow (6255), returns/exchanges/unlinked refunds (6350), cash/checks (5177), settle/tips (8375)

### SumUp (official support centre — Tier 1 index; article bodies inaccessible)

- Support centre root (product/section inventory): https://help.sumup.com/ (fetched 2026-09-08)
- Limitation: product page sumup.com 403; individual help-article URLs render only navigation (JS app, no article body). Evidence is capability-inventory level.

### PayPal Point of Sale / Zettle (official product pages — Tier 2)

- International root: https://zettle.com/ ; GB product page: https://www.zettle.com/gb (fetched 2026-09-08)
- POS systems page: https://www.zettle.com/gb/pos-systems (fetched 2026-09-08)
- Limitation: help centre https://zettle.help/hc/en-gb timed out (1 attempt; abandoned). Operational detail kept at product-page level.

### Supplementary (prior pass 2026-09-06, directly attributed)

- Clover developer documentation — data model, atomic order, transaction types: https://docs.clover.com/ (this pass's device page is a JS app; hardware-availability docs URL 404)
- Loyverse Help Center — Sales topic inventory: https://loyverse.com/help (article bodies 404 in prior pass)
- Erply Wiki — section inventory + sales-permissions article: https://wiki.erply.com/

---

## Product A — Square Point of Sale (mobile surfaces)

### Key observations (evidence layer A — directly observed)

- **Surface spectrum (from the payments topic inventory)**: Square documents acceptance per device — phone/tablet app with **Reader for magstripe** (dongle), **Reader for contactless and chip**, **Square Handheld** ("pocketable POS device with an integrated camera and barcode scanner"), **Square Terminal**, **Square Stand** (counter dock), **Tap to Pay on iPhone / Android** (software-only acceptance on the seller's phone), plus Register, Kiosk, and Virtual Terminal for other surfaces. One app family, many surface classes; the mobile class is the largest single group.
- **Software-only acceptance (Tap to Pay article)**: "Accept contactless payments anywhere on-the-go with just your iPhone — no card reader needed." Flow: enter amount (or charge a sale) in the POS app → select Tap to Pay → customer holds card/NFC device to the front of the phone → audible beep + authorization spinner → receipt screen → New Sale. Constraints observed: device passcode required; a stable internet connection required (offline payments explicitly not supported with Tap to Pay); payment fails cleanly ("customer has not been charged") and cannot be retried — a new tap is required; the transaction registers as a Card payment in Transactions with card type and last 4 digits.
- **Device security rules (Tap to Pay article)**: "Never hand your mobile device over to your customer. Have the customer hold out their card or NFC device… to tap on your iPhone." Passcode option to prevent customers backing out of the payment screen. The sale surface stays with the seller; the customer only presents the payment instrument.
- **Purpose-built handheld (Square Handheld article)**: scan items from the Item Library with the integrated barcode scanner/camera → tap line to modify quantity, apply tax → keypad for custom sale amount → Review sale → Charge → Confirm & Pay → customer pays tap/insert/swipe on the device (magstripe requires an attachable USB-C Reader) → confirmation screen with digital receipt via phone/email entry → payment cancelable before processing. Payment types include card on file, house accounts, QR codes, cash. "Manage orders anywhere" and "keep track of inventory on the go."
- **Permissions**: articles are scoped to "account owners or team members with the checkout permission to take payments. Set permissions in Square Dashboard" — permission gating carries over unchanged from the counter form.
- **Contexts named by the vendor**: "anywhere on-the-go" (Tap to Pay), "tableside" (restaurant mobile POS article), "on the go" inventory management (Handheld). Retail checkout and restaurant tableside are modes of the same app family.
- Prior-pass observations that carry over (evidence A): checkout flow from the item Library/Favorites, split payments, custom amounts, refunds/returns/exchanges, cash drawer auto-open, offline card payments (mode exists for reader-based acceptance).

## Product B — Shopify POS / Shopify mPOS guide

### Key observations

- **Vendor's own market definition (mPOS guide, evidence A for definition)**: "A mobile point-of-sale system (mPOS) is a portable hardware and software system that processes sales. An mPOS is nearly the same as a traditional point-of-sale (POS) system, except that it doesn't have to be anchored to one checkout counter… you can install POS software onto a tablet or smartphone and serve customers wherever they are. And because your checkout moves wherever you need it, your shop doesn't necessarily need a checkout counter at all."
- **Documented mPOS transaction flow (guide, evidence A)**: 1) associate scans the item's barcode (scanner or device camera) or searches for it; 2) the mPOS calculates the total including tax and discounts; 3) customer pays by card, cash, digital wallet, gift card, or loyalty points ("if the customer is paying with cash away from the register, the associate will need to bring them change"); 4) the mPOS processes the payment, offers emailed or printed receipt, and updates inventory counts.
- **Named contexts (guide + product page FAQ, evidence A)**: line busting ("virtually eliminates lines at the checkout counter"), on-the-floor service (check inventory without leaving the floor; save a customer's cart and retrieve it later), pop-ups, markets, trade shows, "anywhere in between"; product page FAQ: "Mobile POS systems are better for businesses selling at events like pop-ups, markets, and trade shows. A mobile POS system allows retailers to process transactions wherever their customer is. These systems typically combine POS software and hardware into a single handheld device. Many brick-and-mortar businesses, however, are also starting to use mobile checkouts in their stores as a way to better serve their customers."
- **Hardware anatomy (guide, evidence A)**: tablet or smartphone (most mPOS software runs on iOS/Android devices); mobile card reader (magstripe/NFC/contactless/wallets); barcode scanner (optional — device camera usually suffices); cash drawer and receipt printer ("if you want to accept cash… you'll need a cash register at one of your counters"; "if you want to give customers printed receipts, keep a receipt printer next to it") — i.e., counter peripherals are optional add-ons, not the base form.
- **Software-only acceptance**: Tap to Pay turns the smartphone itself into the payment device — "no external hardware required" (guide + product page).
- **POS-types taxonomy (product page FAQ, evidence A for market structure)**: countertop POS (permanent stores) / mobile POS (events, pop-ups, markets, trade shows; increasingly in-store) / multichannel POS (in-store + online omnichannel). A separate four-type list (standalone/integrated/mobile/cloud-based) appears in the guide — an older, deployment-shaped taxonomy. Both confirm surface and channel as the axes the market uses to slice POS.
- Prior-pass observation: POS checkout flow (scan → total → checkout → pay → receipt → inventory update) and unified back office.

## Product C — SumUp

### Key observations (evidence layer A for capability inventory; article bodies JS-blocked)

- **Product structure (support centre inventory)**: acceptance hardware lines — **Solo card reader**, **Solo Lite**, **Air card reader**, **3G card reader** (Bluetooth-paired readers), **SumUp Terminal** (standalone device with item catalogue on it), **Tap to Pay on iPhone** section ("Accept contactless payments with Tap to Pay on iPhone", setup + FAQ), **SumUp Kiosk**, **POS PRO - Goodtill** (separate POS line).
- **Sale-side structures (section titles)**: "Add items to my item catalogue" (shared by Terminal, POS, and Online Store sections — one catalogue across surfaces), "Accept card payments", "Set up tipping", "Sales history", "My reports", "Payouts" (payout settings, payout reports), "Payment disputes: Chargeback procedures", "Gift Cards", "SumUp Loyalty", "Invoices", "Payment links", "QR Order & Pay", "Business Account".
- **Interpretation**: a portable-first merchant kit — the seller's phone + a paired reader is the base configuration; a catalogue, sale history, tipping, refunds/disputes, and payouts surround the same sale spine. The merchant can graduate to a standalone Terminal or a kiosk without leaving the product family.
- **Limitation**: article bodies not fetchable (JS); no operational detail asserted beyond section/article titles.

## Product D — PayPal Point of Sale (Zettle by PayPal)

### Key observations (evidence layer A — product pages)

- **Positioning**: "Our point-of-sale app helps you easily manage products and sales from a smartphone or tablet. You can accept payments on your phone with Tap to Pay, set up a card reader in minutes, or get the all-in-one portable Terminal which has the PayPal POS software built in." Brand note: "Zettle by PayPal becomes PayPal Point of Sale" (iZettle lineage).
- **Hardware classes (POS systems page)**: **PayPal Reader** — "Pair the card reader to your mobile device and you're good to go" (touchscreen reader; Bluetooth or USB-C; on-screen tipping; optional countertop dock); **PayPal Terminal** — all-in-one portable device with the POS app built in (Wi-Fi or 4G; optional barcode scanner); **Tap to Pay on phone** — "Transform your phone into a payment device… no additional hardware needed."
- **Context as market segmentation (evidence A)**: the vendor's own lead-qualification form asks "How are you selling your products or services?" with "On-the-go" as a first-class answer alongside "In store" and "Online" — on-the-go selling is a named, product-supported context.
- **Surrounding services**: payments solutions page (major cards + wallets), funds "typically arrive in your PayPal Business account within minutes", integrations (e-commerce, accounting) so "your POS can become a hub for your business."

## Supplementary products (evidence reused from the 2026-09-06 pass; directly attributed)

- **Clover** (developer docs): order/payment data model (order ← line items/modifiers/discounts; payment ← tender semantics sale/auth/pre-auth/closeout) — the same sale spine any mobile client would exercise; Android-based device family with app market; prior pass recorded regional editions. This pass could not reach Clover mobile-hardware pages (device page is a JS app; hardware-availability docs 404) — Clover is used only for the shared spine, not for mobile-specific claims.
- **Loyverse** (help topic inventory): phone/tablet POS app; Sales topic includes "How to Make Sales", "Sell Items Using Barcode Scanners", "Barcode Scanning by Built-in Camera", "Split Payment", "Offline Use of Loyverse POS", "Shift Management", "Open Tickets" — a free mobile-first POS whose help surface documents camera-scanning and offline selling as first-class topics.
- **Erply** (wiki): enterprise retail suite shipping **Mobile POS** as a named edition alongside BerlinPOS/BrazilPOS/Self-Service POS — the mobile form as a deployment edition of one suite at the enterprise end.

---

## Cross-product Comparison

| Dimension | Square | Shopify POS | SumUp | PayPal POS (Zettle) |
|---|---|---|---|---|
| Sale surface | phone/tablet app + attachable Readers; purpose-built Handheld; software-only Tap to Pay | phone/tablet app (iOS/Android); Tap to Pay; counter dock/hardware optional | phone + paired reader (Solo/Air/3G); standalone Terminal; Tap to Pay on iPhone | smartphone/tablet app; paired Reader; all-in-one portable Terminal; Tap to Pay on phone |
| Catalog on device | Item Library (items, variations, modifiers, categories) — observed on Handheld + prior pass | unified Shopify catalog (products synced from back office) | item catalogue shared across Terminal/POS/Online Store | product management "from a smartphone or tablet" |
| Item lookup | scan (integrated scanner/camera), Library/Favorites, keypad custom amount | scan (scanner or device camera) or search | catalogue + card-present flows (inventory-level evidence) | optional barcode scanner accessory (Terminal); app flows generic |
| In-person capture | tap/insert/swipe on Reader or Handheld; Tap to Pay on phone NFC | card reader for swipe/NFC/wallets; Tap to Pay without hardware | paired Bluetooth readers; Terminal; Tap to Pay | Reader (Bluetooth/USB-C); Terminal; Tap to Pay |
| Digital receipts | phone/email entry on confirmation screen; print/send receipts article | emailed or printed receipt at merchant's choice | (inventory-level) | (product-page level) |
| Cash | cash tender + optional drawer; associate brings change (Shopify wording) | cash drawer optional hardware | inventory-level | inventory-level |
| Inventory decrement | "keep track of inventory on the go" (Handheld) | "automatically updates inventory levels" | shared catalogue; inventory section | product management (depth unverified) |
| Sale history / reversals | Transactions list; refunds/returns (prior pass) | refunds and exchanges as essential mPOS features (guide) | Sales history + chargeback/dispute procedures | sales tracked "all in one place" (depth unverified) |
| Permissions | checkout permission per team member | staff permissions (product page) | not verified (inventory-level) | not verified (product-page level) |
| Offline | offline card payments mode exists (reader-based); Tap to Pay requires connectivity | not verified (help 403) | not verified | not verified |
| Contexts named by vendor | on-the-go, tableside, anywhere | line busting, pop-ups, markets, trade shows, floor selling | (kit positioning) | "On-the-go" as first-class segment answer |
| Back office companion | Square Dashboard (web) | unified Shopify admin | SumUp dashboard/app | PayPal Business account + integrations |

**Reading**: all four implement the identical sale spine of the retail pass (priced catalog → sale construction → in-person tender → recorded transaction + receipt). What varies is (1) the acceptance substrate (paired reader ↔ built-in NFC ↔ all-in-one terminal), (2) how much counter paraphernalia exists (paperless base ↔ optional drawer/printer/scanner), and (3) the selling context the product is built around (no-premises micro-merchant ↔ in-store floor selling). No product ties the sale to a fixed location.

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Seller-defined priced item catalog (carried on the mobile device)
└── Sale construction on the device (operator composes basket from catalog;
    system prices it, incl. tax)
    └── In-person payment collection at the point of exchange
        (portable card/other acceptance via paired or built-in capability)
        └── Completed transaction record + receipt
```

Executed on a **portable, seller-carried sale surface** — a general-purpose phone/tablet or a purpose-built handheld, with payment capture either attached/paired or built into the device — **so the sale can be taken to wherever the exchange happens** (counter, sales floor, queue, table, market stall, pop-up, customer's door). No fixed checkout location is required.

Five properties. Removal tests:

- Remove the **priced item catalog** → the product becomes an amount-entry mobile card reader / payment terminal, not a POS.
- Remove **sale construction on the device** → same failure; a bare charge is not a sale.
- Remove **in-person payment collection** → the product becomes remote checkout / payment links / invoicing — a different Type.
- Remove the **completed transaction record + receipt** → ephemeral acceptance hardware, no system of record.
- Remove **portability of the sale surface** (fix it as a purpose-built counter register) → the sibling Type Retail Point of Sale. This is the leaf's defining addition, not the shared spine.

### Historical / market-sample check (§24)

- **Original smartphone-era mPOS (dongle reader + app, early 2010s)**: phone app with item entry, attachable magstripe reader, digital receipt — fits the core with zero modern additions.
- **Purpose-built portable terminals/handhelds (pre-smartphone and current)**: portable devices with item keys / catalog + tender + receipt (delivery, market, festival, queue contexts) — fit; the surface need not be a general-purpose phone.
- **Software-only acceptance (Tap to Pay era)**: no hardware at all beyond the seller's phone — fits; acceptance substrate is implementation, not definition.
- **Amount-only portable card machines** (no catalog, no sale construction): fail the catalog test — correctly excluded as payment terminals, even though the market colloquially calls the hardware "mobile card readers."
- **Restaurant handhelds**: structurally portable sale surfaces, but the sale semantics are check/table-based (Restaurant POS) — excluded as primary; recorded as a cross-Type variant using this surface class.
- Conclusion: the L0 does not over-fit the smartphone/cloud era; the portability invariant holds across dongle-era, handheld-era, and software-only-era products.

### L1 — Common Mature Structure

Present in most mature modern products; not required for the Type:

- **Catalog layer synced from a companion** (web dashboard/back office app); items with prices, tax treatment, often variants/categories; shared across the merchant's devices and surfaces.
- **Item lookup adapted to small screens**: visual grid/favorites, search, camera barcode scan, attachable scanners, keypad/custom amount.
- **Sale adjustment**: quantity, notes, discounts, tax display; held/saved carts for returning to a customer.
- **Tender set**: contactless tap, chip insert, magstripe swipe (substrate-dependent), mobile wallets, cash (with change computation), card on file, gift cards, QR/wallet schemes; tipping prompts where the vertical calls for them.
- **Digital-first receipts**: email/SMS/QR as the default path; printed receipts only when optional printer hardware exists; reprint from the transaction record.
- **Transaction history on the device** with refund flows; dispute/chargeback handling in the surrounding service.
- **Inventory decrement and stock visibility** on sale; back-office reporting; payout/settlement tracking.
- **Staff accounts and permission gating** for sensitive actions (take payment, refund), carried over from the counter form.
- **Offline posture** for reader-based acceptance in some products (full or payments-only), reconciled when connectivity returns.
- **Multi-device operation**: several devices on one account sharing catalog/history.

### L2 — Variant / Optional Structure

- **Acceptance substrate**: paired Bluetooth/USB reader ↔ software-only NFC on the seller's phone ↔ all-in-one portable terminal with the app built in.
- **Business context**: no-premises micro-merchant (markets, mobile services, food trucks); pop-up/event selling; in-store floor selling and line busting in staffed stores; delivery/field selling.
- **Counter-peripheral completeness**: paperless base kit ↔ dock/stand, cash drawer, receipt printer, scanner as add-ons.
- **Connectivity posture**: online-only (some software-only acceptance) ↔ offline-capable reader flows.
- **Scale**: single device as the merchant's entire POS ↔ multiple devices in a store alongside counter registers.
- **Platform**: iOS / Android / cross-platform apps; purpose-built handheld hardware.
- **Regional payment mix**: local card schemes, QR wallets, regional wallets.
- **Vertical adaptations**: services/appointments, food & beverage (tableside ordering on restaurant-semantics systems), benefits schemes.

### L3 — Vendor-specific (research notes only)

- **Square**: Tap to Pay specifics (per-transaction contactless limits, device-code sign-in restriction, no-retry failure semantics, Apple Account linking, passcode option to guard the payment screen); Handheld hardware details (integrated scanner, USB-C magstripe reader requirement); bar-tab pre-authorization capture behavior; hardware family names (Register/Stand/Terminal/Handheld/Reader/Kiosk).
- **Shopify**: Smart Grid customization, email carts, save cart, Tap to Pay on Shopify POS, hardware store, POS Pro/Lite plan split, "four types of POS" legacy taxonomy.
- **SumUp**: product names (Solo, Solo Lite, Air, 3G Reader, Terminal, Kiosk, POS PRO/Goodtill), Business Account/payouts machinery, Cash Advance, Personal Finance app.
- **PayPal POS/Zettle**: PayPal Reader/Terminal pricing offers, funds-arrival claims, Zettle→PayPal rebrand, lead-form "On-the-go" segmentation.

---

## Vendor-specific Findings

Single-product findings that must not be promoted to the canonical core:

- **No-retry failure semantics for software-only acceptance** (Square Tap to Pay: failed payment cannot be retried; a new tap is required) — payment-industry-plausible but observed in one product only → product-specific.
- **Per-transaction limits for Tap to Pay** (Square) — regulatory/product-specific numbers; excluded from the final document.
- **Device-code sign-in restriction** for Tap to Pay (Square) — product-specific operational detail.
- **"On-the-go" as an explicit lead-segmentation answer** (PayPal POS) — marketing/segmentation artifact, used only as evidence that the context is market-recognized.
- **Email carts / save cart** (Shopify) — omnichannel conveniences; single-product named features → Optional.

## Rejected Findings

Considered and rejected during synthesis:

- **"Mobile POS is defined by card-reader acceptance."** Rejected: two of four sampled products ship software-only acceptance (built-in NFC on the seller's phone), and one ships an all-in-one terminal; the acceptance substrate is an implementation axis, not the definition.
- **"Mobile POS serves only micro-merchants without premises."** Rejected: the sampled vendor documentation names in-store uses (line busting, floor selling, tableside) as first-class contexts; the micro-merchant pole is one variant.
- **"A tablet docked at a counter stops being Mobile POS."** Rejected in the strong form: the invariant is the device class and its relocatability, not the position at every moment. The honest cut: purpose-built fixed registers (integrated drawer/printer hardware) are the counter form (Retail POS); portable-device surfaces remain the mobile class even when momentarily docked. Both siblings document each other as the nearest different surface class rather than different sale machinery.
- **"Tap to Pay is a separate Application Type."** Rejected: same spine, same record, same receipt; only the acceptance substrate differs.
- **"Restaurant handhelds belong to this leaf."** Rejected as primary: their sale semantics (check/table lifecycle, coursing, tips) are Restaurant POS; the mobile surface is shared machinery.
- **"mPOS category size / analyst statistics."** Rejected as evidence: no analyst sources fetched; market-size claims would violate the evidence rule.

## Boundary Findings

### vs Retail Point of Sale (sibling leaf; joint review discharged here)

Shared: the entire sale spine (priced catalog → sale construction → in-person tender → completed transaction + receipt), the operator-facing model, permissions, and reversal flows. Different: **the sale surface and what it enables**. Retail POS's canonical surface is a staffed, purpose-built counter register (integrated peripherals, fixed location); Mobile POS's canonical surface is a portable device carried to the exchange, and the Type's context includes selling where no counter exists at all.

**判据 (remove/add test)**: take a Mobile POS and remove the portability requirement (replace the surface with a purpose-built fixed register) → you have Retail Point of Sale. Take a Retail POS and require the sale surface to be a portable seller-carried device → you have Mobile POS. The L0s are nested (Mobile POS = Retail POS spine + portability invariant).

**Joint-review decision (keep-both)**: the 2026-09-06 retail pass assessed both siblings as "likely Variants/Aliases." This pass ratifies keeping Mobile POS as a separately documented leaf, for three evidence-backed reasons: (1) a recognized market category exists — vendors define, name, and segment around "mobile POS / mPOS" (Shopify's own mPOS guide and POS-types FAQ; PayPal POS's "On-the-go" segmentation; SumUp's portable-first kit); (2) mobile-native products exist whose only surface is the portable one — for the no-premises merchant, the portable device is the entire POS, not a mode; (3) the surface class changes the user population, the hardware anatomy (reader pairing, paperless base, optional counter peripherals), and specific rules (device security, connectivity posture). The nesting is documented explicitly in both directions: this leaf cross-references Retail Point of Sale as the fixed-counter sibling, and the retail document's variant table already points here. **Residual risk recorded**: vendors do ship all three 05.10 forms as modes/editions of single products; if the atlas later merges surface-defined siblings, this pair (with Email Client/Webmail as precedent) is the canonical case. Omnichannel POS remains unprocessed and still flagged.

### vs Payment Processing Platform / Gateway / Terminal (08)

Remove the catalog and sale construction from a Mobile POS → a mobile card reader / amount-entry terminal (a real product class). Processing moves money (authorize/capture/settle/disputes); the Mobile POS composes the sale and orchestrates tender on top of processing (its own or external). Evidence: Square records tenders it never processed (cash, checks, custom payment methods); SumUp/PayPal bundle processing with the POS but the POS app remains the sale layer.

### vs E-commerce checkout / Mobile Commerce Application (05.01)

The Mobile POS sale runs on the **seller's** device, in person, at the exchange; e-commerce checkout runs on the **customer's** device, remotely. Remove in-person collection on a seller-carried surface → checkout/payment links territory.

### vs Restaurant POS (handhelds / tableside)

Tableside handhelds in restaurants execute a check-based sale lifecycle (open check across a service period, coursing, tips) — Restaurant POS workflows on a mobile surface. The boundary is sale semantics, not surface: the same vendor ships both semantics on the same mobile app family (Square POS modes; Loyverse dining options).

### vs Digital Wallet / Peer-to-peer Payment Application (08)

Consumer-side personal money movement vs seller-side business sale execution with catalog, records, and taxes. Remove the business sale machinery → wallet.

### vs SoftPOS / "Tap to Pay on phone" as a product category

Software-only acceptance is an acceptance substrate of this Type (and of Retail POS), not a separate Type: the sampled products treat Tap to Pay as a mode of the same POS app (Square enables it inside the POS app; Shopify/PayPal/SumUp the same).

---

## Uncertainties

1. **SumUp operational detail**: article bodies JS-blocked; capability inventory only. No SumUp-specific workflow claims asserted.
2. **PayPal POS (Zettle) operational detail**: help centre timed out; evidence at product-page level; sale-composition flows on the app not directly observed.
3. **Shopify Help Center**: 403 (prior pass, twice-confirmed, not retried); Shopify detail rests on the product page and the vendor's mPOS guide (both fetched successfully this pass).
4. **Clover mobile hardware**: not verified this pass (JS app/404); Clover used only for the shared-spine evidence from the prior pass's developer docs.
5. **Offline capability matrix**: which acceptance substrates support offline varies by product and was verified directly only for Square (reader-based offline mode exists; Tap to Pay requires connectivity). Generalized offline claims avoided.
6. **Cash handling depth on mobile**: verified narratively via Shopify's guide ("associate will need to bring them change") and Square's cash articles; per-product cash-management depth on mobile surfaces not exhaustively verified.

## Final Synthesis

A Mobile POS is the **portable expression of the in-person sale-execution application**: the same priced-catalog → sale → tender → recorded-transaction spine as its fixed-counter sibling, executed on a seller-carried device (phone, tablet, or handheld) with payment capture attached, paired, or built into the device — so the checkout can move to wherever the exchange happens, including places where no counter exists at all. The market recognizes this as a named category and builds products that are mobile-native rather than counter products with a mobile mode; the defining addition over Retail Point of Sale is precisely the portability of the sale surface, with everything else (catalog layer, tenders, receipts, reversals, permissions, inventory decrement, back office) inherited from the shared spine. Acceptance substrate (reader / software-only NFC / all-in-one terminal), selling context (micro-merchant kit, pop-up, line busting, tableside), and peripheral completeness are variant axes, not definitions.
