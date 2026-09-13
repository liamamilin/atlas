# Research Notes — Resale Marketplace

Research date: 2026-09-07

## Research Goal

Understand what a Resale Marketplace is as an Application Type: the core object model, the seller and buyer workflows, how money and goods move through the platform, what trust machinery is definitional, and how the Type separates from its dense neighbor cluster (Online Marketplace, Classifieds, Recommerce Platform, Consignment Management Platform, Online Auction Platform).

Special obligation from STATUS.md: the processed `recommerce-platform` pass recorded a joint-review flag expecting the resale marketplace to be "an open multi-seller consumer venue (any seller self-lists to any buyer; platform is a neutral venue)" and noted that marketplace-side evidence (the Vinted/Depop/Poshmark class) had not been fetched in that pass. This pass must supply that marketplace-side evidence.

## Initial Boundary (working hypothesis before research)

- A resale marketplace is a venue where individuals sell pre-owned goods to other individuals, with the platform mediating the transaction.
- Nearest confusions: general online marketplace (merchant commerce with new goods), classifieds (listings without in-platform transaction), recommerce (brand-operated resale programs), consignment (operator holds and manages the inventory), auctions (bidding as the price mechanism).
- Unknowns going in: is in-platform payment definitional or merely dominant? Is "pre-owned" definitional when many such venues also allow new/handmade goods? What payout/protection machinery is common?

## Research Questions

1. What is the unit of supply? (listing — what does it describe, who creates it, what is its lifecycle?)
2. Who can sell? Is supply operator-curated, brand-affiliated, or open self-listing?
3. What happens at the moment of purchase? Is there an in-platform order object and in-platform payment?
4. How does money flow? Buyer payment → platform → seller payout: what are the stages, holds, and release conditions?
5. How does delivery work? Shipping labels/tracking vs local handover; who confirms receipt?
6. What negotiation modes exist? Fixed price, offers, bidding?
7. What trust machinery exists? Buyer protection, disputes, authentication, prohibited items, offsite-transaction policy?
8. How does the platform earn money, and does the model vary?
9. Where is the seam to Classifieds (no in-platform transaction), to Online Marketplace (merchant new-goods commerce), to Recommerce (brand-operated), to Consignment (operator-held inventory)?
10. Historical/regional check: do older and non-US products (auction-era eBay, classifieds-native products, regional C2C apps) still fit the definition?

## Representative Products

Selection logic: market representativeness across segments (fashion vs gear vs general goods), different product philosophies (curated fashion / vertical specialist / local-first horizontal / global pioneer), and documentation accessibility. Target products that could not be fetched are recorded below with their outcome — no claims are drawn from them.

| Product | Segment / philosophy | Access outcome |
|---|---|---|
| Grailed | menswear fashion resale; curated-but-open C2C; authentication-led | **Deep** — help center (Zendesk) fetched: index, Selling category, sell-flow article, payout timing article, Purchase Protection article |
| Reverb | music-gear marketplace; vertical specialist; strong payments/protection docs | **Deep** — help center fetched: index, "I sold an item, what's next?", "How long does it take to get paid?" |
| OfferUp | local-first horizontal C2C app | **Medium** — help center index + Selling category fetched |
| eBay | global pioneer; auction heritage; now broad | **Index only** — help home fetched (category structure); article pages blocked by bot verification |
| Vestiaire Collective | luxury fashion resale (EU) | **Index only** — help center index fetched, shallow |
| Vinted, Depop, Mercari, Poshmark, Swappa, Carousell, Craigslist | commonly cited market anchors | **Unreachable** (403 / timeout / transport error, abandoned after 1–2 attempts each) — market context only, no evidence drawn |

## Sources

Tier 1 (official operational documentation), fetched 2026-09-07:

- Grailed Help Center — https://support.grailed.com/ (index; /categories/…Selling; /articles/30282427510797 How do I sell an item; /articles/30298995312653 When do I get paid; /articles/30282097906189 Grailed's Purchase Protection; Trust and Safety category)
- Reverb Help Center — https://help.reverb.com/hc/en-us (index; /articles/40917640416027 I sold an item, what's next?; /articles/40917616326171 How long does it take to get paid?; Buying/Selling/Accounts category structure; reverb.com/page/reverb-protection and Price Guide referenced from index)
- OfferUp Support — https://help.offerup.com/ (index; Selling on OfferUp category: Selling Tips / Manage Your Listings / Payments & Refunds / Reports & Analytics)
- eBay Help — https://www.ebay.com/help/home (home page: category structure Buying/Selling/Account/Returns&Refunds/Shipping&Tracking/Fees&Billing + Resolution Center nav; deep articles blocked)
- Vestiaire Collective Help Center — https://faq.vestiairecollective.com/ (index only)

Unreachable (abandoned per retry discipline): vinted.com/help + help.vinted.com (403, transport error), depop.com/help + help.depop.com (403 ×2), help.mercari.com (timeout ×2), support.poshmark.com (transport error), swappa.com/faq (403), help.carousell.com (403), craigslist.org/about (403), eBay article pages (bot verification ×2).

## Product Observations

### Grailed (evidence layer A — direct)

Seller acquisition and listing flow ("How do I sell an item?"):

1. create account
2. click Sell
3. **connect a payment account before first listing can be published** ("Add Payment Details"; third-party payment processor, Stripe named in payouts docs)
4. create listing (official guide covers photo standards, sizing, pricing)
5. publish → **if the item qualifies for the digital authentication process, the listing is reviewed by Grailed's authenticator team before it goes on sale**; authenticators may request more photos and "reserve the right to reject listings for any reason"

Listing management: edit listing, listing deletion, "Why can't I see my new listing in the marketplace?", Listing FAQ.

Selling tools: Account Health; Offers for Sellers (buyer offers to seller); Vacation Mode; international-seller guidance; "Do I need to ship my sold item with tracking information?" (tracking requirement).

Payouts ("When do I get paid?"):

- funds released to bank **within 3 calendar days of the item showing as delivered** — "barring buyer disputes, Grailed investigations, or applicable laws requiring a payout hold"
- **7 calendar days from purchase confirmation to add tracking and ship, or the sale is automatically canceled and the buyer refunded**
- shipping reminders appear in the in-app Messages and Sold pages
- bank processing delays differ US vs international; holds possible while support researches an issue
- refund machinery: "How do I refund a buyer?"; "I've refunded a sale, how do I get the fees returned?" (fees return on refund); payment-processing-fee article; fees article
- "How do transactions qualify for faster payouts?" (payout speed can be earned)

Purchase Protection (buyer side, direct quote-level):

- applies if the item is **deemed inauthentic by Grailed**, **materially differs from description** (color, condition, fabric, measurement), or **wrong item sent**
- **issues must be reported within 3 calendar days from receipt**; late reports may be denied
- photographic evidence, written statements, documentation required
- seller-side safety handled case-by-case (suspected fraudulent buyer behavior)
- related: "My buyer was frozen for filing chargebacks" (chargeback handling)

Trust and Safety category: Fraud Policy; replicas/inauthentic items prohibited; **How does Grailed Verification work?** (verification program); report a bug/listing/user; "The listing looks suspicious"; **"What is an offsite activity warning?"** (moving the transaction off-platform is policed); bug bounty.

### Reverb (evidence layer A — direct)

Help center structure: Buying (Shopping / Managing purchases / Checkout), Selling (Getting paid / Managing orders / Listings), Accounts (settings / Trust and safety / community). Top buyer articles: how offers work; international buying guide; returns for buyers; **protection if item not received or not as described**; contact a seller; change shipping address; delayed/lost package; financing; how long to pay; tax charged on order. Top selling articles: verify seller information; connect bank account with Reverb Payments; "I sold an item, what's next?"; how long to get paid; returns for sellers; shipping labels; Safe Shipping; how to list; **music gear conditions guide**; fees.

"I sold an item, what's next?" (post-sale seller flow):

1. bank account on file (else funds sit as **Payout Balance** until an account is added / manually transferred)
2. gather weight & dimensions, get a shipping label — Reverb labels (US, with optional Safe Shipping), Packlink for EU/UK, or carrier-direct + **manual tracking entry** on the order page
3. track shipment on the Orders page — "if the tracking information on Reverb does not update, your earnings are not automatically initiated"
4. payment sent to bank; notification by email
5. leave feedback for the buyer

"How long does it take to get paid?" (payment lifecycle, direct):

- order created → **order verified & cleared for shipment** ("we secure payment by verifying buyer information") → **ship within 3 business days** → item in transit (repeat sellers) or delivered (first sale) or **"Marked as Received" for local pickup** (buyer performs the marking) → funds available for deposit → payout to bank (1–4 business days) or **Reverb Wallet** (immediate use)
- payout delay causes: wrong tracking, wrong bank info (bounces back 7–10 business days and is resent), **high-value items over $2,000 get an extra security check (3–6 business days after delivery)**
- payment timing "may vary based on existing feedback ratings, sales volume, Preferred Seller status, price of the item, and shipping destination"
- local pickup exists as a first-class flow ("Can I sell my order locally?")

Additional resources referenced from index: Reverb Buyer Protection page, Reverb Seller Protection page, **Price Guide** (sold-price comps), Seller Hub, shipping resources, sales tax information.

### OfferUp (evidence layer A — direct, index + category level)

Help structure: Getting Started; Your Account; Community Safety; Selling on OfferUp; Subscriptions; Buying on OfferUp; **Services; Jobs; Rentals** (category expansion beyond item resale); Rules & Policies; Legal & Privacy; Troubleshooting.

Selling category sections:

- Selling Tips: photos/videos, best practices, "How to create a great listing", selling a vehicle, "How to build trust as a new seller", **"Promote your items"** (paid promotion)
- Manage Your Listings: **"About free listing limits"**, update an item, "Why listings are removed"
- Payments & Refunds: **"Accept an offer"**, **"Getting paid"**, "How sellers handle refund requests", **"OfferUp's Commitment to Sellers"**
- Reports & Analytics: track item listing performance, view promotion results

Confirms: self-listing (with free listing limits), in-app offers, in-app payments and refunds, paid promotion, listing analytics, vehicles as a supported vertical, safety/trust content as a first-class category. Local-first meetup culture is the product's known posture (app store listing names buy/sell locally); direct doc evidence of local transactions sits at index level.

### eBay (evidence layer A — index only; articles blocked by bot verification)

Help home fetched; article-level pages returned a verification wall (2 attempts, abandoned). What the reachable layer establishes:

- category structure: **Buying / Selling / Account / Returns & Refunds / Shipping & Tracking / Fees & Billing**
- a **Resolution Center** is a first-class navigation destination (disputes)
- popular articles: guest buying; **"Item not delivered — get help"**; account restrictions and suspensions; account security
- My eBay surfaces in navigation: watchlist, **bids/offers**, purchase history, selling, saved searches/sellers, messages — confirming the buyer-side object set (watch, bid/offer, purchase record) at structure level
- user agreement + payments terms exist as governing documents

No precise eBay fee/policy claims are drawn (see Uncertainties).

### Vestiaire Collective (evidence layer A — index only, shallow)

Help center index: Buying / Selling / My Account (+ "Tradesy" as a merged help area — evidence of an acquired brand folded into one support surface); card/PayPal/Apple Pay/Google Pay/Klarna payment marks; multilingual support. No workflow detail reachable at index level. Used only as a market-structure data point (luxury fashion resale, international).

### Unreachable products

Vinted, Depop, Mercari, Poshmark, Swappa, Carousell, Craigslist: no official documentation reached. Widely-known market facts about these products (buyer-fee funding models, social feeds, auction/ BIN heritage, regional patterns) are **not** asserted as evidence anywhere in this research; they appear only as market-context names.

## Cross-product Comparison

| Structure | Grailed | Reverb | OfferUp | eBay (index) | Vestiaire (index) |
|---|---|---|---|---|---|
| Seller-side self-listing on a shared venue | yes | yes | yes | yes | yes |
| Pre-owned as venue identity (new tolerated adjunct) | yes (fashion) | yes/new+used (gear) | yes (used goods; +services/jobs/rentals expansion) | mixed at scale, resale roots | yes (luxury) |
| In-platform order + payment | yes (3rd-party processor; payment account required before first listing) | yes (Reverb Payments; Payout Balance; Wallet) | yes (Payments & Refunds category) | yes (payments terms; guest buying) | yes (payment marks) |
| Buyer↔seller messaging tied to listing/order | yes (reminders in Messages) | yes (contact a seller; photos in messages) | yes (implied by offer/refund flows) | yes (Messages nav) | n/i |
| Offers / negotiation | yes (Offers for Sellers) | yes (offers article) | yes (Accept an offer) | yes (bids/offers nav) | n/i |
| Shipping machinery (labels/tracking) | yes (tracking required; ship-window) | yes (labels US/EU/UK; manual tracking) | yes (shipping + refund handling) | yes (Shipping & Tracking) | n/i |
| Local handover variant | not observed | yes ("Mark as Received", local pickup article) | yes (local-first posture) | n/i | n/i |
| Seller payout machinery with release conditions | yes (release after delivery; holds; faster-payout qualification) | yes (in-transit/delivered/marked-received triggers; high-value extra check; wallet) | yes (Getting paid) | n/i (Fees & Billing category) | n/i |
| Buyer protection / dispute machinery | yes (Purchase Protection, 3-day report window; chargeback handling) | yes (protection article; Buyer/Seller Protection pages) | yes (refund requests; Commitment to Sellers; Community Safety) | yes (Resolution Center; item-not-delivered help) | n/i |
| Seller fees | yes (fees articles; fees returned on refund) | yes (fees article; deductions from earnings) | yes (free listing limits; subscriptions; promotion) | yes (Fees & Billing) | n/i |
| Listing promotion (paid) | not observed | not observed | yes (Promote + analytics) | n/i | n/i |
| Authentication / verification program | yes (pre-publication authenticator review; Verification program) | not observed (conditions vocabulary instead) | not observed | n/i | n/i |
| Two-way feedback | yes (community) | yes (leave feedback for buyer; negative-feedback article) | yes (build trust) | n/i | n/i |
| Domain condition vocabulary | yes (fashion sizing/condition guide) | yes (gear conditions guide) | no (general) | n/i | n/i |
| Price guidance / comps | not observed | yes (Price Guide) | not observed | n/i | n/i |

n/i = not observable from the reachable evidence layer. "Yes" rows supported by direct fetched documentation.

Stable commonalities across the deep sample (Grailed + Reverb + OfferUp, mutually consistent with the eBay index): self-listing, in-platform order+payment, buyer-seller messaging, offers, shipping/tracking machinery, payout machinery with delivery-linked release, buyer protection + dispute handling, two-way feedback, fees.

## Abstraction Levels

### L0 — Defining Invariant

1. **Shared multi-seller venue with seller-side self-listing** — any eligible member can become a seller and create listings; the platform does not own, curate, or take custody of the supply.
2. **Pre-owned items as the defining trade** — the venue exists to trade previously-owned goods between parties; listings describe one specific item in hand (one-off supply), with new/handmade items tolerated as adjuncts in some products.
3. **Platform-mediated buyer-seller transaction** — purchase happens as an in-platform order with in-platform payment; the platform stands between buyer and seller for money movement and record-keeping.
4. **Neutral-venue posture** — the platform is an intermediary of record, not the seller, not a brand selling under its identity, not the operator of the supply.

Removal tests: remove self-listing/possession-retention → consignment/recommerce territory; remove pre-owned identity → generic online marketplace; remove in-platform transaction (buyer and seller arrange exchange themselves) → classifieds; remove neutrality (brand-operated supply) → recommerce.

§24 historical check: auction-era eBay (bidding on used goods, in-platform payment) fits; regional C2C apps with meet-up + in-app payment (OfferUp's local-first posture; Reverb's local-pickup "Mark as Received") fit — so **shipping is not definitional**, only the mediated transaction is. Products where payment happens off-platform (classifieds boards) do NOT fit — the line holds.

### L1 — Common Mature Structure

- buyer↔seller messaging bound to listing/order
- offers/negotiation (buyer offers, seller counter/accept)
- search/browse/discovery, favorites/watchlist, following sellers
- shipping machinery: labels, tracking entry requirement, ship-by windows
- payout machinery: payment-processor onboarding (KYC-style), payout balance/wallet, release conditioned on delivery/tracking/receipt, holds for disputes, payout-speed differentiation
- fees + refund-fee symmetry; free listing limits; paid listing promotion
- two-way feedback/ratings
- buyer protection program (report window after receipt, evidence, platform adjudication) + dispute/resolution surface
- trust & safety: prohibited/restricted items, authenticity rules for branded goods, account restrictions, fraud policies, reporting, **offsite-transaction prohibition**
- listing lifecycle management: edit, delete/relist, vacation mode

### L2 — Variant / Optional Structure

- monetization model: seller commission vs buyer-side protection fee vs listing limits/subscriptions vs promotion fees (varies by product)
- category vertical: fashion (sizing/brand fields, authentication), gear (condition vocabularies, price guides), general (none), vehicles (OfferUp)
- pricing modes: fixed price / offers / auction-style bidding (eBay heritage)
- authentication/verification programs for high-risk categories (Grailed pre-publication review; luxury consignment-adjacent models)
- delivery posture: shipped-only vs local meetup vs both
- price guidance from sold history (Reverb Price Guide)
- category expansion beyond resale (OfferUp: services/jobs/rentals)
- social layer: follows, feeds, editorial (Depop/Grailed culture — market context; not directly evidenced this pass)
- regional/currency/tax handling; marketplace-collected sales tax (Reverb tax article)

### L3 — Vendor-specific (research notes only)

- Grailed: digital authentication review before publication (authenticator team can reject); "Grailed Labels"; Account Health metric; Vacation Mode; 3-day payout release + 7-day ship window numbers; faster-payout qualification; chargeback-frozen-buyer support flow; A/W '26 Grail Sale promo event
- Reverb: Reverb Wallet; Safe Shipping add-on; Packlink EU/UK label partnership; Preferred Seller status; >$2,000 high-value extra security check (3–6 business days); first-sale vs repeat-sale payout distinction; Payout Balance manual transfer
- OfferUp: free listing limits; Promote/boost with results analytics; Commitment to Sellers; Services/Jobs/Rentals category expansion
- eBay: Resolution Center naming; guest checkout; Money Back Guarantee naming (name observed in URL/navigation context only — index-level); Managed Payments details unverified
- Vestiaire Collective: Tradesy brand folded into one help center

## Vendor-specific Findings

See L3. None of these are promoted into the canonical description. Fee percentages, exact windows, and named programs from single products stay here.

## Boundary Findings

1. **vs Online Marketplace / Multi-vendor Marketplace (§05.02)** — both are multi-seller venues with in-platform transactions. Seam: supply identity and shape. Online marketplace = primarily new goods from merchant sellers with persistent catalog/SKU inventory; resale marketplace = primarily pre-owned, one-off items listed by their owners with no inventory depth. Test: if the venue's defining supply is new-goods merchant catalogs → Online Marketplace even if some used items appear (large horizontal marketplaces blur at the edges; the Type is defined by what the venue exists to trade).
2. **vs Classifieds Platform / Listing Marketplace (§05.03)** — classifieds are listing boards where buyer and seller contact each other and arrange exchange themselves; the resale marketplace inserts the platform between them: order object + in-platform payment + delivery/receipt tracking + dispute machinery. Direct supporting evidence from this pass: Grailed polices offsite transactions ("offsite activity warning" — completing payment off-platform is a violation), OfferUp and Grailed both ship in-platform payments/refunds machinery. Craigslist itself could not be fetched (limitation), so the classifieds side of the seam rests on structural inference, stated at reduced strength.
3. **vs Recommerce Platform (§05.19 sibling; resolves the joint-review flag from the recommerce pass)** — confirmed with marketplace-side evidence. Recommerce = brand-side program infrastructure (trade-in/take-back, brand-scoped curated P2P with listing approval, selling under the brand's identity, value returned as credit/cash). Resale marketplace = open venue: onboarding is generic member onboarding with no brand affiliation; sellers keep possession until sale; the platform's trust machinery protects arbitrary buyer-seller pairs rather than a brand. Structural test holds both ways: remove the brand-operator relationship and open listing to any seller → resale marketplace; impose a brand operator and brand-scoped supply → recommerce.
4. **vs Consignment Management Platform (§05.19 sibling)** — consignment: the operator takes custody/management of consignors' items (intake, photography, pricing, payout of proceeds); the seller does not self-list or retain possession. Resale marketplace: seller retains possession and self-lists. Authentication-intake programs inside resale marketplaces (Grailed) are a trust feature, not consignment custody.
5. **vs Online Auction Platform (§05.18)** — auction centers competitive bidding with time-boxed price discovery; resale marketplace centers the listing + mediated purchase, with bidding merely one pricing mode where present. eBay straddles historically (auction heritage → broad fixed-price venue); treat auction as a pricing-mode variant of this Type, with the dedicated auction Type remaining for auction-mechanics-centered products.
6. **vs Ticket Resale Marketplace (§26 sibling)** — shares "resale marketplace" naming but the traded object is a dated, seat-bound, event-scoped entitlement with transfer/validation mechanics; a different object world. Separate leaf stands.
7. **vs Shopping Discovery / Deal platforms (§05.05)** — discovery surfaces aggregate and rank offers without holding the transaction; the resale marketplace is the transaction venue itself.

## Uncertainties

- Sample is US/EU-weighted and documentation-availability-biased: the consumer-C2C class most cited in market discussion (Vinted, Depop, Mercari, Poshmark) could not be fetched. Their well-known distinguishing traits (e.g., buyer-fee monetization, social feeds) are NOT asserted anywhere.
- eBay: index-level evidence only (article pages bot-blocked). No precise eBay policy/fee/payout claims made anywhere; eBay is used as a structural anchor (Resolution Center, bids/offers, fees/billing categories) and historical check.
- Vestiaire Collective: index-level only; used as a luxury-segment data point.
- Exact protection-window and payout-window numbers stated in the final document are limited to those directly observed (Grailed 3-day report window; Grailed 7-day ship window; Grailed/Reverb delivery-linked release), and even these are presented as product-observed examples, not industry constants.
- Whether the social/cultural layer (follows, editorial, drops) is common enough across the class to be called standard could not be verified from fetched docs; it is kept as market context.
- Auction-mode prevalence inside the modern sample is unverifiable beyond eBay's navigation ("bids/offers"); kept as a variant with reduced strength.

## Final Synthesis

A Resale Marketplace is a neutral, multi-seller venue where independent sellers — mostly individuals — self-list specific pre-owned items they hold, and buyers purchase them through platform-mediated transactions: an in-platform order, in-platform payment, and platform-governed delivery and disputes. The platform's defining posture is intermediary: it does not own, brand, or custody the supply. Everything else commonly present — messaging, offers, shipping labels, payout machinery, protection programs, feedback, authentication, promotion — makes the model workable but does not define it. The Type's identity rests on four properties (open self-listing, pre-owned one-off supply, mediated transaction, neutral venue), and each neighboring Type is the neighbor that appears when one property is removed.
