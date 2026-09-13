# Examination Platform

## Overview

An **Examination Platform** is an organizer-side system for running formal examinations end to end: it turns an assessment instrument into a scheduled, officially sanctioned exam occasion; enrolls the candidates who are admitted to it; runs the sitting under conditions the organizer declares and enforces; governs the marking of the captured work; and releases the outcome as the **official result of record** for each candidate.

The defining core is small — four structures that exist in every product of this Type:

```text
Examination (occasion of record: instrument + declared rules + schedule)
└── Enrolled candidates (formal roster binding)
    └── Sitting (platform-enforced session under declared conditions)
        └── Governed evaluation (graders / committees / moderation)
            └── Official result of record per candidate
                └── Publication / transfer (candidates, institution, registries)
```

What distinguishes this Type from a general testing tool is not the questions themselves but the **exam as an event**: the platform owns the scheduling, the roster, the enforced session, the exception handling during and after the sitting, and the governed release of results. A paper exam in a supervised hall — printed papers, an attendance list, timed invigilation, hand-marked scripts, a published grade list — is the same structure realized without software, and current products still preserve paper, scanned, offline, and oral exam paths as first-class modes.

## Users & Context

**Organizer side** (the platform's center of gravity):

- **Exam planner / administrator** — creates the exam occasion: attaches the instrument, sets the schedule and conditions, enrolls candidates, activates the event, and manages it through to released results.
- **Author / item owner** — builds and maintains the question sets, banks, rubrics, and mark schemes the exams draw from (sometimes the same person as the planner, sometimes a separate role with separate access).
- **Grader / marker** — evaluates captured responses against rubrics and scales; at institutions, graders often work in committees with shared or confirmation workflows.
- **Invigilator / proctor (exam-day role)** — supervises the sitting: starts sessions, monitors candidate status, intervenes on problems, records incidents.
- **Institution / program administrator** — owns roles, integrations, reporting, and compliance; at professional-program and certification poles, also accreditation and outcome analysis.

**Candidate side:**

- **Exam taker** — a formally enrolled person who takes the exam under the occasion's conditions (log-in or lockdown client, declared window, supervised or controlled environment) and later receives the official result.

Typical contexts: university and school final exams and retakes; national and institutional examination programs; professional education (health sciences, law) with accreditation requirements; certification and licensure exams run by organizations and government bodies.

## Core Model

### The Defining Core

**1. The examination as an occasion of record.** An exam is an identified, persistent event assembled from an instrument (question set, tasks, or a recording shell for external/oral work) plus declared rules: when it opens and closes, how long candidates have, what delivery conditions apply, how results will be produced. The occasion persists as the unit that everything else — enrollment, sitting, marking, results, appeals — attaches to. Remove it and the product degrades into a reusable quiz.

**2. Enrolled candidates.** The organizer formally binds identified candidates to the occasion: roster import, account provisioning, registration, or access granting (per-candidate codes, invitations through an LMS or student-record system). The sitting is a rostered event with accountability, not an open link. Enrollment is also the platform's admission control: candidates outside the roster do not sit the exam.

**3. The sitting under organizer-enforced conditions.** The platform, not the candidate, controls the session's boundaries: the exam opens at the declared time, the duration is enforced, submission is captured at close, and the sitting runs under conditions the organizer selected — from fully invigilated or device-locked environments to controlled open-browser modes. During the sitting the organizer side has a monitoring surface showing candidate progress and status, with tools to intervene. Remove the enforced session and the product becomes a practice or self-study tool.

**4. Governed evaluation producing official results.** Captured responses are evaluated through a managed marking process — automatic scoring for closed items plus human marking for open ones, organized through grader roles and, at the institutional pole, grading committees and moderation, with confirmation before anything becomes final. The outcome is then **released**: published to candidates, reported to the institution, and transferable to student-record systems. Until release, results are working values, not the record.

### Standard Capabilities (what mature products add)

These are widespread in mature products and expected by the market, but they are the machinery around the core, not the definition:

- Item banks / question libraries with categories, reusable question sets, rubrics and mark schemes; rich question types with auto-scoring.
- Grading machinery: marking workspaces, grading scales and thresholds, grader assignment, anonymous marking options.
- Exam-day monitoring and exception operations: real-time progress, candidate status, resubmission, submit-on-behalf, make-up assessments, resume codes, incident review.
- Integrity apparatus scaled to stakes: lockdown browsers or dedicated lockdown clients, identity verification, live/AI proctoring integration; similarity checks in some products.
- Post-result rights: candidate-visible results and feedback; at the institutional pole, explanations of grades and appeal/reassessment workflows.
- Reporting and analytics: per-candidate and aggregate results, item statistics; psychometric or accreditation/outcome analytics at the program pole.
- Integration spine: student-information-system rosters, LMS/LTI launch and grade sync, SSO, open APIs, export files.
- Candidate preparation surfaces: system requirements, mock/demo exams, exam-day instructions.
- Accommodations and accessibility support; multi-language delivery in several products.

### One Structure, Many Implementations

```text
Concept:  Candidate enrollment
Realized as:  roster import from student systems, account registration,
              per-candidate access codes, exam IDs, LMS invitations

Concept:  Enforced sitting
Realized as:  invigilated lab + monitoring console, lockdown browser,
              offline lockdown client (answers uploaded after), remote proctoring,
              controlled open-browser home exam

Concept:  Evaluation governance
Realized as:  single grader, grader pairs with co-signing, grading committees,
              moderation steps, mark confirmation before release

Concept:  Official result release
Realized as:  in-product publication, scheduled release, transfer to the
              student-record system, candidate result review under supervision
```

A reader who has only seen one implementation (say, a fully locked-down professional exam) should still recognize a school's open-book home exam, or a scanned paper exam, as the same Type.

## How It Works

### 1. Plan the exam occasion

```text
Author or reuse an instrument (question set / tasks)
→ declare schedule: opening time, closing time, duration
→ declare conditions: delivery mode, security level, allowed aids,
  grading scale, feedback policy
→ (institutional pole) set up grading: graders, committees, workflows
→ activate the exam
```

Activation makes the occasion visible to its enrolled candidates and typically notifies the graders. Before activation, the exam exists only on the organizer side.

### 2. Enroll the candidates

```text
Import or register the roster (student system, CSV, accounts)
→ bind candidates to this occasion
→ issue access (login, exam ID, or per-candidate code)
→ (optional) anonymize candidate identity toward graders
```

### 3. Run the sitting

```text
Exam opens automatically at the declared time (or is started by the invigilator)
→ candidates take the exam under the declared conditions
→ organizer side monitors progress and candidate status in real time
→ problems are handled as they occur: interruptions, resumes,
  supervisor interventions, incident records
→ session ends at duration or closing time; work is captured/submitted
```

### 4. Handle exceptions

Exams are high-consequence events, so exception handling is part of the product, not an afterthought: resubmission windows opened for a candidate who failed to submit, submitting on a candidate's behalf after verification, make-up assessment creation, resume codes after device failure, and incident review for suspected misconduct with recorded dispositions.

### 5. Evaluate under governance

```text
Auto-scored items scored immediately
→ graders mark open responses against rubrics/scales
  (individually, or in committees with shared/confirmation workflows)
→ marks confirmed / moderated
→ final result computed per candidate
```

### 6. Release the official result

```text
Publish results to candidates (instantly, scheduled, or after moderation)
→ provide explanations of grades / feedback / result review
→ accept appeals or reassessment where offered
→ transfer/export results to student-record systems and registries
```

The released result is the exam's output of record: it feeds transcripts, progression, certification, and accreditation reporting.

## Interfaces

### Exam planning / setup

The organizer's workbench for one occasion.

- Typical information: instrument, schedule, conditions, security level, candidate list, grading setup, status.
- Primary actions: create/activate/disable the exam, edit settings, enroll candidates, configure grading.

### Candidate roster

The enrollment surface binding people to the occasion.

- Typical information: candidates, identifiers, enrollment state, access method, grading assignments.
- Primary actions: import/add/remove candidates, issue access codes, assign graders or committees, set accommodations.

### Monitoring console / invigilator view

The live exam-day surface.

- Typical information: per-candidate progress, status (not started / in progress / submitted / problem), timing, incidents.
- Primary actions: start a session, refresh status, message or intervene, record incidents, handle resumes.

### Marking / grading workspace

Where evaluation happens.

- Typical information: candidate responses, rubric and mark scheme, marks and grades, grader identity, confirmation state.
- Primary actions: score responses, apply scales, share with co-graders, confirm marks, add comments.

### Result publication & reporting

The organizer surface for official outcomes.

- Typical information: final results per candidate, distributions, item statistics, export status.
- Primary actions: publish/release results, send explanations, export results, run reports.

### Candidate exam surface

What the exam taker sees.

- Pre-exam: dashboard with upcoming exams, preparation materials, mock exams, system checks.
- During: the exam itself — questions, navigation, timer, submission — inside a browser or a locked-down client depending on the declared conditions.
- After: released results, feedback, explanations, appeal entry points.

## Important Rules / Behaviors

- **The platform owns the clock.** The window opens and closes on the declared schedule and the duration is enforced; candidates still working at close are submitted or cut off automatically in most implementations. A candidate cannot extend the sitting from their side.
- **Results are not official until released.** Working marks exist from the moment grading starts, but the result becomes the record of truth only through the release step — which may be immediate, scheduled, or gated behind moderation and confirmation at the institutional pole.
- **Enrollment gates the sitting.** Only enrolled candidates can access the exam, through whatever access mechanism the organizer issued; the roster doubles as the admission control.
- **Control conditions are declared per exam.** The same platform runs a fully locked-down, identity-verified sitting and a controlled open-browser home exam; the integrity apparatus is a configuration decision, not a fixed property.
- **Candidate identity and anonymity coexist.** Candidates are strongly identified for admission and record-keeping, while graders may work over anonymized submissions to keep marking impartial.
- **Exceptions leave traces.** Resubmissions, make-ups, resume codes, supervisor interventions, and integrity incidents are recorded against the occasion and the candidate, because the exam is a formal event whose history may be audited or appealed.
- **Released results are consequential.** Institutions commonly run explanation, appeal, and reassessment processes around them; where the platform supports these, a successful appeal corrects the official result through the platform rather than outside it.

## Variants

- **Stakes continuum** — ordinary school tests, course finals, institutional and national examination programs, professional certification and licensure. Stakes tune the configuration: security level, governance depth, auditability — not the core model.
- **Venue and client model** — campus computer labs with invigilated monitoring; bring-your-own-device with lockdown browsers; fully offline lockdown clients that capture answers locally and upload after; remote proctored exams taken anywhere; controlled open-browser home exams.
- **Supervision posture** — human invigilation in the room plus a monitoring console; remote live/AI proctoring as an integrated module; unproctored but access-controlled sittings.
- **Governance depth** — single grader with auto-scoring (school pole); grader pairs and committees with confirmation and moderation (institutional and national pole).
- **Hybrid and non-digital modes** — printed exams scanned for marking, "grading only" shells that register results from external work, offline exam files, oral exam modes.
- **Program analytics** — psychometric dashboards at large-scale programs; accreditation and learning-outcome mapping at professional programs.
- **Packaging** — institutional SaaS, national-scale platforms, open-source delivery engines deployed beneath testing programs, and lockdown add-ons that wrap LMS-run exams.

## Related Application Types

| Type | Distinction |
|---|---|
| Assessment Platform | shares the measurement loop (instrument → delivery → scoring → results); a general assessment tool lacks the exam occasion of record, formal enrollment, exam-day operations, and governed official release as its center. Strip the exam-operations layer and the product becomes an assessment platform |
| Learning Management System | centers course content and the gradebook; quizzes are a course feature. Examination platforms integrate into LMS/SIS and can even secure LMS-run exams, but the exam occasion and its official result are their whole product |
| Online Proctoring Platform | an integrity service consumed by examination platforms (or sold standalone); supervision is its whole product, while the examination platform runs the entire event of which supervision is one part |
| Test Preparation Platform | optimizes the taker's future performance through practice and instruction; the examination platform runs the official measurement event. Mock exams serve familiarization, not curriculum |
| Digital Gradebook / Transcript Management | recipients of released results; they keep ongoing academic records, while the examination platform produces the single event's official outcome |
| Candidate / Technical / Psychometric Assessment Platform (HR) | same delivery mechanics, but for hiring selection with HR record semantics — audience and purpose variant of the assessment family |
| Certification test-delivery networks | sponsor-facing scheduling and test-center logistics for certification programs; examination platforms may serve the same sponsors but center the institution's exam record |
| Survey Platform | collects opinions with no scoring criteria or official outcome; none of the four defining structures apply |

The Assessment Platform boundary is the important one, and it is a gradient in the market: several products are marketed across both. The center-of-gravity test: if the product would still make sense without occasions of record, enrollment, sitting operations, and official release — it is an assessment platform; if those operations are why the product exists — it is an examination platform.

## Representative Products

- **Inspera Assessment** — Nordic institutional examination platform (planner/invigilator/committee machinery, appeals, registry transfer)
- **ExamSoft** — high-stakes professional education and certification/licensure (offline lockdown client, integrity operations, accreditation analytics)
- **Digiexam** — school- and university-facing exam platform with a dedicated invigilator surface
- **TAO Testing** — open-standards delivery engine beneath institutional and national testing programs

The definition was checked against the paper-exam tradition (printed papers, invigilated halls, scanned scripts) and against non-Nordic and certification contexts to avoid over-fitting to any single region or implementation.

## Sources

Research date: **2026-09-07**

- Inspera Help Center — https://support.inspera.com/ (Deliver: test creation/settings, committees, moderation, appeals; Monitor: post-test management; Grade; Candidates)
- ExamSoft — https://examsoft.com/ and https://support.examsoft.com/hc/en-us (Exam-Makers: Enterprise Portal, Assessments create/post/proctor/grade, Exam Integrity, Map, Examplify; Exam-Takers: before/during/after exam, Bar Exam)
- Digiexam — https://digiexam.com/ , https://digiexam.com/platform/how-it-works , https://support.digiexam.se/hc/en-us (Knowledge Center structure: Teachers, Students, Administrators, Invigilator)
- TAO Testing — https://www.taotesting.com/ , https://www.taotesting.com/rostering-delivery/

> Sourcing limitation: Digiexam's help-center article pages were not reachable from the research environment (access denied after repeated attempts); claims about Digiexam rest on its fetched product pages and the Knowledge Center's category/guide structure, and no precise operational details are asserted for it. Precise numeric limits observed at other vendors are intentionally omitted from this document. Corroborating posture evidence for the assessment-management pole (Questionmark) is recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample breadth check are recorded in the paired Research Notes.
