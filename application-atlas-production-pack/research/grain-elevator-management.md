# Research Notes — Grain Elevator Management

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand what grain elevator management software actually is as an Application Type: the objects it keeps records of, the workflows it runs, the money loop it closes, the interfaces it exposes, and where its boundary lies against neighboring agriculture/commodity Types (Grain Management, Grain Origination Platform, Agribusiness ERP, Farm Management, commodity trading/risk).

## Initial Boundary (Step 1 hypothesis)

- Working hypothesis: software for the grain side of a grain-handling business (country elevators, cooperatives, merchandisers, processor receiving points): receiving grain from growers (weighing + grading), contracts, storage inventory, settlements/payments to growers, outbound sales/loadout.
- Likely confusions: grain bin/storage monitoring (physical condition of grain vs bushels as commercial inventory); origination platforms (front-end contracting vs full operation); ag-retail ERP (grain as one module); CTRM (paper positions without physical custody); generic WMS.

## Research Questions

1. What are the core record types? (tickets, contracts, settlements, bins, positions)
2. How does one delivery flow from truck arrival to money paid?
3. How are contracts modeled and how do deliveries apply to them?
4. How is grain inventory tracked (bins, commodities, locations, custody)?
5. What outbound flows exist (sales, loadout, dispatch, proof of delivery)?
6. What interfaces exist (office back office, scale house, grower portal, buyer portal, accounting)?
7. What rules matter (quality factors, discount schedules, quantities vs commitments, multi-location)?
8. Where is the system-of-record line drawn (own accounting vs ERP integration)?

## Representative Products (sample + rationale)

| Product | Pole | Why sampled |
|---|---|---|
| Agvance Grain (SSI) | Co-op ag-retail ERP with a dedicated Grain module | The traditional co-op/country-elevator back office pole; Tier-2 product page reachable |
| Ever.Ag CMS (Commodity Management System) | Integrated grain accounting / merchandising ERP | Merchandiser/processor pole ("elevators, feed mills, ethanol plants"); Tier-2 page + FAQ reachable |
| Bushel | Digital origination/payments layer on top of grain-buyers' ERPs | Modern SaaS pole; release notes give near-Tier-1 operational object vocabulary |
| GrainChain | Blockchain-enabled transaction/inventory platform | Different technology philosophy + geography (TX/MX/Honduras/BR); homepage reachable only |

Rejected during sampling:

- AgWorks (agworks.com) — Product Mismatch: AgOS is "The Unified Agronomy Solution" (ag-retail/agronomy), not a grain elevator system. Rejected.
- Traction Ag — 403 bot wall ×2. Abandoned.
- AgriDigital (AU) — empty responses ×2. Abandoned (would have added an Australia pole).
- AGRIS — transport error; reached only secondhand via Bushel release notes naming it as an integrated grain accounting ERP. No direct product claims made.
- Bushel support Knowledge Base (Zendesk) — timeout ×2. Abandoned; Bushel evidence downgraded to release-notes level.

## Sources

Tier 1 (operational-ish, directly fetched):

- Bushel Release Notes index — https://www.bushelpowered.com/release-notes (fetched 2026-09-08; monthly/quarterly feature notes naming scale tickets, contracts, settlements, discount schedules, bin-level tracking, ERP contract creation, deferred settlement)

Tier 2 (official product pages, directly fetched):

- Bushel — https://www.bushelpowered.com/ , https://www.bushelpowered.com/agribusiness/grain
- Agvance — https://agvance.net/ , https://agvance.net/products/grain
- Ever.Ag — https://ever.ag/agribusiness/cms/ , https://ever.ag/agribusiness/risk-management-for-grains
- GrainChain — https://grainchain.com/ (homepage only; subpages 530-blocked)

Unreachable / degraded:

- https://support.bushelpowered.com/hc/en-us (timeout ×2)
- https://tractionag.com/ (403 ×2)
- https://www.agridigital.com/ (empty ×2)
- https://www.agris.com/ (transport error ×1)
- https://grainchain.com/components/pages/trumodity.html , storage_operators.html (530 ×2)
- https://en.wikipedia.org/wiki/Grain_elevator (timeout ×2 — industry-context check downgraded to conceptual reasoning)

Consequence: no precise numeric facts (bushel capacities, fee schedules, contract-type lists, moisture table values) are asserted anywhere in the final document. All workflow claims are at capability level.

## Product Observations (evidence layer A = directly observed on that product's official page)

### Product 1 — Agvance Grain (SSI) — https://agvance.net/products/grain

- A: Positioned "The Complete Grain Management System" for the "grain elevation workload"; part of an integrated ag-retail ERP suite (Accounting, Agronomy, Energy, Grain, Grower360).
- A: Scale automation: RFID identifies arriving trucks; the software "automatically identifies and tracks arrivals to capture weights, moisture and grade factors. The software generates scale tickets without the driver needing to say a word."
- A: "Contract Management — Simplify contract management. Categorize and monitor contractual obligations, plus easily capture e-signatures."
- A: "Synchronized Dashboards — an interactive view of your grain positions and market activities… isolate specific commodities company-wide or by individual location."
- A: "Market Reporting — Review real-time assessments of the market value of contracts."
- A: Grower portal (Grower360): growers "monitor contracts, balances, payments and more from home or on-site." Controller testimonial: "As they drop off a load of grain, they can see that scale ticket instantaneously."
- A: Offers platform (Barchart integration): growers create offers; "grain merchandisers can easily review, accept and reject them"; status updates flow back to growers.
- A: Hero image shows a settlement screen ("commodities, pricing status, and settlement details") — settlement is a first-class screen; evidence is visual, so kept at module-existence strength.

### Product 2 — Ever.Ag CMS — https://ever.ag/agribusiness/cms/

- A: "specializes in managing the complexities of inventory management and grain accounting for commodity traders and feed manufacturers." FAQ: "used by grain merchandisers, elevators, feed mills, ethanol plants."
- A: Modules: Dispatch ("loads scheduled, loads yet to be scheduled, and completed loads"); CRM ("sale and purchase opportunities"); Accounting ("every tool necessary… accounts receivable to the general ledger… financial reports explicitly customized for a grain business"); Logistics ("inbound or outbound multimodal movement of products or bulk commodities"); Inventory Management ("costing methods and selling prices on a product and location level… nested formula capabilities and bin tracking features").
- A (FAQ): "contract creation, tracking, and settlement"; "contract management, position tracking, inventory management, settlement processing, and accounting integration"; "automates settlement calculations based on contract terms, deliveries, and pricing… timely payments to producers"; "visibility into commodity positions and financial exposure"; multi-location support.
- A (companion product, boundary evidence): Ever.Ag "Vault" (under Grain Risk Management, a separate suite) — "Track profitability with real-time visibility on grain prices, forward positions and physical sales." Risk/brokerage/advisory is packaged as a distinct offering alongside the operations ERP.

### Product 3 — Bushel — https://www.bushelpowered.com/ + /release-notes

- A: Serves "Grain Buyers… Manage contracts, track inventory, and access financing with a single connected system"; "Trusted by 3,500+ grain and ag retail facilities across the United States and Canada."
- A: Solutions: Trade ("Manage cash bids, offers, and hedges in one connected system"; farmer "Make Offer" flow), Bushel Pay (digital payments replacing checks; direct deposit), Customer Portal (white-labeled grower portal), Commercial Portal ("Streamline proof-of-delivery for commercial grain sales"), CRM with "real-time ERP sync" and eSign.
- A (release notes, near-Tier-1 object vocabulary):
  - "search scale tickets, contracts, and settlements by ID number" (Oct 2024)
  - "custom field-name tagging on scale tickets" (Sep 2024)
  - "CRM bin-level tracking" (Q3 2025)
  - "PDF Discount Schedule uploads" (Q2 2025); "manage and share discount schedules" in the customer portal (Q1 2025)
  - "ERP contract creation upon filled offers" (Jul 2024); "automated contract creation" (Q4 2025)
  - "deferred settlement options" (Sep 2024, Q1 2024)
  - "automated Agris statement payments" (Jul 2024); "upgraded Agris contract features" (Q3 2025) — Agris = a third-party grain accounting ERP Bushel integrates with
  - "export transaction histories for easier financial reconciliation" (Oct 2024)
  - "an upcoming storage and load tracking feature" (Q3 2025); "improved grain load tracking in Bushel Farm" (Q4 2025)
  - "cash bids and futures widget" (Summer 2024); "minimum trade offer sizes" (Q3 2025)
- Interpretation: Bushel sits as the digital front office (offers, contracts, grower visibility, payments) layered over the elevator's ERP, which remains the accounting system of record. This is market-structure evidence, not a feature claim.

### Product 4 — GrainChain — https://grainchain.com/

- A: Suite: Trumodity ("Comprehensive Transaction Platform"), Silosys ("Smart Inventory Management Solutions" / "Inventory management and raw material transformation"), Silosys Mobile ("Blockchain-enabled inventory management app"), HarvX ("Easy Logistics Management"), Seed Audit (preharvest).
- A: "Site Operators — Helping growers, elevators and drivers work together" — elevators are a named participant class.
- A: Problems targeted include "Delayed Payments" and "Inefficient Inventory Management Systems"; "cloud-based, blockchain and IoT enabled platform"; multi-country (US/Mexico/Honduras/Brazil offices; "24+ different commodities processed").
- A (privacy policy, fetched with homepage): precise geolocation used for "on-site commodity-drop verification" — delivery-verification at the site is a product behavior.
- Limited depth (subpages blocked); used only to confirm the same object set (transactions, silo inventory, delivery verification, payments) from a different technology philosophy and geography.

## Cross-product Comparison (Layer B — cross-product commonality)

| Finding | Agvance | Ever.Ag CMS | Bushel | GrainChain | Strength |
|---|---|---|---|---|---|
| Delivery ticket as atomic record (weighed, attributed) | A (RFID → scale tickets w/ weight, moisture, grade) | A ("deliveries" feed settlement; dispatch loads) | A (scale tickets searchable; field tagging) | A (commodity-drop verification; Silosys) | B — universal in sample |
| Contracts as standing instruments, tracked to completion | A (obligations, e-sign) | A (creation→tracking→settlement; "contract performance") | A (offers→contract creation; e-sign) | implied (transaction platform) | B |
| Settlement loop: deliveries priced per terms → grower payable → payment | A (settlements screen; growers see payments) | A ("automates settlement calculations… timely payments to producers") | A (settlements; deferred settlement; ACH/direct deposit) | A (delayed-payments problem; Dwolla rails in ToS) | B — universal |
| Quality factors with commercial consequence | A (moisture, grade factors captured) | A- (pricing per "contract terms" — quality adjustment not explicit) | A (discount schedules as managed/shared objects) | not observed | B- common; exact factor sets vary by commodity/market — NOT universalized |
| Bin/storage-located inventory | A ("Measure and track grain"; locations) | A ("bin tracking features") | A ("CRM bin-level tracking"; storage/load tracking) | A (Silosys) | B — universal |
| Commodity position / market-value view | A (positions dashboard; market value of contracts) | A ("positions and financial exposure") | A- (cash bids, offers, hedges in Trade) | not observed | B common; depth varies |
| Outbound/sale side (loads, proof of delivery) | A- (grain tracking; not explicit) | A (inbound/outbound multimodal logistics; dispatch) | A (Commercial Portal proof-of-delivery for commercial grain sales) | A (HarvX) | B common |
| Grower-facing portal/app (tickets, contracts, payments, offers) | A (Grower360) | n/a (no portal evidence) | A (Customer Portal; farmer app) | A (farmers as participants) | B common in current market |
| Offer → contract digital flow | A (Barchart offers; merchandiser accept/reject) | — | A ("ERP contract creation upon filled offers") | — | B- common; 2/4 sample + both poles |
| Multi-location operation | A (company-wide or by location) | A (multi-location FAQ) | A- (locations/hours features) | A- (multi-country) | B common |
| Accounting integration | A (grain is a module of the ERP suite) | A (GL/AP/AR built in) | A (integrates with ERPs, e.g. Agris) | not observed | B universal — but WHERE the ledger lives varies (module vs integration) |
| Payment modernization (digital grower payment) | A- (growers see payments) | — | A (Bushel Pay, direct deposit, ACH) | A (Dwolla rails; instant-payment positioning) | B common, not definitional |

Layer C (canonical inference) is in the Final Synthesis below.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

The Type is the grain-handling business's system of record for its grain commerce. Three jointly-held structures; remove any one and the product stops being recognizable as this Type:

1. **Ticketed grain movements of record** — every physical grain movement crossing the facility boundary (inbound grower deliveries; outbound shipments) is recorded as an identified, measured transaction attributed to counterparty and commodity. (Remove → weighbridge/scale software or a contract book with no physical flow.)
2. **The settlement money loop with growers** — deliveries are priced against the governing terms (contract or posted price) with quality-based adjustments, and resolved into recorded payables and payments to the grower on the same system of record. (Remove → ticket log with no commercial settlement, or a trading book with no custody.)
3. **Storage-located grain inventory** — grain held in custody is tracked as bushels by commodity in identified storage locations (bins), accumulating the movements into a standing inventory/position picture. (Remove → settlement calculator; bin-monitoring tools; spreadsheets.)

Jointly-held is load-bearing: 1+2 without 3 = settlement tooling with no custody; 1+3 without 2 = scale house plus pile with no money loop; 2+3 without 1 = trading/origination book with no physical ticket; each single leg alone = scale software / contract ledger / inventory sheet.

Deliberately NOT in L0 (checked against historical/analog practice): RFID or any specific capture technology; grower portals/apps; digital payments; futures integration; multi-location; discount-schedule UIs; cloud deployment; blockchain. A paper-era country elevator office (carbon-copy scale tickets with weights and moisture noted, contract book, grower ledger cards, bin tags, settlement checks, position sheets) satisfies all three legs — historical check PASSED at analog level. Definition names no era machinery.

### L1 — Common Mature Structure

- Purchase contracts with growers as standing instruments, tracked against delivered quantities; sale contracts with buyers on the outbound side. Contract-type vocabularies (fixed-price vs later-priced vs futures-linked) vary; the sample evidences "contracts carry pricing terms whose market value is tracked" (Agvance market-value reporting, Bushel offers/hedges/cash-bids machinery, Ever.Ag "pricing terms"), not a canonical contract-type list — exact type names NOT asserted.
- Quality factors captured at receiving with commercial consequence; discount schedules as configurable/shared objects (Agvance moisture/grade capture; Bushel discount-schedule upload/share).
- Position/exposure view: physical inventory vs commitments vs sales; unpriced contract value monitoring.
- Grower-facing portal/app: tickets, contracts, balances, payments, offers, cash bids.
- Digital offer→accept→contract flows with e-signature.
- Multi-location segregation (company-wide vs by location).
- Load logistics/dispatch on the outbound side; proof-of-delivery to commercial buyers.
- Accounting handoff: either built-in grain-industry GL/AP/AR or integration to a corporate ERP.

### L2 — Variant / Optional

- Packaging posture: grain module inside an ag-retail/co-op ERP (Agvance pole) vs integrated grain accounting/merchandising ERP (Ever.Ag CMS pole) vs digital origination/payments layer on top of an ERP (Bushel pole) vs blockchain transaction platform (GrainChain pole).
- Risk/hedging depth: embedded position dashboards vs companion risk suite/brokerage (Ever.Ag Vault positioned separately).
- Payment rails: paper check → ACH/direct deposit → platform wallets; deferred vs immediate settlement.
- Commodity breadth (corn/soy/wheat-dominant sample; GrainChain "24+ commodities" across countries).
- Business context: country elevator/origination point vs processor receiving (feed mill, ethanol plant) vs merchandiser.
- Regional practices (storage arrangements, drying charges, warehouse-receipt instruments): standard in the industry per general knowledge, but NOT evidenced in the reachable sample → held as uncertainties, not asserted.
- Geography: reachable sample is US/Canada-dominant with GrainChain's Latin-America presence; Australian vendor unreachable.

### L3 — Vendor-specific (Research Notes only)

- Bushel: Bushel Wallet/Business Account (fintech accounts via The Bancorp), BushelOne analytics, Buddy AI assistant, Buddy Seat content hub, white-label "Find My App" model, "42 seconds / $18 per check / 13 days / 402% growth" marketing figures, named ERP integrations (Agris, Compeer Financial, GROWERS).
- Agvance: Grower360 product name, Barchart offer integration, SKY Grain, Assembly Sheet Management → "Scale Ticket Level Management" conversion program, Agvance Analytics.
- Ever.Ag: CMS module names (Dispatch/Logistics/CRM/Accounting/Inventory Management), Vault, Merchant Ag (ag-retail ERP sibling), Roger (bulk hauling), Dairy.com lineage.
- GrainChain: Trumodity/Silosys/Silosys Mobile/HarvX/Seed Audit product names, blockchain/IoT claims, "225 Billion pounds / 18,000 participants" marketing figures, Dwolla payment processor.

## Vendor-specific / Rejected Findings

- AgWorks is agronomy retail, not grain elevator software (rejected sample; do not confuse with the ag-retail ERP boundary — it simply isn't in this Type).
- The "grain buyers… access financing" line (Bushel) suggests lending-adjacent services — vendor posture, not a Type property.
- Instant-payment positioning (GrainChain) is a philosophy/era marker, not a structural requirement.
- Blockchain/IoT enablement claims (GrainChain) are L3 technology marketing.

## Boundary Findings

- **vs Grain Origination Platform (sibling leaf, unprocessed):** origination names the front-end activity of contracting growers (Bushel literally brands a "Drive Origination" challenge). The elevator-management Type contains origination surfaces (offers, contract creation) but is centered on the full custody + settlement system of record. Probable keep-both (front end vs system of record), but the origination pass should treat this file's Boundary Findings as its counterparty; flagged for joint review.
- **vs Grain Management (sibling leaf, unprocessed):** working seam — bin/storage monitoring manages the physical condition of grain (temperature, moisture, aeration); elevator management manages bushels as commercial inventory and money. GrainChain's Silosys shows the naming overlap ("silo inventory"). The Grain Management pass should confirm this seam.
- **vs Agribusiness ERP (§20):** co-op ERPs carry grain as one module among agronomy/energy/fuel/accounting. The grain module still realizes this Type's core; the difference is suite scope. Keep-both (module-of-suite vs standalone vs layer are packaging poles of one Type).
- **vs Farm Management Platform (§20):** grower-side production/finance record. Bushel ships both (Bushel Farm vs buyer platform) — the actor and record center differ (farm's fields vs elevator's grain).
- **vs Commodity Trading & Risk Management:** paper positions/hedging without physical ticket/settlement custody; Ever.Ag's Vault is positioned as a companion to the ops system, which supports the seam.
- **vs Scale/Weighbridge software:** ticket capture only, no settlement loop, no inventory position.
- **vs generic Warehouse Management System (§10):** no grain grading, contract, or grower-settlement semantics; not evidenced as a competitor in this space.
- Remove-ticket leg → weighbridge tool; remove-settlement leg → bin monitor + ticket log; remove-inventory leg → settlement/contract calculator. Boundary test holds in all directions.

## Uncertainties

- Exact contract-type taxonomy (cash/basis/HTA/minimum-price families): industry-standard vocabulary, but NOT directly evidenced in reachable sources → final document speaks of "contracts whose final price is fixed at signing or priced later against a market reference" at moderate strength only.
- Storage/drying fee billing, grain held for others (customer-owned grain), warehouse receipts, government loan programs: not evidenced in reachable sources → excluded from the final document's claims; noted here.
- Grading factor sets per commodity: only moisture/grade-factor capture (Agvance) and discount schedules (Bushel) evidenced; the full factor vocabulary deliberately omitted.
- AgriDigital (AU) would likely have changed the geography balance; unreachable.
- AGRIS's own feature set known only via Bushel release notes; no direct claims.
- Whether outbound/loadout is present in every realization of the Type: evidenced in 3/4 products (and in the elevator business definition generally); kept inside L0 leg 1 ("inbound deliveries and outbound shipments") at conceptual level rather than as a separate leg to avoid over-weighting a possibly thin pole.

## Final Synthesis

The Application Type is best modeled as the grain elevator's grain-commerce system of record, defined by three jointly-held structures — ticketed grain movements (inbound and outbound), the quality-adjusted contract-and-settlement money loop with growers, and storage-located grain inventory — with contracts, quality/discount machinery, position views, grower portals, offer flows, logistics, and accounting handoff as the standard capabilities that make it operational, and with packaging (ERP module / standalone ERP / digital layer / platform) as the market's main variant axis. Market vocabulary: "grain management system", "grain accounting", "commodity management system" — all observed; the directory leaf name "Grain Elevator Management" fits the co-op/country-elevator pole best and is retained.
