# Research Notes — Software Localization Management

Research date: 2026-09-09
Leaf: Software Localization Management (§12 Software Development & Product Engineering)
Slug: software-localization-management

## Research Goal

Understand what a Software Localization Management application is as an Application Type: what its core objects are (strings, keys, locales, translations), how translation work is produced and tracked, how the system stays in step with ongoing software development, who the users are, and where the boundary lies with neighboring Types (translation management for documents, version control, CI, CMS localization, PIM, terminology tools).

## Initial Boundary

Initial hypothesis: this is the software team's system for managing translation of the product's own user-facing text into many languages — a continuous engineering-adjacent workflow, not a one-off translation project. Nearest conceptual neighbors:

- Translation Management System (TMS) — the translation industry's project system for documents/content; no directory leaf exists for it, but vendors themselves draw the line (Phrase TMS vs Phrase Strings).
- Version Control System / Source Code Hosting — strings files live in repos; this Type adds a translation production layer.
- Continuous Integration Platform — delivery of translations into builds is a handoff, not CI.
- CMS / Headless CMS localization — content entries for publishing surfaces vs software strings for builds.
- Product Information Management — commerce content localization, different subject.
- Dictionary Application — term bases inside this Type are production machinery, not consumer word reference (boundary note recorded by the dictionary-application pass).

## Research Questions

1. What is the unit of record? (string/key, locale, translation)
2. How do strings enter the system and how do translations leave it?
3. What states does a translation carry and how does work get assigned?
4. What quality machinery exists (TM, MT/AI, glossary, QA checks, context)?
5. How is the corpus kept in step with a changing product (staleness, branching, versioning)?
6. Who uses it and what roles exist?
7. Where is the boundary vs document-translation management (TMS)?

## Representative Products

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Crowdin | developer-centric SaaS, "agile localization", VCS + app-store ecosystem | market representative, rich help center |
| Lokalise | developer + product-team SaaS, keys/platforms model, AI-heavy current generation | different packaging (Vantage vs Expert), mobile heritage |
| Phrase (Strings) | enterprise platform; vendor itself splits TMS vs Strings | boundary evidence from the vendor's own product family |
| Transifex | continuous-localization SaaS with community-translation heritage; Live/Native no-file poles | different ingestion philosophy |
| Weblate | open-source, git-native, self-hosted pole | deployment + philosophy contrast; gettext heritage documented |

## Sources

All fetched 2026-09-09. Evidence layer A (directly observed) unless noted.

- Crowdin Docs (help center): Introduction, Translation Strategies, String Management, Version Management, Project Tasks — https://support.crowdin.com/
- Lokalise Help Center: Keys and files collection, Keys and platforms, Translate and collaborate collection, Translation Statuses article — https://docs.lokalise.com/
- Phrase Help Center: Phrase Strings category, Keys (Strings), Jobs (Strings) — https://support.phrase.com/
- Transifex Help Center: Getting started as a translator, Creating a Project, Translations — https://help.transifex.com/
- Weblate Documentation: Weblate basics, Continuous localization, Translation workflows — https://docs.weblate.org/

Not fetched (kept out of precise claims): Phrase "Review Workflow (Strings)" and "Branching (Strings)" articles (referenced but not opened); Transifex "Project Workflows" and state-model articles; Lokalise OTA/CLI detail pages; Smartling (not sampled).

## Product Observations

### Crowdin (Layer A)

- Self-definition: "localization management solution for agile teams"; "agile localization" = frequently updated content, translators work in parallel with development, latest content available to translators "nearly instantly", finished translations received back "via integrations and other automation tools"; tracking "which content has been updated, requires translation, or is ready for production".
- Project types: file-based vs string-based (both documented throughout).
- Sources: uploading source files; string management — string text + identifier ("unique key for the string, often used for referencing the translated text in the application") + context + labels + max translation length + plurals; hidden strings (not translated, e.g. placeholders/technical entities); find & replace across source strings.
- Version management: version branches mirror VCS branches; created via VCS integration, UI, API, CLI; protected branches (string-based) block direct content modification — update via clone → work → merge; merge summary with selective change acceptance (added/changed/deleted/conflicted strings, translation changes, approvals); duplicates handling ("Show within a version branch" — master strings translated once, duplicates inherit).
- Translation strategies: invite own translators/proofreaders (roles: manager, translator, proofreader, language coordinator; per-language access); order professional translations (Vendors Store; "Translate by vendor"/"Proofread by vendor" tasks; API-integrated agencies forward untranslated data and upload translations back); Crowdin AI (auto-translate + in-editor suggestions); MT engines (Google, Microsoft, DeepL, Amazon; auto-translation or suggestions); crowdsourcing (community suggests multiple translations and votes).
- Quality machinery: TM (project-based + global), QA checks (missed commas, extra spaces, typos), screenshots (appear under each string), In-Context visual editor (overlay on the web app), glossary (terms + definitions + approved translations, highlighted in source), style guides, custom variables (placeholders highlighted, not translated), RTL support, length control.
- Online editor: filtering (issues/comments/screenshots/visibility/labels), comments and issues per string, search & replace, preview for 40+ file formats.
- Integrations: VCS (GitHub/GitLab/Bitbucket/Azure Repos — sync source, receive translations as pull/merge requests), CDN distributions (mobile SDK delivers new translations to apps), CLI (CI servers, Git/SVN/Mercurial), API, branches, Figma/Sketch/XD plugins, Google Play (store page content), Jira (issues become sub-tasks), Slack, webhooks, 700+ apps store.
- Tasks: types Translate/Proofread × own translators/vendors; per-language task creation (separate task per language); content splitting between assignees by word count; cost estimates and rates templates (estimated/actual cost reports); sequential tasks (translation task → pending proofreading task that activates on completion); task-based access control (read-only outside assigned tasks); task scope tracking (original vs current scope as source strings change).
- Reports: project reports, contributor reports, cost calculation for paying translators/proofreaders.

### Lokalise (Layer A)

- Keys: "placeholders within the source code of any application — website, mobile app, game, or desktop app... substituted with the appropriate translation values based on the user's chosen language setting"; a key is "an identifier for translations in all languages of a project" (one key → one translation per language); key name + base-language value + platforms + tags + plurals + character limits + custom attributes.
- Platforms: Web / Android / iOS / Other — "global tags for the keys" that route export (a key assigned to iOS+Android exports into .strings and .xml but not web .json); per-platform key names option; same key shared across platforms reduces translation work.
- Project types: "Web and mobile" (classic keyed formats), "Ad hoc documents" (DOCX/HTML/IDML — keys only temporarily represent content, reassembled on export), "Marketing and support" (content imported from third-party services: Contentful, Iterable, Marketo — underlying structure controlled by the third party).
- Key advanced features: key referencing/linking ("link one key to another at the translation level, so you never have to translate the same strings twice"), duplicate handling (key linking and merging), bulk actions, filters, hidden keys (invisible to contributors), archived keys (excluded from statistics/export/search).
- Translation editor: multilingual and bilingual views, MT and TM suggestions, universal placeholders ("internal placeholders automatically converted to those required by your file format"), HTML/placeholder blocks, spelling/grammar check in 20+ languages.
- Statuses (documented article): untranslated (empty) / translated (filled); verified / unverified — **changing the base language automatically marks target translations unverified** ("Lokalise assumes that translations in other languages might also need updating... a quality control step"); reviewed / not reviewed (permission-gated, requires Reviewing feature enabled; reviewing implies verified); completed / not completed (task-scoped); custom statuses (project-configurable).
- Tasks: assign translation and review tasks to contributors or AI; incoming task widget; chained tasks for multiple revision cycles; vendor rate profiles (rates by TM leverage and languages).
- AI features: AI translation tasks (assign to AI), AI suggestions, AI LQA (quality evaluation), MQM-standard quality scoring, custom AI profiles (RAG over past translations), MCP server.
- Professional translations: order from providers.
- Collaboration: comments with @mentions per key, project activity timeline, review center (guest reviewers without full license), statistics (words, keys, progress).
- Analytics: usage dashboard (processed words, translation methods, OTA activity, TM leverage), tasks dashboard, translation-quality dashboard.
- In-context: LiveJS web in-context editor.
- Files: 30+ formats (Android XML, Apple strings/stringsdict/xcstrings, ARB, CSV, DOCX, Excel, gettext PO, HTML, IDML, Java properties, JSON flat/nested/structured, .NET resx, PHP, Qt TS, React Native, Salesforce, SRT, YAML, XLIFF, Xcode XCLOC...); upload/download with filename customization; translation alignment (build TM from existing base+target pairs).

### Phrase Strings (Layer A)

- Vendor family boundary (help-center home): "Phrase TMS — The translation management system for enterprise localization" vs "Phrase Strings — A better localization solution for your product copy" (plus Studio, Portal, Orchestrator). The vendor itself separates document/enterprise TMS from software-strings localization.
- Keys: "used to identify translatable text strings within software code... A key can have multiple translations associated with it, each corresponding to a different language locale of the project. The function is similar to that of the primary key in relational databases with the translations being an attribute of the key. Keys are stored in resource files"; "The use of keys allows localization management platforms to present translatable text to translators without having to present code."
- Key types by file format (string default, array, boolean, markdown, number); naming strategies (descriptive recommended; source-string-as-key "not recommended" — "if the original text changes, it breaks the relationship with the translations"); blocked keys (regex; omit config/date-format keys from management entirely); excluded keys per language (uploaded but ignored — excluded from export and reports); linked keys across projects (consistency automation); duplicate keys.
- Structure: Spaces → Projects → Keys; Jobs tab; CLI; API; integrations (GitHub, GitLab, Contentful, Jira, Sketch, WordPress, ...).
- Jobs: "A job represents a file for translation into a specified target language(s)"; work package over keys × languages with owner, due date, briefing, ticket URL; statuses Draft → In progress → Completed (auto-complete option when all workflow steps finish across target languages; reopen possible); warning not to modify key content while a job is in progress; job templates; **job automations** (rules + triggers — Import or Schedule/cron — that identify translation-ready keys by status/tag and create+start jobs automatically; per-automation exclusion of keys already in its own jobs); job annotations (key-value metadata for integrations).
- Referenced-but-not-opened: Review Workflow (Strings) steps; pre-translation (project-level, triggered by new uploads/keys/languages); Branching (branch projects).
- Deletion semantics: "When working with repositories (GitHub, GitLab, etc.) and deleting keys, the keys must be deleted from both Phrase and the repository to be permanently deleted" — two-sided deletion guard.
- Limits (L3, research-notes only): 10,000-key selection cap per job; unmentioned-key handling above 10,000 keys per project; automation limits.

### Transifex (Layer A)

- Structure: organization → projects → teams; "Teams are made of Translators, Reviewers, and Coordinators, grouped by the language they work on"; join requests approved by maintainers/managers; private projects invite-only.
- Project types: file-based (traditional localization files such as .PO and XLIFF) vs Live ("JavaScript-based technology translating websites without files") vs Native (SDK solution).
- Source language fixed at project creation; target languages changeable later.
- Staffing methods (documented "Translations" article): in-house/freelance translators+reviewers invited to teams; community (public projects with join requests, or private invites); LSPs/agencies (work offline pushing/pulling files, or in-platform using TM/glossary/communication); "mix and match" (community translates, professionals review; different vendors per project).
- Ordering: order wizard with translation partners; vendor-locale constraints (source must be English for vendor orders; target locales must match vendor support).
- Referenced-but-not-opened: Project Workflows; TM setup; glossaries; TQI (Translation Quality Index); Transifex AI; agentic capabilities collection.

### Weblate (Layer A)

- Self-definition: "libre software web-based continuous localization system"; deployed self-hosted (Docker/Debian/Kubernetes/...) or as Hosted Weblate cloud.
- Structure: projects → components ("The component corresponds to one translatable file") → translations per language; categories nest components; **translation propagation** — common strings propagate across components within a project by default (key match required for monolingual formats).
- Continuous localization loop (documented 6-step process): 1. developers push changes to VCS → 2. translation files updated (extraction) → 3. Weblate pulls, parses translation files, updates its database → 4. translators submit translations via web interface or upload offline changes → 5. Weblate commits changes to local repository (lazy commits, grouped by author) → 6. changes pushed back to upstream repository. Local-files mode possible without upstream hosting.
- Repository machinery: webhooks/notification hooks, merge styles (merge/rebase), lock/unlock for outside edits, reset-and-reapply recovery, repository maintenance operations (commit/push/update/synchronize/rescan/cleanup/remove obsolete), protected-branch pull-request flows, add-ons (auto-translation, cleanup, commit squashing).
- Translation states (documented list): Untranslated / Needs editing (fuzzy) / Needs rewriting ("translation needs to be rewritten because of a source string change") / Needs checking / Translated ("Waiting for review" when reviews enabled) / Approved (review-gated; translators can only suggest) / Read-only / Suggestions (stored in Weblate only, not in files). States represented in translation files where the format supports it; translation quality filter decides which states are committed.
- Workflows (documented configurations): direct translation (default, anyone edits); peer review (suggestion voting + auto-accept threshold); dedicated reviewers (translator/reviewer split; reviewers edit approved strings); MT/LLM workflows (human-assisted; service translation with human editing; service suggestions with human acceptance; service translation with review + quality gateway committing only approved translations).
- Quality machinery: checks and fixups, glossary, translation memory, automatic suggestions (MT engines and LLM services), source-string reviews, intermediate language file (quality gateway polishing source before translation), secondary language, per-language workflow customization, language-scoped teams.
- Attribution: translations committed to VCS authored with translator name/email (privacy option available).
- File formats: 50+ documented (gettext PO, Android, iOS, JSON family, YAML, XLIFF 1.2/2.0, RESX, Qt TS, Fluent, subtitles, ...); bilingual (source extracted from code) vs monolingual (keyed) format distinction documented.

## Cross-product Comparison

| Aspect | Crowdin | Lokalise | Phrase Strings | Transifex | Weblate |
|---|---|---|---|---|---|
| Unit of record | string (text + identifier + context) in project | key (per-platform) in project | key in project (spaces) | string in project | string in component (file-bound) |
| Locale model | target languages per project | languages per project, base language | locales per project, default language | source (fixed) + target languages | translations per language per component |
| In-flow | upload/API/CLI/VCS sync/Figma/Google Play | upload/API/CLI/apps | CLI/API/repo sync/Contentful | upload/API/CLI/Live JS/Native SDK | VCS pull (git-native), webhooks |
| Out-flow | download/bundles/VCS PRs/CDN-SDK/CLI/API | download/CLI/API/OTA | download/CLI/API/repo sync | download/API/CLI/Live/Native | VCS push/PR, lazy commits |
| Translation states | translated + approved (proofread) + hidden | translated/verified/reviewed/completed/custom | untranslated/unverified/ready-for-review + workflow steps | (not directly observed) | untranslated/needs-editing/needs-rewriting/translated/approved/read-only |
| Work packaging | tasks (per language, sequential, vendor, cost) | tasks (chained, AI assignees) | jobs (keys × languages, automations) | teams by language + orders | none first-class (states + access control) |
| Quality machinery | TM, glossary, QA checks, style guides, screenshots, in-context, MT, AI | TM, glossary, MT, AI LQA/MQM, screenshots, spell check | TM, glossary, pre-translation, review workflow | TM, glossary, TQI, AI | TM, glossary, checks/fixups, MT/LLM, source reviews |
| Staffing | own team, vendor store, crowdsourcing, language services | own team, translation orders, AI | own team (+ TMS-side services) | own team, community, agencies, order wizard | own team, community |
| Dev sync | VCS integrations, branches, protected branches | GitHub/GitLab apps, CLI, API | repo sync, branching, CLI | GitHub integration, Live, Native | git-native pull/push/PR |
| Deployment | SaaS + Enterprise private | SaaS | SaaS | SaaS | self-hosted OSS + hosted cloud |

### Cross-product commonalities (Layer B)

1. Every product holds a persistent corpus of the software's translatable text organized as source strings (identified by key or by source text) × languages/locales, with the source language as master.
2. Every product tracks translation work per string per locale through states (some form of untranslated → translated → reviewed/approved), with per-language or per-role permission gating on who may translate vs review.
3. Every product has a two-way flow with the software's development: strings in (file upload, API, CLI, VCS sync, or in-product SDK/JS) and translations out (download, API/CLI, VCS commits/PRs, OTA/CDN).
4. Every product carries quality machinery: translation memory, glossary/termbase, MT (now commonly AI), context aids (screenshots, in-context preview, comments).
5. Every product supports plural forms and placeholder/variable protection in some form.
6. Every product has roles separating management, translation, and review, scoped per language in mature products.
7. Every product surfaces progress (per language, per file/component) and commonly cost/word reporting.

### Divergences (implementation, not Type)

- Keyed (monolingual) vs keyless (bilingual, source-text-identified) corpora — Weblate documents both; Crowdin has file-based vs string-based projects.
- Work packaging: first-class task/job objects (Crowdin, Lokalise, Phrase) vs state+access-control-only (Weblate).
- Ingestion philosophy: files/API (most), git-native (Weblate), no-file JS/SDK (Transifex Live/Native).
- Deployment: SaaS-only vs self-hostable OSS.
- Community/crowdsourcing first-class vs private-team-only.
- AI depth: from plain MT suggestions to AI assignees, LQA, MQM scoring, MCP servers.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The product's string corpus of record** — the software's user-facing text held as persistent identified source strings (by key or by source text, with context) each carrying per-locale translations; the source language is the master. Remove → a translation spreadsheet/database or plain file storage.
2. **The translation production loop over that corpus** — work tracked per string per locale through states (untranslated → translated → reviewed/approved), with translators/reviewers assigned under role/language-scoped access and quality machinery (TM, MT/AI, glossary, context) feeding the act of translating. Remove → a static string store, or a generic task tracker.
3. **The two-way flow with the software's development** — strings flow in from the product's source of truth (files/API/CLI/VCS/in-product SDK) and finished translations flow back out in build-consumable form, with source changes propagating staleness to dependent translations. Remove → a one-off translation project tool (document-TMS posture), or a file-conversion utility.

Jointly-held load-bearing:
- 1 alone = translation database/spreadsheet
- 2 without 1 = generic translation task tracker
- 3 without 1+2 = format conversion / CI step
- 1+2 without 3 = document-TMS posture applied to strings (batch projects, no development binding)
- 1+3 without 2 = a synchronized string mirror with no managed production

### L1 — Common Mature Structure

- Translation memory (project and global scopes)
- Glossary/termbase with approved translations
- MT engines, now commonly AI assistance (suggestions, auto-translation, quality evaluation)
- QA checks (placeholder/format/terminology/consistency classes)
- Context aids: screenshots attached to strings, in-context/visual preview, comments and issues per string
- Work packaging: tasks/jobs bundling string scopes × languages with assignees and due dates
- Roles: manager/admin, translator, reviewer/proofreader (+ coordinator/vendor), per-language scoping
- Progress and reporting: per-language/per-file completion, word counts, cost/rate machinery
- Plural forms, placeholder/variable protection, character limits, labels/tags, search/filter
- Translation history/versioning; key linking/propagation for consistency
- Integration fabric: API, CLI, webhooks, VCS connections, design-tool plugins, OTA/CDN delivery

### L2 — Variant / Optional Structure

- Project-type poles: file-based vs string-based/keyed vs keyless bilingual vs no-file JS/SDK website translation vs ad-hoc documents vs third-party-content (CMS/marketing) imports
- Ingestion/delivery philosophy: VCS-native vs API-first vs JS-snippet
- Staffing model: in-house only vs community/crowdsourcing vs agency/marketplace ordering vs AI assignees
- Deployment: multi-tenant SaaS vs self-hosted OSS vs enterprise private cloud
- Content-type extension beyond software UI: docs, marketing, store listings, subtitles
- AI depth: MT suggestions → AI auto-translation → AI quality evaluation/scoring → AI agents/MCP
- Branching/versioning models: VCS-mirrored branches, protected branches, branch projects
- Source-quality machinery: intermediate language gate, source-string reviews
- Pseudolocalization, style guides, offline translation, guest review surfaces

### L3 — Vendor-specific (research notes only)

- Crowdin: Vendors Store, Crowdin Language Services, Advisors, CDN Distributions, CroQL
- Lokalise: Vantage vs Expert split, Messages (Intercom/HubSpot/Drift), platforms model, universal placeholders, MCP server
- Phrase: TMS/Strings/Studio/Portal/Orchestrator family split, job automations with cron triggers, blocked/excluded keys, linked keys
- Transifex: Live (JS) and Native (SDK) no-file ingestion, TQI, agentic capabilities
- Weblate: add-ons framework, intermediate language file, lazy commits, translation propagation defaults, libre-software licensing posture

## Anti-overfitting Checks

- **"Key" terminology is NOT definitional**: gettext-style bilingual formats identify strings by source text, not keys (Weblate documents both monolingual keyed and bilingual keyless formats; Crowdin file-based projects are file+text identified). The invariant is an identified source string, however identified.
- **Git/VCS is NOT definitional**: upload/API poles (Crowdin file-based, Lokalise) and no-file poles (Transifex Live/Native) satisfy the Type without repo integration; Weblate's local-files mode runs without upstream hosting.
- **SaaS is NOT definitional**: Weblate self-hosted OSS pole.
- **MT/AI is NOT definitional**: human-only workflows documented (Weblate direct translation; Crowdin invite-your-team strategy); AI is era-current.
- **Crowdsourcing is NOT definitional**: private-team poles across the sample.
- **First-class task/job objects are NOT definitional**: Weblate runs the loop with states + access control only; the invariant is state-tracked production, not a task object.
- **Specific state names are NOT definitional**: verified/reviewed/approved/needs-editing/completed vary by product; the invariant is a tracked progression from not-translated toward reviewed/accepted.
- **Screenshots/in-context are NOT definitional**: common mature aids, absent in minimal configurations.
- **Cost/rate machinery is NOT definitional**: absent in Weblate's documented core.
- **Website/no-file ingestion is NOT definitional**: Transifex-only pole in-sample (variant).

## Historical / Market-Sample Check

- The gettext/VCS pattern documented by Weblate (bilingual files extracted from source code, msgmerge-style merging, offline translation, commits back to the repository) describes a generation that predates the current SaaS products; a minimal file-passing configuration (string tables in the repo + a coordinator tracking states + translations merged back before build) satisfies all three L0 legs with no modern machinery.
- The market's own vocabulary — "agile localization" (Crowdin), "continuous localization" (Weblate, Transifex) — names the modern generation's posture, not the Type's boundary: batch-mode file passing remains in-type.
- Desktop-era localization tooling (string extraction from resources, translation, re-integration into the build) is the same loop in an earlier form; held as conceptual lineage (not directly sampled — flagged in Uncertainties).
- Regional/open-source projects (Weblate pole, Transifex public projects) satisfy the core with community staffing and no commercial machinery.

Conclusion: the definition holds across older, regional, open-source, and platform-native configurations; no era-specific machinery enters L0.

## Boundary Findings

1. **vs Translation Management System (TMS)** — the sharpest seam, and the vendor sample draws it themselves: Phrase's help center separates "Phrase TMS — the translation management system for enterprise localization" from "Phrase Strings — a better localization solution for your product copy"; Lokalise similarly splits Vantage (long-form content) from Expert (keys). Seam: subject and binding — TMS manages self-contained translation deliverables/projects (documents, marketing content, CAT-editor workflows) for a translation operation; SLM manages the software's own strings bound to the development flow with build-consumable output. Remove the development-sync leg → TMS territory. No TMS leaf exists in the directory; recorded as a taxonomy observation, not resolved here.
2. **vs Version Control System / Source Code Hosting** — strings files live in repositories; this Type adds the translation production layer on top (Weblate is git-native yet its center is the translation workflow, states, and quality machinery, not code history). Remove the translation production loop → VCS territory.
3. **vs Continuous Integration Platform** — delivering translations into builds (CLI/API/OTA/PR) is a handoff to the build system, not build orchestration. Remove the corpus and loop, keep the delivery → CI/CD territory.
4. **vs CMS / Headless CMS** — CMS localization manages content entries for publishing surfaces; SLM manages software strings for builds. Blur zone: CMS content imported as strings (Lokalise "Marketing and support" project type; Phrase Contentful integration) — the SLM product treats external content as translatable string material, which is an extension, not the center.
5. **vs Product Information Management** — PIM localizes commerce product content for channels; different subject (product data vs software text) and different consumer (channels vs build).
6. **vs Developer Documentation Portal** — docs are a reader-facing corpus; SLM's corpus is consumed by the build. Docs localization is a supported content type inside SLM (Crowdin names docs among localized content), but the Type's center is the software's strings.
7. **vs Dictionary Application** — term bases/glossaries inside SLM are production-consistency machinery for translators (recorded from the dictionary-application pass's side); a dictionary is a consumer/professional word reference. Different users, objects, and surfaces.
8. **vs standalone AI/MT translation tools** — MT/AI is a capability inside the production loop here; a pure translation generator has no corpus of record, no state tracking, no development binding.

## Uncertainties

- Transifex's exact translation state model (translated/reviewed/proofread naming and gating) was not directly observed — Transifex claims in this document are limited to structure (org/project/teams), project types, staffing, and ordering.
- Phrase's review-workflow step mechanics and branching details were referenced but not opened; Phrase claims kept to keys/jobs/automations/deletion semantics.
- Lokalise OTA delivery existence is evidenced by the analytics dashboard's "OTA activity" wording; delivery mechanics not studied.
- Desktop-era localization tools (e.g., resource-compiler-based workflows) not directly sampled; the historical check rests on the documented gettext/VCS pattern plus structural reasoning.
- Whether the market would split "software strings" from "content localization" into separate Types in the long run (Lokalise Vantage vs Expert, Phrase TMS vs Strings both split it) — recorded as a taxonomy observation for the boundary-issues log.

## Final Synthesis

Software Localization Management is the software team's translation production system: the product's user-facing text is held as an identified source-string corpus with per-locale translations; translation work is produced and tracked per string per locale through review states under role- and language-scoped access, fed by TM/MT/glossary/context machinery; and the corpus is kept in step with the changing product — strings flow in from development and finished translations flow back out in build-consumable form, with source changes marking dependent translations stale. Everything else commonly associated with the category — keys vs keyless formats, VCS integration, tasks/jobs, crowdsourcing, AI, OTA delivery, cost machinery — is standard, variant, or era-current structure, not the defining core.
