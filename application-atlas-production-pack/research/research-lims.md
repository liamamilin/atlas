# Research Notes — Research LIMS

Research date: 2026-09-09
Directory leaf: "Research LIMS" (§23 Education, Research & Knowledge Institutions)
Slug: research-lims

## Research Goal

Understand, from real products, what a LIMS positioned for research contexts actually is: whether "Research LIMS" is a distinct Application Type or a research-context instance of the already-processed generic LIMS Type (laboratory-information-management-system-lims, §22, processed 2026-09-08), what research-specific structures exist (specimen↔experiment linkage, lineage, protocol-driven work, provenance), who the users are, and how the boundaries hold against the dense neighboring cluster (generic LIMS, ELN, LIS, Biobank, SDMS, Research Data Management, Scientific Instrument Management, Research Core Facility Management).

This pass also carries two joint-review obligations inherited from prior passes:
1. the laboratory-information-management-system-lims pass's flag: "expected research-context instance on the same sample-workflow core; context seam rather than structural seam; joint review recommended when processed"
2. the electronic-lab-notebook-eln pass's flag: "documentation-vs-operations seam drawn; joint review recommended when both LIMS leaves are processed" (the §22 LIMS pass already discharged the ELN flag from its side; this pass discharges the research-lims half)

## Initial Boundary Hypothesis (Step 1)

- Core use: a research laboratory's system of record for its specimen-based work — track research samples through protocol-driven processing, capture results/derived data with provenance, feed analysis and publication.
- Primary users: bench scientists/researchers (often students and postdocs with turnover), lab managers/lab ops, core-facility staff; secondary: PIs, collaborators, biobank curators, IT/bioinformatics.
- Nearest Types: generic LIMS (§22, processed — expected same core, different context), ELN (processed — documentation twin), LIS (§22, unprocessed — clinical), Biobank Management (§22, unprocessed — storage-first), SDMS (§22, unprocessed — data-file layer), Research Data Management (§23, unprocessed — institution-scale data governance), Scientific Instrument Management (§23, unprocessed — instrument-centric), Research Core Facility Management (§23, unprocessed — scheduling/billing).
- Unknowns going in: whether the research context changes the *structure* (new objects?) or only the *color* (context, posture, emphasis); whether the generic LIMS core's "validated result" leg holds in research settings where specification/QC validation is less central; whether lineage/aliquot modeling is definitional here.

## Research Questions (Step 2)

1. What objects exist in a research-context LIMS and how are they related?
2. Is the generic LIMS core (sample of record + managed workflow + results, traceably held) present as-is, or restructured?
3. What is research-specific: experiment/study linkage, lineage/aliquots, protocol configurability, freezer/storage depth, ELN coupling, analysis-pipeline handoff?
4. What is the evidence/compliance posture — provenance/reproducibility vs specification validation and accreditation (ISO 17025/GxP/Part 11/CLIA)?
5. Who uses it, in which research settings (academic labs, biotech/biopharma R&D, biobanks, core facilities, government research)?
6. Where are the boundaries vs generic LIMS, ELN, Biobank, RDM, instrument management, core facility, SDMS, LIS?

## Representative Products (Step 3)

Chosen for market representation + different philosophies + different customer tiers + documentation accessibility; deliberately complementary to the §22 generic-LIMS sample (LabWare/LabVantage/STARLIMS/Autoscribe/SENAITE — enterprise and open-source testing-lab poles):

1. **LabKey (Sample Manager / LabKey LIMS)** — research-native platform pole; "grew out of working research labs"; academic/government research center of gravity (Fred Hutch, NIH, Johns Hopkins biorepository) plus biotech; ships LIMS, Sample Manager, SDMS, EDC, ELN as separate products — high boundary value.
2. **Illumina Clarity LIMS** — commercial genomics-workflow pole (formerly Genologics/BaseSpace Clarity LIMS); genomics labs and sequencing core facilities; preconfigured protocol workflows; instrument/automation integration; shows the research LIMS inside a vendor's wider run→analytics stack.
3. **SciSure (eLabNext)** — ELN+LIMS+EHS hybrid platform pole (eLabNext + SciShield merger, LabFolder acquired 2025); strong academic research customer base (Institut Pasteur, Boston University, Purdue, KU Leuven, Groningen, Fraunhofer) plus biopharma; the hybrid-packaging pole for the ELN boundary.
4. **Genemod** — lightweight modern-SaaS pole for academic labs and startups ("Affordable, easy lab management for academia"); sample/inventory/lineage-centric LIMS with ELN in one data model; AI-agent era-current layer.

Rejected candidates: samples.software (transport error ×2 — abandoned per network rules), SLIMS/Bio-ITech (transport error ×1 — abandoned), Senaite (already sampled by the §22 generic pass; reused as cross-pass context only), Quartzy/FreezerPro (inventory/biobank-storage-first poles — boundary context via Genemod's own comparison pages).

## Sources

All fetched 2026-09-09. Evidence layer A unless noted.

- LabKey — home (https://www.labkey.com/) — positioning, product family, industries, customer claims
- LabKey — LIMS product page (https://www.labkey.com/products-services/lims-software/) — feature areas, LIMS/ELN FAQ, chain-of-custody FAQ, configurability FAQ, Sample-Manager-vs-LIMS FAQ
- LabKey — Sample Manager product page (https://www.labkey.com/products-services/sample-management-software/) — lifecycle, lineage/aliquots, freezer management, Part 11/HIPAA support, pricing tiers, case-study signals
- LabKey — Academic Research industry page (https://www.labkey.com/industry/academic-research-software/) — research-context framing (continuity, data sharing/partitioning, integrity for audits/publishing)
- Illumina — Clarity LIMS product page (https://www.illumina.com/products/by-type/informatics-products/clarity-lims.html) — positioning, key features, preconfigured workflows, regulated-environment features, plans, figures, stack context
- Illumina — Lab management software page (https://www.illumina.com/products/by-type/informatics-products/lab-management-software.html) — category framing, automation integration
- SciSure/eLabNext — home (https://www.elabnext.com/) — platform composition (ELN/LIMS/EHS), segments, customer base
- SciSure/eLabNext — LIMS page (https://www.elabnext.com/lims) — feature list, how-it-works surfaces, ELN-vs-LIMS FAQ, GxP FAQ, comparison table, case studies
- Genemod — home (https://www.genemod.com/) — product set (samples/lineage/freezers/consumables/orders/experiments/protocols/equipment), solutions incl. Academia, compliance claims, AI layer

**Source-access limitation:** no product help center / user manual was fetched in this pass (Clarity LIMS User Guide at help.claritylims.illumina.com, SciSure Help Center at support.elabnext.com, and LabKey documentation were not fetched; samples.software and slims.io unreachable ×2 each — abandoned per network rules). Evidence for all four products is official but from home/product/feature/industry surfaces. Per the evidence rules: operational detail is described only at the granularity the sources support; no numeric limits, no exact state lists, no screen inventories asserted; vendor-stated numbers (user counts, record counts, workflow counts) are quoted as vendor claims and kept out of the final document.

## Product Observations

### LabKey — Sample Manager / LabKey LIMS (evidence layer A)

- Positioning: "LIMS & data management software for labs... From sample to insight, one system for your samples, workflows, notebooks and results. Everything captured as structured, AI-ready data. Built to fit any lab, any science." "LabKey grew out of working research labs, and scientist feedback still shapes every release." Trusted-by claim: 500+ scientific labs & research organizations (vendor claim).
- Product family shipped as separate products: Sample Manager (sample tracking/freezer/ELN), LabKey LIMS (with Agriculture/Biologics/Food & Beverage/Mining editions), Server SDMS, EDC, Panorama (mass-spec data), ELN. Biologics LIMS = suite of ELN + Sample Manager + Bioregistry + Workflow Manager.
- Sample Manager: "tracks location, lineage, and status for every sample across its lifecycle, and logs every action automatically"; lifecycle "from receipt and aliquoting to storage, retrieval, shipping, and disposal"; "freezer-level storage tracking and a full chain-of-custody record, with workflows configured to your lab's SOPs"; "Capture lineage, aliquot relationships, and chain of custody in one connected record"; "Configure sample types, metadata, and statuses to match your lab's processes and study context"; freezer layouts, storage history, freeze/thaw tracking; "built to support 21 CFR Part 11 and HIPAA requirements" (Part 11 support via audit log with timestamp+user; HIPAA hosting as add-on). Used by "academic research labs and biobanks to clinical and translational research teams"; case studies: Johns Hopkins 300K+ biorepository, Tulane NPRC legacy migration, Alaska wildlife/veterinary samples, IVF clinic sample tracking (vendor case studies).
- LabKey LIMS: "samples, data, workflows, and reporting — configured to match how your team works"; "Easily configure sample types, data pipelines, and workflows to match your exact SOPs"; instrument data "captured and transformed automatically on ingest"; lifecycle "from initial registration through storage, aliquoting, and consumption in experiments"; "Track sample status, location, and chain of custody in real time with a detailed audit log that captures every touchpoint"; "Link assay results directly to samples, experiments, and notebook entries for full data provenance"; workflows "mirror your actual SOPs — with task assignments, approval gates, and automatic deviation capture baked in"; "Enforce step-by-step adherence to improve reproducibility, with deviations flagged and logged automatically"; integrated ELN: "notebook entries are connected to the samples, results, and workflows they document."
- Vendor's own LIMS/ELN seam (FAQ): "A LIMS manages sample tracking, chain-of-custody, storage, and workflow execution. An ELN captures experimental protocols, observations, and scientific context."
- Vendor's own chain-of-custody description (FAQ): "Every sample... has a complete, searchable history — registration, processing steps, storage location changes, assay linkages, and any modifications, including the reason for the change. That full timeline is always available, always timestamped, and always tied to a specific user."
- Vendor's own Sample-Manager-vs-LIMS distinction (FAQ): Sample Manager = "sample tracking, storage management, and SOP-driven workflows"; LabKey LIMS "builds on that foundation with deeper capabilities for instrument data integration, advanced protocol execution, configurable experiment metadata schemas, and centralized scientific data management across multi-team or multi-study environments." — the vendor's own proof that tracking-only is a lesser product class (mirrors Autoscribe Matrix Tracker in the §22 pass).
- Academic-research framing (industry page): "Continuity of Research — Academic research can span years and often involve frequent changes of contributors"; "Data Sharing & Collaboration... fine-tunable controls for user permissions and data partitioning"; "Data Integrity... when conducting audits, collaborating or publishing research"; HIPAA and CFR Part 11 support.
- Industries: Academic Research, Government Research, Biotech & Pharma, Biobanks, Environmental, Food & Beverage, Agriculture, Mining. Community Edition download exists (open-source lineage).

### Illumina Clarity LIMS (evidence layer A)

- Positioning: "A highly customizable laboratory information management system that allows genomics labs to track samples and manage workflows efficiently and securely." "Clarity LIMS (formerly known as BaseSpace Clarity LIMS) enables labs to track samples, streamline complex tasks, generate sample sheets, and catch poor quality samples before running them on a sequencing system."
- Benefits: automated workflow "saves time and minimizes errors in sample handling"; workflows usable "without coding expertise"; scales "accommodating third-party instruments and software through an extensible API."
- Key features (vendor FAQ): end-to-end sample traceability; genealogy view; real-time status monitoring; Illumina preset protocols; Illumina instrument integrations; regulatory support; remote collaboration; automation support; configurability and extensibility.
- Preconfigured workflows: "more than 60 preconfigured workflows for Illumina NGS and array applications" (vendor claim).
- Regulated-environment features (for CLIA-certified organizations and other regulated labs): data entry enforcement, workflow enforcement, issue resolution documentation, precision monitoring, role-based permissions, audit trail, electronic signatures.
- Surfaces shown: Sample Management screen (accessioning, copy-across values, custom fields); configuration "all in one location with no need for command-line skills"; sample pooling with drag-and-drop that "helps prevent samples with identical indexes or samples missing an index from being pooled"; Advanced Search ("build, save and share custom queries", scheduled queries, CSV export); System Settings (roles and permissions, IP whitelisting, SSH access); LabLink for sample submission; dashboard reporting; bulk accessioning of kit lots for a reagent type.
- Automation integration: Illumina lab automation software "automatically informs wet lab devices, including liquid-handling robots, on sample placement location and container types. When integrated with Clarity LIMS... real-time status and reporting, enabling end-to-end sample traceability and reagent tracking."
- Stack context: Lab (Clarity LIMS) → Run (BaseSpace Sequence Hub / Local Run Manager) → Analytics (DRAGEN) → Insights (Emedgene) — the LIMS is the wet-lab layer of a genomics pipeline.
- Customers: Rapid Novor (antibody discovery), Beck's Hybrids (agricultural genomics service lab), Illumina's own sequencing services lab (vendor case studies).
- Plans: Professional/Enterprise subscription; named users 3/10; local or cloud deployment; ISO/IEC 27001/27701 certifications; HIPAA BAA (Enterprise, US-only).

### SciSure (eLabNext) (evidence layer A)

- Platform: "Scientific Management Platform (SMP) formed through the merger of eLabNext and SciShield"; LabFolder acquired September 2025. Trusted-by claim: 550,000+ scientists, 55,000+ laboratories (vendor claim).
- Capabilities: ELN ("Manage experiments, ensure research integrity and reproducibility"), LIMS ("Sample tracking, inventory management, and workflow automation"), Health & Safety/EHS, Integrations.
- LIMS page: "gives lab teams a structured way to manage samples, inventory, equipment, and workflows in one system"; "Know where every sample is, and who accessed it last."
- Sample management: centralized sample database with real-time status tracking; advanced search and filtering; customizable sample fields and categories ("Define sample types and attributes to match your lab's workflows"); batch updates; "See the experiment linked to each sample — Trace each sample back to its originating experiment for full context"; "View the full history of any sample — Access complete lineage, updates, and activity for each sample"; sample lifecycle and disposal tracking "with complete traceability and audit logs"; biobanking management (biospecimens, storage locations, traceability).
- Storage: freezers, liquid-nitrogen storage, safety cabinets, cold rooms, custom-defined storage structures.
- Inventory/orders: reagents, consumables, equipment tracked; low-stock alerts; shared shopping lists; order tracking "from request to fulfillment"; supplier integration.
- Equipment: registered, scheduled, booked; "Maintenance, calibration, and validation events can be planned in advance with automated notifications."
- Workflow: "Automated research workflow management — Automate sample workflows to reduce manual tasks"; use case "Multi-step testing workflows — Centralize protocols, track progress in real time, and maintain complete audit history across teams and sites."
- Identification/access: barcode label printing; user roles, permissions, access control.
- Vendor's own ELN/LIMS seam (FAQ): "An ELN captures experiments, notes, and results, while a LIMS manages samples, workflows, and lab operations. Together in SciSure, they connect scientific context with structured operational data for full traceability."
- Compliance (FAQ): "SciSure supports regulated environments with audit trails, e-signatures, version control, and structured records" (GxP, GLP, ISO named); platform trust page: ISO/IEC 27001, GDPR, FDA 21 CFR Part 11, GxP, HIPAA.
- Vendor's own comparison table: Traditional ELN "Good for notes, but disconnected from the rest of your lab"; Traditional LIMS "Strong [sample tracking], but lives in a separate system"; SciSure "Samples, experiments, and results all connected."
- Segments: Academic, Biopharma, Biotech, Start-up. Customers: Institut Pasteur, Boston University, Purdue, KU Leuven, Groningen, Fraunhofer, HistologiX (histology/IHC research services — audit-preparation automation case), Euroimmun, Photanol (sample traceability), Arctic Therapeutics (ISO 15189), Bayer, Pfizer, Nestlé, AstraZeneca, SmartLabs, NYC Office of Chief Medical Examiner (vendor case studies/logos).

### Genemod (evidence layer A)

- Positioning: "LIMS & ELN Software for Biotech Labs"; "ELN, LIMS, inventory, and equipment in one data model — with AI agents that design experiments, execute protocols, and produce audit-ready records." Compliance claims: SOC 2 Type II, HIPAA-ready, 21 CFR Part 11; "10M+ records managed" (vendor claims).
- Product set: Lab inventory; Sample management ("Track every sample down to its box position"); Lineage ("Trace any sample back to its source"); Consumables; Orders ("Request, approve, and receive in one place"); Alerts (low stock/expirations); Experiments ("Document experiments with rich, linked entries"); Protocols ("Reusable templates your whole lab can follow"); Version control ("Every change tracked, nothing ever lost"); Reports ("Turn experiments into shareable PDF reports"); Equipment ("Track and schedule the instruments you run on"); Security; Integrations ("pull results straight from your instruments").
- Virtual freezer: "racks and boxes mapped as they sit on the shelf"; UI signals: "FREEZER 2 · −80 °C / Rack C · Box B7 · 78/81 tubes"; "GM-0482 checked out · M. Chen, 11:03"; low-stock reorder request drafted automatically.
- Customization: custom fields per item type (example shown: "Passage no. · per cell line").
- Research-context framing: "Tech transfer — hand off a protocol with its samples, results, and history intact"; "Audit-ready data exports — pull methods and data for papers or an inspection in one click."
- Solutions: Biopharmaceutical, Industrial biotech, Clinical research ("Traceable, audit-ready sample workflows"), Biomanufacturers, Biorepositories ("Manage large sample collections"), Contract services ("Run client work with full traceability"); research areas: Cell therapy, RNA therapy, Antibodies ("Organize clones, lots, and characterization"), CRO, Chemistry; "Genemod for Academia — Affordable, easy lab management for academia"; Diagnostics; Startups.
- AI layer (era-current): AI LIMS, AI ELN, AI Agent, AI Global Search, AI Sample Tracking, AI Protocol Template, AI Data Migration.
- Comparison pages (boundary context): vs Excel, vs LabArchives (ELN), vs Quartzy (inventory), vs FreezerPro (freezer/sample tracking), vs Benchling ("A Lab OS built for the wet lab").
- Trusted-by logos: Harvard, Stanford Medicine, Johns Hopkins, Memorial Sloan Kettering, Pfizer, Merck, AstraZeneca, Bayer, BMS, Eurofins, Seattle Children's, Colossal Biosciences (vendor claims).

## Cross-product Comparison

| Structure / capability | LabKey | Clarity LIMS | SciSure (eLabNext) | Genemod | Layer |
|---|---|---|---|---|---|
| Sample of record: ID + metadata + status | ✓ (registration, custom types/fields) | ✓ (Sample Management accessioning, custom fields) | ✓ (centralized DB, real-time status) | ✓ (sample management, box position) | A/B |
| Origin linkage (source/subject/study/experiment) | ✓ ("study context"; results↔samples↔experiments) | ✓ (genomics sample context; sample sheets) | ✓ ("experiment linked to each sample") | ✓ ("trace back to its source"; experiments linked) | A/B |
| Lineage / aliquots / genealogy | ✓ (lineage, aliquot relationships) | ✓ (genealogy view) | ✓ (full history incl. lineage) | ✓ (Lineage product) | A/B — 4/4 |
| Managed workflow / status lifecycle | ✓ (workflow templates mirroring SOPs, approval gates, deviation capture) | ✓ (workflows, 60+ preconfigured, workflow enforcement) | ✓ (automated research workflow management, multi-step testing) | ◐ (protocols/experiments + AI workflows; thinner formal workflow engine in fetched evidence) | A/B |
| Results/assay data linked to samples | ✓ (assay data management, provenance links) | ✓ (sample sheets, run integration, status) | ✓ (results connected; experiment linkage) | ✓ (experiments/results, reports) | A/B |
| ELN coupling / experiment documentation | ✓ (integrated ELN product) | ✗ (run/analytics stack instead) | ✓ (ELN capability, one platform) | ✓ (ELN in one data model) | A/B — 3/4 |
| Freezer/storage depth | ✓ (freezer management, freeze/thaw) | ◐ (kit lots/reagents; storage not emphasized) | ✓ (freezers, LN2, cold rooms, custom) | ✓ (virtual freezers, rack/box) | A/B |
| Reagent/consumable inventory + orders | ✓ (inventory management) | ✓ (reagent tracking, kit-lot accessioning) | ✓ (inventory, orders request→fulfillment) | ✓ (consumables, orders, alerts) | A/B |
| Instrument integration | ✓ (capture + transform on ingest) | ✓ (Illumina instruments, liquid handlers) | ✓ (APIs, Developer Hub, Marketplace) | ✓ (API integrations) | A/B |
| Instrument management (calibration/maintenance) | ◐ (implied) | — (not observed at fetched level) | ✓ (calibration/maintenance scheduling) | ✓ (equipment track/schedule) | A/B, uneven |
| Audit trail / traceability posture | ✓ (audit log, chain of custody, timestamped+user) | ✓ (audit trail, e-signatures) | ✓ (audit logs, "who accessed it last") | ✓ (version control, audit-ready exports) | A/B |
| Review/approval/e-signatures | ✓ (approval gates) | ✓ (e-signatures) | ✓ (e-signatures) | ◐ (order approvals observed; e-sig not explicit) | A/B |
| Specification/QC validation machinery | ◐ (QC checks in workflow automation) | ✓ ("catch poor quality samples", data/workflow enforcement, precision monitoring) | — (not emphasized) | — (not emphasized) | A, uneven → variant |
| Compliance support (Part 11/HIPAA/GxP/CLIA/ISO) | ✓ (Part 11, HIPAA) | ✓ (CLIA features, ISO 27001/27701, HIPAA BAA) | ✓ (GxP, Part 11, HIPAA, ISO 27001) | ✓ (Part 11, SOC 2, HIPAA) | A/B — support, not center |
| Configurability (types/fields/workflows, no-code) | ✓ (headline capability) | ✓ (web configuration, no command line) | ✓ (custom fields/categories) | ✓ (custom fields per type) | A/B |
| Roles/permissions | ✓ | ✓ (role-based permissions) | ✓ | ✓ | A/B |
| Search | ✓ | ✓ (Advanced Search, saved/shared queries) | ✓ (advanced search/filter) | ✓ (AI global search) | A/B |
| Dashboards/reporting | ✓ (reports/visualizations) | ✓ (dashboard reporting) | ◐ (reporting via Marketplace) | ✓ (PDF reports) | A/B |
| Barcode/label identification | ◐ (implied) | ◐ (accessioning; labels implied) | ✓ (barcode label printing) | ◐ (checkout codes; labels implied) | A/B, uneven |
| Submitter/client portal | ◐ (external-client case studies) | ✓ (LabLink sample submission) | — (not observed) | — (not observed) | A, uneven → common in service labs |
| Analysis-pipeline handoff | ✓ (bioinformatics/SDMS solutions) | ✓ (BaseSpace/DRAGEN stack) | — (not observed) | — (not observed) | A/B — genomics/data-platform pole |
| AI layer | ◐ ("AI-ready" architecture) | — | ◐ (Marketplace AI add-ons) | ✓ (AI agents, headline) | A — era-current, variant |
| Segment/industry packaging | ✓ (8 industries incl. Academic/Government Research) | ✓ (genomics) | ✓ (Academic/Biopharma/Biotech/Start-up) | ✓ (Academia + biotech solutions) | A/B — variant |
| Deployment | cloud + Community Edition (open-source lineage) | local or cloud | cloud (hosting options) | cloud SaaS | A/B — variant |

Reading: the first block (specimen of record → origin/lineage context → managed protocol workflow → results linked back → traceable retention) is present and load-bearing in every product. The research-context color (experiment linkage, lineage, protocol configurability, freezer depth, ELN coupling) is strongly and repeatedly present. Everything below is unevenly distributed: spec/QC validation machinery, submitter portals, analysis-pipeline handoff, and AI are variant; suite composition and deployment are packaging.

## Canonical Model (Step 5–7)

### L0 — Defining Invariant

Three jointly-held structures; the traceability posture binds them. This is the generic LIMS core (sample of record + managed analysis workflow + result of record, traceably held — documented by the §22 pass) specialized to the research context:

1. **The research specimen of record** — a persistent, individually identified record per physical sample/material in the research lab's custody, carrying its origin (source, subject, study or experiment context), its type, and its status. Remove → a freezer spreadsheet / sample list.
2. **The managed protocol workflow** — the lab's research work organized as defined stages the specimen moves through (registration → processing/assay → results), orchestrated by the system via statuses and worklists, and configured to the lab's own methods and protocols rather than a fixed accredited test menu. Remove → a static registry; the specimen never "moves".
3. **The provenance-tracked result of record** — results and derived data captured per assay/experiment (manually or from instruments), attributed and linked back to the specimens and methods that produced them, and retained as the lab's evidence-bearing research record that feeds analysis, publication, collaboration, and tech transfer. Remove → a tracker with no scientific product.

Binding posture: the whole is retained as an attributable, traceable record (audit-trail class). In the research instance the evidence posture is **provenance and reproducibility** — every result traceable to its sample, method, instrument and operator — which is what "data integrity for audits, collaboration and publishing" means in a research lab.

**Deliberate asymmetry vs the generic LIMS Type (documented, mirrors the environmental instance's asymmetry):** the generic pass holds "validated result of record — checked against specifications and QC" inside its L0. In the research instance, specification/QC validation machinery is the *regulated-lab realization* (observed at the genomics pole: quality catching, data/workflow enforcement; present at LabKey as QC checks), not the invariant: the lightweight academic poles carry the full core with provenance-first retention and no specification-limit machinery. The result leg itself (captured, attributed, retained as evidence-bearing record) is invariant; the validation *mechanism* re-weights from specification-checking to provenance-tracking. If maintainers ever prefer one LIMS Type with industry variants, this leaf becomes the research variant.

**L0 minimality check (§22/§23/§24 discipline):**
- Lineage/aliquot parent-child modeling — the research instance's signature common-mature capability (4/4 observed, stronger than the generic pass's 1/5), but NOT definitional: the paper ancestor (bound sample register + freezer box map + notebook cross-references) satisfies the core without a formal lineage object. Held at L1 with elevated confidence.
- Freezer/box-depth storage — common (3/4 strong); a paper box map satisfies → L1.
- ELN integration — common (3/4 ship ELN; the genomics pole integrates a run/analytics stack instead) → L1.
- Instrument integration — common; manual entry satisfies → L1.
- Protocol libraries / preconfigured workflows — mature form; the invariant is "work organized as the lab's own defined stages" (a paper protocol binder satisfies it) → L1.
- Compliance support (Part 11/HIPAA/GxP/CLIA/ISO) — supported across the sample but as variant depth; the invariant is the traceability posture itself → L2.
- Barcode identification, portals, dashboards, AI — L1/L2.

### L1 — Common Mature Structure

- lineage/aliquot/derivative parent-child modeling with genealogy views (4/4 — the research instance's signature capability)
- freezer/storage-unit depth: box/rack/plate mapping, capacity, freeze/thaw history, checkout tracking
- reagent/consumable inventory with ordering (request→fulfillment), low-stock alerts
- instrument registration, integration and (unevenly) calibration/maintenance scheduling
- ELN coupling: experiments linked to samples/results/workflows; notebook entries referencing actual records
- configurable sample types, custom metadata fields, status workflows without code
- roles/permissions; audit trail; e-signatures at critical steps
- advanced/global search over the specimen and result corpus
- barcode/label identification
- dashboards and reporting (PDF/report exports for papers and inspections)
- submitter/client portal in service-lab deployments (core facilities, CROs, sequencing services)
- analysis-pipeline handoff (genomics: run setup and secondary analysis; data-platform pole: bioinformatics workspaces)

### L2 — Variant / Optional Structure

- domain packaging: genomics (preconfigured protocol workflow libraries), biologics R&D (registry/construct lineage), biobanking depth, clinical/translational (EDC coupling), agriculture/food/mining editions
- compliance depth: Part 11/HIPAA/GxP/CLIA/ISO 15189/17025 support vs none — regulated research labs add specification/QC enforcement machinery
- suite composition: LIMS+ELN+EHS (hybrid platform pole), LIMS+ELN+SDMS+EDC (data-platform pole), LIMS+run+analytics stack (instrument-vendor pole), LIMS+ELN one-data-model (lightweight pole)
- deployment: cloud SaaS / on-premises / open-source community edition
- AI layers (era-current): AI agents, AI search, AI protocol generation
- pricing/packaging: per-user tiers, named-user counts, add-ons (HIPAA hosting, validation packages)

### L3 — Vendor-specific (research notes only)

LabKey: Sample Manager vs LabKey LIMS product split, Bioregistry, Panorama mass-spec product, EDC, Community Edition, industry LIMS editions (Agriculture/Biologics/Food & Beverage/Mining), per-user pricing tiers. Illumina: Clarity LIMS naming lineage (Genologics → BaseSpace Clarity LIMS → Clarity LIMS), LabLink sample submission, 60+ preconfigured Illumina workflows (IPP), genealogy view, Professional/Enterprise plans with named-user counts, ISO certifications, position in the Lab→Run→Analytics→Insights stack. SciSure: eLabNext+SciShield merger and LabFolder acquisition, SMP framing, Marketplace add-ons, Developer Hub, comparison table vs "traditional LIMS/ELN". Genemod: AI agent suite, virtual-freezer UI, comparison pages vs Benchling/Quartzy/FreezerPro/LabArchives/Excel, "one data model" framing.

## Rejected Findings

- "Research LIMS is defined by genomics" — rejected: the sample spans biobanks, wildlife/veterinary samples, IVF clinics, histology research services, agriculture, antibody discovery; genomics is one packaging with the strongest preconfigured-workflow evidence.
- "Research LIMS lacks compliance machinery" — rejected: all four sampled products support Part 11-class features (audit trail, e-signatures); the center of gravity is provenance/reproducibility, and compliance depth is variant.
- "Research LIMS is just an ELN" — rejected: vendors themselves draw the operations-vs-documentation seam (SciSure FAQ, LabKey FAQ) while bundling both; the spines differ.
- "The lineage object is definitional" — rejected: the paper ancestor satisfies the core without it; lineage modeling is the signature common-mature capability, not the invariant.
- "Research LIMS is a distinct Type from the generic LIMS" — rejected: the three-leg core is identical; the difference is context, posture and emphasis — a domain instance (same ruling as environmental-laboratory-management).
- "Tracking-only products are Research LIMS" — rejected: LabKey's own Sample-Manager-vs-LIMS FAQ and the §22 pass's Matrix Tracker evidence show the market treats tracking-without-workflow/results as a lesser product class.

## Boundary Findings

- **vs Laboratory Information Management System / LIMS (§22, processed) — JOINT REVIEW DISCHARGED from this side:** keep-both RATIFIED as generic Type + domain instance (same pattern as environmental-laboratory-management). The research leaf's core is a strict specialization of the generic LIMS core (sample of record + managed analysis workflow + result of record, traceably held) with research-context anchors: specimens tied to studies/experiments/sources, work configured to the lab's own protocols, results valued as provenance-bearing research data feeding analysis/publication, freezer-depth storage, ELN and analysis-layer coupling. One documented asymmetry: the research instance re-weights the result leg's validation posture from specification-checking to provenance-tracking (spec/QC machinery = regulated-lab variant). Seam = organizing context (research program/experiment-driven specimen work vs testing-service/production-QC sample work) + evidence posture (provenance/reproducibility vs specification/accreditation) + downstream consumption (analysis/publication vs reports/certificates/enterprise systems). If maintainers ever prefer one LIMS Type with industry variants, this leaf becomes the research variant (no directory change proposed).
- **vs Electronic Lab Notebook / ELN (processed) — JOINT REVIEW DISCHARGED from this side (research-lims half; the §22 LIMS pass discharged the other half):** operations-vs-documentation seam CONFIRMED with fresh vendor-documented evidence on this side — SciSure FAQ ("An ELN captures experiments, notes, and results, while a LIMS manages samples, workflows, and lab operations"), LabKey FAQ ("A LIMS manages sample tracking, chain-of-custody, storage, and workflow execution. An ELN captures experimental protocols, observations, and scientific context"), LabKey ELN product copy ("notebook entries are connected to the samples, results, and workflows they document"), Genemod's one-data-model framing. The ELN pass's muddy-vocabulary concern (ELNs shipping inventory capability; one open-source ELN carrying a "lims" topic tag) is confirmed but does not breach the seam: hybrid packaging is market-normal (3/4 sampled products bundle ELN; SciSure is ELN+LIMS+EHS), and bundling does not merge Types — the experiment record vs the specimen workflow remain different spines.
- **vs Biobank Management (§22, unprocessed):** storage-first pole boundary. Research LIMS products ship biobanking capability (SciSure biobanking management; LabKey biobank solution; Genemod biorepositories solution; LabKey Sample Manager runs a 300K+ biorepository per case study) — long-term specimen custody and banking depth is the neighbor's spine; the analysis-workflow spine is this Type's. The storage-first pole is the boundary zone; joint review recommended when processed.
- **vs Research Data Management (§23, unprocessed):** institution-scale research data governance (datasets, data management plans, repositories, funder/mandate compliance) vs lab-scale specimen/workflow operations. Seam = unit of management (datasets and data outputs vs physical specimens and their processing). A research LIMS feeds RDM; it does not govern institutional data compliance. Joint review recommended when processed.
- **vs Scientific Instrument Management (§23, unprocessed):** instrument-centric (booking, maintenance, usage, cost) vs specimen-workflow-centric. Equipment management appears as a module inside research LIMS (SciSure equipment, Genemod equipment, LabKey instrument management) — module, not identity.
- **vs Research Core Facility Management (§23, unprocessed):** service scheduling/billing for shared research facilities vs the sample testing workflow itself; a core facility may run both (Clarity LIMS is deployed in sequencing core facilities while core-facility management systems handle booking/billing).
- **vs Scientific Data Management System / SDMS (§22, unprocessed):** data/file layer vs workflow system of record. LabKey ships LabKey LIMS and Server SDMS as separate products — vendor-documented packaging evidence that the two are distinct.
- **vs Laboratory Information System / LIS (§22, unprocessed):** patient+order clinical care context vs specimen+protocol research context; same seam the generic pass drew. Research LIMS products serving clinical/translational research (LabKey) keep the specimen/study frame, not the patient-care frame.
- **vs Chromatography Data System (processed):** instrument-local data acquisition/processing vs lab-wide specimen workflow — consistent with the generic pass's seam.

## Uncertainties

1. **No help-center-grade operational docs were fetched** (Clarity User Guide, SciSure Help Center, LabKey documentation not fetched; samples.software and slims.io unreachable ×2 — abandoned). State machines, exact role sets and rule details are therefore described at feature-page granularity; no numeric limits, defaults or exhaustive state lists are asserted anywhere.
2. **Genemod's workflow leg** is thinner in fetched evidence (protocol/experiment structures and AI workflows rather than a formal workflow engine in the LIMS proper). Held as realization variance, not absence — its solutions pages advertise "traceable, audit-ready sample workflows". The lightweight-pole workflow realization deserves a deeper look if a manual-grade source becomes reachable.
3. **Submitter/client portal**: directly observed at Clarity (LabLink) and implied at LabKey (external-client case studies); not observed at SciSure/Genemod home pages — held common-in-service-labs, not universal.
4. **Spec/QC machinery**: directly observed at Clarity and LabKey; not emphasized at SciSure/Genemod. The provenance-first re-weighting of the validation posture is inferred from this distribution and documented as the deliberate asymmetry — it is the instance's most consequential interpretive move and should be revisited if a regulated-research-pole pass (e.g., GxP research labs) contradicts it.
5. **Historical check is reasoned, not source-verified**: the paper-era academic lab (bound sample register with accession numbers, freezer box maps, notebook cross-references, signed results) and the 2000s core-facility database generation satisfy the core conceptually; no fetched source documents these ancestors — held as conceptual lineage, low confidence.
6. **Vendor claims** (500+ labs, 550K+ scientists, 60+ workflows, 10M+ records, named-user counts) are quoted as vendor claims and excluded from the final document.

## Final Synthesis

Research LIMS is the research organization's LIMS: the generic LIMS core — specimen of record + managed workflow + results of record, retained traceably — specialized to research contexts. Specimens are research samples tied to their sources, studies and experiments, commonly with explicit lineage (aliquots, derivatives, constructs). Work is organized as the lab's own protocols and configured per lab ("your science"), not a fixed accredited test menu. Results are provenance-bearing research data — every result linked back to its specimen, method, instrument and operator — retained as the lab's evidence for analysis, publication, collaboration and tech transfer. Around this core, mature products add freezer-depth storage, reagent/inventory management, instrument integration, ELN coupling, configurable metadata, search, roles and portals. Compliance machinery (Part 11, GxP, CLIA, ISO) is supported where the research lab is regulated, but the instance's evidence posture is provenance and reproducibility rather than specification accreditation. The Type is a research-context instance of the LIMS Type — same three-leg core, different context, posture and emphasis — not a separate Application Type. The defining test: remove the specimen → a freezer spreadsheet; remove the workflow → a static registry; remove provenance-tracked results → a tracker with no scientific product; remove traceability → a shared spreadsheet.
