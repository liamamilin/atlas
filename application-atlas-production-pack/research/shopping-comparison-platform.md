# Research Notes — Shopping Comparison Platform

## Research Goal

Understand the Shopping Comparison Platform as an Application Type: its defining structure, how real products implement it, how shoppers and merchants work with it, and where its boundaries lie against neighboring Types — especially Comparison Platform (§02.10, processed, which carries a joint-review flag against this leaf), Shopping Search Engine (§05.05 sibling, unprocessed), Metasearch Engine (§02.02, unprocessed), Online Marketplace (§05.02, unprocessed), Deal Discovery Platform (§05.05 sibling, unprocessed), and Product Discovery Application (§05.05, processed).

## Initial Boundary

- Leaf: **Shopping Comparison Platform** (§05.05 Shopping Discovery; siblings: Shopping Search Engine, Product Discovery Application, Deal Discovery Platform).
- Working hypothesis before research: a platform where a shopper with a specific product in mind sees offers for that same product from multiple sellers — price, delivery, seller reputation — and clicks through to a seller to buy. Classic "price comparison site / comparison shopping engine".
- Nearest confusion risks:
  - Comparison Platform (§02.10): compares *different* options on attributes, ends in a choice; this Type compares *offers for the same item* across sellers, ends in a purchase.
  - Shopping Search Engine: query-first retrieval vs comparison-centered offer set.
  - Metasearch Engine: query-time aggregation vs persistent owned product/offer registry.
  - Online Marketplace: hosts the transaction vs routes to sellers.
- Prior pass context: `research/comparison-platform.md` §Boundary Findings already defined the seam ("same SKU, many sellers → Shopping Comparison Platform; different products/plans/suppliers → Comparison Platform") and flagged joint review.

## Research Questions

1. What is the unit of comparison — what exactly is held as a record? (product? offer? both?)
2. How do offers get into the system (merchant feeds, crawls, marketplaces) and how are they matched to a shared product identity?
3. What does the shopper's loop look like end to end, and where does it end (outbound click vs hosted checkout)?
4. What offer attributes are compared (price, delivery, stock, condition, seller rating, payment methods)?
5. How do price accuracy, ranking independence, and commercial model work (CPC, traffic payment, sponsored placement)?
6. What personal/tracking machinery exists (price history, alerts, wishlists, comparison lists)?
7. What does the merchant side look like (registration, feeds, billing)?
8. Where are the boundaries vs the six neighboring Types listed above?
9. Historical check: does the definition hold for the 1990s-generation price-comparison engines and for regional products?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different market positions:

| Product | Market position | Philosophy | Reachability |
|---|---|---|---|
| **PriceRunner** (UK/SE/DK + Klarna markets) | European consumer-general pure-play, Klarna-owned since 2022, founded 1999 | consumer trust: independence claims, buyer protection, financing integration, price tracking | ✅ rich (home, about, FAQ, buyer protection, account, product page) |
| **Geizhals** (AT/DE/EU, since 1997) | DACH electronics-specialist, community-heavy | spec-sheet depth, detailed offer tables, forum, test-review aggregation | ✅ rich (home, product page incl. full offer list, merchant-partner page) |
| **Shopping.com** (US, eBay-owned) | classic US comparison-shopping engine | UPC-keyed item model, provider-sourced data | ✅ thin (home, top products) |

Market anchors used qualitatively (unreachable this pass): Google Shopping (support + site timed out), idealo (403), camelcamelcamel (403), Kelkoo (403), Prisjakt (403), Yahoo Shopping (403), PriceGrabber (empty response).

## Sources

Research date: 2026-09-07. All observations below are Evidence Layer A (directly observed on the fetched page) unless marked B (cross-product) or C (canonical inference).

- PriceRunner UK — https://www.pricerunner.com/ (home), https://www.pricerunner.com/info/about-pricerunner , https://www.pricerunner.com/info/faq , https://www.pricerunner.com/info/buyer-protection , https://www.pricerunner.com/info/pricerunner-account , product page https://www.pricerunner.com/pl/1-3520818514/Mobile-Phones/Honor-600-Pro-6.57-AMOLED-Smartphone-Compare-Prices
- Geizhals EU — https://geizhals.eu/ (home), product page https://geizhals.eu/sony-playstation-5-pro-2tb-weiss-a3298140.html , merchant/partner portal https://unternehmen.geizhals.at/haendler/
- Shopping.com — https://www.shopping.com/ (home), https://www.shopping.com/topProducts.html

## Product A — PriceRunner (Evidence Layer A)

### Positioning (About + FAQ)
- "PriceRunner is an independent price comparison service that helps consumers find better products and better prices." "Free to use."
- "Is PriceRunner an online shop? No – PriceRunner is a comparison service. You complete your purchase directly with the retailer."
- Scale claim (home): "compare prices on 4.8 million products from 5,100 shops" (marketing figure — recorded as claim).
- Ownership: "owned by the Swedish bank Klarna and became part of the Klarna Group in 2022"; "operates as an independent comparison service". Founded Sweden 1999, "one of Europe's first price comparison services". Markets: UK/SE/DK sites + inside the Klarna app in 10 more markets.
- Independence: "We show prices from both retailers that partner with us and those that don't. No retailer can pay for a higher position in the price comparison." Monetization: "Retailers pay for traffic when users click through from PriceRunner. This does not affect how prices are ranked." Also: "Some retailers pay for additional visibility" (sponsored placements exist alongside).

### Data mechanics (FAQ)
- "We collect prices from different retailers and display them in one place so you can easily compare and choose the best offer."
- Update cadence: "Most prices are updated at least once a day – often more frequently. Always double-check the price on the retailer's website."
- Price display: "Delivery costs vary between retailers, so prices are shown without delivery by default. You can choose to view prices including delivery." "All prices include VAT."
- Ranking: "The lowest price (excluding delivery) is shown first. If prices are identical, sorting is based on: Active links, Delivery information, Stock status, Delivery time."
- Coverage: "We aim to show all retailers that deliver to your country – both local and international."
- Error handling: "You can report a pricing error directly on the product page."
- Retailer choice guidance: consider "Price, Delivery, Return policy".

### Product page (Honor 600 Pro smartphone)
- Product record: name, image gallery, aggregate rating (4.7), price range ("from £699.00 to £899.99"), popularity rank ("312 in Mobile Phones"), variant tabs (All / Black), tabs: Prices / Reviews / Price history / Product details / Features.
- Offer list: each offer = retailer logo+name, retailer's own product title, delivery line ("Free shipping, 1-4 days" / "£5.99 shipping, 1-3 days"), price, financing line ("Or 3 payments of £233.00/mo" — Klarna), "Lowest price" badge, one "Recommended AD" sponsored offer, retailer rating on some offers (e.g. OnBuy 4.8 (12 ratings)).
- Routing: every offer click goes through a "gotostore" transition API → outbound to the retailer.
- Condition: "Pre-owned from £699.00" — condition appears in the offer set.
- Tools on page: Price alert; Compare (a /pc? URL — product-vs-product compare tool exists as a supporting feature).

### Account features (account page)
- Price tracking + alerts: notified when "the price drops" or "the price reaches your preferred level", via email or notifications.
- Lists: create wishlists/shopping lists, "see the total price of your list", "find the cheapest way to buy all items", share lists.
- Price history: "see how prices have changed over time", "check if a deal is genuine", "spot trends, for example around major sales events".
- Account optional: "you can use PriceRunner without an account."

### Buyer Protection (product-specific, documented)
- "Free coverage up to £5,000"; valid at "over 400 selected retailers on PriceRunner"; "Automatically activated when you have an account"; covers "product is not delivered, arrives damaged, and the retailer doesn't resolve the issue"; "Look for the Buyer Protection symbol next to the retailer name"; "Complete your purchase directly with the retailer – we'll step in if something goes wrong."

### Home surface
- Category tree (Home, Garden, Kids, Toys, Gaming, Electronics, Phones, Sound & TV, Photography, Clothing, Health, Sports, DIY, Mobility), "Top deals of the day" (deal layer), product cards showing name, rating, price, original price + discount %, "9+ stores" (offer count), financing line. Blogs section.

## Product B — Geizhals (Evidence Layer A)

### Positioning (home footer)
- "Geizhals ist ein unabhängiges Preis- und Produktvergleichs-Portal, das mittels detaillierter Filter und vielfältiger Features eine optimale Hilfestellung bei der Kaufentscheidung bietet." (independent price and product comparison portal).
- Operated by Preisvergleich Internet Services AG; "Copyright © 1997-2026" (founding generation).
- Live stats footer: "388.185 aktive Händler / 3.781.472 gelistete Artikel / 253.798.669 Preise / 8.154.539 Beiträge im Forum" + "Letzte Aktualisierung: 2026-09-07, 16:09" (figures as displayed; recorded as claims).
- Country selection: geizhals.at / geizhals.de / geizhals.eu (multi-market). Sister site tarife.at (utility-tariff comparison — the §02.10 Comparison Platform family lives in the same company as a separate product).

### Product page (PS5 Pro) — the offer table in full detail
- Product identity: name + manufacturer part number ("1000046526"), variant grouping ("Alle 4 Varianten anzeigen"), category breadcrumb, "Gelistet seit 2024-09-11" (listed since).
- Product data: 15 "Produkteigenschaften" (spec sheet: CPU, GPU, RAM, storage, ports, wireless, power, dimensions, weight, scope of delivery); "Info beim Hersteller" link to the manufacturer.
- Evaluation layer: user rating (4.7 / 446 Bewertungen) + "Testbewertung: 80 aus 1 Testbericht" (normalized editorial test-review score) + 8 linked external test reports (trustedreviews, futurezone, pcgameshardware, heise, golem, engadget, polygon) with quotes.
- Price range: "Aktueller Preisbereich € 1128,00 bis € 3333,00".
- Tools: "Preisentwicklung öffnen" (price history), "Preisalarm setzen" (price alert), "Zur Wunschliste hinzufügen" (wishlist), "Zur Vergleichsliste hinzufügen" (comparison list — product-vs-product), "Feedback senden".
- Offer list ("20 Angebote") with filters:
  - "inkl. Versand" (include shipping), "nur Abholung" (pickup only)
  - provider country (AT/DE/PL/UK), stock status ("lagernd beim Händler" / "kurzfristig lieferbar")
  - destination country ("Versand nach Österreich/Deutschland/Großbritannien/Polen") + "PLZ, Ort oder Koordinaten" / "aktuellen Standort verwenden" (postal code / current location)
  - payment method ("günstigste Zahlart": Kreditkarte, PayPal, Vorkasse, Nachnahme)
  - "Letztes Preisupdate: 2026-09-07, 16:09" + "Aktualisieren" (refresh)
- Each offer row: price + "zum Angebot" (outbound redir link) + payment logos + merchant country flag + merchant name/logo + marketplace attribution ("(via ebay.de)") + merchant info page + AGB link + merchant rating ("Bewertung: 3.9 von 5 Sternen, 5700 Bewertungen" or "Dieser Händler hat keine gültigen Bewertungen" + "Händler bewerten!") + delivery time + stock status + per-country shipping/payment matrix ("Deutschland: Kreditkarte, PayPal € 5,90." / "Österreich, UK, Polen…: Kein Versand möglich.") + merchant's own product title + price timestamp ("Preis vom: 2026-09-07, 14:10:18 (Preis kann jetzt höher sein!)") + offer grouping ("15 weitere Angebote von eBay.de" / "Nicht gruppieren").
- Empty state: "Es gibt derzeit keine Anbieter für dieses Produkt (mit diesen Filterkriterien)."
- Merchant page: /merchants/<id> with ratings, branch list ("Abholung in den Filialen möglich" — store pickup).
- Disclaimer: "Alle Angaben ohne Gewähr. Die gelisteten Angebote sind keine verbindlichen Werbeaussagen der Anbieter." (offers are not binding advertising statements). VAT display notes per offer.
- Community: forum (8.15M posts), user ratings on products and merchants.
- Related products ("Siehe auch") + "Top-10 in Konsolen" (category ranking by popularity).

### Merchant/partner side (unternehmen.geizhals.at/haendler)
- "Onlineshop anmelden" (register your online shop), "Technische Details" (feed/integration specs), "Kooperationen".
- Monetization: "Vertrieb von Shoplistungen auf CPC-Basis" (shop listings sold on a CPC basis); two documented tiers: with Geizhals logo embedded (€0,38 pro Klick) vs without (€0,41 pro Klick); plus affiliate programs, account management, ad-space sales.
- Network: partner sites heise, Winfuture, Pepper, golem, techstage, Testberichte, PCGH, ComputerBase, Vergleich.org; affiliate publisher program.

## Product C — Shopping.com (Evidence Layer A, thin)

- Self-label: "Shopping Online at Shopping.com | Price Comparison Site" (page title).
- Structure: "Site Index" (/taxonomy.html — category taxonomy), "Top Products" (/topProducts.html), "Top Deals" (/topOffers.html).
- Item model: product pages keyed by UPC/GTIN — `/item.html?id=00865116238651&provider=3` (the `provider` parameter indicates sourced data feeds). Item records carry long retailer-style titles and spec fragments.
- Content quality is thin (eBay data-feed era); no help center reachable. Used only as evidence of the UPC-keyed item model and classic positioning.

## Cross-product Comparison

| Dimension | PriceRunner | Geizhals | Shopping.com |
|---|---|---|---|
| Unit of comparison | offers for one product record | offers for one product record (MPN-keyed) | items keyed by UPC |
| Offer attributes | price, delivery cost/time, retailer, financing, condition, retailer rating, "Lowest price" badge | price, delivery cost/time per destination country, payment methods, stock status, merchant rating, merchant country, marketplace attribution, price timestamp | (not directly observed) |
| Presentation | offer list on product page, price-sorted, "lowest price first" documented | offer table with filter bar (shipping/pickup, countries, stock, payment), price-sorted | item list |
| Purchase routing | outbound "gotostore" click-through; "You complete your purchase directly with the retailer" | outbound "zum Angebot" redir; offers "keine verbindlichen Werbeaussagen" | outbound (assumed from model; not directly observed) |
| Product info layer | specs, features, reviews tabs, images, variants | 15-property spec sheet, manufacturer link, test-review aggregation, user ratings | title + spec fragments |
| Price machinery | price history, price alerts (drop / target level), "check if a deal is genuine" | price history ("Preisentwicklung"), price alerts, 30-day price-change basis, last-update timestamp | — |
| Personal layer | account (optional): lists with totals, cheapest-basket, sharing, tracking | wishlists, comparison list, settings, login | — |
| Trust machinery | independence claims, buyer protection (product-specific), price-error reporting, "double-check on retailer's site" | merchant ratings, "ohne Gewähr" disclaimer, non-binding offers, price display notes | — |
| Commercial model | retailers pay for traffic per click; sponsored visibility exists; "no retailer can pay for a higher position" | CPC shop listings (documented per-click rates), affiliate, ad space | (eBay-owned; not observed) |
| Community | blogs, ratings | forum (8M+ posts), ratings, test reports | — |
| Scope | consumer-general, multi-market (UK/SE/DK + Klarna app markets) | electronics-heavy origin, broadened categories, AT/DE/EU | US general |

Evidence Layer B (cross-product commonality, 2–3 products): product-anchored offer sets; price-led sorted offer lists; outbound click-through routing; per-offer delivery/condition/seller attributes; price history + alerts; wishlists/saved lists; last-update timestamps and "price may have changed" disclaimers; merchant ratings; sponsored placements alongside organic price ranking; category taxonomy + search entry; CPC/traffic-payment merchant model.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Canonical product record (one identified item, shared across sellers)
└── Multi-seller offer set (per seller: price + purchase conditions)
    └── Aligned offer comparison (offers presented comparable, price-led)
        └── Purchase routing (the loop ends in a handoff to the seller to buy)
```

Removal tests:
- Remove shared product identity → offers can't be aligned; the product becomes a query-time results page (shopping search engine / metasearch), not a comparison platform.
- Remove multi-seller offers → single-seller catalog = storefront.
- Remove aligned comparison presentation → a product directory or feed.
- Remove purchase routing → a price database / price-tracking data site, not a shopping application.

Historical check (§24): the founding generation of price-comparison services (mid-1990s onward; PriceRunner self-documents 1999 "one of Europe's first", Geizhals copyright from 1997) operated as product-anchored vendor price lists with click-through routing — the same core without price history, alerts, buyer protection, financing, apps, forums, or sponsored placements. (Specific 1990s products beyond the two documented ones are recalled qualitatively, not verified this pass.) Regional products (DACH, Nordics) fit unchanged. Platform-embedded forms (search-engine shopping tabs) fit the core but sit at the seam with Shopping Search Engine — see Boundary Findings.

### L1 — Common Mature Structure

- Category taxonomy + search/browse entry into the product catalog.
- Offer attribute set: price, delivery cost/time, stock status, condition (new/used), seller identity + rating, payment methods, seller's own product title.
- Price-led sorting (lowest first) and filters (price, brand, rating, popularity, seller country, shipping, payment).
- Price history and price alerts (drop / target-level), with "is this deal genuine" framing.
- Product information layer: images, spec sheets, variants, user ratings, editorial/test-review aggregation.
- Personal layer: optional account, wishlists/saved lists (list totals, sharing), comparison lists.
- Sponsored/advertised placements alongside the organic price ranking, visually marked.
- Merchant-side supply: shop registration, product feeds, per-click billing; merchant info pages with ratings.
- Trust machinery: independence claims, last-update timestamps, "price may have changed / confirm at retailer" disclaimers, price-error reporting, non-binding-offer disclaimers.
- Multi-market scoping: shipping destination, country selection, VAT display.

### L2 — Variant / Optional

- Checkout posture: outbound click-through is the dominant pattern; hosted checkout appears in some products and drifts toward marketplace territory (not directly observed in the reachable sample — kept qualified).
- Vertical scope: consumer-general vs electronics/spec-specialist vs regional.
- Business model: per-click CPC (rates documented at one product), traffic payment, affiliate, ad space; free-listing models exist in the wider market (not verified this pass).
- Buyer protection (product-specific in sample: PriceRunner).
- Financing integration (product-specific in sample: Klarna lines on PriceRunner).
- Community layer: forums, user ratings, test-review aggregation (Geizhals pole).
- Marketplace indexing: offers attributed "(via ebay.de)", grouped per marketplace (Geizhals).
- Deal/sale surfaces as a secondary layer (PriceRunner "Top deals of the day").
- Local/store dimension: pickup-only filters, branch pickup, postal-code/location scoping (Geizhals).
- Apps and browser extensions (apps documented at Geizhals; extensions recalled qualitatively — not verified).

### L3 — Vendor-specific (stays here, not in the final document)

- PriceRunner: Buyer Protection up to £5,000 at 400+ selected retailers, auto-activated with account; Klarna ownership and financing lines; "find the cheapest way to buy all items" list feature; "no retailer can pay for a higher position" independence formula; identical-price tie-breaking order (active links → delivery info → stock status → delivery time); "most prices updated at least once a day".
- Geizhals: CPC rates €0,38/€0,41 per click (with/without logo embedding); test-review normalization ("Testbewertung" 0–100 scale from external reviews); per-country shipping/payment matrices per offer; offer grouping per marketplace; forum; showrooms (manufacturer showcases); tarife.at sister site; live stats footer; "Gelistet seit" dates.
- Shopping.com: UPC-keyed item IDs with `provider` data-feed parameter.

## Vendor-specific Findings

See L3. Additionally: PriceRunner's buyer protection shifts it from pure information intermediary toward transaction-adjacent trust provider — but the purchase itself still happens at the retailer, so the core is unchanged.

## Rejected Findings

- "Shopping comparison = Google Shopping" — rejected: Google Shopping was unreachable this pass; no claims about it are made beyond market-anchor status. Its center-of-gravity (query-first, search-embedded) is treated as a boundary case, not the definition.
- "Comparison shopping engines are metasearch" — rejected as a definition: metasearch aggregates third-party results at query time; every sampled product maintains a persistent product catalog with attached offers (product pages survive between visits, carry specs/ratings/history). Aggregation-at-query-time is a different structure.
- "Hosted checkout is part of the Type" — rejected for the core: the reachable sample routes out; hosted checkout is a variant that drifts toward marketplace.
- "Deals/coupons are the unit" — rejected: deals appear as a secondary layer (PriceRunner deals section); the unit is the offer on a product record.
- "Price tracking defines the Type" — rejected: tracking is L1; a tracker without multi-seller offer comparison (camelcamelcamel-class, unreachable this pass) fails the L0 and is a boundary case.

## Boundary Findings

### vs Comparison Platform (§02.10, processed) — joint-review flag DISCHARGED

- Seam confirmed from this side: Shopping Comparison compares **offers for the same product across sellers** and ends in a purchase handoff ("You complete your purchase directly with the retailer" — PriceRunner; "zum Angebot" — Geizhals). Comparison Platform compares **different options/plans/suppliers on attributes** and ends in a choice + apply/switch.
- Center-of-gravity test: the center here is the product page with its offer table (one product, many sellers); the center there is the results table across options (many options, aligned attributes).
- Overlap acknowledged: shopping comparison products carry product-vs-product compare tools (PriceRunner "Compare" /pc? URL; Geizhals "Vergleichsliste") as supporting features; comparison platforms can show price tables. Neither overlap changes the centers. Removal test both directions: remove the offer structure, keep product-vs-product attribute comparison → still a Comparison Platform; remove the attribute comparison across different products, keep same-SKU offers → still a Shopping Comparison Platform.
- Same-company evidence: Geizhals' operator runs tarife.at (utility tariff comparison) as a separate product — the two Types coexist as distinct products under one roof.

### vs Shopping Search Engine (§05.05, unprocessed) — flag for that leaf

- Proposed seam: query-first retrieval across sellers (results are ranked product/offer links assembled at query time) vs comparison-centered offer set on a persistent product record. Products commonly do both (search → product page → offer table); the center-of-gravity decides. Google Shopping sits at this seam (unreachable this pass — noted as uncertainty).

### vs Metasearch Engine (§02.02, unprocessed) — flag for joint review

- Proposed seam: metasearch aggregates third-party results at query time without a persistent owned registry; this Type maintains a persistent product catalog with attached offers (product pages, price history, alerts all presuppose the registry). Travel metasearch is the classic metasearch pole; "comparison shopping engine" is sometimes classed as metasearch in market literature — the persistent-registry test separates them.

### vs Online Marketplace (§05.02, unprocessed)

- Marketplace = transaction venue (unified catalog/checkout, platform in the middle of payment); Shopping Comparison = routing layer (purchase completed at the retailer). Geizhals indexing eBay sellers ("via ebay.de") shows the relationship: the marketplace is a *source* of offers for this Type, not the venue of it.

### vs Deal Discovery Platform (§05.05, unprocessed)

- Deal platform's unit is the time-limited deal/offer event; here the unit is the stable offer record on a product. Deals appear as a secondary surface (PriceRunner "Top deals of the day").

### vs Product Discovery Application (§05.05, processed)

- Confirmed from that pass's own related-types entry: discovery is query-independent browsing for inspiration; comparison is decision-driven for an item the shopper has already chosen. Sibling test holds.

### vs E-commerce Platform / Online Store Builder (§05.01)

- Tooling for a seller's own storefront (single-seller catalog) vs multi-seller aggregation with routing out.

### Boundary case — price-tracking tools

- camelcamelcamel-class trackers hold price history for products at one seller without a multi-seller offer set → fail L0 → adjacent tool, not this Type. Unreachable this pass; recorded qualitatively.

## Uncertainties

1. Google Shopping (the largest market anchor) unreachable — its consumer-side mechanics (free listings, hosted-checkout status, price-tracking) are unverified; no claims made.
2. idealo, Kelkoo, Prisjakt, camelcamelcamel, Yahoo Shopping, PriceGrabber unreachable (403/timeout/empty) — the European pure-play and price-tracker poles rest on PriceRunner + Geizhals evidence only.
3. Hosted-checkout variant: not directly observed in the reachable sample; kept qualified in the final document.
4. Shopping.com's offer table and routing were not directly observed (thin fetch); only its item model and positioning are used.
5. Historical 1990s products (Pricewatch, Bargain Finder, PriceGrabber, Shopzilla, Nextag) recalled qualitatively, not verified live; the historical check rests on the two documented founding-era products (PriceRunner 1999, Geizhals 1997) plus the structural argument.
6. Scale figures (4.8M products / 5,100 shops; 388k merchants / 3.78M items) are vendor-displayed claims, recorded as claims.

## Final Synthesis

A Shopping Comparison Platform is a purchase-routing comparison application whose defining core is exactly four structures: the canonical product record (one identified item shared across sellers — remove → query-time search results), the multi-seller offer set attached to it (per seller: price + purchase conditions; remove → storefront), the aligned offer comparison (offers presented comparable, price-led; remove → directory/feed), and the purchase routing (the loop ends in a handoff to the seller to buy; remove → price database). Mature products commonly add: category/search entry, rich offer attributes (delivery, stock, condition, seller rating, payment methods), price history + alerts, product info layers (specs, reviews, test aggregation), personal lists, sponsored placements beside organic price ranking, merchant-side feed/CPC supply, trust machinery (independence claims, update timestamps, non-binding disclaimers, error reporting), and multi-market scoping. Variants: general vs vertical-specialist scope, regional vs multi-market, pure-play vs search-embedded, marketplace-indexing, checkout posture, buyer protection / financing / community layers. The Type's sharpest seams: Comparison Platform (same-SKU offers vs different-product options — joint review discharged, both Types kept), Shopping Search Engine and Metasearch Engine (query-time retrieval vs persistent owned registry — flags left for those leaves), Online Marketplace (routing vs venue), Deal Discovery (offer record vs deal event), Product Discovery (decision-driven vs inspiration-driven).
