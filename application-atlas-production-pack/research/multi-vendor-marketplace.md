# Research Notes — Multi-vendor Marketplace

## Research Goal

Understand the **Multi-vendor Marketplace** as an Application Type: the operated goods market itself — one operator hosting many independent third-party sellers who sell goods to buyers through one venue. Distinguish it from the software used to run such a venue (Marketplace Platform, already processed), from service venues (Service Marketplace, processed), from resale venues (Resale Marketplace, processed), and from adjacent commerce Types. Extract the smallest defining core, the standard capability layer, and the variant space.

## Initial Boundary

Hypothesis at start:

- The Type is a **venue** (the operated market with its real participants), not the software (Marketplace Platform) and not seller-side tooling (Multi-marketplace Seller Platform / Seller Portal, both processed).
- Domain anchor: **goods** (shippable items with stock/pricing), as fixed by the Service Marketplace pass ("trades shippable goods with inventory and logistics" is that doc's stated seam with this Type).
- Nearest siblings: Online Marketplace (unprocessed — cluster flag from the marketplace-platform pass), Service Marketplace, Resale Marketplace, Marketplace Platform.
- Likely confusions: e-commerce storefront (1P), classifieds (unmediated), dropshipping (operator is seller of record), wholesale/consignment (stock ownership).

**Cluster flag to discharge:** the marketplace-platform pass (2026-09-08) flagged that `online-marketplace` + `multi-vendor-marketplace` (both §05.02, both unprocessed at that time) appear near-duplicate (generic venue vs multi-seller venue), recommending alias consolidation or a generic-vs-multi-seller seam. This pass must record a position.

## Research Questions

1. What is the unit of supply, and who authors it (operator vs seller)?
2. What is the seller object, and how do sellers enter the venue (open registration / application / invitation)?
3. How does the buyer experience the venue — one catalog, or per-seller shops?
4. How is a transaction bound (buyer × seller × item), and what is attributed to the seller end-to-end?
5. Where does money move: who processes payment, who takes what, how do sellers get paid?
6. What governance does the operator exercise (admission, catalog rules, performance standards, rules of conduct, disputes)?
7. Fulfillment: who ships — and what operator-run fulfillment programs exist?
8. What happens when it fails: returns, refunds, disputes, customer issues.
9. What growth services does the operator sell around the market (ads, financing, insights)?
10. Where are the Type boundaries: vs software, vs services venue, vs resale, vs classifieds, vs dropshipping, vs 1P retail, vs wholesale/consignment?

## Representative Products

Selection logic: market representativeness + documentation reachability + different operator philosophies + different tiers/geographies. Multiple well-known venues could not be reached from the research environment (see Sources); substitutions were made per the network-restriction rule (1–2 failed attempts per source, then abandon).

**Researched (direct evidence):**

1. **Walmart Marketplace** — US retail giant extending its 1P assortment with third-party sellers; application-gated admission; referral-fee economics; operator fulfillment program (WFS). Tier: enterprise-scale retail operator. Evidence: seller-facing marketing/FAQ site + developer portal.
2. **Zalando Partner Program** — Europe's leading fashion "platform… marketplace model"; invitation-only admission; strong operator governance apparatus (Platform Rules, Code of Conduct, article-level catalog governance, return-rate management); operator logistics/marketing service suite. Tier: enterprise, EU, fashion-vertical. Evidence: partner portal + Partner University knowledge base.
3. **Newegg Marketplace** — horizontal tech marketplace operated by a category retailer; application onboarding; category-based commission table; operator fulfillment (SBN); dedicated seller storefronts. Tier: mid/multi-tier tech vertical. Evidence: seller-facing marketing/FAQ site.

**Partially researched:**

4. **eBay** — the long-standing horizontal consumer market (auction + fixed price, C2C/B2C). Direct evidence limited to one seller-help article (seller buyer-blocking controls, buyer requirements, resolution center) before bot-walling. Kept as a partial sample representing the open/auction-heritage pole; no precise claims based on it.

**Attempted and abandoned (access failures):** Etsy (help center timeout, seller handbook timeout, dev docs timeout), Faire (403), Mercado Libre (404 + transport error), Allegro (429 ×2), eMAG (transport error), Kaufland (transport error), bol.com (timeout), Fruugo (transport error), Walmart seller help center (JS-only), eBay help center beyond first article (verification wall), eBay developer docs (403), Walmart developer portal deep API pages beyond the portal overview (not attempted further after overview succeeded).

The reachable sample is skewed toward **operator-curated enterprise venues** (application- or invitation-gated). The open self-service registration pole (Etsy/Allegro/eBay-class) could not be directly documented in this pass; findings about admission modes are written with correspondingly calibrated strength.

## Sources

Research date: **2026-09-08**

Directly fetched:

- Walmart Marketplace — seller marketing site + FAQ (qualifications, fees, WFS, returns, programs): https://marketplace.walmart.com/ ; pricing page referenced at https://marketplace.walmart.com/pricing/
- Walmart Developer Portal — Marketplace Partner APIs overview (Items, Inventory, Orders, Pricing/Promotions, Ship with Walmart, WFS multichannel, sandbox, solution providers): https://developer.walmart.com/ , https://developer.walmart.com/us-marketplace
- Zalando Partner — portal home, Partnership models (Wholesale / Partner Program / Connected Retail), Discover Partner Program (University TOC: onboarding requirements, Platform Rules, Code of Conduct, logistics solutions ZFS/ZRS/ZSS/ZEOS, marketing services, accounting and fees, formal complaints): https://partner.zalando.com/ , https://partner.zalando.com/partnership/partnership-models , https://partner.zalando.com/university/pp/discover-partner-program
- Newegg Marketplace — seller marketing site + FAQ (application onboarding, category commission table, SBN fulfillment, seller storefront, SellerPortal/Seller Academy, RMA, payment/logistics partners, global program): https://www.newegg.com/sellers/
- eBay — one seller-help article (buyer blocking, buyer requirements, resolution center), fetched before bot-wall: https://www.ebay.com/help/selling/selling-basics/selling-basics?id=4082 (redirected to block-buyers article)

Not reachable (limitations recorded; no claims based on these): Etsy, Faire, Mercado Libre, Allegro, eMAG, Kaufland, bol.com, Fruugo, Walmart seller help center, eBay (beyond one article).

## Product Observations

### Walmart Marketplace

Evidence layer: **A** (official seller marketing/FAQ site; official developer portal).

- **Admission is gated by application.** Stated minimum qualifications: Business Tax ID(s) (SSN not accepted) or business license; documents verifying business name/address; "history of marketplace or eCommerce success"; products with GTIN/UPC GS1 company prefix; catalog compliance with a prohibited-products policy; fulfillment through WFS or "another B2C US warehouse with returns capability"; account with a compatible payment processor. [A]
- **Economics: referral fee deducted per completed purchase**, category/price-based, stated range 6–15%; "zero monthly or set up fees" positioning; "you pay for what you sell". [A] (percentage numbers = L3 vendor facts; not for final doc)
- **Seller-authored supply through a structured item model.** Developer portal: Items ("create and manage item listings"), Inventory ("keep your item inventory up-to-date"), Pricing, Promotions ("set promotional item prices… or call out comparison prices"), Orders. Item setup is spec-governed (item spec 5.0; MP_ITEM / MP_WFS_ITEM specs; fitment/vehicle-compatibility data for automotive). [A]
- **Fulfillment is seller-fulfilled by default with operator-run programs as options:** Walmart Fulfillment Services (WFS; outsourced storage/pick/pack/ship, delivery promises, multichannel solutions), Ship with Walmart (discounted labels), seller-fulfilled shipping settings, expedited delivery programs. [A]
- **Returns machinery:** in-store returns at US stores ("omnichannel"), Enhanced Returns (in-store & online). [A]
- **Performance governance:** Pro Seller program ("top performers stand out"), Listing Quality program, Repricer tool. [A]
- **Growth services sold by the operator:** Walmart Connect sponsored search ads (stated ROAS claim), SEM, post-purchase reviews program, review syndication, Brand Portal, working-capital solutions, Marketplace Wallet (receive and transfer funds), Customer Favorites insights, Local Marketplace, Solution Provider Hub (approved third-party tool ecosystem; app-store style OAuth connections after delegated-access keys retired), Seller Center portal, Marketplace Learn / Seller Academy education. [A]
- **Buyer side (indirect, from the same sources):** the venue is walmart.com — customers shop the operator's site/app where marketplace items appear alongside 1P items; weekly customer counts and store network cited as the venue's reach. [A, indirect]
- **Platform posture:** 1P supplier APIs exist in the same portal as 3P marketplace APIs — the operator runs both models side by side (1P wholesale + 3P marketplace). [A]

### Zalando Partner Program

Evidence layer: **A** (official partner portal; Partner University knowledge base).

- **The operator names its own model:** "Zalando is Europe's leading fashion platform with access to more than 60 million active customers across 25 European countries **through our marketplace model, the Partner Program**." Partner metrics across pages (50M / 60M active customers) are marketing figures — recorded, not reproduced in final docs. [A]
- **Three partnership models are explicitly distinguished by stock ownership and control:**
  - **Wholesale:** "We buy your assortments… As the legal stock owner, we take care of order and payment processing, logistics, and customer service." → 1P retail.
  - **Partner Program (the marketplace model):** partner "remain[s] in the driver's seat," sets own prices, "retain[s] ownership and control over assortment, branding, marketing and logistics"; steering via zDirect portal (analytics, business insights, peer benchmarks, tooling). → the multi-vendor pole.
  - **Connected Retail:** brick-and-mortar stores export inventory data from their merchandise-management systems; orders fulfilled from the store; "We process payments, deducting commission and transferring the revenue." → marketplace variant with store-stock integration; also the cleanest statement of venue money mechanics. [A]
- **Admission is invitation-only:** "To ensure our quality and brand-safety promises, we only invite brands that we know our customers will love. We ask for your understanding that we do not accept direct applications." [A]
- **Seller-side administration:** zDirect portal onboarding (accept invitation, account setup, legal details, per-market contact/carrier/VAT setup); article onboarding ("Onboard articles") with operator-specified attributes/silhouettes, image guidelines, article status codes to fix, prices and discounts; season switch and retagging timelines; assortment quality measures. [A]
- **Governance apparatus:** Platform Rules ("your legal reference for operating on our platform"), Code of Conduct, platform compliance requirements, GPSR (product-safety regulation) compliance content, formal complaint process for partners (explicitly separated from customer support). [A]
- **Fulfillment flexibility as a stated principle:** "Use your own logistics or save on shipping costs with Zalando Logistics Solutions (or a mix of both!)". Operator logistics suite: ZFS (end-to-end fulfilment for Partner Program partners), ZRS (returns service, Pure/Plus tiers), ZSS (cross-border shipping), ZEOS (multi-channel logistics). [A]
- **Returns are managed as a discipline:** "Assortment and return rates" optimization content; return-rate webinars; return-rate insights tied to assortment guidance. [A]
- **Growth services:** Partner Marketing Services (ZMS; creative/media/ad manager), Brand Homes (onsite brand pages), sales events, merchant financing (third-party-provided), profitability/market-expansion content. [A]
- **Account and money:** "Accounting and fees" as a University category; customer-issue resolution ("Resolve customer issues") as partner workflow. [A]

### Newegg Marketplace

Evidence layer: **A** (official seller marketing/FAQ site).

- **Admission by application:** "Apply now… start selling in 5 business days"; onboarding "between 3–7 business days"; "minimum qualifications" answered by pointer to application page; positioning "perfect for existing sellers that focus on PCs, tech and tech-related products". [A]
- **Economics: category-based commission table published openly** (rates 8–15% across ~30 categories; refurbished/used availability noted per category; different rates for international sellers; standard commission after new-seller rebate program). [A] (numbers = L3)
- **Seller-authored supply:** "Effortlessly upload your products using the tools available on our platform"; SellerPortal with listing optimization tools; SellingPilot (operator-provided multi-platform sync tool — listings/pricing/inventory across platforms). [A]
- **Fulfillment:** Shipped by Newegg (SBN) — "you store your products in our fulfillment centers, and we pick, pack, ship, and provide customer service"; SBN handles "returns and exchanges"; a-la-carte fulfillment/logistics services; label services. Seller-fulfilled shipping/returns otherwise. [A]
- **Dedicated seller storefront:** "Newegg Seller Store — showcase your brand and products in an immersive shopping experience… curate content… bring more repeat buyers." [A] — the venue exposes seller-level brand surfaces inside the unified market.
- **Seller operations surfaces:** SellerPortal + Seller Academy (knowledge base incl. referral fees, campaign types, integration providers), seller app (sales metrics, customer messages, **RMA requests**). [A]
- **Growth services:** sponsored ads (product/display/video), SEM, A+ content, promotions and on-site campaigns, deal-driven marketing, media services (livestreams, studio content), advertising credits for new sellers, Elite Seller program. [A]
- **Ecosystem:** third-party integration providers and payment partners; logistics partners; API integration advertised. [A]
- **Cross-border:** Newegg Business, Newegg Canada, Global Seller Program, China-specific rates via category manager. [A]

### eBay (partial)

Evidence layer: **A** for the single fetched article; otherwise market context only.

- **Seller-side controls over demand:** sellers can block specific members (entered by username; the article states up to 5,000 usernames) and set "buyer requirements" blocking by condition (e.g., buyers in countries the seller won't ship to, buyers with unpaid-item cancellations). [A, single article]
- **Dispute machinery exists:** the fetched article links to "举报买家问题" (report buyer problems) — "if you have a problem with a buyer because they did not follow our policies, tell us and we will investigate" — and the site nav exposes a Resolution Center surface. [A, single article]
- **Auction/bargain vocabulary is native** (bids/offers surfaces in navigation). [A, site surfaces only]
- Historical position (open C2C + fixed price + auction modes; later managed payments) is **market context, not direct evidence in this pass** — used only in the historical check with weakened strength.

## Cross-product Comparison

| Dimension | Walmart Marketplace | Zalando Partner Program | Newegg Marketplace | eBay (partial) |
|---|---|---|---|---|
| Operator type | mass retail (1P + 3P side by side) | fashion platform (1P wholesale + 3P marketplace + store-stock model) | tech-category retailer operating 3P market | horizontal consumer market (auction heritage) |
| Admission | application with qualifications | invitation-only | application | (not directly evidenced this pass) |
| Unit of supply | item listing (spec-governed, GTIN-based) | article (operator-defined attributes/images/seasons) | product upload (category-governed) | listing (item-level) |
| Seller sets price/stock | yes (pricing + inventory APIs) | yes ("set your own prices"; prices & discounts workflow) | yes (pricing sync tools) | yes (listing-level) |
| Fee form | referral fee deducted per completed purchase, category/price-based | commission deducted; accounting-and-fees administration | category commission table | final-value-fee heritage (market context) |
| Money path | designated payment processor account required; Marketplace Wallet | operator processes payments, deducts commission, transfers revenue | payment partners; payout tooling | (not evidenced this pass) |
| Fulfillment | seller-fulfilled default; WFS operator program; discounted labels | own logistics or operator suite (ZFS/ZRS/ZSS/ZEOS) or mix | seller-fulfilled; SBN operator program | (not evidenced this pass) |
| Returns | in-store + online returns programs | operator returns service; return-rate management | SBN returns/exchanges; RMA workflow | (not evidenced this pass) |
| Catalog governance | item specs, prohibited-products policy, listing quality | attributes/images/status codes, assortment quality measures, platform rules | category rules, listing optimization | listing policies (market context) |
| Performance governance | Pro Seller program | quality/brand-safety curation; benchmarks | Elite Seller program | seller standards (market context) |
| Seller identity in venue | seller sells alongside operator's assortment | invited brands; Brand Homes | dedicated Seller Store | member/seller identity |
| Growth services | ads, capital, wallet, insights | marketing services, financing, brand homes | ads, campaigns, content services | — |
| Buyer surface | operator's site/app, unified with 1P | operator's site/app across 25 markets | operator's site, unified | operator's site, unified |

**Cross-product commonalities (Layer B, observed in 3/3 strong samples unless noted):**

1. One operator runs one venue where many independent third-party sellers sell goods; buyers face one storefront/catalog/search spanning all sellers. [B]
2. Sellers author and maintain their own sellable supply — items/articles/listings with seller-set price and stock — inside an operator-defined catalog structure. [B]
3. Seller remains owner of assortment, pricing, stock, and (by default) logistics; the operator sells services around these. [B]
4. The venue records each purchase as an order bound to the specific seller's item; per-seller attribution carries through fulfillment, customer issues, returns, and settlement. [B]
5. Operator holds a per-sale economic claim — commission/referral fee deducted per sale as the dominant form, administered by venue machinery. [B]
6. Money path runs through the venue: payment processed via venue-designated machinery, seller revenue transferred after deduction. [B, modern venues]
7. Admission is operator-controlled and gated in the researched venues (application or invitation). [B]
8. Operator governance apparatus: platform rules/policies, catalog quality controls, seller performance standards/programs. [B]
9. Operator-run fulfillment/returns programs exist beside seller-fulfilled logistics as an option, not a requirement. [B]
10. Operator sells growth services on top (ads, financing, insights, content). [B]
11. Buyer experiences the venue under the operator's brand, with marketplace offers integrated alongside the operator's own assortment (retailer-operators) or as the whole surface (pure venues). [B]

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

A Multi-vendor Marketplace is an operated goods venue whose defining core is four jointly-held structures:

1. **The operated multi-seller goods market** — one operator hosts many independent third-party sellers, and buyers face **one venue** (shared catalog/search/purchase flow) spanning all sellers, under the operator's brand. Remove many-sellers → the operator's own webstore. Remove the unified venue → hosted multi-shop/multi-store territory.
2. **Seller-authored sellable supply** — each seller creates and maintains its own sellable catalog (items/listings/offers with seller-set content, price, stock) that populates the shared venue under operator-defined taxonomy and quality rules; sellers retain ownership of assortment and pricing. Remove seller-authored supply → 1P retail or consignment.
3. **The mediated, attributed transaction** — purchase happens on the venue: the venue creates the order binding the buyer to the specific seller's item; the seller (or an operator-run program on the seller's behalf) fulfills; the venue's machinery carries completion — status updates, buyer–seller communication, returns/disputes — with attribution to the seller end-to-end. Remove mediation → classifieds. Remove attribution → 1P storefront with payout recipients.
4. **Operator market economics and governance** — the operator holds a per-sale economic claim on sellers' sales (commission/referral fee as the dominant form; other fee models possible), administered by the venue's machinery; governs participation (gated admission, platform rules, catalog standards, seller performance consequences); and stands as a party to the transaction with rules binding both sides. Remove → hosting surface / listing board with no market business loop.

Load-bearing check (all jointly held):

- 1 alone = a hosting surface or shop directory. 2 alone = seller portal / PIM. 3 alone = checkout/OMS machinery. 4 alone = fee-billing back office.
- 1+2 without 3+4 = listing board / hosted shops without transactions. 1+3 without 2+4 = operator's own store with attribution cosmetics. 1+4 without 2+3 = governed hosting with no sellable supply and no orders. 2+3 without 1+4 = seller-side selling tooling. 2+4 without 1+3 = seller-management back office.
- Remove "goods" (supply is a performed service) → Service Marketplace territory. Remove "operated market is the product" (selling the machinery instead) → Marketplace Platform.

### L1 — Common Mature Structure

- Seller portal as the seller's workplace (onboarding, catalog, orders, earnings, performance) — zDirect / Seller Center / SellerPortal. [B]
- Structured catalog intake with operator-defined specs (attributes, images, identifiers, category rules) and listing-quality tooling. [B]
- Reviews / ratings machinery tied to purchases. [A: Walmart post-purchase reviews; market-common]
- Dispute / customer-issue machinery with operator backstop. [B; A: eBay resolution center article, Zalando resolve-customer-issues]
- Operator-run fulfillment and returns programs beside seller-fulfilled default (FBA-class pattern: WFS/SBN/ZFS). [B]
- Buyer-side purchase flow under operator brand: catalog search, product pages, checkout, order tracking. [B, indirect]
- Growth-service layer sold by the operator: advertising/retail media, insights/benchmarks, financing/capital. [B]
- In-path payment processing and seller payout/settlement administration. [B, modern venues]
- Performance-tier programs and seller services ecosystems (solution providers, integration providers). [B]

### L2 — Variant / Optional Structure

- **Admission mode:** invitation-only (Zalando) / application review (Walmart, Newegg) / open self-service registration (well-known shape of long-standing consumer markets — market context, not directly evidenced this pass; keep weakened wording).
- **Operator type:** retailer-hosted venue beside 1P assortment (Walmart, Newegg, Zalando-Partner-Program) vs pure-play venue where the market is the whole surface.
- **Pricing modes:** fixed-price dominant; auction/negotiation modes as variants (eBay heritage).
- **Goods condition mix:** new dominant; refurbished/used segments inside horizontal venues (Newegg categories; Walmart "Resold" pre-owned vertical).
- **B2B vs B2C:** wholesale/B2B venues with business buyers and terms (market context; Faire unfetched).
- **Geographic scope:** single-market vs multi-market with per-country onboarding/tax setup (Zalando 25 markets; Walmart "Sell from India"; Newegg global programs).
- **Seller entity spectrum:** invited brands / professional merchants (sample) vs small and individual sellers (open-registration venues).
- **Fulfillment posture:** seller-fulfilled default vs operator-fulfilled share; omnichannel returns (in-store) as an option.
- **Vertical depth:** horizontal (Newegg is category-leaning but broad) vs vertical fashion (Zalando) vs general (Walmart).

### L3 — Vendor-specific (research notes only)

- Walmart: referral-fee range 6–15%; no-monthly-fee positioning; WFS/SWW/Multichannel Solutions/Marketplace Wallet/Pro Seller/Repricer/Customer Favorites/Local Marketplace/Brand Portal; "280 million customers weekly / 10,900 stores / 4,600+ US locations" marketing figures; GTIN/UPC + business-tax-ID admission requirements; delegated-access key retirement (2026) and app-store OAuth migration; item spec 5.0.
- Zalando: zDirect; ZFS/ZRS (Pure/Plus)/ZSS/ZEOS; ZMS; Brand Homes; Partner University; invitation-only admission policy; 25 markets/50–60M customers figures; season switch/retagging; GPSR compliance program; Connected Retail tool (automatic shipping documents).
- Newegg: SBN; SellingPilot; Seller Store; Elite Seller; commission table (8–15%); 3–7 business-day onboarding; RMA app workflow; A+ content; new-seller rebate (6% effective first 90 days).
- eBay: buyer blocking up to 5,000 usernames; buyer requirements; resolution center (single-article evidence).

## Boundary Findings

- **vs Marketplace Platform (§05.02, processed):** software vs venue. The platform pass itself fixed the convention: venue leaves are the operated market; the platform is the software to operate it. This document is the venue; the platform's document explicitly cross-references both venue leaves. Consistent. [direct, from sibling doc]
- **vs Service Marketplace (§05.02, processed):** supply identity. There, the unit of supply is a performed service bound to a provider and a time; here it is a sellable good (item with price and stock, shippable). That doc's stated seam with this Type matches. [direct, from sibling doc]
- **vs Resale Marketplace (§05.19, processed):** supply identity and custody. Resale: pre-owned, one-off, owner-listed items, seller retains possession. Here: merchant catalogs of (predominantly new) goods. Horizontal venues carry resale segments as variants (Newegg refurbished/used; Walmart "Resold"); the seam blurs at the edges exactly as the resale pass predicted. [direct + sibling prediction confirmed]
- **vs Classifieds Platform (§05.03, unprocessed):** mediated transaction. In this Type the transaction is created, recorded, and governed on the venue (order, payment machinery, disputes); classifieds hand off contact while the transaction happens elsewhere. eBay's own resolution-center/report-buyer machinery and the payout-fee model evidence the mediation from the weak sample. Structural seam; recheck when classifieds is processed.
- **vs Dropshipping Platform (§05.20, unprocessed):** seller of record. Here the seller sells under its own name with per-seller attribution; in dropshipping the operator sells its own catalog and vendors merely fulfill behind the scenes. The marketplace-platform pass articulated this seam; consistent from the venue side.
- **vs E-commerce Platform / Online Store Builder (§05.01):** 1P vs multi-seller venue. Remove the independent seller population → the operator's own store. Zalando's Wholesale model ("we buy your assortments; we are the legal stock owner") is the 1P pole made explicit by the same operator that runs the marketplace model. [direct]
- **vs Wholesale/Consignment:** stock ownership is the seam — sellers retain ownership of assortment and stock in this Type (Zalando Partner Program definition); the operator takes legal stock ownership in wholesale. Connected Retail shows a hybrid (store-owned stock integrated into the venue) — a marketplace variant, not a different Type. [direct]
- **vs Online Marketplace (§05.02, unprocessed) — CLUSTER FLAG:** the two leaves name substantially the same market structure. No real-world product is an "online marketplace" that is not multi-vendor (a one-vendor marketplace is a store), and "multi-vendor" venues are realized online by default. The honest options are (a) alias consolidation, or (b) the generic-vs-pole seam: Online Marketplace as the broader venue term (including auction-originated, C2C-heavy, resale-blended markets) and Multi-vendor Marketplace as the merchant-catalog pole defined by the four-part core above. This pass documents the Type on its own evidence; the online-marketplace pass should ratify the seam or recommend consolidation. Recorded in STATUS Boundary Issues.
- **vs Seller-side leaves (Multi-marketplace Seller Platform / Marketplace Seller Management / Seller Portal):** opposite sides of the market; seller-side leaves manage selling across venues, this Type is the venue itself. [consistent with processed sibling docs]

## Historical / Market-Sample Check (§24)

- **Would older products fit?** The 1990s–2000s generation of venue sites (auction-originated consumer markets, mall-style multi-seller sites, B2B trading exchanges) satisfies the four legs without any modern capability: independent sellers authored listings into a shared venue; purchases were recorded as orders attributed to the seller; completion (feedback/disputes) was venue-governed; the operator held a per-sale economic claim (final-value/listing fees). Note: in the earliest venues the money path did not always run through the venue — payment could settle directly between the parties while the venue's fee was billed separately. The invariant is therefore phrased as the operator's **per-sale economic claim administered by venue machinery**, not as "payment processing must run through the venue". Built-in payment processing + payouts is the modern dominant realization (present in all three strong samples) — recorded as standard capability, not invariant.
- **Regional/platform-native analogs:** paper-era market/mall operators (stall fees + commission + house rules) satisfy the structure abstractly; national-domain venues (Allegro-class) would satisfy if fetched.
- **Era-current capabilities deliberately excluded from the core:** operator fulfillment programs, in-path payments/payouts, reviews, advertising/retail media, performance programs, cross-border tooling, mobile apps, AI features.

## Uncertainties

1. **Open-registration pole under-evidenced:** Etsy/Allegro/eBay-class self-service admission could not be documented this pass. Admission-mode variance is recorded, but the open pole rests on market context. Weakened wording used in the final document.
2. **Buyer-side surfaces documented only indirectly** (through operator/seller-facing sources). No direct buyer-help evidence fetched; buyer-surface description kept generic.
3. **Order lifecycle specifics** (state names, cancellation windows, multi-seller cart behavior) not directly evidenced in fetched pages; deliberately not asserted.
4. **B2B wholesale venues** (Faire) unfetched; B2B recorded as variant on market context.
5. **eBay evidence is single-article**; claims from it are marked product-specific and partial.
6. **Fee-model breadth:** commission-per-sale dominant in sample (3/3); subscription/listing-fee venue models are known market shapes (and were held non-definitional in the marketplace-platform pass) but were not directly evidenced in this venue sample.

## Final Synthesis

The Multi-vendor Marketplace is the **operated goods market itself**: one operator curates and governs a venue where many independent merchant-sellers author their own sellable supply, buyers transact through one shared storefront with every order attributed to its seller, and the operator holds per-sale economics plus the governance machinery that makes the market a governed market rather than a hosting surface. Its four-part core (operated multi-seller venue / seller-authored supply / mediated attributed transaction / operator economics and governance) is era-stable, holds for retailer-hosted and pure-play venues, and is cleanly separated from the software leaf (Marketplace Platform), the services venue (Service Marketplace), the resale venue (Resale Marketplace), 1P retail/wholesale (stock ownership), classifieds (mediation), and dropshipping (seller of record). The online-marketplace cluster flag is partially discharged from this side with a proposed seam test recorded for joint review.
