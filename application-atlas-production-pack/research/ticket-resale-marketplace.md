# Research Notes — Ticket Resale Marketplace

## Research Goal

Understand what a Ticket Resale Marketplace actually is as an Application Type: what object world it manages, who uses it, how the resale transaction actually flows, what rules and guarantees govern it, and where its boundaries sit against the primary ticketing platform (Event Ticketing Platform), the general Resale Marketplace (§05.19), Classifieds, and the reseller-side inventory tooling pole flagged by the ticket-inventory-management pass.

## Initial Boundary (hypothesis before research)

- Core use: a venue where holders of tickets to events (fans, season-ticket holders, brokers) sell them to buyers, with the platform mediating payment, delivery of the ticket entitlement, and guarantees.
- Likely users: buyers (fans who missed the onsale, want better seats, decided late), sellers (fans, season-ticket holders, professional brokers), plus official sources (teams/venues) in some products.
- Nearest neighbors: Event Ticketing Platform (primary sale), Resale Marketplace §05.19 (physical goods), Classifieds Platform, Online Auction Platform, Ticket Inventory Management (reseller pole), Reserved Seating Platform.
- Unknowns: how delivery/transfer works across products; guarantee mechanics; payout timing; whether auction/bidding exists as a mode; how the primary-embedded resale pole differs; where the broker-side tooling pole belongs.

## Research Questions

1. What is the object of record — the listing, the ticket, the order?
2. How is the event catalog used as the organizing axis?
3. What can a seller list, from what sources, under what eligibility rules?
4. How does delivery work when the ticket lives in a third-party ticketing system?
5. How does money flow — when is the seller paid, what fees exist, who holds the risk?
6. What does the platform guarantee, and what happens on failure (undelivered, invalid, canceled, postponed)?
7. How much pricing freedom do sellers have, and what restrictions can event organizers impose?
8. How does the primary-embedded resale pole (Ticketmaster fan-to-fan) differ structurally?
9. Does auction/bidding exist as a pricing mode in current products?
10. Where does the reseller-side inventory tooling pole (Victory Live One) belong?

## Representative Products

| Product | Pole | Evidence level |
|---|---|---|
| SeatGeek | open marketplace + official-source supply mix (teams/venues/box offices), Deal-Score heritage | A — 6 help-center articles fetched |
| TickPick | no-fee/all-in pricing philosophy; explicit broker tier | A — 6 help-center articles fetched |
| Ticketmaster (fan-to-fan resale + Face Value Exchange) | primary-embedded resale pole | A — sell page + Face Value Exchange FAQ fetched |
| StubHub | classic large fan marketplace | NOT REACHABLE (2 attempts, abandoned) |
| Vivid Seats | broker-heavy large marketplace | NOT REACHABLE (3 attempts, abandoned) |
| Gametime | last-minute mobile marketplace | NOT REACHABLE (1 attempt, abandoned) |

Sample rationale: three products with strong official operational documentation, each a different philosophy (open marketplace with official integrations / no-fee marketplace / primary-embedded exchange), plus structural coverage of the classic-marketplace and broker-heavy poles. Stop conditions met: core model explainable, workflows clear, stable commonalities across the sampled products, boundaries clear.

## Sources

- SeatGeek Help Center (support.seatgeek.com): "How do I sell tickets on the SeatGeek Marketplace?", "Can I trust tickets sold on SeatGeek?", "How does SeatGeek verify tickets?", "How does SeatGeek handle ticket pricing and marketplace fairness?", "What happens after your tickets sell on SeatGeek", "What is mobile transfer ticket delivery?" — fetched 2026-09-09.
- TickPick FAQ (support.tickpick.com): "How do I list my tickets for sale?", "What types of tickets am I able to sell on TickPick?", "Can I list my tickets on other marketplaces at the same time?", "Why do I need a credit card on file to list tickets for sale…", "I sold my tickets — how do I confirm the sale and deliver my tickets?", "When and how will I get paid if my tickets are sold?" — fetched 2026-09-09.
- Ticketmaster: "How does Ticketmaster's Face Value Exchange work?" (help.ticketmaster.com, Resale category) and the "Sell on Ticketmaster" page (ticketmaster.com/sell) — fetched 2026-09-09. Help-center home page also yielded Face Value Exchange event-page language and Ticket Transfer references.
- Unreachable: help.stubhub.com (empty render), stubhub.com/legal (title only), vividseats.com/help (challenge validation), support.vividseats.com (404), help.vividseats.com (transport error), tickpick.com/help (404, redirected to support.tickpick.com), support.gametime.co (404).

## Product Observations

### SeatGeek (Layer A — direct)

- **Selling**: list eligible tickets from the Tickets section of the account via a Sell button. Requirements: tickets already in your possession, eligible for resale, Sell button visible. Tickets not yet delivered cannot be listed. Listing flow: choose quantity → set split options, price, payout method → enter original price paid (affects sales-tax base) → publish. Individual resale listings limited to 8 tickets; higher listing tiers exist for eligible accounts. Edit/delist from the same surface. "Smart Pricing" can automatically adjust the listing price based on demand.
- **What can be sold**: most eligible mobile tickets. Not eligible: physical tickets, wristbands, PDFs, screenshots, charity tickets, undelivered tickets (list not exhaustive; Seller Terms govern).
- **Supply mix**: tickets sold by "licensed sellers, other SeatGeek customers, integrated partners, and sometimes the team's box office". Verification article: many tickets come directly from official ticketing sources — professional sports teams and leagues, venues and event organizers, box offices and primary ticketing systems, official ticketing and distribution partners — often via direct integrations with the organization managing the event's inventory. "Verified" indicators mark tickets from official sources on some events.
- **Seller obligations**: deliver valid tickets, follow marketplace policies, meet delivery deadlines, comply with laws and event restrictions. Failure → listing restrictions, account actions, financial responsibility for replacement tickets, other remedies per Seller Terms.
- **Buyer Guarantee**: covers delivery in time for the event, valid entry, tickets matching what was ordered. Remedies: comparable or better replacement tickets or a refund. Canceled (not rescheduled) events: full refund or, where state law applies, credit. Postponed: tickets usually remain valid for the new date; refunds generally not provided; buyer may list tickets for resale. Not covered: mistaken purchases, schedule changes, lineup changes that aren't cancellations, venue-rule denials, personal expenses.
- **Pricing**: open marketplace; sellers set prices within rules/laws/event restrictions; prices move with supply/demand, popularity, seat location, inventory, timing. Some events carry pricing restrictions (minimums/maximums) from teams/venues/artists/promoters/regulations. Buyer aids: Deal Score, pricing comparisons across similar listings, seat views and venue maps, all-in pricing with fees displayed before checkout. SeatGeek does not manually set individual sellers' prices.
- **After sale**: email notification; check sale in Listings. If the ticket barcode is in the SeatGeek account → no action, SeatGeek delivers to the buyer. If the barcode is in a third-party account → seller sends via the original provider (e.g., Ticketmaster, AXS) and confirms the transfer in SeatGeek. "Do not contact the buyer directly. Only use their information to send the tickets." Delivery deadlines apply. Payment sent 2 business days after the event; funds typically arrive within 5–7 business days. Tax requirements for sellers.
- **Mobile transfer delivery**: tickets delivered electronically through the venue or team's official ticketing platform (Ticketmaster, AXS, MLB Ballpark app) via an email invitation/link; buyer accepts with the same email used at purchase; rotating barcodes, QR codes, or Mobile IDs; barcodes often generated 24–48 hours before the event; tickets do NOT move into the SeatGeek account; format/delivery method is set by the venue and cannot be changed by SeatGeek or the seller.

### TickPick (Layer A — direct)

- **Listing flow**: log in → "Sell Tickets" → search the event → select date/venue/time → step-by-step ticket details → price → agree to terms. Tickets may be listed before they are in-hand (delivery delays common); seller must provide an accurate in-hand date; hard-stock listings are taken down 96 hours before the event to allow shipping. Minnesota state law requires seat-number disclosure.
- **Seat disclosures**: sellers must disclose any disclosure printed/displayed on the tickets (limited/obstructed view, wheelchair accessible, wheelchair only, aisle, 21+ section, side/rear view, restricted leg room, alcohol-free, parking pass only/included, not an event ticket, VIP access included, etc.); failure → seller may be held responsible for penalty fees on the order.
- **Pricing**: seller sets the price; the cheapest current price for the event is shown as reference; supply/demand named as the largest factor; sellers advised to monitor and adjust.
- **Ticket forms**: hard stock (paper), E-Tickets (PDF), mobile transfer — depending on event proximity. "Will call" and "local pickup" delivery options are available only to large professional ticket brokers, not individual sellers (explicit broker tier).
- **Multi-marketplace listing**: cannot be prevented, but strongly discouraged; if the seller cannot deliver because the tickets sold elsewhere, penalties of 200% or more of the sale price may be applied to fund a suitable replacement for the buyer.
- **Seller guarantee mechanism**: a credit card on file is required to list; a small authorization charge validates the card; if tickets are not delivered or are invalid for entry, a fee can be processed against the card to secure replacement tickets for buyers or compensation credit.
- **After sale**: email on sale; confirm in the "Sales" page; if not ready to deliver, confirm with an estimated delivery date (reminder emails follow). Delivery by form: mobile transfer → send from the venue's primary ticketing company (Ticketmaster, AXS, SeatGeek, etc.) to the buyer's name/email shown in the selling portal; PDF → upload as attachment; hard stock → print a prepaid shipping label (label paid by buyer), ship via FedEx.
- **Payout**: paid up to 14 days after the event "to ensure there were no issues for the buyer"; Payouts tab; phone/personal/tax verification; payout methods: US bank transfer, PayPal, Venmo; Canada bank account.
- **Season tickets**: multiple events can be listed at once. Parking passes listable. Seller tools: AutoList (list across multiple marketplaces), AutoPrice (automatic repricing), CreditBoost, FanLink, Price Freeze.

### Ticketmaster (Layer A — direct)

- **Fan-to-fan resale (general)**: sell from My Tickets via a Sell button; listings tagged "Verified Resale". Seller sees the payout based on the price set and can compare other listings in the same section; can change price or remove listing anytime. Platform handles delivery to the buyer ("we'll handle getting the tickets to the buyer"); payout typically within 7 business days after the event. Listing is free; a seller fee is collected from the total selling price when sold. A valid card on file is required "to refund the buyer in case the event is postponed or canceled". Seller tax identification required (US 1099-K flow; Canadian fans need US bank account + US tax ID for US events). Bank-verification via two microdeposits.
- **Organizer authority**: "We support the artist, team or event organizer's ability to set the terms for how their tickets are sold and resold. Resale might be capped or turned off on Ticketmaster for some events or ticket types at the event's direction." Eligibility is per event: most tickets bought on Ticketmaster can be resold, but the Event Organizer decides; VIP, commemorative, will-call and charity tickets cannot be resold; events where Ticketmaster is not the primary provider cannot be resold on Ticketmaster. Price restrictions: organizer-set minimum/maximum per ticket; alerts force price changes outside the band.
- **Void-and-reissue**: "when you sell a ticket on Ticketmaster, we void the old one and reissue an entirely new ticket to protect both the buyer and the seller." Distinct from transfer (sending to someone you know).
- **Instant offers**: if available, the seller can accept an immediate offer for the tickets instead of listing (offer may appear during listing or later).
- **Face Value Exchange**: fans sell to other fans at face value; free for sellers; listing price automatically set at the total price paid (face value + fees + taxes); price cannot be changed ("to respect the artist's decision"); first-come first-served; tickets listed up until one hour after event start, then unsold tickets return to the seller's account; only tickets in the Ticketmaster Account can be sold (tickets bought on other sites and not transferred in cannot be resold); a resale ticket can be re-sold at the same price paid; payout typically within 7 business days after the event; event page shows an info box identifying Face Value Exchange purchases. Event-page language: tickets are non-transferable and can only be resold on Ticketmaster at face value; tickets listed elsewhere through unauthorized sources may be fake or invalid; only tickets displayed in the Ticketmaster app are valid. State laws (NY, IL, CO, VA, UT, CT) prevent resale restrictions; Ticketmaster still honors the organizer's terms by keeping resale prices at face value on its site.
- **Ticket Transfer** (adjacent capability, for contrast): available no later than 3 months before the event; transfer to others from the order; merchandise/VIP elements/fan-club memberships/ticket insurance not transferable.

## Cross-product Comparison

| Dimension | SeatGeek | TickPick | Ticketmaster resale | Reading |
|---|---|---|---|---|
| Traded good | tickets to specific dated events (seat/section) | same | same | L0 common |
| Seller identity | customers, licensed sellers, integrated partners, box offices | individual sellers + explicit large-broker tier | fans holding tickets in their TM account (organizer-gated) | secondary-market posture common; supply mix varies |
| Listing as unit | yes (price, quantity, split, payout) | yes (+ in-hand date, disclosures) | yes (+ organizer price bands) | L0/L1 common |
| Event catalog as axis | yes (event pages, search) | yes (search event → date/venue/time) | yes (event pages, section comparison) | L1 common |
| Platform-mediated payment | yes | yes | yes | L0 common |
| Delivery = entitlement transfer | mobile transfer via primary platforms; automatic when barcode in-platform | mobile transfer from primary company / PDF upload / hard-stock shipping | platform handles delivery; void-and-reissue | L1 common, form varies |
| Guarantee | Buyer Guarantee (delivery/validity/matching; replacement or refund) | card-on-file recovery + penalties fund replacements | Verified Resale + card on file to refund buyer; organizer terms | L1 common (naming/mechanics vary) |
| Payout after event | 2 business days after event | up to 14 days after event | ~7 business days after event | L1 common; windows vary by product |
| Seller-set pricing | yes, within event restrictions | yes, with cheapest-price reference | yes, within organizer min/max; FVX = price fixed at paid | L1 common; restriction depth varies |
| Organizer authority over resale | event restrictions acknowledged | event proximity/eligibility rules | explicit and deep (eligibility, caps, off-switch, FVX) | L1 common; strongest at primary-embedded pole |
| Buyer refunds for change of plans | no (sales final) | no (sales final) | no (sales final) | L1 common |
| Auction/bidding | not observed | not observed | not observed | not asserted |
| Multi-marketplace listing | not documented in fetched pages | discouraged, penalized | n/a (only TM-primary tickets) | variant |
| Instant/platform offer | not observed | not observed | yes (instant offers) | product-observed variant |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (three jointly-held structures)

1. **The event-anchored admission entitlement as the traded good.** Listings offer tickets to specific dated event occurrences — event, date, venue, seat or section identity — not generic goods. The entitlement is perishable (worthless after the occurrence) and its delivery is the transfer of entry rights, not the shipment of a product. Remove → a general resale marketplace or classifieds board.
2. **The secondary-market posture.** Sellers are holders of tickets acquired elsewhere — fans, season-ticket holders, brokers — not the event's organizer or box office; the platform is not the primary channel through which the event's inventory is first issued. Remove → Event Ticketing Platform.
3. **The platform-mediated resale transaction ending in entitlement transfer.** The platform inserts itself between buyer and seller: in-platform listing, in-platform order and payment, platform-governed delivery of the ticket to the buyer, and the platform standing behind the sale (resolving failures, compensating or replacing). Remove → classifieds (contact-and-arrange-yourself).

Jointly-held load-bearing tests:
- 1 alone = an event page with prices (no market).
- 2 alone = nothing (a posture needs an object and a venue).
- 3 alone = generic marketplace machinery over unspecified goods.
- 1+2 without 3 = ticket classifieds / street-scalper boards (real market form, different Type).
- 1+3 without 2 = a primary ticketing platform selling its own inventory (the sharpest boundary — Event Ticketing Platform).
- 2+3 without 1 = the general Resale Marketplace (§05.19) over physical goods.

### L1 — Common Mature Structure

- Event catalog as the organizing axis: search/browse by event, date, venue; the event page aggregates all listings for that occurrence.
- The listing as the seller's unit of work: event binding, quantity, seat/section, price, split options, disclosures, payout method; editable and removable until sold.
- The buyer-guarantee posture: valid entry, on-time delivery, tickets as ordered; remedies as replacement or refund; explicit exclusions (buyer's schedule, non-cancellation lineup changes).
- Payout after the event: seller funds settle only after the occurrence passes (windows vary by product) — an escrow-like settlement that funds the guarantee.
- Delivery machinery matched to ticket form: mobile transfer through the primary ticketing platform (accept with the order email), electronic ticket upload, physical shipping for hard stock; delivery deadlines; format set by the venue, not the marketplace.
- Seller accountability: delivery obligations, penalties/fees on failure, financial responsibility for replacements, card-on-file or equivalent security, account restrictions.
- Fees: seller and/or buyer fees; all-in price display in some products.
- Price freedom with event-level limits: seller-set prices within laws and organizer restrictions (minimums/maximums, face-value-only).
- Buyer decision aids: filters, seat views/maps, price comparison across listings, deal/value indicators.

### L2 — Variant / Optional Structure

- Supply mix: pure fan C2C ↔ broker-heavy ↔ official-source integrations (teams/venues/box offices feeding listings directly) ↔ hybrid.
- Primary-embedded resale: fan-to-fan exchange inside the primary platform; void-and-reissue of the entitlement; organizer-gated eligibility; face-value-only exchanges; state-law interplay (some US states prohibit resale restrictions).
- Instant offers: platform or partner buys tickets outright (principal posture) alongside the marketplace.
- Seller automation: demand-based auto-repricing; multi-marketplace listing/sync (with double-selling penalties); season-ticket multi-event listing.
- Adjacent inventory: parking passes; VIP-adjacent caveats (VIP/charity/commemorative often non-resellable).
- Regional/regulatory packaging: seat-disclosure laws, resale-restriction laws, seller tax reporting, payout-method availability by country.
- Rewards/credit programs, price freezes, last-minute deal positioning.
- Auction/bidding: NOT observed in any sampled product's documented flows; not asserted as present or absent market-wide.

### L3 — Vendor-specific (Research Notes only)

- SeatGeek: Deal Score, Smart Pricing, 8-ticket individual listing cap with higher tiers, "Verified" source indicators, 2-business-day post-event payout, sales-tax base tied to declared original price.
- TickPick: no-fee/all-in positioning, AutoList/AutoPrice/CreditBoost/FanLink/Price Freeze, 96-hour hard-stock takedown rule, 200%+ double-selling penalty, card-on-file authorization charge, broker-only will-call/local-pickup delivery.
- Ticketmaster: Verified Resale label, void-and-reissue mechanism, Face Value Exchange (price fixed at total paid, 1-hour-after-start listing deadline, unsold returns to account), instant offers, organizer min/max price bands, microdeposit bank verification, 1099-K seller-tax flow.
- Victory Live One (inherited from ticket-inventory-management pass, product-page level): reseller-side "Ticketing Inventory Management System" — acquired stock synced from POS/uploads, multi-marketplace distribution with price/status sync, dynamic pricing, fulfillment/settlement/reconciliation; self-service/full-service/consignment modes.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical core. The void-and-reissue mechanism (Ticketmaster) is the deepest entitlement-integrity implementation observed but is tied to the primary-embedded pole; independent marketplaces instead rely on transfer-based delivery plus guarantee recovery.

## Boundary Findings

1. **vs Event Ticketing Platform (§26, processed 2026-09-07) — flag DISCHARGED, keep-both RATIFIED.** The seam is who sells and what stage of the ticket's life the system serves. Ticketing platform: the organizer's own-channel sale of newly issued inventory (sell → issue → validate loop; the ticket is created there). Resale marketplace: holders reselling already-issued entitlements (the ticket already exists; the marketplace moves it between holders). The event-ticketing pass correctly observed that fan resale/transfer appears inside ticketing as a policy capability — confirmed here from the other side: Ticketmaster's resale exchange is a capability of the primary platform, and its own docs distinguish transfer (send to someone you know) from selling (void-and-reissue through the platform). Removal tests both ways: remove the secondary posture from a resale marketplace → it becomes a ticketing platform; remove primary issuance from a ticketing platform → its resale exchange becomes this Type. The two Types meet in "official resale exchange" products, which are genuinely the seam. Both leaves stand.
2. **vs Resale Marketplace (§05.19, processed) — flag DISCHARGED from this side.** Same name, different object world, exactly as that pass recorded: general resale trades pre-owned physical goods (possession, shipping, condition); ticket resale trades dated, perishable, seat-bound entitlements (no condition, no shipping as the norm, delivery = accepting entry rights in a ticketing app, hard deadline at event time, worthless after). Separate leaf stands — confirmed with direct evidence from this side.
3. **vs Classifieds Platform (§05.03).** The mediated transaction is the seam, same as the general-resale pass found: TickPick penalizes off-platform double-selling and processes recovery fees; SeatGeek instructs sellers not to contact the buyer directly and routes delivery/disputes through the platform. Classifieds = contact-and-arrange-yourself.
4. **vs Ticket Inventory Management (§26, processed 2026-09-09) — reseller-inventory-pole question DECIDED.** That pass asked whether the reseller inventory pole (Victory Live One "Ticketing Inventory Management System") belongs here, as a future sibling, or stays as that leaf's adjacent pole. Decision from this side: it stays adjacent — it is seller-side stock machinery (acquired stock, multi-marketplace distribution, price sync, settlement) that feeds marketplaces; it is not the venue itself. The marketplace's object world is the listing/order/entitlement transfer; the broker tooling's object world is owned stock across channels. Documented as an adjacent pole in this leaf's Variants/Related; recommendation to the taxonomy owner: if the reseller-side tooling family grows in documentation coverage, it could merit its own leaf (e.g., under §05.23 seller-operations), but no directory change is made from this side.
5. **vs Reserved Seating Platform (§26, processed 2026-09-09) — flag DISCHARGED.** Seat-level resale capability (seat-named listings, seat views) is presentation of the entitlement inside this Type; the managed object here is the listing/order, not the seat map. The reserved-seating leaf centers the seat map as managed inventory for the primary sale; resale marketplaces consume seat identity as a listing attribute. Seam holds.
6. **vs Online Auction Platform (§05.18).** Auction/bidding was not observed as a documented pricing mode in any sampled product this pass. No claim made in either direction; the general-resale pass's treatment (auction as pricing-mode variant, dedicated Type for auction-centered products) is adopted structurally.
7. **vs Event Registration Platform.** No overlap: registration sells attendance records, not admission entitlements; out of scope.

## Historical / Market-Sample Check

Paper-era check: the ticket broker's office (pre-internet) satisfies the L0 with no software — the broker holds tickets acquired from season-ticket holders and subscribers (secondary posture), sells specific seats for specific dated events over the counter or by phone (event-anchored entitlement), takes payment, hands over or will-calls the tickets, and stands behind the sale (guarantees valid seats, sources replacements if a ticket fails — mediated sale with the broker as the accountable party). Settlement after the event matches the payout-after-event pattern. What does NOT satisfy the L0: the newspaper classified or the street scalper operating alone (no mediation, no standing-behind) — correctly excluded as classifieds / informal resale, not a marketplace. The definition therefore does not depend on apps, buyer-guarantee branding, dynamic pricing, or all-in pricing displays — all era-current machinery sits in L1/L2. Older and regional forms (broker networks, agency consignment counters, international secondary markets) fit the same invariant. Check passed.

## Uncertainties

- StubHub, Vivid Seats, and Gametime could not be fetched (bot-blocked/404/empty renders). The classic large-marketplace and broker-heavy poles are covered structurally (via TickPick's explicit broker tier and SeatGeek's licensed-seller/official-source mix) but with no direct evidence from those two product classes; no StubHub/Vivid Seats-specific claims are made anywhere.
- Auction/bidding prevalence in the current market is unknown from fetched evidence; deliberately not asserted.
- Exact guarantee windows, penalty percentages, and payout windows are product-observed (TickPick 200%+, 14-day payout; SeatGeek 2-business-day payout; Ticketmaster ~7-business-day payout) and are NOT generalized into industry constants in the final document.
- The Victory Live One evidence is inherited product-page-level material from the ticket-inventory-management pass; not re-verified this pass.
- Whether "instant offers" (platform-as-principal buying) exist beyond the primary-embedded pole is unverified.
- International/regional marketplaces (e.g., viagogo) not fetched; regional variants described only at the structural level.

## Final Synthesis

A Ticket Resale Marketplace is the mediated venue where already-issued event admission entitlements change hands between holders and buyers. Its defining core is three jointly-held structures: (1) the traded good is the event-anchored admission entitlement — a ticket to a specific dated occurrence, identified by event/date/venue/seat, perishable, delivered as transferred entry rights rather than shipped goods; (2) the secondary-market posture — sellers are holders (fans, season-ticket holders, brokers), not the organizer, and the platform is not the primary issuing channel; (3) the platform-mediated transaction — in-platform listing, order, payment, delivery of the entitlement, with the platform standing behind the sale and settling seller funds only after the event has passed. Everything else — the event catalog, guarantee programs, delivery machinery per ticket form, seller penalties, fees, pricing tools, official-source integrations, face-value exchanges, instant offers — is mature structure or variant machinery that makes the model workable without defining it. The Type sits between the Event Ticketing Platform (which creates and first-sells the entitlement) and the general Resale Marketplace (which mediates physical-goods resale), and its sharpest practical expression is that the marketplace's product is certainty of entry, not the ticket itself.
