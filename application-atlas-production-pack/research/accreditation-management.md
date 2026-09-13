# Research Notes — Accreditation Management (§25 Nonprofit, Membership & Religious Organizations)

Research date: 2026-09-06

## Research Goal

Understand what "Accreditation Management" means as an Application Type in the directory's
association/membership context, how products in this space actually work, and how it differs
from the three adjacent leaves that share the word "accreditation":

- §11 **Accreditation / Certification Management** — already documented; the *seeking
  organization's own* compliance posture toward an external standard (controls, evidence,
  assessment event, credential maintenance).
- §23 **Academic Accreditation Management** — not yet processed; presumably the *education
  institution side* of academic accreditation.
- §25 **Accreditation Management** — this leaf.

Working hypothesis before research: §25's leaf is the **accrediting body side** — an
association/nonprofit that *operates* an accreditation program (like a grantmaker vs a grant
seeker). The research tests this hypothesis against real products.

## Initial Boundary

- Accreditors (bodies that accredit organizations, programs, or institutions) are mostly
  associations/nonprofits themselves: professional societies, standards bodies, education
  commissions. In the directory they live in §25 next to Certification Management, Continuing
  Education Management, and Standards Development Platform.
- The obvious confusion set:
  1. the seeker side (§11, §23) — same relationship, opposite seat;
  2. association Certification Management (§25 sibling) — same machinery, different population
     (individuals vs organizations);
  3. general application/review platforms (awards, grants, abstracts) — same intake+review
     machinery, different outcome (one-shot recognition/money vs standing status);
  4. Standards Development Platform — authoring the standards vs operating a program over them;
  5. Membership Management System — belonging vs earned status.

## Research Questions

1. What does the system of an accreditation *program operator* contain? (objects: program,
   standards, applicants/members, submissions, reviewers, decisions, status)
2. What is the end-to-end workflow: application → evidence → review → decision → renewal?
3. How are standards/criteria represented and used (templates? mapped evidence? scoring)?
4. How does the recurring cycle work (interim/annual reports, renewal, reaccreditation)?
5. Who are the users on each surface (program staff, reviewers/commissioners, applicants)?
6. How do systems connect to the accreditor's member records (AMS/CRM)?
7. Do institutions-side "accreditation management" products (marketing uses the same phrase)
   belong to this Type or to a different one?
8. What distinguishes accreditation from certification/awards/grants in the same vendor's
   platform?

## Representative Products

Selected for: market representativeness in the association/accreditation market, different
product philosophies (general configurable review platform vs domain-specific accreditation
platform), different customer levels, and — critically — coverage of *both seats* of the
accreditation relationship so the boundary could be settled empirically.

Accreditor-side (the candidate anchor for this leaf):

1. **OpenWater** — association-market application & review platform with a dedicated
   Accreditation offering; serves "nearly 1,000 associations, credentialing and accrediting
   bodies" (vendor claim). Philosophy: one configurable platform for every application-based
   program; accreditation is a configured use case.
2. **Weave Accreditation** (Weave Education LLC) — purpose-built platform for higher-education
   accreditors, sold alongside (but separate from) the institution-side Weave product.
   Philosophy: accreditation-specific workflows (applications, self-study, annual reporting,
   reviewer & commissioner workflows) plus services.

Institution-side boundary samples (products that also market themselves as "accreditation
management"):

3. **Weave Education** — institution/program side: assessment, curriculum mapping, standards
   evidence repository for preparing institutional & programmatic accreditation.
4. **Watermark Planning & Self-Study** — institution side; accreditation use-case pages per
   regional accreditor (HLC, SACSCOC, MSCHE, WASC, NWCCU, NECHE).
5. **Nuventive Improvement Platform** — institution-side planning/improvement platform covering
   strategic planning, accreditation, learning outcomes, program review.

Blocked sources (per network rules, abandoned after failures):

- **WizeHive** — root site returned HTTP 403 (twice-counted as two attempts).
- **Submittable** — root site returned HTTP 403.
- Watermark product page `/products/planning-self-study/` returned 404; root site used instead.

## Sources

All accessed 2026-09-06.

- OpenWater — Accreditation Management Software product page:
  https://openwater.com/accreditation-management-software
- OpenWater — Help Center (collections index): https://help.getopenwater.com/
- OpenWater — corporate root (platform list, client quotes): https://www.openwater.com/
- Weave Accreditation — Accreditation Process page (features, pricing, FAQ):
  https://weaveaccreditation.com/accreditation-process/
- Weave Education — root: https://www.weaveeducation.com/
- Watermark Insights — root + Accreditation use-case hub:
  https://www.watermarkinsights.com/ , https://www.watermarkinsights.com/explore/accreditation/
- Nuventive — root: https://nuventive.com/

Evidence layers used below: **A** = directly observed on an official source of a named
product; **B** = cross-product commonality; **C** = canonical inference.

## Product Observations

### OpenWater (accreditor-side; evidence layer A)

From the Accreditation Management Software page, its FAQ, and the Help Center:

- Positioning: "OpenWater runs your entire accreditation or certification program: application
  intake, multi-stage review, decisions, credentialing, payments, and annual renewal. Together
  with the association management software you already use, everything runs as one auditable
  system."
- "Track standards, compliance, and outcomes in every accreditation, reaccreditation,
  certification, and recertification cycle."
- Multi-stage submission and review: "Configurable stages, deadlines, and committee assignments
  that mirror your real process"; multi-round review with automatic forwarding between rounds
  (Help Center: "forward submissions to the next round"); review templates with weighted
  scoring, recusal, and **custom decision types** — the FAQ names examples: "approved, requires
  edits, probation, or any status you define".
- Cycle continuity: "One-click cloning — start next year's application and renewal cycle from
  last year's"; applicants "clone their prior submission and update only what changed".
- Corrections loop: "Reopen for edits — send submissions back to applicants with notes, then
  re-lock them on resubmission" with "a full audit trail of what changed and when".
- Intake governance: "Eligibility rules and validation — enforce required fields, minimums, and
  eligibility before submission to reduce application revisions."
- Category groups: "One workflow serves multiple programs or registrant types."
- Payments: submission fees, credit-card processing, invoices (product page + Help Center
  collection "Accept payments for your submissions").
- Member-data integration: SSO, live lookup fields in forms, and **pushback** — "Decisions,
  credentials, and payments write back automatically" to the AMS (iMIS, Fonteva, Nimble AMS,
  Salesforce named), writing to custom panels so member records are not overwritten.
- Reviewer experience: "Magic links for reviewers — open assigned submissions from a link with
  no password required"; third-party e-sign forms attached to applications.
- AI: "11 features for summaries, compliance checks, and quality scoring... AI assists but
  never decides. Final decisions always stay with you."
- Help Center structure (operational confirmation of the generic machinery): program setup;
  submission form setup (applicant settings, categories, form builder); payments; judging
  portal (evaluation form, ranking, blind fields); public website; managing submissions and
  applicants (approve, impersonate, email blasts); managing judges (teams, bulk assignment);
  results (winners, forwarding); export; integrations hub; roll-up competitions.
- Customer base claim: "trusted by nearly 1,000 associations, credentialing and accrediting
  bodies", including ASAE's Certified Association Executive credentialing process.

### Weave Accreditation (accreditor-side, education accreditors; evidence layer A)

From the weaveaccreditation.com Accreditation Process page (features, pricing, FAQ):

- Positioning: "Weave helps accreditors streamline workflows and increase satisfaction for
  everyone involved"; "a robust, established platform built with educational accreditor
  partners to serve the higher education accreditation community."
- Key features (vendor's own list):
  - **Applications** — "Intake and manage initial inquiries and candidate submissions."
  - **Annual Reporting** — "Simplify routine data collection with structured tracking, clear
    dashboards, and automated notifications."
  - **Self-Study & Special Reporting** — "Collaborate seamlessly on complex institutional
    self-studies and specialized reports within a single system."
  - **Reviewer Management** — "Organize reviewer assignments, track evaluation milestones, and
    flag potential problems before they escalate."
  - "Reviewer & Commissioner Workflows" (pricing tier bullet) — two-body governance (reviewers
    evaluate; commissioners decide).
- Standards as templates: "Weave Accreditation includes unlimited templates based on your
  standards and requirements. Customized description, instructions, and expectations for your
  members are embedded in context."
- Evidence: "unlimited storage for all supporting materials... keeping all evidence
  meticulously organized within the context of your standards."
- Member-based model: the accreditor's participating institutions/programs are "members";
  partner pricing is per member ("Includes up to 50 members; $15/mo per member over 50").
- Deployment spectrum (pricing tiers):
  - **Accept Submissions via Weave ($0)** — accreditor stays platform-neutral; "Program/
    Institution completes self-study in Weave; Provides accreditor with a read-only 'guest'
    link"; standardized electronic report, live hyperlinks/bookmarks, no separate evidence
    folders.
  - **Become an Accreditor Partner ($1500/mo)** — full workflows for staff, reviewers, and
    members; annual reporting and data dashboards; "smart overviews and automations".
- Integration: "fully documented API to enable integration with your CRM, Billing and Payment,
  or marketing and communications solutions."

### Weave Education (institution-side boundary sample; evidence layer A)

- "Weave is uniquely designed, empowering higher education to prepare for their institutional
  and programmatic accreditations."
- Capability set: assessment management, curriculum mapping, program review, strategic
  planning, dashboards, version-controlled reports, "submitting and storing all types of
  standards-related evidence in an easy-to-navigate, unlimited data repository", permissions
  and workflow management, "employing up-to-date standards and criteria".
- Users: institutions and programs (faculty, institutional-effectiveness staff); customers are
  colleges/universities, not accrediting bodies.
- Sold on a separate site/product from Weave Accreditation — the vendor itself splits the two
  seats of the relationship into two products.

### Watermark Planning & Self-Study (institution-side boundary sample; evidence layer A/B)

- "Planning & Self-Study (P&SS): Simplify assessment and accreditation work so your teams can
  focus on outcomes."
- Use-case pages exist per accreditor (HLC, SACSCOC, MSCHE, WASC, NWCCU, NECHE) — i.e., the
  product is marketed against *specific accreditors' requirements*, from the institution's
  seat.
- Customer evidence: "50% reduction in preparation time... for our self-study and our strategic
  plan" (Director of Institutional Effectiveness, Garrett College).
- Part of a broader institution suite (assessment, curriculum, faculty, student learning).

### Nuventive (institution-side boundary sample; evidence layer A)

- "delivers planning and improvement software that helps higher education institutions... from
  strategic planning to accreditation, learning outcomes, program review, and more."
- Institution-facing improvement platform; accreditation is one initiative type inside a
  planning/measurement system.

## Cross-product Comparison

| Dimension | OpenWater | Weave Accreditation | Weave Education / Watermark / Nuventive (institution-side) |
|---|---|---|---|
| Whose workflow | accrediting body / credentialing body (program operator) | accrediting body (education accreditors) | the seeking institution/program |
| Central container | program (application + review + decisions + renewal) | accreditation program with members | assessment/self-study workspace per institution |
| Standards representation | tracked per cycle ("standards, compliance, and outcomes") | templates built from the accreditor's standards; evidence organized against standards | standards mapped to institutional assessment/evidence |
| Participant record | applicant/submitter from member records (AMS) | member organizations (priced per member) | n/a (institution is the user) |
| Submission | application forms, attachments, eligibility gates, fees | applications, self-study, annual reports | self-study authoring, assessment data |
| Review machinery | multi-round, committees, rubrics, recusal, forwarding | reviewer assignments, milestones, reviewer & commissioner workflows | n/a (institution prepares for external review) |
| Decision | recorded; custom decision types (approved / requires edits / probation / custom) | commissioner workflows; decision recorded in system | n/a |
| Status & cycle | annual renewal; reaccreditation/recertification cycles; clone prior cycle | annual reporting; dashboards; ongoing member status | accreditation readiness between cycles |
| Member-system integration | AMS pushback of decisions/credentials/payments | API to CRM/billing | n/a |
| Product philosophy | one configurable platform for all application programs | accreditation-specific SaaS + services | institution-side institutional-effectiveness suite |

Key observations:

- **(B)** Both accreditor-side products — built for very different customers (trade/professional
  associations vs education accreditors) — share the same structural spine: program container →
  participating organizations → standards-structured submission → human review → recorded
  decision → standing status maintained through recurring reporting/renewal.
- **(A→B)** Intake→review→decision machinery is the same as awards/grants/abstract review
  (OpenWater runs all of these on one platform); what differentiates the accreditation use case
  inside that vendor's own platform is standards tracking, credentialing, renewal/reaccreditation
  cycles, and write-back of the standing status.
- **(A)** The market *itself* separates the two seats: Weave ships two different products
  (weaveeducation.com for institutions, weaveaccreditation.com for accreditors). Watermark,
  Nuventive, and Anthology-style institutional-effectiveness suites live on the institution side.
- **(A)** Governance in education accreditation is two-body (reviewers evaluate, commissioners
  decide); OpenWater generalizes to committees with custom decision types.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (accreditor-side program administration)

The smallest structure without which the product is no longer recognizable as accreditation
management for the *operating* body:

1. **Accreditation program as the organizing container** — a named program operated by the
   accrediting body, carrying the published standards/criteria that define what must be met
   (held in the system as the templates/requirements that structure submissions and review).
2. **Participating organizations** — identified organizations (institutions, programs,
   providers, firms) whose standing in the program is managed as records (applicant → candidate
   → accredited member), distinct from individuals.
3. **Standards-based evidence submission** — the organization submits structured application/
   self-study content and evidence organized against the program's standards.
4. **Human review producing a recorded decision** — reviewers/committees/commissions evaluate
   the submission; the system records the outcome decision for that organization.
5. **Standing accreditation status with a recurring cycle** — the decision issues into a status
   the organization holds over time, with validity and recurring obligations (interim/annual
   reporting, renewal/reaccreditation) managed in the system.

Removal tests: remove standards → generic application/review tool; remove organizations →
individual certification management; remove recorded decision → data collection; remove the
standing status/cycle → a one-shot award or grant program; remove the program container →
spreadsheets.

### L1 — Common Mature Structure

- Configurable submission templates bound to the standards (descriptions, instructions,
  expectations embedded in context)
- Multi-stage review: eligibility screening → committee/reviewer rounds → decision body;
  per-stage deadlines, forwarding, rubrics/weighted scoring
- Reviewer management: assignments (incl. bulk), teams, milestone tracking, conflict recusal,
  blinded fields, friction-reducing reviewer access
- Send-back loop: reopen a submission with notes; re-lock on resubmission; audit trail
- Intake governance: eligibility rules and validation before submission
- Automated communications: notifications, reminders, decision letters
- Interim/annual reporting collection with dashboards and automated notifications
- Fees/payments for application/renewal; invoicing
- Program reporting/analytics and export
- Integration with the accreditor's member/CRM systems (SSO, lookups, decision/status/
  payment write-back; or API)
- Cycle continuity: clone prior cycle (program configuration and prior submissions) so
  applicants update rather than re-enter

### L2 — Variant / Optional Structure

- Domain shape: education accreditors (self-study reports, commissioner bodies, member
  institutions) vs professional/trade association accreditors (certification-adjacent,
  payments-heavy, AMS-coupled) vs general submission platforms with accreditation configured
- Deployment posture: full partnership platform (accreditor runs everything in-system) vs
  submission-only neutrality (members may complete reports in the vendor's tool and hand the
  accreditor a read-only link) vs accreditor-side-only portals
- One program vs many programs/registrant types under one workflow (category groups)
- Combined accreditation + certification operation in one body (organizations + individuals)
- AI assistance for compliance checks/summaries/scoring suggestions (human decides)
- Public-facing surfaces (program websites, galleries) — stronger evidence in adjacent program
  types than in accreditation specifically
- Institutional-effectiveness coupling on the member side (assessment/curriculum data feeding
  self-studies) — belongs to the institution-side Type

### L3 — Vendor-specific (research notes only)

- OpenWater: magic links, applicant impersonation, public gallery/voting, roll-up competitions,
  1,500-field form ceiling, "11 AI features", FedRAMP Authorized/PCI DSS Level 1/Canadian data
  residency specifics, named AMS pushback behavior (custom panels), 5-minute chat SLA.
- Weave Accreditation: $0 submission tier vs $1,500/mo partner tier, 50-member pricing basis,
  read-only "guest" link mechanics, live hyperlinks/bookmarks in standardized reports, CSA Star
  Level 1 / TX RAMP certifications.
- Watermark: per-accreditor use-case marketing (HLC/SACSCOC/MSCHE/WASC/NWCCU/NECHE), AI
  "Assessment Catalyst Toolpack", suite bundling (1,500+ institutions claim).
- Nuventive: dual-panel plan+resource UI, Canvas data integration marketing.
- Institution-side suites' claims (e.g., "50% reduction in self-study preparation time") are
  vendor testimonials, not operational facts.

## Vendor-specific Findings

See L3. None of these promoted to the canonical model.

## Rejected Findings

- **"Accreditation management = institution-side self-study authoring."** Rejected as the
  definition of *this* leaf: the largest marketing volume uses the phrase this way (higher-ed
  institutional-effectiveness suites), but that seat is already covered by §11 (generic seeker
  side) and belongs to §23 (education seeker side) — and the market itself ships separate
  products for the two seats (Weave Education vs Weave Accreditation).
- **"Accreditation management = individual certification management."** Rejected: population
  differs (organizations vs persons); OpenWater runs both but distinguishes accreditation
  (organizations) from certification (individuals/programs) on the same page.
- **"Same as awards/grants review."** Rejected: shared machinery, different outcome — a standing
  status with validity and recurring obligations vs one-shot recognition/payment.
- **"Accreditation directories/registries are core."** Not confirmed in reachable sources; not
  included.
- **"Site-visit logistics are core."** Not observed in reachable sources; left as uncertainty.

## Boundary Findings

1. **vs §11 Accreditation / Certification Management** — the two leaves are the two seats of one
   relationship. §11 manages the *seeking organization's* compliance posture toward an external
   standard (controls/evidence/assessment/credential). This leaf manages the *program that
   awards* such standing. Structural test: whose workflow does the system run — if the user is
   the body receiving and deciding applications and maintaining accredited members, it is this
   leaf; if the user is the organization preparing its own evidence for someone else's standard,
   it is §11. Consistent with the §11 document, which lists the seeker-side variants and points
   outward for the operator side.
2. **vs §23 Academic Accreditation Management** — institution-side academic accreditation
   products (Watermark P&SS, Weave Education, Nuventive) are the counterpart of this leaf in the
   education domain. The market splits them into separate products by seat. §23 should anchor
   the institution side; flagged for joint review.
3. **vs §25 Certification Management (association)** — same intake→review→decision→credential
   machinery; the distinguishing axis is the credential population: organizations/programs
   (accreditation) vs individuals (certification). One sampled platform runs both from one
   codebase; several bodies operate both. Probable near-duplicate pairing to review when
   Certification Management is processed.
4. **vs §25 Standards Development Platform** — authoring/publishing standards (content work,
   drafting/comment/voting) vs operating a conformity program over published standards (this
   leaf). A standards body may run both.
5. **vs Grantmaking Platform / awards & abstract review tools** — same submission/review/
   decision machinery; distinguishing structure = standing organizational status with validity
   and recurring maintenance vs a one-shot award/payment. Also: grants move money; accreditation
   moves status.
6. **vs Membership Management System** — membership is ongoing belonging; accreditation is a
   status earned against standards and maintained through conformity. Heavy integration (SSO/
   lookup/pushback) because the accreditor's "members" are usually managed in an AMS — the
   systems interlock but are not the same Type.
7. **vs Government Licensing Management** — government permission to operate (mandatory) vs
   voluntary recognition by a standards body; different issuing authority and object.

## Historical / Market-Sample Check (§24-style)

Would older or differently positioned products still fit the L0? Accreditation programs
predating this software ran on paper binders, spreadsheets, and email; the defining structure
(standards + participating organizations + evidence submission + review decision + standing
status with recurring obligations) is era-independent. A homegrown accreditor database or an
AMS certification module that only manages *individual* credentials fails the L0 population
test — correctly excluded. The abstract "review platform" (awards/grants) fails the standing-
status test — correctly excluded. The definition does not depend on the current
education-accreditor dominance of the marketing term.

## Uncertainties

1. Whether large accreditors (e.g., national education accreditors, healthcare accreditors)
   run commercial products of this Type or homegrown systems — market-structure uncertainty;
   sampled vendors claim accreditor customers but specific large-body deployments were not
   verified.
2. Public registry/directory of accredited organizations as an in-product capability — not
   observed in reachable sources.
3. Site-visit / on-site evaluation logistics inside the system — not observed; may be handled
   offline or in vertical products.
4. Decision-vocabulary conventions (probation/deferral/show-cause etc.) are product- and
   body-specific (OpenWater documents custom decision types); no industry-standard state
   machine asserted.
5. Typical cycle cadences (e.g., years between reaccreditation) — not documented in reachable
   sources; deliberately not asserted in the final document.
6. WizeHive and Submittable (both plausible additional accreditor-side samples) were
   unreachable (HTTP 403); the cross-product base for accreditor-side B-level findings is two
   products, plus generic-machinery confirmation from OpenWater's help center.

## Final Synthesis

"Accreditation Management" in the directory's association/membership context is best
understood as the **accrediting body's program-management application**: it runs a named
accreditation program defined by published standards, manages participating organizations
through application and evidence submission, coordinates human review and records decisions,
and maintains each organization's accreditation status as a standing state across recurring
reporting and renewal cycles. Its machinery overlaps heavily with application/review platforms
and with association certification management; what makes it this Type is the combination of
standards-structured organizational evidence, a recorded human decision, and a maintained
status with a recurring cycle. The institution-side "accreditation management" market is the
opposite seat of the same relationship and belongs to the adjacent leaves (§11/§23).
