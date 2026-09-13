# Research Notes — Deal Discovery Platform

## Research Goal

Understand the Deal Discovery Platform as an Application Type: its defining structure, how real products implement it, who uses it, and where its boundaries lie against neighboring Types — especially the three processed/unprocessed siblings in §05.05 Shopping Discovery (Shopping Search Engine, Shopping Comparison Platform, Product Discovery Application — all processed, all carrying boundary notes against this leaf), Online Marketplace / voucher-selling deal sites (Groupon), and price-tracking tools (camelcamelcamel / Keepa, not directory leaves here).

## Initial Boundary

- Leaf: **Deal Discovery Platform** (§05.05 Shopping Discovery; siblings: Shopping Search Engine, Product Discovery Application, Shopping Comparison Platform).
- Initial hypothesis: a consumer application whose unit of record is the **time-limited deal event** (discount, coupon code, cash back rate, sale, freebie) at an external merchant, aggregated across many merchants and surfaced through discovery surfaces (feed, categories, alerts), with a redemption handoff to the merchant rather than in-platform selling.
- Nearest neighbors: the three §05.05 siblings; Online Marketplace (venue vs router); Coupon functionality (a deal type, not a separate leaf); price trackers (adjacent, single-merchant).

## Research Questions

1. What is a "deal" in these systems — what does the deal record carry (merchant, terms, price, expiry, link)?
2. How do deals enter the system (user submission, editorial, automated, merchant-supplied)?
3. How are deals validated/curated, and how is decay (expiration) handled?
4. How are deals discovered (feed, categories, stores, alerts, extension, app)?
5. How does redemption work (link-out, code copy/auto-apply, cash back activation)?
6. What is the business model, and how does it shape structure (tracked outbound links, activation)?
7. Who are the users, including contributor roles in community variants?
8. Where are the seams vs the three siblings and vs marketplaces/voucher sellers?

## Representative Products

Chosen for market representation, documentation quality, and four distinct product philosophies:

1. **Slickdeals** — community-posted, community-voted deal feed with editorial validation (community-curation philosophy).
2. **RetailMeNot** — coupon/promo-code database plus cash back, editorially verified (coupon-database philosophy).
3. **Honey (PayPal)** — browser-extension-first, automated coupon application at checkout plus price tracking and rewards (checkout-automation philosophy).
4. **Rakuten Rewards** — cash-back-centric portal with per-brand rates (cashback-portal philosophy).

Boundary reference (not core sample): Groupon (sells vouchers — merchant of record), camelcamelcamel/Keepa (single-merchant price tracking).

## Sources

Research date: **2026-09-10**.

- RetailMeNot — homepage incl. FAQ, cash back explainer, extension/app sections: https://www.retailmenot.com/ (fetched directly)
- Honey — Help Center structure + "How does Honey make money?": https://help.joinhoney.com/ , https://help.joinhoney.com/article/30-how-does-honey-make-money (fetched directly)
- Rakuten Rewards — homepage incl. FAQ, payout, in-store/dining sections: https://www.rakuten.com/ (fetched directly)
- Slickdeals — direct fetch of slickdeals.net returned 403 (two attempts, abandoned). Evidence obtained via web search excerpts of official surfaces: https://slickdeals.net/corp/how-slickdeals-works , https://help.slickdeals.net/hc/en-us/articles/115004710094-How-Does-a-Deal-Become-a-Frontpage-Deal , https://help.slickdeals.net/hc/en-us/articles/360000551534-What-Is-a-Popular-Deal , homepage/browse excerpts, extension welcome page. Treated as Layer A (official text) but excerpt-mediated; precise numeric thresholds not claimed.
- Sibling research notes consulted for seams: research/shopping-comparison-platform.md, research/shopping-search-engine.md, research/product-discovery-application.md.

## Product A — Slickdeals (community-curation pole)

### Key observations (Layer A, excerpt-mediated)

- **Deal unit**: a deal post — item, sale price vs original price, % off, merchant, "Found by <member> <timestamp>", vote count, comment thread. Deal types include price drops, coupon codes, free items, app-only offers, PSAs.
- **Supply**: community members post deals ("The deals and coupons you see on Slickdeals are contributed by our community. It's what makes us different.").
- **Curation**: thumbs up/down voting; structured downvote reasons (not a good price / not a good product / not a good merchant / unable to replicate deal / incorrect information / spam / repost); "Popular" status is automatic once votes/clicks/views pass a threshold; **Frontpage** deals are popular deals validated by staff **Deal Editors** (sourced from the community) who research price history, customer reviews, expert reviews, availability, inventory, then author a highlighted post; the original member post remains viewable beneath.
- **Decay**: expiration is first-class — "10 More Expired Deals" surfaces; expired deals remain viewable.
- **Validity caveats**: deals that depend on price-matching or limited availability are labeled **YMMV** ("your mileage may vary"); PSA posts announce price drops/policy changes without being deals.
- **Discovery surfaces**: Frontpage feed, Popular Deals, category pages (e.g., PC Game Deals), store/coupon pages (Trending Stores: eBay, Newegg, Dell…), seasonal pages (Back to School, holidays), filters, search, forums.
- **Alerts**: deal alerts per store, category, or product/keyword, with instant notification on new posting; SMS alert option documented.
- **Companion surfaces**: browser extension, Android/iOS apps.
- **Monetization**: "Slickdeals is community-supported. We may get paid by brands for deals, including promoted items." — affiliate + promoted placements, disclosed.
- **Community layer**: comments under deals are a core part of the value (questions answered by other shoppers); moderation/mod alerts; account needed to vote, save, personalize.

## Product B — RetailMeNot (coupon-database pole)

### Key observations (Layer A, direct fetch)

- **Deal units**: coupon codes, promo codes, sales, free-shipping offers, cash back rates, and product deals (e.g., "Today's Top Deals — Presented by Amazon" linking to Amazon's deal section). Offer tiles carry merchant, offer text, type label ("Coupon code" / "Cash Back"), discount magnitude.
- **Scale + supply**: "coupons and promo codes for 6,000+ stores"; "Our team is constantly verifying the offers on our site"; merchant pages per store; user submission exists ("Submit a Coupon"); community section.
- **Verification**: "Confirmed by RetailMeNot" labels; a "working code promise" (app); sponsored tiles labeled "Sponsored".
- **Cash back**: "cash back offers for nearly 3,800 stores… activate the cash back offers you want to use, shop and check out as normal – we'll give you a percentage of what you spent back in your RetailMeNot wallet"; redemption via Venmo or PayPal; a minimum approved balance is required for redemption (precise figure observed: $5.01 — kept in Research Notes only).
- **Discovery surfaces**: homepage offer feed, Fall/seasonal deal pages, store browse, category browse (Airlines…Video Games), "My Offers" personalization ("Only the best codes and cash back offers from stores you browse and shop on"), app notifications, editorial blog ("The Real Deal").
- **Companion surfaces**: browser extension ("sources and automatically applies coupons and promo codes in real time while you shop online… also sources cash back offers"), mobile app with app-only offers.
- **Monetization**: "When you buy through links on RetailMeNot we may earn a commission." — outbound links are tracked redirect URLs (/out/O/…).

## Product C — Honey (checkout-automation pole)

### Key observations (Layer A, direct fetch of help center)

- **Surface philosophy**: browser extension first; the help center is organized around the extension, the mobile app, and checkout.
- **Deal machinery at checkout**: the extension finds and applies available coupon codes at the store's checkout (category structure: Getting Started, Store Support, Honey Checkout, Gift Card Deals, Honey Tips).
- **Price tracking**: **Droplist** — a dedicated help category for tracking items and price drops (mechanism details not fetched; category existence is the observed fact).
- **Rewards**: **PayPal Rewards** — a rewards program earning points when members "use Honey to find available savings or to activate PayPal Rewards"; points redeemable for gift cards (related-article titles observed: "Redeeming PayPal Rewards for Gift Cards", "Pending PayPal Rewards Points").
- **Monetization** (verbatim): "Honey makes commissions from our merchant partners. We earn these commissions when a member uses Honey to find available savings or to activate PayPal Rewards… we pass some of our earnings back to our members in the form of PayPal Rewards."
- **Merchant side**: "Partner with Honey… if I'm a merchant" — merchant partner program exists.
- **Scope**: works on Amazon and international sites (article titles observed).

## Product D — Rakuten Rewards (cashback-portal pole)

### Key observations (Layer A, direct fetch)

- **Deal unit**: a **cash back rate per brand** — "3,500+ brands with new Cash Back rates every day"; rates displayed on brand tiles (e.g., 12% Cash Back, Up to 17%, $5, "No Cash Back" shown too). Coupons/promo codes exist as a stacking layer.
- **Activation model**: activate Cash Back, then shop through the tracked path (site, extension, or app); "Once you make an eligible purchase, we'll add Cash Back to your account." No receipts needed online.
- **In-store extension of the model**: In-Store Cash Back — add individual offers via the app and pay with a card linked to the account; Dining — 5% at participating restaurants with a linked card (figures as displayed on the page).
- **Payout**: rewards sent on a quarterly cycle; choices include PayPal, points, or check; instant cash-out option via gift cards from 50+ brands; a welcome-boost bonus program exists. (Exact cadence/figures as displayed; treated as observed for this product, not generalized.)
- **Stacking**: "Cash Back stacks on top of sales and credit card rewards. It also stacks on top of coupons… Use the browser extension and we'll automatically apply eligible coupons at checkout."
- **Discovery surfaces**: brand/store pages, category pages, seasonal pages (Black Friday, Cyber Monday, Presidents Day), extension, app.
- **Monetization** (verbatim): "We partner with brands who pay us to bring them customers and we share a portion of that payment with our members in the form of Cash Back. That's it!"
- **Identity**: free member account; 17M+ members claimed (marketing figure — not load-bearing).

## Cross-product Comparison

| Dimension | Slickdeals | RetailMeNot | Honey | Rakuten |
|---|---|---|---|---|
| Unit of record | community-posted deal event (price drop / code / freebie / PSA) | coupon code / cash back offer / sale / product deal | coupon codes applied at checkout; Droplist price-drop watch; rewards-earning offers | per-brand cash back rate (+ stacking coupons) |
| Deal supply | user-posted | editorial team + user submission + merchant/product feeds | automated testing at checkout + merchant partners | merchant partner rates |
| Verification / decay | community votes + editor validation; expired-deals surface; YMMV labels | team verification, "Confirmed" labels, working-code promise | automatic code testing at checkout | rate shown per brand; activation required; rates change daily |
| Discovery surfaces | Frontpage feed, categories, stores, seasonal pages, alerts, forums, search | homepage feed, store/category pages, My Offers, app notifications, blog | extension popup at store/checkout, Droplist, app | brand pages, categories, seasonal pages, extension, app |
| Redemption | tracked link-out to merchant | code copy or extension auto-apply; activate cash back → tracked purchase → wallet → payout | auto-apply at checkout; rewards accrue on activation | activate → shop via tracked link/linked card → balance → periodic payout or gift cards |
| Money flows through platform? | no (referral only) | yes, in cash back variant (wallet → payout) | yes, in rewards variant (points → gift cards) | yes (balance → payout) |
| Business model | affiliate + promoted deals | affiliate commission | merchant commissions, partly shared as rewards | merchant commissions shared as cash back |
| Contributor role | central (posting, voting, commenting) | peripheral (coupon submission, community) | none | none |

### Evidence layers

- **Layer A (directly observed)**: all four products' structures above, from official pages/help centers (Slickdeals excerpt-mediated).
- **Layer B (cross-product commonality)**: deal event with merchant + terms + validity; multi-merchant aggregation; discovery surfaces organized around deals (feed/categories/stores/seasonal); deal alerts; expiration as a handled state; verification machinery (because deals decay and fail); outbound tracked links; free consumer side funded by merchant-side commissions; extension/app companion surfaces; account for personalization/redemption.
- **Layer C (canonical inference)**: the Type is a **deal-event-centric referral layer** between shoppers and many merchants: it does not sell, does not own catalog/checkout, and its defining loop is discover-deal → redeem-at-merchant.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

1. **The deal as unit of record** — a time-limited saving opportunity at an external merchant (price drop, coupon code, cash back rate, sale, freebie), carrying merchant, terms, and validity. Remove → product catalog or shopping search.
2. **Multi-merchant aggregation** — deals from many independent merchants collected in one place. Remove → a single store's own promotions page.
3. **Discovery surface over deals** — feed/browse/search/alerts organized around deal events. Remove → a raw database with no consumer surface.
4. **Redemption handoff to the merchant** — the platform does not sell; it routes the shopper to the merchant to redeem (link-out, code, activation). Remove → marketplace or voucher seller (merchant of record).

Jointly-held load-bearing: 1 alone = a merchant's promo page; 2 alone = a deal database/spreadsheet; 3 without 1+2 = a generic feed; 4 without 1–3 = a bare affiliate link farm; 1+2 without 3 = database nobody browses; 1+3 without 2 = single-store deal feed; 2+3 without 4 = a deals-themed media site with no redemption path.

### L1 — Common Mature Structure

- deal alerts (store/category/product-keyword subscriptions with notifications)
- verification machinery appropriate to the supply model: community voting + editor validation, editorial verification labels, automatic code testing, expiration tracking
- expiration as a first-class deal state (expired deals visible or filtered)
- coupon code as a deal type with reveal/copy or automatic application
- cash back as a deal type with activation, tracked purchase, accumulated balance, payout
- personal account with saved/personalized offers
- browser extension and/or mobile app as companion surfaces
- comment/discussion layer on deals (community variants)
- outbound tracked links with monetization disclosure

### L2 — Variant / Optional Structure

- curation philosophy: community-vetted vs editorial vs automated vs rate-based
- dominant deal type: price-drop hunting vs coupon codes vs cash back
- primary surface: website-first vs extension-first vs app-first
- in-store / card-linked deal redemption (cashback-heavy products)
- seasonal/event deal programming (Black Friday-class pages)
- regional community deal platforms (same structure, local merchant base)
- editorial content/blog as a supporting surface

### L3 — Vendor-specific (Research Notes only)

- Slickdeals: Frontpage/Deal Editor institution, Popular threshold, YMMV/PSA labels, reps, giveaways/Daily Draw, forum structure, classic/mobile/redesign site views.
- RetailMeNot: wallet with minimum approved balance ($5.01 observed), Venmo/PayPal redemption, "autostack" app claim, The Real Deal blog, Ziff Davis ownership.
- Honey: Droplist name, PayPal Rewards points, Honey Checkout, Gift Card Deals category, PayPal integration.
- Rakuten: quarterly "Big Pay Day" cadence, Bilt/Amex Membership Rewards options, welcome boost, Dining 5% at 22,000+ restaurants, SoFi-class non-retail offers, Ebates heritage.

## Vendor-specific Findings

See L3 above. None of these entered the canonical core. Notably, cash back wallet mechanics (payout cadence, minimums, redemption rails) are directly observed in two products (RMN, Rakuten) plus Honey's points analog — treated as common-in-cashback-variants, not definitional.

## Boundary Findings

### vs Shopping Comparison Platform (§05.05, processed — flag DISCHARGED)

Sibling's own note: "Deal platform's unit is the time-limited deal/offer event; here the unit is the stable offer record on a product." Confirmed from this side: none of the four sampled products aligns multiple sellers' offers on one canonical product for comparison; the deal event (often store-wide or category-wide, not SKU-anchored) is the unit. **Keep-both.**

### vs Shopping Search Engine (§05.05, processed — flag DISCHARGED)

Sibling's note: deal machinery there is a secondary layer; the unit of record is the offer/product result on an ingested corpus, retrieved by query. Confirmed: deal platforms are query-independent discovery surfaces over deal events; no query-first retrieval contract, no offer corpus keyed to products. **Keep-both.**

### vs Product Discovery Application (§05.05, processed)

Sibling's note: "unit is the deal/offer (discount, coupon, cashback event) vs the product record." Confirmed: product discovery browses product/brand records for inspiration; deal discovery browses saving opportunities. Overlap exists (both have feeds, saves, personalized surfaces) but the unit of record differs. **Keep-both.**

### vs Online Marketplace / voucher sellers (Groupon pole)

A deal platform never takes the customer's order or money for the underlying goods. Groupon sells vouchers (is merchant of record) → marketplace territory, not this Type. Rakuten/RMN hold cash back balances, but that is reward money from the platform, not payment for goods.

### vs price trackers (camelcamelcamel / Keepa — not directory leaves)

Single-merchant price-history tracking derives "deals" from price data on one merchant's catalog. It lacks multi-merchant aggregation and (typically) curated offer records. Treated as an adjacent tool family; price-drop watching appears *inside* deal platforms (Droplist, deal alerts) as a capability, not as the Type.

### vs merchant's own promotion surfaces

A single store's sale/coupon page has deal events but no multi-merchant aggregation — fails L0 leg 2. The aggregation is what makes it a platform.

### Historical / market-sample check

Older forms satisfy the core: early-2000s deal forums and deal blogs (community-posted deal events, link-out redemption, no extensions/apps/wallets). Extension-only products (Honey's original form) satisfy legs 1–4 without a content website. Regional community deal platforms satisfy with a local merchant base. The definition does not depend on the modern extension/wallet/app layer. **Pass.**

## Uncertainties

- Slickdeals evidence is excerpt-mediated (direct fetch 403); numeric vote thresholds and editor workflow details not asserted.
- Honey's Droplist and PayPal Rewards mechanics observed only at the level of help-center category/article titles; internal mechanics not asserted.
- Whether a pure "local deals" variant (e.g., newspaper-legacy coupon aggregators) fits was not researched with a sample; assumed to fit L0 but unverified.
- Groupon's current positioning was not fetched this pass; the voucher-seller boundary rests on its well-known model + the structural argument (merchant of record), not on fresh observation.

## Final Synthesis

A Deal Discovery Platform is the **deal-event-centric member of the Shopping Discovery family**: a consumer application whose unit of record is the time-limited deal at an external merchant, aggregated across many merchants, surfaced through query-independent discovery (feed, categories, stores, seasonal pages, alerts), and completed by a redemption handoff to the merchant — by link-out, coupon code, or cash back activation. The platform never sells: its money comes from merchants (affiliate commissions), and in cash back variants it shares part of that back to the shopper through an activation-tracked-purchase-payout loop. What distinguishes it from its three siblings is the unit of record (deal event vs product record vs offer-on-product vs query result); what distinguishes it from marketplaces is that it holds no transaction for goods. Curation philosophy (community, editorial, automated, rate-based) is the main variant axis, not the identity.
