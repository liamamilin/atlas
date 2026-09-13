# Research Notes — Event Ticketing Platform

## Research Goal

Understand what an Event Ticketing Platform is as an Application Type: what objects exist inside it (event, ticket type, order, ticket), what the organizer does with them, how the sell → issue → validate loop works, where money/seats/marketplace/resale sit (definitional vs common vs variant), and where the Type's boundary sits — above all against Event Registration Platform (the flagged boundary counterparty from that pass), Event Management Platform, Attraction Ticketing / Attraction Management System, Attendee Management, and the three unprocessed §26 siblings (Reserved Seating Platform, Ticket Inventory Management, Ticket Resale Marketplace).

## Initial Boundary

Working hypothesis before research:

- Core use: organizer-side software whose center is selling tickets to events — the organizer defines ticketed events with priced ticket inventory, the platform sells them (own channels and/or a consumer marketplace), each sale issues tickets as access entitlements, and the organizer manages the resulting sales (orders, refunds, reporting, entry).
- Primary users: event organizers/promoters/venues (concerts, performing arts, festivals, clubs, fairs, sports); ticket buyers are the consumer-facing side.
- Nearest neighbors: Event Registration Platform (registrant-record center — flagged as boundary counterparty), Event Management Platform (whole-lifecycle center, processed), Attraction Ticketing / Attraction Management System (place-admission inventory, processed), Attendee Management (roster center, processed), Reserved Seating Platform (seat-map center, unprocessed), Ticket Inventory Management (allocation machinery center, unprocessed), Ticket Resale Marketplace (secondary market, unprocessed), E-commerce Platform (generic product commerce), Airline Reservation/PSS (processed — that pass already noted the seam), Restaurant Reservation Platform (table-inventory booking), Convention/Exhibition Management (participation monetization, processed), Cashless Venue Platform (spending accounts, processed).
- Known unknowns: is payment definitional (free ticketed events exist)? Is entry validation definitional or standard? Is the seat map definitional (GA events have none)? Is the consumer marketplace definitional (self-serve no-marketplace products exist)? Where does ticketing end and registration begin — exactly?

## Research Questions

1. What is the central object — the event, the ticket type, the ticket, or the order?
2. What does the sell loop look like end-to-end (define event → define ticket types → on-sale → purchase → payment → ticket issuance → delivery → entry validation → reporting)?
3. Is the ticket-as-artifact (a distinct, checkable entitlement) definitional, or is it just a receipt?
4. Is payment definitional? What direct evidence exists for free ticketed events and deferred-payment sales?
5. How is ticket inventory modeled (ticket types, quantities, sections, price bands, holds, allocations)?
6. How do reserved seating and general admission coexist? Is the seat map definitional?
7. What sales channels exist (web, box office/door, mobile app, agents/resellers, marketplace)?
8. What happens at entry (scanning, check-in windows, scan history, door sales)?
9. What post-sale operations exist (refunds, exchanges, transfers, resale, order editing)?
10. Which poles exist (self-serve marketplace, self-serve no-marketplace, box-office/arts platform, full-service agency, dominant primary+marketplace)?
11. Historical check: do box-office-era and paper-ticket practices fit the proposed core?
12. Where exactly are the boundaries vs registration, EMP, attraction ticketing, and the three unprocessed ticket siblings?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer tiers:

| Product | Pole | Tier | Evidence quality |
|---|---|---|---|
| Eventbrite | self-serve organizer ticketing + consumer marketplace discovery | SMB/creator → mid (music, nightlife, food/drink, performing arts, community) | Tier 1 help-center articles directly fetched (ticket types, registration-only mode, check-in app) + Tier 2 product/pricing pages (Layer A) |
| Purplepass | self-serve ticketing, own-channel distribution (no consumer marketplace) | SMB/mid promoters (concerts, festivals, fairs, performing arts, sports) | Tier 1/2: learn/feature pages + Zendesk help-center structure directly fetched (Layer A) |
| Spektrix | arts & culture box-office ticketing platform (venue operations) | mid → enterprise venues (theaters, arts centers, museums) | Tier 1 support-centre categories + deep articles directly fetched (Events/Instances, Orders/Transactions, hardware/scanning) (Layer A) |
| Ticketmaster | dominant large-scale primary ticketing + official resale marketplace | large venues/promoters/tours (concerts, sports leagues) | Tier 2: main site + fan help center directly fetched; organizer-side tooling NOT publicly documented (Layer A consumer-side, limitation recorded) |

Abandoned samples (network rule): Ticket Tailor (flat-fee self-serve pole — help.tickettailor.com and www.tickettailor.com both 403 twice); ShowClix (full-service agency pole — www.showclix.com and support.showclix.com both 403 twice). The flat-fee and full-service poles are therefore evidenced only indirectly (Spektrix covers box-office operations; Eventbrite/Purplepass cover self-serve).

## Sources

- Eventbrite — Help Center topic "Creating an event": https://www.eventbrite.com/help/en-us/topics/creating-an-event/ ; article "Create and edit ticket types": https://www.eventbrite.com/help/en-us/articles/644100/how-to-create-custom-ticket-types/ ; article "How to set up an event that doesn't require PDF tickets (registration only)": https://www.eventbrite.com/help/en-us/articles/250995/how-to-set-up-an-event-that-doesn-t-require-tickets-registration-only/ (all fetched 2026-09-07)
- Eventbrite — Organizer overview: https://www.eventbrite.com/organizer/overview/ ; Sell Tickets feature page: https://www.eventbrite.com/organizer/features/sell-tickets/ ; Organizer Check-In App page: https://www.eventbrite.com/organizer/features/organizer-check-in-app/ ; Pricing page: https://www.eventbrite.com/organizer/pricing/ (fetched 2026-09-07)
- Purplepass — Learn/features hub: https://www.purplepass.com/learn/ ; Event Types: https://www.purplepass.com/learn/event-types/ ; Ticket Types: https://www.purplepass.com/learn/ticket-types/ ; Support hub: https://support.purplepass.com/ ; Help Center organizer category: https://help.purplepass.com/hc/en-us/categories/21570562726807-Event-Organizer ; Creating and Editing Events section: https://help.purplepass.com/hc/en-us/sections/21571110382103-Creating-and-Editing-Events ; Managing Orders section: https://help.purplepass.com/hc/en-us/sections/21571144911511-Managing-Orders (fetched 2026-09-07)
- Spektrix — Support Centre home: https://support.spektrix.com/hc/en-gb ; category "Set up Events, Offers, Subscriptions and Merchandise": https://support.spektrix.com/hc/en-us/categories/4411241161489 ; article "Introduction to Events and Instances": https://support.spektrix.com/hc/en-us/articles/11012056320541 ; category "Sell items and fulfill Orders": https://support.spektrix.com/hc/en-us/categories/4411255920913 ; article "Introduction to Orders and Transactions": https://support.spektrix.com/hc/en-us/articles/360018263917 ; category "Set up and troubleshoot hardware": https://support.spektrix.com/hc/en-us/categories/4411241248145 (fetched 2026-09-07)
- Ticketmaster — main site: https://www.ticketmaster.com/ ; Help Center: https://help.ticketmaster.com/hc/en-us (fetched 2026-09-07; fan-facing help + business contact link; organizer-side tooling not publicly reachable)
- Sibling docs consulted for boundary alignment: research/event-registration-platform.md (boundary counterparty), research/event-management-platform.md, research/attraction-ticketing.md, research/attraction-management-system.md, research/attendee-management.md, research/convention-exhibition-management.md, research/cashless-venue-platform.md, research/event-credential-badge-management.md, research/airline-reservation-passenger-service-system.md, STATUS.md boundary entries

Source-access limitations:

- Ticket Tailor (flat-fee self-serve pole) and ShowClix (full-service agency pole) unreachable (403 ×2 each, abandoned per network rule). No claims are made about those products; the poles they represent are covered structurally by the sampled products (Spektrix for box-office operations; Eventbrite/Purplepass for self-serve).
- Ticketmaster's organizer/promoter-side tooling is not publicly documented; evidence is consumer-side help + the "Ticket Your Event" business contact link. Organizer-side claims about Ticketmaster are kept minimal and marked as such.
- AXS, Dice, Etix, See Tickets, Universe were not fetched; their existence as market participants is evidenced only via Eventbrite's own comparison table (a vendor marketing claim) and Ticketmaster's network-brand footer — treated as market-structure context, not product evidence.
- All sampled products are US/UK-market. Regional ticketing products were not sampled; claims are kept implementation-neutral accordingly.

## Product Observations

### Eventbrite — evidence layer A (Tier 1 help center + Tier 2 product pages)

- Self-label: "all-in-one ticketing and discovery platform"; "the world's largest events marketplace" (marketing claim, recorded as such).
- Event setup (help topic "Creating an event"): create event, change date/time, capacity, reserved seating management, privacy settings, event status management, scheduled publish, cancel, unpublish/delete, postpone/reschedule, single event with multiple dates/times, recurring/timed-entry events (dedicated "new recurring event experience" with dates and time slots), online-only and hybrid events.
- Ticket types (help article, Tier 1): three kinds — **Paid**, **Free**, **Donation**. Settings: name; section (sections have their own capacity; total event capacity = sum of sections); quantity; price with **Dynamic** option (automatic price changes by date or by number sold); **absorb fees** toggle (default: attendees pay fees); sales availability windows (date/time, or chained "when sales end for…" another ticket type); advanced: description, visibility (visible / hidden / hidden-when-not-on-sale; hidden tickets revealed by promo code), tickets-per-order min/max, **sales channel** (online vs **at the door only** via Organizer app), **ticket delivery options** (eTicket via app vs **Will Call** printed for pickup), **check-in time** windows per ticket type.
- Holds: "Create and manage holds" article exists (holds as a first-class ticketing concept).
- Ticket lifecycle rules: cannot delete a ticket type after any sales (even cancelled/refunded); pricing/name edits apply to future sales only; copy tickets (types, add-ons, promo codes, holds) from another event.
- Registration-only mode (Tier 1, boundary-critical): "Registration event" is a **named event type** under Tickets → Settings; free events are registration-only **by default and cannot be changed**; paid events can be switched; PDF tickets can be disabled ("Include printable tickets in all orders" checkbox) so no ticket artifact is issued.
- Order options: order form (collect info from all attendees), custom questions, registration time limit, custom order confirmations, waivers with registration, add-ons (merchandise/extras), guest lists.
- Payments (pricing page, Tier 2): free events free; paid tickets carry a per-ticket service fee + per-order payment-processing fee (exact percentages observed on the page but plan/region-dependent — kept in research notes); organizer can absorb fees; **scheduled payouts** (pre-event payout schedules); waitlists; refunds (buyer-side article: refunds requested from organizer).
- Check-in (Tier 2 feature page): Organizer app scans QR codes on tickets, verifies registrations instantly, "helps prevent ticket fraud at the door", on-site ticket and merchandise sales with payment processing, real-time attendance/sales data.
- Marketing/marketplace: Eventbrite Ads, email marketing, promo codes, attendee discovery recommendations; vendor claims (90M buyers, 30% of paid tickets driven by marketplace) recorded as vendor claims only.
- Roles: 'Manage tickets' permission; organization team management.

### Purplepass — evidence layer A (learn pages + help-center structure)

- Self-label: "event ticketing platform and management hub"; distribution is via the organizer's own event pages/widgets (no consumer marketplace claimed).
- Event types (learn page): one-day; **multi-day** (one event page spanning days); **paid** (credit card, cash, check, gift card, vouchers, COMP; fee control — "customers will pay all fees" by default, organizer can absorb or split); **recurring** (every Friday / 1st of month / custom schedule; "ideal for theater productions… different show times for a production"); **reservations mode** (guests request GA or assigned-seating tickets but **pay at the event** — mail a check, cash later, or charge to an account); **free events** (RSVP-style; no service fees; guests still select tickets and enter information).
- Ticket types (learn page): standard GA→VIP; **custom ticket types** (organizer-defined name/price/deals); **assigned seating** (venue maps with custom charts, images, legends, logos, stage photos from seats, handicap/wheelchair icons); **season passes** (guests select events/dates/seats in advance) and **group/flex passes** (blocks of tickets at a discount); **donations** (campaigns, tiers, minimums); **non-inventoried items** (merchandise, drink tickets, VIP upgrades — do not count toward venue capacity); **live stream tickets** (widget embedded on the organizer's website).
- Promo codes (own learn page).
- Help-center organizer sections (Tier 1 structure): Account Settings; **Assigned Seating**; Creating and Editing Events (Getting Started; Different Event Types — one-time / multi-performance series / recurring; Merchandise & Upgrades (Non-Inventory); Options & Event Settings; **Ticket Creation & Management — COMP tickets, VIP access passes, custom ticket types**; Artwork & Media; Checkout Questions — surveys/polls/file uploads); **Equipment**; **Managing Orders** (Refunds; Selling Tickets from dashboard; Ticket Order Management — edit delivery options etc.); **Passes & Packages**; **Payment and Fees**; **Printed Material**; **Reporting and Stats**; Tools and Integrations.
- Equipment/printed material sections imply scanner hardware and printed ticket stock support (section titles only — contents not fetched).

### Spektrix — evidence layer A (Tier 1 support centre, deep)

- Self-positioning: ticketing platform for arts & culture organizations (theaters, arts centers, museums); box-office operations at the center.
- Core model (Tier 1 article "Introduction to Events and Instances"): **Event** = the unique experience ("run", "show", "production"; also workshops, classes, gallery entry) with name/description/financial target/seat target; **Instance** = a dated occurrence (date + time) holding the sellable ticket configuration: capacity, reserved vs general admission, prices (by demographics, seat location, other factors), when/where tickets can be bought and how they are delivered. **Tickets are sold at the Instance level.** Events can have one or many instances; instances within an event can differ (access services, matinee pricing, members-only phone sales, linked post-show dinner). **Supplementary Events** are linked upsell events (e.g., post-show dinner) with separate capacity/pricing, suggested only to buyers of the linked instance.
- Seating plans (Tier 1): **Reserved** (visual seat map, one or more Areas), **Unreserved** (no map; customer picks quantity), **Multi-area** (mix). **Overlays** per instance: Layout Overlay (hide seats), Price Band Overlay (assign pricing level per seat; colors on reserved plans), Lock Overlay (**locks = holds/kills** on specific seats), plus seat attributes, view-from-seat, info overlay, best-available overlay.
- Tickets & pricing (Tier 1): **Ticket Types** = categories for tickets (often audience demographics; can determine sales channels and delivery methods); **Price Bands** = pricing-level groupings (visual on reserved plans); **Price List** = per-instance matrix of Ticket Type × Price Band whose intersection is the ticket's base price (taxes in; fees/commissions/donations out). Commissions: ticket (per-ticket fees), delivery, transaction commissions; levies. VAT (UK/IE) and US/CA tax handling.
- Subscriptions & series (Tier 1): **Ticket Subscriptions** (prepay for vouchers, redeem later); **Fixed Series** (buy tickets and hold seat rights across a series of instances); memberships sold alongside.
- Offers (Tier 1): multibuy, X-for-Y, package offers, promotion codes, offer priority groups.
- Selling (Tier 1 category "Sell items and fulfill Orders"): Sales Interface for box-office staff; sales channels (**Phone, Counter, Counter Quick, Web**); searching events/instances/customers; **reservations and deposits** (with proforma invoices for e.g. school group bookings); **door sales**; **group booking mode**; selling merchandise; **gift vouchers** (sell/search/redeem/refund); soft crediting orders; facilitated orders.
- Orders & transactions (Tier 1 article): a **Transaction** records a Sale, Return, or Reservation — items (Tickets, Memberships, Subscriptions, Donations, Merchandise, Gift Vouchers), payments (cash/card; **custom payment types** such as cheque, BACS, invoice), commissions, transaction date, **accounting date**, user (Web/API/Agent), sales channel. An **Order** is a container of transactions under a unique order number (e.g., sale + return; reservation → returned reservation → sale); order details include customer, attributes, questionnaire answers; order items show delivery method, price, commission, **seat location, seat number/row, barcode**, and **printed/scanned state with scan history**; **restricted orders** (permission-gated visibility, e.g., large private donations); order merging; group/ungroup tickets.
- Returns & exchanges (Tier 1): return and refund, bulk returns/refunds, refund to account credit, exchanges, returns reporting.
- Hardware & scanning (Tier 1 category): ticket printers (BOCA, Stimare, Microcom, Practical Automation), **scanning interface** ("How to Scan Tickets", "Scanning and Validating Customers in the Scanning Interface", **"Selling Zero Value Tickets in the Scanning Interface"** — door sales at entry, "Troubleshooting Ticket Scanning"), scanners (Zebra, Saveo, Janam), PIN pads/chip readers, Box Office App.
- Wider ring: reporting (standard/custom reports, accounting dates), customer records/lists/tags, email campaigns/mailings, donations/gift aid/memberships, agents selling on the organization's behalf, website integration (iframes/APIs).

### Ticketmaster — evidence layer A consumer-side (Tier 2; organizer side not publicly documented)

- Self-positioning: "Buy Verified Tickets for Concerts, Sports, Theater and Events"; "Official Ticket Marketplace" of the NBA, NHL, MLS (and MLB guide) — primary ticketing plus a branded fan resale marketplace.
- Consumer marketplace: discovery by category/city; event pages per dated occurrence; artist/tour pages with show charts.
- On-sale mechanics (fan help, Tier 2): **presales** (artist presale with signup, sponsor/cardmember presales, fan-club presales), **ticket limits** per purchase with enforcement ("we reserve the right to cancel your orders… if you try to exceed the posted ticket limits"), **queues/waiting rooms** before sales open.
- Mobile entry (fan help): "your phone is your ticket"; scannable ticket made available close to the event (estimated ~48h before, per help pages); add to mobile wallet; some events hide barcodes entirely (wallet-only).
- **Ticket Transfer**: transfer tickets to others from the order; some elements (merchandise, VIP package elements, fan-club memberships, ticket insurance) are non-transferable.
- **Face Value Exchange**: organizer-selected resale restriction — tickets non-transferable, resale only on Ticketmaster at face value; state-law variations noted (some US states prevent resale restrictions; Ticketmaster still honors terms on its site).
- Fan resale: "Sell on Ticketmaster" (listed tickets into the marketplace).
- VIP packages, accessible tickets (venue-controlled), ticket insurance, gift cards, hotels cross-sell.
- Organizer side: "Ticket Your Event" business contact link; business-solutions pages; **no public operational documentation of promoter/venue tooling** — limitation recorded; no organizer-side claims asserted.
- Network brands in footer: Live Nation, House of Blues, Front Gate Tickets, TicketWeb, Universe — family structure recorded as market-structure context.

## Cross-product Comparison

| Dimension | Eventbrite | Purplepass | Spektrix | Ticketmaster |
|---|---|---|---|---|
| Central sellable unit | event (single/multi-date/recurring/timed-entry) with ticket types | event (one-time/multi-day/series/recurring) with ticket types | Event + **Instance** (tickets sold at instance level) | event/show per date (tour charts) |
| Ticket definition | paid/free/donation; name, quantity, price, sales windows, visibility, per-order limits, channel, delivery, check-in window | standard/custom; GA→VIP; COMP; non-inventoried; live-stream; donations | ticket type × price band via per-instance **price list**; commissions/levies | organizer-defined; presale windows; ticket limits |
| Seat maps | reserved seating as a feature (separate product page) | assigned seating with venue maps | reserved/unreserved/multi-area plans + overlays (layout/price band/locks) | seat maps at scale (consumer-side evidence) |
| Holds/reservations | holds article; registration time limit | reservations mode (pay at event) | reservations + deposits + proforma invoices; locks/holds/kills | presales + queues (demand-side) |
| Payment | integrated processing; absorb/pass fees; scheduled payouts; refunds | card/cash/check/gift card/voucher/COMP; fee split control; reservations defer payment | cash/card + custom payment types (cheque/BACS/invoice); commissions; refunds/exchanges/account credit | integrated; resale payouts (fan side) |
| Ticket artifact | eTicket (app) / Will Call (printed); PDF toggle; QR scan | printed/thermal; mobile; QR (implied by equipment) | printed tickets (thermal printers), barcodes, printed/scanned state, scan history | mobile wallet / QR; barcode release window |
| Entry validation | Organizer app scan, fraud prevention, check-in windows | equipment section (scanners) | scanning interface; validate customers; zero-value door sales; scan history | venue entry with mobile tickets (consumer-side) |
| Door/box-office sales | at-the-door channel via Organizer app | dashboard selling; box office fees | full box-office sales interface (phone/counter/web channels) | box office (venue-side, not documented) |
| Distribution | own pages + consumer marketplace discovery | own pages/widgets only | own website integration + agents selling on behalf | consumer marketplace + official resale |
| Resale/transfer | transfer tickets (buyer-side article) | — (not observed) | exchanges (box-office mediated) | Ticket Transfer; Face Value Exchange; fan resale |
| Reporting | real-time sales/attendance analytics | reporting & stats section | standard/custom reports, accounting dates | (not documented organizer-side) |
| Roles | team management, 'Manage tickets' permission | account settings (roles implied) | user accounts with permission-gated restricted orders | (not documented) |

Convergent observations (candidate common structure):

1. All four define **ticketed events with ticket types** — priced (or zero-priced) admission options with quantities, sold against dated occurrences. (B)
2. All four produce **recorded orders** from sales, which the organizer can search, inspect, refund, and report on. (B)
3. All four issue **tickets as distinct artifacts** — electronic or printed, carrying a scannable/checkable identity (QR/barcode) — distinct from the order confirmation. (B; Eventbrite's registration-only mode proves the artifact is optional *within one product*, which makes it a capability boundary, not a universal invariant — see Boundary Findings.)
4. All four support **entry validation** in some form (scan apps, scanners, scanning interface). (B)
5. All four support **on-site/door selling** alongside online sales. (B)
6. All four handle **refunds** as an organizer-side operation. (B)
7. Pricing machinery beyond a flat price (tiers, promo codes, early bird, dynamic/automatic price changes, price bands) is present in all four but shaped very differently. (B, shape varies)
8. Capacity control (event/section/instance caps, holds) is present in all four. (B)
9. The consumer marketplace/discovery layer exists in two of four (Eventbrite, Ticketmaster) and is absent in two (Purplepass, Spektrix — distribution via own channels/agents). (B — variant, not definitional)
10. Reserved seating exists in all four but as a *mode*, with general admission equally first-class. (B — variant, not definitional)
11. Box-office staffed selling (counter channels, reservations/deposits, group bookings, printing hardware) is deep in Spektrix, present in Eventbrite/Purplepass in lighter forms. (B — depth varies by segment)

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three properties. If any one is removed, the product is no longer recognizable as an Event Ticketing Platform:

1. **The ticketed event as sellable inventory.** The organizer defines, inside the system, dated event occurrences with ticket types — admission options carrying a price (which may be zero) and a quantity — and the system tracks availability against sales. Remove it → generic e-commerce (undated products, no admission semantics) or a form/registration tool (sign-up offer, not sellable admission inventory).
2. **The ticket as the sold access artifact.** Each completed order issues tickets as distinct, individually checkable entitlements to attend (electronic or printed, carrying a scannable/checkable identity). The ticket is the product being sold — not a receipt for a registration. Remove it → Event Registration Platform (registrant record is the output) or plain commerce (goods, not entitlements).
3. **Organizer-side management of the sale lifecycle.** The organizer controls the on-sale (publish/open, capacity, pricing windows) and works the resulting sales in the same system — orders, refunds/exchanges, reporting — rather than merely listing tickets elsewhere. Remove it → a bare consumer listing/checkout or a classified ad, not a ticketing platform.

Notes on deliberate exclusions from L0:

- **Payment is NOT definitional.** Free ticketed events are directly documented (Eventbrite free ticket types; Purplepass free events with no service fees), and deferred payment is directly documented (Purplepass reservations mode — pay at the event; Spektrix reservations with deposits/proforma invoices). What is definitional is the *sale of a ticket artifact*, which can be zero-priced or settled later.
- **Entry validation machinery is NOT definitional.** Scanning apps/scanners are the modern standard, but the ticket-as-checkable-artifact predates scanners (paper stubs torn at the door); the historical check passes without scanning. Validation machinery is L1.
- **Seat maps are NOT definitional.** General admission is equally first-class in all sampled products; reserved seating is a mode. (Also the reason a separate Reserved Seating Platform leaf can exist.)
- **The consumer marketplace is NOT definitional.** Two of four sampled products distribute only through the organizer's own channels.
- **Resale is NOT definitional** — it is a separate directory leaf (Ticket Resale Marketplace) and appears here only as a capability.

### L1 — Common Mature Structure

Present across the sample; expected in mature products but not required to recognize the Type:

- public event/listing page with dates, venue, description (the sales surface)
- ticket-type pricing machinery: tiers, early-bird windows, promo/discount codes, automatic/dynamic price changes
- capacity management: event/section/instance caps, holds, waitlists
- integrated payment processing with fee handling (buyer-pays vs organizer-absorbs vs split) and refunds
- order management: search, inspect, edit, refund, resend
- ticket delivery: electronic (app/wallet), print-at-home, will-call/box-office pickup
- entry validation: scan apps, scanner hardware, check-in windows, scan history
- on-site/door sales channel
- sales reporting/analytics (revenue, attendance, channel breakdown)
- buyer/order records with custom questions
- multi-date, recurring, and timed-entry event structures
- team roles/permissions
- order confirmations and event-update notifications

### L2 — Variant / Optional Structure

Depends on segment, scale, business model, or region:

- distribution model: own-channel only vs consumer marketplace discovery vs both
- reserved seating / seat maps vs general admission (and multi-area mixes)
- box-office operations depth: staffed counter selling, reservations/deposits, group bookings, ticket-printing hardware (venue/arts pole)
- subscription/series/pass products: fixed-series seat rights, ticket-subscription vouchers, season/flex passes, memberships (arts/season pole)
- presales, on-sale queues, per-order ticket limits, anti-fraud/anti-bot controls (large-scale pole)
- fan-to-fan resale/exchange and transfer policies (transferable vs locked vs face-value-only)
- dynamic/variable pricing
- add-ons: merchandise, upgrades, drink tickets (inventoried vs non-inventoried), parking
- donations at checkout / donation campaigns
- virtual/live-stream ticket types
- fee models (per-ticket service fee vs flat vs none) and regional tax handling (VAT vs US sales tax)
- agents/resellers selling on the organizer's behalf with commission machinery

### L3 — Vendor-specific Structure (research notes only)

- Eventbrite: "Registration event" as a named event type; sections with own capacity; eTicket/Will Call delivery names; scheduled pre-event payouts; Eventbrite Ads; marketplace-scale claims (90M buyers, 270M tickets in 2024 — vendor claims); dynamic pricing by date or by number sold.
- Spektrix: Events/Instances terminology; per-instance Price List matrix (ticket type × price band); Supplementary Events; soft crediting; restricted orders; accounting dates; custom payment types (cheque/BACS/invoice); gift aid; agents interface; named scanner/printer hardware lines.
- Purplepass: reservations mode (pay at event); non-inventoried items; flex passes; live-stream widget; COMP tickets; fee-split control.
- Ticketmaster: Face Value Exchange; presale signup/queue mechanics; mobile-wallet-only entry with delayed barcode release; ticket-limit enforcement; league "Official Ticket Marketplace" positioning; family brands (Live Nation, Front Gate Tickets, TicketWeb, Universe).

## Rejected Findings

- "Ticketing = seat maps" — rejected. General admission is first-class in all four products; reserved seating is a mode (and a separate directory leaf exists for seat-map-centered selling).
- "Ticketing = marketplace discovery" — rejected. Purplepass and Spektrix distribute through the organizer's own channels only.
- "Ticketing = scanning hardware" — rejected as definitional. The checkable ticket artifact predates scanners; scanning is the modern standard implementation of entry validation (L1).
- "Ticketing = paid events" — rejected. Free ticketed events and deferred-payment reservations are directly documented in two products.
- "Ticketing = consumer-facing app" — the buyer-facing surface is prominent in marketplace products, but the Type's center is the organizer-side sell loop; buyer surfaces are the distribution of that loop.
- "Ticketing includes the event program/agenda" — rejected. Program machinery belongs to Event Agenda Management (processed); none of the sampled products centers it.

## Boundary Findings

1. **vs Event Registration Platform (§26 sibling, processed — flag DISCHARGED, keep-both RATIFIED from this side).** The registration pass proposed "registrant record vs ticket-as-sold-inventory" as the discriminator and asked this pass to ratify. Ratified with direct evidence: Eventbrite's own help center models **"Registration event" as a named event type distinct from ticketed events**, makes free events registration-only by default, and provides a toggle to disable PDF tickets entirely — i.e., the same product can run *without* the ticket artifact, and when it does, the output is a registrant roster, not sold inventory. Conversely, in ticketing mode the ticket is the product being sold: it carries price/quantity/inventory semantics (holds, sales windows, per-order limits, delivery methods, check-in windows) that a registration receipt does not. Removal tests hold both ways: remove the ticket artifact and inventory semantics → a registration platform remains; remove the registrant-record/roster machinery (custom questions, roster operations as the center) → a ticketing platform remains. The market itself splits the poles at company level (the registration pass recorded RunSignup vs TicketSignup sibling brands). Both Types stand; the seam is the ticket artifact + inventory semantics vs the registrant record + roster semantics.
2. **vs Event Management Platform (§26 sibling, processed).** Ticketing centers the sell → issue → validate loop and its inventory; the EMP centers the whole event lifecycle (setup → publish/promote → register → manage → run → closeout) with ticketing as one capability. The EMP pass already recorded this seam; confirmed from this side. Eventbrite straddles (marketplace ticketing + full organizer tooling) — packaging convergence, not Type merger.
3. **vs Attraction Ticketing / Attraction Management System (§26 siblings, processed).** The attraction pass recorded this as "the sharpest structural boundary": event ticketing's inventory unit is dated performances/occurrences (often seat-mapped, one-off); attraction ticketing's unit is admission capacity to a place (day/time-slot, no seat map as primary). Confirmed from this side. Arts & culture platforms (Spektrix in this sample; Tessitura per the attraction pass) contain both models — the boundary is the primary inventory model, not the vendor.
4. **vs Attendee Management (§26 sibling, processed).** Here the person record is a byproduct of the ticket sale; there the roster and presence recording are the center, and selling to the public is not required. Confirmed from this side (that pass's own wording).
5. **vs Convention/Exhibition Management (§26 sibling, processed).** This Type monetizes admission (attendee pays for access); that Type monetizes participation (exhibitor pays for space/services). Both may coexist in one show's stack. Confirmed from this side.
6. **vs Cashless Venue Platform (§26 sibling, processed).** The ticket is an admission entitlement; the cashless platform's objects are credentials, spending accounts, transactions, settlements. Festivals bundle both. Confirmed from this side.
7. **vs Reserved Seating Platform (§26 sibling, unprocessed) — joint review flagged.** Candidate split: the seat map as the primary managed object (seat-level inventory, map design, seat states) vs the ticketed event as the primary object with seat maps as one capability mode. All four sampled products implement reserved seating as a mode inside event ticketing; whether a standalone seat-map-centered product family exists is for that pass to determine.
8. **vs Ticket Inventory Management (§26 sibling, unprocessed) — joint review flagged.** Candidate split: the inventory/allocation discipline as the center (allocations, holds, on-sale times, channel splits, house seats — the large-venue/promoter machinery) vs the full sell → issue → validate loop as the center. Holds exist in this sample (Eventbrite holds; Spektrix locks/holds/kills) as one capability; whether the allocation discipline constitutes its own product family is for that pass to determine.
9. **vs Ticket Resale Marketplace (§26 sibling, unprocessed) — joint review flagged.** This Type is primary ticketing (organizer sells original inventory); the resale leaf is the secondary market (fans resell). Fan resale appears inside this Type as a capability (Ticketmaster's Sell/Face Value Exchange; transfer mechanics) — the seam is primary sale vs secondary transaction, and marketplace products straddle it.
10. **vs E-commerce Platform (§05.01).** Generic commerce sells undated products with shipping; ticketing sells dated admission inventory and issues access entitlements validated at entry. Add-ons/merchandise inside ticketing products are the e-commerce seam (Purplepass explicitly models non-inventoried items that do not count toward capacity).
11. **vs Airline Reservation / Passenger Service System (§18, processed).** That pass already recorded the seam: event ticketing sells numbered seats with inventory controls but has no fare-rule repricing, no interline, no day-of-travel document/bag process. Confirmed from this side.
12. **vs Restaurant Reservation Platform (§26 sibling).** Reservation books a table/cover at a hospitality time slot; ticketing sells admission to a dated event. Different object of record, different operator.
13. **vs Event Agenda Management (§26 sibling, processed).** Program/session machinery is not part of this Type's center; lineup fields on event pages are descriptive content, not a program-of-record.
14. **vs Event Credential / Badge Management (§26 sibling, processed).** That pass recorded: ticket = paid admission entitlement (transaction object); credential = persistent on-site identity + category privileges. Tickets commonly become badges at the door — the handoff is the seam. Confirmed from this side.

"Remove what to become the other Type" summary: remove the ticket artifact and inventory semantics → Event Registration Platform; add the whole event lifecycle as the center → Event Management Platform; switch the inventory unit to place-admission capacity → Attraction Ticketing/Attraction Management System; make the roster/presence the center → Attendee Management; make the seat map the primary object → Reserved Seating Platform (candidate); make the allocation discipline the center → Ticket Inventory Management (candidate); make the secondary market the center → Ticket Resale Marketplace; remove the dated-admission semantics → E-commerce Platform.

## Historical / Market-Sample Check

Box-office ticket selling predates this software generation: paper tickets issued at a box office or through ticket agencies, torn/stubbed at the door, with the seller keeping a record of sales against an event's allocation. The proposed core (ticketed-event inventory + sale producing a recorded order + ticket as a checkable entitlement + organizer-side sales management) holds for that era without any software-era feature: no scanning (stub-checking suffices), no marketplace (box office window), no dynamic pricing, no mobile delivery. The check passes; the core is not an artifact of the current mobile-marketplace implementation.

## Uncertainties

- Ticket Tailor (flat-fee self-serve pole) and ShowClix (full-service agency pole) could not be fetched (403 ×2 each). The flat-fee business-model pole and the full-service/white-glove agency pole are therefore not directly evidenced; the sample covers self-serve (×2), box-office/arts, and dominant primary+marketplace.
- Ticketmaster's organizer-side tooling is not publicly documented; all Ticketmaster evidence is consumer-side. Claims about promoter/venue capabilities are avoided in the final document.
- Waitlist auto-promotion mechanics were not directly evidenced this pass (Eventbrite's pricing page lists waitlists as a feature; mechanics not fetched).
- Exact fee percentages (Eventbrite's 3.7% + $1.79 + 2.9% as displayed) are plan- and region-dependent; they are recorded here but deliberately excluded from the final document.
- Whether invitation-gated/hidden ticket types are common across the market is evidenced in one product (Eventbrite hidden tickets revealed by promo code); kept as a capability observation, not generalized.
- Regional (non-US/UK) ticketing products were not sampled; regional variants (e.g., EU consumer-rights refund rules) are unknown.
- The boundary with the three unprocessed siblings (Reserved Seating Platform, Ticket Inventory Management, Ticket Resale Marketplace) is recorded as candidate splits pending those passes.

## Final Synthesis

The Event Ticketing Platform is the sell-centered member of the event family. Its defining core is a three-link chain: the organizer defines ticketed events — dated occurrences carrying ticket types with price and quantity as sellable inventory; each completed sale is recorded as an order and issues tickets as distinct, checkable access entitlements (the ticket is the product being sold, not a receipt for a registration); and the organizer manages the resulting sales in the same system — on-sale control, orders, refunds, reporting, and entry. Around this core, mature products add a stable ring: public event pages, pricing machinery (tiers, codes, dynamic prices), capacity control with holds and waitlists, integrated payments with fee handling, ticket delivery (electronic, printed, will-call), scanning-based entry validation, door sales, and reporting. The market realizes the Type in distinct poles — self-serve with a consumer marketplace, self-serve with own-channel distribution only, box-office/arts platforms with deep staffed-selling and subscription machinery, and dominant large-scale primary ticketing with presales, queues, and an official resale marketplace — but the poles share the same spine. The Type's sharpest ratified boundary is with the Event Registration Platform (ticket-as-sold-artifact vs registrant record, ratified keep-both with direct product evidence); its open seams are with the three unprocessed ticket siblings (Reserved Seating, Ticket Inventory Management, Ticket Resale Marketplace), where the candidate discriminators are the seat map, the allocation discipline, and the secondary market respectively.
