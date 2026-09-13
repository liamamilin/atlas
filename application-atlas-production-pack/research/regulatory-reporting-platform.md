# Research Notes — Regulatory Reporting Platform

## Research Goal

Understand what a Regulatory Reporting Platform (§08 Finance, Banking, Insurance & Investment) really is from real products: what objects exist inside it, how data becomes a filed supervisory report, what roles and rules govern the process, and where its boundary lies against Reporting Platform (§13), Financial Risk Management Platform, Tax Compliance Platform, Regulatory Change Management (§11), Financial Consolidation, and the life-sciences RIM leaf (§22).

## Initial Boundary

Initial hypothesis: this Type is the financial institution's machinery for producing and filing supervisory reports (prudential, statistical, transaction, tax-information) to regulators — distinct from BI reporting (no submission machinery) and from risk platforms (measurement vs filing). Prior passes left flags to discharge:

- reporting-platform (§13, processed 2026-09-09): "adjacent (filing/submission machinery with taxonomies/validations/submissions vs formatted output from org data with no submission machinery)"
- financial-risk-management-platform (§08): "adjacent, often bundled — risk platforms produce the risk figures and ship regulatory content packs; a regulatory reporting platform's center is the report production/submission machinery"
- actuarial-modeling-platform: joint-review flag vs this leaf left open

## Research Questions

1. What exactly is a "regulatory report" in this context — what binds it (regulator, period, entity, template)?
2. What are the core objects: report, data model, mapping, calculation, validation, workflow, submission?
3. How does data flow from source systems (GL, core banking, trading, risk, policy admin) to a filed report?
4. What role does vendor-maintained regulatory content (templates, taxonomies, rule packs) play?
5. What is the submission lifecycle (prepare → validate → sign-off → submit → acknowledge → amend)?
6. What roles exist and what permissions matter?
7. Which regime families appear (prudential, statistical, granular, insurance, transaction, tax-information, disclosure)?
8. Where are the boundaries: vs BI reporting, vs risk platforms, vs tax compliance, vs regulatory change management, vs consolidation, vs life-sciences RIM, vs statutory financial filing?
9. Does a supervisor-side (collection) pole exist, and is it the same Type?

## Representative Products

Selected for market representation, documentation completeness, different philosophies, different customer tiers:

1. **Regnology** (Reporting Hub / Ascend; also Supervisory Hub) — cloud-native consolidator of the category; serves both regulators and the regulated; Tier-1 through community banks, broker-dealers, insurers.
2. **Nasdaq AxiomSL** (ControllerView) — enterprise modular platform, data-integrity-centered; G-SIBs down to US mid-sized banks; broker-dealers; asset managers.
3. **Oracle Financial Services** (OFSAA / OFSDF + REG REP integration packs + AgileREPORTER integration + DGRR + CRS) — suite pole with official product documentation reachable.
4. **OneSumX for Regulatory Reporting** (Wolters Kluwer FRR → acquired by Regnology 2025-12-01) — finance/risk/regulatory integrated suite; rich official brochure evidence.
5. **deltaconX** (listed on Temenos marketplace) — transaction-reporting-weighted full-stack platform (EMIR, MiFIR, SFTR, Dodd-Frank, FinfraG, MAS, ASIC, REMIT).
6. **Temenos Regulatory Compliance** — embedded-in-core-banking variant (boundary/variant evidence, not a core sample).

Rejected during research:
- **Vermeg** — root site shows pivot to collateral management + insurance core; regulatory reporting division (AGILE, ex-Lombard Risk AgileREPORTER) sold to Regnology 2024-11-25. Product mismatch; recorded.
- **Abrigo** — lending/credit-risk/ALM vendor; not a regulatory reporting platform.

## Sources

- Regnology root: https://www.regnology.net/ (fetched 2026-09-10)
- Regnology Reporting Hub: https://www.regnology.net/en/solutions/for-the-regulated/regnology-reporting-hub/ (fetched 2026-09-10)
- Regnology news — Vermeg AGILE acquisition: https://www.regnology.net/en/resources/news/regnology-acquires-vermegs-regulatory-reporting-business/ (search snippet, 2026-09-10)
- Regnology news — Wolters Kluwer FRR closing: https://www.regnology.net/en/resources/news/regnology-completes-acquisition-of-wolters-kluwers-finance-risk-regulatory-reporting/ (search snippet)
- Business Wire — FRR acquisition closing: https://www.businesswire.com/news/home/20251130594274/en/ (search snippet)
- Nasdaq AxiomSL: https://www.nasdaq.com/solutions/fintech/nasdaq-axiomsl (fetched 2026-09-10)
- Oracle OFS REG REP US Treasury Introduction (official docs): https://docs.oracle.com/cd/E94391_01/PDF/8.1.1.0.0/OFS_REG_REP_US_TREASURY/UG/2_Introduction.htm (fetched 2026-09-10)
- Oracle OFS AGILE RP EBA Introduction (official docs): https://docs.oracle.com/cd/E93135_01/PDF/8.1.2.0.0/AGILE_RP_EBA_HTML/UG/2_Introduction.htm (search snippet)
- Oracle accounting & regulatory compliance page: https://www.oracle.com/financial-services/analytics/accounting-and-regulatory/ (search snippet)
- Oracle DGRR docs: https://docs.oracle.com/cd/F38446_01/PDF/8.1.0.0.0/DG_HTML/DG_IG_8.1/2_Introduction_to_Oracle_Financial_Services_Data_Governance_for_US_Regulatory_Reporting.htm (search snippet)
- OneSumX for Regulatory Reporting brochure (via Temenos marketplace): https://www.temenos.com/solution-provider/wolters-kluwer/ and https://www.temenos.com/wp-content/uploads/2022/10/wolters-kluwer-onesumx-regulatory-reporting-solution-overview.pdf (search snippets)
- deltaconX via Temenos: https://www.temenos.com/solution-provider/regulatory-reporting-platform-deltaconx/ (search snippets)
- Temenos Regulatory Compliance: https://www.temenos.com/products/core-banking/regulatory-compliance/ (search snippets)
- Vermeg root (pivot evidence): https://www.vermeg.com/ (fetched 2026-09-10)

**Source-access limitations:**
- axiomsl.com direct fetch timed out ×2 (root + solutions path); evidence taken from nasdaq.com official product pages (Nasdaq is the product owner post-Adenza). Assertion strength calibrated; no axiomsl.com-only detail claimed.
- No hands-on user manuals/admin guides accessible for Regnology, AxiomSL, deltaconX; evidence is official product/solution pages + Oracle's official docs. Precise operational parameters (per-report deadlines, channel protocols, exact state names) NOT claimed.
- Vendor-claimed numbers (validation-rule counts, regulator counts, G-SIB percentages) recorded as vendor claims only.
- Wolters Kluwer's own OneSumX page 404'd; brochure text obtained via Temenos marketplace (official partner listing).

## Product Observations

### Regnology (Reporting Hub / Ascend) — Evidence Layer A unless noted

- Positioning: "comprehensive, cloud-first regulatory reporting platform designed to streamline and intelligently orchestrate the entire reporting lifecycle, from data ingestion to submission."
- Data model: "unique granular data model — a standardized, multi-jurisdictional model that shields clients from regulatory change, supports 'map once, report many'"; flexible ingestion "at multiple data entry points—granular, results, or report-level—allowing institutions to integrate at any stage of their data maturity."
- Calculation: "powerful calculation engine" supporting "capital, liquidity, credit, and risk calculations with full transparency and auditability" (vendor claims: 25,000+ calculations, 1M allocation rules).
- Validation: "advanced data validation and quality controls... at the granular data input level and throughout the entire reporting lifecycle" (vendor claims: 2,000+ pre-configured data controls, 10,000+ validation rules).
- Workflow: "automated workflow and task management... exception-based processing, task management, and collaborative tooling"; "centralized exception monitor"; KRI dashboard.
- Submission: "Automate reporting submissions and regulator feedback with built-in API connectivity. Integrated schedulers keep you on track with reporting obligations and submission deadlines."
- Governance: "full data lineage and audit trails, tracing every data point and calculation from source to submission" (BCBS 239 framing); separate Data Governance product.
- Coverage: "Prudential, statistical, granular, and disclosure reporting"; "Template, cube, and granular data formats"; regulators named: EBA, ECB, SRB, PRA, FINMA, BaFin, ACPR, BdE, Fed, FDIC, SEC, CFTC, OSFI, MAS, HKMA, APRA, SARB, CIMA.
- Dual-sided: Supervisory Hub, AEOI, Fusion Statistics for regulators; Hubs (Reporting, Transaction, Tax, Insurance, Risk, Finance) for the regulated; "connecting supervisory authorities and financial institutions across more than 100 countries."
- Consolidation (Layer A, official news): acquired Vermeg's regulatory reporting division AGILE (2024-11-25, ex-Lombard Risk AgileREPORTER; "supports over 150 global and international banks"; Vermeg refocuses on collateral + insurance); completed acquisition of Wolters Kluwer's FRR (OneSumX for Finance/Risk) 2025-12-01; acquired Moody's Regulatory Reporting & ALM; announced Fed Reporter acquisition; earlier CG3-1 (broker-dealer, "from Tier 1 banks and broker-dealers to local community banks in North America").
- OneSumX integration note on RRH page: "The integration of OneSumX will extend coverage and functionality... broader jurisdictional reach."

### Nasdaq AxiomSL (ControllerView) — Evidence Layer A (nasdaq.com official pages)

- Positioning: "a cloud, AI-enabled and modular platform that enables financial institutions to produce and manage their regulatory reporting and risk analysis obligations"; FAQ: "a data integrity and control platform that helps financial institutions automate and streamline regulatory reporting across jurisdictions."
- Platform center: "Behind every regulatory reporting and risk analysis module is the same powerful platform, ControllerView. It powers your entire reporting process—from data capture to final filing—delivering true straight-through processing."
- Data: "Data is ingested in its native format from any source and integrated into a unified data model. With data always in a ready state, financial, risk and operational regulatory reports are a click away. Full traceability and lineage views are also readily available."
- STP definition (FAQ): "Straight through processing automates the internal steps of regulatory reporting, including data ingestion, validation and lineage."
- Modules: Capital Risk, ESG Reporting, Global Shareholding Disclosures, Liquidity Risk Reporting, Regulatory Reporting, Trade & Transaction Reporting — "modular, add-as-you-need architecture... accessing shared data, standardized tools, integrated workflows."
- Workflow/oversight: "built-in project management tools, KPI tracking, dashboards, visualizations and automated workflows, bring every task, participant and obligation together."
- Rule content: "embedded Regulatory Rule reference and searchable navigation"; "Produce regulatory and bespoke reports... including RWA Capital Calculations, EBA IFR, IFRS 9, and Broker-Dealer Net Capital" (capital-risk page snippet).
- Audit: "full auditability and traceability of data lineage within the platform including detailed data drilldowns."
- Regulatory change: "Regulatory Change Managed Service monitors global regulatory updates and implements necessary changes within AxiomSL."
- Audiences: banks (financial regulatory reporting, risk regulatory reporting, risk analysis, trade & transaction, GSD); broker-dealers ("high-volume, high-frequency transaction reporting across global regulatory regimes... real-time exception management, detailed dashboards, and strong validation workflows... precise and timely submissions"); asset & fund managers (AIFMD Annex IV, Form PF, EMIR, FATCA/CRS, SFTR, GSD "using a single data repository platform").
- US mid-sized banks pole: "Call Report and FR Y-9C"; "Prescribed regulatory data dictionary... mapped once and reused across reports"; "workflow management and sign[-off]"; "AI-enabled, SaaS"; positioned against "spreadsheet-based logic."
- Deployment: RegCloud SaaS ("continuous integration and deployment pipelines for infrastructure, software updates, and regulatory-driven changes").
- Vendor claims (not canonical): "90% of G-SIBs", "170+ regulators in 60+ jurisdictions" (elsewhere "110 regulators in 55 countries" — internally inconsistent marketing numbers).

### Oracle Financial Services (OFSAA / OFSDF / REG REP packs / AgileREPORTER / DGRR / CRS) — Evidence Layer A (official docs)

- Problem framing (official docs): "banks and financial institutions must file hundreds of regulatory reports. For the U.S. Treasury alone, institutions must file multiple submissions of FFIEC-101, call reports, stress testing reports... Reporting requirements increase rapidly in number and complexity for banks operating regionally or globally, where they must file in multiple jurisdictions."
- Scope statement: "manage and execute regulatory reporting in a single integrated environment. It automates end-to-end processes from data capture through submission."
- Architecture: OFSAA platform on OFSDF ("analytical data warehouse platform for the Financial Services industry... industry data model") + Data Integration Hub sourcing "from multiple source systems"; REG REP integration packs per regulator (US Treasury TIC SHL(A)/SHC(A); US FED; EBA/ECB incl. AnaCredit via Central Bank of Malta).
- AgileREPORTER (integrated "last mile", Vermeg/Lombard Risk product): "a form and workflow tool that enables both creation and submission of regulatory returns... automating compliance with mandated reports to central banks, regulatory agencies... standardizes data elements and automates regulatory report production in prescribed templates with the associated workflow for automatic submission. It is a reliable and efficient infrastructure to compile, generate, and submit regulatory reports. It collects data from a wide universe... It provides automated repeated manual adjustments, variance analysis, and validation checks. It provides features to explain and justify a number quickly."
- Data governance (DGRR): "Defines maintain and track regulatory report submissions"; maps "multiple data sources to a standard, common business glossary" (vendor claim: 20,000+ business terms); BCBS 239 framing.
- Tax-information reporting (CRS): "full regulatory compliance, due diligence, and regulatory reporting—including corresponding e-file reports—for OECD domestic guidelines... Workflow automation to populate, search, and review reports and e-file approved CRS reports"; "flexible and customizable rules engine for multiple jurisdiction requirements"; "generating bulk reports and approvals."
- Suite claim: "Automate financial and regulatory compliance from data capture and consolidation to computation and submission."

### OneSumX for Regulatory Reporting (Wolters Kluwer FRR → Regnology) — Evidence Layer A (official brochure via Temenos marketplace)

- Report-type taxonomy (valuable): "covers various types of reporting, including Financial (e.g. FINREP), Prudential (e.g. COREP, BCAR, FRY-14), Transactional (e.g. MiFID II), Statistical (e.g. Economic & Financial Statistics), Granular (e.g. AnaCredit) and Multi-dimensional (e.g. Smart Cubes) reporting."
- Regulatory content: "subject matter experts actively monitor and analyze regulatory changes in approximately 30 countries worldwide"; "a single and complete regulatory library."
- Multi-regulator: "reporting to multiple regulators ensuring the use of a standard and consistent data platform and reporting tool across multiple geographies"; "global, standardized and flexible data model... while maintaining the specific requirements of local regulators."
- Data quality: "Check and attest the quality of the data that has been reported, including reconciliation between ledger and subledger, production of trial balances, cross validation between reporting regimes and variances against institution-specific thresholds."
- Enrichment & control: "manual as well as automated enrichments, with configurable approval processes, full audit trail and role based security."
- Lineage: "full data versioning and lineage – from the moment a dataset enters the system until the final values are populated inside the submitted reports... Processing preserves data lineage at each functional stage."
- Calculations: "integration of regulatory calculations, such as highly optimized regulatory capital or liquidity computations and regulatory reporting."
- Deployment: on-cloud and on-premise; single-tenant SaaS; value-added services (platform management, upgrades, testing, fixes).
- Suite integration: OneSumX for Risk Management and Business Analytics alongside.

### deltaconX (via Temenos marketplace) — Evidence Layer A (partner listing)

- "Full-stack regulatory reporting... straight-through processing, detailed pre-submission validation, real-time reporting visibility, and remediation management."
- Regime breadth: "One platform supports global regulations including EMIR, MiFID II/MiFIR, SFTR, Dodd-Frank, FinfraG, MAS, ASIC, and REMIT" — transaction-reporting-weighted.
- Submission transparency: "Interactive dashboards deliver real-time status tracking, complete data lineage, and full change history for every submission... accountability, audit readiness."
- Integration: "straightforward integration into existing core banking and trading systems."

### Temenos Regulatory Compliance — Evidence Layer A (embedded variant)

- "All regulatory compliance solutions are pre-integrated into our software"; "The CRS module in the Temenos Core ensures compliance with OECD standards for client reporting"; FATCA/CRS/MiFID II/GDPR/PSD2 support; Regionalized Solutions (country model banks).
- Shows the embedded-in-core-banking form: compliance/reporting modules shipped inside the core banking product rather than as a standalone platform.

### Vermeg — Product Mismatch (recorded)

- Root site (fetched 2026-09-10) shows only Capital Markets (Colline, Megara, Optimizer) and Insurance (Soliam, Solife) solutions; no regulatory reporting product.
- Regnology news confirms Vermeg's regulatory reporting division (AGILE, ex-Lombard Risk) was acquired 2024-11-25; Vermeg quote: "VERMEG will concentrate on our core strengths in Collateral Management and Insurance."
- Former AgileREPORTER identity survives in Oracle's official docs as the integrated "last mile" submission tool.

## Cross-product Comparison

| Dimension | Regnology | Nasdaq AxiomSL | Oracle OFSAA + AgileREPORTER | OneSumX RegRep | deltaconX | Temenos Compliance |
|---|---|---|---|---|---|---|
| Center | reporting lifecycle "from data ingestion to submission" | "data capture to final filing" on one data-integrity platform | "data capture through submission" in integrated environment | data mapped to "a single and complete regulatory library" | "full-stack" STP with pre-submission validation | compliance modules pre-integrated in core banking |
| Report as unit | reporting obligations + submissions tracked; schedulers | tasks/participants/obligations; project management | "creation and submission of regulatory returns"; DGRR "maintain and track regulatory report submissions" | reports populated "inside the submitted reports" | "every submission" with status + change history | CRS client reports (module scope) |
| Data model | granular multi-jurisdictional model, "map once, report many"; ingestion at granular/results/report level | unified data model, native-format ingestion from any source | OFSDF industry data model + Data Integration Hub | "global, standardized and flexible data model" | integrates with core banking/trading systems | core banking's own data |
| Calculations | capital, liquidity, credit, risk calculations in-engine | calculation engines + extensible data dictionaries; RWA, net capital | regulatory computations in OFSAA; AgileREPORTER for forms | "highly optimized regulatory capital or liquidity computations" | not emphasized (transaction reports) | not emphasized |
| Validation | granular + lifecycle validation, data controls | validation in STP; strong validation workflows (broker-dealers) | "validation checks" in AgileREPORTER | cross validation between regimes; variances vs thresholds; ledger/subledger reconciliation | "detailed pre-submission validation" | module-level compliance checks |
| Workflow/sign-off | task management, exception-based processing | automated workflows, KPI tracking | "form and workflow tool"; approvals (CRS "bulk reports and approvals") | "configurable approval processes", role-based security | remediation management | pre-integrated processes |
| Submission | API connectivity; regulator feedback automation | "final filing" | "automatic submission"; e-file (CRS) | submission as lineage endpoint | submissions with status tracking | e-filing inside module (CRS) |
| Regulatory content | multi-jurisdictional coverage; shields from regulatory change | embedded Regulatory Rule reference; Regulatory Change Managed Service | integration packs per regulator | SMEs monitor ~30 countries; regulatory library | multi-regime platform (EMIR…REMIT) | country/regional compliance content |
| Lineage/audit | source-to-submission lineage, audit trails, BCBS 239 | full traceability, drilldowns | "explain and justify a number" | data versioning + lineage each stage | complete data lineage + change history | — |
| Regime families | prudential, statistical, granular, disclosure; banks, broker-dealers, insurers | financial + risk + transaction + GSD + ESG; banks, BDs, asset managers | US Treasury/Fed/EBA packs; CRS | FINREP, COREP, BCAR, FRY-14, MiFID II, statistical, AnaCredit, Smart Cubes | EMIR, MiFIR, SFTR, Dodd-Frank, FinfraG, MAS, ASIC, REMIT | FATCA/CRS/MiFID II client reporting |
| Deployment | cloud-first SaaS (rCloud/Ascend) | RegCloud SaaS + on-prem heritage | on-prem suite + integrated partner tool | on-cloud + on-prem, single-tenant SaaS | platform + expert services | embedded in core banking |
| Dual-sided | yes — Supervisory Hub/AEOI for regulators | serves "financial regulators" (FAQ) | no | no | no | no |

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

1. **The regulatory report/return as the managed unit of record** — a persistent, identified report bound to a specific regulator/authority, a reporting period/reference date, a legal entity, and the regulator's prescribed output structure (template/taxonomy), carried through a lifecycle that ends in submission and tracks acceptance/feedback. Remove → generic report templates / BI output.
2. **Regulatory data production** — the institution's own data (GL, core banking, trading, risk, policy systems) mapped and computed into the regulator's defined data points and report cells, under regulatory formulas where the regime requires. Remove → document assembly or manual form filling; not a platform.
3. **Regulatory validation** — checks of the populated report against the regulator's rules (plus internal quality controls) that gate submission. Remove → unvalidated output; not a compliance instrument.
4. **The submission handoff** — generation of the regulator-ready submission in the required format/channel and tracking of its acceptance, with amendment/resubmission on rejection or correction. Remove → reporting tool with no filing semantics (the §13 seam).

Jointly-held load-bearing: 1 alone = template library; 2 alone = data mapping tool; 3 alone = validation engine; 4 alone = file transfer; 1+2 without 3 = report generator; 1+3 without 2 = validation over nothing; 2+3 without 1 = data-quality tooling; 1+2+3 without 4 = internal regulatory analytics.

### L1 — Common Mature Structure

- Vendor-maintained regulatory content library (templates, taxonomies, validation rule packs per regime/jurisdiction; expert-monitored regulatory change feeding updates)
- Regulatory calendar / obligation tracking (reporting cycles, deadlines, submission status)
- Workflow with review/approval sign-off, role-based security, segregation of duties
- Data lineage and cell-level drill-down; audit trail; data versioning
- Exception/variance handling: manual adjustments with justification, variance analysis, ledger/subledger reconciliation, cross-regime validation
- Multi-regime / multi-jurisdiction / multi-entity operation from a shared data model ("map once, report many")
- Amendment/restatement handling; regulator feedback/query handling
- Data quality controls and attestation

### L2 — Variant / Optional Structure

- Regime-family focus: prudential banking (COREP/FINREP/call reports), statistical/monetary (central bank returns), granular (AnaCredit-class), insurance (Solvency II-class), securities/transaction reporting (EMIR/MiFIR/SFTR/Dodd-Frank class), tax information reporting (FATCA/CRS/AEOI), disclosure (Pillar 3/ESAP-class), ESG
- Deployment: on-premise, SaaS/cloud, managed services, shared utility platforms (AuRep-class shared infrastructure observed at AxiomSL)
- Data-foundation depth: platform includes its own regulatory data warehouse/model vs integration layer over existing warehouse
- Calculation depth: regulatory capital/liquidity computed in-platform vs consumed from risk systems
- Supervisor-side collection platforms (mirror side; Regnology serves both)
- Client-level (investor) tax reporting
- AI assistance (agentic AI, anomaly detection) — era-current, not definitional
- Embedded-in-core-banking form (Temenos-class)

### L3 — Vendor-specific (Research Notes only)

- ControllerView, RegCloud, Regulatory Change Managed Service (Nasdaq AxiomSL)
- RRH Ascend, rCloud, Rconnect, RGD, Supervisory Hub, Exception Monitor, KRI dashboard, Straight-Through Reporting vision (Regnology)
- OFSAA, OFSDF, AgileREPORTER, DGRR, REG REP integration packs (Oracle)
- OneSumX Regulatory Engine, Smart Cubes (OneSumX)
- deltaconX (transaction-reporting platform)
- Vendor-claimed numbers: Regnology 25,000+ calculations / 1M allocation rules / 2,000+ data controls / 10,000+ validation rules / 100+ countries; AxiomSL 90% of G-SIBs / 170+ regulators 60+ jurisdictions (elsewhere 110/55); OneSumX ~30 countries monitored; Oracle DGRR 20,000+ business terms. All marketing claims, not canonical facts.

## Historical / Market-Sample Check

- Paper-era practice: banks filled paper call-report forms from ledger data, checked against regulator instructions, and mailed the return. The defining core (report bound to regulator/period/template; data mapped into prescribed cells; validation against rules; submission with acceptance) holds — the platform digitizes each element. Passes.
- Spreadsheet-era practice: Excel-based preparation against regulator templates + validation macros + portal upload. Core holds with manual machinery. Passes.
- Regional/national vendors and country-specific tools (single-regime reporting tools) satisfy the core with narrower scope. Passes.
- The definition does not depend on cloud, AI, granular data models, XBRL, or vendor-maintained content packs. No overfit to the current consolidated market.

## Vendor-specific Findings

See L3 above. Additional structural observations:
- Category consolidation under Regnology (AGILE 2024-11, Wolters Kluwer FRR 2025-12, Moody's RR & ALM, Fed Reporter announced, CG3-1) — market-structure fact, not definitional.
- Oracle's regulatory reporting is architected as data foundation + per-regulator integration packs + a partner "last mile" tool (AgileREPORTER) — a suite-plus-specialist pattern.
- AxiomSL sells the same platform to supervisors (FAQ mentions financial regulators) and to mid-sized banks via a prescribed-data-dictionary SaaS package.
- Shared utility model exists: AuRep (Austria) runs consolidated regulatory reporting infrastructure for the Austrian industry on AxiomSL technology.

## Boundary Findings

1. **vs Reporting Platform (§13) — DISCHARGED from this side.** Confirmed adjacent, keep both. Seam: a regulatory reporting platform's center is regulator-bound report production + validation + submission machinery (every sampled product centers submission: "from data ingestion to submission", "data capture to final filing", "creation and submission of regulatory returns", "every regulatory submission"); a reporting platform's center is formatted output from organization data with no submission machinery and no regulator-bound templates. Remove submission + regulator-bound structure from the regulatory platform → it collapses into the §13 Type.
2. **vs Financial Risk Management Platform — DISCHARGED from this side.** Confirmed adjacent, often bundled, keep both. Risk platforms measure/monitor risk positions and ship regulatory content packs; regulatory reporting platforms produce and file the reports. Evidence of bundling: AxiomSL risk-analysis modules on the same platform; Regnology Risk Hub; OneSumX for Risk Management integration. Centers remain distinct.
3. **vs Actuarial Modeling Platform — DISCHARGED from this side.** Centers distinct (liability/product projection feeding capital and risk processes vs report production/submission machinery). Adjacency stands.
4. **vs Tax Compliance Platform / Corporate Tax Management.** Adjacent. Tax compliance computes the institution's own tax liabilities and files tax returns; regulatory reporting produces supervisory/statutory information reports. FATCA/CRS/AEOI sits between: information reporting about clients' accounts, not own tax liability — sampled as a variant inside this family (Oracle CRS e-file; Regnology Tax Hub/AEOI; Temenos CRS module; AxiomSL FATCA/CRS).
5. **vs Regulatory Change Management (§11).** Adjacent. RCM tracks regulatory changes and their impact; regulatory reporting platforms consume updated content packs, and some offer managed regulatory-change services (AxiomSL). Different centers.
6. **vs Financial Consolidation Platform.** Upstream feeder. Consolidation produces group financial statements; FINREP-class regulatory reports consume them. Distinct objects (consolidation scope/eliminations vs report cells/submissions).
7. **vs Regulatory Information Management (§22, life sciences).** Name collision only. RIM's objects are regulated products, dossiers, health-authority submissions; this Type's objects are supervisory returns of financial institutions. Different domain, different objects, no shared core.
8. **vs statutory financial filing (Workiva-class SEC/XBRL filing tools).** Adjacent, not sampled deeply. Corporate financial-statement authoring/tagging for public-company filings vs supervisory return production for regulated financial institutions. Different primary object (the annual/quarterly financial statement vs the periodic supervisory return family).
9. **Supervisor-side collection platforms.** Mirror variant sharing the report/taxonomy/validation objects (Regnology Supervisory Hub; AxiomSL FAQ mentions regulators as audience). This leaf is centered on the regulated side (§08 placement); supervisor-side collection noted as the mirror pole, not a separate directory leaf.
10. **Transaction reporting.** Within-family variant: event-level reporting of trades (EMIR/MiFIR/SFTR-class) vs periodic position/prudential returns. Some vendors specialize in it (deltaconX); general platforms carry it as a module (AxiomSL Trade & Transaction; Regnology Transaction Reporting).

## Uncertainties

- Exact submission mechanics per product (direct API vs portal upload vs file export) vary by regulator channel; accessible sources confirm both "automatic submission" (AgileREPORTER) and API-based submission with regulator-feedback automation (Regnology), but per-jurisdiction channel details are unverified. Kept general in the final document.
- Whether every product supports direct transmission or some only produce regulator-ready files — evidence suggests both patterns exist; not resolved per product.
- All vendor-claimed numbers unverified (recorded as claims).
- Degree to which disclosure publishing (Pillar 3/ESAP) belongs to this Type vs a separate disclosure-publishing Type — sampled products include it as a module (Regnology Disclosure Hub; AxiomSL ESG); treated as variant.
- No historical product sampled directly (paper/spreadsheet-era practices reasoned, not fetched) — limitation recorded; core definition kept implementation-neutral.

## Final Synthesis

A Regulatory Reporting Platform is the regulated financial institution's system of record for producing and filing supervisory reports. Its defining core is four jointly-held structures: the regulatory report as a managed unit (bound to regulator, period, legal entity, prescribed template/taxonomy, lifecycle to submission and acceptance); regulatory data production (mapping/computing institution data into the regulator's defined data points); regulatory validation gating submission; and the submission handoff with acceptance tracking and amendment. Around this core, mature products add vendor-maintained regulatory content, obligation calendars, sign-off workflow, lineage/audit, exception and variance handling, and multi-regime/multi-entity operation. The Type's boundary is sharp against BI reporting (no submission machinery), risk platforms (measurement vs filing), tax compliance (own liability vs supervisory information), and life-sciences RIM (name collision only). The market is consolidating around a few platforms serving both regulators and the regulated, but the canonical core is implementation-neutral and holds for paper-era and spreadsheet-era practice.
