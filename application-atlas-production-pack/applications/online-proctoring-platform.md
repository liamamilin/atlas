# Online Proctoring Platform

## Overview

An **Online Proctoring Platform** supervises a test-taking session remotely: it binds the session to an identified test-taker, verifies the taker's identity and testing environment before the assessment begins, observes the session through camera, screen, and audio capture — live, recorded, or both, by human proctors and/or automated monitoring — and delivers the resulting integrity record (time-stamped flags, recordings, incident reports) to the institution, whose own people review the evidence and decide what, if anything, happened.

The defining structure is small: a supervised session, observation of the test-taking, and integrity evidence left for human judgment. Everything else commonly associated with these products — identity-document checks, room scans, lockdown browsers, AI detection, live proctor chat, 24/7 support — makes supervision practical but is machinery around that core.

One boundary is structural: the platform supervises an assessment that **something else delivers and owns**. The exam itself runs in a learning management system, an examination platform, publisher courseware, or a third-party testing site; the proctoring platform wraps it. It does not author questions, score answers, or hold results — one sampled vendor states directly that it has no access to exam results. If a product owns the exam occasion, the roster, and the official result, it is an examination platform with proctoring integrated; the standalone proctoring platform is the supervision service by itself.

## Users & Context

**Test-taker** — a student, certification candidate, or workforce candidate who completes an assessment at a remote (or sometimes test-center) location while being observed. Their experience is dominated by the pre-exam check-in sequence and the awareness of being watched during the exam.

**Proctors** — the people who perform the supervision. Depending on the product and service tier they may be:

- employees of the proctoring vendor, watching live or reviewing recordings afterward
- the institution's own staff (instructors, test-center staff, certification proctors) operating the vendor's proctoring console
- no one in real time — the session is recorded and monitored by automated detection, and reviewed by the instructor afterward

**Instructor / exam administrator** — configures proctoring for their assessments, and is usually the person who receives the post-exam integrity record and decides what flagged events mean.

**Institution administrator** — manages accounts, integrations, roles, policies, and institution-wide settings.

Typical contexts: university and school online courses (the largest segment), professional certification and licensure programs, workforce hiring and compliance testing. The setting is usually the test-taker's home or office; some vendors also offer a test-center mode where the same supervision structure is applied in person.

## Core Model

### The Defining Core

```text
Identified test-taker
└── Supervised session (bounded sitting bound to that taker)
    ├── Networked observation (camera / screen / audio — live, recorded, or both;
    │    human proctors and/or automated monitoring)
    └── Integrity record (flags, incidents, recording, report)
        └── Human review by the institution → decision
```

Three properties, held together:

- **The supervised session.** A bounded sitting in which an identified person completes an assessment, with the session tied to that person in the institution's context. Remove it and there is nothing to supervise — just an exam link.
- **Networked observation of the test-taking.** The taker's person, workspace, and/or screen is observed while the assessment runs. Remove observation and the product degrades into an access-control tool (a locked-down browser with nobody watching is exam security, not proctoring).
- **Integrity evidence for human judgment.** The session leaves a reviewable record that flows back to the institution. The platform never adjudicates on its own; people review the evidence. Remove this and the product is a video feed or surveillance footage with no institutional purpose.

Wrapped around all three: the assessment being taken is delivered by another system. The proctoring layer attaches to that delivery — it authenticates the taker into it, watches it, and reports on it.

### What Mature Products Add

These capabilities are widespread and expected in current products, but they sharpen the core rather than define it:

- **Identity verification** — capturing the taker's photo and an approved ID document, often with face matching; some products verify live before entry, others validate the captured images by human review after the exam.
- **Environment scan** — the taker shows their room, desk, and allowed materials via photos or a short video (self-guided or proctor-guided).
- **System and equipment checks** — webcam/microphone/screen-sharing permission grants, bandwidth and device checks, and a tool for testing equipment before exam day.
- **Rules and accommodations display** — what materials are allowed, what actions are prohibited, and any approved accommodations, surfaced inside the check-in flow.
- **Lockdown layer** — a secure browser or browser extension that blocks other applications, tabs, printing, copying, and shortcuts. Common, but explicitly optional in some products, which can run pure observation with minimal or no blocking.
- **Real-time support** — chat with the proctor or a support team during the exam, plus 24/7 help desks and exam-day guidance.
- **Flag records with timestamps** — automated detection produces time-stamped events (another person in view, a voice, a second device, leaving the frame, disallowed resources) that a reviewer can jump to in the recording.
- **LMS embedding and integrations** — launching proctored exams from the LMS, syncing settings and rosters, APIs and single-sign-on for institution-scale deployment.
- **Accommodation handling** — configurable allowances (screen readers, breaks, extra movement tolerance) so approved accommodations are not mistaken for misconduct.

### One Structure, Many Implementations

```text
Concept:      Identity verification
Realized as:  selfie + government ID photo, document validation with face matching,
              live proctor inspection of ID, human review of captured images after the exam

Concept:      Observation channels
Realized as:  webcam video, screen recording/sharing, microphone audio, desk scan,
              second/side camera, phone/device detection

Concept:      Supervision capacity
Realized as:  vendor-employed live proctors, vendor reviewers of recordings,
              automated AI monitoring, the institution's own proctors on the
              vendor's console, the instructor watching via a video conference

Concept:      The lockdown layer
Realized as:  a dedicated secure browser app, a browser extension, or in-page
              blocking inside the LMS exam

Concept:      The integrity record
Realized as:  a flag list with timestamps and recording playback in the instructor's
              LMS view, a proctor-verified report with an audit trail, or a
              session-status record reviewed through the vendor portal
```

A reader who has only seen one form — say, a fully automated webcam recording reviewed by an instructor — should still recognize a live-proctored certification exam or an institution-staffed proctoring console as the same kind of product.

## How It Works

The product's whole work is one session lifecycle. Everything below recurs across the researched products, with product-specific variations noted in the Variants section.

### 1. Attach to the exam

The institution enables proctoring on an assessment — usually inside the LMS or through the vendor's portal — and configures it: which observation channels to use, whether identity verification is required, how strict the lockdown is, how sensitive flagging should be. The same product can secure a fully locked-down professional exam and a lightly monitored open-book quiz; strictness is a per-exam configuration, not a property of the product.

### 2. Prepare (before exam day)

The test-taker installs the client (secure browser, extension, or nothing beyond the LMS), runs an equipment check, and reviews guidance about the exam environment and allowed materials. Products with appointment-based live proctoring add a scheduling step: the taker books, reschedules, or cancels a session slot. On-demand products skip this entirely — the exam can be started any time.

### 3. Check in (pre-exam authentication)

A guided sequence inside the proctoring layer, typically:

```text
Open the proctored exam (LMS, portal, or exam link)
→ consent to terms / privacy notice
→ system and permission checks (camera, microphone, screen sharing)
→ identity verification (photo + ID; face match; or live proctor inspection)
→ room / desk scan (show the workspace and allowed materials)
→ review exam rules, allowed resources, and accommodations
→ enter the waiting state (lobby)
```

With a live proctor, the proctor connects through chat, may repeat or extend the checks (inspect the ID again, examine materials, look around the room, check monitors or wrists, or temporarily take control of the device to close unpermitted applications), and then releases the taker into the exam — often by entering the exam password themselves or letting the client auto-fill it. With automated supervision, the taker clicks "begin" themselves after the checks pass.

### 4. Observe (during the exam)

The taker takes the exam in the delivery system while the proctoring layer runs alongside: recording the webcam (and often the screen and audio), watching behavior against the configured rules, and either maintaining a live connection (proctor chat visible, proctor ready to intervene) or recording silently. Live proctors intervene when they see a disallowed action — a warning, a request to re-secure the room after leaving the camera's view, or (in hybrid products) an AI-detected event that a proctor checks in real time and pops into the session about only when it looks like a genuine violation. Automated monitoring flags events continuously for later review. Proctors answer procedural questions but do not help with exam content.

### 5. Close and hand over the record

The taker submits the exam (with a live proctor, they usually notify the proctor first, who may ask for closing steps — showing notes, erasing a whiteboard — before ending the session). The proctoring layer then produces the integrity record: the recording, time-stamped flagged events, incident notes, and session status. This record goes to the institution — typically surfaced inside the LMS for the instructor, or through the vendor's review portal.

### 6. Review and decide

The instructor, exam administrator, or a vendor review team examines the record: jumping to flagged moments in the recording, adding or removing flags, annotating, and judging whether anything constitutes misconduct. The consequence of a confirmed violation belongs to the institution's own processes — grades, certification decisions, disciplinary procedures — not to the platform. In service tiers aimed at high-stakes programs, the vendor's trained proctors perform this review themselves and return a human-verified report to the institution.

## Interfaces

### Test-taker check-in flow

The guided pre-exam sequence: consent, system checks, identity capture, room scan, rules review, waiting lobby. Purpose: establish who is testing, in what environment, under what rules before the exam starts. Primary actions: grant permissions, capture photos/video, confirm rules, begin.

### In-exam companion surface

What overlays the exam while it runs: a recording indicator, the proctor chat window (where live proctoring is used), lockdown restrictions, and support access. Primary actions: chat with proctor/support, request or announce breaks, submit.

### Scheduling portal (appointment-based tiers)

The test-taker's list of upcoming proctored sessions with exam rules, plus booking, rescheduling, and cancellation. On-demand products have no scheduling surface at all.

### Proctor console

The supervisor's working surface, whether staffed by the vendor or the institution: a queue or dashboard of sessions, per-session live video/screen view, chat and intervention controls, device-takeover tools, incident recording, and — for institution-staffed setups — management of multiple simultaneous sessions.

### Instructor review surface

Where the integrity record is consumed, usually inside the LMS: the session's flag list with timestamps, recording playback anchored to those moments, flag verification tools (confirm, add, remove), annotations, and the session's overall status. Primary actions: review flags, watch segments, annotate, decide.

### Administration and configuration

Institution-side setup: enabling proctoring per exam, choosing observation channels and strictness, identity-verification and accommodation settings, roles and permissions, integrations (LTI, SSO, APIs), reporting and analytics, and policy templates (syllabus language, proctoring policies) for communicating with test-takers.

## Important Rules / Behaviors

**Flags are evidence, not verdicts.** Automated detection and human observation alike produce flags for review; the reviewed sample shows no product that automatically fails or penalizes a test-taker. Every product frames the flag as an input to human judgment — instructors, proctors, or administrators decide, under the institution's own policies. Vendors differ on who reviews and when (real-time pop-in, post-hoc instructor review, or vendor verification of every recording), not on whether the platform decides.

**The platform holds neither the exam nor the results.** The assessment is delivered elsewhere, and the proctoring layer's output is the integrity record only. One vendor states plainly that it has no access to exam results; the others are structured the same way.

**Strictness is per-exam configuration.** The same product runs a fully locked-down, identity-verified sitting and a minimally monitored open-resource quiz. Observation channels, lockdown level, ID requirements, and flagging sensitivity are all configuration.

**Proctors support procedure, not content.** Live proctors answer questions about the proctoring experience — setup, breaks, technical trouble — but the proctoring layer holds neither the exam's content nor its results, so proctors are in no position to assist with the subject matter; vendors state this rule explicitly in their test-taker guidance.

**The room is part of the contract.** Test-takers are expected to remain alone, in view, in a compliant workspace; leaving the camera's view or taking a break typically requires notifying the proctor and may require re-securing the room afterward.

**False positives are a managed, first-class problem.** Background noise, pets, normal movements, and approved accommodations can all trigger automated flags. Products answer with flag-sensitivity settings, human filtering of flags in real time, review passes that verify or remove flags, and fairness testing of detection algorithms.

**Accommodations live inside the flow.** Approved accommodations are surfaced during check-in and honored during supervision — through configurable allowances, proctor awareness, or human review that keeps disability-related behavior from being flagged as cheating.

**Identity verification can happen before or after.** Many products verify identity live during check-in; some also (or instead) validate the captured ID images by human review once the session is over.

## Variants

- **Supervision-mode spectrum** — the market's main axis: continuous live human proctoring (appointment-based, high-touch); record-then-review (session recorded, humans verify afterward); fully automated (AI monitoring, instructor review); hybrid AI-plus-human (automated monitoring with live proctors intervening only on real violations); and institution-staffed proctoring, where the organization's own proctors run the vendor's console.
- **Instructor-as-proctor** — in some products the instructor can supervise via a video conference while the platform supplies lockdown and recording.
- **Scheduling model** — appointment-based sessions with booking and no-show rules versus on-demand testing available at any time.
- **Client form** — dedicated secure browser, browser extension, native app, or nothing beyond in-page tooling.
- **Setting** — remote proctoring at home or office versus test-center proctoring; several vendors offer both, and test centers themselves use these platforms.
- **Sector packaging** — higher education, K-12, certification and licensure, workforce hiring and compliance. The vocabulary shifts (student / candidate / test-taker) but the session structure does not.
- **Adjacent stretches of the same machinery** — securing interviews and presentations; proctoring exams hosted outside any LMS ("third-party" or "universal" exams).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Examination Platform | closest neighbor, frequently integrated | the examination platform owns the exam occasion of record — scheduling, enrolled candidates, the sitting itself, governed marking, and the official result; the proctoring platform contributes only the supervision and owns neither content nor results. An examination platform can integrate proctoring as a module; a proctoring platform cannot absorb the examination's role without becoming one |
| Assessment Platform | adjacent | delivers and scores assessments (items, scoring rules, results); proctoring adds no items, no scoring, and appears there only as a high-stakes add-on |
| Academic Integrity / Plagiarism Platform | sibling under the "integrity" umbrella | analyzes submitted written artifacts after the fact (similarity to recorded sources); proctoring observes the live exam-taking process. Remove live observation and the plagiarism platform stands; remove artifact analysis and proctoring stands |
| Virtual Classroom / Video Conferencing | shares media, not purpose | webcams, chat, and live video — but no instruction, no meeting; the session exists to supervise an assessment and leaves an integrity record |
| Identity Verification / KYC | capability overlap | identity checks are one step inside the proctoring check-in, in service of the session; identity-verification products make identity assurance itself the product |
| Video Interview / Hiring Assessment Platform | gradient at the edge | interview platforms center the conversation as the evaluated interaction; proctoring observes someone else's evaluation of the taker (some proctoring vendors stretch their machinery to securing interviews) |
| Lockdown-browser tools | companion capability | environment control without observation is exam security, not proctoring; it ships both standalone and bundled, and observation is what turns lockdown into supervision |

## Representative Products

- **ProctorU / Meazure Learning** — live-proctoring lineage; service tiers spanning live proctoring, human-reviewed recordings, and automated recording; secure-browser client; test-center network
- **Proctorio** — automated-first, LMS-embedded proctoring with configurable observation channels and optional lockdown; institutions keep every decision
- **Honorlock** — hybrid model: AI monitoring with live proctors who review flags in real time and enter the session only on genuine violations; bring-your-own-proctor option
- **Respondus (LockDown Browser + Respondus Monitor)** — lockdown-browser heritage with fully automated webcam proctoring layered on top; LMS and publisher courseware integrations

## Sources

Research date: **2026-09-08**

- ProctorU Help Center — Test-Taker Library and Test Owners & Instructors: https://support.proctoru.com/hc/en-us/ , including "What to Expect on Exam Day": https://support.proctoru.com/hc/en-us/articles/9951434736525-What-to-Expect-on-Exam-Day
- ProctorU portal: https://www.proctoru.com/ · Meazure Learning — Remote Exam Proctoring: https://www.meazurelearning.com/exam-proctoring/remote-exam-proctoring
- Proctorio — homepage (settings and suites): https://proctorio.com/ · Integrity solution page: https://proctorio.com/solutions/integrity · Help Center structure: https://proctorio.com/support
- Honorlock — homepage: https://honorlock.com/ · Live Pop-In: https://honorlock.com/live-pop-in/ · Service Options: https://honorlock.com/services/ · Help Center: https://honorlock.kb.help/ (including "How to Use Honorlock (Test Takers)" and faculty guides)
- Respondus Monitor — product page: https://web.respondus.com/he/monitor/

> Sourcing limitations: Proctorio's help-center article bodies were not readable from the research environment (client-side rendering); Proctorio operational mechanics are asserted from its product pages and help-center category descriptions only, and no precise operational details are claimed for it. Respondus Monitor's identity-verification depth was not verifiable from the captured material and is not asserted. Vendor scale figures, accuracy claims, and pricing details from marketing pages are deliberately excluded from this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
