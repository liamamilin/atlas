# Research Notes — Legal Document Automation

Research date: 2026-09-07

## Research Goal

Understand, from real products, what a Legal Document Automation application is: what objects make up its world (templates, variables, answers, generated documents), how documents actually get produced, who authors the automation and who runs it, where output goes, and where this Type's boundaries lie against sibling §11 leaves (Legal Drafting Platform, Contract Lifecycle Management, Law Practice Management System) and against generic document tools.

## Initial Boundary

Working hypothesis before research:

- Core idea: software that turns reusable document templates (with placeholders and embedded logic) plus captured matter/client data into finished legal documents via an assembly engine.
- Likely users: law firms (solo → BigLaw), in-house legal, legal aid, government legal.
- Neighbors: Legal Drafting Platform (generating new language vs assembling from curated templates); CLM (manages the contract record vs produces the draft); LPM (embeds this as a capability — flagged by the LPM pass); Document Editor (edits the output); Online Form Builder (captures data without producing legal documents); Sales Document Automation (§07 sibling — same machinery, sales audience).
- Unknowns: whether the interview/questionnaire is definitional or an implementation of data capture; how template authoring works per product; whether court-form libraries are core; how answer reuse works.

## Research Questions

1. What is a template in these systems — substrate (Word/PDF/hosted form), what it carries (variables, logic)?
2. What logic do templates encode (conditionals, calculations, repeating sections, mandatory provisions)?
3. How is data captured — guided interview/questionnaire, matter-record pull, API feed?
4. What does assembly do, and how fast/automatic is it?
5. Who authors templates, and with what tooling (in-app builder, Word add-in, no-code)?
6. How are template libraries governed (versions, sets, permissions, pre-built content)?
7. What happens to generated documents (edit, download, save to matter, e-signature, regenerate)?
8. Is data entered once and reused across multiple documents (document sets/bundles)?
9. Where is the seam vs Legal Drafting Platform, CLM, LPM?

## Representative Products

Selection logic: market representation + documentation completeness + different product philosophies + different customer tiers.

| Product | Philosophy / segment | Documentation accessed |
|---|---|---|
| HotDocs (Mitratech) | Category-defining enterprise assembly engine, 30+ year lineage; legal + insurance + government; desktop + cloud | Tier 2 (vendor product page + FAQ); support center gated |
| Gavel Workflows (Gavel, fka Documate; acquired by Relativity) | No-code web platform; questionnaire→document workflows; client-facing intake and commerce; SMB→large firms | Tier 1 (official docs: product intro, structure pages) |
| Clio Draft (Clio, fka Lawyaw) | Practice-suite-embedded drafting module; hosted court-form library; Word Template Builder | Tier 1 (official help article "Draft and Manage Documents" + section index) |
| Thomson Reuters Contract Express | Corporate legal / firm self-service contract automation; low-code template authoring; Practical Law precedents | Tier 2 (vendor product page); docs gated |

Cross-check sample for historical validity: HotDocs' own "30+ years" lineage claim (vendor-stated).

## Sources

- HotDocs — https://hotdocs.com/ (product page, features, FAQ) — fetched 2026-09-07. Mitratech Success Center (https://success.mitratech.com/) — product groups do not expose a HotDocs knowledge base without login; deeper operational docs unreachable.
- Gavel — https://www.gavel.io/ (product pages) — fetched 2026-09-07; https://helpdocs.gavel.io/ (official documentation: "Intro To Document Automation", index of workflow-build pages) — fetched 2026-09-07. help.gavel.io/en/ 404 (moved to helpdocs.gavel.io).
- Clio Draft — https://help.clio.com/hc/en-us (help center root), https://help.clio.com/hc/en-us/sections/48844346336923-Clio-Draft (section index), https://help.clio.com/hc/en-us/articles/24317070863899 (Draft and Manage Documents, updated 2026-04-10) — fetched 2026-09-07. Product marketing page www.clio.com/products/clio-draft/ returned 403.
- Thomson Reuters Contract Express — https://legal.thomsonreuters.com/en/products/contract-express — fetched 2026-09-07. Product training/support portal not reachable in this environment.

## Product A — HotDocs (Mitratech) — Tier 2 (product page + FAQ)

Evidence layer: A for vendor-claimed capabilities below (vendor's own page); no help-center depth.

### Key observations

- Positioning: "converts your most-used documents and forms into intelligent templates that auto-populate from existing data sources"; "document automation and assembly".
- Production model (FAQ): "Users answer a short questionnaire, and HotDocs assembles the completed, compliant document automatically, applying conditional logic, populating jurisdiction-specific clauses, and enforcing your organization's standards every time."
- Template logic: "Smart templates that auto-populate clauses, figures, and jurisdiction-specific rules based on back-end logic"; "Business rules can be inserted to intelligently append certain clauses and stipulations that only apply to certain use cases."
- Data sources: "connects document templates directly to existing data sources (like CRM, matter management, or HR systems) and auto-populating all variable fields at generation"; open API for integrations.
- Template governance: "centralized template management system"; "built-in version control… consolidates multiple versions of legacy documents into one comprehensive template."
- Scale mode: "Batch processing that generates 500,000+ documents without manual intervention" — batch generation without an end user answering questions (vendor figure; recorded as vendor claim).
- Authoring posture: "no-code configuration so subject matter experts (not developers) can build and manage document templates… adding clauses, changing variable fields, or modifying questionnaire logic, without raising an IT ticket." Note: "questionnaire logic" is editable by template authors → the interview is derived from/maintained with the template.
- Surfaces: desktop and cloud; "works within your existing word processing environment."
- Audiences: legal (firms + in-house), insurance, financial services, government, HR — the machinery is sold as domain-general; this research's Type is the legal use of it.

## Product B — Gavel Workflows (Gavel) — Tier 1 (official docs)

### Key observations

- Core definition (docs, "Intro To Document Automation"): "A **workflow** is the core building block: it pairs a questionnaire — a series of questions you define — with one or more output document templates. When someone fills out the questionnaire, Gavel uses their answers to generate a fully populated document in seconds. No find-and-replace, no copy-paste."
- Questionnaire: "a step-by-step web form you build in Gavel's workflow editor"; each question has a unique variable name; question types (text, date, yes/no, single select, …); questions organized in pages/sections; conditional logic to "show or hide questions… based on prior answers"; instructional blocks; kickout pages.
- Templates: "One or more Word (.docx) or PDF templates you connect to the workflow. You tag each template with variable names that match your questions." Word tagging via Gavel's Word Add-in ("Gavel Document Tagger"); fillable PDFs mapped via a PDF Tagger.
- Template logic: "You can add conditional clauses, calculations, and repeating-item loops to control exactly how the answers appear in the finished document"; separate "Calculations & Advanced Logic" (complex calculations and nested logic).
- Document sets: "You can connect multiple output documents to a single workflow. For example, a contract workflow might generate a main agreement, an exhibit, and a signature document all from one questionnaire."
- Use-case spectrum (docs table): internal drafting; client intake (client supplies data, firm generates); client-facing portal (clients complete and "receive generated documents immediately"); decision trees ("guide users to a decision… rather than (or in addition to) producing documents"); paid workflows (Stripe payment gate before questionnaire or before generation).
- Content: "Legal Template Library" of pre-built automated templates and court forms, usable inside one's own account and customizable.
- Integrations: Clio, DocuSign, Zapier, API ("end-to-end automated pipeline").
- Output formats: Word documents and PDFs.
- Split-product note: the same vendor ships Gavel Exec (AI contract review/redline/drafting in Word) as a separate product line — the vendor itself separates assembly automation from AI language generation.

## Product C — Clio Draft (Clio) — Tier 1 (official help)

### Key observations

- Drafting workflow (help article, updated 2026-04): three stages — "document selection, information population, and final review."
- Document types in the library:
  - Court forms: blank hosted forms with fillable areas; Clio hosts US court forms plus Ontario and British Columbia; users can request new forms.
  - Form templates: pre-filled court forms the firm saved (e.g., firm name/address baked in).
  - Word templates: built with the Microsoft Word Template Builder.
  - Sets: "groups of forms and/or templates you compile for repeated use across similar matters."
- Data source: with the Clio Manage integration, drafting "populat[es] your Clio Manage client and matter data"; intelligent field mapping pulls regular and custom fields; related contacts auto-select onto "role cards" (e.g., an Attorney card); contact custom fields can be mapped onto form fields by naming convention.
- Enter-once/reuse: "When drafting, you only need to provide case information once. Clio Draft will then use the information to populate fields across all selected documents."
- Populate page: left panel lists documents in the set plus "Cards" (sets of related information); each card shows completion status; auto-filled fields show data provenance ("Use Clio Manage data").
- Review stage: generated documents are reviewed and edited; field-level highlighting distinguishes pre-filled (purple), matter-specific (blue), and manually edited/unlinked (grey) fields; a field can be reset to relink. Word-template outputs cannot be edited on the review page — corrections happen back at the populate stage.
- Persistent document sets: drafted sets are records that can be renamed, edited, regenerated, duplicated, and extended with more documents.
- Outputs: "Save to Clio Manage" (documents stored on the matter), Download (PDF/.docx/zip), E-sign (built-in e-signature flow).

## Product D — Thomson Reuters Contract Express — Tier 2 (product page)

### Key observations

- Positioning: "Legal document automation… Accelerate contract and document creation throughout your entire organization."
- Production model: "relying on guided questionnaires to create single documents and document suites based on the specific information you provide."
- Template authoring: "modern, low-code experience designed for legal professionals, with no need for programmers"; AI-assisted authoring; an in-product chat that "provide[s] specific code suggestions" for template logic — implies a template markup/scripting layer beneath the low-code surface.
- Content: "pre-automated and best practice templates from Practical Law (with subscription)".
- Review surface: "present completed documents for markup in Microsoft Word, where another user can validate it or suggest changes" — a distinct validator/reviewer step after generation.
- Extras: document previews, workflow and task management around the drafting process.
- Integrations: Microsoft Word, Microsoft Excel, iSheets (HighQ).
- Audiences: law firms, in-house counsel, government.

## Cross-product Comparison

| Dimension | HotDocs | Gavel Workflows | Clio Draft | Contract Express |
|---|---|---|---|---|
| Reusable logic-bearing template | intelligent templates w/ business rules, jurisdiction-specific clauses | Word/PDF templates tagged with variables; conditional clauses, calculations, repeating loops | court forms, form templates, Word templates (Template Builder) | low-code templates; pre-automated Practical Law precedents |
| Guided data capture | questionnaire (authors also edit "questionnaire logic") | questionnaire built in workflow editor | populate page with role cards | guided questionnaires |
| Data from connected systems | CRM / matter management / HR via open API | Clio, Zapier, API | Clio Manage matter/contact data sync | Word/Excel/iSheets |
| Conditional logic | yes ("back-end logic", appended clauses) | yes (questions, pages, clauses) | field mapping/linking (logic depth not directly observed) | yes |
| Multiple documents per data pass | document packages | multiple outputs per workflow ("agreement, exhibit, signature document") | Sets, up to 20 selected per set (precise cap = vendor detail) | document suites |
| Template library/governance | centralized template management + version control | legal template library; sharing | library (court forms/form templates/Word templates/sets) | pre-automated precedent library |
| Review/edit after generation | implied (works within word processing environment) | generated docs delivered; edit in Word/PDF | explicit review stage; regenerate | explicit Word markup + validation step |
| Output destinations | word processor; integrations | download Word/PDF; client portals | save to matter, download, e-sign | Word markup; iSheets |
| Batch/no-user mode | batch 500k+ (vendor claim) | not core (paid/intake flows are user-run) | not evidenced | not evidenced |
| Client-facing capture | not evidenced | client portals; client intake; paid self-serve | e-signature on outputs (client-side capture not evidenced) | not evidenced |
| Beyond-legal reach | insurance, HR, government (same engine) | legal only | legal only | legal + government |

Stable commonalities across all four (layer B): logic-bearing reusable template; a guided data-capture step; an assembly engine producing the finished document automatically from answers; multiple documents from one data pass; a managed template library; post-generation review/edit; delivery to word-processor/download/records systems.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three structures; remove any one and the product stops being a legal document automation application:

1. **The logic-bearing reusable template** — a persistent master artifact of the target document (contract, will, pleading, court form) carrying variable placeholders plus embedded assembly logic (conditional clauses, computations, repeating sections). The template is the container of drafting expertise; it is authored once and reused. Remove it → a word processor or a form-filler.
2. **Captured data bound to the template's variables** — the values (party names, dates, amounts, elections, jurisdiction) must be supplied at production time, whether typed into a guided interview or pulled from a connected matter/client system. Remove it → a static template library with no production capability.
3. **Automated assembly into a finished document** — the system evaluates the template's logic against the captured data and emits the completed document(s) without manual find-and-replace; the output is a new, editable document artifact. Remove it → data capture alone (an intake form) or authoring alone (a drafting tool).

Domain scoping note: the assembly machinery itself is domain-general (one sampled product sells the same engine to insurance and HR). What makes this Type is the legal-document workload: legal document genres, jurisdictional/practice-area logic, court forms, legal template libraries.

Historical/market-sample check: the sampled enterprise product claims a 30+ year lineage, i.e. the template+answers+assembly machinery predates client portals, cloud delivery, and AI. Desktop-era assembly (template + answer file + assembly, output to a local word processor) satisfies the same three structures; hosted court-form libraries, client-facing interviews, commerce gates, and AI authoring help are modern accretions and are NOT definitional. No fixed capture-UI form is definitional either: the interview is the standard surface, but matter-system data feeds and batch runs (no live user) satisfy the "captured data" structure in the sampled enterprise product.

### L1 — Common Mature Structure

- **Guided interview / questionnaire as the capture surface** — auto-derived from template variables (enterprise engine) or explicitly authored in a workflow editor (no-code platform); questions, pages, branching.
- **Word as native substrate; PDF as secondary** — templates authored/tagged in Word (Word add-ins/builders), outputs as .docx and PDF.
- **Template library with governance** — centralized template management, versioning, sharing; in several products a pre-built content layer (jurisdiction-hosted court forms, pre-automated precedent libraries).
- **Document sets/bundles** — one data pass populates several related documents (agreement + exhibit + signature page; a pleading set).
- **Enter-once data reuse** — answers (and/or matter-record data) populate every selected document; data provenance shown for review.
- **Post-assembly review & edit; regenerate** — generated documents are human-reviewed before use; corrections are made either in the output or by re-running assembly; template fixes propagate by regeneration, not by editing outputs.
- **Integration spine** — data in (matter management, intake, CRM), documents out (download, save to records system, e-signature service).
- **Non-developer authoring posture** — template authoring positioned for lawyers/knowledge staff rather than programmers.

### L2 — Variant / Optional Structure

- **Client-facing capture** — interviews run by clients through branded portals; client-supplied data reviewed then generated by staff; or self-serve clients receiving generated documents immediately.
- **Commerce layer** — packaging workflows as paid legal products with payment gates.
- **Hosted court-form libraries** — vendor-maintained jurisdiction forms with request-a-form services (practice-suite pole especially).
- **Batch/high-volume generation** — producing document populations from data sources without a live interview (enterprise pole).
- **Workflow layer beyond assembly** — intake→approval→generation sequences, task management around drafting.
- **AI assistance** — authoring help (natural-language guidance for template logic) is a current-generation accretion; AI contract review/redline exists in the same market but as a different product line (see Rejected Findings).
- **Deployment** — desktop, cloud, or hybrid; suite-embedded module vs standalone platform.
- **E-signature integration** as an output channel.

### L3 — Vendor-specific (research notes only)

- Gavel: "workflow/questionnaire/output-document" terminology; Document Tagger / PDF Tagger; kickout pages; decision-tree mode; Stripe paywalls; "Hire an Automator" service marketplace; Relativity acquisition; Gavel Exec product line.
- Clio Draft: purple/blue/grey field-highlight semantics; unlink/reset field mechanics; role-card ↔ related-contact mapping conventions; contact-custom-field naming rules; 20-document selection cap; Ontario/BC court forms; Clio Manage sync field-type restrictions.
- HotDocs: LegalTech Hub "Tier 1" rating claim; 1M+ users / 60+ countries / 500k batch figures (vendor claims); ARIES AI assistant; Mitratech platform bundling.
- Contract Express: Practical Law pre-automated precedent bundling; iSheets/HighQ integration; in-product template-code chat.

## Rejected Findings

- **AI drafting/generation as part of this Type's core.** The sampled no-code vendor ships AI contract review/redline/drafting as a *separate* product line from its document automation product; the enterprise vendors position AI as authoring assistance (code suggestions, drafting help), not as the assembly mechanism. AI language generation belongs to the Legal Drafting Platform seam, not to this Type's definition.
- **"Interview" as definitional.** Rejected as an invariant: the enterprise sample supports batch generation without a live interview, and matter-system data feeds replace interviews in suite-embedded deployments. The guided interview is the standard capture surface, not the invariant; the invariant is captured data itself.
- **Court-form libraries as definitional.** Only suite-embedded and template-library-pole products host forms; the enterprise and corporate poles build from the customer's own precedents. Variant, not core.
- **Batch processing as definitional.** Single-product (enterprise pole) emphasis; not required to recognize the Type.
- **"90% time reduction"-class marketing figures.** Vendor marketing; excluded from all canonical claims.

## Boundary Findings

1. **vs Legal Drafting Platform (§11 sibling)** — sharpest seam. This Type assembles documents from curated, pre-authored, logic-bearing templates: the language was chosen when the template was built, and assembly selects/fills it. A drafting platform generates or proposes new language at drafting time (AI/precedent-driven). Same vendor evidence: the sampled no-code vendor splits its own portfolio into "Workflows" (assembly) and "Exec" (AI drafting/review). Remove the logic-bearing template and only generative drafting remains → the other Type.
2. **vs Contract Lifecycle Management (§11, processed)** — CLM keeps the contract as a managed record through negotiation, approval, signature, and obligation phases; document automation's unit of work *ends* at the produced document, which may then be handed off to storage/e-signature/CLM. Document automation is the produce-the-first-draft engine that CLM deployments commonly embed. Remove the record/lifecycle machinery → this Type; remove the template/assembly machinery → CLM.
3. **vs Law Practice Management System (§11, processed)** — the LPM pass flagged that template/merge automation is embedded in every sampled LPM while standalone engines exist without matter/client/billing context. Resolution (from this side): keep both. LPM-embedded automation is a *capability* of that Type; this Type is the standalone production engine whose core carries no matter ledger, billing, or client file. The suite-embedded product sampled here (a drafting module inside a practice suite) still realizes this Type's own core (library → capture → assembly → review) as its center of gravity.
4. **vs Online Form Builder (§03.11)** — form builders capture data and route it; they do not carry document templates with conditional legal logic and do not emit assembled documents. This Type's capture surface is a means, not the product.
5. **vs Document Editor (§03.01)** — generated documents are typically edited in a word processor afterward; the editor is downstream of this Type, not this Type. Conversely, template authoring happens *inside* this Type's tooling (Word add-ins/builders) — authoring-for-automation vs authoring-for-content.
6. **vs Sales Document Automation (§07 sibling)** — the same assembly machinery applied to proposals/SOWs/quotes with CRM data; different corpus (sales documents), different users, different content governance. Same genus, different domain instantiation — keep separate, note kinship.
7. **vs Legal E-filing / court systems** — outputs may be filed, but filing is a different Type; no sampled product claims filing as its core.

Capability-vs-Type summary: data capture alone → form builder; template authoring alone → document tooling; assembly is what makes the Type; legal corpus is what scopes it.

## Uncertainties

- **HotDocs operational depth**: knowledge base gated in the research environment; all HotDocs statements are Tier 2 (vendor page/FAQ) and kept coarse. Template-authoring mechanics in its own authoring environment not directly observed.
- **Contract Express template logic specifics** (scripting layer, question types) inferred from the product page's "code suggestions" chat claim; not directly observed.
- **Clio Draft questionnaire/builder internals**: the "Questionnaires" and "Template Builder" help sections exist but only the Drafting article was read in full; conditional-logic depth in Clio Draft is not directly evidenced (field mapping/linking is).
- **Older answer-file-era assembly**: the 30-year lineage is vendor-claimed; the claim that early desktop assembly satisfied the same three structures is reasoned inference, not document-verified.
- **Non-US markets**: sampled products are US/Canada-centric in form content; regional products (e.g., UK/AU/German legal form automation) were not sampled.

## Final Synthesis

A Legal Document Automation application is a production engine for legal documents. Its center is the **logic-bearing template**: a reusable master document (contract, will, pleading, court form) whose variables and embedded logic (conditional clauses, calculations, repeating sections) encode the drafting expertise of its author. Around it sits a **capture step** — usually a guided interview, sometimes a pull from a matter/client system — that supplies the values; an **assembly engine** that evaluates the logic and emits the finished document(s) automatically; a **template library** that governs and reuses the templates; and a **review-and-delivery tail** (edit, regenerate, download, save to records, e-sign). One data pass commonly produces a set of related documents. Mature products add Word-native authoring, versioned template governance, pre-built form/precedent libraries, client-facing capture, commerce, batch mode, workflow layers, and AI authoring help — none of which are required to recognize the Type. The Type ends where lifecycle management (CLM), language generation (Legal Drafting Platform), and the firm's business system (LPM) begin.
