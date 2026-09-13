# Research Notes — Electronic Lab Notebook / ELN

Research date: 2026-09-07
Leaf: Electronic Lab Notebook / ELN (slug: electronic-lab-notebook-eln)
Directory location: appears TWICE in DIRECTORY.md — under §22 Healthcare & Life Sciences AND under §23 Education, Research & Knowledge Institutions. Taxonomy observation recorded in Boundary Findings and STATUS.md.

---

## Research Goal

Understand what an Electronic Lab Notebook actually is as an Application Type: its core objects, the defining record structure, how experimental work is documented and protected as evidence, where the boundary with LIMS / RDM / generic note tools lies, and which features are common mature structure vs vendor or segment variants.

## Initial Boundary (working hypothesis before research)

- Core hypothesis: an ELN is the digital replacement of the paper lab notebook — a system of record for experimental work, where researchers create dated, attributed records of experiments containing text, data, files; records are tamper-evident and can be signed/witnessed; everything is searchable and retrievable later.
- Expected neighbors: LIMS (sample/operation management), Research LIMS, Scientific Data Management System, Research Data Management, Note-taking Application, Wiki, Document Editor, eTMF (trial documents).
- Biggest open questions: is sign-off/witnessing definitional or common? Is inventory linkage part of the Type? How do academic vs regulated-industry variants differ?

## Research Questions

1. What is the canonical object hierarchy (notebook/project → entry/experiment/page → content)?
2. What content types live inside a record (rich text, tables, images, attachments, domain-specific objects)?
3. How are records attributed, timestamped, and protected against silent alteration (version history, audit trail, timestamps, sealing/locking)?
4. What role do signatures, review, and witnessing play, and where (regulated vs academic settings)?
5. How do templates / protocols / forms standardize capture?
6. How do search, export, and archiving work (the "record" lifecycle end)?
7. How do sharing, permissions, and oversight (PI / team) work?
8. Where does inventory / sample linkage sit — in-Type capability, module, or neighbor Type?
9. What distinguishes academic, institutional, and regulated-industry realizations?
10. Boundary: ELN vs LIMS vs RDM vs wiki/notes — what flips one into another?

## Representative Products (selected 2026-09-07)

Chosen for market representativeness, documentation quality, differing product philosophies, and differing customer levels:

| Product | Philosophy / Position | Customer level | Evidence base |
|---|---|---|---|
| Benchling | Structure-aware life-sciences R&D platform; Notebook is one module beside Registry/Inventory/Results | Enterprise biotech/pharma + academics | Help Center (2 full operational articles + section index) — Tier 1 |
| SciNote | Structured projects/experiments/tasks ELN with protocols, inventory, GxP add-on | Academic-to-industry SMB; free individual tier | Knowledge Base (2 articles) + product site — Tier 1 + Tier 2 |
| LabArchives | Notebook-first ELN, university-wide deployment, strong Education and Government editions | Universities + commercial + government | Help Center (full section index) + product site — Tier 1 + Tier 2 |
| RSpace | "Open source research data management"; FAIR/PID-oriented generalist ELN with institutional storage integration | Institutions (universities, research institutes) | Product site (ELN page) — Tier 2 only |
| eLabFTW | Open-source, self-hosted, minimalist notebook + resource database for research teams | Academic labs, institutes (self-hosted), some companies | Official GitHub README — Tier 1/2 hybrid (repo docs) |

## Sources

Directly fetched 2026-09-07:

- Benchling Help Center — root, Product Documentation category, Data Capture section, "Plan experiments and collect data in the Notebook" (full article), "Create and use review processes" (full article) — https://help.benchling.com/
- SciNote — product site https://www.scinote.net/ ; Knowledge Base index https://knowledgebase.scinote.net/en/knowledge ; "How to sign a task using an electronic signature and move a task to 'In review' status" (full article); "Is SciNote 21 CFR Part 11 compliant?" (full article)
- LabArchives — product site https://www.labarchives.com/ ; Help Center root and ELN category index https://help.labarchives.com/hc/en-us
- RSpace — product site and ELN page https://www.researchspace.com/ , https://www.researchspace.com/eln
- eLabFTW — official GitHub repository README https://github.com/elabftw/elabftw

Source-access limitations:

- doc.elabftw.net (official user guide) failed twice (transport error) — abandoned per network-failure rule. eLabFTW observations are limited to the official GitHub README; operational details (per-entry behavior, export formats, permission mechanics) are NOT asserted from memory.
- RSpace documentation (researchspace.helpdocs.io) was not fetched; RSpace evidence is product-page level (Tier 2). Operational claims about RSpace are kept weak.
- LabArchives Help Center articles were indexed but not individually fetched beyond category level; feature existence is directly observed, article-level detail is not asserted.
- All five vendor surfaces confirmed reachable; no fabricated details used to fill gaps.

---

## Product Observations

### Benchling — Notebook (evidence layer: A, Tier 1 help docs)

- Notebook described as "a digital workspace for documenting experiments, tracking data, and collaborating with your team".
- Records are **Notebook entries**, created blank or **from templates** (admin-configured); entry creation requires a title and assignment to a **project and folder**.
- Rich text editing: typographical emphasis, superscript/subscript, symbols, headers, lists, checkboxes; insert plain and **structured tables**, attachments, code blocks; auto-compiled table of contents; collapsible sections with names and dates.
- **Date inserts** timestamp actions; the default date insert at the top of an entry "is system-generated metadata for audit purposes" and cannot be deleted; date blocks must be chronologically ordered (out-of-order dates auto-adjust).
- Entry metadata tab: multiple **authors**, project/folder move, **entry schema** for structured tagging/classification, custom fields.
- Tables support spreadsheet features: column types, data validation, formulas (SUM, AVERAGE, IF, XLOOKUP), lookup columns linking other Benchling entities.
- **Version history**: automatic timestamping of all entry updates ("maintain data integrity, meet compliance requirements, and trace contributions"); restore or duplicate from a version.
- Sharing: link sharing, read-only links; **export** entry as PDF or raw data; exports preserve structure of Registry/Inventory-linked tables.
- **Review processes** (admin-configured, assigned per project; apply to all entries in project): self-review, parallel review, sequential review; stages with reviewer pools (authors, teams, project collaborators), configurable action labels (e.g., **"Approve", "Witness"**), stage definitions shown to reviewers, completion status. Sending an entry for review **locks** it (authors cannot edit until review completes / is cancelled / rejected); reopening resets status. Review stage names appear "in entries, audit logs, and exports". SSO credential validation on submission. Legacy model had "Auditor" collaborators. Review processes cannot be deleted once created (deactivation only) — governance posture.
- **Notebook Check** (AI, tenant-enabled): detects formatting/naming issues, incomplete entries, possible mistakes; informational only, not stored.
- Benchling Sync desktop app: check out attachments for edit in desktop tools (Word, Excel, FlowJo); changes sync back "maintaining a complete audit trail".
- Sibling modules in the same platform: **Registry** (entity registration), **Inventory**, **Results** — the Notebook links to them via mentions (@) and structured tables.
- Sub-templates: admin-configured reusable content blocks; updates do not retroactively change entries.
- Academic-variant help article exists ("…for Academic users") — segment-aware documentation.
- L3 detail (research notes only): entry performance guidance (~35,000 table cells supported; warning at 17,500).

### SciNote (evidence layer: A for KB articles, A/B for product site)

- Positioning: "cloud-based ELN software with lab inventory, compliance, & team management tools".
- Structure: **Projects → Experiments → Tasks** ("emulates how research happens"); tasks carry protocols, results, comments; connected tasks visualized as workflows.
- Protocol steps can be **checked off**; **protocol templates** with versions, shareable with team; import from **protocols.io**; AI-assisted SOP/protocol import (blog, 2025).
- Data entry in tasks: notes, tables, checklists, pictures, uploaded result files, hyperlinks; "You will always know what was done, when, how, by whom and which results were generated."
- **Electronic signature workflow** (21 CFR Part 11 add-on; KB article, full):
  - Task moved to "In review" status → task is **locked** ("Locked Tasks CANNOT be edited by any user").
  - Signature requests go to project members (except Viewer role); once one member signs, the request disappears for others; multiple requested signatures must ALL complete before the task can move to final "Done" status (button disabled while pending).
  - Signing requires re-authentication (credentials, SSO provider, or 2FA); optional comment; @mentions to notify.
  - Signatures tab shows full signing history incl. rejected/revoked signatures; **co-sign** and **revoke signature** supported; revocation required before unlocking.
- 21 CFR Part 11 add-on (premium plans) includes: **detailed audit trail, advanced user management, electronic signatures, electronic witnessing**, security features (password expiration, system logs).
- **Inventory**: lab supplies/equipment with stock management, labeling, custom columns; inventory items assignable to tasks/experiments; connected to results.
- Report generator: auto-generated reports from experiments; embed files.
- Search: keyword search "through all your projects, experiments, files, and their content".
- Collaboration: comments, tagging, notifications; user roles/permissions (owner / user / technician / viewer table documented).
- Mobile app (Android/iOS): check off protocol steps, comments, uploads in real time.
- Compliance positioning: GxP / GLP / GMP / 21 CFR Part 11; ISO 27001; Trust Center; used by FDA, USDA (marketing claims).
- Free tier for individual users; premium plans for teams.

### LabArchives (evidence layer: A for feature existence via Help Center index, Tier 2 site for positioning)

- Positioning: "Record, organize, search and share your scientific data" in an ELN; cloud-based; strong university customer base (MIT, Oxford, Cambridge, Duke …) plus commercial and government editions.
- Structure: **Notebooks → Folders → Pages**; **entries** are added to pages ("Adding and Editing Entries", "Example Notebook Page — Recording an Experiment", "Moving and Rearranging Entries").
- **Revision History and Timestamps** (dedicated article) — versioned, timestamped record.
- **"Search Notebooks, Track Activities and Apply Electronic Signatures"** section: basic search, advanced search, **chemical structure searching**, searching within page/folder, Notebook Dashboard, **Tracking Notebook Activity**, plus e-signature articles (section has 7 articles; e-signature feature existence directly observed at index level).
- Entry content: **Rich Text Editor**, attachments, **Microsoft Office for the Web** editing, headings, inventory lists, image text/handwriting extraction.
- **Widgets** library: Chemical Sketcher, Database, Freezer Box, Google Calendar/Docs — embeddable structured content objects.
- **Forms**: Form Center, Form Builder, publishing/archiving forms, CSV export — structured data capture inside the notebook.
- Folder Monitor (Windows/Mac) and Microsoft Office plugins — desktop capture paths.
- Membership & permissions: **Notebook Roles and Permissions**, inviting members, **limiting access to a section of a notebook**, sharing notebook URLs, institutional SSO, Account Manager for enterprise administration.
- Publishing/export: print entries/pages, **download notebook to PDF**, offline notebook, publish via shared URL, **DOI generation**, publish to Figshare.
- **ELN for Education**: courses, assignments, student notebooks, instructor quick starts — teaching variant of the same notebook machinery.
- **LabArchives for Government**: FedRAMP-authorized environment, NIST 800-53 customization.
- Companion products: **Inventory** (samples, freezer locations, ordering), **Scheduler** (equipment booking) — separate products tied to the ELN.
- Integrations: SnapGene, GraphPad Prism, Geneious, Jupyter, Proofig AI (image-integrity check), iChemLabs, Microsoft 365.
- Compliance posture (site): SOC2, ISO 27001, HIPAA, GDPR, 21 CFR Part 11, NIST 800-171 badges.

### RSpace (evidence layer: B — Tier 2 product site only; no operational docs fetched)

- Positioning: "open source research data management"; ELN described as "Intuitive, collaborative, and generalist research notebook"; institutional deployment (cloud or on-premises); customers are universities/research institutes (Harvard, Edinburgh, UCL, MDC …).
- Core capabilities claimed on ELN page:
  - **Collaborative Notebooks** — real-time collaboration, granular sharing controls, templates, structured organization.
  - **Chemistry Workflows** — chemical drawing, stoichiometry tables (automatic calculations), chemistry-specific data management.
  - **Integrated Inventory System** — samples/inventory alongside documentation.
  - **Rich Metadata** — forms with structured fields, ontology support, "FAIR research practices"; PIDs: ORCID, IGSN, PIDINST, RAiD, ROR, RRID, DataCite.
  - **Version Control & Compliance** — "Complete audit trails, **signing & witnessing**, and regulatory compliance built-in"; version history with restore.
  - Feature list: comments & annotations, granular permissions (individuals/groups), export to PDF/Word/HTML/XML/**RO-Crate**, file attachments with automatic versioning, full-text search across content & metadata, folder organization, templates & forms, rich text editing, REST API.
- **File Management** pillar: integrate with institutional storage (SMB, SFTP, iRODS, S3); persistent resource links; bundle external files in exports.
- **Instrument Management** pillar: instrument catalog, reference instruments in documents with bidirectional links, PIDINST fields, calibration states.
- Integrations: 20+ tools incl. repositories (Dataverse, Zenodo, Figshare), storage, instruments, protocols.io, ChemDraw, Jupyter, Slack.

### eLabFTW (evidence layer: A/B — official GitHub README; operational docs unreachable)

- "A free, modern, versatile, secure electronic lab notebook for research teams"; "electronic lab notebook manager for research teams"; open source (AGPL), self-hosted on a server, accessed via browser.
- "It lets you store and organize your research experiments easily."
- Features (README): lab notebook for experiments; **database for resources** (reagents, equipment, storage, cell lines, chemicals…); **trusted timestamping**; **blockchain timestamping**; import/export in various formats; equipment-booking calendar; support for scientific file formats; molecule editor; LaTeX; todolist; public REST API; 21 languages; advanced permissions system; "self contained service that doesn't leak data to third party".
- Team model: several research teams hosted on one installation — institute-level deployment hosting all teams ("what is done at many research institutions around the globe").
- Ecosystem evidence: import scripts from other ELNs (RSpace .eln files, LabFolder); The ELN Consortium (interoperability between ELNs); `.eln` portable format appears in the ecosystem.
- NOT evidenced from README (do not assert): per-entry signing workflow, locking behavior, search detail, template mechanics.

---

## Cross-product Comparison

| Structure | Benchling | SciNote | LabArchives | RSpace | eLabFTW | Assessment |
|---|---|---|---|---|---|---|
| Record hierarchy (container → experiment record) | Project/Folder → Entry | Project → Experiment → Task | Notebook → Folder → Page (+entries on page) | Notebook → Folder → Document | Team → Experiments (per user) | **Universal (B across 5)** — the defining shape |
| Rich evidential authoring (text + tables + attachments) | A (structured tables, formulas, TOC) | A (notes/tables/pictures/results) | A (rich text, Office, attachments) | B (rich text, tables, attachments) | A (scientific file formats; molecule editor) | **Universal** — definitional |
| Templates / protocols / forms | A (entry templates, sub-templates, template collections) | A (protocol templates, protocols.io) | A (templates, widgets, form builder) | B (templates & forms) | not evidenced (README silent) | Common mature structure |
| Attribution: authors on record | A (Authors metadata, author tags) | A ("by whom"; signature identity) | A (revision history) | B (granular permissions, audit) | B (team/user model) | Universal |
| Timestamps | A (mandatory date block, audit-purpose) | A (timestamp in Part 11 set; "when") | A (Revision History and Timestamps) | B (audit trails) | A (trusted + blockchain timestamping) | Universal — definitional |
| Tamper-evidence: version history / audit trail | A (version history; review in audit logs) | A (detailed audit trail; lock) | A (revision history; activity tracking) | B (complete audit trail, version control) | partial (timestamping; secure/audited code) | Universal — definitional |
| Sign-off / review / witness | A (review processes: self/parallel/sequential; "Witness" action label; lock) | A (e-signature → lock; witnessing in Part 11 add-on) | A existence (e-signature section) | B ("signing & witnessing" built-in) | not evidenced | Common; witnessing = compliance/regulated variant |
| Locking / sealing records | A (locked on send-for-review) | A (locked in In review/Done) | not observed at index level | not evidenced | not evidenced | Common (regulated-weighted) |
| Search over the record corpus | A (implied by platform; search not in fetched article) | A (search across projects/experiments/files/content) | A (basic/advanced/chemical structure search) | B (full-text across content & metadata) | not evidenced | Universal in practice (4/5 directly) |
| Export / archive | A (PDF, raw data; read-only links) | A (report generator) | A (PDF, offline notebook, DOI, Figshare) | B (PDF/Word/HTML/XML/RO-Crate) | A (import/export various formats) | Common mature structure |
| Permissions / roles / sharing | A (access policies, reviewer pools) | A (owner/user/technician/viewer) | A (notebook roles, section-limited access) | B (granular per individual/group) | A (advanced permissions) | Common mature structure |
| Inventory / sample linkage | A (Inventory module + structured tables) | A (built-in inventory, stock, labeling) | A (Inventory product, freezer widgets, inventory lists) | B (integrated sample management) | A (resource database) | Present in all 5 in some form — but packaged differently → common, not definitional |
| Domain content objects (chemistry, sequences) | A (sequences, registry entities) | not emphasized in fetched pages | A (chemical sketcher, structure search) | B (chemical drawing, stoichiometry) | A (molecule editor) | Optional domain-dependent content |
| Compliance posture (GxP/Part 11) | B (validated cloud releases) | A (Part 11 add-on, premium) | A/B (Part 11 badge; Gov edition) | B (compliance pages) | not claimed | Variant by segment |
| Publishing / PIDs | not observed | not observed | A (DOI, Figshare) | B (ORCID/IGSN/DataCite, RO-Crate) | not evidenced | Variant (academic RDM-weighted) |
| Integrations / instrument linkage | A (Registry/Inventory/Results, Sync desktop) | A (protocols.io, API/webhooks) | A (SnapGene/Prism/Geneious/Jupyter) | B (20+ integrations, iRODS/S3) | A (REST API, file formats) | Common |
| AI assistance | A (Notebook Check) | A/B (AI import) | A (Proofig AI integration; OCR) | not observed | not evidenced | Era-typical optional |
| Education/teaching surface | A (academic article variant) | not observed | A (full Education edition) | not observed | not evidenced | Variant |
| Deployment | A (cloud, tenant) | A (cloud; hosted options) | A (cloud; FedRAMP gov env) | B (cloud or on-prem) | A (self-hosted, institute-level) | Variant axis |

### Reading of the comparison

1. Five structures recur across ALL sampled products and survive abstraction: (a) the notebook/project container → experiment record hierarchy; (b) rich evidential authoring with embedded files/tables; (c) attributed + timestamped + tamper-evident records; (d) persistent accumulation with later retrieval; (e) a permission/collaboration layer for a research team.
2. Sign-off/review is near-universal in mature commercial products and is the operationalization of the record-as-evidence posture; two-person witnessing appears specifically as regulated-compliance machinery (Benchling action label, SciNote Part 11 add-on, RSpace built-in claim). The open-source academic pole (eLabFTW) instead centers **timestamping/notarization** as its attestation mechanism. Conclusion: formal witness workflow = common/variant, NOT definitional; tamper-evident attestation (of which witnessing/timestamping are realizations) belongs to the definitional layer.
3. Inventory linkage is present in ALL five products but with different packaging (module, separate product, built-in database). Its universality in the current market does not make it definitional — removing it leaves an unmistakable ELN (paper analog had none), so it stays at common level.
4. Templates/protocols: common; forms/structured capture: common-to-variant; domain objects (sequences, chemistry): variant by discipline.
5. Export/archive and publishing (PDF, DOI, RO-Crate, offline notebook): common; specific mechanisms are variant.
6. AI: era-typical optional (2025–2026 pattern).

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (smallest stable structure)

An ELN is recognizable as an ELN if and only if it provides:

1. **The experiment record inside an organizing container** — a unit of record (entry / experiment / page / document) representing a bounded piece of experimental or scientific work, placed in a durable organizational structure (notebook or project, usually with intermediate folders/groupings). Without the experiment-shaped record in a persistent container, it is not a lab notebook.
2. **Evidential authoring** — the record can hold the evidence of the work: free-form text plus embedded content (tables, images, files/data, optionally domain objects). A record that cannot carry data/attachments is not an experimental record.
3. **Attributed, timestamped, tamper-evident record** — each record carries who created/authored it and when; the system preserves the history of changes (version history and/or audit trail) so the record can serve as evidence (research integrity, IP, regulatory). This is the paper-notebook contract made digital: dated, signed pages that cannot be silently altered.
4. **Durable accumulation with later retrieval** — records persist for years and can be found again (navigable structure; full-text search is the standard modern mechanism).

Remove any one: (1)→generic document store, (2)→abstract log, (3)→a wiki/notes tool, (4)→a working scratchpad.

### L1 — Common Mature Structure (very common, not definitional)

- Templates: entry/experiment templates, protocol templates with versions, reusable content blocks, admin-governed template libraries
- Structured capture: tables with typed columns/formulas, forms, structured (metadata) fields on records
- Sign-off / review workflows on records (incl. configurable reviewer stages, action labels such as approve/witness, re-authentication on signing, signature history)
- Locking/sealing records at a workflow state
- Search across the whole corpus (content + metadata; sometimes domain-specific, e.g. chemical structure search)
- Permissions/roles for teams (notebook/project-scoped read/write, viewer roles, section-limited access, external collaborators)
- Export/archive: PDF, office formats, data formats; read-only sharing links; offline copies
- Comments, mentions, notifications; activity feeds
- Inventory/sample linkage (module, companion product, or built-in resource database)
- REST API / integrations (protocols.io, desktop editors, analysis tools, institutional storage)
- Auto-generated reports from records

### L2 — Variant / Optional Structure

- Two-person witnessing as formal mechanism (regulated realizations)
- Regulatory-compliance packaging: GxP/21 CFR Part 11 add-ons, validated environments, government-authorizations (FedRAMP-class)
- Domain content depth: chemistry drawing/stoichiometry, DNA/sequence views, molecule editors, chemical structure search
- Timestamping/notarization mechanisms: trusted timestamps, blockchain timestamps, DOI publishing, repository publishing (Figshare-class)
- Education surfaces: course notebooks, assignments, student roles
- Mobile apps; offline capture
- AI assistance (entry checks, protocol import, image-integrity screening)
- Deployment: cloud SaaS vs self-hosted vs institution-hosted; single-team vs institute-level multi-team
- Segment packaging: life-sciences platform (notebook as one module among registry/inventory/results) vs notebook-first standalone vs RDM-integrated institutional ELN

### L3 — Vendor-specific (research notes only, not in final doc)

- Benchling: entry cell-count performance thresholds (17,500 warning / 35,000 supported), tenant feature settings, legacy review with Auditor checkboxes, Notebook Check AI specifics, Benchling Sync MSI deployment (SCCM/Jamf/Intune), malware scanning of uploads recorded in audit trail
- SciNote: exact status names (In Progress / In review / Done), "Return to → Completed" gating, signature-request widget on dashboard, Viewer role exclusion from signature requests, free individual tier
- LabArchives: Widget library items, Folder Monitor, Account Manager, GovRAMP membership, Education pricing/course structure
- RSpace: RO-Crate export, IGSN/PIDINST/RAiD identifier set, "soon" integrations board (roadmap signals)
- eLabFTW: Docker-based installation, minimum RAM/disk figures, 21 languages, Gitter community, Deltablot commercial hosting

## Historical / Market-Sample Check (per WORKFLOW §24)

Question: would older, regional, platform-native or differently positioned products still fit the proposed L0?

- **Paper lab notebook** (the pre-electronic ancestor): dated, signed entries; glued-in printouts (embedded evidence); immutable pages (tamper-evidence); archived and retrievable. → Fits L0 exactly; the L0 is deliberately the paper contract made digital. Anything the paper notebook lacks (search, templates, inventory, AI) is correctly excluded from L0.
- **Early-generation ELNs** (late-1990s/2000s page-replica notebooks, regional and in-house academic systems): pages, authorship, timestamps, export/print-to-PDF, no cloud, no inventory, no AI. → Fit L0; templates/inventory/integrations correctly excluded.
- **Self-hosted institute deployments** (eLabFTW-style): no vendor cloud, no Part 11 posture, minimal features. → Fits L0 with only items 1–4 present.
- **Notebook-module-inside-platform** (Benchling-class): the notebook is one surface of a wider R&D platform. → Still fits L0 because the experiment-record machinery remains.
- **Teaching ELNs** (LabArchives Education): the record is a student's coursework rather than novel research. → Still fits L0 (experiment-shaped records, attributed, timestamped).
- Check passed. No L0 item depends on the current dominant implementation (cloud, AI, inventory, or witnessing).

---

## Vendor-specific Findings (do not promote to canonical)

- Benchling's Registry/Results triad and sequence-aware entries — a life-sciences platform realization, not the Type.
- SciNote's status pipeline (In Progress → In review → Done) with signature-gated completion — one workflow realization.
- LabArchives' Widget library, Form Center, DOI/Figshare publishing — institutional-RDM-flavored realizations.
- RSpace's identifier stack (IGSN, PIDINST, RAiD, ROR) and RO-Crate export — FAIR/RDM positioning.
- eLabFTW's blockchain timestamping and Docker self-hosting — open-source academic realization.

## Boundary Findings

### ELN vs LIMS (and Research LIMS)
- LIMS is operation-centered: samples/ specimens flow through lab processes (accessioning, workflows, QC, results, chain of custody); the sample lifecycle is the spine. ELN is documentation-centered: the experiment record is the spine; samples/inventory may be *referenced* from records.
- Empirical seam: all five sampled ELNs ship some inventory capability, and eLabFTW's GitHub topics even include "lims"; conversely LIMS products increasingly offer ELN modules. The load-bearing test: remove the experiment record → it becomes inventory/LIMS software; remove sample workflow management → it stays an ELN.
- The directory's separate "Research LIMS" leaf suggests the boundary is expected to be refined when that leaf is processed; flag for joint review.

### ELN vs Scientific Data Management System / RDM
- RDM/repository systems hold, publish, and preserve datasets (often institution-scale, PID-oriented); the ELN's unit is the ongoing experiment record. RSpace deliberately straddles this line ("open source research data management" with an ELN product) — evidence that the market blends them, but the documentation spine remains experiment records. Publishing exports (DOI, Figshare, RO-Crate) are the hand-off seam.

### ELN vs Note-taking / Wiki / Document Editor
- Generic notes/wikis lack: experiment-record semantics, tamper-evidence (version history aimed at collaboration, not evidence), sign-off/witnessing, regulatory posture, and the container→experiment shape. Remove tamper-evidence + experiment anchoring from an ELN and you get a team wiki; that is the boundary test.

### ELN vs eTMF / Clinical trial documentation
- eTMF holds trial master file documents under trial governance; the ELN holds bench records. Adjacent in regulated settings but different unit of record and different lifecycle owner.

### ELN vs Project Management
- SciNote/Benchling carry project containers, but projects exist to organize records, not to plan/schedule/track work as a managed workflow object. PM constructs (tasks with assignees/dates) appear in ELNs as secondary conveniences.

### Taxonomy observation (record in STATUS.md)
- "Electronic Lab Notebook / ELN" appears TWICE in DIRECTORY.md (§22 Healthcare & Life Sciences AND §23 Education, Research & Knowledge Institutions) — same leaf listed in two sections. This document is produced once under the single slug electronic-lab-notebook-eln and covers both contexts. Recommend the directory maintainers consolidate or annotate the duplicate.

## Uncertainties

- eLabFTW operational detail (signing, search, templates, export formats) unverified — official docs unreachable; only README-level claims used.
- RSpace operational detail (record locking, review workflow mechanics) unverified — product-page evidence only; claims kept at marketing level ("signing & witnessing built-in").
- LabArchives e-signature mechanics (who signs, locking behavior) not fetched at article level; only feature existence asserted.
- Witnessing universality: directly evidenced in 3/5 products (2 at A level, 1 at B); treated as regulated/common rather than universal.
- Whether the market treats "ELN" and "Electronic Lab Notebook" module naming consistently when embedded in larger platforms (Benchling markets Notebook; SciNote/RSpace/LabArchives market ELN) — handled by treating the notebook machinery as the Type regardless of packaging.
- Precision on any numeric/behavioral defaults deliberately avoided (see Source-access limitation).

## Final Synthesis

The Electronic Lab Notebook is the research-side system of record for experimental work. Its world model: a durable container (notebook/project) holding experiment records (entries/experiments/pages), each an authored, timestamped, tamper-evident unit of experimental documentation carrying text plus the evidence of the work (tables, images, files, data), accumulating over years into a searchable archive that can be exported, attested (signed/witnessed/timestamped), and defended as evidence (research integrity, IP, regulatory inspection). Around this core, mature products add templates/protocols, structured capture, team permissions, inventory linkage, integrations, export/publishing, and — in regulated segments — signature/witness and compliance machinery. The Type is distinct from LIMS (sample operations vs documentation), from RDM (datasets vs experiment records), and from notes/wikis (evidence posture vs collaboration). Historically it is the paper lab notebook's contract — dated, signed, unalterable pages carrying the experiment's evidence — realized digitally; every feature newer than that contract (search engines, cloud, AI, inventory, chemistry tools) is common or variant structure, not definition.
