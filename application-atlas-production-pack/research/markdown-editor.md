# Research Notes — Markdown Editor

Research date: 2026-09-08

## Research Goal

Understand what a Markdown Editor is as an Application Type: what its defining structure is, how real products realize it, how it differs from neighboring editing Types (Code Editor, Document Editor, Distraction-free Writing Application, Note-taking Application), and where the stable seams lie. Produce evidence-calibrated material for the canonical Application Document.

## Initial Boundary

Initial hypothesis (guidance only, not final):

- Core: an editor application whose documents are plain text written in Markdown markup; the application is markup-aware and derives formatted output from that markup (preview / live rendering / export).
- Likely users: documentation writers, developers, bloggers, note-takers, academics.
- Nearest neighbors: Code Editor (markdown as one language among many), Document Editor (direct visible formatting), Distraction-free Writing Application (composition surface as central promise; already flagged as sharing products with this leaf), Note-taking / PKM Application (markdown files as a vault substrate).
- Unknowns: whether rendering is definitional or merely universal; where seamless live-rendering (Typora-class) sits; how vault-style tools relate; whether any dedicated markdown editor ships without preview.

Prior sibling-pass seams recorded in STATUS.md that this pass must honor:

1. **document-editor vs markdown-editor** (document-editor pass, 2026-09-07): discriminator is the formatting model — explicit user-controlled character/paragraph formatting visible during writing vs markup source edited as text with rendering deferred to a separate step. This pass must hold the boundary from its side.
2. **distraction-free-writing-application vs markdown-editor** (distraction-free pass): overlap flag — flagship distraction-free apps (iA Writer, Ulysses) draft in Markdown with preview, so the leaves share products. This pass must apply the whose-central-promise test (attention-preserving composition surface vs markup source handling as central object) and decide keep-both / shared-family note.

## Research Questions

1. What is the source of record: plain-text file? cloud doc? vault entry?
2. How is formatting presented: side-by-side preview, toggle preview, styled-inline, hidden-markup live rendering?
3. What markup-aware editing assistance exists (syntax highlight, toolbar/buttons, shortcuts, completion, table/image/link helpers)?
4. What derives formatted output (rendering engines, flavors, export targets, publishing)?
5. What surrounds the editor (file management, projects/vaults, git, extensibility, AI)?
6. Who uses these products, in which workflows?
7. Historical / platform-native check: does the definition hold for the older generation (Mou lineage, PageDown lineage) and for markdown modes embedded in code editors?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, different customer tiers:

| Product | Pole | Tier of evidence |
|---|---|---|
| iA Writer | minimalist writing environment built on Markdown; commercial; Mac/iOS/iPadOS/Windows | A — official support docs fetched (support index, Markdown Guide, Features, Export/Share/Print) |
| MacDown | classic source+preview open-source editor for macOS; Mou continuation lineage | A — official site (home + features) fetched |
| Markdown Monster | full-featured documentation-oriented editor for Windows; extensible; commercial | A — official docs (root, Features, HTML Preview) fetched |
| StackEdit | in-browser editor; PageDown (Stack Overflow) lineage; cloud-synced | A — official landing page fetched |
| Obsidian | markdown files as substrate of a personal knowledge tool; freemium | A(−) — official product page fetched; help site is a SPA and did not yield content |
| VS Code | platform-native boundary specimen: markdown as a language mode inside a code editor | A — official docs (Markdown and VS Code) fetched |

Market anchors only (no operational claims; sites unreachable after retry budget):

- Typora (support site + product site failed repeatedly — the seamless live-rendering pole is therefore NOT directly evidenced this pass)
- Zettlr (docs site and GitHub README timed out)
- MarkText (site returned a redirect stub)

## Sources

Tier 1 — official operational documentation / product pages (fetched 2026-09-08):

- iA Writer — https://ia.net/writer/support ; https://ia.net/writer/support/basics/markdown-guide ; https://ia.net/writer/support/basics/features ; https://ia.net/writer/support/preview/export-share-print
- MacDown — https://macdown.uranusjr.com/ ; https://macdown.uranusjr.com/features/
- Markdown Monster — https://markdownmonster.west-wind.com/docs ; https://markdownmonster.west-wind.com/docs/Features.html ; https://markdownmonster.west-wind.com/docs/Features/Working-with-the-HTML-Preview.html
- StackEdit — https://stackedit.io/
- Visual Studio Code — https://code.visualstudio.com/docs/languages/markdown
- Obsidian — https://obsidian.md/ (help site https://help.obsidian.md/ is a SPA; only the page title was returned)

Unreachable (retry budget spent, per network rules):

- https://support.typora.io/ , https://typora.io/ (2–3 failures)
- https://docs.zettlr.com/ , https://www.zettlr.com/ , https://github.com/Zettlr/Zettlr (timeouts)
- https://marktext.app/ (redirect stub, no content)

Evidence layers: **A** = directly observed in an official source for a specific product; **B** = cross-product commonality in the sample; **C** = canonical inference from comparison + boundary reasoning.

## Product Observations

### iA Writer (Layer A)

Positioning: "The idea of iA Writer is simple: Focus and enjoy writing." Markdown is the formatting mechanism: "apply basic formatting by adding a few punctuation characters"; "Auto-Markdown will give you instant feedback if you got the formatting right or not."

- Formatting input paths: typing punctuation; Lightning menu (iPad/iPhone); Toolbar; Format menu (Mac/Windows) — i.e., users need not memorize syntax.
- Markdown coverage: headings (6 levels), bold/italic/strikethrough/highlight, ordered/bulleted/task lists with nesting, blockquotes, paragraph/line-break/horizontal-rule/page-break (+++ extension) semantics, images and links (incl. reference links and header cross-references), pipe tables (with a menu option to generate cells; "Smart MD Tables"), TOC via `{{TOC}}`, footnotes, citations, inline code and fenced code blocks, HTML comments, escape character, LaTeX math via KaTeX, super/subscript, metadata block (key-value separated by `---`, referenced as `[%key]`).
- Content Blocks: include images, CSV tables, text files, code as transcluded blocks.
- Editor aids: Focus Mode (sentence/paragraph dimming), Syntax Highlight, Style Check (redundancies/clichés/filler), Stats (word count, reading time), Authorship (highlights self-authored vs pasted/AI text), Smart Automation (auto text completion/transformation), Writing Goals and Folding/Dynamic Outline (Windows), Wikilinks.
- Library: folders, favourites, hashtags; search; documents are files in Library locations; cloud storage provider agnostic (iCloud, Dropbox, Google Drive, OneDrive).
- Preview: HTML preview in real time; PDF preview; equation rendering; templates and custom templates determine the look.
- Export: PDF, MS Word .docx, HTML, Markdown (.md — "unformatted, unstyled, plain-text file format… Preserves your original MD syntax so you can work with this in other Markdown editors/apps"), project archive (.zip incl. content blocks). Print formatted or plain. MS Word import converts formatting to Writer-flavored Markdown (documented conversion table). Ulysses migration via plain-text export.
- Blogging: post drafts to Ghost, Medium, WordPress, Micropub, Micro.blog.
- Platforms: Mac, iPhone, iPad, Windows; paid apps with trial.

### MacDown (Layer A)

Positioning: "The open source Markdown editor for macOS" (MIT), "heavily influenced by Chen Luo's Mou" — created when Mou's development stalled. Continuation of the classic Mac source+preview generation.

- Live preview: Markdown rendered to HTML ("Hoedown is used internally to render Markdown into HTML. This makes MacDown's live preview both efficient and very configurable").
- "Highly customisable Markdown rendering" — preferences control which syntax features are active; supports "lots of non-standard syntactic features, including the very widely-used fenced code blocks with language identifiers".
- Syntax highlighting inside fenced code blocks (rendered by Prism).
- "Sophisticated auto-completion" (can be turned off).
- Additional rendering tools: TeX-like math syntax, GFM task lists, Jekyll front-matter.
- Single-window source+preview shape (site screenshots show two panes).

### Markdown Monster (Layer A)

Positioning: "an easy to use and extensible Markdown Editor for Windows, that provides you with intuitive features to write project based Markdown based documentation quickly efficiently."

- Editor: syntax highlighted Markdown editing; live and synced HTML preview; "gentle, optional toolbar support for Markdown newbies"; keyboard and command support; inline spell checking; line/word counts; synced document outline; distraction-free mode.
- Preview mechanics (documented in detail): renders "in close to real time while you are entering text"; updated when typing pauses (debounced); cursor-position syncing highlights the current paragraph/section in the preview; five preview sync modes (EditorToPreview default, PreviewToEditor, EditorAndPreview, NavigationOnly, None); preview toggleable (F12), internal or external window (docking/second monitor); external browser preview; presentation mode; preview themes customizable via HTML/CSS.
- Explicit format-scoping evidence: "Markdown Monster supports editing a variety of text file formats, but only HTML and Markdown documents present the Preview Pane — for all others toggling has no effect and there is no preview pane." (Rendering attaches to markup-bearing formats — strong evidence that derived rendering is what makes the markdown mode an editor-mode of this Type rather than generic text editing.)
- Image workflow: paste images from clipboard (with auto-compression), embed from disk/URL, drag from Folder Browser/Explorer, edit in external image editor, built-in screen capture.
- Editing aids: link embedding from clipboard/disk, code snippets with highlighted syntax, two-way interactive table editor, emoji embedding, snippet expansion, command palette.
- Output: save rendered output to raw or packaged HTML; save to PDF; copy Markdown selection as HTML; paste HTML text as Markdown; open rendered output in browser; print rendered output; generate and embed TOC.
- File/organization: integrated folder browser; projects; favorites; tabs; find in files; auto-save and auto-backup; encrypted saves; drag-drop from Explorer; open in terminal/explorer/git client; `mm` command-line launcher.
- Git integration: status in folder browser, commit/push dialogs, diff client, undo, clone.
- Weblog publishing: publish/re-publish Markdown posts; post data stored as YAML metadata in the Markdown; MetaWebLog, WordPress, Medium (limited); document-based blogs (Jekyll, Hugo, Wyam, Ghost); download and edit existing posts; multiple blogs.
- AI integration: context-sensitive chat, image generation, optional completions, summarize, translation, grammar/style checking; bring-your-own-key (online and local providers).
- Extensibility: .NET addins; custom markdown parsers; replaceable preview rendering engine; custom toolbar commands; addin catalog.
- Non-markdown editing: HTML with live preview; JSON/XML/CSS/JS/C# and more without preview.

### StackEdit (Layer A)

Positioning: "In-browser Markdown editor", "Designed for web writers".

- Editor: "Markdown syntax highlighting is unique. The refined text formatting of the editor helps you visualize the final rendering of your files."
- WYSIWYG controls: "very handy formatting buttons and shortcuts, thanks to PageDown, the WYSIWYG-style Markdown editor used by Stack Overflow."
- Live preview with Scroll Sync: "accurately binds the scrollbars of the editor panel and the preview panel."
- Smart layout: flexible layouts for writing / reviewing / commenting.
- Sync: files with Google Drive, Dropbox, GitHub. Publishing: blog posts to Blogger, WordPress, Zendesk; choose upload format — Markdown, HTML, or Handlebars-templated output.
- Collaboration: shared collaborative workspaces via the sync mechanism; concurrent edits to the same file are merged; inline comments and embedded collaborator discussions in files.
- Offline: works offline "just like any desktop application."
- Flavors: "supports different Markdown flavors such as Markdown Extra, GFM and CommonMark. Each Markdown feature can be enabled or disabled at your convenience."
- Extended content: LaTeX math, UML diagrams (sequence/flowchart syntax), ABC-notation musical scores, emoji markup.

### Obsidian (Layer A from product page; help SPA not readable)

Positioning: personal knowledge/thinking tool; "The free and flexible app for your private thoughts."

- Storage model: "Obsidian stores your notes locally as plain text Markdown files"; "Obsidian uses open file formats, so you're never locked in. You own your data for the long term."
- Knowledge machinery layered on the markdown substrate: `[[wikilinks]]` between notes; graph view; Canvas (infinite canvas); thousands of community plugins/themes (example cited on the page: "Kanban… Markdown-backed kanban boards").
- Sync (paid): end-to-end encrypted device sync; version history; shared vaults (team collaboration on shared files).
- Publish (paid): "Turn your notes into an online wiki, knowledge base, documentation, or digital garden."
- Note: the editor's own mode details (source mode vs live-preview editing) are documented on the help site, which was not readable this pass; no claims about editor modes are made beyond the product page.

### Visual Studio Code (Layer A — platform-native boundary specimen)

Official docs "Markdown and Visual Studio Code" describe markdown support inside a code editor:

- Markdown is one language mode among ~25 listed languages (JavaScript, Python, C++, …, Markdown).
- Editing aids: Outline view (header hierarchy as symbol tree); snippets; go-to-header in file (⇧⌘O) and across the workspace (⌘T); path completions for image/file links (IntelliSense); drag-and-drop / copy-paste of files and images inserts Markdown link/image syntax, with automatic copying of pasted images into the workspace (configurable destinations); smart selection over markdown block elements; link validation (local links/fragments; warnings; off by default); Find All References for headers/links; Rename Symbol on headers/links updates all referencing links; automatic link updates on file move/rename (opt-in).
- Preview: "toggle the visualization of the editor between the code and the preview" (⇧⌘V) or side-by-side (⌘K V) "and see changes reflected in real-time as you edit"; editor↔preview scroll sync (both directions, disable-able); lockable previews; preview of markdown diffs; custom preview CSS; preview security levels (default Strict: no script execution, https-only resources).
- Renderer targets CommonMark (markdown-it); FAQ explicitly states GFM is not the target.
- Math (KaTeX) and Mermaid diagrams render in the preview.
- "Doc Writer profile template" — curated profile with spell checker and Markdown linter for documentation writing.
- Extensions marketplace supplies further markdown functionality.

### Cross-checks from anchors (no direct evidence)

- Typora is widely known as the seamless live-rendering markdown editor, and Zettlr as an academic-oriented markdown environment — but none of their official documentation was reachable this pass. No operational claims about either are carried into the final document; recorded here only to note the known market poles that this pass could not verify.

## Cross-product Comparison

| Dimension | iA Writer | MacDown | Markdown Monster | StackEdit | Obsidian | VS Code (mode) |
|---|---|---|---|---|---|---|
| Source of record | plain-text .md files in Library locations (cloud-provider agnostic) | local .md file | local files/folders, projects | cloud files (Drive/Dropbox/GitHub) + local workspaces | local vault of plain-text .md files | .md files in workspace |
| Editing surface | markup text with styled inline feedback ("Auto-Markdown") + menus/toolbar | markup text, syntax-highlighted; auto-completion | markup text, syntax-highlighted; optional toolbar | markup text with syntax highlighting + WYSIWYG-style buttons | markup text (help-site details unverified) | markup text as language mode with markdown-specific IntelliSense |
| Rendering | real-time HTML/PDF preview; templates | live preview pane (Hoedown→HTML), configurable | live synced preview pane (internal/external/browser) | live preview with Scroll Sync | (rendering implied by product concepts; not detailed in fetched source) | toggle or side-by-side preview; real-time; scroll sync |
| Markdown-aware helpers | Lightning menu / Toolbar / Format menu; table generation; `{{TOC}}`; metadata | auto-completion; syntax highlighting in code blocks | toolbar; two-way table editor; link/image embedding; snippets; TOC generator; outline | formatting buttons/shortcuts (PageDown) | plugins ecosystem | outline, snippets, path completion, smart selection, link validation, rename-updates-links |
| Export | PDF, DOCX, HTML, MD, ZIP archive; print | (rendered HTML implied; not detailed on fetched pages) | HTML (raw/packaged), PDF, browser, print; HTML↔MD paste conversion | upload as MD / HTML / templated output; publish to Blogger/WordPress/Zendesk | Publish sites (wiki/docs/garden) | (none built in — copy/preview; extensions) |
| Publishing | Ghost/Medium/WordPress/Micropub/Micro.blog | — | MetaWebLog/WordPress/Medium + static-site (Jekyll/Hugo/Wyam/Ghost), YAML metadata | Blogger/WordPress/Zendesk | Obsidian Publish | — |
| Storage/sync | iCloud/Dropbox/GDrive/OneDrive | local | local; cloud config | Drive/Dropbox/GitHub; offline; collaborative merge | local-first; optional E2EE Sync; shared vaults | local/remote workspaces; source control |
| Flavors/extensions | Writer-flavored Markdown incl. math, footnotes, metadata, page-break | Hoedown w/ GFM-ish features, task lists, Jekyll front-matter, math | (custom parser support; math via rendering tools implied) | Markdown Extra / GFM / CommonMark, per-feature toggles | open formats; plugin-dependent | CommonMark (markdown-it), explicitly not GFM |
| Beyond-core extras | Focus Mode, Style Check, Syntax Highlight, Stats, Authorship, Content Blocks, hashtags | — | Git, projects/favorites, AI chat/completions, addins, `mm` CLI | collaborative workspaces, inline comments/discussions, offline | wikilinks, graph, Canvas, plugins, Sync/Publish | Copilot alt-text; preview security model |

Stable commonalities (Layer B) across all six:

1. Plain-text Markdown files are the documents; the markup is the stored format.
2. The user edits the markup text as text; the product knows the markup structure (highlighting at minimum; usually much more).
3. The product derives formatted output from the source — a rendered preview (live/synced or toggled) and/or HTML/PDF export/publishing.
4. Assistance exists to insert/structure markup without hand-typing (buttons, menus, shortcuts, completion, table/TOC/image helpers).
5. Documents are files in folders/workspaces/libraries/vaults; multiple documents are normal; navigation by header outline is common.

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal; jointly-held; removing any leg collapses the Type)

1. **The Markdown document as plain-text source of record** — the working document is plain text whose formatting is expressed in Markdown markup; the markup itself is what is stored and what travels (copy to another tool, open in any text editor, version-control). Remove → no markdown subject; the tool becomes a generic rich-text/document editor.
2. **Markup-source editing surface** — the primary editing surface is the markup text itself; the user writes and revises markup (directly, or via commands that insert markup on their behalf), and the application is aware of the markdown structure. Remove → formatting is applied directly to visible text (word-processor model), not expressed as source.
3. **Derived formatted output** — the application computes formatted output from the markup — a rendered preview (side-by-side, toggle, or styled inline) and/or export/publishing (HTML, PDF, blog/site) — so that presentation is produced from the source rather than styled by the user. Remove → syntax-highlighted text editing inside a plain-text/code editor; the markdown-specific value disappears.

Jointly-held is load-bearing:

- 1+2 without 3 = editing markdown inside a generic text/code editor (a mode, not this Type).
- 2+3 without 1 = a direct-formatting document editor with markdown import/export.
- 1+3 without 2 = a markdown viewer/converter, not an editor.

### L1 — Common Mature Structure (very common; not definitional)

- Syntax highlighting of markup in the editor.
- Markup-insertion assistance: toolbars/buttons, format menus, keyboard shortcuts, auto-completion; table and TOC generators.
- Live/synced rendered preview (scroll/position sync in mature implementations).
- Export ladder with HTML as the universal target; PDF common; print.
- Image and link embedding assistance (clipboard paste, drag-drop, path completion).
- Header-based navigation: document outline / TOC of the file.
- Plain-text files organized in folders/workspaces; multiple documents open; spell check and word count.

### L2 — Variant / Optional Structure

- Flavor selection and per-feature toggling (CommonMark / GFM / Markdown Extra).
- Extended content types: math (KaTeX/TeX), diagrams (Mermaid/UML), task lists, footnotes/citations, emoji, front matter/metadata blocks.
- Export breadth: DOCX round-trip (incl. Word import converting to markdown), styled templates/themes for preview and PDF, custom CSS.
- Publishing integrations: blog platforms (Ghost, Medium, WordPress, Blogger, MetaWebLog, Micropub, Zendesk) and static-site generators (Jekyll, Hugo, Wyam, Ghost).
- Storage postures: cloud file-provider sync (iCloud/Dropbox/Google Drive/OneDrive), repository hosting sync (GitHub), browser-native with offline support, vault/library abstractions over the file system.
- Distraction-free / focus modes; writing-quality aids (style check, authorship attribution, stats/goals).
- Collaboration (shared workspaces with concurrent-edit merge; inline comments/discussions; shared vaults) — present in a minority of the sample.
- Git integration; projects/favorites organization; command-line launchers.
- Extensibility systems (addins/plugins/extensions; custom markdown parsers; replaceable preview engines).
- AI assistance (chat, completions, summarize/translate/grammar, image alt-text generation) — era-current, present in 2 of 6 sampled.
- Platform reach: desktop-native vs mobile vs in-browser.

### L3 — Vendor-specific (research notes only)

- Markdown Monster: five preview sync modes; debounced preview refresh (~0.5s typical, ~2s for very large documents); F12 toggle; `mm` CLI verbs; FoxPro file editing; Commander/Snippets/Gist/Azure addins; encrypted saves.
- iA Writer: Authorship; Style Check; Content Blocks transclusion; `[%key]` metadata references; `+++` page-break extension; `{{TOC}}`; iA Markdown Dictionary; documented Ulysses migration procedure; per-platform feature matrix.
- VS Code: exact shortcuts; `markdown.copyFiles.destination` glob variables; `workbench.editorAssociations` default-preview configuration; locked previews; preview security levels; Doc Writer profile template; CommonMark-explicit FAQ.
- StackEdit: PageDown lineage; Handlebars-templated publishing output; ABC music scores; Zendesk publishing.
- MacDown: Hoedown/Prism internals; auto-completion toggle; Mou lineage story.
- Obsidian: Sync (E2EE, version history) and Publish products; graph view; Canvas; community plugin catalog.

## Vendor-specific Findings (kept out of the canonical core)

- Two-way clipboard conversion (paste HTML as Markdown; copy Markdown selection as HTML) — Markdown Monster only.
- Authorship attribution (human vs AI text highlighting) — iA Writer only.
- Collaborative merge on markdown files — StackEdit only; shared vaults — Obsidian only. Collaboration is NOT a defining property of this Type.
- AI feature sets — vendor-specific shapes; era-current.
- Preview security models — VS Code-specific framing.
- No sampled product required, or even offered everywhere: accounts, per-document permissions, approval flows — consistent with a single-author editing tool by default.

## Rejected Findings

- "Markdown editors are for developers" — rejected: the sample spans writers (iA Writer, StackEdit), documentation authors (Markdown Monster, VS Code Doc Writer profile), knowledge workers (Obsidian). Developer-adjacent machinery (git, CLI) is variant, not core.
- "Preview must be side-by-side" — rejected: toggle preview (VS Code, Markdown Monster F12, iA Writer's open-Preview model) and styled-inline feedback (iA Writer Auto-Markdown) are documented alternatives; the invariant is that formatted output is derived, not which surface carries it.
- "Cloud sync is part of the Type" — rejected: MacDown and Markdown Monster are local-file editors; StackEdit and iA Writer are cloud/file-provider centric. Storage is a variant axis.
- "Seamless hidden-markup live rendering defines the modern Type" — unverifiable this pass (Typora unreachable); excluded from claims. The directly evidenced rendering postures are side-by-side, toggle, and styled-inline.
- "A markdown editor must target one canonical flavor" — rejected: flavor is explicitly configurable in StackEdit (per-feature toggles) and MacDown (rendering preferences); VS Code explicitly targets CommonMark and not GFM. Flavor plurality is the norm; the canonical concept is "a chosen flavor/extension set of Markdown".
- Homonym note: "Markdown Optimization" (§05.14) is retail price-reduction software — unrelated despite the shared word.

## Boundary Findings

1. **vs Code Editor** — markdown-as-a-language-mode inside a code editor shares the whole conceptual structure (source editing + preview + assistance; VS Code documents it in detail). The discriminator is primacy: a Markdown Editor exists for markdown documents — rendering/export is the point of the product, and there is no general code language surface. Markdown Monster's own docs supply the sharpest evidence: the preview pane exists only for Markdown/HTML documents and "for all others toggling has no effect" — rendering attaches to markup-bearing formats, not to text editing generally. Test: remove the markdown primacy (treat .md as one of many text formats, no rendering purpose) → Code/Text Editor; remove the general code surface → Markdown Editor. VS Code is correctly classified as a Code Editor that embeds this Type's structure as a mode; a dedicated product whose whole purpose is markdown editing is the Type.
2. **vs Document Editor** — the formatting model (per the seam recorded by the document-editor pass): the document editor applies explicit user-controlled character/paragraph formatting that is visible while writing and stored in a formatted artifact; the markdown editor stores markup source and derives presentation. Holding from this side: even when a markdown editor styles text inline (iA Writer's Auto-Markdown feedback) the stored artifact is still markup source, and presentation remains computed (preview/templates). DOCX import/export (iA Writer's documented conversion table) is interchange, not a change of model. Test: remove the markup source as the stored format → Document Editor (or a converter).
3. **vs Distraction-free Writing Application** — overlap flag from that pass discharged with the whose-central-promise test. iA Writer is genuine evidence of a both-member product: its central promise is attention ("Focus and enjoy writing"), yet its markdown handling is complete (syntax guide, menus, preview, export, metadata). Decision: **keep-both with the promise-vs-markup seam** — when the attention-preserving composition surface is the product's central promise and chrome is hidden/on-demand, it is a Distraction-free Writing Application even if it drafts in Markdown; when markup-source handling (syntax, preview, rendering, export machinery) is the central object, it is a Markdown Editor even if it offers focus modes. A markdown editor adding a distraction-free toggle (Markdown Monster ships one) does not become a member of that Type.
4. **vs Note-taking / Personal Knowledge Management Application** — markdown files are the substrate of vault-style tools (Obsidian: "stores your notes locally as plain text Markdown files"), with links/graph/canvas/plugins layered on top. Test: when link/backlink/vault/graph machinery is the central promise and documents are atomized notes in a web, the product is a Note-taking/PKM Application; when the editing and rendering of markdown documents is the central promise, it is a Markdown Editor. Obsidian straddles: it is a Markdown Editor at the storage-and-editing layer and a PKM tool by promise. Recorded as a boundary-adjacent sample, not as a reclassification.
5. **vs plain text editor + converter script (thin ancestor)** — a bare text editor with a separate markdown-to-HTML converter satisfies leg 1 only; without in-app markup awareness (leg 2) and in-app derived output (leg 3) it is not this Type. The older dedicated generation (Mou lineage — MacDown explicitly continues it; PageDown lineage — StackEdit explicitly builds on Stack Overflow's editor) satisfies all three legs with nothing beyond source+preview: historical check passes; nothing modern (cloud, plugins, AI, themes) is definitional.
6. **vs Blogging Platform / CMS** — publishing to blogs/static sites is output plumbing layered on the editor (iA Writer, StackEdit, Markdown Monster all document publishing integrations); the platform that hosts and renders content for readers is a different Type.
7. **Shared-storage consequence** — because the artifact is plain text, interchange across tools is native (iA Writer's export doc explicitly says .md "can be opened across a wide range of systems and apps… so you can work with this in other Markdown editors/apps"). No lock-in layer is part of the Type; products may add proprietary layers (Obsidian's wikilinks are a syntax extension carried inside the plain text; Ulysses' database is recorded as the counter-case that requires export).

## Uncertainties

- The seamless live-rendering posture (Typora-class) could not be verified from official sources this pass; the final document therefore describes rendering postures only at the directly evidenced level (side-by-side, toggle, styled-inline) and notes that presentation varies.
- Zettlr (academic pole) and MarkText unreachable; academic-workflow breadth (citations, bibliography tooling) is evidenced only via iA Writer's citation/footnote syntax, so scholarly tooling breadth stays out of the final document's claims.
- Obsidian's editor-mode specifics (source vs live-preview editing) not directly documented in fetched sources; claims about Obsidian limited to its product page (storage model, links, plugins, Sync/Publish).
- Whether any dedicated markdown editor ships with syntax highlighting but no rendering at all: not established in the sample; no claim either way. (The canonical model treats rendering as definitional; a hypothetical renderer-less editor would be an edge case at the text-editor seam.)
- Precise operational numbers (e.g., Markdown Monster's ~0.5s preview debounce, VS Code shortcut keys) are recorded here only; they do not belong in the final document.

## Final Synthesis

A Markdown Editor is a document-editing application whose defining structure is three jointly-held properties: the document of record is a plain-text file whose formatting is expressed in Markdown markup; the primary editing surface is that markup source (with the application aware of the markdown structure and assisting its insertion); and the application derives formatted output from the source — a rendered preview and/or export/publishing — rather than the user applying styles directly. Formatting is data in the file, not styling applied to it.

Mature products complete this with syntax highlighting, markup-insertion helpers, live/synced preview, an export ladder (HTML universal; PDF common; DOCX and templates optional), image/link embedding assistance, header-based outline navigation, and file/folder-based multi-document work. Flavor configuration (GFM/CommonMark/Markdown Extra), math/diagram/task-list extensions, publishing integrations, cloud/repository/vault storage postures, focus modes, collaboration, git, extensibility, and AI are variant or optional structures. Users are documentation writers, developers, bloggers/web writers, note-takers and academics; the common thread is writing structured prose for the web in a format that any tool can open.
