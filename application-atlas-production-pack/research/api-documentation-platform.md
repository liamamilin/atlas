# Research Notes — API Documentation Platform

## Research Goal

Understand what an API Documentation Platform actually is as an Application Type: its central artifact, how reference documentation is produced and kept current, what the API consumer sees and does, the publication lifecycle, and — critically — how the Type separates from three close neighbors (API Design Platform, Developer Documentation Portal, API Development Workbench) that already have processed leaves in this directory.

## Initial Boundary (hypothesis before research)

- Core hypothesis: the Type's center is a **rendered, consumer-facing API reference** kept consistent with a structured definition of the API, not the authoring of that definition (design platform) and not the execution of requests against the API (workbench).
- Likely confusions:
  - API Design Platform — also renders reference previews; prior sibling research already drew a "downstream gradient" line (contract authoring vs exhibiting the contract).
  - Developer Documentation Portal — a separate directory leaf; expected to differ by center of gravity (whole developer-docs corpus vs API interface reference).
  - API Development Workbench — try-it-out consoles appear inside docs; expected to be embedded workbench capability, not the docs Type's loop.
  - Help Center / Knowledge Base — article-centric vs endpoint-centric.
- Unknowns at start: whether hand-authored (non-spec) reference docs still belong to the Type; whether versioning is definitional; how strong the docs-platform ↔ developer-portal gradient is in current products.

## Research Questions

1. What is the central artifact, and how is it structured (operations, parameters, request/response, errors)?
2. Where does reference content come from: machine-readable specification, request collections, hand-authored structured pages, code?
3. What is the publication model: hosted portal, static docs-as-code toolchain, embeddable renderer? What surfaces exist for authors vs readers?
4. How is the reference kept current as the API changes (git sync, CI/CD, CLI, URL import, API-driven sync)?
5. What surrounds the reference: guides, quickstarts, changelogs, versioning, search, branding?
6. What can the consumer do beyond reading: try-it-out console, code samples, spec download, personalization?
7. Who operates the product (technical writers, DevEx/DevRel, developers) and what roles/permissions matter?
8. Boundary: what would have to be true for this to collapse into API Design Platform / Developer Documentation Portal / Workbench?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

1. **ReadMe** — commercial SaaS pure-play API documentation platform; "docs as the product" philosophy; API-reference-centric with guides around it.
2. **Redocly (Redoc CE / Realm / Reunite)** — OpenAPI-native toolchain lineage: open-source reference renderer (Redoc) plus hosted docs platform (Reunite/Realm); docs-like-code philosophy.
3. **Mintlify** — modern git-based docs-as-code platform for developer documentation with full API reference support; general developer-docs center of gravity (gradient probe toward Developer Documentation Portal).
4. **Postman (published documentation)** — the workbench's publishing face; source artifact is a request collection rather than a specification (boundary probe from the workbench side).
5. **Swagger UI** — historical anchor: the open-source reference renderer that established the pattern; no hosting, no portal, no versioning. Used for the historical/market-sample check.
6. **Stoplight** — boundary probe only, reusing observations recorded during the api-design-platform research pass (its docs site was unreachable then and was not re-attempted).

## Sources

All fetched 2026-09-06 unless noted.

- ReadMe — https://docs.readme.com/main/docs/about-readme , https://docs.readme.com/main/docs/quickstart.md , https://docs.readme.com/main/docs/api-reference.md , https://docs.readme.com/main/docs/versions.md
- Redocly — https://redocly.com/docs/ , https://redocly.com/docs/realm/get-started , https://redocly.com/docs/realm/content/api-docs
- Mintlify — https://mintlify.com/docs/quickstart , https://www.mintlify.com/docs/guides/migrating-from-mdx.md , https://www.mintlify.com/docs/api-playground/openapi-setup.md
- Postman — https://learning.postman.com/docs/publishing-your-api/publishing-your-docs.md
- Swagger UI — https://github.com/swagger-api/swagger-ui (official repository README; official docs pages)
- Stoplight — https://stoplight.io/ (product posture, from the api-design-platform research pass of 2026-09-06; operational docs site rendered as JS-only shell)

Sourcing notes:

- All five primary products yielded Tier-1 operational documentation. Stoplight was downgraded to posture-level evidence (recorded in the sibling research file).
- Swagger.io's dedicated Swagger UI documentation page returned 404; the official GitHub repository README was used instead.

## Product Observations

### ReadMe (evidence layer A)

- Positioning: "Helping you create docs that make your APIs easy to use and maintain." Product organized around **Guides + API Reference + supporting sections** (Recipes = step-by-step code walkthroughs, Changelog, Landing Page, Custom Pages).
- Quickstart flow: create project (name, logo, auto brand colors) → **upload OpenAPI file or URL → "generates interactive API reference with endpoint descriptions, request/response examples, and a built-in API explorer"** → write guides in the editor (or AI agent drafting from the uploaded spec).
- API Reference page: "the definitive technical guide to your API, documenting every endpoint, parameter, and response code"; "an interactive experience where developers can explore your API, make test calls right from the documentation, and see real responses without writing a single line of code."
- Spec intake: OpenAPI 3.0, 3.1, Swagger 2.0; file upload, URL import, GitHub/GitLab **bi-directional sync**, CLI (`rdme`) with GitHub Actions recipes, and an "API Sync" mechanism.
- Without a spec: **API Designer** — build the reference from scratch via an interface ("document your endpoints, parameters, request bodies, and response objects without needing to write a single line of YAML or JSON").
- Customization: authentication details and custom headers, code samples in multiple programming languages, endpoints organized into logical groups, per-group custom documentation.
- **Versioning**: versions forked from existing ones ("semver-ish"); Guides, Recipes, and Reference are versioned; Landing Page/Discussions/Changelog persist across versions; per-version beta/deprecated states with reader-visible banners; default/public/hidden visibility; reader-facing version dropdown.
- Personalization: "Personalized API Docs — inject your users' API keys, server variables, and more."
- Enterprise: groups (multi-project management), user management incl. end-user access; Enterprise Analytics ("documentation metrics"); Global Reusable Content across projects/versions (plan-gated).
- AI layer: Ask AI, MCP servers, LLMs.txt, AI discoverability, inline AI, AI branch reviews with an AI linter; docs linter/style guide configuration.
- Branches + reviews: docs editing with branch/PR review flows (bi-directional GitHub sync).

### Redocly (evidence layer A)

- Product family: **Redoc** (open-source CE: "a clean and easy way to produce web-ready documentation from an OpenAPI description"), **Realm** ("Redoc, Revel, and Reef united into a single platform"; Revel = external developer showcase, Reef = internal service catalog), **Reunite** (cloud platform where projects are "managed and deployed"), **Redocly CLI** ("OpenAPI multi-tool to manage, lint, validate and transform your OpenAPI files").
- "This website runs entirely on Realm" — Redocly's own docs are a deployment of the product (dogfooding evidence).
- API documentation section: spec support for **OpenAPI, AsyncAPI, GraphQL, and SOAP documentation from a WSDL file**; **mock server** ("use the Replay console to send calls to your API operations and see sample responses without the need for backend services"); **Try-it console**; OpenAPI/AsyncAPI extensions for customization.
- Authoring: built-in Reunite web editor or local development with your own editor; content in Markdoc; navigation, branding, search-and-SEO, access control ("Control site access"), measurement ("Measure your docs"), organization management; "Make docs AI ready".
- Get-started: "Go live with your docs in minutes using our guided setup"; projects are git-connected (local dev + Reunite editor paths).

### Mintlify (evidence layer A)

- Positioning: "a platform for building and hosting documentation websites" with docs-as-code: "Every page on your site has a corresponding file stored in your documentation repository." Web editor connects to the repo; git push triggers deployment; CLI (`mint dev/validate/broken-links`).
- **API reference from OpenAPI**: add one or more OpenAPI 3.0/3.1 specs (repo path or public URL) to `docs.json` navigation → endpoint pages auto-generated; navigation can mix generated endpoint pages with hand-written pages (`"GET /users"`, `"POST /users"` interleaved with MDX pages); tags → navigation groups; `x-mint` extensions inject metadata/content per endpoint, `x-hidden` excludes endpoints; `x-group` renames groups.
- **Hand-written API pages still supported**: MDX pages with `openapi` frontmatter referencing a specific spec operation (or `openapi-schema` for data models); scraper CLI can generate MDX stubs from a spec; a migration guide exists from MDX pages → OpenAPI navigation, which states hand-written pages remain useful for "extensive custom content per endpoint".
- **API playground**: request builder enabled by `servers` field; authentication from `securitySchemes`/`security` (API key, bearer, basic); `x-default` prefills credentials; per-endpoint playground visibility (public vs auth-restricted groups); file-upload handling.
- **Multiple API versions**: tabs each bound to a different spec file ("API v1" / "API v2"); per-page `version` metadata.
- Publishing surface: hosted site at subdomain or custom domain; "Download API spec" contextual option (with an explicit warning that the downloaded spec is unfiltered and bypasses authentication groups — a security-relevant behavior); private/authenticated docs via OAuth/Auth0 configuration, authentication groups.
- Analytics + AI: REST API for page views/visitors split by human vs AI traffic, search queries, thumbs feedback, assistant conversations; embeddable assistant; MCP search server; agents that edit docs via PRs; scheduled automations; static export for self-hosting.
- Use-case breadth: developer documentation, knowledge base, help center guides — the general developer-docs posture.

### Postman — published documentation (evidence layer A)

- Publishing model: documentation is generated from a **collection** (not an OpenAPI file); "Public documentation automatically includes details for each request or endpoint in the published collection, along with sample code in various client languages. As you update your collection, the published documentation automatically stays in sync with your latest changes. There's no need to publish the documentation again after making changes."
- Publish lifecycle: publish → public URL ("documenter" surface) → publication settings (version, environment variables, custom domain, layout double/single column, light/dark theme, logo, hex colors, SEO title/description ≤60/≤160 chars) → save and republish → **unpublish** (retract public availability; republish later).
- **Run in Postman button** embeds the collection so readers can open it in the Postman workbench; collections in public workspaces are discoverable on the Postman API Network.
- **Enterprise gate**: "Your Community Manager controls the Postman elements your team makes public... Enter a note for your Community Manager and click Request Publish" — publish requests flow through an approval role.
- Safety behavior: preview detects possibly sensitive tokens and highlights them before publishing.
- This is the workbench's docs byproduct: no standalone guides surface, no doc-version forking (versions can't be created for collections in v10+), branding at publish time.

### Swagger UI — historical anchor (evidence layer A)

- "Allows anyone — be it your development team or your end consumers — to visualize and interact with the API's resources **without having any of the implementation logic in place**. It's **automatically generated from your OpenAPI (formerly known as Swagger) Specification**."
- Distribution: npm module, dependency-free `swagger-ui-dist` ("copy the contents of the /dist folder to your server"), React component flavor — an **embeddable renderer**, not a hosted portal.
- Spec compatibility table from 2011 (Swagger 1.0) through 2026 (OpenAPI 3.2) — the pattern predates the modern SaaS market by a decade and a half.
- Capabilities: configuration, OAuth2 support in the try-it flow, deep linking, CORS documentation, plugin API for customization. No versioning of docs, no guides surface, no hosting, no analytics.

### Stoplight — boundary probe (evidence layer B, posture-level)

- Design-first platform whose published output includes branded, consumer-facing API reference documentation generated from the same specification that the design surface maintains (observations from the api-design-platform research pass; official docs site was a JS-only shell and not re-attempted). Confirms the design→docs hand-off gradient from the design-platform side.

## Cross-product Comparison

| Dimension | ReadMe | Redocly (Realm/Redoc) | Mintlify | Postman (published docs) | Swagger UI |
|---|---|---|---|---|---|
| Source of reference | OpenAPI 3.0/3.1/Swagger 2.0; or API Designer (form-built) | OpenAPI, AsyncAPI, GraphQL, SOAP/WSDL | OpenAPI 3.0/3.1 (nav-driven); or hand-written MDX pages bound to spec operations | Postman collection (HTTP requests) | OpenAPI/Swagger spec |
| Reference generation | spec → interactive reference + explorer | spec → web-ready reference (Redoc) | spec → generated endpoint pages in navigation | collection → per-request details + code samples | spec → dynamic documentation |
| Try-it-out console | yes ("make test calls right from the documentation") | yes (Try-it console + Replay mock server) | yes (playground from `servers`/`securitySchemes`) | Run in Postman button (hands off to workbench) | yes ("Try it out") |
| Guides/content beside reference | Guides, Recipes, Changelog, custom pages | Markdoc content pages in same site | MDX pages mixed into navigation; content types (Diátaxis) | descriptions inside collection only | none |
| Versioning of docs | first-class: forked versions, beta/deprecated, visibility, dropdown | per-spec-version (tabs/naming; site-level, not doc-fork machinery observed) | tabs per spec version; per-page version metadata | not supported for collections (CURRENT only) | none |
| Hosting posture | hosted SaaS portal | hosted Reunite + open-source CE renderer | hosted + static export | hosted publish surface | self-hosted/embedded renderer |
| Sync machinery | GitHub/GitLab bi-directional, CLI, API sync | git + Reunite editor; CLI lint/validate | git push deploys; URL specs need CI trigger; REST API trigger | automatic from collection edits | none (static) |
| Access control | hidden versions, enterprise users/end-users | site access control | private docs, OAuth/IdP, auth groups, group-scoped endpoint visibility | enterprise publish approval (Community Manager) | n/a |
| Analytics | My Developers, Enterprise Analytics | Measure your docs | views/visitors/search/feedback API (human vs AI traffic) | not observed as docs analytics | none |
| AI surfaces | Ask AI, MCP, LLMs.txt, AI linter/agent | "Make docs AI ready" | assistant, MCP search, agents via PRs, Index API | not observed | none |
| Personalization (reader-injected keys) | Personalized API Docs | not observed | playground auth groups; x-default prefills | not observed | OAuth config only |
| Governance/linting of docs | docs linter/style guide | Redocly CLI lint/validate of spec | mint validate; broken-links | secret-detection warning in preview | none |

Reading of the matrix:

- The **spec-derived interactive reference** appears in every product regardless of era (2011→2026) and business model — the strongest candidate for the defining structure.
- The **consumer-facing published surface** (readers who are not the authors) is present in every product — from a self-hosted renderer to a full portal.
- **Keeping current with the API** is present in every product in a form (regeneration from spec, auto-sync from collection, CI deployment) — "stale docs" is the shared failure mode.
- Everything else varies: guides depth, versioning machinery, hosting, access control, analytics, AI.

## Abstraction Hierarchy

### L0 — Defining Invariant

Smallest structure without which the product stops being recognizable as an API Documentation Platform:

```text
API interface reference
  (structured, navigable documentation of the API's interface:
   operations/endpoints, parameters, request/response formats, errors)
└── bound to a structured definition of the API
    (machine-readable specification, request collection, or
     structured authoring surface producing a spec-like definition)
└── published as a consumer-facing documentation surface
    (readers are consumers of the API, not its authors)
└── kept current as the API changes
    (regeneration/sync from the definition, however triggered)
```

- Remove the reference as central artifact → generic website builder or developer-portal corpus (different Type).
- Remove the binding to a structured definition → free-form article site (Help Center / Developer Documentation Portal territory).
- Remove consumer-facing publication → internal design tool (API Design Platform).
- Remove currency (no mechanism tying docs to the API's actual definition) → a static article site that happens to describe an API.

Notes on calibration:

- "Machine-readable specification" is deliberately NOT the invariant wording: Postman generates the reference from a collection, and ReadMe offers form-based endpoint authoring without a spec. The invariant is *a structured definition the reference stays bound to*, with the OpenAPI spec as the dominant realization.
- Versioning is NOT invariant: Swagger UI, Postman published docs, and single-version portals lack doc-version machinery.
- Try-it-out is NOT invariant: Redoc CE and classic static reference sites render without a console.

Historical/market-sample check (per §24): Swagger UI (2011 lineage, self-hosted/embedded, no hosting/versioning/guides/analytics) satisfies the L0 fully. WSDL→SOAP support (Redocly) shows the pattern predates OpenAPI as well. The definition does not over-fit the current SaaS market.

### L1 — Common Mature Structure

Present across most sampled products; makes the Type practical but not definitional:

- **Interactive try-it console** — request builder in the docs, parameters prefilled from the definition, authentication fields drawn from the spec's security schemes (ReadMe, Mintlify, Redocly Realm, Swagger UI; Postman delegates via Run in Postman).
- **Code samples in multiple client languages** per operation (ReadMe, Postman; Mintlify/Redocly via playground and theming).
- **Guides and explanatory content** beside the reference: quickstarts, authentication walkthroughs, conceptual pages (ReadMe Guides/Recipes; Mintlify MDX; Realm Markdoc). Depth varies; reference-only products exist.
- **Sync/keep-current machinery**: git bi-directional sync (ReadMe, Mintlify, Reunite), CLI upload/validate (rdme, mint, Redocly CLI), URL-based spec import, CI triggers, API-driven sync.
- **Versioning of documentation**: doc-version forking with reader-facing version switcher (ReadMe), or spec-per-tab version organization (Mintlify), or site-level version support (Realm). Mechanisms differ; the capability "consumers select the version matching their integration" is common.
- **Branding/customization**: logos, colors, themes, custom domains, layout (ReadMe design themes, Postman appearance settings, Mintlify custom domain, Realm branding).
- **Navigation/organization**: endpoints grouped (tags/resource groups), per-group overview text, mixed content navigation.
- **Search** across the published surface.
- **Public/private publication control**: publish/unpublish or deploy/visibility toggles; hidden versions; private docs with IdP/SSO-backed access (Mintlify auth, Realm access control, ReadMe hidden versions + enterprise users).
- **Endpoint-level enrichment**: injecting custom content, metadata, examples into generated pages (Mintlify x-mint content/metadata; ReadMe per-group docs; spec extensions in Redocly).
- **Documentation analytics**: views, visitors, search terms, feedback (ReadMe, Mintlify, Realm).

### L2 — Variant / Optional Structure

- **Substrate breadth**: OpenAPI-centric vs multi-spec (AsyncAPI, GraphQL, SOAP/WSDL) vs collection-derived (Postman).
- **Delivery posture**: hosted SaaS portal vs docs-as-code static toolchain (CLI + CI + static export) vs embeddable open-source renderer (Swagger UI, Redoc CE as an npm/dist component).
- **Scope posture**: API-reference-centric product (ReadMe) vs full developer-portal platform where the reference is one section (Mintlify, Realm) — a gradient toward Developer Documentation Portal.
- **Authoring philosophy**: hosted visual editor (ReadMe, Reunite editor) vs git-based MDX/Markdoc files (Mintlify, local Reunite) vs form-based endpoint authoring without a spec (ReadMe API Designer).
- **Personalization**: injecting the reader's own API keys/server variables into the docs and console (ReadMe personalized docs; Mintlify playground auth groups and prefills).
- **Mock server / response simulation** in the docs context (Redocly Replay; cf. design platforms' mocks).
- **Governance**: docs style-guide linters (ReadMe linter; Redocly CLI lint for specs).
- **Enterprise program machinery**: organizations, roles, SSO, publish-approval gates (Postman Community Manager), multi-project groups, end-user access management.
- **AI readiness layer**: Ask AI surfaces, MCP servers exposing docs to agents, llms.txt/agent-readable exports, AI-assisted authoring and review (ReadMe, Mintlify, Redocly) — common across current products but new; strength of "standard" unclear yet.
- **Spec distribution**: downloadable spec files from the docs (Mintlify download-spec option with explicit security warning).

### L3 — Vendor-specific (kept out of the final document)

- ReadMe "My Developers" (correlating docs usage with API traffic), API Designer as a productized authoring surface, `rdme` CLI name, "MDXish".
- Mintlify Index REST API, scraper package, automations/agent-job API, static-export API, `.mintlifysite.com` subdomains, `x-mint`/`x-hidden`/`x-group` extension names.
- Redocly product-family naming (Reunite, Realm, Revel, Reef, Respect, Replay) and the dogfooded "this website runs entirely on Realm" posture.
- Postman Run in Postman button, Postman API Network discovery, documenter.getpostman.com URLs, collection "CURRENT" version semantics.
- ReadMe versioning specifics ("semver-ish" naming flexibility, plan-gated version counts), Global Reusable Content enterprise gating.
- Swagger UI distribution flavors (swagger-ui vs swagger-ui-dist vs swagger-ui-react), Scarf analytics.

## Vendor-specific Findings (summary)

The graders above; also worth noting: only Postman showed an explicit **publish-approval workflow** (enterprise role gates public release) — treated as an enterprise variant, not a Type behavior. Only ReadMe showed **doc-version forking as full project forks with per-version visibility** — the canonical capability is "readers can select the docs version matching their integration," realized differently elsewhere.

## Rejected Findings

- "API documentation platforms are OpenAPI-rendering tools" — rejected as definition. Postman derives reference from collections; ReadMe's API Designer builds references without a spec; Mintlify supports hand-written pages. OpenAPI rendering is the dominant implementation, not the invariant (anti-overfitting rule).
- "Try-it-out is defining" — rejected: Redoc CE and classic static references lack it; the Type is recognizable without it.
- "Docs versioning is defining" — rejected: Swagger UI and Postman published docs lack it; single-version products remain clearly in-Type.
- "Guides/tutorials are defining" — rejected: reference-only deployments (Swagger UI, Redoc CE) remain in-Type.
- "The docs platform authors the API contract" — rejected: authoring the contract is the design platform's loop; docs platforms host *descriptions and reference*, and contract authoring inside them (API Designer) is a gradient case, flagged below.

## Boundary Findings

1. **vs API Design Platform** (processed leaf): the design platform's central artifact is the machine-readable contract with authoring + validation as the loop; the docs platform's central artifact is the rendered reference with publication as the loop. Structural tests: remove the published consumer surface → a design platform remains; remove contract authoring/validation → a docs platform remains. Gradient cases: Stoplight and SwaggerHub publish reference from the contract they author (design side reaching downstream); ReadMe's API Designer authors endpoints inside a docs product (docs side reaching upstream). The two capabilities coexist in one product without collapsing the Types — same pattern as the workbench/design boundary recorded earlier.
2. **vs Developer Documentation Portal** (separate directory leaf): center-of-gravity difference. The docs platform centers the API interface reference bound to a definition; a developer documentation portal centers the broader developer-docs corpus (quickstarts, SDK guides, product reference) where an API reference is one section. Mintlify and Realm sit on the gradient (full docs sites including API reference); ReadMe sits on the reference-centric pole. Both leaves exist in the directory; the distinction is held on the central artifact, but the products visibly span both — flagged for joint review.
3. **vs API Development Workbench** (processed leaf): the try-it console embedded in docs is workbench capability embedded at the reading surface. The docs loop is publish → consume; the workbench loop is compose → send → inspect → keep. Postman demonstrates the relation explicitly: documentation is a byproduct of the collection, and the Run in Postman button hands the reader from the docs surface into the workbench.
4. **vs API Management Platform / Gateway Console**: management governs runtime APIs (deployment, policies, analytics over traffic); the docs platform describes the interface for consumers. Portals generated under management platforms are a packaging variant of this Type's output, not a different center.
5. **vs Help Center / Knowledge Base / Product Documentation Portal**: article-centric support/self-service content vs endpoint-centric reference derived from a definition. The consumer audience and structure differ even when both are "documentation."
6. **Taxonomy observation**: the directory lists both API Documentation Platform and Developer Documentation Portal under §12. Research supports both as distinct centers of gravity, but the market is converging on products that span both (Mintlify, Realm). Boundary maintained on the central-artifact test; joint review recommended when Developer Documentation Portal is processed.

## Uncertainties

- Stoplight's operational documentation was never directly reachable (JS-only shell; not re-attempted this pass) — its role is posture-level boundary evidence only.
- Redocly Realm's versioning machinery: spec-level organization was observed (OpenAPI/AsyncAPI/GraphQL/WSDL pages, versioned via naming); whether Realm offers doc-fork-style version objects like ReadMe's was not confirmed. The final document therefore describes versioning capability generically, not per-product.
- Mintlify/ReadMe current-generation AI capabilities move quickly; observations are dated 2026-09-06 and treated as a moving layer.
- Older-generation hosted docs platforms (Apiary-era) were not sampled; the historical check rests on Swagger UI (2011) and WSDL/SOAP support (Redocly) instead. The L0 was deliberately kept small enough that this gap does not threaten the definition.
- Plan-gated features (ReadMe version counts, enterprise analytics) were observed but no plan/price specifics are asserted anywhere.

## Final Synthesis

An API Documentation Platform is software whose central artifact is the **published, navigable reference documentation of an API's interface** — endpoints, parameters, request/response formats, errors — maintained against a structured definition of that API (machine-readable specification, request collection, or structured authoring surface) and delivered to the API's consumers as a documentation surface that stays current as the API changes.

Around that core, mature products add the interactive try-it console, multi-language code samples, guides beside the reference, sync machinery from the definition source, doc versioning, branding, search, access control, and analytics. The market's dominant implementation is OpenAPI-driven; the Type is broader than that implementation. The Type sits downstream of the API Design Platform (which authors the contract), adjacent to the Developer Documentation Portal (which centers the wider docs corpus), and intermittently hosts embedded workbench capability (the try-it console).
