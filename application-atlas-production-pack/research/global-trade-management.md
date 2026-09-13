# Research Notes — Global Trade Management

Research date: **2026-09-07**

## Research Goal

Understand what a Global Trade Management (GTM) application is as a software type: what objects exist inside it, what its users do, how trade transactions flow through it, which rules gate the work, and where its boundary lies against Transportation Management Systems, customs-filing tools, sanctions-screening platforms, and ERP.

## Initial Boundary

Temporary hypothesis before research:

- Core use: managing the regulatory-compliance and fiscal side of physically moving goods across national borders (import and export) — classification, screening, licensing, duties, customs declarations, trade agreements.
- Users: trade compliance officers, customs managers, export-control specialists, trade/logistics operations at importers/exporters; also customs brokers.
- Nearest types: Transportation Management System / TMS (shares shipments), Customs Compliance Platform (directory sibling leaf — declaration filing slice), Sanctions Screening Platform (financial-domain screening), ERP / Order Management (owns the orders), Freight Forwarding System (forwarder-side operations), Supply Chain Planning (consumes landed cost).
- Likely boundary: TMS = carriage (rates, carriers, execution); GTM = the border (whether goods may cross, what they owe, what customs requires).
- Unknowns: whether customs declaration filing is natively in-product or commonly broker-handled; how screening is wired into order/shipment flows; whether duty-program management (FTZ/bonded/drawback) is universal; market split between ERP-embedded and standalone GTM.

## Research Questions

1. What is the unit of record — shipment, order, transaction, or declaration?
2. What master data does the type maintain (classifications, origins, parties, licenses, programs)?
3. How does the compliance gate work at transaction time (screening → controls → license → hold/clear)?
4. How are customs declarations built, and is filing self-executed or broker-handled?
5. How do duty reduction programs (FTA, FTZ, bonded, drawback) work as software structures?
6. Where does landed cost live, and what does it feed?
7. What regulatory content does the vendor supply vs the customer maintain?
8. Who are the users, and what interfaces do they face (queues, workbenches, portals, dashboards)?
9. Where does GTM end and TMS / customs-filing / sanctions-screening / ERP begin?
10. Do older, regional, or broker-side products still fit the definition?

## Representative Products

| Product | Pole | Evidence tier reached |
|---|---|---|
| Oracle Global Trade Management (Oracle Fusion Cloud Transportation & Global Trade Management) | SCM-suite-embedded GTM; transportation+trade pair | Tier-1 docs (get-started, integration playbook "About" page) + Tier-2 product page with 5 capability areas + product tour |
| E2open Global Trade Application Suite (Amber Road / Integration Point heritage) | Standalone trade-first SaaS suite with content database | Tier-2 product pages (suite, Export Management, Duty Management) |
| Descartes (Global Trade Intelligence + Customs & Regulatory Compliance families; Visual Compliance) | Content/screening/classification layer + country-specific declarations; strong broker-side footprint | Tier-2 product pages (customs declarations, solution catalog) |
| SAP Global Trade Services (SAP GTS) | ERP-embedded pole, category heavyweight | Not directly reachable this pass (see Source-access Limitation); category membership evidenced by Descartes's official cross-reference ("content for SAP-GTS, Oracle GTM & other systems") |

Selection rationale: two enterprise suite-embedded poles (Oracle; SAP as unreachable anchor), one trade-first SaaS suite (E2open), one content/declaration specialist with a broker-side variant (Descartes). Different philosophies: suite-native integration vs content-database differentiation vs federated country-specific filing.

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

- Oracle — Global Trade Management product page: https://www.oracle.com/scm/logistics/global-trade-management/
- Oracle — "About Oracle Fusion Cloud Transportation and Global Trade Management" (Integration Playbooks for SCM): https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/26b/faips/otm-about-oracle-fusion-cloud-transportation-and-global-trade-management.html
- Oracle — Transportation and Global Trade Management Cloud 26C Get Started: https://docs.oracle.com/pls/topic/lookup?ctx=otm-latest&id=otm-gs
- E2open — Global Trade Management suite: https://www.e2open.com/global-trade/
- E2open — Export Management: https://www.e2open.com/global-trade/export-management/
- E2open — Duty Management: https://www.e2open.com/global-trade/duty-management/
- Descartes — Customs Declarations: https://www.descartes.com/solutions/customs-and-regulatory-compliance/customs-declarations
- Descartes — solution catalog / Global Trade Intelligence menu: https://www.descartes.com/
- SAP — Help Portal entry for SAP Global Trade Services: https://help.sap.com/docs/SAP_GLOBAL_TRADE_SERVICES (JS-gated shell only)

Failed/abandoned (per source-access rules, 1–2 attempts each, then degraded):

- docs.oracle.com direct book paths for the GTM implementation guide (404 ×2) — compensated by fetchable integration-playbook "About" page and the public product page.
- SAP product-page URLs (404 ×3), SAP Help Portal (JS shell), SAP Community (403) — SAP evidence downgraded to cross-reference + market context only.
- DuckDuckGo search (timeout ×2) — abandoned; Bing returned non-targeted localized results.

## Product A — Oracle Global Trade Management

### Key observations (evidence layer A unless noted)

Positioning: "Centrally manage business processes related to cross-border trade with Oracle's global compliance solution… visibility and control over orders and shipments and ensure adherence to tariffs and trade regulations." Paired with OTM in one cloud: "Oracle Transportation Management and Global Trade Management are a global transportation and logistics operations system and a unique global compliance solution… to centrally manage their global trade operations."

Five official capability areas on the product page:

1. **Tariff Management** — screen for tariff savings opportunities; identify trade agreements / customs programs, compare savings, assign programs for future imports; manage trade incentive programs (drawback, bonded warehouses, foreign trade zones, inward/outward processing, regional programs); estimate total landed costs (transportation, handling fees, insurance, duties, taxes).
2. **Trade Compliance** — centralize regulatory compliance; screen transactions for restricted parties, sanctions, embargos; classify goods (tariff and export control classifications, import and export); manage export licenses and import permits (model, assign, track usage "to help expedite the processing and release of shipments").
3. **Customs Management** — build customs declarations from invoice and shipment data "automatically enriching it with available global trade master data"; create and track customs documents; collaborate with forwarders, customers, brokers, customs authorities.
4. **Trade Agreements** — supplier solicitation campaigns for information/documents; track certificates of origin; qualify shipments for FTAs by analyzing bills of material.
5. **Global Trade Analytics** — configurable dashboards; metrics vs targets/benchmarks/forecasts; navigate between historical and operational information.

Product tour details:

- Classification "under standard regulatory classification regimes, such as the Harmonized Tariff System, export control lists, and munitions lists" — "helps ensure the correct licenses are applied, documents produced, and duties paid downstream."
- Country of origin management "for all the goods that you purchase or manufacture" with support for complex multisource supply chains.
- Landed cost simulator: "Calculate an estimated landed cost for multiple scenarios simultaneously."
- Restricted party and sanction screening on "both your party master data and all your business transactions."
- "Oracle's partners provide refreshed regulatory content daily" (vendor claim).
- Gate behavior: "Automatically place transactions such as sales orders, purchase orders, and shipments on hold when regulatory controls are applicable. Manage by exception to help ensure that restricted goods aren't imported or exported without a license, permit, or other required documentation."
- Document workflow: preview/manage revisions before finalizing for distribution; archive locally or into corporate content management.
- Declarations: "expedite the process of building and managing your pre-entry broker data or customs filings"; "designed to support customs processes globally… prepare your customs filings or the data required for your brokers."
- Named customers in video/marketing blocks: Hologic, Crane Aerospace, World Wide Technology.

## Product B — E2open Global Trade Application Suite

### Key observations (evidence layer A; customer testimonials = layer B-weak, treated as claims)

Suite framing: "Export and import with confidence… leverage trade agreements and duty savings programs… including customs declaration self-filing capabilities… backed by the world's most comprehensive and current trade content database."

Six named applications (all Tier-2 product pages):

1. **Due Diligence Screening** — screen customers, suppliers, and other partners against worldwide denied party lists.
2. **Export Management** — automate export compliance: country controls, restricted party screening, license determination and tracking, document generation. Detail: classification "according to the latest Harmonized System (HS) codes and export control numbers (ECNs)"; screening against "over 900 restricted party and sanctions lists" (vendor claim); "thousands of country-specific regulations"; license determination tells the user what license/documents are needed; "license usage, exemptions, end-user statements, critical trade documents… tracked and stored."
3. **Import Management** — complete documentation for inbound shipments; collaboration with suppliers, brokers, carriers, freight forwarders.
4. **Duty Management** — FTA qualification and duty programs: "identifying relevant duty, tax, and tariff reduction programs"; importer "must solicit product information from supply chain partners and determine which products conform to the rules of origin for each trade agreement"; customs warehouses and FTZs "help importers defer or reclaim their duty payments"; "the system analyzes data down to the last component to find its origin, then identifies transactions eligible for duty savings"; "automatically reconciles inventory movements such as receipts, goods issues, and adjustments against requirements for duty-reduction programs such as FTZs"; drawback named.
5. **Customs Filing** — self-filing with customs agencies; "access to detailed country-specific compliance rules"; reduce broker fees.
6. **Global Knowledge** — content database: "regulatory controls, restricted parties, classifications, and landed costs."

Landed-cost solution brief framing: many companies price only on production cost, "missing critical elements like duties, tariffs, taxes, and transportation fees."

Compliance video description: "automating all compliance functions, performing restricted party screenings, determining license requirements, generating shipping documents and creating an audit trail."

Customer testimonials (marketing claims, layer B-weak): Renault (FTA exploitation), Signify ("from classification and RPS screening to qualifying for free trade agreements… see in advance where we avoid import duties"), Sandvik (centralized export control), Sophos ("automated workflow that approves cases in under a minute, filters out low-risk transactions… every shipment and download complies with global export and sanctions laws… processing around 1,000 orders a week"), Allied Electronics (export compliance automation). UFLPA/forced-labor traceability solution brief exists (adjacent extension).

## Product C — Descartes

### Key observations (evidence layer A; scale figures = vendor claims)

Descartes does not sell one monolithic "GTM suite"; it spans the GTM scope through two solution families plus content:

- **Customs & Regulatory Compliance**: Customs Declarations ("comply with fiscal filing requirements"), Security Filings ("submit advanced manifest data electronically to customs authorities worldwide"; EU ICS2 mentioned), Other Government/Industry Programs, Foreign Trade Zone Management.
- **Global Trade Intelligence**: Product Classification ("integrate classification and duty determination with your business systems"), Duty and Tariff Data ("accurately classify by HTS and tariff codes and calculate landed costs"), Export Classification ("classify against U.S., EU, UK, and other export control lists"), Export License Management (via Visual Compliance), Denied Party Screening ("automate screening processes and integrate with your business systems"), Trade Compliance Content for Business Systems ("content for SAP-GTS, Oracle GTM & other systems"), Global trade data / market intelligence.
- **Customs Declarations page specifics**: country-specific declaration solutions (US: "manage customs entries to U.S. CBP and other U.S. government agencies"; Canada: CBSA submissions; UK e-Customs; Netherlands/Belgium/Sweden/Denmark/Norway/Luxembourg/Ireland). Feature bullets: integrate with internal systems; real-time global customs status visibility; automated data validation; "reduce the risk of trading with unauthorized entities"; capture via manual entry or EDI; "smart automations and prompts to ensure all data is collected."
- Scale claims (vendor-published): 100M+ compliance filings/year; 700M+ restricted party screenings/year.
- Customer base skews to customs brokers/forwarders (Kuehne Nagel, DSV, Expeditors, Kintetsu, Hellmann logos; testimonials from a customs brokerage CFO and a bureau-services head — "manually handling thousands of entries monthly").
- Cross-reference evidence: official menu item "Leverage industry-leading content for SAP-GTS, Oracle GTM & other systems" — establishes that classification/screening/content is a separable market layer consumed by GTM suites, and that SAP GTS and Oracle GTM are recognized members of the category.

## Cross-product Comparison

| Dimension | Oracle GTM | E2open | Descartes |
|---|---|---|---|
| Cross-border transaction as unit evaluated/recorded | Yes (orders, POs, shipments held/managed) | Yes (every export/import transaction screened; case workflow) | Yes (entries/declarations per country; shipments in forwarder stack) |
| Product classification (tariff + export control lists) | Yes (HTS, export control lists, munitions lists) | Yes (HS codes + ECNs) | Yes (HTS/tariff codes; US/EU/UK export lists) |
| Restricted party / sanctions screening | Yes (master data + transactions) | Yes (denied party lists; partner due diligence; 900+ lists claim) | Yes (700M screenings/yr claim; integrates into business systems) |
| License/permit determination and tracking | Yes (model, assign, track usage) | Yes (determination + tracking, exemptions, end-user statements) | Yes (export license manager) |
| Customs declarations built/managed | Yes (from invoice+shipment data, enriched w/ master data; pre-entry broker data or self-file) | Yes (self-filing app; country-specific rules) | Yes (country-specific filing family: CBP, CBSA, UK, EU) |
| Duty/tax/origin determination + landed cost | Yes (landed cost simulator; duties paid "downstream") | Yes (landed cost incl. duties/tariffs/taxes/transport) | Yes (duty determination + landed cost data) |
| FTA qualification / origin programs | Yes (BOM analysis, supplier campaigns, certificates of origin) | Yes (rules-of-origin qualification, component-level analysis, supplier solicitation) | Partial (classification + duty/tariff data; FTA-qualification workflow not directly observed) |
| Duty deferral/refund programs (FTZ, bonded, drawback) | Yes (named in Tariff Management) | Yes (FTZ/customs warehousing/drawback + inventory reconciliation) | Yes (FTZ management product; bonded warehouse ops) |
| Trade document generation/management | Yes (revision workflow, archive) | Yes (document generation, central document management) | Yes (declaration documents; data capture EDI/manual) |
| Regulatory content as a product layer | Yes (partner-refreshed content, daily claim) | Yes (Global Knowledge database) | Yes (sells content itself, incl. into SAP GTS/Oracle GTM) |
| Audit trail / compliance records | Implicit (compliance centralization) | Explicit ("creating an audit trail") | Implicit (filing records; status visibility) |
| Collaboration with brokers/forwarders/customers/suppliers | Yes | Yes (portal) | Yes (broker-side operation is its home turf) |
| Analytics/reporting | Yes (Global Trade Intelligence) | Yes (trade-flow analytics; program reporting) | Partial (shipment portal analytics; BI for trade data) |
| Hold/gate on transactions | Explicit (hold sales orders, POs, shipments) | Implied by case workflow (auto-approve low risk, review rest) | Not directly observed (broker filing context) |
| Native transportation execution | Sibling product (OTM, one cloud) | Sibling suite (Logistics) | Sibling families (Forwarder TMS/shipment management) — separate |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being a GTM:

```text
Product trade master (classification)
└── bound to a cross-border trade transaction (import and/or export movement of goods)
    └── transaction-level regulatory compliance determination
        (restricted party screening · sanctions/embargo controls · license/permit determination
         → outcome recorded on the transaction: clear / hold-for-review / licensed / blocked)
    └── customs-facing output
        (declarations & trade documents for customs authorities,
         underpinned by classification, origin and valuation determination;
         duties/taxes where import processes are in scope)
```

Four properties:

1. **Cross-border trade transaction as the unit of record** — an import and/or export movement of goods between parties in different customs territories is what the system evaluates and records. Remove it → trade content database / tariff research tool.
2. **Product classification against tariff/trade-control catalogs** — each good is bound (by HS-family tariff codes and export control classifications) to the regulations that apply to it. Remove it → shipment management (TMS) with documents.
3. **Transaction-level compliance determination** — screening of parties, sanctions/embargo checks, and license determination producing a recorded outcome on the transaction. Remove it → customs declaration/filing tool (the sibling Customs Compliance Platform slice).
4. **Customs-facing output** — declarations/documents prepared for or filed with customs authorities, resting on classification/origin/valuation determinations (duties/taxes on the import side). Remove it → an export-control screening service.

Historical/§24 check: a 1990s single-country export compliance tool (RPS screening + export documentation + EEI-type filing) satisfies the four invariants — classification, screening, determination, customs-facing output all present; duty calculation genuinely minimal on export side, which is why duty/landed-cost is written as in-scope "where import processes are in scope" rather than invariant. A broker-side country declaration tool satisfies 1, 2, 4 but not 3 — evidence it belongs to the customs-filing slice, not full GTM. A financial-transaction sanctions screener has screening but none of 1/2/4 — different type. The invariant set holds across old, regional, and broker-side products.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- duty/tax/landed-cost determination and simulation (3/3)
- trade document generation/management with distribution to partners (3/3)
- FTA qualification and origin management (BOM analysis, supplier solicitation, certificates of origin; 2/3 directly, 1/3 partial)
- duty deferral/refund program management (FTZ, bonded/customs warehousing, drawback) incl. program inventory reconciliation (3/3, different depths)
- regulatory trade content as a supplied, continuously updated layer (3/3)
- audit trail / retained compliance records (1/3 explicit; universal in practice — moderate wording)
- collaboration surfaces: broker/forwarder/customs authority/supplier portals (3/3)
- analytics/dashboards on trade flows, duty savings, compliance status (3/3)
- integration fabric: ERP/order/TMS/WMS event feeds; declarations assembled from invoice+shipment+master data (3/3)
- exception management of screening hits (false-positive resolution) (2/3 explicit)

### L2 — Variant / Optional Structure

- deployment posture: ERP-embedded (SAP pole) / SCM-suite sibling (Oracle) / standalone SaaS suite (E2open) / federated content+point solutions (Descartes)
- filing posture: self-filing vs pre-entry broker handoff vs broker-side filing operation (Descartes's broker customers)
- trade-side emphasis: export-control-centric (high-tech/defense) vs import-duty-centric (retail/apparel) vs balanced
- geographic depth: per-country declaration families (US CBP + PGA agencies, Canada CBSA, UK CDS, EU member states), security filings (ICS2-type advanced manifest)
- program specialization: FTZ/bonded warehouse operation software as a standalone; drawback-specific tooling
- adjacent extensions: global e-invoicing mandates, forced-labor/UFLPA traceability, trade-data market intelligence (import/export statistics), AI assistance for screening false-positive reduction and classification
- segment tuning: enterprise centralization programs vs mid-market packaged deployments vs bureau services for brokers

### L3 — Vendor-specific (research notes only)

- Oracle: five-pillar naming (Tariff Management / Trade Compliance / Customs Management / Trade Agreements / Global Trade Analytics); landed cost simulator "multiple scenarios simultaneously"; daily partner content refresh claim; OTM+GTM one-cloud bundling; AES X12 601 mapping file in My Oracle Support (US EEI filing artifact); customers Hologic/Crane Aerospace/WWT.
- E2open: app names (Due Diligence Screening, Export/Import Management, Duty Management, Customs Filing, Global Knowledge); "900+ lists", "225+ countries", "$40M annual duty savings" claims; Harmony UX; bond-brief for a Japanese automotive maker's EU bonded warehouses; e2net partner network; Sophos ~1,000 orders/week claim; now owned by WiseTech Global (press release observed).
- Descartes: Visual Compliance brand; QuestaWeb FTZ software; 100M filings/700M screenings per year claims; AI Assist "reduce screening false positives by 60%" claim; per-country microsites; broker logo wall (KN, DSV, Expeditors, KWE, Hellmann).
- SAP GTS: not directly observed this pass; market-known module triad (compliance/customs/risk management) deliberately NOT asserted in the final document.

## Vendor-specific Findings

See L3. Additionally: only Oracle documents the explicit hold-on-transaction rule in directly observed official prose; E2open's gate behavior is evidenced by a customer testimonial describing an automated case workflow with low-risk auto-filtering — moderate wording in the final document. Descartes demonstrates that classification/screening/content and country declarations can be bought as separable products — the GTM suite bundles them, but the market also un-bundles them.

## Boundary Findings

- **vs Transportation Management System / TMS**: shares orders/shipments; TMS plans and executes carriage (rates, carriers, routing, tracking); GTM determines whether goods may legally cross, what they owe, and what customs requires. Oracle ships both as one cloud; E2open bundles both as sibling suites; Descartes keeps them in separate families. Test: remove rate/carrier/execution → still GTM; remove classification/screening/customs → TMS.
- **vs Customs Compliance Platform (directory sibling leaf, §10, unprocessed)**: the declaration/filing-first slice, often country-specific and often broker-operated. GTM = that slice PLUS transaction-level export/import compliance determination (screening/licensing), FTA/origin programs, duty program management, landed cost. Sharpest seam: does the product determine and record the compliance outcome of the transaction (license/hold/clear), or only prepare/fill declarations? Flag for joint review in STATUS.
- **vs Sanctions Screening Platform (financial, §08)**: same list-technology genre; different domain object — financial transactions/payments/customer onboarding vs physical goods trade transactions; GTM screening is a step inside the trade flow attached to licensing determination.
- **vs Freight Forwarding System**: forwarder-side operational system (bookings, consolidation, documents, per-shipment ops). Descartes shows brokers/forwarders operating declaration software for clients — that is the customs-filing slice deployed broker-side, not the importer-side GTM program.
- **vs ERP / Order Management / Procurement**: ERP owns orders/POs/invoices; GTM consumes them as the transaction stream to be screened/determined, and returns holds, documents, duties, and classifications. GTM holds the trade master (classifications, origins) that ERP items typically reference.
- **vs Supply Chain Planning**: planning may consume landed-cost estimates; it performs no regulatory determination and produces no customs output.
- **What would collapse the type**: strip customs/licensing/origin machinery from GTM → TMS + ERP. Strip the cross-border transaction and keep content → tariff/trade content database. Strip customs-facing output and keep screening → export-control screening service.

## Uncertainties

1. SAP GTS internals not directly observed this pass; the ERP-embedded pole is evidenced structurally (Descartes cross-reference + category membership) but no SAP-specific claim is made in the final document.
2. Exact jurisdiction/coverage counts (lists, countries, filings/year) are vendor claims, not independently verified; excluded from the final document except as marked claims.
3. Whether FTA qualification workflow exists in Descartes's own GTM-intelligence products was not confirmed (only classification + duty data observed) — treated as partial.
4. Hold-on-transaction behavior verified directly at Oracle only; E2open evidenced at testimonial strength; not asserted as universal in the final document.
5. The precise boundary between "Global Trade Management" and "Customs Compliance Platform" as the directory separates them needs a joint-review pass when the sibling leaf is processed.

## Final Synthesis

A Global Trade Management application is an importer/exporter-side operational system of record for the compliance and fiscal machinery of cross-border goods trade. Its defining core is a four-part chain: products classified against tariff and trade-control catalogs; those products bound into cross-border trade transactions; every transaction run through a recorded regulatory compliance determination (restricted party screening, sanctions/embargo controls, license/permit determination) that can hold, clear, license, or block it; and the production of customs-facing declarations and trade documents resting on classification, origin, and valuation determinations (duties/taxes where imports are in scope). Around that core, mature products add duty/landed-cost determination, FTA and duty-program management, vendor-supplied regulatory content, document management, partner/broker collaboration, audit records, and analytics. The type is implemented as ERP-embedded modules, SCM-suite siblings, standalone SaaS suites, and — in the same market — as un-bundled content, screening, and country-declaration products; the customs-declaration-first slice is the seam toward the sibling Customs Compliance Platform type, and carriage execution is the seam toward TMS.
