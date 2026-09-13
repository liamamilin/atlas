# Research Notes — Spreadsheet Application

## Research Goal

Understand the Spreadsheet Application as an Application Type: the spreadsheet grammar itself (persistent workbook, addressed cell grid, values and formulas, automatic recalculation), the calculation model users operate through, the standard machinery mature products add around that grammar, and where the boundary sits against the already-processed sibling Collaborative Spreadsheet, the unprocessed Structured Table / Lightweight Database Application, document editors, BI/dashboards, and domain modeling tools.

This is the parent/generic leaf of §03.03 Spreadsheets & Tables. Its defining weight must sit on the spreadsheet grammar and calculation model — NOT on the collaboration layer (that is the sibling leaf's defining layer, already recorded in `research/collaborative-spreadsheet.md`).

## Initial Boundary

- Sits under 03.03 between "Collaborative Spreadsheet" (processed) and "Structured Table / Lightweight Database Application" (unprocessed).
- Working hypothesis: the type = the spreadsheet grammar (persistent workbook → addressed grid of cells → cells hold values or formulas referencing other cells → automatic recalculation of dependents) with single-author operation as the sufficient posture. Collaboration is an add-on capability layer, not part of this Type's definition.
- Nearest neighbors: Collaborative Spreadsheet (same grammar + shared-live multi-user layer), Structured Table / Lightweight DB (record/field semantics instead of addressed cells + recalculation), Collaborative Document Editor (same collaboration skeleton, text-flow grammar), Document Editor (formatted text, not a calculation grid), BI/Dashboard Platform (presents data vs editable calculation artifact), Financial Modeling / FP&A / Budgeting platforms (predefined domain models vs general machinery), Work Management (grid-as-task drift).

## Research Questions

1. What is the workbook/document model? How does work persist?
2. What is the cell grid model — addressing, selection, ranges?
3. What can a cell contain? What are the value types?
4. How do formulas work — initiation, structure (references / operators / functions / constants)?
5. How do references behave (relative/absolute, ranges, whole rows/columns, cross-sheet/cross-table, cross-workbook)?
6. How does recalculation work — dependency model, automatic vs manual, circular references?
7. What is the function library and how is it surfaced (wizards/browsers)?
8. What standard machinery surrounds the core (sort/filter, formatting, charts, pivots, validation, protection, templates, print, interchange)?
9. What is variant rather than defining (cloud storage, AI, macros, what-if tools, cell controls)?
10. Where are the boundaries vs the sibling Collaborative Spreadsheet, Structured Table / Lightweight DB, document editors, BI, and domain modeling tools?

## Representative Products

| Product | Why selected | Evidence level reached |
|---|---|---|
| Microsoft Excel (desktop/M365) | incumbent standard; deepest formula/recalculation documentation; desktop-lineage | Tier-1 deep (2 full articles: formulas overview + recalculation/iteration/precision) |
| LibreOffice Calc | open-source desktop pole; interchange-oriented philosophy; different vendor tier | Tier-1 structural (features page + full guide index; individual guide articles not fetched) |
| Apple Numbers (Mac) | platform-native, consumer tier, canvas-of-tables grammar variant | Tier-1 (full user guide TOC + welcome captions + one deep formulas article) |
| Google Sheets | cloud-native incumbent, free/mass tier | market anchor only (support timeout ×1 this pass, ×2 in sibling pass; zero operational claims) |
| Smartsheet (via sibling pass) | grid-as-work-management drift pole | Tier-1 evidence already recorded in `research/collaborative-spreadsheet.md`; reused for boundary only |
| Airtable (via sibling pass) | structured-table boundary anchor | Tier-2 positioning only; reused for boundary only |

## Sources

- Microsoft Support — Overview of formulas in Excel: https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173 (fetched 2026-09-09)
- Microsoft Support — Change formula recalculation, iteration, or precision in Excel: https://support.microsoft.com/en-us/office/change-formula-recalculation-iteration-or-precision-in-excel-73fc7dac-91cf-4d36-86e8-67124f6bcce4 (fetched 2026-09-09)
- LibreOffice Help — LibreOffice Calc Features: https://help.libreoffice.org/latest/en-US/text/scalc/main0503.html (fetched 2026-09-09)
- LibreOffice Help — Instructions for Using LibreOffice Calc (guide index): https://help.libreoffice.org/latest/en-US/text/scalc/guide/main.html (fetched 2026-09-09)
- Apple — Numbers User Guide for Mac (welcome + TOC): https://support.apple.com/guide/numbers/welcome/mac (fetched 2026-09-09)
- Apple — Calculate values using data in table cells in Numbers on Mac: https://support.apple.com/guide/numbers/calculate-values-using-data-in-table-cells-tan727173a8/mac (fetched 2026-09-09)
- Sibling-pass sources reused for boundaries only: Excel help hub + co-authoring article, Smartsheet help center (3 articles), Numbers for iCloud guide TOC, Zoho Sheet help hub, Airtable homepage (see `research/collaborative-spreadsheet.md`)

### Source-access limitations

- Google Sheets: no operational documentation reachable in this pass or the sibling pass. No Google-specific operational claim appears anywhere. Used only as a market anchor.
- VisiCalc historical site: www.bricklin.com/visicalc.htm transport error; www.visicalc.com now hosts an unrelated 2024 product ("VisiCalc — Spreadsheets for people who hate spreadsheets" by Wecora LLC). The historical anchor could not be fetched; the era check is done conceptually (see Historical Check) and no precise historical claims are asserted from memory.
- LibreOffice: features page and guide index captured; individual guide article bodies (e.g. "Addresses and References, Absolute and Relative") not fetched — LibreOffice behaviors asserted at index-title level only.
- Numbers: formulas article deep; the rest of the guide at TOC/caption level.
- No numeric product limits are asserted in the final document except figures directly stated in fetched articles, which are kept in these notes (L3) rather than the final document.

## Product A — Microsoft Excel

### Key observations (evidence A — formulas overview article)

- Definition sentence: "Learn how to create formulas and use built-in functions to perform calculations and solve problems."
- Formula entry flow: select a cell → type the equal sign ("Formulas in Excel always begin with the equal sign") → select a cell or type its address → enter an operator → next cell → Enter: "The result of the calculation appears in the cell with the formula."
- **Formula Bar**: "When you enter a formula into a cell, it also appears in the Formula Bar." Selecting a cell shows its formula there — the cell shows the result, the bar exposes the formula.
- Formula parts: **functions** (PI() example), **references** ("A2 returns the value in cell A2"), **constants** (values entered directly, "10/9/2008", "Quarterly Earnings"), **operators** (^, *).
- Constants guidance: "If you use constants in a formula instead of references to cells… the result changes only if you modify the formula. In general, it's best to place constants in individual cells… and then reference those cells in formulas." — the cells-as-inputs modeling pattern taught by the vendor itself.
- References: "A reference identifies a cell or a range of cells on a worksheet, and tells Excel where to look for the values or data you want to use in a formula." References can reach other sheets in the same workbook and **other workbooks** ("external references" / links).
- **A1 style**: columns by letter (A through XFD — 16,384 columns), rows by number (1 through 1,048,576); ranges A10:A20, B15:E15; whole row 5:5; whole column H:H.
- Sheet reference: worksheet name + "!" + range, e.g. AVERAGE(Marketing!B1:B10).
- **Relative / absolute / mixed references**: relative (A1) adjusts when copied/filled; absolute ($A$1) stays; mixed ($A1 / A$1) partially. "By default, new formulas use relative references."
- **3-D references**: =SUM(Sheet2:Sheet13!B5) across a range of worksheets; whitelist of functions that accept 3-D refs; behavior on insert/delete/move of sheets defined.
- **R1C1 style**: rows and columns both numbered; "useful for computing row and column positions in macros"; toggleable option.
- See-also set: operator precedence, nested functions, array formulas, define/use names, delete formulas, avoid broken formulas, find/correct errors, functions by category, keyboard shortcuts.

### Key observations (evidence A — recalculation article)

- **Definition of calculation**: "Calculation is the process of computing formulas and then displaying the results as values in the cells that contain the formulas."
- **Dependency-driven recalculation**: "Microsoft Excel automatically recalculates formulas only when the cells that the formula depends on have changed. This is the default behavior when you first open a workbook and when you are editing a workbook."
- **Calculation modes**: Automatic (default) / Partial (except data tables) / Manual ("update formulas only when you manually recalculate, for example, by pressing F9"); desktop option applies to all open workbooks; web version per-workbook. Manual shortcuts: F9, Shift+F9 (active sheet), Ctrl+Alt+F9 (full rebuild), Ctrl+Shift+Alt+F9 (rebuild + dependency check).
- **Iteration / circular references**: "By default, Excel cannot calculate a formula that refers to its own cell—either directly or indirectly." Enabling iterative calculation allows it, with max-iterations and max-change controls. "Circular references can iterate indefinitely."
- **Precision**: "Excel stores and calculates with 15 significant digits"; stored vs displayed values (a date displays as 6/22/2008 but stores a serial number); "Set precision as displayed" permanently changes stored values (irreversible); numeric ceiling ~9.99E+307.
- **Multi-threaded calculation**: optional, processor-count controls.
- **Backward compatibility**: opening a workbook created in an earlier Excel version triggers full recalculation of all formulas (current-version workbooks: only changed-dependency recalculation). Evidence of the file-lineage continuity of the Type.
- **What-if tools**: Solver and Goal Seek named as "what-if analysis tools" that use iteration in a controlled way.

Interpretation: Excel documents the full L0 chain — addressed grid (A1/R1C1), formulas built from references/operators/functions/constants, results displayed in the formula's cell, dependency-driven automatic recalculation with manual override, persistence as workbooks (with format/version lineage). The 15-digit precision, XFD/1,048,576 bounds, R1C1, and shortcut keys are vendor specifics.

## Product B — LibreOffice Calc

### Key observations (evidence A — features page)

- Self-definition: "LibreOffice Calc is a spreadsheet application that you can use to calculate, analyze, and manage your data. You can also import and modify Microsoft Excel spreadsheets."
- **Calculations**: "functions, including statistical and banking functions, that you can use to create formulas to perform complex calculations"; **Function Wizard** assists formula creation.
- **What-If Calculations**: "immediately view the results of changes made to one factor of calculations that are composed of several factors" (loan example — changing the time period changes interest/repayment figures); "manage larger tables by using different predefined scenarios." — the recalculation loop marketed as the Type's signature capability.
- **Database functions**: "Use spreadsheets to arrange, store, and filter your data"; drag-and-drop tables from databases; spreadsheet as data source for form letters in Writer.
- **Arranging Data**: show/hide ranges, format ranges by conditions, quick subtotals/totals.
- **Dynamic Charts**: "present spreadsheet data in dynamic charts that update automatically when the data changes."
- **Interchange**: filters to convert Excel files; open/save a variety of formats.

### Key observations (evidence A — guide index structure; titles only)

- **Entering Values and Formulas**: Entering Values; Calculating With Formulas; Displaying Formulas or Values (toggle between showing formulas and showing results); Entering Formulas; Copying Formulas; Calculating in Spreadsheets; date/time calculations; matrix formulas.
- **Entering References**: Naming Cells; Recognizing Names as Addressing; Referencing Cells by Drag-and-Drop; Addresses and References, Absolute and Relative; Referencing a Cell in Another Sheet; Inserting External Data in Table (WebQuery).
- **Database Ranges**: define / filter / sort a range as a database-like block.
- **Advanced Calculations**: Pivot Table (create/edit/filter/update/delete/select output); Consolidating Data; Goal Seek; Multiple Operations; Validity of Cell Contents; Using Scenarios.
- **Formatting/printing**: conditional formatting, merge/unmerge, number formats incl. user-defined, freeze rows/columns as headers, print ranges, repeat rows/columns on every page.
- **Import/Export**: CSV (incl. with formulas), dBASE, HTML, opening/saving other formats, email.
- **Miscellaneous**: Protecting Cells from Changes / Unprotecting; comments; Recording a Macro; multiple sheets + navigating sheet tabs; autofill based on adjacent cells; sort lists; transposing.

Interpretation: an independent (open-source, different vendor tier) realization of the same grammar: value/formula cells, references (relative/absolute/named/cross-sheet), recalculation-driven what-if as a headline capability, function library + wizard, pivot/goal-seek/consolidate/scenarios as the analysis layer, interchange breadth as a philosophy (Excel/dBASE/HTML/CSV), cell protection, macros. The "What-If" feature page is the clearest vendor articulation of the recalculation loop as the product's essence.

## Product C — Apple Numbers (Mac)

### Key observations (evidence A — welcome + TOC captions)

- Templates: "All spreadsheets begin with a template—a model you can use as a starting point. Replace the template's charts and data with your own content, and add new tables, formulas, and more."
- Data + formulas: "Enter your own data or import data from another file. You can also add a wide range of formulas, like sum or average, to any cell. To organize your data and identify trends, you can add filters, group data into categories, create pivot tables, and more."
- **Charts bound to cells**: "When you make changes to the data in the table, the chart updates automatically." — recalculation semantics extended to chart objects.
- **Sheets**: "Organize your spreadsheet with different sheets for each type of information you want to track—income, expenses, and so on. Then just click a tab at the top of the spreadsheet to switch."
- **Canvas-of-tables grammar**: sheets hold multiple tables plus freely positioned objects (images, shapes, media, text boxes; layer/group/lock objects; rulers/alignment guides; sheet background). Different in-sheet grammar from the single uniform grid — same spreadsheet concept.
- Table machinery: add/delete tables, select cells/rows/columns, add/remove/move/resize rows & columns, merge/unmerge, table styles, autofill, cell controls (checkboxes etc.), custom cell formats, format dates/currency, wrap text, snapshots of tables.
- Organize/analyze: filter, sort, **categories** (group + summarize group data), **pivot tables** (create/arrange/sort/refresh/view source data for a value), charts (2D/3D/interactive).
- File management: save, open/close, find, delete, **restore earlier versions**, lock, **password-protect**, reduce file size, **save large spreadsheets as package files**, iCloud, **import an Excel or text file / export to Excel or another file format**, AirDrop/Handoff transfer, print.
- Collaboration chapter (real-time invite, edit-vs-view) — the sibling Type's layer, present here as one chapter of this product.
- Writing/editing tools: spell-check, find/replace, comments, author name/color.
- Era-current: Apple Creator Studio subscription, Magic Fill (AI fill), generated images.

### Key observations (evidence A — "Calculate values using data in table cells" article)

- Core sentence: "You can create formula or function cells that automatically perform calculations using the data in any cells you select… The result of a formula or function appears in the cell where you entered it."
- **Function library**: "more than 250 functions for applications including statistics, engineering, and finance, some of which retrieve information remotely via the internet." Detailed per-function help in Formulas and Functions Help + a **Functions Browser** that appears when typing "=".
- **Formula Editor**: opens on "=" in a cell; draggable/resizable floating editor; formula tokens; commit/cancel; Smart Cell View shows "the formula result, cell reference values, errors, and warnings."
- **Insert formula**: click result cell → "=" → click cells or type values → arithmetic operators (+ - * /; Numbers inserts "+" between references by default) → Return. Quick-calc path: select a range, toolbar Insert → sum/average/product, "Numbers automatically inserts the formula and chooses a result cell."
- **Insert function**: Functions Browser search/browse → function with required/optional arguments as tokens → fill arguments by clicking cells, dragging ranges, or clicking row/column bars; can convert formula to text permanently.
- **Comparison operators**: >, >=, =, <>, <, <= producing "true" or "false".
- **References**: "you can include references to cells, ranges of cells, and whole columns or rows of data—including cells in other tables and on other sheets." Examples: COUNT(A3:D7); cross-table Table 2::B2 (:: separator); cross-sheet SUM(Sheet 2::Table 1::C2:G2); whole column SUM(C); whole row SUM(1:1); **header names** SUM(Revenue), SUM("Number of Guests").
- **Preserve row/column** (absolute references): toggle per-range via token triangles or Command-K; otherwise "if you move the formula… the references are adjusted relative to the formula's new location."
- **Editing**: double-click result cell → Formula Editor; change/remove/add references.
- **Errors**: syntax error icon appears in the result cell; click for the message; click the referenced cell causing the error.
- Categories caveat: with categories, adding a row inside a referenced range is **not** auto-included unless the reference is changed — an edge behavior of reference semantics.

Interpretation: Numbers proves the Type's grammar outside the desktop-file heritage: same formula-in-cell model (= initiation, references, operators, functions, result-in-cell, auto-calculation), same reference semantics (relative/absolute, ranges, whole rows/columns, cross-container), same analysis extensions (charts bound to data, pivots, categories) — wrapped in a canvas-of-tables sheet grammar and a consumer/template-first posture. Its collaboration chapter is the sibling layer, separable from this Type's core.

## Product D — Google Sheets (market anchor only)

All support fetches timed out (this pass ×1; sibling pass ×2 — abandoned per retry discipline). No operational claims recorded. Retained solely as the universally recognized cloud-native spreadsheet anchoring the market position; every claim in the documents is supported by the other sampled products.

## Product E — Smartsheet (boundary/drift pole; evidence via sibling pass)

Sibling-pass Tier-1 evidence (help center): rows explicitly "individual items or tasks"; permission ladder; dependencies/critical path/baselines; forms feeding rows; Gantt/board/calendar/timeline views. Formula layer present (functions list, cross-sheet formulas). Reused here only to mark the drift boundary: when rows become managed work items and the grid becomes the surface for a work-management object model, the product has left this Type (documented in Boundary Findings).

## Product F — Airtable (boundary anchor; evidence via sibling pass)

Positioning: "system of record for your workflows, data, and agents"; bases/records/databases/interfaces/agents; "drop in a spreadsheet you already have" as the import on-ramp. The spreadsheet-looking surface sits on a record/field data model — the Structured Table pole. "Drop in a spreadsheet" documents adjacency, not identity.

## Cross-product Comparison

| Dimension | Excel | LibreOffice Calc | Numbers (Mac) | Google Sheets (anchor) |
|---|---|---|---|---|
| Persistent document | workbook files; earlier-version files re-open and recalculate; AutoSave-on-cloud per sibling pass | documents; opens/saves Excel + dBASE + HTML + CSV | spreadsheet documents; save/package/password-protect/restore versions; iCloud | market-known cloud document |
| Grid grammar | sheets → row/column-addressed cells (A1 default; R1C1 optional) | sheets/tabs → cell grid; multiple sheets | sheets → multiple tables + freeform objects (canvas-of-tables) | market-known |
| Cell content | values or formulas; constants discouraged in favor of cell references | values or formulas (entering values; formulas; matrix formulas) | values or formulas "in any cell" | market-known |
| Formula initiation | "=" always begins a formula | formula entry; display formulas-or-values toggle | "=" opens Formula Editor | market-known |
| Formula anatomy | functions + references + operators + constants | functions + wizard | functions + references + operators (arithmetic + comparison true/false) | market-known |
| References | relative/absolute/mixed; ranges; whole rows/columns; cross-sheet (Sheet!range); cross-workbook links; 3-D ranges; names | relative/absolute; names; drag-and-drop; cross-sheet; WebQuery external data | relative/absolute (Preserve Row/Column); ranges; whole rows/columns; header names; cross-table (::); cross-sheet (Sheet::Table::cell) | market-known |
| Recalculation | dependency-driven, automatic by default; manual/partial modes; F9 family; multi-threaded; older files full-recalc on open | what-if framing: "immediately view the results of changes"; calculate commands | "automatically perform calculations using the data in any cells you select"; charts "update automatically" | market-known |
| Circular references | rejected by default; iterative calculation opt-in with limits | (iteration settings not directly evidenced at fetched level) | (not evidenced) | not researched |
| Function library | alphabetical + by-category lists; XLOOKUP/VLOOKUP/SUM/COUNT/AVERAGE/IF named | functions incl. statistical/banking; Function Wizard | "more than 250 functions" statistics/engineering/finance; Functions Browser | market-known |
| Formula surface | Formula Bar | formula entry + display toggle | Formula Editor + Functions Browser + Smart Cell View | market-known |
| Errors | broken-formula/error-correction articles named | (guide titles imply) | error icon in result cell; click-through to message and cause cell | market-known |
| Multi-sheet | 3-D references across sheet ranges | multiple sheets + tab navigation + copy to multiple sheets | sheets as tabs organizing tables | market-known |
| Sort/filter | sort/filter machinery (import & analyze category per sibling pass) | autofilter/advanced filters/database ranges/sort | filter, sort, categories | market-known |
| Charts | charts/PivotCharts/sparklines (sibling-pass hub) | "dynamic charts… update automatically" | 2D/3D/interactive; auto-update from table data | market-known |
| Pivot summarization | PivotTables/PivotCharts | Pivot Table guide set | pivot tables incl. source-data inspection | market-known |
| What-if tools | Goal Seek, Solver, data tables | Goal Seek, Multiple Operations, Scenarios, Consolidate | none evidenced at TOC level | not researched |
| Validation | drop-downs/data validation (hub) | Validity of Cell Contents | cell controls (checkboxes, pop-ups), custom formats | market-known |
| Formatting | formats category (hub) | number formats, conditional formatting, autoformat, freeze | table/cell/text/chart/object styling; custom formats | market-known |
| Comments | (not in fetched pages; sibling-pass hub implied) | inserting and editing comments | add/print comments; author color | market-known |
| Protection | protect worksheet/workbook (sibling pass) | protecting/unprotecting cells | lock spreadsheet; password-protect | market-known |
| Interchange | xlsx family; csv/txt import-export; import from web | Excel/dBASE/HTML/CSV (with formulas) | import Excel/text; export Excel/other | market-known |
| Print | print machinery (sibling pass) | print ranges/details/title rows/landscape | print a spreadsheet | market-known |
| Templates | templates workbook download | (not evidenced at fetched level) | template chooser; custom templates | market-known |
| Programming | quick-start macro; R1C1 for macros | Recording a Macro; user-defined functions | none (Applescript outside fetched docs) | market-known |
| AI | Copilot analyze/enter formulas (hub) | (none at fetched level) | Magic Fill; Creator Studio | market-known |
| Collaboration | co-authoring layer (sibling pass) | (not the fetched emphasis) | collaboration chapter | market-known |

## Canonical Model

### L0 — Defining Invariant

```text
Persistent spreadsheet document (workbook) — the unit of work that survives the session
└── Addressed cell grid — content organized in rows × columns, every cell
    individually addressable; the application imposes no record or field
    semantics on the grid (what the model means is the user's construction)
    └── Cell content: a literal value OR a formula that computes
        from references to other cells
    └── Automatic recalculation — when referenced cells change,
        dependent formulas recompute and results update in place
```

Four properties, jointly held:

- **1 alone** (persistent document, no grid) → document editor / ledger document.
- **2 without 3+4** (grid of values, no formulas/recalculation) → a table of data — Structured Table / simple table-editor territory.
- **3 without 4** (formulas that do not auto-recompute) → a document with embedded computed numbers, not a spreadsheet; the defining behavior is recalculation-on-change.
- **4 without 2+3** → a calculator.
- **2+3+4 without 1** → a transient calculation scratchpad, not the accumulated modeling artifact.

Nothing about function-library breadth, multi-sheet organization, charts, pivot tables, collaboration, cloud storage, AI, or any specific reference notation (A1/R1C1/header names) is required by the definition — the founding generation of spreadsheets had none of those beyond the bare chain and are still unambiguously spreadsheets (see Historical Check).

### L1 — Common Mature Structure

Present in essentially all mature products; makes the Type practical but does not define it:

- **Function library** with per-function documentation and discovery surfaces (Excel by-category lists + wizard-level articles; LibreOffice functions incl. statistical/banking + Function Wizard; Numbers 250+ + Functions Browser; Zoho 350+ per sibling pass).
- **Formula authoring surface** distinct from the grid display: formula bar (Excel), Formula Editor + Functions Browser (Numbers), formula entry + formulas-vs-values display (LibreOffice).
- **Reference system**: relative/absolute/mixed; ranges; whole rows/columns; cross-sheet references; names (Excel names/3-D; LibreOffice naming cells; Numbers header names + :: scoping).
- **Multi-sheet organization** (workbook → sheets/tabs) — Excel 3-D refs, LibreOffice tab navigation, Numbers sheet tabs.
- **Sort/filter** over cell ranges (incl. LibreOffice database ranges/autofilter; Numbers filter + categories).
- **Formatting**: number/date/currency formats, conditional formatting, merge cells, freeze panes, styling.
- **Charts bound to cell data** that update when data changes (all three deep samples).
- **Pivot summarization** (Excel PivotTables; LibreOffice Pivot Table; Numbers pivot tables).
- **Data validation / cell controls** (Excel drop-downs; LibreOffice validity; Numbers checkboxes/pop-ups).
- **Comments/notes anchored to cells** (LibreOffice; Numbers; Excel sibling-pass hub).
- **Protection of cells/sheets** (Excel protect worksheet; LibreOffice protect cells; Numbers lock/password).
- **Templates** (Numbers chooser; Excel template downloads).
- **Print machinery** (ranges, repeating title rows, scaling — Excel sibling pass; LibreOffice guide set; Numbers print).
- **Interchange**: CSV/Excel-format import-export as the lingua franca (all three), plus HTML/dBASE (LibreOffice).
- **Undo/redo, find/replace, copy/fill of formulas** (fill-down adjusting relative references — Excel relative-reference docs; Numbers change-formula article; LibreOffice copying formulas + autofill).
- **Version history / restore** where the storage substrate supports it (Numbers restore earlier versions; Excel Version History per sibling pass).

### L2 — Variant / Optional Structure

- **Storage substrate**: local files (desktop-classic), cloud-synced documents, platform package files (Numbers package option). Era/segment choice.
- **Recalculation posture**: automatic (universal default) vs manual/partial modes (Excel; web variant per-workbook) — user-configurable performance/behavior choice.
- **What-if tooling depth**: Goal Seek / Solver / scenarios / multiple operations / consolidate (Excel + LibreOffice have them; Numbers shows none at TOC level) → optional analysis layer, not defining.
- **Cross-workbook links** (Excel external references) — advanced; absent from Numbers TOC evidence.
- **Programming extension layer**: macros (Excel quick-start; LibreOffice macro recording), user-defined functions (LibreOffice), scripting — optional.
- **External data ingestion**: web queries (LibreOffice WebQuery; Excel import-from-web), remote-retrieving functions and stock data cells (Numbers; Excel data types per sibling hub) — optional.
- **In-sheet grammar**: uniform single grid (Excel/LibreOffice-class) vs canvas-of-tables (Numbers) — variant, not boundary.
- **AI assistance** (Copilot, Magic Fill, Smartsheet AI) — era-current, optional.
- **Collaboration layer** (co-authoring, shared live workbook) — the sibling Type's defining layer; available as an add-on capability in several products spanning both Types.
- **Suite membership vs standalone**; desktop/web/mobile surface mix; consumer vs professional depth poles.

### L3 — Vendor-specific Structure (Research Notes only)

- Excel: A–XFD (16,384 columns) × 1–1,048,576 rows; 15-significant-digit stored precision; ~9.99E+307 numeric ceiling; stored-vs-displayed values incl. dates as serial numbers; "Set precision as displayed" irreversibility; R1C1 style tied to macro recording; 3-D reference function whitelist; F9/Shift+F9/Ctrl+Alt+F9/Ctrl+Shift+Alt+F9 recalculation shortcuts; "Recalculate workbook before saving" coupling; multi-threaded calculation up to 1024 threads; older-version workbooks fully recalculated on first open; x86 vs ARM calculation-difference notice; Formula Bar as the formula-exposure surface; XLOOKUP/VLOOKUP/IF/SUM/COUNT/AVERAGE named examples; AutoSum; Solver/Goal Seek named "what-if analysis tools"; Copilot entry points.
- Numbers: floating Formula Editor; Functions Browser on "="; token-based arguments; :: scoping (Table 2::B2; Sheet 2::Table 1::C2:G2); header-name references (SUM(Revenue)); "Preserve Row/Column" absolute mechanism + Command-K; Smart Cell View; syntax-error icon with clickable cause cell; "more than 250 functions"; quick-calc toolbar insert; categories reference caveat (new rows not auto-included); package files for large spreadsheets; snapshots; Magic Fill; Creator Studio subscription framing.
- LibreOffice: Function Wizard; What-If as a headline features page; database ranges; Pivot Table guide family (datapilot heritage); Goal Seek; Multiple Operations; Scenarios; Consolidate; Validity; WebQuery; CSV-with-formulas import/export; dBASE/HTML; sort lists; matrix formulas; user-defined functions; cell protection guide pair.
- Zoho Sheet (sibling pass): "more than 350 functions" self-published count; REST API.
- Naming-drift curiosity: visicalc.com today hosts an unrelated 2024 visual-planning product; the historical product's web presence is gone from its canonical domain.

## Vendor-specific Findings

- Excel's A1 bounds, 15-digit precision, R1C1, and shortcut/option machinery are vendor specifics — kept out of the final document.
- Numbers' header-name references and :: cross-container scoping are product syntax; the canonical concept is "references to cells anywhere in the document."
- Numbers lacks (per TOC evidence) the Goal-Seek/Solver-class what-if tools both Excel and LibreOffice document — what-if tooling is optional, not core.
- The 250+ / 350+ function counts are self-published figures; no cross-product function-count comparison is asserted.
- Circular-reference default rejection + opt-in iteration is evidenced directly for Excel only; held product-documented, qualified wording elsewhere.

## Rejected Findings (considered for the core, rejected)

- **Specific address notation (A1)** — R1C1 (Excel) and header-name references (Numbers) exist; the invariant is "individually addressable," not a notation.
- **Function library** — founding-generation spreadsheets had minimal function sets; breadth is market maturity, not definition.
- **Charts / pivot tables / conditional formatting / validation** — absent from the founding generation; all are mature additions.
- **Multi-sheet workbooks** — the earliest spreadsheets were single-sheet; multi-sheet is L1.
- **Absolute vs relative references** — refinement of the reference system (founding-generation relative refs suffice for the grammar).
- **Collaboration / shared live editing** — the sibling leaf's defining layer; single-author operation satisfies this Type (historical check).
- **Cloud storage / sync / AI / templates / print** — implementation and era machinery.
- **What-if tooling (Goal Seek/Solver/scenarios)** — optional analysis layer (absent in one deep sample).
- **Cross-workbook links** — advanced variant (one deep sample).

## Historical / Market-Sample Check

Check applied: would older, regional, platform-native, or differently positioned products still fit the L0?

- **Era**: the founding generation of spreadsheet products (late-1970s/1980s personal-computer era) is described consistently — including by the sampled vendors' own backward-compatibility behavior (Excel fully recalculates workbooks "created in an earlier version of Excel" on open; LibreOffice's headline interoperability with Excel files; Numbers importing Excel files) — as single-sheet, single-user documents of addressed cells holding values and formulas that recalculate. That is exactly the L0 chain: no charts, no pivots, no collaboration, no cloud required. ✓ (fetched historical sources unavailable — see Source-access limitations; this check is conceptual, supported by the vendors' own documented file-lineage behavior.)
- **Platform-native**: Numbers fits fully with a different in-sheet grammar (canvas-of-tables). ✓
- **Regional / alternative vendor tier**: LibreOffice Calc fits (independent open-source lineage, interchange-first philosophy). Zoho Sheet fits at hub-scope level (sibling pass). ✓
- **Differently positioned grid products**: the Airtable pole fails the formula-recalculation-center test → Structured Table territory. ✓
- **Differently positioned products repurposing the name**: the modern visicalc.com product ("spreadsheets for people who hate spreadsheets… without ever having to hit + - or =") markets itself around avoiding formula entry — evidence that formula+recalculation remains the folk definition of the Type ("spreadsheets" being defined by what it removes), not a counterexample to the invariant. Recorded as an observation only.

## Boundary Findings

- **vs Collaborative Spreadsheet (sharpest seam; sibling processed)** — the sibling's defining layer is the shared-live multi-user capability (one live current version, shared access, concurrent merge) on top of the same grammar. Remove that layer → this Type. Add it → the sibling. Capability-based split, not product-based: Excel, Numbers, Google Sheets all span both. The sibling pass flagged the split for joint review; this pass **confirms keep-both** with the seam on the collaboration layer, the spreadsheet grammar belonging to this (parent) leaf.
- **vs Structured Table / Lightweight Database Application** — the spreadsheet's center is the addressed cell + formula + recalculation over a semantically empty grid; the structured-table pole's center is typed fields, records with app-imposed semantics, and relational record links with views (Airtable: databases/interfaces/agents; "drop in a spreadsheet" as the import on-ramp). Remove the addressed-formula-recalculation model, add typed-record semantics → different Type.
- **vs Collaborative Document Editor** — same collaboration skeleton (sibling-pass finding), different artifact grammar: flowing text vs addressed calculated cells.
- **vs Document Editor** — a word-processor document may embed computed fields, but its center is authored flowing text, not a grid of recalculating cells.
- **vs Business Intelligence Platform / Dashboard Platform** — BI presents governed data for consumption; the spreadsheet is the editable calculation artifact where the model itself is built (consistent with the sibling's boundary recording).
- **vs Financial Modeling Application / Budgeting & Forecasting Platform / FP&A platforms** — those Types carry predefined domain models (accounts, periods, plan versions) as objects; the spreadsheet supplies general machinery with no predefined semantics, and is precisely the tool those products replace or complement (FP&A vendors' Excel-native/add-in postures, per the processed financial-planning-analysis leaf). Remove the predefined domain model → spreadsheet machinery.
- **vs Database management / SQL clients** — records defined by schema and queried via a query language vs the user's free-form grid model built cell by cell.
- **vs Work Management Platform** — the drift path (Smartsheet): when rows become scheduled, dependent work items and the grid becomes the surface, the product has moved toward Work Management; if rows remain cells in a calculation grid, it stays a spreadsheet.
- **vs Calculator-class utilities** — a calculator computes ad-hoc expressions; it holds no addressed grid, no formula layer, no persistent document.

## Uncertainties

- Google Sheets: zero fetched evidence (both passes). Any Google-specific operational behavior is intentionally absent from both documents.
- LibreOffice: individual guide-article bodies not fetched; LibreOffice-specific behaviors asserted only at features-page/index-title level.
- Numbers: what-if tooling absence judged from TOC absence — absence-of-evidence, not evidence-of-absence; held as "none evidenced," not "lacks."
- Circular-reference behavior and manual-recalculation postures evidenced directly for Excel only; qualified wording used elsewhere.
- Historical specifics (exact founding-era capabilities/dates) not asserted — historical anchor sources unreachable; the era check is conceptual plus vendor-documented file-lineage behavior.
- No numeric limits (grid dimensions, precision, thread counts, function counts) asserted in the final document; they live here as L3.

## Final Synthesis

The Spreadsheet Application is the general-purpose modeling tool whose world is the persistent spreadsheet document: an addressed grid of cells — semantically empty, the model's meaning built entirely by the user — where each cell holds either a value or a formula referencing other cells, and the application's defining behavior is automatic recalculation of dependent cells whenever referenced values change. Around that chain mature products add the standard machinery (function libraries with discovery surfaces, formula bars/editors, multi-sheet workbooks, relative/absolute reference systems, sort/filter, formatting, charts bound to data, pivot summarization, validation, protection, templates, print, interchange), while storage substrate, what-if tooling, programming extensions, external data, AI, the in-sheet grammar (uniform grid vs canvas-of-tables), and the collaboration layer are variant or optional. The collaboration layer itself is the sibling Type's defining property; the grid-without-recalculation record model is the Structured Table pole; predefined domain models make it a domain tool. Everything else is the spreadsheet.
