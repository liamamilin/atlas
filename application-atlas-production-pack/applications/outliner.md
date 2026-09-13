# Outliner

## Overview

An **Outliner** is an application whose unit of work is the outline: short items nested by indentation into a persistent tree, where the primary interaction is operating on that structure directly — collapsing and expanding branches, and moving, re-ordering, or re-parenting items together with everything beneath them.

```text
Item (bullet / row / block)
└── children (created by indentation)
    └── subtree — folded, moved, and restructured as one unit
        └── held as a persistent outline
```

The defining core is deliberately small. Items, nesting, subtree-level structure operations, and a durable home for the tree are what make an outliner an outliner. Everything else the market associates with the category — zoom/focus navigation, todo states, tags and due dates, attached notes, backlinks, collaboration, cloud or local storage — is standard capability layered on top, not part of the definition. Older desktop outliners, single-document web outliners, multi-list task outliners, and local plain-text outlines all satisfy the same core.

When the first-class object stops being the item in a tree — becoming the free-form note document, the named wiki page, or the task record — the product has crossed into a neighboring Application Type (Note-taking, Wiki / Knowledge Base, Task Management).

## Users & Context

The primary user is an individual thinking in lists: capturing ideas, plans, meeting notes, research, writing skeletons, and tasks as a tree they can keep reorganizing. Typical moments:

- dumping thoughts quickly and letting structure emerge through indentation
- reorganizing — promoting, demoting, and reordering branches as understanding develops
- focusing on one branch while the rest of the tree is folded away
- tracking items to completion (checklists, projects, agendas) within the same tree
- sharing an outline or a branch with others for joint work

The same tree routinely serves mixed content — a line of thinking in one branch, a checklist in another, a plan in a third. Team-oriented products add shared lists and role-based access; single-user products remain strictly personal documents.

## Core Model

### The Defining Core

Four properties, jointly held. Remove any one and the product stops being recognizable as an outliner:

- **Item as the atomic unit of content** — each bullet, row, or block is a short text entry that is individually selectable, editable, and addressable. Without discrete items there is only a text editor or a document.
- **Indentation-created hierarchy** — indenting an item makes it a child of the item above; children belong to their parent's branch, and depth is unbounded in practice. Without nesting there is only a flat list.
- **Subtree-level structure operations** — the user folds and expands branches, and moves, re-orders, re-parents, copies, or deletes items *together with all their descendants*. The manipulation acts on the content's own hierarchy, in place. Without this, an outline is just indented text that cannot be restructured.
- **A persistent outline** — the tree lives durably in a document, list, or workspace and survives sessions. Without persistence the tool is a scratchpad, not a record.

### Capabilities Shared by Mature Products

These are widespread in current products and expected by users, but they do not define the Type:

- **Focus navigation** — a way to make one branch fill the view: zooming into a bullet so it "becomes the whole world," hoisting a node above all others, or focusing a section; breadcrumbs to climb back out.
- **Completion state on items** — a todo type or checkbox per item; some products derive state (for example, closing a parent when all its children are done) and show progress counts on branches.
- **Item attributes** — tags, due dates, assignees, and priority or color attached to individual items.
- **Attached prose** — longer text kept beside an item without becoming a sibling item: implemented variously as a row note, a comment on the item, or simply child nodes.
- **Search and saved filters** — real-time filtering of the tree by text, tag, or state; saved searches and filter bookmarks; filtering preserves the tree's shape and context.
- **Internal links and backlinks** — links between items, with the target showing what points to it.
- **Sharing and collaboration** — outlines private by default, shareable via invitation or link, with at minimum view-versus-edit permissions; team features in some products.
- **Import/export and interop** — outline-friendly exchange formats (OPML among them, per directly researched documentation; Markdown and plain text are common), plus printing.
- **Formatting and attachments** — text formatting (often Markdown-based), themes or styles, files and images on items.
- **Keyboard acceleration** — shortcuts, command palettes, and slash commands; in some products the keyboard is the primary interface by design.
- **Multi-device surfaces** — web, desktop, and mobile clients over the same outline.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:            Item
Implementations:    bullet (single infinite document), row (document-based editor),
                    list item (multi-list tool), block (page-based graph tools)

Concept:            Subtree operation
Implementations:    drag-and-drop nesting, keyboard indent/outdent and move,
                    cut/copy whole branches, extract a branch into its own list

Concept:            Persistent outline
Implementations:    vendor-cloud workspace, multiple cloud lists,
                    local document files, local plain-text files (Markdown / Org-mode)
```

A reader who has only seen one shape — say, a single cloud document — should still recognize a document-based desktop outliner or a local plain-text outline as the same Type.

## How It Works

### Capture into the tree

```text
Open the outline (or a list/page within it)
→ type an item (Enter creates the next item)
→ indent (Tab) to make it a child; outdent to promote
→ continue — structure emerges as you go
```

There is no document setup, no template requirement. An item can begin as a single thought and grow children until it is effectively a project or a section.

### Restructure

```text
Select an item
→ collapse or expand its branch to see more or less
→ drag it (or use move keys/commands) to a new position or parent
→ the item travels with all of its descendants
```

Restructuring is the outliner's defining activity: as understanding changes, branches are promoted, demoted, regrouped, or split off — with deletion, copy, and branch extraction operating on subtrees the same way.

### Navigate and focus

```text
Fold the tree down to the level you want
→ zoom into / hoist the branch you are working on
→ parents appear as breadcrumbs
→ search or filter when the tree outgrows browsing
→ jump back out via breadcrumbs or saved locations
```

### Work items as tasks (common overlay)

```text
Mark an item as a todo / give it a checkbox
→ optionally add tags, due dates, assignees, priority
→ complete items; view open/overdue via filters or a due view
→ derived behavior in some products: parent completion, progress counters
```

The task layer rides on the item tree; it never replaces it. A checklist in an outliner is still a branch that can be folded, moved, and restructured like any other.

### Share and take the outline elsewhere

```text
Keep the outline private (default)
→ share with specific people (view or edit) or publish a link
→ export to an interchange format (OPML/Markdown/plain text) or print
```

## Interfaces

Described conceptually; exact layout and vocabulary vary by product.

### Outline editor

The product's main surface — usually its only surface.

- a vertical list of items with indentation levels, bullets/handles, and collapse toggles
- primary actions: create item, indent/outdent, move, edit, fold/expand, complete

### Focus view

The branch-level working view reached by zooming or hoisting.

- the selected subtree shown as the whole screen; ancestor path as breadcrumbs
- primary actions: keep working inside the branch, climb out, share the focused view in some products

### Search / filter

- a persistent query surface over the whole outline: text, tags, states, dates
- primary actions: filter live, edit results in place, save a search as a bookmark or sidebar entry

### Container navigation

- sidebar or home listing the outlines the user holds — one document, many lists, or pages/graphs depending on the product's container model
- primary actions: create/open/archive a container, jump to a recent location

### Sharing surface

- per-outline or per-list sharing controls: invite by email, public link, permission level
- primary actions: invite, change permissions, publish/unpublish, export

## Important Rules / Behaviors

- **The subtree is the unit of structural action.** Deleting, moving, copying, or extracting an item carries its descendants with it. This is the behavior that most distinguishes an outliner from a text editor.
- **Indentation is the hierarchy.** There is no separate "parent" field; making something a child is an indentation act, and re-parenting is re-indenting or dragging. Structure and content are edited in the same gesture.
- **Folding is presentation, not deletion.** Collapsed branches remain in the tree and in searches; hiding completed items is similarly a view state that can be toggled back.
- **Derived completion in some products.** A parent item may auto-complete when all its children are complete, and progress may be counted per branch — product-dependent behavior, not a rule of the Type.
- **Notes are second-class by design in some products.** Where an attached note exists, it typically cannot carry its own status, tags, or children — it decorates the item rather than participating in the tree.
- **Private by default.** Outlines are personal until explicitly shared; shared access is graded (at minimum view vs. edit).
- **Filtering preserves tree context.** Search results and filtered views keep items in their hierarchical shape, or offer to show the parent chain, because position in the tree is part of an item's meaning.

## Variants

- **Container philosophy** — the sharpest market divide: one infinite document holding everything; many named lists; document files edited one at a time; or a graph of pages over local files. The core is identical; the sense of "where outlines live" differs.
- **Storage substrate** — vendor-cloud sync versus local-first plain-text files (Markdown or Org-mode) that the user owns directly.
- **Purpose polarity** — task/project-facing products (due dates, assignees, estimates, progress) versus writing/thinking-facing products (essays, agendas, screenplays, brainstorm) versus knowledge-network-facing products (links, backlinks, daily notes). Many products blend two poles; the tree remains the center in all.
- **Structure extensions** — spreadsheet-like columns on rows, tables, boards, and calendar views built out of the item tree in some products.
- **Interaction style** — keyboard-first designs with two-key command vocabularies versus conventional mouse-driven editing.
- **Platform breadth** — web-only tools, native desktop applications, and full web/desktop/mobile families.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Note-taking Application | the note document is the unit of record and organization lives at the library level (folders/tags/links between notes); in an outliner the organization is the content's own item tree, manipulated directly |
| Personal Knowledge Management Application | PKM's promise is a growing connected network of notes (links, backlinks, graph views as the point); the outliner's promise is the hierarchical tree itself; some products straddle both |
| To-do List Application | centers on task records with status and dates; in an outliner tasks are item attributes on a tree, and the tree operations are the point |
| Task Management Application | broader task workflow (projects, dependencies, boards) as first-class structure; an outliner gains task behavior only as an overlay on items |
| Markdown Editor | edits linear source text where hierarchy is heading syntax; an outliner manipulates discrete item objects whose position is edited by indentation and drag, not by editing characters |
| Document Editor | may offer an outline *view* over a document, but the application's identity is the document, not the tree; in an outliner the tree is the whole product |
| Wiki / Knowledge Base Application | centers on named pages with inter-page links; an outliner centers on items nested inside a tree |

The most important boundary is with Note-taking: both are personal capture-and-return tools, and modern products borrow from each other. The structural test is where organization happens — at the library level between documents, or inside the content as an operable tree.

## Representative Products

- **Workflowy** — minimal cloud outliner; a single infinite document; zoom-into-bullet navigation
- **OmniOutliner** — traditional paid desktop/mobile outliner; document-based with rows, notes, checkboxes, and (in the Pro tier) columns and styles
- **Checkvist** — keyboard-first collaborative outliner and task manager; many lists with tags, due dates, and graded sharing
- **Logseq** — local-first, open-source knowledge tool working on plain Markdown/Org-mode files; outliner editing in service of knowledge management
- **Roam Research** — web outliner positioned around networked thought

The defining core was checked against the traditional desktop pole, the single-document web pole, the multi-list task pole, and the local plain-text pole to avoid over-fitting the definition to any one container philosophy.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Workflowy — https://workflowy.com/ , https://workflowy.com/help/ , https://blog.workflowy.com/
- OmniOutliner — https://www.omnigroup.com/omnioutliner
- Checkvist — https://checkvist.com/ , https://checkvist.com/help/
- Logseq — https://logseq.com/ , https://github.com/logseq/logseq (README)
- Roam Research — https://roamresearch.com/

> Sourcing limitation: Logseq's detailed documentation (docs.logseq.com) exceeded fetch limits and its repository timed out; Roam Research's help content lives inside its JavaScript application and was not reachable. Both products are represented here by their official positioning statements only, and no operational detail is claimed from them. Logseq and Roam enter the representative list as positioning-attested poles; capability claims in this document rest on the three products with reachable operational documentation. Detailed evidence and product-by-product observations are recorded in the paired Research Notes.
