# Research Notes — Auction Management System

Research date: 2026-09-06
Slug: `auction-management-system`
Directory leaf: "Auction Management System" (§05.18 Auction, sibling of "Online Auction Platform")

---

## Research Goal

Understand what software that auction companies use to run their auction business actually does — its central objects (lots, sales, bids, awards), workflows (cataloging → sale → award → money), states and rules — well enough to write a vendor-neutral Application Document, and to resolve the boundary against the sibling leaf "Online Auction Platform" (operator-side system vs bidder-side marketplace).

## Initial Boundary

Working hypothesis before research:

- An Auction Management System (AMS) is the auctioneer's operating software: it manages the goods entrusted for sale (consignments), turns them into cataloged lots, organizes them into sale events, captures bids (floor, absentee, online timed, webcast), records the per-lot outcome (hammer / no sale), and drives the money loop (buyer invoicing, seller settlement).
- The users are the auction company's staff (auctioneer, cataloger, clerk, cashier, administrator) — not the bidders. Bidders face a companion bidding surface (the vendor's or a third-party platform).
- Nearest neighbors: **Online Auction Platform** (bidder-facing marketplace — the critical sibling boundary), Artwork Consignment Management (consignor relations without a sale event), E-commerce Platform (fixed price, no competitive award), Classifieds/Listing Marketplace, Event Management (the sale is an event but not the center), E-sourcing (reverse auctions on the buying side).
- Known market pattern to verify: AMS products increasingly bundle a white-label bidder-facing bidding platform, and bidding-platform companies own AMS products (e.g., Wavebid is operated by Proxibid per its site footer) — the two Types are complementary layers of one auction business.

## Research Questions

1. Who operates the software, and what roles exist (auctioneer, cataloger, clerk, cashier, admin)?
2. What is a lot, and how do goods become lots (consignment intake, cataloging, estimates, reserves, starting bids)?
3. What is a sale event, and what sale formats exist (live saleroom, timed online, webcast/simulcast, hybrid)?
4. How are bidders qualified (registration, approval, card verification, deposits, paddle numbers, fraud controls)?
5. How are bids captured and resolved (clerking panel, auto-accept of remote bids, max bids, auto-extend, staggered close)?
6. What is the per-lot terminal outcome and how does it drive money (buyer invoice with premium/tax; seller settlement with commission)?
7. What happens to unsold lots?
8. What reporting and permissions exist?
9. Historical check: would a pre-internet auction house operation (paper clerking sheets, paddle registration, cashier, settlement checks) satisfy the same core?

## Representative Products

Selected for market representability, different philosophies, different customer tiers and geographies:

| Product | Geography / tier | Philosophy | Evidence accessed |
|---|---|---|---|
| **BidWrangler** | US; SMB–mid auctioneers; white-label | Mobile-first all-in-one: cataloging app + admin portal + branded bidding platform; "you own your data" | Tier 1 Knowledge Base index (category structure + article abstracts) + Tier 2 product pages |
| **Bidpath** | UK/global; mid–enterprise; multi-vertical | Back-office toolkit + webcast/timed platforms + bespoke websites + portals; fine art, commercial, industrial | Tier 2 official site (products/services/features) |
| **Maxanet** | US; budget SMB; since 1997 | Affordable white-label online auction platform; single login; consignor payouts | Tier 2 official site (features/verticals) |
| **Wavebid** | US; auto/industrial auctioneers | Cataloging + marketing + clerking pillars; part of the Proxibid bidding-platform family | Tier 2 root page only (deep pages login-walled) |

Considered and excluded:

- **Auction Flex** (US full-service auction house suite): root 403, support subdomain transport error → abandoned per network-limitation rule. No claims made about it.
- **eBay / LiveAuctioneers / Proxibid / the-saleroom / HiBid / EasyLive**: bidder-facing bidding platforms/marketplaces — they define the *sibling* Type (Online Auction Platform), used here only as boundary anchors, not sampled as AMS.
- Wavebid deep documentation: `/products` and `/cataloging` redirect to a login page; `help.wavebid.com` transport error → abandoned after failures; root-page evidence only.

## Sources

Tier 1 (official operational documentation):

- BidWrangler Knowledge Base — https://support.bidwrangler.com/ (category structure: BidWrangler Admin 63 articles; Creating Auctions 54; Auction Management 57; Reporting 10; Invoicing 14; Payment Processing 3; Clerking 1; Simulcast and Live Auctions 1; Bidder Assistance 7; Sellers and Settlements 1; Website Platform — plus article abstracts incl. "Registering Bidders in BidWrangler: The Complete Guide", "Administer Registrations Guide", "How Do I Require Manual Approval for Bidder Registration?", "Why Are Some Max Bid Arrows Red and Some Green in the Online Clerking Panel?", "How to Use Auto-Accept for Online Bids in the Online Clerking Panel", "How can I create a paper clerking sheet?", "How to Bulk Unlock Invoices and Settlements in BidWrangler", "How to Create, Manage, and Apply Flat-Rate Buyer's Fees…", "How to Set a Pay Now Threshold for Invoices", "How to Create Seller Mailing Labels for Auction Settlements", "How to Track VIN and Title Status…", "Block Threshold: Preventing Repeat Fraudulent Bidder Registrations", "How to Register Bidders using a Driver's License Scanner", "Permissions Guide", "Staggered Close and Autoextend", "How to use variable closing speeds in an auction", "How can I pause my auction?", "Items in Auction set to 'No Sale' upon publishing", "How to Add High and Low Estimates to Auction Items", "How to Set Default Starting Bids…", "BidWrangler Auction Staging: How do I Publish or Unpublish Items…", "Move and Duplicate Items", "The Parcel Map feature… multi-par", "How to Communicate 'Per Acre' Bidding…")
  - Limitation: individual article bodies were not retrievable (sitemap 404; search/category endpoints 404 ×2) — evidence is the KB index with article titles and abstracts. Mechanics are asserted only at the level the abstracts state.

Tier 2 (official product pages):

- BidWrangler — https://bidwrangler.com/ (white-label all-in-one; BAM admin portal incl. cataloging, invoicing, payments, seller settlements; AI cataloging; timed real-estate controls incl. approval process, auto-extension, backup bidder; max bids; outbid push notifications; live video; staggered close/auto-extend/auto-clerking; bidder verification via card deposits, terms acceptance, manual approval)
- Bidpath — https://auctionary.com/ (auctionary.com resolves to Bidpath) — products SAM/Go Auction/AIM; Timed Auctions; Auction Portals; Mobile Cataloging; Webcast Auctions; Auction Websites; Back Office ("full client and inventory management, sale-day, post-sale and finance functions, compliance modules, and key business reports"); Buyer Invoicing; eCommerce functionality; multi-language/currency; payment gateways + 3D Secure bidder verification; API suite; verticals (Commercial, Industrial, Fine Art, Insolvency, Aerospace, Electronics, Consumer Returns, Mining, Automotive)
- Maxanet — https://maxanet.com/ (white-label online auction software since 1997; integrated invoicing + Maxanet Pay; bidder data ownership; mobile admin app; reporting; consignor relationships and payouts; verticals incl. livestock, real estate, liquidations, closeouts, unclaimed property)
- Wavebid — https://www.wavebid.com/ (root: "Auction software, simplified" — Cataloging / Marketing / Clerking pillars; seller-centric framing; partners Marknet Alliance, Live Auction Group; footer "Proxibid Inc. t/a Wavebid")

Tier 3: none needed.

## Product Observations

### BidWrangler

Evidence layer: A (direct, official KB index + product pages) unless noted.

Key observations:

- Positioning: "a white-label auction software company with an all-in-one solution for auctioneers around the globe." The admin side is named **BidWrangler Auction Management (BAM)**: "everything you need to run an auction from top to bottom—including cataloging, invoicing, and payments—all within the BidWrangler admin portal. Our BidWrangler Auction Management (BAM) software includes our catalog mobile app, invoicing and payments, and seller settlements."
- KB category structure mirrors the operating loop: Admin (63) / Creating Auctions (54) / Auction Management (57) / Reporting (10) / Invoicing (14) / Payment Processing (3) / Clerking (1) / Simulcast and Live Auctions (1) / Bidder Assistance (7) / Sellers and Settlements (1) / Website Platform.
- **Registration is per-auction**: "A registration in BidWrangler connects a bidder's account to one specific auction, along with any card verification and approval your auction terms require." "To be able to participate in an auction, bidders must first create an account (or log into their existing account) and register for a specific auction."
- Qualification controls: **Manual Approval** ("review and approve every bidder before they can place a bid, instead of approving registrations automatically"); credit card deposits; auction terms & conditions acceptance; **driver's license scanner** in Live Registrations; **Block Threshold** ("helps stop previously blocked bidders from creating new accounts using slightly altered information"); **Custom User Fields** at account creation; separate CSV imports for **Bidders vs Registrations** ("what each import does").
- **Paddle numbers**: "permanent paddle (bidder) numbers" can be bulk-removed; accounts created on-site by the house are **unclaimed** until the bidder claims them and sets a password.
- **Clerking**: an online clerking panel with **SOLD / NO SALE** buttons (language customizable); **Auto-Accept Remote Bids** toggle ("controls whether online bids in the online clerking panel are accepted automatically or wait for your clerk"); **max bid arrows red/green** ("what each color says about a lot's reserve"); a **paper clerking sheet** can be generated via the Buyer's Guide ("this method is the only one that allows the inclusion of item images").
- **Lots/items**: Item ID (8-digit) and Auction ID (6-digit) as identifiers; **high/low estimates** ("assign estimated values to auction items for internal reference or for display to bidders"); **default starting bids at three levels — Company, Auction, and Item**; **publish/unpublish staging** ("keep items unpublished, then publish them only when the lot is ready, been reviewed"); **move and duplicate items** between auctions; categories/subcategories (bulk import); images (AVIF delivery); Matterport 3D tours; **VIN/title tracking** (Vehicle Title Summary report); **per-acre bidding** communication; **multi-parcel** with parcel maps; items can be set to **'No Sale'** upon publishing.
- **Timed auctions**: **staggered close and auto-extend** ("if bidding occurs within the last few minutes of the auction, it will automatically extend for the number of minutes you choose… group items to extend together, or adjust the bid increment in real time"); **variable closing speeds**; closing-speed guidance; **pause my auction**; "auctions are **auto clerked**"; **max bids** ("simplifies pre-bidding… so they can be bidding in the live auction automatically"); **outbid push notifications**; global watchlist; global item search across auctions; real-time support chat; "First Bid Message" popup.
- **Invoicing**: winning-bidder invoices; **flat-rate buyer's fees** applicable "to individual items, entire auctions, or directly to winning bidder invoices"; **Pay Now Threshold** ("control which invoices are eligible for online credit card payment"); **bulk unlock invoices and settlements** ("setup mistakes — an incorrect Buyer's Premium, the wrong tax rate, a misconfigured invoice setting"); 'Emailed at' tracking; statement layout/font customization; invoice header/note/footer fields.
- **Settlements**: "Sellers and Settlements" KB section; **seller settlement checks** with mailing labels; printing a seller's items list.
- **Payments**: integrated processing (Authorize.net merchant-account errors documented); card verification at registration.
- **Live/simulcast**: live video streamed "right from your smartphone" for "simulcast auctions"; broadcast equipment guidance.
- **Permissions**: "Permissions Guide — What Permissions should I assign to my staff?"; Full Admins can see who created/last edited items.
- **Real estate variant**: control over the approval process, auto-extension, **selling to a backup bidder** ("the ability to see who your backup bidder is incredibly important"), multi-parcel combinations.
- **AI cataloging**: "built-in AI cataloging tools draft titles and descriptions from your photos."
- Data ownership: "Ownership of your data (you acquired it, you own it!)".
- Customer framing (testimonial): "BidWrangler is our auction management system… whether live, online, or silent."

### Bidpath

Evidence layer: A (direct, official site).

Key observations:

- Positioning: "leading global auction software solution… over 750 leading auctioneers, retailers and manufacturers in 27 countries… over 20 years" (vendor claims). Products: **SAM Auction Software**, **Go Auction**, **AIM** (reseller).
- **Back Office**: "A complete auction management toolkit. Full client and inventory management, sale-day, post-sale and finance functions, compliance modules, and key business reports." — the operator-side spine in one sentence.
- **Mobile Cataloging**: "the easiest way to manage your auction inventory and save your team hours of cataloging time."
- **Sale formats**: **Timed Auctions** ("buyers engage directly with your brand on a fully configured platform, seamlessly integrated into your website"); **Webcast Auctions** ("live online auction technology enables your buyers to share the experience of a live auction in HD from anywhere"; low-latency real-time audio/video; iOS/Android apps).
- **Auction Portals**: "single website auction portals for multiple companies or company departments… cross-product promotion" — multi-company operation.
- **Auction Websites**: bespoke sites "fully integrated with our back office toolkit."
- **Buyer Invoicing**: "invoice buyers direct from the platform. The invoice will also appear in the buyer's online account, ready for payment; bulk reminders can be sent any time to buyers with unpaid invoices."
- **eCommerce functionality**: "Assets can be easily moved from an auction to a direct sales platform" — auction and fixed-price retail in one estate.
- **Auction management tools**: "all the tools you need to easily create, upload and manage your online auctions. Including a complete auction accounting system with payment gateways, multi currency functionality, watch lists, auction alerts, unlimited photos, auto refresh, and full bidder management."
- **Easy Catalogue Editing**: edits and image uploads "published immediately."
- **Multi-language/currency**: translated lot descriptions in the online catalogue and bidding application.
- **Payments/verification**: multiple gateway integrations (Authorize.net, Paytrace, NMI named); **3D Secure Bidder Verification** via SagePay for UK/EU.
- **API suite** and data feeds; bespoke reporting; 24/7 support; "supporting more than 1,000 auctions every month" (claim).
- Verticals: Commercial, Industrial and Fine Art auctioneers; Insolvency, Recovery and Turnaround; Aerospace; Electronics; Consumer Returns; Mining; Automotive.

### Maxanet

Evidence layer: A (direct, official site).

Key observations:

- Positioning: "white-labeled online auction platform that's quick to launch with no long-term contracts"; "Since 1997, we've been at the forefront of online auctions" (lineage claim; a customer review describes the older "Legacy" software and the rebuilt "Next" platform).
- **One-stop**: "From integrated invoicing to Maxanet Pay credit card processing, we've got it all under one roof. It's the only place you need to login for managing your auctions."
- **White label**: "your bidders and data belong to you."
- **Consignors**: "Maxanet's powerful consignor feature makes it easy to manage consignor relationships and payouts. Track items, monitor sales performance, and generate detailed reports… Whether you have a few consignors or hundreds."
- **Bidder data**: "every bidder registration becomes part of your growing, secure database—fully owned and controlled by you. Use this valuable data to market upcoming auctions."
- **Mobile admin app**: "create and manage auctions anytime, anywhere… add items, capture high-resolution photos in real time" — field cataloging.
- **Reporting**: "full visibility into every aspect of your auctions… real-time data."
- **Credit card processing**: "bidders can pay instantly, and sellers get peace of mind with secure, PCI-compliant technology."
- Verticals: "wholesale liquidations, livestock auctions, real estate sales, or personal property auctions… Even non-auctioneers rely on Maxanet for handling closeouts, unclaimed property, and more."
- Extras: free WordPress website auction templates; native iOS/Android admin app; public demo site ("ABC Auctions").

### Wavebid

Evidence layer: A for the root page only; deep documentation unreachable (login-walled; help center transport error). Treated as thin.

Key observations:

- Root framing: "Auction software, simplified." Three pillars: **Cataloging, Marketing, Clerking** ("Super Simple Clerking, For the Dynamic Auctioneer"). Seller-centric value framing: "put a smile on your seller."
- Ecosystem: partners **Live Auction Group** and **Marknet Alliance**; customers HyperAMS, I-15 Auctions, Fahey Sales (auto/industrial segment). Site footer: "Copyright © Proxibid Inc. t/a Wavebid" — the product sits inside a bidding-platform family, consistent with the AMS↔bidding-platform bundling pattern.
- No further mechanics verifiable from reachable official sources; no claims made beyond the pillars.

## Cross-product Comparison

| Structure | BidWrangler | Bidpath | Maxanet | Wavebid | Assessment |
|---|---|---|---|---|---|
| Lots/items as the cataloged unit of sale (descriptions, photos, categories, IDs) | ✔ (items, categories, images, IDs) | ✔ (inventory management; mobile cataloging; catalogue editing) | ✔ (add items, capture photos; items listed) | ✔ (Cataloging pillar) | Core (all 4) |
| Sale/auction as the organizing event (create auction, catalog, publish) | ✔ (Creating Auctions 54 articles; Auction ID) | ✔ (create/upload/manage online auctions; sale-day functions) | ✔ (create/manage auctions; demo site) | ✔ (implied by pillars) | Core (all 4) |
| Bid capture with identified bidders | ✔ (registrations; clerking panel; auto-accept remote bids) | ✔ (full bidder management; webcast/timed bidding) | ✔ (bidder registrations; real-time bidding) | not directly observed | Core (3 of 4 direct) |
| Definite per-lot outcome (sold / no sale) | ✔ (SOLD/NO SALE clerking buttons; 'No Sale' on publish) | ✔ (sale-day → post-sale functions) | not directly observed (implied by invoicing) | not directly observed | Core (2 direct, 2 implied) — treated as core with cross-product reasoning |
| Buyer-side invoicing from the award | ✔ (Invoicing 14 articles; buyer's fees; Pay Now) | ✔ (Buyer Invoicing; buyer's online account; bulk reminders) | ✔ (integrated invoicing) | not directly observed | Core (3 of 4 direct) |
| Seller/consignor settlement | ✔ (Sellers and Settlements; settlement checks; mailing labels) | ✔ (post-sale and finance functions) | ✔ (consignor payouts) | ✔ ("put a smile on your seller" — seller-centric framing) | Core (all 4, directness varies) |
| Consignor/seller as managed party with relationship record | ✔ (sellers; seller item lists) | ✔ (client management) | ✔ (consignor feature: relationships, payouts, performance) | ✔ (seller-centric) | Core (all 4) |
| Bidder registration & qualification machinery | ✔ (per-auction registration; manual approval; card verification; DL scanner; Block Threshold) | ✔ (3D Secure bidder verification; full bidder management) | ✔ (bidder registration database) | not directly observed | Common (3 of 4 direct) |
| Reserves & estimates on lots | ✔ (high/low estimates; max-bid arrows reflect reserve status) | not directly observed | not directly observed | not directly observed | Common (1 direct) — kept qualitative |
| Buyer's premium / fee machinery | ✔ (flat-rate buyer's fees at item/auction/invoice level) | not directly observed (auction accounting system) | not directly observed | not directly observed | Common (1 direct) — market-universal but sampled evidence thin; kept qualitative |
| Timed/online bidding channel (staggered close, auto-extend, max bids, notifications) | ✔ (staggered close; auto-extend; variable closing speeds; max bids; outbid notifications) | ✔ (Timed Auctions product line) | ✔ (online auction platform; real-time bidding) | not directly observed | Common (3 of 4 direct) |
| Webcast/simulcast of live sales | ✔ (live video from smartphone; simulcast KB section) | ✔ (Webcast Auctions; HD low-latency A/V) | not directly observed | not directly observed | Common (2 of 4 direct) |
| Absentee/pre-bidding (max bids executed in live sale) | ✔ (max bids "bidding in the live auction automatically") | not directly observed | not directly observed | not directly observed | Common (1 direct) — kept qualitative |
| White-label bidder-facing platform + website | ✔ (branded platform, subdomain, apps, integrated website) | ✔ (platform integrated into client's website; bespoke websites; portals) | ✔ (white label; WordPress templates) | ✔ (implied by Proxibid family) | Common (all 4) — the companion-surface pattern |
| Reporting suite | ✔ (Reporting 10 articles; Auction Summary Totals; Vehicle Title Summary) | ✔ (key business reports; bespoke reporting) | ✔ (reporting feature) | not directly observed | Common (3 of 4 direct) |
| Staff roles & permissions | ✔ (Permissions Guide; Full Admin vs staff) | not directly observed | not directly observed (admin app) | not directly observed | Common (1 direct) — kept qualitative |
| Unsold-lot handling | ✔ ('No Sale' status; items missing on publish explained) | not directly observed | not directly observed | not directly observed | Common (1 direct) — kept qualitative |
| eCommerce extension (auction → direct sales) | not observed | ✔ (assets moved from auction to direct sales platform) | not observed | not observed | Optional (1 of 4) |
| Multi-company portals | not observed | ✔ (Auction Portals for multiple companies/departments) | ✔ (customer-built multi-affiliate marketplace — review) | not observed | Optional (2 of 4) |
| Multi-language/multi-currency | not observed | ✔ (translated lot descriptions; multi-currency accounting) | not observed | not observed | Optional (1 of 4) |
| Compliance modules | not observed | ✔ (compliance modules in Back Office) | not observed | not observed | Optional (1 of 4) |
| AI cataloging assistance | ✔ (titles/descriptions drafted from photos) | not observed | not observed | not observed | Optional (1 of 4) |
| Vertical apparatus (VIN/title; multi-parcel real estate; per-acre; livestock) | ✔ (VIN/title report; multi-parcel; per-acre) | ✔ (verticals listed: automotive, mining, aerospace…) | ✔ (livestock, real estate verticals) | ✔ (auto/industrial customer base) | Variant (vertical-dependent) |
| Marketing/outreach to bidder database | not directly observed | ✔ (auction alerts; watch lists) | ✔ ("market upcoming auctions" from bidder data) | ✔ (Marketing pillar) | Common (3 of 4) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software is not recognizable as an auction management system:

```text
Consignor / Seller (party whose goods are offered)
└── Lot (identified item or defined group cataloged as ONE bidding unit)
    └── Sale Event (bounded auction: catalog, order, defined close)
        └── Bid (recorded competitive offer from an identified bidder)
            └── Award (definite per-lot outcome:
                 sold to a specific winning bidder / no sale)
                ├── Buyer Invoice (price + charges → collection)
                └── Seller Settlement (proceeds − commission → payout)
```

Five invariants:

1. **Lot as the unit of sale** — goods are broken into identified, individually-biddable lots. Without lots there is no auction to manage.
2. **Sale event** — lots are gathered into a bounded sale with a catalog, an order and a defined close, run by the operator. Without the bounded event, it is an always-open marketplace, not an auction operation.
3. **Bid capture** — competitive offers against lots are recorded during the sale and attributed to identified bidders. Without recorded bids, the auction mechanics do not exist.
4. **Definite per-lot award** — every lot ends in a recorded outcome: sold to a specific winning bidder (respecting any reserve) or no sale. Without the award, bidding never resolves into a result.
5. **Operator-side commercial close** — the award drives the money loop: a buyer invoice (price plus charges) and a seller/consignor settlement (proceeds minus commission). Without the money loop it is a bidding tool, not a management system for the auction business.

Historical check (§24-style): a pre-internet auction house running on paper — consignment books, a printed catalog, paddle registration, a clerk with a clerking sheet, a cashier invoicing buyers, and settlement checks to sellers — satisfies all five invariants. Maxanet (operating since 1997) and Bidpath ("over 20 years") confirm the same spine across the online transition. Online bidding, white-label platforms, webcast video, AI cataloging and push notifications are NOT part of the definition — they are channels and machinery added around the spine.

### L1 — Common Mature Structure

Present in essentially all mature modern implementations; expected by the market but not definitional:

- consignment intake and consignor/seller records as managed parties (relationships, per-seller item lists, payouts)
- lot cataloging machinery: descriptions, photography (incl. mobile field capture), categories, identifiers, publish/unpublish staging, move/duplicate between sales
- estimates and reserves on lots (internal and/or bidder-visible)
- starting-bid configuration (at company/auction/lot levels in sampled products)
- bidder registration and qualification: per-sale registration, approval modes (automatic vs manual), card verification/deposits, terms acceptance, fraud controls, paddle/bidder numbers
- buyer's premium and fee/tax machinery applied on top of the hammer price
- timed/online bidding channel: scheduled staggered closing, anti-sniping auto-extension, max (pre-)bids, outbid notifications
- webcast/simulcast of live sales (remote bidders bid into the live room in real time)
- absentee/pre-bidding executed automatically in the live sale
- clerking surface for the sale (lot order, bid entry, sold/no-sale recording, acceptance control of remote bids)
- buyer invoicing with online payment collection and reminders
- seller settlement (settlement statements, checks/payouts)
- unsold-lot handling (no-sale status; re-offer or return to consignor)
- reporting (auction totals, sales, settlements; vertical reports)
- staff roles and permissions (clerk, cashier, cataloger, admin)
- white-label bidder-facing platform (web + mobile app) and integrated auction website as the companion surface
- bidder-facing conveniences: search, watchlist, notifications, support chat
- marketing outreach to the owned bidder database

### L2 — Variant / Optional Structure

- sale-format mix: live saleroom only, timed-online only, hybrid simulcast, sealed bid (sealed bid common in market, not directly evidenced in sample)
- vertical apparatus: automotive (VIN/title tracking), real estate (multi-parcel combinations, backup bidder, per-acre pricing), livestock (per-unit sales), charity/benefit auctions (paddle raises, silent auctions), government surplus/insolvency
- eCommerce extension (moving assets between auction and fixed-price direct sales)
- multi-company/multi-department auction portals
- multi-language and multi-currency operation
- compliance modules (regulatory/record-keeping depth)
- deployment and commercial posture: SaaS subscription vs white-label; data-ownership guarantees; marketplace aggregation vs single-house branding
- AI cataloging assistance depth

### L3 — Vendor-specific (research notes only)

- BidWrangler: "BAM" naming; 8-digit Item ID / 6-digit Auction ID; Buyer's Guide paper clerking sheet as the only image-bearing sheet; Pay Now Threshold; Block Threshold; unclaimed accounts; driver's-license scanner; AVIF image serving; Matterport tours; variable closing speeds; First Bid Message; complaint/bounce counts; separate Bidders vs Registrations CSV imports; permanent-paddle bulk removal; Thrive client conference; "No Reserve" podcast; data-ownership policy page.
- Bidpath: SAM / Go Auction / AIM product names; SagePay 3D Secure (UK/EU); named gateways (Authorize.net, Paytrace, NMI); portal cross-product promotion; client/country/auction-volume figures (vendor claims).
- Maxanet: Maxanet Pay; "Legacy"→"Next" platform lineage; WordPress auction templates; ABC Auctions demo site; Google-review ratings display.
- Wavebid: Marknet Alliance and Live Auction Group partnerships; Proxibid parentage (footer); named customers.

## Vendor-specific Findings

See L3. None enter the canonical model. Notable: the *companion bidding platform* is cross-product as a pattern (all four sampled products bundle or belong to a bidding-platform family), but each vendor's platform is its own branded surface — the canonical statement is "AMS products commonly bundle or integrate a bidder-facing bidding surface", not "AMS includes a specific platform".

## Boundary Findings

1. **vs Online Auction Platform (sibling leaf, §05.18)** — the central boundary. The Online Auction Platform is the **bidder-facing marketplace** where bidding is the transaction mechanism and the user population is bidders/sellers at market scale; the AMS is the **auction operator's system of record** where the users are the auction company's staff and the objects are lots, sales, awards and settlements. Removal tests both ways: strip the operator back-office (cataloging, clerking, invoicing, settlement) from a bundled product → what remains is an Online Auction Platform; strip the bidder-facing marketplace → what remains is the AMS. The market bundles the two (every sampled AMS ships a white-label bidding surface; Wavebid is owned by a bidding-platform company), but bundling does not merge the Types — the two sides have different users, objects and workflows. Both leaves remain distinct Types; no taxonomy change proposed.
2. **vs Artwork Consignment Management** — both manage consignors and money owed to them, but the centers differ: consignment management centers the custody-and-terms relationship of unique works *outside* a sale event (placed → on consignment → sold or returned under recorded terms); the AMS centers lots moving *through* a sale event to a competitive award. Remove the sale event and bidding from an AMS → consignment-style tracking remains; add a saleroom sale to consignment management → an auction operation.
3. **vs E-commerce Platform / Checkout** — fixed-price purchase at a posted price vs price discovered through competitive bidding resolved by an award. No lot/hammer/settlement semantics in plain e-commerce.
4. **vs Classifieds Platform / Listing Marketplace** — listings with negotiation or "best offer", no timed competitive close, no clerked award, no premium/settlement machinery.
5. **vs Event Management Platform** — an auction sale is an event, but the event-management center is attendance, agenda and registration of *attendees*; the AMS center is the lot lifecycle and the money loop. An auctioneer does not use event software to clerk lots.
6. **vs E-sourcing / procurement reverse auctions (§10)** — same competitive-bidding mechanics, reverse direction (buyer solicits, suppliers bid prices down, award = contract); different users, objects and rules. Not this Type.
7. **vs Fundraising / charity auction tooling** — benefit auctions run the same lot→bid→award→settlement core with charity-specific apparatus (paddle raises, donor recognition); treated as a Variant posture of this Type unless a future dedicated leaf proves otherwise.
8. **vs Invoicing / Billing applications** — buyer invoicing is a capability inside the AMS driven by the award; standalone invoicing lacks lots, sales, bidding and settlement-to-seller.

## Uncertainties

- **Auction Flex** (major US full-service suite) unreachable (403 + transport error) — the classic installed-base segment is unverified; no claims made about it.
- **Wavebid** deep documentation login-walled; help center unreachable — only the root pillars evidenced; its clerking/cataloging mechanics are inferred from positioning only and are not asserted anywhere.
- **BidWrangler KB article bodies** not retrievable (index/abstracts only) — mechanics such as default auto-extend durations, settlement formula details, and exact approval workflows are NOT asserted; only what the abstracts state.
- Settlement arithmetic (commission structures, premium splits, tax treatment of consignor proceeds) not evidenced at formula level in any sampled product — kept qualitative.
- Reserves/estimates and buyer's premium are market-universal in experience but directly evidenced in only one sampled product each — kept as Common with qualitative wording, not Core.
- Sealed-bid format not directly evidenced in the sample; not claimed.
- Regional/continental-European saleroom software under-sampled (Auctionary's domain now resolves to Bidpath); the regional check rests on Maxanet's 1997 lineage and Bidpath's 27-country footprint rather than a distinct regional product.
- Vendor scale figures (750+ clients, 1,000+ auctions/month, "since 1997") are vendor claims, not verified facts.

## Final Synthesis

An Auction Management System is the auction operator's side of the auction business: software whose world is built from lots (identified, individually-biddable units of sale), gathered into bounded sale events, where recorded competitive bids from identified bidders resolve into a definite per-lot award — sold to a specific winning bidder or no sale — and the award drives the money loop: a buyer invoice on one side, a seller/consignor settlement on the other. Around this spine, mature products add the machinery the market expects: consignment intake and consignor records; cataloging with photos, estimates, reserves and starting bids; bidder registration and qualification (approval modes, card verification, fraud controls, paddle numbers); a clerking surface for sale day; timed-online bidding with staggered closing and auto-extension; webcast simulcast of live sales; buyer invoicing with premium/tax and online payment; seller settlement statements and payouts; unsold-lot handling; reporting; staff permissions; and a white-label bidder-facing platform with website and mobile app as the companion surface. The defining boundary: the AMS is operator-side — its users are the auction company's staff — while the Online Auction Platform is bidder-side; the market bundles the two, but stripping either side leaves the other Type intact. Remove the sale event and bidding, and only consignment/custody tracking remains; remove the competitive award, and it is fixed-price e-commerce; remove the money loop, and it is a mere bidding tool. The historical check holds: the paper-era auction house (consignment book, printed catalog, paddle registration, clerking sheet, cashier, settlement checks) satisfies the same five-part spine, so the definition is not an artifact of the online-bidding era.
