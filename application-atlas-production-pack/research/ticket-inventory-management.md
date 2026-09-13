# Research Notes — Ticket Inventory Management

## Research Goal

Understand what "ticket inventory management" is as an Application Type: what the inventory is (tickets are not physical goods), who manages it, how stock is created, partitioned, gated, released, and reconciled across the sellable life of an event — and how this Type relates to its three processed siblings (Event Ticketing Platform, Reserved Seating Platform, Event Management Platform) and one unprocessed sibling (Ticket Resale Marketplace).

Two prior passes left joint-review flags for this leaf:
- event-ticketing-platform (2026-09-07): "ticket-inventory-management (allocation/holds/on-sale discipline as center vs the full sell→issue→validate loop; holds directly observed as one capability in two sampled products)"
- reserved-seating-platform (2026-09-09): "ticket-inventory-management (ticket-type-grain allocation discipline vs seat-granular map)" and "ticket-inventory-management + ticket-resale-marketplace (sibling slices, flags stand)"

This pass must resolve those flags from its own evidence.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: the organizer/box-office-side discipline of controlling a bounded stock of admission rights — how many tickets exist per event/ticket type, which tranches are removed from general sale (holds, allocations, presales), when and through which channels each tranche can be sold, and how remaining stock is reconciled as sales, pending orders, releases and refunds occur.
- Users: box office managers, ticketing operations, promoters, event organizers, reseller operations (possible second reading).
- Nearest Types: Event Ticketing Platform (sell loop), Reserved Seating Platform (seat grain), Ticket Resale Marketplace (secondary market), Inventory Management System §10 (goods stock), Attraction Ticketing, Venue Management System.
- Unknowns: (1) does a standalone product family exist for this layer in the primary market, or is it a capability inside ticketing platforms? (2) the market also uses "ticket inventory management" for the reseller/broker stock-management category — which reading is the Type?

## Research Questions

1. What is the unit of managed ticket inventory (ticket type, price band, zone, seat, occurrence)?
2. How is inventory created and bounded (per-type quantities, total capacity ceilings, relationship between the two)?
3. How is stock partitioned into controlled tranches (holds, locks, allocations, channel restriction, presale gating) and what per-tranche rules exist (who/when/where)?
4. What is the lifecycle of a tranche of stock (created → held/gated → on sale → sold/pending → released/returned → closed)?
5. How does live reconciliation work (pending orders, releases, refunds returning stock, sold-out arithmetic)?
6. Is there a standalone primary-market product family, or is the layer realized inside ticketing platforms? Does the resale-side "ticketing inventory management" product family (Victory Live) constitute a second reading of the name?
7. Boundary vs Event Ticketing Platform, Reserved Seating Platform, Ticket Resale Marketplace, Inventory Management System (§10), Attraction Ticketing.

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Eventbrite | self-serve mass-market primary ticketing | holds documented as a dedicated feature with its own help article; strong operational docs |
| Spektrix | enterprise arts/venue ticketing (UK/global) | Locks/holds/kills terminology, capacity-vs-on-sale split, channel-bound ticket types documented in support centre |
| Purplepass | self-serve box-office ticketing | per-type quantity vs venue-capacity model documented; box-office G2 positioning |
| Tessitura | enterprise arts/museums/attractions suite | presales/exclusive-inventory and seat-release machinery at enterprise level (Tier-2 evidence) |
| Victory Live (Victory Live One; merger of Ticket Evolution, Logitix, 1Ticket, DTI) | reseller/rightsholder "ticketing inventory management" pole | ships a product literally named "Inventory Management" / "Ticketing Inventory Management System" — the exact leaf name in a different market reading |

## Sources

- Eventbrite Help Center: "Create and manage holds" (https://www.eventbrite.com/help/en-us/articles/779653/how-to-create-and-manage-holds/), "What to do when tickets aren't on sale" (https://www.eventbrite.com/help/en-us/articles/434070/what-to-do-when-tickets-arent-on-sale/), "Creating an event" topic index (https://www.eventbrite.com/help/en-us/topics/creating-an-event/) — fetched 2026-09-09, Tier 1, direct.
- Spektrix Support Centre: "Introduction to Events and Instances" (https://support.spektrix.com/hc/en-us/articles/11012056320541) — fetched 2026-09-09, Tier 1, direct. Note: help.spektrix.com unreachable (transport error ×2); support.spektrix.com used instead.
- Purplepass Help Center: Event Organizer category (https://help.purplepass.com/hc/en-us/categories/21570562726807-Event-Organizer), "Ticket Creation & Management" section index (https://help.purplepass.com/hc/en-us/sections/21574686774039-Ticket-Creation-Management), "Setting venue capacity for your event" (https://help.purplepass.com/hc/en-us/articles/22027576296727-Setting-venue-capacity-for-your-event) — fetched 2026-09-09, Tier 1, direct.
- Tessitura: "Ticketing & Admissions" feature page (https://www.tessitura.com/features/ticketing-admissions) — fetched 2026-09-09, Tier 2 marketing (operational docs gated), used with reduced assertion strength.
- Victory Live: "Ticketing Inventory Management System" product page (https://www.victorylive.com/products/inventory-management/), corporate home (https://www.victorylive.com/) — fetched 2026-09-09, Tier 2 marketing.
- Prior passes: research/event-ticketing-platform.md, research/reserved-seating-platform.md (flag context; Ticketmaster organizer-side tooling not publicly documented — limitation inherited).

## Product Observations

### Eventbrite (self-serve primary ticketing) — Evidence Layer A

From "Create and manage holds" and "What to do when tickets aren't on sale":

- **Hold definition**: "Creating a hold removes tickets from sale so that you can release them at a later time or give them to specific people." Holds are the product's named allocation primitive.
- **GA holds are quantity holds**: a hold is created with a name and a quantity under Tickets → Holds (general admission). Seat-based holds apply on reserved-seating events (assign specific seats/sections to a named, colored hold on the venue map).
- **Holds participate in sold-out arithmetic**: "If the number of held tickets is equal to or greater than the remaining tickets available, your event appears as 'Sold out.'" Availability is computed across holds, per-type quantities, and total capacity.
- **Release-to-public**: deleting a hold returns its stock — "After removing a hold, the seats become available for all buyers."
- **Gated access to held stock**: access codes (named, optional discount amount, ticket limit, start/end dates, ticket types) unlock held tickets for specific buyers; codes can be shared as links. Held tickets also sellable through the organizer app ("Codes & holds" at checkout) or manual orders.
- **Holds reporting**: a "Holds summary" download exists (related-articles link).
- **Two-level quantity model**: each ticket type has its own available quantity; the event has total capacity. Increasing a type's quantity cannot sell past total capacity; raising capacity reopens sales.
- **Per-order quantity rules shape stock**: a minimum tickets-per-order setting makes a type show "Sold out" when remaining stock is below the minimum.
- **Sales windows per type**: sales start / sales end dates per ticket type control when tickets are buyable; expired end dates produce "Sales ended."
- **Channel restriction per type**: sales channel setting — "Online only", "At the door only", "Everywhere."
- **Visibility gating**: hidden ticket types display "Hidden"; visible only via access code.
- **Pending orders hold stock**: tickets in incomplete orders display "Unavailable"; if the buyer doesn't complete, "the tickets will be returned to your available inventory after the registration time limit expires" — live reconciliation with automatic stock return.
- Product-specific: holds not available for recurring events; hold colors are organizer-side management aids, not attendee-visible.

### Spektrix (enterprise arts/venue ticketing) — Evidence Layer A

From "Introduction to Events and Instances":

- **Inventory structure**: Events (shows/runs/productions; also gallery entry, classes) contain Instances (dated occurrences). "Tickets are sold at the Event Instance level."
- **Capacity vs on-sale split documented verbatim**: each Instance holds "Overall maximum capacity and how many tickets to make available for sale" — two distinct inventory controls.
- **Ticket types carry channel semantics**: "Ticket Types are categories for your Tickets... can determine the channels that Tickets are sold through and how the Tickets can be delivered."
- **Channel-exclusive stock**: an Instance can be "a member's only performance with tickets that can only be purchased when calling the box office."
- **Price List = stock × price grid**: Ticket Types × Price Bands determine each ticket's price; seating-plan overlays assign bands to seats/areas.
- **Holds machinery — "Locks"**: the Lock Overlay "assigns Locks (also known as holds or kills) to specific Seats"; in Unreserved (GA) areas "the Lock Overlay allocates a number of Locks" — i.e., holds exist at quantity grain even where there is no seat map; locks "may prevent ineligible Customers from buying them."
- **Availability shaping via overlays**: Layout Overlay "manages the available capacity for the Instance" (e.g., hide seats when the house is reconfigured).
- **Instance updates affect sales**: "certain updates that can affect current and future sales"; bulk edits via the Bulk Instance Updater Tool.
- Supplementary Events hold separate capacity/pricing for linked upsell events — separate inventory containers.

### Purplepass (self-serve box-office ticketing) — Evidence Layer A

From "Setting venue capacity for your event" and the Ticket Creation & Management section:

- **Total ceiling**: "The venue capacity controls how many tickets you can sell; you can't sell past the number you put."
- **Per-class quantities with remainder logic**: each ticket type has a maximum quantity; "If the maximum isn't met, the remainder can be applied as a general admission to meet the venue's capacity" — per-type caps and the shared pool interact explicitly. Leaving the quantity blank lets the venue capacity govern.
- **Ticket-class surface**: dedicated help for COMP (complimentary) ticket types, VIP access passes, age-specific types, group/package types, user-defined custom types — the class structure is the stock structure.
- Section surface confirms box-office operations positioning (G2 "Box Office" badge) but no dedicated holds article found in sampled indexes — holds/allocation depth not verified for this product.

### Tessitura (enterprise arts/museums/attractions suite) — Evidence Layer B (Tier 2 marketing only)

From the "Ticketing & Admissions" feature page:

- **Presale/exclusive inventory**: "Automatically give members, donors, and other VIPs access to special pricing, pre-sales, and other exclusive inventory and benefits."
- **Automatic stock release**: "Automatically release unrenewed seats on your timeline, or release them one by one as needed" — subscription stock returning to the pool on operator-defined schedules.
- **Capacity control across surfaces**: "Streamlined tools to manage capacity for time blocks and entry points" (timed admission); "manage any seated and capacity-controlled venue"; "not-for-sale seat indicators"; pod seating.
- Operational detail (Controls model, allocation workflows) is gated behind Tessitura's support/training portal — no precise claims made.

### Victory Live / Victory Live One (reseller/rightsholder pole) — Evidence Layer A (product page, Tier 2 depth)

From the "Ticketing Inventory Management System" product page:

- **The exact leaf name appears as a product category** on the reseller/rightsholder side: "Manage the full lifecycle of your live event ticket inventory from a single, user-friendly dashboard... from acquisition to fulfillment."
- **Stock is acquired, not created**: "Sync your ticket listings directly from your POS or upload files"; "automatically importing event and barcode data so your inventory is ready to move." Inventory = owned ticket listings (event + seat/barcode data).
- **Multi-marketplace distribution with state sync**: "Distribute listings instantly to partner marketplaces like StubHub, SeatGeek, and Ticketmaster—keeping every price and status up to date"; pricing automated "across primary and secondary markets."
- **Settlement/reconciliation**: "manages order fulfillment, delivery, and reconciliation. Track the entire lifecycle—completed transfers, payments, and performance data."
- **"Monitor market and owned inventory performance"** — market inventory (others' listings) alongside owned stock.
- **Service modes**: Self-Service / Full-Service / Consignment Ticketing Solutions.
- Users: rightsholders, resellers, affiliate partners, travel agents, loyalty operators.

## Cross-product Comparison

| Aspect | Eventbrite | Spektrix | Purplepass | Tessitura | Victory Live |
|---|---|---|---|---|---|
| Unit of managed stock | ticket type × event (quantity); seats on reserved maps | Instance × Ticket Type × Price Band; seats/areas via plans | ticket type × event (max quantity) under a venue capacity | performance/zone/seat; timed-entry blocks (Tier-2 evidence) | owned ticket listings (event + seat/barcode) |
| Stock bounded by | per-type available quantity + total event capacity | Instance max capacity vs tickets made available for sale | venue capacity ceiling + per-type maxima | capacity per time block / venue (Tier-2) | acquisition volume |
| Partition primitive | named holds (quantity or seats) + access codes + hidden types | Locks ("holds or kills") per seat or per count; channel-bound ticket types; box-office-only instances | per-type maxima (remainder flows to GA); COMP/VIP classes | presales/exclusive inventory for member/donor segments (Tier-2) | acquisition tranches synced from POS/uploads |
| Per-tranche gating rules | who: code holders; when: code/date windows; where: sales channel setting | who: channel/eligibility; when: instance on-sale; where: online vs box office | class + quantity | segment membership (Tier-2) | marketplace placement + pricing rules |
| Release / return mechanics | delete hold → public sale; pending orders → returned to inventory after time limit | layout/lock overlays editable; bulk instance updates | quantity/setting edits | automatic release of unrenewed seats on a timeline (Tier-2) | delisting/status sync across marketplaces |
| Reconciliation surface | sold-out diagnostics (holds vs capacity vs quantity vs min-per-order), Holds summary | capacity-vs-available controls, sales-affecting updates | capacity + quantity fields | (gated) | fulfillment, delivery, transfers, payments, reconciliation |
| Sell loop ownership | in-product (its ticketing platform) | in-product | in-product | in-product | external (marketplaces do the selling) |

Reading: the primary-market samples all realize the inventory layer *inside* a ticketing platform. The standalone-product pole exists on the resale side. No standalone primary-market "ticket inventory management" product was found in the sampled evidence.

## Canonical Model (abstraction)

### L0 — Defining Invariant (three jointly-held structures)

1. **The admission stock as the unit of record** — a bounded quantity of admission rights attached to an event occurrence (or timed block), divided into ticket classes (types/price bands/zones), quantity-capped against an overall capacity; the stock is perishable — it expires with the occurrence and cannot be replenished. Remove → a price list or event page with no stock concept.
2. **The partition of stock into controlled tranches** — named held/gated/reserved blocks (holds, locks, channel-restricted or code-gated classes) each carrying eligibility rules: who may buy (channel, code, segment), when (on-sale windows), and how many. Releasing a tranche returns it to general availability. Remove → a single undifferentiated pile sold first-come — which is the bare selling mode of an Event Ticketing Platform, not inventory management.
3. **Live reconciliation of the stock** — as sales, pending orders, releases, refunds and setting changes occur, remaining availability per class updates against the ceiling, and the operator can see and steer it (sold-out diagnostics, holds summaries, quantity/capacity edits). Remove → a static allocation plan / spreadsheet.

Jointly-held is load-bearing: (1) alone = a price list with a capacity field; (2) alone = a reservation list with no stock behind it; (3) alone = a sales counter; (1)+(3) without (2) = plain selling (the ticketing platform's core — the boundary); (1)+(2) without (3) = an allocation plan nobody reconciles; (2)+(3) without (1) = control machinery over nothing.

### L1 — Common Mature Structure (standard, not definitional)

- Scheduled on-sale windows per ticket class (sales start/end; scheduled publish)
- Code-gated hidden inventory (access/promo codes, optionally with discounts, per-code limits and windows)
- Per-channel sales restriction (online / box office / at-the-door)
- Per-order min/max limits as stock-shaping rules
- Holds/locks reporting and summaries
- Scaling actions: increase/decrease per-class quantity, change capacity, extend/end sales
- Multi-date / multi-instance / recurring inventory views
- Seat-grain holds where a seat map exists (the intersection with Reserved Seating)
- Sales reporting by class/channel/instance

### L2 — Variant / Optional Structure

- Grain of partition: quantity-grain (GA) vs seat-grain vs zone-grain — both grains directly observed; neither is definitional
- Presale ladders (member/donor/fan presales; early-bird windows)
- Partner allocation: group sales blocks with deposits, consignment, promoter/agent allotments (deep operations documented only at marketing level in-sample — moderate claims)
- Timed-entry / entry-point capacity blocks (attractions/museums pole)
- The resale pole: acquired owned stock managed across marketplaces with dynamic pricing, automated transfers and settlement (Victory Live pole) — a different market reading of the same name
- Dynamic pricing / automatic price changes
- On-sale traffic machinery (waiting rooms) — observed only as a feature mention

### L3 — Vendor-specific (kept in Research Notes)

- Eventbrite: hold colors; "Holds summary" download; holds unsupported on recurring events; organizer-app "Codes & holds" checkout; manual orders do not process payment
- Spektrix: "Locks (also known as holds or kills)"; Layout/Price Band/Lock overlays; unreserved locks as counts; Supplementary Events; Bulk Instance Updater
- Purplepass: remainder-of-type-flows-as-GA behavior; COMP ticket types; "The Location" section naming
- Tessitura: automatic release of unrenewed seats on a timeline; member/donor presale automation
- Victory Live: Victory Live One suite; 1Ticket/DTI/Ticket Evolution portal lineage; StubHub/SeatGeek/Ticketmaster listing sync; consignment offering

## Rejected Findings (anti-overfitting)

- "Holds must be seat-based" — rejected: quantity-grain holds on GA events are first-class (Eventbrite GA holds; Spektrix unreserved lock counts).
- "Holds exist only for VIPs/comps" — rejected: holds serve presales, staff access, blocked sections, channel control, release-later strategies.
- "Inventory means owned stock" — rejected as universal: primary-market operators create stock they never own as goods; the reseller pole owns acquired stock. Both readings documented; neither promoted alone.
- "Dynamic pricing is definitional" — rejected: single-pole strength only (resale pole; automatic price changes elsewhere as optional).
- "The Type is a standalone product family" — rejected for the primary market on sampled evidence (realized inside ticketing platforms); the standalone family found is the resale pole. Claim scoped to the sample.
- Payment, refund, checkout, ticket issuance and scan-based entry — deliberately NOT definitional here: they are the Event Ticketing Platform's sell loop; this Type treats them as the consumers of the stock.

## Boundary Findings

- **vs Event Ticketing Platform** (processed): ticketing's L0 = ticketed event as sellable inventory + ticket as sold artifact + organizer sell lifecycle (orders→issuance→validation). This Type's L0 = the partition/control/reconciliation discipline over that stock (holds, gated classes, windows, channels, releases). Holds were already observed inside ticketing products as one capability — consistent: the layer is real and usually realized inside ticketing platforms. Keep-both RATIFIED from this side (capability-layer page, same pattern as reserved-seating-platform). Removal tests: remove the sell loop from a ticketing product → it becomes an inventory workbench (this Type); remove the partition/reconciliation machinery → it is a bare ticketing platform.
- **vs Reserved Seating Platform** (processed): seat-map grain vs ticket-class/quantity grain. Seat holds are the intersection; this leaf centers the class/quantity grain (quantity holds, capacity ceilings, per-class windows), with seat-grain holds as the seat-map variant. Flag DISCHARGED.
- **vs Ticket Resale Marketplace** (unprocessed sibling): the marketplace is the consumer-facing venue where resold tickets are exchanged; the reseller inventory pole (Victory Live) is the seller-side stock machinery feeding those marketplaces. This pass documents the pole as an adjacent market reading, not the leaf's center (which follows the two sibling flags' primary-market framing). The resale-marketplace flag "stands" for that pass, sharpened by this pole.
- **vs Inventory Management System (§10) / Retail Inventory**: goods stock is persistent, replenishable, physical, valued on hand; ticket stock is perishable, capacity-bounded, rights-based, worthless after the occurrence. Shared vocabulary ("inventory", "holds", "allocations") but different object worlds — not the same Type.
- **vs Attraction Ticketing / Attraction Management System**: place-admission inventory (open-date or timed place entry) vs occurrence inventory; timed-entry capacity blocks border the attraction pole.
- **vs Venue Management System**: spaces/booking/maintenance vs the admission stock of occurrences in those spaces.
- **vs Event Management Platform**: EMP's center is the event lifecycle + registration records; inventory partitioning appears there only as shallow ticket-type quantity settings.

## Historical / Market-Sample Check

Paper-era box office satisfies the L0 without any software: a printed ticket stock in numbered blocks, allotments set aside for agencies/outlets (allocation), house seats and press held at will-call (holds), an on-sale date per outlet (window), unsold stock reconciled and destroyed after the performance (perishability), a ledger reconciling sold vs held vs returned (reconciliation). Older regional practices (ticket manifests, outlet consignment) and platform-native box-office modules fit the same invariant. The definition therefore does not depend on cloud dashboards, access codes, or dynamic pricing — all era-current machinery sits in L1/L2. Check passed.

## Uncertainties

- The largest-scale allocation operations (major promoter/ticketing-company allocations, e.g. Ticketmaster organizer-side tooling) are not publicly documented (limitation inherited from the event-ticketing pass) — partner-allocation claims kept moderate.
- Tessitura operational depth (Controls model, allocation workflows) is gated; only Tier-2 feature-page evidence used, marked Layer B.
- Spektrix holds depth beyond Locks (e.g., dedicated hold codes/allocation reports) not fully explored; sampled article covers the core machinery.
- "No standalone primary-market family" is a sample-scoped finding (Eventbrite/Spektrix/Purplepass/Tessitura all bundle the layer); a small standalone vendor could exist outside the sample.
- Victory Live evidence is product-page level; exact sync/settlement behaviors unverifiable.

## Final Synthesis

Ticket Inventory Management is the stock-discipline layer of ticketed events: a bounded, perishable stock of admission rights, partitioned into controlled tranches with per-tranche eligibility (who/when/where), reconciled live as the stock is consumed, released, and returned. In the primary market the layer is realized almost entirely inside ticketing platforms (self-serve: named holds + access codes; enterprise: locks/overlays/channel-bound types/presale segments), so the leaf is documented as a capability-layer Type from its own lens — the same resolution pattern the reserved-seating pass ratified. The market also uses the exact name for the reseller-side acquired-stock management category (Victory Live One "Ticketing Inventory Management System"), which is recorded as an adjacent pole and flagged for the taxonomy owner. The definition passes the historical check: a paper box office with numbered stock, outlet allotments, will-call holds and a ledger satisfies the core with none of the modern machinery.
