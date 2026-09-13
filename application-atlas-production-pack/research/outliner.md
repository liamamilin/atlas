# Research Notes — Outliner

## Research Goal

Understand the Outliner as an Application Type: what the unit of work is (item/bullet/row/block), what the hierarchy means, which structure operations define the category (collapse/expand, move/re-parent subtrees), what mature products add (zoom/focus, task attributes, backlinks, collaboration, export), and where the boundary lies against neighboring Types (note-taking, PKM, to-do/task apps, markdown/document editors, wikis).

## Initial Boundary

Placed under §03.02 Notes & Personal Knowledge, sibling of Note-taking Application, Personal Knowledge Management Application, Visual Note-taking Application.

Working hypothesis before research:

- Core use: capture and organize thinking as a nested tree of short items; structure manipulation (indent, fold, drag) IS the workflow.
- Users: individual thinkers, writers, students, engineers; some products serve teams.
- Nearest neighbors: note-taking (document-centric), to-do/task apps (task-centric), PKM (link-network-centric), document editors with outline views.
- Likely confusion: "outliner" products increasingly bundle tasks (checkboxes, due dates) and links/backlinks — must separate defining structure from common additions.

## Research Questions

1. What is the atomic unit of content (item/bullet/row/block) and what can it hold?
2. How is hierarchy created and manipulated? What operations act on subtrees?
3. What are the canonical navigation surfaces (zoom/focus/hoist, folding, breadcrumbs)?
4. Do items carry task semantics (status, due, assignee)? Are they definitional or optional?
5. How do notes/comments relate to items (child item vs. attached note)?
6. What container model holds outlines (one infinite document, multiple lists, document files, graph of pages)?
7. What link/reference machinery exists (internal links, backlinks, mirrors/block refs)?
8. What sharing/collaboration and export/interop exist (OPML, Markdown, Org-mode)?
9. Where is the boundary vs. note-taking, task apps, markdown editors, PKM?
10. Historical check: do older desktop outliners and text-mode outlines (Org-mode-style) satisfy the definition?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, different customer tiers:

| Product | Philosophy | Segment |
|---|---|---|
| Workflowy | minimal, cloud, one infinite document, zoom-centric | individual → teams (freemium) |
| OmniOutliner | traditional paid desktop application, document-based, pro features (columns/styles) | individual professionals (paid) |
| Checkvist | keyboard-first collaborative outliner + task manager, list-based | individuals and small teams (freemium) |
| Logseq | local-first, open-source, Markdown/Org-mode files, knowledge management | individual PKM users |
| Roam Research | web, "networked thought" note-taking | researchers/writers (paid) |

Rejected candidates: Dynalist (same vendor lineage as Workflowy — would duplicate philosophy); Notion (workspace suite that embeds outline-like blocks; would pollute the Type boundary).

## Sources

Research date: 2026-09-08

Fetched (evidence layer A unless noted):

- Workflowy homepage — https://workflowy.com/ (positioning, single-list claim, node metering)
- Workflowy Help Center "Get started" — https://workflowy.com/help/ (core model: infinite document, Enter/Tab, Zoom, Search; node types; help-center section map)
- Workflowy blog — https://blog.workflowy.com/ (product-update list: Panes, node→Table, Calendar, Email-to; replaces notebooks/stickies positioning)
- OmniOutliner product page — https://www.omnigroup.com/omnioutliner (hierarchy, expand/collapse, checkboxes, drag-to-nest, row notes, focus/filters, columns, styles, automation, Essentials/Pro split)
- Checkvist homepage — https://checkvist.com/ (keyboard-first outliner positioning, endless hierarchy, sharing, use cases)
- Checkvist help/reference — https://checkvist.com/help/ (very detailed operational documentation: items, indent/move, hoist, statuses, tags, due dates, sharing permissions, backlinks, OPML, email-in)
- Logseq homepage — https://logseq.com/ (title only: "A privacy-first, open-source knowledge base")
- Logseq GitHub README — https://github.com/logseq/logseq (positioning, Markdown/Org-mode, graphs, plugins, inspiration lineage incl. Workflowy/Roam/Org-mode)
- Roam Research homepage — https://roamresearch.com/ (title only: "A note taking tool for networked thought")

Source-access limitations:

- Logseq: docs.logseq.com fetch exceeded size limits (2 attempts); GitHub repo fetch timed out once; raw README succeeded. The README does not describe outline-level editing operations in detail. Logseq observations below are restricted to what the README/homepage states; operational outline behavior is NOT asserted from memory.
- Roam Research: app is JS-rendered; help lives inside the app and was not reachable; /faq returned 404 (2 attempts). Only the homepage title is used. No operational claims drawn from Roam beyond positioning.
- Historical outliners (1980s desktop products, Word outline view, Org-mode) were NOT fetched; used only in the historical check as reasoning anchors with weakened claims, no precise specifications asserted.

## Product A — Workflowy

### Key observations

Positioning (homepage): "A simpler way to organize your work"; "Stop organizing your notes. Start organizing your thoughts."; "No docs. No folders. No distractions."; "A single bullet list does it all — indent bullets to create order"; homepage demo labels the same bullet as Note / Folder / Todo / Doc. Free tier metered at "100 nodes per month" — the node is the billing unit. Serves individuals; Teams for collaboration; "helping people organize their thinking … for over 14 years".

Core model (Help Center, "Get started"): [A]

- "Workflowy is a single, infinite document. No folders, no separate files. Just one list that can hold everything."
- Four ideas that make it click:
  1. Write anything, anywhere — notes, tasks, ideas, plans in the same place; Enter adds a new item.
  2. Nest to organize — Tab indents an item, making it a child of the one above; "Go as deep as you like. A note can grow into a project; a project can have sub-projects. Structure emerges naturally."
  3. Zoom in to focus — "Click any bullet and it becomes your whole world. Everything outside it disappears. Click the breadcrumb at the top to zoom back out."
  4. Search to find anything — typing filters the document in real time; edit directly in results; click a tag to filter; star a search to save it as a sidebar shortcut.
- Saves automatically, syncs across devices, "no save button".

Extended structure (Help Center map + blog): node types (bullet, todo, heading, paragraph, numbered list, quote block, code block, divider, boards, tables); tags/mentions, date tags; links and backlinks; mirrors; templates; share & collaborate; exporting; instant presentations; fractal comments; Calendar (Today Digest, Timeline) with Google Calendar sync; quick capture (Quick Add, Mobile Share To, Email to Workflowy); keyboard shortcuts, slash command, command palette; panes (multiple parts of the outline side by side, 2026.08); "turn any node into a lightweight Table" (2026.06). Blog tagline: "Workflowy replaces your notebooks, stickies and bloated apps with a simple, smooth digital notebook."

Reading: the product's entire surface is phrased as operations on bullets/nodes; every added capability (table, board, calendar, panes) hangs off the node. Zoom (with breadcrumbs) is the signature navigation operation.

## Product B — OmniOutliner

### Key observations

Positioning: "Outlining Software For Pros"; "Your thoughts, in order. OmniOutliner is a powerful tool for organizing (and reorganizing) information, so you can see the full picture and structure your information effortlessly." Users: writers, students, attorneys, software developers; screenplays, books, speeches, dissertations, essays, class notes, meeting agendas, project plans, budgets.

Core structure (product page): [A]

- "support for unlimited levels of outline hierarchy. Expand and collapse sections to see the full picture or focus on the smallest of details."
- "Row status checkboxes turn any outline into a checklist."
- "Drag and drop to order, re-order, and nest the rows in your outline."
- "Each outline row can also be accompanied by a note … an extra space for as little or as much information you need."
- Attachments; themes.

Pro tier adds: "Focus on specific sections of your outline or apply a saved filter in the document sidebar"; "documents with multiple columns that contain different types of information — pop-up lists, checkboxes, numerical values, dates, durations, or just text"; named styles, row numbering; Omni Automation plug-ins.

Form: document-based (document sidebar; document = outline). Platforms: Mac, iPad, iPhone, Vision Pro; purchase/subscribe once. Longevity: 20-year user testimonial; vendor active since 1994.

Reading: the traditional desktop pole — hierarchy + fold + drag-nest + per-row notes + completion checkboxes as the product's core; columns/styles are document-like extensions; focus = saved-filter navigation.

## Product C — Checkvist

### Key observations

Positioning (homepage): "Keyboard-first outliner for people who think in lists"; "Calm. Focused. Doesn't try to be your second brain."; "Endless hierarchy — on-the-fly navigation and filtering"; "Keyboard-centric — Shift Shift for command palette"; "Shared or private — publish lists publicly, privately, assign tasks, track progress"; "Open and flexible — import, export, integrate. No vendor lock-in." Use cases: project release planning (priorities/tags/due dates), publish checklists (password-protected, time-restricted), research collection (browser clipper), work log, brainstorming results. Testimonial frames it as "collaborative outlining" comparable to OmniOutliner.

Self-description (help): "Checkvist is an online outliner, a task manager and a list-making tool." [A]

Operational model (help/reference): [A]

- Lists: any number of lists; all private by default; share with people or publish publicly; archive; tag lists; extract a branch into a separate list ("cut off" branches, linked back); permalinks preserve filter/expand state.
- List items: Enter adds item below (Alt-Enter above, Shift-Enter sub-item); Tab/Shift-Tab change indentation; Ctrl+↑/↓ move items; drag-and-drop with Shift; delete removes item "with all its sub-items"; edit via ee/F2.
- Navigation: ←/→ collapse/expand; ec menu (expand all / collapse all / collapse to level 1..9); Hoist (focus) — "hide all hierarchy, except one node", parents become breadcrumbs.
- Task semantics on items: "A list item can be open, closed (completed), or invalidated"; parent auto-closes when all sub-items closed (configurable); hide completed; move completed down; wipe/reset completed; progress counters; time-estimate tags summed on parents.
- Item attributes via smart syntax: #tags, ^due dates, @assignees, !1..!9 colors-as-priority; due-date recognition from plain text ("Call John tomorrow"); repeating tasks (PRO).
- Notes: "a note is like a comment on a list item. A note is not a sub-item; it can't have tags or due dates, completed, or invalidated."
- Linking: internal [[ ]] links between list items; "When you create a link, the target list item will show a 'backlink'".
- Sharing: private by default; public unguessable link with view/edit permissions; email invitations; owner/writer/reader roles (owner deletes; writer edits/shares; reader view-only, may act on assigned tasks); embed in web pages; optional password/expiry (PRO); share preserves filter/focus state.
- Interop: OPML import/export (repeating-task info included in OPML); Open API; Zapier; Markdown formatting; email-to-list (each list has an address; subject→item text, body→note); web clipper (Gmail/YouTrack/Jira/GitHub integrations).
- View options: list styles (numbered/boxes/bullets), Zen distraction-free mode, sort (priority/alphabetical/due/created/updated; shallow sort one level), word count, print optimization, saved search/filter bookmarks.
- Mobile: progressive web app.

Reading: same core (item tree + indent + collapse/expand + hoist + subtree move/delete) with the heaviest task layer of the sample — and the vendor itself names the hybrid honestly ("an online outliner, a task manager and a list-making tool").

## Product D — Logseq

### Key observations

Positioning (homepage title): "A privacy-first, open-source knowledge base." [A]

README: "A privacy-first, open-source platform for knowledge management and collaboration"; "focuses on privacy, longevity, and user control"; offers tools for "knowledge management, collaboration, PDF annotation, and task management with support for multiple file formats, including Markdown and Org-mode"; graphs as the container concept (DB graphs; sync/RTC between devices in alpha); desktop/web/mobile apps; plugin API and themes ecosystem. [A]

Lineage: README names its inspirations — "Roam Research, Org Mode, TiddlyWiki, Workflowy, Cuekeeper" — i.e., the vendor itself places the product in the outliner/linked-notes lineage. [A]

Limitation: outline-level editing operations (block indent, folding, zooming) could not be verified from reachable official documentation (docs.logseq.com oversized, repo timeout). No operational outline claims are drawn from Logseq; it enters the sample as the local-first/open-source pole whose storage substrate (plain Markdown/Org-mode files) is directly attested.

## Product E — Roam Research

### Key observations

Positioning (homepage title): "Roam Research – A note taking tool for networked thought." [A]

No further official operational documentation was reachable (JS app; help inside the product; /faq 404). Roam is retained as a representative of the link-dense research pole based on positioning only; all claims about its mechanics are excluded from this research per the evidence rules.

## Cross-product Comparison

| Dimension | Workflowy | OmniOutliner | Checkvist | Logseq | Roam |
|---|---|---|---|---|---|
| Unit of content | bullet/node | row | list item | block (attested as lineage/format, not operations) | block (not verified) |
| Hierarchy | Tab indent, "as deep as you like" | unlimited levels | endless hierarchy | nested (lineage + format) | (not verified) |
| Collapse/expand | implied by zoom model | expand/collapse sections | ←/→, expand-to-level | — | — |
| Focus navigation | Zoom: bullet becomes whole world; breadcrumbs | Focus sections / saved filters | Hoist + breadcrumbs | — | — |
| Subtree operations | structure emerges; node is the object | drag to order/re-order/nest | move/delete/copy/extract with children | — | — |
| Completion state | node type "todo" | row status checkboxes | open/closed/invalidated + parent auto-close | task management listed | — |
| Item attributes | tags, date tags | columns (Pro) | tags, due, assignee, priority-color | — | — |
| Attached prose | (node content) | row note | note = comment, non-item | — | — |
| Search/filter | real-time filter, starred searches | saved filters (Pro) | search + saved filter bookmarks | — | — |
| Links/backlinks | links and backlinks, mirrors | Omni Links (v6) | internal links + backlinks | (lineage attests) | (positioning: networked thought) |
| Container model | ONE infinite document | document files | many lists (extractable branches) | graphs of pages (files) | (not verified) |
| Sharing | share/collaborate, teams | (document-centric product) | owner/writer/reader; public links; embed | RTC in alpha | (not verified) |
| Interop | exporting | (document formats) | OPML, Markdown, API, email-in | Markdown/Org-mode files | — |
| Platforms | web/desktop/mobile sync | Mac/iPad/iPhone/Vision Pro | web + PWA | desktop/web/mobile | web |
| Storage posture | cloud | local documents | cloud | local-first files | cloud |
| Keyboard emphasis | shortcuts, palette, slash | standard | defining trait (two-key shortcuts, palette) | — | — |
| Extra structures | tables, boards, calendar, panes | columns, styles, attachments | notes, attachments (PRO), estimates | PDF annotation, plugins | — |

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal)

1. **Item as the atomic content unit** — short, individually addressable/manipulable text entries (bullet/row/item/block). Remove → free-text editor or document editor.
2. **Indentation-created parent–child hierarchy** — items nest into a tree; a child belongs to its parent's subtree, depth practically unbounded. Remove → flat list (to-do list, plain notes).
3. **Subtree-level structure operations as the primary interaction** — collapse/expand (read-side) and move/re-order/re-parent/delete/copy items TOGETHER WITH their descendants (write-side). Structure manipulation operates on the content's own hierarchy, in place. Remove → static outline text; a text editor with an outline view of a document.
4. **Persistent outline** — the tree is durably held in a document/list/graph that survives sessions. Remove → scratch surface, not a tool of record.

Jointly held: 1+2 without 3 = a nested static text (the thin ancestor: paper outline, typed indented text); 3 without 1+2 = generic drag-and-drop canvas; all four = the Outliner.

### L1 — Common Mature Structure

- zoom / focus / hoist navigation with breadcrumbs (all three operationally attested products)
- completion state on items (todo/checkbox), with derived behavior (parent auto-completion, progress counters) — strongest in task-leaning products, present as item type/checkbox elsewhere
- item attributes: tags, due dates, assignees, priority/color
- attached notes (OmniOutliner row note; Checkvist note-as-comment; Workflowy folds prose into child nodes — different implementations of "longer text beside the item")
- search with real-time filtering; saved searches/filters/bookmarks
- internal links and backlinks between items
- sharing/collaboration with permissions (writer/reader poles in Checkvist; teams in Workflowy; RTC alpha in Logseq)
- export/import with outline interop formats — OPML (Checkvist attested), Markdown/Org-mode (Logseq), product export (Workflowy)
- formatting (Markdown/rich text), themes/styles
- attachments/files
- keyboard acceleration (shortcuts, command palettes, slash commands)
- multi-device surfaces (web/desktop/mobile)

### L2 — Variant / Optional Structure

- Container philosophy: single infinite document (Workflowy) vs. many lists (Checkvist) vs. document files (OmniOutliner) vs. graph of pages over local files (Logseq)
- Storage substrate: vendor cloud sync vs. local-first plain-text files (Markdown/Org-mode)
- Purpose polarity: task/project-oriented (Checkvist's due/assignee/estimates) vs. thinking/writing-oriented (OmniOutliner, Workflowy) vs. knowledge-network-oriented (Roam positioning, Logseq)
- Structure extensions: columns (OmniOutliner Pro), tables/boards/calendar/panes (Workflowy), PDF annotation (Logseq)
- Journals/daily notes (lineage-attested for Logseq; not asserted in detail)
- Presentation mode (Workflowy instant presentations)
- AI assistance (era-current: Workflowy AI surfaces, Apple Intelligence integration in OmniOutliner)
- Monetization shape: freemium with metering unit = the node (Workflowy) vs. one-time purchase/subscription (OmniOutliner) vs. free/open-source (Logseq)

### L3 — Vendor-specific (research notes only)

- Workflowy: mirrors (live-reuse of nodes), fractal comments, Panes, "no folders" single-document philosophy, node-metered free tier (100 nodes/month), Instant Presentations, Email-to-Workflowy, star-a-search sidebar.
- OmniOutliner: Essentials vs Pro split; smart column types (pop-up lists, dates, durations, numbers); named styles; row numbering; Omni Automation plug-ins; Omni Links to document content; Liquid Glass theming (v6).
- Checkvist: two-letter keyboard vocabulary (dd/ll/ee/rd/wipe), Shift-Shift command palette, smart syntax (#tag, ^due, @assignee, !1–!9), per-list email-in addresses, branch→list extraction with auto-sharing, shallow sort, time-estimate tags summed on parents, wipe/reset completed, 24-hour (free) restore window, PRO gating map.
- Logseq: DB version (SQLite) beta, RTC real-time collaboration alpha, plugin API, Org-mode support, Chinese community channel.
- Roam: (nothing asserted — source inaccessible).

## Vendor-specific Findings

(see L3 above; none promoted to the canonical document)

## Rejected Findings

- "An outliner is a task manager" — rejected: only one sample (Checkvist) self-describes as task manager, and it does so as "an online outliner, A task manager AND a list-making tool" (conjunction). Task semantics are L1 item attributes, not the invariant. OmniOutliner/Workflowy are not task-centric.
- "An outliner is defined by bidirectional linking" — rejected: backlinks are common (3/5 with direct evidence) but absent from the two most traditional samples' defining behavior; Workflowy/Checkvist treat linking as one capability among many. L1.
- "An outliner is a cloud, single-document product" — rejected: Workflowy-specific philosophy. OmniOutliner (documents), Checkvist (lists), Logseq (local files) differ. L2 container variant.
- "An outliner is keyboard-only" — rejected: keyboard-centrism is Checkvist's defining trait, a style variant elsewhere. L2.
- "Folding alone defines the outliner" — rejected as too weak: folding is the read-side of subtree operations; the write side (moving/re-parenting subtrees, "reorganizing information" per OmniOutliner) is equally definitional. L0 wording unified as subtree-level structure operations.
- "Blocks/pages/daily-notes model is the modern definition" — rejected: would exclude the traditional document-based desktop pole and the single-document pole. Container model is L2.

## Boundary Findings

- **vs Note-taking Application** (§03.02 sibling, processed 2026-09-08): the note-taking pass pre-hung this seam ("outliner = structure-first hierarchical items"). Confirmed from this side: in note-taking, the unit of record is a free-form note document and organization lives at the library level (containers/tags/links between notes); in the outliner, the unit is the item INSIDE the content and organization IS the content's own indentation tree, operated on directly (indent/fold/move subtrees). Removal tests: remove item-level subtree operations → note-taking (or document editor); remove the free-form page-centric note → outliner. Straddlers: outliner-style note apps exist; Logseq's editing surface satisfies the outliner core while its product promise is knowledge management — classification of such products is a joint-review matter for the PKM pass.
- **vs To-do List Application / Task Management Application** (§03.06): task apps center on tasks (status/dates/projects/assignments) as first-class records; the outliner centers on the item tree, and task semantics appear as optional attributes on items. Checkvist demonstrates the hybrid honestly. Removal test: remove hierarchy/subtree operations, keep task records → task app; keep the tree, add task attributes → outliner with task layer.
- **vs Markdown Editor / Document Editor** (§03.01): markdown/document editors manipulate source text (characters/lines); some offer outline views or heading folding, but items are not first-class manipulable objects and reorganization is text-level. In an outliner the structure operations act on item objects in place. Word-processor outline views are a view mode inside a document editor, not the application's identity.
- **vs Personal Knowledge Management Application** (§03.02 sibling, unprocessed): PKM's promise is a growing connected network of notes (links/backlinks/graph as the point); the outliner's promise is hierarchical structuring of thinking (the tree as the point). Roam ("networked thought") and Logseq (knowledge management platform with outliner lineage) straddle both; the seam must be fixed center-of-gravity at the PKM pass. This pass records: both products satisfy the outliner editing core (Logseq partially attested), so the PKM pass cannot exclude them on editing grounds.
- **vs Wiki / Knowledge Base Application** (§02.06): wiki centers on named pages with inter-page links; the outliner centers on the item tree. Logseq blurs this from the PKM/wiki side, not from the tree side.
- **What makes it a different Type** — removing indentation nesting → flat-list to-do/notes; removing subtree operations → static text/editor; making named pages the first-class object → note-taking/wiki; turning the tree into board columns/timelines → task/project management; making items messages → messaging (irrelevant family).

Historical / market-sample check: the four-part core is satisfied by (a) the traditional desktop outliner pole (hierarchy + fold + drag-nest + per-row notes + checkboxes — OmniOutliner today, and the 1980s–90s desktop outliner generation it descends from, used here only as a weakened reasoning anchor since those products were not fetched); (b) text-mode outlines such as Org-mode-style workflows (heading items + folding + subtree moves over persistent plain files) — satisfied structurally via Logseq's attested Org-mode/Markdown substrate; (c) the paper outline (I./A./1./a.) as the thin pre-history: it has items + indentation + persistence but NOT interactive subtree operations, correctly failing L0 leg 3 — the software Type IS the interactivity of outline structure. No modern capability (cloud sync, backlinks, AI, columns) appears in the core.

## Uncertainties

- Logseq and Roam operational details are unverified (source-access limitation). Consequences: L1 row "links and backlinks" rests on 3/5 products (Workflowy, Checkvist, OmniOutliner v6); Logseq/Roam link behavior is lineage/positioning-inferred only. No numeric limits, defaults, or exact behaviors from these two products are asserted anywhere.
- The exact boundary between "note attached to item" vs "child item as prose" is implemented three different ways in the sample (row note / comment / child node); the canonical model keeps the concept ("longer text beside an item") and leaves the implementation open.
- OPML's status as THE interop format is directly attested for one product (Checkvist, with repeating-task info included) and market-implied elsewhere; kept as common-with-attestation, not universal claim.
- Degree of collaboration in OmniOutliner (document-sharing via OS mechanisms vs live co-editing) was not investigated; OmniOutliner is held as the single-user-professional pole in the sample.

## Final Synthesis

The Outliner is defined by a minimal core: an item as the atomic unit of content; items nested by indentation into a parent–child tree of unbounded depth; the primary interaction being subtree-level structure operations performed directly on that tree (collapse/expand, and move/re-order/re-parent/delete items together with their descendants); and the whole held as a persistent outline. Everything else the market associates with outliners — zoom/hoist focus navigation, todo states with derived completion, tags/due dates/assignees, attached notes, search and saved filters, backlinks, sharing/collaboration, OPML/Markdown interop, columns/tables/boards, keyboard-first operation, cloud vs local-first storage — is standard mature capability or variant, not definition. Container philosophy (one infinite document / many lists / document files / graph of pages) is the sharpest axis of product differentiation and stays at variant level. The boundaries hold against note-taking (library-level vs content-level organization), task apps (tree vs task as center), document/markdown editors (items vs text as the manipulated object), and PKM (tree-first vs network-first promise), with Roam/Logseq flagged as the straddler zone for the PKM pass.
