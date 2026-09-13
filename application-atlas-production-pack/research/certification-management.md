# Research Notes — Certification Management

## Research Goal

Understand what "Certification Management" software (directory §25, Nonprofit/Membership context) actually is and does: what a certification program looks like when run on software, what objects and lifecycles the system manages, who uses it, and how it differs from adjacent Types (accreditation management, continuing education management, LMS, AMS, digital credential platforms, government licensing).

This pass must also resolve or update two prior joint-review flags recorded in STATUS.md:

1. `accreditation-certification-management` (§11) predicted that §25 `certification-management` manages certifications issued **to people** (certificants, CEU/renewal tracking, member credentials) — "probable distinct Types sharing vocabulary."
2. `accreditation-management` (§25) flagged a "probable near-duplicate pairing" with `certification-management` — same intake→review→decision→credential machinery, different credential population (organizations vs individuals); OpenWater reportedly runs both from one codebase.

## Initial Boundary

Working hypothesis before research:

- Core use: a certifying body (professional association, certification board, standards body) operates a credential program for **individuals**: candidates apply, prove eligibility, pass an exam or review, are granted a certification, and must maintain it (renewal, continuing education) over time.
- Users: certification staff at the body; candidates/certificants (self-service); reviewers/auditors; possibly the public/employers (verification).
- Nearest neighbors: Accreditation Management (§25 sibling, organizations), Continuing Education Management (§25 sibling), Accreditation/Certification Management (§11, org's own compliance), Corporate LMS (§09), AMS/Membership Management (§25), Digital Credential Platform (§23), Government Licensing Management (§24), Assessment/Exam platforms.
- Unknowns: How central is exam management vs outsourced to test-delivery vendors? How central is CE tracking vs delegated to CE platforms? Are public registries/verification a standard capability? Does renewal/re-qualification belong in the definition or is it merely common?

## Research Questions

1. What objects make up a certification program in software (program, application, eligibility path, exam, credential, renewal cycle, CE activity)?
2. What is the full lifecycle of a certificant: application → eligibility → exam/review → grant → maintenance → renewal/lapse/revocation?
3. How are program rules (eligibility criteria, CE requirements, category minimums/caps) encoded?
4. How does the exam fit — in-platform or integrated with external test-delivery vendors?
5. What role does continuing education play, and how do approved CE providers interact with the system?
6. How do audits of applications/CE work?
7. What are the self-service surfaces for candidates/certificants vs staff consoles?
8. How does the system integrate with AMS/membership systems?
9. What machinery separates certification management from (a) an LMS, (b) a CE-compliance platform, (c) an application/review platform, (d) accreditation management?
10. Would older/regional/platform-native certification programs (paper-roster era bodies, government licensure boards, no-renewal certifications) still fit the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different deployment postures:

| Product | Vendor | Posture | Why selected |
|---|---|---|---|
| LearningBuilder | Heuristic Solutions | Purpose-built certification / recertification / CE management platform | Deepest documentation of the category; defines itself against AMS/LMS; covers eligibility, exams, CE, recertification, audits, licensure variant |
| TopClass | WBT Systems | Association LMS with a dedicated Certification solution | Different philosophy: learning-first platform carrying credential lifecycle; shows convergence boundary with LMS |
| OpenWater | ASI (Advanced Solutions International) | General application/review platform (accreditation offering documented by sibling pass) | Generalist intake/review/decision machinery; key to resolving the near-duplicate flag |
| EthosCE | Cadmium | Healthcare CE LMS (boundary sample) | Pure CE/credit-tracking pole — demonstrates what certification management is NOT |

Attempted but unreachable (recorded, not substituted from memory):

- **Certemy** — 403 on root and subpage (×2) — abandoned.
- **CE Broker** — 403 on root and /cb/ subpage (×2) — abandoned.
- **iMIS** — 403 on root — abandoned (AMS-embedded variant evidenced indirectly via LearningBuilder/TopClass integration pages instead).

## Sources

Research date: **2026-09-06**. All observations below from official vendor pages/documentation unless noted.

- LearningBuilder (Heuristic Solutions) — https://www.heuristics.net/ ; LearningBuilder home https://www.heuristics.net/learningbuilder/ ; Certification Management https://www.heuristics.net/certification-management/ ; Recertification https://www.heuristics.net/recertification-management-software/ ; Auditing https://www.heuristics.net/flexible-auditing-for-certification-programs/ ; nav references to CE Management, License Management, Accreditation Management, Portfolio Review, Certificate Printing, Employer Voucher Program
- TopClass (WBT Systems) — https://www.wbtsystems.com/ → https://topclasslms.com/ ; Certification https://topclasslms.com/certification ; platform/features pages
- OpenWater — https://openwater.com/ ; Help Center https://help.getopenwater.com/ (collection structure inspected); accreditation offering (cross-referenced from research/accreditation-management.md, researched 2026-09-06)
- EthosCE (Cadmium) — https://www.ethosce.com/ ; platform and FAQ pages

Cross-reference: research/accreditation-management.md and applications/accreditation-management.md (OpenWater accreditation offering, accreditor-side machinery); applications/accreditation-certification-management.md (org-compliance-side machinery).

## Product A — LearningBuilder (Heuristic Solutions)

Evidence tier: A (directly observed on official product pages; multiple pages).

Key observations:

- **Category self-definition (vendor FAQ, quotable structure):** "Certification management software runs the full lifecycle of a professional certification: applications, eligibility, exams, continuing education, and recertification." And: "At minimum: configurable eligibility and application workflows, integration with test-delivery vendors, CE and recertification tracking, automated reminders and notifications, and reporting your staff can build without code. Programs with complex rules should also look for a rules engine that can encode handbook requirements directly."
- **Boundary vs AMS (vendor FAQ):** "An AMS is built to manage membership: dues, events, engagement, and member records. Certification management software is built to manage a credentialing program: eligibility rules, application review, exam coordination, CE requirements, and recertification cycles. Many organizations run both, integrated, with the AMS as the system of record for members and the certification platform running the credential workflows."
- **Candidate journey:** interactive candidate dashboard — applicants check progress, complete applications, update information without staff intervention; uploads replace physical files; "Once your candidates are certified, LearningBuilder opens a recertification application so that you can engage them in the renewal process."
- **Eligibility encoding:** "highly configurable Workflow Editor and Visual Rules Engine"; supports "multiple eligibility paths" (a certification can be reachable via different qualification routes); blog framing "Rules that Rule: From Candidate Handbook to Certification Management Platform" — the program handbook becomes system rules.
- **Exams:** "We handle both complex eligibility paths and simple exam registrations. We integrate with the major test delivery platforms." "Once a candidate is authorized to test, LearningBuilder integrates with the leading test vendors to make scheduling exams easy. After an exam, LearningBuilder accepts the exam results electronically and either begins the conferral process next steps if passing, or otherwise provides options to re-test." → exam delivery is external; the platform handles authorization-to-test, result ingestion, and pass/fail branching.
- **Recertification (dedicated page):** "Recertification management software automates certification renewal: tracking continuing education, sending reminders, and processing renewal applications. With LearningBuilder, a recertification application opens automatically once someone is certified, and the system handles everything from a simple CE log to variable MOC programs, including grace periods and lapsed statuses."
- **Recertification application:** checklist-style; "requirements may include maintaining a valid license, work history, volunteer commitments, or educational activity"; sections completed independently; "As tasks are fulfilled, practitioners (or their education providers) can add them to their application."
- **CE tracking depth gradient:** "from a basic CE tracking log to tracking specific CE categories with minimums and limits. We can even handle more involved continuing education management, helping you engage educators through approved provider networks and courses." Practitioners upload proof of attendance themselves or approved CE providers upload attendance records digitally, so "certificants' eligible CE automatically counts towards their required activities."
- **Auditing (dedicated page):** "Every certification management system, no matter the industry, must be able to conduct audits of both initial and recertification applications. Some organizations audit all submitted applications, and some conduct a random audit on select submissions." Machinery: define audit rules, random selection ("randomly select applications for audit and automatically assign them to pre-determined, anonymous reviewers"), documentation requests fulfilled in-platform (by applicant or third party), outcomes tracked; auto-flagging per rules.
- **Cycle management:** "handle grace periods and extended reporting timelines, manage lapsed statuses, and track interim milestones."
- **Beyond the core (optional modules):** low-stakes assessments with "test out" of recertification requirements; portfolio review; eLearning; reflective practice; employer voucher programs; certificate printing; automated email/SMS communications; reporting module.
- **Program-family breadth (same platform):** certification, recertification, license management for regulatory agencies ("applications, renewals, CE management, and complaints and investigations"), CE management, accreditation management, workforce competency development.

## Product B — TopClass (WBT Systems)

Evidence tier: A (official certification solution page; product positioning pages).

Key observations:

- Positioning: association LMS first ("The Best Association LMS for Educating Members"), with "Manage Certification" as one of three headline pillars: "Track and manage competencies and rules for certification, all types of continuing education (CE) credits, and Maintenance of Certification (MOC)."
- **Certification lifecycle & paths:** "Configure professional certificates, credentials, and micro-credentials with flexible paths that include required or elective courses, exams, external training, and professional experience, while tracking competencies and CE credits, including MOC pathways. Set lifecycle rules for certification expiry, renewals, notifications, and enforce soft or hard stops when credentials lapse."
- **CE & credit tracking:** "Support all types of CE credits, tracking those earned through courses, events, and external activities, with certification tracks tied to CE requirements and MOC rules"; automated reminders and expiration notifications; learners upload evidence of professional experience/external training.
- **Reporting:** dashboards for "certification status, CE progress, test performance, and completion metrics" plus audit logs.
- **Assessment:** timed quizzes, randomized question pools, proctoring-tool integrations; admin overrides (extra time, attempts) — in-platform testing (contrast with LearningBuilder's external-vendor posture).
- **Credential issuance:** branded certificates, digital badges, micro-credentials; badge-platform integration with metadata-rich sharing (LinkedIn).
- **Learner self-service:** learner dashboard — view certifications, enroll, track progress, purchase; "access self-service tools to review history, meet renewal requirements, and earn badges."
- **Integrations:** two-way AMS/CRM sync (iMIS, Salesforce, Personify, NetForum, Wicket), SSO, real-time sync of certification completions and purchases; e-commerce for program fees.
- FAQ confirms: lifecycle rules for expiry/renewals/notifications; soft/hard stops on lapse; MOC + external credits; automated expiration notifications; digital badging.

## Product C — OpenWater (ASI)

Evidence tier: A (official site + help-center structure); corroborated by sibling pass (research/accreditation-management.md).

Key observations:

- Current platform menu: Abstracts, Awards, Speakers, Grants, Fellowships, Scholarships, Applications, Conferences, Competitions, **Accreditation**. **No dedicated certification page in the current site navigation** (a /certification-management-software URL resolves to the homepage).
- Help-center collection structure (full listing inspected): Getting Started, Setup your submission form, Accept payments, Setup your judging portal, Configure your public website, Manage submissions and applicants, Manage judges, View the results of judging, Public gallery and voting, Export data, Build and schedule conference sessions, Integrations, API, Roll-up competitions, Import data, Third-party add-ons. **No CE, recertification, credential-lifecycle, or audit collections.**
- Sibling pass (accreditation-management, 2026-09-06) documented the accreditation offering: intake → multi-stage review → decisions → credentialing → payments → renewal, integrated with AMS — i.e., the same submission/review machinery configured for a credential program over **organizations**.
- Interpretation (my inference, marked as such): OpenWater's machinery covers the front half of a credential program (application, review, decision, status) but the observed help center shows no person-bound maintenance machinery (CE logs, recertification cycles, lapse handling, audits). This supports treating "general application/review platform configured for credential programs" as a variant posture of the front half, with purpose-built maintenance machinery as the differentiating back half.

## Product D — EthosCE (Cadmium) — boundary sample

Evidence tier: A (official pages/FAQ).

Key observations:

- Positioning: healthcare CE LMS ("LMS healthcare professionals trust to simplify continuing education"). "Manage all your CE activities in one place."
- Core objects: courses/course library, learning groups, enrollments, certificates of completion, CME credit tracking, accreditation **of the education provider** (ACCME-style) and reporting to accreditation bodies: "accreditation and reporting automation that integrates with major healthcare accreditation boards and systems, such as ACCME PARS, JA PARS, CPE Monitor, and CE Broker."
- FAQ explicitly ties CE to maintaining certifications ("Automated CME credit tracking: when professionals need a certain number of continuing education credits to maintain certifications… you can set up a system to track that and send reminders about when certificate renewal dates are approaching") — but the tracked objects are learning activities and credits, not the credential lifecycle itself.
- No observed machinery for: eligibility-gated applications, certification grants, renewal/lapse states of a credential, CE audits of certificants, revocation.
- Confirms the seam: CE-LMS = learning delivery + credit capture + provider-accreditation reporting; certification management = credential lifecycle over persons. The two integrate (CE Broker as a reporting destination, badge platforms, etc.).

## Cross-product Comparison

| Dimension | LearningBuilder | TopClass | OpenWater | EthosCE |
|---|---|---|---|---|
| Managed population | Individual candidates/certificants | Individual learners/certificants | Program applicants (organizations in accreditation posture; general applicants) | Learners earning CE credit |
| Program container | Certification program(s), configurable | Certification tracks/paths in an LMS | Configured program (accreditation posture documented) | Course catalog + CE program |
| Eligibility gating | Yes — multiple eligibility paths, rules engine | Yes — paths incl. external training/experience | Yes — application forms + eligibility/review stages | No (observed) |
| Application review | Yes — admin queues, checklist applications | Lighter (paths + evidence upload) | Yes — the platform's core (judging portal, rounds) | No |
| Exam handling | Authorize-to-test → external test-delivery vendors → results ingestion → conferral/re-test | In-platform assessments + proctoring integrations | Not credential-specific (review forms generally) | Quiz-level only |
| Grant/credential record | Yes — certification record, conferral process | Yes — credential with expiry | Decision/status recorded | Certificate of completion only |
| Standing state (active/lapse/renew) | Yes — grace periods, extended timelines, lapsed statuses, interim milestones | Yes — expiry, renewal automation, soft/hard stops on lapse | Renewal cycles (accreditation posture) but no observed lapse/person-state machinery | No |
| CE tracking | Yes — CE log → categories with minimums/limits → approved-provider auto-credit | Yes — all CE types, internal + external, tied to requirements | No | Yes — but as the primary object (credit capture) |
| CE/MOC | Yes — incl. "variable MOC programs" | Yes — MOC pathways explicit | No | CME credit tracking only |
| Audits of certificants | Yes — random/all selection, anonymous reviewers, in-platform documentation | Audit logs mentioned; selection machinery not observed | No | No |
| Credential artifacts | Certificate printing; (badges not observed on fetched pages) | Certificates, digital badges, micro-credentials | Decision letters/status | Completion certificates |
| Self-service portal | Candidate dashboard, checklist applications | Learner dashboard, renewal tools | Applicant portal | Learner portal |
| AMS integration | Yes — positioned as integrated with AMS as member system of record | Yes — two-way iMIS/Salesforce/Personify/NetForum | Yes — iMIS bridge, 65+ integrations | AMS integration for healthcare associations |
| Fees/payments | Yes (fees mentioned across pages) | E-commerce for program fees | Yes — submission fees | Course sales |

Cross-product synthesis (evidence layers):

- **B (cross-product commonality):** person-bound credential as a managed record with a lifecycle; eligibility-gated application; self-service portal; automated reminders; AMS integration; renewal cycle machinery (in purpose-built and LMS-embedded products).
- **A→B gradient:** exam coordination (LearningBuilder external-vendor vs TopClass in-platform — mechanism differs, both "assessment outcome feeds grant decision"); CE tracking depth (log → categories → provider networks).
- **C (canonical inference):** the Type is the credential program as a system of record over persons — the program defines requirements, the system gates entry, records the grant, and maintains the credential's standing state; CE, exams, audits, artifacts, and integrations exist to make that lifecycle operable.

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant (minimal)

1. **Certification program operated by a certifying body** — a named container that defines a credential: who may earn it and what must be done to earn and keep it. Remove → generic records/membership.
2. **Individuals as the managed population** — applicants, candidates, certificants are persons. Remove → organizational accreditation.
3. **Eligibility-gated qualification path ending in a recorded grant decision** — a person's application (evidence of education/experience/etc.) plus an assessment outcome (exam result, reviewed application, portfolio) determines whether the credential is granted. Remove → roster or award list.
4. **Credential held as a standing person-bound state** — the granted credential is an ongoing state that can lapse/expire/be renewed/revoked and that the body can stand behind (attest to) while it is active. Remove → one-shot award/certificate of attendance.

Historical check: paper-roster-era certification bodies (application form → review → grant → annual renewal) satisfy all four without any digital CE tracking; a no-renewal "lifetime" certification still satisfies 1–4 (the state exists; it simply has no renewal obligation — renewal moves to L1). Government licensure boards use the same machinery (LearningBuilder markets a licensure posture) — the definition holds regardless of mandatory/voluntary character. No L0 element over-fits the modern US association implementation.

### L1 — Common Mature Structure

- Recertification/renewal cycles: renewal application opens automatically on grant; checklist-style requirement sections; grace periods, extended timelines, lapsed statuses, interim milestones
- CE tracking: CE log; credit categories with minimums and caps; external evidence upload; approved-provider programs that post attendance so eligible CE counts automatically
- Audits of initial and recertification applications: rule-based or random selection, anonymous reviewers, in-platform documentation collection, outcome tracking
- Exam coordination: authorization to test, integration with test-delivery vendors (or in-platform assessment + proctoring), results ingestion, pass/re-test branching
- Candidate/certificant self-service: dashboard, progress display, document upload, profile updates, renewal completion
- Automated communications: reminders and milestone notifications (email/SMS)
- Fees: application, exam, renewal fees; payment collection
- Credential artifacts: printable certificates; digital badges/micro-credentials (increasingly)
- Staff machinery: application queues, cycle dashboards, reporting/analytics
- Rules encoding: program handbook requirements encoded as configurable rules/paths; multiple eligibility paths
- AMS/CRM integration: SSO, member record sync, write-back of status/completions

### L2 — Variant / Optional Structure

- Program-family posture: standalone certification platform vs suite covering licensure (regulatory agencies, complaints & investigations) / accreditation / CE as siblings of the same codebase
- LMS-embedded posture: learning delivery first, credential lifecycle carried inside the LMS (TopClass pattern)
- General application/review platform configured for credential programs (front-half machinery only; OpenWater pattern)
- MOC (maintenance of certification) programs — medicine-style multi-requirement cycles
- CE-management depth as a product of its own (approved provider networks, course catalogs, revenue programs)
- Assessment depth: external testing vendors vs in-platform proctored exams vs low-stakes assessments with "test out"
- Competency/workforce-development framing (competency models, career paths — employer/internal audience)
- Employer involvement (vouchers, sponsorship)
- Credential tier structures (levels, stacked credentials, micro-credentials)
- Regulatory geography: US healthcare/licensure CE ecosystem vs other regimes

### L3 — Vendor-specific (Research Notes only)

- LearningBuilder: "Learning Plans"; Workflow Editor and Visual Rules Engine; Certification Dashboard; admin queues; FedRAMP-certifiable hosting claim; 508 compliance claim; MOC guide; approved provider program; voucher program; "handbook-to-system rules" framing
- TopClass: soft/hard stop enforcement on lapse; 20+ languages; iMIS/Salesforce/Personify/NetForum/Wicket integrations; Talented Learning awards; revenue stats ($220M/$95M/$4:1) — marketing figures, not operational facts
- OpenWater: phases/rounds; roll-up competitions; Email Wizard; public gallery; iMIS bridge — machinery shared with its awards/grants/abstracts products
- EthosCE: ACCME PARS / JA PARS / CPE Monitor / CE Broker integrations; Learning Groups; Cadmium suite (Eventscribe, Warpwire)

## Vendor-specific Findings

- LearningBuilder's vendor FAQ explicitly defines the category minimum and the AMS boundary (quoted above) — unusually valuable tier-A source for canonical abstraction, but treated as one vendor's framing, corroborated structurally by TopClass's feature set and the absence of the machinery in OpenWater's help center.
- LearningBuilder's claim "Every certification management system, no matter the industry, must be able to conduct audits" is a vendor assertion; treated as strong evidence that auditing is standard in the purpose-built category (corroborated by the product's dedicated audit machinery), but audit selection details (random vs all) vary and are program policy.
- TopClass "soft or hard stops when credentials lapse" — product-specific phrasing for a concept likely broader (enforcement at lapse), but only directly observed in TopClass; kept qualitative in the final document.

## Rejected Findings

- **"Certification management includes exam delivery"** — rejected: LearningBuilder explicitly integrates external test-delivery vendors; TopClass offers in-platform assessment; the invariant is the assessment outcome feeding the grant decision, not where the exam runs.
- **"Certification = course completion"** — rejected: EthosCE shows completion certificates as LMS territory; professional certification requires eligibility + assessment + standing credential.
- **"Public verification registries are a standard capability"** — unverified in the reachable sample (no fetched page described a public registry); recorded as uncertainty, excluded from the canonical model.
- **"CE requirements are universal"** — rejected as L0: lifetime/no-renewal certifications exist historically; renewal/CE is L1 despite market near-universality.
- **"Certification management is an AMS feature"** — rejected: both LearningBuilder and TopClass position the credential program as a distinct system integrated with (not contained in) the AMS.

## Boundary Findings

1. **vs Accreditation Management (§25 sibling) — near-duplicate flag RESOLVED as "distinct Types, shared front half."** The intake→review→decision→standing-status machinery is genuinely shared, and one codebase demonstrably runs both (OpenWater: accreditation offering documented by sibling pass; LearningBuilder markets both certification and accreditation). But the Types differ on two structural axes: (a) managed population — individuals vs organizations; (b) maintenance spine — person-bound recurring maintenance (CE logs, recertification applications, CE audits, lapse handling) vs standards-based organizational evidence (self-studies, peer review, interim reporting). Purpose-built certification products carry the full maintenance spine and no standards-mapping machinery; purpose-built accreditation products show the reverse. Distinct Types in one credentialing-program family; the §25 accreditation doc's "probable near-duplicate" assessment is revised accordingly (shared machinery ≠ same Type).
2. **vs Accreditation / Certification Management (§11) — CONFIRMED distinct.** The §11 pass predicted §25 certification manages credentials issued *to people*. Observed sample confirms: the managed population is individuals; there is no external-standard requirement mapping. The §11 Type runs the *seeking organization's own* compliance posture; this Type runs the *issuing body's* program. Vocabulary collision only.
3. **vs Continuing Education Management (§25 sibling, unprocessed) — gradient, flag for joint review.** CE is the renewal input of certification management, and LearningBuilder ships CE Management as its own solution (approved provider networks, course catalogs). Working distinction: CE management centers on learning-activity approval/credit capture; certification management centers on the credential lifecycle and consumes CE as evidence of maintenance. The same product can serve both. Flagged for joint review when continuing-education-management is processed.
4. **vs LMS (Corporate LMS §09 / association LMS) — structural test: what is the managed record?** LMS manages learning (courses, completions); certification management manages the credential (eligibility, grant, standing). EthosCE (CE-LMS) tracks credits and completions but not credential standing. TopClass shows LMS→certification convergence. Boundary holds on the object of record; convergence noted.
5. **vs AMS / Membership Management (§25) — confirmed distinct by direct vendor evidence** (LearningBuilder FAQ: AMS = membership system of record; certification platform = credential workflows; run integrated). Certification personnel records typically interlock with member records.
6. **vs Government Licensing Management (§24) — machinery overlap, authority difference.** LearningBuilder markets license management for regulatory agencies on the same platform (applications, renewals, CE, complaints & investigations). Licensure is statutory and mandatory; certification is voluntary and issued by a professional body. Probable sibling Type sharing most machinery; disciplinary machinery (complaints, investigations) noted as licensure-side. Recorded lightly (no separate product sampled).
7. **vs Digital Credential Platform (§23, unprocessed) — issuance artifact vs credential infrastructure.** Certification management issues certificates/badges as artifacts of the grant (TopClass delegates to badge platforms). Digital-credential platform as a Type would center the portable credential representation/verification itself. Boundary held; flagged as note only (sibling unprocessed).
8. **vs Assessment/Exam platforms — capability relationship.** Exam delivery may be external (test-delivery vendors) with results ingested; the exam platform is a service provider to this Type, not a variant of it.

## Uncertainties

- **Public verification/registry** (searchable directory of certificants, employer verification) — expected market behavior but not directly observed in the reachable sample; excluded from canonical model; left as uncertainty.
- **Revocation/discipline machinery** in voluntary certification — LearningBuilder mentions complaints & investigations only in its *licensure* posture; whether voluntary certification programs commonly manage revocation in-system is unverified; the final document mentions revocation only as part of the standing state concept, without claiming specific machinery.
- **CE Broker's role** — unreachable; its existence and ecosystem position are evidenced only via EthosCE's integration claims. No operational claims made about it.
- **Application/review platforms' certification depth** — OpenWater's current site shows no certification page (only accreditation); the near-duplicate resolution rests on the help-center structure + sibling accreditation evidence; if a certification-specific OpenWater offering exists undocumented, the front-half/back-half framing still holds structurally.
- **Numeric program parameters** (cycle lengths, CE hour totals, fee structures, grace-period lengths) — none asserted anywhere; not documented in reachable sources.

## Final Synthesis

Certification Management is the certifying body's program system of record for credentials issued to **people**: a named program defines who may qualify and how; individuals apply through eligibility-gated application paths; an assessment outcome (exam result, reviewed evidence, or both) feeds a recorded grant; and the granted credential is held as a standing person-bound state — active, renewable, lapsable, revocable — which the body maintains and attests to. Around that spine, mature products add the maintenance machinery that makes the credential's standing operational over years: recertification applications that open on grant, CE tracking with categories and provider networks, audits of initial and recertification applications, exam coordination with external or in-platform testing, self-service portals, automated reminders, fees, credential artifacts, and AMS/CRM interlock. The Type sits between organizational accreditation (same front half, organizational population, standards-based evidence spine) and CE/LMS platforms (learning-side machinery that feeds, but does not hold, the credential).
