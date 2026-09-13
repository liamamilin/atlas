# Research Notes — Online Marketplace

## Research Goal

Understand the **Online Marketplace** as an Application Type: the operated online market itself — one operator hosting many independent third-party sellers who sell goods to buyers through one shared venue. Resolve the pre-hung **cluster flag** from the marketplace-platform pass (2026-09-08) and the multi-vendor-marketplace pass (2026-09-08): `online-marketplace` + `multi-vendor-marketplace` appear near-duplicate; this pass must either recommend alias consolidation or ratify a generic-vs-pole seam. Additionally, discharge (from this side) the flags hung by the online-auction-platform pass (posted-price vs discovered-price seam, eBay straddle) and confirm the resale-marketplace pass's supply-identity seam.

## Initial Boundary

Hypothesis at start:

- The Type is a **venue** (the operated market with its real participants), not the software (Marketplace Platform, processed) and not seller-side tooling (Multi-marketplace Seller Platform / Marketplace Seller Management / Seller Portal, all processed).
- Domain anchor: **goods** (shippable items with price and stock), per the corpus convention fixed by the service-marketplace pass ("trades shippable goods with inventory and logistics" is that doc's stated seam with the goods-venue Types).
- Nearest siblings: Multi-vendor Marketplace (§05.02, processed — cluster flag), Service Marketplace (§05.02, processed), Marketplace Platform (§05.02, processed), Resale Marketplace (§05.19, processed), Online Auction Platform (§05.18, processed), Classifieds Platform (§05.03, processed 2026-09-07).
- Likely confusions: e-commerce storefront (1P), classifieds (unmediated), dropshipping (operator is seller of record), wholesale/consignment (stock ownership), auction (pricing mode vs Type).

**Cluster flag to discharge:** the multi-vendor pass found "no real-world 'online marketplace' fails to be multi-vendor (a one-vendor marketplace is a store), and multi-vendor venues are online by default" and proposed either (a) alias consolidation or (b) generic-vs-pole seam (online-marketplace as the broader register including auction-originated, C2C-heavy, resale-blended markets; multi-vendor-marketplace as the merchant-catalog pole). This pass researches the poles the multi-vendor pass could not reach (open-registration / C2C / auction-originated / vertical-curated venues) and records a position.

## Research Questions

1. Does the four-part core recorded by the multi-vendor pass (operated multi-seller venue / seller-authored sellable supply / mediated attributed transaction / operator economics + governance) hold on the open, auction-originated, and vertical-curated poles?
2. Who are the sellers — only professional merchants, or also individuals? How does the seller-entity spectrum behave?
3. What pricing modes exist inside venues (fixed / auction / negotiation / classified-ad formats), and are they definitional or variant?
4. How is the catalog structured — one product page per item shared by many sellers, or per-seller listings? Is the catalog model definitional?
5. How does money move: who processes payment, what fee forms exist (commission/referral/final-value/listing/subscription), and is in-path payment processing definitional?
6. What governance does the operator exercise (admission, catalog rules, performance standards, off-platform policing, disputes)?
7. What happens at the edges: returns, refunds, disputes, off-platform leakage attempts.
8. Where are the Type boundaries: vs multi-vendor sibling, vs software, vs services venue, vs resale, vs auction, vs classifieds, vs 1P retail, vs dropshipping, vs listings platforms?

## Representative Products

Selection logic: complement the multi-vendor pass's sample (Walmart Marketplace, Zalando Partner Program, Newegg Marketplace — all retailer-curated, application/invitation-gated) with the poles that pass could not reach: the dominant retailer-hosted horizontal, the open auction-originated venue, and a vertical curated venue. Multiple well-known venues could not be reached from the research environment (see Sources); substitutions per the network-restriction rule (1–2 failed attempts per source, then abandon).

**Researched (direct evidence this pass):**

1. **Amazon Marketplace** — the dominant retailer-hosted horizontal; third-party sellers offer beside the operator's first-party assortment; self-service registration with individual/professional selling plans; category referral fees; operator fulfillment program (FBA) beside seller-fulfilled (FBM). Tier: enterprise-scale retail operator, global multi-market. Evidence: official seller marketing/pricing/program pages (Tier 2).
2. **eBay** — the long-standing open horizontal consumer market; auction-originated with fixed-price and even classified-ad listing formats; individual and business sellers; insertion + final-value fees; managed payments; seller standards with fee consequences. Tier: open consumer venue, C2C + B2C. Evidence: official seller help center fees article (Tier 1).
3. **Back Market** — vertical curated marketplace for refurbished consumer electronics; operator explicitly disclaims the seller role; vetted professional refurbisher-sellers; condition grading; buyer-side order support routed to sellers with operator backstop. Tier: vertical pure-play, global. Evidence: official buyer help center (Tier 1).

**Cross-check context (sibling pass, not re-fetched):** Walmart Marketplace, Zalando Partner Program, Newegg Marketplace (research/multi-vendor-marketplace.md) — used only to confirm that the core recorded there also matches this pass's independent evidence, not as primary evidence for new claims.

**Attempted and abandoned (access failures):** Etsy (www.etsy.com/sell timeout; help.etsy.com article timeout — 2 failures), Mercari (help.mercari.com timeout; www.mercari.com/sell timeout — 2 failures), eBay help center first article attempt (error page; second URL succeeded). The pure C2C open-registration pole (Etsy/Mercari-class) therefore remains under-evidenced across passes; eBay's individual-seller evidence partially covers it.

## Sources

Research date: **2026-09-08**

Directly fetched this pass:

- Amazon — Sell on Amazon: pricing page (selling plans, referral-fee table, revenue calculator): https://sell.amazon.com/pricing
- Amazon — Fulfillment by Amazon program page (FBA definition, how-it-works steps, cost classes, FAQ): https://sell.amazon.com/fulfillment-by-amazon
- Amazon — How to sell overview (6-step selling loop; independent-seller share claim): https://sell.amazon.com/sell
- eBay — Seller Help, "Selling fees" article (insertion fees, final value fees, listing formats incl. auction/fixed-price/classified ad, extra final value fees for off-platform attempts and below-standard performance, dispute fees, international and currency fees, worked examples): https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822
- Back Market — Help Center home (marketplace self-description; buyer→seller contact model): https://help.backmarket.com/hc/en-us
- Back Market — "Does Back Market refurbish devices?" (operator is "a marketplace, not a seller or distributor"): https://help.backmarket.com/hc/en-us/articles/360010667240-Does-Back-Market-refurbish-devices
- Back Market — "Are some sellers better than others on Back Market?" (vetted seller population, ongoing performance assessment, condition grades): https://help.backmarket.com/hc/en-us/articles/360010667440-Are-some-sellers-better-than-others-on-Back-Market

Not reachable (limitations recorded; no claims based on these): Etsy (timeouts ×2), Mercari (timeouts ×2). Previously unreachable in sibling passes (not retried): Allegro, Mercado Libre, Faire, bol.com, Kaufland, eMAG, Fruugo.

## Product Observations

### Amazon Marketplace

Evidence layer: **A** (official seller marketing/pricing/program pages; Tier 2 — marketing site, not deep help center).

- **Self-service admission with a plan choice.** Two selling plans: Individual (per-item-sold fee; "list one product at a time"; static prices) and Professional (monthly fee; bulk operations, automated pricing, advertising, B2B, global selling, apps/APIs). "Just have a few items to sell? Sign up to become an individual seller." Registration is a documented step-by-step guide. [A]
- **Operator economics: referral fees.** "For every item sold, you'll pay a percentage of the total price or a minimum amount, whichever is greater" — category-based table with per-category percentages and tiered/portioned rates; selling-plan fees separate from referral fees; optional-cost layer (FBA, ads). [A] (percentages/prices = L3 vendor facts)
- **Seller-authored supply into a shared catalog.** "Find out how to match or create listings" — sellers either match their offer to an existing catalog product page or create a new one; pricing tools ("set competitive prices", Automate Pricing); inventory management content. The shared-product-page model (many sellers offering on one product detail page) is visible in the listing guidance. [A]
- **Fulfillment posture is a seller choice.** FBA ("outsource order fulfillment… we'll pick, pack, and ship orders, as well as handle customer service and returns"; send inventory into the operator's fulfillment network; FBA dashboard, restock tools) vs FBM ("deliver orders yourself"); a 6-step selling loop lists "select your fulfillment method" as a step. [A]
- **Growth services sold by the operator:** Amazon Ads, Brand Registry (brand-building/protection tools), A+ Content, Brand Store, Brand Analytics, Vine (review program), Transparency (authentication), Product Opportunity Explorer, New Seller Incentives (credits/bonuses). [A]
- **Ecosystem:** Selling Partner Appstore ("find apps and service providers"), Seller Central (the seller workplace), Seller University (education), Seller App. [A]
- **Multi-market and B2B:** Global Selling across ~25 country sites ("Amazon operates stores worldwide"); Amazon Business for business customers; supply-chain outsourcing programs (AWD, Amazon Global Logistics). [A]
- **Market-position claims (marketing figures, recorded not reproduced):** "More than 60% of sales in the Amazon store come from independent sellers — most of which are small and medium-sized businesses." [A, marketing]
- **Buyer side (indirect):** the venue is the operator's store; sellers' offers appear inside it; no direct buyer-help evidence fetched this pass. [A, indirect]

### eBay

Evidence layer: **A** (official seller help center fees article, Tier 1; single deep article — other help URLs error-walled this pass).

- **Two fee classes: insertion + final value.** Insertion fee charged at listing creation (monthly zero-fee quota per seller, more for store subscribers; non-refundable if unsold); final value fee charged when the item sells — "a percentage of the total sale amount, plus a per-order fixed fee"; "you don't pay a third-party payment processing fee" — the fee includes payment processing (managed payments). [A] (numbers = L3)
- **Multiple listing formats inside one venue.** Auction-style (starting price, optional reserve price, 1–10 day durations, optional Buy-It-Now), fixed-price (incl. "Good 'Til Cancelled" auto-renewing long-duration listings), and **classified-ad format** for specific categories (certain business/industrial, services, travel, real estate): flat insertion fee, **no final value fee** — i.e., the venue itself operates an unmediated listing format at its edges. [A]
- **Off-platform leakage is policed with the fee machinery.** "If you attempt to sell or buy items outside of eBay… we may charge the final value fee… even if the item doesn't sell" — contacting off-platform to complete a sale triggers the venue's per-sale claim anyway. [A]
- **Performance governance with fee consequences.** Seller standards: below-standard accounts incur an additional final-value-fee percentage the following month; high "item not as described" request rates in service metrics incur an additional percentage; a seller-level dashboard exists. [A] (numbers = L3)
- **Dispute machinery:** payment-dispute fee charged when the seller is held responsible under eBay policy; resolution center surfaced in site navigation; fee-credit policy for refunds/cancellations. [A] (numbers = L3)
- **Cross-border machinery:** eBay International Shipping program (operator-run international fulfillment); cross-border transaction fee; seller currency-conversion fee. [A] (numbers = L3)
- **Store subscriptions and promoted listings:** eBay Store monthly subscriptions (more free listings, store fees article referenced); Promoted Listings ads referenced as additional terms. [A]
- **Site navigation vocabulary (surface-level):** bids/offers, watchlist, purchase history, selling, messages, resolution center — the buyer and seller surfaces of one venue. [A, nav only]
- **Individual sellers are first-class:** the free-listing quota and per-item fee structure presuppose small/individual sellers; category fee tables include collectibles/used-goods categories (trading cards, coins & paper money, comic books, watches, sneakers) — the venue's condition mix spans new and pre-owned. [A]

### Back Market

Evidence layer: **A** (official buyer help center, Tier 1 — buyer-side perspective).

- **The operator names the structure and disclaims the seller role.** "Nope. We don't refurbish anything ourselves. Back Market is marketplace, not a seller or distributor. However, we work with some of the best tech refurbishers across the globe, they are the ones offering refurbished devices for sale on the marketplace." [A]
- **Gated, vetted seller population with ongoing performance governance.** "A global marketplace including more than 1,500 sellers of refurbished devices. Our rigorous vetting process means that only the best of the best can sell on our platform… we continue to assess their performance with mystery shopping, onsite visits, and our customers' reviews." [A] (counts = L3)
- **Catalog structured by condition grading.** "Every item is given a grade, from Fair to Premium, describing how the item looks. Every device has been tested and restored to perfect working condition according to industry standards." [A]
- **Per-seller attribution visible to buyers.** Help home: "For any question related to your order, the easiest way is to contact the seller from your customer account"; a related article asks "Can I shop items from a specific seller on Back Market?" (seller-level shopping surfaces exist). [A]
- **Operator as backstop.** "Back Market is a marketplace and our merchants are always on hand to answer any questions relating to your order. However, if you have already contacted the merchant and would still like to talk to a Back Market representative, you can directly contact us." Returns procedure initiated by contacting the seller. [A]
- **Seller-side warranty:** "a 1-year limited warranty offered by the seller." [A]
- **Adjacent programs:** Trade-in (device buy-back into the marketplace's supply), B2B services, warranty/protection plans, mobile-plan partners. [A, category nav]
- **Operator economics on this venue:** not directly evidenced in fetched pages (commission model not stated in buyer help) — recorded as market-context inference only, weakened strength. [A→weak]

## Cross-product Comparison

| Dimension | Amazon Marketplace | eBay | Back Market | (Sibling sample: Walmart / Zalando / Newegg) |
|---|---|---|---|---|
| Operator type | mass retailer (1P + 3P side by side) | pure-play open market (auction heritage) | vertical pure-play curator (refurbished electronics) | mass retail / fashion platform / category retailer |
| Admission | open self-service; plan tiers (individual/professional) | open self-service; free-listing quota; store subscriptions | rigorous vetting ("only the best of the best") | application / invitation-only |
| Seller entity spectrum | individuals → SMBs → enterprises/brands | individuals → businesses | professional refurbisher businesses | invited brands / professional merchants |
| Unit of supply | offer on a shared product page (match or create listing) | listing (auction / fixed-price / classified-ad formats) | graded refurbished-device listing | item/article/product upload |
| Seller sets price/stock | yes (pricing tools, automate pricing) | yes (starting/Buy-It-Now/reserve prices) | yes (sellers offer devices; grades describe condition) | yes |
| Fee form | referral fee per item sold (category table) + plan fees | insertion fee + final value fee (percentage + per-order fixed) | not directly evidenced (market context: commission) | referral/commission deducted per sale |
| Payment path | venue machinery (fees deducted; optional-cost layer) | managed payments — FVF includes payment processing | not directly evidenced | venue-designated processing; operator deducts and transfers |
| Fulfillment | seller choice: FBA (operator program) or FBM (seller-fulfilled) | seller-fulfilled; operator international shipping program; labels | seller (refurbisher) ships; operator customer-care backstop | seller-fulfilled default; WFS/ZFS/SBN operator programs |
| Condition mix | new dominant | new + used/collectibles core | refurbished-only (graded) | new dominant; refurbished/used segments |
| Governance | product restrictions, Brand Registry gating, listing policy | seller standards with fee penalties; off-platform policing; prohibited items | vetting + mystery shopping + onsite visits + reviews | platform rules, catalog standards, performance programs |
| Disputes | (not directly evidenced this pass) | payment-dispute fee; resolution center | buyer→seller contact; operator backstop | resolution machinery, operator backstop |
| Growth services | ads, brand tools, analytics, incentives | promoted listings, store subscriptions | trade-in, B2B, protection plans | ads, financing, insights, content services |
| Buyer surface | operator's store/app, unified with 1P | operator's site, unified | operator's shop, unified | operator's site/app, unified |

**Cross-product commonalities (Layer B, observed across this pass's 3 samples + sibling sample):**

1. One operator runs one venue where many independent third-party sellers sell goods; buyers face one storefront/catalog/search spanning all sellers under the operator's brand. [B; 3/3 this pass + 3/3 sibling]
2. Sellers author and maintain their own sellable supply — listings/offers with seller-set content, price, and stock/quantity — inside an operator-structured catalog. [B; 3/3 + 3/3]
3. A purchase creates an order bound to the specific seller's item; per-seller attribution carries through fulfillment, buyer communication, returns, and settlement. [B; direct this pass: Back Market buyer→seller contact; eBay order definition; Amazon order routing via FBA/FBM]
4. The operator holds a per-sale economic claim — a percentage-of-sale fee dominant (referral fee / final value fee / commission), computed by venue machinery per order; listing fees and subscriptions appear as additional or alternative layers. [B; 2/3 direct this pass + 3/3 sibling]
5. Admission is operator-controlled across a spectrum: open self-service (Amazon plans, eBay quota) ↔ application/vetting (Back Market) ↔ invitation (Zalando, sibling sample). [B]
6. Governance is structural: platform rules, catalog standards, prohibited/restricted items, seller performance standards with consequences (fee penalties, visibility, suspension). [B; eBay fee-penalty mechanism is the most explicit direct evidence]
7. Off-platform transaction attempts are policed — eBay charges its final value fee even for unsold items when sellers attempt off-platform sales. [A, single product; treated as the strongest direct evidence of a market-common leakage prohibition]
8. Operator-run fulfillment/returns programs exist beside seller-fulfilled logistics as an option (FBA; eBay International Shipping; sibling WFS/ZFS/SBN). [B]
9. Growth services are sold by the operator on top of the market (ads, brand tools, analytics, financing, subscriptions). [B]
10. Pricing modes are venue-configured formats, not the Type's identity: fixed-price dominant everywhere; auction/negotiation native in the auction-heritage venue; classified-ad format at the edges of one venue. [B]
11. Condition mix varies (new / used / refurbished) and is handled as catalog structure (grades, category conditions), not as a Type boundary. [B]

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

An Online Marketplace is an operated goods venue whose defining core is four jointly-held structures (independently verified this pass on the open, retailer-hosted, and vertical-curated poles; structurally identical to the core recorded by the multi-vendor pass):

1. **The operated market as one buyer-facing venue** — one operator hosts many independent third-party sellers behind a single shared storefront/catalog/purchase flow under the operator's brand. Remove many-sellers → the operator's own webstore. Remove the unified surface → hosted multi-shop territory.
2. **Seller-authored sellable supply** — each seller creates and maintains its own sellable listings (content, price, stock/quantity) published into the operator-structured shared catalog; sellers retain ownership of assortment and pricing. Remove → 1P retail or consignment.
3. **The mediated, seller-attributed transaction** — purchase happens on the venue and creates an order binding the buyer to the specific seller's item; the seller (or an operator-run program on the seller's behalf) fulfills; the venue's machinery carries completion — status, buyer–seller communication, returns, disputes — with attribution end-to-end. Remove mediation → classifieds. Remove attribution → 1P storefront with payout recipients.
4. **Operator market economics and governance** — the operator holds a per-sale economic claim on sellers' sales (percentage-of-sale fee dominant; listing/subscription fees as additional layers), computed by venue machinery per order; governs participation (controlled admission, platform rules, catalog standards, performance consequences); and stands as a party to the transaction. Remove → hosting surface / listing board.

Load-bearing check (all jointly held):

- 1 alone = hosting surface/shop directory. 2 alone = seller portal/PIM. 3 alone = checkout/OMS machinery. 4 alone = fee-billing back office.
- 1+2 without 3+4 = listing board. 1+3 without 2+4 = 1P store with attribution cosmetics. 2+3 without 1+4 = seller-side tooling. 2+4 without 1+3 = seller-management back office.
- Remove "goods" (supply = performed service) → Service Marketplace. Remove "the market is the product" (selling the machinery) → Marketplace Platform.

**Historical/market-sample check (§24):** the 1990s–2000s generation (auction-originated consumer markets, mall-style multi-seller sites, B2B trading exchanges) satisfies all four legs without any modern capability. In the earliest venues payment often settled directly between the parties while the venue billed fees separately — the invariant is therefore the **per-sale economic claim + governed completion**, NOT built-in payment processing. In-path payments/payouts (present in all modern samples: eBay managed payments, Amazon fee deduction, sibling venues) is the modern dominant realization — standard capability, not invariant. Paper-era market/mall operators (stall fees + commission + house rules) satisfy the structure abstractly. The definition does not depend on: web-only delivery, phone/app surfaces, reviews, operator fulfillment, or any specific fee percentage.

### L1 — Common Mature Structure

- Seller portal as the seller's workplace (registration, catalog, orders, earnings, performance) — Seller Central class. [B]
- Structured catalog intake: operator-defined categories, item specs/attributes, image standards, product identifiers, listing-quality tooling; the shared-product-page model (many sellers offering on one product page) as one catalog implementation. [B]
- In-path payment processing and seller payout/settlement administration (managed payments; fee deduction at sale). [B, modern venues]
- Reviews/ratings machinery tied to purchases. [B]
- Dispute/customer-issue machinery with operator backstop (resolution center class; buyer→seller contact with operator escalation). [B]
- Operator-run fulfillment and returns programs beside seller-fulfilled default (FBA class). [B]
- Performance standards/programs with consequences (fee penalties, tiers, visibility). [B]
- Growth-service layer sold by the operator: advertising, brand tools, analytics, financing/credits, subscriptions. [B]
- Ecosystem interfaces: APIs, app stores/partner programs. [B]
- Buyer-side unified purchase flow under the operator's brand (search, product pages, checkout, tracking). [B, indirect this pass]

### L2 — Variant / Optional Structure

- **Operator type:** retailer-hosted (3P beside 1P assortment) / pure-play horizontal / vertical curator.
- **Admission mode:** open self-service with plan tiers and quotas ↔ application/vetting ↔ invitation-only.
- **Seller entity spectrum:** individuals (C2C) ↔ small/medium businesses ↔ enterprises and invited brands.
- **Pricing modes:** fixed-price dominant; auction/negotiation as native formats in auction-heritage venues; classified-ad format at some venues' edges (flat fee, no per-sale claim, off-venue completion for niche categories).
- **Catalog model:** shared product pages with multiple seller offers ↔ per-seller listings/shopfronts; both can coexist.
- **Condition mix:** new dominant; used/collectibles segments; refurbished-only verticals with condition grades.
- **B2B vs B2C:** business buyers, commercial terms (Amazon Business class; B2B venues unfetched — market context).
- **Geographic scope:** single-market vs multi-market with per-country sites, cross-border shipping programs, currency handling.
- **Fee model mix:** per-sale percentage dominant; listing/insertion fees, store subscriptions, optional service costs as layers.
- **Fulfillment posture:** seller-fulfilled default vs operator-program share; operator-run international shipping.

### L3 — Vendor-specific (research notes only)

- Amazon: Individual plan $0.99/item sold vs Professional $39.99/month; referral-fee table (e.g., 8–15% class ranges, per-category tiered/portioned rates, $0.30 minimums); FBA cost classes (fulfillment, storage, aged inventory >181 days, returns processing, removal/disposal/liquidation, inbound placement); FBA New Selection program; New Seller Incentives ($50K-class credits); Brand Registry/Vine/Transparency/A+ Content/Brand Analytics/Product Opportunity Explorer; Selling Partner Appstore; "60%+ of sales from independent sellers" marketing claim; ~25 country sell-sites; AWD/Supply Chain Services; Revenue Calculator.
- eBay: 250 zero-insertion-fee listings/month (most categories); insertion fee $0.35 after quota; FVF ~13.6% up to $7,500 + 2.35% above (most categories), per-order fixed fee $0.30/$0.40; below-standard +6% FVF month penalty (+7% after 4 months); high item-not-as-described rate +5% (+6% after 4 months); $20 payment-dispute fee; 1.65% international fee; 3% seller currency-conversion fee; auction durations 1–10 days; reserve-price fee; classified-ad format $9.95/30 days for niche categories; real-estate notice fees; store subscriptions; promoted listings; eBay International Shipping; sneaker flat 8% ≥$150 class rule.
- Back Market: 1,500+ sellers; 1-in-3 applicant vetting pass rate; mystery shopping/onsite visits; Fair→Premium condition grades; 1-year seller warranty; trade-in program; B2B services; buyer→seller-first support model.
- Sibling pass (context): Walmart referral 6–15%, WFS, Pro Seller; Zalando invitation-only, ZFS/ZRS/ZSS/ZEOS, Connected Retail; Newegg commission table 8–15%, SBN, Seller Store.

## Rejected Findings

Considered and rejected for the defining core (each is common but not required to recognize the Type):

- **Built-in payment processing / payouts** — modern-dominant but historically absent (early venues billed fees; payment settled between parties). Standard capability.
- **Reviews/ratings** — a venue can operate without them (curation-only governance); common, not definitional.
- **Operator-run fulfillment programs** — optional seller choice everywhere observed.
- **One-product-page-shared-by-sellers catalog model** — an implementation (Amazon class); per-seller listing venues (eBay, Back Market, sibling sample) are equally in-type.
- **Auction pricing** — a listing format/variant, not the Type (the auction Type is reserved for price-discovery-centered products).
- **C2C individual sellers** — one end of the seller spectrum, not a requirement (retailer-curated venues admit only professional merchants and remain marketplaces).
- **"Online" as web-only** — the venue is operator-run digital commerce; app/mobile delivery is era-current packaging.
- **Open registration** — one admission mode on a spectrum, not definitional (vetted/invitation venues are marketplaces).
- **Condition mix (new-only)** — refurbished/used segments and refurbished-only verticals remain in-type.

## Boundary Findings

- **vs Multi-vendor Marketplace (§05.02 sibling, processed) — CLUSTER FLAG RESOLVED:** the four-part core recorded by that pass is independently confirmed on this pass's open (eBay), retailer-hosted (Amazon), and vertical-curated (Back Market) poles. No researched product is an online marketplace that fails the multi-vendor core; no researched product is multi-vendor without being an online venue. The two leaves name the same Application Type from different angles ("online" = surface angle; "multi-vendor" = supply-structure angle). **Position: recommend alias consolidation** at a taxonomy pass; until then both documents stand and cross-reference. This document is written as the generic venue register — its evidence base emphasizes the full seller spectrum (individuals → enterprises), pricing-mode breadth, and the venue/classifieds edge; the sibling document emphasizes the merchant-catalog evidence base. (Recorded in STATUS Boundary Issues.)
- **vs Marketplace Platform (§05.02, processed):** venue vs software — consistent with the corpus convention that venue leaves are the operated market. [direct, sibling convention]
- **vs Service Marketplace (§05.02, processed):** unit of supply — sellable good with price/stock vs performed service bound to a provider and time. Observed from inside a venue: eBay's classified-ad format (used for services/travel/real estate) carries a flat listing fee, no final value fee, and off-venue completion — the venue itself treats services as classified-style supply at its edges, confirming the seam. [A]
- **vs Resale Marketplace (§05.19, processed):** supply identity/custody — owner-listed one-off pre-owned items with seller-retained possession vs merchant stock. Back Market confirms the predicted blur from the marketplace side: professional refurbishers own and stock graded refurbished devices — merchant-catalog supply of pre-owned goods, in-type here as a condition variant; the resale Type remains the owner-listed one-off venue. eBay's used/collectibles core shows horizontal venues blending conditions. [A + sibling prediction confirmed]
- **vs Online Auction Platform (§05.18, processed) — flag discharged from this side:** pricing mode vs Type. In eBay (the straddle anchor) auction is one listing format beside fixed-price and classified-ad formats, and the fee machinery (final value fee on sale) treats formats uniformly; the venue's center is the mediated attributed sale, not price discovery. The auction Type remains reserved for products whose defining transaction is the competitive bid with a bounded close and award. [A]
- **vs Classifieds Platform (§05.03, processed):** mediation. The venue creates, records, and governs the transaction (order, payment machinery, disputes); classifieds hand off contact while the transaction completes between the parties. eBay provides direct two-sided evidence: the off-platform prohibition polices leakage with fee penalties (marketplace side), while the classified-ad format (flat fee, no FVF, off-venue completion) is the within-venue demonstration of the classifieds structure. [A]
- **vs E-commerce Platform / Online Store Builder (§05.01):** 1P vs multi-seller venue. Remove the independent seller population → the operator's own store. The same operator can offer both (the retailer-hosted pole runs 1P and 3P side by side; one sampled operator also markets a standalone online-store-builder product — different Type). [A]
- **vs Dropshipping Platform (§05.20, unprocessed):** seller of record — sellers sell under their own names with per-seller attribution here; in dropshipping the operator sells its own catalog and suppliers merely fulfill. [structural, consistent with sibling + platform passes]
- **vs Listings Platform / Listing Marketplace (§02.11 / §05.03, processed):** no checkout/transaction of record there — discovery-and-connection surfaces; consistent with those passes' own "vs Online Marketplace (checkout = drift)" seams. [consistent, sibling docs]
- **vs Shopping Search / Comparison / Deal Discovery (§05.05):** those aggregate and compare offers across venues; the marketplace transacts its own offers. [structural]

## Uncertainties

1. **Pure C2C open-registration venues under-evidenced:** Etsy and Mercari unreachable (timeouts ×2 each this pass; Allegro/Mercado Libre unreachable in sibling passes). The individual-seller pole rests on eBay's individual-plan/quota evidence plus market context; admission-mode and C2C-specific behaviors written with reduced strength.
2. **Buyer-side surfaces documented only indirectly** for Amazon and eBay (seller-side sources); Back Market is the only direct buyer-side source this pass. Buyer-surface description kept generic.
3. **Back Market's operator economics** (commission model) not directly evidenced — inferred from its marketplace self-description and market context; weakened strength.
4. **Order lifecycle state names** (cancellation windows, multi-seller cart splitting, A-to-z-class guarantee mechanics) not directly evidenced this pass; deliberately not asserted.
5. **B2B wholesale venues** (Faire/Alibaba class) unfetched across passes; B2B held as variant on market context.
6. **Regional horizontal venues** (Allegro, Mercado Libre) unreachable across passes; regional structure unverified.
7. **eBay evidence is deep on fees but single-article**; other eBay help URLs error-walled. Claims from it are marked accordingly.

## Final Synthesis

The Online Marketplace is the **operated online goods market itself**: one operator curates and governs a venue where many independent sellers — from individuals to invited brands — author their own sellable supply, buyers transact through one shared storefront with every order attributed to its seller, and the operator holds per-sale economics plus the governance machinery that makes the market a governed market rather than a hosting surface. Its four-part core (operated multi-seller venue / seller-authored supply / mediated attributed transaction / operator economics and governance) is era-stable, holds across retailer-hosted, pure-play, open-registration, auction-heritage, and vertical-curated poles, and is cleanly separated from the software leaf (Marketplace Platform), the services venue (Service Marketplace), the resale venue (Resale Marketplace, custody/supply-identity seam), the auction Type (pricing mode, not Type), classifieds (mediation), 1P retail/wholesale (stock ownership), and dropshipping (seller of record). The cluster flag with Multi-vendor Marketplace is resolved: the two leaves name the same Type; alias consolidation is recommended, with both documents standing as independent evidence bases (merchant-catalog pole vs generic register) until a taxonomy pass decides.
