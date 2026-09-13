# Collaborative Spreadsheet

## Overview

A **Collaborative Spreadsheet** is a multi-user spreadsheet application built around a shared persistent workbook: the grid document lives in the product as one live current version, multiple identified people are granted access to it, and their concurrent edits are merged into that same version as they work.

The defining structure is small:

```text
Shared persistent workbook (one live current version)
└── Spreadsheet grammar: an addressable grid of cells holding values and formulas
    that reference other cells and recalculate automatically
└── Shared access beyond one author (the product's sharing mechanism)
└── Multi-user editing merged into the single live current version
```

Everything else commonly associated with modern collaborative spreadsheets — cloud drives, cell-selection cursors, threaded comments, version timelines, protected ranges, forms, automations, AI helpers — is widespread in current products but is not what makes the product a collaborative spreadsheet. Remove the shared live version and multi-user merge and the product is simply a spreadsheet application; remove the grid-and-formula grammar and it is a different kind of application entirely.

## Users & Context

The primary users are small groups of knowledge workers who need to build or maintain the same set of numbers together:

- contributors who enter and update data in the cells they are responsible for (sales figures, budgets, inventories, rosters, trackers)
- a spreadsheet author or analyst who writes the formulas and structures the sheets
- reviewers and stakeholders who mostly look at the result, leave comments, or export it

Typical occasions: a team budget or forecast that several departments fill in, a shared tracker or list that different people update throughout the day, a calculation model that an owner maintains while others inspect it, class or club sheets where anyone present can edit.

Secondary concerns belong to the workbook owner and, in organizations, to administrators: who may open the workbook, which parts co-editors may change, what the workbook looked like last week, and how the workbook moves in and out of other tools. The work environment is predominantly the browser, with desktop and mobile clients sharing the same live workbook.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as a collaborative spreadsheet:

- **One shared persistent workbook** — the artifact is a single workbook that lives in the product continuously. Nobody owns a private copy that must be emailed or re-merged; everyone works in the same current version. Without this, the product is a single-user spreadsheet with file pass-around.
- **Spreadsheet grammar** — the workbook is organized as sheets holding an addressable grid: every cell has a row-and-column identity, cells hold values, and cells can hold formulas that reference other cells and are recalculated automatically when anything they depend on changes. This grammar is what makes it a spreadsheet rather than a document, a whiteboard, or a list of records. (Mature products add a function library — lookups, sums, conditionals — on top of this grammar.)
- **Shared access beyond one author** — the owner grants access to other identified people through the product's sharing mechanism: direct invites, or links with a chosen access level, at minimum distinguishing people who may edit from people who may only view. Without this, there is no collaboration layer.
- **Multi-user editing merged into one current version** — two or more people can be in the workbook at the same time, each making changes, and the result is one merged workbook rather than competing copies. How immediately the merge is visible varies by product (some propagate changes in seconds; others show saved changes on refresh) — the invariant is the single merged result, not the propagation speed.

### Standard Capabilities of Mature Products

These make collaboration practical. They are common in mature products but not part of the definition.

- **Sharing machinery** — invite people by identity or group, generate share links, assign each person an access level (commonly some ladder among view / comment / edit / manage), let outsiders request access, and let the owner review, change, or revoke access.
- **Cell-level presence** — indicators of who is in the workbook and where they are working: lists of collaborators, colored highlights on the cells or selections each person is touching, author colors and names.
- **Comments anchored to cells or rows** — questions and notes attached to the addressed location rather than to the document as a whole, with authorship and replies. This is the collaboration surface of spreadsheets, the counterpart of the document paragraph comment.
- **Version safety** — a recorded history of the workbook's past states that can be browsed and restored, plus recovery of deleted workbooks. Some products also surface per-cell change history and activity logs.
- **Sub-document edit protection** — the ability to lock parts of the grid (sheets, ranges, rows, columns) against editing — sometimes password-protected — while the rest of the workbook remains open to co-editors. This control is distinctly spreadsheet-shaped: the unit being protected is an address range, not a paragraph.
- **Change surfacing** — ways to see what others did: panes listing recent changes with previous values, highlighting of changed cells, change logs.
- **Spreadsheet machinery** — sorting and filtering, charts that update from the data, pivot-style summarization, number and cell formatting, merged cells, frozen headers, find-and-replace, data-entry validation such as drop-down lists, conditional formatting, and multi-sheet workbooks.
- **Interchange** — import and export in common spreadsheet formats (at minimum delimited text such as CSV; usually the incumbent workbook formats), printing with repeated headers and print areas, and templates as a starting point.

### One Structure, Many Implementations

The model is stated conceptually. The Variants section below shows how implementations differ.

```text
Concept:        One shared persistent workbook
Implementations:  a file stored on a cloud drive; an item native to a platform
                  workspace; a document in a device-platform account

Concept:        Shared access mechanism
Implementations:  identity invites, organization-wide links, per-person roles,
                  account-free view links, shared folders

Concept:        Multi-user merge
Implementations:  continuous auto-save with second-level propagation;
                  saved changes surfaced on refresh with per-cell history

Concept:        Sub-document protection
Implementations:  password-protected worksheets or workbooks; locked rows and
                  columns editable only by higher access levels
```

A reader who has only seen one implementation (say, a browser workbook on a cloud drive) should still be able to recognize the others from the core model.

## How It Works

### Create and share the workbook

```text
Create a workbook (often from a template)
→ build the structure: sheets, headers, formulas
→ choose Share
→ invite people or create a link
→ set each person's access level (edit / comment / view)
```

The workbook now has a shared audience. From this point nobody "sends the file" again; everyone returns to the same workbook.

### Edit together

```text
Open the shared workbook
→ see who else is present and which cells they are working in
→ enter or change values and formulas in your cells
→ changes merge into the one current version for everyone
→ check what changed (change panes, highlighted cells, cell history)
```

Two people working in different areas never notice each other. Two people working in the same area rely on the product's conflict rule — in practice, one change prevails and the history shows what happened — which is why teams commonly agree who owns which sheet or range.

### Comment and review

```text
Select a cell or row
→ leave a comment or question
→ collaborators reply; the thread stays attached to the location
→ the workbook owner resolves and adjusts the sheet
```

Reviewers who only view can comment and export; they cannot change cells.

### Protect what must not change

```text
Identify formula areas or reference data others should not alter
→ lock or protect that sheet, range, or rows
→ co-editors keep editing the unlocked areas
```

### Correct mistakes

```text
Open version history
→ browse past states of the workbook
→ restore an earlier version (products differ on timing conditions; some
   require that no one is currently co-authoring)
```

### Move work in and out

```text
Import an existing spreadsheet file (or paste data)
→ work on it as a live shared workbook
→ export or print for people outside the product
```

### Capability tiers

**Defining core** — without these, not a collaborative spreadsheet:

- one shared persistent workbook (single live current version)
- addressable grid of cells with values and formulas that recalculate automatically
- shared access beyond one author
- multi-user editing merged into that single version

**Standard in mature products:**

- sharing machinery with graded access levels
- cell-level presence
- comments anchored to cells or rows
- version history and restore
- sub-document edit protection (protected sheets/ranges, locked rows/columns)
- change surfacing (change lists, highlights, cell history)
- sort/filter, charts, pivot summarization, formatting, multi-sheet workbooks
- import/export, print, templates

**Variant / optional:**

- container choice: file on a cloud drive vs workspace-native item
- merge cadence: continuous propagation vs saved-change-plus-refresh
- deep role ladders with per-row and per-column controls
- forms that feed rows; reminders and notification rules
- automation (rule-driven workflows, scripting/macros)
- connected external data and large-data modes
- AI assistance (formula generation, data analysis, cleanup)
- work-management overlays (rows treated as tasks with schedules and dependencies)

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Workbook grid

The primary surface: the sheet itself.

- the addressed grid, column and row headers, sheet tabs
- presence indicators on cells, colored selections of co-editors
- primary actions: enter values, write formulas, format, sort, filter, insert rows/columns, switch sheets

### Share panel

The access-control surface of the workbook.

- current collaborators and their access levels
- primary actions: invite people or groups, copy link, change someone's level, handle access requests, stop sharing

### Comments / discussion

Cell- and row-anchored conversation surface.

- comment threads tied to locations, authorship, replies, resolved state
- primary actions: add, reply, resolve

### Version history

The time-travel surface.

- list of past versions with timestamps (in some products, named or attributed versions)
- primary actions: preview, restore, recover deleted workbook

### Protection controls

The sub-document access surface.

- which sheets, ranges, rows, or columns are locked and who may still edit them
- primary actions: lock/unlock, set password or edit exceptions

### Surrounding organization surfaces

Where workbooks live and are found: a document list, drive folders, or workspace — with search, templates, and a recents list. Work-management-flavored products add views (calendar, board, timeline) over the same rows and dashboards built from the data.

## Important Rules / Behaviors

### There is exactly one current version

The workbook everyone opens is the same artifact. There is no "my copy / your copy" once sharing begins — versions exist only in history, not as parallel live documents.

### The last change to a cell prevails

When two people change the same cell around the same time, one change wins (typically the last one the product records). The remedy is organizational — assign sheets or ranges to people — and the audit is forensic: cell history and change logs show what happened.

### Access levels decide what a person can do

View may look and export, comment may discuss, edit may change cells, and higher levels may restructure the sheet, manage sharing, or lock areas. Sharing typically cannot grant a level higher than the sharer's own. Access to a derived view does not automatically confer access to the underlying data.

### Parts of the grid can be closed off while the rest stays open

Protection is finer-grained than whole-workbook permission: a locked sheet or range stays locked even for people who can edit elsewhere. This is how formula integrity is preserved in a shared workbook.

### Co-editing has failure modes

Opening a workbook with an incompatible client can lock it for everyone; unsupported features can pause merging until resolved; offline edits merge only on reconnect. Mature products surface these states rather than silently forking the workbook.

### History is the safety net

Because there is one live version, mistakes are corrected by restoring versions, not by "unsharing" a bad copy. Restoring may be deferred until co-authors have left the workbook.

## Variants

- **File-in-drive collaborative spreadsheets** — the workbook is a file in a personal or organizational cloud drive; sharing rides on the drive's identity system. The dominant modern pattern.
- **Workspace-native collaborative spreadsheets** — the sheet is an item inside a platform workspace with per-item roles, groups, request-access flows, and seat gating; collaboration machinery runs deeper than the file model.
- **Platform-native suites** — the spreadsheet ships inside a device or office-suite ecosystem with its own account layer and companion file formats.
- **Grid-as-work-management spreadsheets** — rows are managed as tasks or items: forms collect rows, reminders and approvals fire on rows, and calendar, board, and timeline views re-present the same grid. The calculation core stays intact while the center of gravity shifts toward work management.
- **Canvas-of-tables variants** — the sheet holds multiple separate tables and freeform objects rather than one uniform grid; the addressed-cell + formula model persists inside each table.
- **SMB / regional suite members** — collaborative spreadsheets sold as one application of a broader office suite, often with API access for integration.

A variant remains a variant while the shared-live grid with formulas is still the center. When rows stop being calculated cells and become scheduled, dependent work items, the product is drifting toward a Project / Work Management Application.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Spreadsheet Application | same grammar, single-user: no shared live version, no concurrent merge; the file is passed around or opened by one person at a time. Several vendors ship both modes as capability layers of one product |
| Structured Table / Lightweight Database Application | grid-like surface, but the center is typed fields, records, and linked-record relational semantics with views over records — not cell-addressed formulas with recalculation; such products often position themselves as app-building or database platforms and import spreadsheets as an on-ramp |
| Collaborative Document Editor | the identical collaboration skeleton (shared live artifact, shared access, concurrent merge, presence, comments, versions) applied to flowing text rather than an addressed, recalculating grid |
| Digital Whiteboard | shared live canvas but unbounded freeform space; no row/column addressing or formula semantics |
| Project / Work Management Application | manages work items, schedules, and dependencies as first-class objects; a grid may be one view, but cell calculation is not the core model |
| Dashboard / BI Platform | presents governed data for consumption; the collaborative spreadsheet is the editable calculation artifact itself, even when it feeds dashboards |

The boundary with the Spreadsheet Application is the sharpest: the entire difference is the shared-live collaboration layer. The boundary with the Structured Table pole is the second most important: both look like grids, but one computes with cell formulas and the other records typed, linkable records.

## Representative Products

- Microsoft Excel (Microsoft 365 / Excel for the web)
- Smartsheet
- Numbers for iCloud
- Zoho Sheet
- Google Sheets

The core model was checked against a platform-native sample (Numbers for iCloud) and a suite/SMB sample (Zoho Sheet) to avoid over-fitting the definition to one container or vendor pattern; Google Sheets is retained as a market anchor (its operational documentation was not reachable during research, and no product-specific claims about it are made here).

## Sources

Research date: **2026-09-06**

- Microsoft Support — Excel help & learning: https://support.microsoft.com/en-us/excel
- Microsoft Support — Collaborate on Excel workbooks at the same time with co-authoring: https://support.microsoft.com/en-us/excel/get-started/collaborate-on-excel-workbooks-at-the-same-time-with-co-authoring
- Smartsheet Help Center — Overview: Share sheets and reports: https://help.smartsheet.com/articles/520104-share-sheets-reports
- Smartsheet Help Center — Permission levels on sheets, reports, or workspaces: https://help.smartsheet.com/articles/2483288/sharing-permission-levels
- Smartsheet Help Center — Work with multiple people on a sheet at the same time: https://help.smartsheet.com/articles/522069-work-with-multiple-people-on-a-sheet-at-same-time
- Apple — Numbers User Guide for iCloud: https://support.apple.com/guide/numbers-icloud/welcome/icloud
- Zoho Sheet — Help resources hub: https://www.zoho.com/sheet/help/
- Airtable — platform positioning (boundary reference): https://www.airtable.com/

> Sourcing limitations: official documentation for Google Sheets was not reachable from the research environment (repeated fetch timeouts), so that product serves only as a market anchor. Zoho Sheet evidence is limited to its official help hub. Per-feature depth for Numbers for iCloud is limited to its published user-guide structure. No numeric limits, default settings, or time windows are asserted in this document; such operational detail was either unreachable or deliberately excluded. Detailed evidence and cross-product comparison are recorded in the paired Research Notes.
