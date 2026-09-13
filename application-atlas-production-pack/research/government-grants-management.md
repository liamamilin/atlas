# Research Notes — Government Grants Management

## Research Goal

Understand how software supports a government agency acting as a **grantmaker** (funder of public funds): how it defines funding programs, receives and evaluates applications, makes awards, and administers the awarded money and recipient performance through to closeout. Produce a vendor-neutral Application Document.

## Initial Boundary

- **What this leaf is:** agency-side (grantor/funder) management of public grant programs — pre-award (opportunity → application → review → award) and post-award (agreement → payments → reporting → closeout).
- **Likely confusions:**
  - Grantmaking Platform (§25) — foundation/nonprofit funder side; same machinery, different operator/regulatory context.
  - Government Procurement Platform — agency *buys* goods/services; grants *give* funds for a public purpose.
  - Public Financial Management System — government-wide budgeting/accounting, not per-award lifecycle.
  - Research Grant Management (§23) / Nonprofit Grant Management (§25) — **recipient** side of the same relationship.
  - Permit Management / Government Licensing — application→decision loop but no money commitment or performance period.
  - Submission-management platforms (Submittable-class) — intake-first, multi-vertical; realize the pre-award stages.
- **Initial hypothesis:** the defining structure is the award as a *managed commitment of public funds to a selected recipient under terms*, wrapped by a defined funding opportunity on the front end and administered execution (money + performance) to closeout on the back end.

## Research Questions

1. What are the core objects? (funding opportunity, application, review, award, budget, payment, report, amendment, closeout)
2. How does the pre-award workflow flow, and who performs each step?
3. How does the post-award (administration) side work — money and performance?
4. What roles exist on the agency side and the external side?
5. What rules/constraints shape behavior (eligibility, caps, deadlines, audit, transparency)?
6. What distinguishes a *government* grants system from a general/foundation grantmaking system?
7. Which capabilities are common mature structure vs variant vs vendor-specific?
8. What would older/regional (pre-portal, non-US) grant practice still require for the Type to hold?

## Representative Products

| Product | Why chosen | Angle |
|---|---|---|
| **Euna Grants** (Euna Solutions; AmpliFund + eCivis heritage) | purpose-built public-sector grants suite; sells maker + seeker + recipient sides; state/local/federal customers | full lifecycle, gov terminology (NOFO/RFP/NOFA) |
| **Submittable** | cross-vertical submission/grants platform heavily used by government agencies; intake-first philosophy | pre-award depth + funds tracking |
| **Foundant Grant Lifecycle Manager (GLM)** | funder-side lifecycle platform (foundations, community foundations, government organizations) | request lifecycle: LOI→application→evaluation→decision→installments→follow-ups |

Historical/market-sample breadth anchors used in reasoning: pre-digital agency grantmaking practice (paper NOFOs, review panels, award letters, installment ledgers, paper progress reports); non-US regional grant vocabulary (NOFA, RFP, subsidy/tender terminology).

## Sources

**Euna Grants (AmpliFund)**
- https://eunasolutions.com/ — Grants Management Software for Public Sector (positioning; compliance/transparency claims; FAQ) [Tier 2]
- https://eunasolutions.com/solutions/grants/maker/ — Grant Maker product page (CREATE/MONITOR/AWARD stages; award & recipient management; compliance oversight) [Tier 2]
- https://grants-help.eunasolutions.com/ — Euna Grants Support hub [Tier 1]
- https://grants-help.eunasolutions.com/hc/en-us/categories/4816097290003 — Grant Maker Training (module map: Master Data, Fund, Opportunity, Application, Workflow/Scoring, Award, Payment Requests, Amendments, Closeout) [Tier 1]
- https://grants-help.eunasolutions.com/hc/en-us/articles/360056160434 — "What is an Opportunity?" (opportunity = chance for funding: competitive / non-competitive / continuation; aka RFP/NOFA/NOFO; linked to funding source; applicant portal) [Tier 1]
- https://grants-help.eunasolutions.com/hc/en-us/articles/42982238636563 — Grant Maker Award Closeout (budget tracking, centralized documentation, performance reporting at closeout) [Tier 1]
- https://grants-help.eunasolutions.com/hc/en-us/articles/3393858 — (Submittable equivalent: Funds Tracking, see below)

**Submittable**
- https://help.submittable.com/ — help center map (Build Your Program / Manage Your Processes / Report on Your Impact / Help for Applicants) [Tier 1]
- http://submittable.help/en/collections/3957059 — Manage Your Processes (88 articles: review workflows, statuses, additional forms, agreement requests, funds) [Tier 1]
- http://submittable.help/en/articles/3393858-funds-tracking — Funds Tracking: Fund → Award → Payment; payment capped at awarded amount; transaction export [Tier 1]
- http://submittable.help/en/articles/924162-progress-reports — (team review progress; grantee reporting lives in Additional Forms) [Tier 1]

**Foundant**
- https://www.foundant.com/ — products (GLM, SmartSimple, GivingData); government solution page [Tier 2]
- https://www.foundant.com/solutions/grant-management-software-for-government/ — Government Organizations solution (applications/reviews, cross-departmental workflows, budget/disbursement dashboards, financial transparency for auditors/public) [Tier 2]
- https://support.foundant.com/hc/en-us — Support Hub [Tier 1]
- https://support.foundant.com/hc/en-us/categories/1500001292601 — GLM category structure: Request Lifecycle; LOI and Application Stages; Evaluations; Decisions; Installments and Payments; Follow Ups; Eligibility; Organizations; Users and Roles; Universal Application; DocuSign; Bill.com; Data Visualization [Tier 1]

**Domain context**
- https://www.grants.gov/... — **unreachable (403, 2 attempts on 2026-09-07)**. Federal lifecycle terminology therefore rests on vendor documentation (Euna explicitly glosses Opportunity as NOFO/NOFA/RFP) rather than the government's own pages.

## Product Observations

### Euna Grants (AmpliFund / eCivis heritage) — evidence layer A

- Public-sector positioning: "purpose-built for government and public sector"; suite = Budget / Grants / Payments / Procurement / Supplier Network; customers include state agencies (Arizona), counties (Mariposa County, CDBG programs), CA HCD.
- Splits the domain into **Grant Maker** (funder side), **Grant Seeker** (agency applying for external funds — includes a funding-opportunity research layer, "25K+ grants in the network"), and **Recipient/Applicant** roles. FAQ explicitly states both makers and seekers "can apply, track, and report, all within one connected solution" (pass-through posture).
- **Grant Maker object chain (from training curriculum):**
  - **Master Data** — Organizations and Individuals; Departments; Budget Categories; Staff and Users; Purpose Areas.
  - **Fund** — "What is a Fund", "Fund Financials", "Fund Tools"; opportunities draw funding from funds.
  - **Opportunity** — "a chance for funding; could be competitive, non-competitive or continuation"; record carries agency details, award information, submission information; other orgs call it RFP / NOFA / NOFO; created under Program Management; visible to applicants on the Applicant Portal.
  - **Application** — configurable application forms (3-part configuration series), budget template, eligibility rules / required fields / attachments; testing and publishing; applications routed automatically for review and scoring.
  - **Workflow / Scoring** — review workflow configuration, assigning users to workflow, enrolling and scoring; reviewer fields; multi-round scoring; reviewer scoring training; Opportunity Scoring Report.
  - **Award (post-award)** — Award Creation, Award Configuration, Post-Award Budget; track awards, budgets, allocations; store signed agreements and compliance documents; recipient self-service access.
  - **Money** — Approving and Rejecting **Payment Requests**; Advanced Payments overview.
  - **Change** — Approving and Rejecting **Amendments**.
  - **Compliance** — Tasks and reminder tracking to "maintain compliance with reporting deadlines".
  - **Closeout** — "Streamline your Award Closeout Process": budget tracking, centralized documentation, performance reporting.
- Marketing/positioning claims (Tier 2, treat as positioning not operations): FOIA-ready audit trails, public transparency tools, ERP integrations, dashboards with milestones/payments/deliverables, "30% increase in drawdown" style metrics (not asserted in final doc).

### Submittable — evidence layer A

- Cross-vertical submission platform ("Build Your Program / Manage Your Processes / Report on Your Impact") with a large government-agency customer base; strong help center.
- **Programs/Projects** collect **submissions**; submission states include New → In-Progress, then Accept/Decline (bulk actions supported); archive/unarchive; draft submissions; allow submitter to edit a submission; manually enter submissions (offline intake).
- **Review machinery** — review workflows (set up per project), manual / randomized / group assignments, multi-stage reviews, custom review forms, automated scoring for forms, reviewer reminders and reviewer workload dashboard, **concealing applicant information from reviewers** (blind review), shareable reviews.
- **Post-acceptance** — **Request Agreement feature when accepting a submission** (agreement step at acceptance); **Additional Forms**: scheduled follow-on forms sent to submitters (progress/financial reports), with deadlines, reminders, submitter-edit permission, collaboration; tracking of additional forms.
- **Funds Tracking** — three-level money model: **Fund** (how much money can be distributed) → **Award** (how much of the Fund is assigned to an awardee, drawn against a chosen Fund showing available balance) → **Payment** (how much of the Award has been paid); payments cannot exceed the awarded amount; transactions exportable to CSV with fund, amount, status, submitter, submission, program, date, description; deleting a fund does not delete award/payment data already recorded on submissions.
- Roles — permission levels (documented numeric ladder 1–5) + custom roles; messaging with submitters; labels; calendar; reporting/impact dashboards; API.
- Applicant side documented separately ("Help for Applicants", 63 articles).

### Foundant Grant Lifecycle Manager (GLM) — evidence layer A (section structure) + B

- Funder-side lifecycle platform; sold to grantmaking foundations **and** "Government Organizations" (dedicated solution page; customers incl. state library, wildlife agency, cities); sibling products: SmartSimple (enterprise configurable, incl. research & government), GivingData, CommunitySuite (fund accounting).
- **Request lifecycle** is the organizing spine: a request (application) moves through **process stages** — help sections for **LOI and Application Stages** (letter of intent before full application), **Evaluations** (evaluators incl. external reviewers and board members), **Decisions** (award/decline), **Installments and Payments** (paying an approved grant in installments; Bill.com integration), **Follow Ups** (post-award reporting requirements from grantees).
- **Eligibility** — dedicated section: eligibility quizzes, testing/management, new **cycle preparation** (recurring grant cycles).
- **Organizations** — applicant organization records; applicant access; **due diligence charity checks** (funder-side vetting — philanthropic flavor).
- **Agreement/award paperwork** — DocuSign integration; merge templates/documents for award letters and notifications; third-party requests/responders (e.g., fiscal sponsors).
- **Universal Application** — a variant where multiple funders share one application (cross-funder standardization).
- Users and roles: admin/grants-manager permissions; applicant, evaluator, board-member resources.
- Reporting: build/run reports, data sets, dashboards, data visualization with fiscal-year handling; AI application analysis / AI summary (era-typical).

## Cross-product Comparison

| Structure | Euna Grants | Submittable | Foundant GLM | Strength |
|---|---|---|---|---|
| Defined funding offer (program/opportunity) | Opportunity (competitive/non-competitive/continuation; NOFO/RFP/NOFA), linked to Fund | Project/program (generic container) | Process built around opportunities/forms incl. LOI stage | B — present in all, most grant-explicit at Euna/Foundant |
| Application from external party | Configurable application, published to Applicant Portal | Submission (with statuses, drafts, edits) | Request through LOI → Application stages | B |
| Review / evaluation workflow | Workflow + scoring, multi-round, reviewer fields | Review workflows, assignments, multi-stage, blind review, custom review forms | Evaluations (evaluators, board members) | B |
| Selection decision | (implied via workflow → award) | Accept/Decline (bulk) | Decisions | B |
| Award as fund commitment | Award object w/ post-award budget; agreements stored | Award (amount from Fund) + Request Agreement at acceptance | Decision → grant with Installments & Payments | B |
| Fund/funding-source ledger | Fund w/ financials; opportunities draw funding | Fund → Award → Payment; balance visible | (fund accounting in sibling CommunitySuite; GLM handles installments) | B (2 direct) |
| Payment/disbursement | Payment Requests (approve/reject); advanced payments | Payments against Award, capped at award amount | Installments & Payments; Bill.com | B |
| Recipient performance reporting | Tasks/reminders for reporting deadlines; milestones | Additional Forms (scheduled, reminders) | Follow Ups | B |
| Award modification | Amendments (approve/reject) | — | — | A — product-specific |
| Closeout | Award Closeout documented | — | — | A — product-specific (plausible common in gov practice, kept cautious) |
| Eligibility handling | eligibility rules/required fields on application | (guidelines/labels; less explicit) | Eligibility quizzes + cycle prep | B (2 direct) |
| Agreement execution | signed agreements stored in hub | Request Agreement feature | DocuSign integration | B |
| External applicant/recipient portal | Applicant Portal; recipient self-service | Applicant hub (63 articles) | Applicant access + resources | B |
| Reviewer pool incl. external reviewers | Reviewer scoring training | Reviewer invites/assignments | Evaluator & board member resources | B |
| Seeker side (agency applying for funds) | Grant Seeker module + opportunity research network | — | — | A — product-specific |
| Recurring cycles | (implied) | — | New Cycle Preparation | A/B |
| Public transparency surfaces | "public transparency tools built-in" (marketing) | public project pages | gov page: "financial reports for … the public" | B-weak |
| Cross-department/finance integration | ERP integrations (positioning) | API, Zapier | CommunitySuite sync; Bill.com | B-weak |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant (deliberately small)

A Government Grants Management application is recognizable when **all four** hold:

1. **The funding program / opportunity** — a defined, published offer of grant funds carrying its rules (who is eligible, what money is available, on what terms and period). Remove → ad-hoc payments or contracts, not a grant program.
2. **Applications from external parties under that program** — parties outside the agency ask for the funds through the system (or through records the system manages). Remove → internal budgeting/payment machinery.
3. **The award as a commitment of public funds to a selected recipient under terms** — a persistent, identified award record (recipient, amount, period, conditions) produced by a recorded selection decision. Remove → an application/review (intake) platform.
4. **Administered execution to a managed end** — the award's life is tracked against money and/or required performance (disbursements, recipient reports, modifications) until it is formally completed (closeout). Remove → a grant CRM or discovery tool.

Historical check (pre-portal, pre-digital, non-US): a paper-era agency ran NOFOs (published notices), received applications, review panels scored them, award letters committed funds, treasuries disbursed in installments, recipients filed paper progress reports, files were closed out. All four invariants hold without any portal, e-signature, or digital money. Regional grants/subsidy schemes fit the same abstract shape with different vocabulary. → definition survives.

### L1 — Common Mature Structure

- Fund / funding-source ledger that awards draw down (2 of 3 direct; third via sibling product)
- Eligibility screening (rules on applications; quizzes)
- Reviewer/scoring workflow: assigned reviewers, scoring rubrics/forms, multi-stage and multi-round review, internal + external reviewer pools
- Budget collection and approval (applicant budgets, budget categories)
- Award agreement/letter generation with signature capture (in-platform agreement requests, e-signature integrations, stored signed documents)
- Recipient performance reporting via scheduled forms with reminders and deadline tracking
- Payment execution in some form (payment requests, installments, capped payments) — often in coordination with an external financial system
- Roles and permissions; audit trails; records retention posture
- Reporting/dashboards (scoring, funds, performance); public transparency surfaces
- Distinct surfaces: agency back office, public application portal, reviewer surface, recipient/awardee portal

### L2 — Variant / Optional

- Seeker side: the same agency also *applying* for funds (grant discovery, deadlines) — product-specific today, structurally plausible for any pass-through agency
- Opportunity kinds: competitive vs non-competitive vs continuation/formula awards
- Scale: single-program office ↔ statewide enterprise (multi-department master data) ↔ federal
- Pass-through structure: federal→state→local chains (subrecipient monitoring flavor)
- Blind review; multi-round scoring
- Closeout formality (documented at one product)
- Emergency/rapid-response grant programs
- Payment rails: in-platform payments vs handoff to financial system vs payment-service integration
- Recurring grant cycles with per-cycle preparation
- Cross-funder universal applications
- Regional vocabulary: NOFO/NOFA/RFP; grant vs subsidy vs tender terminology
- Funder-side vetting tools (charity-status due diligence — philanthropic-flavored)

### L3 — Vendor-specific (research notes only)

- Euna: "25K+ grants" research network; Purpose Areas; Departments master data; Grant Maker/Seeker/Recipient packaging; iorad-based tutorials; specific claims (30% drawdown increase, 72% admin-time reduction) — marketing numbers, not asserted.
- Submittable: numeric permission levels 1–5; 1099-K handling for fee-based projects; literary-magazine vertical; free-submission limits.
- Foundant: GLM/SLM sibling pairing; Compass community; Universal Application program; Candid integration on forms; CommunitySuite sync; Bill.com; DocuSign; AI Application Analysis/AI Summary.

## Vendor-specific / Rejected Findings

- **Rejected as definitional:** grant-opportunity discovery databases (product-specific); FOIA-specific audit language (regional US positioning); numeric marketing metrics; AI summaries; 1099 handling; universal applications; advance payments.
- **Kept as variants:** multi-round scoring, blind review, closeout, amendments, seeker side.
- Anti-overfitting note: all three sampled products are cloud SaaS with portals — portals are implementation, not invariant (paper-era practice satisfies the core).

## Boundary Findings

- **vs Grantmaking Platform (§25):** the funder-side machinery is one market family — Foundant and Submittable sell to both philanthropic and government funders; Euna also serves nonprofits. The distinguishing context is the operator (government agency distributing **public** funds under statutory process: formal notices, eligibility law, audit exposure, public transparency). Structure alone does not separate them cleanly → **taxonomy question worth joint review**; keeping both leaves per directory.
- **vs Government Procurement Platform:** procurement = agency buys goods/services; the counterparty is paid in exchange for deliverables; selection by bid rules. Grants = agency gives funds for a public-purpose project the recipient undertakes; selection by eligibility/merit; money is a contribution under conditions, not a purchase price. The application→review→award→payment skeleton is shared; the *nature of the obligation* differs.
- **vs Public Financial Management System:** PFM manages government-wide budgets/ledger; grants management manages the per-award lifecycle and connects to the financial system (ERP integration seam).
- **vs Research Grant Management / Nonprofit Grant Management:** those are the **recipient** side of the same funding relationship (managing received grants), not the funder side.
- **vs Permit Management / Government Licensing:** both run application→review→decision loops, but neither commits money or imposes a performance/reporting period; permits regulate, grants fund.
- **vs Submission-management platforms:** an intake platform used for a grant program realizes L0 #1–2 (and optionally #3); it becomes full Grants Management when award administration (money + reporting to closeout) is in scope — Submittable crosses that line via Funds Tracking/Additional Forms, which is exactly why it qualifies as a representative product.
- Removal test for the Type: strip the post-award administration → grant application/review platform (intake tool); strip the opportunity/program layer → payment system; strip external applicants → internal budgeting. The leaf holds as a distinct Type.

## Uncertainties

- Grants.gov (and federal-side official lifecycle pages) unreachable (403 ×2) — federal terminology rests on vendor docs; no precise federal process details asserted.
- State-enterprise systems (e.g., IntelliGrants/IGX-class, statewide deployments) not directly examined (no reachable operational docs); their inclusion rests on vendor positioning and customer testimonials (Arizona statewide quote).
- Exact status ladders for awards (active/suspended/closed etc.) vary by product; no universal state names asserted.
- Closeout formality directly documented at one product only; treated as product-documented pattern (common in government practice per vendor positioning, asserted cautiously).
- Public transparency surfaces documented mainly via Tier-2 positioning pages; kept at moderate strength in the final document.
- Submittable's government market share asserted only weakly (its help center does not name government customers; government use is supported by its own marketing and third-party knowledge — final doc does not depend on it).

## Final Synthesis

The Type is best modeled as: **a government agency's system of record for running grant programs with public funds — from a defined funding opportunity, through applications and a recorded selection, to an awarded commitment that is then administered (money and performance) through to formal closeout.** The defining core is small (opportunity → application → award → administered execution); everything else in modern products (funds ledgers, scoring workflows, portals, reminders, dashboards, transparency surfaces) is mature but not definitional. The government flavor is carried less by structure than by context: public money, statutory process, and audit/transparency obligations.
