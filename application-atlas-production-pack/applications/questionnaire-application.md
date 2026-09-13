# Questionnaire Application

## Overview

A **Questionnaire Application** is software for authoring a questionnaire — a structured instrument of questions with defined answer formats — administering it to a population of respondents, collecting their answers as responses, and compiling those answers into results. The questionnaire is the central object: everything in the product exists to design it, get it in front of the right people, retain what they answered, and turn the answers into readable, exportable results.

The defining loop is small:

```text
Authored questionnaire (questions × answer formats, ordered structure, logic)
└── administration to respondents (launch, distribution channels, open/close)
    └── response (one completion's answers, bound to the instrument, with metadata)
        └── compiled results (per-question aggregates + exportable dataset)
```

One naming fact should be stated plainly: this is the same application the market usually calls a **Survey Platform**. "Questionnaire" names the *instrument* — the structured set of questions — while "survey" names the *activity* of fielding it; the two words come from the research tradition the software digitizes. The market uses them interchangeably: products whose object is named "survey" describe its questions as questionnaire design, and products (and whole regional markets) led by the questionnaire word carry exactly the machinery of survey software. No separate product population answers to one label and not the other. Both directory entries describe one Type from two angles — this document from the instrument angle — and readers should treat the two as one application with two names.

Everything else commonly associated with these products — template libraries, question banks, AI drafting, quotas and panel purchasing, cross-tab dashboards, scoring, kiosk and offline modes — is standard or optional capability that mature products add, not what makes the product a questionnaire application. A printed instrument that is mailed out, filled in, returned, and tabulated by hand satisfies the same defining loop; the software industrializes it.

## Users & Context

Three distinct populations surround the instrument:

**The instrument author (the operator side)** — the person with a question to answer:

- researchers and students: scientific studies, theses, academic surveys — often with methodology requirements (randomization, scale instruments, statistical export)
- market and consumer researchers: product concepts, brand funnels, preference models
- HR and program owners: staff feedback, member or citizen consultation
- marketers and customer teams: satisfaction and feedback measurement

**Respondents** — the people who answer. They do not "work in" the product; they encounter a fill surface through a link, an invitation, an embed, or an interviewer's device. They need no account in the default case.

**Results consumers** — the author's stakeholders: thesis supervisors, research teams, management, clients. They read summaries, dashboards, and exports; some products let authors share results directly with them.

Typical context: the author works in the product across the whole life of a study or feedback exercise — design, pilot, fielding, monitoring, analysis — while respondents touch it once. The work is project-shaped: one instrument, one fielding effort, one results set, then the next instrument.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a questionnaire application:

- **The authored questionnaire** — a stored, named, re-editable instrument: a set of questions, each with a defined answer format, organized into an ordered structure (pages, sections, or question groups), carrying presentation settings and response-shaping logic. Without it, there is nothing to field and nothing to measure — the product would be a blank distribution channel.
- **Administration to respondents** — the instrument is put to a population: it is launched or published, distributed through channels (links, email or SMS invitations, embeds, panels, kiosks), and collection can open and close. Without it, the questionnaire is a design document with no one to answer it.
- **The response** — each person's completion is captured as a record of answers bound to the questions that were asked, with metadata such as time, completion state, and whatever identity posture applies. Without it, answers are ephemeral and nothing accumulates.
- **The compiled results** — responses are aggregated into per-question results and an exportable dataset. This is the deliverable the loop exists to produce: not the individual filings, but what the population's answers say. Without it, the product keeps records but never measures.

### The instrument in detail

The questionnaire's building blocks are stable across mature products:

- **Questions and answer formats** — closed choice (single or multiple), scales and ratings (agreement/Likert-style, star ratings, sliders), open text, and, commonly, matrix-style batteries that ask many items against one scale, ranking questions, date and numeric entry, and file upload. Research-grade products extend the palette toward methodology needs (paired-item scales, semantic-differential profiles, timed or latency-recording formats).
- **Structure** — pages or sections that order the instrument; introduction, instructions, closing text, and thank-you pages.
- **Logic** — skip and branching rules (what a respondent sees next depends on answers), mandatory and required-answer controls, answer validation, and — at the methodology pole — rotation and randomization of question or option order so that presentation order cannot bias results.
- **Presentation** — themes and branding, mobile-responsive fill, progress indication; some products favor one-question-per-page or conversational presentation.

### The respondent layer

Administration is built from a small set of concepts whose implementations vary:

```text
Concept:          reaching respondents
Implementations:  open link / QR, email and SMS invitations, website or app embed,
                  purchased or integrated respondent panels, kiosk or interviewer devices

Concept:          who may answer, and whether the answer is attributable
Implementations:  open anonymous collection ↔ tracked collection against a contact list,
                  invitation tokens, or an address book; one-response controls

Concept:          participation state
Implementations:  partial (save-and-resume) responses, completed responses,
                  closed/expired collection
```

The default posture in the market is open, accountless participation; attribution (knowing who answered, tracking non-responders, sending reminders) is a mode the author chooses — and one that shapes what respondents are told about anonymity.

### The results layer

Responses compile into the loop's output:

- per-question summaries — answer distributions, averages for scale questions, response counts
- the response table — every completion as a row bound to the instrument, filterable and inspectable down to individual responses
- export — spreadsheets universally; at the research-grade pole, statistical formats (SPSS/R-class) with coding documentation, so analysis can continue in dedicated statistics software
- at the commercial-research pole, aggregate analysis in-product: cross-tabs, dashboards, model-based reporting

The depth of in-product analysis varies enormously by product; the *existence* of compiled results does not.

## How It Works

### Author the instrument

```text
Create a new questionnaire
→ from scratch, from a template, by duplicating an existing one,
   by pasting drafted questions, or (in current products) by AI drafting
→ add questions, choose answer formats, set required/validation rules
→ organize pages or groups; set logic (skip, branching, rotation)
→ style and brand the fill experience
→ preview and test the respondent experience
```

### Field it

```text
Publish / launch the questionnaire
→ choose who may respond and whether answers are attributed or anonymous
→ distribute (link/QR, email/SMS invitations, embed, panel, kiosk)
→ open collection; monitor responses arriving
→ close collection (deadline, quota, or manual close)
```

### Compile the results

```text
Review per-question summaries as responses accumulate
→ inspect individual responses where needed
→ export the dataset (spreadsheet; statistical formats at the research grade)
→ share or report the results
```

The loop is deliberately asymmetric: one author, many respondents, one results set. The author's effort is front-loaded (instrument design), the respondents' effort is a single sitting, and the value is realized in the compiled results.

## Interfaces

The surfaces below are described conceptually; layouts and labels vary by product.

### Builder / editor

Where the instrument is composed. Typical information: the question list in order, per-question answer formats and settings, page/section organization, logic rules, theme. Primary actions: add/edit/reorder questions, set required and validation rules, define skip logic, preview.

### Distribution / launch surface

Where fielding is arranged. Typical information: collection status (open/closed), response window, channels in use, respondent list where tracking is enabled. Primary actions: generate link or QR, configure email invitations and reminders, open/close collection, set quotas where supported.

### Respondent fill surface

What respondents see. Typical information: questions in the configured order, answer controls, progress indication, closing message. Primary actions: answer, navigate, submit (and resume, where partial saves are supported). No account in the default case.

### Results surface

Where the loop pays off. Typical information: response count and completion state, per-question summary tables and charts, individual response views, filter controls. Primary actions: browse, filter, export, share or report.

### Project list

The author's home: questionnaires as named project cards with status (draft, collecting, closed) and headline response counts. Primary actions: create, duplicate, open, archive.

## Important Rules / Behaviors

### The instrument and its data are coupled

A questionnaire is not a free-form document: questions, their order, and their answer formats define the shape of every response collected against them. Products therefore treat structural changes to a live instrument with care — some lock the structure when collection starts and require a formal step to change it, some warn or restrict edits that would orphan collected answers, and research-grade products document guarded procedures for correcting completed responses. The shared rule beneath the varying strictness: collected responses are only as consistent as the instrument that asked them.

### Attribution is a design decision with consequences

The author chooses between open anonymous collection and tracked collection against known respondents. The choice trades reach (anonymity encourages candor) against follow-up (tracking enables reminders, non-response chasing, and segmented results). Mature products make the choice per instrument, not per account, and research products add consent framing — the instrument can carry an information and consent page as part of ethical fielding.

### The default is accountless participation

Respondents normally answer through the provisioned fill surface without registering. Identity, where needed, enters through invitation tokens, contact lists, or response-attribute settings rather than respondent accounts.

### A fielded instrument can be closed but rarely un-asked

Collection can be stopped (deadline, quota, manual close), and products commonly prevent further responses with a configurable closed message. But responses already collected belong to the instrument's record; the normal way to run an altered instrument is to duplicate and re-field, not to mutate the live one.

### Results aggregate by question, not by submission

The results layer's center of gravity is per-question compilation — what the population answered — with individual responses available for inspection or follow-up. Products differ in how much aggregate analysis happens in-product versus in exported statistical software, but per-question results are the constant deliverable.

## Variants

The questionnaire core is realized across a wide market:

- **Mass-market general-purpose platforms** — self-serve authoring, large template libraries, open-link collection, simple in-product summaries; priced for individuals and teams.
- **Research-grade / academic methodology products** — instrument design to research standards (scales, rotation, randomization, pilot testing), data exit to dedicated statistics software, printable instrument documentation; often self-hostable.
- **Commercial research suites** — the instrument core plus research models (satisfaction frameworks, MaxDiff, conjoint), purchased respondent panels, and consulting-grade packaging.
- **Enterprise experience suites** — the instrument core embedded in program machinery (customer or employee experience management) — at which point the program frame, not the instrument, is the product's center.
- **Regional questionnaire platforms** — in some markets the questionnaire product is the everyday data-collection instrument and extends sideways into sibling modes (online exams, voting, registration forms, assessments) on one platform.
- **Field/offline variants** — kiosk and offline administration for venues or interviewer-led collection, syncing when connected.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Survey Platform | The same application under the market's other name — "survey" names the activity, "questionnaire" names the instrument. Every researched product answers to both vocabularies; one Type, two directory entries; consolidation recommended. |
| Online Form Builder | Shared fill-and-collect machinery, different center: the form builder's defining output is the persisted per-submission record worked individually (viewed, exported, routed); the questionnaire's defining output is the compiled per-question results of fielding a question instrument. |
| Polling Application | A poll is a small instrument — one question, at most a few — with an immediate, consulted aggregate; a questionnaire is an instrument battery whose measurement is compiled after fielding. |
| Employee Survey Platform | The same instrument core bound to the workforce population and employment lifecycle (rosters, engineered anonymity, lifecycle cadence). Remove the workforce orientation and the generic questionnaire remains. |
| Audience Response System | A facilitator-run live session whose responses are collected and displayed back to the same co-present room; a questionnaire is fielded for participants to answer in their own time. |
| Psychometric / Candidate Assessment Platforms | Instruments validated and scored to evaluate a person for an evaluation decision (hiring, measurement of the individual); a questionnaire application centers fielding and results for the author's question, with scoring an optional feature. |
| ePRO / eCOA Platform | Regulated, protocol-scheduled administration of validated clinical instruments inside a study, with auditable records feeding a clinical dataset; no study, schedule, or clinical-record structure here. |
| Examination Platform | Grading-centered instruments for instruction and certification, with scoring and pass/fail semantics as the point; likely seam, to be confirmed by that entry. |

The closest seam inside its own family is the Online Form Builder, because both author a fillable instrument and collect completions. The discriminator is the output: per-submission records processed one by one versus a question instrument whose fielded responses compile into measurement. The next closest is the poll, which is the questionnaire's single-question, instant-aggregate cousin.

## Representative Products

- **SurveyMonkey** — mass-market/enterprise general-purpose pole; help taxonomy organized as create → send → analyze; template library and respondent panel.
- **QuestionPro** — commercial SaaS pole with research-suite packaging (research models, NPS/Likert machinery, kiosk/offline) beside CX/EX product lines.
- **SoSci Survey** — academic/research-methodology pole; manual vocabulary itself splits "questionnaire" (instrument) from "survey" (project); methodology-grade question types, randomization, multi-wave support, statistical export.
- **LimeSurvey** — open-source self-hosted (and cloud) pole; full survey → question group → question object model, activation lifecycle, statistics, and paper-questionnaire PDF export.
- **问卷星 WJX** — regional Chinese pole where the questionnaire is the product noun; edit → send → report loop; questionnaire core extended into exam/vote/form/assessment modes; sample services.

These five span consumer/mass-market, enterprise/commercial-research, academic-methodology, open-source self-hosted, and regional-market poles. The definition was checked against the paper questionnaire practice the software digitizes (printed instrument, postal or field administration, returned sheets, per-question tabulation), so the core does not depend on any era, region, or delivery channel.

## Sources

Research date: **2026-09-08**

- SurveyMonkey Help Center — https://help.surveymonkey.com/en/ ; Creating Surveys: https://help.surveymonkey.com/en/create/ ; Creating Great Surveys: https://help.surveymonkey.com/en/surveymonkey/create/creating-a-survey/
- SoSci Survey user manual — https://www.soscisurvey.de/help/doku.php/en:start ; Part 1 Creating and Designing the Questionnaire: https://www.soscisurvey.de/help/doku.php/en:create:start ; Part 3 Data Retrieval and Questionnaire Documentation: https://www.soscisurvey.de/help/doku.php/en:results:start
- LimeSurvey Manual — https://manual.limesurvey.org/LimeSurvey_Manual
- QuestionPro — https://www.questionpro.com/ (positioning and feature surfaces)
- 问卷星 WJX — https://www.wjx.cn/ (product site)

> Sourcing limitations: QuestionPro's help-center articles and WJX's help center were not fetched this pass, so both products' evidence is held at positioning/feature-title strength; no operational details are asserted from them alone. Google's free forms product was unreachable across research passes and is used only as market context. Precise numbers (question-type counts, template counts, usage volumes, plan limits) are vendor claims recorded in the paired Research Notes and are deliberately not stated as Type facts.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against the neighboring Application Types are recorded in the paired Research Notes.
