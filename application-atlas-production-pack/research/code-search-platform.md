# Research Notes — Code Search Platform

Research date: 2026-09-07
Slug: `code-search-platform` (DIRECTORY §12 Software Development & Product Engineering)

## Research Goal

Understand what a Code Search Platform actually is as an Application Type: what objects exist inside it, what users do with it, how work flows, which rules matter, and where its boundaries lie against neighboring Types (Code Editor/IDE, Source Code Hosting Platform, Code Intelligence Platform, Enterprise Search Platform, AI Coding Assistant).

## Initial Boundary Hypothesis

- Core use: search across a large body of source code (many repositories or a monorepo) to find where code lives — by text, pattern, symbol, or (increasingly) natural language.
- Primary users: software engineers; secondary: support/SRE (find error strings), security (find vulnerable patterns), new hires (onboarding).
- Nearest neighbors: IDE search (single local workspace), source hosting platforms (embed code search as a capability), code intelligence (precise definitions/references), enterprise search (documents, not code).
- Key unknowns at start: query-language shape per product; whether code navigation (definitions/references) belongs to this Type; permission model; how corpus currency is maintained.

## Research Questions

1. What is the corpus object? (repositories, branches, revisions; how assembled and kept current)
2. What query modes exist? (literal text, exact string, regex, boolean, symbol, natural language; scoping filters)
3. What do results look like and what actions do they enable?
4. How does the platform relate to the VCS / code host? (index source, refresh, permissions)
5. What scale problem justifies a platform rather than IDE/grep?
6. Which structures are common vs optional vs vendor-specific?
7. Where are the boundaries with neighboring Types?
8. Historical check: do older / self-hosted / engine-only products fit the same core?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Pole | Why selected |
|---|---|---|
| GitHub Code Search | hosting-platform-native, SaaS, public+private corpus | the largest code corpus in the market; search embedded in a hosting platform |
| GitLab (basic / advanced / exact code search) | DevOps-suite feature, SaaS + self-managed | shows the suite-embedded pole and a multi-engine fallback architecture |
| OpenGrok | self-hosted engine + read-only web UI, open source | historical anchor (Sun heritage, supports SCCS/TeamWare-era VCS); the classic behind-firewall deployment |
| Zoekt | engine library (trigram index), open source | the engine layer that powers other products (GitLab exact code search); CLI/web/API forms |
| Hound | lightweight self-hosted engine, open source (Etsy origin) | minimal-config engine pole; editor-integration seam |

Sourcegraph — the canonical dedicated commercial code search platform — was selected as a representative product but its official docs were unreachable (403 on both docs.sourcegraph.com and sourcegraph.com/docs; 2 attempts each, abandoned per source-access rules). It is listed as a representative product with no precise feature claims derived from memory.

## Sources

Tier-1 (official operational documentation), all fetched 2026-09-07:

- GitHub Docs — Search on GitHub section:
  - About GitHub Code Search — https://docs.github.com/en/search-github/github-code-search/about-github-code-search
  - Understanding GitHub Code Search syntax — https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
  - Using GitHub Code Search — https://docs.github.com/en/search-github/github-code-search/using-github-code-search
  - Search on GitHub (section root) — https://docs.github.com/en/search-github
- GitLab Docs:
  - Searching in GitLab — https://docs.gitlab.com/user/search/
  - Exact code search — https://docs.gitlab.com/user/search/exact_code_search/
  - Advanced search — https://docs.gitlab.com/user/search/advanced_search/
- OpenGrok:
  - Project page — https://oracle.github.io/opengrok/
  - Features wiki — https://github.com/oracle/opengrok/wiki/Features
- Zoekt — README — https://github.com/sourcegraph/zoekt
- Hound — README — https://github.com/hound-search/hound

Unreachable: Sourcegraph product docs (403 ×2 on docs.sourcegraph.com/code_search and sourcegraph.com/docs/code_search). Assertion strength for the dedicated-platform pole is reduced accordingly.

## Product Observations

### GitHub Code Search (evidence layer A — direct observation)

- Positioning: "search, navigate and understand code across GitHub" — your code, your team's code, and open source. Described as "scalable, code-aware".
- Corpus: indexes repositories you own and repositories in organizations you are a member of (public, private, internal), plus indexed public repositories. "Only users with permission to view your code will be able to see your code in search results."
- Query modes: terms + qualifiers; bare terms match file content OR file path; exact strings in quotes; boolean AND/OR/NOT with parentheses; regular expressions in slashes (look-around not supported); case-insensitive by default, case-sensitive via regex flag.
- Qualifiers: `repo:`, `org:`, `user:`, `enterprise:`, `language:`, `license:`, `path:` (globs supported), `symbol:` (definitions only, Tree-sitter parsing, per-language support list), `content:` (restrict to file content), `is:` (archived / fork / vendored / generated).
- Symbol search: parser-based (Tree-sitter), "no extra setup or build tool integration"; searches definitions, not references; language support list documented.
- Code navigation: "jumping to the definition of and finding references for programming language constructs like classes, structs, functions, and methods" for supported languages.
- UI behaviors: search bar with suggestions/completions organized by category (recent searches, suggested repos/teams/projects, saved searches); saved searches are named, creatable, editable, deletable; searches saved automatically and deletable; results view with filters and result-type navigation (code, issues, PRs, repositories); GitHub Mobile uses the same syntax.
- AI layer: "Ask Copilot" from the search bar — natural-language questions about a repository answered in the Copilot panel (requires Copilot access).
- Index limitations (documented): vendored and generated code excluded; empty files and files over 350 KiB excluded; lines over 1,024 characters truncated; binary files excluded; UTF-8 only; very large repositories may not be indexed; exhaustive search not supported; default branch only; query length limited to 1,000 characters; results restricted to 100 results (5 pages); no sorting for code results; forks excluded by default from code results (includable); "Show identical files" expansion for duplicate paths across repos.
- Login required even for public code search.

### GitLab Search — basic / advanced / exact code search (evidence layer A)

- Three search types with a documented fallback order for code: exact code search → advanced search → basic search (basic does not support group/global search; used for non-default branches).
- Exact code search: powered by Zoekt; exact match mode (default) and regular expression mode (toggle); syntax includes `file:`, `lang:`, `repo:`, `sym:` (symbols like class, method, variable names), `case:yes`, `-` exclusion, `or`; scopes: code only (group/project; global restricted/rollout-gated); Zoekt search API exists; tier: Premium/Ultimate; self-managed requires installing Zoekt and enabling the feature.
- Advanced search: Elasticsearch-based; works across scopes: code, comments, commits, groups, work items, merge requests, milestones, projects, users, wikis; `simple_query_string` syntax (exact `"…"`, fuzzy `~`, or `|`, and `+`, exclude `-`, partial `*`, escape `\`, issue `#`, MR `!`); code qualifiers `filename:`, `path:`, `extension:`, `blob:` (git object ID); documented use cases: "identify code patterns across all projects to refactor shared components", "locate security vulnerabilities across your entire organization's codebase", "track usage of deprecated functions or libraries throughout all repositories".
- Basic search: exact substring matching; `filename:`, `path:`, `extension:` qualifiers; code search shows only the first result in a file; language filter sidebar; view Git blame from a result; commit-SHA search redirects to the commit.
- Access control: global search available to unauthenticated users by default but restrictable (admin settings; visibility levels); global search scopes can be disabled per scope; default search scope configurable.
- Query validation: minimum 2 characters; term-length limits; stop-word-only queries rejected; max 4,096 characters / 64 terms; invalid scope/refname rejected.
- Known issues/limits: files smaller than 1 MB (and < 20,000 trigrams for exact search); default branch only; advanced search shows only the first match per file; archived projects excluded by default (includable).
- Autocomplete suggestions while typing (projects, groups, users, recently viewed items).

### OpenGrok (evidence layer A)

- Self-description: "a fast and usable source code search and cross reference engine. It helps you search, cross-reference and navigate your source tree. It understands various program file formats and history from many Source Code Management systems."
- Deployment: Java + servlet container (Tomcat/GlassFish) + Universal ctags; open source (CDDL).
- Search features (Features wiki): full text, definitions, symbols, path, and revision history search; hierarchical search (limit to any subtree); incremental index updates ("update only the changed files since last time"); "Google like syntax (eg. path:Makefile defs:target)"; files modified within a date range; wildcards; matching lines shown in results.
- VCS web interface (read-only): history log of a file, diffs between revisions (udiff/sdiff), cumulative directory history (RSS).
- Cross-reference: online cross-reference with syntax highlighting, customizable via CSS.
- Extensibility: plugins for new languages and VCS; authorization framework (wiki pages on authorization plugins, HTTP-basic-based authorization); RESTful web services; project groups; suggester.
- Users list includes large installations (link to installations wiki).

### Zoekt (evidence layer A)

- Self-description: "a text search engine intended for use with source code."
- Capabilities: fast substring and regexp matching; rich query language with boolean operators (and, or, not); searches individual repositories and across many repositories in a large codebase; ranks results using code-related signals "like whether the match is on a symbol"; trigram indexing + syntactic parsing (Universal ctags recommended so symbol information can rank results).
- Forms of use: (1) CLI commands to index repositories and search (e.g. index a git repo, sync local repos, search an index); (2) indexserver + webserver — indexserver periodically fetches and reindexes repositories from a code host (e.g. a GitHub organization); webserver serves a web UI and APIs.
- APIs: JSON search API (options include BM25 scoring, context lines), gRPC API (structured query objects, streaming results).
- Heritage: forked from google/zoekt in 2017; now the engine behind GitLab exact code search (per GitLab docs).

### Hound (evidence layer A)

- Self-description: "an extremely fast source code search engine"; core based on Russ Cox's trigram-index regex matching.
- Architecture: static React frontend + Go backend; "The backend keeps an up-to-date index for each repository and answers searches through a minimal API."
- Configuration: a config file lists repositories (URL, VCS config, ref); VCS support: Git (default), Mercurial, SVN, Bazaar, local directory.
- Private repositories: indexable via local directory, file:// clones, or SSH URLs (indexing machine's credentials).
- Currency: polls configured URLs for updates (per-repo poll interval configurable; default 30 seconds — precise number kept here only).
- UI: built-in web UI; minimal JSON API; editor plugins (Sublime Text, Vim, Emacs, VS Code).
- Origin: created at Etsy.

## Cross-product Comparison

| Dimension | GitHub Code Search | GitLab | OpenGrok | Zoekt | Hound |
|---|---|---|---|---|---|
| Corpus | indexed repos (default branch): own + member orgs + indexed public | projects in the instance (default branch for exact/advanced) | source tree from many VCS systems | repos synced from a code host | configured repo list (git/hg/svn/bzr/local) |
| Corpus currency | continuous platform indexing | Zoekt/ES indexing pipelines | incremental index updates | indexserver periodic fetch/reindex | polling updates |
| Query modes | terms, exact strings, regex, boolean, symbol (definitions) | exact/regex (Zoekt), fuzzy+boolean (ES), substring (basic) | full text, definitions, symbols, path, history; wildcards; date range | substring, regexp, boolean; symbol-aware ranking | text (trigram core) |
| Scoping filters | repo/org/user/enterprise/language/license/path/content/is | filename/path/extension/blob; file/lang/sym/repo/case | subtree (hierarchical), project groups | file/lang/repo/sym/case | repo selection |
| Results | file+line matches; capped result set; no sorting | first match per file (basic/advanced); multiple (exact) | matching lines shown | ranked matches (symbol signal) | matching lines/files |
| Code navigation | jump to definition / find references (supported languages) | code intelligence/navigation features; blame from results | cross-reference with highlighting; history/diffs | symbol info used for ranking | — |
| Permissions | results restricted to viewable code | authenticated-only option; visibility levels; scope toggles | authorization framework/plugins | — (engine-level) | — (engine-level) |
| Surfaces | search bar, results view, mobile | search box + scope sidebar; API | web UI; REST API | web UI; JSON/gRPC API; CLI | web UI; minimal API; editor plugins |
| Non-code scopes | separate search types (issues, repos, commits…) | advanced search spans code+commits+comments+wikis+… | — (code/VCS focus) | — | — |
| AI layer | NL questions answered from search bar (Copilot) | (Duo exists; not evidenced in fetched pages) | — | — | — |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a code search platform:

```text
Code corpus (many files / repositories at identified revisions)
└── Query surface (pattern/text selection over the corpus, with code-aware scoping)
    └── Located matches (file + line + the matched code content)
```

Three properties:

1. **A managed code corpus** — the search space is an assembled body of source code spanning many files and repositories (or a monorepo), not a single locally opened workspace. Without this, it is editor/IDE search.
2. **A query surface over that corpus** — queries select code by content/pattern, with scoping by code structure (path, file, language, repository). Without this, it is browsing, not search.
3. **Located matches** — results identify where in the code the match is (file, line) and show the matched code, connecting the hit back to the code itself. Without this, it is a bare index or an analytics product.

Deliberately NOT in L0 (tested against the sample and against older products): the specific index technology (trigram vs inverted full-text vs parser-augmented), symbol search, code navigation, saved searches, permissions machinery, AI answering, history search, APIs. OpenGrok (2013-era feature list, SCCS/TeamWare-era VCS support) and the Hound/Zoekt engine pole satisfy L0 with none of those extras; a 2006-era public regex code search would also satisfy it.

### L1 — Common Mature Structure

Present across most of the sample; expected in mature products but not definitional:

- **Index maintained against the VCS** — the corpus is refreshed as repositories change (continuous platform indexing, incremental updates, periodic fetch, or polling — mechanism varies, the currency expectation is common).
- **Structured query language** — scoping qualifiers (repository/file/path/language) combined with boolean operators and exact/regex modes; query validation rules.
- **Syntax-highlighted results** with matching lines shown.
- **Permission-scoped results** — users see only code they may access (directly documented at GitHub and GitLab; OpenGrok ships an authorization framework; engine-only products leave it to the embedding layer).
- **Default-branch scope** — all three hosted products document default-branch-only code search as the current state.
- **Web UI as primary surface + programmatic access** (API and/or CLI).
- **Symbol/definition search** — parser-derived symbol matching (GitHub `symbol:`, GitLab `sym:`, OpenGrok `defs:`, Zoekt symbol ranking). Common in mature products; absent in the simplest engines (Hound) and in basic GitLab search.
- **Result-to-code navigation** — from a match into the file/revision context (blame, history, file view).

### L2 — Variant / Optional Structure

- **Code navigation precision** (go-to-definition / find references across the corpus) — present in GitHub code search and OpenGrok cross-references; this is the seam toward Code Intelligence Platform.
- **Multi-scope search beyond code** (commits, comments, wikis, issues, users) — GitLab advanced search, GitHub unified search; suite drift.
- **History/commit search** (files changed in a date range, commit search) — OpenGrok, GitLab, GitHub (separate commit search).
- **Saved searches / search history / suggestions-completions** — GitHub (directly documented); OpenGrok suggester.
- **Natural-language / AI layer** — asking questions about a repository from the search bar (GitHub Copilot integration); era-common, maturity varies.
- **Editor integration** — plugins that let an IDE query the platform (Hound plugins).
- **Corpus posture** — public open-source corpus vs private organizational corpus vs both.
- **Deployment** — SaaS vs self-hosted; engine-only vs full platform; suite-embedded vs standalone.
- **Monorepo vs many-repo emphasis.**

### L3 — Vendor-specific (kept out of the final document)

- GitHub: 350 KiB file cap, 1,024-char line truncation, 100-result/5-page cap, 1,000-char query limit, Tree-sitter/linguist stack, `enterprise:` qualifier, `is:vendored/generated`, "Show identical files", `saved:` syntax, Ask-Copilot flow.
- GitLab: `search_type=zoekt|advanced|basic` fallback order, Premium/Ultimate tiering, Elasticsearch `simple_query_string` operators, `blob:` qualifier, 1 MB / 20,000-trigram limits, global-search validation numbers (2 chars, 64 terms, 4,096 chars), admin scope toggles, feature-flag history.
- OpenGrok: `defs:`/`path:` Google-like syntax, udiff/sdiff formats, RSS putback-log, Tomcat/GlassFish deployment, CSS customization, CDDL license.
- Zoekt: trigram design, BM25 option, gRPC API, indexserver config format, origin motto.
- Hound: 30-second default poll, config.json schema, Etsy origin, named editor plugins.

## Vendor-specific Findings

See L3 above. None promoted to the canonical model. The only cross-product reuse worth noting: Zoekt is an engine embedded by GitLab (exact code search) — evidence that the market has an engine layer beneath the platform layer, which supports the "engine-only vs full platform" variant rather than a separate Type.

## Boundary Findings

1. **vs Code Editor / IDE (local search)** — IDE search operates on the user's locally opened workspace; a code search platform operates on a managed corpus the user has not checked out. Test: remove the multi-repo managed corpus → editor search. Conversely, editors can act as clients of the platform (Hound editor plugins). Boundary holds.
2. **vs Source Code Hosting Platform** — hosting platforms store/serve repositories and host collaboration; code search is one capability they may embed (GitHub, GitLab). The Type is defined by the search-primary surface over a corpus; standalone products (OpenGrok, Zoekt, Hound, and the dedicated commercial pole) justify it as a separate Type. Test: remove the search-primary surface and the corpus-index → hosting platform. Note for taxonomy: this Type has a strong "capability of a larger platform" realization; recorded as a structural observation, not a merge proposal.
3. **vs Code Intelligence Platform** — code intelligence provides precise, compiler/LSIF-grade definitions, references, and diagnostics; code search provides pattern matching over text with optionally parser-derived symbols (GitHub's symbol search is explicitly definitions-only and parser-based). Products blur the seam by embedding navigation in search results. Test: remove query/match semantics and keep precise navigation → code intelligence. The directory keeps both leaves; boundary documented, no merge issue.
4. **vs Enterprise Search Platform / Internal Knowledge Search** — enterprise search targets documents, people, and records with relevance ranking; code search is code-aware (tokenization, symbols, paths, languages, VCS structure, permission mirroring of repo access). Test: replace the code corpus with documents → enterprise search.
5. **vs Vertical/general web search engines** — public code search engines over open-source corpora are the same Type with a public-corpus variant, not a different Type.
6. **vs AI Coding Assistant** — natural-language answering over a repository (GitHub's search-bar Copilot flow) overlaps with AI assistants; the assistant's primary surface is conversation/editing, not corpus search. The NL feature is an AI layer on the search surface (L2), not a Type change.

## Historical / Market-Sample Check

- OpenGrok's documented feature set (full text / definitions / symbols / path / history search, hierarchical scoping, incremental indexing, cross-reference UI) satisfies the L0 triple with a 2013-era wiki page and support for SCCS/TeamWare-era VCS — the definition is not an artifact of the modern SaaS era.
- Hound (2015, Etsy) and Zoekt (2017 fork of a Google project) satisfy L0 as bare engines with a web UI.
- The hosted products (GitHub, GitLab) satisfy L0 with permission scoping and richer query languages.
- Conclusion: the L0 triple (corpus + query surface + located matches) is era-stable, deployment-stable, and business-model-stable.

## Uncertainties

- **Sourcegraph evidence gap**: the dedicated commercial platform pole is under-evidenced (official docs 403). Its existence and general positioning are market knowledge, but no precise capability claims about it are made in the final document. If a later pass can access its docs, the L1 list (especially saved searches, code monitoring, batch tooling) may need enrichment.
- **Code navigation placement**: whether cross-corpus go-to-definition/find-references belongs to this Type or exclusively to Code Intelligence Platform is a genuine seam; the sample shows it embedded inside code search products, so it is documented as a common/optional capability with an explicit boundary note.
- **Index freshness semantics**: refresh mechanisms differ (polling, periodic fetch, incremental, continuous); the final document describes currency conceptually without asserting specific latencies.
- **Semantic/AI search maturity**: only one product's NL layer was directly evidenced; the final document treats AI assistance as an emerging optional layer.
- **Public-corpus pole**: grep.app and similar public engines were not fetched; the public-corpus variant is asserted structurally (GitHub's indexed public repos) rather than from a dedicated public-engine sample.

## Final Synthesis

A Code Search Platform is defined by a small invariant: a managed corpus of source code assembled from many files/repositories, a query surface that selects code by content and structure, and results that locate the match in the code itself (file, line, matched content). Everything else commonly associated with the category — index maintenance machinery, query languages with qualifiers, symbol search, code navigation, saved searches, permission scoping, APIs, AI answering — is standard capability or variant structure, not definition. The Type's market realizations span engine-only libraries (Zoekt, Hound), self-hosted engines with web UIs (OpenGrok), suite-embedded search (GitLab), hosting-platform-native search (GitHub), and dedicated commercial platforms (Sourcegraph — under-evidenced in this pass). The sharpest boundaries are against IDE search (local workspace vs managed corpus), source hosting (search-primary vs store/collaborate-primary), and code intelligence (pattern matching vs precise navigation).
