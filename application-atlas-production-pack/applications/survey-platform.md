# Survey Platform

## Overview

A **Survey Platform** is software for authoring a survey — a structured instrument of questions with defined answer formats — fielding it to a population of respondents, collecting their answers as responses, and compiling those answers into per-question results: the measurement the survey exists to produce.

The defining loop is small:

```text
Authored survey (questions × answer formats, ordered structure, logic)
└── fielding to respondents (launch, distribution channels, open/close)
    └── response (one completion's answers, bound to the instrument, with metadata)
        └── compiled results (per-question aggregates + exportable dataset)
```

One naming fact should be stated plainly: this is the same application the market often calls a **Questionnaire Application**. "Survey" names the *activity* of fielding an instrument; "questionnaire" names the *instrument* itself. The market uses the words interchangeably — products whose object is named "survey" describe questionnaire design, products led by the questionnaire word carry exactly the machinery of survey software, and some vendors carry both nouns in a single product title. The directory documents this one Type from two angles — this document from the activity and measurement angle, the Questionnaire Application document from the instrument angle — and readers should treat the two as one application with two names.

Everything else commonly associated with these products — template libraries, question banks, AI drafting, quotas, panel purchasing, dashboards, paper scanning, offline apps — is standard or optional capability that mature products add, not what makes the product a survey platform. A printed questionnaire that is mailed out, filled in, returned, and tabulated by hand satisfies the same defining loop; the software industrializes it.

## Users & Context

Three distinct populations surround the survey:

**The survey author (the operator side)** — the person or team with a question to answer:

- researchers and students: studies, theses, academic surveys — often with methodology requirements (scales, randomization, statistical export)
- market and consumer researchers: concept tests, brand and preference measurement
- HR and program owners: staff feedback, member or citizen consultation
- marketers and customer teams: satisfaction and experience measurement
- field teams and enumerators: structured data collection in the field, sometimes offline

**Respondents** — the people who answer. They do not work in the product; they encounter a fill surface through a link, an invitation, an embed, a kiosk, or an interviewer's device. They need no account in the default case.

**Results consumers** — the author's stakeholders: supervisors, research teams, management, clients. They read summaries, dashboards, and reports; mature products let authors share results directly with them.

Typical context: the author works in the product across the whole life of a survey — design, test, fielding, monitoring, analysis — while respondents touch it once. The work is project-shaped: one instrument, one fielding effort, one results set, then the next survey.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a survey platform:

- **The authored survey** — a stored, named, re-editable instrument: a set of questions, each with a defined answer format, organized into an ordered structure (pages, sections, blocks, or question groups), carrying presentation settings and response-shaping logic. Without it, there is nothing to field and nothing to measure.
- **Fielding to respondents** — the survey is put to a population: it is launched or published, distributed through channels (links, email or SMS invitations, embeds, panels, kiosks, enumerator devices), and collection can open and close. Without it, the survey is a design document with no one to answer it.
- **The response** — each person's completion is captured as a record of answers bound to the questions that were asked, with metadata such as time, completion state, and whatever identity posture applies. Without it, answers are ephemeral and nothing accumulates.
- **The compiled results** — responses are aggregated into per-question results and an exportable dataset. This is the deliverable the loop exists to produce: not the individual filings, but what the population's answers say. Without it, the product keeps records but never measures.

### The instrument in detail

The survey's building blocks are stable across mature products:

- **Questions and answer formats** — closed choice (single or multiple), scales and ratings (agreement/Likert-style, star ratings, sliders, NPS-style), open text, and, commonly, matrix-style batteries that ask many items against one scale, ranking questions, date and numeric entry, and file or media upload. Research-grade products extend the palette toward methodology needs (paired-item scales, semantic-differential formats, latency-recording items).
- **Structure** — pages, sections, or blocks that order the instrument; introductions, instructions, and closing or thank-you screens. Research products group questions for flow control and repeat groups for enumerated entries.
- **Logic** — skip and branching rules (what a respondent sees next depends on answers), display logic, required-answer controls, answer validation, piping (one answer's text carried into a later question), and — at the methodology pole — rotation and randomization of question or option order so presentation order cannot bias results.
- **Presentation** — themes and branding, progress indication, mobile-responsive fill; some products favor one-question-per-page or conversational presentation.

### The respondent layer

Fielding is built from a small set of concepts whose implementations vary:

```text
Concept:          reaching respondents
Implementations:  open link / QR, email and SMS invitations, website or app embeds,
                  purchased or integrated respondent panels, kiosks,
                  offline apps and interviewer devices for field collection

Concept:          who may answer, and whether the answer is attributable
Implementations:  open anonymous collection ↔ tracked collection against a contact list,
                  invitation tokens, or a participant database; identity verification
                  before entry at the enterprise pole; one-response controls

Concept:          participation state
Implementations:  partial (save-and-resume) responses, completed responses,
                  closed/expired collection, quotas that stop collection when cells fill
```

The default posture in the market is open, accountless participation; attribution (knowing who answered, tracking non-responders, sending reminders) is a mode the author chooses — and one that shapes what respondents are told about anonymity.

### The results layer

Responses compile into the loop's output:

- per-question summaries — answer distributions, averages for scale questions, response counts
- the response table — every completion as a row bound to the instrument, filterable and inspectable down to individual responses
- export — spreadsheets universally; at the research-grade pole, statistical formats (SPSS/R/Stata-class) with coding documentation, so analysis can continue in dedicated statistics software
- at the commercial and research-grade poles, aggregate analysis in-product: cross-tabs, dashboards, weighting, and bulk or segmented report generation

The depth of in-product analysis varies enormously by product; the *existence* of compiled results does not.

## How It Works

### Author the instrument

```text
Create a new survey
→ from scratch, from a template, by duplicating an existing one,
   by importing a drafted document, or (in current products) by AI drafting
→ add questions, choose answer formats, set required/validation rules
→ organize pages, blocks, or groups; set logic (skip, branch, rotate)
→ style and brand the fill experience
→ preview and test the respondent experience
→ publish the changes live
```

### Field it

```text
Launch the survey
→ choose who may respond and whether answers are attributed or anonymous
→ distribute (link/QR, email/SMS invitations, embed, panel, kiosk, offline device)
→ open collection; monitor responses arriving
→ close collection (deadline, quota, or manual close)
```

### Compile the results

```text
Review per-question summaries as responses accumulate
→ inspect individual responses where needed
→ export the dataset (spreadsheet; statistical formats at the research grade)
→ share, report, or present the results
```

The loop is deliberately asymmetric: one author, many respondents, one results set. The author's effort is front-loaded (instrument design), the respondents' effort is a single sitting, and the value is realized in the compiled results. Around this loop, mature products add automation — follow-up surveys triggered by completion, alerts or tickets raised by particular answers, integrations that carry responses into other systems — and enterprise suites extend the loop into standing measurement programs (see Variants).

## Interfaces

The surfaces below are described conceptually; layouts and labels vary by product.

### Builder / editor

Where the instrument is composed. Typical information: the question list in order, per-question answer formats and settings, page/block/group organization, logic rules, theme. Primary actions: add/edit/reorder questions, set required and validation rules, define skip and display logic, preview, publish.

### Flow / configuration surface

Where the instrument's behavior is arranged (separate from question content in mature products). Typical information: block or section order, branch conditions, embedded data variables, quotas, availability window, language versions. Primary actions: reorder, branch, set quotas, translate, configure access and expiration.

### Distribution / launch surface

Where fielding is arranged. Typical information: collection status (open/closed), response window, channels in use, respondent list where tracking is enabled. Primary actions: generate link or QR, configure email/SMS invitations and reminders, open/close collection, monitor response counts.

### Respondent fill surface

What respondents see. Typical information: questions in the configured order, answer controls, progress indication, closing message. Primary actions: answer, navigate, submit (and resume, where partial saves are supported). No account in the default case.

### Results / analysis surface

Where the loop pays off. Typical information: response count and completion state, per-question summary tables and charts, individual response views, filter controls. Primary actions: browse, filter, cross-tab where supported, export, share or report. At the research-grade pole this surface extends to weighting and statistical analysis; at the enterprise pole it extends to configurable dashboards.

### Project list

The author's home: surveys as named project cards with status (draft, collecting, closed) and headline response counts. Primary actions: create, duplicate, open, archive, share with collaborators.

## Important Rules / Behaviors

### The instrument and its data are coupled

A survey is not a free-form document: questions, their order, and their answer formats define the shape of every response collected against them. Products therefore treat structural changes to a live survey with care — some require an explicit publish step that controls when edits go live, some restrict changes while collection is running, and products generally warn against deleting questions or answer options that already hold collected data (hiding them is the safe alternative). The shared rule beneath the varying strictness: collected responses are only as consistent as the instrument that asked them.

### Attribution is a design decision with consequences

The author chooses between open anonymous collection and tracked collection against known respondents. The choice trades reach (anonymity encourages candor) against follow-up (tracking enables reminders, non-response chasing, and segmented results). Mature products make the choice per survey, not per account, and research products add consent framing — the instrument can carry an information and consent page as part of ethical fielding.

### The default is accountless participation

Respondents normally answer through the provisioned fill surface without registering. Identity, where needed, enters through invitation tokens, contact lists, embedded URL parameters, or verification steps rather than respondent accounts.

### A fielded survey can be closed but rarely un-asked

Collection can be stopped (deadline, quota, manual close), and products commonly prevent further responses with a configurable closed message. But responses already collected belong to the survey's record; the normal way to run an altered instrument is to duplicate and re-field, not to mutate the live one.

### Results aggregate by question, not by submission

The results layer's center of gravity is per-question compilation — what the population answered — with individual responses available for inspection or follow-up. Products differ in how much aggregate analysis happens in-product versus in exported statistical software, but per-question results are the constant deliverable.

## Variants

The survey core is realized across a wide market:

- **Mass-market general-purpose platforms** — self-serve authoring, large template libraries, open-link collection, simple in-product summaries; priced for individuals and teams.
- **Research-grade / academic methodology products** — instrument design to research standards (scales, rotation, randomization, weighting, statistical analysis), data exit to dedicated statistics software, printable instrument documentation; often self-hostable.
- **Commercial research suites** — the instrument core plus research models (satisfaction frameworks, conjoint, MaxDiff), purchased respondent panels, and consulting-grade packaging.
- **Enterprise experience suites** — the survey core embedded in program machinery (customer or employee experience management: standing programs, experience metrics, follow-up routing). When the program, not the instrument, becomes the product's center, it crosses into the Voice of Customer / experience-management territory described in Related Application Types.
- **Multi-mode and field variants** — paper questionnaires scanned back into the same dataset, offline interviewer apps for connectivity-poor fieldwork, kiosk collection, enumerator-led deployment (common in development and humanitarian research).
- **Regional questionnaire platforms** — in some markets the questionnaire product is the everyday data-collection instrument and extends sideways into sibling modes (online exams, voting, registration forms, assessments) on one platform.
- **Design-led conversational products** — presentation-first philosophy (one question at a time, high-finish fill experience); the same core with the fill experience as the differentiator.
- **Deployment variants** — SaaS-only, self-hosted open source, and licensed on-premises editions for organizations that must hold their own data.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Questionnaire Application | The same application under the market's other name — "survey" names the activity, "questionnaire" names the instrument. Every researched product answers to both vocabularies; one Type, two directory entries, documents cross-referenced. |
| Online Form Builder | Shared fill-and-collect machinery, different center: the form builder's defining output is the persisted per-submission record worked individually (viewed, exported, routed, integrated); the survey's defining output is the compiled per-question measurement of fielding a question instrument. Products straddle widely (several sell form and survey creation side by side), but the output object decides. |
| Polling Application | A poll is a small instrument — one question, at most a few — with an immediate, consulted aggregate; a survey is an instrument battery whose measurement is compiled after fielding. |
| Employee Survey Platform | The same instrument core bound to the workforce population and employment lifecycle (rosters synced from HR systems, engineered anonymity, lifecycle cadence, manager-scoped results). Remove the workforce orientation and the generic survey remains. |
| Voice of Customer Platform | A standing experience program built on this machinery: instruments fielded to the organization's own customers at defined touchpoints, responses scored into tracked experience metrics, adverse responses routed for follow-up. The survey core is shared; the program frame, metric layer, and follow-up loop are the additions. |
| Consumer Research / Research Panel Platforms | Those Types center platform-supplied access to consumer audiences (owned panels, panel networks, syndicated datasets) — reach is part of the product. Survey platforms treat respondent supply as an optional commercial add-on. |
| ePRO / eCOA Platform | Regulated, protocol-scheduled administration of validated clinical instruments inside a study, with auditable records feeding a clinical dataset; no study, schedule, or clinical-record structure here. |
| Examination Platform | Grading-centered instruments for instruction and certification, with scoring and pass/fail semantics as the point; probable seam, to be confirmed by that entry. Quiz and exam modes inside survey products are the observed straddle. |
| Audience Response System | A facilitator-run live session whose responses are collected and displayed back to the same co-present room; a survey is fielded for respondents to answer in their own time. |
| A/B Testing Platform | Different evidence source: surveys collect stated preference (what people say when asked); A/B testing measures revealed preference (what users do) under controlled comparison. |
| Psychometric / Candidate Assessment Platforms | Instruments validated and scored to evaluate a person for an evaluation decision (hiring, clinical measurement); a survey platform centers fielding and results for the author's question, with scoring an optional feature. |

The closest seam inside its own family is the Online Form Builder, because both author a fillable instrument and collect completions; the discriminator is the output — per-submission records processed one by one versus a question instrument whose fielded responses compile into measurement. The next closest is the poll, the survey's single-question, instant-aggregate cousin.

## Representative Products

- **Qualtrics** — enterprise experience/research suite pole; the survey project with build → distribute → analyze tabs plus workflow automation and reporting; the pole where survey machinery is packaged inside program machinery.
- **Alchemer** — independent mid-market/enterprise DIY survey pure-play; survey creation with logic, piping, and templates; ships form, poll, and quiz creation beside surveys — the straddle made explicit.
- **Snap Surveys** — research-grade multi-mode pole (UK, founded 1981); online, paper-scanned, offline-interviewed, and kiosk collection in one dataset; weighting and statistical analysis in-product.
- **Typeform** — design-led conversational pole; self-describes as a form builder yet is market-classed among survey tools — the lexical straddle made explicit.
- **KoboToolbox** — field/humanitarian data-collection pole; XLSForm-defined instruments deployed to web forms and an offline Android collection app for enumerator-led fieldwork; exports to statistical software.

The definition was additionally checked against the samples documented in the cross-referenced Questionnaire Application entry (a mass-market leader, an academic methodology product, an open-source self-hosted product, a commercial research suite, and a regional questionnaire-noun platform), and against the practice the software digitizes — the printed questionnaire mailed, fielded, returned, and tabulated by hand — so the core does not depend on any era, region, or delivery channel.

## Sources

Research date: **2026-09-09**

- Qualtrics Support — Getting Started with Surveys: https://www.qualtrics.com/support/survey-platform/getting-started/survey-platform-overview/ ; Survey Tab Basic Overview: https://www.qualtrics.com/support/survey-platform/survey-module/survey-module-overview/
- Alchemer Help — https://help.alchemer.com/help/ ; Create a Survey: https://help.alchemer.com/help/create-a-survey
- Typeform Help Center — https://help.typeform.com/hc/en-us ; What is Typeform?: https://help.typeform.com/hc/en-us/articles/360038717092-What-is-Typeform ; Getting started category: https://help.typeform.com/hc/en-us/categories/360001979032
- Snap Surveys — Snap XMP Survey Software: https://www.snapsurveys.com/survey-software/ (product and FAQ pages)
- KoboToolbox documentation — https://support.kobotoolbox.org/ (topics and glossary)
- Cross-referenced sources (fetched 2026-09-08 for the same Type under its instrument-first name, recorded in the Questionnaire Application document): SurveyMonkey Help Center, SoSci Survey manual, LimeSurvey Manual, QuestionPro, 问卷星 WJX

> Sourcing limitations: Google Forms and Microsoft Forms (the free platform-native tier) were unreachable from the research environment (repeated timeouts), so that tier is characterized only through a vendor's own comparison and no operational claims are made about it. Typeform and Snap Surveys evidence is held at help-structure / product-site level (deep help articles not fetched), and KoboToolbox evidence at documentation-structure level; no precise limits, defaults, or click-path details are asserted from those products alone. Precise numbers that appear in vendor materials (question-type counts, template counts, customer counts) are recorded as vendor claims in the paired Research Notes and are deliberately not stated as Type facts.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against neighboring Application Types are recorded in the paired Research Notes.
