# Research Notes — Consignment Management Platform

> Internal research file. Methodology terms (L0/L1/L2/L3, evidence layers) are used here only, not in the final application document.

## Research Goal

Understand what a Consignment Management Platform is as an Application Type: the core object model (consignor accounts, consigned items, splits, sales, settlements), the workflows (intake → price → floor → sell → settle), the rules that govern the consignor–store money relationship, and the boundary against its dense neighbor cluster (Resale Marketplace, Recommerce Platform, Retail POS, Retail Inventory Management, Online/Vendor Marketplace, Auction Management System, Artwork Consignment Management).

## Initial Boundary

**Working hypothesis (pre-research):** the operating system of a consignment store — a small business that takes custody of individuals' items, prices and sells them at a counter (and increasingly online), and pays the item owner (consignor) an agreed share of each sale price.

**Adjacent types flagged by prior sibling passes (must discharge from this side):**

1. **recommerce-platform (§05.19, processed)** — flagged joint review: "both run a consign-in → sell → settle loop... candidate outcomes are two Types (store-operator vs brand-program) or a consolidation view" (research/recommerce-platform.md §Boundary Findings).
2. **resale-marketplace (§05.19, processed)** — custody seam: "seller retains possession and self-lists vs operator intake/pricing/sale" (research/resale-marketplace.md; resale-marketplace.md related-types table records: "operator takes custody of consignors' items and manages intake, pricing, and sale; sellers do not self-list or retain possession").
3. **artwork-consignment-management (§27, processed)** — prior art on consignment-centered leaves: that leaf ships as a module inside gallery/artist tools; flagged module-delivery pattern.

**Nearest confusions to resolve:** Retail POS (the transaction surface), Retail Inventory Management (stock records), Online Marketplace / vendor-mall mode (shared-venue selling), Auction Management System (consignment intake feeding auction events).

## Research Questions

1. What is a consignor account and what does it carry (contact, terms, payout method, balance)?
2. What is a consigned item record: intake, pricing (manual vs rules), description/photos, categories, tags/barcodes?
3. What lifecycle states does an item pass through (intake → floor → sold / returned / expired)? Is there a consignment period?
4. How do splits work (per consignor, per item, tiered; discount interaction)?
5. How does settlement work: balance accrual, payout methods (cash/check/ACH/store credit), scheduling, statements?
6. What other inventory bases exist (buy-outright, retail-owned, donated) and how do they coexist with consigned stock?
7. What surfaces exist: POS, inventory tables, account detail, payout screens, consignor portal, reports?
8. What rules matter: ownership/asset accounting, payout permissions, expiry/returns, discount effects on splits?
9. Where exactly are the seams: vs Resale Marketplace (custody), vs Recommerce (operator identity), vs Retail POS/Inventory (ownership basis), vs vendor-mall marketplace mode?
10. Historical check: does a paper-era consignment shop (consignment book, tags, cash register, payout ledger) satisfy the core?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers + different eras.

| Product | Pole | Access achieved |
|---|---|---|
| **ConsignCloud** (ConsignCloud LLC) | cloud-native modern, strong Tier-1 help center, transparent plans | Product page + help center home + Accounts & Items collections + 3 Tier-1 articles (Inventory Types, Account Balances, Consignor Payouts) |
| **SimpleConsign** (Traxia) | cloud SMB leader (3,100+ shops claimed), vendor-mall expansion | Product homepage + Consignor Payouts page + Inventory Management page (Tier-2 feature pages with FAQ) |
| **Liberty / Liberty Cloud** (ResaleWorld) | enterprise/veteran pole (30+ years, thousands of stores, 22 countries; desktop Liberty REACT heritage + cloud) | Product homepage (image-heavy; feature text extracted) |
| **Resell4.me** (successor of Best Consignment Shop Software / BCSS, since 2001) | budget/veteran pole, founder-articulated minimum definition, migration evidence from desktop BCSS | Product homepage with detailed FAQ + comparison |

**Rejected/alternative samples:** ConsignPro (www.consignpro.com) — returned 403 on fetch, abandoned after one attempt per network rules; the desktop-veteran pole is instead covered by Resell4.me/BCSS heritage (since 2001, BCSS was a desktop product, migration preserves "consignors, inventory, balances, and sales history... barcodes intact") and by Liberty REACT's desktop heritage.

## Sources

- ConsignCloud — https://www.consigncloud.com/ (product; fetched 2026-09-07)
- ConsignCloud Help Center — https://help.consigncloud.com/en/ ; collections: Accounts (https://help.consigncloud.com/en/collections/19720102-accounts), Items (https://help.consigncloud.com/en/collections/19717324-items); articles: Understanding Inventory Types (…/16396903), Account Balances (…/16445776), Consignor Payouts (…/16501803) (fetched 2026-09-07)
- SimpleConsign — https://www.simpleconsign.com/ ; https://www.simpleconsign.com/consignor-and-vendor-payouts ; https://www.simpleconsign.com/inventory-management (fetched 2026-09-07)
- ResaleWorld (Liberty) — https://www.resaleworld.com/ (fetched 2026-09-07; full content saved to tool output)
- Resell4.me / BCSS — https://www.bestconsignmentshopsoftware.com/ (fetched 2026-09-07)
- ConsignPro — https://www.consignpro.com/ (403 ×1, abandoned 2026-09-07)

## Product Observations

### ConsignCloud (evidence layer A unless noted)

- Positioning (Tier-2): "Consignment software that handles everything that makes consignment & resale unique — tracking who owns what, when it came in, and how much everyone gets paid."
- **Three inventory types documented (Tier-1, "Understanding Inventory Types"): Consignment, Buy Outright, Retail — "all three affect split and Account Balance differently."**
  - Consignment: item brought in by consignor is "shared with the store owner"; on sale, the consignor's share is "immediately put into the Account's Balance" (unless a discount or surcharge affects the split). Balance credited **at time of item sale**.
  - Split convention (Tier-1): a percentage or fraction split is the **consignor's** portion — "a 30/70 split or 30% split is 30% to the consignor and 70% to the store." (Product-documented convention; industry direction may vary.)
  - Buy Outright: store buys the item from the consignor; the **Cost Per** amount goes into the account balance **at time of item entry**; often realized as a 0% split.
  - Retail: owned entirely by the store; account field **optional**; 100% of revenue to the store.
- **Account balances (Tier-1, "Account Balances"):** "When items that belong to a consignor sell, a positive balance entry is made in their Account... That balance is paid out by the store owner periodically." Positive entries = item sales; negative entries = **fees or payouts**. Balance Entries report shows payout payment methods, item detail, adjustment reasons; CSV export.
- **Payouts (Tier-1, "Consignor Payouts"):** individual payout flow = Account Detail → "Pay out Account" → payout type (integrated **Cash, Check, ACH**; non-integrated **Venmo, PayPal**) → register assignment → Gross Amount → payout fees → **Cut-off Date** ("the start date for a payout is always the date of the last payout") → overview with fees → optional receipt → confirm. **Bulk payouts**: Accounts Table → "Outstanding Balances" → "Pay out Accounts" → select accounts → method + register → fees + cut-off → summary → receipts sorted by account number/name/last name.
- Accounts collection (Tier-1 article titles): Adding an Account; Deleting/Restoring; **Invite Vendors**; Vendor Profile; **Email Notifications** (automated emails); Editing Account Fields (customizable creation fields); **Consignor Portal** ("let your consignors log in to get account updates"); Account Filters; Account Balances; Consignor Payouts; **Adjusting Balance** (manual changes); **Partial Payouts**; **Recurring Fees and Payout Fees** ("how to set recurring fees like rent"); **Payouts as of a Specific Date** (cut-off dates); **Reversing and Editing a Balance Change**; **Integrated ACH Payouts**.
- Items collection (Tier-1 article titles): Adding an Item; **Batches**; Locked Fields; Editing Item Fields; **Understanding Inventory Types**; **Moving Consignment Items to Store Property** ("When and Why to Move Items from Consignor Ownership to Store-Owned Stock"); **Tiered Splits** ("for differently priced items"); cleaning duplicate Brands/Categories/Tags; Item Filters; **Bulk Edits**; Deleting/Restoring Items; Tags; Table Customization.
- Product page (Tier-2): Account overview; consignor communication (email updates, **pickup reminders**, self-service portal); payouts (check/cash/digital; **store credit incentives**); balance tracking (automatic updates + manual adjustments); notes & attachments ("consignor contracts"); intake (manual, batches, CSV); **label printing** (barcodes, branded labels, bulk); **Shopify/Square sync** (sold online auto-updates inventory and consignor accounts); multi-location (locations and shelves); pricing ("consignment, buy-outright, or retail pricing with flexible splits, surcharges, and tax rules"); POS (scan barcodes, add customers, **create items on the fly**; split payments, store credit, cards via Stripe/Gravity; discounts, taxes, surcharges; receipts, returns, voids, till reconciliation; gift cards; registers); reporting (Accounts Report "top consignors", Inventory Report, Sales Report, Accounting Report "consignor balances + item sales", export, **audit log**); **Vendor Login** ("allow vendors to log in to add and price their own inventory").
- Segments (Tier-2): Consignment Stores, **Vendor Malls**, High-End Resale, Online-Only, Mixed-Retail, **Buy-Outright Stores**, Furniture Stores, Gift Shops, **Antique Malls**, Art Galleries, Pop-ups.
- Plans (Tier-2): Basic / Pro / Enterprise; Pro adds vendor access (up to 1,000 vendors), **Consignor Portal, automated emails, advanced reporting**, unlimited users, API; ACH payouts carry a per-payout fee on Basic (product-specific).
- Maintains a public resale-industry glossary (resalepedia.com links throughout help docs) — vendor-specific but evidence of industry vocabulary (consignor, split, consignor portion, payout, buy-outright, retail).

### SimpleConsign (evidence layer A)

- Positioning (Tier-2): "Automate the four things that eat your week: POS, inventory, consignor payouts, and reporting." "Trusted by 3,100+ resale shops."
- **Payouts (Tier-2):** "What options are available to pay consignors and vendors from SimpleConsign? ... ACH and direct deposit, checks, and store credit. You can easily set payouts on an immediate or delayed basis."
- **SimpleACH** (Tier-2): consignors/vendors enter banking details themselves in **Consignor Access** (the consignor portal); store enables ACH; approval then batch payouts. KYC onboarding for the store. (Product-specific figures recorded in Vendor-specific section, NOT canonical.) Security posture: "SimpleConsign enhances permissions within our system to restrict payout completion to approved users only. Editing of consignor bank accounts is exclusively accessible from the customer's end."
- **Store-credit incentive (Tier-2):** "This is a common practice where stores add a small premium to consignors' payables if they choose to take their payables as store credit."
- **Payout liability framing (Tier-2):** instant transfers "don't float or remain a payout liability over time" — confirms the consignor balance is the store's payable.
- **Inventory bases (Tier-2):** "inventory management for **consigned, store-owned, donated, or wholesale purchased** inventory."
- **Splits & fees (Tier-2):** "Set the percentage split between consignor and shop, as well as additional vendor fees"; "setting up fees for services such as credit card, consignment, inventory, and more."
- **Pricing machinery (Tier-2):** Price Compare ("compare competitive pricing across multiple industry resale commerce sites"), Price Book ("accurate and consistent pricing from all employees across locations"), Customized tags and labels, AI Item Entry (photograph an item, AI fills inventory fields), bulk editing.
- **Markdown machinery (Tier-2):** "Discount rules and schedules — automatic markdowns by tag colour, category, price or time period."
- **Consignor portal (Tier-2):** "They log in to manage their own inventory and check balances"; cross-location consignor sharing; consignor scheduling (footer: drop-off scheduling surface).
- **Multi-store (Tier-2):** view/search inventory across locations, inventory transfers, unlimited consignors "shared across locations."
- **Accounting (Tier-2):** QuickBooks integration — "Consignor payouts tracked in QuickBooks automatically"; end-of-day reports; Store Insights mobile app.
- **Segments (Tier-2):** Consignment Stores, Vendor Malls (Vendor Mall Plus: rent collection, vendor payments, vendor-managed inventory, vendor portal, 3D floor map), Antique Malls, Buy Outright Stores, Estate Sale Operators, New Stores, thrift.
- **FAQ (Tier-2) — accounting posture:** "Within a consignment arrangement in which a store takes inventory on consignment, that inventory is **not considered an asset** since ownership is not transferred until the actual sale... When it sells, the consignor and consignee will split the sale." Also lists "consignment period, consignor splits, discounting, flexible payouts" as the consignment-specific tracking problems.
- **Paper-era baseline (Tier-2, customer quote):** "SimpleConsign helped me stop running my retail shop like a 'multi-family garage sale'. I no longer had to keep tags, tally consignor accounts, and manually calculate and write checks at the end of each month." — direct description of the pre-software process the category digitizes (useful for the historical check, layer A via quoted customer on vendor page).

### Liberty / ResaleWorld (evidence layer A, homepage text)

- "Trusted for Decades" — "more than 30 years of resale experience"; "Thousands of stores on Liberty"; "22 countries served worldwide"; Liberty REACT (legacy/desktop) and Liberty Cloud ("the same Liberty software... now hosted, updated, and backed up for you"; guided migration, automatic updates & backups).
- **Account model:** "Liberty account list of **consignors, sellers, and buyers** in one searchable account list" — sellers = buy-outright counterparties; buyers = retail customers.
- **Modules:** Inventory & payouts; Client accounts; Web listings; Point of sale; Account transactions.
- **Payouts:** "Prepare and pay consignors by check or with ResaleWallet" (ACH digital payouts; "payment details update in Liberty instantly").
- **Consignor Center:** "secure online portal to check balances, track inventory, and view sales anytime, straight from your Liberty data" — positioned against "What's my balance?" calls.
- **Kiosk:** "Shoppers search inventory and check prices while consignors review **contracts and balances**" — evidence that consignment contracts are first-class records.
- **Web listings:** eBay Integration + Shopify Integration; "Turn your Liberty inventory into a branded online store... titles, prices, photos, and quantities sync automatically"; channel sync framed around "the risk of double-selling."
- **Accounting:** "Send sales, consignor payouts, and cost of goods to QuickBooks with no manual bookkeeping" — evidence the consignor payable is an accounting-grade flow.
- **Pricing support:** AI Pricing Assistant; thermal tag printers and tag plans as first-party hardware.
- Other: Resale Rewards (loyalty), Liberty Mobile Apps, ResalePay (payments).

### Resell4.me (BCSS heritage) (evidence layer A, homepage + FAQ)

- Since 2001 ("Serving consignment shops since 2001"); BCSS desktop predecessor; free migration of "consignors, inventory, balances, and sales history — ... balances to the penny, barcodes intact" (BCSS-style 11-digit barcodes still scan).
- **Founder-articulated minimum definition (Tier-2):** "At minimum, consignment software should keep **each item tied to its owner and commission terms**, track the **complete inventory lifecycle**, process **sales and returns**, calculate **consignor balances accurately**, and produce **records a shop can verify and export**."
- Feature minimum list: consignor accounts, splits, balances, settlement history; inventory intake, status, pricing, discounts, item history; POS, tax, returns, **layaway**, payment records; barcode labels, tag printing, scanning, product lookup; sales/inventory/tax/accounting reports or exports; migration path.
- Positioning: "Not a generic retail system with consignment bolted on. Every feature was built for the way consignment shops actually operate."
- **Consignor management:** "Full split tracking per consignor, running account balances, settlement statements, **carryover balances**, and broadcast email to all consignors at once"; **per-consignor split % AND per-item split %**.
- **Consignor portal (Pro):** shows Active Items / On Floor / Items Sold / History / Total Sales / **Your Share (60% example)** / Already Paid Out / **Balance Due to You** — "Consignors log in anytime from any device — no phone call needed."
- **POS:** type-to-find ("No barcode? Start typing the description, SKU or price"), scan any barcode format, tax, returns, layaway, loyalty (Pro).
- **Settlements:** ACH direct-to-bank; "daily settlement, sales by payment method, tax collected by rate, **consignor performance, accounts payable** — all built in."
- **Sold alerts:** "Send an 'item sold' email alert to select consignors automatically."
- **Offline:** core offline work (non-card sales, item entry, settlements, printing, exports) with sync on reconnect.
- **Mall space rental** (Pro) — vendor-mall/booth-rent variant; online selling (Pro); QuickBooks Online sync (Pro).
- Pricing: $49–$89/month or one-time; competitor comparison $75–$199/month (layer A for this vendor's page; prices not canonical).

## Cross-product Comparison

| Structure / capability | ConsignCloud | SimpleConsign | Liberty | Resell4.me | Evidence |
|---|---|---|---|---|---|
| Consignor account with running balance owed to owner | ✔ (Balance table, entries) | ✔ (Consignor Access, payouts) | ✔ ("account transactions", payouts) | ✔ (running balances, carryover) | A×4 → B |
| Item-level record binding item → owner + commission/split terms | ✔ (inventory type + split + tiered splits) | ✔ (splits per consignor/shop, per-item vendor fees) | ✔ (consignor accounts + items; contracts) | ✔ (owner + commission terms per item; per-consignor AND per-item split %) | A×4 → B |
| Attributed sale crediting the owner's balance | ✔ (balance entry at item sale) | ✔ (splits at checkout) | ✔ (account transactions) | ✔ (settlement from sales) | A×4 → B |
| Settlement/payout of balances (cash/check/ACH/store credit; batch) | ✔ (cash/check/ACH/Venmo/PayPal; bulk payouts; cut-off dates; partial) | ✔ (ACH/check/store credit; immediate/delayed; batches) | ✔ (check or ResaleWallet ACH) | ✔ (ACH; daily settlement) | A×4 → B |
| Mixed inventory bases (consigned + store-owned retail + buy-outright) | ✔ (3 types documented) | ✔ (consigned/store-owned/donated/wholesale) | ✔ (consignors, sellers, buyers in one list) | ✔ (implied: purchases + consignment; layaway) | A×4 → B (exact type counts vary) |
| POS checkout as the sale surface | ✔ | ✔ | ✔ | ✔ | A×4 → B |
| Tags/labels/barcode scanning | ✔ | ✔ | ✔ (thermal tags/plans, first-party hardware) | ✔ (any barcode format; no-retag migration) | A×4 → B |
| Consignor self-service portal | ✔ (Pro-gated) | ✔ (Consignor Access) | ✔ (Consignor Center) | ✔ (Pro-gated, plan-dependent) | A×4 → B, plan tiering is variant |
| Automated emails / notifications to consignors | ✔ | ✔ | ✔ (portal positioning vs phone calls) | ✔ (sold alerts, broadcast email) | A×4 → B |
| Buy-outright mode | ✔ (documented type) | ✔ (segment + basis) | ✔ (sellers) | ✔ (purchases) | A×4 → B |
| Vendor/booth mode (vendor accounts, rent/fees, vendor portals) | ✔ (vendors, recurring fees "like rent", vendor login) | ✔ (Vendor Mall Plus, rent collection, vendor payments) | ◐ (not directly evidenced on homepage) | ✔ (mall space rental) | A×3; vendor-mall variant |
| Discount/markdown machinery | ✔ (discounts/surcharges affect split) | ✔ (auto markdown schedules by tag color/category/price/time) | ◐ | ✔ (discounts) | A×3 → B |
| Donated inventory / thrift mix | ◐ (not evidenced) | ✔ (donated basis; thrift) | ◐ | ◐ | A×1 — common-in-thrift, not universal |
| Online channel sync (Shopify/eBay/Square) | ✔ (Shopify, Square) | ✔ (Shopify) | ✔ (eBay, Shopify, double-selling guard) | ✔ (online selling, Pro) | A×4 → B, modern-era |
| AI item entry / AI pricing | ✘ | ✔ (AI Item Entry) | ✔ (AI Pricing Assistant) | ✘ | A×2 → optional, modern-era |
| Accounting handoff (QuickBooks-class) | ✔ (accounting report/export) | ✔ (QuickBooks, payouts tracked) | ✔ (sales, consignor payouts, COGS) | ✔ (QBO sync) | A×4 → B |
| Multi-store / multi-register | ✔ (locations, shelves) | ✔ (transfers, shared consignors) | ✔ (multi-store heritage) | ✔ (multi-register; large-store plan gate) | A×4 → B |
| Permissions / audit | ✔ (audit log; payout permission restriction — SC) | ✔ (payout completion restricted to approved users) | ◐ | ◐ (account-based access) | A×2 → B, moderate |
| Layaway / loyalty / gift cards | ✔ (gift cards) | ◐ | ✔ (Resale Rewards) | ✔ (layaway, loyalty) | A×3 → common-optional |
| Contracts/agreements as records | ✔ (notes & attachments: contracts) | ◐ | ✔ (kiosk: consignors review contracts) | ✔ (custom agreements) | A×3 → B |

## Abstraction

### L0 — Defining Invariant (deliberately minimal)

A Consignment Management Platform is recognizable as this Type iff all four hold:

1. **Consignor account with a running balance** — a managed party record for the owner of the goods, carrying the amount the store owes them. *(Remove → plain retail POS/inventory with no payables.)*
2. **Item-level consigned inventory bound to owner + recorded commission/split terms** — each item enters the store's custody as an individually tracked record (description, price, owner, terms). *(Remove → generic retail stock; remove custody → marketplace listing.)*
3. **Attributed sale event** — a recorded sale of a specific item at a specific price that closes the item and credits the owner's share to their account. *(Remove → static consignment bookkeeping, not managed selling.)*
4. **Settlement of balances** — the store discharges the running payable through recorded payouts (any method), with retained history. *(Remove → unpaid ledger; not management.)*

**Historical check (§24):** a paper-era consignment shop — consignment book/agreement cards (owner + terms), hand-written tags, a cash register or sales log (attributed sales), and a payout ledger with check stubs — satisfies all four without any modern machinery. The SimpleConsign customer quote ("keep tags, tally consignor accounts, manually calculate and write checks") and Resell4.me's BCSS migration evidence confirm the digital category digitizes exactly this spine. ✔ passes.

### L1 — Common Mature Structure (not definitional)

- Intake workflows: batch/manual/CSV entry, descriptions, photos, categories, brands, locked/required fields, bulk edits
- Tag/label printing (price + item identity + barcode) and barcode scanning; tag/label supplies as first-party hardware (Liberty)
- Pricing machinery: price book, price-comparison references, per-consignor/per-item/tiered splits, fees
- Markdown/discount schedules that step prices down over time (time/tag-color/category/price triggers vary); discounts/surcharges changing the split outcome
- Item lifecycle states: received → priced/tagged → on floor → discounted → sold | returned to owner | expired (consignment period end); pickup reminders
- Settlement machinery: statements, cut-off dates, partial payouts, delayed/immediate payout scheduling, payout fees, balance adjustments and reversals, store-credit premium incentives
- Consignor portal (balances, items, sales, payout status); automated emails/sold alerts/broadcast email
- Mixed bases: buy-outright (payable at intake, not at sale) and store-owned retail alongside consigned stock
- Reporting: sales, inventory aging, consignor performance, accounts payable/balances, tax
- Accounting handoff (QuickBooks-class export/sync of sales, payouts, COGS)
- Multi-store/multi-register; employee roles/permissions (esp. payout approval); audit trail
- Customer (buyer) records, loyalty, gift cards, returns/refunds/voids, layaway
- Consignment contracts/agreements as attached records
- Online channel sync (Shopify/eBay/Square-class) with inventory/account sync

### L2 — Variant / Optional Structure

- **Vendor-mall / antique-mall mode** — vendor (booth) accounts, booth/space rent collection, vendor-managed inventory, vendor self-listing portals, centralized checkout with commission and/or rent; 3D floor maps (SimpleConsign Vendor Mall Plus)
- **Vertical tuning** — furniture/estate shops, high-end luxury resale, children's resale, thrift/donation mix (donation basis), gift shops, art galleries, pop-ups, board sports (ConsignCloud segment list)
- **Online-only consignment** — no storefront, sell through Shopify/Square
- **Estate-sale operators** (SimpleConsign segment)
- AI item entry / AI pricing (2/4 sampled; modern-era)
- Kiosks (Liberty), mobile store-insights apps (SimpleConsign), offline-first postures (Resell4.me)
- Plan-tier packaging (portal/reporting/ACH gated by plan; per-location vs per-store pricing; one-time license vs subscription)
- Regional payment rails (ACH = US; payout rails are regional realizations)

### L3 — Vendor-specific Detail (kept out of the final document)

- ConsignCloud: split-convention documentation ("30/70 = 30% consignor"); resalepedia.com glossary; Pro tier gates (vendor access up to 1,000 vendors); Basic ACH per-payout fee; "Classic Articles" help-center split
- SimpleConsign: SimpleACH specifics (consignor-entered banking, KYC for store, payout minimums/maximums and time-of-day submission cutoffs, 2–5 business-day settlement), "Consignor Access" portal name, tag-color markdown triggers, Store Insights app, Vendor Mall Plus 3D floor map
- Liberty/ResaleWorld: Liberty REACT vs Liberty Cloud packaging, ResaleWallet, Consignor Center, Resale Rewards, kiosk, AI Pricing Assistant, 22 countries/30+ years claims, first-party tag printers/plans
- Resell4.me/BCSS: 11-digit BCSS barcodes, tag-bonus self-funding pricing model, per-tag surcharge, offline-first sync matrix, founder-authored comparison pages

## Canonical Model (synthesis)

```text
Consignor Account (owner of goods; running balance = store's payable)
└── Consigned Item (individually tracked; custody at intake; description/price/status)
    └── Terms (owner share vs store share — per account, per item, or tiered; fees)
        └── Sale (attributed at POS; closes item; credits owner's balance)
            └── Balance Entries (+ sales / − fees & payouts)
                └── Settlement (payout by cash/check/ACH/store credit; statements; history)

Parallel bases on the same floor: Buy-Outright (payable at intake) · Store-owned Retail (no account) · Donated (thrift)
```

**Removal tests:**
- Remove consignor account/balance → generic retail POS + inventory (Retail POS / Inventory Management territory)
- Remove custody & operator pricing (seller keeps possession, self-lists) → Resale Marketplace
- Remove the store-operator identity; supply = brand's own trade-in/grading/channel machinery → Recommerce Platform
- Remove item-level owner binding (mass stock, quantity-ledger) → Inventory Management System
- Remove fixed-price counter sales; lots + competitive bidding events → Auction Management System
- Object world becomes unique artworks (attribution/provenance/condition custody) → Artwork Consignment Management (which ships as modules)

## Vendor-specific Findings

(See L3 above. Notable methodological caution: split direction conventions differ across vendors/regions — ConsignCloud documents consignor-first "30/70"; do NOT treat any one convention as the industry standard in the final document.)

## Boundary Findings

1. **vs Resale Marketplace (§05.19, processed)** — CONFIRMED from this side. The marketplace seller retains possession and self-lists; the consignment operator takes physical custody at intake, prices the item, sells at the counter, and settles the owner's share. The resale-marketplace pass recorded the custody seam; this pass confirms it from the consignment side. Both leaves stand.
2. **vs Recommerce Platform (§05.19, processed) — FLAGGED JOINT REVIEW DISCHARGED.** The recommerce pass asked: two Types (store-operator vs brand-program) or a consolidation view? Verdict from this side: **two Types stand.** Evidence: (a) users differ — consignment platforms are bought by independent store owners/operators (multi-store owners at most); recommerce platforms are bought by brands running resale programs; (b) core objects differ — consignment: consignor account, item custody at intake, split terms, payable settlement; recommerce: trade-in programs, condition grading/refurbishment, brand-scoped P2P modules, branded resale channels, credit/gift-card payout; (c) surfaces differ — counter POS + local store (+ optional Shopify) vs national branded e-commerce + reverse logistics; (d) the shared consign-in→sell→settle loop is a generic resale pattern that also appears (partially) in auction management — it cannot define either leaf. No consolidation; the leaves are adjacent siblings sharing a pattern, not one Type.
3. **vs Retail POS (§05.10)** — consignment platforms embed a POS (checkout is the sale surface in all four samples), but the defining structure is the consignor payable machinery; a retail POS lacks consignor accounts, splits, and settlement. Consignment software explicitly positions against generic retail ("not a generic retail system with consignment bolted on" — Resell4.me). The accounting posture is the crisp discriminator: consigned inventory is not the store's asset until sold (documented).
4. **vs Retail Inventory Management (§05.12) / Inventory Management System** — generic inventory tracks quantities by item/location; consignment platforms track **ownership basis per individual item** (whose it is, what's owed on it) plus the payable ledger. Quantity-ledger semantics are absent from the sampled consignment products' centers.
5. **vs Online Marketplace / Multi-vendor Marketplace (§05.02)** — the vendor-mall/antique-mall mode inside consignment software is the closest variant (vendors supply inventory, store centralizes checkout, settles accounts, collects rent/commission). It remains a **variant** of this Type rather than a marketplace because the operator still holds custody and is the single system of record for settlement; no open buyer-seller venue is exposed.
6. **vs Auction Management System (§05.18, processed)** — auction houses also take consignments, but their center is lots + sale events + competitive price discovery; consignment shops sell at fixed prices at a counter with no bidding machinery. Distinct Types.
7. **vs Artwork Consignment Management (§27, processed)** — same legal arrangement (consignor → consignee custody + terms + settlement) but a different object world (unique artworks with attribution/provenance/condition) and different market packaging (that leaf ships as a module inside gallery/artist suites; this leaf is standalone store-operating software for general-merchandise resale with an embedded POS). Both stand as distinct realizations of the consignment relationship.
8. **Taxonomy note** — the directory name "Consignment Management Platform" sits under Resale (05.19). The market's own name for this category is "consignment software / consignment shop software"; every sampled vendor sells it to store operators as the store's system of record (POS + inventory + consignor money). The leaf is valid as the store-operator consignment Type; "platform" should be read as "product category," not "network platform."

## Uncertainties

1. **ConsignPro unreachable** (403). The desktop-veteran pole is covered indirectly (Resell4.me/BCSS since 2001 with desktop-predecessor migration evidence; Liberty REACT desktop heritage). Low residual risk: the four sampled products are independent and convergent.
2. **Split-direction conventions vary by vendor/region**; only ConsignCloud's convention was directly documented. Final doc avoids stating a universal convention.
3. **Consignment period/expiry mechanics** (exact expiry behaviors, auto-return rules, donation-after-expiry policies) are referenced (consignment period as a tracked concept; pickup reminders) but not deeply researched; final doc stays generic ("items unsold after an agreed period are returned, donated, or discounted per store policy — product-configurable").
4. **Donation basis** directly evidenced in one product (SimpleConsign) plus thrift positioning; treated as common-in-thrift, not universal.
5. **Liberty evidence** comes from the homepage only (image-heavy site; deeper docs not fetched); Liberty-specific claims kept at homepage-strength.
6. **Vendor-mall mode** evidenced in 3/4 products; Liberty's vendor-mall support not directly evidenced — vendor-mall machinery recorded as a variant, not universal.

## Final Synthesis

The Consignment Management Platform is the **store-operator's system of record for selling other people's goods**: consignor accounts with running payable balances, item-level consigned inventory bound to owners and commission terms under the store's custody, POS-attributed sales that credit owner shares, and recorded settlement of those balances. Around this spine, mature products add intake/tagging/pricing/markdown machinery, consignor portals and notifications, mixed inventory bases (buy-outright, retail, donated), reporting, accounting handoff, multi-store operations, and online-channel sync; vendor-mall/booth mode is the principal workflow variant, and vertical tuning (luxury, furniture, thrift, estate) the principal market variant. Boundaries hold on all sides: custody separates it from resale marketplaces, operator identity separates it from recommerce programs, the consignor payable separates it from retail POS/inventory, fixed-price counter sales separate it from auctions, and the general-merchandise object world separates it from artwork consignment. Historical check passes: the four-structure spine describes the paper-era consignment shop unchanged.
