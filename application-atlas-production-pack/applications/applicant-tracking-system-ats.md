# Applicant Tracking System / ATS

## Overview

An **Applicant Tracking System (ATS)** is the employer-side application for running hiring: it tracks the positions an organization wants to fill, holds records of the candidates who apply or are sourced for those positions, and moves each application through a tracked selection pipeline — screening, interviews, offer — to a recorded outcome of hired or rejected.

The defining structure is small:

```text
Position / Job (demand side: the role to be filled)
└── Candidate record (identified person, with intake source)
    └── Application (candidate bound to a position)
        └── Pipeline stages (tracked selection workflow)
            └── Recorded outcome: hired or rejected (reason-coded)
```

Everything else the modern market associates with recruiting software — job-board distribution, careers pages, interview self-scheduling, scorecards, offer e-signature, talent pools, funnel analytics, AI assistance — is a widespread standard capability built around that core, not part of what makes the product an ATS. Older resume-database systems, regional products, and suite-embedded recruiting modules all remain recognizable under the core definition.

When the primary surface shifts to candidate-side job discovery, the product is a Job Board; when it shifts to managing employees after the hire, it has crossed into HRIS / onboarding territory.

## Users & Context

The operator is always the hiring side of the market: an organization filling its own openings, or a staffing firm filling openings on behalf of client employers. Candidates do not log into the ATS to search jobs; they enter it as applicants or sourced records.

Primary users, and what each does to the workflow:

- **Recruiter** — the pipeline owner: creates or receives job intake, manages the candidate pipeline, screens applicants, moves candidates between stages, drives communication, and coordinates the process end to end.
- **Recruiting coordinator** — schedules interviews, manages calendars and logistics for panels, and keeps candidates moving on time.
- **Hiring manager** — the requisition owner inside the business: requests the role, often approves the job or offer, reviews shortlisted candidates, and holds decision authority on their position.
- **Interviewer** — participates in scheduled interviews and submits evaluation feedback, typically seeing only the candidates and stages relevant to them.

Secondary concerns sit with administrators: configuring pipelines, application forms, templates, permissions, and compliance settings. In the staffing-agency variant, account/sales roles managing client relationships work in the same system alongside recruiters.

The context is collaborative and deadline-driven: multiple people act on the same candidate, decisions are distributed, and the system is the shared record of who is in the process, where they stand, and what has been decided.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as an ATS:

- **Employer-side operation** — the system is operated by the hiring organization (or a staffing firm acting for client employers) to manage its own hiring. This is what separates the Type from every candidate-facing surface.
- **Position as the demand-side object** — candidates are tracked against named openings the employer wants filled (a "job," "requisition," or "job order"). Without this anchor, the product is a contact database or a posting channel, not an ATS.
- **Candidate records with per-position applications** — each candidate is an identified person record carrying one or more applications, each application bound to a specific position and marked with its intake source. One person can be considered for several positions at once.
- **Tracked selection workflow toward a recorded outcome** — each application moves through a defined pipeline of selection stages under deliberate user action (advance, reject), ending in recorded terminal outcomes: hired or rejected, with rejection tied to a recorded reason. The tracked movement is the "tracking" in the name.

The demand side and the supply side have parallel lifecycles. A position itself is created, approved or opened, actively recruited for, and eventually closed — filled by a hire or canceled without one. Candidate pipelines hang off the position; the position does not close until its hiring outcome is recorded.

### Standard Capabilities

Mature products commonly carry most of the following. They make an ATS practical; they do not define the Type.

- **Position intake and lifecycle machinery** — job creation from templates, approval workflows before a job opens, requisitions or openings expressing headcount (one position, several people to hire), close/cancel with reasons.
- **Posting and distribution** — publishing the opening to the employer's careers page, syndicating to external job boards, sharing socially, scheduling publication and closing.
- **Application capture** — per-job application forms with screening questions; structured recording of intake source (board, referral, agency, direct, sourced).
- **Hiring team model** — recruiters, coordinators, hiring managers, and interviewers with role- and job-scoped permissions; what a user sees and can do typically depends on their role on that specific job.
- **Interview scheduling** — event scheduling with calendar integration, availability collection, and in some products candidate self-scheduling.
- **Structured evaluation** — scorecards or evaluation forms tied to stages, interview plans, sometimes rules that keep reviewers' scores hidden from each other until submitted, and take-home tests or assessments as pipeline steps.
- **Offer machinery** — offer creation from templates, offer documents with e-signature, approval gates before an offer goes out, and the hire that follows acceptance.
- **Rejection machinery** — disqualification with recorded, often customizable reasons; rejection notifications; sometimes the ability to reverse a rejection.
- **Candidate communication** — email (and often texting) from within the system, templates, and a per-candidate activity timeline that separates internal notes from candidate-facing messages.
- **Candidate database** — searching and filtering across all candidates, tags, saved candidates, and talent pools for people not currently in a process.
- **Analytics** — funnel and stage reporting, time-in-stage, source effectiveness, hiring-plan progress.
- **Compliance surfaces** — demographic self-identification reporting where required (e.g. EEOC/OFCCP-style in the US), data-protection tooling (retention, purging, consent), audit logs.
- **Post-hire handoff** — export or sync of the hired candidate's record into the HRIS/onboarding system, which takes over at the hiring event.

### One Structure, Many Implementations

```text
Concept:        Position to fill
Implementations: job (with pipeline and candidate pool), requisition/opening with headcount,
                 agency job order for a client

Concept:        Application
Implementations: application attached to a job, "candidacy"/"consideration" per job,
                 agency submission of a candidate to a client's order

Concept:        Outcome
Implementations: hired → position filled; rejected → reason recorded; agency placement
```

A reader who has only seen a lightweight small-business tracker should still recognize an enterprise suite module, and vice versa: the four core properties are the same.

## How It Works

### Open a position

```text
Hiring need identified
→ create the job/requisition (title, department, location, description, salary)
→ route for approval where the organization requires it
→ position opens for recruiting
```

The approval step is common but not universal — smaller teams often open jobs directly. Organizations that track headcount may attach one or more openings to a job and require that opening before recruiting starts.

### Attract and capture candidates

```text
Publish the opening (careers page, job boards, social, referral program)
→ candidates apply through the application form
→ application is recorded against the position with its source
→ other intake channels feed the same pipeline:
   recruiters add candidates manually or from sourcing searches,
   employees submit referrals, agencies submit their candidates
```

The pipeline accumulates candidates regardless of channel; the source travels with the application and later feeds source-effectiveness reporting.

### Screen and progress the pipeline

```text
Review new applications (resume, answers, screening questions)
→ advance promising candidates to the next stage
→ disqualify others with a recorded reason
→ repeat per stage until a shortlist emerges
```

The pipeline view — stages as columns with candidate counts — is the recruiter's primary working surface. Moving a candidate is an explicit, recorded, permission-gated act; nothing advances silently.

### Interview and evaluate

```text
Select candidates for a stage
→ schedule interviews (coordinator collects availability; panels invited)
→ interviewers submit evaluations against the stage's scorecard
→ hiring team reviews feedback and decides: advance or reject
```

Evaluation feedback accumulates on the candidate's timeline alongside assessments, tests, and reference or background checks where used.

### Decide and close

```text
Choose the finalist
→ create the offer, route for internal approval
→ send offer document for e-signature
→ candidate accepts (or declines)
→ candidate is marked hired; the position closes as filled
→ hired record is handed off to HRIS/onboarding
```

Candidates not selected are rejected with a recorded reason; many products keep them in the candidate database for future openings. The hire is a recorded event in the pipeline — in mature products it is commonly an explicit action, not an inference from offer acceptance — and it is the seam where the ATS ends and onboarding begins.

### Tiering of capabilities

- **Defining core** — position, candidate records, per-position applications, tracked stage workflow, recorded hire/reject outcomes.
- **Standard capabilities** — approval workflows, posting/distribution, application forms, scheduling, scorecards, offers with e-signature, rejection reasons, communication, database/talent pools, analytics, compliance surfaces, HRIS handoff.
- **Optional / variant** — texting, WhatsApp channels, video interviewing, AI matching and drafting, internal-mobility boards, confidential postings, agency-side client CRM, suite bundling.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Jobs dashboard / hiring plan

The demand-side entry surface. Lists positions with their status (draft, awaiting approval, open, filled/closed), how many are being hired for, and progress signals. Primary actions: create a job, route approvals, open or close positions, jump into a pipeline.

### Job pipeline view

The recruiter's main workspace for one position.

- Purpose: track every active application for the job through the selection stages.
- Typical information: stages as columns, candidates per stage, days in stage, next action needed, referral/private/internal flags.
- Primary actions: add a candidate, move a candidate between stages (often drag-and-drop), disqualify, open a candidate profile.

### Candidate profile

The record and action surface for one person.

- Typical information: contact details, resume and application answers, experience, source, current stage and evaluation results for it, activity timeline (messages, events, comments, files), other candidacies for the same person.
- Primary actions: email/text the candidate, schedule an event, add an internal comment, submit an evaluation, move stage, disqualify, request an offer or a check, export to HRIS.

### Candidates database / search

Cross-job search over all candidate records — filters, tags, saved searches, talent pools. Primary actions: search, add candidate, add to a pool or a job, tag, block.

### Scheduling surface

Interview coordination: availability requests, calendar integration, panel assignment. In some products candidates self-schedule from proposed slots.

### Offer surface

Offer creation from templates, approval routing, document generation with e-signature, and acceptance tracking tied to the position.

### Analytics / reports

Funnel views, stage-conversion and time-in-stage metrics, source performance, hiring-plan progress against open requisitions.

### Candidate-facing surfaces

The application form on the careers page, confirmation and status notifications, interview invitations, and (in some products) a self-service view of application status or self-scheduling. Candidate-facing communication is kept visibly separate from internal notes.

### Settings / administration

Pipeline stage templates, application forms, email templates, approval workflows, roles and permissions, job-board connections, integration configuration, compliance and retention settings.

## Important Rules / Behaviors

### The position anchors everything

Applications exist relative to a position; the hire or rejection is recorded against it. A candidate may have several concurrent applications — they are the same person record, with separate pipelines per position. Deleting or closing the position does not erase the candidate's history in the database.

### Stage movement is deliberate and attributed

A candidate does not drift through the system: advancing, rejecting, and hiring are explicit actions taken by a permitted user, recorded on the timeline with actor and time. Permission to move candidates is typically scoped by role on the job.

### Rejection is structured data

Disqualification is not just a status: mature products record a reason (frequently drawn from a maintained reason list), send a configurable notification, and keep the rejected application queryable. Some products allow reversing a rejection. This machinery exists because rejection reasons feed compliance and process reporting.

### The offer does not automatically equal the hire

In products that track headcount, the position typically closes as filled only when the candidate is explicitly marked hired in the pipeline — an accepted offer alone leaves the requisition open. The recorded hire, not the offer, is the event downstream systems (HRIS, onboarding, payroll) react to.

### Internal notes and candidate communication are separate worlds

Comments and evaluations are internal-only; candidates see the communication channel, not the deliberation. Some products additionally delay the visibility of evaluation scores between panel members until each has submitted their own, as a bias control.

### Visibility is job-scoped

A hiring manager generally sees their own jobs' candidates; interviewers see what they are assigned to; sensitive or confidential openings restrict visibility further. Data protection is a structural surface, not an afterthought: retention and purging of candidate data, consent handling, and demographic-reporting privacy controls appear wherever the regulatory regime requires them.

## Variants

- **In-house talent-acquisition ATS** — the default shape: an employer running its own hiring (the researched mainstream).
- **Staffing-agency ATS** — the same core operated on behalf of client employers: client accounts, job orders per client, submissions and placements as outcomes, usually with a client-facing CRM and billing-adjacent modules bundled in.
- **Suite-module ATS** — recruiting embedded in an HR/HCM suite; the same core structure with deeper native coupling to the employee record.
- **All-in-one recruiting platform** — standalone ATS plus built-in sourcing CRM, employer branding, scheduling, and analytics under one roof.
- **SMB vs enterprise posture** — lightweight quick-start trackers vs configurable enterprise deployments (approval chains, custom objects, sandbox environments, BI export).
- **AI posture** — from none, through assistive features (drafting, matching, auto-rejection of unqualified applications, fraud screening), to agentic operation of parts of the pipeline.
- **Internal mobility mode** — the same pipeline machinery pointed at current employees applying to internal openings.

A variant remains a variant as long as the four core properties hold; a product that abandons the employer-side pipeline (or the position anchor) has become a different Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Recruiting Management Platform | umbrella / near-alias | the market uses the names almost interchangeably; "recruiting platform" frames the same candidate-tracking core plus bundled sourcing, scheduling, and analytics capabilities — flagged for joint review |
| Job Board | intake channel, candidate-side | candidate discovery and application; the ATS is the receiving employer-side system that boards deliver into |
| Career Site Platform | publishing surface | employer-branding and job publishing; an ATS commonly hosts or feeds one, but a careers site has no selection pipeline |
| Interview Scheduling Platform | embedded capability | standalone scheduling products exist and integrate, but scheduling inside the ATS is one step of the pipeline |
| Candidate Assessment Platform | embedded capability | testing/assessment runs as a pipeline step via integration or built-in modules |
| Background Check Platform | embedded capability | ordered and returned as pipeline steps around the offer stage |
| Offer Management Platform | embedded capability | offer creation, approval, and e-signature are standard ATS machinery; deep standalone products exist |
| Candidate Search / Talent Sourcing Platform | upstream | discovers and identifies people; its output is candidate records feeding the ATS pipeline |
| HRIS / Employee Onboarding Platform | downstream seam | the ATS owns candidate → offer → hired; onboarding begins at the hiring event — the market itself describes products that "sit between the ATS and the HRIS" |
| CRM (Sales) | different graph | manages client/customer revenue relationships; only the staffing-agency variant bundles one, for its clients |
| Admissions Management | structural analog | the same application → review → decision shape for student intake, with different population, demand-side objects, and compliance semantics |

## Representative Products

- Greenhouse Recruiting — mid-market/enterprise; structured-hiring philosophy
- Workable — SMB/mid-market; generalist recruiting software with requisition machinery
- Ashby — newer-generation, analytics-first all-in-one
- Bullhorn — staffing-agency side (ATS + client CRM, placements)
- Tellent Recruitee — European SMB; jobs, pipelines, and careers site in one

The core model was checked against historical (resume-database-era), suite-embedded, and regional product shapes to avoid defining the Type by today's dominant implementation.

## Sources

Research date: **2026-09-06**

Primary vendor documentation:

- Greenhouse Support — Create a new job; Visual Candidate Pipeline; Jobs and job openings; Job openings; Rejections; All Recruiting topics — https://support.greenhouse.io/
- Workable Help — Requisition statuses; Candidate profile in pipeline view overview; Recruiting category; Candidate profile & pipeline view — https://help.workable.com/
- Ashby Knowledge Base — home, Jobs & Openings, Applications — https://docs.ashbyhq.com/
- Bullhorn — ATS & CRM product page and FAQ — https://www.bullhorn.com/products/applicant-tracking-system/
- Tellent Recruitee Help Center — home and Jobs collections — https://support.recruitee.com/

> Sourcing limitations: Ashby, Bullhorn, and Tellent Recruitee were documented at knowledge-base index / product-page level (deep help articles not fetched on 2026-09-06); claims about those products are calibrated accordingly and precise operational details are not asserted. Exact stage vocabularies, plan gating, and numeric limits vary by product and are intentionally not stated as general facts. Detailed evidence, per-product observations, and the cross-product comparison are recorded in the paired Research Notes.
