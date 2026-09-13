# Research Notes — ESG Reporting Platform

## Research Goal

Understand what an "ESG Reporting Platform" actually is as a software Type: what object it manages, what its defining loop is, what is definitional vs merely common in the current market, and where its boundaries sit against the neighboring §21 cluster (ESG Management Platform, ESG Disclosure Management, Sustainability Management Platform, Carbon Accounting Platform, Circular Economy Platform) and against generic reporting/BI and environmental management systems.

## Initial Boundary

- Hypothesis: an organization-side platform that holds the organization's ESG (environmental / social / governance) performance data, organizes it against disclosure frameworks / report structures, and produces external report deliverables through a collection → validation → approval → publication cycle.
- Most likely confusions:
  - ESG Management Platform / Sustainability Management Platform (§21 siblings, unprocessed) — program/data operations vs disclosure production.
  - ESG Disclosure Management (§21 sibling, unprocessed) — filing/regulatory-submission machinery vs report production.
  - Carbon Accounting Platform (§21, processed) — emissions inventory computation vs multi-domain disclosure.
  - Reporting Platform / BI (§13) — generic report generation without disclosure semantics.
  - Environmental Management System / EHS (§21) — operational compliance data vs external disclosure.
- Prior passes in this atlas recorded seam hypotheses this pass should address:
  - carbon-accounting-platform: "disclosure-centric Types start from the report/disclosure requirement; carbon accounting starts from measurement."
  - circular-economy-platform: circularity-measurement pole sits near the ESG-reporting seam; joint review recommended.
  - climate-risk-management: disclosure-led pole "dissolves into ESG disclosure management."

## Research Questions

1. What is the central object of record — metrics? data points? report sections? frameworks?
2. What is the end-to-end workflow: how does data become a published disclosure?
3. How do frameworks/standards (GRI, SASB, ESRS/CSRD, ISSB, TCFD, CDP, regional regulations) function inside the product — templates? libraries? questionnaires? datapoint lists?
4. What collection machinery exists (requests, surveys, integrations), and what roles contribute?
5. What review/approval/audit machinery makes the output trustworthy (assurance posture)?
6. What deliverables are produced (report documents, questionnaire responses, tagged filings)?
7. Where is the boundary vs carbon accounting (measurement-first), vs ESG/sustainability management (program-first), vs disclosure management (filing-first)?

## Representative Products

Selected for market representation, documentation accessibility, and distinct product philosophies / carriers:

| Product | Philosophy / carrier | Segment | Evidence level |
|---|---|---|---|
| Workiva | reporting-platform DNA: ESG beside financial/statutory reporting; document + connected data; filer-grade | enterprise / public filers | A (official solutions page, deep) |
| Novisto | ESG data-management-first pure-play; ratings-response strong (CDP, S&P Global CSA) | mid/enterprise | A (official site) |
| Position Green | European regulatory-led pure-play (CSRD/ESRS, EU taxonomy, VSME, SFDR, HRDD) | mid/enterprise | A (official site) |
| Quentic (figbytes.com now resolves here) | EHS-suite-carried sustainability/reporting module | mid-market/industrial | A (official sustainability page) |
| Plan A | carbon-first platform with a reporting leg — boundary-informing sample, NOT a representative | SMB/mid | A (official site) |

Deliberately not sampled / abandoned:
- Diligent ESG (GRC-suite carrier): both URL attempts 404; abandoned per network rules. Carrier posture noted as unverified.
- Plan A treated as boundary evidence only (self-describes carbon accounting / decarbonisation; reporting is one leg of a carbon journey).
- Enablon/Sphera/Intelex (suite-carried): no reachable ESG-reporting-specific surface in budget; not claimed.

## Sources

All fetched 2026-09-08.

- Workiva — "ESG Software & Reporting Platform" — https://www.workiva.com/solutions/esg-reporting (fetched; deep platform structure documented on page)
- Workiva help center — https://support.workiva.com/help/esg-program (404) and https://support.workiva.com/help/ (404); abandoned after 2 attempts
- Novisto — https://www.novisto.com/ (fetched; /product/report URL SPA-fell back to homepage — same content)
- Position Green — https://positiongreen.com/ (fetched); /use-cases/mandatory-reporting guess 404 (abandoned after 1 attempt)
- Quentic Sustainability — https://quentic.com/software/sustainability (fetched); figbytes.com root now serves Quentic (domain/acquisition change observed — recorded, no FigBytes-specific claims made)
- Plan A — https://plana.earth/ (fetched; boundary-informing only)

Source-access limitation: no product's help-center/user-guide operational documentation was reachable (404s, SPA fallbacks). All capability claims below are anchored to official product/marketing pages (Tier 2). No precise numeric limits, defaults, or step-level procedures are asserted. Marketing-page claims (e.g., efficiency percentages, metric counts) are recorded as vendor claims only.

## Product Observations

### Workiva (evidence layer A)

- Self-positioning: "ESG Software & Reporting Platform"; "Transform ESG reporting with transparency, in one integrated and intelligent platform." Verdantix leader claims in both "ESG Reporting and Data Management Software" and sustainability management categories (vendor-quoted).
- Platform structure (page tabs, directly observed): Explore ESG Frameworks → Create a Sustainable Strategy → Collect ESG Data → Connect Your Teams → Report on Demand → Ensure Trust and Audit-Readiness.
- **ESG Explorer**: "Browse Workiva's ESG Explorer and select from pre-built ESG frameworks and standards to measure what matters to you... ensures your governance model remains compliant across multiple global standards." Frameworks shown: SASB, GRI, TCFD (with TCFD recommendations as discrete items: Governance / Strategy / Risk Management). Pre-built templates; "ESG Explorer lets you compare multiple guidelines all in one place."
- **Strategy/materiality**: "Digitise your approach to ESG planning, materiality assessments, and disclosures..."; topics shown: Emissions, Risk Management, Employee Inclusion, Governance, Materiality Assessment; SASB accounting metrics shown as codified items (e.g., FB-PF-440a, CG-AA-440a.1, CG-BF-130a) — framework content exists at metric level.
- **Collect**: "Sync a full range of ESG data seamlessly via APIs, reduce time and error through process automation, and harness a connected ESG hub for benchmarking and interoperability."
- **Teams**: "Empower global teams to collaborate on ESG reporting at once on one platform... Grant permissions on a granular level to manage what you measure."
- **Report on Demand**: "Share progress toward ESG goals with both your internal and external stakeholders... linking evidence of your ESG results in your source reports... board-ready reporting by linking evidence directly to source reports for high-fidelity disclosure. Bring all graphic, narrative and layout elements into Workiva with our enhanced Designed Reporting capabilities while keeping track of comments and version control throughout your review cycles."
- **Trust/audit**: "Capture ESG audit history while streamlining external assurance. Validate ESG data in SEC-ready, XBRL format for investor-trusted, board-ready, and audit-ready data."
- Adjacent uses in same platform (page): SOX Compliance, SEC Reporting, Global Statutory Reporting, Management Reporting, Internal Controls Management, Policy and Procedures — ESG sits beside financial/statutory reporting (reporting-platform carrier confirmed).
- "Financial-grade rigor" framing repeated ("Earn trust with ESG reporting solutions that apply financial-grade rigor within a single, unified platform").

### Novisto (evidence layer A)

- Self-positioning: "Next-Generation Sustainability Management Software" / "Sustainability Management Software — For confident decisions and disclosures... Own your ESG narrative with efficiency and insights from your sustainability data, workflows, and reporting."
- Product split into: **Collect** ("Streamline your ESG data collection with automated processes"), **Manage** ("centralized System of Record and customized metrics"), **Report** ("ESG reporting becomes easier with Novisto's all-in-one solution").
- "ESG data management — Finance-grade ESG data... Backed by curated metrics, approval workflows, embedded audit trails, and more."
- "ESG reporting — Easily navigate the evolving reporting landscape. **Embed live data into your reports to align and collaborate on narrative.** ... **Collect once, report to many**."
- Taxonomies (named framework content): CSRD, S&P Global CSA, SASB, GRI, CDP, SB 261, SB 253.
- Materiality Assessment: "Guided workflow to identify impacts, risks, and opportunities."
- Carbon Management module: "Comprehensive carbon accounting and Net-Zero strategy." Acquired Minimum "to launch the industry's first end-to-end carbon & sustainability platform" (vendor news).
- Ratings-response use cases evidenced by customer quotes: CDP questionnaire assistance; "We leveraged Novisto for the S&P Global Corporate Sustainability Assessment. We cut down the time... by 50%." (vendor-published customer quotes)
- Other: "Benchmark against peers, set targets, and monitor progress"; "700+ average number of metrics tracked per client"; "50% average efficiency gain in submitting disclosures" (vendor-claimed stats); AI "for ESG data automation and audit-readiness"; "enterprise-grade security and bulletproof data governance."
- Customer story: "Centralizing Global ESG Data: C.A.T.'s Shift from Spreadsheets to Strategy — centralized ESG data across 14 regions... automate reporting, improve ISS scores, and win business with audit-ready data."

### Position Green (evidence layer A)

- Self-positioning: "ESG Software That Turns Sustainability Into Business Impact"; "automate reporting, track and reduce emissions, benchmark against peers... all in one place."
- Platform core capabilities: Data management, Controlling and audit, Embedded AI, Benchmarking, Materiality assessment, Integrations.
- Use cases: **Carbon management** (Measure, report, and decarbonize Scopes 1–3), **Mandatory reporting** ("Simplify reporting and stay audit-ready"), **Supplier management** ("Collect data, evaluate suppliers, and identify risk"), **Voluntary reporting** ("Build trust with investor-grade insights"), **Group reporting** ("Consolidate and track data across entities"), Drive business value.
- Frameworks offered: **ESRS reporting, VSME reporting, EU taxonomy, HRDD reporting, SFDR reporting, GRI reporting** — European regulatory-led content set.
- "One single source of truth — Enter data once and reuse it everywhere with one sustainability data hub. Easily connect all your apps and systems for real-time visibility."
- "Full ESG coverage... Scale at your own pace with a flexible, modular design."
- "Continuously updated by Europe's leading sustainability experts so you can navigate regulatory shifts with minimal disruption." (framework content maintenance as a service)
- "Enterprise-grade by design — Configured to support complex org structures and reporting setups."
- Marketing stats: "Save up to 60% reporting time"; "70% faster reporting year on year"; "50% reduction in manual admin" (vendor claims).

### Quentic Sustainability (evidence layer A; carrier = EHS suite; figbytes.com legacy)

- Domain note: figbytes.com (a long-standing self-described "ESG reporting platform" vendor) now resolves to Quentic (EHS & sustainability software under AMCS). Recorded as market-consolidation evidence; no FigBytes-specific product claims.
- Quentic Sustainability page: "transforms complex Climate, Water, and ESG information into sustainability reporting and actionable insights by capturing operational and supplier data in one central, secure, cloud-based platform that **manages strategy, automates framework reporting, and simplifies stakeholder engagement**."
- Features: **Carbon accounting** ("establish a credible greenhouse gas emissions (GHG) inventory with flexible data tools and pre-loaded emission factors"), **Climate disclosure reporting** ("Streamline compliance reporting to climate-related risk and disclosure regulations like the SEC Climate Disclosure, CSRD, and more... audit-ready data and reporting tools"), **Scope 3 emissions management** (supplier engagement, calculation/estimation tools, data-gap handling), **Analytics & insights** (custom dashboards).
- Accreditations (framework-content posture): "CDP Accredited Solutions Provider", "accredited solution provider of GRI", "'Friend of EFRAG'".
- Suite context: one module inside an EHS & sustainability platform (health & safety, hazardous chemicals, environmental management, etc.). Quentic Core: "Control actions and documents."
- Benefits framing: "Reduce reporting burden — Save time and effort with analytics, benchmarking, and gap analysis tools that reduce errors and standardize processes." "Simplify regulatory compliance — Meet the latest regional, industry, and global requirements with fully-auditable, accurate reports." "Visualize sustainability strategy... track progress towards your targets."
- Verdantix Green Quadrant ESG & Sustainability Reporting Software 2025 quoted on page: "strong user adoption, robust data management, and configurability... suitable for large multinational organizations facing complex reporting and regulatory requirements."

### Plan A (boundary-informing sample only, evidence layer A)

- Self-positioning: "Carbon Accounting Software by Plan A"; platform = 1. Carbon accounting, 2. Carbon reporting ("Disclose your sustainability progress with integrated carbon footprint reports"), 3. Decarbonisation.
- Carbon-first: measurement → reporting → reduction. "Decarbonisation-first" is an explicit principle.
- Reading: an emissions platform ships a *reporting leg*; the reporting leg serves the carbon program. This is the carbon-accounting-platform shape (consistent with the processed carbon-accounting pass), not the ESG reporting center of gravity. Useful boundary specimen.

## Cross-product Comparison

| Finding | Workiva | Novisto | Position Green | Quentic | Evidence |
|---|---|---|---|---|---|
| Centralized ESG data of record ("single source of truth", system of record) | ✓ (Collect ESG Data, ESG hub) | ✓ ("centralized System of Record") | ✓ ("one sustainability data hub") | ✓ ("one central, secure, cloud-based platform") | B (4/4) |
| Framework/standard content as first-class organizing layer | ✓ (ESG Explorer, SASB/GRI/TCFD, templates) | ✓ (taxonomies: CSRD/CSA/SASB/GRI/CDP/SB253/261) | ✓ (ESRS/VSME/EU taxonomy/HRDD/SFDR/GRI) | ✓ (CDP/GRI/EFRAG accreditations; framework reporting automation) | B (4/4) |
| Report/disclosure deliverable produced from live data | ✓ (Designed Reporting, board-ready, evidence-linked) | ✓ ("embed live data into your reports... narrative") | ✓ (mandatory + voluntary reporting) | ✓ (sustainability reporting outputs) | B (4/4) |
| Audit trail / audit-readiness / assurance posture | ✓ (audit history, external assurance, XBRL) | ✓ (embedded audit trails, audit-readiness) | ✓ (Controlling and audit; "stay audit-ready") | ✓ ("fully-auditable"; "audit-ready data") | B (4/4) |
| Collect-once, report-many / multi-framework reuse | ✓ ("compliant across multiple global standards"; compare guidelines) | ✓ (explicit slogan) | ✓ ("Enter data once and reuse it everywhere") | ✓ ("automates framework reporting") | B (4/4) |
| Collection machinery to contributors (requests/surveys/integrations) | ✓ (APIs, process automation) | ✓ (Collect; automated processes) | ✓ (Integrations; supplier data collection) | ✓ (capturing operational and supplier data) | B (4/4) |
| Materiality assessment | ✓ (template) | ✓ (guided workflow) | ✓ (core capability) | — (not observed on page) | B (3/4, common) |
| Carbon accounting included | topic shown; engine not observed | ✓ (module + acquisition) | ✓ (use case) | ✓ (feature) | B (3/4, common module — not defining) |
| Ratings/questionnaire responses (CDP, CSA, ISS) | — (not observed on page) | ✓ (CDP, S&P CSA, ISS quote) | — | ✓ (CDP accredited provider) | B (2/4, common) |
| Benchmarking vs peers | ✓ ("connected ESG hub for benchmarking") | ✓ | ✓ | ✓ (benefits list) | B (4/4, common) |
| Targets/progress tracking | ✓ ("Share progress toward ESG goals") | ✓ ("set targets, monitor progress") | ✓ (goals framing) | ✓ ("track progress towards your targets") | B (4/4, common) |
| Supplier / value-chain data collection | — (not observed on page) | ✓ (carbon/Scope 3 posture) | ✓ (Supplier management) | ✓ (supplier data, Scope 3) | B (3/4, common) |
| XBRL / regulator-ready tagged filing | ✓ (SEC-ready XBRL) | — | — | — | A, single-product → variant (filer pole) |
| Group/entity consolidation | ✓ (global statutory adjacency) | ✓ (14-region case) | ✓ (Group reporting) | — | B (3/4, common) |
| AI assistance | ✓ (Workiva AI nav) | ✓ (Novisto AI) | ✓ (Embedded AI) | ✓ (Quentic AI) | B (4/4, era-current — not defining) |
| Permissions/collaboration across teams | ✓ (granular permissions) | ✓ (approval workflows) | ✓ (enterprise org structures) | ✓ (workflows, stakeholder engagement) | B (4/4, common) |
| Carrier: standalone pure-play | — (reporting-suite native) | ✓ | ✓ | — | variant axis |
| Carrier: suite-carried (EHS / financial reporting / GRC) | financial-reporting suite native | — | — | ✓ (EHS suite) | variant axis |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately minimal)

An ESG Reporting Platform is the organization's system for producing external sustainability disclosures. Three jointly-held structures; remove any one and the product stops being recognizable:

1. **The organization's ESG performance data of record** — quantitative metrics and qualitative disclosures spanning environmental, social, and governance domains, scoped to the organization (its entities/sites) and reporting periods, held as managed records. Remove → document editor or BI tool with nothing ESG of record behind the report.
2. **The disclosure structure as organizing layer** — the report is assembled against a defined structure of disclosure items (framework disclosures/datapoints, report sections, questionnaire items) that the data is mapped into. Remove → generic ESG data management/warehouse, or a template publisher with no disclosure mapping.
3. **The disclosure deliverable produced from the record** — an external-facing artifact (report document, questionnaire response, filing-ready output) generated/refreshed from the mapped data, with the published items traceable to the underlying record. Remove → compliance checklist / data-mapping tool with no deliverable.

Jointly-held is load-bearing:
- 1 alone = ESG data management (the ESG-Management-platform seam).
- 2 alone = framework content library (content product, not a platform).
- 3 without 1+2 = document template generator.
- 1+2 without 3 = gap-analysis/checklist tool.
- 2+3 without 1 = template report generator with no data of record.
- 1+3 without 2 = generic report generation over ESG data (BI/document generation), below the Type.

Deliberately NOT in L0: cloud delivery, framework *libraries* as digital content (the abstract requirement is only that a disclosure structure exists), GRI/ESRS/SASB by name, materiality assessment, carbon engine, XBRL, AI, benchmarking, targets, approval workflows, dashboards.

### Historical / market-sample check (§24)

- Thin ancestor: mid-2000s sustainability reporting — ESG data collected in spreadsheets (data of record), report outline + GRI content index printed in the report back-matter (disclosure structure), manual collection → consolidation → review → publication (the loop), Word/InDesign deliverable. Satisfies the three-leg core with zero cloud/AI/XBRL. Confirms the core is era-agnostic.
- Regional check: Japanese/European voluntary reporters under national guidelines, pre-CSRD EU reporters, US reporters under SASB-only — all satisfy "disclosure structure" leg without naming any specific standard. Confirms no standard is definitional.
- Pre-ESG label check: "sustainability report"/"corporate responsibility report" era (late 1990s–2000s, before "ESG" was market vocabulary) — same structure. The Type predates its label.

### L1 — Common Mature Structure (very common in current products, not defining)

- framework/standards library with pre-built mappings, updated as standards evolve (vendor-maintained content)
- data collection machinery: requests/requests-with-deadlines to contributors, surveys, system integrations (ERP/HRIS/utility), supplier questionnaires
- metric library (curated, customizable metrics with owners, units, periods)
- validation/approval workflows (reviewer/approver sign-off before disclosure)
- evidence attachment and audit trail; assurance support
- materiality assessment workflow
- targets and progress tracking
- benchmarking (peer comparison)
- dashboards/analytics
- cross-team permissions and collaboration
- group/entity consolidation for multi-entity organizations

### L2 — Variant / Optional

- XBRL/tagged regulator-ready filings (public-filer pole — Workiva observed; likely the esg-disclosure-management center)
- ratings-response specialization (CDP/S&P CSA/ISS questionnaires — Novisto-observed strength)
- regulatory-led (CSRD/ESRS/EU taxonomy/VSME/SFDR/HRDD — Position Green; SEC Climate Disclosure — Quentic) vs voluntary-led (GRI/SASB narrative) vs ratings-led
- carbon accounting engine depth (none → module → full Scope 1–3 + decarbonisation)
- group reporting consolidation depth
- carrier: standalone pure-play vs EHS-suite-carried (Quentic) vs financial-reporting-suite-native (Workiva) vs GRC-suite-carried (Diligent — unverified)
- region: European regulatory pole vs North American (SEC/California SB 253/261) pole vs global voluntary
- segment: enterprise filer-grade vs mid-market vs SMB self-serve
- data-first vs document-first center (data hub + generated report vs authoring-grade document workspace)

### L3 — Vendor-specific (research notes only)

- Workiva: "ESG Explorer" name, "Designed Reporting" branding, SEC-ready XBRL validation, platform adjacency list (SOX/SEC/statutory), "financial-grade rigor" positioning, Verdantix leader claims.
- Novisto: "Collect once, report to many" slogan, "700+ average metrics tracked per client", "50% efficiency gain" claims, Minimum acquisition, C.A.T. 14-region case, ISS-score improvement quote, taxonomies page naming.
- Position Green: "Save up to 60% reporting time" / "70% faster reporting YoY" / "50% less manual admin" claims, VSME/HRDD framework list specifics, "Europe's leading sustainability experts" content-maintenance framing.
- Quentic: CDP/GRI/EFRAG accreditation framing, figbytes.com domain absorption, Verdantix quote, EHS module lattice, "Friend of EFRAG" designation.
- Plan A: "70% faster data management", "130+ days saved", "20x reporting speed" claims, TÜV/GHG-Protocol certification framing (carbon-first pole).

## Vendor-specific Findings

See L3 above. None of these enter the canonical core. XBRL is the only L3 item with Type-level relevance (it marks the filer pole and the seam to ESG Disclosure Management).

## Boundary Findings

1. **vs Carbon Accounting Platform (§21, processed)** — seam CONFIRMED from this side, consistent with that pass's recorded language. Carbon platform: system of record for the emissions *inventory* (activity × factor computation); ESG Reporting Platform: system for producing *disclosures* across E+S+G. Direction differs: carbon pass = "starts from measurement"; this pass = "starts from the disclosure requirement and works backward to data" (observed: Workiva's flow begins with framework selection; Novisto's "collect once, report to many"). Disclosure is an output of the carbon platform (L1 there); carbon data is one input domain here. Boundary-informing specimen: Plan A (carbon-first, reporting as a leg) belongs to the carbon side.
2. **vs ESG Management Platform / Sustainability Management Platform (§21 siblings, unprocessed)** — hypothesis: management center = ongoing program/data/goals operation; reporting center = disclosure production. The sample shows the seam is NOT exclusive capability: every sampled product blends program management and reporting (Novisto literally brands itself "Sustainability Management Software" while selling a Report pillar; Quentic = "sustainability management software" with disclosure features). Center-of-gravity test required; joint review flag recorded for STATUS.
3. **vs ESG Disclosure Management (§21 sibling, unprocessed)** — hypothesis: disclosure management = regulatory-filing machinery (tagged/XBRL filings, regulator submissions, versioned disclosure documents). Workiva straddles: ESG reporting with SEC-ready XBRL inside a financial-reporting-native platform. Joint review flag; the filer pole is the shared territory.
4. **vs circular-economy-platform (§21, processed)** — flag DISCHARGED from this side: keep-both. Circular products' material-loop objects (traceability, secondary-material identity) appear in ESG reporting, if at all, as data domains feeding E-metrics; the loops do not overlap with the disclosure-production core. No merge.
5. **vs Reporting Platform / BI (§13)** — generic BI generates reports from data but has no ESG domain semantics, no disclosure-structure mapping, no collection/assurance machinery. Remove the E/S/G domain scope + disclosure mapping → generic reporting; that is the removal test in reverse.
6. **vs Environmental Management System / EHS (§21)** — EMS/EHS centers operational compliance (monitoring, permits, incidents) as data *producers*; ESG reporting consumes/consolidates for external disclosure. Quentic demonstrates suite-carried coexistence of both — evidence they are distinct centers, not one Type.
7. **vs Regulatory Reporting Platform (§08)** — financial/regulatory filings center on prudential/legal filing obligations of financial institutions; ESG reporting centers sustainability performance disclosure for general stakeholders. Adjacent; XBRL-tagged sustainability filings are the convergence territory (→ ESG Disclosure Management flag above).
8. **vs Governance/board reporting tools** — governance metrics are one input domain; board reporting is an output surface. Neither is the center.

## Uncertainties

1. No operational (help-center-level) documentation was reachable for any sample. All workflow claims are capability-level; no step-level procedures, numeric limits, or defaults asserted. Assertion strength reduced accordingly.
2. Diligent (GRC-suite carrier) unverified — the fourth carrier pole rests on market knowledge only and is marked as such; not used in evidence.
3. Whether materiality assessment should be L1 or L2: 3/4 observed → held as L1 (common), not defining.
4. The exact L0 of the two unprocessed siblings (esg-management-platform, esg-disclosure-management) is unknown; seams are hypotheses pending joint review.
5. Segment spread downward (SMB self-serve ESG reporting) not directly sampled; assumed from market structure (Plan A-class carbon tools, Quentic mid-market posture), not asserted as evidence.
6. Social/governance data depth varies across the sample (carbon-heavy evidence); the "S" and "G" legs of the data of record are evidenced mainly by topic lists (Employee Inclusion, Governance, DEI data collection) rather than feature detail — held at concept level.

## Final Synthesis

An ESG Reporting Platform is an organization-side platform whose defining loop runs: hold the organization's ESG performance data of record (metrics + qualitative disclosures across environmental, social, governance domains, per entity and period) → map that data into a defined disclosure structure (framework disclosures, report sections, questionnaire items) → produce and maintain the external disclosure deliverable from that record, with published items traceable to the data behind them. Mature products add framework libraries kept current by the vendor, contributor-facing collection machinery, approval workflows, evidence/audit trails, materiality workflows, targets, benchmarking, and consolidation. Variants divide along carrier (pure-play / EHS-suite / financial-reporting-native / GRC-suite), regulatory posture (CSRD/ESRS-led, SEC/California-led, ratings-led, voluntary-led), and pole (data-first vs document-first; XBRL filer-grade marking the seam to ESG Disclosure Management). The Type predates its "ESG" label and any specific standard: the spreadsheet-era sustainability report satisfies the core.
