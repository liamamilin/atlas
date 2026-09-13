# Research Notes — Enrollment Management

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an Enrollment Management application actually is, from real products: the objects it manages, the commitment machinery it owns, how the enrollment cycle runs year over year, its staff and family-facing surfaces, its rules, and — critically — its boundary against the already-documented sibling **Admissions Management** (this leaf carries a joint-review flag from that pass: "probable superset/umbrella framing") and against the pending siblings (Student Recruitment CRM, SIS, Student Billing, Student Success).

## Initial Boundary (hypothesis before research)

- Market usage of "enrollment management" is ambiguous: (a) in higher education it names a *strategic discipline/division* spanning recruitment → admissions → yield → retention; (b) in K-12 private education it names *software* ("Enrollment Management System") covering inquiry → application → enrollment → re-enrollment; (c) generically, "enrollment" names the post-offer, pre-matriculation phase (deposit, contract, preparation).
- Candidate cores to test: (1) umbrella over admissions+recruitment+retention (would make the leaf a superset — taxonomy problem); (2) the enrollment phase itself: commitment (contract/deposit), readiness, renewal cycles, population oversight (would be a structurally distinct Type).
- Users: enrollment/admissions office staff; families (parents/guardians) and students as the completing parties.
- Unknowns: whether a "commitment/contract" machinery exists as a first-class structure across products or only as a K-12 artifact; where the admissions seam really sits; whether re-enrollment is definitional or segment-shaped; how higher-ed realizations differ structurally.

## Research Questions

1. What is the central object — is there a distinct "enrollment" record, and how does it relate to the person, the application, and the academic period?
2. How does a person *enter* the enrollment population — from admissions (accepted applicants) and from the existing student body (rollover/re-enrolment)?
3. What does "commitment" consist of — contracts, signatures, deposits, acceptance — and how is it recorded and tracked?
4. What readiness machinery exists between commitment and the period start (checklists, forms, materials, payments)?
5. What statuses/exits exist on an enrollment (holds, withdrawal, not enrolling) and what rules govern them?
6. How does the cycle renew — rollover, re-enrolment seasons, continuous/perpetual enrollment, transitioning years?
7. What population-level oversight exists (counts, dashboards, reporting, yield views)?
8. How do money and the commitment document interact (tuition/fees/aid amounts flowing into contracts, deposit collection, billing handoff)?
9. Where exactly is the seam with Admissions Management, and does the umbrella framing dissolve into suite packaging?
10. What varies by segment (K-12 private/international/charter, higher ed) and region?

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

| Product | Segment / philosophy | Evidence quality |
|---|---|---|
| **Finalsite Enrollment (EMS)** | US K-12 private/independent schools; full "Enrollment Management System" suite (inquiry→admissions→enrollment→billing); commitment/contract machinery in depth | Strong — public help centre; two deep process articles fetched (layer A) |
| **TADS (VenturEd Solutions)** | K-12 private/faith/boarding; **commitment machinery sold standalone** ("Contracts and Deposits") separate from Admissions, Tuition & Billing, SIS | Moderate — official product/site pages (subpages 403; layer A-/B) |
| **OpenApply (Faria Education)** | International & independent K-12; admissions CRM with a first-class **Re-Enrolment season** (dashboard, eligibility, transitioning years) | Strong — public help centre incl. Re-enrolment QuickStart (layer A) |
| **Slate (Technolutions)** | Higher education; admissions & enrollment CRM; **period-scoped "Enrollments" object** (person vs. academic context) + deposit/commitment decision chain | Strong — public knowledge base (enrollments.md fetched directly; deposit/decision machinery verified in the admissions-management pass) |
| **RNL (Ruffalo Noel Levitz)** | Higher-ed services+software; the **discipline-umbrella pole** ("Enrollment Solutions" = marketing + yield + aid leveraging + retention consulting) | Moderate — official site, category/service level (layer A-/B) |

Supporting (category level): Element451 (higher-ed CRM; "enrollment" named as a lifecycle stage distinct from admissions).

## Sources

Official (Tier 1/2), fetched 2026-09-07:

- Finalsite Enrollment help centre (schooladmin.zendesk.com):
  - KB root/category map: https://schooladmin.zendesk.com/hc/en-us (categories: Inquiry Process; Admissions Process; **Enrollment Process**; Contract Management; Tuition & Fees Management; Annual Enrollment Refresh; Enrollment Reporting; Billing; Payments; Parent Portal; Dashboard; Online Reading & Review; Direct Enrollment)
  - Enrollment Process category: https://schooladmin.zendesk.com/hc/en-us/categories/6217942197517-Enrollment-Process (article map)
  - Enrollment Process for New & Returning Students: https://schooladmin.zendesk.com/hc/en-us/articles/6219259058061 (six-step process; statuses; bulk operations; parent portal authentication; checklist monitoring)
  - Contract States: https://schooladmin.zendesk.com/hc/en-us/articles/6219201258637 (state machine; binding/regeneration semantics; deposit-in-contract; countersignature)
  - Category article titles (map-level evidence): Contract Management (Electronic Signatures; Dual Signatures; Contract Preview; Generation/Regeneration/Closing; Federal Truth in Lending Disclosure; Countersignatures); Tuition & Fees Management (Tuition & Tuition Discounts; Required & Optional Fees; Deposit; Payment Plans Overview; Financial Aid Management; Scholarship Management); Process for New & Returning Students (Rollover for Continuous Enrollment Schools; Intent to Enroll Form; Moving Applicants (New Students) to Enrollment; Rollover for Returning Students; Continuous/Perpetual Enrollment: Bulk Submit Contracts; Parent Enrollment Cycle); Annual Enrollment Refresh; Enrollment Reporting (Net Tuition & Fees Report); Dashboard ("Admissions Funnel, Current Counts, Reminders"); "Running a Lottery"
- TADS: https://www.tads.com/ (product taxonomy: Contracts and Deposits / Tuition and Billing / Educate SIS / Admissions (VenturEd) / Financial Aid; "Serving These Teams: Admissions, **Enrollment**, Financial Aid, Marketing-Comms, IT"; "TADS connects the full student enrollment lifecycle")
- OpenApply help centre:
  - Root: https://help.openapply.com/hc/en-us ("Seasonal Focus: Re-Enrolment Season Resources"; categories Application & Enrolment / Re-Enrolment / Payments / Messaging / Analytics)
  - Re-enrolment QuickStart Guide: https://help.openapply.com/hc/en-us/articles/55569056391449 (enable/configure → notify → track on Re-Enrolment dashboard → mark manually; eligibility conditions; contract-as-form; decline form; deadline extension; transitioning years; payments/FAQs)
  - Article titles (map-level): Re-enrolment Launch Readiness Checklist; Marking Re-Enrolment Manually (Individual/Bulk); Sending Re-Enrolment Email Notifications; Tracking your Re-Enrolment Status; Parent Guide to completing Re-enrolment; Filtering and Exporting Re-enrolled Students
- Slate (Technolutions) Knowledge Base:
  - Getting Started with Enrollments: https://knowledge.technolutions.net/docs/enrollments.md (person record vs. enrollment record; enrollment scoped to term/program/cohort/experience; enrollment dashboards/tabs; enrollment-scoped forms/fields/prompt lists; materials; statuses; class schedules via Course Catalog/Section datasets; data ownership across offices; permissions; reporting)
  - Deposit/decision-chain and applicant-status observations carried from the admissions-management pass (fetched 2026-09-06, layer A there): reply forms; deposit-pending → deposit-paid decision chain; enrollment checklist items; automating the "enrolled" person status; product positioning "Admissions & Enrollment" (https://www.technolutions.com/)
- RNL: https://www.ruffalonl.com/ (Enrollment Solutions umbrella: Enrollment Marketing & Student Search; **Yield Campaigns**/"optimizing yield"; Financial Aid leveraging solutions; Graduate & Online; Strategic Enrollment Planning consulting; separate Student Success/retention line)
- Element451: https://element451.com/ (positioning; journey stages "Marketing · Admissions · Enrollment · Student Success")

Abandoned / failed sources (Source-access Limitation):

- https://www.blackbaud.com/products/blackbaud-enrollment-management-system — 404; https://www.blackbaud.com/products/blackbaud-education-management — 404 (Blackbaud abandoned after 2 failures; the second K-12 suite pole is therefore evidenced indirectly via Finalsite/TADS/OpenApply only)
- https://www.tads.com/solutions/contracts-and-deposits/ and https://www.tads.com/serving-these-teams/enrollment/ — 403 (bot protection; TADS kept at site root level)
- https://knowledge.technolutions.net/docs/deposits.md — 404 (guessed URL; no deposit doc located this pass)
- curl of https://knowledge.technolutions.net/llms.txt index returned nothing usable (Slate deposit article left unlocated; deposit evidence carried from the admissions pass instead)

---

## Product Observations

### Finalsite Enrollment (EMS) — evidence layer A (two full articles + category map)

Positioning/shape: a K-12 "enrollment management system" whose help centre separates an **Inquiry Process**, an **Admissions Process** (dynamic checklists, list filters, bulk communication; Online Reading & Review), and an **Enrollment Process** ("Manage your online contract, update all tuition and fee information, personalize enrollment communications, and track and report on key enrollment data"), plus Billing (module integrated with the enrollment process) and Payments. Dashboard category: "Admissions Funnel, Current Counts, Reminders, Quick Search, Quick Actions, User Notifications".

**Population and inflows (Process for New & Returning Students):**
- The enrollment population lives on a **Students in Enrollment** list page inside an **Enrollment tab**, with a **term picker** (per-year). Two inflows feed it: **Rollover for Returning Students** (existing students carried into the next enrollment year) and **Moving Applicants (New Students) to Enrollment** (accepted applicants cross from admissions into enrollment). Related: **Rollover for Continuous Enrollment Schools**, **Intent to Enroll Form**, **Parent Enrollment Cycle**, **Continuous/Perpetual Enrollment: Bulk Submit Contracts Feature**.
- **Enrollment statuses** (standard, extendable by custom statuses): **Enrollment in Progress** (post-rollover default, enrollment type "Returning", contract status "Pending"), **Academic Hold**, **Financial Hold** ("they can enroll once those requirements have been met"), **Mid-Year Withdrawal** (removed from Enrolled Students page, remains on the enrollment list, gets the **Former Student role**), **Not Enrolling** (student decided during the process not to enroll; Former Student role applied). Bulk status change from the list page (Edit menu → Change Status) or individually.

**The six-step enrollment process (layer A, article):** (1) update enrollment statuses in bulk; (2) **add Financial Aid** — "in most cases… before sending out Contracts so families see the correct amounts"; (3) **preview aid and scholarship amounts in bulk** before generating contracts (filter Enrollment-in-Progress + Pending contracts; add Financial Aid Amount / Scholarship Amount columns via Search & Reports); (4) **contract preview & generation** — preview per student ("as it would appear to the family in the Parent Portal"), generate individually (Manage Contract menu) or **in bulk** from the list page; generated contracts become visible to **financially responsible parents/guardians** in the Parent Portal; (5) **send the enrollment email** — template with merge tokens (portal URL, **authentication link/code** to link the family to the student), family-based sending, scheduling; dual-signature households need two unique portal accounts; (6) **monitor checklist & contract completion** — per-student **checklist progress bar**, hover shows items done/pending; **Filter Options can surface patterns like "Contract complete but Deposit incomplete"** to target bulk reminders ("Contract/Registration Form" and "Deposit/Registration Fee" checklist items).

**Contract machinery (layer A, Contract States article):**
- States: **Pending** (not yet generated; parents see the checklist item but cannot complete it) → **Generated** (blue "Complete Form" button appears; a warning symbol marks contracts generated with errors — "the parent will NOT be able to complete it"; fix + regenerate) → **In Progress** (parent opened it; Save & Finish Later supported) → **Pending Signature** (dual-signature feature: second signer; "The deposit payment page will not be available until both signatures are submitted" — "for legal-binding reasons") → **Pending Payment** (form complete, deposit unpaid; parent can no longer change the contract) → **Pending Countersign** (countersign feature: a school representative must countersign; deposit paid before countersign stays unchecked until full submission) → **Submitted** ("completed, signed by all necessary parties, and the deposit has been paid (if applicable)"; viewable as PDF; no further edits except regeneration).
- **Binding semantics**: states before signature (Pending/Generated/In Progress) are **dynamic** — fee/rule/content changes apply automatically with a red notice to the parent on reopen; states from Pending Signature on "have a submitted signature from the parent, which means the terms are now legally binding" — changes require **regeneration** ("Regeneration deletes the previous contract"; options to regenerate preserving signature; "the parent will not be prompted to pay the deposit again").
- Related machinery (map-level): **Electronic Signatures**, **Dual Signatures on Contracts** (two unique Parent Portal accounts), **Countersignatures** (setup + admin experience), **Contract Preview**, **Contract: Generation, Regeneration, & Closing**, **Contract Fees / Contract Fee Rules** ("Guide to Requesting Contract Fee and Rule Additions and Updates"), **Federal Truth in Lending Disclosure (TILA)**.

**Money layer (Tuition & Fees Management category, map-level):** Tuition & Tuition Discounts; **Required & Optional Fees**; **Deposit**; **Payment Plans Overview**; Financial Aid Management; Scholarship Management. **Annual Enrollment Refresh**: update "fields that drive tuition", term-based fields, enrollment setup. **Enrollment Reporting**: **Net Tuition & Fees Report**; Enrollment-Related Reports. Billing module integrates with the enrollment process; Payments platform processes transactions.

**Adjacent/sibling machinery inside the same suite (context, not this leaf's core):** Inquiry forms (Leadflow), application forms/checklists, **Online Reading & Review** ("Combine the information collected during a student's application process into an easy to read package for readers to review"), events/interviews (School Interviews, Shadow Days, Open Houses), **Running a Lottery**, Data Management (duplicate matching), communication tools, Parent Portal, Integrations.

### TADS (VenturEd Solutions) — evidence layer A- (site root; subpages 403)

- Product taxonomy splits the K-12 back office into: **Contracts and Deposits** ("Streamline enrollment commitments with smart tools that make contract signing and deposit collection fast, secure, and effortless for both schools and families") / **Tuition and Billing** / **Educate SIS** / **Admissions** (sold by sister brand VenturEd) / **Financial Aid**.
- "TADS connects the full student enrollment lifecycle with seamless integrations."
- **"Serving These Teams": Admissions, Enrollment, Financial Aid, Marketing/Comms, IT** — "Enrollment" is treated as a distinct school function/team with its own software needs.
- Suite framing: "Organizations adopt VenturEd Solutions to manage school admissions, enrollment, tuition management, financial aid, and payments."
- Significance: the commitment machinery (contract signing + deposit collection) is **independently productized**, separate from admissions and from billing — direct evidence that the enrollment-commitment core is a distinct, sellable structure (layer B across Finalsite's Enrollment-Process-vs-Admissions-Process split and TADS's productization).

### OpenApply (Faria Education) — evidence layer A (Re-enrolment QuickStart + help-root map)

- Self-labels "Admissions Management & CRM" for international/independent schools; rosters Inquiries → Applicants → Students (from the admissions pass: status levels organize the applicant's movement; "Enrolled" is a status).
- **Re-Enrolment is a first-class seasonal operation** ("Seasonal Focus: Re-Enrolment Season Resources" on the help root): QuickStart Guide, Launch Readiness Checklist ("Validate setup and data before sending invitations"), overview video, webinar.
- QuickStart flow: **Enable & Configure** (re-enrolment preferences + deadlines) → **Notifications** (launch emails from the **Re-Enrolment dashboard**) → **Track Responses** (dashboard monitoring) → **Mark Manually** (individual or bulk marking of re-enrolment decisions).
- **Eligibility conditions** for appearing in re-enrolment: status is Enrolled; not in the top grade; not already enrolled as a new student for next year; assigned to the correct current grade.
- **The re-enrolment form can serve as the enrolment contract** (customise at Settings > Forms or provide the contract to support); a **decline form** appears automatically once forms are enabled; families marked Declined are excluded before notifications.
- Money: payments recorded with confirmation (offline payment option exists — "Parents confirm but no payment is recorded… review payment settings"); FariaPay/Stripe built-in payments (from help root + admissions pass).
- **Transitioning Years**: bulk year-advance operation, run "after all re-enrolment decisions were finalised" (FAQ error pattern); next-year grade adjustable from the Re-Enrolment dashboard before transitioning.
- Deadline extension ("Families cannot access re-enrolment → the deadline has passed → extend… then resend"); analytics ("Re-enrolment numbers do not match expectations → review enrolment analytics for the selected academic year"); filtering/exporting re-enrolled students.

### Slate (Technolutions) — evidence layer A (enrollments.md) + layer A carried from the admissions pass

**Enrollment as a period-scoped record distinct from the person (direct fetch, layer A):**
- "Enrollments provide a flexible way to track a student's participation in a specific academic term, program, cohort, pathway, or experience. The person record stores information about the student overall. An enrollment record stores information connected to a particular academic context."
- "The person record tells you who the student is. The enrollment record helps you understand what academic experience, term, or program the student is participating in."
- Examples: current-term enrollment; study abroad; clinical placement; internship; graduation preparation; cohort/bridge; athletics/co-curricular.
- **Enrollment core components**: Enrollment Dashboards (term/program/status; outstanding checklist items; forms/materials; recent notes; next actions), **Class schedules** (connected via **Course Catalog and Course Sections datasets** — advising/registration-pattern use, e.g. credit load, repeated courses), **Enrollment-scoped Materials** ("the same type of document can be collected multiple times… a financial responsibility agreement each term"), **Enrollment Tabs**, **enrollment-scoped forms/fields/prompt lists** (e.g. Registration Clearance Status: Not Started / Pending Advisor Review / Cleared / Not Cleared / Needs Follow-Up).
- **Enrollment statuses** (naming-convention examples): Active, Pending, Complete, Withdrawn, Cancelled, Needs Review; dashboard examples add "at risk", "cleared", "abroad".
- Governance: **data ownership across offices** (advising, student success, registrar, financial services, study abroad…), **permissions for sensitive information** (financial, health/compliance, accessibility, conduct), reporting needs ("Which students are active in a given term or program?", "Which students still have outstanding requirements?"), historical preservation per term/experience, student-portal question ("Should students be able to view or complete parts of the enrollment process through a portal?").
- Framing note (honesty): this doc sits under Slate's **Student Success** documentation, and the feature is marked "under development" — Slate's enrollment object is the *participation record*, not a contract object.

**Commitment machinery (carried from the admissions pass, layer A there):** post-decision chain on accept: reply form → **deposit-pending decision → enrollment deposit payment-due activity → deposit-paid decision (final)**; assigning **enrollment checklist items**; automating the **enrolled person status**. Decisions are released through the applicant status page. Platform positioning: "Admissions & Enrollment" (one platform; also Student Success, Advancement).

### RNL (Ruffalo Noel Levitz) — evidence layer A- (official site; services/category level)

- Positioning: "Enrollment and Fundraising Management for Higher Education and Nonprofit Organizations."
- The **"Enrollment Solutions" umbrella** spans: Enrollment Marketing & Student Search ("building demand"); **Yield Campaigns** ("optimizing yield" — admitted-student campaigns); **Financial Aid Solutions** ("advanced financial aid… leveraging"); Graduate & Online (lead generation, recruitment & conversion); **Strategic Enrollment Planning Consulting**; CRM implementation/optimization — plus a separate **Student Success** line (Retention Management System, Student Retention Predictor).
- Significance: in higher education, "enrollment management" names the **whole-funnel discipline/division** (recruit → admit → yield/aid → retain) — the umbrella pole. It is largely a *services + analytics* industry around the funnel rather than a distinct software structure beyond the phases' own systems.

### Element451 — evidence layer A- (official site, positioning level)

- "The AI-Driven CRM and Agent Platform for Higher Ed"; journey stages listed as **"Marketing · Admissions · Enrollment · Student Success"**; customer titles include "VP of Enrollment and Marketing"; product features include Applications + Decisions, StudentHub, Journeys, Campaigns.
- Significance: "enrollment" is treated as a distinct lifecycle stage/office adjacent to admissions — supporting the phase distinction (weak/positioning-level evidence only).

---

## Cross-product Comparison

| Aspect | Finalsite Enrollment (EMS) | TADS | OpenApply | Slate | RNL / Element451 |
|---|---|---|---|---|---|
| Central object | Enrollment record per student per enrollment year ("Students in Enrollment", term picker) | Enrollment commitment (contract + deposit) as productized object | Student's place confirmed per academic year via Re-Enrolment | **Enrollment record** scoped to term/program/cohort/experience, distinct from the person record | (services/CRM level — the funnel population) |
| Population inflows | Rollover for Returning Students **and** Moving Accepted Applicants into Enrollment | (not directly documented at reachable level) | Eligibility conditions select currently-enrolled students for the next year | Enrollment records created as students take up/continue academic contexts | (funnel stages: inquiry→app→admit→enroll) |
| Commitment act | Online **enrollment contract** (states Pending→Generated→In Progress→Pending Signature→Pending Payment→Pending Countersign→Submitted) + **deposit** inside the contract flow | **Contract signing + deposit collection** (the product's definition) | Re-enrolment confirmation form — "can be used as the enrolment contract" — + payment | Offer acceptance (reply form) + **enrollment deposit** recorded as decisions → "enrolled" status | (yield campaigns to convert admits; services) |
| Signatures | E-signature; **dual signature** (two unique portal accounts); **school countersignature**; binding semantics after signature | "Contract signing" (depth unreachable) | Contract-as-form (signature depth not documented) | (not in scope of the fetched docs) | — |
| Financial terms on the commitment | Tuition + discounts, required/optional fees, deposit, payment plans; **aid & scholarship amounts applied before contracts go out**; annual refresh of tuition-driving fields; contract fee rules | Contracts carry fees (depth unreachable); Tuition & Billing is a separate product | Payments (online/offline) recorded with confirmation; fees/deposits via FariaPay/Stripe | Deposit payment activity on the decision chain | (aid "leveraging" as a yield service) |
| Readiness tracking | Enrollment checklist with per-item states + progress bars ("Contract complete but Deposit incomplete" filter) | (not directly documented) | Re-enrolment forms; launch-readiness checklist for the school | Enrollment-scoped checklists, materials, forms, clearance-status prompt lists | — |
| Managed standing | Enrollment in Progress / Academic Hold / Financial Hold / Mid-Year Withdrawal / Not Enrolling; Former Student role | (not directly documented) | Confirmed/declined responses; deadline extension; decisions saved before transitioning | Active / Pending / Complete / Withdrawn / Cancelled / Needs Review (+ "at risk", "cleared" examples) | — |
| Population oversight | Dashboard: **Current Counts** + Admissions Funnel; bulk status/contract/communication operations; Search & Reports; Net Tuition & Fees Report | (insights claimed at site level) | **Re-Enrolment dashboard** (responses, counts); enrolment analytics; filtering/exporting re-enrolled students | Reporting by term/cohort/program; dashboards | **Yield analytics/campaigns; strategic enrollment planning (services)** |
| Cycle renewal | **Rollover**; **Continuous/Perpetual Enrollment** (auto-renewal model + bulk submit); Parent Enrollment Cycle | ("full student enrollment lifecycle") | **Annual Re-Enrolment season**; **Transitioning Years** | Per-term enrollment records (recurring, term-based processes; "continuing student processes") | (annual funnel cycles) |
| Family/student surface | **Parent Portal** (contract completion, deposit, authentication codes, dual-signature accounts) | "fast, secure, and effortless for both schools and families" | Parent-facing re-enrolment + Parent Guide; parent email dependency | Portal question (student-facing enrollment parts); applicant status page carries reply/deposit | — |
| Sibling machinery bundled | Inquiry + Admissions (reading/review) + Billing + Payments + CMS pairing | Admissions/Tuition/SIS/Financial Aid are **separate products** | Admissions CRM + Payments + testing (iDAT) | Applications/Reader/Decisions + Student Success + Advancement on one platform | Marketing/retention services as sibling lines |

### Stable commonalities (layer B — observed across ≥3 sampled products)

1. **A period-scoped enrollment population** — individuals held as enrolled/enrolling for a specific academic year or term, distinct from both the person record and any application record (Finalsite, OpenApply, Slate; TADS's product definition implies it).
2. **A commitment act as the decisive event** — a recorded binding of the person to the period via a signed document and/or deposit/acceptance, completed by the family/student through a portal (Finalsite contract+deposit; TADS contract signing+deposit; OpenApply confirmation form+payment; Slate accept+deposit chain).
3. **Readiness/requirements tracking per enrollee** — checklists of forms, materials, and payments due before the period (Finalsite checklist machinery; Slate enrollment-scoped checklists/materials; OpenApply re-enrolment forms).
4. **Managed enrollment standing with exits** — statuses including holds, withdrawal, and "not enrolling/declined", with history preserved (Finalsite, Slate, OpenApply).
5. **Population-level oversight of the period** — list/dashboard of the whole enrollment population with counts and follow-up on incompletes (Finalsite Current Counts + checklist filters; OpenApply Re-Enrolment dashboard; Slate reporting questions; RNL's yield/strategic-planning layer at the discipline pole).
6. **The renewal/annual cycle** — the population is rolled over, re-enrolled, or transitioned into the next period (Finalsite rollover + continuous enrollment; OpenApply re-enrolment season + transitioning; Slate per-term recurring processes).
7. **Money attaches to the commitment moment** — tuition/fees/aid amounts flow into the commitment document; the deposit is collected at/within it; deeper billing/collection lives in a separate billing function (Finalsite Billing module + TADS product split; Slate deposit-only).
8. **Family/portal completion** — the completing party is the family (K-12) or student, authenticated into a portal (Finalsite Parent Portal + authentication codes; OpenApply parent access; Slate portal surface).

### Divergences (implementation/segment, not structure)

- **Commitment instrument**: K-12 private = binding multi-party contract with e-signatures, dual signatures, countersignatures, fee rules (Finalsite; TADS) vs confirmation-form-as-contract (OpenApply) vs higher-ed accept+deposit without a contract object (Slate).
- **Renewal model**: annual opt-in re-enrolment season (OpenApply; Finalsite default) vs **continuous/perpetual enrollment** (contract auto-renews; Finalsite ships a dedicated model) vs per-term enrollment records without a renewal season (Slate higher-ed).
- **Population construction**: rollover + accepted-applicant move (Finalsite) vs eligibility-conditioned selection (OpenApply) vs enrollment records created across many context types (Slate).
- **Where the money machinery lives**: inside the enrollment product (Finalsite Payments/Billing modules) vs separate sibling products (TADS Tuition & Billing) vs deposit-only (Slate).
- **Suite vs standalone**: enrollment machinery as one phase of an "Enrollment Management System" suite that also contains admissions (Finalsite) vs commitment machinery productized alone (TADS Contracts & Deposits) vs enrollment records as a Student Success-serving structure (Slate) vs the whole funnel sold as services (RNL).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
The institution manages a period-scoped enrollment population:

Enrollment record — an identified individual bound to the institution
                    for a specific academic period (year / term / academic context)
└── Commitment capture — a recorded binding act performed by the individual/family
    (signed enrollment contract and/or deposit / offer acceptance), with the
    institution controlling document generation and validity
└── Readiness tracking — per-individual requirements (forms, materials, payments)
    tracked to completion before the period starts
└── Managed standing — enrollment statuses including holds, withdrawal, and
    "not enrolling", updated as reality changes and history preserved
└── Population oversight — the period's enrollees held and worked as a whole:
    who has committed, who is incomplete, who declined or withdrew — counts and follow-up
```

Five properties; remove any one and the product stops being recognizable as enrollment management:

1. **Period-scoped enrollment records** (person × academic period) as the managed unit — without the period binding, it is a generic contact database; without the person's enrollment standing, it is admissions (prospects) or an SIS (academic records).
2. **Commitment capture** — the system of record for the act that converts an offer or an expected return into a committed place (contract/deposit/acceptance). Without it, the product is an admissions tracker or a roster.
3. **Readiness tracking** — per-enrollee requirements toward the period start. Without it, the product is a signature/deposit log.
4. **Managed standing with exits** — holds, withdrawal, not-enrolling, completion; the record reflects reality through the period and preserves history. Without it, an archive of signed documents.
5. **Population oversight** — the population is worked as a whole (lists/dashboards/counts, follow-up on incompletes). Without it, per-student record keeping rather than management.

Note on the spine: the **commitment act is the structural heart** — it is the boundary event between "candidacy/expectation" and "member of the period", and the machinery around it (document generation, signatures, deposit, binding semantics) is the most distinctive structure of this Type.

### L1 — Common Mature Structure (very common; not definitional)

- **Family/student portal completion**: authenticated parent/student access to complete contracts and checklists; authentication codes/links; financially-responsible-party handling; dual-signature account separation.
- **Bulk cycle operations**: bulk status change, bulk contract generation, bulk preview of aid amounts, bulk marking of re-enrolment decisions, bulk year-transition (rollover/transitioning), bulk communications.
- **Communication automation**: enrollment emails with merge tokens, notification on launch, reminders targeted at incomplete states (e.g., contract signed but deposit unpaid), deadline notices.
- **Financial-terms assembly**: tuition and discounts, required/optional fees, payment plans, financial aid and scholarship amounts applied before the commitment document is delivered; contract fee rules; annual refresh of tuition-driving fields.
- **Enrollment reporting/analytics**: counts of committed/pending/declined, enrollment-related reports, net tuition & fees, exports, funnel-context dashboards.
- **The renewal season as a managed operation**: launch-readiness checklists, notification waves, response tracking, deadline extension, transitioning/rollover execution — plus the **continuous/perpetual enrollment** model where renewal is automatic.
- **Roles & permissions**: admin/enrollment staff roles, countersigner role, family roles; sensitive-data permissions (financial, health, conduct — Slate).
- **Integration spine**: admissions handoff (accepted applicants in), SIS handoff (at period start/matriculation), billing/tuition-management handoff (charges move to collection).

### L2 — Variant / Optional Structure (segment, geography, model, posture)

- **Segment shape**: K-12 private/independent (binding contracts, re-enrolment season, rollover) vs higher education (acceptance+deposit commitment; term-scoped enrollment records; yield oversight by the enrollment division) vs international/boarding (agents, families abroad, cross-border payments) vs public/charter (**lottery-based placement** feeding enrollment — Finalsite "Running a Lottery").
- **Renewal model**: annual opt-in vs continuous/perpetual enrollment vs per-term records without renewal season.
- **Commitment instrument depth**: full legal contract with countersignature and regulatory disclosures (e.g., US Truth-in-Lending on K-12 contracts) vs simple confirmation + deposit.
- **Umbrella/suite framing**: products marketed as "Enrollment Management" that bundle inquiry + admissions + enrollment + billing (the sibling Types inside one suite); the discipline-level umbrella (RNL-class: recruitment + yield + aid leveraging + retention as services).
- **Placement selection models**: selective admission upstream vs lottery placement.
- **Regulatory posture**: e-signature regimes, TILA-style disclosures, sensitive-data permissions.

### L3 — Vendor-specific (research notes only)

- **Finalsite Enrollment**: exact contract state machine and names; dual-signature two-account requirement; authentication codes; contract fee rules and the support-requested fee/rule update process; "Former Student" role; Direct Enrollment; Leadflow; convenience-fee merge tokens; lottery runner; rollover specifics; CMS pairing (Composer).
- **Slate**: Enrollments feature under active development; Enrollment Dashboards/Tabs; enrollment-scoped prompt lists; Course Catalog/Section datasets feeding class schedules; deposit-pending→deposit-paid decision chain; turnkey model databases; positioning "Admissions & Enrollment".
- **OpenApply**: Re-Enrolment QuickStart/Launch-Readiness machinery; eligibility condition set; Transitioning Years bulk operation; FariaPay; contract-by-configuration; parent-email dependency failure modes.
- **TADS**: Contracts & Deposits as a standalone product; Educate SIS pairing; VenturEd suite framing; 403-protected documentation depth.
- **RNL**: yield campaigns, financial-aid leveraging, retention predictor, strategic enrollment planning consulting (services).
- **Element451**: Bolt agent teams per lifecycle stage; "Marketing · Admissions · Enrollment · Student Success" stage framing.

### Historical / market-sample check (§24 reasoning)

Would older, regional, platform-native products still fit the L0?

- **Era check**: the paper-era enrollment office kept an enrollment/re-enrollment roster (period-scoped population), collected signed enrollment contracts with deposits (commitment capture), tracked returnee requirements (readiness), marked withdrawals/"not returning" (managed standing), and counted the committed class (oversight) — all five L0 properties without portals, automation, or contracts-as-code. (Canonical inference, layer C; no fetched artifact, assertion kept at structure level.)
- **Regional check**: OpenApply's international-school re-enrolment machinery is explicitly designed for annual place-confirmation across regions; in systems with centralized national admissions, the institution still manages the matriculation/registration of its committed entrants — no direct vendor evidence gathered for centralized-admission countries; kept as inference (C) and listed in Uncertainties.
- **Platform-native check**: enrollment/re-enrolment modules inside SIS-family suites (TADS pairs with Educate SIS; Finalsite integrates outward to SIS/billing) satisfy the L0 spine; module boundary follows the commitment→readiness→renewal machinery.
- Conclusion: the L0 survives era/regional/platform variation. The modern envelope (portals, e-signature depth, payment platforms, communications automation) is L1/L2, not definition.

---

## Vendor-specific Findings

(single-source; not promoted to canon)

- Finalsite's contract binding semantics: once a signature is captured, fee/rule/content changes require **regeneration** of the contract (pre-signature states update dynamically); deposits are withheld until all required signatures exist "for legal-binding reasons"; a deposit paid before countersignature stays unchecked until full submission. Product-specific mechanics of a *concept* (signed commitment documents are treated as binding instruments and changes are reissued, not silently edited).
- Finalsite's checklist interlock pattern ("Contract complete but Deposit incomplete" as a filterable chased state) — concept general, mechanics product-specific.
- OpenApply's eligibility condition set for re-enrolment (Enrolled status, not top grade, not already enrolled for next year, correct current grade) — product-specific formulation of population-selection rules.
- OpenApply's **Transitioning Years** as a gated bulk operation run only after decisions are finalised — product-specific name for the period-advance operation.
- Slate's deposit chain living on the *decision* machinery (deposit-pending decision → payment-due activity → deposit-paid decision) rather than on a contract object — product-specific realization of commitment capture in higher ed.
- Slate's enrollment object serving Student Success contexts (study abroad, placements, cohorts) — evidence that the period-scoped enrollment structure generalizes beyond the admissions-adjacent phase; kept as interlock evidence, not as this Type's definition.
- RNL's "enrollment management" = whole-funnel services umbrella — market-positioning evidence only.

## Rejected Findings

- **"Enrollment Management = the whole funnel (recruit→admit→yield→retain)"** — rejected as the *defining* structure. The umbrella is real as market *positioning* (RNL; Slate's "Admissions & Enrollment"; K-12 suites named EMS) but dissolves structurally into sibling Types (recruitment, admissions, student success) plus the enrollment-phase core documented here. Defining the leaf as the umbrella would make it a superset of two other leaves and would not describe any single product's actual machinery.
- **"Enrollment Management = Admissions Management with another name"** — rejected. The admissions pass's own structural test (remove the application→evaluation→decision pipeline → recruitment + yield/commitment work remains) identifies a distinct residue; this pass finds that residue productized (Finalsite's Enrollment Process category; TADS Contracts & Deposits; OpenApply's Re-Enrolment season; Slate's enrollment records) with machinery admissions does not own (contracts with binding semantics, holds, rollover/re-enrolment, transitioning, enrollment counts).
- **"Re-enrolment is a K-12 variant, therefore not part of the Type"** — rejected as a reason to exclude; adopted as L1 common structure instead: renewal of the period population is how the commitment machinery re-fires, dominant in K-12 but expressed per-term in higher-ed realizations. It stays out of the L0 because higher-ed first-cycle commitment has no renewal of *existing* members.
- **"Contracts are definitional"** — rejected as a strict requirement: higher-ed realizations commit via acceptance + deposit (Slate layer A) and OpenApply substitutes a configurable form. The invariant is *commitment capture*, not the contract instrument.
- **"Deposits/tuition are definitional"** — rejected in their billing depth: fee/tuition *collection over time* belongs to billing/tuition management (TADS ships them as separate products; Finalsite as a separate module). What is definitional is the money *attached to the commitment moment* (the deposit inside the commitment act; terms assembled onto the document).
- **"Yield/melt analytics are definitional"** — rejected; population counts and conversion oversight are L1; services-level yield optimization (RNL) is the discipline pole.
- **"Enrollment = course registration"** — rejected: Slate connects class schedules to enrollment records via separate catalog/section datasets, documenting the seam rather than identity; course/section selection is the Course Registration sibling.

---

## Boundary Findings

### vs Admissions Management (sibling, processed — carries the joint-review flag from that pass)

The admissions pass flagged: "Enrollment Management is very likely a superset/umbrella framing rather than a structurally distinct Type" and recorded the structural test (remove the application→evaluation→decision pipeline → recruitment CRM + yield/retention work remains; keep only the pipeline → Admissions Management remains intact).

**This pass's verdict: the flag is resolved as "keep both Types; the umbrella is suite/discipline framing".**

- The *umbrella* reading is confirmed as market positioning: higher-ed "enrollment management" names a division/discipline spanning recruitment→yield→retention (RNL; Element451's stage list; Slate's "Admissions & Enrollment" platform framing), and K-12 products named "Enrollment Management System" bundle inquiry+admissions+enrollment (Finalsite EMS contains the Admissions Process, Online Reading & Review, and Inquiry Process alongside its Enrollment Process).
- The *structural* reading is also confirmed: a distinct enrollment-phase machinery exists, is documented in depth (Finalsite contract states/deposit/holds/rollover; OpenApply re-enrolment season/transitioning), and is **sold standalone** (TADS Contracts & Deposits) — so the leaf is not merely an alias of admissions.
- **The seam**: admissions owns candidacy through the recorded admission decision and its communication (application → completeness → review → decision). Enrollment management owns the committed population: the offer-response/commitment event (acceptance/contract/deposit), readiness for the period, standing through the period, and renewal for the next period. The seam is directly documented from both sides: admissions products end their canonical flow at offer response + deposit + "enrollment handoff (student of record)"; Finalsite's documented operation "**Moving Applicants (New Students) to Enrollment**" performs exactly that handoff inside a suite.
- Overlap zone: the offer-response/deposit event appears in both kinds of products (admissions pass documented reply forms + deposit decisions as its post-decision L1; this pass treats the same event as the commitment capture). The types therefore interlock at the seam, and suite products realize both; this is packaging, not identity.
- Structural tests, both directions: strip contracts/deposits/holds/rollover/counts from a K-12 EMS → an admissions system remains; strip the application→review→decision pipeline → an enrollment-commitment system remains (TADS Contracts & Deposits proves it can stand alone).

### vs Student Information System / SIS (sibling, unprocessed)

- The SIS owns the enrolled student's *academic record of record* (grades, transcripts, academic history); enrollment management owns the *commitment and readiness* of the period population up to/around the period start. Slate's enrollment object (participation record with term-scoped status) sits near this seam and is documented as serving cross-office processes (registrar owns course information; enrollment records organize contexts) — an interlock, not identity.
- Test: delete academic history → enrollment management still functions (commitments, contracts, readiness); delete the committed-population machinery → the SIS still functions. Handoff: rollover/transitioning feeds the next period's records; contract data flows to billing.
- Flag for the SIS pass: K-12 suites ship enrollment/re-enrolment machinery beside the SIS — recommend joint review of where "re-enrollment of returning students" sits in the SIS leaf's core.

### vs Student Billing System / Tuition Management (sibling, unprocessed)

- The commitment document *assembles* charges (tuition, fees, discounts, aid) and collects the deposit; billing/tuition management owns invoicing, payment plans, and collection over time. Direct evidence of the split: TADS ships **Contracts and Deposits** and **Tuition and Billing** as separate products; Finalsite separates an Enrollment Process from a Billing module. Flag for the student-billing pass (joint review recommended).

### vs Student Recruitment CRM (sibling, unprocessed — second half of the admissions pass's flag)

- Recruitment CRM = pre-application relationship building (inquiries, campaigns, events, engagement); enrollment management = post-offer commitment and period readiness. The phase gradient admissions→enrollment is documented; recruitment sits entirely upstream of the application and shares no machinery with this leaf beyond inquiry-capture being bundled in suites. Flag for that leaf's pass; expected resolution: distinct Types at funnel phases, bundling is packaging.

### vs Student Success Platform (sibling, unprocessed)

- Post-matriculation retention vs pre-matriculation commitment. Interlock documented from this side: Slate positions its Enrollments object under Student Success and uses it for advising/registration-clearance/term-specific support — the same period-scoped structure serves success workflows once the student is active. Flag for that leaf's pass: the enrollment record may appear in both documents; the discriminator is the job (commit/renew/readiness vs retain/succeed), not the record shape.

### vs Course Registration System (sibling, unprocessed)

- Commitment to the institution for a period vs selection of courses/sections within a period. Slate documents the connection (class schedules attached to enrollments via Course Catalog/Section datasets) — integration seam, not the same object.

### vs Financial Aid Management (sibling, unprocessed)

- Aid machinery (applications, methodology, awards) is its own Type; enrollment management consumes award *amounts* onto the commitment document (Finalsite assigns aid before contracts; aid/scholarship columns previewed in bulk). Same shallow-consumption pattern the admissions pass recorded for aid checklists.

### vs Campus Housing Management (sibling, processed)

- Housing selection/assignment is a parallel readiness process feeding enrollment checklists; no evidence in this pass of housing machinery inside enrollment products. Relationship: checklist items/parallel process.

### vs Event Registration Platform (§26)

- Structural analog: commit + readiness for a container (event vs academic period), family/party completion, deadlines. Differences: no institutional membership, no renewal cycle of the population, no contract/holding structure tied to an ongoing relationship. Different Type.

### vs Applicant Tracking System (§09, hiring analog)

- Offer → committed hire analog exists, but employment onboarding lacks the period-scoped renewal of a membership population and the institution/period record structure; noted only as a structural rhyme.

---

## Uncertainties

1. **Blackbaud Enrollment Management System not directly evidenced** (404 ×2) — the second major K-12 suite pole is triangulated via Finalsite/TADS/OpenApply only; no Blackbaud-specific claims made anywhere.
2. **TADS depth** — product subpages 403; the Contracts & Deposits product is evidenced at definition/positioning level (layer A-), not at workflow level. Its internal contract state handling is unknown.
3. **Slate's deposit machinery** — verified in the admissions pass (2026-09-06, layer A) rather than re-fetched this pass (deposits.md guess 404; llms.txt index curl unusable). Treat deposit-chain claims as layer A with the earlier fetch date.
4. **Higher-ed non-US realizations** (e.g., institutions under centralized admissions) — no direct evidence; the L0 is abstract enough to include them but nothing was verified.
5. **Charter/public-school pole** — evidenced only by Finalsite's "Running a Lottery" article title (map-level); internal lottery machinery not fetched.
6. **Whether any higher-ed product ships a true enrollment *contract*** (e.g., for international students or athletics) — not researched; the doc keeps commitment-instrument depth as a variant without claiming contract absence in higher ed universally.
7. **Continuous/perpetual enrollment mechanics** — evidenced at article-map level (titles) plus the bulk-submit feature note; the full model was not fetched.

---

## Final Synthesis

Enrollment Management is the institution-side system of record for **who is actually committed to attend — and return — for each academic period**. Its world model: a period-scoped population of enrollment records (person × academic period), fed by two inflows (rollover of returning members; accepted applicants moved from admissions); a **commitment act** as the structural heart (the signed enrollment contract and/or deposit/acceptance, generated and validated by the institution, completed by the family/student through a portal, with binding semantics after signature); per-enrollee **readiness tracking** (checklists of forms, materials, and payments toward the period start); **managed standing** (holds, withdrawal, not-enrolling, completion, with preserved history); and **population oversight** (the period's enrollees worked as a whole — counts, incompletes, declines — with reporting and handoffs to SIS and billing). The cycle renews period over period (rollover / re-enrolment seasons / continuous enrollment / per-term records).

The market label "enrollment management" also carries an umbrella sense (the higher-ed funnel discipline; suite products bundling recruitment + admissions + enrollment + billing). That umbrella is positioning over a bundle of sibling Types; the structurally distinct, standalone-sellable core — commitment, readiness, standing, oversight, renewal — is what this Type owns. The leaf therefore stands as a genuine Type alongside Admissions Management, with a directly documented handoff seam ("move accepted applicants into enrollment") and interlocks to SIS, billing, recruitment, student success, and financial aid.
