# Interview Management Platform

## Overview

An **Interview Management Platform** is the hiring team's system for managing the interview stage of recruiting as a designed, evaluated program: it holds each role's structured interview plan, turns every individual interview into a managed record with its own guide and scorecard, and converts interviewer feedback into decision-ready evidence for the hiring decision.

The problem it solves is that interviews are usually the highest-signal, least-managed part of hiring. Questions are improvised, notes are rough, feedback arrives late or never, decisions rest on fuzzy recollection, and no one can see whether interviewers evaluate candidates consistently. Interview management software gives that stage the same discipline other business functions get from their systems of record.

Its boundary: it manages the *substance* of interviews — what is asked, what is observed, how it is rated, how the evidence reaches a decision. It does not normally own the recruiting pipeline (the applicant tracking system does) and it does not normally book the interviews (interview scheduling software does). In practice it integrates with both, and those integrations are how a typical deployment works.

## Users & Context

The platform sits in the middle of a hiring team, and its users mirror the interview's own roles:

- **Interviewers** (engineers, managers, ICs drafted into interviewing) are the largest user group. They receive their assigned questions and evaluation criteria, run the interview, and record their assessment. The platform's promise to them is focus: guidance during the conversation and help with the write-up afterward.
- **Recruiters and recruiting coordinators** own the process. They design or assemble interview plans, monitor which feedback is missing, chase or automate its collection, and shepherd candidates toward the decision stage.
- **Hiring managers** consume the outputs: structured notes, summaries, scorecards, and side-by-side candidate comparisons, culminating in the hire/no-hire decision.
- **Talent-operations and talent-acquisition leaders** run the program level: interview quality measurement, interviewer training and coaching, consistency and fairness monitoring, and process analytics across many roles.

The work context is almost always an organization hiring repeatedly, where interviews are conducted by many employees and volume makes ad-hoc practice unsustainable. Deployment is as a layer alongside the existing stack: candidate and interview data flow in from the ATS, calendar and video-conferencing connections let the platform observe or capture the live interview, and evaluation results flow back out to the ATS where the hiring decision is recorded.

## Core Model

Three structures together make the Type what it is. Each one alone would be something else — remove any one and the product stops being an interview management platform.

### 1. The structured evaluation design of record

For each role, the organization defines what the interview process will evaluate and how: the competencies or criteria that matter, the questions to ask, and which interview stage or interviewer covers which part. This design is held in the system as a manageable artifact per role — created by the team, generated from the job description, or assembled from question libraries, depending on the product — and it is the reference against which interviews are conducted and rated. Without this layer there is no managed program, only conversations.

### 2. The interview record with its evaluation instrument

Each individual interview is a persistent record bound to a candidate, a hiring context (the role or application), and one or more interviewers. The record carries the slice of the role's plan assigned to that interview — its guide — and the scorecard criteria its interviewer will rate. It also accumulates what happened: at minimum the completed evaluation, and in current products typically structured notes, a summary, and a transcript or recording of the conversation. This record is what distinguishes the Type from a generic meeting-notes tool: the conversation is captured against hiring semantics — this candidate, this role, these rubric fields — not as free-floating meeting content.

### 3. The feedback-to-decision loop

Interviewer evaluations are captured and then aggregated into a form the hiring team can decide on: a per-candidate synthesis of who said what, comparison across candidates, visible agreement and disagreement between interviewers, and coverage showing what was tested and what nobody asked about. The loop terminates in the hiring decision — recorded in the platform or, more commonly, in the connected ATS that the evidence was pushed into. Without this loop the product is a form or a notes archive.

### How the structures connect

```text
Role
 └── Interview plan (competencies · questions · stage/interviewer assignments)
      └── Interview record (candidate × role × interviewer × time)
           ├── its guide (questions for this conversation)
           ├── its scorecard (criteria to rate)
           └── captured outcome (evaluation · notes · summary · transcript)
                └── aggregated → candidate comparison · debrief
                     └── hiring decision (in-product or pushed to the ATS)
```

### Standard capabilities layered on the core

Mature products commonly add, and the market expects:

- **AI-generated interview notes** — structured summaries organized by the organization's own competencies rather than raw transcripts, produced automatically from the recorded conversation.
- **Scorecard drafting into the ATS** — the platform pre-fills the scorecard fields in the applicant tracking system from the captured conversation; the interviewer reviews, adjusts, and submits.
- **Live in-interview guidance** — the interviewer's questions and prompts surfaced during the call, often as a companion panel inside the video-conferencing tool.
- **Debrief and comparison surfaces** — evidence matrices, interview highlights and clips, side-by-side candidate views.
- **Interviewer coaching and training** — review of interviewer technique against a framework, coachable feedback after interviews, training paths and reference libraries.
- **Program analytics** — interview quality, question coverage, feedback completion, consistency and fairness patterns across roles and interviewers.
- **Consent and privacy machinery** — candidate notification and opt-out for recording, role-based access to interview content, retention and redaction controls.
- **Integration spine** — deep ATS integration (hiring context in, evaluation results out), plus calendar and video-conferencing connections for capture, is standard across the product class.

## How It Works

The characteristic lifecycle runs once per role and then per interview:

**Design the role's interviews.** Before candidates reach the interview stage, the team establishes the plan: competencies, question sets, and who covers what. Many products accelerate this by generating a draft plan from the job description, which the team then edits and approves.

**Connect the surrounding systems.** The platform links to the ATS (candidate and role data flow in; scorecards flow back), to calendars and video-conferencing (so it knows when interviews happen and can join or capture them), and optionally to the scheduling tool that books them.

**Prepare and run the interview.** The assigned interviewer opens the interview's guide — often pre-briefed with what previous interviews already covered — and conducts the conversation with the platform assisting: questions at hand, and in recording-enabled products, capture running under whatever consent the process requires.

**Capture and draft the evaluation.** After the interview, the platform produces structured notes and a summary organized by the plan's competencies, and drafts the scorecard — commonly pre-mapped to the ATS's own scorecard fields. The interviewer reviews, adjusts, and submits. This is the step the products most want to compress: feedback that once arrived late and thin arrives fast and evidence-backed.

**Decide.** The hiring team reviews the aggregated evidence for the candidate — what each round tested, where interviewers agree or diverge, highlights from the conversation — compares candidates side by side, and records the decision.

**Improve the program.** Across many interviews, the platform surfaces patterns: which questions discriminate, which interviewers need coaching, where the process is inconsistent. Coaching feedback and training content close the loop back into the next round of interviews.

## Interfaces

- **Interview plan builder** — the role-level design surface. Typical content: competencies, question lists, stage and interviewer assignments. Primary actions: create or generate a plan, assign questions to stages, reuse across roles.
- **Interview record / conversation page** — the per-interview home. Typical content: candidate, role, interviewers, the guide, the notes, the transcript or recording, and the scorecard status. Primary actions: open the guide, review or edit notes, complete and submit the scorecard, share the conversation.
- **Live interview companion** — an in-call surface (browser panel, native video-conference integration, or a joining assistant). Primary actions: follow the question guide, capture highlights, in some products see real-time prompts about coverage.
- **Scorecard / feedback surface** — where the interviewer records ratings and comments against the plan's criteria. In mature deployments this is frequently experienced *inside the ATS*, with the platform pre-drafting the content the interviewer confirms.
- **Candidate comparison / debrief view** — the decision surface. Typical content: per-candidate synthesis, interviewer-by-interviewer ratings, agreement and coverage indicators, highlights. Primary actions: compare candidates, run the debrief, advance or reject.
- **Insights and program dashboard** — the operations surface. Typical content: interview volume and quality, feedback completion, coverage and fairness patterns, interviewer performance. Primary actions: drill into teams or interviewers, assign training, tune plans.
- **Admin / compliance settings** — consent notification and opt-out configuration, access permissions, retention policies.

## Important Rules / Behaviors

- **The plan governs the interview.** The evaluation is structured by the role's plan and its criteria — the platform's own descriptions of the category draw exactly this contrast with generic note-takers, which capture transcripts without connection to any rubric.
- **Judgment stays with people.** The center of gravity of this product class is support for human interviewers' judgment; some products explicitly disclaim making hiring recommendations at all. Where AI-produced scores exist, they are a contested edge of the market rather than its defining behavior.
- **Recording requires consent.** Where interviews are recorded or transcribed, notifying participants and honoring opt-outs is a first-class part of the workflow, not a setting buried in admin. Access to interview content is restricted by role, and retention/redaction controls apply to what is sensitive candidate data.
- **The ATS remains the pipeline of record.** The platform pushes structured feedback into ATS scorecard fields and reads hiring context from it; the requisition, the application, and usually the final decision record live in the ATS. This division of records is what makes the integration spine load-bearing.
- **Feedback completeness is actively managed.** Chasing interviewer feedback is a named problem the products automate — reminders, pre-drafted scorecards, one-click submission — because the decision loop stalls without it.

## Variants

- **Interview intelligence** — recording-centered products that emphasize the captured conversation as data: searchable evidence, highlights, quality measurement, coaching. The category's most visible philosophy.
- **Live interview companion** — guidance-first products that ride along inside the interview itself: real-time question guides, in-call assistance, immediate feedback collection.
- **AI-notetaker-first** — products that began as interview-specific note capture and structure, integrating deeply with ATS scorecards; several have since expanded toward fuller recruiting workflows.
- **Structured-hiring modules inside ATSs** — the same machinery (interview plans, kits, scorecards) shipped as capabilities of the applicant tracking system rather than a separate product; a packaging variant that coexists with the standalone class.
- **AI-interviewer-adjacent platforms** — screening products where an AI conducts interviews, which have absorbed structured-interview tooling (guides, scorecards, comparison) for the human-conducted stages around them.
- **Scheduling-suite extensions** — interview scheduling platforms adding interviewer training and basic interview analytics, which covers the program layer but not the evaluation core.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Interview Scheduling Platform | owns the *booking* of the interview — availability, confirmations, reschedules; this Type owns the interview's *evaluation substance*. The two meet at integrations, and suite vendors bundle both; scheduling vendors also use "interview management" language for coordination, which is a naming overlap, not a Type overlap |
| Applicant Tracking System / Recruiting Management Platform | owns the requisition, pipeline stages, and application record; interview plans and scorecards exist there as embedded capabilities, while this Type centers and deepens the interview evaluation program on top of the ATS's data |
| Candidate Assessment Platform | administers standardized assessments produced by the vendor with standardized scoring; here the organization's own interviewers conduct the evaluation and record human judgment against the organization's own criteria |
| Psychometric Assessment Platform | measurement instruments with norm-anchored interpretation; interview management records judgment, it does not score psychometrics |
| Meeting Notes Application | captures conversations generically; interview management binds capture to hiring semantics — candidate, role, rubric fields, consent regime |
| Conversation Intelligence Platform (sales) | the same recording-and-analysis machinery pointed at sales calls and sales methodology rather than hiring interviews |
| Customer / Employee Survey Platform | collects form responses without the interview record or the design-governance-decision program around hiring |

## Representative Products

- BrightHire — interview intelligence platform (planning, AI notes, insights, coaching)
- Metaview — AI interview notes origin, now an agentic recruiting platform
- Employ AI Interview Companion (formerly Pillar) — live interview companion embedded with ATSs
- Hirevue — AI interviewing and assessment platform carrying structured-interview tooling (includes acquired HireGuide technology)

GoodTime (interview scheduling, with interviewer training and analytics extensions) was examined to establish the boundary with Interview Scheduling Platform.

## Sources

Research date: **2026-09-10**

- BrightHire — homepage, "What is Interview Intelligence?", "AI Interview Notes" product page: https://brighthire.com/
- Metaview — homepage and help-center documentation index (notes, capture, templates, participants, scorecard autofill extensions, AI skills): https://metaview.app/ , https://support.metaview.ai/
- Employ Inc. — "AI Interview Companion (formerly Pillar)": https://www.employinc.com/ai-interview-companion/
- Hirevue — HireGuide acquisition notice and AI Interviewer / interview feature pages: https://www.hireguide.com/ , https://www.hirevue.com/
- GoodTime — homepage and product feature pages (boundary probe): https://goodtime.io/

> Sourcing limitations: vendor help-center depth varies; deep operational documentation was reachable for Metaview (full documentation index) and BrightHire (product FAQ pages), at product-page level for Employ and Hirevue, and at positioning level for GoodTime. The ATS-embedded pole (native structured-hiring documentation inside ATS products) was not directly examined this pass and relies on prior research passes plus integration documentation, so claims about ATS embedding are kept coarse. No precise numeric limits, defaults, or vendor performance statistics are asserted in this document; vendor-published performance claims were treated as marketing and excluded.

Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
