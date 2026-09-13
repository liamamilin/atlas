# Research Notes — Seed Production Management

Research date: 2026-09-10
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what a **Seed Production Management** application actually is, from real products: what objects exist inside it, who uses it, how the seed-multiplication work flows through it, which states and rules matter, and where its boundary lies against Farm Management, Contract Farming, Food Traceability, Grain Management, and certification-agency systems.

## Initial Boundary (hypothesis before research)

- **What**: software for seed-producing organizations (seed companies, breeders with multiplication programs, cooperatives, contract-multiplication operations) that plans and tracks the multiplication of named varieties into seed lots — variety × grower × field allocation, field inspection, lots through conditioning/testing/bagging, certification & traceability.
- **Who**: seed production managers, grower relations / field officers, inspectors, conditioning plant & QA staff, inventory/sales staff.
- **Easiest confusions**: Farm Management Platform / Crop Management (field ops but food/feed crop), Contract Farming modules of agribusiness ERPs, Food Traceability Platform (lot traceability but no varietal identity/generation), Government Inspection Management (certification *agency* side), Grain Management (commodity, no variety identity), Nursery Management (plant propagation), breeding management software (creates varieties; this Type multiplies them).
- **Unknowns**: actual product landscape; whether certification machinery is core or variant; how generation/class is modeled; whether sales/distribution is core.

## Research Questions

1. What is the central object — seed lot? production contract? field? variety?
2. How is the generation/lineage chain (basic/breeder seed → certified classes) tracked?
3. What role do contract growers play — how are production contracts and settlements managed?
4. How do field inspections and siting constraints (isolation, previous crop) enter the workflow?
5. What happens after harvest: intake, conditioning, treatment, testing, bagging, inventory?
6. How does certification documentation work (tags, labels, bulk certificates, agency interfaces)?
7. What users/roles exist?
8. How does sales/distribution relate to lots?
9. What distinguishes this Type from generic farm management / contract farming?
10. What variants exist (species, certification regimes, breeding-integrated vs pure multiplication)?

## Representative Products

Selected for market representativeness + documentation availability + different product philosophies + different customer levels:

| # | Product | Vendor | Philosophy / position | Evidence quality |
|---|---|---|---|---|
| 1 | Agreo Seeds | SMAG (France) | Dedicated seed-production business suite (upstream production + industrial plant); Europe; breeders, multipliers, cooperatives; customers incl. KWS, Limagrain, Sakata, Florimond Desprez, SESVanderHave, Semences de France | A (official product pages, blog, testimonials) |
| 2 | ERP for Seed | Unify Dots (built on Microsoft Dynamics 365) | Seed-specific verticalization of a horizontal ERP; North America | A (official module pages) |
| 3 | FarmERP (Seed Production & Traceability) | Shivrai Technologies (India) | Multi-vertical agribusiness ERP platform with a seed vertical; India/global | A (official pages) |
| 4 | Cropin Cloud (seed production) | Cropin (India/global) | Agri-intelligence platform for seed companies (field ops + AI); customers incl. Syngenta, Bejo, BASF, Sakata, KWS, East-West Seed | A (official solution page + customer case-study PDF) |
| 5 | Folio3 AgTech Seed Management | Folio3 (US/Pakistan) | Build-to-order seed software suite; also builds certification-agency inspection apps (ICIA) | B/C (search-snippet evidence; direct fetch returned 403 — see Source-access Limitation) |

Boundary/counter-sample sources (not in-type, used for domain process and boundary reasoning):

- North Dakota State Seed Department — Certified Seed Grower's Manual, Field Inspection pages (certification agency side)
- eCFR 7 CFR Part 201 (Federal Seed Act regulations — certified seed) — regulatory definition of the certification process
- SATHI portal (India, NIC/Ministry of Agriculture) — regulator-side national seed traceability
- South Dakota Crop Improvement / CSGA "Seed Tracking System" manual — agency-side grower portal
- eOrganic — Seed Production Contracting guidelines (domain knowledge of grower contracting)
- Stoneridge Software — Dynamics 365 for seed suppliers (implementation-partner evidence, Tier 3)

## Sources

Tier 1/2 (official, fetched 2026-09-10):

- SMAG — Seed production product page: https://smag.tech/en/our-software/seed-production-management-software
- SMAG — Agreo SEEDS launch blog: https://smag.tech/en/blog/smag-launches-agreo-seeds
- SMAG — KWS chooses Agreo Seeds: http://smag.tech/en/blog/kws-chooses-agreo-seeds
- SMAG — Agro-food production (Agreo agribusiness module detail): https://smag.tech/en/agro-food-production-software
- ERP for Seed — Home: https://erpforseed.com/
- ERP for Seed — Grower Contracts: https://erpforseed.com/grower-contracts/
- ERP for Seed — Seed Production & Processing: https://erpforseed.com/seed-production-processing/
- FarmERP — digital.farmerp.com (solution suite incl. Seed Production & Traceability): https://digital.farmerp.com/
- FarmERP — home: https://www.farmerp.com/
- Cropin — Seed production solution: https://www.cropin.com/seed-production
- Cropin — case study PDF "Seeds for the World" (global vegetable seed major): https://www.cropin.com/wp-content/uploads/2025/07/Seed-Producer-Global-agri-operations-transformation-on-Cropin-Cloud.pdf
- ND State Seed Department — Field Seed / Seed Certification / Field Inspection: https://www.seed.nd.gov/field-seed , https://www.seed.nd.gov/field-seed/seed-certification , https://www.seed.nd.gov/field-seed/seed-certification/field-inspection
- ND State Seed Department — Certified Seed Grower's Manual (PDF): http://seed.nd.gov/sites/www/files/documents/CertifiedSeedGrowersManualFinal.pdf
- eCFR — 7 CFR Part 201 (Certified Seed): https://www.ecfr.gov/current/title-7/subtitle-B/chapter-I/subchapter-K/part-201
- SATHI portal (ISSCA record): https://issca.icrisat.org/scalable-solutions/seed-traceability-authentication-and-holistic-inventory-sathi-portal ; PIB launch release: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=1917890
- SD Crop Improvement / CSGA Seed Tracking System manual (PDF): https://agsci.colostate.edu/seeds/wp-content/uploads/sites/145/2025/12/NEW-CO-Seed-Tracking-System-Instruction-Manual-CSGA.pdf
- eOrganic — Seed Production Contracting: https://eorganic.org/node/381

Tier 3 (search-snippet evidence only):

- Folio3 AgTech — Seed Management Software: https://agtech.folio3.com/seed-management-software (direct fetch 403; content from search-result excerpts)
- Stoneridge Software — D365 for seed suppliers: https://stoneridgesoftware.com/industries/agriculture/seed-suppliers

**Source-access Limitation**: Folio3's product page could not be fetched (HTTP 403). Its observations below are based on search-result excerpts of the official page and are marked as such; assertion strength reduced accordingly. No precise numeric limits, prices, or default values are claimed anywhere in this research.

---

## Product 1 — Agreo Seeds (SMAG)

### Key observations (Evidence layer A unless noted)

- Positioning: "agreo Seeds software functionally covers all of your seed station processes, **from production planning to processing, including logistics and invoicing of your batches**."
- Multi-species: "monitor and manage seed production for **self-pollinating, hybrid, vegetable, fodder and floral plant species**."
- Multi-site: "remotely manage several production sites and centralise data for reporting purposes."
- Heritage composition (launch blog): Agreo Semences (upstream production data: **production planning, contracting with producers, field and technical monitoring**) + EuroSemences (production management and **industrial traceability**: plant, processing, laboratory, logistics, sales management, invoicing).
- Functional blocks (launch blog): Production management (**production plan, provision of basic seeds, contracting, technical monitoring**); Management of manufacturing plants and stocks (seeds and consumables); **Laboratory Management**; Sales management (order, delivery, **batch invoicing** and prices).
- Mobile: "mobile applications dedicated to both technical monitoring (**agreo mobile inspection**) and the **barcode management of production orders at the factory**."
- Users/constituency: "cooperatives, trades, breeders, multipliers, production organizations, research stations or **official control services**."
- Customer evidence: KWS (global seed leader) uses Agreo for agronomic data in seed production; goal "using Agreo as the sole business software that will be connected to SAP"; "20 users … full version or the light version"; "inputting field annotations or uploading photos directly from the fields". KWS quote: "We looked for solutions to make the exchange of data between us and the seed producers happen only in one database."
- Testimonial (Semences de France, production engineer): "Thanks to AGREO, we have **reliable and complete traceability from the field to the factory**."
- Business-impact claim (vendor): "a threefold reduction in the process of producer payments" (i.e., grower settlement is a managed process).
- Sibling product (Agreo agribusiness, same platform family) shows the platform's contract/plot machinery: plot setup with crop references and boundaries, contract management with workflows, technical/economic monitoring of interventions, reception–acceptance of batches with acceptance grids, invoicing by contract. (Layer B — same platform, adjacent vertical; used only to understand machinery, not to claim seed features.)

## Product 2 — ERP for Seed (Unify Dots, on Dynamics 365)

### Key observations (Evidence layer A)

- Positioning: "ERP platform for planning, grower management, seed processing, quality testing, packaging, distribution, and financials — built on Microsoft Dynamics 365 Finance and Supply Chain."
- **Grower Contracts**: "agreements, contracted acreage, expected yields, field locations, and harvest timelines"; "contract creation, monitor grower performance throughout the season, and automate settlements using integrated production, procurement, and financial workflows"; screenshot shows "field activity logging, contract terms and quality settings, and contract line items with pricing, quantities, and delivery schedules"; "Automate grower settlements based on **delivered quantities, quality test results, and contract terms**."
- **Seed Production & Processing**: "from planting through harvest intake, conditioning, processing, and packaging"; "Track field activities, **inspections**, production orders, and inventory movements"; "Manage seed processing activities including **cleaning, drying, grading, blending, and treatment in alignment with defined varietal and quality standards**"; "**only approved seed batches progress to packaging and sale**"; "Track production and processing costs at the **lot, batch, and variety level**"; screenshot: "production formulas with ingredient quantities and batch reservation … stock status, batch numbers, expiration dates, and availability."
- **Quality, Traceability & Compliance**: "complete **batch genealogy from grower lots to finished goods**"; "Capture **germination, purity, and viability** test results and link them directly to inventory and production processes"; "Meet regulatory standards, respond quickly to **audits or recalls**."
- **Demand Planning & Forecasting**: "Optimize production planning, inventory levels, and **grower allocations** by balancing supply and demand."
- Also: Pricing Management (seasonal pricing, contract-based pricing), BI (Power BI dashboards).

## Product 3 — FarmERP (Seed Production & Traceability vertical)

### Key observations (Evidence layer A)

- Vertical: "Seed Production & Traceability — Digitize seed production, **quality assurance, processing, and distribution** with complete traceability and compliance across the seed lifecycle." Feature points: "End-to-End Seed Traceability", "Smarter Seed Production Planning", "Integrated Quality & Compliance Management."
- Platform context: agribusiness cloud with farm profile, production, contract farming, planning, inventory, quality control modules; mobile app with offline data capture ("uninterrupted field data capture in remote locations"); modules listed on the app: Farm Profile, Production, Contract Farming, Planning, Inventory, Quality Control.
- Contract-farming heritage (blog, Layer B for the platform's contract machinery): farmer profiles with crop/plot details and plot history; contracts with "yield category, pre-agreed price, quantity or acreage of the yield, quality standards, and a definitive time frame"; procurement linked back to contracts (weight, plot area, quality, dates, rates); inputs issued to farmers on credit.
- Seed industry is a named business category in their success-story selector ("Seed Industry").

## Product 4 — Cropin Cloud (seed production)

### Key observations (Evidence layer A)

- Solution page: "Seed management software for seed production companies"; named customers: Syngenta, Bejo, Savannah, BASF, Bioseed, East-West Seed, Sakata, KWS.
- Audience split on the page: "For breeding & trialing … For seed sales & marketing … For all departments … **For seed multiplication**."
- For seed multiplication: "Optimize **production planning** while ensuring adherence to the **package of practices**, **farmer engagement**, and **compliance** with **end-to-end traceability**"; "Predict yields with region-specific accuracy"; "Digitize supply chains and inventory flow."
- For breeding & trialing: "Ensure **multi-generational traceability** with a digital footprint for each seed variety across diverse environments."
- Case study (global vegetable seed major; Netherlands pilot; 40 crops — cabbage, beetroot, onion, carrot, tomato, cucumber, cauliflower — hundreds of varieties):
  - "centralized platform for tracking, managing, and monitoring every step – from sowing the seed for germination to execution and finally harvest"
  - integrates ERP + supply-chain planning tool + **crop variety database**; "agri-object model" structures agricultural data
  - flow: "Project is created → Crop able area with crops and varieties displayed → Yield estimation → Traceability → Cost of production"
  - "capturing the entire journey from **seed to bulb and bulb to seed**" (onion two-year multiplication cycle) — "complete traceability of the seed production process"
  - field layer: "Streamline scouting for diseases and pests", "Gain insights into **pollination success rates**", "Ensure adherence to the prescribed Package of Practices (PoP)", "Monitor and optimize chemical input usage"
  - "specialized nurseries" and "diverse small and large farms" as production contexts
- EWS case: "100% production visibility … visibility to seed varieties & field ops … inputs traceability & output predictability."

## Product 5 — Folio3 AgTech Seed Management (Evidence layer C — search snippets only)

### Key observations (downgraded evidence; page fetch 403)

- "gain visibility from **grower contracts to global distribution** across your entire seed lifecycle"; "complete oversight of each **seed lot**, with full traceability from production and treatment through storage, sales, and distribution."
- Lot attributes: "Germination Test Results, Bag Label Generation, Purity Percentage Capture, Lot Attribute Drilldown, Seed Treatment Tracking, Moisture Content Recording."
- Inventory/fulfillment: "FEFO/LEFO Allocation, Load Consolidation, Pick Ticket Creation, Packing List Generation, Carrier Rate Shopping, Proof of Delivery."
- Grower side: "Fair Settlements with Growers and Vendors — automating contract reconciliation across volumes, seed grades, deductions, and payments"; "Grower Contract Setup"; "Track grower fields, agreements, and performance while ensuring **multiplications** deliver consistent quality and volume every single season."
- Processing: "Seed Processors — Monitor conditioning, cleaning, and treating workflows, maintaining purity and compliance."
- Identification: "QR/Barcode Batch Tracking — Scan any bag or lot barcode to instantly access seed quality, location, and compliance details"; mobile with offline ("even without internet connectivity").
- Certification-agency adjacency: "A mobile-first inspection platform was built for **ICIA** [Iowa Crop Improvement Association], featuring GPS-enabled workflows, real-time notifications, task tracking, and PDF exports to automate and digitize crop inspections."
- Stated audience: "breeders, large-scale producers, contract growers, processors, distributors, retailers, and **certification labs**."

## Boundary / domain sources (not in-type)

### ND State Seed Department + eCFR 7 CFR 201 (certification process, agency side)

- Five basic steps of seed certification: "field inspection, seed conditioning, quality testing, final certification and labeling."
- "The unit of certification shall be a clearly defined field or fields" (eCFR §201.67(b)); "One or more field inspections shall be made … previous to the time a seed crop … is to be harvested, and … when genetic purity and identity can best be determined."
- Field inspection checks "other varieties, other crops, weeds or seed-borne diseases and whether the crop conforms to the breeder's variety description"; isolation ("The field must be clearly defined and properly isolated according to the specific crop standards"); roguing.
- Class system: application requires "Bulk certificate or tag from Foundation or Registered seed"; "The field will be inspected to the next lower class, i.e. a field planted as registered class seed will be inspected as certified class seed."
- Conditioning: "field inspected seed must be conditioned by an [approved conditioner]"; conditioners must review the Field Inspection Report prior to conditioning; "Records of all operations relating to certification shall be complete and adequate to account for all incoming seed and final disposition of seed" (eCFR §201.73(c)); "Identity of the seed must be maintained at all times."
- Testing: sample submitted with Seed Sampler's Report; lab (report of analysis); "Tests Required for Labeling Certified Seed"; "Seed Lots on Hold".
- Final certification & labeling: official label identifies "the certifying agency, the lot number …, the variety name, and the kind and class of seed"; bulk certificates (C#); "Seed lots of the same variety and class may be blended and the class retained" (eCFR §201.73(f)); downgrading seed lots; carryover seed.
- Re-inspection after correction; failed field may not be cancelled.

### SATHI portal (India, regulator side)

- "records every seed lot's journey—from breeder, through processors and dealers, to the final buyer—using QR/bar-code tagging and real-time inventory updates."
- "Automation of **breeder-seed indents, allocations and lifting**"; "blocks damaged or non-conforming lots"; seven verticals: Research Organisation, Seed Certification, Seed Licensing, Seed Catalogue, Dealer to Farmer Sales, Farmer Registration, Seed DBT.
- Confirms the same domain spine (breeder seed → grower → processing → dealer → farmer) from the regulator's viewpoint.

### SD-CIAC / CSGA Seed Tracking System (agency-side grower portal)

- Grower functions: field inspection applications, document corrections, report harvest amounts, seed sample submission, view lab results, create sales certificates, inventory management/seed disposition, invoicing.
- Confirms the certification workflow (application → inspection → harvest report → sample → analysis → status assignment → sales certificates) and that the agency side is a distinct system-of-record territory.

### eOrganic — Seed Production Contracting (domain knowledge)

- Contract content: quality standards (germination rate, vigor, purity, seed moisture) as basis of payment; deductions for sub-standard lots; roguing responsibilities; partial payments during the season; drying responsibility; indemnity for crop failure; field inspection planning involvement.

### Stoneridge (D365 partner, Tier 3)

- Seed-company pattern on a horizontal ERP: bookings & contracts, royalty management, production planning, lot tracking, blending, outside vendor processing (drying/cleaning), raw→clean inventory states, silo management. Corroborates ERP for Seed's structure (Layer B).

---

## Cross-product Comparison

| Structure | Agreo Seeds | ERP for Seed | FarmERP | Cropin | Folio3 (C) |
|---|---|---|---|---|---|
| Variety as master data (multi-species) | ✔ (self-pollinating, hybrid, vegetable, fodder, floral) | ✔ (variety-level costing; varietal standards) | ✔ (seed vertical) | ✔ (crop variety database; 40 crops / hundreds of varieties in case) | ✔ |
| Multiplication production plan (variety × area × grower) | ✔ (production plan; provision of basic seeds) | ✔ (contract planning linked to production planning; grower allocations) | ✔ (seed production planning) | ✔ (project created from variety DB → croppable area → yield estimation) | ✔ (production yield forecasting) |
| Grower/producer contracts | ✔ (contracting with producers) | ✔ (grower contracts module) | ✔ (contract machinery) | ✔ (farmer engagement) | ✔ (grower contract setup) |
| Field/plot allocation + technical monitoring | ✔ (field & technical monitoring; mobile inspection) | ✔ (field activities, inspections) | ✔ (field monitoring) | ✔ (remote monitoring, scouting, PoP adherence, pollination rates) | ✔ (grower fields; GPS inspection app) |
| Seed lot as unit of record | ✔ (batches; batch invoicing; field→factory traceability) | ✔ (lot/batch/variety costing; batch genealogy) | ✔ (end-to-end seed traceability) | ✔ (seed-to-bulb-to-seed traceability) | ✔ (lot attribute drilldown; QR/barcode) |
| Quality testing (germination/purity/moisture) | ✔ (laboratory management) | ✔ (germination, purity, viability linked to inventory) | ✔ (quality assurance) | ✔ (germination-related workflows) | ✔ (germination, purity %, moisture) |
| Conditioning/processing orders | ✔ (processing; plant management; barcode production orders) | ✔ (cleaning, drying, grading, blending, treatment; production formulas) | ✔ (processing) | partial (farm-to-factory; less explicit) | ✔ (conditioning, cleaning, treating; blending) |
| Lot inventory | ✔ (seeds and consumables stocks) | ✔ (inventory movements; batch reservation) | ✔ (inventory) | ✔ (inventory flow) | ✔ (FEFO/LEFO allocation) |
| Quality gate on progression | implied (traceability discipline) | ✔ explicit ("only approved seed batches progress to packaging and sale") | ✔ (quality & compliance) | ✔ (quality workflows with field ops) | ✔ (compliance details on scan) |
| Certification/labeling machinery | not explicit (official control services are users) | ✔ (regulatory standards, audits, recalls) | ✔ (compliance management) | ✔ (compliance) | ✔ (bag label generation; certification labs audience) |
| Sales/order/distribution | ✔ (order, delivery, batch invoicing) | ✔ (pricing, distribution) | ✔ (distribution) | ✔ (seed sales & marketing) | ✔ (pick tickets, POD, carrier) |
| Grower settlement/payment | ✔ (producer payments process) | ✔ (automated settlements from qty + quality + terms) | ✔ (contract payments) | less explicit | ✔ (reconciliation, deductions) |
| Demand planning → production | not explicit | ✔ | ✔ (planning module) | ✔ (predict demand) | ✔ (yield forecasting) |
| Mobile/offline field capture | ✔ (agreo mobile inspection) | not explicit | ✔ (offline app) | ✔ (remote monitoring) | ✔ (offline mobile) |
| Breeding/trialing support | ✔ (research stations among users) | ✘ | ✘ (separate verticals) | ✔ (breeding & trialing audience) | ✔ (breeders as audience) |

Reading of the comparison:

- The **variety-anchored lot pipeline** (variety master data → multiplication plan → contracted fields → lot with genealogy → testing → conditioning → inventory → release/sale) is present in every sampled product. This is the Type's spine.
- **Grower contracting + settlement** is near-universal (4/5 explicit; Cropin implicit via farmer engagement) — common mature structure, not definitional (a fully vertically-integrated seed operation could run the same lot pipeline on its own farms).
- **Certification-specific machinery** (labels, tags, agency interfaces) is explicit in only some products and is regulator-dependent — variant, not core.
- **Sales/distribution** is present in all, but KWS's pattern (Agreo as production system connected to SAP) shows production can be deployed without owning the sales layer — common, not core.
- **Breeding/trialing** appears in 3/5 as an adjacent audience — optional module territory, and the boundary against breeding management software must be drawn.

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures over one binding:

1. **The seed lot as unit of record with varietal identity and generation.**
   A persistent, identified record of a quantity of seed of a named variety, carrying its generation/class of seed stock (e.g., breeder → foundation → registered → certified, or the company's equivalent), its lineage (parent lot / producing field), and its own lifecycle from production through conditioning, testing, and disposition. The lot accumulates its quality record and remains addressable after completion (inventory, carryover, recall, genealogy).
   *Remove → generic crop/farm management plus a plain inventory system; the "unit" reverts to the field or the SKU, not the lot.*

2. **Variety-anchored multiplication planning over contracted production.**
   The application holds the plan that decides which variety (and which generation of parent/basic seed) is multiplied on which fields, by which growers, in which season — under production contracts carrying area, expected yield, quality standards, and settlement terms — with seed-specific siting constraints (isolation, previous crop, class of planted seed) applied at allocation.
   *Remove → contract farming / crop management: fields and growers exist but nothing is being multiplied toward varietal identity.*

3. **Identity-and-quality gatekeeping to lot release.**
   Field inspections (isolation, off-types, disease, conformity to variety description) and lab tests (germination, purity, moisture, seed health) are recorded against the field/lot; results determine the lot's status and whether it may progress (conditioning → packaging → sale) and at what class/label; identity and quality status travel with the lot through every movement.
   *Remove → produce traceability or a warehouse QC tool; lots move on logistics, not on identity/quality gates.*

**Binding — seed-multiplication semantics**: the product being managed is *planting seed*, whose value is varietal identity and genetic purity, not food/feed commodity. Remove the binding → grain management or contract farming for commodity crops.

**Jointly-held load-bearing tests**:

- 1 alone = lot inventory / traceability tool (Food Traceability territory)
- 2 alone = contract farming / crop management
- 3 without 1+2 = inspection/testing checklist tool
- 1+2 without 3 = multiplication logistics with no quality discipline
- 1+3 without 2 = lot QC without planned multiplication (a conditioner's QC system)
- 2+3 without 1 = field agronomy with inspections but no lot continuity

### L1 — Common Mature Structure

- Grower/producer contracts with lifecycle (create → execute → settle) and settlement computed from delivered quantity × quality results × contract terms
- Field/plot records with boundaries/maps; field activity and technical monitoring; mobile/offline inspection capture
- Conditioning/processing orders (cleaning, drying, grading, blending, treatment) with production orders at the plant; barcode/QR identification of lots and orders
- Lot inventory by location and state (raw/conditioned/treated; FEFO-style allocation observed in one product)
- Laboratory/test-result management linked to lots
- Demand planning / sales forecast feeding the multiplication plan
- Sales, order, and distribution management with lot-level invoicing
- Grower payment/settlement processing
- Dashboards/BI over plan vs actual, quality, inventory

### L2 — Variant / Optional Structure

- Certification-specific machinery: tag/label generation, bulk certificates, agency-facing applications, certification status per lot — depends on whether the market runs mandatory certification (US/Canada/EU/India) vs company-internal QA
- Generation-class vocabulary itself (breeder/foundation/registered/certified) — agency-side realization; companies may run internal class schemes
- Breeding/trialing modules (variety development, trials, demo plots) — adjacent Type's territory, bundled by some platforms
- Royalty / trait-fee management (traited seeds) — observed in the D365 partner pattern
- Species-specific workflows: hybrid pollination monitoring, biennial cycles (seed→bulb→seed), nursery-raised transplants in vegetable seed
- Organic-specific requirements and charters
- Multi-site/multi-country deployment; multi-language
- AI yield prediction, satellite/remote monitoring, sustainability metrics
- Counterfeit protection / consumer-facing QR verification (regulator-side in SATHI; vendor-side in Cropin Trace)

### L3 — Vendor-specific (Research Notes only)

- Agreo: "provision of basic seeds" workflow; agreo mobile inspection; barcode production orders; threefold producer-payment reduction claim; light/full user versions (KWS)
- ERP for Seed: D365 production formulas + batch reservation; Power BI; AI-assisted analytics
- FarmERP: 10X packaging (Grow10X/OutGrow10X/ProcessPack10X…); Field Connect IoT; FarmGyan AI
- Cropin: Sage AI assistant; "agri-object model"; Crop Knowledge Grid; Cropin Trace smart labels
- Folio3: FEFO/LEFO allocation naming; ICIA inspection app; carrier rate shopping

### Anti-overfitting checks (§22 / §24 discipline)

- **Shared-implementation ≠ invariant**: all five sampled products are modern cloud/ERP systems with mobile capture; mobile capture is L1, not L0. Paper-era seed production (field inspection applications on paper, lot registers, tags, ledgers — still documented in the ND manual's form appendices) satisfies all three L0 structures without any software-era feature.
- **Historical check**: certification is a 100+ year-old process ("originated more than 100 years ago" — ND manual). Pre-digital seed organizations ran the same three structures on paper: the multiplication plan in the production office, the lot register with class and test results, inspection reports filed per field. L0 holds.
- **Regional check**: India's SATHI (regulator side) and US AOSCA-style certification (agency side) describe the same domain spine; European cooperative multiplication (Agreo's constituency) likewise. The company-side core is region-neutral.
- **Certification machinery is NOT definitional**: it is regulator-dependent (L2). A seed company producing under internal QA only (common in private vegetable-seed breeding) still needs the lot pipeline, multiplication planning, and quality gating.

### Rejected Findings

- "Seed Production Management = contract farming for seed" — rejected: contract farming lacks the lot-with-generation unit and the identity/quality gate; the lot, not the contract, is the unit of record.
- "Certification integration is the core" — rejected: only some products expose it explicitly; it is regulator-dependent variant machinery.
- "Sales/distribution is core" — rejected: KWS runs Agreo as the production system connected to SAP; production can be deployed without the sales layer.
- "AI yield prediction / satellite monitoring is core" — rejected: modern differentiators, L2.
- "FEFO allocation is standard" — observed in one product (Folio3, C-layer evidence); keep product-specific.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove to cross) |
|---|---|---|
| Farm Management Platform / Crop Management | adjacent, upstream consumer of same field layer | FM manages a farm's crop for food/feed harvest; no varietal identity, no generation/class, no lot genealogy, no certification gating. Remove the lot/class machinery → crop management. |
| Contract Farming (agribusiness ERP procurement) | overlapping machinery | Grower contracts exist in both; in seed production the contract is anchored to variety multiplication with parent-seed provision and quality-grade settlement, and everything rolls into lots. Remove lot identity → contract farming. |
| Food Traceability Platform | shares "lot traceability" vocabulary | Food traceability's unit is a food-safety lot (harvest/origin/handling); seed traceability's unit carries varietal identity + generation + certification status, and the purpose is genetic identity/purity, not food safety. |
| Grain Management / Grain Origination | commodity neighbor | Grain quality = grade factors (test weight, moisture, damage); no variety-identity requirement, no class system, no isolation. Remove variety identity → grain management. |
| Government Inspection Management / certification-agency systems (ND Seed Dept, SATHI, SD-CIAC) | external authority counterpart | The agency inspects and certifies; the company manages production. Agency systems model applications, inspections, certificates, tags as their own records; company systems consume inspection/certification outcomes as gates. Folio3 building an app *for* ICIA shows the two territories are distinct markets. |
| Nursery Management | propagation neighbor | Nursery manages plant propagation (batch of plants, greenhouse); seed production manages field-multiplicated seed lots with class system. Vegetable seed blurs at "specialized nurseries" (Cropin case) but the lot/class spine stays decisive. |
| Breeding management software (e.g., Phenome-type) | upstream neighbor | Breeding *creates* varieties; seed production *multiplies* them. Some platforms bundle both (Cropin's breeding & trialing audience; Agreo serving research stations); the leaf is the multiplication side. |
| Inventory Management System / WMS | capability overlap | Lot inventory exists here, but with variety/class/lineage semantics and the field-production upstream; a bare inventory system has neither. |
| Agribusiness ERP | host/sibling | Several products are ERPs with a seed vertical; the Type is the vertical's core model, not the ERP shell (financials, GL, HR are out of scope). |

**"去掉什么就变成另一个 Type" summary**:
- Remove lot/class/genealogy → Crop Management + generic inventory
- Remove multiplication planning/contracts → lot QC & traceability tool
- Remove quality/inspection gating → contract farming + warehouse
- Remove seed semantics (variety identity as the value) → Grain Management

## Uncertainties

1. **Folio3 evidence is search-snippet only** (fetch 403). Its distinctive claims (FEFO/LEFO, ICIA app, label generation) are kept product-specific and C-layer.
2. **Certification machinery depth in Agreo** not directly observed (its site names "official control services" as users but does not document tag/certificate features). Certification machinery stays L2 on the strength of ERP for Seed / Folio3 / agency-side sources.
3. **Cropin's processing depth** (conditioning plant orders) is less explicit than Agreo/ERP for Seed; Cropin may be deployed alongside an ERP for the industrial layer (the case study explicitly integrates an ERP). Noted as deployment variant.
4. **Whether grower self-service portals are standard** — not directly observed in any sampled product's documentation (agency-side portals exist; company-side grower portals not evidenced). Kept out of L1; flagged as possible emerging pattern.
5. **Generation-class vocabulary varies** by jurisdiction (AOSCA classes vs OECD schemes vs internal schemes); the canonical concept (generation of seed stock with lineage) is well-evidenced, the specific labels are not universal.

## Final Synthesis

A Seed Production Management application is the seed-producing organization's multiplication system of record. Its defining core is three jointly-held structures: **the seed lot as unit of record** (a persistent identified quantity of a named variety, carrying generation/class, lineage, quality record, and lifecycle from production through conditioning/testing to disposition); **variety-anchored multiplication planning over contracted production** (which variety × which generation of parent seed × which grower's fields, under production contracts with siting constraints); and **identity-and-quality gatekeeping to lot release** (field inspections and lab tests recorded against field/lot, results gating progression to packaging/sale and fixing the lot's class/label, with identity and quality traveling with the lot). The binding is seed-multiplication semantics: the managed product is planting seed whose value is varietal identity and genetic purity. Everything else — grower settlements, conditioning orders, lab management, demand planning, sales/distribution, certification paperwork, breeding modules, AI — is common, variant, or vendor-specific structure layered on that spine.
