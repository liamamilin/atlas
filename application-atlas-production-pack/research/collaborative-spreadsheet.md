# Research Notes — Collaborative Spreadsheet

## Research Goal

Understand what a Collaborative Spreadsheet is as an Application Type: the spreadsheet grammar it edits (grid / cell / formula / recalculation), how multi-user collaboration is layered onto that grammar (shared live workbook, cell-level presence, sharing, protection), where the workbook lives and how it is organized, and where the boundary sits against the sibling Spreadsheet Application, the Structured Table / Lightweight Database Application, the Collaborative Document Editor, and work-management products built on grids.

## Initial Boundary

- The leaf sits under 03.03 Spreadsheets & Tables, between "Spreadsheet Application" and "Structured Table / Lightweight Database Application".
- Working hypothesis: the type = spreadsheet grammar (addressable grid of cells, values + formulas referencing cells, automatic recalculation) + the collaboration layer (one shared persistent workbook, shared access beyond one author, concurrent multi-user editing merged into a single live version) — the same skeleton already recorded for Collaborative Document Editor and Collaborative Presentation Editor, with a different artifact grammar.
- Nearest neighbors: Spreadsheet Application (same grammar, no shared-live layer), Collaborative Document Editor (processed; same collaboration skeleton, text-flow grammar), Structured Table / Lightweight Database (unprocessed; record/field model, likely Airtable pole), Digital Whiteboard (unprocessed; unbounded canvas), Work/Project Management Platform (grid-as-work-management drift), BI/Dashboard Platform (presentation of data vs editable calculation artifact).

## Research Questions

1. What is the core object model? (workbook, sheets/tabs, grid, cell, formula, range, named ranges)
2. How does concurrent multi-user editing work on a cell-addressed artifact? (live keystroke merge vs save/refresh cadence; conflict rule)
3. What sharing/permission models exist? (invites, links, graded roles, guests, request access)
4. What sub-document controls exist? (protect sheets/ranges, lock rows/columns — how does a shared grid protect parts of itself from co-editors?)
5. What collaboration surfaces attach to cells? (comments, @mentions, change highlighting, cell history, activity log)
6. Version history / restore? Named versions?
7. What container model holds workbooks? (file-in-drive vs workspace-native)
8. What spreadsheet machinery is standard? (function library, sort/filter, charts, pivot tables, data validation, conditional formatting, freeze, find/replace, number formats)
9. What interchange exists? (xlsx/csv/ods import-export, download, publish)
10. Which advanced layers are variant rather than defining? (automation/scripts, connected data, AI, work-management objects)
11. Where is the line vs Spreadsheet Application, Structured Table / Lightweight Database, Collaborative Document Editor?

## Representative Products

| Product | Why selected | Evidence level reached |
|---|---|---|
| Microsoft Excel (Microsoft 365 / Excel for the web) | incumbent standard, .xlsx ecosystem, desktop-lineage co-authoring | Tier-1 deep (co-authoring article + Share-and-print category + help hub) |
| Smartsheet | grid-as-work-management philosophy, business tier | Tier-1 deep (help center: share overview, permission-level matrix, simultaneous-work article + hub taxonomy) |
| Numbers for iCloud | platform-native check (Apple ecosystem, iWork) | Tier-1 structural (full user guide TOC + welcome/chapter captions) |
| Zoho Sheet | suite/SMB/regional alternative, different vendor tier | Tier-1 hub level (help hub: user guide scope + functions count; KB body unreachable) |
| Google Sheets | cloud-native incumbent, free/edu mass tier | market anchor only (support ×2 + product page ×1 timeouts; zero operational claims) |
| Airtable (boundary anchor only) | structured-table / app-platform pole | Tier-2 positioning page only (no operational claims) |

## Sources

- Microsoft Support — Excel help & learning hub: https://support.microsoft.com/en-us/excel (fetched 2026-09-06)
- Microsoft Support — Share and print (Excel category): https://support.microsoft.com/en-us/excel/share-and-print (fetched 2026-09-06)
- Microsoft Support — Collaborate on Excel workbooks at the same time with co-authoring: https://support.microsoft.com/en-us/excel/get-started/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring (fetched 2026-09-06)
- Smartsheet Help Center — home: https://help.smartsheet.com/ (fetched 2026-09-06)
- Smartsheet — Overview: Share sheets and reports: https://help.smartsheet.com/articles/520104-share-sheets-reports (fetched 2026-09-06)
- Smartsheet — Permission levels on sheets, reports, or workspaces: https://help.smartsheet.com/articles/2483288/sharing-permission-levels (fetched 2026-09-06)
- Smartsheet — Work with multiple people on a sheet at the same time: https://help.smartsheet.com/articles/522069-work-with-multiple-people-on-a-sheet-at-same-time (fetched 2026-09-06)
- Apple — Numbers User Guide for iCloud (welcome + TOC): https://support.apple.com/guide/numbers-icloud/welcome/icloud (fetched 2026-09-06)
- Zoho Sheet — User guide, FAQs, and help resources hub: https://www.zoho.com/sheet/help/ (fetched 2026-09-06)
- Airtable — homepage / platform positioning: https://www.airtable.com/ (fetched 2026-09-06)
- Google — support.google.com (Sheets training answer + docs answer): timeout ×2 — abandoned; google.com/sheets/about: timeout ×1 — abandoned. Google Sheets used as market anchor only.

### Source-access limitations

- Google Sheets: no operational documentation reachable. No claim about Google Sheets' operational behavior appears anywhere in this research or the final document beyond its standing as a widely known collaborative spreadsheet product.
- Zoho Sheet: KB index and FAQ returned empty content; evidence limited to the official help hub (user-guide scope sentence, functions list existence, API guide existence). No operational detail asserted.
- Numbers for iCloud: chapter structure and chapter captions captured (direct), but individual article bodies were not fetched; per-feature behavior described only at the level the TOC/captions state.
- Smartsheet: three deep articles + hub captured; premium module behavior taken from module descriptions only.
- No numeric limits (cell counts, collaborator counts, version-retention windows, function counts beyond Zoho's self-published "350+") are asserted for any product anywhere in the final document.

## Product A — Microsoft Excel (Microsoft 365 / Excel for the web)

### Key observations (evidence A)

From the help hub (category taxonomy):

- Top-level sections: Get started / **Collaborate** (→ Share and print) / Formulas & functions / Import & analyze / Format data / Troubleshoot.
- "Get more done" highlights: Analyze data with Copilot in Excel, stocks and geography data types, "Turn your data into insights" (Analyze Data), alphabetical function list, XLOOKUP / VLOOKUP / IF, drop-down list (data validation), combine text from cells, freeze panes, PivotTables (create / sort / design), PivotChart, sparklines, slicers, import/export .txt/.csv, import data from the web, quick-start macro, data validation, find or replace.

From the "Share and print" category:

- Share files: "Share your Excel workbook with others"; "Work on a file at the same time with co-authoring"; password protect a workbook; **protect a worksheet with or without a password**; print articles (landscape/portrait, print area, page breaks, repeat rows/columns, gridlines, scaling).

From the co-authoring article (deep):

- Definition: "You and your colleagues can open and work on the same Excel workbook. This is called co-authoring. When you co-author, you can see each other's changes quickly—in a matter of seconds." Certain versions show "other people's selections in different colors."
- Preconditions: Microsoft 365 subscription; sign-in; **file must live on OneDrive, OneDrive for Business, or SharePoint Online** (SharePoint On-Premises does not support co-authoring); .xlsx/.xlsm/.xlsb formats (Strict Open XML not supported).
- Share flow: Share button → email addresses → default "Can edit" (toggleable) → optional message → or Copy link. Link defaults in the web app: "anyone in your organization can use the link to open and edit"; link settings dialog adjusts who/what.
- Presence: people icons/initials in the upper-right ("G" stands for guest); others' **cell selections shown in colors** (own selection always green; hover reveals the person's name; "Go to" jumps to where someone is working). On some clients you see changes but not selections.
- **AutoSave**: enabled when the file is stored on OneDrive/SharePoint; "automatically saves your changes to the cloud as you're working"; other people see your changes "in just a matter of seconds".
- Change surfacing: **Show Changes** pane (web) "where you can see the changes, including previous cell values".
- Version history: File > Info > Version History; open a past version; **restore only when everyone is no longer co-authoring**; on iOS/Android via File > History/Restore.
- Conflict rule: "In general, the last change that is saved... is the one that 'wins.' There are some exceptions... If you don't want to have conflicts with other people, **assign areas or sheets to each person**."
- Failure modes: "File is locked" if anyone opens the file with a non-co-authoring version; "Refresh recommended" / "Upload failed" when an unsupported feature is used — co-authoring can pause; remediation via Save a Copy and manual merge of needed changes.
- Offline: "if you're using OneDrive to sync files, changes you make while your computer is offline won't get merged until your computer is online again... once online, all your changes get merged at once."

Interpretation: Excel's collaboration layer is a cloud-storage precondition (file-in-drive) + continuous AutoSave merge + presence + version history, wrapped around the unchanged spreadsheet grammar (worksheets, cells, functions, PivotTables, protection). The desktop single-user, no-cloud mode is the sibling leaf "Spreadsheet Application" — the same product documents both sides of the seam.

## Product B — Smartsheet

### Key observations (evidence A)

From the help hub (category taxonomy):

- Building your solution: Sheets and rows ("Rows represent individual items or tasks within a sheet"), Columns, Forms, Templates, Formulas and functions, Automated workflows, Dashboards, Reports, Views ("timeline, board, grid, Gantt, card, and calendar views"), Workspaces, Attachments, Widgets.
- Sharing and collaboration: Sharing assets and items, Conversations, WorkApps (role-based views).
- Premium modules: Pivot App, DataMesh, Data Shuttle, DataTable, Dynamic View, Control Center, Calendar App, Resource Management, Brandfolder, Bridge.
- Analytics and insights: Create and manage reports; AI in Smartsheet: Conversational AI.

From "Overview: Share sheets and reports" (deep):

- Share a sheet or report with collaborators inside or outside the organization; collaborators can **request access to items**; outside collaborators don't always need Smartsheet accounts to view.
- Share modal: add people by name/email/**group**; per-person **permission level dropdown**; optional message; Notify people / Cc myself; **Default View** for collaborators; Copy link ("Only people with a Smartsheet account and shared to the item can use the link"); stop sharing or change levels at item and workspace levels.
- Governance: "You can't give another collaborator a higher access level than you have"; Manage access window with search/sort; seat types (Member / Contributor / Guest / Provisional Member) gate what permissions can be assigned; Plan Asset Admins review access requests; System Admins can prevent sharing; Group Admins remove group members to remove access.
- Workspace sharing for groups; **sharing a report does not grant access to its source sheets** (collaborators see only data from source sheets they can access).
- Contact-column sharing: adding unshared contacts to a contact column prompts to share them to the item (Editor-can-share default).

From "Permission levels on sheets, reports, or workspaces" (deep):

- Per-item roles: **Viewer / Commenter / Editor / Admin / Owner** (+ Plan Asset Admin, non-collaborative).
- Distinctly spreadsheet-shaped capability ladder: Viewer sees all data incl. comments, exports, filters; Commenter adds attachments/comments; **Editor edits unlocked rows/columns, inserts rows, moves rows (within and across sheets)**; **Admin additionally: edits cells in locked columns/rows, deletes locked rows, inserts/renames/deletes columns, moves/hides columns, locks or unlocks columns and rows, edits conditional formatting rules, renames/deletes the sheet, creates/manages forms, publishes, creates shared filters**; Owner additionally restores deleted items.
- Collaboration controls: share (Editor+), change others' permissions (Admin+), send sheet/rows via email, publish (Business/Enterprise), **Update Requests** (send and edit), submit forms.
- Automation: row-level and sheet-level reminders/alerts per user; **automated workflows (approval requests, automated update requests)** Admin+.
- Project management objects: dependencies in project settings (Admin), **critical path** display, **baselines** create/edit (Admin) / view (all).
- AI tools: generate formulas, text and summaries (Editor+), analyze data (all levels).

From "Work with multiple people on a sheet at the same time" (deep):

- **Active faces**: images/icons next to the Share button when others are viewing or working on the sheet; hover for information.
- **Pop-up messages** when someone opens a sheet you're using; when a collaborator **saved** changes: File > Refresh to see saved changes.
- **Highlight Changes**: background color applied to changed cells.
- Same-cell conflict: "the cell displays the last saved change"; **View Cell History** per cell (right-click).
- Related: View changes made to items (cell history), **activity log** for tracking changes.

Interpretation: Smartsheet keeps the full spreadsheet grammar (grid, columns with types, formulas — a published functions list, cross-sheet formulas, cell history) but rebuilds the container as a workspace-native, permission-rich work object: row = item/task, forms feed rows, automations and approvals run on rows, views (Gantt/board/calendar/timeline) re-present the same rows, reports aggregate across sheets. Collaboration machinery (5-level per-item ladder, request access, contact-column sharing, default view, seat gating) is richer than the file-in-drive products. Its change-merge cadence is coarser ("saved changes" + Refresh) than Excel's AutoSave-seconds model — an implementation spread within the same Type.

## Product C — Numbers for iCloud

### Key observations (evidence A — chapter structure + captions)

From the user guide TOC and welcome:

- Grammar: spreadsheets begin with a **template**; content lives in **tables** ("Add data to a table... enter your own data or import data from another file... add a wide range of formulas, like sum or average, to any cell"); **sheets** (tabs) organize the spreadsheet ("Organize your spreadsheet with different sheets for each type of information you want to track—income, expenses"); tables + text + images/shapes/media are objects positioned on the sheet (layer/group/lock objects) — Numbers' grammar is a canvas-of-tables rather than one uniform grid.
- Table machinery: add/delete tables, select cells/rows/columns/tables, add rows/columns, merge/unmerge cells, table styling, enter text and numbers, **add formulas / change existing formula**, checkboxes and other cell controls, clear content and formatting, currency/other formats, Formulas and Functions Help.
- Organize/analyze: sort, **filter data**, **categories** (group into categories, edit groups, summarize group data), **pivot tables** (intro/create/arrange/sort/group/refresh/**view the source data for a value**), charts (2D and interactive; "When you make changes to the data in the table, the chart updates automatically").
- Collaboration chapter: **"Collaborate in real time — Invite others to work with you on your spreadsheet. Everyone you invite can see changes as they're made, but you control who can edit or only view the spreadsheet."** Sub-chapters: intro to collaboration, invite others, collaborate on a spreadsheet, change shared spreadsheet settings, stop sharing, **shared folders and collaboration**, **use Box to collaborate**.
- Manage: save/name/duplicate, delete/**recover spreadsheets**, **restore earlier versions**, organize spreadsheets, **password-protect spreadsheets**, download spreadsheets (interchange), upload/sync.
- Writing/editing tools: spell-check, find and replace, **add or reply to comments**, **set your author name and color**.
- Troubleshooting: "If you can't find a spreadsheet", **"Resolve spreadsheet conflicts"** (evidence that concurrent editing can produce conflicts needing resolution).
- Positioning: "Collaborate in real time" is a top-level welcome card — collaboration is a first-class chapter of the platform-native spreadsheet, not an add-on.

Interpretation: Numbers passes the platform-native check: the same collaboration skeleton (invite, everyone sees changes as made, edit-vs-view control, version restore, comments, conflicts) exists outside the cloud-suite/file-drive pattern, with iCloud/Box as the storage substrate and a different in-sheet grammar (multiple tables per sheet).

## Product D — Zoho Sheet

### Key observations (evidence A at hub level, limited depth)

From the official help hub:

- Positioning: "Guides you, step by step, through the process of creating, editing, **analyzing data, sharing, and collaborating** on your spreadsheets, using Zoho Sheet."
- **Functions**: "a list of more than 350 functions supported in Zoho Sheet, along with syntax and description."
- REST API guide ("integrate Zoho Sheet with third-party applications, or build your own application based on Zoho Sheet"); community; what's new; FAQs (unreachable body); user guide KB (index unreachable).
- Suite membership: Zoho Sheet is a member application of the Zoho suite (help hub shared with other Zoho apps).

Interpretation: A suite-member collaborative spreadsheet from a different vendor tier, with the same four-part scope (create/edit/analyze/share+collaborate). Depth of evidence does not support any operational claims.

## Product E — Google Sheets (market anchor only)

- All fetch attempts failed (support.google.com ×2, product page ×1). No operational claims recorded. Google Sheets is retained in the sample only as the universally recognized cloud-native collaborative spreadsheet that anchors the market position; everything the final document says about the Type is supported by the other four products.

## Product F — Airtable (boundary anchor only, not part of the Type's sample)

- Homepage positions Airtable as "the system of record for your workflows, data, and agents" — a "next-gen app-building platform": bases, records, **databases** ("use relational databases to connect data from apps, workflows, and tools"), **interfaces** ("create custom interfaces from your data"), views, automations, AI agents, governance; onboarding path: "Describe the app you need in plain words, or **drop in a spreadsheet you already have**."
- Interpretation: the spreadsheet-looking surface sits on a record/field data model with app-building semantics (interfaces, agents) — the Structured Table / Lightweight Database Application pole. "Drop in a spreadsheet" confirms adjacency (spreadsheets as the import on-ramp) rather than identity. No operational claims used.

## Cross-product Comparison

| Dimension | Excel 365 | Smartsheet | Numbers for iCloud | Zoho Sheet | Google Sheets (anchor) |
|---|---|---|---|---|---|
| Grid grammar | workbook → worksheets → cell grid; functions; PivotTables | sheet → columns (typed) × rows; functions list; cross-sheet formulas | sheet (tab) → multiple tables + objects; formulas per cell | create/edit/analyze scope; 350+ functions | (not researched) |
| One live shared version | yes — co-authoring on OneDrive/SharePoint, AutoSave, seconds | yes — simultaneous work; save/refresh cadence; cell history | yes — "see changes as they're made" | positioning states sharing+collaborating | market-known |
| Shared access beyond one author | invite emails / org links; Can-edit toggle; guest ("G") | per-person/group permission levels; request access; non-members view | invite; edit-or-view control; shared folders; Box | share + collaborate scope | market-known |
| Concurrent merge granularity | continuous (AutoSave, seconds) | per-save + Refresh; Highlight Changes; View Cell History | continuous ("as they're made") | unknown | (not researched) |
| Presence | people icons; colored cell selections; hover name; Go to | active faces; pop-ups | author name/color; collaboration menu | unknown | (not researched) |
| Change surfacing | Show Changes pane incl. previous cell values | Highlight Changes background; cell history; activity log | version restore; conflict resolution | unknown | (not researched) |
| Sub-document edit restriction | protect worksheet/workbook (password) | lock/unlock columns+rows (Admin); locked-cell edit = Admin+ | password-protect whole spreadsheet | unknown | (not researched) |
| Version history / restore | Version History; restore when all left co-authoring | restore deleted items (Owner); activity log | restore earlier versions; recover deleted | unknown | (not researched) |
| Roles ladder | edit vs view (binary, per fetch) | Viewer/Commenter/Editor/Admin/Owner | edit vs view | unknown | (not researched) |
| Comments | (not in fetched pages) | per-row comments + attachments; Commenter role | add/reply to comments | unknown | (not researched) |
| Container | file on OneDrive/OneDrive-Business/SharePoint Online | item in Workspaces; workspace sharing | iCloud drive; shared folders; Box | suite account | (not researched) |
| Notifications | share email | Notify people; reminders/alerts per row/sheet; update requests | unknown | unknown | (not researched) |
| Forms | (not evidenced) | create forms (Admin); submit forms; forms feed rows | (not evidenced) | unknown | (not researched) |
| Automation | quick-start macro (desktop) | automated workflows: approvals, update requests | (not evidenced) | unknown | (not researched) |
| AI | Copilot: analyze/clean data | AI: generate formulas, summaries, analyze data | (not evidenced) | unknown | (not researched) |
| Interchange | xlsx/xlsm/xlsb; csv/txt import-export | export; publish; email rows/sheets | download spreadsheets; upload; sync | API; (functions) | (not researched) |
| Beyond-spreadsheet drift | desktop-lineage governance (protection, macros) | rows-as-tasks, Gantt/board/calendar views, dependencies, critical path, baselines, dashboards/reports | freeform objects on sheet (canvas-of-tables) | suite integration | (not researched) |

## Canonical Model

### L0 — Defining Invariant

```text
Shared persistent workbook (one live current version, no save/pass-around loop)
└── Spreadsheet grammar: addressable grid of cells holding values and formulas
    that reference other cells and recalculate automatically
└── Shared access beyond one author (the product's sharing mechanism)
└── Multi-user editing merged into the single live current version
```

Four properties. Remove the shared-live layer → Spreadsheet Application (single-user editing, file pass-around). Remove the grid+formula grammar → not a spreadsheet (Collaborative Document Editor, Whiteboard, or Structured Table territory). Remove shared access or multi-user merge → back to the single-author sibling. Nothing about drive-vs-workspace containers, live-vs-refresh merge cadence, roles depth, AI, or work-management objects is required by the definition.

### L1 — Common Mature Structure

- **Sharing machinery** — invite by identity (email/name/group), share links, graded roles (view / comment / edit / manage), request access, manage/stop sharing. (Excel: invite+link+can-edit; Smartsheet: 5-level ladder + groups + request access; Numbers: invite + edit-or-view.)
- **Cell-level presence** — indicators of who is in the workbook and where they are working (Excel: colored cell selections + hover name + Go to; Smartsheet: active faces; Numbers: author name/color).
- **Cell/row-anchored comments** — discussion attached to the addressed location, with authorship (Smartsheet row comments + Commenter role; Numbers add/reply to comments with author color).
- **Version safety** — version history with browsing and restore; recovery of deleted items (Excel Version History; Numbers restore earlier versions/recover; Smartsheet activity log/cell history/restore deleted).
- **Sub-document edit restriction** — protecting parts of the grid from editing while the rest stays open (Excel protect worksheet/workbook; Smartsheet lock columns/rows with Admin-only locked-cell edit). Distinctly spreadsheet-shaped collaboration control.
- **Change surfacing** — ways to see what others changed: change panes with previous values, highlighted changed cells, per-cell history, activity logs (Excel Show Changes; Smartsheet Highlight Changes + cell history + activity log).
- **Spreadsheet machinery** — function library (Excel alphabetical list; Zoho 350+; Smartsheet functions list; Numbers Formulas & Functions Help), sort/filter, charts that update from table data, pivot tables (Excel; Numbers; Smartsheet Pivot App), number formats, merge cells, freeze panes, find/replace, data validation/drop-downs (Excel), conditional formatting (Excel + Smartsheet), multi-sheet workbooks.
- **Interchange** — import/export of grid formats (Excel csv/txt; Numbers download spreadsheets/upload/sync; Smartsheet export), print/pagination.
- **Organization + templates + search** — template start (Numbers template chooser; Smartsheet templates), organization of workbooks, findability.
- **Web + mobile + desktop surfaces** sharing one live version (Excel across five platforms; Numbers on iCloud web; Smartsheet mobile + desktop app).

### L2 — Variant / Optional Structure

- **Container philosophy** — file-in-cloud-drive (Excel: OneDrive/OneDrive-Business/SharePoint Online; Numbers: iCloud, optionally Box) vs workspace-native items (Smartsheet workspaces). Same L0 either way.
- **Merge-cadence philosophy** — continuous AutoSave merge (Excel: seconds; Numbers: "as they're made") vs saved-change + refresh cadence with per-cell history (Smartsheet). The L0 invariant (one merged current version) holds across the spread.
- **Roles depth** — binary edit/view (Numbers, per fetched evidence) vs five-level ladder with seat gating (Smartsheet).
- **Grid-as-work-management variant** — Smartsheet: rows as tasks/items, forms feeding rows, update requests, approval automations, dependencies/critical path/baselines, Gantt/board/calendar/timeline views, dashboards/reports. Keeps grid+formula core; drifts toward Project/Work Management.
- **In-sheet grammar variant** — Numbers: canvas-of-tables (multiple tables + freeform objects per sheet) vs uniform single grid.
- **Offline posture** — offline edits merge on reconnect (Excel OneDrive sync); desktop app (Smartsheet); platform sync (Numbers).
- **Automation layer** — desktop macros (Excel quick-start), workflow automations/approvals on rows (Smartsheet). Scripting/automation platforms exist beyond the sampled evidence; keep as optional layer.
- **Connected/scale data** — import from the web, data types (Excel stocks/geography), premium large-data tables (Smartsheet DataTable/Data Shuttle).
- **AI assistance** — formula generation, data analysis, cleanup (Excel Copilot; Smartsheet AI tools). Emerging-common, not definitional.
- **Suite membership** — spreadsheet as member application of a wider productivity suite (Excel in Microsoft 365, Zoho Sheet in Zoho, Numbers in iWork) vs standalone.
- **Identity/guest posture** — organization links with guest indicators (Excel "G"), non-member view-only + seat types (Smartsheet), platform-account invites (Numbers).

### L3 — Vendor-specific Structure (Research Notes only)

- Excel: AutoSave preconditions; .xlsx/.xlsm/.xlsb requirement; Strict Open XML unsupported; "File is locked" dynamics; "Refresh recommended"/"Upload failed" remediation via Save a Copy; green self-selection; "Go to"; guest "G"; Show Changes pane; restore gated on "everyone no longer co-authoring"; Protected View; mailing labels; print-area/page-break machinery; stocks & geography data types; XLOOKUP/VLOOKUP; sparklines; slicers; quick-start macro; Copilot clean-up.
- Smartsheet: seat types (Member/Contributor/Guest/Provisional Member); Plan Asset Admin; USM vs Legacy model tabs; Default View; contact-column sharing with Editor-can-share default; Update Requests; approval automations; dependencies/critical path/baselines; cell history via right-click; Highlight Changes; active faces; premium modules (Pivot App, DataMesh, Data Shuttle, DataTable, Dynamic View, Control Center, WorkApps, Bridge, Calendar App); Regions/Gov capability splits; AI generate-formulas permission mapping.
- Numbers: template chooser; categories (group + summarize); pivot with source-data inspection; interactive charts; checkboxes/cell controls; merge cells; author name/color; Box collaboration; spreadsheet-conflict resolution flow; iCloud upload/sync.
- Zoho Sheet: 350+ function count; REST API positioning; suite-shared help hub.
- Airtable (boundary anchor): bases/records/interfaces/agents positioning; "drop in a spreadsheet" on-ramp.

## Vendor-specific Findings

- Excel's co-authoring is conditioned on cloud storage and file format (evidence A). This is an implementation precondition, not a Type requirement — Numbers proves the same skeleton on iCloud/Box, Smartsheet on its own workspace platform.
- Smartsheet's permission ladder is far deeper than any other sampled product's (evidence A for Smartsheet; others evidence only edit/view at fetched depth). Treat the five-level ladder as L2 depth variation, not canonical.
- Smartsheet's "rows as tasks" object overlay (dependencies, critical path, baselines, forms, update requests) is product-family-specific work management built on the grid — L2 variant with drift toward Project/Work Management.
- The 350+ function count is Zoho's self-published figure; no cross-product function-count comparison is valid or asserted.

## §24 Historical / Market-Sample Check

Check applied: would older, regional, platform-native, or differently positioned products still fit the definition?

- Platform-native: Numbers for iCloud fits fully (invite, live changes, edit-vs-view, versions, comments) — L0 holds outside the cloud-suite/file-drive pattern. ✓
- Regional / SMB suite: Zoho Sheet fits at the scope level its official hub states (create/edit/analyze/share+collaborate). ✓ (evidence depth limited; recorded in Uncertainties.)
- Era check: before cloud co-authoring, multi-user spreadsheet work was done by emailing file copies or by legacy file-level shared-workbook mechanisms. Those patterns fail the L0 test (no single live current version, no merged multi-user editing) — which is precisely why "Collaborative Spreadsheet" is a separate leaf from "Spreadsheet Application": the defining layer is the live shared version itself. The Type is era-honest because its defining property is the collaboration layer; older single-user spreadsheet products classify under the sibling leaf. (Reasoning recorded here; legacy-mechanism specifics were not fetched and are not asserted as operational facts.)
- Differently positioned grid products (Airtable pole) fail the L0 formula/recalculation-centric grammar test — they belong to the Structured Table / Lightweight Database Application leaf. ✓ (boundary confirmed, not a taxonomy conflict)

## Boundary Findings

- **vs Spreadsheet Application (sharpest seam)** — remove the shared live version and multi-user merge → single-user desktop app with file pass-around. Excel itself documents the seam from inside one product: desktop-only, no-cloud workbooks are the sibling leaf; co-authoring begins when the file lives on a cloud location. The two leaves are capability-layer siblings; several products span both.
- **vs Structured Table / Lightweight Database Application** — the spreadsheet's center is the addressed cell + formula + recalculation over an open-ended grid; the structured-table pole's center is typed fields, records, and linked-record relational semantics with views over records (Airtable: databases/interfaces/agents positioning; "drop in a spreadsheet" as the import on-ramp). Remove formula-recalculation as the computation model and add typed-field/linked-record semantics → different Type.
- **vs Collaborative Document Editor** — same collaboration skeleton (shared live artifact, shared access, concurrent merge, presence, comments, versions), different artifact grammar: addressed grid of calculated cells vs flowing text. (Consistent with the recorded seam in the collaborative-document-editor research notes: "same skeleton, different grammar".)
- **vs Digital Whiteboard** — unbounded freeform canvas vs row/column-addressed cells with formula semantics.
- **vs Project/Work Management Platform** — Smartsheet shows the drift path (rows→tasks, Gantt, approvals). Test: if rows are managed as scheduled, dependent work items and the grid is merely the surface, the product is drifting; if rows remain cells in a calculation grid, it stays a collaborative spreadsheet.
- **vs BI / Dashboard Platform** — the collaborative spreadsheet's analysis happens inside the editable calculation artifact; dashboard products present governed data. Dashboard modules attached to grids (Smartsheet) are add-on surfaces, not the Type.
- Boundary note for the directory: the Spreadsheet Application / Collaborative Spreadsheet split is capability-based, not product-based — the same vendors ship both modes. Flagged for joint review with the (unprocessed) sibling.

## Uncertainties

- Google Sheets: zero fetched evidence; used as market anchor only. Any Google-specific behavior is intentionally absent from both documents.
- Zoho Sheet: evidence limited to the help hub; operational behavior unknown. No claims beyond the hub's scope sentence and functions/API existence.
- Numbers for iCloud: chapter captions captured; per-article operational depth not verified.
- Excel comments/notes and notification rules were not directly evidenced in fetched pages; treated only as cross-product common structure at L1 with Smartsheet/Numbers support, never claimed with Excel specifics.
- Merge-cadence claims are calibrated per product (Excel "seconds", Smartsheet "saved changes + refresh"); no general real-time guarantee is asserted for the Type.
- No numeric limits (cell counts, collaborator caps, version retention) asserted anywhere.

## Final Synthesis

The Collaborative Spreadsheet is the spreadsheet grammar (workbook → sheets → addressed cell grid → values + formulas → automatic recalculation) with the collaboration skeleton layered on: one shared persistent workbook in one live current version, shared access through the product's sharing mechanism (invites/links with graded roles), and concurrent multi-user editing merged into that single version — with cell-level presence, cell-anchored comments, version safety, and the distinctly spreadsheet-shaped control of protecting parts of the grid from co-editors. Containers, merge cadence, role depth, automation, connected data, and AI are implementation choices; grid-as-work-management is a variant that drifts toward Work Management when rows stop being cells and become scheduled work items.
