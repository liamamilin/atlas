# Research Notes — Developer Documentation Portal

## Research Goal

Understand "Developer Documentation Portal" as an Application Type (DIRECTORY §12 Software Development & Product Engineering): what the software category actually consists of when an organization (or open-source project) produces and operates its developer-facing documentation, what stable structures hold across very different production philosophies (docs-as-code static generators vs hosted platforms vs reference-centric portals), and where the boundaries sit against the neighboring Types — especially API Documentation Platform (§12, processed; carries a joint-review flag that this pass must discharge), Product Documentation Portal (§02.07, unprocessed), Help Center (§02.06, processed), Internal Developer Portal (§12, unprocessed), Blogging Platform (§02.07, processed), and the API-management "developer portal" usage.

## Initial Boundary

Initial hypothesis: the Type is the developer-facing documentation surface for a buildable product — quickstarts, tutorials, how-to guides, API/SDK reference, examples — produced by the product's own team and published as a self-serve navigable site. Two readings of the leaf exist and must be reconciled:

1. the **portal itself** (the operated docs site of a product, e.g. a payments API's docs),
2. the **platform/system** through which such portals are produced and operated (documentation platforms and docs-as-code toolchains).

The production-pack precedent (Help Center, API Documentation Platform passes) samples the platform/system category and treats operated instances as posture evidence. This pass follows the same convention. The most confusable neighbor is API Documentation Platform (sibling leaf, processed 2026-09-06) — its Boundary Findings flagged "api-documentation-platform vs developer-documentation-portal" for joint review when this leaf is processed; discharged below (Boundary Findings #1).

## Research Questions

1. What content genres constitute the corpus (quickstart, tutorial, how-to guide, concept page, API/SDK reference, examples, changelog)?
2. What is the unit of content, and how is the corpus organized (pages, navigation trees, sidebars, guides-vs-reference split)?
3. How is content produced, reviewed, and published (docs-as-code vs editor-first)? What is the production pipeline?
4. How does the corpus stay current with the product (release-coupled versioning, source-coupled rebuilds)? Is versioning definitional?
5. What role does code play in the corpus (blocks, copy, tabs, runnable examples, generated reference)?
6. What does the reader's loop look like (orient → first success → build → return for lookup)?
7. Who produces it (writers, DX engineers, developers, devrel) and how do roles split?
8. Deployment/business forms (open-source generator, hosted SaaS, hosting layer) and customer levels (open-source project vs enterprise)?
9. Where are the boundaries: API Documentation Platform, Product Documentation Portal, Help Center, Internal Developer Portal, Blogging Platform, CMS, API-management "developer portal"?
10. Historical check: would older developer documentation (generated HTML references, manual pages, CHM/PDF manuals) still satisfy the definition?

## Representative Products

| Product | Philosophy | Customer level | Evidence tier |
|---|---|---|---|
| Mintlify | modern hosted docs-as-code platform (git-backed, MDX, CLI + web editor + AI) | commercial, enterprise-leaning devrel | Tier 1 (official quickstart) |
| Docusaurus | open-source static-site documentation framework (Meta OSS) | free/open-source, powers large product portals | Tier 1 (official intro + versioning docs) |
| GitBook | editor-first hosted documentation platform with git/agent/API routes | commercial, general docs posture | Tier 1 (official docs root) |
| ReadMe | hosted, reference-centric pole (API docs framing + full guide corpus) | commercial, enterprise tiers | Tier 1 (official docs welcome) |
| Read the Docs | open-source build/host layer for docs toolchains (Sphinx/MkDocs/Docusaurus) | open-source projects (free) + business tier | Tier 1 (official platform docs) |

Posture anchor: Stripe's operated developer portal (docs.stripe.com) fetched once for operated-portal framing (Tier 2). The api-documentation-platform pass (2026-09-06) independently observed ReadMe/Mintlify at Tier 1; its findings are reused only as cross-pass corroboration, marked B where so.

## Sources

- Mintlify — official documentation: Quickstart (https://mintlify.com/docs/quickstart), fetched 2026-09-08
- Docusaurus — official documentation: Introduction (https://docusaurus.io/docs), Versioning (https://docusaurus.io/docs/versioning), fetched 2026-09-08
- GitBook — official documentation root (https://docs.gitbook.com/), fetched 2026-09-08
- ReadMe — official documentation: Welcome (https://docs.readme.com/main/docs/about-readme), fetched 2026-09-08
- Read the Docs — official platform documentation root (https://docs.readthedocs.com/platform/stable/), fetched 2026-09-08
- Stripe — operated developer portal root (https://docs.stripe.com/), fetched 2026-09-08 (posture only)
- Paired prior pass: research/api-documentation-platform.md (2026-09-06), research/help-center.md (2026-09-07) — boundary corroboration only

## Product Observations

### Mintlify

Evidence layer: A (direct, official quickstart).

Key observations:

- **Docs-as-code posture**: "Mintlify uses a docs-as-code approach... Every page on your site has a corresponding file stored in your documentation repository." Content is MDX; site structure configured in `docs.json`; web editor "connects to your documentation repository".
- **Two production routes**: web editor (edit in browser, click Publish) vs local CLI (scaffold `mint new` with themes/templates, local preview `mint dev`, push to production branch triggers automatic deployment).
- **Quality tooling around the corpus**: `mint validate`, `mint broken-links` (link integrity as a first-class check), CLI reference for more.
- **Publication**: hosted at a default subdomain; custom domain as a customization step; dashboard shows deployment status.
- **AI-era serving**: "Connect AI tools like Claude, Cursor, and ChatGPT to your search MCP server so they can efficiently search and retrieve content from your site." The quickstart page itself is written as agent instructions — the platform treats AI agents as a reader class.
- Genre signals: quickstart = deploy → edit → publish loop; next-steps cards for editor, MCP, CLI, custom domain.

### Docusaurus

Evidence layer: A (direct, official intro + versioning page).

Key observations:

- **Self-description**: "static-site generator... focus on your content and just write Markdown files"; "out-of-the-box documentation features"; explicitly documentation-focused vs general SSGs ("Docusaurus tries to do one thing super well").
- **Feature set named as documentation features**: search ("your full site is searchable"), "Document Versioning: Helps you keep documentation in sync with project releases", i18n, theming, MDX with "interactive components... Share your code in live editors".
- **Versioning mechanics (direct observation)**: CLI tags a new version by freezing `docs/` into `versioned_docs/version-X/` + versioned sidebars + `versions.json`; "current" version labeled Next under `/docs/next`, latest at `/docs`; reader-facing version dropdown; version banners `unreleased`/`unmaintained`; archived versions kept at immutable URLs; deleting a version = removing from `versions.json` + deleting its directory.
- **Versioning is explicitly optional**: "Most of the time, you don't need versioning... Versioning is best suited for websites with high-traffic and rapid changes to documentation between versions." Recommended to "keep the number of versions small" and version "only when needed" (semver reasoning).
- **Docs-as-code contributor flow**: "Edit this page" links to the GitHub source; "Last updated on ... by ..." attribution on pages; link docs by file paths so links survive version cuts.
- **Sidebars/navigation**: sidebar trees (manual or autogenerated from directories), multi-instance docs (several doc trees per site); blog exists as a separate chronological plugin — structurally distinct from docs.
- Their own site operates as a developer documentation portal: version switcher (canary/3.10.2/.../archived), locale switcher, search, showcase.

### GitBook

Evidence layer: A (direct, official docs root).

Key observations:

- **Framing**: "Documentation your users actually read. Your users are humans and their AI agents — GitBook publishes for both."
- **Three production routes**: "In the editor — Write and publish visually. Blocks, change requests, and review without touching a terminal." / "From your agent — Drive GitBook from Claude, Cursor, or any MCP client. Draft, restructure, and open change requests." / "With code — Sync from Git, script with the CLI, or build on the API."
- **Lifecycle as the product's spine**: CREATE (get content in) → COLLABORATE ("review before anything goes live", change requests) → PUBLISH ("structure, brand, and control access") → IMPROVE ("see what readers need next" — analytics).
- **AI layer, both sides**: GitBook Agent (drafts/edits/reviews, flags gaps against style guide), reader-facing AI Assistant ("answers questions on your site from your docs and connected support sources"), AI Insights (visitor questions → knowledge gaps), MCP for docs ("your published docs as a tool, so your customers' agents can read them properly").
- Changelog and support surfaces exist beside the docs corpus (gradient signals toward support/community, not the center).
- Posture: general documentation platform (product docs + developer docs) — gradient toward Product Documentation Portal.

### ReadMe

Evidence layer: A (direct, official docs welcome page). Corroborates the 2026-09-06 API Documentation Platform pass (Layer B across passes).

Key observations:

- **Framing**: "Helping you create docs that make your APIs easy to use and maintain" — the reference-centric pole of this Type, API-facing.
- **Genre tiles**: Quick Start ("learn how to write and publish docs" — for the docs producers), API Reference ("use an OAS file, or create one with ReadMe"), Recipes ("step-by-step code walkthroughs"), Changelog ("keep users up-to-date on the latest changes"), Customize (logo/brand/theme), Integrations, MDXish (Markdown + MDX on one page).
- **Sync machinery**: "Sync with GitHub", "Sync with GitLab — bidirectionally sync docs between GitLab & ReadMe", ReadMe CLI ("update docs and sync OpenAPI specs from CLI"), API V2 ("manage your docs using our API").
- **Analytics**: "My Developers — get developer usage data in ReadMe"; Enterprise Analytics ("documentation metrics for enterprise") — docs usage tied to developer behavior.
- **AI era**: "Build with AI" (write/review/improve docs with AI), "AI Discoverability — your docs, now agent ready", MCP Servers ("AI agents can discover and call your API"), Inline AI, AI Branch Reviews ("review branches before merging with AI Linter").
- Enterprise: groups/project management, user management for teammates and end users.

### Read the Docs

Evidence layer: A (direct, official platform docs root).

Key observations:

- **Framing**: "simplifies managing software documentation by building and hosting your docs automatically, using the Git workflow you already use for code. Treating documentation like code."
- **Currency coupling as the headline feature**: "Whenever you push code to Git, Read the Docs will automatically build your docs so your code and documentation are always up-to-date."
- **Versions**: "Read the Docs can host multiple versions of your docs. Keep your 1.0 and 2.0 documentation online, pulled directly from Git." — versions sourced from git branches/tags; URL versioning schemes documented.
- **Doc-toolchain hosting layer**: supports Sphinx, MkDocs, Docusaurus ("popular documentation tools... quick start for MkDocs and Docusaurus"); reproducible builds; `.readthedocs.yaml` configuration.
- **Maintaining a mature corpus**: user-defined redirects ("redirect your old URLs to new ones"), traffic analytics, security logs; subprojects (multiple projects under one domain); i18n/localization; custom domains.
- **Review flow**: pull request previews ("preview your documentation on every pull request").
- **Audience scope**: Community tier hosts 100,000+ open-source projects; Business tier "supports hundreds of organizations with product and internal documentation" — internal documentation is an explicit deployment variant.
- **Minimal form**: a hosted library manual with versions and zero API-reference machinery is a full member of this Type — evidence that the guide corpus, not the API reference, is the center.

### Stripe (operated portal, posture only)

Evidence layer: A (direct, Tier-2 posture fetch).

- "Explore our guides and examples to integrate Stripe" — integration-first framing of a commercial developer portal.
- Use-case-driven entries ("Accept payments online", "Sell subscriptions"), "Integration quickstarts", "Set up your development environment", browse-by-product structure, "Build on Stripe with AI" (agents page).
- Every docs URL also served as `.md` — the portal serves agent-readable renderings beside human pages (current-era signal, consistent with the platforms' MCP/agent features).

## Cross-product Comparison

| Dimension | Mintlify | Docusaurus | GitBook | ReadMe | Read the Docs | Layer |
|---|---|---|---|---|---|---|
| Team-authored addressable page corpus | yes | yes | yes | yes | yes | A→B |
| Published self-serve navigable site (nav tree + search) | yes | yes (sidebar + search) | yes (structure + brand) | yes | yes | A→B |
| Production machinery (pipeline or editor system) | CLI + web editor + repo | SSG build + git | editor/change requests + git/CLI/API | hosted editor + git sync + CLI + API | git-push builds + yaml config | A→B |
| Currency coupling to the product | git push → deploy | versioning "in sync with project releases" | publish pipeline (currency implicit) | OpenAPI sync, changelog | git push → automatic rebuild | A→B |
| Docs-as-code route available | yes | native | yes (one of three routes) | yes (GitHub/GitLab sync, CLI, API) | native | A→B |
| Editor-first route available | yes (web editor) | no (code-first) | yes (primary) | yes (hosted editor) | no | A |
| Developer-build genre (quickstart/tutorial/how-to/reference) | yes | yes | yes | yes (+API reference core) | yes (library manuals) | A→B |
| API reference section present | yes | optional (plugins) | general | central | often absent (libraries/CLIs) | A |
| Code as first-class content | MDX | MDX + live editors | blocks | MDXish + recipes | toolchain-native (Sphinx/MkDocs) | A→B |
| Release-coupled versioning | not verified in this pass | yes (explicitly optional) | not verified in this pass | yes (doc version forking, prior pass) | yes (from git) | A/B |
| Changelog/release notes | next-step cards | separate plugin | yes | yes | changelog page | A→B |
| Branding / custom domain | yes | theming + any host | yes (PUBLISH stage) | yes | yes | A→B |
| Analytics / reader insight | dashboard | traffic via host | AI Insights + IMPROVE | My Developers + Enterprise Analytics | traffic analytics | A→B |
| Review before publish | git flow | git PR flow | change requests | branch reviews (AI linter) | PR previews | A→B |
| Link integrity tooling | broken-links check | version-safe relative links | not verified | not verified | redirects | A |
| i18n | not verified | yes | not verified | not verified | yes | A |
| Private / access control | not verified | possible via hosting | access control at publish | enterprise user management | business tier (SSO, private sharing) | A |
| AI reader/agent surfaces | search MCP | — (community ecosystem) | AI assistant + docs MCP | agent-ready + MCP | — | A→B (current era) |
| Internal docs deployment | not verified | possible (self-host) | possible (access control) | possible (end-user gating) | explicit (Business tier) | A/B |

Reading: five very different production philosophies (code-first SSG, hosted git platform, editor-first platform, reference-centric platform, toolchain hosting layer) converge on the same three-part skeleton — team-authored corpus + self-serve navigable publication + managed production/currency machinery — with the developer-build genre as the content signature. Everything else varies freely.

## Canonical Model — Abstraction Analysis

### Level 0 — Defining Invariant (candidate)

Three jointly-held structures:

1. **The build-with-product corpus of record.** A persistent body of individually addressable documentation pages, authored and maintained by the product's (or project's) own team, whose content teaches and references building with the product's programmable surface: getting started, building/integrating, and reference of the interfaces (APIs, SDKs, CLIs, configuration, extension points) a developer works against. Authorship belongs to the producer side; readers do not edit the record copy (contribution reaches the corpus only through the team's review machinery). Remove the build-with-product genre → product usage docs or marketing material; remove team authorship → community forum / Q&A site.
2. **The published self-serve developer surface.** The corpus published as a navigable reading surface organized by structure — a topical browse hierarchy (navigation tree/sidebar) plus retrieval (search in current products) — reachable by developers without staff mediation. Remove the published surface → internal manuscript; organize chronologically instead → a blog, not a docs corpus.
3. **The production-and-currency machinery.** A managed production side through which the team creates, organizes, reviews, and updates the corpus (docs-as-code pipeline, or an authoring/publishing system), carrying an explicit mechanism that keeps the published corpus aligned with the product as the product changes — release-coupled doc versioning, or source-coupled rebuild/sync. Remove → a hand-published, unmanaged page collection.

Joint-hold is load-bearing: 1+2 without 3 = a pile of published pages, not a managed portal system; 2+3 without 1 = a generic publishing platform with no developer genre; 1+3 without 2 = an internal writing system with no reader-facing portal.

The three legs jointly serve one purpose: a developer can go from "what is this product" to a working integration entirely self-serve, and return to the corpus as a working lookup surface throughout the build — with the corpus tracking the product's buildable surface over time.

### Level 1 — Common Mature Structure

- **Search** over the corpus (universal in the sample at the reader surface; Docusaurus "your full site is searchable", GitBook IMPROVE stage, ReadMe, RtD via hosts).
- **Code as first-class content**: syntax-highlighted code blocks, copy affordances, language/framework tabs, runnable or "live" examples (Docusaurus live editors; Mintlify/ReadMe MDX; ReadMe recipes).
- **Guides-and-reference split inside one navigation** — hand-written learning pages beside generated or hand-maintained reference pages in one tree (all sampled products; ReadMe/API-doc pass corroborates).
- **Release-coupled versioning with a reader-facing switcher** — docs frozen per release (Docusaurus), pulled from git (RtD), forked doc versions (ReadMe, prior pass). Common and expected, **but explicitly optional** (Docusaurus: "Most of the time, you don't need versioning").
- **Changelog / release notes** as a maintained surface (ReadMe, GitBook, Docusaurus plugin).
- **Branding and custom domains** — the portal presents as the product's own (Mintlify, GitBook PUBLISH stage, ReadMe, RtD).
- **Review-before-publish** — change requests, PR flows, branch reviews, PR previews (GitBook, Docusaurus/RtD git flows, ReadMe AI branch reviews).
- **Reader analytics / content insight** — page traffic, search terms, reader questions → content gaps (RtD traffic analytics, GitBook AI Insights, ReadMe My Developers).
- **Link-integrity machinery** — redirects, broken-link checks, version-safe linking (RtD redirects, Mintlify broken-links, Docusaurus version-safe relative links).
- **AI surfaces (current market layer)**: reader-facing AI assistants grounded in the corpus; agent-oriented machine access to the corpus (MCP servers, `.md` endpoints, agent-ready indexes); AI writing/review assistance (GitBook, Mintlify, ReadMe — all three current products ship it).
- **i18n / translations** (Docusaurus, RtD — optional).
- **Private/gated documentation and access control** (RtD Business, ReadMe enterprise, GitBook publish-stage access control).

### Level 2 — Variant / Optional Structure

- **Production substrate**: code-first static generator (Docusaurus) vs hosted git platform (Mintlify) vs editor-first hosted platform (GitBook, ReadMe) vs build/host layer over toolchains (RtD).
- **Reference depth**: corpus-centric portals where a reference may be thin or absent (RtD library docs) vs reference-centric portals (ReadMe pole) — gradient toward API Documentation Platform.
- **Audience scope**: public developer portal vs internal developer documentation (RtD Business explicitly hosts internal docs) — internal instances are still this Type when the corpus documents building with a product's surface; the Internal Developer Portal Type is a different center (service catalog).
- **Operator type and scale**: open-source project maintainers (RtD community: 100k+ projects) vs commercial devrel organizations (Stripe-class operated portals; enterprise tiers of the platforms).
- **Multi-product/multi-doc-tree organization** (Docusaurus multi-instance, RtD subprojects, ReadMe enterprise groups).
- **Developer-hub breadth**: some operated portals add community links, support channels, status, sandbox provisioning — breadth beyond the docs corpus is optional posture, not the Type's center.
- **Monetization/packaging**: free OSS (Docusaurus, RtD community) vs commercial SaaS with enterprise tiers.

### Level 3 — Vendor-specific (Research Notes only)

- Mintlify: `mint` CLI command set (`mint new/dev/validate/broken-links/login/signup/status`), `docs.json` config, `.mintlify.site` staging domains, dashboard deployment-status page.
- Docusaurus: `versioned_docs/` + `versions.json` + `versioned_sidebars/` scheme; `unreleased`/`unmaintained` banner vocabulary; "current vs latest" terminology; swizzling; multi-instance plugin.
- GitBook: Agent/AI Assistant/AI Insights/MCP product names; change-request model as the review unit; "spaces" vocabulary (not directly verified this pass).
- ReadMe: "Recipes", "My Developers", "Refactored", "MDXish", "AI Discoverability", project/group enterprise model.
- Read the Docs: `.readthedocs.yaml`, subprojects, community-vs-business split, URL versioning schemes.

## Vendor-specific Findings

See Level 3. No vendor module was promoted into the canonical model. One cross-vendor observation worth keeping at L1 rather than L0: **the AI/agent layer is present in all three commercial current products** (Mintlify, GitBook, ReadMe) and in operated portals (Stripe `.md` endpoints) — but the open-source/toolchain side shows it only via ecosystem convention rather than product features, so it is recorded as a current-market expectation, not a defining or even fully universal structure.

## Boundary Findings

1. **vs API Documentation Platform (§12 sibling, processed 2026-09-06 — joint-review flag discharged from this side).** Center-of-gravity difference, held on the central artifact. The API documentation platform's central artifact is the published, definition-bound API interface reference with a currency mechanism against the definition; the developer documentation portal's central artifact is the developer-docs corpus (learning + how-to + reference as one section among several). Evidence from this side: (a) ReadMe — the reference-centric pole — still ships the full corpus (quickstart, recipes, changelog, guides) and markets itself as docs for "APIs easy to use and maintain", i.e. the corpus is the site, the reference its core section; (b) Read the Docs community projects routinely run full developer portals (versioned manuals for CLIs/libraries) with **no** API-reference machinery at all — the corpus stands alone; (c) conversely, an embedded reference renderer with no corpus exists as the API-doc platform's minimal form. Both leaves remain defensible as distinct centers of gravity; products visibly span the gradient (Mintlify, ReadMe). Recommendation stands for a joint review to record the gradient formally; from this side, boundary **held**.

2. **vs Product Documentation Portal (§02.07, unprocessed).** Genre/audience seam, not a wall. Working split: the product documentation portal centers the product's usage documentation (any audience; usage genre); the developer documentation portal centers the build-with-product corpus for developers working against a programmable surface, with build-loop machinery (code-forward content, interface reference, release-coupled currency). The seam collapses where the product's *entire* audience is developers (a CLI or library's product docs are its developer docs) — recorded as a genuine gradient. Help Center's pass (2026-09-07) already described product documentation as "reference/tutorial/API, release-versioned", which overlaps this Type; joint review with the Product Documentation Portal pass is recommended before that leaf is processed, so the two definitions are ratified together rather than sequentially.

3. **vs Help Center (§02.06, processed).** Clear on the content shape and currency rhythm: help-center corpus is problem-shaped (troubleshooting/FAQ answers, continuously maintained, success = deflection); developer-docs corpus is build-shaped (learning → building → reference, release-coupled, success = unassisted first success + working lookups). Tooling overlap (search, feedback, analytics, AI answers) is genre-independent platform machinery. Boundary held.

4. **vs Internal Developer Portal (§12 sibling, unprocessed).** Different center: the internal developer portal catalogs the organization's own services, ownership, environments and golden paths for its engineers (a service-experience surface); this Type's center is the documentation corpus about building with a product. Internal-facing *instances* of developer documentation exist (RtD Business explicitly hosts "internal documentation") and remain this Type — audience location (internal vs external) is a variant, the corpus is the invariant. Boundary expected to hold; noted for the unprocessed pass.

5. **vs "Developer Portal" in the API-management sense** (observed in the API Management Platform pass: "Publish on Developer Portal" as a distinct step; portal issuing keys per application). That surface is an API-consumer onboarding/access venue (app registration, key issuance, subscriptions, usage) — its center is access and commerce, and docs are one panel. Not this Type, though operated developer portals for public APIs may bundle such access surfaces.

6. **vs Blogging Platform (§02.07, processed).** Organization axis: blog = chronological post stream; docs corpus = structure-organized persistent pages. Changelogs and blogs may live *inside* a developer portal (Docusaurus blog plugin; GitBook changelog) as secondary surfaces. Boundary held.

7. **vs Content Management System / Headless CMS (§02.07, processed).** A CMS is general-purpose content management with page/entry models defined by the implementing team; developer-docs platforms are specialized for the documentation genre: doc-tree navigation, release-coupled versioning of whole trees, code presentation, reference generation, doc-specific QA (broken links, validation). A headless CMS can back a docs site (headless-cms pass records this as downstream consumer), but the genre machinery is what the market buys documentation platforms for. Boundary held.

8. **Variant-of-Type check (taxonomy).** Is Developer Documentation Portal merely an audience variant of Product Documentation Portal? Resolution: the directory positions it under §12 as a developer-systems Type, and the researched category (documentation platforms/toolchains) has its own market existence (Mintlify/GitBook/ReadMe/Docusaurus/RtD all sell/serve "developer documentation" as the primary job). The Type is kept; the overlap seam with Product Documentation Portal is recorded in #2 for joint review rather than silently resolved.

## Uncertainties

- **Mintlify versioning**: not fetched in this pass; no claim made either way. Versioning's L1 status rests on Docusaurus (A), Read the Docs (A), ReadMe (A via prior pass).
- **GitBook site structure details** (site sections/variants/spaces): the docs-root fetch succeeded but the follow-up concept query timed out; GitBook observations are posture-level for structure internals and concept-level for the lifecycle/AI layer.
- **Operated-portal side**: only Stripe fetched, posture-only; the operated-portal reading is corroborated mainly through the platforms' own showcases and the api-doc pass — asserted at posture strength, not detail strength.
- **Historical anchors** (generated HTML references such as javadoc/Doxygen/Sphinx-era output, man pages, CHM/PDF manuals): reasoned from general knowledge, not fetched sources; the historical check is therefore reasoning-based (see below), consistent with how other passes handled pre-web-era forms.
- **Market-convergence risk**: whether the market will keep treating developer documentation platforms and product documentation platforms as separate categories is a live question (recorded as joint review, not resolved here).

## Historical / Market-Sample Check (reasoning-based)

Question: would older, regional, platform-native, or differently positioned developer documentation still fit the candidate L0?

- **Generated HTML reference era** (javadoc/Doxygen/Sphinx-class generators): team-authored addressable pages (leg 1), published navigable surface with index/trees (leg 2), and a generation pipeline coupling docs to source (leg 3 — generation tooling long predates the modern platform era). Fits.
- **Manual pages / PDF/CHM manual era**: corpus + published (non-web) reading surface + (primitive but real) production process. Fits the abstract core; the "portal" word is a web-era label — the definition deliberately says "published reading surface", not "website". Search is absent in the oldest forms → search stays L1.
- **Open-source project docs on free hosting** (RtD community): fits directly (observed, Layer A).
- **Internal developer documentation**: fits (RtD Business, Layer A); audience-location variant.
- Versioning fails the invariant test in the other direction: Docusaurus documents that most projects should *not* version (Layer A), so versioning cannot be L0 despite being release-coupled in mature products — currency machinery is L0, release-coupled doc-tree versioning is its common mature realization.

Conclusion: the definition survives the historical check; the L0 keeps no web-specific, platform-specific, or versioning-specific element.

## Final Synthesis

A Developer Documentation Portal is the managed documentation system through which a product's own team publishes, organizes, and keeps current the corpus that teaches developers how to build with the product and references what can be built. Its defining core is three jointly-held structures: the build-with-product corpus of record (team-authored addressable pages), the published self-serve developer surface (structure-organized navigation + retrieval), and the production-and-currency machinery (managed pipeline or authoring system with an explicit mechanism keeping the corpus aligned with the product's evolution). The market realizes the Type across four production philosophies — code-first static generators, hosted git platforms, editor-first platforms, and toolchain hosting layers — plus the reference-centric pole that shades into the API Documentation Platform. Standard capabilities (search, code-forward presentation, guides/reference in one tree, release-coupled versioning, changelogs, branding, review flows, analytics, link integrity, AI/agent surfaces) make the corpus maintainable, discoverable, and trustworthy but do not define it. The load-bearing boundaries: the API Documentation Platform begins where the definition-bound interface reference itself is the central artifact; the Product Documentation Portal seam (usage genre vs build genre) needs joint ratification; the Help Center begins where the corpus becomes problem-shaped support answers; the Internal Developer Portal begins where a service catalog, not a docs corpus, is the center.
