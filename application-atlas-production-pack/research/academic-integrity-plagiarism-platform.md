# Research Notes — Academic Integrity / Plagiarism Platform

Research date: 2026-09-06
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what an Academic Integrity / Plagiarism Platform really is as an Application Type: what objects exist inside it, how submitted work flows through it, what the analysis produces, who consumes it, and where its boundary lies against Online Proctoring, Assessment Platforms, Assignment Management, and generic content-originality checkers.

## Initial Boundary (hypothesis before research)

- Core hypothesis: submission of written work → automated similarity analysis against recorded text corpora → evidence report for a human reviewer; the platform produces evidence, the institution adjudicates.
- Likely neighbors: Online Proctoring Platform (exam-session surveillance), Assessment Platform (delivery/scoring), Assignment Management (LMS submission collection), Peer Review Platform (scholarly review workflow), standalone AI-content detectors, consumer plagiarism checkers.
- Open questions going in: is misconduct case management in-product anywhere? How do repository/retention models differ? What roles exist?

## Research Questions

1. What is a "submission" and how does work enter the platform (web upload, LMS, API)?
2. What corpora does the analysis compare against (web, publications, student-paper repositories, user-supplied texts)?
3. What does the report contain (score, matched passages, sources, filters)?
4. What settings shape the analysis (exclusions, sensitivity, repository selection)?
5. What roles exist and who can see reports?
6. Is there an in-product integrity-case workflow, or does the report feed institutional processes?
7. How is AI-writing detection layered onto the same loop?
8. What is each vendor's stance on "similarity vs plagiarism" and human judgment?
9. What variants exist (audience, market, deployment)?

## Representative Products

| Product | Why selected | Tier of evidence |
|---|---|---|
| Turnitin (Feedback Studio / Similarity / Originality) | dominant incumbent in higher education; richest help center | Tier 1 (guides.turnitin.com) + Tier 2 |
| Copyleaks | modern SaaS; education + enterprise + API; strong developer docs | Tier 1 (docs.copyleaks.com) + Tier 2 |
| Compilatio | European (French) player; GDPR-first positioning; teacher/student/writer product split | Tier 2 (main site); support site unreachable |
| PlagiarismCheck.org | lighter/SMB tier; K-12 + higher-ed + individuals; LMS + API | Tier 2 (homepage) |

Historical / market-sample breadth (reasoning, not fetched): older and regional products — Ephorus and PlagScan (European LMS plug-ins, both later merged into Ouriginal/Turnitin), WCopyfind-style local document-comparison tools (no cloud, no repository, two-document match report), 1990s screening programs based on writing-recognition tests. The L0 below was checked to keep these inside the Type.

## Sources

- Turnitin — Feedback Studio product page: https://www.turnitin.com/products/feedback-studio (fetched 2026-09-06)
- Turnitin Guides — Academic integrity tools category: https://guides.turnitin.com/hc/en-us/categories/22037225052173-Academic-integrity-tools (fetched 2026-09-06)
- Turnitin Guides — "Understanding the similarity score": https://guides.turnitin.com/hc/en-us/articles/23435833938701-Understanding-the-similarity-score (fetched 2026-09-06)
- Turnitin Guides — "Getting Started with Authorship for Investigators": https://guides.turnitin.com/hc/en-us/articles/22040264085133-Getting-Started-with-Authorship-for-Investigators (fetched 2026-09-06)
- Copyleaks — Plagiarism Checker product page: https://copyleaks.com/plagiarism-detector (fetched 2026-09-06)
- Copyleaks API docs index: https://docs.copyleaks.com/llms.txt (fetched 2026-09-06)
- Copyleaks API docs — Data Hubs: https://docs.copyleaks.com/concepts/features/data-hubs (fetched 2026-09-06)
- Compilatio — homepage: https://www.compilatio.net/en/ (fetched 2026-09-06)
- Compilatio — "Similarities Detection": https://www.compilatio.net/en/similarities-detection-info (fetched 2026-09-06)
- PlagiarismCheck.org — homepage: https://plagiarismcheck.org/ (fetched 2026-09-06)

### Source-access limitations

- help.copyleaks.com (end-user help center) is JS-rendered and returned a CSS error shell; abandoned after one retry. Copyleaks operational evidence therefore comes from the API documentation site (Tier 1 for API surface) and the product page (Tier 2). End-user UI mechanics for Copyleaks are asserted only at product-page level.
- support.compilatio.net articles timed out / transport-errored twice; abandoned. Compilatio evidence is Tier 2 (vendor's own product/technology pages), which still directly describes the analysis pipeline, source corpora, and report contents.
- No pricing, numeric limits, or accuracy claims from any vendor were carried into the final document except where the vendor itself frames them as positioning (not operational fact).

## Product A — Turnitin (Feedback Studio / Similarity / Originality)

### Key observations (evidence layer A unless noted)

- Positioning: "Address academic misconduct, streamline feedback and grading…" — integrity + grading bundle; separate "Similarity" product line exists for institutions that want only the similarity check (product page).
- Similarity checking: "Assess originality with the Similarity Report, which compares student work against a vast collection of student submissions, premium publications, and 20+ years of internet content" (product page).
- Repository: "an unparalleled repository of student papers, current and archived web pages, and premium subscription articles from top publishers across 170 languages" (product page).
- Tier 1, similarity score article:
  - "Turnitin does not check for plagiarism in writing. We do check all submissions against our database. If any text in a submission is similar to one of our sources, these matches are highlighted for you to review."
  - Database composition: "billions of web pages: both current and archived content from the internet, a repository of works students have submitted to Turnitin in the past, and a collection of documents that comprises thousands of periodicals, journals, and publications."
  - "The similarity score is simply the percentage of text in a submission that matches other sources. Use this as a tool within your review process to make your own determination if any academic misconduct is present."
  - Color bands on the report icon (blue/green/yellow/orange/red by % range) — vendor-specific presentation; "color scheme may vary depending on the integration".
  - Exclusion filters: quotes, bibliography, small matches (word-count threshold), a student's own previous submissions. Worked examples: student name matching, draft-over-draft 100% score, properly quoted text vs copied text with similar scores.
  - Collusion detection: matching against other students' submissions on the same assignment; requires papers be added to the standard or institution paper repository and reports set to generate "immediately (can overwrite until due date)" or "on due date" — i.e., report-generation timing is a configuration that interacts with the repository.
- AI writing detection: add-on product (Originality); "AI writing indicator… integrated within the Similarity Report, shows an overall percentage of the document that AI writing tools… may have generated"; paraphrased/bypassed AI detection; aggregated AI scores across submissions (product page + guides category).
- Authorship (add-on): Authorship Report + Authorship Dashboard; "Getting Started with Authorship for Investigators" (Tier 1):
  - Audience: "academic integrity officers, student conduct officers, or whoever conducts additional investigations into severe cases of academic misconduct".
  - "Authorship for Investigators does not identify contract cheating. It takes human judgment to determine whether contract cheating has occurred based on the balance of probabilities."
  - Automates evidence-gathering: "collecting document sets for the investigation, trawling document metadata, and creating the misconduct investigation report".
  - Report built by manually uploading files to compare, or by entering a Turnitin paper ID and selecting the student's past work.
  - Accessed from the institution's Turnitin URL, not from the LMS.
- Flags Panel: "highlighting potentially manipulated text such as replaced or hidden characters" (product page).
- Delivery surfaces: web, native/API/LTI 1.3 integrations into LMSs (D2L, Canvas, Microsoft Teams, Moodle, Sakai…) (product page).
- Adjacent bundled capabilities (not integrity-core): grading/feedback tools (QuickMarks, rubrics, comments), Draft Coach (student-side citation/plagiarism/grammar guidance while writing), PeerMark (peer review assignments), Paper to Digital, multipart assignments.

## Product B — Copyleaks

### Key observations

- Positioning: plagiarism checker for education + enterprise; "detecting duplicate content, paraphrasing, source code infringement, and more" (product page).
- Similarity layers (product page FAQ): Identical / Minor changes / Paraphrased / Omitted (text excluded by scan settings, e.g., ignore quotations) — each with its own percentage in the report.
- Corpora (product page): "16,000+ open-access journals… 60 trillion websites and search engines… 1M+ internal documents… 20+ code data repositories"; cross-language detection across 30+ languages; 100+ languages for same-language scanning.
- Scan settings: customizable report; "ignore quotations" style settings; scheduled recurring scans; Google Docs add-on for in-document checking (product page).
- Repository model (Tier 1, Data Hubs):
  - Shared Data Hub: "Global database that contains millions of documents from institutions worldwide… When you index a document, it becomes available for everyone to compare against."
  - Private Cloud Hub: "Private database that is exclusive to your organization… Only you and your organization can access and compare against these documents"; team collaboration with controlled access and user management; data masking policy.
  - IndexOnly submission mode: store documents without scanning; cross-comparison scans compare all indexed documents against each other and selected databases.
  - Indexing is a choice — documents can be excluded from the Copyleaks Internal Database (llms.txt: "prevent documents from being added to the Copyleaks Internal Database").
- API lifecycle (llms.txt + Data Hubs): authenticate → submit (file / URL / OCR) → webhooks (credits checked, indexed, completed, error) → results (matched sources, matched text, AI detection) → export (PDF report, raw export to own servers); hosted web report or open-source report module for display.
- Text manipulation detection: "Detect attempts to deceive Copyleaks detection through text manipulation, and learn how the API flags these techniques" (llms.txt).
- Self-plagiarism prevention: scan ID patterns to prevent an author's documents being flagged against their own previous submissions (llms.txt).
- AI detection: separate product line (AI text/image/video detection) that pairs with the plagiarism checker; "AI Source Match" identifies sources suspected of containing AI-generated content (llms.txt).
- Management: admin.copyleaks.com — organization structure, permissions, credit allocation (llms.txt).
- Adjacent bundled capabilities: grammar checker/writing assistant, moderation API, object detection — a broader content-integrity API suite.

## Product C — Compilatio

### Key observations (Tier 2 — vendor product/technology pages; support site unreachable)

- Product split by audience: Magister (teachers, similarity), Magister+ (teachers: similarity + AI + rephrasing + translation detection), Studium (students, self-check before submission), 1D345 Copyright (writers/publishers) (homepage).
- Similarity vs plagiarism distinction, stated explicitly: "Similarities represent the matches between passages of a text under analysis and those from another source… Interpreting the percentage of similarities in a text helps determine whether it presents a risk of plagiarism." (similarities-detection page)
- Analysis pipeline (4 steps, same page): 1) text extraction (plain text only), 2) search for sources using key information in the text, 3) identifying similarities through exhaustive comparison with selected sources, 4) cleaning up results (filtering relevant passages, removing insignificant similarities).
- Similarity rate: "measures the degree of matching between two documents… quantity of passages… similar to resources from the Internet, scientific publications, student work and other academic content."
- Detection technologies: monolingual; cross-lingual (translated plagiarism); syntactic (exact + slight rewordings); semantic (profound rephrasings) — the latter two in Magister+ (same page).
- Corpora: "hundreds of billions of web pages… over a billion items of content including private publications, open-access publications, professional publishers, university and research centre repositories, website archives, student work"; plus "all documents added and managed autonomously by users or managers of client institutions, in their reference library, while respecting the confidentiality of content" (same page).
- Report contents: similarity percentage, nature of similarities (semantic/syntactic), similarity locations, list of sources, face-to-face view of the document with each source (same page).
- Teaching use case: teacher suspects heavy source use; launches multilingual comparison of the student document against the suspected source; reworded/translated passages detected; score updated — "demonstrate factually and quantify the use of the source" (same page).
- Governance stance: GDPR compliance, servers in France; "Confidentiality of documents analysed, never diffused or sold"; "Presentation of objective indicators highlighting suspicious passages in a text. Indicators to be supplemented by human analysis" (homepage).
- AI detection: percentage of AI-generated text + location of suspicious passages (homepage).
- Altered-text detection: "unrecognized languages, white characters, character substitution" (homepage).
- Delivery: native LMS integrations (Moodle, Canvas, Brightspace, Microsoft Teams, Blackboard…), SSO, API for institutional subscriptions (homepage FAQ).
- Awareness/education resources: training, webinars, "Infoplag", awareness-raising positioning ("not in a punitive way but in a process of raising awareness") (homepage testimonials/FAQ).

## Product D — PlagiarismCheck.org

### Key observations (Tier 2 — homepage)

- Positioning: "check text originality, verify authorship, trace AI-generated content, and improve writing"; audiences: K-12, higher ed, teachers, individuals, business.
- Report: "Our detector shows the similarity percent"; "All links to the sources can be found easily… follow the hyperlinks if you need to review the original materials"; downloadable/interactive reports.
- Detection claims (positioning): exact matches, word substitutions, rearrangements in word order/sentence structure, hidden symbols/Cyrillic substitution; AI detection ("TraceGPT") as separate product.
- Quotation handling: "distinguishes between plagiarism and quotation, not marking references and citations as similarity by default."
- Custom comparison sources: "if you want to analyze your files against some specific texts that aren't in our system, you can upload them and run checks" — e.g., checking whether students copied from one another (batch comparison).
- Authorship: "Fingerprint… verify the authorship and originality of a student's paper. The tool automatically compares the work to the student's previous writing style and checks for signs of writing by someone else" — positioned as unique.
- Delivery: LMS integrations (Moodle, Canvas, Google Classroom, Schoology, Brightspace, Blackboard, Populi), Google Docs add-on, Chrome extension, API for developers.
- Packaging: individual plans vs organization plans (K-12, higher ed, research institutions, businesses).
- Adjacent bundled capabilities: grammar checker, citation generator, essay grader, topic generator.

## Cross-product Comparison

| Aspect | Turnitin | Copyleaks | Compilatio | PlagiarismCheck.org |
|---|---|---|---|---|
| Submission unit | a student paper submitted to an assignment (or uploaded) | a scan (file/URL/OCR text) | a document analyzed in a class/context | a text/file checked |
| Entry surfaces | web, LMS (native/LTI/API) | web app, LMS, API, Google Docs add-on | web app, LMS, SSO, API | web, LMS, API, Google Docs add-on, Chrome ext. |
| Comparison corpora | web (current+archived), student-paper repository, publications | web, open-access journals, internal DB, code repos, private hub | web, publications, student work, institution-managed reference library | own database + real-time search + user-uploaded texts |
| Report | Similarity Report: % score, color band, match overview, filters, flags panel | % + identical/minor/paraphrased layers + matched sources; hosted/PDF/open-source report | similarity rate, nature (semantic/syntactic), locations, source list, face-to-face view | similarity %, source links, highlighted matches, downloadable report |
| Exclusions/settings | quotes, bibliography, small matches, own previous drafts; repository selection; report-generation timing | detection levels, quote/citation/template exclusions, indexing choice | package-level detection tech; institution reference library | quotation vs similarity default; custom source upload |
| Repository posture | standard + institution repositories; collusion detection via repository | Shared Data Hub (global) vs Private Cloud Hub (org-private) vs none | confidentiality-first; institution-managed library; "never diffused or sold" | own DB; no cross-institution sharing evidenced |
| AI-writing detection | add-on (Originality), % + location, aggregated views | product line paired with plagiarism checker | Magister+/Studium feature | separate product (TraceGPT) |
| Authorship/investigation | Authorship Report for investigators (contract-cheating evidence) | — (not evidenced) | — (not evidenced) | Fingerprint (style comparison vs student's past work) |
| Text-manipulation flags | Flags Panel (replaced/hidden characters) | text-manipulation flags in API | altered-texts checker | hidden symbols/substitution detection |
| Human-judgment stance | explicit Tier 1: "does not check for plagiarism… make your own determination" | report for interpretation; "can potentially miss" | "indicators to be supplemented by human analysis" | distinguishes quotation; consequences framed institutionally |
| Adjacent bundles | grading/feedback, peer review, draft coaching | grammar API, moderation, image/video detection | awareness/training resources | grammar, citation, essay grading |

## Canonical Abstraction

### L0 — Defining Invariant

```text
Submission of written work as an analyzable record
└── Automated comparison against corpora of recorded text
    (web, publications, other submitted/student work, user-supplied texts)
    └── Similarity evidence report:
        score + matched passages + identified sources
        └── delivered to a human reviewer for an integrity determination
            the platform itself does not make
```

Four properties. Remove any one and the Type stops being recognizable:

1. **Submitted written work as record** — a document enters the platform and becomes an analyzable object tied to a submitter/context. Without it there is nothing to check.
2. **Automated comparison against recorded text corpora** — the engine matches the submission against sources of recorded text. Without comparison there is no similarity evidence (this is what separates the Type from standalone AI-writing classifiers).
3. **Evidence report** — score + matched passages + identified sources, reviewable in place (highlights, source list, side-by-side). Without the report the analysis has no user-facing deliverable.
4. **Evidence, not verdict** — every sampled vendor states the platform does not itself determine plagiarism/misconduct; the report feeds a human/institutional judgment. A tool that auto-punishes would be a different (and unrecognizable) product.

### L1 — Common Mature Structure

- Similarity score as a percentage of matched text, with visual indicator
- Matched-source list (links/identifiers) and matched-passage navigation; side-by-side / face-to-face views
- Exclusion filters and scan settings (quotes, bibliography/citations, small matches, template text, custom sources)
- Repository layer: institutional and/or cross-institution stores of past submissions; opt-in indexing; collusion/self-plagiarism handling
- LMS integration (native/LTI) + API + direct web upload; downloadable/shareable reports
- AI-writing detection as an add-on/module on the same submission→report loop
- Paraphrase and cross-language (translated-plagiarism) detection
- Text-manipulation / hidden-character flags
- Role separation: student submitter, instructor/reviewer, administrator; report-visibility rules
- Student-facing self-check mode (check work before final submission)

### L2 — Variant / Optional Structure

- Repository posture: global shared hub vs institution-private vs confidentiality-first (no sharing); GDPR/server-location posture as a market differentiator (European vendors)
- Bundle depth: pure similarity check vs similarity + grading/feedback suite vs broader content-integrity API (grammar, moderation, image/video)
- Audience packaging: institution/teacher vs student self-check vs writers/publishers (pre-publication originality) vs enterprise/API
- Authorship / contract-cheating investigation support (style-over-time comparison, metadata trawling, investigation reports)
- Code plagiarism detection (source-code as submission type)
- Awareness/education programs bundled with the tool
- Deployment surface emphasis: LMS-embedded vs standalone web vs API-first

### L3 — Vendor-specific (research notes only)

- Turnitin: color-band scheme (blue/green/yellow/orange/red), Match Groups, Flags Panel, QuickMarks/rubrics/PeerMark/Draft Coach, Clarity Writing Report, Paper to Digital, "20+ years of internet content" and "170 languages" marketing figures, Authorship for Investigators as separately licensed module
- Copyleaks: credits model, IndexOnly action=2, sandbox mode, 48h tokens, Shared Data Hub vs Private Cloud Hub naming, AI Source Match, GenAI Scan Overview, hosted vs open-source report modules, MCP server, "60 trillion websites / 16,000+ journals / 99% accuracy" marketing figures
- Compilatio: Magister / Magister+ / Studium / 1D345 Copyright packaging, Infoplag, French servers, "hundreds of billions of web pages / 1,100 institutions" figures
- PlagiarismCheck.org: Fingerprint, TraceGPT, named per-page pricing tiers, "1,000,000+ users / 21,000,000+ texts" figures

## Rejected Findings

- "Plagiarism detection" as literal verdict machinery — rejected as defining structure. All four vendors explicitly frame output as similarity evidence requiring human interpretation; two state it in Tier 1 text. The Type is an evidence producer.
- "AI-writing detection" as part of the defining core — rejected. It is absent from the historical Type, is sold as an add-on/module in every sampled product, and standalone AI detectors exist outside this Type. It rides the same submission→report loop, so it is L1 (modern common) not L0.
- "Cloud student-paper repository" as defining — rejected by the historical check (local two-document comparison tools satisfy the Type without any repository) and by Copyleaks' explicit indexing opt-out and Compilatio's confidentiality stance. Repository is L1/L2.
- "Grading/feedback tools" as part of the Type — rejected; bundling in one dominant product (Feedback Studio) does not make grading structural. A pure similarity product (Turnitin Similarity line, PlagiarismCheck) exists without it.
- "Similarity percentage thresholds = plagiarism verdicts" — rejected; vendors explicitly warn against threshold-based determination (Turnitin scoring scenarios: quoted vs copied text with near-identical scores).
- Marketing figures (corpus sizes, accuracy %, user counts) — rejected as operational facts; positioning only.

## Boundary Findings

1. **vs Online Proctoring Platform** (sibling under §23): proctoring observes the live exam-taking process (identity, environment, behavior) in real time; this Type analyzes submitted written artifacts after the fact. Structural test: remove live session surveillance → this Type remains; remove artifact analysis → proctoring remains. Clean split; both are sold under "academic integrity" umbrellas, which is the main confusion risk.
2. **vs Assessment Platform / Examination Platform**: those deliver, proctor, and score assessments; this Type evaluates originality/authenticity of written work and produces no grade. A similarity report is not a score of correctness. (Turnitin bundles grading in Feedback Studio — bundling, not structure.)
3. **vs Assignment Management (LMS)**: LMS assignment flow collects and returns student work; this Type consumes submissions and returns integrity evidence. The plagiarism platform is typically embedded in the LMS flow (LTI) rather than replacing it.
4. **vs Peer Review Platform**: peer review orchestrates reviewer assignment and critique for scholarly manuscripts; similarity checking is one input editorial systems consume (e.g., iThenticate in publishing workflows). Different center of gravity; the publishing market is a variant audience of this Type (Compilatio 1D345, Copyleaks publishers use case).
5. **vs generic content-originality checkers (consumer/SEO tools)**: same core loop (text in → matches out), but no institutional roles, no student repository, no integrity-policy context. A gradient, not a wall; the academic-integrity framing (courses, submitters, repositories, adjudication) is what makes this a distinct Type.
6. **vs standalone AI-content detectors**: AI detection is a capability layer here; standalone detectors lack the source-comparison/similarity-report core and the institutional workflow. Products that only classify AI-vs-human sit outside this Type (boundary to revisit if the market converges).
7. **Misconduct case management**: in the researched sample, in-product support stops at evidence-gathering (investigator dashboards, authorship/style reports, investigation report assembly). Hearings, sanctions, and conduct records belong to student-conduct systems outside this Type. The "Academic Integrity" half of the leaf name is realized as evidence support, not case management.

## Uncertainties

- Copyleaks end-user UI mechanics (report viewer details, student view) unverified — help center inaccessible; asserted only at product-page/API level.
- Compilatio operational details (exact filter options, report-generation settings) unverified — support site unreachable; pipeline and report contents come from vendor technology pages (Tier 2).
- Whether any sampled product offers full in-product misconduct case management (hearing scheduling, sanction records) — not evidenced; treated as outside the Type.
- Exact repository retention/visibility policies per vendor (who can match against whose papers, retention duration) — only the structural options (shared vs private vs opt-in) are evidenced; policy details vary and were not researched to the precision level.
- Student report visibility rules (when students may see their own reports) — known to be configuration-dependent; not researched to the precision level.

## Final Synthesis

The Type is an **evidence-producing pipeline for written-work originality**: submitted work is compared automatically against corpora of recorded text, and the output is a similarity report — percentage, matched passages, identified sources — built for a human reviewer inside an institutional integrity process. The defining core is deliberately small (submission → comparison → evidence report → human determination). Everything the modern market associates with the category — repositories of past student work, LMS embedding, AI-writing detection, paraphrase/cross-language matching, authorship investigation, exclusion filters — is common mature structure or variant structure, not definition. The historical check holds: a two-document local comparison tool and a GDPR-first European LMS plug-in satisfy the same core as the dominant cloud incumbent. The platform never adjudicates; that boundary is stated by every sampled vendor and is part of what makes the Type recognizable.
