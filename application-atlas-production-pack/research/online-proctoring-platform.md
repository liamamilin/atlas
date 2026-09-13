# Research Notes — Online Proctoring Platform

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an Online Proctoring Platform actually is by studying real products: what its unit of record is, what its session lifecycle looks like (before / during / after the exam), who the users are on both sides (test-taker and institution), how it attaches to the exam being taken, and where its boundaries run against the neighboring Types already documented under §23 (Examination Platform, Assessment Platform, Academic Integrity / Plagiarism Platform).

## Initial Boundary (pre-research hypothesis)

- Core purpose: supervise exam-takers remotely — confirm who is taking the exam, observe the session, flag suspicious behavior, and hand evidence to humans.
- Nearest neighbors: Examination Platform (owns the whole exam event), Assessment Platform (owns items/scoring/results), Academic Integrity / Plagiarism Platform (post-hoc artifact analysis), Virtual Classroom / video conferencing (same media, different purpose), Identity Verification / KYC (identity as the product vs one step inside a session).
- Prior sibling passes already recorded: plagiarism Type excludes live session surveillance ("that is online proctoring"); examination Type treats proctoring as "an integrity service consumed by examination platforms (or sold standalone); supervision is its whole product"; assessment Type treats it as a high-stakes add-on.

## Research Questions

1. What is the central object — a session? an appointment? a report?
2. What happens before the assessment (scheduling, system checks, identity verification, environment scan)?
3. What happens during (observation channels; live vs recorded vs automated; intervention mechanics)?
4. What happens after (flags, reports, who reviews, who decides)?
5. What does the platform explicitly NOT do (own the exam, score it, hold results)?
6. How does it attach to exam delivery (LMS extension, secure browser, vendor portal, API)?
7. What supervision modes exist across the market (live human / record-review / automated AI / hybrid / institution's own proctors)?
8. What exception behaviors matter (connectivity loss, false flags, breaks, accommodations)?
9. Where are the Type boundaries, and what "remove test" separates this Type from its neighbors?

## Representative Products

Selection rationale: market representation + documentation completeness + different product philosophies + different customer tiers and eras.

| Product | Philosophy / posture | Primary tier |
|---|---|---|
| ProctorU / Meazure Learning | live human proctoring lineage (positioned as pioneer, 2008); service tiers Live+ / Review+ / Record+; test-center network | professional credentialing + higher ed |
| Proctorio | automated/AI-first, LMS-embedded, institution-configured; explicit "decisions stay with the institution" | higher ed, K-12, workforce, credentialing |
| Honorlock | hybrid: AI monitoring + live proctor "pop-in" on real violations; no scheduling; BYOP option | higher ed + corporate/certification |
| Respondus (LockDown Browser + Monitor) | LMS add-on lineage: lockdown browser heritage + fully automated webcam proctoring; publisher integrations | higher ed + K-12 |

Not sampled (documented as gap, not silently filled): Examity, PSI, Inspera/Questionmark proctoring modules (the module form is evidenced from the examination/assessment passes' own research).

## Sources

Primary (Tier 1 — official help centers and product documentation):

- ProctorU Help Center — Test-Taker Library: https://support.proctoru.com/hc/en-us/categories/115001818507
- ProctorU Help Center — Test Owners & Instructors: https://support.proctoru.com/hc/en-us/categories/115001380867
- ProctorU — What to Expect on Exam Day: https://support.proctoru.com/hc/en-us/articles/9951434736525-What-to-Expect-on-Exam-Day
- ProctorU portal: https://www.proctoru.com/ (now Meazure Learning)
- Meazure Learning — Remote Exam Proctoring: https://www.meazurelearning.com/exam-proctoring/remote-exam-proctoring
- Proctorio — homepage (settings list, suites): https://proctorio.com/
- Proctorio — Integrity solution page: https://proctorio.com/solutions/integrity
- Proctorio — Help Center structure: https://proctorio.com/support (category descriptions; article bodies render client-side and were not readable)
- Honorlock — homepage and product menu: https://honorlock.com/
- Honorlock — Live Pop-In: https://honorlock.com/live-pop-in/
- Honorlock — Service Options: https://honorlock.com/services/
- Honorlock Help Center — root: https://honorlock.kb.help/
- Honorlock KB — How to Use Honorlock (Test Takers): https://honorlock.kb.help/how-to-use-honorlock-test-takers/
- Honorlock KB — How to Use Honorlock (Faculty and Exam Administrators): https://honorlock.kb.help/how-to-use-honorlock-faculty-and-exam-administrators/
- Respondus Monitor — product page: https://www.respondus.com/products/monitor/ (fetched via https://web.respondus.com/he/monitor/)

Tier 2 (product/marketing pages) used for positioning and feature confirmation; Tier 1 help-center articles used for operational flows wherever available.

Source-access limitations:

- Proctorio's help-center article bodies (reviewing-an-exam, taking-an-exam, etc.) returned empty content on fetch (client-side rendering). Proctorio operational claims rest on its homepage settings list, the Integrity solution page, and help-center category descriptions. Flagging/report mechanics for Proctorio are asserted only at "category description" strength.
- One ProctorU instructor-category URL 403'd on first form; succeeded on the retry form (no content lost).
- Honorlock's archived student guide redirected to the current test-taker guide (no content lost).
- No numeric limits, pricing figures, accuracy claims, or scale claims from vendor marketing are treated as operational facts in the final document.

---

## Product A — ProctorU / Meazure Learning

### Key observations (evidence layer A = directly observed on official pages)

**Product & positioning.** Portal page ("Take an Exam" at go.proctoru.com, Help Center, sign-up). Meazure Learning's remote proctoring page: "pioneered online proctoring at scale in 2008"; "first remote proctoring vendor to guarantee a professional proctor will review every exam session" (2021); "certified proctors review and validate every exam session... within 24 to 72 hours" (vendor claim — marketing strength, not operational fact). Human-centered posture: "Technology can't replace the context provided by humans."

**Service tiers (instructor documentation).** Distinct product lines documented separately: **Live+** (live proctor), **Review+** (recorded sessions with human review — "Session Review Glossary", "How to view Test Taker Video under 'View Media'"), **Record+** (automated; separate Chromebook getting-started track). Suggested test-taker instructions exist per tier and per client (Guardian Browser vs extension).

**Scheduling & administration.** Test-taker library sections: Scheduling ("How to Schedule, Reschedule, or Cancel an Exam", "How to Accept an Exam Invitation", "Scheduling an Exam Using Your Test Owner's Platform", extension for early/late exams), Equipment Requirements with an automated equipment-check tool, Getting Started per LMS workflow (Canvas/D2L/Blackboard/Moodle), Guardian Browser resources, **Test Center – In Person Testing Articles** (in-person proctored appointments — the vendor spans remote and test-center proctoring). Instructor side: term creation, user role permissions, exam accommodations added "directly to the system", hiding exams, max attempts, max no-shows, open invite links, single-user ("Bluebird") exam scheduling, session statuses explained, admin reports, test-taker survey data, custom incident notifications, API (Record+ V2), LTI 1.3, SAML, JWT integration guides.

**Exam-day flow (test-taker, "What to Expect on Exam Day" — the richest single artifact of this research).**

- Access: "My Sessions" page after login, or directly through the institution's platform (LMS). Exam Rules button shows "the exam's specific requirements and rules."
- Client: Guardian Browser (secure browser) for most exams; Guardian Extension for some; LMI applet or screen sharing connects the proctor.
- Pre-check sequence: quick tips → welcome screen (what to expect, allowed resources, accommodations) → device selection (camera, microphone, screen preview) → allowed exam resources/materials (may be asked to photograph notes or books) → accommodations list → **facial and ID photos** ("take a photo of your face and an approved form of ID") → **self-guided room scan** ("a series of photographs of your testing space... to validate that your testing area complies with your exam's rules") → exam lobby.
- Lobby: automated proctor → "Begin Exam" (timer starts on click). Live proctor → expected wait timer; proctor connects via chatbox. Proctor may repeat checks: additional ID, hold up materials/scratch paper, **temporarily take control of the device** to check background processes and close unpermitted applications, ear/wrist check, monitor check, camera pan of room and desk.
- Passwords: Guardian auto-inputs the exam password for most exams; for some, the proctor takes control to type it.
- During: chat with proctor or support at any time; "they are not allowed to provide any assistance with the subject matter or content of your exam"; live proctor "will not interrupt you unless they notice" a disallowed action; breaks must be announced; leaving camera field of view may require re-securing the room with a quick scan.
- Submit: automated — click submit; live — message proctor first, proctor may ask to show notes or erase whiteboard, then ends the session.
- After: optional survey. **"Keep in mind, neither Meazure Learning nor the ProctorU Platform have access to the results of your exam. To find your exam results, you will need to contact your institution or test provider."** — direct official statement of the Type's structural boundary.

## Product B — Proctorio

### Key observations (layer A for homepage/integrity pages; layer B for help-center category structure)

**Product & positioning.** "The learning integrity platform that verifies identity, protects exam content, and confirms original work at any scale." Three suites: **Integrity** (proctoring + identity verification), **Origin** (authorship: Behavior Tracker, AuthorProof — AI-era extensions), **Vault** (content protection: WebSweep leak tracking, ScreenBlock). Since 2013; "300M+ exams proctored" (marketing, not used). Sectors: K-12, higher ed, workforce, credentialing. Also **Secure Interviews** — the same machinery applied to securing interviews/presentations. Governance posture: "Institutions decide how AI is used. Proctorio provides configurable tools and insights, and every decision stays with the institution."

**Settings list (homepage — a configuration taxonomy of the Type).** Record Video / Record Desk / Record Audio / Record Web Traffic; Verify ID / Verify Signature / Verify Audio / Verify Video; Live Proctor; lockdown: Block New Tabs, Block Download, Clear Cache, Close Existing Tabs, Disable Clipboard / Extensions / Printing / Right Click, Force Full Screen, In-Quiz Links Only, Only allowed external platform; Allow Screen Readers, Mobile Access, Multiple Monitors, Allow Breaks, Allow Reentry (+ With Agent / Blocked); calculators (graphing/scientific/standard); whiteboard; VM/program detection; desk scan at start / periodic. The list shows: observation channels are individually toggleable; lockdown is a separate, optional family; monitoring may be fully automated or paired with a live proctor.

**Integrity page — the four-step value chain.** (1) **Verify identity**: "Live ID check leverages document validation and image matching to authenticate identity before granting entry to an assessment. Or, validate manually with post-exam review." (2) **Prevent unauthorized access**: lockdown suite, explicitly optional — "Don't want to lock things down? No problem. Use minimal (or no) blocking tools and let the monitoring tools... detect and flag." (3) **Monitor session interaction**: "Automate monitoring for flexible assessment windows, review sessions asynchronously, or use **Be Your Own Proctor®** to have your own staff oversee exams in real time. Customize monitoring with any combination of webcam, screen sharing, audio, and web traffic, with adjustable flagging." (4) **Analyze results**: "adjustable flagging and analytical tools to zero in on incidents that need your judgment... annotate results for later action."

**Help-center category structure (names + descriptions only).** Creating an Exam ("Enable Proctorio and configure exam settings"); Getting Started; Live Exams ("Set up and manage live proctoring sessions... monitoring, communicating, and supporting test-takers"); Preparing for an Exam; Taking an Exam ("what to expect before, during, and after"); Reviewing an Exam ("Access exam results and use built-in tools to review, interpret, and document proctoring data"); Organization Resources; Troubleshooting. The category set mirrors the session lifecycle: create → prepare → take → review.

## Product C — Honorlock

### Key observations (layer A)

**Product & positioning.** "Combines AI-powered monitoring with real human review to protect fair testing while treating students and candidates with empathy and respect." Flag reframing: "In traditional proctoring, a flag means 'Gotcha.' At Honorlock, a flag means 'Let's Help.'" Integrates "directly into Canvas, Blackboard, Brightspace, and Moodle for a familiar, low-stress testing experience." Serves higher ed and corporate/certification.

**Live Pop-In page — the hybrid philosophy, stated against both alternatives.** "Why traditional remote proctoring fails": Fully Automated AI → "generates endless false flags... that your team wastes hours reviewing"; Legacy Live Proctoring → "forces one human to watch 12 screens at once, making it easy to miss actual misconduct." Honorlock's model: (1) AI Monitoring — "multi-layered AI monitors video, audio, and desktop activity while blocking secondary devices, unauthorized AI tools, and proxy testing"; (2) Human Review — "instead of instantly interrupting the session, a trained proctor reviews the flag in real-time to filter out low-value noise and account for approved accommodations"; (3) Live Pop-In — "for high-stakes violations, the proctor enters the session via 1:1 chat to resolve the issue." No scheduling: "24/7/365 access... test-takers never have to plan an exam around a proctor's calendar." Accessibility rationale: "Human review ensures disability-related movements or approved accommodations aren't mistaken for cheating." Admin value: "time-stamped reports that point directly to verified incidents."

**Test-taker flow (KB article — layer A).** LMS course navigation → Honorlock → Launch next to the exam → agree to Terms + Exam Taker Privacy Notice → System Check → Begin Authentication (in a small proctoring window): BrowserGuard (if enabled) prompts closing disallowed tabs; after Continue, "you will not be able to access any other applications or resources. Any attempts to do so will be flagged for review"; **photo + ID verification** (with failure fallbacks: QR-code upload, image from computer); microphone check; **room scan** ("show your entire workspace, including desk area, surrounding areas, scratch paper, or additional resources... allowed"; review and re-record option); screen-recording permission grant; Focus Test Window; Start Assessment — **the exam itself opens in the LMS**; Honorlock wraps it.

**Service options (Services page — layer A).** (1) **AI + Live Pop-In** (the flagship hybrid). (2) **Bring Your Own Proctor (BYOP)** — "your team proctor[s] exams using Honorlock's software," supported by the AI ("monitors exam sessions in real time and flags suspicious activity"), with "our intuitive proctoring dashboard" for managing multiple sessions, "centralized and decentralized proctoring setups." (3) **Add-on: Record & Review** — "highly trained exam proctors manually review every minute of selected exam sessions... verify, add, and remove flags as appropriate... A comprehensive... report is sent to your faculty or administrators... in-depth audit trail."

**Feature set across options (layer A, marketing strength).** Cell phone detection (incl. smartwatches — "patented"), AI tool detection/blocking, Search & Destroy (web leak scanning + takedown — content protection beyond supervision), identity verification, BrowserGuard (blocks sites/apps/shortcuts), Smart Speech Detection ("flags only suspicious voice commands like 'Hey Siri'"), desktop recording, control applications, Complete View (side/second camera), Analytics Hub.

**Faculty/admin surface.** Per-LMS guides (Canvas, Blackboard/Ultra, D2L Brightspace, Moodle, Coursera, Intellum); **Universal Exams** (proctoring for exams NOT inside the LMS — third-party exams); "How to use Honorlock in a Test Center"; templated proctoring policy and suggested syllabus verbiage; Analytics Hub; release notes. Exam support is a prominent nav item (chat-based).

## Product D — Respondus (LockDown Browser + Respondus Monitor)

### Key observations (layer A for the product page)

**Product structure — the lockdown lineage.** Respondus Monitor "builds upon LockDown Browser": LockDown Browser is "a custom browser that locks down the testing environment within a learning system. Students cannot print, copy, access other applications, or search the internet during an online exam." Monitor adds: "a fully automated proctoring solution. Students use a webcam to record themselves during an online exam. Afterward, flagged events and proctoring results are available to the instructor for further review." — This two-layer structure is itself evidence that environment lockdown and observation are separable; observation is what makes it proctoring.

**Delivery posture.** "Auto-launches from any browser" after one-time installation; "students are then guided through a pre-exam sequence, including a webcam check." Integrates with LMSs (Canvas, Blackboard, Moodle, Brightspace, Schoology) **and publisher courseware** (Pearson MyLab/Mastering, McGraw Hill ALEKS, Cengage WebAssign, Hawkes). "No scheduling or registration" — no advance scheduling; no separate site registration. Native apps for Windows, Mac, Chromebook, iPad ("not just a browser extension").

**Flexibility framing.** "One technology, lots of flexibility": settings select the exam environment — Remote, Asynchronous, Synchronous, Hybrid, Classroom, In Person, Testing Center, "All of the Above." **Instructor Live Proctoring**: an option where the instructor proctors via Zoom/Microsoft Teams/Google Meet "and other video systems" — the institution's own instructor as the live proctor, using Respondus tooling.

**Review & fairness posture.** "Flagged events and proctoring results are available to the instructor for further review." Newer features: "sensitivity levels, increased precision with flagging, faster proctoring results, greater support for low bandwidth settings." "Respondus Monitor's algorithms are systematically tested for fairness to ensure that age, gender and skin tone don't impact proctoring results." 24/7 live chat support for students. Scale claims (1,500 universities, "over a billion minutes") are marketing — not used.

---

## Cross-product Comparison

| Dimension | ProctorU/Meazure | Proctorio | Honorlock | Respondus Monitor |
|---|---|---|---|---|
| Owns exam content/scoring/results? | No — states it explicitly | No — wraps LMS exams | No — exam opens in LMS | No — exam runs in LMS/publisher courseware |
| Identity verification | Face + ID photos in pre-check (live tier: proctor re-checks) | Verify ID setting; live ID check (doc validation + image match) or manual post-exam review | Photo + ID verification, fallback upload paths | Pre-exam sequence incl. webcam check (ID check not asserted in captured material) |
| Environment scan | Self-guided room scan (photos); proctor-guided pan | Record Desk / desk scan settings | Room scan video, re-recordable | (webcam check; workspace monitoring via webcam) |
| Observation channels | Camera, screen, audio (via Guardian/LMI) | Webcam, screen sharing, audio, web traffic (toggleable) | Video, audio, desktop activity; optional second camera | Webcam (+ screen via lockdown environment) |
| Lockdown layer | Guardian Browser/Extension | Optional lockdown family, explicitly skippable | BrowserGuard | LockDown Browser (the base product) |
| Supervision modes | Live+ (human), Review+ (record+human review), Record+ (automated) | Automated (default), Live Proctor, BYOP (own staff real-time) | AI + Live Pop-In, BYOP, Record & Review add-on | Fully automated; Instructor Live Proctoring via videoconference |
| Scheduling | Appointment-based for live tiers; reschedule/cancel flows | Not appointment-based (flexible windows) | "No scheduling required," 24/7/365 | "No scheduling or registration" |
| Flags → who decides | Certified proctors review (per tier); institution scores/decides; platform "no access to results" | Adjustable flagging; "every decision stays with the institution" | AI flags → proctor filters in real time → instructor reports; Record & Review verifies flags | Flagged events → instructor for further review |
| Integration | Vendor portal + LMS (LTI), API/SAML/JWT | LMS-embedded (settings inside LMS exam) | LMS-embedded; Universal Exams for non-LMS | LMS + publisher courseware; auto-launch |
| Test-taker support | Proctor chat + support team; equipment check tool; survey | 24/7/365 chat | 24/7 chat ("Exam Support"); exam prep guidance | 24/7 live chat; training for instructors |
| Accommodations | Accommodations added to system; shown in pre-check | Allow Screen Readers; configurable allowances | Human review "accounts for approved accommodations" | Sensitivity levels; (accommodation paths documented in their help center — not captured) |
| Stretched uses | Test-center in-person proctoring (same vendor) | Secure Interviews | Universal/third-party exams; test centers | Classroom/testing-center scenarios |

### B-layer findings (cross-product commonality, observed across the sample)

1. **The session wraps delivery the platform does not own.** All four products supervise an exam that runs in an LMS, publisher courseware, exam platform, or third-party site. None authors items or scores. ProctorU states the results boundary verbatim.
2. **A bounded pre-exam authentication/check-in sequence** inside the proctoring layer: device/permission checks → identity confirmation (photo/ID; face/ID capture) → workspace/environment scan → rules and allowed materials displayed → accommodations surfaced.
3. **Observation channels are configurable and channel-wise combinable**: camera, screen, audio, desk; live and/or recorded.
4. **A lockdown/environment-control layer is a common companion but explicitly optional** (Proctorio says it outright; Honorlock/Respondus/ProctorU ship lockdown as a sibling capability).
5. **Automated detection produces flags; humans decide.** Every product's review loop ends at a human (instructor, proctor, administrator) and every product frames the flag as evidence for review. Vendor-marketed differences are about WHO reviews and WHEN (real-time pop-in vs post-hoc instructor review vs guaranteed human verification of every recording) — not about whether the platform adjudicates.
6. **The reviewable record**: session video, time-stamped flagged events, incident annotations — delivered back to the institution (usually surfaced inside the LMS).
7. **Support is a structural surface**, not an afterthought: 24/7 chat, equipment check tools, exam-day guidance, syllabus/policy templates for instructors.
8. **Accommodations are handled as a named concern inside the flow**, typically via human review and configurable allowances.
9. **False-positive management is a first-class product concern** (sensitivity settings, flag filtering, human verification layers, fairness testing claims).

### C-layer canonical inference

The Type can be modeled as: **a supervised test-taking session, bound to an identified test-taker, observed through networked audio/video/screen capture (live and/or recorded, human and/or automated), producing an integrity record that the institution — not the platform — reviews and acts on, around an assessment the platform does not own.**

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (smallest stable structure)

1. **The supervised session of record.** A bounded sitting in which an identified test-taker completes an assessment, with the session bound to that taker in the institution's context. Remove → scheduling tool or video call.
2. **Networked observation of the test-taking.** The taker's person and/or workspace/screen is observed during the assessment — camera, screen, and/or audio; live, recorded, or both; by human proctors and/or automated monitoring. Remove → mere exam-delivery access control (lockdown-only browser tooling) or an unobserved session.
3. **Integrity evidence for human judgment.** The session leaves a reviewable record (flags/incidents, recording, report) delivered to the institution, which — not the platform — reviews and decides. Remove → surveillance footage with no institutional loop, or an auto-verdict bot (no product in the sample is that).

Jointly-held is load-bearing: 1 alone = an appointment/booked exam slot; 2 alone = a webcam/screen platform; 3 alone = an audit log; 1+2 without 3 = a live stream; 1+3 without 2 = an attendance register; 2+3 without 1 = generic surveillance.

The structural separateness from exam delivery is part of the definition's boundary: the assessment itself is delivered by an LMS, examination platform, publisher courseware, or third-party site. (ProctorU states it has no access to results; all four sampled products wrap foreign delivery.) This is what keeps the Type distinct from Examination Platform even though exam platforms integrate proctoring modules.

**Historical / market-sample check (§24):** The 2008–2013 first-generation remote proctoring model — a live human proctor connecting over webcam, checking ID, watching, recording incidents — satisfies all three invariants with no AI, no extensions, no LMS integration. Respondus LockDown Browser alone (lockdown without observation) does NOT satisfy invariant 2 and is correctly positioned by its own vendor as the base layer that Monitor "builds upon" to become proctoring. In-person test-center proctoring (offered by ProctorU and Honorlock as modes) satisfies the structure with the "networked" qualifier dropped — it is the same supervision structure realized at a test center; the "Online" in the Type name marks the remote realization as the center. The definition names no AI, no specific client form, no scheduling model, no sector — all era/segment machinery.

### L1 — Common Mature Structure (very common, not definitional)

- Identity verification mechanics (government ID photo, face capture/matching; automated pre-exam or manual post-exam)
- Workspace/room/desk scan (self-guided photo/video or proctor-guided)
- Pre-exam system/equipment check and permission grants (camera, mic, screen recording)
- Display of exam rules, allowed materials, accommodations inside the check-in flow
- Lockdown / environment-control companion layer (secure browser, extension, or in-page blocking)
- Real-time chat/support channel with the proctor or vendor support; equipment troubleshooting
- Time-stamped flag/incident records and session recording playback for reviewers
- LMS embedding (LTI-style launch, settings inside the LMS exam) and/or vendor portal
- Human-review workflow over flags (instructor review surfaces; proctor verification passes)
- 24/7 support posture; test-taker preparation guidance (what to expect, best practices)

### L2 — Variant / Optional Structure

- Supervision-mode spectrum: continuous live proctoring / record-then-human-review / fully automated / AI+human hybrid pop-in / institution's own proctors on vendor software (BYOP) / instructor proctoring via videoconference
- Scheduling model: appointment-based (booking, reschedule, no-show limits) vs on-demand no-scheduling
- Client form: secure browser app vs browser extension vs native app vs in-page
- Setting: remote vs test-center/in-person mode (same vendors offering both)
- Sector packaging: higher ed, K-12, certification/licensure, workforce/hiring, government
- Extra observation hardware: second/side camera, phone detection, smartwatch detection
- AI-era add-ons: unauthorized AI-tool detection/blocking; web content-leak scanning and takedown; authorship/AI-writing verification (note: spreading fast, present in 2/4 sampled products as product lines)
- Adjacent stretches of the same machinery: securing interviews/presentations; universal/third-party exams outside the LMS

### L3 — Vendor-specific (kept out of the final document)

- ProctorU/Meazure: Guardian Browser, Guardian Extension, LMI applet, Live+/Review+/Record+ tier names, Bluebird single-user exams, open invite links, max no-show/max attempts controls, custom incident notifications, 24–72h review turnaround claim, "pioneer since 2008" and "review every session" guarantees, global office network, proctor training/secret-shopper programs
- Proctorio: suite names (Integrity/Origin/Vault), AuthorProof, Behavior Tracker, WebSweep, ScreenBlock, Be Your Own Proctor®, the homepage settings taxonomy as a whole, 300M+ claim
- Honorlock: Live Pop-In™, BrowserGuard™, Search & Destroy™, Smart Speech Detection, Complete View, Analytics Hub™, "flag means Let's Help" positioning, 500+ organizations claim, flat-rate pricing model
- Respondus: LockDown Browser product lineage, publisher courseware integrations list, licensing tiers/per-exam pricing model, "1,500 universities / billion minutes" claims, algorithm-fairness testing program
- Meazure company scope beyond proctoring: test development, item writing, psychometrics, scoring, data forensics (belongs to assessment-services territory, not this Type)

## Rejected Findings (considered and NOT promoted)

- **"AI monitoring" as definitional.** Rejected: first-generation live proctoring (still sold as Live+) satisfies the Type with no AI. AI is the current-era detection layer, not the invariant.
- **"Lockdown/browser control" as definitional.** Rejected: Proctorio explicitly sells monitoring without lockdown; lockdown-only tools are exam-security capabilities, and Respondus itself treats LockDown Browser as the base that Monitor "builds upon."
- **"Scheduling/appointments" as definitional.** Rejected: three of four products are explicitly no-scheduling; appointment scheduling is the live-service tier's variant.
- **"LMS extension" as definitional.** Rejected: ProctorU's portal model and Honorlock's Universal Exams both proctor exams outside any LMS.
- **"Automatic verdicts / auto-fail" as a behavior.** Rejected: no sampled product documents automatic adjudication; all frame flags as review inputs. (If some product auto-fails somewhere, it was not observed — assertion not made.)
- **"Student-only audience."** Rejected: certification candidates, workforce candidates, and interviewees are served by the same machinery (Honorlock corporate/certification, Proctorio workforce/credentialing/interviews). "Test-taker" is the neutral term.

## Boundary Findings

| Neighbor | Test | Result |
|---|---|---|
| **Examination Platform** | Remove exam ownership (occasion, roster, scoring, official results) from an examination platform → still an examination platform? No — it becomes proctoring. Remove supervision from a proctoring platform → still proctoring? Yes. | Clean split. The proctoring platform has no exam occasion of record and (per ProctorU's own statement) no access to results. Exam platforms integrate proctoring as a module; standalone proctoring is this Type. |
| **Assessment Platform** | Remove items/scoring/results → proctoring retains its whole product (supervision); remove supervision → assessment remains. | Clean. Confirms the assessment pass's "add-on in high-stakes contexts" framing. |
| **Academic Integrity / Plagiarism Platform** | Live observation of the exam-taking process vs post-hoc analysis of submitted artifacts. | Clean split (matches the sibling pass's recorded finding: "remove live session surveillance and this Type remains intact; remove artifact analysis and proctoring remains"). |
| **Virtual Classroom / Video Conferencing** | Same media (webcam, chat), different product: no instruction, no meeting; the session's output is an integrity record, and the session is bound to an assessment. | Clean by purpose and record type. |
| **Identity Verification / KYC** | ID verification is one step inside the check-in sequence, in service of session trust — not a standalone identity-assurance product with its own case/risk lifecycle. | Clean: identity verification is L1 machinery here, not the product. |
| **Video Interview / Hiring assessment platforms** | Proctorio's "Secure Interviews" shows the machinery stretched to interviews; but interview platforms center the conversation as the evaluated interaction. Proctoring observes someone else's evaluation. | Gradient at the stretch, clean at the core. |
| **Lockdown-browser-only tools** | Environment control without observation fails L0 leg 2. | Clean: lockdown is a companion capability (often bundled), not the Type. |

Dual-realization note (for taxonomy consistency): the same supervision capability exists BOTH as standalone products (this Type) AND as modules inside examination platforms (documented in the examination/assessment passes). Both realizations share the L0; the leaf documents the standalone form, and the module form is a packaging of the same capability.

## Uncertainties

- Proctorio's end-user review/report mechanics (exact reviewer tools, flag taxonomy) could not be verified beyond category descriptions and product pages (help-center articles render empty). Assertions about Proctorio review mechanics are held at feature-list strength.
- Respondus Monitor's ID-verification depth: the captured product page does not state ID checks; Monitor's help center (not fetched) likely documents an optional startup sequence with ID verification. The final document therefore treats identity verification as common across the sample but does not claim it for every product's default flow.
- Whether any sampled product offers hard auto-termination or auto-fail was not observed; the document claims only "flags are evidence for human review" — a safe, sample-supported claim.
- Regional (e.g., GDPR-first European proctoring vendors) and government-specific postures were not sampled; privacy/regulatory framing is documented only where the sampled vendors themselves state it (SOC 2/privacy pages exist but their contents were not researched in depth).
- Examity and other live-proctoring service providers were not fetched; their expected fit is the live/record-review variant, but this rests on the market shape, not direct evidence — noted, not asserted in the final document.

## Final Synthesis

An Online Proctoring Platform is the supervision layer of remote assessment: it binds a test-taking session to an identified test-taker, verifies and prepares the taker and their environment before the assessment (identity, workspace, rules, accommodations), observes the session through networked camera/screen/audio capture — live, recorded, or both, by human proctors and/or automated detection — and delivers the resulting integrity record (time-stamped flags, recordings, reports) to the institution, whose people, not the platform, review the evidence and decide outcomes. It wraps an assessment that an LMS, examination platform, publisher courseware, or third-party site delivers, and holds neither the exam's content nor its results. The market varies the supervision mode (live human / record-review / automated AI / hybrid pop-in / institution's own proctors), the scheduling model, the client form, and the setting (remote or test center) — all realizations of one session structure.
