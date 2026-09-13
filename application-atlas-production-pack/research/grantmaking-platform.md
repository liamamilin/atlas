# Research Notes — Grantmaking Platform

## Research Goal

Understand how software supports a **philanthropic funder** (private/family/community foundation, corporate giving program, charity, or government grantmaker using the same machinery) running its grantmaking: defining grant programs, receiving and evaluating requests, deciding, and administering awarded grants (money + follow-up reporting) through to completion. Produce a vendor-neutral Application Document. This pass also carries the **joint review** flagged by the government-grants-management pass (2026-09-07).

## Initial Boundary

- **What this leaf is:** funder-side grant machinery for philanthropic/charitable funders — pre-award (program → request → review → decision) and post-award (grant → installments/payments → follow-ups → close).
- **Likely confusions:**
  - **Government Grants Management (§24)** — same funder-side machinery, government operator of public funds; joint review flagged.
  - **Nonprofit Grant Management (§25, unprocessed)** — recipient side (nonprofit managing grants it receives).
  - **Research Grant Management (§23)** — institution research administration (recipient side); note SmartSimple sells a "Research Grants Management" solution for research *foundations* (funder pole) — segment overlap to note, not a taxonomy conflict.
  - **Donor Management System (§25, processed)** — money **in** (donations) vs money **out** (grants).
  - **Fundraising Management Platform** — campaign machinery for raising money.
  - **Nonprofit Fund Accounting** — the money-pool ledger; grantmaking platform tracks the grant lifecycle and integrates with it.
  - **Submission Management Platform** — intake-only tools; boundary specimen (Submittable).
  - **Financial Aid Management (§23, processed)** — institution-side student aid; the scholarship variant of grantmaking (individuals as recipients) is its cross-domain cousin.
- **Initial hypothesis:** the defining structure is the same four-part chain as the government sibling (program → request → award → administered execution), with the operator context (philanthropic funds, board/donor governance) as the seam — to be tested.

## Research Questions

1. What are the core objects? (program/process, request, evaluation, decision, grant/award, installment, payment, follow-up, grantee organization)
2. How does the request lifecycle flow, and which stages are required vs optional?
3. How is the post-award side handled — money (installments/payments) and performance (follow-ups)?
4. What roles exist on the funder side and the external side?
5. What is philanthropic-specific vs generic grant machinery? (charity due diligence, fiscal sponsors, scholarships, donor-advised/community-foundation structures, relationship management)
6. What distinguishes a grantmaking platform from a government grants system — structure or operator context?
7. Which capabilities are common mature structure vs variant vs vendor-specific?
8. Would pre-digital foundation grantmaking (paper proposals, board votes, check ledgers, paper reports) still satisfy the definition?

## Representative Products

| Product | Why chosen | Angle | Evidence layer reached |
|---|---|---|---|
| **Foundant Grant Lifecycle Manager (GLM)** | community foundations & mid-size funders; request-lifecycle philosophy; strongest public help center | full lifecycle spine + state model | **A (Tier 1)** — support hub articles fetched |
| **Blackbaud Grantmaking** | enterprise/large foundations; GIFTS heritage; CRM-centric philosophy | relationship + multi-entity + compliance | **B (Tier 2)** — product page; Tier 1 unreachable |
| **Fluxx (Grantmaker)** | large foundations (Ford, MacArthur, Knight); data-platform philosophy; also sells Grantseeker + government | end-to-end lifecycle + BI | **B (Tier 2)** — product/FAQ pages; support portal unreachable |
| **SmartSimple Cloud (Grants Management)** | highly configurable platform; multi-sector (philanthropy + government + research + CSR) | configurability pole; boundary-relevant | **B (Tier 2)** — solution pages; wiki 403 |
| **GivingData** | foundations; trust-based/relationship philosophy; now part of Foundant family | CRM + impact pole | **B (Tier 2)** — home page |
| **Submittable** | intake-first cross-vertical platform used by funders and agencies | **boundary specimen** (intake vs full grantmaking) | **A (Tier 1)** — inherited from government-grants-management pass (2026-09-07) |

Market-structure note: Foundant, SmartSimple, and GivingData are now one family ("by Foundant"); Blackbaud and Fluxx are the other major independent poles; Submittable is the cross-vertical intake platform. The sample therefore covers the market's real consolidation while keeping distinct philosophies (lifecycle / CRM / data-platform / configurability / intake-first).

## Sources

**Foundant (Tier 1, fetched 2026-09-08)**
- https://support.foundant.com/hc/en-us — Support Hub
- https://support.foundant.com/hc/en-us/categories/1500001292601-Grant-Scholarship-Lifecycle-Manager — GLM & SLM category (section map: Request Lifecycle; LOI and Application Stages; Evaluations; Decisions; Installments and Payments; Follow Ups; Eligibility; Organizations; Users and Roles; Processes; Communications; Universal Application; Integration with CommunitySuite; Reports and Data Sets; Advanced Features)
- https://support.foundant.com/hc/en-us/articles/4404567889303-Request-Status-Definitions — full request status ladder
- https://support.foundant.com/hc/en-us/articles/4404190708247-Process-Stages — five process stages; Application + Decisions required
- https://support.foundant.com/hc/en-us/articles/40669080674455-Follow-Ups-Overview — follow-up machinery (assignment, due dates, sequential logic, evaluation by license tier)
- https://support.foundant.com/hc/en-us/sections/8427564460823-GLM-SLM-Admin-Installments-and-Payments — money model article map (Multi-Year Grant Workflows; Budgeting Tool; Payment Tracking; Enter a Payment; Add/Edit/Remove/Cancel Installments; Decrease Amount Awarded; Batch Import Payments; Credit/Delete a Payment)
- https://support.foundant.com/hc/en-us/sections/40133284905495-Due-Diligence-Charity-Checks — Candid Charity Check, Ajah, Capture Fiscal Sponsor Information
- https://www.foundant.com/ — product family (GLM, SmartSimple, GivingData, CommunitySuite)

**Blackbaud (Tier 2, fetched 2026-09-08)**
- https://www.blackbaud.com/products/blackbaud-grantmaking — product page (lifecycle, grantee portal, review portal + scoring rubrics, payment schedules, CRM positioning, multi-entity, audit, Candid + CSI WatchDOG integrations)
- Tier 1 NOT reachable: https://webfiles.blackbaud.com/files/support/helpfiles/grantmaking/content/home.html and https://kb.blackbaud.com/knowledgebase both returned JS shells (2 attempts) — recorded as source-access limitation.

**Fluxx (Tier 2, fetched 2026-09-08)**
- https://www.fluxx.io/ — positioning (Grantmaker + Grantseeker; foundations/government/nonprofits; case studies)
- https://www.fluxx.io/products/grantmaker-fluxx-grants-management-software — product page + FAQ (full lifecycle: applications, reviews, approvals, payments, compliance, reporting, impact measurement; grantee portals; grantee relationship management; due diligence/eligibility)
- Tier 1 NOT reachable: https://support.fluxx.io/hc/en-us — transport error (1 attempt) — recorded as source-access limitation.

**SmartSimple (Tier 2, fetched 2026-09-08)**
- https://www.smartsimple.com/ — solutions map (Grants Management; Government Funding; Research Grants Management; CSR; Salesforce edition); Foundant-family stats
- https://www.smartsimple.com/solution/grants-management-tracking-software — grants solution page (application building, review collaboration, budgets/financial oversight, e-signature, finance integrations, product-family comparison chart)
- Tier 1 NOT reachable: https://wiki.smartsimple.com/ — 403 (1 attempt) — recorded as source-access limitation.

**GivingData (Tier 2, fetched 2026-09-08)**
- https://www.givingdata.com/ — positioning (relationships, grants lifecycle, grantee collaboration, impact tracking; foundation customers)

**Submittable (Tier 1, inherited from government-grants-management pass, 2026-09-07)**
- https://help.submittable.com/ ; http://submittable.help/en/collections/3957059 (Manage Your Processes); http://submittable.help/en/articles/3393858-funds-tracking (Fund → Award → Payment); Additional Forms (scheduled post-award forms); review workflows (assignments, blind review, multi-stage)

## Product Observations

### Foundant Grant Lifecycle Manager (GLM) — evidence layer A

- **Request lifecycle is the organizing spine.** Help sections: LOI and Application Stages → Evaluations → Decisions → Installments and Payments → Follow Ups. A "request" is the unit that moves through the process.
- **Process = configurable grant program.** "Process stages are the distinct stages a request for funding may go through. There are five stages: Eligibility, LOI, Application, Decisions, and Follow Ups. The administrator can choose which stages to include in a process, but the Application and Decisions stages are required to be set up in each process." Eligibility, LOI, Follow Ups are toggleable; per-stage form due dates, automatic emails, evaluator assignment. "Auto Configure Installments" exists at process level.
- **Request status ladder (direct observation):** LOI Draft → LOI Submitted → LOI Complete → Application Draft → Application Submitted → Application Complete → Evaluations Assigned → Evaluations Closed → (Denial Draft → Denied) or (Approval Draft → Approved) → Follow Up(s) Assigned → Closed; plus Abandoned. Approved workload pages: "Approved" (no follow ups) vs "All Open Approvals". Follow-up forms carry their own statuses (draft / submitted / complete) surfaced as workload pages.
- **Money model:** approved request → **installments** (scheduled; add/edit/remove/cancel; auto-configure) → **payments** recorded against them (enter, batch import, credit, delete); "Decrease the Amount Awarded" as a governed adjustment; **Budgeting Tool**; **Multi-Year Grant Workflows**; **Bill.com Integration** for payment execution.
- **Follow-ups (post-award reporting):** forms built in processes/universes, assigned to approved requests (individually or in batch) during or after approval; due dates; attachable to the overall award **or to a specific installment**; reassignable to another contact at the grantee organization; submission logic sequential-by-due-date (default) or open; admin marks complete / reverts one step; evaluation options vary by license tier (internal assignment to grants managers, board members, evaluators at Advanced tier); overdue follow-up reporting.
- **Organizations (grantee records):** standing organization records with applicant access; **Due Diligence Charity Checks** — run a **Candid Charity Check** (charity-status fields), **Ajah** (Canadian charity data), **Capture Fiscal Sponsor Information**.
- **Communications:** email templates, merge fields, notifications, interactions, **Third Party Requests / Third Party Responders** (e.g., fiscal sponsors acting for the applicant), **DocuSign Integration**, merge templates/documents (award letters).
- **Eligibility:** dedicated section — eligibility quizzes, testing/management, **New Cycle Preparation** (recurring cycles).
- **Forms:** form builder (question types, tables, advanced features), **Decision Stage Forms**, **Candid Integration on Forms**.
- **Users and Roles:** Grants Manager permissions, user roles; **Evaluator & Board Member Resources** (external reviewers and board as first-class roles).
- **Universal Application:** a cross-funder shared-application variant with its own full section (opportunities, eligibility, evaluations, decisions and installments, follow ups).
- **Integration with CommunitySuite** (sibling fund-accounting product): Sync Grants, Sync Scholarships, Sync Organizations and Users; article "Fiscal Sponsor Recommendations: GLM and CommunitySuite".
- **Advanced:** Data Visualization (fiscal-year handling), Dashboards, Reports and Data Sets, **AI Application Analysis**, **AI Summary**.
- Sibling product **SLM** (Scholarship Lifecycle Manager) shares the machinery with individuals as applicants/recipients ("applicants and scholarship recipients" in Follow Ups Overview).

### Blackbaud Grantmaking — evidence layer B (Tier 2 only)

- Positioning: "manage the full grant lifecycle—from application to award to reporting"; "from accepting online applications to assessing and communicating outcomes—all in one purpose-built tool".
- **Grantee portal** — "design a simple application process using the grantee portal to streamline communication between grantees and funders".
- **Central review portal** — "for funders and external stakeholders to manage the application review process and provide feedback with custom scoring rubrics".
- **Payment schedules** — "tools to create and manage payment schedules and generate one-click budget reports".
- **CRM positioning** — "all-in-one CRM and grant management software"; "Manage relationships, not just applications. Data and documents from application forms feed directly into your records."
- **Multi-entity** — "Oversee more than one grantmaking entity, while keeping data, reporting, and access separate."
- **Compliance/audit** — auditing capabilities track modifications; user permissions; GDPR posture.
- **Integrations** — **Candid** (verify tax status), **CSI WatchDOG** (watchlists), Raiser's Edge NXT (grant info for development teams).
- Reporting/dashboards shared with "board members and committees".
- Marketing metrics (50 days/year, 30%, 10x) — positioning only, not asserted.

### Fluxx Grantmaker — evidence layer B (Tier 2 only)

- FAQ (direct quote): "cloud-based grants management software platform used by foundations and government agencies to manage the full grant lifecycle, including **applications, reviews, approvals, payments, compliance, reporting, and impact measurement**."
- "end-to-end solution for grants management - from the funding announcement stage, all the way through measurement and evaluation of grants programs".
- **Grantee portals** — "personalized, collaborative grantee portal… your branded one-stop shop for all projects, outcomes, and relevant financials."
- **Grantee relationship management** — "Grantmaking is about relationships and people, but also about organizational due diligence and eligibility… verify and match the right grantees to your programs."
- Role-based dashboards/workspaces; **Fluxx Data Core**; **Grantelligence** BI layer; integrations; **Finn** AI assistant.
- Serves private foundations, government agencies, nonprofits; also sells **Grantseeker** (seeker side) — the two-sided packaging.
- Case studies span foundation (Jessie Ball duPont Fund), nonprofit grantmaker (United Way of Greater Atlanta), government agency (Texas Veterans Commission) — the family-overlap evidence again.
- Marketing numbers ($39B+, 200,000+ grantees, "7000+ visualizations") — positioning only, not asserted.

### SmartSimple Cloud (Grants Management) — evidence layer B (Tier 2 only)

- "From crafting applications and reviewing submissions to tracking budgets, manage the entire grant process."
- **Applicant relationship view** — "360° view of a applicant's history with your foundation"; tracked email correspondence; individual or "blast" correspondence.
- **Workflows** — configurable; cross-department collaboration; **multi-year grants across programs**.
- **Applications and reviews** — application builder (auto-save, preview follow-up forms, rich text); auto-import of application/report data; "Engage external collaborators in the review process… review committees… shared access to applications, notes, and evaluations."
- **Financial oversight** — real-time analytics; financial reports for stakeholders; budget dashboards; audit trails (integrated financial management).
- **E-signature** — "electronic signing of grant agreements"; **finance systems integrations** — "streamline payment processes… grant disbursements are executed with precision" (Sage Intacct, QuickBooks, Xero class; documented schema for accounting integrations).
- Product-family chart (post-merger): **Foundant GLM** (smaller orgs; city/county agencies, family/private foundations), **GivingData** (CRM, forecasting, compliance; family/private/independent foundations), **SmartSimple Cloud** (enterprise; state agencies, research foundations, CSR organizations).
- Solutions: Grants Management (foundations/grantmakers), Government Funding (federal/state/local/tribal), Research Grants Management (research foundations and institutions), CSR (corporate/employee giving).
- Annenberg testimonial references **LOI forms**; workflow-driven intake growth.

### GivingData — evidence layer B (Tier 2 only)

- "purpose-built grants management system unites funders and grantees"; "Streamline the entire grants lifecycle"; "Connect, collaborate, and share information with your grantees in real-time"; "Track progress toward outcomes and grantmaking impact."
- Trust-based-philosophy positioning ("build trust-based relationships"); foundation customers (Rockefeller Brothers Fund, Houston Endowment, Overdeck Family Foundation, etc.).
- Now "GD by Foundant" — part of the Foundant family.

### Submittable — evidence layer A (inherited, 2026-09-07)

- Cross-vertical submission platform with a large funder/agency base; Programs/Projects collect **submissions** (statuses, drafts, edits, offline entry).
- **Review machinery:** review workflows, manual/randomized/group assignments, multi-stage, custom review forms, blind review (applicant info concealed), reviewer reminders/workload dashboard.
- **Post-acceptance:** Request Agreement at acceptance; **Additional Forms** — scheduled follow-on forms (progress/financial reports) with deadlines, reminders, submitter editing, collaboration.
- **Funds Tracking:** **Fund** (distributable pool) → **Award** (amount assigned to an awardee, drawn against a Fund with visible balance) → **Payment** (paid against the Award; capped at awarded amount); transaction export.
- Permission levels + custom roles; messaging; labels; reporting/impact dashboards; API.
- **Boundary reading:** with Programs + review + Accept/Decline alone it is an intake platform; with Funds Tracking + Additional Forms it crosses into grantmaking administration. Exactly the intake boundary the government pass flagged.

## Cross-product Comparison

| Structure | Foundant GLM | Blackbaud Grantmaking | Fluxx | SmartSimple | GivingData | Submittable | Strength |
|---|---|---|---|---|---|---|---|
| Defined grant program container | Process (5 stages; Application+Decisions required) | grant cycle configuration | funding announcement → programs | programs/workflows | grants lifecycle | Program/Project (generic) | B (5 direct; Submittable generic) |
| Request/application from grantseeker | Request (LOI → Application stages) | online applications via grantee portal | applications | application builder | applications | Submission | B (all) |
| LOI / intent stage | LOI stage (optional, first-class) | — (not evidenced) | — (not evidenced) | LOI forms (testimonial) | — | — | A/B (2 direct) |
| Eligibility screening | Eligibility stage + quizzes | Candid tax verification + watchlists (post-intake flavor) | due diligence & eligibility | customizable grant criteria | — | — | B (3–4) |
| Review / evaluation | Evaluations (evaluators, board members; scoring) | review portal, custom scoring rubrics, external stakeholders | reviews | review committees, shared access, external collaborators | collaboration | review workflows, blind review, multi-stage | B (all) |
| Recorded selection decision | Decisions (approve/deny with drafts) | award | approvals | decision in workflow | — | Accept/Decline | B (all) |
| Grant as committed award | Approved request + amount awarded | award | grant record | grant record | grant record | Award (drawn from Fund) | B (all) |
| Installments / payment schedules | Installments (add/edit/cancel; auto-configure; multi-year) | payment schedules | payments | budgets + disbursement via finance integrations | — | payments capped at award | B (4–5) |
| Payment execution rails | in-platform records + Bill.com | — (not evidenced) | payments (in lifecycle) | finance-system integrations (Sage Intacct/QuickBooks/Xero class) | — | in-platform records | B (rails vary; recording common) |
| Follow-up / post-award reporting | Follow Ups (assign, due dates, sequential logic, evaluate) | reporting stage of lifecycle | reporting, compliance | follow-up forms (preview/auto-import) | outcomes tracking | Additional Forms (scheduled) | B (all) |
| Grantee/applicant organization records | Organizations (standing records, history, applicant access) | CRM records ("manage relationships, not just applications") | grantee relationship management | 360° applicant history | relationships first | submitter records | B (all) — philanthropic emphasis |
| Grantee portal | Applicant access + resources | grantee portal | personalized grantee portals | applicant portal | grantee collaboration | applicant hub | B (all) |
| Agreements / award letters | merge templates + DocuSign; third-party responders | — (not evidenced) | — (not evidenced) | e-signature grant agreements | — | Request Agreement at acceptance | B (3) |
| Charity due diligence | Candid Charity Check, Ajah, fiscal sponsor capture | Candid + CSI WatchDOG | due diligence (positioning) | — | — | — | B (2–3 direct) |
| Multi-year grants | Multi-Year Grant Workflows | — | — | multi-year grants across programs | — | — | B (2) |
| Recurring cycles | New Cycle Preparation | — | — | — | — | — | A (1 direct; plausible common) |
| Budgeting tools | Budgeting Tool | one-click budget reports | budgeting and forecasting | budget dashboards | forecasting | — | B (4) |
| Reporting / dashboards | Reports, Data Sets, Dashboards, Data Visualization | interactive dashboards for boards | Grantelligence BI | real-time analytics, financial reports | impact analytics | impact dashboards | B (all) |
| Roles / permissions / audit | Users and Roles; Grants Manager permissions | user permissions; audit trail | role-based dashboards | audit trails | — | permission levels | B (4) |
| Scholarship variant (individuals) | SLM sibling | Award Management (higher-ed sibling) | — | — | — | — | A (product-family) |
| Cross-funder shared application | Universal Application | — | — | — | — | — | A (product-specific) |
| Seeker side (discovery/apply-out) | — | — | Grantseeker product | — | — | — | A (product-specific) |
| Multi-entity grantmaking | — | multiple grantmaking entities | — | — | — | — | A (product-specific) |
| AI assistance | AI Application Analysis, AI Summary | — | Finn AI | AI-enriched workflows | — | — | B (3, era-current) |
| Fund-accounting integration | CommunitySuite sync | Financial Edge ecosystem | integrations | finance integrations | — | transaction export | B (weak-moderate) |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant (deliberately small)

A Grantmaking Platform is recognizable when **all four** hold, operated by/for a philanthropic or charitable funder:

1. **The grant program** — a defined offer of grant funds carrying its rules (purpose, eligibility, application requirements, terms, cycle). Remove → an ad-hoc giving ledger / checkbook philanthropy record.
2. **Requests from grantseekers** — parties outside the funder's staff ask (or are invited/nominated) for the funds, captured as records the system manages and moves through a selection process. Remove → internal giving/budgeting machinery.
3. **The grant as a committed award** — a persistent, identified commitment of a defined amount to a selected grantee under terms, produced by a recorded decision. Remove → an application/review (intake) platform.
4. **Administered execution to a managed end** — the grant's life is tracked against money (installments/payments) and/or required follow-up reporting until it reaches a managed end (completed/closed). Remove → a grant CRM or discovery tool.

Jointly-held is load-bearing: 1+2 without 3–4 = submission management; 3+4 without 1–2 = grants ledger / fund accounting; 2+3 without 4 = intake-plus-decision tool with no administered life.

**Historical / market-sample check (§24):** a paper-era foundation ran printed program guidelines, received paper proposals (or invited them), review committees scored them, the board voted (recorded in minutes), grant agreements/award letters committed funds, checks went out on a disbursement schedule, grantees filed paper progress reports, and files were closed. All four invariants hold with no portal, e-signature, or digital money. Non-US funders (UK grant-making trusts, EU stiftungen) fit the same abstract shape with local vocabulary. Corporate giving programs and government grantmakers using the same products also satisfy the chain — which is precisely the evidence that the *structure* is shared with the government Type and the seam is operator context. → definition survives.

### L1 — Common Mature Structure

- **Grantee/applicant organization records** — standing records with history, contacts, and applicant access; the philanthropic emphasis on relationship management ("manage relationships, not just applications") is common mature structure, not definition.
- **Online application portal + grantee portal** — the external surfaces for requesting and then coordinating awarded grants.
- **LOI / intent stage** before a full application (optional but common; directly evidenced at 2 products).
- **Eligibility screening** — rules/quizzes at intake; **charity-status due diligence** via integrated charity-data services (Candid-class; Ajah; watchlist screening) is the philanthropic flavor of vetting.
- **Review/evaluation workflow** — assigned reviewers (staff, external experts, board members), scoring rubrics/forms, shared review access, sometimes blinded.
- **Recorded decisions** — approve/deny as attributable actions (with draft states before finalization in the most lifecycle-explicit product).
- **Agreements and award documents** — award letters/grant agreements via merge templates and e-signature.
- **Installments and payments** — scheduled installments against the awarded amount, payments recorded (sometimes executed via payment-service or accounting integrations); budgeting tools; multi-year grants.
- **Follow-ups** — post-award report forms with due dates, reminders, completion tracking, and internal evaluation.
- **Recurring cycles** — annual/periodic re-opening of programs with per-cycle preparation.
- **Communications machinery** — templates, merge fields, notifications, tracked correspondence.
- **Roles, permissions, audit trails** — program/finance/reviewer separation; attributable records.
- **Reporting and dashboards** — portfolio views (requests, awards, payments, follow-ups, impact) for staff, leadership, boards.

### L2 — Variant / Optional

- **Funder-type variants:** private/family foundations; community foundations (fund structures + fund-accounting integration); corporate giving/CSR programs (employee giving adjacency); research funders; government grantmakers (the boundary zone with §24); religious/other charities.
- **Scholarship management** — same machinery with individuals as applicants/recipients (product-family sibling).
- **Donor-advised / fund-structured grantmaking** — grants initiated from donor funds (community-foundation pole).
- **Cross-funder universal applications** — one shared application accepted by multiple funders.
- **Blind review; multi-round scoring.**
- **Fiscal sponsors / third-party responders** — a sponsor organization acts for the applicant.
- **Multi-entity grantmaking** — one funder staff overseeing several entities with separated data/access.
- **Seeker-side modules** — grant discovery/application-out for funders that also apply for funds (two-sided packaging).
- **AI assistance** — application analysis, summaries, conversational portfolio queries (era-current).
- **Impact/outcome measurement modules** — beyond compliance reporting.
- **Payment rails** — in-platform records + external execution (payment service, accounting handoff) vs fuller in-platform money.
- **Emergency/rapid-response programs** — compressed cycles.

### L3 — Vendor-specific (research notes only)

- **Foundant:** GLM/SLM/Universal Application packaging; Compass community; Candid Charity Check fields; Ajah; Bill.com; DocuSign; CommunitySuite sync; license tiers (Limited/Basic/Standard/Advanced) gating follow-up evaluation features; exact request-status ladder (LOI Draft … Abandoned/Closed); Follow Up Submission Logic default = Sequential; workload-page names (Approved / All Open Approvals / Follow Ups Draft|Submitted|Complete); AI Application Analysis / AI Summary; fiscal-sponsor recommendations article.
- **Blackbaud:** GIFTS heritage; multi-entity separation; CSI WatchDOG watchlists; Raiser's Edge NXT grant-info integration; marketing metrics (50 days, 30%, 10x) — not asserted.
- **Fluxx:** Grantmaker/Grantseeker two-sided packaging; Fluxx Data Core; Grantelligence ("7000+ visualizations" claim); Finn AI assistant; $39B+/200,000+ grantee marketing numbers — not asserted.
- **SmartSimple:** SmartSimple Cloud configurability; Salesforce edition; marketplace; GSA schedule; implementation-length comparisons (2–3 / 2–4 / several months); merger into Foundant family.
- **GivingData:** GDConnect user conference; trust-based-philanthropy positioning.
- **Submittable:** numeric permission ladder (1–5); Fund→Award→Payment naming; Additional Forms mechanics; 1099-K handling for fee-based projects.

## Vendor-specific / Rejected Findings

- **Rejected as definitional:** portals/cloud (paper-era practice satisfies the core); AI features; specific payment rails; universal applications; seeker-side modules; multi-entity; scholarship packaging; marketing metrics; license-tier feature gating; exact status names.
- **Kept as variants:** LOI stage, blind review, multi-year, fiscal sponsors, due-diligence services, donor-advised structures, government-funder packaging.
- **Anti-overfitting note:** the request-lifecycle stage names (LOI → Application → Evaluations → Decisions → Installments → Follow Ups) are one product's articulate version of a chain that all sampled products realize in their own vocabulary — the chain is common; the stage names are not.

## Boundary Findings

1. **vs Government Grants Management (§24) — JOINT REVIEW RESOLVED FROM THIS SIDE.** The funder-side machinery is one market family: Foundant sells GLM to "Government Organizations"; Fluxx sells Grantmaker to government agencies (case study: a state veterans commission); SmartSimple ships a Government Funding solution; Submittable serves agencies; Blackbaud serves public-adjacent funders. Structure alone does not separate the two leaves — the four-part chain is identical. **Resolution: keep-both RATIFIED, seam = operator context, not structure.** Government Grants Management = a government agency distributing **public** funds under statutory process (formal funding notices, statutory eligibility, audit and public-transparency exposure). Grantmaking Platform = a philanthropic/charitable funder distributing **private/charitable** funds under board fiduciary governance and donor intent (program guidelines, discretionary/invited processes, voluntary transparency). The same product can be deployed in either context; the Type follows the operator's posture, not the vendor. This ratifies the government pass's keep-both recommendation.
2. **vs Submission Management Platform (intake boundary).** An intake platform used for a grant program realizes L0 #1–2 and a decision; it becomes grantmaking when the **award administration** is in scope (grant as committed award + money/follow-ups to a managed end). Submittable crosses that line via Funds Tracking (Fund → Award → Payment, capped) + Additional Forms — which is why it qualifies as a boundary specimen rather than a core sample. Removal test: strip post-award administration → intake/review tool; strip the request process → grants ledger; strip the program layer → ad-hoc giving.
3. **vs Nonprofit Grant Management (§25, unprocessed) / Research Grant Management (§23).** Those are the **recipient** side of the same funding relationship (managing grants received). Note: SmartSimple's "Research Grants Management" solution serves research *foundations* (funder pole) — the same product family spans both sides across its solutions; the directory leaves are separated by side (funder vs recipient), and the research-funder segment belongs to this Type.
4. **vs Donor Management System (§25, processed).** Direction of money and object of record: donations **in** attributed to constituents (gift records) vs grants **out** committed to grantees (grant records). Community foundations do both (raise into funds, grant out) — realized as separate products/modules (donor CRM vs grantmaking platform vs fund accounting) with integration seams.
5. **vs Nonprofit Fund Accounting.** Fund accounting tracks the money pools (restricted funds, GL); the grantmaking platform tracks the grant lifecycle and draws on/integrates with the fund ledger (CommunitySuite sync; finance-system integrations). Remove the lifecycle → fund accounting; remove the ledger → grantmaking platform.
6. **vs Financial Aid Management (§23, processed).** The scholarship variant (individuals as recipients, award cycles, follow-ups) is structurally the cousin of institution-side aid management; the seam is the operator (funder vs institution) and the money source (funder's grant funds vs institutional aid funds). Recorded as a cross-domain cousin, not a conflict.
7. **vs Fundraising Management Platform.** Campaign machinery for raising money (appeals, events, peer-to-peer); no grant program, no request-review-decision loop, no award administration.

## Uncertainties

- **Blackbaud Grantmaking operational detail** — Tier 1 help unreachable (JS shells ×2 on 2026-09-08); all Blackbaud assertions rest on its product page (Tier 2) and are kept at positioning strength. Its GIFTS heritage and exact object model were not directly examined.
- **Fluxx operational detail** — support portal transport error (1 attempt); assertions rest on product/FAQ pages (Tier 2). Fluxx's configurable data model was not directly examined.
- **SmartSimple operational detail** — public wiki 403 (1 attempt); assertions rest on solution pages (Tier 2).
- **Submittable evidence is inherited** from the 2026-09-07 pass (help center reachable then); not re-fetched this pass.
- **Recurring cycles** directly evidenced at one product (New Cycle Preparation); treated as common-in-practice but kept at moderate strength.
- **Agreements/e-signature** directly evidenced at 3 of 6; kept as common mature structure with moderate wording.
- **Donor-advised fund workflows** not directly examined (no reachable operational docs); kept as a named variant only.
- **Exact status ladders, numeric limits, default settings** — asserted nowhere in the final document; product-specific state detail stays in these notes.

## Final Synthesis

The Type is best modeled as: **a philanthropic funder's system of record for running its grantmaking — from defined grant programs, through requests from grantseekers and a recorded selection, to grants as committed awards that are then administered (installments/payments and follow-up reporting) to a managed end.** The defining core is the same four-part chain as the government sibling; the seam between the two Types is the operator's posture (private/charitable funds under board and donor governance vs public funds under statutory process), not the structure. Around the core, mature products add grantee relationship records, portals, eligibility and charity due diligence, review workflows, agreements, money machinery, follow-ups, and portfolio reporting; scholarships, donor-advised structures, corporate CSR, research funders, and government deployments are variants of funder type. The market is consolidating (Foundant family: GLM + SmartSimple + GivingData + CommunitySuite) but the philosophies remain distinct: lifecycle-first, CRM-first, data-platform-first, configurability-first, and intake-first (the last crossing into the Type only when award administration is in scope).
