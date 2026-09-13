# Research Notes — Cashless Venue Platform

## Research Goal

Understand what a "Cashless Venue Platform" actually is as an Application Type: what objects it manages, how the guest spending loop works, what the operator administers, and where its boundary lies relative to attraction ticketing, POS, campus card programs, stored-value wallets, and event/festival platforms.

## Initial Boundary (hypothesis before research)

Working hypothesis: a venue-operated payment system that replaces cash and card-present payments inside a venue (theme/water park, FEC/arcade, festival, stadium, ski resort) with venue-bound guest accounts carried on tokens (RFID wristbands, cards, mobile app), charged at venue spend points.

Likely confusion set:

- Attraction Management System / Attraction Ticketing (admission is a different object)
- Retail / Restaurant POS (the spend point, not the account layer)
- Campus Card Management (structurally parallel institution credential program)
- Stored Value Wallet / Digital Wallet (general-purpose consumer wallets)
- Gift Card Management (stored value as retail instrument)
- Festival / Event Management (event production is a different center of gravity)

## Research Questions

1. What is the guest account object, and what form does the carried credential take?
2. How is value loaded (prepaid top-up vs linked payment card vs account-backed), and via which surfaces?
3. What is the charge flow at a spend point, and what spend-point types exist?
4. What happens to refunds, remaining balances, unspent value?
5. What venue-specific behaviors exist (parental control, dual currency credits/e-tickets, promotions, access bundling, offline resilience)?
6. What does the operator side administer (devices, pricing, reconciliation, settlement, multi-site)?
7. How do temporary (event) deployments differ from permanent venues?
8. Where is the boundary with Attraction Ticketing / AMS, POS, Campus Card, and consumer wallets?

## Representative Products

| Product | Segment | Philosophy | Evidence level |
|---|---|---|---|
| Semnox (Parafait / Tixera / Deliko) | Theme/water parks, FECs, F&B — park platform with cashless module | cashless as one module of an integrated park platform | A (product pages) |
| Embed | FECs / arcades / eatertainment | FEC-native integrated cashless hardware+software ecosystem ("EMBED ECOSYSTEM") | A (product pages, FAQ) |
| Intercard | Arcades/FECs, bowling, route operators, cruise ships, cinemas, midways | hardware-led amusement cashless veteran (since 1989), in-house HW+SW | A (product pages) |
| Connect&GO | Attractions: parks, water parks, zoos, museums | cloud Attraction Management System with cashless payments / virtual wallet as feature module | A (feature pages) |
| Intellitix | Festivals, conventions, sports events | RFID event platform: credential + wallet + access + settlement, merchant-of-record payments | A (product pages) |

Coverage check: different segments (parks / FEC / arcade-veteran / attractions-SaaS / events), different philosophies (platform-module vs FEC-native vs hardware-led vs AMS-feature vs event-platform), different scales (small arcades to 200k-attendee events; chain operators like Dave & Buster's / Bowlero appear as customers). §24 historical check: Intercard's "since 1989" positioning documents the pre-smartphone era (swipe cards at arcade games); Semnox documents non-RFID tag forms (barcode/QR) and physical token exchange (Embed kiosk takes old tokens for credits). The model below was checked against these older forms and holds.

## Sources

Fetched 2026-09-06:

- https://www.semnox.com/ (root; solution map)
- https://www.tixera.com/solution/cashless-management.html (Semnox cashless module)
- https://embedcard.com/ (root; ecosystem, FAQ)
- https://www.intercardinc.com/ (root; products/industries)
- https://www.intercardinc.com/software/ (Cutting Edge software)
- https://connectngo.com/ (root; feature map)
- https://connectngo.com/features/cashless-payments (cashless feature detail)
- https://intellitix.com/ (root; how-it-works)
- https://intellitix.com/payments (payments/settlement detail)

Unreachable (limitation): both Zendesk-hosted help centers tried (connectngosupport.zendesk.com, intellitixguest.zendesk.com) timed out ×1 each; embedcard.com root failed once (www variant succeeded). Consequence: guest-facing operational detail (exact refund windows, balance expiry rules, auto-top-up defaults, offline behavior specifics) could not be verified at help-center depth. No precise numeric/behavioral claims are made below where evidence is missing.

## Product Observations

### Semnox (Parafait / Tixera / Deliko)

Evidence layer A (official product pages).

- Cashless Management (Tixera): "Just one tag — available in RFID, Barcode, and QR Code — can be used for all transactions at any of the touchpoints — be it retail, lockers, rental, costumes, restaurant, food kiosks, or merchandise counters."
- Tag forms: plastic cards, ABS wristbands, key chains, tokens, stickers; brand-customizable.
- Acquisition/loading: "Purchase tags at different Point-of-sale – online, kiosks, or on-site counters. Recharge and play."
- Security posture: "non-transferable tags prevent unauthorized access… you eliminate fraud and pilferage" (vendor claim).
- RFID tags double for locker operation (Integrated Locker Management) and ride-based control readers exist as a separate module (deducting readers at rides).
- Parafait (FEC side): Wireless Debit Card Reader, RFID cards/wristbands, Inventory & Redemption Management (ticket redemption), Self-service kiosk, Mobile POS, 360 CRM, party bookings.
- Deliko (F&B): Cashless Prepaid Card Management module; cafeteria/canteen deployments (school/corporate cafeterias listed as industries).
- SemnoxPay listed as a payments surface; Reporting & Business Intelligence modules; "2800+ sites, 60+ countries" (vendor claim, L3).
- Observations: cashless is one module of a park platform; the credential spans payment + lockers + (optionally) admission/ride control; dual-use of one tag across touchpoint types is the headline structure.

### Embed

Evidence layer A (official product pages + FAQ).

- Positioning: "Cashless Arcade Payment System for Arcades, Attractions & Amusement"; integrated "EMBED ECOSYSTEM" of cashless payment solutions.
- Motivation framing: eliminate "problems caused by operating on tokens and tickets, such as high purchase costs for materials and additional maintenance costs for coin jams, labour, and operational downtimes" — documents the replaced incumbent (coins/tokens/paper tickets).
- Hardware: smartTOUCH arcade debit card reader (tap, swipe, or hybrid configurations); KIOSK+ self-service registration kiosks (card purchase, reloads, upsell features, package deals, "automatic reloading of game cards"); game cards & wearables on Playwave® contactless tech; "custom media are your FEC's currency—both means of payment and key to your loyalty programmes."
- Software (TOOLKIT): SALES, PRIZES (redemption), REPORTS, Mobile Wallet; Pro add-ons STATS, BOOKINGS, CGM (Central Games Management — "management of all games, pricing, and promotions in all locations, at a glance"), GURU (back-of-house: inventory, pricing, promotions, users, reader configurations).
- Mobile Wallet: "customers can easily pay and play from their phones without leaving the game" — Apple and Google certified (vendor claim).
- FAQ: supports "a hybrid system of physical and e-tickets"; kiosk "can take old tokens in exchange for credits"; multi-location real-time reports; "Check Card Balance" is a public guest surface.
- Unattended Payments is a distinct solution area (payments at unattended devices).
- Observations: FEC flavor — the account carries paid credits AND earned e-tickets/points; reader-on-every-game is the defining spend-point estate; central management across locations is first-class.

### Intercard

Evidence layer A (official product pages).

- Positioning: "World Leader In Cashless Technology"; "Leading the Way in Cashless Systems for the Amusement Industry since 1989" — documents the Type's pre-mobile era.
- Industries: FECs, bowling centers, route operators, cruise ships, cinemas, midways.
- Hardware: iReaders (all-in-one unit; "real time display of guest photo or avatar"); new iQReader "takes both play cards and credit cards… reads paper ticket or mobile device… built-in scanner to read QR codes… play games and collect points without a card. Send QR code to phone or printed receipt"; iTellers (self-service kiosks); POS & Redemption; Balance and Recycle Station (card handling/recycling).
- Software: Cutting Edge — "customized cloud-based systems support any size facility from one to one hundred locations"; Mobile iReader; Shindigger (mobile); E-commerce; The Edge Mobile App Collection; Online Waiver.
- Observations: account charging extends from staffed POS to unattended game readers; credential tech evolution visible in one catalog (play cards → credit cards → QR/phone, cardless play); cloud console for multi-site operators; e-commerce (remote loading) exists.

### Connect&GO

Evidence layer A (official feature pages).

- Platform: Attraction Management System for attraction & theme parks, water parks, recreational parks, zoos & aquariums, museums; cashless is one feature among many (POS, F&B POS, ticketing, access control, RFID, kiosks, e-commerce, photo & video, CRM, dynamic pricing).
- Cashless Payments / Virtual Wallet detail:
  - "Guests load money and spend it across your park, from snacks to souvenirs." — One Balance: "Guests can pay for food, retail, or ride tickets."
  - Easy Reload: "Guests can top up funds at kiosks, counters or online" (also "reload… right from their phone, a nearby kiosk, or with your staff" mid-visit).
  - Parental control: "Kids don't need cash, and parents stay in control"; "Parents can preload funds and assign them to each kid."
  - Faster payments: "Guests tap using wristbands or phones."
  - Refunds: "Easy Refunds: Transaction history make it easy to track."
  - Promotions: bundled offers ("Add '$20 in Fun Cash' to a ticket"), load bonuses ("Get 10% on food when you buy Fun Cash").
  - Open loop: "Add a credit card so guests can keep paying" — card-linked spend beyond the preloaded balance.
- Water parks: "RFID wristbands that unlock seamless access and cashless payments" — same credential for admission and wallet.
- Vendor claim: "increase your average sales revenue by 25% or more" (L3, not generalized).
- Observations: clearest articulation of the guest wallet model (one balance, multi-surface reload, parental allocation, open-loop fallback); cashless embedded in a multi-module AMS.

### Intellitix

Evidence layer A (official product pages).

- Positioning: RFID-powered event technology platform since 2010; 2,000+ events (vendor claim); festivals, conventions, sports.
- Flow ("Three Steps"): 1) Configure your event — connect ticketing platform, configure "event zones, credential types, and vendor setup through our portal"; 2) Deploy RFID credentials — "wristbands or badges through pre-event fulfillment or on-site distribution, linking each credential to a digital wallet and attendee profile"; 3) Go live with real-time dashboards (entry flow, vendor performance, per-head spending).
- Post-event: "detailed settlement reports and exportable analytics."
- Payments: organizer as "merchant of record… You own the funds, the timeline, and the data"; accepts "cards, Apple Pay, Google Pay, RFID taps"; multi-vendor settlement "broken down automatically"; revenue split by vendor, zone, payment method; PCI-compliant fraud detection.
- Guests: account portal (my.intellitix.com) + guest support center (unreachable).
- Observations: the event variant — credential distribution is a logistics operation (fulfillment), wallet is tied to an attendee profile, and the settlement/set-up/tear-down cycle is event-bounded; merchant-of-record structure means funds flow through the organizer.

## Cross-product Comparison

| Dimension | Semnox | Embed | Intercard | Connect&GO | Intellitix |
|---|---|---|---|---|---|
| Venue-scoped guest spending account | yes (tag wallet) | yes (game card credits) | yes (play card account) | yes (Virtual Wallet, one balance) | yes (digital wallet per credential) |
| Carried credential | RFID / barcode / QR tags: cards, wristbands, key chains, tokens, stickers | contactless game cards & wearables (Playwave) + phone wallet | play cards; newer readers accept credit cards/QR/phone | RFID wristbands + phones | RFID wristbands/badges |
| Spend points | retail, lockers, rental, costumes, restaurant, food kiosks, merchandise; ride-based readers | arcade game readers, POS, unattended | game readers, POS & redemption, kiosks | food, retail, ride tickets (via POS/F&B POS) | vendor booths (ITX POS) |
| Loading surfaces | online, kiosks, on-site counters | kiosks (purchase/reload), e-commerce, mobile wallet | iTellers kiosks, e-commerce, apps | online, kiosks, counters, phone | pre-event fulfillment, on-site, account portal |
| Parental/allocated spending | not explicit in fetched pages | not explicit in fetched pages | not explicit in fetched pages | explicit (parents preload and assign per kid) | not explicit in fetched pages |
| Dual currency (paid credits + earned tickets/points) | redemption management module | PRIZES + e-tickets hybrid | "collect points without a card" | ride tickets as spendable item (single-balance emphasis) | not observed |
| Promotions / bundled value | real-time promotions claimed | package deals, upsell at kiosk | reward options | fun-cash bundles, load bonuses | vendor setup includes pricing (implied) |
| Open-loop / card-linked | not observed | iQReader-class readers take credit cards (Intercard) — for Embed not explicit in fetched pages | explicit (readers take play cards AND credit cards) | explicit ("add a credit card so guests can keep paying") | explicit (cards, Apple/Google Pay accepted) |
| Access control on same credential | yes (entry validation, ride control, lockers) | not emphasized in fetched pages | not emphasized | yes (RFID access + payments) | yes (gate taps + payments) |
| Operator admin | reporting/BI; module config | TOOLKIT/GURU/CGM (devices, pricing, promotions, users, readers) | Cutting Edge cloud (1–100 locations) | AMS feature suite + reporting | portal: zones, credential types, vendors |
| Multi-site/central | 2800+ sites claim | CGM across all locations | cloud 1–100 locations | single-platform, multi-venue industries | per-event + portfolio |
| Settlement/refund machinery | refunds implied via transaction records | token exchange for credits at kiosk | balance & recycle station | easy refunds via transaction history | post-event settlement reports, multi-vendor split |
| Deployment | permanent venues (+cafeterias) | permanent venues | permanent venues (+midways/mobile) | permanent venues | temporary events (fulfillment, settlement cycle) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The smallest structure without which the product stops being a Cashless Venue Platform:

1. **Venue-scoped guest spending account** — an account held on the venue's platform whose purpose is paying for things inside that venue's ecosystem (not a general-purpose wallet).
2. **Guest-carried credential bound to the account** — a physical or virtual token (wristband, card, phone, QR) that presents the account at the moment of purchase.
3. **Charging at venue-operated spend points** — staffed or unattended points of sale that deduct from the account at purchase time, without cash or card-present payment.
4. **Funding path** — a way value enters the account (prepaid top-up and/or linked payment method), with the resulting balance and transactions recorded.

Remove the venue-scoped account → the product is payment processing / POS. Remove the spend points → it is a consumer wallet. Remove the charging loop (credential becomes identity-only) → it is access control. Remove the venue operator (self-service only) → it is a stored-value wallet app. Each removal lands in a different Application Type.

### L1 — Common Mature Structure

Very common across the sample, but not required to recognize the Type:

- Self-service loading surfaces: top-up kiosks, online/e-commerce, mobile app (Semnox, Embed, Intercard, C&G; Intellitix via fulfillment + portal)
- Unattended spend points with readers on devices (games, lockers, ride control) — Semnox, Embed, Intercard
- Guest-facing balance visibility (check-balance surface, reader displays, apps)
- Operator administration: device/reader configuration, pricing and promotions management, user administration (Embed GURU/CGM, Intercard Cutting Edge, C&G AMS, Intellitix portal, Semnox modules)
- Reporting & reconciliation; multi-location/central management for chains (Embed, Intercard, Semnox)
- Promotions and bundled value (load bonuses, packages tied to admission) — Semnox, Embed, C&G
- Refund handling supported by transaction history (C&G explicit; others implied by records + service desks)
- Loyalty tie-in on the same credential (Embed explicit; industry-common)
- Access/entry integration on the same credential (Semnox, C&G, Intellitix) — extremely common in parks/events but bundled rather than defining
- Ancillary device integration: lockers, rentals (Semnox; C&G cabanas via maps/reservations)

### L2 — Variant / Optional Structure

Depends on segment, era, geography, business model:

- Funding model: closed-loop prepaid (top-up) vs open-loop card-linked vs folio-backed (cruise-ship accounts listed by Intercard) — genuinely different economic structures of the same loop
- Credential technology generation: magstripe (era), barcode/QR, RFID/NFC, mobile wallet, cardless QR-to-phone (Intercard iQReader)
- Identity posture: anonymous bearer credential vs registered attendee profile (Intellitix links wallet to profile; C&G ties CRM)
- Permanent venue vs temporary event deployment: event variants add credential fulfillment/distribution, event-bounded expiry and refund windows, post-event settlement and tear-down (Intellitix)
- Dual-currency amusement flavor: paid credits + earned e-tickets/points redeemable for prizes (Embed, Intercard, Semnox redemption) — segment-shaped
- Merchant-of-record / settlement structure: operator-settled vs platform-mediated multi-vendor settlement (Intellitix)
- Parental allocation of child spending (C&G explicit; family venues generally)
- Cafeteria/canteen deployments (Semnox Deliko) — same loop, institutional feeding context

### L3 — Vendor-specific (kept out of the final document)

- Semnox: Parafait/Tixera/Deliko brand split; SemnoxPay; tag form factors list; "non-transferable" claim; ride-based control readers as named module
- Embed: Playwave®, smartTOUCH/KIOSK+/TOOLKIT/SALES/PRIZES/GURU/CGM/STATS/BOOKINGS naming; Apple/Google certification claim; token-exchange kiosk; 27" screen; 1000+ customers / 3000+ installations / 59+ countries claims
- Intercard: iReader/iTeller/iQReader/Shindigger/Balance & Recycle Station/Cutting Edge/Edge apps naming; guest photo/avatar display; "since 1989"; "no fees for updates"; 1–100 locations claim; industry list incl. cruise ships, cinemas, midways
- Connect&GO: Attraction Management System naming; Virtual Wallet / Smart Access Control / Interactive Maps / Photo & Video feature names; "25% revenue" claim; under-200k-admissions segmentation
- Intellitix: ITX POS / Intellitix Payments naming; pre-event fulfillment service; merchant-of-record positioning; festival/convention/sports packaging

## Vendor-specific vs Type findings

- "Cashless as a module of a wider venue platform" (Semnox Tixera, Connect&GO) vs "cashless as the product itself" (Embed, Intercard) vs "cashless+access as the event platform" (Intellitix) are packaging postures over the same underlying loop — not different Types.
- Reader hardware (card readers on games) is a spend-point implementation, not the Type's definition: the defining layer is the account + credential + charging, regardless of device.
- The credit-card acceptance seen in newer readers/products shows the Type is currently absorbing open-loop payments — treat card-linking as a funding variant (L2), not a redefinition.

## Boundary Findings

1. **vs Attraction Management System / Attraction Ticketing** (sibling, processed): AMS defines admission products, entry validation, attendance. The cashless platform defines the guest spending loop. The same credential often carries both, and AMS products bundle cashless modules — but remove the spending account + charging and an AMS remains ticketing; an arcade-only or vendor-booth-only cashless deployment has no admission at all. Boundary holds; the processed attraction-management-system entry correctly records cashless wristbands as its optional (L2) layer.
2. **vs Retail POS / Restaurant POS** (siblings, retail-point-of-sale processed): POS is a spend point. The cashless venue platform is the account/funding/credential layer above spend points; it can drive POS devices but its defining object is not the sale — it is the venue-scoped guest account. Some FEC products ship their own POS, which is bundling, not Type confusion.
3. **vs Campus Card Management** (sibling, processed): structurally parallel loop (issued credential + service points + accounts + central lifecycle), but campus card's center of gravity is institution identity + entitlements (access, meal plans, SIS integration) in education; the venue platform's center of gravity is commercial in-venue spending in entertainment/hospitality. Adjacent, not the same Type. Flag for joint review in case the directory later wants a shared "credential spending program" abstraction.
4. **vs Stored Value Wallet / Digital Wallet (§08)**: consumer wallets are general-purpose, user-owned, usable anywhere the scheme is accepted; the venue wallet is venue-scoped, venue-administered, often closed-loop, with venue-specific promotions and controls. Open-loop card-linking blurs the edge but venue-bound administration remains the discriminator.
5. **vs Gift Card Management / Store Credit (§05.15)**: gift cards are value instruments sold by retailers; the venue platform operates an estate of credentials, spend points, loading surfaces, and settlement. A gift/store-credit module can exist inside it.
6. **vs Festival Management / Event Ticketing (siblings)**: festivals bundle RFID cashless; but festival management's object is the event program (lineup, scheduling, production). The cashless platform's objects are credentials, wallets, transactions, settlements.
7. **Type verdict**: the leaf is a legitimate standalone Type. Products named "cashless system/platform" (Embed, Intercard) exist whose entire product is this loop; the historical line (tokens/coins/paper tickets → swipe cards → RFID → mobile/cardless QR) is documented within the sample.

## Uncertainties

- Guest-facing policy detail (exact refund windows, balance expiry, lost-credential procedures, auto-top-up defaults) lives in help centers that were unreachable (Zendesk timeouts). No precise numbers asserted anywhere.
- Offline operation of readers under venue network conditions: commonly emphasized in this industry, but not directly evidenced in fetched pages — kept qualitative.
- Parental controls: only Connect&GO explicitly documents allocation of funds to children among the fetched pages; phrased as common in family venues, not universal.
- Auto-recharge (automatic reload from a card on file): not verified in any fetched page — not asserted.
- Intercard cruise-ship deployments suggest folio-backed accounts (post-paid); not confirmed at help-center depth — kept as variant hypothesis.
- Semnox/Embed/Intercard revenue-uplift claims are vendor marketing — excluded from the final document.

## Final Synthesis

A Cashless Venue Platform is a venue-operated payment system organized around a venue-scoped guest spending account, presented at the moment of purchase by a guest-carried credential (wristband, card, phone, QR), charged at the venue's staffed and unattended spend points, funded by top-up or card-link, and administered by the venue operator (devices, pricing, promotions, reconciliation, settlement, multi-site). Standard capabilities: self-service loading (kiosks/online/app), balance visibility, promotions and bundled value, refunds supported by transaction history, loyalty, access-control integration on the same credential, and (in amusement segments) a dual currency of paid credits plus earned e-tickets/points. Variants: closed-loop prepaid vs open-loop card-linked vs folio-backed funding; anonymous bearer vs registered-profile credentials; permanent venue vs temporary event deployment (fulfillment, expiry, post-event settlement); campus-card-style institutional deployments form a structurally parallel sibling rather than the same Type.
