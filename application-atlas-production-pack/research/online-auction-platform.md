# Research Notes — Online Auction Platform

Research date: 2026-09-08
Slug: `online-auction-platform`
Directory leaf: "Online Auction Platform" (§05.18 Auction, sibling of "Auction Management System", processed 2026-09-06)

---

## Research Goal

Understand what the bidder-facing side of the auction business actually is as software: what a bidder-facing auction venue holds (lots, auctions, bids, awards), how participation works (registration, bidding, winning, paying), which rules govern the competition (reserves, increments, closes, binding bids), and how the boundary against the sibling leaf "Auction Management System" (operator-side system of record) holds from the bidder side. Also discharge the two pre-hung joint-review flags: (1) auction-management-system vs online-auction-platform (§05.18 siblings), (2) resale-marketplace vs online-auction-platform (bidding as pricing-mode variant).

## Initial Boundary

Working hypothesis before research:

- The Online Auction Platform (OAP) is the bidder-facing venue where competitive bidding is the transaction mechanism: goods are offered as lots, identified bidders compete through bids within bounded auctions, and each lot resolves to a definite award.
- The AMS pass fixed the seam: AMS = auction company staff operating lots/sales/awards/settlements as the system of record; OAP = bidder-facing marketplace where bidding is the transaction mechanism at market scale. The market bundles the two (AMS products ship white-label bidder surfaces; bidding-platform companies own AMS products).
- The resale-marketplace pass recorded: bidding is a pricing-mode variant there (eBay heritage); the auction Type is reserved for price-discovery-centered products.
- Nearest neighbors: Auction Management System (operator side — critical sibling), Online Marketplace / Multi-vendor Marketplace (fixed price), Classifieds (no in-platform transaction), Resale Marketplace (pre-owned, fixed price), E-sourcing (reverse auctions), trading venues (instruments, not goods lots), Fundraising Management (operator frame of the charity pole), Event Management (the sale as event).

## Research Questions

1. What is the unit of competition (lot/item), and how is it presented (photos, descriptions, estimates, reserves, starting bids)?
2. How do bidders participate (accounts, per-auction/per-sale registration, approval, verification, deposits)?
3. What auction formats exist (timed online with staggered closes, live webcast into a saleroom, hybrid, pre-bidding)?
4. How does bidding work (increments, quick bids, max/proxy/absentee bids, outbid notifications, anti-sniping)?
5. How does the competition resolve (scheduled close, soft-close extension, hammer; highest qualifying bid wins; reserve handling; passed/unsold lots)?
6. What happens after the award (winner notification, invoicing, payment — platform-mediated or operator-mediated, shipping/pickup, non-payment handling)?
7. Who are the sellers/operators (auction houses, government agencies, nonprofits, consumers) and what is the platform's economic model (buyer's premium, platform fees)?
8. What does the bidder's dashboard world look like (active bids, watchlists, won items, invoices, price archives)?
9. Historical check: would older online auction products (late-1990s timed C2C auctions, early white-label timed platforms) and the pre-digital analog (absentee-bid book + paddle registration + hammer) satisfy the same core?
10. Boundary checks: vs AMS (operator side), vs fixed-price marketplaces (eBay straddle), vs classifieds, vs e-sourcing reverse auctions, vs trading venues.

## Representative Products

Selected for market representability, different philosophies, different customer tiers; final sample shaped by reachability (many flagship auction marketplaces are bot-protected — see Sources):

| Product | Geography / tier | Philosophy / posture | Evidence accessed |
|---|---|---|---|
| **Invaluable** | US/global; fine art & antiques collectors | Aggregator marketplace of many auction houses; live + timed bidding; house relationships central | Tier 1 help center (Bidding FAQ 19 articles, Auctions & Registration FAQ 7) + root page |
| **LiveAuctioneers** | US/global; art, antiques, collectibles | Aggregator marketplace (ATG family); live + timed; strong bidder-side help | Tier 1 help center (Zendesk: Bidding, Registering, won-items, Buy-Now/Make-Offer, Reserves articles) + root page |
| **Christie's** (online bidding) | Global; single auction house | House-direct pole: the house runs its own online bidding venue on its own site (no marketplace aggregation) | Tier 1 help centre (buying guide: register-and-bid, buying-guide overview) |
| **BiddingOwl** | US; nonprofits/charities | Charity/fundraising pole: nonprofit-run auctions with mobile bidding; operator + bidder sides in one product | Tier 1 knowledge base (FAQs: registration, auto-bidding vs extended bidding, end-of-auction, reserve, buyer's premium) + root page |

Boundary anchors (no product claims made): **eBay** (consumer C2C pole, auction heritage — help center bot-blocked this pass and in the resale pass), **Proxibid / HiBid / the-saleroom / BidSpotter / EasyLive** (ATG-family auctioneer marketplaces — bot-blocked), **Catawiki** (European curated auctions — blocked), **GovDeals / PublicSurplus** (government surplus — JS-shell/timeout), **eBid / Yahoo! JAPAN Auctions** (consumer C2C — blocked/timeout).

Considered and excluded: Maxanet, BidWrangler, Bidpath, Wavebid (already sampled as AMS in the sibling pass; their bidder-facing surfaces are cited there as the bundling pattern).

## Sources

Tier 1 (official operational documentation):

- Invaluable Help & FAQ — https://www.invaluable.com/inv/help/ ; Bidding category: https://www.invaluable.com/inv/help/faq/bidding/ ; Auctions and Registration category: https://www.invaluable.com/inv/help/faq/auctions-registration/ (article bodies fetched in full)
- LiveAuctioneers Help Center — https://help.liveauctioneers.com/ ; Bidding section: https://help.liveauctioneers.com/hc/en-gb/sections/24079891956241-Bidding ; Registering section: https://help.liveauctioneers.com/hc/en-gb/sections/24079945504401-Registering ; articles fetched: "How do I know if I won an item?", "What is Buy now & Make Offer?", "What are Reserve Prices?"
- Christie's Help Centre — https://www.christies.com/en/help (served via christies.com.cn mirror) ; "How to buy at Christie's" buying guide: https://www.christies.com.cn/en/help/buying-guide/overview ; "Register and bid": https://www.christies.com.cn/en/help/buying-guide/register-and-bid
- BiddingOwl Knowledge Base — https://biddingowlcom.instantdocsbase.com/ ; articles fetched: "Are bidders required to register to bid?", "Auto-Bidding vs Extended Bidding", "What happens at the end of my auction?", "Can I input a 'Reserve' amount for my items?"; FAQ index (titles): buyer's premium/Support and Processing Fee, bid increments, Buy It Now, pre-bidding, autobid, private auction, payment options, manager bid deletion

Tier 2 (official product pages):

- Invaluable root — https://www.invaluable.com/ (marketplace structure: upcoming live/timed auctions by house, categories, artists, price archive, sell-on-invaluable, apps with outbid notifications)
- LiveAuctioneers root — https://www.liveauctioneers.com/ and https://www.liveauctioneers.com/how-auctions-work (nav/footer: upcoming auctions, auction house directory, price results, seller sign-in, consign, ATG parentage link, "Since 2002")
- BiddingOwl root — https://www.biddingowl.com/ (fundraising positioning; virtual/in-person event features; manager + bidder logins; featured auctions)
- Christie's help centre index (buying/selling guides, FAQ, auction help library)

Unreachable (abandoned per network-limitation rule; no claims made about any of these):

- eBay — help home and article pages bot-verification wall (×2 this pass; also blocked in the 2026-09-05 resale pass)
- Proxibid — root 403; help.proxibid.com transport error (×2)
- HiBid — root 403; help.hibid.com 403 (×2)
- the-saleroom — 405; BidSpotter — 405; EasyLive — 403; Catawiki — 403 (×2); eBid — 403
- GovDeals — JS-empty shell (×2); PublicSurplus — timeout; Yahoo! JAPAN Auctions — timeout

## Product Observations

### Invaluable

Evidence layer: A (direct, official help-center article bodies + root page).

Key observations:

- Positioning: "the world's leading online auction marketplace, thousands of auction houses use Invaluable to deepen relationships with millions of clients"; footer "© 1986-2026 Invaluable, LLC. and participating auction houses". Sell-side surface: "Sell on Invaluable" (auction houses are the sellers). Price Archive of past results; Artist Database.
- **Two auction types**: Live ("real time sales that allow you watch the auction in progress and participate during the sale"; date/time = when the auction begins) and Timed ("internet-only auctions that are run for a set duration and available for absentee bidding only"; date/time = when bidding on the first lot ends). Distinct icons per type.
- **Registration per sale**: "To participate in an Invaluable Live or Timed auction, you must first register to bid for the sale. Each auction house has different methods for approving bidders." Approval at the house's discretion; email notification on approval; status visible in the bidder's auction list. Registration requires a valid credit/debit card ("ensure your payment check-out process is quick and efficient once receiving your invoice from the auction house") and agreement to the house's terms and conditions. Once approved with a house, the platform auto-submits registration requests for that house's future auctions.
- **Pending registration**: "any bids placed while you are in Pending mode will not get presented to the auctioneer on sale day if you have not been approved by the time the lot comes up for auction."
- **Absentee/max bids before live auctions**: enter a maximum; "If you are the highest absentee bidder, our system will place your bids automatically, one increment higher than the last in-room bid, until we have reached your maximum bid." "SecureBid technology places bids on your behalf without ever revealing the maximum amount you're willing to pay… We try to win the item for you at the lowest possible price." Submitting an absentee bid also registers you for the auction.
- **Live bidding console**: "an exclusive online bidding console that simulates all of the aspects of being at the auction house in person"; requires registration + approval; "Bid Now" button at the current ask.
- **Timed auctions**: "Whoever has the highest bid when the time runs out wins the item." Reserves: "a reserve is the minimum price that an auctioneer will sell their item for… a 'reserve not met' or 'reserve met' message will display next to the bid box… If the reserve price has not been met by the time the auction ends, the item will not be sold."
- **Anti-sniping by extension**: "Invaluable does not allow sniping. If a bid is placed within the last 5 minutes of a lot's scheduled end time, we extend the sale by 5 minutes from the last bid… Extended bidding continues until 2 hours after the last lot's scheduled end time." (product-specific numbers)
- **Bid limits**: "Some auction houses set a limit on the amount a bidder can bid for the duration of a sale. You may request to increase this limit prior to the auction." AMLD5: EU bidders ≥ €7,500 must verify identity (KYC flow with verification-status badge).
- **Bid cancellation**: live — until the lot opens for live bidding; timed — until 2 hours prior to the auction's first lot end time, max 3 cancellations per session. Accidental live bids → contact the house; cancellation of a sale is at the house's sole discretion.
- **High-bidder semantics**: live — "not a guarantee that you will win the item, as your bid will be competing with live floor bids… your bid history will show you the time when your bid was presented to the internet clerk." Timed — highest at close wins.
- **Absentee push**: tie between an absentee max and a live bid at the same amount → the earlier absentee bid takes priority and is presented to the clerk.
- **Passed lots**: "the auction house has sole discretion to accept bids from a variety of sources (floor, internet, phone) as well as the option to pass a lot during a sale" (e.g., reserve not met, item removed).
- **Money loop split**: "you will receive an invoice from the auction house or from Invaluable that outlines the additional fees, including the buyer's premium and any applicable taxes." Buyer's premium includes an online fee component for houses not offering "Buyer's Premium Parity"; "You will be shown the exact buyer's premium on a lot before confirming your bid." Example given: 25% premium + online fee → $30 on a $100 hammer (product-specific illustration).
- **Bid display semantics**: displayed price = starting bid (0 bids) or current leading bid per the auction's increments; "the displayed 'Current Bid' is the amount you should be bidding above and not a reflection on the highest bid left on that lot."
- **Bidder dashboard**: My Bids (upcoming/past), bid history per lot, increase/cancel absentee bids, request limit increase, message the house (Bidding Approval category).
- Authenticity: images/descriptions provided by each house; bidders encouraged to request condition reports; marketplace standards + customer care for disputes.

### LiveAuctioneers

Evidence layer: A (direct, official help-center articles + root page).

Key observations:

- Positioning: "Online Auctions for Arts, Antiques & Collectibles"; "Since 2002, LiveAuctioneers has made exceptional items available for safe purchase in secure online auctions." Footer links to Auction Technology Group leadership/careers (ATG family). Surfaces: Upcoming Auctions, Auctions Near Me, Auction House Directory, Price Results, Consign, Seller Sign-In (partners subdomain), Seller Resource Center, Seller Reviews.
- Root page shows live auctions ("Live 279", "Started:"), timed auctions with staggered ends ("Ends from:"), trending lots with current bid + bid counts + time left, featured auctioneers (incl. Bonhams, Freeman's, Wright, Leland Little), saved searches with followers.
- Help-center categories: Getting Started, Ship with LiveAuctioneers, My Account, Registering, Bidding, Lot Information, Payment Information, Shipping Information, Disputes, Refunds & Returns, Ratings & Reviews, Favorites/Saved Items & Searches, Notifications and Alerts, Selling/Consignment/Appraisals, Technical Support, Promotions and Discounts.
- **Bidding article set** (titles): absentee bid opened at max amount; "Am I bidding against yourself?"; can I bid lower than the start price; mobile bidding; how bidding increments work; how do I know if I won; how do I know if I'm the high bidder; reserve price visibility; cancel/retract bid; how to leave an absentee bid; accidental bid won; what are reserve prices; what is a buyer's premium; Buy now & Make Offer; bid limits and increases; will the auction see my maximum bid.
- **Winning**: won lots appear on the "Won Items" dashboard page + email notification; "You also have the option to contact the auction house and to pay your invoice (if the invoice is sent via LiveAuctioneers). All payment and shipping arrangements are made directly with the auction house… Auction houses typically email you an invoice with payment instructions within 24-48 hours of the end of the auction." Related article: "I thought I won an item but the Auction house says I did not. What should I do?" (award disputes exist; house authority).
- **Buy It Now / Make an Offer**: post-auction sales channel — "allows Auction Houses to try to sell pieces that might not have sold at auction or passed. It also allows users to purchase an item at or below the reserve price… normally be available for up to 14 days after the auction has concluded." Buy Now = purchase at the price the auctioneer finds acceptable; Make an Offer = propose a different price; the auctioneer may decline any offer. (Fixed-price/negotiation modes inside the auction venue.)
- **Reserve prices**: "the minimum price for which an item will sell… If the reserve price is not met, the item will not be sold." "Reserve Not Met" alerts on lot pages and My Bids (only after a bid is placed). House guidelines: reserves not higher than the low estimate; reserves cannot be changed after the item has been sold; lots cannot be canceled post-sale because the price fell short of perceived value; bidders cannot cancel a sale they won at/above reserve; buyers must be informed when a reserve exists; houses should not bid on their own items above reserve; reserve changes no later than 2 hours before sale start. (product-specific policy detail)
- Registration section: articles on registering for auctions, approval, pending registration, declination, and "Can I place a bid before registering?" (title only; body not fetched — no claim made on its answer).

### Christie's (house-direct online bidding)

Evidence layer: A (direct, official help-centre buying guide).

Key observations:

- Single-house pole: the auction house itself operates the bidder-facing online venue on its own site; no marketplace aggregation. Buying guide flow: Create an account → Find what you love → Register and bid → Payment and shipping → (Buying privately = private sales service, outside the auction loop).
- **Two sale forms**: live auctions ("take place on a specific date and time in one of our salerooms around the world") and online auctions ("open for bidding for a fixed period over several days").
- **Four ways to bid in a live auction**: in person (paddle; photo ID + proof of address; "Bidding generally opens below the low estimate and advances in increments of up to 10%, subject to the auctioneer's discretion"); **Christie's LIVE™** ("Our online bidding platform for live auctions allows you to watch and place bids in real time from your desktop or mobile… click 'Join auction' when the session begins to enter the online saleroom and bid"); telephone bidding (staff bid on your behalf; "emergency absentee bid" recommended); absentee bidding ("place an absentee bid beforehand and the auctioneer will bid on the lot for you. If your bid is more than the reserve, the auctioneer will try to win the lot for you at the lowest price they can. An absentee bid takes priority over the same bid amount in the room or on the telephones").
- **Registration and qualification**: account + verified identity → register to bid in any auction; recommendation to register ≥24h before a live auction; "For some auctions, you may also be asked for a financial reference and/or a deposit as a condition of allowing you to bid."
- **Online-auction bid mechanics**: register on the auction page (confirm account details, e.g., shipping address); "quick bid" = next sequential bid per predetermined increments (published in the Conditions of Sale); "max bid" = highest willing bid, "continues to bid on your behalf until that bid is exceeded. If two or more bidders leave identical bids, the first bid received takes precedence." Max bid editable while current bid is below it.
- **Cost transparency before bidding**: "Use the 'Cost calculator' on the lot page for an estimate of Buyer's Premium and shipping before you bid."
- **Binding bids**: "you cannot cancel a bid once it's been submitted."
- **Soft close**: per-lot countdown; "If a bid is placed within three minutes of the closing time of a lot, the lot will remain open for three additional minutes, until no further bids have been placed and a highest bidder has been determined." (product-specific numbers)
- House-side assurances: authentication, provenance review, condition reports, specialist estimates ("assign an estimate range"); ~350 auctions annually (vendor claim).

### BiddingOwl

Evidence layer: A (direct, official knowledge-base articles + root page).

Key observations:

- Positioning: nonprofit fundraising auction platform ("Fundraising Software That Gets Your Mission"); separate Manager Login and Bidder Login; featured auctions directory; pricing "5% on winning online/mobile bids" (vendor claim in a comparison article).
- Operator side (manager): auction setup, items (images, categories, value vs cost fields), donors, sponsors, tickets, donations, paddle raises, fund-a-need, communications (email/SMS), bidder management, bid deletion, multiple auctions, private auctions with access codes, pre-bidding for in-person events (paper bid sheets), Buy It Now option, payment integrations (Stripe/PayPal) or payments outside the system.
- **Bidder registration required**: "To participate in bidding, all bidders must complete the registration process and be logged in. This requirement serves multiple important purposes: it maintains fairness and security throughout the auction, establishes accountability for all participants, and filters out non-serious bidders… credit card details are not required or collected during registration." (contrast with professional-auction card-on-file registration)
- **Anti-sniping by proxy, not extension**: "We don't offer extended bidding on our platform. Instead, we offer auto-bidding, which enables bidders to set their maximum bid and remain competitive without needing to constantly monitor the auction… Prevents last-second 'sniping' by automatically increasing bids up to the bidder's set maximum… No extra time for latecomers once the auction closes." (deliberate design contrast with Invaluable/Christie's soft close)
- **No separate reserve**: "We do not have a reserve price as you would know from Ebay. However, you may set your opening bid instead of a reserve price." (the opening bid is the floor; no hidden reserve)
- **End-of-auction flow**: automated winner notification (email/SMS with cart link) → typical 24h payment window → reminder communications to "Unpaid Bidders" → 48h urgent reminder with deadline ("items must be paid for by the specified deadline… or the item(s) will be awarded to the next-highest bidder") → if a winner does not pay, the manager deletes the bid(s) and "the system automatically awards the item(s) to the next-highest bidder and sends them a winner notification." (award reassignment machinery)
- **Buyer's premium as platform-fee offset**: "You can make your auction completely free by adding a Buyer's Premium, which we call the Support and Processing Fee, to offset platform fees." (charity-pole variant of the premium's purpose)
- Checkout: cart-based; integrated Stripe/PayPal or payments taken outside the system.

## Cross-product Comparison

| Structure | Invaluable | LiveAuctioneers | Christie's | BiddingOwl | Assessment |
|---|---|---|---|---|---|
| Lots/items as the biddable unit (photos, descriptions, estimates) | ✔ (lot pages, estimates, condition info via house) | ✔ (lot pages, lot information section) | ✔ (lots with estimates, condition reports) | ✔ (items with images, value/cost) | Core (4/4) |
| Price discovered by bidding, not posted | ✔ | ✔ | ✔ | ✔ | Core (4/4) |
| Auction as bounded competition with defined close | ✔ (timed: scheduled end; live: session) | ✔ (timed "Ends from"; live sessions) | ✔ (timed fixed period; live date/time) | ✔ (items close at set date/time) | Core (4/4) |
| Identified bidders (accounts) | ✔ | ✔ | ✔ | ✔ | Core (4/4) |
| Registration/approval gating bidding | ✔ (per-sale, house approval, card on file) | ✔ (Registering section; approval/pending/declined) | ✔ (register to bid; financial reference/deposit) | ✔ (registration required; no card) | Core (4/4; depth varies by tier) |
| Recorded competitive bids with visible competition | ✔ (current bid, bid history, high-bidder status) | ✔ (current bid, bid counts, high-bidder article) | ✔ (quick/max bids, increments) | ✔ (bids, outbid texts) | Core (4/4) |
| Definite per-lot award (won/unsold) | ✔ (highest at close wins; passed lots) | ✔ (won items; reserve unmet → not sold) | ✔ (highest bidder determined) | ✔ (winners notified; reassignment) | Core (4/4) |
| Max/proxy/absentee bids executed automatically | ✔ (SecureBid; absentee push) | ✔ (absentee bid articles) | ✔ (max bid; absentee priority) | ✔ (auto-bidding) | Common (4/4) — mechanism naming varies |
| Outbid notifications / alerts | ✔ (app: "instantly notified if you're outbid"; emails/alerts category) | ✔ (Notifications and Alerts section) | not directly observed (app implied) | ✔ (SMS/email outbid texts) | Common (3/4 direct) |
| Anti-sniping: soft-close extension | ✔ (5-min extension, 2h cap) | not directly observed | ✔ (3-min extension) | ✘ (deliberately absent — proxy instead) | Variant mechanism (2/4 direct + 1 explicit negative) |
| Anti-sniping: proxy/max bids | ✔ | ✔ | ✔ | ✔ (stated as the chosen mechanism) | Common (4/4) — the general solution |
| Live bidding console (webcast into saleroom) | ✔ ("simulates all of the aspects of being at the auction house") | ✔ (live auctions; "Live" badges) | ✔ (Christie's LIVE™ "online saleroom") | ✘ (event-side mobile bidding instead) | Common in professional poles (3/4) |
| Timed internet-only auctions | ✔ | ✔ | ✔ | ✔ | Common (4/4) |
| Reserves with not-met handling | ✔ ("reserve not met" display; not sold) | ✔ (guidelines, alerts) | ✔ (absentee only wins above reserve) | ✘ (opening bid instead) | Common (3/4) — NOT definitional |
| Buyer's premium / charges on top of hammer | ✔ (displayed before bid; online fee) | ✔ (buyer's premium article) | ✔ (cost calculator) | ✔ (optional "Support and Processing Fee") | Common (4/4) — rates/purpose vary |
| Post-award money loop | split (invoice from house OR Invaluable) | house-direct ("payment… made directly with the auction house"; platform invoice optional) | house-direct (payment and shipping guide) | platform checkout (cart/Stripe/PayPal) or outside system | Variant placement (4/4, three patterns) |
| Post-auction fixed-price/negotiation channel | not directly observed | ✔ (Buy It Now / Make an Offer, 14 days) | not observed (private sales as separate service) | ✔ (Buy It Now option) | Optional (2/4 direct) |
| Award contestability / reassignment | ✔ (house discretion; accidental-bid path) | ✔ ("house says I did not" dispute article) | not directly observed | ✔ (delete bid → next-highest reassignment) | Common (3/4 direct) |
| Price archive / past results | ✔ (Price Archive) | ✔ (Price Results) | not directly observed | ✘ | Optional (2/4) |
| Discovery machinery (search, categories, house directory, saved searches, alerts) | ✔ (categories, artists, houses) | ✔ (directory, saved searches with followers) | ✔ (find what you love) | ✔ (featured auctions) | Common (4/4) |
| Mobile apps with bidding | ✔ | ✔ | ✔ (bid from desktop or mobile) | ✔ (mobile-optimized bidding) | Common (4/4) |
| KYC / identity verification for high-value bidding | ✔ (AMLD5 €7,500 EU) | not directly observed | ✔ (identity verification at account level; financial references) | ✘ | Optional/variant (2/4) |
| Bid limits set by seller | ✔ (house-set limits, increase requests) | ✔ (bid limit article) | ✔ (financial reference/deposit as gate) | ✘ | Common in professional poles (3/4) |
| Charity apparatus (donations, paddle raises, tickets) | ✘ | ✘ | ✘ | ✔ | Variant (charity pole) |
| Multi-house marketplace aggregation | ✔ | ✔ | ✘ (single house) | ✘ (single organization per auction) | Variant posture (2/4) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which a bidder-facing product is not recognizable as an online auction platform:

```text
Lot (item offered where the price is discovered by bidding, not posted)
└── Auction (bounded competition with a defined close)
    └── Bid (recorded competing offer from an identified bidder)
        └── Award (definite per-lot outcome:
             sold to the highest qualifying bidder / unsold or passed)
```

Plus the posture that makes it this Type rather than its sibling: the venue is **participant-facing** — its users are the bidders competing and the sellers/houses whose lots are offered, not the operator's staff running the back office.

Four invariants:

1. **Lots offered for bid-based price discovery** — the venue presents goods as individually biddable lots whose price emerges from competition rather than a posted price. Without this, the product is a fixed-price marketplace or webstore.
2. **Identified bidders competing through recorded bids** — bids are attributed to identified participants, ordered by the auction's increment rules, and the state of the competition is made visible (current bid, high bidder, bid history, outbid notices). Without identified bidders, it is an anonymous interest poll, not a transaction venue.
3. **Bounded competition with a defined close** — bidding happens within a bounded auction that ends at a defined point: a scheduled lot close (timed auctions, often staggered), or the live session's hammer. Without the bounded close — with lots sitting always-open — it is an always-open marketplace.
4. **Definite per-lot award** — each lot resolves to a recorded outcome: sold to the winning bidder at the final bid (per the lot's configured terms, e.g., a reserve where present) or unsold/passed. Without the award, bidding never resolves into a result and the product is a bid recorder, not a venue.

Deliberately NOT in L0 (checked against the sample):

- **The money loop** — the post-award invoicing/payment loop is variably placed: platform-mediated checkout (BiddingOwl cart), operator-mediated invoicing (LiveAuctioneers: "payment and shipping arrangements are made directly with the auction house"; Invaluable: invoice "from the auction house or from Invaluable"), or house-as-platform (Christie's). The venue's own terminal output is the award and the winner notification; what follows is a handoff. (Contrast: the money loop IS definitional for the AMS — it is what makes the operator side a management system.)
- **Reserves** — BiddingOwl has no separate reserve (the opening bid is the floor); the award rule is "highest qualifying bid per the lot's terms", and a reserve is one possible term.
- **Soft-close extension** — BiddingOwl deliberately does not extend (proxy bids are its anti-sniping mechanism); Invaluable and Christie's extend. The bounded close is the invariant; how late bids are handled is a mechanism choice.
- **Live webcast consoles** — timed-only venues satisfy the core (BiddingOwl is timed-only; many white-label timed platforms exist).
- **Marketplace aggregation** — Christie's is a single house running its own bidder-facing venue; white-label bidder sites are single-operator venues. Multi-house aggregation is a posture, not the definition.
- **Buyer's premium display, cost calculators, price archives, mobile apps, KYC** — common machinery, not definition.

Historical check (§24-style): the pre-digital analog — a saleroom with paddle registration, an absentee-bid book (bidders leave maximum bids the auctioneer executes), and the hammer closing each lot to the winning paddle — satisfies all four invariants at analog level; the OAP digitizes the bidder-facing participation layer (the "Online" in the name marks the digitization, not a feature set). Late-1990s/2000s online timed auctions (C2C auction sites; white-label timed platforms operating since 1997 per the AMS pass's Maxanet evidence) satisfy the core with none of the modern machinery (no apps, no KYC, no soft close, no live video). Regional C2C auction venues (Yahoo! JAPAN Auctions class) and curated European venues (Catawiki class) fit the same core structurally — noted as structural inference only, since those products were unreachable this pass.

### L1 — Common Mature Structure

Present in essentially all mature modern implementations; expected by the market but not definitional:

- bidder accounts with per-auction/per-sale registration; approval workflows (automatic or seller-reviewed), terms acceptance, card-on-file or deposits at professional tiers
- bid mechanics: predetermined increments, quick/one-click bids at the current ask, max/proxy/absentee bids executed automatically on the bidder's behalf, outbid notifications (push/SMS/email), watchlists/favorites
- timed auctions with staggered lot closes; live bidding consoles streaming the saleroom ("online saleroom"); hybrid formats; pre-bidding into in-person events
- reserves with "reserve not met" indicators; estimates displayed on lots; starting bids
- buyer's premium and charges displayed before bid confirmation; cost calculators (premium + shipping estimates)
- bid history visibility per lot; high-bidder status; "am I bidding against myself" guardrails
- won-items dashboard; winner notifications (email/SMS); invoices and payment (platform or operator); shipping/pickup arrangements
- award contestability: seller discretion over live-sale awards, dispute paths, non-payment handling with reassignment to the next-highest bidder
- post-auction sales channels: Buy It Now / Make an Offer on unsold or passed lots
- price archives / past results; discovery machinery (search, categories, seller/house directories, saved searches with alerts)
- mobile apps with outbid notifications; bid limits set by sellers with increase requests; KYC/identity verification for high-value bidding in regulated regions

### L2 — Variant / Optional Structure

- **Venue posture**: multi-house marketplace aggregation vs single-house venue vs white-label bidder sites operated by one organization
- **Seller population**: professional auction houses (consignment), institutional sellers (government agencies, corporations liquidating), nonprofits/charities, consumers (C2C)
- **Format mix**: live webcast, timed-only, hybrid simulcast, pre-bidding into in-person events, sealed-bid (common in market, not directly evidenced in this sample — not claimed)
- **Anti-sniping mechanism**: soft-close auto-extension vs proxy-bid-only vs (historically) hard close with proxy protection
- **Payment mediation**: platform checkout (cart, integrated processors) vs operator invoicing with platform-optional invoicing vs house-as-platform
- **Post-auction channels**: Buy It Now / Make an Offer windows on unsold lots; fixed-price listings alongside auction-format listings (eBay-class products)
- **Regulatory posture**: KYC/identity verification thresholds for high-value bidding (EU AMLD5-class), financial references/deposits, paddle registration at physical sales
- **Charity apparatus**: donations, paddle raises, fund-a-need, tickets, sponsor levels — the fundraising frame around the same bidding core
- **Commercial model**: commission/fee on winning bids, seller subscriptions, buyer's premium as platform-fee offset

### L3 — Vendor-specific (research notes only)

- Invaluable: SecureBid; Buyer's Premium Parity program; 5-minute/2-hour extension specifics; 3-cancellations-per-session rule; €7,500 AMLD5 KYC threshold with verification badge; "absentee push" tie-break; online fee folded into displayed premium; 1986 lineage claim; auto re-registration with previously approved houses.
- LiveAuctioneers: Ship with LiveAuctioneers (shipping service); 14-day Buy-It-Now/Make-Offer window; reserve policy guidelines (2-hour change cutoff, no post-sale cancellation, no house bidding above own reserve); ATG parentage; "Since 2002"; saved searches with follower counts; seller reviews.
- Christie's: Christie's LIVE™ and "online saleroom" naming; increments "up to 10% subject to the auctioneer's discretion"; 3-minute soft close; identical-max-bid first-received precedence; cost calculator; 24-hour registration recommendation; financial references/deposits; telephone bidding with emergency absentee bids; ~350 auctions/year (vendor claim); private sales as a separate buying path.
- BiddingOwl: "Support and Processing Fee" naming for the buyer's premium; 5% fee on winning online/mobile bids (vendor claim); no extended bidding (deliberate); opening-bid-as-reserve; cart checkout with Stripe/PayPal or outside-system payments; next-highest-bidder automatic reassignment; private auctions with access codes; paddle raises/fund-a-need; manager bid deletion; HubSpot-hosted KB.

## Vendor-specific Findings

See L3. None enter the canonical model. Notable cross-vendor pattern: the anti-sniping problem is solved by two different mechanisms (soft-close extension vs proxy bids) — a mechanism-level split, not a Type split. Another: the money loop's placement splits three ways (platform checkout / operator invoicing / house-as-platform) — the venue's job ends at the award.

## Boundary Findings

1. **vs Auction Management System (sibling leaf, §05.18) — pre-hung joint-review flag DISCHARGED from this side.** The boundary holds. The OAP is the participant-facing venue: its users are bidders (and the sellers/houses whose lots are offered); its objects are lots, auctions, bids, awards; its terminal output is the award plus winner notification. The AMS is the operator's system of record: its users are the auction company's staff; its objects add consignors, clerking, buyer invoicing, seller settlement. Removal tests hold both ways: strip the operator back-office from a bundled product → a bidding venue remains (this Type); strip the bidder-facing venue → the AMS remains. The money loop is the sharpest single discriminator: it is definitional for the AMS (invoicing + settlement = managing the auction business) and explicitly NOT definitional for the OAP (three placement patterns observed; the venue ends at the award). Bundling is universal at the professional tier (the AMS pass's four products all ship white-label bidder surfaces; this pass's marketplace products are the bidder-facing side of houses' operations), but bundling does not merge the Types. BiddingOwl demonstrates the bundle from the small-operator side: one product, two surfaces (manager console = AMS-shaped; bidder venue = OAP-shaped), and the two sides remain distinguishable inside it. Both leaves stay distinct Types; no taxonomy change.
2. **vs resale-marketplace (§05.19) — pre-hung seam CONFIRMED from this side.** The resale pass recorded: "bidding is a pricing-mode variant there (eBay heritage), with the auction Type reserved for price-discovery-centered products." This pass confirms the seam from the auction side: in the sampled OAP products, competitive bidding with a bounded close and a definite award is the defining transaction mechanism, and fixed-price modes appear only as secondary channels (LiveAuctioneers Buy It Now / Make an Offer on unsold lots, up to 14 days post-auction; BiddingOwl Buy It Now option) — the reverse of the marketplace relationship. eBay straddles historically (auction heritage → broad fixed-price venue); it was unreachable this pass, so no eBay-specific claims are made; the seam statement stands on the sampled products.
3. **vs Online Marketplace / Multi-vendor Marketplace (§05.02)** — fixed-price mediated purchase at a posted price vs price discovered through competition resolved by an award. The multi-vendor-marketplace pass already lists eBay as its open-venue pole with auction heritage; the seam is whether the bounded competitive award is the defining mechanism or one pricing mode. Removal test: remove bidding → marketplace; remove the always-open listing model → auction venue.
4. **vs Classifieds Platform / Listing Marketplace (§05.03)** — listings with contact-and-arrange or best-offer; no identified-bidder competition, no bounded close, no award recorded by the venue.
5. **vs E-sourcing / Procurement Platforms (§10, reverse auctions)** — same competitive-bidding mechanics, reverse direction: the buyer solicits offers and suppliers bid prices down; users are procurement organizations, the object is a contract award. Not this Type.
6. **vs Trading venues (Brokerage, Carbon Trading, etc.)** — auctions appear as one execution mechanism inside instrument markets; those venues center instruments, membership, and settlement rails, not goods lots for end delivery. The carbon-trading pass recorded this seam from its side ("a standalone auction platform governs the event but not the instrument universe, membership market, and settlement rails").
7. **vs Fundraising Management / charity event tooling** — BiddingOwl's operator frame is fundraising management (donors, tickets, paddle raises, sponsor levels); its bidder-facing auction surface is OAP-shaped. The AMS pass treated charity auction tooling as a variant posture of the auction business; from this side, the charity pole is a variant posture of the OAP (same bidding core, fundraising apparatus around it). No separate directory leaf exists for charity auction platforms; no change proposed.
8. **vs Event Management Platform (§26)** — an auction sale is an event, but event management centers attendee registration, agenda and logistics; the OAP centers the lot competition and award. BiddingOwl bundles event-ish apparatus (tickets) around the auction core — packaging, not identity.
9. **vs Ticket Resale Marketplace (§26)** — same word "auction" in market usage sometimes; different object world (dated seat-bound entitlements with transfer mechanics vs goods lots). No overlap in core objects.

## Uncertainties

- **eBay** (the consumer C2C pole and the historical anchor) was unreachable (bot-verification wall, ×2 this pass; also blocked in the resale pass). No eBay-specific claims are made anywhere. The consumer pole is therefore carried by structural inference and the resale pass's recorded eBay observations, not by fresh Tier-1 evidence.
- **Proxibid, HiBid, the-saleroom, BidSpotter, EasyLive** (the ATG-family auctioneer marketplaces) all bot-blocked — the industrial/commercial liquidation marketplace pole is unverified first-hand; its shape is inferred from the AMS pass's Wavebid/Proxibid-family evidence and this pass's fine-art marketplace poles.
- **Government/institutional surplus venues** (GovDeals, PublicSurplus) unreachable (JS shells/timeout) — the institutional seller pole is unverified first-hand.
- **Catawiki, eBid, Yahoo! JAPAN Auctions** unreachable — the European curated pole and the regional C2C pole rest on structural reasoning only.
- **Sealed-bid / Dutch auction formats** not directly evidenced in the fetched sample; not claimed in the final document beyond a hedged mention in research notes.
- **LiveAuctioneers "Can I place a bid before registering?"** article body not fetched — the registration-before-bidding claim for LiveAuctioneers rests on the Registering section's existence and the cross-product pattern, not that article's answer.
- **Fee/percentage figures** (BiddingOwl 5%, Invaluable premium examples, Christie's 10% increment ceiling) are vendor-stated and product-specific; kept out of the canonical document.
- **Regional check** (continental-European, Asian venues) is structural only, per the unreachable-products list above.

## Final Synthesis

An Online Auction Platform is the bidder-facing venue of the auction business: a place where goods are offered as individually biddable lots whose price is discovered through competition rather than posted, where identified bidders register (and, on professional venues, are approved) before competing through recorded bids inside bounded auctions that end at a defined close, and where each lot resolves to a definite award — sold to the highest qualifying bidder at the final bid, or unsold/passed. Around this spine, mature products add the machinery the market expects: per-sale registration with approval and verification; predetermined increments with quick bids; max/proxy/absentee bids executed automatically with the maximum hidden from competitors; outbid notifications; timed auctions with staggered closes and (on some venues) soft-close extension, or proxy-only closing by design; live bidding consoles that stream the saleroom; reserves with not-met indicators; buyer's premium and cost calculators shown before bidding; won-items dashboards with invoices and payment arranged either by the platform or by the seller; award contestability with dispute paths and next-highest-bidder reassignment on non-payment; post-auction Buy-It-Now/Make-Offer channels for unsold lots; price archives; discovery machinery and mobile apps. The defining boundary is with the Auction Management System: the OAP is the participants' side of the business and ends at the award, while the AMS is the operator's side and is defined by the money loop the award triggers. The market bundles the two relentlessly — every professional venue has an operator back office behind it, and every AMS ships a bidder surface — but stripping either side leaves the other Type intact. The historical check holds: the paddle-and-absentee-book saleroom satisfies the same four-part spine at analog level, and late-1990s timed online auctions satisfy it with none of the modern machinery, so the definition is not an artifact of the live-streaming or mobile era.
