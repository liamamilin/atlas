# Research Notes — Recycling Operations Management

> Slug: `recycling-operations-management` · §21 Environment, Sustainability & Climate · Research date: 2026-09-09

## Research Goal

Understand what "Recycling Operations Management" software actually is in the market: what system-of-record structure runs a recycling operation (scrap yard, MRF, e-waste/ITAD plant, deposit/CRV depot, corporate recycling network), what its core objects and workflows are, and where its boundary sits against neighboring leaves (Waste Hauling Management, Waste Management Platform, Hazardous Waste Management, Circular Economy Platform, MES).

## Initial Boundary

Initial hypothesis (before research): this is the operator-side system of record for a facility/operation that receives secondary material, processes it into classified commodity material, and ships it out — NOT the hauler's route/customer/billing system (Waste Hauling Management), NOT the generator's regulated-waste compliance record (Hazardous Waste Management), NOT the multi-party circular-economy network platform, NOT the equipment maker's tooling.

Prior-pass flags that bind this pass:

- hazardous-waste-management (processed 2026-09-08): "onsite recycling/treatment appears in this sample as a capability only; material-recovery operations belong to that leaf" — this pass must hold the material-recovery operations core.
- waste-management-platform (unprocessed): candidate discriminator = regulated-waste compliance machinery vs general waste-stream operations; this pass should test whether recycling ops is a third structure (commodity recovery loop) distinct from both.
- waste-hauling-management (unprocessed): hauler-side business operations (customers/routes/crews/billing).

## Research Questions

1. What is the unit of record — ticket? load? asset? lot? — and what does each record carry (weight, material, counterparty, price)?
2. How does the operation's material classification work (grades/commodities), and who defines it?
3. Is processing/transformation (sorting, grading, baling, dismantling, data destruction) definitional, or can a pass-through depot qualify?
4. How do the two money poles work — paying suppliers for inbound material, selling outbound commodity (pricing basis: index-linked? per-customer price books?)?
5. What inventory/stock structures exist (by grade, by site, valued how)?
6. What compliance/reporting machinery appears (US scrap-metal statutes, CalRecycle CRV, R2V3, regional recycling statistics, carbon)?
7. What interfaces do users face (scale house, mobile capture, portal, dashboards)?
8. Where does this Type end and hauling/disposal/trading/MES begin?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers + different material segments:

| Product | Pole | Segment | Tier | Evidence reached |
|---|---|---|---|---|
| AMCS Platform for Metal Recycling | integrated enterprise platform (ops↔finance, trading) | scrap metal, multi-site | large enterprise, global | `/solutions/metal-recycling-software/`, `/solutions/resources-plus-recycling/`, homepage (Tier 2) |
| ScrapRight | ticketing-first scrap-yard system w/ compliance engine | ferrous/non-ferrous scrap, auto salvage | SMB yards, US 50-state | homepage + FAQ (Tier 2) |
| WeighPay | scale-house-first connected yard ops | scrap metal, CRV, transfer stations, battery/tire | SMB–mid, North America | homepage (Tier 2; deeper pages JS-gated) |
| RecycleSoft ROMS | reporting-ledger-first recycling ERP ("Recycling Operations Management System") | e-waste/ITAD, battery, corporate recycling networks | corporate-network / regional processors | homepage + Typical Scenario page (Tier 2) |

Boundary probes (not representative products, fetched to test seams):

- Soft-Pak (soft-pak.com) — waste hauler suite; Scale-Pak = scale module. Confirms hauler-side center ≠ this Type.
- Machinex (machinexrecycling.com) — MRF/deposit equipment manufacturer with customer login gateway; equipment-side, not an operations-management product.

## Sources

- AMCS — https://www.amcsgroup.com/ , https://www.amcsgroup.com/solutions/metal-recycling-software/ , https://www.amcsgroup.com/solutions/resources-plus-recycling/ (fetched 2026-09-09)
- ScrapRight — https://www.scrapright.com/ (fetched 2026-09-09)
- WeighPay — https://www.weighpay.com/ , /features/scale-house-software , /industries/scrap-metal (fetched 2026-09-09; feature/industry pages JS-gated, homepage content only)
- RecycleSoft — https://www.recyclesoft.com/ , /recycling-scenario (fetched 2026-09-09)
- Soft-Pak — https://www.soft-pak.com/ (fetched 2026-09-09, boundary probe)
- Machinex — https://machinexrecycling.com/ (fetched 2026-09-09, boundary probe)

Abandoned after repeated transport errors (network-restricted rule): RecySystems ×2, Scrap Dragon (scrapdragon.co.uk) ×2, ScrapWorks ×2 (two domains), docs.amcs.com ×1.

**Source-access limitation:** No Tier-1 help centers / user guides were reachable in this pass (docs.amcs.com transport error; ScrapRight help not separately reachable; WeighPay deeper pages JS-gated). All evidence is Tier-2 official product/marketing pages, several with FAQ-grade operational content. Consequence: no precise numeric operational facts (hold-period day counts, ticket retention periods, exact grade lists, fee formulas, per-index names) are asserted anywhere. Assertion strength calibrated to marketing/FAQ evidence throughout.

## Product Observations

### AMCS Platform for Metal Recycling (evidence layer: A, official product pages)

Positioning: "purpose-built solution for metal recycling operations"; "connects scale, trading, transport, and finance"; "automates the daily work of dispatchers, traders, operations, and finance"; enterprise SaaS with multi-entity support, role-based permissions, location-level configuration, open API.

Key capabilities listed (A-evidence):

- **Customer and supplier management** — "Manage contracts, pricing, and relationships in one system… across suppliers, customers, and transactions."
- **Transport planning and execution** — inbound AND outbound transport with drivers/assets/third-party fleets.
- **Scale and material intake** — "Manage scale operations with role-based workflows… Automate grading, deductions, and ticketing with full traceability."
- **Inventory and production control** — "Maintain accurate inventory and ensure precise material valuations across sites. Automate grading, production, and reconciliation to reduce discrepancies and simplify period close."
- **Trading and pricing management** — "Use pricebooks and index-linked pricing to standardize trading."
- **Financial and payment integration** — "Automate settlements and reconciliation with a full audit trail behind every transaction."
- Comparison table: "real-time margin visibility… at the transaction level"; grading controls ("controls classification, reduces yield variance"); "inventory exposure tracking (real-time cost, position, yard inventory age)"; "financial-operational data linkage (scale, grading, logistics data → financial outcomes)"; "self-service trading portals (sellers and buyers manage orders, pricing, and settlement status)"; native dispatch; AI agents on "AI-ready data foundation" with human-in-the-loop.
- Customer quotes: "follow the complete journey for every material that comes into the sorting process" (Lang Recycling); "map all facets of the metal trade in one system" (Kaatsch).
- Resources+recycling suite page: recycling ERP framing — "produce higher quality materials, digitize daily operations, increase margins"; success stories are recyclers (Mazza, Schupan, A. Jansen, Recology); truck-scale operations management named as a suite capability.

Reading: the enterprise pole sells the FULL loop — scale intake → grading → production → inventory → trading/pricing → transport → settlement/finance — as one ledger with margin analytics on top. Unit of record = the transaction/ticket through scale, tied to material grades, suppliers/buyers, prices.

### ScrapRight (evidence layer: A, official homepage + FAQ)

Positioning: "The recycling software that lets you effortlessly manage transactions, stay compliant in all 50 states, generate instant reports, and track inventory in real-time." For scrap yards / metal recyclers / auto salvage.

Key capabilities (A-evidence):

- **Scrap purchasing ticketing** — "Buy metals fast while compliance handles itself. Capture IDs, build tickets, and print receipts without slowing down your line." Instant receipt printing.
- **Compliance Engine** — "first-of-its-kind… Embedded rules within the software are activated when a material with compliance requirements is identified… Built-in rules kick in automatically." FAQ: "captures seller IDs, enforces hold periods, and auto-uploads reports to local authorities, covering all 50 states without manual configuration."
- **Inventory management** — "Track every pound from purchase to sale. Know your costs and margins in real-time… live costs and margins at a glance."
- **Customer management** — "Know your sellers by name. Pull up history in seconds"; testimonials name commodity/price-per-customer configuration ("different commodities and prices for specific customers").
- **Accounting integration** — GL sync with QuickBooks, Sage, etc.
- Hardware ecosystem: integrated ATM (pays sellers), signature pad, multiple cameras, printers, work stations; iOS/Android mobile apps + browser.
- Packaging tiers: Basic (single-location compliance + ticketing) / Standard (+ reporting, hardware integrations) / Enterprise (multi-location sync).
- Customer quote: "From the time material arrives on our yard, it is tracked by ScrapRight."

Reading: the SMB pole centers the PURCHASE TICKET (inbound material from a seller, with ID capture) and the yard stock it creates, tracked to sale, with per-commodity/per-customer pricing and state scrap-law compliance machinery. Unit of record = ticket; the ledger runs buy → stock → sell.

### WeighPay (evidence layer: A, official homepage; deeper pages JS-gated)

Positioning: "Dispatch, Yard Ops & Financials… Stop running your yard on 3–5 disconnected systems today!" Built for "Aggregates · Transfer Stations · Recycling" (industries served: scrap metal, waste management, CRV recycling, aggregates, industrial recycling, tire, green waste, battery recycling…).

Key capabilities (A-evidence):

- **Scale operations** — "connect ticketing, inventory, compliance, payments, reporting, and accounting handoffs."
- **California CRV** — "connect weighing, counting, payout records, reconciliation, and CalRecycle reporting."
- **Multi-location operations** — "shared records, cross-location reporting, transfers, and consolidated accounting."
- **Dispatch and transportation** — "routes, drivers, fleet work, and billing with or without scales."

Reading: the scale-first pole: the scale house ticket is the hub that connects to inventory, compliance, payments (payout records — paying sellers), reporting, accounting. Container COUNTING alongside weighing appears in the CRV/deposit variant. Multi-site transfers as first-class records.

### RecycleSoft ROMS (evidence layer: A, official homepage + Typical Scenario page)

Positioning: "Recycling ERP software… manage complex, multi-location recycling operations with real-time reporting and automation. Accounting, scheduling, inventory, unit testing, data sanitization, custom reports, sales, CRM… R2V3 compliance is woven throughout as standard." E-waste/ITAD heritage ("ITAD company reinvents itself as a software supplier" — e-Scrap News). "ROMS" = Recycling Operations Management System (vendor's own expansion — direct lexical evidence for the leaf name).

Typical Scenario flow (A-evidence, near-operational):

1. ROMS must know "all of the locations where any recycling takes place and exactly what is recycled there" + subcontractors and what material they process from which locations.
2. Material classification down to fine granularity: "the weights of lithium ion, lead acid, alkaline, nickel cadmium, where and when they came from and where and when they were shipped to."
3. Capture: employee weighs a bale, taps a pictured material type on a smartphone app, enters weight → "RecycleSoft knows you have just produced, say, a 325 Lb bale of cardboard and it knows where that bale is." Week accumulates 30 bales in ROMS (stock accumulation).
4. Custody transfer: subcontractor (different login) picks up; either or both parties mark picked up → "ROMS will generate a virtual E-signed BOL" (bill of lading) recording the move to the subcontractor's warehouse.
5. Reporting layer: "report, down to the pound, by date range, absolutely all of your recycling worldwide, in real-time, at any level; Worldwide, by Continent, Country, State, City, location or individual sub-contractor… If needed you want to see the individual Bills of Lading."

Other modules: Mobile ROMS, Weights Manager, RecycleTime, Salesforce Automation, ReQuipment, Sustainability Reporting, Scalable Data Layers ("differentiates types of material to a single pound"), Battery Recycling software, RecycleWipe (data sanitization), Disaster Recovery, carbon metrics beyond recycling activity.

Reading: the corporate-network / reporting pole: the operation here is a NETWORK of sites and subcontractors; the unit of record is the weighted, classified material movement event (production of stock, pickup/transfer) with e-documents attached; the accumulated ledger serves statutory/ESG reporting "down to the pound." Money exists (accounting, sales) but the center of gravity is the verified material ledger + reporting. This pole proves the buy-side payment is NOT definitional (corporate recycling often moves material without purchase transactions) and that fine-grained material classification + custody documents ARE.

### Soft-Pak (boundary probe — evidence layer A for the boundary)

Whole suite is hauler-centric: operations (customer service, billing, routing), in-cab computing, routing, billing. Scale-Pak is one module (truck scales). "The Soft-Pak suite of products is a complete operational software solution… for waste hauling marketplace." ⇒ Scale/ticket machinery is shared substrate, but the hauling Type centers collection routes/service customers, not material recovery. This is the seam to Waste Hauling Management.

### Machinex (boundary probe — evidence layer A for the boundary)

Equipment manufacturer: optical sorters, robots, balers, conveyors, deposit-return (RVM) equipment, "Machinex Gateway Login" portal. MRF processing hardware ships with data capture (customer gateway), but the product population here is equipment/controls, not the operation's commercial ledger. ⇒ Processing-EQUIPMENT integration is a capability of this Type (L2), while equipment control itself is outside.

## Cross-product Comparison

| Dimension | AMCS | ScrapRight | WeighPay | RecycleSoft ROMS |
|---|---|---|---|---|
| Unit of record | scale/transaction ticket → grading, deductions, traceability | purchase ticket (ID-captured) → inventory → sale | scale ticket → inventory, payments | weighted material event (bale produced / picked up) → e-BOL |
| Material classification | grading controls, automated grading | commodities, per-commodity pricing | material + (CRV) container counting | fine-grained material types ("to a single pound"; battery chemistries) |
| Processing/transformation | grading, production, reconciliation, period close | implicit in "from purchase to sale" stock | yard stock; CRV counting | bale production; data sanitization (ITAD) |
| Stock/inventory | multi-site valuations, exposure/age | live costs & margins per pound | inventory connected to tickets | stock accumulation (30 bales), multi-location |
| Counterparties | suppliers + customers + contracts | sellers + customers history | sellers/payouts, buyers | locations + subcontractors (corporate network) |
| Outbound leg | trading, pricebooks, index-linked pricing; self-service portals | sales; margins on sale | reporting; transfers | BOL transfers; downstream shipment records |
| Money | settlements, reconciliation, payments, audit trail | ATM payout, per-customer prices, GL sync | payout records, accounting handoffs | accounting, sales (not center) |
| Compliance | auditability, governed AI (no named statute on page) | 50-state scrap law engine, ID capture, hold periods, auto-report to authorities | compliance + CalRecycle reporting | R2V3 woven throughout; statutory reporting posture |
| Transport | inbound + outbound planning/execution | (not surfaced on page) | dispatch, routes, drivers | pickup/transfer events with BOLs |
| Posture | enterprise SaaS platform, multi-entity | SMB packages, hardware-heavy scale house | scale-first connected ops | corporate-network reporting ledger |
| Center of gravity | the trade (margin across ops↔finance) | the compliant ticket | the connected ticket | the verified material ledger |

**Layer-B cross-product commonalities (observed across ≥3 of 4):**

- Ticket/transaction as the atomic record binding weight + material + counterparty (4/4).
- Inventory held by material classification, valued/tracked continuously (4/4).
- Payment/settlement machinery on at least one side (3/4 — all except RecycleSoft's network posture).
- Accounting/GL integration or financial linkage (4/4).
- Compliance/reporting machinery specific to the jurisdiction/segment (4/4, differing regimes).
- Multi-site/multi-location support with cross-location transfers/consolidation (4/4).
- Documents generated from records: receipts, tickets, BOLs (3/4 explicit; WeighPay implied by ticketing).
- Transport/dispatch of inbound or outbound loads as a connected capability (3/4 explicit on pages).
- Hardware substrate at the scale house: cameras, signature pads, printers, ATMs, phones (2/4 explicit, others implied).

**Layer-C canonical inference (to be validated below):** The Type is the recycling operation's material-ledger system of record: every pound in → classified/processed → out, with counterparties, documents, and accountability at each movement; money machinery and compliance machinery wrap the ledger.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (jointly-held, minimal)

Three structures, jointly held:

1. **The material-movement record as the unit of record.** Every inbound receipt and outbound shipment exists as an identified transaction — a ticket/load/event — bound to a weight, a material classification, and a counterparty (supplier/source or buyer/receiver). Accumulating, these form the operation's material ledger. (Remove → generic inventory or freight receiving; the ledger IS the yard's memory.)
2. **The graded material stock through the operation's own classification work.** The operation defines a grade/commodity vocabulary; its defining work is converting inbound mixed or unclassified material into classified, sellable stock — receiving, inspection/grading, processing/preparation (sorting, baling, dismantling, sanitizing — depth varies) — with inventory held and tracked by grade. (Remove → pass-through logistics or a weigh log; without classification-to-stock the "recycling" work itself disappears. A pure paper broker with no custody fails this leg → trading territory, not an operation.)
3. **The commodity-out leg.** The loop closes with recorded movements of material OUT as commodity/recovered material to buyers or downstream receivers, documented (tickets/BOLs/manifests/certificates), distinguishing recovery from disposal — in disposal, material exits as a cost; here material exits as product. (Remove → waste/disposal operations territory.)

Jointly-held is load-bearing:
- 1 alone = weigh-ticket log / scale house;
- 2 without 1+3 = process line with no ledger (equipment-side);
- 3 without 1+2 = shipment paperwork with no operation behind it;
- 1+2 without 3 = receiving/process log, never resolving outward;
- 1+3 without 2 = transfer station / cross-dock;
- 2+3 without 1 = processing with no accountability or commercial memory.

Historical check (§24): the paper-era scrap yard satisfies all three legs — weighbridge ticket book (weight+seller+material), grade price board, yard grade stock, bales shipped with BOLs, mill settlements, state license tonnage reporting — with no software, no cloud, no AI. Regional/regulatory variants (deposit depots counting containers, e-waste dismantlers with asset+certificate records, MRFs with daily tonnage reports) fit with no modern machinery. ✓

### L1 — Common Mature Structure (very common, not definitional)

- Weighbridge/scale integration and scale-house workflows (in/out weighing) — 4/4 center it even when named differently; counting (CRV/deposit) as the alternative quantification where pieces matter.
- Counterparty records (suppliers/customers/subcontractors) with history, contracts, per-customer/per-commodity pricing.
- Settlement & payments: seller payout (incl. cash/ATM at scale), buyer invoicing, reconciliation, GL/accounting integration.
- Inventory valuation: cost per unit weight, margins, stock age/exposure.
- Document generation: tickets, receipts, BOLs/manifests, certificates.
- Compliance & reporting machinery (regime-specific: US scrap-metal statutes, hold periods, ID capture, law-enforcement reporting; CalRecycle; R2V3; regional statistics).
- Transport planning/execution for inbound and outbound loads.
- Multi-site: shared records, transfers, consolidated reporting/accounting.
- Reporting layer over the ledger: by material, period, site, counterparty — down to fine granularity; sustainability/carbon metrics commonly added.
- Role-based permissions/auditability.

### L2 — Variant / Optional Structure

- Segment/industry variant: scrap metal yard · MRF (commingled/single-stream) · e-waste/ITAD (asset-level tracking, data sanitization certificates) · deposit/CRV depot (counting, deposit accounting) · battery/tire/green waste · corporate recycling network (locations+subcontractors).
- Money depth: full two-sided trading with index-linked pricebooks (enterprise pole) ↔ payout+tickets (SMB) ↔ none/latent (corporate network pole).
- Classification granularity: coarse commodity grades ↔ "to a single pound" material-type layers.
- Processing depth: grading-only ↔ full production reconciliation/period close ↔ manufacturing-like dismantling with unit testing (ITAD).
- Regulatory regime: 50-state US scrap laws / CalRecycle / R2V3 / EPR-style reporting — machinery is regime-shaped, presence of *some* accountability layer is L1.
- Quantification substrate: weighing ↔ counting ↔ both.
- Deployment: cloud SaaS ↔ on-prem/hosted; hardware-coupled scale house ↔ mobile-app capture ↔ browser.
- AI overlays: pricing-anomaly detection, grading variance, contamination detection — era-current, not definitional.

### L3 — Vendor-specific (research notes only)

- AMCS: governed/agentic AI framework, "RECY to Cloud" migration webinar, self-service trading portals, comparison-table competitor claims.
- ScrapRight: "Compliance Engine" brand, 50-state auto-upload claim, Basic/Standard/Enterprise packaging, ATM/signature-pad/camera hardware bundle, "4 generations of scrap industry experience" claims.
- WeighPay: "Ask Sarah" sales assistant, Auto Assist guided configuration, aggregates/seafood-adjacent industries, ROI calculator.
- RecycleSoft: ROMS/ROMS Lite naming, RecycleCoin (blockchain-verified recycling proof), RecycleWipe data-wipe product, R3eWaste network, stored-procedure/encryption implementation claims.
- Machinex: equipment gateway portal (equipment-side).
- Soft-Pak: Scale-Pak module name (hauler-side).

## Boundary Findings

1. **vs Waste Hauling Management (§21, unprocessed)** — hauling: collection routes, service customers, containers, crew billing (Soft-Pak probe: entire suite hauler-centric; scale module incidental). Recycling ops: facility/network material recovery ledger. Scale+ticket machinery is shared substrate. AMCS ships both as separate solutions — vendor-side confirmation the market holds them apart. Remove the material-processing loop and this Type becomes hauling; remove routes/service customers and hauling becomes this Type's neighbor.
2. **vs Waste Management Platform (§21, unprocessed)** — waste-stream operations center service delivery and disposal as terminal state; recycling ops centers recovery of commodity value with material exiting as product. Test recorded for that pass: material-disposal machinery vs material-recovery loop. (The hazardous-waste pass's discriminator — regulated-waste compliance machinery — is a third structure; three-way seam: disposal ops / regulated-waste compliance / recovery ops.)
3. **vs Hazardous Waste Management (processed 2026-09-08)** — flag discharged: that leaf = generator-side compliance record for shipped-out waste (profiles, codes, manifests); onsite recycling appears there only as a capability. Material-recovery operations = this leaf. Confirmed direction.
4. **vs Circular Economy Platform (processed 2026-09-07)** — CE platform: multi-party network for circular outcomes (objects move between participants; pathways incl. recycling; impact visibility). Recycling ops: ONE operator's (or one corporation's network's) system of record for actually processing material. A CE platform may route an item toward "recycling"; this Type runs the facility that does it. Participant-network vs operator-ledger seam.
5. **vs MES (§16, processed 2026-09-09)** — parallel abstract shape (process execution + traceability) but different unit of record: MES executes released production orders against defined processes at unit/lot grain inside manufacturing; recycling ops centers commercial material movements (buy/grade/process/sell ledger) with counterparties and commodity pricing. An MRF's line controls sit equipment-side (Machinex probe).
6. **vs Scrap/commodity trading (broker desks)** — no material custody, no processing, no movement records → outside the Type even though trading modules exist inside enterprise products (AMCS). Custody+processing is the seam.
7. **vs Resale/Recommerce (§05, processed 2026-09-07)** — resale moves whole items back into use; recycling breaks items into classified commodity material. Item-of-record vs material-of-record.

## Uncertainties

- No Tier-1 operational docs reached; all findings are marketing/FAQ-grade (recorded above). Exact ticket workflows, hold-period mechanics, grade-list structures, index integration details NOT asserted.
- MRF-production software (line-data integration, bale-production analytics beyond AMCS mentions) could not be sampled from a dedicated MRF-software vendor this pass; processing-depth variant axis is asserted from AMCS/RecycleSoft evidence + equipment probe only.
- European/regional vendors (RecySystems, Scrap Dragon) unreachable — regional-variant claims are correspondingly weakened; the historical paper-era check partially compensates.
- Deposit-return systems (bottle depots) as a pole evidenced only via WeighPay's CRV capability + Machinex's deposit equipment context; a dedicated deposit-system software product was not sampled.
- WeighPay's deeper feature pages are JS-gated; its capability set beyond the homepage's four bullets is unverified.
- Whether a "transfer-station-only" product without any classification/processing leg exists as a distinct market product — probable (WeighPay serves aggregates/transfer stations) but unverified; seam recorded in boundary finding 1's "remove → transfer station" logic.

## Final Synthesis

Recycling Operations Management is the recycling operation's system of record for its material economy. The defining core is three jointly-held structures: (1) the material-movement record — identified tickets/loads/events each carrying weight + material + counterparty, accumulating into the operation's ledger; (2) graded material stock produced by the operation's own classification work — converting inbound mixed material into classified, sellable stock held by grade, with processing depth varying by segment; (3) the commodity-out leg — recorded, documented outbound movements of material as product to buyers/downstream receivers, distinguishing recovery from disposal. Money machinery (supplier payout, commodity sale, index-linked pricing), compliance machinery (jurisdiction/segment-specific), transport, multi-site, documents, and reporting wrap the ledger as common mature structure; segments (scrap yard, MRF, e-waste/ITAD, deposit/CRV, corporate network), money depth, classification granularity, and deployment are variant axes. The paper-era yard satisfies the core; remove the commodity-out leg and it becomes disposal ops; remove classification-to-stock and it becomes transfer/haulage; remove custody and it becomes trading.
