# Resale Marketplace

## Overview

A **Resale Marketplace** is a venue where many independent sellers — mostly individuals — list previously-owned items themselves, and buyers purchase them through transactions the platform mediates: an in-platform order, in-platform payment, and platform-governed delivery and dispute handling. The platform acts as a neutral intermediary. It is not the seller, not a brand operating the supply, and does not take custody of the goods before sale.

The defining core is small:

```text
Independent seller (mostly an individual, self-listing)
└── Listing describing one specific pre-owned item in hand
    └── Purchase as an in-platform order (fixed price, offer, or bid)
        └── Platform-mediated payment, delivery, and dispute handling
```

This distinguishes the Type from its neighbors on every side: a venue without the in-platform transaction is a classifieds board; a venue trading primarily new goods from merchant catalogs is a general online marketplace; a venue where the operator takes custody of the items is consignment; a venue operated by a brand selling under its own identity is a brand-resale program.

## Users & Context

**Sellers** are typically individuals parting with items they own — wardrobe cleanouts, collectors, hobbyists upgrading gear — plus a smaller population of semi-professional resellers. The seller's work is: photograph and describe the item, price it, respond to questions and offers, ship (or hand over) the sold item, and get paid.

**Buyers** are consumers hunting for value, discontinued items, or specific brands and models that are no longer sold new. Their work is: search and evaluate, judge condition and authenticity from listing content, negotiate, pay through the platform, and raise problems within the protection window if the item disappoints.

**Platform operations** (trust & safety, support, payments) sit behind both sides: they verify accounts, adjudicate disputes, enforce item policies, and hold or release funds.

The context is consumer commerce, overwhelmingly mobile-app-first in modern products, with the web as a parallel surface. Occasional use is the norm on the seller side (most people list a few items per year); sustained semi-professional selling coexists with it.

## Core Model

### The defining core

Four properties. If any one is removed, the product stops being recognizable as a resale marketplace:

- **Open multi-seller venue with self-listing** — any eligible member can become a seller and create listings; supply is not curated or owned by the operator. Selling is a capability of membership, not a separate commercial relationship.
- **Pre-owned, one-off supply** — the venue exists to trade previously-owned goods; each listing describes one specific item in the seller's possession, with no inventory depth. Many venues tolerate new or handmade items alongside, but second-hand trade is what the venue is for.
- **Platform-mediated transaction** — the purchase is an in-platform order, and the buyer's payment flows through the platform, not directly to the seller. The platform records the order, collects the money, deducts its fees, and forwards the proceeds.
- **Neutral-venue posture** — the platform governs the trade between arbitrary buyer-seller pairs (rules, protection, disputes) without being a party to either side.

### The objects

- **Listing** — the unit of supply: photos, title, brand/model, size or specifications, **condition description**, price, and delivery terms. A listing is bound to one physical item. It is active until it sells, the seller removes it, or the platform removes it for policy reasons.
- **Seller account** — a member profile with selling capability: payment/payout setup (identity verification and a bank or payout account are required before or shortly after the first sale), listings, sold history, and a feedback record.
- **Buyer account** — a member profile with payment methods, purchase history, watchlist/favorites, and a feedback record.
- **Order (transaction)** — created when a purchase closes. It binds the buyer, the listing, the agreed price, and the delivery arrangement, and carries a status that advances from purchase through shipment/delivery to completed — or to canceled/refunded.
- **Payment and payout** — two distinct money movements. The buyer pays the platform at purchase; the seller later receives a payout from which platform fees are deducted. Funds typically sit inside the platform's machinery for a period between these events.
- **Delivery** — either shipping (with a platform-provided or self-arranged label and a tracking number entered on the order) or a local handover, which usually requires the buyer to confirm receipt on the order.
- **Messages** — a buyer-seller conversation attached to the listing or order: questions, size/condition checks, negotiation, shipping coordination.
- **Offers** — a structured price negotiation: a buyer proposes a price, the seller accepts, declines, or counters. Accepting a qualifying offer converts it into an order.
- **Feedback** — two-way ratings after a completed order, forming each side's public reputation.
- **Trust & safety layer** — the policies and machinery that make stranger-to-stranger trade viable: buyer protection, dispute resolution, prohibited-items rules, authenticity rules for branded goods, account restrictions, and reporting.

### One structure, many implementations

```text
Concept:            Who supplies the venue
Implementations:    individuals decluttering, collectors, semi-pro resellers,
                    small independent shops in some products

Concept:            Pricing
Implementations:    fixed price, buyer offers with counteroffers,
                    auction-style bidding (historically dominant in the pioneer product)

Concept:            Delivery
Implementations:    platform shipping labels, self-arranged shipping with tracking entry,
                    local meetup with in-app receipt confirmation

Concept:            Condition language
Implementations:    free-text description, structured condition scales (fashion, gear),
                    brand/model catalogs
```

## How It Works

### The seller loop

```text
Create account → set up payout account (identity + bank/payout details)
→ create listing (photos, description, condition, price)
→ publish (some products review listings or authenticate qualifying items first)
→ respond to messages and offers
→ item sells: order created
→ ship within the required window with tracking (or arrange local handover)
→ funds released after delivery/receipt confirmation (minus fees)
→ leave feedback for the buyer
```

Two seller-side deadlines recur across products: a window to ship after the purchase (one product observed at 7 days, after which the sale auto-cancels and the buyer is refunded), and a payout release tied to delivery. Products observed in research release funds a few days after the item shows as delivered or in transit, and may hold funds longer for disputes, investigations, or unusually high-value sales.

### The buyer loop

```text
Search / browse / follow sellers → open listing detail
→ evaluate photos, condition, seller reputation
→ buy at asking price, send an offer, or place a bid
→ pay through the platform
→ receive the item (or confirm a local handover)
→ inspect within the protection window
→ keep quietly, or report a problem to open a dispute
→ leave feedback
```

### How money moves

The payment is escrow-like in behavior, though products describe it differently: the buyer's money goes to the platform first; the seller's payout is released only after delivery-related conditions are met (tracking shows movement, delivery is confirmed, or the buyer confirms a local handover). The platform subtracts its fees from the seller's proceeds — and, in some products, charges the buyer a protection fee instead. If a refund is granted, fees are typically returned as well. Payout speed can vary with the seller's history, sales volume, and the item's price.

### The dispute path

When something goes wrong — item not received, materially not as described, inauthentic, wrong item — the buyer reports the issue within the product's protection window (measured from receipt; one product observed at 3 days). The platform adjudicates using evidence supplied by both sides (photos, statements, tracking) and can refund the buyer, deny the claim, or broker a return. Sellers have a corresponding channel when they believe a buyer is acting in bad faith.

### Capability tiers

**Defining core** — without these, not a resale marketplace:

- open multi-seller self-listing
- listings for specific pre-owned one-off items
- in-platform order
- platform-mediated payment
- neutral-venue governance of the buyer-seller trade

**Standard capabilities** — present in essentially all mature products:

- buyer-seller messaging tied to listings and orders
- offers / negotiation
- search, browse, favorites/watchlist, seller following
- shipping machinery: labels, tracking entry, ship-by windows
- seller payout machinery: verification, payout balance, delivery-linked release, holds
- fees (seller-side commission or buyer-side protection fee), returned on refunds
- two-way feedback and reputation
- buyer protection with a reporting window + a dispute/resolution surface
- prohibited/restricted item policies and offsite-transaction prohibition
- listing management: edit, remove/relist, vacation mode

**Common variants / optional** — depends on segment, region, and product:

- authentication or verification programs for high-risk categories
- auction-style pricing
- local-meetup-first or shipped-only postures
- price guides computed from sold history
- paid listing promotion with performance analytics
- structured condition vocabularies and brand catalogs
- marketplace-collected sales tax, financing, subscriptions for sellers

## Interfaces

### Marketplace feed / search

The buyer's entry surface. Combines keyword search with category, brand, size, and price filtering; commonly with personalization and followed-seller activity. Primary actions: search, filter, save, open a listing.

### Listing detail page

The evaluation surface. Photos, description, condition, brand/size fields, seller profile with feedback, price, and delivery estimate. Primary actions: buy now, make an offer, message the seller, save/watch, share.

### Listing composer (sell flow)

The seller's creation surface, usually wizard-like: photos (with quality guidance), title, category/brand, size or specs, condition selection, description, price (with product-specific pricing help), delivery setup. Primary actions: add photos, complete fields, set price, publish.

### Seller orders / sold view

The post-sale control surface. Lists active listings and sold orders with their states (awaiting shipment, shipped, delivered, paid). Primary actions: enter tracking, buy a shipping label, message the buyer, view payout status, refund.

### Purchases / orders view

The buyer-side record of orders and their statuses, delivery tracking, and the entry point for reporting problems within the protection window.

### Messaging

A conversation surface bound to listings and orders, carrying questions, offers, and shipping coordination; platform reminders (e.g., shipping nudges) commonly appear here too.

### Offers

A negotiation surface showing incoming/outgoing offers with accept/decline/counter actions and expiry.

### Wallet / payouts / earnings

The seller's money surface: pending funds, released earnings, payout account settings, fee breakdowns, and payout timing.

### Profile / feedback

Each side's public reputation: ratings, reviews, member since, sales count — the trust currency of stranger-to-stranger trade.

### Resolution / disputes

The adjudication surface: report an issue, upload evidence, view case status and outcome.

## Important Rules / Behaviors

- **Payment precedes payout, with a gap.** The seller is paid only after delivery-related conditions are satisfied, and the platform can hold funds for disputes or investigations. Seller trust in this machinery is what makes the C2C model work.
- **Ship-by windows and auto-cancellation.** Sellers must ship (with tracking) within a defined window after purchase; missing it auto-cancels the sale and refunds the buyer.
- **Protection windows are measured from receipt.** Buyer claims must be raised within a product-defined window after the item arrives; late claims are typically denied.
- **Offsite transactions are prohibited.** Taking payment off-platform (to dodge fees) forfeits protection for both sides and is actively policed — the clearest marker of the platform-mediated transaction as the product's center.
- **One item, one order.** A listing describes a single physical item; a completed sale ends the listing. There is no inventory pool behind it.
- **Condition and authenticity carry policy weight.** Branded goods must be authentic (replicas are prohibited; some products authenticate qualifying items before they go live), and condition misrepresentation is a protected ground for disputes.
- **Fees are symmetric with refunds.** When a sale is refunded, the platform's fees are returned with it.
- **Reputation gates participation.** Accumulated feedback and account standing determine visibility, payout speed, and continued membership; serious violations freeze or restrict accounts.

## Variants

- **Category verticals** — fashion resale (sizes, brands, authentication), gear/specialist resale (instrument condition scales, price guides), luxury resale (heavy authentication posture), general-goods horizontal venues, vehicle-adjacent listings.
- **Delivery posture** — local-meetup-first apps with in-app receipt confirmation, shipped-only fashion venues, and hybrids supporting both.
- **Pricing culture** — fixed-price venues, offer-heavy negotiation venues, and auction-heritage venues where bidding remains available.
- **Monetization model** — seller commission, buyer-side protection fee, free-listing limits, subscriptions, paid promotion; several models coexist in one product.
- **Seller population** — consumer declutterers vs semi-professional resellers vs small independent shops, with seller tooling depth scaling accordingly.
- **Social layer** — following, feeds, and editorial content are present in some fashion venues and absent in utilitarian ones.
- **Regional shapes** — regulated marketplace tax collection, regional payment methods, and jurisdiction-specific protection terms.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Online Marketplace / Multi-vendor Marketplace | primarily new goods from merchant sellers with persistent catalog inventory; the resale marketplace trades pre-owned one-off items listed by their owners |
| Classifieds Platform | listing board only: buyer and seller contact each other and arrange exchange themselves; no in-platform order/payment/dispute machinery |
| Recommerce Platform | brand-operated resale infrastructure: trade-in/take-back supply, selling under the brand's identity, value returned as credit/cash; the resale marketplace is an open neutral venue |
| Consignment Management Platform | operator takes custody of consignors' items and manages intake, pricing, and sale; sellers do not self-list or retain possession |
| Online Auction Platform | competitive bidding with time-boxed price discovery is the product's center; in resale marketplaces bidding is at most one pricing mode |
| Ticket Resale Marketplace | shares the name but trades dated, seat-bound event entitlements with transfer/validation mechanics — a different object world |
| Shopping Discovery / Deal Platform | aggregates and ranks offers elsewhere without holding the transaction |
| Payment Processing Platforms | the resale marketplace uses payment rails but is not itself payment infrastructure; its defining object is the listing/order |

The sharpest internal seam is with the Classifieds Platform: both present listings of used goods by owners, and classifieds-style meetups survive inside several resale marketplaces as a delivery variant. The line is the mediated transaction — order, payment, protection, and dispute handling inside the platform. Remove the mediation and the product becomes a classifieds board; add it and a classifieds board becomes a marketplace.

## Representative Products

- **Grailed** — menswear fashion resale; curated-but-open C2C with pre-publication authentication review
- **Reverb** — music-gear marketplace (new and used); strong payments, protection, and price-guide machinery
- **OfferUp** — local-first horizontal C2C app with in-app payments, offers, and promotion
- **eBay** — the historical anchor: auction heritage, now a broad fixed-price/bid venue; included as the older-pattern check for the definition
- **Vestiaire Collective** — international luxury fashion resale

Vinted, Depop, Mercari, and Poshmark are commonly cited members of this market but their official documentation could not be reached during research; they are named as market context only.

## Sources

Research date: **2026-09-07**

- Grailed Help Center — https://support.grailed.com/ (index; Selling category; "How do I sell an item?"; "When do I get paid?"; "Grailed's Purchase Protection"; Trust and Safety category)
- Reverb Help Center — https://help.reverb.com/hc/en-us (index; "I sold an item, what's next?"; "How long does it take to get paid?"; Buying/Selling/Accounts structure; Buyer/Seller Protection and Price Guide pages referenced from the index)
- OfferUp Support — https://help.offerup.com/ (index; Selling on OfferUp category: Selling Tips, Manage Your Listings, Payments & Refunds, Reports & Analytics)
- eBay Help — https://www.ebay.com/help/home (help home: Buying / Selling / Account / Returns & Refunds / Shipping & Tracking / Fees & Billing categories; Resolution Center navigation)
- Vestiaire Collective Help Center — https://faq.vestiairecollective.com/ (index)

> Sourcing limitation: official help centers for Vinted, Depop, Mercari, Poshmark, Swappa, Carousell, and Craigslist were unreachable from the research environment on 2026-09-07 (blocked or timed out), and eBay's article-level pages were behind a verification wall — only its help-home category structure was reachable. Claims in this document are drawn from the five reachable sources; precisely observed numbers (report windows, ship windows, payout timing) are stated as product-observed examples, not industry constants, and no details from the unreachable products are asserted.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
