# Software Localization Management

## Overview

A **Software Localization Management** application is the software team's system for producing and maintaining translations of the product's own user-facing text. The product's strings — button labels, menu items, messages, errors, store listings — are held as an identified corpus of source strings with one translation per target language; translation work is produced and tracked string by string, language by language, through review states; and the corpus is kept in step with the product as it changes: new and modified strings flow in from development, and finished translations flow back out in a form the build can consume.

The defining core is small and jointly held:

```text
The product's string corpus of record
└── The translation production loop over that corpus
    └── The two-way flow with the software's development
```

Everything else commonly associated with the category — key naming schemes, Git integration, task boards, machine translation, AI assistance, crowdsourcing, over-the-air delivery — is standard or optional capability layered on this core, and varies by product, team, and era. Older file-passing workflows, open-source community projects, and no-file website configurations all satisfy the same definition without any of the modern specifics.

When the subject stops being the software's own strings bound to a development flow and becomes self-contained translation deliverables (documents, marketing content) managed as one-off projects, the product is drifting toward translation-management territory — a boundary the market itself maintains.

## Users & Context

The primary users form a production chain around one shared corpus:

- **Developers** — introduce and change the source strings in the course of building the product; they consume translations back into the build. They typically touch the system through files, APIs, CLIs, or repository integrations rather than the translation editor.
- **Localization managers** — own the operation: set up projects and target languages, invite and organize translators and reviewers, package work, track progress and cost, and keep the flow between development and translation running.
- **Translators** — produce translations for their languages, working string by string with the context the system provides (source text, screenshots, glossary, translation-memory and machine-translation suggestions).
- **Reviewers / proofreaders** — check and approve translations; in mature setups they hold a distinct permission, and approved strings become editable only by them.

The work context is continuous software development: strings change with every feature, so translation runs in parallel with development rather than as a final packaging step before release. Community volunteers translating open-source projects, in-house language teams, freelance translators, and external agencies all work in the same system, in different mixes depending on the organization.

## Core Model

### The string corpus of record

The center of the system is a persistent corpus of the product's translatable text, organized as **source strings × languages**:

- A **source string** is one unit of user-facing text, identified so that the product's code can reference it and the system can track it across languages. Two identification styles exist in the market: an explicit **key** — a stable code name that points to the text (the dominant style for modern web and mobile formats) — and the **source text itself** as the identifier (the style of classic bilingual formats extracted from code). What is invariant is that each string is individually identified and addressable; the key mechanism is an implementation.
- Each string carries **context** for translators: descriptions, screenshots of where the text appears, labels or tags grouping related strings, maximum lengths, and plural forms where the language requires them.
- Each string holds **one translation per target language (locale)**. The **source language is the master**: target translations are produced from it, and a change to the source text is the event that drives re-translation.
- Strings are organized in **projects** (one product or product line), commonly subdivided by file, component, or platform so that the corpus mirrors how the product's text is actually stored and shipped.

### The translation production loop

Around the corpus runs a tracked production loop. Each string's translation in each language carries a **state**, and the states form a progression:

```text
Untranslated → Translated → Reviewed / Approved
              ↘ flagged stale when the source changes
```

- Exact state labels vary by product (verified, reviewed, approved, needs-editing, fuzzy); what is structural is that the system distinguishes *not yet translated*, *translated but not checked*, and *checked/accepted*, and that acceptance is permission-gated — reviewing is a distinct role's act, not just another edit.
- **Work is assigned**: managers package string scopes × languages into tasks or jobs with assignees and due dates, or rely on standing per-language teams. Some products make the work package a first-class object with its own lifecycle; others achieve the same through states and access control.
- **Quality machinery feeds the act of translating**: translation memory (reusing prior translations for identical or similar text), glossaries/termbases (approved terms highlighted in the source), machine translation and AI suggestions, automated QA checks (missing placeholders, length, terminology, consistency), and context aids (screenshots, in-product preview).
- **Consistency machinery keeps the corpus coherent**: identical strings can be linked or propagated so a translation made once is reused everywhere the string appears, including across branches and components.

### The two-way flow with development

The corpus is bound to the product's source of truth and kept in step with it:

- **Inbound**: strings enter from the development side — file upload, API, CLI, repository synchronization (the system pulls the repo, parses the localization files, and updates its database), design-tool plugins, or in-product SDKs/JavaScript for surfaces without files.
- **Outbound**: finished translations leave in build-consumable form — downloaded files in the product's formats, commits or pull requests back to the repository, API/CLI retrieval wired into the build, or over-the-air delivery to running apps.
- **Staleness propagation**: when a source string changes, its existing translations are flagged as needing attention (some products do this automatically; others surface it through filters and checks). The corpus is thus a living mirror of the product's text, not a snapshot.
- **Versioning**: development branches can be mirrored as localization branches so feature work is translated in parallel; translations follow the branch structure and are merged back with the code.

### One structure, many implementations

```text
Concept:            identified source string
Implementations:    explicit key (modern web/mobile formats) · source text as identifier
                    (classic bilingual formats extracted from code)

Concept:            inbound flow
Implementations:    file upload · API/CLI · repository sync · design-tool plugins ·
                    in-product SDK / JavaScript snippet

Concept:            outbound flow
Implementations:    file download · repository commits / pull requests · API/CLI build
                    integration · over-the-air delivery to running apps

Concept:            work packaging
Implementations:    first-class tasks/jobs with lifecycles · per-language teams ·
                    states + access control alone
```

## How It Works

### The continuous loop

The typical operating rhythm of the system:

```text
Developers change the product's text
→ new/changed strings flow in (repo sync, upload, API)
→ the corpus updates; affected translations are flagged stale
→ managers package the pending work (or standing teams pick it up)
→ translators produce translations with TM/MT/glossary/context support
→ reviewers check and approve
→ approved translations flow out (download, commits/PRs, API, OTA)
→ the build or the running product picks them up
```

The loop never finishes: as long as the product develops, strings keep arriving, and translation keeps running in parallel. Progress is visible per language and per file/component, so the team can see what is untranslated, what is awaiting review, and what is ready for the build.

### Setting up a localization project

```text
Create the project and its source language
→ add target languages
→ connect the source of strings (upload files, connect the repository,
  install the CLI/API, or embed the SDK/JS)
→ invite translators and reviewers, scoped to their languages
→ configure quality machinery (TM, glossary, MT/AI, QA checks)
→ establish the outbound path (download, repo PRs, build integration)
```

The source language is normally fixed for the project's life; target languages can grow over time.

### Producing a translation

```text
Open the translation editor (filtered to pending work)
→ read the source string with its context (screenshot, description, glossary hits)
→ consult suggestions (translation memory, machine translation, AI)
→ write the translation, respecting placeholders, plurals, and length limits
→ save (state: translated)
→ reviewer approves (state: reviewed/approved) — or rejects back with a comment
```

Translators work string by string; the editor surfaces only their languages and, in stricter setups, only the strings assigned to them.

### Handling change

```text
Source string edited or added in development
→ corpus updated on the next inbound sync
→ existing translations of that string flagged stale (or re-opened)
→ translators update them; reviewers re-approve
→ updated translations flow out on the next outbound sync
```

Branch-based development extends the same pattern: a feature branch's strings are translated in a parallel localization branch and merged back with the code, with duplicate strings across branches translated once and inherited.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Project dashboard / progress view

The manager's entry surface.

- per-language and per-file/component completion, activity, pending work
- primary actions: configure languages and integrations, package work, generate reports

### String list / translation editor

The translator's and reviewer's primary workspace.

- source strings with identifiers, context, screenshots, labels, states; target-language fields with suggestions alongside
- primary actions: translate, edit, comment, report an issue, approve/reject, filter by state/label/language

### Task / job view

The work-packaging surface (where the product offers one).

- work packages with scope, languages, assignees, due dates, progress
- primary actions: create from filters, assign, split scope, track completion

### Resource views

The quality machinery's surfaces.

- translation memory search, glossary/termbase management, QA-check results, style guides
- primary actions: search/reuse matches, maintain terms, resolve flagged issues

### Integration & configuration surfaces

The developer- and admin-facing surfaces.

- repository connections, API/CLI credentials, file-format and export settings, webhooks, roles and per-language permissions
- primary actions: connect a source, configure export, manage members and access

### Reports

- progress, word counts, translation costs, contributor activity — the operational and budgeting view of the localization effort

## Important Rules / Behaviors

### The source language is the master

Translations are produced from the source strings; the source text is not translated into itself. Changing the source is the event that invalidates dependent translations — mature products flag them automatically rather than silently shipping outdated text.

### Review is a distinct, permission-gated act

In mature configurations, translators and reviewers are separate roles: an approved translation can no longer be changed by translators (who may only suggest), and only reviewers can edit or un-approve it. Access is commonly scoped per language, and in stricter setups even per assigned task — a translator sees their languages, or their tasks, and reads the rest.

### String identity is load-bearing

The link between a string's identifier and its translations is what keeps the corpus coherent. Renaming a key or changing source text carelessly can break the linkage and orphan translations; some products guard this explicitly (for example, requiring deletion in both the platform and the repository before a key disappears, or warning against editing strings while their translation job is in progress).

### Placeholders and structure must survive translation

Strings routinely contain variables, markup, and plural machinery that must be preserved verbatim and adapted to the target language's grammar. The system highlights them, checks them, and blocks or warns on violations — a translation that destroys a placeholder breaks the product at runtime.

### The corpus serves two consumers

Translations must satisfy translators (meaning, tone, terminology) and the build (exact identifiers, formats, escaping). The outbound path is therefore format-faithful: the system reassembles translations into the product's own localization files, not a generic interchange format.

### Not everything should be translated

Technical strings (format patterns, configuration values, placeholders-only strings) are routinely hidden or excluded from the translation surface so translators never see them; some products also let whole keys be blocked from management entirely.

## Variants

Common shapes of the same Type:

- **File-based / repository-centered** — the corpus mirrors localization files in the version-control system; strings flow through repo sync and return as commits or pull requests. The open-source, self-hosted pole of the market lives here.
- **Key-based SaaS platform** — explicit keys with per-platform routing (web/iOS/Android), API/CLI-first integration, and rich work packaging; the dominant commercial shape.
- **No-file ingestion** — websites translated through a JavaScript snippet or apps through an SDK, with the system holding the strings directly rather than exchanging files.
- **Community/crowdsourced** — public projects where volunteer translators join per language, often with suggestion-and-vote mechanics and professional review on top.
- **Agency/marketplace-connected** — professional translation ordered from inside the system; untranslated content is forwarded to a vendor and completed translations return into the corpus.
- **AI-forward** — machine translation and AI move from suggestion to producer: AI-assigned translation tasks, AI quality evaluation and scoring, with humans reviewing.
- **Content-type extensions** — the same corpus machinery applied to docs, marketing content, store listings, or subtitles, sometimes as separate project types.

A variant remains a variant unless it changes the core: a product that loses the string corpus, the state-tracked production loop, or the development binding has left the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Translation Management (document/enterprise TMS — no directory leaf) | nearest neighbor | manages self-contained translation deliverables (documents, marketing content) as projects for a translation operation; this Type manages the software's own strings bound to the development flow with build-consumable output. Vendors themselves split the two product families |
| Version Control System / Source Code Hosting | substrate | holds the code and the localization files; this Type adds the translation production layer (states, roles, quality machinery) on top of them |
| Continuous Integration Platform | downstream consumer | receives translations via CLI/API/commits and builds with them; it does not track translation work or own the corpus |
| Content Management System / Headless CMS | adjacent | localizes content entries for publishing surfaces; this Type localizes software strings for builds. CMS content imported as strings is an extension, not the center |
| Product Information Management | adjacent | localizes commerce product content for selling channels; different subject and consumer |
| Developer Documentation Portal | adjacent | publishes a reader-facing documentation corpus; this Type's corpus is consumed by the build (docs localization is a supported content type inside it) |
| Dictionary Application | terminology adjacency | glossaries/termbases here are production-consistency machinery for translators, not a consumer word reference |
| AI / machine translation tools | capability | MT/AI is a producer of suggestions and drafts inside the loop; a standalone generator has no corpus of record, no state tracking, no development binding |

The sharpest seam is with document-oriented translation management: both produce translations with TM/MT/glossary machinery, but only this Type's corpus is the software's own strings, continuously synchronized with development and reassembled into the build.

## Representative Products

- Crowdin — developer-centric SaaS around "agile localization"; VCS integrations, version branches, vendor marketplace, in-context editing
- Lokalise — developer and product-team SaaS; keys-and-platforms model, task chains, AI translation and quality scoring
- Phrase (Strings) — enterprise platform; the vendor maintains a separate document-TMS product family, making the Type boundary visible in one company's catalog
- Transifex — continuous-localization SaaS with community-translation heritage; file-based and no-file (JavaScript/SDK) ingestion poles
- Weblate — open-source, git-native, self-hostable continuous localization; the gettext/repository heritage documented end to end

The core model was checked against the older file-passing generation (gettext-style bilingual files extracted from code, offline translation, commits back to the repository) and against open-source community and no-file configurations, to avoid defining the Type by the current SaaS generation's specifics.

## Sources

Research date: **2026-09-09**

- Crowdin Docs (help center) — Introduction, Translation Strategies, String Management, Version Management, Project Tasks: https://support.crowdin.com/
- Lokalise Help Center — Keys and platforms, Translate and collaborate collection, Translation Statuses: https://docs.lokalise.com/
- Phrase Help Center — Phrase Strings category, Keys (Strings), Jobs (Strings): https://support.phrase.com/
- Transifex Help Center — Getting started as a translator, Creating a Project, Translations: https://help.transifex.com/
- Weblate Documentation — Weblate basics, Continuous localization, Translation workflows: https://docs.weblate.org/

> Sourcing note: official help-center and documentation pages for all five sampled products were directly accessible. Some referenced articles (Transifex workflow/state details, Phrase review-workflow and branching mechanics, Lokalise delivery mechanics) were not opened; claims about those aspects are kept general, and no precise numeric limits or defaults from any product appear in this document. Detailed observations, the cross-product comparison matrix, and the abstraction analysis are recorded in the paired Research Notes.
