# Research Notes — Code Editor

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 (10-step), WRITING_GUIDE_v1.1

## Research Goal

Understand what a Code Editor is as an Application Type: its defining structure, its standard mature capabilities, its variants, and — most importantly — its boundary against the Integrated Development Environment (IDE), Cloud IDE, and AI Coding Assistant leaves that surround it in the directory.

## Initial Boundary (hypothesis before research)

- A code editor is a text-editing application specialized for program source code.
- It operates directly on files; the file system is the "project container".
- An IDE adds an integrated project/build/run/debug model on top of editing.
- Risk of confusion: modern editors (VS Code) ship debugging, tasks, terminals, AI agents — the editor/IDE line is drawn by vendors themselves, not by feature count.

## Research Questions

1. What is the unit of editing and the persistence model (buffer ↔ file, open/save loop)?
2. What code-structural affordances exist (syntax highlighting, folding, bracket matching, navigation) and are they definitional or common?
3. What is the UI model (tabs, splits, sidebars, panels, command palette, keyboard model)?
4. How is the multi-file working set modeled (workspace, project, session)?
5. Where is the customization/extension seam (settings, keybindings, packages, plugins)?
6. How is language intelligence delivered (LSP, tree-sitter, proprietary indexers)?
7. What sits beyond editing (terminal, VCS, build tasks, debugger, AI) — and is that editor or IDE/AI-assistant drift?
8. How do vendors themselves position "editor" vs "IDE"?
9. Historical check: would older/regional/platform-native editors (vi, Notepad++, TextMate, BBEdit) still fit the definition?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy | Tier / model | Docs fetched |
|---|---|---|---|
| Visual Studio Code | editor-as-extensible-platform, free + marketplace | individual → enterprise | code.visualstudio.com/docs (Basic Editing, Keybindings) |
| Sublime Text | performance-native, lightweight, paid license | individual | sublimetext.com/docs (index, Projects, Tab Multi-Select) |
| Neovim | modal, terminal-native, hyperextensible, open source | expert individuals | neovim.io (home/features/FAQ) |
| Zed | performance + built-in collaboration + AI, open source | modern teams/individuals | zed.dev/docs (Getting Started, Languages) |

## Sources

All fetched 2026-09-07 (Tier 1 — official operational documentation):

- VS Code — https://code.visualstudio.com/docs/editor/codebasics ; https://code.visualstudio.com/docs/configure/keybindings (full doc-tree navigation also captured)
- Sublime Text — https://www.sublimetext.com/docs/ ; https://www.sublimetext.com/docs/projects.html ; https://www.sublimetext.com/docs/tab_multi-select.html
- Neovim — https://neovim.io/ (features, FAQ, charter links)
- Zed — https://zed.dev/docs/ ; https://zed.dev/docs/languages

Historical/market-sample check (§24) rests on classification-level reasoning about vi/Vim, Notepad++, TextMate, BBEdit, Emacs — not on freshly fetched docs; no precise claims are made from memory.

## Product Observations

### Visual Studio Code (evidence layer A)

- Self-positioning: "Visual Studio Code is an editor first and foremost, and includes the features you need for highly productive source code editing." (Basic Editing)
- Editing surface: keyboard shortcuts as primary operation mode with a Keyboard Shortcuts editor; keymap extensions to import shortcuts from other editors (Sublime, Atom, Vim); `keybindings.json`; `when`-clause contexts; chords; command palette ("Show All Commands").
- Buffer/file model: explicit Save by default (dot indicator on unsaved tabs, Explorer badge); Auto Save optional (afterDelay/onFocusChange/onWindowChange); Hot Exit preserves unsaved changes across restarts; file encoding handling; overtype mode; compare files (diff views).
- Multi-cursor editing: multiple selections, column (box) selection, multi-cursor modifier setting.
- Find & replace in file; Search across files in the opened folder (glob include/exclude, respects .gitignore, replace across files with diff preview); Search Editor as a persistent results document.
- IntelliSense: word completion always; richer completions for languages with a language service; formatting (Format Document/Selection; format on type/save/paste); folding (indentation-based default, syntax-aware for some languages, region markers); indentation auto-detection.
- Workspaces: folder-based; multi-root workspaces; workspace trust concept.
- Beyond editing (documented sections): integrated Terminal (profiles, shell integration), Source Control (staging/committing, branches, merge conflicts), Debugging & Testing (debug configuration, tasks), Remote (SSH, tunnels, dev containers, WSL, web), Enterprise (policies), and a large Agents/AI section (Copilot chat, agent mode, MCP, agent customization) — 2026 state.
- Extension model: Marketplace, extension categories (formatters, keymaps), extension runtime security.

### Sublime Text (evidence layer A)

- Docs structure: Usage (Tab Multi-Select, Git Integration, Incremental Diff, Indexing, CLI, Column Selection, Multiple Selection with the Keyboard, Completions, Distraction Free Mode, Vintage Mode, Projects); Customization (Settings, Key Bindings, Font, Indentation, Spell Checking, Build Systems, Packages, Selectors, File Patterns); Package Development (Color Schemes, Themes, Menus, API, Syntax Definitions, Scope Naming).
- Project model: a project is two files — `.sublime-project` (JSON: `folders`, `settings`, `build_systems`) and `.sublime-workspace` (user-specific: open files, modifications); project file meant for version control, workspace file not. → the project is a lightweight file-based wrapper over folders, not a build system.
- Multiple selections: multi-cursor editing is a signature capability; tab multi-select extends the same idea to tabs; Goto Anything; symbol navigation (Goto Definition, Goto Symbol in Project, Definitions popup, Switch Header/Implementation).
- Vintage Mode: vi keybindings emulation inside a GUI editor.
- Build Systems: user-defined external command execution (customization-level, not an integrated project model).
- Packages: extension mechanism with syntax definitions and scope naming (scopes drive language-aware color schemes); Indexing powers symbol navigation.

### Neovim (evidence layer A)

- Self-positioning: "hyperextensible Vim-based text editor".
- Editing model: fully compatible with Vim's editing model (modal editing); `:Tutor` for learning; drop-in Vim compatibility.
- Extensibility: first-class versioned API; MessagePack structured communication enabling extensions in any language; remote plugins as co-processes; Lua plugins; `init.lua` config; can be embedded (`--embed`) by GUIs, IDEs, browsers; GUIs are "inverted plugins" (Neovide, vscode-neovim, Firenvim…).
- Language machinery: tree-sitter AST parsing engine for "fast, accurate syntax highlighting, code navigation, refactoring, text objects, and motions"; builtin LSP client for "semantic code inspection and refactoring (go-to definition, find references, format, …)".
- Builtin `:terminal` ("TTY as a basic component"); client-server architecture (attach multiple UIs to a session).
- Explicit boundary stance (FAQ): "Is Neovim trying to turn Vim into an IDE?" — answered no; the vision is to enable new applications "without compromising Vim's traditional roles."

### Zed (evidence layer A)

- Self-positioning: "Zed is an open-source code editor with built-in collaboration and AI tools."
- Getting started: welcome page → open a project (a folder, via CLI `zed ~/projects/my-app` or Cmd+O); command palette described as "your gateway to every action in Zed"; go to file / go to symbol / find in project / toggle terminal as essential commands.
- Panel layout: "Agentic" (Agent Panel + Threads sidebar) vs "Classic" (editor-oriented) — AI is a first-class panel but optional to the layout.
- Settings editor with searchable settings; theme selector; `buffer_font_family`; `format_on_save`.
- Languages: "hundreds of programming languages and text formats. Some work out-of-the-box and others rely on 3rd party extensions" (built-in languages marked; long community-extension list).
- Migration guides from VS Code, IntelliJ IDEA, PyCharm, WebStorm, RustRover; `vim_mode` and `helix_mode` settings.
- AI: Agent Panel conversation + inline assistance (Cmd+Enter).

## Cross-product Comparison

| Dimension | VS Code | Sublime Text | Neovim | Zed |
|---|---|---|---|---|
| Self-description | "editor first and foremost" | (docs; editor with packages) | "Vim-based text editor" | "code editor with built-in collaboration and AI" |
| Unit of editing | text buffer per file | text buffer per file | text buffer per file (Vim model) | text buffer per file |
| Persistence | explicit save default, auto-save optional, hot exit | save; workspace file tracks open files/edits | Vim file model (:w etc.) | save; format-on-save option |
| Working set | folder / multi-root workspace | project = folders+settings+build_systems JSON | buffers/windows/tabs over files | project = folder |
| Code presentation | syntax highlighting, folding, minimap, themes | syntax definitions + scope-named color schemes | tree-sitter highlighting | built-in + extension languages, themes |
| Navigation | go to definition/peek, command palette, search across files | Goto Anything, Goto Definition, symbol in project, indexing | motions/text objects, LSP go-to | go to file/symbol, find in project, palette |
| Completion | IntelliSense (word + language-service) | Completions | word + builtin LSP | language-server based |
| Keyboard model | default shortcuts + editor + keymaps | key bindings config | modal editing (defining) | default shortcuts + vim/helix modes |
| Extensibility | Marketplace extensions | Packages + API + syntax definitions | Lua plugins + any-language RPC + embeddable | extensions (incl. language support) |
| Terminal | integrated terminal panel | (not in fetched docs; CLI available) | builtin :terminal | toggle terminal |
| VCS | source control section (staging, branches, conflicts) | Git integration, incremental diff | (plugin ecosystem) | (built-in per docs index; not fetched in depth) |
| Build/run | Tasks + debugging (extension-provided debuggers) | Build Systems (external commands) | none built-in (external) | tasks (not fetched in depth) |
| Collaboration | (Live Share heritage; not in fetched pages) | none observed | client-server multi-UI | built-in collaboration |
| AI | Copilot chat/agents/MCP (large docs section) | none observed | none observed | Agent Panel + inline assist |
| Distribution | free, marketplace | paid license | open source | open source + paid collab |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being recognizable as a code editor:

1. **Plain-text buffer editing** — the object of work is the raw text of a file, manipulated directly at character level; what the user sees and edits is the characters themselves (no rich formatting layer).
2. **File-system persistence and working set** — buffers map to files on disk through an open/save loop; the working set is files and folders chosen from the file system. No proprietary project artifact, build system, compiler, or debugger is required for the product to function as itself.
3. **Code-structural affordances on that text** — presentation and movement are keyed to the structure of program text: at minimum code-oriented navigation and search (line/word/bracket movement, find); in modern products syntax highlighting, folding, bracket matching; in the most mature products semantic language intelligence.

Negative invariant (boundary, not a positive property): no integrated build/run/debug/project model is required — that is what separates the Type from the IDE.

### L1 — Common Mature Structure

Present across the researched sample (and expected by the market), but not definitional:

- multi-file working-set UI: tabs, split panes, side-by-side views
- syntax highlighting with selectable color themes
- find & replace within a file; search (and replace) across the working set
- code navigation: go to file, go to symbol, go to definition
- completion (word-based at minimum; language-service-based in modern products)
- undo/redo history
- command palette / fuzzy launcher (modern GUI editors)
- keyboard customization (keymaps, keybinding config)
- settings system (user-level + per-project overrides)
- extension/plugin ecosystem (packages, extensions, plugins)
- integrated terminal
- version control integration (status decoration, staging/commit surfaces)
- snippets, code folding, auto-indent/indentation management, encoding/EOL handling

### L2 — Variant / Optional Structure

- editing philosophy: modal editing (native in Neovim; emulated via vim/helix modes or Vintage Mode elsewhere) vs direct GUI editing; multiple cursors (signature of VS Code/Sublime lineage; absent from the Vim model)
- language-intelligence machinery: LSP client (VS Code, Neovim, Zed) vs proprietary indexer (Sublime) vs none (historical)
- build/run/debug integration: tasks/build systems (Sublime, VS Code), debugger integration (VS Code via debug adapters) — IDE-adjacent, optional
- remote development (SSH/containers/web) — drifts toward Cloud IDE
- real-time collaboration (Zed built-in; VS Code via extension heritage)
- AI assistance (Copilot in VS Code, Agent Panel in Zed) — era-common bundling, drifts toward AI Coding Assistant
- distribution & platform: free+marketplace, paid license, open source; Electron desktop, native desktop, terminal, embeddable engine
- audience posture: individual-first (Sublime, Neovim) vs team/enterprise posture (VS Code enterprise policies, Zed collaboration)

### L3 — Vendor-specific (research notes only)

- VS Code: Hot Exit, Workspace Trust, Profiles, Settings Sync, multi-root workspaces, Search Editor, keymap extensions, Copilot agent-harness architecture (agents, MCP, hooks, prompt files), extension runtime security, minimap/overview-ruler details, `when`-clause context system.
- Sublime Text: Goto Anything, Vintage Mode, `.sublime-project`/`.sublime-workspace` file split, scope-naming system, minihtml, GPU rendering, Sublime Merge cross-sell, side-by-side version installs.
- Neovim: MessagePack RPC, client-server attach/detach, "inverted plugin" GUI architecture, `init.lua`, tree-sitter integration, `:Tutor`, Nvim 0.12 "ui2".
- Zed: agentic vs classic panel layout, welcome page behavior, `vim_mode`/`helix_mode` settings, migration guides, llms.txt docs surface, buffer_font naming.

## Boundary Findings

- **vs Integrated Development Environment / IDE**: the IDE integrates a project model + build + run + debug as first-class structures; the code editor treats them as optional extensions/tasks or leaves them external. Vendor evidence: VS Code self-describes as "an editor first and foremost"; Neovim's FAQ explicitly rejects becoming an IDE; Sublime's project file is folders+settings+build commands, not a compiled project model. Test: remove build/debug/project machinery → still a code editor; remove the file-based text-editing surface → not one.
- **vs Cloud IDE**: same editing core, but the workspace is managed remote compute with a lifecycle (see cloud-ide research). A code editor is location-agnostic; local files are the default working set. Remote-development features in editors are the seam between the two Types.
- **vs AI Coding Assistant / AI Coding Agent**: assistants and agents are capability layers that increasingly ship inside editors (VS Code Copilot, Zed Agent Panel) but are not part of the editing core; they are separate directory leaves. The editor's defining core contains no AI.
- **vs generic text editor (not a directory leaf)**: a code editor is a text editor plus code-structural affordances and developer workflow; a plain text editor (e.g. OS-bundled notepads) lacks the code orientation. Notepad++ self-positions as a "source code editor" while OS notepads do not — the boundary is the code-structural affordance layer.
- **vs Markdown Editor / Document Editor**: those are content-type-specific editors (prose/documents); the code editor is language-general over program source. A Markdown file can be edited in a code editor, but the Type is not defined by a content type.
- **vs Debugger / Version Control System (separate leaves)**: in-editor VCS and debugging are integrations, not the Type. The VCS remains the system of record; the debugger remains its own Type.
- **§24 historical check**: vi (1976, modal, file-based, no syntax highlighting by default, no plugin system, no LSP, no command palette) is unambiguously a code editor; Notepad++ (Windows, syntax highlighting + plugins, no project model), TextMate (bundles, tabs), BBEdit (Mac, programmer/HTML text editor) all fit the L0 without any of the modern L1/L2 layers. Therefore: LSP intelligence, command palette, tabs, GUI, extensibility, and AI must NOT enter the defining core. The L0 above passes this check.

## Uncertainties

- Sublime Text's current VCS/collaboration depth was not fetched in detail (Git Integration page listed but not read); claims about it kept minimal.
- Zed's tasks/build and VCS surfaces were not fetched in depth; the getting-started page confirms terminal and project model only.
- The exact boundary behavior of "editor with debugger extensions" (VS Code) vs "IDE" is a spectrum; the research treats vendor self-positioning + required-vs-optional structure as the discriminator, which is defensible but somewhat judgment-based.
- Historical samples (vi, Notepad++, TextMate, BBEdit) were classified from general knowledge, not fresh fetches; used only for the §24 check, no precise claims.

## Final Synthesis

A Code Editor is a general-purpose editing application whose object of work is the plain text of source files, whose persistence and working set are the file system itself, and whose capabilities are organized around code-structural affordances on that text. Everything else — tabs, palettes, language intelligence, terminals, VCS surfaces, build tasks, debuggers, collaboration, AI — is mature-market structure layered on that core, and the modern market increasingly bundles it. The Type's identity survives the removal of every bundle: what remains is buffer + file + code-structural affordance, which is exactly what vi-era and Notepad++-class products already were. The IDE boundary is structural, not feature-count-based: an IDE requires the project/build/debug model; a code editor does not.
