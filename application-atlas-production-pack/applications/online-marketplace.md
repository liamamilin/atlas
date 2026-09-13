# Online Marketplace

## Overview

An **Online Marketplace** is an operated online venue in which one operator hosts many independent third-party sellers who sell goods to buyers through a single shared storefront, while every offer and every resulting order remains attributed to the specific seller behind it.

The operator's product is the market itself: a governed place where buyers find an assortment no single seller could offer, and where sellers — from individuals to invited brands — reach demand they could not reach alone, under the operator's brand, rules, and commercial terms. The operator performs none of the selling. Sellers author their own supply, price and stock their own goods, and fulfill the orders they win; the operator owns the venue, the buyer relationship, the transaction machinery, and the economics that give it a share of every sale.

The defining core is deliberately small — four properties that make the Type what it is:

```text
Operator-run venue
└── Many independent sellers behind one shared buyer storefront
    └── Seller-authored sellable supply (listings / offers)
        └── Mediated transaction attributed to its seller
            └── Operator economics + governance
```

Everything else commonly associated with large marketplaces — built-in payment processing and payouts, reviews, operator-run fulfillment programs, advertising, performance tiers, cross-border programs — is standard machinery that mature venues add around this core, not what makes the venue a marketplace. Early marketplaces operated without most of it: venues billed sellers fees while payment settled directly between the parties, and the market was no less a market.

The boundary: if the supply belongs to the operator and sellers merely fulfill behind the scenes, it is first-party retail or dropshipping. If the unit of supply is a performed service rather than a sellable good, it is a service marketplace. If the transaction leaves the venue after contact, it is classifieds. If competitive bidding with a bounded close is the product's center rather than one pricing mode among several, it is an auction platform. If what is sold is the machinery to run such a venue rather than the venue itself, it is marketplace platform software.

## Users & Context

Four parties sit around the venue, with the operator in the middle:

**The operator** — a retailer, a vertical curator, or a pure-play market operator. It decides who may sell and what may be sold, structures the catalog, sets the commercial terms, operates the transaction machinery, and earns a share of each sale. In retailer-hosted venues the marketplace extends the operator's own first-party assortment; in pure-play venues the market is the operator's entire business. Operator staff govern through rules, controls, and programs rather than by handling merchandise — one refurbished-electronics venue states this plainly: the company is "a marketplace, not a seller or distributor."

**Sellers** — independent businesses and, in open venues, individuals who sell under their own names inside the venue. They maintain their own listings, set their own prices, manage their own stock, fulfill their own orders (or delegate to an operator-run program), receive their sales proceeds minus the operator's share, and answer for their performance. The seller population spans a wide spectrum: individual consumers selling a few items, small and medium-sized businesses, professional merchants, and vetted specialist suppliers. They are participants in someone else's venue, not departments of it.

**Buyers** — they experience only the venue: one storefront, one catalog, one search, one checkout spanning every seller. Most buyers do not distinguish — and need not distinguish — the operator's own assortment from sellers' offers unless the venue surfaces it.

**Supporting ecosystems** — approved tool providers, logistics and payment partners, and agencies that plug into the venue's interfaces to serve sellers at scale.

Typical contexts:

- a mass retailer's site and app where its own assortment sits alongside thousands of sellers' offers, each order routed to the seller behind it
- a broad open market where individuals and businesses list goods — new, used, and collectible — for other consumers and businesses, with several ways to price a listing
- a vertical venue where a curator admits specialist suppliers (for example, professional refurbishers of electronics), grades their goods into a common condition scale, and stands behind the market's quality
- a multi-market venue operating across countries with per-market onboarding and cross-border shipping programs

## Core Model

### The Defining Core

Four structures, in the order they build on each other. All four are held together; removing any one turns the product into a different kind of system.

**1. An operated venue over many independent sellers, presenting one face to buyers.** One operator hosts a population of external sellers and gives buyers a single surface — one catalog, one search, one purchase flow — spanning them all. The venue carries the operator's brand: buyers shop *it*, not the sellers individually. Yet the market is plural: the buyer always faces supply assembled from many independent parties. Remove the seller population and what remains is the operator's own webstore. Remove the single shared surface and what remains is a collection of hosted shops — hosting, not a market.

**2. Seller-authored sellable supply.** Each seller creates and maintains its own sellable catalog inside the venue: listings or offers with their own content, pricing, and stock, authored by the seller and published into the venue's shared catalog. The operator structures the catalog — categories, attributes, image standards, product identifiers, condition grades where relevant — and governs quality, but does not write the supply. Sellers retain ownership of their assortment and pricing. This authored supply is what buyers compare and what makes the venue a market rather than a buying office: remove it, and the operator is a first-party retailer with extra payout recipients.

**3. The mediated, attributed transaction.** A purchase happens on the venue and creates an order that binds the buyer to the specific seller's item. The seller fulfills — directly, or through an operator-run program acting on the seller's behalf — and the venue's machinery carries the transaction through its life: order status, buyer–seller communication, delivery, returns, and disputes. Attribution survives the whole journey: fulfillment, customer issues, refunds, ratings, and settlement all attach to the seller behind the order. Buyers feel this attribution directly — in mature venues, order questions route to the seller first, with the operator as backstop. Remove the mediation and the surface is classifieds. Remove the attribution and the "sellers" are cosmetics on a first-party store.

**4. Operator economics and governance.** The operator holds a per-sale economic claim on sellers' sales — a percentage-of-sale fee (commission, referral fee, or final-value fee) deducted as each sale completes is the dominant form, with listing fees and seller subscriptions appearing as additional or alternative layers — computed per order by the venue's machinery, not negotiated deal by deal. Around the money sits the governance: admission is operator-controlled, participation is bound by platform rules and catalog standards, seller performance is measured and carries consequences, and the operator stands behind the transaction as the party that sets purchase policies and adjudicates when things go wrong. Remove the economics and the venue is a hosting surface; remove the governance and it is an unmoderated listing board.

### One Structure, Many Implementations

The core is conceptual; venues realize it differently:

```text
Concept:   Seller-authored supply
Forms:     offers matched to shared product pages · per-seller listings
           in auction or fixed-price formats · graded refurbished-device
           listings · articles against operator-defined attributes

Concept:   Per-seller attribution
Forms:     orders routed to the seller behind each item · buyer→seller
           order support with operator escalation · seller-level
           storefronts and shops inside the shared venue

Concept:   Operator economics
Forms:     category-based referral fee deducted per sale · final-value
           fee (percentage + per-order amount) · listing/insertion fees
           with free monthly quotas · seller subscription tiers

Concept:   Admission
Forms:     open self-service registration with plan tiers ·
           application and vetting · invitation-only curation

Concept:   Fulfillment
Forms:     seller ships directly · operator fulfillment program
           (storage, pick, pack, ship, customer service on the
           seller's behalf) · operator-run international shipping
```

### Standard Capabilities

Mature venues consistently add this machinery around the core. It makes the market operable and attractive, but a minimal marketplace could exist without parts of it:

- **Seller portal** — the seller's workplace: registration, catalog and inventory management, order queue, earnings and settlement views, performance metrics, messages.
- **Structured catalog intake** — operator-defined categories, item specifications, image standards, product identifiers, condition grades, and listing-quality tooling.
- **Payment and settlement machinery** — buyer payment collected through venue-designated processing, the operator's share deducted per sale, and seller revenue transferred under the venue's rules.
- **Operator-run fulfillment and returns programs** — warehousing, pick-pack-ship, and customer service offered as an option beside seller-fulfilled logistics; operator-run international shipping programs.
- **Reviews and ratings** — purchase-tied evaluations accumulating on sellers and items; the venue's quality signal.
- **Dispute and customer-issue machinery** — structured paths for problems, with the operator as backstop and recorded consequences.
- **Performance governance** — seller standards and tier programs that shape visibility, fees, and standing.
- **Growth services** — advertising, brand-building and analytics tools, financing or credits, and seller subscriptions, sold by the operator on top of the market.
- **Ecosystem interfaces** — APIs, app stores, and partner programs through which tool providers serve sellers.

## How It Works

### Joining the venue

```text
Seller seeks admission
→ operator gates entry (open self-service registration,
  application with vetting, or invitation)
→ seller sets up in the portal: identity/business details,
  payout setup, per-market configuration where relevant
→ seller builds the catalog: listings created against the
  venue's structure (categories, attributes, grades)
→ operator governs publication: catalog standards,
  restricted-items rules, quality checks
→ seller goes live inside the shared venue
```

Admission is always operator-controlled, but its strictness varies widely: open venues let individuals register and start listing within free monthly quotas, while curated venues vet applicants and accept only a fraction. Either way, the seller enters a governed market, not a free hosting space.

### The selling loop

```text
Seller maintains listings (content, price, stock)
→ buyer discovers them in the shared catalog
→ purchase creates an order attributed to the seller
→ seller fulfills — ships directly, or hands the order to an
  operator-run fulfillment program
→ venue machinery tracks the order through delivery
→ returns and issues run through venue paths
→ the operator's share is deducted; seller revenue settles
→ performance is recorded: ratings, standards, standing
```

Everything the seller does happens inside the operator's structure — the same venue governs publication, the transaction, the money, and the consequences.

### The buying loop

```text
Buyer arrives at the operator's storefront
→ searches or browses one catalog spanning all sellers
→ opens a product page (seller attribution visible to varying degrees)
→ checks out once, under the operator's purchase policies
→ order routes to the seller behind the item
→ tracking, delivery, returns, and support run through the venue
```

The buyer's experience is continuous: one brand, one interface, one purchase flow — regardless of which seller owns the item.

### The money flow

```text
Buyer pays the venue
→ payment processed through venue-designated machinery
→ operator's per-sale share computed and deducted by venue rules
→ seller's revenue transferred per the venue's settlement terms
→ refunds and cancellations reverse the same path
```

The venue sits in the money path in mature products: the operator's claim is computed as each sale completes, and settlement to the seller runs through machinery the venue governs. This is the modern dominant realization, not the definition — early marketplaces billed fees while payment settled between the parties, and the per-sale claim plus governed completion is the invariant the money path serves.

### The governance loop

The operator watches the market through its controls: catalog quality, seller performance, buyer outcomes. Consequences are enforced structurally — listing takedowns, fee penalties, reduced visibility, suspension — and the fee machinery gives the rules teeth. The sharpest direct expression of this is the leakage rule: venues prohibit completing transactions off-platform, and at least one major venue enforces it by charging its per-sale fee even on attempted off-platform sales that never complete. Sellers, in turn, are typically given controls over their own side of the market.

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by venue.

### Buyer storefront

The venue as buyers see it — the operator's site and app.

- Purpose: turn demand into completed, attributed purchases.
- Typical information: unified catalog with search and filters, product pages, pricing and availability, delivery promises, reviews, condition grades where used.
- Primary actions: search, compare, buy, track, return, review, contact support.

### Seller portal

The seller's workplace — where nearly all of the venue's operational machinery lives.

- Purpose: let sellers run their business inside the operator's rules.
- Typical information: catalog and inventory states, incoming orders, earnings and settlement, performance metrics, messages and issues.
- Primary actions: register and verify, create and maintain listings, manage prices and stock, acknowledge and fulfill orders, handle returns and buyer issues, view earnings, respond to performance standing.

### Operator back office

The operator's governance surface — largely invisible from outside.

- Purpose: curate and govern the market.
- Typical information: seller pipeline and standing, catalog quality, order and dispute outcomes, fee and settlement configuration, market performance.
- Primary actions: admit or reject sellers, enforce catalog and platform rules, run quality and performance programs, adjudicate escalations, tune economics.

### Dispute / resolution surfaces

Structured paths for when a transaction goes wrong — buyer-reported issues, seller responses, operator adjudication as backstop — reachable from both the buyer and seller sides.

## Important Rules / Behaviors

**Sellers are external, self-administering parties inside a governed structure.** Sellers own their assortment, pricing, and stock decisions — the operator structures the catalog and governs quality but does not author supply. This tension (seller autonomy inside operator control) is structural: the same venue that gives sellers control also enforces standards, performance programs, and suspension.

**Attribution is end-to-end.** The seller attached to a listing at purchase time carries through fulfillment, communication, returns, ratings, and settlement. Venues may integrate sellers' offers seamlessly into one storefront — even onto shared product pages where several sellers offer the same item — but never dissolve who sold what.

**Admission is a control, not a formality.** Venues gate entry — by open registration under plan tiers, application and vetting, or invitation — and admission policy is an explicit instrument of market quality and brand safety. Who may sell is one of the operator's most consequential decisions.

**The operator is a party to every transaction without being the seller.** Purchase policies, payment handling, and dispute adjudication run under the operator's terms; both sides accept them as a condition of participating. When something goes wrong, the venue's machinery — not private arrangement between buyer and seller — is the path.

**Economics is per-sale machinery.** The operator's share is computed by the venue as each sale completes, category by category and order by order. Change the venue's terms and every subsequent sale splits differently; refunds must reverse the split, which is why returns are first-class venue flows rather than seller-side afterthoughts.

**Off-platform leakage is policed.** Completing a marketplace transaction outside the venue undermines the fee model, the buyer protections, and review integrity at once. Venues prohibit it, and the strongest enforcement observed binds it directly to the fee machinery: the per-sale fee can be charged even when the diverted sale never completes on-venue.

**Performance has consequences.** Venues measure seller quality — ratings, defect and return rates, shipping behavior — and bind consequences to standing, from fee penalties to reduced visibility to suspension. In some venues sellers also hold controls over demand, restricting which buyers may purchase from them.

**Fulfillment posture is a choice, not a definition.** Sellers ship their own orders by default; operator-run fulfillment programs are a standard option that some sellers adopt and others ignore. Either way the order remains the seller's.

**Pricing modes are venue-configured formats.** Fixed price dominates, but venues may natively support auction-style and negotiation formats — and even a classified-ad format at their edges, where a flat listing fee replaces the per-sale claim and completion happens off-venue. The presence of such edge formats does not change the Type; the venue's center remains the mediated, attributed sale.

## Variants

Common variants of the Type:

- **Retailer-hosted marketplace** — an established retailer opens its storefront to third-party sellers beside its own assortment; the venue shares the operator's brand, traffic, and often its logistics network.
- **Pure-play venue** — the market is the operator's entire surface rather than an extension of first-party retail.
- **Open horizontal venues** — broad markets with deep seller populations spanning individuals and businesses, historically auction- and negotiation-flavored pricing beside fixed prices, and condition mixes spanning new, used, and collectible goods.
- **Vertical curated venues** — a domain (fashion, electronics, refurbished devices) with specialized catalog structure, condition grading, and vetted specialist suppliers.
- **Admission spectrum** — open self-service registration at one pole, invitation-only curation at the other, application and vetting in between.
- **Seller-entity spectrum** — individual consumers at one pole; small and medium businesses; professional merchants and invited brands at the other.
- **B2B venues** — business buyers, commercial terms, quote or tiered pricing; the same core with commercial vocabulary.
- **Multi-market venues** — one venue operating across countries, with per-market onboarding, cross-border shipping programs, and currency handling.
- **Catalog model** — shared product pages where many sellers offer the same item, per-seller listings and shops, or both coexisting.
- **Fee-model mix** — per-sale percentage dominant; listing fees with free quotas, seller subscriptions, and optional service costs as layers.

A variant remains a variant while the four-part defining core still applies. Where the domain hardens its own machinery of record — performed services, freight, talent — it tends to become its own Application Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Multi-vendor Marketplace | near-synonymous sibling leaf naming the same goods-venue structure from the supply-structure angle ("multi-vendor") rather than the surface angle ("online"); the defining structure documented here is the same multi-seller goods venue |
| Marketplace Platform | the software used to build and run such a venue; this Type is the operated market itself, with its real sellers and buyers |
| Service Marketplace | same market shape, different unit of supply: a performed service bound to a provider and a time, not a sellable good with stock |
| Resale Marketplace | pre-owned, one-off, owner-listed items with seller-retained possession; here, seller-owned stock in merchant fashion — horizontal venues blur at the edges by carrying used and refurbished segments |
| Online Auction Platform | competitive bidding with a bounded close and award is that Type's center; here auction is at most one pricing mode beside fixed price |
| Classifieds Platform | listings with contact and transaction off-platform; here the transaction is created, recorded, and governed on the venue — some venues even offer a classified-ad format at their edges, which is the seam made visible |
| E-commerce Platform / Online Store Builder | runs one merchant's own store; remove this Type's independent seller population and it degrades into exactly that |
| Dropshipping Platform | the operator sells its own catalog and vendors merely fulfill behind the scenes; here sellers sell under their own names with per-seller attribution |
| Wholesale Commerce / B2B E-commerce | the buyer takes legal ownership of stock from the supplier; in a marketplace the seller retains ownership of assortment and stock until sale |
| Listings Platform / Listing Marketplace | discovery-and-connection surfaces over pooled listings with no checkout or transaction of record; here the venue transacts |
| Marketplace Seller Management / Seller Portal / Multi-marketplace Seller Platform | seller-side tools for operating across venues; this Type is the venue they sell on — opposite sides of the same market |
| Order Management System / PIM | record systems a venue may integrate; no seller population or market of their own |

The most consequential seams: with **first-party retail** (stock ownership — the operator buying and owning assortment ends the market), with **classifieds** (mediation — an unmediated transaction ends the venue's role), with the **auction Type** (price discovery as the center vs pricing mode), and with the **platform/software leaf** (the same market viewed as machinery rather than as the operated market itself).

## Representative Products

- **Amazon Marketplace** — the dominant retailer-hosted venue; third-party offers beside the operator's own assortment, open self-service registration with individual and professional selling plans, category referral fees, operator fulfillment program beside seller-fulfilled logistics
- **eBay** — long-standing open horizontal market with auction heritage; fixed-price, auction-style, and classified-ad listing formats; individual and business sellers; insertion and final-value fees; managed payments; seller standards with fee consequences
- **Back Market** — vertical curated marketplace for refurbished electronics; vetted professional refurbisher-sellers, condition grading, buyer→seller order support with operator backstop

The Type was additionally cross-checked against the retailer-curated venues documented in the paired sibling research (mass-retail, fashion-platform, and category-retailer venues with application- or invitation-gated admission); those venues satisfy the same defining core.

## Sources

Research date: **2026-09-08**

- Amazon — Sell on Amazon: pricing (selling plans, referral fees), Fulfillment by Amazon program, and how-to-sell overview: https://sell.amazon.com/pricing , https://sell.amazon.com/fulfillment-by-amazon , https://sell.amazon.com/sell
- eBay — Seller Help, "Selling fees" (insertion and final-value fees, listing formats, off-platform enforcement, seller standards, dispute and international fees): https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822
- Back Market — Help Center (marketplace self-description, seller vetting and performance assessment, condition grades, buyer→seller support model): https://help.backmarket.com/hc/en-us
- Sibling research cross-check: research/multi-vendor-marketplace.md (Walmart Marketplace, Zalando Partner Program, Newegg Marketplace; research date 2026-09-08)

> Sourcing limitations: several prominent open-registration venues could not be reached from the research environment on 2026-09-08 (Etsy and Mercari — repeated timeouts; Allegro and Mercado Libre unreachable in prior passes). The individual-seller pole is therefore evidenced mainly through the open venue's individual-seller machinery, and claims about pure C2C venues are written with reduced strength. Buyer-side surfaces are documented directly for one sampled venue only. Precise fee percentages, quotas, program names, and operational parameters observed in the sampled venues are intentionally not stated in this document; they are recorded in the paired Research Notes. Detailed observations, cross-product comparison, and the historical/market-sample check are in the paired Research Notes.
