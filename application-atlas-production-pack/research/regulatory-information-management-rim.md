# Research Notes — Regulatory Information Management / RIM

## Research Goal

Understand what a Regulatory Information Management (RIM) application really is, from real products: what objects exist inside it, who uses it, how regulatory work flows through it, what rules and states matter, and where its boundaries lie against neighboring Types (pharmacovigilance, medical-device lifecycle management, regulatory change management, eTMF, ECM/document management, eCTD publishing tools).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: RIM is the regulatory-affairs department's system of record in life-sciences companies: it tracks product registrations/authorizations per market, manages dossiers and submissions to health authorities, and tracks regulatory activities (variations, renewals, correspondence, commitments).
- Likely users: regulatory affairs and regulatory operations professionals.
- Nearest neighbors: Pharmacovigilance Platform (safety cases), Medical Device Lifecycle Management (design chain), Regulatory Change Management (external regulation monitoring), eTMF (trial documents), ECM/DMS (documents), eCTD publishing tools (submission format machinery), Regulatory Reporting Platform (financial domain — name collision only).
- Unknowns: how central the registration database really is (vs document/submission-centric products); how much publishing machinery belongs inside RIM; how far beyond drugs the Type extends (devices, animal health, crop, chemicals).

## Research Questions

1. What is a "registration" / "market authorization" in a RIM system, and what data hangs off it?
2. What is the relationship between product data, registrations, dossiers, submissions, and documents?
3. What is the submission lifecycle (plan → compile → publish → transmit → acknowledge → archive)?
4. What are "regulatory activities", "correspondence", and "commitments", and how are they tracked?
5. What does "impact analysis" of a change mean in RIM?
6. Who are the users and what roles exist?
7. How do RIM products relate to safety (PV), quality, and clinical systems?
8. What regional/standards machinery appears (eCTD, NeeS, XEVMPD, IDMP, agency gateways, acknowledgments)?
9. What varies by customer tier (enterprise suite vs mid-market vs lean team)?
10. Where is the boundary against PV, device lifecycle management, RCM, eTMF, ECM, and publishing tools?

## Representative Products

Selected for market representation + documentation reachability + different product philosophies + different customer tiers:

| Product | Vendor | Pole | Tier |
|---|---|---|---|
| LifeSphere Regulatory (RIM, Submissions, Documents, Labeling, HA Interactions) | ArisGlobal | enterprise life-sciences suite, safety+regulatory as separate lines | enterprise pharma |
| EXTEDOpulse (Registration Management Hub / MPDmanager, Submission Management Hub, Document Management Hub) | EXTEDO | European heritage, modular hubs, eCTD publishing/validation heritage, also serves agencies | large pharma → SMB/CRO → agencies |
| Ennov RIM (within Ennov Regulatory Suite) | Ennov | mid-market unified compliance platform, configurable data model | mid-size pharma/devices, 450+ life-sciences customers |
| RegDocs Connect (Montrium RIM) | Montrium | lean-team, document/submission-centric RIM | small sponsors / CROs / scaling biotech |

Context (not primary samples): Generis CARA (regulated-content platform; EXTEDO's MPDmanager is "powered by CARA"); Veeva Vault RIM (market leader — unreachable this pass, see Sources).

Rejected during sampling: Freyr (regulatory *services* vendor with a platform; services-heavy, weak product documentation for this purpose), Instem (preclinical study management + SEND submission data, not RIM), IQVIA RIM Smart (404 ×2).

## Sources

Fetched 2026-09-09 (all Layer A unless noted):

- ArisGlobal — LifeSphere Regulatory overview: https://www.arisglobal.com/products/lifesphere-regulatory/ (redirects to lifesphere-regulatory-advantage page)
- ArisGlobal — LifeSphere RIM: https://www.arisglobal.com/lifesphere/regulatory/rim/
- ArisGlobal — LifeSphere Submissions: https://www.arisglobal.com/lifesphere/regulatory/submission/
- EXTEDO — home: https://www.extedo.com/
- EXTEDO — Registration Management Hub (MPDmanager): https://www.extedo.com/software/registration-management-hub
- EXTEDO — Submission Management Hub: https://www.extedo.com/software/ectd-submission-management-publishing-software
- Ennov — home: https://en.ennov.com/
- Ennov — RIM: https://en.ennov.com/solutions/regulatory/rim/
- Montrium — RegDocs Connect: https://www.montrium.com/regdocs-connect
- Montrium — RegDocs Connect features: https://www.montrium.com/regdocs-connect-features
- Generis — CARA platform (context only): https://www.generiscorp.com/

Unreachable / rejected:

- Veeva (veeva.com/products/vault-rim/, veeva.com/products/rim/, docs.veeva.com) — transport errors ×3 → abandoned per network rule. Veeva Vault RIM is the widely-cited market leader; its internal app structure is NOT asserted from memory. The only Veeva evidence in-sample is Montrium's own FAQ naming "Vault submissions or Veeva Vault submissions publishing" as platforms "designed for larger organizations" (Layer A, quoted from Montrium).
- IQVIA RIM Smart — 404 ×2 → abandoned.
- Ennov /en/ path — 404 (root en.ennov.com worked).

## Product Observations

### ArisGlobal LifeSphere Regulatory (RIM + Submissions)

Layer A observations (vendor product pages):

- Regulatory line modules: RIM, Product Compliance, Documents, Submissions, Labeling, Regulatory Analytics, Health Authority Interactions, Regulatory Intelligence. Safety (MultiVigilance etc.), Medical Affairs, and Quality are separate LifeSphere lines — regulatory and safety are distinct product families.
- RIM page headline: "Regulatory Information Management (RIM) … robust capabilities to manage regulatory planning, tracking, and registration management."
- RIM value props: standardized end-to-end workflows for regulatory planning and tracking across all markets; single source of truth — "a single area for worldwide registration activities and records"; product specifics — "support for investigational and marketed drug/medicinal products, as well as active substances, devices, site registrations and more."
- RIM features: "Regulatory Planning & Tracking — planning your submissions, as well as tracking registrations, correspondence, commitments, and other key information"; "Connectivity and Automation — work with your documents, submissions, interactions, labeling, product data and regulatory intelligence"; global submission planning/tracking centralization; localized/regional support; IDMP compliance support; interactive dashboards.
- Submissions page: "Submissions consolidates submissions and publishing workflows in a single solution that makes it simple to create, compile, and publish submissions in any format."
  - "Streamlined Submission Management — create, compile, and publish submissions starting from a global submission package and automated compilation of national submissions."
  - "Dossier Record — Maintain the current registered dossier position and its version history."
  - "Regulatory Knowledgebase — safekeep knowledge on national, regional submission requirements."
  - "Submission Reuse — compile global submissions to use as the basis for national submissions."
  - "Document Propagation — readily move documents from global to local submission dossiers."
  - Publishing support "including eCTD, NeeS, PDF, and XML"; submission automation into predefined outlines.
- Health Authority Interactions module exists as its own product page ("Automate intake and management of HA communications").

### EXTEDO (EXTEDOpulse hubs)

Layer A observations:

- Positioning: "EXTEDO's end-to-end RIM platform consists of different hubs": Registration Management Hub, Document Management Hub, Submission Management Hub, Quality Management Hub, Safety Management Hub. "For over 25 years EXTEDO's regulatory information management (RIM) solutions have been used by industry and agencies worldwide."
- Registration Management Hub = MPDmanager ("Regulatory Information and Master Data Management Solution"): "Simplifying the management of IDMP, PMS, XEVMPD, medicinal product information, and regulatory activities in a single solution."
  - Pain points named: "missing an overview of all the marketing authorizations we have in the company"; "unsure about the impact on marketing authorizations a change will have"; "overloaded doing repetitive updates on the same product for different regions."
  - Core-data model: "Product data only has to be added to the system once. Identical information such as the formula or composition of one product, does not have to be added per market authorization and region." → core product data vs per-market-authorization data.
  - Change propagation: "you can see authorizations for any changes and the products affected throughout your system. Simply change the data in the core product and the edit will reflect automatically on all related and affected products."
  - "MPDmanager covers the management of authorization details of medical devices."
  - Agency connectivity: "integrated business rules to validate data before submission based on the latest specification. The integrated gateway allows automated submission directly to the agencies"; works with EMA SPOR controlled vocabulary; "receives agency reports (1st, 2nd & 3rd ACK) in the same application linked to the relevant product information"; native EMA PMS (IDMP) download/compare/upload.
  - Activity transfer: "efficiently transfer regulatory activities, dossiers, submissions, and document attributes to eSUBmanager. Automatically link these to relevant change requests and products/applications within change control processes"; "Where Used" functionality maintains relationships between documents and submissions across hubs.
  - Regulatory Intelligence module: centralized hub for Health Authority Documents and RI data, cross-market comparison.
- Submission Management Hub: publishing (CTD, eCTD v3, eCTD v4, NeeS, eCopy, IMPD, CTA, VNeeS, ASMF and other structures), viewing, reviewing, validation; "used by over 35 regulatory authorities worldwide, including EMA" (reviewing/validation side); pharma and crop industry; on-premise or cloud.
- Safety Management Hub is a separate hub (PV seam confirmed at vendor level).

### Ennov RIM

Layer A observations:

- Regulatory Suite framing: "support the entire regulatory product lifecycle from the early planning of registration targets through to product retirement. It is an invaluable solution for regulatory activity planning, product registration management, dossier creation, dossier management and more." Suite modules: Regulatory Documents, Dossier (submission publishing), RIM, IDMP, Artwork. Quality / Commercial / Clinical / Pharmacovigilance are separate suites.
- RIM page: "Designed for Regulatory Affairs, Regulatory Operations, and registration teams, Ennov RIM centralizes product and registration data to support submissions and regulatory activities."
- Challenge framing: teams manage "more products, more markets, and more change, often across spreadsheets, shared drives, and disconnected tools… slower answers when teams need to understand registration status, submission plans, commitments, or upcoming lifecycle activities."
- "Imagine all of your regulatory information regarding products, registrations, submissions, correspondence and commitments in one centralized place."
- Core Capabilities (vendor's own list): "Centralized management of detailed product information; Market authorization and registration management; Submission and Regulatory activity planning and tracking; Automatic linkage between substances, products, registrations, activities, dossiers, submissions and documents; Correspondence and commitment tracking."
- Key Features: role-based access and action rights; configurable data model; automated email notifications; robust workflow engine; 21 CFR Part 11 compliant.
- Impact analysis: "understand which registrations may be affected by a change, for example a manufacturer update or formulation change… showing which registrations may be affected, helping teams plan the right regulatory actions."
- Dashboards: workload, deadlines, overdue activities "across products and markets"; out-of-the-box dashboards for submissions, correspondence, commitments; specialized dashboards "for use cases such as PSUR tracking and additional impact analysis views."
- XEVMPD: "Messages are compiled, validated and submitted through Ennov RIM."
- FAQ language: RIM answers "what is approved where, what is due next, and which activities are at risk"; "A RIM system is not only for tracking approvals, it supports execution"; correspondence/commitments "with clear ownership, deadlines, and status, so nothing gets lost across email threads… connects these items to products and registrations."
- Scope: "supports a broad range of product types, including pharmaceuticals and medical devices, with configurable structures to match your portfolio." RIM for Med Device product brief exists. Industries list includes pharma/biotech, medical device, animal health, healthcare, chemical, food & beverage.
- Customer-scale evidence: Septodont case study — "more than 1500 MAAs in 150 countries… 400 dossiers in just 18 months."

### Montrium RegDocs Connect

Layer A observations:

- Positioning: "The RIM software for lean teams… built for leaner regulatory affairs teams"; "the platform of choice for regulatory professionals in smaller teams"; FAQ explicitly contrasts with "larger platforms like Vault submissions or Veeva Vault submissions publishing… designed for larger organizations."
- FAQ definition (vendor's own): "A RIM system, or regulatory information management system, is designed to help pharmaceutical and medical device companies streamline the organization of regulatory submission activities, ensuring the associated documents are organized into sequences… these tools largely focus on managing the life cycle of documentation supporting regulatory submissions, complying with regulatory requirements as well as centralizing communications between sponsors and health authorities."
- Feature groups:
  - Document management: template center & file plan; real-time collaborative authoring; review & approval workflows; 21 CFR Part 11 / Annex 11 e-signatures; PDF/A conversion; eCTD & EDM reference-model taxonomies; records center for archiving.
  - Submission management: real-time submission readiness reporting; "Manage submission plans & document indexes — plan document packages and manage product dossiers… with built-in eCTD document type mapping and auto-placeholder generation"; global submission planning; export to eCTD publishers (content portability); "Product information store — store all the critical information that relates to your product as metadata within the RIM system"; "Track correspondence & commitments"; "Built-in submissions archive — bring back in previously submitted sequences… navigate through the documents using the XML backbone… reuse and reference existing submission content."
  - Administration/security/compliance: GxP alignment, GDPR, Part 11/Annex 11, SSO, access management.
- Homepage framing: "Centralize your entire regulatory operation, from submission planning to health authority correspondence."
- Note: no full registration/authorization database is advertised on the fetched pages — the product spine appears as product metadata + submission planning/status. Registration tracking depth is thinner at this pole.

### Generis CARA (context only)

Layer A (platform context): general regulated-content platform (content services, data management, process automation, compliance) serving compliance-driven industries; EXTEDO's MPDmanager is "powered by CARA". Demonstrates that RIM modules can be built on generic regulated-content platforms — the RIM identity comes from the regulatory object model, not the content platform.

## Cross-product Comparison

| Structure / capability | ArisGlobal | EXTEDO | Ennov | Montrium | Strength |
|---|---|---|---|---|---|
| Regulated product records (product data spine) | ✓ "product data" | ✓ core product data, entered once, propagated | ✓ "centralized management of detailed product information" | ✓ "product information store" (metadata) | Universal (A) |
| Registration / market-authorization records per market | ✓ "tracking registrations", "worldwide registration activities and records" | ✓ "worldwide product registration data", authorizations | ✓ "Market authorization and registration management" | thin (product metadata + submission status; no advertised authorization database) | Strong at 3/4; depth is a variant axis |
| Submissions & dossiers as managed records | ✓ Dossier Record w/ version history; global→national compilation | ✓ submission lifecycle mgmt; activities→dossiers→submissions transfer | ✓ "dossier creation, dossier management"; submission planning/tracking | ✓ submission plans, product dossiers, submissions archive w/ sequences | Universal (A) |
| Regulatory documents managed in-system | ✓ Documents module | ✓ Document Management Hub | ✓ Regulatory Documents | ✓ full DMS layer | Universal (A) |
| Regulatory activity planning & tracking | ✓ "regulatory planning, tracking" | ✓ regulatory activities linked to change requests | ✓ "Submission and Regulatory activity planning and tracking" | ✓ global submission planning, readiness reporting | Universal (A) |
| Correspondence & commitments tracking | ✓ RIM features + HA Interactions module | (gateway/ACKs; RI module) | ✓ "Correspondence and commitment tracking" | ✓ "Track correspondence & commitments" | Strong (A, 3/4 explicit + EXTEDO gateway) |
| Change impact analysis on registrations | (implied via planning) | ✓ "authorizations for any changes and the products affected" | ✓ explicit impact-analysis dashboards | — | Common (2/4 explicit) |
| Health-authority data exchange (gateway, ACKs, XEVMPD/IDMP/PMS) | ✓ IDMP support | ✓ gateway, SPOR, ACK 1–3, PMS | ✓ XEVMPD compiled/validated/submitted | export-to-publisher pole | Common; EU-centric depth varies |
| eCTD-family publishing/validation | ✓ eCTD, NeeS, PDF, XML publishing | ✓ deep: eCTD v3/v4, NeeS, ASMF…; validator used by 35+ agencies | ✓ Ennov Dossier + InSight Publishing | export-to-publisher (not built-in publishing) | Common; depth is a variant axis |
| Labeling / artwork | ✓ Labeling module | (services line) | ✓ Artwork module | — | Optional module |
| Regulatory intelligence (external requirements content) | ✓ module | ✓ RI module | (resources/IDMP hub) | — | Optional module |
| Dashboards / reporting | ✓ | ✓ (AI search/analytics) | ✓ | ✓ | Universal (A) |
| Workflow engine, roles, audit, Part 11/Annex 11 | ✓ (compliance machinery) | ✓ (validation services) | ✓ explicit | ✓ explicit | Universal (A) |
| Safety/PV as part of RIM | ✗ separate line | ✗ separate hub | ✗ separate suite | ✗ separate product | Universal NEGATIVE (A) — PV is a neighboring Type |
| Devices in scope | ✓ "devices, site registrations" | ✓ device authorization details | ✓ RIM for Med Device | ✓ medical-device industry page | Common (A) |
| Customer tier | enterprise | enterprise→SMB→agencies | mid-market→enterprise | lean teams / small sponsors | Variant axis |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

The life-sciences regulatory-affairs system of record. Three jointly-held structures:

1. **The product's regulatory estate** — the company's regulated products held as structured records whose regulatory state per market/health authority (registrations / marketing authorizations and their status; at minimum product regulatory metadata + submission status) is the system's central data spine — the "what is approved where" memory. Remove → a document management or publishing tool with no product-regulatory memory.
2. **The submission/dossier record** — the structured, versioned record of what was filed to health authorities: dossiers maintained as living records (current registered position + version history), submissions/sequences compiled from controlled documents, archived for reference and reuse. Remove → a registration tracker with no filing record, or a standalone eCTD publisher with no memory.
3. **The regulatory activity loop** — regulatory actions (submissions, lifecycle changes/variations/renewals, correspondence, commitments) planned, assigned, tracked to completion, and linked back to products, registrations, and dossiers, with ownership, deadlines, and status. Remove → a static archive; the "management" is gone.

Jointly-held load-bearing:
- 1 alone = registration tracker / product-data store (the paper-era spreadsheet pole).
- 2 without 1 = standalone submission publishing/viewing tool.
- 3 without 1+2 = generic workflow tool.
- 1+2 without 3 = a static regulatory archive.
- 1+3 without 2 = activity tracking with no dossier record of record.
- 2+3 without 1 = submission tooling not bound to a product estate.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Controlled regulatory document management (versioning, review/approval workflows, e-signatures, PDF rendering) integrated with the submission spine.
- Global→national submission derivation (compile a global package; derive/propagate national submissions; document propagation; content reuse).
- Correspondence and commitment tracking bound to products/registrations.
- Change impact analysis (which registrations/products are affected by a change).
- Dashboards/reporting: what is approved where, what is due, what is at risk; workload and timeliness.
- Role-based access, configurable data model, audit trail, Part 11/Annex 11-class compliance machinery.
- Health-authority data exchange: gateways, acknowledgments, agency data standards (XEVMPD/IDMP in the EU), controlled vocabularies.
- eCTD-family submission formats (eCTD, NeeS) and publishing/validation machinery — common but realized at very different depths (built-in publishing vs export-to-publisher).

### L2 — Variant / Optional Structure

- Registration-data depth: full authorization databases (registration-centric pole) vs product metadata + submission status (document-centric lean pole).
- Labeling/artwork management — separate modules at suite vendors; absent at the lean pole.
- Regulatory intelligence (external requirements content) — optional modules.
- Industry scope: drugs core; medical devices, animal health, crop, site registrations, active substances — configurable product-type structures.
- Agency-side deployments (reviewing/validation tools used by authorities) — same vendor family, opposite side of the exchange.
- Deployment: cloud / on-premises / both; single- vs multi-tenant.
- Regional machinery depth: EU IDMP/XEVMPD/SPOR/PMS; US/eCTD; national formats.
- AI/GenAI assistance (search, authoring, comparison) — current-generation overlay.

### L3 — Vendor-specific (Research Notes only)

- ArisGlobal: LifeSphere module names (RIM / Submissions / Documents / Labeling / HA Interactions / Regulatory Analytics / Regulatory Intelligence); NavaX GenAI/agents; "Dossier Record" feature name.
- EXTEDO: hub names; MPDmanager/eCTDmanager/eSUBmanager/EURS product names; "powered by CARA"; >35 authorities using its validator/reviewer; crop-industry support; ACK 1st/2nd/3rd terminology.
- Ennov: Unified Compliance Platform (Doc/Data/Workflow/Analytics/AI); InSight RIM/Publishing; IDMP EASI; DocShifter partnership; Septodont 1500 MAAs / 150 countries case study; PSUR-tracking dashboards.
- Montrium: RegDocs Connect name; XML-backbone navigation of archived sequences; M365/Office integration; 4–8 week implementation claims; explicit anti-positioning against Veeva.

## Vendor-specific Findings

- Montrium's FAQ is the only in-sample explicit definition of "RIM system" — document/submission/communication-centric; useful as the lean-pole's own understanding, not the whole Type.
- Ennov's "Core Capabilities" list is the cleanest vendor-side object model: substances → products → registrations → activities → dossiers → submissions → documents, with automatic linkage.
- EXTEDO's MPDmanager documents the core-data-vs-market-data split explicitly (enter once, reflect across authorizations/regions) — the strongest single statement of the product-spine mechanics.
- ArisGlobal's "Dossier Record — maintain the current registered dossier position and its version history" is the strongest single statement of the dossier-as-living-record.
- EXTEDO and Ennov both document agency data exchange (gateway, validation, ACKs) at Tier-1 strength; ArisGlobal claims IDMP support; Montrium exports to publishers instead.

## Boundary Findings

- **vs Pharmacovigilance Platform** — keep-both RATIFIED from this side (discharges the PV pass's forward flag). PV = the adverse-event safety-case record world (cases → assessment → expedited/periodic safety reporting). RIM = the product authorization/submission estate. Vendor-side confirmation: all four sampled vendors sell safety and regulatory as separate product lines (ArisGlobal Safety vs Regulatory; EXTEDO Safety Hub vs Registration/Submission Hubs; Ennov PV Suite vs Regulatory Suite; Montrium has no PV product). Touchpoint: safety documents that are *filed* (e.g., periodic safety reports) appear in RIM as tracked regulatory activities/submissions — Ennov advertises PSUR-tracking dashboards — but the case data and safety assessment live in PV. The dossier/submission machinery is shared infrastructure; the record worlds are distinct.
- **vs Medical Device Lifecycle Management** — keep-both RATIFIED from this side (discharges that pass's forward flag). Device lifecycle management = the design-control record chain + controlled change over the device design. RIM = the regulatory-affairs estate. RIM holds device *authorization/registration details* (EXTEDO: "covers the management of authorization details of medical devices"; Ennov sells RIM for Med Device; Montrium serves device makers) and manages device submissions as filings — but not the design chain. The seam is design-chain evidence generation vs regulatory filing/authorization estate.
- **vs Regulatory Change Management (§11 GRC)** — distinct Types. RCM monitors *external* regulatory content (laws, regulations, standards) for arbitrary industries; RIM manages the company's *own* product regulatory estate. Overlap zone: RIM products bundle "regulatory intelligence" modules (ArisGlobal, EXTEDO RI) that hold health-authority requirement content — recorded as an adjacent bundled capability, not definitional. Remove the internal estate → RCM territory.
- **vs Regulatory Reporting Platform (§08)** — name collision only. Financial-domain reporting to financial authorities (prudential/transaction reporting). Different domain, different objects; no shared structure beyond "file reports to a regulator".
- **vs eTMF** — distinct. eTMF = clinical-trial master file (trial conduct documents). RIM = product dossiers/registrations. Vendor-side: Ennov sells eTMF and RIM as separate products; Montrium sells eTMF Connect and RegDocs Connect as separate products. Trial-related regulatory filings (e.g., CTA submissions) touch RIM's submission machinery, but the trial record world is the eTMF's.
- **vs Enterprise Content Management / Document Management** — RIM *includes* regulatory document management but is defined by the product/registration/submission/activity spine. A generic regulated-content platform (Generis CARA) can host RIM modules; the platform alone is not RIM. Remove the regulatory object spine → ECM/DMS.
- **vs eCTD publishing/viewing/validation tools** — publishing machinery is one capability inside the estate. Standalone publishers/validators (EXTEDO's tools are usable standalone; Montrium exports to external publishers) are capabilities or companions, not the Type. Remove the estate and activity loop → publishing tool.
- **vs Product Information Management (§05.04)** — commerce product content vs regulatory product registrations. Different users, objects, rules; no overlap beyond the word "product".

## Uncertainties

- Veeva Vault RIM (market leader) could not be fetched (transport errors ×3). Its app structure is not asserted; only Montrium's FAQ characterization of Veeva as an enterprise-scale platform is used. The L0 was deliberately built to be satisfiable by a suite the research could not open — the three legs come from the four reachable poles.
- Montrium's registration-tracking depth is unconfirmed (no advertised authorization database on fetched pages). Treated as the thin-registration pole; if deeper registration features exist behind gated content, the variant axis narrows but the L0 is unaffected.
- Sample is EU/US-centric; regional vendors (Japan, China, Latin America) and regulator-side RIM systems (authorities' own registration databases) were not sampled. The agency-side pole is evidenced only via EXTEDO's authority-facing tools.
- Exact state names, numeric deadlines, and IDMP implementation details were not researched to precision and are deliberately absent from the final document.
- Whether "site registrations" (establishment/facility registrations) are a first-class object at most vendors or an ArisGlobal-specific scope item is unconfirmed (single-product mention).

## Final Synthesis

RIM is the regulatory-affairs system of record for life-sciences companies. Its world is built around the company's regulated products: each product carries structured regulatory data; per market/authority the product has registrations/authorizations with status; what was filed to authorities is held as dossiers and submissions (versioned, compiled from controlled documents, archived); and the work of maintaining the estate — planning submissions, executing variations/renewals, answering and tracking health-authority correspondence and commitments — runs as tracked regulatory activities linked across the spine. The paper-era lineage (registration certificate files per country, paper dossiers, correspondence files, tracking spreadsheets, commitment letters) satisfies all three defining legs without any software, and the eCTD-era generation satisfies them with different format machinery — so the definition holds across eras and does not depend on eCTD, IDMP, cloud, or AI. The Type's identity is the *internal estate of the regulated company*, which separates it from PV (safety cases), device lifecycle management (design chain), RCM (external regulation monitoring), eTMF (trial records), and ECM (content without the regulatory spine).
