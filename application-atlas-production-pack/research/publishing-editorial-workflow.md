# Research Notes — Publishing Editorial Workflow

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Book Publishing Management, Publishing Metadata Management; adjacent processed: Academic Journal Management §23, Peer Review Platform §23, Newsroom Management System §27, News Publishing Platform §27, Magazine & Periodical Management §27)

Research date: 2026-09-09

## Research Goal

Understand what a Publishing Editorial Workflow application actually is as an Application Type: what the unit of editorial work is, how a manuscript/work moves through the editorial process (submission → evaluation → editing → production handoff), how editorial roles and assignments work, how the process relates to the title-as-commercial-product record managed by Book Publishing Management, and where the boundary lies against Book Publishing Management, Academic Journal Management, Peer Review Platform, Newsroom/News Publishing, Magazine & Periodical Management, and generic workflow/project tools.

This pass also carries a mandatory joint-review duty: the Book Publishing Management pass (2026-09-06) flagged the acquisition-stage seam — "market products genuinely overlap at the acquisition stage (a workflow-specialist product markets 'track submissions and manage peer reviews' inside its acquisitions module; a cloud suite documents acquisition pipelines and editorial-meeting approval gates), while editorial workflow should center on the content process (manuscript/peer-review/editing) and publishing management on the title as commercial product with money+metadata machinery."

## Initial Boundary

Initial hypothesis (to be tested, not asserted):

- Core use: the system that manages the editorial content process of publishing — the manuscript/work's journey from submission or proposal through evaluation (reader reports / peer review / acquisition decision) and editing (copyedit, proof) to release into production.
- Likely users: acquiring/commissioning editors, editorial assistants, managing editors, copyeditors and proofreaders (in-house or freelance), reviewers/readers, production editors — at book publishers of all kinds, including scholarly presses.
- Nearest neighbors: Book Publishing Management (title as commercial product), Academic Journal Management (journal editorial office), Peer Review Platform (the review exchange itself), Newsroom Management System / News Publishing Platform (news editorial loop), Magazine & Periodical Management (periodical business), generic Workflow/Project Management.
- Likely confusion: "editorial workflow" is also used by CMS/news tools (article approval flows) and by content-marketing tools (editorial calendars); this leaf means the book-publishing editorial process.
- Unknowns: whether the market realizes editorial workflow as a standalone product for trade books or only as a module inside publishing management suites; how much review machinery trade (vs scholarly) products carry; whether the leaf collapses into Book Publishing Management.

## Research Questions

1. What is the unit of editorial work — the submission? the manuscript? the work/title? When does it enter the system relative to the publication decision?
2. What stages does the editorial process have, and which transitions are explicit decision gates with recorded outcomes?
3. How does evaluation work — reader reports, peer review, acquisition/editorial meetings? What machinery exists (reviewer assignment, due dates, reminders, overdue visibility)?
4. How are editing stages (developmental edit, copyedit, proofreading) tracked, and who performs them?
5. How are manuscript/production files handled — managed in-system, attached, or delegated to external tools?
6. How does the schedule work — what anchors deadlines (publication date, manuscript delivery date, stage-relative dates)? What task machinery exists (templates, dependencies, reminders, calendars)?
7. What roles exist, how is work assigned, and who monitors progress?
8. What happens to works that are rejected or never published — does the record persist?
9. Where does the workflow end — what exactly is the handoff to production/publication?
10. Which capabilities are defining vs common vs variant vs vendor-specific? Historical/regional check: do older and differently positioned products fit the same core?

## Representative Products

Selected across market structure (workflow-first open source / modern cloud suite / modular SMB suite / US workflow specialist / enterprise suite), prioritizing reachable official documentation. The first four vendors are the same population sampled by the Book Publishing Management pass from the business angle; this pass samples the editorial-process angle of the same products plus a workflow-first pole the sibling pass explicitly assigned to this leaf.

| Product | Segment / role | Why selected | Evidence quality |
|---|---|---|---|
| Open Monograph Press (PKP) | Open-source editorial-workflow-first system for scholarly monograph presses | The standalone "editorial workflow as the whole system" pole; the sibling pass assigned OMP "primarily to the Publishing Editorial Workflow angle"; official PKP documentation | A (official product page, fetched) |
| Consonance | Modern cloud publishing suite (UK indie/mid, all book segments incl. scholarly) | Deepest official user documentation of the editorial process (best-practice process, pipelines, to-dos, production files); shows how the editorial process sits inside a title-management suite | A (official docs, fetched) |
| Stison | Modular SMB cloud suite (UK) | Shows the pre-production/production split and the modular packaging of the workflow machinery | B (official product page, fetched) |
| Firebrand Title Management Enterprise | Title-lifecycle workflow specialist (US, since 1994); enterprise + Lite tier | The market's own category name ("Publishing Workflow and Project Management"); acquisitions with submissions + peer reviews; role-based schedule machinery | B (official product page, fetched) |
| Klopotek (TEP: Title Management, Editorial & Production) | Enterprise publishing suite (Germany; enterprise groups + SME cloud) | The enterprise suite's editorial area: Early Title Manager drafts → Editorial Meeting approval; workflow-driven metadata entry; notification machinery | B (official product page, fetched) |

Considered but not sampled: Ingenta/BiblioSuite (403 in two sibling passes — not retried), Pressbooks/Booktype (book authoring/production tools, not publisher editorial process — classified adjacent by the sibling pass), Editorial Manager/ScholarOne (scholarly journal systems — belong to Academic Journal Management per that pass), WoodWing/vjoon-class magazine layout-workflow systems (magazine/news domain, different object). Legacy/regional products (virtuos, Titleplay, CatS, Publishers Assistant, Broadland) unreachable in sibling passes; not retried.

## Sources

- Open Monograph Press — https://pkp.sfu.ca/software/omp/ (retrieved 2026-09-09); https://github.com/pkp/omp (README, retrieved 2026-09-09). PKP user documentation (docs.pkp.sfu.ca) behind an anti-bot JavaScript challenge — unreachable this pass.
- Consonance — https://consonance.app/docs/ (index); /docs/best-practice-publishing-process/ ; /docs/create-and-use-a-pipeline/ ; /docs/pipelines-ten-uses/ ; /docs/to-dos/ ; /docs/production-files/ (all retrieved 2026-09-09)
- Stison — https://www.stison.com/production-manager (retrieved 2026-09-09)
- Firebrand Technologies — https://firebrandtech.com/title-management-enterprise (retrieved 2026-09-09)
- Klopotek — https://www.klopotek.com/title-management-editorial-and-production (retrieved 2026-09-09)
- Sibling research used for triangulation and seam discharge: research/book-publishing-management.md (2026-09-06), research/academic-journal-management.md (2026-09-06), research/news-publishing-platform.md (2026-09-08), research/magazine-periodical-management.md (2026-09-08), research/peer-review-platform.md (2026-09-08)

Search-engine limitation: DuckDuckGo timed out; Bing redirected to a regional dictionary-results page — general web search unusable this pass. Sampling therefore relied on direct product URLs known from sibling passes; no new vendors were discovered via search. Claims calibrated accordingly.

## Product Observations

### Open Monograph Press (PKP) — evidence layer A

Positioning (official product page): "The full, end-to-end solution for publishing books. Publish your monographs and edited volumes with full metadata for worldwide dissemination and discovery. Manage submissions and conduct internal and external reviews in a single, intuitive workflow." Open source, developed by the Public Knowledge Project for "scholarly presses" (university libraries/presses among quoted clients). OMP self-identifies as book publishing software: "Everything a book publisher needs."

The four-step framing on the product page:

- **Submit** — "Invite authors to submit to your press through a configurable, step-by-step submission wizard."
- **Review** — "Select peer reviewers, assign due dates, and send reminders to keep everyone on schedule."
- **Publish** — "Publish books to your own website in PDF, ePub, or any publication format, alongside supplementary materials."
- **Distribute** — "Drive the dissemination and discovery of your work through Google Scholar, full ONIX creation, and OAI-PMH metadata harvesters."

Key features (official page):

- "Flexible editorial workflow — Run a streamlined publishing pipeline with editors, copyeditors, translators and production assistants."
- "Stay on schedule — Track every submission and find out quickly when editors and reviewers are falling behind."
- "Peer review — Conduct internal and external review rounds, with tools to help you find the right reviewer every time."
- "Rich publication metadata — Distribute book and chapter metadata in machine-readable formats like ONIX and OAI-PMH."
- "Global scholarly infrastructure — DOIs, ORCID authentication and ROR affiliations."
- "Multiple languages"; "Own your data — import/export tools"; "Sell books — accept online or offline payments and sell books directly through your catalog"; "Track your success — detailed book-by-book statistics and … editorial metrics like response times and reviews per submission"; "Preserve the scholarly record — post new editions and keep a record of old editions with versioned metadata."

How It Works (official page, screenshot captions):

- Authors submit through "an easy, step-by-step wizard that collects all the information you need to evaluate a new submission"; drag-and-drop file upload "including chapter files, figures and tables, and other supporting materials."
- "Editors can search and filter their submissions to track them through the submission, review, copyediting and production stages." — the four-stage editorial workflow, named on the official page.
- "Managing editors can assign editors and monitor each editor's assignments."
- Review stage: "Assign internal and external reviewers to conduct anonymous or open review, set due dates with automated reminders, and see when their responses are overdue."
- ONIX metadata "for books and chapters"; publish to "an easy-to-use, mobile-friendly website with searching and browsing by series or category"; usage statistics per book.
- "A configurable user role system lets you adapt the workflow to your publishing pipeline with editors, copyeditors and production assistants."

### Consonance — evidence layer A

Positioning (sibling pass, corroborated): "Publishing enterprise management solution for the modern book publisher"; user docs fetched this pass.

**Best practice publishing process** (official docs; "an opinionated description of the publishing process… the process that Consonance is optimised to support"):

1. **Assign responsibility for data management** — named role-to-data mapping: "Proposal brief. Usually commissioning editors"; "Metadata. Sometimes managing editors, often editorial assistants"; "Contract terms. Usually commissioning editors"; "To-dos set-up. Usually editorial assistants, sometimes production."
2. **Capture the concept early** — "Add product data to Consonance as soon as it is a publishing possibility"; "The originator of the idea adds the data to Consonance"; "Do not type it up in Word or an email first."
3. **Manage the approval process** — "manage the approval decision in one place, for consistency and future reference": (a) **Proposal brief** — "the document in which the proposing editor makes the editorial and marketing-focussed case for the publication… circulated for comment and finally put to the editorial management team for their decision on whether to go ahead"; downloadable as PDF; (b) **Plan** — the financial model (P&L margin contribution); (c) **The acquisition meeting** — "Use a Pipeline to organise and run the acquisition meeting"; (d) **Publishing decision**.
4. **Manage the publication process** — "There are hundreds of to-dos that need completing to get a book published. Use Consonance's to-dos to plan and stay on track"; issues managed as they arise; to-do dates exportable to iCal/Google calendars.
5. **Manage contracts and royalties** (business machinery around the process).
6. **Disseminate data** — ONIX feeds, spreadsheets, PDFs, "feeds to your website, distributors and printers."

**Pipelines** (official docs): "Pipelines contain stages, which in turn contain cards that represent works." Stages defined by the user; cards dragged between stages to change status; pipelines convertible to batches. Ten documented uses — use #1 **Acquisition management**: "Set up a pipeline with stages such as Proposals, Revisit, Approved, and Rejected, to keep track of your submissions… Use the pipeline stage Ready to propose as your meeting agenda. Have Consonance open in the acquisition meeting and click through to the Plan, Discussions, cover ideas, contract and all the other information you need to make an informed acquisition decision. You have a complete record of your acquisition process." Use #4 **Ideas notes**: "jot down rough ideas for new products and commissions in your own pipeline. Give it stages such as Early ideas, and Proposal received." (Other uses — rights deals, sales, catalogue selection, job candidates, prize entries, retail submission — show the pipeline is generic stage-board machinery reused across domains.)

**To-dos** (official docs): "As a publisher of any size there is a large number of tasks required to get a book from initial conception through to publication… The date by which these tasks must be completed is often related to the publication date of the products being produced." A to-do has three elements: what (description), who ("The person responsible must be a user of the system, as they will be the person who checks the activity off when it is complete"), date (none / fixed / **relative to a base date** — base dates include "Earliest pub date", "Latest ebook pub date", "MS delivery date" — "the manuscript delivery date on the contract"). Relative due dates auto-shift when base dates change ("If the earliest print pub date changes at any point in the future, due to delays in the manuscript delivery for example, the due date for this to-do will automatically change"). Example to-dos documented: "Send files to printer", "Check printer proofs", "Confirm job with printer", "Check printer has shipped products", "Start proof-reading"/"End proof-reading" (paired to-dos stand in for durations), "Check delivery to US Warehouse", "Check with author on peer review feedback". Calendar subscriptions: per-user and per-client feeds into Outlook/iCalendar/Google Calendar. The to-dos page sits under a main-menu section named **"Workflow"**.

**Production files** (official docs): "Upload production files as a record of the files you have sent to print, to form an archive and a single source of truth." "It's best to use Consonance as an archive of finished files. There are other tools which handle versioning of large production files better such as Dropbox." Files named with the ISBN auto-match to works.

Project management area: Briefings, Discussions, Issues, Pipelines, Roles, To-dos, Tracked copies.

### Stison — evidence layer B

Positioning (official site): "Seamless software for publishers of all sizes"; Production Manager page: "our publishing management system is used by over 150 publishers" (homepage says 300+ — vendor counts inconsistent across pages, unverified).

**Production Manager** (official page): "take full control of the production schedule, to maximise efficiencies and minimise costs. Track outstanding tasks, from the list to do through to completion."

- **Custom tasks and schedules** — "Create and assign multiple tasks to product schedules with multiple dependencies."
- **Workflow** — "Utilising a very visual production schedule, see the complete picture at a glance to spot potential issues and opportunities ahead of time."
- **Stop-go P&L analysis** — "Create a P&L for multiple outputs with varying costs to better inform decisions."
- **Notes** — "Keep communication flowing between team members at any point in pre-production or production."
- **Costs and print runs** — "Track all estimated and actual details across production costs and print runs."
- **Custom reports** — "Gantt charts, printer schedule report, grid reports."
- **Pre-production** — "Track ideas, submissions and proposals to assist in editorial review meetings."
- **Complete compatibility** — "Bolt this module onto others, such as Royalties Manager to link with sales data." (Modular packaging: separately licensed Managers over one title database.)

### Firebrand Title Management Enterprise — evidence layer B

Positioning (official page): "Comprehensive lifecycle management built to adapt to every publisher's unique workflows"; "The Publishing Industry's Single Source of Truth Since 1994"; "a comprehensive publishing workflow platform that serves as the central system of record for a publisher's titles, metadata, schedules, contracts, production, marketing, and sales activities… designed to manage the entire lifecycle of a publishing project—from acquisition through publication and beyond." Firebrand's own solutions-nav category for TME: **"Publishing Workflow and Project Management"** — the market's name for this territory.

Feature areas (official page):

- **Acquisitions & Financial Planning** — "Track submissions and manage peer reviews from the initial idea phase. Build dynamic Profit & Loss statements to make strong business cases." FAQ: "calculate format-specific sales, royalties, prepress, and manufacturing costs at every critical stage—from initial acquisition through transmittal and publication."
- **Editorial & Metadata Management** — "Centralize your core bibliographic data and descriptive copy in one hub."
- **Contracts & Rights** — contract details "at the exact point of acquisition"; subrights dashboard.
- **Production & Manufacturing** — "component-based printing specifications… purchase orders."
- **Scheduling & Task Tracking** — "highly customizable schedule templates. Trigger automated email alerts to proactively remind users of upcoming task deadlines." FAQ: "Managers can use customizable schedule templates to automatically assign specific tasks and deadlines to team members based on their roles. Custom dashboards also instantly surface active titles, overdue tasks, and critical approval deadlines to keep your projects moving."
- **Asset Management** — "Securely store digital files of any kind directly within title records, and build connections to external DAM systems."
- **Journals & Periodicals** — "Track volumes, issues, and individual articles through dedicated peer-review scheduling" (periodical extension).
- **Title Management Lite** — smaller-publisher tier: "Acquisition and contract management, Schedule and task tracking, Catalog creation, Seamless metadata distribution"; upgrade path to Enterprise.

### Klopotek (Title Management, Editorial & Production) — evidence layer B

Positioning (official page): "Proven Title Management Software for Publishers"; "Enable a faster time to market with best-of-breed title management software"; "Klopotek software has been specifically designed for the publishing industry: unlike customized versions of generic ERP solutions." TEP is the suite's editorial-and-production solution area.

- **Title Life Cycle Manager** — "Three configurable apps in one to make an editor's life easier": *Early Title Manager* — "enables editors to create first drafts without cluttering the system with data for titles that will, eventually, not be published, as evaluations show that they are not ready for market… All workflow steps from entering first pieces of information and metadata to preparing for getting the title approved at the Editorial Meeting are covered"; *Title Structure Manager* — new titles from title templates; "title families" combine version types/formats of the same IP; *Title Metadata Editor* — "You decide which attributes and data should be included in your workflow and thus can create your own user interface for title management." Unified dashboard with filters: "'drafts', 'forthcoming', or 'published' titles – or specific 'series' only."
- **Metadata Management** — "You select or even design your own scenarios and workflows and decide which data has to be added at which point in time, in which quality."
- **Project Management** — *Scheduling* ("calculations and recalculations, even of complex projects… Gantt charts visualize all the elements you need to see to understand how changes will affect your planning"); *Notification Dashboard* — "Schedules are created and modified by specialists, but many people's daily tasks at a publisher are affected by these plans… a configurable notification dashboard to all employees, so everybody in the company will always know what has to be done by when."
- **Production Management** — Purchasing ("guided order-placement workflow") + Suppliers Online (suppliers "also get access to the tools").
- **Permission & Compliance Manager** — inbound rights compliance.
- A downloadable PDF titled "This could be your TEP workflow" (workflow diagram; not fetched).

## Cross-product Comparison

| Dimension | OMP | Consonance | Stison | Firebrand TME | Klopotek TEP |
|---|---|---|---|---|---|
| Unit of editorial work | submission (monograph/edited volume) | work (+ proposal brief) | idea / submission / proposal | submission tracked "from the initial idea phase" | early title draft |
| Enters before publication decision | ✓ (submission wizard "to evaluate a new submission") | ✓ ("as soon as it is a publishing possibility") | ✓ (pre-production ideas/submissions/proposals) | ✓ (idea phase) | ✓ (first drafts; "titles that will, eventually, not be published") |
| Staged process named in-system | ✓ "submission, review, copyediting and production stages" | proposal → plan → acquisition meeting → publication process (to-dos) | pre-production → production | acquisition → transmittal → publication | draft → Editorial Meeting approval → forthcoming → published |
| Recorded decision gates | review outcomes; stage advancement | acquisition meeting decision (pipeline stages Approved/Rejected); publishing decision | editorial review meetings | approval deadlines; acquisition | Editorial Meeting approval |
| Evaluation/review machinery | full: internal + external reviewers, anonymous or open review, due dates, automated reminders, overdue visibility | to-do example "Check with author on peer review feedback" (scholarly segment); acquisition meeting via pipeline | not evidenced on fetched page | "Track submissions and manage peer reviews"; journals module "dedicated peer-review scheduling" | not evidenced on fetched page |
| Editing-stage tracking | copyediting as a named stage; copyeditor role | to-dos (proof-reading start/end examples); proofreader in default cost groups | production tasks | schedule templates incl. editorial tasks | workflow-driven data entry (metadata, not prose editing) |
| Files | submission files (chapters, figures, tables) uploaded; publication formats produced | production files archived as "record of the files you have sent to print"; versioning delegated to Dropbox | not evidenced | assets stored within title records; DAM connections | not evidenced |
| Assignment of stage work | managing editors assign editors, monitor assignments; reviewers assigned | to-dos assigned to system users | tasks assigned | tasks auto-assigned "based on their roles" | notification dashboard to all employees; role-oriented workflow steps |
| Deadline machinery | review due dates + reminders + overdue flags | to-do dates fixed or relative to base dates (pub date, MS delivery date); auto-shift; calendar export | schedule with dependencies; Gantt | schedule templates; automated email alerts; dashboards (active titles, overdue tasks, approval deadlines) | Scheduling (Gantt, recalculation); Notification Dashboard |
| Workflow configurability | configurable workflow + user role system | user-defined pipelines; to-do set-up | custom tasks/schedules | "adapt to every publisher's unique workflows"; customizable templates | "design your own scenarios and workflows" |
| Process record for rejected/unpublished works | submissions tracked regardless | "complete record of your acquisition process"; Rejected stage | ideas/proposals tracked | submissions from idea phase | early drafts "that will, eventually, not be published" kept without cluttering |
| Destination of the workflow | in-system publication (catalog website, PDF/ePub) + distribution (ONIX/OAI) | release to production (printer to-dos, production-file archive) + data dissemination | production schedule through completion | transmittal and publication; metadata delivery | production (purchasing, suppliers) + metadata export |
| Business machinery around the workflow | minimal (payments/selling; scholarly infrastructure) | plans, contracts, royalties, rights, ONIX | Royalties/Rights modules bolt on | P&L, contracts, subrights, marketing, ERP integration | CRR suite (contracts/royalties/rights), O2C separate |
| Deployment / posture | open source, self-hosted or PKP-hosted | SaaS | SaaS, modular | hosted service, tiered (Lite/Enterprise) | on-prem Classic Line + STREAM cloud |

Evidence: OMP and Consonance rows layer A (fetched official pages/docs); Stison/Firebrand/Klopotek rows layer B (fetched official product pages; marketing-level detail). "Not evidenced" = absence on fetched pages, not evidence of absence.

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being recognizable as a publishing editorial workflow system:

```text
Work-in-editorial as the unit of record
(a persistent record for one publishing work during its editorial life —
existing from before the publication decision as submission, proposal,
or early draft; carrying the work's identity and editorial state;
accumulating the process's record: decisions, files, notes, completed steps)
├── Staged editorial process with recorded gates
│   (the work advances through an ordered, configurable set of editorial
│   stages — entry, evaluation, editing, release toward production —
│   where the transitions that matter are explicit decision points with
│   recorded outcomes: proceed / decline / approve)
└── Role-assigned stage work with deadlines
    (each stage's work assigned to identified participants — acquiring
    editor, reviewer, copyeditor, proofreader, production editor — with
    due dates, reminders, and visible completion/overdue state; a managing
    role assigns and monitors)
```

Three properties:

1. **Work-in-editorial as the unit of record** — the system's world is organized around per-work editorial records that exist *before* the publication decision and persist through it (including rejections). Remove → a bare title database or a submission log with no process.
2. **Staged editorial process with recorded gates** — what is managed is the *process* the work moves through, not just tasks: ordered stages with explicit decision points whose outcomes are recorded against the work. Remove → a task list or a static schedule; a status board without gates.
3. **Role-assigned stage work with deadlines** — editorial work is delegated to identified people per stage, with due dates and visible progress/overdue state. Remove → a process description nobody works; assignment without a process is a task tracker.

Jointly-held load-bearing: (1) alone = title database / submission log; (2) without (1) = a workflow diagram / process template; (3) without (1)+(2) = a task tracker; (1)+(2) without (3) = a status board; (1)+(3) without (2) = task assignment with no process; (2)+(3) without (1) = a generic workflow/approval tool.

Publishing-specificity lives in the *content* of the stages and gates — acquisition/reader-report/peer-review evaluation, copyedit and proof stages, transmittal to production — and in the work carrying publishing semantics (publication dates, editions, metadata), not in an additional abstract structure.

Historical check: the paper-era editorial office satisfies all three legs with no software — the submission file/log as the unit of record, the acquisition decision and editing rounds as gated stages, editors/readers/copyeditors as assigned roles with deadlines. Firebrand TME (since 1994) and OMP (2000s open source) represent two software generations of the same core. Regional/legacy products were unreachable (limitation recorded); nothing in L0 requires cloud, ONIX, kanban boards, or digital formats.

### L1 — Common Mature Structure

Present across the researched sample:

- **Submission/proposal intake** — a configured entry path collecting the information needed to evaluate the work (OMP submission wizard; Consonance "capture the concept early" + proposal briefs; Stison pre-production ideas/submissions/proposals; Firebrand submissions from idea phase; Klopotek Early Title Manager drafts). [A×2, B×3]
- **Evaluation machinery** — reviewer/reader assignment with due dates, reminders, and overdue visibility (OMP full; Firebrand "manage peer reviews" + journals peer-review scheduling; Consonance scholarly to-dos reference peer-review feedback; the acquisition/editorial meeting as the trade-pole evaluation gate with recorded outcomes — Consonance pipelines, Klopotek Editorial Meeting). [A×2, B×2 + gate evidence B×2]
- **Task/to-do machinery anchored on key dates** — per-work tasks with assignees and due dates; dates fixed or relative to base dates (publication date, manuscript delivery date); templates, dependencies, reminders, calendar export. [A×2 (Consonance to-dos; OMP due dates/reminders), B×3 (Stison tasks/dependencies; Firebrand templates/alerts; Klopotek Scheduling/Notification)]
- **Schedule visualization and company-wide visibility** — Gantt/visual schedules, dashboards surfacing active works, overdue tasks, approval deadlines; notification surfaces so everyone knows "what has to be done by when". [B×3 (Stison, Firebrand, Klopotek); OMP "track every submission… falling behind" A]
- **Manuscript/production file handling** — files attached to the work's record (submission files, production files as the archive of what was sent to print); depth varies, and versioning of large files is commonly delegated to external tools. [A×2 (OMP, Consonance), B×1 (Firebrand assets)]
- **Issues/exceptions during the process** — tracked as first-class records (Consonance Issues; Stison "spot potential issues"). [A×1, B×1]
- **Configurable workflows and roles** — stage sets, role systems, and workflow steps adaptable to the publisher's process. [A×2 (OMP configurable workflow/roles; Consonance user-defined pipelines), B×2 (Firebrand "unique workflows"; Klopotek "design your own scenarios")]
- **Stage-state filters and dashboards** — drafts/forthcoming/published-style filters over the work population. [B×1 (Klopotek filters); OMP search/filter submissions A; Consonance pipeline stages A]
- **Process record persistence** — rejected/unpublished works keep their record (acquisition record, early drafts). [A×2, B×2]

### L2 — Variant / Optional Structure

- **Packaging**: standalone editorial-workflow system (OMP) vs editorial/process core inside a publishing management suite (Consonance, Stison, Firebrand, Klopotek) vs modular bolt-on (Stison Production Manager).
- **Segment calibration**: scholarly/academic (peer-review rounds as a standard stage, DOIs/ORCID/OAI-PMH, open access, multilingual, in-system catalog publication) vs trade (acquisition-meeting gate, reader reports, production handoff, metadata delivery to the trade); children's, religious, educational variants (suite segment pages).
- **Review machinery depth**: full external peer-review rounds (OMP; Firebrand journals module) vs reader-report/acquisition-decision evaluation (trade pole) vs none evidenced (Stison/Klopotek fetched pages).
- **Destination of the workflow**: in-system publication (OMP catalog website) vs handoff to production and metadata delivery (trade products).
- **UI realization of the process**: kanban-style pipelines (Consonance), stage lists with filters (OMP), workflow-driven guided apps (Klopotek), schedule/Gantt views (Stison, Klopotek, Firebrand).
- **Tier ladders**: Lite vs Enterprise (Firebrand).
- **Deployment**: open-source self-hosted, SaaS, hosted, on-prem + cloud.
- **AI assistance**: emerging layer on title data (vendor-marketed; Klopotek AI page exists; not sampled in depth).

### L3 — Vendor-specific (Research Notes only)

- OMP: PKP ecosystem (OJS/OPS siblings), plugins, PKP hosting services, Google Scholar/OAI-PMH distribution, versioned editions, editorial metrics (response times, reviews per submission), payments/selling through the catalog.
- Consonance: pipelines' ten uses (rights/sales/catalogue/recruitment/prizes/retail), Plans with plan roles and statuses, seasons, Data Studio, exemplar-work duplication, tracked copies, GraphQL API, "Workflow" main-menu section, paired start/end to-dos standing in for durations.
- Stison: separately licensed Manager modules; stop-go P&L; printer schedule/grid reports; inconsistent publisher counts across own pages (unverified).
- Firebrand: TME/TME Lite tiers with upgrade path; EasyCatalog/InDesign catalog automation; Eloquence metadata family; journals & periodicals extension; "Publishing Workflow and Project Management" category naming; vendor metrics unverified.
- Klopotek: STREAM app family (Early Title Manager, Title Structure Manager, Title Metadata Editor, Notification Dashboard, Product 360°, Inventory Manager, Purchasing/Suppliers Online, Permission & Compliance Manager); VLB Gold Status; Editorial Meeting as named gate; "This could be your TEP workflow" PDF.

## Boundary Findings

- **vs Book Publishing Management (§27 sibling, processed 2026-09-06) — JOINT REVIEW DISCHARGED from this side; keep-both RATIFIED.** The seam the sibling pass proposed holds: editorial workflow centers on the *content process* — the work's journey through evaluation and editing to production release, with the gates, assignments, and editorial record as the managed thing. Publishing management centers on the *title as a commercial product* — money (P&L, contracts, royalties), metadata to the trade, sales, backlist. The acquisition stage genuinely overlaps (the sibling observed Firebrand marketing "track submissions and manage peer reviews" inside acquisitions and Consonance documenting acquisition pipelines and editorial-meeting gates; this pass confirms both from the editorial side). Resolution: the same events appear in both Types, but as *editorial-process stages and gates* here and as *business-lifecycle and money events* there. Suite products bundle both (all four trade samples carry both faces); a standalone realization of the editorial face exists (OMP). Remove-tests: remove the content-process depth (evaluation machinery, editing stages, editorial gates, editorial record) and keep the business lifecycle → Book Publishing Management; remove the money/metadata/sales machinery and keep the content process → this Type. Both documents cross-referenced; no directory change.
- **vs Academic Journal Management (§23, processed 2026-09-06)** — the same abstract workflow shape (container + submissions + staged workflow + evaluation + publication) realized over different objects: press/monograph/catalog (books, this Type) vs journal/article/issues (scholarly serials, that Type). The journal pass drew the line from its side ("trade publishing editorial… has different objects (titles, contracts, ISBNs) and no peer-review/issue/DOI machinery") — this pass refines that: trade editorial workflow *can* carry review machinery (Firebrand "manage peer reviews"; scholarly-press use of trade suites), and the scholarly monograph pole (OMP) carries full peer review while remaining book-shaped ("The full, end-to-end solution for publishing books"). OMP deliberately straddles the seam; it is claimed by this leaf (per the sibling pass's own assignment and OMP's book self-positioning), with the scholarly calibration recorded as a segment variant. Keep-both; the straddle is recorded for the taxonomy pass.
- **vs Peer Review Platform (§23, processed 2026-09-08)** — the review exchange (reviewer–submission pairing, review records as first-class objects, outcome loop) vs the editorial workflow (review is one stage inside the work's process; the work, not the review, is the unit of record). OMP carries review machinery as a stage; a peer-review platform centers the exchange itself and is container-agnostic. Keep-both, consistent with that pass's own boundary work.
- **vs Newsroom Management System / News Publishing Platform (§27, processed 2026-09-08)** — per-title, project-like editorial process with a publication horizon and production handoff vs the newsroom's continuous produce-and-publish loop over a story stream with public channels and post-publication correction semantics. Different unit (work vs story), different cadence (campaign-to-pub-date vs continuous), different destination. The news-publishing pass noted the expected distinguishability "by object and cadence" — confirmed.
- **vs Magazine & Periodical Management (§27, processed 2026-09-08)** — the periodical business system (publication, issue cycle, ads, circulation) vs the editorial content process. Editorial tracking with versioning is a standard capability there (flatplans); here the manuscript's process is the center. The magazine pass's own framing (editorial tracking as L1 capability) supports keep-both.
- **vs Workflow Management Platform / Approval Workflow Platform (§10, generic)** — generic workflow tools manage arbitrary processes over arbitrary records; this Type's stages, gates, roles, and unit are publishing-specific (acquisition, reader report, copyedit, proof, transmittal; work/title semantics). Strip the publishing semantics → generic workflow tool (the (2)+(3) without (1) remove-test).
- **vs Project Management Application (§03.07)** — production schedules resemble project plans, but the unit is the publishing work with editorial stage semantics and publishing gates, and the record persists as the work's editorial history. Strip title/editorial semantics → generic PM.
- **vs Document Editor / Collaborative Document Editor (§03.01)** — the editing work itself (writing, revising, tracked changes) happens in editors; the workflow system routes and tracks the process. Consonance explicitly delegates large-file versioning to Dropbox — same-vendor evidence that content editing is not this system's job.
- **vs Desktop Publishing / Page Layout (§04.17)** — layout/typesetting is executed in DTP tools; the workflow tracks the tasks and archives the files (Firebrand pushes catalog data *into* InDesign; Consonance archives finished files).
- **"去掉什么就变成另一个 Type" 判据**: remove the staged process/gates → title database + task tracker; remove the work-as-unit → generic workflow/approval tool; remove the editorial stages and keep only the review exchange → Peer Review Platform; add the journal container + issues + article publication → Academic Journal Management; add money/contracts/metadata/sales machinery → Book Publishing Management; change the unit to the story and the cadence to continuous → newsroom/news-publishing territory.

## Historical / Market-Sample Check

- **Era**: the paper-era editorial office (submission file/log, reader report forms, acquisition decision, editing rounds, transmittal memo) satisfies all three L0 legs with no software. Firebrand TME (1994) and OMP (2000s) represent two software generations. Nothing in L0 requires cloud, ONIX, kanban, or digital-file management.
- **Region**: the reachable sample is UK/US/Germany/Canada-heavy (inherited from sibling passes' reachable set); regional/legacy products (virtuos, Titleplay, CatS, Broadland) unreachable across three sibling passes — recorded as limitation. Regional conventions (German VLB, national classification schemes) sit at L2 configuration.
- **Position**: scholarly presses (OMP; Consonance scholarly segment; Stison university-press customers per sibling pass), trade publishers, and small publishers (TME Lite; Stison SMB) all fit the same core; the scholarly calibration adds review-round machinery (L2), not new structure.

## Uncertainties

1. **OMP production-stage internals** — the four-stage workflow ("submission, review, copyediting and production") is named on the official product page, but stage-internal detail (layout/proofreading steps inside production) could not be verified: PKP user docs behind an anti-bot challenge. No internal detail asserted.
2. **Standalone trade-editorial-workflow products** — the reachable trade sample bundles the editorial workflow inside publishing management suites; the only standalone pole observed (OMP) is scholarly. Whether a standalone trade-book editorial workflow product category exists is unverified; recorded, not resolved. The Type stands on the structure, not on the packaging.
3. **Reader-report machinery in trade products** — not evidenced on fetched Stison/Klopotek pages; review-machinery claims calibrated to OMP/Firebrand/Consonance-scholarly evidence.
4. **Vendor counts** (Stison 150+/300+) — inconsistent marketing claims, unverified; not used.
5. **Exact stage vocabularies** — configurable everywhere; no canonical stage list asserted; gate *structure* (not stage names) is the invariant.
6. **Sample skew** — search engines unusable this pass; sampling relied on sibling-pass-known vendors plus the sibling-assigned OMP pole. Smaller regional products and in-house systems unobserved; claims calibrated (no precise numeric limits, defaults, or state vocabularies asserted in the final document).

## Final Synthesis

A Publishing Editorial Workflow application is the system that manages a publishing work's editorial process: the work enters as a submission, proposal, or early draft — before any publication decision — and is carried as a persistent editorial record through an ordered, configurable set of stages (entry, evaluation, editing, release toward production), advancing only through explicit recorded gates (acquisition/editorial-meeting decisions, review outcomes, approvals), with each stage's work assigned to identified editorial roles (acquiring editors, reviewers/readers, copyeditors, proofreaders, production editors) under deadlines with visible progress and overdue state. Around this core, mature products add submission wizards and proposal briefs, evaluation machinery (reviewer assignment with due dates, reminders, overdue visibility; acquisition-meeting organization), task/to-do systems anchored on key dates (publication date, manuscript delivery date) with dependencies, templates, reminders, and calendar export, schedule visualization and company-wide notification, manuscript/production file attachment and archiving, issue tracking, and configurable workflows and roles. The market realizes the Type in two packagings — the standalone editorial-workflow system (scholarly-monograph pole) and the editorial/process core inside a publishing management suite (trade pole) — with segment calibrations (scholarly peer-review rounds, DOIs/OAI infrastructure; trade acquisition gates and production handoff). The Type is bounded from Book Publishing Management (content process vs title-as-commercial-product; the acquisition-stage overlap resolved as the same events playing different structural roles), Academic Journal Management (same workflow shape over journal/article objects), Peer Review Platform (review as one stage vs the review exchange as the whole), the newsroom/news-publishing Types (per-title gated process vs continuous publish loop), Magazine & Periodical Management (content process vs periodical business), and generic workflow/project/document tools (publishing-specific stages, gates, unit, and semantics).
