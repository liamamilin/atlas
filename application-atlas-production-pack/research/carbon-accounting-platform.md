# Research Notes — Carbon Accounting Platform

Research date: 2026-09-07
Slug: carbon-accounting-platform
Directory leaf: Carbon Accounting Platform (§21 Environment, Sustainability & Climate)

## Research Goal

Understand what a Carbon Accounting Platform actually is as a software Type: its core objects, how emissions measurement really flows through the system, what is definitional vs merely common in the current market, and where its boundaries sit against neighboring Types (ESG suites, CEMS, energy management, product footprint/LCA, decarbonization planning, carbon credits, disclosure platforms).

## Initial Boundary Hypothesis

- Core purpose: measure an organization's greenhouse gas emissions from activity data, using emission factors, producing a structured inventory (typically Scope 1/2/3) over a reporting period, for disclosure, targets, and reduction.
- Likely users: sustainability managers, ESG analysts, finance/controllers, facility and departmental data providers, auditors, IT admins.
- Nearest neighbors: Greenhouse Gas Accounting (directory sibling — possible near-alias), Sustainability Management Platform / ESG Management Platform (broader), ESG Reporting Platform (output-centric), Emissions Monitoring / CEMS (physical measurement), Energy & Carbon Management (energy-first), Product Carbon Footprint Platform / LCA (product as unit), Decarbonization Planning Platform (forward-looking), Carbon Credit Management (offsets ledger), Climate Risk Management.
- Unknowns: how data ingestion works in practice; how factor libraries are maintained/versioned; how audit/assurance support is realized; whether scope organization is definitional or just dominant.

## Research Questions

1. What is the central object — the inventory, the emission source, the activity record, or the computed emission?
2. How does activity data enter the system (integrations, file upload, manual entry, supplier surveys)?
3. How are emission factors sourced, versioned, mapped, and applied? What are estimation factors?
4. How is calculation structured (activity × factor; spend-based vs activity-based; location vs market-based Scope 2; GWP → CO2e; PCAF attribution)?
5. How is the inventory organized (scopes, Scope 3 categories, org hierarchy) and bounded in time (reporting periods, open/closed)?
6. What audit/assurance machinery exists (lineage, audit logs, anomaly detection, approvals, period locking)?
7. What disclosure/reporting outputs exist (frameworks, exports)?
8. What target-setting and reduction tracking exists, and is it part of the core or an extension?
9. Who are the users and roles?
10. Where are the boundaries vs neighboring Types — what would you remove to turn this into another Type?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Position | Tier / philosophy |
|---|---|---|
| Watershed | Enterprise carbon & sustainability platform (US) | Data-quality/audit-grade posture; Measure/Report/Act; premium enterprise |
| Persefoni | Carbon accounting & sustainability management (enterprise + financial services) | "Footprint Ledger" — financial-accounting-style controls; disclosure-oriented |
| Microsoft Sustainability Manager | Suite module (Microsoft Cloud for Sustainability / Dynamics 365) | Data-integration-first; platform extensibility; documented operational docs |
| IBM Envizi | Enterprise ESG data management suite with carbon core | Data-management-first; finance-grade validation; module lattice |
| Greenly | SMB-to-enterprise carbon management (European) | Self-serve/AI-assisted; SMB entry point; compliance breadth |

## Sources

Tier 1 (official operational documentation):

- Microsoft Learn — Microsoft Sustainability Manager: overview, manage emissions, configure emission factors, calculate Scope 2, calculate Scope 3, data import overview (learn.microsoft.com/en-us/industry/sustainability/...) — fetched 2026-09-07
- Watershed — watershed.com root, /platform/measure/carbon-accounting, /platform/measure — fetched 2026-09-07 (product/marketing pages; no public help center reached)
- Persefoni — persefoni.com root, /business/carbon-footprint-measurement-analytics — fetched 2026-09-07 (product pages; no public help center reached)
- IBM Envizi — ibm.com/products/envizi — fetched 2026-09-07 (product page; ibm.com/docs/en/envizi returned 403)
- Greenly — greenly.earth/en-us root, /en-us/products/carbon-footprint — fetched 2026-09-07 (product pages; help center not reached)

Source-access limitations:

- Microsoft is the only product with deep public operational documentation (step-by-step calculation and import docs). Findings for Watershed, Persefoni, Envizi, Greenly rest on official product/platform pages (Tier 2), so their operational claims are kept at the level those pages support.
- IBM's documentation portal (ibm.com/docs) returned 403; only the product page was used.
- No numeric limits, prices, or default values are asserted in the final document beyond what fetched pages state.

## Product Observations

### Microsoft Sustainability Manager (evidence layer A — direct operational docs)

- Positioning: "extensible solution that unifies data intelligence... record, report, and reduce your organization's emissions and water or waste impact." Suite module (Power Platform/Dataverse-based).
- Structure: Record → Report → Track → Reduce. Configuration: organizational units, facilities, company profile, regions, unit groups, reporting settings, carbon fee, user roles, auditing.
- Emissions are records: "All emissions" page lists calculated emissions; filterable by facility/organizational entity/fuel type; exportable to Excel; manually addable; "Emissions can include multiple greenhouse gases... calculates all standard reported greenhouse gases for each emission source."
- Emission factors: stored in **factor libraries** (default/custom/demo). Default libraries with versions: Defra (2022–2026), EPA GHG EF Hub (2015–2025), IEA, NGER (Australia), ADEME Base carbone (France), EXIOBASE, NEEFE (EU), NGA (Australia), Taiwan MoEnv. **Factor mappings** bind factors to reference data (facility, fuel, material, disposal method) so one calculation model serves many factors. **Estimation factors** convert proxy data (square footage, hotel nights) into activity data. Custom factors for industrial processes/renewables.
- Scope 2: location-based vs market-based methods; separate factor libraries per method; factor types (direct line, regional, national; energy attribute certificates, contracts, supplier-specific, residual mix); Emissions = Electricity × EF; GWP conversion to CO2e (CH4, N2O); CHP allocation methods (efficiency/energy content/work potential).
- Scope 3: all 15 categories; per-category methods — spend-based default (EPA supply chain/EEIO: cost × EF by commodity code, with currency/inflation conversion), average-data method substitution, fuel- and energy-related (reuses Scope 1/2 activity data × upstream factors + T&D factor), transport by distance/fuel/cost, waste by material + disposal method, business travel (distance, hotel nights via estimation factors), leased assets (asset-specific method), use of sold products (lifespan fields, report at sale per GHG Protocol), franchises, **Category 15 Investments via PCAF** (attribution factor × emissions; Part A financed emissions formulas for listed equity/bonds, business loans, project finance, CRE, mortgages, motor vehicle loans, sovereign bonds).
- Data import: Excel templates, Power Query guided flow/templates, data provider connectors (Ecolab, EcoVadis, Emissions Impact Dashboard), manual entry. Import mapping (source→destination fields), auto map, data transformation. **Reporting years**: named, start date, period template; periods default **Open**; **Closed** periods block calculations, import, creation, modification, deletion (audit control). **Data approval management (preview)**: staged pending state, records don't affect calculations until approved; disabled by default.
- Reporting: dashboards (emissions overview, Scope 1/2/3, renewable energy, water, waste), quantitative preparation report, deep analysis tool. Track: scorecards and goals. Reduce: targets. Also social/governance tracking (ESRS areas) — suite drift.
- AI: Copilot data query (preview).

### Watershed (evidence layer A for product pages; operational depth limited)

- Positioning: "trusted platform for sustainability AI"; Measure / Report / Act; enterprise posture (90+ Fortune 500 customers claimed).
- Carbon accounting definition (their guide): "emissions are calculated by multiplying business data (such as an employee travel budget or an office electric bill) by an 'emissions factor'" — activity × factor is the stated mechanism.
- Measure: ingest "any kind of data" (utility bills, spreadsheets, APIs) with AI cleaning/standardization, anomaly detection; "2.3 million built-in emissions factors covering 95% of the global GDP"; 150+ automated error checks; full data lineage ("every number is traceable"); transparent AI with cited sources; third-party assured methodologies; Kyoto gas breakdowns; customize calculation methodology; configure footprints per business unit/geography; activity-based Scope 3.1 for purchased products/materials; all 15 Scope 3 categories; bring-your-own factors/methodology (FAQ topics listed).
- Small vs large company feature split (their buying guide): small = manual upload, single-region model (US EEIO), 1–2 measurements/year, manual export; large = automated integrations + manual upload, Scope 1–3, multi-region models (CEDA), multiple measurements/year, reporting, benchmarking, target-setting, simulations/scenario planning, project management for data collection, complete audit trail and data governance.
- Report: Disclosures toolset — pre-populates data, AI drafting, formats to disclosure requirements (CSRD, California SB253/SB261, CDP...), full data lineage, review workflows, peer benchmarks. Act: decarbonization paths, clean power marketplace, supply chain engagement, forecasting at material/product/company level. Product footprints as a solution.
- Supplier engagement: integrated for Scope 3.

### Persefoni (evidence layer A for product pages; operational depth limited)

- Positioning: "Carbon Footprint & Sustainability Reporting"; Measure, Report, Decarbonize; Pro/Advanced plans; free sign-up tier exists.
- **Footprint Ledger**: "manage your emissions data with the same accuracy, granularity, and control as your financial data" — the financial-accounting metaphor is the product's stated philosophy.
- Features: activity & audit logs (who added/modified/deleted, when); **calculation transparency** — "view accounting frameworks, calculation formulas, conversion factors, emission factors, and Global Warming Potential on a per-calculation level"; footprint analytics (hotspots, trends by scope and category "at any level of your organization"); pre-built data integrations; **advanced data controls — lock reporting periods and approve data before it's merged into your Footprint Ledger**; advanced permissions (custom user permission groups).
- Scope 1/2/3 "in alignment with the Greenhouse Gas Protocol"; "assurance-grade GHG emissions reporting for every major climate disclosure regulation"; "detailed activity and usage data, not just spend-based estimates" (assurance posture).
- Frameworks: SBTi, TCFD, California, CSRD, PCAF, SASB. Financial services line: financed emissions accounting (PCAF), investor reporting, portfolio company engagement.
- Decarbonization: net-zero target setting, reduction modeling, supplier engagement.
- AI: PersefoniAI — Copilot (GPT-style chat), anomaly detection (e.g., electricity consumption), natural-language emission factor mapping of spend files to LCA/commodities factors.

### IBM Envizi (evidence layer A for product page; docs portal 403)

- Positioning: "compliance ready solution for ESG data... analytics, reporting and planning"; leader in Verdantix Green Quadrant Enterprise Carbon Management 2026 (vendor-claimed).
- Modules: Emissions Management (Scope 1/2 GHG Accounting + Reporting "emissions calculation engine built on the GHG Protocol"; Scope 3 with AI; Emissions API; Emissions Calculations in Excel; Scope 3 Financed Emissions; Supply Chain Intelligence for Scope 3 Cat 1/2), ESG Reporting (frameworks, building ratings/benchmarks, surveys/assessments), Decarbonization (Planning Analytics, Program Tracking, Utility Bill Analytics, Interval Meter Analytics, Target Setting + Tracking).
- Data features: automated ingestion from ERP, IoT/metering platforms, utility providers, spreadsheets, supplier portals; **data tagging** (metadata at ingestion; one trusted dataset reused across calculations/dashboards/disclosures); **customizable organizational hierarchy** (regions, sites, assets, product lines, joint ventures) with roll-ups; **data health checks & audit trails** ("finance-grade, traceable data... supports internal controls, third-party assurance"); supplier-level transaction data aggregated/normalized for Scope 3.
- Pricing: based on data volume.

### Greenly (evidence layer A for product pages; help center not reached)

- Positioning: "One home for all Carbon Intelligence"; SMB-to-enterprise; European; Carbon Assessment / Supplier Engagement / Decarbonization / Emission Factors / LCA / compliance products (TCFD/IFRS, SBTi, CBAM, EUDR, DPP, California, Ecovadis).
- Carbon assessment method (their FAQ): Identify (find every emission source across internal operations and external value chain) → Calculate (convert to CO2e) → Prioritize. "Tracks your emissions (Scopes 1, 2, and 3) by analyzing the physical and financial data tied to your business activities... methodology aligned with global GHG Protocol standards."
- Data: "activity-based data, spend-based data and supplier-specific metrics."
- Journey: Launch (collect) → Assess Impact (calculate across all scopes, identify reduction opportunities) → Set Targets (SBTi-aligned) → Drive Action (reduction initiatives) → Ensure Accountability (track progress, report via CSRD/CDP/TCFD).
- AI: EcoPilot (file → clean categorized data, supply chain screening, quality control, reduction recommendations). Partner program (consultants resell). Free calculators as lead-gen.

## Cross-product Comparison

| Structure | MS SM | Watershed | Persefoni | Envizi | Greenly | Layer |
|---|---|---|---|---|---|---|
| Activity data records bound to org unit + time | ✓ (activity data model, import) | ✓ (ingest bills/spreadsheets/APIs) | ✓ (activity & usage data) | ✓ (automated capture, tagging) | ✓ (physical + financial data) | Core (B) |
| Emission factor library (published sources, versioned) | ✓ (Defra/EPA/IEA/ADEME/EXIOBASE/NGER/NEEFE/NGA/Taiwan, versioned) | ✓ (2.3M factors claim; CEDA; BYO factors) | ✓ (EFs + GWP per calculation) | ✓ (calculation engine on GHG Protocol) | ✓ (Emission Factors product) | Core (B) |
| Calculation engine: activity × factor → GHG → CO2e (GWP) | ✓ (explicit formulas) | ✓ (stated mechanism) | ✓ (formulas + GWP per calculation) | ✓ | ✓ (CO2e conversion) | Core (B) |
| Organizational hierarchy as attribution dimension | ✓ (org units, facilities, regions) | ✓ (business units/geographies) | ✓ ("any level of your organization") | ✓ (regions/sites/assets/product lines/JVs) | ✓ (implied; sites) | Core (B) |
| Inventory organized by Scope 1/2/3 (+ Scope 3 categories) | ✓ (all 15 categories) | ✓ (all 15 categories) | ✓ (Scope 1/2/3) | ✓ (Scope 1/2, Scope 3 modules) | ✓ (Scopes 1/2/3) | Common mature (B) — universal in sample, GHG Protocol-driven |
| Reporting period as managed container | ✓ (reporting years, open/closed) | ✓ (multiple measurements/year) | ✓ (lock reporting periods) | ✓ (implied by reporting cycles) | ✓ (annual assessment implied) | Common mature (B) |
| Audit trail / lineage / data quality | ✓ (auditing, approval staging, error handling) | ✓ (lineage, 150+ error checks, anomaly detection) | ✓ (audit logs, per-calculation transparency) | ✓ (health checks, audit trails, finance-grade) | ✓ (AI quality control) | Common mature (B) |
| Data ingestion machinery (integrations + upload + manual) | ✓ (Excel/PQ/connectors/manual) | ✓ (60+ integrations + upload) | ✓ (pre-built integrations) | ✓ (ERP/IoT/utility/spreadsheets/supplier portals) | ✓ (file → data via AI) | Common mature (B) |
| Disclosure/framework reporting outputs | ✓ (quantitative preparation report; ESRS S/G tracking) | ✓ (CSRD/SB253/SB261/CDP formatting) | ✓ (assurance-grade, major regulations) | ✓ (ESG Reporting Frameworks module) | ✓ (CSRD/CDP/TCFD/IFRS...) | Common mature (B) |
| Method choices per scope/category | ✓ (spend vs activity; location vs market; distance/fuel; PCAF) | ✓ (spend vs activity-based FAQ; activity-based 3.1) | ✓ (activity/usage "not just spend") | ✓ (supplier-level transactions) | ✓ (activity/spend/supplier-specific) | Common mature (B) |
| Estimation factors / proxy data → activity data | ✓ (explicit estimation factors) | ✓ (AI cleaning/standardization; estimation implied) | — (not observed on fetched pages) | — | ✓ (AI file transformation) | Common (A for MS; B partial) |
| Targets & progress tracking | ✓ (scorecards/goals) | ✓ (target modeling) | ✓ (net-zero, reduction modeling) | ✓ (Target Setting + Tracking) | ✓ (SBTi) | Common mature (B) |
| Supplier engagement for Scope 3 | ✓ (EcoVadis connector; value chain solution) | ✓ (integrated supplier engagement) | ✓ (Scope 3 supplier engagement) | ✓ (Supply Chain Intelligence, supplier portals) | ✓ (Supplier Engagement product) | Common mature (B) |
| Financed emissions (PCAF) | ✓ (Category 15) | ✓ (Finance solution) | ✓ (Financial Services line) | ✓ (Financed Emissions module) | ✓ (Finance industry solution) | Common for financial-institution segment; variant overall |
| Decarbonization planning / abatement modeling | ✓ (Reduce: targets) | ✓ (Act: decarbonization paths, forecasting) | ✓ (Decarbonization Management) | ✓ (Planning Analytics, Program Tracking) | ✓ (Action plans) | Common mature (B) — but forward-looking, not measurement |
| Water/waste/other environmental metrics | ✓ (water & waste features) | ✓ (water, waste, pollution FAQ) | — (not observed) | ✓ (energy/waste data in suite) | ✓ (LCA, ESG products) | Optional / suite drift |
| Product carbon footprint extension | — (product fields in Cat 10/11) | ✓ (Product Footprints solution) | — | — | ✓ (LCA product) | Optional |
| AI assistance | ✓ (Copilot) | ✓ (agents) | ✓ (PersefoniAI) | ✓ (AI-assisted) | ✓ (EcoPilot) | Era-common (B) |
| Carbon fee/pricing internal | ✓ (carbon fee setup) | — | — | — | — | Vendor-specific (A, single product) |
| Marketplace for clean power/credits | — | ✓ (Marketplace) | — | — | — | Vendor-specific (A, single product) |
| Emissions API / embed | — | — | — | ✓ (Emissions API) | — | Vendor-specific (A, single product) |
| Free/self-serve entry tier | — | — | ✓ (Sign up free) | — | ✓ (free calculators) | Segment variant |

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

A Carbon Accounting Platform is recognizable only if all of the following hold:

1. **Organizational activity data as managed records** — quantified records of what the organization does that emits (energy purchased, fuel burned, materials bought, travel, waste), each bound to an organizational unit and a time period.
2. **Emission factors** — documented coefficients that convert activity into greenhouse gas emissions, with traceable source/methodology.
3. **Computed emissions inventory** — the platform calculates emissions (activity × factor, gases converted to CO2e) and aggregates them into an inventory for the organization over a reporting period.

Remove any one: without activity data + factors + computed inventory it is not carbon accounting (it becomes disclosure formatting, a risk tool, or a physical monitoring system); without the organizational unit of account it becomes product footprint/LCA or a consumer calculator.

Historical check: pre-platform practice (spreadsheets computing organizational GHG inventories from activity × factors) and early regional calculators satisfy this minimal core — no scope taxonomy, supplier portals, AI, or framework formatting required. Scope organization is therefore NOT definitional, though it is universal in the current market.

### L1 — Common Mature Structure

- Organizational hierarchy (facilities/sites/business units/regions; sometimes assets, product lines, JVs) as the attribution and roll-up dimension.
- Inventory organized by emission scope (Scope 1 direct, Scope 2 purchased energy, Scope 3 value chain) and Scope 3 categories, per GHG Protocol; Kyoto-gas breakdown and CO2e via GWP.
- Data ingestion machinery: system integrations, file upload (Excel/CSV), manual entry, supplier surveys/portals; import mapping and transformation.
- Emission factor libraries from published sources (national agencies, IEA, input-output databases), versioned by year; factor mappings to reference data; custom factors; estimation factors converting proxy data to activity data.
- Calculation method choices: spend-based vs activity-based; location-based vs market-based Scope 2; distance/fuel/spend methods for transport; PCAF attribution for financed emissions.
- Data quality & audit machinery: audit trails, data lineage, anomaly detection, health checks, approval staging, period locking/closing.
- Reporting period management (annual/period containers; open → closed lifecycle).
- Disclosure outputs: framework/regulation-aligned reports and exports (CSRD, CDP, TCFD/ISSB, California SB 253/261, etc.).
- Analytics: dashboards by scope/category/org unit; hotspots; trends; export.
- Target setting and progress tracking (often SBTi-aligned).
- Supplier engagement to improve Scope 3 data quality.

### L2 — Variant / Optional Structure

- Financed emissions (PCAF) as a financial-institutions segment specialization.
- Decarbonization planning/abatement modeling, reduction roadmaps, program tracking.
- Supplier engagement portals as a distinct product surface.
- Extended environmental metrics (water, waste, pollution) — suite drift toward Sustainability/ESG Management.
- Product carbon footprint / LCA extension.
- Carbon marketplace (clean power, credits) — extension.
- AI assistance (data cleaning, EF mapping, drafting, Q&A) — era-current across all sampled products.
- Regional factor regimes (ADEME/France, NGER/Australia, Taiwan MoEnv, EU NEEFE) — geographic variants.
- Delivery posture: standalone SaaS vs suite module (ERP/Power Platform) vs data-platform module; SMB self-serve vs enterprise sales-led; pricing by data volume.
- Internal carbon fee/pricing (single product in sample).

### L3 — Vendor-specific (research notes only)

- Watershed: CEDA multi-region model, 2.3M factors / 95% GDP claim, 150+ error checks, Cornerstone Sustainability Data Initiative, Marketplace, Data Explorer, product tours.
- Persefoni: Footprint Ledger branding, PersefoniAI Copilot/anomaly detection/NL EF mapping, Pro vs Advanced plan gating (audit logs "coming soon to Pro"), SpydySense.
- Microsoft: Power Platform/Dataverse architecture, factor library loading via Power Platform admin center, Contoso demo data, Copilot data query, carbon fee setup, Ecolab/Emissions Impact Dashboard connectors, unit groups, record uniqueness (OCID).
- IBM Envizi: module lattice naming, Emissions API, Emissions Calculations in Excel, data-volume pricing, Verdantix leader claim, case-study metrics (Ikano 15K data types, Downer 45% error reduction).
- Greenly: EcoPilot, partner program economics, free calculators, comparison pages vs competitors, website-emissions widget.

## Vendor-specific Findings

See L3 above. None of these enter the canonical document except as neutral examples where useful.

## Boundary Findings

- **vs Greenhouse Gas Accounting (directory sibling leaf)**: probable near-alias. "GHG accounting" names the methodology/process; "Carbon Accounting Platform" names the software that performs it. The sampled products describe themselves with both terms interchangeably (Watershed's page is titled "carbon accounting"; Envizi's engine is "built on the GHG Protocol"; Microsoft's docs say "GHG emissions"). Recommend joint review; likely the two leaves should be merged or explicitly split as methodology-vs-software.
- **vs Sustainability Management Platform / ESG Management Platform**: broader Types include social/governance metrics and wider ESG data management. The carbon platform's center of gravity is the emissions inventory as system of record. Evidence of drift: Microsoft adds water/waste/social/governance; Envizi is explicitly an "ESG data" solution; Greenly sells ESG products. The boundary is the center of gravity, not exclusive capability.
- **vs ESG Reporting Platform / ESG Disclosure Management**: disclosure-centric Types start from the report/disclosure requirement; carbon accounting starts from measurement. Disclosure is an output (L1) of the carbon platform, not its defining loop.
- **vs Emissions Monitoring / CEMS**: CEMS continuously measures actual emissions at emission sources with physical instruments (stack analyzers); carbon accounting computes organizational emissions from activity data × factors. Different data model, different users (plant operations vs corporate sustainability). Remove activity-data accounting → you get CEMS.
- **vs Energy & Carbon Management / Building Energy Management**: energy-first Types optimize consumption (metering, control, efficiency); carbon accounting is organization-wide including value chain, with energy as one input. Overlap: utility bill/interval data ingestion appears in both (Envizi has Utility Bill Analytics).
- **vs Product Carbon Footprint Platform / LCA**: unit of account is the product (functional unit, lifecycle stages) vs the organization (boundary, scopes). Some carbon platforms extend to PCF (Watershed, Greenly; Microsoft has product fields in Scope 3 Cat 10/11) — evidence of adjacency, not identity.
- **vs Decarbonization Planning Platform**: forward-looking abatement planning (marginal abatement cost curves, project portfolios) vs measurement-first accounting. All sampled carbon platforms add planning (L2), but the defining loop of this Type ends at a measured, auditable inventory.
- **vs Carbon Credit Management / Carbon Trading**: credits/offsets as instruments with registries/retirement vs the emissions inventory. Watershed's Marketplace is an extension, not the core.
- **vs Climate Risk Management / Scenario Analysis**: risk exposure (physical/transition) vs emissions quantification. Scenario features in carbon platforms (Watershed simulations) are L2.
- **Remove-tests**: remove the organizational boundary → Product Carbon Footprint/LCA; remove activity×factor computation → ESG Reporting; remove GHG quantification → ESG Management; remove computation-from-activity (measure physically) → CEMS; remove the inventory (only forward-looking) → Decarbonization Planning.

## Uncertainties

- Scope organization treated as L1 (common mature), not L0: justified by the historical check (spreadsheet-era inventories satisfy the minimal core without scope structure) and by ISO 14064-1's alternative category scheme. Confidence: moderate-high; no sampled counter-example product lacking scopes was studied (none reached).
- Assurance/verification workflows: products claim "audit-ready"/"assurance-grade" and describe audit logs/lineage/period locking, but the operational detail of third-party assurance support (e.g., auditor seats, evidence packs) was not directly observed. Final document keeps this at the level of audit trail/lineage/period control.
- Factor library contents per vendor: only Microsoft's list is directly documented; other vendors' factor sources are inferred from product pages (Watershed's CEDA/EEIO mentions, Greenly's Emission Factors product). Kept generic in the final document.
- Greenly operational depth: help center not reached; Greenly-specific claims kept moderate.
- Whether "multiple measurement cadences per year" is common: Watershed's buying guide implies small companies measure 1–2×/year and large ones more; not verified across other products. Kept as variant observation.

## Final Synthesis

A Carbon Accounting Platform is an organization's system of record for its greenhouse gas emissions. Its defining loop: capture quantified activity data across the organizational boundary → apply documented emission factors (with method choices per emission category) → compute emissions in CO2e → aggregate into a structured inventory for a reporting period → make that inventory auditable (lineage, audit trail, period control) → produce disclosure outputs and track reduction targets. The scope taxonomy (GHG Protocol) is the dominant organizing scheme but not the definition; data ingestion, supplier engagement, targets, planning, AI, and extended environmental metrics are common mature or optional structures; financed emissions is a segment variant. The Type is bounded against ESG suites (center of gravity), CEMS (measurement physics vs accounting), product footprint/LCA (unit of account), disclosure platforms (output vs measurement), and decarbonization planning (forward vs backward looking).
