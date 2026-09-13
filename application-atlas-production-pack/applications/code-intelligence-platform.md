# Code Intelligence Platform

## Overview

A **Code Intelligence Platform** computes a language-aware model of a codebase — what every symbol is, where it is defined, what references it, and how code entities relate to one another — and serves that model as navigation and understanding surfaces: go-to-definition, find-references, hover documentation, call and dependency views. Its purpose is to let people understand and navigate existing code at a scale no single editor session can hold.

The problem it solves is the gap between *reading code as text* and *understanding code as meaning*. A text search can find every occurrence of a name, but it cannot tell you which occurrence is the definition, which are genuine uses, or how a function relates to its callers across files and repositories. A code intelligence platform resolves those questions against an analysis of the code itself, and holds the answers as a persistent, explorable model of the whole codebase — a project, an organization's many repositories, or a public corpus.

The defining core is small:

```text
Semantic code model (symbols / definitions / references / relations,
                     derived from the code by language-aware analysis)
└── Meaning-resolution surfaces
    (go-to-definition, find-references, hover info, relation views)
    └── Read-side purpose at corpus scale
        (understanding existing code across a whole codebase)
```

Everything else commonly associated with the category — cross-repository scope, compiler-grade precision, automatic indexing, metrics, graph catalogs, AI chat — is standard capability or variant structure, not definition. Older and differently positioned products (free offline desktop explorers, per-project analysis tools) satisfy the same core without any of those extras.

## Users & Context

The primary user is a software engineer who needs to understand code they did not write, or code they cannot hold in their head:

- a developer onboarding to an unfamiliar codebase or team's code
- a developer assessing the impact of a change ("what calls this?", "what breaks if this moves?")
- a reviewer or maintainer reading a proposed change against the code it touches
- an engineer reverse-engineering legacy or inherited code

Secondary users and contexts:

- architects and tech leads reasoning about system-level structure — dependencies, layering, coupling
- auditors, forensics, and quality roles reviewing code they don't own
- platform/tooling teams who operate the deployment for the organization (self-hosted platforms)

The work environment sits alongside the editor and the code host. The dominant surfaces are a web interface (multi-repository platforms), the code host's own file views (embedded navigation), and desktop applications (deep per-project analysis, common in safety-critical and air-gapped environments). The platform's model is also consumed programmatically — through APIs, CLIs, and editor integrations — so the same intelligence appears wherever code is read: in the browser, in the code host, in the review tool, in the editor.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as a code intelligence platform:

- **The semantic code model** — a persistent, language-derived structure over a whole codebase: symbol definitions, references to them, and the relations among code entities (calls, containment, type hierarchies, imports and dependencies). It is built by analyzing the code itself — by a parser, an indexer, or compiler-grade analysis, depending on the product and language. What makes it a *semantic* model rather than a text index is that identity is resolved: a reference is linked to the definition it actually refers to, not to every string that looks like it. Without this model, the product is a text index or a file tree.
- **Meaning-resolution surfaces** — the user-facing operations that answer meaning questions through the model: jump to the definition of a symbol, find all references to it, see its documentation on hover, and view its relations (call trees, inheritance hierarchies, dependency graphs). Without these surfaces, the model is an unused database — infrastructure, not an application.
- **Read-side purpose at corpus scale** — the product's primary job is understanding and navigating *existing* code across a whole codebase, for people who did not write it and often do not have it checked out locally. Code changes happen elsewhere; this is the place where code is read. Without this purpose, the same intelligence is an IDE's editing aid; without the corpus scale, it is a single-file tool.

### Standard Capabilities

Mature products commonly add the following. They make the platform practical but do not define it:

- **Index currency** — the model is kept in step with the code: re-analysis on change, index generation in CI, or fully automatic extraction on push. Currency is an operational property; results reflect the last analyzed revision, not the user's working tree.
- **Cross-file and cross-repository navigation** — the corpus-scale payoff: following a symbol from its use in one file to its definition in another file, another repository, or a third-party dependency.
- **Hover documentation** — doc comments attached to definitions, surfaced where the symbol is used.
- **Symbol search and browse** — finding and listing symbols (functions, classes, methods) as first-class objects, alongside or instead of text search.
- **Relation and graph views** — call trees, callers/callees, class and inheritance hierarchies, dependency graphs, and dependency matrices, rendered from the model.
- **Serving the model where code is read** — integrations into code hosts, review tools, and editors, so navigation works outside the platform's own UI.
- **Programmatic access** — an API, CLI, or query surface over the same model, for scripts, tools, and integrations.
- **Language coverage as a managed dimension** — per-language parsers or indexers, with documented support lists; coverage and precision vary by language.
- **Metrics over the model** — complexity, coupling, and size measures computed from the analyzed structure (common in the deep-analysis pole of the market).

### One Structure, Many Implementations

The core model is conceptual; products realize each part differently:

```text
Concept:            Semantic code model
Implementations:    compiler-grade index formats uploaded per commit; parser-derived
                    name-binding computed automatically; per-project entity/reference
                    databases built by deep per-language analysis

Concept:            Precision
Implementations:    heuristic name resolution (fast, automatic, occasionally wrong);
                    compiler-grade resolution (accurate, requires index generation);
                    deep per-language analysis with build capture — products mix tiers
                    and fall back between them

Concept:            Corpus
Implementations:    an organization's many repositories; a single project; a public
                    open-source corpus; a hosting platform's hosted repositories

Concept:            Resolution surfaces
Implementations:    clickable symbols in a file view; entity detail panels; interactive
                    graph canvases; dependency matrices; query languages over the model
```

A reader who has only seen one implementation — say, automatic navigation on a code-hosting site — should still be able to recognize a desktop analysis tool or an index-based multi-repository platform as the same Type from the core model.

## How It Works

### Build the model

```text
Point the platform at a codebase (project, repository set, or hosted corpus)
→ analyze the code with per-language parsers/indexers
  (optionally informed by the build: captured compile commands, build watching)
→ store the resulting model: definitions, references, relations
→ refresh as the code changes (re-analysis, CI-generated index uploads,
  or automatic extraction on push)
```

Building the model is the platform's defining act, and accuracy is a first-class concern. Products document how to make analysis precise — supplying build information for languages where names resolve differently depending on how the code is compiled, handling generated code, and noting per-language limitations. The heavier the precision, the more machinery is involved: some products ask teams to generate and upload indexes from their own CI; others compute everything automatically at lower precision.

### Resolve meaning

```text
Open code (in the platform's UI, the code host, or the review tool)
→ click or hover a symbol
→ the platform resolves it against the model:
   its definition, its references, its documentation
→ follow the chain: from a use to the definition,
   from the definition to every reference,
   across files, repositories, and dependencies
```

This loop is the product's heart. The value over text search is resolution: the answer is computed against the actual parse, so a hit is the symbol you meant, not a string that looks like it. Products are explicit about the limits — where no precise index exists, results may come from heuristic name matching, and mature products say so, falling back gracefully so that every symbol has *some* useful answer.

### Explore structure

```text
Pick an entity (function, class, file, module)
→ view its relations: what it calls, what calls it,
   what it inherits from, what it depends on
→ render the structure: call trees, graphs, hierarchies,
   dependency matrices
→ walk the structure to reason about impact, layering, and coupling
```

Beyond point resolution, the model supports structural views: expanding a call tree several hops, rendering the dependency graph of a directory, or comparing two versions of the codebase to see what a change affects. In the deep-analysis pole these views extend to curated architecture groupings and dependency-rule checking ("this layer must not depend on that one") — still computed from the code, not drawn by hand.

### Serve it where code is read

```text
The same model is exposed through:
→ the platform's own web or desktop UI
→ the code host's file views (embedded navigation)
→ the code review tool (navigation on diffs)
→ the editor (plugins and integrations)
→ APIs and CLIs (scripts, tools, custom clients)
```

### Keep it current

The model is a living artifact with an operational lifecycle: index generation, upload or extraction, refresh on change, retention of old revisions. Currency rules matter to users: navigation reflects the last analyzed revision; brand-new code may not yet be resolved; old revisions may or may not be covered. Products differ in how automatic this is — from fully automatic extraction to scheduled re-analysis — but every product has an answer, and every user learns its currency behavior.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Code view with resolution affordances

The primary reading surface: a file's source with symbols made interactive.

- clickable and hoverable symbols; definition/reference popovers
- primary actions: jump to definition, find references, open the symbols pane

### Entity / symbol detail

The "everything known about this symbol" surface.

- definition location, callers and callees, references, members, documentation, related metrics
- relationship branches that expand several hops without leaving the view
- primary actions: navigate to any listed location, open a relation view

### References / definitions panel

The result surface of a resolution.

- the list of places a symbol is defined, referenced, or implemented, grouped by file or repository
- primary actions: open a result in place, scope the search, switch between definitions and references

### Graph and structure views

The visual surface over relations.

- call trees, callers/callees ("butterfly") views, class and inheritance hierarchies, dependency graphs, dependency matrices
- interactive: expand, contract, filter, color by metric
- primary actions: navigate between graph and code, export, restyle

### Search

Symbol search and text search over the corpus. In mature products the two are distinct but adjacent: text search finds occurrences; symbol search finds the parsed entities. Some products share this surface with a full code-search capability.

### Administration / configuration

The operator surface (self-hosted and desktop products).

- which repositories/projects to analyze, credentials, index settings and refresh behavior, integrations, access control
- primary actions: connect sources, trigger or schedule analysis, manage index retention

### Programmatic interfaces

- APIs, CLIs, and query surfaces exposing the model to scripts and tools; in some products, an SDK for building custom language indexers

## Important Rules / Behaviors

### Resolution quality varies, and products say so

The model's precision depends on the language, the analysis depth, and whether an index exists for the code being viewed. Mature products are explicit about the tiers: heuristic resolution is fast and automatic but can mis-resolve common names; compiler-grade resolution is accurate but requires index generation; and products fall back from the precise tier to the heuristic tier when index data is missing — for the file, the repository, or a dependency — so that every symbol still gets a useful answer. A user learns to read which tier produced a result.

### The model reflects the last analysis, not the working tree

Navigation answers are computed against an analyzed revision. Code written since the last analysis may not resolve; branches may not be covered until they are indexed; very large repositories or unusual languages may be excluded. A miss in navigation is not proof of absence in the code — coverage and currency limitations are documented, expected behavior.

### Resolution is not text matching

The platform's core promise is resolved identity. Where a product cannot resolve — no parser for the language, no index for the revision — it degrades toward text matching, and the difference is visible to the user. This gradient is the honest boundary between this Type and plain code search.

### Read-oriented by design

The platform's job is understanding, not changing code. Edits happen in the editor and flow through version control and review; the intelligence platform reads the result. Some products add annotations or notes, and deep-analysis tools may offer refactoring aids, but the write path is never the primary surface.

### Results mirror access (multi-repository platforms)

In organizational deployments, navigation respects repository permissions: users resolve symbols only within code they are allowed to see. The model may contain more than any single user can view, and results are filtered per requester.

## Variants

- **Multi-repository platform** — a dedicated product (SaaS or self-hosted) indexing an organization's many repositories and their dependencies; cross-repository navigation is the headline capability.
- **Hosting-platform-embedded navigation** — the same intelligence embedded in a source-hosting platform, computed automatically for hosted repositories; free and zero-configuration, at heuristic precision.
- **Desktop deep-analysis tool** — a per-project application building a rich local database with deep per-language analysis, graphs, and metrics; common in safety-critical, defense, and embedded markets, often air-gapped and tool-qualified.
- **Engine / protocol layer** — index formats and SDKs that define how code intelligence is computed and exchanged, consumed by platforms and custom clients rather than used directly.
- **Quality-extended analysis** — structural understanding bundled with metrics, dependency-rule enforcement, and standards checking; the seam toward code quality tools.
- **AI-augmented understanding** — natural-language chat and answers layered over the semantic model; an emerging capability in several products, not a change of Type.
- **Compliance packaging** — tool qualification and standards certification for regulated development; a market-segment extension, not structural.

A variant remains a variant unless it changes the core: if the primary surface stops being resolved navigation over a semantic model — for example, it becomes pattern matching over text (code search), rule judgment (static analysis), or quality gating (code quality) — it has become a different Application Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Code Search Platform | neighboring specialist, often co-shipped | search finds code by content and structure and returns located matches; code intelligence resolves meaning — which occurrence is the definition, what genuinely references it. Products ship both; the seam is the primary surface. |
| IDE / Code Editor | adjacent, authoring-side | the IDE applies the same language intelligence in service of editing, bound to a local project; the platform serves understanding of a whole corpus to readers. Editors and IDEs act as clients of intelligence platforms. |
| Static Code Analysis Platform | shared infrastructure, different surface | both parse code deeply; static analysis judges code against rule catalogs and reports findings; code intelligence maps structure and answers meaning questions. Analysis may ship as a module inside an intelligence product. |
| Code Quality Platform | downstream consumer | quality platforms hold quality state and verdicts on changes; behavioral-analysis tools (hotspots, change coupling) belong to that territory even when marketed with intelligence-adjacent language. |
| Software Architecture Modeling | derived vs authored | architecture modeling holds authored models of intended structure as the source of truth; code intelligence derives actual structure from the code itself. |
| Application Modernization Platform | consumer of understanding | modernization platforms use dependency and complexity understanding as input to a transformation program; they do not serve day-to-day code navigation. |
| Developer Documentation Portal | generated vs authored | documentation portals publish authored corpora; hover docs and cross-reference pages derived from the parse are generated views over the code model. |
| AI Coding Assistant | adjacent AI layer | assistants suggest and generate inside the coding flow; AI chat over a semantic model is an AI layer on the understanding surface, not a new Type. |
| Source Code Hosting Platform | embedding host | hosting platforms store and serve repositories and host collaboration; code navigation is one capability they may embed, as they may embed search. |

The most important boundary is with Code Search Platform, because the two are frequently one product. The structural test is the primary surface: a product whose center of gravity is *query and match* is code search; a product whose center of gravity is *resolve and navigate* is code intelligence. The second boundary is with the IDE: the same intelligence exists on both sides, but authoring-primary with a project scope is the IDE, and understanding-primary with a corpus scope is this Type.

## Representative Products

- **Sourcegraph** — the platform pole: a self-described code intelligence platform providing layered navigation (heuristic search-based resolution out of the box, compiler-grade precise navigation via uploaded or auto-generated indexes) across an organization's repositories and dependencies, served through web UI, code host and review-tool integrations, and API.
- **GitHub code navigation** — the hosting-platform-embedded pole: automatic, zero-configuration definition/reference navigation and a symbols pane on hosted repositories, computed from parser-derived name binding.
- **SciTools Understand** — the desktop deep-analysis pole: a per-project static-analysis and code-comprehension tool building a cross-referenced entity/reference database, with entity detail views, graph catalogs, dependency matrices, and metrics; the standard-bearer in safety-critical and legacy-code markets.
- **Sourcetrail** — the historical open-source pole (archived 2021): a free, offline, cross-platform source explorer indexing a project (Clang-based for C/C++) and presenting it as an interactive graph for getting productive on unfamiliar code — evidence that the Type's core predates the current platform wave.

The behavioral-analysis pole (e.g. CodeScene) was examined during research and sits outside this Type: its analyses are quality- and process-oriented rather than symbol-level semantic resolution, and it is classified with the code quality territory.

## Sources

Research date: **2026-09-10**

- Sourcegraph Docs — Code Intelligence (overview), Precise code intelligence, Search-based code intelligence — https://3.39.sourcegraph.com/code_intelligence , https://3.39.sourcegraph.com/code_intelligence/explanations/precise_code_intelligence , https://3.39.sourcegraph.com/code_intelligence/explanations/search_based_code_intelligence
- SCIP Code Intelligence Protocol — https://github.com/sourcegraph/scip
- Sourcegraph Blog — Precise Code Intelligence for Java, Scala, and Kotlin; Announcing SCIP — https://sourcegraph.com/blog/java-scala-kotlin-code-intelligence , https://sourcegraph.com/blog/announcing-scip
- GitHub Docs — Navigating code on GitHub — https://docs.github.com/en/repositories/working-with-files/using-files/navigating-code-on-github
- GitHub — code-navigation public documentation repository — https://github.com/github/code-navigation
- GitHub Blog — Introducing stack graphs — https://github.blog/open-source/introducing-stack-graphs
- SciTools — What is Understand; Read the Information Browser — https://ai-docs.scitools.com/help/getting-started/what-is-understand.html , https://ai-docs.scitools.com/help/explore/information-browser.html
- SciTools — Understand product and features pages; documentation root — https://scitools.com/ , https://scitools.com/features.html , https://docs.scitools.com/
- Sourcetrail — README (archived repository) — https://github.com/CoatiSoftware/Sourcetrail
- CodeScene — product site (boundary probe) — https://codescene.com/

> Sourcing limitation: the current Sourcegraph documentation site returned access errors (HTTP 403) during research, consistent with the limitation recorded by the code-search research pass. Sourcegraph claims in this document are therefore calibrated to the fetchable legacy documentation mirror and the open-source SCIP protocol repository; no claims are made about Sourcegraph features documented only in the unreachable current docs. Product-specific operational limits (repository-size caps, branch-coverage rules, index-retention defaults) are recorded in the Research Notes and deliberately not asserted here as category-wide rules.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical-sample check are recorded in the paired Research Notes.
