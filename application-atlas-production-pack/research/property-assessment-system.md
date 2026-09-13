# Research Notes — Property Assessment System

## Research Goal

Understand, from real products, what a Property Assessment System (the government-side property valuation system, commonly called CAMA — Computer-Assisted Mass Appraisal — plus assessment administration) actually is: its unit of record, its valuation machinery, its official deliverable (the assessment roll), its annual operating loop, its users and interfaces, and its boundaries against the neighboring §24 Types (Land Records / Cadastre, Property Tax Administration, Government GIS) and against §17 property Types.

## Initial Boundary

- The leaf sits in §24 Government, Public Sector & Civic, between "Land Records / Cadastre System" and "Property Tax Administration".
- Prior pass (land-records-cadastre-system, 2026-09-08) recorded a joint-review flag: "one parcel spine, three operations — rights-of-record (land records) vs valuation (assessment) vs billing/collection (tax)"; this pass must discharge that flag from the assessment side.
- Initial hypothesis: the Type is the jurisdiction's system of record for property VALUES (mass appraisal + roll), not for rights (land records) or money (tax billing).
- Likely confusions: real-estate AVM/valuation services (market-facing), building condition assessment (physical surveys), property listing platforms (market transactions), government GIS (parcel geometry).

## Research Questions

1. What is the unit of record — parcel, account, roll line? How do ownership, characteristics, and values attach to it?
2. What does "mass appraisal" mean operationally in products (approaches to value, model calibration, valuation runs, valuation dates)?
3. What is the assessment roll and what lifecycle does it have (preliminary → notices → certification → corrections)?
4. How do appeals/abatements/corrections work and how do they change the roll?
5. What flows in (deeds/ownership, sales, permits, field inspections, GIS) and out (tax billing, state reports/equalization, public portals)?
6. What interfaces do staff and the public face?
7. What roles exist (appraiser, data collector, assessment administrator, board, taxpayer)?
8. Where exactly are the boundaries with land records, tax administration, GIS, and market-facing valuation?

## Representative Products

Selected for market coverage, documentation accessibility, and different postures:

1. **Aumentum Technologies — Aumentum Valuation** (aumentumtech.com) — large multi-state suite vendor (ex-Thomson Reuters Aumentum); CAMA + assessment administration + tax collection + public access as separate product lines; "1,000 governments across 39 states, 35M parcels".
2. **DEVNET — Edge CAMA & Assessment Administration** (devnetinc.com) — integrated land-records suite vendor (CAMA + assessment administration + billing & collection + permitting + GIS + public portal); explicitly built to IAAO/USPAP standards.
3. **Vision Government Solutions — Vision 8 CAMA** (vgsi.com) — services+software hybrid: mass-appraisal/revaluation services + CAMA platform + per-state public online databases + taxpayer appointment scheduling; New England municipal base.
4. **Catalis — CAMA (Patriot Properties lineage)** (catalisgov.com) — CAMA + tax roll processing vendor across North America (US + Canada); multi-year database; SaaS and on-premises; per-jurisdiction public lookup portals.

Market anchor NOT sampled: Tyler Technologies (Eagle/iasWorld) — tylertech.com returned HTTP 403 on two attempts; Vanguard Appraisals — transport error on two attempts. No claims about them are made beyond "exists as a major vendor" (recorded as limitation).

Professional-body anchor: IAAO (International Association of Assessing Officers) — General Assessment FAQs and Glossary for Property Appraisal and Assessment (3rd ed. 2022; PDF too large to fetch, page-level evidence only).

## Sources

Fetched 2026-09-09 (all Tier 1 — official vendor/product pages unless noted):

- Aumentum Technologies — homepage: https://www.aumentumtech.com/ ; Aumentum Valuation: https://www.aumentumtech.com/property-valuation ; Aumentum Public Access: https://www.aumentumtech.com/aumentum-public-access
- DEVNET — homepage: https://www.devnetinc.com/ ; CAMA & Assessment Administration: https://www.devnetinc.com/cama-assessment-administration/
- Vision Government Solutions — homepage: https://www.vgsi.com/ ; Vision 8 CAMA: https://www.vgsi.com/vision-8-cama/ ; Taxpayer Info / Online Databases: https://www.vgsi.com/taxpayer-info/
- Catalis (Patriot) — CAMA product page: https://catalisgov.com/tax-cama/computer-assisted-mass-appraisal-cama/ ; Tax & CAMA family: https://catalisgov.com/tax-cama/ ; public jurisdiction portals: https://jurisdictions.patriotproperties.com/patriotproperties.html
- IAAO — General Assessment FAQs: https://www.iaao.org/industry-data/general-assessment-faqs/ ; Glossary page: https://www.iaao.org/publications-list/glossary/ ; homepage/designations: https://www.iaao.org/
- Prior-pass context: applications/land-records-cadastre-system.md, applications/government-gis.md (Related Types sections)

Unreachable (recorded per source-access limitation): tylertech.com (403 ×2), vanguardappraisals.com (transport error ×2), IAAO glossary PDF (>5MB).

## Product A — Aumentum Valuation (Aumentum Technologies)

### Key observations (evidence layer A unless noted)

- Self-description: "Aumentum Valuation is our fully integrated CAMA (Computer Assisted Mass Appraisal) and Assessment solution… tools, sketching, and workflow technologies to assist the Appraiser in completing equitable valuations."
- Valuation: "powerful point-in-time appraisal capabilities with versioned property data, sales tracking, user-configurable property characteristics, and advanced valuation tools that support cost, market, and income approaches to value."
- Scale claim: "complete a comprehensive valuation on properties either in mass, or individually on a case-by-case basis" (Real Property Valuation component).
- Records component: "the foundation of every Aumentum install… a comprehensive database repository of properties and parties with an interest in the jurisdictions' properties… track what property and people exist, the characteristics of the two, and the relationship between them."
- Assessment Administration component: "handles the application of property assessment rules… manages and applies all rules related to deriving taxable values including applicable exemptions, value capping, preferential assessments and penalties… handles and calculates revised values affected by corrections while maintaining value history… applied to Assessments for each individual account used to generate assessment notices and assessment rolls."
- Appeals: Case Management "customize and manage their Appeals business process from start to finish… ranging from simple Assessor only integrations with local boards providing visibility on appeals, to full appeals management including automated calendar scheduling and evidence packet creation."
- Sketch: "fully integrated, industry-leading sketch tool with the ability to sketch all improvements… automatically calculates the square footage of each component and updates the database… multiple structures per record."
- Personal property: separate module — "track business assets… the public to update information, file online… Rapid Asset Entry for mailed filings."
- Field/mobile: "Log and update property characteristics from field locations, using the same configurable business rules you use at the office." Pictometry/Eagleview oblique imagery to "reduce time and money spent on field inspections."
- GIS: "Aumentum GeoAnalyst integrates with Esri's ArcGIS Server… spatial tools to visualize parcel data."
- Suite integration: "Property values automatically flow throughout the system… a single system of record across departments" (valuation ↔ tax ↔ public access).
- Public Access (separate product): "citizens and businesses can securely access property, tax, and assessment information anytime… view records, search property data, download reports, submit forms, upload supporting documents, and complete key transactions"; eForms with "pre-filled account information, validation rules… document uploads"; GIS "comparable searches of neighboring properties… locate properties in the context of valuation and assessment."
- Key-capabilities list: AI-Powered Data Automation & Valuation; Integrated Sketch & Spatial Tools; Modular Valuation Engines; Sales Tracking & Versioned Property Data; Custom Forms & Correspondence; Appeals & Case Management; Third-Party Integrations; Configurable Workflows & Business Rules; Secure, Web-Based Deployment Options.

## Product B — DEVNET Edge CAMA & Assessment Administration

### Key observations

- Framing: "Developed based on IAAO and USPAP industry standards, the DEVNET Edge CAMA and Assessment Administration solutions automate the appraisal and assessment administration functions, allowing for accurate valuation and complete parcel maintenance, assessment, exemption and appeals information." Suite framing: "the entire property tax life cycle from appraisal to collection."
- CAMA features:
  - "Cost, Market and Income Approaches to value for land and buildings"
  - Cost approach: "multiple building cost options including Marshall & Swift, state specific cost manuals and other user-defined cost tables"
  - Analytics: "sales ratio studies, land and building studies, statistical graphing, multiple regression"
  - "Feature rich comparable property search"
  - Income approach: "Gross Potential Income, Net Operating Income, Gross Rent Multiplier, Cap Rate"
  - "Generation of final property values by parcel using cost, sales comparison and income approaches for commercial and industrial properties"
  - "Land valuation by neighborhood or subdivision using base lot, front foot, acreage, or square foot models"
  - "Study builder and equation builder options… customized income approach"
  - APEX Sketch integration; "Integrated digital photography and document scanning"
  - "Seamless land records integration eliminates sales data entry redundancy"
  - Field: "TabletPCs or other hand-held field devices… user-checkout and real-time wireless connectivity… GPS, laser measuring tools"
  - "Electronic PRC customizable for each jurisdiction" (PRC = property record card)
- Assessment Administration features:
  - "complete parcel maintenance, assessment, exemption and Board of Review information"
  - "Parcel tracking by year for complete history of a parcel including its genealogy"
  - "Multiple site addresses per parcel in E911 address format"; legal descriptions free-form or structured
  - "All state required abstracts and reports"
  - "Comprehensive parcel split and combination processes"
  - "Easy integration with 3rd party GIS and CAMA systems"
  - "Exempt property tracking"; "Abatements processing"
  - "Building permit features… track date, dollar value of the permit, contractor occupancy date"
  - "Automated generation and printing of user editable notices (change of assessment notices, etc.)"
- Board of Review, Revision, Equalization, Appeals module:
  - "Docket creation, allowing single or multiple PINS to be attached"
  - Taxpayer-requested value entry; notice queue thresholds (vendor-specific detail: >$100k)
  - "values entered as proposed value changes or final decisions from within the module automatically update the assessment maintenance records… easy data entry of a correction record"
  - "proposed value change notices and/or final decision notices"
  - "hearing scheduling utilizing an electronic calendar… single or multiple hearing rooms"
- Personal Property module: "Individual and business personal property assessments… bar-coded personal property listings… valuation and calculation… abstracts and state required reports… return dates by hand entry, bar coding or OCR… copy prior year… revaluate at current year rates… correction processing… assessment history and waivers… user defined depreciation, trending and condition schedules… mass valuations for personal property… in on-screen, real time mode."
- GIS: EdgeMaps — "real-time GIS integration with authoritative CAMA and Tax Data. Powered by Esri's ArcGIS Platform… web maps live in DEVNET software."
- Public portal: wEDGE — "connects the public, outside agencies and partners to real time Land Record Information. Access property data, appraisal information and take advantage of e-government activities such as property tax bill payment and e-file applications."

## Product C — Vision Government Solutions (Vision 8 CAMA)

### Key observations

- Posture: services + software hybrid. Site sections: Appraisal Services (revaluation services), Software Solutions (Vision 8 CAMA), Taxpayer Info (Online Databases, Taxpayer Reval FAQ, Online Scheduling).
- "VISION 8 CAMA — An Unparalleled CAMA Platform… Designed by assessors, for assessors." "Assessors and appraisers on our Customer Advisory Board custom-built Vision 8."
- "COMPLETELY CONFIGURABLE — Work the way you want with tremendous customization and flexibility."
- Valuation: "Vision 8 supports multiple approaches to value (cost, market, income, regression, condo value apportionment, trending, and more)."
- Reporting: "Vision 8's report writer provides out-of-the-box reports and customizable reports."
- Sketch: "Vision Sketch is specially tailored to reduce time burden on assessors and improve valuation accuracy."
- Public surface: per-state "Online Databases" (CT, ME, MA, MN, NH, PA, RI, VT, VA) — public property/assessment lookup portals operated per jurisdiction; "Taxpayer Reval FAQ" explains revaluation to taxpayers; "Online Scheduling" lets taxpayers book appointments (informal hearings/values discussions during revaluation).
- Client testimonial references IAAO "Certificate of Excellence in Assessment Administration" (CEAA) as the goal the platform supports.

## Product D — Catalis CAMA (Patriot Properties lineage)

### Key observations

- Framing: "Catalis CAMA helps local governments modernize property assessment by unifying data management, valuation, and tax roll processing into a single, easy-to-use platform. Purpose-built for the public sector… streamlined tools for batch editing and advanced property type search."
- "Multi-Year Database — Maintain real estate and personal property data in a single database."
- "Analytical Tools — save data sets and conduct analyses using an advanced suite of analytical tools."
- "Integrated Sketching & Geospatial Tools — Graphically extend your CAMA software functionality with visual tools that support data accuracy."
- "Customizable Workflows — customized tracking, reporting, and notifications." "SaaS Solutions" (cloud) — client quote documents on-premises 2018 → cloud 2024 "without any disruption to our tax cycle."
- Client quote (Martin County FL): "valuation, mass appraisal, assessment administration, and tax roll processing, all within one application"; another: "appraisal, data entry, ownership tracking, and exemption processing."
- Family (Tax & CAMA): Billing & Collections, Escrow Payment Management, CAMA, Assessment E-file, GIS & Sketching Technology, Mass Appraisal Services, Property Tax Oversight.
- Public surface: "select your city or County" → per-jurisdiction public lookup portals (jurisdictions.patriotproperties.com).
- North America scope (US + Canada offices; Canadian flag in nav).

## Cross-product Comparison

| Aspect | Aumentum Valuation | DEVNET Edge CAMA | Vision 8 CAMA | Catalis CAMA |
|---|---|---|---|---|
| Self-description | "fully integrated CAMA and Assessment solution" | "automate the appraisal and assessment administration functions" | "CAMA Platform… by assessors, for assessors" | "unifying data management, valuation, and tax roll processing" |
| Unit of record | parcel/account; Records = "repository of properties and parties"; versioned property data | parcel tracked by year, with genealogy; split/combination | parcel (assessing community) | multi-year database; real estate + personal property |
| Valuation approaches | cost, market, income; "in mass, or individually" | cost, market, income; regression; ratio studies; land models by neighborhood | cost, market, income, regression, condo apportionment, trending | analytical tools over saved data sets |
| Valuation calibration inputs | sales tracking; versioned data | sales ratio studies, multiple regression, cost manuals (Marshall & Swift, state) | regression, trending | data sets + analytics |
| Assessment administration | exemptions, value capping, preferential assessments, penalties; corrections with value history; notices; assessment rolls | exemption tracking, abatements, state abstracts, change-of-assessment notices | via platform + services | exemption processing, tax roll processing |
| Appeals | Case Management end-to-end; boards; calendars; evidence packets | Board of Review module: dockets, hearings, decisions write back to values | taxpayer appointment scheduling (informal pole) | workflows/notifications |
| Sketch | integrated; auto square footage | APEX Sketch integration | Vision Sketch | integrated sketching |
| Field collection | mobile, same business rules as office | TabletPC, GPS, laser, wireless | (services perform field work) | data collection tooling |
| GIS | GeoAnalyst + Esri | EdgeMaps + Esri; "authoritative CAMA and Tax Data" on maps | (public databases) | GIS & sketching technology |
| Personal property | dedicated module + public filing | dedicated module (returns, depreciation, mass valuation) | not surfaced on page | same database as real estate |
| Public access | Public Access portal (search, records, eForms, payments) | wEDGE portal (data, appraisal info, e-file, payment) | per-state Online Databases + revaluation FAQ + scheduling | per-jurisdiction portals |
| Downstream hand-off | "values automatically flow" to tax | billing & collection product line | (services context) | billing & collections product line |
| Standards cited | — | IAAO, USPAP | IAAO CEAA (testimonial) | — |
| Deployment | web-based options | (suite, on-prem lineage) | (platform + services) | SaaS + on-premises documented |

### Stable commonalities (layer B — cross-product)

All four sampled products carry, in their own words:

1. a persistent parcel/property record with characteristics and parties (ownership/interests)
2. mass valuation under multiple standard approaches (cost, market/sales-comparison, income; regression/trending variants)
3. sales data as calibration/analysis input (sales tracking, ratio studies, comparables)
4. assessment administration: exemptions/classification rules deriving taxable value; notices; the roll
5. appeals machinery (dockets/cases, hearings, decisions writing back into values)
6. sketching of improvements with area calculation
7. field data collection
8. GIS integration (parcel map context)
9. a public-facing lookup surface (portal/online database)
10. reporting (state abstracts, roll totals, custom reports)
11. personal property as a second assessed class (3/4 surfaced on the fetched pages; Catalis states "real estate and personal property data in a single database")

### Canonical inference (layer C)

The Type is best understood as: **the jurisdiction's system of record for property value** — parcel-bound property records + mass-appraisal valuation machinery + the assessment roll as the official, dated, governed deliverable. "Assessment administration" (rules turning value into taxable value, notices, appeals) is the operational discipline the system automates; "CAMA" names the valuation machinery.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The parcel/account as the unit of record** — a persistent, individually identified property record in the jurisdiction's inventory, carrying its characteristics (land + improvements), the parties holding interests in it, and its value history. Remove → a valuation/consulting service or property CRM with no jurisdictional record.
2. **Mass appraisal valuation machinery** — systematic, model-based valuation of the jurisdiction's whole property population under standardized approaches to value (cost, market/sales comparison, income), calibrated against market data (sales), producing a value for every parcel as of a defined valuation date — not one-off appraisals. Remove → an appraisal office producing individual reports (or a market AVM).
3. **The assessment roll of record** — the authoritative, dated, per-parcel list of determined values (with exemption/classification adjustments deriving taxable value) that the jurisdiction publishes, notices from, and hands to taxation; changed only through governed processes (appeals, corrections, abatements). Remove → a valuation calculator with no official deliverable; the "assessment" in the Type name disappears.

Jointly-held load-bearing tests:
- 1 alone = property inventory / parcel CRM
- 2 without 1 = valuation model with nothing to value and no record
- 3 without 1+2 = an empty roll template
- 1+2 without 3 = appraisal tooling with no official deliverable
- 1+3 without 2 = a hand-maintained roll (the paper era — satisfies the definition, see historical check)
- 2+3 without 1 = values not bound to identified properties/parties

### L1 — Common Mature Structure (standard capabilities, not definitional)

- property characteristics management (user-configurable; land + improvement components; sketches with automatic area calculation; photos/imaging)
- sales tracking and market analysis (sales capture, comparable search, ratio studies, regression/statistical graphing, study/equation builders)
- valuation modeling depth (neighborhood/land models, cost manuals incl. commercial cost services, income schedules — GRM/cap-rate machinery)
- assessment-rule administration (exemptions, classification, value capping, preferential assessment, penalties → taxable value)
- assessment notices and correspondence (change-of-assessment notices, configurable letters/forms)
- appeals/case management (dockets, hearing scheduling, evidence packets, decisions writing back to values)
- parcel lifecycle events (splits, combinations, parcel genealogy, year-based tracking)
- personal property module (business asset returns, depreciation/trending schedules, mass valuation)
- field data collection (mobile/tablet, GPS, laser measurement, oblique imagery)
- GIS integration (parcel map context, spatial analysis, map-based comparables)
- public access portal (search, view assessment data, eForms/e-file, sometimes payments)
- reporting (state abstracts/reports, roll totals, report writers)
- workflow engines, multi-year/versioned data, configurable business rules

### L2 — Variant / Optional Structure

- assessed-class scope: real property only ↔ real + personal property
- suite posture: standalone CAMA ↔ CAMA + tax billing/collection ↔ full land-records suite (+ permitting, records, GIS portal)
- services+software hybrid (revaluation/mass-appraisal services beside the platform)
- deployment: on-premises ↔ SaaS/cloud (both documented; one client migrated on-prem→cloud mid-tax-cycle)
- regional rule machinery: state-specific cost manuals, state abstracts, assessment e-file, equalization/oversight reporting — jurisdiction-dependent
- taxpayer self-service depth: read-only lookup ↔ eForms/e-file ↔ online payments ↔ appointment scheduling
- AI assistance in valuation/data automation (single sampled vendor so far — product-specific until corroborated)

### L3 — Vendor-specific (research notes only)

- Aumentum: ProVal, customCAMA, T2, GeoAnalyst, Smart Sketch, Rapid Asset Entry; "1,000 governments / 39 states / 35M parcels / $120B" stats; Amplify user conference
- DEVNET: Edge suite naming, wEDGE portal, EdgeMaps, APEX Sketch bundling, electronic PRC, Board-of-Review notice-queue threshold (>$100k)
- Vision: Vision 8, Vision Sketch, per-state Online Databases, Appointment-Plus scheduling, Customer Advisory Board
- Catalis: Patriot lineage, jurisdictions.patriotproperties.com portals, Guided Tours, Escrow Payment Management, Property Tax Oversight line, Canadian market presence

## Vendor-specific Findings

See L3. None promoted to the canonical model. The only near-promotion candidate was AI valuation assistance (Aumentum) — held at L2/product-specific because only one sampled product documents it.

## Boundary Findings

1. **vs Land Records / Cadastre System** (§24 sibling; joint-review flag from the 2026-09-08 pass): same parcel spine, different operation. Land records holds the RIGHTS record (instruments, recording lifecycle, immutability); assessment holds the VALUE record (valuation machinery, roll). Direction of data flow confirms the seam: assessment consumes ownership/sales from land records ("Seamless land records integration eliminates sales data entry redundancy" — DEVNET; the land-records pass observed Harris Govern deeds→CAMA feeding). Remove the valuation machinery + roll → land records territory; remove the instrument/recording lifecycle → assessment. **RATIFIED from this side; keep-both; the joint-review flag is discharged.**
2. **vs Property Tax Administration** (§24 sibling, unprocessed): assessment produces the value; taxation bills and collects against it (rates/millage applied to taxable value, bills, payments, delinquency). IAAO: "The assessor does not determine property taxes. Instead, the assessed valuation determines the overall share of taxes to be paid." Suite vendors sell the two as separate product lines (Aumentum Valuation vs Aumentum Tax; DEVNET CAMA vs Billing & Collection; Catalis CAMA vs Billing & Collections) — packaging evidence of the seam. Remove valuation → tax administration; remove billing/collection → assessment. Forward note for the property-tax-administration pass: the seam is value-of-record vs money-of-record; the roll is the hand-off artifact.
3. **vs Government GIS** (processed): GIS maintains the jurisdiction's authoritative parcel geometry and map fabric; assessment binds characteristics/values to parcel identity and consumes geometry as context. DEVNET EdgeMaps puts "authoritative CAMA and Tax Data" ON maps — the map layer displays the record; the CAMA holds it. A CAMA without maps is still a CAMA (sketch ≠ GIS).
4. **vs market-facing valuation (AVM/real-estate analytics)**: mass appraisal is jurisdiction-wide, periodic, statute-bound, for the tax base; AVMs are per-property market estimates for lending/consumers. No directory leaf sampled for AVM; boundary held conceptually (unit = jurisdiction population vs single property; purpose = tax base vs transaction pricing).
5. **vs Building Condition Assessment** (§17, processed): physical condition surveys of specific buildings for facilities management — no jurisdiction-wide roll, no taxable-value derivation, different unit (building vs parcel) and different user (facility/asset managers vs assessing office).
6. **vs Permit Management** (§24 sibling): permits are regulatory cases; assessment CONSUMES permit data (DEVNET tracks permit date/value/occupancy for assessment) — a feed, not the same Type.
7. **vs Property Listing Platform / Real Estate Brokerage CRM** (§17): market-facing listing/transaction machinery; no roll, no mass appraisal, different users.

## Historical / Market-Sample Check (§24 workflow check)

- Paper-era assessing office: assessor's field cards (parcel record with characteristics), hand mass appraisal using cost manuals and neighborhood factors (valuation machinery), the handwritten assessment roll ledger with exemption columns (roll of record), board of equalization/review hearings (governed change). All three L0 legs satisfied with no software, no GIS, no portals, no AI.
- Older/regional products: 1980s–90s DOS/mainframe CAMA systems and regional vendors (e.g., the ceased-trading Windows-desktop generation seen in sibling passes) satisfy the same legs; state-specific cost manuals and abstracts are regional machinery, not definitional.
- Non-US regimes: national valuation rolls / rating lists (UK-style), land-valuation-based regimes — satisfy the three legs at the conceptual level (valuation of a defined property population + official roll + governed change), though the sample is North America-centric; regional machinery (state abstracts, equalization) is held at L2. Confidence: moderate (reasoned, not directly sampled).
- Anti-overfit guards: "CAMA" as a term is NOT definitional (the Type predates the acronym; the defining content is mass appraisal + roll); personal property is NOT definitional (real-property-only jurisdictions exist); IAAO/USPAP compliance is NOT definitional (professional standards, not structure); GIS/sketch/portals are NOT definitional (paper era satisfies without them).

## Uncertainties

- Tyler Technologies (widely described as the largest US CAMA vendor) could not be fetched (403 ×2) — market anchor only; no structural claims made from it. Vanguard Appraisals unreachable (×2).
- IAAO Glossary PDF (>5MB) not fetched; canonical definitions taken from the IAAO FAQ page only ("assessment is the value of property used to calculate your property taxes"; assessor estimates value, does not set taxes).
- Non-US assessment regimes not directly sampled; the definition is written conceptually to cover them, but evidence is North America-weighted.
- Exact operational parameters (appeal windows, certification dates, notice deadlines, ratio-study thresholds) vary by jurisdiction and are NOT asserted anywhere.
- "Property Tax Oversight" (Catalis product line) suggests a state-oversight-agency variant of assessment software; not enough evidence to characterize — left as an open note for the property-tax-administration pass.

## Final Synthesis

A Property Assessment System is the government's system of record for property value: it maintains a persistent parcel-bound record of every property and its interest holders, values the whole jurisdiction systematically (mass appraisal under cost/market/income approaches, calibrated against sales), and produces the assessment roll — the dated, official, per-parcel statement of value (and taxable value after exemptions/classification) — which it keeps truthful through governed change (appeals, corrections, abatements) and hands to taxation. Everything else commonly bundled — sketching, field collection, GIS, public portals, personal property, state reporting, AI — is standard capability or variant machinery, not the definition. The parcel spine is shared with land records (rights) and tax administration (money); each Type owns one operation over it.
