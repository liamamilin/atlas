# Research Notes — eDiscovery Platform

Research date: 2026-09-08
Slug: ediscovery-platform
DIRECTORY leaf: "eDiscovery Platform" (§11 Legal, Risk, Compliance & Governance)

## Research Goal

Understand what an "eDiscovery Platform" actually is as an Application Type: the end-to-end pipeline realized in real products (identify → preserve → collect → process → review → produce), the central object model (matter/case, custodian, data source, corpus, document, coding, production), who operates it and at which customer tier, how review and production actually work, and the boundaries against legal hold management, matter management, records management, digital forensics, evidence management, corporate investigations, and virtual data rooms.

## Initial Boundary

Initial hypothesis (pre-research):

- eDiscovery = the legal-discovery/disclosure process applied to electronically stored information (ESI). The platform is expected to be a matter-scoped system of record for: assembling a document corpus (collection/ingestion + processing), human document review with coded determinations (responsive / privileged / confidential / issues), and producing/disclosing documents to opposing parties or regulators (numbered, redacted, logged).
- Nearest neighbors: Legal Hold Management (the first pipeline stage — pre-hung boundary flag from the 2026-09-07 pass designates research/legal-hold-management.md as counterparty), Legal Matter Management (matter as anchor vs matter as system of record), Litigation Management Platform, Enterprise Records Management (retention vs trigger-scoped preservation), Digital Forensics Platform (§15 sibling), Evidence Management System (§24), Corporate Investigation Management, Virtual Data Room (processed 2026-09-08).
- Known confusion: "eDiscovery" names both the legal process (EDRM stages) and the software category; some products sell only one stage (collection tools, processing engines) under the same category label. Whether the full pipeline is definitional is a primary research question.

## Research Questions

1. What is the canonical end-to-end workflow as vendors themselves document it?
2. What is the core object model — what is the container (case/matter/workspace/database/project), what is a custodian, what is a document record, what attaches to documents?
3. How does review work at scale — assignments/batches/queues, coding, roles, quality control?
4. How does production work — protocols, formats, numbering (Bates), redactions, endorsements, privilege logs, clawback, re-production?
5. Which pipeline stages are bundled vs separable (legal hold? collection? processing?) — is collection-in-product definitional or a common module?
6. What roles and permissions matter (reviewers, review managers, admins, outside counsel, service-provider hosting)?
7. What "defensibility" concretely means in these products (audit trails, chain of custody, production records)?
8. Where are the boundaries with the sibling Types above?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers.

1. **Relativity (RelativityOne)** — the incumbent enterprise review-platform pole (law firms, service providers, large corporates); extremely deep official documentation at help.relativity.com (Tier 1). Philosophy: platform + developer ecosystem.
2. **Everlaw** — cloud-native modern SaaS pole; self-serve + in-house legal + firms; excellent Knowledge Base (Tier 1). Philosophy: cloud collaboration, built-in case-prep (Storybuilder), speed.
3. **Exterro** — legal-governance suite pole with legal-hold-first heritage (in-house legal/compliance audience); eDiscovery suite page (Tier 2) + hold page observed in the legal-hold pass. Philosophy: end-to-end governed workflow "from preservation through production."
4. **Microsoft Purview eDiscovery** — platform-native suite-module pole (eDiscovery shipped inside a productivity/compliance suite, staged base/premium tiers); official Microsoft Learn documentation (Tier 1). Philosophy: embedded, case-centric, source-system-native.
5. **DISCO** — cloud-native challenger pole (law firms + corporates, litigation focus); product site (Tier 2) + Ediscovery Support Center reachable (Tier 1 index). Philosophy: speed/simplicity, AI-first (Cecilia/Auto Review).

Considered and dropped: Logikcull (post-acquisition folded into Reveal docs — the legal-hold pass already observed its hold docs; self-serve pole partially covered by Everlaw), OpenText/Nuix (processing-engine pole; subsumed in the boundary analysis rather than sampled — time budget).

## Sources

Tier 1 (official operational documentation, fetched 2026-09-08):

- Relativity — RelativityOne User Documentation root (https://help.relativity.com/RelativityOne/Content/index.htm): full capability map (Collect, Processing, Legal Hold, Review, Review Center, Production, Analytics, Reporting, Data transfer/Import-Export, aiR AI suite, Case Metrics, Transcripts, Redact, FOIA app, Purview Sync).
- Relativity — "Production" (https://help.relativity.com/RelativityOne/Content/Relativity/Production/Production_overview.htm): production sets/console/placeholders/branding, Bates numbers, production information object (begin/end Bates, redactions, natives/images/PDF/placeholder counts), re-productions, security permissions; definition: "prepare documents for production—selecting non-privileged documents and turning them over to opposing counsel after review."
- Relativity — "Review Center" (https://help.relativity.com/RelativityOne/Content/Relativity/Review_Center/Review_Center.htm): queues from saved searches, reviewer check-out, AI prioritization (SVM integrative-learning classifier, relevance ranks), dashboards, templates.
- Everlaw — Knowledge Base root (https://support.everlaw.com/hc/en-us): full KB taxonomy (Administration: Project/Review/Database/Org; Uploads: native vs processed/load file; Search; Document review: coding/redaction/batch; Doc analytics: predictive coding, clustering, search-term reports, data visualizer; Production; Storybuilder; Legal Holds; AI Assistant; org analytics).
- Everlaw — "Overview: Create a Production on Everlaw" (https://support.everlaw.com/hc/en-us/articles/218312623): production protocols (rules + document set, templates, unlimited/reusable), automatic pre-production QC, initiate/monitor, ZIP packaging "shared with opposing counsel," production cards with clawback/unprivilege, multi-production privilege logs, production access logs, Bates gap report.
- Everlaw — "Introduction to Assignments" (https://support.everlaw.com/hc/en-us/articles/210222443): assignments = designated document sets per reviewer with admin-specified review criteria; assignment groups (dynamic/static) with inclusion criteria; progress dashboards; permission tiers; self-assign; search-by-assignment.
- Microsoft Learn — "Learn about eDiscovery" (https://learn.microsoft.com/en-us/purview/edisc): definition, capability table (base vs premium), case/custodian/review-set/search/hold/export descriptions, analytics (near-duplicate, email threading, themes), tagging, OCR, decryption, RBAC, guest access.
- Microsoft Learn — "Learn about the eDiscovery workflow" (https://learn.microsoft.com/en-us/purview/edisc-workflow): canonical five-step workflow (trigger → case → search/evaluate/refine → holds & export/review sets → review and act).
- DISCO — Ediscovery Support Center (https://support.csdisco.com/hc/en-us): KB index (native ingest, load file ingest, overlay, document deletion, tags, check-out batches, redactions, review stages, users/roles in review database, productions FAQ, organization & matter management).

Tier 2 (official product pages, fetched 2026-09-08):

- Exterro — eDiscovery suite page (https://www.exterro.com/e-discovery-software): capability blocks (Legal Hold & Preservation; Review & Advanced Analytics; Targeted Data Identification & Collection; Matter Management & Workflow Automation; Data Processing & ECA; Defensibility & Chain of Custody); suite portfolio (EDDM, Exterro Review, Remote Mobile Discovery, Request Management, FOIA & Public Records Response, Subpoena Manager); audience = in-house Legal and Compliance.
- DISCO — product site (https://www.csdisco.com/): DISCO Platform (Ediscovery, Hold, Request, Auto Review, Cecilia AI, Timelines, Deposition Management), professional services (managed review, forensic services & collections), verticals (law firms, corporate legal, IP litigation, plaintiffs).

Paired counterparty (already processed):

- research/legal-hold-management.md + applications/legal-hold-management.md (2026-09-07 pass) — upstream seam; its §Boundary Findings contains the pre-hung flag for this pass.

Unreachable / not attempted: none failed fatally. Relativity help root + docs index reached (2024-era 404s from the legal-hold pass were on different URLs). Logikcull not attempted (Reveal consolidation; pole covered). Nuix/OpenText not attempted (time budget; processing pole covered via other products' processing modules).

## Product Observations

### Relativity — evidence layer A (Tier-1 docs)

- **Container**: the workspace (case-scoped); RelativityOne ships workspaces per matter; a "repository workspace" concept exists for shared data. Applications (Production, Review Center, Legal Hold, Collect) are installed into workspaces.
- **Capability spine (vendor's own documentation TOC)**: Collect (data sources incl. Google Gemini, Anthropic Claude — current-era sources) → Processing → Review (+ Review Center) → Production; Analytics; Legal Hold as a sibling application; Import/Export + Staging for data transfer; Reporting/Case Metrics; Redact, Transcripts as supporting applications; aiR (AI for Review / for Privilege / for Case Strategy) as the gen-AI layer; FOIA as a dedicated application; Purview Sync (bridging Microsoft Purview holds/cases into Relativity).
- **Review at scale**: Review Center = admin builds queues from saved searches, orders documents by AI relevance predictions (SVM classifier learning from reviewer coding; rank 0–100) or custom sort; reviewers "check out documents from a simple interface"; admin monitors progress/relevance-rate dashboards; queue templates; legacy batching vs queue-batching distinction.
- **Production (deeply specified)**: "selecting non-privileged documents and turning them over to opposing counsel after review"; production sets + production data sources; production console with staging; placeholders (privilege slips) and branding; production queue + branding queue; errors + re-productions; production information object storing begin/end Bates, image counts, "has redactions", produced "with natives/images/pdf/placeholder"; deleting a production clears its Bates fields; object-level security permissions (Production, Production Data Source, Placeholder; Re-Produce mass op; "Override Production Restrictions" admin op).
- **Roles/permissions**: object-level + tab visibility + mass-op security model; Relativity certifications exist for review management, processing, analytics — evidence of specialized operator roles.
- **Defensibility**: audit/production records; re-production machinery for fixing productions.

### Everlaw — evidence layer A (Tier-1 docs)

- **Containers**: Organization → Databases → Projects (work happens in projects; legal holds live in Matters — "a space to house custodians and legal holds in the early phases, before documents are ready to upload" — and matters can be promoted into databases; per legal-hold pass).
- **Corpus assembly**: Uploads split into **native data** (product processes it) vs **processed data** (arrives as a load file produced elsewhere; standard format documented; overlaying data onto existing records). Supported native types; multiple-custodian upload handling; "Distinguish between Native and Processed Data."
- **Review**: review window (document viewer + coding panel); coding with presets and coding rules; coding history per document; context panel to batch-code related documents; batch modify; redaction (documents, spreadsheets, audio/video); notes/highlights; difference viewer; hit highlighting; chat review (native chat experience released Sept 2026).
- **Search**: query-builder with named search terms (contents, metadata, Bates/control number, codes, annotations); deduplication options; search-term reports; results table with filters and document groups; saved/shared searches; advanced content searches (wildcard/proximity/fuzzy/regex).
- **Review management**: Assignments (per-reviewer document sets with review criteria) organized in assignment groups (dynamic = auto-inclusion criteria; static = manual); dashboards with % reviewed, assigned/unassigned counts; reviewers can self-assign with permission; assignment groups linked together for staged review ("Sample Assignment Workflow — Substance Review"); search by assignment.
- **Analytics**: predictive coding (model creation, training, prioritization + QC use), clustering, email threading, data visualizer / communication visualizer, search-term reports; Everlaw AI Assistant (document search/Q&A, extractions, case description; credit-metered).
- **Production**: protocols (named rules: formats, metadata fields, numbering — "negotiated at the beginning of a case"); Everlaw-provided templates; automatic pre-production QC detecting common errors; initiate/monitor with production cards; production packaged as ZIP for opposing counsel; share productions externally with **production access logs**; clawback and unprivilege after production; multi-production privilege logs; Bates gap report; SFTP delivery; rolling productions; production notifications; Australia-specific production options.
- **Governance**: project/database permissions, document access management, approved locations, MFA, user activity analytics ("Evaluate Your Reviewers"), suspend/reactivate/delete databases, Everlaw Archive; Everlaw Government support portal exists.
- **Adjacent case-prep**: Storybuilder (narrative, depositions with transcripts/designations, drafts) — beyond discovery proper; Corporate Essentials section for in-house workflows.

### Exterro — evidence layer A- for suite structure (Tier-2 page; hold page Tier-2 from legal-hold pass)

- Positioning: "defensible workflows from preservation through production"; audience "in-house Legal and Compliance teams."
- Capability blocks (vendor's own schema.org featureList): Legal Hold & Preservation; Review & Advanced Analytics; Targeted Data Identification & Collection ("minimizing over-collection and downstream cost"); Matter Management & Workflow Automation; Data Processing & Early Case Assessment (ECA); Defensibility & Chain of Custody ("end-to-end chain of custody and complete audit logs").
- Suite portfolio: eDiscovery Data Management (EDDM), Exterro Review, Remote Mobile Discovery, Request Management, FOIA & Public Records Response, Subpoena Manager — the suite extends beyond the discovery pipeline into governance and request-response; 190+ data connectors.
- Marketing efficacy claims (excluded from final doc): "industry's fastest collection and processing engine," AI numbers.
- Operational detail below feature level is NOT available for Review/Production from this page — assertions about Exterro internals kept weak.

### Microsoft Purview eDiscovery — evidence layer A (Tier-1 docs)

- **Definition (vendor's own)**: "the process of identifying and delivering electronically stored information (ESI) that you can use as evidence in investigations and legal cases." Source systems are the suite's own services (Exchange, Teams, OneDrive, SharePoint, Groups, Viva Engage) + external-data import to review sets.
- **Canonical workflow (vendor-documented)**: trigger event (incl. escalation from Insider Risk Management cases) → create case ("contains all searches, holds, and review sets related to a specific investigation"; members control access) → search/evaluate/refine (statistics, samples, preview) → actions: export search results OR add to review sets; place holds on content locations → review in review sets (filter, analytics, tag, query reports) → export with report package.
- **Case-centricity explicit**: "In eDiscovery, cases are the primary component of the eDiscovery workflow... the case is the central organizing unit." Custodians (people of interest) + non-custodial data sources attach to cases; data-source mapping.
- **Review set**: "a secure, Microsoft-provided Azure Storage location... a static, known set of content that you can search, filter, tag, analyze, and predict relevancy using predictive coding models"; external-data import; cloud attachments; OCR; conversation threading; decryption; computed metadata exportable to third-party review applications (the suite itself exports rather than producing in the formal Bates sense at this tier — export package includes export/summary/error reports).
- **Tagging**: reviewers capture opinions as tags (e.g., "nonresponsive"); review-set queries exclude tagged-out content from subsequent steps.
- **Tier split**: base (search, hold, export, case mgmt, RBAC) vs premium (advanced indexing, review sets, analytics, OCR, threading, tagging, guest access). The base tier has NO review set — Microsoft itself realizes the pipeline in stages.
- **RBAC**: eDiscovery Manager/Administrator role groups; guest users for external reviewers; process reports/managers for long-running jobs.
- **Adjacent use**: search-and-purge of harmful content (Teams/Copilot data) — the same search machinery pointed at remediation rather than discovery.

### DISCO — evidence layer A- (Tier-1 KB index; Tier-2 product pages)

- Platform composition: Ediscovery (the core), Hold, Request, Auto Review (gen-AI first-pass review), Cecilia AI, Timelines, Deposition Management; professional services incl. **forensic services & collections** (collection externalized to services) and managed document review.
- KB structure confirms the standard machinery: native ingest, load file ingest, overlay, document deletion, tags, **check-out batches** (batch check-out to reviewers), redactions, review stages, users/roles/permissions in a review database, **organization & matter management**, fields in DISCO productions, productions FAQ, search syntax manual, cross-matter AI.
- Audience poles: law firms (Am Law 200 case studies), corporate legal, IP litigation, plaintiff/mass tort; international edisclosure case study (UK/EEA); flat-rate pricing positioning.
- Vendor metrics (87% time savings, 32,000 docs/hour, 1.4M docs to production in 4 weeks) — marketing claims, excluded from final doc.

## Cross-product Comparison

| Aspect | Relativity | Everlaw | Exterro | Microsoft Purview | DISCO |
|---|---|---|---|---|---|
| Primary audience | law firms, service providers, corporates | firms + in-house (self-serve), government portal | in-house legal/compliance | org admins inside the suite (legal/compliance/HR) | law firms + corporates |
| Container of record | workspace (per case) | database + project (matter for early phase) | matter (suite-level) | case ("central organizing unit") | matter |
| Corpus assembly | Collect app + Processing + Import/Export (load files) | native upload (processed in-product) OR load file | connectors + collection + processing (EDDM) | search/copy from source services + external import | native/load-file ingest (+ forensic services) |
| Collection in-product? | yes (app) | no (upload-based) | yes (suite) | yes (source-native) | optional (services) |
| Processing machinery | yes (documented app) | yes (on native upload) | yes (ECA framing) | yes (advanced indexing, OCR, threading, decryption) | yes (ingest) |
| Search | advanced saved searches (analytics-backed) | query builder, dedup options, term reports | (page-level claim) | KeyQL + conditions, statistics/samples | search syntax manual |
| Review management | Review Center queues + legacy batches; check-out | assignments + dynamic/static assignment groups | (module claim) | tagging in review sets (lightweight) | check-out batches + review stages |
| Coding | layouts/fields (platform-configurable) | coding panel, presets, rules, history | (module claim) | tags | tags, stages |
| Analytics/TAR | Analytics apps + Review Center AI + aiR | predictive coding, clustering, threading, visualizers | "Advanced Analytics" (claim) | near-dup, threading, themes, predictive coding | TAR 2.0 heritage, cross-matter AI, Auto Review |
| Production | production sets, Bates, placeholders, re-productions, branding | protocols, pre-prod QC, ZIP to opposing counsel, clawback, privilege logs, access logs | "streamlines production" (claim) | export packages w/ reports (formal Bates production not at this tier) | productions w/ fields, Bates warnings (overlap warnings in release notes) |
| Legal hold bundled | yes (Legal Hold app) | yes (Legal Holds tool in matters) | yes (headline module) | yes (holds in case) | yes (Hold product) |
| Privilege workflow | placeholders/privilege slips, aiR for Privilege | privilege-log machinery, QC checks | (defensibility claim) | tagging + redaction | tags + redactions |
| Defensibility articulation | production records, permissions, re-productions | coding history, QC, production access logs | "chain of custody and complete audit logs" (claim) | process reports, RBAC | (FAQ level) |
| Adjacent extensions | FOIA app, Transcripts, Case Metrics, Contracts | Storybuilder, depositions, timelines | Subpoena Manager, Request Mgmt, FOIA product | Insider-Risk escalation, search-and-purge, Copilot | Deposition Mgmt, Timelines, Request |
| Deployment posture | RelativityOne SaaS + private/hybrid + on-prem server lineage | multi-tenant SaaS (+ gov cloud portal) | SaaS platform | embedded in M365 tenant | multi-tenant SaaS (US/CA/EU logins) |

**Reading of the comparison:**

- The same four-stage machine appears everywhere: assemble a matter-bound corpus → search/cull → human-coded review organized as managed team work → a produced/disclosed deliverable with numbering, redactions, and logs. Stage *modules* (collection, processing, hold) are frequently separable and can be externalized (load files, forensic services, external processing) without the Type changing.
- Case/matter-centricity is universal; Microsoft documents it as an explicit design decision ("the case is the central organizing unit").
- The review surface differs in sophistication (queue engines vs assignment groups vs tags-in-review-sets) but the *substance* is the same: per-document determinations recorded as structured coding, plus management machinery for distributing and monitoring review work.
- Production is formalized where the litigation pole is strong (Relativity, Everlaw) and lighter where the suite/native pole treats export as the terminal step (Microsoft base tier); the conceptual output — a recorded, structured document set leaving the platform — is present in all.
- Every vendor bundles a legal hold capability; the legal-hold pass already established hold = separable first stage (Microsoft's own tier split). 5/5 bundling confirms the seam is center-of-gravity, not feature presence.
- Collection-in-product is NOT universal (Everlaw is upload-based; DISCO externalizes collection to services) — so collection machinery is a common module, not an invariant; corpus assembly through *some* ingestion path is the invariant.

## Abstraction

### L0 — Defining core (invariants; remove any one → different Type or no Type)

An eDiscovery Platform, for a specific legal matter (case, investigation, regulatory or public-records request):

1. **The matter-bound document corpus of record** — a case/matter/workspace container holding the matter's document population as individually addressable records with metadata and extracted text, assembled through ingestion (product-side collection from custodians/data sources *or* intake of externally collected/processed data such as load files). *(Remove the corpus → an empty case manager; remove the matter binding → generic archive search; remove ingestion entirely → nothing to review.)*
2. **Human-coded document review** — the defining work of the Type: reviewers examine documents and record structured determinations on the document record (responsive / not, privileged, confidentiality, issues), with the review organized as managed work at scale (assignments, batches or queues, roles, progress tracking, quality control). *(Remove → a search/processing engine or archive; the platform's center of gravity is gone.)*
3. **Production/disclosure as a managed, recorded output** — the selected document set leaves the platform as a structured deliverable (numbering, redactions, privilege treatment, defined formats/metadata), with records of what was produced and machinery to correct or redo (re-productions, clawback, privilege logs). *(Remove → a review tool with no disclosure endpoint; the discovery obligation is unfulfillable.)*

Jointly-held is load-bearing: 1 alone = EDD collection/processing tooling or a case shell; 2 alone = generic document review; 3 alone = document conversion; 1+2 without 3 = early-case-assessment tooling; 2+3 without 1 = an unmanaged review pile; 1+3 without 2 = a conversion pipeline over a case container.

### L1 — Standard capabilities (common mature structure; not definitional)

- Advanced corpus search (query languages/condition builders, metadata + content terms, saved searches, search-term reports)
- Processing machinery on ingestion: text extraction, OCR, metadata normalization, de-duplication, email threading, near-duplicate detection, conversation reconstruction
- Review management at scale: batch/queue/assignment engines, reviewer roles and check-out, progress/productivity dashboards, staged review passes (first-pass → privilege/QC)
- Analytics + TAR: clustering, themes, predictive coding / AI-assisted prioritization; current-generation generative-AI first-pass review and Q&A as an era-common layer
- Redaction (documents and, in mature products, media/spreadsheets) and privilege-log machinery
- Legal hold + custodian management bundled as the upstream stage (market norm, 5/5 sample)
- Collection/connectors into enterprise source systems (dominant in suites; externalizable)
- Early case assessment (pre-review scoping analytics)
- Import/export interchange (load files) with the surrounding ecosystem
- RBAC: case membership, reviewer vs review-manager vs admin, outside-counsel/guest access; audit trails and chain-of-custody articulation ("defensibility")
- Reporting (review progress, production reports, Bates gap reports)

### L2 — Variant / optional structure

- Deployment: multi-tenant SaaS vs single-tenant/private cloud vs government-cloud portals vs on-premises server lineage
- Operating model: self-serve corporate teams vs law-firm/service-provider-hosted (specialist admins) vs managed-review service bundles
- Trigger/regime variants: litigation, internal/regulatory investigations, second requests, FOIA/public-records requests (dedicated applications/products exist), DSAR/privacy reviews, breach response
- Suite posture: standalone platform vs module of a legal-governance suite vs platform-native inside a productivity suite (staged base/premium tiers)
- Regional practice variants (US production conventions vs international "edisclosure"; jurisdiction-specific production options)
- Adjacent case-prep extensions: story/narrative builders, deposition/transcript management, chronologies — case strategy beyond discovery proper
- Scale extremes (queues over tens of millions of documents) and cross-matter AI

### L3 — Vendor-specific (research notes only; excluded from final document)

- Relativity: Review Center SVM ranks (0–100) and hyperplane mechanics; aiR suite (for Review/Privilege/Case Strategy/Data Breach); FOIA application; Purview Sync; ARM archiving; "Override Production Restrictions" permission; workspace repository; Collect data sources for Claude/Gemini.
- Everlaw: Storybuilder; production access logs; Bates gap report; dynamic-vs-static assignment groups; Everlaw AI credit metering; approved locations; Australia production options; matter→database promotion; government support portal.
- DISCO: Cecilia AI / Auto Review (Tag Tuner); check-out batches; ediscovery ID; cross-matter AI; flat-rate pricing positioning; US/CA/EU instances.
- Microsoft: KeyQL; review sets as Azure Storage; PST exports; content-search case; search-and-purge; Insider Risk escalation; Security Copilot NL→KeyQL; E5 licensing gates; classic-experience retirement (2025-08-31) and the new unified experience.
- Exterro: 190+ connectors; ARMOUR AI framework; Employee Change Monitor (from hold pass); Subpoena Manager; Remote Mobile Discovery; marketing performance numbers.

## Vendor-specific Findings

- **FOIA/public-records packaging** — Relativity ships a FOIA application; Exterro sells FOIA & Public Records Response; the same review/production machinery pointed at a different disclosure regime. Category-relevant variant, recorded as L2.
- **Platform-native staged realization** — Microsoft's base tier (search/hold/export without review sets) demonstrates the pipeline can be sold in stages inside one product family; useful evidence for stage-separability.
- **Suite-level matter objects** — Exterro manages matters at suite level (matter management module) while review lives in a module; Everlaw separates Matters (holds phase) from Databases/Projects (review phase) — container naming varies; the *binding* of corpus+review+production to a matter is the invariant, not the container's name or feature depth.
- **Collection externalization** — Everlaw (upload-only core) and DISCO (forensic services) show collection need not be in-product.

## Rejected Findings

- "eDiscovery = collection + processing" (the tool-vendor framing): rejected as the Type's center — products without review/production are point tools; the market's platforms all center review+production.
- "Legal hold is part of the Type's definition": rejected as L0; hold is the upstream stage, bundled in 5/5 but separable (Microsoft tier split; legal-hold pass).
- "Collection machinery is definitional": rejected — load-file ingestion and service-based collection prove the corpus-assembly leg is the invariant, not in-product collection.
- "Production = Bates numbers": Bates-style numbering is the dominant convention (both deep samples document it) but the invariant is the *managed recorded deliverable*; Microsoft's export-package realization shows the number-formalization can vary by tier/regime.
- "Generative AI review is definitional": rejected — era-common layer; all five products also operate fully without it historically.
- Universal status vocabularies: rejected; container names (case/matter/workspace/database/project) and stage labels vary by product.

## Boundary Findings

- **vs Legal Hold Management (§11, processed 2026-09-07 — boundary counterparty, flag DISCHARGED this pass)**: the legal hold is the first stage of the pipeline (identify/preserve). Bundling is the market norm (Relativity Legal Hold app, Everlaw Legal Holds, Exterro Legal Hold & Preservation, DISCO Hold, Microsoft holds-in-case — 5/5). Seam = center of gravity: strip collection/processing/review/production → legal hold management remains fully itself; strip the custodian duty workflow → a pure technical hold is an archiving/records capability. Microsoft's own tiering (hold-only base tier vs custodian+notifications premium) is vendor-internal evidence of separability. **Keep-both**, with mutual cross-references.
- **vs Legal Matter Management (§11, processed 2026-09-08)**: matter-as-anchor/container (this Type: the matter scopes the corpus and the review) vs matter-as-system-of-record (matter management: status, deadlines, spend, work of the legal function). Everlaw's matter is explicitly an early-phase container before documents are ready — the container role, not the dispute-lifecycle record.
- **vs Litigation Management Platform (§11, processed 2026-09-08)**: party-side dispute system of record (pleadings, deadlines, counsel, judgments) vs document-corpus machinery. The eDiscovery platform is invoked *for* a litigated matter; it does not run the litigation.
- **vs Digital Forensics Platform (§15, processed 2026-09-08)**: investigator-facing examination of digital evidence (imaging, artifacts) vs matter-bound document corpus for legal review/production. Exterro sells both as separate product lines (eDiscovery suite vs FTK forensics) — vendor-internal seam evidence; collection is the contact point.
- **vs Evidence Management System (§24, processed 2026-09-07)**: agency custody of evidence *items* (chain of custody for physical/digital items) vs review/production of a document *corpus* under a disclosure obligation. Different objects and actors; both use custody language.
- **vs Enterprise Records Management (§10, processed 2026-09-06)**: standing retention/disposition over record classes vs trigger-scoped, matter-bound corpus assembled for disclosure. Microsoft's own guidance ("for long-term retention not related to eDiscovery investigations, use retention policies") states the seam; a hold is the suspension of that standing regime.
- **vs Virtual Data Room (§11, processed 2026-09-08)**: VDR = owner-controlled *voluntary* disclosure of a staged corpus to invited external parties for a process (deal/audit); eDiscovery = disclosure shaped by *compelled* obligations, review determinations (privilege), and production conventions. Direction of control and purpose differ; both are "controlled document disclosure" surfaces, hence the superficial similarity.
- **vs Corporate Investigation Management (§11, processed 2026-09-07)**: investigation case management (workflow/evidence-of-the-case) vs the corpus/review/production machinery used *inside* investigations. Microsoft explicitly supports investigation use and escalation from Insider Risk cases — the investigation *triggers* the eDiscovery case.
- **vs FOI / Public Records Request Platform (§24, unprocessed)**: NEW FLAG — the review/production machinery appears packaged for public-records regimes (Relativity FOIA app; Exterro FOIA & Public Records Response). Request intake/tracking vs corpus review/production is the likely seam; recommend joint review when that leaf is processed.
- **vs Enterprise Search / Internal Knowledge Search (§10)**: search here is a matter-scoped capability serving review/production, not the organization's standing search surface.

## Historical Check (§24 discipline)

1. **Paper-era discovery (pre-digital)**: producing party gathers files from custodians' offices/files; review attorneys code documents on paper coding sheets; Bates-stamp numbering applied to photocopies; typed privilege log; production of boxed copies with index to opposing counsel. Satisfies all three L0 legs: matter-bound assembled corpus (leg 1 — assembled by hand), coded human review (leg 2 — coding sheets, review teams), managed recorded production (leg 3 — Bates numbers, privilege log, production index). ✓
2. **1990s–2000s litigation-support databases (Concordance/Summation era — conceptual, no doc fetched)**: scanned/imaged documents + coded fields + OCR text in a searchable case database, Boolean search, batch review, Bates-range productions with load-file/image interchange. Satisfies the legs without cloud, TAR, dedup engines, or AI. ✓ (marked conceptual — vendor docs unreachable this pass; the load-file ecosystem evidence comes from the sampled products' own ingest documentation.)
3. **Regional/positioning breadth**: UK "edisclosure" (DISCO case study), Australian production options (Everlaw), government-cloud portals (Everlaw Government; Relativity Government docs TOC), FOIA regimes (Relativity FOIA app) — all satisfy the same core. The definition does not depend on US litigation conventions specifically; production *formalities* vary by regime (kept as variant).

Historical check **passed** — the Type digitizes a paper-era discovery workflow; none of the modern machinery (cloud, TAR, gen-AI, dedup engines, connector farms, staging areas) is definitional.

## Uncertainties

- **Exterro operational depth**: only Tier-2 suite/hold pages observed; Exterro Review/Production internals not documented at feature level. Suite-structure claims kept at page level; Exterro's inclusion still valid (hold-first suite pole), but its review machinery is asserted only directionally.
- **DISCO depth**: KB index observed; individual KB article bodies not fetched (time budget). DISCO's machinery (batches, stages, productions) asserted from index titles + product pages — moderate confidence.
- **Non-litigation regimes** (civil-law jurisdictions, arbitration, non-US regulatory disclosure): not directly researched; sampled products document investigation/FOIA triggers, so trigger breadth is documented, but region-specific formalities are not.
- **Numeric limits** (queue sizes, file-type support, export expiry windows, licensing SKUs): recorded only in these notes where observed; excluded from the final document per precision rules.
- **Processing-engine pole** (Nuix-class products marketed as eDiscovery): reasoned about, not sampled; the L0's "corpus assembly via ingestion, not in-product collection" formulation is designed to stay compatible with it, but a dedicated pass on such a product could refine the boundary.

## Final Synthesis

An eDiscovery Platform is the legal team's system of record for the document side of a disclosure obligation. Its defining core is three jointly-held structures bound to a specific matter: the document corpus of record (assembled through ingestion — product-side collection or externally processed intake — and held as searchable, metadata-bearing records); human-coded review of that corpus organized as managed team work (per-document determinations of responsiveness, privilege, confidentiality, issues, distributed through assignments/batches/queues and tracked to completion); and production/disclosure as a managed, recorded deliverable (numbered, redacted, privilege-treated document set leaving the platform, with logs and correction machinery). Legal hold is the bundled first stage, separable by design (Microsoft's tier split); collection and processing are common modules that can be externalized; analytics, TAR, and generative-AI review are era layers. The Type sits between Legal Hold Management (upstream), Legal Matter/Litigation Management (the dispute record it serves), Records Management (the standing regime it suspends), Digital Forensics (the evidence discipline it borders), and the VDR (the voluntary-disclosure counterpart). The market realizes ONE Type in poles: enterprise review platform, cloud-native SaaS, governance suite, platform-native suite module.
