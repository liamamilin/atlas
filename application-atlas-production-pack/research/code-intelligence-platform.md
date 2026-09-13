# Research Notes — Code Intelligence Platform

Slug: `code-intelligence-platform` (DIRECTORY §12 Software Development & Product Engineering)
Research date: 2026-09-10
Methodology: WORKFLOW v1.1 / WRITING_GUIDE v1.1

## Research Goal

Understand what a "Code Intelligence Platform" actually is as an Application Type: what the market sells under this name, what structure the products share, and where the Type's boundaries sit against its dense neighborhood (code search, IDE, static analysis, code quality, architecture modeling, modernization).

## Initial Boundary (hypothesis before research)

- Hypothesis: a platform that computes a language-aware semantic model of a codebase (symbols, definitions, references, relations) and serves it as navigation/understanding surfaces over a corpus larger than a local editor workspace.
- Nearest neighbors: Code Search Platform (processed 2026-09-07, explicitly reserved a seam toward this leaf: "cross-corpus go-to-definition/find-references precision"), IDE / Code Editor (language services), Static Code Analysis Platform (judgment vs mapping), Code Quality Platform, Software Architecture Modeling (authored vs derived), Application Modernization Platform (understanding as input to transformation), Developer Documentation Portal, AI Coding Assistant.
- Unknowns: is "platform" (service posture) definitional, or can desktop tools be in-type? Is heuristic (non-compiler-grade) navigation still "code intelligence"? Where do behavioral-analysis tools (CodeScene) fall?

## Research Questions

1. What does the system compute? What is the "model" — symbols? references? relations? At what precision?
2. How does the model get built and kept current (indexers, build capture, CI, auto-indexing)?
3. What surfaces expose the model (web, desktop, code host, review tool, editor, API)?
4. What do users actually do (jobs): onboarding, impact analysis, review, reverse-engineering, audits?
5. What rules govern results (precision vs heuristic, staleness, coverage, fallback behavior)?
6. Where is the seam vs code search (lexical matching vs resolved identity)?
7. Where is the seam vs IDE language services (understanding-primary vs authoring-primary)?
8. Do older/regional/desktop products fit the same definition (historical check)?
9. Do behavioral-analysis tools ("code intelligence" as marketing umbrella) belong in-type?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Sourcegraph | The namesake platform pole — self-described "code intelligence platform"; multi-repo SaaS/self-hosted; SCIP/LSIF precise + search-based heuristic | The vendor that coined the category language |
| GitHub code navigation | Hosting-platform-embedded pole; free, automatic, tree-sitter heuristic | Shows the capability-of-a-larger-platform realization and the heuristic precision tier |
| SciTools Understand | Desktop deep-analysis pole; per-project database; safety-critical/defense/automotive market | Different philosophy (deep per-language analysis, desktop, air-gapped), different customer tier, long lineage |
| Sourcetrail | Open-source visual explorer pole (archived 2021) | Historical check (§24): older, free, offline desktop form |
| CodeScene | Boundary probe — "behavioral code analysis" | Tests whether behavioral/temporal analysis is in-type |

## Sources

- Sourcegraph docs (legacy mirror, fetchable): https://3.39.sourcegraph.com/code_intelligence , /code_intelligence/explanations/precise_code_intelligence , /code_intelligence/explanations/search_based_code_intelligence (fetched 2026-09-10)
- Sourcegraph current docs domain https://sourcegraph.com/docs/... returned HTTP 403 (same limitation the code-search-platform pass recorded 2026-09-07). Current-docs claims avoided; SCIP repository used as the current protocol-layer source: https://github.com/sourcegraph/scip (README fetched via search excerpt)
- Sourcegraph blog (search excerpt): https://sourcegraph.com/blog/java-scala-kotlin-code-intelligence ; https://sourcegraph.com/blog/announcing-scip
- GitHub Docs — Navigating code on GitHub: https://docs.github.com/en/repositories/working-with-files/using-files/navigating-code-on-github (fetched 2026-09-10)
- GitHub code-navigation public docs repo: https://github.com/github/code-navigation (search excerpt)
- GitHub Blog — Introducing stack graphs: https://github.blog/open-source/introducing-stack-graphs (search excerpt)
- SciTools Understand — What is Understand: https://ai-docs.scitools.com/help/getting-started/what-is-understand.html (fetched 2026-09-10); Read the Information Browser: https://ai-docs.scitools.com/help/explore/information-browser.html (fetched 2026-09-10); product pages https://scitools.com/ , https://scitools.com/features.html (search excerpts); docs root https://docs.scitools.com/ (search excerpt)
- Sourcetrail — README, archived repo: https://github.com/CoatiSoftware/Sourcetrail (fetched 2026-09-10)
- CodeScene — product site https://codescene.com/ (fetched 2026-09-10, boundary probe)

## Product Observations

### Sourcegraph (evidence layer A — legacy docs mirror + SCIP repo; current docs unreachable)

- Self-identification: docs describe Sourcegraph as "the code intelligence platform" (page title of the precise-code-navigation doc).
- Docs carry a first-class "Code intelligence" product section (tutorials / how-to guides / explanations / references), parallel to "Code search".
- "Code Intelligence adds advanced code navigation to Sourcegraph, enabling developers to explore code by: jumping to definitions, finding references, listing implementations, browsing symbols defined in current document or folder, navigate dependencies, documentation in hover tooltips."
- Layered feature model, explicitly "features that build on top of each other":
  - **Search-based code intelligence** — "built-in code intelligence provided by search-based heuristics"; works out of the box for popular languages. Three core features: Jump to definition (performs symbol search), Hover documentation (finds the definition then extracts documentation from comments near it), Find references (case-sensitive word-boundary cross-repository plain-text search). Filters results by file extension and imports for some languages. Uses heuristics "rather than parsing the code into an abstract syntax tree"; incorrect results occur more often for tokens with common names.
  - **Precise code intelligence** — "relies on LSIF data to deliver precomputed code intelligence. It provides fast and highly accurate code intelligence but needs to be periodically generated and uploaded to your Sourcegraph instance." Opt-in; repositories without uploaded indexes "continue to use the search-based code intelligence."
  - **Auto-indexing** — executors create indexes automatically, "up-to-date cross-repository code intelligence."
  - **Dependency navigation** — "navigate and search through the dependencies of your code, by leveraging precise code intelligence and auto-indexing" (dependency code hosts for npm/JVM).
- Cross-repository navigation: precise cross-repo intelligence requires index data for both dependent and dependency repos "at the correct commits or versions"; otherwise results are "supplemented with imprecise search-based code intelligence." Fallback philosophy: "This ensures every symbol has useful code intelligence."
- Adoption ladder documented as a progression: search-based (out of the box) → manual index + upload → CI automation → auto-indexing → auto-dependency indexing.
- Surfaces: "In the Sourcegraph web UI; When browsing code on your code host, via integrations; While looking at diffs in your code review tool, via integrations; In the Sourcegraph API."
- SCIP (successor to LSIF): "a language-agnostic protocol for indexing source code, which can be used to power code navigation functionality such as Go to definition, Find references, and Find implementations." Per-language indexers emit SCIP (scip-java, scip-typescript, rust-analyzer, scip-clang, scip-ruby, scip-python, scip-dotnet, scip-dart, scip-php).
- Marketing/blog claim: "Cross-repository navigation on Sourcegraph makes it possible to find usages of symbols across thousands of repositories–unlike a local IDE that only shows usages in your own project."
- Operational details (L3): ctags-based symbol extraction for search-based CI (universal-ctags), Rockskip experimental indexer for big repos, environment-variable tuning, data-retention policies for uploads.

### GitHub code navigation (evidence layer A — docs.github.com + public docs repo + engineering blog)

- "Code navigation helps you to read, navigate, and understand code by showing and linking definitions of a named entity corresponding to a reference to that entity, as well as references corresponding to an entity's definition."
- Embedded in the hosting platform: "You do not need to configure anything in your repository to enable code navigation. We will automatically extract code navigation information for these supported languages in all repositories." (tree-sitter based; ~21 languages listed.)
- Surfaces: clickable symbols in the file view with a Definition/Reference popover; symbols pane (view and navigate symbols in a file); symbol search scoped to file / repository / all public repositories ("Symbol search is a feature of code search"); keyboard shortcuts.
- Precision posture: heuristic name-binding, not compiler-grade. "GitHub has developed a code navigation approach based on the open source tree-sitter library that searches all definitions and references across a repository to find entities with a given name." The code-navigation repo: navigation "uses code search to find all definitions and references across a repository"; implemented on the Tree-sitter parser ecosystem; fully-qualified names extracted via tag queries to improve navigation and search relevance.
- Stack graphs (engineering blog): "Code navigation is a family of features that let you explore the relationships in your code and its dependencies at a deep level. The most basic code navigation features are 'jump to definition' and 'find all references.'" Stack graphs encode name-binding rules per language; graphs built incrementally per file from tree-sitter parses, merged per commit at query time; "without requiring any configuration from the repository owner, and without tapping into a build process or other CI job."
- Documented limits (product-specific): navigation works on active branches; repositories with fewer than 100,000 files.
- Historical note: GitHub previously supported LSIF uploads for precise navigation; current docs describe the tree-sitter approach (the blog's "Why aren't we using LSP or LSIF?" section explains the choice).

### SciTools Understand (evidence layer A — official docs site + product pages)

- Self-definition: "Understand is a static analysis and code-comprehension tool. You point it at source code and it builds a cross-referenced database of everything in it — every function, class, variable, file, and the relationships between them — without running the code. It reads your existing source; it does not move, rewrite, or require building it (though for C/C++ knowing the build makes analysis more accurate)."
- Framed as four questions: "What is this codebase?" (orientation/structure views), "Where is X used?" (every place referenced; "No more guessing whether a grep hit is the symbol you meant — the answer is resolved against the actual parse"), "Who depends on this?" (call graphs, include/import dependencies, architectures), "Is it risky?" (metrics + CodeCheck — the quality layer).
- Core artifact: the project database (`.und` directory) holding entities and references; "Everything the IB shows comes from the entities and references in the database — the same objects the Python API exposes as understand.Ent and understand.Ref."
- Accuracy machinery (a defining concern of this pole): Strict vs Fuzzy C/C++ analysis, build capture (Build Watcher vs Buildspy, compile_commands.json), per-language accuracy notes, embedded/firmware setup, machine-generated code handling; a docs page titled "Is Understand a compiler?"
- Surfaces: Information Browser ("shows just about everything Understand knows about an entity — adapts to entity type; for a function: what it calls and is called by, parameters, basic metrics, everywhere it's used, set, or modified"; relationship branches expand several hops); Browse Mode (clicking entities in the editor updates the IB); graphs (call tree, butterfly, control flow, UML class, dependency; interactive, expandable); dependency matrix (a DSM); architectures (manual or auto-generated from Git; rule enforcement "X must not depend on Y"); Instant Search; Virtual Debugger (step through logic statically); change-impact/ripple analysis; compare versions.
- Extensions beyond the core (L2/L3): metrics (cyclomatic complexity etc., per-language catalogs), CodeCheck (static-analysis engine with MISRA/CWE/CERT-class checks), compliance/tool-qualification (DO-178C, ISO 26262, IEC 62304, IEC 61508, EN 50128), reports, Python API + `und` CLI (headless/CI), editor integrations (external editors, VS Code extension), AI chat over the analyzed project (local or cloud LLM, MCP), air-gapped deployment.
- Use cases documented: legacy reverse-engineering, safety-critical (aerospace/defense/automotive/medical), mixed-language codebases, refactoring at scale, onboarding, audits/forensics ("review code you don't own"), modernization scoping.
- Market posture: desktop GUI + CLI; per-seat licensing; air-gapped; safety-certified.

### Sourcetrail (evidence layer A — archived README; historical pole)

- "Sourcetrail is a free and open-source cross-platform source explorer that helps you get productive on unfamiliar source code."
- Free, working offline, desktop (Windows/macOS/Linux), C/C++/Java/Python; SDK (SourcetrailDB) "to write custom language extensions."
- C/C++ indexing via LLVM/Clang ("running the preprocessor on the indexed source code, building and traversing an Abstract Syntax Tree"); Java indexer via JDK; Python indexer separate.
- Archived by maintainers end of 2021 (read-only). UI (from project materials): interactive graph visualization combined with source code view and symbol navigation.
- Relevance: proves the Type's core (index a whole project → explore symbols/references/relations visually) existed as a free offline desktop product years before the current SaaS wave; no cloud, no service posture, no multi-repo corpus — still recognizably the same Type.

### CodeScene (evidence layer A — product site; boundary probe)

- Current positioning: CodeHealth™ metric, technical-debt management, AI-risk assessment, PR gates, IDE feedback, MCP server for AI agents. Marketing centers on quality management and delivery impact.
- Its analysis heritage is "behavioral code analysis — go beyond static code analysis": hotspots (change frequency × complexity), temporal/change coupling, knowledge maps from VCS history.
- Structural test result: no symbol-level semantic model (no definitions/references/relations resolution) is offered as the product surface. Under the defining-core test this product belongs to Code Quality / code-analysis territory, not this Type — despite "code intelligence"-adjacent marketing language in the broader market.
- Value of the probe: demonstrates that "code intelligence" as a marketing umbrella is wider than the Type; the Type must be defined structurally, not by vendor vocabulary.

## Cross-product Comparison

| Dimension | Sourcegraph | GitHub code navigation | Understand | Sourcetrail |
|---|---|---|---|---|
| Semantic model | SCIP/LSIF indexes (precise) + search-based heuristics (ctags/symbol search) | tree-sitter name-binding (stack graphs), search-backed | per-project entity/reference database (`.und`), compiler-informed for C/C++ | per-project index (Clang AST / Java / Python indexers) |
| Corpus scope | many repositories + dependencies (cross-repo) | all hosted repositories (per-repo resolution) | one project at a time | one project at a time |
| Precision posture | two-tier, explicit (heuristic default, precise opt-in, documented fallback) | heuristic by design (automatic, no build needed) | deep per-language, accuracy machinery (strict/fuzzy, build capture) | compiler-grade for C/C++ |
| Resolution surfaces | go-to-def, find refs, find implementations, hover docs, symbol browse, dependency navigation | go-to-def, find refs, hover popover, symbols pane, symbol search | Information Browser (entity-centric), graphs, dependency matrix, architectures, ripple analysis | interactive graph + code view navigation |
| Surfaces | web UI, code host integration, review tool, API | code host UI (file view, symbols pane) | desktop GUI, CLI, Python API, editor integrations | desktop GUI |
| Currency | index uploads / auto-indexing vs commits | automatic on push (active branches) | re-analysis on demand / watch | manual re-index |
| Extensions | code search, batch changes, insights, AI (Cody) | code search, hosting platform | metrics, CodeCheck, compliance, reports, AI chat | SDK for custom indexers |
| Customer tier | org-wide engineering (SaaS/self-hosted) | every GitHub user (free, automatic) | safety-critical/defense/automotive teams (per-seat, air-gapped) | individual developers (free, offline) |

Stable across all four: a language-derived model of symbols/definitions + references + relations over a whole codebase; resolution surfaces (definition/reference/hover); relation views; the read-side purpose (understanding existing code); index currency as an operational concern; language coverage as a managed dimension.

Not stable (variant): service vs desktop posture; single-project vs multi-repo corpus; heuristic vs compiler-grade precision; presence of metrics/quality extensions; AI layer.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Three jointly-held structures:

1. **The semantic code model** — a persistent, language-derived structure over a whole codebase (a project, or a multi-repository corpus): symbol definitions, references to them, and relations among code entities (calls, containment, type hierarchies, imports/dependencies). Built by analyzing the code itself — parser, indexer, or compiler-grade; precision varies by product and language, but the model is about code meaning, not raw text. Remove → a text index or file tree (code search / file browsing territory).
2. **Meaning-resolution surfaces** — user-facing ways to resolve code meaning through the model: go-to-definition, find-references/implementations, hover/summary information, and relation views (call trees, dependency graphs, hierarchies). Remove → a raw index/parse dump with no user surface (an engine, not an application).
3. **Read-side purpose at corpus scale** — the product's primary job is understanding and navigating existing code across a whole codebase, for people who did not write it and often do not have it in an editor. Remove → IDE/editor language services (authoring-primary) or single-file tooling.

Jointly-held load-bearing:
- 1 alone = a code-facts database/index (SCIP index files, engine stores — infrastructure, not an application)
- 2 without 1 = lexical "find references" guessing (grep-class navigation — the code-search side of the seam)
- 3 without 1 = documentation/wiki about the code; architecture diagrams not derived from code
- 1+2 without 3 = IDE language services (authoring-primary, workspace-scoped — the IDE Type)
- 2+3 without 1 = code search with navigation aids (search-primary — the Code Search Type)
- 1+3 without 2 = an unused index (no product)

### L1 — Common Mature Structure

- Index maintenance against the VCS/build: re-analysis on change; CI-driven index generation; auto-indexing (Sourcegraph executors; GitHub automatic extraction; Understand re-analysis; Sourcetrail manual re-index)
- Cross-file and cross-repository navigation (the corpus-scale payoff; Sourcegraph's headline; GitHub within-repo; Understand/Sourcetrail within-project)
- Hover documentation extracted from comments near definitions (Sourcegraph search-based CI; GitHub popover; Understand IB)
- Symbol search/browse (Sourcegraph symbol search; GitHub symbols pane; Understand Instant Search/entity lists)
- Relation/graph views: call trees, butterfly/callers-callees, class/inheritance hierarchies, dependency graphs, dependency matrix (Understand's catalog; Sourcetrail's graph view; Sourcegraph dependency navigation)
- Serving the model where code is read: code host integrations, review-tool integrations, editor plugins (Sourcegraph integrations; Understand for VS Code)
- Programmatic access: API/CLI/query surface (Sourcegraph API; Understand Python API + `und`; SourcetrailDB SDK)
- Language coverage as a managed, per-language dimension (indexers/parsers per language; documented support lists)
- Metrics over the model (complexity, coupling) — common in the deep-analysis pole (Understand), absent in the navigation-first pole

### L2 — Variant / Optional Structure

- Precision posture: heuristic (tree-sitter/ctags/search-based) vs compiler-grade (SCIP/LSIF) vs deep per-language (strict/fuzzy, build capture) — products mix tiers with documented fallback
- Platform posture: SaaS/self-hosted multi-repo platform; hosting-platform-embedded capability; desktop application; engine/protocol layer with clients
- Corpus posture: single project vs organization multi-repo vs public corpus
- Analysis extensions: metrics, dependency-rule enforcement, architecture views, change-impact/ripple analysis, dead-code finding
- Behavioral/temporal layer (change coupling, hotspots) — boundary-stretching, quality-adjacent
- AI layer: natural-language chat/answers over the semantic model (Understand AI; Sourcegraph Cody) — an emerging layer, not definitional
- Compliance/tool-qualification packaging (safety-critical market)
- Deployment: cloud, self-hosted, air-gapped desktop

### L3 — Vendor-specific (Research Notes only)

- Sourcegraph: SCIP vs LSIF formats, executors/auto-indexing, Rockskip, dependency code hosts (npm/JVM), Cody, Batch Changes, Code Insights
- GitHub: stack graphs, tree-sitter tag queries/@scope captures, symbols pane, 100k-file limit, active-branch requirement
- Understand: `.und` database, Information Browser, Browse Mode, Buildspy/Build Watcher, Strict vs Fuzzy, Virtual Debugger, CodeCheck, DSM dependency matrix, architectures-from-Git, DO-178C/ISO 26262 qualification, `und` CLI, upython API
- Sourcetrail: three-pane interactive UI, SourcetrailDB SDK
- CodeScene: CodeHealth™, hotspots, change coupling, PR gates, MCP server

## Vendor-specific Findings

- The two-tier precision model (search-based vs precise) with documented fallback is Sourcegraph's explicit design; GitHub's single-tier heuristic design and Understand's deep-accuracy design are different answers to the same problem. No single precision posture is definitional.
- GitHub's "code navigation only works for repositories with fewer than 100,000 files" and "active branches" are product-specific operational limits — not category rules.
- Understand's compliance certifications and CodeCheck are market-segment extensions, not Type structure.
- SourcetrailDB SDK shows the engine/extension seam existed in the open-source pole too.

## Boundary Findings

- **vs Code Search Platform** (seam reserved by that pass): search-primary (query → located matches; text/pattern selection) vs intelligence-primary (resolve meaning: definitions/references/relations). Products ship both (Sourcegraph, GitHub); the seam is the primary surface, not feature presence. The precision gradient is real: lexical cross-references (OpenGrok xrefs, cscope heritage) sit on the search side; heuristic name-binding (stack graphs) and compiler-grade indexing (SCIP) sit on the intelligence side. RATIFIED from this side: keep both Types; code-search pass's "neighboring specialist" framing confirmed.
- **vs IDE / Code Editor**: authoring-primary (editing/building/debugging bound to a project) vs understanding-primary (reading/navigating a corpus). IDE language services are the same intelligence applied in service of editing; editors/IDEs act as clients of intelligence platforms (Sourcegraph editor integrations; Understand for VS Code). The IDE pass's "project as first-class context" vs this Type's "corpus as first-class context."
- **vs Static Code Analysis Platform**: mapping (what is what, where used) vs judging (rule violations with locations). Shared infrastructure (both parse code deeply); different primary surface. Understand ships CodeCheck — an analysis capability inside an intelligence product; the static-analysis pass's core (packaged detection knowledge + located findings) is present as a module, not as the product's identity.
- **vs Code Quality Platform**: quality state/verdict on changes vs structural understanding. CodeScene probe: behavioral analysis + CodeHealth = quality territory; fails the semantic-model leg of L0.
- **vs Software Architecture Modeling**: derived-from-code (actual structure, computed) vs authored model (intended structure, held as source of truth independent of code). Understand's "architectures" are curated groupings over the code database — still derived; architecture-modeling tools hold models that exist whether or not the code matches.
- **vs Application Modernization Platform**: understanding as the end product (answers/navigation) vs understanding as input to a transformation program (assessment → route → tracked transformation). Modernization platforms consume dependency/complexity understanding; they do not serve day-to-day code navigation.
- **vs Developer Documentation Portal**: generated-from-code reference (hover docs, cross-reference pages derived from the parse) vs authored documentation corpus. Doxygen-class generators produce documentation with embedded cross-references — adjacent historical form, documentation-output-primary.
- **vs AI Coding Assistant**: understanding surfaces vs suggestion/answer generation inside the coding flow. AI chat over the semantic model (Understand AI, Cody) is an AI layer on the intelligence surface — variant, not Type change.
- **vs Source Code Hosting Platform**: GitHub shows the intelligence as an embedded capability of the host; the Type is defined by intelligence-primary products (standalone platform/desktop/engine+clients justify the separate Type, same pattern as the code-search pass's hosting-platform reasoning).

### "去掉什么就变成另一个 Type" 判据

- 去掉语义模型（只按文本匹配）→ Code Search Platform
- 去掉 corpus 尺度与 read-side 目的（模型服务于编辑）→ IDE / Code Editor
- 去掉导航表面（只留索引/事实库）→ engine/infrastructure，不是 Application
- 把主表面换成规则判定 → Static Code Analysis Platform
- 把主表面换成质量状态与门禁 → Code Quality Platform
- 把模型换成作者维护的架构模型 → Software Architecture Modeling

## Historical / Market-Sample Check (§24)

- Sourcetrail (2010s, free offline desktop explorer) and Understand (2000s lineage, desktop, per-project) satisfy the three-leg core with no cloud, no service posture, no multi-repo corpus → "platform" posture is NOT definitional; the Type survives the historical check.
- Lexical-era tools (cscope; OpenGrok xrefs) provided definition/reference lookup over whole codebases but are positioned and used as search/browse — they sit on the code-search side of the seam; the intelligence side requires language-derived resolution (heuristic name-binding at minimum).
- Doxygen-class documentation generators (1990s) produce cross-referenced output from source — adjacent form whose primary output is documentation, not an interactive intelligence surface.
- Conclusion: the definition is not over-fitted to the current SaaS multi-repo wave.

## Uncertainties

- Sourcegraph's current (post-3.39) official docs were unreachable (HTTP 403, consistent with the code-search pass's experience). Claims about Sourcegraph are calibrated to the documented code-intelligence layer of the 3.39-era mirror plus the current SCIP repository; the product may have evolved (AI/Cody positioning). No precise current-product claims made.
- The market term "code intelligence" is used loosely (editor features in Zed/Fleet marketing, AI assistants, behavioral analysis). The Type is defined structurally; marketing usage of the term is wider than the Type. Recorded as a taxonomy observation, not a directory change.
- Whether GitHub still supports LSIF-based precise navigation is unclear from current docs (the tree-sitter approach is documented; the LSIF era is documented in older blog/repo material). Treated as historical detail, not asserted as current.
- Exact numeric limits (GitHub's 100k files; Sourcegraph env-var defaults) recorded as product-specific facts in Research Notes only.

## Final Synthesis

A Code Intelligence Platform is the read-side semantic layer over a codebase: it computes a language-derived model of what every symbol is, where it is defined, what references it, and how code entities relate — and serves that model as resolution surfaces (go-to-definition, find-references, hover, relation views) so people can understand and navigate existing code at a scale no single editor session holds. Its neighbors each hold one piece: code search finds text, the IDE applies the same intelligence to authoring, static analysis judges, architecture modeling authors intent, modernization consumes understanding for transformation. The Type's identity is the resolved semantic map of the code itself, served for reading.

The defining core is three jointly-held structures (semantic code model + meaning-resolution surfaces + read-side purpose at corpus scale). Precision posture, platform posture, corpus posture, analysis extensions, and AI layers are variants. The definition survives the historical check (desktop/offline/single-project products fit) and holds the seam with code search on the primary-surface test.
