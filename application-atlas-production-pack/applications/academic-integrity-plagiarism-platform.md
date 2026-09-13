# Academic Integrity / Plagiarism Platform

## Overview

An **Academic Integrity / Plagiarism Platform** is software that takes submitted written work, automatically compares it against large corpora of recorded text — web content, publications, and previously submitted student work — and produces a **similarity report**: the percentage of text that matches recorded sources, the matched passages themselves, and the sources they match.

The platform's defining posture is that it produces **evidence, not verdicts**. A high similarity score is not, by itself, a finding of plagiarism; the report is built for a human reviewer — an instructor, integrity officer, or editor — who interprets it under the institution's own policy. Every major product in this category states this explicitly in its own documentation.

What the category does *not* cover: watching students take exams in real time (that is online proctoring), delivering and scoring assessments, or managing misconduct hearings and sanctions. It sits inside the integrity process as the analysis-and-evidence step.

## Users & Context

**Primary users:**

- **Instructors / reviewers** — submit or receive student work for checking, read the similarity report, decide whether matches are acceptable (quoted, cited, common phrasing) or suspicious, and escalate when needed.
- **Students** — submit work through a course assignment; in many products they may also run self-checks on drafts before final submission and see (depending on settings) the report for their own work.

**Secondary users:**

- **Integrity officers / administrators** — configure institutional settings (which repositories to search, what to exclude, who sees reports), and in some products use investigation-oriented views that gather evidence about a suspected case.
- **Researchers, editors, and publishers** — a related audience that runs the same kind of check on manuscripts before publication rather than on coursework.

The typical context is an educational institution with an academic-integrity policy: work flows from a course assignment into the platform, the report flows back to the instructor, and any disciplinary consequence happens in institutional processes outside the platform.

## Core Model

The platform's world is built around five structures.

### Submission

The central record: a piece of written work (essay, thesis, report, article — sometimes source code) that has been submitted into the platform for checking. A submission carries the document's text, its submitter, and usually the course or assignment context it belongs to. Submissions arrive by direct upload, through a learning-management-system assignment, or programmatically through an API.

### Source corpora

The bodies of recorded text the submission is compared against. Conceptually one comparison surface, operationally several layers that products combine:

- the live and archived web
- publications: journals, periodicals, publisher content, open-access repositories
- previously submitted student work, held in repositories (see below)
- texts the institution or reviewer supplies itself (course packs, internal documents, suspected sources)

### Similarity report

The deliverable. Its stable anatomy across the category:

- a **similarity score** — the percentage of the submitted text that matches recorded sources
- **matched passages** — the specific text in the submission that matched, highlighted in place
- **identified sources** — where each match came from, usually with a link or reference, and a side-by-side view of the submission against the source
- **filters and exclusions** — the reviewer's ability to recompute what counts: exclude quoted material, citations and bibliographies, small matches below a word threshold, or the submitter's own earlier drafts

### Repository

An optional but very common store of past submissions that future checks can match against. This is what makes "did two students copy from each other?" answerable. Its posture varies materially and is a policy-laden choice:

- a **shared, cross-institution** repository, where indexed work becomes comparable by other institutions
- an **institution-private** repository, visible only within the organization
- **no retention at all**, or indexing strictly by consent — a posture common where data-protection law (e.g., GDPR in Europe) shapes the product

### Roles and visibility

Who can see what is a structural concern, not an afterthought: students, instructors, and administrators have different report visibility; whether a student may see their own similarity report is a configurable policy in institutional deployments; investigation-oriented roles (where offered) see evidence-gathering views rather than teaching views.

### Concept vs implementation

The core model is conceptual; products implement each piece differently:

```text
Concept:            Submission
Implementations:    file upload in a web app, LMS assignment submission, API submission,
                    text pasted or scanned (OCR) input

Concept:            Source corpora
Implementations:    proprietary web archives, licensed publication databases,
                    shared cross-institution repositories, institution-private repositories,
                    reviewer-supplied comparison texts

Concept:            Similarity score
Implementations:    single overall percentage; percentage broken into match types
                    (identical / minor changes / paraphrased); per-source breakdown
```

## How It Works

### The main loop

```text
Work is submitted (upload, LMS assignment, or API)
→ the platform extracts the text
→ it searches and compares against the selected source corpora
→ matches are identified and insignificant ones cleaned out
→ a similarity report is generated:
   score + highlighted passages + source list
→ the reviewer opens the report, applies or adjusts filters
   (quotes, citations, small matches, prior drafts)
→ the reviewer interprets the remaining matches
→ the institution's integrity process takes over if needed
→ optionally, the submission is indexed into a repository
   so future submissions can be matched against it
```

Two properties of this loop matter more than any feature:

**The report is recomputable.** Filters and exclusions change what the score means. A quoted, properly cited passage still matches the original source — matching is textual, not moral — so reviewers routinely exclude quotations and bibliographies to see the score that reflects unattributed text. The same submission can legitimately show different scores under different filter settings.

**Repository timing interacts with fairness.** Whether a submission is indexed before or after the due date, and whether reports can be regenerated, determines whether late-submitting students are matched against earlier ones. Products expose this as explicit configuration (for example, generating all reports for an assignment only on the due date) precisely so that collusion checking treats every student the same way.

### The AI-writing layer

Modern products add a second analysis on the same submission: an estimate of how much of the text was likely generated by AI writing tools, usually shown as a percentage with the flagged passages located in the document. It rides the same loop — submission, analysis, report, human judgment — and carries the same caveat: it is an indicator to be interpreted, not a determination. It is typically licensed as an add-on or a higher product tier.

### The investigation loop

For suspected serious misconduct (for example, contract cheating — work commissioned from a third party), some products offer an evidence-gathering mode for integrity officers: comparing a suspect document against the student's own past work to profile writing style over time, inspecting document metadata, and assembling the findings into a report that supports — but does not replace — the institution's investigation.

### Capability tiers

**Defining core** — without these, it is not this Type:

- submission of written work as an analyzable record
- automated comparison against corpora of recorded text
- similarity report: score + matched passages + identified sources
- evidence for human judgment, never an automatic verdict

**Standard capabilities** — present in most mature products:

- exclusion filters (quotes, citations/bibliography, small matches, prior drafts)
- matched-source navigation with side-by-side passage views
- repository of past submissions with configurable sharing posture
- LMS integration, direct web upload, and API access
- downloadable / shareable reports
- role-based visibility (student / instructor / administrator)
- AI-writing detection as an add-on layer
- paraphrase and cross-language (translated-plagiarism) matching
- flags for text manipulation (hidden or substituted characters)
- student self-check mode before final submission

**Optional / variant** — depends on segment and product:

- authorship / contract-cheating investigation support
- source-code plagiarism detection
- grading and feedback tools bundled around the similarity report
- awareness and training programs bundled with the tool
- pre-publication originality checking for publishers and researchers

## Interfaces

### Submission surface

Where work enters. In institutional use this is usually the LMS assignment flow with the platform embedded, or an upload page in the platform's own web app. Typical information: submitter, assignment/course context, file or pasted text. Primary actions: submit, resubmit, view submission status.

### Similarity report viewer

The central working surface for reviewers. The document is shown with matched passages highlighted; a panel lists the matched sources with their percentages; clicking a source opens a side-by-side view of the submission against it. Primary actions: toggle filters and exclusions, drill into individual matches, exclude a source, download or share the report. In products with AI detection, an indicator and flagged passages appear alongside the similarity layer.

### Settings / configuration

Instructor- and administrator-level controls: which repositories to search, whether submissions are indexed and where, what is excluded by default, when reports are generated, and who may see reports. This surface is where institutional policy becomes system behavior.

### Student view

For submitters: their own submission, and — where policy allows — their own report, often with guidance on citation and paraphrasing. Self-check products are built entirely around this surface: a student uploads a draft, sees matches, and fixes attribution before official submission.

### Administration / investigation dashboard

Institution-level views: usage across courses, aggregated statistics, and — where offered — evidence-gathering workspaces for suspected cases (document sets, style comparison, assembled investigation reports).

## Important Rules / Behaviors

**Similarity is not plagiarism.** The score measures textual matching, not misconduct. Properly quoted and cited text still matches its source; a low score does not prove originality (paraphrased plagiarism may not match verbatim); a high score may be entirely legitimate (a literature review with heavy quotation). Vendors state this in their own guidance, and institutional policies are expected to define interpretation.

**Matching is textual, not semantic — unless the product says otherwise.** The baseline engine matches recorded text; paraphrase, translation, and meaning-level matching are progressively deeper capabilities that not all products or tiers include.

**Exclusions change the score, and that is by design.** The reviewer's filters (quotes, bibliography, small matches, prior drafts) exist because raw matching always over-reports. Two reviewers can produce different scores from the same submission legitimately.

**Repository participation is a policy decision.** Whether student work is retained and who may match against it in the future differs by product and configuration — shared global repositories, institution-private stores, or no retention. Data-protection regimes (notably GDPR in Europe) have made confidentiality-first postures a real market segment.

**Report generation timing is a fairness control.** Generating all reports for an assignment at the due date (rather than as each student submits) is the standard mechanism for making collusion checks even-handed.

**The platform never adjudicates.** Determinations, penalties, and records belong to the institution. Products that support investigations still frame their output as evidence for human judgment on the balance of probabilities.

**False positives are expected and managed, not eliminated.** Student names, assignment prompts, common phrases, template text, and the submitter's own earlier drafts all produce matches; exclusion filters and reviewer judgment are the built-in answers.

## Variants

- **Institutional higher-education deployment** — the center of the category: LMS-embedded checking of coursework, repositories, policy configuration, integrity-officer roles.
- **K-12 / school deployment** — lighter packaging, teacher-centric, often bundled with affordability and simplicity positioning.
- **Student self-check** — the student is the customer; drafts are checked before official submission; no institutional repository participation.
- **Research and publishing** — the same engine pointed at manuscripts before publication (journals, theses, editorial workflows); similarity evidence supports editorial decisions rather than course grading.
- **Enterprise / API-first** — originality checking embedded into other platforms (learning platforms, content systems) via API, with white-label report display.
- **Regional / regulatory variants** — European products emphasizing GDPR compliance, in-region hosting, and confidentiality-first repository postures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Online Proctoring Platform | adjacent (both sold as "academic integrity") | proctoring observes the live exam-taking process (identity, environment, behavior) in real time; this Type analyzes submitted written artifacts after the fact |
| Assessment Platform | adjacent | delivers and scores assessments; this Type evaluates originality of written work and produces no grade |
| Assignment Management (LMS) | upstream | collects and returns student work; the plagiarism platform plugs into that flow and returns integrity evidence, not submissions or grades |
| Peer Review Platform | adjacent | orchestrates reviewer assignment and critique for scholarly manuscripts; similarity checking is one input such systems may consume |
| AI Content Detector (standalone) | capability overlap | classifies AI-vs-human text without source comparison or a similarity report; here AI detection is a layer on the submission→report loop, not the whole product |
| Consumer plagiarism checker | gradient | same core loop, but no institutional roles, no student repository, no integrity-policy context |

The most important boundary is with **Online Proctoring**: the two are bought under the same "academic integrity" umbrella, but the structural test is clean — remove live session surveillance and this Type remains intact; remove artifact analysis and proctoring remains.

## Representative Products

- **Turnitin** (Feedback Studio / Similarity / Originality) — the dominant higher-education incumbent; similarity checking plus an extensive repository, with AI-writing detection and authorship investigation as add-ons
- **Copyleaks** — modern SaaS serving education and enterprise; strong API surface, shared and private repository options, paired AI-detection product line
- **Compilatio** — European (French) player with GDPR-first positioning; separate product lines for teachers, students, and writers/publishers
- **PlagiarismCheck.org** — lighter-tier platform for K-12, higher education, and individuals; LMS integrations, API, and an authorship-comparison feature

## Sources

Research date: **2026-09-06**

- Turnitin — Feedback Studio product page: https://www.turnitin.com/products/feedback-studio
- Turnitin Guides (help center) — Academic integrity tools: https://guides.turnitin.com/hc/en-us/categories/22037225052173-Academic-integrity-tools
- Turnitin Guides — Understanding the similarity score: https://guides.turnitin.com/hc/en-us/articles/23435833938701-Understanding-the-similarity-score
- Turnitin Guides — Getting Started with Authorship for Investigators: https://guides.turnitin.com/hc/en-us/articles/22040264085133-Getting-Started-with-Authorship-for-Investigators
- Copyleaks — Plagiarism Checker product page: https://copyleaks.com/plagiarism-detector
- Copyleaks API documentation — index and Data Hubs: https://docs.copyleaks.com/llms.txt , https://docs.copyleaks.com/concepts/features/data-hubs
- Compilatio — homepage and Similarities Detection: https://www.compilatio.net/en/ , https://www.compilatio.net/en/similarities-detection-info
- PlagiarismCheck.org — homepage: https://plagiarismcheck.org/

> Sourcing limitations: Copyleaks' end-user help center and Compilatio's support-knowledge-base articles were not reachable from the research environment on 2026-09-06. For those two products, end-user interface mechanics are asserted only at product-page level, and operational specifics (exact filter options, retention durations, visibility defaults) are intentionally not stated. No numeric limits, thresholds, or accuracy figures from vendor marketing are treated as operational facts in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
