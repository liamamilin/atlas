# Research Notes — Contract Analytics Platform

Research date: 2026-09-07
Leaf: Contract Analytics Platform (DIRECTORY §11 Legal, Risk, Compliance & Governance)
Slug: contract-analytics-platform

---

## Research Goal

Determine what a "Contract Analytics Platform" actually is as an Application Type, and resolve the standing boundary question recorded in STATUS.md Boundary Issues: a prior pass on Business Contract Administration flagged that "contract-analytics-platform (§11) looks like a capability slice of the same systems (extraction/reporting/risk scoring embedded in all sampled products)". This pass must test that verdict directly: is there a standalone market pole for contract analytics, and if so, what is its defining core and where is the seam with Contract Lifecycle Management / Business Contract Administration?

## Initial Boundary (working hypothesis before research)

- Suspected core: software that ingests contract documents and turns unstructured legal text into structured, queryable data — clause/term extraction, risk and deviation flagging, population-level reporting — typically without managing the contract's lifecycle.
- Suspected users: in-house legal/legal-ops, law-firm deal teams (M&A due diligence), procurement, real-estate/lease abstraction teams.
- Neighbors to test: Contract Lifecycle Management, Business Contract Administration (same category per prior pass), Legal Document Automation, eDiscovery Platform, Due Diligence Platform, Virtual Data Room, Spend Analysis Platform.
- Key uncertainty: standalone Type vs capability slice of CLM.

## Research Questions

1. What is the unit of work — the document, the clause, the extracted field, the review project, the portfolio?
2. How do contracts enter the system (upload, inbox, data room, repository sync)? Is the platform a system of record for contracts or a lens over documents it does not manage?
3. What extraction machinery exists (pre-trained field libraries, custom-trained fields, LLM Q&A, document classification)? How are results validated by humans?
4. What are the outputs — document-level review deliverables, risk/deviation flags, structured exports, dashboards, downstream sync?
5. Where does the workflow end? Is there any request→draft→approve→sign loop (i.e., lifecycle)?
6. What distinct market poles exist (due-diligence review, enterprise portfolio analysis, incoming-paper review automation, extraction API, human+AI service)?
7. Boundary: vs CLM/administration, vs eDiscovery, vs due-diligence/VDR platforms, vs legal drafting tools.

## Representative Products

Selection logic: market representativeness (all five are established, widely cited products), different product philosophies (law-firm diligence tool vs standalone analysis product vs broad legal-AI platform vs analytics-first CLM vs API/service pole), different customer levels (law firms, corporates, in-house teams), documentation completeness.

| Product | Pole | Evidence |
|---|---|---|
| Litera Kira | law-firm high-volume due-diligence review | A (official product page) |
| eBrevia Contract Analyzer (DFIN) | standalone contract analysis for legal teams | A (official product + category pages) |
| Luminance (Analyze module) | broad legal-AI platform, analytics module | A (official homepage + Analyze page) |
| LinkSquares (Analyze / Contract Intelligence) | analytics-first product that expanded into CLM | A (official pages + Tier-1 help center) |
| Zuva | Kira-lineage extraction AI; self-serve analyzer + API + human+AI diligence service | A (official homepage/product pages) |

Rejected/unreachable: LawGeex (incoming third-party-paper review automation pole; transport errors on two attempts — abandoned per network rule, pole under-documented here); Robin AI (transport errors on two attempts — abandoned).

## Sources

- Litera — Kira product page — https://www.litera.com/products/kira/ (fetched 2026-09-07)
- eBrevia — Contract Analyzer — https://www.ebrevia.com/contract-analyzer (fetched 2026-09-07)
- eBrevia — AI Contract Analysis Software (category explainer) — https://www.ebrevia.com/contract-analysis-software (fetched 2026-09-07)
- Luminance — homepage — https://www.luminance.com/ (fetched 2026-09-07)
- Luminance — Analyze — https://www.luminance.com/analyze/ (fetched 2026-09-07)
- LinkSquares — homepage — https://www.linksquares.com/ (fetched 2026-09-07)
- LinkSquares — Contract Intelligence — https://www.linksquares.com/contract-intelligence/ (fetched 2026-09-07)
- LinkSquares Help Center — category index — https://help.linksquares.com/hc/en-us (fetched 2026-09-07)
- LinkSquares Help Center — Quick Start - Analyze: Using the Main Agreement Page — https://help.linksquares.com/hc/en-us/articles/29570253081239 (fetched 2026-09-07)
- Zuva — homepage (sell-side M&A diligence; Analyze / API / Create products; 1,400+ AI fields; 225 doc classifications) — https://zuva.ai/ (fetched 2026-09-07)

Source-access limitation: no public operational documentation was reachable for LawGeex or Robin AI (transport errors), so the "automated review of incoming third-party paper against a policy playbook" pole is evidenced only indirectly (Luminance Negotiate positioning; eBrevia playbook-review resource links) and is treated as a variant with weaker evidence. No precise operational claims in this report depend on those two products.

---

## Product Observations

### Litera Kira (law-firm due-diligence pole) — Evidence Layer A

From https://www.litera.com/products/kira/ :

- Positioning: "Due diligence is where deals slow down... Extract key provisions, answer deal-critical questions, and report findings with confidence, with legal-grade accuracy lawyers can verify and defend."
- Extraction: "1,400+ pre-built smart fields, plus fields you train yourself"; "lawyer-trained extraction fields ready on day one".
- Review surface: "Collaborative review grids for M&A, real estate, banking and finance"; "Every document, every clause, every version, in one grid"; "Compare clauses, flag risks, and collaborate across teams in one review environment, with every finding connected to its source document."
- NL Q&A: "Query an entire contract set in natural language, or build custom fields for deal-specific questions. Every answer links back to the source contract." (Grid Chat blog post title confirms cross-document Q&A.)
- Deliverables: "Turn findings into summaries and export-ready reports without compiling results by hand."
- Governance: "Governance controls over how and where AI is applied."
- Ecosystem: works "where your team already works — Microsoft 365, Litera Transact, HighQ, Intralinks" (i.e., document systems and virtual data rooms).
- Companion product Lito: diligence reports in plain language using Kira's extraction report.
- Marketing metrics present (95%+ precision claim, 70% of top 50 firms) — treated as vendor marketing, not recorded as fact.

Observation summary: corpus of deal documents in → lawyer-trained field extraction → grid-based human review with source-linked findings → cross-set Q&A → summary/report deliverables. No lifecycle machinery (no drafting/approval/signature) appears anywhere on the page. The system of record for these documents is elsewhere (DMS/VDR).

### eBrevia Contract Analyzer (standalone analysis pole) — Evidence Layer A

From https://www.ebrevia.com/contract-analyzer and https://www.ebrevia.com/contract-analysis-software :

- Category self-definition: "Contract analysis software helps teams review and interpret contracts at scale. Instead of reading documents one by one, it makes it possible to analyze large volumes of contracts in a faster, more consistent, and more repeatable way."
- Documented workflow (five steps): 1) Upload or connect documents ("import contracts directly or connect to existing repositories, data rooms, and systems through eBrevia Connect"); 2) Extract key data automatically ("AI identifies and extracts important clauses, obligations, and metadata using 700+ pre-trained fields"); 3) Review with full context ("See extracted data alongside the source document. Click any result to jump to the exact text"); 4) Analyze across documents ("Compare provisions, cluster similar agreements, and identify patterns across your contract set"); 5) Export structured outputs ("Generate reports and datasets for workflows, audits, or decision-making").
- Review operations: "Assign documents to reviewers. Track review status (unreviewed, in progress, complete). Enable QA workflows for accuracy. Collaborate across teams and projects."
- Extraction detail: "Capture key clauses such as termination, renewal, assignment, and governing law"; "Clause-level extraction with direct source linking"; "Support for multiple contract types and languages"; custom fields "with or without training data".
- Population analysis: "Similarity clustering — group similar contracts automatically to avoid reviewing the same template repeatedly, and identify duplicate or near-duplicate agreements"; "Clause comparison — compare provisions across agreements and identify deviations from standard language"; advanced filtering by clause content/metadata/parties/dates; dashboards and reporting.
- NL Q&A: "eBrevia Lens... query contracts using natural language and get instant, context-aware answers... Answer deal-specific or compliance questions."
- Integrations: "Import contracts from data rooms, SharePoint, Box, and iManage"; "Sync extracted contract data into downstream systems"; diagram shows Salesforce, SAP, iManage, Box, Teams, Slack, HighQ, Microsoft 365.
- Use cases (own claim): M&A due diligence, contract management ("turn contracts into a usable, searchable dataset; track renewals and expiration dates"), compliance and risk analysis; the category page adds Lease Abstraction and Vendor/Procurement Review.
- Category-page capability list: data extraction (parties, dates, clauses, obligations, financial terms); contract search; risk identification (non-standard or missing clauses, unfavorable terms, deviations from templates or policies); contract comparison (templates, playbooks, other agreements); summaries and reporting.
- Direct boundary statement (FAQ): "Contract analysis software focuses on reviewing and extracting insights from contracts, while contract management software is designed to manage the lifecycle of contracts, including creation, approval, and storage."

Observation summary: the fullest public articulation of the Type's workflow; explicitly not a lifecycle system; ingestion is deliberately multi-source including deal data rooms; outputs flow onward to other systems.

### Luminance — Analyze module (broad legal-AI platform pole) — Evidence Layer A

From https://www.luminance.com/ and https://www.luminance.com/analyze/ :

- Platform spans Draft / Negotiate / Analyze / Comply / Investigate / Collaborate modules — analytics is one module of a wider legal-AI platform (relevant to capability-slice question: the same vendor ships analytics both standalone-flavored and adjacent to lifecycle modules).
- Analyze module claims: "AI organizes, understands and compares all contracts, immediately surfacing over 1,000 legal concepts"; "Deep Insights acts as an intelligent layer on top of your contract repository"; "automatic alerts for key periods such as break or termination dates"; "Ask Lumi Pro... instant, legally accurate responses to any natural language query across your organization's entire contract database"; "AI automatically identifies anomalies, trends and deviations to spot hidden risks which a user might not actively think to search for, such as a missing clause or unusual wording."
- Analyze use cases (own claim): Contract Management and Review, M&A Due Diligence, Risk Assessment, Knowledge Management, Trend Analysis and Benchmarking, Regulatory Compliance.
- Module positioning sentence: "Manage obligations and rapidly respond to business queries with at-a-glance insight into the entire contractual landscape."

Observation summary: same conceptual pipeline (organize → extract concepts → compare → alert → Q&A); the phrase "intelligent layer on top of your contract repository" is direct evidence for the lens posture. The platform also contains drafting/negotiation modules — evidence that analytics is a distinct functional center that platforms bolt other lifecycle modules onto, not merely a CLM dashboard.

### LinkSquares — Analyze / Contract Intelligence (analytics-first→CLM pole) — Evidence Layer A (incl. Tier-1 help center)

From https://www.linksquares.com/contract-intelligence/ and help center:

- Positioning: "LinkSquares contract intelligence software transforms contracts into a living source of structured, actionable data. Analyze agreements across your contract lifecycle to understand obligations, identify risk, and uncover insights... all in one connected platform."
- "Intelligent Contract Repository — Stop storing contracts. Start using them... automatically identifies key provisions, obligations, and metadata you can search, analyze, and use."
- NL Q&A: "Ask questions in plain language and get clear, direct answers across all agreements."
- Proactive risk: "LinkAI flags liability exposure, compliance gaps, and upcoming key dates automatically"; "Monitor upcoming contract renewals and obligations across your entire repository."
- Extraction scale: "LinkAI... trained on 10 million+ real legal contracts to extract 120+ data points from every agreement."
- Legacy corpora: "LinkSquares uses advanced data extraction technology to digitize and analyze legacy contracts... especially valuable during M&A due diligence, audits, or when building a centralized repository from scattered document management systems."
- Help center (Tier 1), Analyze module: "The Analyze Product is your central repository of finalized agreements. It contains both active and expired agreements. The Analyze Product generates text from all your agreements so they can be searched, filtered, and reported on and gives you a 360 view of your contracts."
  - Pending vs Processed agreements: "Pending agreements are new agreements to the platform, and will need to be approved by a Manager or Administrator level user" before entering the processed repository.
  - Filtering: high-level (name, type/tags) and advanced (terms, content, tag color, date added); extracted terms addable as columns for quick view and .xls export.
  - Navigation: Agreements, Saved Reports, Governing Summaries ("roll-up of the active language across a group of agreements, keeps track of amended language"), Dashboard, Events ("calendar or list view of upcoming term specific due dates"), Tasks.
  - Upload: single .docx/.pdf with name/type/tags; bulk upload with AI-determined "Smart Types/Tags", manual tagging, or CSV-driven tagging.
  - Individual agreement page: Terms, Summary, Info (type/tags), Links (parent/child agreements), Tasks, Notes, Attachments, index text, global terms (user- or AI-generated).
  - Separate modules exist for creation (Finalize), signature (Sign), intake prioritization (Prioritize) — the vendor's product family shows analytics as one module among lifecycle modules.
- Direct boundary statement (FAQ): "Contract management software focuses on storing, organizing, and tracking contracts through their lifecycle. Contract intelligence software goes further, using artificial intelligence and machine learning to extract structured data from agreements, surface risk patterns, track obligations automatically, and connect contract insights to broader business workflows. LinkSquares combines both in one platform."

Observation summary: the clearest case of the Type expanding into CLM — the vendor still names and badges the analytics capability (G2 "Contract Analytics" category awards) and explicitly distinguishes "contract intelligence" from "contract management" while selling both. Its Analyze module is also the one sampled product that describes itself as the central repository of finalized agreements (repository-of-record posture).

### Zuva (Kira-lineage AI; analyzer + API + human+AI service pole) — Evidence Layer A

From https://zuva.ai/ :

- Lineage: "Zuva was founded by the team behind Kira Systems... We retained a copy of the underlying Kira AI."
- Self-serve products: Analyze (extraction/reporting), API ("extraction" endpoints — API reference published), Create (creation). Resources: "AI Fields 1,400+", "Document Classification 225".
- Sell-side M&A offering: "Diligence Reviews — We pair experienced lawyers with purpose-built AI... find items like change of control implications, non-competes, exclusivity, MFN clauses, and IP assignments, and turn those findings into actionable reports and disclosure-schedule-ready outputs." Process: "Upload contracts → AI scans for risks (1,400+ legal provisions) → Lawyer reviews findings → Report delivered."
- Document classification: 225 document types (classification as a distinct layer from clause extraction).

Observation summary: demonstrates (a) the extraction field library as reusable machinery (same 1,400+ number as Kira — shared lineage, so treat the identical number as related-lineage evidence, not independent corroboration), (b) the extraction engine sold as an API capability for embedding in other systems, and (c) a human+AI service wrapper around the same machinery. Also confirms document classification as a layer distinct from clause-level extraction.

---

## Cross-product Comparison

| Dimension | Kira | eBrevia | Luminance (Analyze) | LinkSquares (Analyze) | Zuva |
|---|---|---|---|---|---|
| Corpus enters by | upload; DMS/VDR ecosystems (HighQ, Intralinks, M365) | upload or connect (data rooms, SharePoint, Box, iManage) | connected repository ("layer on top of your contract repository") | upload (single/bulk); central repository of finalized agreements | upload (service); self-serve analyze; API |
| Extraction machinery | 1,400+ pre-built smart fields + custom-trained fields | 700+ pre-trained fields + custom (Lens/Lens+, with or without training data) | 1,000+ legal concepts surfaced | 120+ data points; Smart Types/Tags | 1,400+ AI fields; 225 doc types; API |
| Source-linked results | yes ("every answer links back to the source contract"; "every finding connected to its source document") | yes ("click any result to jump to the exact text") | yes (dashboard + alerts; deviation surfacing) | yes (terms on agreement page; index text) | yes (findings contextualized by lawyers) |
| Human review workflow | collaborative review grids; findings verified by lawyers | reviewer assignment; status unreviewed/in progress/complete; QA workflows | lawyer-validated positioning ("Legal-Grade") | pending→processed approval gate by Manager/Admin | ex-Biglaw lawyers review AI findings |
| Population-level analysis | query whole set; compare clauses, flag risks | clustering, clause comparison vs standard, filtering, dashboards | anomalies/trends/deviations; benchmarking | dashboards, saved reports, governing summaries, events | disclosure-schedule-ready outputs across set |
| NL Q&A across corpus | yes (Grid Chat) | yes (Lens) | yes (Ask Lumi Pro) | yes | not observed on fetched pages |
| Outputs | summaries, export-ready reports | structured summaries/datasets; downstream sync | insights, alerts | xls export, dashboards, reports, tasks/events | actionable reports, disclosure schedules |
| Lifecycle machinery | none | none (explicitly disclaims in FAQ) | separate Draft/Negotiate modules | separate Finalize/Sign/Prioritize modules | none (Create is a separate product) |
| Repository-of-record posture | no (analysis workspace) | no (analysis + export; syncs onward) | lens over repository | yes ("central repository of finalized agreements") | no (service/API) |
| Primary audience | law firms (M&A, real estate, banking) | legal teams (corporations + law firms) | enterprise legal + business functions | in-house legal (+ sales/finance/procurement) | sell-side M&A teams |

Reading of the table:

- The pipeline ingest → extract-with-source-linking → human validation → population analysis → deliver/export is present in all five (Layer B — cross-product commonality).
- Lifecycle machinery (drafting, approval routing, signature) is absent from the analytics centers in all five; where it exists at all it is a separate module/product (Luminance Draft/Negotiate; LinkSquares Finalize/Sign/Prioritize; Zuva Create). (Layer B)
- Repository posture varies: one product is explicitly a repository of record; the others are analysis surfaces over externally-held or uploaded corpora. (Layer A per product; posture = variant, not invariant)
- NL Q&A across the corpus is near-universal in the current era (4 of 5 observed) but is an era feature, not definitional. (Layer B, common-not-core)
- Extraction-field libraries in the hundreds-to-thousands range are common (700+/1,000+/1,200-ish/1,400+ observed); exact counts are vendor marketing figures — direction (large pre-built libraries) is the reliable finding, numbers stay in Research Notes.

## Canonical Model (abstraction)

### Level 0 — Defining Invariant (deliberately small)

A Contract Analytics Platform is recognizable as this Type only with all three of:

1. **The contract corpus as analysis input.** A body of contract documents brought into the platform from outside it (uploaded sets, deal data rooms, legacy archives, connected repositories) to be analyzed as a set. The platform is a lens over documents; being their system of record or lifecycle manager is not required and usually absent.
   - Remove → generic document/NLP tooling or BI over already-structured data; no contract analysis happens.
2. **Extraction of contract content into structured, source-linked data.** The platform identifies contract-meaningful content — clauses, terms, parties, dates, obligations, metadata, document type — inside unstructured documents and records it as structured data attributed to its source text. Machine extraction (ML/LLM) is the current standard implementation; the invariant is the unstructured→structured transformation with traceability, not a specific AI technique (human abstraction is the historical implementation of the same transformation).
   - Remove → document storage or a repository; that is the CLM/administration side, not analytics.
3. **Analysis and delivery over the extracted layer.** The structured layer is worked and consumed: document-level review outputs (validated findings, summaries, comparisons against standards) and population-level outputs (search, filtering, dashboards, reports, structured exports, downstream sync, alerts on extracted dates).
   - Remove → an extraction engine/API alone (a capability, not a platform users analyze in); remove the population dimension and only single-document summarization remains.

Definition sentence for L0: *a lens that turns a corpus of contract documents into structured, source-linked contract data, and works that data into document-level and portfolio-level answers for legal and business consumers.*

### Level 1 — Common Mature Structure (common in current products; not definitional)

- Pre-built extraction-field libraries spanning hundreds to 1,400+ provisions, plus user-defined/custom fields (trained or untrained).
- Document classification into contract types (e.g., 225 doc types in one sample).
- Natural-language Q&A across the corpus with answers grounded in source text.
- Comparison against standard language / playbooks / other agreements; anomaly, deviation, and missing-clause detection ("unknown unknowns").
- Date/obligation surfacing with alerts (renewals, expirations, break/termination dates).
- Dashboards, saved reports, filtering (metadata + extracted terms), columnar term views, .xls/structured exports.
- Review operations: reviewer assignment, review-status tracking, QA workflows, approval gates for ingested documents.
- Integration both ways: ingestion from data rooms/DMS/cloud stores; extraction sync outward to downstream systems (CLM, CRM, BI).
- Role-based access, SSO, enterprise security posture; AI-governance controls over where AI is applied.

### Level 2 — Variant / Optional Structure

- Corpus scope: deal data-room set (diligence) vs enterprise legacy archive (digitization/audit) vs ongoing executed-contract population (portfolio management support).
- Repository posture: analysis lens vs repository of record (one sampled product claims the latter; most are lenses).
- Delivery form: analyst workbench vs platform module (inside a wider legal-AI suite or CLM) vs extraction API vs packaged human+AI review service.
- Audience: law-firm deal teams vs in-house legal/legal-ops vs procurement/real-estate abstraction teams.
- Playbook-driven review of incoming third-party paper (the review-automation pole — under-evidenced in this sample; see Uncertainties).
- Vertical tunings: lease abstraction, procurement/vendor review, financial-services/insurance clause regimes; multi-language support.

### Level 3 — Vendor-specific (stays in Research Notes)

- Kira Grid Chat (cross-document Q&A); Litera Lito companion; "1,400+ smart fields"; governance-controls phrasing.
- eBrevia Lens (NL Q&A), eBrevia Connect (integration layer), "700+ pre-trained fields", similarity-clustering phrasing.
- Luminance "Legal-Grade™" branding, Panel of Judges/Mixture of Experts architecture, Ask Lumi Pro, Deep Insights, "1,000+ legal concepts".
- LinkSquares LinkAI ("trained on 10 million+ contracts", "120+ data points"), Smart Types/Tags, Governing Summaries, Pending/Processed approval gate, Prioritize module.
- Zuva's identical 1,400+ field count (shared Kira lineage), Bidder Question Management product, disclosure-schedule service packaging, ~$10K–$75K deal pricing (marketing figures, not recorded as Type facts).

## Vendor-specific Findings

See Level 3. Additionally: LinkSquares is the only sampled product whose analytics module is documented (Tier 1) as the central repository of finalized agreements with a pending-approval ingestion gate — a repository-of-record posture none of the others claim. Zuva is the only sampled product packaging the machinery as a fixed-fee human+AI service and as a public extraction API.

## Rejected Findings

- "Contract analytics = CLM dashboards" (the prior capability-slice verdict): **rejected as a total verdict**. Two vendors articulate the analysis/management distinction in their own FAQs; four of five sampled products are consumable without any lifecycle machinery; ingestion is commonly from sources the platform does not manage (data rooms, legacy archives, third-party paper). The capability-slice observation is correct only for the CLM-embedded realization (see Boundary Findings).
- "AI/LLM is definitional": **rejected**. The defining transformation is unstructured→structured with source traceability; the pre-AI realization of the same job was human abstraction into term sheets/spreadsheets (§24 historical check; no pre-AI product directly researched — kept as reasoned context, not evidence-backed claim). Current products are all AI-based (observed), so AI is the standard modern implementation, documented as such.
- "Contract analytics is M&A due-diligence software": **rejected**. Diligence is the loudest pole but portfolio/compliance/abstraction use cases are documented by three sampled vendors.
- Marketing accuracy figures (95%+ precision, 90% time savings etc.): rejected as Type facts; they are vendor claims.

## Boundary Findings

| Neighboring Type | Seam | "Remove what → becomes the other Type" |
|---|---|---|
| Contract Lifecycle Management / Business Contract Administration (§11/§10) | CLM/administration is the **system of record** that manages agreements through request→draft→approve→sign→administer→renew. Contract analytics is the **legibility layer**: it makes contract content structured and queryable, over corpora it typically does not create or manage. They meet at extracted key terms (CLM repositories extract fields for administration; analytics exists for analysis) and increasingly ship in one product family. Remove lifecycle+record-keeping from an analytics product → it is just analytics; remove the extraction/analysis center from a CLM and give it dashboards only → dashboarding is a capability, and the product remains CLM. Vendor-articulated: eBrevia FAQ and LinkSquares FAQ both contrast "analysis/insight" with "managing the lifecycle/creation, approval, storage". | Take the analytics product and add managed repository + lifecycle + obligation administration → Contract Lifecycle Management. Take the CLM and strip drafting/approval/signature, leaving extraction+reporting over corpora → Contract Analytics. |
| Legal Document Automation / Legal Drafting Platform (§11) | Drafting produces contract language; analytics reads and interprets existing contract language. Reverse arrow: analytics feeds drafting standards (clause benchmarking). | Give the analytics product authoring/templating/redlining as its center → Legal Drafting. |
| eDiscovery Platform (§11) | eDiscovery reviews large document corpora for litigation/investigation with legal-hold, custodian, and production machinery; analytics reviews contract corpora for contract-meaning (clauses/terms). Corpus type and question type differ. (One sampled vendor sells an "Investigate" module for discovery-adjacent work — straddle noted.) | Point the lens at evidentiary review with hold/production workflow → eDiscovery. |
| Due Diligence Platform / Virtual Data Room (§11/§11) | VDR = controlled document sharing during deals; DD platform = deal-process management. Contract analytics = the analysis machinery whose inputs often come out of a VDR (Kira integrates HighQ/Intralinks; eBrevia imports data rooms). | Add deal/workflow/VDR hosting → DD Platform; strip analysis, keep sharing → VDR. |
| Spend Analysis Platform (§10) | Spend analysis works structured spend/transaction data; contract analytics works unstructured contract text. They meet where extracted financial terms feed spend visibility. | Change the corpus to transaction data → Spend Analysis. |
| Due Diligence "capability slice" question (prior flag) | Resolved as: analytics IS an embedded capability inside CLM products **and** a standalone Type whose market pole serves corpora no CLM holds (deal rooms, archives, third-party paper). The standalone pole is real (Kira, eBrevia, Zuva exist for it); the CLM-embedded realization is the variant that prevails inside CLM products. Both belong in the atlas; the CLM leaf should document analytics as a standard capability and cross-reference. |

Product pollution check on the synthesis: no vendor name appears in the canonical model; every L0 element is attested by 4–5 products (Layer B), with posture and delivery-form differences held at variant level.

## Uncertainties

1. **Incoming-paper review-automation pole** (policy/playbook-driven automated review-and-response on third-party contracts): intended sample (LawGeex) and backup (Robin AI) unreachable — transport errors. Pole exists per market knowledge but is documented here only via Luminance Negotiate positioning and eBrevia playbook-review resource links. Assertions about it are kept weak; no operational claims made.
2. **Historical samples**: pre-AI abstraction tooling (manual lease/contract abstraction software, spreadsheet-based abstraction) not directly researched; the claim that the Type's job predates AI is reasoned inference from the transformation-centered definition, kept out of the final document's factual claims.
3. **Numbers** (700+/1,000+/1,200+/1,400+ fields; 225 doc types; 120+ data points): vendor-marketing figures, useful only directionally; Kira and Zuva share lineage so their identical count is not independent corroboration.
4. **Market trajectory**: analytics-first products are visibly expanding into CLM (LinkSquares "Agentic CLM"; Luminance Draft/Negotiate modules; eBrevia DraftPro; Zuva Create). If the trajectory completes, the standalone pole may thin out into (a) diligence-focused workbenches/services and (b) embedded analytics. Recorded as trend, not prediction.
5. Exact permission models, export formats, and review-status vocabularies beyond what was fetched; deliberately not specified in the final document.

## Final Synthesis

Contract Analytics Platform is a real standalone Application Type — the **legibility layer** for contract documents: it takes in a corpus of contracts the platform does not have to own or manage, transforms unstructured legal text into structured, source-linked contract data (clauses, terms, parties, dates, obligations, document types), and works that data into document-level answers (validated findings, summaries, comparisons, flags) and portfolio-level answers (search, dashboards, reports, exports, alerts, downstream sync). Its center of gravity is the extraction-plus-analysis loop; drafting, approval, signature, and obligation administration belong to Contract Lifecycle Management, which analytics products either lack entirely (pure poles) or bolt on as separate modules (expanding platforms). The defining core is three-part (corpus-in → structured-with-traceability → analysis-out); AI is the standard current engine, not the definition; the review-automation and human+AI-service realizations are variants; the CLM-embedded analytics dashboard is the embedded realization of the same machinery. The prior "capability slice" flag is discharged with this refinement: slice inside CLM products, distinct Type in its own right.
