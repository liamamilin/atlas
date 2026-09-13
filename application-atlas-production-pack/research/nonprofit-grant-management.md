# Research Notes — Nonprofit Grant Management

## Research Goal

Understand how software supports the **recipient side** of grant funding — a nonprofit (or similar mission organization) managing the grants it seeks and receives: tracking funding opportunities and funders, submitting applications, and administering awarded grants (obligations, reporting, budgets, compliance, documents) through to closeout. Produce a vendor-neutral Application Document.

This pass carries the reciprocal boundary recorded by two processed siblings:

- **Grantmaking Platform (§25, processed 2026-09-08)** — Boundary Finding 3: "vs Nonprofit Grant Management (§25, unprocessed) / Research Grant Management (§23). Those are the **recipient** side of the same funding relationship (managing grants received)."
- **Government Grants Management (§24, processed 2026-09-07)** — boundary note: "vs Research/Nonprofit Grant Management (funder vs recipient side)."
- **Nonprofit Fund Accounting (§25, processed)** — Boundary 5: grant lifecycle vs "grant-as-funding-source inside the books."

## Initial Boundary

- **What this leaf is:** recipient-side grant machinery — the organization's system of record for its own grant funding relationships (seek, win, manage, close out).
- **Likely confusions:**
  - **Grantmaking Platform (§25, processed)** — funder side (foundations deciding and distributing). Same market family, opposite side of the funding relationship.
  - **Government Grants Management (§24, processed)** — funder side for public funds. Note: governments also *receive* grants (pass-through, federal awards to states/municipalities) — a government-grantee posture of this Type, evidenced by Euna and Fluxx serving government seekers.
  - **Research Grant Management (§23, unprocessed)** — university research administration (proposal pipeline, awards, effort, compliance) — the academic cousin of the recipient side.
  - **Nonprofit Fund Accounting (§25, processed)** — grants as restricted revenue inside the ledger; this Type owns the grant lifecycle and hands financial detail to the books.
  - **Research Funding Discovery Platform (§23, unprocessed)** — discovery-only databases (Instrumentl-class); below/beside this Type.
  - **Donor Management System / Fundraising Management Platform (§25, processed)** — donations-in (donor's will, stewardship) vs grants-in (competitive award under terms, compliance).
  - **Project/Task Management (§03)** — generic execution machinery without the grant/funder/award/obligation model.
- **Initial hypothesis:** the defining structure is a grant record of the funding relationship held from the receiving side, plus obligation tracking and money discipline against the award. Open question: is the pursuit pipeline (opportunities, applications) definitional, or common-mature? And is discovery in or out?

## Research Questions

1. What are the core objects on the recipient side? (funder, opportunity, application/proposal, grant/award record, budget, deliverable/measure, report, document, task)
2. What does the pre-award half look like (discovery, fit assessment, LOI/proposal, submission, decision) and is it required for the Type?
3. What does the post-award half look like (reporting calendar, performance/deliverables, budgets/spending, amendments, closeout)?
4. Where does the grant record begin — at opportunity or at award — across products?
5. What roles exist on the recipient side (grant writer, grant manager, finance, program staff, leadership)?
6. How do two-sided vendors package seeker vs maker (Fluxx, Euna/AmpliFund, Foundant GLM/GrantHub)?
7. What is the finance pole (grants in fund accounting) and where is the seam?
8. Which capabilities are common mature structure vs variant vs vendor-specific?
9. Historical check: would a paper-era nonprofit grants office (grant folders, reporting calendar, budget worksheets, award-letter file) satisfy the definition?

## Representative Products

| Product | Why chosen | Angle | Evidence layer reached |
|---|---|---|---|
| **Euna Grants (formerly AmpliFund)** | full-lifecycle grant management serving government and nonprofit recipients; only major recipient-side product with a reachable public help center | full lifecycle spine + object model | **A (Tier 1)** — Zendesk help center (grants-help.eunasolutions.com, still AmpliFund-branded) + Tier 2 product pages |
| **Fluxx Grantseeker** | enterprise seeker-side product of the two-sided Fluxx family; "grant tracking" (active-grant) philosophy | post-award-forward tracking pole | **B (Tier 2)** — product page + FAQ; support portal not re-attempted (sibling pass transport error) |
| **Blackbaud Financial Edge NXT** | finance pole — grants as restricted funding sources/subfunds inside nonprofit fund accounting | ledger-realized money discipline (boundary pole) | **B (Tier 2)** — product page + FAQ; deeper docs JS-shelled in prior passes |
| **Grantable** | AI-era writing-native entrant; discovery + proposal production + light tracking; self-declared spreadsheet/tracker replacement | pre-award/writing pole (boundary flavor) | **B (Tier 2)** — product page; app login-gated |
| Instrumentl | discovery+tracking market leader for nonprofits | named anchor only | **unreachable (403 ×2: root + /help)** — no claims drawn |
| Foundant GrantHub | historically the symmetric seeker-side sibling of GLM | named anchor only | **retired** — product page redirects to vendor home; support hub has no GrantHub category (checked 2026-09-08). Market consolidation evidence, not a current sample |

Inherited cross-product context (Tier 1/2, fetched 2026-09-07/08 by sibling passes): Foundant GLM, Fluxx Grantmaker, SmartSimple, GivingData, Blackbaud Grantmaking, Submittable (funder side — see research/grantmaking-platform.md).

## Sources

**Euna Grants / AmpliFund (Tier 1, fetched 2026-09-08)**
- https://grants-help.eunasolutions.com/hc/en-us — support hub (categories: Release Notes; User Guides; Instructions/Knowledge Center; Training & Videos; Import Templates; FAQ & Best Practices; **Grant Seeker Training**; **Grant Maker Training**; **Recipient and Applicant Training**)
- https://grants-help.eunasolutions.com/hc/en-us/categories/201641726-Knowledge-Center — full section map (Activity; Administration; Applicant Portal; Award Management; Program Management; Contacts; Documents; Fund Management; **Grant Management: Overview / Pre-Award / Award / Post-Award / Grant Workflow**; Project Management; Reports; Tools)
- https://grants-help.eunasolutions.com/hc/en-us/articles/54118645875603-Deliverables-Measures-and-Activities-Overview — three-level performance model + role-based article index (Funder / Recipient / Applicant)
- https://grants-help.eunasolutions.com/hc/en-us/articles/42982202158995-Grant-Seeker-Streamline-your-Grants-Closeout-Process — closeout as named recipient process
- https://grants-help.eunasolutions.com/hc/en-us/articles/41214764762003-Grant-Seeker-Post-Award-Financial-Checklist — "Track expenses against your budget, payment requests, and cash receipts"
- https://eunasolutions.com/solutions/grants/seeker/ — PLAN / WIN / MANAGE seeker posture (Tier 2)
- https://eunasolutions.com/solutions/grants/research/ — Grants Research module: Discover → Evaluate → Track (Tier 2)
- Note: amplifund.com now serves Euna Solutions branding; help-center sign-in routes to amplifund.zendesk.com. Recorded as rebrand/consolidation evidence (AmpliFund + eCivis lineage).

**Fluxx (Tier 2, fetched 2026-09-08)**
- https://www.fluxx.io/products/grantseeker-fluxx-grants-management-software — positioning, capability blocks, six-question FAQ (incl. "What is the difference between grant tracking software and grant management software?" and the Grantmaker add-on note)

**Blackbaud (Tier 2, fetched 2026-09-08)**
- https://www.blackbaud.com/products/blackbaud-financial-edge-nxt — subfund accounting FAQ, "Federal Grant 1004 record" screenshot caption, Grant Income and Expense Report, compliance/stewardship blocks

**Grantable (Tier 2, fetched 2026-09-08)**
- https://www.grantable.co/ — pipeline stage list, funder discovery, lifecycle tracking claims, "replaces" positioning

**Unreachable**
- Instrumentl: https://www.instrumentl.com/ and /help — 403 ×2 (abandoned per network rules). Market anchor only.
- Blackbaud deeper product docs (kb/webfiles) — JS shells in prior passes; not re-attempted.

## Product Observations

### Euna Grants (formerly AmpliFund) — evidence layer A (Tier 1 help center)

- **Two-sided packaging, first-class:** help-center training split into **Grant Seeker Training**, **Grant Maker Training**, and **Recipient and Applicant Training** (external portal users). Product pages market three postures: Grants Research / Grant Seeker / Grant Maker.
- **Seeker posture (product page):** PLAN (identify opportunities, search/filter, save/monitor/track) → WIN (configurable application workflows: task tracking, collaboration, deadline reminders, versioned application materials) → MANAGE (post-award: "Track deadlines, deliverables, and spending in one system; automate reminders for progress and financial reporting; maintain audit-ready documentation for every award cycle").
- **Grant lifecycle split on the grant record (help-center section map):** **Grant Management: Pre-Award** (submission budgets with categories; deliverables/measures set up pre-award and copied to post-award) → **Grant Management: Award** ("How To Mark a Grant as Awarded"; "How To Activate a Grant Award"; award budget settings; copy submission budget to post-award) → **Grant Management: Post-Award** (largest section, 85 articles: deliverables, activities, performance measures, **amendments**) → **Grant Workflow** (workflow instances, tasks, actions). Plus **Grant Management: Overview** (grant records; overall + individual grant dashboards; add/edit/copy/delete/purge/restore/disable a Grant).
- **Performance model (article, direct):** three levels — **Deliverables** ("what must be completed": name, description, due date, completion status) → **Measures** ("how progress is tracked": Milestone / Number / Percent types with target + target date) → **Activities** ("the actual work reported": reporting period, number complete, description, attachments). "Activities flow upward automatically: Activities (real work) → Measures (progress tracking) → Deliverables (completion status)."
- **Recipient-side amendments (direct):** a Recipient role "propose[s] amendments to your performance plan" (add/edit/remove a performance measure in an amendment); the Funder role "reviews and approves a Performance Measure Amendment." Direct evidence of funder-facing change control on the award.
- **Money side (direct):** Post-Award Financial Checklist — "Track expenses against your budget, payment requests, and cash receipts in a centralized place"; closeout guide — "budget tracking to centralized documentation and performance reporting." Award budget vs submission budget are distinct objects.
- **Supporting machinery:** Activity calendar (events/tasks filterable by grant); Tools (tasks, emails); Contacts (organization records); Documents (folders per grant); Project Management (projects as a separate object); Reports; Administration (custom form extensions on activities/deliverables/measures; task review automation).
- **Discovery as a separate module (product page):** **Grants Research** — DISCOVER (consolidated state/federal/regional/foundation listings, filters) → EVALUATE (fit criteria, summaries) → TRACK (save to dashboard, deadline alerts, pre-application tasks, share/assign). Packaged as its own module beside Seeker — discovery is purchasable adjacency, not the seeker core.

### Fluxx Grantseeker — evidence layer B (Tier 2)

- Positioning: "Manage deadlines, budgets, reporting, and responsibilities for every grant in one place"; "for teams managing growing portfolios of active grants — where deadlines, reporting requirements, and funding have become too difficult to manage in spreadsheets alone."
- Capability blocks: shared view of grant activity (centralize grant data, deadlines, documents, financials); structured execution (tasks, deadlines, approvals, ownership); budgets and reporting ("see what's been awarded, spent, and remaining while keeping reporting on schedule"); compliance/audit readiness ("structured records of grant activity, financials, and reporting requirements").
- Calendar view across grants; dashboard with funding totals/reporting/program performance.
- **FAQ, direct quotes:** "Grant tracking software helps organizations manage grant activity, including deadlines, application status, budgets, reporting requirements, and team responsibilities in one place." / "Grant management software is a broader category that may include both grantseeking and grantmaking workflows. Fluxx Grantseeker focuses on grant tracking and execution." / Best for "nonprofits, higher education institutions, and public sector organizations with 10–50+ active grants." / "What if our organization does both grantseeking and grantmaking? … Fluxx Grantmaker can be added later… bringing both workflows into one connected platform."
- Emphasis is **active grants** (post-award-forward); pursuit machinery present only as "application status" in the FAQ definition.

### Blackbaud Financial Edge NXT — evidence layer B (Tier 2)

- Positioning: nonprofit fund accounting ("fund accounting for nonprofits").
- Grants realized as **subfunds**: FAQ — "Subfund accounting is a hierarchical structure within your general ledger that allows you to carry the revenue, expense, and equity related to a restricted fund. Valuable for endowments, **grants**, contracts, and agency funds… Using a record for each subfund allows you to track qualitative data, such as **spending guidelines, key dates, and contact information**, along with the detailed financial data."
- Compliance block: "Track grants, projects, and endowments in granular detail with flexible subfund functionality"; "provide detailed reporting to your funders."
- Direct screenshot caption: "Federal Grant 1004 record showing contact details, attachments, and grant activity with **beginning balance, ending balance, revenue, and expenses**"; "Grant Income and Expense Report with starting balance, net change, and ending balance."
- No pursuit pipeline or reporting-workflow machinery visible at this evidence level — the finance pole carries the money leg inside the ledger and hands lifecycle workflow elsewhere. Matches Nonprofit Fund Accounting's recorded seam ("grant-as-funding-source inside the books").

### Grantable — evidence layer B (Tier 2, boundary flavor)

- Positioning: "AI grant writing that finds your funders, drafts proposals in your voice, and never misses a deadline."
- Declared pipeline stages: Find funders → Assess fit → Read the RFP → Extract checklist → Plan narrative → Draft sections → AI review → Build budget → Team collaboration → Submit → **Track & report** → Reuse & iterate.
- "Manage the lifecycle": "Track deadlines and your pipeline in list, board, and calendar views, share drafts with teammates, and **write progress reports from the same workspace when the grant is funded**."
- Claims to "fully replace grant database subscriptions (Instrumentl, Foundation Directory, GrantStation)" and "fully replace grant management tools (Monday.com, ClickUp, the spreadsheet)" — positioning only, not asserted as fact.
- Center of gravity is proposal production with discovery and a light tracker attached; deeper post-award machinery (budgets vs spend, funder-specified reporting forms, compliance artifacts) is not evidenced at this layer. Treated as the writing-native pre-award pole, not the Type's center.

## Cross-product Comparison

| Structure | Euna Grants (AmpliFund) | Fluxx Grantseeker | Blackbaud FE NXT | Grantable | Strength |
|---|---|---|---|---|---|
| Grant as persistent record from the receiving side (funder + amount + period + terms) | Grant object (add/edit/copy/disable; overall + individual dashboards) | grant record with deadlines/financials/documents | Federal Grant subfund record (contact details, attachments, balances) | proposals/grants in workspace | **B (all 4)** |
| External funder identified on the record | Contacts/organizations; funder role documented | funder context in grant data | funder contact details on subfund record | funder records (discovery/prospecting) | B (all 4) |
| Deadline-and-obligation machinery (reports/deliverables with due dates, tasks, reminders, assignments) | Deliverables/Measures/Activities + Tasks + reminders; closeout guide | "deadlines, reporting requirements, responsibilities"; approvals/ownership | "key dates" on subfund records (thin) | deadline tracking; progress reports when funded | **B (all 4, depth varies)** |
| Performance/deliverable tracking toward the award's terms | three-level model (A) | program performance insights (positioning) | — (not evidenced) | progress reports (light) | B (2 direct + 2 light) |
| Money discipline against the award (budget, spending vs grant, payment requests/receipts) | expenses vs budget, payment requests, cash receipts; submission vs award budget | "what's been awarded, spent, and remaining" | grant subfund balances: revenue/expense, beginning/ending balance | "Build budget" (production-side only) | **B (3.5 of 4; ledger realization at FE NXT)** |
| Compliance/audit-ready documentation | audit-ready documentation per award cycle (A) | compliance tool, audit readiness | audit trail, restricted-fund reporting | — | B (3) |
| Pursuit pipeline (opportunities → application → submission → decision) | Pre-Award section + configurable application workflows (A) | "application status" in FAQ definition (light) | — (absent at finance pole) | full declared pipeline (center) | B (2.5 of 4) — **common, not defining** |
| Discovery of opportunities (databases, matching) | separate Grants Research module | — | — | agents/screening (center) | B (2, module-gated) — **optional** |
| Application/proposal content management | versioned application materials; documents | documents centralization | attachments on subfund record | content library (center) | B (4, depth varies) |
| Funder-facing change control (amendments) | performance measure amendments, funder review/approval (A) | — | — | — | **A (1 direct)** — product-specific depth |
| Closeout as managed end | named closeout process + guide (A) | — (lifecycle implies) | — | — | A (1 direct), consistent with funder-side closeout machinery |
| Reporting to funder/leadership/auditors | Reports section; performance reporting | reporting on schedule | funder reporting, Grant Income and Expense Report | progress reports | B (all 4) |
| Portfolio views (overall dashboard, list/board/calendar) | overall + individual grant dashboards | list/board/calendar/dashboard views | dashboards | list/board/calendar/stats | B (all 4) |
| Tasks/reminders/assignments machinery | Tasks + Activity calendar + workflow instances | tasks, approvals, ownership | — | assignments | B (3) |
| Roles/permissions/audit | User Security Access (help-center featured); roles index | responsibilities/ownership | role-based access | team collaboration | B (4) |
| Accounting/ERP integration spine | ERP integrations (suite) | — | **is the accounting system** | — | B (2 + finance pole) |
| AI assistance | suite-level Euna AI (era-current) | — | AI-powered finance tools | core of the product | B (3, era-current) |

## Canonical Abstraction (L0–L3)

### L0 — Defining Invariant (deliberately small)

A Nonprofit Grant Management application is recognizable when **all three** hold, operated **from the receiving side** of the funding relationship:

1. **The grant as the organization's record of the funding relationship** — a persistent, identified record binding the organization × an identified external funder (foundation, government agency, or other grantmaker) × an amount over a defined period for a purpose, with the funder's terms carried on the record. The record spans the organization's own grant cycle: products differ on where it begins (full-lifecycle products open it at opportunity/pursuit; tracking-first products begin at award) — the standing grant relationship record itself is the invariant. Remove → a project/task list or a plain award note with no funding-relationship structure.
2. **Obligation machinery against the award** — the grant's terms are operationalized as tracked obligations: required reports/deliverables with deadlines, task/reminders/assignments around them, compliance documentation kept audit-ready — with the grant advancing through its period toward a managed end (final report/closeout/renewal). Remove → a static award log; the "management" is gone.
3. **The grant's money discipline** — the award carries a budget that the organization tracks money against (spending vs the grant budget; payment requests/cash receipts where payment-based; realized in the finance pole as the grant's subfund ledger with revenue/expense and balances), so grant money stays visibly inside its terms. Remove → a deadline calendar with no money; the same structure then collapses into generic project tracking.

Jointly-held is load-bearing: 1 without 2+3 = a spreadsheet row per grant; 2 without 1+3 = generic deadline tracker; 3 without 1+2 = the grant line in fund accounting (the fund-accounting pass's own seam); 1+2 without 3 = reporting calendar without money; 1+3 without 2 = award ledger with budgets but no obligation management; 2+3 without 1 = budgets and deadlines with no grant anchor.

**Historical / market-sample check (§24):** a paper-era nonprofit grants office — a folder or notebook page per grant recording funder, amount, period, and terms; a reporting calendar of what is due when; grant budget worksheets comparing spending to the grant line; a correspondence file with the program officer; copies of proposals and award letters; a final report filed at closeout — satisfies all three invariants with no software. Restricted legacies with conditions tracked by religious/charitable institutions in ledgers with condition notes are the same structure at older depth. Non-US recipients (UK charities tracking statutory/Lottery grants, EU beneficiaries under national programs) fit the same abstract shape with local vocabulary. The finance-pole product shows the legs can be realized inside a ledger; the writing-pole product shows the pre-award half can dominate the market posture without changing the invariant. → definition survives.

### L1 — Common Mature Structure

- **Pursuit pipeline (pre-award)** — opportunities/funders under evaluation, fit/eligibility assessment, LOI/proposal production, submission task tracking, recorded win/loss. Present in full-lifecycle and writing-native products; absent at the finance pole → common, not defining.
- **Application/proposal content management** — documents, narratives, budgets, reusable content libraries attached to pursuits.
- **Funder relationship records** — organizations/contacts (program officers), history with each funder.
- **Performance machinery** — deliverables with due dates and completion status; measures/indicators with targets; activity/progress reporting that aggregates upward (three-level model directly evidenced at one product; two-level variants elsewhere).
- **Reporting calendar + tasks/reminders/assignments** — the compliance heartbeat across the whole portfolio.
- **Documents per grant** — award letters, agreements, budgets, reports, correspondence, attachments.
- **Portfolio surfaces** — overall + per-grant dashboards; list/board/calendar views; deadlines-at-a-glance.
- **Roles/permissions/audit trails** — grant staff, finance, program staff, leadership; attributable records.
- **Reporting/exports** — for leadership, boards, auditors, and funders.
- **Integration spine** — accounting/ERP, calendars, email; the finance pole realizes money inside the ledger rather than integrating to it.

### L2 — Variant / Optional Structure

- **Discovery/research module** — opportunity databases and matching (Euna Research module; Instrumentl-class standalone products; Grantable's agent-based prospecting). Module-gated or a different Type (Research Funding Discovery Platform).
- **Funder-type postures** — foundation grants (lighter terms, narrative reporting) vs government grants (payment requests/drawdowns, heavier compliance, audit posture); governments and higher education also act as recipients (Fluxx and Euna explicitly serve them).
- **Two-sided packaging** — the same vendor sells maker and seeker postures/products (Fluxx Grantmaker/Grantseeker; Euna maker/seeker; Foundant GLM + the retired GrantHub).
- **Finance-pole deployment** — grant lifecycle machinery folded into fund accounting as subfunds; the Type's money leg realized as ledger records.
- **Writing-native entrants** — AI-era proposal-production products whose center is drafting, with discovery and light tracking attached.
- **Amendment/change control** — proposing modifications to the award's plan/budget for funder approval (directly evidenced at one product; consistent with funder-side amendment machinery in the government pass).
- **Scale workflow** — multi-department approval chains, workflow instances, review automation.
- **AI assistance** — drafting, summaries, portfolio Q&A (era-current).

### L3 — Vendor-specific (research notes only)

- **Euna/AmpliFund:** PLAN/WIN/MANAGE posture framing; Research module (Discover/Evaluate/Track); object set (Grant, Opportunity, Fund, Project, Activity, Task, Email, Organization, Deliverable/Measure/Activity triad); "Mark a Grant as Awarded" / "Activate a Grant Award" state actions; submission-budget vs award-budget objects; copy-deliverable/measure-to-post-award actions; workflow instances/task review automation; Grant Seeker / Grant Maker / Recipient-Applicant training split; AmpliFund→Euna rebrand (sign-in still amplifund.zendesk.com); grantexec.com reference; numeric claims (25K+ grants in network, 72% time saved) — positioning, not asserted.
- **Fluxx:** Grantseeker/Grantmaker product split; "grant tracking vs grant management" vocabulary distinction; 10–50+ active grants positioning; 1–2 week implementation claim; dedicated compliance tool; "awarded, spent, and remaining" framing.
- **Blackbaud:** subfund accounting definition; Federal Grant 1004 example; Grant Income and Expense Report; Raiser's Edge NXT integration; "25% increase in grant funding" customer metric — not asserted.
- **Grantable:** full stage list; "fully replaces" claims (Instrumentl/Foundation Directory/Monday/ClickUp/spreadsheet); 990-screening agents; email-operated workspace; Agency Hub add-on; pricing/capacity tiers — positioning, not asserted.
- **Instrumentl:** unreachable — no claims of any kind.

## Vendor-specific / Rejected Findings

- **Rejected as definitional:** pursuit pipeline and application machinery (finance pole lacks it); discovery databases (module-gated; separate Type exists); AI features; specific performance-model depth (three-level triad is one product's articulate version); amendment machinery (single-product at current evidence); closeout naming (concept is the managed-end invariant, the term is product vocabulary); portals (recipient here is an internal seat, not a portal user); cloud deployment; specific payment rails.
- **Kept as variants:** government-grantee posture, higher-ed recipients, two-sided packaging, finance-pole deployment, writing-native entrants, discovery modules, multi-entity scale.
- **Anti-overfitting note:** Euna's Pre-Award → Award → Post-Award section split is one product's articulate version of a cycle all sampled products realize in their own vocabulary (Fluxx compresses pre-award to "application status"; FE NXT begins at award). The cycle is common; the section names and state actions are not.
- **Vocabulary note (recorded):** the market uses "grant tracking," "grant management," and "grant lifecycle management" interchangeably on the recipient side; Fluxx's own FAQ defines grant *tracking* as active-grant management and grant *management* as the broader category spanning seeking and making. The directory leaf is read as the recipient-side management Type under either label.

## Boundary Findings

1. **vs Grantmaking Platform (§25, processed) — DISCHARGES this pass's joint-review obligation from the recipient side.** Same market family, opposite side of the funding relationship. Funder side = defined programs, requests from grantseekers, recorded selection, money out under the funder's governance. Recipient side (this Type) = the organization's own funding relationships: compete/apply, receive the award as terms-and-obligations record, comply, report, close out. Two-sided vendors sell the two sides as separate postures/products (Fluxx Grantmaker vs Grantseeker as separate products with an "add later" note; Euna maker vs seeker posture pages; Foundant GLM vs the retired GrantHub). Keep-both ratified; the seam is whose money and whose obligations.
2. **vs Government Grants Management (§24, processed).** Consistent with that pass's note: funder side of public funds vs recipient side (this Type), including governments-as-recipients (pass-through awards to states/localities — Euna and Fluxx both serve government seekers). No conflict.
3. **vs Research Grant Management (§23, unprocessed) — FORWARD FLAG.** Academic research administration is the university-sector cousin of the recipient side (proposals to sponsors, awards, post-award management). Expected seam: research-administration machinery (sponsors/rates/effort/compliance proper to §23) vs mission-organization grant funding (this Type). Fluxx explicitly sells Grantseeker to higher education — the overlap zone is real. Joint review recommended when that pass runs.
4. **vs Nonprofit Fund Accounting (§25, processed).** Held on that pass's own seam: grant lifecycle vs grant-as-funding-source inside the books. The finance pole (FE NXT subfunds) realizes this Type's money leg as ledger records with balances; the lifecycle/obligation machinery is what makes this Type distinct. Integration/handoff, not merger. Add grantee-side lifecycle → this Type; remove it → fund accounting's grant dimension.
5. **vs Research Funding Discovery Platform (§23, unprocessed) + discovery databases.** Discovery-only products (opportunity databases, funder matching) satisfy none of the three legs except a thin slice of leg 1's funder context — they hold no grant records, no obligations, no money. Discovery appears here only as an optional module (Euna Research; Grantable prospecting). Instrumentl-class products named as market anchors only (unreachable).
6. **vs Donor Management System (§25, processed).** Both are money-in records, but the semantics differ structurally: a gift is given at the donor's will and managed through stewardship; a grant is competitively (or formula) awarded under terms the recipient must fulfill — obligations, reporting, spending constraints. Different record content, different lifecycle, different failure modes (missed report vs lapsed donor).
7. **vs Fundraising Management Platform (§25).** Campaign machinery for raising donations (appeals, events, P2P); no award terms, no obligation machinery, no funder relationship of the grant kind.
8. **vs Project Management / Task Management (§03).** Execution machinery is shared (tasks, deadlines, boards); the seam is the record model — no funder/award/terms/obligations/budget-restriction structure. Grantable's own "replaces Monday.com/ClickUp" positioning marks the overlap zone from inside the market.
9. **vs Submission Management Platform.** Intake machinery belongs to the funder side; from the recipient side, application support is pre-award content management inside the pursuit pipeline (common-mature), not the Type's center.

## Uncertainties

- **Instrumentl** unreachable (403 ×2 on 2026-09-08) — the discovery-forward market leader was not directly examined; its posture (and whether it tracks awards post-award) is unverified. No claims drawn; named as anchor only.
- **Fluxx Grantseeker operational depth** — Tier 2 only; the support portal was unreachable in the sibling pass and was not re-attempted. All Fluxx claims are positioning/FAQ strength.
- **Grantable post-award depth** — product page claims "track & report" and progress-report writing; the app is login-gated and no help-center evidence was reachable. Treated as boundary pole, not core sample.
- **Blackbaud FE NXT** — product-page evidence only; deeper "grants management" module documentation not reachable. The subfund/grant-record mechanics asserted are those shown on the page itself.
- **Euna rebrand recency** — help center still AmpliFund-branded; some marketing links (grantexec.com) unexplored. No claims depend on them.
- **Pursuit-pipeline strength** — directly evidenced (Tier 1) at one product and centered at the writing pole; kept out of the defining core on the finance pole's negative evidence. If a future pass finds recipient-side products that are pipeline-only *and* self-label as grant management, the L0 boundary may need re-examination.
- **Closeout** — directly evidenced at one product (named process + guide); held as the managed-end reading of leg 2, not as separately definitional.

## Final Synthesis

The Type is best modeled as: **a mission organization's system of record for its own grant funding — holding each grant as a standing relationship record with an identified funder (amount, period, terms), operationalizing the award's terms as tracked obligations (reports, deliverables, deadlines, audit-ready documentation) and money discipline (budget vs spending, payment requests/receipts), and advancing each grant through the organization's grant cycle toward a managed end.** The defining core is three jointly-held legs; products realize the cycle from different starting points — full-lifecycle suites (Euna Grants/AmpliFund: plan → win → manage, with a deep post-award section), active-grant trackers (Fluxx Grantseeker), the finance pole where the money leg lives inside fund accounting (Blackbaud FE NXT subfunds), and writing-native entrants (Grantable) whose center is proposal production. Around the core, mature products add the pursuit pipeline, application content management, funder relationship records, performance machinery, portfolio dashboards, roles/audit, and accounting integration; discovery is an optional module or a separate Type. The seam against the funder side is whose money and whose obligations; the seam against fund accounting is lifecycle vs ledger; the seam against generic project tools is the grant-specific record model.
