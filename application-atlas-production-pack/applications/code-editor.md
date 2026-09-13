# Code Editor

## Overview

A **Code Editor** is a general-purpose editing application for program source code: the user edits the plain text of files directly, the file system itself is the working set, and the tooling is organized around the structure of code — its presentation, movement, and search.

The defining structure is small:

```text
File on disk
└── Text buffer (an opened file)
    └── Direct character-level editing
        └── Code-structural affordances
            (code-oriented presentation, movement, and search)
```

No build system, compiler, debugger, or proprietary project artifact is required for the product to be what it is. That is the line between a code editor and an IDE: an IDE integrates a project/build/run/debug model as first-class structure; a code editor treats those as optional additions or leaves them to external tools.

Everything commonly associated with modern editors — tabs, command palettes, semantic completion, integrated terminals, version-control surfaces, extension marketplaces, AI assistance — is widespread in current products but is not part of the defining core. Older, terminal-native, and lightweight editors fit the same definition without any of those layers.

## Users & Context

The primary user is a software developer — writing, reading, navigating, and changing source code as part of the development loop. The same surface serves adjacent technical work: configuration files, build scripts, markup, queries, and data files, because the editor is language-general rather than tied to one content type.

Typical reasons to open the application:

- write or modify code in one or more files
- read and navigate an unfamiliar codebase (jump to definitions, search across files)
- search and replace across a project
- run quick commands (build, test, git) without leaving the editing context

The dominant environment is the local desktop application; terminal-native editors serve the same role inside a shell, and web-delivered editors exist as a variant. The editor usually sits at the center of a toolchain that includes a version control system, a build/test toolchain, and a runtime — but those tools remain conceptually external to the editing core.

## Core Model

### The Defining Core

Three properties. If any one is removed, the product is no longer recognizable as a code editor:

- **Plain-text buffer editing** — the object of work is the raw text of a file, manipulated directly at character level. What the user sees and edits is the characters themselves; there is no rich-formatting layer between the user and the text.
- **File-system persistence and working set** — buffers map to files on disk through an open/save loop, and the working set is files and folders chosen from the file system. Where products offer a "project" concept, it is a lightweight wrapper over folders (settings, open-file state), not a compiled or proprietary artifact.
- **Code-structural affordances** — presentation and movement are keyed to the structure of program text: at minimum code-oriented navigation and search (line/word/bracket movement, find); in modern products syntax highlighting, code folding, and bracket matching; in the most mature products semantic language intelligence such as go-to-definition and diagnostics.

### Standard Capabilities of Mature Products

A typical modern code editor carries most of the following. They are not what makes the product a code editor, but they make it practical for real development work:

- **Multi-file working-set UI** — tabs, split panes, and a file-explorer sidebar over the opened folder.
- **Syntax highlighting and themes** — language-aware coloring, usually with selectable color themes.
- **Find & replace in a file, and search across the working set** — the project-wide search with include/exclude patterns is a daily-use surface.
- **Code navigation** — go to file, go to symbol, go to definition; back/forward navigation history.
- **Completion** — word-based at minimum; language-service-based (semantic) completion in modern products.
- **Undo/redo history** — per-buffer edit history.
- **Command palette** — a searchable entry point to every command, typical of modern GUI editors.
- **Keyboard customization** — keybinding configuration, often with importable keymaps from other editors.
- **Settings system** — user-level preferences with per-project overrides.
- **Extension ecosystem** — packages/plugins/extensions that add language support and tooling.
- **Integrated terminal** — a shell panel inside the editor for build/test/git commands.
- **Version-control integration** — change decorations in the gutter and staging/commit surfaces over an external VCS.
- **Editing conveniences** — snippets, code folding, auto-indent and indentation management, encoding and line-ending handling.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Products realize each concept differently:

```text
Concept:          Text buffer ↔ file
Implementations:  explicit save with dirty indicators, auto-save modes,
                  unsaved-state preservation across restarts

Concept:          Working set
Implementations:  opened folder, multi-root folder set, lightweight project file
                  (folders + settings), plain buffers/windows/tabs

Concept:          Code-structural presentation
Implementations:  regex/grammar-based syntax definitions, AST-based parsing
                  (tree-sitter-style), language-server-driven semantics

Concept:          Keyboard model
Implementations:  direct GUI editing with shortcuts, modal editing
                  (native or emulated vim/helix modes), command palette

Concept:          Extensibility
Implementations:  curated marketplace, package manager, scriptable plugin API,
                  embeddable editor engine
```

A reader who has only seen one implementation (e.g. a marketplace-distributed GUI editor) should still be able to recognize a terminal modal editor or a lightweight paid editor as the same Type from the Core Model.

## How It Works

### Open a working set

```text
Launch the editor
→ open a file, or more commonly a folder (the working set)
→ browse the file tree in a sidebar
→ open files into buffers (tabs or splits)
```

There is no mandatory project creation step. Opening a folder is the whole setup; the editor indexes or scans the files it finds.

### Edit

```text
Type / select / delete in the buffer
→ rely on auto-indent, bracket handling, folding as you go
→ undo/redo as needed
→ save (explicitly, or via auto-save depending on configuration)
```

Editing is character- and line-level text manipulation. Advanced selection models (multiple cursors, column selection) or modal operator grammars (change-inside-brackets, delete-to-mark) accelerate the same underlying operation: changing text in a buffer.

### Navigate and search

```text
Go to file (fuzzy by name)
→ go to symbol (within file or across the working set)
→ go to definition / references (where language intelligence exists)
→ find & replace within a file
→ search & replace across all files, with include/exclude patterns
```

Navigation is the reading half of the loop; search across the working set is how developers answer "where else does this appear?".

### Get language intelligence (as available)

```text
The editor detects the file's language
→ applies syntax highlighting and structure-aware folding
→ offers completion, diagnostics, formatting, go-to-definition
   where a language service or parser for that language is present
```

Capability depth varies by language: some have full semantic support, others only highlighting. The editing core never depends on it.

### Customize and extend

```text
Adjust settings (user-level, with per-project overrides)
→ remap keys or import a keymap
→ install a theme
→ install extensions/packages for additional languages and tools
```

### Beyond editing (optional layers)

```text
Integrated terminal → run builds/tests without leaving the editor
Version-control surface → stage, commit, branch, resolve conflicts
Tasks / build systems → run configured external commands
Debugger integration → attach a debugger (where the product offers it)
AI assistance → completion, chat, or agent panels (era-common bundling)
```

Each layer is additive. A code editor without all of them is still fully itself; this is what distinguishes the Type from an IDE.

### Core vs Common vs Optional

**Defining core** — without these, not a code editor:

- plain-text buffer editing
- file-system persistence and working set
- code-structural affordances (code-oriented presentation, movement, search)

**Standard capabilities** — present in most modern products:

- tabs/splits/explorer, syntax highlighting + themes, find/replace + project-wide search, code navigation, completion, undo/redo, command palette, keybinding customization, settings, extension ecosystem, integrated terminal, VCS integration, snippets/folding/indentation/encoding handling

**Optional / variant** — depends on product philosophy, era, and audience:

- modal editing (native or emulated), multiple cursors
- build tasks and debugger integration (IDE-adjacent)
- remote development over SSH/containers/web
- real-time collaboration
- AI assistance (completion/chat/agents)
- distribution models: free with marketplace, paid license, open source

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Editor surface (buffer view)

The primary surface — where text is actually edited.

- syntax-colored code text, one or more cursors, current selection
- gutter with line numbers (and often change/fold markers), optional code minimap
- primary actions: type, select, cut/copy/paste, undo/redo, fold regions, save

### File explorer / workspace sidebar

The working-set surface.

- tree of files and folders in the opened working set
- primary actions: open a file, create/rename/move/delete files, reveal in file system

### Tabs and split panes

The multi-buffer arrangement surface.

- open buffers as tabs; split the view to see files side by side
- primary actions: switch, arrange, close buffers

### Command palette / launcher

The universal action entry in modern GUI editors.

- searchable list of every command, with fuzzy matching
- primary actions: run any command without touching menus

### Search panel

The working-set-wide search surface.

- query box with match counts grouped by file, include/exclude patterns, replace-with-preview
- primary actions: search, replace across files, jump to a match

### Terminal panel

The shell surface inside the editor.

- one or more shell sessions scoped to the working set
- primary actions: run commands (build, test, git), split terminals

### Source-control surface

The integration surface over an external VCS.

- changed-file list, per-file diffs, staging and commit controls
- primary actions: stage, commit, switch branch, view history/blame (depth varies)

### Settings and keybinding editors

The configuration surfaces.

- searchable settings (user-level and per-project), keybinding list with rebind actions, theme picker

### Extension / package browser

The extensibility surface.

- searchable catalog of language support and tooling packages
- primary actions: install, disable, uninstall, configure

## Important Rules / Behaviors

### Buffer state is visible and load-bearing

The difference between the buffer and the file on disk is a first-class, user-visible state: unsaved changes are marked (dot indicators, badges), and saving is the act that persists them. Products differ on the default (explicit save vs auto-save) and on whether unsaved work survives an abnormal exit, but the buffer↔file distinction itself is structural.

### Language detection drives affordances

The editor infers the language of each file (typically from extension or content) and applies the matching presentation and intelligence. Capability depth varies per language — full semantic support for some, plain highlighting for others — and the editing core never depends on the semantic layer.

### Keyboard-first operation

Nearly every action is reachable from the keyboard, and the keyboard model is a customization surface in its own right (rebinding, keymaps, modal modes). The command palette, where present, makes the full command set discoverable without menus.

### The file system is the project

The editor does not require a proprietary project artifact to function. Where project files exist, they are lightweight, human-readable wrappers (folders, settings, maybe build commands) that can usually be kept in version control — not compiled or opaque containers.

### Editing does not require understanding

The editor can always edit the text even when it does not understand the program: semantic features (completion, go-to-definition, diagnostics) are additive layers over a text core that works for any file. This is why the same tool handles known languages, obscure languages, and arbitrary text.

### Extensibility is the seam for everything else

Language support, themes, linters, VCS polish, and even debugger or AI capabilities typically arrive through the extension/package mechanism rather than the core. A fresh install with no extensions is still a working code editor.

## Variants

The Type is implemented in several recognizable philosophies:

- **extension-platform GUI editor** — free distribution, large marketplace, deep configurability; commonly bundles terminal, VCS, tasks, debugging, and AI layers (e.g. Visual Studio Code)
- **performance-native lightweight editor** — paid license, minimal footprint, fast startup, signature editing models such as multiple selections (e.g. Sublime Text)
- **modal terminal-native editor** — keyboard-modal editing, runs in the terminal, scriptable plugin API, embeddable as an engine (e.g. Vim / Neovim)
- **modern collaborative editor** — performance-focused native client with built-in real-time collaboration and AI panels (e.g. Zed)
- **classic/historical editors** — vi/Emacs-era and 1990s–2000s editors (Notepad++, TextMate, BBEdit class): file-based text editing with code affordances, without the modern bundle; they fit the defining core exactly
- **AI-bundled editors** — current-era products where completion/chat/agent panels ship in the box; the editing core is unchanged
- **remote/web-delivered variants** — the editing surface reaches files on remote machines or in the browser; this drifts toward the Cloud IDE Type

A variant remains a **Variant** unless it changes the core objects or workflow so much that the Core Model no longer applies — as happens when a managed remote workspace with its own lifecycle becomes the product, which is the Cloud IDE boundary.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Integrated Development Environment / IDE | integrates a project model + build + run + debug as first-class structure; a code editor requires none of these and treats them as optional extensions or external tools |
| Cloud IDE | same editing core, but the workspace is managed remote compute with its own lifecycle (provisioning, suspension, retention); a code editor is location-agnostic with local files as the default working set |
| AI Coding Assistant | a capability layer (completion/chat/agents) that increasingly ships inside editors but is not part of the editing core; it is its own Type |
| AI Coding Agent | autonomous multi-step code-changing agent; consumes editor surfaces but is not an editing surface itself |
| Debugger | its own Type; in-editor debugging is an integration over an external or extension-provided debugger |
| Version Control System | the system of record for code history; the editor's VCS surface is a convenience layer over it |
| Markdown Editor | content-type-specific editor for prose documents; the code editor is language-general over program source |
| Web Development IDE | an IDE specialized for web stacks; inherits the IDE's integrated project/build/run model rather than the editor's file-only model |
| Source Code Hosting Platform | repository hosting, review, and collaboration on a server; the editor is the local authoring surface |

The IDE boundary is the most important one, because modern editors increasingly ship IDE-like layers. The structural test: remove the build/debug/project machinery — if the product is still fully itself, it is a code editor; if its identity collapses, it is an IDE. Vendor self-positioning supports this: leading editors describe themselves as "an editor first and foremost" or explicitly reject becoming IDEs, while IDE vendors market the integrated toolchain as the product.

## Representative Products

- Visual Studio Code
- Sublime Text
- Neovim
- Zed

The Core Model was checked against older / terminal-native / lightweight samples (vi/Vim lineage, Notepad++, TextMate, BBEdit class) to avoid over-fitting the definition to the modern marketplace-distributed GUI editor pattern.

## Sources

Research date: **2026-09-07**

Primary vendor documentation (official operational docs):

- Visual Studio Code — https://code.visualstudio.com/docs/editor/codebasics , https://code.visualstudio.com/docs/configure/keybindings
- Sublime Text — https://www.sublimetext.com/docs/ , https://www.sublimetext.com/docs/projects.html , https://www.sublimetext.com/docs/tab_multi-select.html
- Neovim — https://neovim.io/ (features, FAQ, charter)
- Zed — https://zed.dev/docs/ , https://zed.dev/docs/languages

> Sourcing limitations: historical/classic editors (vi, Notepad++, TextMate, BBEdit) were used for the historical breadth check as classification examples without freshly fetched documentation, so no precise operational claims are made about them. Some Sublime Text and Zed documentation pages (VCS depth, tasks) were listed but not read in full; claims touching those areas are kept minimal. Precise product details (exact defaults, key names, feature matrices) are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
