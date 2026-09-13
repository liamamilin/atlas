# Research Notes — Legal Drafting Platform

Research date: 2026-09-07

## Research Goal

Understand, from real products, what a Legal Drafting Platform is: what object the application works on (the draft? the precedent? the clause?), where the work happens (inside Word? a hosted editor? a separate web surface?), what legal-specific machinery the products actually apply to a draft, how suggestions and generated language enter the document, and where this Type's boundaries lie against the processed sibling Legal Document Automation, against Legal Research Platform, CLM, and the generic Document Editor.

## Initial Boundary

Working hypothesis before research:

- Core idea: software that assists the act of drafting legal documents — composing and revising legal language — with machinery that understands legal documents (defined terms, cross-references, clauses, citations) and supplies legal knowledge (precedent, clauses, standards, authorities) at drafting time.
- Likely users: transactional lawyers (firms), litigators, in-house counsel.
- Neighbors: Legal Document Automation (assembles documents from logic-bearing templates — the language pre-exists; processed sibling whose research notes name this leaf as its sharpest seam); Legal Research Platform (finding law vs writing documents); Contract Lifecycle Management (draft vs managed contract record); Document Editor (generic text editing vs legal-document machinery); Legal Contract Analytics (reads a corpus vs works on one draft).
- Unknowns: is generative AI definitional or an accretion? Is Word-native integration definitional? Is firm-precedent grounding definitional? Does the market have a coherent product family under this name? What did the Type look like before LLMs?

## Research Questions

1. What is the central object of work — the draft document, the precedent corpus, or the clause?
2. Where does drafting assistance operate — in the lawyer's editor, or in a separate surface?
3. What legal-document structures do products parse and act on (defined terms, cross-references, clauses, citations, formatting conventions)?
4. How does language enter the draft — generation, clause insertion, suggestion adoption — and who approves it?
5. What knowledge supplies the drafting (firm DMS precedent, clause libraries, playbooks, market corpora, authorities, evidence records)?
6. What verification/checking passes exist (defined terms, proofing, cite-check, risk flags)?
7. How do products handle review/negotiation (redlines, comments, counterparty positions)?
8. What integrations and security posture are standard (DMS, research providers, permissions mirroring)?
9. Where is the seam vs Legal Document Automation, Legal Research Platform, CLM, and generic editors — and would pre-AI drafting tools still fit the definition?

## Representative Products

Selection logic: market representation + documentation completeness + different product philosophies + different customer tiers. The sample intentionally spans the main philosophy poles of the current market: precedent-grounded AI drafting (enterprise firms), verification/navigation-first tooling (enterprise firms), generative copilot (SMB/in-house, self-serve), litigation drafting (evidence-citation machinery), plus one pre-generative-generation drafting tool as a historical anchor.

| Product | Philosophy / segment | Documentation accessed |
|---|---|---|
| Draftwise | Precedent-grounded AI drafting platform; Big Law + mid law + in-house; Word-native; DMS-grounded | Tier 2 (vendor home + product page) |
| Definely (Draft/Read/Proof/Vault/Cascade/Enhance) | Verification/navigation-first drafting suite; enterprise firms + in-house; Word-native | **Tier 1** (official help centre: Draft/Read overview + 15-article learning center index + Vault overview + full drafting workflow article; product pages) |
| Spellbook | Generative AI drafting/review copilot; in-house + firms, self-serve trial; Word + Google Docs | Tier 2 (vendor home + Draft feature page) |
| Clearbrief | Litigation drafting: evidence-hyperlinked citations, cite-checking, TOA machinery; litigators, courts, arbitrators; solo self-serve pole | Tier 2 (vendor site; user guides sign-in gated) |
| Thomson Reuters Drafting Assistant (historical anchor) | Pre-generative drafting toolkit: citation checking, authority location, court formatting, model documents; transactional + litigation editions | Tier 2 (vendor product page) |

Rejected candidates: Henchman (LexisNexis Clause Companion) — www and apex both transport-error ×1 each, abandoned per the network rule; recorded as market context only (clause-companion products exist as a recognized category). LexisNexis CoCounsel/Westlaw drafting surfaces — research-platform family, better used as boundary counterparty than sample.

## Sources

- Draftwise — https://www.draftwise.com/ (home; fetched 2026-09-07), https://www.draftwise.com/product (product page; fetched 2026-09-07). No public help center reachable from this environment.
- Definely — https://definely.com/ (home), /products/read, /products/proof (fetched 2026-09-07); https://help.definely.com/ (help centre root), /en-us/collections/1437106 (Definely Draft Learning Center, 15 articles), /en-us/articles/674792 (Overview of Definely Draft/Definely Read), /en-us/articles/704744 (Definely Vault: overview and getting started), /en-us/articles/704750 (Inserting a clause and resolving undefined terms: the full Definely workflow) — all fetched 2026-09-07.
- Spellbook — https://www.spellbook.legal/ (home; fetched 2026-09-07), https://www.spellbook.legal/features/draft (Draft feature page; fetched 2026-09-07). Help Centre (intercom.help/spellbooklegal) timed out ×2 — abandoned per network rule.
- Clearbrief — https://www.clearbrief.com/ (home; fetched 2026-09-07), /guides (user guides index — content sign-in gated; fetched 2026-09-07).
- Thomson Reuters Drafting Assistant — https://legal.thomsonreuters.com/en/products/drafting-assistant (fetched 2026-09-07).

## Product A — Draftwise — Tier 2 (vendor home + product page)

Evidence layer: A for vendor-stated capabilities; no operational docs reachable.

### Key observations

- Positioning: "Precedent-powered contract drafting AI… directly in Word." Workflow framed as **Draft → Review → Negotiate**.
- Grounding: "connects to your firm's complete deal history—documents, clauses, tags and all—to draft like one of your own." DMS integration (iManage, NetDocuments shown as partner logos); "mirrors your DMS permissions."
- Drafting mode: "Turn your legal direction and deal terms into client-ready drafts pulling from your most relevant precedent"; "intelligently search and analyze millions of documents in seconds to surface and apply your best negotiated language" (vendor figures kept as claims); "analyzes and understands your contracts automatically so you don't have to tag or collect precedent."
- Agentic posture: "perform deep research on your DMS, interpret redlines and comments, understand version history, and edit entire documents in minutes"; review mode "reads redlines and comments, applies patterns from past deals, and drafts responses based on your precedent"; "lawyer-quality edits… clear, easy to review, and negotiation-ready."
- Knowledge governance: "Never write another playbook" — playbooks auto-built from precedent and guidance; "smart collections, zero effort" — auto-curated contract collections per task; a Knowledge Console to "control the knowledge that powers every workflow"; a "Legal Ontology" structured intelligence layer (positions, fallbacks, counterparty patterns); Deal Table (comparing terms across past deals by client/counterparty/industry); market benchmarking against EDGAR.
- Audiences: law firms (big/mid) and in-house teams across several industries; security posture emphasized (SOC 2 Type II, ISO 27001, GDPR — vendor claims; "your data never trains public models").

## Product B — Definely — Tier 1 (official help centre) + Tier 2 (product pages)

### Key observations

- Suite shape (product pages): **Read** (navigate and understand complex contracts), **Proof** (audit and fix document errors), **Cascade** (identify ripple effects of changes and mark-up), **Enhance** (AI-powered contract analysis), **Vault** (secure document indexing and precedent search). All "in Word"; one shared side panel; deployed via Intune-class enterprise deployment (customer testimony); iManage/Word/NetDocuments/SharePoint integration logos.
- Draft/Read core (help centre, Overview article):
  - "Run a scan" → the document's defined terms and references are highlighted; "double-click any highlighted term to view its full definition in the Definely side panel"; drill into embedded references; "references open… side by side with the clause."
  - Definition/reference cards: bookmark, view control, jump around the document, search within the card, track how a term is used.
  - Editing: split-screen amendment of definitions/references "without losing your place"; compatible with Track Changes; insert new definitions "with automatic alphabetical placement and matching formatting."
  - Multi-document: link related agreements (including PDFs); cross-document defined terms; edit definitions in their source document.
  - **Definition Report**: all defined terms, undefined terms needing attention, unused definitions (with bulk delete); exportable.
  - **Reference Report**: "interactive table of contents that breaks your document down into schedules, paragraphs, clauses and sub-clauses"; jump to sections; export provisions; edited extracts can be merged back into the master document ("reincorporating changes").
  - **Extract Changes**: surfaces all tracked changes, comments and footnotes as an exportable issues list.
  - **Gaps List**: exports "anything in the document that needs attention, such as square-bracketed text, drafting notes, highlighted text and other drafting placeholders."
- Proof (product page + learning center): automated proofreading checks — "hundreds of proofreading checks with the click of a button"; placeholders/bracketed text/comments/highlights into a smart gaps list; defined terms that aren't capitalized; inconsistent formatting; incorrect spacing; number alignment; placeholder replacement of confidential details for external sharing.
- Vault (help centre overview): "your firm's intelligent precedent library… directly in Microsoft Word"; search firm precedents and personal documents; **insert clauses and definitions straight into the document** with auto-formatting and correct placement (definitions alphabetized); **compare** live draft wording against precedent clauses to see divergence from the firm's preferred position; two supply modes — connect the firm DMS (NetDocuments, iManage, SharePoint) or build a personal Vault (uploaded documents, shareable folders).
- Full drafting workflow (help centre, dedicated article) — the canonical loop, verbatim structure:
  1. Find and review the clause in Vault (check contract type, author, date).
  2. On choosing to insert, Definely **automatically scans the document** for undefined terms the insertion would introduce.
  3. Surface and insert missing definitions from Vault — auto-placed, right formatting, alphabetical.
  4. Insert the clause — auto-formatting to match the surrounding document (numbering, indentation, fonts) or yellow-highlight marking of new content; Track Changes supported.
  5. Review/update definitions in Draft (side panel, without losing place).
  6. Final check with Proof — "Changes only" view filtering to just the added content (cross-references affected by the new clause, remaining undefined/unused terms, capitalization/numbering/formatting inconsistencies introduced).
- Cascade: "identify the ripple effects of changes & mark-up" (scope from product page; learning center has 3 articles, not read).
- Enhance: "AI-powered contract analysis"; an "Ask anything" AI assistant is advertised across pages.
- Notably, the core Draft/Read/Proof machinery is **non-generative**: scanning, navigation, reports, checks, and clause/definition insertion from the firm's own library. Generative features (Enhance, Ask) are additive.

## Product C — Spellbook — Tier 2 (vendor home + Draft feature page)

### Key observations

- Positioning: "AI Contract Review and Drafting… Review contracts, draft with your standards, and search every deal you've signed"; "tuned for commercial legal work"; self-serve 7-day trial; targets in-house teams and law firms (smaller-firm-friendly posture).
- Surfaces: "Works in Word and Google Docs — draft and review… without switching windows or endless copy and paste"; Microsoft Word add-in ("right in Word").
- **Draft** feature: "Quickly draft language tailored to your agreement, based on your preferences"; "automatically detects the substance of your document to draft relevant, ready to use language" — contract type, jurisdiction, party details, writing style; "Draft from scratch or existing precedents"; "You direct which content is approved and applied."
- Clause library: "Save favourite clauses — store and access your favourite clauses and documents"; "Pull from precedents — upload documents to your Clause Library to reference key language you want to repurpose. Share documents for yourself, or make them accessible to your team"; "Insert directly without copy/paste — easily input your draft content in-line with a single click."
- **Review**: "Spot risks and add redlines to your contracts—right in Word"; Playbooks — "Encode your legal standards" (review against the organization's standards).
- **Compare/Market**: "Compare your contracts to thousands of similar agreements" (benchmarks; vendor claim).
- **Ask**: "Quick answers to complex questions" with "answers you can trust, with citations."
- **Associate**: "multi-document workflows… the first AI agent that can assemble multi-document transactions."
- Adjacent drift: "Autonomous Contract Management" (ACM) — "powering contracts end-to-end" (intake → review → insight → indexed signed-contract history) — the vendor itself is extending beyond drafting toward contract-lifecycle territory; recorded as drift, not as this Type's core.
- Multi-language drafting/review/chat claim ("140+ languages" — vendor figure, kept as claim). Security posture (SOC 2 Type II, zero data retention claims).

## Product D — Clearbrief — Tier 2 (vendor site; guides gated)

### Key observations

- Positioning: "Cite facts, not fake cases. AI for legal-grade accuracy in Word, trusted by serious litigators, in-house teams, and courts." Litigation drafting (briefs, pleadings, investigation reports, timelines).
- Core machinery: "backs every claim with clickable, verifiable citations… right in Word" — **Analyze & Add Fact-Cite**: the lawyer writes facts; the tool locates supporting text in the case's source documents (depositions, records) and inserts hyperlinked fact citations; "hyperlinked evidence."
- **Cite-checking**: hooked into LexisNexis — flags hallucinated/nonexistent case citations ("it will tell you if some of them are hallucinations" — customer quote on vendor site); cite formatting conversion between citation styles (e.g., California style ↔ Bluebook — customer quote on vendor site).
- **Output machinery**: "Magically generated Tables of Authorities, exhibits, & hyperlinked filings"; Table Builder; Timelines; Summaries; AI-generated investigation reports with hyperlinked citations; real-time trial-strategy tools (instant cross-examination outline).
- Audience breadth: large firms, in-house teams, state and federal courts, arbitrators (AAA partnership), solo practitioners; self-serve solo pricing tier exists (price recorded as vendor claim, excluded from final doc); BYO storage option.
- Historical note: product launched 2021 (vendor-stated "since our product launched in 2021") — its core (citation checking, TOA generation, hyperlinking) is non-generative machinery; generative AI is layered on.

## Product E — Thomson Reuters Drafting Assistant (historical anchor) — Tier 2 (product page)

### Key observations

- Positioning: "Start drafting legal documents faster… draft faster, locate authority, check citations, and ensure your accuracy."
- Two editions mirroring the practice split: **Transactional documents** — "integrated drafting, review, and analysis tools, model documents and automated templates, and document benchmarking"; **Litigation documents** — "prepare and format documents for court… easily cite to leading authority, and reduce citation and copy errors."
- Westlaw/Practical Law integration shown in product screenshots ("Utilize Westlaw legal research while in Drafting Assistant").
- Significance for this research: a drafting-support product whose machinery (citation checking, authority location, court formatting, model documents, benchmarking) contains **no generative language production** — evidence that the Type's machinery predates generative AI. Thomson Reuters also maintains a "Drafting software, service & guidance" category in its own navigation — the product family is an established market category, not a marketing coinage.

## Cross-product Comparison

| Dimension | Draftwise | Definely | Spellbook | Clearbrief | TR Drafting Assistant |
|---|---|---|---|---|---|
| Object of work | the draft (contract) in Word | the draft (complex contract) in Word | the draft (commercial contract) in Word/Docs | the draft (brief/pleading/timeline) in Word | the draft (transactional or litigation doc) |
| Surface | Word add-in/companion; DMS-grounded | Word add-in; shared side panel suite | Word + Google Docs | Word add-in (Microsoft AppSource distribution) | Word-integrated toolkit |
| Legal-structure machinery | precedent pattern analysis; redline/comment interpretation; position/ontology layer | defined terms (defined/undefined/unused), cross-references, clause structure, numbering, formatting, gaps | document-substance detection (type/jurisdiction/parties/style); risk flags in review | citations (facts→record; cases→authorities), citation style, TOA | citations/authorities, court formatting |
| Language supply | firm deal history (DMS, auto-curated); precedent-grounded generation | firm Vault (DMS or personal folders); clause/definition insertion; AI analysis | generative drafting from scratch + clause library of saved/uploaded precedents | evidence record + LexisNexis authorities; generative AI optional layer | model documents; automated templates; Westlaw/Practical Law content |
| Proposal→adoption posture | drafts/redlines "easy to review"; lawyer reviews | insertion marked/highlighted; Track Changes; Changes-only review | "You direct which content is approved and applied" | lawyer writes; tool adds verifiable citations; outputs reviewed | lawyer drafts; tool checks/repairs |
| Verification passes | review at firm standards; playbooks | Proof checks; Definition/Reference reports; gaps list; Cascade ripple effects | risk flags vs playbooks; market comparison; cited answers | cite-check; hallucination flagging; formatting conversion | citation checking; copy-error reduction |
| Knowledge grounding source | firm's own precedent + EDGAR benchmark | firm DMS precedent + the document itself | generative model + firm clause library + market corpus | case evidence record + LexisNexis caselaw | model documents + Westlaw/Practical Law |
| Negotiation support | redline responses; counterparty patterns; deal tables | issues lists; extract changes; compare vs firm position | redlines vs playbooks; Associate multi-doc workflows | reviewing opponent briefs via hyperlinked citations | (not evidenced at page level) |
| Generative language production | yes (current generation, agentic) | additive (Enhance/Ask); core is non-generative | yes (primary posture) | optional layer over extractive core | no |
| Customer tier | Big Law / mid law / in-house | enterprise firms + in-house | in-house + firms, self-serve trial | firms/courts/solo self-serve | firms (sales-led) |
| Practice orientation | transactional (contracts) | transactional (complex contracts) | transactional (commercial contracts) | litigation (+ investigation) | transactional + litigation editions |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three structures; remove any one and the product stops being a Legal Drafting Platform:

1. **The draft as the object of work** — a specific legal document in progress (contract, brief, pleading, opinion, letter) that a lawyer composes and revises as editable text. The platform operates on this document in place, inside the lawyer's drafting surface, and the lawyer remains the author of record. Remove it → a precedent/content library or a research tool (nothing being written); if documents are instead emitted by an engine from template-plus-data, the product is Legal Document Automation.
2. **In-place legal-document machinery** — capabilities tuned to the structure and conventions of legal documents rather than generic text: parsing and navigating defined terms, cross-references, clause organization and numbering; checking drafting conventions, formatting, and citations; supplying or generating clause language; interpreting redlines and comments. Remove it → a generic word processor or writing assistant.
3. **Proposal-and-adoption as the interaction model** — the platform proposes, surfaces, and checks; nothing becomes part of the document except through the lawyer's adoption (or an explicit run of a check the lawyer invokes). The product assists the drafting act; it does not replace it. Remove it → an assembly engine that emits finished documents from data (Document Automation) or an autonomous agent acting without review.

Domain scoping note: the machinery is defined by the legal-document workload (legal document genres, their structure and conventions, legal knowledge sources). The same assistance machinery applied to non-legal professional documents would be a different instantiation.

Historical/market-sample check: the Type demonstrably predates generative AI. Thomson Reuters' Drafting Assistant (citation checking, authority location, court formatting, model documents) and the cores of Definely Draft/Read/Proof (scan/navigation/reports/checks) and Clearbrief (cite-check, TOA, hyperlinked evidence) are non-generative machinery that fully satisfies the three structures. Generative language production — today the loudest feature of the category — is a current-market accretion, not the definition. Word-native integration is likewise the dominant but not definitional substrate (one sampled product also operates in Google Docs). Firm-precedent grounding is common but not definitional: one sampled product drafts from scratch plus a user-built clause library, and another's core machinery grounds in the document itself and the case's evidence record. Older or differently positioned drafting tools (clause banks in practice systems, citation checkers, style/format tools) fit the definition as long as legal-document machinery acts on the lawyer's draft; a bare style macro with no legal-document semantics does not.

### L1 — Common Mature Structure

- **Word-native operation** — add-in/companion architecture inside Microsoft Word (side panels, ribbon scans, in-line insertion); Google Docs support in one sampled product; the draft lives in the lawyer's existing editor, not a replacement application.
- **Precedent and clause supply** — a searchable library of trusted language feeding the draft: the firm's DMS connected and indexed (documents, clauses, tags), auto-curated collections, personal/team clause folders, uploaded precedent documents; insertion in place with auto-formatting (numbering, indentation, alphabetical placement for definitions).
- **Draft-vs-precedent comparison** — checking the live draft's wording against the organization's preferred position / firm precedent.
- **Generative drafting and revision** — producing first-draft language from instructions and document context (detected contract type, jurisdiction, parties, style); rewriting clauses per comments; first-pass redlines responding to counterparty marks. Current-market common, layered on the core.
- **Playbooks / organizational standards** — encoded preferred positions applied during review and drafting.
- **Verification passes** — defined-term reports (defined / undefined / unused), cross-reference repair, proofing checks (capitalization, numbering, spacing, placeholders), gaps lists of unresolved drafting notes, citation checking against authorities including hallucination flagging, risk flagging against standards.
- **Market / authority benchmarks** — comparing draft terms against market corpora or published authorities.
- **Negotiation support** — interpreting incoming redlines and comments, drafting responses, surfacing the organization's history with a counterparty or term.
- **Reports and exports** — issues lists, definitions/reference reports, tables of authorities, hyperlinked filings, extracted provisions with merge-back.
- **Integration spine** — DMS in (iManage/NetDocuments/SharePoint-class), legal research providers (LexisNexis/Westlaw/EDGAR-class), permissions mirroring from the DMS.
- **Confidentiality posture** — enterprise security certifications, no-training guarantees, ethical-wall-aware access (security is a first-class marketing axis in every sampled product).

### L2 — Variant / Optional Structure

- **Practice-area split** — transactional (contract machinery: terms, clauses, defined terms, playbooks) vs litigation (citation/evidence machinery: fact citations, record sources, authorities, TOAs, court formatting). Several vendors ship both as editions.
- **Grounding philosophy** — firm-precedent-first (your own deals are the supply) vs generative-first (model + curated market content) vs verification-first (the document itself plus the record/authorities).
- **Surface posture** — Word add-in dominant; Google Docs; hosted editors exist in the wider market (not directly sampled this pass — see Uncertainties).
- **Customer tier and commercial model** — sales-led enterprise (Big Law, in-house) vs self-serve trial/subscription (small firms, solos).
- **Agentic scope** — single-document assistance vs multi-document transaction workflows vs end-to-end "contract management" ambitions (the latter drifts toward CLM).
- **Generative-AI depth** — none (pre-AI machinery), additive assistant, or primary generation posture.
- **Multi-language drafting/review** (vendor-claimed breadth; not definitional).

### L3 — Vendor-specific (research notes only)

- Draftwise: "Legal Ontology", "Knowledge Console", "Playbook Studio", "Deal Table", auto-playbook/auto-collection claims; named firm customers (Orrick, Gunderson, Mishcon, Katten et al.); "millions of documents" scale claims.
- Definely: product naming (Draft/Read/Proof/Cascade/Enhance/Vault); split-screen amendment mechanics; yellow-highlight insertion convention; changes-only Proof view; Connector for Claude; licence-manager deployment.
- Spellbook: "Associate" (multi-document agent), "Ask", "Market/Compare", ACM ("Autonomous Contract Management") early-access program; "140+ languages" and "5,000+ legal teams" claims; G2 rating.
- Clearbrief: "Analyze & Add Fact-Cite", Table Builder, instant cross-examination outline; AAA partnership; Legalweek awards; "$300/month solo" pricing; "3.2M+ pleadings" claim.
- Thomson Reuters: Drafting Assistant transactional vs litigation editions; Westlaw/Practical Law integration; CoCounsel Legal as the successor AI surface ("unites research, analysis, and drafting").

## Rejected Findings

- **"Generative AI defines the Type."** Rejected: the historical anchor and the cores of two sampled products are non-generative yet fully satisfy the Type; generation is the current-market accretion. Writing the definition around generation would exclude the pre-AI generation of drafting tools and the verification-first pole.
- **"Word add-in is definitional."** Rejected: dominant substrate, but one sampled product supports Google Docs; the invariant is operating inside the lawyer's drafting surface, not Word specifically.
- **"Firm-precedent grounding is definitional."** Rejected: sampled products ground in the firm's own deals, in user-built clause libraries, in market corpora, in the document itself, and in case evidence records. The invariant is legal knowledge supply at drafting time, not the firm's DMS specifically.
- **"A chat assistant over legal questions is this Type."** Rejected: without the draft as the object of work, such products are research assistance (Legal Research Platform / AI Research Assistant territory).
- **"Playbooks are definitional."** Only 2 of 4 modern sampled products center them; common-not-core.
- **"This Type equals the drafting module of CLM."** Rejected: standalone drafting products exist without any contract record; CLM drafting modules are capabilities of that Type.
- Vendor scale/price claims ("millions of documents", "5,000+ teams", "$300/month", "3.2M+ pleadings") — vendor marketing figures; excluded from all canonical claims.

## Boundary Findings

1. **vs Legal Document Automation (§11 sibling, processed)** — sharpest seam; DISCHARGES that pass's flag from this side. Automation assembles documents from curated, pre-authored, logic-bearing templates: the language was chosen when the template was built, and the engine emits the document from captured data. A drafting platform's object of work is the lawyer's in-progress draft, worked in place with drafting-time machinery; language is proposed/generated/verified at drafting time and adopted by the lawyer. Removal tests hold both directions: remove the logic-bearing template and only drafting-time assistance remains → this Type; remove the draft-as-object and only template-plus-data production remains → automation. Market corroboration from both sides: the automation pass's sampled vendor splits its own portfolio into an assembly product and an AI-drafting product; this pass's samples contain no template-assembly machinery at all (clause insertion from a precedent library is retrieval + adoption, not logic-bearing assembly).
2. **vs Legal Research Platform (§11 sibling, unprocessed)** — the object differs: research platforms center the law (cases, statutes, secondary sources) and answer questions; drafting platforms center the document being written and consume legal knowledge in service of it. The seam is porous by design — the historical anchor embeds Westlaw inside the drafting toolkit, and research vendors now ship drafting surfaces as modules (one major vendor markets "research, analysis, and drafting in one experience"). Recommendation: keep both; the research-platform pass should treat a shipped "drafting" module as a capability unless the draft becomes the platform's object of record.
3. **vs Contract Lifecycle Management (§11, processed)** — CLM keeps the contract as a managed business record through negotiation, approval, signature, and obligations; a drafting platform works on the text of the current draft and hands off. Directly observed drift: one sampled drafting copilot now markets an "end-to-end contract management" line (intake → review → signed-contract index) — flagged as variant drift toward CLM, not part of this Type's core.
4. **vs Document Editor (§03.01)** — generic editors manipulate text without legal-document semantics; the drafting platform is a layer over the editor (add-in/companion), not a competing editor. Historical check: lawyers drafted in word processors long before any of this machinery existed; the editor alone satisfies none of the three structures.
5. **vs Generic AI writing/proofreading assistants** — same test as (4): no defined-term, cross-reference, citation, clause, or legal-convention machinery → not this Type, however good the prose help.
6. **vs Legal Contract Analytics (§11, processed)** — analytics reads a corpus of existing contracts to extract and analyze; drafting platforms produce/revise one draft. Meet where a drafting product's "compare draft to precedent" feature looks like analysis: there it is a drafting-time check, not corpus analytics.
7. **vs Law Practice Management System (§11, processed)** — the firm's business system (client → matter → money) carries no drafting machinery at its center; drafting platforms carry no client/matter/billing records. Some LPM suites embed drafting modules — capability relationship, same pattern as the automation boundary.
8. **vs Document comparison tooling (redline/compare products, adjacent)** — comparison centers the diff between two documents; drafting platforms generate redlines as part of revision. Capability overlap, different center.

Capability-vs-Type summary: knowledge supply alone → precedent library/research; editing alone → editor; generation without a document object → assistant; machinery acting on the lawyer's draft with adoption → this Type.

## Uncertainties

- **Spellbook operational depth**: help centre timed out ×2 (abandoned per network rule); evidence is Tier 2 vendor pages. Clause-library mechanics, review-scan behavior, and Associate workflow internals not directly observed; assertions kept at feature level.
- **Clearbrief operational depth**: user guides sign-in gated; evidence is the vendor site (feature-rich but not operational). Fact-cite workflow internals, record-upload mechanics, and court-specific behaviors not directly observed.
- **Draftwise**: no public help center reachable; evidence is Tier 2 vendor pages; agentic claims ("edit entire documents") are vendor-stated posture, not observed workflow.
- **Henchman / LexisNexis Clause Companion** (clause-companion category exemplar) unreachable — the category's existence is recorded as market context, no product-level claims.
- **Hosted-editor pole**: not directly sampled; the market's Word-centricity is direct evidence, the existence of hosted legal drafting editors is background knowledge only and is NOT asserted in the final document (only the Google Docs support of a sampled product is directly evidenced).
- **Pre-2000 drafting tools** (standalone citation checkers, clause banks on disk, style packs): not directly fetched; the historical check rests on the current page of a legacy-tool-class product plus structural reasoning — recorded as canonical inference, not document-verified history.
- **Regional markets**: all sampled products are US/UK-origin with global reach; jurisdiction-specific drafting conventions (e.g., civil-law jurisdictions' drafting machinery) were not observed and are not claimed.

## Final Synthesis

A Legal Drafting Platform is a lawyer-facing assistance environment whose object of work is the draft legal document itself. It operates in place — inside the lawyer's drafting surface, overwhelmingly Word — reading the draft's legal structure (defined terms, cross-references, clause organization, citations, conventions) and acting on it: navigating and repairing it, checking it, comparing it against the organization's preferred positions, and proposing or generating language drawn from legal knowledge sources (the firm's own precedent, clause libraries, market corpora, authorities, the case record). Its interaction model is proposal-and-adoption: the platform surfaces suggestions, insertions, and findings; the lawyer reviews and adopts; the document remains the lawyer's work product. Common mature structure adds Word-native integration, precedent/clause supply with in-place insertion, playbooks, generative drafting and redlining, verification passes, market benchmarks, negotiation support, reports and exports, a DMS/research-provider integration spine, and an enterprise confidentiality posture — none definitional. The Type predates generative AI (citation checkers, precedent toolkits, and navigation suites satisfy the core without generation), and it ends where language pre-exists in a template (Document Automation), where the law rather than the draft is the object (Legal Research), where the contract becomes a managed record (CLM), and where the firm's business rather than its documents is the object (LPM).
