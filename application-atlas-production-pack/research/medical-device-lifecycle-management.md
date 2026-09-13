# Research Notes — Medical Device Lifecycle Management

## Research Goal

Understand what "Medical Device Lifecycle Management" actually is as an Application Type: what record structure it maintains for a medical device across its life (concept → design → market → post-market), how the device regulatory regime (design controls, risk management, technical documentation, submission pathways) shapes the software, who uses it, and where its boundaries run against Life Sciences QMS (eQMS), Engineering Requirements Management, generic PLM, Medical Device Post-market Surveillance, and Regulatory Information Management.

## Initial Boundary

Working hypothesis before research:

- **What**: the medical-device manufacturer's product-lifecycle system of record — software holding the device as a managed subject and maintaining the regulated design-control record chain (user needs → requirements/design inputs → design outputs → risk controls → verification & validation) as linked, traceable, approval-gated records accumulating into the device's design history / technical documentation.
- **Who**: R&D / systems / design engineers, risk managers, quality assurance, regulatory affairs at device manufacturers (startups through global enterprises), including SaMD teams.
- **Problem**: device regimes (FDA design controls / QMSR, ISO 13485, ISO 14971, EU MDR, IEC 62304) demand a complete, current, traceable evidence chain per device; spreadsheets and disconnected tools break traceability and audit readiness.
- **Nearest types**: Life Sciences QMS (§22, processed — pre-hung seam: "shift center to design controls & product lifecycle → medical-device product development platform"), Engineering Requirements Management (§16, processed — traceability machinery overlap), Product Lifecycle Management / PLM (§16, unprocessed), Medical Device Post-market Surveillance (§22 sibling, unprocessed), Regulatory Information Management / RIM (§22, unprocessed), CAPA Management (§16, processed), Bill of Materials Management (§16, processed).
- **Unknowns**: whether the Type is real beyond one vendor's branding (the leaf name matches Greenlight Guru's platform vocabulary); which record classes are definitional vs bundled; how the requirements-tool pole and the PLM pole relate; the post-market leg's position.

## Research Questions

1. What is the central record structure — is there a "device product of record" and what hangs off it?
2. Is the design-control chain (needs → inputs → outputs → risk → V&V) with traceability the defining structure?
3. What lifecycle stages does the software actually carry (design → transfer → submission → post-market)?
4. How is risk management (ISO 14971) positioned — record class inside the chain or separate module?
5. Where does the eQMS record population (CAPA/complaints/audits/training) sit — inside this Type or beside it?
6. How do the different product poles (device-native platform, requirements tool, QMS suite, enterprise PLM) realize the same job?
7. What evidence outputs does the software generate (traceability matrices, DHF/DDF/RMF exports)?
8. What distinguishes this Type from generic PLM and from the eQMS sibling?

## Representative Products

| Product | Pole / philosophy | Segment | Evidence depth |
|---|---|---|---|
| Greenlight Guru | Device-native platform; markets the platform category spanning QMS + Product Development + Clinical; coined "medical device lifecycle management" vocabulary | Mid-market device companies, startups → enterprise | Homepage + Product Development page with definitional FAQ (Tier 2) |
| Jama Connect (Jama Software) | Requirements/traceability-centered engineering platform with a packaged medical-device framework | Enterprise device makers (Abbott, Medtronic, Stryker, Dexcom cited as customers) | MedTech solution page with capability + FAQ detail (Tier 2) |
| MasterControl | Enterprise QMS suite pole; device offering = five "Excellence" suites (Development / Quality / Supplier / Manufacturing / Postmarket) | Enterprise life-sciences manufacturers | Medical-device industry page + Development Excellence product page (Tier 2) |
| PTC Windchill | Enterprise PLM pole; generic PLM machinery (PDM/BOM/change/quality) with MedTech industry positioning | Large enterprises | Windchill product page incl. MedTech blurb + regulated-industry FAQ (Tier 2) |

Selection rationale: four different product philosophies (device-native platform / requirements tool / QMS suite / enterprise PLM), different customer tiers, all official vendor surfaces. **Arena Solutions** (cloud PLM+QMS mid-market pole) was targeted but unreachable (404 this pass; transport errors ×2 in the 2026-09-06 BOM pass) — dropped per the network-limitation rule; the mid-market cloud PLM+QMS pole is under-sampled and no claims rest on it.

## Sources

Research date: **2026-09-08**

- Greenlight Guru — https://www.greenlight.guru/ , https://www.greenlight.guru/product-development-software
- Jama Software — https://www.jamasoftware.com/ , https://www.jamasoftware.com/solutions/medtech/
- MasterControl — https://www.mastercontrol.com/industries/medical-device/ , https://www.mastercontrol.com/product-development/
- PTC — https://www.ptc.com/en/products/windchill (device-specific paths 404 ×2: /en/industries/medical-devices, /en/products/windchill/medical-device)
- Arena Solutions — https://www.arenasolutions.com/industries/medical-devices/ — 404; abandoned (prior-pass transport failures ×2)

Source-access limitation: no Tier-1 help-center articles were fetched for any product; all evidence is official product/solution-page depth (Tier 1–2 boundary). No exact workflow state names, numeric limits, defaults, or packaging prices are asserted anywhere. PTC's device-specific solution page was not reachable — the enterprise-PLM pole is evidenced at "generic PLM product page + MedTech industry blurb" strength only, and no device-specific workflow claims are drawn from it.

## Product Observations

### Greenlight Guru (evidence layer A)

- Platform framing: "The medical device platform… 1,000+ device companies trust our AI-powered platform to manage quality, product development, and clinical evidence"; "ready for scrutiny at every stage of the device lifecycle". Three named platform areas: **Quality Management System** (eQMS), **Product Development** (design controls + traceability), **Clinical Evidence** (EDC/ePRO/PMCF).
- Product Development page (the design-control center):
  - "Medical Device Product Development — Intelligent tools for medical device design and development."
  - Design Controls: "Build your DDF as you build your product… Greenlight Guru links design inputs, risks, and tests, so traceability builds automatically"; "Add requirements, connect risks, and flag verifications without leaving the workspace"; "AI checks your requirements for verifiability, while real-time trace graphs expose missing links across design, risk, and test."
  - Software Release Lifecycle Management (SaMD pole): release forms, affected software parts, code changes/pull requests tied to each release; GitHub/Jira sync "so engineers can continue working with the systems they love."
  - Risk Management: "Build your risk matrix… a structured matrix that stays tied to your design work"; "maintain a dynamic, audit-ready Risk Management File (RMF)"; built in accordance with ISO 14971:2019.
  - FAQ definitional sentence: "medical device product development software is designed with the unique needs of the medtech industry in mind… built to manage the highly regulated design and development of medical devices, ensuring that all your engineering activities are documented in compliance according to applicable industry regulations and standards."
  - FAQ: "compliant workflows for each phase of design controls, ensuring a compliant path from development to submission and post-market surveillance."
  - FAQ: DDF "builds automatically as you begin design controls, maintaining complete traceability… Every element is versioned, reviewable, and export-ready."
  - FAQ design artifacts: "every step of design controls, from user needs, design inputs, and design outputs, to verification and validation. You'll also be able to carry out design reviews and link any element within the system."
  - FAQ exports: "traceability matrices, a complete Design History File, and Risk Management File… also download a Medical Device File (MDF), DDF, and audit trails."
  - Standards alignment listed: ISO 13485, ISO 14971, IEC 62304, IEC 60601, ISO 10993, ISO 11135/11137/11607/17665, ISO 42001, ISTA-3A.
  - Positioning vs sibling: "Generic eQMS tools weren't built for medical device development" — the vendor itself separates the eQMS product from the product-development product.
- Use-case nav spans the whole lifecycle: Design Control & DHF, Risk Management, Change Management, Training, CAPA, Complaint, Nonconformance, Project Management, Audit, Supplier, Product Management, eCRF/ePRO, Post-Market Clinical Surveys. Solutions by org type: Pre-Market / Post-Market / CRO / Enterprise / SiMD-SaMD.

### Jama Connect — MedTech & Life Sciences (evidence layer A)

- Page title: "Medical Device Requirements Management Software"; hero: "Engineering Management Platform for Faster, Safer MedTech & Life Sciences Development… from medical device requirements management to release."
- Customer logos: Abbott, Boston Scientific, Medtronic, Dexcom, Stryker, Thermo Fisher, Illumina — top-tier device makers use the requirements pole.
- Solution spread: Complex Medical Devices, IVDs (IVDR alignment), SaMD (IEC 62304, agile, cybersecurity), Combination Devices, RUO/LDT, adjacent life sciences.
- Capability set:
  - **Live Traceability™**: "Track all requirements, risks, and tests in real time… updates linked artifacts as items change and flags suspect downstream links automatically."
  - **Medical Device Framework** (packaged industry content): "pre-built medical device framework aligned to design controls"; "Comply with FDA QMSR, ISO 13485, EU MDR, IEC 62304, and more"; "Automatically generate high-quality design documentation."
  - **Risk Management**: "Conduct risk management in alignment with ISO 14971… Embed cybersecurity directly into risk workflows."
  - **Collaborative Reviews**: "e-signatures with FDA 21 CFR Part 11 compliance."
  - **Scalable Reuse**: reuse across projects/releases; Systems of Systems and Product Line Engineering.
  - **Integrations**: Jira, Azure DevOps, Windchill, Teamcenter, CATIA No Magic — "Streamline change management across systems."
  - AI guidance: flag poor requirements; INCOSE/EARS best practice.
- FAQ (definitional value): "Every user need should link forward to design inputs, outputs, and verification/validation evidence, and you need to traverse that chain in both directions on demand… [the tool] keeps those relationships current… and flags suspect downstream links automatically." And: "[It] connects design controls, risk management, and V&V in one system and produces audit-ready documentation from live data instead of manual assembly."
- Customer evidence of the workflow: Dexcom (traceability model for complex configuration), Vave Health ("trace matrices generation in 1 day… managing our software cadence"), Grifols (Review Center, incremental reviews).
- Segments: startup (FDA/ISO compliance foundations, templates) / mid-market (traceability at scale, R&D+QA/RA+systems collaboration) / enterprise (audit defensibility, portfolio visibility).

### MasterControl — Medical Device (evidence layer A)

- Device offering = five named suites on one platform: **Development Excellence** (product development), **Quality Excellence** (QMS), **Supplier Excellence** (SQM/AVL/SCAR), **Manufacturing Excellence** (eDHR/MES/EBR/logbooks), **Postmarket Excellence** (complaints).
- "Medical device companies can start product development on compliant footing with MasterControl Development Excellence, part of the fully integrated MasterControl platform."
- Development Excellence page: "streamlines the collection and compilation of new product development documentation, integrates quality requirements early in the design process and effectively manages design control throughout the product development lifecycle."
- "MasterControl simplifies design control and bill of materials while aligning your quality and compliance processes with the product development lifecycle, allowing teams to shave considerable time in product introductions with faster changes, approvals, notifications and **transfers**."
- "Uniting product development processes with quality management practices… ensure that market feedback and customer complaints inform product evolution."
- Platform framing: "connecting applications, documentation and data across your entire product development life cycle, **from concept to commercialization**."
- Quality Excellence (bundled eQMS): document control, change control, training, audit, risk, quality events, CAPA — the same machinery the life-sciences-qms pass documented as the eQMS Type.
- Regime context on the industry page: QMSR/ISO 13485 harmonization resources; GMP; Form 483/Warning Letter avoidance framing.

### PTC Windchill (evidence layer A — generic-PLM strength only)

- "Windchill is PTC's enterprise PLM software that connects product data, processes, and people across the entire product lifecycle."
- Core feature set: BOM management (eBOM/mBOM/software BOM), engineering change & configuration management, CAD/PDM, manufacturing process management, parts classification, product variability, supply chain collaboration, **quality management** ("closed-loop processes that connect design, manufacturing, and feedback. Support audits, CAPAs, and traceability").
- MedTech industry blurb: "Ensure regulatory compliance and product quality with end-to-end traceability, document control, and closed-loop processes—supporting faster approvals and continuous innovation in regulated environments."
- FAQ: "Is Windchill suitable for regulated industries? Yes… widely used in… medical technology. It supports compliance through: end-to-end traceability of product data and changes, document control and audit trails, closed-loop quality processes, secure collaboration."
- Separate product: Windchill Risk & Reliability (FMEA, fault tree, corrective actions).
- Reading: the enterprise-PLM pole serves device makers with generic product-data/change/traceability machinery; the device-regime record chain (design controls, risk file, submission evidence) is NOT the center of its own description. This is the boundary evidence vs PLM.

## Cross-product Comparison

| Structure / capability | Greenlight Guru | Jama Connect | MasterControl | PTC Windchill | Reading |
|---|---|---|---|---|---|
| Device product as managed subject (program/product record the chain hangs off) | ✓ (device/product records; "every stage of the device lifecycle") | ✓ (projects per device/product line; portfolio visibility) | ✓ ("from concept to commercialization"; product lines) | ✓ (product/PDM structures) | 4/4 — core |
| Design-control record chain: needs → inputs/requirements → outputs → V&V | ✓ (explicit; "every step of design controls") | ✓ (explicit; "user need → design inputs, outputs, and verification/validation evidence") | ✓ ("manages design control throughout the product development lifecycle") | partial (traceability/change, no design-control semantics on page) | 3/4 explicit — core |
| Traceability links as the connective tissue (forward+backward, gap/suspect flagging) | ✓ ("traceability builds automatically"; "real-time trace graphs expose missing links") | ✓ (Live Traceability; "flags suspect downstream links") | ✓ ("full traceability" in change control; connected platform) | ✓ ("end-to-end traceability") | 4/4 — core |
| Versioned, reviewable, approval-gated records | ✓ ("versioned, reviewable, export-ready"; Part 11 approvals) | ✓ (Review Center; Part 11 e-signatures) | ✓ (automated sign-offs, audit trails) | ✓ (change/approval workflows, audit trails) | 4/4 — core |
| Accumulated design history / technical documentation as output | ✓ (DHF, DDF, MDF exports) | ✓ ("audit-ready documentation from live data"; design documentation generation) | ✓ ("collection and compilation of new product development documentation") | — (document control generic) | 3/4 — core-adjacent, device-regime shaped |
| Risk management tied to the chain (ISO 14971) | ✓ (RMF tied to design work) | ✓ (ISO 14971 workflows + cybersecurity) | ✓ (risk module across lifecycle) | separate product (Risk & Reliability, FMEA) | 3/4 in-chain — standard capability |
| Design reviews as recorded events | ✓ (FAQ: "carry out design reviews") | ✓ (Review Center) | ✓ (approvals/collaboration) | ✓ (reviews in change) | 4/4 — standard |
| Controlled documents (SOPs/specs) | ✓ (QMS module) | — (item-based; not centered) | ✓ (Document Control) | ✓ (document control) | 3/4 — common, separable |
| Design transfer / production transition | ✓ (path "development to submission and post-market") | ✓ (Windchill/Teamcenter integrations "streamline change management across systems") | ✓ explicit ("faster changes, approvals, notifications and transfers") | ✓ (manufacturing process management) | 4/4 — common |
| Regulatory submission support / evidence generation | ✓ (submission pathway; exports) | ✓ ("Improve submissions"; auto-generated design documentation) | ✓ (Regulatory add-on; eDHR "simplify submissions") | — (generic compliance) | 3/4 — common |
| Post-market linkage (complaints/CAPA feed changes) | ✓ (post-market surveillance solutions; PMCF) | — (not on page) | ✓ (Postmarket Excellence; "complaints inform product evolution") | ✓ (closed-loop quality "connect design, manufacturing, and feedback") | 3/4 — common |
| eQMS record classes bundled (CAPA/complaints/NC/audits/training/suppliers) | ✓ (QMS product) | — | ✓ (Quality Excellence) | thin (quality workflows) | 2/4 strong — bundled in device-native & suite poles, NOT definitional |
| BOM / parts management | ✓ (parts & inventory/BOM in QMS) | — | ✓ (BOM datasheet) | ✓ (BOM core) | 3/4 — common in suite/PLM poles |
| Traceability matrix / audit-ready exports | ✓ (explicit export list) | ✓ (trace matrices; "1 day" customer quote) | ✓ (audit readiness framing) | ✓ (traceability) | 4/4 — standard |
| Dev-tool integrations for SaMD (Jira/GitHub/ADO) | ✓ | ✓ | — | — (ALM via IPE) | 2/4 — SaMD-pole variant |
| Regime alignment named (QMSR/ISO 13485/ISO 14971/EU MDR/IEC 62304) | ✓ | ✓ | ✓ | partial (generic "regulatory compliance") | 3/4 — regime anchor |
| Cloud SaaS | ✓ | ✓ | ✓ | ✓ (Windchill+ SaaS; on-prem heritage) | common-dominant — variant |
| AI assistance | ✓ (verifiability checks, smart links) | ✓ (AI guidance) | ✓ (AI platform) | ✓ (AI assistants) | 4/4 era-current — era layer |

Evidence layers: all cells are directly observed (A) on official pages; row readings generalize across the sample (B). The Windchill column is generic-PLM-strength evidence only (source-access limitation recorded above).

## Canonical Model

### L0 — Defining Invariant (three jointly-held structures)

1. **The device product as the lifecycle subject of record** — a persistent, individually identified record of the device (or device family / SaMD product) being developed and maintained, spanning concept → design → market → post-market; the whole record chain hangs off it. Remove → a requirements project or document library with nothing device-shaped; the "lifecycle" is gone.
2. **The design-control record chain with traceability** — user needs, design inputs (requirements), design outputs, risk controls, and verification/validation evidence held as individually identified, linked records; the links are the point: every requirement traces forward to its verification and backward to its need and risk, and the chain accumulates as the device's design history / technical documentation. Remove → a document store or generic PLM without regulated design-control semantics; a bare requirements tool covers only one link class.
3. **Controlled change and release over the chain** — records are versioned, reviewable, and approval-gated with attributed sign-offs; changes are assessed for impact across the chain and propagate with traceability intact, so the released definition of the device's records stays unambiguous. Remove → a static archive; the "management" is gone.

Jointly-held is load-bearing:
- 1 alone = a product/project record (project-management territory).
- 2 without 1 = a traceable requirements/risk/V&V chain not bound to a device subject → Engineering Requirements Management territory.
- 3 without 1+2 = change machinery with nothing device-regulated to change → generic document/PLM change control.
- 1+2 without 3 = a design-history archive with no controlled evolution → a paper DHF binder.
- 1+3 without 2 = product record + change control without the design-control chain → generic PLM.

### L1 — Common Mature Structure (not definitional)

- Risk management as a first-class record class tied to the chain (ISO 14971 risk file/hazard analysis; risk controls linked to requirements and design; cybersecurity risk in the SaMD pole) — 3/4 in-chain.
- Design reviews as recorded, linked events — 4/4.
- Traceability-matrix generation and audit-ready evidence exports (DHF/DDF/RMF/MDF-class outputs) — 4/4.
- Controlled document management (SOPs, specs) — 3/4, separable (absent from the requirements pole's center).
- Design transfer / production transition linkage — 4/4 (explicit in one, structural in others).
- Regulatory submission support (evidence packages for 510(k)/CE-class pathways) — 3/4.
- Post-market linkage (complaints/CAPA/post-market data feeding changes back into the chain) — 3/4.
- eQMS record classes bundled (CAPA, complaints, nonconformances, audits, training, suppliers) — strong in the device-native and QMS-suite poles, absent/thin elsewhere → bundled standard capability, NOT definitional (the seam vs Life Sciences QMS).
- BOM / parts management — 3/4 (suite/PLM poles).
- Regime alignment machinery (QMSR/ISO 13485/ISO 14971/EU MDR/IEC 62304 framings, Part 11-class e-signatures and audit trails as the implementation of attributed approvals) — 3/4 named.

### L2 — Variant / Optional Structure

- **Product pole**: device-native platform (QMS + product development + clinical on one platform) vs requirements/traceability-centered tool with packaged device framework vs enterprise QMS suite (development as one suite beside quality/manufacturing/postmarket) vs enterprise PLM (generic product-data estate serving medtech).
- **Device class**: traditional hardware devices; SaMD/SiMD (software release lifecycle, dev-tool integrations, IEC 62304); IVD (IVDR); combination products; RUO/LDT.
- **Regulatory regime**: FDA (510(k)/QMSR) vs EU (MDR/CE) vs both; regional pathways.
- **Deployment**: cloud SaaS dominant; on-premises enterprise PLM heritage.
- **Scale packaging**: startup templates/guardrails vs mid-market vs enterprise governance/portfolio.
- **Clinical evidence module** (device EDC/ePRO/PMCF surveys) — optional platform extension.
- **AI assistance** (verifiability checks, smart-link suggestions, requirement-quality flags) — era-current.

### L3 — Vendor-specific (research notes only)

- Greenlight Guru: markets the platform category with "medical device lifecycle management" vocabulary; three named platform areas; AI traceability-gap checks and "predictive verifiability"; SafeBeat release-automation case; Guru expert services; 3.5x audit-risk marketing stat; separate Quality vs Clinical pricing.
- Jama Connect: Live Traceability™ trademark; packaged "Medical Device Framework" content; "100 million items" scale claim; SOC 2/TISAX badges; named customer stats (60% efficiency, trace matrices in 1 day, 80 hours saved).
- MasterControl: five "Excellence" suite naming; no-code quality-event form designer; patented validation tooling; FedRAMP government packaging; eDHR/MES/EBR as separate suite.
- PTC Windchill: Windchill+ SaaS and PTC Jetstream collaboration product; AI Part Intelligence; Integrated Product Engineering (PLM+ALM digital thread); Risk & Reliability as separate product; comparison pages vs Teamcenter/ENOVIA/Arena.

## §24 Historical / Market-Sample Check

Paper-era device development: a design plan, user-needs and design-input documents, design outputs (drawings, specifications), a risk analysis file, verification and validation protocols with results, design-review minutes, and change-request forms with signatures — bound to the device project and accumulating as the design history file / technical file — satisfies all three L0 legs at analog level. The design-controls regime itself (US) dates to the pre-QMSR quality-system regulation's design controls and the DHF concept (regulatory-history fact asserted at general-knowledge strength; not verified against a fetched source this pass); the EU technical-file/technical-documentation concept predates cloud software. Early electronic implementations (document management + spreadsheets + hand-built traceability matrices) satisfy without cloud, AI, dev-tool integrations, or SaMD machinery. Therefore: DHF/DDF naming, cloud, AI, integrations, and SaMD-specific machinery are held as modern implementations/variants, NOT invariants. Regional check: EU-first manufacturers run the same chain against technical documentation/MDR rather than FDA DHF vocabulary — the invariant is the traceable design-control chain, not any one regulator's file name.

Anti-overfitting check: the sampled device-native and QMS-suite products bundle eQMS record classes (CAPA/complaints/training), but the requirements pole and the PLM pole serve the same device-lifecycle job without them — bundling is packaging, not definition. Conversely, all four poles carry the traceable chain — that is the stable center.

## Boundary Findings

- **vs Life Sciences QMS (§22, processed 2026-09-08)** — seam held from this side, DISCHARGES that pass's forward flag ("shift center to design controls & product lifecycle → medical-device product development platform (Greenlight Guru's own second product is exactly that, sold separately)"): eQMS centers the quality-event/action loop (deviations/CAPA/change/audits as compliance evidence of the quality system); this Type centers the device product's design-control record chain and lifecycle. Direct evidence: Greenlight Guru sells Quality Management and Product Development as separately named products and states "Generic eQMS tools weren't built for medical device development"; MasterControl sells Development Excellence as a distinct suite beside Quality Excellence. The eQMS record population appears here only as a bundled standard capability in two of four poles.
- **vs Engineering Requirements Management (§16, processed 2026-09-08)** — that Type centers the requirement of record + structured specification + traceability + managed change for any engineered product; this Type centers the device lifecycle (chain + device subject + transfer/submission/post-market + regime anchor). Requirements traceability is one leg of this Type's chain. Jama Connect is the recorded straddler: its medtech solution is requirements-centered and its customers include top device makers — held as one product serving this Type from the requirements pole by center of gravity (it does not carry transfer/submission/post-market machinery as its center). Consistent with that pass's regulated-industry-pole variant note.
- **vs Product Lifecycle Management / PLM (§16, unprocessed)** — PLM centers the product data estate (CAD/PDM, BOM, change, manufacturing process) across industries; this Type centers the device-regime record chain. Windchill evidence: its own MedTech positioning is generic PLM machinery (traceability, document control, closed-loop quality) without design-control/risk-file/submission semantics at the center. Enterprise PLM vendors serve device makers with medtech accelerators — packaging straddle to be confirmed by the PLM pass. Removal test: remove the design-control chain semantics → generic PLM remains.
- **vs Medical Device Post-market Surveillance (§22 sibling, unprocessed)** — proposed seam: PMS centers the marketed-device vigilance/safety loop (complaints, adverse-event reporting, trend analysis, PMCF) as its own record world; this Type centers the development/lifecycle record chain, with post-market linkage as the downstream leg feeding changes. That pass should confirm from its own sample.
- **vs Regulatory Information Management / RIM (§22, unprocessed)** — RIM centers regulatory data/submissions/dossier management as the regulatory-affairs system of record; this Type's submission support is evidence generation from the design chain, not the regulatory dossier system. Pre-hung note for that pass.
- **vs CAPA Management (§16, processed 2026-09-07)** — CAPA is a bundled record class here (in QMS-integrated poles), not the center; consistent with that pass's object-scope test.
- **vs Bill of Materials Management (§16, processed 2026-09-06)** — BOM/parts is a bundled capability in the suite/PLM poles, not the center; consistent with that pass's packaging-gradient finding.
- **vs Validation Management (§22, unprocessed)** — process/computerized-system validation is a distinct function (MasterControl sells Validation as a separate product line); design V&V here is verification/validation of the device design, not system validation.
- **vs Manufacturing QMS / eDHR (§16, unprocessed)** — production-floor quality and device history records vs design-phase records; MasterControl sells Manufacturing Excellence beside Development Excellence — suite packaging, different centers.
- **Removal tests**: remove the device subject → requirements management; remove the design-control chain → generic PLM/document management; remove controlled change → static DHF archive; remove the regime anchor (design controls/risk/submission semantics) → generic project+document tooling; shift center to quality events → Life Sciences QMS; shift center to marketed-device vigilance → Medical Device Post-market Surveillance.

## Uncertainties

- **Arena Solutions unreachable** (404 this pass; transport ×2 in the 2026-09-06 BOM pass) — the mid-market cloud PLM+QMS pole is under-sampled; no claims rest on it.
- **PTC device-specific page unreachable** (404 ×2) — the enterprise-PLM pole is evidenced at generic-PLM strength; no device-specific workflow claims drawn from Windchill.
- No Tier-1 help-center articles fetched → no exact state names, numeric limits, or defaults asserted; workflow descriptions are conceptual and match vendor-described stages only at that grain.
- The leaf name "Medical Device Lifecycle Management" matches vendor-coined category vocabulary (Greenlight Guru's platform positioning); the market also uses "medical device product development software" (Greenlight Guru's own FAQ term), "medical device requirements management" (Jama's page title), and medtech PLM/QMS language. The Type is real across four poles; recorded as a taxonomy naming observation, no directory change.
- Design transfer's exact workflow depth varies (explicit in MasterControl's wording; structural elsewhere) — kept at "common" strength.
- Post-market linkage depth varies (strong in device-native and suite poles; absent from the requirements pole's page) — kept at "common" strength.

## Final Synthesis

Medical Device Lifecycle Management is the medical-device manufacturer's product-lifecycle system of record. Its defining core is exactly three jointly-held structures: (1) the device product as the lifecycle subject of record — a persistent identified record of the device spanning concept → design → market → post-market; (2) the design-control record chain with traceability — user needs, design inputs/requirements, design outputs, risk controls, and verification/validation evidence held as linked records whose links accumulate into the device's design history / technical documentation; (3) controlled change and release over the chain — versioned, reviewable, approval-gated records whose changes propagate with traceability intact. Risk management (ISO 14971), design reviews, traceability-matrix and design-history exports, controlled documents, design transfer, submission support, post-market linkage, bundled eQMS record classes, BOM/parts, and dev-tool integrations are the standard capability layer — common but not definitional. The market realizes the Type on four poles (device-native platform, requirements/traceability tool, enterprise QMS suite, enterprise PLM), across device classes (hardware, SaMD/SiMD, IVD, combination) and regulatory regimes (FDA QMSR, EU MDR). The seams to Life Sciences QMS (quality-event center), Engineering Requirements Management (requirement-of-record center), PLM (product-data-estate center), and Medical Device Post-market Surveillance (vigilance center) are all held from this side, with the life-sciences-qms pass's forward flag discharged.
